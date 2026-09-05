# -*- coding: utf-8 -*-
"""b328_extract.py -- THE EXTRACT STEP FOR THE DISCRIMINATING FAMILY. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The four-term sum at an off-line quadruple, as b326 wrote
### it and as the corpus's closure tool forms it; the conventions the seeds must obey (the involution,
### the two moments, the class test); the library's first off-line zero and its on-line neighbours; the
### ledger row and the trail this act updates. ### b283's law: every quotation located at its emitting
### file and its line before it is written anywhere else; the gate suite pulls its needles from THIS file.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b328_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


WANTED = [
    # ### ---- b326: the four-term sum, the family finding, the seed priced
    ('b326 -- the off-line pair\'s contribution on g conv g^#', d('b326_the_reach.txt'), 'an off-line pair contributes'),
    ('### the sign condition b326 named', d('b326_the_reach.txt'), 'for a seed whose transform does not change sign between'),
    ('### the family that could see it', d('b326_the_reach.txt'), 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN'),
    ('### the seed priced, not built', d('b326_the_reach.txt'), 'A seed that changes sign there is'),
    ('### the first banked pair refined to a point', d('b326_the_reach.txt'), 'rho = 0.953260475 + 16.290215720 i'),
    ('### the four complex terms at a = 3', d('b326_the_reach.txt'), 'f~(0.953260 + 16.290216 i) = +8.577524e-03 + 9.590412e-03 i'),
    ('### the arc\'s verdict', d('b326_the_reach.txt'), "TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT"),
    ('### the entailment b326 left', d('b326_the_reach.txt'), 'IT IS A TEST THIS FAMILY CANNOT FAIL'),
    ('### the aimed family, positive', d('b326_the_reach.txt'), 'NEGATIVE THAN THE ARC\'S, NOT LESS'),
    # ### ---- b321: the pole term, the balance as minus the zero side, the off-line zero as what breaks it
    ('b321 -- the pole term vanishes for a lawful f', d('b321_the_window_opened.txt'), 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
    ('### P = f~(0) + f~(1)', d('b321_the_window_opened.txt'), 'P = f-tilde(0) +'),
    ('### the balance collapses to minus the zero side', d('b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z'),
    ('### Z is a sum of squared moduli on the line', d('b321_the_window_opened.txt'), 'BECAUSE `f` IS A SQUARE'),
    ('### an off-line zero is what would break it', d('b321_the_window_opened.txt'), 'A ZERO OFF THE LINE IS EXACTLY WHAT WOULD BREAK IT'),
    # ### ---- b320: the class test, Definition 3.1
    ('b320 -- Definition 3.1 applied', d('b320_the_lawful_function.txt'), '`f-hat >= 0` pointwise'),
    ('### the class test can fail', d('b320_the_lawful_function.txt'), 'A CLASS TEST EVERYTHING PASSES IS NOT ONE'),
    ('### the two vanishing conditions hold by construction', d('b320_the_lawful_function.txt'), 'they are built into the corpus\'s mean-zero seed by'),
    # ### ---- the tools: conventions
    ('b318 -- the square is the source\'s g conv g^', t('b318_square.py'), "THE SOURCE'S `g conv g^`"),
    ('### its transform is |f-hat|^2', t('b318_square.py'), 'transform is `|f-hat|^2`'),
    ('### the class test is a scan of f-hat', t('b318_square.py'), 'So the test is a scan of `f-hat` and nothing cleverer'),
    ('b317 -- the two moments', t('b317_smear.py'), 'INT f d*rho = 0'),
    ('### and eq. (54) for an even test function', t('b317_smear.py'), 'the single condition `INT w(v) cosh(v/2) dv = 0`'),
    ('b321_window -- the half-line normalization and f^#', t('b321_window.py'), 'f^#(x) = x^{-1} f(1/x) = x^{-1/2} w(-log x)'),
    ('### the two prime routes agree only for even w', t('b321_window.py'), 'THEY ARE THE SAME NUMBER ONLY IF `w` IS EVEN'),
    ('b326_closure -- f~(rho) as the tool forms it', t('b326_closure.py'), 'f~(rho) = INT w(v) e^{(rho - 1/2) v} dv'),
    ('### the four terms of a quadruple, as the tool sums them', t('b326_closure.py'), 'for rho in (complex(beta, gam), complex(beta, -gam), complex(1 - beta, gam), complex(1 - beta, -gam)):'),
    ('b326_windows -- the places sides as the tool forms them', t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1'),
    ('### the sign certified through the gate', t('b326_windows.py'), 'certified = (verdict == NF.RESOLVED) and abs(value) > SIGN_MARGIN * drift'),
    ('### the derived Epstein kernel', t('b326_windows.py'), '2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)'),
    ('b326_windows -- the aimed family, cos-modulated bumps', t('b326_windows.py'), 'multiplied by `cos(omega v)`'),
    # ### ---- the libraries
    ('the first off-line zero, at the library', d('b326_epstein_zeros.json'), '0.9532604747946607'),
    ('### its ordinate', d('b326_epstein_zeros.json'), '16.290215720390393'),
    ('### the on-line neighbour below', d('b326_epstein_zeros.json'), '14.630459532385498'),
    ('### the on-line neighbour above', d('b326_epstein_zeros.json'), '18.82849120037208'),
    ('### the completeness census: seventeen', d('b326_offline.json'), '"total_winding": 17'),
    # ### ---- the ledger and the trail this act updates
    ('the faces ledger\'s Epstein row', os.path.join(PP, 'FACES_LEDGER.md'), '| F7 | F7 -- the Epstein negative control'),
    ('### its owed bridge', os.path.join(PP, 'FACES_LEDGER.md'), 'OWED -- `W-ORD-DISCRIMINATING-FAMILY` (pair F1-F7)'),
    ('the trail on OPEN_TRAILS', os.path.join(PP, 'OPEN_TRAILS.md'), '| **2** | `W-ORD-DISCRIMINATING-FAMILY` | **CONSTRUCTION** |'),
    ('b327 named this act next', d('b327_the_faces_ledger.txt'), 'THE DISCRIMINATING-FAMILY ACT IS NAMED NEXT BY THE ORDER'),
]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b328_extract.py -- THE DISCRIMINATING FAMILY. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(ROOT, '<relay>').replace('\\', '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
