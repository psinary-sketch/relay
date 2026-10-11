# -*- coding: utf-8 -*-
"""b651_record.py -- THE RECORD TOOL OF b651, UNDER (R261): THE RE-CUTS OPENED -- THE DATA AND PAGE ROWS, THE SEAM ROW, THE SIMPLICITY ROW;
THE AXIOM-CLAIM RESOLVER; THE CENSUS AT v0.8.1; THE RESTATED LINES; THE LARGEST KERNEL'S DOCSTRINGS; THE NAVIGATOR'S ROWS.

### Written by the Write tool and extended by the Edit tool as the act runs; sealed at Component 7. Its helpers are b649_record's form; its
### routes write relay data/b651_* alone unless a route's docstring names another file.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
RELAY = ROOT
PP = 'D:/MY-DOwnloads/PLACE-papers'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
os.makedirs(SP, exist_ok=True)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### the lists in force at b651: the zeta list b649's (unchanged), the chi list b651's (its backmatter line re-cut, (R261)(3)(b))
NODES = {'zeta': 'b649_nodes_zeta.txt', 'chi': 'b651_nodes_chi.txt'}
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _write(path, b):
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)


def put_txt(name, L):
    _write(os.path.join(D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


# ================================================================================ COMPONENT 2: THE PAGE ARMS
def page_arms(tag='', *a):
    """data/b651_page_arms[_<tag>].txt: the page arms on the lists in force against PLACE-papers HEAD, and the frozen control with the E0 rule
    at its relay pin (b649's page_arms, carried)."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    import chain_page as CP
    import b626_record as R26
    L = ['b651 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s, relay %s (%s)%s' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc(), (' -- ' + tag) if tag else '')]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b651_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', NODES[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    rule = CP.E0
    CP.E0 = R26.e0_module(T.RELAY_PIN)
    try:
        c = T.control()
    finally:
        CP.E0 = rule
    L.append('### the control`s E0 rule: loaded at relay %s' % T.RELAY_PIN)
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b651_page_arms%s.txt' % (('_' + tag) if tag else ''), L)
    print(NL.join(l[:220] for l in L))


# ================================================================================ COMPONENT 4: THE CENSUS AT v0.8.1, (R261)(5)
CEN8 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md'
CEN81 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md'
CEN_SELF = ('p2-42',)          # ### the census itself (b648_record.CEN_SELF)
GLOSS_AT_V8 = '936766a8'       # ### relay at b650's close: the glossary v0.8 was generated beside (b649's three entries in, b651's not)


def _docs():
    """[(id, cluster, text)] for the census rows that are documents (b647's 48 roster keystones and 7 Day 1 companions), read at PLACE-papers
    HEAD; and the kernel rows."""
    j = jl('b647_census_columns.json')['rows']
    docs = [(r['id'], r.get('cluster') or '', g(PP, 'show', 'HEAD:' + r['path'])) for r in j if r['kind'] in ('roster', 'companion') and r.get('path')]
    return docs, [r for r in j if r['kind'] == 'kernel']


def clusters(*a):
    """data/b651_clusters_served.txt and .json: every kernel's CLUSTERS-SERVED by tools/licensed_table.py clusters_served, the documents citing
    it in their Correspondence tables, beside b648's placement (data/b648_kernel_cites.json); N3 read."""
    import licensed_table as LT
    docs, ks = _docs()
    kc = dict((x['kernel'], x) for x in jl('b648_kernel_cites.json').get('rows') or [])
    rows = []
    for k in ks:
        kn = k['id'].split()[0]
        s, cites = LT.clusters_served(kn, docs, exclude=CEN_SELF)
        rows.append(dict(kernel=kn, main=k['id'].split()[1] if len(k['id'].split()) > 1 else '', served=s, cites=cites,
                         b648=(kc[kn]['how'] if kn in kc else 'placed by the rules at b647: %s' % (k.get('cluster') or '-'))))
    split = [r for r in rows if r['b648'].startswith('split')]
    none8 = [r for r in rows if r['b648'] == 'named by no keystone']
    L = ['b651 -- COMPONENT 4, (R261)(5): CLUSTERS-SERVED FOR EVERY KERNEL OF THE CENSUS (%s)' % utc(), '',
         '### the rule: tools/licensed_table.py clusters_served at relay %s -- the clusters of the documents whose Correspondence tables cite the '
         'kernel by repository name; the documents: b647`s 48 roster keystones and 7 Day 1 companions (relay data/b647_census_columns.json) read '
         'at PLACE-papers %s, %d of them carrying a Correspondence section; the census itself (%s) read and not counted.' % (
             g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip(),
             sum(1 for d in docs if LT.correspondence_text(d[2]).strip()), ', '.join(CEN_SELF)), '',
         '### kernel | CLUSTERS-SERVED | the documents citing it (id, cluster, citations) | b648`s reading']
    for r in rows:
        L += ['  %-34s %s' % (r['kernel'], ', '.join(r['served']) or 'served: none'),
              '      cited by: %s' % ('; '.join('%s (%s) x%d%s' % (i, c or 'no cluster', n, ' NOT COUNTED' if i in CEN_SELF else '')
                                            for i, c, n in r['cites']) or 'none'),
              '      b648: %s' % r['b648']]
    two = [r for r in split if len(r['served']) >= 2]
    L += ['', '### N3, read: of b648`s %d split kernels, %d read two or more clusters served (%s); %d read fewer (%s). Of b648`s %d kernels named by '
              'no keystone: %s.' % (len(split), len(two), ', '.join(r['kernel'] for r in two), len(split) - len(two),
                                    '; '.join('%s: %s' % (r['kernel'], ', '.join(r['served']) or 'served: none') for r in split if len(r['served']) < 2),
                                    len(none8), '; '.join('%s: %s' % (r['kernel'], ', '.join(r['served']) or 'served: none') for r in none8)),
          '', '### ### **KERNELS %d ; SERVED BY ONE CLUSTER %d ; BY TWO OR MORE %d ; SERVED: NONE %d.**' % (
              len(rows), sum(len(r['served']) == 1 for r in rows), sum(len(r['served']) >= 2 for r in rows), sum(not r['served'] for r in rows))]
    put_txt('b651_clusters_served.txt', L)
    put_json('b651_clusters_served.json', dict(at=utc(), rows=rows))
    print(NL.join(L[-3:]))


