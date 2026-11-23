# 07 — Seedance Cinema Modes

Seedance 2.0 is a text-to-video and image-to-video model with native audio. It responds well to **mode-anchored prompts** — pick a cinema mode, write to its grammar, get consistent results.

This doc defines 5 working cinema modes for Seedance prompts. Each has a canonical:
- Camera / lens / movement
- Filtration / grade
- Diegetic audio design

---

## Why "modes"?

Seedance is a generalist model. It can do almost anything, which means it does nothing especially well unless you anchor it. Modes are anchors.

Pick one mode per prompt. Don't mix.

---

## Mode 1 — Narrative

For story-driven scenes with character emotion.

```
MODE: Narrative
Camera: 35mm, f/2.0, shallow DoF, eye-level
Movement: slow steady push-in or pull-back, no shake
Filtration: mild diffusion, slight halation in highlights
Grade: warm shadows, gentle contrast, skin tones prioritized
Audio: ambient room tone, footsteps, fabric rustle, breath
       — no music, no voice unless prompted
```

Best for: emotional moments, dialogue-free intimacy, slice-of-life.

### Prompt example

```
[Seedance Narrative Mode]
A woman sits on a windowsill in late afternoon light, reading a letter.
Camera: 35mm f/2.0 shallow depth of field, eye level, slow 4-second
push-in to medium close-up. Filtration: mild diffusion, warm grade.
Audio: distant traffic ambient, paper rustle as she turns the page,
soft breath. No music.
```

---

## Mode 2 — Studio

For controlled product / beauty / commercial shots.

```
MODE: Studio
Camera: 50mm or 85mm, f/4-5.6 for product clarity, slight low angle
Movement: smooth gimbal float or locked-off, no handheld
Filtration: clean, no diffusion
Grade: high saturation, bright midtones, hero product palette
Audio: product handling sounds (cap opens, fabric, glass clink),
       minimal ambient, no music unless prompted
```

Best for: product reveals, beauty close-ups, fashion.

### Prompt example

```
[Seedance Studio Mode]
Close-up of a glass perfume bottle on a white marble surface,
soft directional studio light from camera-left. Camera: 85mm f/4,
slight low angle (5° below eye), smooth orbit around the bottle
180° over 5 seconds. Grade: bright, clean, slight warm bias.
Audio: subtle handling sound, glass tap as it touches marble.
```

---

## Mode 3 — Action

For movement-heavy or kinetic scenes.

```
MODE: Action
Camera: 24-35mm, f/2.8, deep DoF, low or chest height
Movement: handheld with intentional shake, tracking with subject
Filtration: none, sharp
Grade: cool shadows, punchy contrast, slight teal-orange split
Audio: footsteps, fabric, breath under exertion, environmental impact
       sounds, no music
```

Best for: running, fighting, chase, athletic action.

### Prompt example

```
[Seedance Action Mode]
A runner sprints through a wet alley at night, neon signs reflecting
in puddles. Camera: 28mm f/2.8 handheld, chest height, tracking shot
parallel to the runner, intentional micro-shake.
Grade: cool blue shadows, sodium-orange neon highlights.
Audio: hard footsteps on wet ground, heavy breath, distant traffic,
splashes when feet hit puddles.
```

---

## Mode 4 — Performance

For musical / dance / theatrical performance.

```
MODE: Performance
Camera: 50mm or 85mm, f/2.0, eye level or slight low angle
Movement: smooth steadicam follow, sometimes orbit
Filtration: heavy diffusion, blooming highlights
Grade: high saturation, stage lighting respected (often dominant
       single color), spotlight feel
Audio: instrument sounds, dance feet, breath, hall ambient,
       no music track unless explicitly prompted
```

Best for: musicians, dancers, theatrical staging, music video b-roll.

### Prompt example

```
[Seedance Performance Mode]
A dancer in a black dress performs a slow turn on a dark stage,
single spotlight from above. Camera: 85mm f/2.0, smooth steadicam
orbit around the dancer 90° over 6 seconds, eye level.
Filtration: heavy diffusion, halation around the spotlight.
Audio: bare foot soft contact on stage, fabric movement, breath.
```

---

## Mode 5 — Atmospheric

For environmental / landscape / mood-driven scenes without a clear subject.

```
MODE: Atmospheric
Camera: 24mm wide or 14mm ultra-wide, f/5.6 deep DoF
Movement: very slow crane, drift, or locked-off
Filtration: optional mild diffusion
Grade: naturalistic, time-of-day appropriate
Audio: full environmental soundscape (wind, water, distant birds,
       insects, weather), no music
```

Best for: establishing shots, nature, weather, environmental mood.

### Prompt example

```
[Seedance Atmospheric Mode]
A mist-covered mountain valley at dawn, sun just breaking over the
ridge. Camera: 24mm wide, f/8 deep DoF, very slow crane up over
8 seconds revealing the wider valley. Grade: cold blue shadows
warming into orange highlights.
Audio: light wind, distant bird calls, water flowing somewhere
unseen, occasional insect.
```

---

## Mode comparison table

| Mode | Lens | Movement | Grade | Audio |
|---|---|---|---|---|
| Narrative | 35mm shallow | Slow push/pull | Warm soft | Ambient + foley |
| Studio | 50–85mm sharp | Smooth gimbal | Clean bright | Product foley only |
| Action | 24–35mm deep | Handheld track | Teal/orange punchy | Heavy environmental |
| Performance | 50–85mm shallow | Steadicam orbit | Stage spotlight | Performance sounds only |
| Atmospheric | 14–24mm wide | Slow crane / lock | Naturalistic | Full soundscape |

---

## Audio design notes (Seedance specific)

Seedance generates **diegetic audio** — sounds that come from the scene. It does **not** generate music well.

Best practices:
- Always specify audio explicitly. Default is silence or random.
- List 3-5 specific sound elements (footsteps, wind, fabric, breath, etc.)
- Avoid words like "soundtrack" or "score" — model tries and fails.
- Avoid voice/dialogue unless you accept whatever the model invents.

---

## Common mistakes

- ❌ Mixing modes ("narrative + studio + atmospheric") → muddled output.
- ❌ Forgetting audio → silent or random sounds.
- ❌ Wrong lens for the mode (e.g., 14mm wide for an intimate Narrative) → looks off.
- ❌ Asking for music → bad music.
- ✅ Pick one mode. Follow its grammar. Specify audio as foley list.

---

## Next

← Back to [README](../README.md) — see `prompts/` for drop-in templates.
