# -*- coding: utf-8 -*-
"""b345_extract.py -- THE EXTRACT STEP FOR THE LI CONTROL, RE-RUN. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The prior leg's sealed bar and its unmet verdict; the rule its own
### diagnosis named for the tail panel, quoted from that bank and from that diagnostic's record, so that this act's
### tail rule is fixed before any value by the record and not by memory; the prior leg's two route implementations at
### their lines, so that this act's second route can be shown to share no code with the first; the kernel's formula at
### its emitter; the prior leg's certifications lists, to be listed again as it listed them; the keystone's tabulated
### indices and the deposit's proven finite-range positivity at its scope; the bridge row and the sentence it is to
### carry; the sortie ferry's leg-1 sentences and (L1). ### b283's law: every quotation located at its emitting file
### and its line before it is written anywhere else.
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

NOTES = os.path.join(D, 'b345_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


B340 = d('b340_the_li_family_control.txt')
DIAG = d('b340_diagnose_run.txt')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
KEY = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
FERRY = d('b345_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the prior leg's bar, its verdict, and the rule its diagnosis named
    ('b340 -- the verdict as sealed', B340, 'THE VERDICT AS SEALED: THE DIFFERING CONSTITUENT -- A QUADRATURE FAILURE, THE GATE REFUSING THE SEALED'),
    ('### the sealed bar, both clauses', B340, '### identity `|I(n) + 1 - lambda_A(n)| <= 1e-9 max(1, |lambda_A|)`, and the drift between the two sealed'),
    ('### the drift that failed it', B340, '### the `u` route by Gauss-Legendre drifts from the theta route by `6.797e-07` at `n = 1`, growing as `n^2`'),
    ('### THE RULE THE DIAGNOSIS NAMED', B340, '### the tail differs by `0.0115` between the rules); the same `u` route by tanh-sinh meets the sealed bar'),
    ('### the sealed refinement, not the identity, failed', B340, '### REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.'),
    ("### the diagnostic's reading, in its own record", DIAG, '  ### READING: the sealed refinement route (Gauss-Legendre on an infinite panel with a logarithmic tail) is what failed, and not the identity; the bar as sealed is NOT MET and is not rewritten.'),
    ('### the tail carries the drift', DIAG, '  ### THE DRIFT LIVES IN THE TAIL PANEL UNDER THE GAUSS-LEGENDRE RULE at every diagnosed index : True'),
    ('### tanh-sinh meets the bar', DIAG, '  ### THE u ROUTE BY TANH-SINH (the same substitution, the other rule) MEETS THE SEALED BAR AGAINST THE THETA ROUTE at every diagnosed index : True'),
    # ### ---- the prior leg's identity, and its columns
    ('b340 -- the identity within the bar at all 22', B340, "### `1.86e-212` -- within the bar at all 22 indices, worst `7.47e-26`; the pole constant `L_n[log s]`, carried"),
    ('### the pole constant its own column', B340, '### as its own column, is `1` at every index to `1.42e-39`; b327\'s identity `lambda_A = S_inf + 1` against'),
    ("### the keystone's column reproduced", B340, '### to its rounding, worst `4.57e-10` (at `n = 100`, where the column carries eleven digits after the'),
    ('### which certifications apply', B340, '### ### **WHICH CERTIFICATIONS APPLY:** the kernel identity (b333), a property of the kernel; the arrangement'),
    ('### which do not', B340, "### method. ### **WHICH DO NOT:** Theorem 1's inequality and the Sonin margin (defined on the class only --"),
    ('### not in the lawful class', B340, '### ### **(4) THE LI TEST FUNCTIONS ARE BUILT, AND THEY ARE NOT IN THE LAWFUL CLASS:** ### `g_n(x) = SUM_j C(n,j)'),
    # ### ---- the prior leg's two routes, at their lines, so a disjoint second route can be shown to be one
    ("b340's tool -- the theta route", t('b340_li_control.py'), '    """### (1/4pi) INT_0^pi [1 - (-1)^n cos n theta] h_+(u(theta)) sec^2(theta/2) dtheta, u = tan(theta/2)/2; tanh-sinh on 4n+4 panels."""'),
    ('### the u route it sealed', t('b340_li_control.py'), '    """### (1/pi) INT_0^inf Re G_n(1/2 + iu) h_+(u) du on panels at the phase multiples; Gauss-Legendre."""'),
    ('### its kernel evaluator', t('b340_li_control.py'), '    """### the derived kernel, b326\'s kernel_zeta formula: Re psi(1/4 + iu/2) - log pi."""'),
    ('### its closed form on the line', t('b340_li_control.py'), '    """### Re G_n(1/2 + iu) = 1 - (-1)^n cos(2n arctan 2u), in the stable form 2 sin^2 / 2 cos^2."""'),
    ("b326 -- the kernel's formula at its emitter", t('b326_windows.py'), '        _KCACHE[key] = (np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U])'),
    # ### ---- the deposit's side: the indices, the certificate, the bench's sentence
    ('the keystone -- the table head', KEY, '| n | \u03bb_A(n) | \u03bb_Z(n) | margin \u03bb_n | agree digits |'),
    ('### n = 1', KEY, '| 1 | \u22120.554119955935 | 0.577215664902 | **0.0230957089661** | 258 |'),
    ('### the margin positive to 300', KEY, '**The margin M(n) = \u03bb_A(n) + \u03bb_Z(n) = \u03bb_n nevertheless stays positive throughout 1 \u2264 n \u2264 300**'),
    ('the monograph -- the certificate at its scope', MONO, "partialPositivity_finiteRange` (v0.8.0) certifies \u03bb_n \u2265 0 for n up to Voros's detection threshold N\u2080(T) \u2248 2T\u00b2, with the on-line term's nonnegativity proved"),
    ('the bench -- an instrument, not an argument', BENCH, 'print("respects (Keiper 1992; BALANCE_AND_POSITIVITY sec V). This is an instrument, not an argument.")'),
    # ### ---- the bridge row and the sentence it is to carry
    ('the ledger -- the bridge row L1', LEDGER, '| L1 | L1 -- the Li-to-Weil bridge: the Li coefficients as the Weil functional on the Li test family'),
    ("b327 -- one distribution on two families", d('b327_the_faces_ledger.txt'), '### ### ### **ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.**'),
    ('### the family lies outside the class', d('b327_the_faces_ledger.txt'), 'function whose inverse Mellin transform has no compact support, so the Li family lies outside'),
    # ### ---- b344's printed figures for the two axes it did NOT move, which this act's closing files as priceable
    ('b344 -- the two held axes, printed at every rung', d('b344_the_floor_priced.txt'), "### later act can price them without re-running this one: the cut's `tau = 1.0e-06` in force, with `2`"),
    ('### the eigenvalues either side, and the smallest kept', d('b344_the_floor_priced.txt'), "### of the sandwich's eigenvalues inside a decade either side of it at every rung, the smallest kept"),
    ('### one axis moved is one axis moved', d('b344_the_floor_priced.txt'), '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ("### b344's own ladder tool, which printed them", t('b344_ny.py'), 'def held_axes(st):'),
    ('the trails ledger -- the owed-bridges table head', os.path.join(PP, 'OPEN_TRAILS.md'), '| | trail | species | what is owed | price, as the record states it | trigger |'),
    ('### an appended trail update, the shape to follow', os.path.join(PP, 'OPEN_TRAILS.md'), '<!-- b328 trail update -->'),
    ('### nothing here is a route', os.path.join(PP, 'OPEN_TRAILS.md'), '*Nothing here is a route. No grade moves. h2 stands exactly where the deposit left it.*'),
    # ### ---- the sortie ferry, leg 1
    ('the sortie -- leg 1', FERRY, 'LEG 1 (b344) \u2014 THE LI CONTROL, RE-RUN: the prior leg\'s bar is'),
    ('### the tail rule fixed before any value', FERRY, 'with the tail'),
    ('### the two routes share no code', FERRY, 'required to share no code. Then: the identity at the tabulated'),
    ('### the two verdicts', FERRY, 'Verdicts: (FOURTH CONTROL HOLDS \u2014 the'),
    ('### the bridge row updated', FERRY, 'The faces ledger\'s bridge row'),
    ('### (L1)', FERRY, 'The navigator\'s expectations: (L1) the control HOLDS under the'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b345_extract.py -- THE LI CONTROL, RE-RUN. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
