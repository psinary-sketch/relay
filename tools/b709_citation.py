# -*- coding: utf-8 -*-
"""b709_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b709's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (0be08567, the SAME session as b708; the anchor (R319)'s line is unique among the user's lines in it); the answer route is b682's,
### imported from tools/b682_citation.py with its act names pointed at b709 and its commit reach widened to the kernels, with b706's repair
### carried (a bare eight-hex token that a bank's row or a kernel's lakefile names as a sha256 or a rev is not read as a commit); the `word`
### route is b694's. Routes: `check [dry]` -> data/b709_citation_check.txt (.json) ; `ferry` -> data/b709_ferry_scan.txt ; `answer <needle>` /
### `word <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b709 from b708_citation.py's form (its engine :1-:118 and :401-:527 read by offset and limit, its cite rows
### replaced); this tool writes only the banks named above.
"""
import glob
import hashlib
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
import b709_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b708 closed: relay ab5e5278, PLACE-papers 6abebe6; suite 143 of 145; root a840da576458c3a1\u2026; 1 prompt answered; 7 defects'


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


def _tree(repo, ref):
    return [x for x in (g(repo, 'ls-tree', '-r', '--name-only', ref)[1] or '').split(NL) if x.strip()]


def _blob_lines(repo, ref, path):
    return ((g(repo, 'show', '%s:%s' % (ref, path))[1] or '').replace(chr(13), '')).split(NL)


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    EF, LV = K.EF_DIR, K.LV_DIR
    # ### the ferry's read-first list and the banks (R319)(1) names, by existence
    for f in ('data/b708_closing.txt', 'data/b708_defects.txt', 'data/b708_registrations.txt', 'data/b708_tool_repairs.txt', 'data/b708_repair_controls.txt',
              'data/b708_closing_push_out.txt', 'data/b707_port.txt', 'data/b707_registrations.txt', 'data/b707_onset.txt', 'data/b707_onset_controls.txt',
              'data/b705_i6_ranking.txt', 'data/b703_q0_band.txt', 'data/b703_registrations.txt', 'tools/b696_witness_balls.py', 'tools/b707_onset.py',
              'tools/b705_window.py', 'tools/b705_detection.py', 'tools/b675_li_bench.py', 'data/b705_detection.txt', 'data/b705_detection_controls.txt',
              'data/b705_window.txt', 'data/b675_li_bench.txt', 'tools/b708_checks.py', 'data/b708_reg_gate.txt', 'data/b680_rules.txt', 'data/b675_rules.txt',
              'data/b684_rules.txt', 'data/b686_rules.txt', 'data/b692_rules.txt', 'data/b694_rules.txt', 'data/b698_rules.txt', 'data/b706_rules.txt',
              'data/b708_rules.txt', 'data/b675_corrigenda.txt', K.B708_FACE, 'data/b708_probe_compare.txt', 'data/b708_probe_run.txt', 'data/b708_prints_v0.17.txt',
              'data/b708_cells_reread.txt', 'data/b708_cut.txt', 'data/b708_quote.txt', 'data/b708_port_lines.txt', 'data/b708_scratch_branches.txt',
              'data/b708_act_root.json', 'data/b708_root_banks.txt', 'data/b708_scores.json', 'data/b708_scores_close.json', 'data/b708_mirror.txt',
              'data/b708_mirror_verify.txt', 'data/b708_checks.txt', 'data/b708_checks_postpush.txt', 'data/b708_seal_hashes.json', 'data/b708_author_answers.txt',
              'data/b708_standing_figures.json', 'data/b708_report.txt', 'data/b708_corrigendum.txt', 'tools/b708_report.py', 'tools/b708_record.py',
              'tools/b708_citation.py', 'tools/b708_closing.py', 'tools/b708_reg_gate.py', 'tools/b708_regspec.py', 'tools/b708_corrigendum.py',
              'tools/b708_worklist.py', 'tools/b708_tests.py', 'tools/b706_standing_figures.py', 'tools/circuit_read.py', 'tools/mirror_verify.py',
              'tools/mirror_build.ps1', 'tools/mirror_prevbuild.json', 'tools/push_gated.sh', 'tools/act_root.py', 'tools/rule_arms.py', 'tools/b694_witness_terms.py',
              'data/b690_r3_residues.txt', 'data/b700_r4_licensed.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R319)(1), by row
    cl = lines_of(p('data', 'b708_closing.txt'))
    add('ruling (1)', 'data/b708_closing.txt :1, the head line, against (R319)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b708_closing.txt :1 = %r' % cl[0][:130], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b708_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and first(cl, '    (a) ', cf) > 0 and first(cl, '    (h) ', cf) > 0,
        'data/b708_closing.txt :%d (the head), (a) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (h) ', cf)), '0-1')
    po = lines_of(p('data', 'b708_closing_push_out.txt'))
    head = g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    add('ruling (1); ruling (7)', 'the closing commit relay 60739238 pushed in main mode and read back (data/b708_closing_push_out.txt, to be committed)',
        first(po, 'main read back at the remote: 607392380bf61ca2') == 5 and 'branch push-b708-closing' in at(po, 2) and head == K.PRE_RELAY,
        'data/b708_closing_push_out.txt :2 (branch push-b708-closing), :5 (read back) ; relay HEAD %s' % head, '0-1')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b708_closing_push_out.txt')[1].strip()
    add('ruling (7); ferry C0', 'data/b708_closing_push_out.txt uncommitted at the act`s start', st.startswith('??'), 'git status %r' % st, '0')
    pc = lines_of(p('data', 'b708_probe_compare.txt'))
    pr = lines_of(p('data', 'b708_probe_run.txt'))
    add('ruling (1)', 'the chain`s probe through the workflow`s own step on probe-b708 (run 39980813418), 568 of 568 cells read, 0 sigs moved against b704`s bank, the page untouched',
        first(pr, 'RUN 39980813418 (probe) ; CONCLUSION success ; THE PROBE ARTIFACT AGREE ; THE STEP RAN ; ERROR LINES 0 ; PROBE CELLS 568 OF 568 ; MISSING 0') > 0
        and first(pc, 'CELLS COMPARED 568 ; EQUAL 568 ; DIFFERING 0 ; SIGS MOVED 0') > 0 and 'THE PAGE NOT REGENERATED' in at(pc, first(pc, 'CELLS COMPARED 568')),
        'data/b708_probe_run.txt :%d ; data/b708_probe_compare.txt :%d' % (first(pr, 'RUN 39980813418 (probe)'), first(pc, 'CELLS COMPARED 568')), '1')
    sb = lines_of(p('data', 'b708_scratch_branches.txt'))
    add('ruling (1)', 'the branch deleted (data/b708_scratch_branches.txt: the two scratch branches deleted locally and at the remote)',
        first(sb, 'SCRATCH BRANCHES 2 ; DELETED LOCALLY 2 ; DELETED AT THE REMOTE 2') > 0, 'data/b708_scratch_branches.txt :%d' % first(sb, 'SCRATCH BRANCHES 2'), '1')
    cr = lines_of(p('data', 'b708_cells_reread.txt'))
    pv = lines_of(p('data', 'b708_prints_v0.17.txt'))
    add('ruling (1)', 'the entry-tag print at v0.17 (run 39980908842) reading simplicity_iff equal to its statement at v0.37; the mentions 10 of 11 equal, FACES_LEDGER :20 unbanked by its own line',
        'RUN 39980908842' in at(pv, 1) and first(cr, 'SIMPLICITY_OF_RIEMANN_ZEROS.md :442 | SIDEExplicitFormula.Simplicity.simplicity_iff | tag v0.17 | equal') > 0
        and first(cr, 'FACES_LEDGER.md :20 | (none named) | tag (no tag) | unbanked') > 0 and first(cr, 'MENTIONS 11 ; EQUAL 10 (9 CARRIED FROM b706, 1 RE-READ THIS ACT) ; DIFFERS 0 ; UNBANKED 1') > 0,
        'data/b708_prints_v0.17.txt :1 ; data/b708_cells_reread.txt :%d, :%d, :%d' % (first(cr, 'SIMPLICITY_OF_RIEMANN_ZEROS.md :442'), first(cr, 'FACES_LEDGER.md :20'), first(cr, 'MENTIONS 11 ;')), '1')
    ct = lines_of(p('data', 'b708_cut.txt'))
    qt = lines_of(p('data', 'b708_quote.txt'))
    add('ruling (1)', 'day1/Spectral_Inertness.md re-cut by the b670 method from 22 rows outside LICENSED/CITED to 3, 37 quoting lines entered as residues',
        first(ct, 'THE DISTANCE BY THE b670 METHOD: BEFORE 22, AFTER 3 ; ROWS APPLIED 20 ; HELD 4 (CORRESPONDENCE CELLS) ; QUOTING LINES 37 ENTERED AS RESIDUES') > 0
        and first(qt, 'QUOTING LINES 37 -- EACH ENTERED AS A RESIDUE ; SEARCHED BEFORE THE CUT`S COMMIT') > 0 and 'day1/Spectral_Inertness.md' in at(ct, 1),
        'data/b708_cut.txt :1, :%d ; data/b708_quote.txt :%d' % (first(ct, 'THE DISTANCE BY THE b670 METHOD: BEFORE 22'), first(qt, 'QUOTING LINES 37')), '1')
    rg8 = lines_of(p('data', 'b708_registrations.txt'))
    rfiles = [x for x in g(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', '6045dd8c')[1].split(NL) if x.strip()]
    rlog8 = g(ROOT, 'log', '--format=%h', '--', 'data/b708_registrations.txt')[1].split()
    add('ruling (1); ruling (3); ferry read-first', 'the fine grid registered and committed alone in data/b708_registrations.txt before any number (relay 6045dd8c with the rules bank; the one commit touching it)',
        first(rg8, '  (i) THE FINE GRID OF THE SIGN-ONSET RADIUS AT Q0 -- COMPUTED AT b709') == 10 and sorted(rfiles) == ['data/b708_registrations.txt', 'data/b708_rules.txt'] and rlog8 == ['6045dd8c'],
        'data/b708_registrations.txt :10 ; relay 6045dd8c carries %s ; commits touching it %s' % (rfiles, rlog8), '1-2')
    pl = lines_of(p('data', 'b708_port_lines.txt'))
    add('ruling (1); ruling (4)', 'the port`s two lines read by kind, nothing edited (data/b708_port_lines.txt: :277:55 a changed signature, :380:8 a renamed Mathlib declaration, port-b707 unedited)',
        first(pl, 'LINES 2 ; KINDS: :277:55 a changed signature ; :380:8 a renamed Mathlib declaration ; port-b707 UNEDITED True') > 0,
        'data/b708_port_lines.txt :%d' % first(pl, 'LINES 2 ; KINDS:'), '1-3')
    add('ruling (1)', 'the entry at FINDINGS :10152, the trail at OPEN_TRAILS :15724', at(fi, K.B708_ENTRY).startswith('## The faces chain probed through the workflow') and at(ot, K.B708_TRAIL) == K.B708_TRAIL_HEAD,
        'FINDINGS :%d %r ; OPEN_TRAILS :%d %r' % (K.B708_ENTRY, at(fi, K.B708_ENTRY)[:50], K.B708_TRAIL, at(ot, K.B708_TRAIL)[:60]), '1')
    ar = _jl('b708_act_root.json')
    rb = lines_of(p('data', 'b708_root_banks.txt'))
    add('ruling (1)', 'the root a840da57 over 98 banks chained from 6fe154f9 (data/b708_act_root.json; data/b708_root_banks.txt; data/act_roots.txt`s b708 row)',
        (ar.get('root') or '').startswith('a840da57') and (ar.get('previous') or '').startswith('6fe154f9') and bool(act_root_line('b708')) and first(rb, 'BANKS 98 ;') > 0,
        'data/b708_act_root.json (root %s, prev %s) ; data/b708_root_banks.txt :%d ; data/act_roots.txt row b708 %s' % ((ar.get('root') or '')[:8], (ar.get('previous') or '')[:8], first(rb, 'BANKS 98 ;'), bool(act_root_line('b708'))), '1')
    ck, cp = rd(p('data', 'b708_checks.txt')) or '', rd(p('data', 'b708_checks_postpush.txt')) or ''
    mcp = re.search(r'LIVE FAILING : \d+ \[(.*?)\]', cp)
    add('ruling (1)', 'the chain b624-b708 AGREE (G-ACTROOT-VERIFY passing post-push)', bool(mcp) and 'G-ACTROOT-VERIFY' not in mcp.group(1) and 'b708 AGREE' in cp,
        'data/b708_checks_postpush.txt LIVE FAILING %s' % (mcp.group(1) if mcp else '### NOT READ'), '1')
    mi = lines_of(p('data', 'b708_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-23-b708.zip CLEAN on all three clauses over 70 files (data/b708_mirror.txt)',
        first(mi, 'THE VERIFICATION : CLEAN ON ALL THREE CLAUSES') > 0 and first(mi, 'files 70') > 0 and os.path.exists(K.MIRROR_ZIP) and 'mirror-refresh-2026-10-23-b708.zip' in at(mi, 2),
        'data/b708_mirror.txt :2, :%d (files 70), :%d (CLEAN) ; the zip exists %s' % (first(mi, 'files 70'), first(mi, 'THE VERIFICATION : CLEAN'), os.path.exists(K.MIRROR_ZIP)), '1')
    sr, sc = _jl('b708_scores.json'), _jl('b708_scores_close.json')
    add('ruling (1)', 'N1 REFUTED as worded on the count (two dispatches, the navigator`s (f)), N2-N5 and S1-S3 HELD (data/b708_scores.json, data/b708_scores_close.json)',
        (sr.get('N1') or [''])[0] == 'REFUTED' and 'dispatches banked 2' in (sr.get('N1') or ['', ''])[1] and all((sr.get(k) or [''])[0] == 'HELD' for k in ('N2', 'N3', 'N5', 'S3'))
        and all((sc.get(k) or [''])[0] == 'HELD' for k in ('N4', 'S1', 'S2')),
        'data/b708_scores.json: %s ; data/b708_scores_close.json: N4 %s, S1 %s, S2 %s' % (', '.join('%s %s' % (k, (sr.get(k) or ['-'])[0]) for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S3')),
                                                                                    (sc.get('N4') or ['-'])[0], (sc.get('S1') or ['-'])[0], (sc.get('S2') or ['-'])[0]), '1')
    add('ruling (1)', 'suite 143 of 145 pre-push and post-push; G-READ-RULE-STANDING declared on the face and G-CLOSING-DRY-STEP found after the seal',
        'ARMS RUN : 145. ### LIVE PASSING : 143.' in ck and 'ARMS RUN : 145. ### LIVE PASSING : 143.' in cp and bool(mcp) and set(x.strip().strip("'") for x in mcp.group(1).split(',')) == {'G-READ-RULE-STANDING', 'G-CLOSING-DRY-STEP'}
        and 'BY NAME:** `G-READ-RULE-STANDING`.' in (rd(p(*K.B708_FACE.split('/'))) or ''),
        'data/b708_checks.txt ; data/b708_checks_postpush.txt ; the face`s declaration line', '1')
    df = lines_of(p('data', 'b708_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ruling (1); ferry read-first', 'data/b708_defects.txt (rows are defects as lettered): seven, (a)-(g), (c)-(f) the navigator`s, (g) the seat`s one-line interpreter program',
        [x for x, _o in lt] == list('abcdefg') and [x for x, o in lt if o == 'NAVIGATOR'] == list('cdef') and dict(lt).get('g') == 'SEAT' and 'ONE-LINE PROGRAM' in _defect_row(df, 'g')[1],
        'letters %s ; the navigator`s %s ; (g) :%d' % (''.join(x for x, _o in lt), [x for x, o in lt if o == 'NAVIGATOR'], _defect_row(df, 'g')[0]), '1')
    add('ruling (1)', '"nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b709_worklist.py DRAFT', '6')
    # ### (R319)(2)
    chk = lines_of(p('tools', 'b708_checks.py'))
    cd_ = first(chk, 'def closing_dry_ok(S):')
    nd_ = first(chk, "'### NO VERDICT LINE' not in g", cd_)
    rgt = lines_of(p('data', 'b708_reg_gate.txt'))
    nv = first(rgt, 'the entry-tag print at v0.17 (relay data/b708_prints_v0.17.txt): ### NO VERDICT LINE')
    add('ruling (2); ferry read-first', 'G-CLOSING-DRY-STEP`s source by path and line: tools/b708_checks.py closing_dry_ok, its needle "### NO VERDICT LINE" not in the gate record',
        cd_ > 0 and nd_ > 0 and nd_ - cd_ <= 6, 'tools/b708_checks.py :%d (def closing_dry_ok), :%d (the needle)' % (cd_, nd_), '1')
    add('ruling (2)', 'the closing prints "NO VERDICT LINE" for the prints bank (data/b708_reg_gate.txt, the closing dry-run step`s print), the bank carrying no verdict line by its form',
        nv > 0 and not re.search(r'(?ms)^### ### \*\*.*?\*\*\s*$', rd(p('data', 'b708_prints_v0.17.txt')) or ''),
        'data/b708_reg_gate.txt :%d ; data/b708_prints_v0.17.txt carries no `### ### **...**` line' % nv, '1')
    ev = first(df, '    G-CLOSING-DRY-STEP FAILING AFTER THE SEAL, IN THE PRE-PUSH RUN.')
    add('ruling (2)', 'b708`s post-seal item for the corrigendum (data/b708_defects.txt, the unlettered event: G-CLOSING-DRY-STEP failing after the seal)',
        ev > 0 and 'entered here unlettered' in ' '.join(df[ev - 1:ev + 7]), 'data/b708_defects.txt :%d-:%d' % (ev, ev + 6), '1')
    tr = lines_of(p('data', 'b708_tool_repairs.txt'))
    hunks = [i + 1 for i, l in enumerate(tr) if l.strip().startswith('@@')]
    add('ruling (2); ferry read-first', 'data/b708_tool_repairs.txt (the spans the carry reads): row (1) the print-list reader`s diff, its hunk headers by line',
        first(tr, '  (1) tools/b708_record.py `_print_modules708`') > 0 and len(hunks) >= 1 and first(tr, 'REPAIRS 1 ; CARRIED IN FORM 2') > 0,
        'data/b708_tool_repairs.txt :%d (row (1)), the hunks at %s, the verdict :%d' % (first(tr, '  (1) tools/b708_record.py'), hunks, first(tr, 'REPAIRS 1 ;')), '1-5')
    cgb = lines_of(p('data', 'b675_corrigenda.txt'))
    lastrow = max([int(m) for m in re.findall(r'^  \((\d+)\) ', NL.join(cgb), re.M)] or [0])
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (28), b708`s)', lastrow == 28, 'data/b675_corrigenda.txt, last row (%d) at :%d' % (lastrow, first(cgb, '  (%d) ' % lastrow)), '1')
    add('ruling (2)', 'b708`s corrigendum tool to carry (b678`s form)', os.path.exists(p('tools', 'b708_corrigendum.py')) and os.path.exists(p('tools', 'b678_corrigendum.py')), 'tools/b708_corrigendum.py ; tools/b678_corrigendum.py', '1')
    add('ruling (2); ruling (8)', 'data/b709_rules.txt row (1) -- TO BE WRITTEN at step zero (the carry read by diff)', not os.path.exists(p('data', 'b709_rules.txt')), 'absent, as ordered', '0')
    add('ruling (2); ferry C5', 'data/b708_rules.txt row (1): the report tool outside the sealed list until the root`s word; this act`s SEALED names no report tool',
        '(1) THE REPORT TOOL IS KEPT OUT OF THE SEALED LIST' in (rd(p('data', 'b708_rules.txt')) or '') and not any('report' in t for t in K.SEALED), 'data/b708_rules.txt :6 ; tools/b709_worklist.py SEALED', '5')
    add('ruling (2); ferry read-first', 'W-ORD-WORKFLOW-PROBE-STEP at OPEN_TRAILS :15544 (entered) and :15638 (discharged, the trigger b708) -- to be annotated DISCHARGED in the author`s words',
        'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_WORKFLOW_PROBE) and 'W-ORD-WORKFLOW-PROBE-STEP' in at(ot, K.ORDER_WORKFLOW_PROBE_DISCHARGED) and 'The trigger for the chain’s next probe, b708' in at(ot, K.ORDER_WORKFLOW_PROBE_DISCHARGED),
        'OPEN_TRAILS :%d, :%d' % (K.ORDER_WORKFLOW_PROBE, K.ORDER_WORKFLOW_PROBE_DISCHARGED), '1')
    # ### (R319)(3)
    add('ruling (3); ferry read-first', 'data/b708_registrations.txt (rows are registrations): the interval per family, the grid at the rungs log p^k and the midpoints, the quantity, the hypothesis, the falsifier, the controls, computed at b709',
        first(rg8, 'THE INTERVAL PER FAMILY') == 15 and first(rg8, 'THE GRID, in (R318)(3)\'s words') == 21 and first(rg8, 'THE QUANTITY: at each grid point a') == 34
        and first(rg8, 'HYPOTHESIS: the onset lies within one subdivision step past a rung') == 37 and first(rg8, 'FALSIFIER: the onset lies at a midpoint with no rung within one step below it') == 38
        and first(rg8, 'CONTROLS: (C1) the coarse endpoints') == 46 and first(rg8, 'COMPUTED AT b709') > 0,
        'data/b708_registrations.txt :15-:20 (the interval), :21-:33 (the grid: rho_0 197 rungs :24, the band 2026 rungs :26), :34 (the quantity), :37, :38, :46-:50', '2')
    on = lines_of(p('data', 'b707_onset.txt'))
    add('ruling (3); ferry read-first', 'data/b707_onset.txt (rows are rungs): the coarse endpoints per family, band 128 (positive) and 192 (negative), rho0 log2 (positive) and 32 (negative), each with its lambda_min',
        first(on, '  band | 128 ') == 17 and first(on, '  band | 192 ') == 18 and first(on, '  rho0 | log2 ') == 19 and first(on, '  rho0 | 32 ') == 20
        and 'POSITIVE DEFINITE BEYOND ITS BOUND' in at(on, 17) and 'NEGATIVE DIRECTION BEYOND ITS BOUND' in at(on, 18) and 'POSITIVE DEFINITE BEYOND ITS BOUND' in at(on, 19) and 'NEGATIVE DIRECTION BEYOND ITS BOUND' in at(on, 20),
        'data/b707_onset.txt :17-:20', '2')
    wb = lines_of(p('tools', 'b696_witness_balls.py'))
    add('ruling (3); ferry read-first', 'tools/b696_witness_balls.py :124-:146 (zero_tail: the zeros above T0 in arb) and arch_tail :90 (the certified tail the ζ control prints beside lambda_min)',
        first(wb, 'def zero_tail(') == 124 and first(wb, 'def zero_integral(') == 148 and first(wb, 'def arch_tail(') == 90,
        'tools/b696_witness_balls.py :124 (zero_tail), :148 (zero_integral), :90 (arch_tail)', '2')
    ono = lines_of(p('tools', 'b707_onset.py'))
    add('ruling (3); ferry read-first', 'tools/b707_onset.py by path (the family, the ladder, the controls before the figures, the form in balls), its reader of the registered windows',
        len(ono) > 400 and first(ono, 'def ') > 0 and os.path.exists(p('tools', 'b705_window.py')) and os.path.exists(p('tools', 'b705_detection.py')),
        'tools/b707_onset.py (%d lines) ; tools/b705_window.py ; tools/b705_detection.py' % len(ono), '2')
    add('ruling (3)', 'data/b709_grid.txt and its hashes bank -- TO BE WRITTEN by tools/b709_grid.py', not os.path.exists(p('data', 'b709_grid.txt')) and not os.path.exists(p('tools', 'b709_grid.py')), 'absent, as ordered', '2')
    # ### (R319)(4)
    rhl = _remote_heads(LV)
    add('ruling (4); ruling (7)', 'port-b707 at b707`s one commit 69e239d locally and at the remote, held (one ls-remote of SIDE-lv-conservation)',
        branch_listed(LV, K.PORT_BRANCH) and rhl.get('refs/heads/%s' % K.PORT_BRANCH) == K.PORT_BASE and g(LV, 'rev-parse', K.PORT_BRANCH)[1].strip() == K.PORT_BASE,
        'local %s ; remote %s' % (g(LV, 'rev-parse', K.PORT_BRANCH)[1].strip()[:8], (rhl.get('refs/heads/%s' % K.PORT_BRANCH) or 'absent')[:8]), '3')
    c7 = _blob_lines(LV, K.PORT_BRANCH, K.PORT_FILE)
    pt = lines_of(p('data', 'b707_port.txt'))
    h264 = first(c7, 'theorem exists_norm_completedRiemannZeta₀_le_exp_half :')
    add('ruling (4); ferry read-first', 'SIDE-lv-conservation`s C7OrderBounds.lean at port-b707 :277 and :380 (read by offset and limit at the checkout): :277 the hasMellin call; :380 "a renamed Mathlib declaration" (data/b707_port.txt`s kind as b708 read it, (R319)(4))',
        'hasMellin' in at(c7, 277) and 'exists_norm_completedRiemannZeta₀_le_exp_half' in at(c7, 380),
        'C7OrderBounds.lean :277 %r ; :380 %r -- :380 opens the kernel`s own theorem exists_norm_completedRiemannZeta₀_le_exp, whose proof (:383) uses the kernel`s own '
        'exists_norm_completedRiemannZeta₀_le_exp_half declared at :%d, the theorem that failed at :277; the kernel`s "unknown constant" at :380:8 is a cascade of :277, NOT a renamed '
        'Mathlib declaration: b708`s kind for :380 (data/b708_port_lines.txt) the seat`s misreading, the one edit at :277 answering both lines' % (at(c7, 277).strip()[:90], at(c7, 380).strip()[:90], h264), '3')
    add('ruling (4); ferry read-first', 'data/b707_port.txt (the two lines by kind): :11 :277:55 Application type mismatch (:35-:42 the hypothesis `k < re s` expected where `w` was given), :14 :380:8 unknown constant',
        'Application type mismatch' in at(pt, 11) and 'WeakFEPair.hasMellin (hurwitzEvenFEPair 0).toStrongFEPair w' in at(pt, 42) and "unknown constant 'SIDELvConservation.exists_norm_completedRiemannZeta₀_le_exp_half'" in at(pt, 14)
        and first(pt, 'modules built 6 of 12:') == 16,
        'data/b707_port.txt :11, :14, :16, :35-:42', '3')
    add('ruling (4)', 'the deposit and lv-conservation`s main stand (v0.10.0 at 93c27ec, main at d38f3e8c), the print list absent at the branch`s tree',
        g(LV, 'rev-parse', 'v0.10.0^{commit}')[1].strip() == K.LV_V0100 and g(LV, 'rev-parse', 'main')[1].strip() == K.LV_MAIN and 'print_targets.txt' not in _tree(LV, K.PORT_BRANCH) and K.WORKFLOW in _tree(LV, K.PORT_BRANCH),
        'v0.10.0 %s ; main %s ; the branch`s tree %d files, no print_targets.txt, the workflow present' % (K.LV_V0100[:8], K.LV_MAIN[:8], len(_tree(LV, K.PORT_BRANCH))), '3')
    add('ruling (4)', 'data/b709_port.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b709_port.txt')), 'absent, as ordered', '3')
    # ### (R319)(5)
    rg7 = lines_of(p('data', 'b707_registrations.txt'))
    add('ruling (5); ferry read-first', 'data/b707_registrations.txt (rows are registrations): the twelve pairs :24-:36, the route :39-:43, the precision 256 bits :45, the hypothesis :68, the falsifier [0.67, 1.5] :70, the controls :71-:75',
        first(rg7, '  (i) THE HIGHER PAIRS\' ROUTE -- COMPUTED AT b709') == 10 and first(rg7, 'idx |  Re rho') == 24 and first(rg7, '            16  |') == 36 and first(rg7, 'THE ROUTE: b675\'s route unchanged') == 39
        and "the working precision: b675's 256 bits" in at(rg7, 45) and first(rg7, 'FALSIFIER: any pair\'s n* outside [0.67, 1.5]') == 70 and first(rg7, 'CONTROLS: (C1) b675\'s figure at rho0') == 71,
        'data/b707_registrations.txt :10, :24-:36, :39, :45, :68, :70, :71-:75', '2')
    rlog7 = g(ROOT, 'log', '--format=%h', '--', 'data/b707_registrations.txt')[1].split()
    add('ruling (5)', 'the registration unchanged from its b707 commit (6e8ece87), the one commit touching it', rlog7 == ['6e8ece87'], 'commits touching data/b707_registrations.txt %s' % rlog7, '2')
    dt = lines_of(p('data', 'b705_detection.txt'))
    dc = lines_of(p('data', 'b705_detection_controls.txt'))
    add('ruling (5)', 'the controls` figures: b675`s n*(rho0) = 63676 (data/b705_detection_controls.txt :6) and b705`s five pairs idx 0-4 (data/b705_detection.txt :10-:14); the twelve idx 5-16 at :15-:26',
        '63676' in at(dc, 6) and all(('   %d ' % i) in at(dt, 10 + i) or (' %d |' % i) in at(dt, 10 + i) or at(dt, 10 + i).strip().startswith(str(i)) for i in range(5))
        and at(dt, 15).strip().startswith('5') and at(dt, 26).strip().startswith('16'),
        'data/b705_detection_controls.txt :6 %r ; data/b705_detection.txt :10 %r ... :26 %r' % (at(dc, 6).strip()[:60], at(dt, 10).strip()[:50], at(dt, 26).strip()[:50]), '2')
    lb = lines_of(p('tools', 'b675_li_bench.py'))
    add('ruling (5)', 'b675`s route (tools/b675_li_bench.py constants_for :163, onset :153) and b705`s configuration (tools/b705_detection.py pair_rows)',
        first(lb, 'def constants_for(') == 163 and first(lb, 'def onset(') == 153 and first(lines_of(p('tools', 'b705_detection.py')), 'def pair_rows(') > 0,
        'tools/b675_li_bench.py :163, :153 ; tools/b705_detection.py :%d' % first(lines_of(p('tools', 'b705_detection.py')), 'def pair_rows('), '2')
    qb = lines_of(p('data', 'b703_q0_band.txt'))
    add('ruling (5); ferry read-first', 'data/b703_q0_band.txt (rows are bins): 163 rows, 17 off the line and 146 on it (:8), the heights to 149.718 (:9), the off-line rows by real part (:13-:15)',
        'rows 163 ; off the line 17 ; on the line 146' in at(qb, 8) and '149.718' in at(qb, 9) and at(qb, 13).strip().startswith('(0.6, 0.75]') and at(qb, 15).strip().startswith('(7/8, 1)'),
        'data/b703_q0_band.txt :8, :9, :13-:15', '2')
    add('ruling (5); ferry', 'data/b680_rules.txt (1), a binary bank beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt :5', '2')
    add('ruling (5)', 'data/b709_pairs.txt and its hashes bank -- TO BE WRITTEN by tools/b709_pairs.py', not os.path.exists(p('data', 'b709_pairs.txt')) and not os.path.exists(p('tools', 'b709_pairs.py')), 'absent, as ordered', '2')
    # ### (R319)(6)
    i6 = lines_of(p('data', 'b705_i6_ranking.txt'))
    add('ruling (6); ferry read-first', 'the second axis of data/b705_i6_ranking.txt (:58, (e) representation coordinates), its statement-grade re-expression as the ranking holds it',
        first(i6, '2. (e) representation coordinates') == 58, 'data/b705_i6_ranking.txt :58 %r' % at(i6, 58).strip()[:120], '4')
    add('ruling (6)', 'data/b709_registrations.txt -- TO BE WRITTEN at step zero, committed alone before any computation', not os.path.exists(p('data', 'b709_registrations.txt')), 'absent, as ordered', '0')
    # ### (R319)(7)-(10) and the ferry
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (7)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    add('ruling (7)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b709_worklist.py HOLD', '0')
    add('ruling (8)', 'the READFIRST-CLOSURE reader', 'def readfirst(' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py :%d' % first(lines_of(p('tools', 'circuit_read.py')), 'def readfirst('), '0')
    add('ruling (8)', 'data/b710_rules.txt by form (the (W) list admits it; none written)', not os.path.exists(p('data', 'b710_rules.txt')), 'absent; admitted by form', '5')
    add('ruling (8); ferry read-first', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'tools/mirror_prevbuild.json', '5')
    add('ruling (9)', 'the draft at v5, held', K.DRAFT == '23228113', 'tools/b709_worklist.py DRAFT', '6')
    add('ruling (10)', 'W-ORD-STANDING-CLAUSES-BANK at OPEN_TRAILS :15450, trigger b710', 'W-ORD-STANDING-CLAUSES-BANK' in at(ot, K.ORDER_STANDING_CLAUSES) and 'Trigger: the reading act b710' in at(ot, K.ORDER_STANDING_CLAUSES), 'OPEN_TRAILS :%d' % K.ORDER_STANDING_CLAUSES, '6')
    add('ruling (10)', 'readings 3 and 4 (data/b690_r3_residues.txt, data/b700_r4_licensed.txt) for b710`s readfirst flip', os.path.exists(p('data', 'b690_r3_residues.txt')) and os.path.exists(p('data', 'b700_r4_licensed.txt')),
        'data/b690_r3_residues.txt ; data/b700_r4_licensed.txt', '6')
    ppf = (g(PP, 'ls-files')[1] or '').split(NL)
    bm = [x for x in ppf if 'BRIGHTENING_MOVES' in x]
    ins = [x for x in ppf if x.endswith('INSTRUMENTS.md')]
    add('ruling (10)', 'THE_BRIGHTENING_MOVES and INSTRUMENTS I-6 (for b710`s moves-by-locus table): located at PLACE-papers', bool(bm) and bool(ins), 'PLACE-papers %s ; %s' % (bm[:2], ins[:2]), '6')
    add('ruling (10)', 'W-ORD-LV-CLOSURE-JOIN at OPEN_TRAILS :15452 (the join`s dispatch for b711 where (4) completes)', 'W-ORD-LV-CLOSURE-JOIN' in at(ot, K.ORDER_LV_JOIN), 'OPEN_TRAILS :%d' % K.ORDER_LV_JOIN, '3-6')
    add('ruling (4); ruling (10)', 'W-ORD-LV-FORWARD-PORT at OPEN_TRAILS :15686 (trigger the next ruling that names it: this one)', 'W-ORD-LV-FORWARD-PORT' in at(ot, K.ORDER_LV_PORT) and 'Trigger: the next ruling that names it (b709 the research act)' in at(ot, K.ORDER_LV_PORT),
        'OPEN_TRAILS :%d' % K.ORDER_LV_PORT, '3')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them, b709 added to the second', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or '') and K.CHAIN_HALVES == (('b624', 'b658'), ('b659', 'b709')),
        'tools/b693_worklist.py :52 ; tools/b709_worklist.py CHAIN_HALVES', '5')
    add('ferry C5', 'the four standing arms` figures tool and b708`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b708_standing_figures.json')),
        'tools/b706_standing_figures.py (b707 and b708 read it unedited) ; data/b708_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'data/b706_rules.txt row (1): ROOT_EXCLUDE carried and extended, the root route dry READY before the seal', 'a face whose dry READY reads False is not locked' in (rd(p('data', 'b706_rules.txt')) or ''), 'data/b706_rules.txt :6-:15', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b708_relay_push_out.txt')), 'data/b708_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b708_mirror.txt')), 'data/b708_mirror.txt (the form carried)', '6')
    add('ferry C6', 'the unsealed report tool`s form (tools/b708_report.py, written after the root`s word; data/b708_report.txt)', os.path.exists(p('tools', 'b708_report.py')) and os.path.exists(p('data', 'b708_report.txt')) and not os.path.exists(p('tools', 'b709_report.py')),
        'tools/b708_report.py ; data/b708_report.txt ; tools/b709_report.py TO BE WRITTEN after the root`s word', '6')
    add('ferry C0', 'this act`s session transcript (the same session as b708)', os.path.exists(C.SESSION), C.SESSION, '0')
    return R


def _write(L, R, miss):
    for name, data in (('b709_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b709_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b709 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR OR ENTERED BY THE FACT CLAUSE BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b709_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b709_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b709_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b709_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b709, and b706's repair carried: before b682's body runs, every eight-hex
    token of the answer that a bank's row names as a sha256 is checked against that row and printed, and masked from b682's commit reading."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b709'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b709')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b709)', 'exec'), ns)
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
        print('usage: b709_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
