# -*- coding: utf-8 -*-
"""b616_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R226)(3): THE CLAIMS OF CLUSTER 2G'S SEVEN PAPERS AND TWO SIMULATORS.

### Every claim is the seat's one-sentence restatement of a paper's (or a simulator's) sentence, carried with a needle that must occur on the
### cited line at PLACE-papers 3dd4f29; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, confirmed by (R222)(1): kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. THE SIMULATORS, (R226)(3): a simulator's claim grades computationally-verified only where a bank holds the run;
### where none does, the claim is graded by what its text states, and the bank search is printed. A ROUTE is a claim offered as an argument
### toward RH, simplicity or the open clause; each is read through the sieve's five tests in order. A pin RESOLVES, by the rule (R223)(1)
### confirms, when its commit is in the clone and at the remote. THE LOAD-BEARING CLAUSE, OPEN_TRAILS :12699: the tier reads KC only when a
### kernel-verified row is load-bearing for the thesis the head states.
### QUATERNIONIC :228 names TECHNE once; the row carries a pointer alone (the sha256 of TECHNE-Core's tracked-file manifest).
### THE REMOTE READS, OPEN_TRAILS :12703: every remote is read once per run (remote_refs), each ls-remote counted per repository in LSR.
### This module writes nothing: `python tools/b616_claims.py` runs the resolvers and prints.
"""
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
PRE_PP = '3dd4f29'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_D = 'phase2/physics-speculative/'
PAPERS = {
    'SF': (_D + 'SYMMETRY_FILTER.md', 'p2-d1', 301),
    'LC': (_D + 'LOCAL_COSMIC.md', 'p2-d2', 302),
    'TC': (_D + 'T7_CMB.md', 'p2-d3', 303),
    'QD': (_D + 'QUATERNIONIC.md', 'p2-d4', 304),
    'DM': (_D + 'DARK_DELTA_MU.md', 'p2-d5', 305),
    'FD': (_D + 'FORMATION_DISTANCE.md', 'p2-d6', 306),
    'TH': (_D + 'THEORY_SPACE.md', 'p2-d7', 307),
    'QI': (_D + 'qec_kappa_infrastructure.py', 'p2-d8', 308),
    'QV': (_D + 'qec_kappa_v2.py', 'p2-d9', 309),
}
SIMULATORS = ('QI', 'QV')
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel pins the papers name with a terminal: none -- no paper of the cluster names a declaration at a pin
PINS = {}
# ### the pins the papers name with no terminal, resolved for the record and certifying no row: key -> (repo, pin as cited, expected commit, where)
PINS_NT = {
    't7v03': ('SIDE-t7-topology-cmb', 'v0.3', '8eb0d5a', 'TC :172'),
    't7v01': ('SIDE-t7-topology-cmb', 'v0.1', '33c32a9', 'TC :174'),
    'lci': ('SIDE-local-cosmic-interface', '7a62ced', '7a62ced', 'LC :163'),
    'qds': ('SIDE-quaternionic-dark-sector', 'e860142', 'e860142', 'QD :236'),
}
# ### the reads at those pins, for the record (not a certifying read): key -> (pin key, file, line, needle, what stands there)
NTREADS = {
    't7_h1': ('t7v03', 'SIDET7TopologyCMB/Basic.lean', 62, 'def H1_free_rank : Nat := 1',
              '`H1_free_rank := 1` and `H1_torsion_rank := 3` entered by definition (:62-:63), the homology the paper states read in as numerals'),
    'lci_k': ('lci', 'SIDELocalCosmicInterface/Basic.lean', 52, 'def kappa_x100 : Channel → Nat',
              '`kappa_x100` defined by cases on the eight channels (:52-:60), `em_98` to `dark_0` by decide (:62-:69): the paper’s estimates as '
              'definitions'),
    'qds_dm': ('qds', 'SIDEQuaternionicDarkSector/Basic.lean', 70, 'def dm_per_element : Frac := ⟨16, 9⟩',
               '`dm_per_element := ⟨16, 9⟩` (:70) and `dm_total_eq_16_over_3` by decide (:74): arithmetic over weights the file defines'),
}
# ### the registered run's bank (TC :172-:178): the results file the pipeline wrote, committed at the pipeline's main
T7BANK = ('SIDE-t7-topology-cmb', '575a802', 't7_results.json', 'a340fabf74c720f39cdcbd994177fc47')
UNPINNED = {}

T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
R1 = ('R1', 'DARK', 2, T2, 'the SIDE Exclusion Principle the papers name is the mechanism enumeration: its compiled exclusions are conditions on a '
                          'real σ naming no function, so they hold beside the Epstein configuration the detector meets at ρ_E', 'RH-60')

