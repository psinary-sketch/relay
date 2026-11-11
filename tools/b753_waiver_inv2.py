"""inventory, second pass: set apart (A) rows the same path already held at origin/main, (B) words the pushed relay already carries anywhere."""
import io, os, re, subprocess, sys, collections, pickle
REL = 'D:/relay'
SP = os.path.dirname(os.path.abspath(__file__))
flag = pickle.load(open(SP + '/inv1_753.pkl', 'rb'))
def g(*a, **k):
    r = subprocess.run(['git', '-C', REL] + list(a), capture_output=True, **k)
    return r.stdout.decode('utf-8', 'replace')
commits = [c for c in g('log', '--reverse', '--format=%h', 'origin/main..HEAD').split() if c]
order = {c: i for i, c in enumerate(commits)}
# (A)
A = collections.Counter()
keep = {}
for path, fl in flag.items():
    old = set(g('show', 'origin/main:' + path).split('\n'))
    for c, n, text, src in fl:
        if text in old:
            A[path] += 1
        else:
            keep.setdefault((path, text), []).append((c, n, src))
A_rows = collections.Counter()
for path, fl in flag.items():
    old = set(g('show', 'origin/main:' + path).split('\n'))
    A_rows[path] = len(set(t for _c, _n, t, _s in fl if t in old))
# (B): the literal fragment of each kept row that carries the shared seven words
frag = {}
for (path, text), v in keep.items():
    s = v[0][2][3]
    rx = re.compile(r'[^A-Za-z0-9]+'.join(re.escape(w) for w in s.split()), re.I)
    m = rx.search(text)
    frag[(path, text)] = m.group(0) if m else None
lit = sorted(set(f for f in frag.values() if f and '\n' not in f))
pf = SP + '/inv2_frags.txt'
io.open(pf, 'w', encoding='utf-8', newline='\n').write('\n'.join(lit) + '\n')
out = g('grep', '-I', '-h', '-o', '-i', '-F', '-f', pf, 'origin/main', '--', 'data', 'tools')
pub = set(x.lower() for x in out.split('\n') if x)
print('fragments', len(lit), '; found in the relay at origin/main', len(set(l.lower() for l in lit) & pub), '; rows whose fragment could not be located literally', sum(1 for f in frag.values() if not f))
CITE = re.compile(r'PLACE-papers|PLACE-phase|FINDINGS|REGISTRY|ERRATA|INSTRUMENTS|OPEN_TRAILS|SPIRAL_MAP|README|FACES_LEDGER|THE_[A-Z_]{6,}|SIDE-carrier-spec|SIDE-constants|SIDE-spinor-calibration-mathlib')
res = collections.defaultdict(lambda: collections.defaultdict(list))
for (path, text), v in keep.items():
    f = frag[(path, text)]
    cls = 'B' if (f and f.lower() in pub) else ('NEW, CITES A PRIVATE FILE' if CITE.search(text) else 'NEW, CITES NONE') if f else 'UNLOCATED'
    res[path][cls].append((text, v))
pickle.dump({p: dict(d) for p, d in res.items()}, open(SP + '/inv2_753.pkl', 'wb'))
print()
print('%-42s %5s %5s %6s %6s %5s  earliest commit holding a NEW row ; sources of NEW rows' % ('file', 'A-old', 'B-pub', 'NEWcit', 'NEWnon', 'unloc'))
tot = collections.Counter()
for path in sorted(set(list(flag) )):
    d = res.get(path, {})
    new = d.get('NEW, CITES A PRIVATE FILE', []) + d.get('NEW, CITES NONE', [])
    cs = sorted(set(c for _t, v in new for c, _n, _s in v), key=lambda c: order.get(c, 999))
    srcs = collections.Counter('%s:%s' % (v[0][2][0], v[0][2][1]) for _t, v in new)
    print('%-42s %5d %5d %6d %6d %5d  %s ; %s' % (path, A_rows[path], len(d.get('B', [])), len(d.get('NEW, CITES A PRIVATE FILE', [])), len(d.get('NEW, CITES NONE', [])), len(d.get('UNLOCATED', [])),
                                             cs[0] if cs else '-', ', '.join('%s x%d' % kv for kv in srcs.most_common(3))))
    tot['A'] += A_rows[path]; tot['B'] += len(d.get('B', [])); tot['NEWcit'] += len(d.get('NEW, CITES A PRIVATE FILE', [])); tot['NEWnon'] += len(d.get('NEW, CITES NONE', [])); tot['unloc'] += len(d.get('UNLOCATED', []))
print(dict(tot))
