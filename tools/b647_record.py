# -*- coding: utf-8 -*-
"""b647_record.py -- THE ACT'S RECORD TOOL, UNDER (R257). ### ONE SUBCOMMAND PER BANK.

### ### b647: LANE THREE, ACT SEVENTY-FOUR -- EVERY KERNEL'S DOCSTRINGS THROUGH THE LICENSED-STATEMENT TABLE; THE NAVIGATOR'S MEMORY THROUGH
### THE TABLE; THE DESCRIPTION AT v4 WITH ITS GLOSSARY ENTRIES, A FIFTH READER, THE DRAFT HELD; THE WATCHDOG ON THE PROCESS TREE; THE CENSUS
### COLUMNS EXTENDED. Subcommands write only `data/b647_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad.
### The generic helpers are b602's, b633's and b641's record tools', imported; b646's composer, reader and route imported where carried;
### ledger appends through b566's guarded `append_to`. Written by the Write tool, edited through the Edit tool only. Every bank is LF.
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
import b647_worklist as K  # noqa: E402
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
FACE = 'b647_registration_2026-10-10.txt'
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
    """data/b647_procs.txt: the process listing -- tail, lean, lake and python named, each with its parent and command line -- and the free
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
    L = ['b647 -- COMPONENT 0: THE PROCESS LISTING AT STEP ZERO, tail, lean, lake AND python NAMED (%s)' % utc(), '',
         '### pid / parent / parent state / name / command line (this tool`s own python process left out, pid %d)' % me]
    L += ['  ' + l[:400] for l in rows] or ['  ### NONE: no tail, lean, lake or python process is running']
    L += ['', '### orphans: %s ; stopped by PID: %s' % (len(orph) if orph else 'NONE', 'none needed' if not stopped else len(stopped))] + stopped
    L += ['### free memory: %s MB ; the hold %d MB' % (free.group(1) if free else '?', K.HOLD)]
    put_txt('b647_procs.txt', L)
    print(NL.join(L[3:]))


def stepzero(*a):
    """data/b647_stepzero.txt: the branch deletions read back (relay and PLACE-papers, push-b646* listed by --merged and deleted by name in the
    commands the capture holds), the two untracked banks by git status and git log, the free memory before any build."""
    import build_watch as BW
    lines = []
    for repo, name in ((RELAY, 'relay'), (PP, 'PLACE-papers')):
        lines.append('  %-13s push-b646* branches now: %s' % (name, g(repo, 'branch', '--list', 'push-b646*').strip() or 'NONE'))
    for p in (K.LOCAL_BANK, K.EXPORT):
        st = g(RELAY, 'status', '--porcelain', '--', p).strip()
        lg = g(RELAY, 'log', '--all', '--format=%h', '--', p).strip()
        idx = g(RELAY, 'ls-files', '--', p).strip()
        lines.append('  %-42s status %s ; in a commit %s ; in the index %s' % (p, st or '(clean)', lg or 'NONE', idx or 'NO'))
    import hashlib
    eb = open(os.path.join(ROOT, *K.EXPORT.split('/')), 'rb').read()
    L = ['b647 -- COMPONENT 0: THE BRANCHES, THE UNTRACKED BANKS AND THE FREE MEMORY AT STEP ZERO (%s)' % utc(), '',
         '### the b646 push branches, listed by `git branch --merged main` and deleted by name with the lower-case flag (relay push-b646, '
         'push-b646-closing, push-b646-root; PLACE-papers push-b646, push-b646-root), read back:'] + lines[:2] + [
        '', '### the two banks that stay untracked (b628`s local intake bank; the navigator`s export, b647`s input, %d bytes, sha256 %s):' % (
            len(eb), hashlib.sha256(eb).hexdigest())] + lines[2:] + [
        '', '### free memory before any build: %d MB ; the hold %d MB' % (BW.free_mb(), K.HOLD)]
    put_txt('b647_stepzero.txt', L)
    print(NL.join(L[2:]))


