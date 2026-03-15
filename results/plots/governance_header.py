#!/usr/bin/env python3
"""
Header Image: Interconnected Governance Nodes
A professional scientific illustration showing the network topology of governance structures
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, ConnectionPatch, FancyArrowPatch
from matplotlib.collections import LineCollection
import matplotlib.colors as mcolors

# Set up the figure with a clean, professional style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 10), facecolor='#fafafa')
ax.set_facecolor('#fafafa')

# Create a hierarchical network structure representing governance nodes
np.random.seed(42)

# Central governance hub
center = (0, 0)

# Level 1: Core governance nodes (inner ring - represents Dunbar-limited core team)
n_level1 = 6
level1_radius = 2
level1_angles = np.linspace(0, 2*np.pi, n_level1, endpoint=False)
level1_nodes = [(level1_radius * np.cos(a), level1_radius * np.sin(a)) for a in level1_angles]

# Level 2: Department/functional nodes (middle ring)
n_level2 = 18
level2_radius = 4.5
level2_angles = np.linspace(0, 2*np.pi, n_level2, endpoint=False) + np.pi/n_level2
level2_nodes = [(level2_radius * np.cos(a), level2_radius * np.sin(a)) for a in level2_angles]

# Level 3: Edge nodes (outer ring - represents extended network)
n_level3 = 36
level3_radius = 7
level3_angles = np.linspace(0, 2*np.pi, n_level3, endpoint=False)
level3_nodes = [(level3_radius * np.cos(a), level3_radius * np.sin(a)) for a in level3_angles]

# Color scheme - professional blue palette
color_center = '#1a365d'
color_level1 = '#2c5282'
color_level2 = '#4299e1'
color_level3 = '#90cdf4'
color_edge = '#bee3f8'

# Draw connections first (so they're behind nodes)
# Center to Level 1
for node in level1_nodes:
    ax.plot([center[0], node[0]], [center[1], node[1]],
            color='#a0aec0', linewidth=1.5, alpha=0.6, zorder=1)

# Level 1 to Level 2 (hierarchical)
for i, l1_node in enumerate(level1_nodes):
    # Connect to nearest 3 level2 nodes
    for j in range(3):
        l2_idx = (i * 3 + j) % n_level2
        l2_node = level2_nodes[l2_idx]
        ax.plot([l1_node[0], l2_node[0]], [l1_node[1], l2_node[1]],
                color='#a0aec0', linewidth=1.2, alpha=0.5, zorder=1)

# Level 2 to Level 3 (hierarchical)
for i, l2_node in enumerate(level2_nodes):
    # Connect to nearest 2 level3 nodes
    for j in range(2):
        l3_idx = (i * 2 + j) % n_level3
        l3_node = level3_nodes[l3_idx]
        ax.plot([l2_node[0], l3_node[0]], [l2_node[1], l3_node[1]],
                color='#a0aec0', linewidth=0.8, alpha=0.4, zorder=1)

# Peer connections within Level 1 (representing coordination)
for i in range(n_level1):
    for j in range(i+1, n_level1):
        if abs(i - j) <= 2 or abs(i - j) >= n_level1 - 2:
            ax.plot([level1_nodes[i][0], level1_nodes[j][0]],
                    [level1_nodes[i][1], level1_nodes[j][1]],
                    color='#cbd5e0', linewidth=1.5, alpha=0.4, linestyle='--', zorder=1)

# Draw nodes with gradients and shadows
def draw_governance_node(ax, pos, radius, color, label=None, zorder=2):
    # Shadow
    shadow = Circle((pos[0]+0.05, pos[1]-0.05), radius,
                    color='#000000', alpha=0.1, zorder=zorder-1)
    ax.add_patch(shadow)
    # Main node
    node = Circle(pos, radius, color=color, ec='#2d3748', linewidth=1.5, zorder=zorder)
    ax.add_patch(node)
    if label:
        ax.text(pos[0], pos[1], label, ha='center', va='center',
                fontsize=8, fontweight='bold', color='white', zorder=zorder+1)
    return node

# Central hub
draw_governance_node(ax, center, 0.6, color_center, 'G', zorder=10)

# Level 1 nodes (core governance - Dunbar limited)
for i, node in enumerate(level1_nodes):
    draw_governance_node(ax, node, 0.45, color_level1, zorder=8)

# Level 2 nodes (departments)
for i, node in enumerate(level2_nodes):
    draw_governance_node(ax, node, 0.35, color_level2, zorder=6)

# Level 3 nodes (edge/extended network)
for i, node in enumerate(level3_nodes):
    draw_governance_node(ax, node, 0.25, color_level3, zorder=4)

# Add annotation boxes
annotation_style = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#718096', alpha=0.95)

# Dunbar annotation
ax.annotate('Dunbar Core\n~150 relationships',
            xy=(level1_radius * 0.7, level1_radius * 0.7),
            xytext=(3.5, 3.5),
            fontsize=10, fontweight='bold', color='#2d3748',
            bbox=annotation_style,
            arrowprops=dict(arrowstyle='->', color='#718096', lw=1.5),
            zorder=20)

# Scaling annotation
ax.annotate('Coordination Cost\n$\lambda \\propto \\sqrt{N}$',
            xy=(level2_radius * 0.9, -level2_radius * 0.3),
            xytext=(6, -3.5),
            fontsize=10, fontweight='bold', color='#2d3748',
            bbox=annotation_style,
            arrowprops=dict(arrowstyle='->', color='#718096', lw=1.5),
            zorder=20)

# G constant annotation
ax.annotate('Governance Constant\nG $\\approx$ 0.1-1.0',
            xy=(-level2_radius * 0.5, level2_radius * 0.8),
            xytext=(-6.5, 5.5),
            fontsize=10, fontweight='bold', color='#2d3748',
            bbox=annotation_style,
            arrowprops=dict(arrowstyle='->', color='#718096', lw=1.5),
            zorder=20)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=color_center, edgecolor='#2d3748', label='Central Governance Hub'),
    mpatches.Patch(facecolor=color_level1, edgecolor='#2d3748', label='Core Team (Dunbar ~150)'),
    mpatches.Patch(facecolor=color_level2, edgecolor='#2d3748', label='Functional Units'),
    mpatches.Patch(facecolor=color_level3, edgecolor='#2d3748', label='Extended Network'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          framealpha=0.95, edgecolor='#a0aec0')

# Title and styling
ax.set_title('Governance Physics: Network Topology of Organizational Scaling',
             fontsize=16, fontweight='bold', color='#1a365d', pad=20)
ax.set_xlabel('Hierarchical Complexity', fontsize=11, color='#4a5568')
ax.set_ylabel('Coordination Span', fontsize=11, color='#4a5568')

ax.set_xlim(-9, 9)
ax.set_ylim(-9, 9)
ax.set_aspect('equal')
ax.axis('off')

# Add subtle grid circles to show scaling levels
for r in [level1_radius, level2_radius, level3_radius]:
    circle = Circle((0, 0), r, fill=False, color='#e2e8f0',
                    linestyle=':', linewidth=1, zorder=0)
    ax.add_patch(circle)

plt.tight_layout()
plt.savefig('/home/peace/research-governance-physics/results/plots/01_governance_header.png',
            dpi=300, bbox_inches='tight', facecolor='#fafafa', edgecolor='none')
plt.close()

print("Header image saved: 01_governance_header.png")
