# -*- coding: utf-8 -*-
"""b611_record.py -- THE ACT'S RECORD TOOL, UNDER (R221). ### ONE SUBCOMMAND PER BANK.

### ### b611: LANE THREE, ACT THIRTY-EIGHT -- THE SYNTHESIS FOR PHASE 1.2: ONE DOCUMENT FROM THE CLUSTER'S FOUR PAPERS READ AT ADDRESS,
### EVERY CLAIM GRADED BY ITS PAPER'S OWN TEXT; THE ANNEX ACT STRUCK; THE UNPUSHED TAGS ENTERED AS A WORK-ORDER.
### Subcommands write only `data/b611_*` unless the docstring names another file; `dry` on the command line routes every b611 bank and the
### document to the seat's scratchpad (for `findings` and `trail`, `dry` prints and appends nothing). Banks are written by encode, temp
### file, `os.replace`; ledger appends through b566's guarded `append_to`. The act's data and resolvers are tools/b611_claims.py's. No
### platform call. No Lean call. The template is tools/b610_record.py.
"""
import difflib
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
import b611_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = 'fdca0101'
STEPZERO = '49386de5'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/8f2ff82c-2889-4443-a8e7-85de4d1b215f/scratchpad'
SESSION_ID = '8f2ff82c-2889-4443-a8e7-85de4d1b215f'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')   # ### for these two, `dry` prints and appends nothing
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b611_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b611_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _segs(l):
    return R4._segs(l)


def _cell(s):
    return s.replace('|', '¦')


DEFECTS = [
    '(a) THE SEAT`S, IN THE SUITE, FOUND AT THE PRE-PUSH RUN: G-CLAIMS-BANKED compared the claim bank`s stamp with the document`s by a '
    'strict less-than, where both stamps are whole seconds and the two banks were written in one second (2026-10-04T03:04:06Z; by the '
    'files` own mtimes the claim bank`s json 0.3 s before the document`s), so the arm failed LIVE on a true order. The predicate '
    'corrected through the Edit tool: the stamps compared by less-or-equal and the order read from the two files` mtimes; its positive '
    'control unchanged. The entry and the trail record, appended but not yet committed with the line none recorded, were cut back to '
    'their banked byte lengths before the append and re-appended; the suite re-run whole.',
]
DEFECT_SHORT = ['(a) the seat’s: G-CLAIMS-BANKED compared two whole-second stamps by a strict less-than, and the claim bank and the '
                'document were written in one second, so it failed on a true order -- the order now also read from the files’ mtimes; '
                'the uncommitted entry and trail record cut back and re-appended; the suite re-run whole']


def defects(*a):
    L = ['b611 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b611_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the Phase 1.2 row and the no-keystone section', PP, PRE_PP, CEN3, ('GREP', r'^\| R02 \||^## §2|^- \*\*R\d\d '), 900),
    ('REGISTRY.md: rows 1.5a-1 to 1.5a-4, the phase attribute`s 1.2 row, the deposit record lines and :333, :628, :731, :787', PP, PRE_PP, 'REGISTRY.md',
     [142, 143, 144, 145, 333, 628, 731, 780, 787], 900),
    ('THE_EXCLUSION_ARCHITECTURE.md whole (1.5a-1)', PP, PRE_PP, K.PAPERS['EA'][0], 'ALL', 300),
    ('MECHANISM_EXCLUSION.md whole (1.5a-2)', PP, PRE_PP, K.PAPERS['ME'][0], 'ALL', 300),
    ('IDS_TO_RH.md whole (1.5a-3)', PP, PRE_PP, K.PAPERS['IR'][0], 'ALL', 300),
    ('INTEGRATED_PROOF.md whole (1.5a-4)', PP, PRE_PP, K.PAPERS['IP'][0], 'ALL', 300),
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the rows the cluster`s routes meet (RH-02, RH-58, RH-59, RH-60) and the five tests', PP, PRE_PP,
     'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md', [27, 28, 29, 30, 31, 59, 120, 121, 122], 700),
    ('OPEN_TRAILS: the form, the precedence order, b610`s lines and record', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12228, 12564, 12566, 12568], 1500),
    ('the cluster`s folder: the paths spine (a 1.5A synthesis, not a registry row)', PP, PRE_PP, 'phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md',
     [1, 3, 15, 17], 300),
    ('SIDE-kernel v1.2: ConservationBridge`s premise, conditional and second structural_exhaustiveness_proved', 'D:/SIDE-kernel', 'v1.2',
     'Bridge/ConservationBridge.lean', [7, 13, 14, 15, 16, 29, 30, 36, 37, 38], 220),
    ('SIDE-kernel v1.2: Integration`s StructuralExhaustiveness and its conditional', 'D:/SIDE-kernel', 'v1.2', 'Kernel/Integration.lean',
     [201, 202, 210, 211, 212], 220),
    ('SIDE-kernel v1.2: the spectral cannon', 'D:/SIDE-kernel', 'v1.2', 'Kernel/SpectralCannonFull.lean', [11, 58, 59], 220),
    ('SIDE-kernel v1.2: the formation terminals', 'D:/SIDE-kernel', 'v1.2', 'Kernel/Core.lean', [16, 50, 53], 220),
    ('SIDE-kernel v1.2: the balance theorem', 'D:/SIDE-kernel', 'v1.2', 'Kernel/Voice1.lean', [22, 23, 24], 220),
    ('SIDE-kernel v1.2: the root structural_exhaustiveness_proved', 'D:/SIDE-kernel', 'v1.2', 'Bridge/TheBridgeComplete.lean', [180, 181, 182, 188, 189, 190], 220),
    ('SIDE-kernel v1.2: all_zeros_simple`s one mention outside a root file (a comment)', 'D:/SIDE-kernel', 'v1.2', 'Kernel/PerpendicularCrossing.lean', [173], 220),
    ('relay data/b610_census.txt: the kernels` table (Part C)', RELAY, STEPZERO, 'data/b610_census.txt', ('GREP', r'^### PART C|^  SIDE-'), 400),
    ('relay data/b610_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b610_closing_push_out.txt', 'ALL', 260),
    ('relay data/b610_scores.json (whole)', RELAY, STEPZERO, 'data/b610_scores.json', 'ALL', 300),
]


