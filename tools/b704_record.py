# -*- coding: utf-8 -*-
"""b704_record.py -- THE ACT'S RECORD TOOL, b704 under (R314).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b704 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers (_deps, the primed names; _defect_short, its act at the call; the span line from the mirror bank chain) are IMPORTED from
### tools/b703_record.py (sealed at b703 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b704 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b704_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b704_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited
import b703_record as P3           # noqa: E402  ### b703's repaired readers, imported unedited (its import rebinds R to b703: rebound again below)

ACT, PREV = 'b704', 'b703'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b703 ran and closed in ANOTHER session (e5bcf1d0); this act opens a new one (fb68aaef) -- b701's form: the
# ### previous window from b703's anchor in its own session to that session's end
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
FACE = os.path.join(D, 'b704_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b704_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b703_closing_push_out.txt', 'b675_corrigenda.txt', 'glossary.txt')
R.N5_RELAY_TOOLS = ()
R.ROOT_EXCLUDE = re.compile(r'^b704_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')

_R_anchor_ts = P3._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap)


def _anchor_ts(anchor, session=None):
    """b698's _anchor_ts bound its session at definition (b699's trap 1): this one reads this act's session unless another is named."""
    return _R_anchor_ts(anchor, session or SESSION)


R._anchor_ts = _anchor_ts


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='3b6de278' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S REPAIRED READERS, IMPORTED
_deps = P3._deps                   # ### the primed names read (b703 (f)); R._deps already rebound to it by b703's import
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen = R.rowgen
answers = R.answers


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R314)(8); b703's form)
def branches(*a):
    """`branches before`: data/b704_branches_before.json -- b698's route, carried (every branch (R314)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b704_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the two kernel branches of the prompt read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b704_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    kb = []
    rh = R._remote_heads(K.KERNEL_DIR)
    for b in K.KERNEL_BRANCHES_PROMPT:
        lt = g(K.KERNEL_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
        kb.append((b, lt[:7] or 'ABSENT', (rh.get(b) or '')[:7] or 'ABSENT'))
    L = ['%s -- STEP ZERO, (R314)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b704_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. The kernel branches widening-b701 and epstein-b703 raised as one',
         '### prompt before any kernel delete ((R314)(8)), read beneath.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### the kernel branches of the prompt at the close of step zero: %s' % ' ; '.join('%s local %s remote %s' % x for x in kb)]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, kernel_branches=kb))
    print(NL.join(L[7:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R314)(1)
WH = ('*Appended 2026-10-22 by b704 to b703’s entry (:9888), under `(R314)`(1) -- b703 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b703_closing.txt):*')
WB = (' “b703 closed: relay 3ee79ba0, PLACE-papers 1532695; suite 138 of 138; root 3b6de278d4eb0467…; 4 prompts answered; 12 defects” '
      '(data/b703_closing.txt :1); the closing commit 295e53f0 pushed alone after the line was written and read back equal at the remote '
      '(data/b703_closing_push_out.txt :5). classK widened at one token: H2SignWide.lean :59 le_rfl -> one_ne_zero on widening-b701, run '
      '39700585515 DERIVES at 89 of 89 (read again by its run id once the axioms reader read primed names), merged and tagged SIDE-explicit-formula '
      'v0.36 = dfadc8c; ten names graded at the standard three, every salt-check passing -- acDeriv_of_contDiff_two, the three inclusions classK ⊆ '
      'classKsum ⊆ classK’, h2_sign’_imp_h2_sign, h2_sign’_imp_rh, rh_imp_h2_sign_sum, h2_sign_sum_imp_h2_sign and h2_sign_sum_iff_rh DERIVES, '
      'paperFT_finset_sum INTERFACES on its hypotheses hf and hs, the inclusions’ E0 reading PREDICATE-UNLISTED and entered as W-ORD-E0-MET-CLASSK '
      '(data/b703_widening_grade.txt); the glossary’s classK’ row written. The Epstein zeta of x² + xy + 6y² a Lean object: Schema/EpsteinZQ.lean '
      'merged and tagged v0.37 = 38e2734 naming v0.36, run 39703864050 DERIVES at 109 of 109, its four premises ZQContinuation, ZQZeros, '
      'ZQExplicitFormula and ZQPremises printed beside their names over Wide.WideConfig, nothing about a zero stated as proved '
      '(data/b703_epstein_grade.txt). b681’s certified zeros of Q0 counted by real part by the named reader after both hashes agreed: 163 rows, '
      '17 off the line and 146 on it, binned (1/2, 0.6] 0, (0.6, 0.75] 5, (0.75, 7/8] 10, (7/8, 1) 2, fifteen in (1/2, 7/8], the lowest in height '
      '0.79799715717868013876 + 29.55176109862911459913 i, the control reproducing 163 rows and ρ₀’s real part (data/b703_q0_band.txt), the four '
      'registrations committed alone before any number (relay b8a36309). The pins priced: the closure join one dispatch at SIDE-explicit-formula’s '
      'pin (Lean v4.34.0-rc1, Mathlib de5ce8a9) rebuilding SIDE-lv-conservation’s 15 files; the interval vendoring one dispatch over 86 files and '
      '44 days, waiting on BINDER-PROVENANCE (data/b703_pins.txt). The four standing arms G-CORRESPONDENCE-CURRENCY, G-README-CURRENCY, '
      'G-PARTNER-COPIES and G-SISTER-PINS added, b703’s figures 0, 11, 131, 0 the baseline (data/b703_standing_figures.txt); the quote arm '
      'branched by the kind of cut and the mirror bank’s span line read from the chain (data/b703_tool_repairs.txt); four annotations and four '
      'orders at OPEN_TRAILS :15492-:15506. b702’s two items after its root answered by the generated corrigendum at FINDINGS :9874 (corrigenda '
      'rows (22)-(23)); b702’s weight at :9872. The entry at FINDINGS :9888, the trail at OPEN_TRAILS :15508; the root 3b6de278 over 83 banks '
      'chained from 56312178 (data/b703_act_root.json); suite 138 of 138 pre-push and post-push with no failure carried (data/b703_checks.txt; '
      'data/b703_checks_postpush.txt); all eight scores held (data/b703_scores_close.json); the sealed tools’ hashes equal at the close, 11 of 11; '
      'the citation check 105 cites, 105 OK; twelve defects (a)-(l), (d) and (e) the navigator’s (data/b703_defects.txt); the mirror '
      'mirror-refresh-2026-10-21-b703.zip, sha256 5263fb6f, CLEAN on all three clauses, its span line reading b702 as the last export '
      '(data/b703_mirror.txt); the scratch clone deleted by its verified absolute path. One item after the closing, entered by this act’s '
      'corrigendum: the project-state memory file read whole. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B703_ENTRY,
         check=[('FINDINGS.md', K.B703_ENTRY, '## classK widened at SIDE-explicit-formula v0.36'), ('OPEN_TRAILS.md', K.B703_TRAIL, '### b703')],
         dry=dry)


# ================================================================================ COMPONENT 2: THE DISPATCH, THE RUNNER (b698's routes; b703's runner)
EF = K.KERNEL_DIR
dispatch, runstatus = R.dispatch, R.runstatus
STD3 = P3.STD3
runner = P3.runner                 # ### b703's runner by copy, its names read at the call from b703's module: rebound below
NODES_B704 = os.path.join(D, 'b704_nodes_zeta.txt')
NODES_B702 = os.path.join(D, 'b702_nodes_zeta.txt')
CANDIDATES = ('SIDEExplicitFormula.B321.h2_sign_sum_iff_rh', "SIDEExplicitFormula.B321.h2_sign'_imp_rh")   # ### (R314)(3), the node prompt
PROBE_BRANCH = 'probe-b704'


def nodesdiff(*a):
    """data/b704_nodes_diff.txt: b704's list against b702's, line for line (difflib, autojunk off) -- every row unchanged but its tag."""
    import difflib
    old = rd(NODES_B702).replace(chr(13), '').split(NL)
    new = rd(NODES_B704).replace(chr(13), '').split(NL)
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    L = ['%s -- (R314)(3): THE NODE LIST`S SUCCESSOR AGAINST b702`S, LINE FOR LINE (%s)' % (ACT, utc()), '',
         '### rows are the opcodes of the two lists (difflib, autojunk off): the kind | b702`s lines | b704`s lines | the lines. Every row of',
         '### b702`s list unchanged but its tag is the order; the head`s comment block is b704`s own.', '']
    ch = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        ch.append((op, i1, i2, j1, j2))
        L += ['  %s | :%d-:%d | :%d-:%d' % (op, i1 + 1, i2, j1 + 1, j2)] + ['      - %s' % x for x in old[i1:i2]] + ['      + %s' % x for x in new[j1:j2]]
    rec_old = [x for x in old if x and not x.startswith('#')]
    rec_new = [x for x in new if x and not x.startswith('#')]
    pins = ([x for x in old if x.startswith('# pin:')], [x for x in new if x.startswith('# pin:')])
    comm = [c for c in ch if not all(x.startswith('#') for x in new[c[3]:c[4]] + old[c[1]:c[2]])]
    L += ['', '### ### **RECORD LINES b702 %d ; b704 %d ; EQUAL %s ; THE PIN %s -> %s ; CHANGES OUTSIDE COMMENT LINES %d.**' % (
        len(rec_old), len(rec_new), rec_old == rec_new, pins[0], pins[1], len(comm))]
    if 'dry' not in a:
        put_txt('%s_nodes_diff.txt' % ACT, L)
    print(NL.join(L[-1:]))


def _probe_parts():
    """chain_page's own selection at the b704 list's pin: (names, corr_names, watch, the probe's module imports)."""
    import chain_page as CP
    CP.VARIANT = None
    CP.PIN_TAG, CP.PIN = CP.node_pin(NODES_B704)
    nodes, _drops, _corr, marks = CP.read_nodes(NODES_B704)
    names = [x['name'] for x in nodes]
    corr = CP.corr_select(CP.record_rows(), names, marks, None)
    return CP, names, corr, ['SIDEExplicitFormula.RegisterDepth']


def probe(*a):
    """`probe [dry]`: the probe text by tools/chain_page.py's probe_text at the b704 list's pin (v0.37), its cells the list's names, the two
    candidate nodes of (R314)(3) and the Correspondence names, the node set the list's names and the candidates -- written in run_probe's form
    (chain_page.py :268-:271) as the root CircuitClosure.lean of the probe branch's working tree, which must be checked out at probe-b704 cut
    from v0.37 with no tracked change. data/b704_probe.txt: the text's sha256, its cells, the lake target (the probe's own module imports)."""
    import hashlib
    CP, names, corr, watch = _probe_parts()
    br = g(EF, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    base = g(EF, 'rev-parse', 'HEAD').strip()
    dirty = g(EF, 'status', '--porcelain', '--untracked-files=no').strip()
    cells = names + [c for c in CANDIDATES if c not in names] + corr
    text = CP.probe_text(cells, names + [c for c in CANDIDATES if c not in names], watch)
    mods = [l.split()[1] for l in CP.probe_imports().split(NL) if l.startswith('import ')]
    target = ' '.join(mods)
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    ok = br == PROBE_BRANCH and base == K.EF_V037 and not dirty and CP.PIN == K.EF_V037
    L = ['%s -- (R314)(3): THE FACES PROBE, ITS TEXT BY THE GENERATOR AND ITS TARGET (%s)' % (ACT, utc()), '',
         '### the generator: relay tools/chain_page.py probe_text at the list relay data/b704_nodes_zeta.txt (pin %s = %s); the kernel checkout %s at %s,' % (
             CP.PIN_TAG, (CP.PIN or '')[:7], br, base[:7]),
         '### tracked changes %s. The text is written in run_probe`s form as the probe branch`s root CircuitClosure.lean; the workflow`s closure' % (dirty or 'NONE'),
         '### step (build-module.yml :98-:111) prepends one import per target module and runs it, its output out/closure_log.txt.',
         '  cells %d (the list`s names %d ; the candidates %d ; the Correspondence names %d) ; the node set %d ; the watch %s' % (
             len(cells), len(names), len([c for c in CANDIDATES if c not in names]), len(corr), len(names) + len([c for c in CANDIDATES if c not in names]), watch),
         '  the text: %d bytes ; %d lines ; sha256 %s' % (len(text.encode('utf-8')), text.count(NL), sha),
         '  the lake target (the probe`s module imports at the pin, %d): %s' % (len(mods), target),
         '', '### ### **THE PROBE TEXT %s ; sha256 %s ; CELLS %d ; TARGET MODULES %d ; THE CHECKOUT AT %s %s.**' % (
             'WRITTEN' if ok and 'dry' not in a else ('NOT WRITTEN (dry)' if ok else '### NOT WRITTEN, THE CHECKOUT NOT AS ORDERED'), sha[:16], len(cells),
             len(mods), PROBE_BRANCH, 'FROM v0.37' if ok else '### NOT AS ORDERED')]
    if ok and 'dry' not in a:
        import io as _io
        _io.open(os.path.join(EF, 'CircuitClosure.lean'), 'w', encoding='utf-8', newline=NL).write(text)
        put_txt('%s_probe.txt' % ACT, L)
        put_json('%s_probe.json' % ACT, dict(at=utc(), sha256=sha, cells=cells, nodes=names, candidates=list(CANDIDATES), corr=corr, target=target,
                                            pin=CP.PIN, branch=br, base=base))
    print(NL.join(L[-3:]))


# ================================================================================ STEP ZERO: THE READ RULE'S SORT, (R314)(2)
def _read_calls(path, since=None):
    """every Read call of a session transcript: (transcript line, time, file_path, offset, limit), from `since` (an ISO time) on."""
    out = []
    for i, raw in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        ts = o.get('timestamp') or ''
        if since and ts < since:
            continue
        for c in ((o.get('message') or {}).get('content') or []) if isinstance((o.get('message') or {}).get('content'), list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                out.append((i, ts, inp.get('file_path', ''), inp.get('offset'), inp.get('limit')))
    return out


def _nlines(p):
    try:
        return len(open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '').rstrip(NL).split(NL))
    except OSError:
        return None


def readsort(*a):
    """data/b704_read_sort.txt: (R314)(2) -- each read-rule breach of b703 ((k) thirteen calls, (l), (m)) with whether its path, offset and
    limit leave a trace in a bank the suite can read: the act's command bank (data/b703_commands.txt) and its read bank
    (data/b703_read_calls.txt), each by path and line; and the arm the traceable ones would take. Nothing is written but the sort's bank."""
    rb = rdn('b703_read_calls.txt').split(NL)
    cb = rdn('b703_commands.txt').split(NL)
    off = [(i + 1, l) for i, l in enumerate(rb) if '| ### AN OFFENCE |' in l and re.match(r'^  \d+ \|', l)]
    calls = dict((c[0], c) for c in _read_calls(PREV_SESSION_PATH))
    rows = []
    for n, l in off:
        tl = int(l.split('|')[0].strip())
        c = calls.get(tl)
        letter = 'l' if tl == 10815 else 'k'
        incb = [j + 1 for j, x in enumerate(cb) if c and c[2] and c[2] in x]
        rows.append((letter, tl, c[1] if c else '-', c[2] if c else l.split('|')[-1].strip(), c[3] if c else '?', c[4] if c else '?',
                     _nlines(c[2]) if c else None, 'data/b703_read_calls.txt :%d' % n,
                     ('NONE (a command naming the path at data/b703_commands.txt :%s, not this call)' % incb[0]) if incb else 'NONE'))
    closing = '2026-10-22T03:06:13'
    mem = [c for c in _read_calls(PREV_SESSION_PATH, since=closing) if (_nlines(c[2]) or 0) >= 200 and not (c[3] and c[4])]
    for c in mem:
        n_ = _nlines(c[2])
        rows.append(('m', c[0], c[1], c[2], c[3], c[4], n_, 'NONE (after the read bank`s stamp 02:25:02Z and after the closing)', 'NONE'))
    L = ['%s -- STEP ZERO, (R314)(2): THE READ RULE`S BREACHES AT b703, SORTED BY TRACE (%s)' % (ACT, utc()), '',
         '### the rule: data/b698_rules.txt row (2), whole under two hundred lines, by offset and limit otherwise, memory files included. The author`s',
         '### word of 2026-10-18 (relay data/b683_ferry.txt :5): "arms for the traceable ones, the seat sorts them". Rows are breaches: the letter |',
         '### the transcript line in b703`s session (%s) | the time | the path | offset | limit | the file`s lines now | its trace in the read bank |' % K.PREV_SESSION[:8],
         '### its trace in the command bank. A breach is TRACEABLE where a bank the suite reads carries its path at a line; the offset and limit',
         '### are carried by the read bank`s row form (a row is a call without both), not as values.', '']
    for r in rows:
        L.append('  (%s) | %s | %s | %s | offset %s | limit %s | lines %s | %s | %s | %s' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8],
                 'TRACEABLE' if not r[7].startswith('NONE') else 'NOT IN A BANK'))
    tr = [r for r in rows if not r[7].startswith('NONE')]
    nt = [r for r in rows if r[7].startswith('NONE')]
    L += ['', '### THE SORT:',
          '  TRACEABLE %d ((k) %d, (l) %d): each a row of relay data/b703_read_calls.txt, written by the record tool from the session transcript at the' % (
              len(tr), sum(1 for r in tr if r[0] == 'k'), sum(1 for r in tr if r[0] == 'l')),
          '    root; the command bank (data/b703_commands.txt) carries commands, not Read calls, so it traces none of them.',
          '  NOT IN A BANK %d ((m)): made after the closing, after every bank of b703 was written; the session transcript alone carries it.' % len(nt),
          '', '### THE ARM IT WOULD WRITE (raised before any arm is written, "write the arm" / "keep it prose"):',
          '  G-READ-RULE-STANDING -- a standing arm reading the act`s own read bank (data/b<act>_read_calls.txt, written at the root from the',
          '    session transcript): it fails on any row ### AN OFFENCE (a Read call of a file of two hundred lines or more without both an offset and',
          '    a limit) not lettered in the act`s defects bank; and it reads the previous act`s session from its closing push to that session`s end',
          '    (the window the command bank already reads for commands), so a breach after the closing, as (m), is printed and lettered by the next',
          '    act. Its NEG control: a planted offence row unlettered fails it. b703`s act arm G-READ-RULE read the bank within the act alone.', '',
          '### ### **BREACHES %d ; TRACEABLE %d ((k) %d, (l) %d) ; NOT IN A BANK %d ((m) %d) ; THE COMMAND BANK TRACES 0.**' % (
              len(rows), len(tr), sum(1 for r in tr if r[0] == 'k'), sum(1 for r in tr if r[0] == 'l'), len(nt), len(nt))]
    if 'dry' not in a:
        put_txt('%s_read_sort.txt' % ACT, L)
    print(NL.join(L[8:]))


