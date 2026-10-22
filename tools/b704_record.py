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


ORDERS = [
    ('*Appended 2026-10-22 by b704 beneath `W-ORD-FACES-PROBE-CURRENT` (:15444), under `(R314)`(3) -- THE ORDER DISCHARGED:*',
     ' the chain’s `#print sig` re-probed at SIDE-explicit-formula v0.37 = 38e2734 on one dispatch (run 39721668586, read by its run id, the '
     'artifact’s sha256 agreeing, 568 of 568 cells; relay data/b704_runner_SIDE-explicit-formula_probe.txt), the probe run as the root '
     'CircuitClosure.lean of the scratch branch probe-b704 cut from v0.37 on the author’s word -- the runner at v0.37 runs `#print axioms` and '
     'b692’s constant closure alone -- the branch deleted locally and at the remote once its bank was committed, main and every tag untouched; '
     'the node list’s successor relay data/b704_nodes_zeta.txt, every row unchanged but its tag, with h2_sign_sum_iff_rh (↔) and h2_sign’_imp_rh '
     '(→) as nodes on the author’s word; the page regenerated by relay tools/chain_page.py (PLACE-papers 5cf62a2), its header at v0.37, and '
     'written again after the glossary companions (c9b2e55): six lines over the act, each with its cause (relay data/b704_faces_diff.txt). '
     'Status DISCHARGED.'),
    ('*Appended 2026-10-22 by b704, under the author’s word at the probe-route prompt -- THE ORDER **`W-ORD-WORKFLOW-PROBE-STEP`**, ENTERED:*',
     ' a probe step in SIDE-explicit-formula’s build-module.yml that runs a root ChainProbe.lean when the ref carries one, so later chain '
     'probes need no scratch branch. At b704 the probe ran as the root CircuitClosure.lean of the scratch branch probe-b704, the workflow at '
     'v0.37 running `#print axioms` over print_targets.txt and b692’s constant closure alone (build-module.yml :78-:111). Priced at one main '
     'commit and one dispatch. Nothing edited in the workflow at b704. Trigger: the re-cut act b706. Status OPEN.'),
    ('*Appended 2026-10-22 by b704, under the author’s word at the cells prompt -- THE ORDER **`W-ORD-CORRESPONDENCE-EF-REACH`**, ENTERED:*',
     ' the Correspondence generator (relay tools/correspondence_gen.py) parses the kernel cell of 16 kernels, SIDE-explicit-formula not among '
     'them (relay data/b704_correspondence_dry.txt); 11 roster table lines name it, in status, claim and terminal cells, in the citation form '
     '“(`theorem`, SIDE-explicit-formula vX = `sha`)”; their 15 mentions read against probe run 39721668586 -- 4 equal at the named tag, 11 '
     'unbanked, none differing, none written (relay data/b704_cells_reach.txt). THE ORDER: the generator’s parser extended to the cell form in '
     'which the papers name SIDE-explicit-formula, priced by the forms the 11 table lines use; with it, G-CORRESPONDENCE-CURRENCY’s reach '
     'printed beside its figure -- how many of its counted rows name each of the 16 parsed kernels, and that SIDE-explicit-formula is not among '
     'them -- “a currency arm that does not parse the programme’s central kernel is reported with its figure, not after it”. Trigger: the '
     're-cut act b706. Status OPEN.'),
    ('*Appended 2026-10-22 by b704 beneath `W-ORD-E0-MET-CLASSK` (:15506), under `(R314)`(6) and the author’s word at the glossary prompt:*',
     ' companion rows taken up at b704 under (R314)(6), the grade settled at b703 -- h2_sign’_imp_rh and h2_sign_sum_iff_rh read DERIVES under '
     'E0 and by hand (relay data/b704_glossary.txt), the rows h2_sign’ and h2_sign_sum appended at relay data/glossary.txt :107-:108. The order '
     'stays open for its remaining content, the extension of E0’s MET lexicon to classK’, classKsum and acDeriv. Status OPEN.'),
]


