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


# ================================================================================ COMPONENT 3: THE LEGACY MAP, (R259)(3)
# ### W-ORD-LEGACY-MAP: on each branch sorry-quarantine-<kernel>, a README.md listing every quarantined declaration -- its file and line at
# ### the quarantine commit (the branch's tip, the main b648 quarantined from), its statement, the date it entered main, and its successor in
# ### the built kernel by file and line, or "no successor; superseded by" with the reason -- from b648's classification bank; committed alone
# ### on the branch; its rows counted against the quarantined declarations. A successor is named only where the line it cites is in a
# ### lean_lib of the kernel's main and carries the declaration named (checked here).
SUCCESSOR = {
    'schwarz_discharge': ('Kernel/SchwarzDischarge.lean', 42, 'schwarz_reflection_completedZeta₀'),
    'schwarz_v2': ('Kernel/SchwarzDischarge.lean', 42, 'schwarz_reflection_completedZeta₀'),
    'schwarz_v3': ('Kernel/SchwarzDischarge.lean', 42, 'schwarz_reflection_completedZeta₀'),
    'schwarz_v4': ('Kernel/SchwarzDischarge.lean', 42, 'schwarz_reflection_completedZeta₀'),
    'schwarz_v5': ('Kernel/SchwarzDischarge.lean', 42, 'schwarz_reflection_completedZeta₀'),
    'product_formula_prime_pow': ('Kernel/ProductFormula_Clean.lean', 86, 'product_formula_prime_pow')}
SUPERSEDED = {
    'focus_on_critical_line': 'legacy/SchwarzReflection_PR.lean :129 (completedRiemannZeta₀_im_eq_zero_on_half), itself outside every lean_lib',
    ('SIDE-lv-conservation', '(example)'): 'SIDELvConservation/T3_StepNineBridge.lean :108, the goal it reproduced, the theorem b648 RESTATED as a '
                                           'Prop on branch b648-restate-SIDE-lv-conservation'}


def _legacy_rows(k):
    import no_sorry_main as NSM
    lines = [r for r in (jl('b648_sorry_classification.json').get('rows') or []) if r['kernel'] == k and r.get('proposed') == 'QUARANTINED']
    # ### b648's bank holds one row per `sorry` LINE; a declaration closing two (SchwarzBuild2's schwarz_discharge :87, at :111 and :113) is
    # ### one declaration of the map, its sorry lines named
    rows, seen = [], {}
    for r in lines:
        key = (r['file'], r['decl_line'])
        if key in seen:
            seen[key]['sorry_lines'].append(r['line'])
            continue
        seen[key] = dict(r, sorry_lines=[r['line']])
        rows.append(seen[key])
    p = 'D:/' + k
    main = g(p, 'rev-parse', 'main').strip()
    files = [x for x in g(p, 'ls-tree', '-r', '--name-only', main).split(NL) if x.strip()]
    read = lambda f: _show(p, main, f)   # noqa: E731
    built = set(NSM.lib_files(files, read, (read('lakefile.lean') or '') + NL + (read('lakefile.toml') or '')))
    out = []
    for r in rows:
        nm = r['decl'] if r['decl'] != '(example)' else None
        s = SUCCESSOR.get(nm)
        if s:
            line = (read(s[0]) or '').split(NL)[s[1] - 1] if read(s[0]) else ''
            if s[0] not in built or s[2] not in line:
                sys.exit('### THE SUCCESSOR %s :%d (%s) IS NOT A BUILT LINE CARRYING ITS NAME -- NOTHING WRITTEN' % s)
            succ = '`%s` :%d `%s`' % s
        else:
            sup = SUPERSEDED.get(nm) or SUPERSEDED.get((k, r['decl']))
            succ = 'no successor; superseded by %s' % (sup if sup else 'nothing -- %s' % r['reason'].replace('`', '’'))
        out.append(dict(file=r['file'], line=r['decl_line'], kind=r['decl_kind'], decl=r['decl'], sorry_lines=r['sorry_lines'],
                        statement=' '.join((r.get('statement') or '').split(':=')[0].split()).replace('|', '¦').replace('`', "'"),
                        entered=r['entered'], successor=succ))
    return out, main


