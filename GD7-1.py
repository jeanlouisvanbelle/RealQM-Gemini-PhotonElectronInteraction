# =====================================================================
# RealQM Diamond Cut 3D Lattice Trajectory Analyzer (Deterministic v3.2)
# CORRECTED: Element-Explicit Scalar Extraction for Quick 3D Processing
# =====================================================================

import numpy as np

np.random.seed(42)
photons_per_angle = 1500  

# Macro Optical Properties
n_diamond = 2.417
critical_angle_rad = np.arcsin(1.0 / n_diamond) 

# RealQM Sub-Nanometer 3D Matrix Setup (Scale: 1.0 unit = 100 nm = 1000 Å)
lattice_constant = 0.00357 
atom_interaction_radius = lattice_constant * 0.45

# High-Fidelity Room-Temperature 3D Phonon Jitter (~0.05 Å)
phonon_jitter_std = 0.00005 

# Calibrated Microscopic Torque Scaling (Inversely matching n=2.417 phase velocity)
max_torque_rad = np.radians(3.4) 
atomic_hold_steps = 4 

# Macro Diamond Facet Profile Setup (Extruded 3D Tolkowsky Volume)
table_half_width = 0.3
girdle_half_width = 0.5
table_y = 0.2
girdle_y = 0.0
culet_y = -0.4
z_thickness = 0.4 # Diamond volume depth boundary

m_pav_left = (culet_y - girdle_y) / (0.0 - (-girdle_half_width))
b_pav_left = culet_y
m_pav_right = (culet_y - girdle_y) / (0.0 - girdle_half_width)
b_pav_right = culet_y

# 3D Normal Vectors for Pavilion Sides
normal_pav_left = np.array([np.cos(np.arctan(m_pav_left) + np.pi/2), np.sin(np.arctan(m_pav_left) + np.pi/2), 0.0])
if normal_pav_left[1] < 0: normal_pav_left = -normal_pav_left

normal_pav_right = np.array([np.cos(np.arctan(m_pav_right) - np.pi/2), np.sin(np.arctan(m_pav_right) - np.pi/2), 0.0])
if normal_pav_right[1] < 0: normal_pav_right = -normal_pav_right

sweep_angles_deg = np.arange(15, 76, 5)

print("="*82)
print("  REALQM RIGOROUS 3D LATTICE SWEEP: COMPONENT-EXPLICIT VECTOR COUPLING   ")
print("="*82)
print(f" {'Launch Angle':<14} | {'Brilliance (%)':<16} | {'Leakage (%)':<14} | {'Empty Space (%)':<16}")
print("-"*82)