# ================================================================================ COMPONENT 1: THE READ BANK, REPAIRED ((R314)(2), the author's word at the sort)
CAP = 200
CAP_NEEDLE = 'a limit above two hundred'   # ### the author's answer at the sort that named the cap


def _cap_word_at():
    """the time of the author's answer that named the cap: the first user line of this act's session carrying CAP_NEEDLE after the anchor."""
    for _i, o, _st, _sid in R._session_rows():
        if o.get('type') != 'user':
            continue
        cs = (o.get('message') or {}).get('content')
        texts = [cs] if isinstance(cs, str) else []
        for c in (cs if isinstance(cs, list) else []):
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                texts.append(''.join(x.get('text', '') for x in t if isinstance(x, dict)) if isinstance(t, list) else (t or ''))
            elif isinstance(c, dict) and c.get('type') == 'text':
                texts.append(c.get('text', ''))
        if any(CAP_NEEDLE in t and 'BEGIN' in t for t in texts):
            return o.get('timestamp')
    return None


def _read_verdict(r, word):
    """one Read call against the rule: under 200 lines within it; otherwise an offset and a limit no greater than the cap, or a breach -- a
    breach before the word that named the cap, with both an offset and a limit, the cap's precursor and not counted."""
    big = r['lines'] is None or r['lines'] >= CAP
    if not big:
        return 'WITHIN THE RULE (UNDER 200 LINES)'
    if r['offset'] is not None and r['limit'] is not None and r['limit'] <= CAP:
        return 'WITHIN THE RULE'
    if r['offset'] is not None and r['limit'] is not None and word and r['ts'] < word:
        return 'BEFORE THE WORD -- THE CAP`S PRECURSOR, NOT COUNTED'
    return '### AN OFFENCE'