def legacy_map(kernel, *a):
    """the README.md on sorry-quarantine-<kernel>, committed alone on the branch; data/b649_legacy_map_<kernel>.txt. Refuses unless the kernel
    is on main with a clean tracked tree and the branch's README is absent; returns to main."""
    p = 'D:/' + kernel
    qb = 'sorry-quarantine-' + kernel
    if g(p, 'branch', '--show-current').strip() != 'main' or g(p, 'status', '--porcelain', '--untracked-files=no').strip():
        sys.exit('### %s IS NOT ON A CLEAN main -- NOTHING WRITTEN' % kernel)
    tip = g(p, 'rev-parse', qb).strip()
    if not tip or g(p, 'rev-parse', '%s~1' % qb).strip() and g(p, 'log', '-1', '--format=%s', qb).startswith('b649'):
        sys.exit('### THE BRANCH %s IS ABSENT OR ITS LEGACY MAP IS WRITTEN ALREADY -- NOTHING WRITTEN' % qb)
    # ### the branch is a whole snapshot of the main it was made at, the kernel's own README.md among its files: the legacy map takes the
    # ### name the ruling gives, and the kernel's README stays whole at the tip's commit and on main, the map's first lines naming both
    old_readme = _show(p, tip, 'README.md')
    old_blob = g(p, 'rev-parse', '%s:README.md' % tip).strip() if old_readme is not None else None
    rows, main = _legacy_rows(kernel)
    for r in rows:
        src = (_show(p, tip, r['file']) or '').split(NL)
        if r['line'] > len(src) or (r['decl'] != '(example)' and r['decl'].split('.')[-1] not in src[r['line'] - 1]):
            sys.exit('### %s :%d DOES NOT CARRY %s AT THE BRANCH`S TIP -- NOTHING WRITTEN' % (r['file'], r['line'], r['decl']))
    R = ['# The legacy map of %s' % qb, '',
         'This branch holds, as they stood, the declarations that b648 quarantined from `main` under the author’s ruling (R258)(2): each was '
         'closed by `sorry` and entered `main` before the standing rule that no `sorry` reaches any `main` (relay OPEN_TRAILS :11508). The branch’s '
         'tip, `%s`, is the commit of `main` they were quarantined from; `main` (`%s` when this map was written) no longer carries them, and the '
         'kernel’s `ERRATA.md` on `main` names each. Each row gives the declaration’s file and line at the tip, its statement, the date it entered '
         '`main`, and its successor in the built kernel -- the declaration in a lean_lib of `main` proving the same content, by file and line -- '
         'or “no successor; superseded by” with the reason. Written by relay b649 under (R259)(3) from relay `data/b648_sorry_classification.json`.'
         % (tip[:7], main[:7]), '',
         ('The kernel’s own `README.md`, which this map replaces on this branch alone, stands whole at the tip `%s` (blob `%s`) and on `main`.'
          % (tip[:7], (old_blob or '')[:12])) if old_blob else 'The tip `%s` carries no `README.md` of its own.' % tip[:7], '',
         '| # | file :line (at `%s`) | kind | declaration | its `sorry` | statement | entered main | successor |' % tip[:7],
         '|:--|:--|:--|:--|:--|:--|:--|:--|']
    R += ['| %d | `%s` :%d | %s | `%s` | %s | `%s` | %s | %s |' % (i, r['file'], r['line'], r['kind'], r['decl'], ', '.join(':%d' % x for x in r['sorry_lines']),
                                                             r['statement'][:240], r['entered'], r['successor'])
          for i, r in enumerate(rows, 1)]
    R += ['', '%d quarantined declarations (%d `sorry` lines); %d with a successor in the built kernel.' % (
        len(rows), sum(len(r['sorry_lines']) for r in rows), sum(1 for r in rows if not r['successor'].startswith('no '))), '']
    body = (NL.join(R)).encode('utf-8')
    L = ['b649 -- COMPONENT 3, (R259)(3): THE LEGACY MAP ON %s (%s)' % (qb, utc()), '',
         '### the branch`s tip %s (the main b648 quarantined from) ; main now %s ; the rows from relay data/b648_sorry_classification.json' % (
             tip[:12], main[:12])]
    if DRY:
        put_txt('b649_legacy_map_%s.txt' % kernel, L + ['', '### THE README (dry):'] + R)
        print(NL.join(R[:12]))
        return
    g(p, 'checkout', '-q', qb)
    try:
        open(os.path.join(p, 'README.md'), 'wb').write(body + NL.encode())
        g(p, 'add', 'README.md')
        g(p, 'commit', '-q', '-m', 'b649 under (R259)(3), W-ORD-LEGACY-MAP: README.md -- the %d declarations quarantined from main at b648, each with its file '
                                   'and line at %s, its statement, the date it entered main and its successor in the built kernel or none; committed '
                                   'alone on this branch.' % (len(rows), tip[:7]))
        new = g(p, 'rev-parse', 'HEAD').strip()
        files = [x for x in g(p, 'show', '--name-only', '--pretty=format:', new).split(NL) if x.strip()]
    finally:
        g(p, 'checkout', '-q', 'main')
    n_rows = len(re.findall(r'^\| \d+ \|', (_show(p, new, 'README.md') or ''), re.M))
    qrows = [r for r in (jl('b648_sorry_classification.json').get('rows') or []) if r['kernel'] == kernel and r.get('proposed') == 'QUARANTINED']
    want = len(set((r['file'], r['decl_line']) for r in qrows))
    L += ['### the README committed alone on the branch: %s, files %s ; back on %s' % (new[:12], files, g(p, 'branch', '--show-current').strip()),
          '### ### **README ROWS %d ; QUARANTINED DECLARATIONS %d (b648`s sorry lines %d) ; EQUAL %s.**' % (n_rows, want, len(qrows), n_rows == want),
          '', '### THE README, WHOLE:'] + R
    put_txt('b649_legacy_map_%s.txt' % kernel, L)
    put_json('b649_legacy_map_%s.json' % kernel, dict(at=utc(), kernel=kernel, branch=qb, tip=tip, commit=new, files=files, rows=n_rows,
                                                      quarantined=want, sorry_lines=len(qrows), equal=n_rows == want, main=main))
    print(L[-len(R) - 3])


# ================================================================================ COMPONENT 4: THE LV BUILD MEASURED, (R259)(4)
# ### W-ORD-LV-BUILD-HOST priced from a measurement: every module of SIDE-lv-conservation's lean_lib, one per call, under the tree-aware
# ### watchdog (tools/build_watch.py, the hold 2560 MB, a stop beneath it tried once more). Every module had a built .olean at main, so a
# ### `lake build` of it would compile nothing: each is measured by `lake env lean <its file>`, the elaboration a rebuild pays for that
# ### module against its built imports. Read from relay data/b649_build_peaks.json (every attempt) and the watchdog's logs (the free memory
# ### at each start). A module stopped beneath the hold has a lower bound for its need, never a value: its tree peak at the stop.
LV_ORDER = ('Genus5', 'Genus5Confinement', 'TwoSidesIdentity', 'AxiomCheck_D2', 'FieldLayer', 'LeadLaw', 'SaltCheck_LeadLaw', 'AxiomCheck_LeadLaw',
            'T1_MellinFactorization', 'T2_SDarkness', 'T3_StepNineBridge', 'GammaBounds', 'C7OrderBounds', 'CouplingsAtPhi', 'RegisterPentagon',
            'ZeroCarrier', 'PartialPositivity', 'C7FiniteTypeFalse', 'AxiomCheck_v0_10_0', 'ZeroActingPairing', 'QWantedPoster',
            'CompositionBarrier', 'DirichletC7Order', 'Smoke', 'ZeroActingPartial')


