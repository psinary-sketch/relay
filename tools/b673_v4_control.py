# -*- coding: utf-8 -*-
"""b673_v4_control.py -- (R283)(4): THE NUMERICAL CONTROL ON V4'S CONSTANT AT Q0, BEFORE ANY LEAN. Written by the Write tool at b673.

### The input: b671's narrowed balls, relay data/b671_epstein_zeros_narrowed.json.gz, its sha256 checked against b671's hashes bank before
### the read (tools/b673_worklist.py Q0_NARROWED_SHA, data/b671_epstein_zeros_narrowed_hashes.txt :3), read through gzip, no copy written.
### The configuration's dominant set: the off-line points of the list lie right of the line (σ > 1/2), so the points with ‖z‖ > 1,
### z = 1 - 1/ρ, are their reflections ρ' = 1 - conj ρ, with ‖z'‖^2 = 1 + (2σ - 1)/((1 - σ)^2 + γ^2); every reflection's ‖z'‖ printed in
### balls and the largest named; the dominant pair is that reflection and its conjugate (Q0's zeros symmetric under conjugation),
### multiplicities one, so c = Σ m^2 / (4 Σ m) = 2 / 8 = 1/4.
### s_n = w^n + conj(w)^n = 2 Re(w^n), w = z'/‖z'‖ from the ball, computed in Arb balls at 256 bits for n = 1..4000; a row per n: its ball, and
### CERTIFIED AT OR ABOVE c (the ball's lower end ≥ 1/4), CERTIFIED AT OR BELOW -c (its upper end ≤ -1/4), or NEITHER. The control is on
### the statement's constant, not on the theorem. (C2) planted: one w replaced by 1, s_n = 1 + conj(w)^n, its mean over n < N printed
### tending to 1 (the multiplicity of the entry equal to 1) and not to 0; the control's own mean printed beside it, tending to 0.
### Writes data/b673_v4_control.txt and data/b673_v4_control.json alone.
"""
import gzip
import hashlib
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b673_worklist as K   # noqa: E402
from flint import arb, acb, ctx   # noqa: E402


