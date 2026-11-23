#!/usr/bin/env node
/**
 * build_deck.js
 * Production-grade Academic Paper Presentation Slide Deck Generator (16:9 widescreen).
 * 
 * Aesthetic Standards:
 * - Minimalist Academic Black & White / Grayscale Palette (default: academic_mono)
 * - Heavy Multi-Modal Visual Dominance: Figures, architecture diagrams & tables take center stage
 * - Dynamic OMML mathematical formula vertical spacing with zero overlap
 * - Native PPTX Table & Vector Flowchart Diagram Engines
 * - Clean responsive card grids with overflow & shrinkText protections
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const PptxGenJS = require('pptxgenjs');

// Parse CLI Arguments
const args = process.argv.slice(2);
let inputPath = '';
let configPath = '';
let figuresPath = '';
let outputPath = 'output/academic_presentation.pptx';
let themeName = 'academic_mono'; // Default: Minimalist Academic Black & White
let skipOmml = false;

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--input' && args[i + 1]) inputPath = args[++i];
  else if (args[i] === '--config' && args[i + 1]) configPath = args[++i];
  else if (args[i] === '--figures' && args[i + 1]) figuresPath = args[++i];
  else if (args[i] === '--output' && args[i + 1]) outputPath = args[++i];
  else if (args[i] === '--theme' && args[i + 1]) themeName = args[++i];
  else if (args[i] === '--no-omml') skipOmml = true;
  else if (args[i] === '--help' || args[i] === '-h') {
    console.log('Usage: node build_deck.js --input <data.json> [--config <config.json>] [--figures <meta.json>] --output <out.pptx> [--theme <name>] [--no-omml]');
    process.exit(0);
  }
}

if (!inputPath) {
  const defaultPath = path.join(__dirname, '../resources/sample_deck_input.json');
  const fixturePath = path.join(__dirname, '../tests/fixtures/sample_paper_data.json');
  if (fs.existsSync(defaultPath)) inputPath = defaultPath;
  else if (fs.existsSync(fixturePath)) inputPath = fixturePath;
  else {
    console.error('Error: --input JSON file is required.');
    process.exit(1);
  }
}

// Load Input JSON & Figures Metadata
const rawInput = fs.readFileSync(inputPath, 'utf8');
const deckData = JSON.parse(rawInput);

let figuresMetadata = {};
if (figuresPath && fs.existsSync(figuresPath)) {
  try {
    const rawFigs = fs.readFileSync(figuresPath, 'utf8');
    const parsedFigs = JSON.parse(rawFigs);
    if (parsedFigs.figures && Array.isArray(parsedFigs.figures)) {
      parsedFigs.figures.forEach(f => {
        figuresMetadata[f.id] = f;
      });
    } else if (typeof parsedFigs === 'object') {
      figuresMetadata = parsedFigs;
    }
  } catch (e) {
    console.warn(`[build_deck.js] Warning loading figures metadata: ${e.message}`);
  }
}

// Color Theme Defaults (Harmonized Minimalist Black & White Default + Conference Themes)
const THEMES = {
  academic_mono: {
    id: 'academic_mono',
    name: 'Academic Minimalist (Black & White)',
    primary: '000000',
    accent: '111827',
    secondary: '374151',
    bg: 'FFFFFF',
    background: 'FFFFFF',
    cardBg: 'FFFFFF',
    cardBorder: 'D1D5DB',
    cardHeaderBg: 'F9FAFB',
    headerText: '000000',
    bodyText: '1F2937',
    textPrimary: '000000',
    textSecondary: '374151',
    textMuted: '6B7280',
    calloutBg: 'F9FAFB',
    calloutBorder: '374151',
    calloutText: '000000',
    sideNoteBg: 'F9FAFB',
    sideNoteBorder: '374151',
    sideNoteAccent: '111827',
    sideNoteText: '000000',
    highlightBg: 'F3F4F6',
    highlightText: '000000',
    badgeBg: 'F3F4F6',
    badgeText: '111827'
  },
  mono: {
    id: 'mono',
    name: 'Pure Monochrome',
    primary: '000000',
    accent: '000000',
    secondary: '4B5563',
    bg: 'FFFFFF',
    background: 'FFFFFF',
    cardBg: 'FFFFFF',
    cardBorder: 'E5E7EB',
    cardHeaderBg: 'FAFAFA',
    headerText: '000000',
    bodyText: '18181B',
    textPrimary: '000000',
    textSecondary: '3F3F46',
    textMuted: '71717A',
    calloutBg: 'F4F4F5',
    calloutBorder: '18181B',
    calloutText: '000000',
    sideNoteBg: 'F4F4F5',
    sideNoteBorder: '18181B',
    sideNoteAccent: '000000',
    sideNoteText: '000000',
    highlightBg: 'F4F4F5',
    highlightText: '000000',
    badgeBg: 'F4F4F5',
    badgeText: '000000'
  },
  neurips: {
    id: 'neurips',
    name: 'NeurIPS (Midnight Navy)',
    primary: '0F2042',
    accent: '2563EB',
    secondary: '475569',
    bg: 'F8FAFC',
    background: 'F8FAFC',
    cardBg: 'FFFFFF',
    cardBorder: 'CBD5E1',
    cardHeaderBg: 'F8FAFC',
    headerText: '0F172A',
    bodyText: '334155',
    textPrimary: '0F172A',
    textSecondary: '475569',
    textMuted: '64748B',
    calloutBg: 'F8FAFC',
    calloutBorder: '334155',
    calloutText: '0F172A',
    sideNoteBg: 'EFF6FF',
    sideNoteBorder: '1D4ED8',
    sideNoteAccent: '2563EB',
    sideNoteText: '1E3A8A',
    highlightBg: 'EFF6FF',
    highlightText: '1E40AF',
    badgeBg: 'E0E7FF',
    badgeText: '3730A3'
  },
  icml: {
    id: 'icml',
    name: 'ICML (Emerald Teal)',
    primary: '004D40',
    accent: '0D9488',
    secondary: '334155',
    bg: 'F0FDFA',
    background: 'F0FDFA',
    cardBg: 'FFFFFF',
    cardBorder: 'CCFBF1',
    cardHeaderBg: 'F0FDFA',
    headerText: '064E3B',
    bodyText: '334155',
    textPrimary: '064E3B',
    textSecondary: '334155',
    textMuted: '64748B',
    calloutBg: 'F0FDFA',
    calloutBorder: '0F766E',
    calloutText: '134E4A',
    sideNoteBg: 'F0FDFA',
    sideNoteBorder: '0F766E',
    sideNoteAccent: '0D9488',
    sideNoteText: '134E4A',
    highlightBg: 'CCFBF1',
    highlightText: '115E59',
    badgeBg: 'D1FAE5',
    badgeText: '065F46'
  },
  cvpr: {
    id: 'cvpr',
    name: 'CVPR (Crimson Rose)',
    primary: '881337',
    accent: 'E11D48',
    secondary: '334155',
    bg: 'FFF1F2',
    background: 'FFF1F2',
    cardBg: 'FFFFFF',
    cardBorder: 'FFE4E6',
    cardHeaderBg: 'FFF1F2',
    headerText: '4C0519',
    bodyText: '334155',
    textPrimary: '4C0519',
    textSecondary: '334155',
    textMuted: '64748B',
    calloutBg: 'FFF1F2',
    calloutBorder: 'BE123C',
    calloutText: '881337',
    sideNoteBg: 'FFF1F2',
    sideNoteBorder: 'BE123C',
    sideNoteAccent: 'E11D48',
    sideNoteText: '881337',
    highlightBg: 'FFE4E6',
    highlightText: '9F1239',
    badgeBg: 'FCE7F3',
    badgeText: '9D174D'
  },
  iclr: {
    id: 'iclr',
    name: 'ICLR (Amethyst Violet)',
    primary: '4C1D95',
    accent: '7C3AED',
    secondary: '334155',
    bg: 'FAF5FF',
    background: 'FAF5FF',
    cardBg: 'FFFFFF',
    cardBorder: 'EDE9FE',
    cardHeaderBg: 'FAF5FF',
    headerText: '2E1065',
    bodyText: '334155',
    textPrimary: '2E1065',
    textSecondary: '334155',
    textMuted: '64748B',
    calloutBg: 'FAF5FF',
    calloutBorder: '6D28D9',
    calloutText: '4C1D95',
    sideNoteBg: 'FAF5FF',
    sideNoteBorder: '6D28D9',
    sideNoteAccent: '7C3AED',
    sideNoteText: '4C1D95',
    highlightBg: 'EDE9FE',
    highlightText: '5B21B6',
    badgeBg: 'F5F3FF',
    badgeText: '5B21B6'
  },
  kdd: {
    id: 'kdd',
    name: 'KDD (Bronze Amber)',
    primary: '78350F',
    accent: 'D97706',
    secondary: '334155',
    bg: 'FFFBEB',
    background: 'FFFBEB',
    cardBg: 'FFFFFF',
    cardBorder: 'FEF3C7',
    cardHeaderBg: 'FFFBEB',
    headerText: '451A03',
    bodyText: '334155',
    textPrimary: '451A03',
    textSecondary: '334155',
    textMuted: '64748B',
    calloutBg: 'FEF3C7',
    calloutBorder: 'B45309',
    calloutText: '78350F',
    sideNoteBg: 'FEF3C7',
    sideNoteBorder: 'B45309',
    sideNoteAccent: 'D97706',
    sideNoteText: '78350F',
    highlightBg: 'FEF3C7',
    highlightText: '92400E',
    badgeBg: 'FEF9C3',
    badgeText: '854D0E'
  }
};

const theme = THEMES[themeName.toLowerCase()] || THEMES.academic_mono;

// Initialize PPTX with custom widescreen 16:9 layout (13.333333 x 7.500 inches)
const pptx = new PptxGenJS();
pptx.defineLayout({ name: 'LAYOUT_16x9_WIDE', width: (40 / 3), height: 7.5 });
pptx.layout = 'LAYOUT_16x9_WIDE';
pptx.author = (deckData.meta?.presenter || 'Academic Presentation Agent').replace(/&/g, 'and');
pptx.company = (deckData.meta?.affiliation || 'AI Research Lab').replace(/&/g, 'and');
pptx.title = (deckData.meta?.title || 'Academic Paper Presentation').replace(/&/g, 'and');

// Slide Coordinate Standards (16:9 Canvas)
const CANVAS = {
  w: 13.333,
  h: 7.500,
  marginL: 0.600,
  marginR: 0.600,
  marginT: 0.350,
  headerH: 1.200,
  contentY: 1.650,
  contentH: 5.200,
  contentW: 12.133,
  footerY: 7.000,
  footerH: 0.350
};

/**
 * Adds standard slide header and footer chrome in minimalist academic styling
 */