C = [
    # ---------------------------------------------------------------- SYMMETRY_FILTER (p2-d1)
    ('SF-01', 'SF', 12, 'Using formation analysis applied to 439 fundamental constants across 50 sectors', 'SF reads formation analysis of 439 '
     'constants in 50 sectors as an interface that transmits gauge-invariant content at κ ≈ 0.8–0.98 and blocks symmetry-breaking content at '
     'κ ≈ 0.', 'synthesis-suggested', 'reading', 'the abstract’s reading of the channels at :38-:54 and the census at :62-:100', None),
    ('SF-02', 'SF', 12, 'The five violations of P-smooth arithmetic structure among 439 constants cluster exclusively', 'SF reports that the five '
     'P-smooth violations among 439 constants cluster at the local–cosmic boundary, p < 6 × 10⁻⁵.', 'computationally-verified', 'computation',
     'reported at :82-:100; its bins table (:64-:74) sums to 279 constants and 265 P-smooth, not 439 and 434 (the claim bank)', None),
    ('SF-03', 'SF', 20, 'we measure the conservation strength kappa across eight observational channels', 'SF states that κ measured across '
     'eight channels shows a sharp gradient, gauge-invariant content crossing near 1 and symmetry-breaking content blocked at 0.',
     'statement-grade', 'statement', 'the eight values at :38-:52 are given without a measurement procedure', None),
    ('SF-04', 'SF', 26, "measures how much of Q's internal structure survives transmission through I", 'SF defines κ(Q, I) as how much of Q’s '
     'internal structure survives transmission through I, 1 conserving all relationships and 0 none.', 'statement-grade', 'statement',
     'a definition with no formula', None),
    ('SF-05', 'SF', 28, 'Delta-mu equals n minus mu', 'SF defines the formation distance Δμ = n − μ, μ the sum of the κ values over n relationships.',
     'statement-grade', 'statement', 'a definition', None),
    ('SF-06', 'SF', 30, 'if its rational approximation factors entirely through the prime set P', 'SF calls a constant P-smooth when a rational '
     'approximation of it factors through a fifteen-prime set, with corrections at orders of α.', 'statement-grade', 'statement',
     'a definition; the approximation’s tolerance is not stated', None),
    ('SF-07', 'SF', 38, '**Channel 1: Electromagnetism (kappa = 0.98).**', 'SF assigns κ = 0.98 to electromagnetism down to κ = 0 for the dark '
     'sector over eight channels.', 'statement-grade', 'statement', 'values assigned at :38-:52 without a stated measurement; SIDE-local-cosmic-'
     'interface 7a62ced enters them as definitions', None),
    ('SF-08', 'SF', 54, 'The interface is a symmetry filter.', 'SF reads the channels near κ = 1 as gauge-invariant and those near 0 as '
     'symmetry-breaking, and calls the interface a symmetry filter.', 'synthesis-suggested', 'reading', 'a reading at :54', None),
    ('SF-09', 'SF', 76, 'The linear fit gives kappa = 1.047 minus 0.039 times distance', 'SF gives a linear fit of the P-smooth rate against '
     'distance with slope −0.039 and correlation r = −0.66.', 'computationally-verified', 'computation', 'reported at :76; the line and r '
     'recomputed from the bins table’s rates in the claim bank', None),
    ('SF-10', 'SF', 82, 'exactly 5 are violations (1.1%)', 'SF reports exactly five violations among 439 constants, 1.1 percent.',
     'computationally-verified', 'computation', 'reported at :82; its own bins table (:64-:74) leaves 14 constants not P-smooth', None),
    ('SF-11', 'SF', 91, 'Observing zero is a 1.9% event.', 'SF reports that zero violations among 350 local constants is a 1.9 percent event '
     'and the clustering pattern p ≈ 5.8 × 10⁻⁵.', 'computationally-verified', 'computation', 'reported at :91 without its model; the claim bank '
     'recomputes (1 − 5/439)^350 and the draw of five from 439', None),
    ('SF-12', 'SF', 96, '- theta-13 mixing (PMNS matrix)', 'SF lists θ₁₃ mixing among the five violations.', 'statement-grade', 'statement',
     'against :112, which marks sin²θ₁₃ P-smooth with κ = 1.0', None),
    ('SF-13', 'SF', 121, 'The discriminating variable is symmetry content.', 'SF argues from the neutrino table that within one sector the mixing '
     'angles are P-smooth and the mass-squared differences are not, so symmetry content discriminates.', 'argument-supported', 'argument',
     'argued from the table at :108-:115', None),
    ('SF-14', 'SF', 131, 'The residual tension IS Delta-mu.', 'SF reads the Hubble tension as the formation distance, one formation unit blocked '
     'between local and cosmic measurement.', 'statement-grade', 'statement', 'stated at :131', None),
    ('SF-15', 'SF', 141, 'separated by approximately 6–8 km/s/Mpc', 'SF predicts the local and cosmic H₀ values stabilizing about 6–8 km/s/Mpc '
     'apart, Δμ = 1 in H₀ units.', 'statement-grade', 'statement', 'a prediction; the values it quotes at :127 differ by 5.68 km/s/Mpc (the '
     'claim bank)', None),
    ('SF-16', 'SF', 139, 'A positive detection at ANY nonzero gauge charge refutes this framework.', 'SF predicts that no dark matter particle with '
     'Standard Model gauge charge will be found, a positive detection refuting the framework.', 'statement-grade', 'statement',
     'a falsifiable prediction, stated', None),
    ('SF-17', 'SF', 153, 'the product formula (the archimedean-multiplicative interface) is s-dark', 'SF reads the gauge group at the local–cosmic '
     'interface as the analogue of the product formula, which it calls s-dark at the scale of ζ.', 'statement-grade', 'statement',
     'an analogy stated at :153-:155', None),
    ('SF-18', 'SF', 161, 'This paper does NOT claim to know what dark matter is.', 'SF states that it does not claim to know what dark matter is, '
     'only what makes it dark.', 'statement-grade', 'statement', 'the paper’s own scope at :161-:163', None),
    # ---------------------------------------------------------------- LOCAL_COSMIC (p2-d2)
    ('LC-01', 'LC', 12, 'CCC+TL is excluded by four independent observations', 'LC states that CCC+TL is excluded by four observations: '
     'supernova time dilation, the CMB blackbody, α-variation constraints and the Bullet Cluster.', 'argument-supported', 'argument',
     'argued at :86-:92; the table’s four zero scores (:68, :70, :73, :78) put σ₈ where :12 and :90 put α variation', None),
    ('LC-02', 'LC', 28, 'we assess kappa — the fraction of local structural information that successfully predicts', 'LC assesses κ per channel '
     'as the fraction of local structural information that predicts the cosmological observable.', 'statement-grade', 'statement',
     'an assessment, no procedure stated', None),
    ('LC-03', 'LC', 32, 'We use the 439-constant census from Constance: The Prime Mosaic (v13.0)', 'LC takes its P-smooth rates from the '
     '439-constant census of Constance v13.0.', 'statement-grade', 'statement', 'a census cited; no bank of it is read here', None),
    ('LC-04', 'LC', 55, 'Mean kappa (all channels): 0.70. Mean kappa (excluding dark): 0.80.', 'LC gives the mean κ as 0.70 over eight channels '
     'and 0.80 without the dark sector.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('LC-05', 'LC', 59, 'Channels with kappa greater than 0.7 transmit **gauge-invariant** quantities', 'LC reads the channels above 0.7 as '
     'transmitting gauge-invariant quantities and those near 0 as symmetry-breaking.', 'synthesis-suggested', 'reading', 'a reading at :59-:61',
     None),
    ('LC-06', 'LC', 79, '| **Total** | **21/24** | **10/24** | **14/24** | **20/24** |', 'LC totals its twelve-test comparison as 21 of 24 for '
     'ΛCDM, 10 for CCC+TL, 14 for MOND and 20 for the programme.', 'computationally-verified', 'computation', 'the column sums recomputed in '
     'the claim bank; the scores themselves are assigned at :67-:78', None),
    ('LC-07', 'LC', 82, 'MOND is excluded by two.', 'LC states that MOND is excluded by two observations and that ΛCDM and the programme have no '
     'outright failure.', 'argument-supported', 'argument', 'the zero scores at :67 and :73', None),
    ('LC-08', 'LC', 90, 'Tension: 100-fold.', 'LC states that CCC needs α to vary by 10⁻⁵ per Hubble time where atomic clocks allow below '
     '10⁻⁷, a hundred-fold tension.', 'computationally-verified', 'computation', 'the ratio recomputed in the claim bank', None),
    ('LC-09', 'LC', 98, 'The temporal distance is similar; the kappa values differ by 0.96.', 'LC states that BBN abundances and the dark matter '
     'density lie at similar temporal distance yet differ in κ by 0.96.', 'statement-grade', 'statement', 'the 0.96 is the P-smooth rate of '
     'SYMMETRY_FILTER’s bin 5 (SF :71), not a channel κ of :46-:53', None),
    ('LC-10', 'LC', 117, 'No model satisfies all four SIDE conditions for cosmology.', 'LC states that no cosmological model satisfies all four '
     'SIDE conditions, the dark sector being the failure of exhaustiveness.', 'argument-supported', 'argument', 'the table at :110-:115', None),
    ('LC-11', 'LC', 123, 'It extends Conservation of Spectra from number theory to cosmology.', 'LC states that the programme’s diagnostic extends '
     'Conservation of Spectra from number theory to cosmology.', 'statement-grade', 'statement', 'stated at :123', None),
    ('LC-12', 'LC', 163, 'SIDE-local-cosmic-interface `7a62ced`', 'LC’s era annotation names SIDE-local-cosmic-interface 7a62ced as the kernel '
     'leg, its κ×100 terminals a data table entered by definition.', 'statement-grade', 'statement', 'a pin with no terminal named; at 7a62ced '
     '`kappa_x100` is defined by cases and each value decided (SIDELocalCosmicInterface/Basic.lean :52-:69)', None),
    # ---------------------------------------------------------------- T7_CMB (p2-d3)
    ('TC-01', 'TC', 12, 'seven matched arc pairs at angular separations determined by the Fano incidence geometry', 'TC proposes a seven-fold '
     'non-orientable topology whose CMB signature is seven matched arc pairs at Fano-determined separations.', 'statement-grade', 'statement',
     'a proposal; the paper’s own :174 and :215 record the seven scales as corpus-underdetermined', None),
    ('TC-02', 'TC', 12, 'a 3-torus produces 3 matched circles, a Poincare dodecahedral space produces 12', 'TC distinguishes its signature from '
     'a 3-torus’s three matched circles and a dodecahedral space’s twelve.', 'statement-grade', 'statement', 'against :39 and :68, which count '
     'three pairs for the torus and six pairs for the dodecahedron, so the two counts are of different things', None),
    ('TC-03', 'TC', 22, '| l = 2 (quadrupole) | 201 | 1150 | 0.17 |', 'TC tabulates the observed low-multipole power against ΛCDM, the '
     'quadrupole at 0.17 of its prediction.', 'computationally-verified', 'computation', 'the four ratios at :22-:25 recomputed in the claim '
     'bank', None),
    ('TC-04', 'TC', 27, 'The combined power deficit at l = 2 through 5 is 24%.', 'TC gives the combined deficit at l = 2 to 5 as 24 percent.',
     'computationally-verified', 'computation', 'recomputed from the table in the claim bank', None),
    ('TC-05', 'TC', 49, 'with first homology group H_1 = Z direct sum (Z/2Z)-cubed', 'TC states that the Klein surface with seven Möbius strips '
     'on the Fano frame has H₁ = ℤ ⊕ (ℤ/2)³.', 'statement-grade', 'statement', 'stated without a construction; SIDE-t7-topology-cmb v0.3 enters '
     'the free rank 1 and the torsion rank 3 as definitions (SIDET7TopologyCMB/Basic.lean :62-:63)', None),
    ('TC-06', 'TC', 60, '- Total incidences: 21', 'TC counts 21 incidences in the Fano plane, seven lines of three points.', 'argument-supported',
     'argument', 'the count at :55-:60, recomputed in the claim bank', None),
    ('TC-07', 'TC', 70, '| T-seven | 7 arc pairs | **Non-orientable** | GL(3, F_2), order 168 | 7 matched arcs |', 'TC tabulates T-seven with '
     'seven arc pairs, non-orientable, its symmetry group GL(3, 𝔽₂) of order 168.', 'statement-grade', 'statement', 'GL(3, 𝔽₂) has order 168 '
     '(the claim bank); that it is the symmetry group of a cosmic topology is stated', None),
    ('TC-08', 'TC', 72, 'The polarization reflection is a unique, falsifiable signature that no orientable topology produces.', 'TC argues that '
     'orientation reversal makes the matched features arcs whose polarization is reflected, a signature no orientable topology produces.',
     'argument-supported', 'argument', 'argued at :72 and :98', None),
    ('TC-09', 'TC', 106, 'The eigenvalues of the Fano incidence matrix are 3 (multiplicity 1) and minus 1 (multiplicity 6).', 'TC states that the '
     'Fano incidence matrix has eigenvalues 3 once and −1 six times.', 'statement-grade', 'statement', 'the incidence matrix N has N Nᵀ = 2I + J, '
     'its other eigenvalues of modulus √2; 3 and −1 six times are the eigenvalues of the collinearity graph K₇ (the claim bank)', None),
    ('TC-10', 'TC', 144, 'Total: approximately 10-to-the-11 evaluations.', 'TC estimates the search at about 10¹¹ evaluations, 10⁶ pairs by 100 '
     'domain sizes by 1000 trials.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('TC-11', 'TC', 172, 'has now been **run once** on Planck 2018 SMICA', 'TC reports the pre-registered search run once on Planck 2018 SMICA with '
     'the frozen seed, pipeline SIDE-t7-topology-cmb v0.3 = 8eb0d5a.', 'computationally-verified', 'computation', 'the run banked as '
     't7_results.json at SIDE-t7-topology-cmb 575a802 on its main, read in the claim bank', None),
    ('TC-12', 'TC', 174, 'is therefore recorded as UNTESTED-AS-UNDERDETERMINED', 'TC records the seven-distinct-scale discriminator as untested '
     'and underdetermined, GL(3, 𝔽₂)’s transitivity collapsing the scales.', 'argument-supported', 'argument', 'argued at :174 and :190',
     None),
    ('TC-13', 'TC', 178, 'is **p = 0.046**', 'TC reports the best θ_min 54.0°, a near-zero statistic and a look-elsewhere p = 0.046, the Marginal '
     'band of its decision table.', 'computationally-verified', 'computation', 'the bank’s p_global_look_elsewhere and best θ_min, read in the '
     'claim bank', None),
    ('TC-14', 'TC', 180, '**the SIDE methodology is not falsified', 'TC states that the methodology is not falsified and the specific topology '
     'is unsupported at marginal at this sensitivity.', 'statement-grade', 'statement', 'the paper’s reading of its outcome D at :180', None),
    ('TC-15', 'TC', 199, '| Fano incidence eigenstructure | eigenvalues 3, −1×6 (two values)', 'TC’s derivation table again gives the Fano '
     'incidence eigenstructure as 3 and −1 six times.', 'statement-grade', 'statement', 'as TC :106', None),
    ('TC-16', 'TC', 213, '**functorial-limit negative theorem**', 'TC cites a negative theorem of another programme paper, that no canonical map '
     'takes the seven discriminants to the seven mechanism classes.', 'statement-grade', 'statement', 'a result of another paper cited by name, '
     'not read here', None),
    ('TC-17', 'TC', 215, 'the **seven-distinct-scale discriminator is corpus-underdetermined**', 'TC concludes that the substrate does not '
     'determine the seven lengths, every screened construction yielding at most three classes or one scale.', 'argument-supported', 'argument',
     'the screens at :194-:211', None),
    ('TC-18', 'TC', 225, 'The dark-to-visible ratio 77/4 (observed with 0.17% error) would be 7 (Fano elements) times 11/4', 'TC hypothesizes that '
     'the dark-to-visible ratio 77/4 is seven Fano elements times 11/4.', 'statement-grade', 'statement', 'a hypothesis by the paper’s own word '
     'at :227', None),
    # ---------------------------------------------------------------- QUATERNIONIC (p2-d4)
    ('QD-01', 'QD', 12, '(Ω_DM + Ω_Λ) / Ω_b ≈ 19.28 (Planck 2018)', 'QD gives the dark-to-baryon ratio as 19.28 from Planck 2018.',
     'computationally-verified', 'computation', 'recomputed from :22-:24 in the claim bank', None),
    ('QD-02', 'QD', 12, '7 × (11/4) = 77/4 = 19.25 (Decomposition A, error 0.17%)', 'QD fits the ratio by 7 × 11/4 = 77/4 at 0.17 percent and by '
     '16/3 + 14 = 58/3 at 0.26 percent.', 'computationally-verified', 'computation', 'recomputed in the claim bank (0.176 and 0.256 percent)',
     None),
    ('QD-03', 'QD', 12, 'Both use only the structural integers {2, 3, 7, 11} without free parameters.', 'QD states that both decompositions use '
     'only the integers 2, 3, 7 and 11 with no free parameter.', 'statement-grade', 'statement', 'stated at :12 and :35', None),
    ('QD-04', 'QD', 12, 'under the GL(3, 𝔽₂) parabolic stabilizer of the diagonal', 'QD places the (3, 3, 1) Hamming-weight partition under the '
     'GL(3, 𝔽₂) parabolic stabilizer of the diagonal.', 'statement-grade', 'statement', 'the stabilizer of the diagonal has order 24 and is '
     'transitive on the six other non-zero vectors, so its orbits are (6, 1) (the claim bank)', None),
    ('QD-05', 'QD', 30, '| DM / visible | 5.381 | 16/3 = 5.333 | 0.89% |', 'QD matches dark matter over visible, 5.381, to 16/3 at 0.89 percent and '
     'dark energy over visible, 13.903, to 14 at 0.70 percent.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('QD-06', 'QD', 35, 'The 1/12 = (58/3 − 77/4) discrepancy is the symmetry-breaking weight', 'QD reads the 1/12 between the two decompositions '
     'as the symmetry-breaking weight of the diagonal element.', 'statement-grade', 'statement', 'the difference recomputed in the claim bank; '
     'its reading as a weight is stated', None),
    ('QD-07', 'QD', 43, 'to the 7 nontrivial discriminants in ℚ\\*/(ℚ\\*)² generated by {−1, 2, 3}', 'QD identifies the seven non-identity '
     'elements of (ℤ/2)³ with the seven nontrivial square classes generated by −1, 2 and 3.', 'argument-supported', 'argument',
     'three independent order-2 generators give 2³ − 1 = 7 (:55)', None),
    ('QD-08', 'QD', 55, 'Identity-Formation Bijection (Theorem 5.1) makes this the same 7', 'QD states, citing the Identity-Formation Bijection, '
     'that this seven is the formation count of ξ(s).', 'statement-grade', 'statement', 'a result of another paper cited by name, not read here',
     None),
    ('QD-09', 'QD', 67, '- 11 is the necessity ceiling (M-theory dimensions', 'QD reads 11 as the necessity ceiling, the dimension count of M-theory.',
     'statement-grade', 'statement', 'stated at :67', None),
    ('QD-10', 'QD', 69, '- 11/4 = 2.750 matches the empirical factor 2.755 to 0.18%', 'QD matches the per-element weight 11/4 to the empirical '
     'factor 2.755 at 0.18 percent.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('QD-11', 'QD', 83, 'Verification: 3 × (16/9) = 16/3 (matches Ω_DM/Ω_b); 3 × (14/3) = 14', 'QD verifies that three weight-2 elements at 16/9 '
     'give 16/3 and three weight-1 elements at 14/3 give 14.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('QD-12', 'QD', 121, 'All six are satisfied by construction.', 'QD states that its six structural constraints are all satisfied by '
     'construction.', 'statement-grade', 'statement', 'the sixth (:119) rests on an injection into the gauge kernel the paper names and does not '
     'construct', None),
    ('QD-13', 'QD', 125, 'The stabilizer subgroup of the diagonal is the symmetric group S_3, permuting coordinates.', 'QD states that the '
     'stabilizer of the diagonal is S₃ permuting coordinates, with orbits of sizes 3, 3 and 1.', 'statement-grade', 'statement',
     'the stabilizer of (1, 1, 1) in GL(3, 𝔽₂) has order 168/7 = 24; the coordinate permutations are a subgroup of order 6 (the claim bank)',
     None),
    ('QD-14', 'QD', 135, 'Hamming distance 2 from the diagonal', 'QD places the weight-1 elements at Hamming distance 2 from the diagonal and the '
     'weight-2 elements at distance 1.', 'argument-supported', 'argument', 'the counting at :135-:137, recomputed in the claim bank', None),
    ('QD-15', 'QD', 139, 'The assignment maps "most-broken relative to a uniform fluid" to vacuum-like', 'QD assigns the most asymmetric elements '
     'the vacuum-like equation of state and the nearer ones the matter-like one.', 'statement-grade', 'statement', 'the abstract keeps the '
     'equation-of-state assignment open (:12)', None),
    ('QD-16', 'QD', 149, r'\frac{\Omega_b}{12} \approx 0.0041', 'QD gives the flatness deviation of the asymmetric decomposition as Ω_b/12 ≈ '
     '0.0041.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('QD-17', 'QD', 153, 'The 1/12 echoes ζ(−1) = −1/12', 'QD notes that the 1/12 echoes ζ(−1) = −1/12.', 'statement-grade', 'statement',
     'an echo the abstract leaves open (:12)', None),
    ('QD-18', 'QD', 177, 'The 16/9 and 14/3 weights are not free parameters.', 'QD states that the weights 16/9 and 14/3 are not free parameters, '
     'being forced by the partition matching the observed ratios.', 'statement-grade', 'statement', 'they are the observed ratios’ fits divided '
     'by three (:177)', None),
    ('QD-19', 'QD', 183, 'has zero projection onto the seven non-identity elements', 'QD states that α sees the identity element and has zero '
     'projection onto the seven non-identity elements, giving κ = 0 for dark channels.', 'statement-grade', 'statement', 'stated at :183', None),
    ('QD-20', 'QD', 197, 'the asymmetric decomposition predicts +0.41%', 'QD names its falsifiers: the ratio leaving 19.25 by more than 1σ, a '
     'gauge-charged detection, w ≠ −1, or flatness outside ±0.5 percent.', 'statement-grade', 'statement', 'predictions stated at :197', None),
    ('QD-21', 'QD', 228, '*v0.3 changes from v0.2: editorial discipline pass through', 'QD’s version note records an editorial pass through a tool '
     'of a private library, carried here by pointer alone.', 'statement-grade', 'statement', 'TECHNE-POINTER', None),
    ('QD-22', 'QD', 236, 'SIDE-quaternionic-dark-sector `e860142`', 'QD’s era annotation names SIDE-quaternionic-dark-sector e860142 as the kernel '
     'leg, its terminals arithmetic over weight data the file defines.', 'statement-grade', 'statement', 'a pin with no terminal named; at '
     'e860142 the weights are defined and their sums decided (SIDEQuaternionicDarkSector/Basic.lean :70-:74)', None),
    # ---------------------------------------------------------------- DARK_DELTA_MU (p2-d5)
    ('DM-01', 'DM', 12, 'It is the **formation distance** of the local↔cosmic interface', 'DM states that the dark sector is the formation distance '
     'of the local–cosmic interface, not a substance, an illusion or modified gravity.', 'statement-grade', 'statement', 'the thesis, stated; its '
     'own note at :153 rests it on the subtractive Δμ', None),
    ('DM-02', 'DM', 37, '(439 constants, Spearman ρ = −0.66)', 'DM reports the P-smooth degradation over 439 constants with Spearman ρ = −0.66.',
     'computationally-verified', 'computation', 'reported; −0.66 is the Pearson r of SYMMETRY_FILTER’s linear fit (SF :76), and Spearman ρ '
     'over the nine bins is −0.644 (the claim bank)', None),
    ('DM-03', 'DM', 58, 'Zero violations in 350 local constants.', 'DM reports zero violations among 350 local constants and a clustering '
     'probability near 5.8 × 10⁻⁵.', 'computationally-verified', 'computation', 'the count SYMMETRY_FILTER reports (SF :82-:91), restated',
     None),
    ('DM-04', 'DM', 69, '### 5. Contingency Hierarchy (Spearman ρ = 1.00, p < 0.001)', 'DM reports that the α-order of a constant rank-correlates '
     'perfectly with its derivation difficulty, Spearman ρ = 1.00.', 'computationally-verified', 'computation', 'reported without its data or the '
     'number of ranks', None),
    ('DM-05', 'DM', 83, '(Ω_DM + Ω_DE) / Ω_b = 7 × 11/4 = 77/4 = 19.25', 'DM gives the dark-to-visible ratio as 7 × 11/4 = 77/4 against the '
     'observed 19.28.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('DM-06', 'DM', 86, 'first prime non-{2,3}-smooth above the Størmer wall', 'DM reads 11 as the necessity ceiling, the M-theory dimension count.',
     'statement-grade', 'statement', 'stated at :86', None),
    ('DM-07', 'DM', 91, '81 = 3⁴ = n₂^(n₁+n₃)', 'DM reads 81 = 3⁴ = n₂^(n₁+n₃) as the formation phase space of the tuple (2, 3, 2, 0), four '
     'visible and 77 dark.', 'argument-supported', 'argument', 'the identity over the tuple, recomputed in the claim bank; the exponent n₁ + n₃ '
     'is the paper’s choice', None),
    ('DM-08', 'DM', 107, 'under the GL(3, 𝔽₂) parabolic stabilizer of the diagonal element', 'DM places the (3, 3, 1) partition under the '
     'parabolic stabilizer of the diagonal.', 'statement-grade', 'statement', 'as QD :12; the stabilizer’s orbits are (6, 1) (the claim bank)',
     None),
    ('DM-09', 'DM', 121, 'SU(3) × SU(2) × U(1) has no dark sector representations', 'DM gives three levels for κ = 0: gauge closure, the symmetry '
     'filter and quaternionic orthogonality.', 'statement-grade', 'statement', 'the table at :119-:123', None),
    ('DM-10', 'DM', 137, 'Distinguishable from 3-torus (3 circles), dodecahedron (12 circles), and infinite flat (none).', 'DM predicts seven '
     'matched arc pairs, distinguishable from a 3-torus’s three circles and a dodecahedron’s twelve.', 'statement-grade', 'statement',
     'as TC :12; against TC :39 and :68', None),
    ('DM-11', 'DM', 147, 'by showing that no mechanism class produces off-line zeros when the system is sealed', 'DM states that the SIDE Exclusion '
     'Principle settles RH by showing that no mechanism class produces off-line zeros once the system is sealed.', 'statement-grade',
     'statement', 'stated at :147; the argument it names is the mechanism enumeration the sieve reads at RH-60', R1),
    ('DM-12', 'DM', 149, 'the local↔cosmic interface is s-dark for symmetry-breaking information', 'DM extends Conservation of Spectra to '
     'cosmological scale, the local–cosmic interface s-dark for symmetry-breaking information.', 'statement-grade', 'statement',
     'stated at :149', None),
    ('DM-13', 'DM', 175, 'Δμ IS the dark sector.', 'DM closes on Δμ as the dark sector, a conservation property.', 'statement-grade', 'statement',
     'the paper’s statement at :173-:179', None),
    # ---------------------------------------------------------------- FORMATION_DISTANCE (p2-d6)
    ('FD-01', 'FD', 14, 'The universe has 81 parts. 4 are visible. 77 are dark.', 'FD states that the universe has 81 parts, 4 visible and 77 dark.',
     'statement-grade', 'statement', 'stated at :14 from the tuple identity at :16', None),
    ('FD-02', 'FD', 16, '77 = 81 − 4 = 7 × 11', 'FD derives 81 = n₂^(n₁+n₃) and 4 = n₁^n₃ from the tuple, 77 = 81 − 4 = 7 × 11.',
     'argument-supported', 'argument', 'the identity over the tuple at :16, recomputed in the claim bank', None),
    ('FD-03', 'FD', 22, 'The prediction sits 0.13σ from observation.', 'FD gives Ω_b = 4/81 = 0.04938 at 0.13σ from Planck’s 0.04930 ± 0.00066.',
     'computationally-verified', 'computation', 'recomputed in the claim bank (0.126σ)', None),
    ('FD-04', 'FD', 22, 'Five independent datasets, combined, place the dark-to-visible ratio at 0.03σ', 'FD reports five combined datasets '
     'placing the ratio 0.03σ from 77/4.', 'computationally-verified', 'computation', 'the datasets are not named; Planck’s values alone give '
     'about 0.11σ (the claim bank)', None),
    ('FD-05', 'FD', 46, 'but have κ = 0.96', 'FD states that BBN abundances at distance 5 have κ = 0.96 while the dark matter density at distance 7 '
     'has κ = 0.', 'statement-grade', 'statement', 'the 0.96 is SYMMETRY_FILTER’s bin-5 P-smooth rate (SF :71), as at LC :98', None),
    ('FD-06', 'FD', 77, 'the first prime that cannot be reached from {2, 3} by smoothness', 'FD reads 11 as the first prime not reached from 2 and '
     '3 by smoothness.', 'statement-grade', 'statement', 'every prime other than 2 and 3 is not {2, 3}-smooth; 5 and 7 come before 11', None),
    ('FD-07', 'FD', 108, 'Ω_total(B) − 1 = 1/243 = (1/12) × (4/81) = Ω_b / 12', 'FD gives the flatness deviation of Decomposition B as 1/243 = '
     'Ω_b/12.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('FD-08', 'FD', 112, 'is consistent with both Decomposition A (Ω_total = 1 exactly) and Decomposition B (Ω_total = 1.0041)', 'FD reads Planck’s '
     'Ω_K = −0.0007 ± 0.0019 as consistent with both decompositions.', 'argument-supported', 'argument', 'Decomposition B’s Ω_K = −1/243 lies '
     '1.8σ from the quoted value (the claim bank)', None),
    ('FD-09', 'FD', 128, 'Δμ = 77/4 = 19.25 means the dark structure is 19.25 times the visible structure', 'FD reads Δμ in cosmology as 77/4, the '
     'dark structure 19.25 times the visible.', 'statement-grade', 'statement', 'against :61, where Δμ = n − μ is a difference of counts, not a '
     'ratio', None),
    ('FD-10', 'FD', 145, '| DM/visible | 16/3 = 5.333 | 0.45σ from Planck |', 'FD places 16/3 at 0.45σ and 14 at 0.41σ from Planck.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('FD-11', 'FD', 161, 'the condition reads **UNDER PRESSURE** at a stated preference of three sigma or more', 'FD’s threshold clause, appended '
     'under (R38), reads the w = −1 condition UNDER PRESSURE at three sigma and FIRED at five.', 'statement-grade', 'statement', 'a ruling '
     'appended at b426 (:161)', None),
    ('FD-12', 'FD', 163, 'testable at approximately 2.5σ with CMB-S4 precision', 'FD predicts Ω_b = 4/81 testable at about 2.5σ with CMB-S4.',
     'statement-grade', 'statement', 'a prediction, stated', None),
    ('FD-13', 'FD', 179, 'by showing that no mechanism class among seven produces off-line zeros', 'FD states that the SIDE Exclusion Principle '
     'settles RH by showing that no mechanism class among seven produces off-line zeros, Conservation of Spectra sealing the interfaces.',
     'statement-grade', 'statement', 'stated at :179; the argument it names is the mechanism enumeration the sieve reads at RH-60', R1),
    ('FD-14', 'FD', 183, 'by 18.6σ to 351σ', 'FD states that the cosmos selects the arithmetic class at 0.13σ, excluding the other three by 18.6σ '
     'to 351σ.', 'statement-grade', 'statement', 'figures of MATTER_AS_ARITHMETIC, cited, not computed here', None),
    ('FD-15', 'FD', 187, 'and the zeros are confined to the critical line', 'FD restates that at ζ’s scale the interfaces carry no spectral content '
     'and the zeros are confined to the critical line.', 'statement-grade', 'statement', 'a restatement of :179', R1),
    # ---------------------------------------------------------------- THEORY_SPACE (p2-d7)
    ('TH-01', 'TH', 18, 'α_T = 0.918 ± 0.018 (CV = 2.0%)', 'TH reports a mean alignment α_T = 0.918 ± 0.018 for the I∩D∩S theories, CV 2.0 '
     'percent.', 'computationally-verified', 'computation', 'reported; the per-domain table (:108-:118) gives a count-weighted mean 0.922 '
     '(the claim bank)', None),
    ('TH-02', 'TH', 20, 'across all 15 domains', 'TH states that α_T is the same across all fifteen domains.', 'statement-grade', 'statement',
     'against :120, where four of the fifteen domains have no I∩D∩S theory', None),
    ('TH-03', 'TH', 20, 'Fourteen I∩D∩S theories are identified.', 'TH identifies fourteen theories satisfying I, D and S.',
     'computationally-verified', 'computation', 'the per-domain counts (:108-:118) sum to 14 (the claim bank)', None),
    ('TH-04', 'TH', 65, '| **Total** | **375** | |', 'TH totals its sample at 375 theories over fifteen domains.', 'computationally-verified',
     'computation', 'the domain counts at :50-:64 sum to 348 (the claim bank)', None),
    ('TH-05', 'TH', 79, 'Inter-rater agreement: κ = 0.87', 'TH reports two raters with Cohen’s κ = 0.87.', 'computationally-verified',
     'computation', 'reported; the data are available on request (:306) and not supplied', None),
    ('TH-06', 'TH', 128, 'χ² = 2.1, df = 10, p = 0.995', 'TH reports χ² = 2.1 on 10 degrees of freedom, p = 0.995, against a uniform law on '
     '[0.85, 0.95].', 'computationally-verified', 'computation', 'the survival probability recomputed in the claim bank', None),
    ('TH-07', 'TH', 130, '**Bootstrap 95% CI** (10,000 resamples): [0.906, 0.930].', 'TH reports a bootstrap 95 percent interval [0.906, 0.930].',
     'computationally-verified', 'computation', 'reported; a normal interval from its own mean and deviation is computed in the claim bank',
     None),
    ('TH-08', 'TH', 176, 'compiles the ARCHITECTURE of the proof', 'TH states that the Lean kernel for RH compiles the architecture of the argument, '
     'what classes exhaust ξ’s mechanisms, leaving the instantiation to Lean’s riemannZeta.', 'statement-grade', 'statement', 'stated at :176; '
     'the architecture it names is the mechanism enumeration the sieve reads at RH-60', R1),
    ('TH-09', 'TH', 208, 'Retrocheck: 3/3.', 'TH’s retrocheck finds phlogiston, the ether and steady-state cosmology each failing the I condition.',
     'argument-supported', 'argument', 'argued at :198-:202', None),
    ('TH-10', 'TH', 216, 'The difference is 0.0013 — within the standard deviation of 0.018.', 'TH notes α_T within 0.0013 of 11/12.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('TH-11', 'TH', 218, '12 is the number of Standard Model fermions per generation.', 'TH reads 11/12 as M-theory’s eleven dimensions over the '
     'twelve Standard Model fermions per generation.', 'statement-grade', 'statement', 'a generation carries two quark flavours in three colours '
     'and two leptons; twelve is the flavour count over three generations', None),
    ('TH-12', 'TH', 232, 'cannot distinguish 0.918 from 0.917', 'TH states that fourteen points cannot distinguish 0.918 from 0.917 and asks for at '
     'least thirty.', 'argument-supported', 'argument', 'argued at :232 from the sample size', None),
    ('TH-13', 'TH', 254, '| General relativity | 1915 | 1915 | ~1960 | ~1960 | 45 years M1→M5 |', 'TH tabulates the paths M1 to M5 as 45 years '
     'for general relativity, 68 for plate tectonics and 15 for BCS.', 'computationally-verified', 'computation', 'recomputed in the claim bank',
     None),
    ('TH-14', 'TH', 300, 'The findings are empirical and independently reproducible.', 'TH states that its findings are empirical and '
     'independently reproducible.', 'statement-grade', 'statement', 'against :306, where the table of 375 theories is available on request',
     None),
    # ---------------------------------------------------------------- qec_kappa_infrastructure.py (p2-d8), no bank holds a run
    ('QI-01', 'QI', 7, '3. Non-Clifford gates: T-gate, Toffoli', 'QI’s docstring lists a T gate and a Toffoli among its non-Clifford gates.',
     'statement-grade', 'statement', 'the module defines a T gate (:156-:160) and no Toffoli', None),
    ('QI-02', 'QI', 59, 'assert len(HAMMING_CODEWORDS) == 16', 'QI asserts that the [7, 4, 3] Hamming code has sixteen codewords.',
     'statement-grade', 'statement', 'a check the module runs on import; no bank holds a run; the claim bank recounts sixteen', None),
    ('QI-03', 'QI', 61, '# Even-weight codewords form |0_L> support', 'QI takes the eight even-weight codewords as the support of |0_L⟩ and the odd '
     'as that of |1_L⟩.', 'statement-grade', 'statement', 'no bank holds a run; the claim bank finds the even-weight words of weights 0 and 4',
     None),
    ('QI-04', 'QI', 167, 'Logical Z is the parity of all 7 qubits', 'QI measures logical Z as the parity of all seven qubits.', 'statement-grade',
     'statement', 'no bank holds a run; Z on all seven qubits is a logical Z of the Steane code (the claim bank)', None),
    ('QI-05', 'QI', 187, 'Compute kappa(logical, syndrome) = 1 - (mean within-class variance / total variance).', 'QI defines κ at the syndrome '
     'interface as one minus the mean within-class variance of the logical outcome over its total variance.', 'statement-grade', 'statement',
     'a definition the module computes; no bank holds a run', None),
    ('QI-06', 'QI', 280, '# T-gates anti-commute with X-stabilizers', 'QI states that T gates anticommute with the X-type stabilizers, so the X '
     'syndrome should detect non-Clifford content.', 'statement-grade', 'statement', 'no bank holds a run; T X T† = (X + Y)/√2, so T neither '
     'commutes nor anticommutes with X (the claim bank)', None),
    ('QI-07', 'QI', 358, 'For Steane [[7,1,3]] this should be ~0', 'QI expects κ near 0 at T-count 0, perfect protection by design.',
     'statement-grade', 'statement', 'no bank holds a run; the companion paper’s table reports 0.0000 (phase2/quantum/QEC_KAPPA_MAGIC_FINDINGS_v0_1.md '
     ':19), a report and not a bank', None),
    ('QI-08', 'QI', 366, 'Expected pattern if conjecture holds: monotonically rising kappa', 'QI expects κ to rise monotonically with T-count '
     'toward saturation if the conjecture holds.', 'statement-grade', 'statement', 'no bank holds a run; the companion paper reports κ not '
     'monotonic (:38)', None),
    # ---------------------------------------------------------------- qec_kappa_v2.py (p2-d9), no bank holds a run
    ('QV-01', 'QV', 17, 'For n_T = 7 this is transversal T = logical T.', 'QV states that T on all seven qubits is the transversal T and a logical '
     'T of the Steane code.', 'statement-grade', 'statement', 'no bank holds a run; T on all seven qubits multiplies the weight-4 words of |0_L⟩ '
     'by −1 and so leaves the code space (the claim bank)', None),
    ('QV-02', 'QV', 66, 'k, syn = kappa_full(prep, n_states=40, n_meas=8)', 'QV runs forty states by eight measurements at each T-count from 0 '
     'to 7.', 'statement-grade', 'statement', 'the sizes match the companion paper’s table (:15); no bank holds the run', None),
    ('QV-03', 'QV', 78, 'Transversal T is a logical operation - it should PRESERVE the code', 'QV states that transversal T preserves the code '
     'space, so κ at n_T = 7 should return to about 0.', 'statement-grade', 'statement', 'as QV :17; the companion paper reports 0.0153 at '
     'n_T = 7 (:26)', None),
    ('QV-04', 'QV', 81, 'Confirmed: kappa at n_T=7 = ', 'QV prints “Confirmed” beside whatever value its run gives at n_T = 7.', 'statement-grade',
     'statement', 'the word is printed unconditionally; no bank holds a run', None),
]

