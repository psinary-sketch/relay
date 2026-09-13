# -*- coding: utf-8 -*-
"""b448_components.py -- THE PARTITION READ AGAINST THE TAXONOMY, AND THE OUTLIER'S FREE CANDIDATE. ### **AFTER THE LOCK.**

### Usage: `techne` -- Component 3's one line appended to `BAR_FLOOR_RULE.md`, the prior bytes proved a prefix;
### `report` -- Components 1, 2 and 3 into `data/b448_components.txt`, `data/b448_partition.json`, `data/b448_channels.json`.
### ### **NO CHAIN IS RUN.** Every figure is a banked value re-read here; every rule is the locked face's.
"""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b448_components.txt')
PJ = os.path.join(D, 'b448_partition.json')
CJ = os.path.join(D, 'b448_channels.json')
TRUN = os.path.join(D, 'b448_techne_append_run.txt')
BFR = os.path.join(TE, 'modules', '2026-09', 'BAR_FLOOR_RULE.md')
CELL = '4.123106'
NL = chr(10)

SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
COORDS = [('abscissa', 'beta'), ('height', 'gamma'), ('phase', 'phi'), ('width', 'a')]
STATES = ('BOUNDED BY AN ARGUMENT', 'BOUNDED BY A MEASUREMENT', 'NOT BOUNDED')

LINE = ('- **The window\'s upper bound (b448):** a convergence window carries no upper bound below the method\'s '
        'asymptotic order, and an order above it is reported as SUPER-CONVERGENT and not as refusal. Incident: **b447**, '
        'where the outlier `a = 4.123106`\'s order `2.43` was read as refusal against a window whose upper edge, `1.95`, '
        'was set from other cells\' pre-asymptotic orders, beside the trapezoid rule\'s asymptotic `2` (relay '
        '`data/b447_components.txt`, `data/b446_components.txt`). The author\'s correction; b447\'s bank is unedited.')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def lines_of(path):
    try:
        return io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
    except Exception:
        return []


def q(path, needle):
    for i, l in enumerate(lines_of(path)):
        if needle in l:
            return i + 1, l.strip()
    return None, None


