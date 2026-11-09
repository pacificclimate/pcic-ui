from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import font_manager

OUTPUT = Path("PCIC-Style-Quick-Reference.pdf")

# ---------------------------------------------------------------------
# Font setup
# ---------------------------------------------------------------------

available_fonts = {f.name for f in font_manager.fontManager.ttflist}

if "Myriad Pro" in available_fonts:
    plt.rcParams["font.family"] = "Myriad Pro"
else:
    plt.rcParams["font.family"] = "sans-serif"

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

# ---------------------------------------------------------------------
# Brand data supplied by PCIC User Engagement
# ---------------------------------------------------------------------

palette = [
    ("PCIC dark blue", "#003f5e", "RGB 0, 63, 94", True),
    ("PCIC medium blue", "#205768", "RGB 32, 87, 104", False),
    ("PCIC light blue", "#6d9fb9", "RGB 109, 159, 185", True),
    ("PCIC dark green", "#2b6733", "RGB 43, 103, 51", False),
    ("PCIC medium green", "#60ba46", "RGB 96, 186, 70", True),
    ("PCIC light green", "#bbdc9b", "RGB 187, 220, 155", False),
    ("PCIC grey-green", "#c1cda4", "RGB 193, 205, 164", False),
    ("PCIC light-grey green", "#e4eada", "RGB 228, 234, 218", False),
]

# ---------------------------------------------------------------------
# Web application conventions maintained by Comp Support
# ---------------------------------------------------------------------

web_semantics = [
    ("Primary action", "#003f5e", "PCIC dark blue"),
    ("Primary hover", "#205768", "PCIC medium blue"),
    ("Accent", "#6d9fb9", "PCIC light blue"),
    ("Success", "#2b6733", "PCIC dark green"),
    ("Warning", "#b36b00", "UI semantic colour"),
    ("Danger", "#c94a38", "UI semantic colour"),
    ("Page background", "#f5f5f5", "Neutral"),
    ("Surface", "#ffffff", "Neutral"),
    ("Muted surface", "#f0f0f0", "Neutral"),
    ("Hover surface", "#e8f4f8", "Neutral"),
    ("Text", "#333333", "Neutral"),
    ("Muted text", "#666666", "Neutral"),
]

scientific = [
    ("Precipitation", "#1976a8"),
    ("Temperature", "#c94a38"),
    ("Snow", "#5b84b1"),
    ("Flow", "#39796b"),
    ("Evaporation", "#4f7f47"),
    ("Glacier", "#477f9d"),
    ("Soil", "#8a6541"),
]

font_stacks = [
    (
        "Interface font",
        "--pcic-font-sans",
        'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
        "Normal web application text: controls, tables, dialogs, navigation, labels, charts, and body UI.",
    ),
    (
        "Monospace font",
        "--pcic-font-mono",
        'ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace',
        "Fixed-width technical content such as code, identifiers, coordinates, logs, or similar values.",
    ),
]

BLUE = "#003f5e"
MED_BLUE = "#205768"
GREEN = "#60ba46"
GREY_GREEN = "#c1cda4"
GREY_GREEN_LIGHT = "#e4eada"
TEXT = "#333333"
MUTED = "#666666"

LEFT = 0.06
RIGHT = 0.94
CONTENT_W = RIGHT - LEFT


def new_page():
    fig = plt.figure(figsize=(8.5, 11))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def page_title(ax, title, subtitle):
    ax.text(
        LEFT,
        0.952,
        title,
        fontsize=22,
        fontweight="bold",
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT,
        0.907,
        subtitle,
        fontsize=10,
        color=MED_BLUE,
        va="top",
    )


def section_title(ax, y, number, title):
    ax.text(
        LEFT,
        y,
        f"{number} {title}",
        fontsize=13,
        fontweight="bold",
        color=GREEN,
        va="top",
    )


def swatch(ax, x, y, width, height, color, edge="#cccccc"):
    ax.add_patch(
        Rectangle(
            (x, y - height),
            width,
            height,
            facecolor=color,
            edgecolor=edge,
            linewidth=0.8,
        )
    )


