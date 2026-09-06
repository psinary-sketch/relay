# -*- coding: utf-8 -*-
"""b333_extract.py -- THE EXTRACT STEP FOR THE ARCHIMEDEAN TERM DERIVED. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The classical archimedean term as the pinned source states it
### in its Appendix B -- (147) the Mellin transform, (148) the explicit formula, (150) the principal value,
### (151) the Gamma form, (152)-(153) the digamma kernel -- and (53) the functional; the corpus's own
### conventions at their owners (the bump, the transform `hhat`, `f-hat`, the atlas's kernel and channel,
### the sign of the explicit formula as the calibration fixed it); the two routes the record already has
### (b320's (38) route and its digamma route, their table); the factor-of-two hazard b326 found; the stated
### clause's K5 row and its ranking (b332). ### b283's law: every quotation located at its emitting file and
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

NOTES = os.path.join(D, 'b333_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


SRC = d('b328_source_text.txt')

WANTED = [
    # ### ---- the source, pinned: Appendix B
    ('source -- Appendix B gathers the normalizations', SRC, 'In this appendix, we gather di\ufb00erent sources on the normalization of the archimedean contri-'),
    ('### (147) the Mellin transform', SRC, 'fpxqxs\u00b41dx. (147)'),
    ('### the involution and (148)', SRC, 'Then, with f7pxq :\u201cx\u00b41fpx\u00b41q the explicit formula takes the form'),
    ('### (148)', SRC, 'Wvpfq, (148)'),
    ('### (149) the prime term', SRC, 'Wppfq\u201cp logpq'),
    ('### (150) the archimedean distribution as a principal value', SRC, 'WRpfq :\u201cp log 4\u03c0`\u03b3qfp1q`'),
    ('### (150) the subtracted term at the identity', SRC, 'fpxq` f7pxq\u00b4 2'),
    ('### (151) the Gamma form', SRC, 'WRpfq\u201cp log\u03c0qfp1q\u00b4 1'),
    ('### (151) closes', SRC, '\u02dcfpwqdw. (151)'),
    ('### the digamma form (152), W_inf = -W_R', SRC, 'In [6] and [8] a positivity result for the distribution W8 \u201c\u00b4 WR is proven'),
    ('### (152)', SRC, 'h`p\u03c4q \u02dcfpwqd\u03c4'),
    ('### (153) h_+', SRC, 'h`p\u03c4q\u201c\u00b4 log\u03c0` \u211cp\u03bbp1{4`i\u03c4{2qq, \u03bb pzq\u201c \u03931pzq{\u0393pzq. (153)'),
    ('### h_+ is the derivative of 2 theta', SRC, 'It is the derivative of 2 \u03b8p\u03c4q, where \u03b8 is the Riemann-Siegel angular function de\ufb01ned as'),
    ('### (53) the functional W_inf', SRC, 'fp\u03c1\u00b41q\u03c4p\u03c1qd\u02da\u03c1 (53)'),
    ('### W_R defined as a principal value', SRC, 'The distribution WR is then de\ufb01ned as a principal value.'),
    ('### the singularity at rho = 1', SRC, '\u03c1\u201c 1 and the use of a principal value in its de\ufb01nition.'),
    ('### W_R = -W_inf', SRC, 'namely the equality for the local term ( WR\u201c\u00b4W8)'),
    # ### ---- the pin
    ('b333 -- the pin re-verified', d('b333_source.txt'), 'local copies matching the pin, re-hashed now :'),
    ('### the text layer pinned', d('b333_source.txt'), 'sha256 588eb5ac022653bdffd9ba0b75ddc37c4832d736963d9753061279b36b985016'),
    # ### ---- the corpus's conventions, at their owners
    ('b321_window -- the explicit formula as the corpus reads (148)', t('b321_window.py'), '`SUM_rho f-tilde(rho) = INT f + INT f^# - SUM_v W_v(f)`'),
    ('### and (149)', t('b321_window.py'), '`W_p(f) = (log p) SUM_m ( f(p^m) + f^#(p^m) )`'),
    ('b318 -- f-hat', t('b318_square.py'), '`f-hat(t) = INT f(rho) rho^{-it} d*rho = INT w(v) e^{-itv} dv`'),
    ('### real for even w', t('b318_square.py'), 'For a REAL EVEN `w` this is `INT w(v) cos(t v) dv`, real.'),
    ('atlas -- the explicit formula sign', t('e16/carto_atlas.py'), 'sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH   [sign fixed BY the E2 calibration]'),
    ('### the bump', t('e16/carto_atlas.py'), 'w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))'),
    ('### normalized to unit mass', t('e16/carto_atlas.py'), 'w /= np.trapezoid(w, v)'),
    ('### hhat', t('e16/carto_atlas.py'), 'return np.cos(np.outer(u, v)) @ (w * dv)'),
    ('### the kernel', t('e16/carto_atlas.py'), 'Re psi(1/4 + i u/2) - log pi, cached.'),
    ('### the channel', t('e16/carto_atlas.py'), 'A = float(np.trapezoid(hhat(v, w, U) * kernel(U), U) / (2.0 * math.pi))'),
    ('b326_closure -- the closed-form transform', t('b326_closure.py'), 'INT w e^{c v} dv = -(1/c^2) SUM_j beta_j (e^{c v_{j+1}} - e^{c v_j})'),
    # ### ---- the two routes the record has
    ('b320_corroborate -- the digamma route', t('b320_corroborate.py'), '`A(f) = (1/2 pi) INT f-hat(u) [Re psi(1/4 + i u/2) - log pi] du`'),
    ('### the (38) route, a Hadamard integral', t('b320_corroborate.py'), 'source\'s (38) and (53): a real-side Hadamard integral with a principal-value constant measured'),
    ('### nothing in the path touches the Hadamard integral', t('b320_corroborate.py'), 'Nothing in this path touches the Hadamard integral, the split radius, or `C_R`.'),
    ('b320 -- the table head', d('b320_the_lawful_function.txt'), 'a      covered   W_inf by (38)      A by digamma       difference'),
    ('### a = 1.3', d('b320_the_lawful_function.txt'), '1.3    YES       8.781214000        8.781179663        3.434e-05'),
    ('### a = 3', d('b320_the_lawful_function.txt'), '3      no        0.506677452        0.506670618        6.834e-06'),
    ('### the worst difference', d('b320_the_lawful_function.txt'), 'WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS : 3.434e-05.'),
    ('### C_R measured', d('b320_the_lawful_function.txt'), '`C_R = 2.415093331442` at split radius `R = 1`'),
    ('b315 -- the term defined, no free constant', d('b315_the_calibration_and_the_rate.txt'), 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    ('### an explicit integral of the digamma kernel', d('b315_the_calibration_and_the_rate.txt'), '`A` is an explicit integral of the digamma kernel'),
    ('### the calibration chooses where A goes', d('b315_the_calibration_and_the_rate.txt'), 'IT DOES NOT SCALE `A`. ### IT DOES NOT SET `A`. ### IT CHOOSES WHERE `A` GOES.'),
    # ### ---- the sign chain and the factor-of-two hazard
    ('b321 -- the places sum is minus the zero side', d('b321_the_window_opened.txt'), '`SUM_v W_v(f) = - Z`.**'),
    ('b326 -- the halved kernel', d('b326_the_reach.txt'), 'Epstein archimedean kernel was ### **HALF** ### the derived'),
    ('### Gamma(s) against Gamma(s/2)', d('b326_the_reach.txt'), "zeta's archimedean unit; `Z_Q`'s factor is `(sqrt23/2pi)^s Gamma(s)`. ### `Gamma(s)` against"),
    ('b326_windows -- the derived Epstein kernel', t('b326_windows.py'), '`2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)`'),
    # ### ---- the stated clause's K5 and the ranking
    ('b332 -- the ranking', d('b332_the_clause_stated.txt'), '1. K5 (`DEFINED-ONLY`); 2. K6 (`MEASURED-AT-COVERED-CELLS`); 3. K1 and 4. K2'),
    ('### the reason in the rule', d('b332_the_clause_stated.txt'), 'THE REASON IS IN THE RULE AND NOT IN A JUDGEMENT:'),
    ('### the ledger row S1', os.path.join(PP, 'FACES_LEDGER.md'), '| S1 | S1 -- the clause stated:'),
    ('### the anchor', os.path.join(PP, 'FINDINGS.md'), '<a id="clause-stated"></a>'),
    ('### the K5 row in the section', os.path.join(PP, 'FINDINGS.md'), '| **K5** the archimedean distribution | defined at b315'),
    ('### the sealed rule', d('b332_registration_2026-09-06.txt'), "constituent's rank is its softest grade among its owners, ordered"),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b333_extract.py -- THE ARCHIMEDEAN TERM DERIVED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
