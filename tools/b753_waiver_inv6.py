"""seventh word (1): the column. One pass over every blob of origin/main's tree: for each inventory row, do its words, or its figures and formulas, already stand there. Printed; no bank."""
import io, os, re, subprocess, sys, collections, pickle, time, json, difflib
REL, PP = 'D:/relay', 'D:/MY-DOwnloads/PLACE-papers'
SP = os.path.dirname(os.path.abspath(__file__))
def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')
K = 5
def toks(s):
    s = s.replace('[...]', ' ')
    return re.findall(r'[^\W_]+', s.lower())
def shing(s):
    t = toks(s)
    if len(t) < K:
        return [' '.join(t)] if len(t) >= 3 else []
    return [' '.join(t[i:i + K]) for i in range(len(t) - K + 1)]
NUM = re.compile(r'(?<![\w.:/-])(?:\d+(?:\.\d+)+|\d+\.\d+|\d+/\d+|\d+(?:\.\d+)?\s?%)(?![\w/-])')
DATE = re.compile(r'\d{4}-\d{2}-\d{2}|\bv\d+(?:\.\d+)+\S*|\b10\.\d{4,}/\S+')
def squeeze(s):
    return re.sub(r'[*`\s\\$]+', '', s)
EQ = re.compile(r'([^\s=,;()|"]{1,40})\s*(=|≈|≥|≤|∈)\s*([^\s=,;|"]{1,40})')
def figs(s):
    s0 = DATE.sub(' ', s.replace('[...]', ' '))
    out = set()
    for m in NUM.finditer(s0):
        out.add('N ' + re.sub(r'\s', '', m.group(0)))
    s1 = re.sub(r'[*`\\$]+', '', s0)
    pos = 0
    while True:
        m = EQ.search(s1, pos)
        if not m:
            break
        l, r = m.group(1).strip('.:*"\''), m.group(3).rstrip('.:*"\'')
        if l and r and (re.search(r'\d', l + r) or len(l) + len(r) >= 4) and not re.fullmatch(r'[A-Za-z]{1,20}', l + r):
            out.add('E ' + l + m.group(2) + r)
        pos = m.start(3)
    return out

# ---------------- the rows
rows = []   # dict(bank, n, kind, src, text)
A = io.open(REL + '/data/b753_anchors.txt', encoding='utf-8').read().split('\n')
sec, slug = None, None
for i, l in enumerate(A, 1):
    if l.startswith('## '):
        sec = l
    s = l.strip()
    m = re.match(r'^([a-zA-Z0-9-]+) \(:(\d+), (I+)\) \|', s)
    if m and sec and 'THE ANCHORS' in sec:
        slug = (m.group(1), int(m.group(2)))
        rows.append(dict(bank='anchors', n=i, kind='slug', src='FINDINGS :%d' % slug[1], text=m.group(1).replace('-', ' '), raw=m.group(1), anchor=slug))
        continue
    m = re.match(r'^:(\d+) "(.*)"$', s)
    if m and sec and ('THE ANCHORS' in sec or 'OWN RULE' in sec):
        rows.append(dict(bank='anchors', n=i, kind='sentence/tag' if 'THE ANCHORS' in sec else 'layer rule', src='FINDINGS :%s' % m.group(1), text=m.group(2), anchor=slug if 'THE ANCHORS' in sec else None))
        continue
    m = re.match(r'^MOVED BY (FINDINGS|REGISTRY|ERRATA) :(\d+) \(.*?\): "(.*)"$', s)
    if m:
        rows.append(dict(bank='anchors', n=i, kind='later line', src='%s :%s' % (m.group(1), m.group(2)), text=m.group(3), anchor=slug))
        continue
    m = re.match(r'^REGISTRY :(\d+) \*(.*)\*$', s)
    if m:
        rows.append(dict(bank='anchors', n=i, kind='ceiling phrase', src='REGISTRY :%s' % m.group(1), text=m.group(2), anchor=None))
        continue
    if sec and 'THE ANCHORS' not in sec and re.search(r'"[^"]{12,}"|\*[^*]{6,}\*', s):
        q = re.findall(r'"([^"]{12,})"', s) + re.findall(r'\*([^*]{6,})\*', s)
        rows.append(dict(bank='anchors', n=i, kind='other', src='(phrase in the rule, a control or the list)', text=' / '.join(q), anchor=None))
H = io.open(REL + '/data/b753_head_read.txt', encoding='utf-8').read().split('\n')
for i in (64, 65, 66):
    q = re.findall(r'"([^"]{12,})"', H[i - 1])
    rows.append(dict(bank='head_read', n=i, kind='head read', src='PLACE-papers README / description', text=' / '.join(q) if q else H[i - 1], anchor=None))
# the structural pass rows (inv5's logic), fragment = the shared run
NAMES = {'FINDINGS': 'FINDINGS.md', 'REGISTRY': 'REGISTRY.md', 'ERRATA': 'ERRATA.md', 'README': 'README.md', 'OPEN_TRAILS': 'OPEN_TRAILS.md', 'SPIRAL_MAP': 'SPIRAL_MAP.md',
         'FACES_LEDGER': 'FACES_LEDGER.md', 'INSTRUMENTS': 'phase1.5/method/INSTRUMENTS.md', 'VERIFICATION_LOOM': 'VERIFICATION_LOOM.md'}
