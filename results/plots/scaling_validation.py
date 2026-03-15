#!/usr/bin/env python3
"""
Scaling Law Validation Plot: Dunbar Number Validation vs G Constant Uncertainty
Shows the confidence levels of different framework claims
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.colors as mcolors

# Set up the figure
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(16, 8), facecolor='white')

# Color scheme
color_validated = '#38a169'  # Green
color_plausible = '#d69e2e'  # Yellow/Gold
color_speculative = '#e53e3e'  # Red
color_unfalsifiable = '#718096'  # Gray

# ============================================================================
# LEFT PLOT: Claim Confidence Levels
# ============================================================================

ax1 = axes[0]

claims = [
    'Dunbar ~150\nCognitive Limit',
    'Coordination Cost\nScales Superlinearly',
    '$\\lambda \\propto \\sqrt{N}$\nScaling Law',
    'Universal Scaling\nfor Organizations',
    'G $\\approx$ 0.1-1.0\nGovernance Constant'
]

confidence = [0.78, 0.85, 0.55, 0.50, 0.25]
evidence_types = ['Cross-cultural validation',
                  'Network theory + observation',
                  'Theoretical derivation only',
                  'Mixed empirical support',
                  'Post-hoc fitting, no protocol']

colors = [color_validated, color_validated, color_plausible,
          color_plausible, color_unfalsifiable]

y_pos = np.arange(len(claims))

# Create horizontal bars with rounded edges
bars = ax1.barh(y_pos, confidence, height=0.6, color=colors,
                edgecolor='#2d3748', linewidth=1.5, alpha=0.85)

# Add confidence values on bars
for i, (bar, conf) in enumerate(zip(bars, confidence)):
    width = bar.get_width()
    label_color = 'white' if conf > 0.5 else '#2d3748'
    ax1.text(width - 0.03, bar.get_y() + bar.get_height()/2,
             f'{conf:.0%}', ha='right', va='center',
             fontsize=12, fontweight='bold', color=label_color)

# Add evidence type labels
for i, evidence in enumerate(evidence_types):
    ax1.text(0.02, i, evidence, ha='left', va='center',
             fontsize=9, color='#2d3748', style='italic',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))

ax1.set_yticks(y_pos)
ax1.set_yticklabels(claims, fontsize=11)
ax1.set_xlabel('Confidence Level', fontsize=12, fontweight='bold')
ax1.set_xlim(0, 1)
ax1.set_title('Framework Claims: Evidence Strength Assessment',
              fontsize=14, fontweight='bold', pad=15)

# Add vertical lines for thresholds
ax1.axvline(x=0.7, color=color_validated, linestyle='--', linewidth=1.5, alpha=0.7)
ax1.axvline(x=0.5, color=color_plausible, linestyle='--', linewidth=1.5, alpha=0.7)

# Threshold labels
ax1.text(0.72, -0.5, 'Validated', fontsize=9, color=color_validated, fontweight='bold')
ax1.text(0.52, -0.5, 'Plausible', fontsize=9, color=color_plausible, fontweight='bold')

# Legend
legend_patches = [
    mpatches.Patch(color=color_validated, label='High Confidence (Validated)'),
    mpatches.Patch(color=color_plausible, label='Medium Confidence (Plausible)'),
    mpatches.Patch(color=color_unfalsifiable, label='Low Confidence (Unfalsifiable)')
]
ax1.legend(handles=legend_patches, loc='lower right', fontsize=9)

# ============================================================================
# RIGHT PLOT: Validation vs Uncertainty
# ============================================================================

ax2 = axes[1]

# Create scatter plot showing validation level vs empirical support
framework_components = {
    "Dunbar's Number": {'validation': 0.85, 'empirical': 0.90, 'size': 800},
    "Kleiber's Law": {'validation': 0.95, 'empirical': 0.95, 'size': 1000},
    "City Scaling (West)": {'validation': 0.80, 'empirical': 0.75, 'size': 700},
    r"$\lambda \propto \sqrt{N}$": {'validation': 0.45, 'empirical': 0.35, 'size': 600},
    "G Constant": {'validation': 0.20, 'empirical': 0.15, 'size': 500},
    "Phase Transitions": {'validation': 0.40, 'empirical': 0.30, 'size': 450},
}

# Plot zones
ax2.fill([0.7, 1.0, 1.0, 0.7], [0.7, 0.7, 1.0, 1.0],
         color=color_validated, alpha=0.15, zorder=0)
ax2.fill([0.5, 0.7, 0.7, 0.5], [0.5, 0.5, 0.7, 0.7],
         color=color_plausible, alpha=0.15, zorder=0)
ax2.fill([0, 0.5, 0.5, 0], [0, 0, 0.5, 0.5],
         color='#e53e3e', alpha=0.1, zorder=0)

# Scatter plot
for name, props in framework_components.items():
    scatter = ax2.scatter(props['validation'], props['empirical'],
                         s=props['size'], c='#3182ce', edgecolors='#1a365d',
                         linewidths=2, alpha=0.8, zorder=5)

    # Position labels to avoid overlap
    offset_x = 0.03 if props['validation'] < 0.7 else -0.03
    ha = 'left' if props['validation'] < 0.7 else 'right'

    ax2.annotate(name, (props['validation'], props['empirical']),
                xytext=(offset_x, 0.04), textcoords='offset points',
                fontsize=10, fontweight='bold', ha=ha,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor='#a0aec0', alpha=0.9))

# Add diagonal reference line
ax2.plot([0, 1], [0, 1], 'k--', alpha=0.3, linewidth=1.5, zorder=1)

# Zone labels
ax2.text(0.85, 0.95, 'VALIDATED\nZONE', fontsize=10, fontweight='bold',
         color=color_validated, ha='center', alpha=0.7)
ax2.text(0.6, 0.6, 'PLAUSIBLE\nZONE', fontsize=10, fontweight='bold',
         color=color_plausible, ha='center', alpha=0.7)
ax2.text(0.25, 0.25, 'SPECULATIVE\nZONE', fontsize=10, fontweight='bold',
         color='#e53e3e', ha='center', alpha=0.7)

ax2.set_xlabel('Theoretical Validation Score', fontsize=12, fontweight='bold')
ax2.set_ylabel('Empirical Support Score', fontsize=12, fontweight='bold')
ax2.set_title('Framework Components: Validation vs Empirical Support',
              fontsize=14, fontweight='bold', pad=15)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# Add annotation for the key insight
ax2.annotate('G Constant falls in\nspeculative zone:\nno measurement protocol',
            xy=(0.20, 0.15), xytext=(0.45, 0.10),
            fontsize=9, color='#2d3748',
            arrowprops=dict(arrowstyle='->', color='#718096', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff5f5',
                     edgecolor='#fc8181', alpha=0.9))

# Grid
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/peace/research-governance-physics/results/plots/02_scaling_validation.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Scaling validation plot saved: 02_scaling_validation.png")
