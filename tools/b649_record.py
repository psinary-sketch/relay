# -*- coding: utf-8 -*-
"""b649_record.py -- THE ACT'S RECORD TOOL, UNDER (R259). ### ONE SUBCOMMAND PER BANK.

### ### b649: LANE THREE, ACT SEVENTY-SIX -- THREE ARMS (NO SORRY ON MAIN, AXIOM CLAIMS AGAINST PRINTS, MODULE HEADERS AGAINST FILES); THE
### LEGACY MAP; THE LV-CONSERVATION BUILD MEASURED; THE POSITIVITY CLAUSE NAMED; THE DESCRIPTION AT v5; THE DRAFT HELD. Subcommands write
### only `data/b649_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers are b602's, b633's
### and b641's record tools', imported; ledger appends through b566's guarded `append_to`. Written by the Write tool, edited through the Edit
### tool only. Every bank is LF. Every string this tool puts in a ledger is dry-run through the ledger guards before the seal (b647 (o)).
"""
import collections
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b649_worklist as K  # noqa: E402
import edit_route as ER  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, DATE = K.PRE_PP, K.PRE_RELAY, K.DATE
SP = K.SP
SESSION_ID = K.SESSION_ID
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
SESSIONS_AFTER = ()   # ### a continuation session after a /clear is named here, with its first user line, before any capture is banked
FACE = 'b649_registration_2026-10-11.txt'
DRY = 'dry' in sys.argv[2:]
R3.DRY = DRY
os.makedirs(SP, exist_ok=True)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of = R3.lines_of
STD3 = '[propext, Classical.choice, Quot.sound]'