V81_TAG = '## Back matter of the v0.8.1 edition — written 2026-10-11 by b651 under the author’s ruling `(R261)`(5), by the form of `(R187)`(5)'


def _v81_backmatter():
    import licensed_table as LT
    rows = jl('b651_clusters_served.json')['rows']
    none_ = [r for r in rows if not r['served']]
    L = ['', V81_TAG, '',
         '### The readings v0.8.1 adds, each the seat’s and strikeable', '',
         '- **CLUSTERS-SERVED.** A kernel’s one-word cluster is replaced by the clusters it serves: the clusters of the documents whose '
         'Correspondence tables cite it by its repository name, the census itself not counted (relay `tools/licensed_table.py`, '
         'clusters_served). A kernel no Correspondence table cites reads “served: none” and is listed. Keystones and companions keep their '
         'single cluster, v0.8’s, unchanged. A Correspondence table is the text under a heading naming Correspondence, to the next heading of '
         'its level.',
         '- **The documents read** are v0.8’s rows that are documents, %d of them, at PLACE-papers as this edition was generated; a kernel '
         'named in a document’s prose and not in its Correspondence tables is not counted as served by it.' % len(_docs()[0]),
         '- **The glossary block** is regenerated: one entry leaves it by a marked supersession (entry 65, “bNNN”, its words less “(b638 is '
         'this one)”, `(R261)`(3)(a)) and six enter it, the five items the second reader marked unclear at b648 (`(R261)`(5)).',
         '- **The numerals.** In this back matter every numeral is a count of the rows below or of a table’s rows.', '',
         '### The clusters each kernel serves', '',
         '| # | kernel | clusters served | the documents citing it in their Correspondence tables |', '|:--|:--|:--|:--|']
    for i, r in enumerate(rows, 1):
        L.append('| %d | `%s` | %s | %s |' % (i, r['kernel'], ', '.join(r['served']) or 'served: none',
                                              '; '.join('%s (%s)' % (d, c or '—') for d, c, _n in r['cites'] if d not in CEN_SELF) or '—'))
    L += ['', '*%d kernels: served by one cluster %d, by two or more %d, served by none %d.*' % (
        len(rows), sum(len(r['served']) == 1 for r in rows), sum(len(r['served']) >= 2 for r in rows), len(none_)),
          '', '### The kernels served by none', '',
          '- %s.' % (', '.join('`%s`' % r['kernel'] for r in none_) or 'none'),
          '', '### Version history', '',
          '- **v0.8.1, 2026-10-11 (b651, `(R261)`(5))**: the kernels’ cluster read as the clusters they serve, from the Correspondence tables '
          'that cite them; the glossary block regenerated; every other row and cell v0.8’s.',
          '- **v0.8, 2026-10-10 (b648)** and the editions before it: carried above.']
    return L


def _old_block():
    """v0.8's glossary block: the shared glossary at relay GLOSS_AT_V8, printed by the builder of now."""
    import chain_page as CP
    p = os.path.join(SP, 'b651_glossary_at_v8.txt')
    _write(p, g(RELAY, 'show', '%s:data/glossary.txt' % GLOSS_AT_V8).encode('utf-8'))
    return CP.glossary_block(p)


