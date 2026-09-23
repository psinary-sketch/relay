# -*- coding: utf-8 -*-
"""b498_components.py -- THE THREE COMPONENTS, EACH RUN AS ITS OWN STEP.

### `python tools/b498_components.py c1|c2|c3|assemble`
### ### **EACH STEP BANKS ITS OWN SECTION AND MERGES ITS CELLS INTO `b498_results.json`**, so a step
### that is interrupted leaves the steps before it banked and the steps after it visibly absent.
### ### **THE LAUNCH LOG IS WRITTEN BY THE LAUNCHED PROCESS AND NEVER OPENED HERE.**
"""
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
TRANSCRIPT = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--',
                          '49943484-5ff3-4a99-9f75-0f3a8ae0d39a.jsonl')
B495_LOG = os.path.join(D, 'b495_ef_build.log')
RESULTS = os.path.join(D, 'b498_results.json')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    with open(p, 'rb') as fh:
        return fh.read().decode('utf-8', 'replace').replace(chr(13), '')


def merge(cells):
    R = json.loads(read(RESULTS)) if os.path.exists(RESULTS) else {}
    R.update(cells)
    io.open(RESULTS, 'w', encoding='utf-8', newline=NL).write(
        json.dumps(R, indent=1, ensure_ascii=False) + NL)


def bank(name):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % name)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def utc(s):
    return datetime.strptime(s[:23], '%Y-%m-%dT%H:%M:%S.%f').replace(tzinfo=timezone.utc)


