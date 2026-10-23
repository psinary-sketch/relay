# -*- coding: utf-8 -*-
"""b707_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b707's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (aa198636, a NEW session: b706 ran in 44411d52; the anchor (R317)'s line is unique in it); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b707 and its commit reach widened to the kernels, with b706's repair carried
### (a bare eight-hex token that a bank's row or a kernel's lakefile names as a sha256 or a rev is not read as a commit); the `word` route is
### b694's. Routes: `check [dry]` -> data/b707_citation_check.txt (.json) ; `ferry` -> data/b707_ferry_scan.txt ; `answer <needle>` /
### `word <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b707 from b706_citation.py's form; this tool writes only the banks named above.
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b677_citation as C   # noqa: E402  ### the helpers, imported unchanged
import b707_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEAD_QUOTE = 'b706 closed: relay 30313a13, PLACE-papers c9e0086; suite 129 of 140; root aa8a696b1c7e9fef\u2026; 4 prompts answered; 13 defects'
RULING_ROOT_BANKS = 100          # ### (R317)(1): "the root aa8a696b over 100 banks" -- read against data/b706_act_root.json's data/ items
RULING_NAV = ['i', 'l', 'm']     # ### (R317)(1): "(i), (l) and (m) the navigator's" -- read against the bank's owners
SEVEN_POST_SEAL = ['G-NOTHING-RAN-AHEAD', 'G-TABLE-FINAL', 'G-ACTROOT-BANKED', 'G-RULE-SUITE-PARTS', 'G-TRAIL-LINES-EQUAL-DEFECTS',
                   'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL']
FOUR_DECLARED = ['G-WORKFLOW-FILES', 'G-RUNNER-READ', 'G-RUNNER-GATE', 'G-RULE-ONE-GIT-WRITE']


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def _ws(s):
    return ''.join((s or '').split())


def _remote_heads(repo):
    out = g(repo, 'ls-remote', '--heads', 'origin')[1] or ''
    return dict((l.split('\t', 1)[1].strip(), l.split('\t', 1)[0]) for l in out.split(NL) if '\t' in l)


def _defect_row(L, letter):
    """the text of a lettered defect row, from its letter to the next letter's row."""
    s = first(L, '    (%s) ' % letter)
    if not s:
        return 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, ' '.join(x.strip() for x in L[s - 1:e])