def orders(*a):
    """the four trail lines of Components 2-3 appended to OPEN_TRAILS through b698's guarded landing, each beneath the order it annotates by
    its line (the ledger is append-only); data/b704_orders_line.json."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', h, NL + h + b + NL) for h, b in ORDERS], '%s_orders_line.json' % ACT, 'orders', entry=None,
         check=[('OPEN_TRAILS.md', K.ORDER_FACES, '*Appended 2026-10-21 by b702 beneath `W-ORD-CLASSK-WIDENING-HELD`'),
                ('OPEN_TRAILS.md', K.ORDER_E0, '*Appended 2026-10-22 by b703, under the author’s word at the classK’ prompt')], dry=dry)


# ### Component 5, the author's word at the README-figure prompt (2026-10-22): the order entered before the seal, landed alone
ORDER_README = (
    '*Appended 2026-10-22 by b704, under the author’s word at the README-figure prompt -- THE ORDER **`W-ORD-README-FIGURE-SCOPE`**, ENTERED:*',
    ' G-README-CURRENCY read 12 stale lines at b704 against b703’s 11 (relay data/b704_standing_figures.txt), the one new line PLACE-papers '
    'README.md :135, the v0.36–v0.37 append written verbatim on the author’s word under `(R314)`(5): relay tools/b703_standing_figures.py’s '
    'readme() counts every tag below the kernel’s highest as stale, the dated appends and the deposit note’s deposited versions included. '
    'THE ORDER: the arm reads the README’s currency lines, the lines that state current state, as relay data/b702_readme_currency.txt '
    'registered them, and not every tag; the dated ceiling appends (“Appended under the author’s ruling …”) and the deposit note’s deposited '
    'versions (SIDE-lv-conservation v0.10.0, SIDE-kernel v1.5) are records of their date, excluded by their text and not by line number. The '
    'repair a carry-time diff in data/b705_tool_repairs.txt; its control: b704’s README reading 0 stale on the repaired figure, and a mutated '
    'copy with the kernel line set back to v0.35 reading 1 and failing. At b704 G-README-CURRENCY is declared on the face as a carried '
    'failure, N3 scored REFUTED with :135 printed; the README and the figures tool not edited. Trigger: b705 at carry time. Status OPEN.')


def order_readme(*a):
    """the order of the author's word at the README-figure prompt, appended to OPEN_TRAILS through b698's guarded landing beneath the act's
    other orders (the ledger is append-only); data/b704_order_readme.json."""
    dry = 'dry' in a
    last = (jl('%s_orders_line.json' % ACT).get('lines') or [{}])[-1].get('line')
    land([('OPEN_TRAILS.md', ORDER_README[0], NL + ORDER_README[0] + ORDER_README[1] + NL)], '%s_order_readme.json' % ACT, 'order_readme', entry=None,
         check=[('OPEN_TRAILS.md', last, '*Appended 2026-10-22 by b704 beneath `W-ORD-E0-MET-CLASSK`')], dry=dry)


# ================================================================================ COMPONENT 4: THE RE-CUT OF day1/ONE_PAGE_PROOF.md ((R314)(7))
CUT_DOC = 'day1/ONE_PAGE_PROOF.md'
CUT_TABLE = 'b646_table_ONE_PAGE_PROOF.txt'
# ### the lines the cut changes, each with one case-exact needle and one wider case-insensitive needle (the two shapes of b702's search)
QUOTE_LINES = [
    (13, '**Theorem.** All nontrivial zeros of the Riemann zeta function', 'all nontrivial zeros of the riemann zeta function lie on re(s) = 1/2.'),
    (27, 'Four certifications, each from classical mathematics', 'four certifications, each from classical'),
    (34, 'Tate 1950, Lean-verified', 'conservation of spectra | tate 1950, lean-verified'),
    (38, 'If an off-line zero existed, some mechanism would produce it.', 'with everything surrounding it machine-checked'),
    (40, 'Therefore all nontrivial zeros of ζ(s) lie on Re(s) = 1/2.', 'therefore all nontrivial zeros of ζ(s)'),
    (44, 'decompose into combinations of C₁–C₇ with no eighth class', 'c₁–c₇ with no eighth class'),   # ### tightened once: "with no eighth class" also read PATHS :164/:166's "with no eighth class compensating", another sentence
    (48, 'The three routes to σ = 1/2 compile independently in the Lean 4 kernel', 'two commands settle it'),
    (70, 'step (8) states the one named premise (§27.3 five registers)', 'states the one named premise (§27.3 five registers)'),
    (86, 'the corpus names it openly at every site that depends on it', 'names it openly at every site that depends on it'),
    (98, 'NO terminal — `h2`, undischarged, manuscript-resident.', 'no terminal — `h2`, undischarged, manuscript-resident'),
]
CUT_HELD = (90, 91, 92)   # ### the Correspondence table's cells (:88-:92): N3, no cell by hand, the paper off the roster


def quote(*a):
    """data/b704_quote.txt (.json): data/b690_rules.txt row (2) at a paper cut, BEFORE the cut's commit -- each line the cut changes read at
    PLACE-papers HEAD, its two needles checked to stand in it, each searched with git grep -n -F across PLACE-papers' tracked tree at HEAD (the
    exact shape and the case-insensitive shape); every hit outside the cut lines themselves a quoting line, entered as a residue in the cut bank.
    The b670 form a paper cut takes (a `document`, no kernel, no merge), as b703's repaired arm reads it."""
    doc = (_show(PP, 'HEAD', CUT_DOC) or '').replace(chr(13), '').split(NL)
    rows, bad = [], []
    for ln, nd, wd in QUOTE_LINES:
        line = doc[ln - 1]
        if nd not in line or wd.lower() not in line.lower():
            bad.append((ln, nd in line, wd.lower() in line.lower()))
        h1 = [x for x in g(PP, 'grep', '-n', '-F', nd, 'HEAD', '--').split(NL) if x.strip()]
        h2 = [x for x in g(PP, 'grep', '-n', '-i', '-F', wd, 'HEAD', '--').split(NL) if x.strip()]
        own = lambda h: h.split(':', 2)[1] == CUT_DOC and int(h.split(':', 3)[2]) in [q[0] for q in QUOTE_LINES]   # noqa: E731
        rows.append(dict(line_no=ln, line=line, needle=nd, wide=wd, hits=[h for h in h1 if not own(h)], hits_wide=[h for h in h2 if not own(h)],
                         own=[h for h in h2 if own(h)]))
    if bad:
        sys.exit('### A NEEDLE DOES NOT STAND IN ITS OWN LINE %s -- NOTHING WRITTEN' % bad)
    quoting = sorted(set((h.split(':', 3)[1], int(h.split(':', 3)[2])) for r in rows for h in r['hits'] + r['hits_wide']))
    L = ['%s -- COMPONENT 4, (R314)(7): THE QUOTATION SEARCH BEFORE THE CUT`S COMMIT, data/b690_rules.txt row (2), OVER %s (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the lines the cut changes, read at PLACE-papers HEAD %s; each with a case-exact needle and a case-insensitive needle, both checked to' % g(PP, 'rev-parse', '--short=7', 'HEAD').strip(),
         '### stand in the line; each searched with git grep -n -F across the tracked tree at HEAD. The cut lines themselves are not counted (their own',
         '### hits printed). Rows are lines: :line | needle | hits | case-insensitive needle | hits, then every hit with its quoting line.', '']
    for r in rows:
        L.append('  :%-3d | %-62r %d hit(s) | %-50r %d hit(s) | own %d' % (r['line_no'], r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']), len(r['own'])))
        L += ['      %s' % h[:220] for h in sorted(set(r['hits'] + r['hits_wide']))]
    L += ['', '### THE QUOTING LINES, DISTINCT (file :line), EACH A RESIDUE: %s' % ('; '.join('%s :%d' % q for q in quoting) or 'NONE'),
          '### ### **LINES CHANGED BY THE CUT %d ; NEEDLES %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE ; SEARCHED BEFORE THE CUT`S COMMIT.**' % (
              len(rows), 2 * len(rows), len(quoting))]
    if 'dry' not in a:
        put_txt('%s_quote.txt' % ACT, L)
        put_json('%s_quote.json' % ACT, dict(at=utc(), document=CUT_DOC, base=g(PP, 'rev-parse', 'HEAD').strip(), rows=rows, quoting=[list(q) for q in quoting]))
    print(NL.join(L[6:]) if 'dry' in a else NL.join([x for x in L if x.startswith('  :')] + L[-2:]))


TROW = re.compile(r'^  :(\d+) \| [^|]+\| [^|]+\| [^|]+\| [^|]+\| (MATCHES|OVERREACHES|UNLICENSED|UNDERSTATES) ; "(.*)" ; (.*)$')


def cutbank(*a):
    """data/b704_cut.txt (.json): (R314)(7), the re-cut of day1/ONE_PAGE_PROOF.md by the b670 method -- each non-MATCHES row of its table
    (relay data/b646_table_ONE_PAGE_PROOF.txt) with its STATED text searched whitespace-normalized in the document at the base and now, the
    row met where it no longer stands; the Correspondence cells held under N3; the residues from the quotation search (data/b704_quote.json).
    `cutbank [<cut commit>]`: with the cut's PLACE-papers commit named, the bank's base is that commit's parent (`<sha>^`) and "now" its tree."""
    commit = a[0] if a and re.match(r'^[0-9a-f]{7,40}$', a[0]) else None
    base_ref = (commit + '^') if commit else 'HEAD'
    norm = lambda s: ' '.join((s or '').split())   # noqa: E731
    base = norm(_show(PP, base_ref, CUT_DOC))
    now = norm(_show(PP, commit, CUT_DOC) if commit else rd(os.path.join(PP, CUT_DOC)))
    rows = []
    for l in rdn(CUT_TABLE).split(NL):
        m = TROW.match(l)
        if not m or m.group(2) == 'MATCHES':
            continue
        ln, v, st, act = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        held = ln in CUT_HELD
        rows.append(dict(line=ln, verdict=v, stated=st, action=act.split(' -- ')[0][:60], held=held, base=norm(st) in base, now=norm(st) in now))
    mt = [(int(m.group(1)), m.group(3)) for m in (TROW.match(l) for l in rdn(CUT_TABLE).split(NL)) if m and m.group(2) == 'MATCHES']
    mt_lost = [(ln, st) for ln, st in mt if norm(st) in base and norm(st) not in now]
    q = jl('b704_quote.json')
    res = [list(x) for x in (q.get('quoting') or [])]
    dist = [r for r in rows if r['verdict'] in ('OVERREACHES', 'UNLICENSED')]
    und = [r for r in rows if r['verdict'] == 'UNDERSTATES']
    before = sum(1 for r in dist if r['base'])
    after = sum(1 for r in dist if r['now'])
    L = ['%s -- COMPONENT 4, (R314)(7): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the document: %s (v1.0.1), named by b652`s order passing to the companions and the author`s word on the tie (relay data/b704_tie.txt), b674`s' % CUT_DOC,
         '### measures read in their written order. Its table: relay data/%s, pinned at 96779e5, 100 lines, sha256 29f18b706bda30bb = the base`s. The' % CUT_TABLE,
         '### cut: each non-MATCHES row`s ACTION applied by the Edit tool on the rows alone, the paper`s title, opening label lines and file name untouched',
         '### (W-ORD-KEYSTONE-HEADS held); the Correspondence cells :90-:92 held under N3 (the paper off the roster, no generator writes them).',
         '### the base %s ; now %s.' % (base_ref, commit or 'the working tree'), '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row`s STATED text searched whitespace-normalized in the document at the base and now,',
         '### the row met where it no longer stands. Rows: base line | verdict | applied or HELD | stands at the base | stands now | the STATED text:']
    for r in rows:
        L.append('  :%-3d | %-11s | %-7s | base %-5s | now %-5s | %s' % (r['line'], r['verdict'], 'HELD' if r['held'] else 'applied', r['base'], r['now'], r['stated'][:110]))
        if r['held']:
            L.append('        HELD: a cell of the paper`s Correspondence table (base :88-:92); N3: no Correspondence cell by hand, and the paper is off the 19-table roster')
    unmet = [r for r in rows if not r['held'] and r['now']]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b704_quote.txt, two shapes, the search run before the cut`s commit): each quoting',
          '### line, file :line -- the monograph`s copies of this page (day1/A_Place_to_Stand.md and its versioned copies), the deposited and archived',
          '### copies, and four other documents quoting it (ERRATA :417, THE_LOAD_BEARING_MAP :373, THE_RIEMANN_PATHS_CLUSTER_SPINE :61,',
          '### THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY :13), each carried by its own table or frozen as deposited; none written:']
    L += ['  %s :%d' % (f, n_) for f, n_ in res]
    L += ['', '### THE ROWS APPLIED THAT STILL STAND: %s' % (['%d %s' % (r['line'], r['stated'][:60]) for r in unmet] or 'NONE'),
          '### UNDERSTATES (not in the distance): %d at the base, %d now (the held cells :92 standing)' % (sum(1 for r in und if r['base']), sum(1 for r in und if r['now'])),
          '### THE CONTROL, THE MATCHES ROWS: %d at the base ; standing now %d ; no longer standing %s' % (
              sum(1 for _l, st in mt if norm(st) in base), sum(1 for _l, st in mt if norm(st) in now), ['%d %s' % (ln, st[:60]) for ln, st in mt_lost] or 'NONE'),
          '### ### **THE DISTANCE BY THE b670 METHOD: BEFORE %d, AFTER %d ; ROWS APPLIED %d ; HELD %d (CORRESPONDENCE CELLS) ; QUOTING LINES %d ENTERED AS RESIDUES.**' % (
              before, after, sum(1 for r in rows if not r['held']), sum(1 for r in rows if r['held']), len(res))]
    if 'dry' not in a:
        put_txt('%s_cut.txt' % ACT, L)
        put_json('%s_cut.json' % ACT, dict(at=utc(), document=CUT_DOC, base=base_ref if commit else '', before=before, after=after,
                                          held=[r['line'] for r in rows if r['held']], residues=res,
                                          rows=[dict((k, v) for k, v in r.items()) for r in rows]))
    print(NL.join(L[-4:]))


def quotecheck(*a):
    """a print only: G-RULE-RECUT-QUOTE's reading (tools/rule_arms.py, unedited) over the quote banks, restricted to this act's -- the search
    before the cut's own PLACE-papers commit, every quoting line entered in the cut bank's residues."""
    import rule_arms as RA
    S = RA.sources(ACT, None, K.ANCHOR, K.PARTS, pre_relay=None, pre_pp=None)
    mine = [q for q in S['quotes'] if q['act'] == int(ACT[1:])]
    S2 = dict(S)
    S2['quotes'] = mine
    S2['cut_banks'] = dict((k, v) for k, v in S['cut_banks'].items() if k == int(ACT[1:]))
    for q in mine:
        print('  %s kind %s ; merge %s ; search at %s ; before the merge %s ; needled %s ; quoting %d ; unentered %d' % (
            q['bank'], q.get('kind', 'kernel'), (q['merge'] or ['-'])[0][:7], q['at'], bool(q['merge'] and q['at'] and q['at'] < q['merge'][1]),
            q['needled'], len(q['quoting']), len(q['unentered'])))
    print('  the arm over b704`s banks: %s ; over every bank: %s' % (RA.reading('G-RULE-RECUT-QUOTE', S2), RA.reading('G-RULE-RECUT-QUOTE', S)))


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
        L.append('    (i) the rule`s condition, equal OVERREACHES counts: %s -- %s' % (', '.join('%s %d' % (t['doc'], t['over']) for t in tabs), 'MET' if len(ov) == 1 else 'NOT MET'))
        if len(ov) > 1:
            L += ['        the tie stands at the agenda`s count (OVERREACHES + UNLICENSED: %s), a tie neither b674`s rule nor b666`s beneath it' % (
                      ', '.join('%s %d + %d' % (t['doc'], t['over'], t['unl']) for t in tabs)),
                  '        (OPEN_TRAILS :14238, kernels at the same OVERREACHES count) names; the rule`s measures printed beside the gap, none applied:',
                  '        OVERREACHES %s ; rows outside LICENSED/CITED of any kind %s ; the table`s CLAIMS %s' % (
                      ', '.join('%s %d' % (t['doc'], t['over']) for t in tabs), ', '.join('%s %d' % (t['doc'], t['outside']) for t in tabs),
                      ', '.join('%s %d' % (t['doc'], t['claims']) for t in tabs)),
                  '    ### THE RULES DO NOT REACH THIS TIE -- RAISED, NOTHING NAMED']
            tabs_raised = True
            cand = []
        else:
            cand = tabs
        if cand:
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
        if pick is None and cand:
            L.append('    ### THE RULE ENDS IN A TIE -- RAISED, NOTHING NAMED')
    word = jl('%s_tie_word.json' % ACT).get('pick') if os.path.exists(os.path.join(D, '%s_tie_word.json' % ACT)) else None
    if pick is None and word:
        pick = next((t for t in tabs if t['doc'] == word), None)
        L.append('    THE AUTHOR`S WORD (relay data/b704_tie_word.json): %s' % word)
    nxt = [r for r in comp if r['count'] < (top or 0)][:2]
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER AND b674`S TIE-BREAK: %s (A COMPANION ; THE TOP COUNT %s, %d DOCUMENTS AT IT ; %s ; THE NEXT BY COUNT %s).**' % (
        pick['doc'] if pick else '### NONE NAMED', top, len(at_top),
        ('THE AUTHOR`S WORD: b674`S MEASURES READ IN THEIR WRITTEN ORDER, THE FIRST THAT SEPARATES DECIDING (OVERREACHES)' if word else
         '### THE RULES DO NOT REACH THE TIE') if len(tabs) > 1 else 'NO TIE',
        '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in nxt))]
    if 'dry' not in a:
        put_txt('%s_tie.txt' % ACT, L)
        put_json('%s_tie.json' % ACT, dict(at=utc(), top=top, at_top=[t['doc'] for t in tabs], pick=pick['doc'] if pick else None,
                                          tables=[dict((k, v) for k, v in t.items() if k != 'row') for t in tabs]))
    print(NL.join(L))


# ================================================================================ THE LATE ROUTES (b703's, carried with b704's names)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor. Rebound here: b703's
    import rebound b698's to its own, which reads b703's session."""
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('%s/%s.jsonl' % (PROJ, sid), anc, '%s/%s/subagents' % (PROJ, sid))
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    rows.sort(key=lambda r: r['ts'])
    bg = R._bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


R.capture = capture
prev_capture = R.prev_capture
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b703's route with b704's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window, the
    local lean reading (N1), the dispatch (one, the probe's), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves
    and deletes by shape, the outbound requests. data/b704_commands.txt (.json)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if DISPATCH_CMD.search(QUOTED.sub('""', r['cmd']))]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = R.outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCH, THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, its own session %s, from its post-push combine to that session`s end): '
              '%d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (one ordered this act, N1: the faces probe) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A PIPE OF ANY KIND, read outside quoted strings (%d):' % len(anypipe)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in anypipe] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R314)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; PIPES OF ANY KIND %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(anypipe), len(pyreads), len(mv), good,
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        for r, o in hits:
            print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV, session=R.PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], any_pipes=[r['n'] for r in anypipe], py_programs=[r['n'] for r in pyreads],
                                           moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


