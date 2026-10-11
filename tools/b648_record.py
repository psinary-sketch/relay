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
                    if op.get('preview'):   # ### b648: an option's preview is part of the option, banked verbatim beneath it
                        L += ['    PREVIEW | ' + x for x in op['preview'].split(NL)]
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


# ================================================================================ COMPONENT 2: THE SORRY CLASSIFICATION, (R258)(2)
# ### Each of the 37 lines read whole with the declaration it closes and the files of its kernel naming that declaration (git grep -w at the
# ### main); the classification PROPOSED per line with one reason; raised as one prompt; no kernel edit before the author's word.
BUILT_LIB_NOTE = {
    'SIDE-kernel': 'outside every lean_lib (lakefile.lean: Kernel, Bridge, MetaKernel); a probe or a superseded build attempt',
    'SIDE-effects': 'inside lean_lib SIDEEffects (Milestones imported by the root)',
    'SIDE-lv-conservation': 'T3_StepNineBridge inside lean_lib SIDELvConservation; PinnedGoal.lean outside every lean_lib'}
DECL = re.compile(r'^\s*(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|example|instance|abbrev)\b\s*([^\s:(\[{]*)')
# ### the seat's reason per declaration, read from the source at the main and the kernel's built libraries
REASONS = {
    'twin_primes_infinite': ('RESTATED', 'its statement is the twin-prime conjecture itself; the corpus cites it as the open milestone M3 '
                             '(ADDITIVE_MULTIPLICATIVE_CONSPIRACY :411, T4); kept as a Prop with no proof, read as a premise'),
    'goldbach': ('RESTATED', 'its statement is the binary Goldbach conjecture; cited as the open milestone M4 (ADDITIVE_MULTIPLICATIVE_CONSPIRACY '
                 ':412, T4); kept as a Prop with no proof'),
    'sophie_germain_infinite': ('RESTATED', 'its statement is the Sophie Germain infinitude conjecture; cited as the open milestone M5 '
                                '(ADDITIVE_MULTIPLICATIVE_CONSPIRACY :413, T4); kept as a Prop with no proof'),
    'T3_perClass_to_combinations': ('RESTATED', 'the pinned step of the bracket the keystones cite (PATHS :293, SURROUND :177); its universal '
                                    'form is refuted in the same file (T3doubleprime_general_commutation_fails) and it closes under the '
                                    'shared witness (T3prime_shared_witness); kept as a Prop naming the per-instance step, its docstring '
                                    'saying so; consumed by the two AxiomCheck files alone'),
    'PinnedGoal': ('QUARANTINED', 'an example outside every lean_lib that only reproduces the goal at T3`s sorry; nothing consumes it'),
    'focus_on_critical_line': ('QUARANTINED', 'a legacy probe outside every lean_lib; its content is proved in the kernel`s own file '
                               'legacy/SchwarzReflection_PR.lean (completedRiemannZeta₀_im_eq_zero_on_half) and nothing consumes it'),
    'zeros_in_strip': ('QUARANTINED', 'a legacy probe outside every lean_lib; nothing consumes it'),
    'simple_zero_isolated': ('QUARANTINED', 'a legacy build attempt outside every lean_lib; nothing consumes it'),
    'accumulation_kills_derivs': ('QUARANTINED', 'a legacy build attempt outside every lean_lib; nothing consumes it'),
    'product_formula_prime_pow': ('QUARANTINED', 'a legacy copy outside every lean_lib; the built kernel proves its namesakes '
                                  '(Kernel/ProductFormula_Clean.lean :86, Kernel/ProductFormula_v2.lean :24), which do not import it'),
    'product_formula_nat': ('QUARANTINED', 'false as stated (n = 6 at p = 2 gives 3; the file`s own comment at :124), outside every lean_lib, '
                            'nothing consumes it'),
    'schwarz_discharge': ('QUARANTINED', 'one of the legacy Schwarz build attempts outside every lean_lib; the built kernel proves the '
                          'reflection (Kernel/SchwarzDischarge.lean :42, schwarz_reflection_completedZeta₀); its namesakes are the other '
                          'attempts, none imported'),
    'schwarz_v2': ('QUARANTINED', 'a legacy Schwarz attempt outside every lean_lib; superseded by Kernel/SchwarzDischarge.lean :42'),
    'schwarz_v3': ('QUARANTINED', 'a legacy Schwarz attempt outside every lean_lib; superseded by Kernel/SchwarzDischarge.lean :42'),
    'schwarz_v4': ('QUARANTINED', 'a legacy Schwarz attempt outside every lean_lib; superseded by Kernel/SchwarzDischarge.lean :42'),
    'schwarz_v5': ('QUARANTINED', 'a legacy Schwarz attempt outside every lean_lib; superseded by Kernel/SchwarzDischarge.lean :42'),
    '(example)': ('QUARANTINED', 'an unnamed legacy probe (example) outside every lean_lib; nothing can consume it'),
}


def _sorry_rows():
    rows = []
    for k, m, f, ln, built, s, d, subj, txt in sorry_lines():
        src = _show('D:/' + k, m, f).replace(chr(13), '').split(NL)
        i = ln - 1
        while i >= 0 and not DECL.match(src[i]):
            i -= 1
        kind, name = DECL.match(src[i]).groups() if i >= 0 else ('?', '?')
        users = []
        if name and kind != 'example':
            out = g('D:/' + k, 'grep', '-n', '-w', name.split('.')[-1], m, '--', '*.lean')
            users = sorted(set(l.split(':')[1] for l in out.split(NL) if l.strip()) - {f})
        key = 'PinnedGoal' if f == 'PinnedGoal.lean' else ('(example)' if kind == 'example' else name)
        prop, why = REASONS.get(key, ('### UNCLASSIFIED', '### NO REASON'))
        rows.append(dict(kernel=k, main=m, file=f, line=ln, built=built, text=src[ln - 1].strip(), decl_kind=kind, decl=name or '(example)',
                         decl_line=i + 1, statement=' '.join(x.strip() for x in src[i:ln - 1] if x.strip())[:400], files_naming=users,
                         entered=d, entered_sha=s, proposed=prop, reason=why))
    return rows


# ### the four built lines: the sentences across keystones, pages and ledgers at PLACE-papers HEAD that cite one of them as holding, each read
# ### whole; a sentence naming a milestone as open, sorry-carrying or a target is not a citation as holding
CITES_HOLDING = [
    ('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', 241,
     'the three conjectures the milestones state (twin primes, Goldbach, Sophie Germain) given as following -- "therefore the negation '
     'fails" -- from a "kernel-verified" structural argument; no kernel line carries the conjectures, the milestones close by sorry'),
    ('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md', 243,
     'the same sentence in the edition: "therefore the negation fails", the argument called kernel-verified; the milestones close by sorry'),
]


def sorry_classify(*a):
    """data/b648_sorry_classification.txt and .json: every one of the 37 lines verbatim with its declaration, statement head, the files naming
    it, its entry date and the classification proposed with one reason; the four built lines` citing sentences read and the ones citing a
    milestone as holding printed as UNLICENSED rows; no kernel edited."""
    rows = _sorry_rows()
    bad = [r for r in rows if r['proposed'].startswith('###')]
    if len(rows) != 37 or bad:
        sys.exit('### %d ROWS, %d UNCLASSIFIED -- NOTHING WRITTEN' % (len(rows), len(bad)))
    names = ('twin_primes_infinite', 'goldbach', 'sophie_germain_infinite', 'T3_perClass_to_combinations')
    hits = []
    for n in names:
        out = g(PP, 'grep', '-n', '-w', n, 'HEAD', '--', '*.md')
        hits += [l[len('HEAD:'):] for l in out.split(NL) if l.strip()]
    hits = sorted(set(hits))
    L = ['b648 -- COMPONENT 2, (R258)(2): THE 37 SORRY LINES ON KERNEL MAINS, EACH READ WHOLE, THE CLASSIFICATION PROPOSED FOR THE AUTHOR`S WORD; '
         'NO KERNEL EDITED (%s)' % utc(), '',
         '### the source: relay data/b647_sorry_census.json (every `sorry` in code at each kernel`s main); the declaration each closes read at the '
         'main, the files of its kernel naming it by git grep -w, the commit that brought the line by git blame and git log',
         '### the repairs of (R258)(2): PROVED -- a proof supplied on a branch and merged, graded by the gate; QUARANTINED -- moved to a branch '
         'sorry-quarantine-<kernel> and removed from main by the house delete form, its name and statement recorded in the kernel`s ERRATA-form '
         'file; RESTATED -- kept on main as a Prop or def with no proof and the docstring "stated, not proved; open", read as a premise', '',
         '### THE LINES (kernel@main:file:line | BUILT or TRACKED ONLY | the line verbatim | the declaration | entered | PROPOSED -- reason):']
    for r in rows:
        L += ['  %s@%s:%s:%d | %s | %s' % (r['kernel'], r['main'], r['file'], r['line'], 'BUILT' if r['built'] else 'TRACKED ONLY', r['text']),
              '      %s %s (:%d) -- %s' % (r['decl_kind'], r['decl'], r['decl_line'], r['statement'][:300]),
              '      files of the kernel naming it: %s ; entered %s at %s' % (', '.join(r['files_naming']) or 'none', r['entered'], r['entered_sha']),
              '      PROPOSED %s -- %s' % (r['proposed'], r['reason'])]
    c = collections.Counter(r['proposed'] for r in rows)
    L += ['', '### THE FOUR BUILT LINES` CITING SENTENCES (PLACE-papers %s, every *.md, git grep -w on the four names: %d lines, each read whole):' % (
        PRE_PP, len(hits)),
          '### a line naming a milestone open, sorry-carrying, a target or a T4 row is no citation as holding; the rows citing one as holding:']
    for f, ln, why in CITES_HOLDING:
        t = (_show(PP, 'HEAD', f) or '').replace(chr(13), '').split(NL)
        L += ['  UNLICENSED  PLACE-papers@%s:%s:%d -- %s' % (PRE_PP, f, ln, why), '      STATED: ' + (t[ln - 1][:900] if len(t) >= ln else '### OUT')]
    L += ['', '### ### **LINES 37 ; PROPOSED PROVED %d, QUARANTINED %d, RESTATED %d ; BUILT 4 ; CITING SENTENCES READ %d, UNLICENSED ROWS %d ; NO '
              'KERNEL EDITED.**' % (c['PROVED'], c['QUARANTINED'], c['RESTATED'], len(hits), len(CITES_HOLDING))]
    put_txt('b648_sorry_classification.txt', L)
    put_json('b648_sorry_classification.json', dict(at=utc(), rows=rows, cites_read=hits, unlicensed=[dict(file=f, line=ln, why=w) for f, ln, w in CITES_HOLDING]))
    print(L[-1])


BREACH_LINE = 13731      # ### OPEN_TRAILS: the breach line landed by record_lines
C_HEAD = ('*Appended 2026-10-10 by b648 to the sorry breach (:%d), under `(R258)`(2) and the author’s answer -- A CORRECTION, BY THE '
          'AUTHOR’S WORD: THE RULE UNENFORCED ON LEGACY CODE, NOT REFUTED; A NEW ARM:*')


def _correction():
    return ('\n%s the line above titles the 37 lines a refutation of the standing rule; all 37 entered their mains before the rule`s first line '
            '(:%d, b559, 2026-09-29), so by the author`s word the rule is not refuted: it was not enforced on code older than itself. The repairs, '
            'by the same word: QUARANTINED 33 -- the 32 SIDE-kernel legacy/ lines and SIDE-lv-conservation PinnedGoal.lean :23, each moved to a '
            'branch sorry-quarantine-<kernel>, its name and statement recorded in the kernel`s ERRATA-form file with a line naming where the true '
            'content is proved (SIDE-kernel Kernel/SchwarzDischarge.lean :42, Kernel/ProductFormula_Clean.lean :86); RESTATED 4 -- SIDE-effects '
            'Milestones.lean :32, :49, :63 as the open conjectures they are and SIDE-lv-conservation T3_StepNineBridge.lean :108 with its '
            'docstring naming the universal form`s refutation in the same file, each a Prop with "stated, not proved; open". From b648 the suite '
            'carries G-NO-SORRY-MAIN, an arm that reads every kernel main for a `sorry` in code outside a quarantine branch and fails on any '
            'hit. The two sentences citing the conjectures of the milestones as holding (ADDITIVE_MULTIPLICATIVE_CONSPIRACY :241 and its edition :243) '
            'stay UNLICENSED until their documents are re-cut.\n' % (C_HEAD % BREACH_LINE, RULE_LINE))


def correction(*a):
    """OPEN_TRAILS: the correction beneath the breach line, by the author's answer at Component 2; through the ledger guards before it lands."""
    import b641_record as R41
    Q = R2._Q()
    if C_HEAD.split('--')[0] in io.open(Q.OT, encoding='utf-8').read() and not DRY:
        sys.exit('### THE CORRECTION IS WRITTEN ALREADY -- NOTHING WRITTEN')
    t = R41._poss(_correction())
    cells = R3.predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = R3._nd(t)
    p = os.path.join(SP if DRY else D, 'b648_scanfile_correction.md')
    _write(p, t.encode('utf-8'))
    clean = _clean(_scan(p))
    ticks = [l[:60] for l in t.split(NL) if l.count('`') % 2]
    print('  table cells: %s ; nd %s ; scanner %s ; odd backticks %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE'))
    if DRY:
        print(t)
        return
    if cells or any(nd.values()) or not clean or ticks:
        sys.exit('### NOTHING WRITTEN')
    R3._land(Q, [('OPEN_TRAILS.md', C_HEAD % BREACH_LINE, t)], 'b648_correction_line.json', BREACH_LINE)


