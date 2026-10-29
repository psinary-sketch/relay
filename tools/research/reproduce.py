# -*- coding: utf-8 -*-
"""tools/research/reproduce.py -- THE RESEARCH INSTRUMENTS REPRODUCED, ONE ROW PER INSTRUMENT ((R332)(7)). Written whole at b722 by the
Write tool; sealed with b722's tools.

  run [--bank data/<name>] [--only I-nn,...]
        for each row: the instrument's tool imported unedited in a fresh process (python -X utf8, cwd a scratch directory, 60 s at most),
        the call printed and run, one banked figure read from its bank and line, and the row graded REPRODUCES or DIFFERS; beside it the
        planted control -- the same comparison against a wrong figure (the banked figure's leading digit moved by one, or a word appended)
        -- which must DIFFER. A row needing a dispatch or a network read, or more than 60 s, prints NOT RUN with its reason and price. The
        host's free memory is read before each row against the 2,560 MB hold; the relay's tools/ and data/ are listed before and after
        each row, and a row whose call writes there is graded DIFFERS, its writes the reason (nothing else may write there while it
        runs: the listing cannot tell a call's write from another process's). --bank writes <name>.txt and <name>.json; without it nothing is written.
  rows  prints the rows (id, tool, bank, line, the figure's substrings, the call) and runs nothing.

THE COMPARISON, printed before any row: the numbers of the banked figure (the row's substrings of the bank line, in order) against the
leading numbers of the call's output (its last line, or the part a row's output pattern picks); an integer equal exactly; a decimal equal
at the lesser of the two printed significant-digit counts, both rounded half-even in decimal (the banked figure is a printed rounding of
its generator; the generator is compared, never a float derived from it). A row graded by words compares the text exactly. Digits inside
an identifier (n0, mid929_937, T0) are not numbers.
"""
import ctypes
import decimal
import json
import os
import re
import subprocess
import sys
import tempfile
import time

TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(TOOLS)
NL = chr(10)
HOLD_MB = 2560
TIMEOUT = 60
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRE = 'import sys; sys.path.insert(0, %r); sys.path.insert(0, %r)' % (TOOLS, os.path.join(TOOLS, 'e16')) + NL
NUM = re.compile(r'(?<![A-Za-z_\d.])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')
RULE = ('THE COMPARISON: the banked figure`s numbers against the leading numbers of the call`s output; an integer exactly; a decimal at '
        'the lesser of the two printed significant-digit counts, rounded half-even in decimal; a row graded by words, the text exactly. '
        'THE PLANTED CONTROL: the banked figure`s leading digit moved by one (a word row: " (planted)" appended), compared the same way; '
        'it must DIFFER. NOT RUN: a row needing a dispatch or a network read, or more than 60 s, with its reason and price.')