def answers(*a):
    """data/b647_author_answers.txt: every prompt put by the seat in this act, from the ruling's delivery (and any continuation session from its
    first user line), banked verbatim with the options, the recommended mark and the answer."""
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
            r = results.get(cid, (None, '### NO RESULT'))
            L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    head = ['### b647 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; the sessions read: %s.' % (n, DATE, ', '.join('%s from %r' % (s[:8], an) for s, _, an in srcs)), '']
    put_txt('b647_author_answers.txt', head + (L or ['### NONE: no prompt has been put to the author in this act.']))
    print('  prompts banked: %d' % n)


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in SESSIONS_AFTER:
        rows += ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc, 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def commands(*a):
    """data/b647_commands.txt and .json: the act's command bank -- every Bash and PowerShell command of the seat's session from the ruling's
    delivery (K.ANCHOR) onward and its helper readers' -- each with the arm G-EDIT-ROUTE's reading (tools/edit_route.py)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % K.ANCHOR)
    hits = ER.scan(rows)
    L = ['b647 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING ((R256)(2); tools/edit_route.py) (%s)' % utc(), '',
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
    put_txt('b647_commands.txt', L)
    put_json('b647_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R257)(1), (5)
B646_ENTRY = 8095        # ### FINDINGS: b646's entry
FOOTPRINT_LINE = 13631   # ### OPEN_TRAILS: W-ORD-HOLD-FOOTPRINT entered and priced at b645
W_HEAD = '*Appended 2026-10-10 by b647 to b646’s entry (:%d), under `(R257)`(1) -- b646 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
HF_HEAD = '*Appended 2026-10-10 by b647 to W-ORD-HOLD-FOOTPRINT (:%d), under `(R257)`(5) -- ACTED:*'


def _need(pat, text, what):
    m = re.search(pat, text, re.M)
    if not m:
        sys.exit('### %s NOT FOUND -- NOTHING WRITTEN' % what)
    return m


def _weight():
    c = rd('b646_closing.txt')
    h = _need(r'^b646 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts? answered; (\d+) defects', c,
              'b646`s closing head line')
    cmd = _need(r'\*\*COMMANDS (\d+) ; G-EDIT-ROUTE OFFENCES (\d+)\.\*\*', rd('b646_commands.txt'), 'b646`s command bank')
    names = ('Exhaustive_Enumeration', 'Which_Structure_Confines', 'Spectral_Inertness', 'Seven_Mechanism_Classes', 'Third_Identity_Element',
             'Silence_of_Foundations', 'ONE_PAGE_PROOF')
    cnt, fixed, rows = collections.Counter(), 0, 0
    for n in names:
        j = jl('b646_table_%s.json' % n)
        cnt.update(j.get('counts') or {})
        fixed += sum(1 for r in j.get('rows') or [] if r.get('fixed'))
        rows += len(j.get('rows') or [])
    ag = _need(r'### ### \*\*ROWS (\d+) ; CHAPTERS (\d+)\.\*\*', rd('b645_v6_agenda.txt'), 'the monograph`s agenda')
    mem = jl('b646_table_seat_memory.json')
    mc = mem.get('counts') or {}
    rep = mem.get('repairs') or []
    dj, cp = jl('b646_deposit_description.json'), jl('b646_reader_d4_compare.json')
    sc = jl('b646_scores.json')
    nd = len(re.findall(r'^    \([a-z]\) ', rd('b646_defects.txt'), re.M))
    act = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b646 --', PRE_RELAY).strip()[:8]
    closing = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b646 closing', PRE_RELAY).strip()[:8]
    seal = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b646 seal', PRE_RELAY).strip()[:8]
    if rows != 1008 or [cnt[v] for v in ('MATCHES', 'UNDERSTATES', 'OVERREACHES', 'UNLICENSED')] != [878, 12, 94, 24] or fixed != 27:
        sys.exit('### b646`S COMPANION BANKS DO NOT READ THE RULING`S FIGURES -- NOTHING WRITTEN')
    sco = ', '.join('%s %s' % (k, (sc.get(k) or ['?'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5'))
    return ('\n%s relay %s (closing), %s (act), %s (seal), PLACE-papers %s; the suite %s of %s, NOT CLEAN on G-EDIT-ROUTE alone; the root '
            '%s…; %s prompt answered; %d defects, (a) to (l). The edit-route arm tools/edit_route.py, its planted test 25 of 25, read %s '
            'captured commands and found %s offence -- the seat`s cp of three tools into tools/ (defect (k)), declared on the face before the '
            'lock. The seven companions at %d claims -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d -- every non-MATCHES row read '
            'whole by the seat, %d of the readers’ verdicts corrected with their reasons, a 35-row MATCHES sample agreeing; the re-cut agenda '
            'now %d sentences over eight documents, the monograph`s %s and the companions’ %d. TrivialSummandPremise’ in the E0 rule`s list of '
            'premise structures, dedekind_rhs’ INTERFACES on its two premises, no other grade moved. The description at v3, %s bytes against '
            '%s, the fourth reader %s of 3 by the needles and %s of 3 by hand, the residue six passages, the draft`s description replaced and '
            'read back, held. The seat`s standing memory at %d rows -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d -- %d re-cuts '
            'applied in place and %d sentence retired. The run-log encoding fault (UTF-16 from PowerShell`s redirect) found and repaired with a '
            'planted control. %s; N5 as computed REFUTED, by its predicate`s intent in one clause (defect (l)). `(R257)`(1) read three figures '
            'from a report made before the close -- 0 offences over 1,046 commands, defects (a) to (g), the export saved by the author -- and the '
            'banks print 1 over %s, (a) to (l), and the export written by the seat from the author`s paste (defect (j)): the navigator`s, '
            'the banks’ figures standing. Nothing deposited; no edition touched.\n' % (
                W_HEAD % B646_ENTRY, closing, act, seal, h.group(2), h.group(3), h.group(4), h.group(5)[:8], h.group(6), nd,
                cmd.group(1), cmd.group(2), rows, cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'], fixed,
                int(ag.group(1)) + cnt['OVERREACHES'] + cnt['UNLICENSED'], ag.group(1), cnt['OVERREACHES'] + cnt['UNLICENSED'],
                dj.get('bytes'), dj.get('v2_bytes'), cp.get('needles'), cp.get('hand'), len(mem.get('rows') or []), mc.get('MATCHES', 0),
                mc.get('UNDERSTATES', 0), mc.get('OVERREACHES', 0), mc.get('UNLICENSED', 0),
                sum(1 for x in rep if x['state'] == 'APPLIED'), sum(1 for x in rep if x['state'] == 'RETIRED'), sco, cmd.group(1)))


def _footprint():
    pk = (jl('b647_build_peaks.json').get('rows') or [])
    r = [x for x in pk if x.get('module') == 'test_elab_reader_b634']
    if not r:
        sys.exit('### NO TREE PEAK BANKED -- NOTHING WRITTEN')
    r = r[-1]
    return ('\n%s tools/build_watch.py samples the process tree beneath the driver -- the driver and every descendant, lean and lake among them, '
            'their working sets summed -- beside the driver`s own working set and the host`s free memory, prints the tree`s peak beside the host`s '
            'low on every run`s EXIT line, and banks every attempt`s row (`--peaks`); the hold rule unchanged. Committed alone at b647`s step zero '
            '(relay %s) with its planted test tools/test_build_watch_b647.py: a grandchild holding 400 MB reads a tree peak above the driver`s, a '
            'driver with no child reads the two together, b644`s hold test passes whole. Its first measurement, b647`s step zero: '
            'test_elab_reader_b634 run to its end for the first time since b634 (7 of 7) -- the driver`s peak %d MB, the tree`s %d MB, the '
            'host`s low %d MB, %d s (relay data/b647_build_peaks.json). A later ruling may set the hold on what a run adds.\n' % (
                HF_HEAD % FOOTPRINT_LINE, K.WATCH_COMMIT, r['driver_peak'], r['tree_peak'], r['host_low'], r['seconds']))


def record_lines(*a):
    """Component 1, (R257)(1), (5): FINDINGS, b646 at its weight (to :8095); OPEN_TRAILS, W-ORD-HOLD-FOOTPRINT acted (to :13631)."""
    import b641_record as R41
    Q = R2._Q()
    if not (Q.line_of(Q.FIND, '## The edit-route arm; the seven companions at 1008 claims') == B646_ENTRY):
        sys.exit('### b646`S ENTRY MOVED -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % B646_ENTRY, R41._poss(_weight())), ('OPEN_TRAILS.md', HF_HEAD % FOOTPRINT_LINE, R41._poss(_footprint()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if DRY else D, 'b647_scanfile_lines.md')
    _write(p, allt.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    ticks = [l[:60] for l in allt.split(NL) if l.count('`') % 2]
    unread = [x for x in ('### NOT', 'None', '-1 MB') if x in allt] + re.findall(r'(?:^|[\s(,;])\?', allt, re.M)
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
    R3._land(Q, items, 'b647_record_lines.json', B646_ENTRY)


# ================================================================================ COMPONENT 2: EVERY KERNEL'S DOCSTRINGS, (R257)(2)
# ### The kernels of the chain: every repository holding a row of the terminal table at relay HEAD. SIDE-explicit-formula was read whole at
# ### b645 (relay data/b645_table_docstrings.txt, 1369 rows at v0.26 = 82550e4, its main unmoved since) and is carried into the joined table,
# ### not read again; the other kernels are read here at their main. A kernel with an elaborated bank takes it (SIDE-structural-error-
# ### correction, relay data/b643_elab_sec.txt at v0.2.2 = 6bf19ab, its main); every other kernel takes the textual reader -- the statement
# ### from the table's row or the source's header -- each row marked TEXTUAL. A module RUN-BENEATH-HOLD at b645 (SIDE-global-section
# ### Interfaces/RestrictedTensorLayer1.lean, relay data/b645_hold_preseal.txt) takes no row and is named.
ELAB = {'SIDE-structural-error-correction': 'b643_elab_sec.txt'}
RBH_FILES = {'SIDE-global-section': ['Interfaces/RestrictedTensorLayer1.lean']}
CARRIED = {'SIDE-explicit-formula': 'b645_table_docstrings.json'}


def _tt_rows():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def kernels_of_chain():
    return sorted(set(r['repo'] for r in _tt_rows()))


def _kmain(k):
    return g('D:/' + k, 'rev-parse', '--short=7', 'main').strip()


def _kfiles(k):
    fs = [x for x in g('D:/' + k, 'ls-tree', '-r', '--name-only', 'main').split(NL) if x.endswith('.lean') and not x.startswith('.lake/')]
    return sorted(x for x in fs if x not in RBH_FILES.get(k, []))


def _elab_index(bank):
    idx = {}
    cur, binders, concl = None, [], None
    for l in rd(bank).split(NL):
        if l.startswith('DECL '):
            cur, binders, concl = l.split()[1], [], None
        elif l.startswith('BINDER ') and cur:
            binders.append(l[len('BINDER '):])
        elif l.startswith('CONCL ') and cur:
            concl = l[len('CONCL '):]
        elif l == 'END' and cur:
            hyps = [b.split(' ', 1)[1] for b in binders if b.startswith('explicit ') and re.match(r'^explicit h\w*\s*:', b)]
            idx[cur] = ((' '.join('(%s)' % b.split(' ', 1)[1] for b in binders) + ' ⊢ ' + (concl or '')).strip(), hyps)
            cur = None
    return idx


def _kdoc_rows(k):
    """the generated rows of one kernel at its main: b645's _doc_rows (tools/b645_record.py :863) carried kernel by kernel, the statement
    elaborated where the kernel has a bank and TEXTUAL where it has none."""
    import licensed_table as LT
    import b645_record as R45
    rev = _kmain(k)
    rows = [x for x in _tt_rows() if x['repo'] == k]
    full = dict((x['name'], x) for x in rows)
    last = collections.defaultdict(list)
    for x in rows:
        last[x['name'].split('.')[-1]].append(x)

    def lookup(n):
        x = full.get(n) or (last[n.split('.')[-1]][0] if len(last.get(n.split('.')[-1], [])) == 1 else None)
        return (x['name'], x['grade']) if x else None
    ST = dict((r['head'], r['status']) for r in jl('b643_premise_table.json').get('rows') or [])
    PB = {}
    for x in rows:
        m = re.match(r'^theorem (\S+)\s*:\s*([\w.\'’]+)\s*$', re.sub(r'\s+', ' ', x['statement'] or '').strip())
        if m:
            PB.setdefault(m.group(2).split('.')[-1], '%s : %s (%s, grade %s)' % (x['name'], m.group(2), x['statement_file'], x['grade']))
    proved_by = lambda d: PB.get(d.split('.')[-1])   # noqa: E731
    by_file = collections.defaultdict(dict)
    for x in rows:
        if x.get('statement_file'):
            by_file[x['statement_file']].setdefault(x['name'].split('.')[-1], []).append(x)
    E = _elab_index(ELAB[k]) if k in ELAB else {}
    textual = k not in ELAB
    out = []
    for f in _kfiles(k):
        text = (_show('D:/' + k, rev, f) or '').replace(chr(13), '')
        for kind, ln, doc, kw, name, dl in R45._docstrings(f, text):
            sid = '%s@%s:%s:%d' % (k, rev, f, ln)
            src = '%s:%d' % (f, ln)
            if kind == 'module':
                names = sorted(set(n for n, _s, _e in LT.names_in(doc)))
                hits = [(n, lookup(n)) for n in names]
                summ = '; '.join('%s %s' % (h[0].split('.')[-1], h[1]) for n, h in hits if h) or 'it names no row of the table'
                r = LT.docstring_row(sid, src, doc, None, 'module', summ, None, None, [], lookup, module=True, status=ST.get)
                r.update(kernel=k, rev=rev, file=f, line=ln, kind='module', decl=None, grade=None, textual=textual)
                out.append(r)
                continue
            if kind == 'field':
                ft = re.sub(r'\s+', ' ', NL.join(text.split(NL)[dl - 1:dl + 3]).split('/--')[0]).strip()
                r = LT.docstring_row(sid, src, doc, name, 'field', '%s (a structure field, read at the source, %s :%d)' % (ft, f, dl), 'DEF',
                                     'the field`s type', [], lookup, status=ST.get, proved_by=proved_by)
                r.update(kernel=k, rev=rev, file=f, line=ln, kind='field', decl=name, grade='DEF', decl_line=dl, textual=textual)
                out.append(r)
                continue
            if not name:
                r = LT.docstring_row(sid, src, doc, None, 'module', 'a docstring before no declaration the reader parses', None, None, [],
                                     lookup, module=True, status=ST.get)
                r.update(kernel=k, rev=rev, file=f, line=ln, kind='orphan', decl=None, grade=None, textual=textual)
                out.append(r)
                continue
            cands = by_file.get(f, {}).get(name.split('.')[-1], [])
            x = cands[0] if len(cands) == 1 else None
            hdr = re.sub(r'\s+', ' ', NL.join(text.split(NL)[dl - 1:dl + 14]).split(':=')[0]).strip()
            if x is None:
                g_ = 'DEF' if kw in ('def', 'abbrev', 'structure', 'class', 'inductive', 'instance', 'opaque') else 'UNGRADED'
                st = (E.get(name) or ('%s (read at the source, %s :%d)' % (hdr, f, dl), []))[0]
                r = LT.docstring_row(sid, src, doc, name, kw, st, g_, 'keyword, not in the table', [], lookup, status=ST.get, proved_by=proved_by)
                r.update(kernel=k, rev=rev, file=f, line=ln, kind='decl', decl=name, grade=g_, decl_line=dl, textual=textual or name not in E)
                out.append(r)
                continue
            st, hyps = E.get(x['name'], (re.sub(r'\s+', ' ', x['statement'] or hdr), []))
            r = LT.docstring_row(sid, src, doc, x['name'], kw, st, x['grade'], x['provenance'], hyps, lookup, status=ST.get, proved_by=proved_by)
            r.update(kernel=k, rev=rev, file=f, line=ln, kind='decl', decl=x['name'], grade=x['grade'], decl_line=dl,
                     textual=textual or x['name'] not in E)
            out.append(r)
    return out


def kdocs_yield(*a):
    """the generated rows of every kernel but the carried one, their yields printed and written to the scratchpad (mem: kdocs_<kernel>.json);
    no bank. The flagged rows (non-MATCHES or hand-needed) are the helper readers` and the seat`s."""
    tot = collections.Counter()
    for k in kernels_of_chain():
        if k in CARRIED:
            continue
        rows = _kdoc_rows(k)
        c = collections.Counter(r['verdict'] for r in rows)
        fl = [r for r in rows if r['verdict'] != 'MATCHES' or r.get('hand_needed')]
        tot.update(c)
        tot['FLAGGED'] += len(fl)
        _write(os.path.join(SP, 'kdocs_%s.json' % k), json.dumps(rows, ensure_ascii=False, indent=1).encode('utf-8'))
        print('  %-34s main %s ; files %3d ; rows %4d ; textual %4d ; %s ; flagged %d' % (
            k, _kmain(k), len(_kfiles(k)), len(rows), sum(1 for r in rows if r['textual']), dict(c), len(fl)))
    print('  TOTAL %s' % dict(tot))


WHOLE_SP = os.path.join(SP, 'whole')
_GRH_N1 = 'relay@a66c50a1:data/b555_ferry.txt:123'
KFIX = {        # ### row id -> dict of cells the seat corrects after its whole read (verdict, cls, licensed, cited, action, why)
    'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:1': dict(
        licensed="The file's composite GRHStructuralExhaustiveness has no character, L-function or zero in it: it is card MechanismClass = 7, "
                 "seven exclusions of sigma-conditions on defined real functions, and Ostrowski, with chi, chibar unused; "
                 "grh_structural_exhaustiveness_proved is graded INTERFACES and b555's (N1) reads no character value in its conclusion, so "
                 "\"the composite GRH theorem for L(s, chi)\" and \"the chi-paired form\" claim more than the file compiles.",
        cited='SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:5 ; SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:12 ; '
              'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:65 ; SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:133 ; '
              'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:145 ; relay:data/terminal_table.md:1814 ; ' + _GRH_N1,
        why='the reader cited PLACE-papers FINDINGS.md:5830 with no commit; at 2d6daf3 that line is the GRH_CASCADE tier entry and does not say '
            'character-free; the reading it meant is b555 (N1), relay data/b555_ferry.txt:123'),
    'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:142': dict(
        cited='SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:133 ; SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean:145 ; '
              'relay:data/terminal_table.md:1814 ; ' + _GRH_N1,
        why='the same uncommitted FINDINGS.md:5830 cite, replaced by b555 (N1)'),
    'SIDE-kernel@0256e9e:Kernel/Cascade/SieveCeiling.lean:132': dict(
        licensed='proof_dichotomy is proved by induction and cases, and its banked print reads no axioms (b557 probe c1, the file at v1.4 the '
                 'SAME as at 0256e9e), so "axiom-free" matches its print.',
        cited='SIDE-kernel@0256e9e:Kernel/Cascade/SieveCeiling.lean:134 ; relay@a66c50a1:data/b557_probe_c1.txt:3 ; '
              'relay@a66c50a1:data/b557_probe_c1.txt:13',
        why='the reader wrote "no banked print exists"; the seat\'s class-A control (every axiom claim against the 1420 banked prints) found '
            "proof_dichotomy's print, which agrees: the verdict stands, the ground is corrected"),
}
KREAD_AT = {   # ### file -> lines of its non-MATCHES rows the seat read whole against their cited lines (285 rows)
    'SIDE-archimedean@8019d9d:SIDEArchimedean/Reflection.lean': (1, 58),
    'SIDE-bijection@a26f6f1:SIDEBijection/Theorem.lean': (1, 130, 178, 245),
    'SIDE-carrier-spec@b3916cc:SIDECarrierSpec/ArithContent.lean': (5, 41, 63),
    'SIDE-carrier-spec@b3916cc:SIDECarrierSpec/Grading/DivisorLadder.lean': (55,),
    'SIDE-carrier-spec@b3916cc:SIDECarrierSpec/SaltCheck.lean': (68, 122, 150),
    'SIDE-carrier-spec@b3916cc:SIDECarrierSpec/Spec.lean': (4, 55),
    'SIDE-class-number-anomaly@2203b88:SIDEClassNumberAnomaly/Basic.lean': (102, 105, 147),
    'SIDE-cosmo@c5cba30:SIDECosmo/FanoFormation.lean': (9,),
    'SIDE-cosmo@c5cba30:SIDECosmo/SteaneExemplar.lean': (6, 60, 65, 72, 80),
    'SIDE-effects@ef4cff7:SIDEEffects/ExhaustivenessLicense.lean': (1, 99),
    'SIDE-effects@ef4cff7:SIDEEffects/Milestones.lean': (3, 21, 33, 50, 65),
    'SIDE-global-section@17ce9ff:Core/AlternationShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/BallAbsorptionShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/BallPairShadow.lean': (1, 33),
    'SIDE-global-section@17ce9ff:Core/BoundaryValueShadow.lean': (164,),
    'SIDE-global-section@17ce9ff:Core/CeilingSweepShadow.lean': (1, 104),
    'SIDE-global-section@17ce9ff:Core/CrossPlaceShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/DependenceShadow.lean': (1, 63),
    'SIDE-global-section@17ce9ff:Core/DiagonalSection.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/E1UnitPurityDraft.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/E2EvenMonotoneShadow.lean': (1, 37),
    'SIDE-global-section@17ce9ff:Core/H1Mechanism.lean': (30,),
    'SIDE-global-section@17ce9ff:Core/InequalityShadow.lean': (1, 18),
    'SIDE-global-section@17ce9ff:Core/JunctionSignShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/KLSilence.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/LefschetzShadow.lean': (1, 32, 49, 57, 68),
    'SIDE-global-section@17ce9ff:Core/LinkShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/M4EnvelopeShadow.lean': (66, 85, 91),
    'SIDE-global-section@17ce9ff:Core/MetaplecticRootShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/OrbitDictionary.lean': (54,),
    'SIDE-global-section@17ce9ff:Core/PairingShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/RadializationShadow.lean': (1, 30),
    'SIDE-global-section@17ce9ff:Core/RationalEnclosureShadow.lean': (131,),
    'SIDE-global-section@17ce9ff:Core/SectorArithmetic.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/SinglePrimeFactor.lean': (205, 219),
    'SIDE-global-section@17ce9ff:Core/StatedChoiceShadow.lean': (71,),
    'SIDE-global-section@17ce9ff:Core/TensorSquareShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/ThetaContinuationShadow.lean': (1, 41),
    'SIDE-global-section@17ce9ff:Core/TowerMonotoneShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/TraceSilence.lean': (46,),
    'SIDE-global-section@17ce9ff:Core/TwistedRootShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Core/ValuationDivisibilityShadow.lean': (1,),
    'SIDE-global-section@17ce9ff:Interfaces/FiniteInstanceIdentity.lean': (1,),
    'SIDE-global-section@17ce9ff:Interfaces/LocalLimit.lean': (1, 40, 152, 251, 363),
    'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/CharacterTopological.lean': (1, 51),
    'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/GRHBridge.lean': (1, 142),
    'SIDE-grh-transfer@858cbf6:SIDEGRHTransfer/Voice7Vendored.lean': (1, 58),
    'SIDE-interfaces@cbdcd5f:Interfaces.lean': (1,),
    'SIDE-kernel@0256e9e:Bridge/CartanBBridge.lean': (1, 82, 95, 112, 159, 202, 226),
    'SIDE-kernel@0256e9e:Bridge/ConservationBridge.lean': (9, 31),
    'SIDE-kernel@0256e9e:Bridge/CrossClassExclusion.lean': (4, 31),
    'SIDE-kernel@0256e9e:Bridge/FanoSteane.lean': (4, 46, 66, 123, 137),
    'SIDE-kernel@0256e9e:Bridge/OstrowskiBridge.lean': (3, 29, 52, 92, 101),
    'SIDE-kernel@0256e9e:Bridge/SIDEBridge.lean': (63, 88),
    'SIDE-kernel@0256e9e:Bridge/TheBridgeComplete.lean': (7, 223),
    'SIDE-kernel@0256e9e:Kernel/Cascade/SieveCeiling.lean': (1,),
    'SIDE-kernel@0256e9e:Kernel/Cascade/SieveCeilingBridge.lean': (1,),
    'SIDE-kernel@0256e9e:Kernel/Cascade/SieveCeilingSemantic.lean': (1, 70),
    'SIDE-kernel@0256e9e:Kernel/Core.lean': (42,),
    'SIDE-kernel@0256e9e:Kernel/DistributiveDark.lean': (4, 44),
    'SIDE-kernel@0256e9e:Kernel/Formation.lean': (41,),
    'SIDE-kernel@0256e9e:Kernel/Integration.lean': (104, 120, 143, 181, 191, 200, 215, 248, 263),
    'SIDE-kernel@0256e9e:Kernel/Kappa.lean': (49, 59),
    'SIDE-kernel@0256e9e:Kernel/PerpendicularCrossing.lean': (9, 102),
    'SIDE-kernel@0256e9e:Kernel/PoissonExhaustion.lean': (7, 30, 53),
    'SIDE-kernel@0256e9e:Kernel/ProductFormula_Rat.lean': (68,),
    'SIDE-kernel@0256e9e:Kernel/SilencePrinciple.lean': (1,),
    'SIDE-kernel@0256e9e:Kernel/SilenceTheorem.lean': (108, 116, 121, 127),
    'SIDE-kernel@0256e9e:Kernel/SimplicityRouteD.lean': (69,),
    'SIDE-kernel@0256e9e:Kernel/SimplicityRouteE.lean': (77,),
    'SIDE-kernel@0256e9e:Kernel/StructuralCount.lean': (1, 136, 147, 163, 174),
    'SIDE-kernel@0256e9e:Kernel/Trivium.lean': (11, 76, 406, 414, 451, 462),
    'SIDE-kernel@0256e9e:Kernel/TriviumCode.lean': (9, 20),
    'SIDE-kernel@0256e9e:Kernel/TypeLevel.lean': (14,),
    'SIDE-kernel@0256e9e:Kernel/Voice2.lean': (80, 103),
    'SIDE-kernel@0256e9e:Kernel/Voice5.lean': (57,),
    'SIDE-kernel@0256e9e:Kernel/Voice6.lean': (66, 77, 88),
    'SIDE-kernel@0256e9e:Kernel/Voice7.lean': (52, 144),
    'SIDE-kernel@0256e9e:MetaKernel.lean': (3, 36, 52, 56, 59, 76, 118, 124, 173, 183, 203, 207, 239, 285, 294, 309, 342, 345, 357, 377, 411,
                                            415, 427, 464, 474, 487),
    'SIDE-kernel@0256e9e:legacy/Foundation3v2.lean': (35, 42, 54, 61),
    'SIDE-kernel@0256e9e:legacy/Foundation4v2.lean': (27, 33, 37, 42),
    'SIDE-kernel@0256e9e:legacy/ProductFormula_Int.lean': (71, 115, 136, 151),
    'SIDE-kernel@0256e9e:legacy/SchwarzReflection_PR.lean': (116,),
    'SIDE-li-map@b515e6b:LiLinearMap.lean': (1, 54),
    'SIDE-li-map@b515e6b:PrimeLedgerPositivity.lean': (3,),
    'SIDE-lv-conservation@2f71068:AxiomCheck.lean': (8,),
    'SIDE-lv-conservation@2f71068:PinnedGoal.lean': (4,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/C7OrderBounds.lean': (222,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/CouplingsAtPhi.lean': (1, 82, 124, 158, 256, 309, 330, 340, 397),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/DirichletC7Order.lean': (4,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/GammaBounds.lean': (4, 69),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/Genus5Confinement.lean': (103,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/LeadLaw.lean': (3,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/QWantedPoster.lean': (3, 53, 64, 171),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/RegisterPentagon.lean': (6, 103, 168, 280, 289),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/T2_SDarkness.lean': (4,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/T3_StepNineBridge.lean': (77,),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/ZeroActingPairing.lean': (3, 77, 141, 179, 258, 348, 444),
    'SIDE-lv-conservation@2f71068:SIDELvConservation/ZeroActingPartial.lean': (38, 82, 97, 111, 118),
    'SIDE-rcurve@d5f33b4:SIDERCurve/Criterion.lean': (1, 26),
    'SIDE-silence-principle@667c254:SIDESilencePrinciple/Basic.lean': (1, 110, 341, 417),
    'SIDE-simplicity@54ba4f3:SIDESimplicity/Codimension.lean': (1,),
    'SIDE-spinor@520abe7:SIDESpinor/Spinor.lean': (1, 55),
    'SIDE-spinor@520abe7:SIDESpinor/SpinorLeg.lean': (1,),
    'SIDE-structural-error-correction@6bf19ab:SIDEStructuralErrorCorrection/Basic.lean': (1, 83, 87, 116, 136, 140, 150, 185, 205, 218),
    'SIDE-structural-error-correction@6bf19ab:SIDEStructuralErrorCorrection/DeAlignment.lean': (1, 72, 82),
    'SIDE-substrate-cluster@2e76426:SIDESubstrateCluster/T7Labeling.lean': (1,),
    'SIDE-trivium@1aac3a9:Trivium/Bijection.lean': (1, 55, 240, 245, 252),
    'SIDE-window@3dab5f4:SIDEWindow/LocalModel.lean': (1,),
    'SIDE-window@3dab5f4:SIDEWindow/Sawtooth.lean': (1, 115, 124, 131, 153),
}
KREAD = set('%s:%d' % (f, n) for f, ns in KREAD_AT.items() for n in ns)   # ### row ids the seat read whole against their cited lines
KCONTROLS = [
    '  ### CLASS A: every row whose STATED makes an axiom claim (no/zero/0 axioms, axiom-free, standard three, a named profile) -- 69 rows -- '
    'against every `depends on axioms` print banked in relay data at a66c50a1 (1420 distinct prints in 411 files), matched by declaration name '
    'and then by the print`s own kernel, pin and file-identity line. Rows it moved: SIDE-kernel Kernel/Cascade/SieveCeiling.lean:132 (MATCHES '
    'stands; its ground corrected to the print relay data/b557_probe_c1.txt:13). Candidates read and dismissed: CartanBBridge.lean:1 (its `0 '
    'axioms beyond Mathlib core` at :49 is what the print relay data/b554_probe_k5.txt:7 shows), GS FoldedMirrorShadow (the `conv` print is '
    'SIDE-explicit-formula`s), SIDE-silence-principle Basic.lean:142 (its axiom-free names SIDE-kernel`s silence_universal, not the propext '
    'Bool lemma), MetaKernel.lean:140 (its recorded profile [propext, Quot.sound] is what type_I_has_ostrowski prints at v1.2, '
    'relay data/b557_probe_k6.txt; the file DIFFERS from 0256e9e there, so the print neither confirms nor contradicts it at the pin), SIDE-effects Milestones.lean:65 (the sorryAx print is at '
    'c66f3c5, a different file content; its sorries are at ef4cff7 too, and the row is OVERREACHES on that ground already). The control`s '
    'miss: it matched prints to the declarations of the row`s own file, so a docstring naming another kernel`s profile escaped it -- '
    'SIDE-kernel Kernel/TriviumCode.lean:9 names SIDE-cosmo`s steane_parameters at {propext, Quot.sound}, which relay data/b557_probe_co.txt:10 '
    'prints and agrees with; its helper reader found the print after hand-back and corrected the row`s ground (read_12, 18:39, after the '
    'banks` first commit 7ece93aa; read_10 corrected SieveCeiling.lean:132 the same way the seat had); the row stays OVERREACHES on its '
    'other ground, and these banks were rewritten from the corrected readings.',
    '  ### CLASS S: every `sorry` in code in relay data/b647_sorry_census.txt (37), the declaration it closes, and every row on that declaration '
    'or naming it: T3_perClass_to_combinations (lv :108) is row :77, S; product_formula_prime_pow and product_formula_nat (SIDE-kernel legacy) '
    'are rows :71 and :115, S; the three SIDE-effects milestones are rows that call them sorry-closed (not S); lv PinnedGoal :23 closes an '
    '`example` whose module header is row :4 (OVERREACHES, H: the header`s convertibility guarantee, which nothing compiles); the remaining 30 '
    '(SIDE-kernel legacy Schwarz builds and probes, CodimProbe, IdentityBuild1, FmodifProbe) close declarations that carry no docstring row '
    '(SchwarzBuild2`s head block, row :4, states a goal and a strategy). No sorry-closed declaration is described as holding by a row read MATCHES.',
]
CLASSES = {'S': 'a sorry-closed theorem described as holding', 'A': 'an axiom-profile claim against a banked print',
           'H': 'a module header claiming more than its file compiles'}


def _whole():
    """{row id: reader's fields} from the whole reading's read_NN.tsv; faults listed."""
    got, faults = collections.defaultdict(list), []
    n_chunks = len([p for p in os.listdir(WHOLE_SP) if re.match(r'^chunk_\d\d\.tsv$', p)]) if os.path.isdir(WHOLE_SP) else 0
    for n in range(1, n_chunks + 1):
        p = os.path.join(WHOLE_SP, 'read_%02d.tsv' % n)
        if not os.path.exists(p):
            faults.append('read_%02d.tsv absent' % n)
            continue
        for raw in io.open(p, encoding='utf-8'):
            f = raw.rstrip('\n').rstrip('\r').split('\t')
            if f[0].strip() and not f[0].startswith('#'):
                got[f[0].strip()].append(f)
    return got, faults, n_chunks


READ_AT = 'a66c50a1'   # ### relay: the commit the whole reading ran at (the brief's addendum); a reader's cite of a relay bank pins to it


def _kcite(c):
    """a reader's cite in the table's form: `relay:data/x:N`, `relay data/x:N`, `D:/relay/data/x:N`, `relay@data:x:N`
    -> relay@READ_AT:data/x:N."""
    c = c.strip()
    m = re.match(r'^(?:D:/relay/|relay[: /]\s*|relay@data:)(?:data/)?([\w./\-]+:\d+(?:-\d+)?)$', c)
    return ('relay@%s:data/%s' % (READ_AT, m.group(1))) if m else c


def _krows():
    """every kernel's rows: the generated row with the whole reading's verdict beside it, the seat's corrections applied."""
    got, faults, _n = _whole()
    out = []
    for k in kernels_of_chain():
        if k in CARRIED:
            continue
        for r in json.load(io.open(os.path.join(SP, 'kdocs_%s.json' % k), encoding='utf-8')):
            fs = got.get(r['id'], [])
            if len(fs) != 1:
                faults.append('%s: %d readings' % (r['id'], len(fs)))
                continue
            f = (fs[0] + [''] * 6)[:6]
            cell = dict(verdict=f[1].strip(), cls=f[2].strip() or '-', licensed=f[3].strip(), cited=f[4].strip(), action=f[5].strip())
            cell.update(KFIX.get(r['id'], {}))
            row = dict(id=r['id'], source='%s:%d' % (r['file'], r['line']), stated=r['stated'], licensed=cell['licensed'],
                       verdict=cell['verdict'], action=cell['action'], by='HAND', cited=[_kcite(c) for c in cell['cited'].split(';') if c.strip()],
                       kernel=k, rev=r['rev'], file=r['file'], line=r['line'], kind=r['kind'], decl=r['decl'], textual=r['textual'],
                       generated_verdict=r['verdict'] + ('/HAND-NEEDED' if r.get('hand_needed') else ''), generated_findings=r['findings'],
                       cls=cell['cls'] if cell['verdict'] != 'MATCHES' else '-', fixed=r['id'] in KFIX, why=KFIX.get(r['id'], {}).get('why', ''))
            out.append(row)
    extra = sorted(set(got) - set(r['id'] for r in out))
    if extra:
        faults.append('readings of no row: %s' % extra[:8])
    return out, faults


def kcheck(*a):
    """the whole reading read without writing: coverage, faults, counts, the non-MATCHES rows the seat has still to read."""
    import licensed_table as LT
    rows, faults = _krows()
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    c = collections.Counter(r['verdict'] for r in rows)
    print('  rows %d ; faults %d ; %s ; non-MATCHES unread by the seat %d' % (len(rows), len(faults), dict(c),
                                                                            sum(1 for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in KREAD)))
    for x in faults[:30]:
        print('    ### ' + x)


def kernel_banks(*a):
    """data/b647_table_<kernel>.txt/.json for each kernel read here and data/b647_table_kernels.txt/.json joined (SIDE-explicit-formula
    carried from b645): every row one verdict (HAND, cited), the generated verdict beside it, the rule's miss rate, the three classes counted,
    the seat's corrections with their reasons; refuses on a fault or a non-MATCHES row the seat has not read."""
    import licensed_table as LT
    rows, faults = _krows()
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in KREAD]
    if faults or unread:
        sys.exit('### %d FAULTS, %d NON-MATCHES ROWS UNREAD BY THE SEAT -- NOTHING WRITTEN: %s %s' % (len(faults), len(unread), faults[:5], unread[:8]))
    plan = json.load(io.open(os.path.join(SP, 'kdocs_plan.json'), encoding='utf-8'))
    J = []
    for k in sorted(set(r['kernel'] for r in rows)):
        rs = [r for r in rows if r['kernel'] == k]
        cnt, _f = LT.table(rs)
        gm = [r for r in rs if r['generated_verdict'] == 'MATCHES']
        missed = [r for r in gm if r['verdict'] != 'MATCHES']
        cls = collections.Counter(r['cls'] for r in rs if r['verdict'] != 'MATCHES')
        smp = plan.get('samples', {}).get(k, [])
        L = ['b647 -- COMPONENT 2, (R257)(2) AND THE AUTHOR`S ANSWER: %s`S DOCSTRINGS AT ITS MAIN %s, EACH TO ONE VERDICT (tools/licensed_table.py) (%s)' % (
            k, rs[0]['rev'], utc()), '',
            '### the rows: every declaration docstring, structure-field docstring, module header and head block of the kernel`s tracked .lean files '
            'at its main%s; the statement %s; the generated verdict (D1-D6) beside each row; every row read whole by a helper reader from the '
            'banked brief (relay data/b647_kernel_brief.txt) and every non-MATCHES row read whole by the seat' % (
                (' (%s, RUN-BENEATH-HOLD at b645, takes no row)' % ', '.join(RBH_FILES[k])) if k in RBH_FILES else '',
                'from the elaborated bank relay data/%s where the declaration is in it, TEXTUAL elsewhere' % ELAB[k] if k in ELAB else 'TEXTUAL throughout'),
            '### THE GENERATED RULE`S MISS RATE: of %d rows it read MATCHES, %d read otherwise whole (%s) ; its non-MATCHES rows read MATCHES whole: %d' % (
                len(gm), len(missed), ('%.1f%%' % (100.0 * len(missed) / len(gm))) if gm else '-',
                sum(1 for r in rs if r['generated_verdict'].split('/')[0] != 'MATCHES' and r['verdict'] == 'MATCHES')),
            '### THE THREE CLASSES THE RULE CANNOT SEE (the author`s answer): ' + ' ; '.join('%s %s %d' % (c, CLASSES[c], cls[c]) for c in 'SAH') +
            ' ; other grounds %d' % cls['-'],
            '### the seeded MATCHES sample of the generated rule (seed 647-%s): %s' % (k, ('%d rows, read by a helper reader before the whole '
                                                                                          'reading' % len(smp)) if smp else 'none (under 200 rows)'),
            '### the seat`s corrections after its whole read: %d' % sum(1 for r in rs if r['fixed']), '']
        L += ['### THE NON-MATCHES ROWS, EACH IN FULL (id | VERDICT | CLASS | generated):']
        for r in rs:
            if r['verdict'] != 'MATCHES':
                L += ['  %s | %s | %s | generated %s' % (r['id'], r['verdict'], r['cls'], r['generated_verdict']),
                      '      STATED   ' + re.sub(r'\s+', ' ', r['stated'])[:1200], '      LICENSED ' + r['licensed'], '      CITED    ' + '; '.join(r['cited']),
                      '      ACTION   ' + r['action']] + (['      SEAT     ' + r['why']] if r['why'] else [])
        L += ['', '### EVERY ROW (id | VERDICT | generated | TEXTUAL):']
        L += ['  %s | %s | %s | %s' % (r['id'], r['verdict'], r['generated_verdict'], 'TEXTUAL' if r['textual'] else 'ELABORATED') for r in rs]
        L += ['', '### ### **%s: ROWS %d ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d ; A ROW WITHOUT A VERDICT 0 ; THE RULE`S MISSES '
                  '%d OF %d ; CLASSES S %d A %d H %d.**' % (k, len(rs), cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'],
                                                          len(missed), len(gm), cls['S'], cls['A'], cls['H'])]
        put_txt('b647_table_%s.txt' % k, L)
        put_json('b647_table_%s.json' % k, dict(at=utc(), kernel=k, rev=rs[0]['rev'], counts=cnt, missed=len(missed), generated_matches=len(gm),
                                                classes=dict(cls), rows=rs))
        J.append(dict(kernel=k, rev=rs[0]['rev'], rows=len(rs), counts=dict(cnt), missed=len(missed), generated_matches=len(gm), classes=dict(cls),
                      fixed=sum(1 for r in rs if r['fixed'])))
    ef = jl(CARRIED['SIDE-explicit-formula'])
    tot = collections.Counter()
    for x in J:
        tot.update(x['counts'])
    tot.update(ef.get('counts') or {})
    T = ['b647 -- COMPONENT 2: EVERY KERNEL`S DOCSTRINGS, THE KERNELS` COUNTS JOINED ((R257)(2) and the author`s answer) (%s)' % utc(), '',
         '### SIDE-explicit-formula carried from b645 (relay data/b645_table_docstrings.txt at v0.26 = 82550e4, its main unmoved): %d rows ; %s' % (
             len(ef.get('rows') or []), ' ; '.join('%s %d' % (v, (ef.get('counts') or {}).get(v, 0)) for v in LT.VERDICTS)),
         '### every other kernel of the chain read here at its main, whole (kernel | main | rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED | the rule`s '
         'misses of its MATCHES | classes S A H | seat corrections):']
    for x in J:
        T.append('  %-34s %s | %4d | %4d | %3d | %3d | %3d | %3d of %4d | %d %d %d | %d' % (
            x['kernel'], x['rev'], x['rows'], x['counts'].get('MATCHES', 0), x['counts'].get('UNDERSTATES', 0), x['counts'].get('OVERREACHES', 0),
            x['counts'].get('UNLICENSED', 0), x['missed'], x['generated_matches'], x['classes'].get('S', 0), x['classes'].get('A', 0),
            x['classes'].get('H', 0), x['fixed']))
    nrow = sum(x['rows'] for x in J) + len(ef.get('rows') or [])
    T += ['', '### THE SEAT`S CONTROLS ON THE TWO CLASSES A READER COULD MISS (run over the whole reading before this bank was written):'] + KCONTROLS
    T += ['', '### ### **KERNELS %d (%d read here, 1 carried) ; ROWS %d -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d ; THE RULE`S MISSES %d OF '
              '%d ; CLASSES S %d A %d H %d.**' % (len(J) + 1, len(J), nrow, tot['MATCHES'], tot['UNDERSTATES'], tot['OVERREACHES'], tot['UNLICENSED'],
                                                 sum(x['missed'] for x in J), sum(x['generated_matches'] for x in J),
                                                 sum(x['classes'].get('S', 0) for x in J), sum(x['classes'].get('A', 0) for x in J),
                                                 sum(x['classes'].get('H', 0) for x in J))]
    put_txt('b647_table_kernels.txt', T)
    put_json('b647_table_kernels.json', dict(at=utc(), kernels=J, carried=dict(kernel='SIDE-explicit-formula', rows=len(ef.get('rows') or []),
                                                                              counts=ef.get('counts')), totals=dict(tot), rows=nrow))
    print(T[-1])


