# Office OpenXML Math (OMML) Syntax & DrawingML Integration Guide

This guide specifies the mathematical architecture for injecting native, editable **Office Math Markup Language (OMML)** formulas into PowerPoint presentation decks (`.pptx`).

---

## 1. OpenXML Math Architecture in PowerPoint

In Microsoft PowerPoint OpenXML (ECMA-376 and ISO/IEC 29500), mathematical formulas are embedded inside slide XML (`ppt/slides/slideN.xml`) as first-class DrawingML objects rather than static bitmap images or plain raw text.

### 1.1 Required XML Namespaces
Slide XML files containing math must declare the following namespaces at `<p:sld>` or within the math container:
- `xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"`
- `xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main"`
- `xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"`

### 1.2 DrawingML Math Wrappers

In DrawingML text bodies (`<p:txBody>`), math elements reside inside paragraph nodes (`<a:p>`) wrapped by the DrawingML 2010 Math extension tag `<a14:m>`:

#### Inline Math (`<m:oMath>`)
Used for inline equations embedded within regular text sentences:
```xml
<a:p>
  <a:r>
    <a:rPr lang="en-US" sz="1300"/>
    <a:t>where loss </a:t>
  </a:r>
  <a14:m xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main"
         xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
    <m:oMath>
      <m:sSub>
        <m:e><m:r><m:t>L</m:t></m:r></m:e>
        <m:sub><m:r><m:t>reg</m:t></m:r></m:sub>
      </m:sSub>
      <m:r><m:t> ≥ 0</m:t></m:r>
    </m:oMath>
  </a14:m>
  <a:r>
    <a:rPr lang="en-US" sz="1300"/>
    <a:t> is the penalty term.</a:t>
  </a:r>
</a:p>
```

#### Block / Display Math (`<m:oMathPara>`)
Used for standalone centered equations:
```xml
<a:p>
  <a:pPr algn="ctr"/>
  <a14:m xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main"
         xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
    <m:oMathPara>
      <m:oMath>
        <m:sSub>
          <m:e><m:r><m:t>L</m:t></m:r></m:e>
          <m:sub><m:r><m:t>total</m:t></m:r></m:sub>
        </m:sSub>
        <m:d>
          <m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr>
          <m:e><m:r><m:t>θ</m:t></m:r></m:e>
        </m:d>
        <m:r><m:t> = </m:t></m:r>
        <m:f>
          <m:fPr><m:type m:val="bar"/></m:fPr>
          <m:num><m:r><m:t>1</m:t></m:r></m:num>
          <m:den><m:r><m:t>N</m:t></m:r></m:den>
        </m:f>
        <m:nary>
          <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/></m:naryPr>
          <m:sub><m:r><m:t>i=1</m:t></m:r></m:sub>
          <m:sup><m:r><m:t>N</m:t></m:r></m:sup>
          <m:e>
            <m:sSub>
              <m:e><m:r><m:t>ℓ</m:t></m:r></m:e>
              <m:sub><m:r><m:t>i</m:t></m:r></m:sub>
            </m:sSub>
            <m:d>
              <m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr>
              <m:e><m:r><m:t>θ</m:t></m:r></m:e>
            </m:d>
          </m:e>
        </m:nary>
      </m:oMath>
    </m:oMathPara>
  </a14:m>
</a:p>
```

---

## 2. LaTeX to OMML XML Element Mapping Matrix

