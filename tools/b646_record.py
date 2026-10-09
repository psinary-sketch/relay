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
RULES = ()   # ### the composition rules of (R256)(4), each added through the Edit tool with its test


def _R4():
    import b644_record as R4
    return R4


def _tr(rev=None):
    if rev is None:
        T = jl('terminal_table.json')
    else:
        T = json.loads(_show(RELAY, rev, 'data/terminal_table.json'))
    return dict(((r['repo'], r['name'].split('.')[-1]), r) for r in T.get('rows') or [])


def compose_v3(rules=None, TR=None):
    """the description's HTML: b644's composer carried, with the rules of (R256)(4) named in `rules` applied (default: RULES)."""
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
    same = h == v2
    L = ['b646 -- COMPONENT 4: THE CARRIED COMPOSER AGAINST v2, BYTE FOR BYTE (%s)' % utc(), '',
         '### the composer: relay tools/b646_record.py compose_v3, no rule applied; the table: relay %s:data/terminal_table.json' % V2_TABLE_REV,
         '### v2: relay data/%s, %d bytes, sha256 %s' % (V2, len(v2.encode('utf-8')), hashlib.sha256(v2.encode('utf-8')).hexdigest()),
         '### composed: %d bytes, sha256 %s' % (len(h.encode('utf-8')), hashlib.sha256(h.encode('utf-8')).hexdigest()),
         '', '### ### **THE CARRIED COMPOSER REPRODUCES v2 BYTE FOR BYTE: %s.**' % ('YES' if same else 'NO')]
    put_txt('b646_composer_carried.txt', L)
    print(NL.join(L[2:]))
    if not same:
        sys.exit(1)


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b646_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
