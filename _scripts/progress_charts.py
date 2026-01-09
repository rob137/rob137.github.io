#!/usr/bin/env python3
"""
Generate charts showing AI progress scenarios using Rule of 72 projections.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Create output directory
output_dir = Path(__file__).parent.parent / "assets" / "images"
output_dir.mkdir(parents=True, exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

def rule_of_72_projection(years, growth_rate_percent):
    """Project growth over years given annual growth rate."""
    return np.power(1 + growth_rate_percent/100, years)

# Chart 1: Different growth rate scenarios over 10 years
fig, ax = plt.subplots()

years = np.linspace(0, 10, 100)

# Different scenarios
scenarios = [
    ("Moore's Law (~41%/yr)", 41, '#888888', '--'),      # Moore's law: 2x in 1.75 years
    ("Current AI Progress (~100%/yr)", 100, '#2563eb', '-'),  # Doubling every year (conservative for AI)
    ("Accelerated (+50% rate)", 150, '#059669', '-'),    # If growth rate increases 50%
    ("Accelerated (+100% rate)", 200, '#dc2626', '-'),   # If growth rate doubles
]

for label, rate, color, style in scenarios:
    multiplier = rule_of_72_projection(years, rate)
    ax.semilogy(years, multiplier, label=label, color=color, linestyle=style, linewidth=2)

ax.set_xlabel('Years from Now')
ax.set_ylabel('Cumulative Improvement (log scale)')
ax.set_title('AI Progress Scenarios: What If Growth Accelerates?')
ax.legend(loc='upper left')
ax.set_xlim(0, 10)
ax.set_ylim(1, 1e7)

# Add annotations
ax.axhline(y=1000, color='gray', linestyle=':', alpha=0.5)
ax.text(0.5, 1200, '1,000x', fontsize=9, color='gray')
ax.axhline(y=1000000, color='gray', linestyle=':', alpha=0.5)
ax.text(0.5, 1200000, '1,000,000x', fontsize=9, color='gray')

plt.tight_layout()
plt.savefig(output_dir / 'progress-scenarios.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Saved: {output_dir / 'progress-scenarios.png'}")


# Chart 2: The doubling problem visualization
fig, ax = plt.subplots()

minutes = np.arange(0, 61)
values = np.power(2.0, minutes)

ax.semilogy(minutes, values, color='#2563eb', linewidth=2)

# Highlight the specific points user asked about
ax.scatter([15, 57], [2**15, 2**57], color='#dc2626', s=100, zorder=5)
ax.annotate(f'Minute 15\n32,768', xy=(15, 2**15), xytext=(20, 2**15 * 100),
            arrowprops=dict(arrowstyle='->', color='#dc2626'),
            fontsize=10, color='#dc2626')
ax.annotate(f'Minute 57\n144 quadrillion', xy=(57, 2**57), xytext=(45, 2**57 / 100),
            arrowprops=dict(arrowstyle='->', color='#dc2626'),
            fontsize=10, color='#dc2626')

ax.set_xlabel('Minutes')
ax.set_ylabel('Size (log scale)')
ax.set_title('Something Doubling Every Minute')
ax.set_xlim(0, 60)

# Add context lines
ax.axhline(y=1e6, color='gray', linestyle=':', alpha=0.5)
ax.text(2, 2e6, '1 million', fontsize=9, color='gray')
ax.axhline(y=1e9, color='gray', linestyle=':', alpha=0.5)
ax.text(2, 2e9, '1 billion', fontsize=9, color='gray')
ax.axhline(y=1e12, color='gray', linestyle=':', alpha=0.5)
ax.text(2, 2e12, '1 trillion', fontsize=9, color='gray')

plt.tight_layout()
plt.savefig(output_dir / 'doubling-problem.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Saved: {output_dir / 'doubling-problem.png'}")


# Chart 3: Inference cost decline (actual data)
fig, ax = plt.subplots()

# Data points from research: 280x reduction Nov 2022 to Oct 2024
# Starting at $20/million tokens, ending at $0.07
months = np.array([0, 6, 12, 18, 24])  # Nov 2022 = 0, Oct 2024 = 24
costs = np.array([20, 8, 2, 0.5, 0.07])  # Approximate trajectory

ax.semilogy(months, costs, 'o-', color='#2563eb', linewidth=2, markersize=8)

ax.set_xlabel('Months (from Nov 2022)')
ax.set_ylabel('Cost per Million Tokens ($)')
ax.set_title('GPT-3.5-Level Inference Cost: 280x Drop in 2 Years')
ax.set_xlim(-1, 25)

# Add labels
ax.annotate('$20.00', xy=(0, 20), xytext=(2, 30), fontsize=10)
ax.annotate('$0.07', xy=(24, 0.07), xytext=(19, 0.02), fontsize=10)

# Shade the drop
ax.fill_between([0, 24], [0.01, 0.01], [20, 0.07], alpha=0.1, color='#2563eb')

plt.tight_layout()
plt.savefig(output_dir / 'inference-cost-decline.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Saved: {output_dir / 'inference-cost-decline.png'}")


# Chart 4: Hardware generations comparison
fig, ax = plt.subplots()

generations = ['A100\n(2020)', 'H100\n(2022)', 'B200\n(2024)', 'Projected\n(2026)']
x = np.arange(len(generations))

# Relative performance (normalized to A100 = 1)
training = [1, 3, 9, 27]  # ~3x per generation
inference = [1, 15, 60, 240]  # More dramatic for inference

width = 0.35
bars1 = ax.bar(x - width/2, training, width, label='Training (relative)', color='#2563eb')
bars2 = ax.bar(x + width/2, inference, width, label='Inference (relative)', color='#059669')

ax.set_ylabel('Performance (A100 = 1)')
ax.set_title('GPU Performance Across Generations')
ax.set_xticks(x)
ax.set_xticklabels(generations)
ax.legend()

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}x',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.0f}x',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(output_dir / 'gpu-generations.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Saved: {output_dir / 'gpu-generations.png'}")

print("\nAll charts generated successfully!")
