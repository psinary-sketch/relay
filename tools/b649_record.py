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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b649_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