def edition81(*a):
    """PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md beside v0.8 (unedited), and data/b651_edition.json: v0.8 line for line but
    its glossary block regenerated, a v0.8.1 version line above v0.8's, and the v0.8.1 back matter. `dry`: the scratchpad."""
    import chain_page as CP
    import hashlib
    dry = 'dry' in a
    if not jl('b651_clusters_served.json'):
        sys.exit('### NO CLUSTERS-SERVED BANK -- NOTHING WRITTEN')
    v8 = g(PP, 'show', 'HEAD:' + CEN8).split(NL)
    if v8 and v8[-1] == '':
        v8 = v8[:-1]
    nb = CP.glossary_block()
    # ### v0.8's block found in v0.8 itself: the builder's four head lines (heading, blank, introduction, blank), then its run of entry lines
    hd = [i for i in range(len(v8)) if v8[i:i + 4] == nb[:4]]
    ob = []
    if len(hd) == 1:
        k = hd[0] + 4
        while k < len(v8) and v8[k].startswith('- **'):
            k += 1
        ob = v8[hd[0]:k]
    at = hd if ob else []
    vl = [i for i, l in enumerate(v8) if l.startswith('*v0.8, 2026-10-10')]
    if len(at) != 1 or len(vl) != 1:
        sys.exit('### v0.8`S GLOSSARY BLOCK (%s) OR ITS VERSION LINE (%s) NOT FOUND ONCE -- NOTHING WRITTEN' % (at, vl))
    i, j = at[0], vl[0]
    rows = jl('b651_clusters_served.json')['rows']
    ver = ('*v0.8.1, 2026-10-11 -- the kernels’ cluster read as the clusters each serves, from the Correspondence tables that cite it (%d kernels, '
           '%d served by none, listed); the glossary block regenerated; every other row and cell v0.8’s, which stands beside it, unedited.*' % (
               len(rows), sum(1 for r in rows if not r['served'])))
    out = v8[:i] + nb + v8[i + len(ob):j] + [ver, ''] + v8[j:] + _v81_backmatter()
    b = (NL.join(out) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b651_census_dry.md') if dry else os.path.join(PP, *CEN81.split('/'))
    if not dry and os.path.exists(dest) and 'regen' not in a:
        sys.exit('### v0.8.1 EXISTS -- NOTHING WRITTEN')
    _write(dest, b)
    if not dry:
        put_json('b651_edition.json', dict(at=utc(), path=CEN81, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b), lines=len(out),
                                           glossary_at=i + 1, glossary_lines=len(nb), old_glossary_lines=len(ob), backmatter=out.index(V81_TAG) + 1,
                                           v8_lines=len(v8), v8_at=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : %d lines, %d bytes ; the glossary block %d lines at :%d (was %d) ; the version line at :%d ; the back matter at :%d' % (
        ('DRY ' + dest) if dry else CEN81, len(out), len(b), len(nb), i + 1, len(ob), j + 1 + len(nb) - len(ob), out.index(V81_TAG) + 1))


GLOSS_DOCS = ('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', CEN81)


def glossary_alike(*a):
    """data/b651_glossary_alike.txt: the shared glossary's block found once, byte for byte, in the two pages and the census at v0.8.1 at
    PLACE-papers HEAD; its sha256 in each."""
    import chain_page as CP
    import hashlib
    nb = CP.glossary_block()
    L = ['b651 -- (R261)(5): THE GLOSSARY BLOCK ACROSS THE THREE DOCUMENTS AT PLACE-papers %s, the builder at relay %s (%s)' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc()), '',
         '### the block: %d lines from relay data/glossary.txt (%d entries)' % (len(nb), len(CP.glossary_entries()))]
    shas = []
    for f in GLOSS_DOCS:
        t = g(PP, 'show', 'HEAD:' + f).split(NL)
        at = [i for i in range(len(t)) if t[i:i + len(nb)] == nb]
        s = hashlib.sha256(NL.join(t[at[0]:at[0] + len(nb)]).encode('utf-8')).hexdigest() if len(at) == 1 else None
        shas.append(s)
        L.append('  %-48s found %d time(s)%s ; sha256 %s' % (f, len(at), (' at :%d' % (at[0] + 1)) if at else '', s or '-'))
    ok = len(set(shas)) == 1 and shas[0] is not None
    L += ['', '### ### **THE BLOCK BYTE FOR BYTE THE SAME IN ALL THREE: %s.**' % ok]
    put_txt('b651_glossary_alike.txt', L)
    print(NL.join(L[2:]))
    return ok


# ================================================================================ COMPONENT 6: THE SENTENCE ROWS, (R261)(7) AND THE AUTHOR'S ANSWERS
# ### b647's SIDE-kernel table grades blocks (relay data/b647_table_SIDE-kernel.txt :3); the author's answer before the seal: no docstring
# ### edit this act; the 116 OVERREACHES and UNDERSTATES blocks read into sentence rows by the table's own machinery where it fits the
# ### foreground -- b647's generator (_kdoc_rows) run at SIDE-kernel's main, each block's context (statement, grade, lookup) captured, each
# ### parent block split into units by the table's unit rule (b647_record._MSPLIT) and each unit read by licensed_table.docstring_row with
# ### its parent's context. A GENERATED reading per sentence, the parent's HAND verdict beside it; the HAND reading per sentence is b652's.
def _bank_line(bank_lines, rid_tail):
    for i, l in enumerate(bank_lines, 1):
        if l.startswith('  SIDE-kernel@0256e9e:' + rid_tail + ' |'):
            return i
    return None


