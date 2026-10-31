# -*- coding: utf-8 -*-
"""b726, (R336)(7): THE MECHANISM TABLE, W-ORD-MECHANISM-TABLE (OPEN_TRAILS :16589), FROM THE BANKS, NO COMPUTATION. Each figure is read at its bank and
line before anything is written; a miss refuses the table. The one literature row reads its sources at data/b726_beurling_read.txt, written by the
Write tool from the three papers read this act. Writes data/b726_mechanisms.txt alone.

  python -X utf8 tools/b726_mechanisms.py dry | bank"""
import os
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(T), 'data')
OUT = os.path.join(D, 'b726_mechanisms.txt')
NL = '\n'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

READS = [('b723_c2_closed_form.txt', 21, 'log(Z_Q / 2) = log zeta_K - S + log cosh S'), ('b723_c2_closed_form.txt', 32, 'for Re s > 1'),
         ('b723_c2_closed_form.txt', 70, 'NOT COMPILED'), ('b723_c2_closed_form.txt', 70, '19 ROWS OF 19'),
         ('b725_interference.txt', 31, 'zeta_K(rho) = Z_Q1(rho) = -2 L(rho, psi) (FORCED)'), ('b725_interference.txt', 106, 'Z_Q1 EXCLUDES 0 AT 69'),
         ('b725_interference.txt', 104, 'HELD'), ('b725_registration_2026-10-30.txt', 159, '69 certified off-line zeros to height 445'),
         ('b709_grid.txt', 441, 'a = 6.838396011'), ('b709_grid.txt', 4501, 'a = 10.38532711'),
         ('b675_hypotheses.txt', 67, 'FAILS (Davenport-Heilbronn, above t = 150)'), ('b705_contour.txt', 37, "DAVENPORT-HEILBRONN'S ZEROS BEYOND Re s = 1"),
         ('b705_contour.txt', 39, 'with Re ρ > 1 above t = 150'), ('b710_r5_controls.txt', 110, 'theorem dh_witness'),
         ('b725_dial.txt', 4, 'G_c(s) = zeta(s + c/2) zeta(s - c/2)'), ('b725_dial.txt', 33, 'a = 3.039966598'), ('b725_dial.txt', 35, 'a = 2.888826162'),
         ('b725_dial.txt', 37, 'a = 2.772588722'), ('b725_dial.txt', 40, 'REFUTED'), ('b725_dial.txt', 39, '0.4120'),
         ('b726_beurling_read.txt', 8, 'no additive structure or functional equation'), ('b726_beurling_read.txt', 10, 'Re s = β'),
         ('b726_beurling_read.txt', 16, 'a criterion'), ('b726_beurling_read.txt', 23, 'NO INSTANCE FOUND')]

