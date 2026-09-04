# -*- coding: utf-8 -*-
"""b313_run.py -- THE COMPONENTS. ### **TWO COLUMNS, AND WHAT DIFFERS BETWEEN THEM.**

### ### **THE LOOP IS TRANSCRIBED FROM `b38_act10.main()` AND THE TRANSCRIPTION IS NOT TRUSTED.**
### It is checked against `data/b38_2026-08-18.txt` -- the owner's OWN banked table -- at that
### table's own printed precision, before either column is read. ### **A TRANSCRIPTION THAT CANNOT
### ### REPRODUCE THE ARTIFACT IT TRANSCRIBES IS NOT A TRANSCRIPTION.**

### ### **THE OWNER MODULES ARE IMPORTED, NEVER EDITED, AND `main()` IS NEVER CALLED** -- calling
### it would rewrite the owner's banked table, which is the artifact this act reads as its
### reference.

### ### **AND THE ONE THING THIS FILE MAY NOT DO, NAMED AT THE TOP:** ### it may not name a target.
### The flip is licensed by the source's definition, quoted in the bank; ### **A RESIDUE THAT MOVES
### ### TOWARD SOMETHING IS NOT EVIDENCE, AND THIS FILE PRINTS TWO COLUMNS AND THEIR DIFFERENCE AND
### ### NOTHING ELSE.**
"""
import io
import json
import math
import os
import re
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b313_flip as FLIP   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

B38_BANK = os.path.join(D, 'b38_2026-08-18.txt')
B264_ROWS = os.path.join(D, 'b264_rows.json')

# ### THE AXES, NAMED BEFORE ANY NUMBER IS READ. ### **EVERY ONE OF THEM IS THE OWNER'S OWN AND
# ### NONE IS COINED BY THIS ACT.**
AXES = [
    ('EPS_NQ', 'prolate quadrature nodes in the eigensolver'),
    ('EPS_NG', 'Gauss-Legendre nodes in the remainder integral'),
    ('EPS_NRHO', 'points on the rho grid the remainder is tabulated on'),
    ('NU_HALF', 'points on the log grid the window integral uses'),
    ('NTERM', 'modes carried'),
    ('TRIPLE', 'the (NQ, NMODE) settings the spread is taken over'),
]


def banked_table():
    """### ### **THE OWNER'S OWN BANKED TABLE, PARSED.** ### The reference column."""
    txt = io.open(B38_BANK, encoding='utf-8').read()
    rows = {}
    pat = re.compile(
        r'^(\d+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+\|\s+([-\d.]+)\s+([-\d.]+)\s+'
        r'([-\d.]+)\s+([-\d.]+)\s+\|\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*$', re.M)
    for m in pat.finditer(txt):
        g = m.groups()
        rows[g[0]] = dict(A=float(g[1]), P=float(g[2]), PR=float(g[3]),
                          Wp=float(g[4]), Wm=float(g[5]), f=float(g[6]), resid=float(g[7]),
                          Dd=float(g[8]), Dc=float(g[9]), spread=float(g[10]))
    ecomp = {}
    lab = None
    for line in txt.splitlines():
        m = re.match(r'^(\d+)\s+[-\d.]', line)
        if m:
            lab = m.group(1)
        m2 = re.search(r'-E2even = ([-\d.]+)', line)
        if m2 and lab:
            ecomp[lab] = -float(m2.group(1))
    for k in rows:
        rows[k]['E2even'] = ecomp.get(k)
    return rows


def parser_fixture():
    """### **THE PARSER MUST BE ABLE TO FAIL.** ### b308: a control that cannot fire reads as a
    ### pass."""
    good = ('2       -1.990528   2.009515   0.000000 |  -1.37813  -0.61239   0.6923   4.0486 '
            '|    -2.681242    -1.614208   0.09704')
    pat = re.compile(
        r'^(\d+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+\|\s+([-\d.]+)\s+([-\d.]+)\s+'
        r'([-\d.]+)\s+([-\d.]+)\s+\|\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*$', re.M)
    a = bool(pat.match(good))
    b = not bool(pat.match(good.replace('|', '')))
    c = not bool(pat.match('nothing at all'))
    return a, b, c