for angle_deg in sweep_angles_deg:
    brilliance_returned = 0
    pavilion_leaked = 0
    total_atomic_interactions = 0
    total_free_space_skips = 0
    
    for p in range(photons_per_angle):
        # Rule 1: Initial State Uncertainty over 3D Entry Table Plane
        x = np.random.uniform(-table_half_width * 0.95, table_half_width * 0.95)
        y = table_y
        z = np.random.uniform(-z_thickness * 0.95, z_thickness * 0.95)
        
        theta_center = np.radians(angle_deg)
        theta_in = np.random.normal(theta_center, np.radians(1.5))
        phi_in = np.random.uniform(0, 2*np.pi) # 3D Azimuthal launch spread
        
        # Microscopic entry refraction angle
        theta_refracted = np.arcsin(np.clip(np.sin(theta_in) / n_diamond, -1.0, 1.0))
        
        vx = np.sin(theta_refracted) * np.cos(phi_in)
        vy = -np.cos(theta_refracted)
        vz = np.sin(theta_refracted) * np.sin(phi_in)
        
        active = True
        bounces = 0
        step_size = lattice_constant * 0.15  
        last_atom_coord = None
        
        while active and bounces < 35:
            # Rules 2 & 3: Fast 3D Diamond Cubic Matrix Indexing
            row_x = round(x / lattice_constant)
            row_y = round(y / lattice_constant)
            row_z = round(z / lattice_constant)
            
            nearest_grid_x = row_x * lattice_constant
            nearest_grid_y = row_y * lattice_constant
            nearest_grid_z = row_z * lattice_constant
            
            # Inject the interpenetrating diamond cubic diagonal offset shift
            if (row_x + row_y + row_z) % 2 != 0:
                nearest_grid_x += lattice_constant * 0.25
                nearest_grid_y += lattice_constant * 0.25
                nearest_grid_z += lattice_constant * 0.25
            
            # High-Fidelity 3D Thermal Phonon Jitter
            jx, jy, jz = np.random.normal(0, phonon_jitter_std, 3)
            
            dx = x - (nearest_grid_x + jx)
            dy = y - (nearest_grid_y + jy)
            dz = z - (nearest_grid_z + jz)
            dist_sq = dx**2 + dy**2 + dz**2
            
            current_atom_coord = (nearest_grid_x, nearest_grid_y, nearest_grid_z)
            
            if dist_sq <= atom_interaction_radius**2 and dist_sq > 1e-12:
                if current_atom_coord != last_atom_coord:
                    total_atomic_interactions += 1
                    dist = np.sqrt(dist_sq)
                    
                    # Core Right-Handed 3D Cross-Product Lorentz Torque Matrix
                    v_vec = np.array([vx, vy, vz])
                    r_vec = np.array([dx, dy, dz])
                    
                    rot_axis = np.cross(v_vec, r_vec)
                    axis_len = np.sqrt(np.sum(rot_axis**2))
                    
                    if axis_len > 1e-12:
                        rot_axis /= axis_len
                        theta_deflect = max_torque_rad * ((atom_interaction_radius - dist) / atom_interaction_radius)
                        
                        # Rodrigues' 3D Vector Rotation Formula (Clean mechanical hand-off)
                        cos_t = np.cos(theta_deflect)
                        sin_t = np.sin(theta_deflect)
                        v_rotated = v_vec * cos_t + np.cross(rot_axis, v_vec) * sin_t + rot_axis * np.dot(rot_axis, v_vec) * (1 - cos_t)
                        
                        # CORRECTED ELEMENTS HANDOFF: Extracted explicitly by array positioning indices
                        vx = v_rotated[0]
                        vy = v_rotated[1]
                        vz = v_rotated[2]
                    
                    for _ in range(atomic_hold_steps):
                        total_atomic_interactions += 1
                        
                    last_atom_coord = current_atom_coord
                else:
                    total_free_space_skips += 1
            else:
                total_free_space_skips += 1
                if dist_sq > atom_interaction_radius**2:
                    last_atom_coord = None 

            # Advance coordinates along 3D space vector
            x += vx * step_size
            y += vy * step_size
            z += vz * step_size
            
            # Depth confinement check (Z-boundary volume reflections)
            if np.abs(z) >= z_thickness:
                vz = -vz
                z += vz * step_size
                
            # Macro boundaries profile checking
            if vy > 0 and y >= table_y:
                if np.abs(x) <= table_half_width:
                    v_len = np.sqrt(vx**2 + vy**2 + vz**2)
                    if v_len > 1e-12 and np.abs(vy / v_len) >= (1.0 / n_diamond):
                        brilliance_returned += 1
                    else:
                        pavilion_leaked += 1 
                else:
                    pavilion_leaked += 1
                active = False
                break
                
            is_outside = False
            if x <= 0:
                if y < (m_pav_left * x + b_pav_left):
                    is_outside = True
                    normal = normal_pav_left
            else:
                if y < (m_pav_right * x + b_pav_right):
                    is_outside = True
                    normal = normal_pav_right
                    
            if is_outside:
                bounces += 1
                v_len = np.sqrt(vx**2 + vy**2 + vz**2)
                if v_len > 1e-12:
                    vx, vy, vz = vx/v_len, vy/v_len, vz/v_len
                
                # Full 3D dot product array tracking
                dot_prod = vx * normal[0] + vy * normal[1] + vz * normal[2]
                angle_incidence = np.arccos(np.clip(np.abs(dot_prod), -1.0, 1.0))
                
                if angle_incidence > critical_angle_rad:
                    # 3D Total Internal Reflection
                    vx = vx - 2.0 * dot_prod * normal[0]
                    vy = vy - 2.0 * dot_prod * normal[1]
                    vz = vz - 2.0 * dot_prod * normal[2]
                    x += vx * step_size
                    y += vy * step_size
                    z += vz * step_size
                    last_atom_coord = None  
                    continue
                else:
                    pavilion_leaked += 1
                    active = False
                    break

    total_steps = total_atomic_interactions + total_free_space_skips
    empty_space_ratio = (total_free_space_skips / total_steps) * 100 if total_steps > 0 else 0
    brill_pct = (brilliance_returned / photons_per_angle) * 100
    leak_pct = (pavilion_leaked / photons_per_angle) * 100
    
    print(f" {angle_deg:>3}° launch    | {brill_pct:>13.2f}% | {leak_pct:>11.2f}% | {empty_space_ratio:>13.2f}%")

print("="*82)
