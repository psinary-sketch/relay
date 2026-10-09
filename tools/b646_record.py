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
COMP_FIX = {}       # ### row id -> (grade, stated_as, reason[, route]): the seat's corrections, each after its whole read of the row
COMP_SAMPLE = {}    # ### row id -> 'AGREE' | 'CORRECTED': MATCHES rows drawn with seed 646 and read whole by the seat
COMP_READ_ALL = set()   # ### the companions whose every non-MATCHES row the seat has read whole


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


def _comp_rows(name):
    import licensed_table as LT
    ls = _comp_lines(name)
    recs, faults = _comp_records(name)
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
        src = _show(PP, PRE_PP, 'day1/%s.md' % name)
        L = ['b646 -- COMPONENT 2, (R256)(3): %s AT ITS PATCH LABEL %s THROUGH THE INTAKE FORM, EVERY CLAIM A ROW (tools/licensed_table.py) (%s)' % (
            name, lab, utc()), '',
            '### the document: PLACE-papers day1/%s.md at %s, %d lines, sha256 %s' % (name, PRE_PP, len(lines_of(src)), sha(src.encode('utf-8'))),
            '### the form: b628`s intake (relay tools/b628_record.py `intake`, tools/b628_worklist.py); the rows read by one helper reader of this '
            'session from the brief (the scratchpad`s companion_brief.md, `established` narrowed per b645`s defect (d), F5 naming both theorems '
            'per its (e)); the verdict by the mapping alone (relay data/b646_mapping.txt), never by a reader; every non-MATCHES row read whole by '
            'the seat (%d corrected); the stated-as rule moved %d rows' % (sum(1 for r in rows if r['fixed']), sum(1 for r in rows if r['refined'])), '']
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


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b646_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
