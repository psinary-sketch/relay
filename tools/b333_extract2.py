# -*- coding: utf-8 -*-
"""b333_extract2.py -- THE SECOND EXTRACT STEP: THE QUOTATIONS THE DIAGNOSIS RESTS ON, AT THEIR EMITTING FILES.

### ### The derivation tool printed `MISMATCH`; the diagnosis of that word rests on WHICH FUNCTION each
### banked number was computed for. ### Every sentence the bank uses for that is located here first --
### b320's tool building its own function before either route runs, b320's bank naming that function, the
### atlas's bank carrying the bump's own archimedean channel, this act's registration pairing the two, the
### derivation tool's verdict line as printed. ### b283's law, again: located at its emitting file and its
### line before it is written anywhere else. ### The first extract file is not rewritten.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b333_extract2_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


REG = d('b333_registration_2026-09-06.txt')

WANTED = [
    # ### ---- b320's table: the function it was made for, at the tool that made it
    ("b320_corroborate -- the function the table was made for, built before either route runs", t('b320_corroborate.py'), 'g = SM.mean_zero_variant(a)'),
    ('### its autocorrelation', t('b320_corroborate.py'), 'f = SQ.autocorrelation(g)'),
    ('### the (38) route applied to it', t('b320_corroborate.py'), 'w = WE.weil(f)[0]'),
    ('### the digamma route applied to it', t('b320_corroborate.py'), 'A = digamma_side(f, U=U, ker=K)'),
    ('### the digamma route re-forms the kernel at its own grid, not the atlas\'s', t('b320_corroborate.py'), "atlas's grid was built for the atlas's test function."),
    ('b320 bank -- the function is the autocorrelation', d('b320_the_lawful_function.txt'), 'product is the autocorrelation `f(v) = INT g(u) g(u-v) du`'),
    ("b320 bank -- the sign certified, the size not", d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    # ### ---- the bump as a test function, and the atlas's own banked channel for it
    ('b317 -- the corpus bump as a test function', t('b317_smear.py'), "return TestFunction('corpus bump a=%g' % a, v, w,"),
    ("atlas bank -- the bump's archimedean channel at a = 1.3", d('carto_atlas.jsonl'), '"a": 1.3, "zero": 0.2065114708720861, "pole": 2.002722246159938, "arch": -1.7962126389496489'),
    ('### at a = 3', d('carto_atlas.jsonl'), '"a": 3.0, "zero": -0.020016'),
    ('atlas -- the channel is formed for the bump', t('e16/carto_atlas.py'), 'v, w = bump(a)'),
    # ### ---- this act's own sealed pairing, and the tool's verdict as printed
    ('registration (E) -- the route on the bump', REG, "precision, on the bump re-implemented from the atlas's definition"),
    ("### the bar's comparators", REG, "banked values read from b320's table."),
    ('### the values the bar expected', REG, 'magnitude at every cell (the values run from `0.5` to `8.8`).'),
    ('### the registration orders a disagreement reported first', REG, 'A DISAGREEMENT IS REPORTED AT FULL PROMINENCE, FIRST.'),
    ('### F3 as sealed', REG, "the bank's verdict equals the tool's, and if not `DERIVES-ON-IMPORT` it is the"),
    ('derive run -- the verdict as printed', d('b333_derive_run.txt'), 'VERDICT : MISMATCH at (L3)'),
    ('### the chain\'s own verdict as printed', d('b333_derive_run.txt'), 'DERIVES-ON-IMPORT'),
    # ### ---- b332: the rule the re-rank runs under
    ('b332 -- the sealed rule', d('b332_registration_2026-09-06.txt'), "constituent's rank is its softest grade among its owners, ordered"),
    ('### K5 in the statement', t('b332_statement.py'), "('K5', 'the archimedean distribution',"),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b333_extract2.py -- THE SECOND EXTRACT STEP. ### THE QUOTATIONS THE DIAGNOSIS RESTS ON, AT THEIR EMITTING FILES.')
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
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
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
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