def sorries(*a):
    """data/b647_sorry_census.txt and .json: the author's answer at Component 2 -- before any further row is read, every `sorry` on every
    kernel's main at its current head, by file and line (git grep -n -w at the main commit, every .lean the main tracks outside .lake/),
    each occurrence classed as a sorry in code (a tactic or term on a line whose code part names it) or a mention (in a comment or a doc
    string). The standing rule: no sorry reaches any main. Every line goes to the closing in full."""
    ks = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    J, L = {}, []
    tot = collections.Counter()
    for k in ks:
        rev = g('D:/' + k, 'rev-parse', '--short=7', 'main').strip()
        if not rev:
            continue
        hits = []
        out = g('D:/' + k, 'grep', '-n', '-w', 'sorry', rev, '--', '*.lean')
        for l in out.split(NL):
            m = re.match(r'^[0-9a-f]+:(.+?):(\d+):(.*)$', l)
            if not m or m.group(1).startswith('.lake/'):
                continue
            f, ln, txt = m.group(1), int(m.group(2)), m.group(3)
            code = txt.split('--', 1)[0]
            # ### a line inside a block comment or doc string reads as a mention; the block state is read from the file at the commit
            hits.append(dict(file=f, line=ln, text=txt.strip()[:200], code_word=bool(re.search(r'\bsorry\b', code))))
        if hits:
            texts = {}
            for h in hits:
                if h['file'] not in texts:
                    texts[h['file']] = (_show('D:/' + k, rev, h['file']) or '').replace(chr(13), '').split(NL)
                ls = texts[h['file']]
                depth = 0
                for i, x in enumerate(ls[:h['line']], 1):
                    pre = x if i < h['line'] else x[:x.find('sorry') if 'sorry' in x else len(x)]
                    depth += pre.count('/-') - pre.count('-/')
                h['kind'] = 'code' if (h['code_word'] and depth <= 0) else 'mention'
            # ### built or not: the file under a lean_lib's `.submodules` glob or named as a lean_lib root in the lakefile at the commit
            # ### a lean_lib builds its roots (explicit `roots`, else its own name -- Lake's default) and every module they import, and
            # ### every module under a `.submodules` glob; the closure is read from the files' imports at the commit (lakefile.lean or .toml)
            lk = (_show('D:/' + k, rev, 'lakefile.lean') or '') + NL + (_show('D:/' + k, rev, 'lakefile.toml') or '')
            subs = re.findall(r'\.submodules\s+`([\w.]+)', lk)
            roots = [x.strip().lstrip('`').strip('"') for r in re.findall(r'roots\s*:?=\s*#?\[([^\]]*)\]', lk) for x in r.split(',') if x.strip()]
            for blk in re.split(r'(?=lean_lib\s+\w+|\[\[lean_lib\]\])', lk)[1:]:
                nm = re.match(r'lean_lib\s+(\w+)', blk) or re.search(r'name\s*=\s*"([\w.]+)"', blk)
                if nm and not re.search(r'roots\s*:?=|globs\s*:?=', blk):
                    roots.append(nm.group(1))
            tracked = set(x[:-5].replace('/', '.') for x in g('D:/' + k, 'ls-tree', '-r', '--name-only', rev).split(NL) if x.endswith('.lean'))
            built, todo = set(), [r for r in roots if r in tracked]
            built |= set(m for m in tracked for s in subs if m == s or m.startswith(s + '.'))
            todo += list(built)
            while todo:
                m = todo.pop()
                built.add(m)
                src = _show('D:/' + k, rev, m.replace('.', '/') + '.lean') or ''
                for imp in re.findall(r'^\s*import\s+([\w.]+)', src, re.M):
                    if imp in tracked and imp not in built:
                        todo.append(imp)
            for h in hits:
                h['built'] = h['file'][:-5].replace('/', '.') in built
        J[k] = dict(main=rev, hits=hits)
        nc = sum(1 for h in hits if h['kind'] == 'code')
        tot['code'] += nc
        tot['mention'] += len(hits) - nc
        L.append('  %-38s main %s ; sorry in code %d ; mentions %d' % (k, rev, nc, len(hits) - nc))
    D_ = ['b647 -- EVERY sorry ON EVERY KERNEL`S MAIN AT ITS CURRENT HEAD, BY FILE AND LINE (the author`s answer at Component 2; the standing '
          'rule: no sorry reaches any main) (%s)' % utc(), '',
          '### read: git grep -n -w sorry at each SIDE-* repository`s main commit, every tracked .lean outside .lake/; a hit is CODE when the word '
          'stands in the line`s code part outside any block comment or doc string, a MENTION otherwise', '', '### BY KERNEL:'] + L + ['']
    D_ += ['### EVERY sorry IN CODE, BY FILE AND LINE (BUILT: the file inside a lean_lib of the kernel`s lakefile at the commit; TRACKED ONLY: on '
           'main, outside every lean_lib):']
    for k, v in J.items():
        for h in v['hits']:
            if h['kind'] == 'code':
                D_.append('  %s@%s:%s:%d | %s | %s' % (k, v['main'], h['file'], h['line'], 'BUILT' if h['built'] else 'TRACKED ONLY', h['text']))
    built = sum(1 for v in J.values() for h in v['hits'] if h['kind'] == 'code' and h['built'])
    D_ += ['### sorry in code inside a built lean_lib: %d ; on main outside every lean_lib: %d' % (
        built, sum(1 for v in J.values() for h in v['hits'] if h['kind'] == 'code') - built)]
    D_ += ['', '### EVERY MENTION, BY FILE AND LINE:']
    for k, v in J.items():
        for h in v['hits']:
            if h['kind'] == 'mention':
                D_.append('  %s@%s:%s:%d | %s' % (k, v['main'], h['file'], h['line'], h['text']))
    D_ += ['', '### ### **KERNELS READ %d ; sorry IN CODE %d IN %d KERNELS ; MENTIONS %d.**' % (
        len(J), tot['code'], sum(1 for v in J.values() if any(h['kind'] == 'code' for h in v['hits'])), tot['mention'])]
    put_txt('b647_sorry_census.txt', D_)
    put_json('b647_sorry_census.json', dict(at=utc(), kernels=J, counts=dict(tot)))
    print(NL.join(L))
    print(D_[-1])


