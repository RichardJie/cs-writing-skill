import { z } from 'zod';
import { executeToolJsx } from '../tool-executor.js';
import { coordinateSystemSchema } from '../session.js';
import { DESTRUCTIVE_ANNOTATIONS } from './shared.js';

export const jsxCode = `
var preflight = preflightChecks();
if (preflight) { writeResultFile(RESULT_PATH, preflight); }
else {
  var params = readParamsFile(PARAMS_PATH);
  var coordSystem = params.coordinate_system || "document";
  var abRect = coordSystem === "artboard-web" ? getActiveArtboardRect() : null;
  var results = [], plans = [], seen = {}, invalid = 0;
  function normalizedContents(s) { return s.split(String.fromCharCode(10)).join(String.fromCharCode(13)); }
  function textSnapshot(item) {
    var snap = verifyItem(item, coordSystem, abRect);
    snap.position = {x:item.position[0], y:item.position[1], coordinate_system:"document"};
    snap.text_runs = [];
    var count = item.characters.length;
    for (var ci = 0; ci < Math.max(1, count); ci++) {
      var a = count ? item.characters[ci].characterAttributes : item.textRange.characterAttributes;
      var last = snap.text_runs.length ? snap.text_runs[snap.text_runs.length-1] : null;
      var font = a.textFont.name, size = a.size, baseline = a.baselineShift;
      if (last && last.font_name===font && last.font_size===size && last.baseline_shift===baseline) last.end=ci+1;
      else snap.text_runs.push({start:ci,end:count ? ci+1 : 0,font_name:font,font_size:size,baseline_shift:baseline});
    }
    return snap;
  }
  function changedFields(before, after) {
    var changed = [];
    if (before.contents !== after.contents) changed.push("contents");
    if (before.name !== after.name) changed.push("name");
    if (before.position.x !== after.position.x || before.position.y !== after.position.y) changed.push("position");
    if (jsonStringify(before.text_runs) !== jsonStringify(after.text_runs)) changed.push("text_attributes");
    return changed;
  }
  function verifyRequested(item, props, errors) {
    if (typeof props.contents === "string" && item.contents !== normalizedContents(props.contents)) errors.push("VERIFY_CONTENTS");
    if (typeof props.name === "string" && item.name !== props.name) errors.push("VERIFY_NAME");
    if (props.position) {
      var pos = webToAiPoint(props.position.x,props.position.y,coordSystem,abRect);
      if (Math.abs(item.position[0]-pos[0])>0.05 || Math.abs(item.position[1]-pos[1])>0.05) errors.push("VERIFY_POSITION");
    }
    var count = item.characters.length;
    for (var ci=0; ci<Math.max(1,count); ci++) {
      var font=props.font_name, size=props.font_size, baseline;
      var runs=props.character_runs || [];
      for(var ri=0;ri<runs.length;ri++) {
        var run=runs[ri];
        if(ci>=run.start && ci<run.end) {
          if(run.font_name) font=run.font_name;
          if(typeof run.font_size==="number") size=run.font_size;
          if(typeof run.baseline_shift==="number") baseline=run.baseline_shift;
        }
      }
      var a=count ? item.characters[ci].characterAttributes : item.textRange.characterAttributes;
      if(font && a.textFont.name!==font) { errors.push("VERIFY_FONT at character "+ci); break; }
      if(typeof size==="number" && Math.abs(a.size-size)>0.01) { errors.push("VERIFY_SIZE at character "+ci); break; }
      if(typeof baseline==="number" && Math.abs(a.baselineShift-baseline)>0.01) { errors.push("VERIFY_BASELINE at character "+ci); break; }
    }
  }
  // Validate the entire batch before any mutation, including all font lookups.
  for(var bi=0;bi<params.items.length;bi++) {
    var request=params.items[bi], props=request.properties, item=null;
    var result={uuid:request.uuid,status:"not_applied",success:false,errors:[],changed_fields:[]};
    var plan={request:request,props:props,item:null,font:null,runFonts:[],before:null};
    try {
      item=findItemByUUID(request.uuid); assertEditableText(item); plan.item=item;
      var nativeId=ensureUUID(item);
      if(seen[nativeId]) throw new Error("DUPLICATE_BATCH_OBJECT");
      seen[nativeId]=true; result.native_id=nativeId;
      plan.before=textSnapshot(item);
      if(props.font_name) plan.font=app.textFonts.getByName(props.font_name);
      var length=typeof props.contents==="string" ? normalizedContents(props.contents).length : item.characters.length;
      var runs=props.character_runs || [];
      for(var ri=0;ri<runs.length;ri++) {
        var run=runs[ri];
        if(run.end<=run.start || run.end>length) throw new Error("INVALID_CHARACTER_RANGE at index "+ri);
        plan.runFonts[ri]=run.font_name ? app.textFonts.getByName(run.font_name) : null;
      }
    } catch(e) { result.errors.push(String(e.message || e)); invalid++; }
    plans.push(plan); results.push(result);
  }
  var succeeded=0, stopped=false;
  if(invalid===0) {
    for(var bi=0;bi<plans.length;bi++) {
      var plan=plans[bi], item=plan.item, props=plan.props, result=results[bi];
      if(stopped) { result.errors.push("NOT_STARTED_AFTER_PREVIOUS_FAILURE"); continue; }
      try {
        if(typeof props.contents==="string") item.contents=normalizedContents(props.contents);
        if(typeof props.name==="string") item.name=props.name;
        if(plan.font) item.textRange.characterAttributes.textFont=plan.font;
        if(typeof props.font_size==="number") item.textRange.characterAttributes.size=props.font_size;
        var runs=props.character_runs || [];
        for(var ri=0;ri<runs.length;ri++) {
          var run=runs[ri];
          for(var ci=run.start;ci<run.end;ci++) {
            var a=item.characters[ci].characterAttributes;
            if(plan.runFonts[ri]) a.textFont=plan.runFonts[ri];
            if(typeof run.font_size==="number") a.size=run.font_size;
            if(typeof run.baseline_shift==="number") a.baselineShift=run.baseline_shift;
          }
        }
        if(props.position) item.position=webToAiPoint(props.position.x,props.position.y,coordSystem,abRect);
      } catch(e) { result.errors.push("APPLY_FAILED: "+String(e.message || e)); }
      try {
        result.verified=textSnapshot(item);
        result.changed_fields=changedFields(plan.before,result.verified);
        verifyRequested(item,props,result.errors);
        result.success=result.errors.length===0;
        result.status=result.success ? "verified" : (result.changed_fields.length ? "partial" : "not_applied");
      } catch(e) {
        result.errors.push("READBACK_FAILED: "+String(e.message || e)); result.status="needs_verification";
      }
      if(result.success) succeeded++;
      else stopped=true;
    }
  }
  writeResultFile(RESULT_PATH,{
    success:invalid===0 && succeeded===params.items.length,
    phase:invalid ? "preflight_rejected" : "applied",
    documentRef:currentDocumentReference(), coordinateSystem:coordSystem,
    requested:params.items.length,succeeded:succeeded,failed:params.items.length-succeeded,
    invalid:invalid,results:results
  });
}
`;

