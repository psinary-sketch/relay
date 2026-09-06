# -*- coding: utf-8 -*-
"""b336_extract.py -- THE EXTRACT STEP FOR THE COST CENSUS. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### Every row of the faces ledger at its id (the cost is typed from
### each row's own cells); the four prices the record has, at their emitters -- the unit's domain factor (b322),
### the exponent's ratio (b321), the instrument's act count (b321_run's imports), the crossing widths (b328,
### b334); the pole-constant relation between the Li and positivity faces where the record states it (b327's
### bank, the fold at FINDINGS); the b334 chart's sign column and the bank's threshold sentence for the
### phase-rule addendum; the writer's two entry points; the ledger's column law; the sortie ferry's leg-1
### sentences. ### b283's law: every quotation located at its emitting file and its line before it is
### written anywhere else.
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

NOTES = os.path.join(D, 'b336_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FERRY = d('b336_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the ledger: every row at its id, and the column law
    ('ledger -- the column law', LEDGER, '**THE COLUMN LAW.** `id`'),
] + [('### row %s' % r, LEDGER, '| %s | %s -- ' % (r, r)) for r in ('R1', 'R2', 'R3', 'R4', 'R5', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'L1', 'S1')] + [
    ("### b328's update block", LEDGER, '<!-- b328 update -->'),
    ("### b334's update block", LEDGER, '<!-- b334 update -->'),
    # ### ---- the four prices
    ("b322 -- the unit's domain factor", d('b322_the_membership.txt'), '### ### **`3.104e+02`.** ### **THAT IS AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS'),
    ('### the domain reached and required', d('b322_the_membership.txt'), '### ### **`X = 3.973e+04`**, against the ### **`X = 128`** ### this act reached -- a factor of'),
    ('### the price computed as b321 priced the exponent', d('b322_the_membership.txt'), 'THE PRICE, COMPUTED AS b321 PRICED THE EXPONENT.'),
    ("b321 -- the exponent's ratio", d('b321_the_window_opened.txt'), 'than either lies to the equality: they are apart by between one twenty-fourth and one fifth of'),
    ('### the table at a = 1.3', d('b321_the_window_opened.txt'), '    1.3    0.158889558      0.157908477      0.000981080    0.023223882      PASSES'),
    ('### the table at a = 1.41', d('b321_the_window_opened.txt'), '    1.41   0.221284108      0.217290580      0.003993528    0.018807781      PASSES'),
    ("b321_run -- the instrument's acts, imported", t('b321_run.py'), 'import b316_instrument as INS'),
    ('### b317', t('b321_run.py'), 'import b317_smear as SM'),
    ('### b318', t('b321_run.py'), 'import b318_square as SQ'),
    ('### b319', t('b321_run.py'), 'import b319_stable as ST'),
    ('### b320', t('b321_run.py'), 'import b320_weil as WE'),
    ('### b321', t('b321_run.py'), 'import b321_window as WI'),
    ('b328 -- the crossing widths', d('b328_family_run.txt'), "**VERDICT : SEES IT** at [('E', 40.0), ('E', 81.0), ('E', 160.0), ('O', 20.0), ('O', 40.0), ('O', 81.0), ('O', 160.0)]"),
    ('b334 -- the crossing region', d('b334_the_aim_map.txt'), 'THE EPSTEIN CROSSING REGION -- THE NEGATIVE CONTROL CHARTED -- IS THREE AIMS:'),
    ('### its members', d('b334_the_aim_map.txt'), '16.290216)` with `places_q = +0.655053`, `(a = 81, gamma = 16.290216)` with `+1.362830`, and `(a = 81,'),
    # ### ---- the pole-constant relation, where the record states it
    ('b327 -- the pole-at-zero constant', d('b327_the_faces_ledger.txt'), 'the archimedean place PLUS the pole-at-zero constant -- *"log s"* in the keystone\'s own split,'),
    ('### the source\'s words', d('b327_the_faces_ledger.txt'), '*"a contribution from the pole at s = 0"* in the source. ### The gamma-factor part IS the'),
    ('### the fold: one distribution, the pole constant 1', FINDINGS, 'The deposit\u2019s archimedean channel is the archimedean distribution on the Li family plus the pole constant `1`; the two margins are two'),
    ('### row L1 carries the derivation', LEDGER, 'gives \u03bb_A(n) = S\u221e(n) + 1 for every n \u2265 1 -- the gamma factor is exactly the source\'s archimedean term and `log s` is exactly the source\'s pole constant.'),
    # ### ---- the phase rule and the chart's sign column
    ('b334 bank -- the threshold rule is not the sign condition', d('b334_the_aim_map.txt'), 'THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.'),
    ('### negative only between 45 and 135', d('b334_the_aim_map.txt'), 'quadruple\'s term `4 |G|^2 cos 2 phi` is negative only between `45` and `135` degrees. ### By the sealed'),
    ("b334 chart -- the sign column", d('b334_chart_run.txt'), "(* = the phase exceeds 45 deg at that beta: REACHED ; the trailing sign is the quadruple's term S_4 = 4 |G|^2 cos 2 phi, negative only between 45 and 135 degrees)"),
    ('### the counts', d('b334_chart_run.txt'), 'aims REACHED by the sealed rule 270 ; of these with a NEGATIVE quadruple term (discriminating) 170 ; REACHED with a POSITIVE term (the phase past 135 deg) 100'),
    ('b328 bank -- the rule as b328 stated it', d('b328_the_discriminating_family.txt'), 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE**;'),
    # ### ---- the writer
    ('the writer -- write_row', t('b327_faces_row.py'), 'def write_row(row):'),
    ('### append_block', t('b327_faces_row.py'), 'def append_block(mark, body_lines):'),
    ('### the rows are never rewritten', t('b327_faces_row.py'), 'above are never rewritten; an UPDATE to a row is a block that names the row."""'),
    # ### ---- the sortie ferry, leg 1
    ('the sortie -- leg 1', FERRY, 'LEG 1 (b336) \u2014 THE COST CENSUS: a typed cost column on the'),
    ('### one grade', FERRY, 'one grade would take (read / import / derivation / construction'),
    ('### the prices', FERRY, "/ measurement) with the record's price where it has one (the"),
    ('### the pole-constant row', FERRY, 'the pole-constant relation between the Li and positivity faces'),
    ('### STATED, cost zero', FERRY, 'added as its own row (STATED, cost zero); the b328 phase-rule'),
    ('### no grade moved', FERRY, "chart's sign column cited). No grade moved."),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b336_extract.py -- THE COST CENSUS. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