ROUTE_ROWS = {'RH-58': 'NOT A ROUTE', 'RH-59': 'DARK, test 1', 'RH-60': 'DARK, test 2', 'MC-01': 'NOT A ROUTE'}
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'
LSR = {}   # ### OPEN_TRAILS :12703: the ls-remote calls this process made, per repository
SIM_SEARCH = (('PLACE-papers tracked and untracked', 'git grep / ls-files'), ('relay tracked', 'git grep'),
              ('D:/MY-DOwnloads, D:/HERITAGE, D:/PLACE-phase2, D:/PLACE-phase1.5 by file name', 'os.walk'))
SIM_NEEDLES = ('kappa vs T-count', 'kappa(logical | full syndrome)', 'STEANE [[7,1,3]] kappa')


def g(repo, *a):
    if 'ls-remote' in a:
        LSR[repo] = LSR.get(repo, 0) + 1
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def show_bytes(path, rev, repo):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def paper_lines():
    return {k: lines_of(show(v[0])) for k, v in PAPERS.items()}


def techne_pointer():
    """### the pointer to TECHNE-Core: the sha256 of its tracked-file manifest at HEAD (`git ls-tree -r HEAD`), no body read or printed"""
    r = subprocess.run(['git', '-C', TE, 'ls-tree', '-r', 'HEAD'], capture_output=True)
    return hashlib.sha256(r.stdout.replace(b'\r\n', b'\n')).hexdigest() if r.returncode == 0 else None


