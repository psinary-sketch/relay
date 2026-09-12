# -*- coding: utf-8 -*-
"""b440_extract.py -- THE SURVEY. ### **WRITTEN BEFORE THE FACE.**

### ### **IT READS, AND IT EVALUATES TWO FIXED FUNCTIONS.** ### `h+` and `log(u/2pi)` carry no
### family, no radius and no cell; comparing them is a read of two closed expressions. ### **EVERY
### CELL VALUE AND EVERY BUILD BELONGS TO THE COMPONENTS, AFTER THE FACE IS LOCKED.**
"""
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
WIN = os.path.join('D:', os.sep, 'SIDE-window')
OUT = os.path.join(D, 'b440_extract.txt')
SR = os.path.join(PP, 'phase2', 'method', 'SIGN_ARRANGEMENT_RECONCILIATION.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, READS, MISS = [], [0], []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    return s.replace(chr(13) + chr(10), chr(10))


def wrap(s, n=88):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, label=None, indent='      ', clip=300):
    READS[0] += 1
    lines = nl(read(path)).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('%s%s:%d' % (indent, os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip()[:clip], 84):
                    rec('%s  | %s' % (indent, c))
            return True
    MISS.append('%s : %r NOT LOCATED' % (os.path.basename(path), (label or needle)[:60]))
    rec('%s### **NOT LOCATED** : %s' % (indent, (label or needle)[:60]))
    return False


def main():
    rec('=' * 100)
    rec('b440 -- THE FIXED POINT NAMED, THE BREAK ATTRIBUTED. ### THE SURVEY.')
    rec('=' * 100)

    # ------------------------------------------------------------------------------------------
    head(1, "DOES THE CORPUS ALREADY CARRY THE SMOOTH ZERO-COUNTING DENSITY, AND UNDER WHAT NAME?")
    rec('    ### **THE SEARCH, BY THE CLASSICAL NAME AND BY THE FORM:**')
    pats = [('the name', r'Riemann[-–]von Mangoldt'),
            ('the counting function', r'\bN\(T\)'),
            ('the density, written out', r'\(T\s*/\s*2\s*pi\)\s*log|T/2π\)\s*log'),
            ('the asymptote 2 pi in a counting law', r'log\s*\(?\s*T\s*/\s*2\s*\\?pi')]
    found = {}
    for lbl, rx in pats:
        where = []
        for base in (PP,):
            for root, dirs, fs in os.walk(base):
                dirs[:] = [x for x in dirs if x not in ('.git', '__pycache__')]
                for f in fs:
                    if not f.endswith('.md'):
                        continue
                    if re.search(rx, read(os.path.join(root, f)), re.I):
                        where.append(os.path.relpath(os.path.join(root, f), PP)
                                     .replace(os.sep, '/'))
        found[lbl] = where
        rec('      %-38s %-4d %s' % (lbl, len(where), ', '.join(where[:2]) or '-'))
    rec('')
    rec('    ### **AND THE NAME, AT A LINE:**')
    quote(os.path.join(PP, 'FACES_LEDGER.md'), 'Riemann-von Mangoldt main term', 0,
          label='the RvM main term in the ledger')
    rec('')
    rec('    ### ### **AND THE CROSSING AT `2 pi` IS ALREADY IN THE CORPUS, IN THESE WORDS:**')
    quote(SR, 'WHICH EQUALS `log π` EXACTLY AT', 0, label='the 2 pi crossing', clip=260)
    rec('')
    quote(SR, 'is **NEGATIVE at low frequency and POSITIVE at high frequency**', 0,
          label='the kernel changes sign', clip=320)
    rec('')
    rec('    ### ### **SO THE RECORD CARRIES THE CROSSING AS A PROPERTY OF `W_inf`, THE')
    rec('    ### ### ARCHIMEDEAN KERNEL. ### WHETHER IT ALSO CARRIES IT AS A ZERO-COUNTING')
    rec('    ### ### DENSITY IS COMPONENT 1`S CLAUSE (2), AND THE NAMES ABOVE ARE THE EVIDENCE.**')
    json.dump(found, io.open(os.path.join(D, 'b440_density_search.json'), 'w', encoding='utf-8'),
              indent=1)

    # ------------------------------------------------------------------------------------------
    head(2, "DOES THE CORPUS`S OWN DERIVATION OF `h+` EXHIBIT THIS EXPRESSION?")
    rec('    ### **`b333` DERIVED `h+` AND ITS EPSTEIN SIBLING, AND THE SIBLING IS THE CHECK:**')
    quote(os.path.join(T, 'b333_derive.py'), 'hplus = -log(pi) + mre(digamma', 0, label='h+')
    rec('')
    quote(os.path.join(T, 'b333_derive.py'), 'kq = 2 * mre(digamma(mpc(mpf(1) / 2, tau)))', 0,
          label='the Epstein kernel')
    rec('')
    rec('    ### ### **THE TWO HAVE THE SAME SHAPE WITH DIFFERENT CONSTANTS:** ### for zeta,')
    rec('    ### `Re psi(1/4 + i u/2) - log pi`; for the Epstein object of discriminant `-23`,')
    rec('    ### `2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt 23)`. ### **THE CONSTANT IS THE')
    rec('    ### CONDUCTOR`S**, and that is what Component 1 must check against the counting law.')
    rec('')
    rec('    ### and the corpus`s own Epstein counting law, for the comparison:')
    quote(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                       'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'),
          'N(T) ∼ (T/π) log(cT)', 0, label='the Epstein counting law', clip=260)

    # ------------------------------------------------------------------------------------------
    head(3, "`h+` AGAINST ITS OWN ASYMPTOTE. ### **TWO CLOSED EXPRESSIONS, NO FAMILY.**")
    try:
        from mpmath import mp, mpf, mpc, log, pi, digamma, re as mre, findroot
        mp.dps = 30

        def h(u):
            return mre(digamma(mpc(mpf(1) / 4, mpf(u) / 2))) - log(pi)

        def asym(u):
            return log(mpf(u) / (2 * pi))

        rec('      %-9s %-24s %-24s %s' % ('u', 'h+(u)', 'log(u / 2 pi)', '|difference|'))
        for u in (6.2898, 10, 50, 200, 1000, 10000):
            rec('      %-9s %-24s %-24s %.3e'
                % (u, mp.nstr(h(u), 14), mp.nstr(asym(u), 14), float(abs(h(u) - asym(u)))))
        u0 = findroot(h, mpf('6.29'))
        rec('')
        rec('      ### ### **u0 (the exact zero of `h+`)   = %s**' % mp.nstr(u0, 21))
        rec('      ### ### **2 pi (the asymptote`s zero)   = %s**' % mp.nstr(2 * pi, 21))
        rec('      ### ### **RATIO u0 / 2 pi              = %s**' % mp.nstr(u0 / (2 * pi), 12))
        rec('      ### and `h+(2 pi) = %s` -- ### **THE ASYMPTOTE VANISHES AT `2 pi`; THE EXACT'
            % mp.nstr(h(2 * pi), 12))
        rec('      ### KERNEL DOES NOT.**')
        rec('')
        rec('    ### ### **THE DIFFERENCE FALLS LIKE `u^-2`** -- `4.17e-08` at `u = 1000` and')
        rec('    ### `4.17e-10` at `u = 10000`, a factor of `100` for a factor of `10`. ### So the')
        rec('    ### asymptote is exact and the correction is the digamma`s own tail.')
        json.dump(dict(u0=str(u0), two_pi=str(2 * pi), ratio=str(u0 / (2 * pi)),
                       h_at_two_pi=str(h(2 * pi))),
                  io.open(os.path.join(D, 'b440_u0.json'), 'w', encoding='utf-8'), indent=1)
    except Exception as e:                                       # noqa: BLE001
        MISS.append('h+ against its asymptote : %s' % str(e)[:60])
        rec('      ### **NOT EVALUATED** : %s' % str(e)[:70])

    # ------------------------------------------------------------------------------------------
    head(4, "WHAT IS THE `cosh(v/2)` WEIGHT? ### **READ FROM THE SOURCE, NOT NAMED BY THE SEAT.**")
    rec('    ### **WHERE IT ENTERS THE AIM:**')
    quote(os.path.join(T, 'b317_smear.py'), 'M = np.array([np.trapezoid(p * np.cosh(V / 2.0), V)',
          0, label='the second moment')
    rec('')
    rec('    ### **AND WHAT THE SAME EXPRESSION IS IN THE EXPLICIT FORMULA -- THE POLE TERM:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0)',
          0, label='the pole term')
    rec('')
    quote(os.path.join(T, 'b321_window.py'), 'P = 2.0 * float(np.trapezoid(w * np.cosh(v / 2.0)',
          0, label="b321's pole term")
    rec('')
    rec('    ### ### **THE SAME INTEGRAL IS THE AIM`S SECOND MOMENT AND THE EXPLICIT FORMULA`S')
    rec('    ### ### POLE TERM.** ### Component 3 must say what that weight IS, from the source.')
    rec('')
    rec('    ### and the corpus`s own name for what the pole term is:')
    quote(os.path.join(T, 'b321_run.py'), 'f-tilde(0)+f-tilde(1)', 0, label='the pole column')
    rec('')
    quote(os.path.join(T, 'b321_run.py'), 'g-hat(i/2) = 0', 1, label='the lawfulness condition')
    rec('')
    rec('    ### **AND WHAT THE AIM`S SECOND CONDITION IS, IN THE INSTRUMENT`S OWN HEADER:**')
    quote(os.path.join(T, 'b317_smear.py'), 'test function is the single condition', 0,
          label='eq. (54), the single condition')
    rec('')
    rec('    ### ### **THE CORPUS`S OWN TERM-FOR-TERM DICTIONARY -- ### THE ANSWER TO')
    rec('    ### ### COMPONENT 3 IS A TABLE ROW, NOT AN INFERENCE:**')
    for nd, lb in (('`P = ĥ(i/2) + ĥ(−i/2) = 2∫w cosh(v/2)dv`', 'the P row'),
                   ('`A = (1/2π)∫ĥ(u)[Re ψ(1/4 + iu/2)', 'the A row')):
        quote(SR, nd, 0, label=lb, clip=200)
    rec('')
    rec('    ### ### **`cosh(v/2)` WEIGHTS `W_pole`. ### THE ARCHIMEDEAN WEIGHT IS A DIFFERENT')
    rec('    ### ### EXPRESSION IN A DIFFERENT VARIABLE.** ### Component 3 scores (N3) on this.')
    rec('')
    rec('    ### **AND WHAT THE `2` IS, IN THE SOURCE`S WORDS:**')
    quote(SR, 'it is the count of the two pole terms', 0, label='the two pole terms', clip=420)

    # ------------------------------------------------------------------------------------------
    head(5, "THE KERNEL`S DEPENDENCIES -- ### **WHAT COMPONENT 2 MAY AND MAY NOT STATE.**")
    p = subprocess.run(['git', '-C', WIN, 'log', '-1', '--format=%H'],
                       capture_output=True, text=True)
    rec('    SIDE-window pin : %s' % (p.stdout or '').strip())
    st = subprocess.run(['git', '-C', WIN, 'status', '--porcelain'], capture_output=True, text=True)
    rec('    working tree    : %s'
        % ('CLEAN' if not (st.stdout or '').strip() else '### DIRTY ###'))
    rec('')
    quote(os.path.join(WIN, 'SIDEWindow', 'Ladder.lean'), 'Vanilla Lean 4', 1,
          label='the no-dependency declaration')
    rec('')
    rec('    ### **AND THE MANIFEST, WHICH SETTLES IT:**')
    mf = read(os.path.join(WIN, 'lake-manifest.json'))
    try:
        j = json.loads(mf) if mf else {}
        pk = j.get('packages', [])
        rec('      packages in lake-manifest.json : %d %s'
            % (len(pk), [x.get('name') for x in pk] if pk else ''))
    except Exception:                                            # noqa: BLE001
        rec('      lake-manifest.json : %s' % (mf[:120] if mf else 'NOT READ'))
    rec('')
    rec('    ### **THE DEFINITION FACT (i) WOULD REST ON:**')
    quote(os.path.join(WIN, 'SIDEWindow', 'Window.lean'), 'def primePowersLT', 1,
          label='primePowersLT')
    rec('')
    rec('    ### ### **AND THE ONE THING THE SURVEY FLAGS FOR THE FACE, WITHOUT DECIDING IT:**')
    rec('    ### fact (ii) is `2 Lambda(n) / sqrt(n)` -- ### **A REAL NUMBER.** ### This kernel has')
    rec('    ### no Mathlib, no Batteries and no dependencies, so it has ### **NO REALS, NO `log`')
    rec('    ### AND NO `sqrt`.** ### Whether that makes the fact unstatable here is Component 2`s')
    rec('    ### call and the face declares how it will be made.')
    rec('')
    rec('    ### **AND THE KERNEL`S OWN PRECEDENT FOR REFUSING A MEASURED TABLE:**')
    quote(os.path.join(WIN, 'SIDEWindow', 'Ladder.lean'), 'MEASURED-AT-BANK', 2,
          label="the ladder's refusal of a measured law")

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