# ================================================================================================ c1
def c1():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE CAUSE, BANKED. ### **WHAT THE RECORD SHOWS, AND WHERE IT DOES NOT, SAID SO.**')
    rec('=' * 104)

    # ---------------------------------------------------------------- (a) the launcher`s flags
    push = read(os.path.join(T, 'b495_push.py'))
    launch = read(os.path.join(T, 'b495_launch.py'))
    fl = [l.strip() for l in push.split(NL) if re.match(r'\s*flags\s*=\s*subprocess\.', l)]
    pop = push[push.index('p = subprocess.Popen([sys.executable, launcher]'):]
    pop = pop[:pop.index(')') + 1]
    group = any('CREATE_NEW_PROCESS_GROUP' in l for l in fl)
    detached = any('DETACHED_PROCESS' in l for l in fl)
    newcons = any('CREATE_NEW_CONSOLE' in l for l in fl)
    devnull = all(k in pop for k in ('stdin=subprocess.DEVNULL', 'stdout=subprocess.DEVNULL',
                                     'stderr=subprocess.DEVNULL'))
    child_flags = [l.strip() for l in launch.split(NL) if 'creationflags' in l and not l.strip().startswith('#')]
    rec('')
    rec('### (a) THE PROCESS GROUP AND THE CONSOLE. ### **READ FROM b495`S OWN CODE.**')
    rec('-' * 104)
    rec('    `tools/b495_push.py`, the flags line : %s' % (fl[0] if fl else '### NOT FOUND'))
    rec('    the Popen of the launcher            : %s' % re.sub(r'\s+', ' ', pop))
    rec('      CREATE_NEW_PROCESS_GROUP : ### **%s**' % group)
    rec('      DETACHED_PROCESS         : ### **%s**' % detached)
    rec('      CREATE_NEW_CONSOLE       : ### **%s**' % newcons)
    rec('      std handles all DEVNULL  : %s' % devnull)
    rec('    `tools/b495_launch.py`, creation flags on its own `lake` / `lean` Popen : ### **%s**'
        % (child_flags or 'NONE'))
    rec('    ### ### **WHAT THE RECORD SHOWS:** ### the launcher was created in ### **ITS OWN PROCESS')
    rec('    ### GROUP, NOT THE SEAT`S**, and ### **WITH NO CONSOLE AT ALL, SO NOT THE SEAT`S')
    rec('    ### CONSOLE EITHER.** ### It started `lake` and `lean` with no creation flags.')
    rec('    ### ### **WHAT FOLLOWS FROM WINDOWS` DOCUMENTED BEHAVIOUR, NOT FROM THE RECORD:** ### a')
    rec('    ### console program started by a parent that has no console, without')
    rec('    ### `DETACHED_PROCESS` or `CREATE_NO_WINDOW`, is given a NEW console of its own. ### So')
    rec('    ### `lake` ran in a console of its own, and the probe`s `lake env lean` in another.')
    rec('    ### **THE RECORD DOES NOT SHOW THOSE CONSOLES**: nothing banked says a window was drawn,')
    rec('    ### where, or whether anyone saw it.')

    # ---------------------------------------------------------------- (b) the instants
    log = read(B495_LOG)
    lines = [l for l in log.split(NL) if l[:4] == '2026']
    ends = [(l[:23], int(re.search(r'EXIT (-?\d+)', l).group(1)), re.search(r'END (.+?)\*\*', l).group(1))
            for l in lines if '### **END ' in l]
    begins = [(l[:23], re.search(r'BEGIN (.+?)\*\*', l).group(1)) for l in lines if '### **BEGIN ' in l]
    last = lines[-1][:23]
    rec('')
    rec('### (b) THE INSTANTS, FROM THE LOG`S OWN STAMPS (UTC, `time.gmtime`).')
    rec('-' * 104)
    for t, what in begins:
        rec('    BEGIN %-34s %s' % (what, t))
    for t, code, what in ends:
        rec('    END   %-34s %s   EXIT %d = 0x%08X' % (what, t, code, code & 0xFFFFFFFF))
    rec('    the launcher`s own last line                 %s' % last)
    survived = bool(ends) and last >= max(t for t, _, _ in ends) and 'BUILD EXIT' in lines[-1]
    rec('    ### ### **THE LAUNCHER SURVIVED BOTH EVENTS : %s** ### -- it wrote both `END` lines and'
        % survived)
    rec('    ### its own closing line after them. ### **WHAT WAS KILLED WAS WHAT RAN IN THE CHILD')
    rec('    ### CONSOLES; THE PROCESS THAT HAD NO CONSOLE WAS NOT TOUCHED.**')
    all_ctrlc = all(code == 3221225786 for _, code, _ in ends)
    rec('    both exits `0xC000013A` = STATUS_CONTROL_C_EXIT : %s' % all_ctrlc)

    # ---------------------------------------------------------------- (c) the clocks
    off = git(ROOT, 'log', '-1', '--format=%cI', 'dae85c5')[-6:]
    sign = -1 if off[0] == '-' else 1
    tz = timezone(sign * timedelta(hours=int(off[1:3]), minutes=int(off[4:6])))
    kill1 = utc(ends[0][0]) if ends else None
    rec('')
    rec('### (c) THE ORDER`S 15:02, IN BOTH CLOCKS.')
    rec('-' * 104)
    rec('    local offset, read off b495`s closing commit `dae85c5` : %s' % off)
    for t, code, what in ends:
        rec('    %-36s UTC %s = local %s' % (what, t[11:], utc(t).astimezone(tz).strftime('%H:%M:%S.%f')[:12]))
    w_local = datetime(2026, 9, 23, 15, 2, tzinfo=tz)
    w_utc = datetime(2026, 9, 23, 15, 2, tzinfo=timezone.utc)
    start = utc(lines[0][:23])
    rec('    15:02 read as LOCAL = %s UTC : the first kill is ### **%s** it'
        % (w_local.astimezone(timezone.utc).strftime('%H:%M'),
           'AT OR BEFORE' if kill1 <= w_local else 'AFTER'))
    rec('    15:02 read as UTC   = %s local : the build`s first mark is %s it -- ### **THE BUILD HAD'
        % (w_utc.astimezone(tz).strftime('%H:%M'), 'AFTER' if start > w_utc else 'BEFORE'))
    rec('    ### NOT STARTED BY THEN**, so on that reading no event before 15:02 could reach it.')
    rec('    ### ### **THE LOG`S KILL IS AT %s LOCAL; 15:02 LOCAL IS b496`S CLOSING (15:01:32).** ### The'
        % kill1.astimezone(tz).strftime('%H:%M:%S'))
    rec('    ### window the order names contains the kill on the local reading, and the kill is 44')
    rec('    ### minutes earlier than its bound. ### **THE ORDER`S BOUND IS HONOURED, NOT TIGHTENED.**')

    # ---------------------------------------------------------------- (d) the seat`s shell
    ev = []
    with io.open(TRANSCRIPT, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            try:
                o = json.loads(line)
            except Exception:
                continue
            ts = o.get('timestamp', '')
            if not ('2026-09-23T17:58' <= ts <= '2026-09-23T19:03'):
                continue
            kind = o.get('type')
            sub = o.get('subtype', '')
            tool = ''
            m = o.get('message')
            if isinstance(m, dict) and isinstance(m.get('content'), list):
                for b in m['content']:
                    if isinstance(b, dict) and b.get('type') == 'tool_use':
                        tool = (b.get('name') or '') + ' ' + json.dumps(b.get('input'))[:90]
            ev.append((ts, kind, sub, tool))
    ev.sort()
    tools_before = [e for e in ev if e[3] and e[0] < ends[0][0] + 'Z']
    lastcall = tools_before[-1] if tools_before else None
    turn_end = [e for e in ev if e[2] == 'turn_duration' and e[0] < ends[0][0] + 'Z']
    te = turn_end[-1][0] if turn_end else None
    after = [e for e in ev if e[0] > ends[-1][0] + 'Z']
    nxt = after[0] if after else None
    in_window = [e for e in ev if ends[0][0] + 'Z' >= e[0] >= (te or '')] if te else []
    rec('')
    rec('### (d) THE SEAT`S SHELL, FROM THE SEAT`S OWN SESSION TRANSCRIPT.')
    rec('-' * 104)
    rec('    transcript : %s' % os.path.basename(TRANSCRIPT))
    rec('    events read between the build`s first mark and 15:02 local : %d' % len(ev))
    rec('    tool calls by the seat in that window, before the first kill : %d' % len(tools_before))
    if lastcall:
        rec('    the LAST of them : %s  %s' % (lastcall[0], lastcall[3]))
    rec('    ### ### **THE SEAT`S b495 TURN ENDS : %s**' % te)
    d1 = (kill1 - datetime.strptime(te, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)).total_seconds() if te else None
    rec('    ### ### **THE FIRST KILL FOLLOWS IT BY %.3f s**' % d1 if d1 is not None else '    ### turn end NOT FOUND')
    rec('    events between the turn end and the first kill : %d %s' % (len(in_window) - 1 if in_window else 0, ''))
    rec('    the next event after the second kill : %s %s %s' % (nxt[0], nxt[1], nxt[2]) if nxt else '    none')
    rec('    tool calls by the seat at either kill instant : ### **0**' if not any(
        e[3] and (e[0][:19] == ends[0][0][:19] or e[0][:19] == ends[-1][0][:19]) for e in ev)
        else '    ### A TOOL CALL AT A KILL INSTANT -- PRINTED ABOVE')
    rec('    ### ### **WHAT THE RECORD SHOWS:** ### (1) the build shared ### **NEITHER THE SEAT`S')
    rec('    ### PROCESS GROUP NOR ITS CONSOLE**; (2) the seat made ### **NO TOOL CALL** in the %.1f s'
        % (kill1 - utc(lastcall[0][:23])).total_seconds() if lastcall else '    ### (2) no tool call found')
    rec('    ### before the first kill, nor at either kill; (3) the one event of the seat`s session')
    rec('    ### close before the kill is ### **THE END OF THE b495 TURN, %.3f s EARLIER.**' % (d1 or 0))
    rec('    ### ### **WHAT THE RECORD DOES NOT SHOW:** ### ### **WHO OR WHAT SENT THE CONSOLE')
    rec('    ### CONTROL EVENT.** ### Nothing banked names a sender. ### A console control event')
    rec('    ### reaches the processes attached to ONE console; the seat`s shell was attached to')
    rec('    ### none of the build`s, so ### **NO EVENT OF THE SEAT`S SHELL IN THE RECORD HAS A PATH')
    rec('    ### TO THEM** -- that is Windows` documented behaviour applied to the flags in (a), not')
    rec('    ### a finding. ### Closing a console window delivers `CTRL_CLOSE_EVENT` to what runs in')
    rec('    ### it, and the two kills %.1f s apart fall on the two separate child consoles; ### **THAT'
        % (utc(ends[-1][0]) - utc(ends[0][0])).total_seconds())
    rec('    ### IS CONSISTENT WITH A WINDOW BEING CLOSED, AND IT IS NOT EVIDENCE THAT ONE WAS.**')
    rec('    ### ### **THE SENDER STAYS NOT ESTABLISHED.** ### This act does not guess, and the')
    rec('    ### launch in Component 3 is built so that the one console it creates is TITLED and')
    rec('    ### MINIMISED rather than several untitled ones appearing unannounced.')
    rec('=' * 104)

    merge(dict(c1=dict(
        flags_line=fl[0] if fl else None, new_group=group, detached=detached, new_console=newcons,
        std_devnull=devnull, child_flags=child_flags, ends=[dict(t=t, exit=c, what=w) for t, c, w in ends],
        launcher_last=last, launcher_survived=survived, all_ctrl_c=all_ctrlc, local_offset=off,
        turn_end=te, kill_after_turn_end_s=d1, tools_in_window=len(tools_before),
        last_tool_call=lastcall[0] if lastcall else None,
        sender='NOT ESTABLISHED')))
    bank('b498_components_c1.txt')


# ================================================================================================ c2
def modules():
    root = os.path.join(KERNEL, 'Zeta23')
    out = []
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f.endswith('.lean'):
                out.append(os.path.join(dp, f))
    return sorted(out)


def imports_of(path):
    """### ### **EVERY `import` LINE OF THE FILE, NOT JUST THE LEADING BLOCK.** ### b495`s parser
    ### stopped at the first non-import line -- the licence header -- and returned ONE module."""
    out = []
    for l in read(path).split(NL):
        m = re.match(r'^\s*import\s+(.+?)\s*$', l)
        if m:
            out += m.group(1).split()
    return out


def c2():
    rec('=' * 104)
    rec('COMPONENT 2 -- THE CACHE, AND MATHLIB`S CLOSURE, TIMED.')
    rec('=' * 104)
    rec('')
    rec('### (a) `lake exe cache get`, in `%s`.' % KERNEL)
    rec('-' * 104)
    t0 = time.time()
    p = subprocess.run(['lake', 'exe', 'cache', 'get'], cwd=KERNEL, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    dt = time.time() - t0
    raw = (p.stdout or '') + (p.stderr or '')
    io.open(os.path.join(D, 'b498_cache_get.txt'), 'w', encoding='utf-8', newline=NL).write(
        raw.replace(chr(13), ''))
    rec('    ### ### **EXIT : %d** ; wall %.1f s ; output %d lines, banked WHOLE at `b498_cache_get.txt`'
        % (p.returncode, dt, len(raw.splitlines())))
    # ### ### **THE COUNT IS PARSED FROM THE TOOL`S OWN LINE, AND THE LINE IS PRINTED BESIDE IT.**
    cands = [l.strip() for l in raw.replace(chr(13), NL).split(NL)
             if re.search(r'download|decompress|unpack|file\(s\)|files|No files|Completed|attempt',
                          l, re.I)]
    for l in cands[-12:]:
        rec('      | %s' % l[:150])
    fetched = None
    m = None
    for l in cands:
        m = re.search(r'Downloaded:?\s*([\d,]+)\s*file', l, re.I) or m
    if m:
        fetched = int(m.group(1).replace(',', ''))
    elif any(re.search(r'No files to download', l, re.I) for l in cands):
        fetched = 0
    # ### ### **THE LINE PRINTED IS THE LINE THE COUNT WAS PARSED FROM** -- the LAST `Downloaded`
    # ### line. ### The first version printed the FIRST (`Downloaded: 1 file(s)`) beside a count
    # ### taken from the last, and `G-FETCH-COUNT-FROM-LINE` was written to catch exactly that.
    fline = ([l for l in cands if re.search(r'Downloaded:?\s*[\d,]+\s*file', l, re.I)] or [None])[-1]
    rec('    ### ### **FILES FETCHED : %s**' % (fetched if fetched is not None else 'NOT FOUND'))
    rec('      from the line : %s' % (fline or '(no `Downloaded` line printed)'))
    avail = (p.returncode == 0)
    cells = dict(cache_exit=p.returncode, cache_wall=dt, fetched=fetched, fetched_line=fline,
                 cache_available=avail)

    rec('')
    rec('### (b) MATHLIB`S CLOSURE NEEDED BY THE VENDORED LIBRARY. ### **COMPUTED, NOT RECALLED.**')
    rec('-' * 104)
    mods = modules()
    ext = sorted(set(i for f in mods for i in imports_of(f) if i.startswith('Mathlib')))
    other = sorted(set(i for f in mods for i in imports_of(f)
                       if not i.startswith('Mathlib') and not i.startswith('Zeta23')))
    rec('    vendored `.lean` files under `Zeta23/` : %d' % len(mods))
    rec('    distinct external `Mathlib.*` imports  : ### **%d**' % len(ext))
    rec('    imports neither Mathlib nor Zeta23     : %s' % (other or 'NONE'))
    cells.update(vendored=len(mods), closure_roots=ext, other_imports=other)
    if not avail:
        # ### ### **(R109)(2)`S FALLBACK, OBEYED.**
        b491 = read(os.path.join(D, 'b491_components.txt'))
        ln = next((l.strip() for l in b491.split(NL) if 'start to `RUN COMPLETE`' in l), '### NOT FOUND')
        rec('    ### ### **THE CACHE IS UNAVAILABLE AT THE PINNED MATHLIB COMMIT.** ### The closure build')
        rec('    ### is NOT run in the foreground; the launch still runs detached.')
        rec('    ### ### **HOW LONG b475`S TOOK**, read from b491`s bank of it : %s' % ln)
        cells.update(closure_run=False, b475_line=ln)
    else:
        t0 = time.time()
        q = subprocess.run(['lake', 'build'] + ext, cwd=KERNEL, capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        dt2 = time.time() - t0
        out = ((q.stdout or '') + (q.stderr or '')).replace(chr(13), '')
        io.open(os.path.join(D, 'b498_closure_build.txt'), 'w', encoding='utf-8', newline=NL).write(out)
        built = [l for l in out.split(NL) if re.search(r'\bBuilt Mathlib\.', l)]
        built_other = [l for l in out.split(NL) if re.search(r'\bBuilt (?!Mathlib\.)', l)]
        replayed = [l for l in out.split(NL) if re.search(r'\bReplayed Mathlib\.', l)]
        errs = [l for l in out.split(NL) if re.search(r'^\s*error|✖', l)]
        rec('    `lake build` on the %d roots : ### **EXIT %d** ; ### **WALL %.1f s** ; output banked WHOLE'
            % (len(ext), q.returncode, dt2))
        rec('      at `b498_closure_build.txt`, %d lines' % len(out.split(NL)))
        rec('    ### ### **LINES READING `Built Mathlib.` : %d**' % len(built))
        for l in built[:40]:
            rec('      | %s' % l.strip()[:140])
        rec('    lines reading `Replayed Mathlib.` : %d ### -- replayed is NOT compiled' % len(replayed))
        rec('    lines reading `Built` for anything else : %d' % len(built_other))
        rec('    error lines : %d' % len(errs))
        for l in errs[:10]:
            rec('      | %s' % l.strip()[:140])
        cells.update(closure_run=True, closure_exit=q.returncode, closure_wall=dt2,
                     built_mathlib=len(built), replayed_mathlib=len(replayed),
                     built_other=len(built_other), closure_errors=len(errs))

    rec('')
    rec('### (c) THE KERNEL`S TRACKED TREE, AFTER.')
    rec('-' * 104)
    st = git(KERNEL, 'status', '--porcelain')
    rec('    `git status --porcelain` : ### **%s**' % (repr(st) if st else 'EMPTY'))
    rec('    HEAD : %s' % git(KERNEL, 'rev-parse', '--short', 'HEAD'))
    cells.update(kernel_status=st, kernel_head=git(KERNEL, 'rev-parse', 'HEAD'))
    rec('=' * 104)
    merge(dict(c2=cells))
    bank('b498_components_c2.txt')


# ================================================================================================ c3
def c3():
    rec('=' * 104)
    rec('COMPONENT 3 -- THE LAUNCH. ### **A NEW PROCESS GROUP AND A NEW CONSOLE; NOT DETACHED_PROCESS.**')
    rec('=' * 104)
    launcher = os.path.join(T, 'b498_launch.py')
    CREATE_NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
    CREATE_NEW_PROCESS_GROUP = subprocess.CREATE_NEW_PROCESS_GROUP
    flags = CREATE_NEW_CONSOLE | CREATE_NEW_PROCESS_GROUP
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = 7            # ### SW_SHOWMINNOACTIVE: minimised, and it does not take focus
    p = subprocess.Popen([sys.executable, launcher], cwd=KERNEL, creationflags=flags,
                         startupinfo=si, close_fds=True)
    log = os.path.join(D, 'b498_ef_build.log')
    names = [n for n, v in (('CREATE_NEW_CONSOLE', CREATE_NEW_CONSOLE),
                            ('CREATE_NEW_PROCESS_GROUP', CREATE_NEW_PROCESS_GROUP),
                            ('DETACHED_PROCESS', 0x00000008)) if flags & v]
    rec('')
    rec('    launcher : `tools/b498_launch.py`')
    rec('    ### ### **pid : %d**' % p.pid)
    rec('    ### ### **creation flags : 0x%08X = %s**' % (flags, ' | '.join(names)))
    rec('      CREATE_NEW_CONSOLE       = 0x%08X : %s' % (CREATE_NEW_CONSOLE, bool(flags & CREATE_NEW_CONSOLE)))
    rec('      CREATE_NEW_PROCESS_GROUP = 0x%08X : %s' % (CREATE_NEW_PROCESS_GROUP, bool(flags & CREATE_NEW_PROCESS_GROUP)))
    rec('      DETACHED_PROCESS         = 0x%08X : %s' % (0x8, bool(flags & 0x8)))
    rec('    startup : STARTF_USESHOWWINDOW, wShowWindow 7 = SW_SHOWMINNOACTIVE (minimised, no focus)')
    rec('    ### ### **log : %s**' % os.path.relpath(log, ROOT).replace(os.sep, '/'))
    rec('    ### `lake build`, then PrintAxioms on `EF_lit_zetaZeroConfig`, `EF_lit`, `EF_lit_zeta`,')
    rec('    ### each line stamped with ### **AN INSTANT TAKEN AT THAT LINE.**')
    rec('    ### ### **THE LOG IS NOT READ IN THIS ACT.** ### The act after reads it behind b497`s gate.')
    rec('=' * 104)
    merge(dict(c3=dict(pid=p.pid, flags=flags, flag_names=names,
                       new_group=bool(flags & CREATE_NEW_PROCESS_GROUP),
                       new_console=bool(flags & CREATE_NEW_CONSOLE),
                       detached=bool(flags & 0x8), show=7,
                       log=os.path.relpath(log, ROOT).replace(os.sep, '/'),
                       launched_utc=datetime.now(timezone.utc).isoformat())))
    bank('b498_components_c3.txt')


def assemble():
    parts = []
    for n in ('c1', 'c2', 'c2_reparse', 'c3'):
        p = os.path.join(D, 'b498_components_%s.txt' % n)
        parts.append(read(p) if os.path.exists(p) else '### COMPONENT %s NOT RUN' % n[1] + NL)
    io.open(os.path.join(D, 'b498_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(parts))
    print('  written: b498_components.txt')


def c2reparse():
    """### ### **RE-DERIVE (a)`S COUNT AND ITS LINE FROM THE BANKED RAW OUTPUT, WITHOUT RE-RUNNING.**
    ### The first c2 bank is KEPT as written, beside this correction."""
    raw = read(os.path.join(D, 'b498_cache_get.txt'))
    cands = [l.strip() for l in raw.replace(chr(13), NL).split(NL)
             if re.search(r'Downloaded:?\s*[\d,]+\s*file', l, re.I)]
    # ### ### **ANSI ESCAPES STRIPPED**: the tool`s progress line carries `ESC[K`, and the first
    # ### trail append wrote that control byte into OPEN_TRAILS.md before this repair.
    cands = [re.sub(chr(27) + r'\[[0-9;]*[A-Za-z]', '', l) for l in cands]
    fline = cands[-1] if cands else None
    m = re.search(r'Downloaded:?\s*([\d,]+)\s*file', fline or '', re.I)
    fetched = int(m.group(1).replace(',', '')) if m else None
    att = next((l.strip() for l in raw.split(NL) if l.startswith('Attempting to download')), None)
    esc = raw.count(chr(27))
    dec = next((l.strip() for l in raw.split(NL) if re.match(r'Decompressed \d+ file', l)), None)
    rec('=' * 104)
    rec('COMPONENT 2 (a), RE-DERIVED FROM THE BANKED RAW OUTPUT. ### **THE FIRST PRINT PAIRED THE WRONG LINE.**')
    rec('=' * 104)
    rec('    ### the first c2 run printed the FIRST `Downloaded` line beside a count parsed from the LAST.')
    rec('    ### The count was right; the line beside it was not. ### Nothing was re-downloaded.')
    rec('    ### ### **FILES FETCHED : %s**' % fetched)
    rec('      from the line : %s' % fline)
    rec('      the tool`s own plan line : %s' % att)
    rec('      the tool`s own finish line : %s' % dec)
    rec('    ### ESC bytes in the raw output : %d -- stripped from the printed line, kept in the raw bank' % esc)
    rec('=' * 104)
    R = json.loads(read(RESULTS))
    R['c2'].update(fetched=fetched, fetched_line=fline, attempt_line=att, decompressed_line=dec,
                   fetched_line_repaired=True)
    io.open(RESULTS, 'w', encoding='utf-8', newline=NL).write(json.dumps(R, indent=1, ensure_ascii=False) + NL)
    bank('b498_components_c2_reparse.txt')


if __name__ == '__main__':
    {'c1': c1, 'c2': c2, 'c3': c3, 'c2reparse': c2reparse, 'assemble': assemble}[sys.argv[1]]()
