# -*- coding: utf-8 -*-
"""b644_record.py -- THE ACT'S RECORD TOOL, UNDER (R254). ### ONE SUBCOMMAND PER BANK.

### ### b644: LANE THREE, ACT SEVENTY-ONE -- THE CHAIN READ AT COMMIT AND SHARED FILES ADDITIVE; THE WATCHDOG STOP; THE HINGES RECOUNTED
### UNDER THE REFINED DEFINITION AND THE CENSUS AT v0.7.1; SIDE-GLOBAL-SECTION'S INTERFACES BUILT; THE TWO ROSTERS; THE SEVEN PATCH EDITIONS;
### THE DEPOSIT DESCRIPTION AS SYNTHESIS, SECOND-READ, THE DRAFT'S FILE SET REPLACED AND HELD; THE LATTICE BANKED. Subcommands write only
### `data/b644_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers are b602's, b633's,
### b641's and b643's record tools', imported; ledger appends through b566's guarded `append_to`. Lean runs are the seat's, detached under
### tools/build_watch.py (W-ORD-WATCHDOG-STOP, (R254)(3)); this tool generates their files and reads their logs. Every bank is written LF.
"""
import collections
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b641_record as R41  # noqa: E402
import b644_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'f004d01d-ad93-416c-a916-fe6e52403753'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b644_registration_2026-10-09.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of, _nd, predict_cells, _land = R3.lines_of, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
KERNS_READ = R41.KERNS_READ
_poss = R41._poss
OUTSIDE_NEEDLES = R41.OAI_NEEDLES     # ### no line naming an outside collection; b641's needles carried
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
    try:
        return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b644_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b644 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b644_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b644_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R254) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b644 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in since:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not since:
        L.append('### NONE: no prompt has been put to the author in this act.')
    put_txt('b644_author_answers.txt', L)
    print('  prompts banked: %d' % n)


def kernels(*a):
    put_json('b644_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


# ================================================================================ READING (1): THE READS THE FERRY NAMES, BY PATH AND LINE
def READS():
    return [
        ('relay data/b643_closing.txt: its head line and its defects', RELAY, PRE_RELAY, 'data/b643_closing.txt', ('GREP', r'^b643 closed|^    \([a-m]\) '), 260),
        ('relay data/b643_defects.txt: defect (m)', RELAY, PRE_RELAY, 'data/b643_defects.txt', ('GREP', r'^    \(m\) '), 400),
        ('relay data/b643_consumers.txt: the hinge lines and the count', RELAY, PRE_RELAY, 'data/b643_consumers.txt', ('GREP', r'### HINGE|^### ### \*\*HEADS'), 200),
        ('relay data/b643_reader_compare.txt :22', RELAY, PRE_RELAY, 'data/b643_reader_compare.txt', [22], 200),
        ('relay data/b643_pi01_attempts.txt :21', RELAY, PRE_RELAY, 'data/b643_pi01_attempts.txt', [21], 260),
        ('relay tools/act_root.py: verify and the root bank`s fields', RELAY, PRE_RELAY, 'tools/act_root.py',
         ('GREP', r'^def verify|^def compute|j = dict\(act=act|^def gather|sha256_file\(p\) != parts\[1\]|getmtime'), 220),
        ('relay data/act_roots.txt', RELAY, PRE_RELAY, 'data/act_roots.txt', ('GREP', r'.'), 120),
        ('relay data/glossary.txt: CHAIN and HINGE', RELAY, PRE_RELAY, 'data/glossary.txt', ('GREP', r'^(CHAIN|HINGE)\t'), 260),
        ('the watchdog`s sampling code (b643`s scratchpad build1.py)', RELAY, None, K.SP_B643 + '/build1.py', ('GREP', r'^HOLD|def sampler|SAMPLE|REFUSED|EXIT'), 200),
        ('SIDE-global-section`s Interfaces modules at HEAD', K.GS, 'HEAD', 'README.md', ('GREP', r'Interfaces'), 260),
        ('relay tools/b239_reprint.py: the Interfaces` last build route and pins', RELAY, PRE_RELAY, 'tools/b239_reprint.py', ('GREP', r'PIN_|lake.*env.*lean|-> D:'), 200),
        ('relay tools/mirror_roster.json: its day1 rows and its census rows', RELAY, PRE_RELAY, 'tools/mirror_roster.json', ('GREP', r'day1|KEYSTONE_CENSUS|lastChanged'), 200),
        ('the seven companions` label lines', PP, PRE_PP, 'day1/Exhaustive_Enumeration.md', [3], 200),
        ('', PP, PRE_PP, 'day1/Which_Structure_Confines.md', [3], 200), ('', PP, PRE_PP, 'day1/Spectral_Inertness.md', [3], 200),
        ('', PP, PRE_PP, 'day1/Seven_Mechanism_Classes.md', [5], 200), ('', PP, PRE_PP, 'day1/Third_Identity_Element.md', [5], 200),
        ('', PP, PRE_PP, 'day1/Silence_of_Foundations.md', [3], 200), ('', PP, PRE_PP, 'day1/ONE_PAGE_PROOF.md', [3, 42, 64], 200),
        ('relay data/b640_deposit_description.txt: its paragraphs` heads', RELAY, PRE_RELAY, 'data/b640_deposit_description.txt', ('GREP', r'.'), 200),
        ('relay tools/b640_record.py: the description composer', RELAY, PRE_RELAY, 'tools/b640_record.py', ('GREP', r'^def compose|^def describe|^def _desc_scan|^Q1_'), 200),
        ('ERRATA.md: its reporting form', PP, PRE_PP, 'ERRATA.md', list(range(12, 21)), 200),
        ('OPEN_TRAILS: :13397, :13489-:13497, :13529, :13531, :13563, :13591', PP, PRE_PP, 'OPEN_TRAILS.md',
         [K.OT_PATCH, 13489, 13491, 13493, 13495, 13497, K.OT_LATTICE, K.OT_PI1, K.OT_WATCHDOG, K.B643_CORRECTION], 500),
        ('FINDINGS: b643`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B643_ENTRY], 300),
        ('relay data/b643_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b643_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b644 -- READING (1): THE READS THE FERRY NAMES, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        if rev is None:
            t = io.open(path, encoding='utf-8', errors='replace').read() if os.path.exists(path) else None
            at = 'the file'
        else:
            at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
            t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)] if isinstance(sel, tuple) else \
            [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label or 'the label line', path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### SIDE-global-section`s Interfaces modules at HEAD: %s' % ', '.join(
        x for x in g(K.GS, 'ls-tree', '--name-only', 'HEAD', 'Interfaces/').split(NL) if x.endswith('.lean')),
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()),
          '### the reads banked late: read at step zero (this session`s transcript) and printed here after Component 7 -- the act`s defect']
    put_txt('b644_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()), len(L)))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R254)(1)-(4)
W_HEAD = '*Appended 2026-10-09 by b644 to b643’s entry (:%d), under `(R254)`(1) -- b643 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
CA_HEAD = ('*Appended 2026-10-09 by b644 to W-ORD-ACT-ROOT (:%d), under `(R254)`(2) and the author’s answer at b644 -- W-ORD-CHAIN-AT-COMMIT, '
           'ACTED:*')
AD_HEAD = ('*Appended 2026-10-09 by b644 beneath W-ORD-CHAIN-AT-COMMIT (:%d), under `(R254)`(2) -- SHARED DATA FILES ADDITIVE, STANDING '
           'FROM (R254):*')
WS_HEAD = ('*Appended 2026-10-09 by b644 to W-ORD-WATCHDOG-STOP (:%d), under `(R254)`(3) and the author’s answer at b644 -- ACTED:*')


def _b643_figures():
    """b643's figures, each read from its banks (data/b643_*)."""
    head = rd('b643_closing.txt').split(NL)[0]
    m = re.match(r'^b643 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts answered; (\d+) defects', head)
    closing = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b643 closing', PRE_RELAY).strip()[:8]
    Z, C = jl('b643_page_zeta.json'), jl('b643_page_chi.json')
    PT, CO = jl('b643_premise_table.json'), jl('b643_consumers.json')
    st = PT.get('status') or {}
    hinges = [r for r in CO.get('rows') or [] if r.get('hinge')]
    cross = [(r['head'], r['hinge_kernels']) for r in hinges if r.get('hinge_kernels')]
    gs_unread = sorted(r['head'] for r in CO.get('rows') or [] if 'SIDE-global-section' in (r.get('unread') or []))
    RC = jl('b643_reader_compare.json')
    pi = re.search(r'SOURCES NAMED (\d+) ; REACHED AND READ (\d+)', rd('b643_pi01_attempts.txt'))
    lows = [c.get('low') for c in jl('b643_deps_runs.json').get('calls') or [] if isinstance(c.get('low'), int)]
    nprompt = len(re.findall(r'^### PROMPT ', rd('b643_author_answers.txt'), re.M))
    ndef = len(jl('b643_defects.json').get('defects') or [])
    return dict(m=m, closing=closing, Z=Z, C=C, st=st, nh=len(hinges), cross=cross, gs_unread=gs_unread, RC=RC, pi=pi,
                low=min(lows) if lows else None, nprompt=nprompt, ndef=ndef, heads=len(PT.get('rows') or []))


def _weight():
    f = _b643_figures()
    m, Z, C = f['m'], f['Z'], f['C']
    six = ', '.join('%s %s' % (k, f['st'].get(k)) for k in ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'DOMAIN', 'REFUTED-BY-COMPUTATION'))
    return ('\n%s relay %s (closing %s), PLACE-papers %s; the suite %s of %s pre-push and post-push; the root %s…; %d prompts answered; '
            '%d defects, (a) to (m). The pages at v0.26, emitted twice -- at Component 3 and again before the seal, once the generator listed '
            'the new census as a keystone naming a node: the zeta page`s Correspondence %s rows (%s before), the chi page`s %s (%s before). The '
            'census at v0.7 generated from banks: %d heads, six statuses (%s), non-vacuity with DEGENERATE its own value, consumers by kernel, '
            '%d hinges under the definition then ruled, %s the one hinge across kernels (%s). The second reader %s of 3 by the repaired needle '
            'and %s of 3 by hand. The Pi-0-1 sources named %s, reached and read %s; W-ORD-H2-PI1 open (:%d). Defect (m): data/glossary.txt, '
            'an item of b638`s and b639`s roots, extended as ordered, so the chain read at the working tree recomputed both DISAGREE (the '
            'correction :%d); no root recomputed. The watchdog`s trigger met, the dependency print`s lowest sample %s MB, none stopped. '
            'SIDE-global-section`s Interfaces modules had no build product, so the consumers there of %s were not read. The draft %s held; '
            'nothing deposited.\n' % (
                W_HEAD % K.B643_ENTRY, m.group(1) if m else '?', f['closing'] or '?', m.group(2) if m else '?', m.group(3) if m else '?',
                m.group(4) if m else '?', (m.group(5) if m else '?')[:16], f['nprompt'], f['ndef'], Z.get('corr_after'), Z.get('corr_before'),
                C.get('corr_after'), C.get('corr_before'), f['heads'], six, f['nh'], ', '.join(h for h, _k in f['cross']) or '?',
                '; '.join(', '.join(k) for _h, k in f['cross']) or '?', f['RC'].get('needles'), f['RC'].get('hand'),
                f['pi'].group(1) if f['pi'] else '?', f['pi'].group(2) if f['pi'] else '?', K.OT_PI1, K.B643_CORRECTION, f['low'],
                ', '.join(f['gs_unread']) or '?', K.DRAFT))


def _chain_figures():
    t = rd('b644_actroot_commit.txt')
    commit = re.search(r'### AT THE RECORDED COMMIT.*?### ACTS (\d+) ; BANKS AGREE (\d+) ; DISAGREE (\d+)', t, re.S)
    wt = re.search(r'### THE WORKING TREE.*?### ACTS (\d+) ; BANKS AGREE (\d+) ; DISAGREE (\d+)', t, re.S)
    crlf = re.search(r'### CRLF READS (\d+) over b624-b643', t)
    b638 = re.search(r'^  b638 (\S+)\s+\[at', t, re.M)
    b639 = re.search(r'^  b639 (\S+)\s+\[at', t, re.M)
    wtd = list(dict.fromkeys(re.findall(r'^  (b\d+) DISAGREE \[the working tree\]', t, re.M)))   # ### the bank reprints b638 and b639 at its end
    test = re.search(r'(\d+) of (\d+) cases as wanted', t)
    return commit, wt, crlf, b638, b639, wtd, test


def _chain_text():
    commit, wt, crlf, b638, b639, wtd, test = _chain_figures()
    return ('\n%s tools/act_root.py`s verify reads every bank a root names at the commit that root recorded, by git and not from the working '
            'tree (relay %s, with its planted test, alone): the relay commit the root banks from b644 (`commit`, the relay and PLACE-papers '
            'heads at the computation), and for a root banked before b644 the relay head it read; a bank the act wrote after that commit is read '
            'at the first commit on relay main`s first-parent line that carries it. The planted test %s of %s: a later edit to a named file AGREE '
            'at the recorded commit and DISAGREE at the working tree. Every root of the chain read so: %s of %s AGREE at commit, b638 %s and '
            'b639 %s; at the working tree %s DISAGREE (%s). The author`s answer at b644: relay`s `* text=auto eol=lf` writes every commit LF, '
            'so a bank written with CR LF was hashed in a form no commit holds; its read agrees on the blob or on the blob`s CRLF form, counted '
            'apart per act (%s such reads over b624 to b643), no root recomputed -- a property of how the banks were written, not of what they '
            'say; and from b644 every bank is written LF before it is hashed: compute refuses a CR LF bank, and verify reads a CRLF read on '
            'any act after b643 as DISAGREE (relay data/b644_actroot_commit.txt).\n' % (
                CA_HEAD % K.OT_ACT_ROOT, K.CHAIN_COMMIT, test.group(1) if test else '?', test.group(2) if test else '?',
                commit.group(2) if commit else '?', commit.group(1) if commit else '?', b638.group(1) if b638 else '?',
                b639.group(1) if b639 else '?', wt.group(3) if wt else '?', ', '.join(wtd) or 'none', crlf.group(1) if crlf else '?'))


def _additive_text(ca_line):
    return ('\n%s a data file named by more than one act`s root, and data/glossary.txt and data/act_roots.txt, is additive: an entry is '
            'added, or a dated line beneath it, and no line is edited or removed. relay tools/additive_shared.py diffs each such file against '
            'its previous commit, and the working file against HEAD, reading a removed or changed line as a failure (relay %s, with its test); '
            'the suite carries it as an arm. A definition superseded in such a file keeps its line, a dated line beneath it, and the new entry '
            'appended.\n' % (AD_HEAD % ca_line, K.ADDITIVE_COMMIT))


