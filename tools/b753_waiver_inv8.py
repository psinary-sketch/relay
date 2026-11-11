"""the figure and formula arm, widened after its control failed on FINDINGS :825 (a formula with a comma and a space inside its left side). argv: part, parts."""
import io, os, re, subprocess, sys, collections, pickle, time
REL = 'D:/relay'
SP = os.path.dirname(os.path.abspath(__file__))
def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')
NUM = re.compile(r'(?<![\w.:/-])(?:\d+(?:\.\d+)+|\d+/\d+|\d+(?:\.\d+)?\s?%)(?![0-9A-Za-z_/-])')
DATE = re.compile(r'\d{4}-\d{2}-\d{2}|\bv\d+(?:\.\d+)+\S*|\b10\.\d{4,}/\S+|\S+\.(?:md|py|json|txt|lean|tpl)\b|\S*[/\\]\S*[/\\]\S*')
OPS = set('|^/·×±≥≤≈∏∑√∈=<>+−∀∃→↔⊂∩∪∘⊗')
REL_ = '=≈≥≤∈'
def mathy(t):
    for c in t:
        if c.isdigit() or c in OPS or c in '()_' or '\u0370' <= c <= '\u03ff' or '\u2070' <= c <= '\u209f' or '\u2100' <= c <= '\u214f' or '\u2200' <= c <= '\u22ff' or c in '²³¹':
            return True
    return False
def clean(x):
    return x.strip('.,;:"\'“”’`*=≈')
def ok(x):
    nop = sum(1 for c in x if c in OPS)
    return len(x) >= 5 and (nop >= 2 or (nop >= 1 and any(c.isdigit() or c > '\u036f' for c in x)))
def figs(s):
    s0 = DATE.sub(' ', s.replace('[...]', ' '))
    out = set()
    for m in NUM.finditer(s0):
        out.add('N ' + re.sub(r'\s', '', m.group(0)))
    s1 = re.sub(r'[*`\\$]+', '', s0)
    run = []
    def flush():
        if run:
            x = clean(''.join(run))
            if ok(x):
                out.add('X ' + x)
            for side in re.split('[%s]' % REL_, x):
                side = clean(side)
                if side != x and ok(side) and len(side) >= 6:
                    out.add('X ' + side)
        del run[:]
    for t in s1.split():
        if mathy(t) or (run and len(t) <= 2 and run[-1][-1:] in OPS):
            run.append(t)
            if t[-1:] in '.;"”' or (t[-1:] == ',' and not run[0].count('(') > ''.join(run).count(')')):
                flush()
        else:
            flush()
    flush()
    return out
if __name__ == '__main__':
    part, parts = int(sys.argv[1]), int(sys.argv[2])
    R = pickle.load(open(SP + '/inv6_753.pkl', 'rb'))
    want = collections.defaultdict(list)
    rf = []
    for k, r in enumerate(R):
        f = figs(r['text'])
        rf.append(sorted(f))
        for x in f:
            want[x].append(k)
    if part < 0:
        for k, r in enumerate(R):
            if r['src'] in ('FINDINGS :821', 'FINDINGS :825', 'FINDINGS :765', 'FINDINGS :785', 'FINDINGS :797'):
                print(r['src'], rf[k])
        print('rows with a figure', sum(1 for x in rf if x), '; distinct', len(want), '; kinds', dict(collections.Counter(x[0] for x in want)))
        sys.exit()
    t0 = time.time()
    seen = {}
    for l in g(REL, 'ls-tree', '-r', 'origin/main').split('\n'):
        if l:
            meta, path = l.split('\t', 1)
            mode, typ, sha = meta.split()
            if typ == 'blob':
                seen.setdefault(sha, path.strip('"'))
    items = sorted(seen.items())[part::parts]
    p = subprocess.Popen(['git', '-C', REL, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    hit = collections.defaultdict(dict)
    PRE = re.compile(r'[0-9|^·×±≥≤≈∏∑√∈=−\u0370-\u03ff\u2070-\u209f\u2100-\u214f\u2200-\u22ff²³¹]')
    n_read = 0
    for sha, path in items:
        p.stdin.write((sha + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        if b'\0' in data[:8000]:
            continue
        n_read += 1
        for n, l in enumerate(data.decode('utf-8', 'replace').split('\n'), 1):
            if len(l) < 4 or not PRE.search(l):
                continue
            for f in figs(l[:200000]):
                if f in want:
                    for k in want[f]:
                        hit[k].setdefault(f, (path, n))
    p.stdin.close()
    pickle.dump((rf, dict(hit)), open(SP + '/inv8_753_%d.pkl' % part, 'wb'))
    print('part %d of %d: text blobs %d ; rows with a hit %d ; seconds %.0f' % (part, parts, n_read, len(hit), time.time() - t0))
