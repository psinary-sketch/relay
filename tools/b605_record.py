# -*- coding: utf-8 -*-
"""b605_record.py -- THE ACT'S RECORD TOOL, UNDER (R215). ### ONE SUBCOMMAND PER BANK.

### ### b605: LANE THREE, ACT THIRTY-TWO -- THE SIEVE TABLE AT v0.3: THE VERDICT COLUMN RE-READ WITH NOT A ROUTE AS A THIRD
### VERDICT AND THE FACES OF ONE CLAUSE UNDER ONE VERDICT.
### Subcommands write only `data/b605_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to`. The rows are tools/b604_rows.py's data and b604_record's cell writers, imported; the v0.3 verdicts are
### tools/b605_verdicts.py's data. No platform call. No Lean call: both pages are re-emitted from their banked probes.
"""
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b604_rows as W  # noqa: E402
import b605_verdicts as V  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
GSK = 'D:/SIDE-global-section'
RELAY = ROOT.replace('\\', '/')
PRE_PP = 'c7d3d48'
PRE_RELAY = '3651a663'
PRE_KER = '1d5d4dd'
PRE_GS = '3528bcf'
STEPZERO = '61594b11'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/c780ded1-4e24-4686-94a2-dbeb16d65f7a/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/c780ded1-4e24-4686-94a2-dbeb16d65f7a.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'
ED2 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'
ED = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc, flat = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc, R2.flat
_show = R4._show


DEFECTS = []
DEFECT_SHORT = []


def defects():
    L = ['b605 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b605_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('THE_FINDINGS_AS_THEY_STAND v0.2 whole (every non-blank line): the head, every row`s verdict and test, the FACE candidates, the bench',
     PP, PRE_PP, ED2, 'ALL', 400),
    ('relay data/b604_sieve_mapping.txt: its head, its parts` headings and PART D (the counts)', RELAY, 'HEAD', 'data/b604_sieve_mapping.txt',
     [1, 2, 3, '### THE FIVE TESTS', '### THE SIEVE:', '### PART A', '### PART B', '### PART C', '### PART D', '  conclusions of the current version',
      '  of them own', '  rows : 84', '  rows from the current', '  BRIGHT 6', '### ### **H38c'], 400),
    ('relay data/b604_author_answers.txt (whole)', RELAY, 'HEAD', 'data/b604_author_answers.txt', 'ALL', 400),
    ('the ζ page: its pin line and the iff-faces` nodes, names and pins', PP, PRE_PP, PAGE, [3, 11, 12, 14, 15, 24, 38, 41, 42], 260),
    ('the χ page: its pin line and the χ, schema and family faces` nodes', PP, PRE_PP, DIR_PAGE, [3, 16, 19, 20, 22, 27], 260),
    ('Keiper.lean at v0.20: λ₁`s closed form', EFK, 'v0.20', 'SIDEExplicitFormula/Keiper.lean', [238, 239, 240], 300),
    ('KeiperSign.lean at v0.20: liCoeff_one_pos (it lives here, not in Keiper.lean)', EFK, 'v0.20', 'SIDEExplicitFormula/KeiperSign.lean',
     [81, 82, 83], 300),
    ('Keiper.lean at v0.20: the Keiper face, λ_n from the Stieltjes side on named obligations', EFK, 'v0.20', 'SIDEExplicitFormula/Keiper.lean',
     [112, 133], 300),
    ('DetectionRegion.lean at v0.21: the finite-support rungs and the forall_upto pair', EFK, 'v0.21', 'SIDEExplicitFormula/DetectionRegion.lean',
     [29, 33, 37, 47, 52], 300),
    ('OPEN_TRAILS: the form`s block and its H28b and re-pin clauses, the page and restatement clauses, b604`s work-order and record',
     PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 11902, 11930, 11932, 12190, 12192, 12436, 12438, 12440], 700),
    ('FINDINGS: b604`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [7056, 7058, 7060], 600),
    ('relay data/b604_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b604_closing_push_out.txt', 'ALL', 260),
]


def reads():
    L = ['b605 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = t.split(NL)
        if sl and sl[-1] == '':
            sl = sl[:-1]
        if sel == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        else:
            nums = []
            for n in sel:
                if isinstance(n, str):
                    hit = [i + 1 for i, l in enumerate(sl) if l.startswith(n)]
                    nums.append(hit[0] if hit else -1)
                else:
                    nums.append(n)
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the pages` pins: the ζ page`s list %s %s ; the χ page`s list %s %s -- the ferry`s "THE_CLAUSE_AND_ITS_COMPILED_FACES.md at '
          'v0.21" read at the ζ page`s own pin v0.20, a fact correction recorded as the navigator`s (as at b604)' % (
              NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
              [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
          '### the ferry`s "Keiper.lean`s λ₁ closed form and liCoeff_one_pos at v0.20": the closed form `liCoeff_one_keiper` is in '
          'Keiper.lean, `liCoeff_one_pos` in KeiperSign.lean (both at v0.20 = %s), a fact correction recorded as the navigator`s' % (
              g(EFK, 'rev-parse', '--short=7', 'v0.20^{commit}').strip()),
          '### v0.2 at HEAD equals v0.2 at %s : %s' % (PRE_PP, g(PP, 'rev-parse', 'HEAD:' + ED2).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, ED2)).strip())]
    put_txt('b605_reads.txt', L)


