# 单页约 10 分钟首次通过闸门

## 适用范围

普通单页学术框图、技术路线图、研究框架图和 Hybrid Reconstruction 参考图复刻任务，在参数或骨架确认后使用本流程。质量门槛不因时间目标降低；如果第一次合并审查发现真实阻断项，则暂停 10 分钟目标，执行一次集中修正和一次定向审查。

## 时间预算

| 时间 | 工作 |
|---|---|
| 0–2 分钟 | 同时完成运行时预检、源图分区、对象/文字/连接器/颜色账本 |
| 2–7 分钟 | 使用组件函数一次构建全部可编辑对象；在内存中完成保存前四闸门 |
| 7–9 分钟 | 保存唯一权威 PPTX，运行结构脚本与一次 PowerPoint 原生合并审计 |
| 9–10 分钟 | 查看同一原生渲染；零阻断则立即交付 |

不得在任务中临时重写 PowerPoint 原生审计程序。使用 `scripts/audit_powerpoint_native.ps1`、连接器审计、视觉覆盖审计和 OOXML 几何验证脚本；同一次 PowerPoint 会话同时取得原生渲染和对象审计结果。

## 四份权威账本

首次构建前冻结以下内容；所有后处理和审计都读取同一份数据，不得重新手写对象名、中文文本或坐标：

1. **对象账本**：稳定对象名、页码、对象类型、语义图层、预期对象数。
2. **文字账本**：稳定对象名与完整 Unicode 文本；标点、空格和换行均视为内容。
3. **连接器账本**：源对象、目标对象、真实锚点或白名单代理锚点、方向、共轴约束和头部。
4. **视觉账本**：所有闭合区域、底板、标题条和容器的填充模式、填充色、线色、透明度及文字色。

PowerShell 后处理脚本不得内嵌中文可见文本。中文及其他非 ASCII 文本只能从显式 UTF-8 解码的 JSON 文字账本读取；脚本本身保持 ASCII，或在确有必要时使用 Unicode 码点构造。禁止依赖 Windows PowerShell 5.1 的默认脚本代码页。

## 首次保存前四闸门

### 1. 文字与编码闸门

- 将全部独立文字对象与文字账本逐对象、逐 Unicode 字符比较。
- 检查文本实际边界与有效文本框尺寸；标题、符号和单字符文本也必须检查，禁止把“+”“−”等短文本排除。
- 检查 `U+FFFD`、空文本、非预期替换、孤立标点、孤字行和异常换行。
- 任何不一致都在首次保存前修正。不得为了改一个标点而在 PowerShell 脚本中重新赋值整段中文。

### 2. 图层闸门

- 生成完全部对象后，按对象账本显式建立最终相对 Z 序：`background < path < node < complex_image < icon < text`。
- 创建顺序不能作为图层证明。读取每个对象的最终 Z 序，执行全局相对关系检查；`layer_violation_count` 必须为 `0`。
- 背景可以绝对置底；路径禁止绝对置底。连接器位于背景之上、节点之下。

### 3. 连接与共轴闸门

- 创建直连接器前按账本验证水平中心轴或垂直中心轴差 `≤ 0.1 pt`。
- 连接后再次从最终对象读取端点和相连对象身份；两端必须连接到预期真实对象或白名单代理锚点。
- `unconnected_endpoint_count`、`anchor_target_mismatch_count`、`non_axis_aligned_straight_connector_count` 均须为 `0`。

### 4. 颜色与完整性闸门

- 视觉账本必须在构建前完成，不得等首次渲染后再回忆颜色和填充。
- 所有对象、区域底色、文字、路径和复杂图片层的预期数与实际数必须一致。
- `expected_object_count = checked_object_count`，且颜色/填充问题数必须为 `0`。

四个闸门全部通过后才允许首次保存完整 PPTX。闸门失败属于构建阶段，不消耗审查次数；先在生成脚本或内存模型中修正。

## PowerPoint 原生合并审计

生成 `native-audit-manifest.json`，至少包含：

```json
{
  "slide_index": 1,
  "render_width": 1440,
  "render_height": 1080,
  "expected_slide_count": 1,
  "expected_shape_count": 1,
  "expected_image_count": 0,
  "expected_connector_count": 0,
  "require_full_registry": true,
  "objects": [{"name": "BG_PAGE", "layer": "background"}],
  "axis_constraints": [],
  "expected_text": [{"name": "TXT_TITLE", "text": "标题"}]
}
```

运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit_powerpoint_native.ps1 `
  -PresentationPath <权威PPTX> `
  -ManifestPath <native-audit-manifest.json> `
  -OutputDirectory <审计目录>
```

该脚本一次性完成：精确路径与只读状态验证、原生渲染、对象计数、对象注册覆盖、全局语义图层、原生连接器端点、共轴约束、文本 Unicode 回读和文本溢出检查。对象账本中每个 `text` 对象都必须在 `expected_text` 中有唯一条目；不得把未注册对象、漏登记文字或 `null/not_checked` 当作通过。

颜色/填充和连接目标身份继续分别由 `audit_hybrid_visual_coverage.py` 与 `audit_connector_target_identity.py` 核对；三项审计读取首次构建生成的同一批账本，不再临时创建另一套近似规则。

## 集中修正防回归

第一次合并审查发现问题时：

1. 先汇总全部问题和受影响对象，生成一份 UTF-8 修正清单。
2. 在同一可写 PowerPoint 会话中一次修改；禁止把中文修正文本写进临时 `.ps1` 字面量。
3. 保存前读取所有已修改对象，与对象、文字、连接器和视觉账本重新比较。
4. 如果修改涉及文字、图层、框体位置、颜色、连接器或页面尺寸，同时复核四个首次保存前闸门。
5. 仅当修正清单逐项回读一致后保存一次。
6. 第二次定向审查使用同一个原生审计脚本；不再临时编写第三套审计逻辑。

如果修正脚本自身发生参数错误、编码错误、空 COM 对象或未保存异常，视为工具调用失败，不得把该次失败计为内容审查，也不得在未确认 PPTX 实际状态时继续修改。
