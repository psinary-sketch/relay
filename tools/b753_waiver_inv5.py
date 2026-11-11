"""inventory, structural pass: a row that CITES a line of a PLACE-papers file and carries 24 or more consecutive characters of that line (or its neighbours)."""
import io, os, re, subprocess, collections, difflib, sys
REL, PP = 'D:/relay', 'D:/MY-DOwnloads/PLACE-papers'
SP = os.path.dirname(os.path.abspath(__file__))
def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')
NAMES = {'FINDINGS': 'FINDINGS.md', 'REGISTRY': 'REGISTRY.md', 'ERRATA': 'ERRATA.md', 'README': 'README.md', 'OPEN_TRAILS': 'OPEN_TRAILS.md', 'SPIRAL_MAP': 'SPIRAL_MAP.md',
         'FACES_LEDGER': 'FACES_LEDGER.md', 'INSTRUMENTS': 'phase1.5/method/INSTRUMENTS.md', 'VERIFICATION_LOOM': 'VERIFICATION_LOOM.md'}
ppfile = {}
for k, p in NAMES.items():
    if os.path.isfile(PP + '/' + p):
        ppfile[k] = io.open(PP + '/' + p, encoding='utf-8', errors='replace').read().split('\n')
own = collections.defaultdict(set)
cur = None
for l in g(PP, 'diff', '-U0', 'origin/main..HEAD').split('\n'):
    if l.startswith('+++ b/'):
        cur = l[6:]
    m = re.match(r'^@@ -\S+ \+(\d+)(?:,(\d+))?', l)
    if m and cur:
        own[cur].update(range(int(m.group(1)), int(m.group(1)) + int(m.group(2) or 1)))
CITE = re.compile(r'\b(%s)(?:\.md)?[`\']?(?:,| at| line)? ?((?::\d+(?:-:?\d+)?(?:, ?| and )?)+)' % '|'.join(NAMES))
commits = [c for c in g(REL, 'log', '--reverse', '--format=%h', 'origin/main..HEAD').split() if c]
order = {c: i for i, c in enumerate(commits)}
rows, seen = {}, set()
def take(path, c, text):
    for n, l in enumerate(text.split('\n'), 1):
        if len(l) > 30 and CITE.search(l):
            rows.setdefault((path, l), (c, n))
for c in commits:
    for p in g(REL, 'diff-tree', '--no-commit-id', '--name-only', '-r', c).split('\n'):
        if p and p.endswith(('.txt', '.json', '.py', '.tpl', '.md')):
            b = g(REL, 'rev-parse', '%s:%s' % (c, p)).strip()
            if (p, b) in seen:
                continue
            seen.add((p, b))
            take(p, c, g(REL, 'show', '%s:%s' % (c, p)))
for l in g(REL, 'status', '--porcelain').split('\n'):
    p = l[3:].strip().strip('"')
    if p and os.path.isfile(REL + '/' + p) and p.endswith(('.txt', '.json', '.py')):
        take(p, 'WORKTREE', io.open(REL + '/' + p, encoding='utf-8', errors='replace').read())
print('rows citing a line of a PLACE-papers ledger, over every version past origin and the working tree:', len(rows))
oldrows = {}
found = []
for (path, text), (c, n) in rows.items():
    if path not in oldrows:
        oldrows[path] = set(g(REL, 'show', 'origin/main:' + path).split('\n'))
    if text in oldrows[path]:
        continue
    best = None
    for m in CITE.finditer(text):
        k = m.group(1)
        if k not in ppfile:
            continue
        for a in re.findall(r':(\d+)', m.group(2)):
            a = int(a)
            for ln in (a, a + 1, a - 1, a + 2):
                if 1 <= ln <= len(ppfile[k]) and ln not in own[NAMES[k]]:
                    src = ppfile[k][ln - 1]
                    if len(src) < 24:
                        continue
                    sm = difflib.SequenceMatcher(None, text, src[:4000], autojunk=False)
                    mm = sm.find_longest_match(0, len(text), 0, min(len(src), 4000))
                    if mm.size >= 24 and (best is None or mm.size > best[0]):
                        best = (mm.size, k, ln, text[mm.a:mm.a + mm.size])
    if best:
        found.append((path, n, c, best, text))
lit = sorted(set(f[3][3] for f in found))
io.open(SP + '/inv5_frags.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(lit) + '\n')
pub = set(x for x in g(REL, 'grep', '-I', '-h', '-o', '-F', '-f', SP + '/inv5_frags.txt', 'origin/main', '--', 'data', 'tools').split('\n') if x)
by = collections.defaultdict(list)
for f in found:
    by[f[0]].append(f)
print('%-40s %5s %9s %9s  earliest ; cited lines' % ('file', 'rows', 'new words', 'in origin'))
for path in sorted(by):
    fs = by[path]
    new = [f for f in fs if f[3][3] not in pub]
    cs = sorted(set(f[2] for f in fs), key=lambda c: order.get(c, 999))
    cn = sorted(set(f[2] for f in new), key=lambda c: order.get(c, 999))
    srcs = sorted(set('%s :%d' % (f[3][1], f[3][2]) for f in fs), key=lambda s: (s.split()[0], int(s.split(':')[1])))
    print('%-40s %5d %9d %9d  %s (new words from %s) ; %s' % (path, len(fs), len(new), len(fs) - len(new), cs[0], cn[0] if cn else '-', ', '.join(srcs[:40]) + (' ... %d in all' % len(srcs) if len(srcs) > 40 else '')))
if len(sys.argv) > 1:
    for f in found:
        if f[0] == sys.argv[1]:
            print('  :%d %s:%d shared %d chars, in origin %s' % (f[1], f[3][1], f[3][2], f[3][0], f[3][3] in pub))