function addSlideChrome(slide, slideIndex, totalSlides, section, badge, title, subtitle, citation) {
  // Tracker / Badge (Clean Dark Neutral)
  const badgeStr = (badge || section || 'ACADEMIC PRESENTATION').toUpperCase();
  slide.addText(badgeStr, {
    x: CANVAS.marginL,
    y: 0.25,
    w: 8.0,
    h: 0.20,
    fontSize: 9.5,
    fontFace: 'Arial',
    bold: true,
    color: theme.accent || '111827'
  });

  // Slide Number (Clean Muted Gray)
  slide.addText(`${slideIndex} / ${totalSlides}`, {
    x: CANVAS.w - CANVAS.marginR - 2.0,
    y: 0.25,
    w: 2.0,
    h: 0.20,
    fontSize: 9.5,
    fontFace: 'Arial',
    align: 'right',
    color: theme.textMuted || '6B7280'
  });

  // Main Title (22-26pt bold, crisp black, autoFit & shrinkText)
  slide.addText(title, {
    x: CANVAS.marginL,
    y: 0.48,
    w: CANVAS.contentW,
    h: 0.58,
    fontSize: 22,
    fontFace: 'Arial',
    bold: true,
    color: theme.headerText || '000000',
    shrinkText: true
  });

  // Subtitle / Question (14-15pt italic gray)
  if (subtitle) {
    slide.addText(subtitle, {
      x: CANVAS.marginL,
      y: 1.08,
      w: CANVAS.contentW,
      h: 0.34,
      fontSize: 14,
      fontFace: 'Arial',
      italic: true,
      color: theme.textSecondary || '4B5563',
      shrinkText: true
    });
  }

  // Elegant Hairline Divider Line
  slide.addShape(pptx.ShapeType.line, {
    x: CANVAS.marginL,
    y: 1.48,
    w: CANVAS.contentW,
    h: 0,
    line: { color: theme.cardBorder || 'E5E7EB', width: 1 }
  });

  // Footer Citation (Clean Gray)
  const footerText = citation || deckData.meta?.doi || deckData.meta?.url || `${deckData.meta?.title} (${deckData.meta?.conference || ''})`;
  slide.addText(footerText, {
    x: CANVAS.marginL,
    y: CANVAS.footerY,
    w: CANVAS.contentW - 3.0,
    h: CANVAS.footerH,
    fontSize: 10,
    fontFace: 'Arial',
    color: theme.textMuted || '6B7280'
  });
}