# ================================================================================ THE AUTHOR'S ANSWERS
def answers():
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if c.get('type') == 'tool_result':
                    t = c.get('content')
                    t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                    results[c.get('tool_use_id')] = (i, t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b605 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session c780ded1-4e24-4686-94a2-dbeb16d65f7a, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act; the precedence order and the ruling`s letter reached every '
                 'reading, each declared on the face and strikeable.')
    put_txt('b605_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B604_ENTRY = '## The edition of THE_FINDINGS_AS_THEY_STAND as the sieve table by cluster'
W_HEAD = '*Appended 2026-10-03 by b605 to b604’s entry (:%d), under `(R215)`(1) -- b604 AT ITS WEIGHT:*'
C_HEAD = '*Appended 2026-10-03 by b605 to b604’s entry (:%d), under `(R215)`(2) -- THE VERDICT COLUMN, READ:*'
H_HEAD = ('*Appended 2026-10-03 by b605, under the author’s ruling `(R215)`(3), to the form of an edition (:11864) -- H28b FOR A '
          'REORGANISING EDITION:*')


def _texts(entry):
    h1, h2 = W_HEAD % entry, C_HEAD % entry
    t1 = ('\n%s PLACE-papers `%s` (aca6804), beside its prior version unedited: 84 rows across 5 of SPIRAL_MAP §4A’s 8 clusters '
          '(Simplicity / RH cascade 57, Methodology 22, Foundations 3, Cubit / Trivium 1, Matter / cosmology 1); 51 rows from the prior '
          'version’s 72 conclusions, each landing in exactly one row by the mapping banked before the writing; 29 page-theorem rows with '
          'their supporting lemmas inside the row; 4 reading rows; the dated entries in marked blocks beneath the tables they fed, counted '
          'as back matter; act numbers out of the body; re-pin 216 of 216; H28a-H28c and H38a-H38d held, H28b by the reading that every '
          'sentence moved to back matter is a recorded removal (accepted at `(R215)`(3)); N2 refuted -- 5 clusters, the three empty ones '
          'named in the edition, the navigator’s count. The three answers before the seal banked verbatim (relay '
          'data/b604_author_answers.txt). Both pages re-emitted from their banked probes, each gaining the edition’s Placement row. '
          'FINDINGS :7056 (the q = 5 correction the navigator’s), :7058, :7060; OPEN_TRAILS :12436, :12440. The suite 78 of 78 before '
          'and after the push. Defects (a) and (b) the seat’s, (a) caught before commit by the prefix check and the OPEN_TRAILS cut-back '
          'with no line moved. Nothing deposited; no kernel touched.\n' % (h1, ED2))
    t2 = ('\n%s The edition’s 6 BRIGHT and 78 DARK, test 1 darkening 65, is the sieve applied as written and not as meant; the fault is '
          'the navigator’s specification at `(R214)`(4) and in the five-tests answer, recorded here as the navigator’s '
          'mis-specification. The five tests were written for routes -- candidate arguments toward a located clause -- and most of the '
          'table’s rows are conclusions that are not routes, which no test asks a question. The seat’s application of the ruling as '
          'written is recorded as correct, its darkening of the Li faces under test 2 included: a test written for routes applied to a '
          'reformulation that is not one. The correction is the v0.3 edition, with a third verdict, NOT A ROUTE, and the faces of the '
          'located clause read as one object under one verdict.\n' % h2)
    t3 = ('\n%s where an edition reorganises a body, every sentence moved whole to back matter counts as a recorded removal in H28b’s '
          'bound, and the diff bank lists each with its destination; the bound is then checked on what remains. The seat’s reading at '
          'b604 is this clause applied before it was written; it stands.\n' % H_HEAD)
    return (h1, t1), (h2, t2), (H_HEAD, t3)


def ledger_check(*texts):
    """### b604 (a): no appended line may put a grade word within the table generator's window of a backticked name."""
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def record_lines(*a):
    """### PLACE-papers FINDINGS: b604's weight and the verdict-column correction, addressed to b604's entry; OPEN_TRAILS: the H28b
    ### reorganising clause, appended at the end addressed to the form's block :11864 (the ledgers are append-only). `dry` prints."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B604_ENTRY)
    if entry != 7060:
        sys.exit('### THE ADDRESSED LINE MOVED -- NOTHING WRITTEN')
    (h1, t1), (h2, t2), (h3, t3) = _texts(entry)
    bad = ledger_check(t1, t2, t3)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        for t in (t1, t2, t3):
            print(t)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    for p, h in ((Q.FIND, h1), (Q.FIND, h2), (Q.OT, h3)):
        Q.guard_absent(p, h)
    out = []
    for p, h, t in ((Q.FIND, h1, t1), (Q.FIND, h2, t2), (Q.OT, h3, t3)):
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b605_record_lines.json', dict(entry=entry, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE VERDICTS
def _old(r):
    v, n = W.verdict(r)
    return v if n is None else '%s, test %d' % (v, n)


def _new(rid):
    x = V.NEW[rid]
    return x['verdict'] if x['test'] is None else '%s, test %d' % (x['verdict'], x['test'])


def _shape(rid):
    return R4._row(rid)['shape']


def h39():
    dark = [k for k, v in V.NEW.items() if v['verdict'] == V.DARK]
    a1 = [k for k in dark if not (V.NEW[k]['kind'] == 'statistic' or V.NEW[k]['test'] == 2)]
    a2 = [k for k in dark if V.NEW[k]['kind'] in V.RULED_FOUR]
    faces = V.FACE_GROUP
    rungs = [k for k, v in V.NEW.items() if v['verdict'] == V.BRIGHT and v['test'] == 4 and _shape(k) == 'FINITE']
    nar = [k for k, v in V.NEW.items() if v['verdict'] == V.NAR]
    S = dict(
        H39a=('HOLDS' if not a1 and not a2 else 'REFUTED',
              'DARK rows %s ; neither a statistic offered as a placement argument nor a route refuted at Epstein (test 2): %s ; a compiled '
              'identity, census, method theorem or face: %s' % (dark, ['%s (%s, test %d)' % (k, V.NEW[k]['kind'], V.NEW[k]['test']) for k in a1] or 'none', a2 or 'none')),
        H39b=('HOLDS' if len(faces) >= 7 and len(set(V.NEW[k]['verdict'] for k in faces)) == 1 else 'REFUTED',
              'the FACE group of the located clause: %d rows %s, one verdict -- the clause`s, %s by test %d' % (len(faces), faces, V.CLAUSE['verdict'], V.CLAUSE['test'])),
        H39c=('HOLDS' if len(rungs) >= 2 else 'REFUTED',
              'FINITE rungs reading BRIGHT by test 4: %d %s ; the forall_upto window: no row -- %s' % (len(rungs), rungs, V.UPTO_READ)),
        H39d=('HOLDS' if len(nar) > len(dark) else 'REFUTED', 'NOT A ROUTE %d against DARK %d' % (len(nar), len(dark))),
    )
    return S, dict(dark=dark, faces=faces, rungs=rungs, nar=nar, a1=a1, a2=a2)


def verdicts():
    """### data/b605_verdicts.txt (and .json), banked before any writing of the edition: the mapping bank (b604's, read through its
    ### json) extended by the verdict column -- every row with its old verdict, its new one and the reason in one line; the FACE group
    ### with its clause and the clause's verdict; the counts; H39a-H39d scored on the bank."""
    M = jl('b604_sieve_mapping.json')
    if [r['id'] for r in M.get('rows') or []] != [r['id'] for r in W.ROWS]:
        sys.exit('### THE MAPPING BANK`S ROWS ARE NOT THE ROWS DATA -- NOTHING WRITTEN')
    mv = {r['id']: (r['verdict'], r['test']) for r in M['rows']}
    L = ['b605 -- COMPONENT 2: THE VERDICTS, (R215)(4) -- THE MAPPING BANK EXTENDED BY A VERDICT COLUMN (OLD, NEW, REASON)',
         '### the mapping: relay data/b604_sieve_mapping.txt and .json (84 rows, the 72 conclusions of the prior version placed); the rows: '
         'relay tools/b604_rows.py; the new verdicts: relay tools/b605_verdicts.py, each read by hand under (R215)(2)(i)-(ii); banked %s, '
         'before any writing of the edition.' % utc(),
         '### the rule, (R215)(2)(i): a row whose conclusion is not a candidate argument toward h2_sign, simplicity or a GRH_chi target reads '
         'NOT A ROUTE, its test column "—"; test 1 applies only to a statistic or average over the zeros offered as a placement argument. '
         '(R215)(2)(ii): the compiled iff-faces of the located clause read FACE under the clause`s one verdict; the Li ladder`s bright row is '
         'its arithmetic end, the Keiper face, and liCoeff_one_pos a FINITE rung of it, bright by test 4.', '',
         '### THE LOCATED CLAUSE, ITS VERDICT STATED ONCE: %s -- %s ; verdict %s, test %d: %s' % (V.CLAUSE['name'], V.CLAUSE['what'],
                                                                                              V.CLAUSE['verdict'], V.CLAUSE['test'], V.CLAUSE['why']), '',
         '### EVERY ROW, OLD -> NEW, WITH THE REASON IN ONE LINE (row | cluster | kind | old | new | reason):']
    lines = {}
    for r in W.ROWS:
        x = V.NEW[r['id']]
        if (W.verdict(r)[0], W.verdict(r)[1]) != tuple(mv[r['id']]):
            sys.exit('### THE MAPPING`S VERDICT FOR %s IS NOT THE ROWS DATA`S -- NOTHING WRITTEN' % r['id'])
        L.append('  %s | %s | %s | %s -> %s | %s' % (r['id'], r['cluster'], x['kind'], _old(r), _new(r['id']), x['why']))
        lines[r['id']] = len(L)
    L += ['', '### THE FACE GROUPS, EACH WITH ITS CLAUSE AND THE CLAUSE`S VERDICT:',
          '  %s (%d rows): %s -- one verdict, %s, decided by test %d' % (V.CLAUSE['name'], len(V.FACE_GROUP), ', '.join(V.FACE_GROUP),
                                                                      V.CLAUSE['verdict'], V.CLAUSE['test'])]
    for k in V.FACE_GROUP:
        L.append('    %s  %s' % (k, V.NEW[k]['why']))
    cnt = {v: sum(1 for x in V.NEW.values() if x['verdict'] == v) for v in (V.BRIGHT, V.DARK, V.NAR, V.FACE)}
    by_cl = {}
    for r in W.ROWS:
        by_cl.setdefault(r['cluster'], {}).setdefault(V.NEW[r['id']]['verdict'], 0)
        by_cl[r['cluster']][V.NEW[r['id']]['verdict']] += 1
    changed = [r['id'] for r in W.ROWS if _old(r) != _new(r['id'])]
    kept = [r['id'] for r in W.ROWS if _old(r) == _new(r['id'])]
    S, X = h39()
    L += ['', '### THE COUNTS',
          '  BRIGHT %d ; DARK %d ; NOT A ROUTE %d ; FACE %d (the located clause`s, one verdict %s) ; total %d' % (
              cnt[V.BRIGHT], cnt[V.DARK], cnt[V.NAR], cnt[V.FACE], V.CLAUSE['verdict'], sum(cnt.values())),
          '  by cluster: %s' % by_cl,
          '  DARK by test: %s' % {t: sum(1 for x in V.NEW.values() if x['verdict'] == V.DARK and x['test'] == t) for t in (1, 2, 3, 4, 5)},
          '  rows whose verdict changed: %d ; kept (the reason restated where test 1`s scope moved): %d %s' % (len(changed), len(kept), kept),
          '  at v0.2: BRIGHT %d, DARK %d (test 1: %d, test 2: %d, test 3: %d)' % (
              sum(W.verdict(r)[0] == 'BRIGHT' for r in W.ROWS), sum(W.verdict(r)[0] == 'DARK' for r in W.ROWS),
              *[sum(W.verdict(r) == ('DARK', k) for r in W.ROWS) for k in (1, 2, 3)]),
          '', '### H39a-H39d, SCORED ON THIS BANK:']
    for k in ('H39a', 'H39b', 'H39c', 'H39d'):
        L.append('### ### **%s %s -- %s.**' % (k, S[k][0], S[k][1]))
    put_txt('b605_verdicts.txt', L)
    put_json('b605_verdicts.json', dict(at=utc(), lines=lines, counts=cnt, by_cluster=by_cl, changed=changed, kept=kept, scores=S, X=X,
                                        rows=[dict(id=r['id'], cluster=r['cluster'], kind=V.NEW[r['id']]['kind'], old=_old(r), new=_new(r['id']),
                                                   verdict=V.NEW[r['id']]['verdict'], test=V.NEW[r['id']]['test'], why=V.NEW[r['id']]['why'])
                                              for r in W.ROWS]))
    for k in ('H39a', 'H39b', 'H39c', 'H39d'):
        print('  %s %s' % (k, S[k][0]))
    print('  counts %s' % cnt)