def _watch_text():
    rows = jl('b644_build_watch.json').get('rows') or []
    return ('\n%s relay tools/build_watch.py, the watchdog carried from the scratchpad`s build1.py into the tree (relay %s and %s, with its '
            'test): a detached run whose sample reads free memory beneath the 2,560 MB hold is stopped by PID, its process tree`s command '
            'lines printed; the host freed by the standing procedure (every lean, lake or python process whose parent is gone stopped by PID, '
            'then a wait for the hold); the run retried once; a retry beneath the hold again, or one that cannot start above it, recorded '
            'RUN-BENEATH-HOLD with its low and the module`s name, in the log and in relay data/b644_build_watch.json, and the act proceeds with '
            'the module unbuilt and the omission named in its closing. The planted run -- the hold set above the host`s free memory -- stopped '
            'twice and recorded. The author`s answer at b644: the hold stays at 2,560 MB and the seat does not lower it; if the host cannot '
            'reach the hold for any run, every build is recorded RUN-BENEATH-HOLD, nothing is built, and the hold is raised as a prompt with the '
            'host`s free memory printed. First recorded at b644`s step zero: %s.\n' % (
                WS_HEAD % K.OT_WATCHDOG, K.WATCH_COMMITS[0], K.WATCH_COMMITS[1],
                '; '.join('%s, lows %s MB' % (r['module'], r['lows']) for r in rows) or 'none'))


def record_lines(*a):
    """### Component 1, (R254)(1)-(3): FINDINGS, b643 at its weight (to :7995); OPEN_TRAILS, W-ORD-CHAIN-AT-COMMIT acted (to :12210), the
    additive clause beneath it, W-ORD-WATCHDOG-STOP acted (to :13563)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The two readers repaired and rerun')
    if entry != K.B643_ENTRY:
        sys.exit('### b643`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    ot_n = len(lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), '')))
    ca_line = ot_n + 2
    items = [('FINDINGS.md', W_HEAD % K.B643_ENTRY, _poss(_weight())), ('OPEN_TRAILS.md', CA_HEAD % K.OT_ACT_ROOT, _poss(_chain_text())),
             ('OPEN_TRAILS.md', AD_HEAD % ca_line, _poss(_additive_text(ca_line))), ('OPEN_TRAILS.md', WS_HEAD % K.OT_WATCHDOG, _poss(_watch_text()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None') if x in allt]
    outside = [n for n in OUTSIDE_NEEDLES if n in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks: %s ; unread figures: %s ; outside names: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread or outside:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS, AN UNREAD FIGURE OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    _land(Q, items, 'b644_record_lines.json', K.B643_ENTRY)


# ================================================================================ COMPONENT 2: THE INTERFACES BUILT, (R254)(5)
# ### Each Interfaces module of SIDE-global-section at HEAD compiled to a build product, one module per call, by the route its README states
# ### (:40-:41, "elaborate against a mathlib4 checkout at the declared pin"), at the checkout its banked profile was built with (b239's pins):
# ### the pin's own lean, LEAN_PATH the checkout's library and its packages' and the output directory, --root the Interfaces directory so the
# ### module's name is its file's. Every call detached under tools/build_watch.py, which stops a run sampling beneath the hold, retries it
# ### once and records RUN-BENEATH-HOLD; the free memory read before each launch is printed. The dependency print of each built module runs
# ### the same way (b643's prelude, the module imported alone).
def _toolchain(pin):
    return io.open(os.path.join(pin, 'lean-toolchain'), encoding='utf-8').read().strip().replace('leanprover/lean4:', '')


def _iface_env(pin):
    tc = _toolchain(pin)
    out = '%s/%s' % (K.IFACE_OUT, tc)
    libs = [pin + '/.lake/build/lib/lean'] + sorted('%s/.lake/packages/%s/.lake/build/lib/lean' % (pin, p)
                                                     for p in os.listdir(pin + '/.lake/packages')
                                                     if os.path.isdir('%s/.lake/packages/%s/.lake/build/lib/lean' % (pin, p)))
    lean = 'D:/elan/toolchains/leanprover--lean4---%s/bin/lean.exe' % tc
    return tc, out, libs + [out], lean


def _iface_cmd(mod, pin, kind='build'):
    tc, out, path, lean = _iface_env(pin)
    src = '%s/Interfaces/%s.lean' % (K.GS, mod)
    if kind == 'build':
        args = ['--root=%s/Interfaces' % K.GS, '-o', '%s/%s.olean' % (out, mod), '-i', '%s/%s.ilean' % (out, mod), src]
    else:
        args = [_deps_src(mod)]
    return lean, args, ';'.join(p.replace('/', '\\') for p in path), out


DEPS_DIR = os.path.join(SP, 'b644_deps')


def _deps_src(mod):
    import b643_record as R43
    p = os.path.join(DEPS_DIR, 'deps_%s.lean' % mod)
    R43._deps_file(mod, [mod], p)
    return p.replace('\\', '/')


def iface_plan(*a):
    """prints each Interfaces module's pin, toolchain, output directory and the two commands; writes nothing."""
    for mod, pin in K.IFACES:
        lean, args, lp, out = _iface_cmd(mod, pin)
        print('  %-24s pin %s (%s %s) ; out %s' % (mod, pin, _toolchain(pin), g(pin, 'rev-parse', '--short', 'HEAD').strip(), out))
        print('      build: %s %s' % (lean, ' '.join(args)))
    print('  LEAN_PATH (D:/mathlib4): %s' % _iface_cmd('GlobalSection', K.MATHLIB_MAIN)[2])


def iface_launch(mod, kind='build'):
    """writes the PowerShell launcher for ONE call (scratchpad) and prints its path: Start-Process of build_watch.py, hidden, LEAN_PATH set."""
    pin = dict(K.IFACES)[mod]
    lean, args, lp, out = _iface_cmd(mod, pin, kind)
    os.makedirs(out, exist_ok=True)
    tag = '%s_%s' % (kind, mod)
    log = '%s/w_%s.log' % (SP, tag)
    wargs = ['D:\\relay\\tools\\build_watch.py', '--module', 'SIDE-global-section/Interfaces/%s.%s' % (mod, kind), '--bank',
             'D:\\relay\\data\\b644_build_watch.json', pin.replace('/', '\\'), log.replace('/', '\\'), lean.replace('/', '\\')] + \
        [x.replace('/', '\\') if not x.startswith('--root') else x for x in args]
    q = lambda s: "'" + s.replace("'", "''") + "'"   # noqa: E731
    ps = ['$os = Get-CimInstance Win32_OperatingSystem',
          '"free before: " + [math]::Round($os.FreePhysicalMemory/1024) + " MB"',
          '$env:LEAN_PATH = %s' % q(lp),
          '$a = @(%s)' % ', '.join(q('"%s"' % x if ' ' in x else x) for x in wargs),
          '$p = Start-Process -FilePath python -WorkingDirectory %s -ArgumentList $a -WindowStyle Hidden -PassThru '
          '-RedirectStandardOutput %s -RedirectStandardError %s' % (q(SP.replace('/', '\\')), q('%s\\w_%s.out' % (SP.replace('/', '\\'), tag)),
                                                                     q('%s\\w_%s.err' % (SP.replace('/', '\\'), tag))),
          '"watchdog pid " + $p.Id + " log %s"' % log]
    p = os.path.join(SP, 'launch_%s.ps1' % tag)
    io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(ps) + '\n')
    print(p)


def _log_outcome(log):
    t = io.open(log, encoding='utf-8', errors='replace').read() if os.path.exists(log) else ''
    ls = t.split(NL)
    ex = [l for l in ls if l.startswith('### EXIT')]
    lows = [int(x) for x in re.findall(r' low (\d+) MB', NL.join(ex))]
    samples = [int(x) for x in re.findall(r'^### SAMPLE \S+ free (\d+) MB', t, re.M)]
    rbh = [l for l in ls if l.startswith('### RUN-BENEATH-HOLD')]
    errs = [l for l in ls if re.search(r': error', l)][:5]
    if not t:
        v = 'NOT RUN'
    elif rbh:
        v = 'RUN-BENEATH-HOLD'
    elif ex and re.match(r'^### EXIT 0 ', ex[-1]):
        v = 'BUILT' if 'build' in log else 'PRINTED'
    elif ex:
        v = 'FAILED (exit %s)' % ex[-1].split()[2]
    else:
        v = 'RUNNING'
    return dict(verdict=v, exits=ex, lows=lows, samples_min=min(samples) if samples else None, starts=t.count('### START attempt'),
                refused=t.count('### REFUSED'), stops=t.count('### STOPPED-BENEATH-HOLD'), errors=errs)


def iface_bank(*a):
    """data/b644_iface_builds.txt and .json: each Interfaces module's build and dependency-print outcome from its watchdog log."""
    L = ['b644 -- COMPONENT 2, (R254)(5): SIDE-global-section`s Interfaces MODULES, ONE BUILD PER CALL UNDER tools/build_watch.py (%s)' % utc(), '',
         '### the route: SIDE-global-section README :40-:41, each at the mathlib4 checkout its banked profile was built with (relay tools/b239_reprint.py '
         ':16-:17); the build products under %s/<toolchain>/ (build/ is the kernel`s .gitignore`d tree); no source touched.' % K.IFACE_OUT, '']
    J = []
    for mod, pin in K.IFACES:
        row = dict(module=mod, pin=pin, toolchain=_toolchain(pin))
        for kind in ('build', 'deps'):
            row[kind] = _log_outcome('%s/w_%s_%s.log' % (SP, kind, mod))
        J.append(row)
        b, d = row['build'], row['deps']
        L.append('  %-24s %-8s %-20s build %-16s (starts %d, refused %d, stopped %d, lows %s, lowest sample %s) ; print %s%s' % (
            mod, row['toolchain'], pin, b['verdict'], b['starts'], b['refused'], b['stops'], b['lows'] or '-', b['samples_min'], d['verdict'],
            (' ; errors: ' + ' | '.join(b['errors'])) if b['errors'] else ''))
    nb = sum(1 for r in J if r['build']['verdict'] == 'BUILT')
    L += ['', '### ### **INTERFACES MODULES %d ; BUILT %d ; RUN-BENEATH-HOLD %d ; FAILED %d ; NOT RUN %d ; PRINTED %d.**' % (
        len(J), nb, sum(1 for r in J if r['build']['verdict'] == 'RUN-BENEATH-HOLD'), sum(1 for r in J if r['build']['verdict'].startswith('FAILED')),
        sum(1 for r in J if r['build']['verdict'] == 'NOT RUN'), sum(1 for r in J if r['deps']['verdict'] == 'PRINTED'))]
    put_txt('b644_iface_builds.txt', L)
    put_json('b644_iface_builds.json', dict(at=utc(), rows=J))
    print(NL.join(L[4:]))


# ================================================================================ COMPONENT 2: THE HINGES RECOUNTED, (R254)(4)
# ### The refined definition (data/glossary.txt, the appended HINGE entry): a premise's own evidence is removed from the use-graph before the
# ### components are taken -- every declaration whose statement is the premise's satisfiability (the Salt witnesses), its negation (the not_*
# ### refutations) or a projection of it -- and a head of status DOMAIN is printed with its chains and is not a hinge. The evidence rule, read
# ### per declaration, its reason printed:
# ###   E1 SALT        the declaration sits in a SaltCheck module (the module's last component begins `SaltCheck`): the Salt witnesses;
# ###   E2 NEGATION    a theorem whose conclusion is the head negated (`¬ H ...`, `¬ ∃ ..., H ...`, or `H ... → False`);
# ###   E3 SATISFIABLE a theorem whose conclusion is the head itself, under any `∃` binders, with no hypothesis naming the head;
# ###   the projections and constructors of the head are the head's own names and leave the graph with it, as at b643 (_head_names).
# ### The conclusion is read by the table's own textual reader (tools/terminal_table.py statement, the file at the kernel's HEAD), cut at the last
# ### colon at bracket depth 0; a statement the reader cannot resolve is printed UNRESOLVED and kept in the graph.
FIVE = ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'REFUTED-BY-COMPUTATION')
_STMT = {}


def _statement(k, n):
    import terminal_table as TT
    if (k, n) not in _STMT:
        try:
            st = TT.statement('D:/' + k, 'HEAD', n)
        except Exception:
            st = None
        _STMT[(k, n)] = ' '.join(st['text'].split()) if st else None
    return _STMT[(k, n)]


def _split_conclusion(text):
    """(binders, conclusion): the statement cut at its last colon at bracket depth 0 (the declaration line up to `:=`)."""
    depth, cut = 0, None
    for i, c in enumerate(text):
        if c in '([{⟨':
            depth += 1
        elif c in ')]}⟩':
            depth -= 1
        elif c == ':' and depth == 0 and text[i + 1:i + 2] != '=' and text[i - 1:i] != ':':
            cut = i
    return (text[:cut], text[cut + 1:].strip()) if cut is not None else (text, '')


def _evidence(k, n, h, K_):
    """the evidence reason for declaration n against head h (short name), or None."""
    mod = (K_.get(n) or {}).get('module') or ''
    if mod.split('.')[-1].startswith('SaltCheck'):
        return 'E1 SALT (module %s)' % mod
    if (K_.get(n) or {}).get('kind') != 'theorem':
        return None
    t = _statement(k, n)
    if t is None:
        return None
    binders, concl = _split_conclusion(t)
    hp = r'(?:@?[\w.]*\.)?%s\b' % re.escape(h)
    body = re.sub(r'^(?:∃\s*[^,]+,\s*)+', '', concl)
    if re.match(r'^¬\s*\(?\s*(?:∃\s*[^,]+,\s*)*' + hp, concl) or (re.match('^' + hp, body) and re.search(r'→\s*False\s*$', concl)):
        return 'E2 NEGATION (%s)' % concl[:80]
    if re.match('^' + hp, body) and not re.search(r'→|↔|∧|∨', body) and not re.search(hp, binders):
        hyp = re.search(r'\((?!\s*[\w\s]+\s*:\s*(?:Type|Sort|ℕ|ℤ|ℝ|ℂ|Nat|Int|Real|Complex)\b)[^()]*:[^()]*\)|\[[^\]]+\]', binders)
        return ('E3b SATISFIABLE UNDER HYPOTHESES' if hyp else 'E3a SATISFIABLE') + ' (%s)' % concl[:80]
    return None


def _gs_iface_deps(DEP):
    """the Interfaces modules' dependency prints (their watchdog logs), folded into SIDE-global-section's declarations, b643's reader."""
    import b643_record as R43
    got = []
    for mod, _pin in K.IFACES:
        log = '%s/w_deps_%s.log' % (SP, mod)
        o = _log_outcome(log)
        if o['verdict'] != 'PRINTED':
            continue
        K_ = DEP.setdefault('SIDE-global-section', {})
        for l in io.open(log, encoding='utf-8', errors='replace'):
            if not l.startswith('DEP\t'):
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) < 8:
                continue
            nm, kind, m, t, v = p[1], p[2], p[3], p[5], p[7]
            ow = R43._owner(nm)
            e = K_.setdefault(ow, dict(kind=None, module=m, T=set(), V=set()))
            if ow == nm:
                e['kind'], e['module'] = kind, m
                e['T'] |= set(R43._owner(x) for x in t.split())
                e['V'] |= set(R43._owner(x) for x in v.split())
            else:
                e['V'] |= set(R43._owner(x) for x in t.split() + v.split())
        got.append(mod)
    return got