C, U, B = 'COMPUTED', 'READ FROM UNITS', 'READ FROM BANKS'
# ### ROWS: (id, tool, bank, line, [substrings of the bank line carrying the figure], call, mode, output pattern, kind, NOT RUN reason)
ROWS = [
    ('I-41', 'b302_kernel', 'data/b302_kernel_run.txt', 37, ['11, 11 zero-axiom, 0'],
     "import b302_kernel as M\nraw=open(M.PROFILE,'rb').read()\nsel=b''.join(l+b'\\n' for l in raw.split(b'\\n') if b\"'B302.\" in l)\nprint(M.count_prints(sel))",
     'num', None, C, None),
    ('I-42', 'b303_family', 'data/b303_family_run.txt', 27, ['fires 64'], "import b303_family as M\nprint(len(M.nullspace(M.rows_member(3,2,0,0),81)))",
     'num', None, C, None),
    ('I-43', 'b304_smearing', 'data/b304_smearing_run.txt', 68, ['= -3'],
     "import b304_smearing as M\nF=M.FAM\nP,rk=M.projector(F.nullspace(F.rows_member(2,2,0,0),16),16)\nprint(M.trace_scaled(P,5,16))", 'num', None, C, None),
    ('I-44', 'b308_local_field', 'data/b308_instrument_run.txt', 56, ['M = 16   cell mass 1/4'],
     "import b308_local_field as M\nfr=M.Frame(2,2,2)\nprint(fr.M, fr.cell_mass())", 'num', None, C, None),
    ('I-45', 'b309_scaling_trace', 'data/b309_components_run.txt', 158, ['B         0                0'],
     "import b309_scaling_trace as M\nprint(M.trace_route_a(2,2,-1)[0], M.trace_route_b(2,2,-1))", 'num', None, C, None),
    ('I-46', 'b316_instrument', 'data/b316_components_run.txt', 156, ['0.9455'],
     "import numpy as np, b316_instrument as M\nfr=M.Frame(1024,16.0,256); sub=fr.subspace(); u=M.sonin_unit(fr)\n"
     "print(float(np.linalg.norm(fr.outside(sub,u))/max(np.linalg.norm(u[sub['hi']]),1e-300)))", 'num', None, C, None),
    ('I-47', 'b317_smear', 'data/b317_components_run.txt', 140, ['-0.0417829'],
     "import b316_instrument as INS, b317_smear as M\nfr=INS.Frame(4096,32.0,512); sub=fr.subspace()\nprint(M.compressed_trace(fr,sub,M.corpus_bump(1.5))[0])",
     'num', None, C, None),
    ('I-48', 'b318_square', 'data/b318_components_run.txt', 138, ['3.781374629'],
     "import b316_instrument as INS, b317_smear as SM, b318_square as M\nfr=INS.Frame(4096,32.0,512); sub=fr.subspace()\n"
     "print(M.square_trace(fr,sub,SM.mean_zero_variant(1.5)))", 'num', None, C, None),
    ('I-49', 'b319_stable', 'data/b319_components_run.txt', 62, ['80        69'],
     "import b316_instrument as INS, b319_stable as M\nst,gr=M.both_subspaces(INS.Frame(4096,32.0,512))\nprint(gr['rank'], st['rank'])", 'num', None, C, None),
    ('I-50', 'b320_corroborate', 'data/b320_corroboration.txt', 5, ['2.466025237'],
     "import b317_smear as SM, b318_square as SQ, b320_corroborate as M\nprint(M.digamma_side(SQ.autocorrelation(SM.mean_zero_variant(SM.FIXTURE_A))))",
     'num', None, C, None),
    ('I-51', 'b320_weil', 'data/b320_components_run.txt', 15, ['2.466039906'],
     "import b317_smear as SM, b318_square as SQ, b320_weil as M\nprint(M.weil(SQ.autocorrelation(SM.mean_zero_variant(SM.FIXTURE_A)))[0])",
     'num', None, C, None),
    ('I-52', 'b321_window', 'data/b321_components_run.txt', 51, ['-0.158889558       -0.158889572'],
     "import b317_smear as SM, b318_square as SQ, b321_window as M\nf=SQ.autocorrelation(SM.mean_zero_variant(1.3))\n"
     "print(M.remainder_integral(f), M.remainder_integral(f, route='cheb'))", 'num', None, C, None),
    ('I-53', 'b322_ladder', 'data/b322_components_run.txt', 42, ['20       0.797250168'],
     "import b322_ladder as M\nr=M.frame_row(1024,8.0,512)\nprint(r['rank'], r['stable'])", 'num', None, C, None),
    ('I-54', 'b325_epstein', 'data/b325_run.txt', 111, ['0.006348865       2.249539781'],
     "import b317_smear as SM, b318_square as SQ, b325_epstein as M\nf=SQ.autocorrelation(SM.mean_zero_variant(3.0))\nc=M.channels_q(f.v,f.w)\n"
     "print(c['finite'], c['arch'])", 'num', None, C, None),
    ('I-55', 'b326_closure', 'data/b326_closure_run.txt', 9, ['zeta 0.315809856997'],
     "import numpy as np, carto_atlas as AT, b326_windows as BW, b326_closure as M\nf=BW.cell_function(3.0)\n"
     "print(2.0*float(np.sum(M.hhat_exact(f.v,f.w,np.asarray(AT.GAM,dtype=float)))))", 'num', None, C, None),
    ('I-56', 'b326_windows', 'data/b326_windows_run.txt', 37, ['-0.251245834   -0.000389214'],
     "import b326_windows as M\nlz=M.von_mangoldt_sieve(1026); lq=M.lambda_q_sieve(1026)\nc=M.channels(M.cell_function(32.0),lz,lq,refine=1)\n"
     "print(c['arch_z'], c['places_z'])", 'num', None, C,
     'MORE THAN 60 s: two 41,600 x 16,385 transforms and about 125,000 digamma calls at a = 32; priced at 60-120 s on this host '
     '(the drafter`s estimate, unmeasured)'),
    ('I-57', 'b326_zeros', 'data/b326_zeros_run.txt', 77, ['route A [0.9532604747946607, 16.290215720390393]'],
     "import b326_zeros as M\nM.bind(119,240)\nr=M.task_offline(((0.94,1.08),(16.0,16.5)))\nprint(r[2]['rho_a'])", 'num', None, C,
     'MORE THAN 60 s: two secant root-finds at 119 digits with 240 incomplete-gamma terms; measured past the 60 s cap at b722 '
     '(scratch run, killed at 60.0 s); priced at 60-120 s'),
    ('I-58', 'b327_bridge', 'data/b327_bridge_run.txt', 40, [': 1.33e-251'],
     "import b327_bridge as M, mpmath as mp\nns,_,_ = M.load_bench_definitions()\neta = ns['taylor_coeffs'](ns['f_A'], mp.mpf(M.RADII[0]), M.M_QUAD, 30)\n"
     "lam = ns['lambdas'](eta, 30)\nprint(mp.nstr(abs(lam[30] - M.s_inf_closed(30) - 1), 3))", 'num', None, C, None),
    ('I-59', 'b328_family', 'data/b328_family_run.txt', 7, ['+6.550532e-01'],
     "import b328_family as M\na = 40.0; f = M.SQ.autocorrelation(M.make_seed('E', a)); N = int(a*a) + 2\nlam_z, lam_q, _, _ = M.finite_sides(N)\n"
     "print(M.BW.channels(f, lam_z, lam_q, refine=1)['places_q'])", 'num', None, C, None),
    ('I-60', 'b333_diagnose', 'data/b333_diagnose_run.txt', 24, ['1.864e-06'],
     "import json, b333_diagnose as M\nR = json.load(open(M.os.path.join(M.D, 'b333_derive.json'), encoding='utf-8'))\narch = {}\n"
     "for ln in open(M.os.path.join(M.D, 'carto_atlas.jsonl'), encoding='utf-8'):\n    r = json.loads(ln) if ln.strip() else {}\n"
     "    if r.get('a') is not None: arch[str(r['a'])] = float(r['arch'])\n"
     "print(max(abs(R['cells'][a]['A3'] - arch[a if a in arch else str(float(a))]) for a in M.CELLS))", 'num', None, B, None),
    ('I-61', 'b334_aimmap', 'data/b334_chart_run.txt', 64, ['sealed rule 270'], '', 'num', None, C,
     'MORE THAN 60 s: the count 270 is the whole route (grid, three legs, chart), the covered leg alone 1906.9 s by its bank; no import-only '
     'route reaches it; priced at about 3,600 s on this host'),
    ('I-62', 'b340_li_control', 'data/b340_control_run3.txt', 31, ['-1.5541199559354118268'],
     "import b340_li_control as M\nprint(M.I_theta(1)[0])", 'num', None, C, None),
    ('I-63', 'b352_fit', 'data/b352_fit_run6.txt', 27, ['A=22.057336 p=1.551336 c=+1.151251e-02'],
     "import json, numpy as np, b352_fit as M\nP = json.load(open(M.os.path.join(%r, 'data', 'b339_price.json'), encoding='utf-8'))\n"
     "X = np.asarray(P['xs'], float); R = np.asarray(P['cells']['1.3']['R'], float)\nt1, S1, _ = M.fit(M.m1, [1.0, 1.0], X, R)\n"
     "t, S, r = M.fit(M.m2, list(t1) + [0.0], X, R)\nprint(*[repr(float(x)) for x in t])" % ROOT, 'num', None, C, None),
    ('I-64', 'b437_components', 'data/b437_components.txt', 116, ['Z 0.315810473  A 0.506671341'],
     "import b437_components as M\nr = M.run_cell(3.0)\nprint(r['zero'], r['arch'])", 'num', None, C, None),
    ('I-65', 'b501_bound', 'data/b501_components_c234.txt', 52, ['m_grid -1.391017772759520'],
     "import numpy as np, b501_bound as M\nL, s = 2.2, 2.2/8.0\ndef gauss(N):\n    v = np.linspace(-L, L, 2*N-1); return v, np.exp(-v**2/(2*s*s))\n"
     "print(repr(M.bound_for(gauss, M.LEVELS)['levels'][0]['m']))", 'num', None, C, None),
    ('I-66', 'b503_zero', 'data/b503_fixture.txt', 11, ['HOLDS TO 4.27e-14'],
     "import numpy as np, b503_zero as M\nv, w = M.vw(4.061553); dv = float(v[1]-v[0])\nex = M.BC.hhat_exact(v, w, M.LOW5); tr = M.AT.hhat(v, w, M.LOW5)\n"
     "s2 = (np.sin(M.LOW5*dv/2)/(M.LOW5*dv/2))**2\nprint(np.max(np.abs(ex - s2*tr)/np.abs(ex)))", 'num', None, C, None),
    ('I-67', 'b504_chain', 'data/b504_fixture.txt', 4, ['r -4.608526620042408e-08'],
     "import b504_chain as M\nK = M.kernels()\na = min((r['a'] for r in M.BZ.rows_all()), key=lambda x: abs(x-4.061553))\nprint(repr(M.cell(a, K)['r']))",
     'num', None, C, None),
    ('I-68', 'b511_families', 'data/b511_components.txt', 6, ['= 1.59e-14'],
     "import numpy as np, b511_families as M\nW = M.Window(5.0, 4, ())\n"
     "kb = np.unique(np.round((W.knots[:,None]+W.knots[None,:]).ravel(), 14)); kb = kb[(kb>=-2*W.half)&(kb<=2*W.half)]\n"
     "nd, wt = np.polynomial.legendre.leggauss(24); a0, b0 = kb[:-1], kb[1:]; mid, rad = (a0+b0)/2, (b0-a0)/2\n"
     "xx = (mid[:,None]+rad[:,None]*nd[None,:]).ravel(); ww = (rad[:,None]*wt[None,:]).ravel(); kx = W.k(xx, 10)\n"
     "us = np.array([0.0, 1.0, 5.0, 14.134725141734695, 30.0, 60.0])\nnum = np.array([float(np.sum(ww*kx*np.cos(u*xx))) for u in us])\n"
     "print(np.max(np.abs(W.khat(us).real - num)))", 'num', None, C, None),
    ('I-69', 'b512_table', 'data/b512_table.txt', 88, ['COMPILED'],
     "import b512_table as M\nprint('COMPILED' if M.in_kernel('h2_sign_imp_cell') else 'NOT COMPILED')", 'text', None, B, None),
    ('I-70', 'b514_window', 'data/b514_components.txt', 6, ['6.11e-16'],
     "import numpy as np, b514_window as M\nG0 = 14.1347; W = M.MWindow(5.0, G0)\n"
     "kb = np.unique(np.round((W.knots[:,None]+W.knots[None,:]).ravel(), 14)); kb = kb[(kb>=-2*W.half)&(kb<=2*W.half)]\n"
     "nd, wt = np.polynomial.legendre.leggauss(80); a0, b0 = kb[:-1], kb[1:]; mid, rad = (a0+b0)/2, (b0-a0)/2\n"
     "xx = (mid[:,None]+rad[:,None]*nd[None,:]).ravel(); ww = (rad[:,None]*wt[None,:]).ravel(); kx = W.k(xx, M.QH)\n"
     "G = M.F.GAM; near = sorted(G[np.argsort(np.abs(G-G0))[:3]].tolist()); near = [x for x in near if abs(x-G0) > 1e-3][:2]\n"
     "us = np.array([0.0, 1.0, G0] + near + [30.0, 60.0])\nnum = np.array([float(np.sum(ww*kx*np.cos(u*xx))) for u in us])\n"
     "print(np.max(np.abs(W.khat(us).real - num)))", 'num', None, C, None),
    ('I-71', 'b519_window', 'data/b519_components.txt', 24, ['1.6e-13'],
     "import b519_window as M\nW = M.VWindow(5.0, 'xi', 'B')\nprint(abs(W.k([0.7], M.QH)[0] - W.k([-0.7], M.QH)[0]))", 'num', None, C, None),
    ('I-72', 'b521_tail', 'data/b521_components.txt', 127, [': 6.0999e-09'],
     "import b521_tail as M\nprint(M.tail_s(M.PWindow(60.0, 'q', 7), 0.5))", 'num', None, C, None),
    ('I-73', 'b522_reach', 'data/b522_components.txt', 10, ['1.522e-06   1.669e-07'],
     "import b522_reach, b521_tail as B21\nc = B21.cell_q(15.0, 7)\nprint(c['Etail'], c['Bprime'])", 'num', None, C, None),
    ('I-74', 'b523_caveats', 'data/b523_components.txt', 151, ['eta = 1.994818 (exact part 1.968754'],
     "import b523_caveats as M\nr, a = M.tables()\nprint(*M.eta_bound(1.425, r, a)[:2])", 'num', None, C, None),
    ('I-75', 'b527_values', 'data/b527_values.json', 287, ['4.440892098500626e-16'],
     "import math, b527_values as M\nL=math.log(34.0); us=[(1-M.F)*L+M.F*L*(k+0.5)/20.0 for k in range(20)]\n"
     "print(max(abs(float(M.phi_chain(u,34.0))-float(M.phi_kernel_mp(u,34.0))) for u in us+[-x for x in us]))", 'num', None, C, None),
    # ### b723, the author's word (3): the row reads its tool's pinned input -- b542_record.REPOS rebound in memory to b544's pins, the eleven
    # ### repositories it cites by no pin at the last first-parent commit at or before data/b544_decls.json's commit time (deb2a187), as
    # ### tools/b723_i76.py read them (data/b723_i76.txt: the inputs class CONFIRMED, 5293 at b544's pins, 6650 over today's trees)
    ('I-76', 'b544_probe_part', 'data/b544_decls.json', 1, ['"count": 5293'],
     "import b542_record as Q, b544_probe_part as M\nt = '2026-09-26T01:45:59-04:00'\n"
     "Q.REPOS = [(r, c or Q.g(r, 'rev-list', '-1', '--first-parent', '--before=' + t, 'HEAD').strip(), x) for r, c, x in Q.REPOS]\n"
     "ds, fed = M.classify(M.enumerate_all())\nprint(len(ds))", 'num', None, C, None),
    ('I-77', 'b634_elab', 'data/b634_elab_types.txt', 4, ['927 ; MISSING : 13'],
     "import b634_elab as M\nB=M.load_bank_text(open(M.TYPES, encoding='utf-8').read())\n"
     "print(sum(1 for v in B.values() if not v['missing']), sum(1 for v in B.values() if v['missing']))", 'num', None, B, None),
    ('I-78', 'b661_map', 'data/b661_detection_map.txt', 252, ['NONE ≤ J_max'],
     "import b661_map as M\nfrom flint import ctx; ctx.prec=M.PREC\nn,zl,ok,_a,_b=M.zero_list(); lo,hi=M.i4_ball(); i4=M.span(lo,hi)\n"
     "print(M.cell('0.8','29.6',M.PREC,zl,i4)['reading'])", 'text', None, C, None),
    ('I-79', 'b662_map', 'data/b662_detection_map_40.txt', 750, ['j₀ = 31'],
     "import b662_map as M\nfrom flint import ctx; ctx.prec=M.PREC\nn,zl,ok,_a,_b=M.zero_list(); lo,hi=M.i4_ball(); i4=M.span(lo,hi)\n"
     "print(M.cell('0.8','29.6',M.PREC,zl,i4)['reading'])", 'num', None, C, None),
    ('I-80', 'b663_epstein_map', 'data/b663_epstein_control.txt', 86, ['j₀ = 38'],
     "import b663_epstein_map as M\nfrom flint import ctx; ctx.prec=M.PREC\nlo,hi=M.i4_ball(); i4s={M.PREC: M.span(lo,hi)}; on,off=M.q0_list()\n"
     "print(M.run_cell('Q0 AT qE0', off[M.Q0_BASE], on, off, i4s, None, above=M.Q0_T, a0_premise=M.Q0_A0)['reading'])", 'num', None, C, None),
    ('I-81', 'b667_epstein_certify', 'data/b667_epstein_counts.txt', 34, ['[3.54841378141857 +/- 1.08e-15]'],
     "import b667_epstein_certify as M\nfrom flint import acb, arb, ctx; ctx.prec=M.PREC\nprint(M.zq(acb(arb(3)/2, 0)).real.str(15, radius=True))",
     'num', None, C, None),
    ('I-82', 'b667_epstein_map_balls', 'data/b667_epstein_control_balls.txt', 81, ['HYP-UNVERIFIED(hQtie)'],
     "import b667_epstein_map_balls as M\nfrom flint import ctx; ctx.prec=M.PREC\nlo,hi=M.i4_ball(); i4s={M.PREC: M.span(lo,hi)}; on,off=M.q0_list()\n"
     "print(M.run_cell('Q0 AT qE0', off[M.Q0_BASE], on, off, i4s, None, above=M.Q0_T, a0_premise=M.Q0_A0)['reading'])", 'text', None, C, None),
    ('I-83', 'b671_narrow', 'data/b671_narrow_log.txt', 6, ['depth 40'],
     "import b671_narrow as M\nfrom flint import acb, ctx; ctx.prec=M.PREC\nt0=acb.zeta_zero(1).imag.mid().str(M.DIGITS, radius=False)\n"
     "r,_=M.narrow_on(M.lam_z_at, 'C1 n=1', t0, M.H0)\nprint(r['depth'], r['reading'])", 'num', None, C, None),
    ('I-84', 'b675_li_bench', 'data/b675_li_bench.txt', 851, ['HOLD) 63676'],
     "import b675_li_bench as M\nprint(M.constants_for(M.terms(M.reps()), 'ref0')['n_star'])", 'num', None, C, None),
    ('I-85', 'b677_epstein_map_angle', 'data/b677_map.txt', 131, ['PASS 29 (j 24-52)'],
     "import b677_epstein_map_angle as M\nfrom flint import ctx; ctx.prec=M.PREC\np=[x['j'] for x in M._tie_cell()['ties'] if x['word']=='PASS']\n"
     "print('%d (j %d-%d)' % (len(p), min(p), max(p)))", 'num', None, C, None),
    ('I-86', 'b685_count', 'data/b685_count.txt', 21, ['a = 0.432571915432'],
     "import b685_count as M\nfrom flint import ctx; ctx.prec=M.PREC\ngrid=M.get('b685_count_part1.json')['grid']; pr=M.params_q(grid, 1.7, 2.05, 0.2)\n"
     "I=M.jensen(pr, M.N_FINAL, M.A(M.T_MIN))\nprint(M.bs((I[0]-1)/(2*pr['ell'])))", 'num', None, C, None),
    ('I-87', 'b687_readings', 'data/b687_composition.txt', 12, ['MARGIN 41.9784580673'],
     "import b687_readings as M\nprint(M.bs(M.des(M.composition()['narrowest']['margin'])))", 'num', None, C, None),
    ('I-88', 'b694_witness', 'data/b694_witness_zeros.txt', 5, ['= 0.453260474794660686250509013567280024290084839'],
     "import b694_witness as M\nr=[x for x in M.balls()['rows'] if x['kind']=='OFF'][0]\nprint(M._minus_half(r['re']))", 'num', None, C, None),
    ('I-89', 'b694_witness_terms', 'data/b694_witness.txt', 15, ['S -7.7752874967979'],
     "import b694_witness_terms as M\nprint(M.fmt(M.bl(M.terms(M.Window('32','N'),'q0')['S'])))", 'num', None, C, None),
    ('I-90', 'b696_witness_balls', 'data/b696_witness_balls.txt', 14, ['S -7.7752874967979'],
     "import b696_witness_balls as M\nprint(M.fmt(M.bl(M.terms(M.W.Window('32','N'),'q0')['S'])))", 'num', None, C, None),
    ('I-91', 'b705_detection', 'data/b705_detection.txt', 10, ['n* 63651'],
     "import b705_detection as M\nprint(M.B.constants_for(M.B.terms(M.pair_rows(M.rows_all(), 0)), 'ref0')['n_star'])", 'num', None, C, None),
    ('I-92', 'b707_onset', 'data/b707_onset.txt', 12, ['S_CC 10.46804976'],
     "import b707_onset as M\nu=M.units()[('terms','band','C','log2','q0')]\nprint(M.fmt(M.bl(u['S']),10))", 'num', None, U, None),
    ('I-93', 'b709_grid', 'data/b709_grid.txt', 409, ['lambda -0.003719132066'],
     "import b709_grid as M\nU=M.units(); pt=M.grid('rho0')[362]; us,G,Mm,r=M._form(U,'rho0',pt,'q0')\nprint(M.fmt(M.bl(r['lmin']),10))", 'num', None, U, None),
    ('I-94', 'b709_pairs', 'data/b709_pairs.txt', 46, ['n* 1646498'], "import b709_pairs as M\nM.pairs('5','5')", 'num', r'n\* \d+', U, None),
    ('I-95', 'b710_fit', 'data/b710_fit.txt', 21, ['alpha 19.065093 ; beta 7.997097'],
     "import math, b710_fit as M\nR=[x for x in M.rows() if x['nstar']]\nprint(*M.lsq([math.log(x['nstar']+1) for x in R], [x['r']*x['nstar'] for x in R]))",
     'num', None, C, None),
    ('I-96', 'b711_coeffs', 'data/b711_coeffs.txt', 12, ['(-8) log 2 + (-2) log 3'],
     "import b711_coeffs as M, b694_witness_terms as W\nfrom flint import fmpq\nN=100; spf=M.spf_table(N); lam,r=W.lambda_q(N)\n"
     "c=M.recursion([fmpq(r[k],2) for k in range(N+1)],N,spf)\nprint(M.show(c[48]))", 'num', None, C, None),
    ('I-97', 'b711_list', 'data/b711_list.txt', 16, ['COMPLETE TO 445.0'],
     "import b711_list as M\nU=M.units()\nprint(M.P9._complete_to(M.P9._bands(U),U))", 'num', None, U, None),
    ('I-98', 'b712_genus_control', 'data/b712_genus_control.txt', 43, [': 0'],
     "import b712_genus_control as M\nrows,misses=M.compute()\nprint(len(misses))",
     'num', None, C, None),
    ('I-99', 'b713_list', 'data/b713_list.txt', 74, ['COMPLETE TO 199.33082'], "import b713_list as M\nM.status()", 'num', r'COMPLETE TO [\d.]+', U, None),
    ('I-100', 'b713_predict', 'data/b713_predictions.txt', 10, ['n*_pred 50972.9'],
     "import b713_predict as M\nT0p,on,pairs,j=M.list_rows(); k,off,ref=pairs[0]\nc=M.P9.constants_for709(M.B.terms(on+[off,ref]),'ref1',T0p,1)\n"
     "print(M.law(M.P9._arb(c['C']), M.P5.r_of(off[1],off[2])).mid().str(10, radius=False))", 'num', None, C, None),
    ('I-101', 'b716_genus_control', 'data/b716_genus_control.txt', 46, [': 0'],
     "import b716_genus_control as M\nc=M.compute()\nprint(len(c['misses']))", 'num', None, C, None),
    ('I-102', 'b717_coeffs', 'data/b717_coeffs.txt', 16, ['n = 120'],
     "import b717_coeffs as M, b711_coeffs as C\nN=200; spf=C.spf_table(N)\nb,c,neg,und,vals=M.coeffs(M.counts((1,1,10),-39,N),N,spf)\nprint(neg[0])",
     'num', None, C, None),
    ('I-103', 'b717_list', 'data/b717_list.txt', 69, ['COMPLETE TO 200.0'], "import b717_list as M\nM.status()", 'num', r'COMPLETE TO [\d.]+', U, None),
    ('I-104', 'b717_predict', 'data/b717_predictions.txt', 11, ['n*_pred 207551.1'],
     "import b717_predict as M\nT0p,on,pairs,j=M.list_rows(); k,off,ref=pairs[0]\nc=M.P9.constants_for709(M.B.terms(on+[off,ref]),'ref1',T0p,1)\n"
     "print(M.law(M.P9._arb(c['C']), M.P5.r_of(off[1],off[2])).mid().str(10, radius=False))", 'num', None, C, None),
    ('I-105', 'b718_abstract', 'data/b718_derivation.txt', 104, ['shapes 4'],
     "import b718_abstract as M\nr=M.census(groups=[(3,)], oms=(4,5), verbose=False)\nprint(sum(v['minimal'] for v in r.values()))", 'num', None, C, None),
    ('I-106', 'b718_classgroup', 'data/b718_derivation.txt', 6, ['-23: h 3, ALL TRUE ; -15: h 2, ALL TRUE'],
     "import b718_classgroup as M\nprint(' ; '.join('%d: h %d, ALL %s' % (D, len(M.group(D)[0]), str(all(M.group(D)[3].values())).upper()) for D in (-23, -15)))",
     'text', None, C, None),
    ('I-107', 'b718_pin', 'data/b718_pin.txt', 7, ['BUILDS 1'], '', 'num', None, C,
     'A NETWORK READ: the figure is run 40587516142`s read (route `read SIDE-effects 40587516142`, which appends to data/b718_pin_rows.json); '
     'priced at one read of the run and its artifact, under a minute, with a bank write the route would make'),
    ('I-108', 'b720_predict', 'data/b720_prediction.txt', 21, ['n0 = 135', 'b(n0) = -2'],
     "import b720_predict as M\nr=M.predict(M.setup(-35))\nprint(r['n'], r['b'])", 'num', None, C, None),
]