# ================================================================================ COMPONENT 2: THE REPAIRS BY THE AUTHOR'S WORD
# ### QUARANTINED: on a work branch b648-quarantine-<kernel> from the main, each quarantined declaration's span -- its docstring directly above,
# ### its head and every line to the next line at column 0 -- replaced by one comment line naming the branch; the branch
# ### sorry-quarantine-<kernel> made at the main before any edit holds every declaration as it stood; the kernel's ERRATA.md (the house form
# ### of PLACE-papers ERRATA.md: the declaration, the affected file and line, the correction, the date) written new, each entry with where the
# ### true content is proved. The work branch is merged alone by fast-forward after its diff is read; nothing is built (the files lie outside
# ### every lean_lib).
TRUE_HOME = {'schwarz_discharge': 'Kernel/SchwarzDischarge.lean :42 (schwarz_reflection_completedZeta₀)',
             'schwarz_v2': 'Kernel/SchwarzDischarge.lean :42', 'schwarz_v3': 'Kernel/SchwarzDischarge.lean :42',
             'schwarz_v4': 'Kernel/SchwarzDischarge.lean :42', 'schwarz_v5': 'Kernel/SchwarzDischarge.lean :42',
             'product_formula_prime_pow': 'Kernel/ProductFormula_Clean.lean :86 (product_formula_prime_pow, its built namesake)',
             'focus_on_critical_line': 'legacy/SchwarzReflection_PR.lean :129 (completedRiemannZeta₀_im_eq_zero_on_half)'}


def _span(src, decl_line):
    """[a, b) 0-based: the docstring block directly above the declaration, the declaration, every line to the next non-empty line at column 0."""
    a = decl_line - 1
    if a > 0 and src[a - 1].rstrip().endswith('-/'):
        j = a - 1
        while j >= 0 and not src[j].lstrip().startswith('/-'):
            j -= 1
        if j >= 0:
            a = j
    b = decl_line
    while b < len(src) and not (src[b].strip() and not src[b][0].isspace()):
        b += 1
    while b > decl_line and not src[b - 1].strip():
        b -= 1
    return a, b


def quarantine(kernel, *a):
    """the quarantine of the author's word for one kernel: the branches made, the spans removed and banked whole, ERRATA.md written, the work
    branch committed; data/b648_quarantine_<kernel>.txt. Refuses unless the kernel is on main, its main the census's, its tracked tree clean."""
    rp = 'D:/' + kernel
    rows = [r for r in jl('b648_sorry_classification.json').get('rows') or [] if r['kernel'] == kernel and r['proposed'] == 'QUARANTINED']
    if not rows:
        sys.exit('### NO QUARANTINED LINE IN %s -- NOTHING DONE' % kernel)
    main = rows[0]['main']
    qb, wb = 'sorry-quarantine-%s' % kernel, 'b648-quarantine-%s' % kernel
    if g(rp, 'rev-parse', '--abbrev-ref', 'HEAD').strip() != 'main' or not g(rp, 'rev-parse', 'main').strip().startswith(main) \
            or g(rp, 'status', '--porcelain', '--untracked-files=no').strip():
        sys.exit('### %s IS NOT ON A CLEAN main AT %s -- NOTHING DONE' % (kernel, main))
    by_file = collections.defaultdict(list)
    for r in rows:
        by_file[r['file']].append(r)
    L = ['b648 -- COMPONENT 2, (R258)(2) AND THE AUTHOR`S ANSWER: THE QUARANTINE OF %s (%s)' % (kernel, utc()), '',
         '### main %s ; the branch %s made at the main before any edit, holding every declaration as it stood ; the work branch %s' % (main, qb, wb), '']
    new_files, entries = {}, []
    for f, rs in sorted(by_file.items()):
        src = _show(rp, main, f).replace(chr(13), '').split(NL)
        spans = sorted(set(_span(src, r['decl_line']) for r in rs), reverse=True)
        out = list(src)
        for x, y in spans:
            names = sorted(set(r['decl'] for r in rs if x <= r['decl_line'] - 1 < y))
            out[x:y] = ['-- [b648, (R258)(2)] %s closed by `sorry` -- quarantined to branch %s; recorded in ERRATA.md.' % (', '.join(names), qb)]
            L += ['### %s :%d-:%d removed (%s), the block whole:' % (f, x + 1, y, ', '.join(names))] + ['    | ' + s for s in src[x:y]] + ['']
        new_files[f] = NL.join(out)
        for r in rs:
            entries.append(r)
    E = ['# Errata', '', 'This file records corrections to %s`s main. Each entry lists the declaration, the affected file and line, the correction, '
         'and the date; entries are retained.' % kernel, '',
         '## E-2026-10-10-1 — %d `sorry`-closed declarations quarantined from main (b648, the author`s ruling (R258)(2))' % len(entries), '',
         'Every declaration below closed by `sorry` on main at `%s`, in files outside every `lean_lib` of the lakefile; each entered main before the '
         'programme`s standing line "no `sorry` on any `main`" (its first ledger line, PLACE-papers OPEN_TRAILS.md :11508, 2026-09-29). Each is '
         'removed from main and kept whole on the branch `%s`, made at `%s`. Correction: removed from main, quarantined. Date: 2026-10-10.' % (
             main, qb, main), '']
    for r in entries:
        home = TRUE_HOME.get(r['decl'])
        E.append('- `%s` (%s), `%s` :%d (its `sorry` at :%d), entered %s at `%s`: `%s`%s' % (
            r['decl'], r['decl_kind'], r['file'], r['decl_line'], r['line'], r['entered'], r['entered_sha'],
            re.sub(r'\s+', ' ', r['statement'])[:220].replace('`', "'"), ('. True content proved at ' + home + '.') if home else '.'))
    etext = NL.join(E) + NL
    L += ['### ERRATA.md, written new at the kernel`s root:'] + ['    | ' + s for s in etext.rstrip(NL).split(NL)]
    if DRY:
        put_txt('b648_quarantine_%s.txt' % kernel, L)
        print('  DRY: %d declarations in %d files ; the bank in the scratchpad' % (len(entries), len(new_files)))
        return
    for b in (qb, wb):
        if g(rp, 'rev-parse', '--verify', '-q', 'refs/heads/' + b).strip():
            sys.exit('### THE BRANCH %s EXISTS -- NOTHING DONE' % b)
    g(rp, 'branch', qb, 'main')
    g(rp, 'checkout', '-q', '-b', wb, 'main')
    for f, t in new_files.items():
        open(os.path.join(rp, *f.split('/')), 'wb').write((t if t.endswith(NL) else t + NL).encode('utf-8'))
    open(os.path.join(rp, 'ERRATA.md'), 'wb').write(etext.encode('utf-8'))
    g(rp, 'add', '--', 'ERRATA.md', *new_files.keys())
    msg = ('b648 under (R258)(2), the author`s word: %d sorry-closed declarations quarantined from main to branch %s (made at %s), each recorded in '
           'ERRATA.md (E-2026-10-10-1) with where its true content is proved; legacy files outside every lean_lib, nothing built.' % (len(entries), qb, main))
    g(rp, 'commit', '-q', '-m', msg)
    L += ['', '### the work branch committed: %s %s ; the files changed: %s' % (wb, g(rp, 'rev-parse', '--short=7', 'HEAD').strip(),
                                                                          g(rp, 'diff', '--stat', 'main', wb).strip().split(NL)[-1])]
    L += ['', '### ### **%s: %d DECLARATIONS QUARANTINED IN %d FILES ; ERRATA.md WRITTEN ; BRANCHES %s AND %s ; NOT YET MERGED.**' % (
        kernel, len(entries), len(new_files), qb, wb)]
    put_txt('b648_quarantine_%s.txt' % kernel, L)
    print(L[-1])


RESTATE = {'SIDE-effects': ('b648-restate-SIDE-effects', 'SIDEEffects/Milestones.lean', 'SIDEEffects.Milestones'),
           'SIDE-lv-conservation': ('b648-restate-SIDE-lv-conservation', 'SIDELvConservation/T3_StepNineBridge.lean', 'SIDELvConservation.T3_StepNineBridge')}
def code_sorries(k, rev='main'):
    """every `sorry` in code at `rev` of kernel `k` -- b647's census rule (tools/b647_record.py `sorries`): git grep -n -w sorry over the
    .lean files outside .lake/, a hit in code when the part of its line before `--` names it and the line lies outside every block comment
    or doc string (the depth of `/-` against `-/` read from the file at `rev`): [(file, line, text)]."""
    out, texts = [], {}
    for l in g('D:/' + k, 'grep', '-n', '-w', 'sorry', rev, '--', '*.lean').split(NL):
        m = re.match(r'^[^:]+:(.+?):(\d+):(.*)$', l)
        if not m or m.group(1).startswith('.lake/'):
            continue
        f, ln, txt = m.group(1), int(m.group(2)), m.group(3)
        if not re.search(r'\bsorry\b', txt.split('--', 1)[0]):
            continue
        if f not in texts:
            texts[f] = (_show('D:/' + k, rev, f) or '').replace(chr(13), '').split(NL)
        depth = 0
        for i, x in enumerate(texts[f][:ln], 1):
            pre = x if i < ln else x[:x.find('sorry') if 'sorry' in x else len(x)]
            depth += pre.count('/-') - pre.count('-/')
        if depth <= 0:
            out.append((f, ln, txt.strip()))
    return out


CODE_SORRY = 'b647`s census rule (code_sorries)'


def repairs(*a):
    """data/b648_sorry_repairs.txt: every line's repair as it stands, read from the kernels -- the quarantines merged (main and branch read
    locally and at the remote), the restatements on their branches with their diffs whole and the build`s watchdog row; the sorries in code
    left on each kernel's main counted by git grep."""
    W = jl('b648_build_watch.json').get('rows') or []
    L = ['b648 -- COMPONENT 2, (R258)(2): THE REPAIRS BY THE AUTHOR`S WORD, AS THEY STAND (%s)' % utc(), '']
    for k in ('SIDE-kernel', 'SIDE-lv-conservation'):
        rp = 'D:/' + k
        qb = 'sorry-quarantine-%s' % k
        rem = dict((l.split('\t')[1], l.split('\t')[0]) for l in g(rp, 'ls-remote', 'origin', 'refs/heads/main', 'refs/heads/' + qb).split(NL) if '\t' in l)
        L.append('### QUARANTINED, %s: main %s (remote %s) ; %s %s (remote %s) ; ERRATA.md on main: %s' % (
            k, g(rp, 'rev-parse', '--short=7', 'main').strip(), rem.get('refs/heads/main', '?')[:7], qb, g(rp, 'rev-parse', '--short=7', qb).strip(),
            rem.get('refs/heads/' + qb, '?')[:7], 'E-2026-10-10-1' in (_show(rp, 'main', 'ERRATA.md') or '')))
    L.append('')
    for k, (b, f, mod) in RESTATE.items():
        rp = 'D:/' + k
        w = [r for r in W if r.get('module') == mod]
        L += ['### RESTATED, %s: branch %s %s, NOT MERGED ; its build: %s' % (
            k, b, g(rp, 'rev-parse', '--short=7', b).strip(),
            ('; '.join('%s exit %s, host low %s MB, the hold %s' % (r.get('module'), r.get('rc'), r.get('lows'), r.get('hold')) for r in w)
             if w else 'NOT RUN -- RUN-BENEATH-HOLD territory ((R258)(5)), the smaller module of SIDE-effects stopped beneath the hold first')),
              '### the diff, main..%s, whole:' % b] + ['    | ' + x for x in g(rp, 'diff', 'main', b, '--', f).replace(chr(13), '').rstrip(NL).split(NL)] + ['']
    L.append('### `sorry` IN CODE ON EACH KERNEL`S MAIN NOW (git grep at main, %s):' % CODE_SORRY)
    tot = 0
    for k in ('SIDE-kernel', 'SIDE-effects', 'SIDE-lv-conservation'):
        out = code_sorries(k)
        tot += len(out)
        L += ['  %s: %d' % (k, len(out))] + ['      %s:%d: %s' % (f, ln, t[:140]) for f, ln, t in out]
    L += ['', '### ### **QUARANTINED 33, MERGED AND PUSHED ; RESTATED 4, ON BRANCHES, NOT MERGED, THEIR BUILDS BENEATH THE HOLD ; SORRY IN CODE ON THE '
              'MAINS NOW %d.**' % tot]
    put_txt('b648_sorry_repairs.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 3: THE TWO PAGES THROUGH THE TABLE
# ### (R258)(3): every sentence of both pages one row of the licensed-statement table (tools/licensed_table.py). The prose and the glossary
# ### entries by HAND, each citing the lines read; the node lines and the Correspondence rows by the table's `terminal` rule against relay's
# ### terminal table at the revision read, a name with no row read by HAND at the probe's cell; the Placement rows by HAND at the line the
# ### path's file carries. A title or a heading is not a sentence and takes no row; a prose sentence no entry below reads refuses the bank.
READ_AT = {'relay': '8a8e9cc8', 'PLACE-papers': '6783833', 'SIDE-explicit-formula': '82550e4', 'SIDE-global-section': '17ce9ff',
           'mathlib': 'de5ce8a9'}
REPO_DIR = {'relay': RELAY, 'PLACE-papers': PP, 'SIDE-explicit-formula': 'D:/SIDE-explicit-formula', 'SIDE-global-section': 'D:/SIDE-global-section',
            'mathlib': 'D:/SIDE-explicit-formula/.lake/packages/mathlib'}
NODES = {'zeta': 'b643_nodes_zeta.txt', 'chi': 'b643_nodes_chi.txt'}
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}


def _cite(repo, path, at, rev=None):
    """'repo@rev:path:N' for the lines read: `at` a line or range, checked inside the file, or '~needle', the first line carrying it; at
    the revision read (READ_AT) unless one is named."""
    rev = rev or READ_AT[repo]
    t = _show(REPO_DIR[repo], rev, path)
    if t is None:
        raise SystemExit('### REFUSED: the cited file is unread, %s@%s:%s' % (repo, rev, path))
    L = t.split(NL)
    if at.startswith('~'):
        hits = [i for i, l in enumerate(L, 1) if at[1:] in l]
        if not hits:
            raise SystemExit('### REFUSED: the needle %r is not in %s@%s:%s' % (at[1:], repo, rev, path))
        at = str(hits[0])
    elif int(at.split('-')[-1]) > len(L):
        raise SystemExit('### REFUSED: %s@%s:%s has %d lines, the cite reads %s' % (repo, rev, path, len(L), at))
    return '%s@%s:%s:%s' % (repo, rev, path, at)


