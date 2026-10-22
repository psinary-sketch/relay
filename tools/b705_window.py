# -*- coding: utf-8 -*-
"""b705_window.py -- THE NOTCHED WEIL WINDOW OF b518 AT THE LOWEST BAND ZERO, (R315)(7)(ii), AS data/b703_registrations.txt (ii) REGISTERED IT
BESIDE THE DETECTION LAW (:29-:30, committed alone at relay b8a36309, unchanged): "the notched Weil window of b518 at that zero, computed at
b705; its falsifier a nonnegative reading at every width 32 to 192; its control the centred window and the zeta windows".

### THE ZERO: the lowest-height certified off-line zero of Q0 in (1/2, 7/8], data/b703_q0_band.txt :18 -- 0.79799715717868013876 +
### 29.55176109862911459913 i (the detection law`s pair 1, data/b705_detection.txt). THE WINDOW: b694`s two families on one ladder, IMPORTED
### unedited from tools/b694_witness_terms.py (Window :106) with gamma_0 set to the band zero`s ordinate: N, b518`s notched window
### h_a(u) = (gamma_0^2 + D^2)[cos(gamma_0 u) phi_a(u)] (its transform (gamma_0^2 - z^2) g^(z), notched at the ordinate); C, the centred window
### cos(gamma_0 u) phi_a(u); phi_a the sixth-order cardinal B-spline on [-L, L], L = log a; k = h * h. THE TERMS at each width, IMPORTED unedited
### from tools/b696_witness_balls.py (terms :179): P = k^(i/2) + k^(-i/2); PR = SUM_n c(n) n^(-1/2) 2 k(log n), c = Lambda_Q at Q0 (Dirichlet
### inversion of r_Q/2 in balls), Lambda at zeta; A = (1/2 pi) INT k^(r) bracket(r) dr over [0, 4000] doubled with the archimedean tail beyond
### as b696`s DLMF ball (arch_tail :90) in the radius; S = P - PR + A, every value a ball at 128 bits. THE READING per width: the sign of S beyond
### its radius (b696`s reading :192): NEGATIVE / NONNEGATIVE BEYOND ITS BOUND / UNDECIDED. The zero-side identity (C3 of b694/b696) is not
### read this act: the registration names the window`s sign and its controls.
### THE FALSIFIER (the registration`s): a nonnegative reading at every width 32 to 192 of the notched family at Q0 -- the window then reads no
### witness at the band zero; the hypothesis HELD where some width reads negative, the least such width printed.
### THE CONTROLS, run and printed BEFORE any Q0 figure: (C1) the zeta windows, both families, every width, at the same gamma_0 -- the instrument
### where no off-line zero stands, expected NONNEGATIVE (the Weil form at zeta over a transform k^ = h^^2 >= 0 on the line; its zeros on the
### line below the height the tail bounds); a Q0 term is refused until C1 reads nonnegative at every width of both families (b694`s N4 gate,
### carried); (C2) the centred family at Q0, run before the notched family at Q0. THE ANATOMY per width: P, PR and A at Q0 and at zeta from
### this act`s units, and b694`s banked terms at rho_0 (data/b694_witness.json.gz, opened only after its sha256 and its JSON`s equal
### data/b694_witness_hashes.txt :3 and :2) at the same width and family; the term named that moves the sign: between zeta and Q0 at the band
### zero, and between rho_0 (b694) and the band zero at Q0, the term of largest change, and at each Q0 width which side of S = P - PR + A
### prevails. The widths: b694`s ladder from 32 (tools/b694_witness_terms.py :51 LADDER[2:]), '32', '48', '64', '96', '128', '192'.
### THE TAIL`S CONTOUR: the archimedean tail assumes nothing of the zeros; no zero tail enters (the identity is not read).
### Routes (each its own foreground call; one unit per (route, fam, a), appended to data/b705_window_units.jsonl, untracked, resumable):
###   zeta <fam> [a ...]      C1 at zeta        q0 <fam> [a ...]      C2 (fam C) then the reading (fam N)
###   bank                    data/b705_window_controls.txt, data/b705_window.txt, data/b705_window.json.gz beside data/b705_window_hashes.txt
### Written by the Write tool at b705; it writes only the banks it names and its units file.
"""
import gzip
import hashlib
import io
import json
import os
import sys
import time

