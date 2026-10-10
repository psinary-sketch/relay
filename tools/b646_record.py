# -*- coding: utf-8 -*-
"""b646_record.py -- THE ACT'S RECORD TOOL, UNDER (R256). ### ONE SUBCOMMAND PER BANK.

### ### b646: LANE THREE, ACT SEVENTY-THREE -- THE EDIT-ROUTE ARM; THE SEVEN COMPANIONS THROUGH THE INTAKE FORM; THE MONOGRAPH'S AGENDA
### TO THE AUTHOR; THE DEPOSIT DESCRIPTION AT v3 UNDER COMPOSITION RULES, THE MET LIST WIDENED, dedekind_rhs' RE-GRADED, A FOURTH READER,
### THE DRAFT HELD; THE SEAT'S MEMORY THROUGH THE TABLE; THE CROSS-FIELD RESONANCES ENTRY. Subcommands write only `data/b646_*` unless
### the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers are b602's, b633's and b641's record
### tools', imported; ledger appends through b566's guarded `append_to`. Written by the Write tool, edited through the Edit tool only.
### Every bank is written LF.
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
import b646_worklist as K  # noqa: E402
import edit_route as ER  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, DATE = K.PRE_PP, K.PRE_RELAY, K.DATE
SP = K.SP
SESSION_ID = 'f004d01d-ad93-416c-a916-fe6e52403753'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
SESSIONS_AFTER = (('bc5efa87-33bc-483a-b723-ace1d978aa31', 'The fourth reader has run'),)   # ### the act's continuation after a /clear
FACE = 'b646_registration_2026-10-09.txt'
DRY = 'dry' in sys.argv[2:]
R3.DRY = DRY

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
    try:
        return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


def _need(pat, text, what):
    m = re.search(pat, text, re.M | re.S)
    if not m:
        sys.exit('### %s NOT READ (%r) -- NOTHING WRITTEN' % (what, pat[:60]))
    return m


# ================================================================================ THE COMMAND BANK, (R256)(2)
def commands(*a):
    """data/b646_commands.txt and .json: the act's command bank -- every Bash and PowerShell command of the seat's session from the
    ruling's first delivery (K.ANCHOR) onward, and its helper readers' (the subagents' transcripts, entries at or after it) -- each with
    the arm G-EDIT-ROUTE's reading (tools/edit_route.py), each offending command printed."""
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % K.ANCHOR)
    # ### the act continued after a /clear in a second session (b646, the seat's catch): its commands are read from its first user line too
    for sid, anc in SESSIONS_AFTER:
        more = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                          'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    for i, r in enumerate(rows):
        r['n'] = i + 1
    hits = ER.scan(rows)
    L = ['b646 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING ((R256)(2); tools/edit_route.py) (%s)' % utc(), '',
         '### the source: the seat`s session transcript %s from its first user line carrying %r, and its subagents` transcripts (%s) at or '
         'after that line`s timestamp %s' % (os.path.basename(SESSION), K.ANCHOR, SUBAGENTS.rsplit('/', 2)[-2] + '/subagents', rows[0]['ts']),
         '### commands read: %d (seat %d ; helper readers %d) ; by tool %s' % (
             len(rows), sum(1 for r in rows if r['src'].startswith('seat')), sum(1 for r in rows if not r['src'].startswith('seat')),
             dict(collections.Counter(r['tool'] for r in rows))), '']
    L += ['### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + \
             ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    for r in rows:
        L.append('  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]))
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d.**' % (len(rows), len(hits))]
    put_txt('b646_commands.txt', L)
    put_json('b646_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits]))
    print(L[-1])


def answers(*a):
    """data/b646_author_answers.txt: every prompt put by the seat in this act -- in the first session from the ruling's first delivery, in the
    continuation sessions (SESSIONS_AFTER) from their first user line -- banked verbatim with the options, the recommended mark and the answer."""
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
    head = ['### b646 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; the sessions read: %s.' % (n, DATE, ', '.join('%s from %r' % (s[:8], an) for s, _, an in srcs)), '']
    put_txt('b646_author_answers.txt', head + (L or ['### NONE: no prompt has been put to the author in this act.']))
    print('  prompts banked: %d' % n)


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R256)(1), (2), (6), (7)
W_HEAD = '*Appended 2026-10-09 by b646 to b645’s entry (:%d), under `(R256)`(1) -- b645 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
WO_HEAD = ('*Appended 2026-10-09 by b646, under `(R256)`(2) and (5) -- W-ORD-EDIT-ROUTE-ARM ENTERED AND ACTED; W-ORD-SEAT-BELIEFS '
           'ENTERED AND ACTED:*')
XR_HEAD = ('*Appended 2026-10-09 by b646, under `(R256)`(6), the author’s word by that clause and strikeable -- CROSS-FIELD RESONANCES, A '
           'RESEARCH-ARC ENTRY OPENED, in the research-arc line’s form (:%d):*')
OS_HEAD = '*Appended 2026-10-09 by b646 to b645’s outsiders’ line (FINDINGS :%d), under `(R256)`(7) -- THE OUTSIDERS AS b645 READ THEM:*'


def _b645_figures():
    c = rd('b645_closing.txt')
    head = _need(r'^b645 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts answered; (\d+) defects', c,
                 'b645`s closing head line')
    tabs = {}
    for k, pat in (('seam', r'the seam rows \((\d+)\)\s+MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)'),
                   ('map', r'the load-bearing map \((\d+)\) MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)'),
                   ('doc', r'the docstrings \((\d+)\)\s+MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)'),
                   ('mono', r'the monograph \((\d+)\)\s+MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')):
        tabs[k] = [int(x) for x in _need(pat, c, 'b645`s %s counts' % k).groups()]
    ag = _need(r'### ### \*\*ROWS (\d+) ; CHAPTERS (\d+)\.\*\*', rd(K.AGENDA), 'the agenda`s rows')
    hold = [r for r in (jl('b645_build_watch.json').get('rows') or [])]
    pre = [r for r in hold if r.get('log', '').endswith('_preseal.log')]
    closing = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b645 closing', PRE_RELAY).strip()[:8]
    act = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b645 --', PRE_RELAY).strip()[:8]
    seal = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b645 seal', PRE_RELAY).strip()[:8]
    d = rd('b645_defects.txt')
    nd = len(re.findall(r'^    \([a-z]\) ', d, re.M))
    tests = jl('b645_tests_stepzero.json')
    return dict(head=head, tabs=tabs, agenda=ag, pre=pre, closing=closing, act=act, seal=seal, ndef=nd,
                b638=tests.get('test_chain_page_b638.py', {}).get('failing'))


def _weight():
    f = _b645_figures()
    h, t = f['head'], f['tabs']
    if t['mono'][1:] != [1834, 37, 154, 63] or t['map'][1:] != [371, 4, 12, 1] or t['doc'][1:] != [1366, 3, 0, 0] or t['seam'][1:] != [0, 2, 0, 0]:
        sys.exit('### b645`S BANKS DO NOT READ THE RULING`S FIGURES %s -- NOTHING WRITTEN' % t)
    lows = ', '.join('%s at lows %s MB' % (r['module'].split('/')[-1].replace('.build', ''), ' and '.join(str(x) for x in r['lows'])) for r in f['pre'])
    b638 = f['b638'] or []
    cases = '%s-%s' % (b638[0], b638[-1]) if b638 else ''
    return ('\n%s relay %s (closing), %s (act), %s (seal), PLACE-papers %s; the suite %s of %s; the root %s…; %s prompts answered; %d defects, '
            '(a) to (k), two of them b644`s repeated -- a stream edit of an unsealed tool against the Edit-tool rule (b), a delete on a relative '
            'path (c). The instrument tools/licensed_table.py, five cells and four verdicts, one planted case per verdict and one for a HAND row '
            'without its citation. The seam rows %d of %d UNDERSTATES; THE_LOAD_BEARING_MAP %d rows -- MATCHES %d, UNDERSTATES %d, OVERREACHES '
            '%d, UNLICENSED %d; SIDE-explicit-formula`s docstrings at 82550e4, %d rows -- MATCHES %d, UNDERSTATES %d (Props labelled not proved '
            'that Seam.lean proves); A_Place_to_Stand_v5_18, %d claims -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d, under the '
            'seat`s printed rule for `established` after its brief read the word too widely (d), and with the brief`s F5 naming the conditional '
            'one of two same-named theorems (e). v6.0`s agenda, %s rows over %s chapters (relay data/%s), the re-cut`s agenda, sent to the '
            'author as a file. The hold retried before the seal: %s, RUN-BENEATH-HOLD final, named. N1-N4 held; N5 refuted in one clause by '
            'the ferry`s own wording (the banks step zero ordered are banks beyond the five tables); S2 refuted (test_chain_page_b638 carried, '
            'cases %s; the reader`s test beneath the hold). The census`s three columns defined and applied to the two keystones reached; the '
            'outsiders read by the default rule. Nothing deposited; no edition touched; the draft held.\n' % (
                W_HEAD % K.B645_ENTRY, f['closing'], f['act'], f['seal'], h.group(2), h.group(3), h.group(4), h.group(5)[:8], h.group(6),
                f['ndef'], t['seam'][2], t['seam'][0], t['map'][0], t['map'][1], t['map'][2], t['map'][3], t['map'][4], t['doc'][0],
                t['doc'][1], t['doc'][2], t['mono'][0], t['mono'][1], t['mono'][2], t['mono'][3], t['mono'][4], f['agenda'].group(1),
                f['agenda'].group(2), K.AGENDA, lows, cases))


def _workorders():
    arm = g(RELAY, 'log', '--format=%h', '-1', K.ARM_COMMIT).strip()[:8]
    return ('\n%s W-ORD-EDIT-ROUTE-ARM, named by `(R256)`(2) after b644`s defect (a) and b645`s (b) and (c), is acted at b646`s step zero '
            '(relay %s, committed alone): tools/edit_route.py reads the act`s command bank -- the shell commands the record tool captures from '
            'the seat`s session and its helper readers’ sessions -- and reads any sed -i, any heredoc or redirect writing under tools/, and any rm or '
            'Remove-Item whose path is not absolute, or a branch deletion whose operand is not an explicit name, as a failure of the arm '
            'G-EDIT-ROUTE, each offending command printed; its planted test tools/test_edit_route_b646.py plants a command of each kind beside '
            'the house forms. Trigger: the arm itself, in the suite of every act from b646. W-ORD-SEAT-BELIEFS, opened by `(R256)`(5), is acted '
            'at b646`s Component 5: the seat`s project-state memory files read through the licensed-statement table as a document, every '
            'sentence stating a fact about the corpus a row, HAND with the lines read, each UNDERSTATES or OVERREACHES row repaired in its file '
            'with the repair printed (relay data/b646_table_seat_memory.txt); the navigator`s standing memory follows at b647, exported by the '
            'navigator as a file.\n' % (WO_HEAD, arm))


XR_QUESTIONS = [
    ('the closure lattice, read as a question before it was a bank',
     'If the lattice of relay data/b644_lattice.txt were not yet written, which of its closures would the corpus ask for first, and does '
     'the order of asking match the order in which they were banked?',
     'one closure is named whose question can be printed from the banks alone and checked against the lattice`s own row'),
    ('topology read at a critical point where the bulk spectrum closes, against the transversality jaw',
     'Does an invariant read at the point where a spectrum closes, as condensed-matter physics reads one at a transition, say anything '
     'about the line that the transversality jaw of THE_UNCONDITIONAL_SURROUND section 6a does not already say?',
     'a named invariant is written as a definition over a compiled object of the corpus and its value at the line is a statement a gate '
     'can grade'),
    ('amplification of a small bias through a catalytic chain, against the ferry-and-ledger route',
     'Can a bias too small to read at one step be carried through a chain of steps that each multiply it, as a catalytic chain does, and '
     'how does such a chain compare with the ferry-and-ledger route`s own way of accumulating small corrections act by act?',
     'a chain is named whose steps are compiled terminals and whose amplification is a statement with a printed bound'),
    ('the squeeze`s close-pair target',
     'What does the geometric face of the open node (THE_UNCONDITIONAL_SURROUND section 6a: uniform control of close zero pairs, '
     'Lehmer-type, at every height) ask of a pair of zeros close together, and which published separation results bear on it?',
     'the target is stated as a Prop over the corpus`s zeros and a premise-table row records its status'),
    ('the Epstein rungs as a formalization contribution',
     'Would the five Epstein rungs priced at b642 (OPEN_TRAILS :13533; relay data/b642_epstein_rungs.txt), offered on their own and apart '
     'from the programme`s claims, be a contribution to a formal library, and what would it take to put them in that library`s form?',
     'the rungs’ declarations are listed with their axiom prints and the target library`s contribution rules are read and banked'),
]


def _resonances():
    L = ['\n%s questions, no claims, each with the sentence naming what would make it a work-order; no question graded. Every tenth act '
         'from b650 is a reading act -- no build, no deposit, no seal -- in which both seats read this entry against the corpus and print '
         'which questions have grown a trigger.\n' % (XR_HEAD % K.RESEARCH_ARC_MODEL)]
    for i, (name, q, wo) in enumerate(XR_QUESTIONS, 1):
        L.append('- **Research-arc line, 2026-10-09 (b646, `(R256)`(6); owner: the author) -- cross-field resonance %d, %s.** %s It becomes a '
                 'work-order when %s.\n' % (i, name, q, wo))
    return NL.join(L)


def _outsiders():
    ro = rd('b645_outsider_roster.txt')
    n = _need(r'STANDS ASIDE (\d+)', rd('b645_closing.txt') + ro, 'the outsiders` count')
    return ('\n%s each of the %s stands as b645 printed its reading under the default rule (relay data/b645_outsider_roster.txt), STANDS ASIDE '
            'by its printed line; the private repository stands aside unnamed; the author`s strike at any closing replaces a reading; the chain '
            'is not widened by the seat.\n' % (OS_HEAD % K.B645_OUTSIDERS, n.group(1)))


def record_lines(*a):
    """Component 1, (R256)(1), (2), (5)-(7): FINDINGS, b645 at its weight (to :8061) and the outsiders as b645 read them (to :8079);
    OPEN_TRAILS, W-ORD-EDIT-ROUTE-ARM and W-ORD-SEAT-BELIEFS entered and acted, and the cross-field resonances research-arc entry."""
    import b641_record as R41
    Q = R2._Q()
    if not Q.line_of(Q.FIND, '## The review pass opened: the licensed-statement table') == K.B645_ENTRY:
        sys.exit('### b645`S ENTRY MOVED -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % K.B645_ENTRY, R41._poss(_weight())), ('FINDINGS.md', OS_HEAD % K.B645_OUTSIDERS, R41._poss(_outsiders())),
             ('OPEN_TRAILS.md', WO_HEAD, R41._poss(_workorders())),
             ('OPEN_TRAILS.md', XR_HEAD % K.RESEARCH_ARC_MODEL, R41._poss(_resonances()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if DRY else D, 'b646_scanfile_lines.md')
    _write(p, allt.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    ticks = [l[:60] for l in allt.split(NL) if l.count('`') % 2]
    # ### a figure not read prints as a bare `?`; a question's own mark follows a word, so only a `?` after a space, a bracket or a
    # ### line's start is read as an unread figure
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
    R3._land(Q, items, 'b646_record_lines.json', K.B645_ENTRY)


# ================================================================================ COMPONENT 2: THE COMPANIONS, (R256)(3)
INTAKE_GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
# ### the re-cut each fact names (b645's RECUT_BY_FACT, F5 re-written for the two theorems of that name, b645's defect (e))
RECUT_BY_FACT = {
    'F1': 'state RH as equivalent to the one open clause h2_sign (h2_sign_iff_rh, Seam.lean :101), not as conditional on it',
    'F2': 'say Route 3 compiles RH from its own restatement (ch_iff_rh, H2Bridge.lean :71): no route and no reduction',
    'F3': 'say conservation_of_spectra states (1 : ℚ)^s = 1; the n₄ = 0 reading is the paper’s argument, not the terminal’s content',
    'F4': 'say h1_complete_at_Phi certifies eight coupling facts at Φ and closes no clause on the strip (mellin_Phi_eq_zero_of_re_le_one)',
    'F5': 'name the terminals for what they state: ConservationBridge’s structural_exhaustiveness_proved takes ConservationHypothesis; '
          'TheBridgeComplete’s states the seven-class count, the per-class exclusion and Ostrowski’s covering, not that every zero is '
          'produced by a named class; spectral_cannon is a fact on the line; none reaches σ = 1/2',
    'F6': 'state partialPositivity_finiteRange with its premises (Bombieri–Lagarias, Voros, VerifiedZerosTo T)',
    'F7': 'state the registers at their depths: R1 false as stated, R2 RH restated, R4 equivalent to RH, R5’s output a theorem',
    'F8': 'name h2_sign and h2_sign_iff_rh as h2’s terminal',
    'F9': 'say the seam is compiled (rh_strip_imp_rh_holds, Seam.lean :84)',
    'F10': 'say the kernel checks the arithmetic 2 + 3 + 2 + 0 = 7; the classification is the paper’s argument',
    'F11': 'say the kernel counts a defined type (Fintype.card MechanismClass = 7); that every zero is produced by a named class '
           '(covers_all) is the open clause, not compiled',
    'F12': 'state silence_universal with its premise I.is_universal',
    'F13': 'say the Lean form is the logical schema (modus tollens over an abstract domain); the Mechanism Theorem’s content is the paper’s argument',
    'F15': 'state GRH for a primitive χ ≠ 1 as equivalent to h2_sign_chi (h2_sign_chi_iff_grh_chi), not as conditional on it',
}
# ### THE STATED-AS RULE, b645's, printed: an argument-, synthesis- or theorem-grade row the reader marked `established` keeps it only where its
# ### quote claims a status beyond argument (STATUS_WORDS) or its reason names a corpus fact it conflicts with (F1-F13, F15); else `graded`.
STATUS_WORDS = re.compile(r'(?i)\b(?:prov(?:ed|es|en|able)|proof|theorem|verif\w*|certif\w*|compil\w*|machine|Lean|kernel|ZFC|established|rigorous\w*|'
                          r'demonstrat\w*|confirm\w*|settled|unconditional\w*|closes?|closed|follows as)\b')
COMP_FIX = {       # ### row id -> (grade, stated_as, reason[, route]): the seat's corrections, each after its whole read of the row
    # ### ONE_PAGE_PROOF, read whole by the seat (:1-:100 at 96779e5)
    'COMP-ONE_PAGE_PROOF-17-13': ('argument-supported', 'graded', 'the seat`s read: the paper`s own argument about its specification '
                                  '(n² → θ → ξ determines ξ), stated as its argument'),
    'COMP-ONE_PAGE_PROOF-33-28': ('statement-grade', 'open', 'the seat`s read: the row marks its own count Definitional -- a definition of '
                                  'the paper`s terms'),
    'COMP-ONE_PAGE_PROOF-38-33': ('argument-supported', 'established', 'the seat`s read: the syllogism`s premise is covers_all, the open clause '
                                  '(F11), stated as a step of the proof'),
    # ### Exhaustive_Enumeration, every non-MATCHES row read whole by the seat
    'COMP-Exhaustive_Enumeration-161-142': ('argument-supported', 'graded', 'the seat`s read: the document cites no kernel, true; that '
                                            'completeness is not settled by a Lean terminal is the corpus`s own reading of the compiled schema (F13)'),
    'COMP-Exhaustive_Enumeration-161-144': ('argument-supported', 'graded', 'the seat`s read: the corpus`s own reading -- the compiled form is '
                                            'logic alone, its Fintype unused (F13); completeness is not what it settles'),
    'COMP-Exhaustive_Enumeration-166-148': ('kernel-verified', 'established', 'the seat`s read: the completeness it describes is Ostrowski`s, '
                                            'the conjunct ostrowski_exhaustive_prime of TheBridgeComplete`s unconditional structural_exhaustiveness_proved '
                                            '(SIDE-kernel v1.5 Bridge/TheBridgeComplete.lean :249), cited at its pin (F5 (ii))'),
    # ### Which_Structure_Confines, every non-MATCHES row read whole by the seat
    'COMP-Which_Structure_Confines-121-126': ('kernel-verified', 'established', 'the seat`s read: the two compiled negatives are the corpus`s '
                                              '(C7_finite_type_false, F14; the per-class-to-combined commutation, machine-checked false, named in '
                                              'the Paths census), cited as negatives'),
    'COMP-Which_Structure_Confines-226-207': ('argument-supported', 'graded', 'the seat`s read: a corpus record, true -- OrbitDictionary.lean '
                                              '7 of 7 at no axioms (FINDINGS F.2026-08-18p, archived at 2026-08-24)'),
    # ### Spectral_Inertness, every non-MATCHES row read whole by the seat; the counts at :59-:63 checked at the pin (SIDE-kernel 0e5233f:
    # ### Kernel/ProductFormula_v2.lean 6, _Clean 11, _Rat 9 theorems -- not 6 + 8 + 8 = 22) and left UNLICENSED; v1.7 resolves to 2957e7d
    'COMP-Spectral_Inertness-63-53': ('argument-supported', 'graded', 'the seat`s read: a record with its citation -- the line gives the '
                                      'repository`s URL, the federation`s public chain repository'),
    'COMP-Spectral_Inertness-179-146': ('kernel-verified', 'graded', 'the seat`s read: 1^s = 1 is what conservation_of_spectra compiles '
                                        '(SIDE-kernel v1.5 Kernel/ProductFormula_Rat.lean :72), stated as the computation (F3)'),
    'COMP-Spectral_Inertness-206-172': ('kernel-verified', 'established', 'the seat`s read: the archimedean complement is '
                                        'real_no_compact_open_addSubgroup (SIDE-global-section Interfaces/LocalLimit.lean :218), compiled'),
    # ### Seven_Mechanism_Classes, every non-MATCHES row read whole by the seat; the file rows checked at SIDE-kernel 0e5233f by git grep
    # ### (no sorry outside comments, no axiom declaration in Kernel/PoissonExhaustion.lean, Kernel/Layer1.lean)
    'COMP-Seven_Mechanism_Classes-129-108': ('argument-supported', 'established', 'the seat`s read: the distributive interface`s inertness is '
                                             'the inter-class conservation step, a register of the one open clause (F7), stated as fact'),
    'COMP-Seven_Mechanism_Classes-142-119': ('synthesis-suggested', 'established', 'the seat`s read: universality is R1, false as stated '
                                             '(not_register1, F7), asserted by construction'),
    'COMP-Seven_Mechanism_Classes-155-136': ('argument-supported', 'established', 'the seat`s read: "proved spectrally inert" -- the '
                                             'inter-class conservation step stated as proved (F7)'),
    'COMP-Seven_Mechanism_Classes-155-137': ('synthesis-suggested', 'established', 'the seat`s read: every summand certified is the '
                                             'catalogue`s exhaustiveness at ξ, open (F11)'),
    'COMP-Seven_Mechanism_Classes-209-178': ('kernel-verified', 'established', 'the seat`s read: Kernel/PoissonExhaustion.lean at SIDE-kernel '
                                             'v1.5 = 0e5233f carries no sorry and no axiom declaration (git grep at the pin)'),
    'COMP-Seven_Mechanism_Classes-211-180': ('kernel-verified', 'established', 'the seat`s read: Kernel/Layer1.lean at SIDE-kernel v1.5 = '
                                             '0e5233f carries no sorry and no axiom declaration (git grep at the pin)'),
    # ### Silence_of_Foundations, every non-MATCHES row read whole by the seat
    'COMP-Silence_of_Foundations-45-51': ('theorem-supported', 'graded', 'the seat`s read: a textbook fact of molecular biology (the standard '
                                          'code, NCBI Translation Table 1, which the paper cites at :47), stated as such'),
    'COMP-Silence_of_Foundations-108-121': ('argument-supported', 'graded', 'the seat`s read: the ZFC proof from Tate`s thesis stated as the '
                                            'paper`s result (F3), as its :9 states it'),
    'COMP-Silence_of_Foundations-134-143': ('synthesis-suggested', 'graded', 'the seat`s read: a reading of the cited literature (Kim 1999, '
                                            'Chalmers 2006), stated as a reading'),
    # ### Third_Identity_Element, every non-MATCHES row read whole by the seat
    'COMP-Third_Identity_Element-11-8': ('argument-supported', 'graded', 'the seat`s read: the paper`s own argument (the voice theorems derive '
                                         'σ = 1/2 for C₁-C₅, F5 (ii); the rest is the paper`s), stated as its framing'),
    'COMP-Third_Identity_Element-17-12': ('theorem-supported', 'graded', 'the seat`s read: an elementary identity of arithmetic, true'),
    'COMP-Third_Identity_Element-21-22': ('theorem-supported', 'graded', 'the seat`s read: an elementary identity of arithmetic, true'),
    'COMP-Third_Identity_Element-32-31': ('theorem-supported', 'graded', 'the seat`s read: an elementary identity of arithmetic, true'),
    'COMP-Third_Identity_Element-33-32': ('theorem-supported', 'graded', 'the seat`s read: an elementary identity of arithmetic, true'),
    'COMP-Third_Identity_Element-55-49': ('argument-supported', 'graded', 'the seat`s read: true for coprime pairs above 1 -- g(a, b) = 1 '
                                          'forces (a - 1)(b - 1) = 2, so {a, b} = {2, 3}'),
    'COMP-Third_Identity_Element-101-85': ('argument-supported', 'established', 'the seat`s read: the bijection`s content, stated as proved '
                                           '(its Lean form identity_formation_bijection SHELL in the terminal table; F11), as its sibling row'),
}
# ### row id -> 'AGREE' | 'CORRECTED': MATCHES rows drawn with seed 646 (five per companion, _sample) and read whole by the seat
COMP_SAMPLE = dict((k, 'AGREE') for k in (
    'COMP-Exhaustive_Enumeration-120-122', 'COMP-Exhaustive_Enumeration-57-56', 'COMP-Exhaustive_Enumeration-58-57',
    'COMP-Exhaustive_Enumeration-92-87', 'COMP-Exhaustive_Enumeration-92-89',
    'COMP-Which_Structure_Confines-117-110', 'COMP-Which_Structure_Confines-181-164', 'COMP-Which_Structure_Confines-224-204',
    'COMP-Which_Structure_Confines-261-246', 'COMP-Which_Structure_Confines-61-45',
    'COMP-Spectral_Inertness-13-18', 'COMP-Spectral_Inertness-13-19', 'COMP-Spectral_Inertness-17-21', 'COMP-Spectral_Inertness-31-31',
    'COMP-Spectral_Inertness-52-45',
    'COMP-Seven_Mechanism_Classes-103-89', 'COMP-Seven_Mechanism_Classes-137-114', 'COMP-Seven_Mechanism_Classes-282-228',
    'COMP-Seven_Mechanism_Classes-46-43', 'COMP-Seven_Mechanism_Classes-55-51',
    'COMP-Third_Identity_Element-148-126', 'COMP-Third_Identity_Element-167-145', 'COMP-Third_Identity_Element-184-163',
    'COMP-Third_Identity_Element-280-233', 'COMP-Third_Identity_Element-88-73',
    'COMP-Silence_of_Foundations-102-111', 'COMP-Silence_of_Foundations-218-199', 'COMP-Silence_of_Foundations-224-203',
    'COMP-Silence_of_Foundations-74-85', 'COMP-Silence_of_Foundations-9-7',
    'COMP-ONE_PAGE_PROOF-19-15', 'COMP-ONE_PAGE_PROOF-21-17', 'COMP-ONE_PAGE_PROOF-25-21', 'COMP-ONE_PAGE_PROOF-32-27',
    'COMP-ONE_PAGE_PROOF-90-89'))
COMP_READ_ALL = {'ONE_PAGE_PROOF', 'Exhaustive_Enumeration', 'Which_Structure_Confines', 'Spectral_Inertness', 'Seven_Mechanism_Classes',
                 'Silence_of_Foundations', 'Third_Identity_Element'}   # ### the companions whose every non-MATCHES row the seat has read whole
SAMPLE_N = 5


def _sample(name, rows):
    import random
    pool = sorted(r['id'] for r in rows if r['verdict'] == 'MATCHES' and not r['fixed'])
    return sorted(random.Random('646-' + name).sample(pool, min(SAMPLE_N, len(pool))))


def _comp_lines(name):
    return lines_of(_show(PP, PRE_PP, 'day1/%s.md' % name))


def _comp_records(name):
    recs, faults = [], []
    p = os.path.join(SP, 'intake_%s.tsv' % name)
    if not os.path.exists(p):
        return [], ['%s: no reader file' % name]
    for k, raw in enumerate(io.open(p, encoding='utf-8').read().replace(chr(13), '').split(NL), 1):
        if not raw.strip():
            continue
        f = raw.split('\t')
        if f[0] == 'CLAIM' and len(f) >= 8:
            recs.append(('CLAIM', dict(line=f[1].strip(), grade=f[2].strip(), stated_as=f[3].strip(), terminal=f[4].strip(),
                                       route=f[5].strip(), quote=f[6], reason='\t'.join(f[7:]).strip(), rec=k)))
        elif f[0] == 'SKIP' and len(f) >= 3:
            recs.append(('SKIP', dict(line=f[1].strip(), reason='\t'.join(f[2:]).strip(), rec=k)))
        else:
            faults.append('%s record %d malformed: %r' % (name, k, raw[:120]))
    return recs, faults


# ### the seat's own SKIP records for a non-blank line a reader left uncovered, each read by the seat and marked as the seat's
SEAT_SKIPS = {('Third_Identity_Element', 73): 'the seat`s (the reader left the line uncovered): a heading label, "**Corollary.**", no assertion'}


def _comp_rows(name):
    import licensed_table as LT
    ls = _comp_lines(name)
    recs, faults = _comp_records(name)
    recs += [('SKIP', dict(line=str(ln), reason=why, rec=0)) for (nm, ln), why in sorted(SEAT_SKIPS.items()) if nm == name]
    rows_all, _md = _tt()
    tnames = collections.defaultdict(list)
    for x in rows_all:
        tnames[x['name'].split('.')[-1]].append(x)
    covered = collections.defaultdict(list)
    rows, skips = [], []
    for kind, r in recs:
        if not r['line'].isdigit() or not (1 <= int(r['line']) <= len(ls)):
            faults.append('%s record %d: line %r outside :1-:%d' % (name, r['rec'], r['line'], len(ls)))
            continue
        ln = int(r['line'])
        covered[ln].append(kind)
        if kind == 'SKIP':
            skips.append(dict(line=ln, reason=r['reason']))
            continue
        q = r['quote']
        if not (len(q) >= 8 and q in ls[ln - 1]):
            faults.append('%s record %d (:%d): the quote is not a substring of its line: %r' % (name, r['rec'], ln, q[:80]))
            continue
        rid = 'COMP-%s-%d-%d' % (name, ln, r['rec'])
        fix = COMP_FIX.get(rid)
        grade, sa, reason = (fix[:3] if fix else (r['grade'], r['stated_as'], r['reason']))
        route = (fix[3] if fix and len(fix) > 3 else r['route'])
        refined = False
        if not fix and grade in ('argument-supported', 'synthesis-suggested', 'theorem-supported') and sa == 'established' \
                and not STATUS_WORDS.search(q) and not re.search(r'\bF(?:[1-9]|1[0-3]|15)\b', reason):
            sa, refined = 'graded', True
        if grade not in INTAKE_GRADES:
            faults.append('%s record %d (:%d): grade %r' % (name, r['rec'], ln, grade))
            continue
        route = route if route in ('no', 'DARK', 'BRIGHT') else 'no'
        try:
            v = LT.map_intake(grade, sa, 'DARK' if route == 'DARK' else 'NOT A ROUTE')
        except KeyError:
            faults.append('%s record %d (:%d): the pair (%s, %s) is not in the mapping' % (name, r['rec'], ln, grade, sa))
            continue
        term = r['terminal'].strip('`') if r['terminal'] not in ('-', '') else ''
        tline = ''
        if term:
            hits = tnames.get(term.split('.')[-1]) or []
            tline = ('; its row: %s' % ' | '.join('%s %s %s' % (x['repo'], x['name'], x['grade']) for x in hits[:2])) if hits else \
                '; the terminal is no row of the terminal table'
        facts = sorted(set(re.findall(r'\bF(\d{1,2})\b', reason)), key=int)
        if v == 'MATCHES':
            act = 'none'
        elif v == 'UNLICENSED':
            act = 'RETIRE TO ERRATA: asserted with no kernel and no citation reaching it (%s); the companion`s next edition carries no such sentence' % grade
        else:
            rc = [RECUT_BY_FACT['F' + f] for f in facts if 'F' + f in RECUT_BY_FACT]
            act = 'RE-CUT: %s -- %s' % (q[:120], '; '.join(rc) if rc else 'state the claim at its grade (%s), %s' % (
                grade, 'saying what the corpus now licenses' if v == 'UNDERSTATES' else 'no more than its support carries'))
        rows.append(dict(id=rid, source='day1/%s.md:%d' % (name, ln), stated=q, line=ln, companion=name,
                         licensed='intake: %s, stated as %s%s%s; the mapping (%s, %s) -> %s; %s' % (
                             grade, sa, (', terminal ' + term) if term else '', tline, grade, sa, v, reason),
                         by='intake', verdict=v, action=act, grade=grade, stated_as=sa, terminal=term, route=route, fixed=bool(fix),
                         refined=refined))
    unc = [i for i, l in enumerate(ls, 1) if l.strip() and i not in covered]
    return rows, skips, faults, unc


_TT = None


def _tt():
    global _TT
    if _TT is None:
        _TT = (json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'],
               lines_of(_show(RELAY, PRE_RELAY, 'data/terminal_table.md')))
    return _TT


def mapping(*a):
    """data/b646_mapping.txt: the outcome-to-verdict mapping as b645 printed it (tools/licensed_table.py MAPPING, by line), the stated-as
    rule and the re-cut by fact -- written and committed before any companion's run."""
    import licensed_table as LT
    src = io.open(os.path.join(ROOT, 'tools', 'licensed_table.py'), encoding='utf-8').read().split(NL)
    at = [i for i, l in enumerate(src, 1) if l.startswith('MAPPING = [')][0]
    L = ['b646 -- COMPONENT 2, (R256)(3): THE MAPPING, PRINTED BEFORE THE RUN (%s)' % utc(), '',
         '### from relay tools/licensed_table.py :%d (MAPPING) and :%d (map_intake), sha256 %s -- as b645 printed it (relay '
         'data/b645_table_monograph.txt)' % (at, [i for i, l in enumerate(src, 1) if l.startswith('def map_intake')][0],
                                             sha(io.open(os.path.join(ROOT, 'tools', 'licensed_table.py'), 'rb').read())[:16]), '',
         '### (grade, stated as) -> verdict:'] + ['    %-26s %-12s -> %-12s %s' % m for m in LT.MAPPING]
    L += ['', '### the stated-as rule (b645`s, relay tools/b645_record.py STATUS_WORDS): an argument-, synthesis- or theorem-grade row the reader '
          'marked `established` keeps it only where its quote matches %s or its reason names F1-F13 or F15; else `graded`.' % STATUS_WORDS.pattern,
          '', '### the re-cut by fact (F5 re-written for the two theorems of that name, b645`s defect (e)):'] + \
         ['    %s %s' % kv for kv in sorted(RECUT_BY_FACT.items(), key=lambda kv: int(kv[0][1:]))]
    L += ['', '### the readers` brief: the scratchpad`s companion_brief.md, sha256 %s' % sha(io.open(os.path.join(SP, 'companion_brief.md'), 'rb').read())]
    put_txt('b646_mapping.txt', L)
    print('  written: b646_mapping.txt (%d lines)' % len(L))


def comp_check(*a):
    """prints each reader's records' validation -- faults, uncovered lines, counts -- and its non-MATCHES rows for the seat's read; writes nothing."""
    for name, _lab in K.COMPANIONS:
        if a and name not in a:
            continue
        rows, skips, faults, unc = _comp_rows(name)
        print('=== %s: rows %d ; skips %d ; faults %d ; uncovered %s ; %s' % (name, len(rows), len(skips), len(faults), unc[:20] or 'NONE',
                                                                          dict(collections.Counter(r['verdict'] for r in rows))))
        for f in faults[:30]:
            print('  FAULT ' + f)
        if 'sample' in a:
            byid = dict((r['id'], r) for r in rows)
            for i in _sample(name, rows):
                r = byid[i]
                print('  SAMPLE %s [%s, %s] %r | %s' % (i, r['grade'], r['stated_as'], r['stated'][:200], r['licensed'].split('; ')[-1][:160]))
        if 'rows' in a:
            for r in rows:
                if r['verdict'] != 'MATCHES':
                    print('  %s %s [%s, %s, %s] %r | %s' % (r['id'], r['verdict'], r['grade'], r['stated_as'], r['route'], r['stated'][:160],
                                                         r['licensed'].split('; ')[-1][:160]))


def companions(*a):
    """data/b646_table_<name>.txt and .json for each of the seven: (R256)(3) -- the companion at its patch label through the intake form,
    every claim a row of the licensed-statement table, each to one verdict with its ACTION by the mapping printed first (data/b646_mapping.txt);
    the readers' records checked (every quote a substring of its line, every non-blank line a CLAIM or a SKIP, every pair in the mapping);
    every non-MATCHES row read whole by the seat; counts by verdict; the OVERREACHES and UNLICENSED rows printed in full."""
    import licensed_table as LT
    if not os.path.exists(os.path.join(D, 'b646_mapping.txt')):
        sys.exit('### THE MAPPING IS NOT BANKED -- RUN `mapping` FIRST -- NOTHING WRITTEN')
    out = {}
    for name, lab in K.COMPANIONS:
        rows, skips, faults, unc = _comp_rows(name)
        if faults or unc:
            sys.exit('### %s: %d FAULTS AND %d UNCOVERED LINES -- NOTHING WRITTEN: %s %s' % (name, len(faults), len(unc), faults[:3], unc[:10]))
        cnt, f2 = LT.table(rows)
        if f2:
            sys.exit('### %s: THE TABLE REFUSED: %s' % (name, list(f2.items())[:4]))
        unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and name not in COMP_READ_ALL and r['id'] not in COMP_FIX]
        if unread:
            sys.exit('### %s: %d NON-MATCHES ROWS NOT READ BY THE SEAT -- NOTHING WRITTEN: %s' % (name, len(unread), unread[:8]))
        smp = _sample(name, rows)
        if any(i not in COMP_SAMPLE for i in smp):
            sys.exit('### %s: THE SAMPLE DRAWN %s IS NOT THE SAMPLE READ -- NOTHING WRITTEN' % (name, smp))
        src = _show(PP, PRE_PP, 'day1/%s.md' % name)
        L = ['b646 -- COMPONENT 2, (R256)(3): %s AT ITS PATCH LABEL %s THROUGH THE INTAKE FORM, EVERY CLAIM A ROW (tools/licensed_table.py) (%s)' % (
            name, lab, utc()), '',
            '### the document: PLACE-papers day1/%s.md at %s, %d lines, sha256 %s' % (name, PRE_PP, len(lines_of(src)), sha(src.encode('utf-8'))),
            '### the form: b628`s intake (relay tools/b628_record.py `intake`, tools/b628_worklist.py); the rows read by one helper reader of this '
            'session from the brief (the scratchpad`s companion_brief.md, `established` narrowed per b645`s defect (d), F5 naming both theorems '
            'per its (e)); the verdict by the mapping alone (relay data/b646_mapping.txt), never by a reader; every non-MATCHES row read whole by '
            'the seat (%d corrected); the stated-as rule moved %d rows' % (sum(1 for r in rows if r['fixed']), sum(1 for r in rows if r['refined'])),
            '### the MATCHES sample: %d rows drawn with seed 646 from the MATCHES rows no correction touched, each read whole by the seat -- %d agree, '
            '%d corrected (%s)' % (len(smp), sum(1 for i in smp if COMP_SAMPLE[i] == 'AGREE'), sum(1 for i in smp if COMP_SAMPLE[i] != 'AGREE'),
                                   ', '.join(i.split('-', 2)[2] for i in smp)),
            '### a seat SKIP for an uncovered line: %s' % ('; '.join(':%d %s' % (ln, w) for (nm, ln), w in SEAT_SKIPS.items() if nm == name) or 'none'), '']
        L += ['### EVERY ROW (line | grade | stated as | terminal | route | VERDICT ; the quote ; the ACTION):']
        for r in sorted(rows, key=lambda x: (x['line'], x['id'])):
            L.append('  :%d | %s | %s | %s | %s | %s ; "%s" ; %s' % (r['line'], r['grade'], r['stated_as'], r['terminal'] or '-', r['route'],
                                                                  r['verdict'], r['stated'][:200], r['action'][:240]))
        L += ['', '### THE SKIPS (line | reason), %d:' % len(skips)] + ['  :%d | %s' % (s['line'], s['reason'][:120]) for s in sorted(skips, key=lambda x: x['line'])]
        L += ['', '### THE ROWS READING OVERREACHES OR UNLICENSED, IN FULL:']
        for r in sorted(rows, key=lambda x: x['line']):
            if r['verdict'] in ('OVERREACHES', 'UNLICENSED'):
                L += ['  :%d %s -- STATED "%s"' % (r['line'], r['verdict'], r['stated']), '      LICENSED %s' % r['licensed'], '      ACTION %s' % r['action']]
        L += ['', '### ### **%s: CLAIMS %d ; SKIPPED LINES %d ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d ; A ROW WITHOUT A '
                  'VERDICT 0 ; UNCOVERED LINES 0.**' % (name, len(rows), len(set(s['line'] for s in skips)), cnt['MATCHES'], cnt['UNDERSTATES'],
                                                       cnt['OVERREACHES'], cnt['UNLICENSED'])]
        put_txt('b646_table_%s.txt' % name, L)
        put_json('b646_table_%s.json' % name, dict(at=utc(), label=lab, counts=cnt, rows=rows, skips=skips))
        out[name] = cnt
        print(L[-1])
    tot = collections.Counter()
    for c in out.values():
        tot.update(c)
    print('  ### ### **THE SEVEN: CLAIMS %d ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d**' % (
        sum(tot.values()), tot['MATCHES'], tot['UNDERSTATES'], tot['OVERREACHES'], tot['UNLICENSED']))


# ================================================================================ COMPONENT 3: THE MET LIST AND THE RE-GRADE, (R256)(4)(d)
MET_ENTRY = "TrivialSummandPremise'"
DEDEKIND = "SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'"


def _graded(fn):
    """grade each subject by fn() twice -- MET without the entry (before the ruling) and MET at HEAD -- and return [(subject, before, after)]."""
    import e0_rule as E
    met = E.MET
    if MET_ENTRY not in met:
        sys.exit('### THE ENTRY IS NOT IN MET AT HEAD -- NOTHING WRITTEN')
    E.MET = tuple(x for x in met if x != MET_ENTRY)
    try:
        before = fn()
    finally:
        E.MET = met
    after = fn()
    return [(k, before[k], after.get(k)) for k in before]


def regrade(*a):
    """data/b646_regrade.txt: (R256)(4)(d) -- the gate rerun over SIDE-explicit-formula after the MET entry: every statement the gate and the
    table grade by the rule, graded without the entry and at HEAD, every move printed -- (i) the gate's bank of b642 (relay data/b642_grades.txt,
    each graded statement); (ii) the terminal table's SIDE-explicit-formula rows by their printed statements (terminal_table.rule_reading);
    (iii) the elaborated reader's bank (relay data/elab_types.txt, terminal_table.elab_reading)."""
    import e0_rule as E
    import terminal_table as T
    g42 = lines_of(rd('b642_grades.txt'))
    subj = []
    for i, l in enumerate(g42):
        m = re.match(r'^(\S+)  (theorem|def)  (\S+)', l)
        if m and m.group(2) == 'theorem' and i + 1 < len(g42) and g42[i + 1].startswith('    statement: '):
            subj.append((m.group(3), g42[i + 1].split('statement: ', 1)[1]))

    def gate():
        out = {}
        for n, st in subj:
            try:
                out[n] = E.grade(st, 'theorem')[:2]
            except Exception as x:
                out[n] = ('UNCLASSED', str(x)[:80])
        return out
    rows = [x for x in json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'] if x['repo'] == 'SIDE-explicit-formula']

    def table():
        out = {}
        for x in rows:
            try:
                out[x['name']] = T.rule_reading(x.get('statement'), x['name'])
            except Exception as e:
                out[x['name']] = ('?', 'UNCLASSED %s' % str(e)[:60])
        return out
    names = sorted(T.elab_bank().keys())

    def elab():
        out = {}
        for n in names:
            try:
                out[n] = T.elab_reading(n)
            except Exception as e:
                out[n] = ('UNCLASSED %s' % str(e)[:60], None)
        return out
    parts = [('the gate`s bank of b642 (data/b642_grades.txt, the graded theorems)', _graded(gate)),
             ('the terminal table`s SIDE-explicit-formula rows by their printed statements', _graded(table)),
             ('the elaborated reader`s bank (data/elab_types.txt)', _graded(elab))]
    L = ['b646 -- COMPONENT 3, (R256)(4)(d): THE GATE RERUN OVER SIDE-explicit-formula AFTER THE MET ENTRY (%s)' % utc(), '',
         '### the entry: %s, in tools/e0_rule.py`s MET at relay %s (MET %d names at HEAD); each subject graded without the entry and at HEAD' % (
             MET_ENTRY, g(RELAY, 'log', '--format=%h', '-1', '--', 'tools/e0_rule.py').strip()[:8], len(E.MET)), '']
    allmoves = []
    for what, res in parts:
        mv = [(k, b, a) for k, b, a in res if b != a]
        allmoves += [(what, k, b, a) for k, b, a in mv]
        L += ['### %s: subjects %d ; moved %d' % (what, len(res), len(mv))]
        for k, b, a in mv:
            L.append('    MOVE %s : %s -> %s' % (k, b, a))
    names_moved = sorted(set(k for _w, k, _b, _a in allmoves))
    L += ['', '### ### **DECLARATIONS MOVED %d (%s) ; dedekind_rhs` %s.**' % (
        len(names_moved), ', '.join(names_moved) or 'none',
        'READS INTERFACES' if any(k == DEDEKIND and (a[0] if isinstance(a, tuple) else a) == 'INTERFACES' for _w, k, _b, a in allmoves) else 'DID NOT MOVE TO INTERFACES')]
    put_txt('b646_regrade.txt', L)
    put_json('b646_regrade.json', dict(at=utc(), moves=[dict(part=w, name=k, before=list(b) if b else b, after=list(a) if a else a)
                                                       for w, k, b, a in allmoves]))
    print(NL.join(L[2:]))


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_diff(*a):
    """data/b646_table_diff.txt: the terminal table regenerated (tools/terminal_table.py) after the MET entry and diffed against relay HEAD`s
    committed table, by row -- every moved row printed with its grade, profile and provenance before and after."""
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b646 -- COMPONENT 3: THE TERMINAL TABLE REGENERATED AFTER THE MET ENTRY (%s); exit %d ; against relay HEAD %s' % (
        utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    for k in moved:
        L.append('    MOVED %s %s : %s -> %s' % (k[0], k[1], before[k], after[k]))
    for k in added:
        L.append('    ADDED %s %s : %s' % (k[0], k[1], after[k]))
    for k in gone:
        L.append('    GONE %s %s : %s' % (k[0], k[1], before[k]))
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (
        len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b646_table_diff.txt', L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 4: THE DESCRIPTION AT v3, (R256)(4)
# ### The composer, carried from b644's (relay tools/b644_record.py :1205-:1332, sealed at b644), its sources read through b644's own sealed
# ### helpers (imported, never copied): the glossary, README's ceiling, the banked #print axioms lines, the premise table, the hinges, the
# ### W-ORD-PREMISE-* discharge clauses, the surround, ERRATA's form, the draft's creator. The terminal table is a parameter (`TR`), so the
# ### carried composer is shown to reproduce v2 byte for byte from the table as it stood at v2 before any rule of (R256)(4) is added.
V2 = 'b644_deposit_description.txt'
V2_TABLE_REV = 'e1d39ccf^'    # ### the table as it stood when v2 was composed (unchanged from b644 to the MET entry)
ZEN_URL = 'https://developers.zenodo.org/'
ZEN_PAGE = 'zenodo_dev.html'   # ### the page as read at source, in the scratchpad
ZEN_SHA = 'bbd72463dcf7e07f597ed2b145e8019fb0e861c4811a8d22e0e5d202bde69e61'
RULES = ('a', 'b', 'c', 'd')   # ### the composition rules of (R256)(4), each added through the Edit tool with its test (tools/test_composer_b646.py)


def _R4():
    import b644_record as R4
    return R4


def _tr(rev=None):
    if rev is None:
        T = jl('terminal_table.json')
    else:
        T = json.loads(_show(RELAY, rev, 'data/terminal_table.json'))
    return dict(((r['repo'], r['name'].split('.')[-1]), r) for r in T.get('rows') or [])


def compose_carried(rules=None, TR=None):
    """the description's HTML: b644's composer carried as it stood, no rule applied (the reproduction of v2)."""
    R4 = _R4()
    rules = RULES if rules is None else rules
    gl, (sup, nsup), PR = R4._gl(), R4._readme_ceiling(), R4._prints()
    TR = _tr() if TR is None else TR
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    HJ = dict((r['head'], r) for r in jl('b644_hinges.json').get('rows') or [])
    DC = R4._discharge_clauses()
    creator = jl('b644_draft_meta.json').get('creators') or []
    surround = R4.K.show('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 'HEAD') or ''
    sq = re.search(r'the geometric face names a single concrete analytic target: (the jaws overlap at every height \*\*iff\*\* .+?reaches the zero-free region)',
                   surround)
    errata = R4.K.show('ERRATA.md', 'HEAD') or ''
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
    located = gl['the located clause'].rstrip('.')
    P.append('THE CLAIM. %s is the name of the research programme whose papers, kernels and ledgers this record deposits; it makes its '
             'claim in one sentence, as its README states it: "%s." Here RH is %s. The located clause: '
             '%s. %s h2_sign is %s. %s classK is %s. The ceiling, in the README\'s words: supportable, "%s"; not supported, "%s" -- the corpus does '
             'not support that sentence, since h2_sign is open, and nothing in this record states that the Riemann Hypothesis holds.' % (
                 'A PLACE TO STAND', sup, gl['RH'].rstrip('.'), located, mex, gl['h2_sign'].rstrip('.'), one,
                 gl['classK'].rstrip('.'), sup, nsup))
    # ---- (ii) WHAT IS MACHINE-VERIFIED
    tags = dict((k, g('D:/' + k, 'rev-parse', '--short=7', '%s^{commit}' % t).strip()) for k, t in R4.KERNEL_TAG.items())
    items = []
    for k, n in R4.DESC_THEOREMS:
        r = TR.get((k, n))
        full = [x for x in PR if x.split('.')[-1] == n]
        pr = PR[full[0]] if full else None
        grade = r['grade'] if r else 'not in the table'
        s = '%s (%s at its tag %s = %s; %s; #print axioms %s)' % (n, k, R4.KERNEL_TAG[k], tags[k], grade, pr or 'NOT BANKED')
        stmt = (r or {}).get('statement') or ''
        if n == 'h1_complete_at_Phi':
            conj = [c.strip().split()[0] for c in R4._split_conclusion(' '.join(stmt.split()))[1].split('∧')]
            s += (' -- it states that the fixed function Phi meets the %d couplings it names at once (%s); its docstring calls it the h1 leg of a '
                  'bracket whose other leg is h2, %s, which stays open' % (len(conj), ', '.join(conj), gl['h2'].split(';')[0]))
        if n.endswith('_holds') and (k, n[:-len('_holds')]) in TR:
            s += ' -- it proves %s, a proposition the kernel defines' % n[:-len('_holds')]
        if grade in ('INTERFACES', 'PREDICATE-UNLISTED'):
            on = R4._rests_on(n)
            hyp = [x for x in re.findall(r'(\w+)\s*→', R4._split_conclusion(stmt)[1] or stmt) if (k, x + '_holds') in TR]
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
                d = ('what would discharge it: ' + DC[h][1].rstrip('.')) if h in DC else ('carried by %s' % R4.CARRIED_WO.get(h, 'its work-order'))
            elif st == 'CITED':
                d = 'cited at its literature source and not compiled; a compiled proof would discharge it in the kernel'
            elif st == 'DISCHARGED':
                d = 'discharged where it is used'
            elif st == 'WITNESSED':
                d = ('witnessed by a construction nothing uses; a compiled proof would discharge it [a witness shows the premise can be met by '
                     'some object; a discharge proves it for the objects the theorems resting on it use]')
            else:
                d = ('refuted: its pole term is positive where it requires zero; TrivialSummandPremise\' carries the pole term in its place, '
                     'and dedekind_rhs\' is proved on it')
            ents.append('%s%s, %s' % (h, mark, d))
        if st == 'OPEN':
            salted = [h for h in hs if h in DC and 'salt checks show it is not vacuous' in DC[h][1]]
            if salted:
                ents.append('[the clause of %s differs because its salt checks already show it can be satisfied: what remains is a construction '
                            'that a proof actually uses]' % ', '.join(salted))
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
    fc = re.search(r'The attribution face (asks whether every zero is single-class-produced) \(`covers_all`\); the geometric face (asks whether the '
                   r'two jaws meet at every height)\.', surround)
    faces = ('The two faces, in the same text\'s words: the attribution face %s; the geometric face %s.' % (fc.group(1), fc.group(2))
             if fc else 'NOT READ')
    P.append('WHAT IS OPEN. h2_sign: %s. The squeeze between the zero-free region pressing in from the line of real part one and the transversality '
             'at the critical line has one concrete target, in the words of THE_UNCONDITIONAL_SURROUND: %s. Its faces, the same text says, are '
             'two statements of one open node: "%s", as h2_sign is by h2_sign_iff_rh; the squeeze\'s target is that node seen geometrically, not a '
             'second open premise. %s' % (gl['h2_sign'], (re.sub(r'\*\*', '', sq.group(1)).strip().rstrip(',')) if sq else 'NOT READ',
                                          eq.group(1) if eq else 'NOT READ', faces))
    # ---- (v) HOW A DEFECT IS REPORTED
    P.append('HOW A DEFECT IS REPORTED. A defect in this record is filed as an entry of ERRATA.md, in this record\'s files: %s Write to the '
             'record\'s creator, %s.' % (
                 ('ERRATA "records corrections to the deposited line after its Zenodo publication", and each entry lists the paper, the affected '
                  'section or line, the correction, and the date; entries are retained across deposits.') if ef else 'NOT READ',
                 '; '.join('%s (ORCID %s)' % (c.get('name'), c.get('orcid')) for c in creator) or 'NOT READ'))
    return ''.join('<p>%s</p>' % R4._esc(p.replace('`', '')) for p in P)


# ### THE FOUR COMPOSITION RULES OF (R256)(4), each tested (tools/test_composer_b646.py):
# ###  (a) a cell common to every row of a list is stated once as the list's header (the two headers below, verbatim); the rows carry their
# ###      grade, caveat and exceptions alone;
# ###  (b) the five parts headed and the theorems and the premises-by-status lists, in the HTML Zenodo accepts (relay data/b646_zenodo_tags.json):
# ###      a part's head <p><strong>..</strong></p>, a list <ul><li>..</li></ul>, every tag used checked against the bank;
# ###  (c) the exhaustiveness sentence verbatim, THE_UNCONDITIONAL_SURROUND §6a cited by its words, and the located clause's "bounds by its
# ###      mechanism exclusions" replaced by the sentence's short form; the old exclusions sentence leaves;
# ###  (d) no instrument's unfinished reading: no PREDICATE-UNLISTED definition or grade in the text (dedekind_rhs' reads INTERFACES after the
# ###      MET entry), an INTERFACES theorem whose premises no bank names given them from the rule's own reading of its statement.
ALL_RULES = ('a', 'b', 'c', 'd')
PART_HEADS = ('THE CLAIM.', 'WHAT IS MACHINE-VERIFIED.', 'WHAT THE LOAD-BEARING THEOREMS ASSUME.', 'WHAT IS OPEN.', 'HOW A DEFECT IS REPORTED.')
HEAD_THEOREMS = ('every theorem below is in SIDE-explicit-formula at v0.26 = 82550e4 and holds at the standard three axioms, unless marked')
HEAD_PREMISES = 'unless noted, a premise is discharged by a compiled proof, a vendored theorem, or a citation of every field'
EXHAUST = ('the seven-class catalogue is complete over its named classes; that every zero is produced by a named class (covers_all) is the open '
           'clause in its attribution face, equivalent to h2_sign given the surround, and not a separate obligation')
OLD_BOUNDS = ', bounds by its mechanism exclusions,'
SHORT_FORM = ' (in its attribution face covers_all, over the seven-class catalogue complete over its named classes)'
DEFAULT_DC = 'a compiled proof in its kernel, a vendored theorem that proves it, or a citation of every field'


class UL(object):
    """a list: its items (a str, or (label, UL) for a nested list), the separator and tail its flat rendering takes."""
    def __init__(self, items, sep, tail=''):
        self.items, self.sep, self.tail = items, sep, tail


def _flat(seg):
    if isinstance(seg, UL):
        return seg.sep.join(_flat(x) for x in seg.items) + seg.tail
    if isinstance(seg, tuple):
        return seg[0] + _flat(seg[1])
    return seg


def _render(parts, rules):
    """flat (v2's form, one <p> per part) unless rule (b); under (b) each part headed and its lists as <ul>."""
    R4 = _R4()
    if 'b' not in rules:
        return ''.join('<p>%s</p>' % R4._esc(''.join(_flat(s) for s in segs).replace('`', '')) for _h, segs in parts)
    e = lambda s: R4._esc(s.replace('`', ''))   # noqa: E731

    def ul(L):
        return '<ul>%s</ul>' % ''.join('<li>%s</li>' % (e(x[0].rstrip(' -:')) + ul(x[1]) if isinstance(x, tuple) else e(x.rstrip(';. ')))
                                       for x in L.items)
    out = []
    for head, segs in parts:
        out.append('<p><strong>%s</strong></p>' % e(head.rstrip('.')))
        buf = ''
        for s in segs:
            if isinstance(s, UL):
                if buf.strip(' .;:|'):
                    out.append('<p>%s</p>' % e(buf.strip()))
                buf = ''
                out.append(ul(s))
            else:
                buf += s
        if buf.strip(' .;:|'):
            out.append('<p>%s</p>' % e(buf.strip().lstrip('.; ')))
    return ''.join(out)


def _premises_named(stmt):
    """the premise heads the E0 rule reads in a statement as the table prints it: the type heads of its INTERFACES binders, namespace dropped."""
    import e0_rule as E
    import terminal_table as T
    m = T._DECL_KW.match(stmt or '')
    if not m:
        return []
    head = re.sub(r'^\S+', '', stmt[m.end():], count=1)
    gr, why, _b = E.grade(' '.join(head.split()), 'theorem')
    if gr != 'INTERFACES':
        return []
    return [re.split(r'\s+', t.split(' : ', 1)[1].strip())[0].split('.')[-1] for t in why.split(', ') if ' : ' in t]


def compose_v3(rules=None, TR=None):
    """the description's HTML: b644's composer carried, with the rules of (R256)(4) named in `rules` applied (default: RULES); with no rule it
    is the carried composer's text (the reproduction of v2, checked by `carried`)."""
    R4 = _R4()
    rules = RULES if rules is None else tuple(rules)
    gl, (sup, nsup), PR = R4._gl(), R4._readme_ceiling(), R4._prints()
    TR = _tr() if TR is None else TR
    PT = dict((r['head'], r) for r in jl('b643_premise_table.json').get('rows') or [])
    HJ = dict((r['head'], r) for r in jl('b644_hinges.json').get('rows') or [])
    DC = R4._discharge_clauses()
    creator = jl('b644_draft_meta.json').get('creators') or []
    surround = R4.K.show('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md', 'HEAD') or ''
    sq = re.search(r'the geometric face names a single concrete analytic target: (the jaws overlap at every height \*\*iff\*\* .+?reaches the zero-free region)',
                   surround)
    errata = R4.K.show('ERRATA.md', 'HEAD') or ''
    ef = re.search(r'Each entry lists: the\s+paper, the affected section or line, the correction, and the date\.', errata)
    eq = re.search(r'(Both are equivalent to RH given the surround)\.', surround)
    fc = re.search(r'The attribution face (asks whether every zero is single-class-produced) \(`covers_all`\); the geometric face (asks whether the '
                   r'two jaws meet at every height)\.', surround)
    parts = []
    # ---- (i) THE CLAIM
    sup, nsup = (sup or '').rstrip('.'), (nsup or '').rstrip('.')
    cp = rd('b644_clause_path.txt')
    one = ('h2_sign is the one open clause of the reduction: the dependency path from h2_sign to RiemannHypothesis passes through the seam '
           'rh_strip_imp_rh, a classical fact the kernel compiles (rh_strip_imp_rh_holds), and consumes no OPEN premise; the OPEN premises in '
           'the table belong to the faces, instances and bounds, none on that path [in plain words: every OPEN premise in the table is assumed '
           'only by theorems the reduction from h2_sign to RH does not use], and the table is the keystone census at v0.7.1, in this '
           'record\'s files.' if re.search(r'; OPEN 0 ', cp) else 'NOT READ')
    located = gl['the located clause'].rstrip('.')
    if 'c' in rules:
        # ### (c): the located clause's "bounds by its mechanism exclusions" replaced by the exhaustiveness sentence's short form; the old
        # ### exclusions sentence replaced by the sentence verbatim, §6a cited by its words
        located = (located.replace(OLD_BOUNDS, ',').replace('h2_sign itself,', 'h2_sign itself%s,' % SHORT_FORM)
                   if OLD_BOUNDS in located and 'h2_sign itself,' in located else 'NOT READ')
        mex = ('On exhaustiveness: %s -- in the words of THE_UNCONDITIONAL_SURROUND, section 6a: "The attribution face %s (covers_all); the '
               'geometric face %s. %s."' % (EXHAUST, fc.group(1), fc.group(2), eq.group(1)) if fc and eq else 'NOT READ')
    else:
        mx = re.search(r'the mechanism exclusions are (the route terminals of SIDE-kernel) set out under WHAT IS MACHINE-VERIFIED below, (which compile '
                       r'that none of seven named mechanism classes produces the off-line signature the kernel defines, the exhaustiveness of the seven '
                       r'classes over all mechanisms not being compiled)', rd('b640_deposit_description.txt'))
        mex = ('Its mechanism exclusions are %s, %s; they rule out named sources of a zero off the critical line and do not prove h2_sign.' % (
            mx.group(1), mx.group(2)) if mx else 'NOT READ')
    parts.append(('THE CLAIM.', [
        'THE CLAIM. ' if 'b' not in rules else '',
        '%s is the name of the research programme whose papers, kernels and ledgers this record deposits; it makes its '
        'claim in one sentence, as its README states it: "%s." Here RH is %s. The located clause: '
        '%s. %s h2_sign is %s. %s classK is %s. The ceiling, in the README\'s words: supportable, "%s"; not supported, "%s" -- the corpus does '
        'not support that sentence, since h2_sign is open, and nothing in this record states that the Riemann Hypothesis holds.' % (
            'A PLACE TO STAND', sup, gl['RH'].rstrip('.'), located, mex, gl['h2_sign'].rstrip('.'), one,
            gl['classK'].rstrip('.'), sup, nsup)]))
    # ---- (ii) WHAT IS MACHINE-VERIFIED
    tags = dict((k, g('D:/' + k, 'rev-parse', '--short=7', '%s^{commit}' % t).strip()) for k, t in R4.KERNEL_TAG.items())
    STD = '[propext, Classical.choice, Quot.sound]'
    EFK = 'SIDE-explicit-formula'
    head_pin = '%s at %s = %s' % (EFK, R4.KERNEL_TAG[EFK], tags[EFK])
    items = []
    for k, n in R4.DESC_THEOREMS:
        r = TR.get((k, n))
        full = [x for x in PR if x.split('.')[-1] == n]
        pr = PR[full[0]] if full else None
        grade = r['grade'] if r else 'not in the table'
        if 'a' in rules:
            # ### (a): the row carries its grade, its caveat and its exceptions alone; the kernel, tag and axioms are the list's header
            exc = []
            if k != EFK:
                exc.append('in %s at %s = %s' % (k, R4.KERNEL_TAG[k], tags[k]))
            if pr != STD:
                exc.append('#print axioms %s' % (pr or 'NOT BANKED'))
            s = '%s -- %s%s' % (n, grade, (' (%s)' % '; '.join(exc)) if exc else '')
        else:
            s = '%s (%s at its tag %s = %s; %s; #print axioms %s)' % (n, k, R4.KERNEL_TAG[k], tags[k], grade, pr or 'NOT BANKED')
        stmt = (r or {}).get('statement') or ''
        if n == 'h1_complete_at_Phi':
            conj = [c.strip().split()[0] for c in R4._split_conclusion(' '.join(stmt.split()))[1].split('∧')]
            s += (' -- it states that the fixed function Phi meets the %d couplings it names at once (%s); its docstring calls it the h1 leg of a '
                  'bracket whose other leg is h2, %s, which stays open' % (len(conj), ', '.join(conj), gl['h2'].split(';')[0]))
        if n.endswith('_holds') and (k, n[:-len('_holds')]) in TR:
            s += ' -- it proves %s, a proposition the kernel defines' % n[:-len('_holds')]
        if grade in ('INTERFACES', 'PREDICATE-UNLISTED'):
            on = R4._rests_on(n)
            hyp = [x for x in re.findall(r'(\w+)\s*→', R4._split_conclusion(stmt)[1] or stmt) if (k, x + '_holds') in TR]
            named = _premises_named(stmt) if 'd' in rules else []
            if on:
                s += ' -- it holds on %s' % ', '.join('the premise %s, whose status is %s' % (h, PT[h]['status']) if h in PT else h for h in on)
            elif hyp:
                s += ' -- it holds on %s, which %s proves' % (hyp[0], hyp[0] + '_holds')
            elif named:
                # ### (d): the premises from the rule's own reading of the statement, each with its status where the premise table has it,
                # ### the restated premise with its witness as b642 banked it (relay data/b642_grades.txt, the dedekind_rhs' note)
                wit = re.search(r"\((trivialSummandPremise)`(_witness) at the constant 1", rd('b642_grades.txt'))
                ds = []
                for h in named:
                    if h in PT:
                        ds.append('%s, whose status is %s' % (h, PT[h]['status']))
                    elif h == "TrivialSummandPremise'" and wit:
                        ds.append("%s, the restated premise, witnessed in the kernel at the constant 1 (%s'%s)" % (h, wit.group(1), wit.group(2)))
                    else:
                        ds.append('%s, NOT READ' % h)
                s += ' -- it holds on the premises %s' % ' and '.join(ds)
            else:
                s += ' -- the premise it holds on is named in its statement'
        items.append(s)
    if 'd' in rules:
        itf = gl['INTERFACES'].rstrip('.')
        grades = 'The grades, read from each statement: DERIVES, %s; INTERFACES, %s%s' % (gl['DERIVES'].rstrip('.'), itf, '' if itf.endswith('."') else '.')
    else:
        grades = ('The grades, read from each statement: DERIVES, %s; '
                  'INTERFACES, %s; PREDICATE-UNLISTED, %s [In plain words: the grading rule met a named predicate on one of the statement\'s variables '
                  'that its list of restrictions does not yet hold; it marks the theorem for a ruling by the programme\'s author, who rules on the grading '
                  'rule, rather than reading the predicate as a premise.]' % (gl['DERIVES'].rstrip('.'), gl['INTERFACES'].rstrip('.'),
                                                                               gl['PREDICATE-UNLISTED'].rstrip('.') + '.'))
    intro = ('The named theorems -- %s: ' % HEAD_THEOREMS) if 'a' in rules else 'The named theorems: '
    if 'a' in rules and HEAD_THEOREMS.find(head_pin) < 0:
        intro = 'NOT READ: the header`s pin is not %s ' % head_pin
    parts.append(('WHAT IS MACHINE-VERIFIED.', [
        ('WHAT IS MACHINE-VERIFIED. ' if 'b' not in rules else '') +
        'A kernel is %s. A theorem holds at the standard three when its #print axioms reads exactly %s. %s %s' % (
            gl['kernel'].split(':')[0].rstrip('. '), gl['the standard three'].rstrip('.').replace(', written std3', ''), grades, intro),
        UL(items, '; ', '.')]))
    # ---- (iii) WHAT THE LOAD-BEARING THEOREMS ASSUME
    order = ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'REFUTED-BY-COMPUTATION')
    ST_NOTE = {'CITED': 'cited at its literature source and not compiled; a compiled proof would discharge it in the kernel',
               'DISCHARGED': 'discharged where it is used',
               'WITNESSED': ('witnessed by a construction nothing uses; a compiled proof would discharge it [a witness shows the premise can be met '
                             'by some object; a discharge proves it for the objects the theorems resting on it use]')}
    sts = []
    for st in order:
        hs = [h for h in PT if PT[h]['status'] == st]
        ents = []
        salted = [h for h in hs if h in DC and 'salt checks show it is not vacuous' in DC[h][1]] if st == 'OPEN' else []
        for h in hs:
            mark = ' (a HINGE)' if (HJ.get(h) or {}).get('hinge') else ''
            if st == 'OPEN':
                d = ('what would discharge it: ' + DC[h][1].rstrip('.')) if h in DC else ('carried by %s' % R4.CARRIED_WO.get(h, 'its work-order'))
                if 'a' in rules and h in DC and DC[h][1].rstrip('.') == DEFAULT_DC:
                    d = ''
                if 'a' in rules and h in salted:
                    d += (' [the clause differs because its salt checks already show it can be satisfied: what remains is a construction that a '
                          'proof actually uses]')
            elif st in ST_NOTE:
                d = '' if 'a' in rules else ST_NOTE[st]
            else:
                d = ('refuted: its pole term is positive where it requires zero; TrivialSummandPremise\' carries the pole term in its place, '
                     'and dedekind_rhs\' is proved on it')
            ents.append('%s%s%s' % (h, mark, (', ' + d) if d else ''))
        if st == 'OPEN' and salted and 'a' not in rules:
            ents.append('[the clause of %s differs because its salt checks already show it can be satisfied: what remains is a construction '
                        'that a proof actually uses]' % ', '.join(salted))
        label = ('%s, %s -- ' % (st, ST_NOTE[st])) if ('a' in rules and st in ST_NOTE) else '%s -- ' % st
        sts.append((label, UL(ents, '; ')))
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
    pintro = ('The premises, by status -- %s: ' % HEAD_PREMISES) if 'a' in rules else 'The premises, by status: '
    parts.append(('WHAT THE LOAD-BEARING THEOREMS ASSUME.', [
        ('WHAT THE LOAD-BEARING THEOREMS ASSUME. ' if 'b' not in rules else '') +
        'A premise is %s; a HINGE is %s %s %s' % (gl['premise'].rstrip('.'), hinge_def, wo, pintro),
        UL(sts, ' | '),
        '. The status DOMAIN marks a Mathlib predicate that restricts a variable its statement quantifies (%s): not an assumption, and not a '
        'hinge. The refuted premise is TrivialSummandPremise: %s; TrivialSummandPremise\' replaces it, carrying the pole term, and dedekind_rhs\' '
        'is proved on the restated premise. The full table, every premise with its status, its non-vacuity, its consumers by kernel and its '
        'hinge, is the keystone census at v0.7.1 (THE_KEYSTONE_CENSUS_v0_7_1.md, in this record\'s files).' % (
            ', '.join(dom), re.sub(r'^the sixth status of a premise: ', '', gl['REFUTED-BY-COMPUTATION']).rstrip('.'))]))
    # ---- (iv) WHAT IS OPEN
    faces = ('The two faces, in the same text\'s words: the attribution face %s; the geometric face %s.' % (fc.group(1), fc.group(2))
             if fc else 'NOT READ')
    if 'c' in rules:
        faces = 'Its attribution face is the exhaustiveness clause stated under THE CLAIM.'
    parts.append(('WHAT IS OPEN.', [
        ('WHAT IS OPEN. ' if 'b' not in rules else '') +
        'h2_sign: %s. The squeeze between the zero-free region pressing in from the line of real part one and the transversality '
        'at the critical line has one concrete target, in the words of THE_UNCONDITIONAL_SURROUND: %s. Its faces, the same text says, are '
        'two statements of one open node: "%s", as h2_sign is by h2_sign_iff_rh; the squeeze\'s target is that node seen geometrically, not a '
        'second open premise. %s' % (gl['h2_sign'], (re.sub(r'\*\*', '', sq.group(1)).strip().rstrip(',')) if sq else 'NOT READ',
                                     eq.group(1) if eq else 'NOT READ', faces)]))
    # ---- (v) HOW A DEFECT IS REPORTED
    parts.append(('HOW A DEFECT IS REPORTED.', [
        ('HOW A DEFECT IS REPORTED. ' if 'b' not in rules else '') +
        'A defect in this record is filed as an entry of ERRATA.md, in this record\'s files: %s Write to the record\'s creator, %s.' % (
            ('ERRATA "records corrections to the deposited line after its Zenodo publication", and each entry lists the paper, the affected '
             'section or line, the correction, and the date; entries are retained across deposits.') if ef else 'NOT READ',
            '; '.join('%s (ORCID %s)' % (c.get('name'), c.get('orcid')) for c in creator) or 'NOT READ')]))
    html = _render(parts, rules)
    if 'b' in rules:
        used = set(re.findall(r'</?([a-zA-Z0-9]+)', html))
        bad = sorted(used - _allowed_tags())
        if bad:
            sys.exit('### A TAG ZENODO DOES NOT ACCEPT: %s -- NOTHING COMPOSED' % bad)
    return html


def _parts_of(h):
    """the five parts of a description, v2's (one <p> each, its head its first words) or v3's (a <p><strong> head, then its blocks), as text."""
    if '<strong>' in h:
        segs = re.split(r'<p><strong>(.*?)</strong></p>', h)
        return [(segs[i] + '.', re.sub(r'<[^>]+>', ' ', segs[i + 1])) for i in range(1, len(segs) - 1, 2)]
    out = []
    for p in re.findall(r'<p>(.*?)</p>', h, re.S):
        hd = [x for x in PART_HEADS if p.startswith(x)]
        out.append((hd[0] if hd else '?', p[len(hd[0]):] if hd else p))
    return out


def describe(*a):
    """data/b646_deposit_description.txt (v3, the HTML the draft takes) and .json, beside v2 (relay data/b644_deposit_description.txt):
    composed by the record tool from banks under the four rules, the forbidden-content test run over it (b644's sealed `forbidden`), the
    five parts in the ruled order, every tag in Zenodo's bank; refuses to write on any hit or unread figure."""
    import hashlib
    R4 = _R4()
    html = compose_v3()
    heads = re.findall(r'<p><strong>(.*?)</strong></p>', html)
    order_ok = heads == [h.rstrip('.') for h in PART_HEADS]
    hits = R4.forbidden(html)
    unread = [m.group(0) for m in re.finditer(r'NOT READ|NOT BANKED|not in the table|None', html)]
    print('  parts %d, in the ruled order %s ; forbidden hits %d ; unread %d ; bytes %d' % (len(heads), order_ok, len(hits), len(unread),
                                                                                         len(html.encode('utf-8'))))
    for h in hits + [('unread', u) for u in unread]:
        print('    ### %s : %s' % h)
    if DRY:
        _write(os.path.join(SP, 'b646_deposit_description_dry.txt'), html.encode('utf-8'))
        return
    if hits or unread or not order_ok:
        sys.exit('### A FORBIDDEN CONTENT, AN UNREAD FIGURE OR THE PARTS OUT OF ORDER -- NOTHING WRITTEN')
    b = html.encode('utf-8')
    _write(os.path.join(D, 'b646_deposit_description.txt'), b)
    put_json('b646_deposit_description.json', dict(at=utc(), bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), heads=heads, rules=list(RULES),
                                                   order_ok=order_ok, forbidden=hits, v2_bytes=len(rd(V2).encode('utf-8'))))
    print('  written: data/b646_deposit_description.txt %d bytes, sha256 %s' % (len(b), hashlib.sha256(b).hexdigest()[:16]))


def desc_diff(*a):
    """data/b646_desc_diff.txt: v2 against v3, by part -- each part's bytes in each, the change in bytes, and what moved: the tokens the
    change-invariance check (b644's sealed `invariance`) reads as lost and added, printed for the reader; the whole's bytes."""
    R4 = _R4()
    v2, v3 = rd(V2), rd('b646_deposit_description.txt')
    if not v3:
        sys.exit('### v3 IS NOT BANKED -- RUN `describe` FIRST')
    p2, p3 = dict(_parts_of(v2)), dict(_parts_of(v3))
    L = ['b646 -- COMPONENT 4, (R256)(4): THE DESCRIPTION, v2 AGAINST v3, BY PART (%s)' % utc(), '',
         '### v2: relay data/%s, %d bytes ; v3: relay data/b646_deposit_description.txt, %d bytes ; the change %+d bytes' % (
             V2, len(v2.encode('utf-8')), len(v3.encode('utf-8')), len(v3.encode('utf-8')) - len(v2.encode('utf-8'))), '']
    for h in PART_HEADS:
        a, b = p2.get(h, ''), p3.get(h, '')
        lost, added = R4.invariance('<p>%s</p>' % a, '<p>%s</p>' % b)
        L += ['### %s v2 %d bytes (text) ; v3 %d bytes (text, tags removed) ; %+d' % (h, len(a.encode('utf-8')), len(b.encode('utf-8')),
                                                                                   len(b.encode('utf-8')) - len(a.encode('utf-8'))),
              '    tokens lost: %s' % (sorted(lost.items()) or 'none'), '    tokens added: %s' % (sorted(added.items()) or 'none')]
    L += ['', '### ### **v2 %d BYTES ; v3 %d BYTES ; v3 SHORTER %s.**' % (len(v2.encode('utf-8')), len(v3.encode('utf-8')),
                                                                       'YES' if len(v3.encode('utf-8')) < len(v2.encode('utf-8')) else 'NO')]
    put_txt('b646_desc_diff.txt', L)
    print(NL.join(L[2:]))


def desc_test(*a):
    """data/b646_desc_test.txt: the forbidden-content test rerun (b644's sealed `forbidden`), by planted text -- one plant per forbidden kind
    (a hit of that kind expected), the ceiling's denial (no hit), and v3 as banked (no hit) -- each case counted; and the composer's rule
    tests (tools/test_composer_b646.py) run and counted beside it."""
    R4 = _R4()
    cases = [('an act number', '<p>composed at b643.</p>', 'an act number'),
             ('a bank path', '<p>read from data/b643_premise_table.json.</p>', 'a bank path'),
             ('root arithmetic', '<p>root e583d138ea28f97569fe859a5826996bda1cebe83fac102cf9821b6a1b2c3d4.</p>', 'root arithmetic'),
             ('a provenance count', '<p>the rows are 209 cell and 1707 rule.</p>', 'a provenance count'),
             ('an outside collection', '<p>read beside %s.</p>' % (R4.OUTSIDE_NEEDLES[0] if R4.OUTSIDE_NEEDLES else 'X'), 'an outside collection'),
             ('a banned stem', '<p>a ' + 'ga' + 'p remains.</p>', 'a banned stem'),
             ('the unsupported sentence asserted', '<p>The programme shows that RH is proved.</p>', 'the unsupported sentence asserted'),
             ('the ceiling denied (no hit)', '<p>Not supported: that RH is proved; the corpus does not claim it.</p>', None),
             ('v3 as banked (no hit)', rd('b646_deposit_description.txt'), None)]
    L = ['b646 -- COMPONENT 4: THE DESCRIPTION`S FORBIDDEN-CONTENT TEST, RERUN BY PLANTED TEXT, AND THE COMPOSER`S RULE TESTS (%s)' % utc(), '']
    n = 0
    for i, (label, text, want) in enumerate(cases, 1):
        hits = R4.forbidden(text)
        ok = (any(k == want for k, _m in hits) if want else (not hits and bool(text)))
        n += ok
        L.append('  (%d) %-40s hits %s ; %s' % (i, label, [k for k, _m in hits][:4], 'PASS' if ok else '### FAIL'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_composer_b646.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    L += ['', '### THE FORBIDDEN-CONTENT TEST: %d of %d cases as wanted -- %s' % (n, len(cases), 'PASS' if n == len(cases) else 'FAIL'), '',
          '### THE COMPOSER`S RULE TESTS (tools/test_composer_b646.py), exit %d:' % r.returncode] + ['  ' + x for x in (r.stdout or '').rstrip(NL).split(NL)]
    L += ['', '### ### **FORBIDDEN-CONTENT %d of %d ; RULE TESTS EXIT %d.**' % (n, len(cases), r.returncode)]
    put_txt('b646_desc_test.txt', L)
    print(NL.join(L[-3:]))


# ================================================================================ THE FOURTH READER, (R256)(4): b644's form, carried
# ### A packet staged off D:\ at C:\reader_b646, a directory with no project memory: v3 as text, the three questions of (R254)(8), a lead and the
# ### full prompt; the command run by the author on the author's PowerShell; the answers scored by needles (b644's, imported) and by hand
# ### (data/b646_reader_d4_handread.txt, the seat's, written before the needles are read); the residue banked.
READER = dict(dir='C:/reader_b646', doc='description.txt', what='the description of a research deposit',
              questions=('What is claimed?', 'What is not claimed?', 'Which premise is refuted, and what replaced it?'))


def _v3_text(html):
    """v3 as plain text for a reader: a part's head on its own line, a paragraph a line, a list item a line marked '- ' (nested '  - ')."""
    out, depth = [], 0
    for tok in re.split(r'(<ul>|</ul>|<li>|</li>|<p>|</p>)', html):
        if tok == '<ul>':
            depth += 1
        elif tok == '</ul>':
            depth -= 1
        elif tok == '<li>':
            out.append(NL + '  ' * (depth - 1) + '- ')
        elif tok == '<p>':
            out.append(NL)
        elif tok in ('</li>', '</p>'):
            pass
        else:
            out.append(re.sub(r'<strong>(.*?)</strong>', r'== \1 ==', tok))
    t = ''.join(out)
    t = t.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    return NL.join(l.rstrip() for l in t.split(NL) if l.strip()).strip()


def _reader_lead():
    d = READER['dir'].replace('/', '\\')
    return ('Reader task follows. The packet is at %s\\packet\\ and your answers go to %s\\answers.txt. Read only the two packet files. Do not open '
            'any other file on this machine, do not run any command, and do not search the web. Write the answers file, report that it is '
            'written, and stop.' % (d, d))


def _reader_task():
    r = READER
    return (_reader_lead() + NL + NL +
            'You are an independent reader. You know nothing of the research programme the packet describes, and that is the point. The packet has '
            'two files: %s, %s, and questions.txt, 3 questions. Read the document and answer each question in your own words, from the document '
            'alone, in a few sentences each: say what the text says, not what you know of the mathematics, and say plainly where the text is '
            'unclear to you. Write the file %s\\answers.txt with exactly 3 sections, headed ANSWER 1:, ANSWER 2:, ANSWER 3:, each followed by '
            'your answer to that question; then a section headed UNCLEAR: listing any sentence of the document you could not follow, or the word '
            'none. Then stop.' % (r['doc'], r['what'], r['dir'].replace('/', '\\')))


def _reader_cmd():
    d = READER['dir'].replace('/', '\\')
    return ('Get-Content %s\\full_prompt.txt -Raw | claude -p --output-format json --allowedTools Read Glob Write --disallowedTools Bash PowerShell '
            'WebFetch WebSearch --permission-mode acceptEdits --setting-sources user --strict-mcp-config > %s\\reader_run.log 2> '
            '%s\\reader_run.err' % (d, d, d))


def reader_packet(*a):
    """data/b646_reader_d4_packet.txt and data/b646_reader_d4_packet/: v3 (relay data/b646_deposit_description.txt) as text with the three
    questions, staged at C:\\reader_b646 (refused if it exists and is not empty), the no-disclosure arm and the outside names checked, the
    command the author runs printed."""
    import b616_record as R6
    R4 = _R4()
    r = READER
    doc = _v3_text(rd('b646_deposit_description.txt'))
    if not doc.strip():
        sys.exit('### v3 IS EMPTY -- NOTHING WRITTEN')
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(r['questions']))
    task = _reader_task()
    nd = R6.nd_hits(doc + NL + qs + NL + task, R6.nd_sets())[0]
    outside = [n for n in R4.OUTSIDE_NEEDLES if n in doc]
    if any(nd.values()) or outside:
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b646_reader_d4_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in ((r['doc'], doc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    if not DRY:
        if os.path.exists(r['dir']) and os.listdir(r['dir']):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- NOT WRITTEN' % r['dir'])
        os.makedirs(r['dir'] + '/packet', exist_ok=True)
        for n_, t_ in (('packet/' + r['doc'], doc), ('packet/questions.txt', qs), ('lead.txt', _reader_lead()), ('full_prompt.txt', task)):
            _write(os.path.join(r['dir'], n_), (t_.rstrip(NL) + NL).encode('utf-8'))
    L = ['b646 -- THE FOURTH READER`S PACKET D4, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/%s %d bytes, sha256 %s ; packet/questions.txt ; lead.txt ; full_prompt.txt) ; banked: relay data/b646_reader_d4_packet/' % (
             r['dir'], r['doc'], len(doc.encode('utf-8')), sha(doc.encode('utf-8'))),
         '### the document: v3 (relay data/b646_deposit_description.txt) as text -- a part`s head as == HEAD ==, a list item as a line marked -',
         '### the questions, (R254)(8)`s three: %s' % ' / '.join(r['questions']),
         '### the no-disclosure arm: %s ; outside names: %s' % (dict(nd), outside or 'NONE'),
         '', '### the command, run by the author on the author`s PowerShell from %s, a directory with no project memory:' % r['dir'], '    ' + _reader_cmd()]
    put_txt('b646_reader_d4_packet.txt', L)
    print(NL.join(L[2:]))


def reader_score(*a):
    """data/b646_reader_d4_compare.txt and .json: the reader's answers copied from off D:\\, each scored by b644's needles (imported) and beside
    it the seat's hand reading (data/b646_reader_d4_handread.txt), both figures; question 2 refuses an assertion of the unsupported sentence."""
    R4 = _R4()
    r = READER
    src = os.path.join(r['dir'], 'answers.txt')
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b646_reader_d4_answers.txt'), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in re.finditer(r'^ANSWER (\d):\s*(.*?)(?=^ANSWER \d:|^UNCLEAR:|\Z)', t, re.M | re.S))
    N = R4._needles('d')
    lg = os.path.join(r['dir'], 'reader_run.log')
    # ### the author's PowerShell 5.1 `>` writes the log as UTF-16 with a BOM; read as UTF-8 the matcher cannot fire (b646, the seat's catch)
    lb = open(lg, 'rb').read() if os.path.exists(lg) else None
    lt = lb.decode('utf-16') if lb and lb[:2] in (b'\xff\xfe', b'\xfe\xff') else (lb.decode('utf-8', 'replace') if lb else '')
    ctl = bool(re.search(r'MEMORY\.md', 'x MEMORY.md y'.encode('utf-16').decode('utf-16')))
    mem = ('memory named in the run log: %s (read as %s, %d chars; the planted control fires: %s)' % (
        bool(re.search(r'MEMORY\.md|[\\/]memory[\\/]', lt)), 'UTF-16' if lb[:2] in (b'\xff\xfe', b'\xfe\xff') else 'UTF-8', len(lt), ctl)
           if lb else 'the run log absent')
    hr = rd('b646_reader_d4_handread.txt')
    hand = dict((int(m.group(1)), m.group(2).strip()) for m in re.finditer(r'^HAND (\d): (AGREE|DIFFER)', hr, re.M))
    L = ['b646 -- THE FOURTH READER D4: ANSWERS SCORED BY THE NEEDLES AND BY HAND (%s)' % utc(), '',
         '### the answers: relay data/b646_reader_d4_answers.txt, copied from %s ; the reader`s session: %s' % (src, mem), '']
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
          '### ### **BY THE NEEDLES %d OF %d ; BY HAND %s OF %d.**' % (n_ok, len(N), kh if hand else '### NOT READ', len(N))]
    put_txt('b646_reader_d4_compare.txt', L)
    put_json('b646_reader_d4_compare.json', dict(at=utc(), answers=res, needles=n_ok, hand=kh if hand else None, of=len(N),
                                                 unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


def zenodo_tags(*a):
    """data/b646_zenodo_tags.txt and .json: (R256)(4)(b) -- Zenodo's documentation of the HTML its description accepts, read at source (the
    page as fetched, in the scratchpad, its sha256 checked), the sentence quoted verbatim and the tag list parsed from it -- banked before the
    composer uses a tag."""
    import hashlib
    import html as H
    b = open(os.path.join(SP, ZEN_PAGE), 'rb').read()
    s = hashlib.sha256(b).hexdigest()
    if s != ZEN_SHA:
        sys.exit('### THE PAGE IS NOT THE PAGE READ (%s) -- NOTHING WRITTEN' % s)
    t = H.unescape(' '.join(re.sub(r'<[^>]+>', '', b.decode('utf-8')).split()))   # ### each tag name sits in <code>; removed, not spaced
    m = _need(r'(For string fields that allow HTML \(e\.g\. description, notes\), for security reasons, only the following tags are accepted: '
              r'([a-z, ]+)\.)', t, 'Zenodo`s accepted-tags sentence')
    tags = [x.strip() for x in m.group(2).split(',')]
    uniq = sorted(set(tags))
    L = ['b646 -- COMPONENT 4, (R256)(4)(b): ZENODO`S ACCEPTED HTML, READ AT SOURCE (%s)' % utc(), '',
         '### the page: %s (Zenodo`s REST API developer documentation), fetched by the seat with no identifier of the author in the request; '
         '%d bytes, sha256 %s' % (ZEN_URL, len(b), s),
         '### the sentence, verbatim: "%s"' % m.group(1),
         '### the tags it lists, in its order (%d, %d distinct; `caption` listed twice): %s' % (len(tags), len(uniq), ', '.join(tags)),
         '### no heading tag (h1-h6) is accepted: a part is headed as <p><strong>...</strong></p>; a list is <ul><li>...</li></ul>', '',
         '### ### **ACCEPTED TAGS %d: %s.**' % (len(uniq), ' '.join(uniq))]
    put_txt('b646_zenodo_tags.txt', L)
    put_json('b646_zenodo_tags.json', dict(at=utc(), url=ZEN_URL, sha256=s, sentence=m.group(1), tags=uniq))
    print(NL.join(L[2:]))


def _allowed_tags():
    tg = jl('b646_zenodo_tags.json').get('tags')
    if not tg:
        sys.exit('### ZENODO`S TAGS ARE NOT BANKED -- RUN `zenodo_tags` FIRST')
    return set(tg)


def carried(*a):
    """data/b646_composer_carried.txt: the carried composer, no rule of (R256)(4) applied, run on the table as it stood at v2 (relay
    V2_TABLE_REV), compared byte for byte with v2 (relay data/b644_deposit_description.txt)."""
    import hashlib
    h = compose_v3(rules=(), TR=_tr(V2_TABLE_REV))
    v2 = rd(V2)
    same = h == v2 and compose_carried(rules=(), TR=_tr(V2_TABLE_REV)) == v2   # ### the rules' composer with none applied, and the carried one
    L = ['b646 -- COMPONENT 4: THE CARRIED COMPOSER AGAINST v2, BYTE FOR BYTE (%s)' % utc(), '',
         '### the composer: relay tools/b646_record.py compose_v3, no rule applied; the table: relay %s:data/terminal_table.json' % V2_TABLE_REV,
         '### v2: relay data/%s, %d bytes, sha256 %s' % (V2, len(v2.encode('utf-8')), hashlib.sha256(v2.encode('utf-8')).hexdigest()),
         '### composed: %d bytes, sha256 %s' % (len(h.encode('utf-8')), hashlib.sha256(h.encode('utf-8')).hexdigest()),
         '', '### ### **THE CARRIED COMPOSER REPRODUCES v2 BYTE FOR BYTE: %s.**' % ('YES' if same else 'NO')]
    put_txt('b646_composer_carried.txt', L)
    print(NL.join(L[2:]))
    if not same:
        sys.exit(1)


# ================================================================================ COMPONENT 5: THE SEAT'S MEMORY, (R256)(5)
# ### The population, by the author's answer at Component 5 (data/b646_author_answers.txt): the seven project files MEMORY.md indexes. A sentence
# ### that is not a fact about the corpus (a deadline, a location, anything personal or about the local patent repository) is not a row and
# ### enters no bank -- its text is not written anywhere, its count alone is; the table reads corpus claims alone.
MEMFILES = (('state', 'project_state_cp4_cp5_b559_b576.md'), ('wave', 'project_deposit_wave_and_c4_next.md'),
            ('cascade', 'project_cascade_cp1_cp1b_b547_b558.md'), ('place', 'project_place_to_stand.md'),
            ('relay', 'project_relay_held_commit_push_procedure.md'), ('office', 'project_office_deadlines_2026-08.md'),
            ('patent', 'project_patent_repo_location.md'))
MEM_WHOLLY_NOT_CORPUS = {'office': 'USPTO deadlines and fees, personal', 'patent': 'the local patent repository and its location'}
MEMSP = os.path.join(SP, 'mem')
MEM_CHUNK = 110
_MSPLIT = re.compile(r'(?<=[.!?])["\'*)\]]*\s+(?=\S)')
MEM_RULE = [
    'THE UNIT: a sentence of a file`s body (and its frontmatter description), split where . ! or ? (and any closing quote, asterisk or '
    'bracket) meets whitespace; numbered file:line.n; every unit read.',
    'A ROW: a unit asserting a fact about the corpus -- the programme`s papers, ledgers, registry, kernels, tags, commits, the relay`s banks and '
    'tools, deposits and drafts, and what they contain. NOT A ROW: a deadline, a location on this machine, anything personal or about the local '
    'patent repository, and an instruction or reason that asserts no corpus fact; its text enters no bank, its count does.',
    'THE READING: a unit under a dated act heading (bNNN closed, State through bNNN) is read at that act`s commits; an undated unit at HEAD '
    '(relay fee57bfc, PLACE-papers 11a83b5); every fact in the unit -- figure, hash, name, line number, status, count -- against the lines cited, '
    'each repo@commit:path:N (a commit object itself repo@commit:COMMIT:1).',
    'MATCHES: every fact agrees with the lines cited. UNDERSTATES: the unit says less than the lines license (a thing called open, pending, '
    'unbuilt or absent that they show done, compiled, closed or present at the unit`s date). OVERREACHES: the unit states more than or other '
    'than the lines carry (a figure, hash, line number, name or status that differs; a conditional result stated without its condition; a thing '
    'called compiled, pushed, deposited or closed that they show was not). UNLICENSED: no corpus line reached bears on it. A unit of several '
    'facts takes the worst verdict among them (UNLICENSED, OVERREACHES, UNDERSTATES, MATCHES).',
    'ACTION: MATCHES none; UNDERSTATES or OVERREACHES RE-CUT: the sentence as the lines license it, and the repair made in the memory file with '
    'the repair printed; UNLICENSED RETIRE TO ERRATA: why (the unit leaves the file) or a work-order with a trigger.',
    'THE SEAT: every non-MATCHES row read whole by the seat against its lines; a MATCHES sample of 35 drawn by seed 646 read and printed.',
]


def _mem_units(text):
    ls = text.replace(chr(13), '').split(NL)
    fm = [i for i, l in enumerate(ls) if l.strip() == '---'][:2]
    out = []
    for i, l in enumerate(ls, 1):
        if len(fm) == 2 and i - 1 <= fm[1]:
            m = re.match(r'^description:\s*(.*)$', l)
            if m:
                out.append((i, 1, m.group(1).strip()))
            continue
        if l.strip():
            for j, s in enumerate([s for s in _MSPLIT.split(l.strip()) if s.strip()], 1):
                out.append((i, j, s.strip()))
    return out


def mem_rule(*a):
    """data/b646_seat_memory_rule.txt: the unit, the row, the reading and the verdicts, printed before any helper reader reads a row."""
    L = ['b646 -- COMPONENT 5: THE SEAT`S MEMORY THROUGH THE LICENSED-STATEMENT TABLE, THE RULE PRINTED BEFORE THE RUN (%s)' % utc(), '',
         '### the population, by the author`s answer at Component 5: the seven project files MEMORY.md indexes -- %s' % ', '.join(f for _, f in MEMFILES),
         '### wholly not corpus, by that answer, read and counted, no row and no text banked: %s' % '; '.join(
             '%s (%s)' % (dict(MEMFILES)[k], why) for k, why in MEM_WHOLLY_NOT_CORPUS.items()),
         '### the table: relay tools/licensed_table.py, five cells, four verdicts, every row HAND with its lines cited (check() refuses one without)', '']
    L += ['  (%d) %s' % (i + 1, r) for i, r in enumerate(MEM_RULE)]
    put_txt('b646_seat_memory_rule.txt', L)
    print(NL.join(L[2:]))


def mem_units(*a):
    """the scratchpad's mem/: each corpus file snapshotted (snap/<file>) with its sha256, its units written (units_<key>.tsv) and chunked for the
    helper readers (chunk_NN.tsv, about MEM_CHUNK units each, cut at line boundaries); the wholly-not-corpus files counted, nothing written."""
    import hashlib
    os.makedirs(os.path.join(MEMSP, 'snap'), exist_ok=True)
    idx, chunks = {}, []
    for k, fn in MEMFILES:
        b = open(os.path.join(K.MEMDIR, fn), 'rb').read()
        u = _mem_units(b.decode('utf-8'))
        idx[k] = dict(file=fn, sha256=hashlib.sha256(b).hexdigest(), bytes=len(b), units=len(u))
        if k in MEM_WHOLLY_NOT_CORPUS:
            continue
        _write(os.path.join(MEMSP, 'snap', fn), b)
        _write(os.path.join(MEMSP, 'units_%s.tsv' % k), ''.join('%s:%d.%d\t%d\t%s\n' % (k, ln, j, ln, s.replace('\t', ' ')) for ln, j, s in u).encode('utf-8'))
        cur, last = [], None
        for ln, j, s in u:
            if len(cur) >= MEM_CHUNK and ln != last:
                chunks.append((k, cur))
                cur = []
            cur.append((ln, j, s))
            last = ln
        if cur:
            chunks.append((k, cur))
    for n, (k, cur) in enumerate(chunks, 1):
        _write(os.path.join(MEMSP, 'chunk_%02d.tsv' % n), ''.join('%s:%d.%d\t%s\n' % (k, ln, j, s.replace('\t', ' ')) for ln, j, s in cur).encode('utf-8'))
    _write(os.path.join(MEMSP, 'index.json'), json.dumps(dict(at=utc(), files=idx, chunks=[dict(n=n, key=k, units=len(c), lines='%d-%d' % (
        c[0][0], c[-1][0])) for n, (k, c) in enumerate(chunks, 1)]), indent=1).encode('utf-8'))
    for k, v in idx.items():
        print('  %-8s %-46s units %4d ; sha256 %s' % (k, v['file'], v['units'], v['sha256'][:16]))
    for n, (k, c) in enumerate(chunks, 1):
        print('  chunk %02d: %s :%d-:%d, %d units' % (n, k, c[0][0], c[-1][0], len(c)))


MEM_FIX = {}        # ### uid -> dict of cells the seat corrects after its whole read (kind, verdict, licensed, cited, action)
MEM_READ = set()    # ### uids of the non-MATCHES rows the seat has read whole against their lines
MEM_SAMPLE = {}     # ### uid -> 'AGREE' / 'DISAGREE: why', the MATCHES sample the seat read
MEM_SAMPLE_N = 35


def _mem_rows():
    """[(uid, unit, row-or-None)] over every corpus unit, from the helper readers' rows_NN.tsv with the seat's corrections; faults listed."""
    import hashlib
    idx = json.loads(open(os.path.join(MEMSP, 'index.json'), encoding='utf-8').read())
    units, faults = collections.OrderedDict(), []
    for k, fn in MEMFILES:
        if k in MEM_WHOLLY_NOT_CORPUS:
            continue
        b = open(os.path.join(MEMSP, 'snap', fn), 'rb').read()
        if hashlib.sha256(b).hexdigest() != idx['files'][k]['sha256']:
            faults.append('%s: the snapshot differs from its index digest' % fn)
        for ln, j, s in _mem_units(b.decode('utf-8')):
            units['%s:%d.%d' % (k, ln, j)] = dict(key=k, file=fn, line=ln, text=s)
    got = collections.defaultdict(list)
    for c in idx['chunks']:
        p = os.path.join(MEMSP, 'rows_%02d.tsv' % c['n'])
        if not os.path.exists(p):
            faults.append('rows_%02d.tsv absent' % c['n'])
            continue
        for raw in io.open(p, encoding='utf-8'):
            f = raw.rstrip('\n').rstrip('\r').split('\t')
            if not f[0].strip() or f[0].startswith('#'):
                continue
            got[f[0].strip()].append(f)
    out = []
    for uid, u in units.items():
        fs = got.get(uid, [])
        if len(fs) != 1:
            faults.append('%s: %d judgements' % (uid, len(fs)))
            continue
        f = fs[0] + [''] * 6
        cell = dict(kind=f[1].strip(), verdict=f[2].strip(), licensed=f[3].strip(), cited=f[4].strip(), action=f[5].strip())
        cell.update(MEM_FIX.get(uid, {}))
        if cell['kind'] == 'NOTCORPUS':
            out.append((uid, u, None))
            continue
        if cell['kind'] != 'ROW':
            faults.append('%s: kind %r' % (uid, cell['kind']))
            continue
        row = dict(id=uid, source='memory/%s:%d' % (u['file'], u['line']), stated=u['text'], licensed=cell['licensed'], verdict=cell['verdict'],
                   action=cell['action'], by='HAND', cited=[c.strip() for c in cell['cited'].split(';') if c.strip()], fixed=uid in MEM_FIX)
        out.append((uid, u, row))
    extra = sorted(set(got) - set(units))
    if extra:
        faults.append('judgements for no unit: %s' % extra[:10])
    return out, faults, idx


def mem_check(*a):
    """the helper readers' rows read without writing: coverage, the table's faults, the counts, the non-MATCHES rows the seat has still to read."""
    import licensed_table as LT
    out, faults, idx = _mem_rows()
    rows = [r for _, _, r in out if r]
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    cnt = collections.Counter(r['verdict'] for r in rows)
    unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in MEM_READ]
    print('  units %d ; rows %d ; not rows %d ; faults %d ; %s ; non-MATCHES unread by the seat %d' % (
        len(out), len(rows), len(out) - len(rows), len(faults), dict(cnt), len(unread)))
    for f in faults[:40]:
        print('    ### ' + f)
    if 'list' in a:
        for r in rows:
            if r['verdict'] != 'MATCHES':
                print('  %s | %s | %s%s\n      STATED: %s\n      LICENSED: %s\n      CITED: %s\n      ACTION: %s' % (
                    r['id'], r['verdict'], r['source'], ' [READ]' if r['id'] in MEM_READ else '', r['stated'], r['licensed'], '; '.join(r['cited']),
                    r['action']))


def _mem_sample(rows):
    import random
    pool = sorted(r['id'] for r in rows if r['verdict'] == 'MATCHES')
    return sorted(random.Random('646-memory').sample(pool, min(MEM_SAMPLE_N, len(pool))))


def seat_memory(*a):
    """data/b646_table_seat_memory.txt and .json: (R256)(5) -- the seven files, every unit read, the corpus units rows of the table (HAND, cited),
    counts per file and by verdict, every row printed, each UNDERSTATES or OVERREACHES repair printed with its state in the live file; refuses on a
    fault, an uncovered unit, an unread non-MATCHES row or a sample not read as drawn. Not-corpus units are counted; their text is not written."""
    import hashlib
    import licensed_table as LT
    out, faults, idx = _mem_rows()
    rows = [r for _, _, r in out if r]
    faults += ['%s: %s' % (r['id'], '; '.join(LT.check(r))) for r in rows if LT.check(r)]
    unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in MEM_READ]
    smp = _mem_sample(rows)
    if faults or unread:
        sys.exit('### %d FAULTS, %d NON-MATCHES ROWS UNREAD BY THE SEAT -- NOTHING WRITTEN: %s %s' % (len(faults), len(unread), faults[:5], unread[:8]))
    if sorted(MEM_SAMPLE) != smp:
        sys.exit('### THE SAMPLE READ IS NOT THE SAMPLE DRAWN -- NOTHING WRITTEN: drawn %s' % smp)
    T = LT.table(rows)
    live = dict((fn, io.open(os.path.join(K.MEMDIR, fn), encoding='utf-8').read()) for _, fn in MEMFILES)
    L = ['b646 -- COMPONENT 5: THE SEAT`S MEMORY THROUGH THE LICENSED-STATEMENT TABLE ((R256)(5); the author`s answer at Component 5) (%s)' % utc(), '',
         '### the rule: relay data/b646_seat_memory_rule.txt, printed and committed before the run ; the table: relay tools/licensed_table.py',
         '### the readers: helper readers of this session, one per chunk (the scratchpad`s mem/chunk_NN.tsv), each row then judged by the seat: '
         'every non-MATCHES row read whole (%d corrected), a MATCHES sample of %d (seed 646) read, %d agree' % (
             sum(1 for r in rows if r['fixed']), len(smp), sum(1 for v in MEM_SAMPLE.values() if v == 'AGREE')), '',
         '### PER FILE (sha256 of the file as read ; units read ; rows ; not rows):']
    for k, fn in MEMFILES:
        n_u = idx['files'][k]['units']
        n_r = sum(1 for _, u, r in out if r and u['key'] == k)
        c = collections.Counter(r['verdict'] for _, u, r in out if r and u['key'] == k)
        L.append('  %-46s %s ; units %4d ; rows %4d ; not rows %4d ; %s' % (fn, idx['files'][k]['sha256'][:16], n_u, n_r, n_u - n_r,
                                                                         ', '.join('%s %d' % (v, c[v]) for v in LT.VERDICTS)))
    cnt = collections.Counter(r['verdict'] for r in rows)
    L += ['', '### THE MATCHES SAMPLE READ BY THE SEAT (%d):' % len(smp)] + ['  %s : %s' % (i, MEM_SAMPLE[i]) for i in smp]
    L += ['', '### THE REPAIRS, EACH UNDERSTATES OR OVERREACHES ROW (the sentence before ; the re-cut ; in the live file):']
    rep = []
    for r in rows:
        if r['verdict'] in ('UNDERSTATES', 'OVERREACHES'):
            new = r['action'][len('RE-CUT: '):] if r['action'].startswith('RE-CUT: ') else None
            fn = r['source'].split('/', 1)[1].rsplit(':', 1)[0]
            st = ('APPLIED' if new and new in live[fn] and r['stated'] not in live[fn] else ('### NOT APPLIED' if new else '### A WORK-ORDER'))
            rep.append(dict(id=r['id'], before=r['stated'], after=new, state=st))
            L += ['  %s %s -- %s' % (r['id'], r['verdict'], st), '      BEFORE: ' + r['stated'], '      AFTER:  ' + (new or r['action'])]
    if not rep:
        L.append('  NONE')
    L += ['', '### EVERY ROW (id | verdict | stated | licensed | cited | action):']
    for r in rows:
        L += ['  %s | %s | %s' % (r['id'], r['verdict'], r['stated']), '      LICENSED: %s' % r['licensed'], '      CITED: %s' % '; '.join(r['cited']),
              '      ACTION: %s' % r['action']]
    na = sum(1 for x in rep if x['state'] != 'APPLIED')
    L += ['', '### ### **FILES %d ; UNITS READ %d ; ROWS %d ; NOT ROWS %d -- MATCHES %d, UNDERSTATES %d, OVERREACHES %d, UNLICENSED %d ; REPAIRS %d, '
              'NOT APPLIED %d ; FAULTS 0.**' % (len(MEMFILES), sum(v['units'] for v in idx['files'].values()), len(rows),
                                               sum(v['units'] for v in idx['files'].values()) - len(rows), cnt['MATCHES'], cnt['UNDERSTATES'],
                                               cnt['OVERREACHES'], cnt['UNLICENSED'], len(rep), na)]
    put_txt('b646_table_seat_memory.txt', L)
    put_json('b646_table_seat_memory.json', dict(at=utc(), files=idx['files'], counts=dict(cnt), table=T, rows=rows, repairs=rep, sample=MEM_SAMPLE))
    print(L[-1])


# ================================================================================ THE DRAFT'S DESCRIPTION, (R256)(4): b644's route, carried
# ### b639's http (the token in the Authorization header alone, the User-Agent naming the act); the draft's description replaced by v3's bank,
# ### every other metadata key carried, no file touched, nothing published; read back once; HELD.
ZRES = 'b646_zenodo.json'


def _jx(b):
    try:
        return json.loads(b.decode('utf-8'))
    except Exception:
        return None


def _straight(s):
    return s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def _zmerge(cells):
    R = jl(ZRES) if os.path.exists(os.path.join(D, ZRES)) else {}
    R.update(cells)
    put_json(ZRES, R)


def z_desc(*a):
    """data/b646_zenodo_desc.txt: draft K.DRAFT read once (unsubmitted, or nothing done) and its metadata PUT once with the description v3's bank
    (relay data/b646_deposit_description.txt), every other key carried; the prior description's bytes and digest banked, not its text; the file
    list before banked for the read-back; nothing published. Refuses to run twice."""
    import hashlib
    import b639_record as R39
    if not R39._tok():
        sys.exit('### THE TOKEN IS NOT SET -- NO CALL MADE')
    if os.path.exists(os.path.join(D, ZRES)) and jl(ZRES).get('desc'):
        sys.exit('### THE DESCRIPTION HAS BEEN REPLACED -- IT DOES NOT RUN TWICE')
    v3 = open(os.path.join(D, 'b646_deposit_description.txt'), 'rb').read().decode('utf-8')
    base = '%s/deposit/depositions/%s' % (K.API if hasattr(K, 'API') else 'https://zenodo.org/api', K.DRAFT)
    st, b = R39.http('GET', base)
    d = _jx(b) or {}
    if st != 200 or d.get('submitted') or str(d.get('id')) != K.DRAFT:
        sys.exit('### THE DRAFT IS NOT AN UNSUBMITTED %s (HTTP %d) -- NOTHING DONE' % (K.DRAFT, st))
    md = dict(d.get('metadata') or {})
    old = md.get('description') or ''
    files = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    md['description'] = v3
    sp, bp = R39.http('PUT', base, body={'metadata': md})
    hx = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
    L = ['b646 -- THE ROUTE, THE DRAFT`S DESCRIPTION REPLACED BY v3 (%s)' % utc(), '',
         '### GET the draft %s : HTTP %d ; state %s ; submitted %s ; %d files' % (K.DRAFT, st, d.get('state'), d.get('submitted'), len(files)),
         '### the description before : %d bytes, sha256 %s ; v2`s bank %d bytes, sha256 %s ; the draft held v2: %s' % (
             len(old.encode('utf-8')), hx(old), len(rd(V2).encode('utf-8')), hx(rd(V2)), old == rd(V2) or _straight(old) == _straight(rd(V2))),
         '### PUT metadata (the description v3`s bank, %d bytes, sha256 %s ; %d keys carried) : HTTP %d' % (len(v3.encode('utf-8')), hx(v3), len(md), sp),
         '', '### ### **CALLS 2 ; THE PUT %s ; NO FILE TOUCHED ; NOTHING PUBLISHED.**' % ('ACCEPTED' if sp in (200, 201) else '### REFUSED HTTP %d' % sp)]
    put_txt('b646_zenodo_desc.txt', L)
    _zmerge(dict(desc=dict(get=st, put=sp, before_bytes=len(old.encode('utf-8')), before_sha256=hx(old), v3_sha256=hx(v3), files_before=files,
                           at=utc())))
    print(NL.join(L[2:]))


def z_read(*a):
    """data/b646_zenodo_read.txt: the draft read back once -- identifier, title, version, state; the description against v3's bank byte for byte and
    digest for digest (and up to quote straightening); the file list against the one z_desc banked, name, checksum and size."""
    import hashlib
    import b639_record as R39
    base = 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT
    st, b = R39.http('GET', base)
    d = _jx(b) or {}
    md = d.get('metadata') or {}
    bank = open(os.path.join(D, 'b646_deposit_description.txt'), 'rb').read().decode('utf-8')
    back = md.get('description') or ''
    exact = back == bank
    dig = hashlib.sha256(back.encode('utf-8')).hexdigest() == hashlib.sha256(bank.encode('utf-8')).hexdigest()
    fb = (jl(ZRES).get('desc') or {}).get('files_before') or []
    fa = [dict(name=f.get('filename'), checksum=f.get('checksum'), size=f.get('filesize')) for f in d.get('files') or []]
    key = lambda x: sorted((f['name'], f['checksum'], f['size']) for f in x)
    files_same = bool(fb) and key(fa) == key(fb)
    L = ['b646 -- THE ROUTE, THE DRAFT READ BACK AFTER THE DESCRIPTION`S REPLACEMENT (%s)' % utc(), '',
         '### GET the draft : HTTP %d ; identifier %s ; state %s ; submitted %s ; title %s ; version %s' % (
             st, d.get('id'), d.get('state'), d.get('submitted'), md.get('title'), md.get('version')),
         '### the description : %d characters back against the bank`s %d ; byte for byte %s ; digest for digest %s ; equal up to quote straightening %s' % (
             len(back), len(bank), exact, dig, _straight(back) == _straight(bank)),
         '### the files : %d back against %d before the PUT ; name, checksum and size the same %s' % (len(fa), len(fb), files_same), '',
         '### ### **THE DESCRIPTION BYTE FOR BYTE %s AND DIGEST FOR DIGEST %s ; THE FILES UNTOUCHED %s ; THE DRAFT %s SUBMITTED %s -- NOTHING '
         'PUBLISHED.**' % (exact, dig, files_same, d.get('id'), d.get('submitted'))]
    put_txt('b646_zenodo_read.txt', L)
    _zmerge(dict(read=dict(get=st, id=d.get('id'), state=d.get('state'), submitted=d.get('submitted'), exact=exact, digest=dig,
                           straight=_straight(back) == _straight(bank), files_same=files_same, n_files=len(fa), at=utc())))
    print(NL.join(L[2:]))


def z_hold(*a):
    """data/b646_zenodo_hold.txt: the draft HELD, (R256)(4): its state read once and banked; publish is the author's word in a later act."""
    import b639_record as R39
    st, b = R39.http('GET', 'https://zenodo.org/api/deposit/depositions/%s' % K.DRAFT)
    d = _jx(b) or {}
    L = ['b646 -- THE DRAFT HELD, (R256)(4) (%s)' % utc(), '', '### the draft %s : HTTP %d ; state %s ; submitted %s ; nothing published; v3 sent to '
         'the author as a file (relay data/b646_deposit_description.txt)' % (K.DRAFT, st, d.get('state'), d.get('submitted'))]
    put_txt('b646_zenodo_hold.txt', L)
    _zmerge(dict(hold=dict(id=K.DRAFT, state=d.get('state'), submitted=d.get('submitted'), at=utc())))
    print(L[-1])


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b646_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