def claims():
    """### the claims with the TECHNE row's pointer filled"""
    p = techne_pointer()
    out = []
    for c in C:
        if c[7] == 'TECHNE-POINTER':
            c = c[:7] + ('the TECHNE citation, carried by pointer alone: TECHNE-Core, its tracked-file manifest sha256 %s; no sentence of its body '
                         'carried and no tool of it named' % p,) + c[8:]
        out.append(c)
    return out


def resolve_claims():
    """### every claim's needle on its cited line at the pin: [(id, ok, the line)]"""
    P = paper_lines()
    out = []
    for c in C:
        cid, pk, n, needle = c[0], c[1], c[2], c[3]
        l = P[pk][n - 1] if 0 < n <= len(P[pk]) else ''
        out.append((cid, needle in l, l))
    return out


_REMOTE = {}   # ### OPEN_TRAILS :12703: each repository's remote refs, read once per run and reused by every later read


def remote_refs(path):
    """### one `git ls-remote origin` per repository per run, its refs reused across arms; a failed read is retried once alone, and a
    ### read that fails twice is kept as failed for the run: {ref: sha}"""
    if path not in _REMOTE:
        out = g(path, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            out = g(path, 'ls-remote', 'origin')
        _REMOTE[path] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[path]


def pin_state(key):
    """### a pin resolves when its commit is in the clone, peels to the expected commit, and is at the remote:
    ### (key, repo, pin, local commit, how the remote holds it or None) -- the remote read once per run (remote_refs)"""
    repo, pin, want, _where = PINS[key] if key in PINS else PINS_NT[key]
    path = 'D:/' + repo
    loc = g(path, 'rev-parse', '--verify', '-q', pin + '^{commit}').strip()
    if not loc.startswith(want):
        return (key, repo, pin, loc[:12], None)
    refs = remote_refs(path)
    tags = [(r[len('refs/tags/'):], h) for r, h in sorted(refs.items()) if r.startswith('refs/tags/')]
    peeled = [r[:-3] for r, h in tags if r.endswith('^{}') and h.startswith(loc)]
    light = [r for r, h in tags if not r.endswith('^{}') and h.startswith(loc)]
    rem = ('remote tag %s' % peeled[0]) if peeled else ('remote tag %s' % light[0]) if light else None
    if rem is None:
        head = refs.get('refs/heads/main', '')
        if head and subprocess.run(['git', '-C', path, 'merge-base', '--is-ancestor', loc, head], capture_output=True).returncode == 0:
            rem = 'on the remote main %s' % head[:7]
    return (key, repo, pin, loc[:12], rem)


def _read(table, k):
    pk, f, n, needle, _what = table[k]
    repo, pin, _w, _where = PINS[pk] if pk in PINS else PINS_NT[pk]
    ls = lines_of(show(f, pin, 'D:/' + repo))
    l = ls[n - 1] if 0 < n <= len(ls) else ''
    return (k, needle in l, l)


def resolve_nt():
    """### the pins named without a terminal, read for the record: [(key, ok, line)]"""
    return [_read(NTREADS, k) for k in NTREADS]


def t7_bank():
    """### the registered run's bank: the committed results file, its fields, its working copy's md5 against the paper's, and whether its
    ### commit is on the remote main"""
    repo, rev, f, md5_paper = T7BANK
    path = 'D:/' + repo
    b = show_bytes(f, rev, path)
    if b is None:
        return dict(ok=False)
    J = json.loads(b.decode('utf-8'))
    wc = os.path.join(path, f)
    md5_wc = hashlib.md5(open(wc, 'rb').read()).hexdigest() if os.path.exists(wc) else None
    head = remote_refs(path).get('refs/heads/main', '')
    on_remote = bool(head) and subprocess.run(['git', '-C', path, 'merge-base', '--is-ancestor', rev, head], capture_output=True).returncode == 0
    best = J.get('best') or {}
    return dict(ok=True, rev=g(path, 'rev-parse', '--short=7', rev).strip(), p=best.get('p_global_look_elsewhere'), theta=best.get('theta_min_deg'),
                signal=best.get('signal'), seed=(J.get('frozen') or {}).get('seed'), n_mc=(J.get('frozen') or {}).get('n_mc'),
                scan=len(J.get('theta_min_deg') or []), decision=J.get('decision_global'), md5_blob=hashlib.md5(b).hexdigest(), md5_wc=md5_wc,
                md5_paper=md5_paper, wc_matches=md5_wc == md5_paper, on_remote=on_remote, remote_main=head[:7])


def commit_subject(key):
    repo, pin, _w, _where = PINS_NT[key]
    return g('D:/' + repo, 'log', '-1', '--format=%s', pin).strip()


def sieve_rows():
    out = {}
    for l in lines_of(show(SIEVE)):
        m = re.match(r'^\| ((?:RH|FD|CT|MC)-\d\d) \| ', l)
        if m and m.group(1) in ROUTE_ROWS and m.group(1) not in out:
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = (c[4], c[5])
    return out


def grade_ok(c):
    if c[5] not in GRADES or c[6] not in NEEDS[c[5]]:
        return False
    if c[1] in SIMULATORS and c[5] == 'computationally-verified':   # ### (R226)(3): only where a bank holds the run
        return bool(sim_banks())
    if c[5] == 'kernel-verified':   # ### no pin with a terminal: no row can certify
        return False
    return True


def sim_banks():
    """### the bank search for a run of either simulator: tracked and untracked text in PLACE-papers and relay carrying the runs' printed
    ### headers, and any file named for the simulators outside their own two paths that is not a copy of a script: [paths]"""
    hits = []
    for repo in (PP, ROOT):
        for n in SIM_NEEDLES:
            r = subprocess.run(['git', '-C', repo, 'grep', '-l', '-F', '--untracked', n], capture_output=True)
            for p in r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL):
                if p.strip() and not p.endswith('.py') and not os.path.basename(p).startswith('b616_'):
                    hits.append('%s:%s' % (os.path.basename(repo), p.strip()))
    return sorted(set(hits))


