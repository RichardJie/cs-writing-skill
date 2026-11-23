import { AsyncLocalStorage } from 'node:async_hooks';
import { spawn } from 'node:child_process';
import { realpathSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import pLimit from 'p-limit';
import { z } from 'zod';

const context = new AsyncLocalStorage();
const localLimit = pLimit(1);
const noDocumentRequired = new Set(['open_document', 'create_document', 'set_workflow', 'set_illustrator_version']);
export function currentToolContext() { return context.getStore() || {}; }

export async function acquireExecutionLock() {
    const helper = fileURLToPath(new URL('./execution-lock.py', import.meta.url));
    const child = spawn('/usr/bin/python3', ['-B', helper], { stdio: ['pipe', 'pipe', 'pipe'] });
    let diagnostic = '';
    child.stderr.on('data', chunk => { diagnostic += chunk.toString(); });
    await new Promise((resolve, reject) => {
        child.once('error', reject);
        child.stdout.once('data', chunk => {
            if (chunk.toString().trim() === 'locked') resolve();
            else reject(new Error('Invalid execution lock response'));
        });
        child.once('exit', code => reject(new Error(diagnostic.trim() || `Execution lock exited (${code})`)));
    });
    return () => new Promise(resolve => {
        child.once('exit', resolve);
        child.stdin.end();
    });
}

function documentReference(value) {
    if (value === undefined) return undefined;
    if (value.startsWith('unsaved:') && value.length > 8) return value;
    if (!path.isAbsolute(value)) throw new Error('expected_document must be an absolute file path or an unsaved: reference from get_document_info');
    return realpathSync(value);
}

export function installDocumentGuards(server) {
    const register = server.registerTool.bind(server);
    server.registerTool = (name, config, handler) => {
        const requiresDocument = config.annotations?.readOnlyHint !== true && !noDocumentRequired.has(name);
        const referenceSchema = z.string().min(1).describe('Exact documentRef from get_document_info. Required for operations that modify, save, close, or export an existing document.');
        const guardedConfig = {
            ...config,
            inputSchema: {
                ...config.inputSchema,
                expected_document: requiresDocument ? referenceSchema : referenceSchema.optional(),
            },
        };
        return register(name, guardedConfig, (params, extra) => localLimit(async () => {
            if (extra?.signal?.aborted) throw new Error('Request cancelled before execution');
            const expectedDocument = documentReference(params?.expected_document);
            if (requiresDocument && !expectedDocument) throw new Error('expected_document is required');
            const release = await acquireExecutionLock();
            try {
                if (extra?.signal?.aborted) throw new Error('Request cancelled before execution');
                return await context.run({ expectedDocument, toolName: name }, () => handler(params, extra));
            } finally {
                await release();
            }
        }));
    };
}
