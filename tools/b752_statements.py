# -*- coding: utf-8 -*-
"""tools/b752_statements.py -- (R362)(5): THE STATEMENTS, each declaration printed whole from its kernel's git tree at the named commit and
graded from its statement (DERIVES ; INTERFACES ; ENCODES-CONCLUSION/SHELL), with the amendment's sources (row 1) read before the grading.
Spans are printed by `git show <rev>:<path>` and `git grep` in the local clones (reads only; no fetch, no remote, no lake or lean process);
the grade lines are the seat's, held in GRADES below, each naming the lines it reads.

  python -X utf8 -u tools/b752_statements.py            print every span and every grade (dry)
  python -X utf8 -u tools/b752_statements.py --bank     data/b752_statements.txt, written once, LF
Written at b752 by the Write tool; no identifier of the author in any string here.
"""
import io
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
BANK = os.path.join(RELAY, 'data', 'b752_statements.txt')
NL = '\n'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
K, EF = 'D:/SIDE-kernel', 'D:/SIDE-explicit-formula'
ML = 'D:/SIDE-kernel/.lake/packages/mathlib'


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# (part, repo, rev, path, lo, hi)
SPANS = [
    ('i', K, 'v1.5', 'Bridge/TheBridgeComplete.lean', 1, 60),
    ('i', K, 'v1.5', 'Bridge/TheBridgeComplete.lean', 150, 262),
    ('i', K, 'v1.5', 'Kernel/Layer1.lean', 1, 40),
    ('i', K, 'v1.5', 'Bridge/SIDEBridge.lean', 1, 60),
    ('i', K, 'v1.5', 'Bridge/CrossClassExclusion.lean', 40, 90),
    ('i', K, 'v1.5', 'MetaKernel.lean', 55, 100),
    ('i', K, 'v1.5', 'MetaKernel.lean', 150, 165),
    ('ii', EF, 'v0.38', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 1, 90),
    ('ii', EF, 'v0.38', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 1, 120),
    ('ii', EF, 'v0.38', 'SIDEExplicitFormula/Schema/Config.lean', 1, 60),
    ('ii', EF, 'v0.38', 'SIDEExplicitFormula/B321Identity.lean', 1, 40),
    ('ii', EF, 'v0.38', 'Zeta23/WeilEF/VerticalLine.lean', 98, 115),
    ('i', 'D:/SIDE-lv-conservation', '2f71068', 'SIDELvConservation/T3_StepNineBridge.lean', 1, 110),
    ('census', K, 'v1.5', 'Bridge/TheBridgeComplete.lean', 60, 149),
    ('census', K, 'v1.5', 'Kernel/ThomBridge.lean', 37, 45),
    ('census', K, 'v1.5', 'Bridge/ConservationBridge.lean', 26, 56),
    ('dh', K, 'v1.8', 'Kernel/Cascade/SieveCeilingSemantic.lean', 50, 80),
    ('dh', K, 'v1.8', 'Kernel/Cascade/SieveCeilingWitness.lean', 40, 103),
    ('iii', ML, 'e960b841', 'Mathlib/NumberTheory/ArithmeticFunction/VonMangoldt.lean', 76, 84),
    ('iii', ML, 'e960b841', 'Mathlib/NumberTheory/LSeries/Nonvanishing.lean', 1, 40),
    ('iii', ML, 'e960b841', 'Mathlib/NumberTheory/LSeries/Nonvanishing.lean', 215, 315),
    ('iii', ML, 'e960b841', 'Mathlib/NumberTheory/LSeries/Nonvanishing.lean', 380, 420),
    ('iii', ML, 'e960b841', 'Mathlib/NumberTheory/LSeries/Dirichlet.lean', 322, 330),
]
GREPS = [
    ('i', K, 'v1.5', r'MechanismClass|seven_classes|PerClass|ClassExcludes'),
    ('ii', EF, 'v0.38', r'def cQ|def rQ|vonMangoldt|ArithmeticFunction\.Λ'),
]
GRADES = [
    '### THE SEAT`S GRADES, FROM EACH STATEMENT AS PRINTED ABOVE; the grade words are (R362)(5)`s: DERIVES ; INTERFACES ; ENCODES-CONCLUSION/SHELL. A definition is described,'
    ' not graded. Each row names the lines it reads.',
    '',
    '## (i) SIDE-kernel v1.5 (0e5233f0): WHAT A CLASS IS',
    '  MechanismClass, Bridge/TheBridgeComplete.lean :20-:23 -- a DEFINITION: an inductive of seven constructors carrying no data (no argument, no field); DecidableEq, Fintype.',
    '  seven_classes :25 -- DERIVES what it states, Fintype.card MechanismClass = 7, by decide: a COUNT of constructors.',
    '  produces_offline :157-:165 -- a DEFINITION by cases on the class; each case a Prop about a real sigma alone (C1-C5 an equation in sigma with sigma != 1/2; C6'
    ' zero_codimension sigma = 1; C7 hadamard_contrib sigma != hadamard_contrib (1/2)). No case takes a function, an L-series, zeta or a zero as argument.',
    '  c1_exclusion .. c6_exclusion :167-:192 -- DERIVES what each states (real algebra about sigma, C6 through cr_forces_half). c7_exclusion :194-:196 -- ENCODES-CONCLUSION/SHELL:'
    ' hadamard_contrib := 0 (:138), so voice7_sigma_neutral (:144-:145) is rfl, as the docstring :113-:118 says.',
    '  none_produce :198-:207 -- DERIVES, the case split of the seven; its strength is the weakest of its cases (C7`s, SHELL).',
    '  StructuralExhaustiveness :215-:221 and structural_exhaustiveness_proved :249-:251 -- DERIVES the literal conjunction (card = 7 ; the seven sigma-predicates false ; Ostrowski over Q);'
    ' as a statement about the zeros of zeta, ENCODES-CONCLUSION/SHELL: no conjunct names a zero; v1.8`s docstring (the diff v1.5..v1.8, docstrings only) says it does not state exhaustiveness.',
    '  transformation_class :257-:260 -- a DEFINITION: three stages to three classes.',
    '  Kernel/Layer1.lean :4-:6, structure MechanismClass (X) (P) -- a DEFINITION: a name and produces : X -> Prop, a predicate on POINTS of X. ExhaustiveCatalogue :21-:24; NoneProduces :26-:28;'
    ' SIDE_exclusion :30-:38 DERIVES (pure logic: a covering catalogue none of whose classes produces x gives not P x).',
    '  Bridge/SIDEBridge.lean :21-:35, its one instance, X = C (a point s): C1 and C2 both produce := s.re != 1/2 (:23, :28), C_simple := s.re = 1/2 and deriv = 0 (:33);'
    ' xi_catalogue :37-:49 -- ENCODES-CONCLUSION/SHELL: its covering holds because C1`s predicate IS the off-line disjunct of OffLineOrNonSimple (:15-:17).',
    '  MetaKernel.lean :60-:68 RH_MechanismClass -- a DEFINITION, seven constructors; rh_classes_complete :77-:88 DERIVES the enumeration; the Fintype instance :155-:159 certifies the catalogue,'
    ' and :94-:95 say so ("certify the catalogue (exactly seven classes), not the exclusion").',
    '  Bridge/CrossClassExclusion.lean :52-:53 coupling_strength _c1 _c2 -- a DEFINITION ignoring both arguments (a constant, 0 + 0); cross_class_exclusion :72-:77 and all_pairs_excluded :80-:82'
    ' DERIVE from none_produce and that constant: ENCODES-CONCLUSION/SHELL as a statement about couplings.',
    '  THE SIBLING, W-ORD-PREMISE-PERCLASSEXCLUDES (OPEN_TRAILS :13445): SIDE-lv-conservation 2f71068 T3_StepNineBridge.lean :44 Coupling := (R -> C) -> Prop, :52-:53 PerClassExcludes C s :='
    ' exists Phi, C Phi and mellin Phi (s/2) != 0 -- a DEFINITION whose class IS a predicate on FUNCTIONS (Mellin integrands); T3_perClass_to_combinations :92-:108 is pinned by one sorry (:108),'
    ' the forall-exists to exists-forall swap of FINDINGS F.2026-07-09-b. It is not linked to the seven constructors: no declaration printed above maps a Coupling to a MechanismClass.',
    '  THE ANSWER TO (5)(i): SIDE-kernel v1.5 gives a class AN ENUMERATION WITH A COUNT (TheBridgeComplete :20-:25; MetaKernel :60-:88), with per-class predicates on a real sigma (:157-:165);'
    ' its general structure (Layer1 :4-:6) gives a predicate on points, instanced only at points s of C (SIDEBridge :21-:33). NO CLASS OF THE SEVEN IS GIVEN A PREDICATE ON FUNCTIONS.'
    ' A predicate on functions is found, in what this bank read, only at SIDE-lv-conservation`s Coupling (2f71068 :44), outside the seven; the federation was not searched for others.',
    '  THE CENSUS (FINDINGS :4885-:4922, read at HEAD), CLASS BY CLASS AT THE v1.5 TREE: C1 c1_closing (Kernel/ThomBridge.lean :39-:41, a value statement on completedRiemannZeta0) and'
    ' c1_exclusion :167 -- STANDS. C2 conservation_activates_balance (ConservationBridge.lean :34-:38) under ConservationHypothesis (:26-:29) and c2_exclusion :171 -- STANDS; its ch_iff_rh is'
    ' SIDE-explicit-formula`s (H2Bridge.lean :71, FINDINGS :4756), absent from SIDE-kernel`s history (git log -S, every ref: none). C3 voice3_fe_zeros :45-:48 on completedRiemannZeta0 and'
    ' c3_exclusion :175 -- STANDS. C4 c4_closing (ThomBridge.lean :43-:44, Mathlib`s riemannZeta_ne_zero_of_one_le_re, a zero-free half-plane) and c4_exclusion :179 -- STANDS. C5 c5_exclusion :183'
    ' -- STANDS; Register5_output_HilbertPolya is SIDE-explicit-formula`s (RegisterDepth.lean, FINDINGS :4833), not in this tree. C6 the docstring :239-:242 naming xi-faithfulness'
    ' MANUSCRIPT-RESIDENT and c6_exclusion :187 -- STANDS. C7 voice7_zero_symmetry :70-:73 (C3`s reflection under C7`s name) and hadamard_contrib := 0 :138 -- STANDS.'
    ' The census`s reading stands at the tree for all seven; the table is not rebuilt.',
    '  THE RECORD`S OWN WORD ON EPSTEIN AT C7 (TheBridgeComplete.lean :129-:136, v1.5): "Completed Epstein zeta functions ALSO have Hadamard factorizations and DO have off-line zeros; the product is'
    ' present in systems that violate RH, so its presence cannot enforce on-line placement" -- unmodeled at the pin; refiled as W-ORD-C7-WITNESS, "a two-point Epstein-vs-ideal countermodel, kin to'
    ' SieveCeilingWitness/dh_witness".',
    '',
    '## (ii) SIDE-explicit-formula v0.38 (14ca5725)',
    '  rQ, Schema/EpsteinZQ.lean :59-:62 -- a DEFINITION: the lattice count of Q0form m n = k over the box |m| <= 2k, |n| <= k; rQ 0 = 0 (:64-:65, DERIVES). ZQ :69 the LSeries of rQ.',
    '  cQ, Schema/ZQ/LogDeriv.lean :63-:66 -- a DEFINITION by the recursion 2 cQ(n) = rQ(n) log n - SUM over proper divisors cQ(d) rQ(n/d); cQ_eq :71-:81 and cQ_conv :84-:96'
    ' (c conv rQ = log . rQ off 0) DERIVE. :6 states "Z_Q has no Euler product".',
    '  THE DECLARATION TAKING c TO BE VON MANGOLDT AT zeta: NONE AS A NAMED DECLARATION OF A GENERIC c. The generic schema WeilConfig (Schema/Config.lean :24-:34) carries the arithmetic side as'
    ' rhs : (R -> C) -> C, with no coefficient field. At zeta, Lambda enters by name: B321.primeSum (B321Identity.lean :33-:34) writes the prime channel with ArithmeticFunction.vonMangoldt, a'
    ' DEFINITION; integrand_eq_tsum (Zeta23/WeilEF/VerticalLine.lean :100-:111) DERIVES -logDeriv riemannZeta = LSeries Lambda on Re s > 1 through Mathlib`s'
    ' ArithmeticFunction.LSeries_vonMangoldt_eq_deriv_riemannZeta_div (:108), as a local have. No declaration of the tree relates cQ to Lambda (the grep above: cQ and vonMangoldt share no file).',
    '',
    '## (iii) MATHLIB AT THE KERNEL`S PIN (e960b841, SIDE-kernel lake-manifest :8; SIDE-explicit-formula pins de5ce8a9)',
    '  ArithmeticFunction.vonMangoldt_nonneg, VonMangoldt.lean :80-:84 -- DERIVES 0 <= Lambda n, for Lambda alone.',
    '  riemannZeta_ne_zero_of_one_le_re, Nonvanishing.lean :411-:415 -- DERIVES, from LFunction_ne_zero_of_one_le_re (:398-:401) at chi = 1 (LFunction_modOne_eq), and'
    ' riemannZeta_one_ne_zero at s = 1.',
    '  THE ROUTE (the file`s outline :28-:40 and the lemmas :220-:314): the 3-4-1 product L(chi^0, 1+x)^3 L(chi, 1+x+iy)^4 L(chi^2, 1+x+2iy) has norm >= 1 (norm_LSeries_product_ge_one :285-:303),'
    ' through LSeries_eulerProduct_exp_log (:295-:296) and re_log_comb_nonneg (:241-:265), which reads each EULER FACTOR -log(1 - chi(p) p^-s) with |chi(p) p^-iy| = 1 at units (:250-:254)'
    ' and the Taylor series of -log(1 - a z) (re_log_comb_nonneg` :220-:238).',
    '  THE ANSWER TO (5)(iii): THE HYPOTHESES ARE FOR DIRICHLET CHARACTERS (chi : DirichletCharacter C N, :216), through their Euler products, with zeta as chi = 1 -- NOT for a Dirichlet series with'
    ' nonnegative coefficients. vonMangoldt_nonneg is not called in Nonvanishing.lean (git grep of Mathlib/NumberTheory/LSeries at e960b841: Dirichlet.lean :385 and PrimesInAP.lean :136, :139,'
    ' :206 only; the Euler-product files outside that directory not grepped).'
    ' The general positivity lemmas for nonnegative coefficients exist (LSeries/Positivity.lean :59 positive, :99 LSeries_positive: an LSeries with a >= 0, a 1 > 0 is positive on the real axis'
    ' right of its abscissa) and serve the quadratic case at s = 1 (:33-:35), not the 3-4-1 product.',
    '',
    '## (iv) PATHS (PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md, read at HEAD) AND THE TABLE ORDER',
    '  A9 :389: "Lambda(n) >= 0 (von Mangoldt) => zero-free region near sigma=1 | proven classically | de la Vallee Poussin 1896, via 3+4cos+cos2 >= 0 (3-4-1);'
    ' ArithmeticFunction.vonMangoldt_nonneg (Mathlib)". READ AGAINST (iii): the classical citation stands; the Mathlib name it gives is the nonnegativity lemma, which Mathlib`s'
    ' Nonvanishing.lean at e960b841 does not call (that proof runs on unimodular Euler-factor coefficients chi(p), :241-:265). A finding of this bank, to carry, not an edit.',
    '  B3 :396: "Lambda>=0 yields the edge, never the center" -- a classical boundary, cited; no declaration to grade. C1 :410: positivity -> the sigma = 1 edge, universally, for families whose'
    ' ledger -L`/L is positive -- cited; no declaration to grade. :402: "EPSTEIN-SIGN takes B3 as its exact statement (Epstein loses Lambda>=0 -> loses even the edge)".',
    '  W-ORD-MECHANISM-TABLE (OPEN_TRAILS :16589): its object a table of the mechanisms by which a function with some of {Euler product, functional equation, Ramanujan size, additive structure}'
    ' has off-line zeros, the Epstein zetas and Davenport-Heilbronn "under class-group averaging"; built at b726 (data/b726_mechanisms.txt, three rows) and left open for a fourth row (:28, :42).',
    '',
    '## THE AMENDMENT`S SOURCES (row 1), READ WHOLE',
    '  data/b726_mechanisms.txt (42 lines): ROW 1 :7-:12 CLASS-GROUP AVERAGING -- "Z_Q averages over the class group, and its zeros are where the averaged terms cancel" (:10); h = 2 by the'
    ' closed form log(Z_Q/2) = log zeta_K - S + log cosh S (b723, NOT COMPILED, checked POST HOC 19 of 19); h = 3 "at a zero of Z_Q0, zeta_K = Z_Q1 = -2 L(s, psi)" (b725 :31), H-INTERFERENCE'
    ' HELD 69 of 69; INSTANCE the 69 certified off-line zeros of Z_Q0 to height 445 (:11) and dh_witness. INGREDIENTS kept: functional equation, Ramanujan size, additive structure; dropped: the'
    ' Euler product (:9). ROW 2 size, ROW 3 Beurling (no instance with a functional equation, :25, :39-:42). Asserts nothing about zeta (:4).',
    '  data/b723_c2_closed_form.txt (70 lines): h(D) = 2; the four steps :23-:33 (genus character psi; L(psi)/zeta_K = e^(-2S) over the NON-PRINCIPAL primes, :26-:30); consequences :35-:60 --'
    ' (a) b(n) = 0 at every n with two distinct primes one principal; (b) no negative at Omega(n) <= 3; (c) Omega(n) = 4 the first place a negative can sit (-S^4/12); (d) a non-principal ramified'
    ' prime at every such field. A derivation, NOT COMPILED, NOT NEW (genus theory, :3-:4); checked POST HOC (:62-:68).',
    '  data/b732_beurling_read.txt (28 lines): no Beurling system with a functional equation and a zero off its centre line found in the sources read (:26); a search is not a survey (:5).',
    '  dh_witness, SIDE-kernel v1.8 (70aba3cd) Kernel/Cascade/SieveCeilingWitness.lean :94-:95 (unchanged since v1.5: git diff --stat v1.5 v1.8 -- Kernel/Cascade/ lists four other files and not'
    ' this one), with the definitions its statement names: Config :49-:52 (two constructors, ideal and dh), darkObs :62-:64 (true at both), iIndist :71, allOnLine :87-:89 (True at ideal,'
    ' FALSE at dh, by definition), NonInvarianceWitness (SieveCeilingSemantic.lean :59-:60). GRADE: ENCODES-CONCLUSION/SHELL -- the off-line zeros of Davenport-Heilbronn are the definitional'
    ' datum allOnLine .dh = False, "cited, not reproved" (:84-:86), and the indistinguishability is darkObs constant by stipulation (:54-:61); the witness is then rfl, trivial and id (:95).'
    ' dh_sieve_ceiling :100-:102 DERIVES from it through sieve_ceiling_of_witness.',
    '',
    '## THE SIGNATURE BANK READ BESIDE b723 (data/b752_cq_signature.txt, committed 8c0b6206; this bank counts its cells, it computes no cQ)',
]