# ================================================================================ THE LOAD-BEARING READING
# ### OPEN_TRAILS :12699: no row reads kernel-verified, so no row is load-bearing and the tier reads C
LOAD = {}


# ================================================================================ THE CLAIM BANK'S ARITHMETIC
def _is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


SF_BINS = [(0, 42, 42), (1, 90, 90), (2, 38, 37), (3, 30, 27), (4, 25, 21), (5, 28, 27), (6, 6, 6), (7, 14, 12), (8, 6, 3)]
LC_KAPPA = [0.98, 0.95, 0.85, 0.80, 0.75, 0.70, 0.60, 0.00]
LC_SCORES = {'ΛCDM': [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2], 'CCC+TL': [1, 0, 2, 0, 1, 1, 0, 1, 1, 2, 1, 0],
             'MOND': [0, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 1], 'Programme': [2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1]}
TC_POWER = [(2, 201, 1150), (3, 783, 944), (4, 574, 686), (5, 1704, 1504)]
TH_DOMAINS = [28, 22, 25, 31, 24, 20, 29, 27, 18, 15, 23, 28, 21, 19, 18]
TH_IDS = [(1, 0.952), (1, 0.948), (2, 0.941), (1, 0.937), (2, 0.929), (1, 0.921), (2, 0.912), (1, 0.908), (1, 0.901), (1, 0.895), (1, 0.888)]