from flint import acb, arb, ctx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b694_witness_terms as W    # noqa: E402  ### the window, imported unedited
import b696_witness_balls as WB   # noqa: E402  ### the terms with the archimedean tail as a ball, imported unedited

ACT = 'b705'
PREC = WB.PREC
ctx.prec = PREC
UNITS = os.path.join(D, '%s_window_units.jsonl' % ACT)
BAND_RE = '0.79799715717868013876'      # ### data/b703_q0_band.txt :18
BAND_IM = '29.55176109862911459913'     # ### data/b703_q0_band.txt :18 ; gamma_0 of every window here
WIDTHS = W.LADDER[2:]                   # ### '32', '48', '64', '96', '128', '192'
FAMS = W.FAMS                           # ### ('N', 'C')
B694_GZ = os.path.join(D, 'b694_witness.json.gz')
B694_HASHES = os.path.join(D, 'b694_witness_hashes.txt')
bs, bl, fmt, reading = WB.bs, WB.bl, WB.fmt, WB.reading


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put_txt(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def units():
    U = {}
    if os.path.exists(UNITS):
        for l in io.open(UNITS, encoding='utf-8'):
            if l.strip():
                u = json.loads(l)
                U[(u['route'], u['fam'], u['a'])] = u
    return U


def put_unit(u):
    u['at'] = utc()
    with open(UNITS, 'ab') as fh:
        fh.write((json.dumps(u, ensure_ascii=False) + NL).encode('utf-8'))


def window(w, fam):
    return W.Window(w, fam, g0=BAND_IM)


# ================================================================================ THE GATES (b694`s N4 gate, carried; the control before the figure)
def _zeta_ok(U):
    rows = [U.get(('zeta', f, w)) for f in FAMS for w in WIDTHS]
    if any(r is None for r in rows):
        return False, 'C1 (ZETA) NOT BANKED AT EVERY WIDTH OF BOTH FAMILIES'
    bad = [(r['fam'], r['a']) for r in rows if reading(r['S']) != 'NONNEGATIVE BEYOND ITS BOUND']
    return (not bad), ('C1 (ZETA) NOT NONNEGATIVE BEYOND ITS BOUND AT %s' % bad if bad else 'C1 (ZETA) NONNEGATIVE AT EVERY WIDTH OF BOTH FAMILIES')


def _c2_ok(U):
    rows = [U.get(('q0', 'C', w)) for w in WIDTHS]
    if any(r is None for r in rows):
        return False, 'C2 (THE CENTRED WINDOW AT Q0) NOT BANKED AT EVERY WIDTH'
    return True, 'C2 (THE CENTRED WINDOW AT Q0) BANKED AT EVERY WIDTH: ' + ', '.join('%s %s' % (r['a'], reading(r['S'])[:3]) for r in rows)


def _run(route, obj, fam, widths):
    U = units()
    if obj == 'q0':
        ok, why = _zeta_ok(U)
        if not ok:
            sys.exit('### %s -- NO Q0 TERM COMPUTED (the control before the figure)' % why)
        print('  ' + why)
        if fam == 'N':
            ok, why = _c2_ok(U)
            if not ok:
                sys.exit('### %s -- NO NOTCHED Q0 TERM COMPUTED (the control before the figure)' % why)
            print('  ' + why)
    for w in widths:
        if (route, fam, w) in U:
            print('  %s %s a %-4s banked: S %s %s' % (route, fam, w, fmt(bl(U[(route, fam, w)]['S'])), reading(U[(route, fam, w)]['S'])))
            continue
        Wd = window(w, fam)
        u = WB.terms(Wd, obj)
        u.update(route=route, fam=fam, a=w, obj=obj, prec=PREC, g0=BAND_IM, L=bs(Wd.L), reading=reading(u['S']))
        put_unit(u)
        print('  %s %s a %-4s P %s | PR %s (%d terms to n %d) | A %s (tail ball %s) | S %s | %s | %d s' % (
            route, fam, w, fmt(bl(u['P']), 8), fmt(bl(u['PR']), 10), u['prime_terms'], u['nmax'], fmt(bl(u['A']), 10), fmt(bl(u['tail']), 3),
            fmt(bl(u['S'])), u['reading'], u['seconds']), flush=True)


def zeta(fam, *a):
    _run('zeta', 'zeta', fam, a or WIDTHS)


def q0(fam, *a):
    _run('q0', 'q0', fam, a or WIDTHS)


# ================================================================================ b694`S TERM BANK AT rho_0, THROUGH ITS HASHES
def _b694():
    H = io.open(B694_HASHES, encoding='utf-8').read().replace(chr(13), '').split(NL)
    want_gz, want_js = H[2].split('sha256 ')[1].split(' ')[0], H[1].split('sha256 ')[1].split(' ')[0]
    gzb = open(B694_GZ, 'rb').read()
    raw = gzip.decompress(gzb)
    have_gz, have_js = hashlib.sha256(gzb).hexdigest(), hashlib.sha256(raw).hexdigest()
    if have_gz != want_gz or have_js != want_js:
        sys.exit('### data/b694_witness.json.gz %s / its JSON %s DO NOT EQUAL data/b694_witness_hashes.txt :3 %s / :2 %s -- NOT READ' % (
            have_gz[:16], have_js[:16], want_gz[:16], want_js[:16]))
    j = json.loads(raw.decode('utf-8'))
    O = {}
    for u in j['units']:
        if u.get('route') in ('zeta', 'q0') and u.get('prec', 128) == 128:
            O[(u['route'], u['fam'], u['a'])] = u
    return O, have_gz, have_js


def _mover(x, y, names=('P', 'PR', 'A')):
    """the term of largest change from x to y (dicts of ball lists), with every change."""
    ch = {n: bl(y[n]) - bl(x[n]) for n in names}
    top = max(names, key=lambda n: abs(float(ch[n].mid())))
    return top, ch


def _prevails(u):
    P, PR, A = (bl(u[n]) for n in ('P', 'PR', 'A'))
    plus = P + A
    if plus > PR:
        return 'P + A exceeds PR by %s' % fmt(plus - PR, 6)
    if PR > plus:
        return 'PR exceeds P + A by %s' % fmt(PR - plus, 6)
    return 'P + A and PR undecided within their balls'


# ================================================================================ THE BANKS
def bank(*a):
    U = units()
    need = [(r, f, w) for r in ('zeta', 'q0') for f in FAMS for w in WIDTHS]
    miss = [k for k in need if k not in U]
    if miss:
        sys.exit('### UNITS MISSING -- NOTHING WRITTEN: %s' % miss)
    O, gz_sha, js_sha = _b694()
    zeta_ok, zeta_why = _zeta_ok(U)
    c2 = [U[('q0', 'C', w)] for w in WIDTHS]
    nn = [U[('q0', 'N', w)] for w in WIDTHS]
    neg = [u['a'] for u in nn if u['reading'] == 'NEGATIVE BEYOND ITS BOUND']
    nonneg_all = all(u['reading'] == 'NONNEGATIVE BEYOND ITS BOUND' for u in nn)
    undecided = [u['a'] for u in nn if u['reading'] == 'UNDECIDED']
    verdict = 'REFUTED' if nonneg_all else ('HELD' if neg else 'UNDECIDED')
    # --- the controls bank
    C = ['%s -- (R315)(7)(ii): THE WINDOW`S CONTROLS AT THE BAND ZERO, RUN BEFORE ANY Q0 FIGURE (%s)' % (ACT, utc()), '',
         '### gamma_0 = %s (the band zero`s ordinate, data/b703_q0_band.txt :18); the window tools/b694_witness_terms.py Window :106 and the' % BAND_IM,
         '### terms tools/b696_witness_balls.py terms :179, both imported unedited. Rows are widths: family | a | P | PR | A (the archimedean tail',
         '### ball in its radius) | S = P - PR + A | the reading | seconds.', '',
         '### (C1) THE ZETA WINDOWS, both families, every width -- the instrument where no off-line zero stands (b694`s N4 gate: a Q0 term is',
         '### refused until every row reads NONNEGATIVE BEYOND ITS BOUND):']
    for f in FAMS:
        for w in WIDTHS:
            u = U[('zeta', f, w)]
            C.append('  %s | %-4s | P %s | PR %s | A %s | S %s | %s | %d s' % (f, w, fmt(bl(u['P']), 8), fmt(bl(u['PR']), 10), fmt(bl(u['A']), 10),
                                                                              fmt(bl(u['S'])), u['reading'], u['seconds']))
    C += ['  ' + zeta_why, '', '### (C2) THE CENTRED WINDOW AT Q0, every width, run before the notched family at Q0:']
    for u in c2:
        C.append('  C | %-4s | P %s | PR %s | A %s | S %s | %s | %d s' % (u['a'], fmt(bl(u['P']), 8), fmt(bl(u['PR']), 10), fmt(bl(u['A']), 10),
                                                                         fmt(bl(u['S'])), u['reading'], u['seconds']))
    c2_neg = [u['a'] for u in c2 if u['reading'] == 'NEGATIVE BEYOND ITS BOUND']
    C += ['', '### ### **C1 ZETA NONNEGATIVE AT EVERY WIDTH OF BOTH FAMILIES %s ; C2 THE CENTRED WINDOW AT Q0 NEGATIVE AT %s.**' % (
        zeta_ok, c2_neg or 'NO WIDTH')]
    put_txt('%s_window_controls.txt' % ACT, C)
    # --- the reading bank
    L = ['%s -- (R315)(7)(ii): THE NOTCHED WEIL WINDOW OF b518 AT THE LOWEST BAND ZERO, AS data/b703_registrations.txt (ii) REGISTERED IT BESIDE' % ACT,
         'THE DETECTION LAW (:29-:30) (%s)' % utc(), '',
         '### THE ZERO: %s + %s i (data/b703_q0_band.txt :18, the lowest-height certified off-line zero of Q0 in (1/2, 7/8]; the' % (BAND_RE, BAND_IM),
         '### detection law`s pair 1). The window: b518`s notched family N at gamma_0 = the zero`s ordinate, b694`s ladder from 32 (tools/',
         '### b694_witness_terms.py :51), its terms in balls at 128 bits by tools/b696_witness_balls.py terms :179 (the archimedean tail beyond',
         '### R = 4000 as a DLMF ball in the radius; no zero tail: the identity is not read this act). The controls in data/b705_window_controls.txt.',
         '### Rows are widths: a | P | PR | A | S = P - PR + A | the reading (the sign beyond the ball`s radius) | which side prevails.', '',
         '### THE READING, THE NOTCHED FAMILY N AT Q0:']
    for u in nn:
        L.append('  %-4s | P %s | PR %s | A %s | S %s | %s | %s' % (u['a'], fmt(bl(u['P']), 8), fmt(bl(u['PR']), 12), fmt(bl(u['A']), 12),
                                                                   fmt(bl(u['S']), 14), u['reading'], _prevails(u)))
    L += ['', '### THE FALSIFIER (a nonnegative reading at every width 32 to 192): %s ; negative at %s ; undecided at %s' % (
        'FIRED' if nonneg_all else 'NOT FIRED', neg or 'NO WIDTH', undecided or 'NO WIDTH'),
          '### THE REGISTRATION`S HYPOTHESIS (the notched window at the band zero reads a witness): %s%s' % (
              verdict, (' -- NEGATIVE FROM WIDTH %s' % neg[0]) if neg else (' -- NONNEGATIVE AT EVERY WIDTH' if nonneg_all else '')), '',
          '### THE TERM ANATOMY per width (rows: family | a | the object | P | PR | A | S): this act`s terms at the band zero at Q0 and at zeta, and',
          '### b694`s banked terms at rho_0 = 0.953... + 16.290... i (data/b694_witness.json.gz, read after its sha256 %s... and its JSON`s %s...' % (gz_sha[:12], js_sha[:12]),
          '### equalled data/b694_witness_hashes.txt :3 and :2) at the same family and width; the mover: the term of largest change.']
    anatomy = []
    for f in FAMS:
        for w in WIDTHS:
            uq, uz, ob = U[('q0', f, w)], U[('zeta', f, w)], O.get(('q0', f, w))
            oz = O.get(('zeta', f, w))
            L.append('  %s | %-4s | Q0 at the band zero  | P %s | PR %s | A %s | S %s %s' % (
                f, w, fmt(bl(uq['P']), 8), fmt(bl(uq['PR']), 12), fmt(bl(uq['A']), 12), fmt(bl(uq['S']), 12), uq['reading'][:3]))
            L.append('  %s | %-4s | zeta at the band g0  | P %s | PR %s | A %s | S %s %s' % (
                f, w, fmt(bl(uz['P']), 8), fmt(bl(uz['PR']), 12), fmt(bl(uz['A']), 12), fmt(bl(uz['S']), 12), uz['reading'][:3]))
            m1, ch1 = _mover(uz, uq)
            row = dict(fam=f, a=w, zeta_to_q0=dict(mover=m1, **{n: bs(c) for n, c in ch1.items()}))
            L.append('      zeta -> Q0 at the band zero: dP %s, dPR %s, dA %s ; THE MOVER %s' % (fmt(ch1['P'], 6), fmt(ch1['PR'], 6), fmt(ch1['A'], 6), m1))
            if ob:
                L.append('  %s | %-4s | Q0 at rho_0 (b694)   | P %s | PR %s | A %s | S %s %s' % (
                    f, w, fmt(bl(ob['P']), 8), fmt(bl(ob['PR']), 12), fmt(bl(ob['A']), 12), fmt(bl(ob['S']), 12), W.reading(ob['S'])[0][:3]))
                m2, ch2 = _mover(ob, uq)
                row['rho0_to_band'] = dict(mover=m2, **{n: bs(c) for n, c in ch2.items()})
                L.append('      rho_0 -> the band zero at Q0: dP %s, dPR %s, dA %s ; THE MOVER %s' % (fmt(ch2['P'], 6), fmt(ch2['PR'], 6), fmt(ch2['A'], 6), m2))
            if oz:
                L.append('  %s | %-4s | zeta at rho_0`s g0   | P %s | PR %s | A %s | S %s %s' % (
                    f, w, fmt(bl(oz['P']), 8), fmt(bl(oz['PR']), 12), fmt(bl(oz['A']), 12), fmt(bl(oz['S']), 12), W.reading(oz['S'])[0][:3]))
            anatomy.append(row)
    movers = [r['zeta_to_q0']['mover'] for r in anatomy if r['fam'] == 'N']
    L += ['', '### ### **THE NOTCHED WINDOW AT THE BAND ZERO: %s AT %s ; THE FALSIFIER %s ; THE HYPOTHESIS %s ; C1 ZETA NONNEGATIVE %s ; C2 CENTRED AT Q0 NEGATIVE AT %s ; THE MOVER (N, zeta -> Q0) %s.**' % (
        'NEGATIVE' if neg else 'NONNEGATIVE', neg or 'NO WIDTH', 'FIRED' if nonneg_all else 'NOT FIRED', verdict, zeta_ok, c2_neg or 'NO WIDTH',
        sorted(set(movers)))]
    put_txt('%s_window.txt' % ACT, L)
    J = dict(at=utc(), zero=dict(re=BAND_RE, im=BAND_IM, cite='data/b703_q0_band.txt :18'), widths=list(WIDTHS), prec=PREC, verdict=verdict,
             negative_at=neg, undecided_at=undecided, falsifier_fired=nonneg_all, c1_zeta_nonneg=zeta_ok, c2_centred_negative_at=c2_neg,
             b694_bank=dict(gz_sha256=gz_sha, json_sha256=js_sha),
             units=[dict((k, v) for k, v in U[k_].items()) for k_ in need], anatomy=anatomy)
    gz = os.path.join(D, '%s_window.json.gz' % ACT)
    raw = (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(gz + '.tmp', 'wb') as fh:
        fh.write(gzip.compress(raw, 9, mtime=0))
    os.replace(gz + '.tmp', gz)
    gzb = open(gz, 'rb').read()
    put_txt('%s_window_hashes.txt' % ACT, ['%s -- THE WINDOW`S BINARY BANK, ITS HASHES (data/b680_rules.txt row (1)) (%s)' % (ACT, utc()), '',
                                            '### rows: path ; sha256 ; bytes, LF (the json inside the gz and the gz itself)',
                                            'data/%s_window.json.gz ; %s ; %d' % (ACT, hashlib.sha256(gzb).hexdigest(), len(gzb)),
                                            'data/%s_window.json (inside the gz) ; %s ; %d' % (ACT, hashlib.sha256(raw).hexdigest(), len(raw))])
    print(NL.join(C[-1:] + L[9:]))


ROUTES = dict(zeta=zeta, q0=q0, bank=bank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b705_window.py zeta <fam> [a ...] | q0 <fam> [a ...] | bank')
        sys.exit(2)
    fn(*sys.argv[2:])
