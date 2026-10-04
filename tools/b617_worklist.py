# -*- coding: utf-8 -*-
"""b617_worklist.py -- THE ACT'S DATA, UNDER (R227)(4). ### NO WRITE.

### (R227)(4): the sieve's v0.5 beside v0.4 (PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md at 52962da) -- the ten
### conclusions of relay data/b616_routes_for_sieve.txt as rows, each with its quantifier shape (H), register, verdict and test, instrument
### at pin and source syntheses named; the head's counts re-stated; the FACE and NOT A ROUTE groups unchanged; the bench unchanged. Each
### row's instruments and its source route rows are resolved by git at their pins (the line exists, its needle is on it); each head
### rewrite is a fragment of a v0.4 line that occurs once on it, with the seat's new wording; `resolve_*` read the blobs and check every
### fragment; nothing here writes. The template is tools/b609_worklist.py.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
PRE_PP = '52962da'
NL = chr(10)

SV4 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'      # ### the sieve's current version, unedited
SV3 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'      # ### unedited
SV2 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'      # ### unedited
SV1 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'           # ### the unnumbered version, read as v0.1, unedited
SV5 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md'      # ### this act's edition
SYN = {
    '1.2': 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md',
    '1.5E': 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
    '2B': 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md',
}


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _at(repo, rev, path, n):
    ls = lines_of(show(rev, path, repo))
    return ls[n - 1] if 0 < n <= len(ls) else None


# ================================================================================ THE INSTRUMENTS AT THEIR PINS (v0.4's own cells)
T1 = '1 (I-7 @ 847e433; IB Thm 3.1 @ 1d0109f)'
T2 = '2 (detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f)'
T4 = '4 (forall_upto pair @ v0.3 = 04eda4a; li_nonneg_iff_rh @ v0.9 = e5a5a83)'
IB = 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md'
# ### each test's instrument lines, resolved by git: (repo, rev, path, line, the needle the line must hold)
INST = {
    T1: [(PP, '847e433', 'phase1.5/method/INSTRUMENTS.md', 93, '## I-7 — THE PLACEMENT SCREEN'),
         (PP, '1d0109f', IB, 148, '**Theorem 3.1 (Sieve Ceiling Lemma).**')],
    T2: [(EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean', 99, 'theorem detector (C : WeilConfig)'),
         (EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean', 57, 'theorem epstein_not_h2_sign_cfg'),
         (PP, '1d0109f', IB, 259, '**Theorem 3.7 (Euler-product barrier against T).**')],
    T4: [(EFK, 'v0.3', 'SIDEExplicitFormula/DetectionRegion.lean', 47, 'theorem h2_sign_iff_forall_upto'),
         (EFK, 'v0.3', 'SIDEExplicitFormula/DetectionRegion.lean', 52, 'theorem forall_upto_iff_rh'),
         (EFK, 'v0.9', 'SIDEExplicitFormula/LiCriterionBridge.lean', 179, 'theorem li_nonneg_iff_rh')],
}
RH60_TEST = T2   # ### RH-60's test cell at v0.4 :122, read again by resolve_sieve

# ================================================================================ THE TEN ROWS (R227)(4)
NAR, DARK = 'NOT A ROUTE', 'DARK'
SYMREG = 'the symmetry and its level curves'
NEW_ROWS = [
    dict(id='RH-61', key='K1', verdict=NAR, test='—', shape='FINITE (H)', register=SYMREG,
         conclusion='The paths to σ = 1/2 share the one involution s ↦ 1 − s, so their agreement identifies the line and places no zero; the '
                    'papers withdraw them as an argument for placement.',
         reason='the papers’ own correction of 2026-08-10: the paths identify the line through the involution they share and carry no '
                'placement, offered toward no target',
         sources=[('1.2', 'R3', 135, '| R3 | ME-15 | NOT A ROUTE |'), ('1.5E', 'R2', 183, '| R2 | TF-02, TS-03, CO-16 | NOT A ROUTE |'),
                  ('2B', 'R2', 165, '| R2 | IS-02 | NOT A ROUTE |')]),
    dict(id='RH-62', key='K2', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register=SYMREG,
         conclusion='An off-line zero is read as a location-type property that neither the symmetry structure nor the multiplicative '
                    'structure produces, offered as excluding off-line zeros of ξ; the type analysis is the papers’ argument and no compiled '
                    'step.',
         reason='with the symmetry structure alone, as an Epstein ζ_Q has it, the same type analysis finds no location-type mechanism, yet the '
                'Epstein configuration carries an off-line point, which the detector meets at ρ_E with a negative window',
         sources=[('1.2', 'R2', 134, '| R2 | IR-05 | DARK |')]),
    dict(id='RH-63', key='K3', verdict=DARK, test=T4, shape='FINITE (H)', register='multiplicity',
         conclusion='Localizing the explicit formula at a zero equates its multiplicity with a prime-side value, computed to be 1 at finitely '
                    'many zeros; the step to every zero is the localization the papers list as owed.',
         reason='the prime side enters, so test 2 is cleared, but the value is computed at finitely many zeros and the universal step is the '
                'localization owed: a FINITE check with no ladder of rungs to every zero; tests 1 and 3 n/a',
         sources=[('1.2', 'R4', 136, '| R4 | ME-12 | DARK |')]),
    dict(id='RH-64', key='K4', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register=SYMREG,
         conclusion='Along the curve Re ξ = 0 leaving a simple zero, the modulus of Im ξ is argued to increase strictly, offered as keeping '
                    'off-line zeros off that curve; the step that the curve has no critical points is not given.',
         reason='the argument uses the functional equation, Schwarz reflection and the Cauchy–Riemann equations alone, which an Epstein ζ_Q '
                'with real coefficients carries, and the Epstein configuration carries an off-line point the detector meets at ρ_E',
         sources=[('1.2', 'R5', 137, '| R5 | ME-10, IP-06 | DARK |')]),
    dict(id='RH-65', key='K5', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register=SYMREG,
         conclusion='An off-line zero needs two real conditions in one real parameter where an on-line zero needs one, offered with '
                    'genericity as excluding off-line zeros of a determined system; the step from generic to actual for ξ is marked open.',
         reason='the count of real conditions holds for every function real on its symmetry line, an Epstein ζ_Q among them, whose off-line '
                'point the detector meets at ρ_E; the papers mark the step for ξ open',
         sources=[('1.2', 'R6', 138, '| R6 | ME-11 | DARK |'), ('1.5E', 'R5', 186, '| R5 | TS-18, CO-12 | DARK |')]),
    dict(id='RH-66', key='K6', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register=SYMREG,
         conclusion='The involution s ↦ 1 − s fixes σ = 1/2, and its fixed line with the monodromy concentrated there is offered as placing '
                    'the zeros on the line.',
         reason='the fixed point of s ↦ 1 − s and its monodromy are shared by every function with this functional equation, an Epstein ζ_Q '
                'among them, whose off-line point the detector meets at ρ_E',
         sources=[('1.2', 'R7', 139, '| R7 | IP-02 | DARK |'), ('1.5E', 'R4', 185, '| R4 | CO-18 | DARK |')]),
    dict(id='RH-67', key='K7', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register=SYMREG,
         conclusion='Analytic, topological and structural lines of evidence are read as converging on every nontrivial zero lying on the line, '
                    'and the papers call them evidence.',
         reason='the papers’ analytic results use only the functional equation and the Cauchy–Riemann equations, not the Euler product, so '
                'they hold unchanged at the Epstein configuration',
         sources=[('1.5E', 'R6', 187, '| R6 | TS-26 | DARK |')]),
    dict(id='RH-68', key='K8', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register='the mechanism catalogue',
         conclusion='An inventory of the known mechanisms producing zeros of functions with a functional equation finds none producing a zero '
                    'off the line, offered as excluding one; the inventory names no prime-side ingredient.',
         reason='the inventory names no prime-side ingredient, and the Epstein configuration (FD-01) carries an off-line point with a '
                'functional equation',
         sources=[('1.5E', 'R7', 188, '| R7 | TS-25 | DARK |')]),
    dict(id='RH-69', key='K9', verdict=DARK, test=T2, shape='UNIVERSAL (H)', register='the codes and the substrate',
         conclusion='The Frobenius property of {2, 3}, read by the papers as fixing the physical constants, is offered as also placing the zeta '
                    'zeros on the line, the step stated without an argument.',
         reason='the Frobenius property of {2, 3} is a fact about the integers and names no prime side; the integers an Epstein ζ_Q sums over '
                'carry it unchanged',
         sources=[('1.5E', 'R8', 189, '| R8 | CO-09 | DARK |')]),
    dict(id='RH-70', key='K10', verdict=DARK, test=T1, shape='DENSITY (H)', register='multiplicity',
         conclusion='The modulus of ζ′(ρ) divided by √γ over the first thirty zeros, mean 0.251 with no trend, is read as a barrier growing '
                    'like √γ; a statistic over finitely many ordinates.',
         reason='a statistic over thirty ordinates offered toward placement and simplicity: it carries no zero’s real part and bounds no zero '
                'beyond the thirty',
         sources=[('1.5E', 'R9', 190, '| R9 | CO-15 | DARK |')]),
]


def face_cell(r):
    return 'none -- the syntheses’ route rows: ' + '; '.join('%s %s (its :%d)' % (k, rr, n) for k, rr, n, _nd in r['sources'])


def row_line(r):
    return '| %s | %s | %s | %s | %s | %s | %s | %s |' % (r['id'], r['conclusion'], r['shape'], r['register'], r['verdict'], r['test'],
                                                          r['reason'], face_cell(r))


VERSION5 = ('*v0.5, 2026-10-04 -- ten rows added from the routes the six syntheses list for the sieve (nine DARK, seven of them by test 2, '
            'and one NOT A ROUTE) and one register; v0.4 stands beside it, unedited.*')

# ### the head's rewrites: (v0.4 line, old fragment, new fragment, what)
SV_REWRITES = [
    (40, 'their per-class exclusions and the place count).',
     'their per-class exclusions and the place count); at v0.5, one more: the symmetry and its level curves (the involution s ↦ 1 − s, '
     'its fixed line σ = 1/2 and the level curves of ξ, real on that line).',
     'the registers: the one the added rows read that the list lacked, (R227)(4)'),
    (44, '5 of them carry the table’s 87 rows', '5 of them carry the table’s 97 rows', 'the head’s row count re-stated, (R227)(4)'),
    (48, '87 rows -- 2 BRIGHT, 7 DARK, 67 NOT A ROUTE, and 11 FACE rows', '97 rows -- 2 BRIGHT, 16 DARK, 68 NOT A ROUTE, and 11 FACE rows',
     'the head’s verdict counts re-stated, (R227)(4)'),
    (50, '— 60 rows: 11 FACE, 2 BRIGHT, 7 DARK, 40 NOT A ROUTE', '— 70 rows: 11 FACE, 2 BRIGHT, 16 DARK, 41 NOT A ROUTE',
     'the cluster heading’s counts re-stated, (R227)(4)'),
    (70, '— 49 rows', '— 59 rows', 'the other rows’ heading re-stated, (R227)(4)'),
]

# ### each row read against the existing rows by conclusion (H51a): the nearest existing row by hand and why the conclusions differ
DUP = {
    'RH-61': ('RH-02', 'RH-02 is the deposit’s Route 3 clause shown to be RH restated; RH-61 is the papers’ own withdrawal of the paths to '
                       'σ = 1/2 as placement, a reading of their shared involution, and names no clause'),
    'RH-62': ('RH-60', 'RH-60 is the seven compiled classes and their σ-only exclusions; RH-62 is IR’s type analysis of a location-type property '
                       'against the symmetry and multiplicative structures, uncompiled and naming no class'),
    'RH-63': ('RH-15', 'RH-15 is the simplicity target unfolded; RH-63 is an argument equating multiplicity with a prime-side value at finitely '
                       'many zeros, a candidate route toward it'),
    'RH-64': ('RH-25', 'RH-25 is the detector meeting every off-line point with a negative window; RH-64 is the level-curve monotonicity along '
                       'Re ξ = 0, an argument about ξ alone'),
    'RH-65': ('RH-60', 'RH-60 enumerates classes; RH-65 counts real conditions, two off the line against one on it, with a genericity step'),
    'RH-66': ('RH-60', 'RH-60 is the compiled class enumeration; RH-66 offers the involution’s fixed line and its monodromy as placing the '
                       'zeros, beside the new RH-61, which reads the same involution as identifying the line and is offered toward no target'),
    'RH-67': ('RH-60', 'RH-60 is the compiled class enumeration; RH-67 is a convergence of three lines of evidence the papers name evidence'),
    'RH-68': ('RH-60', 'RH-60 is the seven classes, Ostrowski-exhaustive and compiled at SIDE-kernel v1.5; RH-68 is TS’s uncompiled inventory '
                       'of the known zero-producing mechanisms (TS :605-:611: algebraic, spectral, topological, knot-theoretic, analytic), '
                       'none of them a class of the seven'),
    'RH-69': ('CT-01', 'CT-01 is the findings pass’s independence decision for the codes and the substrate; RH-69 offers the substrate’s '
                       'Frobenius property as placing the zeros'),
    'RH-70': ('RH-59', 'RH-59 is the GUE spacing statistic toward simplicity; RH-70 is a different statistic, the modulus of ζ′(ρ) over √γ '
                       'at thirty zeros, read as a growing barrier'),
}


def _tok(s):
    return set(w for w in re.findall(r'[a-zα-ωζξρσγ0-9]+', s.lower()) if len(w) > 3 and w not in STOP)


STOP = {'that', 'with', 'from', 'this', 'their', 'they', 'which', 'every', 'zero', 'zeros', 'line', 'offered', 'read', 'papers'}


def neighbours(rows4, r, k=3):
    """### the existing rows nearest a new row by shared content words of the conclusion (a printed aid; the reading is DUP's)"""
    a = _tok(r['conclusion'])
    sc = []
    for rid, concl in rows4:
        b = _tok(concl)
        sc.append((len(a & b) / max(1, len(a | b)), rid))
    return sorted(sc, reverse=True)[:k]


