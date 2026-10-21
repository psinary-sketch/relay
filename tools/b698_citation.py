# -*- coding: utf-8 -*-
"""b698_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b698's step zero, run before any other step
((R308)(8)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (c677eaf2); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b698; the `word` route
### is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b698_citation_check.txt (.json) ; `ferry` -> data/b698_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b698 from b697_citation.py's form; this tool writes only the banks named above.
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
import b677_citation as C   # noqa: E402  ### the helpers, imported unchanged
import b698_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle):
    return next((i + 1 for i, l in enumerate(L) if needle in l), 0)


def show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    page = lines_of(os.path.join(PP, K.FACES_PAGE))
    SI = 'D:/SIDE-simplicity'
    # ### the ferry's read-first list
    for f in ('data/b697_closing.txt', 'data/b697_defects.txt', 'data/b697_cut.txt', 'data/b697_arith_plan.txt', 'data/b697_read_calls.txt',
              'data/b695_circuit_spec.txt', 'data/b690_nodes_zeta.txt', 'data/b676_strip_uses.txt', 'data/b684_residue_actions.txt',
              'data/b670_licensed_table.txt', 'tools/correspondence_gen.py', 'tools/circuit_read.py', 'data/b697_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b697_closing.txt'))
    df = lines_of(p('data', 'b697_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b697_defects.txt (rows are defects as lettered)', lt == list('abc'), 'letters %s' % ''.join(lt), '0')
    cu = lines_of(p('data', 'b697_cut.txt'))
    add('ferry read-first', 'data/b697_cut.txt, the quoting line by line', len(cu) > 17 and cu[16].startswith('  R-1  README.md :9'), 'data/b697_cut.txt :17', '0-4')
    add('ferry read-first', 'data/b697_cut.txt, the held cell by line', len(cu) > 19 and 'SIMPLICITY_OF_RIEMANN_ZEROS :441' in cu[18], 'data/b697_cut.txt :19', '0-4')
    ap = lines_of(p('data', 'b697_arith_plan.txt'))
    add('ferry read-first', 'data/b697_arith_plan.txt, both routes by row', first(ap, '== 2. THE QUANTITY (ROUTE A') == 34 and first(ap, '== 3. THE SECOND ROUTE (ROUTE B') == 50,
        'data/b697_arith_plan.txt :34 (Route A), :50 (Route B), :112 the summary', '0-1')
    rc = lines_of(p('data', 'b697_read_calls.txt'))
    add('ferry read-first', 'data/b697_read_calls.txt', len(rc) > 22 and 'READ CALLS 60 ; WITH OFFSET AND LIMIT 42 ; WITHOUT BOTH 18' in rc[22], 'data/b697_read_calls.txt :23', '0-1')
    cs = lines_of(p('data', 'b695_circuit_spec.txt'))
    add('ferry read-first', 'data/b695_circuit_spec.txt row 11', len(cs) > 53 and cs[52].strip() == 'CORRESPONDENCE-DOMINANCE', 'data/b695_circuit_spec.txt :53-:64', '0-2')
    nz = lines_of(p('data', 'b690_nodes_zeta.txt'))
    add('ferry read-first', 'data/b690_nodes_zeta.txt :126', len(nz) > 125 and nz[125].startswith('@corr SIDE-lv-conservation | residue_irreducible'),
        'data/b690_nodes_zeta.txt :126', '0-2')
    pl = first(page, '| `residue_irreducible` | SIDE-lv-conservation |')
    add('ferry read-first', 'the faces page`s Correspondence row for SIDE-lv-conservation by line', pl > 0, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md :%d' % pl, '0-2')
    row = nz[125] if len(nz) > 125 else ''
    lvtag = re.findall(r'SIDE-lv-conservation (v[0-9.]+)', row + (page[pl - 1] if pl else ''))
    add('ferry read-first', 'SIDE-lv-conservation`s print bank at the tag the row names', bool(lvtag),
        'the row names no SIDE-lv-conservation tag (it names %s); the lv print bank, data/b694_prints_SIDE-lv-conservation.txt, is an axioms bank of '
        'the 8 T3 terminals, residue_irreducible not among them, and no relay bank carries residue_irreducible`s printed statement'
        % ', '.join(re.findall(r'SIDE-explicit-formula v[0-9.]+ = [0-9a-f]+', row)), '0-2')
    pr = rd(p('data', 'b643_probe_out_zeta.txt')) or ''
    v34 = [f for f in ('b689_prints_SIDE-explicit-formula.txt', 'b691_prints_SIDE-explicit-formula.txt', 'b692_prints_SIDE-explicit-formula.txt')
           if 'def SIDEExplicitFormula.B321.h2_sign : Prop' in (rd(p('data', f)) or '')]
    add('ferry read-first', 'SIDE-explicit-formula`s print bank at v0.34, the h2_sign line by row', bool(v34),
        'no v0.34 print bank carries h2_sign`s statement (data/b689_, b691_, b692_prints_SIDE-explicit-formula.txt are axioms banks); its #print '
        'is banked in the generator`s probe data/b643_probe_out_zeta.txt :%d-:%d at v0.26 = 82550e4, H2Sign.lean unchanged v0.26 to v0.34 %s' % (
            first(pr.split(NL), '@@BEGIN SIDEExplicitFormula.B321.h2_sign'), first(pr.split(NL), '@@END SIDEExplicitFormula.B321.h2_sign'),
            g(K.EF_DIR, 'diff', '--quiet', 'v0.26', K.EF_TAG, '--', 'SIDEExplicitFormula/H2Sign.lean')[0] == 0), '0-2')
    h2 = show(K.EF_DIR, K.EF_TAG, 'SIDEExplicitFormula/H2Sign.lean').split(NL)
    add('ferry read-first', 'H2Sign.lean :22-:29 at v0.34', len(h2) > 29 and h2[21].startswith('/-- The class K') and h2[23].startswith('def classK')
        and h2[28].startswith('def h2_sign : Prop'), 'SIDE-explicit-formula v0.34 = %s SIDEExplicitFormula/H2Sign.lean :22 (classK`s docstring), :24 '
        '(classK), :28-:29 (h2_sign)' % g(K.EF_DIR, 'rev-parse', '--short', K.EF_TAG + '^{commit}')[1].strip(), '0-3')
    ot = lines_of(OT)
    add('ferry read-first', 'OPEN_TRAILS :15200 (W-ORD-H2-BRIDGE as annotated)', len(ot) > 15199 and 'beneath `W-ORD-H2-BRIDGE` (:10257)' in ot[15199], 'OPEN_TRAILS :15200', '0-2')
    add('ferry read-first', '(R128)(2)`s line', len(ot) > 10256 and ot[10256].startswith('(2) **`W-ORD-H2-BRIDGE`**'), 'OPEN_TRAILS :10257', '0-2')
    su = lines_of(p('data', 'b676_strip_uses.txt'))
    add('ferry read-first', 'data/b676_strip_uses.txt (the template; rows are uses)', len(su) > 45 and su[5].startswith('### rows are uses'),
        'data/b676_strip_uses.txt :6 (the row unit), :9-:30 (the uses), :46 (the summary)', '0-3')
    ra = lines_of(p('data', 'b684_residue_actions.txt'))
    add('ferry read-first', 'data/b684`s residue ACTION form by path', len(ra) > 6 and ra[6].startswith('== R1'), 'data/b684_residue_actions.txt :7-:16 (R1, the form)', '0-4')
    tb = lines_of(p('data', 'b647_table_SIDE-simplicity.txt'))
    lt_ = lines_of(p('data', 'b670_licensed_table.txt'))
    add('ferry read-first', 'the licensed table`s SIDE-simplicity row (the claim at its ceiling by line)', len(tb) > 14 and tb[11].strip().startswith('LICENSED')
        and tb[13].strip().startswith('ACTION') and first(lt_, 'SIDE-simplicity docstrings (read at 54ba4f3)                      1 ->    1') == 115,
        'data/b670_licensed_table.txt :115 ; data/b647_table_SIDE-simplicity.txt :12 (LICENSED), :14 (ACTION)', '0-4')
    add('ferry read-first', 'tools/correspondence_gen.py', 'read_carry' in (rd(p('tools', 'correspondence_gen.py')) or ''), 'tools/correspondence_gen.py', '0-4')
    add('ferry read-first', 'tools/circuit_read.py', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    po = rd(p('data', 'b697_closing_push_out.txt')) or ''
    add('ferry read-first', 'data/b697_closing_push_out.txt (commit at the start)', 'main read back at the remote: dcce6eed' in po
        and not (g(ROOT, 'ls-files', 'data/b697_closing_push_out.txt')[1] or '').strip(), 'untracked at the working tree ; :5', '0')
    # ### (R308)(1)
    add('ruling (1)', 'the head line quoted from data/b697_closing.txt :1', cl[0] == ('b697 closed: relay 5d4932b5, PLACE-papers f5a4a6e; suite 120 of 120; '
                                                                                   'root afc141e1f2179e86\u2026; 1 prompt answered; 3 defects'), cl[0][:120], '1')
    add('ruling (1)', 'the closing pushed and read back at relay main dcce6eed', 'main read back at the remote: dcce6eed' in po, 'data/b697_closing_push_out.txt :5', '1')
    fd = rd(p('data', 'b697_faces_date.txt')) or ''
    add('ruling (1)', 'the head`s date read as the act`s opening UTC date (data/b697_faces_date.txt)', "THE ACT'S OPENING UTC DATE AS ITS MIRROR NAMES IT" in fd,
        'data/b697_faces_date.txt :23', '1')
    fx = rd(p('data', 'b697_faces_diff.txt')) or ''
    add('ruling (1)', 'b695`s list re-emitting the page byte for byte; the page differing at :3 and :734 alone', 'CONTROL EQUAL True ; LINES DIFFERING :3, :734' in fx,
        'data/b697_faces_diff.txt :20', '1')
    add('ruling (1)', 'the row carrying ± 3.68e-23', len(page) > 733 and '± 3.68e-23' in page[733], 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md :734', '1')
    ti = rd(p('data', 'b697_tie.txt')) or ''
    add('ruling (1)', 'tied with SIDE-substrate-cluster, named at the OVERREACHES step, 1 against 0', 'SIDE-simplicity (THE TOP COUNT 1, 2 DOCUMENTS AT IT ; DECIDED AT STEP (i))' in ti
        and 'SIDE-substrate-cluster: ROWS 78 ; MATCHES 77 ; UNDERSTATES 0 ; OVERREACHES 0' in ti, 'data/b697_tie.txt :40, :44', '1')
    add('ruling (1)', 'runs 39530030132 and 39530116146, merged at 53df27f, tagged v0.1.1 naming v0.1.0', len(cu) > 9 and '39530030132' in cu[8] and '39530116146' in cu[8]
        and 'the merge 53df27f' in cu[6] and 'naming the' in cu[6] and 'v0.1.0 = 54ba4f3' in cu[7], 'data/b697_cut.txt :7-:9', '1')
    add('ruling (1)', 'the distance 1 to 0', 'THE DISTANCE BEFORE 1, AFTER 0' in (cu[-2] if len(cu) > 2 else ''), 'data/b697_cut.txt :21', '1')
    rm = lines_of(os.path.join(SI, 'README.md'))
    add('ruling (1)', 'SIDE-simplicity README.md :9 restating the old claim', len(rm) > 8 and 'Section I.2 (perpendicular crossing) and Section III (trace-formula closing logic) '
        'are already proved in SIDE-kernel' in rm[8], 'SIDE-simplicity README.md :9', '1')
    sp = lines_of(os.path.join(PP, 'phase1.5', 'simplicity', K.STALE_PAGE))
    add('ruling (1)', 'SIMPLICITY_OF_RIEMANN_ZEROS :441 with the kernel token v0.1.0', len(sp) > 440 and '| SIDE-simplicity v0.1.0 |' in sp[440],
        'PLACE-papers phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md :441', '1')
    add('ruling (1)', 'li_identity_sym; blPoly a Laguerre polynomial; m ≈ e^{4n}', len(ap) > 45 and 'li_identity_sym' in ap[13] and 'L_{n−1}^{(1)}(X)' in ap[40]
        and 'e^(4n)' in ap[43], 'data/b697_arith_plan.txt :14, :41, :44', '1')
    add('ruling (1)', 'Route A at 3 foreground parts for n ≤ 2; not priceable at n ≈ 10⁴; Route B priceable in the tens', len(ap) > 111
        and 'PRICED AT 3 FOREGROUND PARTS FOR n ≤ 2' in ap[111] and 'ROUTE B (LAGARIAS LEMMA 4.2) OFFERED, PRICEABLE AT n IN THE TENS' in ap[111], 'data/b697_arith_plan.txt :112', '1')
    for f in ('b697_checks.txt', 'b697_checks_postpush.txt'):
        add('ruling (1)', 'suite 120 of 120 (%s)' % f, 'ARMS RUN : 120. ### LIVE PASSING : 120.' in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = rd(p('data', 'b697_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b697_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    mi = rd(p('data', 'b697_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-21-b697.zip CLEAN with the root line', 'Act root: b697 afc141e1' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi
        and 'mirror-refresh-2026-10-21-b697.zip' in mi, 'data/b697_mirror.txt', '1')
    add('ruling (1)', 'three defects, the seat`s, (a)-(c)', lt == list('abc') and len(re.findall(r"^    \([abc]\) THE SEAT'S", NL.join(df), re.M)) == 3,
        'data/b697_defects.txt :6-:19', '1')
    add('ruling (1)', '(b) 18 of 60 Read calls reading a file whole', len(rc) > 22 and 'READ CALLS 60' in rc[22] and 'WITHOUT BOTH 18' in rc[22], 'data/b697_read_calls.txt :23', '1')
    add('ruling (1)', 'one event beneath, an act arm stricter than the ferry', first(df, 'The first pre-run of the act part') == 26, 'data/b697_defects.txt :26-:28', '1')
    # ### (R308)(2)
    add('ruling (2)', 'data/b697_arith_plan.txt with both routes', bool(ap) and first(ap, 'ROUTE B') > 0, 'data/b697_arith_plan.txt', '1')
    # ### (R308)(3)
    add('ruling (3)', 'data/b695_circuit_spec.txt row 11', len(cs) > 53 and cs[52].strip() == 'CORRESPONDENCE-DOMINANCE', 'data/b695_circuit_spec.txt :53', '2')
    add('ruling (3)', 'tools/circuit_correspondence.py -- TO BE WRITTEN', not os.path.exists(p('tools', 'circuit_correspondence.py')), 'absent, as ordered', '2')
    add('ruling (3)', 'the compiled face the row names (data/b690_nodes_zeta.txt :126 and the row`s line in the page)', len(nz) > 125 and 'residue_irreducible' in nz[125] and pl > 0,
        'data/b690_nodes_zeta.txt :126 ; the page :%d' % pl, '2')
    add('ruling (3)', 'its #print sig from lv-conservation`s print bank at the tag the row names', bool(lvtag), 'as the read-first row: no tag named, no print banked', '2')
    add('ruling (3)', 'h2_sign`s statement from SIDE-explicit-formula`s print bank at v0.34', bool(v34), 'as the read-first row: the probe at v0.26 prints it', '2')
    gl = lines_of(p('data', 'glossary.txt'))
    add('ruling (3)', 'H2Sign.lean :28-:29 as the glossary cites it', 'H2Sign.lean :28-:29' in (gl[10] if len(gl) > 10 else '') and len(h2) > 29 and h2[28].startswith('def h2_sign'),
        'data/glossary.txt :11 ; H2Sign.lean :28-:29 at v0.34', '2')
    add('ruling (3)', 'data/b698_correspondence_dominance.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b698_correspondence_dominance.txt')), 'absent, as ordered', '2')
    cd = lines_of(p('data', 'b694_circuit_dominance.txt'))
    add('ruling (3)', 'CLAUSE-DOMINANCE 1 of 2 by closure', len(cd) > 11 and 'CLAUSE-DOMINANCE 1 OF 2 FACES KERNELS' in cd[11], 'data/b694_circuit_dominance.txt :12', '2')
    add('ruling (3)', 'W-ORD-H2-BRIDGE ((R128)(2), OPEN_TRAILS :15200 as annotated)', len(ot) > 15199 and 'W-ORD-H2-BRIDGE' in ot[15199] and 'W-ORD-H2-BRIDGE' in ot[10256],
        'OPEN_TRAILS :10257 ; :15200', '2')
    # ### (R308)(4)
    add('ruling (4)', 'data/b676_strip_uses.txt the template', bool(su), 'data/b676_strip_uses.txt', '3')
    add('ruling (4)', 'classK`s four hypotheses (even, C², compact support, h ⋆ h~)', len(h2) > 25 and 'k (-x) = k x' in h2[24] and 'ContDiff ℝ 2 k' in h2[24]
        and 'HasCompactSupport k' in h2[24] and 'Zeta23.EF.weilTest h h' in h2[25], 'H2Sign.lean :24-:26 at v0.34', '3')
    add('ruling (4)', 'data/b698_regularity_uses.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b698_regularity_uses.txt')), 'absent, as ordered', '3')
    # ### (R308)(5)
    add('ruling (5)', 'b684`s form', bool(ra), 'data/b684_residue_actions.txt', '4')
    add('ruling (5)', 'data/b698_residue_actions.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b698_residue_actions.txt')), 'absent, as ordered', '4')
    add('ruling (5)', 'the licensed table`s row for SIDE-simplicity (the claim at its ceiling)', len(tb) > 13 and 'Only Section III' in tb[11], 'data/b647_table_SIDE-simplicity.txt :12', '4')
    add('ruling (5)', 'recut-simplicity-readme-b698 -- not yet a branch ; v0.1.2 -- not yet a tag', not g(SI, 'branch', '--list', 'recut-simplicity-readme-b698')[1].strip()
        and not g(SI, 'tag', '-l', K.NEXT_TAG)[1].strip() and g(SI, 'tag', '-l', K.PRIOR_TAG)[1].strip() == K.PRIOR_TAG, 'SIDE-simplicity tags (v0.1.1 present)', '4')
    add('ruling (5)', 'b676`s form (the re-cut)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '4')
    add('ruling (5)', 'data/b698_rules.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b698_rules.txt')), 'absent, as ordered', '0')
    # ### (R308)(6)
    add('ruling (6)', 'source b697 (b)', len(df) > 10 and df[10].startswith('    (b) THE SEAT'), 'data/b697_defects.txt :11', '0')
    # ### (R308)(7)
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (7)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'listed at the working repository before any delete', '0')
    for repo, b in K.DELETE_REMOTE:
        add('ruling (7)', '%s %s (remote)' % (os.path.basename(repo), b), bool(g(repo, 'branch', '-r', '--list', 'origin/' + b)[1].strip()),
            'the remote-tracking ref origin/%s at the working repository' % b, '0')
    # ### (R308)(8)-(10)
    add('ruling (8)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (9)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b697_worklist.py')) or ''), 'tools/b697_worklist.py :25', '6')
    add('ruling (10)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '6')
    add('ruling (10)', 'b674`s rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '6')
    add('ruling (10)', 'rule (2) of data/b690_rules.txt', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''), 'data/b690_rules.txt :9', '6')
    add('ruling (10)', '(R307)(8)`s list for reading 4', 'b700 the reading act, reading 4' in (line(p('data', 'b697_ferry.txt'), 19) or ''), 'data/b697_ferry.txt :19', '6')
    add('ruling (10)', 'W-ORD-EPSTEIN-COUNT-LEAN', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(OT) or ''), 'OPEN_TRAILS', '6')
    # ### the ferry
    add('ferry C1', 'b697`s entry and trail', (line(FI, K.B697_ENTRY) or '').startswith('## ') and (line(OT, K.B697_TRAIL) or '').startswith('### b697'),
        'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B697_ENTRY, K.B697_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b697_relay_push_out.txt')), 'data/b697_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b670_mirror.txt')) or os.path.exists(p('data', 'b697_mirror.txt')), 'data/b697_mirror.txt (the form carried)', '6')
    add('ruling; ferry', 'data/b698_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b698_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b698_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b698_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b698 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R308)(8)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b698_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b698_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b698_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b698_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b698."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b698'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b698')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b698)', 'exec'), ns)
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
        print('usage: b698_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
