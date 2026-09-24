# -*- coding: utf-8 -*-
"""b509_kernel.py -- (R104)'S ACT 3 IN SIDE-explicit-formula. ### `python tools/b509_kernel.py compile | profile | statement | clauses`

### `compile`   -- `lake env lean -o <olean> SIDEExplicitFormula/B321Identity.lean` in the kernel, foreground; the
###                output banked verbatim, each run numbered by `run_clock` (`b509_compile_log*.txt`). ### A declaration
###                that fails elaborates with `sorryAx`: the exit code is printed and NOT read as the verdict.
### `profile`   -- `lake env lean data/b509_printaxioms.lean`: `#print axioms` on the new terminal and, as the
###                positive control, on `EF_lit_zetaZeroConfig` (b500 banked it as the standard three); the new
###                terminal's line MATCHED ON THE WHOLE STRING.
### `statement` -- the new terminal printed from its declaration line to its `:=`.
### `clauses`   -- Components 2 and 3: every clause's two sides QUOTED from their sources and each quote found
###                there before a verdict is printed; the family's regularity measured on the chain's own object.
"""
import io
import json
import math
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))
import run_clock  # noqa: E402
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MOD = os.path.join('SIDEExplicitFormula', 'B321Identity.lean')
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'B321Identity.olean')
PRINT = os.path.join(D, 'b509_printaxioms.lean')
NAME = 'SIDEExplicitFormula.B321.b321_identity'
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def lake(args, stem):
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean'] + args, cwd=KER, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    body = ['$ lake env lean ' + ' '.join(args), 'exit %d ; %.1f s' % (r.returncode, time.time() - t0), '--- stdout ---',
            r.stdout.rstrip(NL), '--- stderr ---', r.stderr.rstrip(NL)]
    path = run_clock.write(D, stem, body)
    print(NL.join(body))
    return r, path


def compile_():
    os.makedirs(os.path.join(KER, os.path.dirname(OLEAN)), exist_ok=True)
    r, p = lake(['-o', OLEAN, MOD], 'b509_compile_log')
    out = r.stdout + r.stderr
    print('### sorry mentioned : %s ; error lines : %d ; exit %d (NOT the verdict) ; banked : %s'
          % ('sorry' in out, sum(1 for l in out.split(NL) if ': error' in l), r.returncode, p))
    return 0


