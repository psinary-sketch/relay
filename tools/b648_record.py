# -*- coding: utf-8 -*-
"""b648_record.py -- THE ACT'S RECORD TOOL, UNDER (R258). ### ONE SUBCOMMAND PER BANK.

### ### b648: LANE THREE, ACT SEVENTY-FIVE -- THE SORRY LINES CLASSIFIED FOR THE AUTHOR'S WORD; THE TWO PAGES THROUGH THE TABLE AND
### RE-EMITTED; THE KEYSTONE CENSUS AT v0.8; THE h2 ROW; THE RE-CUT ORDER TO THE AUTHOR. Subcommands write only `data/b648_*` unless the
### docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers are b602's, b633's and b641's record tools',
### imported; ledger appends through b566's guarded `append_to`. Written by the Write tool, edited through the Edit tool only. Every bank is LF.
### Every string this tool puts in a ledger is dry-run through the ledger guards (the scanner, the backtick count) before the seal (b647 (o)).
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
import b648_worklist as K  # noqa: E402
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
FACE = 'b648_registration_2026-10-10.txt'
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
    """data/b648_procs.txt: the process listing -- tail, lean, lake and python named, each with its parent and command line -- and the free
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
    L = ['b648 -- COMPONENT 0: THE PROCESS LISTING AT STEP ZERO, tail, lean, lake AND python NAMED (%s)' % utc(), '',
         '### pid / parent / parent state / name / command line (this tool`s own python process left out, pid %d)' % me]
    L += ['  ' + l[:400] for l in rows] or ['  ### NONE: no tail, lean, lake or python process is running']
    L += ['', '### orphans: %s ; stopped by PID: %s' % (len(orph) if orph else 'NONE', 'none needed' if not stopped else len(stopped))] + stopped
    L += ['### free memory: %s MB ; the hold %d MB' % (free.group(1) if free else '?', K.HOLD)]
    put_txt('b648_procs.txt', L)
    print(NL.join(L[3:]))


def stepzero(*a):
    """data/b648_stepzero.txt: the branch deletions read back (relay and PLACE-papers, push-b647* listed by --merged and deleted by name in the
    commands the capture holds), the untracked banks by git status and git log, the free memory before any build."""
    import build_watch as BW
    lines = []
    for repo, name in ((RELAY, 'relay'), (PP, 'PLACE-papers')):
        lines.append('  %-13s push-b647* branches now: %s' % (name, g(repo, 'branch', '--list', 'push-b647*').strip() or 'NONE'))
    for p in (K.LOCAL_BANK, K.EXPORT):
        st = g(RELAY, 'status', '--porcelain', '--', p).strip()
        lg = g(RELAY, 'log', '--all', '--format=%h', '--', p).strip()
        idx = g(RELAY, 'ls-files', '--', p).strip()
        lines.append('  %-42s status %s ; in a commit %s ; in the index %s' % (p, st or '(clean)', lg or 'NONE', idx or 'NO'))
    L = ['b648 -- COMPONENT 0: THE BRANCHES, THE UNTRACKED BANKS AND THE FREE MEMORY AT STEP ZERO (%s)' % utc(), '',
         '### the b647 push branches, listed by `git branch --merged main` and deleted by name with the lower-case flag (relay push-b647, '
         'push-b647-closing, push-b647-root; PLACE-papers push-b647, push-b647-root), read back:'] + lines[:2] + [
        '', '### the banks that stay untracked (b628`s local intake bank; the navigator`s export):'] + lines[2:] + [
        '', '### free memory before any build: %d MB ; the hold %d MB' % (BW.free_mb(), K.HOLD)]
    put_txt('b648_stepzero.txt', L)
    print(NL.join(L[2:]))


