import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# RealQM Batch Simulation Loop: Statistical Analysis of Grid Hits
# Derived from "Lecture Z-1: How Amplitude Math works"
# =====================================================================

# 1. Physics & Simulation Framework Setup
np.random.seed(137)  # Set the fine-structure constant inverse as seed for elegance
photons_per_run = 1000
angles = np.arange(15, 76, 5) # 15 to 75 degrees in steps of 5

# Lattice Dimensions matching our pristine crystalline layout
num_layers = 6
lattice_spacing_z = 0.4e-9  # 0.4 nm layer depth increments
lattice_spacing_y = 0.5e-9  # Horizontal spacing within a layer
electron_radius = 5.29e-11   # Interaction cross-section radius

# Containers to hold our end-state distributions for plotting
# End states: Layer 1, Layer 2, Layer 3, Layer 4, Layer 5, Layer 6, Transmitted (Index 6)
distribution_matrix = np.zeros((len(angles), num_layers + 1))

# 2. Execute the Structural Batch Loop
for i, base_angle in enumerate(angles):
    # Convert base incidence angle to radians
    angle_rad = np.radians(base_angle)
    
    # Apply the motivated Initial State Uncertainty (Gaussian angular dispersion ~1.0 mrad)
    # The beam divergence mimics the diffraction limit spread of a real UV-C source
    divergence_spread = np.random.normal(0, 0.001, photons_per_run) 
    photon_angles = angle_rad + divergence_spread
    
    for p in range(photons_per_run):
        theta = photon_angles[p]
        
        # Ray casting through our multi-layered grid
        # Track if the localized trajectory intersects any atomic cross-sections
        interacted = False
        
        for layer in range(num_layers):
            z_coord = (layer + 1) * lattice_spacing_z
            # Calculate where this specific ray intersects the plane of the current layer
            # y = z * tan(theta) offset from the centerline projection
            y_intersect = z_coord * np.tan(theta)
            
            # Find distance to the nearest localized atomic coordinate center in this row
            closest_atom_y = np.round(y_intersect / lattice_spacing_y) * lattice_spacing_y
            distance_to_atom = np.abs(y_intersect - closest_atom_y)
            
            # Strict Localized Selection Rule
            if distance_to_atom <= electron_radius:
                distribution_matrix[i, layer] += 1
                interacted = True
                break # Particle is elastically back-scattered, trajectory terminates
                
        if not interacted:
            # The photon sailed directly through the empty highways of all 6 layers
            distribution_matrix[i, num_layers] += 1

# Convert final raw counts into percentages for rigorous reporting
distribution_percentages = (distribution_matrix / photons_per_run) * 100

# 3. Generating the Comprehensive Statistical Graphics
plt.figure(figsize=(12, 7))
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#3498db', '#9b59b6', '#7f8c8d']
labels = [f'Layer {l+1}' for l in range(num_layers)] + ['Transmitted (Pass)']

# Create a stacked bar chart to display the structural evolution across angles
bottom_tracker = np.zeros(len(angles))
for state in range(num_layers + 1):
    plt.bar(angles, distribution_percentages[:, state], bottom=bottom_tracker, 
            width=3.5, color=colors[state], label=labels[state], edgecolor='black', alpha=0.85)
    bottom_tracker += distribution_percentages[:, state]

plt.xticks(angles, [f"{a}°" for a in angles], fontsize=11)
plt.yticks(fontsize=11)
plt.xlabel("Base Angle of Incidence (Degrees)", fontsize=12, fontweight='bold')
plt.ylabel("Statistical Distribution Percentage (%)", fontsize=12, fontweight='bold')
plt.title("RealQM Multi-Layer Statistical Distribution: Angle Dependency", fontsize=14, fontweight='bold', pad=15)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=11)
plt.tight_layout()
plt.show()

# 4. Display a Clean Summary of Specific Landmark Configurations
print("="*80)
print("             REALQM ANALYTICAL RUNS: LAYER TALLY BREAKDOWN            ")
print("="*80)
print(f"Angle | L1 (%) | L2 (%) | L3 (%) | L4 (%) | L5 (%) | L6 (%) | Transmitted (%)")
print("-"*80)
for i, a in enumerate(angles):
    p = distribution_percentages[i]
    print(f" {a}°  |  {p[0]:4.1f}  |  {p[1]:4.1f}  |  {p[2]:4.1f}  |  {p[3]:4.1f}  |  {p[4]:4.1f}  |  {p[5]:4.1f}  |    {p[6]:4.1f}")
print("="*80)
