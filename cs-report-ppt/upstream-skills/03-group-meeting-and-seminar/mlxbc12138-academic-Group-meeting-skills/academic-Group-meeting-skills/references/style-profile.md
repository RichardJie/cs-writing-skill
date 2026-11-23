# Reference Style Profile

Use this profile when no stronger user-provided template exists.

## Deck Geometry

- 16:9 widescreen, 13.333 x 7.5 in.
- Use Microsoft YaHei for all generated text.
- Caption text should be large enough to fill the right-side text column vertically. Increase font size, line spacing, and paragraph spacing before accepting large blank areas.
- Most content slides have a compact top header and a thin horizontal rule near y=0.72 in.
- Main visual area starts around y=0.9 in and ends around y=7.15 in.
- Keep margins near 0.25-0.35 in unless a figure needs full width.

## Slide Patterns

- Cover slide: use a horizontal crop of the PDF first page top region, including journal banner, English title, authors, and affiliations. Do not show the abstract/body text. Add the Chinese title plus `IF <value>` and the author school/institution below the crop.
- Default figure slide: place a large image on the left and caption/panel notes on the right. This should fill most of the screen and keep the explanation visually tied to the image.
- Very wide figure: place image across the upper/middle canvas, then put caption/panel notes below.
- Tall figure: place image on the left, caption boxes on the right.
- Multi-panel figure: place the combined figure crop large, then add figure-level caption plus separate nearby panel lines labeled `A:`, `B:`, `C:`, etc.
- Large composite figure: crop into panel groups and expand into multiple slides. Prefer larger text over preserving the whole figure on one slide when readability conflicts.
- Dense methods figure: keep figure large enough for labels; use shorter Chinese explanations rather than shrinking the image.

## Caption Voice

Preferred style:

```text
Fig. 2c 作者在 SARS-CoV-2 基因组上设计并标出了 9 组 LAMP 引物的位置。这些引物覆盖了 Orf1ab、N、E、Nsp3 等不同区域，用于筛选最快、最稳定的扩增靶区。
```

Use Chinese explanatory prose, not a literal caption dump. Preserve figure labels and technical terms.

For multi-panel captions, keep the first line as the figure-level message and then add short panel lines:

```text
Fig. 4 作者展示了二进制空间-光谱编码和腔室级解码策略。
A: 多通道读取同一批空间索引微腔，并把各通道阳性/阴性状态转成二进制码字。
B: 编码矩阵把不同二进制码字分配给不同靶标。
C: 原始荧光强度经过阈值化后拼接成激活模式，用于靶标判定。
```

## QA Checklist

- Slide 1 is a top-region first-page screenshot plus Chinese title, IF, and institution.
- Multi-panel figures include A/B/C/D panel explanations, not only a one-sentence figure summary.
- Figure order matches the article.
- Captions are near the relevant visual and do not overlap the image.
- Chinese text is readable at normal presentation zoom.
- No irrelevant journal logos, page numbers, author photos, or decorative icons were extracted as figures unless intentionally used.
- Long captions have been summarized to the experimental purpose and conclusion.