def lv_build(*a):
    """data/b649_lv_build.txt and .json: per module its attempts (start free, seconds, tree peak, host low, exit), its outcome and its price."""
    pk = [r for r in (jl('b649_build_peaks.json').get('rows') or []) if (r.get('module') or '').startswith('SIDELvConservation.')]
    p = 'D:/SIDE-lv-conservation'
    main = g(p, 'rev-parse', '--short=7', 'main').strip()
    rows = []
    for m in LV_ORDER:
        at = [r for r in pk if r['module'] == 'SIDELvConservation.' + m]
        log = io.open(at[0]['log'], encoding='utf-8', errors='replace').read() if at else ''
        starts = [int(x) for x in re.findall(r'^### START attempt \d+ \S+ free (\d+) MB', log, re.M)]
        done = [r for r in at if r.get('rc') == 0 and not r.get('stopped')]
        peak = max([r.get('tree_peak') or 0 for r in at] or [0])
        imports = re.findall(r'^\s*import\s+(\S+)', _show(p, main, 'SIDELvConservation/%s.lean' % m) or '', re.M)
        rows.append(dict(module=m, attempts=[dict(start_free=(starts[i] if i < len(starts) else None), seconds=r['seconds'], tree_peak=r['tree_peak'],
                                                 host_low=r['host_low'], rc=r['rc'], stopped=r['stopped']) for i, r in enumerate(at)],
                         outcome='COMPLETED' if done else 'RUN-BENEATH-HOLD', peak=peak, need=K.HOLD + peak, bound='=' if done else '>=',
                         mathlib=[x for x in imports if x.startswith('Mathlib')], imports=len(imports)))
    beneath = [r for r in rows if r['outcome'] == 'RUN-BENEATH-HOLD']
    starts = [x['start_free'] for r in rows for x in r['attempts'] if x['start_free']]
    smoke = next(r for r in rows if r['module'] == 'Smoke')
    gamma = next(r for r in rows if r['module'] == 'GammaBounds')
    L = ['b649 -- COMPONENT 4, (R259)(4): THE LV-CONSERVATION BUILD MEASURED, MODULE BY MODULE (%s)' % utc(), '',
         '### SIDE-lv-conservation main %s ; its lean_lib SIDELvConservation, 25 modules in import order ; each by `lake env lean <file>` under '
         'tools/build_watch.py (the hold %d MB; a stop beneath it tried once more), one per call, detached and watched from the foreground ; '
         'every module had a built .olean, so `lake build` would have compiled nothing' % (main, K.HOLD), '',
         '### module | outcome | attempts: free at start / seconds / tree peak / host low / exit | the free memory it needs at start (hold + tree peak)']
    for r in rows:
        L.append('  %-22s %-16s %s | needs %s %d MB' % (r['module'], r['outcome'], ' ; '.join(
            '%s/%ds/%dMB/%dMB/%s' % (x['start_free'] or '?', x['seconds'], x['tree_peak'], x['host_low'], ('stopped' if x['stopped'] else 'exit %d' % x['rc']))
            for x in r['attempts']), r['bound'], r['need']))
    L += ['', '### THE MODULES THAT CANNOT COMPLETE UNDER THE HOLD (%d), each with its tree peak at the stop (a lower bound of its need):' % len(beneath)]
    L += ['  %-22s tree peak >= %d MB ; needs >= %d MB free at start ; imports %d (Mathlib: %s)' % (
        r['module'], r['peak'], r['need'], r['imports'], ', '.join(r['mathlib'][:3]) + (' ...' if len(r['mathlib']) > 3 else '')) for r in beneath]
    allat = [x for r in rows for x in r['attempts'] if x['stopped']]
    fast = [x for x in allat if x['seconds'] <= 45]
    slow = ['%s %d s' % (r['module'], x['seconds']) for r in rows for x in r['attempts'] if x['stopped'] and x['seconds'] > 45]
    zap = next(r for r in rows if r['module'] == 'ZeroActingPartial')
    zdone = [x for x in zap['attempts'] if x['rc'] == 0 and not x['stopped']]
    L += ['', '### THE READING, from the bank:',
          '  - of %d stopped attempts, %d reached the hold within 45 s, while lean was still mapping its imports (the slower: %s): the peak at '
          'the stop is the import`s cost, not a module`s own elaboration -- Smoke, %d lines importing two Mathlib modules and declaring nothing of '
          'weight, reached %d MB, above GammaBounds` %d MB;' % (len(allat), len(fast), ', '.join(slow) or 'none',
                                                               len((_show(p, main, 'SIDELvConservation/Smoke.lean') or '').split(NL)), smoke['peak'], gamma['peak']),
          '  - the peaks climb from the first module to the last as the operating system`s file cache warms (%d MB at the first, %d MB at the '
          'last stopped), so a later module`s peak is no larger a need than an earlier one`s;' % (rows[0]['peak'], beneath[-1]['peak'] if beneath else 0),
          '  - ZeroActingPartial %s;' % (('completed on attempt %d, its elaboration ending before the first sample (exit 0, %d s, host low %d MB)'
                                          % (zap['attempts'].index(zdone[0]) + 1, zdone[0]['seconds'], zdone[0]['host_low'])) if zdone else 'did not complete'),
          '  - the free memory at a start ranged %d-%d MB ; the hold is %d MB.' % (min(starts), max(starts), K.HOLD), '',
          '### THE PRICE: the host would need about %d MB free at a module`s start (the hold plus the largest tree peak measured, %d MB), against '
          'the %d-%d MB this host offered; the peak is the Mathlib import`s and not GammaBounds` own, so a split of GammaBounds.lean at :177 does not '
          'answer it. No hold changed, no kernel edited.' % (K.HOLD + max(r['peak'] for r in rows), max(r['peak'] for r in rows), min(starts), max(starts)),
          '', '### ### **MODULES 25 ; COMPLETED %d ; BENEATH THE HOLD %d ; LARGEST TREE PEAK %d MB ; NEED ABOUT %d MB FREE AT START.**' % (
              25 - len(beneath), len(beneath), max(r['peak'] for r in rows), K.HOLD + max(r['peak'] for r in rows))]
    put_txt('b649_lv_build.txt', L)
    put_json('b649_lv_build.json', dict(at=utc(), main=main, hold=K.HOLD, rows=rows))
    print(L[-1])