ppfile = {k: io.open(PP + '/' + p, encoding='utf-8', errors='replace').read().split('\n') for k, p in NAMES.items() if os.path.isfile(PP + '/' + p)}
own = collections.defaultdict(set)
cur = None
for l in g(PP, 'diff', '-U0', 'origin/main..HEAD').split('\n'):
    if l.startswith('+++ b/'):
        cur = l[6:]
    m = re.match(r'^@@ -\S+ \+(\d+)(?:,(\d+))?', l)
    if m and cur:
        own[cur].update(range(int(m.group(1)), int(m.group(1)) + int(m.group(2) or 1)))
CITE = re.compile(r'\b(%s)(?:\.md)?[`\']?(?:,| at| line)? ?((?::\d+(?:-:?\d+)?(?:, ?| and )?)+)' % '|'.join(NAMES))
changed = set()
for p in g(REL, 'diff', '--name-only', 'origin/main', '--').split('\n'):
    if p and p != 'data/b753_anchors.txt' and p.endswith(('.txt', '.json', '.py', '.tpl', '.md')) and os.path.isfile(REL + '/' + p):
        changed.add(p)
for p in sorted(changed):
    old = set(g(REL, 'show', 'origin/main:' + p).split('\n'))
    for n, text in enumerate(io.open(REL + '/' + p, encoding='utf-8', errors='replace').read().split('\n'), 1):
        if len(text) <= 30 or text in old or not CITE.search(text):
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
                        mm = difflib.SequenceMatcher(None, text, src[:4000], autojunk=False).find_longest_match(0, len(text), 0, min(len(src), 4000))
                        if mm.size >= 24 and (best is None or mm.size > best[0]):
                            best = (mm.size, k, ln, text[mm.a:mm.a + mm.size])
        if best:
            rows.append(dict(bank=p.replace('data/b753_', '').replace('tools/', 't/'), n=n, kind='cited line', src='%s :%d' % (best[1], best[2]), text=best[3], anchor=None))
print('rows', len(rows), dict(collections.Counter(r['bank'] for r in rows)))
for r in rows:
    r['sh'] = shing(r['text'])
    r['fg'] = figs(r['text'])
want_sh = collections.defaultdict(list)
want_fg = collections.defaultdict(list)
for k, r in enumerate(rows):
    for s in set(r['sh']):
        want_sh[s].append(k)
    for f in r['fg']:
        want_fg[f].append(k)
print('distinct shingles', len(want_sh), '; distinct figures', len(want_fg))

# ---------------- one pass over origin/main's tree
t0 = time.time()
ls = [l for l in g(REL, 'ls-tree', '-r', '-l', 'origin/main').split('\n') if l]
blobs = []
for l in ls:
    meta, path = l.split('\t', 1)
    mode, typ, sha, size = meta.split()
    if typ == 'blob' and size != '-':
        blobs.append((sha, int(size), path.strip('"')))
print('blobs at origin/main', len(blobs), '; bytes', sum(b[1] for b in blobs))
seen = {}
for sha, size, path in blobs:
    seen.setdefault(sha, path)
p = subprocess.Popen(['git', '-C', REL, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
sh_hit = collections.defaultdict(lambda: collections.Counter())   # row -> (path, line) -> shingles there
sh_any = collections.defaultdict(set)
fg_hit = collections.defaultdict(dict)                            # row -> fig -> (path, line)
read, binary, skipped = 0, 0, 0
WS = set(want_sh)
for sha, path in seen.items():
    p.stdin.write((sha + '\n').encode()); p.stdin.flush()
    head = p.stdout.readline().split()
    size = int(head[2])
    data = p.stdout.read(size); p.stdout.read(1)
    if b'\0' in data[:8000]:
        binary += 1
        continue
    read += 1
    text = data.decode('utf-8', 'replace')
    for n, l in enumerate(text.split('\n'), 1):
        if len(l) < 4:
            continue
        if len(l) > 200000:
            l = l[:200000]; skipped += 1
        t = toks(l)
        if len(t) >= 3:
            ss = [' '.join(t[i:i + K]) for i in range(max(1, len(t) - K + 1))]
            if len(t) < K + 3:
                ss += [' '.join(t[i:i + 3]) for i in range(len(t) - 2)] + [' '.join(t[i:i + 4]) for i in range(len(t) - 3)]
            for s in set(ss):
                if s in WS:
                    for k in want_sh[s]:
                        sh_hit[k][(path, n)] += 1
                        sh_any[k].add(s)
        if any(c.isdigit() for c in l) or '=' in l:
            for f in figs(l):
                if f in want_fg:
                    for k in want_fg[f]:
                        fg_hit[k].setdefault(f, (path, n))
p.stdin.close()
print('text blobs read %d ; binary set apart %d ; lines cut at 200000 chars %d ; seconds %.0f' % (read, binary, skipped, time.time() - t0))
out = []
for k, r in enumerate(rows):
    S = set(r['sh'])
    cov = len(sh_any[k]) / len(S) if S else None
    bl = sh_hit[k].most_common(1)
    bestcov = (bl[0][1] / len(S)) if (bl and S) else 0
    r2 = dict((x, r[x]) for x in ('bank', 'n', 'kind', 'src', 'text', 'anchor'))
    r2.update(nsh=len(S), cov=cov, best=bl[0][0] if bl else None, bestcov=bestcov, figs=sorted(r['fg']), fhit=dict(fg_hit[k]))
    out.append(r2)
pickle.dump(out, open(SP + '/inv6_753.pkl', 'wb'))
print('pickled', len(out))