def _recount_head(v, DEP, refined=True):
    import b643_record as R43
    h, decl = v['head'], v.get('decl')
    per = []
    for k in v['kernels']:
        K_ = DEP.get(k)
        if K_ is None:
            per.append(dict(kernel=k, read=False, why='no call of that kernel'))
            continue
        rows_k = [x.split(' ', 1)[1] for x in v.get('rule_rows') or [] if x.split(' ', 1)[0] == k]
        seen = [x for x in rows_k if x in K_ or any(nn.endswith('.' + x) for nn in K_)]
        if rows_k and not seen:
            per.append(dict(kernel=k, read=False, why='the declarations its rows sit in (%s) are in modules with no build product read' %
                            ', '.join(rows_k[:3])))
            continue
        H = R43._head_names(k, h, decl, K_)
        direct = [nn for nn, e in K_.items() if nn not in H and ((e['T'] | e['V']) & H)]
        ev = {}
        if refined:
            for nn in direct:     # ### evidence is the premise's own: a declaration that uses the head directly
                r = _evidence(k, nn, h, K_)
                if r:
                    ev[nn] = r
        X = set(H) | set(ev)
        direct = [nn for nn in direct if nn not in X]
        thm = sorted(nn for nn in direct if K_[nn]['kind'] == 'theorem')
        R_ = set(direct)
        grow = True
        while grow:
            new = set(nn for nn, e in K_.items() if nn not in R_ and nn not in X and ((e['T'] | e['V']) & R_))
            grow = bool(new)
            R_ |= new
        comps = R43._components(R_, K_)
        cons_comps = [c for c in comps if set(thm) & c[0]]
        per.append(dict(kernel=k, read=True, consumers=len(thm), reach=len(R_), chains=[t[:3] for _c, t in cons_comps], n_chains=len(cons_comps),
                        evidence=sorted(ev.items())))
    kk = [p['kernel'] for p in per if p.get('read') and p['consumers'] > 0]
    hc = [p['kernel'] for p in per if p.get('read') and p['n_chains'] > 1]
    return dict(head=h, per=per, hinge_kernels=kk if len(kk) > 1 else [], hinge_chains=hc, shape=bool(len(kk) > 1 or hc),
                unread=[p['kernel'] for p in per if not p.get('read')])


def hinges(*a):
    """data/b644_hinges.txt and .json: the 50 heads recounted under the refined definition beside b643's 28 -- each head that leaves, its reason;
    the DOMAIN heads printed with their chains and set aside; every evidence declaration removed, its rule; the Interfaces' prints folded in."""
    import b643_record as R43
    P = jl('b642_premise_status.json')
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    DEP = R43._deps_load()
    ifaces = _gs_iface_deps(DEP)
    old = dict((r['head'], r) for r in jl('b643_consumers.json').get('rows') or [])
    rows = []
    for v in P.get('heads') or []:
        st = PT[v['head']]['status']
        r = _recount_head(v, DEP, refined=st != 'DOMAIN')   # ### a DOMAIN head printed with b643's chains: the evidence rule reads programme premises
        r['status'] = st
        r['hinge'] = r['shape'] and st in FIVE
        r['old_hinge'] = bool((old.get(v['head']) or {}).get('hinge'))
        rows.append(r)
    leave, join = [r for r in rows if r['old_hinge'] and not r['hinge']], [r for r in rows if r['hinge'] and not r['old_hinge']]

    def why(r):
        if r['status'] == 'DOMAIN':
            return 'DOMAIN (a Mathlib predicate restricting a quantified variable): printed with its chains, not a hinge of the programme' + (
                '' if r['shape'] else '; and its chains after the evidence leaves are one')
        ev = sum(len(p.get('evidence') or []) for p in r['per'] if p.get('read'))
        return 'its own evidence removed (%d declarations): consumers in %s ; chains %s' % (
            ev, ', '.join(p['kernel'] for p in r['per'] if p.get('read') and p['consumers']) or 'no kernel',
            ', '.join('%s %d' % (p['kernel'], p['n_chains']) for p in r['per'] if p.get('read')))
    L = ['b644 -- COMPONENT 2, (R254)(4): THE HINGES RECOUNTED UNDER THE REFINED DEFINITION, BESIDE b643`S (%s)' % utc(), '',
         '### the definition: data/glossary.txt, the HINGE entry appended at b644 ((R254)(4)); the evidence rule E1 SALT / E2 NEGATION / E3 SATISFIABLE '
         '(tools/b644_record.py, its comment block); the print: b643`s 135 calls (data/b643_deps_runs.json) and the Interfaces` prints read: %s.' % (
             ', '.join(ifaces) or 'none'),
         '### b643`s hinges %d ; the refined count %d.' % (sum(r['old_hinge'] for r in rows), sum(r['hinge'] for r in rows)), '']
    L.append('### THE HEADS THAT LEAVE (%d):' % len(leave))
    L += ['  %-34s %-24s %s' % (r['head'], r['status'], why(r)) for r in leave]
    L += ['', '### THE HEADS THAT JOIN (%d):' % len(join)] + ['  %-34s %-24s %s' % (r['head'], r['status'], why(r)) for r in join]
    L += ['', '### THE HINGES UNDER THE REFINED DEFINITION (%d):' % sum(r['hinge'] for r in rows)]
    for r in rows:
        if r['hinge']:
            L.append('  %-34s %-24s across kernels: %s ; across chains within: %s' % (r['head'], r['status'], r['hinge_kernels'] or 'no',
                                                                                     r['hinge_chains'] or 'no'))
    L += ['', '### THE DOMAIN HEADS, PRINTED WITH THEIR CHAINS AND SET ASIDE (%d):' % sum(r['status'] == 'DOMAIN' for r in rows)]
    for r in rows:
        if r['status'] == 'DOMAIN':
            L.append('  %-34s %s' % (r['head'], ' ; '.join('%s: %s' % (p['kernel'], ('consumers %d, chains %d' % (p['consumers'], p['n_chains']))
                                                                     if p.get('read') else 'UNREAD (%s)' % p['why'][:90]) for p in r['per'])))
    L += ['', '### EVERY HEAD, PER KERNEL, THE EVIDENCE REMOVED BY RULE:']
    for r in rows:
        L.append('%s  [%s]%s%s' % (r['head'], r['status'], '  ### HINGE' if r['hinge'] else '', '  (b643 HINGE)' if r['old_hinge'] else ''))
        for p in r['per']:
            if not p.get('read'):
                L.append('    %s : UNREAD -- %s' % (p['kernel'], p['why']))
                continue
            L.append('    %s : consumers %d ; reach %d ; chains %d%s' % (p['kernel'], p['consumers'], p['reach'], p['n_chains'],
                                                                     (' : ' + ' | '.join(', '.join(t) for t in p['chains'][:6])) if p['n_chains'] else ''))
            for nn, rr in p.get('evidence') or []:
                L.append('      evidence %s -- %s' % (nn, rr))
    nh = sum(r['hinge'] for r in rows)
    L += ['', '### ### **HEADS %d ; b643`S HINGES %d ; LEAVE %d ; JOIN %d ; HINGES UNDER THE REFINED DEFINITION %d ; A DOMAIN HEAD IN THE LIST %d ; '
              'EVIDENCE DECLARATIONS REMOVED %d ; HEADS WITH A KERNEL UNREAD %d.**' % (
                  len(rows), sum(r['old_hinge'] for r in rows), len(leave), len(join), nh, sum(1 for r in rows if r['hinge'] and r['status'] == 'DOMAIN'),
                  sum(len(p.get('evidence') or []) for r in rows for p in r['per'] if p.get('read')), sum(1 for r in rows if r['unread']))]
    put_txt('b644_hinges.txt', L)
    put_json('b644_hinges.json', dict(at=utc(), ifaces=ifaces, rows=rows))
    print(NL.join(L[3:4] + L[-1:]))


# ================================================================================ COMPONENT 2: THE CENSUS AT v0.7.1, (R254)(4)-(5)
# ### v0.7 carried line for line, three changes: (1) the glossary block regenerated from data/glossary.txt by the generator's own builder (the
# ### refined HINGE entry joins it; the pages' block byte for byte); (2) the v0.7.1 version line above v0.7's; (3) a v0.7.1 back matter at the end:
# ### the refined definition, the evidence rule, the premise table with the refined hinge column and the consumers column (UNREAD with the
# ### module where a build recorded RUN-BENEATH-HOLD), each head that leaves b643's 28 and why, the version history. No cell is typed: every row
# ### and count is read from data/b644_hinges.json, data/b643_premise_table.json and data/b644_iface_builds.json.
V71_TAG = '## Back matter of the v0.7.1 edition — written 2026-10-09 by b644 under the author’s ruling `(R254)`(4)-(5), by the form of `(R187)`(5)'


def _glossary_block_at(rev):
    import tempfile
    import chain_page as CP
    old = subprocess_out(['git', '-C', RELAY, 'show', '%s:data/glossary.txt' % rev])
    p = os.path.join(tempfile.mkdtemp(), 'glossary_at.txt')
    open(p, 'wb').write(old)
    return CP.glossary_block(p)


def subprocess_out(cmd):
    import subprocess
    return subprocess.run(cmd, capture_output=True).stdout


def _rbh_modules():
    """{Interfaces module: lows} for every Interfaces build recorded RUN-BENEATH-HOLD (data/b644_iface_builds.json)."""
    return dict((r['module'], r['build']['lows']) for r in jl('b644_iface_builds.json').get('rows') or [] if r['build']['verdict'] == 'RUN-BENEATH-HOLD')


def _reconcile():
    """{head: (status, non-vacuity, why)} for the heads whose STATUS and NON-VACUITY disagree as the author's word at b644 reads them: a WITNESSED
    status requires a witness theorem -- one of the head's own-evidence declarations concluding it (E1, E3a or E3b, data/b644_hinges.json)
    -- and absent one the status is OPEN."""
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    HJ = dict((r['head'], r) for r in jl('b644_hinges.json').get('rows') or [])
    out = {}
    for h, r in PT.items():
        if r['status'] == 'WITNESSED' and not r['nonvacuity'].startswith(('WITNESSED', 'DEGENERATE')):
            wit = [n for p in (HJ.get(h) or {}).get('per') or [] if p.get('read') for n, why in p.get('evidence') or [] if not why.startswith('E2')]
            if wit:
                out[h] = ('WITNESSED', 'WITNESSED (%s, its kernel’s own witness; the non-vacuity reader read one kernel’s salt file)' % wit[0].split('.')[-1],
                          'a witness theorem found among its own evidence: %s' % wit[0])
            else:
                out[h] = ('OPEN', r['nonvacuity'], 'no witness theorem: the status WITNESSED read as OPEN')
    return out


def _v71_rows():
    HJ, PT = jl('b644_hinges.json'), dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    RC = _reconcile()
    rbh = _rbh_modules()
    rows = []
    for r in HJ.get('rows') or []:
        h = r['head']
        cells = []
        for p in r['per']:
            if p.get('read'):
                ev = len(p.get('evidence') or [])
                cells.append('%s %d%s' % (p['kernel'], p['consumers'], (', its evidence %d apart' % ev) if ev else ''))
            else:
                mods = re.findall(r'\(([^)]*)\)', p.get('why') or '')
                decls = mods[0].split(', ') if mods else []
                unread_mods = sorted(set(d.split('.')[0] for d in decls))
                tag = ', '.join('Interfaces/%s.lean, RUN-BENEATH-HOLD' % m if m in rbh else m for m in unread_mods) or p['kernel']
                cells.append('%s UNREAD (%s)' % (p['kernel'], tag))
        n = sum(p['consumers'] for p in r['per'] if p.get('read'))

        def _ch(p):
            names = ['`%s`' % t[0].split('.')[-1] if not t[0].startswith('(a cycle)') else 'a cycle at `%s`' % t[0].split()[-1].split('.')[-1]
                     for t in p['chains']]
            return '%d chains, %s%s' % (p['n_chains'], ', '.join(names[:6]), (' and %d more' % (len(names) - 6)) if len(names) > 6 else '')
        if r['hinge']:
            hc = 'HINGE: %s' % '; '.join((['kernels ' + ', '.join(r['hinge_kernels'])] if r['hinge_kernels'] else []) +
                                         ['in %s %s' % (p['kernel'], _ch(p)) for p in r['per'] if p.get('read') and p['kernel'] in r['hinge_chains']])
        elif r['status'] == 'DOMAIN' and r['shape']:
            hc = 'DOMAIN, not a hinge: %s' % '; '.join((['kernels ' + ', '.join(r['hinge_kernels'])] if r['hinge_kernels'] else []) +
                                                       ['in %s %s' % (p['kernel'], _ch(p)) for p in r['per'] if p.get('read') and p['n_chains'] > 1])
        else:
            hc = '—'
        st_, nv_ = RC[h][:2] if h in RC else (r['status'], PT[h]['nonvacuity'])
        rows.append(dict(head=h, status=st_, nonvacuity=nv_, cons='%d (%s)' % (n, '; '.join(cells)) if any(
            p.get('read') for p in r['per']) else '; '.join(cells), hinge=hc, is_hinge=r['hinge'], old=r['old_hinge']))
    return rows