def _rank(xs):
    s = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and xs[s[j + 1]] == xs[s[i]]:
            j += 1
        for k in range(i, j + 1):
            r[s[k]] = (i + j) / 2.0 + 1
        i = j + 1
    return r


def _pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy), sxy / sxx, my - sxy / sxx * mx


def _gl32():
    """### GL(3, F_2) by enumeration: its order, its action on the seven non-zero vectors, the stabilizer of (1, 1, 1) and its orbits"""
    import itertools
    vecs = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
    mats = []
    for rows in itertools.product(vecs, repeat=3):
        det = (rows[0][0] * (rows[1][1] * rows[2][2] + rows[1][2] * rows[2][1]) + rows[0][1] * (rows[1][0] * rows[2][2] + rows[1][2] * rows[2][0])
               + rows[0][2] * (rows[1][0] * rows[2][1] + rows[1][1] * rows[2][0])) % 2
        if det:
            mats.append(rows)

    def act(M, v):
        return tuple(sum(M[i][j] * v[j] for j in range(3)) % 2 for i in range(3))
    orbit = set(act(M, (1, 0, 0)) for M in mats)
    stab = [M for M in mats if act(M, (1, 1, 1)) == (1, 1, 1)]
    rest = [v for v in vecs if v != (1, 1, 1)]
    seen, orbs = set(), []
    for v in rest:
        if v in seen:
            continue
        o = set(act(M, v) for M in stab)
        seen |= o
        orbs.append(len(o))
    perms = [M for M in stab if all(sum(r) == 1 for r in M) and all(sum(M[i][j] for i in range(3)) == 1 for j in range(3))]
    return len(mats), len(orbit), len(stab), sorted(orbs, reverse=True), len(perms)