def reads(*a):
    L = ['b611 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = R4._show(repo, rev, path)
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
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### SIDE-kernel v1.2 = %s ; declarations beginning `axiom` at v1.2: %d (git grep "^axiom ")' % (
        g('D:/SIDE-kernel', 'rev-parse', '--short=8', 'v1.2^{}').strip(),
        len([x for x in g('D:/SIDE-kernel', 'grep', '-n', '^axiom ', 'v1.2', '--', '*.lean').split(NL) if x.strip()])),
          '### TECHNE mentions in the four papers: %s' % {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()},
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b611_reads.txt', L)


def answers(*a):
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and i > ANSWERS_FROM_LINE:
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b611 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for q in inp.get('questions', []):
            L.append('### PROMPT (%s): %s' % (q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d: %s :: %s' % (j, op.get('label'), op.get('description')))
        L += ['RESULT: %s' % (results.get(cid, (None, '### NO RESULT'))[1]), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act; the precedence order and the ruling`s letter reached every '
                 'reading, each declared on the face and strikeable.')
    put_txt('b611_author_answers.txt', L)


ANSWERS_FROM_LINE = 0   # ### the session carries b610 too; b610 put no prompt, so every call found is b611's


# ================================================================================ COMPONENT 1: THE RECORD LINES
B610_ENTRY = '## The phase-state reading: THE_KEYSTONE_CENSUS at v0.3 as one row per phase and cluster'
B610_TRAIL = '### b610 — lane three, act thirty-seven under (R220): the phase-state reading'
B610_SEQ = '*Appended 2026-10-03 by b610, under `(R220)`(5), the author’s explicit ask -- THE SYNTHESIS SEQUENCE, ENTERED WITH ITS FORM:*'
W_HEAD = '*Appended 2026-10-03 by b611 to b610’s entry (:%d), under `(R221)`(1) -- b610 AT ITS WEIGHT:*'
A_HEAD = '*Appended 2026-10-03 by b611 to b610’s record (:%d), under `(R221)`(2)(i) -- THE ANNEX ACT STRUCK; THE SEQUENCE RUNS b611-b616:*'
T_HEAD = '*Appended 2026-10-03 by b611, under `(R221)`(2)(ii) -- W-ORD-TAG-REMOTES, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD:*'
F_HEAD = '*Appended 2026-10-03 by b611, under `(R221)`(2)(iii) -- TWO FACT ITEMS, ENTERED FOR THE DOCUMENTS THEY SIT IN:*'
S_HEAD = '*Appended 2026-10-03 by b611 to the synthesis sequence’s form (:%d), under `(R221)`(3) -- THREE CLAUSES OF THE SYNTHESIS FORM:*'


def _b610():
    S = json.loads(R4._show(RELAY, STEPZERO, 'data/b610_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, trail, seq):
    s = _b610()
    tags = K.unpushed_tags()
    kernels = sorted(set(t['repo'] for t in tags))
    t1 = ('\n%s THE_KEYSTONE_CENSUS_v0_3.md (PLACE-papers c83c72b) beside the current version, unedited: 23 rows, all 135 registry rows placed '
          'each by one stated rule; §0 ruling the test to the taxonomy, the old test beneath under the history clause, the old body moved whole '
          'to back matter; seven clusters with documents and no keystone -- Phase 1.2 (1.5a-1 to 1.5a-4), 1.5E, 2B, 2D, 2F, 2G, the ANNEX. '
          'SPIRAL_MAP_v0_7.md (3433158): one pointer line per cluster beneath §4A’s table, the table unedited; one stem (v0.6 :98) and three '
          'ceiling sentences (:62, :102, :104) corrected to their objects. The verdicts, as relay data/b610_scores.json prints them: H28a-H28c '
          '%s, %s, %s for the census (H28a vacuous, no work-list) and %s, %s, %s for the map; H44a-H44d %s, %s, %s, %s; N1-N5 %s; S1-S5 %s; '
          're-pins 26 of 26 and 22 of 22. The second reader’s addendum at relay data/b610_residue_addendum.txt (55 lines, 38 kin), beside the '
          'seed and not in it, accepted. FINDINGS :7208, :7210, :7212; OPEN_TRAILS :12564, :12566, :12568. The pages unchanged. The suite 93 of 93 '
          'before and after the push. Defects (a)-(c) the seat’s, (b)-(c) corrected and the trail record cut back and re-appended by the '
          'recorded length. “Tier E errata-class” the navigator’s wording; the taxonomy’s :20 (filing-facing) governs. Nothing deposited; no '
          'kernel touched.\n' % (W_HEAD % entry, s['H28a-CENSUS'], s['H28b-CENSUS'], s['H28c-CENSUS'], s['H28a-SPIRAL'], s['H28b-SPIRAL'],
                                 s['H28c-SPIRAL'], s['H44a'], s['H44b'], s['H44c'], s['H44d'],
                                 'HELD' if all(s['N%d' % i] == 'HELD' for i in range(1, 6)) else [s['N%d' % i] for i in range(1, 6)],
                                 'HELD' if all(s['S%d' % i] == 'HELD' for i in range(1, 6)) else [s['S%d' % i] for i in range(1, 6)]))
    t2 = ('\n%s REGISTRY calls the download layer non-keystone and outside the repository tree, and no keystone is written from a file the '
          'tree does not hold: the act b617 named at :%d is struck, the census row R22 stands as the ANNEX’s record, and the synthesis '
          'sequence runs b611 (Phase 1.2), b612 (1.5E), b613 (2B), b614 (2D), b615 (2F), b616 (2G).\n' % (A_HEAD % trail, trail))
    items = '; '.join('%s %s = %s (%s)' % (t['repo'], t['tag'], t['sha'], ('cited at ' + ', '.join(c for c in t['cited'] if not c.startswith('OPEN_TRAILS')))
                                          if [c for c in t['cited'] if not c.startswith('OPEN_TRAILS')] else 'cited by no ledger')
                      for t in tags)
    t3 = ('\n%s %d tags in %d kernels are carried by their clones and absent at their remotes (relay data/b610_census.txt, Part C, read by '
          'ls-remote): %s. The work: each tag read back in its clone; a tag a ledger cites pushed by tools/push_gated.sh after the read-back; an '
          'uncited tag recorded as local in the kernel’s housekeeping list; REGISTRY’s row notes corrected to the state found by a dated row '
          'update in REGISTRY’s own form. Price: one act, no Lean call, one push per cited tag. Trigger: the author’s word. Not started.\n' % (
              T_HEAD, len(tags), len(kernels), items))
    t4 = ('\n%s (a) REGISTRY :787 says `internal/` and `meta/` have no REGISTRY section of any kind, while REGISTRY :333 heads a table listing '
          'six `internal/` files: for REGISTRY’s next correction, which REGISTRY as the source of truth takes as a dated row update in its own '
          'form, not by the edition form. (b) SPIRAL_MAP :104 (v0.7 :106) says each Phase 1.2 checkpoint kernel forces σ = 1/2, while REGISTRY '
          ':731 records that SIDESpinor.spinor_forces_half does not conclude σ = 1/2: for SPIRAL_MAP’s next edition, the kernels’ statements read '
          'at their pins before the correction is written.\n' % F_HEAD)
    t5 = ('\n%s (i) the Correspondence table sits in the back matter for a Tier C document and after the front matter, where `(R19)` puts it, '
          'when the document’s tier line reads KC -- the placement follows the tier the rows earn, decided after the rows are graded; (ii) the '
          'title names the cluster’s objects and no property; (iii) the document’s head carries one line saying it synthesises the papers it '
          'names and certifies nothing they do not.\n' % (S_HEAD % seq))
    return [(W_HEAD % entry, t1), (A_HEAD % trail, t2), (T_HEAD, t3), (F_HEAD, t4), (S_HEAD % seq, t5)]


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _addr():
    Q = R2._Q()
    return Q, Q.line_of(Q.FIND, B610_ENTRY), Q.line_of(Q.OT, B610_TRAIL), Q.line_of(Q.OT, B610_SEQ)


def record_lines(*a):
    """### FINDINGS: b610's weight, addressed to b610's entry; OPEN_TRAILS: the ANNEX act struck (addressed to b610's record),
    ### W-ORD-TAG-REMOTES, the two fact items, the synthesis form's three clauses (addressed to :12566) -- each appended at the end."""
    Q, entry, trail, seq = _addr()
    if (entry, trail, seq) != (7212, 12568, 12566):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, trail, seq))
    parts = _texts(entry, trail, seq)
    bad = ledger_check(*[t for _h, t in parts])
    print('  grade-word lines naming a backticked name: %s' % (bad or 'NONE'))
    if 'dry' in a:
        for _h, t in parts:
            print(t)
        return
    if bad:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME -- NOTHING WRITTEN')
    plan = [(Q.FIND, parts[0])] + [(Q.OT, p) for p in parts[1:]]
    for p, (h, _t) in plan:
        Q.guard_absent(p, h)
    out = []
    for p, (h, t) in plan:
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b611_record_lines.json', dict(entry=entry, trail=trail, seq=seq, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE CLAIM BANK
def _route_rows():
    rs = {}
    for c in K.C:
        if c[8]:
            rs.setdefault(c[8][0], []).append(c)
    return rs


def h45d_score(sieve):
    rs = _route_rows()
    reached = [r for r, cs in rs.items() if cs[0][8][1] in ('DARK', 'BRIGHT', 'NOT A ROUTE')]
    matched = []
    for r, cs in rs.items():
        row = cs[0][8][5]
        if row and row in sieve:
            v, t = sieve[row]
            mine = cs[0][8][1] + ('' if cs[0][8][2] is None else ', test %d' % cs[0][8][2])
            theirs = v + ('' if t.strip() == '—' else ', test %s' % t.split()[0])
            matched.append((r, row, mine, theirs, mine == theirs))
    return ('HOLDS' if reached and matched and all(x[4] for x in matched) else 'REFUTED'), reached, matched


def claims(*a):
    """### data/b611_claims_1_2.txt and .json: each paper's path, version and head; every claim with its line, grade and reason; the routes
    ### through the five tests; the terminals at the pin; H45a's trace table and H45d -- banked before any writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    rk = K.resolve_kernel()
    sieve = K.sieve_rows()
    if not all(ok for ok, _l in rc.values()) or not all(ok for _k, ok, _l in rk):
        sys.exit('### A NEEDLE OR A KERNEL READ FAILS -- NOTHING WRITTEN')
    L = ['b611 -- COMPONENT 2: THE CLAIM BANK OF PHASE 1.2, (R221)(4), banked %s before any writing' % utc(),
         '### the papers at PLACE-papers %s; the kernel at SIDE-kernel %s = %s; the sieve v0.4 at %s' % (PRE_PP, K.KPIN, K.KSHA, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'A ROUTE is' in x] + ['']
    L += ['### PART A -- THE PAPERS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        ver = next((l for l in ls[:20] if re.search(r'Version|v\d|Summary|February|March|January', l)), '')
        L.append('  %s = `%s` -- REGISTRY %s (:%d) -- %d lines -- head :1 “%s” -- version/date line “%s”' % (k, path, rid, rline, len(ls), ls[0][:120], ver.strip()[:140]))
    L += ['', '### PART B -- THE CLAIMS, EACH WITH ITS LINE, NEEDLE, GRADE AND REASON (%d):' % len(K.C)]
    for c in K.C:
        cid, pk, n, needle, text, grade, support, reason, route, kr = c
        L.append('  %-6s %s :%-4d %-25s support %-11s -- %s' % (cid, pk, n, grade, support, text))
        L.append('         needle “%s” on the line: %s ; reason: %s%s' % (needle[:80], rc[cid][0], reason,
                                                                     (' ; route %s %s%s' % (route[0], route[1], '' if route[2] is None else ' test %d' % route[2])) if route else ''))
    L += ['', '### PART C -- THE ROUTES, EACH THROUGH THE FIVE TESTS IN ORDER, WITH ITS VERDICT AND INSTRUMENT:']
    for r, cs in sorted(_route_rows().items()):
        c = cs[0]
        _rid, v, t, inst, why, row = c[8]
        passed = ('tests 1-%d passed; ' % (t - 1)) if t and t > 1 else ''
        L.append('  %s -- claims %s -- %s%s -- %s, %s -- %s -- the sieve`s row %s' % (
            r, ', '.join(x[0] for x in cs), passed, 'fails test %d' % t if t else 'not asked (not a route)', v, inst, why,
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', '')))) if row else 'none')))
    L += ['', '### PART D -- THE TERMINALS AT THE PIN (SIDE-kernel %s = %s), EACH READ ON ITS LINE, AND THE TABLE`S GRADE:' % (K.KPIN, K.KSHA)]
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '{}')
    tt = dict((r['name'], r) for r in T.get('rows') or [] if r.get('repo') == 'SIDE-kernel')
    TT_NAME = {'conservation_rh': 'ConservationBridge.riemann_hypothesis', 'integration_rh': 'techne_kernel_integration.rh_from_structural_exhaustiveness',
               'spectral_cannon': 'SpectralCannonFull.spectral_cannon', 'formation': 'SIDEKernel.formation', 'formation_count': 'SIDEKernel.formation_count',
               'balance': 'balance_theorem', 'sep_root': 'structural_exhaustiveness_proved', 'sep_cons': 'ConservationBridge.structural_exhaustiveness_proved'}
    for k, ok, l in rk:
        f, n, _needle, what = K.KREADS[k]
        r = tt.get(TT_NAME.get(k, ''), {})
        L.append('  %-20s %s :%-4d %s -- “%s” -- %s%s' % (k, f, n, 'RESOLVES' if ok else '### FAILS', l.strip()[:140], what,
                                                       (' -- terminal table: grade %s, profile %s, pin %s' % (r.get('grade'), r.get('profile'), r.get('pin'))) if r else ''))
    L += ['  the pages: no node of either page`s list names a terminal the four papers cite (the ζ list relay data/%s, the χ list data/%s)' % (NODES['zeta'], NODES['chi'])]
    trace = sorted(set((c[1], c[2]) for c in K.C))
    L += ['', '### PART E -- H45a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    h45d, reached, matched = h45d_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in K.C)
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### ### **H45d %s** -- the five tests reach %d routes (%s); where the sieve has a row: %s' % (
              h45d, len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                     for r, row, m, t, ok in matched))]
    put_txt('b611_claims_1_2.txt', L)
    put_json('b611_claims.json', dict(at=utc(), n=len(K.C), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, h45d=h45d, matched=matched,
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in K.C]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE DOCUMENT
TITLE = ('# The Four Presentations of the Mechanism Exclusion: the Specification n² → θ → ξ, the Seven Classes, the I.D.S. Mechanism Theorem '
         'and the Three Paths')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional)\b')
