# -*- coding: utf-8 -*-
"""b358_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **THE ACT IS A READ AND A PRICING**, and this extract IS its evidence: every sentence the bank
### quotes must be locatable at the file that carries it -- the DEPOSIT for the corpus's side, the PINNED
### SOURCE TEXTS for the literature's -- and the reading must be defensible against the words on that line
### and not against a memory of them.
### ### **THE SOURCE TEXTS ARE THE ONES `tools/b358_locate.py` FETCHED AND HASHED.** ### A line quoted here
### is a line of bytes whose sha-256 is banked.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


VOROS = d('b358_source_voros0506326.txt')
LAG = d('b358_source_lagarias0404394.txt')

READS = [
    # ---- THE ORDER AND THE CAP ---------------------------------------------------------------------
    ('the order -- act b358, the Li asymptotics under a cap', 'ORDER', d('b358_ferry_2026-09-07.txt'),
     'ACT b358 — THE LI ASYMPTOTICS, READ UNDER A CAP. Number not'),
    ('the cap -- reads and a pricing only', 'ORDER', d('b358_ferry_2026-09-07.txt'),
     'CAP, quoted in the registration: ONE act; reads and a pricing'),
    ('the cap -- NO USABLE ASYMPTOTICS LOCATED is a full verdict', 'ORDER', d('b358_ferry_2026-09-07.txt'),
     'beyond what is banked; "NO USABLE ASYMPTOTICS LOCATED" is a'),
    ('the order -- the circularity check, before any verdict', 'ORDER', d('b358_ferry_2026-09-07.txt'),
     'COMPONENT 3 — THE CIRCULARITY CHECK, run before any verdict:'),
    ('ruling R4 -- the instrument lane is PARKED', 'ORDER', d('b358_ferry_2026-09-07.txt'),
     '(R4) The instrument lane is PARKED: the draft'),

    # ---- THE DEPOSIT'S OWN WORDS (COMPONENT 1's FIRST HALF) -----------------------------------------
    ('THE DEPOSIT -- the finite-range certificate and where it stops', 'DEPOSIT', DEPOSIT,
     'certifies λ_n ≥ 0 for n up to Voros'),
    ('THE DEPOSIT -- the ancestry of the sharpest form', 'DEPOSIT', DEPOSIT,
     'The ancestry of the sharpest form.'),
    ('THE DEPOSIT -- the open clause, in the two-channel Li form', 'DEPOSIT', DEPOSIT,
     'the inequality λ_Z(n) ≥ −λ_A(n) for every n (RH-equivalent'),
    ('THE DEPOSIT -- Voros 2006 in the bibliography', 'DEPOSIT', DEPOSIT,
     'Voros, A. (2006). A sharpening of Li'),
    ('THE DEPOSIT -- Oesterle, unpublished, cited in Voros', 'DEPOSIT', DEPOSIT,
     'Oesterlé, J. (unpublished). Asymptotic behaviour of the Li coefficients'),
    ('THE FACES LEDGER -- row R4, the finite-range certificate', 'LEDGER', FACES,
     'R4 -- the distance between balance and positivity at the multiplicative place'),
    ('THE FACES LEDGER -- row L1, the Li-to-Weil bridge and the pin', 'LEDGER', FACES,
     'L1 -- the Li-to-Weil bridge: the Li coefficients as the Weil functional'),

    # ---- VOROS (S1), PINNED ------------------------------------------------------------------------
    ('VOROS -- the abstract: if (and only if) the Hypothesis is true', 'VOROS', VOROS,
     'For n → ∞ we obtain that if (and only if) the Hypothesis is true,'),
    ('VOROS -- the criterion as Li stated it', 'VOROS', VOROS,
     'Li’s criterion for the Riemann Hypothesis (RH) states that the latter is true if an d'),
    ('VOROS -- the two mutually exclusive asymptotic forms', 'VOROS', VOROS,
     'if RH is true, λ n will grow tamely according to (17); if RH is false'),
    ('VOROS -- the derivation of (17) OPENS by assuming the zeros are on the line', 'VOROS', VOROS,
     'all the zeros lie on the critical line, ﬁrst transform the summation'),
    ('VOROS -- (24), the archimedean expansion, UNCONDITIONALLY', 'VOROS', VOROS,
     '4k n1−2k (n → ∞ ) unconditionally. (24)'),
    ('VOROS -- (24) holds to all orders, and what it confirms', 'VOROS', VOROS,
     'and to all orders in n, {Sn} has the asymptotic expansion (24).'),
    ('VOROS -- (26), the RH-false alternative, blowing up exponentially', 'VOROS', VOROS,
     'which gives oscillations that blow up exponentially with n.'),
    ('VOROS -- the height a violating zero can be signalled up to', 'VOROS', VOROS,
     'can only reliably signal a zero violating RH up to a height'),
    ('VOROS -- the detection index, n greater than about 10^18', 'VOROS', VOROS,
     'they could only be detected by'),
    ('VOROS -- Bombieri-Lagarias Cor 1(c), quoted inside Voros', 'VOROS', VOROS,
     'In [2, Cor. 1(c)], rather weak exponential lower bounds'),
    ('VOROS -- the numerical agreement is inconclusive regarding RH', 'VOROS', VOROS,
     'Yet the above numerical agreeme nt is inconclusive'),
    ('VOROS -- the general case: (15) under GRH, or (18) otherwise', 'VOROS', VOROS,
     'either (15) if the generalized Riemann Hypothesis (GRH)'),
    ('VOROS -- the counting-function hypothesis (16)', 'VOROS', VOROS,
     'N(T ) = 2T [2R−2(logT − 1) +R−1] +δN(T ), δN (T ) = O(T α ) for T → +∞ (16)'),
    ('VOROS -- Lagarias mod O(sqrt n log n) under GRH', 'VOROS', VOROS,
     'obeys (15) mod O(1) unconditionally (thm 5.1), then that Sn =O(√ n logn) under GRH'),

    # ---- LAGARIAS (S2), THE RECORD'S OWN PIN, RE-VERIFIED --------------------------------------------
    ('LAGARIAS -- the abstract: an unconditional formula IN TERMS OF THE ZEROS', 'LAGARIAS', LAG,
     'We derive an unconditional asymptotic formula for the coe'),
    ('LAGARIAS -- and the closed asymptotic, ASSUMING the Riemann hypothesis', 'LAGARIAS', LAG,
     'zeros of L(s,π ). Assuming the Riemann hypothesis for L(s,π ), we deduce that'),
    ('LAGARIAS -- Theorem 5.1, the archimedean part, unconditional', 'LAGARIAS', LAG,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representationπ onGL(N )'),
    ('LAGARIAS -- Theorem 5.1s hypothesis on n and its K(pi)', 'LAGARIAS', LAG,
     'the quantities S∞(n,π ) are real-valued. There is a constant K(π) such that for n ≥K(π) there'),
    ('LAGARIAS -- Theorem 6.1, the finite-place part', 'LAGARIAS', LAG,
     'Theorem 6.1. For any irreducible cuspidal (unitary) automorphic repres entation on GL(N )'),
    ('LAGARIAS -- and 6.1s BOUND requires the Riemann hypothesis', 'LAGARIAS', LAG,
     'in which the implied constant in the O-notation depends on π. If the Riemann hypothesis holds'),
    ('LAGARIAS -- the decomposition the record already carries', 'LAGARIAS', LAG,
     'In §5 we obtain an unconditional asymptotic formula for the arch imedean contribution'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b358 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b358_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e)[:150])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n, differs=bool(differs)))
        rec('')
        rec('  [%-9s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b358_extract_notes', LINES)
    io.open(d('b358_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
