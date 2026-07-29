# Ω_b preregistration — validity gate — 2026-07-29

A preregistration was ordered to test the corpus's forced Ω_b = 4/81 against the CHIME/FRB
dispersion–galaxy result, **with a step-zero validity check first**: does the paper DERIVE a baryon-density
constraint, or ASSUME one? The rule: if it assumes, the channel is not independent — record it and STOP,
do not manufacture a comparison. **The gate closed. No preregistration was written; no comparison was run.**

## The paper

Wang, Masui, et al., "Measurement of the Dispersion–Galaxy Cross-Power Spectrum with the Second CHIME/FRB
Catalog," *Phys. Rev. Lett.*, DOI 10.1103/9th9-qc51 = arXiv:2506.08932. First 5.1σ detection of spatial
correlations in FRB dispersion measure from cosmic structure (2873 FRBs × ~6M DESI Legacy galaxies,
0.05 < z < 0.5).

## The validity check — the paper ASSUMES Ω_b, does not derive it

Read at source (arXiv full text). The analysis **fixes the cosmology from Planck 2018** and measures the
*distribution* of baryons, not their abundance:

- Fiducial cosmology, fixed input (verbatim): *"compute its corresponding comoving distance χg using the
  **Planck-measured cosmology**"*; *"non-linear matter power spectrum computed using CAMB and the **Planck
  cosmology**."*
- Measured quantity: the plasma–galaxy cross-power **cutoff scale** *"the plasma–galaxy cross-power spectrum
  cuts off relative to the matter power spectrum at a scale k_cut⁻¹ = 0.9⁺⁰·⁴₋₀.₄ Mpc"* — the feedback/
  evacuation scale, plus galaxy-bias and FRB-population nuisance parameters.
- Ω_b as output: **none.** The paper presents no measured Ω_b (or Ω_b h²) constraint; baryon density is a
  fixed Planck input throughout. Consistent with the press framing (locating the "missing" baryons in the
  diffuse IGM, not weighing them).

**Determination: Ω_b is an assumed input (Planck 2018), not a derived output.**

## The finding, and the STOP

**The channel is NOT independent for validating a prediction of Ω_b.** A measurement that fixes Ω_b from
Planck cannot test the corpus's Ω_b = 4/81 — a comparison would be comparing 4/81 to *Planck's* baryon
density (which the FRB paper assumed), i.e. circular, not a test against an independent instrument. Per the
ruling, the finding is recorded and the pass STOPS. No preregistration is written; no comparison statistic,
decision rule, or outcome table is drafted; nothing is compared.

Recorded durably at `FINDINGS.md` F.2026-07-29-b (commit `2c4af9f`).

## For the record (not a comparison)

- The corpus quantity is the dimensionless **Ω_b = 2²/3⁴ = 4/81 = 0.0493827…** — a baryon *density
  fraction*, **not** Ω_b h². Any future test must state which the comparand reports and convert accordingly.
- Ω_b = 4/81 is testable only against **genuinely independent** Ω_b determinations — the Planck CMB
  likelihood *directly*, or BBN + primordial deuterium (D/H) — never against a downstream analysis (FRB
  cross-power, weak-lensing baryon-fraction, etc.) that *assumes* one of those as input. The CHIME/FRB
  cross-power is a baryon-**census/distribution** result; it is out of scope for an Ω_b test by construction.
- The T7 preregistration remains the template for when a genuinely-independent, Ω_b-*deriving* channel
  appears.

## Sources

- [PRL abstract (DOI 10.1103/9th9-qc51)](https://journals.aps.org/prl/abstract/10.1103/9th9-qc51)
- [arXiv:2506.08932 (abstract)](https://arxiv.org/abs/2506.08932)
- [arXiv:2506.08932 (full text)](https://arxiv.org/html/2506.08932v1)
- [CHIME "missing matter" press release (EurekAlert)](https://www.eurekalert.org/news-releases/1137025)

No paper or kernel changed by the comparison (there was none). The only durable record is the FINDINGS
screening entry.
