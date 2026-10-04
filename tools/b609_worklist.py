# -*- coding: utf-8 -*-
"""b609_worklist.py -- THE ACT'S DATA, UNDER (R219)(2)-(3). ### NO WRITE.

### (R219)(3)(a): the sieve's v0.4 beside v0.3 (PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md at 3d2f67d) -- three
### rows added per OPEN_TRAILS :12518 (the computational range, GUE statistics, the mechanism enumeration), FD-01 and FD-02 read once,
### the head's counts re-stated. (R219)(3)(b): the monograph's v5.17 beside v5.16 (day1/A_Place_to_Stand_v5_16.md at 3d2f67d) --
### §24.4's three "no row" cells and the Epstein cell corrected to the v0.4 rows, §25.8's opening row to the qualified name, and
### nothing else. (R219)(2)(iv): the second reader's seed, the residue the ceiling pattern cannot see, every candidate of four
### matchers read by hand and marked. Each change is a fragment of a line copied from its blob (it must occur once on its line) with
### the seat's new wording; `resolve_*` read the blobs at the pin and check every fragment; nothing here writes.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PP = 'D:/MY-DOwnloads/PLACE-papers'
SKER = 'D:/SIDE-kernel'
EFK = 'D:/SIDE-explicit-formula'
PRE_PP = '3d2f67d'
NL = chr(10)

SV3 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'      # ### the sieve's current version, unedited
SV2 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'      # ### unedited
SV1 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'           # ### the unnumbered version, read as v0.1, unedited
SV4 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'      # ### this act's edition
M16 = 'day1/A_Place_to_Stand_v5_16.md'                        # ### the monograph's current version, unedited
M15 = 'day1/A_Place_to_Stand_v5_15.md'
M14 = 'day1/A_Place_to_Stand_v5_14.md'
M13 = 'day1/A_Place_to_Stand.md'
M17 = 'day1/A_Place_to_Stand_v5_17.md'                        # ### this act's edition


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


# ================================================================================ THE INSTRUMENTS AT THEIR PINS
T1 = '1 (I-7 @ 847e433; IB Thm 3.1 @ 1d0109f)'
T2 = '2 (detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f)'

# ### each new row's sources, resolved by git: (repo, rev, path, line, needle the line must hold)
INSTRUMENTS = {
    'RH-58': [(PP, PRE_PP, M16, 1500, '| Computation | Zero tables (Odlyzko, LMFDB) | 1986–present | 10¹³⁺ zeros simple'),
              ('D:/MY-DOwnloads/PLACE-papers', PRE_PP, 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 319,
               'as $10^{13}+$ computations confirm, RH holds at every zero computed')],
    'RH-59': [(PP, '847e433', 'phase1.5/method/INSTRUMENTS.md', 93, '## I-7 — THE PLACEMENT SCREEN'),(PP, '1d0109f', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 148, 'Theorem 3.1'),
              (PP, PRE_PP, 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 343,
               'GUE statistics predict 100% simplicity in the limit'),
              (PP, PRE_PP, 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 240, 'fitted $\\beta \\approx 12.32$'),
              (PP, PRE_PP, M16, 1478, 'Montgomery (1973) conjectured, and Odlyzko (1987) computationally confirmed')],
    'RH-60': [(EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean', 99, 'theorem detector (C : WeilConfig)'),
              (EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean', 57, 'theorem epstein_not_h2_sign_cfg'),
              (PP, '1d0109f', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 259, 'Theorem 3.7'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 20, 'inductive MechanismClass where'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 25, 'theorem seven_classes'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 79, 'theorem ostrowski_exhaustive_prime'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 157, 'noncomputable def produces_offline : MechanismClass -> Prop'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 159, '| .C2_euler => ∃ σ : Real, σ ≠ 1 / 2 ∧ -σ = -(1 - σ)'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 198, 'theorem none_produce'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 249, 'theorem structural_exhaustiveness_proved'),
              (SKER, 'v1.5', 'Bridge/TheBridgeComplete.lean', 251, '⟨seven_classes, none_produce, ostrowski_exhaustive_prime⟩'),
              (SKER, 'v1.5', 'Kernel/Integration.lean', 213, '∀ (sigma : Real), is_xi_zero sigma → sigma = 1 / 2'),
              (SKER, 'v1.5', 'Kernel/Integration.lean', 252, 'theorem structural_exhaustiveness_iff_rh'),
              (PP, PRE_PP, 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 33, '29. `SIDEExplicitFormula.Schema.detector` — SIDEExplicitFormula/Schema/Detector.lean:99 — v0.16 = c404e72')],
}
# ### the four compiled pieces the ferry names, searched on both pages at PLACE-papers HEAD: none is a node of either page
PIECES = ['structural_exhaustiveness_proved', 'seven_classes', 'none_produce', 'ostrowski_exhaustive']

# ================================================================================ THE SIEVE AT v0.4: THE THREE ROWS
NAR, DARK = 'NOT A ROUTE', 'DARK'
NEW_ROWS = [
    dict(id='RH-58', after='RH-57', verdict=NAR, test='—',
         conclusion='The zeros of ζ computed to a finite height, 10¹³ and more of them, are simple and on the line; the range is finite and '
                    'says nothing of the zeros beyond it.',
         shape='FINITE (H)', register='the computational range',
         reason='a bench fact: a finite range of zeros computed simple and on the line, offered toward no target and recorded at its own '
                'grade, the zeros beyond the range left open',
         face='computed, no declaration: the zero tables (Odlyzko, LMFDB) as A_Place_to_Stand v5.16 §24.4 cites them (:1500), and '
              'SIMPLICITY v1.1.3 :319'),
    dict(id='RH-59', after='RH-58', verdict=DARK, test=T1,
         conclusion='The unfolded spacings of ζ’s zeros match the GUE statistics to every tested range, and GUE predicts that no zero is '
                    'multiple; a statistic over the ordinates, a conjecture with numerical support.',
         shape='DENSITY (H)', register='the super-repulsion fit',
         reason='a GUE statistic offered toward simplicity: a statistic over the ordinates carries no zero’s real part and no zero’s '
                'multiplicity, the bench’s super-repulsion fit read beside it',
         face='none: Montgomery 1973 (pair correlation) and Odlyzko 1987 (the computed spacings), as SIMPLICITY v1.1.3 :343 and '
              'A_Place_to_Stand v5.16 §24.2 (:1478) cite them'),
    dict(id='RH-60', after='RH-59', verdict=DARK, test=T2,
         conclusion='The seven mechanism classes are enumerated, Ostrowski-exhaustive at the places of ℚ, and each class’s exclusion compiles '
                    'as a statement about a real σ alone; the step from the classes to ξ’s zeros is open -- at their real parts it is the '
                    'located clause, at their multiplicity the geometric clause.',
         shape='UNIVERSAL (H)', register='the mechanism catalogue',
         reason='a candidate route toward the located clause and toward simplicity through the classes: its compiled exclusions name no '
                'function -- C₂_euler’s off-line condition is σ ≠ 1/2 ∧ -σ = -(1 - σ), the Euler product entering none of them -- so they '
                'hold unchanged beside the Epstein configuration, which the detector meets at ρ_E with a negative window; no page carries '
                'a node of the route',
         face='`_root_.structural_exhaustiveness_proved` @ SIDE-kernel v1.5 = 0e5233f (Bridge/TheBridgeComplete.lean :249; its conjuncts '
              '`seven_classes` :25, `none_produce` :198, `ostrowski_exhaustive_prime` :79), not a page node'),
]


def row_line(r):
    return '| %s | %s | %s | %s | %s | %s | %s | %s |' % (r['id'], r['conclusion'], r['shape'], r['register'], r['verdict'], r['test'],
                                                          r['reason'], r['face'])


VERSION4 = ('*v0.4, 2026-10-03 -- three rows added (the computational range, GUE statistics, the mechanism enumeration) and the Epstein '
            'rows read as two conclusions; v0.3 stands beside it, unedited.*')

# ### the head's rewrites: (v0.3 line, old fragment, new fragment, what)
SV_REWRITES = [
    (38, ' -- not about its object).',
     ' -- not about its object); at v0.4, two more: the computational range (the zeros computed simple and on the line, to a finite '
     'height); the mechanism catalogue (the seven mechanism classes, their per-class exclusions and the place count).',
     'the registers: the two the added rows read, (R219)(3)(a)'),
    (42, '5 of them carry the table’s 84 rows', '5 of them carry the table’s 87 rows', 'the head`s row count re-stated, (R219)(3)(a)'),
    (46, '84 rows -- 2 BRIGHT, 5 DARK, 66 NOT A ROUTE, and 11 FACE rows', '87 rows -- 2 BRIGHT, 7 DARK, 67 NOT A ROUTE, and 11 FACE rows',
     'the head`s verdict counts re-stated, (R219)(3)(a)'),
    (48, '— 57 rows: 11 FACE, 2 BRIGHT, 5 DARK, 39 NOT A ROUTE', '— 60 rows: 11 FACE, 2 BRIGHT, 7 DARK, 40 NOT A ROUTE',
     'the cluster heading`s counts re-stated'),
    (68, '— 46 rows', '— 49 rows', 'the other rows` heading re-stated'),
]

# ### FD-01 and FD-02, read once (R219)(3)(a): one conclusion or two
FD_READ = dict(
    decision='two conclusions, two rows',
    reason=('FD-01 (`epstein_not_h2_sign_cfg`, SIDE-explicit-formula v0.16, Schema/Epstein.lean :57) concludes that a configuration is '
            'not Weil-positive and needs the located point in its carrier (hE : rhoE ∈ Z.carrier); FD-02 (`epstein_ef_at_window`, v0.20, '
            'Schema/PlateauRamp.lean :209) concludes the premises’ explicit formula at the plateau-ramp window and names no zero -- two '
            'declarations at two pins with two statements, neither implying the other'),
    lines=[(EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean', 58, '(hE : rhoE ∈ Z.carrier) : ¬ h2_sign_cfg (epsteinConfig Z rhs hP)'),
           (EFK, 'v0.20', 'SIDEExplicitFormula/Schema/PlateauRamp.lean', 209, 'theorem epstein_ef_at_window (Z : Zeta23.ZeroConfig) (rhs : (ℝ → ℂ) → ℂ) (hE : EpsteinPremises Z rhs)')],
    navigator=('(N2)’s reason, “two located zeros, two witnesses”, is not what the statements carry: one located point, ρ_E, enters '
               'FD-01 alone, and FD-02 names none'))

# ### the mechanism-enumeration row, decided against the pages and the detector (R219)(3)(a), H43b
MECH = dict(
    navigator='BRIGHT by test 2, the detector the instrument that shows C₂ is the class the control removes',
    verdict='DARK, test 2',
    deciding=[('SIDE-explicit-formula v0.16 = c404e72, Schema/Detector.lean :99 (the χ page node 29, its line :33)',
               'the detector is generic over WeilConfig and names no mechanism class'),
              ('SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean :157, :159',
               'produces_offline is a predicate on a real σ alone; C₂_euler’s is σ ≠ 1/2 ∧ -σ = -(1 - σ), carrying no Euler product'),
              ('SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean :249-:251',
               'the route’s compiled face is the conjunction of seven_classes, none_produce and ostrowski_exhaustive_prime, closed with no '
               'function argument, so it holds beside every configuration, the Epstein one among them'),
              ('SIDE-kernel v1.5 = 0e5233f, Kernel/Integration.lean :213, :252',
               'the step to ξ’s zeros is Integration’s StructuralExhaustiveness, ∀ σ, a ξ-zero at σ forces σ = 1/2 -- RH restated, the '
               'located clause’s target, open'),
              ('SIDE-explicit-formula v0.16 = c404e72, Schema/Epstein.lean :57',
               'at the Epstein configuration the located point ρ_E makes the configuration not Weil-positive (FD-01)'),
              ('the pages at PLACE-papers HEAD', 'no node of either page is one of the four compiled pieces')],
    refuted=('the navigator’s BRIGHT-by-test-2 reading is refuted: the detector names no class and no compiled line ties C₂ to the '
             'Epstein configuration; that the route located the clause does not give it the clause’s prime side, which the located '
             'clause’s FACE rows carry (:{FACE_LINE})'))

# ================================================================================ THE MONOGRAPH AT v5.17: THE FIVE CELLS
# ### (id, v5.16 line, old fragment, new fragment with {S4:...} tokens resolved from the sieve's v0.4 lines, clause, why, cites)
CELLS = [
    ('V01', 1499, 'DARK, test 1 — no row; the bench’s super-repulsion fit (v0.3 :593): a spacing statistic carries no real part',
     'DARK, test 1 — RH-59 (v0.4 :{S4:RH-59}), GUE statistics as a row beside the bench’s super-repulsion fit (v0.4 :{S4:bench_sr}): a '
     'spacing statistic carries no real part',
     'the restatement clause', 'the GUE row’s “no row” cell corrected to the v0.4 row (R219)(3)(b)', 'the sieve v0.4 RH-59 (:{S4:RH-59})'),
    ('V02', 1500, 'no row at v0.3 — the sieve carries no row and no register for a finite range of zeros found simple',
     'NOT A ROUTE — RH-58 (v0.4 :{S4:RH-58}), the computational range: a finite range of zeros computed simple and on the line, a bench '
     'fact offered toward no target',
     'the restatement clause', 'the computation row’s “no row” cell corrected to the v0.4 row (R219)(3)(b)', 'the sieve v0.4 RH-58 (:{S4:RH-58})'),
    ('V03', 1501, 'NOT A ROUTE — FD-01 (v0.3 :277) and FD-02 (v0.3 :278), the Epstein witnesses: test 2’s own instrument, not a route; the '
     'bench (v0.3 :595)',
     'NOT A ROUTE — FD-01 (v0.4 :{S4:FD-01}) and FD-02 (v0.4 :{S4:FD-02}), the Epstein witnesses, read at v0.4 as two conclusions: the '
     'compiled control on the located point ρ_E, and the explicit formula at the plateau-ramp window, which names no zero; test 2’s own '
     'instrument, not a route; the bench (v0.4 :{S4:bench_ep})',
     'the restatement clause', 'the Epstein cell corrected to the v0.4 rows, read as two conclusions (R219)(3)(b)',
     'the sieve v0.4 FD-01 (:{S4:FD-01}), FD-02 (:{S4:FD-02}) and its back matter’s reading'),
    ('V04', 1502, 'no row at v0.3 — the sieve carries no row for the per-class reductions; their joint step is the geometric clause, '
     'carried openly',
     'DARK, test 2 — RH-60 (v0.4 :{S4:RH-60}), the mechanism enumeration: its compiled per-class exclusions name no function, so they '
     'hold beside the Epstein configuration; their joint step is the geometric clause, carried openly',
     'the restatement clause', 'the mechanism row’s “no row” cell corrected to the v0.4 row (R219)(3)(b)', 'the sieve v0.4 RH-60 (:{S4:RH-60})'),
    ('V05', 1674, '| `structural_exhaustiveness_proved` | `Bridge/TheBridgeComplete.lean` |',
     '| `_root_.structural_exhaustiveness_proved` | `Bridge/TheBridgeComplete.lean` |',
     'the fact clause', 'the concordance’s opening row takes the qualified name (R219)(2)(ii): the bare name resolves at the terminal '
     'table to the conditional theorem of namespace ConservationBridge', 'SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean '
     ':249 (no namespace) beside Bridge/ConservationBridge.lean :7, :46'),
]
M_CORR = 2240           # ### v5.16's own Correspondence heading: the body is every line above it

# ================================================================================ THE SECOND READER'S SEED (R219)(2)(iv)
RESIDUE_MATCHERS = [
    ('M1', 'establish / settle / resolve', re.compile(r'\b(establish(?:es|ed|ing)?|settl(?:e|es|ed|ing)|resolv(?:e|es|ed|ing))\b', re.I)),
    ('M2', 'a proof label', re.compile(r'\*Proof\.?\*|\*\*Proof\.?\*\*|^Proof\.|^## \d+\.\d+ Proof$')),
    ('M3', 'demonstrate / conclusive / unfoldable / definitive / decisive', re.compile(r'\b(demonstrat\w*|conclusive\w*|unfoldable|definitive\w*|decisive\w*)\b', re.I)),
    ('M4', 'a QED mark', re.compile(r'∎|\bQ\.?E\.?D\b|□')),
]
KIN, NOT, LABEL, DATED = 'KIN', 'NOT KIN', 'LABEL', 'DATED'
# ### the seat's marks on v5.16's body, every candidate read by hand in its sentence: (line, word) -> (mark, reason)
MARKS16 = {
    (67, 'establishes'): (KIN, 'a reading guide says an argument Part establishes σ = 1/2’s significance'),
    (416, 'established'): (KIN, 'the I+D+S conditions said established for ξ in an argument Part'),
    (420, 'established'): (KIN, 'the I+D+S conditions said established for ξ in Chapter 13'),
    (451, 'establishes'): (KIN, 'Part I said to establish where the zeros must be'),
    (461, 'established'): (KIN, 'Part I said to have established σ = 1/2 distinguished'),
    (534, 'establishes'): (KIN, 'an argued chapter said to establish spectral silence; the compiled terminal states (1 : ℚ)^s = 1'),
    (766, 'establish'): (KIN, 'two chapters said to establish the seal that makes the catalogue sufficient'),
    (798, 'resolves'): (NOT, 'Connes’ framework, external literature'),
    (836, 'establishes'): (NOT, 'a field fact about classical density theorems'),
    (980, 'Resolves'): (NOT, 'a table column label'),
    (996, 'settled'): (NOT, 'field facts about ℤ'),
    (1018, 'establishes'): (KIN, 'a closure said to establish why the zeros cannot be elsewhere'),
    (1114, 'establish'): (KIN, '§18.1: five results said to establish the conversion (the seat’s list at b608)'),
    (1128, 'establish'): (KIN, 'the five closures said each to establish that codimension-2 coincidences cannot occur'),
    (1130, 'resolved'): (KIN, '§18.3: the codimension question said resolved by five results (the seat’s list at b608)'),
    (1231, 'established'): (NOT, 'established computation, a field fact'),
    (1231, 'resolving'): (NOT, 'a conditional on a chain not produced'),
    (1281, 'resolves'): (NOT, 'conditional on GRH, corrected at v5.16 (X05)'),
    (1285, 'established'): (NOT, 'a requirement still to be met'),
    (1800, 'established'): (DATED, 'carried with a history line beneath under E-2026-09-22-1 (v5.14)'),
    (1806, 'established'): (NOT, 'Voros, literature'),
    (1810, 'established'): (NOT, 'compiled kernel facts at their tiers (T1, T2)'),
    (1952, 'Resolve'): (NOT, 'a document title, Critical Resolve'),
    (1959, 'Resolve'): (KIN, 'the title is a name; the row’s status “Verified” for no class producing off-line zeros reads past none_produce, '
                            'a statement about a real σ'),
    (2233, 'establishing'): (DATED, 'the dated Correspondence of 2026-08-12, carried by the history clause (R-8)'),
    (431, '## 7.2 Proof'): (LABEL, 'chapter 7’s proof heading, the bijection conditional on I+D+S'),
    (780, '*Proof.*'): (LABEL, 'a lemma’s proof label in chapter 13'),
    (1350, '*Proof.*'): (LABEL, 'a lemma’s proof label in chapter 22'),
    (1358, '*Proof.*'): (LABEL, 'a lemma’s proof label in chapter 22'),
    (1366, '*Proof.*'): (LABEL, 'a lemma’s proof label in chapter 22'),
    (1380, '*Proof.*'): (LABEL, 'a lemma’s proof label in chapter 22, the fold lemma'),
    (317, 'unfoldable'): (KIN, '§4.5: ξ said unfoldable, where the absence of folds is RH-equivalent (the seat’s list at b608)'),
    (359, 'demonstrated'): (NOT, 'a finite computation at its grade'),
    (772, 'definitive'): (NOT, 'Tate, literature'),
    (930, 'demonstrate'): (NOT, 'a field fact, Epstein’s off-line zeros'),
    (1258, 'demonstrate'): (NOT, 'an example announced'),
    (1275, 'demonstrated'): (KIN, 'the SIDE conditions said verified for each L(s, χ), the transfer shown for χ mod 5 alone'),
    (1780, 'demonstrated'): (NOT, 'the Trivium code at its re-scoped grade'),
    (1883, 'demonstrating'): (KIN, 'the Epstein experiment read as demonstrating class independence; no compiled line ties a class to it'),
    (1883, 'demonstrate'): (KIN, 'polynomials and Hadamard products read as demonstrating output-stage independence'),
    (1954, 'Demonstrated'): (NOT, 'the Trivium code at its re-scoped grade'),
    (2196, 'demonstrated'): (DATED, 'a version-history entry (v5.9.2)'),
}


def residue_hits(lines, upto):
    out = []
    for mid, _desc, rx in RESIDUE_MATCHERS:
        for i, l in enumerate(lines[:upto]):
            for m in rx.finditer(l):
                out.append((mid, i + 1, m.group(0)))
    return out


def sieve_mark(n, l, word):
    """### the sieve v0.3's candidates: every one negated, inside a dated history block, or in the back matter -- read by hand."""
    low = l.lower()
    if 'not establish' in low or 'neither side is established' in low or 'rather than resolved' in low or 'not resolved' in low:
        return NOT, 'negated'
    if l.startswith('>') or l.startswith('The arc summary') or 'Collisions resolved' in l or l.startswith('| '):
        return DATED if l.startswith('>') or l.startswith('The arc summary') else NOT, \
            'a dated block quoted under the history clause' if l.startswith('>') or l.startswith('The arc summary') else 'a back-matter record'
    return None, None


