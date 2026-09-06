# -*- coding: utf-8 -*-
"""b343_extract.py -- THE EXTRACT STEP FOR THE MAP'S NEXT REACH. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The executor's draft's component 2 and its component 3 (what a finer chart
### says and does not); b334's narrowest points at both reaching widths and its (F1); b334's grid, its like-for-like
### comparator and its gate; the frames' axes -- which of them moves the rank and which does not; the stable cut and the
### square; the remainder integral with its two conventions and the erratum's standing clause that a banked value is
### quotable only with its convention named; b339's floor, which this leg's second component bears on; the sortie
### ferry's leg-5 sentence. ### b283's law: every quotation located at its emitting file and its line before it is
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

NOTES = os.path.join(D, 'b343_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


DRAFT = d('b342_executor_draft_2026-09-06.txt')
B334, B339 = d('b334_the_aim_map.txt'), d('b339_the_exponent_resolved.txt')
CHART = d('b334_chart_run.txt')
ERR = os.path.join(PP, 'ERRATA.md')
FERRY = d('b343_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the executor's draft, components 2 and 3
    ("the draft -- component 2", DRAFT, "COMPONENT 2 \u2014 THE MAP'S NEXT REACH: the aim-map at the two heights the"),
    ('### the narrowest heights named', DRAFT, 'chart named narrowest (\u03b3 = 4 at both reaching widths, where the'),
    ('### the finer grid between 2 and 8', DRAFT, 'archimedean term and the prime sum nearly cancel) on a finer height grid'),
    ('### the same two routes and the gate', DRAFT, 'between 2 and 8, with the same two routes and the gate, the crossing of'),
    ('### the crossing looked for, its absence or presence stated', DRAFT, 'A_z \u2212 PR_z through zero looked for and its absence or presence stated;'),
    ("### the residual's growth with the square's rank", DRAFT, "and the identity residual's growth with the square's rank at one aimed"),
    ('### the reference against the two larger grid-axis frames', DRAFT, 'seed (the reference frame against the two larger grid-axis frames),'),
    ('### a measurement of the instrument, not of the theorem', DRAFT, 'stated as a measurement of the instrument and not of the theorem.'),
    ('### component 3, a finer chart is a finer chart', DRAFT, 'COMPONENT 3 \u2014 WHAT IT SAYS AND DOES NOT: the modules bind nothing; a'),
    ("### it prices K6's instrument and moves no grade", DRAFT, "finer chart is a finer chart; the residual's rank behaviour prices K6's"),
    ("### the draft's expectations", DRAFT, 'censuses. The navigator\'s expectations: (F1) A_z \u2212 PR_z stays positive'),
    ('### (F2) the residual grows with rank', DRAFT, 'on the finer grid; (F2) the residual grows with rank. Registration'),
    # ### ---- b334: the narrowest points, the grid, (F1)
    ('b334 -- the narrowest point at a = 40', CHART, '  reaching  a = 40    : A_z - PR_z smallest at gamma = 4.000000 : +0.000577751 [-]'),
    ('### at a = 81', CHART, '  reaching  a = 81    : A_z - PR_z smallest at gamma = 4.000000 : +0.000507481 [-]'),
    ('### the narrowest-points heading', CHART, '  ### (F-b) THE NARROWEST POINTS -- the height at which the prime sum comes closest to the room, per leg and width.'),
    ('### b334 (F1) MET', B334, '### ### **THE NAVIGATOR\'S (F1): MET. THIS SEAT\'S (F1): MET.**'),
    ("### b334's sealed grid", t('b334_aimmap.py'), 'GAMMAS = (4.0, 8.0, 12.0, 14.134725, 16.290215720390393, 20.0, 25.0, 29.551761098629115, 33.650101, 40.0,'),
    ('### the reaching widths', t('b334_aimmap.py'), 'REACHING = (40.0, 81.0)'),
    ('### the like-for-like comparator', t('b334_aimmap.py'), '    """### the only comparison in this file; it raises when the two sides name different functions."""'),
    ('### the gate at two resolutions', t('b334_aimmap.py'), 'def gate(name, v1, v4):'),
    ('### the four quantities per aim', t('b334_aimmap.py'), 'def quantities(s, lam_z, lam_q, lamq_diff):'),
    ('### the aimed seed', t('b334_aimmap.py'), 'def seed_aimed(gamma, a):'),
    ('### the reference and grid frames', t('b334_aimmap.py'), 'FRAME_GRID = tuple(SM.GRID_AXIS[2])   # ### (8192, 32, NY): rank constant against the reference'),
    # ### ---- the axes: which moves the rank and which does not
    ('b317 -- the grid axis', t('b317_smear.py'), 'GRID_AXIS = ((2048, 32.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('### the domain axis', t('b317_smear.py'), 'DOMAIN_AXIS = ((1024, 8.0, NY_FIXED), (2048, 16.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('### NY fixed', t('b317_smear.py'), 'NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing'),
    ('b319 -- both cuts from one SVD', t('b319_stable.py'), 'def both_subspaces(fr, tau=TAU, T=None):'),
    ('b318 -- the square', t('b318_square.py'), 'def square_trace(fr, sub, f, block=None):'),
    # ### ---- the remainder and its two conventions; the standing clause
    ('b321 -- the remainder integral', t('b321_window.py'), "def remainder_integral(f, mod=EF, route='uniform', n=None):"),
    ('### the source exponent', t('b321_window.py'), 'import b313f_qeps_layer as EF       # noqa: E402  ### the SOURCE exponent  (rho ** +0.5)'),
    ("### the corpus's banked exponent", t('b321_window.py'), "import b313r_qeps_layer as ER       # noqa: E402  ### the corpus's banked exponent (rho ** -0.5)"),
    ('ERRATA -- quotable only with its convention named', ERR, 'is quotable only with its convention named.'),
    # ### ---- b339's floor, which this leg bears on
    ("b339 -- the floor, and what the next pricing must price", B339, '### floor is what the next pricing must price; its origin (the fixed `NY = 512`, the cut\'s `tau`, the'),
    ('### the limit above both candidates', B339, '### limit reading (R2) applied to the five frames the record already holds -- the margin\'s descent'),
    ('### the verdict unaffordable', B339, '### ### **(1) THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.** ### No'),
    # ### ---- the sortie ferry, leg 5
    ('the sortie -- leg 5', FERRY, "LEG 5 (b343) \u2014 THE MAP'S NEXT REACH: the finer height grid"),
    ('### between 2 and 8 at both reaching widths', FERRY, 'between 2 and 8 at both reaching widths at the narrowest room,'),
    ("### and the residual's growth with the square's rank", FERRY, "and the identity residual's growth with the square's rank at one"),
    ('### a finer chart is a finer chart', FERRY, 'finer chart is a finer chart.'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec("b343_extract.py -- THE MAP'S NEXT REACH. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.")
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