def reads(*a):
    """b698's route (tools/b698_record.py :1219), REPAIRED at b704's carry on the author's word at the sort: every Read call of the seat since
    the anchor with its offset and limit VALUES (b698's route recorded only whether each was passed), the file's line count read now beside it;
    a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an offence -- a call before the
    word that named the cap, carrying both, printed as the cap's precursor and not counted. data/b704_read_calls.txt."""
    word = _cap_word_at()
    rows = []
    for i, o, _st, _sid in R._session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i, ts=o.get('timestamp'), path=p, offset=inp.get('offset'), limit=inp.get('limit'), lines=R._lines_now(p)))
    for r in rows:
        r['verdict'] = _read_verdict(r, word)
    bad = [r for r in rows if r['verdict'] == '### AN OFFENCE']
    pre = [r for r in rows if r['verdict'].startswith('BEFORE THE WORD')]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) AND THE AUTHOR`S WORD AT THE SORT (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines; otherwise an offset and a limit, the limit no greater than two hundred (the',
         '### cap, the author`s word at %s). Rows are Read calls: transcript line | time | the file`s lines read now | offset | limit | the verdict |' % (word or '### NOT READ'),
         '### path. A call before the word carrying both an offset and a limit above the cap is its precursor, printed and not counted.']
    L += ['  %s | %s | %s | offset %s | limit %s | %s | %s' % (r['line'], r['ts'], r['lines'], r['offset'], r['limit'], r['verdict'], r['path']) for r in rows] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; ON FILES OF 200 LINES OR MORE %d ; OFFENCES %d ; THE CAP`S PRECURSORS %d ; THE WORD AT %s.**' % (
        len(rows), sum(1 for r in rows if r['lines'] is None or r['lines'] >= CAP), len(bad), len(pre), word or '### NOT READ')]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
        put_json('%s_read_calls.json' % ACT, dict(at=utc(), word=word, cap=CAP, rows=rows))
    print(NL.join([l for l in L if '### AN OFFENCE' in l or 'PRECURSOR' in l][:40] + L[-1:]))


def names(*a):
    """the functions of an imported record module (b698's by default) with the line each opens at -- names and numbers, no source printed."""
    import importlib
    import inspect
    mod = {'b698': R, 'b703': P3}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
    for n, f in sorted(vars(mod).items(), key=lambda kv: inspect.getsourcelines(kv[1])[1] if inspect.isfunction(kv[1]) and kv[1].__module__ == mod.__name__ else 0):
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            print('  %-28s :%d' % (n, inspect.getsourcelines(f)[1]))


