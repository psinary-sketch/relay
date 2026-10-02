# -*- coding: utf-8 -*-
"""b589_bench.py -- COMPONENTS 4 AND 5 OF b589, UNDER (R199)(5)-(6). ### A BENCH AND READS; NOTHING ABOUT ZETA'S ZEROS IS CLAIMED.

### `three_way` -- W-ORD-LI-THREE-WAY: lambda_n for n = 1..12 by the zero sum (relay data/b562_drift.txt table (i): Lambda_N + T2, floor T2),
###                the arithmetic limit (data/b563_per_n.txt: Z(n,0), floor the bank's column) and Keiper's expansion (the Taylor coefficients of
###                log xi at s = 1 from mpmath's Stieltjes constants, floor the 50/70-digit difference or 1e-45); H30a as the face fixes it.
### `keiper [dry]` -- Mathlib at SIDE-explicit-formula's .lake/packages/mathlib searched by git grep; the re-price entered after the hits are read.
### `lv_bank <logdir>` -- the lv re-measure's per-module logs banked, with the dependents of each failing module by the import graph.
### `product [dry]` -- the schema's fields read for a sum of two configurations; the price.
### Writes only data/b589_*.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
EFK = 'D:/SIDE-explicit-formula'
MATHLIB = EFK + '/.lake/packages/mathlib'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')


# ================================================================================ (a) THE THREE-WAY TABLE
def keiper(dps, N=12):
    import mpmath as mp
    mp.mp.dps = dps
    K = N + 2
    # (s-1) zeta(s) = 1 + sum_k (-1)^k gamma_k / k! t^{k+1}, t = s - 1
    a = [mp.mpf(0)] * (K + 1)
    a[0] = mp.mpf(1)
    for k in range(K):
        a[k + 1] = (-1) ** k * mp.stieltjes(k) / mp.factorial(k)
    # log of a power series with a[0] = 1
    l = [mp.mpf(0)] * (K + 1)
    for n in range(1, K + 1):
        l[n] = a[n] - sum(k * l[k] * a[n - k] for k in range(1, n)) / n
    eta = [mp.mpf(0)] * (K + 1)
    for j in range(1, K + 1):
        logs = (-1) ** (j + 1) / mp.mpf(j)                                  # log s = log(1 + t)
        arch = mp.polygamma(j - 1, mp.mpf(1) / 2) / mp.factorial(j) / mp.mpf(2) ** j  # log Gamma((1+t)/2)
        pi = -mp.log(mp.pi) / 2 if j == 1 else 0                            # -(s/2) log pi
        eta[j] = l[j] + logs + arch + pi
    lam = {}
    for n in range(1, N + 1):
        lam[n] = n * sum(mp.binomial(n - 1, j - 1) * eta[j] for j in range(1, n + 1))
    return lam


def three_way():
    import mpmath as mp
    k50, k70 = keiper(50), keiper(70)
    zero, arith, balpos = {}, {}, {}
    for l in rd('b562_drift.txt').split(NL)[13:26]:
        c = l.split()
        if len(c) >= 6 and c[0].isdigit():
            n = int(c[0])
            zero[n] = (float(c[4]), float(c[2]))         # Lambda_N + T2, floor T2
            if c[5] != '(not':
                balpos[n] = float(c[5])
    for l in rd('b563_per_n.txt').split(NL):
        c = l.split()
        if len(c) >= 8 and c[0].isdigit() and 1 <= int(c[0]) <= 12:
            arith[int(c[0])] = (float(c[3]), float(c[6]))  # Z(n,0), floor
    L = ['b589 -- COMPONENT 4 (a): W-ORD-LI-THREE-WAY, (R199)(5)(a). ### A BENCH, GRADED READING; NOTHING ABOUT ZETA`S ZEROS IS CLAIMED.', '',
         '### the routes, as the face fixes them (reading (xii)): ZERO = relay data/b562_drift.txt table (i) Lambda_N + T2, floor T2(n) ; '
         'ARITH = data/b563_per_n.txt Z(n,0), floor the bank`s column ; KEIPER = mpmath %s, Stieltjes constants, eta_j the Taylor coefficients '
         'of log xi at s = 1, lambda_n = n sum C(n-1, j-1) eta_j, floor max(|run 50 - run 70|, 1e-45).' % mp.__version__,
         '### H30a: every pair of routes at every n agrees within the sum of the two floors; refuted by one miss. BALPOS (li_bench, the '
         'channel quadrature) printed beside, not scored.', '',
         '   n   KEIPER (70 digits)        floor_K    ZERO (Lambda_N+T2)     floor_Z     ARITH Z(n,0)           floor_A    '
         '|Z-K|/(fZ+fK)  |A-K|/(fA+fK)  |A-Z|/(fA+fZ)   BALPOS - KEIPER']
    misses, rows = [], []
    for n in range(1, 13):
        kv = k70[n]
        fk = max(abs(float(k50[n] - k70[n])), 1e-45)
        zv, fz = zero[n]
        av, fa = arith[n]
        kf = float(kv)
        r1, r2, r3 = abs(zv - kf) / (fz + fk), abs(av - kf) / (fa + fk), abs(av - zv) / (fa + fz)
        for nm, r in (('ZERO-KEIPER', r1), ('ARITH-KEIPER', r2), ('ARITH-ZERO', r3)):
            if r > 1:
                misses.append((n, nm, r))
        bp = ('%+.3e' % (balpos[n] - kf)) if n in balpos else '(not banked)'
        L.append('  %2d   %s  %.1e   %.15f  %.3e   %.15f  %.3e    %.4f        %.4f        %.4f       %s' % (
            n, mp.nstr(kv, 22), fk, zv, fz, av, fa, r1, r2, r3, bp))
        rows.append(dict(n=n, keiper=mp.nstr(kv, 30), floor_k=fk, zero=zv, floor_z=fz, arith=av, floor_a=fa, r_zk=r1, r_ak=r2, r_az=r3))
    held = not misses
    L += ['', '### misses: %s' % (misses or 'NONE'),
          '### the closest to its floor: %s' % (max(((r['n'], k, r[k]) for r in rows for k in ('r_zk', 'r_ak', 'r_az')), key=lambda x: x[2]),),
          '### ### **H30a %s -- the three routes agree within the sum of their floors at every n = 1..12 (36 comparisons, %d misses).**' % (
              'HOLDS' if held else 'REFUTED', len(misses))]
    put_txt('b589_three_way.txt', L)
    put_json('b589_three_way.json', dict(rows=rows, misses=misses, H30a='HOLDS' if held else 'REFUTED'))
    for l in L[-3:]:
        print(l)


# ================================================================================ (b) THE KEIPER READ
KEIPER_PATTERNS = [
    ('the Stieltjes constants by name', ['-i', '-e', 'stieltjes'], 'Stieltjes'),
    ('the residue / Laurent expansion of riemannZeta at 1', ['-e', 'riemannZeta_residue', '-e', 'tendsto_riemannZeta_sub_one', '-e',
                                                              'riemannZeta_sub_one_div', '-e', 'Laurent', '-e', 'eulerMascheroni'], None),
    ('the log of completedRiemannZeta, or its derivatives at 1', ['-e', 'log (completedRiemannZeta', '-e', 'logDeriv completedRiemannZeta',
                                                                   '-e', 'log completedRiemannZeta', '-e', 'deriv completedRiemannZeta'], None),
]
KEIPER_PRICE = [
    'READ: Mathlib holds the pole of riemannZeta at 1 (`riemannZeta_residue_one`, NumberTheory/LSeries/RiemannZeta.lean :242), its constant '
    'term the Euler-Mascheroni constant (`tendsto_riemannZeta_sub_one_div`, NumberTheory/Harmonic/ZetaAsymp.lean :342), and the split '
    'riemannZeta = (s - 1)⁻¹ + riemannZeta₀ with riemannZeta₀ entire (the same file`s header); it holds no Stieltjes constant beyond the '
    'zeroth by name (every Stieltjes hit is the Lebesgue-Stieltjes measure) and no log of completedRiemannZeta by name.',
    'THE KERNEL ALREADY HOLDS the derivative form: `li_coeff_eq_taylorCoeff` (SIDE-explicit-formula v0.9 = e5a5a83, the ζ page node 18) '
    'equates LiCoeff (n+1) with the real part of Bulka`s taylorCoeff of riemannXi.',
    'THE PRICE, TWO LEMMAS OF SUBSTANCE: (1) the Keiper-Taylor identity -- the Stieltjes constants defined as the Taylor coefficients of '
    'riemannZeta₀ at 1 (a definition, the zeroth equal to γ by the Mathlib limit above), and taylorCoeff riemannXi n equal to the finite '
    'Keiper sum in them, the polygamma values at 1/2 and log π (power-series log and the binomial transform); (2) computable two-sided bounds '
    'for the Stieltjes constants up to the eleventh and for the polygamma values at 1/2 (the odd zeta values among them), which interval '
    'arithmetic would consume to certify a finite-n sign in-kernel. Bookkeeping beside them: the definitions, the n = 1 check against γ.',
    'TRIGGER unchanged: W-ORD-LI-THREE-WAY`s agreement, which this act banks (H30a).',
]


def keiper_read(*a):
    head = g(MATHLIB, 'rev-parse', 'HEAD').strip()
    L = ['b589 -- COMPONENT 4 (b): THE KEIPER READ, (R199)(5)(b). ### Mathlib at %s HEAD %s (the manifest`s de5ce8a9); git grep over Mathlib/**.lean.' % (
        MATHLIB, head[:10]), '']
    out = {}
    for label, args, drop in KEIPER_PATTERNS:
        hits = [h for h in g(MATHLIB, 'grep', '-n', *args, 'HEAD', '--', 'Mathlib/*.lean').split(NL) if h.strip()]
        kept = [h for h in hits if not (drop and 'StieltjesFunction' in h)] if drop else hits
        out[label] = dict(all=len(hits), kept=len(kept))
        L.append('### %s : %d hit(s)%s' % (label, len(hits), (' ; %d after the measure-theoretic `StieltjesFunction` (Lebesgue-Stieltjes '
                                                                 'measures, another object) is set aside' % len(kept)) if drop else ''))
        for h in kept[:80]:
            L.append('    %s' % h[5:260])
        if len(kept) > 80:
            L.append('    ... %d more, all printed in the json' % (len(kept) - 80))
        out[label]['hits'] = [h[5:400] for h in kept]
    if 'dry' in a:
        for l in L:
            print(l[:300])
        return
    if not KEIPER_PRICE:
        sys.exit('### THE RE-PRICE IS NOT ENTERED -- the hits are read first')
    L += ['', '### THE RE-PRICE OF W-ORD-KEIPER-FACE, on these hits (the seat`s read):'] + ['    ' + x for x in KEIPER_PRICE]
    put_txt('b589_keiper_read.txt', L)
    put_json('b589_keiper_read.json', dict(head=head, patterns=out, price=KEIPER_PRICE))


# ================================================================================ (c) THE lv BANK
def lv_bank(logdir):
    meta = json.load(io.open(os.path.join(logdir, 'meta.json'), encoding='utf-8'))
    mods = meta['order']
    res = {}
    for m in mods:
        p = os.path.join(logdir, m.replace('.', '_') + '.log')
        t = io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
        rc = re.search(r'### EXIT (\-?\d+)', t)
        errs = [l for l in t.split(NL) if re.search(r'error[:\(]', l) and 'warning' not in l]
        st = re.search(r'### STOPPED BY (?:THE SEAT|THE WATCHDOG) AT THE MEMORY HOLD: (.*)', t)
        res[m] = dict(exit=int(rc.group(1)) if rc else None, errors=len(errs), first=errs[:3], ran=bool(t), free=meta.get('free', {}).get(m),
                      stopped=st.group(1)[:200] if st else None, not_run=meta.get('not_run', {}).get(m))
    imports = meta['imports']

    def deps_of(bad):
        out, frontier = set(), {bad}
        while frontier:
            nxt = {m for m, ims in imports.items() if set(ims) & frontier and m not in out}
            out |= nxt
            frontier = nxt
        return sorted(out)
    failing = [m for m in mods if res[m]['exit'] not in (0, None)]
    L = ['b589 -- COMPONENT 4 (c): THE lv RE-MEASURE AGAINST de5ce8a9, (R199)(5)(c). ### a scratch worktree, nothing merged, nothing pushed.', '',
         '### the worktree: %s, detached at %s (toolchain-trial-b551`s tip) ; lean-toolchain %s ; Mathlib %s ; the lakefile`s rev set in the '
         'worktree, uncommitted' % (meta['worktree'], meta['head'], meta['toolchain'], meta['mathlib']),
         '### the cache: %s' % meta.get('cache', '?'), '',
         '| module | exit | errors | first error, or the stop | free memory before (MB) | dependents of a failure |', '|:--|--:|--:|:--|--:|:--|']
    for m in mods:
        r = res[m]
        what = ('STOPPED AT THE MEMORY HOLD: ' + r['stopped']) if r['stopped'] else (r['first'][0][:160].replace('|', '/') if r['first'] else
                                                                                   ('not run: ' + r['not_run'] if r['not_run'] else '--'))
        L.append('| %s | %s | %d | %s | %s | %s |' % (m, r['exit'] if r['ran'] else 'not run', r['errors'], what, r['free'] or '--',
                                                    len(deps_of(m)) if m in failing else '--'))
    first_fail = next((m for m in mods if m in failing), None)
    errored = [m for m in mods if res[m]['errors'] and not res[m]['stopped']]
    own = [m for m in errored if any(m.split('.')[-1] + '.lean' in e for e in res[m]['first'])]
    first_error = own[0] if own else None
    stopped = [m for m in mods if res[m]['stopped']]
    L += ['', '### modules %d ; built clean %d ; failing %d %s' % (len(mods), sum(1 for m in mods if res[m]['exit'] == 0), len(failing), failing),
          '### stopped at the memory hold (no error counted): %d %s' % (len(stopped), stopped),
          '### the first module whose own source errs, in build order: %s ; its dependents %d %s' % (
              first_error, len(deps_of(first_error)) if first_error else 0, deps_of(first_error) if first_error else []),
          '### the first failing module in build order, a stop included: %s ; its dependents %d %s' % (first_fail, len(deps_of(first_fail)) if first_fail else 0,
                                                                                                    deps_of(first_fail) if first_fail else []),
          '### ### **THE PRICE: %s**' % meta.get('price', '(entered after the read)')]
    put_txt('b589_lv_remeasure.txt', L)
    put_json('b589_lv_remeasure.json', dict(meta=meta, res=res, failing=failing, first_fail=first_fail, first_error=first_error,
                                            first_error_dependents=deps_of(first_error) if first_error else [], stopped=stopped,
                                            first_fail_dependents=deps_of(first_fail) if first_fail else []))
    print('failing', len(failing), 'first', first_fail)


# ================================================================================ COMPONENT 5 -- THE PRODUCT LEMMA, PRICED
PRODUCT_PRICE = [
    'THE OBJECT: for two configurations C1, C2 of the schema, the sum C1 + C2 -- carrier C1.carrier ∪ C2.carrier, multiplicity the sum of '
    'each configuration`s multiplicity on its own carrier (ZeroConfig`s `mult` is irrelevant off its carrier, Defs.lean :140), rhs the sum '
    'of the two rhs, target the conjunction of the two targets.',
    'BOOKKEEPING (no lemma of substance): the ZeroConfig fields of the sum -- one_le_mult, the strip, reflect_mem, mult_reflect, '
    'finite_window -- each from the two parts; target_iff from the two target_iff`s and membership in the union; COUNT -- the windowed '
    'count N (a finsum of multiplicities over a finite window, Defs.lean :162) adds over the union, so HCount holds with A₀ the sum of '
    'the two (RestBound.lean :44, 1 ≤ A₀ kept).',
    'ONE LEMMA OF SUBSTANCE, the summed explicit formula: on even C_c² test functions, the tsum over the union carrier with the summed '
    'multiplicities equals the sum of the two zero sides, each summable by the count it carries (the summability `dominant_summable` '
    'draws from HCount), so the sum`s `ef` is the two `ef`s added.',
    'THE CRITERION, FREE: `h2_sign_cfg_iff_target` holds for every WeilConfig (Schema/Converse.lean :265), so the sum`s criterion is its '
    'target, the conjunction of the two targets, each its own part`s criterion -- no further lemma.',
    'THE INSTANCE, PRICED BESIDE AND NOT INSIDE: zeta · L(s, χ_d) as a sum of the ζ configuration and the χ_d configuration needs the χ_d '
    'instance at a real primitive quadratic character (the χ page`s instances are for primitive χ); naming it the Dedekind zeta of the '
    'quadratic field needs the factorization ζ_K = ζ · L(s, χ_d), which this read did not search in Mathlib -- a separate item.',
    'PRICE: one lemma of substance (the summed explicit formula) and the bookkeeping above; the Dedekind identification is a separate item.',
]


def product(*a):
    src = g(EFK, 'show', 'main:SIDEExplicitFormula/Schema/Config.lean').split(NL)
    L = ['b589 -- COMPONENT 5: THE PRODUCT LEMMA, PRICED AND NOT ATTEMPTED, (R199)(6). ### SIDE-explicit-formula main %s.' %
         g(EFK, 'rev-parse', '--short=7', 'main').strip(), '',
         '### the schema`s fields (Schema/Config.lean at main):']
    s = next(i for i, l in enumerate(src) if l.startswith('structure WeilConfig'))
    L += ['    :%d %s' % (i + 1, src[i]) for i in range(s, s + 13)]
    rb = g(EFK, 'grep', '-n', '-A14', 'def HCount', 'main', '--', '*.lean').split(NL)
    L += ['### the count the COUNT field consumes (B321.HCount):'] + ['    %s' % l[5:220] for l in rb[:16]]
    zc = g(EFK, 'grep', '-n', '-A10', '-E', '^structure ZeroConfig', 'main', '--', 'Zeta23/*.lean').split(NL)
    nn = g(EFK, 'grep', '-n', '-E', '^def N ', 'main', '--', 'Zeta23/*.lean').split(NL)
    L += ['### the configuration the schema extends (Zeta23.ZeroConfig, vendored):'] + ['    %s' % l[5:220] for l in zc[:12] + nn[:1]]
    iff = [l for l in g(EFK, 'grep', '-n', '-A3', 'theorem h2_sign_cfg_iff_target', 'main', '--', '*.lean').split(NL) if l.strip()]
    L += ['### the criterion over the structure (h2_sign_cfg_iff_target):'] + ['    %s' % l[5:220] for l in iff[:6]]
    if 'dry' in a:
        for l in L:
            print(l[:240])
        return
    if not PRODUCT_PRICE:
        sys.exit('### THE PRICE IS NOT ENTERED -- the fields are read first')
    L += ['', '### THE PRICE (the seat`s read of the fields):'] + ['    ' + x for x in PRODUCT_PRICE]
    put_txt('b589_product_price.txt', L)
    put_json('b589_product_price.json', dict(price=PRODUCT_PRICE))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(three_way=three_way, keiper=keiper_read, lv_bank=lv_bank, product=product).get(cmd)
    if not fn:
        print('usage: b589_bench.py three_way | keiper [dry] | lv_bank <logdir> | product [dry]')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
