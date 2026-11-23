# 字体渲染与导出修复

SVG 预览、PPTX 文本框和 PDF 渲染由不同环节处理。先区分问题，再修复对应环节：

| 现象 | 常见原因 | 处理 |
| --- | --- | --- |
| 中文缺字、方框、显示成错误字体 | 渲染器未发现中文字体，或静默替换 | 用下方脚本检测已安装字体并隔离配置后导出 |
| SVG 正常，PPTX 的长标题、中文日期或手工换行正文多出一行 | 导出器文本框宽度估算不足 | 检查 ppt-master 版本，按需应用兼容补丁，然后从源项目重新导出 |
| 本机正常，另一台电脑换行变化 | 目标电脑字体或 Office 渲染器不同 | 确认目标字体、预检实际幻灯片；同时提供检查过的 PDF |

模板保持 Arial / Microsoft YaHei 的字体设定，未分发或嵌入字体。PingFang SC 是 macOS 可用的后备；Linux 可安装 Noto Sans CJK SC。字体替换不能保证与原字体字宽完全相同。

## 1. 检测字体并导出 PDF（macOS / Linux）

需要 Python 3、LibreOffice 和 Fontconfig（`fc-list`、`fc-match`）。例如：

```bash
# macOS（Homebrew）
brew install fontconfig
brew install --cask libreoffice

# Debian / Ubuntu
sudo apt-get install libreoffice-impress fontconfig fonts-noto-cjk
```

在仓库根目录执行：

```bash
python3 scripts/render_pdf.py \
  "academic_group_meeting/exports/简约学术组会_版式示例.pptx" \
  --output-dir /tmp/ustc-ppt-preview
```

脚本会：

- 为本次进程生成临时 Fontconfig 配置，显式纳入系统与用户字体目录。
- 从支持中文的已安装字体中，依次选择 Microsoft YaHei、PingFang SC、Noto Sans CJK SC、Source Han Sans SC、WenQuanYi Micro Hei；找不到就报错，不把 `fc-match` 的静默后备当成字体已安装。
- 当选择后备字体时，仅在本次进程中将 Microsoft YaHei 映射到该字体，并打印中英文字体匹配结果。
- 使用独立 LibreOffice 用户配置导出 PDF，避免复用已启动实例而忽略环境设置。
- 在输出目录生成 PDF 和同名 `.font-rendering.json` 诊断记录。已有 PDF 默认不覆盖，需要覆盖时加 `--overwrite`。

明确指定已安装字体或 LibreOffice 路径：

```bash
python3 scripts/render_pdf.py /path/to/report.pptx \
  --output-dir /path/to/preview \
  --cjk-font "PingFang SC" \
  --soffice /Applications/LibreOffice.app/Contents/MacOS/soffice
```

脚本不安装字体，不修改 PPTX，也不修改全局字体配置。诊断记录是 Fontconfig 的匹配结果，实际 PDF 仍需目视检查；Windows 请在 PowerPoint 中确认字体后使用其 PDF 导出功能。

## 2. ppt-master 6.8.0 文本宽度兼容补丁

补丁位于 [`patches/ppt-master-6.8.0/preserve-text-width.patch`](../patches/ppt-master-6.8.0/preserve-text-width.patch)，适用于本次验证的 6.8.0 源码。它修复两处导出宽度估算：

1. preserve 模式的多行文本沿用单行文本已有的宽度余量，避免保留的手工换行再次被渲染器折行。
2. 含中文的文字 run 为全角引号与中英／数字边界增加针对性余量。纯英文引号不增加该项余量。

reflow 段落继续使用原始换行约束；显式导入的精确文本框尺寸保持原样。补丁不改变字体、字号或文字内容，也不对全部文本框统一加宽。跨独立 run 的混排边界尚未单独处理。

**只在安装版本匹配且预检通过时应用。** 更新版本可能已修复此问题或改动实现；不要强制套用。下面使用 `git apply`，目标目录无需是 Git 仓库：

```bash
# 在本仓库根目录执行，改为实际 ppt-master 安装位置。
PPT_MASTER_DIR="/你的绝对路径/ppt-master"
FONT_PATCH="$(pwd)/patches/ppt-master-6.8.0/preserve-text-width.patch"

# 先预检；失败时停止，不继续应用。
git -C "$PPT_MASTER_DIR" apply --check "$FONT_PATCH" && \
  git -C "$PPT_MASTER_DIR" apply "$FONT_PATCH"
```

补丁重复应用会失败。可用 `git -C "$PPT_MASTER_DIR" apply --reverse --check "$FONT_PATCH"` 判断当前源码是否已包含同一补丁；若正向和反向预检均失败，应人工比较版本。

应用后，在已装好 ppt-master 依赖的环境中运行其相关回归测试：

```bash
python3 -m unittest discover \
  -s "$PPT_MASTER_DIR/scripts/tests" -p 'test_preserved_text_width.py'
python3 -m unittest discover \
  -s "$PPT_MASTER_DIR/scripts/tests" -p 'test_text_baseline.py'
python3 -m unittest discover \
  -s "$PPT_MASTER_DIR/scripts/tests" -p 'test_text_measure.py'
```

随后按 ppt-master 的正常流程重新运行项目的 final SVG 质量检查并导出 PPTX，再用本仓库脚本生成 PDF 检查。补丁不会自动修改既有 PPTX，包括仓库中此前发布的示例文件。

如需撤销，仅在反向预检成功时执行：

```bash
git -C "$PPT_MASTER_DIR" apply --reverse --check "$FONT_PATCH" && \
  git -C "$PPT_MASTER_DIR" apply --reverse "$FONT_PATCH"
```

ppt-master 升级可能覆盖本地修改；升级后先检查新版行为，再决定是否仍需要补丁。补丁按同目录 [MIT 许可](../patches/ppt-master-6.8.0/LICENSE) 分发，模板许可不变。

## 3. 交付前检查

优先检查中文日期、带中文引号的长标题、中英数字混排、多行正文以及左右边界附近的文字。检查字体、意外换行、文字遮挡和缺字；渲染成功或 SVG 质量检查通过都不能替代实际排版检查。

本仓库脚本的回归测试：

```bash
python3 -m unittest discover -s tests -v
```

本次验证环境为 macOS + LibreOffice + Fontconfig：仓库脚本的 5 项测试、导出器的 48 项相关测试均通过；补丁在独立目录中的预检、应用与撤销通过；10 页模板示例与 32 页中文汇报均完成 PDF 导出，并检查了示例页面及汇报中的标题、日期和正文。另验证了缺少指定字体时报错、已有 PDF 默认不覆盖。Linux 和 Windows 的实际排版尚未在本次验证中覆盖。
