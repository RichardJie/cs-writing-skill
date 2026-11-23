# 来源与第三方权利说明

## 原版与衍生模板

- 上游项目：[atomiechen/THU-PPT-Theme](https://github.com/atomiechen/THU-PPT-Theme)。
- 原版来源：v1 顶边 16:9；本仓库原 README 已记录此改编关系。
- 上游许可：[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)。[LICENSE](LICENSE) 保留该许可全文。
- 本仓库改编：将原版调整为 USTC 主题；新增 `academic_group_meeting` 工作区，重新组织论文组会页面、章节导航、设计规范、SVG 占位符与可编辑演示文稿示例。
- 模板与本仓库改编贡献依 CC BY-NC-SA 4.0 分享。请保留上游及本仓库署名、注明修改，并遵守非商业和相同方式共享条件。

建议在再分发说明中保留：

> 基于 liano3/ustc-ppt-theme，原版改编自 atomiechen/THU-PPT-Theme（v1 顶边 16:9）。模板依 CC BY-NC-SA 4.0 分享；本版本的修改：……

## 中国科学技术大学标识

`academic_group_meeting/images/ustc-emblem.png` 和 `ustc-wordmark.png` 来源于：

- [USTC Logo 资源页](https://jbyang1987.github.io/ustclogo/图片.html)

两项素材也出现在模板 SVG、PPTX 示例和预览图片中。学校名称、校徽和校名标识的相关权利归原权利人；本仓库的模板许可证不授予这些标识的额外权利。使用时请遵守学校的标识使用规范。本项目为个人整理分享，不代表学校官方发布或背书。

## 工具与字体

- [ppt-master](https://github.com/hugohe3/ppt-master) 用于模板制作、验证与导出。本仓库未打包完整引擎；`patches/ppt-master-6.8.0/preserve-text-width.patch` 包含针对该项目 6.8.0 的代码修改及回归测试，改动为 preserve 模式文本宽度余量、中文引号与混排边界余量。该补丁及其中的代码按 MIT 许可提供，上游版权为 Copyright (c) 2025–2026 Hugo He，许可全文保存在同目录的 `LICENSE`。模板的 CC BY-NC-SA 4.0 许可不替代补丁的 MIT 许可。
- 模板引用 Arial、Microsoft YaHei，以及用于 SVG 预览后备的 PingFang SC。字体文件未包含在本仓库中，字体的授权由其各自权利人规定。
