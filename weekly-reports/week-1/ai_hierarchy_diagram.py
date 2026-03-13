"""
Week 1 — AI Hierarchy Diagram
Generates a visual diagram showing: Traditional AI → ML → DL → Generative AI
Run:  python weekly-reports/week-1/ai_hierarchy_diagram.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─── Config ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# ─── Concentric circles (outer → inner) ─────────────────
layers = [
    {"center": (5, 4.8), "r": 4.2, "color": "#1a3a5c", "edge": "#4a9eff",
     "label": "Traditional AI", "label_pos": (5, 9.3)},
    {"center": (5, 4.5), "r": 3.2, "color": "#1c4a3a", "edge": "#4ade80",
     "label": "Machine Learning", "label_pos": (5, 7.95)},
    {"center": (5, 4.2), "r": 2.2, "color": "#4a2040", "edge": "#f472b6",
     "label": "Deep Learning", "label_pos": (5, 6.6)},
    {"center": (5, 4.0), "r": 1.2, "color": "#4a3a10", "edge": "#facc15",
     "label": "Generative AI", "label_pos": (5, 4.0)},
]

for layer in layers:
    circle = plt.Circle(
        layer["center"], layer["r"],
        facecolor=layer["color"], edgecolor=layer["edge"],
        linewidth=2.5, alpha=0.85
    )
    ax.add_patch(circle)
    lx, ly = layer["label_pos"]
    ax.text(lx, ly, layer["label"],
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=layer["edge"],
            fontfamily='sans-serif')

# ─── Subtitle descriptions ──────────────────────────────
descriptions = [
    (5, 8.75, "Rule-based systems, Expert systems", "#7fb8ff", 9),
    (5, 7.55, "Supervised, Unsupervised, Reinforcement", "#86efac", 9),
    (5, 6.2,  "Neural Networks, CNNs, RNNs, Transformers", "#f9a8d4", 9),
    (5, 3.5,  "LLMs · ChatGPT · Claude · Perplexity", "#fde68a", 9),
]

for x, y, text, color, size in descriptions:
    ax.text(x, y, text, ha='center', va='center', fontsize=size,
            color=color, alpha=0.8, fontstyle='italic', fontfamily='sans-serif')

# ─── Title ───────────────────────────────────────────────
ax.text(5, 0.6, "AI  HIERARCHY",
        ha='center', va='center', fontsize=22, fontweight='bold',
        color='#e2e8f0', fontfamily='sans-serif')

ax.text(5, 0.15, "Week 1 — Generative AI Engineering Program",
        ha='center', va='center', fontsize=10, color='#94a3b8',
        fontfamily='sans-serif')

plt.tight_layout()
plt.savefig("weekly-reports/evidence/week1-ai-hierarchy.png", dpi=150,
            bbox_inches='tight', facecolor='#0d1117')
plt.show()
print("\n✅ Diagram saved → weekly-reports/evidence/week1-ai-hierarchy.png")