/**
 * Calculates card bounding boxes for all 7 responsive grid layout models
 */
function getGridLayout(layoutType, count) {
  const W = CANVAS.contentW; // 12.133"
  const H = CANVAS.contentH; // 5.200"
  const Y = CANVAS.contentY; // 1.650"
  const X = CANVAS.marginL;  // 0.600"

  if (layoutType === 'hero_header' || layoutType === 'hero_1col' || count === 1) {
    return [{ x: X, y: Y, w: W, h: H }];
  }

  if (layoutType === 'split_65_35' || layoutType === 'split_2col_65_35' || layoutType === 'figure_and_mechanism_60_40') {
    const gap = 0.300;
    const w1 = 7.700;
    const w2 = 4.133;
    if (count <= 2) {
      return [
        { x: X, y: Y, w: w1, h: H },
        { x: X + w1 + gap, y: Y, w: w2, h: H }
      ];
    } else {
      const leftCount = count - 1;
      const leftGap = 0.250;
      const leftH = (H - leftGap * (leftCount - 1)) / leftCount;
      const boxes = [];
      for (let i = 0; i < leftCount; i++) {
        boxes.push({
          x: X,
          y: Y + i * (leftH + leftGap),
          w: w1,
          h: leftH
        });
      }
      boxes.push({
        x: X + w1 + gap,
        y: Y,
        w: w2,
        h: H
      });
      return boxes;
    }
  }

  if (layoutType === 'quadrant_2x2' || layoutType === 'grid_2x2' || layoutType === 'grid_2col_2row') {
    const gapX = 0.300;
    const gapY = 0.250;
    const cardW = 5.916;
    const cardH = 2.475;
    return [
      { x: X, y: Y, w: cardW, h: cardH },
      { x: X + cardW + gapX, y: Y, w: cardW, h: cardH },
      { x: X, y: Y + cardH + gapY, w: cardW, h: cardH },
      { x: X + cardW + gapX, y: Y + cardH + gapY, w: cardW, h: cardH }
    ];
  }

  if (layoutType === 'asymmetric_2row' || layoutType === 'asymmetric_2_row') {
    const heroH = 2.300;
    const gapY = 0.200;
    const gapX = 0.300;
    const bottomH = 2.700;
    const bottomY = 4.150;
    const bottomCount = Math.max(1, count - 1);
    const bottomW = (W - gapX * (bottomCount - 1)) / bottomCount;

    const boxes = [{ x: X, y: Y, w: W, h: heroH }];
    for (let i = 0; i < bottomCount; i++) {
      boxes.push({
        x: X + i * (bottomW + gapX),
        y: bottomY,
        w: bottomW,
        h: bottomH
      });
    }
    return boxes;
  }

  if (layoutType === 'split_2col_equal' || layoutType === 'split_equal_2col' || count === 2) {
    const gap = 0.300;
    const cardW = 5.916;
    return [
      { x: X, y: Y, w: cardW, h: H },
      { x: X + cardW + gap, y: Y, w: cardW, h: H }
    ];
  }

  if (layoutType === 'grid_3col' || layoutType === 'three_column_grid' || count === 3) {
    const gap = 0.250;
    const cardW = 3.877;
    return [
      { x: X, y: Y, w: cardW, h: H },
      { x: X + cardW + gap, y: Y, w: cardW, h: H },
      { x: X + (cardW + gap) * 2, y: Y, w: cardW, h: H }
    ];
  }

  if (layoutType === 'grid_4col' || count === 4) {
    const gap = 0.200;
    const cardW = 2.883;
    return [
      { x: X, y: Y, w: cardW, h: H },
      { x: X + cardW + gap, y: Y, w: cardW, h: H },
      { x: X + (cardW + gap) * 2, y: Y, w: cardW, h: H },
      { x: X + (cardW + gap) * 3, y: Y, w: cardW, h: H }
    ];
  }

  const gap = 0.250;
  const cardW = (W - gap * (count - 1)) / count;
  const boxes = [];
  for (let i = 0; i < count; i++) {
    boxes.push({ x: X + i * (cardW + gap), y: Y, w: cardW, h: H });
  }
  return boxes;
}