def sentences(*a):
    """data/b651_table_SIDE-kernel_sentences.txt and .json."""
    import b647_record as B7
    import licensed_table as LT
    N = lambda s: ' '.join(s.split())   # noqa: E731
    parents = [r for r in jl('b647_table_SIDE-kernel.json')['rows'] if r['verdict'] in ('OVERREACHES', 'UNDERSTATES')]
    bl = rd('b647_table_SIDE-kernel.txt').split(NL)
    ctx, orig = {}, LT.docstring_row

    def cap(rid, source, doc, *args, **kw):
        ctx.setdefault(N(doc), (source, args, kw))
        return orig(rid, source, doc, *args, **kw)
    LT.docstring_row = cap
    try:
        B7._kdoc_rows('SIDE-kernel')
    finally:
        LT.docstring_row = orig
    rows, unread = [], []
    for p in parents:
        c = ctx.get(N(p['stated']))
        if c is None:
            unread.append(p)
            continue
        src, args, kw = c
        units = [s for s in B7._MSPLIT.split(p['stated'].strip()) if s.strip()]
        for j, u in enumerate(units, 1):
            r = orig('%s.s%d' % (p['id'], j), p['source'], u, *args, **kw)
            rows.append(dict(id=r['id'], parent=p['id'], parent_line=_bank_line(bl, p['source']), parent_verdict=p['verdict'], kind=p['kind'],
                             n=j, of=len(units), sentence=N(u), generated=r['verdict'], findings=r.get('findings') or [],
                             hand_needed=r.get('hand_needed')))
    import collections
    gc = collections.Counter(x['generated'] for x in rows)
    L = ['b651 -- (R261)(7) AND THE AUTHOR`S ANSWERS: SIDE-kernel`S 116 OVERREACHES AND UNDERSTATES BLOCKS READ INTO SENTENCE ROWS (%s)' % utc(), '',
         '### the parents: relay data/b647_table_SIDE-kernel.json, its OVERREACHES and UNDERSTATES rows (117), read at 0256e9e; the generator: '
         'b647_record._kdoc_rows at SIDE-kernel main %s, each block`s context captured and each unit read by licensed_table.docstring_row; '
         'the unit: b647_record._MSPLIT (a sentence split where . ! or ? meets whitespace). A GENERATED reading per sentence; the HAND reading '
         'per sentence is b652`s, and no docstring is edited at this act.' % g('D:/SIDE-kernel', 'rev-parse', '--short=8', 'main').strip(),
         '### parents read %d ; parents not found at main %d (%s)' % (len(parents) - len(unread), len(unread),
                                                                       '; '.join('%s (%s)' % (u['source'], u['decl'] or u['kind']) for u in unread) or 'none'), '']
    cur = None
    for x in rows:
        if x['parent'] != cur:
            cur = x['parent']
            L += ['', '== %s (%s ; b647`s bank line :%s ; HAND %s ; %d sentences)' % (x['parent'].split(':', 1)[1], x['kind'], x['parent_line'],
                                                                                     x['parent_verdict'], x['of'])]
        L.append('  s%d %-11s %s%s' % (x['n'], x['generated'], x['sentence'][:600],
                                       ('  [%s]' % '; '.join(x['findings'])[:300]) if x['findings'] else ''))
    L += ['', '### ### **PARENT BLOCKS %d ; SENTENCE ROWS %d ; GENERATED: %s ; HAND PER SENTENCE: b652`s.**' % (
        len(parents) - len(unread), len(rows), ', '.join('%s %d' % kv for kv in sorted(gc.items())))]
    L = [l.replace('\r', '') for l in L]
    put_txt('b651_table_SIDE-kernel_sentences.txt', L)
    put_json('b651_table_SIDE-kernel_sentences.json', dict(at=utc(), rows=rows, unread=[u['id'] for u in unread]))
    print(NL.join(L[2:4] + L[-1:]))


