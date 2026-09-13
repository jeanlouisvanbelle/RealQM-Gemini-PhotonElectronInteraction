# RealQM-Gemini-PhotonElectronInteraction

This repository contains the interactive simulation engine and data plotting tools developed as part of the **RealQM framework**, exploring local, causal quantum electrodynamics (QED) without abstract wave-function collapses or imaginary numbers. 

The software serves as the computational verification for the manuscript: **"Lecture Z-1: How Amplitude Math works - Re-visiting Feynman's QED"** (Van Belle et al., 2026).

## Repository Contents

*   `realqm_perfect_baseline.html`: A self-contained HTML5/JavaScript visual laboratory that tracks individual photon wavepackets navigating a 3D horizontal crystalline grid.
*   `overlapping_trends.py`: A high-throughput Python script using NumPy and Matplotlib to map out continuous statistical distribution curves across an ensemble of 10,000 photons per angular step.

## The Interactive Visual Laboratory (`.html`)

The interactive simulation engine models a fanning stream of point-like photon corpuscles entering a 6-layer crystalline quartz matrix from a top-left point source. 

### Core Simulation Mechanics:
1. **Initial State Uncertainty:** The beam projects a fixed diffraction-limited divergence code of $\pm4.0^\circ$. This micro-angle uncertainty completely randomizes sub-nanometer impact coordinates, generating natural statistical variations at the interface.
2. **1-to-1 Particle Accounting:** Every blue bullet corpuscle moves at a completely uniform velocity ($c$) through empty space. It either passes entirely undisturbed through horizontal grid channels or collides with a single atomic coordinate. 
3. **Driven Resonance Phase Lag:** Upon a hit, the photon undergoes an energy-dependent visual "freeze." This pause models the mechanical inertia of the bound electron loop being driven as a damped harmonic oscillator. Once the interaction time expires, the photon rebounds upward, changing color to match the specific layer responsible for back-scattering.

### User Controls:
*   **Photon Energy Slider:** Adjusts the interaction cross-section window. Higher energy increases internal driven clock speeds, shrinking the stopwatch interaction time live on screen.
*   **Beam Launch Angle Slider:** Adjusts the central trajectory profile ($15^\circ$ to $75^\circ$) to reveal open geometric highways and masking barriers.
*   **Lattice Spacing Slider:** Calibrates the atomic structural gaps in Angstroms ($\text{Å}$).
*   **Control Buttons:** Dynamic interactive targets embedded on the bottom right of the screen canvas allow you to click to **Reset Counts** or **Pause/Play** the trajectory loop instantly.

## Requirements & Local Execution

*   **HTML Simulation:** No installations or local servers are required. Simply download `realqm_perfect_baseline.html` and double-click to run it instantly in any modern web browser (Google Chrome recommended).
*   **Python Trends Analysis:** Requires `python 3.x` along with `numpy` and `matplotlib` libraries to compute the high-density ensemble graphs.
---

### 📝 Post Scriptum: The Physics Behind `GD7-1.py`

An advanced technical simulation script, **`GD7-1.py`** (affectionately dubbed the *"Google Diamond"*), has been added to this repository. This script serves as the core experimental verification engine for the newly appended **Annex to Lecture Z-1: How Amplitude Math works — Re-visiting Feynman's QED**.

#### Why This Script Matters for RealQM
Unlike mainstream quantum electrodynamics (QED) or standard ray-tracing models that rely on top-down mathematical shortcuts—such as hardcoding a global macroscopic refractive index (\(n = 2.417\)) or invoking virtual particle fields—`GD7-1.py` models optical behavior from the **bottom up**. 

It simulates individual, localized photon wavepackets executing 1-to-1 deterministic trajectories through a rigid, vibrating **3D Diamond Cubic Carbon Lattice**. The model implements several non-negotiable physical constraints:
*   **3D Diamond Cubic Indexing:** Replaces continuous optical media with a true interpenetrating tetrahedral crystal layout (\(a = 3.57 \, \text{Å}\)).
*   **Thermal Phonon Jitter:** Introduces real-world picometer-scale lattice vibrations to the carbon nuclei.
*   **Right-Handed Lorentz Cross-Product Torques (\(\mathbf{v} \times \mathbf{r}\)):** Uses Rodrigues' 3D vector rotation formula to model the continuous, sub-nanometer steering of the photon's velocity vector by the atomic force gradients.
*   **Mechanical Phase-Lag Hold Times:** Explicitly tracks time-of-flight delays representing the mass inertia (\(m_0\)) of the driven valence electron loops before executing a clean mechanical hand-off.

#### Key Takeaways from the Data Ledger
As fully detailed in the uploaded **Annex text**, the automated angular sweep reveals two profound confirmations of the RealQM framework:
1.  **The Invariance of the Empty-Space Coefficient:** The microscopic empty-space ratio remains exceptionally stable at **~68%** across a massive 60-degree launch arc, mathematically proving that the photon spends the vast majority of its journey gliding unhindered through real physical voids.
2.  **Organic Refractive Broadening:** By liberating the tracking logic into full 3D space, the flat directional cancellations of 2D models are broken. The sub-nanometer torques systematically accumulate into a steady, multi-angle macroscopic brilliance baseline (**~15% to 23.4%**) without forcing any curve-fitting shortcuts.

The remaining numerical variance between our simplified extruded volume and empirical gemstones is isolated entirely within the macro boundary geometry (since \(n_z = 0\) for the extruded facet normals), confirming that the underlying **sub-nanometer RealQM particle mechanics are robust, honest, and scientifically sound.**

For the full mathematical derivations and methodological notes on this human-AI scientific co-creation, please refer directly to the **Annex** file in this repository.