/**
 * Format bullet text with math placeholders
 */
function formatBulletText(bullet) {
  let text = typeof bullet === 'string' ? bullet : (bullet.text || '');
  let result = '';
  let i = 0;
  while (i < text.length) {
    if (text.startsWith('{{MATH:', i) || text.startsWith('{{MATH_DISPLAY:', i) || text.startsWith('{{MATH_INLINE:', i)) {
      const isInline = text.startsWith('{{MATH_INLINE:', i);
      const prefix = text.startsWith('{{MATH_DISPLAY:', i) ? '{{MATH_DISPLAY:' : (isInline ? '{{MATH_INLINE:' : '{{MATH:');
      let j = i + prefix.length;
      let depth = 0;
      let math = '';
      while (j < text.length) {
        if (text[j] === '{') {
          depth++;
          math += '{';
        } else if (text[j] === '}') {
          if (depth === 0 && text[j+1] === '}') {
            j += 2;
            break;
          } else if (depth > 0) {
            depth--;
            math += '}';
          } else {
            math += '}';
          }
        } else {
          math += text[j];
        }
        j++;
      }
      result += `<<MATH_${isInline ? 'INLINE' : 'DISPLAY'}:${math.trim()}>>`;
      i = j;
    } else if (text[i] === '$' && text[i+1] !== '$') {
      let j = i + 1;
      let math = '';
      while (j < text.length && text[j] !== '$') {
        math += text[j];
        j++;
      }
      if (j < text.length && text[j] === '$') {
        result += `<<MATH_INLINE:${math.trim()}>>`;
        i = j + 1;
      } else {
        result += text[i];
        i++;
      }
    } else {
      result += text[i];
      i++;
    }
  }
  return result;
}

