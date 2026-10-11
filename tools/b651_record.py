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


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn):
        sys.exit('usage: b651_record.py <route> [args]')
    fn(*sys.argv[2:])
