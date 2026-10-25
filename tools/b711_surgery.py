# -*- coding: utf-8 -*-
"""b711_surgery.py -- THE SURGERY AT Q0'S ONSET RADII, (R321)(5), AS data/b710_registrations.txt (ii) REGISTERED IT (:51-:69, committed at b710's
step zero before any number, unchanged): "the Weil form of Q0 (the Epstein zeta of x^2 + xy + 6y^2), S = P - PR + A on the family F_a(gamma_0) =
span{C, N}, as b707's tool computes it in balls and b709's grid read it, with its prime side's coefficients at the n that are NOT prime powers
removed -- the composition terms; the coefficients at prime powers kept as they stand. Read at each family's onset radius as b709 placed it: the
band zero's at the rung log 32381 (a = 10.38532711) and rho_0's at the midpoint between log 929 and log 937 (a = 6.838396011)".

### THE FORM, b709's unchanged (tools/b709_grid.py, IMPORTED unedited: grid, _window, prime_sum709, _prime_powers, INTERVAL, FREQS, KINDS; through it
### tools/b707_onset.py gram and reading, tools/b694_witness_terms.py lambda_q and lambda_z, tools/b696_witness_balls.py a_int, arch_tail and
### unit_ball): terms709 (:228-:248) read line for line in `terms` below with the coefficient list a parameter, so the one change is the list.
### THE OPERATION: Lambda_Q(n) set to the zero ball at every n <= the family's top that is not a prime power (the sieve of _prime_powers); the
### archimedean term A and the polar term P do not depend on the list and are computed once per window, PR twice (the list as it stands, the list
### operated). THE QUANTITY: the least eigenvalue of the operated 2 x 2 form in the L2 metric at each onset point, read POSITIVE DEFINITE, NEGATIVE
### DIRECTION or UNDECIDED beyond its bound (b707's reading); beside it the share of the prime side carried by non-prime-power n, per window: the
### removed part (PR as it stands less PR operated) over PR as it stands, in balls.
### THE CONTROLS, computed and printed BEFORE any operated figure: (C1) zeta unchanged by the operation -- its list's entries off the prime powers
### all the zero ball, and the operated zeta form's S per window equal to the unoperated one's, both points; (C2) the unoperated Q0 form reproducing
### b709's onset eigenvalues -- each window's S and k(0) equal to b709's banked unit (data/b709_grid_units_seg_qC.jsonl for the band's,
### data/b709_grid_units_rho0_q0.jsonl for rho_0's; the units files b709's grid tool declares) and lambda_min equal to the registration's figure
### (:65-:66) at its printed digits.
### THE HYPOTHESIS (:60-:61) and THE FALSIFIER (:62) printed HELD / REFUTED: HELD where the operated form is POSITIVE DEFINITE beyond its bound at
### both onsets, REFUTED where it is NEGATIVE DIRECTION beyond its bound at either, UNDECIDED otherwise. THE SCOPE (:67-:68), printed with the
### figures: the corrected prime side is not the log-derivative of a function with these zeros; the surgery attributes the form's prime-side
### expression and states nothing about any function's zeros.
### Routes: `run [dry]` -> the controls, then the figures, printed; without `dry` written to data/b711_surgery.txt, data/b711_surgery.json and
### data/b711_surgery_hashes.txt (each bank's sha256). Written by the Write tool at b711; it writes only those three banks. Every value a ball
### (python-flint) at 128 bits. Nothing here proves RH or GRH or locates any zero.
"""
import hashlib
import io
import json
import math
import os
import sys
import time

from flint import acb, arb, fmpq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b709_grid as G             # noqa: E402  ### b709's grid, imported unedited
O7, W, WB = G.O7, G.W, G.WB
bs, bl, fmt = G.bs, G.bl, G.fmt