| LaTeX Mathematical Construct | LaTeX Syntax | OMML XML Tag | XML Structure |
|---|---|---|---|
| **Fraction** | `\frac{A}{B}` | `<m:f>` | `<m:f><m:fPr><m:type m:val="bar"/></m:fPr><m:num>A</m:num><m:den>B</m:den></m:f>` |
| **Subscript** | `x_i` | `<m:sSub>` | `<m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>` |
| **Superscript** | `x^2` | `<m:sSup>` | `<m:sSup><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup>` |
| **Sub-Superscript** | `x_i^2` | `<m:sSubSup>` | `<m:sSubSup><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSubSup>` |
| **Radical / Sqrt** | `\sqrt{x}` | `<m:rad>` | `<m:rad><m:radPr/><m:deg/><m:e><m:r><m:t>x</m:t></m:r></m:e></m:rad>` |
| **N-th Root** | `\sqrt[n]{x}` | `<m:rad>` | `<m:rad><m:radPr/><m:deg><m:r><m:t>n</m:t></m:r></m:deg><m:e><m:r><m:t>x</m:t></m:r></m:e></m:rad>` |
| **N-Ary Summation** | `\sum_{i=1}^N` | `<m:nary>` | `<m:nary><m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/></m:naryPr><m:sub><m:r><m:t>i=1</m:t></m:r></m:sub><m:sup><m:r><m:t>N</m:t></m:r></m:sup><m:e>...</m:e></m:nary>` |
| **N-Ary Product** | `\prod_{k=1}^K` | `<m:nary>` | `<m:nary><m:naryPr><m:chr m:val="∏"/><m:limLoc m:val="undOvr"/></m:naryPr><m:sub>...</m:sub><m:sup>...</m:sup><m:e>...</m:e></m:nary>` |
| **N-Ary Integral** | `\int_0^\infty` | `<m:nary>` | `<m:nary><m:naryPr><m:chr m:val="∫"/><m:limLoc m:val="subSup"/></m:naryPr><m:sub><m:r><m:t>0</m:t></m:r></m:sub><m:sup><m:r><m:t>∞</m:t></m:r></m:sup><m:e>...</m:e></m:nary>` |
| **Delimiters (Parens)** | `\left( X \right)` | `<m:d>` | `<m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/><m:grow m:val="1"/></m:dPr><m:e>X</m:e></m:d>` |
| **Delimiters (Brackets)** | `\left[ X \right]` | `<m:d>` | `<m:d><m:dPr><m:begChr m:val="["/><m:endChr m:val="]"/><m:grow m:val="1"/></m:dPr><m:e>X</m:e></m:d>` |
| **Delimiters (Braces)** | `\left\{ X \right\}` | `<m:d>` | `<m:d><m:dPr><m:begChr m:val="{"/><m:endChr m:val="}"/><m:grow m:val="1"/></m:dPr><m:e>X</m:e></m:d>` |
| **Delimiters (Norm)** | `\| X \|` | `<m:d>` | `<m:d><m:dPr><m:begChr m:val="‖"/><m:endChr m:val="‖"/></m:dPr><m:e>X</m:e></m:d>` |
| **Accent (Hat)** | `\hat{y}` | `<m:acc>` | `<m:acc><m:accPr><m:chr m:val="̂"/></m:accPr><m:e><m:r><m:t>y</m:t></m:r></m:e></m:acc>` |
| **Accent (Tilde)** | `\tilde{x}` | `<m:acc>` | `<m:acc><m:accPr><m:chr m:val="̃"/></m:accPr><m:e><m:r><m:t>x</m:t></m:r></m:e></m:acc>` |
| **Accent (Bar)** | `\bar{z}` | `<m:acc>` | `<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e><m:r><m:t>z</m:t></m:r></m:e></m:acc>` |
| **Accent (Vector)** | `\vec{v}` | `<m:acc>` | `<m:acc><m:accPr><m:chr m:val="⃗"/></m:accPr><m:e><m:r><m:t>v</m:t></m:r></m:e></m:acc>` |
| **Matrix / Array** | `\begin{matrix} a & b \\ c & d \end{matrix}` | `<m:m>` | `<m:m><m:mPr><m:baseJc m:val="center"/></m:mPr><m:mr><m:e>a</m:e><m:e>b</m:e></m:mr><m:mr><m:e>c</m:e><m:e>d</m:e></m:mr></m:m>` |
| **Bold Vectors** | `\mathbf{w}, \boldsymbol{\theta}` | `<m:r>` with bold | `<m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>w</m:t></m:r>` |
| **Blackboard Bold** | `\mathbb{R}, \mathbb{E}, \mathbb{N}` | `<m:r>` | `<m:r><m:t>ℝ</m:t></m:r>`, `<m:r><m:t>𝔼</m:t></m:r>` (Direct UTF-8) |
| **Calligraphic Font** | `\mathcal{L}, \mathcal{N}, \mathcal{D}` | `<m:r>` | `<m:r><m:rPr><m:scr m:val="script"/></m:rPr><m:t>L</m:t></m:r>` |
| **Named Operators** | `\min, \max, \arg\min, \log, \exp` | `<m:func>` / `<m:r>` | `<m:r><m:rPr><m:nor/></m:rPr><m:t>min</m:t></m:r>` |