def profile():
    io.open(PRINT, 'w', encoding='utf-8', newline=NL).write(
        'import SIDEExplicitFormula.B321Identity\n\n#print axioms %s\n#print axioms Zeta23.WeilEF.EF_lit_zetaZeroConfig\n' % NAME)
    r, p = lake([PRINT], 'b509_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    new = [l for l in lines if l.startswith("'%s'" % NAME)]
    ctl = [l for l in lines if l.startswith("'Zeta23.WeilEF.EF_lit_zetaZeroConfig'")]
    res = dict(new=new, control=ctl, new_std3=(new == [STD3 % NAME]),
               control_std3=(ctl == [STD3 % 'Zeta23.WeilEF.EF_lit_zetaZeroConfig']),
               sorry=('sorryAx' in r.stdout), exit=r.returncode)
    io.open(os.path.join(D, 'b509_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### the new terminal, whole string : %s' % res['new_std3'])
    print('### the control, whole string      : %s' % res['control_std3'])
    return 0


def statement():
    src = io.open(os.path.join(KER, MOD), encoding='utf-8').read()
    i = src.index('theorem b321_identity')
    j = src.index(':=', i)
    st = src[i:j + 2]
    io.open(os.path.join(D, 'b509_statement.txt'), 'w', encoding='utf-8', newline=NL).write(st + NL)
    print(st)
    return 0


# ### ================================================================================================
# ### COMPONENTS 2 AND 3. ### Each side of each clause is a QUOTATION with its file; `clauses` finds every
# ### quotation in its file before printing any verdict, and refuses if one is missing.
# ### ================================================================================================
EFF = os.path.join(KER, 'Zeta23', 'ExplicitFormula.lean')
B321 = os.path.join(T, 'b321_window.py')
ATL = os.path.join(T, 'e16', 'carto_atlas.py')
CLO = os.path.join(T, 'b326_closure.py')
NEW = os.path.join(KER, MOD)
CLAUSES = [
    ('sign of Z', 'SAME', 'both put the zero side alone on the left',
     (NEW, 'zeroSide k = b321Norm * (poleTerm k - primeSum k + archTerm k)'), (B321, 'residual=Z - (P - PR + A)')),
    ('sign of P', 'SAME', 'plus in both',
     (EFF, 'paperFT k (I / 2) + paperFT k (-I / 2)'), (B321, 'P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0), v))')),
    ('sign of PR', 'SAME', 'minus in both',
     (EFF, '- ∑\' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)'), (B321, 'Z - (P - PR + A)')),
    ('sign of A', 'SAME', 'plus in both',
     (EFF, '+ (1 / (2 * π) : ℂ) * ∫ r : ℝ, paperFT k r * (gammaBracket r : ℂ)'), (B321, 'Z - (P - PR + A)')),
    ('normalization', 'SAME', 'the constant is 1 in every channel: A carries 1/(2 pi) and the same bracket Re psi(1/4 + iu/2) - log pi in both; P is h(i/2) + h(-i/2) = 2 INT k cosh(u/2) for even k; PR is Lambda(n) n^(-1/2) (k(log n) + k(-log n)) = 2 log p n^(-1/2) k(log n) for even k; Z counts each zero at gamma and -gamma, = 2 SUM_(gamma>0) for even k. ### Printed as `b321Norm := 1`.',
     (EFF, 'def gammaBracket (r : ℝ) : ℝ := (Complex.digamma (1 / 4 + I * r / 2)).re - Real.log π'),
     (ATL, 'np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U]) - math.log(math.pi)')),
    ('class of test functions', 'DIFFERS', 'EF_lit and the new terminal: every k : R -> C with ContDiff R 2 k and compact support (the new terminal adds evenness). b321: any sampled (v, w), and on the ladder the chain transforms w as a CONTINUOUS PIECEWISE-LINEAR function (b326 hhat_exact, the product form over segments) -- kinked at its nodes, so C^0 and NOT C^1, and not in C_c^2.',
     (EFF, '∀ k : ℝ → ℂ, ContDiff ℝ 2 k → HasCompactSupport k →'), (CLO, 'ROUTE ONE (product form): hhat(g) = -(2 sin(g dv/2) / g^2) SUM_j beta_j sin(g (v_j + dv/2))')),
    ('truncation', 'DIFFERS', 'EF_lit carries none: the zero side is a tsum over every zero with multiplicity (summability proved), A an integral over all of R. b321: Z sums the banked ordinates only (carto_atlas.GAM, simple and on the line, to T), A integrates over [-UMAX, UMAX]; PR is exact (finite by the support).',
     (EFF, 'Summable (fun ρ : Z.carrier => (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ)) ∧'), (B321, 'U = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)')),
]
PREMISE = ('P-PL: the explicit formula EF_lit holds for every even, compactly supported, continuous piecewise-linear k '
           '-- the windows the ladder`s chain actually transforms. Not compiled; not in the record as a terminal.')


def regularity():
    """### the chain's own object at one ladder cell: slope jumps at the nodes of f_a (a = 5.0, b506's nv)."""
    import numpy as np
    import b317_smear as SM
    import b318_square as SQ
    g = SM.mean_zero_variant(5.0)
    f = SQ.autocorrelation(g, 8193)
    v, w = np.asarray(f.v), np.asarray(f.w)
    s = np.diff(w) / np.diff(v)
    jumps = np.abs(np.diff(s))
    inner = jumps[np.abs(v[1:-1]) < 0.5 * float(v[-1])]
    return dict(nodes=int(v.size), max_slope_jump=float(jumps.max()), median_slope_jump_inner=float(np.median(inner)),
                nonzero_jumps=int((jumps > 1e-9).sum()))


def clauses():
    miss = []
    for c, verdict, why, a, b in CLAUSES:
        for f, q in (a, b):
            if q not in io.open(f, encoding='utf-8', errors='replace').read():
                miss.append((c, os.path.basename(f), q[:60]))
    if miss:
        print('### REFUSED -- QUOTATIONS NOT FOUND: %s' % miss)
        return 2
    prof = json.loads(io.open(os.path.join(D, 'b509_profile.json'), encoding='utf-8').read()) if os.path.exists(os.path.join(D, 'b509_profile.json')) else {}
    if not (prof.get('new_std3') and not prof.get('sorry')):
        print('### REFUSED -- NO CLEAN TERMINAL IS BANKED (profile %s); NOTHING IS GRADED.' % prof)
        return 2
    reg = regularity()
    diff = [c for c in CLAUSES if c[1] == 'DIFFERS']
    L = ['=' * 104, 'b509 -- COMPONENTS 2 AND 3. ### THE DERIVED STATEMENT AGAINST b321`S INTERFACE FORM, AND THE GRADE.', '=' * 104]
    for c, verdict, why, a, b in CLAUSES:
        L += ['  %-26s %-8s %s' % (c, verdict, why),
              '      derived side : %s  <%s>' % (a[1], os.path.basename(a[0])),
              '      b321 side    : %s  <%s>' % (b[1], os.path.basename(b[0]))]
    L += ['  ### ### **CLAUSES : %d ; SAME %d ; DIFFERS %d -- %s.**' % (len(CLAUSES), len(CLAUSES) - len(diff), len(diff),
                                                                       ', '.join(c[0] for c in diff)),
          '', '### THE LADDER`S FAMILY, MEASURED ON THE CHAIN`S OWN OBJECT (a = 5.0, nv 8193):',
          '    nodes %(nodes)d ; slope jumps above 1e-9 at %(nonzero_jumps)d nodes ; largest %(max_slope_jump).3e ; median over the inner half %(median_slope_jump_inner).3e' % reg,
          '    ### the chain transforms this w as piecewise linear: its derivative jumps at %d nodes, so it is not C^1.' % reg['nonzero_jumps'],
          '', '### COMPONENT 3 -- THE GRADE, BY STATEMENT-READ, AGAINST: "b321`s identity holds for every test function of the ladder`s family".',
          '    the terminal proves the identity for every EVEN k in C_c^2(R); the ladder`s family, as the chain transforms it, is not in C_c^2.',
          '    ### ### **GRADE : INTERFACES**, on the named premise', '    ' + PREMISE,
          '    ### not DERIVES: the class clause DIFFERS and no compiled step carries the family into the class;',
          '    ### not NOT THE CLAIM: the identity proved is b321`s, channel for channel, on the class it quantifies over;',
          '    ### not ENCODES: nothing of the claim sits in a hypothesis of the terminal other than the class and evenness.',
          '=' * 104]
    io.open(os.path.join(D, 'b509_clauses.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    res = dict(clauses=[dict(clause=c, verdict=v) for c, v, _w, _a, _b in CLAUSES], differs=[c[0] for c in diff],
               norm_constant=1, grade='INTERFACES', premise=PREMISE, regularity=reg)
    io.open(os.path.join(D, 'b509_clauses.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit({'compile': compile_, 'profile': profile, 'statement': statement, 'clauses': clauses}[sys.argv[1]]())
