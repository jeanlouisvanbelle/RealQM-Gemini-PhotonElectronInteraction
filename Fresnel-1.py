import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# RealQM Simulation: Partial Reflection by a Discrete Quartz Grid
# Derived from "Lecture Z-1: How Amplitude Math works"
# =====================================================================

# 1. Physical Constants & Parameters (SI Units unless specified)
np.random.seed(42) # For reproducible statistical ensemble
N_photons = 50000   # Number of individual localized photon wavepackets

# Grid Geometry (Section II.2)
lattice_spacing = 0.4e-9  # 0.4 nm spacing between SiO2 units
electron_radius = 5.29e-11 # Bohr radius (interaction zone cross-section)

# Calculate the geometric probability of an interaction based on area ratio
# Cross-sectional area of the electron loop vs total area of the lattice cell
cell_area = lattice_spacing ** 2
interaction_area = np.pi * (electron_radius ** 2)
geometric_interaction_prob = interaction_area / cell_area

# Fresnel & Medium macro-properties for verification (Section III.2)
n1 = 1.0   # Vacuum
n2 = 1.5   # Quartz / Crown Glass
# Classical reflection coefficient r = -0.2 (180 degree phase reversal)
r_classical = (n1 - n2) / (n1 + n2) 
R_classical = r_classical ** 2  # 0.04 (4% Macro probability)

# 2. Simulate the Localized Photon Ensemble (Section II.1 & III.3)
# Each photon has a sub-nanometer impact position variation within the lattice cell
impact_x = np.random.uniform(-lattice_spacing/2, lattice_spacing/2, N_photons)
impact_y = np.random.uniform(-lattice_spacing/2, lattice_spacing/2, N_photons)

# Radial distance from the closest localized electron loop center (at origin 0,0)
radial_distance = np.sqrt(impact_x**2 + impact_y**2)

# Determinstic sorting based on the physical cross-section counter-boundary
# Photons striking inside the active force-field radius undergo immediate torque/back-scatter
reflected_mask = radial_distance <= electron_radius
transmitted_mask = ~reflected_mask

N_reflected = np.sum(reflected_mask)
N_transmitted = np.sum(transmitted_mask)

# 3. Calculate Statistical Outcomes
simulated_R = N_reflected / N_photons
simulated_T = N_transmitted / N_photons

# 4. Print the Scannable Summary
print("="*60)
print("             REALQM LOCALIZED SIMULATION RESULTS             ")
print("="*60)
print(f"Total Simulated Photon Ensemble : {N_photons:,}")
print(f"Lattice Geometry Unit Spacing   : {lattice_spacing * 1e9:.2f} nm")
print(f"Effective Electron Bohr Radius  : {electron_radius * 1e9:.4f} nm")
print(f"Calculated Geometric Ratio      : {geometric_interaction_prob * 100:.2f}%")
print("-"*60)
print(f"Photons Elastically Reflected   : {N_reflected:,} ({simulated_R*100:.2f}%)")
print(f"Photons Cleanly Transmitted     : {N_transmitted:,} ({simulated_T*100:.2f}%)")
print("-"*60)
print(f"Target Classical Fresnel Value  : {R_classical*100:.2f}%")
print(f"Simulation Absolute Deviation   : {abs(simulated_R - R_classical)*100:.4f}%")
print("="*60)

# 5. Visualizing the Spatial Cross-Section Decision Plane
plt.figure(figsize=(8, 8))
# Plot a subset for clean visual density tracking
visual_limit = 3000
plt.scatter(impact_x[:visual_limit] * 1e9, impact_y[:visual_limit] * 1e9, 
            c=['#e74c3c' if r else '#3498db' for r in reflected_mask[:visual_limit]], 
            s=2, alpha=0.6, label='Photons')

# Draw the physical interaction cross-section boundary
circle = plt.Circle((0, 0), electron_radius * 1e9, color='#c0392b', fill=False, linewidth=2, 
                    linestyle='--', label='Electron Force Loop Cross-Section')
plt.gca().add_patch(circle)

plt.xlim(-lattice_spacing*0.6*1e9, lattice_spacing*0.6*1e9)
plt.ylim(-lattice_spacing*0.6*1e9, lattice_spacing*0.6*1e9)
plt.xlabel("Lattice X-Axis Dimension (nm)", fontsize=11)
plt.ylabel("Lattice Y-Axis Dimension (nm)", fontsize=11)
plt.title("RealQM Localized Reflection Geometry inside a 0.4nm Grid Cell", fontsize=12, fontweight='bold')
plt.grid(True, linestyle=':', alpha=0.5)

# Custom legend mapping
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=6, label='Reflected (Hit Cross-Section)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#3498db', markersize=6, label='Transmitted (Empty Space Pass)'),
    Line2D([0], [0], color='#c0392b', lw=2, linestyle='--', label='Bohr Boundary ($r_B$)')
]
plt.legend(handles=legend_elements, loc='upper right')
plt.show()
