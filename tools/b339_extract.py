# -*- coding: utf-8 -*-
"""b339_extract.py -- THE EXTRACT STEP FOR THE EXPONENT RESOLVED. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The two exponent candidates at their emitters (the source's `rho ** +0.5`
### and the corpus's `rho ** -0.5`, one character apart in two copies); b321's ladder of the identity residual along
### the domain axis and its table of the two copies' separation at the covered cells; b322's sealed resolving-power
### rule -- the price is the ratio, the fit is a least-squares slope, a price is not a prediction -- and its fitter;
### b323's two rates; the frames' axes and the fixed NY; the stable cut and the square; the convention erratum's
### standing clause; the sortie ferry's leg-1 sentences and the navigator's (L1). ### b283's law: every quotation
### located at its emitting file and its line before it is written anywhere else.
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

NOTES = os.path.join(D, 'b339_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


B321, B322, B323 = d('b321_the_window_opened.txt'), d('b322_the_membership.txt'), d('b323_the_fold.txt')
FERRY = d('b339_ferry_2026-09-06.txt')
ERR = os.path.join(PP, 'ERRATA.md')

WANTED = [
    # ### ---- the two candidates, one character apart
    ("b321_window -- the source exponent", t('b321_window.py'), 'import b313f_qeps_layer as EF       # noqa: E402  ### the SOURCE exponent  (rho ** +0.5)'),
    ("### the corpus's banked exponent", t('b321_window.py'), "import b313r_qeps_layer as ER       # noqa: E402  ### the corpus's banked exponent (rho ** -0.5)"),
    ('### the source copy, its line', t('e16/b313f_qeps_layer.py'), 'out[k] = float((lam2 / (1 - lam2) * (r ** 0.5) * I).sum())'),
    ("### the corpus copy, its line", t('e16/b313r_qeps_layer.py'), 'out[k] = float((lam2 / (1 - lam2) * (r ** -0.5) * I).sum())'),
    ('### one implementation of (84)', t('b321_window.py'), 'There is exactly one implementation of (84) in this corpus.'),
    ('### the remainder integral', t('b321_window.py'), "def remainder_integral(f, mod=EF, route='uniform', n=None):"),
    # ### ---- b321: the ladder and the separation
    ("b321 -- the ladder's head", B321, 'rank     frame    Tr (square)        margin W - Tr      residual to -INT'),
    ('### frame 1', B321, '    20       1        7.725767619        1.055446382        0.896556824'),
    ('### frame 5', B321, '    262      5        8.599100561        0.182113440        0.023223882'),
    ('### the other two cells', B321, 'The same shape at `a = 1.35` (`0.671666 ... 0.020793`) and at `a = 1.41` (`0.524907 ... 0.018808`).'),
    ("### the separation table's head", B321, 'a      source copy      corpus copy      apart by       from equality    corpus?'),
    ('### a = 1.3', B321, '    1.3    0.158889558      0.157908477      0.000981080    0.023223882      PASSES'),
    ('### a = 1.35', B321, '    1.35   0.186481766      0.184544767      0.001936999    0.020792865      PASSES'),
    ('### a = 1.41', B321, '    1.41   0.221284108      0.217290580      0.003993528    0.018807781      PASSES'),
    ('### the corpus copy passes too', B321, 'THE ANSWER IS NO. ### THE CORPUS COPY PASSES THE SAME ARMS AT 3 OF 3 CELLS.'),
    ('### the two quadratures a limit', B321, '### these arms buy is a quadrature limit and the act calls it that.'),
    # ### ---- b322: the sealed resolving-power rule and its fitter
    ('b322 -- the rule: the price is the ratio', B322, 'PRICE IS THE RATIO.**'),
    ('### the rule stated', B322, 'THE RESOLVING-POWER RULE: ### A QUESTION IS UNDER-RESOLVED, NOT OPEN, WHEN THE'),
    ('### the incident that bought it', B322, "THE INCIDENT THAT BOUGHT IT WAS b321's, ONE ACT AGO."),
    ('### the price computed as b321 priced the exponent', B322, 'THE PRICE, COMPUTED AS b321 PRICED THE EXPONENT.'),
    ('### a price is not a prediction', B322, 'A PRICE IS NOT A PREDICTION.**'),
    ('### an extrapolation labelled as one', B322, 'IT IS AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS ONE.'),
    ("### the unit's fitted rate", B322, "the unit's residual        : ### **`p = -0.519901`** ### (fit rms `0.0543`)"),
    ('### the fitter', t('b322_ladder.py'), 'def fit_power(xs, ys):'),
    ('### least squares for log y', t('b322_ladder.py'), 'LEAST SQUARES FOR `log y = A + p log x`. ### RETURNS `(p, A, rms)`.'),
    ('b323 -- the two rates', B323, "rate is now known: the instrument's own residual falls as `X^-1.324` while the unit's falls as"),
    # ### ---- the frames, the cut, the square
    ('b317 -- the domain axis', t('b317_smear.py'), 'DOMAIN_AXIS = ((1024, 8.0, NY_FIXED), (2048, 16.0, NY_FIXED), (4096, 32.0, NY_FIXED),'),
    ('### NY fixed', t('b317_smear.py'), 'NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing'),
    ('b316 -- the frame', t('b316_instrument.py'), 'def __init__(self, N, X, NY=None):'),
    ('b319 -- the stable cut', t('b319_stable.py'), 'def stable_subspace(fr, tau=TAU, T=None):'),
    ('### both cuts from one SVD', t('b319_stable.py'), 'def both_subspaces(fr, tau=TAU, T=None):'),
    ('b318 -- the square', t('b318_square.py'), 'def square_trace(fr, sub, f, block=None):'),
    # ### ---- the convention erratum
    ('ERRATA -- the convention entry', ERR, "## E-2026-09-03-1 \u2014 The archimedean remainder's normalization convention is the corpus's own, not the source's (INTERNAL RECORD"),
    ('### its standing clause', ERR, 'THE STANDING CLAUSE THIS ENTRY IMPOSES, AND IT TRAVELS WITH THE RECORD RATHER THAN WITH ANY ACT\'S MEMORY:'),
    ('### quotable only with its convention named', ERR, 'is quotable only with its convention named.'),
    ('### the partition places it internal', ERR, '- `E-2026-09-03-1` \u2014 *INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED*'),
    # ### ---- the sortie ferry, leg 1
    ('the sortie -- leg 1', FERRY, 'LEG 1 (b339) \u2014 THE EXPONENT RESOLVED: price the domain the'),
    ('### the price against the separation', FERRY, "(the trace's measured convergence rate against the candidates'"),
    ('### if the price fits', FERRY, "if the price fits one act's ceiling, run the remainder under"),
    ('### by two routes', FERRY, 'both conventions at that domain on the stable-rank subspace, by'),
    ('### the three verdicts', FERRY, 'prefers \u2014 (RESOLVED, the convention named, its consequence for'),
    ('### the sealed rule governs', FERRY, 'bar moved; the sealed rule from b322 governs.'),
    ("### the navigator's (L1)", FERRY, 'by ls-remote; the hook and mirror where the papers repo moves;'),
    ('### (L1) stated', FERRY, 'navigator\'s expectations, registered here: (L1) the price fits'),
    ('### and the identity prefers the source', FERRY, "and the identity prefers the source's convention; (L2) the"),
    ('### the wave parked', FERRY, "ruling of this day and not named as next anywhere."),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b339_extract.py -- THE EXPONENT RESOLVED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