/**
 * Dynamic equation height calculator to avoid formula collisions
 */
function getEquationHeight(latex) {
  let h = 0.60;
  if (latex.includes('\\frac') || latex.includes('\\dfrac') || latex.includes('\\sum') || latex.includes('\\int') || latex.includes('\\prod') || latex.includes('\\bigcup') || latex.includes('\\bigcap')) {
    h += 0.45;
  }
  if (latex.includes('\\sqrt') || latex.includes('\\matrix') || latex.includes('\\begin') || latex.includes('\\left') || latex.includes('\\max') || latex.includes('\\min')) {
    h += 0.30;
  }
  if (latex.length > 70) {
    h += 0.25;
  }
  return Math.min(1.5, h);
}

/**
 * Render PPTX Table with Zebra Striping and SOTA Bold Metrics
 */
function renderTable(slide, box, tableData) {
  if (!tableData || !tableData.headers || !tableData.rows) return;
  const headers = tableData.headers;
  const rows = tableData.rows;
  const colWidths = tableData.colWidths || headers.map(() => (box.w - 0.4) / headers.length);

  const tableRows = [];

  // Header Row
  const headerRow = headers.map(h => ({
    text: String(h),
    options: {
      fill: { color: theme.primary || '0F2042' },
      color: 'FFFFFF',
      bold: true,
      fontSize: 12,
      fontFace: 'Arial',
      align: 'center',
      valign: 'middle'
    }
  }));
  tableRows.push(headerRow);

  // Data Rows
  rows.forEach((r, rIdx) => {
    const isOdd = rIdx % 2 === 1;
    const rowFill = isOdd ? (theme.cardHeaderBg || 'F8FAFC') : 'FFFFFF';
    const rowCells = r.map(cell => {
      let val = String(cell);
      let isBold = false;
      if (val.startsWith('**') && val.endsWith('**')) {
        val = val.substring(2, val.length - 2);
        isBold = true;
      }
      return {
        text: val,
        options: {
          fill: { color: rowFill },
          color: theme.bodyText || theme.textPrimary || '1F2937',
          bold: isBold,
          fontSize: 11,
          fontFace: 'Arial',
          align: 'center',
          valign: 'middle'
        }
      };
    });
    tableRows.push(rowCells);
  });

  slide.addTable(tableRows, {
    x: box.x + 0.2,
    y: box.y,
    w: box.w - 0.4,
    colW: colWidths,
    border: { type: 'solid', pt: 0.5, color: theme.cardBorder || 'CBD5E1' }
  });
}

/**
 * Render Vector Architecture Flowchart with DrawingML Shapes
 */
