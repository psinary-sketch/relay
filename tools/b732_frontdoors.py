# -*- coding: utf-8 -*-
"""b732 -- (R342)(5)-(6)(i): THE DRAFTS FOR THE SECOND SITTING, data/b726_frontdoors.txt`s form, ASSEMBLED AND NOT APPLIED.

Every statement quoted is read at the census pin by b732_doors.decls, verbatim, and a statement absent there refuses the run. The classes and the rows are data/b732_door_classes.json's and
data/b732_door_grades.json's; the kernels with a draft are computed from them and compared to the table below, so a kernel dropped or added by hand refuses. The relay is public and SIDE-constants
is private (data/repo_visibility.txt :17): its rows go by digest and it carries no draft text here. No README, description, Zenodo record, paper or kernel main is written by this tool.

  python -X utf8 -u tools/b732_frontdoors.py controls | bank
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b732_doors as B

D = B.D
OUT = os.path.join(D, 'b732_phase2_frontdoors.txt')
CLASSES = os.path.join(D, 'b732_door_classes.json')
NL = chr(10)
GH_MAX = 350
PRIVATE = B.PRIVATE

# ### kernel: (the words before the statements, the statements as (file ending, name), the words after, the one-line description). The after-words read data/b732_phase2_doors.txt's rows.
DRAFT = {
 'SIDE-bijection': ("SIDE-bijection compiles a structure, IDSSystem, and the statement that its identity map is bijective at each of four stages.",
   [('SIDEBijection/Theorem.lean', 'identity_formation_bijection')],
   "The proof pairs the structure's own fields distinctness and noOrphans, so the statement restates what an IDSSystem is assumed to carry: the paper's Lemmas 3.1 and 4.1 enter as those fields, and no corpus-level object is compiled.",
   "Lean 4 kernel: the structure IDSSystem and the statement that its identity map is bijective at four stages, from the structure's own fields"),
 'SIDE-bsd-formation-transfer': ("SIDE-bsd-formation-transfer is the placement skeleton its banner says it is: arithmetic over the literal tuple (2, 3, 2, 0) and conjunctions of Bool values set by definition.",
   [('SIDEBSDFormationTransfer/Basic.lean', 'formation_transfer_xi_to_bsd'), ('SIDEBSDFormationTransfer/Basic.lean', 'bsd_fully_closed'), ('SIDEBSDFormationTransfer/Basic.lean', 'Sha_finite')],
   "Each of these certifies a stipulation only. No statement names L(E, s), a zero, Re(s) = 1, a functional equation in s, a Hasse bound or Ш as a group; the location of zeros, Ш finiteness and the closure of the architecture are where the thesis places them, and nothing here delivers them. BSD stays open.",
   "Lean 4 placement skeleton: the tuple (2, 3, 2, 0) and stipulated Bool values marking where the formation-transfer thesis places BSD's components; none is derived"),
 'SIDE-class-coupling': ("SIDE-class-coupling compiles a faithful coupling between two concrete finite substrates.",
   [('SIDEClassCoupling/Concrete.lean', 'SmallA_to_SmallB')],
   "\"Trace 7\" and the matter-as-remainder spiral are the papers' words for it; no statement names either, and the class of this kernel is a substrate class, with no class number or anomaly in it.",
   "Lean 4 kernel: a faithful coupling between two concrete finite substrates, SmallA and SmallB"),
 'SIDE-compression': ("SIDE-compression compiles a statement on finite catalogues and a statement on a record of flags.",
   [('SIDECompression/ChainLength.lean', 'compression'), ('SIDECompression/Basic.lean', 'silence_yields_compression')],
   "The first says that an exhaustive catalogue cleared class by class clears every object, with no interface hypothesis. The second takes X.chainLength = X.formationTotal as a hypothesis, chainLength being a hand-set field, so no statement concludes that chain length equals N from the conditions. No statement names ξ(s), a zero or the Silence Principle.",
   "Lean 4 kernel: an exhaustive catalogue cleared class by class clears every object; chain length = N is a hypothesis of the record-level statement, not a conclusion"),
 'SIDE-cosmo': ("SIDE-cosmo compiles natural-number arithmetic on a four-component tuple: slot counts for the tuple xi, a wall-squared identity, a strict inequality between visible and total slots, and Fano-incidence arithmetic.",
   [('SIDECosmo/FormationPhaseSpace.lean', 'xi_total'), ('SIDECosmo/FormationPhaseSpace.lean', 'xi_visible'), ('SIDECosmo/FormationPhaseSpace.lean', 'xi_dark'), ('SIDECosmo/FormationPhaseSpace.lean', 'xi_wall_sq'), ('SIDECosmo/FormationPhaseSpace.lean', 'dark_sector_exists')],
   "These compute naturals; no ratio is formed, and no statement names a cosmological object, Ω_b, a prediction, the SIDE Exclusion Principle or GL(3,𝔽₂), whose 168 = 24 × 7 stands here as a product of naturals. At this pin the xi statements close by native_decide.",
   "Lean 4 kernel: natural-number slot counts on the tuple xi (81 total, 4 visible, 77 dark), a wall-squared identity and Fano-incidence arithmetic"),
 'SIDE-coupling': ("SIDE-coupling compiles a Coupling structure between arbitrary abstract substrates, its faithful form and a local observer, with two statements on primitive accessibility.",
   [('SIDECoupling/Coupling.lean', 'coupling_preserves_accessibility'), ('SIDECoupling/Projection.lean', 'faithful_detected_image_iff_primitive_source')],
   "Both hold over arbitrary substrates. The readings as the Class A and Class C coupling and as local alpha are the paper's targets: no statement names them.",
   "Lean 4 kernel: couplings between abstract substrates preserve primitive accessibility, with its observer-level form for faithful couplings"),
 'SIDE-cubit-axis': ("SIDE-cubit-axis compiles equalities among natural numbers defined in its own file.",
   [('SIDECubitAxis/Basic.lean', 'cubit_unification')],
   "The file imports no sibling, so nothing it states of another kernel is checked, and no statement names (ℤ/2)³.",
   "Lean 4 kernel: equalities among the file's own natural-number constants; no sibling kernel is imported"),
 'SIDE-dark-interface': ("SIDE-dark-interface compiles lookups in a table entered by hand.",
   [('SIDEDarkInterface/Basic.lean', 'nl_dark_for_validity')],
   "The entries of kappa_x100 are inputs: the kernel checks what follows from the table and measures nothing.",
   "Lean 4 kernel: statements over a hand-entered table of κ values; the entries are inputs, not measurements"),
 'SIDE-effects': ("At the census pin v0.1 = afb196e, SIDE-effects compiles abstract exclusion statements, and three theorems of Milestones.lean close by sorry.",
   [('SIDEEffects/Structural.lean', 'side_exclusion'), ('SIDEEffects/Structural.lean', 'no_type_d')],
   "The first restates its hypothesis; the second takes the modular coupling as its premise h. At this pin no statement names a ladder of licenses, CRT exhaustiveness or EDifficultyTop.",
   "Lean 4 kernel at v0.1: abstract exclusion statements, with three milestone theorems closing by sorry"),
 'SIDE-formation-arithmetic': ("SIDE-formation-arithmetic compiles natural-number arithmetic over a formation tuple.",
   [('SIDEFormationArithmetic/Classes.lean', 'classA_total'), ('SIDEFormationArithmetic/Core.lean', 'wall_squared_when_n1_eq_n3')],
   "\"Traces 2 and 3\" of the matter-as-remainder spiral are comments and the papers' words: no statement names a trace or a spiral.",
   "Lean 4 kernel: natural-number arithmetic on the formation tuple, including the wall-squared identity when n1 = n3"),
 'SIDE-interfaces': ("SIDE-interfaces compiles a ConservationProfile structure over a finite parameter type, and three statements.",
   [('Interfaces/ConnectionRequiresStructure.lean', 'connection_requires_structure'), ('Interfaces/ConnectionRequiresStructure.lean', 'parametric_mechanism_theorem'), ('Interfaces/ConservationProfile.lean', 'rank_decomposition')],
   "connection_requires_structure concludes one witness and only under its bimodality premise, and it alone concludes an existential. The profile's field kvec is tied by no statement to a measured conservation strength.",
   "Lean 4 kernel: conservation profiles over a finite parameter type; one structural witness under a bimodality premise; a rank decomposition"),
 'SIDE-kernel': ("SIDE-kernel compiles, over Mathlib, the logical structure of a two-leg approach to the Riemann Hypothesis. It holds no unconditional term of type RiemannHypothesis.",
   [('Bridge/ConservationBridge.lean', 'riemann_hypothesis'), ('Kernel/Integration.lean', 'structural_exhaustiveness_iff_rh'), ('Kernel/SpectralCannonFull.lean', 'spectral_cannon'), ('Kernel/SilenceTheorem.lean', 'silence_universal')],
   "The premise ConservationHypothesis is the Riemann Hypothesis restated (ERRATA E-2026-09-25-1), and the second statement is an equivalence, so neither proves it. spectral_cannon speaks of Mathlib's completedRiemannZeta₀; silence_universal holds over an abstract interface, and no statement uses Tate's thesis. The default target lean_lib Kernel does not reach Bridge/. The Riemann Hypothesis stays open.",
   "Lean 4 kernel of the PLACE TO STAND two-leg approach to the Riemann Hypothesis: it machine-checks the logical structure (route terminals such as ConservationBridge.riemann_hypothesis on its named premise, and the E-Difficulty SieveCeiling subsystem); the classical mathematics is carried by the companion manuscripts."),
 'SIDE-local-cosmic-interface': ("SIDE-local-cosmic-interface compiles adjacent inequalities over the file's own table.",
   [('SIDELocalCosmicInterface/Basic.lean', 'em_ge_weak'), ('SIDELocalCosmicInterface/Basic.lean', 'qm_ge_dark')],
   "The table kappa_x100 is an input. No statement names a physical κ or a local-cosmic boundary.",
   "Lean 4 kernel: ordering statements over a hand-entered table of κ values; the entries are inputs"),
 'SIDE-meta': ("SIDE-meta compiles a parametric template, the structure SIDESystem, with the statement that any such system carries its conservation.",
   [('SIDEMeta/Meta/SIDESystem.lean', 'conservation_from_SIDE')],
   "SIDESystem has no inhabitant at this pin, so neither the proof stack nor the patent stack is an instance of it here; MechanismClass has no ξ in any binder, and kappa is a Prop, not a strength.",
   "Lean 4 kernel: the parametric template SIDESystem and its conservation statement; no instance at this pin"),
 'SIDE-omega-b': ("SIDE-omega-b compiles a pair of naturals computed from a tuple the file defines.",
   [('SIDEOmegaB/Theorem.lean', 'omega_b_equals_4_over_81'), ('SIDEOmegaB/Theorem.lean', 'arithmeticSubstrate'), ('SIDEOmegaB/Theorem.lean', 'Formation.omega')],
   "The pair is ⟨4, 81⟩. Its reading as Ω_b and as the last step of a derivation chain is the paper's: no statement names Ω_b or a chain.",
   "Lean 4 kernel: the pair ⟨4, 81⟩ computed from a defined tuple; its reading as Ω_b is the paper's"),
 'SIDE-quaternionic-dark-sector': ("SIDE-quaternionic-dark-sector compiles natural-number and fraction arithmetic over literals.",
   [('SIDEQuaternionicDarkSector/Basic.lean', 'residual_eq_1_over_12'), ('SIDEQuaternionicDarkSector/Basic.lean', 'cubit_total'), ('SIDEQuaternionicDarkSector/Basic.lean', 'omega_arithmetic_eq_4_over_81')],
   "The weights are literal definitions, computed from no group. No statement names (ℤ/2)³, a Hamming weight function or a dark-to-visible ratio.",
   "Lean 4 kernel: fraction arithmetic over literal weights summing to 8, with 1/12 and 4/81 among the values"),
 'SIDE-residual-bridge': ("SIDE-residual-bridge compiles decide-closed fraction arithmetic.",
   [('SIDEResidualBridge/Bridge.lean', 'residual_eq_omegaB_div_12')],
   "Here residual is the fraction (1, 243) and omegaB is (4, 81). The readings as a weight-3 residual, as Ω_b and as a total cosmic quantity are the papers'; no statement carries a bridge from 1/12.",
   "Lean 4 kernel: decide-closed fraction arithmetic, among it (1, 243) = (4, 81) / 12"),
 'SIDE-silence-principle': ("SIDE-silence-principle compiles a chain over Bool fields and an abstract statement on interfaces.",
   [('SIDESilencePrinciple/Basic.lean', 'silence_principle'), ('SIDESilencePrinciple/Basic.lean', 'silence_universal')],
   "The chain's step implications enter as hypotheses through chain_holds, so no statement proves that essential implies universal or that universal implies constant action. The tested systems are bare constructors. Of the six consequences, A, D and F appear as aliases or arithmetic; B, C and E were removed as vacuous at this pin and are manuscript-resident.",
   "Lean 4 kernel: the κ = 0 chain over Bool fields with its steps as hypotheses, and an abstract constant-action statement"),
 'SIDE-structural-error-correction': ("SIDE-structural-error-correction compiles natural-number constants and their relations.",
   [('SIDEStructuralErrorCorrection/Basic.lean', 'd_eff_formula')],
   "d_eff is defined as 2 * S - 1, and the statement unfolds that definition. No statement names a code, an error model, a distance or Knill-Laflamme equivalence.",
   "Lean 4 kernel: natural-number constants, among them d_eff defined as 2 * S - 1 = 5; no code or error model is constructed"),
 'SIDE-substrate-cluster': ("SIDE-substrate-cluster compiles seven-constructor labelings and the agreement of their weight tables.",
   [('SIDESubstrateCluster/Cluster.lean', 'cluster_bijection_family')],
   "No statement names (ℤ/2)³ \\ {0} as a group or says any labeling realizes it.",
   "Lean 4 kernel: four labelings of a seven-constructor type whose weight tables agree"),
 'SIDE-trivium': ("SIDE-trivium compiles an equivalence between two seven-constructor enumerations.",
   [('Trivium/Bijection.lean', 'trivium_theorem')],
   "Any two seven-element types carry such an equivalence. The enumerations are named for mechanism classes and discriminants; no statement names ξ, a zero, an exclusion or a field, so that they govern off-line zero exclusion is not compiled.",
   "Lean 4 formalization of the Trivium count-bijection: seven mechanism classes and seven quadratic discriminants have equal count (trivium_theorem). Element-level pairing is convention, not canonical — basis-relative under GL(3,𝔽₂); see the §4 functorial-limit negative."),
 'SIDE-yang-mills-formation': ("SIDE-yang-mills-formation is the placement skeleton its banner says it is: literals carrying a yang_mills prefix and Bool values set by definition.",
   [('SIDEYangMillsFormation/Basic.lean', 'yang_mills_code_consistent'), ('SIDEYangMillsFormation/Basic.lean', 'mass_gap_equals_n3_certification')],
   "The first says a three-field record equals the file's own totals: no code is constructed and no statement names AG(3, 𝔽₂) or PG(2, 𝔽₂). Read as a quantum code, [[8, 1, 5]] fails the quantum Singleton bound. The second certifies a stipulation. The mass gap stays open.",
   "Lean 4 placement skeleton: literal totals and stipulated Bool values marking where the formation thesis places Yang-Mills; the mass gap stays open"),
}

# ### deposit notes: b726's words, then what the record's own exceeding rows need. Nothing about a record's later version is claimed: none was read.
DEPOSIT = [
 ('SIDE-cosmo', 'dep:19938009', "CURRENCY. This record is the citable deposit at v0.3, as deposited on 2026-05-01. The live kernel stands ahead of it and is not deposited. The kernel computes natural numbers on a four-component tuple (total_slots xi = 81, visible_slots xi = 4) and forms no ratio: Ω_b, the zero-free-parameter prediction and the distance of 0.13σ above are the paper's reading of those numbers, not compiled statements."),
 ('SIDE-effects', 'dep:19938005', "CURRENCY. This record is the citable deposit at v0.1 = afb196e. The live kernel stands ahead of it and is not deposited. At that version three theorems close by sorry and side_exclusion restates its hypothesis; the nine consequences of the title are not verified there."),
 ('SIDE-trivium', 'dep:19938003', "CURRENCY. This record is the citable deposit at v0.1. The live kernel stands ahead of it and is not deposited. Where the text above says the SIDE proof, that claim is not supported, and the Riemann Hypothesis stays open. At the census pin ec92d62 the Lean compiles an equivalence between two seven-constructor enumerations and names no Fano plane, valence pattern or Steane code; those are the paper's."),
 ('SIDE-interfaces', 'dep:19931797', "CURRENCY. This record is the citable deposit at v0.1.1. The live kernel stands ahead of it and is not deposited. Of the existence theorems the text names, connection_requires_structure alone concludes an existential, one witness, under a bimodality premise the sentence above does not carry."),
 ('SIDE-kernel', 'dep:21520474', "CURRENCY. This record is the citable deposit at SIDE-kernel v1.5 = 0e5233f. The live kernel line names SIDE-explicit-formula beside it and is not deposited. Where the text above says \"the proof\", it names the argument under the named premise, which stays open. Of the route terminals, riemann_hypothesis alone concludes the Riemann Hypothesis, on that premise; spectral_cannon speaks of Mathlib's completedRiemannZeta₀, and c7_exclusion is definition-encoded at its site. The sealing from Tate's thesis is the manuscript's, not a compiled statement."),
]

HEADS = [
 ('p2-10', '11.1', 'MOVED-IN-MEANING', "*v1.0.1 (2026-07-19, ARM 5): brought to Science-Statement Standard parity (A_METHODOLOGY §VI.3.1) -- the excluded-class σ-distances quantified in the Selection table (B 351σ, C 18.6σ, D 304σ, computed against Planck 2018), and the `xi_*` cluster cited in the status table: `xi_visible : visible_slots xi = 4`, `xi_total : total_slots xi = 81`, `xi_wall_sq : total_slots xi = (stormer_wall xi) ^ 2` (SIDE-cosmo at 95d2540, `SIDECosmo/FormationPhaseSpace.lean`, closing by `native_decide` at that pin). Those statements compute two natural numbers; the fraction 4/81 and its reading as Ω_b are this paper's.*",
  "the edition form's MOVED-IN-MEANING clause: rewritten to what the compiled fact says, citing the declarations by name and pin. {propext, Quot.sound} holds at main and not at this pin, so the print goes with the pin's own close"),
 ('p2-10', '11.2', 'REMOVED', "(removed; back matter: \"No claim changed; the derived 4/81 and its 0.13σ match stand.\" No compiled statement derives 4/81 as a physical fraction or carries a match; the comparison stands in the paper's body with its own error bar.)",
  "(R342)(5) says restated; the edition form says a marked sentence the compiled facts do not support is removed and its removal recorded in back matter, not reworded. The form's clause is the one the ruling names, so this is a removal, printed as such. The error bar differs by citation: 0.00066 in this paper, 0.00059 at SIDE-cosmo (data/b726_frontdoors.txt [20]), 0.0031 in the SIDE-cosmo record"),
]

NOTE_2C = ("The five fields of ZQPremises, the premises of the Weil chain for the Epstein zeta Z_Q of x² + xy + 6y², make a worked example of three kinds of premise. "
           "The first kind is the premise Mathlib's theory already reaches. Three fields are of it and are compiled on the branch zq-b730, each at the axioms propext, Classical.choice and Quot.sound: continuation, by Mathlib's even-kernel route, in 835 lines and 6 dispatches against an estimate of 1,500-3,000 lines and 25-50 dispatches; zeros, in the form of zetaZeroConfig over the completed function, in 340 lines and 1 dispatch against 300-600 and 5-10, one observation and no rate; and logDeriv, by the LSeries route, in 786 lines and 3 dispatches against 200-400 and 3-8, the estimate having carried no line for the bound Z_Q(3/2) < 4 on which the field rests. "
           "The second kind is the premise finite computation settles with no axiom, and none of the five fields is of it: the nearest, that bound, closes by analysis, the rows telescoped by the mean value theorem and summed against ζ(2), and it carries the same three axioms. The kind's instance is elsewhere, in the C2 certificates: cert D n0 v q = true at each of 18 fields by decide +kernel, each depending on no axiom at all. There the second kind sits under the first, for the theorem above the certificates, c2_value_law, compiles at the same 18 fields at the three axioms, with the completeness of the list of fields cited and not compiled. "
           "The third kind needs new analysis, and two fields are of it, open and not touched: count, whose lower bound at the centre of the disc has no neighbour in Lean because the neighbour's tool is the Euler product, which Z_Q has not; and explicitFormula, a contour chain whose neighbour is 12 modules and 3,742 lines. Their estimates, 800-2,000 lines and 3,000-5,000 lines, read by the three measured ratios give 222-7,860 and 835-19,650 lines; the ratios disagree, and that spread is not a confidence interval. "
           "The premises stand stated and not proved, and nothing here bears on the zeros of zeta.")
NOTE_2C_WHY = ("(R342)(6)(i), for THE_FINDINGS_AS_THEY_STAND's next edition (p2-41). Figures: data/b731_price_measured.txt :17-:19, :27-:36, :47; data/b729_count_price.txt :24, :25, :32. C2: data/b728_c2.txt :25, data/b729_c2.txt :45. Statements: zq-b730 tip 1b34964a, ZQPremises Schema/EpsteinZQ.lean :137-:142, zq_three_halves_lt Schema/ZQ/Bound.lean :319. "
               "THE ORDER'S THREE KINDS READ AGAINST THE FIVE FIELDS: the second kind is empty among them, and the paragraph says so rather than seat a field there; the C2 certificates, the order's second instance, are the kind's whole population here. "
               "FOR b733 BESIDE (R342)(9): C4 of data/b729_count_price.txt :33, Z_Q(3/2) bounded above by a rational, was compiled at b731 as zq_three_halves_lt; the price of C4 reads that row.")


def statement(k, pin, ds, fend, name):
    hit = [d for d in ds if d[0].endswith(fend) and (d[3] == name or d[3].endswith('.' + name))]
    if len(hit) != 1:
        raise SystemExit('### REFUSED: %s %s %s at %s: %d declarations' % (k, fend, name, pin, len(hit)))
    h = hit[0][4]
    return (re.sub(r'\s+where$', '', h), hit[0][0], hit[0][1])


def item(L, n, tag, file_, line, cur, new, why=''):
    L.append('  [%d] %s' % (n, tag))
    L.append('    FILE: %s' % file_)
    L.append('    LINE: %s' % line)
    L.append('    CURRENT: %s' % cur)
    L.append('    DRAFT:   %s' % new)
    if why:
        L.append('    WHY:     %s' % why)
    L.append('')


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def ahead(k, pin):
    return int(B.git('D:/' + k, 'rev-list', '--count', '%s..main' % pin).strip())


def load():
    H = json.load(io.open(B.HAND, encoding='utf-8'))
    C = json.load(io.open(CLASSES, encoding='utf-8'))
    U = B.units()
    O = dict((o['kernel'], o) for o in B.objects())
    return H, C, U, O


def grade(H, key, sid):
    return B.grade_of(H, key, sid)


def kernels_due(H, C, U, O):
    """the kernels the order names: a LOAD-BEARING EXCEEDS README or description row, or a title line that exceeds; the title line read as the first README row graded other than NO CLAIM."""
    lb = {}
    for c in C:
        if c['cls'] == 'LOAD-BEARING' and c['group'] in ('README', 'DESCRIPTION'):
            lb.setdefault(c['row'], []).append(c['id'])
    title = {}
    for g, row, key, sid, s, cl in U:
        if g == 'README' and row not in title and grade(H, key, sid)[0] != 'NO CLAIM':
            title[row] = (sid, s, grade(H, key, sid)[0])
    due = sorted(k for k in O if k in lb or title[k][2] == 'EXCEEDS')
    return due, lb, title


def controls():
    H, C, U, O = load()
    out = []
    k = 'SIDE-omega-b'
    ds = B.decls(k, O[k]['pin'])
    try:
        statement(k, O[k]['pin'], ds, 'SIDEOmegaB/Theorem.lean', 'amber_lantern_theorem')
        out.append(('a planted statement absent at the pin refuses', False))
    except SystemExit:
        out.append(('a planted statement absent at the pin refuses', True))
    h = statement(k, O[k]['pin'], ds, 'SIDEOmegaB/Theorem.lean', 'omega_b_equals_4_over_81')
    blob = B.git('D:/' + k, 'show', '%s:%s' % (O[k]['pin'], h[1]))
    out.append(('a statement quoted is the pin`s, whole, at its line', h[0].split(' ')[1] in blob.split(NL)[h[2] - 1]))
    due, lb, title = kernels_due(H, C, U, O)
    planted = dict(DRAFT)
    planted.pop('SIDE-bijection')
    out.append(('a kernel dropped from the table is seen', sorted(set(due) - set(PRIVATE)) != sorted(planted)))
    out.append(('a description over the limit is seen', len('x' * (GH_MAX + 1)) > GH_MAX))
    return out


def cmd_controls():
    for n, ok in controls():
        print('  %-60s %s' % (n, 'AS WANTED' if ok else '### NOT AS WANTED'))


def cmd_bank():
    t0 = B.utc()
    ctl = controls()
    if not all(ok for n, ok in ctl):
        raise SystemExit('### CONTROLS NOT AS WANTED: %s' % ctl)
    H, C, U, O = load()
    due, lb, title = kernels_due(H, C, U, O)
    if sorted(set(due) - set(PRIVATE)) != sorted(DRAFT):
        raise SystemExit('### THE TABLE AND THE CLASSES DIFFER: %s' % sorted(set(due).symmetric_difference(DRAFT)))
    text = dict(((g, row, sid), (key, s)) for g, row, key, sid, s, cl in U)
    gaps = dict((k, ahead(k, O[k]['pin'])) for k in due)
    L = ['b732 -- (R342)(5)-(6): THE DRAFTS FOR THE SECOND SITTING, ASSEMBLED AND NOT APPLIED (%s)' % t0, '',
         '### By tools/b732_frontdoors.py, in data/b726_frontdoors.txt`s form. Nothing here is applied: no README, GitHub description, Zenodo record, paper or kernel main is touched. Every draft is for the',
         '### author`s second sitting, by (R337)`s form, whose words govern. The grades and classes are data/b732_phase2_doors.txt`s. EVERY STATEMENT QUOTED IS READ AT THE KERNEL`S CENSUS PIN BY THE TOOL, VERBATIM.',
         '### THE TITLE LINE, READ: the first README row graded other than NO CLAIM. A kernel is due a paragraph and a description by a LOAD-BEARING README or description row, or by that row grading EXCEEDS.',
         '### THE PIN AND MAIN: a kernel whose main stands ahead of its pin is drafted at the pin, as the order says; the sitting decides for each such kernel whether the paragraph lands as drafted or is re-read at main, and the WHY prints the gap.',
         '### THE PRIVATE KERNEL: SIDE-constants is private and the relay public (data/repo_visibility.txt :17), so its rows go by digest and no draft text of it stands in this bank; the form is SPIRAL_MAP`s at data/b726_frontdoors.txt.',
         '', '## THE CONTROLS, BEFORE ANY DRAFT']
    for n, ok in ctl:
        L.append('  %-60s %s' % (n, 'AS WANTED' if ok else '### NOT AS WANTED'))
    n = 0
    # -------------------------------------------------- PART A
    rows = [c for c in C if c['cls'] == 'LOAD-BEARING']
    L += ['', '## PART A -- THE LOAD-BEARING SENTENCES, AT THE HEAD OF THE LIST (%d)' % len(rows), '']
    withheld = 0
    for c in rows:
        n += 1
        g, row, sid = c['group'], c['row'], c['id']
        key, s = text[(g, row, sid)]
        r = grade(H, key, sid)
        where = ' ; '.join(sorted(set('%s %s' % (h[0], h[1]) for h in c['hits'])))
        if row in PRIVATE:
            withheld += 1
            item(L, n, 'LOAD-BEARING, THE PRIVATE KERNEL', '%s README.md' % row, ':%s' % sid, '[private; sha256 %s]' % sha(s), 'NO DRAFT TEXT IN THIS BANK',
                 'cited at: the paper of the kernel`s own cluster, by repository and path at data/b732_door_classes.json. The sitting reads the kernel in its own repository.')
            continue
        target = {'README': 'the README paragraph of PART B for %s' % row, 'DESCRIPTION': 'the GitHub description of PART B for %s' % row, 'DEPOSIT': 'the note of PART C for %s' % row}[g]
        item(L, n, 'LOAD-BEARING', '%s %s' % (row, {'README': 'README.md', 'DESCRIPTION': 'GitHub description', 'DEPOSIT': 'Zenodo record %s' % key[4:]}[g]),
             ':%s (relay data/b732_phase2_doors.txt)' % sid, s, target, 'cited at: %s. %s' % (where, r[1]))
    # -------------------------------------------------- PART B
    L += ['## PART B -- THE README PARAGRAPHS AND THE GITHUB DESCRIPTIONS (%d kernels, SIDE-constants withheld)' % len(DRAFT), '']
    Rd = json.load(io.open(B.READS, encoding='utf-8'))
    quoted = 0
    for k in sorted(DRAFT):
        pre, st, post, desc = DRAFT[k]
        if len(desc) > GH_MAX:
            raise SystemExit('### %s DESCRIPTION %d CHARACTERS' % (k, len(desc)))
        pin = O[k]['pin']
        ds = B.decls(k, pin)
        q = [statement(k, pin, ds, f, nm) for f, nm in st]
        quoted += len(q)
        sid, s, g = title[k]
        why = 'title row %s graded %s; LOAD-BEARING rows %s' % (sid, g, ', '.join(lb.get(k, [])) or 'none')
        if gaps[k]:
            why += '. MAIN STANDS %d COMMITS AHEAD OF THE PIN: the sitting decides at which of the two this paragraph lands' % gaps[k]
        if k == 'SIDE-effects':
            why += '; THE WIDE CASE, the README at main names objects absent at this pin, present at main by file listing and not read, so this paragraph drafted at the pin would drop them'
        if k == 'SIDE-kernel':
            why += '; the line of data/b732_phase2_doors.txt`s kernel description is STATED, its draft keeps those words and drops only the stale "Current tag v1.4."'
        n += 1
        item(L, n, 'README PARAGRAPH', '%s README.md' % k, ':%s (the row under the title; the sentences of PART A and the SILENT rows go with it)' % sid, s,
             '%s Statements at %s: %s %s' % (pre, pin, ' '.join('%s (%s :%d)' % (h, f, ln) for h, f, ln in q), post), why)
        n += 1
        item(L, n, 'GITHUB DESCRIPTION', '%s GitHub description' % k, 'the one line (%d characters)' % len(desc), Rd[k].get('description') or '(none)', desc,
             'the current line graded %s' % grade(H, k, 'description')[0])
    # -------------------------------------------------- PART C
    L += ['## PART C -- THE DEPOSITED RECORDS THAT EXCEED (no Zenodo record is edited; read at data/b732_zenodo_read.json; T7 graded with no EXCEEDS row and takes no note: a clean document is a result)', '']
    for k, key, note in DEPOSIT:
        ex = [(sid, s) for (g, row, sid), (kk, s) in text.items() if g == 'DEPOSIT' and kk == key and grade(H, key, sid)[0] == 'EXCEEDS']
        if not ex:
            raise SystemExit('### %s HAS NO EXCEEDS ROW' % key)
        n += 1
        item(L, n, 'ZENODO NOTE', '%s Zenodo record %s' % (k, key[4:]), 'the end of the description', 'the exceeding rows, %s' % ' ; '.join('%s: %s' % (sid, s[:120]) for sid, s in ex), note,
             'b726`s CURRENCY words, then what the rows need. The note says nothing of a later Zenodo version: none was read.')
    # -------------------------------------------------- PART D
    L += ['## PART D -- THE SYNTHESIS HEAD SENTENCES THAT EXCEED, FOR THAT DOCUMENT`S NEXT EDITION, IN THE EDITION FORM`S CLAUSES (OPEN_TRAILS :11864)', '']
    for doc, sid, tag, new, why in HEADS:
        s = text[('HEAD', doc, sid)][1]
        n += 1
        item(L, n, 'HEAD SENTENCE, ' + tag, '%s phase2/physics/STORMER.md' % doc, sid, s, new, why)
    # -------------------------------------------------- PART E
    L += ['## PART E -- THE 2C NOTE, ONE PARAGRAPH FOR p2-41`S NEXT EDITION, APPLIED NOWHERE', '']
    n += 1
    item(L, n, 'THE 2C NOTE', 'phase2/method/THE_FINDINGS_AS_THEY_STAND (next edition)', 'a paragraph of its own; the sitting places it', '(none)', NOTE_2C, NOTE_2C_WHY)
    # -------------------------------------------------- PART F
    sil = {}
    for c in C:
        if c['cls'] == 'SILENT':
            sil[c['row']] = sil.get(c['row'], 0) + 1
    L += ['## PART F -- THE SILENT SENTENCES, CARRIED (%d): each row and its note stand at data/b732_phase2_doors.txt; cited by nothing, not repaired for a citation`s sake; each falls with its kernel`s README paragraph or note, except the rows of SIDE-orchestrator, whose kernel is due no paragraph (title row STATED, no LOAD-BEARING row), and of SIDE-constants, withheld' % sum(sil.values())]
    for k in sorted(sil):
        L.append('  %-36s %d' % (k, sil[k]))
    p = len(DRAFT)
    drafts = p * 2 + len(DEPOSIT) + len(HEADS) + 1
    L += ['', '### DRAFTS %d: README PARAGRAPHS %d, GITHUB DESCRIPTIONS %d, DEPOSIT NOTES %d, HEAD SENTENCES %d (ONE RESTATED, ONE REMOVED BY THE EDITION FORM), THE 2C NOTE 1. ITEMS %d, WITH THE %d ROWS OF PART A POINTING AT THEM.' % (drafts, p, p, len(DEPOSIT), len(HEADS), n, len(rows)),
          '### STATEMENTS QUOTED AT THEIR PINS %d. THE PRIVATE KERNEL: %d LOAD-BEARING ROWS BY DIGEST, NO DRAFT TEXT.' % (quoted, withheld), '',
          '### ### **ITEMS %d ; DRAFTS %d ; LOAD-BEARING %d ; SILENT %d CARRIED ; THE BEURLING ROW AT data/b726_mechanisms.txt BY ITS OWN COMMIT ; CONTROLS %d OF %d AS WANTED ; LISTED, APPLIED NOWHERE.**' % (n, drafts, len(rows), sum(sil.values()), sum(1 for x, ok in ctl if ok), len(ctl))]
    body = NL.join(L) + NL
    for w in ('TERMINUS', 'Book II', 'Book I '):
        if w in body:
            raise SystemExit('### A PRIVATE WORD IN THE BANK: %s' % w)
    with io.open(OUT + '.tmp', 'w', encoding='utf-8', newline='') as fh:
        fh.write(body)
    os.replace(OUT + '.tmp', OUT)
    print(L[-1])
    print('written', OUT, len(L), 'lines')


if __name__ == '__main__':
    fn = {'controls': cmd_controls, 'bank': cmd_bank}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit(__doc__)
    fn()
