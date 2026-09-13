# -*- coding: utf-8 -*-
"""b447_components.py -- THE OUTLIER, THE ARM THAT BITES, AND THE STOCK-TAKE. ### **UNDER (R60), AFTER THE LOCK.**

### Usage: `run` -- the third doubling at a = 4.123106 into `data/b447_doubling.json`;
### `loom` -- Component 2's one loom block (by `b244_loom_append.py`) and one line appended to `BAR_FLOOR_RULE.md`;
### `report` -- Components 1 and 3 into `data/b447_components.txt` and `data/b447_stocktake.json`.
### ### No chain file is edited: `nv` is passed; `NU` is set on the imported atlas module with its kernel cache cleared
### and restored -- b446's code path, carried.
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
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
DBL = os.path.join(D, 'b447_doubling.json')
OUT = os.path.join(D, 'b447_components.txt')
STK = os.path.join(D, 'b447_stocktake.json')
BLOCK = os.path.join(D, 'b447_loom_block.md')
LOOMRUN = os.path.join(D, 'b447_loom_append_run.txt')
BFR = os.path.join(TE, 'modules', '2026-09', 'BAR_FLOOR_RULE.md')
CELL = '4.123106'
NV0, NU0 = 8193, 12001
NV3, NU3 = 65537, 96001
M_OTHERS = 1.4465
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(p):
    try:
        return json.load(io.open(p, encoding='utf-8'))
    except Exception:
        return {}


def run():
    import carto_atlas as AT
    import b317_smear as SM
    import b318_square as SQ
    import b321_window as WI
    assert SQ.AUTOCORR_NV == NV0 and AT.NU == NU0 and len(AT.GAM) == 10000, 'the chain is not at its banked constants'
    d = load(DBL)
    if CELL in d:
        print('already run')
        return
    a = load(os.path.join(D, 'b445_arms.json'))['a'][CELL]['a']
    AT.NU = NU3
    AT._KERN = None
    try:
        t = time.time()
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g, nv=NV3)
        ch = WI.channels(f.v, f.w)
        d[CELL] = dict(a=a, e=ch['residual'], zero=ch['zero'], arch=ch['arch'], prime=ch['prime'], pole=ch['pole'],
                       nv=NV3, nu=NU3, ngam=int(len(AT.GAM)), seconds=round(time.time() - t, 1))
        io.open(DBL + '.tmp', 'w', encoding='utf-8').write(json.dumps(d, indent=1))
        os.replace(DBL + '.tmp', DBL)
        print('aaa a=%s e=%+.6e %.0fs' % (CELL, ch['residual'], time.time() - t))
    finally:
        AT.NU = NU0
        AT._KERN = None


def loom():
    cj = load(os.path.join(D, 'b446_floor_census.json'))
    kd, res = cj['kind'], cj['residue']
    block = NL.join([
        '',
        '<!-- b447 loom entry -->',
        '',
        '### **THE ARM THAT BITES — noted once, 2026-09-12 (b447)**',
        '',
        '`relay/tools/noise_floor.py` gives every verdict two arms: a FLOOR arm (`|value| <= sqrt(machine epsilon) = 1.49e-08`) '
        'and a DRIFT arm (relative change under refinement against `1e-3`). Its own header, written at b272, already said which '
        'one carries the weight: *"A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR OF b264\'s FLOOR MODES"* and *"IT IS THE '
        'DRIFT ARM THAT BITES, NOT THE FLOOR ARM."*',
        '',
        'b446 counted it (`relay/data/b446_floor_census.txt`). There were **%d** banked comparisons against the floor, and **%d** '
        'of them were of a kind other than the spectral or modal quantities it was measured on. The floor arm fired **%d** '
        'times, in structured records, **every one on a value of exactly zero, which any positive floor refuses. The floor\'s '
        'size decided no banked verdict.**' % (kd['all'], kd['out'], res['json_verdicts']['AT_FLOOR']),
        '',
        '**So the gate\'s verdicts are the drift arm\'s, and a closing that reads "resolved against the floor" names the arm '
        'that did not decide.** This note is the whole of the record\'s response. Nothing is re-verdicted and no closing is '
        'edited: the sites are not repairable, and no verdict among them is wrong. It is filed once, here, so that a reader '
        'knows which arm carried the weight.',
        '',
        '*Its rule\'s other face is filed with the bar-floor rule (TECHNE `BAR_FLOOR_RULE.md`, local). Nothing deposits.*',
        ''])
    io.open(BLOCK, 'w', encoding='utf-8', newline=NL).write(block)
    p = subprocess.run([sys.executable, os.path.join(T, 'b244_loom_append.py'), BLOCK], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    io.open(LOOMRUN, 'w', encoding='utf-8', newline=NL).write(p.stdout + p.stderr)
    print(p.stdout)
    line = ('- **The other face (b447):** a bar that never bites is uninformative rather than lenient, as a bar below its '
            'object\'s floor is uninformative rather than strict. Incidents: **b272**, where a magnitude test alone would '
            'have passed all four of b264\'s floor modes, and **b446**, where the `1.49e-08` floor\'s size decided no banked '
            'verdict (relay `tools/noise_floor.py`, `data/b446_floor_census.txt`).')
    before = io.open(BFR, 'rb').read()
    text = before.decode('utf-8')
    if 'The other face (b447)' in text:
        print('bar-floor line already present')
        return p.returncode
    nl = b'\r\n' if b'\r\n' in before else b'\n'
    new = before.rstrip(b'\r\n') + nl + nl + line.encode('utf-8') + nl
    open(BFR, 'wb').write(new)
    after = open(BFR, 'rb').read()
    print('bar-floor rule: prefix unchanged %s ; lines added %d' % (after.startswith(before.rstrip(b'\r\n')),
                                                                   after.count(b'\n') - before.count(b'\n')))
    return p.returncode


def q(path, needle):
    try:
        ls = io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
    except Exception:
        return None, None
    for i, l in enumerate(ls):
        if needle in l:
            return i + 1, l.strip()
    return None, None


def desk_items():
    items = []
    for b in ['440', '441', '442', '443r', '444', '445', '446']:
        ls = io.open(os.path.join(D, 'b%s_desk_notes.txt' % b), encoding='utf-8').read().splitlines()
        i = 0
        while i < len(ls):
            m = re.match(r'^    (.{60,}?)\s+(STAND|CLOSE)$', ls[i])
            if m:
                txt, j = [], i + 1
                while j < len(ls) and ls[j].startswith('        '):
                    txt.append(ls[j].strip())
                    j += 1
                items.append(dict(act='b' + b, name=m.group(1).strip(), state=m.group(2), text=' '.join(txt)))
                i = j
            else:
                i += 1
    return items


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    a45 = load(os.path.join(D, 'b445_arms.json'))
    a46 = load(os.path.join(D, 'b446_doubling.json'))
    d = load(DBL)
    rec('=' * 100)
    rec('b447 -- THE OUTLIER, THE ARM THAT BITES, AND THE STOCK-TAKE. ### THE COMPONENTS, AFTER THE LOCK, UNDER (R60).')
    rec('=' * 100)

    rec('')
    rec('  ### ### **COMPONENT 1 -- THE THIRD DOUBLING AT a = 4.123106.**')
    lv = [(8193, a45['base'][CELL]['e']), (16385, a45['a'][CELL]['e']), (32769, a46[CELL]['e'])]
    c1 = dict(run=CELL in d)
    if CELL in d:
        lv.append((NV3, d[CELL]['e']))
    rec('    %-8s %-15s %-15s' % ('nv', 'e', 'difference'))
    diffs = []
    for i, (nv, e) in enumerate(lv):
        df = (lv[i - 1][1] - e) if i else None
        if df is not None:
            diffs.append(df)
        rec('    %-8d %+.6e  %s' % (nv, e, ('%+.6e' % df) if df is not None else '-'))
    p1 = math.log2(abs(diffs[0]) / abs(diffs[1]))
    rec('    p1 = log2(|d1| / |d2|) = %.4f   (b446`s, three levels)' % p1)
    outcome = 'NOT RUN'
    if len(diffs) == 3:
        p2 = math.log2(abs(diffs[1]) / abs(diffs[2]))
        rate = math.log2(abs(lv[2][1]) / abs(lv[3][1]))
        shrinks = abs(diffs[2]) < abs(diffs[1])
        conv = (M_OTHERS - 0.5 <= p2 <= M_OTHERS + 0.5) and shrinks
        outcome = 'CONVERGES AT THE OTHERS` RATE' if conv else 'STILL REFUSES'
        rec('    p2 = log2(|d2| / |d3|) = %.4f   (the new order) ; rate log2(|e2| / |e3|) = %.4f' % (p2, rate))
        rec('    rule: p2 in [%.4f, %.4f] : %s ; |d3| < |d2| : %s' % (M_OTHERS - 0.5, M_OTHERS + 0.5,
                                                                  M_OTHERS - 0.5 <= p2 <= M_OTHERS + 0.5, shrinks))
        rec('    |e| at 65537 below 1.49e-08 (the bar quoted outside its kind) : %s' % (abs(lv[3][1]) <= 1.49e-08))
        rec('  ### ### **THE OUTLIER %s.**' % outcome)
        if conv:
            rec('    ### THE REFUSAL WAS THE THREE-LEVEL ESTIMATE`S, PRE-ASYMPTOTIC: the first two differences grew before the')
            rec('    ### error began to shrink at the others` order. THE MEASUREMENT IS CLOSED.')
        else:
            rec('    ### WHAT REMAINS, EACH A CANDIDATE WITH ITS TEST AND PRICE, NOT RUN:')
            rec('    ### (c1) THE INTEGRAND`S OWN BEHAVIOUR AT THAT RADIUS -- a non-smooth point of the autocorrelation at a = sqrt(17).')
            rec('    ###      Test: evaluate the integrand`s one-sided derivatives across its support at this radius and at 4.061553;')
            rec('    ###      a read of existing functions, about a minute. NOT RUN.')
            rec('    ### (c2) THE GRID`S ALIGNMENT WITH A FEATURE OF IT -- a kink falling on or between nodes differently per level.')
            rec('    ###      Test: the same nv with the grid shifted by half a step, at two levels; about four minutes, and it needs')
            rec('    ###      a grid offset the chain does not take as a parameter -- an instrument edit. NOT RUN.')
            rec('    ### (c3) SOMETHING THE RECORD CANNOT SEE -- the residual here is a difference of channels near their own')
            rec('    ###      cancellation, and its error may not be the quadrature`s alone. Test: the channels` own differences')
            rec('    ###      level by level, read from the banked channel values at no cost. NOT RUN.')
            if shrinks and p2 > M_OTHERS + 0.5:
                rec('    ### ### **READ BESIDE THE RULE: IT REFUSES FROM ABOVE.** The last difference shrank %.1f-fold, order %.2f --' % (abs(diffs[1]) / abs(diffs[2]), p2))
                rec('    ### the trapezoid rule`s asymptotic 2 is nearer to it than the window is. The window was built from the other')
                rec('    ### four cells` orders, which b446 itself printed as PRE-ASYMPTOTIC. So the cell`s error shrank once, faster than')
                rec('    ### the window allows; what the rule refuses is the first two levels` growth, which the candidates above address.')
            rec('    ### THE MEASUREMENT STAYS OPEN BY THE RULE because (R60) opened the lane for one doubling and every test above lies past it.')
        c1.update(e=[x[1] for x in lv], nv=[x[0] for x in lv], diffs=diffs, p1=p1, p2=p2, rate=rate, shrinks=shrinks,
                  converges=conv, outcome=outcome)
    else:
        rec('  ### ### **COMPONENT 1 NOT RUN.**')

    # ------------------------------------------------------------------ COMPONENT 2 READ-BACK
    rec('')
    rec('  ### ### **COMPONENT 2 -- THE ARM THAT BITES, NOTED ONCE.**')
    loom_txt = io.open(os.path.join(PP, 'VERIFICATION_LOOM.md'), encoding='utf-8-sig').read()
    run_txt = io.open(LOOMRUN, encoding='utf-8').read() if os.path.exists(LOOMRUN) else ''
    rec('    loom entry markers <!-- b447 loom entry --> : %d' % loom_txt.count('<!-- b447 loom entry -->'))
    rec('    appender : %s' % ('APPENDED, prefix verified' if 'PREFIX UNCHANGED (pure insertion) : YES' in run_txt else '### NOT VERIFIED'))
    bfr = io.open(BFR, encoding='utf-8').read()
    rec('    bar-floor rule line present : %d' % bfr.count('The other face (b447)'))

    # ------------------------------------------------------------------ COMPONENT 3
    rec('')
    rec('  ### ### **COMPONENT 3 -- THE STOCK-TAKE, READ AND NOT PROPOSED.**')
    FND = os.path.join(PP, 'FINDINGS.md')
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    closed = [
        ('the witness arc, complete at six sites with its taxonomy', FND, 'the enumeration completed at six sites, 82 candidates, and a closed taxonomy of 11 failure kinds'),
        ('the archimedean channel`s identification', os.path.join(D, 'b444_closing.txt'), 'The channel was identified as twice the Riemann-Siegel theta'),
        ('its named minimum', os.path.join(D, 'b444_closing.txt'), "its sign change named as theta's minimum on"),
        ('the residual attributed to the chain', os.path.join(D, 'b445_closing.txt'), 'VERDICT, BY THE RULE FIXED ON THE FACE: INTEGRATION'),
        ('the floor understood by kind', os.path.join(D, 'b446_closing.txt'), 'NO DOMAIN OF RADIUS EXISTS'),
    ]
    rec('    CLOSED:')
    closed_out = []
    for name, path, needle in closed:
        n, l = q(path, needle)
        closed_out.append(dict(item=name, file=os.path.basename(path), line=n))
        rec('      %-58s %s' % (name, ('%s:%d | %s' % (os.path.basename(path), n, l[:110])) if n else '### ANCHOR MISSING'))

    items = desk_items()
    pairs = {'site (vi)': ('b443r', 'site (vi) of the witness arc'),
             'whether the residual is the object`s or the quadrature`s': ('b445', 'whose residual it is (b444`s standing item)'),
             'what the grid refinement leaves': ('b446', 'the second doubling at the five cells')}
    alias = {'b363_span.py misses b434`s fold': 'W-ORD-SPAN-HEADING'}
    closes = {(it['act'], it['name']) for it in items if it['state'] == 'CLOSE'}
    latest = {}
    for it in items:
        if it['state'] != 'STAND':
            continue
        nm = alias.get(it['name'], it['name'])
        latest[nm] = dict(it, name=nm)
    desk_open, desk_closed = [], []
    for nm, it in latest.items():
        if nm in pairs:
            ok = pairs[nm] in closes
            (desk_closed if ok else desk_open).append(dict(it, closed_by='%s %s' % pairs[nm] if ok else None))
        elif nm == 'the outlier 4.123106':
            if c1.get('converges'):
                desk_closed.append(dict(it, closed_by='b447 Component 1: CONVERGES'))
            else:
                desk_open.append(dict(it, closed_by=None))
        else:
            desk_open.append(dict(it, closed_by=None))

    def trigger_of(text):
        for pat in (r'trigger\W{0,6}:?\**\s*([^.;]*[.;])', r'(on the next opening[^.;]*[.;])', r'(priced[^.;]*[.;])',
                    r'(the author`s[^.;]*[.;])', r'(routed[^.;]*[.;])'):
            m = re.search(pat, text, re.I)
            if m and m.group(1).strip(' *.;'):
                return m.group(1).strip()
        return 'NO TRIGGER IN THE RECORD`S WORDS'

    def q_last(path, needle):
        ls = io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
        hits = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
        return hits[-1] if hits else (None, None)

    def aim_of(text):
        if re.search(r'(aimed at|reach\w*|points? at)[^.]{0,40}quantifier', text, re.I):
            return 'AIMED'
        if re.search(r'quantifier', text, re.I):
            return 'NAMES'
        return 'NEITHER'

    rec('')
    rec('    CLOSED SINCE THEIR DESK, BY THE DECLARED PAIRS ONLY:')
    for it in desk_closed:
        rec('      %-6s %-58s closed by %s' % (it['act'], it['name'][:58], it['closed_by']))
    rec('')
    rec('    OPEN -- (D) THE DESK, LATEST READING PER NAME:')
    open_out = []
    in_record = {'the fast-radio-burst trail': 'the fast-radio-burst trail', 'W-ORD-SPAN-HEADING': 'W-ORD-SPAN-HEADING (work-order)'}
    dup = [it for it in desk_open if it['name'] in in_record]
    desk_open = [it for it in desk_open if it['name'] not in in_record]
    for it in dup:
        rec('      %-6s %-50s ### PRINTED ONCE, BELOW, AS THE RECORD`S NAMED ITEM "%s"' % (it['act'], it['name'][:50], in_record[it['name']]))
    for it in desk_open:
        trg = trigger_of(it['text'])
        aim = aim_of(it['text'])
        open_out.append(dict(source=it['act'] + ' desk', item=it['name'], trigger=trg, aim=aim))
        rec('      %-6s %-50s aim %-7s | trigger: %s' % (it['act'], it['name'][:50], aim, trg[:120]))

    named = [
        ('W-ORD-SPAN-HEADING (work-order)', FND, '**W-ORD-SPAN-HEADING.**', 'Filed with this fold', None),
        ('W-REMOVAL-VERIFIED (work-order)', FND, '**Its trigger:** the next act that removes a directory', None, None),
        ('the disproof lane', OT, '**Trigger unchanged: the instrument lane opening.**', None, None),
        ('the fast-radio-burst trail', OT, 'fast-radio-burst dispersion measures as an independent baryon-fraction probe.** Trigger:', None, None),
        ('the four lists', OT, 'Trigger: the ruling on which test governs, or any disposition on the four open lists.', None, None),
        ('M-2', FND, '| **`M-2`** | OWED', None, None),
        ('the failure-mode partition', FND, '| **The failure-mode partition** |', None, None),
        ('the uniformity row U1', FND, '| **The uniformity row `U1`** | NAMED-ONLY', None, None),
    ]
    rec('')
    rec('    OPEN -- (R) THE RECORD`S NAMED ITEMS:')
    for name, path, needle, _x, _y in named:
        n, l = q_last(path, needle)
        if not n:
            rec('      %-36s ### ANCHOR MISSING' % name)
            open_out.append(dict(source=os.path.basename(path), item=name, trigger='ANCHOR MISSING', aim='UNCLASSED'))
            continue
        trg = trigger_of(l)
        if name == 'W-ORD-SPAN-HEADING (work-order)':
            n2, l2 = q(os.path.join(D, 'b444_desk_notes.txt'), 'repair on the next opening of the instrument lane or')
            trg = 'repair on the next opening of the instrument lane or the next fold (b444 desk) -- (R58) and (R60) each opened the lane for one purpose only'
        if name == 'the failure-mode partition':
            trg = 'NO TRIGGER IN THE RECORD`S WORDS -- "what would move it": ' + l.split('|')[3].strip()[:90]
        aim = aim_of(l)
        open_out.append(dict(source='%s:%d' % (os.path.basename(path), n), item=name, trigger=trg, aim=aim))
        rec('      %-36s %s:%-5d aim %-7s | trigger: %s' % (name, os.path.basename(path), n, aim, trg[:130]))
    n8, l8 = q(FND, '| **K8** the quantifiers | UNOWNED')
    rec('')
    rec('    THE CLAUSE, APART: FINDINGS.md:%s | %s' % (n8, (l8 or '')[:170]))
    rec('    ### K8 IS THE QUANTIFIER, UNOWNED -- printed as the clause, not as an item aimed at it.')
    n1, _ = q(FND, 'the exhaustion move reaches the quantifier in no branch of that act')
    n2, _ = q(FND, 'No move aimed at the quantifier remains on this board that the span has not tried and priced.')
    rec('    beside the partition: b351 (FINDINGS.md:%s) "the exhaustion move reaches the quantifier in no branch of that act";' % n1)
    rec('    b360`s fold (FINDINGS.md:%s) "No move aimed at the quantifier remains on this board that the span has not tried and priced."' % n2)
    aimed = [o for o in open_out if o['aim'] == 'AIMED']
    rec('')
    rec('  ### ### **OPEN ITEMS AIMED AT THE QUANTIFIER, IN THE RECORD`S OWN WORDS : %d -- %s.**'
        % (len(aimed), ', '.join(o['item'] for o in aimed) or 'none'))
    rec('    open items %d ; AIMED %d ; NAMES %d ; NEITHER %d' % (len(open_out), len(aimed), sum(1 for o in open_out if o['aim'] == 'NAMES'),
                                                             sum(1 for o in open_out if o['aim'] == 'NEITHER')))
    rec('    ### NOTHING IS PROPOSED; THE LIST IS THE PRODUCT.')

    # ------------------------------------------------------------------ EXPECTATIONS
    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1a = ('HELD' if c1.get('converges') else 'REFUTED') + ' -- %s' % c1.get('outcome', 'NOT RUN') if c1.get('run') else 'NOT SCORABLE -- not run'
    n1b = 'REFUTED AS WORDED -- b446`s order used three levels; ' + (
        'the refusal was the three-level estimate`s' if c1.get('converges') else 'and the refusal stands at four levels')
    n2s = ('REFUTED -- %d open item(s) aimed at the quantifier in the record`s words: %s' % (len(aimed), ', '.join(o['item'] for o in aimed))
           if aimed else 'HELD -- no open item aimed at the quantifier')
    rec('    (N1)(a) the outlier converges at the third doubling   ### %s' % n1a)
    rec('    (N1)(b) the refusal was the two-level estimate`s      ### %s' % n1b)
    rec('    (N2)    no open item aimed at the quantifier          ### %s' % n2s)
    rec('    ### the seat`s own from the face: (N1)(a) no expectation; (N1)(b) REFUTED AS WORDED -- %s; (N2) REFUTED -- %s.'
        % ('HELD', 'HELD' if aimed else 'REFUTED'))
    rec('')
    rec('    ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. NOTHING RE-VERDICTED. NO CLOSING EDITED. NOTHING PROPOSED.')
    rec('    ### ### **THE INSTRUMENT LANE OPENED BY (R60) CLOSES AT THIS ACT`S END.** No instrument built; no chain file edited.')
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    J = dict(c1=c1, closed=closed_out, desk_closed=[dict(act=i['act'], item=i['name'], by=i['closed_by']) for i in desk_closed],
             open=open_out, aimed=[o['item'] for o in aimed], expect=dict(n1a=n1a, n1b=n1b, n2=n2s))
    io.open(STK + '.tmp', 'w', encoding='utf-8').write(json.dumps(J, indent=1))
    os.replace(STK + '.tmp', STK)


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'run':
        run()
    elif cmd == 'loom':
        sys.exit(loom())
    else:
        report()