function renderVectorDiagram(slide, box, diagramData) {
  if (!diagramData || !diagramData.nodes) return;

  // Background Box
  slide.addShape(pptx.ShapeType.roundRect, {
    x: box.x,
    y: box.y,
    w: box.w,
    h: box.h,
    rectRadius: 0.08,
    fill: { color: theme.cardBg || 'FFFFFF' },
    line: { color: theme.cardBorder || 'CBD5E1', width: 1 }
  });

  // Diagram Title
  if (diagramData.title) {
    slide.addText(diagramData.title, {
      x: box.x + 0.3,
      y: box.y + 0.2,
      w: box.w - 0.6,
      h: 0.35,
      fontSize: 15,
      fontFace: 'Arial',
      bold: true,
      color: theme.primary || '0F2042'
    });
  }

  const innerX = box.x + 0.3;
  const innerY = box.y + (diagramData.title ? 0.6 : 0.3);
  const innerW = box.w - 0.6;
  const innerH = box.h - (diagramData.title ? 1.2 : 0.8);

  // Render Nodes
  diagramData.nodes.forEach(node => {
    const nx = innerX + (node.x || 0) * innerW;
    const ny = innerY + (node.y || 0) * innerH;
    const nw = (node.w || 1.8);
    const nh = (node.h || 0.8);

    let shapeType = pptx.ShapeType.roundRect;
    if (node.shape === 'rect') shapeType = pptx.ShapeType.rect;
    else if (node.shape === 'oval' || node.shape === 'ellipse' || node.shape === 'circle') shapeType = pptx.ShapeType.ellipse;

    const isNovel = node.type === 'novel' || node.highlight;
    const isLoss = node.type === 'loss' || node.type === 'terminal';

    let fillColor = isNovel ? (theme.highlightBg || 'EFF6FF') : (isLoss ? 'FEF2F2' : (theme.badgeBg || 'E0E7FF'));
    let borderColor = isNovel ? (theme.accent || '2563EB') : (isLoss ? 'DC2626' : (theme.secondary || '475569'));
    let textColor = isNovel ? (theme.highlightText || '1E40AF') : (isLoss ? '991B1B' : (theme.textPrimary || '0F172A'));

    slide.addShape(shapeType, {
      x: nx,
      y: ny,
      w: nw,
      h: nh,
      rectRadius: 0.06,
      fill: { color: fillColor },
      line: { color: borderColor, width: isNovel ? 2 : 1 }
    });

    slide.addText(node.name, {
      x: nx,
      y: ny,
      w: nw,
      h: nh,
      fontSize: 11,
      fontFace: 'Arial',
      bold: isNovel,
      color: textColor,
      align: 'center',
      valign: 'middle',
      shrinkText: true
    });
  });

  // Render Arrows
  if (diagramData.arrows) {
    diagramData.arrows.forEach(arr => {
      const ax = innerX + (arr.x || 0) * innerW;
      const ay = innerY + (arr.y || 0) * innerH;
      const aw = (arr.w || 0.08) * innerW;
      const ah = (arr.h || 0.15);
      slide.addShape(pptx.ShapeType.rightArrow, {
        x: ax,
        y: ay,
        w: Math.max(0.4, aw),
        h: Math.max(0.15, ah),
        fill: { color: arr.color || theme.accent || '2563EB' },
        line: { color: arr.color || theme.accent || '2563EB', width: 0 }
      });
    });
  }

  // Legend Badges
  const legendY = box.y + box.h - 0.45;
  slide.addText('PROPOSED / NOVEL', {
    x: innerX,
    y: legendY,
    w: 2.0,
    h: 0.3,
    fontSize: 9,
    fontFace: 'Arial',
    bold: true,
    color: theme.highlightText || '1E40AF'
  });
  slide.addText('BASELINE / INPUT', {
    x: innerX + 2.2,
    y: legendY,
    w: 2.0,
    h: 0.3,
    fontSize: 9,
    fontFace: 'Arial',
    bold: true,
    color: theme.textSecondary || '475569'
  });
}

/**
 * Render single card with text bullets, equations, images, or tables
 */