def answers(*a):
    """data/b648_author_answers.txt: every prompt put by the seat in this act, from the ruling's delivery (and any continuation session from its
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
    head = ['### b648 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; the sessions read: %s.' % (n, DATE, ', '.join('%s from %r' % (s[:8], an) for s, _, an in srcs)), '']
    put_txt('b648_author_answers.txt', head + (L or ['### NONE: no prompt has been put to the author in this act.']))
    print('  prompts banked: %d' % n)


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in SESSIONS_AFTER:
        rows += ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc, 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


def commands(*a):
    """data/b648_commands.txt and .json: the act's command bank -- every Bash and PowerShell command of the seat's session from the ruling's
    delivery (K.ANCHOR) onward and its helper readers' -- each with the arm G-EDIT-ROUTE's reading (tools/edit_route.py)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % K.ANCHOR)
    hits = ER.scan(rows)
    L = ['b648 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING ((R256)(2); tools/edit_route.py) (%s)' % utc(), '',
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
    put_txt('b648_commands.txt', L)
    put_json('b648_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R258)(1), (2)
B647_ENTRY = 8123        # ### FINDINGS: b647's entry
RULE_LINE = 11508        # ### OPEN_TRAILS: the first ledger line carrying "no `sorry` on any `main`" (b559, 2026-09-29)
W_HEAD = '*Appended 2026-10-10 by b648 to b647’s entry (:%d), under `(R258)`(1) -- b647 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
S_HEAD = ('*Appended 2026-10-10 by b648 to the b559 record (:%d), under `(R258)`(2) -- THE STANDING RULE REFUTED AT THIRTY-SEVEN LINES ON KERNEL '
          'MAINS, EACH WITH THE DATE IT ENTERED:*')


def _need(pat, text, what):
    m = re.search(pat, text, re.M)
    if not m:
        sys.exit('### %s NOT FOUND -- NOTHING WRITTEN' % what)
    return m


def sorry_lines():
    """the 37 sorry lines in code from relay data/b647_sorry_census.json, each with the commit that brought its line (git blame at the main,
    then git log): [(kernel, main, file, line, built, sha, date, subject, text)]."""
    c = jl('b647_sorry_census.json')
    out = []
    for k, v in c['kernels'].items():
        for h in v['hits']:
            if h.get('kind') != 'code':
                continue
            rp = 'D:/' + k
            b = g(rp, 'blame', '-L', '%d,%d' % (h['line'], h['line']), '--porcelain', v['main'], '--', h['file'])
            s = b.split()[0] if b.strip() else ''
            lg = g(rp, 'log', '-1', '--format=%h|%cs|%s', s).strip().split('|', 2) if s else ['?', '?', '?']
            out.append((k, v['main'], h['file'], h['line'], bool(h.get('built')), lg[0], lg[1], lg[2], h.get('text', '').strip()))
    return out


def _weight():
    c = rd('b647_closing.txt')
    h = _need(r'^b647 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts? answered; (\d+) defects', c,
              'b647`s closing head line')
    kj = jl('b647_table_kernels.json')
    t = kj.get('totals') or {}
    ks = kj.get('kernels') or []
    miss = sum(x.get('missed', 0) for x in ks)
    gm = sum(x.get('generated_matches', 0) for x in ks)
    cl = dict((x, sum((y.get('classes') or {}).get(x, 0) for y in ks)) for x in 'SAH')
    nav = jl('b647_table_navigator_memory.json')
    nc = nav.get('counts') or {}
    dj, cp = jl('b647_deposit_description.json'), jl('b647_reader_d5_compare.json')
    cols = jl('b647_census_columns.json').get('rows') or []
    sc = jl('b647_scores.json')
    nd = len(re.findall(r'^    \([a-z]\) ', rd('b647_defects.txt'), re.M))
    act = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b647 --', PRE_RELAY).strip()[:8]
    seal = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b647 seal', PRE_RELAY).strip()[:8]
    nn = sum(1 for r in nav.get('rows') or [] if r['verdict'] != 'MATCHES')
    if (kj.get('rows'), t.get('MATCHES'), t.get('OVERREACHES')) != (3804, 3516, 266) or len(nav.get('rows') or []) != 163:
        sys.exit('### b647`S BANKS DO NOT READ AS EXPECTED -- NOTHING WRITTEN')
    sco = ', '.join('%s %s' % (k, (sc.get(k) or ['?'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5'))
    return ('\n%s relay %s (closing), %s (act), %s (seal), PLACE-papers %s; the suite %s of %s, NOT CLEAN on G-EDIT-ROUTE alone, declared on '
            'the face; the root %s…; %s prompt answered; %d defects, (a) to (p). Every kernel`s docstrings: 22 kernels, %d rows -- MATCHES %d, '
            'UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d -- the textual kernels read whole by helper readers on the author`s answer and every '
            'non-MATCHES row read whole by the seat; the generated rule`s verdict kept beside each row, its misses %d of the %d rows it read '
            'MATCHES; the three classes it cannot see counted, a sorry-closed theorem described as holding %d, an axiom-profile claim against a '
            'banked print %d, a module header claiming more than its file compiles %d; every sorry on every kernel`s main printed by file and '
            'line, 37 in code in three kernels, 4 inside a built library. The navigator`s memory at %d rows -- MATCHES %d, UNDERSTATES %d, '
            'OVERREACHES %d, UNLICENSED %d -- four row units redacted in the bank for a location or a label outside the corpus. The description '
            'at v4, %s bytes against v3`s %s, the fifth reader %s of 3 by the needles and %s of 3 by hand, the residue six passages, the draft`s '
            'description replaced, read back and held. The watchdog on the process tree. The census columns over %d rows. %s. `(R258)`(1) '
            'gives the navigator`s memory at 128 rows -- MATCHES 104, OVERREACHES 22, UNDERSTATES 2 -- and `(R258)`(8) its repairs at 24 rows, '
            'figures from a report the seat sent before the last of the seven readings landed; the banks print %d rows and %d non-MATCHES '
            'rows: the navigator`s, the banks’ figures standing. Nothing deposited; no edition touched.\n' % (
                W_HEAD % B647_ENTRY, PRE_RELAY, act, seal, h.group(2), h.group(3), h.group(4), h.group(5)[:8], h.group(6), nd,
                kj.get('rows'), t.get('MATCHES', 0), t.get('UNDERSTATES', 0), t.get('OVERREACHES', 0), t.get('UNLICENSED', 0), miss, gm,
                cl['S'], cl['A'], cl['H'], len(nav.get('rows') or []), nc.get('MATCHES', 0), nc.get('UNDERSTATES', 0), nc.get('OVERREACHES', 0),
                nc.get('UNLICENSED', 0), dj.get('bytes'), dj.get('v3_bytes'), cp.get('needles'), cp.get('hand'), len(cols), sco,
                len(nav.get('rows') or []), nn))


def _breach():
    sl = sorry_lines()
    if len(sl) != 37 or sum(1 for x in sl if x[4]) != 4:
        sys.exit('### THE SORRY LINES DO NOT READ 37 WITH 4 BUILT -- NOTHING WRITTEN')
    rule_date = '2026-09-29'
    before = sum(1 for x in sl if x[6] < rule_date)
    L = ['', S_HEAD % RULE_LINE + ' the standing line "no `sorry` on any `main`" first stands in this ledger at :%d (b559, %s); the census of '
         'b647 (relay data/b647_sorry_census.txt) found 37 `sorry` lines in code on the mains of three kernels, 4 of them inside a built library. '
         'Each line below carries its kernel and main, its file and line, BUILT or TRACKED ONLY, and the commit that brought the line '
         '(git blame at the main, then git log): %d of the 37 entered before the rule`s first line, %d after. Each takes one repair by the '
         'author`s word under `(R258)`(2) -- PROVED, QUARANTINED or RESTATED -- raised as one prompt before any kernel edit.' % (
             RULE_LINE, rule_date, before, 37 - before)]
    for k, m, f, ln, built, s, d, subj, _t in sl:
        L.append('- %s %s `%s` :%d -- %s; entered %s at `%s`%s' % (k, m, f, ln, 'BUILT' if built else 'TRACKED ONLY', d, s,
                                                                   ' -- **inside a built library**' if built else ''))
    return NL.join(L) + NL


def record_lines(*a):
    """Component 1, (R258)(1), (2): FINDINGS, b647 at its weight (to :8123); OPEN_TRAILS, the sorry breach beneath the rule`s first line (:11508)."""
    import b641_record as R41
    Q = R2._Q()
    if not (Q.line_of(Q.FIND, '## Every kernel’s docstrings at 3804 rows') == B647_ENTRY):
        sys.exit('### b647`S ENTRY MOVED -- NOTHING WRITTEN')
    if 'no `sorry` on any `main`' not in lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), ''))[RULE_LINE - 1]:
        sys.exit('### THE RULE`S LINE MOVED -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % B647_ENTRY, R41._poss(_weight())), ('OPEN_TRAILS.md', S_HEAD % RULE_LINE, R41._poss(_breach()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if DRY else D, 'b648_scanfile_lines.md')
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
    R3._land(Q, items, 'b648_record_lines.json', B647_ENTRY)


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b648_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
