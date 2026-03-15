#!/usr/bin/env python3
"""
Research Lab Agent Stack Diagram
Publication-quality visualization of the brain-inspired multi-agent architecture.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, RegularPolygon
import numpy as np

# Set up high-DPI figure
fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#FAFAFA')
ax.set_facecolor('#FAFAFA')

# Colors
GREEN = '#4CAF50'
RED = '#E44336'
TEAL = '#009688'
ORANGE = '#FF9800'
CHARCOAL = '#2D2D2D'
PURPLE = '#4A148C'
LIGHT_GREEN = '#81C784'
LIGHT_RED = '#E57373'

# Typography settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'dejavusans'

def draw_agent_node(x, y, role, agent_name, brain_region, agent_type='E', is_orchestrator=False):
    """Draw an agent node with role, name, and brain region."""

    # Determine color based on type
    if agent_type == 'I':
        color = RED
        edge_color = '#B71C1C'
    elif is_orchestrator:
        color = ORANGE
        edge_color = '#E65100'
    else:
        color = GREEN
        edge_color = '#2E7D32'

    # Draw node (rounded rectangle)
    width = 2.0
    height = 1.0

    if is_orchestrator:
        width = 2.4
        height = 1.1

    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle="round,pad=0.05,rounding_size=0.15",
                          facecolor=color, edgecolor=edge_color, linewidth=2)
    ax.add_patch(box)

    # Role name (bold, white)
    ax.text(x, y + 0.15, role.upper(), ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

    # Agent name (smaller, white)
    ax.text(x, y - 0.1, agent_name, ha='center', va='center',
            fontsize=6, color='white', alpha=0.9)

    # Brain region label below (italic, charcoal)
    ax.text(x, y - 0.75, brain_region, ha='center', va='top',
            fontsize=7, fontstyle='italic', color=CHARCOAL)

    # Type indicator for E/I
    type_label = 'E' if agent_type == 'E' else 'I'
    type_color = LIGHT_GREEN if agent_type == 'E' else LIGHT_RED
    circle = Circle((x + width/2 - 0.15, y + height/2 - 0.15), 0.12,
                    facecolor=type_color, edgecolor='white', linewidth=1)
    ax.add_patch(circle)
    ax.text(x + width/2 - 0.15, y + height/2 - 0.15, type_label,
            ha='center', va='center', fontsize=6, fontweight='bold', color='white')

    return (x, y)

def draw_checkpoint(x, y):
    """Draw a checkpoint diamond."""
    diamond = RegularPolygon((x, y), numVertices=4, radius=0.45, orientation=np.pi/4,
                              facecolor='#FFF9C4', edgecolor='#FBC02D', linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, 'CHECK', ha='center', va='center',
            fontsize=6, fontweight='bold', color=CHARCOAL)

def draw_arrow(start, end, color=TEAL, style='simple'):
    """Draw a flow arrow between nodes."""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                              connectionstyle='arc3,rad=0'))

# Title and subtitle
ax.text(0.5, 8.5, 'Research Lab Agent Stack', fontsize=20, fontweight='bold',
        color=CHARCOAL, ha='left', va='top', style='italic')
ax.text(0.5, 8.0, 'Brain-Inspired Multi-Agent Architecture', fontsize=12,
        color='#666666', ha='left', va='top')

# === DIRECTOR (Top, Orchestrator) ===
director = draw_agent_node(8, 7.5, 'Director', 'Main Session',
                           'Brainstem + Thalamus', is_orchestrator=True)

# === WAVE 1 (Left side) ===
scientist = draw_agent_node(2, 5.5, 'Scientist', 'ClaudeResearcher',
                            'Prefrontal Cortex', agent_type='E')
skeptic = draw_agent_node(2, 3.5, 'Skeptic', 'GrokResearcher',
                          'Amygdala', agent_type='I')
historian = draw_agent_node(2, 1.5, 'Historian', 'Research skill',
                            'Temporal Cortex', agent_type='E')

# === CHECKPOINT ===
checkpoint = draw_checkpoint(4.5, 3.5)

# === WAVE 2 (Center-right) ===
experimenter = draw_agent_node(6.5, 5.5, 'Experimenter', 'CodexResearcher',
                               'Motor Cortex', agent_type='E')
philosopher = draw_agent_node(6.5, 3.5, 'Philosopher', 'Thinking skill',
                              'Limbic System', agent_type='E')
explainer = draw_agent_node(6.5, 1.5, 'Explainer', 'GeminiResearcher',
                            'Language Areas', agent_type='E')

# === OUTPUT STAGE (Right) ===
artist = draw_agent_node(11, 4.5, 'Artist', 'Media skill',
                         'Visual Cortex', agent_type='E')
archivist = draw_agent_node(14, 4.5, 'Archivist', 'File Write',
                            'Hippocampus', agent_type='E')

# === SYNTHESIZER (Bottom) ===
synthesizer = draw_agent_node(8, 0.8, 'Synthesizer', 'PerplexityResearcher',
                              'Default Mode Network', agent_type='E')

# === DRAW FLOW ARROWS ===

# Wave 1 to checkpoint
draw_arrow((3.0, 5.5), (4.2, 3.7), TEAL)
draw_arrow((3.0, 3.5), (4.2, 3.5), TEAL)
draw_arrow((3.0, 1.5), (4.2, 3.3), TEAL)

# Checkpoint to Wave 2
draw_arrow((4.8, 3.5), (5.5, 3.5), TEAL)
draw_arrow((4.8, 3.6), (5.5, 5.5), TEAL)
draw_arrow((4.8, 3.4), (5.5, 1.5), TEAL)

# Wave 2 to Artist
draw_arrow((7.5, 5.5), (10.0, 4.7), TEAL)
draw_arrow((7.5, 3.5), (10.0, 4.5), TEAL)
draw_arrow((7.5, 1.5), (10.0, 4.3), TEAL)

# Artist to Archivist
draw_arrow((12.0, 4.5), (13.0, 4.5), TEAL)

# Director connections (dashed, to show orchestration)
for node in [scientist, skeptic, historian, experimenter, philosopher, explainer, artist, archivist, synthesizer]:
    ax.plot([director[0], node[0]], [director[1] - 0.55, node[1] + 0.5],
            color=ORANGE, linestyle='--', linewidth=0.8, alpha=0.4)

# Synthesizer connections (dashed, to show integration)
for node in [scientist, skeptic, historian, experimenter, philosopher, explainer]:
    ax.plot([node[0], synthesizer[0]], [node[1] - 0.5, synthesizer[1] + 0.4],
            color=PURPLE, linestyle=':', linewidth=0.8, alpha=0.4)

# === WAVE LABELS ===
ax.text(2, 6.5, 'WAVE 1', ha='center', fontsize=9, fontweight='bold',
        color=CHARCOAL, alpha=0.7)
ax.text(6.5, 6.5, 'WAVE 2', ha='center', fontsize=9, fontweight='bold',
        color=CHARCOAL, alpha=0.7)
ax.text(12.5, 5.8, 'OUTPUT', ha='center', fontsize=9, fontweight='bold',
        color=CHARCOAL, alpha=0.7)

# === INSIGHT CALLOUTS ===
ax.text(10.5, 8.2, '*E/I balance mirrors neural computation*',
        fontsize=8, fontstyle='italic', color=PURPLE, ha='left')
ax.text(10.5, 7.8, '*Wave gates ensure quality control*',
        fontsize=8, fontstyle='italic', color=PURPLE, ha='left')
ax.text(10.5, 7.4, '*Parallel processing with convergent synthesis*',
        fontsize=8, fontstyle='italic', color=PURPLE, ha='left')

# === LEGEND ===
legend_x = 0.5
legend_y = 0.3

# E/I Legend
e_box = FancyBboxPatch((legend_x, legend_y), 0.3, 0.2,
                        boxstyle="round,pad=0.02", facecolor=GREEN,
                        edgecolor='#2E7D32', linewidth=1)
ax.add_patch(e_box)
ax.text(legend_x + 0.4, legend_y + 0.1, 'Excitatory (E) - Generate ideas',
        fontsize=7, color=CHARCOAL, va='center')

i_box = FancyBboxPatch((legend_x + 3.5, legend_y), 0.3, 0.2,
                        boxstyle="round,pad=0.02", facecolor=RED,
                        edgecolor='#B71C1C', linewidth=1)
ax.add_patch(i_box)
ax.text(legend_x + 3.9, legend_y + 0.1, 'Inhibitory (I) - Can HALT process',
        fontsize=7, color=CHARCOAL, va='center')

# === FOOTER (CAVE WALL PRINCIPLE) ===
ax.text(8, 0.05, 'Research reveals patterns that already exist',
        fontsize=10, fontstyle='italic', color=CHARCOAL, ha='center',
        alpha=0.8)

# Save figure
plt.tight_layout()
plt.savefig('/home/peace/research-governance-physics/results/research_stack_diagram.png',
            dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(),
            edgecolor='none', transparent=False)
print('Diagram saved to /home/peace/research-governance-physics/results/research_stack_diagram.png')