def probeview(*a):
    """`probeview <run id>`: the probe's run read by its id; the artifact downloaded into memory and its sha256 compared with the platform's
    digest BEFORE any reading; out/closure_log.txt banked whole as data/b704_probe_out_zeta.txt (the probe output), the build log and the
    axioms output beside it; the output parsed by chain_page's own parser, every cell of the probe named or missing; each name's axioms
    compared with b703's two run banks (data/b703_axioms_SIDE-explicit-formula_run1r.txt, _run2.txt) for every name both carry (N2).
    data/b704_runner_SIDE-explicit-formula_probe.txt (.json)."""
    import hashlib
    import io as _io
    import zipfile
    import chain_page as CP
    run_id = int(a[0])
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event')
    run = json.loads(out or b'{}')
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    pj = jl('%s_probe.json' % ACT)
    L = ['%s -- THE FACES PROBE ON THE HOSTED RUNNER, READ BY ITS RUN ID (%s)' % (ACT, utc()), '',
         '### the probe: relay data/b704_probe.txt (the generator`s text sha256 %s, %d cells) as the root CircuitClosure.lean of %s at %s, its' % (
             (pj.get('sha256') or '')[:16], len(pj.get('cells') or []), PROBE_BRANCH, g(EF, 'rev-parse', PROBE_BRANCH).strip()[:7]),
         '### modules` tree v0.37`s (the branch`s one commit changes that file alone; relay data/b704_probe_diff.txt)',
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'), run.get('updatedAt'))]
    T_ = {}
    sha = None
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        agree = bool(digest) and digest == sha
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN', 'AGREE' if agree else '### NOTHING READ FROM IT'))
        if agree:
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
        else:
            sha = None
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip() or None
    berr = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    clog = T_.get('closure_log.txt', '')
    cells, perr = CP.parse(clog)
    want = pj.get('cells') or []
    missing = [n for n in want if n not in cells or cells[n].get('missing')]
    ax_prev = {}
    for b in ('b703_axioms_SIDE-explicit-formula_run1r.txt', 'b703_axioms_SIDE-explicit-formula_run2.txt'):
        for n, d in _deps(rdn(b)):
            ax_prev[n] = (sorted(d), b)
    both = [n for n in want if n in ax_prev and n in cells and not cells[n].get('missing')]
    diff = [n for n in both if sorted(cells[n].get('axioms') or []) != ax_prev[n][0]]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (low[-1] if low else None, K.HOLD, any(l.startswith('STOP ') for l in mem.split(NL))),
          '### the build: exit %s ; error lines %d' % (bexit, len(berr))] + ['    ' + l for l in berr[:20]] + [
          '### the closure step (the probe): out/closure_log.txt %d bytes ; error lines %d ; cells parsed %d ; cells wanted %d ; missing %d' % (
              len(clog), len(perr), len(cells), len(want), len(missing))] + ['    ' + l for l in perr[:20]] + [
          '### the missing cells: %s' % (missing or 'NONE'),
          '### N2: the names both this probe and b703`s two runs print (%d): axioms equal %d ; differing %d %s' % (len(both), len(both) - len(diff), len(diff), diff or '')]
    ok = run.get('conclusion') == 'success' and sha and bexit == '0' and not berr and not perr and not missing
    L += ['', '### ### **RUN %s (probe) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; PROBE CELLS %d OF %d ; MISSING %d ; N2 EQUAL %d OF %d ; '
          'THE PROBE %s.**' % (run_id, run.get('conclusion'), 'AGREE' if sha else '### UNREAD', bexit, len(berr) + len(perr), len(want) - len(missing),
                               len(want), len(missing), len(both) - len(diff), len(both), 'READ' if ok else '### NOT READ WHOLE -- THE PAGE HOLDS')]
    put_txt('%s_runner_%s_probe.txt' % (ACT, K.KERNEL), L)
    put_json('%s_runner_%s_probe.json' % (ACT, K.KERNEL), dict(at=utc(), run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=sha,
                                                               build_exit=bexit, missing=missing, n2_both=len(both), n2_diff=diff, ok=bool(ok)))
    if sha:
        put_txt('%s_probe_out_zeta.txt' % ACT, clog.rstrip(NL).split(NL))
        put_txt('%s_buildlog_%s_probe.txt' % (ACT, K.KERNEL), blog.rstrip(NL).split(NL))
        put_txt('%s_axioms_%s_probe.txt' % (ACT, K.KERNEL), (T_.get('axioms.txt', '').rstrip(NL) or '### EMPTY').split(NL))
    print(NL.join(L[:8] + L[-6:]))


def probediff(*a):
    """data/b704_probe_diff.txt: the probe branch's commit against v0.37, by path (git diff --stat, name-status) -- one path, the root file."""
    tip = g(EF, 'rev-parse', PROBE_BRANCH).strip()
    ns = [l for l in g(EF, 'diff', '--name-status', K.EF_V037, tip).split(NL) if l.strip()]
    st = [l for l in g(EF, 'diff', '--stat', K.EF_V037, tip).split(NL) if l.strip()]
    L = ['%s -- (R314)(3): THE PROBE BRANCH`S DIFF AGAINST v0.37 (%s)' % (ACT, utc()), '',
         '### %s = %s against v0.37 = %s; rows are paths changed (git diff --name-status), then the stat.' % (PROBE_BRANCH, tip[:7], K.EF_V037[:7]), '']
    L += ['  ' + l for l in ns] + [''] + ['  ' + l for l in st]
    ok = ns == ['M\tCircuitClosure.lean']
    L += ['', '### ### **PATHS CHANGED %d ; THE ONE PATH THE ROOT FILE CircuitClosure.lean %s ; THE MODULES` TREE v0.37`S %s.**' % (len(ns), ok, ok)]
    if 'dry' not in a:
        put_txt('%s_probe_diff.txt' % ACT, L)
    print(NL.join(L[-1:]))


def _vkey(v):
    return tuple(int(x) for x in v.lstrip('v').split('.'))