ACT = 'b711'
REG = 'data/b710_registrations.txt'
POINTS = (('band', 'rung32381'), ('rho0', 'mid929_937'))          # ### :55-:56
B709_UNITS = dict(band='b709_grid_units_seg_qC.jsonl', rho0='b709_grid_units_rho0_q0.jsonl')
B709_LMIN = dict(band='-3.5300862e-5', rho0='-0.0037191321')      # ### :65-:66, data/b709_report.txt :16


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def terms(fam, pt, kind, obj, lam):
    """b709's terms709 (tools/b709_grid.py :228-:248) with the coefficient list `lam` given: P and A per window, PR for the list."""
    Wd = G._window(fam, pt, kind)
    N = pt['N']
    nmax = math.isqrt(N)
    P = (Wd.khat(acb(0, 0.5)) + Wd.khat(acb(0, -0.5))).real
    Ai = WB.a_int(Wd, obj, 0, G.R_INT)
    tl = WB.arch_tail(Wd, obj, G.R_INT)
    A = Ai + WB.unit_ball(tl)
    k0 = Wd.kval(arb(0), fmpq(0))
    out = {}
    for name, ls in lam.items():
        PR, nterms, absum = G.prime_sum709(Wd, N, ls, nmax)
        out[name] = dict(P=bs(P), PR=bs(PR), A=bs(A), tail=bs(tl), S=bs(P - PR + A), k0=bs(k0), nmax=nmax, prime_terms=nterms, absum=absum)
    return out


def _lists(fam, obj):
    top = int(G.INTERVAL[fam][1]) ** 2
    lam = W.lambda_q(top)[0] if obj == 'q0' else W.lambda_z(top)
    pp = set(q for _p, _k, q in G._prime_powers(1, top))
    op = [x if (n in pp) else arb(0) for n, x in enumerate(lam)]
    off_nonzero = sum(1 for n in range(2, top + 1) if n not in pp and not lam[n].is_zero())
    return dict(full=lam, operated=op), off_nonzero, top, len(pp)


def _b709_units(fam, name):
    out = {}
    for l in io.open(os.path.join(D, B709_UNITS[fam]), encoding='utf-8'):
        if l.strip():
            u = json.loads(l)
            if u.get('route') == 'terms' and u.get('point') == name and u.get('obj') == 'q0' and u.get('fam') == fam:
                out[u['kind']] = u
    return out


def compute():
    R = {}
    for fam, name in POINTS:
        pt = next(p for p in G.grid(fam) if p['name'] == name)
        for obj in ('zeta', 'q0'):
            lam, off_nz, top, npp = _lists(fam, obj)
            t0 = time.time()
            U = dict((kd, terms(fam, pt, kd, obj, lam)) for kd in G.KINDS)
            forms = {}
            for ver in ('full', 'operated'):
                Gm, M = O7.gram(*[U[kd][ver] for kd in G.KINDS])
                forms[ver] = O7.reading(Gm, M)
            R[(fam, obj)] = dict(point=name, a=bs(2 * G._window(fam, pt, 'C').L), N=pt['N'], top=top, prime_powers=npp, off_nonzero=off_nz,
                                 units=U, forms=forms, seconds=int(time.time() - t0))
            print('  computed %s %s at %s in %d s' % (fam, obj, name, R[(fam, obj)]['seconds']), flush=True)
    return R


def _share(u):
    full, op = bl(u['full']['PR']), bl(u['operated']['PR'])
    return (full - op) / full


