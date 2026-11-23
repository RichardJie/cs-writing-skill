# Agent Knowledge 真源说明

这个目录是个人 Agent Skills 的本地真源。

## GitHub 发布范围

本地目录可能包含大量个人 skills。当前默认 Git 发布范围只开放一个中文写作 skill：

- `skills/zh-humanizer-literary`

以下内容默认保持私有，不进入公开仓库：

- 原始语料和私有风格笔记
- 任何个人或品牌专属 skills
- 其他本地个人 skills
- 原始表格、客户资料、商业策略、定价、现金流和内部复盘

以后如果要发布其他技能，需要明确取消忽略，并先做脱敏审计。

## 目录结构

- `skills/`：canonical skill source。长期维护 `SKILL.md`、references、assets 等都在这里。
- `knowledge/`：辅助笔记、示例、参考资料和可复用素材。
- `scripts/`：知识库维护脚本。
- `archive/`：迁移备份和被替换的宿主入口。

## 宿主入口

Codex、Claude 和其他宿主目录只作为入口，不作为长期真源：

- `~/.codex/skills/<name>` 链接到 `/Users/dahebao/Documents/Agent-Knowledge/skills/<canonical-name>`
- `~/.claude/skills/<name>` 链接到同一 canonical skill
- `~/.agents/skills/<name>` 在适用时也链接到同一 canonical skill

不要在宿主目录里长期维护 skill 逻辑。修改应回到 `skills/` 下的 canonical source。

## 历史别名

这些历史名称保留为宿主入口，但指向同一个 canonical source：

- `iOS-APP-developer` -> `developing-ios-apps`
- `nuwa-skill` -> `huashu-nuwa`
- `paul-graham-skill` -> `paul-graham-perspective`

`steve-jobs-skill` 和 `steve-jobs-perspective` 暂时保留为不同技能，因为它们的 `SKILL.md` 内容不同。

## 备份

迁移备份路径记录在 `.last-migration-archive`。

如果某个宿主不识别软链接 skills，可以从备份里的 `replaced-*` 文件夹恢复该宿主原目录，再升级宿主后重试。