ROWS = [
    ('CLASS-GROUP AVERAGING', 'the Epstein zetas, class numbers 2 and 3; Davenport-Heilbronn cited as the same mechanism',
     'kept: functional equation, Ramanujan size, the integers` additive structure. dropped: the Euler product.',
     'Z_Q averages over the class group, and its zeros are where the averaged terms cancel. h = 2: log(Z_Q / 2) = log zeta_K - S + log cosh S for Re s > 1 (data/b723_c2_closed_form.txt :21, :32; a derivation, NOT COMPILED, checked POST HOC 19 of 19, :70), the off-line zeros where zeta_K does not vanish being those of cosh S read through the continuation. h = 3: at a zero of Z_Q0, zeta_K = Z_Q1 = -2 L(s, psi) (data/b725_interference.txt :31), H-INTERFERENCE HELD, Z_Q1 excluding 0 at 69 of 69 (:104, :106).',
     'the 69 certified off-line zeros of Z_Q0 to height 445, x^2 + xy + 6y^2 (data/b725_registration_2026-10-30.txt :159). Davenport-Heilbronn: zeros with Re rho > 1 above t = 150 (data/b675_hypotheses.txt :67; data/b705_contour.txt :37-:39), cited, not computed here; the kernel`s witness SIDE-kernel v1.8 dh_witness (data/b710_r5_controls.txt :110).',
     'Q0`s two onsets: a = 6.838396011 and 10.38532711, so 6.84 to 10.39 (data/b709_grid.txt :441, :4501).'),
    ('SIZE', 'zeta(s + c/2) zeta(s - c/2), the frame of zeta(s) zeta(s - c), at c = 0.6, 0.8, 1.0',
     'kept: an Euler product, a functional equation. dropped: Ramanujan size.',
     'the shift moves each factor`s zeros off the product`s centre line by c/2: off the line by construction, at every zero of zeta (data/b725_dial.txt :4).',
     'each zero rho of zeta gives zeros at rho + c/2 and rho - c/2; the frame`s lowest ordinate gamma_0 is the banked instance (:4).',
     'a = 3.039966598, 2.888826162, 2.772588722 at c = 0.6, 0.8, 1.0, so 2.77 to 3.04 (data/b725_dial.txt :33, :35, :37). H-DIAL`s constant product REFUTED (spread 0.4120, :39-:40): no law of c is read from them.'),
    ('ADDITIVE STRUCTURE', 'Beurling generalized-prime systems',
     'kept: an Euler product. dropped: the integers` additive structure. A functional equation: NO INSTANCE FOUND in the sources read.',
     'the prime system itself is chosen, and the cited constructions choose it so that the zeros fall where they are placed (data/b726_beurling_read.txt :9, :13). Why additive structure would exclude this is not read here.',
     'NO INSTANCE FOUND of a Beurling system carrying a functional equation with a zero off its centre line, sources read at data/b726_beurling_read.txt. Cited without a functional equation: Broucke-Debruyne, Appendix A, zeros at rho_k = beta + i gamma_k, on the line Re s = beta, theta < beta < 1 (:9-:10). There is no centre line for that zero to be off, so the row`s mechanism stands at that weaker instance.',
     'none banked.'),
]


def main(mode):
    for bank, line, needle in READS:
        t = open(os.path.join(D, bank), encoding='utf-8').read().replace('\r', '').split(NL)
        if needle not in t[line - 1]:
            sys.exit('### data/%s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (bank, line, needle))
    L = ['b726 -- (R336)(7): THE MECHANISM TABLE, W-ORD-MECHANISM-TABLE, FROM THE BANKS, NO COMPUTATION (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### by tools/b726_mechanisms.py; every figure below read at its bank and line before composition (%d reads, all as wanted).' % len(READS),
         '### THE SCOPE: this table lists the mechanisms the record and the cited literature show, and asserts nothing about zeta.',
         '### Each onset row is a record of what was read at that family. That onsets differ between rows is an observation, POST HOC, not a law (FINDINGS.md :11797).', '']
    for i, (m, fam, ing, mech, inst, ons) in enumerate(ROWS, 1):
        L += ['## ROW %d -- %s' % (i, m), '  FAMILY:      ' + fam, '  INGREDIENTS: ' + ing, '  MECHANISM:   ' + mech, '  INSTANCE:    ' + inst, '  ONSET:       ' + ons, '']
    L += ['## THE ORDER: W-ORD-MECHANISM-TABLE stays OPEN for its fourth row.', '',
          '### ### **THE MECHANISM TABLE: 3 ROWS ; READS %d OF %d AS WANTED ; THE BEURLING INSTANCE WITH A FUNCTIONAL EQUATION: NO INSTANCE FOUND ; ASSERTS NOTHING ABOUT ZETA ; THE ORDER OPEN.**' % (len(READS), len(READS))]
    print(NL.join(L))
    if mode == 'bank':
        with open(OUT + '.tmp', 'wb') as f:
            f.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(OUT + '.tmp', OUT)
        print('written data/b726_mechanisms.txt')


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') not in ('dry', 'bank'):
        sys.exit(__doc__)
    main(sys.argv[1])
