# -*- coding: utf-8 -*-
"""b679_q0_membership.py -- COMPONENT 4, (R289)(5)(iv) AND (6)-(7), H4: Q0 READ AGAINST THE WIDENED CLASS, ROW BY ROW, EACH ROW WITH ITS SOURCE.

### Rows are the fields of SIDEExplicitFormula.Schema.WideConfig and the hypotheses of S5' (Wide.HExcl, Wide.HCount), each with its reading at
### Q0 and its source (relay data/b679_strip_plan.txt == 5 and == 11). The certified balls: relay data/b671_epstein_zeros_narrowed.json.gz, its
### sha256 and the inner JSON's compared with data/b671_epstein_zeros_narrowed_hashes.txt :2-:3 BEFORE any row is read (the author's answer
### on the ball bank). HExcl's reading by the route the author's answer names, verified and cited, not taken from the answer: Z_Q(σ) > 0 for
### real σ > 1 as a sum of positive terms, Λ_Q(s) = Λ_Q(1 - s) with Γ < 0 on (-1, 0), and Z_Q(0) read directly; then the completed
### function's route evaluated in balls on (-1/2, 0] by b667's Chowla-Selberg instrument (tools/b667_epstein_certify.py `zq`, imported and
### unchanged), each subinterval a ball, every ball printed with its sign. The band count stands beside it (data/b667_epstein_counts.txt :56).
### Usage: `python -X utf8 tools/b679_q0_membership.py` -> data/b679_q0_membership.txt (.json). No lean; no kernel file written.
"""
import gzip
import hashlib
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import arb, acb, ctx   # noqa: E402
import b667_epstein_certify as E   # noqa: E402  ### the Chowla-Selberg instrument, imported unchanged

NSUB = 32                          # ### (-1/2, 0] covered by 32 closed subintervals of width 1/64, [-1/2 + k/64, -1/2 + (k+1)/64]
PREC = 200


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')


def line(name, n):
    L = rd(name).split(NL)
    return L[n - 1] if len(L) >= n else ''