def lines(R):
    L = ['%s -- COMPONENT 3, (R321)(5): THE SURGERY AT Q0`S ONSET RADII, AS %s (ii) REGISTERED IT (:51-:69) (%s)' % (ACT, REG, utc()), '',
         '### rows are readings at the two onset points (the band zero`s family at rung32381, rho_0`s at mid929_937; b709`s grid points, tools/b709_grid.py',
         '### grid); the form S = P - PR + A per window C, N, CN (b709`s terms709, the coefficient list the one change), the 2 x 2 form`s least eigenvalue',
         '### in the L2 metric, b707`s reading. THE CONTROLS FIRST, THEN THE FIGURES.', '']
    # ### (C1) zeta unchanged
    c1 = []
    for fam, name in POINTS:
        z = R[(fam, 'zeta')]
        eq = all(z['units'][kd]['full']['S'] == z['units'][kd]['operated']['S'] for kd in G.KINDS)
        same = z['forms']['full']['lmin'] == z['forms']['operated']['lmin']
        c1.append(dict(fam=fam, off_nonzero=z['off_nonzero'], S_equal=eq, lmin_equal=same, ok=z['off_nonzero'] == 0 and eq and same,
                       lmin=z['forms']['full']['lmin'], reading=z['forms']['full']['reading']))
    L += ['### (C1) ZETA UNCHANGED BY THE OPERATION (Lambda vanishes off the prime powers):']
    for c in c1:
        L.append('  %-5s %-11s | Lambda off the prime powers nonzero at %d n | S per window operated = unoperated %s | lambda_min equal %s (%s, %s) | %s' % (
            c['fam'], dict(POINTS)[c['fam']], c['off_nonzero'], c['S_equal'], c['lmin_equal'], fmt(bl(c['lmin']), 10), c['reading'], 'AS WANTED' if c['ok'] else '### NOT AS WANTED'))
    # ### (C2) the unoperated Q0 form against b709
    c2 = []
    for fam, name in POINTS:
        q = R[(fam, 'q0')]
        b = _b709_units(fam, name)
        eqS = all(kd in b and b[kd]['S'] == q['units'][kd]['full']['S'] for kd in G.KINDS)
        eqK = all(kd in b and b[kd]['k0'] == q['units'][kd]['full']['k0'] for kd in G.KINDS)
        lm = bl(q['forms']['full']['lmin'])
        dig = len(B709_LMIN[fam].lstrip('-').replace('.', '').split('e')[0].lstrip('0'))
        printed = ('%.' + str(dig - 1) + 'e') % float(lm.mid())
        want = '%.' + str(dig - 1) + 'e'
        eqL = printed == want % float(B709_LMIN[fam])
        c2.append(dict(fam=fam, units=sorted(b), S_equal=eqS, k0_equal=eqK, lmin=q['forms']['full']['lmin'], lmin_printed=printed, registered=B709_LMIN[fam],
                       lmin_equal=eqL, reading=q['forms']['full']['reading'], ok=eqS and eqK and eqL))
    L += ['', '### (C2) THE UNOPERATED Q0 FORM AGAINST b709`S ONSET UNITS AND THE REGISTRATION`S FIGURES (:65-:66):']
    for c in c2:
        L.append('  %-5s %-11s | b709`s units %s (data/%s) | S per window equal %s | k(0) equal %s | lambda_min %s (%s) against %s at its digits %s | %s' % (
            c['fam'], dict(POINTS)[c['fam']], ''.join(c['units']), B709_UNITS[c['fam']], c['S_equal'], c['k0_equal'], fmt(bl(c['lmin']), 10), c['reading'],
            c['registered'], c['lmin_equal'], 'AS WANTED' if c['ok'] else '### NOT AS WANTED'))
    ctl_ok = all(c['ok'] for c in c1 + c2)
    L += ['', '### THE CONTROLS: C1 %s ; C2 %s -- %s' % (all(c['ok'] for c in c1), all(c['ok'] for c in c2),
                                                       'THE FIGURES FOLLOW' if ctl_ok else '### A CONTROL NOT AS WANTED: THE FIGURES PRINTED, READ AGAINST IT'), '']
    # ### the figures
    L += ['### THE FIGURES: the operated Q0 form at each onset point (composite coefficients removed; prime powers kept):']
    figs = []
    for fam, name in POINTS:
        q = R[(fam, 'q0')]
        op = q['forms']['operated']
        sh = dict((kd, _share(q['units'][kd])) for kd in G.KINDS)
        figs.append(dict(fam=fam, point=name, a=q['a'], N=q['N'], off_nonzero=q['off_nonzero'], prime_powers=q['prime_powers'], top=q['top'],
                         reading=op['reading'], lmin=op['lmin'], lmax=op['lmax'], det=op['det'], witness=op['witness'], witness_S=op['witness_S'],
                         lmin_unoperated=q['forms']['full']['lmin'], shares=dict((kd, bs(v)) for kd, v in sh.items()),
                         PR=dict((kd, dict(full=q['units'][kd]['full']['PR'], operated=q['units'][kd]['operated']['PR'])) for kd in G.KINDS),
                         S=dict((kd, dict(full=q['units'][kd]['full']['S'], operated=q['units'][kd]['operated']['S'])) for kd in G.KINDS)))
    for f in figs:
        L += ['  %-5s %-11s | a = %s | N = %d | the list to %d: %d prime powers kept, %d composite n carrying a nonzero coefficient set to zero' % (
                  f['fam'], f['point'], fmt(bl(f['a']), 10), f['N'], f['top'], f['prime_powers'], f['off_nonzero']),
              '        OPERATED lambda_min %s ; lambda_max %s ; det %s ; %s' % (fmt(bl(f['lmin']), 10), fmt(bl(f['lmax']), 10), fmt(bl(f['det']), 10), f['reading']),
              '        unoperated lambda_min %s (b709`s onset reading)' % fmt(bl(f['lmin_unoperated']), 10)]
        for kd in G.KINDS:
            L.append('        window %-2s | PR as it stands %s | PR operated %s | the composite share %s | S %s -> %s' % (
                kd, fmt(bl(f['PR'][kd]['full']), 10), fmt(bl(f['PR'][kd]['operated']), 10), fmt(bl(f['shares'][kd]), 8),
                fmt(bl(f['S'][kd]['full']), 10), fmt(bl(f['S'][kd]['operated']), 10)))
    pos = [f['reading'].startswith('POSITIVE DEFINITE') for f in figs]
    neg = [f['reading'].startswith('NEGATIVE DIRECTION') for f in figs]
    verdict = 'REFUTED' if any(neg) else ('HELD' if all(pos) else 'UNDECIDED')
    L += ['', '### THE HYPOTHESIS (:60-:61): the operated form POSITIVE DEFINITE beyond its bound at both onsets -- %s' % ('HELD' if all(pos) else 'NOT HELD'),
          '### THE FALSIFIER (:62): the operated form NEGATIVE DIRECTION beyond its bound at either onset -- %s' % ('FIRED' if any(neg) else 'NOT FIRED'),
          '### THE SCOPE (:67-:68): the corrected prime side is not the log-derivative of a function with these zeros; the surgery attributes the',
          '### form`s prime-side expression and states nothing about any function`s zeros.', '']
    L += ['### ### **THE SURGERY %s ; THE OPERATED FORM %s (band, rung32381) AND %s (rho_0, mid929_937) ; LAMBDA_MIN %s AND %s ; THE COMPOSITE SHARE (C, N, CN) %s AND %s ; '
          'C1 %s ; C2 %s.**' % (
              verdict, figs[0]['reading'], figs[1]['reading'], fmt(bl(figs[0]['lmin']), 8), fmt(bl(figs[1]['lmin']), 8),
              ' / '.join(bl(figs[0]['shares'][kd]).mid().str(4, radius=False) for kd in G.KINDS),
              ' / '.join(bl(figs[1]['shares'][kd]).mid().str(4, radius=False) for kd in G.KINDS),
              all(c['ok'] for c in c1), all(c['ok'] for c in c2))]
    return L, dict(at=utc(), registration=REG, c1=c1, c2=c2, controls_ok=ctl_ok, figures=figs, verdict=verdict, hypothesis='HELD' if all(pos) else 'NOT HELD',
                   falsifier='FIRED' if any(neg) else 'NOT FIRED')


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def run(*a):
    R = compute()
    L, j = lines(R)
    print(NL.join(L))
    if 'dry' in a:
        return
    h1 = _put('%s_surgery.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_surgery.json' % ACT, (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    H = ['%s -- THE SURGERY`S BANKS, THEIR sha256 (%s)' % (ACT, utc()), '', '  %s  data/%s_surgery.txt' % (h1, ACT), '  %s  data/%s_surgery.json' % (h2, ACT), '',
         '### ### **BANKS 2 HASHED.**']
    _put('%s_surgery_hashes.txt' % ACT, (NL.join(H) + NL).encode('utf-8'))
    print(H[-1])


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'run':
        print('usage: b711_surgery.py run [dry]')
        sys.exit(2)
    run(*sys.argv[2:])
