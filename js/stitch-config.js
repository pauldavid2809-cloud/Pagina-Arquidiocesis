/**
 * Stitch Sacred Modernism — Unified Tailwind Configuration
 * All pages import this file to ensure consistent design tokens.
 * Font: DM Sans (headings) + Poppins (body) via Google Fonts
 */
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        /* ── Core Brand ─────────────────── */
        "crimson-deep":   "#7A1A22",
        "gold-antique":   "#C59B27",
        "slate-warm":     "#4A4543",
        "warm-ivory":     "#F9F7F2",
        "lake-azure":     "#87CEEB",

        /* ── Material 3 Surfaces ────────── */
        "surface":                   "#fbf9f4",
        "surface-dim":               "#dbdad5",
        "surface-bright":            "#fbf9f4",
        "surface-container-lowest":  "#ffffff",
        "surface-container-low":     "#f5f3ee",
        "surface-container":         "#f0eee9",
        "surface-container-high":    "#eae8e3",
        "surface-container-highest": "#e4e2dd",
        "on-surface":                "#1b1c19",
        "on-surface-variant":        "#5a403c",
        "surface-variant":           "#e4e2dd",
        "surface-tint":              "#b52619",

        /* ── Primary ───────────────────── */
        "primary":                    "#5b000f",
        "on-primary":                 "#ffffff",
        "primary-container":          "#7a1a22",
        "on-primary-container":       "#ff8888",
        "inverse-primary":            "#ffb3b1",
        "primary-fixed":              "#ffdad8",
        "primary-fixed-dim":          "#ffb3b1",
        "on-primary-fixed":           "#410008",
        "on-primary-fixed-variant":   "#842229",

        /* ── Secondary (Gold) ──────────── */
        "secondary":                  "#775a00",
        "on-secondary":               "#ffffff",
        "secondary-container":        "#fece57",
        "on-secondary-container":     "#735700",
        "secondary-fixed":            "#ffdf98",
        "secondary-fixed-dim":        "#eec14b",
        "on-secondary-fixed":         "#251a00",
        "on-secondary-fixed-variant": "#5a4300",

        /* ── Tertiary ──────────────────── */
        "tertiary":                   "#002d3b",
        "on-tertiary":                "#ffffff",
        "tertiary-container":         "#004558",
        "on-tertiary-container":      "#6db4d0",
        "tertiary-fixed":             "#baeaff",
        "tertiary-fixed-dim":         "#89d0ed",
        "on-tertiary-fixed":          "#001f29",
        "on-tertiary-fixed-variant":  "#004d62",

        /* ── Inverse ───────────────────── */
        "inverse-surface":     "#30312e",
        "inverse-on-surface":  "#f2f1ec",

        /* ── Outline ───────────────────── */
        "outline":          "#8a7170",
        "outline-variant":  "#ddc0be",

        /* ── Error ─────────────────────── */
        "error":              "#ba1a1a",
        "on-error":           "#ffffff",
        "error-container":    "#ffdad6",
        "on-error-container": "#93000a",

        /* ── Background ────────────────── */
        "background":    "#fbf9f4",
        "on-background": "#1b1c19"
      },

      borderRadius: {
        DEFAULT: "0.25rem",
        lg:      "0.5rem",
        xl:      "0.75rem",
        "2xl":   "1rem",
        "3xl":   "1.5rem",
        full:    "9999px"
      },

      spacing: {
        "stack-sm":       "0.5rem",
        "stack-md":       "1rem",
        "stack-lg":       "2rem",
        "section-gap":    "5rem",
        "margin-mobile":  "1rem",
        "margin-desktop": "4rem",
        "gutter":         "1.5rem",
        "container-max":  "1200px"
      },

      fontFamily: {
        "display":     ["'DM Sans'", "sans-serif"],
        "headline":    ["'DM Sans'", "sans-serif"],
        "editorial":   ["'DM Sans'", "serif"],
        "body":        ["Poppins", "sans-serif"],
        "label":       ["Poppins", "sans-serif"],
        /* Legacy compat aliases */
        "display-lg":          ["'DM Sans'", "sans-serif"],
        "headline-lg":         ["'DM Sans'", "sans-serif"],
        "headline-lg-mobile":  ["'DM Sans'", "sans-serif"],
        "headline-md":         ["'DM Sans'", "sans-serif"],
        "body-lg":             ["Poppins", "sans-serif"],
        "body-md":             ["Poppins", "sans-serif"],
        "label-md":            ["Poppins", "sans-serif"],
        "label-sm":            ["Poppins", "sans-serif"]
      },

      fontSize: {
        "display-lg":         ["64px", { lineHeight: "1.1",  letterSpacing: "-0.02em", fontWeight: "700" }],
        "headline-lg":        ["48px", { lineHeight: "1.2",  letterSpacing: "-0.01em", fontWeight: "600" }],
        "headline-lg-mobile": ["32px", { lineHeight: "1.2",  fontWeight: "600" }],
        "headline-md":        ["28px", { lineHeight: "1.3",  fontWeight: "500" }],
        "body-lg":            ["18px", { lineHeight: "1.6",  fontWeight: "400" }],
        "body-md":            ["16px", { lineHeight: "1.6",  fontWeight: "400" }],
        "label-lg":           ["14px", { lineHeight: "1.2",  letterSpacing: "0.05em",  fontWeight: "600" }],
        "label-md":           ["14px", { lineHeight: "1.2",  letterSpacing: "0.05em",  fontWeight: "600" }],
        "label-sm":           ["12px", { lineHeight: "1.2",  letterSpacing: "0.05em",  fontWeight: "500" }]
      },

      maxWidth: {
        "container": "1200px"
      }
    }
  }
};