def _jl(name):
    try:
        return json.loads(rd(os.path.join(D, name)) or '{}')
    except Exception:
        return {}


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    EF, LV, FJ = K.EF_DIR, K.LV_DIR, K.JOIN_DIR
    # ### the ferry's read-first list, by existence
    for f in ('data/b706_closing.txt', 'data/b706_defects.txt', 'data/b706_report.txt', 'data/b706_join_grade.txt',
              'data/b706_buildlog_SIDE-faces-join_join.txt', 'data/b706_tool_repairs.txt', 'data/b706_closing_push_out.txt', 'tools/mirror_roster.json',
              'tools/terminal_table.py', 'tools/rule_arms.py', 'data/b705_registrations.txt', 'data/b705_i6_ranking.txt', 'data/b705_contour.txt',
              'tools/b696_witness_balls.py', 'tools/b326_windows.py', 'tools/b705_window.py', 'tools/b694_witness_terms.py', 'data/b703_q0_band.txt',
              'data/b703_pins.txt', 'data/b705_source_cc_2006_13771.txt', 'data/b680_rules.txt', 'data/b684_rules.txt', 'data/b706_rules.txt',
              'data/b675_rules.txt', 'data/b686_rules.txt', 'data/b690_rules.txt', 'data/b675_corrigenda.txt', 'data/b705_detection.txt',
              'data/b705_detection_controls.txt', 'data/b705_window.txt', 'data/b696_witness_balls.txt', 'data/b706_standing_figures.json',
              'data/b706_partners.json', 'data/b706_cells_reread.txt', 'data/b706_mirror.txt', 'data/b706_mirror_verify.txt', 'data/b706_table_final.txt',
              'tools/b706_report.py', 'tools/b706_record.py', 'tools/b706_checks.py', 'tools/b706_citation.py', 'tools/b706_closing.py', 'tools/b706_reg_gate.py',
              'tools/b706_regspec.py', 'tools/b706_corrigendum.py', 'tools/b706_standing_figures.py', 'tools/b706_worklist.py', 'tools/b706_tests.py',
              'tools/circuit_read.py', 'tools/mirror_verify.py', 'tools/push_gated.sh', 'tools/act_root.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R317)(1), by row
    cl = lines_of(p('data', 'b706_closing.txt'))
    add('ruling (1)', 'data/b706_closing.txt :1, the head line, against (R317)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b706_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b706_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b706_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = rd(p('data', 'b706_closing_push_out.txt')) or ''
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (7)', 'the closing commit relay 37e4a12f pushed in main mode and read back (data/b706_closing_push_out.txt, to be committed)',
        'main read back at the remote: 37e4a12f' in po and 'branch push-b706-closing' in po and head == K.PRE_RELAY,
        'data/b706_closing_push_out.txt :2 (branch push-b706-closing), :5 (read back) ; relay HEAD %s' % head, '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b706_closing_push_out.txt')[1].strip()
    add('ruling (7); ferry C0', 'data/b706_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    pr = lines_of(p('data', 'b706_partners.txt'))
    pv = at(pr, first(pr, '### ### **PAIRS 17'))
    add('ruling (1)', 'the 17 partner pairs renamed in place, 0 held (data/b706_partners.txt)', 'RENAME 17 ; HELD 0' in pv, 'data/b706_partners.txt :%d' % first(pr, '### ### **PAIRS 17'), '1')
    n17 = g(PP, 'rev-list', '--count', '1dfd9bc^..cedf7e9')[1].strip()
    add('ruling (1)', 'PLACE-papers 1dfd9bc..cedf7e9, one commit per pair (seventeen)', n17 == '17' and commit_in(PP, '1dfd9bc') and commit_in(PP, 'cedf7e9'),
        'git rev-list --count 1dfd9bc^..cedf7e9 = %s' % n17, '1')
    prr = lines_of(p('data', 'b706_partners_read.txt'))
    add('ruling (1)', 'the 8 hand edits resolved by their kind (data/b706_partners_read.txt HAND EDITS 8; data/b706_partners.txt THE HAND EDITS RESOLVED BY KIND 6, counted apart 107)',
        first(prr, 'HAND EDITS 8') > 0 and 'THE HAND EDITS RESOLVED BY KIND 6' in pv and 'THE VERSIONED SIDE CARRIES IT (COUNTED APART) 107' in pv,
        'data/b706_partners_read.txt :%d ; data/b706_partners.txt :%d -- the closing`s wording "8 hand edits resolved by their kind" (data/b706_closing.txt :34, :95)' % (
            first(prr, 'HAND EDITS 8'), first(pr, '### ### **PAIRS 17')), '1')
    pd = lines_of(p('data', 'b706_partners_dry.txt'))
    add('ruling (1)', 'the generator run once, 26 + 13 cells (data/b706_partners_dry.txt: 2 versioned copies, 39 cells)', first(pd, 'THE GENERATOR WROTE 2 VERSIONED COPIES (39 CELLS CHANGED)') > 0,
        'data/b706_partners_dry.txt :%d' % first(pd, 'THE GENERATOR WROTE 2 VERSIONED COPIES (39 CELLS CHANGED)'), '1')
    add('ruling (1)', 'the second pass 0 (data/b706_partners.txt)', 'THE SECOND PASS CHANGES 0' in pv, 'data/b706_partners.txt :%d' % first(pr, '### ### **PAIRS 17'), '1')
    ra = lines_of(p('data', 'b706_readers_after.txt'))
    add('ruling (1)', 'reader hits 102 before and after (data/b706_readers_after.txt)', first(ra, 'HITS 102 ; TABLES FOUND') > 0 and first(ra, 'STANDING READER HITS 102') > 0,
        'data/b706_readers_after.txt :%d, :%d' % (first(ra, 'HITS 102 ; TABLES FOUND'), first(ra, 'STANDING READER HITS 102')), '1')
    jl_ = lines_of(p('data', 'b706_join_lakefile.txt'))
    jtip = g(FJ, 'rev-parse', 'main')[1].strip()
    add('ruling (1)', 'SIDE-faces-join`s lakefile re-ordered mathlib last at b37a7b6 (data/b706_join_lakefile.txt; the kernel`s main there)',
        first(jl_, 'MATHLIB LAST True') > 0 and jtip == K.JOIN_TIP, 'data/b706_join_lakefile.txt :%d ; SIDE-faces-join main %s' % (first(jl_, 'MATHLIB LAST True'), jtip[:8]), '1')
    dj = _jl('b706_dispatches.json').get('rows') or []
    joins = [d for d in dj if d.get('label') == 'join']
    add('ruling (1)', 'one dispatch of the join (data/b706_dispatches.json), run 39850337262', len(joins) == 1 and joins[0].get('run_id') == K.JOIN_RUN,
        'dispatch rows %d, join rows %d, run %s' % (len(dj), len(joins), joins[0].get('run_id') if joins else '-'), '1')
    cg = lines_of(p('data', 'b706_art_SIDE-faces-join_join_cache_log.txt'))
    bl = lines_of(p('data', 'b706_buildlog_SIDE-faces-join_join.txt'))
    add('ruling (1)', 'the cache served and Mathlib built from it (the artifact`s cache log: 8691 files decompressed; the build log then builds the kernels` own modules)',
        first(cg, 'Decompressed 8691 file(s)') > 0 and first(bl, 'Built Zeta23.') > 0,
        'data/b706_art_SIDE-faces-join_join_cache_log.txt :%d ; data/b706_buildlog_SIDE-faces-join_join.txt :%d (the first kernel module built past the cache)' % (first(cg, 'Decompressed 8691 file(s)'), first(bl, 'Built Zeta23.')), '1')
    add('ruling (1); ferry read-first', 'the join held at SIDE-lv-conservation`s GammaBounds.lean :177 at the shared pin -- the join run`s artifact bank by line',
        first(bl, 'error: SIDELvConservation/GammaBounds.lean:177:8') == K.JOIN_BUILDLOG_LINE and first(lines_of(p('data', 'b706_join_grade.txt')), 'THE JOIN HELD') > 0,
        'data/b706_buildlog_SIDE-faces-join_join.txt :%d ; data/b706_join_grade.txt :%d' % (first(bl, 'error: SIDELvConservation/GammaBounds.lean:177:8'), first(lines_of(p('data', 'b706_join_grade.txt')), 'THE JOIN HELD')), '1-3')
    jtags = (g(FJ, 'tag', '--list')[1] or '').split()
    add('ruling (1)', 'no tag at SIDE-faces-join', not jtags, 'tags %s' % (jtags or 'NONE'), '1')
    efm = g(EF, 'rev-parse', 'main')[1].strip()
    add('ruling (1)', 'the workflow`s probe step on SIDE-explicit-formula main at badaccc', efm == K.EF_MAIN, 'SIDE-explicit-formula main %s' % efm[:8], '1')
    gr = lines_of(p('data', 'b706_generator_reach.txt'))
    gv = at(gr, first(gr, '### ### **PARSED KERNELS'))
    add('ruling (1)', 'the generator parsing the citation form: 17 kernels, 13 cells, every re-emission byte-equal (data/b706_generator_reach.txt)',
        'PARSED KERNELS 17' in gv and 'ITS CITATION-FORM CELLS 13' in gv and 'EVERY RE-EMISSION EQUAL BYTE FOR BYTE True' in gv, 'data/b706_generator_reach.txt :%d' % first(gr, '### ### **PARSED KERNELS'), '1')
    rv1 = rd(p('data', 'b706_runner_SIDE-explicit-formula_prints_v0_1.txt')) or ''
    rv2 = rd(p('data', 'b706_runner_SIDE-explicit-formula_prints_v0_2.txt')) or ''
    cr = lines_of(p('data', 'b706_cells_reread.txt'))
    add('ruling (1)', 'the entry-tag prints at v0.1 and v0.2 both DERIVES; 9 of 11 mentions equal, 2 unbanked (data/b706_cells_reread.txt)',
        'GATE DERIVES' in rv1 and 'GATE DERIVES' in rv2 and first(cr, 'MENTIONS RE-READ 11 ; EQUAL 9 ; DIFFERS 0 ; UNBANKED 2') > 0,
        'data/b706_runner_SIDE-explicit-formula_prints_v0_1.txt, _v0_2.txt (GATE DERIVES) ; data/b706_cells_reread.txt :%d' % first(cr, 'MENTIONS RE-READ 11'), '1')
    add('ruling (1)', 'the entry at FINDINGS :10046, b705`s weight :10028, b706`s corrigendum :10030',
        at(fi, K.B706_ENTRY).startswith('## 17 of 17 partner pairs renamed in place') and at(fi, K.B706_WEIGHT).startswith('*Appended 2026-10-22 by b706 to b705’s entry') and at(fi, K.B706_CORRIGENDUM).startswith('## Corrigendum to b705’s record'),
        'FINDINGS :%d %r ; :%d ; :%d' % (K.B706_ENTRY, at(fi, K.B706_ENTRY)[:60], K.B706_WEIGHT, K.B706_CORRIGENDUM), '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15644', at(ot, K.B706_TRAIL) == K.B706_TRAIL_HEAD, 'OPEN_TRAILS :%d %r' % (K.B706_TRAIL, at(ot, K.B706_TRAIL)[:70]), '1')
    six = [n for n in K.ORDERS_B706 if at(ot, n).startswith('*Appended 2026-10-22 by b706 beneath `W-ORD-')]
    add('ruling (1)', 'six order lines at OPEN_TRAILS :15632-:15642', len(six) == 6, 'OPEN_TRAILS %s' % ', '.join(':%d' % n for n in six), '1')
    sc = _jl('b706_scores_close.json')
    sr = _jl('b706_scores.json')
    held = all((sc.get(k) or [''])[0] == 'HELD' for k in ('N1', 'N2', 'N4', 'S2', 'S3'))
    add('ruling (1)', 'N1, N2, N4, S2, S3 HELD; N3 REFUTED; N5 REFUTED; S1 REFUTED (data/b706_scores_close.json)',
        held and all((sc.get(k) or [''])[0] == 'REFUTED' for k in ('N3', 'N5', 'S1')),
        'data/b706_scores_close.json: %s' % ', '.join('%s %s' % (k, (sc.get(k) or ['-'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), '1')
    n3 = (sr.get('N3') or ['', ''])[1]
    add('ruling (1)', 'N3 REFUTED on its lakefile clause, struck by the author`s word (the scores bank`s own text)',
        'first clause reads REFUTED by the author`s word' in n3 and 'Mathlib BEFORE both requires False' in n3, 'data/b706_scores.json N3', '1')
    n5 = (sr.get('N5') or ['', ''])[1]
    add('ruling (1)', 'N5 REFUTED on (g): one git write per message False (the scores bank`s text; data/b706_defects.txt (g))',
        'one git write per message' in n5 and 'False' in n5 and _defect_row(lines_of(p('data', 'b706_defects.txt')), 'g')[0] > 0,
        'data/b706_scores.json N5 ; data/b706_defects.txt (g) :%d' % _defect_row(lines_of(p('data', 'b706_defects.txt')), 'g')[0], '1')
    s1 = (sc.get('S1') or ['', ''])[1]
    tf = lines_of(p('data', 'b706_table_final.txt'))
    add('ruling (1)', 'S1 REFUTED on the table`s 15 moved grades (data/b706_scores_close.json S1; data/b706_table_final.txt)',
        'grade moved 15' in s1 and first(tf, 'ROWS MOVED 18 ; ADDED 12 ; GONE 0 ; GRADE MOVED 15') > 0, 'data/b706_table_final.txt :%d' % first(tf, 'GRADE MOVED 15'), '1')
    ar = _jl('b706_act_root.json')
    nb = len([it for it in ar.get('items') or [] if it.startswith('data/')])
    add('ruling (1)', 'the root aa8a696b chained from 8454a2bb (data/b706_act_root.json; data/act_roots.txt`s b706 row)',
        (ar.get('root') or '').startswith('aa8a696b') and (ar.get('previous') or '').startswith('8454a2bb') and bool(act_root_line('b706')),
        'data/b706_act_root.json (root %s, prev %s) ; data/act_roots.txt row b706 %s' % ((ar.get('root') or '')[:8], (ar.get('previous') or '')[:8], bool(act_root_line('b706'))), '1')
    add('ruling (1)', '"the root aa8a696b over 100 banks": the root`s data/ items against the ruling`s figure', nb == RULING_ROOT_BANKS,
        'data/b706_act_root.json names %d data/ banks (data/b706_root_banks.txt: BANKS 114); the figure 100 is the root route`s DRY run before the seal '
        '(data/b706_root_banks_dry.txt: BANKS 100), not the root`s' % nb, '1')
    ck, cp = rd(p('data', 'b706_checks.txt')) or '', rd(p('data', 'b706_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 129 of 140 (pre-push and post-push)', 'ARMS RUN : 140. ### LIVE PASSING : 129.' in ck and 'ARMS RUN : 140. ### LIVE PASSING : 129.' in cp,
        'data/b706_checks.txt ; data/b706_checks_postpush.txt', '1')
    m11 = re.search(r"LIVE FAILING : 11 \[(.*?)\]", cp)
    fails = [x.strip().strip("'") for x in (m11.group(1) if m11 else '').split(',') if x.strip()]
    add('ruling (2)', 'the four declared and the seven after the seal, as the post-push bank lists them (G-RULE-SUITE-PARTS among the seven)', sorted(fails) == sorted(FOUR_DECLARED + SEVEN_POST_SEAL),
        'data/b706_checks_postpush.txt LIVE FAILING %d: %s' % (len(fails), fails), '1')
    df = lines_of(p('data', 'b706_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    nav = [x for x, o in lt if o == 'NAVIGATOR']
    add('ruling (1); ferry read-first', 'data/b706_defects.txt (rows are defects as lettered): thirteen, (a)-(m)', [x for x, _o in lt] == list('abcdefghijklm'),
        'letters %s' % ''.join(x for x, _o in lt), '1')
    add('ruling (1)', '"(i), (l) and (m) the navigator`s": the bank`s owners', nav == RULING_NAV,
        'the navigator`s by the bank: %s ((l) THE SEAT`S: the split parts named with letters; (a), (b), (c) the navigator`s too)' % nav, '1')
    mv = lines_of(p('data', 'b706_mirror_verify.txt'))
    add('ruling (1)', 'the mirror NOT CLEAN on clause 3 alone (data/b706_mirror_verify.txt)', first(mv, 'CLAUSE 1 : CLEAN') > 0 and first(mv, 'CLAUSE 2 : CLEAN') > 0 and first(mv, 'CLAUSE 3 : NOT CLEAN') > 0,
        'data/b706_mirror_verify.txt :%d, :%d, :%d' % (first(mv, 'CLAUSE 1 : CLEAN'), first(mv, 'CLAUSE 2 : CLEAN'), first(mv, 'CLAUSE 3 : NOT CLEAN')), '1')
    ros = json.loads(rd(p('tools', 'mirror_roster.json')) or '{}').get('files') or []
    pj = _jl('b706_partners.json').get('rows') or []
    versioned = sorted(r['versioned'] for r in pj if r.get('versioned'))
    unversioned = sorted(r['unversioned'] for r in pj if r.get('unversioned'))
    ros_n = [x.replace('\\', '/') for x in ros]
    retired_in = [v for v in versioned if v in ros_n]
    add('ruling (1); ruling (2); ferry read-first', 'tools/mirror_roster.json naming the 17 retired paths (the versioned names), by line', len(retired_in) == 17 and len(ros) == 83,
        'tools/mirror_roster.json: %d entries, the 17 retired versioned paths at lines %s' % (len(ros), [7 + ros_n.index(v) for v in retired_in]), '1')
    mi = ' '.join(lines_of(p('data', 'b706_mirror.txt')))
    add('ruling (1)', 'the export carrying the root line (data/b706_mirror.txt)', 'Act root: b706 aa8a696b' in mi and os.path.exists(K.MIRROR_ZIP), 'data/b706_mirror.txt :6 ; the zip exists %s' % os.path.exists(K.MIRROR_ZIP), '1')
    add('ruling (1)', '"nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b707_worklist.py DRAFT', '6')
    # ### (R317)(2)
    add('ruling (2)', 'the mirror`s dry run against b706`s export: tools/mirror_verify.py clause3 reads the roster from disk; b706`s zip exists',
        'def clause3(names, roster_path=None)' in (rd(p('tools', 'mirror_verify.py')) or '') and os.path.exists(K.MIRROR_ZIP), 'tools/mirror_verify.py :90 ; %s' % K.MIRROR_ZIP, '1')
    tt = lines_of(p('tools', 'terminal_table.py'))
    add('ruling (2); ferry read-first', 'the terminal table`s scope by path and line: ledger_files walks PLACE-papers/archive/ (tools/terminal_table.py)',
        first(tt, 'def ledger_files():') == 477 and first(tt, "arch = os.path.join(PP, 'archive')") == 488 and first(tt, 'for dirpath, _, files in os.walk(arch):') == 489,
        'tools/terminal_table.py ledger_files :%d ; the archive walk :%d-:%d' % (first(tt, 'def ledger_files():'), first(tt, "arch = os.path.join(PP, 'archive')"), first(tt, 'for dirpath, _, files in os.walk(arch):')), '1')
    add('ruling (2)', 'b706`s final table: 12 added rows and 15 moved grades, every one citing a retired copy (data/b706_table_final.txt; data/b706_report.txt (3))',
        first(tf, 'added 12') > 0 and '15 of the 15 after-cells cite the retired copies' in (rd(p('data', 'b706_report.txt')) or '') and '12 of the 12 added rows cite them too' in (rd(p('data', 'b706_report.txt')) or ''),
        'data/b706_table_final.txt :3 ; data/b706_report.txt :8', '1')
    ra_ = lines_of(p('tools', 'rule_arms.py'))
    fam = first(ra_, "fam.setdefault(re.sub(r'(?<=^standing-[a-z])[0-9]$', '', p), []).append(p)")
    gov = first(ra_, r"re.search(r'\bstanding-[a-z][0-9]?\b', r)")
    add('ruling (2); ferry read-first', 'the suite`s part-family reading by path and line (tools/rule_arms.py G-RULE-SUITE-PARTS: the family regex and the governing-row pattern)',
        fam == 551 and gov == 301 and first(ra_, "if name == 'G-RULE-SUITE-PARTS':") == 539,
        'tools/rule_arms.py :%d (the arm), :%d (the family regex, one trailing digit), :%d (the governing pattern standing-<letter><digit>?)' % (first(ra_, "if name == 'G-RULE-SUITE-PARTS':"), fam, gov), '1')
    add('ruling (2)', 'G-RULE-SUITE-PARTS failing on b706`s run banks (data/b706_checks_postpush.txt), (l)', 'G-RULE-SUITE-PARTS' in fails and 'lettered halves' not in '' and _defect_row(df, 'l')[0] > 0,
        'data/b706_checks_postpush.txt ; data/b706_defects.txt (l) :%d' % _defect_row(df, 'l')[0], '1')
    b5 = rd(p('data', 'b705_checks_postpush.txt')) or ''
    add('ruling (2)', 'b705`s unsplit banks (standing-b2 as one part) for the repaired arm`s reading', 'PART standing-b2 :' in b5 and 'standing-b2a' not in b5, 'data/b705_checks_postpush.txt', '1')
    cgb = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cgb), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (26), b706`s)', lastrow == 26, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cgb, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b706`s corrigendum tool to carry (b678`s form)', os.path.exists(p('tools', 'b706_corrigendum.py')) and os.path.exists(p('tools', 'b678_corrigendum.py')), 'tools/b706_corrigendum.py ; tools/b678_corrigendum.py', '1')
    for letter in ('i', 'j', 'k', 'l', 'm'):
        s_, t_ = _defect_row(df, letter)
        add('ruling (2)', 'b706`s item (%s) found after the seal, for the corrigendum' % letter, s_ > 0 and ('after the seal' in t_ or 'NEXT MIRROR SORT' in t_ or 'LEDGER REACH' in t_), 'data/b706_defects.txt (%s) :%d' % (letter, s_), '1')
    two = [l for l in cr if 'unbanked (no tag named beside the kernel)' in l]
    s442 = at(lines_of(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md')), 442)
    f20 = at(lines_of(os.path.join(PP, 'FACES_LEDGER.md')), 20)
    add('ruling (2)', 'the two unbanked mentions of the 11, by paper and line (data/b706_cells_reread.txt): SIMPLICITY_OF_RIEMANN_ZEROS :442 and FACES_LEDGER :20',
        len(two) == 2 and 'SIMPLICITY_OF_RIEMANN_ZEROS.md :442' in two[0] and 'FACES_LEDGER.md :20' in two[1], 'data/b706_cells_reread.txt :%d, :%d' % (first(cr, 'SIMPLICITY_OF_RIEMANN_ZEROS.md :442'), first(cr, 'FACES_LEDGER.md :20')), '1')
    m442 = re.search(r'SIDE-explicit-formula (v\d+(?:\.\d+)*) = `([0-9a-f]{7,40})`', s442)
    m20 = re.search(r'SIDE-explicit-formula (v\d+(?:\.\d+)*) = `([0-9a-f]{7,40})`', f20)
    add('ruling (2)', '"with the tag each cites": the two lines read for a tag beside the kernel',
        bool(m442) and bool(m20),
        'SIMPLICITY_OF_RIEMANN_ZEROS :442 %s ; FACES_LEDGER :20 %s (b704`s reader: no tag named beside the kernel; the line names SIDE-explicit-formula %s)' % (
            ('names %s = %s' % (m442.group(1), m442.group(2))) if m442 else 'names NO tag beside the kernel',
            ('names %s = %s' % (m20.group(1), m20.group(2))) if m20 else 'names NO tag beside the kernel', 'SIDE-explicit-formula' in f20), '1')
    add('ruling (2); ferry read-first', 'W-ORD-ENTRY-TAG-PRINTS at :15590 and its discharge at :15642 (the remainder entered beneath)',
        'W-ORD-ENTRY-TAG-PRINTS' in at(ot, K.ORDER_TAG_PRINTS) and 'ENTERED' in at(ot, K.ORDER_TAG_PRINTS) and 'W-ORD-ENTRY-TAG-PRINTS' in at(ot, K.ORDER_TAG_PRINTS_DISCHARGED) and 'DISCHARGED' in at(ot, K.ORDER_TAG_PRINTS_DISCHARGED),
        'OPEN_TRAILS :%d, :%d' % (K.ORDER_TAG_PRINTS, K.ORDER_TAG_PRINTS_DISCHARGED), '1')
    add('ruling (2)', 'data/b707_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b707_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R317)(3)
    rg = lines_of(p('data', 'b705_registrations.txt'))
    i3 = first(rg, '  (iii) THE SIGN-ONSET RADIUS AT Q0')
    add('ruling (3); ferry read-first', 'data/b705_registrations.txt (iii) by line: the parameter, the empty prime side, the source, the quantity, the hypothesis, the falsifier, the controls',
        i3 == 15 and first(rg, 'THE PARAMETER: a > 0') == 17 and first(rg, 'THE EMPTY PRIME SIDE') == 22 and first(rg, 'THE QUANTITY: for each support radius a on a ladder') == 39
        and first(rg, 'HYPOTHESIS: a* exists on the ladder') == 44 and first(rg, 'FALSIFIER: a positive form at every a computed') == 47 and first(rg, 'CONTROLS: (C1) the zeta form') == 48,
        'data/b705_registrations.txt (iii) :%d ; the parameter :%d ; the empty prime side :%d ; the source :%d ; the quantity :%d ; the hypothesis :%d ; the falsifier :%d ; the controls :%d' % (
            i3, first(rg, 'THE PARAMETER: a > 0'), first(rg, 'THE EMPTY PRIME SIDE'), first(rg, 'THE SMALL-SUPPORT POSITIVITY RESULT'), first(rg, 'THE QUANTITY: for each support radius a on a ladder'),
            first(rg, 'HYPOTHESIS: a* exists on the ladder'), first(rg, 'FALSIFIER: a positive form at every a computed'), first(rg, 'CONTROLS: (C1) the zeta form')), '2')
    rlog = g(ROOT, 'log', '--format=%h', '--', 'data/b705_registrations.txt')[1].split()
    add('ruling (3); N2', 'the registration unchanged from its b705 commit (d139cfcf), the one commit touching it', rlog == [K.REGISTRATION_B705_COMMIT], 'commits touching data/b705_registrations.txt %s' % rlog, '2')
    add('ruling (3)', '"the grid the registration names": the ladder from a = log 2 upward through 2 log w, w = 32 ... 192 (:39-:40)',
        'from a = log 2 upward through the' in at(rg, 39) and "ladder's radii 2 log w, w = 32 ... 192" in at(rg, 40), 'data/b705_registrations.txt :39-:40', '2')
    add('ruling (3)', '"the form at Q0 reproducing (R315)(7)(ii)`s sign at a = 32": (C2) :49-:52 -- data/b705_window.txt`s S at width 32 NONNEGATIVE, b696`s at rho_0 NEGATIVE',
        'CONTROLS: (C1) the zeta form' in at(rg, 48) and '(C2) the form at Q0 evaluated at (ii)' in at(rg, 49) and 'NONNEGATIVE BEYOND ITS BOUND' in at(lines_of(p('data', 'b705_window.txt')), 11)
        and 'NEGATIVE BEYOND ITS BOUND' in at(lines_of(p('data', 'b696_witness_balls.txt')), 14),
        'data/b705_registrations.txt :48-:52 ; data/b705_window.txt :11 (a 32, S 1476.18 NONNEGATIVE) ; data/b696_witness_balls.txt :14 (a 32 at rho_0, S -7.775 NEGATIVE)', '2')
    add('ruling (3)', 'the thresholds log 2, log 3, log 4, log 5, log 7 and the coefficient of Z_Q at each: the registration`s empty prime side (Lambda_Q(2) = Lambda_Q(3) = 0, the first term at n = 4)',
        'Lambda_Q(2) = Lambda_Q(3) = 0' in at(rg, 24) and 'its first term at n = 4' in at(rg, 25), 'data/b705_registrations.txt :22-:25', '2')
    wb = lines_of(p('tools', 'b696_witness_balls.py'))
    add('ruling (3); ferry read-first', 'tools/b696_witness_balls.py :124-:146, the zero tail b696 certified; terms :179; arch_tail :90',
        first(wb, 'def zero_tail(') == 124 and first(wb, 'def terms(') == 179 and first(wb, 'def arch_tail(') == 90, 'zero_tail :%d ; terms :%d ; arch_tail :%d' % (first(wb, 'def zero_tail('), first(wb, 'def terms('), first(wb, 'def arch_tail(')), '2')
    co = lines_of(p('data', 'b705_contour.txt'))
    add('ruling (3); ferry read-first', 'data/b705_contour.txt: the contour b705 read, each range enclosing every zero of Λ_Q', first(co, 'EACH ENCLOSE EVERY ZERO') > 0, 'data/b705_contour.txt :%d' % first(co, 'EACH ENCLOSE EVERY ZERO'), '2')
    bw = lines_of(p('tools', 'b326_windows.py'))
    add('ruling (3); ferry read-first', 'tools/b326_windows.py :220-:228, the Q0 bracket 2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt 23)', first(bw, 'def kernel_q_derived(U):') == 220, 'tools/b326_windows.py :%d' % first(bw, 'def kernel_q_derived(U):'), '2')
    wt = lines_of(p('tools', 'b694_witness_terms.py'))
    add('ruling (3); ferry read-first', 'the b705 window tool by path (tools/b705_window.py) and the window it imports (tools/b694_witness_terms.py Window :106, lambda_q :291, prime_sum :346)',
        os.path.exists(p('tools', 'b705_window.py')) and first(wt, 'class Window:') == 106 and first(wt, 'def lambda_q(') == 291 and first(wt, 'def prime_sum(') == 346,
        'tools/b705_window.py ; tools/b694_witness_terms.py Window :%d, lambda_q :%d, prime_sum :%d' % (first(wt, 'class Window:'), first(wt, 'def lambda_q('), first(wt, 'def prime_sum(')), '2')
    cc = lines_of(p('data', 'b705_source_cc_2006_13771.txt'))
    add('ruling (3); ferry read-first', 'the Connes-Consani source bank by path and page: page 2 (the support (1/2, 2), :94-:97; Weil`s inequality :104-:106), page 3 (Theorem 1 :120-:125)',
        first(cc, '== PAGE 2') > 0 and 'so that rational primes are not involved' in at(cc, 97) and 'For any smooth, positive' in at(cc, 104) and first(cc, '== PAGE 3') == 114 and 'Theorem 1' in at(cc, 120),
        'data/b705_source_cc_2006_13771.txt == PAGE 2 :%d, :97, :104-:106 ; == PAGE 3 :%d, :120-:125' % (first(cc, '== PAGE 2'), first(cc, '== PAGE 3')), '2')
    add('ruling (3)', 'tools/b707_onset.py, data/b707_onset.txt and its hashes bank -- TO BE WRITTEN', not os.path.exists(p('tools', 'b707_onset.py')) and not os.path.exists(p('data', 'b707_onset.txt')), 'absent, as ordered', '2')
    # ### (R317)(4)
    qb = lines_of(p('data', 'b703_q0_band.txt'))
    add('ruling (4); ferry read-first', 'data/b703_q0_band.txt: 17 off-line rows with their heights and real parts (rows are bins)', first(qb, 'rows 163 ; off the line 17') > 0 and first(qb, '(0.6, 0.75]    5 |') > 0 and first(qb, '(0.75, 7/8]   10 |') > 0 and first(qb, '(7/8, 1)       2 |') > 0,
        'data/b703_q0_band.txt :8, :13-:15', '0-4')
    de = lines_of(p('data', 'b705_detection.txt'))
    add('ruling (4)', 'the twelve pairs beyond b675`s modulus rule, idx 5-16, each with its predicted n* and the modulus bound (data/b705_detection.txt :15-:26)',
        first(de, 'beyond reach 12 [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]') > 0 and all('beyond reach: b675`s rule' in at(de, n) and 'predicted' in at(de, n) for n in range(15, 27)),
        'data/b705_detection.txt :15-:26, :28', '0-4')
    dc = lines_of(p('data', 'b705_detection_controls.txt'))
    add('ruling (4)', 'the controls: b675`s figure at rho_0 (n* 63676) and the five pairs b705 computed (idx 0-4, WITHIN)', first(dc, 'n* 63676 ; b675`s 63676 ; EQUAL True') == 6 and all('WITHIN' in at(de, n) for n in range(10, 15)),
        'data/b705_detection_controls.txt :6 ; data/b705_detection.txt :10-:14', '0-4')
    add('ruling (4)', 'the detection law`s hypothesis and falsifier as b703 registered them (data/b703_registrations.txt (ii) :21-:31)',
        'HYPOTHESIS (THE PREDICTION): n*(ρ) = L₀ / r(ρ) within the factor range [0.67, 1.5]' in at(lines_of(p('data', 'b703_registrations.txt')), 25) and 'FALSIFIER: any pair' in at(lines_of(p('data', 'b703_registrations.txt')), 26),
        'data/b703_registrations.txt :25-:26', '0-4')
    lb = lines_of(p('tools', 'b675_li_bench.py'))
    add('ruling (4)', 'b675`s route (the arithmetic the price reads): tools/b675_li_bench.py constants_for :163, onset :153, PREC, T0', first(lb, 'def constants_for(') == 163 and first(lb, 'def onset(') == 153 and first(lb, 'PREC = ') > 0,
        'tools/b675_li_bench.py constants_for :%d ; onset :%d ; PREC :%d ; T0 :%d' % (first(lb, 'def constants_for('), first(lb, 'def onset('), first(lb, 'PREC = '), first(lb, 'T0 = ')), '0-4')
    add('ruling (4)', 'data/b707_registrations.txt -- TO BE WRITTEN at step zero, committed alone before any computation', not os.path.exists(p('data', 'b707_registrations.txt')), 'absent, as ordered', '0')
    # ### (R317)(5)
    lt_ = (g(LV, 'show', '%s:lean-toolchain' % K.LV_V0100)[1] or '').strip()
    man = (g(LV, 'show', '%s:lake-manifest.json' % K.LV_V0100)[1] or '').split(NL)
    lkf = (g(LV, 'show', '%s:lakefile.lean' % K.LV_V0100)[1] or '').split(NL)
    tree = (g(LV, 'ls-tree', '-r', '--name-only', K.LV_V0100)[1] or '').split()
    add('ruling (5); ferry read-first', 'SIDE-lv-conservation`s lean-toolchain and lake-manifest.json at 93c27ec by line: Lean v4.29.1 (:1), Mathlib 5e932f97 (manifest :8 rev, :11 inputRev)',
        lt_ == K.LV_LEAN and first(man, '"rev": "%s"' % K.LV_MATHLIB) == 8 and first(man, '"inputRev": "%s"' % K.LV_MATHLIB) == 11,
        'lean-toolchain :1 %r ; lake-manifest.json rev :%d, inputRev :%d (the working tree`s two files equal, data/b703_pins.txt :12)' % (lt_, first(man, '"rev": "%s"' % K.LV_MATHLIB), first(man, '"inputRev": "%s"' % K.LV_MATHLIB)), '3')
    add('ruling (5)', 'lakefile.lean at 93c27ec pins Mathlib by rev too (:12, `@ "5e932f97..."`) -- a third file the pin move touches, beyond the two the ruling names',
        first(lkf, '@ "%s"' % K.LV_MATHLIB) == 0, 'lakefile.lean :%d carries `@ "%s"` -- RAISED: the ruling moves the toolchain and the manifest alone' % (first(lkf, '@ "%s"' % K.LV_MATHLIB), K.LV_MATHLIB[:8]), '3')
    add('ruling (5)', 'the port branch dispatched "with the tip as the ref": the tree at 93c27ec carries the workflow build-module.yml the runner reads from the ref', K.WORKFLOW in tree,
        'the tree at 93c27ec: %s -- NO .github/workflows (the workflow entered lv-conservation`s main at b694, d38f3e8) -- RAISED: a dispatch of the branch needs the workflow at its ref' % ' '.join(sorted(set(x.split('/')[0] for x in tree))), '3')
    lean_files = [x for x in tree if x.endswith('.lean')]
    mods = [x for x in tree if x.startswith('SIDELvConservation/') and x.endswith('.lean')]
    add('ruling (5)', '"files built of 15": the .lean files at 93c27ec (the 12 modules of SIDELvConservation, AxiomCheck.lean, PinnedGoal.lean, lakefile.lean)', len(lean_files) == K.LV_LEAN_FILES and len(mods) == K.LV_MODULES,
        '.lean files %d ; modules under SIDELvConservation/ %d' % (len(lean_files), len(mods)), '3')
    ef_lt = (rd(os.path.join(EF, 'lean-toolchain')) or '').strip()
    efm_ = lines_of(os.path.join(EF, 'lake-manifest.json'))
    add('ruling (5)', 'SIDE-explicit-formula`s pin: Lean v4.34.0-rc1 (lean-toolchain :1), Mathlib de5ce8a9 (lake-manifest.json :10, :13)', ef_lt == K.EF_LEAN and first(efm_, '"rev": "%s"' % K.EF_MATHLIB) == 10 and first(efm_, '"inputRev": "%s"' % K.EF_MATHLIB) == 13,
        'lean-toolchain %r ; lake-manifest.json :%d, :%d' % (ef_lt, first(efm_, '"rev": "%s"' % K.EF_MATHLIB), first(efm_, '"inputRev": "%s"' % K.EF_MATHLIB)), '3')
    dstat = g(LV, 'diff', '--numstat', K.LV_V0100, 'main', '--', 'SIDELvConservation/GammaBounds.lean')[1].strip()
    gb = lines_of(os.path.join(LV, 'SIDELvConservation', 'GammaBounds.lean'))
    add('ruling (5)', 'GammaBounds.lean :177 at 93c27ec: the error line of the join`s artifact (the `rw [show (-1 / 2 : ℝ) * t = -t / 2 by ring]` of the working tree`s :179; main differs from 93c27ec in docstring lines alone, 5 added 3 removed)',
        dstat.startswith('5\t3\t') and 'rw [show (-1 / 2 : ℝ) * t = -t / 2 by ring]' in at(gb, 179) and 'Did not find an occurrence of the pattern' in at(bl, K.JOIN_BUILDLOG_LINE) and '-1 / 2 * t' in at(bl, K.JOIN_BUILDLOG_LINE + 1),
        'git diff --numstat 93c27ec main: %r ; the working tree :179 %r ; the artifact`s target `(fun x => rexp (-1 / 2 * x)) t = rexp (-t / 2)` (data/b706_buildlog_SIDE-faces-join_join.txt :%d-:%d)' % (
            dstat, at(gb, 179).strip()[:60], K.JOIN_BUILDLOG_LINE, K.JOIN_BUILDLOG_LINE + 3), '3')
    rh = _remote_heads(LV)
    add('ruling (5)', 'the branch port-b707 absent before the act, locally and at the remote; lv-conservation`s main d38f3e8 and v0.10.0 93c27ec unmoved',
        not branch_listed(LV, K.PORT_BRANCH) and ('refs/heads/%s' % K.PORT_BRANCH) not in rh and g(LV, 'rev-parse', 'main')[1].strip() == K.LV_MAIN and g(LV, 'rev-parse', 'v0.10.0^{commit}')[1].strip() == K.LV_V0100,
        'local %s ; remote %s ; main %s ; v0.10.0 %s -- one ls-remote of SIDE-lv-conservation' % ('present' if branch_listed(LV, K.PORT_BRANCH) else 'absent', 'present' if ('refs/heads/%s' % K.PORT_BRANCH) in rh else 'absent',
                                                                                                    g(LV, 'rev-parse', 'main')[1].strip()[:7], g(LV, 'rev-parse', 'v0.10.0^{commit}')[1].strip()[:7]), '3')
    add('ruling (5)', 'the join`s module unchanged at SIDE-faces-join (its main at b37a7b6)', jtip == K.JOIN_TIP, 'SIDE-faces-join main %s' % jtip[:8], '3')
    nfp = sum(1 for l in ot if 'W-ORD-LV-FORWARD-PORT' in l)
    add('ruling (5)', 'W-ORD-LV-FORWARD-PORT not yet at OPEN_TRAILS (to be entered); W-ORD-LV-CLOSURE-JOIN :15452 with the hold :15634 naming the forward-port for the next ruling',
        nfp == 0 and 'W-ORD-LV-CLOSURE-JOIN' in at(ot, K.ORDER_LV_JOIN) and 'the forward-port of lv-conservation’s GammaBounds.lean at the shared pin' in at(ot, K.ORDER_LV_JOIN_HELD),
        'OPEN_TRAILS lines naming W-ORD-LV-FORWARD-PORT %d ; :%d ; :%d' % (nfp, K.ORDER_LV_JOIN, K.ORDER_LV_JOIN_HELD), '3')
    add('ruling (5)', 'data/b707_port.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b707_port.txt')), 'absent, as ordered', '3')
    # ### (R317)(6)
    i6 = lines_of(p('data', 'b705_i6_ranking.txt'))
    add('ruling (6); ferry read-first', 'data/b705_i6_ranking.txt with the support radius at its head and the next axis (e) representation coordinates second',
        first(i6, '1. (d`) the support radius a as the deformation parameter -- 5') == 57 and first(i6, '2. (e) representation coordinates') == 58,
        'data/b705_i6_ranking.txt :57 (the head), :58 (the next axis)', '4')
    # ### (R317)(7)-(10) and the ferry
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (7)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    add('ruling (7)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b707_worklist.py HOLD', '0')
    add('ruling (8)', 'the READFIRST-CLOSURE reader', 'def readfirst(' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py :%d' % first(lines_of(p('tools', 'circuit_read.py')), 'def readfirst('), '0')
    add('ruling (8)', 'data/b707_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b707_readfirst.txt')), '0')
    add('ruling (8)', 'data/b708_rules.txt by form (the (W) list admits it; none written)', not os.path.exists(p('data', 'b708_rules.txt')), 'absent; admitted by form', '5')
    add('ruling (9)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b707_worklist.py DRAFT', '6')
    add('ruling (10)', 'W-ORD-STANDING-CLAUSES-BANK at OPEN_TRAILS :15450, trigger b710', 'W-ORD-STANDING-CLAUSES-BANK' in at(ot, K.ORDER_STANDING_CLAUSES) and 'Trigger: the reading act b710' in at(ot, K.ORDER_STANDING_CLAUSES), 'OPEN_TRAILS :%d' % K.ORDER_STANDING_CLAUSES, '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5'), ('R315', (7,), '2')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C5', 'the four standing arms` figures tool and b706`s baseline', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b706_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b706_standing_figures.json', '5')
    add('ferry; ruling (3)', 'data/b680_rules.txt (1), a binary bank beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt :5', '2')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'data/b706_rules.txt row (1): ROOT_EXCLUDE carried and extended, the root route dry READY before the seal', 'a face whose dry READY reads False is not locked' in (rd(p('data', 'b706_rules.txt')) or ''), 'data/b706_rules.txt :6-:15', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b706_relay_push_out.txt')), 'data/b706_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b706_mirror.txt')), 'data/b706_mirror.txt (the form carried)', '6')
    add('ferry C6', 'the report tool b706 wrote (tools/b706_report.py), its form carried as tools/b707_report.py', os.path.exists(p('tools', 'b706_report.py')) and not os.path.exists(p('tools', 'b707_report.py')), 'tools/b706_report.py ; tools/b707_report.py TO BE WRITTEN', '6')
    add('ferry C0', 'this act`s session transcript (a new session; b706 ran in 44411d52)', os.path.exists(C.SESSION) and os.path.exists('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.PREV_SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b707_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b707_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b707 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b707_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b707_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b707_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b707_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### b706's repair of the answer checker (b705 defect (n)), carried: b682's route reads every bare eight-hex token as a commit. A token that a
# ### bank's row names as a sha256 -- the root list, a hashes bank's row, a bank line carrying "sha256" -- or that a kernel's lakefile or
# ### manifest pins as a rev, is a root prefix, a file hash or a pin, not a commit, and is checked against that row instead.
_HEX8 = re.compile(r'(?<![0-9a-f])([0-9a-f]{8})(?![0-9a-f])')


def _sha_rows():
    out = {}
    for q in [os.path.join(D, 'act_roots.txt')] + sorted(glob.glob(os.path.join(D, '*.txt')), reverse=True):   # ### the later act's row named first
        t = rd(q) or ''
        if 'sha256' not in t and not q.endswith('act_roots.txt') and not q.endswith('_hashes.txt'):
            continue
        for i, l in enumerate(t.split(NL), 1):
            if 'sha256' in l or q.endswith('act_roots.txt') or q.endswith('_hashes.txt'):
                for m in re.finditer(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])', l):
                    out.setdefault(m.group(1)[:8], ('data/' + os.path.basename(q), i))
    for kd in sorted(d_ for d_ in os.listdir('D:/') if d_.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d_, '.git'))):
        for f in ('lakefile.toml', 'lakefile.lean', 'lake-manifest.json'):
            t = rd(os.path.join('D:/', kd, f)) or ''
            for i, l in enumerate(t.split(NL), 1):
                for m in re.finditer(r'(?:rev\s*=\s*"|"rev"\s*:\s*"|@\s*"|rev\s+")([0-9a-f]{40})"', l):
                    out.setdefault(m.group(1)[:8], ('%s/%s' % (kd, f), i))
    return out


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b707, and b706's repair carried: before b682's body runs, every eight-hex
    token of the answer that a bank's row names as a sha256 is checked against that row and printed, and masked from b682's commit reading."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b707'))
    shas = _sha_rows()
    base = P.C._user_texts

    def masked(*k, **kw):
        out = []
        for t in base(*k, **kw):
            if t and needle in t:
                for m in _HEX8.finditer(t):
                    h8 = m.group(1)
                    if h8 in shas:
                        print('  ### SHA256 PREFIX %s... NAMED BY %s :%d -- a root or file hash by its bank`s row, not a commit; OK, masked from the commit reading' % (h8, shas[h8][0], shas[h8][1]))
                        t = t.replace(h8, 'SHA-' + h8[:4] + '-' + h8[4:])
            out.append(t)
        return out

    P.C._user_texts = masked
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b707')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b707)', 'exec'), ns)
    ns['answer'](needle)


def word(needle, *a):
    """(R278)(4) on an author's word delivered as a bare BEGIN ... END paste: b694's route."""
    import b682_citation as P
    base = C._user_texts

    def marked(*k, **kw):
        return [("THE AUTHOR'S WORD " + t) if (t or '').lstrip().startswith(('BEGIN', '<pasted_content')) and 'END' in (t or '') else t
                for t in base(*k, **kw)]

    C._user_texts = marked
    P.C._user_texts = marked
    answer(needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer, 'word': word}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b707_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
