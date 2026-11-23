# 03 — Composition

Lighting tells the model **how light behaves**. Composition tells it **where everything is in the frame**. Most prompts don't specify composition at all — they just describe the subject and hope. This doc fixes that.

---

## The 5 composition variables

Every shot has these. Specify them deliberately.

1. **Framing** — wide / medium / close-up / extreme close-up
2. **Subject position** — center / rule of thirds / negative space placement
3. **Camera height** — low angle / eye level / high angle / overhead
4. **Symmetry** — perfectly symmetric / off-axis / dutch tilt
5. **Foreground / midground / background** — layered or flat?

---

## Master director signatures

Pick a director, get the formula.

### Stanley Kubrick — Perfect symmetry + one-point perspective

```
composition in the style of Stanley Kubrick:
perfectly symmetric frame, one-point perspective leading to dead center,
subject placed exactly in the middle of the frame,
hallway or corridor extending into distance,
slight wide angle distortion, eye level, locked-off camera
```

Works for: Sterile interiors, institutional spaces, dread, control.

---

### Wes Anderson — Flat tableau + center subject + pastel palette

```
composition in the style of Wes Anderson:
flat tableau composition, subject dead center facing camera,
perfectly horizontal and vertical lines,
pastel symmetric palette, no depth — like a painting,
overhead or straight-on angle, no diagonal lines
```

Works for: Whimsy, deadpan humor, doll-house worlds.

---

### Wong Kar-wai — Cropped, intimate, off-axis

```
composition in the style of Wong Kar-wai:
tight cropped frame, subject occupies bottom or side third,
strong negative space above or beside the subject,
slight dutch tilt, blurred foreground element (cigarette smoke, fabric, hair),
warm color palette with high contrast, intimate medium close-up
```

Works for: Romance, melancholy, urban Asia, longing.

---

### Andrei Tarkovsky — Long take, depth, water/fire elemental

```
composition in the style of Andrei Tarkovsky:
long take steady frame, deep depth from foreground to far background,
elemental presence (water, fire, smoke, fog) in the frame,
horizon line in upper third, subject small against natural environment,
slow drift in or pan, contemplative pacing
```

Works for: Spiritual, contemplative, nature, philosophical.

---

### Christopher Nolan — Epic scale + IMAX wide + subject small

```
composition in the style of Christopher Nolan:
IMAX wide aspect ratio 1.43:1 or 2.20:1,
subject small in lower third against vast architecture or landscape,
strong horizon line, deep negative space,
clean geometric lines, no clutter,
camera at slight low angle to emphasize subject's environment
```

Works for: Epic, sci-fi, war, scale.

---

## Composition for shorts (9:16 vertical)

Vertical framing breaks most of the above. Here's what works:

### Safe areas for vertical

```
top 20% — usually reserved for UI (caption, status bar)
70.3% from top — subtitle safe zone for Reels/Shorts
bottom 18% — also usually UI
center 60% vertical — keep the main subject here
```

### Vertical composition recipes

**Single subject portrait**
```
single subject occupying center 60% vertical,
head at upper third intersection,
shoulders crossing mid-frame,
keep eye line at 1/3 from top
```

**Wide environmental**
```
horizon at 1/3 from top,
subject small in lower third center,
foreground texture (grass, water, ground) for depth,
strong vertical lines in background (trees, buildings) reinforce frame
```

**Product on a surface**
```
product at center,
camera slightly above (5-10° down angle),
foreground negative space (clean table surface) 30%,
background blurred environmental context 40%
```

---

## Negative-space recipes

Negative space is one of the most underused tools in AI prompts.

```
strong negative space camera-left, subject pushed to right third,
sky filling upper half, ground in lower quarter,
clean unbroken negative area, no clutter,
subject framed by emptiness
```

Use when: You want the subject to feel isolated, contemplative, important.

---

## Common mistakes

- ❌ "Beautiful composition" = vague.
- ❌ "Rule of thirds" without specifying which third = the model guesses.
- ❌ Center composition for everything = boring.
- ❌ Ignoring camera height — eye level is the default, but rarely the most interesting choice.
- ✅ "Subject at lower-right third, camera at low angle 15° below eye level, strong negative space in upper-left, foreground out-of-focus leaf framing the bottom edge."

---

## Composition + Lighting = signature look

These pair up:

| Director look | Lighting style | Composition |
|---|---|---|
| Deakins | Single key + negative fill | Center or thirds, mid shot |
| Lubezki | Backlit golden hour | Long lens, subject moving across frame |
| Doyle | Practical neon | Tight crop, dutch tilt |
| Khondji | Sodium orange | Frame within frame, claustrophobic |
| van Hoytema | Cold blue + warm orange | Subject small, vast negative space |
| Kubrick | Hard, central | One-point symmetry |
| Wes Anderson | Flat soft | Tableau symmetry |
| Tarkovsky | Window-light or fire-light | Long static, deep depth |
| Wong Kar-wai | Neon practicals | Cropped, off-axis |
| Nolan | IMAX natural | Epic wide, subject small |

---

## Next

→ [04 — Camera Motion](04-camera-motion.md)