def info_band(ax, y_top, height, title, body=None):
    # y_top is the top edge of the band.
    ax.add_patch(
        FancyBboxPatch(
            (LEFT, y_top - height),
            CONTENT_W,
            height,
            boxstyle="round,pad=0.004,rounding_size=0.004",
            linewidth=0,
            facecolor=GREY_GREEN_LIGHT,
        )
    )
    title_y = y_top - 0.016
    ax.text(
        LEFT + 0.015,
        title_y,
        title,
        fontsize=9.2,
        fontweight="bold",
        color=BLUE,
        va="top",
    )
    if body:
        ax.text(
            LEFT + 0.015,
            title_y - 0.022,
            body,
            fontsize=8.5,
            color=MED_BLUE,
            va="top",
            linespacing=1.25,
        )


def footer(ax):
    ax.plot([LEFT, RIGHT], [0.025, 0.025], color=GREY_GREEN, linewidth=0.6)
    ax.text(
        RIGHT,
        0.010,
        "PCIC internal quick reference",
        fontsize=7.5,
        color=MED_BLUE,
        ha="right",
        va="bottom",
    )


with PdfPages(OUTPUT) as pdf:
    # =================================================================
    # PAGE 1 - OFFICIAL BRAND REFERENCE
    # =================================================================
    fig, ax = new_page()

    page_title(
        ax,
        "PCIC STYLE QUICK REFERENCE",
        "Colour palette and typography guidance",
    )

    section_title(ax, 0.855, "1", "Official Colours")

    start_y = 0.812
    row_gap = 0.073

    for i, (name, hex_value, rgb, logo_colour) in enumerate(palette):
        col = i % 2
        row = i // 2
        x = LEFT + col * 0.47
        y = start_y - row * row_gap

        swatch(ax, x, y, 0.075, 0.045, hex_value)

        label = name + ("  - logo colour" if logo_colour else "")
        ax.text(
            x + 0.09,
            y,
            label,
            fontsize=9.6,
            fontweight="bold" if logo_colour else "normal",
            color=BLUE,
            va="top",
        )
        ax.text(
            x + 0.09,
            y - 0.024,
            f"{hex_value.upper()}  -  {rgb}",
            fontsize=8.3,
            color=MED_BLUE,
            va="top",
        )

    # -----------------------------------------------------------------
    # Typography and general guidance - balanced two-column lower half
    # -----------------------------------------------------------------

    section_title(ax, 0.505, "2", "Typography")

    # Left column: typography hierarchy supplied by User Engagement.
    ax.text(
        LEFT,
        0.464,
        "TITLES",
        fontsize=15.5,
        fontweight="bold",
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT,
        0.439,
        "Myriad Pro Bold Condensed - ALL CAPS",
        fontsize=8.8,
        color=MED_BLUE,
        va="top",
    )

    ax.text(
        LEFT,
        0.398,
        "Subtitles",
        fontsize=11.5,
        fontweight="bold",
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT,
        0.375,
        "Myriad Pro Bold",
        fontsize=8.8,
        color=MED_BLUE,
        va="top",
    )

    ax.text(
        LEFT,
        0.334,
        "Main/body text",
        fontsize=10.2,
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT,
        0.311,
        "Myriad Pro Regular",
        fontsize=8.8,
        color=MED_BLUE,
        va="top",
    )

    # Right column: short usage guidance, aligned to the same baseline.
    guide_x = 0.53
    ax.text(
        guide_x,
        0.505,
        "3 General Guidance",
        fontsize=13,
        fontweight="bold",
        color=GREEN,
        va="top",
    )

    guidance = [
        "Use the official PCIC palette consistently across communications.",
        "Dark blue is the primary text colour in branded materials.",
        "Medium green works well for section headings and emphasis.",
        "Light green and grey-green tones work well for callout areas.",
        "Scientific figures may use additional colours where needed for clarity.",
    ]

    gy = 0.464
    for item in guidance:
        ax.text(
            guide_x,
            gy,
            "\u2022",
            fontsize=8.8,
            color=GREEN,
            va="top",
        )
        ax.text(
            guide_x + 0.020,
            gy,
            item,
            fontsize=8.15,
            color=BLUE,
            va="top",
            wrap=True,
        )
        gy -= 0.030

    # Licensing note
    note_top = 0.255
    note_height = 0.105
    ax.add_patch(
        FancyBboxPatch(
            (LEFT, note_top - note_height),
            CONTENT_W,
            note_height,
            boxstyle="round,pad=0.004,rounding_size=0.004",
            linewidth=0.55,
            edgecolor=GREY_GREEN,
            facecolor=GREY_GREEN_LIGHT,
        )
    )

    ax.text(
        LEFT + 0.015,
        note_top - 0.017,
        "Myriad Pro licensing note",
        fontsize=8.8,
        fontweight="bold",
        color=BLUE,
        va="top",
    )

    license_lines = [
        "Myriad Pro is an Adobe typeface and may be subject to licence restrictions.",
        "Standard desktop/Adobe Fonts licensing generally permits use in printed and exported documents, including PDFs,",
        "but does not permit redistribution of the font files themselves or embedding the font directly in software applications.",
        "Confirm the applicable Adobe or font licence before distributing font files or using Myriad Pro outside normal",
        "document-production workflows.",
    ]

    ly = note_top - 0.043
    for line in license_lines:
        ax.text(
            LEFT + 0.015,
            ly,
            line,
            fontsize=7.35,
            color=MED_BLUE,
            va="top",
        )
        ly -= 0.0145

    footer(ax)

    pdf.savefig(fig)
    plt.close(fig)

    # =================================================================
    # PAGE 2 - WEB APPLICATION CONVENTIONS
    # =================================================================
    fig, ax = new_page()

    page_title(
        ax,
        "WEB APPLICATION CONVENTIONS",
        "Recommended PCIC interface conventions derived from the official brand palette",
    )

    info_band(
        ax,
        y_top=0.850,
        height=0.064,
        title="Comp Support web design-system conventions",
        body=(
            "These provide consistent application defaults while allowing scientific "
            "and map colours to remain context dependent."
        ),
    )

    section_title(ax, 0.755, "1", "Interface Colour Use")

    start_y = 0.713
    row_gap = 0.049

    for i, (name, hex_value, source) in enumerate(web_semantics):
        col = i % 2
        row = i // 2
        x = LEFT + col * 0.47
        y = start_y - row * row_gap

        swatch(ax, x, y, 0.058, 0.030, hex_value)

        ax.text(
            x + 0.072,
            y - 0.001,
            name,
            fontsize=8.9,
            fontweight="bold",
            color=BLUE,
            va="top",
        )
        ax.text(
            x + 0.072,
            y - 0.020,
            f"{hex_value.upper()}  -  {source}",
            fontsize=7.6,
            color=MED_BLUE,
            va="top",
        )

    section_title(ax, 0.385, "2", "Scientific Variable Accents")

    ax.text(
        LEFT,
        0.355,
        "Shared visualization defaults; use additional colours where required for scientific clarity.",
        fontsize=8.5,
        color=MED_BLUE,
        va="top",
    )

    y = 0.316
    for i, (name, hex_value) in enumerate(scientific):
        x = LEFT + (i % 4) * 0.225
        yy = y - (i // 4) * 0.065

        swatch(ax, x, yy, 0.052, 0.033, hex_value)
        ax.text(
            x + 0.063,
            yy - 0.001,
            name,
            fontsize=8.5,
            fontweight="bold",
            color=BLUE,
            va="top",
        )
        ax.text(
            x + 0.063,
            yy - 0.021,
            hex_value.upper(),
            fontsize=7.4,
            color=MED_BLUE,
            va="top",
        )

    section_title(ax, 0.190, "3", "Web Application Typography")

    # Concise explanation of the three shared font tokens.
    # The full CSS definitions are presented on page 3.
    ax.text(
        LEFT,
        0.157,
        "Existing PCIC web applications use system, Arial, or generic sans-serif typefaces rather than Myriad Pro.",
        fontsize=8.6,
        color=BLUE,
        va="top",
    )

    roles = [
        (
            "Interface",
            "Shared system sans-serif stack for controls, tables, dialogs, navigation, charts, and body UI.",
        ),
        (
            "Monospace",
            "System monospace stack for code, identifiers, coordinates, logs, and other fixed-width technical content.",
        ),
    ]

    y = 0.124
    for label, description in roles:
        ax.text(
            LEFT + 0.015,
            y,
            f"{label}:",
            fontsize=8.5,
            fontweight="bold",
            color=BLUE,
            va="top",
        )
        ax.text(
            LEFT + 0.115,
            y,
            description,
            fontsize=8.3,
            color=MED_BLUE,
            va="top",
        )
        y -= 0.030

    footer(ax)

    pdf.savefig(fig)
    plt.close(fig)

    # =================================================================
    # PAGE 3 - COMP SUPPORT FONT DEFINITIONS
    # =================================================================
    fig, ax = new_page()

    page_title(
        ax,
        "WEB TYPOGRAPHY DEFINITIONS",
        "Shared interface font-family definitions used by PCIC web applications",
    )

    info_band(
        ax,
        y_top=0.850,
        height=0.064,
        title="How to read these definitions",
        body=(
            "Each font stack is an ordered list of fallbacks. The browser uses the first available font.\n"
            "Publication typography remains Myriad Pro; web interface typography uses system fonts."
        ),
    )

    section_title(ax, 0.755, "1", "Shared Font Families")

    card_top = 0.710
    card_height = 0.165
    card_gap = 0.028

    for i, (role, token, stack, description) in enumerate(font_stacks):
        top = card_top - i * (card_height + card_gap)
        bottom = top - card_height

        ax.add_patch(
            FancyBboxPatch(
                (LEFT, bottom),
                CONTENT_W,
                card_height,
                boxstyle="round,pad=0.006,rounding_size=0.006",
                linewidth=0.7,
                edgecolor=GREY_GREEN,
                facecolor="#ffffff",
            )
        )

        ax.text(
            LEFT + 0.018,
            top - 0.022,
            role,
            fontsize=10.2,
            fontweight="bold",
            color=BLUE,
            va="top",
        )

        ax.text(
            RIGHT - 0.018,
            top - 0.022,
            token,
            fontsize=8.1,
            color=MED_BLUE,
            ha="right",
            va="top",
            family="monospace",
        )

        ax.text(
            LEFT + 0.018,
            top - 0.053,
            description,
            fontsize=8.7,
            color=TEXT,
            va="top",
        )

        # Light background for the CSS-style stack itself.
        code_y = top - 0.090
        ax.add_patch(
            Rectangle(
                (LEFT + 0.018, code_y - 0.046),
                CONTENT_W - 0.036,
                0.052,
                facecolor="#f5f5f5",
                edgecolor="#dddddd",
                linewidth=0.5,
            )
        )

        # Wrap manually at sensible commas to avoid running off the page.
        parts = [p.strip() for p in stack.split(",")]
        lines = []
        current = ""
        for part in parts:
            candidate = part if not current else f"{current}, {part}"
            if len(candidate) > 82:
                lines.append(current + ",")
                current = part
            else:
                current = candidate
        if current:
            lines.append(current)

        code_text = "\n".join(lines[:3])
        ax.text(
            LEFT + 0.028,
            code_y,
            code_text,
            fontsize=7.4,
            color=BLUE,
            va="top",
            family="monospace",
            linespacing=1.25,
        )

    section_title(ax, 0.315, "2", "Usage Summary")

    ax.text(
        LEFT + 0.015,
        0.270,
        "Reports, primers, presentations, and other branded communications: follow the Myriad Pro hierarchy on page 1.",
        fontsize=8.5,
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT + 0.015,
        0.238,
        "Web applications: use the shared system sans-serif and monospace definitions above.",
        fontsize=8.5,
        color=BLUE,
        va="top",
    )

    ax.text(
        LEFT + 0.015,
        0.165,
        "Web implementation reference",
        fontsize=8.6,
        fontweight="bold",
        color=BLUE,
        va="top",
    )
    ax.text(
        LEFT + 0.015,
        0.140,
        "Current web design tokens, component guidance, and implementation details are maintained in:",
        fontsize=8.2,
        color=MED_BLUE,
        va="top",
    )
    ax.text(
        LEFT + 0.015,
        0.113,
        "github.com/pacificclimate/pcic-ui",
        fontsize=8.4,
        fontweight="bold",
        color=BLUE,
        va="top",
        url="https://github.com/pacificclimate/pcic-ui",
    )

    footer(ax)

    pdf.savefig(fig)
    plt.close(fig)

print(f"Created {OUTPUT}")
