# -*- coding: utf-8 -*-
"""b340_extract.py -- THE EXTRACT STEP FOR THE LI FAMILY CONTROL. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The pinned source's Li class and its special test functions (3.2), its
### Theorem 3.1 (the Weil norm of `G_n`), its Lemma 4.2 (`lambda_n = S_inf - S_f + delta`, the archimedean term
### `SUM C(n,j) tau_{j-1}`) and its (4.11); the deposit's channel as its keystone and bench define it (`f_A`, the Li
### map, the tabulated column and its indices); b327's derived map `lambda_A(n) = S_inf(n) + 1` and its corroboration,
### the fourth control as b327 priced it; the derived kernel at its emitters (b326's `kernel_zeta`, b333's identity
### `h_+ = 2 Re (log Gamma_R)'`); the explicit formula's arrangement `Z = P - PR + A` (b321); the lawful class's three
### conditions (b320); the finite-range certificate at its scope (the monograph, the R4 row); the noise-floor gate;
### the sortie ferry's leg-2 sentences and (L2). ### b283's law: every quotation located at its emitting file and
### its line before it is written anywhere else.
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

NOTES = os.path.join(D, 'b340_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def p(n):
    return os.path.join(PP, n)


SRC = d('b327_source_text.txt')
B327, B321, B320, B333, B336 = d('b327_the_faces_ledger.txt'), d('b321_the_window_opened.txt'), d('b320_the_lawful_function.txt'), d('b333_the_archimedean_term_derived.txt'), d('b336_the_cost_census.txt')
KEY = p(os.path.join('phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md'))
BENCH = p(os.path.join('internal', 'bench', 'li_bench.py'))
LEDGER = p('FACES_LEDGER.md')
MONO = p(os.path.join('day1', 'A_Place_to_Stand.md'))
FERRY = d('b340_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the source, pinned by b327 (arXiv:math/0404394v4, sha256 86f3d3c4...)
    ('the source -- the Li class', SRC, 'We de\ufb01ne the Li class L of test functions to be the set of rational functions in the fu nction'),
    ('### vanishing at infinity, poles in {0, 1}', SRC, '\ufb01eld C(s) that vanish at in\ufb01nity (on the Riemann sphere) and whose pol ar divisor is contained'),
    ('### the special test functions (3.2)', SRC, 'The special test functions Gn(s) \u2208 L corresponding to the Li coe\ufb03cients are'),
    ('### Theorem 3.1', SRC, 'Theorem 3.1. Let\u03c0 be an irreducible cuspidal unitary automorphic representation of GL(N ),'),
    ('### (3.4) the Weil norm', SRC, 'W(\u03c0) =\u03bbn(\u03c0) +\u03bb\u2212n(\u03c0) = 2 \u211c(\u03bbn(\u03c0)). (3.4)'),
    ('### Weil positivity for a particular test function', SRC, 'Weil\u2019s quadratic functional for a particular test function gn(x).'),
    ('### Lemma 4.2', SRC, 'Lemma 4.2. Let\u03c0 be an irreducible cuspidal automorphic representation on GL(N ) over Q.'),
    ('### (4.6)', SRC, '\u03bbn(\u03c0) = S\u221e(n,\u03c0 ) \u2212Sf (n,\u03c0 \u2228) +\u03b4(\u03c0), (4.6)'),
    ('### (4.7) the archimedean term', SRC, '\u03c4j\u22121(\u03c0\u2228) (4.7)'),
    ('### delta = 1 at the trivial representation', SRC, 'and \u03b4(\u03c0) = 1 if \u03c0 =\u03c0triv and \u03b4(\u03c0) = 0 otherwise.'),
    ('### the archimedean primes', SRC, 'In the expression (4.6) the term S\u221e(n,\u03c0 \u2228) corresponds to the contribution of the archimedean'),
    ('### (4.11)', SRC, '2j )\u03b6 \u2217(j), (4.11)'),
    ('### zeta*(1)', SRC, 'in which \u03b6 \u2217(j) = \u03b6(j) for j \u2265 2, and \u03b6 \u2217(1) = log(4\u03c0) +\u03b3, where \u03b3 is Euler\u2019s constant. For the'),
    # ### ---- the deposit's channel: the keystone and the bench
    ("the keystone -- the split", KEY, 'f_A(s) = log s + log\u0393(s/2) \u2212 (s/2)\u00b7log \u03c0  (archimedean)'),
    ('### the Li map per channel', KEY, 'then \u03bb(n) = n\u00b7\u03a3_{j=1..n} C(n\u22121, j\u22121)\u00b7\u03b7_j per channel, and \u03bb_n = \u03bb_A(n) + \u03bb_Z(n)'),
    ('### the margin', KEY, '**The channels and the margin.** M(n) := \u03bb_Z(n) + \u03bb_A(n) = \u03bb_n is the margin in the inequality \u03bb_Z(n) \u2265 \u2212\u03bb_A(n).'),
    ('### the table head', KEY, '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'),
    ('### n = 1', KEY, '| 1 | \u22120.554119955935 | 0.577215664902 | **0.0230957089661** | 258 |'),
    ('### n = 8, the sign change', KEY, '| 8 | **+0.0208999330276** | 1.44485574412 | 1.46575567715 | 257 |'),
    ('### n = 130', KEY, '| 130 | 170.196427671 | 2.27351901152 | 172.469946682 | 215 |'),
    ('### the margin positive to 300', KEY, '**The margin M(n) = \u03bb_A(n) + \u03bb_Z(n) = \u03bb_n nevertheless stays positive throughout 1 \u2264 n \u2264 300**'),
    ('### the sharpest form', KEY, '*The bench is an instrument. The premise remains open, and the honest form of the joint is the one this keystone already carries: RH \u27fa \u03bb_Z(n) \u2265 \u2212\u03bb_A(n) for every n.*'),
    ('the bench -- f_A', BENCH, '    return mp.log(s) + mp.loggamma(s / 2) - (s / 2) * mp.log(mp.pi)'),
    ('### the Li map', BENCH, 'Li coefficients:  lambda_n = n * sum_{j=1..n} C(n-1, j-1) * eta_j,'),
    ('### an instrument, not an argument', BENCH, 'print("respects (Keiper 1992; BALANCE_AND_POSITIVITY sec V). This is an instrument, not an argument.")'),
    # ### ---- b327: the map derived and corroborated; the fourth control priced
    ('b327 -- the derivation (d)', B327, '### ### **`lambda_A(n) = S_inf(n) + 1`**, and `lambda_Z(n) = -S_f(n)`.'),
    ('### the corroboration', B327, "`mpmath.zeta`. ### Worst `|lambda_A(n) - S_inf(n) - 1|` at `n <= 30`: **`1.33e-251`**, bar `1e-20`,"),
    ('### question one', B327, "### the archimedean place PLUS the pole-at-zero constant -- *\"log s\"* in the keystone's own split,"),
    ('### the distribution both channels evaluate', B327, "archimedean term, and the distribution it evaluates is `2 Re(Gamma_R'/Gamma_R)` on the line, the"),
    ('### the Li family outside the class', B327, "function whose inverse Mellin transform has no compact support, so the Li family lies outside"),
    ('### the fourth control priced', B327, '### ### **THE FOURTH CONTROL, PRICED AND NOT RUN:** ### the explicit formula closed on the Li family'),
    ('### the third route named', B327, "`S_inf(n) - S_f(n) + 1`, with `S_inf` by a third route, the atlas's kernel against `G_n` on the"),
    ('### the u-tail registered first', B327, "line; its conditionally convergent `u`-tail and the `O(n log T / T)` zero tail bounded and"),
    ("b327's bridge tool -- route B", t('b327_bridge.py'), "def s_inf_closed(n):"),
    ('### the bench definitions executed from its file', t('b327_bridge.py'), 'def load_bench_definitions():'),
    # ### ---- the derived kernel, the arrangement, the class, the gate
    ('b326 -- the kernel on this grid', t('b326_windows.py'), 'def kernel_zeta(U):'),
    ('### its formula', t('b326_windows.py'), "        _KCACHE[key] = (np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U])"),
    ("b333 -- the corpus's A is the source's W_inf", B333, "### `tau = 0.5, 3, 17`, worst `1.972e-31`. ### **THE CORPUS'S `A(f)` IS THE SOURCE'S `W_inf(f) = -W_R(f)`**,"),
    ('### h_+ twice the real part', B333, '### ### **(2) THE FACTOR-OF-TWO HAZARD IS ONE IDENTITY.** ### `h_+` is twice the real part of the'),
    ('b321 -- the arrangement', B321, '### and the identity is ### **`Z = P - PR + A`**.'),
    ('### the channels', t('b321_window.py'), '    return dict(zero=Z, pole=P, arch=A, prime=PR,'),
    ("b320 -- Theorem 1's three conditions", B320, "### ### 1.41.** ### Theorem 1 asks three things of the seed. ### **THE SUPPORT CONDITION IS THE ONLY"),
    ('### the support', B320, '### ### ONE THAT BITES**: `supp g` inside `[2^-1/2, 2^1/2]`, i.e. `a <= 1.414213562`. ### The two'),
    ('### the vanishing conditions', B320, '### vanishing conditions, `g-hat(0) = 0` and `g-hat(i/2) = 0`, hold at ### **EVERY** ### cell to'),
    ('the ledger -- Definition 3.1 quoted', LEDGER, 'Definition 3.1: *"positive de\ufb01nite when its Fourier transform is pointwise positive"*'),
    ('### row R4, the certificate', LEDGER, "PROVED, the finite range: *\"`partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2"),
    ('### the pair F1-L1, owed', LEDGER, '| F1\u2013L1 | OWED | `W-ORD-LI-FAMILY-CONTROL`. The finite-instance identity is closed on the arc\'s family (F1) and not on the Li family;'),
    ('the monograph -- the certificate at its scope', MONO, "partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2, with the on-line term's nonnegativity proved"),
    ('the noise-floor gate', t('noise_floor.py'), 'def classify(value, refined=None, floor=DEFAULT_FLOOR, drift_bar=DEFAULT_DRIFT_BAR,'),
    ("b336 -- F1's price", B336, "record prices the step: F1, F2, F7, S1."),
    # ### ---- the sortie ferry, leg 2
    ('the sortie -- leg 2', FERRY, 'LEG 2 (b340) \u2014 THE LI FAMILY CONTROL: the Li test functions'),
    ('### the pole constant carried', FERRY, "own normalization (b327's map, the pole constant carried"),
    ('### not in the lawful class, say so', FERRY, '(they are NOT in the lawful class \u2014 say so, and state which of'),
    ('### the measurement', FERRY, 'derived kernel set against the deposit\'s archimedean channel of'),
    ("### b327's identity as the bar", FERRY, '\u2014 the identity of b327 as the bar; the deposit\'s proven finite-'),
    ('### the two verdicts', FERRY, 'values. A fourth control if it holds; the differing constituent'),
    ('### (L2)', FERRY, 'fourth control holds with the pole constant carried; (L3) the'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b340_extract.py -- THE LI FAMILY CONTROL. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
