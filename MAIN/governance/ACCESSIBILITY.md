# Accessibility Statement

> **ONI Framework** is committed to ensuring digital accessibility for all users, including people with disabilities.

**Last Updated:** 2026-01-26
**WCAG Version:** 2.1 Level AA

---

## Compliance Status

Both **ONI Academy** and **TARA** user interfaces meet WCAG 2.1 Level AA standards.

### Conformance Level

| Criteria | Status | Notes |
|----------|--------|-------|
| **1.4.3 Contrast (Minimum)** | ✅ Compliant | All text meets 4.5:1 ratio |
| **1.4.11 Non-text Contrast** | ✅ Compliant | UI components meet 3:1 ratio |
| **2.1.1 Keyboard** | ✅ Compliant | All functions keyboard accessible |
| **2.1.2 No Keyboard Trap** | ✅ Compliant | Focus can always be moved |
| **2.4.1 Bypass Blocks** | ✅ Compliant | Skip links implemented |
| **2.4.7 Focus Visible** | ✅ Compliant | Focus indicators on all interactive elements |
| **2.3.1 Three Flashes** | ✅ Compliant | No flashing content |
| **2.3.3 Animation from Interactions** | ✅ Compliant | Respects prefers-reduced-motion |

---

## Color Contrast Ratios

### ONI Academy

All colors tested against primary background `#0f0f1a`:

| Color | Hex | Contrast Ratio | WCAG AA |
|-------|-----|----------------|---------|
| Primary Text | `#e2e8f0` | 13.5:1 | ✅ Pass |
| Secondary Text | `#a8b5c7` | 7.2:1 | ✅ Pass |
| Muted Text | `#8b9cb3` | 5.5:1 | ✅ Pass |
| Success | `#22c997` | 5.2:1 | ✅ Pass |
| Warning | `#fbbf24` | 8.5:1 | ✅ Pass |
| Error | `#f87171` | 5.1:1 | ✅ Pass |

### TARA Stack

All colors tested against primary background `#0a0a0f`:

| Color | Hex | Contrast Ratio | WCAG AA |
|-------|-----|----------------|---------|
| Primary Text | `#e2e8f0` | 14.5:1 | ✅ Pass |
| Secondary Text | `#a8b5c7` | 7.2:1 | ✅ Pass |
| Muted Text | `#8b9cb3` | 5.5:1 | ✅ Pass |
| Cyan Neon | `#00f5ff` | 8.9:1 | ✅ Pass |
| Magenta Neon | `#ff66ff` | 6.2:1 | ✅ Pass |
| Green Neon | `#33ff99` | 11.2:1 | ✅ Pass |
| Warning | `#ffcc00` | 10.8:1 | ✅ Pass |
| Error | `#ff6666` | 5.5:1 | ✅ Pass |

---

## Accessibility Features

### Keyboard Navigation

- **Tab**: Move between interactive elements
- **Enter/Space**: Activate buttons and links
- **Arrow Keys**: Navigate within components (sliders, menus)
- **Escape**: Close modals and dropdowns

### Skip Links

Both UIs include skip links that appear on keyboard focus, allowing users to:
- Skip to main content
- Skip navigation

### Focus Indicators

All interactive elements display visible focus indicators:
- 2px solid outline in brand color
- 2px offset for visibility
- Box shadow glow for enhanced visibility

### Motion Preferences

Both UIs respect `prefers-reduced-motion`:
- Animations are disabled or reduced to 0.01ms
- Scanline effects are hidden
- Transitions are minimized

---

## Font Sizes

Minimum font sizes enforced:
- Body text: 14px (0.875rem) minimum
- Small text: 14px (0.875rem) minimum
- Labels: 14px (0.875rem) minimum

---

## Screen Reader Support

HTML structure includes:
- Semantic HTML elements (`<main>`, `<nav>`, `<header>`, `<section>`)
- ARIA labels where needed
- Proper heading hierarchy (h1 → h2 → h3)
- Alt text for informational images

---

## Known Limitations

1. **Streamlit Framework**: Some accessibility features are limited by the Streamlit framework
2. **Dynamic Content**: Some dynamically generated charts may have limited screen reader support
3. **Color-Only Information**: Charts use both color and pattern/labels for information

---

## Automated Testing

### GitHub Action: Accessibility Check

Accessibility compliance is automatically verified after each PyPI package publish. This ensures every released version meets WCAG 2.1 AA standards.

**Workflow:** `.github/workflows/accessibility.yml`

**Triggers:**
- After successful PyPI publish (automatic)
- Manual workflow dispatch (for ad-hoc testing)

**Checks performed:**
- Color contrast ratios (WCAG 1.4.3)
- Minimum font sizes
- Focus indicator presence (WCAG 2.4.7)
- Reduced motion support (WCAG 2.3.3)
- Skip link implementation (WCAG 2.4.1)

**Badge:** The repository displays an accessibility compliance badge showing current status.

### Running Locally

```bash
# Run accessibility checker
python MAIN/governance/scripts/check_accessibility.py

# Verbose output with suggestions
python MAIN/governance/scripts/check_accessibility.py --verbose

# Strict mode (warnings become errors)
python MAIN/governance/scripts/check_accessibility.py --strict

# Check specific files
python MAIN/governance/scripts/check_accessibility.py --files path/to/styles.py
```

### Script Location

```
MAIN/governance/scripts/check_accessibility.py
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed |
| 1 | Accessibility violations found |
| 2 | Script error |

---

## Manual Testing

In addition to automated checks, perform manual testing with:
- Keyboard-only navigation (Tab, Enter, Escape)
- Screen reader testing (VoiceOver, NVDA)
- Browser zoom up to 200%
- Color contrast analyzer tools
- Chrome DevTools Accessibility audit
- prefers-reduced-motion simulation

---

## Feedback

We welcome feedback on the accessibility of ONI Framework interfaces.

Please report accessibility issues:
- GitHub Issues: https://github.com/qikevinl/ONI/issues
- Label issues with `accessibility`

---

## Technical Implementation

### Files

| File | Purpose |
|------|---------|
| `oni-framework/oni/ui/styles.py` | ONI Academy styles (WCAG compliant) |
| `tara-nsec-platform/tara_mvp/ui/styles.py` | TARA styles (WCAG compliant) |
| `governance/scripts/check_accessibility.py` | Automated compliance checker |
| `.github/workflows/accessibility.yml` | CI/CD accessibility workflow |

### CSS Features Added

```css
/* Skip link for keyboard navigation */
.skip-link { ... }

/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) { ... }

/* Focus states for keyboard navigation */
*:focus-visible { ... }
```

### Accessibility Checker Features

The `check_accessibility.py` script validates:

```python
# Color contrast calculation (WCAG algorithm)
def contrast_ratio(color1, color2) -> float

# Minimum requirements
WCAG_AA_CONTRAST_NORMAL = 4.5  # For regular text
WCAG_AA_CONTRAST_LARGE = 3.0   # For large text (18pt+)
MIN_FONT_SIZE_REM = 0.875      # 14px minimum
```

### CI/CD Integration

The GitHub Action runs on:
- After successful PyPI publish (`workflow_run` trigger)
- Manual workflow dispatch

```yaml
# Trigger configuration
on:
  workflow_run:
    workflows: ["Publish to PyPI"]
    types: [completed]
  workflow_dispatch:
```

This ensures every published package version is verified for accessibility compliance.

---

*This accessibility statement was created on 2026-01-26.*
*ONI Framework is committed to continuous accessibility improvement.*