_kerns = R._kerns                  # ### b703's list (b698's and SIDE-substrate-cluster), rebound by b703's import


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (read after the probe branch`s deletes; no kernel written after this read)' % len(ks))


def _standing():
    import b703_worklist as K703
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B703_FACE.split('/')))) - set(K703.ACT_ARMS)) | set(K.STANDING_ADDED))


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


# ================================================================================ COMPONENT 5: THE CARRY-TIME REPAIRS ((R314)(2), the author's word at the sort)
REPAIR_ROWS = [
    ('(1) tools/b704_record.py `reads`, the read bank -- ANSWERS the author`s word at the read-rule sort (2026-10-22, "write the arm for the traceable '
     'class"): b698`s route (tools/b698_record.py :1219) recorded only whether an offset and a limit were passed, so it could not see a limit above two '
     'hundred; the repaired route records each call`s offset and limit VALUES, reads the cap of two hundred and the time of the word that named it '
     'from the session, and prints a call before the word carrying both as the cap`s precursor, not counted (the author`s word at the arm`s '
     'baseline prompt). The repair is approved by that word and sealed before the suite runs. The arm it serves: tools/b704_read_arm.py, '
     'G-READ-RULE-STANDING, its controls on mutated copies of the repaired bank`s form (data/b704_read_arm_control.txt). The diff of b698`s '
     '`reads` against b704`s, then the new functions and the arm`s tool whole.', None, ('reads', ('_cap_word_at', '_read_verdict')), 'b704_read_arm.py'),
    ('(2) tools/b704_record.py `capture`, the command capture -- ANSWERS the carry: b703`s record tool, imported here for its repaired readers, '
     'rebinds b698`s `capture` at its import to its own, which reads b703`s session (e5bcf1d0) from (R313)`s line; b704 runs in a new session '
     '(fb68aaef), so the capture is rebound to b704`s own, reading this act`s session from (R314)`s line and any continuation. The new function.',
     None, (None, ('capture',)), None),
]


