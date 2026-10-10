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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b647_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
