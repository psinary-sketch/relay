# -*- coding: utf-8 -*-
"""b470_extract.py -- THE SURVEY. ### zeta23's explicit formulas for zeta, b321's identity, the (R79)
### targets, the deposited digests, and the build state -- all banked BEFORE the seal.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def decl(path, head, label, maxl=16):
    """### A declaration's statement VERBATIM: from its head line to the first `:= by` / `:=` that
    ### closes the signature, or to the blank line ending a `def ... : Prop :=` body."""
    ls = read(os.path.join(Z, path)).split(NL)
    for i, l in enumerate(ls):
        if l.startswith(head):
            body, past = [], False
            for j in range(i, min(i + maxl + 8, len(ls))):
                x = ls[j]
                if past and not x.strip():
                    break
                body.append(x)
                if not past and (':= by' in x or x.rstrip().endswith(':=') or re.search(r':=\s+\S', x)):
                    if x.rstrip().endswith(':=') and head.startswith('def'):
                        past = True
                        continue
                    break
            rec('  %-34s %s:%d' % (label, path.replace(os.sep, '/'), i + 1))
            for x in body:
                rec('      %s' % x.rstrip()[:150])
            return dict(label=label, file=path.replace(os.sep, '/'), line=i + 1, statement=NL.join(body))
    MISSES.append((path, head))
    rec('  %-34s ### MISS %r' % (label, head))
    return None