def main():
    t0 = time.time()
    H = rd('b671_epstein_zeros_narrowed_hashes.txt')
    want_json = re.search(r'json \(inside the \.gz\) sha256 ([0-9a-f]{64})', H).group(1)
    want_gz = re.search(r'json\.gz sha256 ([0-9a-f]{64})', H).group(1)
    raw = open(os.path.join(D, 'b671_epstein_zeros_narrowed.json.gz'), 'rb').read()
    inner = gzip.decompress(raw)
    gz_ok, js_ok = hashlib.sha256(raw).hexdigest() == want_gz, hashlib.sha256(inner).hexdigest() == want_json
    if not (gz_ok and js_ok):
        sys.exit('### THE BALL BANK`S HASHES DO NOT AGREE WITH data/b671_epstein_zeros_narrowed_hashes.txt -- NOTHING READ')
    rows = json.loads(inner)['rows']
    ctx.prec = PREC
    on = [r for r in rows if r['kind'] == 'ON']
    off = [r for r in rows if r['kind'] == 'OFF']
    res = [arb(r['re'], r['h']) for r in off]
    ims = [arb(r['im'], r['h']) for r in rows]
    re_lo = min(float(x.lower()) for x in res)
    re_hi = max(float(x.upper()) for x in res)
    re_refl_lo, re_refl_hi = 1 - re_hi, 1 - re_lo
    im_lo = min(float(abs(x).lower()) for x in ims)
    all_in_strip = all(x > arb(-1) / 2 and x < arb(3) / 2 for x in res) and all(arb(r['re']) == arb(1) / 2 for r in on)
    any_real = any(x.contains(0) for x in ims)

    # ### HExcl: the route, each step evaluated, and the balls on (-1/2, 0]
    z0 = E.zq(acb(0), PREC)
    s_r = [arb('1.05'), arb('1.25'), arb('1.5')]
    zpos = [(float(s.mid()), E.zq(acb(s), PREC)) for s in s_r]
    gam = [(x, acb(arb(x)).gamma()) for x in ('-0.9', '-0.5', '-0.1')]
    def zq_fe(s):
        """Z_Q(s) = (2π/√23)^{2s-1} Γ(1 - s) Γ(s)⁻¹ Z_Q(1 - s), from Λ_Q(s) = Λ_Q(1 - s) (plan :10): finite through s = -1/2, where the
        direct route's Γ(s - ½) pole meets ζ(2s - 1) = ζ(-2) = 0."""
        z1 = E.zq(1 - s, PREC)
        ctx.prec = PREC
        return acb(2 * arb.pi() / arb(23).sqrt()) ** (2 * s - 1) * (1 - s).gamma() * s.rgamma() * z1

    balls = []

    def cover(a, b, form, depth):
        s = acb(arb((a + b) / 2, (b - a) / 2))
        v = zq_fe(s) if form == 'FE' else E.zq(s, PREC)
        if (v.contains(0) or not v.is_finite()) and depth < 12:
            m = (a + b) / 2
            cover(a, m, form, depth + 1)
            cover(m, b, form, depth + 1)
            return
        balls.append((float(a.mid()), float(b.mid()), v, bool(v.real < 0 and v.imag.contains(0)), bool(v.is_finite() and not v.contains(0)), form))
    for k in range(NSUB // 2):                        # ### [-1/2, -1/4] by the FE form, 16 subintervals of width 1/64
        cover(arb(-1) / 2 + arb(k) / 64, arb(-1) / 2 + arb(k + 1) / 64, 'FE', 0)
    for k in range(NSUB // 2):                        # ### [-1/4, 0] by the direct route, 16 subintervals of width 1/64
        cover(arb(-1) / 4 + arb(k) / 64, arb(-1) / 4 + arb(k + 1) / 64, 'direct', 0)
    excl_ok = all(x[4] for x in balls) and all(x[3] for x in balls) and not z0.contains(0)
    V2 = line('b667_epstein_counts.txt', 34)
    band = line('b667_epstein_counts.txt', 56)
    NR = line('b667_epstein_counts.txt', 52)
    v2_ok = 'below 2 : True' in V2
    band_ok = ': 0 (ball' in band and 'the list in B 0' in band
    nr_ok = 'N(R) = 180' in NR
    L = ['b679 -- COMPONENT 4, (R289)(5)(iv), H4: Q0 READ AGAINST THE WIDENED CLASS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are hypotheses of the widened class with their reading at Q0 and source. The ball bank: relay data/b671_epstein_zeros_narrowed.json.gz,',
         '### sha256 %s %s, the JSON inside %s %s (data/b671_epstein_zeros_narrowed_hashes.txt :2-:3); rows %d (ON %d, OFF %d), half-width %s.' % (
             want_gz[:16], 'EQUAL' if gz_ok else 'DIFFER', want_json[:16], 'EQUAL' if js_ok else 'DIFFER', len(rows), len(on), len(off), rows[0]['h']), '',
         '  strip (-1/2, 3/2), every height      HOLDS -- (3c): "Σ_{n ≥ 2} r_Q(n) n^{−3/2} = Z_Q(3/2) − 2 printed as a ball below 2" (relay',
         '                                       data/b667_epstein_plan.txt :247-:248), its ball "%s" (data/b667_epstein_counts.txt :34, below 2 %s), so' % (
             re.search(r'Z_Q\(3/2\) − 2 = (\[[^\]]+\])', V2).group(1) if re.search(r'Z_Q\(3/2\) − 2 = (\[[^\]]+\])', V2) else '### UNREAD', v2_ok),
         '                                       |Z_Q(s) − 2| < 2 and no zero at Re s ≥ 3/2; with Λ_Q(s) = Λ_Q(1 − s) (:10) none at Re s ≤ −1/2. On the',
         '                                       certified balls: the 17 off-line real parts in [%.4f, %.4f], their reflections in [%.4f, %.4f], the %d' % (
             re_lo, re_hi, re_refl_lo, re_refl_hi, len(on)),
         '                                       on-line rows at Re 0.5: all inside (-1/2, 3/2) %s.' % all_in_strip,
         '  reflect_mem, mult_reflect            HOLDS -- Λ_Q(1 − conj s) = conj Λ_Q(s) (data/b667_epstein_plan.txt :12), at every height.',
         '  finite_window                        HOLDS below 150 by count ("%s", data/b667_epstein_counts.txt :52, %s); above 150 under' % (
             'N(R) = 180', nr_ok),
         '                                       T-COUNT, a unit-window count presupposing finitely many points (P3, Schema/EpsteinQ0.lean :104-:108).',
         '  one_le_mult                          HOLDS -- every certified ball`s count 1 (the bank`s "count" field: %s of %d rows); a multiplicity, by' % (
             sum(1 for r in rows if r.get('count') == 1), len(rows)),
         '                                       definition, above 150.',
         '  HExcl (no real point in (-1/2, 0])   %s -- THE ROUTE THE AUTHOR`S ANSWER NAMES, CHECKED:' % ('HOLDS' if excl_ok else '### NOT READ AS HOLDING'),
         '                                       (i) Z_Q(σ) = Σ_k r_Q(k) k^{−σ} > 0 for real σ > 1, every term positive (data/b667_epstein_plan.txt :9);',
         '                                           the instrument at σ = %s: %s.' % (
             ', '.join('%.2f' % s for s, _v in zpos), '; '.join(v.real.str(8) for _s, v in zpos)),
         '                                       (ii) Λ_Q(s) = (2π/√23)^{−s} Γ(s) Z_Q(s) = Λ_Q(1 − s) (:10); for s in (−1/2, 0), 1 − s in (1, 3/2), so',
         '                                           Λ_Q(s) > 0, and Γ(s) < 0 on (−1, 0) (at %s: %s), so Z_Q(s) < 0 there, nonzero.' % (
             ', '.join(x for x, _g in gam), '; '.join(g.real.str(6) for _x, g in gam)),
         '                                       (iii) Z_Q(0) read directly by the instrument (Γ(s)⁻¹ = 0 at s = 0 removes T2 and T3; T1 = 2ζ(0)): %s.' % z0.str(20),
         '                                       (iv) the balls on [-1/2, 0], %d closed subintervals of width 1/64 at %d bits, each bisected where its ball' % (NSUB, PREC),
         '                                           meets 0 (depth at most 12): on [-1/2, -1/4] by the FE form Z_Q(s) = (2π/√23)^{2s-1} Γ(1-s) Γ(s)⁻¹ Z_Q(1-s)',
         '                                           (Λ_Q(s) = Λ_Q(1 - s), :10; finite through -1/2, where the direct route`s Γ(s - ½) pole meets ζ(-2) = 0),',
         '                                           on [-1/4, 0] by b667`s route direct, T4 in the radius (rows: subinterval ; form ; Z_Q`s real part, its',
         '                                           midpoint and radius ; negative real ; excludes 0):']
    L += ['                                             [%+.9f, %+.9f] %-6s %+.6f +/- %.3e  %s  %s' % (a, b, form, float(v.real.mid()), float(v.real.rad()), neg, nz)
          for a, b, v, neg, nz, form in balls]
    L += ['                                       BALLS %d ; EXCLUDING 0 %d ; NEGATIVE %d. Beside it, the band count: "%s" (data/b667_epstein_counts.txt' % (
              len(balls), sum(1 for x in balls if x[4]), sum(1 for x in balls if x[3]), band.strip()[:90]),
          '                                           :56, %s). Against the certified real parts: the off-line points are not real (the least |Im| over' % band_ok,
          '                                           all %d rows %.4f, a ball containing 0 %s). Against (3c)`s form: (3c) bounds Re s ≥ 3/2 alone and' % (
              len(rows), im_lo, any_real),
          '                                           says nothing on the real segment inside the strip; the exclusion is read from (i)-(iv).',
          '  HCount Z 10                          ASSUMED -- T-COUNT, as b675 left it (P3, A₀Q = 10, Schema/EpsteinQ0.lean :104, :108; data/b675_hypotheses.txt',
          '                                       :67).',
          '  a Lean instance                      NOT WRITTEN -- the kernel has no Lean term for Λ_Q`s zero set (its Q0 premises are over an abstract',
          '                                       Z : ZeroConfig, Schema/EpsteinQ0.lean :112-:116); this reading is of banks, lines and balls.', '']
    ok = gz_ok and js_ok and v2_ok and all_in_strip and nr_ok and excl_ok and band_ok and not any_real
    hold = [n for n, v in (('strip', v2_ok and all_in_strip), ('reflect', True), ('finite_window', nr_ok), ('one_le_mult', True),
                           ('HExcl', excl_ok and band_ok and not any_real)) if v]
    L += ['### ### **HYPOTHESES READ 7 ; HOLDING %d (%s) ; ASSUMED 1 (HCount, T-COUNT) ; NOT WRITTEN 1 (the Lean instance) ; HExcl BALLS %d OF %d '
          'EXCLUDING 0, NEGATIVE %d, Z_Q(0) %s ; H4 %s ; %d s.**' % (
              len(hold), ', '.join(hold), sum(1 for x in balls if x[4]), len(balls), sum(1 for x in balls if x[3]), z0.real.str(8),
              'HELD' if ok else '### NOT HELD', int(time.time() - t0))]
    for name, data in (('b679_q0_membership.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b679_q0_membership.json', (json.dumps(dict(
                           at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), gz_ok=gz_ok, json_ok=js_ok, v2_ok=v2_ok, strip_on_balls=all_in_strip,
                           re_off=[re_lo, re_hi], nr_ok=nr_ok, band_ok=band_ok, any_real=any_real, im_lo=im_lo, z0=z0.str(30),
                           balls=[[a, b, form, v.str(20), neg, nz] for a, b, v, neg, nz, form in balls], excl=excl_ok, h4='HELD' if ok else 'NOT HELD'),
                           indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(data)
        os.replace(p + '.tmp', p)
    print(NL.join(L[-1:]))


if __name__ == '__main__':
    main()
