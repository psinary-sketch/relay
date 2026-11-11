import os, pickle, sys, collections
SP = os.path.dirname(os.path.abspath(__file__))
R = pickle.load(open(SP + '/inv6_753.pkl', 'rb'))
rf, hit = None, collections.defaultdict(dict)
for k in range(3):
    a, h = pickle.load(open(SP + '/inv8_753_%d.pkl' % k, 'rb'))
    rf = a
    for i, d in h.items():
        for f, v in d.items():
            hit[i].setdefault(f, v)
for i, r in enumerate(R):
    r['figs'], r['fhit'] = rf[i], hit.get(i, {})
def wv(r):
    if not r['nsh']:
        return 'SHORT'
    if r['bestcov'] >= 0.9:
        return 'SAME'
    if r['cov'] >= 0.9:
        return 'SAME*'
    if r['cov'] >= 0.5:
        return 'MOST'
    return 'PART' if r['cov'] > 0 else 'NONE'
def fv(r):
    return '-' if not r['figs'] else '%d/%d' % (len(r['fhit']), len(r['figs']))
def sh(p):
    return p.replace('data/', '')
def loc(r):
    return sh('%s:%d' % r['best']) if r['best'] else '-'
def floc(r, n=2):
    # prefer a formula hit over a bare number
    ks = sorted(r['fhit'], key=lambda f: (f[0] != 'X', -len(f)))
    return ', '.join(sh('%s:%d' % r['fhit'][f]) for f in ks[:n]) if ks else '-'
def cls(r):
    w = wv(r)
    if w in ('SAME', 'SAME*'):
        return 'A words stand'
    if r['figs'] and len(r['fhit']) == len(r['figs']):
        return 'B every figure stands, words differ'
    if r['fhit']:
        return 'C some figures stand'
    if r['figs']:
        return 'D figure not found'
    return 'E no figure; words %s' % ('mostly found' if w == 'MOST' else 'not found as a run')
mode = sys.argv[1]
if mode == 'control':
    for r in R:
        if r['src'] in ('FINDINGS :821', 'FINDINGS :825') and r['bank'] == 'anchors':
            print(r['src'], wv(r), loc(r), fv(r), {f: v for f, v in r['fhit'].items()})
if mode == 'anchors':
    by = collections.OrderedDict()
    for r in R:
        if r['bank'] == 'anchors' and r['anchor'] and r['kind'] == 'sentence/tag':
            by.setdefault(r['anchor'], []).append(r)
    c = collections.Counter()
    for a, rs in by.items():
        s, t = rs[0], rs[1] if len(rs) > 1 else None
        c[cls(s)] += 1
        print('%d|%s|%s %d%%|%s|%s|%s|%s' % (s['n'], s['src'].replace('FINDINGS ', ''), wv(s), 100 * (s['cov'] or 0), loc(s), fv(s), floc(s), cls(s)[:1]))
    for k, v in sorted(c.items()):
        print('%3d %s' % (v, k))
    ct = collections.Counter()
    for a, rs in by.items():
        if len(rs) > 1:
            ct[wv(rs[1])] += 1
    print('tag rows, words:', dict(ct))
if mode == 'others':
    for r in R:
        if r['bank'] == 'anchors' and r['kind'] in ('later line', 'layer rule', 'ceiling phrase', 'other'):
            print('%d|%s|%s|%s %d%%|%s|%s|%s' % (r['n'], r['kind'], r['src'], wv(r), 100 * (r['cov'] or 0), loc(r), fv(r), floc(r)))
    c = collections.Counter(wv(r) for r in R if r['kind'] == 'slug')
    print('slugs', dict(c))
    for r in R:
        if r['bank'] != 'anchors' and r['figs']:
            print('%s:%d|%s|%s|%s|%s' % (r['bank'], r['n'], r['src'], wv(r), fv(r), floc(r)))
