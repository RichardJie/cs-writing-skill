# nature-fig-env

[English](README.md) | 简体中文

> 面向环境、气候与能源研究的清晰、克制、可审计的发表级科研绘图工作流。

`nature-fig-env` 是一个 Codex skill，服务于大气、环境、地球系统、地理空间、海洋、水文、生态、城市与能源系统研究。它不仅提供科学配色，还把数据含义、归一化、排版、可编辑矢量输出和质量审查整合为可复用流程，帮助团队稳定地产出适合投稿、组图与后续修改的科研图件。

每条自动检查都对应稳定的 rule ID，便于定位问题、复核修改并统一质量标准。

## 核心能力

- 根据变量的物理含义与统计结构选择 cmocean、ColorBrewer、viridis 等科学配色。
- 对异常、差值和有符号变化默认采用以科学中点（通常为 0）居中的发散色标。
- 对直接比较的图保持坐标范围、colorbar 范围、单位、类别颜色和图例顺序一致。
- 强制最终组图尺寸下所有必要文字不小于 13 pt。
- 每个子图单独输出，默认不添加 a、b、c 等 panel 编号，便于用户自行组图。
- 图例与 colorbar 独立输出，并强制生成可编辑 SVG/PDF。
- 从绘图源码、metadata 和实际 SVG/PDF 三个层面检查字号。
- 明确记录统计量、样本量 `n`、独立观测/实验单位和误差线或不确定性定义。

## 字体标准

- [FONT-01] 最终组图尺寸下，任何必要文字均不得小于 13 pt。
- 坐标轴和 colorbar 标签默认使用 15–17 pt。
- 刻度、图例、注释、地图标签与 inset 标签默认使用 13–15 pt。
- 可以适当放大字体，但必须逐张审查输出图，确保文字不超出图片边缘 [LAYOUT-03]。子图后续缩小时，应按缩放比例预先放大工作字号；不得通过缩小到 13 pt 以下来解决拥挤。

## 安装

可直接让 Codex 执行：

```text
Install the nature-fig-env skill from https://github.com/haohuresearch/nature-fig-env.git into my Codex skills directory. Validate the installed skill and tell me when it will be available.
```

安装后刷新或重启 Codex，可通过 `$nature-fig-env` 显式调用，也可在相关科研绘图任务中自动启用。

### 手动安装

macOS 或 Linux：

```bash
git clone https://github.com/haohuresearch/nature-fig-env.git ~/.codex/skills/nature-fig-env
python -m pip install -r ~/.codex/skills/nature-fig-env/requirements.txt
```

Windows PowerShell：

```powershell
git clone https://github.com/haohuresearch/nature-fig-env.git "$env:USERPROFILE\.codex\skills\nature-fig-env"
python -m pip install -r "$env:USERPROFILE\.codex\skills\nature-fig-env\requirements.txt"
```

## 快速审查

```bash
python scripts/audit_source_fonts.py plot.py --minimum-pt 13
python scripts/audit_figure.py figure.png figure.figure.json
python scripts/audit_vector_text.py figure.svg --minimum-pt 13
python scripts/audit_figure.py colorbar_family.png figure.figure.json --asset-role legend
```

规则 ID 的完整定义见 [`references/rule-registry.md`](references/rule-registry.md)，字体、版式与最终检查要求分别见 [`references/layout-typography.md`](references/layout-typography.md) 和 [`references/qa-checklist.md`](references/qa-checklist.md)。

## 个人参考图库

将有权保存和参考的优秀图件放入 `assets/reference-images/`，再生成 contact sheet：

```bash
python scripts/make_reference_contact_sheet.py assets/reference-images work/reference-contact-sheet.jpg
```

Skill 只提取字体层级、留白、线宽、配色逻辑、地图边框和图例位置等一般风格特征，不复制原图数据、标签、标识或具有独创性的图形内容。

## 配色参考

- [cmocean](https://matplotlib.org/cmocean/)
- [NASA GISS Panoply colorbars](https://www.giss.nasa.gov/tools/panoply/colorbars/)
- [ColorBrewer](https://colorbrewer2.org/)
- [viridis](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)
- [Scientific Colour Maps](https://www.fabiocrameri.ch/colourmaps/)
- [NCAR/NCL color tables](https://www.ncl.ucar.edu/Document/Graphics/color_tables.shtml)
- [Unidata MetPy colortables](https://unidata.github.io/MetPy/latest/api/generated/metpy.plots.ctables.html)
- [Generic Mapping Tools CPTs](https://docs.generic-mapping-tools.org/latest/cookbook/cpts.html)

## 许可证

本项目采用 MIT License，详见 [LICENSE](LICENSE)。
