# -*- coding: utf-8 -*-
"""circuit_read.py -- THE DEPENDENCY-CIRCUIT READER (relay data/b690_circuit_spec.txt; its successor data/b692_circuit_spec.txt), built at b692
under (R302)(3)(b)-(d). It reads the closure banks the runner's closure step writes (data/bNNN_circuit_<kernel>_<tag>_<tip>.jsonl.gz, one record
per programme constant: n name, m module, k kind, l line, t type class, h type hash, a axioms, b binders, c closure over the programme's names)
and prints the spec's readings as rows; the bars are the build act's, banked before the run (data/b692_circuit_bars.txt).

### Routes (python -X utf8 tools/circuit_read.py <route> ...):
###   read <bank.jsonl.gz> <kernel> <tag> <tip> <main theorem>  -> data/b692_circuit_<kernel>_<tag>.txt (SERIES, TERMINALS, SHORTS, WIDTH, LOAD),
###        its .dot (OUTPUT) and .png beside data/b692_circuit_<kernel>_<tag>_png_hashes.txt
###   dominance <bank.jsonl.gz> <kernel> <tip> <main> <face> <faces page> <not reached...>  -> data/b692_circuit_dominance.txt
###   controls <bank.jsonl.gz> <kernel> <tip> <print bank>      -> data/b692_circuit_controls.txt (the planted short in a scratch copy of the
###        records; HCount among the strip-free theorem's TERMINALS; no premise at h2_sign_iff_rh)
###   shorts <bank.jsonl.gz> <kernel> <label> <declaration>     -> data/b692_circuit_shorts_<label>.txt (SHORTS on another bank: the branch's)
###   readfirst <ferry bank> <hand readfirst bank>              -> data/b692_readfirst_closure.txt and data/b692_readfirst_diff.txt
###   suiteload <first act> <last act>                          -> data/b692_suite_load.txt
### The reader writes only the banks named; it edits no bank it reads. Written by the Write tool at b692.
"""
import collections
import gzip
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = chr(10)
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
FEW = 5                     # ### data/b692_circuit_bars.txt, banked before the run
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### each kernel's libraries: (module prefix, tree path of that prefix's root)
LIBS = {'SIDE-explicit-formula': (('SIDEExplicitFormula', ''), ('Zeta23', ''), ('Lc', 'Vendored/Bulka/'), ('Hadamard', 'Vendored/Bulka/'),
                                  ('FunctionsOfOneComplexVariable', 'Vendored/Bulka/'))}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def put(name, lines):
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write((NL.join(lines) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def load(bank):
    txt = gzip.decompress(open(os.path.join(D, bank) if not os.path.isabs(bank) else bank, 'rb').read()).decode('utf-8')
    recs, head, lines, dup = {}, {}, 0, collections.defaultdict(list)
    for l in txt.split(NL):
        if not l.strip():
            continue
        j = json.loads(l)
        if j.get('header'):
            head = j
            continue
        lines += 1
        if j['n'] in recs:
            dup[j['n']].append(j['m'])
            if recs[j['n']]['c'] != j['c'] or recs[j['n']].get('a') != j.get('a') or recs[j['n']]['t'] != j['t']:
                sys.exit('### %s IS RECORDED TWICE WITH DIFFERENT CLOSURES -- NOTHING READ' % j['n'])
            continue
        recs[j['n']] = j
    if head.get('records') != lines:
        sys.exit('### THE BANK`S HEADER COUNT %s IS NOT ITS RECORD LINES %d -- NOTHING READ' % (head.get('records'), lines))
    head = dict(head, lines=lines, duplicates=dict((n, [recs[n]['m']] + ms) for n, ms in dup.items()))
    return recs, head


def own(kernel, module):
    return any(module == p or module.startswith(p + '.') for p, _src in LIBS[kernel])


def path_of(kernel, module):
    for p, src in LIBS[kernel]:
        if module == p or module.startswith(p + '.'):
            return src + module.replace('.', '/') + '.lean'
    return None


_SRC = {}


def src_lines(kernel, tip, module):
    k = (kernel, tip, module)
    if k not in _SRC:
        r = subprocess.run(['git', '-C', 'D:/' + kernel, 'show', '%s:%s' % (tip, path_of(kernel, module))], capture_output=True)
        _SRC[k] = r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if r.returncode == 0 else []
    return _SRC[k]


def named_prop(kernel, tip, rec):
    """a programme definition declared with result type Prop: its header from its line to the first ':=' carries ': Prop' before it."""
    if not rec or rec.get('k') != 'def' or not rec.get('l'):
        return False
    L = src_lines(kernel, tip, rec['m'])
    hdr = ' '.join(L[rec['l'] - 1: rec['l'] + 7])
    hdr = hdr.split(':=', 1)[0]
    return bool(re.search(r':\s*Prop\s*$', hdr.strip()))


def premises(kernel, tip, recs, rec):
    """the binders of rec's type that name a premise: a Prop binder whose type names a named Prop of the programme."""
    out = []
    for name, is_prop, cs in rec.get('b') or []:
        hits = [c for c in cs if named_prop(kernel, tip, recs.get(c))]
        if is_prop and hits:
            out.append((name, hits))
    return out


def listed(n):
    """the bars' "internal auxiliaries traversed and not listed": a name with an internal component once a private prefix is stripped (the
    generated `_simp_N_M`, `_proof_N`, `match_N`), or a generated equation or congruence lemma (`eq_N`, `eq_def`, `congr_simp`)."""
    core = re.sub(r'^_private\..*?\.0\.', '', n)
    parts = core.split('.')
    return not any(p.startswith('_') for p in parts) and not re.match(r'^(eq_\d+|eq_def|congr_simp)$', parts[-1])


def series(recs, main):
    S = set(recs[main]['c']) | {main}
    S = set(x for x in S if x in recs and listed(x))
    cl = dict((x, set(recs[x]['c']) & S) for x in S)
    order = sorted(S, key=lambda x: (len(cl[x]), x))
    chain = {}
    for x in order:
        prev = [y for y in cl[x] if cl[y] < cl[x]]
        chain[x] = 1 + max([chain[y] for y in prev] or [0])
    tip = max(order, key=lambda x: (chain[x], x == main))
    path = [tip]
    while chain[path[-1]] > 1:
        x = path[-1]
        nxt = max((y for y in cl[x] if cl[y] < cl[x] and chain[y] == chain[x] - 1), key=lambda y: (len(cl[y]), y))
        path.append(nxt)
    return order, chain, list(reversed(path))


def shorts(recs):
    S = [n for n, r in recs.items() if 'sorryAx' in (r.get('a') or [])]
    out = []
    for n in sorted(S):
        firsts = [x for x in [n] + recs[n]['c'] if x in recs and 'sorryAx' in (recs[x].get('a') or [])
                  and not any(y in recs and 'sorryAx' in (recs[y].get('a') or []) for y in recs[x]['c'])]
        out.append((n, sorted(set(firsts))))
    return out


def width(recs):
    groups = collections.defaultdict(list)
    for n, r in recs.items():
        if r.get('k') == 'theorem' and listed(n):
            groups[r['t']].append(n)
    pairs = []
    for t, ns in groups.items():
        ns = sorted(ns)
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                a, b = ns[i], ns[j]
                meet = set(recs[a]['c']) & set(recs[b]['c'])
                pairs.append((len(meet), a, b))
    return sorted(pairs)


def load_counts(recs):
    cnt = collections.Counter()
    for r in recs.values():
        cnt.update(set(x for x in r['c'] if listed(x)))
    return cnt


def where(rec):
    return '%s:%s' % (rec.get('m'), rec.get('l'))


# ================================================================================ read
def read(bank, kernel, tag, tip, main):
    recs, head = load(bank)
    if main not in recs:
        sys.exit('### THE MAIN THEOREM %s IS NOT A RECORD -- NOTHING WRITTEN' % main)
    notown = [n for n, r in recs.items() if not own(kernel, r['m'])]
    order, chain, longest = series(recs, main)
    m = recs[main]
    prem = premises(kernel, tip, recs, m)
    ax_out = [x for x in m.get('a') or [] if x not in STD3]
    sh = shorts(recs)
    wp = width(recs)
    few = [p for p in wp if p[0] <= FEW]
    cnt = load_counts(recs)
    mcl = set(m['c'])
    top = cnt.most_common(12)
    L = ['b692 -- THE DEPENDENCY-CIRCUIT READING OF %s AT %s (tip %s), (R302)(3)(b), BY tools/circuit_read.py (%s)' % (kernel, tag, tip, utc()), '',
         '### the bank: relay data/%s ; record lines %d, the header`s count %s ; distinct names %d ; programme modules %d ; records outside the '
         'kernel`s own libraries %d' % (bank, head['lines'], head.get('records'), len(recs), len(head.get('modules') or []), len(notown)),
         '### names recorded twice (one constant listed under two modules, its closure, axioms and type class equal): %s' % (
             '; '.join('%s in %s' % (n, ' and '.join(ms)) for n, ms in sorted(head['duplicates'].items())) or 'NONE'),
         '### the bars: relay data/b692_circuit_bars.txt (FEW = %d ; the main theorem %s)' % (FEW, main), '',
         '## SERIES -- the main theorem`s closure over the own names in dependency order (each after every name in its own closure); rows: the',
         '## position | the name | module:line | its chain length.',
         '   names %d ; the longest chain %d' % (len(order), max(chain.values()))]
    L += ['   %5d  %-70s %s  chain %d' % (i + 1, x, where(recs[x]), chain[x]) for i, x in enumerate(order)]
    L += ['', '## SERIES -- THE LONGEST CHAIN (%d names), from the deepest to the main theorem:' % len(longest)] + ['   %s  (%s)' % (x, where(recs[x])) for x in longest]
    L += ['', '## TERMINALS -- the main theorem`s binders that name a premise, and the axioms in its closure beyond the standard three; rows are terminals.']
    L += ['   PREMISE  %s : names %s' % (b, ', '.join(h)) for b, h in prem] or ['   PREMISE  NONE (the type`s binders %d)' % len(m.get('b') or [])]
    L += ['   AXIOM    %s' % x for x in ax_out] or ['   AXIOM    NONE beyond the standard three (the axioms %s)' % (m.get('a') or [])]
    L += ['', '## SHORTS -- every record whose axioms carry sorryAx, with the first record on its path that uses sorryAx directly; rows are shorts.']
    L += ['   %s (%s) ; first on its path: %s' % (n, where(recs[n]), ', '.join(f)) for n, f in sh] or ['   SHORTS 0']
    L += ['', '## WIDTH -- theorem pairs of one type class whose closures over the own names meet in at most FEW = %d names; rows are pairs: meet |' % FEW,
          '## the one | the other. Every same-type theorem pair %d ; at or under the bar %d.' % (len(wp), len(few))]
    L += ['   %3d | %s (%s) | %s (%s)' % (k, a, where(recs[a]), b, where(recs[b])) for k, a, b in few] or ['   NONE at or under the bar']
    L += ['', '## WIDTH -- every same-type theorem pair with its meet (the bar`s context):']
    L += ['   %3d | %s | %s' % (k, a, b) for k, a, b in wp]
    L += ['', '## LOAD -- each own name by the count of records whose closure carries it, the twelve highest; * marks the main theorem`s closure.']
    L += ['   %5d %s %s' % (k, '*' if n in mcl else ' ', n) for n, k in top]
    L += ['', '### ### **RECORDS %d ; SERIES %d NAMES, THE LONGEST CHAIN %d ; TERMINALS: PREMISES %d, AXIOMS BEYOND THE STANDARD THREE %d ; SHORTS %d ; '
          'WIDTH: SAME-TYPE THEOREM PAIRS %d, AT OR UNDER FEW = %d: %d ; LOAD`S THREE HIGHEST %s.**' % (
              len(recs), len(order), max(chain.values()), len(prem), len(ax_out), len(sh), len(wp), FEW, len(few),
              ', '.join('%s (%d)' % (n, k) for n, k in top[:3]))]
    stem = 'b692_circuit_%s_%s' % (kernel, tag)
    put(stem + '.txt', L)
    dot, png = output(stem, recs, longest, few, prem, sh, main)
    put(stem + '_png_hashes.txt', [
        'b692 -- THE CIRCUIT FIGURE`S HASHES, %s AT %s (tip %s) (%s)' % (kernel, tag, tip, utc()), '',
        '### rows are binary banks this text bank roots (data/b680_rules.txt row (1)): the bank | sha256 | bytes | the DOT bank it renders.',
        '  data/%s.png | %s | %d | data/%s.dot (sha256 %s)' % (stem, hashlib.sha256(png).hexdigest(), len(png), stem, hashlib.sha256(dot).hexdigest()),
        '', '### ### **THE PNG DRAWN BY PIL FROM THE DOT BANK`S NODES (no graphviz on this host).**'])
    print(NL.join(L[:4] + [L[-1]]))


def output(stem, recs, longest, few, prem, sh, main):
    """the DOT bank (series as a chain, parallel pairs side by side, terminals as open ends, shorts marked) and a PNG drawn from the same nodes."""
    short = lambda n: n.split('.')[-1]   # noqa: E731
    dl = ['digraph circuit {', '  rankdir=TB; node [shape=box, fontsize=10];', '  // the series: the longest chain']
    for a, b in zip(longest, longest[1:]):
        dl.append('  "%s" -> "%s";' % (a, b))
    for i, (k, a, b) in enumerate(few[:20]):
        dl.append('  subgraph cluster_w%d { label="parallel, meet %d"; rank=same; "%s"; "%s"; }' % (i, k, a, b))
    for b, hits in prem:
        for h in hits:
            dl.append('  "open:%s" [shape=plaintext, label="%s (open)"]; "open:%s" -> "%s";' % (h, short(h), h, main))
    for n, _f in sh:
        dl.append('  "%s" [color=red, style=bold];' % n)
    dl.append('}')
    dot = (NL.join(dl) + NL).encode('utf-8')
    open(os.path.join(D, stem + '.dot') + '.tmp', 'wb').write(dot)
    os.replace(os.path.join(D, stem + '.dot') + '.tmp', os.path.join(D, stem + '.dot'))
    from PIL import Image, ImageDraw
    rows = len(longest)
    W, H = 1400, max(400, 60 + 26 * max(rows, len(few[:20]) + 2))
    im = Image.new('RGB', (W, H), 'white')
    dr = ImageDraw.Draw(im)
    dr.text((20, 10), 'the series: the longest chain to %s' % short(main), fill='black')
    for i, n in enumerate(longest):
        y = 40 + 26 * i
        dr.rectangle((20, y, 520, y + 20), outline='red' if n in dict(sh) else 'black')
        dr.text((26, y + 4), short(n)[:70], fill='black')
        if i:
            dr.line((270, y - 6, 270, y), fill='black')
    dr.text((600, 10), 'parallel pairs (one type, meet <= %d)' % FEW, fill='black')
    for i, (k, a, b) in enumerate(few[:20]):
        y = 40 + 26 * i
        dr.rectangle((600, y, 880, y + 20), outline='black')
        dr.text((606, y + 4), short(a)[:38], fill='black')
        dr.rectangle((900, y, 1180, y + 20), outline='black')
        dr.text((906, y + 4), short(b)[:38], fill='black')
        dr.text((1190, y + 4), 'meet %d' % k, fill='black')
    for j, (b, hits) in enumerate(prem):
        dr.text((20, H - 30 - 16 * j), 'open end: %s' % ', '.join(short(h) for h in hits), fill='blue')
    buf = io.BytesIO()
    im.save(buf, format='PNG', optimize=False)
    png = buf.getvalue()
    open(os.path.join(D, stem + '.png') + '.tmp', 'wb').write(png)
    os.replace(os.path.join(D, stem + '.png') + '.tmp', os.path.join(D, stem + '.png'))
    return dot, png


# ================================================================================ dominance
def dominance(bank, kernel, tip, main, face, page, *not_reached):
    recs, _head = load(bank)
    cl = set(recs[main]['c'])
    inn = face in cl or face == main
    path = []
    if inn:
        cur = main
        path = [cur]
        while cur != face:
            cand = [x for x in recs[cur]['c'] if x in recs and (x == face or face in recs[x]['c']) and x != cur]
            cur = min(cand, key=lambda x: (x != face, -len(recs[x]['c']), x)) if face in recs[cur]['c'] and face not in cand else \
                max(cand, key=lambda x: (x == face, len(recs[x]['c']), x))
            if cur in path:
                break
            path.append(cur)
    pg = rd(page).split(NL)
    faces = []
    for i, l in enumerate(pg, 1):
        mm = re.match(r'^\d+\. `([^`]+)` — [^—]+ — [^—]+ — `(theorem [^`]+)`', l)
        if mm and 'RiemannHypothesis' in mm.group(2) and '↔' in mm.group(2):
            faces.append((i, mm.group(1), mm.group(2)))
    L = ['b692 -- CLAUSE-DOMINANCE, (R302)(3)(c), BY tools/circuit_read.py (%s)' % utc(), '',
         '### the faces kernels: the kernels the faces page`s generator input names (relay data/b690_nodes_zeta.txt :94-:164, :126); the clause`s',
         '### compiled face %s (relay data/b690_nodes_zeta.txt :95); rows are kernels: the kernel | its main theorem | IN or NOT IN | the path.' % face, '',
         '  %-24s %-48s %s ; the path: %s' % (kernel, main, 'IN' if inn else 'NOT IN', ' -> '.join(path) if path else '-')]
    L += ['  %-24s %-48s NOT REACHED -- the closure step stopped at the price (relay data/b692_closure_step.txt); carried to b694 by name' % (k, '-')
          for k in not_reached]
    reached = 1
    L += ['', '### within %s, the faces the page names (its node lines whose statement is an equivalence with RiemannHypothesis): rows are faces |' % kernel,
          '### the page line | the clause`s face IN or NOT IN its closure:']
    fin = 0
    for i, n, st in faces:
        r = recs.get(n)
        v = 'NOT A RECORD' if r is None else ('IN' if face in r['c'] or n == face else 'NOT IN')
        fin += v == 'IN'
        L.append('  %-58s :%d  %s' % (n, i, v))
    L += ['', '### ### **CLAUSE-DOMINANCE %d OF %d FACES KERNELS REACHED (%s %s) ; %d NOT REACHED (%s) ; WITHIN %s THE CLAUSE`S FACE IN %d OF %d FACES THE '
          'PAGE NAMES.**' % (int(inn), reached, kernel, 'IN' if inn else 'NOT IN', len(not_reached), ', '.join(not_reached) or 'none', kernel, fin, len(faces))]
    put('b692_circuit_dominance.txt', L)
    print(NL.join(L[4:]))


# ================================================================================ controls
def controls(bank, kernel, tip, print_bank):
    recs, _head = load(bank)
    L = ['b692 -- THE READER`S CONTROLS, (R302)(3)(b), BY tools/circuit_read.py (%s)' % utc(), '',
         '### rows are controls: the control | what it reads | the reading | as wanted.', '']
    s0 = shorts(recs)
    L.append('  SHORTS ON THE BANK        relay data/%s | SHORTS %d | as wanted (0) %s' % (bank, len(s0), len(s0) == 0))
    leaf = sorted((n for n, r in recs.items() if r.get('k') == 'theorem' and own(kernel, r['m'])), key=lambda n: (len(recs[n]['c']), n))[0]
    planted = dict(recs)
    planted[leaf] = dict(recs[leaf], a=(recs[leaf].get('a') or []) + ['sorryAx'])
    s1 = shorts(planted)
    L.append('  SHORTS, A PLANTED COPY    sorryAx planted in a scratch copy of the records at %s | SHORTS %d at %s | as wanted (1, there) %s' % (
        leaf, len(s1), [n for n, _f in s1], len(s1) == 1 and s1[0][0] == leaf))
    sf = 'SIDEExplicitFormula.Schema.Wide.li_nonneg_cfg_imp_online_ne_zero'
    hc = 'SIDEExplicitFormula.Schema.Wide.HCount'
    pr = premises(kernel, tip, recs, recs[sf]) if sf in recs else []
    L.append('  THE STRIP-FREE THEOREM    %s`s TERMINALS (its premise binders): %s | Wide.HCount among them %s' % (
        sf, ['%s : %s' % (b, h) for b, h in pr], any(hc in h for _b, h in pr)))
    L.append('                            its SERIES carries %s: %s ; its axioms %s' % (hc, hc in recs.get(sf, {}).get('c', []), recs.get(sf, {}).get('a')))
    mn = 'SIDEExplicitFormula.B321.h2_sign_iff_rh'
    pm = premises(kernel, tip, recs, recs[mn])
    ax = rd(os.path.join(D, print_bank))
    pl = [l for l in ax.split(NL) if l.startswith("'%s'" % mn)]
    pg = [l for l in rd(os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')).split(NL) if l.startswith('8. `%s`' % mn)]
    ax_cell = re.search(r'axioms: (\[[^\]]*\])', pg[0]).group(1) if pg and re.search(r'axioms: (\[[^\]]*\])', pg[0]) else 'unread'
    L.append('  NO PREMISE AT THE MAIN    %s`s premise binders %s ; its axioms by collectAxioms %s ; the print bank (relay data/%s): %s ; the faces '
             'page :108 "%s", its axioms cell %s | as wanted (none) %s' % (
                 mn, pm or 'NONE', recs[mn].get('a'), print_bank, pl[0] if pl else 'the name is not on the kernel`s print list (print_targets.txt), '
                 'so the print bank carries no line for it', 'premises: none' if pg and 'premises: none' in pg[0] else 'premises cell unread', ax_cell,
                 not pm and bool(pg) and 'premises: none' in pg[0]))
    ok = len(s0) == 0 and len(s1) == 1 and any(hc in h for _b, h in pr) and not pm
    L += ['', '### ### **SHORTS 0 ON THE BANK ; THE PLANTED COPY READ AS ONE SHORT ; Wide.HCount A TERMINAL OF THE STRIP-FREE THEOREM %s ; NO PREMISE AT '
          'h2_sign_iff_rh %s ; THE CONTROLS AS WANTED %s.**' % (any(hc in h for _b, h in pr), not pm, ok)]
    put('b692_circuit_controls.txt', L)
    print(NL.join(L[3:]))


def shorts_route(bank, kernel, label, decl):
    recs, head = load(bank)
    s = shorts(recs)
    L = ['b692 -- SHORTS ON THE BANK %s (%s), BY tools/circuit_read.py (%s)' % (bank, label, utc()), '',
         '### records %d ; the header`s count %s ; rows are shorts: the record | module:line | the first on its path.' % (len(recs), head.get('records'))]
    L += ['   %s (%s) ; first on its path: %s' % (n, where(recs[n]), ', '.join(f)) for n, f in s] or ['   SHORTS 0']
    firsts = sorted(set(x for _n, f in s for x in f))
    L += ['', '### ### **SHORTS %d (RECORDS CARRYING sorryAx) ; THE FIRST ON EVERY PATH %s ; THE PLANTED DECLARATION %s %s.**' % (
        len(s), firsts, decl, 'THE ONE FIRST' if firsts == [decl] else '### NOT THE ONE FIRST')]
    put('b692_circuit_shorts_%s.txt' % label, L)
    print(NL.join(L[3:]))


# ================================================================================ readfirst
CITE = re.compile(r'(?<![\w/.-])((?:data|tools)/[\w.+-]+\.(?:txt|json|py|md|gz|png|sh|jsonl)|(?:phase1\.5|outputs)/[\w./-]+\.md|'
                  r'(?:FINDINGS|OPEN_TRAILS|INSTRUMENTS|README|REGISTRY|THE_CLAUSE_AND_ITS_COMPILED_FACES)\.md)')
LEDGERS = ('FINDINGS.md', 'OPEN_TRAILS.md')


def resolve(p):
    for base in (ROOT, PP):
        q = os.path.join(base, *p.split('/'))
        if os.path.exists(q):
            return q
    if p == 'INSTRUMENTS.md' and os.path.exists(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')):
        return os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
    return None


def readfirst(ferry, hand):
    ft = rd(os.path.join(D, ferry) if not os.path.isabs(ferry) else ferry).split(NL)
    seen, order = {}, []
    frontier = []
    for i, l in enumerate(ft, 1):
        for p in CITE.findall(l):
            if p not in seen:
                seen[p] = (0, 'relay data/%s :%d' % (ferry, i))
                order.append(p)
                frontier.append(p)
    depth = 0
    own_instruments = ('data/%s' % hand, 'tools/circuit_read.py')   # ### the reading's own instruments: listed, not followed
    while frontier:
        depth += 1
        nxt = []
        for p in frontier:
            q = resolve(p)
            if q is None or p.endswith(('.gz', '.png', '.json', '.jsonl')) or os.path.basename(p) in LEDGERS or p in own_instruments:
                continue
            for i, l in enumerate(rd(q).split(NL), 1):
                for c in CITE.findall(l):
                    if c not in seen:
                        seen[c] = (depth, '%s :%d' % (p, i))
                        order.append(c)
                        nxt.append(c)
        frontier = nxt
    direct = [p for p in order if seen[p][0] == 0]
    hl = rd(os.path.join(D, hand)).split(NL)
    hand_paths = []
    for l in hl:
        for p in CITE.findall(l):
            if p not in hand_paths:
                hand_paths.append(p)
    L = ['b692 -- READFIRST-CLOSURE ON THE RULING AND FERRY (relay data/%s), (R302)(3)(c), BY tools/circuit_read.py (%s)' % (ferry, utc()), '',
         '### rows are items in the b688 form: the path | resolved or not | the depth (0 cited by the text itself) | the line that cites it | the',
         '### unit of the bank`s rows and what the act takes from it (left for the seat`s hand). The ledgers, the hand list it is diffed against',
         '### and the reader itself are listed and not followed.', '']
    for p in order:
        dep, by = seen[p]
        L.append('  %-70s %-10s depth %d | cited at %s | -- | --' % (p, 'RESOLVED' if resolve(p) else 'UNRESOLVED', dep, by))
    L += ['', '### ### **ITEMS %d ; CITED BY THE TEXT ITSELF %d ; RESOLVED %d ; THE DEEPEST %d.**' % (
        len(order), len(direct), sum(1 for p in order if resolve(p)), max([v[0] for v in seen.values()] or [0]))]
    put('b692_readfirst_closure.txt', L)
    key = lambda p: os.path.normcase(resolve(p) or p)   # noqa: E731  ### one file under two spellings is one path
    dk, hk = set(key(p) for p in direct), set(key(p) for p in hand_paths)
    only_hand = [p for p in hand_paths if key(p) not in dk]
    only_text = [p for p in direct if key(p) not in hk]
    in_closure = [p for p in only_hand if p in seen]
    M = ['b692 -- READFIRST-CLOSURE AGAINST THE HAND LIST, (R302)(3)(c): THE TWO LISTS DIFFED (%s)' % utc(), '',
         '### the hand list: relay data/%s (paths %d) ; the computed list: relay data/b692_readfirst_closure.txt (cited by the text itself %d ; the' % (hand, len(hand_paths), len(direct)),
         '### closure %d). Rows: < a path the hand list carries and the text does not cite by path ; > a path the text cites and the hand list' % len(order),
         '### does not carry. No bank is rewritten by this reading.', '']
    M += ['  < %-68s %s' % (p, ('in the closure at depth %d, cited at %s' % seen[p]) if p in seen else 'outside the closure') for p in only_hand]
    M += ['  > %-68s cited at %s' % (p, seen[p][1]) for p in only_text]
    M += ['', '### ### **THE HAND LIST %d PATHS ; THE TEXT CITES %d ; BOTH %d ; LINES DIFFERING %d (HAND ONLY %d, OF WHICH IN THE CLOSURE %d ; TEXT ONLY %d).**' % (
        len(hand_paths), len(direct), len([p for p in hand_paths if key(p) in dk]), len(only_hand) + len(only_text), len(only_hand), len(in_closure),
        len(only_text))]
    put('b692_readfirst_diff.txt', M)
    print(NL.join(L[-1:] + M[-1:]))


# ================================================================================ suiteload
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) (.*)$", re.M)
SOURCE = re.compile(r"\bb(6\d\d)(?:’s|'s)? \(([a-z])\)")
SOURCES = (('bNNN (x)', SOURCE), ('data/bNNN_defects.txt (x)', re.compile(r"\bdata/b(6\d\d)_defects\.txt (?::\d+(?:-:\d+)? )?\(([a-z])\)")),
           ("bNNN's defect (x)", re.compile(r"\bb(6\d\d)(?:’s|'s)? defects? \(([a-z])\)")))


def suiteload(first, last):
    sys.path.insert(0, T)
    import rule_arms as RA
    first, last = int(first), int(last)
    series_ = []
    for a in range(first, last + 1):
        t = rd(os.path.join(D, 'b%d_defects.txt' % a))
        rows = DEFECT_ROW.findall(t)
        ck = rd(os.path.join(D, 'b%d_checks.txt' % a))
        m = re.search(r'ARMS RUN : (\d+)', ck)
        series_.append((a, len(rows), int(m.group(1)) if m else None))
    rule_src, yields = {}, collections.Counter()
    for nm, rule in RA.RULE_OF.items():
        mm = re.match(r'b(\d+) row \(?(\d+)\)?', rule)
        if not mm:
            continue
        txt = rd(os.path.join(D, 'b%s_rules.txt' % mm.group(1)))
        parts = re.split(r'(?m)^(?:  \(?(?=\d+\)? )|ROW (?=\d+ --))(\d+)\)? (?:-- )?', txt)
        body = ''
        for i in range(1, len(parts) - 1, 2):
            if parts[i] == mm.group(2):
                body = parts[i + 1]
        found = set()
        for shape, rx in SOURCES:
            hits = set(rx.findall(body))
            yields[shape] += len(hits)
            found |= hits
        own_hits = set((mm.group(1), x) for x in re.findall(r"defects bank(?:'|’)s entry \(([a-z])\)", body))   # ### the bank's own act
        yields["the defects bank's entry (x)"] += len(own_hits)
        found |= own_hits
        rule_src[nm] = sorted(found)
    by_defect = collections.defaultdict(list)
    for nm, src in rule_src.items():
        for s in src:
            by_defect[s].append(nm)
    L = ['b692 -- SUITE-LOAD, (R302)(3)(d): THE STANDING RULE ARMS AGAINST THE DEFECTS THEY ANSWER, AND THE DEFECTS-PER-ACT SERIES b%d-b%d (%s)' % (first, last, utc()), '',
         '### rows are standing rule arms: the arm | its rule (tools/rule_arms.py RULE_OF) | the source defects its rule`s row cites | the ones it',
         '### alone answers (no other arm`s rule cites them). A reading; no arm added. The needle`s yield printed: rule rows read %d, carrying a' % len(rule_src),
         '### source %d ; each shape`s yield: %s.' % (sum(1 for v in rule_src.values() if v), ' ; '.join('%s %d' % (s, yields[s]) for s in [x for x, _r in SOURCES] + ["the defects bank's entry (x)"])), '']
    for nm in RA.NAMES:
        src = rule_src.get(nm, [])
        alone = [s for s in src if by_defect[s] == [nm]]
        L.append('  %-30s %-14s sources %s ; alone %s' % (nm, RA.RULE_OF.get(nm, '-'), ['b%s (%s)' % s for s in src] or 'no lettered defect cited by its row',
                                                        ['b%s (%s)' % s for s in alone] or 'NONE'))
    L += ['', '### the other standing arms -- the checks tool`s own (93 standing at b691 less these 24) -- carry no rules-bank row, so no source',
          '### defect is read for them here; their classes are the arms` own reads (each act`s checks tool), not a rule`s Source line.']
    L += ['', '### the series: rows are acts | defects lettered in the act`s bank | arms run in its pre-push suite:']
    L += ['  b%d  defects %2d  arms %s' % (a, n, k) for a, n, k in series_]
    half = len(series_) // 2
    lo, hi = series_[:half], series_[half:]
    mean = lambda xs: sum(xs) / len(xs) if xs else 0.0   # noqa: E731
    dl, dh = mean([n for _a, n, _k in lo]), mean([n for _a, n, _k in hi])
    al, ah = mean([k for _a, _n, k in lo if k]), mean([k for _a, _n, k in hi if k])
    fac = (dl / dh) if dh else None
    L += ['', '### the first half b%d-b%d: defects per act %.2f, arms per act %.1f ; the second half b%d-b%d: defects per act %.2f, arms per act %.1f' % (
        lo[0][0], lo[-1][0], dl, al, hi[0][0], hi[-1][0], dh, ah),
          '### a ratio of two means over a short series, not a fit and not a cause: the arms rose and the defects per act %s' % (
              'fell by the factor %.2f' % fac if fac and fac > 1 else ('did not fall (the factor %.2f)' % fac if fac else 'are not read')),
          '', '### ### **RULE ARMS %d ; WITH A SOURCE READ %d ; ANSWERING A DEFECT ALONE %d ; DEFECTS PER ACT %.2f -> %.2f AS ARMS %.1f -> %.1f ; THE FACTOR %s.**' % (
              len(RA.NAMES), sum(1 for v in rule_src.values() if v), sum(1 for nm in RA.NAMES if any(by_defect[s] == [nm] for s in rule_src.get(nm, []))),
              dl, dh, al, ah, ('%.2f' % fac) if fac else 'NOT READ')]
    put('b692_suite_load.txt', L)
    print(NL.join(L[-4:]))


if __name__ == '__main__':
    r, a = (sys.argv[1] if len(sys.argv) > 1 else ''), sys.argv[2:]
    fn = dict(read=read, dominance=dominance, controls=controls, shorts=shorts_route, readfirst=readfirst, suiteload=suiteload).get(r)
    if fn is None:
        print(__doc__)
        sys.exit(2)
    fn(*a)
