# -*- coding: utf-8 -*-
"""b608_worklist.py -- CP-8 ACT THREE'S WORK-LIST AS DATA, UNDER (R218)(4). ### NO WRITE.

### The scope (R218)(4) fixes: the monograph's v5.15 (PLACE-papers day1/A_Place_to_Stand_v5_15.md at 0800a6a) outside the sentences
### acts one and two wrote or read, with the whole document as the bound under the multi-act clause (OPEN_TRAILS :12496): the b558
### work-list's 31 rows (relay data/b558_editions/A_Place_to_Stand.txt, numbered by v5.13, mapped to v5.15 through b606's and b607's
### banked maps), every remaining ceiling hit of b607's 154, Part IV's preamble (:1305-:1311), chapter 24's opening and title, the
### stem at :722, the §22.4 item of (R218)(3) and §25.8's Kernel Concordance. Each change is a fragment of a v5.15 line copied from
### its blob (it must occur once on its line) with the seat's new wording, the clause that reaches it, and what it cites; each carry is
### a fragment holding a ceiling hit with its named exception. The resolver (`resolve`) reads the blob at the pin and checks every old
### wording, every carry and the coverage of every ceiling hit in the body; nothing here writes.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PP = 'D:/MY-DOwnloads/PLACE-papers'
CUR = 'day1/A_Place_to_Stand_v5_15.md'          # ### the current version this act reads (v5.15), unedited
PREV = 'day1/A_Place_to_Stand_v5_14.md'         # ### v5.14, unedited
ORIG = 'day1/A_Place_to_Stand.md'               # ### v5.13, unedited
ED = 'day1/A_Place_to_Stand_v5_16.md'
PRE_PP = '0800a6a'
NL = chr(10)
CORR_LINE = 2237        # ### v5.15's own Correspondence heading: the body is every line above it


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


# ================================================================================ THE CITATIONS, AS THE PAGES, THE TABLE AND THE BANKS PRINT THEM
H2 = 'h2_sign_iff_rh (v0.2 = 5c72cad, ζ page node 8); README :106'
OST = ('OPEN_TRAILS :12072 (the author’s reading: census proved, exhaustiveness open -- Ostrowski closes the place count, the catalogue’s '
       'exhaustiveness at ξ is the open premise h2); h2_sign_iff_rh (v0.2, ζ page node 8)')
CONS = ('conservation_of_spectra (SIDE-kernel v1.5 = 0e5233f, Kernel/ProductFormula_Rat.lean :72: ∀ (s : Int), (1 : Rat) ^ s = 1), T2; '
        'relay data/b558_cp1b.txt :513, :526, :529, :573, :575')
CH = 'ch_iff_rh (v0.1 = baed4df, ζ page node 7); ERRATA E-2026-09-25-1 (:486)'
SC = ('SpectralCannonFull.spectral_cannon (SIDE-kernel v1.5 = 0e5233f, Kernel/SpectralCannonFull.lean :65); ERRATA E-2026-09-25-5, '
      'E5-05 (:641, replacement :643)')
SIMP = 'simplicity_iff (v0.17, ζ page node 41); positivity_not_imp_simplicity (v0.19, ζ page node 52)'
CHI = 'h2_sign_chi_iff_grh_chi (v0.14 = 4dce7b9, χ page node 12)'
LI = ('partialPositivity_finiteRange (SIDE-lv-conservation v0.8.0 = 6efa9e5), T1-lit; the work-list row (relay '
      'data/b558_editions/A_Place_to_Stand.txt, :1810) and relay data/b558_cp1b.txt :565, :278')
E611 = 'ERRATA E-2026-09-25-6, E6-11 (:735, replacement :737): for each class, algebra forcing σ = 1/2 from its stated constraint'
V591 = 'the monograph’s own dated entry v5.9.1 (4) (v5.15 :2193): the [[7,1,3]] “proved” claims re-scoped to demonstrated'
J = 'the joins of act two (J06, J07, J12; v5.15 back matter :2448-:2470)'

LEANC = '`∀ s : ℤ, (1 : ℚ) ^ s = 1`'

# ================================================================================ THE CHANGES
# ### (id, v5.15 line, kind, clause, old (a fragment of the line, copied; once on it), new, cites, why)
# ### kind: row (a b558 work-list row), ceiling, restatement, stem, fact, title, repin (§25.8's pin column)
CHANGES = [
    # ### ------------------------------------------------ the b558 work-list's rows that stand verbatim in v5.15
    ('W01', 105, 'row', 'the work-list row (v5.13 :103, conservation_of_spectra)',
     '| Tate 1950, Lean-verified |',
     '| Tate 1950; in Lean the terminal `conservation_of_spectra` states ' + LEANC + ' (T2), its conservation reading carried by the name |',
     CONS, 'calls n₄ = 0 via Conservation of Spectra “Lean-verified”; the Lean terminal states (1 : ℚ) ^ s = 1, its reading carried by the name'),
    ('W03', 1008, 'row', 'the work-list row (v5.13 :1006, conservation_of_spectra)',
     'n₄ = 0 from Conservation of Spectra (Lean-verified)',
     'n₄ = 0 from Conservation of Spectra (in Lean its terminal states ' + LEANC + ', T2)',
     CONS, 'calls n₄ = 0 from Conservation of Spectra “Lean-verified”; the terminal states (1 : ℚ) ^ s = 1, T2'),
    ('W04', 1206, 'row', 'the work-list row (v5.13 :1204, conservation_of_spectra)',
     '| Proved (ZFC), Lean-verified |',
     '| Proved (ZFC); in Lean the terminal states ' + LEANC + ' (T2) |',
     CONS, 'marks Conservation of Spectra “Lean-verified”; the terminal states (1 : ℚ) ^ s = 1, T2'),
    ('W05', 1577, 'row', 'the work-list row (v5.13 :1573, ch_iff_rh), E-2026-09-25-1’s phrase',
     'Three routes compile independently in Lean: Route 1 (structural exhaustiveness) on its own, Route 2 (codimension / Spectral Cannon) on its own, Route 3 (Conservation) on its own.',
     'Three route terminals compile independently in Lean: Route 1 (structural exhaustiveness) on its own, Route 2 (codimension / Spectral Cannon) on its own, Route 3 (Conservation) on its own, its premise RH restated (ch_iff_rh).',
     CH, 'says three routes compile independently, Route 3 among them; Route 3’s premise is RH restated -- the phrase E-2026-09-25-1 replaced with “three route terminals”'),
    ('W07', 1634, 'row', 'the work-list row (v5.13 :1630, ch_iff_rh)',
     '| Route 3 — RH from Conservation + balance |',
     '| Route 3 — RH from `ConservationHypothesis`, which `balance_theorem` shows is RH restated (ch_iff_rh) |',
     CH, 'counts Route 3 among routes to RH; its premise is RH restated, so it formalizes RH from RH restated'),
    ('W10', 1673, 'row', 'the work-list rows (v5.13 :1669, ch_iff_rh and riemann_hypothesis)',
     '| Route 3 — RH from the conservation interface |',
     '| Route 3 — RH from the conservation interface `ConservationHypothesis`, RH restated (ch_iff_rh) |',
     CH, 'names the row “RH from the conservation interface”; the interface is RH restated, so the row is RH from RH restated'),
    ('W15', 1818, 'row', 'the work-list row (v5.13 :1810, partialPositivity_finiteRange)',
     'certifies λ_n ≥ 0 for n up to Voros\'s detection threshold N₀(T) ≈ 2T², with',
     'certifies λ_n ≥ 0 for n up to Voros\'s detection threshold N₀(T) ≈ 2T² under two uncompiled literature premises (Bombieri–Lagarias, Voros) and verified zeros — T1-lit, not compiled outright — with',
     LI, 'presents λ_n ≥ 0 up to N₀(T) as certified outright; the terminal proves it only under two uncompiled literature premises and verified zeros, T1-lit'),
    ('W19', 1863, 'row', 'the work-list row (v5.13 :1855, conservation_of_spectra)',
     'Conservation of Spectra, proved from Tate\'s thesis within ZFC and verified in Lean.',
     'Conservation of Spectra, argued from Tate\'s thesis within ZFC (Chapter 13); in Lean its terminal states ' + LEANC + ' (T2).',
     CONS, 'says Conservation of Spectra is “verified in Lean”; the terminal states (1 : ℚ) ^ s = 1, T2'),
    ('W20', 1942, 'row', 'the work-list row (v5.13 :1934, conservation_of_spectra)',
     '| Proved (ZFC), Lean-verified |',
     '| Proved (ZFC); in Lean the terminal states ' + LEANC + ' (T2) |',
     CONS, 'marks the s-darkness of the product formula “Lean-verified”; the terminal states (1 : ℚ) ^ s = 1, T2'),
    # ### ------------------------------------------------ the stem at :722 and its ceiling hits (the precedence order: stem, then ceiling)
    ('S01', 722, 'stem', 'the stem clause (OPEN_TRAILS :11904)',
     'five independent closures of the codimension gap',
     'five independent closures of the step from structural to actual independence (§18.1)',
     'the object chapter 18 names: §18.1 “From Structural to Actual” (v5.15 :1109, :1113)', 'the scanner`s one live stem; the object the sentence names is the conversion of §18.1'),
    ('C001', 722, 'ceiling', 'the ceiling clause (OPEN_TRAILS :11906)',
     'the dichotomy the whole proof turns on',
     'the dichotomy the whole reduction turns on', H2, '“the whole proof” names the monograph`s argument a proof of RH'),
    ('C002', 722, 'ceiling', 'the ceiling clause',
     'seven mechanism classes, proved exhaustive by Ostrowski',
     'seven mechanism classes, their place count closed by Ostrowski and their exhaustiveness at ξ the open clause h2',
     OST, 'exhaustiveness at ξ is the open premise; Ostrowski closes the place count'),
    # ### ------------------------------------------------ Part IV's preamble: the restatement clause, citing the rows it restates (R218)(4)
    ('P01', 1305, 'restatement', 'the restatement clause (OPEN_TRAILS :12192), restating J12',
     'This Part reaches RH through a different strategy',
     'This Part argues toward RH through a different strategy', J + '; ' + SIMP, 'restates “Part IV argues RH from simplicity” (J12), a join act two read as an open direction'),
    ('P02', 1305, 'restatement', 'the restatement clause, restating J06',
     'the conditional (simplicity → RH) is proved, while',
     'the conditional (simplicity → RH) is the programme’s reading of an open direction, an edge no compiled statement carries (simplicity_iff, v0.17; positivity_not_imp_simplicity, v0.19), while',
     J + '; ' + SIMP, 'restates the conditional act two`s J06 reads as an open direction'),
    ('P03', 1305, 'ceiling', 'the ceiling clause',
     'Part III\'s proof does not consume this clause',
     'Part III\'s reduction does not consume this clause', H2, '“Part III`s proof” names the reduction a proof of RH'),
    ('P04', 1307, 'restatement', 'the restatement clause, restating J02',
     'We establish it here.',
     'We argue it here, as an open direction (§22.5).',
     J + '; ' + SIMP, 'restates the direction J02 reads as the programme`s reading of an open direction'),
    ('P05', 1309, 'restatement', 'the restatement clause, restating J06',
     '**Theorem (ZFC).** If all nontrivial zeros of ξ are simple, then the Riemann Hypothesis holds.',
     '**The conditional, the programme’s reading of an open direction.** If all nontrivial zeros of ξ are simple, then the Riemann Hypothesis holds — an edge no compiled statement carries (simplicity_iff, v0.17; positivity_not_imp_simplicity, v0.19).',
     J + '; ' + SIMP, 'restates J06`s theorem, which act two read as an open direction'),
    ('P06', 1311, 'restatement', 'the restatement clause, restating J07 and E5-05',
     'The proof uses the perpendicular crossing theorem (formally verified in Lean 4)',
     'The argument uses the perpendicular crossing theorem (compiled in Lean 4 for completedRiemannZeta₀ as spectral_cannon, §25.8; the same fact for ξ′ is not compiled)',
     J + '; ' + SC, 'restates J07`s “proof” and the perpendicular crossing E5-05 corrected'),
    ('P07', 1311, 'restatement', 'the restatement clause, restating J06',
     'The simplicity reduction (this theorem) provides',
     'The simplicity reduction (this conditional) provides', J, 'names the conditional a theorem'),
    # ### ------------------------------------------------ chapter 24's title and opening (R218)(4): the ceiling clause, the title naming objects
    ('T01', 1463, 'title', 'the ceiling clause, the title naming objects (R218)(4)',
     '# Chapter 24: Three Proofs Converge',
     '# Chapter 24: Three Traditions on Simplicity, Convergent Evidence',
     '§24.4`s convergence table and its sieve column (v5.15 :1493-:1499, act two`s T00-T06)', 'the title names three proofs converging; the chapter carries three traditions` evidence on simplicity, none a proof (§24.4)'),
    ('T02', 1465, 'ceiling', 'the ceiling clause (R218)(4)',
     'converge on the same conclusion: all zeros of ξ are simple.',
     'bear on the same question, whether all zeros of ξ are simple: a proportion (§24.1), a statistical prediction conditional on GUE (§24.2), and per-class reductions whose joint step is the geometric clause, open (§24.3, §24.4).',
     '§24.4`s table (RH-16 DARK, test 1; GUE in the bench, DARK, test 1; the mechanism row`s joint step open); ' + SIMP,
     'the opening states all zeros simple as the conclusion of three traditions; §24.4 carries them as evidence rows, none as proof'),
    ('T03', 1487, 'restatement', 'the restatement clause, restating §22.5 and §24.4`s mechanism row',
     'The answer is the same: nothing in the seven mechanism classes produces the codimension-2 coincidence ξ(ρ) = ξ\'(ρ) = 0.',
     'The answer per class is the same: no one of the seven mechanism classes produces the codimension-2 coincidence ξ(ρ) = ξ\'(ρ) = 0 (C₁ derives, the others at the interface level); the joint step is the geometric clause, open (§22.5, §24.4).',
     '§22.5 (v5.15 :1397) and §24.4`s mechanism row (:1498)', 'states the joint step as settled; §22.5 and §24.4 carry it open'),
    # ### ------------------------------------------------ §25.5's restatements of the route rows (E-2026-09-25-1's “route terminals”)
    ('R01', 1583, 'restatement', 'the restatement clause, restating the :1573 row',
     '## 25.5 The Three Compiled Routes',
     '## 25.5 The Three Compiled Route Terminals', CH, 'counts Route 3 a route, the phrase E-2026-09-25-1 replaced'),
    ('R02', 1640, 'restatement', 'the restatement clause, restating the :1573 row',
     'the kernel\'s three routes in the shortest path',
     'the kernel\'s three route terminals in the shortest path', CH, 'counts Route 3 a route'),
    ('R03', 1689, 'restatement', 'the restatement clause, restating the :1653 row (E1-M-13)',
     'The hypothesis is the programme\'s one counted premise (§27.3), open and named — not the discharged Chapter 13 theorem',
     'The hypothesis is RH restated by the kernel\'s own `balance_theorem` (ch_iff_rh, E-2026-09-25-1), open because RH is open — not the discharged Chapter 13 theorem',
     CH, 'restates “the programme`s one counted premise”, which E-2026-09-25-1 corrected at :1657'),
    # ### ------------------------------------------------ the conservation restatements (the rows' reading, the restatement clause)
    ('R04', 647, 'restatement', 'the restatement clause and the ceiling clause, restating the conservation rows',
     'is proved spectrally inert (Chapter 13, verified in Lean)',
     'is argued spectrally inert (Chapter 13; in Lean its terminal states ' + LEANC + ')', CONS, 'restates “verified in Lean” for Conservation'),
    ('R05', 767, 'restatement', 'the restatement clause and the ceiling clause',
     'This is proved by computation (1^s = 1), verified in Lean, and confirmed',
     'This is shown by computation (1^s = 1) — the Lean terminal states ' + LEANC + ' — and confirmed', CONS, 'the s-darkness; its Lean terminal states (1 : ℚ) ^ s = 1'),
    ('R06', 801, 'restatement', 'the fact clause (OPEN_TRAILS :11954) and the restatement clause',
     'The s-darkness theorem has been formally verified in Lean 4 (Chapter 24).',
     'The s-darkness theorem’s Lean terminal, `conservation_of_spectra`, states ' + LEANC + ' (Chapter 25), its conservation reading carried by the name.',
     CONS + '; the Lean kernel is Chapter 25 (v5.15 :1526), not Chapter 24', 'restates “verified in Lean”; the chapter cited is the convergence chapter, the kernel`s is 25'),
    ('R07', 1004, 'restatement', 'the restatement clause',
     '| 1950, Lean-verified |',
     '| 1950; in Lean the terminal states ' + LEANC + ' (T2) |', CONS, 'restates the :1006 row`s “Lean-verified”'),
    ('R08', 2029, 'restatement', 'the restatement clause',
     'Formally verified in Lean 4.',
     'In Lean its terminal states ' + LEANC + ' (T2).', CONS, 'restates the conservation rows` “verified in Lean”'),
    ('R09', 2037, 'restatement', 'the restatement clause',
     'n₄ = 0 from Conservation (Lean-verified)',
     'n₄ = 0 from Conservation (in Lean its terminal states ' + LEANC + ', T2)', CONS, 'restates the :1006 row'),
    # ### ------------------------------------------------ the perpendicular-crossing restatements (E5-05's reading)
    ('R10', 1783, 'restatement', 'the restatement clause, restating E5-05',
     'The perpendicular crossing theorem (Re(ξ\'(1/2+it)) = 0) is formally verified.',
     'The perpendicular crossing theorem is compiled for completedRiemannZeta₀ (spectral_cannon, §25.8); the same fact for ξ′ is not compiled.',
     SC, 'restates the crossing for ξ′ as verified; E5-05 reads it for completedRiemannZeta₀'),
    ('R11', 2065, 'restatement', 'the restatement clause, restating E5-05',
     'Formally verified in Lean 4.',
     'Compiled in Lean 4 for completedRiemannZeta₀ (spectral_cannon, §25.8); the same fact for ξ′ is not compiled.', SC, 'as R10'),
    ('R12', 1564, 'restatement', 'the restatement clause and the ceiling clause, restating E5-05 and E6-01',
     'The perpendicular crossing is proved by path differentiation',
     'The perpendicular crossing is compiled for completedRiemannZeta₀ by path differentiation', SC, 'act one`s line (E5-11): the sentence beside its replacement restates the crossing for ξ'),
    # ### ------------------------------------------------ the finite-range restatement (W15's reading)
    ('R13', 1170, 'restatement', 'the restatement clause, restating the :1810 row',
     'the on-line contribution and the finite range to Voros\'s ≈ 2T² threshold proved, the all-n tail open',
     'the on-line contribution compiled and the finite range to Voros\'s ≈ 2T² threshold certified under two literature premises, T1-lit, the all-n tail open',
     LI, 'restates the finite range as proved'),
    # ### ------------------------------------------------ the χ side: §20.3's label and §20.4 (the ceiling clause, GRH conditional)
    ('X01', 1272, 'ceiling', 'the ceiling clause (the case-insensitive sweep)',
     '**Theorem (GRH).**',
     '**Theorem (GRH), reduced here for each χ to its located clause.**', CHI, 'GRH stated as a theorem; act one`s U04 reduces it'),
    ('X02', 1274, 'ceiling', 'the ceiling clause (the case-insensitive sweep)',
     '*Proof.* The four SIDE conditions',
     '*Argument.* The four SIDE conditions', CHI, 'a proof label for GRH'),
    ('X03', 1274, 'ceiling', 'the ceiling clause (act one`s line, U04)',
     'The brevity of this proof reflects',
     'The brevity of this argument reflects', CHI, 'names the GRH argument a proof'),
    ('X04', 1278, 'ceiling', 'the ceiling clause',
     'No Siegel zeros exist.',
     'Under GRH, no Siegel zeros exist.', CHI, 'states the consequence of GRH unconditionally'),
    ('X05', 1280, 'ceiling', 'the ceiling clause',
     'This resolves a problem that has resisted',
     'Under GRH this resolves a problem that has resisted', CHI, 'claims the problem resolved; it is resolved conditional on GRH'),
    # ### ------------------------------------------------ titles and labels (the case-insensitive sweep of the ceiling pattern)
    ('L01', 82, 'title', 'the ceiling clause (the case-insensitive sweep)', '## The Proof in One Page', '## The Reduction in One Page', H2, 'titles the section a proof of RH'),
    ('L02', 86, 'ceiling', 'the ceiling clause (the case-insensitive sweep)', '**Method.** Proof by exhaustive enumeration', '**Method.** Argument by exhaustive enumeration', H2, 'the method of the reduction named a proof'),
    ('L03', 712, 'title', 'the ceiling clause (the case-insensitive sweep)', '# PART III: THE PROOF', '# PART III: THE REDUCTION', H2, 'titles Part III a proof of RH'),
    ('L04', 1148, 'title', 'the ceiling clause (the case-insensitive sweep)', '## 19.1 The Proof', '## 19.1 The Reduction', H2, 'titles §19.1 a proof of RH'),
    ('L05', 1150, 'ceiling', 'the name-and-title exception (OPEN_TRAILS :11934), then the ceiling clause',
     '**Theorem (Riemann\'s Theorem).**',
     '**Theorem (Riemann\'s Theorem), reduced here to its located clause.**', H2,
     'RH stated as a proved theorem; the name “Riemann`s Theorem”, the monograph`s own title, carries under the exception'),
    ('L06', 1152, 'ceiling', 'the ceiling clause (the case-insensitive sweep)', '*Proof.*', '*The reduction, under the clause of step (9).*', H2, 'a proof label for RH; step (10) states the clause'),
    ('L07', 1174, 'title', 'the ceiling clause (the case-insensitive sweep)', '## 19.2 Proof Architecture', '## 19.2 The Reduction\'s Architecture', H2, 'titles a proof of RH'),
    ('L08', 1198, 'title', 'the ceiling clause (the case-insensitive sweep)', '## 19.3 What the Proof Uses', '## 19.3 What the Reduction Uses', H2, 'titles a proof of RH'),
    ('L09', 1890, 'title', 'the ceiling clause (the case-insensitive sweep)', '## 28.6 The Proof\'s Logical Structure', '## 28.6 The Reduction\'s Logical Structure', H2, 'titles a proof of RH'),
    # ### ------------------------------------------------ the ceiling hits of the 154 (and act one's lines' own), corrected
    ('C003', 35, 'ceiling', 'the ceiling clause', 'The formation count is exhaustive — proved by Ostrowski\'s classification of the places of ℚ (1916).',
     'The formation count is exhaustive at the places — its place count closed by Ostrowski\'s classification of the places of ℚ (1916), its exhaustiveness at ξ the open clause h2.', OST, 'exhaustiveness at ξ is the open premise'),
    ('C004', 37, 'ceiling', 'the ceiling clause', 'it is not load-bearing for the proof of RH.', 'it is not load-bearing for the reduction of RH.', H2, '“the proof of RH”'),
    ('C005', 41, 'ceiling', 'the ceiling clause', 'Every component theorem used in this proof is classical.', 'Every component theorem used in this reduction is classical.', H2, '“this proof”'),
    ('C006', 41, 'ceiling', 'the ceiling clause', 'The barrier to proving the Riemann Hypothesis was not mathematical but methodological: the recognition that proof by exhaustive enumeration',
     'The barrier to reducing the Riemann Hypothesis to one located clause was not mathematical but methodological: the recognition that argument by exhaustive enumeration', H2, 'the barrier to proving RH read as crossed'),
    ('C007', 49, 'ceiling', 'the ceiling clause', 'develop individual components of the proof in standalone form', 'develop individual components of the argument in standalone form', H2, '“the proof”'),
    ('C008', 49, 'ceiling', 'the ceiling clause', 'A one-page proof summary, a proof architecture diagram,', 'A one-page summary of the reduction, an architecture diagram of the argument,', H2, 'the supplements named proofs of RH'),
    ('C009', 62, 'ceiling', 'the ceiling clause', 'The monograph assembles all six into the proof.', 'The monograph assembles all six into the reduction.', H2, '“the proof”'),
    ('C010', 66, 'ceiling', 'the ceiling clause (act one`s line, U02)', 'Part III assembles the proof.', 'Part III assembles the reduction.', H2, '“the proof”'),
    ('C011', 70, 'ceiling', 'the ceiling clause (act one`s line, E5-01)', 'Every step of the proof is verifiable by hand', 'Every step of the reduction is verifiable by hand', H2, '“the proof”'),
    ('C012', 117, 'ceiling', 'the ceiling clause', '**What the proof uses:**', '**What the reduction uses:**', H2, '“the proof”'),
    ('C013', 127, 'ceiling', 'the ceiling clause', '*The proof has one architecture applied through several layers', '*The reduction has one architecture applied through several layers', H2, '“the proof”'),
    ('C014', 165, 'ceiling', 'the ceiling clause', 'This work proves it.', 'This work reduces it to a single located clause, h2_sign, equivalent to RH (h2_sign_iff_rh) and open.', H2, '“This work proves it” (RH)'),
    ('C015', 205, 'ceiling', 'the ceiling clause', 'distinct from the five proof-paths of Chapter 16', 'distinct from the five identification paths of Chapter 16', 'Appendix H`s own name, “Five identification paths” (v5.15 :2229)', 'the paths named proof-paths'),
    ('C016', 245, 'ceiling', 'the ceiling clause', 'a fact proved independently through completely different mathematics', 'a count reached independently through completely different mathematics', OST, 'the formation count`s exhaustiveness named proved'),
    ('C017', 304, 'ceiling', 'the ceiling clause', 'exhibits proved analytical structure at σ = 1/2:', 'exhibits analytical structure at σ = 1/2:', '§4.5`s own list (v5.15 :306-:314): the absence of folds is RH-equivalent', 'names the list proved, the fold criterion among it'),
    ('C018', 316, 'ceiling', 'the ceiling clause', 'These are proved structural properties, not heuristics.',
     'These are structural properties, not heuristics, each with the status its paragraph states (the absence of folds RH-equivalent, checked to 25,000 sample points).', '§4.5 (v5.15 :312)', 'calls the fold criterion`s conclusion proved'),
    ('C019', 358, 'ceiling', 'the ceiling clause', 'This is proved by explicit matrix computation.', 'This is demonstrated by explicit matrix computation (Knill–Laflamme, the formation-block model).', V591, 'the [[7,1,3]] claim the monograph`s own v5.9.1 entry re-scoped'),
    ('C020', 409, 'ceiling', 'the ceiling clause', 'turns this structural landscape into a proof.', 'turns this structural landscape into the reduction of RH to its located clause.', H2, '“into a proof”'),
    ('C021', 415, 'ceiling', 'the ceiling clause', 'not a step in the proof.', 'not a step in the reduction.', H2, '“the proof”'),
    ('C022', 415, 'ceiling', 'the ceiling clause', 'and the RH proof of Part III does not depend on it.', 'and the RH reduction of Part III does not depend on it.', H2, '“the RH proof”'),
    ('C023', 415, 'ceiling', 'the ceiling clause', 'A reader driving toward the proof may', 'A reader driving toward the reduction may', H2, '“the proof”'),
    ('C024', 448, 'ceiling', 'the ceiling clause', 'the proof of RH (Part III) does not depend on it.', 'the reduction of RH (Part III) does not depend on it.', H2, '“the proof of RH”'),
    ('C025', 448, 'ceiling', 'the ceiling clause', 'the oldest proof technique in mathematics', 'the oldest technique of exclusion in mathematics', 'the sentence`s own object, the sieve of Eratosthenes', 'the sieve named the programme`s proof technique'),
    ('C026', 450, 'ceiling', 'the ceiling clause', 'is not the proof — it is the landscape the proof navigates.', 'is not the reduction — it is the landscape the reduction navigates.', H2, '“the proof”'),
    ('C027', 493, 'ceiling', 'the ceiling clause', 'SIDE proves theorems by eliminating', 'SIDE argues by eliminating', H2, 'the method named a prover of theorems'),
    ('C028', 533, 'ceiling', 'the ceiling clause and the fact clause', '(proved within ZFC — Chapter 14)', '(argued within ZFC — Chapter 13)', CONS + '; Conservation of Spectra is Chapter 13 (v5.15 :759)', 'the programme`s theorem named proved; its chapter is 13'),
    ('C029', 562, 'ceiling', 'the ceiling clause', 'prove the enumeration is complete', 'certify the enumeration is complete', OST, '“prove the enumeration complete”'),
    ('C030', 562, 'ceiling', 'the ceiling clause', 'What is new for ξ is the proof that the seven mechanism classes are all the filters there are.',
     'What is new for ξ is the argument that the seven mechanism classes are all the filters there are — their place count closed by Ostrowski, their exhaustiveness at ξ the open clause h2.', OST, 'the catalogue`s exhaustiveness at ξ named proved'),
    ('C031', 619, 'ceiling', 'the ceiling clause', 'The proof requires no novel principle.', 'The reduction requires no novel principle.', H2, '“the proof”'),
    ('C032', 629, 'ceiling', 'the ceiling clause', 'accepts the syllogism accepts the proof.', 'accepts the syllogism accepts the reduction.', H2, '“the proof”'),
    ('C033', 633, 'ceiling', 'the ceiling clause', '"can we prove all zeros are on the line?"', '"can we show all zeros are on the line?"', H2, 'the question framed as a proof'),
    ('C034', 681, 'ceiling', 'the ceiling clause', 'The proof of RH (Parts I–III) does not depend on DCL.', 'The reduction of RH (Parts I–III) does not depend on DCL.', H2, '“The proof of RH”'),
    ('C035', 793, 'ceiling', 'the ceiling clause', 'Conservation proves no external force can exist:', 'Conservation of Spectra argues (Chapter 13) that no external force can exist:', CONS, 'the programme`s theorem named a proof'),
    ('C036', 827, 'ceiling', 'the ceiling clause (act one`s line, E5-04)', 'The proof is four steps —', 'The compiled argument is four steps —', 'silence_universal (SIDE-kernel v1.5, Kernel/SilenceTheorem.lean); E5-04 beside it', 'the Lean argument named a proof'),
    ('C037', 827, 'ceiling', 'the ceiling clause (act one`s line)', 'removing it from the proof leaves an unsolved goal.', 'removing it from the Lean term leaves an unsolved goal.', 'silence_universal (SIDE-kernel v1.5)', 'the Lean term named a proof'),
    ('C038', 827, 'ceiling', 'the ceiling clause (act one`s line)', 'The RH proof uses two specific instances', 'The RH reduction uses two specific instances', H2, '“The RH proof”'),
    ('C039', 829, 'ceiling', 'the ceiling clause', 'Its proof does not — and cannot — reference `s : ℂ`.)', 'Its Lean term does not — and cannot — reference `s : ℂ`.)', 'Mathlib`s mul_add', 'the Lean term named a proof'),
    ('C040', 835, 'ceiling', 'the ceiling clause', 'analytic number theory proves density theorems', 'analytic number theory establishes density theorems', 'the sentence`s own object', '“proves density theorems”'),
    ('C041', 835, 'ceiling', 'the ceiling clause', 'The sieve proves what the interface transmits (density) and cannot prove what it doesn\'t (placement).',
     'The sieve reaches what the interface transmits (density) and cannot reach what it doesn\'t (placement).', 'the sentence`s own object', '“proves” / “cannot prove”'),
    ('C042', 853, 'ceiling', 'the ceiling clause', 'The count n₂ = 3 is proved by the Poisson Exhaustion Theorem (Chapter 16).', 'The count n₂ = 3 is closed by the Poisson Exhaustion Theorem (Chapter 16).', OST, 'the place count: closed (OPEN_TRAILS :12072)'),
    ('C043', 897, 'ceiling', 'the ceiling clause', 'Conservation of Spectra (Chapter 13) proves that no structural force', 'Conservation of Spectra (Chapter 13) argues that no structural force', CONS, 'the programme`s theorem named a proof'),
    ('C044', 929, 'ceiling', 'the ceiling clause', 'Conservation of Spectra (Chapter 13) proves no force beyond these exists.', 'Conservation of Spectra (Chapter 13) argues that no force beyond these exists.', CONS, 'as C043'),
    ('C045', 995, 'ceiling', 'the ceiling clause', '(contradicting Conservation, which is proved)', '(contradicting Conservation, argued in Chapter 13)', CONS, 'the programme`s theorem named proved'),
    ('C046', 1006, 'ceiling', 'the ceiling clause', '| Ring structure, proved |', '| Ring structure (classical); the two-channel reading is this programme’s |', 'the row`s own object, the ring structure of ℤ', 'the programme`s analysis named proved'),
    ('C047', 1170, 'ceiling', 'the ceiling clause', 'the proof carries the identity soundly', 'the reduction carries the identity soundly', H2, '“the proof”'),
    ('C048', 1176, 'ceiling', 'the ceiling clause', 'The proof flows through four levels:', 'The reduction flows through four levels:', H2, '“The proof”'),
    ('C049', 1212, 'ceiling', 'the ceiling clause', 'The proof uses exhaustive enumeration', 'The reduction uses exhaustive enumeration', H2, '“The proof”'),
    ('C050', 1216, 'ceiling', 'the ceiling clause', 'The proof examines seven mechanism classes', 'The reduction examines seven mechanism classes', H2, '“The proof”'),
    ('C051', 1216, 'ceiling', 'the ceiling clause', 'The balance equation alone does not prove RH — the balance equation plus the exhaustive catalogue does.',
     'The balance equation alone does not reach RH — the balance equation plus the exhaustive catalogue does, under the open clause h2 that the catalogue is exhaustive at ξ.', OST, 'the catalogue read as closing RH'),
    ('C052', 1220, 'ceiling', 'the ceiling clause', 'A reader who has followed the proof to this point', 'A reader who has followed the reduction to this point', H2, '“the proof”'),
    ('C053', 1230, 'ceiling', 'the ceiling clause', 'require violating a proved theorem', 'require violating a published theorem', 'the options` own theorems (Ostrowski, Cartan B, Tate)', '“a proved theorem”'),
    ('C054', 1230, 'ceiling', 'the ceiling clause', 'which this proof asserts is correct.', 'which this reduction asserts is correct.', H2, '“this proof”'),
    ('C055', 450, 'ceiling', 'the ceiling clause', 'Parts II–III establish *that* no mechanism exists to place them elsewhere.', 'Parts II–III argue *that* no mechanism exists to place them elsewhere, under the open clause h2 (§27.3).', H2, 'the exclusion read as established'),
    ('C056', 1453, 'ceiling', 'the ceiling clause', 'once RH is established by the syllogism (Part III)', 'once RH is granted under the syllogism’s open premise h2 (Part III)', H2, 'RH read as established'),
    ('C057', 1453, 'ceiling', 'the ceiling clause', 'The computational evidence confirms what the proof predicts.', 'The computational evidence confirms what the reduction predicts.', H2, '“the proof”'),
    ('C058', 1528, 'ceiling', 'the ceiling clause', 'The logical form is not the proof status;', 'The logical form is not the compiled status;', 'Chapter 25`s own concordance (§25.8)', 'the status named a proof status'),
    ('C059', 1532, 'ceiling', 'the ceiling clause', 'a Lean 4 formalization of the proof\'s logical architecture.', 'a Lean 4 formalization of the reduction\'s logical architecture.', H2, '“the proof`s”'),
    ('C060', 1532, 'ceiling', 'the ceiling clause', 'The core proof modules —', 'The core kernel modules —', '§25.8', 'the modules named proof modules'),
    ('C061', 1536, 'ceiling', 'the ceiling clause', '`cartan_B_consequence` proved as `True` by `trivial`', '`cartan_B_consequence` closed as `True` by `trivial`', 'the sentence`s own object', 'a vacuous Lean term named a proof'),
    ('C062', 1542, 'ceiling', 'the ceiling clause (act one`s line, E5-08)', 'This is the proof\'s structure,', 'This is the reduction\'s structure,', H2, '“the proof`s structure”'),
    ('C063', 1550, 'ceiling', 'the ceiling clause', 'Each proves that its class identifies σ = 1/2:', "Each compiles algebra showing that its class's stated constraint forces σ = 1/2:", E611, 'the Voices` content, as E6-11 reads it'),
    ('C064', 1575, 'ceiling', 'the ceiling clause', 'the mathematical proof in the manuscripts,', 'the mathematical argument in the manuscripts,', 'the sentence`s own object', '“the mathematical proof”'),
    ('C065', 1577, 'ceiling', 'the ceiling clause', 'The convergence is the proof.', 'The convergence is the argument, under the named premise h2, open (h2_sign_iff_rh).', H2, '“The convergence is the proof”'),
    ('C066', 1587, 'ceiling', 'the ceiling clause', 'the conjunction of three proved components:', 'the conjunction of three compiled components:', 'structural_exhaustiveness_proved (§25.8)', 'compiled components named proved'),
    ('C067', 1593, 'ceiling', 'the ceiling clause', 'The conjunction is proved unconditionally as', 'The conjunction is compiled unconditionally as', 'structural_exhaustiveness_proved (§25.8)', 'a compiled theorem named proved'),
    ('C068', 1603, 'ceiling', 'the ceiling clause (act one`s line, E1-M-09)', 'the s-darkness of the product formula, proved within ZFC from Tate\'s thesis', 'the s-darkness of the product formula, argued within ZFC from Tate\'s thesis', CONS, 'the programme`s theorem named proved'),
    ('C069', 1603, 'ceiling', 'the ceiling clause (act one`s line)', 'The bridge then proves:', 'The bridge then compiles:', 'ConservationBridge.riemann_hypothesis (§25.8)', 'a compiled implication named a proof'),
    ('C070', 1633, 'ceiling', 'the ceiling clause', '| Route 1 — structural exhaustiveness proved |', '| Route 1 — structural exhaustiveness, compiled |', 'structural_exhaustiveness_proved (§25.8)', 'a compiled theorem named proved'),
    ('C071', 1645, 'ceiling', 'the ceiling clause', 'The structural exhaustiveness theorem proved unconditionally.', 'The structural exhaustiveness theorem compiled unconditionally.', 'structural_exhaustiveness_proved (§25.8)', 'as C070'),
    ('C072', 1655, 'ceiling', 'the ceiling clause', 'are not required for the Day 1 proof.', 'are not required for the Day 1 reduction.', H2, '“the Day 1 proof”'),
    ('C073', 1693, 'ceiling', 'the ceiling clause', 'neither imported by any proof path', 'neither imported by any compiled module', 'the sentence`s own object', 'an import path named a proof path'),
    ('C074', 1706, 'ceiling', 'the ceiling clause', 'whose proof had not yet been found.', 'whose derivation had not yet been found.', 'the sentence`s own object', '“whose proof”'),
    ('C075', 1712, 'ceiling', 'the ceiling clause (act one`s line, E6-01)', 'Every theorem is proved from Lean 4\'s core plus Mathlib.', 'Every theorem is compiled from Lean 4\'s core plus Mathlib.', '§25.8', 'compiled theorems named proved'),
    ('C076', 1712, 'ceiling', 'the ceiling clause (act one`s line)', 'formalization reveals what needs to be proved, and then mathematics proves it.', 'formalization reveals what needs to be shown, and then mathematics shows it.', 'the sentence`s own object', 'a general maxim on proof'),
    ('C077', 1749, 'ceiling', 'the ceiling clause', 'multiple proof strategies,', 'multiple strategies of argument,', H2, '“proof strategies”'),
    ('C078', 1757, 'ceiling', 'the ceiling clause', 'it moved the proof\'s novel content', 'it moved the argument\'s novel content', H2, '“the proof`s”'),
    ('C079', 1759, 'ceiling', 'the ceiling clause', 'Early versions implied the proof required principles beyond ZFC.', 'Early versions implied the argument required principles beyond ZFC.', H2, '“the proof”'),
    ('C080', 1759, 'ceiling', 'the ceiling clause', 'The proof operates entirely within ZFC.', 'The argument operates entirely within ZFC.', H2, '“The proof”'),
    ('C081', 1767, 'ceiling', 'the ceiling clause', 'Thom transversality removed from the proof\'s logical spine', 'Thom transversality removed from the argument\'s logical spine', H2, '“the proof`s”'),
    ('C082', 1767, 'ceiling', 'the ceiling clause', 'the proof establishes RH, from which simplicity follows as a consequence, not as an equivalence.',
     'the argument reduces RH to its located clause, and simplicity is a separate located clause (simplicity_iff, v0.17), not carried by positivity within the schema (positivity_not_imp_simplicity, v0.19), and not an equivalent of RH.',
     H2 + '; ' + SIMP, 'RH read as established and simplicity as its consequence; the kernel carries simplicity as a second located clause'),
    ('C083', 1769, 'ceiling', 'the ceiling clause', 'eliminated Thom transversality from the proof\'s logical spine', 'eliminated Thom transversality from the argument\'s logical spine', H2, '“the proof`s”'),
    ('C084', 1771, 'ceiling', 'the ceiling clause', 'retraction to what can actually be proved.', 'retraction to what can actually be shown.', 'the sentence`s own object', 'a general statement'),
    ('C085', 1779, 'ceiling', 'the ceiling clause', 'formalized as a ZFC proof method,', 'formalized as a ZFC method of argument,', 'the sentence`s own object', '“proof method”'),
    ('C086', 1781, 'ceiling', 'the ceiling clause', 'The product formula is spectrally silent — proved within ZFC from Tate\'s thesis.', 'The product formula is spectrally silent — argued within ZFC from Tate\'s thesis (Chapter 13).', CONS, 'the programme`s theorem named proved'),
    ('C087', 1789, 'ceiling', 'the ceiling clause', 'If the RH proof is rejected,', 'If the RH reduction is rejected,', H2, '“the RH proof”'),
    ('C088', 1789, 'restatement', 'the restatement clause, restating E5-05', 'The perpendicular crossing remains formally verified.', 'The perpendicular crossing remains compiled for completedRiemannZeta₀ (spectral_cannon).', SC, 'restates the crossing as verified for ξ′'),
    ('C089', 1789, 'ceiling', 'the ceiling clause', 'a named and formalized proof template', 'a named and formalized template of argument', 'the sentence`s own object', '“proof template”'),
    ('C090', 1837, 'restatement', 'the restatement clause, restating J06', 'Part IV establishes one result and reduces a second.', 'Part IV argues one direction and reduces a second.', J + '; ' + SIMP, 'the conditional named an established result'),
    ('C091', 1837, 'ceiling', 'the restatement clause, restating J06', 'perpendicular crossing, monotonicity, fold exclusion; proved.', 'perpendicular crossing, monotonicity, fold exclusion; an open direction, no compiled statement carrying it (simplicity_iff, v0.17).', J + '; ' + SIMP, 'the conditional named proved'),
    ('C092', 1839, 'ceiling', 'the ceiling clause', '— not a second proof, and not a reduction', '— not a second argument closing RH, and not a reduction', H2, '“a second proof”'),
    ('C093', 1855, 'ceiling', 'the ceiling clause', 'A ten-step convergence proof is developed', 'A ten-step convergence argument is developed', 'the sentence`s own object', '“convergence proof”'),
    ('C094', 1873, 'ceiling', 'the ceiling clause', 'with independence proof and the Ostrowski parallel table.', 'with the independence argument and the Ostrowski parallel table.', 'the sentence`s own object', '“independence proof”'),
    ('C095', 1884, 'ceiling', 'the ceiling clause', 'it is an interface, proved spectrally inert (n₄ = 0).', 'it is an interface, spectrally inert by the n₄ = 0 count (Chapter 14).', 'Chapter 14 (v5.15 :829)', 'the programme`s claim named proved'),
    ('C096', 1892, 'ceiling', 'the ceiling clause', 'The proof is a syllogism (§10.4): all properties trace to the specification (Determination); the mechanism catalogue is exhaustive (Ostrowski); no catalogued mechanism produces off-line zeros (per-class exclusion); therefore no off-line zeros exist.',
     'The reduction is a syllogism (§10.4): all properties trace to the specification (Determination); the mechanism catalogue is exhaustive (its place count closed by Ostrowski, its exhaustiveness at ξ the open clause h2); no catalogued mechanism produces off-line zeros (per-class exclusion); therefore, under that clause, no off-line zeros exist.',
     OST, 'the syllogism named a proof; its exhaustiveness premise is the open clause'),
    ('C097', 1894, 'ceiling', 'the ceiling clause', 'But the proof\'s logical spine is the syllogism', 'But the reduction\'s logical spine is the syllogism', H2, '“the proof`s”'),
    ('C098', 1894, 'ceiling', 'the ceiling clause', 'The proof asks nothing of the reader', 'The reduction asks nothing of the reader', H2, '“The proof”'),
    ('C099', 1908, 'ceiling', 'the ceiling clause', 'proved exhaustive by Ostrowski\'s classification of the places of ℚ.', 'its place count closed by Ostrowski\'s classification of the places of ℚ, its exhaustiveness at ξ the open clause h2.', OST, 'exhaustiveness at ξ named proved'),
    ('C100', 1912, 'ceiling', 'the ceiling clause', 'The proof method — enumerate', 'The method — enumerate', H2, '“The proof method”'),
    ('C101', 1912, 'ceiling', 'the ceiling clause', 'elevated from computation to proof.', 'elevated from computation to argument.', H2, '“to proof”'),
    ('C102', 1912, 'ceiling', 'the ceiling clause', 'What is new is the proof that the enumeration is complete.', 'What is new is the argument that the enumeration is complete — its place count closed, its exhaustiveness at ξ the open clause h2.', OST, 'the catalogue`s completeness named proved'),
    ('C103', 1922, 'ceiling', 'the ceiling clause', 'Every component theorem of the proof predates this programme.', 'Every component theorem of the reduction predates this programme.', H2, '“the proof”'),
    ('C104', 1922, 'ceiling', 'the ceiling clause', 'placed in the right relation, close the question.', 'placed in the right relation, reduce the question to one located clause.', H2, 'the question read as closed'),
    ('C105', 1965, 'ceiling', 'the ceiling clause', 'Both systems are proved in this monograph', 'Both systems\' formation counts are derived in this monograph', 'Appendix B`s own table (v5.15 :1960-:1963)', 'the systems named proved'),
    ('C106', 1993, 'ceiling', 'the ceiling clause', 'Every theorem in the proof is visible', 'Every theorem in the reduction is visible', H2, '“the proof”'),
    ('C107', 2063, 'ceiling', 'the ceiling clause', 'the proof\'s conclusion holds regardless', 'the reduction\'s conclusion holds regardless', H2, '“the proof`s”'),
    ('C108', 2173, 'ceiling', 'the ceiling clause', 'Mathematical content, proof strategies, and editorial decisions', 'Mathematical content, strategies of argument, and editorial decisions', 'the sentence`s own object', '“proof strategies”'),
    ('C109', 2224, 'ceiling', 'the ceiling clause (Appendix H, relocated text, live)', 'The proof has one architecture, applied through multiple layers.', 'The reduction has one architecture, applied through multiple layers.', H2, '“The proof”'),
    ('C110', 2227, 'ceiling', 'the ceiling clause (Appendix H)', 'The proof has one architecture, applied through multiple layers.', 'The reduction has one architecture, applied through multiple layers.', H2, '“The proof”'),
    ('C111', 2228, 'ceiling', 'the ceiling clause (Appendix H)', 'This is the proof\'s foundation', 'This is the reduction\'s foundation', H2, '“the proof`s”'),
    ('C112', 2231, 'ceiling', 'the ceiling clause (Appendix H)', '**Two proof strategies** (Part III and Part IV). Part III assembles the proof through direct per-class exclusion. Part IV arrives at the same conclusion through the structural behavior of zeros: simplicity of all zeros implies the Riemann Hypothesis.',
     '**Two strategies** (Part III and Part IV). Part III assembles the reduction through direct per-class exclusion. Part IV argues toward the same conclusion through the structural behavior of zeros: that simplicity of all zeros implies the Riemann Hypothesis is an open direction (§22.5).',
     H2 + '; ' + SIMP, 'two proofs of RH; the second is an open direction (J06)'),
    ('C113', 2234, 'ceiling', 'the ceiling clause (Appendix H)', 'are one proof with structural redundancy', 'are one argument with structural redundancy', H2, '“one proof”'),
    ('C114', 2235, 'ceiling', 'the ceiling clause (Appendix H)', 'this monograph proves the theorem and presents the method.', 'this monograph reduces the theorem to its located clause and presents the method.', H2, '“proves the theorem”'),
]

# ================================================================================ §25.8: THE KERNEL CONCORDANCE, RE-PINNED ENTRY BY ENTRY
# ### (v5.15 line, the theorem as the row names it, its module, its line at v1.3 = 0bc21c0, at v1.5 = 0e5233f, the terminal table's name)
CONCORDANCE = [
    (1671, 'structural_exhaustiveness_proved', 'Bridge/TheBridgeComplete.lean', 188, 249, 'structural_exhaustiveness_proved'),
    (1672, 'SpectralCannonFull.spectral_cannon', 'Kernel/SpectralCannonFull.lean', 58, 65, 'SpectralCannonFull.spectral_cannon'),
    (1673, 'ConservationBridge.riemann_hypothesis', 'Bridge/ConservationBridge.lean', 53, 53, 'ConservationBridge.riemann_hypothesis'),
    (1674, 'techne_kernel_integration.rh_from_structural_exhaustiveness', 'Kernel/Integration.lean', 210, 221, 'techne_kernel_integration.rh_from_structural_exhaustiveness'),
    (1675, 'techne_kernel_integration.structural_exhaustiveness_iff_rh', 'Kernel/Integration.lean', 241, 252, 'techne_kernel_integration.structural_exhaustiveness_iff_rh'),
    (1676, 'SIDEKernel.formation', 'Kernel/Core.lean', 53, 53, 'SIDEKernel.formation'),
    (1677, 'techne_kernel_cross_exclusion.all_pairs_excluded', 'Bridge/CrossClassExclusion.lean', 80, 80, 'techne_kernel_cross_exclusion.all_pairs_excluded'),
]
OLD_PIN, NEW_PIN, HEAD_PIN = 'v1.3 = 0bc21c0', 'v1.5 = 0e5233f', '0256e9e'
LIVE_ROW = (1683, 'SIDE-global-section v0.1.0 = 706a81b', 'the dated live-layer row of 2026-08-20, carried by the history clause; the table '
                                                          'reads SIDE-global-section at HEAD 3528bcf unpinned; v0.1.0 resolves (peeled 706a81b)')


def _pin_cell(old_l, new_l):
    return ' %s, :%d (from %s, :%d); at HEAD %s; not a page node |' % (NEW_PIN, new_l, OLD_PIN, old_l, HEAD_PIN)


REPIN = [('K00', 1669, 'repin', '(R218)(4): §25.8 re-pinned entry by entry against the pages and the terminal table',
          '| Claim | Theorem | Module | `#print axioms` |', '| Claim | Theorem | Module | `#print axioms` | Pin (relay terminal table) |',
          'relay data/terminal_table.json at HEAD (pin v1.5 = 0e5233f, the deposited wave)', 'the column`s head'),
         ('K01', 1670, 'repin', '(R218)(4)', '|---|---|---|---|', '|---|---|---|---|---|', 'relay data/terminal_table.json', 'the alignment cell')]
for _i, (_n, _thm, _mod, _a, _b, _tt) in enumerate(CONCORDANCE, 2):
    REPIN.append(('K%02d' % _i, _n, 'repin', '(R218)(4)', '| propext, Classical.choice, Quot.sound |' if _n != 1676 else '| (none) |',
                  ('| propext, Classical.choice, Quot.sound |' if _n != 1676 else '| (none) |') + _pin_cell(_a, _b),
                  'SIDE-kernel %s:%d (git grep at v1.3 and v1.5); relay data/terminal_table.json row %s' % (_mod, _b, _tt),
                  'the pin moved from %s to %s%s' % (OLD_PIN, NEW_PIN, '' if _a == _b else ', the line from :%d to :%d' % (_a, _b))))
CHANGES += REPIN

# ================================================================================ THE HISTORY LINES (the history clause), each beneath its line
HIST = {
    1399: ('*v5.16, 2026-10-03, a history line under the sentence above, under `(R218)`(3): the fold criterion of §22.4 runs from a fold to '
           'an off-line zero, while the link above reads the converse, from the absence of folds to the absence of off-line zeros — that '
           'converse is the open direction and no compiled statement carries it; what is compiled on this chain is the perpendicular '
           'crossing, for completedRiemannZeta₀ (spectral_cannon, §25.8).*'),
    2243: ('*v5.16, 2026-10-03, a history line under the paragraph above, the dated Correspondence of 2026-08-12 carried as its record: the '
           'route the kernels check to RH composes under `ConservationHypothesis`, which the kernel’s own `balance_theorem` shows is RH '
           'restated (ch_iff_rh, E-2026-09-25-1); the compiled reduction of RH to its located clause is h2_sign_iff_rh '
           '(SIDE-explicit-formula v0.2): Weil positivity on classK, h2_sign, is equivalent to RH, both directions compiled, and stays open.*'),
    2245: ('*v5.16, 2026-10-03, a history line under the register above, the README’s sentence (README :106) quoted verbatim and carried: '
           'the README carries beside it the rewordings of `(R145)`(2) and `(R146)`(2) (README :113, :115) -- the sentence is supportable '
           'only with the clause named as h2_sign, Weil positivity on classK equivalent to RH with both directions compiled '
           '(h2_sign_iff_rh, SIDE-explicit-formula v0.2), and “reduction machine-verified” is not said of Route 3, whose clause is RH '
           'restated (E-2026-09-25-1).*'),
    2259: ('*v5.16, 2026-10-03, a history line under the table above, the dated Correspondence of 2026-08-12 carried as its record: its '
           'Route 3 row is the implication from `ConservationHypothesis`, which the kernel’s own `balance_theorem` shows is RH restated '
           '(ch_iff_rh, E-2026-09-25-1), so the row formalizes RH from RH restated; and `h2` has a compiled face, h2_sign, equivalent to '
           'RH with both directions compiled (h2_sign_iff_rh, SIDE-explicit-formula v0.2, ζ page node 8), which no kernel discharges.*'),
}
HIST_CITE = {
    1399: SC + ' (what is compiled); nothing for the converse (R218)(3)',
    2243: CH + '; ' + H2,
    2245: 'README :106, :113, :115; ' + H2 + '; ' + CH,
    2259: CH + '; ' + H2,
}

# ================================================================================ THE CARRIED CEILING HITS, EACH UNDER A NAMED EXCEPTION
# ### (v5.15 line, a fragment holding the hit, the exception, its reason)
QS, NT, DE = 'a quoted source', 'the name-and-title exception', 'a dated entry under the history clause'
CARRIES = [
    (41, 'Størmer proved his theorem on consecutive smooth numbers in 1897.', QS, 'Størmer (1897), a published theorem attributed'),
    (70, 'not a second, redundant proof.', QS, 'ERRATA E-2026-09-25-5, E5-01`s replacement text verbatim (act one), the ledger quoted'),
    (102, '| 1916, proved |', QS, 'Ostrowski`s theorem (1916), a published theorem'),
    (103, '| 1876/1951, proved |', QS, 'Cartan B (1876/1951), a published theorem'),
    (226, 'Carl Størmer proved in 1897', QS, 'Størmer (1897)'),
    (237, 'The proof uses Pell equations', QS, 'Størmer`s published proof (1897)'),
    (531, 'proved by Artin and Whaples (1945)', QS, 'Artin and Whaples (1945)'),
    (586, 'proved by Riemann, made rigorous by Hecke and Tate', QS, 'Riemann (1859), Hecke, Tate (1950)'),
    (619, 'the same one Euclid used to prove', QS, 'Euclid, a published proof'),
    (673, 'Gödel (1940) proved CH consistent with ZFC.', QS, 'Gödel (1940)'),
    (673, 'Cohen (1963) proved ¬CH consistent with ZFC.', QS, 'Cohen (1963)'),
    (771, 'proved unconditionally by Artin and Whaples (1945)', QS, 'Artin and Whaples (1945)'),
    (799, 'proved by Artin and Whaples (1945)', QS, 'Artin and Whaples (1945)'),
    (909, 'This is proved in Selberg (1956)', QS, 'Selberg (1956), with Iwaniec cited'),
    (917, 'proved by integration by parts (Green\'s identity)', QS, 'Green`s identity, a classical source named'),
    (955, 'Ostrowski proved that no such place exists.', QS, 'Ostrowski (1916)'),
    (995, '(Ostrowski proves none exists)', QS, 'Ostrowski (1916)'),
    (995, '(Cartan B proves none exists)', QS, 'Cartan B (1876/1951)'),
    (1003, '| 1916, proved |', QS, 'Ostrowski`s theorem (1916)'),
    (1005, '| 1876/1951, proved |', QS, 'elliptic regularity, the Identity Theorem and Cartan B (1876/1951)'),
    (1131, 'Ostrowski proved does not exist', QS, 'Ostrowski (1916)'),
    (1296, 'If one proves the equality', QS, 'Emmy Noether, a quotation verbatim'),
    (1313, '40.77% proved (Conrey 1989)', QS, 'Conrey (1989); act two read the figure with §24.4`s note (L01)'),
    (1313, 'proved for function fields (Weil-Deligne)', QS, 'Weil, Deligne, a published theorem over function fields'),
    (1469, 'Conrey (1989) proved that at least 40.77%', QS, 'Conrey (1989)'),
    (1521, 'I have only proved it correct, not tested it.', QS, 'Knuth, a quotation verbatim'),
    (1528, 'Wiles\'s FLT proof', QS, 'Wiles (1995), a published proof'),
    (1528, 'Hales\'s Kepler proof', QS, 'Hales (2005), a published proof'),
    (1564, '`Kernel/PerpendicularCrossing.lean` proves that', QS, 'ERRATA E-2026-09-25-5, E5-11`s replacement text verbatim (act one)'),
    (1575, 'Wiles proved modularity lifting', QS, 'Wiles (1995)'),
    (1575, 'Ribet proved the earlier semistable-curve correspondence', QS, 'Ribet (1990)'),
    (1575, 'Hales presented the Kepler proof in a manuscript', QS, 'Hales (2005)'),
    (1575, 'verified the proof\'s components in HOL Light', QS, 'the Flyspeck project, of Hales`s published proof'),
    (1894, 'check Ostrowski (proved, 1916)', QS, 'Ostrowski (1916)'),
    (2061, 'used in Conrey\'s proof that at least 40.77%', QS, 'Conrey (1989)'),
    (2133, 'A proof of the Kepler conjecture.', NT, 'a bibliography title (Hales 2005)'),
    (1683, '(stated, not proved, not claimed)', DE, 'the live-layer concordance row of 2026-08-20 (v5.15 :1679), a dated addition'),
    (1693, '**What it proves (label correction, 2026-07-21).**', DE, 'the label correction of 2026-07-21'),
    (2193, 'verifies the proof end-to-end', DE, 'the version-history entry v5.9.1 (2026-07-23), its quotation of a retired framing'),
    (2193, 'the [[7,1,3]] "proved" claims', DE, 'the entry v5.9.1 (2026-07-23)'),
    (2195, 'so the proof\'s spine', DE, 'the entry v5.10 (2026-07-24)'),
    (2197, 'is now proved', DE, 'the entry v5.10.1 (2026-07-24)'),
    (2199, 'the one-page-proof step (8)', DE, 'the entry v5.10.2 (2026-07-24)'),
    (2203, '"proved by the same logic as RH" / "a second proof"', DE, 'the entry v5.12 (2026-07-26), quoting the text it corrected'),
    (2203, 'none as proof', DE, 'the entry v5.12 (2026-07-26)'),
    (2203, '**Part III\'s single-premise proof of RH is unchanged**', DE, 'the entry v5.12 (2026-07-26)'),
]

# ### the carries of the earlier acts that stand in the body, each with its act's own reason (ratified at (R218)(1) and (R217)(1))
PRIOR_CARRIES = [
    (1566, 'and proves:', 'act one`s U09, accepted at (R217)(1): its “proves” governs the compiled reduction printed beneath'),
]

# ================================================================================ THE b558 WORK-LIST'S 31 ROWS, EACH WITH ITS LANDING
# ### (row, v5.13 line, terminal, v5.15 line, landing, a needle the v5.15 line must hold)
ROWS = [
    (1, 103, 'conservation_of_spectra', 105, 'rewritten: W01', None),
    (2, 117, 'h2_sign', 119, 'landed at act one: E5-02', 'equivalent to RH (h2_sign_iff_rh'),
    (3, 1006, 'conservation_of_spectra', 1008, 'rewritten: W03', None),
    (4, 1204, 'conservation_of_spectra', 1206, 'rewritten: W04', None),
    (5, 1573, 'ch_iff_rh', 1577, 'rewritten: W05', None),
    (6, 1599, 'ch_iff_rh', 1603, 'landed at act one: E1-M-09', 'so the proposition is RH restated'),
    (7, 1630, 'ch_iff_rh', 1634, 'rewritten: W07', None),
    (8, 1653, 'ch_iff_rh', 1657, 'landed at act one: E1-M-13', 'is RH restated by the kernel\'s own `balance_theorem`'),
    (9, 1653, 'ch_iff_rh', 1657, 'landed at act one: E1-M-14', 'a chain from RH restated to RH'),
    (10, 1669, 'ch_iff_rh', 1673, 'rewritten: W10', None),
    (11, 1669, 'riemann_hypothesis', 1673, 'rewritten: W10', None),
    (12, 1708, 'ch_iff_rh', 1712, 'landed at act one: E1-M-18', 'shows is RH restated (E-2026-09-25-1)'),
    (13, 1793, 'ch_iff_rh', 1797, 'landed at act one: E1-M-20, E1-M-22, E6-02', 'RH restated (E-2026-09-25-1)'),
    (14, 1808, 'h2_sign', 1816, 'landed at act one: E4-02, E4-03, E6-05', 'mellin_Phi_eq_zero_of_re_le_one'),
    (15, 1810, 'partialPositivity_finiteRange', 1818, 'rewritten: W15', None),
    (16, 1823, 'ch_iff_rh', 1831, 'landed at act one: E1-M-23', 'three route terminals'),
    (17, 1823, 'ch_iff_rh', 1831, 'landed at act one: E1-M-24', 'shows is RH restated (E-2026-09-25-1), not its discharge'),
    (18, 1823, 'riemann_hypothesis', 1831, 'landed at act one: E1-M-23', '— RH restated (E-2026-09-25-1) — to `RiemannHypothesis`'),
    (19, 1855, 'conservation_of_spectra', 1863, 'rewritten: W19', None),
    (20, 1934, 'conservation_of_spectra', 1942, 'rewritten: W20', None),
    (21, 2224, 'ch_iff_rh', 2232, 'landed at act one: E1-M-02, E6-09', 'Route 3\'s conclusion is its premise restated (ch_iff_rh)'),
    (22, 2224, 'conservation_of_spectra', 2232, 'landed at act one: E1-M-02, E6-09', 'Route 3, the compiled implication'),
    (23, 2224, 'riemann_hypothesis', 2232, 'landed at act one: E1-M-02, E6-09', 'three route terminals'),
    (24, 2225, 'ch_iff_rh', 2233, 'landed at act one: E1-M-04, E6-10', 'the second is RH restated (ch_iff_rh)'),
    (25, 2225, 'silence_universal', 2233, 'landed at act one: E1-M-04, E6-10', 'the first is false as stated (not_register1)'),
    (26, 2233, 'ch_iff_rh', 2241, 'landed at act one: E6-11, E6-12, E6-13', 'yields RH from a premise that is RH restated (ch_iff_rh)'),
    (27, 2235, 'h2_sign', 2243, 'history line beneath :2243 (the dated Correspondence, the history clause)', None),
    (28, 2237, 'h2_sign', 2245, 'history line beneath :2245 (README :106 quoted verbatim; the history clause)', None),
    (29, 2243, 'ch_iff_rh', 2251, 'history line beneath the table, :2259 (the dated Correspondence)', None),
    (30, 2243, 'riemann_hypothesis', 2251, 'history line beneath the table, :2259', None),
    (31, 2250, 'h2_sign', 2258, 'history line beneath the table, :2259', None),
]

# ### Part IV's preamble lines (R218)(4) names, and chapter 24's opening and title
PREAMBLE = [1305, 1307, 1309, 1311]
CH24 = [1463, 1465]
STEM_LINE = 722
S224 = 1399


def resolve():
    """### every change`s old wording once on its v5.15 line; every carry`s fragment on its line; every row`s needle; returns (M, rows, bad)."""
    M = lines_of(show(PRE_PP, CUR))
    rows, bad = [], []
    for c in CHANGES:
        cid, n, kind, clause, old, new, cites, why = c
        k = M[n - 1].count(old)
        rows.append(dict(id=cid, line=n, kind=kind, clause=clause, old=old, new=new, cites=cites, why=why, count=k))
        if k != 1 or n >= CORR_LINE:
            bad.append((cid, n, k))
    seen = {}
    for c in rows:
        seen.setdefault(c['line'], []).append(c)
    for n, cs in seen.items():
        spans = sorted((M[n - 1].index(c['old']), M[n - 1].index(c['old']) + len(c['old']), c['id']) for c in cs)
        for a, b in zip(spans, spans[1:]):
            if a[1] > b[0]:
                bad.append(('overlap', n, a[2], b[2]))
    for n, frag, exc, why in CARRIES + [(n, f, 'prior', w) for n, f, w in PRIOR_CARRIES]:
        if M[n - 1].count(frag) != 1:
            bad.append(('carry', n, frag[:40], M[n - 1].count(frag)))
    for r in ROWS:
        if r[5] and r[5] not in M[r[3] - 1]:
            bad.append(('row', r[0], r[3], r[5][:40]))
    for n in HIST:
        if not M[n - 1].strip() or (n < CORR_LINE and n != S224):
            bad.append(('hist', n))
    return M, rows, bad


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    M, rows, bad = resolve()
    print('changes %d (ids unique %s) ; carries %d ; rows %d ; history lines %d' % (
        len(rows), len(set(r['id'] for r in rows)) == len(rows), len(CARRIES), len(ROWS), len(HIST)))
    print('problems:', bad or 'NONE')
