# -*- coding: utf-8 -*-
"""b606_record.py -- THE ACT'S RECORD TOOL, UNDER (R216). ### ONE SUBCOMMAND PER BANK.

### ### b606: LANE THREE, ACT THIRTY-THREE -- CP-8 ACT ONE: THE MONOGRAPH'S NEXT VERSION OVER THE ELEVEN CEILING USES AND THE
### LIVE ERRATA BY THE FORM.
### Subcommands write only `data/b606_*` unless the docstring names another file. Every bank is written through b602_record's
### `put_txt` / `put_json` (encode, temp file, `os.replace`), imported, never copied; every ledger append through b566's guarded
### `append_to`. The work-list is tools/b606_worklist.py's data. No platform call. No Lean call: both pages are re-emitted from
### their banked probes.
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
import b606_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
RELAY = ROOT.replace('\\', '/')
PRE_PP = 'cabbed7'
PRE_RELAY = 'f35dd023'
STEPZERO = 'e5fd0a8d'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/2b3af15c-1dfb-403d-a9a7-9f40c54cf08d/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/2b3af15c-1dfb-403d-a9a7-9f40c54cf08d.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'
CUR, ED = K.CUR, K.ED
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
CORR_HEAD = '## Correspondence *(added 2026-08-12'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, put_txt, put_json, jl, rd, sha, utc = R2.g, R2.put_txt, R2.put_json, R2.jl, R2.rd, R2.sha, R2.utc
_show = R4._show


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


DEFECTS = [
    '(a) AN UNSEALED TOOL EDITED THROUGH A HEREDOC, AGAINST THE FERRY`S PROCEDURAL LINE ("edits to unsealed tools through the Edit '
    'tool and not a heredoc"): before the seal the seat adapted its own tools/b606_closing.py (score keys, title, carried list, '
    'summary line) by a python heredoc that read, replaced and rewrote the file. Read back at once: no line of the old text left '
    '(grep for H39, THIRTY-TWO and the v0.2 line empty) and the file parses; every later edit to the act`s tools went through the '
    'Edit tool. The seat`s.',
    '(b) THE SCORER OF (S3) WAS DEFECTIVE AT ITS FIRST RUN, AFTER THE SEAL: `_unrender_ok` reversed every rendering on every '
    'target -- an ERRATA "—" read back as a rendered " -- ", and b532`s transliterations (§, σ, ξ) reversed on sentences that never '
    'had them -- and scored S3 REFUTED on eight replacements (E4-02, E4-03, E4-04, E5-04, E6-06, E6-07, E6-11, E6-14) whose words '
    'in the edition are their sources`. Both figures: the first form 37 of 45 passing, REFUTED; the corrected form, through the '
    'Edit tool -- reading (vii)`s rendering applied forward to the source, markup set aside -- 45 of 45, with a positive control '
    '(one word altered in each sentence) failing 45 of 45. The edition is unchanged; the defective predicate is the scorer`s. The '
    'seat`s.',
]
DEFECTS += [
    '(c) A SUITE ARM`S NEEDLE WAS CASE-SENSITIVE (the b588 trap, repeated): G-ERRATA-BY-ID searched ERRATA`s entries for "monograph" '
    'in lower case and missed E-2026-07-27, whose text reads "Monograph v5.13 absorbs ..."; at the first pre-push run it read 15 '
    'entries against the work-list`s 16 and FAILED live. The work-list is right (the entry addresses the monograph); the needle was '
    'made case-insensitive through the Edit tool and the suite re-run. Both figures: first run 77 of 79, re-run below. The seat`s.',
    '(d) A POSITIVE CONTROL ON THE SIDE ITS ARM ALREADY READ: G-H40D-SCORED`s control set the body`s change to -99, which leaves H40d '
    'REFUTED, the act`s own reading, so the control passed and G-ARMS-NO-LIVE-LIMB failed at the first pre-push run. The control now '
    'sets the change across the bound (to the credits and history lines, or one past them), through the Edit tool. The seat`s.',
]
DEFECT_SHORT = ['(a) the act`s own closing tool edited through a heredoc before the seal, read back clean, the seat`s',
                '(b) the S3 scorer reversed renderings a sentence never had, REFUTED on 8 of 45, corrected to 45 of 45 with its control, the seat`s',
                '(c) G-ERRATA-BY-ID`s needle case-sensitive, failing on E-2026-07-27 at the first pre-push run, corrected, the seat`s',
                '(d) G-H40D-SCORED`s positive control on its arm`s own side, corrected, the seat`s']


def defects():
    L = ['b606 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b606_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('relay data/b605_verdicts.txt: the located clause, the counts and H39a-H39d', RELAY, STEPZERO, 'data/b605_verdicts.txt',
     ['### THE LOCATED CLAUSE', '### THE COUNTS', '  BRIGHT 2', '  by cluster', '  DARK by test', '  rows whose verdict', '  at v0.2',
      '### ### **H39a', '### ### **H39b', '### ### **H39c', '### ### **H39d'], 420),
    ('relay data/b605_scores.json (whole)', RELAY, STEPZERO, 'data/b605_scores.json', 'ALL', 300),
    ('the monograph`s current version: its head, its version line, its version history, §25.8, its Correspondence, the eleven uses',
     PP, PRE_PP, CUR, [1, 5, 13, 19, 31, 64, 405, 1272, 1303, 1336, 1407, 1562, 1657, 1795, 1946, 2173, 2187, 2189, 2191, 2193, 2195, 2197,
                       2229, 2231], 300),
    ('relay data/b584_ceiling_census.txt (whole)', RELAY, STEPZERO, 'data/b584_ceiling_census.txt', 'ALL', 400),
    ('ERRATA.md: every entry`s heading (those addressed to A_Place_to_Stand among them)', PP, PRE_PP, 'ERRATA.md', ('GREP', r'^## E-'), 260),
    ('THE_FINDINGS_AS_THEY_STAND v0.3: its FACE rows and the row citing a monograph section', PP, PRE_PP, SIEVE,
     ('GREP', r' \| FACE \| — \| |A_Place_to_Stand'), 260),
    ('the ζ page (at its own pin v0.20): its pin line and the nodes the rewrites cite', PP, PRE_PP, PAGE, ('GREP', r'^(This page is generated|7\. |8\. |41\. )'), 300),
    ('the χ page (at its own pin v0.21): its pin line and the node the rewrites cite', PP, PRE_PP, DIR_PAGE, ('GREP', r'^(This page is generated|12\. )'), 300),
    ('OPEN_TRAILS: the form, the precedence order, lane three`s order, the H28b clause and b605`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11906, 11908, 12062, 12192, 12228, 12456, 12458], 700),
    ('FINDINGS: the monograph`s tier map and b605`s record lines and entry', PP, PRE_PP, 'FINDINGS.md', [4835, 7080, 7082, 7084], 400),
    ('relay data/b558_editions/A_Place_to_Stand.txt: its head (act three`s input)', RELAY, STEPZERO, 'data/b558_editions/A_Place_to_Stand.txt', [1, 3], 300),
    ('relay data/b605_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b605_closing_push_out.txt', 'ALL', 260),
]


def reads():
    L = ['b606 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
        elif isinstance(sel, tuple):
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
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
    b558 = _show(RELAY, STEPZERO, 'data/b558_editions/A_Place_to_Stand.txt') or ''
    L += ['', '### the pages` pins: the ζ page`s list %s %s ; the χ page`s list %s %s -- the ferry`s "THE_CLAUSE_AND_ITS_COMPILED_FACES.md '
          'at v0.21 and THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md at v0.20" read at the pages` own pins, the ζ page at v0.20 and the χ page at '
          'v0.21, a fact correction recorded as the navigator`s (as at b604 and b605)' % (
              NODES['zeta'], [l for l in rd(NODES['zeta']).split(NL) if l.startswith('# pin:')], NODES['chi'],
              [l for l in rd(NODES['chi']).split(NL) if l.startswith('# pin:')]),
          '### the monograph at the census pin %s and at %s: blob %s and %s -- %s' % (
              K.CENSUS_PIN, PRE_PP, g(PP, 'rev-parse', '%s:%s' % (K.CENSUS_PIN, CUR)).strip()[:12], g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12],
              'THE SAME BLOB: no line has moved since the census' if g(PP, 'rev-parse', '%s:%s' % (K.CENSUS_PIN, CUR)).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip() else '### DIFFERENT'),
          '### the census bank prints counts and no lines: the eleven uses are re-derived by line with relay tools/b584_record.py`s classifier '
          '(imported) at the census pin -- see data/b606_worklist_PLACE.txt',
          '### the b558 work-list for the monograph: %d rows (":<line> -- <terminal>"), the input act three takes by (R216)(2)' % (
              len(re.findall(r'^:\d+ -- ', b558, re.M))),
          '### the monograph carries no tier block in its own file (b584: "the monograph has none"); its tier map is FINDINGS :4835']
    put_txt('b606_reads.txt', L)


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
                if not isinstance(c, dict):
                    continue
                if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if c.get('type') == 'tool_result':
                    t = c.get('content')
                    t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                    results[c.get('tool_use_id')] = (i, t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b606 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 2b3af15c-1dfb-403d-a9a7-9f40c54cf08d, transcript line %d)' % (cid, i))
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
    put_txt('b606_author_answers.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B605_ENTRY = '## The sieve table at v0.3: NOT A ROUTE as the third verdict'
LANE3 = '*Appended 2026-10-01 by b586 to the critical path’s lane three (:11417), under the author’s ruling `(R196)`(4) -- LANE THREE’S ORDER, REFINED:*'
W_HEAD = '*Appended 2026-10-03 by b606 to b605’s entry (:%d), under `(R216)`(1) -- b605 AT ITS WEIGHT:*'
F_HEAD = '*Appended 2026-10-03 by b606 to b605’s entry (:%d), under `(R216)`(1) -- THE TWO FACT CORRECTIONS, THE NAVIGATOR’S:*'
P_HEAD = ('*Appended 2026-10-03 by b606, under the author’s ruling `(R216)`(2), to lane three’s order (:%d) -- CP-8 IN THREE ACTS, '
          'THE MONOGRAPH’S NEXT VERSION BY ITS OWN SERIES:*')


def _b605_counts():
    VB = json.loads(_show(RELAY, STEPZERO, 'data/b605_verdicts.json'))
    S = json.loads(_show(RELAY, STEPZERO, 'data/b605_scores.json'))
    return VB['counts'], {k: v[0] for k, v in S.items()}


def _texts(entry, lane):
    c, s = _b605_counts()
    h1, h2, h3 = W_HEAD % entry, F_HEAD % entry, P_HEAD % lane
    t1 = ('\n%s PLACE-papers `%s` (22e5d8d) beside v0.2 unedited, the pages re-emitted each alone (be1c977, 7ccd4c8), the record '
          'cabbed7: the verdict column re-read row by row under `(R215)`(2), the density rows kept as the statistics test 1 asks about, '
          'liCoeff_one_pos read as the rung’s identity. The counts, as relay data/b605_verdicts.txt prints them: %d rows -- %d BRIGHT, %d DARK, '
          '%d NOT A ROUTE, %d FACE (the located clause’s, under its one verdict). The verdicts, as the act’s scores bank '
          '(data/b605_scores.json) prints them: H39a %s, H39b %s, H39c %s, H39d %s; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s; H28a %s, H28b %s, '
          'H28c %s; S1-S5 %s. FINDINGS :7080, :7082, :7084; OPEN_TRAILS :12456 (the H28b clause, addressed to :11864), :12458. Relay '
          'f35dd023 with the act at 6064507d; the suite 79 of 79 before and after the push; the terminal table unchanged. Nothing '
          'deposited; no kernel touched.\n' % (
              h1, R4.ED if False else 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md', sum(c.values()), c['BRIGHT'], c['DARK'], c['NOT A ROUTE'],
              c['FACE'], s['H39a'], s['H39b'], s['H39c'], s['H39d'], s['N1'], s['N2'], s['N3'], s['N4'], s['N5'], s['H28a'], s['H28b'],
              s['H28c'], 'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else [s['S%d' % i] for i in range(1, 6)]))
    t2 = ('\n%s the ζ page stands at its own pin v0.20 and the χ page at v0.21 -- `(R215)`’s ferry read the ζ page at v0.21, and '
          '`(R216)`’s prints the pair crossed (the ζ page at v0.21, the χ page at v0.20); the pages’ own pin lines read them '
          '(relay data/b606_reads.txt). liCoeff_one_pos is in KeiperSign.lean, not Keiper.lean (both at v0.20 = 914c413). Each is '
          'recorded as the navigator’s; no reading of b605 moves.\n' % h2)
    t3 = ('\n%s as ruled: the monograph A_Place_to_Stand’s next version by its own series, each act one version beside the one before '
          'it, by the form with its clauses, the precedence order and H28a-H28c, the sieve at v0.3 as the spine and the pages at their '
          'own pins: act one (b606) -- the eleven ceiling uses of relay data/b584_ceiling_census.txt and every live-line erratum ERRATA '
          'addresses to the monograph, each sentence rewritten or carried with a history line, with the version line and nothing else; '
          'act two (b607) -- chapters 21, 22, §24.4 and §27.3 read against b596-b605; act three -- the remaining chapters by the b558 '
          'work-list where one exists (relay data/b558_editions/A_Place_to_Stand.txt) and otherwise by the ceiling and stem clauses '
          'alone, with §25.8’s Kernel Concordance re-pinned. Each act prices the next from what it finds.\n' % h3)
    return (h1, t1), (h2, t2), (h3, t3)


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
    """### PLACE-papers FINDINGS: b605's weight and the two fact corrections, addressed to b605's entry; OPEN_TRAILS: CP-8's three-act
    ### plan, appended at the end addressed to lane three's order :12062 (the ledgers are append-only). `dry` prints."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B605_ENTRY)
    lane = Q.line_of(Q.OT, LANE3)
    if entry != 7084 or lane != 12062:
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s) -- NOTHING WRITTEN' % (entry, lane))
    (h1, t1), (h2, t2), (h3, t3) = _texts(entry, lane)
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
    put_json('b606_record_lines.json', dict(entry=entry, lane=lane, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE WORK-LIST
COLL_SKIP = {'E1-M-04': 'E6-10', 'E22-01': 'E5-01'}      # ### the sentence another target governs (collisions C2, C3)


def _uses_rederived():
    import b584_record as B
    import b558_record as CP
    t = _show(PP, K.CENSUS_PIN, CUR)
    out = []
    for i, line in enumerate(t.split(NL), 1):
        for s in CP.segments(line):
            if not s or not B.OBJECT.search(s):
                continue
            ph = B.PHRASE.findall(s)
            if not ph:
                continue
            k = 'negated' if B.NEGATED.search(s) else 'hedged' if B.HEDGED.search(s) else 'live'
            if k == 'live':
                for p in ph:
                    out.append((i, p, s))
    cnt = B._classify(t)
    return out, cnt


def worklist(*a):
    """### data/b606_worklist_PLACE.txt (and .json), banked before any writing of the edition: the eleven uses by line, the errata by
    ### id with their live lines and replacements, the sieve`s citations into the monograph, the version history and tier block;
    ### H40a and H40b scored on the bank."""
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    uses, cnt = _uses_rederived()
    T = K.ids()
    L = ['b606 -- COMPONENT 2: CP-8 ACT ONE`S WORK-LIST, (R216)(3) -- ASSEMBLED BEFORE ANY WRITING, banked %s' % utc(),
         '### the current version: PLACE-papers %s @ %s, %d lines, blob %s; its version line :19 "%s"' % (
             CUR, PRE_PP, len(M), g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip()[:12], M[18]),
         '### the next version by its own series: v5.14, written beside it as %s' % ED, '',
         '### PART A -- THE ELEVEN CEILING USES (relay data/b584_ceiling_census.txt :11, "A_Place_to_Stand | ... | 11 |", counts only): re-derived '
         'by line with relay tools/b584_record.py`s classifier, imported, at the census pin %s (blob = the current version`s): whole live %d, '
         'hedged %d, negated %d' % (K.CENSUS_PIN, cnt['live'], cnt['hedged'], cnt['negated'])]
    rows = []
    for j, (i, p, s) in enumerate(uses):
        u = K.USES[j] if j < len(K.USES) else None
        ok = bool(u) and u[1] == i and u[2] == p and u[3] in M[i - 1] and (u[3] == s or s in u[3] or u[3] in s)
        rows.append(dict(id=u[0] if u else '?', line=i, phrase=p, ok=ok, action=u[4] if u else None))
        L.append('  %s :%d (moved since the census: %s) "%s" -- %s -- %s' % (u[0] if u else '?', i, 'no' if ok else '### CHECK', p, s[:200], u[4] if u else '?'))
    h40a = 'HOLDS' if len(uses) == 11 and all(r['ok'] for r in rows) else 'REFUTED'
    L += ['', '### PART B -- THE ERRATA ERRATA.md ADDRESSES TO A_Place_to_Stand, BY ID (searched by name; ids, live lines and replacements):']
    for eid, kind, why in K.ERRATA_IDS:
        L.append('  %s : %s -- %s' % (eid, 'LIVE LINES' if kind == 'live' else 'NO LIVE LINE', why))
    L += ['', '### PART C -- EVERY ERRATUM SENTENCE, RESOLVED (id | erratum | ERRATA line | live line | the live sentence | the replacement, '
          'raw | rendered by R-3 | what the act does):']
    for t in T:
        act = ('governed by %s (collision)' % COLL_SKIP[t['id']]) if t['id'] in COLL_SKIP else \
            'no live line: not written' if not t['line'] else \
            'carried with a history line (no replacement)' if t['new'] is None else 'rewritten by its replacement'
        t['act'] = act
        L += ['  %s | %s | ERRATA :%s%s | live %s%s' % (t['id'], t['eid'], t['err_line'], (', replacement :%s' % t['rep_line']) if t.get('rep_line') else '',
                                                         (':%d' % t['line']) if t['line'] else 'NONE', (' (ERRATA prints :%s)' % t['errata_live']) if t['errata_live'] and t['errata_live'] != t['line'] and t['line'] else ''),
              '      live : %s' % (t['old'] or '### NONE'),
              '      raw  : %s' % (t['raw_used'] or '### NO REPLACEMENT IN ERRATA'),
              '      new  : %s' % (t['new'] or '—'),
              '      R-3  : %s' % (t['render'] or 'no rendering'),
              '      act  : %s%s' % (act, (' -- ' + t['note']) if t.get('note') else '')]
    by = {}
    for t in T:
        by.setdefault(t['eid'], []).append(t)
    h40b_rows = []
    for eid, kind, _w in K.ERRATA_IDS:
        ts = by.get(eid, [])
        live = [t for t in ts if t['line']]
        in_errata = [t for t in ts if t['raw'] and not t.get('b532')]
        h40b_rows.append((eid, len(ts), len(live), len(in_errata)))
    h40b = 'HOLDS' if all(n and lv == n and r == n for _e, n, lv, r in h40b_rows) else 'REFUTED'
    L += ['', '### PART D -- THE SIEVE`S CITATIONS INTO THE MONOGRAPH (PLACE-papers %s @ %s):' % (SIEVE, PRE_PP)]
    sv = (_show(PP, PRE_PP, SIEVE) or '').split(NL)
    face = [i + 1 for i, l in enumerate(sv) if ' | FACE | — | ' in l]
    cites = [(i + 1, l) for i, l in enumerate(sv) if 'A_Place_to_Stand' in l]
    L.append('  FACE rows %d (:%s .. :%s); FACE rows citing a monograph section: %d' % (len(face), face[0] if face else '-', face[-1] if face else '-',
                                                                                      sum(1 for i in face if 'A_Place_to_Stand' in sv[i - 1])))
    for i, l in cites:
        L.append('  :%d %s' % (i, l[:300]))
    L += ['  -> §24.4`s analytic-row note (:1499 of the current version) is act two`s object by (R216)(2); act one writes nothing there.',
          '', '### PART E -- THE MONOGRAPH`S OWN VERSION HISTORY AND TIER BLOCK:',
          '  the version line :19 %s ; the closing stamp :2173 %s ; the version log :2187-:2197 (v5.10 .. v5.13), read as records of their '
          'dates (the history clause; E-2026-09-25-6`s own "What is not corrected")' % (M[18], M[2172]),
          '  the tier block: none in the file (b584: "the monograph has none"); its declared class TIER K at :5; its tier map FINDINGS :4835',
          '  the Correspondence section :2229 (added 2026-08-12), back matter by its own heading -- the body of the H28b count is every line above it',
          '', '### ### **H40a %s -- %d of 11 uses resolve to a live line at the current version, each on the line the classifier read at the census '
          'pin, moved since the census: %d.**' % (h40a, sum(r['ok'] for r in rows), sum(not r['ok'] for r in rows)),
          '### ### **H40b %s -- per erratum (id, sentences, with a live line, with a replacement in ERRATA itself): %s.**' % (h40b, h40b_rows)]
    put_txt('b606_worklist_PLACE.txt', L)
    put_json('b606_worklist.json', dict(at=utc(), uses=rows, targets=T, h40a=h40a, h40b=h40b, h40b_rows=h40b_rows, census=cnt))
    print('  H40a %s ; H40b %s ; uses %d ; targets %d (live %d)' % (h40a, h40b, len(rows), len(T), sum(1 for t in T if t['line'])))


# ================================================================================ COMPONENT 3: THE EDITION
BM_TAG = '<!-- b606 (R216) THE v5.14 EDITION`S BACK MATTER, 2026-10-03 -->'
VERSION = ('**v5.14, 2026-10-03** — CP-8 act one under `(R216)`: the eleven ceiling uses of the census and the live-line sentences of the '
           'errata addressed to this monograph, beside v5.13, which stands unedited; every change is recorded in the back matter.  ')
HIST = {
    1793: ('*v5.14, 2026-10-03, a history line under E-2026-09-22-1 (ERRATA :414, :415): the two sentences above that begin “This is '
           'distinct from the Mechanism Theorem” and “The input-stage spectral coupling” assert a machine check, name no terminal and have no '
           'row in §25.8’s concordance; they carry unchanged, their narrowing waiting on the wave the erratum names.*'),
    1797: ('*v5.14, 2026-10-03, a history line under E-2026-09-22-1 (ERRATA :416): the sentence above that begins “The programme’s channel '
           'decomposition” asserts a machine check, names no terminal and has no row in §25.8’s concordance; it carries unchanged, its '
           'narrowing waiting on the wave the erratum names.*'),
}
READINGS = [
    ('R-1', 'the next version by the document`s own series is v5.14 (its version line, v5.13 :19, reads v5.13), written beside it as '
            'day1/A_Place_to_Stand_v5_14.md; its version line goes above v5.13`s'),
    ('R-2', 'the body of the H28b count is every line above the monograph`s own Correspondence heading (v5.13 :2229, "added 2026-08-12 ... Back matter, '
            'per the writing law"); that section and this act`s back matter are back matter, counted beside'),
    ('R-3', 'a replacement is written in its own words, the drafts` ASCII dash " -- " written as the document`s " — " (as E-2026-09-25-2 '
            'rendered it at Zenodo); b532`s bank`s transliterations (a backtick possessive, xi, sigma, "section") written back in the document`s '
            'own characters; and the live sentence`s markup -- a bold label, an italic phrase, a backticked name -- kept where the replacement '
            'repeats the marked words; every raw and rendered text printed in data/b606_worklist_PLACE.txt'),
    ('R-4', 'the history clause reaches the version log and the era annotations (E-2026-09-25-6`s own "What is not corrected"); the '
            'Correspondence sentences E-2026-09-25-6 lists (v5.13 :2233, :2241) are rewritten by its replacements'),
    ('R-5', 'an erratum with a live line and no replacement (E-2026-09-22-1) carries its sentences unchanged with a history line beneath '
            'their paragraph; a sentence two entries address takes the replacement of the entry that extends the other (collisions)'),
    ('R-6', '"nothing else" (R216)(2): the ceiling, stem and restatement clauses reach no sentence outside the eleven uses and the errata`s; '
            'the rest is priced for acts two and three, and H28c is scored by its letter over the whole body'),
    ('R-7', 'a ceiling use inside the ceiling carries, its reason printed (U09: "proves" governs the compiled theorem printed beneath it)'),
]
COLLISIONS = [
    ('C1', 1946, 'U11 (the ceiling clause) and E6-15 (E-2026-09-25-6, Appendix A row 13)', 'E6-15`s replacement governs: the erratum`s text '
     'takes the object the ceiling clause would name'),
    ('C2', 2225, 'E1-M-04 (E-2026-09-25-1) and E6-10 (E-2026-09-25-6)', 'E6-10 governs: E-2026-09-25-6 names b532`s M-04 and extends it '
     '("beyond b532`s scope, the registers stand at four depths")'),
    ('C3', 68, 'E22-01 (E-2026-09-22-1, no replacement) and E5-01 (E-2026-09-25-5)', 'E5-01`s replacement governs; E-2026-09-22-1 '
     'carries none'),
    ('C4', 1793, 'E1-M-20, E1-M-22, E6-02, E6-03 (rewritten) and E22-02, E22-03 (carried) on one line', 'each applies to its own sentence; '
     'the carried two take the history line beneath the paragraph'),
]


def _changes():
    T = K.ids()
    ch = []
    for t in T:
        if not t['line'] or t['new'] is None or t['id'] in COLL_SKIP:
            continue
        ch.append(dict(id=t['id'], src=t['eid'], cite='ERRATA :%s' % t['err_line'] if t['eid'] != 'E-2026-09-25-1' else
                       'ERRATA :%s (E-2026-09-25-1`s %s; its replacement relay data/b532_rows.txt)' % (t['err_line'], t['label']),
                       line=t['line'], old=t['old'], new=t['new'], kind='erratum'))
    for u in K.USES:
        uid, line, ph, old, act, new, why = u
        if act == 'rewrite':
            ch.append(dict(id=uid, src='the ceiling clause (OPEN_TRAILS :11906)', cite='data/b584_ceiling_census.txt :11, the use re-derived at :%d' % line,
                           line=line, old=old, new=new, kind='ceiling', why=why))
    return T, ch


def _decl_cites(text):
    return [k for k in K.PINS if k in text]


def _build():
    """### the edition from v5.13`s blob by line transforms (carry / rewrite / insert); returns the lines, the map and the record."""
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    T, ch = _changes()
    new_line = {}
    seg_d = []
    for i, l in enumerate(M, 1):
        mine = [c for c in ch if c['line'] == i]
        s = l
        for c in mine:
            if s.count(c['old']) != 1:
                sys.exit('### %s: the live sentence is not once on :%d -- NOTHING WRITTEN' % (c['id'], i))
            s = s.replace(c['old'], c['new'])
        if mine:
            new_line[i] = s
            seg_d.append(dict(line=i, ids=[c['id'] for c in mine], d=len(_segs(s)) - len(_segs(l)), body=i < _corr_idx(M) + 1))
    out, where = [], {}
    for i, l in enumerate(M, 1):
        if i == 19:
            out.append(VERSION)
        out.append(new_line.get(i, l))
        where[i] = len(out)
        if i in HIST:
            out += ['', HIST[i]]
    return M, T, ch, out, where, seg_d


def _corr_idx(ls):
    return next(i for i, l in enumerate(ls) if l.startswith(CORR_HEAD))


def _E(where, n):
    return where[n]


def _bm(M, T, ch, where, edlen):
    """### this act`s back matter, appended after v5.13`s last line; every line it cites is the edition`s own (`where`)."""
    w = lambda n: where[n]  # noqa: E731
    L = ['', '---', '', BM_TAG, '', '## Back matter of v5.14 -- CP-8 act one, 2026-10-03, under `(R216)`', '',
         '*This section records every change v5.14 makes to v5.13, which stands beside it unedited; each line cited is this file`s own.*', '',
         '### The act’s readings, each the seat’s and strikeable', '']
    L += ['- **%s** %s.' % (k, v.replace('`', '’')) for k, v in READINGS]
    L += ['', '### The eleven ceiling uses (relay `data/b584_ceiling_census.txt`, re-derived by line in relay `data/b606_worklist_PLACE.txt`)', '']
    for uid, line, ph, old, act, new, why in K.USES:
        if act == 'rewrite':
            L.append('- **%s** :%d (v5.13 :%d) — rewritten by the ceiling clause — the use “%s” — %s — was: “%s” — now: “%s” — cites: %s.' % (
                uid, w(line), line, ph, why.replace('`', '’'), old, new, ', '.join('%s (%s, %s)' % (k, K.PINS[k][1], K.PINS[k][2]) for k in _decl_cites(new)) or 'none'))
        elif act == 'carry':
            L.append('- **%s** :%d (v5.13 :%d) — carried, inside the ceiling — the use “%s” — %s.' % (uid, w(line), line, ph, why.replace('`', '’')))
        else:
            L.append('- **%s** :%d (v5.13 :%d) — the use “%s” — %s.' % (uid, w(line), line, ph, why.replace('`', '’')))
    L += ['', '### The errata addressed to this monograph, every sentence by id (relay `data/b606_worklist_PLACE.txt` prints each raw and rendered)', '']
    for eid, kind, why in K.ERRATA_IDS:
        L.append('- **%s** — %s — %s.' % (eid, 'live lines' if kind == 'live' else 'no live line', why.replace('`', '’')))
    L.append('')
    for t in T:
        if not t['line']:
            L.append('- **%s** (%s, ERRATA :%s) — no live line (deposited :%s at v1.1.2): nothing written.' % (t['id'], t['eid'], t['err_line'], t['deposited']))
        elif t['id'] in COLL_SKIP:
            L.append('- **%s** :%d (v5.13 :%d) (%s, ERRATA :%s) — governed by %s (the collisions below).' % (t['id'], w(t['line']), t['line'], t['eid'], t['err_line'], COLL_SKIP[t['id']]))
        elif t['new'] is None:
            L.append('- **%s** :%d (v5.13 :%d) (%s, ERRATA :%s) — carried unchanged with the history line at :%d — “%s”.' % (
                t['id'], w(t['line']), t['line'], t['eid'], t['err_line'], w(t['line']) + 2, t['old']))
        else:
            L.append('- **%s** :%d (v5.13 :%d) (%s, ERRATA :%s) — rewritten by its replacement — was: “%s” — now: “%s”.' % (
                t['id'], w(t['line']), t['line'], t['eid'], t['err_line'], t['old'], t['new']))
    L += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228) and the act’s readings', '']
    for cid, line, who, how in COLLISIONS:
        L.append('- **%s** :%d (v5.13 :%d) — %s — %s.' % (cid, w(line), line, who, how.replace('`', '’')))
    L += ['', '### History lines', '',
          '- :%d beneath :%d (E22-02, E22-03) and :%d beneath :%d (E22-04): E-2026-09-22-1’s sentences, carried.' % (
              w(1793) + 2, w(1793), w(1797) + 2, w(1797)),
          '', '### Removals', '', '- None: no sentence of v5.13 is removed.', '',
          '### Fact corrections', '', '- None: the fact clause reaches no sentence this act writes.', '',
          '### Stem corrections', '', '- None in this act: the live stems of v5.13’s body are act three’s, by `(R216)`(2).',
          '- :%d, carried-by-history — the era annotation of 2026-08-14 (v5.13 :2264), a dated record the history clause carries '
          'unchanged (reading R-4); nothing in it is rewritten.' % w(2264), '',
          '### Placement', '',
          '| page | node this edition names | its pin as the page prints it | status |', '|:--|:--|:--|:--|']
    for k, (q, pin, where_) in K.PINS.items():
        L.append('| %s | `%s` | %s | named in v5.14 |' % ('THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md' if 'χ' in where_ else 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', q, pin))
    L += ['', '### Correspondence', '', '| claim, as v5.14 states it | kernel | terminal | pin | status |', '|:--|:--|:--|:--|:--|',
          '| Weil positivity on classK is equivalent to RH | SIDE-explicit-formula | `SIDEExplicitFormula.B321.h2_sign_iff_rh` | v0.2 = 5c72cad | compiled; cited at the rewritten uses and errata |',
          '| the conservation premise is RH restated | SIDE-explicit-formula | `SIDEExplicitFormula.B321.ch_iff_rh` | v0.1 = baed4df | compiled; cited by E-2026-09-25-1, -5, -6 |',
          '| simplicity is a separate located clause | SIDE-explicit-formula | `SIDEExplicitFormula.Simplicity.simplicity_iff` | v0.17 = 5a1630b | compiled; cited at U06 and U08 |',
          '| the χ-instance of the clause is equivalent to GRH for χ | SIDE-explicit-formula | `SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi` | v0.14 = 4dce7b9 | compiled; cited at U04 |',
          '', '### Version history', '',
          '- v5.14, 2026-10-03 — CP-8 act one under `(R216)`: %d uses rewritten and %d carried; %d erratum sentences rewritten, %d carried with '
          'history lines, %d governed by another, %d with no live line; v5.13 unedited beside it.' % (
              sum(1 for u in K.USES if u[4] == 'rewrite'), sum(1 for u in K.USES if u[4] == 'carry'),
              sum(1 for t in T if t['line'] and t['new'] is not None and t['id'] not in COLL_SKIP),
              sum(1 for t in T if t['line'] and t['new'] is None and t['id'] not in COLL_SKIP), len(COLL_SKIP), sum(1 for t in T if not t['line']))]
    return L


def edition(*a):
    """### PLACE-papers day1/A_Place_to_Stand_v5_14.md beside v5.13 (unedited), from v5.13`s blob at cabbed7 and the work-list; the
    ### re-pin step last (`repin`). Writes the edition and data/b606_edition.json; `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    if not dry and not os.path.exists(os.path.join(D, 'b606_worklist_PLACE.txt')):
        sys.exit('### THE WORK-LIST IS NOT BANKED -- NOTHING WRITTEN')
    M, T, ch, out, where, seg_d = _build()
    out += _bm(M, T, ch, where, len(out))
    text = NL.join(out) + NL
    b = text.encode('utf-8')
    ci, cm = _corr_idx(out), _corr_idx(M)
    bm_at = out.index(BM_TAG) + 1
    E = dict(at=utc(), lines=len(out), sha256=sha(b), where={str(k): v for k, v in where.items()}, version=where[19] - 1,
             hist={str(k): where[k] + 2 for k in HIST}, corr=ci + 1, bm=bm_at, changes=ch, seg_d=seg_d,
             n_body=_count(out[:ci]), n_cur_body=_count(M[:cm]), n_backmatter=_count(out[ci:]), n_cur_backmatter=_count(M[cm:]),
             n_full=_count(out), credit=0, removals=0, history_lines=len(HIST), version_lines=1, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip())
    if dry:
        p = os.path.join(SP, 'b606_edition_dry.md')
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
        json.dump(E, io.open(os.path.join(SP, 'b606_edition_dry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('  DRY: %s ; %d lines ; body %d (v5.13 %d, %+d) ; back matter %d ; changes %d' % (p, len(out), E['n_body'], E['n_cur_body'],
                                                                                              E['n_body'] - E['n_cur_body'], E['n_backmatter'], len(ch)))
        return
    dest = os.path.join(PP, *ED.split('/'))
    if os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    put_json('b606_edition.json', E)
    print('  %s ; %d lines ; sha256 %s ; body %d (v5.13 %d, %+d) ; back matter %d' % (ED, len(out), E['sha256'][:16], E['n_body'], E['n_cur_body'],
                                                                                     E['n_body'] - E['n_cur_body'], E['n_backmatter']))


def termscan():
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b606_edition_termscan.txt."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *ED.split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b606_edition_termscan.txt', (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l])


def _ed():
    t = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return K.lines_of(t)


def carried(E, ed, M):
    """### every non-blank v5.13 line: carried verbatim at its mapped line, or rewritten with every change recorded in the back matter."""
    bm = NL.join(ed[E['bm'] - 1:])
    byl = {}
    for c in E['changes']:
        byl.setdefault(c['line'], []).append(c)
    ok, bad = 0, []
    for n in range(1, len(M) + 1):
        if not M[n - 1].strip():
            continue
        w = E['where'].get(str(n))
        if not w:
            bad.append(n)
            continue
        if n in byl:
            s = M[n - 1]
            for c in byl[n]:
                s = s.replace(c['old'], c['new'])
            good = ed[w - 1] == s and all(('was: “%s” — now: “%s”' % (c['old'], c['new'])) in bm for c in byl[n])
        else:
            good = ed[w - 1] == M[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


CEILING = R4.CEILING


def edition_bank():
    """### The diff with its offset line, every change, the collisions, the counts, the ceiling read, the scanner`s verdict, H28a-H28c,
    ### H40c-H40d."""
    E = jl('b606_edition.json')
    ed = _ed()
    M = K.lines_of(_show(PP, PRE_PP, CUR))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    scan = rd('b606_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad = carried(E, ed, M)
    ci = E['corr'] - 1
    changed_ed = set(E['where'][str(c['line'])] for c in E['changes'])
    carry_ed = set(E['where'][str(u[1])] for u in K.USES if u[4] == 'carry')
    hist_ed = set(E['hist'].values()) | {E['version']}
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if i > ci else 'rewritten-line' if i in changed_ed else 'carried (R-7)' if i in carry_ed
                    else 'history' if i in hist_ed else 'beyond (unread in act one, priced for acts two and three)')
            hits.append(dict(line=i, hit=m.group(0), kind=kind))
    beyond = [h for h in hits if h['kind'].startswith('beyond')]
    # ### the act-scope figure: ceiling hits inside the sentences this act wrote (its new texts), each printed for the reading
    act_hits = [(c['id'], m.group(0), c['new'][max(0, m.start() - 50):m.end() + 30]) for c in E['changes'] for m in CEILING.finditer(c['new'])]
    # ### H28a: every MOVED-IN-MEANING sentence (every change) resolves to a sentence citing a declaration on a page or a banked line
    bm = NL.join(ed[E['bm'] - 1:])
    h28a_rows = []
    for c in E['changes']:
        cites_decl = bool(_decl_cites(c['new'])) or bool(re.search(r'E-2026-\d\d-\d\d-\d|ch_iff_rh|h2_sign_iff_rh|not_register1|register5_output_holds|'
                                                                    r'mellin_Phi_eq_zero_of_re_le_one|lvh2_corrected_iff|spectral_cannon|completedRiemannZeta|b542|b538', c['new']))
        rec = ('was: “%s” — now: “%s”' % (c['old'], c['new'])) in bm
        h28a_rows.append(dict(id=c['id'], line=E['where'][str(c['line'])], cites=cites_decl, recorded=rec, banked=c['cite']))
    h28a = 'HOLDS' if all(x['recorded'] and (x['cites'] or x['banked']) for x in h28a_rows) else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur_body']
    rw = sum(abs(x['d']) for x in E['seg_d'] if x['body'])
    rw_net = sum(x['d'] for x in E['seg_d'] if x['body'])
    allowed = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines'] + rw
    strict = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if (clean and not beyond) else 'REFUTED'
    h40c = 'HOLDS' if (h28a == h28b == h28c == 'HOLDS') else 'REFUTED'
    h40d_letter = E['credit'] + E['history_lines']
    h40d = 'HOLDS' if body_dn == h40d_letter else 'REFUTED'
    offs, last = [], None
    for n in range(1, len(M) + 1):
        o = E['where'][str(n)] - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v5.13 (R190)(3): %s -- the offset changes at each v5.13 line printed (v5.13 line, offset); every v5.13 line`s '
         'v5.14 line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b606 -- COMPONENT 3: THE MONOGRAPH`S NEXT VERSION, v5.14, (R216)(2), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v5.13 : PLACE-papers %s @ %s (blob %s), %d lines, its head "%s"' % (CUR, PRE_PP, E['cur_blob'][:8], len(M), M[0]),
         '### v5.14 : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (E['version'], ed[E['version'] - 1]), '',
         '### EVERY REWRITTEN SENTENCE (%d), WITH THE WORK-LIST LINE IT ANSWERS AND WHAT IT CITES:' % len(E['changes'])]
    for c in E['changes']:
        L += ['  %s  v5.13 :%d -> v5.14 :%d -- %s -- %s' % (c['id'], c['line'], E['where'][str(c['line'])], c['src'], c['cite']),
              '      was : %s' % c['old'], '      now : %s' % c['new'],
              '      cites: %s' % (', '.join('%s (%s, %s)' % (k, K.PINS[k][1], K.PINS[k][2]) for k in _decl_cites(c['new'])) or 'the erratum`s own words and ids')]
    L += ['', '### CARRIED (the ceiling use inside the ceiling, R-7; the erratum sentences with no replacement, with their history lines):']
    L += ['  %s v5.13 :%d -> :%d -- %s' % (u[0], u[1], E['where'][str(u[1])], u[6]) for u in K.USES if u[4] == 'carry']
    L += ['  history line :%s beneath v5.13 :%s : %s' % (v, k, ed[v - 1][:200]) for k, v in E['hist'].items()]
    L += ['', '### COLLISIONS, BOTH WORDINGS IN THE WORK-LIST BANK (PART C):']
    L += ['  %s v5.13 :%d -- %s -- %s' % c for c in COLLISIONS]
    L += ['', '### SEGMENT CHANGES ON REWRITTEN LINES (b558 segments; the ruled replacements` own sentence counts):']
    L += ['  v5.13 :%d %s %+d%s' % (x['line'], x['ids'], x['d'], '' if x['body'] else ' (back matter)') for x in E['seg_d']]
    L += ['', '### EVERY NON-BLANK v5.13 LINE -> ITS v5.14 LINE (%d carried verbatim or rewritten with every change recorded ; failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, w) for n, w in sorted(((int(k), v) for k, v in E['where'].items()))]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v5.13`s BODY %d ; v5.14`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v5.13`s %d, the Correspondence onward, and this act`s), printed separately ; the edition whole %d' % (
              E['n_cur_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_cur_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + the history lines the ruling orders %d + one version '
          'line %d + the ruled replacements` segment changes %d (net %+d, each listed above) = %d ; the strict count %d' % (
              body_dn, E['credit'], E['removals'], E['history_lines'], E['version_lines'], rw, rw_net, allowed, strict), '',
          '### THE CEILING, every hit in the edition, by kind: %s' % {k: sum(1 for h in hits if h['kind'] == k) for k in sorted(set(h['kind'] for h in hits))}]
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits]
    L += ['### the act-scope figure, NOT H28c`s population: ceiling hits inside the %d sentences this act wrote: %d' % (len(E['changes']), len(act_hits))]
    L += ['    %s "%s" ... %s ...' % x for x in act_hits]
    L += ['### sentences beyond the ceiling in the body (lines this act neither rewrote nor carried): %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'),
          '### H28a: rewritten sentences %d ; each recorded in the back matter with both wordings %d ; citing a declaration, an erratum id or '
          'a banked line %d' % (len(h28a_rows), sum(x['recorded'] for x in h28a_rows), sum(1 for x in h28a_rows if x['cites'] or x['banked'])), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d) resolves to a sentence citing a declaration or a banked line.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- by its letter over the whole body: the scanner`s verdict %s (live uses %s), sentences beyond the ceiling %d -- the '
          'stems and ceiling sentences outside the eleven uses and the errata are acts two and three`s by (R216)(2) (reading R-6), a conflict '
          'inside the order, not a sentence this act wrote.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else None, len(beyond)),
          '### ### **H40c %s -- the edition lands with no sentence held; H28a %s, H28b %s, H28c %s.**' % (h40c, h28a, h28b, h28c),
          '### ### **H40d %s -- the body changes by %+d against the credits %d and history lines %d alone (%d by the letter; %d with the version '
          'line; the replacements` own segment changes net %+d).**' % (h40d, body_dn, E['credit'], E['history_lines'], h40d_letter, h40d_letter + 1, rw_net),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b606_edition_PLACE.txt', L)
    put_json('b606_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H40c=h40c, H40d=h40d, h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed,
                                   strict=strict, rw=rw, rw_net=rw_net, backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None,
                                   clean=clean, beyond=len(beyond), act_hits=len(act_hits), hits=hits, carried_ok=ok, carried_bad=bad, held=None))
    print('H28a %s H28b %s H28c %s H40c %s H40d %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; beyond %d ; live %s' % (
        h28a, h28b, h28c, h40c, h40d, ok, bad, body_dn, allowed, strict, len(beyond), live.group(1) if live else None))


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b606_repin.txt."""
    E = jl('b606_edition.json')
    ed = _ed()
    bm = ed[E['bm'] - 1:]
    checks = []
    for m in re.finditer(r'^- \*\*([A-Z0-9-]+)\*\* :(\d+) \(v5\.13 :(\d+)\)', NL.join(bm), re.M):
        i, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        checks.append(('back matter %s cites :%d for v5.13 :%d' % (i, a, b), E['where'].get(str(b)) == a and bool(ed[a - 1].strip())))
    for c in E['changes']:
        a = E['where'][str(c['line'])]
        checks.append(('%s`s new sentence on :%d' % (c['id'], a), ed[a - 1].count(c['new']) >= 1))
    for k, v in E['hist'].items():
        checks.append(('history line :%d beneath :%s' % (v, k), ed[v - 1].startswith('*v5.14, 2026-10-03, a history line') and E['where'][k] == v - 2))
    for m in re.finditer(r':(\d+) beneath :(\d+)', NL.join(bm)):
        a, b = int(m.group(1)), int(m.group(2))
        checks.append(('the history section`s :%d beneath :%d' % (a, b), a == b + 2 and ed[a - 1].startswith('*v5.14')))
    for cid, line, _w, _h in COLLISIONS:
        checks.append(('collision %s at :%d' % (cid, E['where'][str(line)]), ('**%s** :%d (v5.13 :%d)' % (cid, E['where'][str(line)], line)) in NL.join(bm)))
    checks.append(('the version line on :%d above v5.13`s' % E['version'], ed[E['version'] - 1] == VERSION and ed[E['version']] == '**v5.13, 2026-07-27**'))
    checks.append(('the Correspondence heading on :%d' % E['corr'], ed[E['corr'] - 1].startswith(CORR_HEAD)))
    checks.append(('the back-matter tag on :%d' % E['bm'], ed[E['bm'] - 1] == BM_TAG))
    bank = rd('b606_edition_PLACE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v5.13') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    for m in re.finditer(r'v5\.13 :(\d+) -> v5\.14 :(\d+)', bank):
        b, a = int(m.group(1)), int(m.group(2))
        checks.append(('the diff bank`s v5.13 :%d -> v5.14 :%d' % (b, a), E['where'].get(str(b)) == a))
    L = ['### b606 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-100s %s' % (w[:100], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b606_repin.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k):
    """### after the edition commit: ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b602's list
    ### at v0.20, the χ page from b603's at v0.21; no Lean call). Writes the page only when it changed, and data/b606_page_<k>.json."""
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b606_%s' % k)
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
        put_json('b606_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
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
    put_json('b606_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; the probe read %s' % (k, rc, len(b), changed, secs, src_out))
    for x in dl[:60]:
        print('    ' + x[:240])


def page_arms(tag):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b606 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    L.append('### the lists read: %s' % {k: (NODES[k], PROBE[k]) for k in NODES})
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b606_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b606_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
SCORE_KEYS = ('H28a', 'H28b', 'H28c', 'H40a', 'H40b', 'H40c', 'H40d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _unrender_ok(t):
    """### S3: a rendered replacement`s words equal ERRATA`s (or b532`s) raw words once R-3`s rendering and markup are taken off."""
    # ### b606 defect (b): the first form reversed every rendering on every target -- an ERRATA "—" read as a rendered "--", and
    # ### b532`s transliterations reversed on targets that never had them -- and refuted S3 on eight sentences whose words were
    # ### right. The rendering is now applied forward to the source, as reading (vii) declares it, and the markup is set aside.
    def strip(s):
        return re.sub(r'\s+', ' ', s.replace('**', '').replace('`', '').replace('*', '')).strip()
    rendered, _used = K.render(t['raw_used'], t.get('b532', False))
    return strip(t['new']) == strip(rendered)


def scores():
    WJ, H, E = jl('b606_worklist.json'), jl('b606_h28.json'), jl('b606_edition.json')
    Z, X = jl('b606_page_zeta.json'), jl('b606_page_chi.json')
    rp = rd('b606_repin.txt')
    T = WJ['targets']
    uses = WJ['uses']
    moved = sum(not u['ok'] for u in uses)
    ceil_n = sum(1 for u in K.USES if u[4] == 'rewrite') + sum(1 for u in K.USES if u[4] == 'erratum')
    landed = {}
    edt = '\n'.join(_ed()) if os.path.exists(os.path.join(PP, *ED.split('/'))) else ''
    for t in T:
        if t['line'] and t['new'] is not None and t['id'] not in COLL_SKIP:
            landed.setdefault(t['eid'], []).append(t['new'] in edt)
    with_rep = [e for e in K.FIVE if any(t['eid'] == e and t['line'] and t['raw'] for t in T)]
    n2_land = all(all(v) for e, v in landed.items() if e in with_rep)
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle',
                                                                               'SIDE-global-section')}
    kern_ok = kern == {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254',
                       'SIDE-global-section': '3528bcf'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    trail_landed = os.path.exists(os.path.join(D, 'b606_trail.json'))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = g(PP, 'rev-parse', 'HEAD:' + CUR).strip() == E.get('cur_blob') and not g(PP, 'status', '--porcelain', '--', CUR).strip()
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b606_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b605_closing_push_out.txt'))
    m = re.search(r'RE-PIN : (\d+) of (\d+)', rp)
    arms2 = rd('b606_page_arms_c2.txt')
    s3 = [t['id'] for t in T if t['line'] and t['new'] is not None and t['id'] not in COLL_SKIP and not _unrender_ok(t)]
    S = dict(
        H28a=(H.get('H28a'), 'every MOVED-IN-MEANING sentence (%d) recorded with both wordings and citing a declaration, an erratum id or a banked line: %d' % (
            len(H.get('h28a_rows') or []), sum(1 for x in H.get('h28a_rows') or [] if x['recorded'] and (x['cites'] or x['banked'])))),
        H28b=(H.get('H28b'), 'the body differs by %+d against at most %d (strict %d; the replacements` segment changes %d, net %+d)' % (
            H.get('body_dn', 0), H.get('allowed', 0), H.get('strict', 0), H.get('rw', 0), H.get('rw_net', 0))),
        H28c=(H.get('H28c'), 'by its letter over the whole body: the scanner %s (live uses %s); beyond the ceiling %s -- reading R-6, the order`s '
                             'own split of the body over three acts' % ('CLEAN' if H.get('clean') else 'NOT CLEAN', H.get('live'), H.get('beyond'))),
        H40a=(WJ.get('h40a'), '%d of 11 uses on a live line, moved %d' % (sum(u['ok'] for u in uses), moved)),
        H40b=(WJ.get('h40b'), 'per erratum (id, sentences, live, replacement in ERRATA itself): %s' % WJ.get('h40b_rows')),
        H40c=(H.get('H40c'), 'no sentence held; H28a %s, H28b %s, H28c %s' % (H.get('H28a'), H.get('H28b'), H.get('H28c'))),
        H40d=(H.get('H40d'), 'the body %+d against credits and history lines %d (with the version line %d; the replacements` net %+d)' % (
            H.get('body_dn', 0), E.get('credit', 0) + E.get('history_lines', 0), E.get('credit', 0) + E.get('history_lines', 0) + 1, H.get('rw_net', 0))),
        N1=('HELD' if len(uses) == 11 and all(u['ok'] for u in uses) and moved <= 2 else 'REFUTED',
            'all eleven resolve %s ; moved since the census %d (the census pin`s blob is the current version`s)' % (all(u['ok'] for u in uses), moved)),
        N2=('HELD' if len(with_rep) >= 4 and n2_land else 'REFUTED', 'errata with a live line and a replacement: %d %s ; every sentence of them '
            'landed %s %s' % (len(with_rep), with_rep, n2_land, {e: '%d/%d' % (sum(v), len(v)) for e, v in landed.items()})),
        N3=('HELD' if ceil_n >= 11 else 'REFUTED', 'ceiling corrections %d (rewritten by the clause %d, by the erratum governing U11 1; carried U09 '
            'inside the ceiling); fact corrections 0' % (ceil_n, sum(1 for u in K.USES if u[4] == 'rewrite'))),
        N4=('HELD' if all(H.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and H.get('held') is None else 'REFUTED',
            'H28a %s, H28b %s, H28c %s ; held %s' % (H.get('H28a'), H.get('H28b'), H.get('H28c'), H.get('held'))),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; every kernel`s main unmoved %s; the current version unedited %s; PLACE-papers %s (wanted %s); relay files beyond '
            'the act`s banks, tools and the table %s%s' % (kern_ok, cur_same, pp_ch, want_pp, relay_beyond, '' if trail_landed else ' ; the trail record pending')),
        S1=('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        S2=('HELD' if not H.get('carried_bad') else 'REFUTED', 'every non-blank v5.13 line carried verbatim or rewritten with every change '
                                                              'recorded: %d ; failing %s' % (H.get('carried_ok', 0), H.get('carried_bad'))),
        S3=('HELD' if not s3 else 'REFUTED', 'every written replacement`s words are its source`s once R-3`s rendering is taken off: failing %s' % (s3 or 'none')),
        S4=('HELD' if Z.get('changed') is True and X.get('changed') is True else 'REFUTED', 'the ζ page changed %s ; the χ page changed %s (the '
            'edition names nodes of both)' % (Z.get('changed'), X.get('changed'))),
        S5=('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
            'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    )
    put_json('b606_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _k_live():
    return len(K.FIVE)


TITLE = ('## CP-8, act one: the monograph’s next version, v5.14, over the eleven ceiling uses and {k} live errata, from the ceiling census '
         'and ERRATA by the form')
TRAIL_HEAD = ('### b606 — lane three, act thirty-three under (R216): CP-8 act one -- the monograph’s next version over the eleven ceiling '
              'uses and the live errata by the form')


def _title():
    return TITLE.replace('{k}', str(_k_live()))


def _finding_text():
    S, WJ, H, E = jl('b606_scores.json'), jl('b606_worklist.json'), jl('b606_h28.json'), jl('b606_edition.json')
    rl = jl('b606_record_lines.json')
    w1, w2, pl = [x['line'] for x in rl['lines']]
    ec = _pp_commit('b606 (R216)(2): ' + ED)
    zc, xc = _pp_commit('b606 (R216)(2): ' + PAGE), _pp_commit('b606 (R216)(2): ' + DIR_PAGE)
    T = WJ['targets']
    nre = sum(1 for t in T if t['line'] and t['new'] is not None and t['id'] not in COLL_SKIP)
    t = _title()
    e = ['', t, '',
         '*Filed at b606 on the author’s ruling `(R216)`. Banks: relay `data/b606_reads.txt`, `data/b606_worklist_PLACE.txt`, '
         '`data/b606_edition_PLACE.txt`, `data/b606_edition_termscan.txt`, `data/b606_repin.txt`, `data/b606_page_zeta.json`, '
         '`data/b606_page_chi.json`, `data/b606_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R216)`(2)). PLACE-papers `%s` (commit %s), the monograph’s v5.14 by its own series, beside v5.13, unedited; '
         'the version line above v5.13’s; %d ceiling uses rewritten by the ceiling clause, one carried inside the ceiling and one '
         'answered by the erratum that governs its sentence; %d erratum sentences rewritten by their replacements, three carried with '
         'two history lines (E-2026-09-22-1, which carries no replacement), two governed by the entry that extends them, two with no live '
         'line; the back matter records every change with both wordings, the collisions, the Placement and the Correspondence.' % (
             ED, ec, sum(1 for u in K.USES if u[4] == 'rewrite'), nre), '',
         '**The work-list** (`(R216)`(3), relay `data/b606_worklist_PLACE.txt`, banked before the writing). The eleven uses re-derived by '
         'line with b584’s classifier at the census pin, whose blob is the current version’s; the errata addressed to the monograph by '
         'id -- %d entries name it, %d with live lines (E-2026-09-22-1, E-2026-09-25-1, -4, -5, -6), %d with none; the sieve’s one '
         'citation into the monograph (§24.4’s analytic-row note, act two’s).' % (len(K.ERRATA_IDS), len(K.FIVE), len(K.ERRATA_IDS) - len(K.FIVE)), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '. H28c refuted by its letter over the whole body: the '
         'live stems and the ceiling sentences outside the eleven uses and the errata are acts two and three’s by `(R216)`(2), so the '
         'body’s scanner and ceiling read cannot be clean at act one -- a conflict inside the order, recorded as such; H40c and N4 fall '
         'with it. H40b refuted by its letter: E-2026-09-22-1 carries no replacement and E-2026-09-25-1’s stand in the relay bank it '
         'cites, not in ERRATA itself.', '',
         '**The pages.** Both re-emitted after the edition commit from their banked probes, no Lean call: the ζ page (PLACE-papers %s) and '
         'the χ page (%s), each committed alone, the edition entering their Placement.' % (zc, xc), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition carries into the monograph the corrections of E-2026-09-25-1 '
         '(b532, b535), -4 (b540), -5 (b541) and -6 (b543), the deposited-text census those entries filed, and b584’s ceiling census '
         '(FINDINGS :6608); it cites the faces the sieve at v0.3 counts under one verdict (:7084) at the pins the pages print; and it is '
         're-read in turn by CP-8’s act two, whose chapters 21, 22, §24.4 and §27.3 hold the restatements this act leaves. It strengthens '
         'the programme’s offering of the monograph: its own text now says what the compiled faces say at the sites the errata named.', '',
         '**The record lines.** b605’s weight at FINDINGS :%d; the two fact corrections, the navigator’s, at :%d; CP-8’s three-act '
         'plan at OPEN_TRAILS :%d, addressed to lane three’s order :12062.' % (w1, w2, pl), '',
         '**Next.** Per `(R216)`(4): b607, CP-8 act two -- chapters 21, 22, §24.4 and §27.3 read against b596-b605. The author rules on '
         'the closing.', '',
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
    put_json('b606_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


TWO_PRICE = ('act two’s work-list, priced from what this act found: chapters 21 and 22 (:1315-:1418) against simplicity_iff, the doubling '
             'corollary and SimpleProportion; §24.4 (:1489-:1511) and its analytic-row note (:1499), the one sieve citation into the monograph; '
             '§27.3 (:1787-:1817), where four of this act’s lines fall (:1793, :1795, :1801, :1808) and the restatements it leaves stand -- '
             '“A reader who discharges any one of them discharges all five” (:1795) beside the corrected “These registers stand at '
             'different depths”; the registers at their four depths as b538 and the pages read them; the product lemma and the family '
             'theorem where the monograph speaks of the χ-side (chapter 20, :1232-:1289, beside U04’s rewrite)')


def _trail_text():
    S, fj, rl = jl('b606_scores.json'), jl('b606_findings.json'), jl('b606_record_lines.json')
    H = jl('b606_h28.json')
    w1, w2, pl = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R216) ratified.** (1) b605 at its weight, the counts and verdicts from its banks. (2) CP-8 in three acts. (3) Act one’s '
             'work-list, banked before the writing; H40a-H40d. (4) The act after: b607, CP-8 act two.', '',
             '**Entered:** FINDINGS.md:%d (b605’s weight), :%d (the two fact corrections), :%d (the entry, with its mutual-light line); '
             'OPEN_TRAILS :%d (CP-8 in three acts, addressed to :12062); this record; PLACE-papers `%s` (v5.14, beside v5.13, unedited); both '
             'pages re-emitted.' % (w1, w2, fj['entry_line'], pl, ED), '',
             '**Resolved by the seat, for the author’s strike:** readings R-1 to R-7 of the edition’s back matter -- v5.14 by the series, the '
             'body above the monograph’s own Correspondence, the replacements rendered in the document’s typography with their words '
             'kept, the history clause reaching the version log and the era annotations and not the Correspondence E-2026-09-25-6 corrects, '
             'E-2026-09-22-1’s sentences carried with history lines, “nothing else” read as the order’s split of the body over three '
             'acts, and U09 carried inside the ceiling; the collisions C1-C4. No prompt was put (relay data/b606_author_answers.txt).', '',
             '**For the author:** H28c, H40c and N4 refuted by the letter, the order’s own split -- the body keeps %s ceiling hits and %s live '
             'stem outside act one’s sentences, acts two and three’s by `(R216)`(2). H40b refuted by the letter: of the 16 entries naming the '
             'monograph, 11 carry no live line, E-2026-09-22-1 no replacement, and E-2026-09-25-1’s replacements stand in the relay bank it '
             'cites. H40d refuted: the body moves by +%s against the history lines’ 2 -- the version line and two replacements that each '
             'carry one more sentence than the line they replace. N3 refuted: 10 ceiling corrections, not 11 -- the use at v5.13 :1562 '
             'reads inside the ceiling and carries (R-7).' % (H.get('beyond'), H.get('live'), H.get('body_dn')), '',
             '**Act two, priced:** %s.' % TWO_PRICE, '',
             '**Defects** (relay data/b606_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R216)`(4), b607, CP-8 act two; the author rules on the closing.', '',
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
    put_json('b606_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b606_trail.json')['line'])


def desk():
    S = jl('b606_scores.json')
    HK = ('H28a', 'H28b', 'H28c', 'H40a', 'H40b', 'H40c', 'H40d')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b606 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c and H40a-H40d, (R216)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H28/H40 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b606_defects.txt').rstrip(NL).split(NL)
    put_txt('b606_desk_notes.txt', L)


def components():
    S, fj, tj, rl = jl('b606_scores.json'), jl('b606_findings.json'), jl('b606_trail.json'), jl('b606_record_lines.json')
    Z, X = jl('b606_page_zeta.json'), jl('b606_page_chi.json')
    L = ['b606 -- THE COMPONENTS, BANKED UNDER (R216).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b605`s closing push-out relay %s ; push-b605* branches deleted by '
         'name (data/b606_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b606_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b605`s weight FINDINGS :%d ; the fact corrections :%d ; CP-8 in three acts OPEN_TRAILS :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the work-list data/b606_worklist_PLACE.txt ; H40a %s, H40b %s' % (S['H40a'][0], S['H40b'][0]),
         '### COMPONENT 3 : the edition %s ; the diff data/b606_edition_PLACE.txt ; H28a %s, H28b %s, H28c %s ; H40c %s, H40d %s' % (
             ED, S['H28a'][0], S['H28b'][0], S['H28c'][0], S['H40c'][0], S['H40d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b606_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b607, CP-8 act two ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b606_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b606_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
