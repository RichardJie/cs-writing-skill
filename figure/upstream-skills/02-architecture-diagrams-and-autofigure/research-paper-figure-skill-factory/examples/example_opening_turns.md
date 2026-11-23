# Example Opening Turn - v2.0.5

This is the canonical factory first response when `start_confirmed: false`. It is `STARTUP_PLAN_ONLY (TEXT_ONLY)`. It must list S0, B1-B9, P1-P6, P6b, P6b-IMAGE, P6c, and P7-P9 individually and must not perform target-paper image generation.

For generated specialized skills, the first/startup response should also display already-saved subtype/style atlas boards when they are packaged in the skill. Displaying saved atlas images is allowed; calling Create image, `$imagegen`, or an image API for target-paper images is not.

## 当前执行计划

当前处于 S0：启动确认。本轮只展示流程，不做论文分析、不生成候选方案、不调用 Create image、`$imagegen` 或图像 API 生成目标论文图片。

| 编号 | 层级 | 回复类型 | 做什么 | 本步产物 |
|---|---|---|---|---|
| S0 | Startup | STARTUP_PLAN_ONLY (TEXT_ONLY) | 展示完整流程 | 启动计划 |
| B1 | Skill Builder | TEXT_ONLY | 定义目标图类和 skill 目标 | figure-class brief |
| B2 | Skill Builder | TEXT_ONLY | 制定语料和合法获取计划 | corpus plan |
| B3 | Skill Builder | TEXT_ONLY | 获取/整理 PDF 和 manifest | local corpus |
| B4 | Skill Builder | TEXT_ONLY | 提取 figure/caption/panel 证据 | evidence map |
| B5 | Skill Builder | TEXT_ONLY | 构建图类 taxonomy 和 atlas 覆盖 | taxonomy |
| B6 | Skill Builder | TEXT_ONLY | 生成保存 atlas 并转成 blueprint | atlas + blueprint |
| B7 | Skill Builder | TEXT_ONLY | 生成 skill 包 | skill package |
| B8 | Skill Builder | TEXT_ONLY | 测试和修补 skill | test report |
| B9 | Skill Builder | TEXT_ONLY | 锁定专项 skill | locked skill |
| P1 | Figure Production | TEXT_ONLY | 收集目标论文材料并展示 atlas | material status |
| P2 | Figure Production | TEXT_ONLY | 诊断图需求和子类型，展示参考/概念图 | subtype routing |
| P3 | Figure Production | TEXT_ONLY | 给出 4-6 个文字候选方案，通常 6 个 | text candidates |
| P4 | Figure Production | TEXT_ONLY | 设置第一轮方向多样候选图板 | diverse board brief |
| P5 | Figure Production | IMAGE_ONLY | 生成/展示方向差异尽量大的候选图 | first-round image candidates only |
| P6 | Figure Production | TEXT_ONLY | 回看第一轮候选图并选当前最佳方向 | first-round current best |
| P6b | Figure Production | TEXT_ONLY | 设置二轮论文局部最佳实践优化轴 | second-round setup |
| P6b-IMAGE | Figure Production | IMAGE_ONLY | 生成二轮局部优化变体图 | second-round variants only |
| P6c | Figure Production | TEXT_ONLY | 回看二轮变体并锁定最终方向 | final direction |
| P7 | Figure Production | TEXT_ONLY | 构建正式 image brief | final image brief |
| P8 | Figure Production | IMAGE_ONLY | 生成正式候选图/修订图 | formal images only |
| P9 | Figure Production | TEXT_ONLY | 诊断、caption、legend、正文衔接 | final text package |

## 默认推荐

先确认目标图类，进入 B1。生成专项 skill 后，后续具体制图会强制经过 P3 文字候选、P4/P5 方向多样的第一轮候选图、P6 当前最佳方向选择、P6b/P6b-IMAGE/P6c 论文局部二轮优化，再进入 P7 最终 prompt。

## 当前状态与产物

- **阶段:** Startup
- **当前步骤:** S0
- **当前回复模式:** STARTUP_PLAN_ONLY (TEXT_ONLY)
- **全部步骤与当前位置:** S0 [当前位置] -> B1 -> B2 -> B3 -> B4 -> B5 -> B6 -> B7 -> B8 -> B9 -> P1 -> P2 -> P3 -> P4 -> P5 -> P6 -> P6b -> P6b-IMAGE -> P6c -> P7 -> P8 -> P9
- **本轮新增产物:** 启动计划
- **待产物:** 目标图类定义、corpus/evidence、专项 skill、候选图桥接测试、概念/建模示例图测试、二轮优化测试
- **session 状态延续提醒:** 默认根据当前 session/history 自动延续状态。

## 下一步你可以这样问

1. `请使用 **research-paper-figure-skill-factory**，执行，根据当前状态，下一步执行：确认开始，我想生成一个论文 diagram 制图 skill。`
2. `请使用 **research-paper-figure-skill-factory**，根据当前状态，提供下一步提问建议。`