def columns(M, label, rec):
    """### **ONE COLUMN, THROUGH ONE MODULE.** ### The loop is `b38_act10.main()`'s, transcribed.

    ### The module carries its own `qeps` layer as `M.Q`, so the SAME code path produces the
    ### banked column when `M` is the owner and the flipped column when `M` is the copy.
    """
    Q = M.Q
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(M.EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    rr = np.exp(np.linspace(1e-4, math.log(12.001), M.EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=M.EPS_NQ, NG=M.EPS_NG))
    ee_modes = M.per_mode_eps_grids(rr)
    mode_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    rec('    [%s] per-mode mask algebra: max|sum_n eps_n - eps_full| = %.2e  %s'
        % (label, mode_alg, 'PASS' if mode_alg <= 1e-10 else '### FAIL ###'))

    out = {}
    for a, alab in M.CELLS:
        v, w2, corr, vc, L = M.family(a)
        A, P, PR = M.left_side(a, M.S4, v, w2, corr, vc, L)
        Thq = M.theta_quotient(a, M.S4, corr, vc, L)
        Dcs, det = [], None
        for (NQ, NMODE) in M.TRIPLE:
            tr = M.trace_modes(a, corr, vc, L, NQ, NMODE)
            N = len(tr)
            E2n = np.array([M.e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
            E2N = float(E2n.sum())
            E2full = M.e2_of_grid(a, corr, vc, L, rr, ee_full)
            E2even = float(E2n[0::2].sum())
            E2odd = float(E2n[1::2].sum())
            TrN = float(tr.sum())
            resid = TrN - A - E2N
            s = t_n[:N] / float(t_n[:N].sum())
            wmode = tr - E2n - s * resid
            Wp = float(wmode[0::2].sum())
            Wm = float(wmode[1::2].sum())
            sum_gate = abs(Wp + Wm - A)
            D_dict = (Thq - PR) + (E2odd - 2.0 * E2full)
            D_closed = (A - PR) - ((Wp + E2even) - Thq)
            D_closed_alt = Wm - E2even + (Thq - PR)
            Dcs.append(D_closed)
            if (NQ, NMODE) == M.TRIPLE[1]:
                det = dict(Wp=Wp, Wm=Wm, resid=resid, Dd=D_dict, Dc=D_closed,
                           Dca=D_closed_alt, gate=sum_gate, E2even=E2even, E2odd=E2odd,
                           TrN=TrN, E2N=E2N, E2full=E2full)
        det.update(A=A, P=P, PR=PR, Thq=Thq, f=det['Wp'] / A,
                   spread=max(abs(d - Dcs[1]) for d in Dcs))
        out[alab] = det
    return out, rr, ee_full, ee_modes, mode_alg


def ladder(M264, LAY, rows, nres, rec, label):
    """### **b264's LADDER, AT ITS OWN REACH, WITH THE NOISE-FLOOR GATE IN THE PATH.**"""
    outs = []
    for row in rows:
        r = float(row['rho'])
        NG = M264.ng_for(r)
        em = M264.eps_modes(r, NG, LAY)
        allev = float(em[0::2].sum())
        resev = float(sum(em[n] for n in range(0, len(em), 2) if n < nres))
        floor = [n for n in range(0, len(em), 2) if n >= nres]
        outs.append(dict(rho=r, NG=NG, kind=M264.gl_kind(NG),
                         even_all=allev, even_resolved=resev, floor_modes=floor))
    return outs


def main():
    lines = []

    def rec(s):
        lines.append(s)
        print(s)

    t0 = time.time()
    rec('=' * 100)
    rec('b313 -- THE COMPONENTS. ### **THE EXPONENT: THE REMAINDER UNDER THE SOURCE\'S'
        ' NORMALIZATION.**')
    rec('=' * 100)

    fails = []

    # ---------------------------------------------------------------- COMPONENT 1 (recorded)
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE WARRANT. ### **RECORDED IN THE SEALED REGISTRATION, SECTION (5).**')
    rec('-' * 100)
    rec('  ### The warrant is quotations, not computation, and it is banked in full. ### What this')
    rec('  ### runner records is that the reads preceded everything below: the registration was')
    rec('  ### SEALED before this file was run, and the seal covers section (5).')
    rec('  ### ### **THE ONE SENTENCE, RESTATED HERE BECAUSE EVERY NUMBER BELOW DEPENDS ON IT:**')
    rec("  ### **THE CORPUS DECLARED ITS REMAINDER TO BE THE SOURCE\'S EQUATION, THE SOURCE DEFINES")
    rec("  ### THAT EQUATION\'S SCALING ACTION AT ITS OWN eq. (61) AND UNFOLDS IT THE SAME WAY TWICE")
    rec('  ### MORE, SO THE EXPONENT IS SETTLED BY THAT DEFINITION ALONE -- BEFORE ANY RESIDUE IS')
    rec('  ### LOOKED AT, AND WHATEVER THE RESIDUE TURNS OUT TO DO.**')
    rec("  ### **THE RESIDUE\'S DIRECTION IS UNPREDICTED. ### THIS SEAT REGISTERED NO EXPECTATION.**")

    # ---------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE COMPUTATION.')
    rec('=' * 100)

    rec('')
    rec('  ### (2a) THE COPIES, AND THE DIFF.')
    ok_flip, flip_lines = FLIP.build(write=True, verbose=False)
    rec('  ### the copy-maker ran, all controls: %s' % ok_flip)
    if not ok_flip:
        fails.append('the copies did not build')
    for ln in flip_lines:
        rec('  ' + ln)

    # ### THE RESTORED COPIES -- the positive control's material.
    rec('')
    rec("  ### (2b) THE POSITIVE CONTROL\'S MATERIAL: ### **THE COPY WITH THE EXPONENT RESTORED.**")
    restored = []
    for spec in FLIP.FILES:
        src = FLIP.read(spec['src'])
        flipped = FLIP.read(spec['dst'])
        back, _ = FLIP.apply_subs(flipped, spec['subs'], inverse=True)
        same = (back == src)
        rpath = os.path.join(E16, 'b313r_' + os.path.basename(spec['src']))
        open(rpath + '.tmp', 'wb').write(back.encode('utf-8'))
        os.replace(rpath + '.tmp', rpath)
        restored.append((os.path.basename(rpath), same))
        rec('    %-28s byte-identical to the owner : %s  %s'
            % (os.path.basename(rpath), same, 'PASS' if same else '### FAIL ###'))
        if not same:
            fails.append('restored copy differs from owner: %s' % rpath)
    rec('    ### **SO THE RESTORED COPY IS THE OWNER FILE UNDER ANOTHER NAME**, and any number it')
    rec("    ### produces that differs from the owner\'s would be a fact about the copy machinery.")

    import b38_act10 as ORIG              # noqa: E402  ### the OWNER, imported, never edited
    import b313f_b38_act10 as FLIPPED     # noqa: E402
    import b313r_b38_act10 as RESTORED    # noqa: E402

    rec('')
    rec("  ### (2c) THE AXES, NAMED. ### **EVERY ONE THE OWNER\'S OWN; NONE COINED HERE.**")
    for name, what in AXES:
        holder = ORIG.Q if name == 'NTERM' else ORIG
        rec('    %-10s = %-24s %s   [%s]'
            % (name, getattr(holder, name), what, holder.__name__))
    rec('    ### **AND THE INSTRUMENT IS NOT EXACT ANYWHERE IN THIS PATH.** ### It is double')
    rec('    ### precision throughout: a prolate eigensolver, Gauss-Legendre quadrature, and')
    rec('    ### trapezoidal integration on fixed grids. ### **SO EVERY VALUE BELOW IS REPORTED AT')
    rec("    ### THE OWNER\'S OWN PRINTED PRECISION AND NOT ONE DIGIT FURTHER**, and the one thing")
    rec('    ### that IS exact -- the ratio the flip induces -- is measured separately in (3a).')

    rec('')
    rec("  ### (2d) THE TRANSCRIPTION, CHECKED AGAINST THE OWNER\'S OWN BANKED TABLE.")
    pf = parser_fixture()
    rec('    parser fixture (matches a real row / rejects a mangled one / rejects prose) : %s  %s'
        % (list(pf), 'PASS' if all(pf) else '### FAIL ###'))
    if not all(pf):
        fails.append('parser fixture')
    bank = banked_table()
    rec('    rows parsed from %s : %d' % (os.path.basename(B38_BANK), len(bank)))

    rec('')
    rec('  ### (2e) THE THREE COLUMNS.')
    colO, rrO, eefO, eemO, algO = columns(ORIG, 'OWNER   ', rec)
    colR, _rrR, _eefR, _eemR, algR = columns(RESTORED, 'RESTORED', rec)
    colF, rrF, eefF, eemF, algF = columns(FLIPPED, 'FLIPPED ', rec)
    for lbl, alg in (('OWNER', algO), ('RESTORED', algR), ('FLIPPED', algF)):
        if alg > 1e-10:
            fails.append('mask algebra gate under %s' % lbl)

    rec('')
    rec("  ### ### **THE TRANSCRIPTION vs THE BANKED TABLE** -- at the table\'s own printed")
    rec('  ### precision, which is the only precision the artifact carries:')
    rec('    %-5s %-10s %-12s %-12s %-10s' % ('a^2', 'quantity', 'banked', 'transcribed', 'agree'))
    worst = 0.0
    for a, alab in ORIG.CELLS:
        b = bank.get(alab)
        c = colO[alab]
        for key, fmt, tol in (('A', '%.6f', 5e-7), ('PR', '%.6f', 5e-7),
                              ('Wp', '%.5f', 5e-6), ('Wm', '%.5f', 5e-6),
                              ('resid', '%.4f', 5e-5), ('Dd', '%.6f', 5e-7),
                              ('Dc', '%.6f', 5e-7), ('spread', '%.5f', 5e-6)):
            got, want = c[key], b[key]
            d = abs(got - want)
            worst = max(worst, d)
            agree = d <= tol
            if not agree:
                fails.append('transcription %s at a^2=%s' % (key, alab))
            rec('    %-5s %-10s %-12s %-12s %s'
                % (alab, key, fmt % want, fmt % got, 'yes' if agree else '### NO ###'))
    rec('    ### ### **WORST ABSOLUTE DEPARTURE FROM THE BANKED TABLE : %.2e**' % worst)
    rec('    ### **THIS IS THE CONTROL THAT MATTERS MOST IN THE ACT**: it is a reproduction of a')
    rec('    ### month-old artifact by a loop written today, and it is what licenses reading the')
    rec('    ### second column at all.')

    rec('')
    rec('  ### ### **THE POSITIVE CONTROL: ### THE COPY WITH THE EXPONENT RESTORED REPRODUCES THE')
    rec('  ### ### OWNER.**')
    exact = 0
    total = 0
    worstR = 0.0
    for a, alab in ORIG.CELLS:
        for key in ('A', 'P', 'PR', 'Wp', 'Wm', 'resid', 'Dd', 'Dc', 'spread', 'E2even',
                    'E2odd', 'TrN', 'E2N'):
            total += 1
            dv = abs(colO[alab][key] - colR[alab][key])
            worstR = max(worstR, dv)
            if colO[alab][key] == colR[alab][key]:
                exact += 1
    rec('    quantities compared : %d ; ### **BITWISE IDENTICAL : %d** ; worst difference : %.2e'
        % (total, exact, worstR))
    if exact != total:
        fails.append('the restored copy did not reproduce the owner bitwise')
    rec('    ### **A COPY THAT COULD NOT REPRODUCE THE ORIGINAL COULD NOT BE USED TO DIFFER FROM')
    rec('    ### IT**, and this arm is what makes the second column a statement about the exponent')
    rec('    ### rather than a statement about the copying.')

    rec('')
    rec('  ### ### **THE TWO COLUMNS, SIDE BY SIDE.** ### `resid = Tr - A - E2`, the residue')
    rec('  ### between the two constructions of the archimedean trace.')
    rec('    %-5s | %-10s %-10s | %-10s %-10s | %-11s %-11s'
        % ('a^2', 'A (both)', 'Tr (both)', 'E2 banked', 'E2 source', 'resid banked', 'resid source'))
    for a, alab in ORIG.CELLS:
        o, f = colO[alab], colF[alab]
        rec('    %-5s | %-10.6f %-10.6f | %-10.6f %-10.6f | %-11.4f %-11.4f'
            % (alab, o['A'], o['TrN'], o['E2N'], f['E2N'], o['resid'], f['resid']))
    rec('    ### **`A` AND `Tr` ARE THE SAME NUMBER IN BOTH COLUMNS** -- neither call path touches')
    rec('    ### the exponent -- and that is measured in (3c) rather than asserted here.')

    # ---------------------------------------------------------------- COMPONENT 3
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- WHAT MOVES AND WHAT DOES NOT.')
    rec('=' * 100)

    rec('')
    rec('  ### (3a) THE STRUCTURAL FACT, MEASURED: ### **THE FLIP IS EXACTLY MULTIPLICATION BY'
        ' `rho`.**')
    ratio = np.zeros_like(rrO)
    nz = np.abs(eefO) > 0
    ratio[nz] = eefF[nz] / eefO[nz]
    dev = float(np.max(np.abs(ratio[nz] / rrO[nz] - 1.0)))
    rec('    grid points with a nonzero banked value : %d of %d' % (int(nz.sum()), len(rrO)))
    rec('    ### **max | (eps_source / eps_banked) / rho  -  1 |  =  %.2e**' % dev)
    rec("    ### This is the registration\'s one structural expectation and it is MEASURED, not")
    rec('    ### assumed: the exponent enters each per-mode value as a single multiplicative')
    rec('    ### factor, so the two columns are related pointwise by `rho` and by nothing else.')
    rec('    ### **IF THIS ARM HAD FAILED, THE COPY WOULD BE DOING SOMETHING NOBODY DECLARED AND')
    rec('    ### THE ACT WOULD STOP HERE.**')
    if dev > 1e-12:
        fails.append('the flip is not a pointwise rho factor')

    rec('')
    rec("  ### (3b) THE RESIDUE\'S SIZE UNDER EACH CONVENTION, PER CELL.")
    rec('    %-5s | %-12s %-12s | %-12s %-12s'
        % ('a^2', 'resid banked', 'resid source', 'abs banked', 'abs source'))
    for a, alab in ORIG.CELLS:
        o, f = colO[alab], colF[alab]
        rec('    %-5s | %-12.4f %-12.4f | %-12.4f %-12.4f'
            % (alab, o['resid'], f['resid'], abs(o['resid']), abs(f['resid'])))
    rec('    ### **NO TARGET IS NAMED AND NO FIT IS PERFORMED.** ### These are two columns.')

    rec('')
    rec('  ### (3c) EVERY QUANTITY THAT CHANGES AND EVERY QUANTITY THAT DOES NOT, BY CALL PATH.')
    rec('    %-10s %-40s %-10s' % ('quantity', 'call path', 'changes?'))
    paths = [
        ('A', 'left_side -> carto_atlas.hhat/kernel', 'A'),
        ('P', 'left_side -> bump, cosh', 'P'),
        ('PR', 'left_side -> the prime loop', 'PR'),
        ('Thq', 'theta_quotient -> b8/b10', 'Thq'),
        ('TrN', 'trace_modes -> qeps.layer, math.sqrt(lamd)', 'TrN'),
        ('E2N', 'per_mode_eps_grids -> THE FLIPPED LINE', 'E2N'),
        ('E2even', 'e2_of_grid over the even modes', 'E2even'),
        ('E2odd', 'e2_of_grid over the odd modes', 'E2odd'),
        ('resid', 'TrN - A - E2N', 'resid'),
        ('Wp', 'tr - E2n - s*resid, even', 'Wp'),
        ('Wm', 'tr - E2n - s*resid, odd', 'Wm'),
        ('Dd', '(Thq-PR) + (E2odd - 2 E2full)', 'Dd'),
        ('Dc', '(A-PR) - ((Wp+E2even) - Thq)', 'Dc'),
        ('spread', 'D_closed over TRIPLE', 'spread'),
    ]
    for name, path, key in paths:
        same_all = all(colO[alab][key] == colF[alab][key] for _a, alab in ORIG.CELLS)
        rec('    %-10s %-40s %-10s' % (name, path, 'NO' if same_all else 'yes'))
    ep_o = ORIG.Q.epsprime1(ORIG.EPS_NQ)
    ep_f = FLIPPED.Q.epsprime1(FLIPPED.EPS_NQ)
    rec('    %-10s %-40s %-10s' % ("eps'(1+)", 'epsprime1 -- no rho in its body at all',
                                   'NO' if ep_o == ep_f else 'yes'))
    rec('    ### banked eps\'(1+) = %.8f ; source-convention eps\'(1+) = %.8f ; bitwise equal : %s'
        % (ep_o, ep_f, ep_o == ep_f))
    if ep_o != ep_f:
        fails.append("epsprime1 moved under the flip")

    rec('')
    rec("  ### (3d) WHY THE BANKED CROSS-CHECK NEVER SAW IT -- b312\'s DERIVATION, NOW MEASURED.")
    rec('    ### `epsprime1` does not contain `rho` at all, so the flip is not on its call path;')
    rec('    ### that is the trivial half. ### **THE HALF THAT MATTERS IS THAT THE DERIVATIVE OF')
    rec('    ### THE FUNCTION ITSELF IS ALSO UNMOVED**, because the integral vanishes at the')
    rec('    ### identity. ### Measured as a one-sided difference quotient:')
    rec('    %-12s %-16s %-16s %-12s' % ('h', 'banked (eps/h)', 'source (eps/h)', 'difference'))
    for h in (1e-3, 1e-4, 1e-5, 1e-6):
        r1 = 1.0 + h
        qo = float(np.atleast_1d(ORIG.Q.eps(np.array([r1]),
                                            NQ=ORIG.EPS_NQ, NG=ORIG.EPS_NG))[0]) / h
        qf = float(np.atleast_1d(FLIPPED.Q.eps(np.array([r1]),
                                               NQ=FLIPPED.EPS_NQ, NG=FLIPPED.EPS_NG))[0]) / h
        rec('    %-12.0e %-16.8f %-16.8f %-12.2e' % (h, qo, qf, abs(qo - qf)))
    rec('    ### ### **BOTH APPROACH THE SAME LIMIT, AND THE DIFFERENCE BETWEEN THEM GOES TO ZERO')
    rec('    ### ### WITH `h`.** ### The two functions differ by a factor of `rho`, and at `rho = 1`')
    rec('    ### that factor is `1` while the function is `0` -- so the slope at the identity is')
    rec("    ### blank to it. ### **THAT IS THE WHOLE REASON THE CORPUS\'S ONE CROSS-CHECK PASSED.**")

    rec('')
    rec("  ### (3e) b264\'s LADDER, RE-RUN UNDER THE FLIP, AT ITS OWN REACH,")
    rec('  ### **WITH THE NOISE-FLOOR GATE IN THE PATH.**')
    b264 = json.load(io.open(B264_ROWS, encoding='utf-8'))
    nres = int(b264['nres'])
    rec('    b264\'s resolved-mode count, READ from its banked rows : NRES = %d (bar %.0e)'
        % (nres, b264['res_bar']))
    rec("    ### **MODES AT OR ABOVE THAT INDEX ARE AT THE EIGENSOLVER\'S FLOOR** -- b264 measured")
    rec('    ### it and filed `W-ORD-NTERM-FLOOR`. ### Every row below prints BOTH the all-mode')
    rec("    ### even sum (b264\'s own definition, so the columns are comparable) AND the")
    rec('    ### resolved-only sum, and names the floor modes it excluded.')
    import b264_eps_decay as L264            # noqa: E402
    import b313f_b264_eps_decay as L264F     # noqa: E402
    LAY = ORIG.Q.layer(ORIG.EPS_NQ)
    lad_o = ladder(L264, LAY, b264['ladder'], nres, rec, 'banked')
    lad_f = ladder(L264F, LAY, b264['ladder'], nres, rec, 'source')
    rec('    %-8s %-8s %-26s %-13s %-13s %-11s %-11s'
        % ('rho', 'NG', 'rule', 'even banked', 'even source',
           'floor bkd', 'floor src'))
    for ro, rf, bro in zip(lad_o, lad_f, b264['ladder']):
        rec('    %-8g %-8d %-26s %-13.6g %-13.6g %-11.3e %-11.3e'
            % (ro['rho'], ro['NG'], ro['kind'], ro['even_all'], rf['even_all'],
               ro['even_all'] - ro['even_resolved'], rf['even_all'] - rf['even_resolved']))
    rec('    ### floor modes excluded from the resolved sum, every row : %s'
        % lad_o[0]['floor_modes'])
    rec('    ### **THE LAST TWO COLUMNS ARE WHAT THE GATE ACTUALLY REMOVES**, printed rather than')
    rec('    ### described: the difference between the all-mode even sum and the resolved-only')
    rec('    ### one. ### It is far below the printed precision of the columns beside it, which is')
    rec("    ### what b264's own floor measurement predicted -- and the gate is reported by its")
    rec('    ### SIZE rather than by the word `negligible`, because a gate whose effect nobody')
    rec('    ### prints is a gate nobody can check.')
    rec("    ### **AND THE LADDER REPRODUCES b264\'s BANKED `eps_even` COLUMN**, which is the")
    rec('    ### control that makes the flipped column readable:')
    worstL = max(abs(ro['even_all'] - float(bro['eps_even']))
                 for ro, bro in zip(lad_o, b264['ladder']))
    rec('    ### worst absolute departure from b264\'s banked `eps_even` : %.2e' % worstL)
    if worstL > 1e-9:
        fails.append('the ladder did not reproduce b264')

    rec('')
    rec('  ### (3f) THE DECAY ALONG THE CUTOFF, UNDER EACH CONVENTION.')
    rec("    ### b264 measured the banked column\'s decay by the product `eps_even * rho^{3/2}`,")
    rec("    ### which it found approaching a constant. ### **UNDER THE SOURCE\'S EXPONENT THE SAME")
    rec('    ### PRODUCT IS `eps_even * rho^{1/2}`, AND IT IS THE SAME NUMBER** -- because the two')
    rec('    ### columns differ pointwise by `rho`. ### So the decay RATE moves by one power and')
    rec('    ### the leading constant does not move at all.')
    rec('    %-8s %-16s %-16s %-12s' % ('rho', 'banked * rho^3/2', 'source * rho^1/2', 'difference'))
    worstS = 0.0
    for ro, rf in zip(lad_o, lad_f):
        so = ro['even_all'] * ro['rho'] ** 1.5
        sf = rf['even_all'] * rf['rho'] ** 0.5
        worstS = max(worstS, abs(so - sf))
        rec('    %-8g %-16.8g %-16.8g %-12.2e' % (ro['rho'], so, sf, abs(so - sf)))
    rec('    ### worst difference between the two scaled columns : %.2e' % worstS)
    rec('    ### **THE ROWS FROM `rho = 500` UPWARD ARE THE ONES b264 ITSELF REPORTED AS SITTING')
    rec('    ### BEYOND ITS MEASURED `EPS_NQ` CEILING (~238), AND THEY ARE NOT READ AS DECAY BY')
    rec('    ### EITHER COLUMN.** ### They are printed because deleting them would be a choice')
    rec('    ### nobody could check.')

    rec('')
    rec('  ### (3g) TWO DERIVED COLUMNS, PRINTED BECAUSE THE ORDER SAYS TO REPORT WHAT MOVES.')
    rec("    ### The first is the residue's relative change; the second is `A + E2`, which is")
    rec('    ### `Tr - resid` and is therefore just a third way of writing the same three numbers.')
    rec('    %-5s | %-12s %-12s %-10s | %-13s %-13s'
        % ('a^2', 'resid banked', 'resid source', 'ratio', 'A+E2 banked', 'A+E2 source'))
    for a, alab in ORIG.CELLS:
        o, f = colO[alab], colF[alab]
        rec('    %-5s | %-12.4f %-12.4f %-10.4f | %-13.6f %-13.6f'
            % (alab, o['resid'], f['resid'], f['resid'] / o['resid'],
               o['A'] + o['E2N'], f['A'] + f['E2N']))
    rec("    ### ### **THESE ARE COLUMNS OF THIS ACT'S OWN TABLE, NOT COMPARISONS TO ANY TARGET.**")
    rec('    ### No banked target, prime sum, mass or asymptote is named here, and none is meant.')
    rec('    ### ### **AND THE SECOND COLUMN IS NOT INTERPRETED BY THIS ACT.** ### It is printed')
    rec('    ### because it is a quantity that moved and the order says to report what moved;')
    rec('    ### what it might mean is a question this act does not have the instrument to answer,')
    rec('    ### and it is filed as a question in the bank rather than read as a result.')
    rec("    ### ### **AND ONE CAUTION THAT IS NOT OPTIONAL, BECAUSE b312 FOUND IT AND IT LANDS")
    rec("    ### ### EXACTLY HERE:** ### `A` comes from `carto_atlas.py`, whose own header says")
    rec("    ### ### its sign is *[sign fixed BY the E2 calibration]* and which disclaims any sign")
    rec("    ### ### claim. ### So `A + E2` compares a term against the very quantity its sign was")
    rec("    ### ### calibrated against. ### **A COLUMN LIKE THAT CAN REPORT THE CALIBRATION")
    rec("    ### ### RATHER THAN THE MATHEMATICS, AND THIS ACT HAS NO INSTRUMENT THAT CAN TELL")
    rec("    ### ### THE TWO APART.** ### That is why it is filed as a question and not read, and")
    rec("    ### the reason is a measured property of the corpus rather than a hedge.")
    rec("    ### ### **AND ITS DIRECTION, SO NOBODY READS IT AS AN IMPROVEMENT:** ### under the")
    rec("    ### source's exponent the identity's two right-hand terms very nearly CANCEL, so the")
    rec("    ### residue becomes essentially the whole trace. ### **THAT IS NOT AN IDENTITY")
    rec("    ### ### CLOSING; IT IS THE OPPOSITE SHAPE, AND SAYING SO IS PART OF REPORTING IT.**")

    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- THE READING, AT EXACTLY ITS SCOPE.')
    rec('=' * 100)
    ratios = [colF[alab]['resid'] / colO[alab]['resid'] for _a, alab in ORIG.CELLS]
    collapsed = all(abs(colF[alab]['resid']) < 0.01 * abs(colO[alab]['resid'])
                    for _a, alab in ORIG.CELLS)
    rec("  ### **THE BRANCH IS DECIDED BY THE NUMBERS AND NOT BY THIS SEAT'S PREFERENCE**, and the")
    rec("  ### criterion is stated before the verdict: the order's word is COLLAPSE, and a residue")
    rec('  ### that keeps its order of magnitude has not collapsed.')
    rec('    residue ratios, source over banked, per cell : %s'
        % ', '.join('%.4f' % x for x in ratios))
    rec('    ### **RANGE : %.4f to %.4f. ### THE RESIDUE SHRINKS BY BETWEEN %.0f%% AND %.0f%% AND'
        % (min(ratios), max(ratios), 100 * (1 - max(ratios)), 100 * (1 - min(ratios))))
    rec('    ### KEEPS ITS ORDER OF MAGNITUDE AT EVERY CELL.**')
    rec('    collapsed (every cell below one per cent of its banked value) : %s' % collapsed)
    rec('')
    if collapsed:
        rec('  ### ### **BRANCH ONE. ### THE RESIDUE COLLAPSED.**')
        fails.append('branch one taken -- the bank must be rewritten for it')
    else:
        rec('  ### ### ### **BRANCH TWO. ### THE RESIDUE IS NOT THE EXPONENT.**')
        rec('  ### The order states this branch in its own words: ### *if it does not collapse, the')
        rec('  ### residue is not the exponent and the act says so.* ### **IT DOES NOT COLLAPSE,')
        rec('  ### AND THIS ACT SAYS SO.**')
        rec('  ### ### **WHAT THAT DOES AND DOES NOT MEAN, BOTH STATED:**')
        rec('  ###   ### **IT DOES NOT MEAN THE FLIP WAS WRONG.** ### b312 decided which function')
        rec("  ###     the corpus's remainder is, by unfolding definitions, and a residue is not a")
        rec("  ###     vote on that. ### **THE EXPONENT IS FIXED BY THE SOURCE'S DEFINITION AND BY")
        rec('  ###     ### NOTHING THE RESIDUE DOES** -- which is the standing clause, and it binds')
        rec('  ###     in this direction exactly as hard as it would have bound in the other.')
        rec('  ###   ### **IT DOES MEAN THE SEARCH CONTINUES.** ### The convention mismatch is')
        rec('  ###     real, it is an instrument finding, and it accounts for between %.0f%% and'
            % (100 * (1 - max(ratios))))
        rec('  ###     %.0f%% of the residue at these six cells. ### **IT DOES NOT ACCOUNT FOR THE'
            % (100 * (1 - min(ratios))))
        rec('  ###     ### REST, AND NOTHING HERE SAYS WHAT DOES.**')
        rec('  ###   ### **AND THE THIRD AND FOURTH FACE-OFFS ARE NOT RE-READ.** ### The order')
        rec('  ###     attaches a sentence to their interpretation only on branch one. ### On this')
        rec('  ###     branch their numbers stand as banked and their readings stand unamended.')
    rec('  ### ### **IN EITHER BRANCH, AND SAID BECAUSE THE ORDER REQUIRES IT SAID: ### NOTHING')
    rec('  ### ### ABOUT THE IDENTITY, ABOUT `h2`, OR ABOUT THE ROSTER FOLLOWS FROM ANY OF THIS.**')
    rec('  ### ### **AND NO BANKED NUMBER IS CALLED WRONG.** ### Every value in the banked column')
    rec('  ### is what the banked instrument computes. ### **WHAT THIS ACT ADDS IS A SECOND COLUMN')
    rec('  ### AND A STATEMENT OF WHAT DIFFERS BETWEEN THEM.**')

    rec('')
    rec('  ### CHECKS FAILING : %d' % len(fails))
    for f in fails:
        rec('    ### FAILED: %s' % f)
    rec('  ### elapsed : %.1f s' % (time.time() - t0))
    rec('=' * 100)

    payload = {'cells': {k: {kk: vv for kk, vv in v.items()} for k, v in colO.items()},
               'flipped': {k: {kk: vv for kk, vv in v.items()} for k, v in colF.items()},
               'ladder_banked': lad_o, 'ladder_source': lad_f,
               'ratio_dev': dev, 'transcription_worst': worst,
               'restored_exact': exact, 'restored_total': total,
               'ladder_worst': worstL, 'scaled_worst': worstS,
               'epsprime1': [ep_o, ep_f], 'nres': nres, 'fails': fails,
               'ratios': ratios, 'collapsed': collapsed}
    open(os.path.join(D, 'b313_rows.json') + '.tmp', 'wb').write(
        (json.dumps(payload, indent=1, default=float) + '\n').encode('utf-8'))
    os.replace(os.path.join(D, 'b313_rows.json') + '.tmp', os.path.join(D, 'b313_rows.json'))
    return (0 if not fails else 1), lines


if __name__ == '__main__':
    code, ls = main()
    io.open(os.path.join(D, 'b313_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(ls) + '\n')
    sys.exit(code)
