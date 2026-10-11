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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b648_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