# ================================================================================ COMPONENT 3: THE NAVIGATOR'S MEMORY, (R257)(3)
# ### The export (relay data/b647_navigator_memory.txt, local and untracked) read through the licensed-statement table under the rule its
# ### header states: a sentence stating a fact about the corpus is a row; a sentence about how a seat behaves, a deadline, a patent, a
# ### location or anything personal is not a row and enters no relay bank -- its text is written nowhere, its count is. b646's seat-memory
# ### route (tools/b646_record.py `mem_rule` .. `seat_memory`) carried: the unit a sentence, the reading at the dated heading's date, the
# ### verdicts the same; no repair here -- the navigator repairs its own files on the author's word.
NAV_SP = os.path.join(SP, 'nav')
_MSPLIT = re.compile(r'(?<=[.!?])["\'*)\]]*\s+(?=\S)')
NAV_RULE = [
    'THE EXPORT: relay data/b647_navigator_memory.txt, four files between ==== lines; its header (before FILE 1) is the rule and no unit.',
    'THE UNIT: a sentence of a file`s lines, a heading line included, split where . ! or ? (and any closing quote, asterisk or bracket) meets '
    'whitespace; numbered fN:line.n by the export`s own line; every unit read.',
    'A ROW: a unit asserting a fact about the corpus -- the programme`s papers, ledgers, registry, kernels, tags, commits, the relay`s banks '
    'and tools, deposits and drafts, and what they contain. NOT A ROW, by the header`s rule: how a seat behaves (an instruction, a habit, a '
    'preference, a rule of conduct), a deadline, a patent, a location, anything personal; its text enters no bank, its count does. A unit '
    'mixing a conduct rule with a corpus fact is a row, judged on its facts.',
    'THE READING: a unit under a dated heading (`Current state -- ... (verified 2026-07-29 ...)`, `... b526-b536 ...`, a FILE line`s '
    '`updated` date) is read at the commits of its date or acts; an undated one at HEAD (relay and PLACE-papers main at the act); every fact '
    'against the lines cited, each repo@commit:path:N.',
    'MATCHES, UNDERSTATES, OVERREACHES, UNLICENSED as b646`s rule (relay data/b646_seat_memory_rule.txt (4)); the worst fact decides.',
    'ACTION: MATCHES none; UNDERSTATES or OVERREACHES RE-CUT: the sentence as the lines license it, for the navigator; UNLICENSED RETIRE TO '
    'ERRATA: why, or a work-order with a trigger. No repair is made by the seat.',
    'THE SEAT: every non-MATCHES row read whole against its lines; a MATCHES sample of 35 drawn by seed `647-navigator` (Python '
    'random.Random over the sorted MATCHES ids) read and printed.',
    'THE READERS: helper readers of this session, one per chunk of the units (FILE 1 in four chunks cut at line boundaries, FILES 2-4 one '
    'each); each writes uid <TAB> ROW or NOTCORPUS <TAB> VERDICT <TAB> LICENSED <TAB> CITED <TAB> ACTION, and for a NOTCORPUS unit the uid '
    'and the kind alone -- no text of a non-row is written anywhere.',
]