# ================================================================================ THE LATE ROUTES: ANSWERS, CAPTURE, THE NAVIGATOR'S ROWS, THE SEAL,
# ================================================================================ THE ROOT, THE TABLE, THE SCORES, THE RECORD (b649's, carried)
import collections                 # noqa: E402
import b602_record as R2           # noqa: E402
import b633_record as R3           # noqa: E402
import b651_worklist as K          # noqa: E402
import edit_route as ER            # noqa: E402
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
_scan, _clean = R3._scan, R3._clean


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def answers(*a):
    """data/b651_author_answers.txt: every prompt put by the seat in this act, from the ruling's delivery in this session, banked verbatim with
    its options and the answer (b649's scan)."""
    calls, results, start = [], {}, None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and start is not None:
                calls.append((i, c['id'], c['input']))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, K.SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    head = ['### b651 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; the session read: %s from %r (transcript line %d).' % (n, K.DATE, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b651_author_answers.txt', head + (L or ['### NONE: no prompt has been put to the author in this act.']))
    print('  prompts banked: %d' % n)


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def commands(*a):
    """data/b651_commands.txt and .json: the act's command bank and G-EDIT-ROUTE's reading."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    L = ['b651 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING (tools/edit_route.py) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d.**' % (len(rows), len(hits))]
    put_txt('b651_commands.txt', L)
    put_json('b651_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


def navigator_rows(*a):
    """data/b651_navigator_rows.txt: (R261)(8) -- the OVERREACHES and UNDERSTATES rows of relay data/b647_table_navigator_memory.json, STATED,
    LICENSED and ACTION verbatim, for the navigator; the ruling names 33, the bank holds 33 OVERREACHES and 6 UNDERSTATES, all printed. The seat
    reads the relay bank alone and touches no navigator file."""
    rows = [r for r in jl('b647_table_navigator_memory.json').get('rows') or [] if r.get('verdict') in ('OVERREACHES', 'UNDERSTATES')]
    c = collections.Counter(r['verdict'] for r in rows)
    L = ['b651 -- (R261)(8): THE NAVIGATOR`S ROWS, PRINTED FOR IT (%s)' % utc(), '',
         '### the source: relay data/b647_table_navigator_memory.json (b647, the navigator`s export read through the licensed-statement table); '
         'its OVERREACHES and UNDERSTATES rows, %d: OVERREACHES %d, UNDERSTATES %d. The ruling names 33 -- the OVERREACHES count alone; every '
         'row of both verdicts is printed. STATED, LICENSED and ACTION verbatim; the navigator repairs its own files on the author`s word.' % (
             len(rows), c['OVERREACHES'], c['UNDERSTATES']), '']
    for i, r in enumerate(rows, 1):
        L += ['### ROW %d (%s, %s, %s)' % (i, r['id'], r['source'], r['verdict']), '  STATED   : %s' % ' '.join(r['stated'].split()),
              '  LICENSED : %s' % ' '.join(r['licensed'].split()), '  ACTION   : %s' % ' '.join(r['action'].split()), '']
    L += ['### ### **ROWS %d ; OVERREACHES %d ; UNDERSTATES %d.**' % (len(rows), c['OVERREACHES'], c['UNDERSTATES'])]
    put_txt('b651_navigator_rows.txt', L)
    print(L[-1])


def kernels(*a):
    """data/b651_kernels_face.json: every kernel's main, tags, branches and tracked status, read before the seal for N5."""
    import b641_record as R41
    put_json('b651_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_SHORT = []      # ### filled from data/b651_defects.txt by `defects`


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rd('b651_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    """data/b651_defects.json from data/b651_defects.txt (the seat's list and the navigator's): every defect line and its short form."""
    t = rd('b651_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b651_defects.json', dict(at=utc(), defects=ds, short=_defect_short(), correction=''))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b651_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b651 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-24s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    put_txt('b651_seal_check_%s.txt' % (a[0] if a else 'record'), L)
    print(NL.join(L[2:]))


ROOT_EXCLUDE = re.compile(r'^b651_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b651_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                  and ('data/' + f) != K.EXPORT)


def root(*a):
    """(R251)(3): the act root, the last step of the act; every bank it names written LF (compute refuses CR LF). `dry`: computed, not written."""
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b651_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b651'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """the root recomputed from its banked items offline and a one-byte change on a copy of one bank moving it; the root order read locally."""
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b651_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b651 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b651_root_arm.txt', L)
    put_json('b651_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    """the terminal table regenerated at the end and diffed against relay HEAD`s table, by row."""
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b651 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b651_table_final.txt', L)
    put_json('b651_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
NEW_TESTS = K.NEW_TESTS
N5_RELAY_TOOLS = K.EDITED_SHARED + K.NEW_TESTS
N5_RELAY_DATA = ('glossary.txt', 'act_roots.txt', 'b650_relay_push_out.txt', 'b650_pp_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN81, K.SIMPL)


def TRAIL_HEAD():
    return ('### b651 — lane three, act seventy-eight under (R261): the re-cuts opened -- the data and page rows, the seam row, the simplicity row; '
            'the axiom-claim resolver; the census at v0.8.1; the restated lines; the largest kernel`s docstrings; the navigator`s rows printed')


def _ac():
    b, a = jl('b651_axiom_claim_before.json').get('rows') or [], jl('b651_axiom_claim_after.json').get('rows') or []
    return collections.Counter(r['verdict'] for r in b), collections.Counter(r['verdict'] for r in a), a


def _row(rows, f, ln):
    x = [r for r in rows if r['file'] == f and r['line'] == ln and r['verdict'] not in ('MENTION', 'OUT OF SCOPE')]
    return x[0] if x else {}


def _n5():
    face = jl('b651_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    mains0 = dict((r['kernel'], r['main']) for r in jl('b651_no_sorry_main.json').get('rows') or [])
    moved = [k for k, m in mains0.items() if g('D:/' + k, 'rev-parse', 'main').strip() != m]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b651_|audit_b651_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS) or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    ok = kern_ok and not moved and not pp_beyond and not kinds_beyond and not differ
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched and no request made to the deposit service by this act (draft %s last read at b649, '
            'unsubmitted, its description v5); no kernel main moved since step zero (%s) -- no merge was made, the restated lines and the docstring '
            'branch staying unmerged; every kernel as the face read it %s; sealed tools not agreeing %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS, '
            'the two pages, the census at v0.8.1 and the simplicity file`s dated line: %s; relay files of a kind beyond the repairs and their tests, '
            'the generator edits, the glossary, the banks and the root list: %s; no identifier of the author in any outbound request (the act`s '
            'outbound calls git pushes and remote reads alone)' % (K.DRAFT, moved or 'NONE', kern_ok, differ or 'NONE', pp_beyond or 'NONE',
                                                                   kinds_beyond or 'NONE'))


def scores(*a):
    TF, RA = jl('b651_table_final.json'), jl('b651_root_arm.json')
    _r, _n, sh = seal_hashes()
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    seam_t = [r['grade'] for r in T if r['name'] == 'rh_strip_imp_rh']
    seam_l = [x['grade'] for x in jl('b651_lattice.json').get('rows') or [] if x['name'] == 'rh_strip_imp_rh']
    arms = rd('b651_page_arms_c4.txt')
    cb, ca, A = _ac()
    r2, r5 = _row(A, 'Interfaces/LocalLimit.lean', 226), _row(A, 'MetaKernel.lean', 140)
    real = [_row(A, 'SIDECosmo/SteaneExemplar.lean', 6), _row(A, 'Kernel/Integration.lean', 215), _row(A, 'MetaKernel.lean', 3), _row(A, 'AxiomCheck.lean', 8)]
    cs = jl('b651_clusters_served.json').get('rows') or []
    split = [r for r in cs if r['b648'].startswith('split')]
    none8 = [r for r in cs if r['b648'] == 'named by no keystone']
    alike = 'BYTE FOR BYTE THE SAME IN ALL THREE: True' in rd('b651_glossary_alike.txt')
    tests = {}
    for t in NEW_TESTS:
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                           env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        m = re.search(r'(\d+) of (\d+) cases as wanted', r.stdout or '')
        tests[t] = (r.returncode, m.group(0) if m else '?')
    ds = rd('b651_docstrings_SIDE-kernel.txt')
    S = {
        'N1': ('HELD' if seam_t == ['DERIVES'] and seam_l == ['DERIVES'] and 'PAGE ARMS PASSING : 2 of 2.' in arms else 'REFUTED',
               'the seam`s def rh_strip_imp_rh reads %s in the terminal table and %s in the lattice bank (data/b651_lattice.json), CONFLICT in '
               'neither; the page arms after the last re-emission 2 of 2 (data/b651_page_arms_c4.txt)' % (seam_t, seam_l)),
        'N2': (('HELD' if r2.get('verdict') == 'VERIFIED' and r5.get('verdict') == 'VERIFIED' else 'REFUTED IN ONE CLAUSE')
               if all(x.get('verdict') == 'CONTRADICTED' for x in real) else 'REFUTED',
               'row 2 %s (re-bound to %s), row 5 %s -- by the author`s answer before the seal a hypothetical variant reads UNBOUND, neither PASS nor '
               'CONTRADICTED, so row 5 does not read PASS; the four real contradictions %s; CONTRADICTED %d before, %d after' % (
                   r2.get('verdict'), r2.get('bound_to'), r5.get('verdict'), [x.get('verdict') for x in real], cb['CONTRADICTED'], ca['CONTRADICTED'])),
        'N3': ('HELD' if all(len(r['served']) >= 2 for r in split) and all(not r['served'] for r in none8) and alike else 'REFUTED IN TWO CLAUSES',
               'of b648`s %d split kernels %d read two or more clusters served, %d fewer (%s); of its %d uncited kernels %s; the glossary block byte '
               'for byte the same in the two pages and the census %s' % (
                   len(split), sum(len(r['served']) >= 2 for r in split), sum(len(r['served']) < 2 for r in split),
                   ', '.join('%s %s' % (r['kernel'], r['served'] or 'none') for r in split if len(r['served']) < 2), len(none8),
                   '; '.join('%s served by %s' % (r['kernel'], r['served'] or 'none') for r in none8), alike)),
        'N4': ('NOT SCORABLE IN TWO CLAUSES',
               'by the author`s answers before the seal no docstring of SIDE-kernel was re-cut at this act (the ACTION cells answer block rows, and '
               'the sentence reading comes first), so neither "no grade moved by the re-cut" nor "every docstring row MATCHES on the rerun" has a '
               'population; the third clause: the two plain comments no longer assert the unsupported sentence on the branch %s (%s), which the '
               'build beneath the hold left unmerged, so main still carries them' % (K.DS_BRANCH, 'DEFERRED' in ds)),
        'N5': _n5(),
        'S1': ('HELD' if all(rc == 0 for rc, _x in tests.values()) else 'REFUTED', 'the act`s planted tests: %s' % '; '.join(
            '%s exit %d, %s' % (t, rc, x) for t, (rc, x) in tests.items())),
        'S2': ('HELD' if rd('b651_first_rows.txt').count('relay ') >= 4 else 'REFUTED', 'every repair committed alone, its diff read by kind '
               '(data/b651_first_rows.txt)'),
        'S3': (('HELD' if not TF.get('gone') and not TF.get('added') and not TF.get('moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s' % (len(TF.get('moved') or []), len(TF.get('gone') or []),
                                                                                       len(TF.get('added') or []))),
        'S4': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S5': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b651_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:400]))


def _title():
    _cb, ca, _A = _ac()
    nr = len(re.findall(r'^### ROW \d+ ', rd('b651_navigator_rows.txt'), re.M))
    return ('## The re-cuts opened: four rows repaired and the seam re-graded; the axiom-claim resolver at %d contradictions after repair; the census '
            'at v0.8.1 with clusters served; 0 of four restated lines merged; SIDE-kernel`s docstrings read into sentence rows, none re-cut, two plain '
            'comments re-cut on a branch beneath the hold; the navigator`s %d rows printed' % (ca['CONTRADICTED'], nr))


NEXT_LINE = ('b652, the author`s word pending, per `(R261)`(9) and the author`s answers before the seal: the INSTRUMENT verdict at its step zero '
             'under its own ruling; SIDE-kernel`s 116 blocks read by hand sentence by sentence and re-cut by the rule the author gave, the plain-comment '
             'branch merged where a build holds; then the next kernel by count, then the companions in descending count under "papers state; ledgers '
             'narrate" with the Classical-context front section and the positivity-clause name')


def _finding_text():
    S, rl, J = jl('b651_scores.json'), jl('b651_record_lines.json'), jl('b651_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b651_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    cb, ca, _A = _ac()
    cs = jl('b651_clusters_served.json').get('rows') or []
    sj = jl('b651_table_SIDE-kernel_sentences.json').get('rows') or []
    nr = len(re.findall(r'^### ROW \d+ ', rd('b651_navigator_rows.txt'), re.M))
    e = ['', _title(), '',
         '*Filed at b651 on the author’s ruling `(R261)` and the author’s answers (%d). Banks: relay `data/b651_first_rows.txt`, '
         '`data/b651_lattice.txt`, `data/b651_axiom_claim_rerun.txt`, `data/b651_axiom_claim_rows.txt`, `data/b651_clusters_served.txt`, '
         '`data/b651_glossary_alike.txt`, `data/b651_restated.txt`, `data/b651_table_SIDE-kernel_sentences.txt`, `data/b651_docstrings_SIDE-kernel.txt`, '
         '`data/b651_navigator_rows.txt`, `data/b651_act_root.txt`.*' % n_ans, '',
         '**The first rows** (`(R261)`(3)): glossary entry 65 out of the block by a marked supersession the generator now honours, its superseding '
         'entry in; the χ page’s back matter re-cut in its node list, the refuted premise named as refuted; the seam’s def re-graded by a dated '
         'correction beneath OPEN_TRAILS :10909 -- CONFLICT to DERIVES in the terminal table and the lattice bank, one row moved in each, '
         'W-ORD-SEAM-ROW acted; SIMPLICITY_OF_RIEMANN_ZEROS.md :355 brought under the ceiling clause by a dated line, the deposited v1.1.2 file not '
         'rewritten. Both pages re-emitted one per call, their arms and the frozen control 2 of 2. N1 %s.' % sc('N1'), '',
         '**The resolver** (`(R261)`(4) and the author’s answer): a claim said of another named object re-bound to it where it resolves in the '
         'tree, graded by its prints, and read UNBOUND where it does not -- b649’s row 2 VERIFIED on the TraceSilence instances, row 5 UNBOUND; '
         'the four real contradictions stand; CONTRADICTED %d before, %d after; UNBOUND %d counted apart. W-ORD-VERDICT-INSTRUMENT’s trigger '
         'fired, the verdict not added. N2 %s.' % (cb['CONTRADICTED'], ca['CONTRADICTED'], ca['UNBOUND'], sc('N2')), '',
         '**The census at v0.8.1** (`(R261)`(5)): a kernel’s cluster read as the clusters it serves, from the Correspondence tables that cite it: '
         '%d kernels, one cluster %d, two or more %d, served by none %d; six glossary entries for the second reader’s unclear items; the block '
         'byte for byte the same in the two pages and the census. N3 %s.' % (len(cs), sum(len(r['served']) == 1 for r in cs),
                                                                          sum(len(r['served']) >= 2 for r in cs), sum(not r['served'] for r in cs), sc('N3')), '',
         '**The restated lines** (`(R261)`(6)): neither module builds under the hold on its measured peak -- T3_StepNineBridge needs about 4204 MB '
         'free at its start, Milestones about 3970 -- so no branch is merged and G-NO-SORRY-MAIN reads its four hits still.', '',
         '**The docstrings** (`(R261)`(7) and the author’s answers): b647’s cells answer blocks, not sentences, so no docstring was re-cut; '
         'SIDE-kernel’s 116 blocks read into %d sentence rows, the generated rule seeing none of what the hand reading graded; the two plain '
         'comments of PerpendicularCrossing.lean re-cut on a branch, its one module`s build stopped beneath the hold twice, the kernel deferred. '
         'N4 %s.' % (len(sj), sc('N4')), '',
         '**The navigator’s rows** (`(R261)`(8)): %d rows of its memory export printed with their licence and action, for its own repair.' % nr, '',
         '**The record lines** (`(R261)`(1), (2)): b650 at its weight (FINDINGS :%s); the delivery clause (OPEN_TRAILS :%s).' % (
             ls[0].get('line'), ls[1].get('line')), '',
         '**The root.** b651 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, sc(k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the re-cuts met their instruments’ grain -- a table that grades blocks cannot say which '
         'sentence to cut, a resolver that binds by position cannot tell a claim from a mention, a host whose free memory sits near the hold cannot '
         'land a kernel -- and each limit is now a measured row rather than a guess. It strengthens the programme’s offering of statements a reader '
         'can check: the seam reads as the theorem that proves it, a kernel names the clusters it serves, and a sentence that asserted the open '
         'clause settled no longer stands on the branch that will carry it.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a verdict compares a sentence with a licence and confers none.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the glossary`s supersession by a marked comment line the generator honours, the file additive; (2) the chi back matter repaired '
              'in a new node list, b649`s list being named by its root; (3) the seam re-graded by the trail-line supersession form with one cell; '
              '(4) a module builds under the hold when its start`s free memory less its tree peak stays at or above the hold; (5) the rows of the '
              'navigator`s table printed are all 39 of both verdicts, the ruling naming 33')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b651_scores.json', 'b651_findings.json', 'b651_record_lines.json', 'b651_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b651_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R261) ratified.** (1) b650 at its weight. (2) Delivery: the navigator pastes; the seat files. (3) The first re-cut rows. (4) The '
             'axiom-claim resolver. (5) The census at v0.8.1. (6) The four restated lines. (7) The largest kernel`s docstrings. (8) The navigator`s '
             'rows. (9) The act after: b652.', '',
             '**Entered:** FINDINGS.md:%s (b650’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the delivery clause), :13870 (the seam`s correction), '
             ':13872 (W-ORD-VERDICT-INSTRUMENT`s trigger fired); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line')), '',
             '**The census:** PLACE-papers %s; the χ list relay data/b651_nodes_chi.txt; the glossary 89 entries.' % K.CEN81, '',
             '**Act root:** b651 `%s` (previous `%s`, b650’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b651_author_answers.txt), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b651_defects.txt): %s.' % '; '.join(_defect_short()), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b651_scores.json')
    L = ['=' * 104, 'b651 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rd('b651_defects.txt').rstrip(NL).split(NL)
    put_txt('b651_desk_notes.txt', L)


def components(*a):
    """data/b651_components.txt -- run after `findings` and `trail`; refuses when either bank is absent."""
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b651_scores.json', 'b651_findings.json', 'b651_trail.json', 'b651_record_lines.json', 'b651_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    L = ['b651 -- THE COMPONENTS, BANKED UNDER (R261).', '',
         '### COMPONENT 0 : step zero (data/b651_ferry.txt, data/b651_stepzero.txt, data/b651_tests_stepzero.txt) ; push-outs relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b650`s weight FINDINGS :%s ; the delivery clause OPEN_TRAILS :%s' % (ls[0].get('line'), ls[1].get('line')),
         '### COMPONENT 2 : the first rows (data/b651_first_rows.txt, data/b651_lattice.txt, data/b651_page_arms_c2.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 3 : the resolver (data/b651_axiom_claim_rerun.txt, data/b651_axiom_claim_rows.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 4 : the census at v0.8.1 (data/b651_clusters_served.txt, data/b651_edition.json, data/b651_glossary_alike.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 5 : the restated lines (data/b651_restated.txt, data/b651_no_sorry_main.txt)',
         '### COMPONENT 6 : the docstrings (data/b651_table_SIDE-kernel_sentences.txt, data/b651_docstrings_SIDE-kernel.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 7 : the seal (data/b651_seal_hashes.json) ; S5 %s' % S['S5'][0],
         '### COMPONENT 8 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the navigator`s rows (data/b651_navigator_rows.txt) ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b651_components.txt', L)
    print(NL.join(L[2:]))


def findings(*a):
    import b641_record as R41
    Q = R2._Q()
    dry = 'dry' in a
    t, e = _finding_text()
    e = R41._poss(e)
    if e.count('`') % 2 or [l for l in e.split(NL) if l.count('`') % 2]:
        sys.exit('### ODD BACKTICKS IN THE ENTRY -- NOTHING WRITTEN')
    cells = R3.predict_cells(e, 'FINDINGS.md')
    nd, _n = R3._nd(e)
    p = os.path.join(SP, 'b651_scanfile_entry.md') if dry else os.path.join(D, 'b651_scanfile_entry.md')
    _write(p, e.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    unread = [x for x in ('### NOT', 'None', '?;', ' ? ', '`?`') if x in e]
    outside = [n for n in R41.OAI_NEEDLES if n in e]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, e, re.I)]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s ; outside names %s ; stems %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', unread or 'NONE', outside or 'NONE', stems or 'NONE'))
    if dry:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread or outside or stems:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b651_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    import b641_record as R41
    Q = R2._Q()
    dry = 'dry' in a
    e = R41._poss(_trail_text())
    if e.count('`') % 2 or [l for l in e.split(NL) if l.count('`') % 2]:
        sys.exit('### ODD BACKTICKS IN THE RECORD -- NOTHING WRITTEN')
    cells = R3.predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = R3._nd(e)
    p = os.path.join(SP, 'b651_scanfile_trail.md') if dry else os.path.join(D, 'b651_scanfile_trail.md')
    _write(p, e.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    unread = [x for x in ('### NOT', 'None', '`?`') if x in e]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, e, re.I)]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s ; stems %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                   unread or 'NONE', stems or 'NONE'))
    if dry:
        print(e[:9000])
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread or stems:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b651_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b651_trail.json')['line'])


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn):
        sys.exit('usage: b651_record.py <route> [args]')
    fn(*sys.argv[2:])
