import os, pickle, sys, collections
SP = os.path.dirname(os.path.abspath(__file__))
R = pickle.load(open(SP + '/inv6_753.pkl', 'rb'))
def wv(r):
    if not r['nsh']:
        return 'TOO SHORT'
    if r['bestcov'] >= 0.9:
        return 'SAME'
    if r['cov'] >= 0.9:
        return 'SAME, OVER SEVERAL LINES'
    if r['cov'] >= 0.5:
        return 'MOST'
    if r['cov'] > 0:
        return 'PART'
    return 'NONE'
def fv(r):
    n, k = len(r['figs']), len(r['fhit'])
    return 'no figure' if not n else '%d/%d' % (k, n)
def loc(r):
    return '%s:%d' % r['best'] if r['best'] else '-'
def floc(r):
    return ', '.join(sorted(set('%s:%d' % v for v in r['fhit'].values())))[:150]
mode = sys.argv[1]
if mode == 'control':
    for r in R:
        if r['bank'] == 'anchors' and r['src'] in ('FINDINGS :821', 'FINDINGS :825'):
            print(r['n'], r['src'], wv(r), '%.2f' % (r['cov'] or 0), loc(r), '| figs', len(r['figs']), 'hit', {k: v for k, v in r['fhit'].items()})
if mode == 'sum':
    for kind in ('sentence/tag', 'slug', 'later line', 'ceiling phrase', 'layer rule', 'other', 'head read', 'cited line'):
        rs = [r for r in R if r['kind'] == kind]
        c = collections.Counter(wv(r) for r in rs)
        f = collections.Counter('no figure' if not r['figs'] else ('all figures found' if len(r['fhit']) == len(r['figs']) else ('some' if r['fhit'] else 'no figure found')) for r in rs)
        print('%-15s %4d | words %s | figures %s' % (kind, len(rs), dict(c), dict(f)))
    # anchors as units: sentence row = first sentence/tag row after slug
    by = collections.OrderedDict()
    for r in R:
        if r['bank'] == 'anchors' and r['anchor'] and r['kind'] in ('sentence/tag',):
            by.setdefault(r['anchor'], []).append(r)
    cls = collections.Counter()
    for a, rs in by.items():
        s = rs[0]
        w = wv(s)
        allf = bool(s['figs']) and len(s['fhit']) == len(s['figs'])
        cls[('words ' + ('SAME' if w.startswith('SAME') else w)) + ' ; ' + ('no figure' if not s['figs'] else 'all figures found' if allf else 'some figures found' if s['fhit'] else 'no figure found')] += 1
    print('ANCHORS BY SENTENCE ROW', len(by))
    for k, v in sorted(cls.items()):
        print('  %3d  %s' % (v, k))
if mode == 'anchors':
    for r in R:
        if r['bank'] == 'anchors' and r['kind'] != 'slug':
            print('%d|%s|%s|%s %.0f%%|%s|%s|%s' % (r['n'], r['kind'][:8], r['src'].replace('FINDINGS ', 'F').replace('REGISTRY ', 'R').replace('ERRATA ', 'E')[:10], wv(r)[:4], 100 * (r['cov'] or 0), loc(r).replace('data/', '')[:60], fv(r), floc(r).replace('data/', '')[:90]))
if mode == 'slugs':
    c = collections.Counter()
    for r in R:
        if r['kind'] == 'slug':
            c[wv(r)] += 1
    print(dict(c))
if mode == 'rest':
    for r in R:
        if r['bank'] != 'anchors':
            print('%s:%d|%s|%s %.0f%%|%s|%s|%s' % (r['bank'], r['n'], r['src'], wv(r), 100 * (r['cov'] or 0), loc(r), fv(r), floc(r)))
            if r['bank'] == 'head_read':
                print('     figs', r['figs'], r['fhit'])
