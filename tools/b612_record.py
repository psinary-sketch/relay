# -*- coding: utf-8 -*-
"""b612_record.py -- THE ACT'S RECORD TOOL, UNDER (R222). ### ONE SUBCOMMAND PER BANK.

### ### b612: LANE THREE, ACT THIRTY-NINE -- THE SYNTHESIS FOR CLUSTER 1.5E: ONE DOCUMENT FROM THE CLUSTER'S SIX PAPERS READ AT ADDRESS,
### EVERY CLAIM GRADED BY ITS PAPER'S OWN TEXT, THE ROUTES READ BY THE FIVE TESTS.
### Subcommands write only `data/b612_*` unless the docstring names another file; `dry` on the command line routes every b612 bank and the
### document to the seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are written by
### encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. The act's data and resolvers are
### tools/b612_claims.py's. No platform call. No Lean call. The template is tools/b611_record.py.
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
import b612_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = '4c6c371c'
STEPZERO = '4bfcaa29'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/8f2ff82c-2889-4443-a8e7-85de4d1b215f/scratchpad'
SESSION_ID = '8f2ff82c-2889-4443-a8e7-85de4d1b215f'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md'
B611_DOC = 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
BANK = 'b612_claims_1_5E.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines')   # ### for these, `dry` prints and appends nothing
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b612_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b612_') else '', name, len(b)))
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


DEFECTS = []
DEFECT_SHORT = []


def defects(*a):
    L = ['b612 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b612_defects.txt', L)


# ================================================================================ READING (1): THE READS
def _kr(label, pk, path, sel):
    repo, pin, _w = K.PINS[pk]
    return (label, 'D:/' + repo, pin, path, sel, 220)


READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the 1.5E row and the no-keystone section', PP, PRE_PP, CEN3, ('GREP', r'^\| R07 \||^## §2|^- \*\*R07 '), 900),
    ('REGISTRY.md: the 1.5E heading and rows 1.5e-1 to 1.5e-6', PP, PRE_PP, 'REGISTRY.md', [187, 191, 192, 193, 194, 195, 196], 900),
    ('CONSTANCE.md whole (1.5e-1)', PP, PRE_PP, K.PAPERS['CO'][0], 'ALL', 300),
    ('FROBENIUS.md whole (1.5e-2)', PP, PRE_PP, K.PAPERS['FR'][0], 'ALL', 300),
    ('TRIVIUM.md whole (1.5e-3)', PP, PRE_PP, K.PAPERS['TR'][0], 'ALL', 300),
    ('TRIVIUM_FINDINGS.md whole (1.5e-4)', PP, PRE_PP, K.PAPERS['TF'][0], 'ALL', 300),
    ('TRIVIUM_IDENTITY_SUBSPACE.md whole (1.5e-5)', PP, PRE_PP, K.PAPERS['TS'][0], 'ALL', 300),
    ('CLASS_NUMBER_ANOMALY.md whole (1.5e-6)', PP, PRE_PP, K.PAPERS['CN'][0], 'ALL', 300),
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the five tests, the rows the routes meet (RH-58, RH-60), the Epstein row FD-01 and the Cubit / Trivium table', PP, PRE_PP,
     K.SIEVE, [27, 28, 29, 30, 31, 120, 122, 282, 560, 564], 700),
    ('OPEN_TRAILS: the form, the precedence order, the sequence`s form, the form`s three clauses and b611`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 12228, 12566, 12601, 12603], 1500),
    ('THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md v0.1, the form`s worked instance: tier line, head line, version, Correspondence, '
     'body, back matter, and the row ME-14', PP, PRE_PP, B611_DOC, [1, 3, 5, 7, 22, 62, 84, 122], 500),
    _kr('SIDE-frobenius v0.1.0: the Frobenius number, the indicial terminals and the modular relations', 'frobenius', 'SIDEFrobenius/Indicial.lean',
        [29, 32, 33, 54, 55, 63, 65, 68, 69, 70, 85, 86, 91, 92, 95, 98]),
    _kr('SIDE-class-number-anomaly v0.2: the class-number table, the honesty note and the diagonal biconditional', 'cna',
        'SIDEClassNumberAnomaly/Basic.lean', [52, 53, 59, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207]),
    _kr('SIDE-dirichlet-mod-24 v0.1.0: the units, their squares and the count equality', 'mod24', 'SIDEDirichletMod24/Basic.lean',
        [57, 62, 82, 83, 84, 120, 122, 124, 125, 127]),
    _kr('SIDE-substrate-cluster v0.4: the (3, 3, 1) partition', 'substrate', 'SIDESubstrateCluster/Substrate.lean', [126, 127, 128, 129, 130]),
    _kr('SIDE-substrate-cluster v0.4: the pairing obstruction', 'substrate', 'SIDESubstrateCluster/PairingObstruction.lean', [41, 64, 65, 66]),
    _kr('SIDE-bijection v0.1: the abstract schema', 'bij01', 'SIDEBijection/Theorem.lean', [134, 135, 137]),
    _kr('SIDE-bijection v0.2.0: the instance sideIDS', 'bij020', 'SIDEBijection/Theorem.lean', [230, 231, 232, 236, 241, 242, 243]),
    _kr('SIDE-trivium 1df5bad4: the Trivium theorem', 'trivium', 'Trivium/Bijection.lean', [64, 74, 256, 257, 258, 259]),
    _kr('SIDE-spinor v0.1.0: spinor_forces_half (CONSTANCE names it without a pin)', 'spinor', 'SIDESpinor/Spinor.lean', [70]),
    ('relay data/housekeeping_terminal_table.txt: H-TT-1', RELAY, STEPZERO, 'data/housekeeping_terminal_table.txt', [3], 600),
    ('relay data/b611_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b611_closing_push_out.txt', 'ALL', 260),
    ('relay data/b611_scores.json (whole)', RELAY, STEPZERO, 'data/b611_scores.json', 'ALL', 300),
]


def reads(*a):
    L = ['b612 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    L += ['', '### THE PINS THE PAPERS NAME, EACH RESOLVED IN ITS CLONE AND AT ITS REMOTE:']
    for k in K.PINS:
        key, repo, pin, loc, rem = K.pin_state(k)
        L.append('    %-10s %s %s -> %s ; at the remote: %s' % (key, repo, pin, loc, rem or '### NOT AT THE REMOTE'))
    L += ['### TECHNE mentions in the six papers: %s' % {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()},
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b612_reads.txt', L)


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
    L = ['### b612 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-03), banked verbatim with the options and the recommended '
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
    put_txt('b612_author_answers.txt', L)


ANSWERS_FROM_LINE = 0   # ### the session carries b610 and b611 too; neither put a prompt, so every call found is b612's


# ================================================================================ COMPONENT 1: THE RECORD LINES
B611_ENTRY = '## The Phase 1.2 synthesis: the four presentations of the mechanism exclusion at v0.1'
B611_TRAIL = '### b611 — lane three, act thirty-eight under (R221): the synthesis for Phase 1.2'
W_HEAD = '*Appended 2026-10-03 by b612 to b611’s entry (:%d), under `(R222)`(1) -- b611 AT ITS WEIGHT; THE GRADING RULE, THE VERDICTS AND THE TIER CONFIRMED:*'
F_HEAD = ('*Appended 2026-10-03 by b612 to b611’s record (:%d), under `(R222)`(2)(i)-(iii) -- THREE FACT ITEMS FOR THE PHASE 1.2 PAPERS’ '
          'NEXT EDITIONS, NOT CORRECTED IN THE SYNTHESIS:*')
R_HEAD = '*Appended 2026-10-03 by b612, under `(R222)`(2)(iv) -- A REGISTRY ROW-ADDITION ITEM, FOR THE AUTHOR’S WORD:*'


def _b611():
    S = json.loads(R4._show(RELAY, STEPZERO, 'data/b611_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, trail):
    s = _b611()
    allh = lambda ks: 'HELD' if all(s[k] == 'HELD' for k in ks) else [s[k] for k in ks]   # noqa: E731
    t1 = ('\n%s THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md v0.1 (PLACE-papers c6a8d33), in the Phase 1.2 papers’ folder: 1.5a-1 to '
          '1.5a-4 read whole at f374bba and unedited; 55 claims, each restated in one sentence and graded by its own paper’s text; tier KC on 8 '
          'rows naming terminals at SIDE-kernel v1.2 = b1407b2 whose statements, read at the pin, carry their claims, the Correspondence after '
          'the front matter; 7 routes -- the mechanism enumeration DARK by test 2 matching RH-60, four more DARK by test 2, one by test 4, the '
          'five identification paths NOT A ROUTE, withdrawn by their own paper; the ζ page with one Placement row (bb85d86), the χ page '
          'unchanged. The verdicts, as relay data/b611_scores.json prints them: H45a-H45d %s, %s, %s, %s; N1, N2, N4, N5 %s; N3 %s, the tier '
          'reading KC where the navigator expected C, the better outcome; S1-S5 %s. The author confirms the grading rule, the routes’ verdicts '
          'and the KC tier. FINDINGS :7238, :7240; OPEN_TRAILS :12595, :12597, :12599, :12601, :12603; PLACE-papers a79215a; relay b369460b, '
          '4c6c371c. The suite 82 of 82 before and after the push. Defect (a) the seat’s, a strict comparison of two whole-second stamps on '
          'a true order, repaired and the two appends cut back by recorded length and re-appended. Nothing deposited; no kernel touched; '
          'TECHNE-Core untouched.\n' % (W_HEAD % entry, s['H45a'], s['H45b'], s['H45c'], s['H45d'], allh(('N1', 'N2', 'N4', 'N5')), s['N3'],
                                        allh(('S1', 'S2', 'S3', 'S4', 'S5'))))
    t2 = ('\n%s (i) phase1.5/proofs/MECHANISM_EXCLUSION.md :210 calls all_zeros_simple a residual axiom, while at SIDE-kernel v1.2 no '
          'declaration begins axiom and all_zeros_simple occurs only in a comment (Kernel/PerpendicularCrossing.lean :173): the sentence takes '
          'the fact clause at that paper’s edition, and the synthesis’s row ME-14 already reads statement-grade with that reason '
          '(phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md :62). (ii) MECHANISM_EXCLUSION.md :93 says native_decide, '
          'where v1.2 compiles the count by decide (Kernel/Core.lean :50, :53). (iii) the bare name structural_exhaustiveness_proved names '
          'two theorems at v1.2 (Bridge/TheBridgeComplete.lean :188, Bridge/ConservationBridge.lean :29), H-TT-1 already (relay '
          'data/housekeeping_terminal_table.txt :3): the citations at THE_EXCLUSION_ARCHITECTURE.md :542, MECHANISM_EXCLUSION.md :408, '
          'IDS_TO_RH.md :302 and INTEGRATED_PROOF.md :403 take the qualified name at their papers’ editions.\n' % (F_HEAD % trail))
    t3 = ('\n%s phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md sits in the Phase 1.2 papers’ folder and no REGISTRY row names it. Adding a '
          'row is a source-of-truth change, made as a dated row update in REGISTRY’s own form, on the author’s word; not started. The '
          'census’s row R02 updates at its next version.\n' % R_HEAD)
    return [(W_HEAD % entry, t1), (F_HEAD % trail, t2), (R_HEAD, t3)]


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
    return Q, Q.line_of(Q.FIND, B611_ENTRY), Q.line_of(Q.OT, B611_TRAIL)


def record_lines(*a):
    """### FINDINGS: b611's weight, addressed to b611's entry; OPEN_TRAILS: the three fact items (addressed to b611's record) and the
    ### REGISTRY row-addition item -- each appended at the end."""
    Q, entry, trail = _addr()
    if (entry, trail) != (7240, 12603):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s) -- NOTHING WRITTEN' % (entry, trail))
    parts = _texts(entry, trail)
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
    put_json('b612_record_lines.json', dict(entry=entry, trail=trail, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ================================================================================ COMPONENT 2: THE CLAIM BANK
def _route_rows():
    rs = {}
    for c in K.C:
        if c[8]:
            rs.setdefault(c[8][0], []).append(c)
    return rs


def h46d_score(sieve):
    """### every route's verdict against the sieve's row where one exists; a route with no row is listed for the sieve's next version."""
    rs = _route_rows()
    reached = [r for r, cs in rs.items() if cs[0][8][1] in ('DARK', 'BRIGHT', 'NOT A ROUTE')]
    matched, listed = [], []
    for r, cs in sorted(rs.items()):
        row = cs[0][8][5]
        mine = cs[0][8][1] + ('' if cs[0][8][2] is None else ', test %d' % cs[0][8][2])
        if row and row in sieve:
            v, t = sieve[row]
            theirs = v + ('' if t.strip() == '—' else ', test %s' % t.split()[0])
            matched.append((r, row, mine, theirs, mine == theirs))
        elif not row and cs[0][8][1] != 'NOT A ROUTE':   # ### a path its own paper withdraws is not a route and wants no row
            listed.append((r, mine))
    nonroutes = [r for r, cs in rs.items() if not cs[0][8][5] and cs[0][8][1] == 'NOT A ROUTE']
    ok = bool(reached) and all(x[4] for x in matched) and len(matched) + len(listed) + len(nonroutes) == len(rs)
    return ('HOLDS' if ok else 'REFUTED'), reached, matched, listed


def _tt_rows():
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '[]')
    return T.get('rows') if isinstance(T, dict) else T


def _decl(needle):
    m = re.match(r'^(?:theorem|def|lemma)\s+(\S+)', needle.strip())
    return m.group(1) if m else None


def claims(*a):
    """### data/b612_claims_1_5E.txt and data/b612_claims.json: each paper's path, version and head; every claim with its line, grade and reason;
    ### the routes through the five tests; the terminals at their pins with the table's rows; H46a's trace table and H46d -- banked before any writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    rk = K.resolve_kernel()
    sieve = K.sieve_rows()
    pins = dict((k, K.pin_state(k)) for k in K.PINS)
    if not all(ok for ok, _l in rc.values()) or not all(ok for _k, ok, _l in rk) or not all(p[4] for p in pins.values()):
        sys.exit('### A NEEDLE, A KERNEL READ OR A PIN FAILS -- NOTHING WRITTEN')
    L = ['b612 -- COMPONENT 2: THE CLAIM BANK OF CLUSTER 1.5E, (R222)(3), banked %s before any writing' % utc(),
         '### the papers at PLACE-papers %s; the kernels at the pins the papers name (PART D); the sieve v0.4 at %s' % (PRE_PP, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'A ROUTE is' in x or 'RESOLVES' in x] + ['']
    L += ['### PART A -- THE PAPERS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        reg = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        ver = '; '.join(l.strip() for l in [next((l for l in ls[:20] if re.search(r'^\*{0,2}v\d|^\*{0,2}February|^\*v\.', l.strip())), ''),
                                             next((l for l in ls if re.match(r'^\*\*Version \d', l.strip())), '')] if l)
        L.append('  %s = `%s` -- REGISTRY %s (:%d), its version %s, its status %s -- %d lines -- head :1 “%s” -- the paper`s own version/date line “%s”' % (
            k, path, rid, rline, reg[3], reg[5].replace('*', '')[:40], len(ls), ls[0][:120], ver.strip()[:120]))
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
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', ''))))) if row else 'none: listed for the sieve`s next version'))
    L += ['', '### PART D -- THE TERMINALS AT THEIR PINS, EACH READ ON ITS LINE, WITH THE PIN`S RESOLUTION AND THE TABLE`S ROW:']
    for k in K.PINS:
        key, repo, pin, loc, rem = pins[k]
        L.append('  pin %-10s %s %s -> %s ; at the remote: %s' % (key, repo, pin, loc, rem))
    TT = _tt_rows()
    for k, ok, l in rk:
        pk, f, n, needle, what = K.KREADS[k]
        repo = K.PINS[pk][0]
        nm = _decl(needle)
        r = next((x for x in TT if x.get('repo') == repo and nm and (x.get('name') == nm or str(x.get('name', '')).endswith('.' + nm))), None) if nm else None
        L.append('  %-12s %s %s :%-4d %s -- “%s” -- %s%s' % (k, repo, f, n, 'RESOLVES' if ok else '### FAILS', l.strip()[:140], what,
                                                          (' -- terminal table: %s, grade %s, profile %s' % (r.get('name'), r.get('grade'), r.get('profile'))) if r else
                                                          (' -- terminal table: no row' if nm else '')))
    nodes = {k: io.open(os.path.join(D, v), encoding='utf-8').read() for k, v in NODES.items()}
    named = sorted(set(_decl(v[3]) for v in K.KREADS.values() if _decl(v[3])))
    hits = {k: [x for x in named if re.search(r'\b%s\b' % re.escape(x), t)] for k, t in nodes.items()}
    L += ['  the pages: the cited terminals on the ζ list relay data/%s: %s ; on the χ list data/%s: %s' % (
        NODES['zeta'], hits['zeta'] or 'NONE', NODES['chi'], hits['chi'] or 'NONE')]
    trace = sorted(set((c[1], c[2]) for c in K.C))
    L += ['', '### PART E -- H46a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    h46d, reached, matched, listed = h46d_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in K.C)
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### THE ROUTES WITH NO SIEVE ROW, LISTED FOR THE SIEVE`S NEXT VERSION: %s' % ('; '.join('%s %s' % x for x in listed) or 'none'),
          '### ### **H46d %s** -- the five tests reach %d routes (%s); where the sieve has a row: %s; with no row, listed: %d' % (
              h46d, len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                         for r, row, m, t, ok in matched), len(listed))]
    put_txt(BANK, L)
    put_json('b612_claims.json', dict(at=utc(), n=len(K.C), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, h46d=h46d, matched=matched,
                                      listed=listed, pins={k: list(v) for k, v in pins.items()},
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in K.C]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE DOCUMENT
TITLE = ('# The {2, 3} Substrate and the Trivium: the Frobenius Pair, the Seven Quadratic Fields, the Trivium Vector, the Class-Number '
         'Diagonal and the Prime Mosaic')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional|[Uu]nique|[Ee]xact)\b')
HEADLINE = '*This document synthesises the six papers it names and certifies nothing they do not.*'
VERSION = '*v0.1, 2026-10-03 -- written at b612 under `(R222)`(3), the synthesis for 1.5E that THE_KEYSTONE_CENSUS v0.3 names (its row R07).*'
BM_TAG = '<!-- b612 (R222) THE v0.1 BACK MATTER, 2026-10-03 -->'

BODY = [
    ('## 1. The papers and their scope', [
        'CO states that its physics readings are proposed and not forced and records its reclassification to the theory-space cluster, leaving a pointer here (CO :18).',
        'FR states that it does not establish RH and that an earlier version overstated what the substrate provides (FR :111).',
        'TF calls the Mechanism Theorem the load-bearing axiom of its framework (TF :391), and TS grades its own fold criterion a reformulation and global separation open (TS :660).']),
    ('## 2. The pair {2, 3}', [
        'FR states that {2, 3} is the one coprime pair with both entries at least 2 whose Frobenius number is 1 (FR :26), and CO reaches the same pair from (a − 1)(b − 1) = 2 (CO :324).',
        'FR states that every integer n ≥ 2 is a sum 2a + 3b with a, b ≥ 0 (FR :32).',
        'FR states that the indicial equation of (xp)² factors as (r + 1/2)² = 0 with the double root −1/2 (FR :50), and that the modular generators satisfy S² = −I and, in PSL₂(ℤ), (ST)³ = I (FR :75).',
        'TS records the Frobenius and modular parts as checked in a kernel and Størmer’s finiteness as classical (TS :174).',
        'TF and TS state Størmer’s theorem for {2, 3}, the consecutive smooth pairs being (1, 2), (2, 3), (3, 4) and (8, 9) (TF :241, TS :184).',
        'FR reads {2, 3} as the one basis from which these appearances derive (FR :101) and states that the pair generates the seven discriminants that are the seven mechanism classes of ξ (FR :103).']),
    ('## 3. The balance point and the three roads', [
        'TS states that n^(−σ) = n^(−(1−σ)) for every n ≥ 2 holds exactly at σ = 1/2 (TS :98), as TR and TF state it for the primes (TR :30, TF :22).',
        'TS calls 1/2 an identity element by analogy, as the fixed point of σ ↦ 1 − σ (TS :110).',
        'TR states that in w = s − 1/2 the functional equation reads ξ(w) = ξ(−w) (TR :26), that the exponent 1/2 of the theta transformation comes from the n² in θ (TR :34), and places the Trivium at the fixed point τ = i of S (TR :74).',
        'TF, TS and CO each state five derivations of σ = 1/2 and, corrected on 2026-08-10, call their agreement convergent identification, the derivations sharing the involution σ ↦ 1 − σ and carrying no placement (TF :70, TS :116, CO :2790).',
        'TR states that its Trivium reformulation and RH are the same statement (TR :104).']),
    ('## 4. The seven fields and the valence', [
        'TS states that {−1, 2, 3} generate (ℤ/2)³ in ℚ*/ℚ*², giving seven nontrivial quadratic fields (TS :180), and that the dimension 7 comes from those fields and the Størmer range (TS :194).',
        'TS states that every prime p > 3 splits in exactly 3 or exactly 7 of the seven fields, 7 exactly when (−1/p), (2/p) and (3/p) are all +1 (TS :285), and TF states the dichotomy for every prime (TF :169).',
        'TR reads the seven classes, the seven elements of (ℤ/2)³, the seven Hamming syndromes and the seven Fano points as one algebraic object (TR :112).']),
    ('## 5. The Trivium vector and its structure', [
        'TF and TS state that the matrix vv† of the Trivium vector has spectrum {0⁶, 12} (TF :134, TS :238), and TS gives its eigenvalue entropy as about 0.592 bits (TS :246).',
        'TS states that the Weil representation’s lift of the Fourier transform has order 8 (TS :312) and a correspondence between it and the vector’s quarter-twist (TS :318).',
        'TS states that over the critical line the real bundle is non-orientable (TS :326), with its monodromy at σ = 1/2 alone (TS :359).',
        'TS states that the trefoil’s Alexander polynomial is Φ₆(t) (TS :381) and reads it as the functional equation acting on the quarter-twist (TS :394).']),
    ('## 6. The class-number diagonal', [
        'CN states that six of the seven fields have class number 1 and ℚ(√−6) has class number 2 (CN :15), checked in PARI/GP with a Mathlib derivation open (CN :142).',
        'CN states that ℚ(√−6) is the weight-3 vertex (1, 1, 1) of (ℤ/2)³, the weights splitting (3, 3, 1) (CN :49), and that under antipodal pairing that diagonal is the one unpaired element (CN :132).',
        'CN states that weight 3, class number 2 and discriminant magnitude 24 hold together for d = −6 alone among the seven discriminants (CN :146), the discriminant being −24 since −6 ≡ 2 mod 4 (CN :62).',
        'CN reads the three as views of one property (CN :66), and reads the class number 2 as the arithmetic shadow of the CSS construction (CN :86) and the 3 of the denominator 81 of Ω_b = 4/81 as the ramification of 3 (CN :90).',
        'CN states that (ℤ/24)* has the structure (ℤ/2)³ (CN :53).']),
    ('## 7. The bijections', [
        'CN states that SIDE-bijection v0.1 carries an abstract schema with no concrete seven-count (CN :134), that the schema is demonstrated at the instance sideIDS of total 7 (CN :82), and that SIDE-trivium exhibits MechanismClass ≃ QuadraticDiscriminant with both cardinalities 7 (CN :134).',
        'CN states that an element-level canonical bijection is not forced, a transitive symmetry making any assignment a choice of basis (CN :82).']),
    ('## 8. The analytic thread', [
        'TS states that ξ(1/2 + it) is real (TS :464), that a zero on the line is one real condition and a zero off it two (TS :476), and that at each simple zero the level curves cross at right angles (TS :520).',
        'TS states that along the curve Re ξ = 0 through a simple zero Im ξ vanishes at σ = 1/2 alone nearby (TS :538), gives V′ₖ = −|ξ′|²/u_t along that curve (TS :548), and states that no fold at any zero is equivalent to RH (TS :558).',
        'TS states that these results use only the functional equation and the Cauchy–Riemann equations, not the Euler product (TS :643), and that its computations and its inventory are evidence (TS :671).',
        'CO states the same count of real conditions (CO :2729) and that turning “generically” into “necessarily” for ζ is equivalent to RH (CO :2105).',
        'CO states that Re ξ′(ρ) = 0 at every zero on the line (CO :2746) and that the product formula is s-dark (CO :2754).']),
    ('## 9. The computations', [
        'TS reports C(t) positive at 109 heights (TS :583) and cites Platt and Trudgian’s computation of the first 12,363,153,093,004 zeros on the line (TS :587), and TF records the same range (TF :502).',
        'CO reports partial Euler products approximating the first zero about seventy times more closely than partial Dirichlet sums (CO :2097), and |ζ′(ρ)|/√γ with mean 0.251 over thirty zeros (CO :2772).']),
    ('## 10. The constant-analysis reading', [
        'CO states that six adjacent-generation mass ratios factor into primes tied to {2, 3} and three non-adjacent ones do not (CO :192), and reports 47 of 51 parameters factoring into its fifteen core primes (CO :1327).',
        'CO states that among k = 4 to 17 only k = 6 and 7 make both 2^k + 3 and 2^k + 9 prime (CO :1162), and predicts the two Hubble values 337/5 and 73 exactly (CO :1284).',
        'CO tabulates sixteen predictions as confirmed (CO :1353) and leaves open whether the generation count traces to its sector count (CO :1737).']),
    ('## 11. The routes the papers offer', [
        'TR states that the seven mechanism classes together forbid zeros off the Trivium (TR :106), and TF sets out an architecture ending in the Mechanism Theorem (TF :371).',
        'TS inventories the known mechanisms and finds none producing an off-line zero (TS :607), and states that its three lines of evidence converge on every nontrivial zero lying on the line (TS :615).',
        'CO states that the arithmetic fixing the constants also places the zeta zeros on the line (CO :1824), and that the concentration of the monodromy at σ = 1/2 explains why searches find no off-line zero (CO :2908).']),
    ('## 12. What the papers leave open', [
        'TF states that methods through averaged quantities cannot locate individual zeros (TF :211), that the Euler product converges only for Re(s) > 1 (TF :223), and that its explanation of the 3/4 exponent remains a conjecture (TF :421).',
        'CO states that the remaining step runs from the neighborhood of each zero to the whole strip (CO :2852), and that SIDESpinor.spinor_forces_half does not conclude σ = 1/2 (CO :2888).',
        'FR states that the critical line corresponds to the indicial boundary condition (FR :58), and TR that ξ(1/2 + it) is real, reading the phases of e, i and π as cancelling there (TR :88).']),
]
TRACE_RE = re.compile(r'\b(CO|FR|TR|TF|TS|CN) :(\d+)')
QN = {'g23': 'SIDEFrobenius.g_two_three', 'g23min': 'SIDEFrobenius.g_two_three_minimal', 'ind_factor': 'SIDEFrobenius.indicial_factor',
      'ind_unique': 'SIDEFrobenius.indicial_root_unique', 'ind_half': 'SIDEFrobenius.indicial_forces_half', 'S_sq': 'SIDEFrobenius.S_squared',
      'ST_cu': 'SIDEFrobenius.ST_cubed', 'tri_diag': 'triple_identification_diagonal', 'part_card': 'SIDESubstrateCluster.partition_cardinalities',
      'diag_unp': 'SIDESubstrateCluster.diagonal_unpaired', 'obstr': 'SIDESubstrateCluster.obstruction_theorem',
      'ifb_v01': 'SIDEBijection.identity_formation_bijection', 'side_bij': 'SIDEBijection.sideIDS_bijection', 'side_ids': 'SIDEBijection.sideIDS',
      'triv_thm': 'Trivium.trivium_theorem'}


def _pinstr(pk):
    repo, pin, want = K.PINS[pk]
    return '%s %s = `%s`' % (repo, pin, want) if pin != want else '%s `%s`' % (repo, want)


def cert_terminals():
    """### the certifying terminals: (qualified name, pin key, file, line) for every kernel read a kernel-verified row names"""
    out = []
    for c in K.C:
        if c[5] == 'kernel-verified':
            for k in c[9]:
                if k in QN and (QN[k], k) not in [(x[0], x[4]) for x in out]:
                    pk, f, n, _nd, _w = K.KREADS[k]
                    out.append((QN[k], pk, f, n, k))
    return out


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | paper | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(P[k][0].lstrip('# ').strip()),
                                                                     _cell(st[5]).replace('*', '').split(' → ')[0][:40]))
    bypin = {}
    for qn, pk, f, n, _k in cert_terminals():
        bypin.setdefault(pk, []).append('`%s` (%s :%d)' % (qn, f, n))
    names = '; '.join('at %s: %s' % (_pinstr(pk), ', '.join(v)) for pk, v in bypin.items())
    return [TITLE, '',
            '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-03 (b612), under `(R222)`(3): '
            'the tier the rows earn, decided after they were graded -- %d rows read kernel-verified, each naming terminals at a pin that resolves in '
            'its clone and at its remote, whose statements carry the claim (%s); the synthesis relationships are cited as Tier C allows, each row '
            'at its stated grade (`(R19)`).*' % (tier, cert_rows, names), '',
            HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for cluster 1.5E (THE_KEYSTONE_CENSUS v0.3, its row R07 and §2): the six papers REGISTRY '
            'files as 1.5e-1 to 1.5e-6, each claim listed with the grade its own text supports; for a reader who meets those papers and needs what each '
            'states and what backs it.*', '',
            '**The papers, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** REGISTRY files CONSTANCE (CO) as reclassified to the theory-space cluster with a pointer left here; it is '
            'synthesised here because the census row and REGISTRY’s 1.5E section list it. The grades are `(R19)`’s vocabulary as `(R220)`(5) lists '
            'it -- kernel-verified at a pin, theorem-supported, argument-supported, computationally-verified, synthesis-suggested, statement-grade -- '
            'and a row whose backing is not machine-checked says so; cite the synthesis for orientation and each row at its stated grade.', '']