def repairs(*a):
    """data/b704_tool_repairs.txt: the carry-time repairs, each with the order or carry it answers, its diff written by this route (difflib, the
    plain unified_diff of whole lines; the old text from b698's sealed tool)."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS (%s)' % (ACT, utc()), '',
         '### rows are repairs with what they answer: the tool and its part ; what it answers ; the form. Each diff beneath its row, written by',
         '### this route (difflib over the function`s source: b698`s sealed tool against this act`s; a new file printed whole).', '']
    n = 0
    for text, whole, fns, newfile in REPAIR_ROWS:
        L += ['  ' + text, '']
        if fns:
            main_fn, extra = fns
            if main_fn:
                old = R._fn_src(rd(os.path.join(T, 'b698_record.py')), main_fn).split(NL)
                new = R._fn_src(rd(os.path.join(T, 'b704_record.py')), main_fn).split(NL)
                d = list(difflib.unified_diff(old, new, 'tools/b698_record.py %s (sealed)' % main_fn, 'tools/b704_record.py %s (this act)' % main_fn, lineterm=''))
                n += len(d)
                L += ['      ' + x for x in d] + ['']
            for fn in extra:
                new = R._fn_src(rd(os.path.join(T, 'b704_record.py')), fn).split(NL)
                d = list(difflib.unified_diff([], new, '(none)', 'tools/b704_record.py %s (this act)' % fn, lineterm=''))
                n += len(d)
                L += ['      ' + x for x in d] + ['']
        if newfile:
            new = rd(os.path.join(T, newfile)).replace('\r', '').split(NL)
            d = list(difflib.unified_diff([], new, '(none)', 'tools/%s (this act, new)' % newfile, lineterm=''))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; SHARED TOOLS EDITED 0 ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES AT b704, AND THE GENERATOR'S REACH
def figures(*a):
    """data/b704_standing_figures.txt (.json): the four figures by relay tools/b703_standing_figures.py (unedited), read against b703's baseline
    (data/b703_standing_figures.json); beside G-CORRESPONDENCE-CURRENCY its reach (the author's word at the cells prompt, W-ORD-CORRESPONDENCE-
    EF-REACH): the rows it counts that name each of the 16 kernels the generator parses, and SIDE-explicit-formula not among them."""
    import b703_standing_figures as SF
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b703_standing_figures.json')
    f = SF.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    cr = (f.get('correspondence') or {}).get('papers') or []
    reach = {}
    gen = rdn('b704_correspondence_run.txt')
    tabled = sorted(set(re.findall(r'^    (SIDE-[\w-]+)\s+(?:READ|v\d|###)', gen, re.M)))
    for x in cr:
        for k in tabled:
            reach[k] = reach.get(k, 0)
    counted = [r for p in cr for r in (p.get('changed_rows') or [])]   # ### the rows the figure counts: each paper's changed-statement rows
    for r in counted:
        k = r.get('kernel') if isinstance(r, dict) else None
        reach[k or '(no kernel named)'] = reach.get(k or '(no kernel named)', 0) + 1
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b704 AGAINST b703`S BASELINE, AND G-CORRESPONDENCE-CURRENCY`S REACH (%s)' % (ACT, utc()), '',
         '### by relay tools/b703_standing_figures.py (unedited), %.0f s; each arm fails on a regression from the previous act`s figure (b703`s).' % (t1 - t0), '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        L.append('  %-15s b704 %s ; b703 %s ; %s' % (k, (f.get(k) or {}).get('figure'), (base.get(k) or {}).get('figure'),
                                                   'AT OR BELOW' if isinstance((f.get(k) or {}).get('figure'), int) and isinstance((base.get(k) or {}).get('figure'), int)
                                                   and f[k]['figure'] <= base[k]['figure'] else '### ABOVE OR UNREAD'))
    L += ['', '### G-CORRESPONDENCE-CURRENCY`S REACH (W-ORD-CORRESPONDENCE-EF-REACH): the kernels the generator parses in a shaped table (relay',
          '### data/b704_correspondence_run.txt), %d: %s ; SIDE-explicit-formula among them %s ; the rows the arm counts (each paper`s changed-' % (
              len(tabled), ', '.join(tabled), 'SIDE-explicit-formula' in tabled),
          '### statement rows) %d, by kernel: %s ; the rows it reads, current %d, behind %d, unread %d, over %d papers' % (
              len(counted), '; '.join('%s %d' % kv for kv in sorted(reach.items())) or 'NONE BY KERNEL', sum(p.get('current') or 0 for p in cr),
              sum(p.get('behind') or 0 for p in cr), sum(p.get('unread') or 0 for p in cr), len(cr)),
          '### THE README`S STALE LINES, each with its kernel and cited tag: %s' % '; '.join(
              ':%d %s %s (highest %s)' % (r['line'], r['kernel'], r['cited'], r['highest']) for r in ((f.get('readme') or {}).get('rows') or [])
              if r.get('state') == 'STALE'),
          '### ### **FIGURES AT b704: CORRESPONDENCE %s ; README %s ; PARTNERS %s ; PINS %s -- AGAINST b703`S %s, %s, %s, %s ; THE REACH %d KERNELS, '
          'SIDE-explicit-formula NOT AMONG THEM.**' % tuple([(f.get(k) or {}).get('figure') for k in ('correspondence', 'readme', 'partners', 'pins')]
                                                            + [(base.get(k) or {}).get('figure') for k in ('correspondence', 'readme', 'partners', 'pins')] + [len(tabled)])]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), reach=dict(tabled=tabled, rows=reach), **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L))


# ================================================================================ THE SCORES: (N1)-(N5) OF (R314)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b704_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK, SK, SCORE_KEYS = R.NK, R.SK, R.SCORE_KEYS
read_score_row, read_head = R.read_score_row, R.read_head
N5_RELAY_DATA = ('act_roots.txt', 'b703_closing_push_out.txt', 'b675_corrigenda.txt', 'glossary.txt')


def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _n1():
    """N1: no lean process on this host; one runner dispatch, the probe's, read by its run id with its artifact's sha256 verified."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    pj = jl('%s_runner_%s_probe.json' % (ACT, K.KERNEL))
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == 1 and len(dj) == 1 and dj[0].get('ref') == K.PROBE_TIP \
        and dj[0].get('run_id') == pj.get('run_id') == K.PROBE_RUN and bool(pj.get('artifact_sha256'))
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches in the capture: %s (relay data/b704_commands.json); the '
        'dispatches bank (relay data/b704_dispatches.json): %s -- the probe branch`s tip, its run, the run read for it by its id, its artifact`s '
        'sha256 %s; no kernel re-cut, so no second dispatch' % (
            cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread',
            ['%s run %s' % ((d.get('ref') or '')[:7], d.get('run_id')) for d in dj], (pj.get('artifact_sha256') or 'UNREAD')[:16]))