def _v71_backmatter():
    HJ = jl('b644_hinges.json')
    rows = _v71_rows()
    leave = [r for r in HJ.get('rows') or [] if r['old_hinge'] and not r['hinge']]
    join = [r for r in HJ.get('rows') or [] if r['hinge'] and not r['old_hinge']]
    ev = collections.Counter(x[1].split(' (')[0] for r in HJ.get('rows') or [] for p in r['per'] if p.get('read') for x in p.get('evidence') or [])
    rbh = _rbh_modules()
    IB = jl('b644_iface_builds.json').get('rows') or []

    def why(r):
        if r['status'] == 'DOMAIN':
            return 'DOMAIN: a Mathlib predicate restricting a quantified variable, printed with its chains and not a hinge of the programme'
        return 'its own evidence removed: %s' % ', '.join('in %s %d chain%s' % (p['kernel'], p['n_chains'], '' if p['n_chains'] == 1 else 's')
                                                        for p in r['per'] if p.get('read') and p['consumers'])
    L = ['', V71_TAG, '',
         '### The readings v0.7.1 adds, each the seat’s and strikeable', '',
         '- **HINGE, refined.** The glossary’s HINGE entry appended at v0.7.1: a premise of one of the five programme statuses whose consumers lie '
         'in more than one kernel, or in more than one chain within a kernel, the chains taken after the premise’s own evidence is removed from '
         'the use-graph; a premise of status DOMAIN is printed with its chains and is not a hinge. The entry v0.7 counted under, and the first '
         'form of this one (which named its own date as the entry it replaced), stand above it in the glossary, each marked superseded.',
         '- **The premise’s own evidence**, in the glossary’s words (its entry `own evidence`, the one definition the count follows): '
         '“%s”. Read by statement through the table’s textual reader, at each kernel’s HEAD (relay `data/b644_hinges.txt`).' % (
             _gl()['own evidence'].replace('`', '')),
         '- **The Interfaces of SIDE-global-section.** Each module built, one per call, at the mathlib4 checkout its banked profile was built '
         'with. The hold is the free memory, 2,560 MB, beneath which no build of the programme runs: a build whose sampled free memory falls '
         'beneath it is stopped and tried once more, and a second fall records the module RUN-BENEATH-HOLD, unbuilt. Its consumers are UNREAD '
         'and the consumers column names the module (relay `data/b644_iface_builds.txt`). %s' % (
             'Every head with a kernel unread is of status DOMAIN (%s), and a DOMAIN head is not a hinge, so the unread consumers cannot change '
             'the hinge list.' % ', '.join(sorted(r['head'] for r in HJ.get('rows') or [] if r['unread'])) if all(
                 r['status'] == 'DOMAIN' for r in HJ.get('rows') or [] if r['unread']) else
             'The heads with a kernel unread are not all of status DOMAIN (%s); their hinge reading is incomplete.' % ', '.join(
                 '%s %s' % (r['head'], r['status']) for r in HJ.get('rows') or [] if r['unread'])),
         '- **STATUS beside NON-VACUITY.** A WITNESSED status requires a witness theorem; absent one the status is OPEN (the author’s word at b644). '
         'The heads the two columns disagreed on, reconciled by the banks: %s.' % ('; '.join(
             '%s -- %s, now %s / %s' % (h, why, st_, nv_) for h, (st_, nv_, why) in sorted(_reconcile().items())) or 'none'),
         '- **The numerals.** In this back matter every numeral is a count of the table’s own rows or cells, or of the evidence removed.', '',
         '### The premise table at v0.7.1: status, non-vacuity, consumers, hinge', '',
         '| head | status | non-vacuity | consumers (by kernel) | hinge |', '|:--|:--|:--|:--|:--|']
    L += ['| %s | %s | %s | %s | %s |' % (r['head'], r['status'], r['nonvacuity'], r['cons'], r['hinge']) for r in rows]
    L += ['', '*%d heads. Hinges under the refined definition: %d (under v0.7’s: %d). Evidence removed: %s. Interfaces modules: %d, built %d, '
          'RUN-BENEATH-HOLD %d%s.*' % (
              len(rows), sum(r['is_hinge'] for r in rows), sum(r['old'] for r in rows), ', '.join('%s %d' % kv for kv in sorted(ev.items())),
              len(IB), sum(1 for x in IB if x['build']['verdict'] == 'BUILT'), len(rbh),
              (' (%s)' % ', '.join(sorted(rbh))) if rbh else ''), '',
          '### The heads that leave v0.7’s hinge list', '']
    L += ['- **%s** (%s): %s.' % (r['head'], r['status'], why(r)) for r in leave]
    L += ['', '### The heads that join it', '']
    L += ['- **%s** (%s): its own evidence removed, the chains it joined part: %s.' % (
        r['head'], r['status'], ', '.join('in %s %d chains' % (p['kernel'], p['n_chains']) for p in r['per'] if p.get('read') and p['n_chains'] > 1))
          for r in join] or ['- none.']
    L += ['', '### Version history', '',
          '- **v0.7.1, 2026-10-09 (b644, `(R254)`(4)-(5))**: the hinges recounted under the refined definition, the premise’s own evidence '
          'removed from the use-graph and the DOMAIN heads set aside; the consumers of SIDE-global-section’s Interfaces read where built and '
          'named UNREAD with the module where not; the glossary’s HINGE entry superseded by the refined one, the old entry kept.',
          '- **v0.7, 2026-10-08 (b643)** and the editions before it: carried above.']
    return L