# ================================================================================ COMPONENTS 5 AND 6: THE NAME AND THE DESCRIPTION AT v5
# ### v5's composer: b647's compose_v4 (its edits a-d, over b646's sealed compose_v3) with (R259)'s edits applied after, each anchored once:
# ###   (e) THE NAME, (R259)(5): the opening mention of the open statement in the glossary's words, "the positivity clause (h2_sign: ...)",
# ###       every later mention "the positivity clause"; the bare phrase "the clause" leaves the text (v4's one, a premise's discharge clause,
# ###       reads "this entry");
# ###   (f) THE RESIDUE, (R259)(6): the glossary's entries "act" and "the constant 1" applied where v4 used the terms unexplained.
V5_EDITS = ('e', 'f')
BARE = re.compile(r'\bthe clause\b', re.I)
E_ANCHORS = (('and the open clause being the sign statement h2_sign itself', 'and %s being the sign statement itself'),
             ('is the open clause in its attribution face', 'is the positivity clause in its attribution face'),
             ("h2, the programme's name for the open clause", "h2, the programme's name for the positivity clause"),
             ('[the clause differs because', '[this entry differs because'))


def compose_v5(edits=V5_EDITS):
    """v5's HTML: b647's compose_v4 with (R259)'s edits named in `edits` applied in the order e, f."""
    import b647_record as B7
    import chain_page as CP
    h = B7.compose_v4()
    if 'e' in edits:
        m = CP.positivity_mention()
        for i, (o, n) in enumerate(E_ANCHORS):
            h = B7._once(h, o, n % m if '%s' in n else n, 'e%d, the name' % (i + 1))
    if 'f' in edits:
        h = _residue(h)
    return h


F_ACT = "which an act takes up on the author's word"


def act_gloss(gl):
    return gl['act'].replace("the relay's work", "the programme's work").rstrip('.')
F_ONE = "witnessed in the kernel at the constant 1 (trivialSummandPremise'_witness)"


def _residue(h):
    """(f): the glossary's entries for the two terms b647's residue marked (relay data/b647_desc_residue.txt (4), (5)) placed beside them,
    in the glossary's words read at composition."""
    import b647_record as B7
    gl = B7._gl4()
    if 'act' not in gl or 'the constant 1' not in gl:
        return h + ' NOT READ (f: the glossary lacks an entry)'
    # ### the description names no repository of the programme (b644's forbidden-content rule reads "relay" as a bank path): the entry's
    # ### "the relay's work" is rendered "the programme's work" here, the glossary keeping the ruling's words
    h = B7._once(h, F_ACT, "which an act -- %s -- takes up on the author's word" % act_gloss(gl), 'f1, act')
    one = gl['the constant 1'].replace("of TrivialSummandPremise': ", '')
    h = B7._once(h, F_ONE, "witnessed in the kernel at the constant 1, %s (trivialSummandPremise'_witness)" % one.rstrip('.'), 'f2, the constant 1')
    return h


LIST_HEAD = ['# b649 -- (R259)(5), THE NAME: b648`s list (relay data/%s), every line unchanged, with the one line `# positivity clause`',
             '# appended, by which the generator titles the page by the positivity clause and carries the opening mention in the glossary`s',
             '# words in its head line (relay tools/chain_page.py, `node_positivity`). A list without that line emits exactly as before.', '#']
NODES = {'zeta': 'b649_nodes_zeta.txt', 'chi': 'b649_nodes_chi.txt'}
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}


def lists(*a):
    """data/b649_nodes_zeta.txt and data/b649_nodes_chi.txt: b648's lists, byte for byte, beneath a four-line head and above the one line."""
    for k, old in (('zeta', 'b648_nodes_zeta.txt'), ('chi', 'b648_nodes_chi.txt')):
        body = rd(old).rstrip(NL).split(NL)
        L = [x % old if '%s' in x else x for x in LIST_HEAD] + body + ['#', '# positivity clause']
        put_txt(NODES[k], L)
        print('%s: %d lines, b648`s %d unchanged beneath the head' % (NODES[k], len(L), len(body)))


def page_arms(tag='', *a):
    """data/b649_page_arms[_<tag>].txt: the page arms on b649's marked lists against PLACE-papers HEAD and the frozen control with the E0
    rule at its relay pin (b648's page_arms, carried)."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    import chain_page as CP
    import b626_record as R26
    L = ['b649 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s, relay %s (%s)%s' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc(), (' -- ' + tag) if tag else '')]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b649_gcp'), os.path.join(D, PROBE[k]))
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
    put_txt('b649_page_arms%s.txt' % (('_' + tag) if tag else ''), L)
    print(NL.join(l[:220] for l in L))


V4 = 'b647_deposit_description.txt'
V5 = 'b649_deposit_description.txt'


def v4_same(*a):
    """b647's composer at this act against v4 as banked: byte for byte."""
    import b647_record as B7
    h, v4 = B7.compose_v4(), rd(V4)
    print('  compose_v4 at this act %d bytes ; v4 as banked %d bytes ; the same: %s' % (len(h.encode('utf-8')), len(v4.encode('utf-8')), h == v4))
    return h == v4