# ================================================================================ COMPONENT 3: THE EDITION
BM_TAG3 = '<!-- b605 (R215) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION3 = ('*v0.3, 2026-10-03 -- the correction edition: the verdict column re-read with NOT A ROUTE as a third verdict and the faces '
            'of the located clause under one verdict; v0.2 stands beside it, unedited.*')
BULLET3 = ('- **Verdict**: one of four words -- a route (a candidate argument toward `h2_sign`, simplicity or a GRH_chi target) is read '
           'through the five tests below in order, DARK at the first test it fails with that test’s number, its instrument’s pin and the '
           'reason, and BRIGHT when it fails none, which says the row’s register reaches placement at a compiled face and not that the '
           'row’s open side holds; a row whose conclusion is not a route reads NOT A ROUTE, its test column “—”. A compiled iff-face of '
           'the located clause reads FACE and takes the clause’s one verdict, stated once above its group.')
ROUTES = ('The five tests are tests of routes: each asks a candidate argument toward the located clause, simplicity or a GRH_chi target '
          'a question about placement, and a row that is not a route is not asked.')
TEST1_SCOPE = ('; it reads only a row that is a statistic or an average over the zeros offered as a placement argument -- a density, a '
               'zero-density, a mollifier, a GUE statistic, a proportion -- and nothing else')
HEADER3 = '| row | the conclusion | shape | register | verdict | test, instrument at pin | reason | compiled face |'
SEP3 = '|:--|:--|:--|:--|:--|:--|:--|:--|'
FACE_HEAD = '### The located clause and its faces — %d rows, one verdict'
REST_HEAD = '### The other rows of this cluster — %d rows'

MUTUAL3 = {
    'RH': 'Read in mutual light: Foundations’ rows supply test 2’s instrument -- the located clause is BRIGHT at test 2 because a route '
          'through it fails at the Epstein configuration those rows compile -- and Methodology’s record rows fix how far any row here may '
          'be read (the findings pass, its fences, the document’s limits); Cubit / Trivium’s and Matter / cosmology’s rows change no '
          'reading here, their objects decided independent of the identity and the density.',
    'FD': 'Read in mutual light: the Simplicity / RH cascade’s located clause is the route Theorem 3.7 says must use the Euler product, '
          'and the schema’s generic theorems this table’s witness reaches read NOT A ROUTE beside it; Methodology’s record rows bound '
          'this table’s barrier row.',
    'MT': 'Read in mutual light: every other cluster’s rows are read through this table’s, whose rows fix what a row may claim (the '
          'governing claim’s ceiling, the findings pass, the limits of the fold); no other cluster’s row changes a record row’s own '
          'verdict, since a statement about the corpus is not a route.',
}


def _v2():
    t = _show(PP, PRE_PP, ED2)
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _cells2(r):
    return R4._row_cells(r)


def _row3(r):
    c = _cells2(r)
    x = V.NEW[r['id']]
    if x['verdict'] in (V.FACE, V.NAR):
        tcell = '—'
    else:
        tcell = '%d (%s)' % (x['test'], W.TESTS[x['test']]['short'])
    return c[:4] + [x['verdict'], tcell, x['why'], c[5]]


def _line3(r):
    return '| ' + ' | '.join(R4._cell(x) for x in _row3(r)) + ' |'


def _counts_head(rs):
    n = {v: sum(1 for r in rs if V.NEW[r['id']]['verdict'] == v) for v in (V.FACE, V.BRIGHT, V.DARK, V.NAR)}
    parts = (['%d FACE' % n[V.FACE]] if n[V.FACE] else []) + ['%d BRIGHT' % n[V.BRIGHT], '%d DARK' % n[V.DARK], '%d NOT A ROUTE' % n[V.NAR]]
    return '%d row%s: %s' % (len(rs), '' if len(rs) == 1 else 's', ', '.join(parts))


def _segs(l):
    return R4._segs(l)


