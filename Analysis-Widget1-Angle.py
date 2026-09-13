import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# RealQM Smooth Trend Analysis: Incorporating Spatial Beam Width
# Prepared for Jean Louis Van Belle's YouTube Lecture Series
# =====================================================================

np.random.seed(42)
photons_per_run = 5000  # High statistics for ultra-smooth lines
angles = np.arange(15, 75.1, 0.5) # Fine 0.5-degree resolution steps

# Lattice Properties (Crystalline Quartz Baseline)
num_layers = 6
lattice_spacing_z = 0.4e-9  
lattice_spacing_y = 0.5e-9  
electron_radius = 5.29e-11   

distribution_matrix = np.zeros((len(angles), num_layers + 1))

for i, base_angle in enumerate(angles):
    angle_rad = np.radians(base_angle)
    
    # Real-world Physics: Photons are spread across the macroscopic width of the beam
    # This uniformly maps them across the periodic boundaries of the lattice cells
    y_initials = np.random.uniform(0, lattice_spacing_y, photons_per_run)
    
    # Angular divergence (diffraction limit spread)
    divergence_spread = np.random.normal(0, 0.002, photons_per_run)
    photon_angles = angle_rad + divergence_spread
    
    for p in range(photons_per_run):
        theta = photon_angles[p]
        y_pos = y_initials[p]
        interacted = False
        
        for layer in range(num_layers):
            z_coord = (layer + 1) * lattice_spacing_z
            # Trajectory projection including its unique entry point
            y_intersect = y_pos + z_coord * np.tan(theta)
            
            # Check interaction against the periodic grid
            closest_atom_y = np.round(y_intersect / lattice_spacing_y) * lattice_spacing_y
            if np.abs(y_intersect - closest_atom_y) <= electron_radius:
                distribution_matrix[i, layer] += 1
                interacted = True
                break
                
        if not interacted:
            distribution_matrix[i, num_layers] += 1

# Convert to percentages
distribution_percentages = (distribution_matrix / photons_per_run) * 100

# 3. Render Pristine Presentation Graphics
plt.figure(figsize=(12, 6.5), dpi=300) # Maximum resolution for video production

colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#3498db', '#9b59b6', '#7f8c8d']
labels = [f'Layer {l+1} Reflections' for l in range(num_layers)] + ['Total Transmission (Pass)']

for state in range(num_layers + 1):
    plt.plot(angles, distribution_percentages[:, state], 
             color=colors[state], label=labels[state], 
             linewidth=3.0, alpha=0.85) # Smooth continuous lines

plt.xlim(15, 75)
plt.ylim(-2, 102)
plt.xlabel("Angle of Incidence (Degrees)", fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel("Statistical Outcome Probability (%)", fontsize=12, fontweight='bold', labelpad=10)
plt.title("RealQM Localized Distribution Dynamics: Spatial Ensemble Trends", fontsize=13, fontweight='bold', pad=15)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.9, edgecolor='lightgrey', fontsize=10)
plt.tight_layout()

# Save automatically with a production name
filename = "Analysis-Widget1-Angle.png"
plt.savefig(filename, bbox_inches='tight', dpi=300)
print(f"Success! Pristine video-ready line graph saved as: {filename}")
plt.show()
