import io, re, collections
L = io.open('D:/relay/data/b753_anchors.txt', encoding='utf-8').read().split('\n')
mask = lambda s: re.sub(r'"[^"]{12,}"?|\*[^*]{6,}\*', lambda m: '<%d>' % len(m.group(0)), s)
cat = collections.OrderedDict()
def put(k, i):
    cat.setdefault(k, []).append(i)
sec = None
for i, l in enumerate(L, 1):
    if l.startswith('## '):
        sec = l[:40]
    s = l.strip()
    if not s:
        continue
    if re.match(r'^[a-zA-Z0-9-]+ \(:\d+, I+\) \|', s):
        put('anchor row: the slug (a heading of FINDINGS) with its line, section and verdict', i)
    elif re.match(r'^:\d+ "', s) and sec and 'THE ANCHORS' in sec:
        put('quoted sentence or tag of an anchor (FINDINGS :762-:1083)', i)
    elif s.startswith('MOVED BY FINDINGS'):
        put('quoted later line of FINDINGS', i)
    elif s.startswith('MOVED BY REGISTRY'):
        put('quoted later line of REGISTRY', i)
    elif s.startswith('MOVED BY ERRATA'):
        put('quoted later line of ERRATA', i)
    elif re.match(r'^REGISTRY :\d+ \*', s):
        put('quoted phrase of REGISTRY`s ceiling block', i)
    elif '"' in s or '*' in s:
        put('other line with a quoted run (%s)' % (sec or 'head')[:30], i)
tot = 0
for k, v in cat.items():
    tot += len(v)
    print('%4d  %s ; bank lines %s' % (len(v), k, (', '.join(':%d' % x for x in v[:6]) + (' ... :%d' % v[-1] if len(v) > 6 else ''))))
print('total', tot, 'of', len(L), 'lines')
for i in list(range(84, 92)) + cat.get('other line with a quoted run (## THE CONTROLS, printed befor)', [])[:0]:
    print(':%d %s' % (i, mask(L[i - 1])[:230]))
for k, v in cat.items():
    if k.startswith('other'):
        for i in v:
            print('OTHER :%d %s' % (i, mask(L[i - 1])[:200]))