def edition(*a):
    """### PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md beside v0.2 (unedited), written from v0.2's blob at c7d3d48,
    ### tools/b604_rows.py and tools/b605_verdicts.py; the re-pin step last (`repin`). Writes the edition file and data/b605_edition.json;
    ### `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    v2 = _v2()
    if g(PP, 'rev-parse', 'HEAD:' + ED2).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, ED2)).strip():
        sys.exit('### v0.2 MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    if not dry and os.path.exists(os.path.join(PP, *ED.split('/'))):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    VB = jl('b605_verdicts.json') if os.path.exists(os.path.join(D, 'b605_verdicts.json')) else {}
    if not VB and not dry:
        sys.exit('### THE VERDICT BANK IS NOT BANKED -- COMPONENT 2 FIRST')
    bank_line = VB.get('lines') or {r['id']: 0 for r in W.ROWS}
    # ### v0.2's anchors, by content
    i_ver = v2.index(R4.VERSION) + 1
    i_bullet = [i + 1 for i, l in enumerate(v2) if l.startswith('- **Bright or dark**:')][0]
    i_tests = v2.index('## The five tests') + 1
    i_t1 = [i + 1 for i, l in enumerate(v2) if l.startswith('1. **Placement register**')][0]
    i_cl = [i + 1 for i, l in enumerate(v2) if l.startswith('The clusters are SPIRAL_MAP')][0]
    i_bm2 = v2.index(R4.BM_TAG) + 1
    rows_by = {r['id']: r for r in W.ROWS}
    v2row = {}
    for i, l in enumerate(v2, 1):
        m = re.match(r'^\| ([A-Z]{2}-\d\d) \| ', l)
        if m and i < i_bm2:
            v2row[m.group(1)] = i
            if l != R4._row_line(rows_by[m.group(1)]):
                sys.exit('### v0.2`S ROW %s IS NOT THE ROWS DATA`S LINE -- NOTHING WRITTEN' % m.group(1))
    tables = {}
    for cid, cname in W.CLUSTERS:
        rs = [r for r in W.ROWS if r['cluster'] == cid]
        if not rs:
            continue
        h = [i + 1 for i, l in enumerate(v2) if l.startswith('## %s — ' % cname)][0]
        hdr = h + 2
        if not v2[hdr - 1].startswith('| row | the conclusion |'):
            sys.exit('### v0.2`S TABLE HEADER FOR %s IS NOT WHERE IT WAS READ -- NOTHING WRITTEN' % cid)
        mut = [i + 1 for i, l in enumerate(v2) if i + 1 > hdr and l.startswith('Read in mutual light')][0]
        tables[cid] = dict(name=cname, head=h, hdr=hdr, rows=[r['id'] for r in rs], last=max(v2row[r['id']] for r in rs), mut=mut)
    E, where, rew, ins, rep = [], {}, [], [], []
    pos = dict(rows={}, tables={}, heads={}, mutual={}, face_head=0, clause_line=0, rest_head=0, routes=0, verdicts=0, test1=0, bullet=0,
               version=0, bm3=0)

    def carry(n):
        E.append(v2[n - 1])
        where[n] = len(E)

    def rewrite(n, new, what):
        E.append(new)
        rew.append(dict(v2=n, v3=len(E), old=v2[n - 1], new=new, what=what))
        where.setdefault(n, len(E))

    def insert(text, what, body=True):
        E.append(text)
        ins.append(dict(v3=len(E), text=text, what=what, body=body))

    skip_to = 0
    cnt = {v: sum(1 for x in V.NEW.values() if x['verdict'] == v) for v in (V.BRIGHT, V.DARK, V.NAR, V.FACE)}
    COUNTS = ('**The verdicts at this edition:** %d rows -- %d BRIGHT, %d DARK, %d NOT A ROUTE, and %d FACE rows of the located clause, '
              'whose one verdict is %s.' % (len(W.ROWS), cnt[V.BRIGHT], cnt[V.DARK], cnt[V.NAR], cnt[V.FACE], V.CLAUSE['verdict']))
    CLAUSE_LINE = ('**The clause’s verdict, stated once: %s, by test %d (%s).** The located clause is %s; its verdict was %s. Each row '
                   'below is an iff-face of this one clause and reads FACE.' % (
                       V.CLAUSE['verdict'], V.CLAUSE['test'], W.TESTS[V.CLAUSE['test']]['short'], V.CLAUSE['what'], V.CLAUSE['why']))
    for n in range(1, len(v2) + 1):
        if n < skip_to:
            continue
        if n >= i_bm2:
            l = v2[n - 1]
            m1 = re.match(r'^\| ([A-Z]{2}-\d\d) \(:(\d+)\) \|', l)
            m2 = re.match(r'^\| ([A-Z]{2}-\d\d) \| :(\d+) \|', l)
            m = m1 or m2
            if m:
                rid, old = m.group(1), int(m.group(2))
                if v2row.get(rid) != old:
                    sys.exit('### v0.2`S BACK-MATTER CELL FOR %s CITES :%d, NOT ITS ROW :%s -- NOTHING WRITTEN' % (rid, old, v2row.get(rid)))
                new = l.replace('(:%d) |' % old, '(:{ROW3:%s}) |' % rid, 1) if m1 else l.replace('| :%d |' % old, '| :{ROW3:%s} |' % rid, 1)
                E.append(new)
                rep.append(dict(v2=n, v3=len(E), row=rid, old=old, kind='rewrites or fact cell' if m1 else 'Correspondence cell'))
                where[n] = len(E)
                continue
            carry(n)
            continue
        if n == i_ver:
            insert(VERSION3, 'the version line, above the previous')
            pos['version'] = len(E)
            insert('', 'blank')
            carry(n)
            continue
        if n == i_bullet:
            rewrite(n, BULLET3, 'the verdict bullet: the four verdicts, (R215)(2)(i)-(ii)')
            pos['bullet'] = len(E)
            continue
        if n == i_tests + 1:
            carry(n)
            insert(ROUTES, 'the one sentence that the five tests are tests of routes, (R215)(4)')
            pos['routes'] = len(E)
            insert('', 'blank')
            continue
        if n == i_t1:
            l = v2[n - 1]
            cut = l.index('. Instrument:')
            rewrite(n, l[:cut] + TEST1_SCOPE + l[cut:], 'test 1 restated: its scope, (R215)(2)(i)')
            pos['test1'] = len(E)
            continue
        if n == i_cl + 1:
            carry(n)
            insert('## The verdicts', 'the head`s verdict counts, (R215)(4)')
            insert('', 'blank')
            insert(COUNTS, 'the head`s verdict counts, (R215)(4)')
            pos['verdicts'] = len(E)
            insert('', 'blank')
            continue
        hit = [c for c, t in tables.items() if n == t['head']]
        if hit:
            c = hit[0]
            t = tables[c]
            rs = [rows_by[x] for x in t['rows']]
            rewrite(n, '## %s — %s' % (t['name'], _counts_head(rs)), 'the cluster heading`s counts')
            pos['heads'][c] = len(E)
            continue
        hit = [c for c, t in tables.items() if n == t['hdr']]
        if hit:
            c = hit[0]
            t = tables[c]
            rs = [rows_by[x] for x in t['rows']]
            if c == 'RH':
                insert(FACE_HEAD % len(V.FACE_GROUP), 'the FACE group`s heading, (R215)(4)')
                pos['face_head'] = len(E)
                insert('', 'blank')
                insert(CLAUSE_LINE, 'the clause`s verdict, stated once, (R215)(2)(ii) and (4)')
                pos['clause_line'] = len(E)
                insert('', 'blank')
                rewrite(n, HEADER3, 'the table header: verdict, test and reason in their own columns')
                pos['tables']['RH-face'] = len(E)
                rewrite(n + 1, SEP3, 'the table header`s rule')
                for x in V.FACE_GROUP:
                    rewrite(v2row[x], _line3(rows_by[x]), 'row %s re-read' % x)
                    pos['rows'][x] = len(E)
                insert('', 'blank')
                rest = [r for r in rs if r['id'] not in V.FACE_GROUP]
                insert(REST_HEAD % len(rest), 'the other rows` heading, (R215)(4)')
                pos['rest_head'] = len(E)
                insert('', 'blank')
                insert(HEADER3, 'the second table`s header')
                pos['tables']['RH'] = len(E)
                insert(SEP3, 'the second table`s rule')
                for r in rest:
                    rewrite(v2row[r['id']], _line3(r), 'row %s re-read' % r['id'])
                    pos['rows'][r['id']] = len(E)
            else:
                rewrite(n, HEADER3, 'the table header: verdict, test and reason in their own columns')
                pos['tables'][c] = len(E)
                rewrite(n + 1, SEP3, 'the table header`s rule')
                for r in rs:
                    rewrite(v2row[r['id']], _line3(r), 'row %s re-read' % r['id'])
                    pos['rows'][r['id']] = len(E)
            skip_to = t['last'] + 1
            continue
        hit = [c for c, t in tables.items() if n == t['mut']]
        if hit:
            c = hit[0]
            if c in MUTUAL3:
                rewrite(n, MUTUAL3[c], 'the mutual-light line, by the restatement clause (OPEN_TRAILS :12192)')
            else:
                carry(n)
            pos['mutual'][c] = len(E)
            continue
        carry(n)
    # ### the v0.3 back matter, appended after v0.2's
    E += ['', '---', '']
    pos['bm3'] = len(E) + 1
    vb_ref = 'relay `data/b605_verdicts.txt`'
    E += [BM_TAG3, '',
          '## Back matter of the v0.3 edition — written 2026-10-03 by b605 under the author’s ruling `(R215)`(4), by the form of '
          '`(R187)`(5), its clauses and the precedence order', '',
          '*This file is v0.3 of THE_FINDINGS_AS_THEY_STAND, written beside v0.2 (`%s`, unedited) from that version’s blob at PLACE-papers '
          '%s and the verdict bank (%s) banked before the edition was written; the current version (`%s`, read as v0.1) stands unedited '
          'too. v0.2’s back matter is carried above whole, its own-line cells re-pinned to this file’s lines (listed below). Every line '
          'cited in this section is this file’s own unless it is marked as v0.2’s.*' % (ED2, PRE_PP, vb_ref, CUR), '',
          '### The re-read and its readings', '',
          '- `(R215)`(2)(i): a row whose conclusion is not a candidate argument toward `h2_sign`, simplicity or a GRH_chi target reads NOT A '
          'ROUTE, its test column “—”; test 1 reads only a statistic or average over the zeros offered as a placement argument (in this '
          'table: the proportion row RH-16 and the density rows RH-39, RH-40, RH-43).',
          '- `(R215)`(2)(ii): the compiled iff-faces of the located clause read FACE under the clause’s one verdict (:{POS:clause_line}). '
          'The χ and family forms join the group by the ruling’s letter; `h2_sign_cfg_iff_target` (RH-22) joins it by the ruling’s own '
          'reason -- it holds of every configuration and so says nothing by itself of the prime side -- the seat’s reading, strikeable.',
          '- The test that decided the clause’s verdict is named as test 2, the clause carrying the explicit formula’s prime sum at ζ and '
          'at χ; the seat’s reading, strikeable.',
          '- The Keiper face is read as RH-11 (`keiperTaylorIdentity_of`, λ_n from the Stieltjes side for every n), BRIGHT by test 4; '
          '`liCoeff_one_pos` (RH-13) as its FINITE rung, BRIGHT by test 4; λ₁’s closed form (RH-12) as the compiled identity that rung '
          'reads, NOT A ROUTE; the seat’s readings, strikeable.',
          '- The Dedekind reading (RH-30) is read as a candidate route toward GRH_chi for every character mod q and keeps its DARK by test 3.',
          '- No sentence moved to back matter: the reorganising clause of `(R215)`(3) is not invoked, and H28b is read on the body as it '
          'stands, every change a ruled insertion or a ruled rewrite listed below.', '',
          '### Removals', '', 'None.', '',
          '### Verdict changes -- every row re-read', '',
          '| row | this edition’s line | v0.2’s verdict cell, verbatim | the verdict at v0.3 | the reason | the bank’s line | Status |',
          '|:--|:--|:--|:--|:--|:--|:--|']
    for r in W.ROWS:
        c = _cells2(r)
        E.append('| %s | :{ROW3:%s} | %s | %s | %s | %s :%d | %s |' % (
            r['id'], r['id'], R4._cell(c[4]), _new(r['id']), R4._cell(V.NEW[r['id']]['why']), vb_ref, bank_line.get(r['id'], 0),
            'the verdict changed' if _old(r) != _new(r['id']) else 'the verdict kept, its reason restated'))
    E += ['', '### Rewrites -- the head, the headings, the table headers and the mutual-light lines', '',
          '| this edition’s line | v0.2’s line | v0.2’s wording | this edition’s wording | Status |', '|:--|:--|:--|:--|:--|']
    for x in rew:
        if x['what'].startswith('row '):
            continue
        E.append('| :%d | :%d | %s | %s | %s |' % (x['v3'], x['v2'], R4._cell(x['old']), R4._cell(x['new']), x['what']))
    E += ['', '### Insertions ordered by the ruling', '', '| this edition’s line | the text | Status |', '|:--|:--|:--|']
    for x in ins:
        if x['what'] == 'blank':
            continue
        E.append('| :%d | %s | %s |' % (x['v3'], R4._cell(x['text'])[:400], x['what']))
    E += ['', '### Fact corrections', '',
          '| where | the ferry’s wording | this edition’s reading | the source | Status |', '|:--|:--|:--|:--|:--|',
          '| the ferry’s reads | “THE_CLAUSE_AND_ITS_COMPILED_FACES.md at v0.21” | the ζ page at its own pin v0.20 = 914c413 | relay '
          '`data/b602_nodes_zeta.txt`, its `# pin:` line | a fact correction to the ferry’s letter, recorded as the navigator’s |',
          '| the ferry’s reads | “Keiper.lean’s λ₁ closed form and liCoeff_one_pos at v0.20” | `liCoeff_one_keiper` in Keiper.lean, '
          '`liCoeff_one_pos` in KeiperSign.lean, both at v0.20 = 914c413 | SIDE-explicit-formula v0.20, the two files | a fact correction '
          'to the ferry’s letter, recorded as the navigator’s |',
          '| H39c’s “the forall_upto window” | a FINITE rung reading BRIGHT | no row: the forall_upto pair are faces (UNIVERSAL), and no '
          'declaration fixes one rung at a finite support length | SIDE-explicit-formula v0.21 `DetectionRegion.lean` :29, :47, :52 | '
          'recorded; H39c scored on the rows as they stand |', '',
          '### Re-pins of v0.2’s back matter', '',
          '%d own-line cells of v0.2’s back matter re-pinned to this file’s row lines: %d in the rewrites and fact-correction tables, %d in '
          'the Correspondence; every other line of v0.2’s back matter carried verbatim.' % (
              len(rep), sum(1 for x in rep if x['kind'] != 'Correspondence cell'), sum(1 for x in rep if x['kind'] == 'Correspondence cell')), '',
          '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.3 | `%s` | written at b605 |' % ED,
          '| v0.2 | `%s` | unedited |' % ED2,
          '| the current version, unnumbered (read as v0.1) | `%s` | unedited |' % CUR,
          '| the verdict bank | %s | banked at b605 before the edition |' % vb_ref,
          '| the mapping | relay `data/b604_sieve_mapping.txt` | read |',
          '| the sentence-by-sentence diff | relay `data/b605_edition_FINDINGS_STAND.txt` | banked at b605 |', '',
          '### Correspondence', '',
          '| row | this edition’s line | v0.2’s line | the verdict at v0.2 | the verdict at v0.3 | Status |', '|:--|:--|:--|:--|:--|:--|']
    for r in W.ROWS:
        E.append('| %s | :{ROW3:%s} | :%d | %s | %s | %s |' % (r['id'], r['id'], v2row[r['id']], _old(r), _new(r['id']),
                                                            'changed' if _old(r) != _new(r['id']) else 'kept'))
    E += ['', '### Version history', '',
          '- **v0.3, 2026-10-03 (b605, `(R215)`(4))**: the verdict column re-read -- %d BRIGHT, %d DARK, %d NOT A ROUTE, %d FACE under '
          'the located clause’s one verdict, %s; the head’s five tests restated as tests of routes; the bench, the readings and the dated '
          'blocks unchanged. v0.2 stands beside it, unedited.' % (cnt[V.BRIGHT], cnt[V.DARK], cnt[V.NAR], cnt[V.FACE], V.CLAUSE['verdict']),
          '- **v0.2, 2026-10-03 (b604, `(R214)`(4))**: its own version history is carried above.', '']
    # ### resolve the tokens to the final lines
    E = [re.sub(r'\{ROW3:([A-Z]{2}-\d\d)\}', lambda m: str(pos['rows'][m.group(1)]), x) for x in E]
    E = [re.sub(r'\{POS:([a-z0-9_]+)\}', lambda m: str(pos[m.group(1)]), x) for x in E]
    for x in rep:
        x['new'] = pos['rows'][x['row']]
    text = NL.join(E) + NL
    b = text.encode('utf-8')
    dest = os.path.join(SP, 'b605_edition_dry.md') if dry else os.path.join(PP, *ED.split('/'))
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ed = text.split(NL)[:-1]
    body3, bm3 = R4._body_and_bm(ed)
    body2, bm2 = R4._body_and_bm(v2)
    body3_idx = set(i for i, _l in body3)
    n_b3, n_b2 = R4._count([l for _i, l in body3]), R4._count([l for _i, l in body2])
    ins_body = [x for x in ins if x['v3'] in body3_idx and x['what'] != 'blank']
    ver = [x for x in ins_body if x['what'].startswith('the version line')]
    ruled_ins = sum(len(_segs(x['text'])) for x in ins_body if not x['what'].startswith('the version line'))
    rew_body = [x for x in rew if x['v3'] in body3_idx]
    deltas = [dict(v2=x['v2'], v3=x['v3'], what=x['what'], d=len(_segs(x['new'])) - len(_segs(x['old']))) for x in rew_body]
    J = dict(at=utc(), dry=dry, path=ED, sha256=sha(b), bytes=len(b), lines=len(ed), v2_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, ED2)).strip(),
             n_v2_body=n_b2, n_body=n_b3, n_backmatter=R4._count([l for _i, l in bm3]), n_v2_backmatter=R4._count([l for _i, l in bm2]),
             n_full=R4._count(ed), version_lines=sum(len(_segs(x['text'])) for x in ver), credit=0, removals=0, ruled_insertions=ruled_ins,
             rewrite_deltas=deltas, where={str(k): v for k, v in where.items()}, rew=rew, ins=ins, rep=rep,
             pos=dict(rows=pos['rows'], tables=pos['tables'], heads=pos['heads'], mutual=pos['mutual'], face_head=pos['face_head'],
                      clause_line=pos['clause_line'], rest_head=pos['rest_head'], routes=pos['routes'], verdicts=pos['verdicts'],
                      test1=pos['test1'], bullet=pos['bullet'], version=pos['version'], bm3=pos['bm3']),
             v2row=v2row, acts_in_body=[(i, m.group(0)) for i, l in body3 for m in R4.ACTNUM.finditer(l)],
             ceiling_in_body=[(i, m.group(0)) for i, l in body3 for m in R4.CEILING.finditer(l)])
    if dry:
        open(os.path.join(SP, 'b605_edition_dry.json'), 'w', encoding='utf-8').write(json.dumps(J, indent=1, ensure_ascii=False))
    else:
        put_json('b605_edition.json', J)
    print('  %s : %d lines, %d bytes, sha256 %s' % (dest, len(ed), len(b), J['sha256'][:16]))
    print('  body v0.2 %d ; body v0.3 %d (%+d) ; version %d ; ruled insertions %d ; rewrite deltas %s ; back matter v0.3 %d (v0.2 %d)' % (
        n_b2, n_b3, n_b3 - n_b2, J['version_lines'], ruled_ins, [(x['v2'], x['d']) for x in deltas if x['d']], J['n_backmatter'], J['n_v2_backmatter']))
    print('  acts in body %s ; ceiling in body %s ; rewrites %d ; insertions %d ; re-pins %d' % (J['acts_in_body'], J['ceiling_in_body'], len(rew), len(ins), len(rep)))


def termscan():
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b605_edition_termscan.txt."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b605_edition_termscan.txt', (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l])


def _ed():
    t = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '')
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def carried(E, ed, v2):
    """### every non-blank v0.2 line: carried verbatim at its mapped line, or re-pinned (its own-line cell only), or rewritten with its
    ### old wording in this file's back matter (a row: its v0.2 verdict cell, verbatim, in the verdict-change table, every other cell
    ### kept in the new row; any other line: its whole wording in the rewrites table)."""
    rewd = {x['v2']: x for x in E['rew']}
    repd = {x['v2']: x for x in E['rep']}
    bm3 = NL.join(ed[E['pos']['bm3'] - 1:])
    ok, bad = 0, []
    for n in range(1, len(v2) + 1):
        if not v2[n - 1].strip():
            continue
        if n in rewd:
            x = rewd[n]
            if x['what'].startswith('row '):
                rid = x['what'].split()[1]
                old = R4._row_line(R4._row(rid))
                oc = [c.strip() for c in old.strip('|').split(' | ')]
                nc = [c.strip() for c in ed[x['v3'] - 1].strip('|').split(' | ')]
                good = v2[n - 1] == old and nc[:4] == oc[:4] and nc[7] == oc[5] and ('| %s | :%d | %s |' % (rid, x['v3'], oc[4])) in bm3
            else:
                good = ed[x['v3'] - 1] == x['new'] and ('| :%d | :%d | %s |' % (x['v3'], n, R4._cell(x['old']))) in bm3
        elif n in repd:
            x = repd[n]
            want = v2[n - 1].replace('(:%d) |' % x['old'], '(:%d) |' % x['new'], 1) if '(:%d) |' % x['old'] in v2[n - 1] \
                else v2[n - 1].replace('| :%d |' % x['old'], '| :%d |' % x['new'], 1)
            good = ed[x['v3'] - 1] == want
        else:
            w = E['where'].get(str(n))
            good = bool(w) and ed[w - 1] == v2[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def edition_bank():
    """### The diff with its offset line, the insertions and rewrites, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b605_edition.json')
    ed = _ed()
    v2 = _v2()
    if sha('\n'.join(ed).encode('utf-8') + b'\n') != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    VB = jl('b605_verdicts.json')
    body, bm = R4._body_and_bm(ed)
    scan = rd('b605_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad = carried(E, ed, v2)
    hits = []
    body_idx = set(i for i, _l in body)
    for i, l in enumerate(ed, 1):
        for m in R4.CEILING.finditer(l):
            hits.append(dict(line=i, hit=m.group(0), kind='body' if i in body_idx else 'record (carried history or back matter)'))
    beyond = [h for h in hits if h['kind'] == 'body']
    # ### H28a: every MOVED-IN-MEANING sentence -- a row whose verdict changed -- resolves to a sentence citing a declaration on a page
    # ### (its own compiled face) or a banked line: its verdict-change row in the back matter cites the verdict bank by line, and that
    # ### bank line carries the row's old -> new
    vb = rd('b605_verdicts.txt').split(NL)
    bmt = NL.join(ed[E['pos']['bm3'] - 1:])
    h28a_rows = []
    for rid in VB['changed']:
        bl = VB['lines'][rid]
        bank_ok = 0 < bl <= len(vb) and vb[bl - 1].startswith('  %s | ' % rid) and (' -> %s | ' % _new(rid)) in vb[bl - 1]
        cites = ('| %s | :%d | ' % (rid, E['pos']['rows'][rid])) in bmt and ('`data/b605_verdicts.txt` :%d |' % bl) in bmt
        pagef = [f['name'] for f in R4._row(rid)['faces'] if f['role'] == 'face' and f.get('page')]
        h28a_rows.append(dict(row=rid, bank_line=bl, bank_ok=bank_ok, cites_bank=cites, page_faces=pagef))
    h28a = 'HOLDS' if all(x['bank_ok'] and x['cites_bank'] for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_v2_body']
    d = sum(x['d'] for x in E['rewrite_deltas'])
    allowed = E['credit'] + E['removals'] + E['ruled_insertions'] + sum(abs(x['d']) for x in E['rewrite_deltas']) + E['version_lines']
    strict = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if (clean and not beyond) else 'REFUTED'
    # ### the offset, read from the map
    offs, last = [], None
    for n in range(1, len(v2) + 1):
        w = E['where'].get(str(n))
        if not w:
            continue
        o = w - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v0.2 (R190)(3): %s -- the offset changes at each v0.2 line printed (v0.2 line, offset); inside the Simplicity / '
         'RH cascade table the FACE group`s rows move above the rest; every v0.2 line`s v0.3 line is printed below (the map), and every '
         'edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs[:12]), '',
         'b605 -- COMPONENT 3: THE SIEVE TABLE AT v0.3, (R215)(4), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v0.2 : PLACE-papers %s @ %s (blob %s), %d lines' % (ED2, PRE_PP, E['v2_blob'][:8], len(v2)),
         '### v0.3 : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines'], E['sha256']), '',
         '### THE HEAD`S RESTATEMENT, PRINTED:',
         '    :%d %s' % (E['pos']['version'], ed[E['pos']['version'] - 1]),
         '    :%d %s' % (E['pos']['bullet'], ed[E['pos']['bullet'] - 1]),
         '    :%d %s' % (E['pos']['routes'], ed[E['pos']['routes'] - 1]),
         '    :%d %s' % (E['pos']['test1'], ed[E['pos']['test1'] - 1]),
         '    :%d %s' % (E['pos']['verdicts'], ed[E['pos']['verdicts'] - 1]),
         '    :%d %s' % (E['pos']['face_head'], ed[E['pos']['face_head'] - 1]),
         '    :%d %s' % (E['pos']['clause_line'], ed[E['pos']['clause_line'] - 1]), '',
         '### EVERY CHANGED ROW, PRINTED (%d rows; v0.2 line -> v0.3 line):' % len(W.ROWS)]
    for r in W.ROWS:
        L += ['  %s  v0.2 :%d -> v0.3 :%d -- %s -> %s' % (r['id'], E['v2row'][r['id']], E['pos']['rows'][r['id']], _old(r), _new(r['id'])),
              '      v0.3 : %s' % ed[E['pos']['rows'][r['id']] - 1][:420]]
    L += ['', '### EVERY OTHER REWRITE (v0.3 line <- v0.2 line, the segment change):']
    for x in E['rew']:
        if not x['what'].startswith('row '):
            L.append('  :%d <- :%d  %s (%+d)' % (x['v3'], x['v2'], x['what'], len(_segs(x['new'])) - len(_segs(x['old']))))
    L += ['', '### EVERY INSERTION (v0.3 line, its segments, what orders it):']
    L += ['  :%d (%d) %s' % (x['v3'], len(_segs(x['text'])), x['what']) for x in E['ins'] if x['what'] != 'blank']
    L += ['', '### THE RE-PINS OF v0.2`S BACK MATTER (%d cells: v0.2 line -> v0.3 line, the row, its old and new line):' % len(E['rep'])]
    L += ['  :%d -> :%d  %s :%d -> :%d (%s)' % (x['v2'], x['v3'], x['row'], x['old'], x['new'], x['kind']) for x in E['rep']]
    L += ['', '### EVERY NON-BLANK v0.2 LINE -> ITS v0.3 LINE (%d carried verbatim, re-pinned or rewritten with its old wording recorded ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, w) for n, w in sorted(((int(k), v) for k, v in E['where'].items()))]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v0.2`s BODY %d ; v0.3`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v0.2`s carried and v0.3`s own, the history blocks included), printed separately ; the edition whole %d' % (
              E['n_v2_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d (no sentence moved to back matter; the clause of '
          '(R215)(3) not invoked) + ruled insertions %d + ruled rewrites` changes %d (net %+d, each listed above) + one version line %d = %d ; '
          'the strict count, every rewrite keeping its segments, %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_insertions'], sum(abs(x['d']) for x in E['rewrite_deltas']), d,
              E['version_lines'], allowed, strict), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling in the body: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'),
          '### H28a: rows whose verdict changed (MOVED-IN-MEANING) %d ; each resolving to its verdict-change row citing the verdict bank by '
          'line, the bank line carrying its old -> new: %d ; with a declaration on a page in its own row besides: %d' % (
              len(h28a_rows), sum(1 for x in h28a_rows if x['bank_ok'] and x['cites_bank']), sum(1 for x in h28a_rows if x['page_faces'])), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING row (%d) resolves to a sentence citing a banked line.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling in the body %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b605_edition_FINDINGS_STAND.txt', L)
    put_json('b605_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed, strict=strict,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, clean=clean, beyond=len(beyond),
                                   hits=hits, carried_ok=ok, carried_bad=bad, held=None))
    print('H28a %s H28b %s H28c %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; beyond %d' % (
        h28a, h28b, h28c, ok, bad, body_dn, allowed, strict, len(beyond)))


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b605_repin.txt."""
    E = jl('b605_edition.json')
    ed = _ed()
    P = E['pos']
    cut2 = ed.index(R4.BM_TAG)
    cut3 = ed.index(BM_TAG3)
    checks = []
    for r in W.ROWS:
        ln = P['rows'][r['id']]
        checks.append(('row %s on :%d' % (r['id'], ln), ed[ln - 1] == _line3(r) and ln < cut2))
    bm2 = NL.join(ed[cut2:cut3])
    bm3 = NL.join(ed[cut3:])
    for r in W.ROWS:
        checks.append(('v0.2`s Correspondence names %s at :%d' % (r['id'], P['rows'][r['id']]), ('| %s | :%d |' % (r['id'], P['rows'][r['id']])) in bm2))
        checks.append(('v0.3`s Correspondence names %s at :%d' % (r['id'], P['rows'][r['id']]), ('| %s | :%d | :%d |' % (r['id'], P['rows'][r['id']], E['v2row'][r['id']])) in bm3))
        checks.append(('v0.3`s verdict-change table names %s at :%d' % (r['id'], P['rows'][r['id']]), ('\n| %s | :%d | ' % (r['id'], P['rows'][r['id']])) in bm3))
    for x in re.findall(r'\| [A-Z]{2}-\d\d \(:(\d+)\) \|', bm2):
        checks.append(('v0.2`s back-matter row cell :%s is a row line' % x, ed[int(x) - 1].startswith('| ') and int(x) < cut2 and re.match(r'^\| [A-Z]{2}-\d\d \| ', ed[int(x) - 1]) is not None))
    for c, ln in P['tables'].items():
        checks.append(('table %s header on :%d' % (c, ln), ed[ln - 1] == HEADER3))
    for c, ln in P['heads'].items():
        checks.append(('cluster heading %s on :%d' % (c, ln), ed[ln - 1].startswith('## ')))
    for c, ln in P['mutual'].items():
        checks.append(('mutual-light line %s on :%d' % (c, ln), ed[ln - 1].startswith('Read in mutual light')))
    for k in ('version', 'bullet', 'routes', 'test1', 'verdicts', 'face_head', 'clause_line', 'rest_head'):
        checks.append(('%s on :%d' % (k, P[k]), bool(ed[P[k] - 1].strip())))
    for m in re.finditer(r'\| :(\d+) \| :(\d+) \| ', bm3):
        a_, b_ = int(m.group(1)), int(m.group(2))
        x = [y for y in E['rew'] if y['v3'] == a_ and y['v2'] == b_]
        checks.append(('the rewrites table`s :%d <- :%d' % (a_, b_), bool(x) and ed[a_ - 1] == x[0]['new']))
    checks.append(('the clause line cited at :%d' % P['clause_line'], ('(:%d)' % P['clause_line']) in bm3 and ed[P['clause_line'] - 1].startswith('**The clause’s verdict')))
    bank = rd('b605_edition_FINDINGS_STAND.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v0.2') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b605 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (w[:100], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b605_repin.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after the edition commit: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602's list
    ### at v0.20, the χ page from b603's at v0.21; no Lean call). Writes the page only when it changed, and data/b605_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b605_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, C.HOLD_MB))
    if 0 <= fm < C.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    src_out = os.path.join(D, PROBE[k])
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), pdir, src_out)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b605_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), log=log)
    put_json('b605_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b605 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b605_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b605_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H28a', 'H28b', 'H28c', 'H39a', 'H39b', 'H39c', 'H39d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _only_placement(X):
    prev = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, PNAME['chi'])], capture_output=True).stdout.decode('utf-8', 'replace').split(NL)
    if not prev or not X.get('diff'):
        return False
    try:
        a, b = prev.index('## Placement'), prev.index('## Correspondence')
    except ValueError:
        return False
    for h in X['diff']:
        m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+', h)
        if m:
            s = int(m.group(1))
            if not (a + 1 <= s <= b + 1):
                return False
    return True