HEADLINE = '*This document synthesises the four papers it names and certifies nothing they do not.*'
VERSION = '*v0.1, 2026-10-03 -- written at b611 under `(R221)`(4), the synthesis for Phase 1.2 that THE_KEYSTONE_CENSUS v0.3 names (its row R02).*'
BM_TAG = '<!-- b611 (R221) THE v0.1 BACK MATTER, 2026-10-03 -->'
KC_TERMS = ['spectral_cannon', 'conservation_rh', 'integration_rh', 'balance', 'formation']

BODY = [
    ('## 1. The conditional each paper states', [
        'EA states that every nontrivial zero of ζ lies on Re(s) = 1/2 under the conservation clause h2, with the surround h1 complete and only h2 open (EA :48).',
        'ME states the same conditional, the catalogue’s completeness at the ξ interface carried openly as h2 (ME :21).',
        'IR states it under h2 read as the completeness of its Sym ∪ Card type partition (IR :151), and IP under h2 read as its three paths saturating the catalogue (IP :317).',
        'EA names h2 in four equivalent faces: the Euler balance at some prime, realization-totality at the ξ interface, the R4 positivity face and the Mellin-nonvanishing clause (EA :387).',
        'EA places the whole logical weight on one claim, that the seven-class catalogue is exhaustive, which is h2 (EA :399).']),
    ('## 2. The specification and the seven classes', [
        'EA states that ξ is an entire function of order one satisfying ξ(s) = ξ(1 − s) (EA :70).',
        'EA states that the functional equation and Schwarz reflection set the zeros in quadruples, collapsing to pairs on the critical line (EA :130).',
        'EA counts the classes by stage: two from the group structures of ℤ (EA :164), three from the places of ℚ by Ostrowski’s theorem (EA :178, EA :192), two from the output stage as a structural reading (EA :210), and none from the interfaces, which it calls s-dark (EA :216).',
        'ME gives the same count and states that the arithmetic 2 + 3 + 2 + 0 = 7 is checked in Lean (ME :93).',
        'EA states that each of the seven classes identifies σ = 1/2 and fails to produce a zero off the line (EA :240), and ME that the catalogue is exhaustive by Ostrowski’s theorem with Conservation sealing the interfaces (ME :111).']),
    ('## 3. The exclusion principle and the Mechanism Theorem', [
        'EA names its method exhaustive mechanism enumeration from a finite specification (EA :50).',
        'EA states the SIDE Exclusion Principle, that in a determined system with an exhaustive catalogue a property no class produces does not hold (EA :99).',
        'ME and IR state the Mechanism Theorem, no mechanism meaning no effect, by a five-step derivation from independence, determination and symmetry (ME :49, IR :96).',
        'IR grounds the derivation in the statement that independent structures cannot conspire (IR :28).',
        'IR states that the archimedean and multiplicative structures are independent by six criteria (IR :123), and that an off-line zero is a location-type property neither produces (IR :133).',
        'ME states that independence, determination and symmetry are grounded in five traditions and validated on five test cases (ME :37), and IR places them at the level of the axiom of choice (IR :54).']),
    ('## 4. The analytic pieces', [
        'ME states that the completed zeta function is real on the critical line (ME :137) and that off the line a zero needs two real conditions at once (ME :141).',
        'ME states that its derivative is purely imaginary on the line (ME :145).',
        'ME states that at a simple zero the level curves cross perpendicularly and that |Im| grows along the curve Re = 0 without returning to zero (ME :149), and IP states the growth as strict (IP :167).',
        'ME states that in a determined system generic behaviour is actual (ME :151).',
        'IP states that σ = 1/2 is the unique fixed point of the functional equation’s symmetry (IP :87) and that the Euler product’s contributions balance only there (IP :97).']),
    ('## 5. Simplicity and the explicit formula', [
        'IP states the Weil explicit formula as an identity between a sum over zeros and a sum over primes (IP :125).',
        'ME states that localizing it at a zero forces the multiplicity to a prime-side value, computed as 1 at every tested zero (ME :161), and IP reports the residue at the first zero as 1.0000 (IP :137).',
        'ME sets this beside the Lefschetz trace formula of the function-field case (ME :163).']),
    ('## 6. The controlled comparison and the computations', [
        'EA states that Epstein zeta functions satisfy functional equations, generally lack Euler products and can carry off-line zeros (EA :316).',
        'ME reads the comparison as making the Euler product responsible for confinement together with the functional equation (ME :127).',
        'EA reports ζ’s zeros computed on the line to 10¹³ and more (EA :331), and IP reports checks at ten zeros (IP :176, IP :298).']),
    ('## 7. The readings across programmes', [
        'EA states that ten research programmes decompose into the seven classes (EA :281) and reads the programmes that stalled as having crossed a dark interface (EA :296).',
        'EA states an Identity-Formation Bijection between classes and identity elements (EA :341) and reads the critical line as the identity subspace of arithmetic (EA :367).',
        'IP states that its three paths converge and calls their agreement necessary (IP :26).',
        'ME withdraws its five identification paths as an argument for placement, since they share one involution and identify the line (ME :275).']),
    ('## 8. The compiled pieces the papers name', [
        'EA and IR name the conditional StructuralExhaustiveness → RH as the kernel’s output and say they argue for its antecedent (EA :542, IR :302).',
        'EA names the route and formation terminals at SIDE-kernel v1.2 with their axiom profiles (EA :542).',
        'ME names the residual axiom all_zeros_simple as the simplicity face of h2 (ME :210), while its conclusion still states that no axiom remains (ME :306).']),
    ('## 9. What the papers leave open', [
        'IP states that the paths’ independence is evidence for h2 and not a discharge of it (IP :317).',
        'IP lists as owed the formalization of its localization, checks beyond ten zeros and an unconditional simplicity (IP :341).',
        'IR states that ABC and an arithmetic P ≠ NP follow from independence, determination and symmetry (IR :165).']),
]
TRACE_RE = re.compile(r'\b(EA|ME|IR|IP) :(\d+)')


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | paper | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(P[k][0].lstrip('# ').strip()), _cell(st[5]).replace('*', '')[:60]))
    qn = {'spectral_cannon': 'SpectralCannonFull.spectral_cannon', 'conservation_rh': 'ConservationBridge.riemann_hypothesis',
          'integration_rh': 'techne_kernel_integration.rh_from_structural_exhaustiveness', 'balance': 'balance_theorem', 'formation': 'SIDEKernel.formation'}
    names = ', '.join('`%s` (%s :%d)' % (qn[x], K.KREADS[x][0], K.KREADS[x][1]) for x in KC_TERMS)
    return [TITLE, '',
            '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-03 (b611), under `(R221)`(3)-(4): '
            'the tier the rows earn, decided after they were graded -- %d rows read kernel-verified, each a terminal at SIDE-kernel v1.2 = `b1407b2` whose '
            'statement carries its claim (%s); the synthesis relationships are cited as Tier C allows, each row at its stated grade (`(R19)`).*' % (
                tier, cert_rows, names), '',
            HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for Phase 1.2 (THE_KEYSTONE_CENSUS v0.3, its row R02 and §2): the four papers REGISTRY '
            'files as 1.5a-1 to 1.5a-4, each claim listed with the grade its own text supports; for a reader who meets those papers and needs what each '
            'states and what backs it.*', '',
            '**The papers, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** The class symbols in EA and ME are in the EXCLUSION-ORDER scheme those papers declare at their :2, where C₄ is the '
            'Euler product; the kernel’s enumeration names the Euler class `C2_euler`. The grades are `(R19)`’s vocabulary as `(R220)`(5) lists it -- '
            'kernel-verified at a pin, theorem-supported, argument-supported, computationally-verified, synthesis-suggested, statement-grade -- and a '
            'row whose backing is not machine-checked says so; cite the synthesis for orientation and each row at its stated grade.', '']


