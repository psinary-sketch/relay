# -*- coding: utf-8 -*-
"""b334_extract.py -- THE EXTRACT STEP FOR THE AIM-MAP. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The sign conventions as the derivation just banked them (b333),
### never from a seat; the like-for-like rule (b333's species); the discriminating seed's construction, its
### threshold and its widths (b328); the windows' channels, the places convention, the derived Epstein kernel
### and the certification gate (b326); the identity that makes the margin minus the remainder integral, the
### remainder's single eps evaluator and its reach (b321, b313f); the square on the stable cut, its frames and
### Theorem 1's support condition (b318, b319, b317, b320); the stated clause's K5 and K6 and the sealed rule
### (b332); the ledger's rows S1 and F7 and b328's update block; the findings anchor and the b333 addendum;
### the ferry's three expectations at their lines. ### b283's law: every quotation located at its emitting
### file and its line before it is written anywhere else.
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

NOTES = os.path.join(D, 'b334_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


B333 = d('b333_the_archimedean_term_derived.txt')
B328 = d('b328_the_discriminating_family.txt')
B326 = d('b326_the_reach.txt')
B321 = d('b321_the_window_opened.txt')
B320 = d('b320_the_lawful_function.txt')
FERRY = d('b334_ferry_2026-09-06.txt')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

WANTED = [
    # ### ---- the sign conventions, from the derivation just banked
    ("b333 -- the corpus's A is the source's W_inf", B333, "**THE CORPUS'S `A(f)` IS THE SOURCE'S `W_inf(f) = -W_R(f)`**,"),
    ('### entering (148) in the orientation the calibration fixed', B333, "entering (148) as `pole + W_inf - PRIME`, the orientation the calibration fixed (b315: *\"IT CHOOSES"),
    ("### the atlas's own sign line", t('e16/carto_atlas.py'), 'sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH'),
    ("### the places convention", t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1, places_q_b325=PRq - Aq325,'),
    # ### ---- the like-for-like rule, b333's species
    ("b333 -- the like-for-like diagnosis", B333, "`tools/b333_diagnose.py` (`data/b333_diagnose_run.txt`), like for like:"),
    ('### E1, the defect the rule answers', B333, 'E1 -- THE SEALED BAR PAIRED THE BUMP WITH A TABLE MADE FOR ANOTHER FUNCTION.'),
    ('### the aim-map named as next', B333, 'THE AIM-MAP IS NAMED AS NEXT, ITS TARGET THE NEW SOFTEST PAIR; NEITHER IT NOR THIS ACT IS THE DISCHARGE.'),
    ('### the (150) route, importable', t('b333_diagnose.py'), 'def w150_in_v(v, w, refine=1):'),
    # ### ---- the discriminating seed: construction, threshold, widths, the exception
    ("b328 -- the even seed's construction", t('b328_family.py'), 'phi0 = _bump_on(V, a) * np.sin(GAMMA1 * np.abs(V))'),
    ('### the threshold', t('b328_family.py'), 'THRESHOLD_DEG = 45.0'),
    ('### lawfulness by the source\'s definition', t('b328_family.py'), "(L1) Definition 3.1 on f = g conv g^#, by b318's scan; (L2) the pole conditions on the seed and P."),
    ('### the aim quoted from the library', t('b328_family.py'), "BETA1, GAMMA1 = LIB['offline'][0]['rho_a']"),
    ('b328 bank -- negative past forty-five degrees', B328, 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE**;'),
    ('### the phases at the registered widths', B328, "the sine-aimed seed's phase at the zero is `88.10, 88.67, 89.21, 89.39` degrees at `a = 20, 40, 81,"),
    ('### E20, the narrowest even cell', B328, 'THE ONE CELL THAT DOES NOT SEE IT IS THE NARROWEST EVEN ONE**, `E20`'),
    ('### sees it at seven of eight', B328, 'SEES IT -- AT SEVEN OF EIGHT CELLS.**'),
    ('b328 registration -- the widths', d('b328_registration_2026-09-05.txt'), '`a in {20, 40, 81, 160}`, `L = log a`, so `delta L = 1.358,'),
    ('### the phase bar', d('b328_registration_2026-09-05.txt'), '`|phi| > 45 deg` there; the odd seed iff `|phi_o| < 45 deg`.'),
    # ### ---- the windows: channels, the derived Epstein kernel, the gate, the u-grid
    ("b326 -- the derived Epstein kernel", t('b326_windows.py'), '`2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)`'),
    ('### the certification', t('b326_windows.py'), 'certified = (verdict == NF.RESOLVED) and abs(value) > SIGN_MARGIN * drift'),
    ('### the u-grid', t('b326_windows.py'), 'du = min(0.1, 0.2 / max(L, 1e-9)) / refine'),
    ('### the gate', t('noise_floor.py'), 'def classify(value, refined=None, floor=DEFAULT_FLOOR, drift_bar=DEFAULT_DRIFT_BAR,'),
    ('### the drift bar', t('noise_floor.py'), 'DEFAULT_DRIFT_BAR = 1e-3'),
    ('b326 bank -- no crossing at this reach', B326, 'CELLS.** ### **NO CROSSING AT THIS REACH.** ### The finite side rises to `0.453` at `a = 32`'),
    ('### the ceiling', B326, 'Epstein, with every located off-line zero, at twenty-one of twenty-one below the ceiling and at'),
    ('### the representation numbers', t('b325_epstein.py'), 'def rep_counts(K=KMAX):'),
    # ### ---- the identity, the remainder, its one evaluator and its reach
    ("b321 -- the margin is minus the remainder", B321, "that makes b320's margin exactly minus the remainder integral."),
    ('### the prime sum inside the margin, at the ladder', B321, 'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER.**'),
    ('### the domain axis drifting', B321, 'domain values are ### **DRIFTING.** ### So this act certifies the SIZE of the remainder integral'),
    ('### the remainder integral', t('b321_window.py'), "def remainder_integral(f, mod=EF, route='uniform', n=None):"),
    ('### one implementation of (84)', t('b321_window.py'), 'There is exactly one implementation of (84) in this corpus.'),
    ('### the eps evaluator', t('e16/b313f_qeps_layer.py'), 'def eps(rho, NQ=700, NG=400):'),
    # ### ---- the square, the frames, the support condition
    ('b318 -- the square as a sum of squares', t('b318_square.py'), 'def square_trace(fr, sub, f, block=None):'),
    ("### Theorem 1's support condition", t('b318_square.py'), 'SUPPORT_G_HI = math.sqrt(2.0)            # ### Theorem 1 / (3): supp g inside [2^-1/2, 2^1/2]'),
    ('### the stable cut', t('b319_stable.py'), 'def stable_subspace(fr, tau=TAU, T=None):'),
    ('### the reference frame', t('b317_smear.py'), 'REFERENCE = '),
    ('### the grid axis', t('b317_smear.py'), 'GRID_AXIS = '),
    ('b320 bank -- the sign certified, the size not', B320, "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    # ### ---- the stated clause: K5, K6, the rule
    ('b332 -- K5', t('b332_statement.py'), "('K5', 'the archimedean distribution',"),
    ('### K6', t('b332_statement.py'), "('K6', 'the decomposition: the compressed square plus the remainder',"),
    ('### the sealed rule', d('b332_registration_2026-09-06.txt'), "constituent's rank is its softest grade among its owners, ordered"),
    ('### the re-rank: the pair', d('b333_rerank_run.txt'), 'THE AIM-MAP IS NAMED AS NEXT; ITS TARGET IS THE NEW SOFTEST: K5 and K6.'),
    # ### ---- the ledger and the findings
    ('ledger -- row S1', LEDGER, '| S1 | S1 -- the clause stated:'),
    ('### row F7', LEDGER, "| F7 | F7 -- the Epstein negative control at b326's result"),
    ("### b328's update block", LEDGER, '<!-- b328 update -->'),
    ("### b333's update block", LEDGER, '<!-- b333 update -->'),
    ('findings -- the anchor', FINDINGS, '<a id="clause-stated"></a>'),
    ('### the b333 addendum', FINDINGS, '<!-- b333 addendum: the archimedean term derived -->'),
    # ### ---- the order's expectations, at their lines
    ('the ferry -- (F1)', FERRY, 'here: (F1) for \u03b6 the prime sum stays inside the margin at'),
    ('### (F2)', FERRY, 'every aim at this reach; (F2) the Epstein crossing region'),
    ('### (F3)', FERRY, "contains its banked off-line zeros' aims; (F3) K5 and K6"),
    ('### the shadow', FERRY, 'ordered. THE SHADOW: expected nothing; say so.'),
    ('### the next act named', FERRY, 'censuses; the cost census named as next (a typed cost column'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b334_extract.py -- THE AIM-MAP. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