def span(repo, rev, path, lo, hi):
    L = g(repo, 'show', '%s:%s' % (rev, path)).replace('\r', '').split(NL)
    out = ['---- %s %s:%s :%d-:%d (commit %s, blob %s, %d lines)' % (os.path.basename(repo), rev, path, lo, min(hi, len(L)),
                                                                      g(repo, 'rev-parse', '--short=8', rev + '^{commit}').strip(),
                                                                      g(repo, 'rev-parse', '--short=8', '%s:%s' % (rev, path)).strip(), len(L))]
    for i in range(lo, min(hi, len(L)) + 1):
        out.append('  %5d  %s' % (i, L[i - 1]))
    return out


def sig_read():
    """Counts of the cells of data/b752_cq_signature.txt: the sign against the prime types present. Reads the committed bank; computes no cQ."""
    import re
    t = io.open(os.path.join(RELAY, 'data', 'b752_cq_signature.txt'), encoding='utf-8').read().replace('\r', '')
    cells = [c.strip() for l in t.split(NL) if l.startswith('  ') and ' = ' in l and ' ; ' in l for c in l.split('|')]
    cells = [c for c in cells if re.match(r'^\d+ = .* ; [-+] ; ', c)]
    neg = [c for c in cells if ' ; - ; ' in c]
    pos = [c for c in cells if ' ; + ; ' in c]
    other = lambda c: re.search(r'\[(P|I|R)\]', c.split(' ; ')[0]) is not None
    hasN = lambda c: '[N]' in c.split(' ; ')[0]
    mixed = [c for c in cells if other(c) and hasN(c)]
    return ['  cells read: %d (negative %d, positive %d); the bank`s own count of n with cQ(n) != 0 is 501' % (len(cells), len(neg), len(pos)),
            '  negative n carrying a prime of type P, I or R: %d of %d -- every negative n is a product of type-N primes alone (b723 (c)`s "no listed negative carrying a principal prime", read'
            ' at h = 3 over n <= 3000)' % (sum(map(other, neg)), len(neg)),
            '  n with cQ(n) != 0 carrying both a type-N prime and a prime of type P, I or R: %d -- every nonzero cQ(n) sits on an n whose primes are all N or none N (the shape of b723 (a) at h = 3,'
            ' over n <= 3000)' % len(mixed),
            '  the bank`s (o1): no negative at Omega_N <= 3; the first negatives at Omega_N = 4 (b723 (b)-(c)`s shape at h = 3). The table`s TRUE (102 of 102) is carried in every case by 2 or 3'
            ' ((o4): the pair (0, 0) holds no negative), so it reads no finer than "every negative n is divisible by 2 or 3"; the all-N count above is the finer reading.',
            '  POST HOC: these readings were made after the bank was printed, knowing b723; nothing here is claimed beyond n <= 3000; no closed form for h = 3 is written or compiled.']