def _corr():
    S = ['## Correspondence', '',
         '*Every claim of the six papers this document carries, with the grade the paper’s own text supports. A route is read through the sieve’s '
         'five tests in order; the routes and their instruments are in the back matter.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in K.C:
        cid, pk, n, _needle, text, grade, _support, reason, route, kr = c
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(reason), rcell))
    return S + ['']


def _back():
    sieve = K.sieve_rows()
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-03 by b612 under the author’s ruling `(R222)`(3), by the synthesis form of `(R220)`(5) and `(R221)`(3)', '',
         '### The grading rule, confirmed by `(R222)`(1)', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A pin resolves when its commit is in the clone and at the remote, as a remote tag peeling to it or on the remote main.',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.', '',
         '### The routes through the five tests', '',
         '| route | claims | verdict | test, instrument at pin | reason | the sieve’s row |', '|:--|:--|:--|:--|:--|:--|']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        B.append('| %s | %s | %s | %s | %s | %s |' % (r, ', '.join(x[0] for x in cs), v, ('%d (%s)' % (t, inst)) if t else '—', _cell(why),
                                                   ('%s, %s' % (row, ' '.join(sieve.get(row, ('?', ''))).replace(' —', ''))) if row
                                                   else 'none; listed for the sieve’s next version'))
    B += ['', '### The terminals read at their pins', '', '| pin | file | line | the line read | what it states |', '|:--|:--|:--|:--|:--|']
    for k, (pk, f, n, needle, what) in K.KREADS.items():
        B.append('| %s | `%s` | :%d | `%s` | %s |' % (_pinstr(pk), f, n, _cell(needle), _cell(what)))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b612 |' % DOC]
    for k, (path, rid, _rl) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R07 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/%s` | banked before this document |' % BANK, '',
          '### Version history', '',
          '- **v0.1, 2026-10-03 (b612, `(R222)`(3))**: the synthesis of 1.5e-1 to 1.5e-6, %d claims graded, the routes read through the five tests.' % len(K.C), '']
    return B


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    return ('KC' if cert else 'C'), len(cert)


def doc(*a):
    """### PLACE-papers phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md (created) and data/b612_doc.json; `dry`: the
    ### scratchpad. Needs the claim bank first."""
    if not os.path.exists(_p('b612_claims.json')):
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
    dest = os.path.join(SP, 'b612_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b612_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(K.C)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b612_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b612_doc_termscan.txt', t.rstrip(NL).split(NL))


def h46a(ls, J):
    """### every body sentence carries a trace, and every trace is a (paper, line) pair of the bank: (ok, sentences, failing)."""
    trace = set((p, n) for p, n in jl('b612_claims.json')['trace'])
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


def h46c_check(tier_line):
    """### the tier line reads C, or KC with every certifying terminal named and its pin named and resolving"""
    if 'TIER C**' in tier_line:
        return True, []
    miss = []
    for qn, pk, _f, _n, _k in cert_terminals():
        st = K.pin_state(pk)
        if ('`%s`' % qn) not in tier_line or _pinstr(pk) not in tier_line or not st[4]:
            miss.append((qn, pk, bool(st[4])))
    return ('TIER KC**' in tier_line and not miss), miss


def doc_bank(*a):
    """### data/b612_doc_bank.txt and data/b612_h46.json: the title's property-word check, H46a-H46c, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b612_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b612_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h46a(ls, J)
    rows = [l for l in ls[J['corr_at']:] if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h46b = 'HOLDS' if len(rows) >= 10 and not over and len(rows) == len(K.C) else 'REFUTED'
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    c_ok, c_miss = h46c_check(tier_line)
    h46c = 'HOLDS' if c_ok else 'REFUTED'
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    nd = nodisclosure()
    L = ['b612 -- COMPONENT 3: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified, so the tier line reads %s with its certifying terminals named at their pins; the line: %s' % (
             J['tier'], J['cert_rows'], J['tier'], tier_line[:600]),
         '### the certifying terminals named on the tier line with a resolving pin: %d of %d ; missing %s' % (
             len(cert_terminals()) - len(c_miss), len(cert_terminals()), c_miss or 'NONE'),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'after the front matter, before the body (KC)' if placed and J['tier'] == 'KC'
                                                                                          else 'in the back matter (C)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s' % (HEADLINE in ls[:12]),
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM: TECHNE-Core module documents %d, prose sentences of 60 characters or more %d (read, not printed); found in this '
         'document: %d' % (nd['files'], nd['needles'], nd['hits']),
         '### H46a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H46a %s** -- every body sentence traces by path and line to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H46b %s** -- the Correspondence carries %d rows (at least ten), none graded above its paper`s named backing (%s)' % (h46b, len(rows), over or 'none'),
         '### ### **H46c %s** -- the tier line reads %s with every certifying terminal resolving at its pin' % (h46c, J['tier']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and nd['hits'] == 0 and placed else '### ### **HELD.**']
    put_txt('b612_doc_bank.txt', L)
    put_json('b612_h46.json', dict(H46a='HOLDS' if a_ok else 'REFUTED', H46b=h46b, H46c=h46c, sentences=n_sent, untraced=a_bad, rows=len(rows), over=over,
                                   clean=clean, ceiling=len(ceiling), title_props=title_props, nodisclosure=nd, placed=placed, tier=J['tier'],
                                   cert_missing=c_miss))
    for l in L[-5:]:
        print(l)


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b612_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b612_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b612_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b612 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b612_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b612_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H46a', 'H46b', 'H46c', 'H46d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-frobenius': None, 'SIDE-class-number-anomaly': None, 'SIDE-dirichlet-mod-24': None, 'SIDE-substrate-cluster': None,
            'SIDE-bijection': None, 'SIDE-trivium': None, 'SIDE-spinor': None}
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + (CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md', B611_DOC,
                                                     'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', K.SIEVE)
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the seat's expectation, registered on the face