def main():
    ctx.prec = 256
    p = os.path.join(D, K.Q0_NARROWED)
    b = open(p, 'rb').read()
    sha = hashlib.sha256(b).hexdigest()
    if sha != K.Q0_NARROWED_SHA:
        sys.exit('### THE NARROWED LIST`S sha256 %s IS NOT b671`S %s -- NOTHING READ' % (sha, K.Q0_NARROWED_SHA))
    raw = gzip.decompress(b)
    if hashlib.sha256(raw).hexdigest() != K.Q0_NARROWED_JSON_SHA:
        sys.exit('### THE JSON INSIDE THE .gz IS NOT b671`S -- NOTHING READ')
    j = json.loads(raw.decode('utf-8'))
    off = [r for r in j['rows'] if r['kind'] == 'OFF']
    c = arb(1) / 4
    L = ['b673 -- (R283)(4): THE NUMERICAL CONTROL ON V4`S CONSTANT AT Q0, RUN BEFORE ANY LEAN (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the input: relay data/%s, sha256 %s (EQUAL to b671`s hashes bank), the JSON inside %s; %d rows, %d off-line; Arb balls at %d bits.' % (
             K.Q0_NARROWED, sha[:16], K.Q0_NARROWED_JSON_SHA[:16], len(j['rows']), len(off), ctx.prec), '',
         '### THE DOMINANT SET: each off-line point ρ (σ > 1/2) and its reflection ρ` = 1 - conj ρ; ‖z`‖ = ‖1 - 1/ρ`‖ in balls (rows are points):']
    cand = []
    for r in off:
        h = arb(r['h'])
        rho = acb(arb(r['re'], h), arb(r['im'], h))
        rp = 1 - rho.conjugate()
        zp = 1 - 1 / rp
        cand.append((r['idx'], rho, rp, zp, abs(zp)))
        L.append('    idx %-3d ρ = %s + %si ; ρ` = 1 - conj ρ, ‖ρ`‖ %s ; ‖z`‖ %s' % (r['idx'], r['re'][:20], r['im'][:20], abs(rp).str(12, radius=False),
                                                                          abs(zp).str(20, radius=True)))
    top = max(cand, key=lambda x: x[4].mid())
    small = min(cand, key=lambda x: abs(x[2]).mid())
    others = [x for x in cand if x[0] != top[0]]
    sep = all((top[4] - x[4]) > 0 for x in others)
    L += ['### the largest ‖z`‖: idx %d, certified above every other in balls %s ; the off-line zero of smallest ‖ρ`‖: idx %d ; THE SAME POINT %s' % (
        top[0], sep, small[0], top[0] == small[0]),
        '### the dominant pair: ρ` of idx %d and its conjugate, multiplicities one: Σ m = 2, Σ m^2 = 2, c = Σ m^2 / (4 Σ m) = 1/4.' % top[0], '']
    w = top[3] / abs(top[3])
    L += ['### w = z`/‖z`‖ = %s ; ‖w‖ - 1 = %s ; θ = arg w = %s ; w^n read as e^{inθ}, Re s_n = 2 cos(nθ)' % (
        w.str(24, radius=True), (abs(w) - 1).str(5, radius=True), w.arg().str(24, radius=True)), '',
          '### ROWS ARE n: n ; Re s_n = 2 Re(w^n) in balls ; CERTIFIED AT OR ABOVE c, CERTIFIED AT OR BELOW -c, or NEITHER']
    # ### the first run multiplied the complex ball by w at each step, and the rectangular ball's radius grew by about (|Re w| + |Im w|) per
    # ### step, past the value near n = 1000 (b673 defect (f)): w^n is read through its angle instead, θ = arg w a real ball, w^n = e^{inθ},
    # ### Re s_n = 2 cos(nθ), whose radius grows as n rad θ
    rows = []
    th = w.arg()
    up = dn = neither = 0
    first_up = first_dn = None
    mean = arb(0)
    mean2 = arb(0)
    for n in range(1, K.CONTROL_N + 1):
        cn = (n * th).cos()
        s = 2 * cn
        if (s - c) >= 0:
            v, up = 'CERTIFIED AT OR ABOVE c', up + 1
            first_up = first_up or n
        elif (s + c) <= 0:
            v, dn = 'CERTIFIED AT OR BELOW -c', dn + 1
            first_dn = first_dn or n
        else:
            v, neither = 'NEITHER', neither + 1
        mean += s
        mean2 += 1 + cn
        rows.append(dict(n=n, mid=float(s.mid()), rad=float(s.rad()), reading=v))
        L.append('    %4d  %s  %s' % (n, s.str(15, radius=True), v))
    N = K.CONTROL_N
    m1, m2 = mean / N, mean2 / N
    L += ['', '### (C2), PLANTED: one w replaced by 1 -- s`_n = 1 + conj(w)^n; its mean over n = 1..%d is %s, tending to 1 (the multiplicity of the '
              'entry equal to 1), not to 0; the control`s own mean over the same n is %s, tending to 0.' % (N, m2.str(10, radius=True), m1.str(10, radius=True)),
          '', '### ### **V4`S CONSTANT AT Q0: c = 1/4 ; n = 1..%d ; CERTIFIED AT OR ABOVE c %d, THE LEAST n %s ; CERTIFIED AT OR BELOW -c %d, THE LEAST n %s ; '
              'NEITHER %d ; (C2) MEAN %s (AS PLANTED: %s).**' % (N, up, first_up, dn, first_dn, neither, m2.str(6, radius=False),
                                                              abs(float(m2.mid()) - 1) < 0.01 and abs(float(m1.mid())) < 0.01)]
    out = io.open(os.path.join(D, 'b673_v4_control.txt'), 'w', encoding='utf-8', newline=NL)
    out.write(NL.join(L) + NL)
    out.close()
    js = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), input=K.Q0_NARROWED, sha256=sha, dominant_idx=top[0], dominant_separated=sep,
              smallest_rho_idx=small[0], c='1/4', N=N, up=up, first_up=first_up, down=dn, first_down=first_dn, neither=neither,
              c2_mean=float(m2.mid()), control_mean=float(m1.mid()), rows=rows)
    o2 = io.open(os.path.join(D, 'b673_v4_control.json'), 'w', encoding='utf-8', newline=NL)
    o2.write(json.dumps(js, indent=1, ensure_ascii=False) + NL)
    o2.close()
    print(NL.join(L[:len(off) + 9]))
    print(L[-1])


if __name__ == '__main__':
    main()