def _n2():
    """N2: the probe's prints at v0.37 equal b703's run prints for every name both carry; every line of the faces diff names its cause; the
    header reads v0.37."""
    pj = jl('%s_runner_%s_probe.json' % (ACT, K.KERNEL))
    fj = jl('%s_faces_diff.json' % ACT)
    eq = pj.get('n2_both', 0) > 0 and not pj.get('n2_diff')
    caused = bool(fj.get('rows')) and fj.get('no_cause') == 0
    ok = eq and caused and fj.get('head_v037') is True and pj.get('ok') is True
    return ('HELD' if ok else 'REFUTED'), (
        'the names this probe and b703`s two runs both print: %s, axioms equal %s, differing %s (relay data/b704_runner_SIDE-explicit-formula_probe.json); '
        'the faces diff`s changed lines %d, without a cause %s, by cause %s; the head at v0.37 %s (relay data/b704_faces_diff.json)' % (
            pj.get('n2_both'), eq, pj.get('n2_diff') or 'NONE', len(fj.get('rows') or []), fj.get('no_cause'), fj.get('by_cause'), fj.get('head_v037')))


def _n3():
    """N3: no Correspondence cell written by hand; the cell count the dry run prints equals the count written; the four standing figures at or
    below b703's once this act's regenerations land."""
    run_ = rdn('%s_correspondence_run.txt' % ACT)
    dry_ = rdn('%s_correspondence_dry.txt' % ACT)
    m_run = re.search(r'CELLS CHANGED (\d+) ; FILES CHANGED (\d+)', run_)
    m_dry = re.search(r'THE GENERATOR`S CELLS CHANGED (\d+)', dry_)
    fj, bj = jl('%s_standing_figures.json' % ACT), jl('b703_standing_figures.json')
    figs = [((fj.get(k) or {}).get('figure'), (bj.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins')]
    below = all(isinstance(a_, int) and isinstance(b_, int) and a_ <= b_ for a_, b_ in figs)
    eq = bool(m_run) and bool(m_dry) and m_run.group(1) == m_dry.group(1) and m_run.group(2) == '0'
    pp_cells = [x for x in g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if x.strip() and x not in K.PP_WRITTEN]
    ok = eq and below and not pp_cells
    st = [r for r in ((fj.get('readme') or {}).get('rows') or []) if r.get('state') == 'STALE']
    new = sorted(set(r['line'] for r in st) - set(r['line'] for r in ((bj.get('readme') or {}).get('rows') or []) if r.get('state') == 'STALE'))
    return ('HELD' if ok else 'REFUTED'), (
        'the generator`s run wrote %s cells in %s files, its dry run %s cells (relay data/b704_correspondence_run.txt, data/b704_correspondence_dry.txt): '
        'equal %s; no cell by hand -- PLACE-papers files beyond the named ones %s; the four figures at b704 against b703`s (correspondence, '
        'README, partners, pins) %s, at or below %s (relay data/b704_standing_figures.json); the README`s stale lines not stale at b703: %s -- %s' % (
            m_run.group(1) if m_run else '?', m_run.group(2) if m_run else '?', m_dry.group(1) if m_dry else '?', eq, pp_cells or 'NONE', figs, below,
            ', '.join(':%d' % n for n in new) or 'NONE',
            ':135 the v0.36–v0.37 append written verbatim on the author`s word, naming v0.36 as the tag of its date (defect (n); G-README-CURRENCY '
            'declared on the face as a carried failure; W-ORD-README-FIGURE-SCOPE)' if new == [135] else 'read as printed'))


def _n4():
    """N4: the distance after the cut at or below the distance before by the b670 method; the quotation search before the cut's commit, its
    hit count printed."""
    cj, qj = jl('%s_cut.json' % ACT), jl('%s_quote.json' % ACT)
    qt = rdn('%s_quote.txt' % ACT)
    q_at = _iso_epoch(qj.get('at') or '')
    c_ct = _git_ct(PP, K.C4_PP)
    hits = re.search(r'QUOTING LINES (\d+)', qt)
    ok = isinstance(cj.get('before'), int) and isinstance(cj.get('after'), int) and cj['after'] <= cj['before'] and bool(q_at) and bool(c_ct) \
        and q_at < c_ct and bool(hits)
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by the b670 method %s -> %s (relay data/b704_cut.json); the quotation search at %s, the cut`s commit %s at %s: before it %s; '
        'its quoting lines printed %s (relay data/b704_quote.txt)' % (
            cj.get('before'), cj.get('after'), qj.get('at'), K.C4_PP, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(c_ct)) if c_ct else '-',
            bool(q_at and c_ct and q_at < c_ct), hits.group(1) if hits else 'UNREAD'))


def _n5():
    import b633_record as R3
    import b703_worklist as K703
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    main_ok = ef_main == K.EF_V037 and not g(EF, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b704_', x)]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b704_|audit_b704_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B703_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(EF, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl.startswith(pre_gl) and len([l for l in now_gl[len(pre_gl):].split(NL) if l.strip() and not l.startswith('#')]) == 2
    ok = k_ok and main_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ and arms_ok and not amended \
        and not ident and not chained and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-explicit-formula`s '
            'main at v0.37 and no tag past it: %s; the standing arms added beyond b703`s face, the act arms apart: %s (the author`s one: %s); shared '
            'tools edited: %s; sealed tools not agreeing: %s; commits amended after the seal: %s; deletes with anything chained after: %s; one git write '
            'per message (%s): %s; PLACE-papers beyond the named files (the two ledgers, the README, the faces page, the cut paper): %s; papers moved or '
            'renamed: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, the corrigenda bank, the glossary and '
            'b703`s push-out bank: %s; the glossary appended by two entries alone: %s; outbound requests other than git and gh %d, an identifier of '
            'the author in %s' % (K.DRAFT, k_ok, main_ok, added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                                   chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, len(ob),
                                   [r['line'] for r in ident] or 'NONE'))


def scores(*a):
    """`scores [dry]` writes data/b704_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b704_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
num_word = P3.num_word


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b704 — lane two, act one hundred and thirty-one, the re-cut act under (R314): b703 at its weight; its unlettered read by '
            'corrigendum and the read rule sorted into an arm; the faces chain re-probed at v0.37 with two nodes; the Correspondence cells of a '
            'moved tag read; the README, the glossary companions and One Page Proof re-cut')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    ol = [x.get('line') for x in (jl('%s_orders_line.json' % ACT).get('lines') or []) + (jl('%s_order_readme.json' % ACT).get('lines') or [])]
    fd = jl('%s_faces_diff.json' % ACT)
    cut = jl('%s_cut.json' % ACT)
    reach = rdn('%s_cells_reach.txt' % ACT)
    rm = re.search(r'EQUAL (\d+) ; DIFFERS (\d+) ; NO PRINT BANK AT THE TAG (\d+) ; NO THEOREM OR NO TAG (\d+)', reach)
    run_ = re.search(r'CELLS CHANGED (\d+)', rdn('%s_correspondence_run.txt' % ACT))
    rq = re.search(r'QUOTING LINES (\d+)', rdn('%s_quote.txt' % ACT))
    fj_ = jl('%s_standing_figures.json' % ACT)
    gl = rdn('%s_glossary.txt' % ACT)
    gls = re.findall(r"the rows in relay data/glossary.txt after the append: h2_sign' :(\d+); h2_sign_sum :(\d+)", gl)
    rmd = rdn('%s_readme.txt' % ACT)
    rk = re.search(r'THE KERNEL LINE AT :(\d+) ; THE APPEND AT :(\d+)', rmd)
    return dict(corr_line=co.get('entry_line', '-'), orders=ol + ['-'] * 4, faces_lines=len(fd.get('rows') or []), by_cause=fd.get('by_cause') or {},
                before=cut.get('before', '-'), after=cut.get('after', '-'), held=len(cut.get('held') or []), quoting=rq.group(1) if rq else '-',
                equal=rm.group(1) if rm else '-', unbanked=str(int(rm.group(3)) + int(rm.group(4))) if rm else '-', cells=run_.group(1) if run_ else '-',
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                gl=gls[0] if gls else ('-', '-'), kline=rk.group(1) if rk else '-', append=rk.group(2) if rk else '-')


def _title():
    f = _figs()
    return ('## The faces page at v0.37 with the finite-sum equivalence and the wider-class direction as nodes; %s Correspondence cells regenerated '
            'at v0.37; the README’s kernel line and the v0.36–v0.37 append; One Page Proof re-cut: %s rows outside LICENSED/CITED to %s' % (
                f['cells'], f['before'], f['after']))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) the faces probe run as the root CircuitClosure.lean of the scratch branch probe-b704 cut from v0.37, on the author’s word -- the '
            'runner at v0.37 runs no #print sig -- the branch deleted locally and at the remote once its bank was committed; (2) the faces page written '
            'twice, at 5cf62a2 and again at c9b2e55 on the author’s word, the glossary companions landing after its first write; (3) the generator '
            'writing 0 cells, SIDE-explicit-formula outside the kernels it parses, the 15 prose mentions read against the probe and the 11 unbanked '
            'raised, W-ORD-CORRESPONDENCE-EF-REACH entered; (4) the tie at the agenda’s count 22, which b674’s rule and b666’s do not reach, settled '
            'on the author’s word by b674’s measures in their written order, OVERREACHES 21 against 14; (5) the cut’s :86 register re-quoted from '
            'README :115 verbatim, one MATCHES row’s wording moving with it, the UNDERSTATES rows outside the Correspondence cells applied and the '
            'cells :90-:92 held; (6) G-READ-RULE-STANDING written on the author’s word, reading b704 from the word that named the cap, failing at b704 '
            'on (i) and (o) and declared on the face; (7) the companion clause of W-ORD-E0-MET-CLASSK annotated by a line appended beneath it, OPEN_TRAILS '
            'being append-only; (8) G-README-CURRENCY at 12 against 11, its one new line the ordered append at README :135, declared failing on '
            'the author’s word with N3 refuted and W-ORD-README-FIGURE-SCOPE entered for b705; (9) G-WORKFLOW-FILES failing on the probe’s print '
            'step, 63 of its 109 names unknown to the chain’s 43 target modules, declared, no second dispatch; (10) the %s navigator %s (%s) and '
            'the seat’s %s defect%s as lettered' % (
                num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', letters, num_word(seat), '' if seat == 1 else 's'))


def _finding_text():
    """the FINDINGS entry, composed before the root: its head line the result sentence; its scores line from the scores bank alone (data/b686_rules.txt
    row (1)); the root carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The faces page now reads at SIDE-explicit-formula v0.37 (38e2734): the chain from Mathlib’s RiemannHypothesis to the ceiling sentence '
         're-probed on one runner dispatch, every cell b702’s page carried unchanged at the new tag, and two compiled terminals added as nodes -- '
         'h2_sign_sum_iff_rh, Weil positivity on finite sums of autocorrelations equivalent to RH, and h2_sign’_imp_rh, positivity on the wider class '
         'implying RH, its converse open. The README names v0.37 and carries the v0.36–v0.37 sentence; the glossary carries h2_sign’ and h2_sign_sum; '
         'One Page Proof’s rows outside LICENSED/CITED fall from %s to %s, its Correspondence cells at :90-:92 held; no Correspondence cell is regenerated, the '
         'generator parsing no kernel cell that names SIDE-explicit-formula.' % (f['before'], f['after']), '',
         '*Filed at b704 on the author’s ruling `(R314)` and the author’s words at its prompts; %d question%s put. Banks: relay '
         '`data/b704_runner_SIDE-explicit-formula_probe.txt`, `data/b704_faces_diff.txt`, `data/b704_correspondence_dry.txt`, `data/b704_cells_reach.txt`, '
         '`data/b704_readme.txt`, `data/b704_glossary.txt`, `data/b704_tie.txt`, `data/b704_quote.txt`, `data/b704_cut.txt`, `data/b704_read_sort.txt`, '
         '`data/b704_corrigendum.txt`, `data/b704_tool_repairs.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R314)`(1)-(2)): b703 entered at its weight (FINDINGS :%s); the generated entry at FINDINGS :%s letters (m), the '
         'project-state memory file read whole after b703’s closing; the corrigenda bank appended at row (24); the sealed face, the trail and the '
         'root-named banks unedited.' % (c1_[0], f['corr_line']), '',
         '**The read rule** (`(R314)`(2)): b703’s breaches sorted by trace (relay data/b704_read_sort.txt) -- (k) thirteen calls and (l) one, rows of '
         'its read bank, (m) in none; on the author’s word the arm for the traceable class, G-READ-RULE-STANDING, written over the repaired read bank '
         '(each call’s offset and limit, the cap of two hundred), its controls on mutated copies as wanted (relay data/b704_read_arm_control.txt); it '
         'reads b704 from the word that named the cap and fails on (i) and (o), four calls, declared; (m)’s kind stays prose.', '',
         '**The faces page** (`(R314)`(3), N2): run 39721668586 on the scratch branch probe-b704 (one path, the root file), 568 of 568 cells, the '
         'artifact’s sha256 agreeing, its print step reading 46 of the 109 listed names (defect (p)); the node list’s successor with every row unchanged but its tag and the two nodes on the author’s word; the page '
         'by the generator, %d changed lines each with its cause (relay data/b704_faces_diff.txt); the head at v0.37.' % f['faces_lines'], '',
         '**The cells** (`(R314)`(4), N3): the generator run and %s cells written, SIDE-explicit-formula outside its 16 parsed kernels; the 15 prose '
         'mentions read against the probe -- %s equal at the named tag, %s unbanked, none differing -- raised, no cell or prose line written '
         '(relay data/b704_cells_reach.txt); W-ORD-CORRESPONDENCE-EF-REACH entered.' % (f['cells'], f['equal'], f['unbanked']), '',
         '**The README** (`(R314)`(5)): the kernel line at v0.37 (now :%s; the ruling’s :160, the navigator’s (g)) and the v0.36–v0.37 append at :%s, '
         'the author’s sentence verbatim, on the word (relay data/b704_readme.txt).' % (f['kline'], f['append']), '',
         '**The glossary** (`(R314)`(6)): h2_sign’ and h2_sign_sum appended at :%s and :%s after E0 and the hand grade both read DERIVES for '
         'h2_sign’_imp_rh and h2_sign_sum_iff_rh (relay data/b704_glossary.txt); the faces page written again for them.' % f['gl'], '',
         '**The re-cut** (`(R314)`(7), N4): day1/ONE_PAGE_PROOF.md, on the author’s word at the tie (relay data/b704_tie.txt); the quotation search before '
         'the cut’s commit, %s quoting lines entered as residues (relay data/b704_quote.txt); %s rows outside LICENSED/CITED to %s by the b670 method, '
         'the cells :90-:92 held (relay data/b704_cut.txt; PLACE-papers 02b7aad). The keystone heads held under W-ORD-KEYSTONE-HEADS.' % (
             f['quoting'], f['before'], f['after']), '',
         '**The orders** (`(R314)`(3)-(6) and the author’s words): W-ORD-FACES-PROBE-CURRENT discharged (OPEN_TRAILS :%s); W-ORD-WORKFLOW-PROBE-STEP '
         '(:%s) and W-ORD-CORRESPONDENCE-EF-REACH (:%s) entered, trigger b706; W-ORD-E0-MET-CLASSK’s companion clause taken up (:%s); '
         'W-ORD-README-FIGURE-SCOPE entered (:%s), trigger b705 at carry time.' % tuple(f['orders'][:5]), '',
         '**The standing arms**: the four figures at b704 -- %s, %s, %s, %s -- against b703’s 0, 11, 131, 0 (relay data/b704_standing_figures.txt); '
         'the README’s one new stale line :135, the v0.36–v0.37 append written on the author’s word and naming the tag of its date, so '
         'G-README-CURRENCY is declared failing on the face and N3 refuted on it; G-READ-RULE-STANDING added on the author’s word and declared '
         'failing on (i) and (o); G-WORKFLOW-FILES declared failing on the probe’s print step, 46 of 109 names printed (p).' % (f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and raised; %d answer check%s, each before its '
         'answer was acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the page, the README and the paper now say one thing at one tag -- Weil positivity on '
         'classK equivalent to RH, on finite sums equivalent, on the wider class implying it -- and the paper that argued for RH now states it as the '
         'one open clause’s equivalent. It strengthens the programme’s offering of a located clause: the clause’s compiled faces are read from one '
         'probe, and the corpus’s shortest proof-claim no longer says more than the kernel compiles.', '',
         '**Carried to:** b705 (W-ORD-README-FIGURE-SCOPE at carry time; the closure join, W-ORD-P3-CONTOUR-SIGMA, the detection law, the band '
         'witness, the I-6 ranking, W-ORD-E0-MET-CLASSK); '
         'b706 (W-ORD-PAPER-PARTNER-COPIES, W-ORD-WORKFLOW-PROBE-STEP, W-ORD-CORRESPONDENCE-EF-REACH); b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5); '
         'W-ORD-KEYSTONE-HEADS on its trigger; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R314) ratified.** (1) b703 at its weight. (2) The corrigendum and the read rule. (3) The faces re-probe. (4) The Correspondence cells. '
             '(5) The README. (6) The glossary companions. (7) The re-cut. (8) The branches. (9) The readfirst bank. (10) The draft held at v5. (11) The '
             'acts after.', '',
             '**Entered:** FINDINGS.md:%s (b703`s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s-:%s (one discharge, three orders, '
             'one annotation); this record.' % (c1_[0], f['corr_line'], fj.get('entry_line'), f['orders'][0], f['orders'][4]), '',
             '**Act root:** b704 `%s` (previous `%s`, b703`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b704_author_answers.txt); the root`s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The faces page:** at v0.37, the two nodes added, %d lines over the act each with its cause (relay data/b704_faces_diff.txt; PLACE-papers '
             '5cf62a2, c9b2e55).' % f['faces_lines'], '',
             '**The cells:** %s written; %s mentions equal, %s unbanked, raised (relay data/b704_cells_reach.txt).' % (f['cells'], f['equal'], f['unbanked']), '',
             '**The README:** the kernel line and the v0.36–v0.37 append, on the word (PLACE-papers 05c6dd6; relay data/b704_readme.txt).', '',
             '**The glossary:** h2_sign’ and h2_sign_sum appended (relay data/b704_glossary.txt).', '',
             '**The re-cut:** day1/ONE_PAGE_PROOF.md, %s to %s rows outside LICENSED/CITED, %s quoting lines as residues (relay data/b704_cut.txt; '
             'PLACE-papers 02b7aad).' % (f['before'], f['after'], f['quoting']), '',
             '**The kernels:** none written on a main; one dispatch, the probe on the scratch branch probe-b704, deleted after its bank; widening-b701 '
             'and epstein-b703 deleted on the word; no lean or lake on this host.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b704_closing.txt).', '',
             '**The open orders:** `W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-PAPER-PARTNER-COPIES`; `W-ORD-STANDING-CLAUSES-BANK`; '
             '`W-ORD-LV-CLOSURE-JOIN`; `W-ORD-KEYSTONE-HEADS`; `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA`; `W-ORD-E0-MET-CLASSK`; '
             '`W-ORD-WORKFLOW-PROBE-STEP`; `W-ORD-CORRESPONDENCE-EF-REACH`; `W-ORD-README-FIGURE-SCOPE`.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b703`s 0, 11, 131, 0; G-README-CURRENCY and G-READ-RULE-STANDING declared '
             'on the face as carried failures, on README :135 and on (i) and (o) (relay data/b704_standing_figures.txt, data/b704_read_calls.txt); '
             'G-WORKFLOW-FILES declared beside them on the probe`s print step, 46 of 109 names (defect (p)).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b704_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R314).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b704_citation_check.txt), step zero (data/b704_ferry.txt, data/b704_readfirst.txt, data/b704_stepzero.txt, '
         'data/b704_tests_stepzero.txt, data/b704_rowgen_stepzero.txt, data/b704_branches.txt, data/b704_read_sort.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b703`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s ; the read bank repaired and G-READ-RULE-STANDING '
         '(data/b704_read_calls.txt, data/b704_read_arm_control.txt)' % (c1_[0], f['corr_line']),
         '### COMPONENT 2 : the probe (data/b704_runner_SIDE-explicit-formula_probe.txt), the node list (data/b704_nodes_zeta.txt), the faces diff '
         '(data/b704_faces_diff.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the cells (data/b704_correspondence_run.txt, data/b704_cells_reach.txt) ; the README (data/b704_readme.txt) ; the glossary '
         '(data/b704_glossary.txt) ; the orders OPEN_TRAILS :%s-:%s ; N3 %s' % (f['orders'][0], f['orders'][4], S['N3'][0]),
         '### COMPONENT 4 : the tie (data/b704_tie.txt), the search (data/b704_quote.txt), the cut (data/b704_cut.txt), %s to %s ; N4 %s' % (
             f['before'], f['after'], S['N4'][0]),
         '### COMPONENT 5 : the carry-time reading (data/b704_tool_repairs.txt), the dry-run steps (data/b704_reg_gate.txt), the seal '
         '(data/b704_seal_hashes.json), the suite in six parts, the per-part seconds (data/b704_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def findings(*a):
    t, e = _finding_text()
    e = R.conv(e)
    dry = 'dry' in a
    cells_, fired = R.screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = R.conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = R.screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


_trail_defects, _trail_resolved = P3._trail_defects, P3._trail_resolved


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; the trail's Defects line AND its Resolved line read against
    the defects bank. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = R.conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = R.screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = R._face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        if which == 'TRAIL':
            m = re.search(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % ACT, text, re.M)
            got = m.group(1) if m else None
            want = '; '.join(_defect_short(ACT)) or 'none'
            eq = got == want
            print('  THE TRAIL`S DEFECTS LINE: %s' % got)
            print('  THE DEFECTS BANK`S ROWS (relay data/%s_defects.txt, by the repaired reader): %s' % (ACT, want))
            print('  ### THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK %s' % eq)
            rows, nav = _owners_now()
            gr = _trail_resolved(t)
            wr = (num_word(len(nav)), num_word(len(rows) - len(nav)))
            eqr = gr == wr
            print('  THE TRAIL`S RESOLVED LINE`S COUNTS: %s ; THE BANK`S OWNERS (navigator, seat): %s' % (gr, wr))
            print('  ### THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK %s' % eqr)
            clean = clean and eq and eqr
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def mbank(*a):
    """b703's mbank (its span line read from the mirror bank chain) carried by copy with b704's names."""
    import hashlib as _hl
    import zipfile
    import b616_record as R6
    ZIP = R.ZIP
    z = zipfile.ZipFile(ZIP)
    names_ = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names_), R6.nd_sets())[0]
    files_ = [n for n in names_ if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT)))
    for l in L[:9]:
        print(l[:240])