def free_mb():
    class _MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = _MS()
    m.dwLength = ctypes.sizeof(_MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ullAvailPhys // 2 ** 20


def listing():
    return subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--untracked-files=all', '--', 'tools', 'data'],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def sig(s):
    d = decimal.Decimal(s)
    t = d.as_tuple()
    digits = list(t.digits)
    while len(digits) > 1 and digits[0] == 0:
        digits.pop(0)
    return d, len(digits)


def is_int(s):
    return not re.search(r'[.eE]', s)


def same_number(b, c):
    if is_int(b) and is_int(c):
        return int(b) == int(c)
    db, kb = sig(b)
    dc, kc = sig(c)
    k = max(1, min(kb, kc))
    with decimal.localcontext() as ctx:
        ctx.prec = 200
        ctx.rounding = decimal.ROUND_HALF_EVEN
        return ('{:.%de}' % (k - 1)).format(db) == ('{:.%de}' % (k - 1)).format(dc)


def compare(mode, banked, got):
    if mode == 'text':
        return got.strip() == banked.strip(), 'text'
    bn, gn = NUM.findall(banked), NUM.findall(got)
    if not bn or len(gn) < len(bn):
        return False, 'numbers banked %d, computed %d' % (len(bn), len(gn))
    return all(same_number(b, c) for b, c in zip(bn, gn)), 'numbers %s against %s' % (bn, gn[:len(bn)])


def plant(mode, banked):
    if mode == 'text':
        return banked + ' (planted)'
    m = NUM.search(banked)
    s = m.group(0)
    i = next(k for k, ch in enumerate(s) if ch.isdigit() and ch != '0') if re.search(r'[1-9]', s) else next(k for k, ch in enumerate(s) if ch.isdigit())
    d = int(s[i])
    return banked[:m.start()] + s[:i] + str((d + 1) % 10 if d != 9 else 8) + s[i + 1:] + banked[m.end():]


def banked_figure(bank, line, figs):
    L = open(os.path.join(ROOT, bank), encoding='utf-8', errors='replace').read().split(NL)
    text = L[line - 1] if 0 < line <= len(L) else ''
    miss = [f for f in figs if f not in text]
    return ' '.join(figs), miss


def run_row(r, scratch):
    rid, tool, bank, line, figs, call, mode, pat, kind, notrun = r
    fig, miss = banked_figure(bank, line, figs)
    out = dict(id=rid, tool=tool, bank=bank, line=line, figure=fig, kind=kind, call=call, mode=mode)
    if miss:
        out.update(grade='DIFFERS', why='THE FIGURE NOT AT ITS BANK LINE: %r' % miss)
        return out
    if notrun:
        out.update(grade='NOT RUN', why=notrun)
        return out
    out['free_mb'] = free_mb()
    if out['free_mb'] < HOLD_MB:
        out.update(grade='NOT RUN', why='FREE MEMORY %d MB UNDER THE HOLD %d MB' % (out['free_mb'], HOLD_MB))
        return out
    before, t0 = listing(), time.time()
    try:
        p = subprocess.run([sys.executable, '-X', 'utf8', '-c', PRE + call], capture_output=True, text=True, encoding='utf-8', errors='replace',
                           timeout=TIMEOUT, cwd=scratch)
        stdout, rc = p.stdout, p.returncode
    except subprocess.TimeoutExpired:
        out.update(grade='NOT RUN', why='TIMED OUT AT %d s IN THIS RUN' % TIMEOUT, seconds=TIMEOUT)
        return out
    out['seconds'] = round(time.time() - t0, 1)
    wrote = sorted(set(listing().split(NL)) ^ set(before.split(NL)))
    lines = [l for l in stdout.split(NL) if l.strip()]
    if pat:
        m = re.search(pat, stdout)
        got = m.group(0) if m else ''
    else:
        got = lines[-1] if lines else ''
    out['got'] = got[:400]
    if rc != 0:
        out.update(grade='DIFFERS', why='THE CALL EXITED %d: %s' % (rc, p.stderr.strip().split(NL)[-1][:300] if p.stderr.strip() else ''))
        return out
    if wrote:   # ### (R332)(7) names three grades; a call that writes does not reproduce, its writes printed as the reason
        out.update(grade='DIFFERS', why='THE CALL WROTE UNDER tools/ OR data/: %s' % wrote)
        return out
    ok, how = compare(mode, fig, got)
    pl = plant(mode, fig)
    pok, _ = compare(mode, pl, got)
    out.update(grade='REPRODUCES' if ok else 'DIFFERS', why=how, planted=pl, planted_grade='REPRODUCES' if pok else 'DIFFERS',
               planted_as_wanted=not pok)
    return out


def run(*a):
    bank = a[a.index('--bank') + 1] if '--bank' in a else None
    only = set(a[a.index('--only') + 1].split(',')) if '--only' in a else None
    t0 = time.time()
    L = ['tools/research/reproduce.py -- THE RESEARCH INSTRUMENTS REPRODUCED, ONE ROW PER INSTRUMENT (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
         '', '### ' + RULE, '### rows %d ; the hold %d MB ; the cap %d s a row ; relay %s' % (len(ROWS), HOLD_MB, TIMEOUT, ROOT), '']
    print(NL.join(L), flush=True)
    J = []
    with tempfile.TemporaryDirectory() as scratch:
        for r in ROWS:
            if only and r[0] not in only:
                continue
            x = run_row(r, scratch)
            J.append(x)
            row = ['%-6s %-24s %-11s %s :%d -- "%s" (%s)' % (x['id'], x['tool'], x['grade'], x['bank'], x['line'], x['figure'], x['kind'])]
            if x['grade'] in ('REPRODUCES', 'DIFFERS') and 'got' in x:
                row.append('         computed "%s" in %s s (free %s MB) ; %s' % (x['got'][:200], x.get('seconds'), x.get('free_mb'), x['why'][:300]))
                if 'planted' in x:
                    row.append('         PLANTED "%s": %s -- %s' % (x['planted'], x['planted_grade'], 'AS WANTED' if x['planted_as_wanted'] else 'NOT AS WANTED'))
            else:
                row.append('         ' + x['why'])
            row.append('         CALL: ' + (x['call'].replace(NL, ' ; ')[:600] if x['call'] else '(none: the route named in the reason)'))
            print(NL.join(row), flush=True)
            L += row
    n = dict((g, sum(1 for x in J if x['grade'] == g)) for g in ('REPRODUCES', 'DIFFERS', 'NOT RUN'))
    pw = sum(1 for x in J if x.get('planted_as_wanted'))
    pr = sum(1 for x in J if 'planted' in x)
    foot = ('### ### **ROWS %d ; REPRODUCES %d ; DIFFERS %d ; NOT RUN %d ; PLANTED CONTROLS AS WANTED %d OF %d ; %d s.**' % (
        len(J), n['REPRODUCES'], n['DIFFERS'], n['NOT RUN'], pw, pr, int(time.time() - t0)))
    L += ['', foot]
    print(NL + foot)
    if bank:
        for ext, data in (('.txt', NL.join(L) + NL), ('.json', json.dumps(dict(rule=RULE, counts=n, planted=[pw, pr], rows=J), indent=1, ensure_ascii=False) + NL)):
            p = os.path.join(ROOT, bank + ext)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(data.encode('utf-8'))
            os.replace(p + '.tmp', p)
        print('written %s.txt, .json' % bank)


def rows(*a):
    for r in ROWS:
        print('%-6s %-24s %s :%d %r%s' % (r[0], r[1], r[2], r[3], r[4], ' NOT RUN' if r[9] else ''))


if __name__ == '__main__':
    fn = dict(run=run, rows=rows).get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit('usage: reproduce.py run [--bank data/<name>] [--only I-nn,...] | rows')
    fn(*sys.argv[2:])
