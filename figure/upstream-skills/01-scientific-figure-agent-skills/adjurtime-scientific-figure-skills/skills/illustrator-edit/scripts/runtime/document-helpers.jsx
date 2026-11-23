// illustrator-edit: native-object-id and same-execution document binding
function ensureUUID(item) {
  var id = "";
  try { id = item.uuid; } catch(e) {}
  if (typeof id !== "string" || !id.length) {
    throw new Error("OBJECT_ID_UNAVAILABLE: native Illustrator object ID is unavailable; no note was changed");
  }
  return "native:" + id;
}

function findItemByUUID(id) {
  var doc = app.activeDocument;
  if (id.indexOf("native:") === 0) {
    try { return doc.getPageItemFromUuid(id.substring(7)); }
    catch(e) { return null; }
  }
  // Accept an old note-based ID only when it identifies exactly one object.
  var match = null;
  var nativeSeen = {};
  function visit(container) {
    for (var i = 0; i < container.pageItems.length; i++) {
      var item = container.pageItems[i];
      var nativeId = ensureUUID(item);
      if (nativeSeen[nativeId]) continue;
      nativeSeen[nativeId] = true;
      var note = "";
      try { note = item.note || ""; } catch(e) {}
      if (extractUUIDFromNote(note) === id) {
        if (match) throw new Error("AMBIGUOUS_OBJECT_ID: multiple objects share the legacy ID; read fresh native IDs");
        match = item;
      }
      if (item.typename === "GroupItem") visit(item);
    }
    if (container.typename === "Layer") {
      for (var sli = 0; sli < container.layers.length; sli++) visit(container.layers[sli]);
    }
  }
  for (var li = 0; li < doc.layers.length; li++) visit(doc.layers[li]);
  return match;
}

function currentDocumentReference() {
  var doc = app.activeDocument;
  try { return doc.fullName.fsName; }
  catch(e) { return "unsaved:" + doc.name; }
}

function checkExpectedDocument(expected) {
  if (!expected) return null;
  if (app.documents.length === 0) {
    return {error:true, message:"DOCUMENT_MISMATCH: no document is open; no action was performed"};
  }
  var actual = currentDocumentReference();
  if (expected.indexOf("unsaved:") !== 0) expected = (new File(expected)).fsName;
  if (actual !== expected) {
    return {error:true, message:"DOCUMENT_MISMATCH: active document differs from expected_document; no action was performed", expected:expected, actual:actual};
  }
  if (expected.indexOf("unsaved:") === 0) {
    var matches = 0;
    for (var di = 0; di < app.documents.length; di++) {
      var candidate = app.documents[di];
      try { var savedPath = candidate.fullName.fsName; }
      catch(e) { if ("unsaved:" + candidate.name === expected) matches++; }
    }
    if (matches !== 1) return {error:true, message:"DOCUMENT_MISMATCH: unsaved document name is ambiguous"};
  }
  return null;
}

function assertEditableText(item) {
  if (!item) throw new Error("OBJECT_NOT_FOUND");
  if (item.typename !== "TextFrame") throw new Error("OBJECT_TYPE_MISMATCH: expected TextFrame");
  if (item.editable === false) throw new Error("OBJECT_NOT_EDITABLE");
  var parent = item;
  while (parent && parent.typename !== "Document") {
    if (parent.locked === true) throw new Error("OBJECT_LOCKED");
    if (parent.hidden === true || (parent.typename === "Layer" && parent.visible === false)) throw new Error("OBJECT_HIDDEN");
    parent = parent.parent;
  }
}