def scores():
    VB, H, E = jl('b605_verdicts.json'), jl('b605_h28.json'), jl('b605_edition.json')
    Z, X = jl('b605_page_zeta.json'), jl('b605_page_chi.json')
    rp = rd('b605_repin.txt')
    S9, XX = h39()
    dark = XX['dark']
    n1_bad = [k for k in dark if V.NEW[k]['kind'] in V.RULED_FOUR]
    nar = XX['nar']
    hs = [H.get(k) for k in ('H28a', 'H28b', 'H28c')]
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle',
                                                                               'SIDE-global-section')}
    kern_ok = kern == {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
                       'SIDE-global-section': '3528bcf'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b605_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    if not trail_landed and 'OPEN_TRAILS.md' not in pp_ch:
        want_pp = [x for x in want_pp if x != 'OPEN_TRAILS.md']
    v2_same = g(PP, 'rev-parse', 'HEAD:' + ED2).strip() == E.get('v2_blob') and not g(PP, 'status', '--porcelain', '--', ED2).strip()
    cur_same = g(PP, 'rev-parse', 'HEAD:' + CUR).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip() and not g(PP, 'status', '--porcelain', '--', CUR).strip()
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b605_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b604_closing_push_out.txt'))
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    arms2 = rd('b605_page_arms_c2.txt')
    xplace = _only_placement(X)
    S = dict(
        H28a=(H.get('H28a'), 'every MOVED-IN-MEANING row (%d, the rows whose verdict changed) resolves to its verdict-change row citing the verdict '
                             'bank by line: %d' % (len(H.get('h28a_rows') or []), sum(1 for x in H.get('h28a_rows') or [] if x['bank_ok'] and x['cites_bank']))),
        H28b=(H.get('H28b'), 'the body differs by %+d against at most %d (strict, every rewrite keeping its segments: %d); no sentence moved to '
                             'back matter, the clause of (R215)(3) not invoked' % (H.get('body_dn', 0), H.get('allowed', 0), H.get('strict', 0))),
        H28c=(H.get('H28c'), 'the scanner %s (live uses %s); sentences beyond the ceiling in the body %s' % ('CLEAN' if H.get('clean') else 'NOT CLEAN', H.get('live'), H.get('beyond'))),
        H39a=(S9['H39a'][0], S9['H39a'][1]),
        H39b=(S9['H39b'][0], S9['H39b'][1]),
        H39c=(S9['H39c'][0], S9['H39c'][1]),
        H39d=(S9['H39d'][0], S9['H39d'][1]),
        N1=('HELD' if not n1_bad else 'REFUTED', 'DARK rows %s, their kinds %s ; a compiled identity, census, method theorem or face among them: %s' % (
            dark, {k: V.NEW[k]['kind'] for k in dark}, n1_bad or 'none')),
        N2=('HELD' if len(V.FACE_GROUP) >= 7 else 'REFUTED', 'the FACE group of h2_sign, the located clause: %d rows' % len(V.FACE_GROUP)),
        N3=('HELD' if len(nar) >= 2 * len(dark) else 'REFUTED', 'NOT A ROUTE %d against DARK %d (at least two to one: %d)' % (len(nar), len(dark), 2 * len(dark))),
        N4=('HELD' if all(x == 'HOLDS' for x in hs) and H.get('held') is None else 'REFUTED', 'H28a-H28c: %s ; held %s' % (
            dict(zip(('H28a', 'H28b', 'H28c'), hs)), H.get('held'))),
        N5=('HELD' if kern_ok and v2_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; every kernel`s main unmoved %s; v0.2 unedited %s; the current version unedited %s; PLACE-papers %s (wanted %s); '
            'relay files beyond the act`s banks, tools and the table %s%s' % (kern_ok, v2_same, cur_same, pp_ch, want_pp, relay_beyond,
                                                                            '' if trail_landed else ' ; the trail record pending')),
        S1=('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        S2=('HELD' if not H.get('carried_bad') else 'REFUTED', 'every non-blank v0.2 line carried verbatim, re-pinned or rewritten with its old '
                                                               'wording in the back matter: %d ; failing %s' % (H.get('carried_ok', 0), H.get('carried_bad'))),
        S3=('HELD' if X.get('changed') is True and xplace else 'REFUTED', 'the χ page`s re-emission changes only its Placement block: changed %s ; '
            'every changed line inside Placement %s' % (X.get('changed'), xplace)),
        S4=('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s (the edition names nodes of both)' % (
            Z.get('changed'), X.get('changed'))),
        S5=('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
            'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    )
    put_json('b605_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


TITLE = ('## The sieve table at v0.3: NOT A ROUTE as the third verdict, the faces of the located clause under one verdict, {B} BRIGHT, '
         '{D} DARK, {N} NOT A ROUTE, {F} FACE rows')
TRAIL_HEAD = ('### b605 — lane three, act thirty-two under (R215): the sieve table at v0.3 -- the verdict column re-read with NOT A ROUTE '
              'as a third verdict and the faces of one clause under one verdict')


def _title():
    c = jl('b605_verdicts.json')['counts']
    return TITLE.replace('{B}', str(c[V.BRIGHT])).replace('{D}', str(c[V.DARK])).replace('{N}', str(c[V.NAR])).replace('{F}', str(c[V.FACE]))


def _finding_text():
    S, VB, H, E = jl('b605_scores.json'), jl('b605_verdicts.json'), jl('b605_h28.json'), jl('b605_edition.json')
    rl = jl('b605_record_lines.json')
    w1, w2, hc = [x['line'] for x in rl['lines']]
    ec = _pp_commit('b605 (R215)(4): ' + ED)
    zc, xc = _pp_commit('b605 (R215)(4): ' + PAGE), _pp_commit('b605 (R215)(4): ' + DIR_PAGE)
    c = VB['counts']
    t = _title()
    e = ['', t, '',
         '*Filed at b605 on the author’s ruling `(R215)`. Banks: relay `data/b605_reads.txt`, `data/b605_verdicts.txt`, '
         '`data/b605_edition_FINDINGS_STAND.txt`, `data/b605_edition_termscan.txt`, `data/b605_repin.txt`, `data/b605_page_zeta.json`, '
         '`data/b605_page_chi.json`, `data/b605_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R215)`(4)). PLACE-papers `%s` (commit %s), beside v0.2, unedited, and the current version, unedited. The head '
         'restated: the verdict bullet with four words, the one sentence that the five tests are tests of routes, test 1’s scope narrowed to '
         'a statistic or average over the zeros offered as a placement argument, the verdict counts. The verdict column re-read row by '
         'row, each change with its old and new verdict and its reason in one line, banked first (relay data/b605_verdicts.txt); the bench, '
         'the reading rows and the dated blocks unchanged; v0.2’s back matter carried whole with its own-line cells re-pinned.' % (ED, ec), '',
         '**The verdicts.** %d FACE rows of the located clause under its one verdict, BRIGHT by test 2 (the clause carries the explicit '
         'formula’s prime sum at ζ and at χ): `h2_sign_iff_rh`, `ch_iff_rh`, the forall_upto pair, `li_nonneg_iff_rh` with its register-4 '
         'and Taylor forms, `arith_limit_nonneg_iff_rh`, `h2_sign_chi_iff_grh_chi`, `h2_sign_cfg_iff_target` and `family_theorem`. %d BRIGHT '
         'by test 4: the Li ladder’s arithmetic end, the Keiper face (`keiperTaylorIdentity_of`), and its FINITE rung `liCoeff_one_pos`. %d '
         'DARK: the proportion row and the three density rows by test 1, the Dedekind reading by test 3. %d NOT A ROUTE: the compiled '
         'identities, the schema’s method theorems, test 2’s own instruments, the record’s statements, the censuses, the Trivium and '
         'cosmology rows.' % (c[V.FACE], c[V.BRIGHT], c[V.DARK], c[V.NAR]), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '. H39a refuted in its first clause by the Dedekind '
         'reading, a route darkened at test 3 and neither a statistic nor refuted at the Epstein configuration; its second clause holds (no '
         'DARK row is an identity, census, method theorem or face). H39c refuted: one FINITE rung reads BRIGHT; “the forall_upto window” '
         'names no row, the pair being faces and no declaration fixing one rung at a finite support length (relay data/b605_verdicts.txt).', '',
         '**The pages.** Both re-emitted after the edition commit from their banked probes, no Lean call: the ζ page (PLACE-papers %s) and '
         'the χ page (%s), each committed alone, the edition entering their Placement.' % (zc, xc), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition re-reads b604’s entry (:7060), whose 6 BRIGHT and 78 DARK it corrects '
         'under the ruling recorded at :%d, and b601’s and b602’s Keiper rows (:6972, :6998), now the Li ladder’s bright end and its rung; '
         'the H28b clause (OPEN_TRAILS :%d) reads b604’s reorganisation; and it is re-read in turn by CP-8’s monograph v6, whose spine the '
         'sieve table at v0.3 is. It strengthens the programme’s offering of the clause and its compiled faces: one clause, its faces '
         'counted under one verdict, and the routes that remain named.' % (w2, hc), '',
         '**The record lines.** b604’s weight at FINDINGS :%d; the verdict-column correction, the navigator’s mis-specification and the '
         'seat’s application recorded as correct, at :%d; the H28b clause for a reorganising edition at OPEN_TRAILS :%d, addressed to the '
         'form’s block :11864.' % (w1, w2, hc), '',
         '**Next.** Per `(R215)`(5): b606, CP-8 -- the monograph’s v6, the sieve table at v0.3 its spine and the eleven ceiling uses of relay '
         'data/b584_ceiling_census.txt its work-list, by the form, in as many acts as the monograph’s length prices. The author rules on the '
         'closing.', '',
         '*Nothing deposits; no keystone edited beyond the edition written beside its prior version; README and REGISTRY unwritten; nothing '
         'here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        print(e)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b605_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b605_scores.json'), jl('b605_findings.json'), jl('b605_record_lines.json')
    w1, w2, hc = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R215) ratified.** (1) b604 at its weight. (2) The verdict column read: the navigator’s mis-specification, the seat’s '
             'application correct; NOT A ROUTE as a third verdict; the faces of one clause under one verdict. (3) H28b for a reorganising '
             'edition. (4) The sieve table at v0.3. (5) The act after: b606, CP-8.', '',
             '**Entered:** FINDINGS.md:%d (b604’s weight), :%d (the verdict column, read), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (the H28b clause, addressed to :11864); this record; PLACE-papers `%s` (the edition, beside v0.2, unedited); '
             'both pages re-emitted.' % (w1, w2, fj['entry_line'], hc, ED), '',
             '**Resolved by the seat, for the author’s strike:** the χ and family forms in the located clause’s FACE group by the ruling’s '
             'letter, `h2_sign_cfg_iff_target` beside them by the ruling’s reason; the clause’s verdict BRIGHT, named as decided by test 2; '
             'the Keiper face read as `keiperTaylorIdentity_of`, λ₁’s closed form as the identity its rung reads (NOT A ROUTE); the density '
             'rows read as the statistics test 1 still asks; the Dedekind reading kept a route, DARK by test 3; the ζ page read at its own '
             'pin v0.20 and `liCoeff_one_pos` in KeiperSign.lean, two fact corrections to the ferry’s letter recorded as the navigator’s. '
             'No prompt was put (relay data/b605_author_answers.txt).', '',
             '**Defects** (relay data/b605_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R215)`(5), b606, CP-8 -- the monograph’s v6 with the sieve table at v0.3 as its spine and the eleven ceiling '
             'uses as its work-list, in as many acts as its length prices; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit '
             'left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        print(e)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b605_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b605_trail.json')['line'])