def put_txt(name, L):
    _write(os.path.join(SP if DRY else D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(SP if DRY else D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


# ================================================================================ COMPONENT 0: STEP ZERO
def procs(*a):
    """data/b649_procs.txt: the process listing -- tail, lean, lake and python named, each with its parent and command line -- and the free
    memory; orphans stopped by PID with their command lines printed (none expected)."""
    ps = ("Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(tail|lean|lake|python|python3)(\\.exe)?$' } | ForEach-Object { "
          "$par = Get-CimInstance Win32_Process -Filter (\"ProcessId=\" + $_.ParentProcessId); "
          "\"{0}`t{1}`t{2}`t{3}`t{4}\" -f $_.ProcessId, $_.ParentProcessId, ($(if ($par) {'parent alive'} else {'ORPHAN'})), $_.Name, $_.CommandLine }; "
          "'FREE ' + [int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
    out = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    me = os.getpid()
    rows = [l for l in out.split(NL) if l.strip() and not l.startswith('FREE ') and not l.startswith('%d\t' % me)]
    free = re.search(r'^FREE (\d+)', out, re.M)
    orph = [l for l in rows if '\tORPHAN\t' in l]
    stopped = []
    for l in orph:
        pid = l.split('\t')[0]
        r = subprocess.run(['taskkill', '/T', '/F', '/PID', pid], capture_output=True, text=True)
        stopped.append('  stopped pid %s (taskkill exit %d): %s' % (pid, r.returncode, l[:400]))
    L = ['b649 -- COMPONENT 0: THE PROCESS LISTING AT STEP ZERO, tail, lean, lake AND python NAMED (%s)' % utc(), '',
         '### pid / parent / parent state / name / command line (this tool`s own python process left out, pid %d)' % me]
    L += ['  ' + l[:400] for l in rows] or ['  ### NONE: no tail, lean, lake or python process is running']
    L += ['', '### orphans: %s ; stopped by PID: %s' % (len(orph) if orph else 'NONE', 'none needed' if not stopped else len(stopped))] + stopped
    L += ['### free memory: %s MB ; the hold %d MB' % (free.group(1) if free else '?', K.HOLD)]
    put_txt('b649_procs.txt', L)
    print(NL.join(L[3:]))


def stepzero(*a):
    """data/b649_stepzero.txt: the branch deletions read back (relay and PLACE-papers, push-b648* listed by --merged and deleted by name in the
    commands the capture holds), the untracked banks by git status and git log, the free memory before any build."""
    import build_watch as BW
    lines = []
    for repo, name in ((RELAY, 'relay'), (PP, 'PLACE-papers')):
        lines.append('  %-13s push-b648* branches now: %s' % (name, g(repo, 'branch', '--list', 'push-b648*').strip() or 'NONE'))
    for p in (K.LOCAL_BANK, K.EXPORT):
        st = g(RELAY, 'status', '--porcelain', '--', p).strip()
        lg = g(RELAY, 'log', '--all', '--format=%h', '--', p).strip()
        idx = g(RELAY, 'ls-files', '--', p).strip()
        lines.append('  %-42s status %s ; in a commit %s ; in the index %s' % (p, st or '(clean)', lg or 'NONE', idx or 'NO'))
    L = ['b649 -- COMPONENT 0: THE BRANCHES, THE UNTRACKED BANKS AND THE FREE MEMORY AT STEP ZERO (%s)' % utc(), '',
         '### the b648 push branches, listed by `git branch --merged main` and deleted by name with the lower-case flag (relay push-b648, '
         'push-b648-closing, push-b648-root; PLACE-papers push-b648, push-b648-root), read back:'] + lines[:2] + [
        '', '### the banks that stay untracked (b628`s local intake bank; the navigator`s export):'] + lines[2:] + [
        '', '### free memory before any build: %d MB ; the hold %d MB' % (BW.free_mb(), K.HOLD)]
    put_txt('b649_stepzero.txt', L)
    print(NL.join(L[2:]))


def answers(*a):
    """data/b649_author_answers.txt: every prompt put by the seat in this act, from the ruling's delivery (and any continuation session from its
    first user line), banked verbatim with the options, their previews, the recommended mark and the answer."""
    def scan(path, anchor):
        calls, results, start = [], {}, None
        for i, raw in enumerate(io.open(path, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anchor in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and start is not None:
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
        return start, calls, results
    srcs = [(SESSION_ID, SESSION, K.ANCHOR)] + [(sid, 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc) for sid, anc in SESSIONS_AFTER]
    L, n = [], 0
    for sid, path, anc in srcs:
        start, calls, results = scan(path, anc)
        if start is None:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))
        for i, cid, inp in calls:
            L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, sid, i))
            for k, q in enumerate(inp.get('questions', []), 1):
                n += 1
                L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
                for j, op in enumerate(q.get('options', []), 1):
                    L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                         op.get('description')))
                    if op.get('preview'):
                        L += ['    PREVIEW | ' + x for x in op['preview'].split(NL)]
            r = results.get(cid, (None, '### NO RESULT'))
            L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    head = ['### b649 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; the sessions read: %s.' % (n, DATE, ', '.join('%s from %r' % (s[:8], an) for s, _, an in srcs)), '']
    put_txt('b649_author_answers.txt', head + (L or ['### NONE: no prompt has been put to the author in this act.']))
    print('  prompts banked: %d' % n)


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in SESSIONS_AFTER:
        rows += ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc, 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def commands(*a):
    """data/b649_commands.txt and .json: the act's command bank -- every Bash and PowerShell command of the seat's session from the ruling's
    delivery (K.ANCHOR) onward and its helper readers' -- each with the arm G-EDIT-ROUTE's reading (tools/edit_route.py)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % K.ANCHOR)
    hits = ER.scan(rows)
    L = ['b649 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING ((R256)(2); tools/edit_route.py) (%s)' % utc(), '',
         '### the source: the seat`s session transcript %s from its first user line carrying %r, and its subagents` transcripts at or after it' % (
             os.path.basename(SESSION), K.ANCHOR),
         '### commands read: %d (seat %d ; helper readers %d)' % (len(rows), sum(1 for r in rows if r['src'].startswith('seat')),
                                                                  sum(1 for r in rows if not r['src'].startswith('seat'))), '',
         '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d.**' % (len(rows), len(hits))]
    put_txt('b649_commands.txt', L)
    put_json('b649_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R259)(1), (3), (4)
B648_ENTRY = 8151        # ### FINDINGS: b648's entry
B648_CORR = 13770        # ### OPEN_TRAILS: the correction beneath b648's sorry breach (the quarantines and the arm G-NO-SORRY-MAIN)
B648_TRAIL = 13772       # ### OPEN_TRAILS: b648's trail record (the re-cut order's answer, W-ORD-LV-BUILD-HOST named in its note)
W_HEAD = '*Appended 2026-10-11 by b649 to b648’s entry (:%d), under `(R259)`(1) -- b648 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
LM_HEAD = ('*Appended 2026-10-11 by b649 to the correction beneath the sorry breach (:%d), under `(R259)`(3) -- W-ORD-LEGACY-MAP, ENTERED AND '
           'ACTED BY THIS ACT:*')
BH_HEAD = ('*Appended 2026-10-11 by b649 to b648’s record (:%d), under `(R259)`(4) -- W-ORD-LV-BUILD-HOST, OPENED, ITS TRIGGER THE h2 '
           'DOCSTRING EDIT:*')


def _need(pat, text, what):
    m = re.search(pat, text, re.M)
    if not m:
        sys.exit('### %s NOT FOUND -- NOTHING WRITTEN' % what)
    return m


def _weight():
    c = rd('b648_closing.txt')
    h = _need(r'^b648 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts? answered; (\d+) defects', c,
              'b648`s closing head line')
    cl = jl('b648_sorry_classification.json')
    rows = cl.get('rows') or []
    cc = collections.Counter(r.get('proposed') for r in rows)
    before = sum(1 for r in rows if (r.get('entered') or '9999') < '2026-09-29')
    unl = cl.get('unlicensed') or []
    tp, ta = jl('b648_table_pages.json').get('rows') or [], jl('b648_table_pages_after.json').get('rows') or []
    c0, c1 = collections.Counter(r['verdict'] for r in tp), collections.Counter(r['verdict'] for r in ta)
    kc = jl('b648_kernel_cites.json').get('rows') or []
    cmp_ = jl('b648_reader_compare.json')
    ro = jl('b648_recut_order.json').get('rows') or []
    sc = jl('b648_scores.json')
    closing = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b648 closing', PRE_RELAY).strip()[:8]
    seal = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b648 seal', PRE_RELAY).strip()[:8]
    if (len(rows), cc.get('QUARANTINED'), cc.get('RESTATED'), len(tp), len(ta), len(kc), len(ro)) != (37, 33, 4, 1261, 1267, 20, 33):
        sys.exit('### b648`S BANKS DO NOT READ AS EXPECTED -- NOTHING WRITTEN')
    sco = ', '.join('%s %s' % (k, (sc.get(k) or ['?'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5'))
    return ('\n%s relay %s (act), %s (seal), %s (closing), PLACE-papers %s; the suite %s of %s, NOT CLEAN on G-EDIT-ROUTE and G-NO-SORRY-MAIN, '
            'both declared on the face; the root %s…; %s prompts answered; %s defects, (a) to (i), and a note beside them. The 37 `sorry` lines '
            'classified on the author`s word: QUARANTINED %d, RESTATED %d, PROVED %d, each with its entry date, %d of them before the rule`s '
            'line at OPEN_TRAILS :11508; the quarantine branches sorry-quarantine-SIDE-kernel and sorry-quarantine-SIDE-lv-conservation pushed, '
            'each kernel`s ERRATA.md naming the quarantined declarations; the four RESTATED Props on local branches, unmerged, their builds '
            'beneath the hold; the citing sentences UNLICENSED, %d. The two pages through the table, %d rows before -- MATCHES %d, UNDERSTATES '
            '%d, OVERREACHES %d, UNLICENSED %d -- and %d after three template repairs and re-emission at the new glossary -- MATCHES %d, '
            'OVERREACHES %d, UNLICENSED %d. The census at v0.8 with cluster, phase and maturity over 77 rows; of the 20 kernels the rules leave '
            'unplaced, %d placed by the keystones naming them, %d split, %d named by none; the second reader %s of 2 by hand. The h2 row banked. '
            'The re-cut order raised over %d documents and the author`s answer banked. %s. Read at b649`s step zero: the two pages regenerate one '
            'Placement row longer since the census at v0.8 (PLACE-papers f66d23d) names nodes of the chain, a commit made after the pages were '
            're-emitted and their arms read; the arms test_chain_page.py (1), (14) and test_g_chain_page.py (1) fail on that row, and this act`s '
            're-emission carries it. Nothing deposited; the draft held at v4.\n' % (
                W_HEAD % B648_ENTRY, h.group(1), seal, closing, h.group(2), h.group(3), h.group(4), h.group(5)[:8], h.group(6), h.group(7),
                cc.get('QUARANTINED', 0), cc.get('RESTATED', 0), cc.get('PROVED', 0), before, len(unl), len(tp), c0['MATCHES'], c0['UNDERSTATES'],
                c0['OVERREACHES'], c0['UNLICENSED'], len(ta), c1['MATCHES'], c1['OVERREACHES'], c1['UNLICENSED'],
                sum(1 for r in kc if r['cluster']), sum(1 for r in kc if r['how'].startswith('split')),
                sum(1 for r in kc if r['how'] == 'named by no keystone'), cmp_.get('hand'), len(ro), sco))


def _legacy_map_line():
    q = collections.Counter(r['kernel'] for r in (jl('b648_sorry_classification.json').get('rows') or []) if r.get('proposed') == 'QUARANTINED')
    return ('\n%s on each branch sorry-quarantine-<kernel> a README.md in the house form lists every declaration the quarantine took off main '
            '-- its file and line at the quarantine commit, its statement, the date it entered main, and its successor, the declaration in the '
            'built kernel proving the same content by file and line from b648`s classification bank (relay data/b648_sorry_classification.json), '
            'or "no successor; superseded by" with the reason -- committed alone on the branch; its rows counted against the quarantined '
            'declarations (%s), an arm of the suite reading the equality. Acted at this act`s Component 3, its bank relay data/b649_legacy_map.txt.\n'
            % (LM_HEAD % B648_CORR, '; '.join('%s %d' % kv for kv in sorted(q.items()))))


def _build_host_line():
    return ('\n%s every module of SIDE-lv-conservation built one per call under the tree-aware watchdog (relay tools/build_watch.py), each '
            'module`s tree peak and the host`s low banked (relay data/b649_lv_build.txt); the modules that cannot complete under the hold, 2560 MB, '
            'listed with their peaks; the price written as the host memory each would need, or a split of GammaBounds.lean at :177 where the peak '
            'is that module`s own. No hold change and no kernel edit. Trigger: the h2 docstring edit -- the row W-ORD-LV-H2-DOCSTRING of b648 '
            '(relay data/b648_h2_row.txt), which `(R259)`(4) names W-ORD-H2-DOCSTRING -- waits on this bank. Opened at this act; its price written '
            'from the bank at Component 4.\n' % (BH_HEAD % B648_TRAIL))


def record_lines(*a):
    """Component 1, (R259)(1), (3), (4): FINDINGS, b648 at its weight (to :8151); OPEN_TRAILS, W-ORD-LEGACY-MAP entered and acted (to :13770)
    and W-ORD-LV-BUILD-HOST opened (to :13772)."""
    import b641_record as R41
    Q = R2._Q()
    if not (Q.line_of(Q.FIND, '## The sorry lines on kernel mains: 37 classified') == B648_ENTRY):
        sys.exit('### b648`S ENTRY MOVED -- NOTHING WRITTEN')
    ot = lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), ''))
    if 'A CORRECTION, BY THE AUTHOR' not in ot[B648_CORR - 1] or not ot[B648_TRAIL - 1].startswith('### b648 —'):
        sys.exit('### b648`S TRAIL LINES MOVED -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % B648_ENTRY, R41._poss(_weight())), ('OPEN_TRAILS.md', LM_HEAD % B648_CORR, R41._poss(_legacy_map_line())),
             ('OPEN_TRAILS.md', BH_HEAD % B648_TRAIL, R41._poss(_build_host_line()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if DRY else D, 'b649_scanfile_lines.md')
    _write(p, allt.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    ticks = [l[:60] for l in allt.split(NL) if l.count('`') % 2]
    unread = [x for x in ('### NOT', 'None', ' ? ') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread or outside:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS, AN UNREAD FIGURE OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    R3._land(Q, items, 'b649_record_lines.json', B648_ENTRY)


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b649_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