def efcells(*a):
    """data/b704_correspondence_dry.txt: (R314)(4)'s dry run. The generator run dry over the roster (its verdict line read from its own print),
    and beside it the reader over every roster table, located by the generator's own find_table and anchor: each table line naming
    SIDE-explicit-formula, the column it sits in by the header (the generator's `columns`), the kernel cell's clauses as the generator parses
    them (parse_kernel_cell), the version tokens beside the name, and whether that version is behind v0.37 -- the count of cells and the
    papers they sit in. Nothing written but this bank."""
    import correspondence_gen as CG
    gen = subprocess.run([sys.executable, '-X', 'utf8', '-B', os.path.join(T, 'correspondence_gen.py'), 'dry', os.path.join(D, 'b672_roster_read.json'), 'full'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT)
    gv = [l for l in gen.stdout.split(NL) if l.startswith('### ### **TABLES')]
    tabled = sorted(set(re.findall(r'^    (SIDE-[\w-]+)\s+READ LOCALLY', gen.stdout, re.M)))
    ro = jl('b672_roster_read.json').get('tables') or []
    rows, per = [], {}
    for t in ro:
        if t.get('withheld'):
            continue
        p = os.path.join(PP, t['path'])
        lines = (rd(p) or '').replace(chr(13), '').split(NL)
        ft = CG.find_table(lines, t)
        if isinstance(ft, str):
            rows.append((t['doc'], t['path'], 0, '### ' + ft, '', '', '', ''))
            continue
        i0, i1 = ft
        cols = CG.columns(lines[i0])
        sp_h = CG.spans(lines[i0])
        for i in range(i0 + 1, i1):
            l = lines[i]
            if 'explicit-formula' not in l or CG.SEP_ROW.match(l):
                continue
            sp = CG.spans(l)
            where = [k for k, c in (('kernel', cols['kernel']), ('terminal', cols['terminal']), ('profile', cols['profile']), ('status', cols['status']))
                     if c is not None and c < len(sp) and 'explicit-formula' in CG.cell(l, sp[c])]
            other = [n for n in range(len(sp)) if 'explicit-formula' in CG.cell(l, sp[n]) and n not in [cols[k] for k in ('kernel', 'terminal', 'profile', 'status')]]
            kc = CG.cell(l, sp[cols['kernel']]) if cols['kernel'] is not None and cols['kernel'] < len(sp) else ''
            parsed = [(k, [x[3] for x in toks]) for k, toks in CG.parse_kernel_cell(kc)] if kc else []
            vers = sorted(set(re.findall(r'explicit-formula`?\*?\*?\s*(?:at\s+)?`?(v\d+(?:\.\d+)*)', l)))
            behind = [v for v in vers if _vkey(v) < _vkey('v0.37')]
            rows.append((t['doc'], t['path'], i + 1, ','.join(where + ['col%d' % n for n in other]), parsed, vers, behind,
                         'BEHIND v0.37' if behind else ('AT v0.37' if 'v0.37' in vers else 'NO VERSION BESIDE THE NAME')))
            if behind:
                per[t['doc']] = per.get(t['doc'], 0) + 1
    L = ['%s -- COMPONENT 3, (R314)(4): THE CORRESPONDENCE CELLS NAMING SIDE-explicit-formula, THE GENERATOR`S DRY RUN AND THE READER BESIDE IT (%s)' % (ACT, utc()), '',
         '### the generator: `python -X utf8 -B tools/correspondence_gen.py dry data/b672_roster_read.json` (exit %d), the local clones` tags, nothing' % gen.returncode,
         '### written; its verdict, verbatim: %s' % (gv[0] if gv else '### NOT PRINTED'),
         '### the kernels it tables (a kernel cell it parses in a shaped table, %d): %s' % (len(tabled), ', '.join(tabled)),
         '### SIDE-explicit-formula among them: %s' % ('SIDE-explicit-formula' in tabled), '',
         '### THE READER: rows are table lines naming SIDE-explicit-formula: document | file :line | the column(s) carrying the name | the kernel',
         '### cell as the generator parses it | the versions beside the name | the reading against v0.37.']
    L += ['  %s | %s :%s | %s | %s | %s | %s' % (r[0], r[1], r[2], r[3] or '-', r[4] or '-', r[5] or '-', r[7]) for r in rows] or ['  NONE']
    nb = sum(1 for r in rows if r[7] == 'BEHIND v0.37')
    L += ['', '### THE CELLS BEHIND v0.37 BY PAPER: %s' % (', '.join('%s %d' % kv for kv in sorted(per.items())) or 'NONE'),
          '### ### **TABLE LINES NAMING SIDE-explicit-formula %d ; BEHIND v0.37 %d IN %d PAPERS ; IN A KERNEL CELL THE GENERATOR PARSES %d ; THE GENERATOR`S '
          'CELLS CHANGED %s ; NOTHING WRITTEN.**' % (
              len([r for r in rows if r[2]]), nb, len(per), sum(1 for r in rows if 'kernel' in (r[3] or '') and any(k == 'SIDE-explicit-formula' for k, _ in (r[4] or []))),
              (re.search(r'CELLS CHANGED (\d+)', gv[0]).group(1) if gv else '?'))]
    if 'dry' not in a:
        put_txt('%s_correspondence_dry.txt' % ACT, L)
    print(NL.join(L[2:6] + L[8:]))


def cands(*a):
    """data/b704_nodes_prompt.txt: the two candidate nodes of (R314)(3) as the probe prints them (chain_page's parser over
    data/b704_probe_out_zeta.txt): kind, module :line, the statement, the axioms, the nodes each consumes; and whether any node of the list
    consumes either (so a page at the probe alone reads the same cells as one with them)."""
    import chain_page as CP
    cells, errs = CP.parse(rdn('b704_probe_out_zeta.txt'))
    _CP, names, _corr, _w = _probe_parts()
    L = ['%s -- COMPONENT 2, (R314)(3): THE TWO NODE ADDITIONS AS THE PROBE PRINTS THEM, FOR THE PROMPT (%s)' % (ACT, utc()), '',
         '### the probe: run 39721668586 (relay data/b704_runner_SIDE-explicit-formula_probe.txt), its output relay data/b704_probe_out_zeta.txt parsed by',
         '### relay tools/chain_page.py`s parser; rows are the candidates: kind | module :line | the statement (#print sig) | axioms | consumes.', '']
    for n in CANDIDATES:
        c = cells.get(n) or {}
        L += ['  %s' % n, '      %s | %s :%s | %s' % (c.get('kind'), c.get('module'), c.get('line'), c.get('axioms_text')),
              '      statement: %s' % c.get('statement'), '      consumes: %s' % (c.get('consumes') or 'NONE')]
    users = [(n, [x for x in (cells.get(n) or {}).get('consumes') or [] if x in CANDIDATES]) for n in names]
    users = [(n, x) for n, x in users if x]
    L += ['', '### the list`s nodes consuming a candidate: %s' % (users or 'NONE'),
          '### ### **CANDIDATES %d ; PRINTED %d ; AT THE STANDARD THREE %d ; THE LIST`S NODES CONSUMING EITHER %d.**' % (
              len(CANDIDATES), sum(1 for n in CANDIDATES if n in cells and not cells[n].get('missing')),
              sum(1 for n in CANDIDATES if set((cells.get(n) or {}).get('axioms') or ['x']) <= set(STD3)), len(users))]
    if 'dry' not in a:
        put_txt('%s_nodes_prompt.txt' % ACT, L)
    print(NL.join(L[4:]))


SCR = K.SP
PAGE_NEW = os.path.join(SCR, 'faces_b704.md')
PAGE_CTL = os.path.join(SCR, 'faces_b702_now.md')
PAGE_NEW2 = os.path.join(SCR, 'faces_b704_gloss.md')   # ### the second write's page, after Component 3's glossary rows


def _ops(a_, b_):
    import difflib
    return [o for o in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes() if o[0] != 'equal']


def facesraw(*a):
    """a print only: the committed page (PLACE-papers HEAD) against the control (b702's list from b643's probe, regenerated now) and against
    the new page (b704's list from b704's probe), each changed line shown short -- for the cause rules of facesdiff. Writes nothing."""
    C = (_show(PP, 'HEAD', K.FACES_PAGE) or '').replace(chr(13), '').split(NL)
    O = rd(PAGE_CTL).replace(chr(13), '').split(NL)
    N = rd(PAGE_NEW).replace(chr(13), '').split(NL)
    for lab, x, y in (('COMMITTED -> CONTROL', C, O), ('CONTROL -> NEW', O, N)):
        ops = _ops(x, y)
        print('=== %s : %d opcodes' % (lab, len(ops)))
        for op, i1, i2, j1, j2 in ops:
            print('  %s :%d-:%d -> :%d-:%d' % (op, i1 + 1, i2, j1 + 1, j2))
            for l in x[i1:i2]:
                print('     - %s' % l[:150])
            for l in y[j1:j2]:
                print('     + %s' % l[:150])


def facesdiff(*a):
    """data/b704_faces_diff.txt: (R314)(3), every line of the page the regeneration changes, named with its cause. The committed page (PLACE-papers
    HEAD) against the new page by the generator (b704's list from b704's probe, run 39721668586); the control page (b702's list from b643's probe,
    regenerated now by the same generator) separates what changed before this act's probe from what the probe and the list change. A line no
    cause rule names prints ### NO CAUSE and holds the write."""
    base = K.PRE_PP   # ### the act's start: the page as b702 wrote it (b704 writes it twice, 5cf62a2 and the glossary write after Component 3)
    C = (_show(PP, base, K.FACES_PAGE) or '').replace(chr(13), '').split(NL)
    O = rd(PAGE_CTL).replace(chr(13), '').split(NL)
    N = rd(PAGE_NEW2 if os.path.exists(PAGE_NEW2) else PAGE_NEW).replace(chr(13), '').split(NL)
    co = _ops(C, O)
    o_new = set(l for op, i1, i2, j1, j2 in co for l in O[j1:j2])
    gl = rdn('glossary.txt').split(NL)
    rows = []
    for op, i1, i2, j1, j2 in _ops(C, N):
        for k, l in enumerate(N[j1:j2]):
            if l in o_new and l.startswith("- **classK'**"):
                gi = next((i + 1 for i, x in enumerate(gl) if x.startswith("classK'\t")), 0)
                cause = ('THE GLOSSARY`S classK` ROW, appended at b703 on the author`s word (relay data/glossary.txt :%d), carried into the page`s '
                         'glossary block by the generator (the list`s `# glossary` line) -- present in the control page too: the change '
                         'test_chain_page.py (1), (14) and test_g_chain_page.py (1) read at step zero' % gi)
            elif l.startswith("- **h2_sign'**") or l.startswith('- **h2_sign_sum**'):
                gi = next((i + 1 for i, x in enumerate(gl) if x.startswith(l[4:].split('**')[0] + '\t')), 0)
                cause = ('THE GLOSSARY COMPANIONS, (R314)(6) and the author`s word ("write, after one check"): the row appended at relay '
                         'data/glossary.txt :%d after the page`s first write (5cf62a2), carried by the page`s second write on the author`s word '
                         '("regenerate once more"); the page written twice because (R314) put the page before the rows it prints (the '
                         'navigator`s, by that word)' % gi)
            elif j1 + k + 1 == 3 and 'b704_nodes_zeta.txt' in l:
                cause = 'THE LIST AND ITS PIN, (R314)(3): b702`s list -> b704`s (relay data/b704_nodes_zeta.txt, every row unchanged but its tag)'
            elif any('`%s`' % c in l for c in CANDIDATES):
                cause = 'A NODE ADDITION, (R314)(3) and the author`s word ("regenerate with both nodes"), its cells from probe run 39721668586'
            else:
                cause = '### NO CAUSE'
            rows.append((op, j1 + k + 1, (C[i1 + k] if op == 'replace' and i1 + k < i2 else None), l, cause))
        if op in ('replace', 'delete') and (i2 - i1) > (j2 - j1):
            for k in range(j2 - j1, i2 - i1):
                rows.append(('delete', None, C[i1 + k], None, '### NO CAUSE'))
    hdr = [l for l in N[:6] if 'v0.37' in l]
    L = ['%s -- COMPONENT 2, (R314)(3): THE FACES PAGE REGENERATED FROM THE PROBE AT v0.37, EVERY CHANGED LINE WITH ITS CAUSE (%s)' % (ACT, utc()), '',
         '### the page: PLACE-papers %s at the act`s start, %s (%d lines), against the generator`s page from relay data/b704_nodes_zeta.txt and relay' % (K.FACES_PAGE, base, len(C)),
         '### data/b704_probe_out_zeta.txt (run 39721668586; %d lines). The control: b702`s list from b643`s probe regenerated now (%d lines),' % (len(N), len(O)),
         '### differing from the committed page in %d line(s) before any change of this act. No cell is written by hand. Rows are changed lines:' % sum(max(i2 - i1, j2 - j1) for _o, i1, i2, j1, j2 in co),
         '### the kind | the new page`s line | the committed line it replaces | the new line | the cause.', '']
    for op, ln, old, new, cause in rows:
        L += ['  %s | :%s | %s' % (op, ln, cause)]
        if old is not None:
            L.append('      - %s' % old)
        if new is not None:
            L.append('      + %s' % new)
    bycause = {}
    for r in rows:
        key = r[4].split(',')[0].split(' (')[0]
        bycause[key] = bycause.get(key, 0) + 1
    nc = sum(1 for r in rows if r[4].startswith('### NO CAUSE'))
    L += ['', '### THE HEADER: %s' % ('the page`s head names v0.37 at :%d' % (N.index(hdr[0]) + 1) if hdr else '### THE HEAD DOES NOT NAME v0.37'),
          '### THE CHANGED LINES BY CAUSE: %s' % '; '.join('%s %d' % kv for kv in sorted(bycause.items())),
          '### ### **CHANGED LINES %d ; WITH A CAUSE %d ; WITHOUT %d ; NODES %d -> %d ; THE HEAD AT v0.37 %s.**' % (
              len(rows), len(rows) - nc, nc, len([l for l in C if re.match(r'^\d+\. `', l)]), len([l for l in N if re.match(r'^\d+\. `', l)]), bool(hdr))]
    if 'dry' not in a:
        put_txt('%s_faces_diff.txt' % ACT, L)
        put_json('%s_faces_diff.json' % ACT, dict(at=utc(), rows=[dict(kind=r[0], line=r[1], cause=r[4]) for r in rows], by_cause=bycause, no_cause=nc,
                                                 head_v037=bool(hdr)))
    print(NL.join(L[6:]))


def _probe_pins():
    """each banked chain probe with the pin its node list names (a list without a `# pin:` line is b568's, at v0.10)."""
    out = []
    for f in sorted(os.listdir(D)):
        m = re.match(r'^(b\d+)_probe_out(_zeta)?\.txt$', f)
        if not m:
            continue
        lst = next((x for x in ('%s_nodes_zeta.txt' % m.group(1), '%s_nodes.txt' % m.group(1), '%s_nodes_faces.txt' % m.group(1))
                    if os.path.exists(os.path.join(D, x))), None)
        pin = 'v0.10'
        if lst:
            pins = re.findall(r'^# pin: (\S+)\s*$', rdn(lst), re.M)
            pin = pins[-1] if pins else 'v0.10'
        out.append((f, lst, pin))
    return out


def cellsreach(*a):
    """data/b704_cells_reach.txt: (R314)(4) on the author's word -- each table line naming SIDE-explicit-formula at a tag (data/b704_correspondence_dry.txt's
    rows), read against the probe: the paper and line, each kernel theorem the line names (an identifier whose last component is a probe cell's),
    the tag the line names beside the kernel, the theorem's statement at v0.37 from probe run 39721668586, and its statement at the named tag
    from the banked chain probe whose list's pin is that tag, by path. EQUAL: the mention stands as an entry-tag citation; DIFFERS or NO PRINT
    BANK AT THE TAG: raised before the closing, nothing written. The source header at the named tag is printed beside as a source, not a print."""
    import chain_page as CP
    cells, _e = CP.parse(rdn('b704_probe_out_zeta.txt'))
    by_short = {}
    for n in cells:
        by_short.setdefault(n.split('.')[-1], []).append(n)
    pins = _probe_pins()
    dry_rows = [l for l in rdn('b704_correspondence_dry.txt').split(NL) if re.match(r'^  \S+ \| \S+ :\d+ \|', l)]
    rows = []
    for l in dry_rows:
        doc, rest = l.strip().split(' | ', 1)
        path, ln = re.match(r'^(\S+) :(\d+)', rest).groups()
        line = (rd(os.path.join(PP, path)) or '').replace(chr(13), '').split(NL)[int(ln) - 1]
        # ### the citation form the lines use: a backticked name, a comma, SIDE-explicit-formula and its tag (or "at the page's pin" and the tag)
        pairs = re.findall(r"`([A-Za-z_][\w.']*)`,\s*SIDE-explicit-formula\s+(?:at [^`|;)]*?pin\s+)?(v\d+(?:\.\d+)*)", line) or [('(none named)', '(no tag)')]
        for idn, tg0 in pairs:
            full = (by_short.get(idn.split('.')[-1]) or [None])[0]
            st37 = (cells.get(full) or {}).get('statement') if full else None
            for tg in [tg0]:
                bank = next((f for f, _lst, p in pins if p == tg), None)
                st_t = None
                if bank and full:
                    c2, _ = CP.parse(rdn(bank))
                    st_t = (c2.get(full) or {}).get('statement')
                src = None
                if full and tg.startswith('v'):
                    mod = (cells.get(full) or {}).get('module') or ''
                    blob = _show(EF, tg, '/'.join(mod.split('.')) + '.lean') if mod else ''
                    m0 = re.search(r'^(?:theorem|lemma|def)\s+(?:[\w.]*\.)?%s\b(.*?):=' % re.escape(full.split('.')[-1]), blob or '', re.M | re.S)
                    src = ' '.join(m0.group(0).split())[:300] if m0 else None
                verdict = ('EQUAL' if st_t and st37 and ' '.join(st_t.split()) == ' '.join(st37.split()) else
                           'DIFFERS' if st_t and st37 else 'NO PRINT BANK AT THE TAG' if full and tg.startswith('v') else 'NO THEOREM OR NO TAG READ')
                rows.append(dict(doc=doc, path=path, line=int(ln), text=line, id=idn, full=full, tag=tg, st37=st37, bank=bank, st_t=st_t, src=src, verdict=verdict))
    L = ['%s -- COMPONENT 3, (R314)(4) AND THE AUTHOR`S WORD AT THE CELLS PROMPT: THE PROSE MENTIONS OF SIDE-explicit-formula READ AGAINST THE PROBE (%s)' % (ACT, utc()), '',
         '### the mentions: the reader`s rows of relay data/b704_correspondence_dry.txt (11 table lines naming the kernel). The statement at v0.37: probe run',
         '### 39721668586 (relay data/b704_probe_out_zeta.txt, chain_page`s parser). The print banks holding a tag: the banked chain probes, each at its',
         '### list`s pin -- %s. Rows are (line, theorem, tag): the line verbatim, then the readings.' % '; '.join('%s at %s' % (f, p) for f, _l, p in pins), '']
    for r in rows:
        L += ['  %s | %s :%d | %s | tag %s | %s' % (r['doc'], r['path'], r['line'], r['full'] or r['id'], r['tag'], r['verdict']),
              '      the line: %s' % r['text'],
              '      at v0.37 (the probe): %s' % (r['st37'] or '### NOT A PROBE CELL'),
              '      at %s (%s): %s' % (r['tag'], ('relay data/' + r['bank']) if r['bank'] else '### NO PRINT BANK HOLDS THE TAG', r['st_t'] or '-'),
              '      the source at %s (git show, not a print): %s' % (r['tag'], r['src'] or '-')]
    raised = [r for r in rows if r['verdict'] != 'EQUAL']
    # ### the author's word at the page-again prompt: each raised mention prints its cause in one word -- "differs" (the statement at v0.37
    # ### differs from the statement at the named tag) or "unbanked" (no print bank holds the named tag; a line naming no tag beside the kernel
    # ### reads unbanked too, no bank holding a tag it does not name)
    L += ['', '### THE RAISED MENTIONS, EACH WITH ITS CAUSE IN ONE WORD (the author`s word):']
    L += ['  %s | %s :%d | %s | tag %s | %s%s' % (r['doc'], r['path'], r['line'], r['full'] or r['id'], r['tag'],
                                               'differs' if r['verdict'] == 'DIFFERS' else 'unbanked',
                                               '' if r['tag'].startswith('v') else ' (no tag named beside the kernel)') for r in raised]
    L += ['### EQUAL %d ; differs %d ; unbanked %d' % (sum(1 for r in rows if r['verdict'] == 'EQUAL'), sum(1 for r in raised if r['verdict'] == 'DIFFERS'),
                                                      sum(1 for r in raised if r['verdict'] != 'DIFFERS'))]
    L += ['', '### ### **MENTIONS READ %d (LINES %d) ; EQUAL %d ; DIFFERS %d ; NO PRINT BANK AT THE TAG %d ; NO THEOREM OR NO TAG %d ; RAISED BEFORE THE CLOSING %d ; '
          'NOTHING WRITTEN.**' % (len(rows), len(dry_rows), sum(1 for r in rows if r['verdict'] == 'EQUAL'), sum(1 for r in rows if r['verdict'] == 'DIFFERS'),
                                  sum(1 for r in rows if r['verdict'] == 'NO PRINT BANK AT THE TAG'), sum(1 for r in rows if r['verdict'].startswith('NO THEOREM')),
                                  len(raised))]
    if 'dry' not in a:
        put_txt('%s_cells_reach.txt' % ACT, L)
        put_json('%s_cells_reach.json' % ACT, dict(at=utc(), rows=[dict((k, v) for k, v in r.items() if k != 'text') for r in rows]))
    print(L[-1])


def readmediff(*a):
    """data/b704_readme.txt: (R314)(5) on the author's word ("apply") -- the README's diff against PLACE-papers HEAD (the working tree, before the
    commit) or, after it (`committed <sha>`), the commit's diff and the blob read back at the remote by one ls-remote of PLACE-papers; where each
    edit landed by line; the two edits and nothing else."""
    rm = (rd(os.path.join(PP, 'README.md')) or '').replace(chr(13), '').split(NL)
    kl = next((i + 1 for i, l in enumerate(rm) if 'the live kernel line names SIDE-explicit-formula **v0.37** (`38e2734`)' in l), 0)
    ap = next((i + 1 for i, l in enumerate(rm) if l.startswith("*(Appended under the author's ruling `(R314)`(5), 2026-10-22, b704")), 0)
    if a and a[0] == 'committed':
        sha = a[1]
        d = g(PP, 'show', '--format=%H %s', '--unified=0', sha, '--', 'README.md').split(NL)
        blob = g(PP, 'rev-parse', '%s:README.md' % sha).strip()
        remote = g(PP, 'ls-remote', 'origin', 'refs/heads/main').split()[:1]
        rblob = g(PP, 'rev-parse', '%s:README.md' % remote[0]).strip() if remote else ''
        tail = ['### the commit %s ; its README blob %s ; the remote main %s, its README blob %s ; %s' % (
            sha[:7], blob[:8], (remote or ['-'])[0][:7], rblob[:8], 'EQUAL' if blob and blob == rblob else '### NOT EQUAL')]
    else:
        d = g(PP, 'diff', '--unified=0', '--', 'README.md').split(NL)
        tail = ['### the working tree against HEAD, before the commit']
    plus = [l for l in d if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d if l.startswith('-') and not l.startswith('---')]
    L = ['%s -- COMPONENT 3, (R314)(5): THE README`S TWO EDITS ON THE AUTHOR`S WORD (%s)' % (ACT, utc()), '',
         '### rows are the diff`s lines (git diff --unified=0 of PLACE-papers README.md), then where each edit landed and the read-back.', '']
    L += ['  ' + l for l in d if l.strip()]
    L += ['', '### the kernel line at :%d ; the append at :%d (beneath the b702 append, :133)' % (kl, ap)] + tail
    ok = len(minus) == 1 and len(plus) == 3 and kl and ap == 135
    L += ['### ### **LINES REMOVED %d ; ADDED %d (THE KERNEL LINE, A BLANK, THE APPEND) ; THE KERNEL LINE AT :%d ; THE APPEND AT :%d ; AS ORDERED %s.**' % (
        len(minus), len(plus), kl, ap, bool(ok))]
    if 'dry' not in a:
        put_txt('%s_readme.txt' % ACT, L)
    print(NL.join(L[-3:]))


def glosscheck(*a):
    """data/b704_glossary.txt: (R314)(6) on the author's word ("write, after one check") -- E0's reading and the hand grade of the two theorems
    the companion rows rest on, read from b703's grade bank (data/b703_widening_grade.txt, its verdict line and each theorem's check line); a
    row is written where both read DERIVES, held otherwise; after the append (`landed`), the two rows read back from data/glossary.txt by line."""
    wg = rdn('b703_widening_grade.txt').split(NL)
    vl = next((i + 1 for i, l in enumerate(wg) if 'THEOREMS 10' in l), 0)
    out = []
    for th, row in (("h2_sign'_imp_rh", "h2_sign'"), ('h2_sign_sum_iff_rh', 'h2_sign_sum')):
        hd = next((i + 1 for i, l in enumerate(wg) if l.startswith('== %s ' % th)), 0)
        e0 = next((i + 1 for i, l in enumerate(wg) if i + 1 > hd and l.strip().startswith('E0 GRADE ')), 0) if hd else 0
        gr = next((i + 1 for i, l in enumerate(wg) if i + 1 > hd and l.strip().startswith('THE GRADE READ FROM THE STATEMENT:')), 0) if hd else 0
        m = re.search(r"%s GRADE (\S+) \(E0 (\S+)\)" % re.escape(th), wg[vl - 1] if vl else '')
        ok = bool(m) and m.group(1) == 'DERIVES' and m.group(2) == 'DERIVES'
        out.append((th, row, hd, e0, gr, m.group(1) if m else None, m.group(2) if m else None, ok,
                    wg[e0 - 1].strip() if e0 else '', wg[gr - 1].strip() if gr else ''))
    gl = rdn('glossary.txt').split(NL)
    landed = [(r, next((i + 1 for i, l in enumerate(gl) if l.startswith(r + '\t')), 0)) for _t, r, *_x in out]
    L = ['%s -- COMPONENT 3, (R314)(6): THE GLOSSARY COMPANIONS, THE CHECK BEFORE THE APPEND AND THE ROWS AFTER IT (%s)' % (ACT, utc()), '',
         '### the check (the author`s word at the glossary prompt): E0`s reading and the hand grade of the theorem each row rests on, from relay',
         '### data/b703_widening_grade.txt (the verdict :%d and each theorem`s block). Rows are theorems: the row it carries | the block | E0 | the hand' % vl,
         '### grade | write or hold.', '']
    for th, row, hd, e0, gr, hg, eg, ok, e0l, grl in out:
        L += ['  %s (the row %s) | data/b703_widening_grade.txt :%d | E0 %s | hand %s | %s' % (th, row, hd, eg, hg, 'WRITE' if ok else '### HOLD'),
              '      :%d %s' % (e0, e0l), '      :%d %s' % (gr, grl)]
    L += ['', '### the rows in relay data/glossary.txt after the append: %s' % ('; '.join('%s :%d' % x for x in landed))]
    L += ['### ### **THEOREMS 2 ; BOTH DERIVES UNDER E0 AND BY HAND %s ; ROWS TO WRITE %d ; ROWS IN THE GLOSSARY %d.**' % (
        all(o[7] for o in out), sum(1 for o in out if o[7]), sum(1 for _r, n in landed if n))]
    if 'dry' not in a:
        put_txt('%s_glossary.txt' % ACT, L)
    print(NL.join(L[6:]))


def runwait(*a):
    """`runwait <kernel> <run id> [seconds]`: the run's status read every 30 s in the FOREGROUND until it completes or the seconds pass (at most
    560, under the 590 s guard); each read printed. No wait is backgrounded."""
    end = time.time() + min(int(a[2]) if len(a) > 2 else 540, 560)
    while True:
        rc, out, err = R._gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,updatedAt')
        j = json.loads(out or b'{}')
        print('  %s  status %s ; conclusion %s ; updated %s' % (utc(), j.get('status'), j.get('conclusion') or '-', j.get('updatedAt')), flush=True)
        if j.get('status') == 'completed' or time.time() + 30 > end:
            return
        time.sleep(30)


SUMMARY = re.compile(r'^### ### \*\*(\S+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b704_tie.txt: (R314)(7), the licensed table's next document -- b652's order and b674's tie-break rule printed verbatim before the
    document is named; the agenda's rows as b702's tie bank read them (data/b702_tie.txt, reading 4), b702's cut entered from its own bank
    (data/b702_cut.json); the documents at the top count, each table's summary line verbatim, each document's sha256 at PLACE-papers HEAD
    against its table's read; b674's rule step by step in its written order."""
    import hashlib
    f52 = rdn('b652_ferry.txt').split(NL)
    r74 = rdn('b674_rules.txt').split(NL)
    t02 = rdn('b702_tie.txt').split(NL)
    cut = jl('b702_cut.json')
    rows = []
    for i, l in enumerate(t02, 1):
        m = re.match(r'^\s+(\d+) \| (\w[\w ]*?)\s+\| (.*)$', l)
        if m:
            rows.append(dict(line=i, count=int(m.group(1)), kind=m.group(2).strip(), row=m.group(3)))
    for r in rows:
        if r['row'].startswith('day1/Seven_Mechanism_Classes.md') and cut.get('after') is not None:
            r['count_b702'], r['count'] = r['count'], cut['after']
    kern = [r for r in rows if r['kind'] == 'kernel']
    comp = sorted([r for r in rows if r['kind'] == 'companion'], key=lambda r: -r['count'])
    top = comp[0]['count'] if comp else None
    at_top = [r for r in comp if r['count'] == top]
    L = ['%s -- COMPONENT 4, (R314)(7): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER AND b674`S TIE-BREAK RULE PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + f52[18].strip(), '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + [r74[k] for k in range(7, 11)] + ['',
         '### THE AGENDA`S ROWS, VERBATIM FROM b702`S TIE BANK (relay data/b702_tie.txt :14-:46, reading 4), b702`S CUT ENTERED FROM relay data/b702_cut.json',
         '### (day1/Seven_Mechanism_Classes.md %s -> %s); rows are documents: the count now | the kind | the row (its line in b702`s bank):' % (cut.get('before'), cut.get('after'))]
    L += ['  %4d | %-9s | %s (b702_tie :%d)%s' % (r['count'], r['kind'], r['row'], r['line'], ('   ### b702`s cut: %d -> %d' % (r['count_b702'], r['count'])) if 'count_b702' in r else '')
          for r in rows]
    L += ['', '### THE KERNELS BY DESCENDING COUNT: the top count %s ; kernels at 0 %d of %d -- the order passes to the companions ("then the companions")' % (
        max([r['count'] for r in kern] or [0]), sum(1 for r in kern if r['count'] == 0), len(kern)),
          '### THE COMPANIONS BY DESCENDING COUNT: %s' % '; '.join('%s %d' % (r['row'].split('   ')[0].split(' (v')[0] + (' (v' + r['row'].split(' (v')[1].split(')')[0] + ')' if ' (v' in r['row'] else ''), r['count']) for r in comp),
          '### THE TOP COUNT %s ; the documents standing at it %d' % (top, len(at_top)), '### the tables of the documents at the top count, their summary lines verbatim, and the document at HEAD against the table`s read:']
    tabs = []
    for r in at_top:
        tb = re.search(r'\[data/(b646_table_\w+\.txt)\]', r['row'])
        tl = rdn(tb.group(1)).split(NL) if tb else []
        sm = next((SUMMARY.match(x) for x in tl if SUMMARY.match(x)), None)
        dm = re.search(r'PLACE-papers (\S+) at (\w+), (\d+) lines, sha256 ([0-9a-f]{64})', NL.join(tl[:4]))
        doc = dm.group(1) if dm else '?'
        head_sha = hashlib.sha256((_show(PP, 'HEAD', doc) or '').encode('utf-8')).hexdigest() if dm else ''
        x = dict(row=r, bank=tb.group(1) if tb else None, summary=sm.group(0) if sm else '### NO SUMMARY LINE', doc=doc,
                 claims=int(sm.group(2)) if sm else 0, und=int(sm.group(5)) if sm else 0, over=int(sm.group(6)) if sm else 0,
                 unl=int(sm.group(7)) if sm else 0, read_sha=dm.group(4) if dm else '', head_sha=head_sha)
        x['outside'] = x['over'] + x['unl'] + x['und']
        tabs.append(x)
        L += ['    relay data/%s : %s' % (x['bank'], x['summary']),
              '      the document %s: sha256 at the table`s read %s ; at PLACE-papers HEAD %s ; %s' % (
                  doc, x['read_sha'][:16], head_sha[:16], 'UNMOVED' if x['read_sha'] == head_sha else '### MOVED SINCE ITS READ')]
    L += ['### b674`s rule, step by step in its written order:']
    pick = None
    if len(tabs) == 1:
        pick = tabs[0]
        L.append('    NOT REACHED: one document at the top count')
    elif tabs:
        ov = sorted(set(t['over'] for t in tabs))
        L.append('    (i) the OVERREACHES counts: %s -- %s' % (', '.join('%s %d' % (t['doc'], t['over']) for t in tabs), 'EQUAL' if len(ov) == 1 else 'NOT EQUAL'))
        if len(ov) > 1:
            mx = max(t['over'] for t in tabs)
            cand = [t for t in tabs if t['over'] == mx]
            L.append('        the rule`s condition (equal OVERREACHES) not met: the greater OVERREACHES count %d stands first' % mx)
        else:
            cand = tabs
        L.append('    (ii) a declared suite failure on either document: NONE (no arm of b703`s suite names either; data/b703_checks.txt)')
        if len(cand) > 1:
            mo = max(t['outside'] for t in cand)
            L.append('    (iii) the rows outside LICENSED/CITED of any kind (OVERREACHES + UNLICENSED + UNDERSTATES): %s' % ', '.join(
                '%s %d (%d + %d + %d)' % (t['doc'], t['outside'], t['over'], t['unl'], t['und']) for t in cand))
            c2 = [t for t in cand if t['outside'] == mo]
            if len(c2) > 1:
                mc = max(t['claims'] for t in c2)
                L.append('    (iv) the larger table (CLAIMS): %s' % ', '.join('%s %d' % (t['doc'], t['claims']) for t in c2))
                c2 = [t for t in c2 if t['claims'] == mc]
            cand = c2
        pick = cand[0] if len(cand) == 1 else None
        if pick is None:
            L.append('    ### THE RULE ENDS IN A TIE -- RAISED, NOTHING NAMED')
    nxt = [r for r in comp if r['count'] < (top or 0)][:2]
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER AND b674`S TIE-BREAK: %s (A COMPANION ; THE TOP COUNT %s, %d DOCUMENTS AT IT ; %s ; THE NEXT BY COUNT %s).**' % (
        pick['doc'] if pick else '### NONE NAMED', top, len(at_top), 'b674`S RULE APPLIED' if len(tabs) > 1 else 'NO TIE',
        '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in nxt))]
    if 'dry' not in a:
        put_txt('%s_tie.txt' % ACT, L)
        put_json('%s_tie.json' % ACT, dict(at=utc(), top=top, at_top=[t['doc'] for t in tabs], pick=pick['doc'] if pick else None,
                                          tables=[dict((k, v) for k, v in t.items() if k != 'row') for t in tabs]))
    print(NL.join(L))


ROUTES = dict(names=names, defshort=defshort, probeview=probeview, probediff=probediff, efcells=efcells, tie=tie, runwait=runwait, cands=cands, facesraw=facesraw, facesdiff=facesdiff, cellsreach=cellsreach, readmediff=readmediff, glosscheck=glosscheck, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch, runstatus=runstatus,
              readsort=readsort, c1=c1, reads=reads, nodesdiff=nodesdiff, probe=probe)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b704_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