def main(argv):
    t0 = time.time()
    L = ['b752 -- (R362)(5): THE STATEMENTS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '']
    only = [a[7:] for a in argv if a.startswith('--part=')]
    if only and '--bank' in argv:
        sys.exit('### --bank WITH --part REFUSED: THE BANK IS WRITTEN WHOLE OR NOT AT ALL -- NOTHING WRITTEN')
    for part, repo, rev, path, lo, hi in SPANS:
        if only and part not in only:
            continue
        L += ['## (%s)' % part] + span(repo, rev, path, lo, hi) + ['']
    for part, repo, rev, needle in GREPS:
        if only and part not in only:
            continue
        rows = [r for r in g(repo, 'grep', '-n', '-E', needle, rev, '--', '*.lean').split(NL) if r.strip()]
        L += ['## (%s) git grep -n -E "%s" at %s in %s: %d rows' % (part, needle, rev, os.path.basename(repo), len(rows))] + ['  ' + r[:240] for r in rows[:60]] + ['']
    L += ['## THE GRADES'] + ['  ' + x for x in GRADES]
    L += sig_read()
    L += ['', '### ### **THE STATEMENTS: (i) A CLASS OF SIDE-kernel v1.5 IS AN ENUMERATED CONSTRUCTOR WITH A COUNT (7) AND A PREDICATE ON A REAL sigma; NONE OF THE SEVEN HAS A PREDICATE ON'
          ' FUNCTIONS (the one such predicate found in what was read: SIDE-lv-conservation`s Coupling, outside the seven) ; THE CENSUS STANDS AT THE TREE FOR ALL SEVEN ; (ii) NO GENERIC c IS'
          ' INSTANCED AS LAMBDA, LAMBDA ENTERS AT zeta BY NAME, NO DECLARATION RELATES cQ TO LAMBDA ; (iii) MATHLIB`S 3-4-1 ROUTE IS FOR DIRICHLET CHARACTERS THROUGH EULER PRODUCTS, NOT'
          ' FOR NONNEGATIVE COEFFICIENTS, AND Nonvanishing.lean DOES NOT CALL vonMangoldt_nonneg ; (iv) PATHS A9`s MATHLIB NAME IS NOT THAT ROUTE`S LEMMA (carried) ; dh_witness SHELL ; %.1f s.**' % (time.time() - t0)]
    text = NL.join(L) + NL
    print(text, end='')
    if '--bank' in argv:
        if os.path.exists(BANK):
            sys.exit('### %s EXISTS: WRITTEN ONCE -- NOTHING WRITTEN' % BANK)
        io.open(BANK, 'w', encoding='utf-8', newline='\n').write(text)
        print('  banked: data/b752_statements.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