> [!NOTE]
> **OpenXML N-Ary Operator Structure**: In OMML, n-ary operator characters (`∑`, `∫`, `∏`) are encoded inside the `<m:chr m:val="..."/>` XML attribute of `<m:naryPr>`, rather than as inner text of `<m:t>`. Automated XML validators must check attribute values for operator conformance.

---

## 3. Special Symbol & Greek Letter Mappings

All standard Greek letters and mathematical symbols are mapped directly to Unicode UTF-8 strings inside `<m:r><m:t>SYMBOL</m:t></m:r>`:

### 3.1 Greek Alphabet (Lowercase & Uppercase)
- Lowercase: `\alpha` $\rightarrow$ `α`, `\beta` $\rightarrow$ `β`, `\gamma` $\rightarrow$ `γ`, `\delta` $\rightarrow$ `δ`, `\epsilon` / `\varepsilon` $\rightarrow$ `ε`, `\zeta` $\rightarrow$ `ζ`, `\eta` $\rightarrow$ `η`, `\theta` $\rightarrow$ `θ`, `\iota` $\rightarrow$ `ι`, `\kappa` $\rightarrow$ `κ`, `\lambda` $\rightarrow$ `λ`, `\mu` $\rightarrow$ `μ`, `\nu` $\rightarrow$ `ν`, `\xi` $\rightarrow$ `ξ`, `\pi` $\rightarrow$ `π`, `\rho` $\rightarrow$ `ρ`, `\sigma` $\rightarrow$ `σ`, `\tau` $\rightarrow$ `τ`, `\upsilon` $\rightarrow$ `υ`, `\phi` / `\varphi` $\rightarrow$ `ϕ`, `\chi` $\rightarrow$ `χ`, `\psi` $\rightarrow$ `ψ`, `\omega` $\rightarrow$ `ω`.
- Uppercase: `\Gamma` $\rightarrow$ `Γ`, `\Delta` $\rightarrow$ `Δ`, `\Theta` $\rightarrow$ `Θ`, `\Lambda` $\rightarrow$ `Λ`, `\Xi` $\rightarrow$ `Ξ`, `\Pi` $\rightarrow$ `Π`, `\Sigma` $\rightarrow$ `Σ`, `\Phi` $\rightarrow$ `Φ`, `\Psi` $\rightarrow$ `Ψ`, `\Omega` $\rightarrow$ `Ω`.

### 3.2 Operators, Relations & Set Symbols
- Relations: `\le` $\rightarrow$ `≤`, `\ge` $\rightarrow$ `≥`, `\neq` $\rightarrow$ `≠`, `\approx` $\rightarrow$ `≈`, `\equiv` $\rightarrow$ `≡`, `\sim` $\rightarrow$ `∼`, `\propto` $\rightarrow$ `∝`, `\in` $\rightarrow$ `∈`, `\notin` $\rightarrow$ `∉`, `\subset` $\rightarrow$ `⊂`, `\subseteq` $\rightarrow$ `⊆`.
- Binary Ops: `\times` $\rightarrow$ `×`, `\cdot` $\rightarrow$ `·`, `\pm` $\rightarrow$ `±`, `\mp` $\rightarrow$ `∓`, `\circ` $\rightarrow$ `∘`, `\otimes` $\rightarrow$ `⊗`, `\oplus` $\rightarrow$ `⊕`.
- Arrows & Delimiters: `\to` / `\rightarrow` $\rightarrow$ `→`, `\leftarrow` $\rightarrow$ `←`, `\Rightarrow` $\rightarrow$ `⇒`, `\nabla` $\rightarrow$ `∇`, `\partial` $\rightarrow$ `∂`, `\infty` $\rightarrow$ `∞`, `\forall` $\rightarrow$ `∀`, `\exists` $\rightarrow$ `∃`.

---

## 4. XML Entity Escaping & Integrity Rules

When constructing text nodes inside `<m:t>` or `<a:t>`, raw XML reserved characters must be escaped:

