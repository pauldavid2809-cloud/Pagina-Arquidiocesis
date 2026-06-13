---
name: Sacred Modernism
colors:
  # Core Brand
  crimson-deep: '#7A1A22'
  gold-antique: '#C59B27'
  slate-warm: '#4A4543'
  warm-ivory: '#F9F7F2'
  lake-azure: '#87CEEB'

  # Material Design 3 Surfaces
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#5a403c'
  surface-variant: '#e4e2dd'
  surface-tint: '#b52619'

  # Primary
  primary: '#5b000f'
  on-primary: '#ffffff'
  primary-container: '#7a1a22'
  on-primary-container: '#ff8888'
  inverse-primary: '#ffb3b1'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b1'
  on-primary-fixed: '#410008'
  on-primary-fixed-variant: '#842229'

  # Secondary (Gold)
  secondary: '#775a00'
  on-secondary: '#ffffff'
  secondary-container: '#fece57'
  on-secondary-container: '#735700'
  secondary-fixed: '#ffdf98'
  secondary-fixed-dim: '#eec14b'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5a4300'

  # Tertiary
  tertiary: '#002d3b'
  on-tertiary: '#ffffff'
  tertiary-container: '#004558'
  on-tertiary-container: '#6db4d0'
  tertiary-fixed: '#baeaff'
  tertiary-fixed-dim: '#89d0ed'
  on-tertiary-fixed: '#001f29'
  on-tertiary-fixed-variant: '#004d62'

  # Inverse
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'

  # Outline
  outline: '#8a7170'
  outline-variant: '#ddc0be'

  # Error
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'

  # Background
  background: '#fbf9f4'
  on-background: '#1b1c19'

typography:
  display-lg:
    fontFamily: DM Sans
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: DM Sans
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: DM Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: DM Sans
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Poppins
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Poppins
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Poppins
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Poppins
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The design system embodies a philosophy of "Sacred Modernism"—a synthesis of timeless theological solemnity and contemporary functionalism. It targets an audience seeking depth, ritual, and clarity, evoking an emotional response of reverence, stability, and intellectual calm.

The visual style is **Minimalist** with **Tactile** undertones. It prioritizes vast, intentional whitespace (breathing room for contemplation) and high-quality typography. While the layout remains strictly grid-based and modern, the interaction model utilizes subtle physical metaphors to suggest the weight and permanence of liturgical objects. The aesthetic avoids unnecessary ornamentation, allowing the relationship between rich color and stark geometry to communicate authority.

## Colors

The palette is anchored by **Crimson Deep** (#7A1A22), representing sacrifice, vitality, and deep-rooted tradition. This is paired with **Gold Antique** (#C59B27), used sparingly for highlights, interactive states, and "divine" accents to signify value and enlightenment.

The background uses a warm, parchment-leaning neutral (#F9F7F2) rather than a clinical white to soften the high contrast of the Crimson and provide a more organic, archival feel. **Lake Azure** (#87CEEB) is used as a tertiary accent for informational elements and alerts.

## Typography

**DM Sans** (substitute for Rotis Sans Serif) is utilized for all headings and titles, providing a humanist, intellectual, and authoritative structure. Its unique legibility and distinctive letterforms create a sense of curated editorial excellence.

**Poppins** is used for all body text, navigation, and functional UI elements. Its geometric purity provides a friendly yet precise counter-balance to the more complex DM Sans.

For labels and small UI elements, Poppins is often set in uppercase with increased letter spacing to mimic the inscription style found in classical architecture. Ensure line heights for body text remain generous (1.6) to promote long-form reading and clarity.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for desktop to maintain a "book-like" centered composition, transitioning to a fluid model for mobile devices.

- **Desktop:** 12-column grid, 1200px max-width, 24px gutters.
- **Tablet:** 8-column grid, fluid margins (minimum 32px).
- **Mobile:** 4-column grid, 16px margins, 16px gutters.

Spacing follows an 8px base unit. Use "XL" spacing (80px+) between major sections to emphasize the minimalist aesthetic and give content a "monumental" feel. Avoid crowding elements; if in doubt, increase the margin.

## Elevation & Depth

Hierarchy is established primarily through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows.

1. **Base Layer:** The warm neutral surface (#F9F7F2).
2. **Raised Surfaces (Cards/Modals):** Use a pure white background with a very subtle, 1px hairline border in a slightly darker neutral or 5% opacity Crimson.
3. **Depth:** Shadows, when used for high-priority modals, should be "Ambient"—extremely diffused (24px+ blur), low opacity (5-8%), and tinted with the primary Crimson color to maintain warmth.
4. **Interactive States:** Use Gold for subtle "glow" underlines or border-bottom transitions rather than traditional heavy lifts.

## Shapes

The shape language is **Soft (Level 1)**. Elements utilize a 0.25rem (4px) base radius. This creates a "precision-milled" look—not as harsh as sharp 90-degree angles, but far more disciplined and serious than fully rounded or pill-shaped designs.

## Components

### Buttons
- **Primary:** Solid Crimson background, White text (Poppins Medium). No rounded corners larger than 4px, except pill CTAs.
- **Secondary:** Transparent background, Crimson border (1px), Crimson text.
- **Tertiary/Ghost:** Gold text, no border. Used for low-priority actions.

### Input Fields
- Use "Floating Label" style to maintain a clean aesthetic when empty.
- Border is 1px neutral-gray, turning Crimson on focus.

### Cards
- Minimalist containers with no shadow by default.
- Defined by a thin 1px neutral border.
- Headlines within cards must use DM Sans.

### Chips & Tags
- Background: Very light tint of Crimson (5% opacity).
- Text: Crimson, Poppins Bold, All-caps, small font size.

### Lists
- Separated by thin, horizontal dividers in a light Gold or neutral tone.
- Ensure generous vertical padding (16px-24px) between list items.