# ================================================================================ THE RESOLVERS
def _at(repo, rev, path, n):
    ls = lines_of(show(rev, path, repo))
    return ls[n - 1] if 0 < n <= len(ls) else None


def resolve_instruments():
    """### every new row's sources and the FD lines resolve: the pin exists, the line exists, its needle is on it."""
    out = []
    for rid, src in list(INSTRUMENTS.items()) + [('FD', FD_READ['lines'])]:
        for repo, rev, path, n, needle in src:
            l = _at(repo, rev, path, n)
            ok = l is not None and (needle is None or needle in l)
            out.append(dict(row=rid, repo=os.path.basename(repo), rev=rev, path=path, line=n, ok=ok, text=(l or '### NO SUCH LINE')[:200]))
    return out


def resolve_sieve():
    S3 = lines_of(show(PRE_PP, SV3))
    bad = []
    for n, old, new, what in SV_REWRITES:
        if S3[n - 1].count(old) != 1:
            bad.append(('rewrite', n, S3[n - 1].count(old)))
    ids = [l.split(' | ')[0][2:] for l in S3 if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    for r in NEW_ROWS:
        if r['id'] in ids:
            bad.append(('row id taken', r['id']))
        if any(x in row_line(r) for x in ('|  |', ' || ')):
            bad.append(('blank cell', r['id']))
        if row_line(r).count(' | ') != 7:
            bad.append(('cells', r['id'], row_line(r).count(' | ')))
    return S3, bad


def resolve_cells():
    M = lines_of(show(PRE_PP, M16))
    bad = []
    for cid, n, old, new, clause, why, cites in CELLS:
        if M[n - 1].count(old) != 1 or n >= M_CORR:
            bad.append((cid, n, M[n - 1].count(old)))
    if not M[M_CORR - 1].startswith('## Correspondence *(added 2026-08-12'):
        bad.append(('corr', M_CORR))
    return M, bad


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    _S3, b1 = resolve_sieve()
    _M, b2 = resolve_cells()
    ins = resolve_instruments()
    print('sieve rewrites %d, rows %d: %s ; cells %d: %s ; instruments %d of %d resolve %s' % (
        len(SV_REWRITES), len(NEW_ROWS), b1 or 'OK', len(CELLS), b2 or 'OK', sum(x['ok'] for x in ins), len(ins),
        [(x['row'], x['path'], x['line']) for x in ins if not x['ok']] or ''))
    hits = residue_hits(_M, M_CORR - 1)
    unmarked = [(n, w) for _m, n, w in hits if (n, w) not in MARKS16]
    print('residue candidates in v5.16`s body %d ; unmarked %s ; marks without a candidate %s' % (
        len(hits), unmarked or 'NONE', sorted(set(MARKS16) - set((n, w) for _m, n, w in hits)) or 'NONE'))