def describe5(*a):
    """data/b649_deposit_description.txt (v5) and .json beside v4: composed from banks, b644's sealed `forbidden` run over it, the five parts in
    order, every tag Zenodo accepts, no bare "the clause"; refuses on any hit, unread figure or part out of order."""
    import hashlib
    import b646_record as B6
    R4 = B6._R4()
    if not v4_same():
        sys.exit('### b647`S COMPOSER DOES NOT REPRODUCE v4 -- NOTHING COMPOSED')
    html = compose_v5()
    heads = re.findall(r'<p><strong>(.*?)</strong></p>', html)
    order_ok = heads == [x.rstrip('.') for x in B6.PART_HEADS]
    hits = R4.forbidden(html)
    unread = [m.group(0) for m in re.finditer(r'NOT READ|NOT BANKED|not in the table|None', html)]
    bad = sorted(set(re.findall(r'</?([a-zA-Z0-9]+)', html)) - B6._allowed_tags())
    bare = BARE.findall(html)
    print('  parts %d, in order %s ; forbidden hits %d ; unread %d ; tags outside Zenodo`s %s ; bare "the clause" %d ; bytes %d' % (
        len(heads), order_ok, len(hits), len(unread), bad or 'none', len(bare), len(html.encode('utf-8'))))
    for x in hits + [('unread', u) for u in unread]:
        print('    ### %s : %s' % x)
    if DRY:
        _write(os.path.join(SP, 'b649_deposit_description_dry.txt'), html.encode('utf-8'))
        return
    if hits or unread or not order_ok or bad or bare:
        sys.exit('### A FORBIDDEN CONTENT, AN UNREAD FIGURE, A TAG, THE BARE PHRASE OR THE PARTS OUT OF ORDER -- NOTHING WRITTEN')
    b = html.encode('utf-8')
    _write(os.path.join(D, V5), b)
    put_json('b649_deposit_description.json', dict(at=utc(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), heads=heads, edits=list(V5_EDITS),
                                                   order_ok=order_ok, forbidden=hits, v4_bytes=len(rd(V4).encode('utf-8'))))
    print('  written: data/%s %d bytes, sha256 %s' % (V5, len(b), hashlib.sha256(b).hexdigest()[:16]))


def desc_diff5(*a):
    """data/b649_desc_diff.txt: v4 against v5 by part -- each part's bytes, the tokens lost and added (b644's sealed `invariance`), and each
    edit's text before and after as the composer applies it."""
    import b646_record as B6
    import chain_page as CP
    import b647_record as B7
    R4 = B6._R4()
    v4, v5 = rd(V4), rd(V5)
    if not v5:
        sys.exit('### v5 IS NOT BANKED -- RUN `describe5` FIRST')
    p4, p5 = dict(B6._parts_of(v4)), dict(B6._parts_of(v5))
    b4, b5 = len(v4.encode('utf-8')), len(v5.encode('utf-8'))
    L = ['b649 -- COMPONENT 6, (R259)(6): THE DESCRIPTION, v4 AGAINST v5, BY PART (%s)' % utc(), '',
         '### v4: relay data/%s, %d bytes ; v5: relay data/%s, %d bytes ; the change %+d bytes' % (V4, b4, V5, b5, b5 - b4), '']
    for h in B6.PART_HEADS:
        a_, b_ = p4.get(h, ''), p5.get(h, '')
        lost, added = R4.invariance('<p>%s</p>' % a_, '<p>%s</p>' % b_)
        L += ['### %s v4 %d bytes ; v5 %d bytes ; %+d' % (h, len(a_.encode('utf-8')), len(b_.encode('utf-8')), len(b_.encode('utf-8')) - len(a_.encode('utf-8'))),
              '    tokens lost: %s' % (sorted(lost.items()) or 'none'), '    tokens added: %s' % (sorted(added.items()) or 'none')]
    m = CP.positivity_mention()
    gl = B7._gl4()
    L += ['', '### THE EDITS, EACH AS APPLIED (before -> after):']
    for i, (o, n) in enumerate(E_ANCHORS, 1):
        L += ['  (e%d) the name' % i, '      v4: ' + o, '      v5: ' + (n % m if '%s' in n else n)]
    L += ['  (f1) act', '      v4: ' + F_ACT, "      v5: which an act -- %s -- takes up on the author's word" % act_gloss(gl),
          "      (the glossary's entry reads \"%s\"; \"the relay's work\" rendered \"the programme's work\", the description naming no "
          "repository)" % gl['act'],
          '  (f2) the constant 1', '      v4: ' + F_ONE,
          "      v5: witnessed in the kernel at the constant 1, %s (trivialSummandPremise'_witness)" % gl['the constant 1'].replace("of TrivialSummandPremise': ", '').rstrip('.')]
    L += ['', '### ### **v4 %d BYTES ; v5 %d BYTES ; %+d ; THE BARE PHRASE "the clause" IN v4 %d, IN v5 %d.**' % (
        b4, b5, b5 - b4, len(BARE.findall(v4)), len(BARE.findall(v5)))]
    put_txt('b649_desc_diff.txt', L)
    print(L[-1])


def desc_test5(*a):
    """data/b649_desc_test.txt: the forbidden-content test rerun (b644's sealed `forbidden`) by b646's planted cases with v5 as banked in v4's
    place, each case counted; the composer's edit tests (tools/test_composer_b649.py) and the name's test (tools/test_name_b649.py) run beside."""
    import b646_record as B6
    R4 = B6._R4()
    cases = [('an act number', '<p>composed at b643.</p>', 'an act number'),
             ('a bank path', '<p>read from data/b643_premise_table.json.</p>', 'a bank path'),
             ('root arithmetic', '<p>root e583d138ea28f97569fe859a5826996bda1cebe83fac102cf9821b6a1b2c3d4.</p>', 'root arithmetic'),
             ('a provenance count', '<p>the rows are 209 cell and 1707 rule.</p>', 'a provenance count'),
             ('an outside collection', '<p>read beside %s.</p>' % (R4.OUTSIDE_NEEDLES[0] if R4.OUTSIDE_NEEDLES else 'X'), 'an outside collection'),
             ('a banned stem', '<p>a ' + 'ga' + 'p remains.</p>', 'a banned stem'),
             ('the unsupported sentence asserted', '<p>The programme shows that RH is proved.</p>', 'the unsupported sentence asserted'),
             ('the ceiling denied (no hit)', '<p>Not supported: that RH is proved; the corpus does not claim it.</p>', None),
             ('v5 as banked (no hit)', rd(V5), None)]
    L = ['b649 -- COMPONENT 6: THE DESCRIPTION`S FORBIDDEN-CONTENT TEST, RERUN BY PLANTED TEXT, AND THE COMPOSER`S TESTS (%s)' % utc(), '']
    n = 0
    for label, text, want in cases:
        hits = R4.forbidden(text)
        kinds = sorted(set(k for k, _x in hits))
        ok = (want in kinds) if want else not hits
        n += ok
        L.append('  %-42s hits %s ; %s' % (label, kinds or 'none', 'PASS' if ok else '### FAIL'))
    outs = []
    for t in ('test_composer_b649.py', 'test_name_b649.py'):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', t)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                           env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        outs.append((t, r.returncode, [x for x in (r.stdout or '').split(NL) if x.strip() and not x.startswith('chain_page')]))
    L += ['', '### THE FORBIDDEN-CONTENT TEST: %d of %d cases as wanted -- %s' % (n, len(cases), 'PASS' if n == len(cases) else 'FAIL')]
    for t, rc, lines in outs:
        L += ['', '### %s, exit %d:' % (t, rc)] + ['  ' + x for x in lines]
    L += ['', '### ### **FORBIDDEN-CONTENT %d of %d ; %s.**' % (n, len(cases), ' ; '.join('%s EXIT %d' % (t, rc) for t, rc, _l in outs))]
    put_txt('b649_desc_test.txt', L)
    print(NL.join(L[-3:]))