function renderCard(slide, box, card, cardIdx) {
  if (card.diagram) {
    renderVectorDiagram(slide, box, card.diagram);
    return;
  }

  const isCallout = card.is_callout || card.type === 'marginal_annotation' || card.type === 'callout';
  const bgColor = isCallout ? (theme.sideNoteBg || 'F9FAFB') : (theme.cardBg || 'FFFFFF');
  const borderColor = isCallout ? (theme.sideNoteBorder || '374151') : (theme.cardBorder || 'D1D5DB');
  const titleColor = isCallout ? (theme.sideNoteText || '000000') : (theme.headerText || '000000');

  // Background Box with subtle shadow
  slide.addShape(pptx.ShapeType.roundRect, {
    x: box.x,
    y: box.y,
    w: box.w,
    h: box.h,
    rectRadius: 0.06,
    fill: { color: bgColor },
    line: { color: borderColor, width: isCallout ? 1.5 : 1.0 },
    shadow: {
      type: 'outer',
      color: '000000',
      opacity: 0.04,
      blur: 4,
      offset: 1.5,
      angle: 45
    }
  });

  // Left Accent Bar for Marginal Callout Cards
  if (isCallout) {
    slide.addShape(pptx.ShapeType.roundRect, {
      x: box.x,
      y: box.y,
      w: 0.08,
      h: box.h,
      rectRadius: 0.04,
      fill: { color: theme.sideNoteAccent || '111827' },
      line: { color: theme.sideNoteAccent || '111827', width: 0 }
    });
  }

  const padLeft = isCallout ? 0.28 : 0.25;
  const padRight = 0.25;
  const contentW = box.w - padLeft - padRight;
  let currentY = box.y + (isCallout ? 0.18 : 0.22);

  // Card Header / Tag / Badge
  if (card.badge || card.tag || card.category) {
    const badgeText = (card.badge || card.tag || card.category).toUpperCase();
    slide.addText(badgeText, {
      x: box.x + padLeft,
      y: currentY,
      w: contentW,
      h: 0.25,
      fontSize: 10,
      fontFace: 'Arial',
      bold: true,
      color: theme.textSecondary || '4B5563'
    });
    currentY += 0.28;
  }

  // Card Title
  if (card.title) {
    slide.addText(card.title, {
      x: box.x + padLeft,
      y: currentY,
      w: contentW,
      h: 0.45,
      fontSize: 16,
      fontFace: 'Arial',
      bold: true,
      color: titleColor,
      shrinkText: true
    });
    currentY += 0.48;
  }

  // Embedded Image with Aspect Ratio Preservation
  let imgPath = card.image;
  if (!imgPath && card.figure_id && figuresMetadata[card.figure_id]) {
    imgPath = figuresMetadata[card.figure_id].file_path || figuresMetadata[card.figure_id].path;
  } else if (imgPath && figuresMetadata[imgPath]) {
    imgPath = figuresMetadata[imgPath].file_path || figuresMetadata[imgPath].path;
  }
  if (imgPath && fs.existsSync(imgPath)) {
    const imgH = card.imageH || Math.min(3.4, box.h - (currentY - box.y) - 0.35);
    const imgW = card.imageW || contentW;
    slide.addImage({
      path: imgPath,
      x: box.x + (box.w - imgW) / 2,
      y: currentY,
      w: imgW,
      h: imgH,
      sizing: { type: 'contain', w: imgW, h: imgH }
    });
    currentY += imgH + 0.15;
  }

  // Embedded Table
  if (card.table) {
    renderTable(slide, { x: box.x, y: currentY, w: box.w, h: box.h - (currentY - box.y) }, card.table);
    return;
  }

  // Math Equations (OMML Tags with Dynamic Spacing & No Overlap)
  if (card.omml_equations && card.omml_equations.length > 0) {
    card.omml_equations.forEach((eq, eqIdx) => {
      const latex = eq.latex || eq;
      const label = eq.label ? ` (${eq.label})` : '';
      const mathPlaceholder = `<<MATH_DISPLAY:${latex}>>`;
      const eqH = getEquationHeight(latex);

      slide.addText(`${mathPlaceholder}${label}`, {
        x: box.x + padLeft,
        y: currentY,
        w: contentW,
        h: eqH,
        fontSize: 14,
        fontFace: 'Arial',
        color: theme.primary || '000000',
        bold: true,
        align: 'left',
        shrinkText: true
      });
      currentY += eqH + 0.12;

      if (eq.explanation || eq.intuition) {
        const explText = eq.explanation || eq.intuition;
        slide.addText(`💡 Physical Intuition: ${explText}`, {
          x: box.x + padLeft + 0.10,
          y: currentY,
          w: contentW - 0.10,
          h: 0.35,
          fontSize: 12,
          fontFace: 'Arial',
          italic: true,
          color: theme.textSecondary || '4B5563',
          shrinkText: true
        });
        currentY += 0.42;
      }
    });
  }

  // Bullet Points or Text
  if (card.bullets && card.bullets.length > 0) {
    const textItems = [];
    card.bullets.forEach(bullet => {
      const formattedText = formatBulletText(bullet);

      textItems.push({
        text: formattedText,
        options: {
          fontSize: 13,
          fontFace: 'Arial',
          color: theme.bodyText || '1F2937',
          bullet: { type: 'bullet' },
          paraSpaceAfter: 5,
          lineSpacingMultiple: 1.20
        }
      });
    });

    slide.addText(textItems, {
      x: box.x + padLeft,
      y: currentY,
      w: contentW,
      h: Math.max(0.6, box.h - (currentY - box.y) - 0.15),
      valign: 'top',
      shrinkText: true,
      autoFit: true
    });
  } else if (card.text) {
    const formattedText = formatBulletText(card.text);
    slide.addText(formattedText, {
      x: box.x + padLeft,
      y: currentY,
      w: contentW,
      h: Math.max(0.6, box.h - (currentY - box.y) - 0.15),
      fontSize: 13,
      fontFace: 'Arial',
      color: theme.bodyText || '1F2937',
      valign: 'top',
      lineSpacingMultiple: 1.20,
      shrinkText: true,
      autoFit: true
    });
  }
}

