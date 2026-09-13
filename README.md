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
