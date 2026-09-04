# -*- coding: utf-8 -*-
"""b325_extract.py -- THE EXTRACT STEP FOR THE NEGATIVE CONTROL.

### ### **WHAT THIS ACT IS READING FOR, AND WHY THE READS DECIDE THE PRICING.**
### The order asks whether the arc's instrument can be aimed at a hypothesis that ### **FAILS** ###
### -- the Epstein zeta of a class-number-3 form, which has a functional equation, no Euler product,
### and zeros off the critical line. ### **THE PRICING IS NOT A JUDGEMENT ABOUT DIFFICULTY. ### IT
### ### IS A CENSUS OF WHICH CONSTITUENTS THE CORPUS ALREADY OWNS**, and this file takes it.

### ### **AND ONE READ DECIDES MORE THAN THE REST.** ### The arc's `W_infinity` is built from
### Connes-Consani's (38) and (53), whose kernel is `Re psi(1/4 + i u/2) - log pi` -- and that kernel
### is ### **ZETA'S**, because it comes from zeta's archimedean factor `pi^{-s/2} Gamma(s/2)`.
### ### **THE EPSTEIN FUNCTION'S ARCHIMEDEAN FACTOR IS DIFFERENT**, and the corpus states it in its
### own emitting file. ### If it is different, the arc's archimedean distribution ### **DOES NOT
### ### TRANSFER**, and that is a BUILD rather than a re-run.

### ### **b283's LAW GOVERNS EVERY QUOTATION**, and for this act the emitters are the deposited
### confinement keystone, the internal residue keystone, and the corpus's own Epstein tools --
### `epstein_census.py`, which states the completed function's method in its header, and
### `epstein_li_v3.py`, which implements it.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b325_extract_notes.txt')
CENSUS_BANK = os.path.join(E16, 'epstein_census_bank.jsonl')

WANTED = [
    # ### ---- the deposited confinement keystone: the experiment and its result
    ('the experiment, subject B', os.path.join(DEPOSIT, 'Which_Structure_Confines.md'),
     'When the class number of Q exceeds 1'),
    ('### the theorem it rests on', os.path.join(DEPOSIT, 'Which_Structure_Confines.md'),
     'Davenport'),
    ('### and what it concludes', os.path.join(DEPOSIT, 'Which_Structure_Confines.md'),
     'One ingredient removed'),
    ('### and what the functional equation does NOT do',
     os.path.join(DEPOSIT, 'Which_Structure_Confines.md'), 'it does not confine zeros to it'),
    # ### ---- the internal residue keystone: the ledger, and which register it lives in
    ('the ledger called positive, and the form',
     os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'), 'positive ledger but RH false'),
    ('### and what the coherence functional therefore measures',
     os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'),
     'measures **ledger-positivity, not RH-truth**'),
    # ### ---- THE ARCHIMEDEAN FACTOR, at the corpus's own emitting file
    ('### ### THE COMPLETED EPSTEIN FUNCTION AND ITS ARCHIMEDEAN FACTOR',
     os.path.join(E16, 'epstein_census.py'), 'Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)'),
    ('### the incomplete-gamma representation it is evaluated by',
     os.path.join(E16, 'epstein_census.py'), 'a_k^-s Gamma(s,a_k)'),
    ('### the form, its discriminant and its class number',
     os.path.join(E16, 'epstein_census.py'), 'disc -23, principal form'),
    ('### and the census method, 2-D by construction',
     os.path.join(E16, 'epstein_census.py'), 'winding number of'),
    ('### the same completed function, implemented', os.path.join(E16, 'epstein_li_v3.py'),
     'a.gamma_upper(s)'),
    ('### and ZETA\'S, in the same file, for the contrast', os.path.join(E16, 'epstein_li_v3.py'),
     'def E_zeta_fl'),
    ('### the representation numbers, formed', os.path.join(E16, 'epstein_li_v3.py'),
     'x * x + x * y + 6 * y * y'),
    # ### ---- the arc's own archimedean kernel, for the comparison
    ("### THE ARC'S KERNEL -- ZETA'S, AT ITS EMITTING FILE",
     os.path.join(E16, 'carto_atlas.py'), 'def kernel'),
    ('### and the arc\'s prime channel, for the shape the finite side must take',
     os.path.join(E16, 'carto_atlas.py'), 'math.log(p)'),
]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b325_extract.py -- THE NEGATIVE CONTROL. ### THE READ, AND THE CENSUS OF WHAT IS OWNED.')
    rec('=' * 100)
    rec('  ### **THE PRICING IS A CENSUS OF CONSTITUENTS, NOT A JUDGEMENT ABOUT DIFFICULTY.**')
    rec('')

    rec('-' * 100)
    rec('### (A) THE QUOTATIONS, EACH AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('-' * 100)
    missing = 0
    for lbl, path, frag in WANTED:
        rec('')
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            missing += 1
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
            t = ln.strip()
            rec('    | line %-5d %s' % (n, t[:460]))
    rec('')
    rec('  ### ### **QUOTATIONS NOT FOUND : %d**' % missing)

    # ### ------------------------------------------------------------------ THE OWNED CENSUS
    rec('')
    rec('-' * 100)
    rec('### (B) THE ZERO LIBRARY THE CORPUS ALREADY OWNS. ### **COUNTED, NOT DESCRIBED.**')
    rec('-' * 100)
    if not os.path.exists(CENSUS_BANK):
        rec('  ### **THE CENSUS BANK IS NOT PRESENT -- HARD FAILURE**')
        missing += 1
    else:
        cells, selftest = [], []
        for ln in io.open(CENSUS_BANK, encoding='utf-8', errors='replace'):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            (cells if r.get('kind') == 'cell' else selftest).append(r)
        sig_lo = min(c['sig_lo'] for c in cells)
        sig_hi = max(c['sig_hi'] for c in cells)
        t_lo = min(c['t_lo'] for c in cells)
        t_hi = max(c['t_hi'] for c in cells)
        found = [c for c in cells if abs(c.get('wind', 0.0)) > 0.5]
        rec('  cells banked            : %d' % len(cells))
        rec('  self-test records       : %d  %s'
            % (len(selftest), selftest[0] if selftest else ''))
        rec('  sigma range covered     : [%.3f, %.3f]' % (sig_lo, sig_hi))
        rec('  t range covered         : [%.2f, %.2f]' % (t_lo, t_hi))
        rec('  ### ### **ZEROS FOUND (winding 1) : %d**' % len(found))
        for c in found:
            rec('      sigma in [%.3f, %.3f], t in [%.2f, %.2f], winding %.3f'
                % (c['sig_lo'], c['sig_hi'], c['t_lo'], c['t_hi'], c['wind']))
        rec('')
        rec('  ### ### **AND THE MEASUREMENT THAT PRICES THE RUN:** ### the census starts at')
        rec('  ### `sigma = %.3f`. ### **IT NEVER SCANNED THE CRITICAL LINE ITSELF, AND IT NEVER'
            % sig_lo)
        rec('  ### ### SCANNED `sigma < 1/2`.** ### The zeros it banks are all in the RIGHT half-')
        rec('  ### strip, which is what it was built for: it was looking for off-line zeros and it')
        rec('  ### found them. ### **SO THE CORPUS OWNS OFF-LINE ZEROS AND DOES NOT OWN THE ON-LINE')
        rec('  ### ### ONES**, and an explicit formula needs BOTH.')

    # ### ------------------------------------------------------------------ THE ARCHIMEDEAN SPLIT
    rec('')
    rec('-' * 100)
    rec('### (C) THE TWO ARCHIMEDEAN FACTORS, SIDE BY SIDE, FROM THE CORPUS\'S OWN FILES.')
    rec('-' * 100)
    rec('  ### **ZETA** ### -- `xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)`, deposited at the confinement')
    rec('  ### keystone and implemented at `epstein_li_v3.py: def E_zeta_fl`.')
    rec('  ###   its explicit-formula kernel, at `carto_atlas.py: def kernel` :')
    rec('  ###   ### **`Re psi(1/4 + i u/2) - log pi`**')
    rec('  ### **EPSTEIN (disc -23)** ### -- `Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)`, stated')
    rec('  ### in `epstein_census.py`\'s own METHOD header.')
    rec('  ###   its explicit-formula kernel, DERIVED from that factor at `s = 1/2 + i u` :')
    rec('  ###   ### **`Re psi(1/2 + i u) - log(2 pi / sqrt 23)`**')
    rec('  ### ### **THEY ARE DIFFERENT FUNCTIONS.** ### `Gamma(s/2)` against `Gamma(s)`, and')
    rec('  ### `log pi` against `log(2 pi / sqrt 23)`. ### **THE ARC\'S ARCHIMEDEAN DISTRIBUTION IS')
    rec('  ### ### ZETA\'S AND DOES NOT TRANSFER.** ### That is one BUILD, and it is small and')
    rec('  ### exactly specified -- but it is a build and not a re-run, and the pricing says so.')
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not missing else 5


if __name__ == '__main__':
    sys.exit(main())