def techne():
    before = open(BFR, 'rb').read()
    out = []
    if b"The window's upper bound (b448)" in before:
        out.append('the b448 line is already present; nothing appended')
    else:
        nl = b'\r\n' if b'\r\n' in before else b'\n'
        new = before.rstrip(b'\r\n') + nl + nl + LINE.encode('utf-8') + nl
        open(BFR + '.tmp', 'wb').write(new)
        os.replace(BFR + '.tmp', BFR)
        after = open(BFR, 'rb').read()
        prefix = after.startswith(before.rstrip(b'\r\n'))
        added = [x for x in after[len(before.rstrip(b'\r\n')):].split(b'\n') if x.strip()]
        out.append('BAR_FLOOR_RULE.md : PRIOR BYTES A TRUE PREFIX : %s' % ('YES' if prefix else 'NO'))
        out.append('non-empty lines added : %d' % len(added))
        out.append('bytes before %d ; after %d' % (len(before), len(after)))
    io.open(TRUN, 'w', encoding='utf-8', newline=NL).write(NL.join(out) + NL)
    print(NL.join(out))
    return 0


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    misses = []

    def anchor(label, path, needle):
        n, t = q(path, needle)
        if n is None:
            misses.append(label)
            rec('      ### ANCHOR MISSING : %s' % label)
        else:
            rec('      %-26s %s:%d | %s' % (label, os.path.basename(path), n, t[:120]))
        return n, t

    rec('=' * 100)
    rec('b448 -- THE PARTITION READ AGAINST THE TAXONOMY, AND THE OUTLIER`S FREE CANDIDATE. ### THE COMPONENTS, AFTER THE LOCK.')
    rec('=' * 100)

    # ------------------------------------------------------------------ COMPONENT 1
    rec('')
    rec('  ### ### **COMPONENT 1 -- THE PARTITION READ AGAINST THE TAXONOMY.**')
    FND = os.path.join(PP, 'FINDINGS.md')
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    R351 = os.path.join(D, 'b351_registration_2026-09-07.txt')
    RUN351 = os.path.join(D, 'b351_read_run.txt')
    DR = os.path.join(D, 'b443r_u1_draft.md')
    rec('    THE ANCHORS, RE-READ:')
    anchor('partition (b348)', FND, 'a finite classification of the ways the margin could fail, over the aim plane')
    n40, t40 = anchor('partition element (b351)', R351, "and it FAILS at an aim when that room is not")
    anchor('partition classes (b351)', RUN351, 'finitely many classes C1..Ck such that every aim with gamma > T0 lies in one of them')
    n79, t79 = anchor('branch rule (b351)', R351, 'An absence of a bound is NOT an obstruction')
    n5223, t5223 = anchor('arc element (b423)', OT, 'enumerate every candidate shared witness for the site')
    anchor('arc taxonomy (b444)', FND, 'a closed taxonomy of 11 failure kinds')
    anchor('taxonomy table (b443r)', DR, '| kind | (i) | (ii) | (iii) | (iv) | (v) | (vi) | total |')
    anchor('distinction one (b351)', R351, 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.')
    anchor('distinction two (b351)', R351, 'A METHOD THAT PRODUCES INSTANCES DOES')
    anchor('no failure found (b351)', R351, 'NO ACT OF THE RECORD HAS EVER FOUND ONE')

    # ### the draft's table and site rows
    dlines = lines_of(DR)
    table = {}
    for l in dlines:
        m = re.match(r'^\| ([A-Z][A-Z -]+[A-Z]) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', l)
        if m:
            table[m.group(1)] = dict(zip([s for s, _ in SITES], [int(x) for x in m.group(2, 3, 4, 5, 6, 7)]))
    kinds = list(table.keys())
    rows = {}
    for l in dlines:
        m = re.match(r'^\| \*\*\((i|ii|iii|iv|v|vi)\)\*\* ([^|]+)\| [^|]+\| ([^|]+)\|', l)
        if m:
            rows[m.group(1)] = dict(name=m.group(2).strip(), missing=m.group(3).strip())

    # ### the banks, re-counted, so the table is not trusted because a draft printed it
    bank = {s: {} for s, _ in SITES}
    held, cite, nb = 0, [], 0
    for s, p in SITES:
        d = load(p)
        for c in d['candidates']:
            nb += 1
            bank[s][c['kind']] = bank[s].get(c['kind'], 0) + 1
            if 'b351' in json.dumps(c, ensure_ascii=False):
                cite.append(dict(site=s, id=c['id'], kind=c['kind'], name=c['name']))
        h = d.get('held')
        held += (len(h) if isinstance(h, list) else int(h or 0))
    table_eq_banks = all(bank[s].get(k, 0) == table[k][s] for k in kinds for s, _ in SITES) and \
        all(k in table for s, _ in SITES for k in bank[s])
    rec('    the draft`s table : %d kinds, %d candidates ; the banks re-counted : %d candidates, held %d ; table equals banks : %s'
        % (len(kinds), sum(sum(v.values()) for v in table.values()), nb, held, table_eq_banks))

    # ### THE ELEMENT TEST
    arc_thing = 'candidate' if (t5223 and 'candidate' in t5223) else None
    arc_place = 'a quoted step' if (t5223 and 'fail each at a quoted step' in t5223) else None
    par_thing = 'the margin' if (t40 and 'room' in t40) else None
    par_place = 'an aim' if (t40 and 'FAILS at an aim' in t40) else None
    one_kind = bool(par_thing and arc_thing) and (par_thing == arc_thing and par_place == arc_place)
    rec('')
    rec('    THE ELEMENT TEST (face, reading (1)):')
    rec('      the partition : what fails = %s (the room `places = prime - arch`) ; where = %s ; classes = sets of aims' % (par_thing, par_place))
    rec('      the arc       : what fails = a %s shared witness ; where = %s ; a kind = the reason at the first failing step' % (arc_thing, arc_place))
    rec('      ### OF ONE KIND : %s' % one_kind)

    # ### THE BRANCH TEST
    obstruction = [k for k in kinds if 'OBSTRUCTION' in k]
    branch_met = held > 0 or bool(obstruction)
    rec('')
    rec('    THE BRANCH TEST (b351`s section (D), its line %s):' % n79)
    rec('      candidates held across the six sites : %d ; kinds naming an obstruction : %d' % (held, len(obstruction)))
    rec('      (A SHAPE EXISTS) supplied : %s ; (NO FINITE PARTITION) supplied : %s -- an exhausted list is an absence'
        % (held > 0, bool(obstruction)))
    rec('      ### BRANCH TEST MET : %s' % branch_met)

    # ### THE LINKS
    assign = {}
    for word, _sym in COORDS:
        assign[word] = [s for s, _ in SITES if s in rows and re.search(r'\b%s\b' % word, rows[s]['missing'])]
    l1 = sum(len(v) for v in assign.values())
    l2k = [k for k in kinds if k in STATES]
    l3 = len(cite)
    rec('')
    rec('    THE LINKS, COUNTED APART:')
    for word, _sym in COORDS:
        rec('      (L1) %-9s sites whose missing statement names it : %s' % (word, ['(%s) %s' % (s, rows[s]['missing'][:60]) for s in assign[word]] or 'NONE'))
    rec('      (L1) total %d ; (L2) kinds named verbatim as a b351 state : %d %s ; (L3) candidates carrying `b351` : %d'
        % (l1, len(l2k), l2k, l3))
    for c in cite:
        rec('           (%s) %-4s %-26s %s' % (c['site'], c['id'], c['kind'], c['name'][:70]))
    links = l1 + len(l2k) + l3
    verdict = 'SAME' if (one_kind and branch_met) else ('RELATED' if links >= 1 else 'DIFFERENT')
    rec('')
    rec('  ### ### **COMPONENT 1 VERDICT, BY THE FACE`S RULE : %s.**' % verdict)
    rec('    ### elements of one kind %s ; branch test met %s ; links L1 %d + L2 %d + L3 %d = %d.' % (one_kind, branch_met, l1, len(l2k), l3, links))

    # ### THE TABLE
    st351 = {}
    for sym in ('beta', 'gamma', 'phi', 'a'):
        n, t = q(RUN351, '      %s ' % sym if sym != 'a' else '      a      ')
        st351[sym] = (n, t)
    rec('')
    rec('    THE TABLE -- THE PARTITION`S FOUR COORDINATES AGAINST THE ARC`S ELEVEN KINDS (cells: banked candidates of the kind')
    rec('    at the sites (L1) assigns to the coordinate).')
    abbrev = {k: 'K%d' % (i + 1) for i, k in enumerate(kinds)}
    hdr = '      %-9s %-26s %-10s' % ('coord', 'b351 state', 'sites') + ''.join('%5s' % abbrev[k] for k in kinds) + '  total'
    rec(hdr)
    tab = {}
    for word, sym in COORDS:
        n, t = st351[sym]
        state = next((s for s in STATES if t and t.endswith(s)), 'ANCHOR MISSING')
        if state == 'ANCHOR MISSING':
            misses.append('b351 state ' + sym)
        cells = [sum(table[k][s] for s in assign[word]) for k in kinds]
        tab[word] = dict(symbol=sym, b351_state=state, b351_line=n, sites=assign[word], cells=dict(zip(kinds, cells)), total=sum(cells))
        rec('      %-9s %-26s %-10s' % (word, state, ','.join(assign[word]) or '-') + ''.join('%5d' % c for c in cells) + '  %5d' % sum(cells))
    rec('      key : ' + ' ; '.join('%s = %s' % (abbrev[k], k) for k in kinds))
    rec('      b351`s states read at b351_read_run.txt:%s-%s ; sites not assigned to any coordinate : %s'
        % (st351['beta'][0], st351['a'][0], [s for s, _ in SITES if not any(s in v for v in assign.values())]))

    gives = [
        ('VOCABULARY', 'one kind is b351`s own state, verbatim -- %s, %d candidates -- and two more restate its two distinctions: '
         'INSTRUMENT DOES NOT REACH (face line 60, "A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE") and INSTANCES '
         'NOT A CLASS (face line 65, "A METHOD THAT PRODUCES INSTANCES DOES NOT PRODUCE A CLASSIFICATION")'
         % (', '.join(l2k), sum(sum(table[k].values()) for k in l2k))),
        ('AN EXHAUSTED SEARCH AT TWO COORDINATES', 'at the height (%d candidates) and the width (%d), every candidate for a '
         'statement of the kind b351 typed as missing -- (M-gamma), (M-a) -- failed at a quoted step'
         % (tab['height']['total'], tab['width']['total'])),
        ('CITATION', '%d candidates carry b351 in their banked record' % l3),
    ]
    gives_not = [
        ('A CLASS OF AIMS', 'its elements are candidates, not aims (the element test: %s)' % one_kind),
        ('EITHER BRANCH', '%d held and no obstruction; by b351`s line %s an absence is not an obstruction, so UNDECIDED stands' % (held, n79)),
        ('THE ABSCISSA OR THE PHASE', 'no site`s missing statement names either (rows total %d and %d); b351`s states stand there as b351 left them'
         % (tab['abscissa']['total'], tab['phase']['total'])),
        ('THE MARGIN`S FAILURE', 'no candidate is classed by where the margin fails, and b351`s face says no act has ever found one'),
    ]
    rec('')
    rec('    WHAT THE ARC GIVES THE PARTITION:')
    for h, t in gives:
        rec('      + %s -- %s.' % (h, t))
    rec('    WHAT IT DOES NOT:')
    for h, t in gives_not:
        rec('      - %s -- %s.' % (h, t))
    item_state = {'RELATED': 'OPEN, TRIGGER STATE UNCHANGED (NO TRIGGER IN THE RECORD`S WORDS); NOT CLOSED, RESTATED OR SHELVED',
                  'SAME': 'CLOSURE OR RESTATEMENT ROUTED, NOT WRITTEN',
                  'DIFFERENT': 'TRIGGER OR SHELVED (R23) ROUTED, NOT WRITTEN'}[verdict]
    rec('  ### ### **THE ITEM : %s.**' % item_state)
    rec('    ### NO BRIDGE TYPED. ### ROW U1`S REFUSAL GOVERNS.')

    # ------------------------------------------------------------------ COMPONENT 2
    rec('')
    rec('  ### ### **COMPONENT 2 -- THE OUTLIER`S FREE CANDIDATE (c3), THE CHANNELS AT a = 4.123106.**')
    a45 = load('b445_arms.json')
    lv = [a45['base'][CELL], a45['a'][CELL], load('b446_doubling.json')[CELL], load('b447_doubling.json')[CELL]]
    CH = [('zero', 'Z', +1), ('pole', 'P', -1), ('prime', 'PR', +1), ('arch', 'A', -1)]
    recon = max(abs(r['zero'] - (r['pole'] - r['prime'] + r['arch']) - r['e']) for r in lv)
    rec('    e reconstructed as Z - (P - PR + A) at all four levels, max |difference| %.2e : %s' % (recon, recon < 1e-15))
    rec('    %-7s %-24s %-24s %-24s %-11s %-15s' % ('nv', 'Z (zero)', 'A (arch)', 'PR (prime)', 'P (pole)', 'e'))
    for r in lv:
        rec('    %-7d %.16e  %.16e  %.16e  %+.2e  %+.6e' % (r['nv'], r['zero'], r['arch'], r['prime'], r['pole'], r['e']))
    steps = []
    rec('')
    rec('    CHANGE PER LEVEL, AND EACH CHANNEL`S SIGNED CONTRIBUTION TO THE CHANGE OF e:')
    rec('    %-15s %-12s %-12s %-12s %-12s | %-11s %-11s %-11s %-11s | %-11s %-8s %-6s %s'
        % ('step', 'dZ', 'dA', 'dPR', 'dP', '+dZ', '-dA', '+dPR', '-dP', 'de', 'share', 'gross/', 'class'))
    for j in (1, 2, 3):
        a, b = lv[j - 1], lv[j]
        dch = {k: b[k] - a[k] for k, _s, _g in CH}
        contrib = {k: g * dch[k] for k, _s, g in CH}
        de = b['e'] - a['e']
        gross = sum(abs(v) for v in contrib.values())
        top = max(contrib, key=lambda k: abs(contrib[k]))
        share = abs(contrib[top]) / gross
        ratio = gross / abs(de)
        if share >= 0.9:
            cls, pair = 'ONE CHANNEL`S', [top]
        elif gross > 2 * abs(de):
            srt = sorted(contrib, key=lambda k: -abs(contrib[k]))
            pos = [k for k in srt if contrib[k] > 0][:1]
            neg = [k for k in srt if contrib[k] < 0][:1]
            cls, pair = 'CANCELLATION', pos + neg
        else:
            cls, pair = 'MIXED', []
        sumchk = abs(sum(contrib.values()) - de)
        steps.append(dict(step='%d->%d' % (a['nv'], b['nv']), d=dch, contrib=contrib, de=de, gross=gross, share=share,
                          top=top, ratio=ratio, cls=cls, pair=pair, sumchk=sumchk))
        rec('    %-15s %+.4e %+.4e %+.4e %+.2e | %+.3e %+.3e %+.3e %+.1e | %+.3e %.6f %.4f %s (%s)'
            % ('%d->%d' % (a['nv'], b['nv']), dch['zero'], dch['arch'], dch['prime'], dch['pole'], contrib['zero'],
               contrib['arch'], contrib['prime'], contrib['pole'], de, share, ratio, cls, ', '.join(pair)))
    rec('    contributions sum to de at every step, max |difference| %.2e' % max(s['sumchk'] for s in steps))
    rec('    each channel`s own |change| per step:')
    for k, sym, _g in CH:
        mags = [abs(s['d'][k]) for s in steps]
        ords = ['%.2f' % math.log2(mags[i] / mags[i + 1]) if mags[i + 1] else '-' for i in (0, 1)]
        rec('      %-6s %-3s %s ; orders log2(|d1|/|d2|), log2(|d2|/|d3|) : %s' % (k, sym, ['%.3e' % m for m in mags], ords))
    s1, s2 = steps[0], steps[1]
    if s1['cls'] == s2['cls'] == 'ONE CHANNEL`S' and s1['top'] == s2['top'] and abs(s2['d'][s1['top']]) > abs(s1['d'][s1['top']]):
        growth, gchan = 'ONE CHANNEL`S', s1['top']
    elif 'CANCELLATION' in (s1['cls'], s2['cls']):
        growth, gchan = 'CANCELLATION', ', '.join(s1['pair'] if s1['cls'] == 'CANCELLATION' else s2['pair'])
    else:
        growth, gchan = 'MIXED', ''
    rec('    the growth: |de| step 1 %.3e -> step 2 %.3e (grows : %s)' % (abs(s1['de']), abs(s2['de']), abs(s2['de']) > abs(s1['de'])))
    rec('  ### ### **THE GROWTH BETWEEN THE FIRST TWO LEVELS, BY THE FACE`S RULE : %s -- %s.**' % (growth, gchan.upper() or 'NO CHANNEL'))
    if growth == 'ONE CHANNEL`S':
        mstate = 'STAYS OPEN, NARROWED TO THE %s CHANNEL' % gchan.upper()
        c3 = 'REFUTED'
        rec('    ### (c3), the channels cancelling : REFUTED -- the change of e at each of the first two steps is the %s channel`s,' % gchan)
        rec('    ### and that channel`s own change grows between them while the zero and arch channels` shrink; the pole`s')
        rec('    ### changes sit at the rounding level of the channels, near 1e-17, eight decades below every de compared.')
        rec('    ### READ BESIDE THE RULE: the %s channel is evaluated by linear interpolation of the autocorrelation at fixed points' % gchan)
        rec('    ### (b321_window.py:118), not by the trapezoid rule; the record states no asymptotic order for that evaluation.')
        rec('    ### (c1) the integrand at sqrt(17), about a minute, and (c2) the grid`s alignment with a kink, an instrument edit,')
        rec('    ### stay PRICED AND NOT RUN; both instrument lanes are parked.')
    elif growth == 'CANCELLATION':
        mstate, c3 = 'CLOSES', 'HELD'
    else:
        mstate, c3 = 'STAYS OPEN, UNNARROWED', 'NOT DECIDED'
    rec('  ### ### **THE MEASUREMENT %s.**' % mstate)

    # ------------------------------------------------------------------ COMPONENT 3
    rec('')
    rec('  ### ### **COMPONENT 3 -- THE CONVERGENCE WINDOW`S UPPER BOUND.**')
    e = [r['e'] for r in lv]
    dd = [e[i - 1] - e[i] for i in (1, 2, 3)]
    p1 = math.log2(abs(dd[0]) / abs(dd[1]))
    p2 = math.log2(abs(dd[1]) / abs(dd[2]))
    shrink = abs(dd[2]) < abs(dd[1])
    lo, hi_old, asym = 0.9465, 1.9465, 2.0
    hi = max(hi_old, asym)
    old = 'CONVERGES' if (lo <= p2 <= hi_old and shrink) else 'REFUSES'
    if shrink and lo <= p2 <= hi:
        new = 'CONVERGES'
    elif shrink and p2 > hi:
        new = 'SUPER-CONVERGENT'
    else:
        new = 'REFUSES'
    tl = [l for l in lines_of(BFR) if l.startswith("- **The window's upper bound (b448):**")]
    rec('    the line in BAR_FLOOR_RULE.md : %d present' % len(tl))
    rec('    p1 %.4f ; p2 %.4f (re-taken from the banks) ; |d3| < |d2| : %s' % (p1, p2, shrink))
    rec('    b447`s rule   : p2 in [%.4f, %.4f] -> %s' % (lo, hi_old, old))
    rec('    corrected rule: p2 in [%.4f, %.4f] -> CONVERGES ; p2 > %.4f -> SUPER-CONVERGENT ; the asymptotic 2 in the record`s words' % (lo, hi, hi))
    rec('  ### ### **THE OUTLIER UNDER THE CORRECTED RULE : %s.**' % new)
    rec('    ### b447`s bank reads REFUSES and is not edited; the corrected rule reads its last order, and Component 2 reads its first two.')

    # ------------------------------------------------------------------ EXPECTATIONS
    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1 = 'HELD' if verdict == 'RELATED' else 'REFUTED'
    n2a = 'HELD' if (growth == 'CANCELLATION' and set(gchan.split(', ')) == {'arch', 'prime'}) else 'REFUTED'
    n2b = 'HELD' if mstate == 'CLOSES' else 'REFUTED'
    rec('    (N1)    RELATED, vocabulary and not answer              ### %s -- %s; the arc gives the vocabulary and an exhausted search, not a branch' % (n1, verdict))
    rec('    (N2)(a) a cancellation between arch and prime           ### %s -- %s (%s)' % (n2a, growth, gchan))
    rec('    (N2)(b) the measurement closes                          ### %s -- %s' % (n2b, mstate))
    seat = dict(n1='HELD', n2a='REFUTED', n2b='REFUTED')
    rec('    ### the seat`s own from the face, taken with its inputs seen: (N1) %s -- %s; (N2)(a) %s -- %s; (N2)(b) %s -- %s.'
        % (seat['n1'], 'HELD' if seat['n1'] == n1 else 'REFUTED', seat['n2a'], 'HELD' if seat['n2a'] == n2a else 'REFUTED',
           seat['n2b'], 'HELD' if seat['n2b'] == n2b else 'REFUTED'))
    rec('')
    rec('    ### MISSES : %d %s' % (len(misses), misses or ''))
    rec('    ### NO CHAIN RUN. ### NO BRIDGE TYPED. ### NO CLOSING EDITED. ### NOTHING RE-VERDICTED IN ITS OWN BANK.')
    rec('    ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. ### THE FOUR LISTS ARE OPEN.')
    rec('=' * 100)

    json.dump(dict(verdict=verdict, one_kind=one_kind, branch_met=branch_met, held=held, l1=l1, l2=l2k, l3=l3, cite=cite,
                   assign=assign, table=tab, kinds=kinds, table_eq_banks=table_eq_banks, gives=gives, gives_not=gives_not,
                   item_state=item_state, misses=misses,
                   expect=dict(n1=n1, n2a=n2a, n2b=n2b), seat=seat),
              io.open(PJ + '.tmp', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    os.replace(PJ + '.tmp', PJ)
    json.dump(dict(levels=lv, recon=recon, steps=steps, growth=growth, channel=gchan, measurement=mstate, c3=c3,
                   p1=p1, p2=p2, shrink=shrink, old=old, new=new, hi=hi, line_present=len(tl)),
              io.open(CJ + '.tmp', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    os.replace(CJ + '.tmp', CJ)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if not misses else 2


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    sys.exit(techne() if mode == 'techne' else report())
