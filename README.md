# Verification Capsule — *Deriving α and sin²θ<sub>W</sub> from Spectral Balance*

This directory contains the **minimal Tier-Ω artefacts** required to verify the locked constants reported in:

> **Pham, T. T. D.**  
> *Deriving α and sin²θ<sub>W</sub> from Spectral Balance* (2025)  
> DOI: [10.5281/zenodo.15335014](https://doi.org/10.5281/zenodo.15335014)

---

## Verified Constants

| Quantity               | Value (ζ-scheme)                | Source Section |
|------------------------|----------------------------------|----------------|
| Fine-structure constant | **α⁻¹ = 137.036000**             | §6             |
| Weak mixing angle      | **sin²θ<sub>W</sub> = 0.231000** | §7             |
| Entropy saddle         | **m\* = 137** (ΔF(137) = 0)      | §6             |
| ζ-determinant ratio    | **R<sub>det</sub> = 1** (analytic); truncated → +0.395 | §4 |

All values match boxed predictions in the manuscript and are numerically reproduced here.



## 📂 Capsule Layout



verification/
├── data/
│   ├── eigvals\_mod.json      # 20 eigenvalues of D\_mod
│   ├── eigvals\_ph.json       # 20 eigenvalues of D\_ph (sign-fixed)
│   └── entropy\_row\.json      # ΔF values for 100 ≤ m ≤ 138
├── quick\_check.py            # Verifies constants and Ω-condition
├── make\_digest.py            # Recomputes SHA256SUMS.txt
├── SHA256SUMS.txt (+ .ots)   # Integrity ledger (OpenTimestamp)
└── README.md                 # This file


All public code is licensed under **MIT**.  
Data and documentation are licensed under **CC-BY-ND 4.0**.

---

## ⚙️ Quick Usage

### 1. Verify file integrity

bash
python3 make_digest.py
sha256sum -c SHA256SUMS.txt


### 2. Reproduce constants and saddle outputs

bash
python3 quick_check.py


**Expected output (rounded):**


Det ratio      = +0.395407        # Truncated product, sign-correct
ΔF(136)        = -0.0214
ΔF(137)        = +0.0000
ΔF(138)        = +0.0214
m              = 137
AlphaInv       = 137.036000
sin2_theta_W   = 0.231000
sigma_m        = 0.267
alpha_error    = 0.00195
All checks passed (constants locked)


### 3. Run Ω flip-phase falsification

bash
python3 quick_check.py --flip-phase


This intentionally flips the first phase eigenvalue.
The determinant ratio deviates from unity, violating Axiom Ω:


Ω violated (sign flip)


---

## ⚠️ Determinant Disclaimer

This script evaluates a **truncated product** (20 eigenvalues per operator) for demonstration purposes.
The full determinant identity $\det_{\zeta}(D_{\text{mod}}) = \det_{\zeta}(D_{\text{ph}})$ is proven analytically using heat-kernel techniques in the paper (Lemma 5.3) and is not reconstructed numerically here.

---

## 🔒 Availability of Full Proofs

Formal Lean 4 verification scripts and extended numerical tools are privately archived and available upon request for editorial or scholarly review.

📩 Contact: [thomas@observerfieldtheory.com](mailto:thomas@observerfieldtheory.com)