| Character | Escaped XML Entity | Example in Math |
|---|---|---|
| `&` | `&amp;` | `<m:t>A &amp; B</m:t>` |
| `<` | `&lt;` | `<m:t>x &lt; y</m:t>` |
| `>` | `&gt;` | `<m:t>x &gt; 0</m:t>` |
| `"` | `&quot;` | `<m:t>&quot;test&quot;</m:t>` |
| `'` | `&apos;` | `<m:t>&apos;x&apos;</m:t>` |

---

## 5. Two-Phase Build & Injection Architecture

Because high-level PowerPoint generation libraries (`pptxgenjs`) write standard DrawingML text runs, native OMML insertion can be accomplished via a two-phase architecture or direct XML generation:

1. **Phase 1: Deck Layout & Placeholder Tagging (`build_deck.js`)**:
   - Math expressions are written as tagged text tokens:
     - Inline math: `{{MATH:\alpha + \beta = \gamma}}`
     - Display block math: `{{MATH_DISPLAY:\mathcal{L}(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^N \ell_i(\boldsymbol{\theta})}}`
   - PPTX is rendered to an intermediate build archive (`stage1_deck.pptx`).

2. **Phase 2: OpenXML XML Node Replacement (`latex_to_omml.py`)**:
   - Unpack PPTX archive in-memory via ZIP stream.
   - Scan all `ppt/slides/slide*.xml` files for regex pattern `\{\{MATH(?:_DISPLAY)?:(.*?)\}\}`.
   - Parse LaTeX payload into OMML ElementTree / XML string.
   - Replace parent `<a:r>` text run with `<a14:m><m:oMath>...</m:oMath></a14:m>`.
   - Ensure `xmlns:m` and `xmlns:a14` namespaces are properly registered.
   - Repackage `.pptx` archive and validate XML integrity.

---

## 6. Concrete Academic ML Formula Examples

### Example 1: Multi-Head Latent Attention (MLA) KV Compression
**LaTeX**:
`\mathbf{c}_t^{KV} = W^{DKV} \mathbf{h}_t, \quad \mathbf{k}_t^C = W^{UK} \mathbf{c}_t^{KV}, \quad \mathbf{v}_t^C = W^{UV} \mathbf{c}_t^{KV}`

**Target OMML XML**:
```xml
<a14:m xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main"
       xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSubSup>
      <m:e><m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>c</m:t></m:r></m:e>
      <m:sub><m:r><m:t>t</m:t></m:r></m:sub>
      <m:sup><m:r><m:t>KV</m:t></m:r></m:sup>
    </m:sSubSup>
    <m:r><m:t> = </m:t></m:r>
    <m:sSup><m:e><m:r><m:t>W</m:t></m:r></m:e><m:sup><m:r><m:t>DKV</m:t></m:r></m:sup></m:sSup>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>h</m:t></m:r></m:e>
      <m:sub><m:r><m:t>t</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t>,  </m:t></m:r>
    <m:sSubSup>
      <m:e><m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>k</m:t></m:r></m:e>
      <m:sub><m:r><m:t>t</m:t></m:r></m:sub>
      <m:sup><m:r><m:t>C</m:t></m:r></m:sup>
    </m:sSubSup>
    <m:r><m:t> = </m:t></m:r>
    <m:sSup><m:e><m:r><m:t>W</m:t></m:r></m:e><m:sup><m:r><m:t>UK</m:t></m:r></m:sup></m:sSup>
    <m:sSubSup>
      <m:e><m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>c</m:t></m:r></m:e>
      <m:sub><m:r><m:t>t</m:t></m:r></m:sub>
      <m:sup><m:r><m:t>KV</m:t></m:r></m:sup>
    </m:sSubSup>
  </m:oMath>
</a14:m>
```

### Example 2: Variational Auto-Encoder (VAE) Evidence Lower Bound (ELBO)
**LaTeX**:
`\mathcal{L}_{\text{ELBO}}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}) = \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})}[\log p_{\boldsymbol{\theta}}(\mathbf{x}|\mathbf{z})] - D_{\text{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) \,\|\, p(\mathbf{z}))`

**Target OMML XML Structure**:
Includes `<m:sSub>` for subscripted expectations, `<m:d>` brackets for expectations and KL divergence, and blackboard bold `<m:r><m:t>𝔼</m:t></m:r>`.