# ### THE SIXTH READER, (R259)(6): b647's form carried (b646's lead, task and command builders, the directory C:\reader_b649); v5 as text; the
# ### three questions of (R254)(8); run by the author on the author's PowerShell from a directory with no project memory, by the one-line
# ### command banked whole; scored by the hand reading first (data/b649_reader_handread.txt), then by b644's needles.
READER9 = 'C:/reader_b649'


def _b6r9():
    import b646_record as B6
    B6.READER = dict(B6.READER, dir=READER9)
    return B6


def reader_packet9(*a):
    """data/b649_reader_packet.txt, data/b649_reader_command.txt (the one line) and data/b649_reader_packet/: v5 as text with the three
    questions, staged at C:\\reader_b649 (refused if it exists and is not empty), the no-disclosure arm and the outside names checked."""
    import b616_record as R6
    B6 = _b6r9()
    R4 = B6._R4()
    r = B6.READER
    doc = B6._v3_text(rd(V5))
    if not doc.strip():
        sys.exit('### v5 IS EMPTY -- NOTHING WRITTEN')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(r['questions']))
    task = B6._reader_task()
    nd = R6.nd_hits(doc + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in R4.OUTSIDE_NEEDLES if n in doc]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b649_reader_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in ((r['doc'], doc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    if not DRY:
        if os.path.exists(r['dir']) and os.listdir(r['dir']):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- NOT WRITTEN' % r['dir'])
        os.makedirs(r['dir'] + '/packet', exist_ok=True)
        for n_, t_ in (('packet/' + r['doc'], doc), ('packet/questions.txt', qs), ('lead.txt', B6._reader_lead()), ('full_prompt.txt', task)):
            _write(os.path.join(r['dir'], n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    cmd = 'Set-Location %s; %s' % (r['dir'].replace('/', '\\'), B6._reader_cmd())
    L = ['b649 -- THE SIXTH READER`S PACKET, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/%s %d bytes, sha256 %s ; packet/questions.txt ; lead.txt ; full_prompt.txt) ; banked: relay data/b649_reader_packet/' % (
             r['dir'], r['doc'], len(doc.encode('utf-8')), sha(doc.encode('utf-8'))),
         '### the document: v5 (relay data/%s) as text -- a part`s head as == HEAD ==, a list item as a line marked -' % V5,
         '### the questions, (R254)(8)`s three: %s' % ' / '.join(r['questions']),
         '### the no-disclosure arm: %s ; outside names: %s' % (dict(nd), outside or 'NONE'),
         '', '### the command, run by the author on the author`s PowerShell, one line moving to %s, a directory with no project memory (banked alone '
         'at relay data/b649_reader_command.txt):' % r['dir'], '    ' + cmd]
    put_txt('b649_reader_packet.txt', L)
    put_txt('b649_reader_command.txt', [cmd])
    print(NL.join(L[2:]))


def reader_score9(*a):
    """data/b649_reader_answers.txt, data/b649_reader_compare.txt and .json: the sixth reader's answers copied from off D:\\, each scored by
    b644's needles (imported) and beside it the seat's hand reading (data/b649_reader_handread.txt, written first); refuses without it."""
    B6 = _b6r9()
    R4 = B6._R4()
    r = B6.READER
    src = os.path.join(r['dir'], 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    hr = rd('b649_reader_handread.txt')
    if not re.search(r'^HAND \d: (AGREE|DIFFER)', hr, re.M):
        sys.exit('### THE HAND READING IS NOT BANKED -- THE NEEDLES ARE NOT READ BEFORE IT')
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b649_reader_answers.txt'), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in re.finditer(r'^ANSWER (\d):\s*(.*?)(?=^ANSWER \d:|^UNCLEAR:|\Z)', t, re.M | re.S))
    N = R4._needles('d')
    lg = os.path.join(r['dir'], 'reader_run.log')
    lb = open(lg, 'rb').read() if os.path.exists(lg) else None
    lt = lb.decode('utf-16') if lb and lb[:2] in (b'\xff\xfe', b'\xfe\xff') else (lb.decode('utf-8', 'replace') if lb else '')
    ctl = bool(re.search(r'MEMORY\.md', 'x MEMORY.md y'.encode('utf-16').decode('utf-16')))
    mem = ('memory named in the run log: %s (read as %s, %d chars; the planted control fires: %s)' % (
        bool(re.search(r'MEMORY\.md|[\\/]memory[\\/]', lt)), 'UTF-16' if lb[:2] in (b'\xff\xfe', b'\xfe\xff') else 'UTF-8', len(lt), ctl)
           if lb else 'the run log absent')
    hand = dict((int(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^HAND (\d): (AGREE|DIFFER)', hr, re.M))
    L = ['b649 -- THE SIXTH READER: ANSWERS SCORED BY THE NEEDLES AND BY HAND (%s)' % utc(), '',
         '### the answers: relay data/b649_reader_answers.txt, copied from %s ; the reader`s session: %s' % (src, mem),
         '### the hand reading: relay data/b649_reader_handread.txt, banked before the needles were read', '']
    res, n_ok = {}, 0
    for q in sorted(N):
        a_ = ans.get(q, '')
        p1, l1, p2, l2, deny = N[q]
        m1 = bool(re.search(p1, a_, re.I))
        m2 = bool(re.search(p2, a_)) if p2 else True
        asserted = deny(a_) if deny else []
        ok = m1 and m2 and not asserted
        n_ok += ok
        why = ['%s %s' % (l1, m1)] + (['%s %s' % (l2, m2)] if p2 else []) + (['the unsupported sentence asserted %s' % (asserted or 'no')] if deny else [])
        res[q] = dict(question=r['questions'][q - 1], answer=a_, needle=ok, why=why, hand=hand.get(q))
        L += ['### QUESTION %d: %s' % (q, r['questions'][q - 1]), '    the reader: %s' % (a_ or '### NO ANSWER'),
              '    the needles: %s ; ### %s' % ('; '.join(why), 'AGREE' if ok else 'DIFFER'), '    by hand: %s' % (hand.get(q) or '### NOT READ'), '']
    kh = sum(1 for v in hand.values() if v == 'AGREE')
    unclear = re.search(r'^UNCLEAR:\s*(.*)\Z', t, re.M | re.S)
    L += ['### NOTE, beside the score: %s' % n_ for n_ in re.findall(r'^NOTE: (.*)$', hr, re.M)]
    L += ['### UNCLEAR, the reader`s: %s' % (' '.join(unclear.group(1).split())[:1500] if unclear else '### NONE GIVEN'), '',
          '### ### **BY THE NEEDLES %d OF %d ; BY HAND %d OF %d.**' % (n_ok, len(N), kh, len(N))]
    put_txt('b649_reader_compare.txt', L)
    put_json('b649_reader_compare.json', dict(at=utc(), answers=res, needles=n_ok, hand=kh, of=len(N),
                                              unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ### THE DRAFT'S DESCRIPTION, (R259)(6): b647's route (z_desc4 / z_read4 / z_hold4) carried with v5's bank -- b639's http, the token in the
# ### Authorization header alone, the User-Agent naming no person; the draft's description replaced by v5, every other metadata key carried, no
# ### file touched, publish never called; read back once; HELD. Runs after the sixth reader's scoring and the residue.
ZRES = 'b649_zenodo.json'


def _zmerge(cells):
    R = jl(ZRES) if os.path.exists(os.path.join(D, ZRES)) else {}
    R.update(cells)
    put_json(ZRES, R)


def z_desc5(*a):
    """data/b649_zenodo_desc.txt: draft K.DRAFT read once (unsubmitted, or nothing done) and its metadata PUT once with v5's bank, every other
    key carried; the prior description's bytes and digest banked, not its text; the file list banked for the read-back. Runs once."""
    import hashlib
    import b639_record as R39
    import b646_record as B6
    if not R39._tok():
        sys.exit('### THE TOKEN IS NOT SET -- NO CALL MADE')
    if os.path.exists(os.path.join(D, ZRES)) and jl(ZRES).get('desc'):
        sys.exit('### THE DESCRIPTION HAS BEEN REPLACED -- IT DOES NOT RUN TWICE')
    if not os.path.exists(os.path.join(D, 'b649_reader_compare.txt')) or not os.path.exists(os.path.join(D, 'b649_desc_residue.txt')):
        sys.exit('### THE SIXTH READER IS NOT SCORED OR THE RESIDUE NOT BANKED -- THE DESCRIPTION IS NOT REPLACED BEFORE THEM')
    v5 = open(os.path.join(D, V5), 'rb').read().decode('utf-8')
    base = 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT
    st, b = R39.http('GET', base)
    d = B6._jx(b) or {}
    if st != 200 or d.get('submitted') or str(d.get('id')) != K.DRAFT:
        sys.exit('### THE DRAFT IS NOT AN UNSUBMITTED %s (HTTP %d) -- NOTHING DONE' % (K.DRAFT, st))
    md = dict(d.get('metadata') or {})
    old = md.get('description') or ''
    files = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    md['description'] = v5
    sp, bp = R39.http('PUT', base, body={'metadata': md})
    hx = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()   # noqa: E731
    v4 = rd(V4)
    L = ['b649 -- THE ROUTE, THE DRAFT`S DESCRIPTION REPLACED BY v5 (%s)' % utc(), '',
         '### GET the draft %s : HTTP %d ; state %s ; submitted %s ; %d files' % (K.DRAFT, st, d.get('state'), d.get('submitted'), len(files)),
         '### the description before : %d bytes, sha256 %s ; v4`s bank %d bytes, sha256 %s ; the draft held v4: %s' % (
             len(old.encode('utf-8')), hx(old), len(v4.encode('utf-8')), hx(v4), old == v4 or B6._straight(old) == B6._straight(v4)),
         '### PUT metadata (the description v5`s bank, %d bytes, sha256 %s ; %d keys carried) : HTTP %d' % (len(v5.encode('utf-8')), hx(v5), len(md), sp),
         '', '### ### **CALLS 2 ; THE PUT %s ; NO FILE TOUCHED ; NOTHING PUBLISHED.**' % ('ACCEPTED' if sp in (200, 201) else '### REFUSED HTTP %d' % sp)]
    put_txt('b649_zenodo_desc.txt', L)
    _zmerge(dict(desc=dict(get=st, put=sp, before_bytes=len(old.encode('utf-8')), before_sha256=hx(old), v5_sha256=hx(v5), files_before=files,
                           at=utc())))
    print(NL.join(L[2:]))


def z_read5(*a):
    """data/b649_zenodo_read.txt: the draft read back once -- the description against v5's bank byte for byte, digest for digest and up to quote
    straightening; the file list against the one z_desc5 banked."""
    import hashlib
    import b639_record as R39
    import b646_record as B6
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    d = B6._jx(b) or {}
    md = d.get('metadata') or {}
    bank = open(os.path.join(D, V5), 'rb').read().decode('utf-8')
    back = md.get('description') or ''
    exact = back == bank
    dig = hashlib.sha256(back.encode('utf-8')).hexdigest() == hashlib.sha256(bank.encode('utf-8')).hexdigest()
    fb = (jl(ZRES).get('desc') or {}).get('files_before') or []
    fa = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    key = lambda x: sorted((f['name'], f['checksum'], f['size']) for f in x)   # noqa: E731
    files_same = bool(fb) and key(fa) == key(fb)
    L = ['b649 -- THE ROUTE, THE DRAFT READ BACK AFTER THE DESCRIPTION`S REPLACEMENT (%s)' % utc(), '',
         '### GET the draft : HTTP %d ; identifier %s ; state %s ; submitted %s ; title %s ; version %s' % (
             st, d.get('id'), d.get('state'), d.get('submitted'), md.get('title'), md.get('version')),
         '### the description : %d characters back against the bank`s %d ; byte for byte %s ; digest for digest %s ; equal up to quote straightening %s' % (
             len(back), len(bank), exact, dig, B6._straight(back) == B6._straight(bank)),
         '### the files : %d back against %d before the PUT ; name, checksum and size the same %s' % (len(fa), len(fb), files_same), '',
         '### ### **THE DESCRIPTION BYTE FOR BYTE %s AND DIGEST FOR DIGEST %s ; THE FILES UNTOUCHED %s ; THE DRAFT %s SUBMITTED %s -- NOTHING '
         'PUBLISHED.**' % (exact, dig, files_same, d.get('id'), d.get('submitted'))]
    put_txt('b649_zenodo_read.txt', L)
    _zmerge(dict(read=dict(get=st, id=d.get('id'), state=d.get('state'), submitted=d.get('submitted'), exact=exact, digest=dig,
                           straight=B6._straight(back) == B6._straight(bank), files_same=files_same, n_files=len(fa), at=utc())))
    print(NL.join(L[2:]))


def z_hold5(*a):
    """data/b649_zenodo_hold.txt: the draft HELD, (R259)(6): its state read once and banked; publish is the author's word, no part of this act."""
    import b639_record as R39
    import b646_record as B6
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    d = B6._jx(b) or {}
    L = ['b649 -- THE DRAFT HELD, (R259)(6) (%s)' % utc(), '', '### the draft %s : HTTP %d ; state %s ; submitted %s ; nothing published; v5 sent to '
         'the author as a file (relay data/%s)' % (K.DRAFT, st, d.get('state'), d.get('submitted'), V5)]
    put_txt('b649_zenodo_hold.txt', L)
    _zmerge(dict(hold=dict(id=K.DRAFT, state=d.get('state'), submitted=d.get('submitted'), at=utc())))
    print(L[-1])


BH_LINE = 13798          # ### OPEN_TRAILS: W-ORD-LV-BUILD-HOST opened by Component 1
PR_HEAD = ('*Appended 2026-10-11 by b649 to W-ORD-LV-BUILD-HOST (:%d), under `(R259)`(4) -- ITS PRICE, WRITTEN FROM THE MEASUREMENT:*')


def lv_price(*a):
    """Component 4: OPEN_TRAILS, the price of W-ORD-LV-BUILD-HOST from relay data/b649_lv_build.json, beneath its opening line."""
    import b641_record as R41
    Q = R2._Q()
    if 'W-ORD-LV-BUILD-HOST, OPENED' not in lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), ''))[BH_LINE - 1]:
        sys.exit('### W-ORD-LV-BUILD-HOST`S LINE MOVED -- NOTHING WRITTEN')
    j = jl('b649_lv_build.json')
    rows = j.get('rows') or []
    if len(rows) != 25:
        sys.exit('### THE BUILD BANK DOES NOT READ 25 MODULES -- NOTHING WRITTEN')
    ben = [r for r in rows if r['outcome'] == 'RUN-BENEATH-HOLD']
    peak = max(r['peak'] for r in rows)
    starts = [x['start_free'] for r in rows for x in r['attempts'] if x['start_free']]
    smoke = next(r for r in rows if r['module'] == 'Smoke')
    gamma = next(r for r in rows if r['module'] == 'GammaBounds')
    t = ('\n%s the 25 modules of SIDE-lv-conservation`s lean_lib at main %s, each by `lake env lean` under the tree-aware watchdog, one per call '
         '(relay data/b649_lv_build.txt): %d beneath the hold of %d MB on both attempts, %d completed; the largest tree peak %d MB; the free memory '
         'at a start %d-%d MB. The peak is the Mathlib import`s -- Smoke, which declares nothing of weight, reached %d MB against the %d MB of '
         'GammaBounds -- so a split of GammaBounds.lean at :177 does not answer it. THE PRICE: a host offering about %d MB free at a module`s start, the '
         'hold plus the largest peak; this host offered %d-%d MB. No hold changed and no kernel edited; the h2 docstring edit waits on a host '
         'at that price.\n' % (PR_HEAD % BH_LINE, j.get('main'), len(ben), j.get('hold'), 25 - len(ben), peak, min(starts), max(starts),
                                smoke['peak'], gamma['peak'], j.get('hold') + peak, min(starts), max(starts)))
    t = R41._poss(t)
    nd, _n = R3._nd(t)
    p = os.path.join(SP if DRY else D, 'b649_scanfile_price.md')
    _write(p, t.encode('utf-8'))
    sc = _scan(p)
    ticks = [l[:60] for l in t.split(NL) if l.count('`') % 2]
    print('  table cells %s ; nd %s ; scanner %s ; odd backticks %s' % (R3.predict_cells(t, 'OPEN_TRAILS.md') or 'NONE', nd,
                                                                       'CLEAN' if _clean(sc) else 'NOT CLEAN', ticks or 'NONE'))
    if DRY:
        print(t)
        return
    if R3.predict_cells(t, 'OPEN_TRAILS.md') or any(nd.values()) or not _clean(sc) or ticks:
        sys.exit('### NOTHING WRITTEN')
    R3._land(Q, [('OPEN_TRAILS.md', PR_HEAD % BH_LINE, t)], 'b649_price_line.json', BH_LINE)


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b649_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
