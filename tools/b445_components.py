# -*- coding: utf-8 -*-
"""b445_components.py -- WHOSE RESIDUAL IT IS. ### **UNDER (R57): THE SAME CHAIN, THE SAME CELLS, TWO PARAMETERS.**

### Usage: `python b445_components.py run <arm>` for arm in base, a, a_nv, a_nu, b -- each cell's result is banked
### in `data/b445_arms.json` as soon as it is computed, so a run can resume; `python b445_components.py report`
### applies the decision rule the face fixed and writes `data/b445_components.txt`.
### ### No chain file is edited: `nv` is passed; `NU` is set on the imported atlas module with its kernel cache
### cleared; the library is swapped on the module for arm (b) and restored.
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
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
D = os.path.join(ROOT, 'data')
ARMS = os.path.join(D, 'b445_arms.json')
OUT = os.path.join(D, 'b445_components.txt')
FLOOR = 1.49e-08
NV0, NU0 = 8193, 12001
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load():
    try:
        return json.load(io.open(ARMS, encoding='utf-8'))
    except Exception:
        return {}


def save(d):
    io.open(ARMS + '.tmp', 'w', encoding='utf-8').write(json.dumps(d, indent=1))
    os.replace(ARMS + '.tmp', ARMS)


def cells():
    dec = json.load(io.open(os.path.join(D, 'b444_decorrelation.json'), encoding='utf-8'))
    return [(x['a'], x['e']) for x in dec['above']]


def run_arm(arm):
    import numpy as np
    import carto_atlas as AT
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    assert SQ.AUTOCORR_NV == NV0 and AT.NU == NU0 and len(AT.GAM) == 10000, 'the chain is not at its banked constants'
    nv = 2 * NV0 - 1 if arm in ('a', 'a_nv') else NV0
    nu = 2 * NU0 - 1 if arm in ('a', 'a_nu') else NU0
    gam0 = AT.GAM
    if arm == 'b':
        ext = np.load(os.path.join(D, 'b445_ordinates_10001_15000.npy'))
        AT.GAM = np.concatenate([gam0, ext])
    AT.NU = nu
    AT._KERN = None
    d = load()
    d.setdefault(arm, {})
    try:
        for a, e_banked in cells():
            key = '%.6f' % a
            if key in d[arm]:
                continue
            t = time.time()
            g = SM.mean_zero_variant(a)
            f = SQ.autocorrelation(g, nv=nv)
            ch = WI.channels(f.v, f.w)
            d[arm][key] = dict(a=a, e=ch['residual'], zero=ch['zero'], arch=ch['arch'], prime=ch['prime'],
                               pole=ch['pole'], nv=nv, nu=nu, ngam=int(len(AT.GAM)), e_banked=e_banked,
                               seconds=round(time.time() - t, 1))
            save(d)
            print('%-5s a=%-10s e=%+.4e (banked %+.4e) %.0fs' % (arm, key, ch['residual'], e_banked, time.time() - t),
                  flush=True)
    finally:
        AT.GAM = gam0
        AT.NU = NU0
        AT._KERN = None


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)
    import numpy as np
    d = load()
    C = cells()
    rec('=' * 100)
    rec('b445 -- WHOSE RESIDUAL IT IS. ### THE COMPONENTS, RUN AFTER THE LOCK, UNDER (R57).')
    rec('=' * 100)
    rec('')
    rec('  ### ### **COMPONENT 1 -- DOES THE ZERO SIDE TRUNCATE? FROM THE CHAIN`S OWN SOURCE.**')
    src = io.open(os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py'), encoding='utf-8').read().splitlines()
    for ndl in ('NGAM    = 10000', 'GAM = np.load', 'Truncation bound for the zero side is computed'):
        hit = [(i + 1, l.strip()) for i, l in enumerate(src) if ndl in l]
        rec('      carto_atlas.py:%d | %s' % hit[0])
    lib = np.load(os.path.join(ROOT, 'tools', 'e16', 'zeta_ordinates.npy'))
    rec('      the library file holds %d ordinates, the last %.12f' % (len(lib), lib[-1]))
    bounds = [r['bound'] for r in json.load(io.open(os.path.join(D, 'b437_rungs.json'), encoding='utf-8'))['rows']
              if r.get('bound') is not None]
    rec('      the source`s own truncation bound, as b437 banked it : max %.2e' % max(bounds))
    rec('    ### ### **YES: THE ZERO SIDE TRUNCATES AT 10000 ORDINATES, HEIGHT %.6f. THE COUNT IS IN THE SOURCE; THE' % lib[-1])
    rec('    ### ### HEIGHT IS IN THE DATA FILE THE SOURCE LOADS. THE HYPOTHESIS IS ALIVE; THE SOURCE`S BOUND PUTS ITS TAIL')
    rec('    ### ### BELOW %.1e.**' % max(bounds))
    rec('    ### (P4), declared on the face: the library differs from mpmath by up to 1.1e-04 above n = 100.')

    rec('')
    rec('  ### ### **COMPONENT 2 -- THE DISCRIMINATOR**')
    ordrun = io.open(os.path.join(D, 'b445_ordinates_run.txt'), encoding='utf-8').read() \
        if os.path.exists(os.path.join(D, 'b445_ordinates_run.txt')) else ''
    rec('    ordinates control : %s' % ('PASS' if 'CONTROL : PASS' in ordrun else ('FAIL' if ordrun else 'NOT RUN')))
    base = d.get('base', {})
    repro = {k: abs(v['e'] - v['e_banked']) <= 1e-12 for k, v in base.items()}
    rec('    base reproduces the banked residual to 1e-12 at %d of %d cells' % (sum(repro.values()), len(C)))
    good = [('%.6f' % a) for a, _ in C if repro.get('%.6f' % a)]
    rec('')
    hdr = '    %-10s %-12s %-12s %-12s %-12s %-12s %-12s' % ('a', 'e base', 'e (a) grid', 'e (b) reach', 'a: nv only', 'a: NU only', 'rate (a)')
    rec(hdr)
    status = {'a': {}, 'b': {}}
    rates = {}
    for a, _ in C:
        k = '%.6f' % a
        eb = base.get(k, {}).get('e')
        row = [eb] + [d.get(arm, {}).get(k, {}).get('e') for arm in ('a', 'b', 'a_nv', 'a_nu')]
        if k in good:
            for arm, ev in (('a', row[1]), ('b', row[2])):
                if ev is None:
                    status[arm][k] = 'NOT RUN'
                elif abs(ev) <= 0.5 * abs(eb) or abs(ev) <= FLOOR:
                    status[arm][k] = 'FALLS'
                elif abs(ev - eb) <= 0.1 * abs(eb):
                    status[arm][k] = 'STABLE'
                else:
                    status[arm][k] = 'MOVES'
            if row[1] is not None and status['a'][k] == 'FALLS' and row[1] != 0:
                rates[k] = math.log2(abs(eb) / abs(row[1]))
        fmt = lambda x: ('%+.3e' % x) if isinstance(x, float) else ('NOT RUN' if x is None else str(x))
        rec('    %-10s %-12s %-12s %-12s %-12s %-12s %-12s%s' % (k, fmt(row[0]), fmt(row[1]), fmt(row[2]), fmt(row[3]),
                                                             fmt(row[4]), ('%.2f' % rates[k]) if k in rates else '-',
                                                             '' if k in good else '   ### DROPPED -- base does not reproduce'))
    rec('')
    for arm in ('a', 'b'):
        cnt = {}
        for k, s_ in status[arm].items():
            cnt[s_] = cnt.get(s_, 0) + 1
        rec('    arm (%s) per-cell : %s' % (arm, cnt))
    below = {arm: sum(1 for a, _ in C if abs(d.get(arm, {}).get('%.6f' % a, {}).get('e', 1)) <= FLOOR) for arm in ('base', 'a', 'b')}
    rec('    cells below the floor : base %d, arm (a) %d, arm (b) %d -- a value below the floor is the instrument`s' % (below['base'], below['a'], below['b']))
    n = len(good)

    def arm_state(arm):
        falls = sum(1 for s_ in status[arm].values() if s_ == 'FALLS')
        stable = sum(1 for s_ in status[arm].values() if s_ == 'STABLE')
        notrun = sum(1 for s_ in status[arm].values() if s_ == 'NOT RUN')
        if notrun:
            return 'NOT RUN', falls, stable
        return ('FALLS' if falls >= 8 else ('STABLE' if stable >= 12 else 'MIXED')), falls, stable
    sa, fa, ta = arm_state('a')
    sb, fb, tb = arm_state('b')
    rec('    ARM (a) : %s (falls %d, stable %d) ; ARM (b) : %s (falls %d, stable %d)' % (sa, fa, ta, sb, fb, tb))
    if n < 8:
        verdict = 'NOT DECIDED -- THE CHAIN DOES NOT REPRODUCE ITS BANK'
    elif sa == 'FALLS' and sb == 'STABLE':
        verdict = 'INTEGRATION'
    elif sb == 'FALLS' and sa == 'STABLE':
        verdict = 'TRUNCATION'
    elif sa == 'STABLE' and sb == 'STABLE':
        verdict = 'UNDETERMINED'
    elif 'NOT RUN' in (sa, sb):
        verdict = 'NOT DECIDED -- AN ARM NOT RUN'
    elif sa == 'FALLS' and sb == 'FALLS':
        verdict = 'BOTH MOVE'
    else:
        verdict = 'MIXED'
    rec('')
    rec('  ### ### **VERDICT, BY THE RULE FIXED ON THE FACE : %s.**' % verdict)
    if rates:
        rec('    apparent order of arm (a), log2(|e_base| / |e_a|): median %.2f over %d cells'
            % (sorted(rates.values())[len(rates) // 2], len(rates)))
    nv_same = max(abs(d.get('a_nv', {}).get(k, {}).get('e', 1.0) - d.get('a', {}).get(k, {}).get('e', 0.0)) for k in good)
    nu_same = max(abs(d.get('a_nu', {}).get(k, {}).get('e', 1.0) - base[k]['e']) for k in good)
    rec('    halves, beside and not governing: max |e(nv only) - e(a)| %.2e ; max |e(NU only) - e(base)| %.2e' % (nv_same, nu_same))
    report_ = dict(verdict=verdict, arm_a=sa, arm_b=sb, falls_a=fa, stable_a=ta, falls_b=fb, stable_b=tb,
                   reproduced=n, rates=rates, status=status, below=below, nv_half_vs_a=nv_same, nu_half_vs_base=nu_same)
    rec('')
    rec('  ### ### **COMPONENT 3 -- WHAT THE VERDICT OBLIGES**')
    import glob
    import tokenize

    def code(pth):
        out_ = []
        try:
            for tk in tokenize.generate_tokens(io.open(pth, encoding='utf-8', errors='replace').readline):
                if tk.type in (tokenize.COMMENT, tokenize.STRING):
                    continue
                out_.append(tk.string)
        except Exception:
            return ''
        return re.sub(r'\s*\.\s*', '.', ' '.join(out_))
    users = []
    for pth in sorted(glob.glob(os.path.join(ROOT, 'tools', 'b3[2-9][0-9]_*.py')) + glob.glob(os.path.join(ROOT, 'tools', 'b4[0-4][0-9]_*.py'))):
        c = code(pth)
        k = [x for x in ('channels', 'autocorrelation', 'prime_sum', 'hhat_blocked')
             if re.search(r'\b(WI|WIN|W|b321_window|SQ|b318_square)\.' + x + r' \(', c)]
        if k and not os.path.basename(pth).startswith('b445'):
            users.append((os.path.basename(pth), k))
    if verdict == 'INTEGRATION':
        rec('    ### ### **b444`S STRUCTURE VERDICT IS RESTATED AS THE CHAIN`S: THE RESIDUAL IS THE CHAIN`S INTEGRATION.**')
        if nv_same <= 1e-12 and nu_same <= 1e-12:
            rec('    ### by the halves, printed beside and not governing: the nv-only half reproduces arm (a) to %.1e and the' % nv_same)
            rec('    ### NU-only half reproduces the base to %.1e -- the autocorrelation grid carries it, the frequency grid does not.' % nu_same)
        rec('    ### **b444`s banked verdict is not edited; its owner is named here.**')
        rec('    ### **EVERY TOOL WHOSE CODE RAN THIS CHAIN, LISTED FOR ITS OWNER TO CHECK -- NONE RE-VERDICTED:**')
        for nm, k in users:
            rec('      %-28s calls %s' % (nm, ', '.join(k)))
        rec('    ### %d tools. The figures they banked rest on the chain`s default grid unless their own record says otherwise;' % len(users))
        rec('    ### which of their figures are small enough for this to bear on is for their owner to check. None is re-verdicted.')
    elif verdict == 'TRUNCATION':
        rec('    ### the identity closes with the reach, and the reach becomes a stated parameter of every cell; tools listed:')
        for nm, k in users:
            rec('      %-28s calls %s' % (nm, ', '.join(k)))
    elif verdict == 'UNDETERMINED':
        rec('    ### the residual filed at its measured size with two refutations; the third test priced below.')
    rec('    ### ### **THE FOURTH CANDIDATE, PRICED AND NOT RUN:** the inherited ordinates` precision (P4) -- replace the')
    rec('    ### library by mpmath ordinates at 25 digits for n = 101 ... 10000 and re-run the base: about 9900 ordinates at')
    rec('    ### 1.5-3 s each, about 40 minutes on ten workers; a MEASUREMENT, outside (R57)`s two parameters.')
    report_['chain_users'] = [dict(tool=nm, calls=k) for nm, k in users]
    d = load()
    d['report'] = report_
    save(d)
    rec('    ### NO CLAIM ABOUT ZEROS IN ANY BRANCH; the zero side is inherited, and the extension ordinates are mpmath`s.')
    rec('    ### ### **THE INSTRUMENT LANE OPENED BY (R57) CLOSES AT THIS ACT`S END.** No instrument built; no chain file edited.')
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return verdict


if __name__ == '__main__':
    if sys.argv[1] == 'run':
        run_arm(sys.argv[2])
    else:
        report()
