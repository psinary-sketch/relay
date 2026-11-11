"""(R363) sixth word (2): the inventory. Printed, written to no bank and no tracked file (one pickle of results in the scratchpad)."""
import io, os, re, subprocess, sys, json, collections, pickle
REL = 'D:/relay'
PRIV = ['PLACE-papers', 'TECHNE-Core', 'PLACE-phase1.5', 'PLACE-phase2', 'SIDE-carrier-spec', 'SIDE-spinor-calibration-mathlib', 'SIDE-constants', 'glassbead-game']
LOC = lambda n: 'D:/MY-DOwnloads/PLACE-papers' if n == 'PLACE-papers' else 'D:/' + n
N = 7
SP = os.path.dirname(os.path.abspath(__file__))

def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')

PATHISH = re.compile(r'\S*[/\\_]\S*|\S+\.(?:md|py|json|txt|lean|tpl|ps1)\b|\b[0-9a-f]{7,64}\b')
def toks(s):
    s = PATHISH.sub(' ', s)
    return re.findall(r'[A-Za-z0-9]+', s.lower())
def shingles(s):
    t = toks(s)
    out = []
    for i in range(len(t) - N + 1):
        w = t[i:i + N]
        if sum(1 for x in w if x.isalpha() and len(x) >= 3) >= 5:
            out.append(' '.join(w))
    return out

# ---- every version of every text file the commits past origin touch, and the working tree
commits = [c for c in g(REL, 'log', '--reverse', '--format=%h', 'origin/main..HEAD').split() if c]
rows = {}            # text -> [(path, commit)] first seen
order = {c: i for i, c in enumerate(commits)}
def take(path, c, text):
    for n, l in enumerate(text.split('\n'), 1):
        if len(l) > 30:
            rows.setdefault(l, []).append((path, c, n))
seen_blob = set()
for c in commits:
    for p in g(REL, 'diff-tree', '--no-commit-id', '--name-only', '-r', c).split('\n'):
        if p and (p.startswith('data/') or p.startswith('tools/')) and p.endswith(('.txt', '.json', '.py', '.tpl', '.md')):
            b = g(REL, 'rev-parse', '%s:%s' % (c, p)).strip()
            if (p, b) in seen_blob or not b or ' ' in b:
                continue
            seen_blob.add((p, b))
            take(p, c, g(REL, 'show', '%s:%s' % (c, p)))
wt = [l[3:].strip().strip('"') for l in g(REL, 'status', '--porcelain', '--', 'data', 'tools').split('\n') if l.strip()]
wt = [p for p in wt if os.path.basename(p).startswith('b753') or 'b753' in p]
for p in wt:
    if os.path.isfile(REL + '/' + p) and p.endswith(('.txt', '.json', '.py')):
        take(p, 'WORKTREE', io.open(REL + '/' + p, encoding='utf-8', errors='replace').read())
print('commits past origin', len(commits), '; file versions', len(seen_blob), '; working-tree b753 files not committed', len(wt), wt[:8], '; distinct rows over 30 chars', len(rows))

# the pushed relay at origin/main: a row already there is not this act's addition (the old banks, public already)
index = collections.defaultdict(list)
for text in rows:
    for s in set(shingles(text)):
        index[s].append(text)
print('shingles of the rows', len(index))

# ---- the private corpus, streamed
hit = {}   # text -> (repo, path, line, shingle)
stats = collections.Counter()
for name in PRIV:
    root = LOC(name)
    if not os.path.isdir(root + '/.git'):
        print('NO CLONE ON D:', name)
        continue
    own = set()
    if name == 'PLACE-papers':   # lines this act landed itself (past PP's origin) are the act's own composition
        cur = None
        for l in g(root, 'diff', '-U0', 'origin/main..HEAD').split('\n'):
            if l.startswith('+++ b/'):
                cur = l[6:]
            m = re.match(r'^@@ -\S+ \+(\d+)(?:,(\d+))?', l)
            if m and cur:
                a, k = int(m.group(1)), int(m.group(2) or 1)
                own.update((cur, x) for x in range(a, a + k))
        print('PLACE-papers lines landed by this act (set apart):', len(own))
    files = [p for p in g(root, 'ls-files').split('\n') if p.endswith(('.md', '.txt', '.lean', '.tex', '.py', '.json', '.yml', '.toml')) or os.path.basename(p).upper().startswith('README')]
    stats[name + ' files'] = len(files)
    for p in files:
        try:
            if os.path.getsize(root + '/' + p) > 40_000_000:
                continue
            L = io.open(root + '/' + p, encoding='utf-8', errors='replace').read().split('\n')
        except OSError:
            continue
        for n, l in enumerate(L, 1):
            if (p, n) in own or len(l) < 30:
                continue
            for s in shingles(l):
                if s in index:
                    for text in index[s]:
                        if text not in hit:
                            hit[text] = (name, p, n, s)
print(dict(stats))
# is the hit row already in the relay at origin/main (public before this act)? then the words left earlier, not by this act
old = {}
flag = collections.defaultdict(list)
for text, src in hit.items():
    for path, c, n in rows[text]:
        flag[path].append((c, n, text, src))
pickle.dump(dict(flag), open(SP + '/inv1_753.pkl', 'wb'))
print()
print('BY FILE: rows carrying 7 consecutive words of a private file (paths, names with _ or /, and hashes stripped first); earliest commit; sources')
for path in sorted(flag):
    fl = flag[path]
    texts = set(t for _c, _n, t, _s in fl)
    cs = sorted(set(c for c, _n, _t, _s in fl), key=lambda c: order.get(c, 999))
    srcs = collections.Counter((s[0], s[1]) for _c, _n, _t, s in set((c, n, t, s) for c, n, t, s in fl))
    print('%-44s rows %4d ; earliest %s ; sources %s' % (path, len(texts), cs[0], ', '.join('%s:%s x%d' % (r, p, k) for (r, p), k in srcs.most_common(4))))