def main():
    rec('=' * 104)
    rec('b470 -- THE SURVEY.')
    rec('=' * 104)

    rec('')
    rec('(P1) zeta23 -- EVERY DECLARATION IN Zeta23/ STATING AN EXPLICIT FORMULA FOR ZETA.')
    rec('-' * 104)
    X = [
        decl(os.path.join('Zeta23', 'ExplicitFormula.lean'), 'def literatureRHS', 'the literature right-hand side'),
        decl(os.path.join('Zeta23', 'ExplicitFormula.lean'), 'def gammaBracket', 'the Gamma bracket'),
        decl(os.path.join('Zeta23', 'ExplicitFormula.lean'), 'def EF_lit', 'EF_lit (statement)'),
        decl(os.path.join('Zeta23', 'ExplicitFormula.lean'), 'def EF_paper', 'EF_paper (statement)'),
        decl(os.path.join('Zeta23', 'Hypotheses.lean'), 'def ExplicitFormulaPaper', 'ExplicitFormulaPaper (statement)'),
        decl(os.path.join('Zeta23', 'WeilEF', 'Main.lean'), 'theorem EF_lit_zeta ', 'EF_lit_zeta (theorem)'),
        decl(os.path.join('Zeta23', 'WeilEF', 'Main.lean'), 'theorem EF_lit_zetaZeroConfig', 'EF_lit_zetaZeroConfig (theorem)'),
        decl(os.path.join('Zeta23', 'Final.lean'), 'theorem zetaEF', 'zetaEF (theorem)'),
        decl(os.path.join('Zeta23', 'ExplicitFormula.lean'), 'theorem prop_EF_of_lit', 'prop_EF_of_lit (bridge)'),
        decl(os.path.join('Zeta23', 'ExplicitFormula', 'Bridge.lean'), 'theorem explicitFormulaPaper_of_lit',
             'explicitFormulaPaper_of_lit (bridge)'),
        decl('Zeta23' + os.sep + 'Defs.lean', 'def paperFT', 'the transform, paperFT'),
        decl('Zeta23' + os.sep + 'Defs.lean', 'def gammaOf', 'the ordinate, gammaOf'),
    ]
    rec('  ### EXCLUDED, WITH THE REASON: the `EF_lit_chi` family (for L(s, chi), not zeta) and the')
    rec('  ### `xiEF` / `wEF` family (for the zeros of xi-prime and of Hardy`s W, not the zeros of zeta).')

    rec('')
    rec('(P2) b321`S IDENTITY AS THE CHAIN DEFINES IT.')
    rec('-' * 104)
    w = read(os.path.join(T, 'b321_window.py')).split(NL)
    for n in (143, 144):
        rec('    b321_window.py:%d  %s' % (n, w[n - 1].rstrip()))
    for lab, needle in (('Z, the zero side', 'Z = 2.0 * float(np.sum(hhat_blocked'),
                        ('P, the pole term', 'P = 2.0 * float(np.trapezoid(w * np.cosh'),
                        ('A, the archimedean channel', 'A = float(np.trapezoid(hhat_blocked(v, w, U) * AT.kernel'),
                        ('PR, the prime sum (corpus route)', "val = 2.0 * math.log(p) / math.sqrt(n)"),
                        ('the half-line normalization', 'f(x) = x^{-1/2} w(log x)'),
                        ('the signs, quoted from the atlas', 'sum_gamma hhat(gamma) = hhat(i/2)')):
        hit = [(i + 1, x) for i, x in enumerate(w) if needle in x]
        if hit:
            rec('    %-34s b321_window.py:%d  %s' % (lab, hit[0][0], hit[0][1].strip()[:110]))
        else:
            MISSES.append(('b321_window.py', lab))
            rec('    %-34s ### MISS' % lab)
    at = read(os.path.join(T, 'e16', 'carto_atlas.py')).split(NL)
    for lab, needle in (('the atlas`s hhat', 'def hhat'), ('the atlas`s kernel', '"""Re psi(1/4 + i u/2) - log pi')):
        hit = [(i + 1, x) for i, x in enumerate(at) if needle in x]
        rec('    %-34s carto_atlas.py:%s  %s' % (lab, hit[0][0] if hit else '?', hit[0][1].strip() if hit else 'MISS'))
    sq = read(os.path.join(T, 'b318_square.py')).split(NL)
    hit = [(i + 1, x) for i, x in enumerate(sq) if '(f^ conv f)(v) = INT f(u) f(u + v) du' in x]
    rec('    %-34s b318_square.py:%s  %s' % ('f = g conv g-bar-sharp, formed', hit[0][0], hit[0][1].strip()))
    cc = read(os.path.join(D, 'b328_source_text.txt')).split(NL)
    rec('    the class of g, CC Prop C.1 (155) : b328_source_text.txt:3830-3835 -- g in C_c^inf(R*_+), g~(z)=0 on F >= {0,1}')
    rec('    CC Definition 3.1                  : b328_source_text.txt:1301 -- %s' % cc[1300].strip()[:90])

    rec('')
    rec('(P3) THE (R79) TARGETS, AND THE DEPOSITED DIGESTS BEFORE ANY WRITE.')
    rec('-' * 104)
    wk = read(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')).split(NL)
    n244 = next(i + 1 for i, x in enumerate(wk) if x.startswith('## 24.4'))
    nrow = next(i + 1 for i, x in enumerate(wk) if x.startswith('| Analytic number theory |') and i > n244 - 1)
    ntab_end = next(i + 1 for i in range(nrow, len(wk)) if not wk[i].startswith('|'))
    rec('    working 24.4 at :%d ; analytic row at :%d ; table ends before :%d' % (n244, nrow, ntab_end))
    rec('      %s' % wk[nrow - 1][:150])
    it = read(os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')).split(NL)
    nflag = next(i + 1 for i, x in enumerate(it) if 'no-Euler-clause' in x)
    rec('    the intake item at its address : reports/2026-08-20-external-intake.md:%d' % nflag)
    rec('      %s' % it[nflag - 1].strip())
    md5 = {fn: hashlib.md5(open(os.path.join(DEP, fn), 'rb').read()).hexdigest()
           for fn in sorted(os.listdir(DEP)) if os.path.isfile(os.path.join(DEP, fn))}
    rec('    deposited files digested : %d ; A_Place_to_Stand.md md5 %s' % (len(md5), md5['A_Place_to_Stand.md']))

    rec('')
    rec('(P4) THE BUILD STATE, AND WHAT THE ORDERED FLAG DOES IN THIS LAKE.')
    rec('-' * 104)
    env = dict(os.environ)
    ver = subprocess.run(['lake', '--version'], cwd=Z, capture_output=True, text=True).stdout.strip()
    j1 = subprocess.run(['lake', 'build', '-j1', 'NoSuchTarget'], cwd=Z, capture_output=True, text=True)
    jobs = subprocess.run(['lake', 'build', '--jobs', '1', 'NoSuchTarget'], cwd=Z, capture_output=True, text=True)
    rec('    %s' % ver)
    rec('    `lake build -j1`      -> %s' % (j1.stderr or j1.stdout).strip().split(NL)[0])
    rec('    `lake build --jobs 1` -> %s' % (jobs.stderr or jobs.stdout).strip().split(NL)[0])
    mods, built = [], []
    for dp, dns, fns in os.walk(os.path.join(Z, 'Zeta23')):
        for fn in fns:
            if fn.endswith('.lean'):
                rel = os.path.relpath(os.path.join(dp, fn), Z)[:-5].replace(os.sep, '.')
                mods.append(rel)
                ol = os.path.join(Z, '.lake', 'build', 'lib', 'lean', *rel.split('.')) + '.olean'
                if os.path.exists(ol):
                    built.append(rel)
    rec('    Zeta23 modules : %d ; already built (.olean present) : %d ; remaining : %d'
        % (len(mods), len(built), len(mods) - len(built)))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b470_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(decls=[x for x in X if x], b321=[w[142], w[143]], work_244=n244, work_row=nrow,
                   work_table_end=ntab_end, intake_line=nflag, md5_before=md5, lake=ver,
                   j1_error=(j1.stderr or j1.stdout).strip().split(NL)[0],
                   jobs_error=(jobs.stderr or jobs.stdout).strip().split(NL)[0],
                   modules=len(mods), built=len(built), misses=MISSES),
              io.open(os.path.join(D, 'b470_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