const characterRun = z.object({
    start:z.number().int().min(0), end:z.number().int().min(1),
    font_name:z.string().min(1).optional(), font_size:z.number().positive().optional(),
    baseline_shift:z.number().optional(),
}).strict();
const properties = z.object({
    position:z.object({x:z.number(),y:z.number()}).strict().optional(),
    contents:z.string().optional(), name:z.string().optional(),
    font_name:z.string().min(1).optional(), font_size:z.number().positive().optional(),
    character_runs:z.array(characterRun).optional(),
}).strict().refine(value=>Object.keys(value).length>0,'At least one property is required');

export function register(server) {
    server.registerTool('batch_modify_text',{
        title:'Batch Modify Text',
        description:'Preflight all target text frames, fonts and ranges before writing. Returns per-item verified, partial, not_applied or needs_verification status with actual text attributes. Never replays or rolls back a failed batch.',
        inputSchema:{items:z.array(z.object({uuid:z.string().min(1),properties}).strict()).min(1).max(200),coordinate_system:coordinateSystemSchema},
        annotations:DESTRUCTIVE_ANNOTATIONS,
    },async params=>{
        const response=await executeToolJsx(jsxCode,params,{heavy:true,resolveCoordinate:true});
        const value=JSON.parse(response.content[0].text);
        return {...response,isError:value.success===false};
    });
}