def arith2g():
    """### the cluster's arithmetic recomputed: [(label, value, the paper's figure, agrees)]"""
    import numpy as np
    A = []
    n_c, n_p = sum(b[1] for b in SF_BINS), sum(b[2] for b in SF_BINS)
    A.append(('SF :64-:74 the bins table’s constants and P-smooth counts summed', '%d constants, %d P-smooth, %d not P-smooth' % (n_c, n_p, n_c - n_p),
              '439 constants, 5 violations (:62, :82)', n_c == 439 and n_c - n_p == 5))
    d = [b[0] for b in SF_BINS]
    rate = [b[2] / b[1] for b in SF_BINS]
    r, slope, icpt = _pearson(d, rate)
    rs = _pearson(_rank(d), _rank(rate))[0]
    A.append(('SF :76 the P-smooth rate against distance over the nine bins: the least-squares line and Pearson r',
              'rate = %.3f − %.4f × distance ; r = %.3f' % (icpt, -slope, r), 'κ = 1.047 − 0.039 × distance, r = −0.66',
              round(icpt, 3) == 1.047 and round(slope, 3) == -0.039 and round(r, 2) == -0.66))
    A.append(('DM :37 the same nine bins: Spearman ρ', 'ρ = %.3f' % rs, 'Spearman ρ = −0.66', round(rs, 2) == -0.66))
    pu = (1 - 5 / 439) ** 350
    pp = math.exp(-350 * 5 / 439)
    ph = math.comb(89, 5) / math.comb(439, 5)
    A.append(('SF :91 zero of five violations among 350 of 439 constants: a Poisson count at mean 350 × 5/439, a per-constant rate 5/439, and '
              'five drawn from 439', 'exp(−%.3f) = %.4f ; (1 − 5/439)^350 = %.4f ; C(89, 5)/C(439, 5) = %.2e' % (350 * 5 / 439, pp, pu, ph),
              'a 1.9% event', round(pp * 100, 1) == 1.9))
    A.append(('SF :127 and :141 the H₀ values’ difference and its combined error', '73.04 − 67.36 = %.2f km/s/Mpc ± %.2f (%.1fσ)' % (
        73.04 - 67.36, math.hypot(1.04, 0.54), (73.04 - 67.36) / math.hypot(1.04, 0.54)), 'a separation of 6–8 km/s/Mpc predicted', 6 <= 73.04 - 67.36 <= 8))
    A.append(('LC :55 the mean κ over eight channels and over seven', '%.3f ; %.3f' % (sum(LC_KAPPA) / 8, sum(LC_KAPPA[:7]) / 7), '0.70 ; 0.80',
              round(sum(LC_KAPPA) / 8, 2) == 0.70 and round(sum(LC_KAPPA[:7]) / 7, 2) == 0.80))
    A.append(('LC :67-:80 the four columns summed and their zero scores counted', ' ; '.join('%s %d, zeros %d' % (k, sum(v), v.count(0)) for k, v in LC_SCORES.items()),
              '21, 10, 14, 20 ; failures 0, 4, 2, 0', [sum(v) for v in LC_SCORES.values()] == [21, 10, 14, 20]
              and [v.count(0) for v in LC_SCORES.values()] == [0, 4, 2, 0]))
    A.append(('LC :90 the α-variation tension', '10⁻⁵ / 10⁻⁷ = %d' % round(1e-5 / 1e-7), '100-fold', round(1e-5 / 1e-7) == 100))
    rt = ', '.join('l = %d: %.3f' % (l, o / p) for l, o, p in TC_POWER)
    so, sp = sum(o for _l, o, _p in TC_POWER), sum(p for _l, _o, p in TC_POWER)
    A.append(('TC :22-:25 the observed over predicted D_l', rt, '0.17, 0.83, 0.84, 1.13',
              [round(o / p, 2) for _l, o, p in TC_POWER] == [0.17, 0.83, 0.84, 1.13] or [round(o / p, 2) for _l, o, p in TC_POWER] == [0.17, 0.83, 0.84, 1.13]))
    A.append(('TC :27 the combined deficit at l = 2 to 5', '1 − %d/%d = %.1f%%' % (so, sp, 100 * (1 - so / sp)), '24%', round(100 * (1 - so / sp)) == 24))
    lines = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]
    N = np.zeros((7, 7))
    for j, ln in enumerate(lines):
        for i in ln:
            N[i, j] = 1
    ev = [round(float(x), 4) for x in sorted(np.abs(np.linalg.eigvals(N)))]
    nnt = [round(float(x), 4) for x in sorted(np.linalg.eigvalsh(N @ N.T))]
    k7 = [round(float(x), 4) for x in sorted(np.linalg.eigvalsh(np.ones((7, 7)) - np.eye(7)))]
    A.append(('TC :60 the Fano incidences, seven lines of three points', '%d' % int(N.sum()), '21', int(N.sum()) == 21))
    A.append(('TC :106 and :199 the Fano incidence matrix N (lines {0, 1, 3} + k mod 7): the moduli of its eigenvalues; the eigenvalues of N Nᵀ; '
              'those of the collinearity graph K₇', '|λ(N)| %s ; λ(N Nᵀ) %s ; λ(K₇) %s' % (ev, nnt, k7), '3 once and −1 six times', False))
    order, orb, stab, orbs, perms = _gl32()
    A.append(('TC :70, :190 and QD :12, :125 GL(3, 𝔽₂) enumerated: its order, the orbit of a non-zero vector, the stabilizer of (1, 1, 1), the '
              'stabilizer’s orbits on the other six, the coordinate permutations inside it', 'order %d ; orbit %d ; stabilizer %d ; its orbits %s ; '
              'permutation matrices %d' % (order, orb, stab, orbs, perms), 'order 168, transitive (TC); stabilizer S₃ with orbits 3, 3 (QD :125)',
              False))
    A.append(('TC :144 the evaluation count', '10⁶ × 100 × 1000 = %.0e' % (1e6 * 100 * 1000), '10¹¹', 1e6 * 100 * 1000 == 1e11))
    tb = t7_bank()
    A.append(('TC :172-:178 the registered run’s bank, SIDE-t7-topology-cmb %s:%s' % (T7BANK[1], T7BANK[2]),
              'p_global %s ; best θ_min %s ; signal %s ; seed %s ; n_mc %s ; scan %s points ; decision %s ; working-copy md5 %s (the paper’s %s…) ; '
              'the committed blob’s md5 %s (core.autocrlf) ; on the remote main %s' % (
                  tb.get('p'), tb.get('theta'), tb.get('signal'), tb.get('seed'), tb.get('n_mc'), tb.get('scan'), tb.get('decision'), tb.get('md5_wc'),
                  T7BANK[3][:8], tb.get('md5_blob'), tb.get('on_remote')), 'p = 0.046, θ_min 54.0°, seed 770411, md5 a340fabf…',
              tb.get('ok') and round(tb.get('p') or 0, 3) == 0.046 and tb.get('theta') == 54.0 and tb.get('wc_matches') and tb.get('on_remote')))
    om_b, om_dm, om_de = 0.04930, 0.2653, 0.6854
    tot = (om_dm + om_de) / om_b
    A.append(('QD :12, :30-:33 and DM :83-:100 the Planck ratios and their distances from the fractions', 'total %.3f ; DM/b %.3f ; DE/b %.3f ; 77/4 off by %.3f%% ; '
              '58/3 off by %.3f%% ; 16/3 off by %.2f%% ; 14 off by %.2f%%' % (tot, om_dm / om_b, om_de / om_b, 100 * abs(tot - 77 / 4) / tot, 100 * abs(tot - 58 / 3) / tot,
                                                                  100 * abs(om_dm / om_b - 16 / 3) / (om_dm / om_b), 100 * abs(om_de / om_b - 14) / (om_de / om_b)),
              '19.284 ; 5.381 ; 13.903 ; 0.17% ; 0.26% ; 0.89% ; 0.70%', round(tot, 3) == 19.284 and round(om_dm / om_b, 3) == 5.381))
    A.append(('QD :69 the per-element factor', '%.4f / 7 → %.4f ; off 11/4 by %.2f%%' % (tot, tot / 7, 100 * abs(tot / 7 - 2.75) / (tot / 7)), '2.755, 0.18%',
              round(tot / 7, 3) == 2.755))
    A.append(('QD :35, :83, :145 and FD :97-:108 the decomposition arithmetic', '3 × 16/9 = %s ; 3 × 14/3 = %s ; 58/3 − 77/4 = %s ; Ω_b/12 at Ω_b = 4/81: %s = %.5f' % (
        Fr(16, 9) * 3, Fr(14, 3) * 3, Fr(58, 3) - Fr(77, 4), Fr(4, 81) / 12, float(Fr(4, 81) / 12)), '16/3 ; 14 ; 1/12 ; 1/243 ≈ 0.0041',
              Fr(58, 3) - Fr(77, 4) == Fr(1, 12) and Fr(4, 81) / 12 == Fr(1, 243)))
    hd = {v: sum(1 for a, b in zip(v, (1, 1, 1)) if a != b) for v in [(1, 0, 0), (1, 1, 0)]}
    A.append(('QD :135-:137 the Hamming distances to (1, 1, 1)', 'weight 1: %d ; weight 2: %d' % (hd[(1, 0, 0)], hd[(1, 1, 0)]), '2 ; 1',
              hd[(1, 0, 0)] == 2 and hd[(1, 1, 0)] == 1))
    A.append(('DM :91 and FD :16 the tuple (2, 3, 2, 0)', 'n₂^(n₁+n₃) = 3^(2+2) = %d ; n₁^n₃ = 2^2 = %d ; %d − %d = %d = 7 × 11' % (3 ** 4, 2 ** 2, 81, 4, 77),
              '81 ; 4 ; 77', 3 ** 4 == 81 and 81 - 4 == 77 == 7 * 11))
    zb = (4 / 81 - 0.04930) / 0.00066
    s_dm = (om_dm / om_b) * math.hypot(0.0039 / om_dm, 0.00066 / om_b)
    s_de = (om_de / om_b) * math.hypot(0.0073 / om_de, 0.00066 / om_b)
    s_t = tot * math.hypot(math.hypot(0.0039, 0.0073) / (om_dm + om_de), 0.00066 / om_b)
    A.append(('FD :20-:22 and :143-:146 the pulls from Planck 2018', 'Ω_b = 4/81 = %.6f, %.3fσ ; 16/3 %.2fσ ; 14 %.2fσ ; 77/4 %.2fσ (Planck alone)' % (
        4 / 81, zb, (om_dm / om_b - 16 / 3) / s_dm, (14 - om_de / om_b) / s_de, (tot - 77 / 4) / s_t), '0.13σ ; 0.45σ ; 0.41σ ; 0.03σ (five datasets)',
              round(zb, 2) == 0.13 and round((om_dm / om_b - 16 / 3) / s_dm, 2) == 0.45))
    A.append(('FD :112 Decomposition B’s curvature against Planck’s Ω_K = −0.0007 ± 0.0019', 'Ω_K = −1/243 = %.4f, %.2fσ' % (-1 / 243, (-1 / 243 + 0.0007) / 0.0019),
              'consistent with both', abs((-1 / 243 + 0.0007) / 0.0019) < 2))
    nT = sum(TH_DOMAINS)
    ni = sum(c for c, _v in TH_IDS)
    wm = sum(c * v for c, v in TH_IDS) / ni
    um = sum(v for _c, v in TH_IDS) / len(TH_IDS)
    vals = [v for c, v in TH_IDS for _k in range(c)]
    sd = math.sqrt(sum((x - wm) ** 2 for x in vals) / (len(vals) - 1))
    A.append(('TH :50-:65 and :108-:118 the domain counts, the I∩D∩S counts, the means and the deviation', '%d theories ; %d I∩D∩S ; count-weighted mean %.4f, '
              'unweighted %.4f ; deviation %.4f' % (nT, ni, wm, um, sd), '375 ; 14 ; 0.918 ± 0.018', nT == 375 and ni == 14 and round(wm, 3) == 0.918))
    import mpmath
    chi = float(mpmath.gammainc(5, 1.05, mpmath.inf, regularized=True))
    A.append(('TH :128 the χ² survival at 2.1 on 10 degrees of freedom', 'p = %.4f' % chi, '0.995', abs(chi - 0.995) < 0.001))
    h = 1.96 * 0.018 / math.sqrt(14)
    A.append(('TH :130 a normal 95 percent interval from 0.918 ± 0.018 over fourteen', '[%.3f, %.3f]' % (0.918 - h, 0.918 + h), '[0.906, 0.930]',
              round(0.918 - h, 3) == 0.906))
    A.append(('TH :216 the distance from 11/12', '0.918 − 11/12 = %.5f' % (0.918 - 11 / 12), '0.0013', round(0.918 - 11 / 12, 4) == 0.0013))
    A.append(('TH :254-:256 the paths M1 to M5', '%d ; %d ; %d' % (1960 - 1915, 1980 - 1912, 1972 - 1957), '45 ; 68 ; 15',
              (1960 - 1915, 1980 - 1912, 1972 - 1957) == (45, 68, 15)))
    H = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    import itertools
    cw = [b for b in itertools.product((0, 1), repeat=7) if not ((H @ np.array(b)) % 2).any()]
    ev_w = sorted(set(sum(b) for b in cw if sum(b) % 2 == 0))
    A.append(('QI :43-:64 the [7, 4, 3] codewords and the weights of the even ones', '%d codewords ; even %d of weights %s ; odd %d' % (
        len(cw), sum(1 for b in cw if sum(b) % 2 == 0), ev_w, sum(1 for b in cw if sum(b) % 2 == 1)), '16 ; 8 ; 8', len(cw) == 16))
    T = np.diag([1, np.exp(1j * np.pi / 4)])
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    TXT = T @ X @ T.conj().T
    A.append(('QI :280 T X T† against ±X and (X + Y)/√2', 'T X T† = (X + Y)/√2: %s ; commutes: %s ; anticommutes: %s' % (
        np.allclose(TXT, (X + Y) / np.sqrt(2)), np.allclose(T @ X, X @ T), np.allclose(T @ X, -X @ T)), 'anti-commute', False))
    idx = lambda b: int(''.join(map(str, b)), 2)   # noqa: E731
    z = np.zeros(128, complex)
    o = np.zeros(128, complex)
    for b in cw:
        (z if sum(b) % 2 == 0 else o)[idx(b)] = 1 / np.sqrt(8)
    t7 = np.array([np.exp(1j * np.pi / 4 * bin(i).count('1')) for i in range(128)])
    tz = t7 * z
    ov0, ov1 = np.vdot(z, tz), np.vdot(o, tz)
    A.append(('QV :17 and :78 T on all seven qubits applied to |0_L⟩: its overlaps with |0_L⟩ and |1_L⟩ and the norm left in the code space',
              '⟨0_L|T⊗7|0_L⟩ = %.3f%+.3fi ; ⟨1_L|T⊗7|0_L⟩ = %.3f ; norm in the code space %.3f' % (ov0.real, ov0.imag, abs(ov1), math.hypot(abs(ov0), abs(ov1))),
              'a logical operation preserving the code space', abs(math.hypot(abs(ov0), abs(ov1)) - 1) < 1e-9))
    return A


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:90]) for i, _o, l in bad] or 'NONE'))
    for k in list(PINS) + list(PINS_NT):
        print('### pin %s' % (pin_state(k),))
    nb = [x for x in resolve_nt() if not x[1]]
    print('### reads at the pins without a terminal %d ; failing %s ; subjects %s' % (len(NTREADS), [(k, l[:90]) for k, _o, l in nb] or 'NONE',
                                                                                      [commit_subject(k) for k in PINS_NT]))
    print('### the T7 bank: %s' % t7_bank())
    print('### the simulators` bank search: %s' % (sim_banks() or 'NONE'))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    print('### simulator grades: %s' % dict(Counter(c[5] for c in C if c[1] in SIMULATORS)))
    print('### ids unique: %s' % (len(set(c[0] for c in C)) == len(C)))
    print('### TECHNE pointer: %s' % techne_pointer())
    print('### ls-remote calls this run, per repository: %s' % LSR)
    if '--arith' in sys.argv:
        for a in arith2g():
            print('### %s -- %s ; the paper: %s ; agrees %s' % (a[0], a[1][:400], a[2], a[3]))


if __name__ == '__main__':
    main()