def resolve_instruments():
    out = []
    for t, src in INST.items():
        for repo, rev, path, n, needle in src:
            l = _at(repo, rev, path, n)
            out.append(dict(test=t.split(' ')[0], repo=os.path.basename(repo), rev=rev, path=path, line=n, ok=l is not None and needle in l,
                            text=(l or '### NO SUCH LINE')[:200]))
    return out


def resolve_sources():
    out = []
    for r in NEW_ROWS:
        for k, rr, n, needle in r['sources']:
            l = _at(PP, PRE_PP, SYN[k], n)
            out.append(dict(row=r['id'], cluster=k, route=rr, path=SYN[k], line=n, ok=l is not None and l.startswith(needle),
                            text=(l or '### NO SUCH LINE')[:220]))
    return out


def rows_of(ls):
    """### the table rows of a sieve version's body: (id, conclusion, verdict, test)"""
    out = []
    for l in ls:
        m = re.match(r'^\| ([A-Z]{2}-\d\d) \| ', l)
        if m:
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out.append((c[0], c[1], c[4], c[5]))
    return out


def resolve_sieve():
    S4 = lines_of(show(PRE_PP, SV4))
    bad = []
    for n, old, new, what in SV_REWRITES:
        if S4[n - 1].count(old) != 1:
            bad.append(('rewrite', n, S4[n - 1].count(old)))
    body = S4[:S4.index('<!-- b604 (R214) THE v0.2 EDITION`S BACK MATTER, 2026-10-03 -->')]
    rows = rows_of(body)
    ids = [x[0] for x in rows]
    for r in NEW_ROWS:
        if r['id'] in ids:
            bad.append(('row id taken', r['id']))
        if any(x in row_line(r) for x in ('|  |', ' || ')):
            bad.append(('blank cell', r['id']))
        if row_line(r).count(' | ') != 7:
            bad.append(('cells', r['id'], row_line(r).count(' | ')))
    r60 = [x for x in rows if x[0] == 'RH-60']
    if not r60 or r60[0][3] != RH60_TEST:
        bad.append(('RH-60 test cell', r60))
    if S4[121] != next(l for l in S4 if l.startswith('| RH-60 | ')):
        bad.append(('RH-60 not at :122',))
    return S4, bad
