# Prompt Anatomy Template

A production-grade prompt has 5-6 stacked layers. Build them deliberately.

---

## The stack

```
[1. SUBJECT + ACTION]
+
[2. PHYSICAL REALISM]
+
[3. LIGHTING]
+
[4. COMPOSITION]
+
[5. CAMERA + LENS + MOTION]
+
[6. STYLE ANCHOR — optional DP, film stock, decade reference]
```

---

## Drop-in template

Copy and fill in:

```
[1 — SUBJECT + ACTION]
A [age/description] [person/object] is [doing what action] in [location].

[2 — PHYSICAL REALISM]
Skin: subsurface scattering, visible pores, [warm/cool] bloom.
Materials: [fabric type with weave detail], [liquid with Fresnel/caustics
if applicable].
Contact: [contact shadow at base], [color bounce from X onto Y].
Anatomy: natural posture, weight on [left/right] leg, [eye details].
Performance: [micro-expression detail, e.g., Duchenne smile, subtle
nostril breath].

[3 — LIGHTING]
[DP style reference, e.g., "in the style of Deakins"]:
Key: [direction, angle, hardness, color temperature].
Fill: [side or negative fill].
Rim / back: [direction if any].
Practical: [in-frame light sources if any].
Motivation: [why is the light there — window, sunset, lamp].

[4 — COMPOSITION]
Framing: [wide / medium / close-up].
Subject position: [center / left third / right third / lower third].
Camera height: [low / eye level / high].
Negative space: [where empty space lives].

[5 — CAMERA + LENS + MOTION]
Lens: [14/24/35/50/85/100mm], aperture f/[stop].
Movement: [push-in / pull-back / tracking / pan / locked-off / orbit].
Duration: [seconds].
Direction & speed: [slow, fast, smooth, handheld].

[6 — STYLE ANCHOR — optional]
"in the style of [DP / decade / film stock / aesthetic]"

[NEGATIVE]
plastic skin, deformed hands, floating objects, painted water,
t-pose, dead eyes, frozen expression, [add per scene]
```

---

## Worked example — woman by a pool

```
[1] A young woman in her late 20s walks slowly toward the camera
beside an outdoor pool at sunset.

[2] Subsurface scattering on skin, visible pores at 1:1, soft warm
bloom on her cheek. Cotton sundress with visible weave, natural drape
following body, wrinkle at the hip from walking motion. Pool water
shows Fresnel reflection, caustic light pattern on the floor behind
her. Contact: feet press into soft poolside tiles, subtle deformation.
Posture: weight transferring as she walks, slight shoulder lean.
Eyes: catchlight from sky, subtle Duchenne smile breaks at midpoint.

[3] Cinematography in the style of Emmanuel Lubezki:
natural light only, sun low on horizon camera-back, strong rim
backlight glowing her hair, lens flare. No artificial fill — let
her face fall into soft warm shadow. Warm amber palette.

[4] Subject lower third, walking from background to mid-ground.
Camera at eye level. Pool fills lower fifth as foreground.
Wide environmental composition with strong horizon line in upper third.

[5] Shot on 35mm at f/2.0. Slow steady push-in toward her over
5 seconds. Smooth gimbal, no shake. She arrives at medium close-up
as the push completes.

[6] Style: warm summer commercial aesthetic, late afternoon golden hour.

[NEGATIVE] plastic skin, deformed hands, painted water, no rim light,
flat ambient lighting, t-pose, frozen face
```

---

## Speed tip — layer-by-layer iteration

When a generation fails, you usually know **which layer** failed:

- Face looks plastic → Layer 2 (Physical Realism: skin)
- Light is flat → Layer 3 (Lighting)
- Subject lost in frame → Layer 4 (Composition)
- Motion is wrong speed → Layer 5 (Camera Motion duration)

Iterate one layer at a time. Don't rewrite the whole prompt.

---

## See also

- [01 — Physical Realism](../docs/01-physical-realism.md)
- [02 — Cinematic Lighting](../docs/02-cinematic-lighting.md)
- [03 — Composition](../docs/03-composition.md)
- [04 — Camera Motion](../docs/04-camera-motion.md)