def kern_state():
    """### every kernel this act reads, its main and its tags, at the reads (the face's pins) and now"""
    out = {}
    for k in KERN_PIN:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


KERN_AT_FACE = None   # ### filled from the reads bank's kernel state, banked at data/b612_kernels_face.json


def kernels(*a):
    """### data/b612_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b612_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores(*a):
    H, CJ, J = jl('b612_h46.json'), jl('b612_claims.json'), jl('b612_doc.json')
    Z, X = jl('b612_page_zeta.json'), jl('b612_page_chi.json')
    face = jl('b612_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items() if v)
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b612_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b611_closing_push_out.txt'))
    rc = K.resolve_claims()
    rk = K.resolve_kernel()
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    pins = dict((k, K.pin_state(k)) for k in K.PINS)
    kv_ok = all(c[9] and all(ok for k, ok, _l in rk if k in c[9]) and all(pins[pk][4] for pk in K.kv_pins(c)) for c in kv)
    arms2 = rd('b612_page_arms_c2.txt')
    nroutes = len(CJ['routes'])
    routes_printed = [r for r, cs in _route_rows().items() if cs[0][8][1] and cs[0][8][3]]
    S = {
        'H46a': (H['H46a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H46b': (H['H46b'], 'Correspondence rows %d, graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H46c': (H['H46c'], 'the tier line reads %s, %d kernel-verified rows, every certifying terminal named with its pin resolving (missing %s)' % (
            H['tier'], J['cert_rows'], H['cert_missing'] or 'none')),
        'H46d': (CJ['h46d'], 'routes reached %d; against the sieve: %s; with no row, listed for its next version: %s' % (nroutes, CJ['matched'], CJ['listed'])),
        'N1': ('HELD' if CJ['n'] >= 20 else 'REFUTED', '%d claims (the floor 20)' % CJ['n']),
        'N2': ('HELD' if kv_ok else 'REFUTED', '%d kernel-verified rows, each naming terminals read on their lines at pins that resolve in the clone and '
                                               'at the remote: %s' % (len(kv), kv_ok)),
        'N3': ('HELD' if routes_printed else 'REFUTED', '%d route(s), each printed with its verdict and instrument in data/%s PART C: %s' % (
            len(routes_printed), BANK, ', '.join(sorted(routes_printed)))),
        'N4': ('HELD' if H['H46a'] == 'HOLDS' and H['clean'] and H['ceiling'] == 0 else 'REFUTED',
               'every body sentence traced %s ; the scanner %s ; the ceiling pattern %d' % (H['H46a'], 'CLEAN' if H['clean'] else 'NOT CLEAN', H['ceiling'])),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the papers, the census, REGISTRY, SPIRAL_MAP, b611`s document, the taxonomy and the '
               'sieve unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools and the table %s' % (
                   kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if all(ok for _k, ok, _l in rk) and all(p[4] for p in pins.values()) and kv_ok else 'REFUTED',
               'kernel reads at their pins: %d of %d ; pins resolving at their remotes: %d of %d ; every kernel-verified row names a read %s' % (
                   sum(ok for _k, ok, _l in rk), len(rk), sum(bool(p[4]) for p in pins.values()), len(pins), kv_ok)),
        'S3': ('HELD' if H['placed'] else 'REFUTED', 'the Correspondence placed by (R221)(3) for tier %s: %s' % (H['tier'], H['placed'])),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b612_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _title():
    J, CJ = jl('b612_doc.json'), jl('b612_claims.json')
    return ('## The 1.5E synthesis: the {2, 3} substrate and the Trivium at v0.1 from 1.5e-1 to 1.5e-6, %d claims graded, %d routes read, tier %s'
            % (J['rows'], len(CJ['routes']), J['tier']))


TRAIL_HEAD = ('### b612 — lane three, act thirty-nine under (R222): the synthesis for 1.5E -- one document from the cluster’s six papers read at '
              'address, every claim graded by its paper’s own text, the routes read by the five tests')
FOR_AUTHOR = (
    '(1) TRIVIUM_FINDINGS.md :171 and CONSTANCE.md :2216 give the valence-7 primes as those ≡ ±1 mod 24, where the argument at '
    'TRIVIUM_IDENTITY_SUBSPACE.md :287 and CONSTANCE.md :2210 gives 1 mod 24 alone (a prime ≡ 23 mod 24 has (−1/p) = −1 and valence 3); '
    '(2) FROBENIUS.md :75 and :93 and TRIVIUM_IDENTITY_SUBSPACE.md :174 write (ST)³ = I as the relation checked, where `ST_cubed` at '
    'SIDE-frobenius v0.1.0 compiles (ST)³ = −1 in SL₂(ℤ), I only in PSL₂(ℤ); (3) CLASS_NUMBER_ANOMALY.md :53, :130 and :134 say '
    'SIDE-dirichlet-mod-24 v0.1.0 verifies (ℤ/24)* ≅ (ℤ/2)³, where at 597b0869 φ(24) = 8, the eight squares and a count equality '
    'compile and the isomorphism stands in its comments (:84, :124); (4) CONSTANCE.md :1315 gives the u to t ratio as 79981 = 11 × 661, '
    'which is 7271, and :2469 gives 79949 = 31 × 2579; (5) CONSTANCE.md drops superscripts at :685-:693, :796-:798, :1007 and :1530 '
    '(832 printed as 2 × 13), and :2667 names SL₃(ℤ) for the modular group; (6) TRIVIUM_FINDINGS.md :255 places π^(1/4) between √2 '
    'and √3, where its :257 places it below √2; (7) the census row R07 and REGISTRY’s 1.5E section list CONSTANCE, which REGISTRY :191 '
    'reclassifies to the theory-space cluster -- synthesised here as listed, the reclassification noted in the front matter; (8) the '
    'two clone-only tags the papers cite, SIDE-substrate-cluster v0.4 and SIDE-bijection v0.1, peel to the commits their remotes carry '
    'as v0.1.0 -- W-ORD-TAG-REMOTES’ items, read here')


def _finding_text():
    S, J, CJ = jl('b612_scores.json'), jl('b612_doc.json'), jl('b612_claims.json')
    rl = jl('b612_record_lines.json')
    w, fa, ra = [x['line'] for x in rl['lines']]
    dc = _pp_commit('b612 (R222)(3): ' + DOC)
    t = _title()
    gr = CJ['grades']
    e = ['', t, '',
         '*Filed at b612 on the author’s ruling `(R222)`. Banks: relay `data/b612_reads.txt`, `data/%s`, `data/b612_doc_bank.txt`, '
         '`data/b612_page_arms_c2.txt`. Nothing deposits.*' % BANK, '',
         '**The document** (`(R222)`(3)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the six papers REGISTRY files as 1.5e-1 to '
         '1.5e-6 read whole at %s, %d claims each restated in one sentence and graded by its paper’s own text -- kernel-verified %d, '
         'theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d. Tier %s: the '
         'kernel-verified rows name terminals at six pins of five kernels, each pin resolving in its clone and at its remote -- SIDE-frobenius, '
         'SIDE-class-number-anomaly, SIDE-substrate-cluster, SIDE-bijection at two pins and SIDE-trivium -- so the Correspondence sits after the '
         'front matter (`(R221)`(3)). Read at their pins, the Frobenius number and its minimality, the indicial factorization, the modular '
         'relations in SL₂(ℤ), the (3, 3, 1) partition and the unpaired diagonal, the diagonal biconditional over an encoded class-number table, '
         'the abstract schema and its instance, and the seven-element equivalence carry their rows; SIDE-dirichlet-mod-24 compiles the order and '
         'the exponent of (ℤ/24)* but not the isomorphism, so that row reads argument-supported.' % (
             DOC, dc, PRE_PP, CJ['n'], gr.get('kernel-verified', 0), gr.get('theorem-supported', 0), gr.get('argument-supported', 0),
             gr.get('computationally-verified', 0), gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), J['tier']), '',
         '**The routes** (the five tests). %d routes: the seven-class exclusion DARK by test 2, matching the sieve’s RH-60; the finite computations '
         'NOT A ROUTE, matching RH-58; the five identification paths NOT A ROUTE by the papers’ own correction; the monodromy route, the count of '
         'real conditions, the analytic lines of evidence, the mechanism inventory and the Frobenius property DARK by test 2, each holding unchanged '
         'at the Epstein configuration; the |ζ′|/√γ statistic DARK by test 1. The six routes the sieve has no row for are listed for its next '
         'version.' % len(CJ['routes']), '',
         '**The record lines.** b611’s weight, with the rule, the verdicts and the tier confirmed, at FINDINGS :%d; the three fact items for the '
         'Phase 1.2 papers at OPEN_TRAILS :%d; the REGISTRY row-addition item, for the author’s word, at :%d.' % (w, fa, ra), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R07 (FINDINGS :7212, b610’s §2) and follows the form '
         'b611’s synthesis set (:7240); its routes meet b609’s sieve rows (:7186) at RH-60 and RH-58 and add six for the sieve’s next version; its '
         'kernel rows read the cluster’s kernels at the pins W-ORD-TAG-REMOTES (OPEN_TRAILS :12597) priced, two of them clone-only tags whose '
         'commits the remotes carry. It strengthens the programme’s offering of the {2, 3} substrate: six papers, one reclassified and one '
         'archival in REGISTRY, now have one place where each claim stands at its own grade and each kernel citation is read at its pin.', '',
         '**Next.** Per `(R222)`(4): b613, the synthesis act for 2B. The author rules on the closing.', '',
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
    put_json('b612_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b612_scores.json'), jl('b612_findings.json'), jl('b612_record_lines.json')
    w, fa, ra = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R222) ratified.** (1) b611 at its weight, the grading rule, the verdicts and the tier confirmed. (2) The seat’s four findings '
             'about the Phase 1.2 papers entered as fact items, the REGISTRY row-addition for the author’s word. (3) The synthesis for 1.5E; '
             'H46a-H46d. (4) The act after: b613.', '',
             '**Entered:** FINDINGS.md:%d (b611’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (three fact items, addressed '
             'to b611’s record :12603), :%d (the REGISTRY row-addition item); this record; PLACE-papers `%s`; relay data/%s.' % (
                 w, fj['entry_line'], fa, ra, DOC, BANK), '',
             '**Resolved by the seat, for the author’s strike:** CONSTANCE synthesised as the census row and REGISTRY’s 1.5E section list it, its '
             'reclassification noted; a pin resolves when its commit is in the clone and at the remote; the dirichlet-mod-24 row graded '
             'argument-supported, its isomorphism not a declaration; the routes and their verdicts, six listed for the sieve’s next version; the '
             'tier read from the rows, KC. No prompt was put (relay data/b612_author_answers.txt).', '',
             '**For the author:** %s.' % FOR_AUTHOR, '',
             '**b613 priced** (the sequence’s form: each act prices the next): the census row R12, 2B, six papers, 1,856 lines -- '
             'phase2/philosophy/SILENCE_EMERGENCE.md, DARK_INTERFACE.md, COGNITION.md, UNIFIED_COGNITIVE.md, '
             'INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md and phase2/method/IDENTITY_SUBSPACE.md -- read whole at address; one act, '
             'no Lean call; the tier read from the rows; the no-disclosure arm bears, DARK_INTERFACE.md naming TECHNE once.', '',
             '**Defects** (relay data/b612_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R222)`(4), b613, the synthesis act for 2B; the author rules on the closing.', '',
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
    put_json('b612_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b612_trail.json')['line'])


def desk(*a):
    S = jl('b612_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b612 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H46a-H46d, (R222)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H46 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
        sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b612_defects.txt').rstrip(NL).split(NL)
    put_txt('b612_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b612_scores.json'), jl('b612_findings.json'), jl('b612_trail.json'), jl('b612_record_lines.json')
    Z, X = jl('b612_page_zeta.json'), jl('b612_page_chi.json')
    L = ['b612 -- THE COMPONENTS, BANKED UNDER (R222).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b611`s closing push-out relay %s ; push-b611* branches deleted by name '
         '(data/b612_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b612_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b611`s weight FINDINGS :%d ; three fact items OPEN_TRAILS :%d ; the REGISTRY row-addition item :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the claim bank data/%s ; H46d %s' % (BANK, S['H46d'][0]),
         '### COMPONENT 3 : the document %s ; data/b612_doc_bank.txt ; H46a %s, H46b %s, H46c %s' % (DOC, S['H46a'][0], S['H46b'][0], S['H46c'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b612_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b613 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b612_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b612_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