// Build Slide Deck
console.log(`[build_deck.js] Building ${deckData.slides.length}-slide academic deck: "${deckData.meta?.title}" (Theme: ${theme.name})`);

const slides = deckData.slides || [];
const totalSlides = slides.length;

slides.forEach((sData, idx) => {
  const slide = pptx.addSlide();
  const slideNum = idx + 1;

  // Chrome (Header / Footer / Tracker)
  addSlideChrome(
    slide,
    slideNum,
    totalSlides,
    sData.section,
    sData.badge,
    sData.title,
    sData.subtitle,
    sData.citation || (deckData.meta?.doi ? `Source: ${deckData.meta.doi}` : '')
  );

  // If slide is a full-bleed diagram slide
  if (sData.diagram) {
    renderVectorDiagram(slide, { x: CANVAS.marginL, y: CANVAS.contentY, w: CANVAS.contentW, h: CANVAS.contentH }, sData.diagram);
    return;
  }

  // Cards List Assembly
  let cards = (sData.cards || []).slice();

  // If slide has side_note, append it as a callout card
  if (sData.side_note) {
    cards.push({
      is_callout: true,
      type: 'marginal_annotation',
      title: sData.side_note.title || 'Relationship to Our Research',
      category: sData.side_note.category || 'Lab Synergy',
      text: sData.side_note.text || sData.side_note.content || ''
    });
  }

  if (cards.length > 0) {
    const layoutType = sData.side_note ? 'split_65_35' : (sData.layout || 'split_2col_equal');
    const boxes = getGridLayout(layoutType, cards.length);
    cards.forEach((card, cIdx) => {
      if (boxes[cIdx]) {
        renderCard(slide, boxes[cIdx], card, cIdx);
      }
    });
  }
});

// Create Output Directory
const outDir = path.dirname(outputPath);
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

// Generate PPTX file
const tempPptx = outputPath.replace(/\.pptx$/i, '_stage1.pptx');

pptx.writeFile({ fileName: tempPptx })
  .then(() => {
    console.log(`[build_deck.js] Stage 1 PPTX generated: ${tempPptx}`);

    if (skipOmml) {
      fs.copyFileSync(tempPptx, outputPath);
      fs.unlinkSync(tempPptx);
      console.log(`[build_deck.js] Finished without OMML injection: ${outputPath}`);
      return;
    }

    // Phase 2: Inject Native OMML
    const injectorScript = path.join(__dirname, 'latex_to_omml.py');
    if (fs.existsSync(injectorScript)) {
      console.log(`[build_deck.js] Phase 2: Running latex_to_omml.py injector...`);
      try {
        const cmd = `python3 "${injectorScript}" --inject --input "${tempPptx}" --output "${outputPath}"`;
        execSync(cmd, { stdio: 'inherit' });
        if (fs.existsSync(tempPptx)) fs.unlinkSync(tempPptx);
        console.log(`[build_deck.js] Successfully created finalized OMML deck: ${outputPath}`);
      } catch (err) {
        console.warn(`[build_deck.js] Warning during OMML injection: ${err.message}. Falling back to Stage 1.`);
        fs.copyFileSync(tempPptx, outputPath);
      }
    } else {
      fs.copyFileSync(tempPptx, outputPath);
      console.log(`[build_deck.js] Saved to: ${outputPath}`);
    }
  })
  .catch(err => {
    console.error(`[build_deck.js] Fatal error:`, err);
    process.exit(1);
  });
