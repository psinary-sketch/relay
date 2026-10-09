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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b644_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