def _corr():
    S = ['## Correspondence', '',
         '*Every claim of the four papers this document carries, with the grade the paper’s own text supports. A route is read through the sieve’s '
         'five tests in order; the routes and their instruments are in the back matter.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in K.C:
        cid, pk, n, _needle, text, grade, _support, reason, route, kr = c
        back = reason + ((' -- read at the pin: ' + '; '.join(K.KREADS[x][3] for x in kr if not x.endswith('_stmt') and x not in ('cons_hyp', 'integration_se')))
                         if kr else '')
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(back), rcell))
    return S + ['']


def _back():
    sieve = K.sieve_rows()
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-03 by b611 under the author’s ruling `(R221)`(3)-(4), by the synthesis form of `(R220)`(5)', '',
         '### The grading rule, the seat’s and strikeable', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.', '',
         '### The routes through the five tests', '',
         '| route | claims | verdict | test, instrument at pin | reason | the sieve’s row |', '|:--|:--|:--|:--|:--|:--|']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        B.append('| %s | %s | %s | %s | %s | %s |' % (r, ', '.join(x[0] for x in cs), v, ('%d (%s)' % (t, inst)) if t else '—', _cell(why),
                                                   ('%s, %s' % (row, ' '.join(sieve.get(row, ('?', ''))).replace(' —', ''))) if row else 'none'))
    B += ['', '### The terminals read at SIDE-kernel v1.2 = `b1407b2`', '', '| file | line | the line read | what it states |', '|:--|:--|:--|:--|']
    for k, (f, n, needle, what) in K.KREADS.items():
        B.append('| `%s` | :%d | `%s` | %s |' % (f, n, _cell(needle), _cell(what)))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b611 |' % DOC]
    for k, (path, rid, _rl) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R02 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/b611_claims_1_2.txt` | banked before this document |', '',
          '### Version history', '',
          '- **v0.1, 2026-10-03 (b611, `(R221)`(4))**: the synthesis of 1.5a-1 to 1.5a-4, %d claims graded, the routes read through the five tests.' % len(K.C), '']
    return B


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    return ('KC' if cert else 'C'), len(cert)


def doc(*a):
    """### PLACE-papers phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md (created) and data/b611_doc.json; `dry`: the scratchpad.
    ### Needs the claim bank first."""
    if not os.path.exists(_p('b611_claims.json')):
        sys.exit('### THE CLAIM BANK IS NOT BANKED -- NOTHING WRITTEN')
    tier, ncert = _tier()
    front = _front(tier, ncert)
    corr = _corr()
    body = []
    for h, ss in BODY:
        body += [h, ''] + [' '.join(ss), '']
    lines = (front + corr) if tier == 'KC' else front
    body_at = len(lines) + 1
    lines = lines + body
    body_end = len(lines)
    lines = lines + (corr if tier == 'C' else []) + _back()
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b611_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b611_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(K.C)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b611_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b611_doc_termscan.txt', t.rstrip(NL).split(NL))


def h45a(ls, J):
    """### every body sentence carries a trace, and every trace is a (paper, line) pair of the bank: (ok, sentences, failing)."""
    trace = set((p, n) for p, n in jl('b611_claims.json')['trace'])
    body = [l for l in ls[J['body_at'] - 1:J['body_end']] if l.strip() and not l.startswith('#')]
    sents = [s for l in body for s in _segs(l)]
    bad = []
    for s in sents:
        tr = [(m.group(1), int(m.group(2))) for m in TRACE_RE.finditer(s)]
        if not tr or any(x not in trace for x in tr):
            bad.append(s[:120])
    return not bad, len(sents), bad


def nodisclosure():
    """### the no-disclosure arm: every prose sentence of 60 characters or more in TECHNE-Core's module documents, read locally and never
    ### printed, searched for in this document; the count of hits is banked, the sentences are not."""
    TE = 'D:/MY-DOwnloads/TECHNE-Core'
    files = [x for x in g(TE, 'ls-files', 'modules').split(NL) if x.endswith('.md')]
    needles = set()
    for f in files:
        try:
            t = io.open(os.path.join(TE, f), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for s in re.split(r'(?<=[.!?])\s+', t):
            s = ' '.join(s.split())
            if len(s) >= 60 and not s.startswith('|') and not s.startswith('#'):
                needles.add(s)
    text = ' '.join(' '.join(doc_lines()).split())
    hits = sum(1 for s in needles if s in text)
    return dict(files=len(files), needles=len(needles), hits=hits)


def doc_bank(*a):
    """### data/b611_doc_bank.txt and data/b611_h45.json: the title's property-word check, H45a-H45c, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b611_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b611_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h45a(ls, J)
    rows = [l for l in ls[J['corr_at']:] if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h45b = 'HOLDS' if len(rows) >= 10 and not over and len(rows) == len(K.C) else 'REFUTED'
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    h45c = 'HOLDS' if ('TIER C**' in tier_line) or ('TIER KC**' in tier_line and 'SIDE-kernel v1.2 = `b1407b2`' in tier_line
                                                    and '`SpectralCannonFull.spectral_cannon`' in tier_line) else 'REFUTED'
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    nd = nodisclosure()
    L = ['b611 -- COMPONENT 3: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified, so the tier line reads KC with its certifying terminals named at SIDE-kernel v1.2 = b1407b2; '
         'the line: %s' % (J['tier'], J['cert_rows'], tier_line[:400]),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'after the front matter, before the body (KC)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s' % (HEADLINE in ls[:12]),
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM: TECHNE-Core module documents %d, prose sentences of 60 characters or more %d (read, not printed); found in this '
         'document: %d' % (nd['files'], nd['needles'], nd['hits']),
         '### H45a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H45a %s** -- every body sentence traces to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H45b %s** -- the Correspondence carries %d rows (at least ten), none graded above its paper`s named backing (%s)' % (h45b, len(rows), over or 'none'),
         '### ### **H45c %s** -- the tier line reads %s with the certifying terminal named at its pin' % (h45c, J['tier']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and nd['hits'] == 0 and placed else '### ### **HELD.**']
    put_txt('b611_doc_bank.txt', L)
    put_json('b611_h45.json', dict(H45a='HOLDS' if a_ok else 'REFUTED', H45b=h45b, H45c=h45c, sentences=n_sent, untraced=a_bad, rows=len(rows), over=over,
                                   clean=clean, ceiling=len(ceiling), title_props=title_props, nodisclosure=nd, placed=placed, tier=J['tier']))
    for l in L[-5:]:
        print(l)


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b611_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b611_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b611_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b611 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b611_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b611_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H45a', 'H45b', 'H45c', 'H45d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf'}
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + (CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md')
S4_EXPECT = {'zeta': True, 'chi': False}   # ### the seat's expectation, registered on the face


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores(*a):
    H, CJ, J = jl('b611_h45.json'), jl('b611_claims.json'), jl('b611_doc.json')
    Z, X = jl('b611_page_zeta.json'), jl('b611_page_chi.json')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in KERN_PIN}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b611_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b610_closing_push_out.txt'))
    rc = K.resolve_claims()
    rk = K.resolve_kernel()
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    kv_ok = all(c[9] and all(ok for k, ok, _l in rk if k in c[9]) for c in kv)
    arms2 = rd('b611_page_arms_c2.txt')
    nroutes = len(CJ['routes'])
    S = {
        'H45a': (H['H45a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H45b': (H['H45b'], 'Correspondence rows %d, graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H45c': (H['H45c'], 'the tier line reads %s, %d kernel-verified rows, the terminals named at SIDE-kernel v1.2 = b1407b2' % (H['tier'], J['cert_rows'])),
        'H45d': (CJ['h45d'], 'routes reached %d; against the sieve: %s' % (nroutes, CJ['matched'])),
        'N1': ('HELD' if CJ['n'] >= 25 and nroutes >= 3 else 'REFUTED', '%d claims, %d routes' % (CJ['n'], nroutes)),
        'N2': ('HELD' if kv_ok else 'REFUTED', '%d kernel-verified rows, each naming a terminal at SIDE-kernel v1.2 read on its line: %s' % (len(kv), kv_ok)),
        'N3': ('HELD' if H['tier'] == 'C' else 'REFUTED', 'the tier line reads %s: %d rows are kernel-verified, so by (R220)(5) the line reads KC' % (H['tier'], J['cert_rows'])),
        'N4': ('HELD' if H['H45a'] == 'HOLDS' and H['clean'] and H['ceiling'] == 0 else 'REFUTED',
               'every body sentence traced %s ; the scanner %s ; the ceiling pattern %d' % (H['H45a'], 'CLEAN' if H['clean'] else 'NOT CLEAN', H['ceiling'])),
        'N5': ('HELD' if kern == KERN_PIN and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved %s; the papers, the census, REGISTRY and SPIRAL_MAP unedited %s; PLACE-papers %s (wanted %s); relay '
               'beyond the act`s banks, tools and the table %s' % (kern == KERN_PIN, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if all(ok for _k, ok, _l in rk) and kv_ok else 'REFUTED', 'kernel reads at v1.2: %d of %d ; every kernel-verified row names a read %s' % (
            sum(ok for _k, ok, _l in rk), len(rk), kv_ok)),
        'S3': ('HELD' if H['placed'] else 'REFUTED', 'the Correspondence placed by (R221)(3) for tier %s: %s' % (H['tier'], H['placed'])),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the page commits: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b611_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _title():
    J = jl('b611_doc.json')
    return ('## The Phase 1.2 synthesis: the four presentations of the mechanism exclusion at v0.1 from 1.5a-1 to 1.5a-4, %d claims graded, tier %s'
            % (J['rows'], J['tier']))


TRAIL_HEAD = ('### b611 — lane three, act thirty-eight under (R221): the synthesis for Phase 1.2 -- one document from the cluster’s four papers, '
              'every claim graded by its paper’s own text; the ANNEX act struck; W-ORD-TAG-REMOTES entered')


def _finding_text():
    S, J, CJ, H = jl('b611_scores.json'), jl('b611_doc.json'), jl('b611_claims.json'), jl('b611_h45.json')
    rl = jl('b611_record_lines.json')
    w, an, tg, fa, sf = [x['line'] for x in rl['lines']]
    dc = _pp_commit('b611 (R221)(4): ' + DOC)
    t = _title()
    gr = CJ['grades']
    e = ['', t, '',
         '*Filed at b611 on the author’s ruling `(R221)`. Banks: relay `data/b611_reads.txt`, `data/b611_claims_1_2.txt`, `data/b611_doc_bank.txt`, '
         '`data/b611_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The document** (`(R221)`(4)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the four papers REGISTRY files as 1.5a-1 to '
         '1.5a-4 read whole at f374bba, %d claims each restated in one sentence and graded by its paper’s own text -- kernel-verified %d, '
         'theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d. Tier %s: the '
         'kernel-verified rows are terminals at SIDE-kernel v1.2 = b1407b2 whose statements carry their claims -- the spectral cannon, the two '
         'compiled conditionals, the balance theorem and the formation arithmetic -- so the Correspondence sits after the front matter (`(R221)`(3)). '
         'Read at that pin, the conditional the papers call the kernel’s output has for antecedent ∀ σ, is_xi_zero σ → σ = 1/2, and the '
         'conservation conditional’s premise is the sieve’s RH-02, the clause restated.' % (
             DOC, dc, CJ['n'], gr.get('kernel-verified', 0), gr.get('theorem-supported', 0), gr.get('argument-supported', 0),
             gr.get('computationally-verified', 0), gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), J['tier']), '',
         '**The routes** (the five tests). %d routes: the mechanism enumeration DARK by test 2, matching the sieve’s RH-60; the type analysis, the '
         'perpendicular-crossing monotonicity, the determination-genericity step and the fixed-point path DARK by test 2, each meeting the Epstein '
         'configuration unchanged; the trace-formula simplicity route DARK by test 4, its value computed at finitely many zeros; the five '
         'identification paths NOT A ROUTE, withdrawn by their own paper.' % len(CJ['routes']), '',
         '**The record lines.** b610’s weight at FINDINGS :%d; the ANNEX act struck at OPEN_TRAILS :%d; W-ORD-TAG-REMOTES at :%d; the two fact items '
         'at :%d; the synthesis form’s three clauses at :%d.' % (w, an, tg, fa, sf), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R02 (FINDINGS :7212, b610’s §2) and reads its routes '
         'against b609’s sieve rows (:7186, RH-60’s DARK by test 2 met again by the enumeration as these papers state it); its conditional rows re-read '
         'b609’s finding that Integration’s StructuralExhaustiveness is RH restated, now at the pin the papers cite. It strengthens the programme’s '
         'offering of Phase 1.2: the four presentations, two of them superseded or archival in REGISTRY, now have one place where each claim stands '
         'at its own grade.', '',
         '**Next.** Per `(R221)`(5): b612, the synthesis act for 1.5E. The author rules on the closing.', '',
         '*Nothing deposits; no paper of the cluster edited; README, REGISTRY and the census unwritten; nothing here is a statement about RH, GRH or '
         'any zero beyond the compiled statements’ own words.*', '']
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
    put_json('b611_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b611_scores.json'), jl('b611_findings.json'), jl('b611_record_lines.json')
    w, an, tg, fa, sf = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R221) ratified.** (1) b610 at its weight. (2) The seat’s items ruled: the ANNEX act struck, W-ORD-TAG-REMOTES entered, two fact items '
             'entered. (3) The synthesis form’s three clauses. (4) The synthesis for Phase 1.2; H45a-H45d. (5) The act after: b612.', '',
             '**Entered:** FINDINGS.md:%d (b610’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the ANNEX act struck, addressed '
             'to b610’s record :12568), :%d (W-ORD-TAG-REMOTES), :%d (two fact items), :%d (the form’s three clauses, addressed to :12566); this record; '
             'PLACE-papers `%s`; relay data/b611_claims_1_2.txt.' % (w, fj['entry_line'], an, tg, fa, sf, DOC), '',
             '**Resolved by the seat, for the author’s strike:** the grading rule (kernel-verified only for a terminal the paper names at a pin whose '
             'statement read there carries the claim); the routes and their verdicts; the tier read from the rows, KC; the census row R02 updated at '
             'the census’s next version, not here. No prompt was put (relay data/b611_author_answers.txt).', '',
             '**For the author:** at SIDE-kernel v1.2 no declaration begins `axiom`, so ME :210’s residual axiom all_zeros_simple stands only in comments '
             'there; ME :93 says `native_decide` where v1.2 compiles the count by `decide`; the bare name structural_exhaustiveness_proved resolves to two '
             'theorems at v1.2; the cluster’s folder also holds THE_RIEMANN_PATHS_CLUSTER_SPINE.md, a spine of the 1.5A keystones that no registry row '
             'names.', '',
             '**Defects** (relay data/b611_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R221)`(5), b612, the synthesis act for 1.5E; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left '
             'it; the four lists stay OPEN.', '']
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
    put_json('b611_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b611_trail.json')['line'])


def desk(*a):
    S = jl('b611_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b611 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H45a-H45d, (R221)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H45 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
        sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b611_defects.txt').rstrip(NL).split(NL)
    put_txt('b611_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b611_scores.json'), jl('b611_findings.json'), jl('b611_trail.json'), jl('b611_record_lines.json')
    Z, X = jl('b611_page_zeta.json'), jl('b611_page_chi.json')
    L = ['b611 -- THE COMPONENTS, BANKED UNDER (R221).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b610`s closing push-out relay %s ; push-b610* branches deleted by name '
         '(data/b611_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b611_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b610`s weight FINDINGS :%d ; the ANNEX act struck OPEN_TRAILS :%d ; W-ORD-TAG-REMOTES :%d ; two fact items :%d ; the '
         'form`s three clauses :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the claim bank data/b611_claims_1_2.txt ; H45d %s' % S['H45d'][0],
         '### COMPONENT 3 : the document %s ; data/b611_doc_bank.txt ; H45a %s, H45b %s, H45c %s' % (DOC, S['H45a'][0], S['H45b'][0], S['H45c'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b611_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b612 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b611_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b611_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