def _nav_units():
    """[(fileno, line, n, text)] over the export's four files; the header and the closing marker are no unit."""
    ls = io.open(os.path.join(ROOT, *K.EXPORT.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    out, fno = [], 0
    for i, l in enumerate(ls, 1):
        m = re.match(r'^==== FILE (\d): ', l)
        if m:
            fno = int(m.group(1))
            out.append((fno, i, 1, l.strip('= ').strip()))
            continue
        if l.startswith('==== END OF EXPORT') or not fno or not l.strip():
            continue
        for j, s in enumerate([s for s in _MSPLIT.split(l.strip()) if s.strip()], 1):
            out.append((fno, i, j, s.strip()))
    return out


def nav_rule(*a):
    """data/b647_nav_rule.txt: the unit, the row, the reading and the verdicts, printed before any helper reader reads a unit."""
    import hashlib
    b = open(os.path.join(ROOT, *K.EXPORT.split('/')), 'rb').read()
    L = ['b647 -- COMPONENT 3: THE NAVIGATOR`S MEMORY THROUGH THE LICENSED-STATEMENT TABLE, THE RULE PRINTED BEFORE THE RUN (%s)' % utc(), '',
         '### the export: relay %s, %d bytes, sha256 %s, untracked (written by the seat from the author`s paste, b646`s defect (j))' % (
             K.EXPORT, len(b), hashlib.sha256(b).hexdigest()),
         '### the table: relay tools/licensed_table.py, five cells, four verdicts, every row HAND with its lines cited', '']
    L += ['  (%d) %s' % (i + 1, r) for i, r in enumerate(NAV_RULE)]
    put_txt('b647_nav_rule.txt', L)
    print(NL.join(L[2:]))


def nav_units(*a):
    """the scratchpad's nav/: the units chunked for the helper readers by file (FILE 1 in four chunks cut at line boundaries); no bank."""
    os.makedirs(NAV_SP, exist_ok=True)
    U = _nav_units()
    chunks = []
    for f in (1, 2, 3, 4):
        us = [u for u in U if u[0] == f]
        if f == 1:
            size, cur, last = (len(us) + 3) // 4, [], None
            for u in us:
                if len(cur) >= size and u[1] != last:
                    chunks.append(cur)
                    cur = []
                cur.append(u)
                last = u[1]
            if cur:
                chunks.append(cur)
        else:
            chunks.append(us)
    for n, c in enumerate(chunks, 1):
        _write(os.path.join(NAV_SP, 'chunk_%02d.tsv' % n), ''.join('f%d:%d.%d\t%s\n' % (f, ln, j, s.replace('\t', ' ')) for f, ln, j, s in c).encode('utf-8'))
        print('  chunk %02d: FILE %d :%d-:%d, %d units' % (n, c[0][0], c[0][1], c[-1][1], len(c)))
    print('  units %d' % len(U))


# ### THE SEAT'S REDACTIONS: a row unit (a corpus fact in it) carrying words the header's rule keeps out of every bank -- a location on
# ### this machine, a patent -- has those words replaced in its STATED before any bank is written; each listed with what replaced it and
# ### printed in the table (the words themselves nowhere). Found by the screen over every row's three cells (drive paths, Users, patent,
# ### USPTO, deadline, ORCID, the author's names), 6 hits, 1 a false hit ("sealed"). The patterns are written so that this file does not
# ### spell the words they remove.
NAV_REDACT = {
    'f1:40.1': [(r', \w+ sessions P-\d–P-\d\)', ', [a label outside the corpus, omitted by the seat])')],
    'f1:60.1': [(r'[A-Z]:\\\S+ \(7 md\) and [A-Z]:\\\S+ \(8 md\)', '[two sibling directories on this machine, named by the seat abstractly] (7 md and 8 md)')],
    'f1:61.1': [(r'clones at [A-Z]: \(', 'clones [on this machine] (')],
    'f1:116.2': [(r'; \[\w+-shaped clause omitted\]\.', '; [a clause outside the corpus, omitted].')],
}
NAV_FIX = {}
# ### the 39 non-MATCHES rows, each read whole by the seat against its cited lines (spot-read at the source: f1:54.1 SIDE-effects
# ### Structural.lean :76-:84 at a0dc376; f1:113.2 README :121 at 5340891; f2:143.1 REGISTRY :191 at e1478b6; f1:86.1 FINDINGS :4751-:4753
# ### at 7c1c2da; f1:68.1 OPEN_TRAILS :8269 at eba14af) -- no correction
NAV_READ = set(('f1:18.1 f1:23.1 f1:31.1 f1:42.1 f1:44.1 f1:45.1 f1:54.1 f1:58.1 f1:59.1 f1:60.1 f1:61.1 f1:62.1 f1:68.1 f1:69.1 f1:70.1 '
                'f1:71.1 f1:79.1 f1:83.2 f1:85.1 f1:86.1 f1:88.1 f1:90.1 f1:104.2 f1:104.4 f1:109.2 f1:111.2 f1:112.2 f1:113.2 f1:114.2 f1:115.5 '
                'f1:116.1 f2:127.2 f2:143.1 f2:148.1 f2:149.1 f3:179.1 f3:190.1 f3:191.1 f3:235.1').split())
# ### the seeded MATCHES sample (seed 647-navigator, 35), each read by the seat against its cited lines at their commits
_AG = 'AGREE'
NAV_SAMPLE = dict((i, _AG) for i in (
    'f1:103.2 f1:104.1 f1:105.1 f1:106.1 f1:106.2 f1:106.3 f1:106.4 f1:108.2 f1:108.4 f1:109.4 f1:110.1 f1:112.3 f1:112.6 f1:113.3 f1:114.3 '
    'f1:115.3 f1:115.6 f1:28.1 f1:46.1 f1:53.1 f1:81.1 f1:82.1 f1:84.2 f1:93.3 f1:95.1 f2:127.1 f2:141.1 f2:142.1 f4:245.1 f4:250.1 '
    'f4:254.2 f1:96.1 f1:99.2').split())
NAV_SAMPLE['f1:95.2'] = 'AGREE (the lines give 4-7 % of the rest, the unit against the pair: the same range to the rounding, FINDINGS :5617)'
NAV_SAMPLE['f1:110.3'] = ('AGREE (H13b is "order of limits", OPEN_TRAILS :11586 at 0a0f958; H8 is read at "fine resolution", :11394; H4`s '
                          'gloss is not separately carried)')


def _redact(uid, s):
    for o, n in NAV_REDACT.get(uid, []):
        s2, k = re.subn(o, lambda _m: n, s)
        s = s2 if k == 1 else s + ' ### REDACTION NOT APPLIED'
    return s


def _nav_rows():
    U = dict(('f%d:%d.%d' % (f, ln, j), (f, ln, s)) for f, ln, j, s in _nav_units())
    got, faults = collections.defaultdict(list), []
    for p in sorted(os.listdir(NAV_SP)) if os.path.isdir(NAV_SP) else []:
        if not re.match(r'^rows_\d\d\.tsv$', p):
            continue
        for raw in io.open(os.path.join(NAV_SP, p), encoding='utf-8'):
            f = raw.rstrip('\n').rstrip('\r').split('\t')
            if f[0].strip() and not f[0].startswith('#'):
                got[f[0].strip()].append(f)
    out = []
    for uid, (fno, ln, s) in U.items():
        fs = got.get(uid, [])
        if len(fs) != 1:
            faults.append('%s: %d judgements' % (uid, len(fs)))
            continue
        f = fs[0] + [''] * 6
        cell = dict(kind=f[1].strip(), verdict=f[2].strip(), licensed=f[3].strip(), cited=f[4].strip(), action=f[5].strip())
        cell.update(NAV_FIX.get(uid, {}))
        if cell['kind'] == 'NOTCORPUS':
            out.append((uid, fno, None))
            continue
        if cell['kind'] != 'ROW':
            faults.append('%s: kind %r' % (uid, cell['kind']))
            continue
        out.append((uid, fno, dict(id=uid, source='%s:%d' % (K.EXPORT, ln), stated=_redact(uid, s), licensed=cell['licensed'], verdict=cell['verdict'],
                                   action=cell['action'], by='HAND', cited=[c.strip() for c in cell['cited'].split(';') if c.strip()],
                                   file='FILE %d' % fno, fixed=uid in NAV_FIX)))
    extra = sorted(set(got) - set(U))
    if extra:
        faults.append('judgements for no unit: %s' % extra[:10])
    return out, faults


def nav_check(*a):
    import licensed_table as LT
    out, faults = _nav_rows()
    rows = [r for _u, _f, r in out if r]
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    print('  units %d ; rows %d ; faults %d ; %s ; non-MATCHES unread %d' % (len(out), len(rows), len(faults),
                                                                           dict(collections.Counter(r['verdict'] for r in rows)),
                                                                           sum(1 for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in NAV_READ)))
    for x in faults[:30]:
        print('    ### ' + x)
    if 'list' in a:
        for r in rows:
            if r['verdict'] != 'MATCHES':
                print('  %s | %s | %s\n      STATED: %s\n      LICENSED: %s\n      CITED: %s\n      ACTION: %s' % (
                    r['id'], r['verdict'], r['file'], r['stated'], r['licensed'], '; '.join(r['cited']), r['action']))


def _nav_sample(rows):
    import random
    pool = sorted(r['id'] for r in rows if r['verdict'] == 'MATCHES')
    return sorted(random.Random('647-navigator').sample(pool, min(35, len(pool))))


def nav_table(*a):
    """data/b647_table_navigator_memory.txt and .json: every unit of the export read, the corpus units rows (HAND, cited), rows and non-rows
    counted per file, counts by verdict, every row printed (its sentence, a row`s text alone), the non-MATCHES rows in full for the navigator;
    refuses on a fault, an uncovered unit, an unread non-MATCHES row or a sample not read as drawn. No non-row`s text is written."""
    import licensed_table as LT
    out, faults = _nav_rows()
    rows = [r for _u, _f, r in out if r]
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in NAV_READ]
    smp = _nav_sample(rows)
    if faults or unread:
        sys.exit('### %d FAULTS, %d NON-MATCHES ROWS UNREAD -- NOTHING WRITTEN: %s %s' % (len(faults), len(unread), faults[:5], unread[:8]))
    if sorted(NAV_SAMPLE) != smp:
        sys.exit('### THE SAMPLE READ IS NOT THE SAMPLE DRAWN -- NOTHING WRITTEN: drawn %s' % smp)
    cnt = collections.Counter(r['verdict'] for r in rows)
    L = ['b647 -- COMPONENT 3: THE NAVIGATOR`S MEMORY THROUGH THE LICENSED-STATEMENT TABLE ((R257)(3)) (%s)' % utc(), '',
         '### the rule: relay data/b647_nav_rule.txt, printed and committed before the run ; the export: relay %s, untracked' % K.EXPORT,
         '### the readers: helper readers of this session, one per chunk; every non-MATCHES row read whole by the seat (%d corrected); a MATCHES '
         'sample of %d (seed 647-navigator) read, %d agree' % (sum(1 for r in rows if r['fixed']), len(smp),
                                                                sum(1 for v in NAV_SAMPLE.values() if v.startswith('AGREE'))),
         '', '### PER FILE (units read ; rows ; not rows ; by verdict):']
    for f in (1, 2, 3, 4):
        us = [x for x in out if x[1] == f]
        rs = [r for _u, _f, r in us if r]
        c = collections.Counter(r['verdict'] for r in rs)
        L.append('  FILE %d : units %3d ; rows %3d ; not rows %3d ; %s' % (f, len(us), len(rs), len(us) - len(rs),
                                                                          ', '.join('%s %d' % (v, c[v]) for v in LT.VERDICTS)))
    L += ['', '### THE MATCHES SAMPLE READ BY THE SEAT (%d):' % len(smp)] + ['  %s : %s' % (i, NAV_SAMPLE[i]) for i in smp]
    L += ['', '### THE SEAT`S REDACTIONS (%d rows): words the header`s rule keeps out of every bank, found in row units by the screen over every '
              'row`s three cells and replaced in STATED before this bank was written (the words nowhere here):' % len(NAV_REDACT)]
    L += ['  %s : replaced by "%s"' % (u, '"; "'.join(n for _o, n in NAV_REDACT[u])) for u in sorted(NAV_REDACT)]
    L += ['', '### THE NON-MATCHES ROWS, IN FULL, FOR THE NAVIGATOR (who repairs its own files on the author`s word):']
    for r in rows:
        if r['verdict'] != 'MATCHES':
            L += ['  %s %s (%s)' % (r['id'], r['verdict'], r['file']), '      STATED:   ' + r['stated'], '      LICENSED: ' + r['licensed'],
                  '      CITED:    ' + '; '.join(r['cited']), '      ACTION:   ' + r['action']]
    L += ['', '### EVERY ROW (id | verdict | stated | licensed | cited):']
    for r in rows:
        L += ['  %s | %s | %s' % (r['id'], r['verdict'], r['stated']), '      LICENSED: %s' % r['licensed'], '      CITED: %s' % '; '.join(r['cited'])]
    L += ['', '### ### **UNITS READ %d ; ROWS %d ; NOT ROWS %d -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d ; FAULTS 0.**' % (
        len(out), len(rows), len(out) - len(rows), cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'])]
    put_txt('b647_table_navigator_memory.txt', L)
    put_json('b647_table_navigator_memory.json', dict(at=utc(), counts=cnt, per_file={('FILE %d' % f): dict(
        units=sum(1 for x in out if x[1] == f), rows=sum(1 for x in out if x[1] == f and x[2])) for f in (1, 2, 3, 4)}, rows=rows, sample=NAV_SAMPLE))
    print(L[-1])


# ================================================================================ COMPONENT 4, (R257)(4): THE DESCRIPTION AT v4
# ### b646's composer (tools/b646_record.py `compose_v3`, sealed at b646, reproducing v3 byte for byte at this act -- `v3_same`) carried
# ### unedited; v4 is its output with (R257)(4)'s four edits applied in order, each an exact replacement whose anchor must occur once (a
# ### missed anchor writes NOT READ, which `describe` refuses):
# ###   (a) the glossed passages: not_trivialSummandPremise's row glossed in six words; dedekind_rhs' row's two premises separated; one
# ###       plain-words bracket each for Phi and the bracket (h1_complete_at_Phi's row) and for the squeeze and its jaws (WHAT IS OPEN), each
# ###       from its source's own lines; "the surround" given its glossary entry where THE CLAIM first quotes it;
# ###   (b) exhaustiveness said once: the parenthesis in the located clause removed, the "On exhaustiveness" sentence kept;
# ###   (c) the open-premise phrase twice: the located clause's "and carries as its one open premise" removed, so "carried as the one open
# ###       premise" stands once in THE CLAIM (h2_sign's gloss) and once in WHAT IS OPEN;
# ###   (d) the definitions paragraph of WHAT THE LOAD-BEARING THEOREMS ASSUME cut to the glossary's one-sentence forms, the glossary named,
# ###       the plain-words brackets that were not glossary forms removed, "priced" glossed beside W-ORD, the lists untouched; the salt-check
# ###       sentence (no glossary entry) kept as v3 has it.
V4_EDITS = ('a', 'b', 'c', 'd')
V3 = 'b646_deposit_description.txt'
V4 = 'b647_deposit_description.txt'
EXH_PAREN = ' (in its attribution face covers_all, over the seven-class catalogue complete over its named classes)'
LOC_TAIL = ('which the kernel states, proves equivalent to RH, and carries as its one open premise.',
            'which the kernel states and proves equivalent to RH.')
NOT_TSP = ('<li>not_trivialSummandPremise -- DERIVES</li>', '<li>not_trivialSummandPremise -- DERIVES -- it proves TrivialSummandPremise false as stated</li>')
DED = ("it holds on the premises TrivialSummandPremise', the restated premise, witnessed in the kernel at the constant 1 "
       "(trivialSummandPremise'_witness) and EulerFactorPremise, whose status is WITNESSED",
       "it holds on two premises: TrivialSummandPremise', the restated premise, witnessed in the kernel at the constant 1 "
       "(trivialSummandPremise'_witness); and EulerFactorPremise, whose status is WITNESSED")
# ### Phi: SIDE-lv-conservation SIDELvConservation/T1_MellinFactorization.lean :24-:26 at v0.8.0 = 6efa9e5 ("The (fixed) Mellin integrand
# ### whose Mellin transform at s / 2 reproduces completedRiemannZeta s on the convergence half-plane"); the bracket: CouplingsAtPhi.lean
# ### :415-:416 ("the h1 leg of the T3' bracket; h2 ... remains the outstanding obligation")
PHI = ('which stays open</li>',
       'which stays open [in plain words: Phi is the fixed function whose Mellin transform at s/2 gives the completed zeta function where '
       'the transform converges; the bracket pairs what is proved at Phi, the couplings, with what is not, h2]</li>')
# ### the squeeze and its jaws: THE_UNCONDITIONAL_SURROUND_v0_5.md :153 ("One jaw is the Euler zero-free region ... pressing in from σ = 1
# ### ... The other jaw is the functional-equation transversality at the line ... If the two jaws provably overlap, the interior between
# ### them admits no off-line zero.")
SQZ = ('large enough that the transversality obstruction reaches the zero-free region.',
       'large enough that the transversality obstruction reaches the zero-free region. [In plain words: one jaw is the region near real part '
       'one where the Euler product allows no zero; the other is the region around real part one half that a simple zero on the line opens '
       'by crossing it; a height is a zero\'s imaginary part; if the jaws overlap at every height, no zero lies off the line.]')
SURR_AT = 'Both are equivalent to RH given the surround." '


def _gl4():
    """the glossary's entries, the latest of a repeated name winning, read from relay data/glossary.txt as committed in this act."""
    g = {}
    for l in io.open(os.path.join(D, 'glossary.txt'), encoding='utf-8').read().replace(chr(13), '').split(NL):
        if l.strip() and not l.startswith('#'):
            p = l.split('\t')
            g[p[0]] = p[1]
    return g


def _once(h, old, new, tag):
    n = h.count(old)
    return h.replace(old, new) if n == 1 else h + ' NOT READ (%s: the anchor found %d times)' % (tag, n)


def _defs4(gl):
    """(d): the definitions paragraph in the glossary's one-sentence forms, the glossary named."""
    return ('The definitions here are the programme\'s glossary\'s, one sentence each, as the keystone census prints them. A premise is %s. '
            'A premise\'s own evidence is %s. A HINGE is %s. A name beginning W-ORD- is %s; priced, of a work-order, means %s. OPEN_TRAILS is '
            '%s. ' % (
                gl['premise'].rstrip('.'), gl['own evidence'].replace('of a premise: ', '').rstrip('.'),
                gl['HINGE'].replace(' (the entry above)', '').rstrip('.'), gl['W-ORD'].rstrip('.'),
                gl['priced'].replace('of a work-order: ', '').rstrip('.'), gl['OPEN_TRAILS'].rstrip('.')))


def compose_v4(edits=V4_EDITS):
    """v4's HTML: b646's compose_v3 (its rules as sealed) with (R257)(4)'s edits named in `edits` applied in the order a, b, c, d."""
    import b646_record as B6
    h = B6.compose_v3()
    gl = _gl4()
    if 'a' in edits:
        h = _once(h, NOT_TSP[0], NOT_TSP[1], 'a, not_trivialSummandPremise')
        h = _once(h, DED[0], DED[1], "a, dedekind_rhs'")
        h = _once(h, PHI[0], PHI[1], 'a, Phi and the bracket')
        h = _once(h, SQZ[0], SQZ[1], 'a, the squeeze')
        h = _once(h, SURR_AT, SURR_AT + 'The surround, in the glossary\'s words: %s. ' % gl['the surround'].rstrip('.'), 'a, the surround')
    if 'b' in edits:
        h = _once(h, EXH_PAREN, '', 'b, the parenthesis')
    if 'c' in edits:
        h = _once(h, LOC_TAIL[0], LOC_TAIL[1], 'c, the located clause')
    if 'd' in edits:
        i, j = h.find('A premise is a binder'), h.find('The premises, by status')
        sc_ = re.search(r'A salt check is [^.]+\. ', h[i:j]) if 0 <= i < j else None
        h = (h[:i] + _defs4(gl) + sc_.group(0) + h[j:]) if sc_ and h.count('A premise is a binder') == 1 else h + ' NOT READ (d)'
    return h


def v3_same(*a):
    """b646's composer at this act against v3 as banked: byte for byte."""
    import b646_record as B6
    h, v3 = B6.compose_v3(), rd(V3)
    print('  compose_v3 at this act %d bytes ; v3 as banked %d bytes ; the same: %s' % (len(h.encode('utf-8')), len(v3.encode('utf-8')), h == v3))
    return h == v3


def describe4(*a):
    """data/b647_deposit_description.txt (v4) and .json beside v3: composed from banks, the forbidden-content test (b644's sealed
    `forbidden`) run over it, the five parts in order, every tag Zenodo accepts; refuses on any hit, unread figure or part out of order."""
    import hashlib
    import b646_record as B6
    R4 = B6._R4()
    if not v3_same():
        sys.exit('### b646`S COMPOSER DOES NOT REPRODUCE v3 -- NOTHING COMPOSED')
    html = compose_v4()
    heads = re.findall(r'<p><strong>(.*?)</strong></p>', html)
    order_ok = heads == [x.rstrip('.') for x in B6.PART_HEADS]
    hits = R4.forbidden(html)
    unread = [m.group(0) for m in re.finditer(r'NOT READ|NOT BANKED|not in the table|None', html)]
    bad = sorted(set(re.findall(r'</?([a-zA-Z0-9]+)', html)) - B6._allowed_tags())
    print('  parts %d, in order %s ; forbidden hits %d ; unread %d ; tags outside Zenodo`s %s ; bytes %d' % (
        len(heads), order_ok, len(hits), len(unread), bad or 'none', len(html.encode('utf-8'))))
    for x in hits + [('unread', u) for u in unread]:
        print('    ### %s : %s' % x)
    if DRY:
        _write(os.path.join(SP, 'b647_deposit_description_dry.txt'), html.encode('utf-8'))
        return
    if hits or unread or not order_ok or bad:
        sys.exit('### A FORBIDDEN CONTENT, AN UNREAD FIGURE, A TAG OR THE PARTS OUT OF ORDER -- NOTHING WRITTEN')
    b = html.encode('utf-8')
    _write(os.path.join(D, V4), b)
    put_json('b647_deposit_description.json', dict(at=utc(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), heads=heads, edits=list(V4_EDITS),
                                                   order_ok=order_ok, forbidden=hits, v3_bytes=len(rd(V3).encode('utf-8'))))
    print('  written: data/%s %d bytes, sha256 %s' % (V4, len(b), hashlib.sha256(b).hexdigest()[:16]))


def desc_diff4(*a):
    """data/b647_desc_diff.txt: v3 against v4 by part -- each part's bytes in each, the change, the tokens lost and added (b644's sealed
    `invariance`), and each edit's text before and after as the composer applies it."""
    import b646_record as B6
    R4 = B6._R4()
    v3, v4 = rd(V3), rd(V4)
    if not v4:
        sys.exit('### v4 IS NOT BANKED -- RUN `describe4` FIRST')
    p3, p4 = dict(B6._parts_of(v3)), dict(B6._parts_of(v4))
    b3, b4 = len(v3.encode('utf-8')), len(v4.encode('utf-8'))
    L = ['b647 -- COMPONENT 4, (R257)(4): THE DESCRIPTION, v3 AGAINST v4, BY PART (%s)' % utc(), '',
         '### v3: relay data/%s, %d bytes ; v4: relay data/%s, %d bytes ; the change %+d bytes' % (V3, b3, V4, b4, b4 - b3), '']
    for h in B6.PART_HEADS:
        a_, b_ = p3.get(h, ''), p4.get(h, '')
        lost, added = R4.invariance('<p>%s</p>' % a_, '<p>%s</p>' % b_)
        L += ['### %s v3 %d bytes (text) ; v4 %d bytes (text, tags removed) ; %+d' % (h, len(a_.encode('utf-8')), len(b_.encode('utf-8')),
                                                                                   len(b_.encode('utf-8')) - len(a_.encode('utf-8'))),
              '    tokens lost: %s' % (sorted(lost.items()) or 'none'), '    tokens added: %s' % (sorted(added.items()) or 'none')]
    L += ['', '### THE EDITS, EACH AS APPLIED (before -> after):']
    for tag, (o, n) in (('(a) not_trivialSummandPremise', NOT_TSP), ("(a) dedekind_rhs'", DED), ('(a) Phi and the bracket', PHI),
                        ('(a) the squeeze', SQZ), ('(b) the parenthesis', (EXH_PAREN.strip(), '(removed)')), ('(c) the located clause', LOC_TAIL)):
        L += ['  %s' % tag, '      v3: ' + o, '      v4: ' + n]
    L += ['  (a) the surround: after "%s" v4 adds the glossary entry' % SURR_AT.strip(), '  (d) the definitions paragraph, v4: ' + _defs4(_gl4()).strip()]
    L += ['', '### ### **v3 %d BYTES ; v4 %d BYTES ; %+d.**' % (b3, b4, b4 - b3)]
    put_txt('b647_desc_diff.txt', L)
    print(L[-1])


def desc_test4(*a):
    """data/b647_desc_test.txt: the forbidden-content test rerun (b644's sealed `forbidden`) by b646's planted cases with v4 as banked in
    v3's place, each case counted; the composer's edit tests (tools/test_composer_b647.py) run and counted beside it."""
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
             ('v4 as banked (no hit)', rd(V4), None)]
    L = ['b647 -- COMPONENT 4: THE DESCRIPTION`S FORBIDDEN-CONTENT TEST, RERUN BY PLANTED TEXT, AND THE COMPOSER`S EDIT TESTS (%s)' % utc(), '']
    n = 0
    for i, (label, text, want) in enumerate(cases, 1):
        hits = R4.forbidden(text)
        ok = (any(k == want for k, _m in hits) if want else (not hits and bool(text)))
        n += ok
        L.append('  (%d) %-40s hits %s ; %s' % (i, label, [k for k, _m in hits][:4], 'PASS' if ok else '### FAIL'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_composer_b647.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    L += ['', '### THE FORBIDDEN-CONTENT TEST: %d of %d cases as wanted -- %s' % (n, len(cases), 'PASS' if n == len(cases) else 'FAIL'), '',
          '### THE COMPOSER`S EDIT TESTS (tools/test_composer_b647.py), exit %d:' % r.returncode] + ['  ' + x for x in (r.stdout or '').rstrip(NL).split(NL)]
    L += ['', '### ### **FORBIDDEN-CONTENT %d of %d ; EDIT TESTS EXIT %d.**' % (n, len(cases), r.returncode)]
    put_txt('b647_desc_test.txt', L)
    print(NL.join(L[-3:]))


# ### THE FIFTH READER, (R257)(4): b646's form carried (its packet, lead, task and command builders imported, the directory C:\reader_b647);
# ### v4 as text; the three questions of (R254)(8); run by the author on the author's PowerShell; scored by b644's needles and by the seat's
# ### hand reading (data/b647_reader_d5_handread.txt, written before the needles are read); the residue banked.
READER5 = 'C:/reader_b647'


def _b6r():
    import b646_record as B6
    B6.READER = dict(B6.READER, dir=READER5)
    return B6


def reader_packet5(*a):
    """data/b647_reader_d5_packet.txt and data/b647_reader_d5_packet/: v4 as text with the three questions, staged at C:\\reader_b647
    (refused if it exists and is not empty), the no-disclosure arm and the outside names checked, the command the author runs printed."""
    import b616_record as R6
    B6 = _b6r()
    R4 = B6._R4()
    r = B6.READER
    doc = B6._v3_text(rd(V4))
    if not doc.strip():
        sys.exit('### v4 IS EMPTY -- NOTHING WRITTEN')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(r['questions']))
    task = B6._reader_task()
    nd = R6.nd_hits(doc + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in R4.OUTSIDE_NEEDLES if n in doc]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b647_reader_d5_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in ((r['doc'], doc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    if not DRY:
        if os.path.exists(r['dir']) and os.listdir(r['dir']):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- NOT WRITTEN' % r['dir'])
        os.makedirs(r['dir'] + '/packet', exist_ok=True)
        for n_, t_ in (('packet/' + r['doc'], doc), ('packet/questions.txt', qs), ('lead.txt', B6._reader_lead()), ('full_prompt.txt', task)):
            _write(os.path.join(r['dir'], n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    L = ['b647 -- THE FIFTH READER`S PACKET D5, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/%s %d bytes, sha256 %s ; packet/questions.txt ; lead.txt ; full_prompt.txt) ; banked: relay data/b647_reader_d5_packet/' % (
             r['dir'], r['doc'], len(doc.encode('utf-8')), sha(doc.encode('utf-8'))),
         '### the document: v4 (relay data/%s) as text -- a part`s head as == HEAD ==, a list item as a line marked -' % V4,
         '### the questions, (R254)(8)`s three: %s' % ' / '.join(r['questions']),
         '### the no-disclosure arm: %s ; outside names: %s' % (dict(nd), outside or 'NONE'),
         '', '### the command, run by the author on the author`s PowerShell from %s, a directory with no project memory:' % r['dir'], '    ' + B6._reader_cmd()]
    put_txt('b647_reader_d5_packet.txt', L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 5, (R257)(6): THE CENSUS'S COLUMNS EXTENDED
# ### b645's rules (tools/licensed_table.py `cluster`, `maturity`; printed in relay data/b645_census_columns.txt) applied unchanged to every
# ### keystone the table now reaches: the 48 of b645's roster (the monograph's maturity from b645's table, as b645 set it), the seven Day 1
# ### companions (relay data/b646_table_<name>.json, b646), and every kernel of (2) (relay data/b647_table_<kernel>.json, SIDE-explicit-
# ### formula from b645's table). A kernel's CLUSTER by the terminal rule over its rows in the terminal table (the path rule has no path);
# ### its open-stated rows its theorems at INTERFACES on a premise whose status is OPEN (b645's reading for SIDE-explicit-formula); a
# ### kernel's PHASE `-` (no REGISTRY heading; b645 printed 1 for SIDE-explicit-formula, carried as printed).
def columns5(*a):
    """data/b647_census_columns.txt and .json beside b645's: CLUSTER, PHASE, MATURITY for the roster, the companions and the kernels; the
    keystones still blank listed; no census edition (v0.8 at b648)."""
    import licensed_table as LT
    import b645_record as B5
    K_ = B5._roster()
    if len(K_) != 48:
        sys.exit('### THE ROSTER READ %d KEYSTONES, NOT 48 -- NOTHING WRITTEN' % len(K_))
    M = jl('b645_table_monograph.json')
    mono_open = sum(1 for r in M.get('rows') or [] if r.get('stated_as') == 'open')
    ST = dict((r['head'], r['status']) for r in jl('b643_premise_table.json').get('rows') or [])
    tt, _md = B5._tt()
    reg = K.show('REGISTRY.md', K.PRE_PP) or ''

    def open_itf(rows):
        return sum(1 for x in rows if x['grade'] == 'INTERFACES' and any(ST.get(h) == 'OPEN' for h in re.findall(r'\b([A-Z]\w+)\b', x['statement'] or '')))
    L = ['b647 -- COMPONENT 5, (R257)(6): THE CENSUS`S CLUSTER, PHASE AND MATURITY COLUMNS EXTENDED TO EVERY KEYSTONE THE TABLE REACHES -- NO '
         'EDITION (%s)' % utc(), '',
         '### the rules: b645`s, unchanged (relay data/b645_census_columns.txt, its head; tools/licensed_table.py cluster and maturity) ; the '
         'roster: b645`s 48 (tools/b645_record.py _roster) ; the tables: the monograph b645, the seven companions b646, the kernels b647 and '
         'SIDE-explicit-formula b645', '',
         '### (i) THE ROSTER`S 48 (row | tier | id | path | PHASE | CLUSTER (how) | MATURITY (why)):']
    J = []
    for k in K_:
        t = B5._show(PP, 'HEAD', k['path']) or ''
        names = set(re.findall(r'`(?:[\w.]+\.)?([A-Za-z_][\w\'₀-₉]*)`', t))
        c, how = LT.cluster(k['path'], names)
        if not c and k['id'] in B5.CLUSTER_HAND:
            c, cites = B5.CLUSTER_HAND[k['id']]
            how = 'HAND: ' + ', '.join(cites)
        if k['id'] == 'd1-1':
            mat, why = LT.maturity(M['counts'], open_rows=mono_open)
            why += ' (relay data/b645_table_monograph.txt: %s ; stated open %d)' % (', '.join('%s %d' % kv for kv in M['counts'].items()), mono_open)
        else:
            mat, why = LT.maturity(None)
        J.append(dict(k, kind='roster', cluster=c, how=how, maturity=mat, why=why))
        L.append('  %s | %-2s | %-40s | %-52s | %-4s | %-15s (%s) | %s (%s)' % (k['row'], k['tier'], k['id'][:40], k['path'][:52], k['phase'],
                                                                             c or '### BLANK', how[:40], mat or '### BLANK', why))
    L += ['', '### (ii) THE SEVEN DAY 1 COMPANIONS (id | path | REGISTRY row | PHASE | CLUSTER (how) | MATURITY (why)):']
    import b646_worklist as K6
    for name, lab in K6.COMPANIONS:
        path = 'day1/%s.md' % name
        T = jl('b646_table_%s.json' % name)
        cn = T.get('counts')
        rid = [l for l in reg.split(NL) if ('%s.md' % name) in l][:1]
        t = B5._show(PP, K.PRE_PP, path) or ''
        names = set(re.findall(r'`(?:[\w.]+\.)?([A-Za-z_][\w\'₀-₉]*)`', t))
        c, how = LT.cluster(path, names)
        so = sum(1 for r in T.get('rows') or [] if r.get('stated_as') == 'open')
        mat, why = LT.maturity(cn, open_rows=so)
        why += ' (relay data/b646_table_%s.txt: %s ; stated open %d)' % (name, ', '.join('%s %d' % kv for kv in (cn or {}).items()), so)
        J.append(dict(kind='companion', id='%s %s' % (name, lab), path=path, phase='1', registry=(rid[0].strip()[:120] if rid else 'NOT IN REGISTRY'),
                      cluster=c, how=how, maturity=mat, why=why))
        L.append('  %-28s %s | %-48s | 1 | %-15s (%s) | %s (%s)' % (name + ' ' + lab, path, (rid[0].strip()[:48] if rid else '### NOT IN REGISTRY'),
                                                                    c or '### BLANK', how[:40], mat or '### BLANK', why))
    L += ['', '### (iii) THE KERNELS (kernel | main | PHASE | CLUSTER (how) | MATURITY (why)):']
    KJ = jl('b647_table_kernels.json')
    ef = jl('b645_table_docstrings.json')
    kin = [(x['kernel'], x['rev'], x['counts'], 'relay data/b647_table_%s.txt' % x['kernel']) for x in KJ.get('kernels') or []]
    kin.append(('SIDE-explicit-formula', '82550e4', ef.get('counts'), 'relay data/b645_table_docstrings.txt'))
    for kname, rev, cn, src in sorted(kin):
        rows = [x for x in tt if x['repo'] == kname]
        c, how = LT.cluster('', set(x['name'].split('.')[-1] for x in rows))
        so = open_itf(rows)
        mat, why = LT.maturity(cn, open_rows=so)
        why += ' (%s: %s ; theorems at INTERFACES on an OPEN premise %d)' % (src, ', '.join('%s %d' % kv for kv in (cn or {}).items()), so)
        ph = '1' if kname == 'SIDE-explicit-formula' else '-'
        J.append(dict(kind='kernel', id='%s %s' % (kname, rev), path='D:/' + kname, phase=ph, cluster=c, how='terminals: ' + how if c else how,
                      maturity=mat, why=why, terminals=len(rows)))
        L.append('  %-34s %s | %s | %-15s (%s) | %s (%s)' % (kname, rev, ph, c or '### BLANK', ('terminals: ' + how)[:60] if c else how[:60],
                                                           mat or '### BLANK', why))
    blank_m = [x['id'] for x in J if not x['maturity']]
    blank_c = [x['id'] for x in J if not x['cluster']]
    L += ['', '### BY KIND: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['kind'] for x in J).items())),
          '### BY CLUSTER: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['cluster'] or 'BLANK' for x in J).items())),
          '### BY MATURITY: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['maturity'] or 'BLANK (NOT YET IN THE TABLE)' for x in J).items())),
          '', '### THE KEYSTONES STILL BLANK IN MATURITY (%d), not yet in the table:' % len(blank_m)] + ['  ' + x for x in blank_m]
    L += ['### CLUSTER BLANK (%d): %s' % (len(blank_c), blank_c or 'none')]
    L += ['', '### ### **ROWS %d (ROSTER 48, COMPANIONS 7, KERNELS %d) ; CLUSTER PLACED %d, BLANK %d ; MATURITY ASSIGNED %d, BLANK AND MARKED %d ; NO '
              'BLANK COUNTED AS A VALUE.**' % (len(J), sum(1 for x in J if x['kind'] == 'kernel'), len(J) - len(blank_c), len(blank_c),
                                               len(J) - len(blank_m), len(blank_m))]
    put_txt('b647_census_columns.txt', L)
    put_json('b647_census_columns.json', dict(at=utc(), rows=J, rule=LT.MATURITY_RULE))
    print(L[-1])


def reader_score5(*a):
    """data/b647_reader_d5_compare.txt and .json: the fifth reader's answers copied from off D:\\, each scored by b644's needles (imported) and
    beside it the seat's hand reading (data/b647_reader_d5_handread.txt, written first), both figures; refuses without the hand reading."""
    B6 = _b6r()
    R4 = B6._R4()
    r = B6.READER
    src = os.path.join(r['dir'], 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    hr = rd('b647_reader_d5_handread.txt')
    if not re.search(r'^HAND \d: (AGREE|DIFFER)', hr, re.M):
        sys.exit('### THE HAND READING IS NOT BANKED -- THE NEEDLES ARE NOT READ BEFORE IT')
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b647_reader_d5_answers.txt'), t.encode('utf-8'))
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
    L = ['b647 -- THE FIFTH READER D5: ANSWERS SCORED BY THE NEEDLES AND BY HAND (%s)' % utc(), '',
         '### the answers: relay data/b647_reader_d5_answers.txt, copied from %s ; the reader`s session: %s' % (src, mem),
         '### the hand reading: relay data/b647_reader_d5_handread.txt, banked before the needles were read', '']
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
    put_txt('b647_reader_d5_compare.txt', L)
    put_json('b647_reader_d5_compare.json', dict(at=utc(), answers=res, needles=n_ok, hand=kh, of=len(N),
                                                 unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ### THE DRAFT'S DESCRIPTION, (R257)(4): b646's route (z_desc / z_read / z_hold) carried with v4's bank: b639's http (the token in the
# ### Authorization header alone, the User-Agent naming no person); the draft's description replaced by v4, every other metadata key carried,
# ### no file touched, publish never called; read back once; HELD. Runs after the fifth reader's scoring and the residue.
ZRES4 = 'b647_zenodo.json'


def _zmerge4(cells):
    R = jl(ZRES4) if os.path.exists(os.path.join(D, ZRES4)) else {}
    R.update(cells)
    put_json(ZRES4, R)


def z_desc4(*a):
    """data/b647_zenodo_desc.txt: draft K.DRAFT read once (unsubmitted, or nothing done) and its metadata PUT once with v4's bank, every other
    key carried; the prior description's bytes and digest banked, not its text; the file list banked for the read-back. Runs once."""
    import hashlib
    import b639_record as R39
    import b646_record as B6
    if not R39._tok():
        sys.exit('### THE TOKEN IS NOT SET -- NO CALL MADE')
    if os.path.exists(os.path.join(D, ZRES4)) and jl(ZRES4).get('desc'):
        sys.exit('### THE DESCRIPTION HAS BEEN REPLACED -- IT DOES NOT RUN TWICE')
    if not os.path.exists(os.path.join(D, 'b647_reader_d5_compare.txt')):
        sys.exit('### THE FIFTH READER IS NOT SCORED -- THE DESCRIPTION IS NOT REPLACED BEFORE IT')
    v4 = open(os.path.join(D, V4), 'rb').read().decode('utf-8')
    base = 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT
    st, b = R39.http('GET', base)
    d = B6._jx(b) or {}
    if st != 200 or d.get('submitted') or str(d.get('id')) != K.DRAFT:
        sys.exit('### THE DRAFT IS NOT AN UNSUBMITTED %s (HTTP %d) -- NOTHING DONE' % (K.DRAFT, st))
    md = dict(d.get('metadata') or {})
    old = md.get('description') or ''
    files = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    md['description'] = v4
    sp, bp = R39.http('PUT', base, body={'metadata': md})
    hx = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
    v3 = rd(V3)
    L = ['b647 -- THE ROUTE, THE DRAFT`S DESCRIPTION REPLACED BY v4 (%s)' % utc(), '',
         '### GET the draft %s : HTTP %d ; state %s ; submitted %s ; %d files' % (K.DRAFT, st, d.get('state'), d.get('submitted'), len(files)),
         '### the description before : %d bytes, sha256 %s ; v3`s bank %d bytes, sha256 %s ; the draft held v3: %s' % (
             len(old.encode('utf-8')), hx(old), len(v3.encode('utf-8')), hx(v3), old == v3 or B6._straight(old) == B6._straight(v3)),
         '### PUT metadata (the description v4`s bank, %d bytes, sha256 %s ; %d keys carried) : HTTP %d' % (len(v4.encode('utf-8')), hx(v4), len(md), sp),
         '', '### ### **CALLS 2 ; THE PUT %s ; NO FILE TOUCHED ; NOTHING PUBLISHED.**' % ('ACCEPTED' if sp in (200, 201) else '### REFUSED HTTP %d' % sp)]
    put_txt('b647_zenodo_desc.txt', L)
    _zmerge4(dict(desc=dict(get=st, put=sp, before_bytes=len(old.encode('utf-8')), before_sha256=hx(old), v4_sha256=hx(v4), files_before=files,
                            at=utc())))
    print(NL.join(L[2:]))


def z_read4(*a):
    """data/b647_zenodo_read.txt: the draft read back once -- the description against v4's bank byte for byte, digest for digest and up to quote
    straightening; the file list against the one z_desc4 banked."""
    import hashlib
    import b639_record as R39
    import b646_record as B6
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    d = B6._jx(b) or {}
    md = d.get('metadata') or {}
    bank = open(os.path.join(D, V4), 'rb').read().decode('utf-8')
    back = md.get('description') or ''
    exact = back == bank
    dig = hashlib.sha256(back.encode('utf-8')).hexdigest() == hashlib.sha256(bank.encode('utf-8')).hexdigest()
    fb = (jl(ZRES4).get('desc') or {}).get('files_before') or []
    fa = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    key = lambda x: sorted((f['name'], f['checksum'], f['size']) for f in x)
    files_same = bool(fb) and key(fa) == key(fb)
    L = ['b647 -- THE ROUTE, THE DRAFT READ BACK AFTER THE DESCRIPTION`S REPLACEMENT (%s)' % utc(), '',
         '### GET the draft : HTTP %d ; identifier %s ; state %s ; submitted %s ; title %s ; version %s' % (
             st, d.get('id'), d.get('state'), d.get('submitted'), md.get('title'), md.get('version')),
         '### the description : %d characters back against the bank`s %d ; byte for byte %s ; digest for digest %s ; equal up to quote straightening %s' % (
             len(back), len(bank), exact, dig, B6._straight(back) == B6._straight(bank)),
         '### the files : %d back against %d before the PUT ; name, checksum and size the same %s' % (len(fa), len(fb), files_same), '',
         '### ### **THE DESCRIPTION BYTE FOR BYTE %s AND DIGEST FOR DIGEST %s ; THE FILES UNTOUCHED %s ; THE DRAFT %s SUBMITTED %s -- NOTHING '
         'PUBLISHED.**' % (exact, dig, files_same, d.get('id'), d.get('submitted'))]
    put_txt('b647_zenodo_read.txt', L)
    _zmerge4(dict(read=dict(get=st, id=d.get('id'), state=d.get('state'), submitted=d.get('submitted'), exact=exact, digest=dig,
                            straight=B6._straight(back) == B6._straight(bank), files_same=files_same, n_files=len(fa), at=utc())))
    print(NL.join(L[2:]))


def z_hold4(*a):
    """data/b647_zenodo_hold.txt: the draft HELD, (R257)(4): its state read once and banked; publish is the author's word, no part of this act."""
    import b639_record as R39
    import b646_record as B6
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    d = B6._jx(b) or {}
    L = ['b647 -- THE DRAFT HELD, (R257)(4) (%s)' % utc(), '', '### the draft %s : HTTP %d ; state %s ; submitted %s ; nothing published; v4 sent to '
         'the author as a file (relay data/%s)' % (K.DRAFT, st, d.get('state'), d.get('submitted'), V4)]
    put_txt('b647_zenodo_hold.txt', L)
    _zmerge4(dict(hold=dict(id=K.DRAFT, state=d.get('state'), submitted=d.get('submitted'), at=utc())))
    print(L[-1])


def glossary_cmp(*a):
    """data/b647_glossary_block.txt: the glossary block regenerated by the pages' own builder (tools/chain_page.py glossary_block) from
    relay data/glossary.txt as appended here, against the block each of the two pages and the census at v0.7.1 prints at PLACE-papers main
    before the act, byte for byte: each printed block equal to the block before the append, the new block that block plus the two entries."""
    import tempfile
    import chain_page as CP
    import b638_record as R8
    old = subprocess.run(['git', '-C', RELAY, 'show', '%s:data/glossary.txt' % K.PRE_RELAY], capture_output=True).stdout
    p = os.path.join(tempfile.mkdtemp(), 'glossary_at.txt')
    open(p, 'wb').write(old)
    ob, nb = CP.glossary_block(p), CP.glossary_block()
    docs = [('the zeta page', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'), ('the chi page', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'),
            ('the census at v0.7.1', 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md')]
    added = nb[len(ob):]
    L = ['b647 -- COMPONENT 4, (R257)(4)(a): THE GLOSSARY BLOCK REGENERATED AND COMPARED (%s)' % utc(), '',
         '### the builder: relay tools/chain_page.py glossary_block ; the glossary before: relay %s:data/glossary.txt (%d block lines) ; after: as '
         'appended in this act (%d block lines)' % (K.PRE_RELAY, len(ob), len(nb)),
         '### the new block is the old block plus the appended lines, byte for byte: %s' % (nb[:len(ob)] == ob and len(added) == 2), '']
    ok = nb[:len(ob)] == ob and len(added) == 2
    for name, path in docs:
        t = K.show(path, K.PRE_PP) or ''
        pb = R8.glossary_lines(t)
        same_old = pb == ob
        ok = ok and same_old
        L.append('  %-22s PLACE-papers %s:%s -- %d block lines ; equal to the block before the append, byte for byte: %s ; to the new block: %s '
                 '(the pages and the census reprint at b648, v0.8)' % (name, K.PRE_PP, path, len(pb), same_old, pb == nb))
    L += ['', '### the appended block lines:'] + ['  ' + x for x in added]
    L += ['', '### ### **THE BLOCK %d LINES, WAS %d ; THE THREE PRINTED BLOCKS EQUAL TO THE BLOCK BEFORE, BYTE FOR BYTE: %s ; THE NEW BLOCK THE OLD PLUS '
              'THE TWO ENTRIES: %s.**' % (len(nb), len(ob), 'YES' if ok else '### NO', 'YES' if nb[:len(ob)] == ob and len(added) == 2 else '### NO')]
    put_txt('b647_glossary_block.txt', L)
    print(L[-1])


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b647_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
