# Step 4 生产级细节检查清单

Step 4 是把 AI 初稿变成"你的图"的关键。**在交付/投稿前逐项核查**。任何一项漏掉，reviewer 都可能挑出来。

---

## ① 数据准确性（最重要，错了直接出局）

- [ ] **所有数值** 与正文 Table / Equation 一致（百分比、参数量、score、loss）
- [ ] **缩写大小写规范**：BERT、ResNet、Transformer 首字母规则；不要混用 GPT/Gpt
- [ ] **数学符号**：θ、Δ、α、Σ 等希腊字母用 italic serif，不是直立体；下标/上标位置正确（如 `m_t` 不是 `mt`）
- [ ] **公式与正文一致**：图里的 `f_enc: x_t → m_t` 和正文 Eq. (3) 的写法完全相同
- [ ] **方向箭头**：数据流向 / 时间流向 / 反馈方向不能搞反
- [ ] **图例（legend）** 颜色和图中颜色完全一致；图例中的简写在 caption 或正文有定义
- [ ] **单位**：百分比是 `%` 还是 `pp`；时间是 `ms` 还是 `s`；显存是 `GB` 还是 `GiB`
- [ ] **统计标记**：`±std`、`±sem`、`* p<0.05`、`** p<0.01` 都和方法描述一致
- [ ] **error bar / shading** 含义在 caption 里说明清楚

---

## ② 视觉规范（顶会/期刊基本功）

### 字体

- [ ] 主字体 **Times New Roman** 或期刊指定字体（NeurIPS / ACL 都可用 Times）
- [ ] 数学符号 **italic serif**（用 `\mathit{}` 或 LaTeX-style）
- [ ] 字号层级正确：
  - Panel label（(a)(b)(c)）：bold 12pt
  - Module title：bold 11pt
  - Body text / labels：10pt
  - Caption / annotation：italic 9pt
- [ ] **不要混用字体**（除非数学公式用专门 math font）
- [ ] **PDF 嵌入字体**：导出时勾选 "Embed all fonts"，subset 100%

### 颜色

- [ ] **配色 ≤ 4 种**（不算黑白灰）
- [ ] **每种颜色有语义**（蓝=输入 / 绿=正样本 / 红=输出 / 灰=baseline）
- [ ] **色盲友好**：避免红绿对比作为唯一区分；用 ColorBrewer / Viridis 调色板更稳
- [ ] **黑白打印可辨识**：用 `colorgrayscale` 工具检查，不能颜色一变灰就看不出区别
- [ ] **十六进制色值**全图统一，不要同色出现两个 hex（`#4A90E2` 和 `#4A91E1` 视觉一样但数据不一致）

### 风格

- [ ] **flat design**：白底、无阴影、无渐变、无 3D
- [ ] **线条粗细统一**：边框 1px，主箭头 1.5px，强调箭头 2px——分级要一致
- [ ] **箭头样式统一**：实线/虚线在全图有清晰语义（实线=数据流，虚线=可选 / 反馈）
- [ ] **icon 风格统一**：要么全 line icon，要么全 filled，不要混用
- [ ] **对齐**：模块边缘、文字基线、间距，用 grid 对齐而不是肉眼

---

## ③ 文件规范（投稿格式硬要求）

- [ ] **分辨率 300 DPI**（位图）或矢量（PDF/SVG/EPS）
- [ ] **宽度**：
  - 单栏 ≤ 8.5 cm（≈ 3.35 inch）
  - 双栏 ≤ 17.5 cm（≈ 6.9 inch）
  - 期刊版面：查 author guide，Nature 单栏 89mm / 双栏 183mm
- [ ] **格式**：
  - 顶会（NeurIPS/ICML/ACL）：PDF 矢量
  - 期刊（Nature/Science）：EPS 或 PDF
  - 投稿系统兼容性：Cell 系不接受 SVG，要 EPS
- [ ] **文件名**：`figure1_architecture.pdf` 这种 `figureN_<key>.ext` 格式
- [ ] **文件大小** < 期刊上限（通常 < 10 MB）
- [ ] **caption 不嵌进图里**——caption 写在正文里，图本身只有"Figure N: <title>"作为标题

---

## ④ Caption 规范

- [ ] 第一句话是图的标题（一句话讲清楚这图在干啥）
- [ ] 后续句子按顺序解释每个 panel：(a) ..., (b) ..., (c) ...
- [ ] 所有缩写在 caption 里**首次出现时**展开（即使正文已经定义过）
- [ ] Error bar / shading / `*` 含义说明
- [ ] 数据来源 / 实验设置（n=N seeds, dataset=...）

---

## ⑤ 版权 / 合规（投稿前必查）

- [ ] **AI 绘图披露**：查目标会议/期刊的 AI 政策
  - **NeurIPS 2025**：允许 AI 辅助，需要在 acknowledgments / disclosure 写明
  - **ICML 2025**：允许，但作者对内容完全负责
  - **ACL 2025**：允许 AI 辅助 figure，需在 limitations / ethics 提及
  - **Nature**：AI 不能列为作者；AI 生成内容需在 methods 中说明工具和用途
  - **Science**：禁止 AI 生成的图作为主图（截至 2025），仅可用于流程辅助

- [ ] **复刻参考图**：如果是基于他人论文的图改造
  - 大幅改变 + 重新生成 = OK，但建议在 caption 写 "Adapted from [ref]"
  - 直接复制布局 + 换内容 = 引用 [ref] + 致谢
  - 直接用别人的图 = 申请 permission（Springer / Elsevier / Wiley 都有授权流程）

- [ ] **数据 / 截图**：用了真实数据集要引用 dataset paper；用了别人的产品截图要确认 usage policy

---

## ⑥ 最后一遍 sanity check

- [ ] **缩小到投稿尺寸看一遍**：在 PDF reader 里缩到 50% / 100%，文字还看得清吗？箭头还分得清虚实吗？
- [ ] **黑白打印一份**：用打印机或 Acrobat "Print as image, grayscale" 模拟 reviewer 的纸质打印
- [ ] **手机看一遍**：很多 reviewer 在手机/iPad 上读 PDF，重要细节不能太小
- [ ] **找一个组里没参与的同事看一眼**："你能从这张图猜出我这篇做的是啥吗？" — 5 秒内说不出来，图就有问题
- [ ] **跟 abstract 对照**：图里讲的 story 和 abstract 一致吗？

---

## ⑦ 反模式（写完图回头查这些）

- ❌ 图里堆了 8 种颜色（reviewer：信息过载）
- ❌ 用了渐变 / 阴影 / 3D 效果（reviewer：不专业）
- ❌ 字号太小，缩到 50% 就糊（reviewer：印刷体验差）
- ❌ Times New Roman 和 Arial 混用（reviewer：审美粗糙）
- ❌ 数学符号用直立体（reviewer：不熟悉学术规范）
- ❌ Caption 只有标题没解释 panel（reviewer：图自身要 self-contained）
- ❌ 没有 caption / Figure 编号（投稿系统直接打回）
- ❌ AI 没改的"假数据"留在图里（如默认的 `lorem ipsum`、`Module X`、`Method A`）

---

## 快速版（30 秒过一遍）

如果 deadline 在即，至少过这 5 项：

1. 数值 / 缩写 / 公式 == 正文一致 ✓
2. 字体全 Times New Roman + 数学 italic ✓
3. 配色 ≤ 4 种、有语义、色盲友好 ✓
4. 单/双栏宽度合规 + 300 DPI 或矢量 ✓
5. 缩小到 100% 看清晰、AI 默认占位符全清掉 ✓