_P, _R, _E, _S = 'PLACE-papers', 'relay', 'SIDE-explicit-formula', 'SIDE-global-section'
_RM, _OT, _FI, _CR = 'README.md', 'OPEN_TRAILS.md', 'FINDINGS.md', 'CORRESPONDENCE.md'
_C5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
GLOSS_CITES = {
    1: [(_P, _OT, '12354'), (_P, _RM, '22-23')], 2: [('mathlib', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', '185')],
    3: [(_P, _RM, '125')], 4: [(_R, 'data/b638_ferry.txt', '70'), (_P, _RM, '22-23'), (_S, _CR, '459')],
    5: [(_E, 'SIDEExplicitFormula/H2Sign.lean', '28')], 6: [(_E, 'SIDEExplicitFormula/H2Sign.lean', '28-29')],
    7: [(_E, 'SIDEExplicitFormula/H2Sign.lean', '22-26')],
    8: [(_E, 'SIDEExplicitFormula/Seam.lean', '100-101'), (_P, _RM, '115'), (_S, _CR, '459')],
    9: [(_P, _RM, '121')], 10: [(_P, _RM, '121'), (_S, _CR, '476')], 11: [(_P, _RM, '121'), (_S, _CR, '476')],
    12: [(_E, 'SIDEExplicitFormula/PowerWindow.lean', '492-495'), (_P, _RM, '113'), (_R, 'tools/e0_rule.py', '~rh_strip_imp_rh')],
    13: [(_P, _RM, '18')], 14: [(_P, _RM, '15'), (_P, _RM, '18')], 15: [(_P, _RM, '15')], 16: [(_P, _RM, '~pins move')],
    17: [(_P, _RM, '79-80')], 18: [(_P, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', '3'), (_P, 'REGISTRY.md', '~copied from `anthropics/formal-math`')],
    19: [(_P, _RM, '121')], 20: [(_R, 'tools/e0_rule.py', '~RULE_TEXT = ['), (_P, _OT, '13337')],
    21: [(_R, 'data/b637_binder_classes.txt', '1')], 22: [(_R, 'data/b637_binder_classes.txt', '1'), (_R, 'tools/e0_rule.py', '~CLASSES = (')],
    23: [(_R, 'tools/e0_rule.py', '~(R235)(2), b625')], 24: [(_R, 'tools/e0_rule.py', '~(R235)(2), b625')],
    25: [(_P, _RM, '64-65')], 26: [(_P, _RM, '66-68')], 27: [(_P, _RM, '69-71'), (_R, 'tools/e0_rule.py', '~(R234)(2), b624')],
    28: [(_P, _RM, '69-71')], 29: [(_R, 'tools/terminal_table.py', '~(R164)(2)(a)')], 30: [(_P, _RM, '72-73')],
    31: [(_R, 'data/b637_binder_classes.txt', '~THE GRADE:')], 32: [(_P, _OT, '13221')], 33: [(_P, _OT, '13221'), (_R, 'tools/e0_rule.py', '~MET = (')],
    34: [(_R, 'tools/terminal_table.py', '10-12')], 35: [(_P, _C5, '43')], 36: [(_R, 'tools/terminal_table.py', '1-12')],
    37: [(_P, _C5, '43'), (_R, 'tools/terminal_table.py', '~(R245)(2)-(3)')], 38: [(_P, _OT, '13335')],
    39: [(_R, 'data/b539_ferry.txt', '21-22')], 40: [(_R, 'data/b539_ferry.txt', '22-24'), (_P, _FI, '4823'), (_P, _FI, '5812')],
    41: [(_P, _FI, '4823'), (_P, _FI, '5812')], 42: [(_R, 'data/b539_ferry.txt', '25-28')], 43: [(_P, _FI, '5812')],
    44: [(_R, 'data/b539_ferry.txt', '28-29')], 45: [(_R, 'data/b539_ferry.txt', '29-30')], 46: [(_P, _C5, '20')],
    47: [(_P, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', '14-20'), (_P, _C5, '20')], 48: [(_P, _C5, '41')],
    49: [(_P, _RM, '35')], 50: [(_P, _RM, '37'), (_P, _FI, '6450')], 51: [(_P, _RM, '36'), (_P, _FI, '6450')], 52: [(_P, _RM, '36')],
    53: [(_P, _RM, '40')], 54: [(_P, _RM, '39')], 55: [(_P, _RM, '41')], 56: [(_P, _OT, '12354')],
    57: [(_P, 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md', '1')], 58: [(_P, _RM, '106'), (_P, _RM, '113-125')],
    59: [(_P, _OT, '11864')], 60: [(_P, _OT, '11864')], 61: [(_P, _OT, '11864')], 62: [(_P, _OT, '12699')], 63: [(_P, 'REGISTRY.md', '360')],
    64: [(_P, _OT, '11413')], 65: [(_P, _OT, '13339')], 66: [(_R, 'data/b638_ferry.txt', '1-3')], 67: [(_R, 'tools/act_root.py', '4-10')],
    68: [(_P, _OT, '12354')], 69: [(_P, _OT, '12354')], 70: [(_P, _OT, '13489')], 71: [(_R, 'data/b642_ferry.txt', '92')],
    72: [(_R, 'data/b643_ferry.txt', '97')], 73: [(_R, 'data/b643_ferry.txt', '97')], 74: [(_R, 'data/b643_author_answers.txt', '4-5')],
    75: [(_R, 'data/b643_ferry.txt', '97')], 76: [(_R, 'data/b644_ferry.txt', '72')], 77: [(_R, 'data/b644_ferry.txt', '72')],
    78: [(_R, 'data/b644_ferry.txt', '72')], 79: [(_P, 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', '27')],
    80: [(_R, 'data/b647_ferry.txt', '57-60')]}
GLOSS_NOTE = {
    13: 'the quotation is at README :18 inside a link, "~45 further Lean kernels under [psinary-sketch](...) carry the arms" -- the words '
        'the same, the markup between them',
    34: 'the quotation is at terminal_table.py :10-:11 across a comment marker ("### **WITHOUT CHOOSING**"), the words the same',
    50: 'its "append-only" is not at README :37; FINDINGS :6450 names the four ledgers append-only',
    51: 'its quotation drops README :36`s "(`O.n`)" with no mark of the omission; its "append-only" is at FINDINGS :6450, not README :36',
    12: 'PowerWindow.lean :492-:495 is the seam`s own docstring: from the strip form to Mathlib`s RH, the left half-plane`s zeros the trivial ones'}
GLOSS_FIND = {
    65: ('UNLICENSED', 'the entry`s "(b638 is this one)": on a page or a census generated after b638 it names an act that is not the one the '
                       'reader holds, and nothing in the corpus makes a later document b638`s',
         'W-ORD-GLOSSARY-ACT-NAME, TRIGGER the author`s word on the re-cut order ((R258)(6)); relay data/glossary.txt is additive and its '
         'line stays; the re-cut is an appended entry for bNNN without the parenthesis, by the author`s word')}

_TT = 'relay data/terminal_table.json'
_CHI_PREM = 'the table grades it INTERFACES by b626`s supersession cells, its premises hχ : χ.IsPrimitive and h1 : χ ≠ 1 -- and the sentence names them'
PROSE = [
    ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/b643_nodes_zeta.txt`', 'MATCHES',
     [(_R, 'tools/chain_page.py', '742-744'), (_R, 'data/b643_nodes_zeta.txt', '144')], 'the generator`s head template, the ζ list named'),
    ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/b643_nodes_chi.txt`', 'MATCHES',
     [(_R, 'tools/chain_page.py', '777-779'), (_R, 'data/b643_nodes_chi.txt', '83')], 'the generator`s Dirichlet head template, the χ list named'),
    ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/b648_nodes_zeta.txt`', 'MATCHES',
     [(_R, 'tools/chain_page.py', '~def emit(nodes', '87d3e6b9'), (_R, 'data/b648_nodes_zeta.txt', '~# table grade', '87d3e6b9')],
     'the generator`s head template, b648`s marked ζ list named'),
    ('This page is generated by relay `tools/chain_page.py` from the node list relay `data/b648_nodes_chi.txt`', 'MATCHES',
     [(_R, 'tools/chain_page.py', '~def emit_dirichlet(', '87d3e6b9'), (_R, 'data/b648_nodes_chi.txt', '~# table grade', '87d3e6b9')],
     'the generator`s Dirichlet head template, b648`s marked χ list named'),
    ('It is generated at SIDE-explicit-formula v0.26 = `82550e4`', 'MATCHES',
     [(_R, 'data/b643_nodes_zeta.txt', '59'), (_R, 'data/b643_nodes_chi.txt', '39'), (_R, 'tools/chain_page.py', '87-96')],
     'both lists carry `# pin: v0.26`; v0.26 peels to 82550e4 (git rev-parse v0.26^{commit})'),
    ('Each line reads: name', 'MATCHES', [(_R, 'tools/chain_page.py', '761-762'), (_R, 'tools/chain_page.py', '795-796')],
     'the node line`s template, cell for cell'),
    ("A node's tier cell is computed from three printed facts", 'MATCHES', [(_R, 'tools/chain_page.py', '384-408'), (_R, 'tools/chain_page.py', '~CONFLICT -- the table')],
     'tier_of_node computes the cell as stated; a disagreement with the table`s tier refuses the page'),
    ("The terminal table's grade for the node, where it differs from the E0 grade", 'MATCHES',
     [(_R, 'tools/chain_page.py', '~TABLE_GRADE_KEY = (', '87d3e6b9'), (_R, 'tools/chain_page.py', '~def e0_cell(', '87d3e6b9')],
     'repair 3`s key sentence: e0_cell prints the row`s grade beside E0 where the two differ, never for UNGRADED (relay 87d3e6b9 on)'),
    ('*The internal names this document uses', 'MATCHES', [(_R, 'data/glossary.txt', '1-5')], 'the glossary`s header: each entry the name, its definition, its source'),
    ('The block is printed by relay `tools/chain_page.py` from relay `data/glossary.txt`', 'MATCHES',
     [(_R, 'tools/chain_page.py', '494-496'), (_R, 'data/b647_glossary_block.txt', '1')],
     'one source, one printer; at b647 the two pages and v0.7.1 printed the same block byte for byte'),
    ("The shape cell after each statement is read by the generator", 'MATCHES', [(_R, 'tools/chain_page.py', '442-449'), (_R, 'tools/chain_page.py', '687-697')],
     'the shape key and shape_of'),
    ('h2_sign — open; by the compiled equivalences above', 'MATCHES', [(_S, _CR, '459'), (_S, _CR, '476')],
     'h2_sign_iff_rh, li_nonneg_iff_rh, arith_limit_nonneg_iff_rh each DERIVES; h2_sign stated as open'),
    ("*(Appended under the author's ruling `(R177)`(2)", 'MATCHES', [(_P, _RM, '121')], 'README :121, the same words'),
    ("Supportable, the author's sentence: *Li's criterion", 'MATCHES', [(_P, _RM, '121'), (_S, _CR, '476')], 'README :121; li_nonneg_iff_rh DERIVES'),
    ('Weil positivity on classK, Li positivity and arithmetic-limit positivity are compiled', 'MATCHES', [(_P, _RM, '121')], 'README :121'),
    ('Not supportable, unchanged:', 'MATCHES', [(_P, _RM, '121')], 'README :121'),
    ("*(Appended under the author's ruling `(R206)`(4)(c)", 'MATCHES', [(_R, 'data/b643_nodes_zeta.txt', '123')], 'the list`s backmatter record'),
    ('The faces and multiplicity:', 'MATCHES', [(_S, _CR, '459'), (_S, _CR, '476'), ('mathlib', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', '185')],
     'each face an equivalence with RiemannHypothesis, whose statement names no multiplicity'),
    ("At the schema's form, a configuration whose fields", 'MATCHES', [(_E, 'SIDEExplicitFormula/SaltCheckSimplicity.lean', '107-112')],
     'allSimple_not_forced (rule DERIVES): ∃ C, C.target ∧ h2_sign_cfg C ∧ ¬ allSimple C, its witness toyCfg 2 a point of multiplicity two; simplicity a DEF'),
    ('exceptional_mass_le_third (SIDE-explicit-formula v0.23', 'MATCHES', [(_P, _FI, '6862'), (_R, 'data/b643_nodes_zeta.txt', '143')],
     'exceptional_mass_le_third INTERFACES (cell FINDINGS :6862), its premise cited as discharged at its source kernel'),
    ('GRH_chi — open, for each primitive χ ≠ 1', 'MATCHES', [(_S, _CR, '522')], _CHI_PREM),
    ('The criterion for primitive χ is composed', 'MATCHES', [(_S, _CR, '522'), (_P, _RM, '125')], _CHI_PREM + '; README :125, the author`s sentence'),
    ('The one clause now has two compiled instances', 'MATCHES', [(_P, _RM, '125')], 'README :125; neither instance stated as proved'),
    ("the instance's positivity equivalence is the family theorem", 'OVERREACHES', [(_R, 'data/b643_premise_table.txt', '47'), (_R, 'data/b643_premise_table.txt', '14')],
     'dedekind_instance DERIVES; but of dedekind_rhs`s two premises TrivialSummandPremise is REFUTED-BY-COMPUTATION (b643`s premise table :47) -- the '
     "sentence offers a refuted premise as the cost of the reading; at v0.26 the reading is dedekind_rhs' on TrivialSummandPremise' k, witnessed"),
    ('The instance is a statement about the schema', 'MATCHES', [(_R, 'data/b643_nodes_chi.txt', '82')], 'dedekind_instance`s statement: h2_sign_cfg (DedekindConfig q) ↔ ...'),
]
PROSE_RECUT = {"the instance's positivity equivalence is the family theorem": (
    'RE-CUT: the instance`s positivity equivalence is the family theorem with the trivial summand added and needs no premise; reading the '
    "summed side as the Dedekind zeta's costs two premises, which at v0.26 sit on dedekind_rhs' -- TrivialSummandPremise' k and "
    'EulerFactorPremise q, both witnessed -- the earlier TrivialSummandPremise of dedekind_rhs being REFUTED-BY-COMPUTATION. (The node list`s '
    'backmatter record, data, not the generator`s template: HELD for the author`s word on the re-cut order.)')}
_SPLIT = re.compile(r'(?<=\.)\*?\)?\*?\s+(?=[A-Z*`(])|(?<=\.)\s+(?=exceptional_mass_le_third )')


def _sentences(l):
    out, last = [], 0
    for m in _SPLIT.finditer(l):
        out.append(l[last:m.end()].strip())
        last = m.end()
    out.append(l[last:].strip())
    return [s for s in out if s]


def _tt_index(rev):
    T = json.loads(_show(RELAY, rev, 'data/terminal_table.json'))['rows']
    idx = collections.defaultdict(list)
    for x in T:
        idx[(x['repo'], x['name'])].append(x)
    return idx


def _page_rows(key, text, idx, page_rev):
    import licensed_table as LT
    pname = K.PNAME[key]
    probe = rd(PROBE[key]).split(NL)
    rows, skipped = [], []
    sec = 'head'
    node_short = []
    for l in text.split(NL):
        m = re.match(r'^\d+\. `([^`]+)` — (\S+):\d+ — ', l)
        if m and not m.group(2).startswith('Mathlib'):
            node_short.append(m.group(1).split('.')[-1])
    gi = 0
    for n, l in enumerate(text.split(NL), 1):
        src = '%s:%d' % (pname, n)
        if not l.strip():
            continue
        if l.startswith('#'):
            sec = l[3:].strip() if l.startswith('## ') else sec
            skipped.append('%d %s' % (n, l))
            continue
        m = re.match(r'^(\d+)\. `([^`]+)` — .* — E0: (\S+)(?: \(table: (\S+)\))? — tier: ', l)
        if m:
            # ### a line carrying the table's grade beside E0 (repair 3) states that grade as the table's: the claim read is the table's
            nm, e0 = m.group(2), (m.group(4) or m.group(3))
            hit = idx.get(('SIDE-explicit-formula', nm)) or []
            row = None
            if len(hit) == 1:
                x = hit[0]
                lk = lambda _n, x=x: (x['name'], x['grade'], re.sub(r'\s+', ' ', x['statement'] or '')[:150], (x.get('head') or '')[:7])  # noqa: E731
                row = LT.terminal_row('%s:node:%s' % (key, nm), src, 'node line %s: E0 %s' % (m.group(1), e0), nm, e0, lk)
                if row and row['verdict'] != 'MATCHES':
                    row = LT.recut(row, 'the node line printed with the table`s grade beside the E0 grade -- "E0: %s (table: %s)" -- by '
                                        'the template repair of relay tools/chain_page.py (Component 3)' % (e0, x['grade']))
            if row is None:
                pl = [i for i, p in enumerate(probe, 1) if p == '@@BEGIN ' + nm]
                if not pl:
                    raise SystemExit('### REFUSED: %s has no table row and no probe cell' % nm)
                kind = (re.search(r'@@KIND (\S+)', probe[pl[0]]) or [None, '?'])[1]
                v = 'MATCHES' if (kind != 'theorem' and e0 == 'DEF') else 'UNLICENSED'
                row = dict(id='%s:node:%s' % (key, nm), source=src, stated='node line %s: E0 %s' % (m.group(1), e0), by='HAND',
                           cited=['%s@%s:data/%s:%d' % (_R, READ_AT[_R], PROBE[key], pl[0] + 1)],
                           licensed='the probe`s cell: @@KIND %s; no row of the terminal table (%s); the line states a definition as DEF and claims '
                                    'nothing beyond it' % (kind, 'upstream' if nm.split('.')[0] in ('riemannZeta', 'RiemannHypothesis') else 'a definition the table does not list'),
                           verdict=v, action='none')
            row.update(page=key, kind='node', line=n)
            rows.append(row)
            continue
        m = re.match(r'^\| `([^`]+)` \| ([^|]+?) \| ([^|]+?) \| ([^|]*?) \|$', l)
        if sec == 'Correspondence' and m:
            nm, repo, gr = m.group(1), m.group(2).strip(), m.group(3).strip()
            claimed = gr.split()[0]
            claimed = {'PREDICATE-UNLISTED': 'INTERFACES', 'ENCODES-CONCLUSION': 'INTERFACES'}.get(claimed, claimed)
            hit = idx.get((repo, nm)) or []
            row = None
            if len(hit) == 1:
                x = hit[0]
                lk = lambda _n, x=x: (x['name'], x['grade'], re.sub(r'\s+', ' ', x['statement'] or '')[:150], (x.get('head') or '')[:7])  # noqa: E731
                row = LT.terminal_row('%s:corr:%s' % (key, nm), src, 'Correspondence: %s %s' % (nm.split('.')[-1], gr.split()[0]), nm, claimed, lk)
                if row and row['verdict'] != 'MATCHES':
                    row = LT.recut(row, 'the Correspondence row re-emitted from the table at the close')
            if row is None and nm == 'residue_irreducible':
                row = dict(id='%s:corr:%s' % (key, nm), source=src, stated='Correspondence: residue_irreducible %s' % gr[:60], by='HAND',
                           cited=[_cite(_P, 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', '108'), _cite(_P, 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', '228')],
                           licensed='THE_RESIDUE_OF_RH :228 tiers it T1-lit, CARRIED -- INTERFACES on a literature theorem; :108 its axiom print; no '
                                    'row of the terminal table (SIDE-lv-conservation is outside it)', verdict='MATCHES', action='none')
            if row is None:
                raise SystemExit('### REFUSED: the Correspondence row %s (%s) has no reading' % (nm, repo))
            row.update(page=key, kind='correspondence', line=n)
            rows.append(row)
            continue
        m = re.match(r'^\| ([^|`]+?) \| (.+) \|$', l)
        if sec == 'Placement' and m and not l.startswith('| object') and not l.startswith('|:--'):
            obj, cell = m.group(1).strip(), m.group(2).strip()
            paths = re.findall(r'`([^`]+)`', cell)
            cites, v, lic, act = [], 'MATCHES', '', 'none'
            if obj in ('this page', 'the ζ-leg'):
                cites, lic = [_cite(_P, paths[0], '1')], 'the page at PLACE-papers'
            elif obj == 'ledger':
                cites, lic = [_cite(_P, paths[0], '1')], 'the ledger at PLACE-papers'
            elif obj in ('the ceiling sentence', 'the successor sentence'):
                for p in paths:
                    f, ln = p.split(':')
                    cites.append(_cite(_P, f, ln))
                    t = _show(PP, READ_AT[_P], f).split(NL)[int(ln) - 1]
                    if not t.startswith("*(Appended under the author's ruling `(R177)`(2)" if obj == 'the ceiling sentence' else "*(Appended under the author's ruling `(R183)`(3)"):
                        v = 'OVERREACHES'
                lic = 'the line cited carries the ruled sentence' if v == 'MATCHES' else 'the line cited does not carry the ruled sentence'
                if v != 'MATCHES':
                    act = 'RE-CUT: the row re-emitted with the line read at PLACE-papers HEAD'
            elif obj == 'keystone naming a node':
                t = _show(PP, READ_AT[_P], paths[0])
                if t is None:
                    v, lic, act = 'OVERREACHES', 'the file is not at PLACE-papers %s' % READ_AT[_P], 'RE-CUT: the row dropped at re-emission'
                    cites = [_cite(_P, pname, str(n))]
                else:
                    pat = re.compile(r'\b(' + '|'.join(re.escape(s) for s in sorted(set(node_short)) if not re.fullmatch(r'[a-z]+|[A-Z]+', s)) + r')\b')
                    hits = [i for i, x in enumerate(t.split(NL), 1) if pat.search(x)]
                    if hits:
                        cites, lic = [_cite(_P, paths[0], str(hits[0]))], 'the file names %s at :%d' % (pat.search(t.split(NL)[hits[0] - 1]).group(1), hits[0])
                    else:
                        v, lic, act = 'OVERREACHES', 'no line of the file names a node of the page', 'RE-CUT: the row dropped at re-emission'
                        cites = [_cite(_P, paths[0], '1')]
            elif obj == 'the χ-leg' and paths == [K.DIR_PAGE]:
                cites, lic = [_cite(_P, K.DIR_PAGE, '1')], 'the χ page at PLACE-papers (repair 3`s row, by the list`s `# table grade`)'
            elif obj == 'the χ-leg':
                cites = [_cite(_P, K.DIR_PAGE, '1'), _cite(_R, 'tools/chain_page.py', '~| the χ-leg | its own page')]
                v, lic = 'UNDERSTATES', ('the χ-leg`s page exists, THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md, generated under (R183)(5); the row says it '
                                         'will have one when EF_lit_chi`s proof lands -- a fixed string in the generator`s template')
                act = ('RE-CUT: | the χ-leg | `THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md` | -- the χ page`s own form for the ζ-leg, by the template '
                       'repair of relay tools/chain_page.py (Component 3)')
            else:
                raise SystemExit('### REFUSED: a Placement row with no reading: %r' % l[:80])
            rows.append(dict(id='%s:place:%d' % (key, n), source=src, stated='Placement: %s -> %s' % (obj, cell[:90]), by='HAND', cited=cites,
                             licensed=lic, verdict=v, action=act, page=key, kind='placement', line=n))
            continue
        if l.startswith('|'):
            skipped.append('%d %s' % (n, l[:60]))
            continue
        if sec == 'Glossary' and l.startswith('- **'):
            gi += 1
            ent = K_GLOSS[gi - 1]
            if not l.startswith('- **%s** — ' % ent[0]):
                raise SystemExit('### REFUSED: glossary line %d is not entry %d (%s)' % (n, gi, ent[0]))
            v, lic, act = 'MATCHES', ('the definition read against the lines cited; its quotations found there; a name of the programme`s own, '
                                      'defined in its own words'), 'none'
            if gi in GLOSS_NOTE:
                lic += '; ' + GLOSS_NOTE[gi]
            if gi in GLOSS_FIND:
                v, lic, act = GLOSS_FIND[gi]
            rows.append(dict(id='%s:gloss:%d' % (key, gi), source=src, stated='glossary entry %d: %s' % (gi, ent[0]), by='HAND',
                             cited=[_cite(*c) for c in GLOSS_CITES[gi]], licensed=lic, verdict=v, action=act, page=key, kind='glossary', line=n))
            continue
        for j, s in enumerate(_sentences(l), 1):
            hit = [p for p in PROSE if s.startswith(p[0])]
            if len(hit) != 1:
                raise SystemExit('### REFUSED: %s :%d sentence %d is read by %d entries: %r' % (pname, n, j, len(hit), s[:80]))
            nd, v, cs, lic = hit[0]
            rows.append(dict(id='%s:prose:%d.%d' % (key, n, j), source=src, stated=s[:200], by='HAND', cited=[_cite(*c) for c in cs],
                             licensed=lic, verdict=v, action=PROSE_RECUT.get(nd, 'none'), page=key, kind='prose', line=n))
    return rows, skipped


K_GLOSS = []


def pages_table(pp_rev=None, bank='b648_table_pages', *a):
    """data/<bank>.txt and .json: both pages at PLACE-papers `pp_rev` (default the revision read, READ_AT) through the licensed-statement
    table; counts by page, kind and verdict; every row one line, every row not MATCHES in full."""
    import licensed_table as LT
    import chain_page as CP
    pp_rev = pp_rev or READ_AT[_P]
    if g(RELAY, 'diff', '--stat', READ_AT[_R], '--', 'data/glossary.txt').strip():
        raise SystemExit('### REFUSED: data/glossary.txt differs from relay %s' % READ_AT[_R])
    K_GLOSS[:] = CP.glossary_entries()
    idx = _tt_index(READ_AT[_R])
    allrows, out = [], []
    for key in ('zeta', 'chi'):
        text = _show(PP, pp_rev, K.PNAME[key])
        rows, skipped = _page_rows(key, text, idx, pp_rev)
        allrows += rows
        out.append((key, rows, skipped))
    counts, faults = LT.table(allrows)
    L = ['b648 -- COMPONENT 3, (R258)(3): THE TWO PAGES THROUGH THE LICENSED-STATEMENT TABLE (%s)' % utc(),
         'read at PLACE-papers %s (the pages), relay %s (the generator, the table, the probes, the lists), SIDE-explicit-formula %s, '
         'SIDE-global-section %s, Mathlib %s' % (pp_rev, READ_AT[_R], READ_AT[_E], READ_AT[_S], READ_AT['mathlib']),
         'the rules: HAND -- the prose sentences and the glossary entries, each citing the lines read, and the Placement rows at the line the '
         'path carries; terminal -- %s' % LT.RULES['terminal'], '']
    if counts is None:
        L += ['### ### **REFUSED: %d rows with faults**' % len(faults)] + ['  %s: %s' % (k, v) for k, v in sorted(faults.items())]
        put_txt(bank + '.txt', L)
        print(L[-len(faults) - 1])
        return
    for key, rows, skipped in out:
        c = collections.Counter((r['kind'], r['verdict']) for r in rows)
        L.append('### %s (%s): %d rows; %d lines not sentences (a title, a heading, a table`s head) -- %s' % (
            K.PNAME[key], key, len(rows), len(skipped), '; '.join(skipped)))
        for kind in ('prose', 'glossary', 'node', 'placement', 'correspondence'):
            L.append('  %-15s %s' % (kind, '  '.join('%s %d' % (v, c[(kind, v)]) for v in LT.VERDICTS)))
        L.append('')
    L.append('### NOT MATCHES, IN FULL')
    for r in allrows:
        if r['verdict'] != 'MATCHES':
            L += ['  [%s] %s %s by %s' % (r['verdict'], r['id'], r['source'], r['by']), '      stated: ' + r['stated'], '      licensed: ' + r['licensed'],
                  '      cited: ' + ', '.join(r.get('cited') or []), '      action: ' + r['action']]
    L += ['', '### EVERY ROW']
    L += ['  %s | %s | %s | %s | %s' % (r['id'], r['source'], r['verdict'], r['by'], ', '.join(r.get('cited') or [])) for r in allrows]
    tot = collections.Counter(r['verdict'] for r in allrows)
    L += ['', '### ### **%d ROWS: %s.**' % (len(allrows), ', '.join('%s %d' % (v, tot[v]) for v in LT.VERDICTS))]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(read_at=dict(READ_AT, pages=pp_rev), rows=allrows))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE CENSUS AT v0.8
# ### (R258)(4) and the author's word at b648 (data/b648_author_answers.txt, the census prompts): a kernel the cluster rules leave unplaced
# ### takes a cluster only as SERVED-KEYSTONE -- the roster keystones naming it at PLACE-papers agree on one cluster, each named -- or as
# ### TERMINAL-HEADS -- its heads in a cluster's terminal set, listed; a split stays blank with its clusters beside it; a kernel no keystone
# ### names, and whose heads name no cluster, stays blank. The census itself (p2-42) is not counted: it names every kernel by construction.
CEN_SELF = ('p2-42',)
REG_ID = re.compile(r'^(?:d1-|1\.5[a-h]-|p2-d?|m5-)\d+$')


def _kid(r):
    """a roster keystone's name: its REGISTRY id, else its file's name (b647's bank cuts an id that is a file name at 46 characters)."""
    return r['id'] if REG_ID.match(r['id']) else os.path.basename(r['path'])


def kernel_cites(*a):
    """data/b648_kernel_cites.txt/.json: for each kernel b647's columns leave unplaced, the roster keystones naming it by repository name at
    PLACE-papers (READ_AT), their clusters, its heads in the terminal sets, and the reading under the author's word."""
    import licensed_table as LT
    j = jl('b647_census_columns.json')['rows']
    ros = [r for r in j if r['kind'] == 'roster']
    ks = [r for r in j if r['kind'] == 'kernel' and not r['cluster']]
    T = json.loads(_show(RELAY, READ_AT[_R], 'data/terminal_table.json'))['rows']
    txt = dict((r['id'], _show(PP, READ_AT[_P], r['path'])) for r in ros)
    unread = [r['path'] for r in ros if txt[r['id']] is None]
    if unread:
        sys.exit('### ROSTER PATHS UNREAD AT PLACE-papers %s: %s -- NOTHING WRITTEN' % (READ_AT[_P], unread))
    rows = []
    L = ['b648 -- COMPONENT 4, (R258)(4): THE UNPLACED KERNELS AND THE KEYSTONES THAT NAME THEM (%s)' % utc(),
         'read at PLACE-papers %s (the 48 roster keystones of b647`s columns, relay data/b647_census_columns.json) and relay %s (the terminal '
         'table); a keystone names a kernel when its text carries the repository name with no letter, digit, _ or - on either side; the census '
         'itself (%s) is printed and not counted' % (READ_AT[_P], READ_AT[_R], ', '.join(CEN_SELF)), '']
    for k in ks:
        kn = k['id'].split()[0]
        pat = re.compile(r'(?<![\w-])' + re.escape(kn) + r'(?![\w-])')
        hits = [(_kid(r), r['cluster'], len(pat.findall(txt[r['id']]))) for r in ros if pat.search(txt[r['id']])]
        counted = [h for h in hits if h[0] not in CEN_SELF]
        cl = collections.Counter(h[1] for h in counted)
        names = set(x['name'].split('.')[-1] for x in T if x['repo'] == kn)
        heads = dict((c, sorted(s & names)) for c, s in LT.TERMINAL_SETS.items() if s & names)
        if len(heads) == 1:
            c, how = list(heads)[0], 'TERMINAL-HEADS: %s' % ', '.join(list(heads.values())[0])
        elif len(cl) == 1:
            c, how = list(cl)[0], 'SERVED-KEYSTONE: %s' % ', '.join(h[0] for h in counted)
        elif cl:
            c, how = '', 'split: %s' % ', '.join('%s %d' % kv for kv in sorted(cl.items(), key=lambda kv: (-kv[1], kv[0])))
        else:
            c, how = '', 'named by no keystone'
        rows.append(dict(kernel=kn, id=k['id'], cluster=c, how=how, hits=hits, counted=len(counted), heads=heads))
        L += ['  %-34s %-16s %s' % (kn, c or '### BLANK', how),
              '      keystones naming it: %s' % ('; '.join('%s (%s) x%d%s' % (i, cc, n, ' NOT COUNTED' if i in CEN_SELF else '') for i, cc, n in hits) or 'none'),
              '      heads in a cluster`s terminal set: %s' % (heads or 'none')]
    placed = [r for r in rows if r['cluster']]
    L += ['', '### ### **KERNELS %d: PLACED %d (%s) ; BLANK %d (split %d, named by no keystone %d).**' % (
        len(rows), len(placed), ', '.join('%s %s' % (r['kernel'], r['cluster']) for r in placed), len(rows) - len(placed),
        sum(r['how'].startswith('split') for r in rows), sum(r['how'] == 'named by no keystone' for r in rows))]
    put_txt('b648_kernel_cites.txt', L)
    put_json('b648_kernel_cites.json', dict(at=utc(), read_at=dict(READ_AT), rows=rows))
    print(L[-1])


V8_TAG = '## Back matter of the v0.8 edition — written 2026-10-10 by b648 under the author’s ruling `(R258)`(4), by the form of `(R187)`(5)'


def _how(r):
    h = r.get('how') or ''
    if h.startswith('path: '):
        return 'by path (%s)' % ', '.join(x.replace('\\', '') for x in h[len('path: '):].replace('(^|/)', '').split('|') if x)
    if h.startswith('terminals: '):
        return 'by the terminals it names (%s)' % h.split('terminals: ')[-1].replace('|', '/')
    return h.replace('|', '/')


def _v8_rows():
    j = jl('b647_census_columns.json')['rows']
    kc = dict((r['id'], r) for r in jl('b648_kernel_cites.json').get('rows') or [])
    out = []
    for r in j:
        x = dict(r)
        if r['kind'] == 'kernel' and r['id'] in kc:
            x['cluster'], x['how'] = kc[r['id']]['cluster'], kc[r['id']]['how']
        x['phase'] = '' if r.get('phase') in (None, '', '-') else r['phase']
        out.append(x)
    return out


def _v8_backmatter(rows):
    import licensed_table as LT
    lab = lambda r: (('%s `%s`' % (r.get('row'), _kid(r))) if r['kind'] == 'roster' else ('`%s`' % r['id']))  # noqa: E731
    bl_p = [r for r in rows if not r['phase']]
    bl_c = [r for r in rows if not r['cluster']]
    bl_m = [r for r in rows if not r['maturity']]
    by_m = collections.Counter(r['maturity'] or 'blank' for r in rows)
    kc = jl('b648_kernel_cites.json').get('rows') or []
    L = ['', V8_TAG, '',
         '### The readings v0.8 adds, each the seat’s and strikeable', '',
         '- **Maturity.** How far a document’s claims are licensed by the kernels, read from its rows in the licensed-statement table (relay '
         '`tools/licensed_table.py`), in the rule’s own words: “%s”' % LT.MATURITY_RULE,
         '- **Phase and cluster.** The phase is REGISTRY’s, read from the document’s REGISTRY row or the section heading it sits under. The '
         'cluster is one of eight -- %s -- read by the document’s path first, then by the terminals it names (relay `tools/licensed_table.py`, '
         'PATH_RULES and TERMINAL_SETS); a document neither reading places is left blank.' % ', '.join(LT.CLUSTERS),
         '- **The kernels the rules leave unplaced** (the author’s word at b648, relay `data/b648_author_answers.txt`): a kernel takes a cluster '
         'as SERVED-KEYSTONE when the roster keystones naming it agree on one cluster, each keystone named, or as TERMINAL-HEADS when its heads '
         'lie in one cluster’s terminal set, the heads listed; where the keystones naming it split, the cluster stays blank and the split is '
         'printed beside it, a kernel that serves several subjects being a finding about the kernel; a kernel no keystone names stays blank. '
         'The census itself is not counted among the keystones, since it names every kernel by construction (relay `data/b648_kernel_cites.txt`). '
         'Placed: %s. No cluster is assigned by the resemblance of a name.' % (
             ', '.join('%s (%s)' % (r['kernel'], r['cluster']) for r in kc if r['cluster']) or 'none'),
         '- **The kernels’ rows** are read at the mains b647 read (relay `data/b647_census_columns.txt`). At b648 two mains moved by the sorry '
         'quarantine under `(R258)`(2): SIDE-kernel and SIDE-lv-conservation, whose legacy `sorry` declarations left main for a branch '
         'sorry-quarantine-<kernel>, named in each kernel’s ERRATA.md; their maturity is b647’s reading, not re-read here.',
         '- **The numerals.** In this back matter every numeral is a count of the rows below or of a table’s rows.', '',
         '### The phase, cluster and maturity of every keystone, companion and kernel', '',
         '| # | kind | document or kernel | phase | cluster | how the cluster is read | maturity | why |', '|:--|:--|:--|:--|:--|:--|:--|:--|']
    for i, r in enumerate(rows, 1):
        L.append('| %d | %s | %s | %s | %s | %s | %s | %s |' % (
            i, r['kind'], lab(r) + (' (%s)' % r['path'] if r['kind'] != 'kernel' else ''), r['phase'] or '—', r['cluster'] or '—', _how(r),
            r['maturity'] or '—', (r.get('why') or '').replace('|', '/')))
    L += ['', '*%d rows: %d keystones, %d Day 1 companions, %d kernels. Maturity: %s. Blank cells are listed below and none is counted as a '
          'value.*' % (len(rows), sum(r['kind'] == 'roster' for r in rows), sum(r['kind'] == 'companion' for r in rows),
                       sum(r['kind'] == 'kernel' for r in rows), ', '.join('%s %d' % (m, by_m[m]) for m in list(LT.MATURITY) + ['blank'] if by_m[m])),
          '', '### The blank cells', '',
          '- **Phase blank (%d)**: %s.' % (len(bl_p), ', '.join(lab(r) for r in bl_p) or 'none'),
          '- **Cluster blank (%d)**: %s.' % (len(bl_c), '; '.join('%s -- %s' % (lab(r), _how(r)) for r in bl_c) or 'none'),
          '- **Maturity blank, not yet in the table (%d)**: %s.' % (len(bl_m), ', '.join(lab(r) for r in bl_m) or 'none'),
          '', '### Version history', '',
          '- **v0.8, 2026-10-10 (b648, `(R258)`(4))**: the phase, cluster and maturity columns for every keystone, Day 1 companion and kernel, '
          'from the banks of b645-b647; the kernels the rules leave unplaced placed by the author’s word where the keystones naming them agree, '
          'the rest blank and listed; maturity blank where no table reaches, listed; the glossary block regenerated (the surround, priced).',
          '- **v0.7.1, 2026-10-09 (b644)** and the editions before it: carried above.']
    return L


def edition8(*a):
    """PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8.md beside v0.7.1 (unedited), and data/b648_edition.json. `dry`: the scratchpad."""
    import chain_page as CP
    if not jl('b648_kernel_cites.json'):
        sys.exit('### NO KERNEL CITES BANK -- NOTHING WRITTEN')
    v71 = lines_of(_show(PP, 'HEAD', K.CEN71))
    nb = CP.glossary_block()
    ob = nb[:4] + ['- **%s** — %s *(%s)*' % e for e in CP.glossary_entries()[:-2]]
    at = [i for i in range(len(v71)) if v71[i:i + len(ob)] == ob]
    vl = [i for i, l in enumerate(v71) if l.startswith('*v0.7.1, 2026-10-09')]
    if len(at) != 1 or len(vl) != 1:
        sys.exit('### THE OLD GLOSSARY BLOCK (%s) OR THE v0.7.1 VERSION LINE (%s) NOT FOUND ONCE -- NOTHING WRITTEN' % (at, vl))
    i, j = at[0], vl[0]
    rows = _v8_rows()
    ver = ('*v0.8, 2026-10-10 -- the phase, cluster and maturity columns for every keystone, Day 1 companion and kernel (%d rows), from the '
           'banks of b645-b647; the kernels the cluster rules leave unplaced placed by the author’s word where the keystones naming them agree '
           '(%d), the rest blank and listed; maturity blank where no table reaches, listed; the glossary block regenerated; v0.7.1 stands beside '
           'it, unedited.*' % (len(rows), sum(1 for r in rows if r['kind'] == 'kernel' and r['cluster'] and r['how'].startswith(('SERVED', 'TERMINAL-HEADS')))))
    out = v71[:i] + nb + v71[i + len(ob):j] + [ver, ''] + v71[j:] + _v8_backmatter(rows)
    b = (NL.join(out) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b648_census_dry.md') if DRY else os.path.join(PP, *K.CEN8.split('/'))
    if not DRY and os.path.exists(dest) and 'regen' not in a:
        sys.exit('### v0.8 EXISTS -- NOTHING WRITTEN (`regen` regenerates this act`s own edition, on the author`s word before the seal)')
    _write(dest, b)
    put_json('b648_edition.json', dict(at=utc(), path=K.CEN8, sha256=sha(b), bytes=len(b), lines=len(out), glossary_at=i + 1,
                                       glossary_lines=len(nb), backmatter=out.index(V8_TAG) + 1, v71_lines=len(v71),
                                       v71_at=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), dry=DRY))
    print('  %s : %d lines, %d bytes, sha256 %s ; the glossary block %d lines at :%d (was %d) ; the back matter at :%d' % (
        ('DRY ' + dest) if DRY else K.CEN8, len(out), len(b), sha(b)[:16], len(nb), i + 1, len(ob), out.index(V8_TAG) + 1))


def termscan8(*a):
    """data/b648_census_termscan.txt: the scanner over the census at v0.8, its verdict printed."""
    t = _scan(os.path.join(PP, *K.CEN8.split('/')))
    put_txt('b648_census_termscan.txt', t.rstrip(NL).split(NL))
    print('  ' + ' ; '.join(l.strip() for l in t.split(NL) if re.search(r'live uses|VERDICT', l)) + ' ; clean %s' % _clean(t))


def edition_diff8(*a):
    """data/b648_edition_diff.txt: v0.8 against v0.7.1, by section, every changed line printed with its kind."""
    import difflib
    v71 = lines_of(_show(PP, 'HEAD', K.CEN71))
    v8 = lines_of(io.open(os.path.join(PP, *K.CEN8.split('/')), encoding='utf-8').read())
    L = ['b648 -- COMPONENT 4: v0.8 AGAINST v0.7.1, BY SECTION (%s)' % utc(), '']
    kinds, removed = collections.Counter(), 0
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, v71, v8, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        removed += a2 - a1
        head = next((v8[k] for k in range(min(b1, len(v8) - 1), -1, -1) if v8[k].startswith('#')), '(the head)')
        kinds[tag] += 1
        L.append('### %s at v0.7.1 :%d-:%d -> v0.8 :%d-:%d ; section: %s ; removed %d, added %d' % (
            tag.upper(), a1 + 1, a2, b1 + 1, b2, head[:90], a2 - a1, b2 - b1))
        L += ['    - %s' % l[:200] for l in v71[a1:a2]][:6] + ['    + %s' % l[:200] for l in v8[b1:b2]][:8]
    L += ['', '### ### **HUNKS %d (%s) ; v0.7.1 LINES REMOVED OR REPLACED : %d.**' % (sum(kinds.values()), dict(kinds), removed)]
    put_txt('b648_edition_diff.txt', L)
    print(NL.join(L[2:]))


# ### THE SECOND READER, (R258)(4): b646's form carried (its lead and command builders, its no-disclosure arm and outside names), the
# ### directory C:\reader_b648; the census at v0.8 as committed, whole; the ruling's two questions; run by the author on the author's
# ### PowerShell from a directory with no project memory; scored by hand first (data/b648_reader_handread.txt), then by the needles below.
READER8 = dict(dir='C:/reader_b648', doc='census.md', what='the census of a research programme`s papers and kernels, at its edition v0.8',
               questions=('What does maturity mean in this census?', 'Which documents and kernels does the census mark ONGOING?'))


def _b6r8():
    import b646_record as B6
    B6.READER = dict(B6.READER, dir=READER8['dir'])
    return B6


def _reader_task8():
    B6 = _b6r8()
    r = READER8
    n = len(r['questions'])
    return (B6._reader_lead() + NL + NL +
            'You are an independent reader. You know nothing of the research programme the packet describes, and that is the point. The packet has '
            'two files: %s, %s, and questions.txt, %d questions. Read the document and answer each question in your own words, from the document '
            'alone, in a few sentences each: say what the text says, not what you know of the mathematics, and say plainly where the text is '
            'unclear to you. Write the file %s\\answers.txt with exactly %d sections, headed %s, each followed by your answer to that question; '
            'then a section headed UNCLEAR: listing any sentence of the document you could not follow, or the word none. Then stop.' % (
                r['doc'], r['what'].replace('`', "'"), n, r['dir'].replace('/', '\\'), n, ', '.join('ANSWER %d:' % (i + 1) for i in range(n))))


def reader_packet8(*a):
    """data/b648_reader_packet.txt, data/b648_reader_command.txt (the one line) and data/b648_reader_packet/: v0.8 as committed with the two
    questions, staged at C:\\reader_b648 (refused if it exists and is not empty), the no-disclosure arm and the outside names checked."""
    import b616_record as R6
    B6 = _b6r8()
    R4 = B6._R4()
    r = READER8
    doc = _show(PP, 'HEAD', K.CEN8)
    if not doc or not doc.strip():
        sys.exit('### v0.8 IS NOT AT PLACE-papers HEAD -- NOTHING WRITTEN')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(r['questions']))
    task = _reader_task8()
    nd = R6.nd_hits(doc + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in R4.OUTSIDE_NEEDLES if n in doc]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT (%s) OR AN OUTSIDE NAME (%s) -- NOTHING WRITTEN' % (
            dict((k, v) for k, v in nd.items() if v), outside))
    pdir = os.path.join(SP if DRY else D, 'b648_reader_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in ((r['doc'], doc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    staged = (('packet/' + r['doc'], doc), ('packet/questions.txt', qs), ('lead.txt', B6._reader_lead()), ('full_prompt.txt', task))
    if not DRY and 'banks' in a:   # ### the banks rewritten over a packet already staged: every staged file must equal what would be staged
        differ = [n_ for n_, t_ in staged if open(os.path.join(r['dir'], n_), 'rb').read() != (t_.rstrip(NL) + NL).encode('utf-8')]
        if differ:
            sys.exit('### THE STAGED PACKET DIFFERS AT %s -- NOTHING WRITTEN' % differ)
    elif not DRY:
        if os.path.exists(r['dir']) and os.listdir(r['dir']):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- NOT WRITTEN' % r['dir'])
        os.makedirs(r['dir'] + '/packet', exist_ok=True)
        for n_, t_ in staged:
            _write(os.path.join(r['dir'], n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    # ### the one line the author pastes whole: it moves to the reader's directory itself (b648)
    cmd = 'Set-Location %s; %s' % (r['dir'].replace('/', '\\'), B6._reader_cmd())
    L = ['b648 -- THE SECOND READER`S PACKET, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/%s %d bytes, sha256 %s, the census at v0.8 as committed at PLACE-papers %s ; packet/questions.txt ; lead.txt ; '
         'full_prompt.txt) ; banked: relay data/b648_reader_packet/' % (r['dir'], r['doc'], len(doc.encode('utf-8')), sha(doc.encode('utf-8')),
                                                                        g(PP, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### the questions, (R258)(4)`s two: %s' % ' / '.join(r['questions']),
         '### the no-disclosure arm: %s ; outside names: %s' % (dict(nd), outside or 'NONE'),
         '', '### the command, run by the author on the author`s PowerShell from %s, a directory with no project memory (one line, banked alone '
         'at relay data/b648_reader_command.txt):' % r['dir'], '    ' + cmd]
    put_txt('b648_reader_packet.txt', L)
    put_txt('b648_reader_command.txt', [cmd])
    print(NL.join(L[2:]))


# ### the needles for the two questions, written before the answers are read: (pattern, label, pattern, label)
READER8_NEEDLES = {
    1: (r'licens', 'names licensing by the kernels', r'(?=[\s\S]*ONGOING)(?=[\s\S]*SETTLED)', 'names ONGOING and SETTLED'),
    2: (r'A_Place_to_Stand|d1-1|monograph', 'names the monograph', r'(?=[\s\S]*SIDE-)(?=[\s\S]*(?:companion|Exhaustive_Enumeration|'
        r'Seven_Mechanism_Classes|ONE_PAGE_PROOF|Spectral_Inertness))', 'names a companion and a kernel'),
}


def reader_score8(*a):
    """data/b648_reader_answers.txt, data/b648_reader_compare.txt and .json: the second reader's answers copied from off D:\\, each scored by
    the needles above and beside it the seat's hand reading (data/b648_reader_handread.txt, written first), both figures; refuses without the
    hand reading."""
    r = READER8
    src = os.path.join(r['dir'], 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    hr = rd('b648_reader_handread.txt')
    if not re.search(r'^HAND \d: (AGREE|DIFFER)', hr, re.M):
        sys.exit('### THE HAND READING IS NOT BANKED -- THE NEEDLES ARE NOT READ BEFORE IT')
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b648_reader_answers.txt'), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in re.finditer(r'^ANSWER (\d):\s*(.*?)(?=^ANSWER \d:|^UNCLEAR:|\Z)', t, re.M | re.S))
    lg = os.path.join(r['dir'], 'reader_run.log')
    lb = open(lg, 'rb').read() if os.path.exists(lg) else None
    lt = lb.decode('utf-16') if lb and lb[:2] in (b'\xff\xfe', b'\xfe\xff') else (lb.decode('utf-8', 'replace') if lb else '')
    ctl = bool(re.search(r'MEMORY\.md', 'x MEMORY.md y'.encode('utf-16').decode('utf-16')))
    mem = ('memory named in the run log: %s (read as %s, %d chars; the planted control fires: %s)' % (
        bool(re.search(r'MEMORY\.md|[\\/]memory[\\/]', lt)), 'UTF-16' if lb[:2] in (b'\xff\xfe', b'\xfe\xff') else 'UTF-8', len(lt), ctl)
           if lb else 'the run log absent')
    hand = dict((int(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^HAND (\d): (AGREE|DIFFER)', hr, re.M))
    L = ['b648 -- THE SECOND READER: ANSWERS SCORED BY THE NEEDLES AND BY HAND (%s)' % utc(), '',
         '### the answers: relay data/b648_reader_answers.txt, copied from %s ; the reader`s session: %s' % (src, mem),
         '### the hand reading: relay data/b648_reader_handread.txt, banked before the needles were read', '']
    res, n_ok = {}, 0
    for q in sorted(READER8_NEEDLES):
        a_ = ans.get(q, '')
        p1, l1, p2, l2 = READER8_NEEDLES[q]
        m1, m2 = bool(re.search(p1, a_, re.I)), bool(re.search(p2, a_))
        ok = m1 and m2
        n_ok += ok
        why = ['%s %s' % (l1, m1), '%s %s' % (l2, m2)]
        res[q] = dict(question=r['questions'][q - 1], answer=a_, needle=ok, why=why, hand=hand.get(q))
        L += ['### QUESTION %d: %s' % (q, r['questions'][q - 1]), '    the reader: %s' % (a_ or '### NO ANSWER'),
              '    the needles: %s ; ### %s' % ('; '.join(why), 'AGREE' if ok else 'DIFFER'), '    by hand: %s' % (hand.get(q) or '### NOT READ'), '']
    kh = sum(1 for v in hand.values() if v == 'AGREE')
    unclear = re.search(r'^UNCLEAR:\s*(.*)\Z', t, re.M | re.S)
    L += ['### NOTE, beside the score: %s' % n_ for n_ in re.findall(r'^NOTE: (.*)$', hr, re.M)]
    L += ['### UNCLEAR, the reader`s: %s' % (' '.join(unclear.group(1).split())[:1500] if unclear else '### NONE GIVEN'), '',
          '### ### **BY THE NEEDLES %d OF %d ; BY HAND %d OF %d.**' % (n_ok, len(READER8_NEEDLES), kh, len(READER8_NEEDLES))]
    put_txt('b648_reader_compare.txt', L)
    put_json('b648_reader_compare.json', dict(at=utc(), answers=res, needles=n_ok, hand=kh, of=len(READER8_NEEDLES),
                                              unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE h2 ROW
# ### (R258)(5): h1_complete_at_Phi's docstring against the glossary's h2, both quoted by line; the surround's sentence that the faces are one
# ### node cited; the docstring's re-cut sentence proposed and NOT applied (a kernel docstring on main is edited under a later ruling, with the
# ### lv-conservation build under the hold); no kernel edit.
H2_AT = {'lv': ('D:/SIDE-lv-conservation', 'b2238d4', 'SIDELvConservation/CouplingsAtPhi.lean', (415, 416)),
         'gloss': (RELAY, '8a8e9cc8', 'data/glossary.txt', (10, 10)),
         'h2sign': ('D:/SIDE-explicit-formula', '82550e4', 'SIDEExplicitFormula/H2Sign.lean', (28, 29)),
         'surround': (PP, '6783833', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', (116, 116)),
         'faces': (PP, '6783833', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', (167, 167))}
H2_RECUT = ('This theorem is the `h1` leg of the T3′ bracket; its `h2` leg -- nonvanishing of the Mellin transform at the operative point, '
            'this kernel’s register and not the Prop the programme’s glossary names h2, which is `h2_sign`, Weil positivity on classK '
            '(SIDE-explicit-formula `SIDEExplicitFormula/H2Sign.lean` :28-:29) -- remains outstanding.')


def h2_row(*a):
    """data/b648_h2_row.txt and .json: the named row, its sources quoted by line at their revisions, the re-cut proposed, the row checked by
    the table's own check(); no kernel file is written."""
    import licensed_table as LT
    q = {}
    for k, (repo, rev, path, (x, y)) in H2_AT.items():
        t = _show(repo, rev, path)
        if t is None:
            sys.exit('### %s@%s:%s UNREAD -- NOTHING WRITTEN' % (repo, rev, path))
        q[k] = t.split(NL)[x - 1:y]
    if 'nonvanishing of' not in q['lv'][0] or 'the Mellin transform at the operative point' not in q['lv'][1]:
        sys.exit('### THE DOCSTRING`S SENTENCE IS NOT AT :415-:416 -- NOTHING WRITTEN')
    if not q['gloss'][0].startswith('h2\t'):
        sys.exit('### THE GLOSSARY`S h2 IS NOT AT :10 -- NOTHING WRITTEN')
    cite = lambda k: '%s@%s:%s:%s' % (os.path.basename(H2_AT[k][0]), H2_AT[k][1], H2_AT[k][2], '%d-%d' % H2_AT[k][3] if H2_AT[k][3][0] != H2_AT[k][3][1] else H2_AT[k][3][0])  # noqa: E731
    row = dict(id='h2:CouplingsAtPhi:415', source='SIDELvConservation/CouplingsAtPhi.lean:415-416',
               stated='`h2` (nonvanishing of the Mellin transform at the operative point) remains the outstanding obligation',
               licensed=('the glossary defines h2 as the programme`s name for the open clause, in the kernel the one Prop h2_sign (data/glossary.txt '
                         ':10), h2_sign being Weil positivity on classK (H2Sign.lean :28-:29); no source the table reads states h2 as the '
                         'nonvanishing of a Mellin transform, and none equates the two statements'),
               by='HAND', cited=[cite(k) for k in ('lv', 'gloss', 'h2sign', 'surround', 'faces')], verdict='UNLICENSED',
               action=('W-ORD-LV-H2-DOCSTRING, TRIGGER a later ruling that edits the docstring on SIDE-lv-conservation`s main with its build '
                       'under the hold (RUN-BENEATH-HOLD territory); the re-cut proposed below, NOT applied'),
               proposed=H2_RECUT)
    faults = LT.check(row)
    L = ['b648 -- COMPONENT 5, (R258)(5): h2`S TWO DEFINITIONS AS A NAMED ROW (%s)' % utc(), '',
         '### (1) THE lv-conservation REGISTER -- h1_complete_at_Phi`s docstring, %s:' % cite('lv')] + ['    | ' + x for x in q['lv']] + [
         '', '### (2) THE WEIL REGISTER -- the glossary`s h2, %s (name, definition, source; tab-separated):' % cite('gloss')] + [
         '    | ' + x.replace('\t', '  ||  ') for x in q['gloss']] + [
         '    its source, %s:' % cite('h2sign')] + ['    | ' + x for x in q['h2sign']] + [
         '', '### (3) THE SURROUND, that the reduction has one node and its faces are one wall -- %s and %s:' % (cite('surround'), cite('faces'))] + [
         '    | ' + x[:400] + (' [...]' if len(x) > 400 else '') for x in q['surround'] + q['faces']] + [
         '', '### THE ROW (tools/licensed_table.py, its cells):'] + ['    %-9s %s' % (k, row[k] if not isinstance(row[k], list) else ', '.join(row[k]))
                                                               for k in ('id', 'source', 'stated', 'licensed', 'by', 'cited', 'verdict', 'action')] + [
         '', '### THE RE-CUT PROPOSED, NOT APPLIED -- in place of the docstring`s sentence at :415-:416:', '    ' + H2_RECUT,
         '', '### check(): %s' % (faults or 'the table takes the row'),
         '', '### ### **ONE ROW, UNLICENSED, ITS RE-CUT PROPOSED AND NOT APPLIED ; NO KERNEL FILE WRITTEN (SIDE-lv-conservation main %s).**' %
         g('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'main').strip()]
    put_txt('b648_h2_row.txt', L)
    put_json('b648_h2_row.json', dict(at=utc(), row=row, quotes=q, faults=faults))
    print(L[-1])


LIST_HEAD = ['# b648 -- (R258)(3), THE TABLE`S GRADE ON THE PAGE: b643`s list (relay data/%s), every line unchanged, with the one line',
             '# `# table grade` appended, by which the generator prints the terminal table`s grade beside a node`s E0 grade where the two',
             '# differ and, on the ζ page, names the χ page in the χ-leg`s Placement row (relay tools/chain_page.py, `node_table_grade`). A list',
             '# without that line emits exactly as before.', '#']


def lists(*a):
    """data/b648_nodes_zeta.txt and data/b648_nodes_chi.txt: b643's lists, byte for byte, beneath a five-line head and above the one line."""
    for k, old in (('zeta', 'b643_nodes_zeta.txt'), ('chi', 'b643_nodes_chi.txt')):
        body = rd(old).rstrip(NL).split(NL)
        L = [x % old if '%s' in x else x for x in LIST_HEAD] + body + ['#', '# table grade']
        put_txt('b648_nodes_%s.txt' % k, L)
        print('b648_nodes_%s.txt: %d lines, b643`s %d unchanged beneath the head' % (k, len(L), len(body)))


LISTS_IN_FORCE = {'zeta': 'b648_nodes_zeta.txt', 'chi': 'b648_nodes_chi.txt'}


def page_arms(tag='', *a):
    """data/b648_page_arms[_<tag>].txt: the page arms (G-CHAIN-PAGE, G-CHAIN-PAGE-CHI) on the lists in force (b643's for the first run,
    data/b648_page_arms.txt; b648's marked lists after repair 3) against PLACE-papers HEAD, and the frozen control
    (tools/test_chain_page_b596.py control(): b592's lists against PLACE-papers ba5f0ea), from the tagged runs on with the E0 rule loaded
    at the control's relay pin as the suites run it since b626 (b644_checks extra_sources) -- b602's page_arms, carried."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    import chain_page as CP
    import b626_record as R26
    lists = LISTS_IN_FORCE if tag else NODES
    L = ['b648 -- COMPONENT 3: THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s, relay %s (%s)%s' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc(), (' -- ' + tag) if tag else '')]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, lists[k]), os.path.join(SP, '_b648_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', lists[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    rule = CP.E0
    if tag:
        CP.E0 = R26.e0_module(T.RELAY_PIN)
    try:
        c = T.control()
    finally:
        CP.E0 = rule
    L.append('### the control`s E0 rule: %s' % (('loaded at relay %s' % T.RELAY_PIN) if tag else 'the live rule (b602`s form)'))
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b648_page_arms%s.txt' % (('_' + tag) if tag else ''), L)
    print(NL.join(l[:220] for l in L))


# ================================================================================ COMPONENTS 6 AND 7: THE SEAL, THE RE-CUT ORDER, THE ROOT, THE RECORD
# ### b647's routes carried (tools/b647_record.py :1566-:2017), every name and every sentence re-written for b648's banks.
def kernels(*a):
    """data/b648_kernels_face.json: every kernel's main, tags, branches and tracked status, read before the seal for N5."""
    import b641_record as R41
    put_json('b648_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_SHORT = ['(a) a commit message naming the wrong ledger line', '(b) a recursive grep over a kernel tree',
                '(c) two template repairs that reached unmarked lists', '(d) a scratch copy written outside the scratchpad',
                '(e) a reader command that could not be pasted whole', '(f) a scratch script broken by a heredoc backslash',
                '(g) two stream edits on a scratch script', '(h) a template repair not committed alone']


def defects(*a):
    """data/b648_defects.json from data/b648_defects.txt (the seat's list): every defect line, and the short forms."""
    t = rd('b648_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    if len(ds) != len(DEFECT_SHORT):
        sys.exit('### %d DEFECT LINES AGAINST %d SHORT FORMS -- NOTHING WRITTEN' % (len(ds), len(DEFECT_SHORT)))
    put_json('b648_defects.json', dict(at=utc(), defects=ds, short=DEFECT_SHORT, correction=''))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b648_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b648 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-24s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    put_txt('b648_seal_check_%s.txt' % (a[0] if a else 'record'), L)
    print(NL.join(L[2:]))


ROOT_EXCLUDE = re.compile(r'^b648_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b648_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                  and ('data/' + f) != K.EXPORT)


def root(*a):
    """(R251)(3): the act root, the last step of the act; every bank it names written LF (compute refuses CR LF)."""
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b648_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b648'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """the root recomputed from its banked items offline and a one-byte change on a copy of one bank moving it; the root order read locally."""
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b648_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b648 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b648_root_arm.txt', L)
    put_json('b648_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    """the terminal table regenerated at the end and diffed against relay HEAD`s table, by row."""
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b648 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b648_table_final.txt', L)
    put_json('b648_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ### (R258)(6): THE RE-CUT ORDER -- per document its OVERREACHES and UNLICENSED counts and its bytes, from the banks; raised to the author
# ### before the root as one prompt; the author's word sets b649 and after.
def recut_order(*a):
    """data/b648_recut_order.txt and .json: the monograph, the seven companions, the two pages, the h2 row and the kernel docstrings by kernel,
    each with its OVERREACHES and UNLICENSED counts, its bytes and its bank."""
    import b645_worklist as K5
    import b646_worklist as K6
    rows = []
    m = jl('b645_table_monograph.json').get('counts') or {}
    mb = _show(PP, 'HEAD', K5.MONO)
    rows.append(dict(doc=K5.MONO, kind='monograph', over=m.get('OVERREACHES', 0), unl=m.get('UNLICENSED', 0),
                     bytes=len(mb.encode('utf-8')) if mb else None, bank='data/b645_table_monograph.txt'))
    for name, lab in K6.COMPANIONS:
        c = jl('b646_table_%s.json' % name).get('counts') or {}
        p = 'day1/%s.md' % name
        t = _show(PP, 'HEAD', p)
        rows.append(dict(doc='%s (%s)' % (p, lab), kind='companion', over=c.get('OVERREACHES', 0), unl=c.get('UNLICENSED', 0),
                         bytes=len(t.encode('utf-8')) if t else None, bank='data/b646_table_%s.txt' % name))
    pa = jl('b648_table_pages_after.json').get('rows') or []
    for key in ('zeta', 'chi'):
        t = _show(PP, 'HEAD', K.PNAME[key])
        rows.append(dict(doc=K.PNAME[key], kind='page', over=sum(1 for r in pa if r['page'] == key and r['verdict'] == 'OVERREACHES'),
                         unl=sum(1 for r in pa if r['page'] == key and r['verdict'] == 'UNLICENSED'), bytes=len(t.encode('utf-8')) if t else None,
                         bank='data/b648_table_pages_after.txt'))
    KJ = jl('b647_table_kernels.json').get('kernels') or []
    for x in KJ:
        kr = jl('b647_table_%s.json' % x['kernel']).get('rows') or []
        files = sorted(set(r['file'] for r in kr))
        nb = sum(len((_show('D:/' + x['kernel'], x['rev'], f) or '').encode('utf-8')) for f in files)
        onmain = set(g('D:/' + x['kernel'], 'ls-tree', '-r', '--name-only', 'main').split(NL))
        off = [r for r in kr if r['verdict'] in ('OVERREACHES', 'UNLICENSED') and r['file'] not in onmain]
        rows.append(dict(doc='%s docstrings (read at %s)' % (x['kernel'], x['rev']), kind='kernel', over=x['counts'].get('OVERREACHES', 0),
                         unl=x['counts'].get('UNLICENSED', 0), bytes=nb, bank='data/b647_table_%s.txt' % x['kernel'], off_main=len(off)))
    ef = jl('b645_table_docstrings.json').get('counts') or {}
    rows.append(dict(doc='SIDE-explicit-formula docstrings (read at 82550e4)', kind='kernel', over=ef.get('OVERREACHES', 0), unl=ef.get('UNLICENSED', 0),
                     bytes=None, bank='data/b645_table_docstrings.txt', off_main=0))
    h2 = jl('b648_h2_row.json').get('row') or {}
    rows.append(dict(doc='SIDE-lv-conservation CouplingsAtPhi.lean :415-:416 (the h2 row)', kind='h2 row', over=0,
                     unl=1 if h2.get('verdict') == 'UNLICENSED' else 0, bytes=None, bank='data/b648_h2_row.txt'))
    comp = [r for r in rows if r['kind'] == 'companion']
    L = ['b648 -- (R258)(6): THE RE-CUT ORDER, PER DOCUMENT, FROM THE BANKS (%s)' % utc(), '',
         '### document | kind | OVERREACHES | UNLICENSED | together | bytes | bank']
    L += ['  %-62s | %-9s | %4d | %4d | %4d | %s | %s%s' % (r['doc'][:62], r['kind'], r['over'], r['unl'], r['over'] + r['unl'],
                                                         r['bytes'] if r['bytes'] is not None else '-', r['bank'],
                                                         (' ; of them on files now off main: %d' % r['off_main']) if r.get('off_main') else '') for r in rows]
    L += ['', '### the monograph %d ; the seven companions %d together ; the two pages %d ; the kernels` docstrings %d ; the h2 row %d' % (
        rows[0]['over'] + rows[0]['unl'], sum(r['over'] + r['unl'] for r in comp), sum(r['over'] + r['unl'] for r in rows if r['kind'] == 'page'),
        sum(r['over'] + r['unl'] for r in rows if r['kind'] == 'kernel'), sum(r['over'] + r['unl'] for r in rows if r['kind'] == 'h2 row')),
          '### ### **DOCUMENTS %d ; OVERREACHES AND UNLICENSED %d IN ALL.**' % (len(rows), sum(r['over'] + r['unl'] for r in rows))]
    put_txt('b648_recut_order.txt', L)
    put_json('b648_recut_order.json', dict(at=utc(), rows=rows))
    print(NL.join(L[2:]))


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
# ### N5's list in its own words: the template repairs, the re-emitted pages, the census edition, the banks, the reader packet, the record
# ### lines and the trails; and the kernel edits the author's answer ordered, on branches, the quarantines merged
N5_RELAY = {'tools/chain_page.py', 'data/b647_closing_push_out.txt', 'data/act_roots.txt'}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN8)


def TRAIL_HEAD():
    return ('### b648 — lane three, act seventy-five under (R258): the sorry lines classified for the author’s word; the two pages through the '
            'table and re-emitted; the keystone census at v0.8; the h2 row; the re-cut order to the author')


def _n1():
    j = jl('b648_sorry_classification.json')
    rows = j.get('rows') or []
    # ### the classification is the one proposed, the author's Option 1 taking every proposal as made; the entry date git log's
    one = all(r.get('proposed') in ('PROVED', 'QUARANTINED', 'RESTATED') for r in rows) and all(r.get('entered') for r in rows)
    ans = re.search(r'^RESULT \(transcript line (\d+)\)', rd('b648_author_answers.txt'), re.M)
    return [dict(r, classification=r.get('proposed')) for r in rows], one, ans


def _n5():
    face = jl('b648_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b648_|audit_b648_)', x) or re.match(r'^data/terminal_table', x) or x in N5_RELAY)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched, the draft %s unpublished at v4; kernel source touched after the author`s answer alone '
            '(the quarantines on branches sorry-quarantine-<kernel>, merged to main by push_gated.sh; the restatements on branches, unmerged, their '
            'builds RUN-BENEATH-HOLD), every kernel unmoved since the face %s; sealed tools not agreeing %s; PLACE-papers beyond FINDINGS, '
            'OPEN_TRAILS, the two pages and the census edition: %s; relay files of a kind beyond the act`s banks and tools, the template file, the '
            'push-out bank and the root list: %s; no identifier of the author in any outbound request (the act made none but git`s own)' % (
                K.DRAFT, kern_ok, differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


def scores(*a):
    import licensed_table as LT_
    import chain_page as CP
    TF, RA = jl('b648_table_final.json'), jl('b648_root_arm.json')
    _r, _n, sh = seal_hashes()
    rows, one, ans = _n1()
    first_edit = [l for l in g(RELAY, 'log', '--reverse', '--format=%h %s', K.PRE_RELAY + '..HEAD').split(NL) if 'quarantine' in l.lower()][:1]
    n1 = len(rows) == 37 and one and bool(ans) and before_answer_ok()
    tp, ta = jl('b648_table_pages.json').get('rows') or [], jl('b648_table_pages_after.json').get('rows') or []
    arms = rd('b648_page_arms_c2.txt')
    blk = NL.join(CP.glossary_block()) + NL
    same = [p for p in (K.PAGE, K.DIR_PAGE, K.CEN8) if blk in (_show(PP, 'HEAD', p) or '')]
    n2 = LT_.table(tp)[0] is not None and LT_.table(ta)[0] is not None and 'PAGE ARMS PASSING : 2 of 2.' in arms and len(same) == 3
    cols = jl('b648_kernel_cites.json').get('rows') or []
    v8 = _show(PP, 'HEAD', K.CEN8) or ''
    cmp_ = jl('b648_reader_compare.json')
    n3 = '77 rows: 48 keystones, 7 Day 1 companions, 22 kernels' in v8 and '### The blank cells' in v8 and cmp_.get('hand') == 2 and cmp_.get('of') == 2
    h2 = jl('b648_h2_row.json')
    n4 = not h2.get('faults') and len(h2.get('quotes', {}).get('lv') or []) == 2 and len(h2.get('quotes', {}).get('gloss') or []) == 1 \
        and H2_RECUT.count('. ') == 0 and H2_RECUT.endswith('.')
    pt, pc = LT_.table(tp)[0] or {}, LT_.table(ta)[0] or {}
    S = {
        'N1': ('HELD' if n1 else 'REFUTED', '%d lines, each one classification of three and its entry date %s; the author`s answer at transcript line %s; '
               'the first quarantine commit after it: %s' % (len(rows), one, ans.group(1) if ans else '?', first_edit[0][:60] if first_edit else 'none')),
        'N2': ('HELD' if n2 else 'REFUTED', 'every sentence of both pages one verdict: %d rows at PLACE-papers 6783833 (%s), %d after re-emission (%s); '
               'the page arms after re-emission: %s; the glossary block byte for byte in %d of the two pages and v0.8' % (
                   len(tp), dict(pt), len(ta), dict(pc), re.search(r'PAGE ARMS PASSING : \d of 2', arms).group(0) if 'PAGE ARMS PASSING' in arms else '?',
                   len(same))),
        'N3': ('HELD' if n3 else 'REFUTED', 'v0.8 carries the three columns for 77 rows with its blank cells listed %s; the unplaced kernels read under the '
               'author`s word, %d placed; the second reader %s of 2 by hand, %s of 2 by the needles' % (
                   '77 rows: 48 keystones' in v8, sum(1 for r in cols if r['cluster']), cmp_.get('hand'), cmp_.get('needles'))),
        'N4': ('HELD' if n4 else 'REFUTED', 'the h2 row quotes the docstring at :415-:416 and the glossary at :10 by line, its source at H2Sign.lean :28-:29, '
               'the surround at :116 and :167; one re-cut sentence proposed, not applied; check() faults %s' % (h2.get('faults') or 'none')),
        'N5': _n5(),
        'S1': ('HELD' if all(r['by'] in ('HAND', 'terminal') for r in tp + ta) else 'REFUTED',
               'every page row HAND with its lines cited or by the terminal rule; the non-MATCHES rows printed in full in the bank'),
        'S2': ('HELD' if LT_.table(tp)[0] is not None and LT_.table(ta)[0] is not None and LT_.table([h2.get('row') or {}])[0] is not None else 'REFUTED',
               'the instrument takes both page tables and the h2 row with no fault'),
        'S3': (('HELD' if not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s' % (len(TF.get('moved') or []), len(TF.get('gone') or []),
                                                                                       len(TF.get('added') or []))),
        'S4': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S5': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b648_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:400]))


def before_answer_ok():
    """no kernel commit of the act precedes the author's answer: the answer's time read from the transcript, every kernel commit since b647's
    face after it."""
    t = None
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
        if 'toolu_01ALSgo9f1Qh5sHVhtLthwUE' in raw and '"tool_result"' in raw:
            m = re.search(r'"timestamp":"([^"]+)"', raw)
            t = m.group(1) if m else None
            break
    if not t:
        return False
    import calendar
    import time as _t
    at = calendar.timegm(_t.strptime(t[:19], '%Y-%m-%dT%H:%M:%S'))
    face = jl('b647_kernels_face.json').get('kernels') or {}
    for k, v in face.items():
        for l in g('D:/' + k, 'log', '--all', '--format=%ct', '%s..' % v[0] if isinstance(v, list) else 'HEAD..HEAD').split(NL):
            if l.strip() and int(l) < at:
                return False
    return True


def _title():
    rows, _one, _a = _n1()
    c = collections.Counter(r.get('classification') for r in rows)
    pa = jl('b648_table_pages_after.json').get('rows') or []
    pc = collections.Counter(r['verdict'] for r in pa)
    kc = jl('b648_kernel_cites.json').get('rows') or []
    return ('## The sorry lines on kernel mains: %d classified, %d proved, %d quarantined, %d restated by the author’s word; the two pages at '
            '%d/%d/%d/%d; the keystone census at v0.8 with %d kernels placed; the h2 row; the re-cut order raised' % (
                len(rows), c['PROVED'], c['QUARANTINED'], c['RESTATED'], pc['MATCHES'], pc['UNDERSTATES'], pc['OVERREACHES'], pc['UNLICENSED'],
                sum(1 for r in kc if r['cluster'])))


def _finding_text():
    S, rl, J = jl('b648_scores.json'), jl('b648_record_lines.json'), jl('b648_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b648_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}]
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    tp, ta = jl('b648_table_pages.json').get('rows') or [], jl('b648_table_pages_after.json').get('rows') or []
    c0, c1 = collections.Counter(r['verdict'] for r in tp), collections.Counter(r['verdict'] for r in ta)
    kc = jl('b648_kernel_cites.json').get('rows') or []
    cmp_ = jl('b648_reader_compare.json')
    ro = jl('b648_recut_order.json').get('rows') or []
    rows, _one, _a = _n1()
    e = ['', _title(), '',
         '*Filed at b648 on the author’s ruling `(R258)` and the author’s answers (%d). Banks: relay `data/b648_sorry_classification.txt`, '
         '`data/b648_sorry_repairs.txt`, `data/b648_table_pages.txt`, `data/b648_table_pages_after.txt`, `data/b648_page_arms_c2.txt`, '
         '`data/b648_kernel_cites.txt`, `data/b648_edition_diff.txt`, `data/b648_reader_compare.txt`, `data/b648_h2_row.txt`, '
         '`data/b648_recut_order.txt`, `data/b648_act_root.txt`.*' % n_ans, '',
         '**The sorry lines** (`(R258)`(2) and the author’s answer): the 37 lines on kernel mains read whole and classified, each with its entry '
         'date; all 37 entered main before the rule’s line at OPEN_TRAILS :11508, so the rule was unenforced on legacy code, not refuted. 33 '
         'QUARANTINED -- SIDE-kernel’s 32 legacy declarations and SIDE-lv-conservation’s PinnedGoal example -- moved to branches '
         'sorry-quarantine-<kernel> and off main, each name and statement in the kernel’s ERRATA.md with the line where the true content is '
         'proved; the four built lines RESTATED as Props on branches, stated and not proved, their builds beneath the hold and so unmerged. From '
         'this act the suite carries G-NO-SORRY-MAIN; it fails while the four stand on their mains. N1 %s.' % sc('N1'), '',
         '**The two pages** (`(R258)`(3)): every sentence of both generated pages a row of the licensed-statement table -- %d rows, MATCHES %d, '
         'UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d. Three template repairs in the generator, the last gating the first two on a node list’s '
         'mark so that b592’s frozen lists emit as before; both pages re-emitted from marked lists -- %d rows, MATCHES %d, UNDERSTATES %d, '
         'OVERREACHES %d, UNLICENSED %d, the three left being the glossary’s and a node list’s, not the template’s. Page arms 2 of 2, the '
         'frozen control 2 of 2. N2 %s.' % (len(tp), c0['MATCHES'], c0['UNDERSTATES'], c0['OVERREACHES'], c0['UNLICENSED'], len(ta), c1['MATCHES'],
                                            c1['UNDERSTATES'], c1['OVERREACHES'], c1['UNLICENSED'], sc('N2')), '',
         '**The census at v0.8** (`(R258)`(4)): the phase, cluster and maturity of 77 rows -- 48 keystones, 7 Day 1 companions, 22 kernels -- '
         'beside v0.7.1, the glossary block regenerated; of the 20 kernels the rules leave unplaced, %d placed by the keystones that name them, '
         'agreeing, %d split and printed as split, %d named by none. A second reader with no project memory: %s of 2 by hand, %s of 2 by the '
         'needles. N3 %s.' % (sum(1 for r in kc if r['cluster']), sum(1 for r in kc if r['how'].startswith('split')),
                              sum(1 for r in kc if r['how'] == 'named by no keystone'), cmp_.get('hand'), cmp_.get('needles'), sc('N3')), '',
         '**The h2 row** (`(R258)`(5)): h1_complete_at_Phi’s docstring names h2 the nonvanishing of a Mellin transform at the operative point; '
         'the glossary’s h2 is h2_sign, Weil positivity on classK; both quoted by line, the surround’s one-node sentence cited, the row '
         'UNLICENSED, one re-cut sentence proposed and not applied. N4 %s.' % sc('N4'), '',
         '**The re-cut order** (`(R258)`(6)): %d documents with their OVERREACHES and UNLICENSED counts and bytes, raised to the author before the '
         'root.' % len(ro), '',
         '**The record lines** (`(R258)`(1)-(2)): b647 at its weight (FINDINGS :%s); the sorry lines on OPEN_TRAILS (:%s), with the correction '
         'beneath them.' % (ls[0].get('line'), ls[1].get('line')), '',
         '**The root.** b648 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, sc(k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the pages now read by the same table as the monograph, the companions and the '
         'kernels; the census places a kernel only where the keystones citing it agree, and shows the split where they do not; the sorry rule now '
         'has an arm. It strengthens the programme’s offering of statements a reader can check: a generated page, a census row and a kernel main '
         'each say no more than their sources license, and say where they do not.', '',
         '**Next.** By the author’s word on the re-cut order (relay `data/b648_author_answers.txt`), %s; b650 the reading act per `(R256)`(6).' % _next_act(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a verdict compares a sentence with a licence and confers none.*', '']
    return _title(), NL.join(e)


RECUT_HEADER = 'Re-cut order'   # ### the header of the (R258)(6) prompt, by which its answer is read from the answers bank


def _next_act():
    """the author's word on the re-cut order, read from data/b648_author_answers.txt (the prompt headed RECUT_HEADER): its answer's label and
    notes, backticks written as apostrophes; the prompt's absence printed as such."""
    t = rd('b648_author_answers.txt')
    m = re.search(r'^### PROMPT \d+ \(%s\):.*?^RESULT \(transcript line \d+\): (.*?)$' % re.escape(RECUT_HEADER), t, re.M | re.S)
    if not m:
        return 'the re-cut order prompt not yet answered'
    r = m.group(1)
    lab = re.search(r'"=("[^"]*"|\(no option selected\))', r)
    notes = re.search(r'notes: (.*?)(?:\. Read the answers carefully|$)', r)
    out = 'the author chose %s' % (lab.group(1).strip('"') if lab else '?')
    if notes:
        out += ', with the note: “%s”' % ' '.join(notes.group(1).split())
    return out.replace('`', '’')


NEXT_ACT = None   # ### read from the answers bank at the record (_next_act), the answer arriving after the seal
FOR_AUTHOR = ('(1) the two template repairs reached b592`s frozen lists and printed UNGRADED, so the third gated both on a node list`s mark; '
              '(2) the three page rows left non-MATCHES are data, not template -- glossary entry 65`s "(b638 is this one)" on both pages and the χ '
              'list`s backmatter sentence on dedekind_rhs`s refuted premise -- held for the re-cut order; (3) the author`s second census answer '
              'carried "Most citations" as its label and Option 1 in its notes: the notes followed; (4) with the census itself not counted, '
              'SIDE-simplicity reads unanimous, so four kernels are placed where the answer counted three; (5) the four RESTATED lines stay on their '
              'mains while their builds fall beneath the hold, and G-NO-SORRY-MAIN fails at the close for them')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b648_scores.json', 'b648_findings.json', 'b648_record_lines.json', 'b648_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b648_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}]
    ta = jl('b648_table_pages_after.json').get('rows') or []
    c1 = collections.Counter(r['verdict'] for r in ta)
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R258) ratified.** (1) b647 at its weight. (2) The 37 sorry lines classified and repaired by the author’s word. (3) The two pages '
             'through the table and re-emitted. (4) The census at v0.8 with a second reader. (5) The h2 row. (6) The re-cut order to the author. (7) '
             'The description at v4, the draft held. (8) The navigator’s memory repaired outside any act.', '',
             '**Entered:** FINDINGS.md:%s (b647’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the sorry lines and their correction); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line')), '',
             '**The pages:** %d rows after re-emission, MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d (relay '
             'data/b648_table_pages_after.txt).' % (len(ta), c1['MATCHES'], c1['UNDERSTATES'], c1['OVERREACHES'], c1['UNLICENSED']), '',
             '**The draft:** %s at v4, held; the deposit route untouched this act; nothing published.' % K.DRAFT, '',
             '**Act root:** b648 `%s` (previous `%s`, b647’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b648_author_answers.txt), none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b648_defects.txt): %s.' % '; '.join(DEFECT_SHORT), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** by the author’s word on the re-cut order (relay data/b648_author_answers.txt), %s; b650 the reading act per `(R256)`(6).' % _next_act(), '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b648_scores.json')
    L = ['=' * 104, 'b648 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rd('b648_defects.txt').rstrip(NL).split(NL)
    put_txt('b648_desk_notes.txt', L)


def components(*a):
    """data/b648_components.txt -- run after `findings` and `trail`; refuses when either bank is absent."""
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b648_scores.json', 'b648_findings.json', 'b648_trail.json', 'b648_record_lines.json', 'b648_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}]
    L = ['b648 -- THE COMPONENTS, BANKED UNDER (R258).', '',
         '### COMPONENT 0 : step zero (data/b648_ferry.txt, data/b648_stepzero.txt, data/b648_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b647`s weight FINDINGS :%s ; the sorry lines OPEN_TRAILS :%s' % (ls[0].get('line'), ls[1].get('line')),
         '### COMPONENT 2 : the sorry classification and repairs (data/b648_sorry_classification.txt, data/b648_sorry_repairs.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 3 : the pages (data/b648_table_pages.txt, data/b648_table_pages_after.txt, data/b648_page_arms_c2.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 4 : the census at v0.8 and the second reader (data/b648_edition_diff.txt, data/b648_reader_compare.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 5 : the h2 row (data/b648_h2_row.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 6 : the seal (data/b648_seal_hashes.json) ; S5 %s' % S['S5'][0],
         '### COMPONENT 7 : the re-cut order (data/b648_recut_order.txt) ; the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b648_components.txt', L)
    print(NL.join(L[2:]))


def findings(*a):
    import b641_record as R41
    Q = R2._Q()
    t, e = _finding_text()
    e = R41._poss(e)
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE ENTRY -- NOTHING WRITTEN')
    cells = R3.predict_cells(e, 'FINDINGS.md')
    nd, _n = R3._nd(e)
    p = os.path.join(SP if DRY else D, 'b648_scanfile_entry.md')
    _write(p, e.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    unread = [x for x in ('### NOT', 'None', '?;', ' ? ', '`?`') if x in e]
    outside = [n for n in R41.OAI_NEEDLES if n in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s ; outside names %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                         unread or 'NONE', outside or 'NONE'))
    if DRY:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread or outside:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b648_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    import b641_record as R41
    Q = R2._Q()
    e = R41._poss(_trail_text())
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE RECORD -- NOTHING WRITTEN')
    cells = R3.predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = R3._nd(e)
    p = os.path.join(SP if DRY else D, 'b648_scanfile_trail.md')
    _write(p, e.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    unread = [x for x in ('### NOT', 'None', '`?`') if x in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', unread or 'NONE'))
    if DRY:
        print(e[:9000])
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b648_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b648_trail.json')['line'])


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b648_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
