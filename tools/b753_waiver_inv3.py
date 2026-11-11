import io, os, re, json, pickle, sys, collections
REL = 'D:/relay'
SP = os.path.dirname(os.path.abspath(__file__))
PRIV = ['PLACE-papers', 'TECHNE-Core', 'PLACE-phase1.5', 'PLACE-phase2', 'SIDE-carrier-spec', 'SIDE-spinor-calibration-mathlib', 'SIDE-constants', 'glassbead-game']
mode = sys.argv[1]
if mode == 'head':
    j = json.load(io.open(REL + '/data/b753_head_read.json', encoding='utf-8'))
    for n in PRIV:
        d = j['descriptions'].get(n)
        print('JSON descriptions[%s] = %r' % (n, d))
    for k in ('returned', 'recomposed'):
        v = j.get(k)
        print('JSON', k, type(v).__name__, (list(v.keys())[:6] if isinstance(v, dict) else str(v)[:200]))
    rd = j.get('returned') if isinstance(j.get('returned'), dict) else {}
    for n in PRIV:
        for k, v in j.items():
            if isinstance(v, dict) and n in v and k != 'descriptions':
                print('JSON %s[%s] = %s' % (k, n, json.dumps(v[n], ensure_ascii=False)[:900]))
    L = io.open(REL + '/data/b753_head_read.txt', encoding='utf-8').read().split('\n')
    for i, l in enumerate(L, 1):
        if any(n in l for n in PRIV) or 'private' in l.lower() or 'PRIVATE' in l:
            print('TXT :%d [%d] %s' % (i, len(l), l[:1500]))
            for k in range(i, min(i + 6, len(L))):   # continuation lines of the row
                if L[k].startswith('      ') or L[k].startswith('    '):
                    print('TXT :%d   %s' % (k + 1, L[k][:1500]))
                else:
                    break
elif mode == 'anchors':
    L = io.open(REL + '/data/b753_anchors.txt', encoding='utf-8').read().split('\n')
    kinds = collections.Counter()
    for i, l in enumerate(L, 1):
        if '"' in l:
            q = re.findall(r'"([^"]{12,})"', l)
            if q:
                key = re.sub(r'[a-z0-9-]+ \(:\d+', 'SLUG (:N', l.strip()[:40])
                kinds[re.sub(r'\d+', 'N', l.strip()[:22])] += 1
    print('lines', len(L))
    for k, v in kinds.most_common(30):
        print('%5d  %s' % (v, k))
    for i in (60, 61, 62, 63, 64, 65, 66, 67, 68):
        print(':%d [%d] %s' % (i, len(L[i - 1]), re.sub(r'"[^"]{12,}"', lambda m: '"<%d chars>"' % len(m.group(0)), L[i - 1])[:260]))
else:
    res = pickle.load(open(SP + '/inv2_753.pkl', 'rb'))
    skip = ('data/b753_anchors.txt',)
    for path in sorted(res):
        if path in skip:
            continue
        for cls in ('NEW, CITES A PRIVATE FILE', 'NEW, CITES NONE', 'UNLOCATED'):
            for text, v in res[path].get(cls, []):
                c, n, src = v[0]
                print('%s :%d [%s] %s | SRC %s:%s:%d "%s"' % (path.replace('data/b753_', '').replace('tools/', 't/'), n, cls[:8], ' '.join(text.split())[:170], src[0][:6], src[1][-28:], src[2], src[3]))