def desk():
    S = jl('b605_scores.json')
    HK = ('H28a', 'H28b', 'H28c', 'H39a', 'H39b', 'H39c', 'H39d')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b605 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c and H39a-H39d, (R215)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H39 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b605_defects.txt').rstrip(NL).split(NL)
    put_txt('b605_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b605_scores.json'), jl('b605_findings.json'), jl('b605_trail.json'), jl('b605_record_lines.json')
    Z, X, VB = jl('b605_page_zeta.json'), jl('b605_page_chi.json'), jl('b605_verdicts.json')
    c = VB['counts']
    L = ['b605 -- THE COMPONENTS, BANKED UNDER (R215).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b604`s closing push-out relay %s ; push-b604* branches deleted by '
         'name (data/b605_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b605_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b604`s weight FINDINGS :%d ; the verdict column read :%d ; the H28b clause OPEN_TRAILS :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the verdicts data/b605_verdicts.txt ; BRIGHT %d, DARK %d, NOT A ROUTE %d, FACE %d ; H39a %s, H39b %s, H39c %s, H39d %s' % (
             c[V.BRIGHT], c[V.DARK], c[V.NAR], c[V.FACE], S['H39a'][0], S['H39b'][0], S['H39c'][0], S['H39d'][0]),
         '### COMPONENT 3 : the edition %s ; the diff data/b605_edition_FINDINGS_STAND.txt ; H28a %s, H28b %s, H28c %s' % (
             ED, S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b605_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b606, CP-8 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b605_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b605_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
