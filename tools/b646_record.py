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
    hits = ER.scan(rows)
    L = ['b646 -- THE ACT`S COMMAND BANK AND THE ARM G-EDIT-ROUTE`S READING ((R256)(2); tools/edit_route.py) (%s)' % utc(), '',
         '### the source: the seat`s session transcript %s from its first user line carrying %r, and its subagents` transcripts (%s) at or '
         'after that line`s timestamp %s' % (os.path.basename(SESSION), K.ANCHOR, SUBAGENTS.rsplit('/', 2)[-2] + '/subagents', rows[0]['ts']),
         '### commands read: %d (seat %d ; helper readers %d) ; by tool %s' % (
             len(rows), sum(1 for r in rows if r['src'] == 'seat'), sum(1 for r in rows if r['src'] != 'seat'),
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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b646_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