def guard(*a):
    """data/b704_guard_dry.txt (.json): b703's route with b704's names -- the suite's `--guard-dry` run in its own process (it writes nothing), its
    print banked verbatim; the writes by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b704_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b704_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b704_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b704_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b704_checks.py :%d `%s`,'
         % (k, src[k - 1].strip() if k else '?'), '### the line above the per-part seconds write at :%d.' % ((k or 0) + 1), '',
         '### THE PRINT, VERBATIM (exit %d):' % r.returncode]
    L += [x for x in r.stdout.rstrip(NL).split(NL)]
    L += ['', '### THE WRITES BY MODE, READ FROM THE SUITE`S writer_plan: %s' % '; '.join('%s %s' % (m, w or 'NONE') for m, w in writes.items()), '',
          '### ### **%s**' % ('THE GUARD HELD ; THE POST-ROOT PATH WRITES NONE OF THE PER-PART SECONDS BANKS ; THE PRE-RUN WRITES THEM ALONE'
                               if ok else '### THE GUARD IS NOT AS READ -- SEE ABOVE')]
    if 'dry' not in a:
        put_txt('%s_guard_dry.txt' % ACT, L)
        put_json('%s_guard_dry.json' % ACT, dict(at=utc(), writes=writes, guard_line=k, exit=r.returncode, ok=ok))
    print(NL.join(L))


def verdicts(*a):
    """prints each named bank's verdict line (its last `### ### **...**` line), for the suite's predicates to quote; writes nothing."""
    for n_ in a:
        m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', rdn(n_))
        print('  %s | %s' % (n_, ' '.join(m[-1].split()) if m else '### NO VERDICT LINE'))


ROUTES = dict(capture_routes=None, verdicts=verdicts, order_readme=order_readme, commands=commands,kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank, repairs=repairs, figures=figures, scores=scores, components=components,
              findings=findings, trail=trail, drycheck=drycheck, guard=guard, rootbanks=rootbanks, root=root, root_arm=root_arm,
              table_final=table_final)
ROUTES.pop('capture_routes')
ROUTES.update(names=names, defshort=defshort, probeview=probeview, probediff=probediff, efcells=efcells, tie=tie, runwait=runwait, cands=cands, facesraw=facesraw, facesdiff=facesdiff, cellsreach=cellsreach, readmediff=readmediff, glosscheck=glosscheck, orders=orders, quote=quote, cutbank=cutbank, quotecheck=quotecheck, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch, runstatus=runstatus,
              readsort=readsort, c1=c1, reads=reads, nodesdiff=nodesdiff, probe=probe)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b704_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