def edition71(*a):
    """PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md beside v0.7 (unedited), and data/b644_edition.json. `dry`: the scratchpad."""
    import chain_page as CP
    if not jl('b644_hinges.json') or not jl('b644_iface_builds.json'):
        sys.exit('### NO HINGES OR INTERFACES BANK -- NOTHING WRITTEN')
    v7 = lines_of(K.show(K.CEN7))
    ob, nb = _glossary_block_at(K.PRE_RELAY), CP.glossary_block()
    at = [i for i in range(len(v7)) if v7[i:i + len(ob)] == ob]
    vl = [i for i, l in enumerate(v7) if l.startswith('*v0.7, 2026-10-08')]
    if len(at) != 1 or len(vl) != 1:
        sys.exit('### THE GLOSSARY BLOCK (%s) OR THE VERSION LINE (%s) NOT FOUND ONCE -- NOTHING WRITTEN' % (at, vl))
    i, j = at[0], vl[0]
    hj = jl('b644_hinges.json')
    ver = ('*v0.7.1, 2026-10-09 -- the hinges recounted under the refined definition (%d, from v0.7’s %d), the premise’s own evidence removed '
           'and the DOMAIN heads set aside; the consumers of SIDE-global-section’s Interfaces read where built; the glossary’s HINGE entry '
           'superseded; v0.7 stands beside it, unedited.*' % (sum(r['hinge'] for r in hj['rows']), sum(r['old_hinge'] for r in hj['rows'])))
    out = v7[:i] + nb + v7[i + len(ob):j] + [ver, ''] + v7[j:] + _v71_backmatter()
    b = (NL.join(out) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b644_census_dry.md') if DRY else os.path.join(PP, *K.CEN71.split('/'))
    if not DRY and os.path.exists(dest) and 'regen' not in a:
        sys.exit('### v0.7.1 EXISTS -- NOTHING WRITTEN (`regen` regenerates this act`s own edition, on the author`s word before the seal)')
    _write(dest, b)
    put_json('b644_edition.json', dict(at=utc(), path=K.CEN71, sha256=sha(b), bytes=len(b), lines=len(out), glossary_at=i + 1,
                                       glossary_lines=len(nb), version_line=j + len(nb) - len(ob) + 1, backmatter=out.index(V71_TAG) + 1,
                                       v7_lines=len(v7), dry=DRY))
    print('  %s : %d lines, %d bytes, sha256 %s ; the glossary block %d lines at :%d (was %d) ; the back matter at :%d' % (
        ('DRY ' + dest) if DRY else K.CEN71, len(out), len(b), sha(b)[:16], len(nb), i + 1, len(ob), out.index(V71_TAG) + 1))


def termscan71(*a):
    """data/b644_census_termscan.txt: the scanner over the census at v0.7.1, its verdict printed."""
    t = _scan(os.path.join(PP, *K.CEN71.split('/')))
    put_txt('b644_census_termscan.txt', t.rstrip(NL).split(NL))
    print('  ' + ' ; '.join(l.strip() for l in t.split(NL) if re.search(r'live uses|VERDICT', l)) + ' ; clean %s' % _clean(t))


def edition_diff71(*a):
    """data/b644_edition_diff.txt: v0.7.1 against v0.7, by section, every changed line printed with its kind."""
    import difflib
    v7 = lines_of(K.show(K.CEN7))
    v71 = lines_of(io.open(os.path.join(PP, *K.CEN71.split('/')), encoding='utf-8').read())
    L = ['b644 -- COMPONENT 2: v0.7.1 AGAINST v0.7, BY SECTION (%s)' % utc(), '']
    kinds, removed = collections.Counter(), 0
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, v7, v71, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        removed += a2 - a1
        head = next((v71[k] for k in range(min(b1, len(v71) - 1), -1, -1) if v71[k].startswith('#')), '(the head)')
        kinds[tag] += 1
        L.append('### %s at v0.7 :%d-:%d -> v0.7.1 :%d-:%d ; section: %s ; removed %d, added %d' % (
            tag.upper(), a1 + 1, a2, b1 + 1, b2, head[:90], a2 - a1, b2 - b1))
        L += ['    - %s' % l[:200] for l in v7[a1:a2]][:6] + ['    + %s' % l[:200] for l in v71[b1:b2]][:8]
    L += ['', '### ### **HUNKS %d (%s) ; v0.7 LINES REMOVED OR REPLACED : %d.**' % (sum(kinds.values()), dict(kinds), removed)]
    put_txt('b644_edition_diff.txt', L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 2: THE PAGES RE-EMITTED, THE PAGE CLAUSE (OT :12190)
# ### The census at v0.7.1 names page nodes, and the glossary block both pages print moved: each page is re-emitted from its banked probe (b643's,
# ### data/b643_probe_out_<k>.txt; no lean call), diffed by kind against PLACE-papers HEAD, and written when its bytes differ.
def _corr_rows(text):
    i = text.find('\n## Correspondence')
    return re.findall(r'^\| `([^`]+)`', text[i:], re.M) if i >= 0 else []


def _kind(l):
    if l.startswith('| `'):
        return 'a Correspondence or Placement row'
    if l.startswith('- **'):
        return 'a glossary line'
    if re.match(r'^\d+\. |^- `|^`', l):
        return 'a node line'
    if l.startswith('#'):
        return 'a heading'
    return 'other'


def page(k, *a):
    """the page `k` (zeta | chi) re-emitted from the banked probe; data/b644_page_<k>.json."""
    import difflib
    import subprocess
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    src = os.path.join(D, K.PROBE[k])
    rc, pg, _meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b644_%s' % k), src)
    if rc:
        sys.exit('### %s RE-EMIT FROM THE BANKED PROBE FAILED, exit %d %s' % (k, rc, log[-2:]))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    pt = prev.decode('utf-8')
    changed = prev != b
    dl = [x for x in difflib.unified_diff(pt.split(NL), pg.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    kinds = collections.Counter('%s %s' % ('added' if x[0] == '+' else 'removed', _kind(x[1:])) for x in dl)
    c0, c1 = _corr_rows(pt), _corr_rows(pg)
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    put_json('b644_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), probe=K.PROBE[k], changed=changed,
                                           written=bool(changed and not DRY), kinds=dict(kinds), corr_before=len(c0), corr_after=len(c1),
                                           diff=dl, free_mb_before=fm, at=utc()))
    print('  %s : exit %d ; changed against HEAD %s ; Correspondence %d -> %d' % (k, rc, changed, len(c0), len(c1)))
    for kk, n in sorted(kinds.items()):
        print('      %-50s %d' % (kk, n))
    for x in dl:
        print('      ' + x[:220])


def page_arms(*a):
    """the page arms (G-CHAIN-PAGE, G-CHAIN-PAGE-CHI) on the lists in force against PLACE-papers HEAD; data/b644_page_arms.txt."""
    import g_chain_page as GCP
    L = ['b644 -- THE PAGE ARMS AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b644_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; first differing line %s' % (arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'],
                                                                                         r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    put_txt('b644_page_arms.txt', L)
    print(NL.join(l[:200] for l in L))


# ================================================================================ COMPONENT 3: THE TWO ROSTERS, (R254)(6)
# ### (a) The census's section list and its roster header (§1's table header, one row per phase and cluster), and for each keystone the §1
# ### rows name by tier: its REGISTRY row, and where its phase and its subject cluster come from -- a FIELD (a cell of its own REGISTRY row names
# ### a phase or a cluster), the HEADING (the REGISTRY section heading the row sits under), or a PATH FRAGMENT (the directories of its file
# ### cell) -- each reading printed and whether they agree. No edition changed; the cluster, phase and maturity columns are v0.8's.
TIER_RE = re.compile(r'\b(KC|K|C|N): ([^;|]+)')


def _registry_rows():
    t = K.show('REGISTRY.md', 'HEAD') or ''
    rows, head2, head3, header = {}, '', '', []
    ID = re.compile(r'^(?:d1-|1\.5[a-h]-|p2-d?|m5-)\d+$')
    for i, l in enumerate(t.split(NL), 1):
        if l.startswith('## '):
            head2, head3 = l[3:].strip(), ''
        elif l.startswith('### '):
            head3 = l[4:].strip()
        elif l.startswith('|:'):
            continue
        elif l.startswith('|'):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if not any(ID.match(c.strip('`* ')) for c in cells[:2]) and not re.search(r'`[^`]+\.(?:md|py|lean|txt)`', l):
                header = cells       # ### a table's header row: the next rows' columns
                continue
            fm = re.search(r'`([^`]+\.(?:md|py|lean|txt))`', l)
            ids = [c.strip('`* ') for c in cells[:2] if ID.match(c.strip('`* '))]
            field = [(header[j], cells[j]) for j in range(min(len(header), len(cells))) if re.search(r'\bphase\b|\bcluster\b', header[j], re.I)]
            for k_ in ids + ([os.path.basename(fm.group(1))] if fm else []):
                if k_ and k_ not in rows:
                    rows[k_] = dict(line=i, h2=head2, h3=head3, file=fm.group(1) if fm else '', cells=cells, field=field)
    return rows


def census_roster(*a):
    """data/b644_census_roster.txt: the census's sections and roster header, and each keystone's phase and cluster -- field, heading or path."""
    path = K.CEN71 if os.path.exists(os.path.join(PP, *K.CEN71.split('/'))) else K.CEN7
    t = io.open(os.path.join(PP, *path.split('/')), encoding='utf-8').read().replace(chr(13), '')
    ls = t.split(NL)
    secs = [(i + 1, l) for i, l in enumerate(ls) if re.match(r'^#{1,3} ', l)]
    hdr = [(i + 1, l) for i, l in enumerate(ls) if l.startswith('| row | phase and cluster |')]
    R = _registry_rows()
    L = ['b644 -- COMPONENT 3, (R254)(6)(a): THE CENSUS ROSTER -- ITS SECTIONS, ITS ROSTER HEADER, EACH KEYSTONE`S PHASE AND CLUSTER (%s)' % utc(), '',
         '### the census read: PLACE-papers %s at %s ; REGISTRY.md at HEAD ; no edition changed' % (path, g(PP, 'rev-parse', '--short=7', 'HEAD').strip()),
         '', '### THE SECTION LIST (%d headings):' % len(secs)]
    L += ['  :%-5d %s' % (i, l[:150]) for i, l in secs]
    L += ['', '### THE ROSTER HEADER (§1):'] + ['  :%d %s' % (i, l) for i, l in hdr]
    L += ['', '### EACH KEYSTONE §1 NAMES BY TIER: its REGISTRY row; PHASE and CLUSTER read as FIELD (a cell of the row names one), HEADING (the '
          'REGISTRY section the row sits under), PATH (its file cell`s directories); AGREE where heading and path name the same phase', '']
    n = collections.Counter()
    for l in ls:
        m = re.match(r'^\| (R\d\d) \| ([^|]*) \| [^|]* \| ([^|]*) \|', l)
        if not m:
            continue
        for tier, names in TIER_RE.findall(m.group(3)):
            for nm in [x.strip().strip('`') for x in names.split(',')]:
                nm = re.sub(r'\s*\(.*$', '', nm).strip()
                if not nm or nm.startswith('no tier'):
                    continue
                r = R.get(nm)
                if not r:
                    L.append('  %s %-4s %-40s ### NO REGISTRY ROW FOUND BY ID OR FILE NAME' % (m.group(1), tier, nm))
                    n['unfound'] += 1
                    continue
                field = r['field']
                dirs = os.path.dirname(r['file'])
                pp_ = re.match(r'(?:phase([\d.]+)|day(\d))', dirs)
                ph_path = ('1' if pp_.group(2) else pp_.group(1)) if pp_ else ''
                hd = r['h3'] or r['h2']
                ph_ = re.search(r'\bPhase\s*([\d.]+)([A-Z]?)\b', hd) or re.match(r'^([\d.]+)([A-Z])\b', hd) or re.match(r'^DAY (\d)()', hd)
                ph_head, cl_head = (ph_.group(1), ph_.group(2)) if ph_ else ('', '')
                agree = bool(ph_path and ph_head and ph_path == ph_head)
                n['FIELD' if field else 'NOFIELD'] += 1
                n['PATH' if ph_path else 'NOPATH'] += 1
                L.append('  %s %-4s %-46s REGISTRY :%-5d heading `%s` (phase %s, cluster %s) ; path `%s` (phase %s) ; field %s ; phase heading '
                         'and path %s' % (m.group(1), tier, nm[:46], r['line'], hd[:60], ph_head or '-', cl_head or '-', dirs or '-', ph_path or '-',
                                         ('YES: ' + '; '.join('%s = %s' % (a_, b_[:40]) for a_, b_ in field)) if field else 'NO',
                                         'AGREE' if agree else ('DIFFER' if ph_path and ph_head else 'ONE ABSENT')))
                n['agree' if agree else 'differ'] += 1
    L += ['', '### ### **KEYSTONES READ %d ; A ROW CELL NAMING A PHASE OR CLUSTER %d ; A PATH FRAGMENT %d ; HEADING AND PATH AGREE %d ; DIFFER OR '
              'ABSENT %d ; NO REGISTRY ROW %d.** The phase and the cluster of every keystone come from the REGISTRY heading its row sits under; '
              'a file path carries a phase directory where it has one; v0.8 decides which is the column.' % (
                  n['FIELD'] + n['NOFIELD'], n['FIELD'], n['PATH'], n['agree'], n['differ'], n['unfound'])]
    put_txt('b644_census_roster.txt', L)
    print(NL.join(L[-1:]))


# ### (b) Every local clone (a `.git` under D:\ to depth three, `.lake` trees excluded), its remote URL from `git remote -v` (the clone's own
# ### config; no API call), diffed against the repositories data/act_roots.txt's last root names; each clone outside the chain listed with its
# ### last commit date and its build state as it stands on disk (build products present, its build files) -- no build is run for it, every
# ### lean call being under the hold. The patent repository is counted and its name withheld (the b590 rule). The author's naming is a prompt.
PRIVATE = ('patent-package',)


def repo_roster(*a):
    import act_root as AR
    clones = [x.strip() for x in io.open(os.path.join(SP, 'clones.txt'), encoding='utf-8') if x.strip()]
    last = [l.split()[0] for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8') if l.strip()][-1]
    heads = sorted((jl('%s_act_root.json' % last).get('reads') or {}).get('heads') or {})
    chain_paths = dict((AR.path_of(h).replace('\\', '/').lower().rstrip('/'), h) for h in heads)
    L = ['b644 -- COMPONENT 3, (R254)(6)(b): THE REPOSITORY ROSTER -- EVERY LOCAL CLONE`S REMOTE AGAINST THE CHAIN`S %d (%s)' % (len(heads), utc()), '',
         '### the chain: data/act_roots.txt`s last line (%s), its root bank`s repositories, %d; the clones: every .git under D:\\ to depth three '
         '(%d); each remote read from the clone`s own config by `git remote -v`; no API call; no build run (the hold governs every lean call).' % (
             last, len(heads), len(clones)), '']
    inside, outside, withheld = [], [], 0
    seen_chain = set()
    for c in clones:
        p = ('D:' + c[2:]) if c.startswith('/d/') else c
        key = p.replace('\\', '/').lower().rstrip('/')
        if any(x in p for x in PRIVATE):
            withheld += 1
            continue
        rem = [l.split()[1] for l in g(p, 'remote', '-v').split(NL) if l.strip().endswith('(fetch)')]
        date = g(p, 'log', '-1', '--format=%cs').strip() or 'no commit'
        lake = os.path.isdir(os.path.join(p, '.lake', 'build', 'lib'))
        olean = os.path.isdir(os.path.join(p, 'build')) and any(f.endswith('.olean') for f in os.listdir(os.path.join(p, 'build'))[:2000])
        files = [f for f in ('lakefile.lean', 'lakefile.toml', 'lean-toolchain') if os.path.exists(os.path.join(p, f))]
        row = dict(path=p, remote=rem[0] if rem else 'NO REMOTE', date=date, products='.lake/build' if lake else ('build/*.olean' if olean else 'none'),
                   files=files)
        if key in chain_paths:
            inside.append((chain_paths[key], row))
            seen_chain.add(chain_paths[key])
        else:
            outside.append(row)
    L.append('### IN THE CHAIN, A LOCAL CLONE AT ITS PATH (%d of %d):' % (len(inside), len(heads)))
    L += ['  %-34s %-62s last commit %s' % (h, r['remote'][:62], r['date']) for h, r in sorted(inside)]
    missing = sorted(set(heads) - seen_chain)
    L += ['', '### IN THE CHAIN, NO CLONE AT ITS PATH (%d): %s' % (len(missing), ', '.join(missing) or 'none'), '',
          '### OUTSIDE THE CHAIN (%d), each with its remote, its last commit, its build state on disk:' % len(outside)]
    for r in outside:
        rn = r['remote'].rstrip('/').split('/')[-1].replace('.git', '') if r['remote'] != 'NO REMOTE' else ''
        twin = ' ; same remote as the chain`s %s' % rn if rn in heads else ''
        L.append('  %-44s remote %-60s last commit %-10s ; build products %-13s ; build files %s%s' % (
            r['path'], r['remote'][:60], r['date'], r['products'], ', '.join(r['files']) or 'none', twin))
    L += ['', '### a local-only private repository counted and not named (the b590 rule): %d' % withheld, '',
          '### ### **CLONES %d ; IN THE CHAIN %d OF %d ; CHAIN REPOSITORIES WITH NO CLONE AT THEIR PATH %d ; OUTSIDE THE CHAIN %d (OF THEM A SECOND '
          'CLONE OF A CHAIN REMOTE %d, NO REMOTE %d) ; WITHHELD %d.** Which outsider joins the chain, retires or stands aside, and any repository on '
          'the account with no local clone, is the author`s to name.' % (
              len(clones), len(inside), len(heads), len(missing), len(outside),
              sum(1 for r in outside if r['remote'].rstrip('/').split('/')[-1].replace('.git', '') in heads),
              sum(1 for r in outside if r['remote'] == 'NO REMOTE'), withheld)]
    put_txt('b644_repo_roster.txt', L)
    put_json('b644_repo_roster.json', dict(at=utc(), chain=heads, inside=[dict(repo=h, **r) for h, r in inside], outside=outside, withheld=withheld))
    print(NL.join(L[-1:]))


# ================================================================================ COMPONENT 4: THE PATCH EDITIONS, (R254)(7)
# ### W-ORD-DAY1-PATCH-VERSIONS (OPEN_TRAILS :13397) as b641 resolved it, with the author's answer at b644 for ONE_PAGE_PROOF: b641's `label v1.3`
# ### was SIDE-kernel's tag (b639's reader took the first version string in the file's first 4000 bytes), the document has no label line and
# ### REGISTRY's d1-8 row gives v1.0, so it takes v1.0.1 on a new label line under the author line. Each label and its dated line are written by
# ### the seat through the Edit tool, each committed alone; this tool plans them (the label line, the new label, the dated line's text) and banks
# ### the result (each diff's line count, the scanner on each). What moved is read against the deposited bytes (PLACE-papers
# ### outputs/DEPOSITED-v1.1.2), by section heading, and the commits since the deposit that touched the file.
COMPANIONS = [('Exhaustive_Enumeration', 'v2.3', 'v2.3.1'), ('Which_Structure_Confines', 'v2.3', 'v2.3.1'), ('Spectral_Inertness', 'v2.3', 'v2.3.1'),
              ('Seven_Mechanism_Classes', 'v3.3', 'v3.3.1'), ('Third_Identity_Element', 'v2.3', 'v2.3.1'),
              ('Silence_of_Foundations', 'v2.3', 'v2.3.1'), ('ONE_PAGE_PROOF', None, 'v1.0.1')]
DEPOSIT_DATE = '2026-07-24'


def _moved(name):
    import difflib
    dep = (K.show('outputs/DEPOSITED-v1.1.2/%s.md' % name, 'HEAD') or '').split(NL)
    cur = (K.show('day1/%s.md' % name, 'HEAD') or '').split(NL)
    secs = collections.OrderedDict()
    n = 0
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, dep, cur, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        n += (a2 - a1) + (b2 - b1)
        block = NL.join(cur[b1:b2])
        if '## Correspondence' in block:
            what = 'the Correspondence section appended after the References (added 2026-08-12, additive) with the notes since within it'
        elif 'CLASS-NUMBERING SCHEME' in block:
            what = 'the class-numbering note beneath the title'
        elif '*(Grammar' in block:
            what = 'a grammar note beneath the theorem (:%d)' % (b1 + 2 + 2)     # ### the edition's own lines: the dated line and its blank add two
        elif tag == 'replace':
            what = 'one line amended (:%d)' % (b1 + 1 + 2)
        else:
            what = '%d lines %s at :%d' % (max(a2 - a1, b2 - b1), 'inserted' if tag == 'insert' else 'removed', b1 + 1)
        secs[what] = 1
    commits = [l for l in g(PP, 'log', '--format=%h %cs', '--since=%s' % DEPOSIT_DATE, '--', 'day1/%s.md' % name).split(NL) if l.strip()]
    return n, list(secs), commits


def patch_plan(*a):
    """prints, per companion, its label line (by line number), the new label and the dated line to write beneath it; writes nothing."""
    out = []
    for name, old, new in COMPANIONS:
        t = K.show('day1/%s.md' % name, 'HEAD')
        ls = t.split(NL)
        al = [i for i, l in enumerate(ls) if l.startswith('**J. York Seale**')]
        n, secs, commits = _moved(name)
        lab = (old or 'none')
        dl = ('*%s, 2026-10-09 -- the patch label of the edition deposited as %s on %s (Zenodo v1.1.2), under `(R254)`(7). What moved since '
              'that edition, %d lines against its deposited bytes: %s; by the commits %s. The text otherwise stands as it stood.*' % (
                  new, old if old else 'v1.0 (REGISTRY’s d1-8 row)', DEPOSIT_DATE, n, '; '.join(secs), ', '.join(commits)))
        out.append(dict(name=name, author_line=al[0] + 1 if al else None, author_text=ls[al[0]] if al else None, old=old, new=new,
                        dated=dl, moved_lines=n, sections=secs, commits=commits))
        print('== %s : author line :%s ; label %s -> %s ; moved %d lines ; sections %d ; commits %s' % (
            name, al[0] + 1 if al else '?', lab, new, n, len(secs), ', '.join(commits)))
        print('   ' + dl)
    put_json('b644_patch_plan.json', dict(at=utc(), rows=out))


def patch_bank(*a):
    """data/b644_patch_editions.txt: each companion's edition commit (read from git, the commit touching its file alone), its label before and
    after, the diff's line count, the scanner's live uses on the file at the commit and at its parent, the mirror roster's commit."""
    import tempfile
    L = ['b644 -- COMPONENT 4, (R254)(7): THE SEVEN PATCH EDITIONS, EACH THROUGH THE EDIT TOOL AND COMMITTED ALONE (%s)' % utc(), '',
         '### W-ORD-DAY1-PATCH-VERSIONS (OPEN_TRAILS :%d) as b641 resolved it; ONE_PAGE_PROOF by the author`s answer at b644 (v1.0.1, a new label '
         'line; b641`s v1.3 was SIDE-kernel`s tag, read by b639`s reader tools/b639_record.py :869-:871)' % K.OT_PATCH, '']
    n_ok = 0
    for name, old, new in COMPANIONS:
        path = 'day1/%s.md' % name
        c = g(PP, 'log', '--format=%h', '-1', '--grep=^b644 Component 4', '--', path).strip()
        files = [x for x in g(PP, 'show', '--name-only', '--format=', c).split(NL) if x.strip()] if c else []
        ns = g(PP, 'show', '--numstat', '--format=', c).strip() if c else ''
        live = []
        for rev in (c, c + '^'):
            p = os.path.join(tempfile.mkdtemp(), os.path.basename(path))
            open(p, 'wb').write(subprocess_out(['git', '-C', PP, 'show', '%s:%s' % (rev, path)]))
            m = re.search(r'live uses\s*:\s*(\d+)', _scan(p))
            live.append(int(m.group(1)) if m else None)
        after = K.show(path, c) or ''
        has_new = ('| %s, October 2026' % new in after) or ('%s, October 2026' % new in after)
        ok = bool(c) and files == [path] and has_new and live[0] == live[1]
        n_ok += ok
        L.append('  %-28s %s -> %-7s commit %s alone %s ; numstat %s ; the new label on the file %s ; scanner live uses at the commit %s, at its '
                 'parent %s (the edit adds none: %s)' % (name, old or 'none', new, c or '### NONE', files == [path], ns.replace('\t', ' '),
                                                        has_new, live[0], live[1], live[0] == live[1]))
    rc = g(RELAY, 'log', '--format=%h %s', '-1', '--', 'tools/mirror_roster.json').strip()
    L += ['', '### the mirror roster: relay %s' % rc[:200], '### the seven appended at the end with the census at v0.7 and v0.7.1 (the author`s '
          'answer at b644); the ruling`s `roster edited to the patch labels` has no roster object -- the labels live inside the files',
          '', '### ### **COMPANIONS %d ; LABELLED AND COMMITTED ALONE, THE SCANNER UNMOVED %d.**' % (len(COMPANIONS), n_ok)]
    put_txt('b644_patch_editions.txt', L)
    print(NL.join(L[4:]))


# ================================================================================ COMPONENT 5: THE DESCRIPTION AS SYNTHESIS, (R254)(8)
# ### The composer carried from b640's (tools/b640_record.py :554 compose, which stays as sealed) into this tool, re-cut to five parts in the
# ### ruled order and nothing else: (i) THE CLAIM, (ii) WHAT IS MACHINE-VERIFIED, (iii) WHAT THE LOAD-BEARING THEOREMS ASSUME, (iv) WHAT IS OPEN,
# ### (v) HOW A DEFECT IS REPORTED. Every figure, name, grade, status, print and line is read: the glossary (relay data/glossary.txt) by the
# ### generator's parser; README's supportable and not-supportable sentences; the terminal table at relay HEAD (grades); the banked
# ### #print axioms lines (the page probes and b557's lv probe); the kernels' tags by git; the premise statuses (b643's premise table), the
# ### hinges (b644's recount), the work-orders' discharge clauses (OPEN_TRAILS, the W-ORD-PREMISE-* lines and the four older ones); the
# ### surround's squeeze sentence (THE_UNCONDITIONAL_SURROUND_v0_5 §6a); ERRATA's own statement of its form; the record's creator (the draft's
# ### metadata, read once). Straight quotes, HTML paragraphs, &, < and > escaped (Zenodo straightens curly quotes, b639).
DESC_THEOREMS = [('SIDE-lv-conservation', 'h1_complete_at_Phi'), ('SIDE-explicit-formula', 'h2_sign_iff_rh'),
                 ('SIDE-explicit-formula', 'rh_strip_imp_rh_holds'), ('SIDE-explicit-formula', 'ch_iff_h2_sign_of_seam'),
                 ('SIDE-explicit-formula', 'forall_rh_upto_iff_rh'), ('SIDE-explicit-formula', 'rh_upto_platt'),
                 ('SIDE-explicit-formula', 'dedekind_instance'), ('SIDE-explicit-formula', "dedekind_rhs'"),
                 ('SIDE-explicit-formula', 'rh_iff_nb'), ('SIDE-explicit-formula', 'binomialTransform_holds'),
                 ('SIDE-explicit-formula', 'logDerivSplit_holds'), ('SIDE-explicit-formula', 'stieltjesLog_holds'),
                 ('SIDE-explicit-formula', 'convStep_holds'), ('SIDE-explicit-formula', 'smooth4_holds'),
                 ('SIDE-explicit-formula', 'not_trivialSummandPremise')]
PRINT_BANKS = ('b643_probe_out_zeta.txt', 'b643_probe_out_chi.txt', 'b557_probe_lh.txt')
KERNEL_TAG = {'SIDE-explicit-formula': 'v0.26', 'SIDE-lv-conservation': 'v0.8.0'}
CARRIED_WO = {'ConservationHypothesis': 'W-ORD-H2-BRIDGE', 'KeiperObligations': 'W-ORD-QUANTIFIER-COLUMN',
              'WindowObligations': 'W-ORD-QUANTIFIER-COLUMN', 'farSmall': 'W-ORD-WEIL-CONVERSE'}


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def _gl():
    import chain_page as CP
    d = {}
    for n, de, _s in CP.glossary_entries():
        d[n] = de          # ### a later entry of the same name (the refined HINGE) supersedes the earlier
    return d


def _readme_ceiling():
    t = K.show('README.md', 'HEAD') or ''
    sup = re.search(r'^Supportable: \*([^*]+)\*$', t, re.M)
    nsup = re.search(r'^Not supportable: \*([^*]+)\*', t, re.M)
    return (sup.group(1) if sup else None), (nsup.group(1) if nsup else None)


def _prints():
    out = {}
    for b in PRINT_BANKS:
        for m in re.finditer(r"^'(.+?)' depends on axioms: (\[[^\]]*\])", rd(b), re.M):   # ### a primed name prints as 'x.n'' depends
            out.setdefault(m.group(1), m.group(2))
    return out


def _table_rows():
    T = jl('terminal_table.json')
    return dict(((r['repo'], r['name'].split('.')[-1]), r) for r in T.get('rows') or [])


def _discharge_clauses():
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'^- \*\*(W-ORD-PREMISE-[A-Z0-9-]+)\*\*: the premise (\S+), .*?what would discharge it: (.+)$', ot, re.M):
        out[m.group(2)] = (m.group(1), m.group(3).strip())
    return out


def _rests_on(name):
    """the premise heads a theorem rests on: the heads whose rule rows (b642's status bank) name it."""
    return sorted(v['head'] for v in jl('b642_premise_status.json').get('heads') or []
                  if any(x.split(' ', 1)[-1].split('.')[-1] == name for x in v.get('rule_rows') or []))


def compose():
    gl, (sup, nsup), PR, TR = _gl(), _readme_ceiling(), _prints(), _table_rows()
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    HJ = dict((r['head'], r) for r in jl('b644_hinges.json').get('rows') or [])
    DC = _discharge_clauses()
    creator = jl('b644_draft_meta.json').get('creators') or []
    surround = K.show('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 'HEAD') or ''
    sq = re.search(r'the geometric face names a single concrete analytic target: (the jaws overlap at every height \*\*iff\*\* .+?reaches the zero-free region)',
                   surround)
    errata = K.show('ERRATA.md', 'HEAD') or ''
    ef = re.search(r'Each entry lists: the\s+paper, the affected section or line, the correction, and the date\.', errata)
    P = []
    # ---- (i) THE CLAIM
    sup, nsup = (sup or '').rstrip('.'), (nsup or '').rstrip('.')
    cp = rd('b644_clause_path.txt')
    one = ('h2_sign is the one open clause of the reduction: the dependency path from h2_sign to RiemannHypothesis passes through the seam '
           'rh_strip_imp_rh, a classical fact the kernel compiles (rh_strip_imp_rh_holds), and consumes no OPEN premise; the OPEN premises in '
           'the table belong to the faces, instances and bounds, none on that path [in plain words: every OPEN premise in the table is assumed '
           'only by theorems the reduction from h2_sign to RH does not use], and the table is the keystone census at v0.7.1, in this '
           'record\'s files.' if re.search(r'; OPEN 0 ', cp) else 'NOT READ')
    mx = re.search(r'the mechanism exclusions are (the route terminals of SIDE-kernel) set out under WHAT IS MACHINE-VERIFIED below, (which compile '
                   r'that none of seven named mechanism classes produces the off-line signature the kernel defines, the exhaustiveness of the seven '
                   r'classes over all mechanisms not being compiled)', rd('b640_deposit_description.txt'))
    mex = ('Its mechanism exclusions are %s, %s; they rule out named sources of a zero off the critical line and do not prove h2_sign.' % (
        mx.group(1), mx.group(2)) if mx else 'NOT READ')
    P.append('THE CLAIM. %s is the name of the research programme whose papers, kernels and ledgers this record deposits; it makes its '
             'claim in one sentence, as its README states it: "%s." Here RH is %s. The located clause: '
             '%s. %s h2_sign is %s. %s classK is %s. The ceiling, in the README\'s words: supportable, "%s"; not supported, "%s" -- the corpus does '
             'not support that sentence, since h2_sign is open, and nothing in this record states that the Riemann Hypothesis holds.' % (
                 'A PLACE TO STAND', sup, gl['RH'].rstrip('.'), gl['the located clause'].rstrip('.'), mex, gl['h2_sign'].rstrip('.'), one,
                 gl['classK'].rstrip('.'), sup, nsup))
    # ---- (ii) WHAT IS MACHINE-VERIFIED
    tags = dict((k, g('D:/' + k, 'rev-parse', '--short=7', '%s^{commit}' % t).strip()) for k, t in KERNEL_TAG.items())
    items = []
    for k, n in DESC_THEOREMS:
        r = TR.get((k, n))
        full = [x for x in PR if x.split('.')[-1] == n]
        pr = PR[full[0]] if full else None
        grade = r['grade'] if r else 'not in the table'
        s = '%s (%s at its tag %s = %s; %s; #print axioms %s)' % (n, k, KERNEL_TAG[k], tags[k], grade, pr or 'NOT BANKED')
        stmt = (r or {}).get('statement') or ''
        if n == 'h1_complete_at_Phi':
            conj = [c.strip().split()[0] for c in _split_conclusion(' '.join(stmt.split()))[1].split('∧')]
            s += (' -- it states that the fixed function Phi meets the %d couplings it names at once (%s); its docstring calls it the h1 leg of a '
                  'bracket whose other leg is h2, %s, which stays open' % (len(conj), ', '.join(conj), gl['h2'].split(';')[0]))
        if n.endswith('_holds') and (k, n[:-len('_holds')]) in TR:
            s += ' -- it proves %s, a proposition the kernel defines' % n[:-len('_holds')]
        if grade in ('INTERFACES', 'PREDICATE-UNLISTED'):
            on = _rests_on(n)
            hyp = [x for x in re.findall(r'(\w+)\s*→', _split_conclusion(stmt)[1] or stmt) if (k, x + '_holds') in TR]
            if on:
                s += ' -- it holds on %s' % ', '.join('the premise %s, whose status is %s' % (h, PT[h]['status']) if h in PT else h for h in on)
            elif hyp:
                s += ' -- it holds on %s, which %s proves' % (hyp[0], hyp[0] + '_holds')
            else:
                s += ' -- the premise it holds on is named in its statement'
        items.append(s)
    P.append('WHAT IS MACHINE-VERIFIED. A kernel is %s. A theorem holds at the standard three when its #print axioms reads exactly %s. The grades, read from each statement: DERIVES, %s; '
             'INTERFACES, %s; PREDICATE-UNLISTED, %s [In plain words: the grading rule met a named predicate on one of the statement\'s variables '
             'that its list of restrictions does not yet hold; it marks the theorem for a ruling by the programme\'s author, who rules on the grading '
             'rule, rather than reading the predicate as a premise.] '
             'The named theorems: %s.' % (
                 gl['kernel'].split(':')[0].rstrip('. '), gl['the standard three'].rstrip('.').replace(', written std3', ''),
                 gl['DERIVES'].rstrip('.'), gl['INTERFACES'].rstrip('.'), gl['PREDICATE-UNLISTED'].rstrip('.') + '.', '; '.join(items)))
    # ---- (iii) WHAT THE LOAD-BEARING THEOREMS ASSUME
    order = ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'REFUTED-BY-COMPUTATION')
    parts = []
    for st in order:
        hs = [h for h in PT if PT[h]['status'] == st]
        ents = []
        for h in hs:
            mark = ' (a HINGE)' if (HJ.get(h) or {}).get('hinge') else ''
            if st == 'OPEN':
                d = ('what would discharge it: ' + DC[h][1].rstrip('.')) if h in DC else ('carried by %s' % CARRIED_WO.get(h, 'its work-order'))
            elif st == 'CITED':
                d = 'cited at its literature source and not compiled; a compiled proof would discharge it in the kernel'
            elif st == 'DISCHARGED':
                d = 'discharged where it is used'
            elif st == 'WITNESSED':
                d = 'witnessed by a construction nothing uses; a compiled proof would discharge it'
            else:
                d = ('refuted: its pole term is positive where it requires zero; TrivialSummandPremise\' carries the pole term in its place, '
                     'and dedekind_rhs\' is proved on it')
            ents.append('%s%s, %s' % (h, mark, d))
        parts.append('%s -- %s' % (st, '; '.join(ents)))
    dom = sorted(h for h in PT if PT[h]['status'] == 'DOMAIN')
    hinge_def = gl['HINGE'].replace(' (the entry above)', '').rstrip('.') + '. A premise\'s own evidence is, in the glossary\'s words, %s. ' % (
        gl['own evidence'].replace('of a premise: ', '').rstrip('.')) + ('[In plain words: own evidence is any declaration that is about the '
                                                                         'premise itself -- showing it can hold, cannot hold, or holds under a '
                                                                         'condition -- rather than a use of it.] '
                                                                         '[In plain words: a hinge is a premise that separate lines of the '
                                                                         'kernels\' reasoning lean on, counted once the declarations that only test, '
                                                                         'refute or instance the premise itself are set aside.]')
    wo = 'A name beginning W-ORD- is %s; OPEN_TRAILS is, in its own words, %s.' % (gl['W-ORD'].rstrip('.'), gl['OPEN_TRAILS'].split(';')[0].rstrip('.'))
    sc_ = re.search(r'a salt check -- (a test file that only shows a premise is not vacuous, that is, that it can be satisfied, so that a theorem '
                    r'resting on it is not true merely because nothing satisfies it) --', rd('b640_deposit_description.txt'))
    wo += ' A salt check is %s.' % (sc_.group(1) if sc_ else 'NOT READ')
    tpl = ('WHAT THE LOAD-BEARING THEOREMS ASSUME. A premise is %s; a HINGE is %s ' + wo.replace('%', '%%') + ' The premises, by status: %s. The status DOMAIN marks a '
           'Mathlib predicate that restricts a variable its statement quantifies (%s): not an assumption, and not a hinge. The refuted premise '
           'is TrivialSummandPremise: %s; TrivialSummandPremise\' replaces it, carrying the pole term, and dedekind_rhs\' is proved on the restated '
           'premise. The full table, every premise with its status, its non-vacuity, its consumers by kernel and its hinge, is the keystone '
           'census at v0.7.1 (THE_KEYSTONE_CENSUS_v0_7_1.md, in this record\'s files).')
    P.append(tpl % (gl['premise'].rstrip('.'), hinge_def, ' | '.join(parts), ', '.join(dom),
                    re.sub(r'^the sixth status of a premise: ', '', gl['REFUTED-BY-COMPUTATION']).rstrip('.')))
    # ---- (iv) WHAT IS OPEN
    eq = re.search(r'(Both are equivalent to RH given the surround)\.', surround)
    P.append('WHAT IS OPEN. h2_sign: %s. The squeeze between the zero-free region pressing in from the line of real part one and the transversality '
             'at the critical line has one concrete target, in the words of THE_UNCONDITIONAL_SURROUND: %s. Its faces, the same text says, are '
             'two statements of one open node: "%s", as h2_sign is by h2_sign_iff_rh; the squeeze\'s target is that node seen geometrically, not a '
             'second open premise.' % (gl['h2_sign'], (re.sub(r'\*\*', '', sq.group(1)).strip().rstrip(',')) if sq else 'NOT READ',
                                       eq.group(1) if eq else 'NOT READ'))
    # ---- (v) HOW A DEFECT IS REPORTED
    P.append('HOW A DEFECT IS REPORTED. A defect in this record is filed as an entry of ERRATA.md, in this record\'s files: %s Write to the '
             'record\'s creator, %s.' % (
                 ('ERRATA "records corrections to the deposited line after its Zenodo publication", and each entry lists the paper, the affected '
                  'section or line, the correction, and the date; entries are retained across deposits.') if ef else 'NOT READ',
                 '; '.join('%s (ORCID %s)' % (c.get('name'), c.get('orcid')) for c in creator) or 'NOT READ'))
    return ''.join('<p>%s</p>' % _esc(p.replace('`', '')) for p in P)


ACT_RE = re.compile(r'\bb\d{3}\b')
FORBID = [('an act number', ACT_RE), ('a bank path', re.compile(r'\bdata/|\brelay\b|_act_root|\.json\b')),
          ('root arithmetic', re.compile(r'\b[0-9a-f]{40,64}\b|\bact root\b', re.I)),
          ('a provenance count', re.compile(r'\b\d+\s+(?:cell|rule|rule-elab|none|upstream)\b|\b(?:rule-elab|provenance)\b', re.I)),
          ('a ruling number', re.compile(r'\(R\d{2,3}\)'))]


def forbidden(html):
    """[(kind, match)] for every forbidden content in the description: the act numbers, bank paths, root arithmetic, provenance counts and
    ruling numbers above, the outside collections' names (b641's needles), the two stems (the scanner's), and the ceiling's unsupported
    sentence asserted (b641's repaired needle)."""
    import b640_record as R40   # ### Question 1's needle as b641 repaired it (tools/b640_record.py :777-:791): an assertion, never a denial
    text = re.sub(r'<[^>]+>', ' ', html)
    hits = [(k, m.group(0)) for k, rx in FORBID for m in rx.finditer(text)]
    hits += [('an outside collection', n) for n in OUTSIDE_NEEDLES if n.lower() in text.lower()]
    hits += [('a banned stem', m.group(0)) for m in re.finditer(r'\b(?:gap|blind)\w*', text, re.I)]
    hits += [('the unsupported sentence asserted', s[:80]) for s in R40.q1_asserts(text)]
    return hits


def draft_meta(*a):
    """data/b644_draft_meta.json: the held draft's metadata read once through the route (b639's http: the token in the Authorization header
    alone, the act's User-Agent), its description's length and digest in place of its text, its file list with the service's digests."""
    import hashlib
    import b639_record as R39
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    j = json.loads(b.decode('utf-8')) if st == 200 else {}
    md = dict(j.get('metadata') or {})
    desc = md.pop('description', '') or ''
    put_json('b644_draft_meta.json', dict(at=utc(), status=st, state=j.get('state'), submitted=j.get('submitted'), creators=md.get('creators'),
                                          metadata=md, description_bytes=len(desc.encode('utf-8')),
                                          description_sha256=hashlib.sha256(desc.encode('utf-8')).hexdigest(),
                                          files=[dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in j.get('files') or []]))
    print('  status %s ; state %s ; submitted %s ; files %d ; creators %s' % (st, j.get('state'), j.get('submitted'), len(j.get('files') or []),
                                                                            [c.get('name') for c in md.get('creators') or []]))


PART_HEADS = ('THE CLAIM.', 'WHAT IS MACHINE-VERIFIED.', 'WHAT THE LOAD-BEARING THEOREMS ASSUME.', 'WHAT IS OPEN.', 'HOW A DEFECT IS REPORTED.')


def describe(*a):
    """data/b644_deposit_description.txt (the HTML the draft takes) and .json: composed, the forbidden-content test run over it, the five parts in
    the ruled order and nothing else checked, every NOT READ / NOT BANKED read printed; refuses to write on any hit."""
    import hashlib
    html = compose()
    ps = re.findall(r'<p>(.*?)</p>', html, re.S)
    heads = [p.split(' ', 1)[0] for p in ps]
    order_ok = len(ps) == len(PART_HEADS) and all(p.startswith(h) for p, h in zip(ps, PART_HEADS))
    hits = forbidden(html)
    unread = [m.group(0) for m in re.finditer(r'NOT READ|NOT BANKED|not in the table|None', html)]
    print('  parts %d, in the ruled order %s ; forbidden hits %d ; unread %d ; bytes %d' % (len(ps), order_ok, len(hits), len(unread),
                                                                                         len(html.encode('utf-8'))))
    for h in hits + [('unread', u) for u in unread]:
        print('    ### %s : %s' % h)
    if DRY:
        _write(os.path.join(SP, 'b644_deposit_description_dry.txt'), html.encode('utf-8'))
        return
    if hits or unread or not order_ok:
        sys.exit('### A FORBIDDEN CONTENT, AN UNREAD FIGURE OR THE PARTS OUT OF ORDER -- NOTHING WRITTEN')
    b = html.encode('utf-8')
    _write(os.path.join(D, 'b644_deposit_description.txt'), b)
    put_json('b644_deposit_description.json', dict(at=utc(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), parts=[p[:60] for p in ps],
                                                   order_ok=order_ok, forbidden=hits))
    print('  written: data/b644_deposit_description.txt %d bytes, sha256 %s' % (len(b), hashlib.sha256(b).hexdigest()[:16]))


def desc_test(*a):
    """data/b644_desc_test.txt: the forbidden-content test, by planted text -- one plant per forbidden kind (expected: a hit of that kind), the
    ceiling's denial planted (expected: no hit), and the composed description (expected: no hit) -- each case counted."""
    cases = [('an act number', '<p>composed at b643.</p>', 'an act number'),
             ('a bank path', '<p>read from data/b643_premise_table.json.</p>', 'a bank path'),
             ('root arithmetic', '<p>root e583d138ea28f97569fe859a5826996bda1cebe83fac102cf9821b6a1b2c3d4.</p>', 'root arithmetic'),
             ('a provenance count', '<p>the rows are 209 cell and 1707 rule.</p>', 'a provenance count'),
             ('an outside collection', '<p>read beside %s.</p>' % (OUTSIDE_NEEDLES[0] if OUTSIDE_NEEDLES else 'X'), 'an outside collection'),
             ('a banned stem', '<p>a ' + 'ga' + 'p remains.</p>', 'a banned stem'),
             ('the unsupported sentence asserted', '<p>The programme shows that RH is proved.</p>', 'the unsupported sentence asserted'),
             ('the ceiling denied (no hit)', '<p>Not supported: that RH is proved; the corpus does not claim it.</p>', None),
             ('the composed description (no hit)', compose(), None)]
    L = ['b644 -- COMPONENT 5: THE DESCRIPTION`S FORBIDDEN-CONTENT TEST, BY PLANTED TEXT (%s)' % utc(), '']
    n = 0
    for i, (label, text, want) in enumerate(cases, 1):
        hits = forbidden(text)
        ok = (any(k == want for k, _m in hits) if want else not hits)
        n += ok
        L.append('  (%d) %-40s hits %s ; %s' % (i, label, [k for k, _m in hits][:4], 'PASS' if ok else '### FAIL'))
    L += ['', '### ### **%d of %d cases as wanted -- %s**' % (n, len(cases), 'PASS' if n == len(cases) else 'FAIL')]
    put_txt('b644_desc_test.txt', L)
    print(NL.join(L[2:]))


B640_MAP = [('THE RECORD.', None, 'the record`s own paragraph: its version, its file changes and its order of parts -- dropped (not one of the five)'),
            ('WHAT IS CLAIMED.', '(i)', 'the claim'), ('The programme\'s README', '(i)', 'the register sentence and its further sentences'),
            ('Not supportable', '(i)', 'the ceiling'), ('WHAT IS MACHINE-VERIFIED.', '(ii)', 'the named theorems'),
            ('WHAT THE KERNELS ASSUME.', '(iii)', 'the premises; its provenance counts dropped'), ('WHAT REMAINS OPEN.', '(iv)', 'what is open'),
            ('THE CENSUS, THE ROOT CHAIN', None, 'bank paths and root arithmetic -- dropped'), ('THE FILES', None, 'the file list -- dropped'),
            ('DEFINITIONS', None, 'the glossary block -- dropped; its definitions read inline where a part uses them'),
            ('THIS DESCRIPTION', None, 'the composition line with act numbers and bank paths -- dropped')]


def desc_diff(*a):
    """data/b644_desc_diff.txt: b640's held text against b644's, by part -- each of b640's paragraphs mapped to the part that carries it or
    marked dropped, with sizes; each of b644's five parts with its size."""
    old = re.findall(r'<p>(.*?)</p>', rd('b640_deposit_description.txt'), re.S)
    new = re.findall(r'<p>(.*?)</p>', rd('b644_deposit_description.txt'), re.S)
    L = ['b644 -- COMPONENT 5: THE DESCRIPTION RE-CUT AS SYNTHESIS -- b640`S HELD TEXT AGAINST b644`S, BY PART (%s)' % utc(), '',
         '### b640 (relay data/b640_deposit_description.txt, %d bytes, %d paragraphs):' % (len(rd('b640_deposit_description.txt').encode('utf-8')), len(old))]
    for p in old:
        m = next((x for x in B640_MAP if p.startswith(x[0])), None)
        L.append('  %-28s %6d bytes -> %s' % (p[:28], len(p.encode('utf-8')), ('part %s, %s' % (m[1], m[2])) if m and m[1] else (m[2] if m else '### UNMAPPED')))
    L += ['', '### b644 (relay data/b644_deposit_description.txt, %d bytes, %d parts):' % (len(rd('b644_deposit_description.txt').encode('utf-8')), len(new))]
    L += ['  %-44s %6d bytes' % (p[:44], len(p.encode('utf-8'))) for p in new]
    L += ['', '### ### **b640 PARAGRAPHS %d -> b644 PARTS %d ; DROPPED %d.**' % (
        len(old), len(new), sum(1 for p in old if not (next((x for x in B640_MAP if p.startswith(x[0])), (0, 0))[1])))]
    put_txt('b644_desc_diff.txt', L)
    print(NL.join(L[2:]))


PATH_FROM, PATH_KERNEL = 'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDE-explicit-formula'


def _clause_path():
    """(closure, [(head, status, n users, sample)]): every declaration h2_sign_iff_rh uses, transitively, in the dependency print (b643's,
    the consumers' source), and every premise head any of them consumes, with its status."""
    import b643_record as R43
    K_ = R43._deps_load()[PATH_KERNEL]
    seen, st = set(), [PATH_FROM]
    while st:
        x = st.pop()
        if x in seen or x not in K_:
            continue
        seen.add(x)
        st += [y for y in (K_[x]['T'] | K_[x]['V']) if y in K_]
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    RC = _reconcile()
    out = []
    for v in jl('b642_premise_status.json').get('heads') or []:
        if PATH_KERNEL not in v['kernels']:
            continue
        H = R43._head_names(PATH_KERNEL, v['head'], v.get('decl'), K_)
        users = sorted(n for n in seen if n in H or (K_[n]['T'] | K_[n]['V']) & H)
        if users:
            out.append((v['head'], RC.get(v['head'], (PT[v['head']]['status'],))[0], len(users), users[:3]))
    return seen, out, K_


def clause_path(*a):
    """data/b644_clause_path.txt: the author's word before the seal -- every premise consumed by any declaration on the dependency path from
    h2_sign to RiemannHypothesis (the closure of h2_sign_iff_rh, through the seam), with its status; the seam's own declarations printed."""
    seen, out, K_ = _clause_path()
    seam = sorted(n for n in seen if re.search(r'rh_strip|ZetaSeam|zetaSeam|h2_sign', n))
    L = ['b644 -- THE CLAUSE`S PATH: EVERY PREMISE ON THE DEPENDENCY PATH FROM h2_sign TO RiemannHypothesis, WITH ITS STATUS (%s)' % utc(), '',
         '### the path: the closure of %s in %s`s dependency print (relay data/b643_deps_runs.json, the consumers` source), %d declarations' % (
             PATH_FROM, PATH_KERNEL, len(seen)),
         '### the seam and the clause on it: %s' % ', '.join('%s (%s)' % (n.split('.')[-1], K_[n]['kind']) for n in seam), '',
         '### THE PREMISES CONSUMED ON THE PATH (%d):' % len(out)]
    L += ['  %-22s %-24s used by %3d declarations of the path, e.g. %s' % (h, s, n, ', '.join(x.split('.')[-1] for x in smp)) for h, s, n, smp in out]
    opn = [h for h, s, _n, _s in out if s == 'OPEN']
    L += ['', '### ### **PREMISES ON THE PATH %d ; OPEN %d %s ; DOMAIN %d ; DISCHARGED %d ; WITNESSED %d ; CITED %d.** %s' % (
        len(out), len(opn), opn or '', sum(s == 'DOMAIN' for _h, s, _n, _s in out), sum(s == 'DISCHARGED' for _h, s, _n, _s in out),
        sum(s == 'WITNESSED' for _h, s, _n, _s in out), sum(s == 'CITED' for _h, s, _n, _s in out),
        'No OPEN premise on the path: h2_sign is the one open clause of the reduction.' if not opn else
        'AN OPEN PREMISE ON THE PATH: the register sentence names it, and the finding is the act`s.')]
    put_txt('b644_clause_path.txt', L)
    print(NL.join(L[3:4] + L[-1:]))


INV_TOKEN = re.compile(r"v\d+(?:\.\d+)+|\b[0-9a-f]{7}\b|\d+(?:[.,]\d+)*|\b(?:OPEN|CITED|DISCHARGED|WITNESSED|DOMAIN|REFUTED-BY-COMPUTATION|DERIVES|"
                       r"INTERFACES|PREDICATE-UNLISTED|HINGE)\b|\b[\w']*_[\w']+\b|\b[A-Z][a-z]+[A-Z][\w']*\b")


def invariance(old, new):
    """(lost, added): the change-invariance check -- every figure, name, status and grade token of the old text must survive in the new one
    (counted as a multiset); the new tokens are printed for the reader."""
    a = collections.Counter(INV_TOKEN.findall(re.sub(r'<[^>]+>', ' ', old)))
    b = collections.Counter(INV_TOKEN.findall(re.sub(r'<[^>]+>', ' ', new)))
    return dict((k, a[k] - b[k]) for k in a if a[k] > b[k]), dict((k, b[k] - a[k]) for k in b if b[k] > a[k])


def describe_repair(name, *a):
    """one passage's rewrite, the author's word before the seal: the description recomposed; the change-invariance check against the description
    as it stood (data/b644_deposit_description.txt at HEAD) and its planted failure (one figure changed in a copy: must be caught); the forbidden
    test; written with data/b644_desc_repairs.json (one entry per passage) only when both checks hold."""
    import hashlib
    import subprocess
    old = subprocess.run(['git', '-C', RELAY, 'show', 'HEAD:data/b644_deposit_description.txt'], capture_output=True).stdout.decode('utf-8')
    new = compose()
    lost, added = invariance(old, new)
    planted = new.replace('v0.26', 'v0.25', 1)
    p_lost, _p = invariance(old, planted)
    hits = forbidden(new)
    ok = not lost and bool(p_lost) and not hits
    print('  %s : lost %s ; added %s ; the planted failure caught %s (%s) ; forbidden %d ; %s' % (
        name, lost or 'none', added or 'none', bool(p_lost), p_lost, len(hits), 'WRITTEN' if ok and not DRY else 'NOT WRITTEN'))
    if not ok or DRY:
        return
    _write(os.path.join(D, 'b644_deposit_description.txt'), new.encode('utf-8'))
    R = jl('b644_desc_repairs.json') or dict(repairs=[])
    R['repairs'].append(dict(passage=name, at=utc(), lost=lost, added=added, planted_caught=p_lost, bytes=len(new.encode('utf-8')),
                             sha256=hashlib.sha256(new.encode('utf-8')).hexdigest()))
    put_json('b644_desc_repairs.json', R)


# ================================================================================ THE SECOND READER, TWICE: (R254)(4) AND (8)
# ### b643's form: a packet staged off D:\ in a directory with no project memory, a lead and the full prompt, the command the reader is run by
# ### (the author runs it: a headless reader launched from this session is refused by the classifier, b620); the answers scored by needles and
# ### by hand (data/b644_reader*_handread.txt, the seat's, written before the needles are read).
READERS = {
    'a': dict(dir='C:/reader_b644a', doc='census.txt', what='a census of the programme`s premises',
              questions=('What is a hinge, and which premises are hinges?',)),
    'd': dict(dir='C:/reader_b644', doc='description.txt', what='the description of a research deposit',
              questions=('What is claimed?', 'What is not claimed?', 'Which premise is refuted, and what replaced it?')),
}
# ### the re-runs the author ordered before the seal, on the repaired texts, each in a fresh directory (nothing deleted under C:\)
READERS['a2'] = dict(READERS['a'], dir='C:/reader_b644a2')
READERS['d2'] = dict(READERS['d'], dir='C:/reader_b644_2')


def _reader_lead(k):
    r = READERS[k]
    return ('Reader task follows. The packet is at %s\\packet\\ and your answers go to %s\\answers.txt. Read only the two packet files. Do not open '
            'any other file on this machine, do not run any command, and do not search the web. Write the answers file, report that it is '
            'written, and stop.' % (r['dir'].replace('/', '\\'), r['dir'].replace('/', '\\')))


def _reader_task(k):
    r = READERS[k]
    n = len(r['questions'])
    heads = ', '.join('ANSWER %d:' % i for i in range(1, n + 1))
    return (_reader_lead(k) + NL + NL +
            'You are an independent reader. You know nothing of the research programme the packet describes, and that is the point. The packet has '
            'two files: %s, %s, and questions.txt, %s. Read the document and answer each question in your own words, from the document alone, in '
            'a few sentences each: say what the text says, not what you know of the mathematics, and say plainly where the text is unclear to '
            'you. Write the file %s\\answers.txt with %s, each followed by your answer to that question; then a section headed UNCLEAR: listing '
            'any sentence of the document you could not follow, or the word none. Then stop.' % (
                r['doc'], r['what'], 'one question' if n == 1 else '%d questions' % n, r['dir'].replace('/', '\\'),
                ('one section headed ANSWER 1:' if n == 1 else 'exactly %d sections, headed %s' % (n, heads))))


def _reader_cmd(k):
    d = READERS[k]['dir'].replace('/', '\\')
    return ('Get-Content %s\\full_prompt.txt -Raw | claude -p --output-format json --allowedTools Read Glob Write --disallowedTools Bash PowerShell '
            'WebFetch WebSearch --permission-mode acceptEdits --setting-sources user --strict-mcp-config > %s\\reader_run.log 2> '
            '%s\\reader_run.err' % (d, d, d))


def reader_packet(k, *a):
    """the packet `k` (a: the census v0.7.1 and the hinge question; d: the description and the three questions) staged off D:\\ and banked
    (data/b644_reader_<k>_packet/, data/b644_reader_<k>_packet.txt with the command)."""
    import b616_record as R6
    r = READERS[k]
    if k.startswith('a'):
        doc = io.open(os.path.join(PP, *K.CEN71.split('/')), encoding='utf-8').read().replace(chr(13), '')
    else:
        html = rd('b644_deposit_description.txt')
        doc = NL.join(re.sub(r'<[^>]+>', '', p).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&') for p in re.findall(r'<p>(.*?)</p>', html, re.S))
    if not doc.strip():
        sys.exit('### THE DOCUMENT IS EMPTY -- NOTHING WRITTEN')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(r['questions']))
    task = _reader_task(k)
    nd = R6.nd_hits(doc + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in OUTSIDE_NEEDLES if n in doc]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b644_reader_%s_packet' % k)
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in ((r['doc'], doc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    if not DRY:
        if os.path.exists(r['dir']) and os.listdir(r['dir']):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- NOT WRITTEN' % r['dir'])
        os.makedirs(r['dir'] + '/packet', exist_ok=True)
        for n_, t_ in (('packet/' + r['doc'], doc), ('packet/questions.txt', qs), ('lead.txt', _reader_lead(k)), ('full_prompt.txt', task)):
            _write(os.path.join(r['dir'], n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    L = ['b644 -- THE SECOND READER`S PACKET %s, STAGED OFF D:\\ (%s)' % (k.upper(), utc()), '',
         '### staged: %s (packet/%s %d bytes, sha256 %s ; packet/questions.txt ; lead.txt ; full_prompt.txt) ; banked: relay data/b644_reader_%s_packet/' % (
             r['dir'], r['doc'], len(doc.encode('utf-8')), sha(doc.encode('utf-8')), k),
         '### the questions: %s' % ' / '.join(r['questions']), '### the no-disclosure arm: %s ; outside names: %s' % (dict(nd), outside or 'NONE'),
         '', '### the command, run by the author from %s, a directory with no project memory:' % r['dir'], '    ' + _reader_cmd(k)]
    put_txt('b644_reader_%s_packet.txt' % k, L)
    print(NL.join(L[-5:]))


def _needles(k):
    import b640_record as R40
    if k.startswith('a'):
        hn = [r['head'] for r in jl('b644_hinges.json').get('rows') or [] if r.get('hinge')]
        return {1: (r'more than one (kernel|chain)|across (kernels|chains|more than one)|several (kernels|chains)', 'what a hinge is',
                    r'\b(%s)\b' % '|'.join(re.escape(h) for h in hn), 'names a hinge of the refined list', None)}
    return {1: (r'located clause|single (located )?clause|reduc', 'the claim: the reduction to the located clause', None, None, None),
            2: (r'not (supported|claimed)|does not (claim|state|support)|unsupported|not proved|open', 'what is not claimed: RH proved, h2_sign open',
                None, None, R40.q1_asserts),
            3: (r'TrivialSummandPremise\b', 'the refuted premise named', r"TrivialSummandPremise'|pole term|restat", 'what replaced it', None)}


def reader_score(k, *a):
    """data/b644_reader_<k>_compare.txt and .json: the reader's answers copied from off D:\\, each scored by its needles and beside it the seat's
    hand reading (data/b644_reader_<k>_handread.txt), both figures; question 2 of `d` refuses an assertion of the unsupported sentence."""
    r = READERS[k]
    src = os.path.join(r['dir'], 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b644_reader_%s_answers.txt' % k), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in re.finditer(r'^ANSWER (\d):\s*(.*?)(?=^ANSWER \d:|^UNCLEAR:|\Z)', t, re.M | re.S))
    N = _needles(k)
    lg = os.path.join(r['dir'], 'reader_run.log')
    mem = ('memory named in the run log: %s' % bool(re.search(r'MEMORY\.md|[\\/]memory[\\/]', io.open(lg, encoding='utf-8', errors='replace').read()))
           if os.path.exists(lg) else 'the run log absent')
    hand = dict((int(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^HAND (\d): (AGREE|DIFFER)', rd('b644_reader_%s_handread.txt' % k), re.M))
    L = ['b644 -- THE SECOND READER %s: ANSWERS SCORED BY THE NEEDLES AND BY HAND (%s)' % (k.upper(), utc()), '',
         '### the answers: relay data/b644_reader_%s_answers.txt, copied from %s ; the reader`s session: %s' % (k, src, mem), '']
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
    L += ['### NOTE, beside the score: %s' % n_ for n_ in re.findall(r'^NOTE: (.*)$', rd('b644_reader_%s_handread.txt' % k), re.M)]
    L += ['### UNCLEAR, the reader`s: %s' % (' '.join(unclear.group(1).split())[:1500] if unclear else '### NONE GIVEN'), '',
          '### ### **BY THE NEEDLES %d OF %d ; BY HAND %s OF %d.**' % (n_ok, len(N), kh if hand else '### NOT READ', len(N))]
    put_txt('b644_reader_%s_compare.txt' % k, L)
    put_json('b644_reader_%s_compare.json' % k, dict(at=utc(), answers=res, needles=n_ok, hand=kh if hand else None, of=len(N),
                                                      unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ================================================================================ COMPONENT 7: W-ORD-H2-LATTICE, A BANK, (R254)(10)
# ### The rows: every graded row of SIDE-explicit-formula in the terminal table at relay HEAD whose statement names the clause or a predicate
# ### of RH's family (CLAUSE_RE) -- the squeeze's cells (OPEN_TRAILS :13529); the seat's scope, printed with its count. The rule assigns each
# ### row to the axes its name and its statement's binders and predicates read, by AXES below (a row may sit on several axes); a row no axis
# ### reads is UNPLACED and raised as one prompt. Each cell prints its grade (the table's) and its status (the statuses of the premises it
# ### rests on, b643's premise table; none when it rests on none). Not an edition: the author reads the bank before it enters any census.
CLAUSE_RE = r'RiemannHypothesis|\bh2_sign\w*|\brh_\w+|GRH\w*|li_nonneg\w*|arith_limit\w*|NymanBeurling\w*|conservationHypothesis'
AXES = [('HEIGHT', r'upto|height|Platt|L₀|\(T\s*:|\bT₀\b|\|\s*\w+\.im\s*\||\.im\b'),
        ('INSTANCE', r'_chi\b|χ|Dirichlet|LFunction|Dedekind|dedekind|Epstein|epstein|_cfg\b|Config\b|instance'),
        ('REGISTER', r'h2_sign|Weil|weil|\bli_|LiCriterion|LiCoeff|Register\d|taylorCoeff|\bnb\b|_nb\b|NymanBeurling|conservation|\bch_|arith_limit'),
        ('FAMILY', r'GRH|Family\.|family|cascade'),
        ('TEST-CLASS', r'classK|window|Window|plateau|\bbox\b|test')]


def lattice_axes(name, statement):
    """[(axis, the token that placed it)] for one row."""
    text = '%s %s' % (name, statement)
    out = []
    for ax, rx in AXES:
        m = re.search(rx, text)
        if m:
            out.append((ax, m.group(0)))
    return out


PLANTED = [('HEIGHT', 'X.forall_rh_upto_iff_rh', 'theorem forall_rh_upto_iff_rh : (∀ T : ℝ, rh_upto T) ↔ RiemannHypothesis'),
           ('INSTANCE', 'X.GRH_chi', 'theorem GRH_chi (χ : DirichletCharacter ℂ q) : GRH χ'),
           ('REGISTER', 'X.li_nonneg_iff_rh', 'theorem li_nonneg_iff_rh : (∀ n, 0 ≤ li n) ↔ RiemannHypothesis'),
           ('FAMILY', 'X.Family.grh_family', 'theorem grh_family : GRH_family F'),
           ('TEST-CLASS', 'X.h_classK', 'theorem h (k : ℝ → ℝ) (hk : k ∈ classK) : 0 ≤ P k'),
           (None, 'X.rh_base', 'theorem rh_base : RiemannHypothesis ↔ ∀ s, Z s → s.re = 1 / 2')]


def lattice(*a):
    """data/b644_lattice.txt and .json: the rule's planted test (one row per axis and one no axis reads), the lattice table (row, axes, grade,
    status), the unplaced rows. Writes nothing beyond its two banks."""
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    L = ['b644 -- COMPONENT 7, (R254)(10): W-ORD-H2-LATTICE -- THE ASSIGNMENT RULE, ITS TEST, THE LATTICE TABLE (%s) -- A BANK, NOT AN EDITION' % utc(), '',
         '### the axes and the token each reads (name and statement): %s' % ' ; '.join('%s `%s`' % (a_, r_) for a_, r_ in AXES),
         '### the rows: SIDE-explicit-formula`s graded rows in the terminal table at relay HEAD whose statement matches `%s` (the seat`s scope)' % CLAUSE_RE,
         '', '### THE RULE`S TEST, PLANTED ROWS:']
    n = 0
    for i, (want, nm, st) in enumerate(PLANTED, 1):
        got = [a_ for a_, _t in lattice_axes(nm, st)]
        ok = (want in got) if want else not got
        n += ok
        L.append('  (%d) %-12s %-26s axes read %s ; %s' % (i, want or 'NO AXIS', nm, got or 'none', 'PASS' if ok else '### FAIL'))
    L += ['  ### ### **%d of %d cases as wanted -- %s**' % (n, len(PLANTED), 'PASS' if n == len(PLANTED) else 'FAIL'), '']
    T = jl('terminal_table.json')
    rows = [r for r in T.get('rows') or [] if r['repo'] == 'SIDE-explicit-formula' and r['grade'] not in ('UNGRADED', None)
            and re.search(CLAUSE_RE, r.get('statement') or '')]
    out, unplaced = [], []
    for r in rows:
        ax = lattice_axes(r['name'], r.get('statement') or '')
        on = _rests_on(r['name'].split('.')[-1])
        st = ', '.join('%s %s' % (h, PT[h]['status']) for h in on if h in PT) or 'none'
        out.append(dict(name=r['name'], axes=ax, grade=r['grade'], status=st))
        if not ax:
            unplaced.append(r)
    cnt = collections.Counter(a_ for x in out for a_, _t in x['axes'])
    L.append('### THE LATTICE TABLE (%d rows): row | axes (the token) | grade | the premises it rests on, with status' % len(out))
    L += ['  %-58s | %-46s | %-18s | %s' % (x['name'][-58:], ', '.join('%s (%s)' % t for t in x['axes']) or 'UNPLACED', x['grade'], x['status'])
          for x in sorted(out, key=lambda x: ([a_ for a_, _t in x['axes']] or ['~'], x['name']))]
    L += ['', '### TOP (%d) -- the author`s answer at b644 to the prompt that raised these rows, the rule placing none of them: "the lattice`s top '
          '-- the base statement (RH in strip form, the seam, and the cell form) that every cell is a restriction of"; no axis is added, and the '
          'table above reads five axes beneath it.' % len(unplaced)]
    L += ['  %s : %s' % (r['name'], ' '.join((r.get('statement') or '').split())[:200]) for r in unplaced]
    L += ['', '### ### **ROWS %d ; PLACED ON THE FIVE AXES %d ; TOP %d ; ON EACH AXIS: %s ; THE RULE`S TEST %d OF %d.**' % (
        len(out), len(out) - len(unplaced), len(unplaced), ', '.join('%s %d' % (a_, cnt[a_]) for a_, _r in AXES), n, len(PLANTED))]
    put_txt('b644_lattice.txt', L)
    put_json('b644_lattice.json', dict(at=utc(), test=[n, len(PLANTED)], rows=out, unplaced=[r['name'] for r in unplaced]))
    print(NL.join(L[-1:]))


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b644_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
