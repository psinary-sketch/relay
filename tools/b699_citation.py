# -*- coding: utf-8 -*-
"""b699_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b699's step zero, run before any other step
((R309)(7)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (c677eaf2); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b699 and its commit reach
### widened to the act's kernels as b698 widened it; the `word` route is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b699_citation_check.txt (.json) ; `ferry` -> data/b699_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b699 from b698_citation.py's form; this tool writes only the banks named above.
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
import b699_worklist as K   # noqa: E402

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


def at(L, n):
    return L[n - 1] if len(L) >= n else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    SI = 'D:/SIDE-simplicity'
    # ### the ferry's read-first list
    for f in ('data/b698_closing.txt', 'data/b698_defects.txt', 'data/b698_correspondence_dominance.txt', 'data/b698_regularity_uses.txt',
              'data/b698_rules.txt', 'data/b697_cut.txt', 'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b690_rules.txt',
              'tools/correspondence_gen.py', 'data/b698_roster_simplicity.json', 'tools/b678_corrigendum.py', 'data/b698_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b698_closing.txt'))
    add('ferry read-first', 'data/b698_closing.txt :1 the head line', cl[0].startswith('b698 closed: relay f19eccc4'), 'data/b698_closing.txt :1', '0')
    s0 = [i + 1 for i, l in enumerate(cl) if '2d19edd' in l or '069778f' in l]
    add('ferry read-first', 'data/b698_closing.txt, section (0)`s two commits by line', bool(s0), 'data/b698_closing.txt :%s (the defect (c) row as the closing '
        'carries it)' % ', :'.join(str(i) for i in s0), '0')
    df = lines_of(p('data', 'b698_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b698_defects.txt (rows are defects as lettered)', lt == list('abcd'), 'letters %s' % ''.join(lt), '0')
    cd = lines_of(p('data', 'b698_correspondence_dominance.txt'))
    b1 = first(cd, '  binder 1   |')
    add('ferry read-first', 'data/b698_correspondence_dominance.txt (rows are binders; binder 1 by line)', b1 == 33 and 'h2_sign: (k : ℝ → ℂ)' in at(cd, 33),
        'data/b698_correspondence_dominance.txt :33 (binder 1), :77 (the verdict)', '0-3')
    ru = lines_of(p('data', 'b698_regularity_uses.txt'))
    add('ferry read-first', 'data/b698_regularity_uses.txt (rows are uses; the per-column counts by line)', at(ru, 24).startswith('### rows are uses')
        and 'W1 DISCHARGED 11, RE-PROVED 6, OBSTRUCTED 0 ; W2 DISCHARGED 6, RE-PROVED 4, OBSTRUCTED 7 ; W3 DISCHARGED 13, RE-PROVED 4, OBSTRUCTED 0' in at(ru, 85),
        'data/b698_regularity_uses.txt :24 (the row unit), :85 (the uses` counts), :86 (the path`s)', '0')
    rr = lines_of(p('data', 'b698_rules.txt'))
    add('ferry read-first', 'data/b698_rules.txt rows (1) and (2)', at(rr, 6).startswith("  (1) A KERNEL'S TAG MOVE REGENERATES")
        and at(rr, 10).startswith('  (2) THE READ TOOL READS A FILE WHOLE'), 'data/b698_rules.txt :6-:9 (1), :10-:12 (2)', '0')
    ot = lines_of(OT)
    add('ferry read-first', 'OPEN_TRAILS at W-ORD-H2-BRIDGE by line', at(ot, 10257).startswith('(2) **`W-ORD-H2-BRIDGE`**')
        and 'beneath `W-ORD-H2-BRIDGE`' in at(ot, K.B698_BRIDGE_LINE), 'OPEN_TRAILS :10257 (the order), :15200 (annotated), :%d (b698`s binder 1)' % K.B698_BRIDGE_LINE, '0-3')
    oc = first(ot, 'W-ORD-ONE-COPY')
    add('ferry read-first', 'OPEN_TRAILS at W-ORD-ONE-COPY by line', oc == 14386 and 'beneath `W-ORD-ONE-COPY`' in at(ot, K.B698_ONECOPY_LINE),
        'OPEN_TRAILS :14386 (the order), :14450 (its trigger), :%d (b698`s reading)' % K.B698_ONECOPY_LINE, '0-3')
    cu = lines_of(p('data', 'b697_cut.txt'))
    rc = lines_of(p('data', 'b698_readme_cut.txt'))
    held = [i + 1 for i, l in enumerate(rc) if l.startswith('  PATHS_TO_THE_CRITICAL_LINE :285 |')]
    add('ferry read-first', 'data/b697_cut.txt (the three archimedean cells by line)', False,
        'data/b697_cut.txt :19 names the three SIDE-archimedean cells as a count in one line ("THREE SIDE-archimedean`S AS AT b693"), none by its own '
        'line; the three by line stand in data/b698_readme_cut.txt :%s (b698`s held-cells section, the cells by kind: kernel, profile, status)'
        % ', :'.join(str(i) for i in held), '0-3')
    lt_ = lines_of(p('data', 'b670_licensed_table.txt'))
    sc_ = first(lt_, 'SIDE-substrate-cluster docstrings')
    add('ferry read-first', 'data/b670_licensed_table.txt and the per-document tables (rows are licensed-table rows)', sc_ > 0
        and at(lines_of(p('data', 'b647_table_SIDE-substrate-cluster.txt')), 96).startswith('### ### **SIDE-substrate-cluster: ROWS 78'),
        'data/b670_licensed_table.txt :%d (SIDE-substrate-cluster) ; data/b647_table_SIDE-substrate-cluster.txt :96 (its summary)' % sc_, '0-2')
    add('ferry read-first', 'data/b674_rules.txt (the tie-break rule by line)', at(lines_of(p('data', 'b674_rules.txt')), 8).startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'),
        'data/b674_rules.txt :8-:11', '0-2')
    add('ferry read-first', 'data/b690_rules.txt row (2)', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in at(lines_of(p('data', 'b690_rules.txt')), 9),
        'data/b690_rules.txt :9-:12', '0-2')
    add('ferry read-first', 'tools/correspondence_gen.py and the one-table roster form', 'read_carry' in (rd(p('tools', 'correspondence_gen.py')) or '')
        and '"partner_lines_differing": 6' in (rd(p('data', 'b698_roster_simplicity.json')) or ''), 'tools/correspondence_gen.py ; data/b698_roster_simplicity.json :1-:42', '0-3')
    co = [f for f in sorted(os.listdir(T)) if re.match(r'b\d+_corrigendum\.py$', f)]
    ran698 = any('corrigendum' in (rd(p('tools', f)) or '') for f in ('b698_record.py', 'b698_closing.py', 'b698_worklist.py'))
    add('ferry read-first', 'tools/b678_corrigendum.py`s successor as b698 ran it', ran698,
        'b698 ran no corrigendum tool (no b698 tool names one); the successors on disk: %s, the last tools/%s' % (', '.join(co), co[-1] if co else 'NONE'), '0-1')
    po = rd(p('data', 'b698_closing_push_out.txt')) or ''
    add('ferry read-first', 'data/b698_closing_push_out.txt (commit at the start)', 'main read back at the remote: 14a0cb57' in po
        and not (g(ROOT, 'ls-files', 'data/b698_closing_push_out.txt')[1] or '').strip(), 'untracked at the working tree', '0')
    # ### (R309)(1)
    add('ruling (1)', 'the head line quoted from data/b698_closing.txt :1', cl[0] == ('b698 closed: relay f19eccc4, PLACE-papers 1a8d8d1; suite 122 of 123; '
                                                                                   'root 1db808250727b615\u2026; 4 prompts answered; 4 defects'), cl[0][:120], '1')
    add('ruling (1)', 'the closing commit 14a0cb57 pushed and read back at relay main', 'main read back at the remote: 14a0cb577f98' in po, 'data/b698_closing_push_out.txt', '1')
    add('ruling (1)', 'tools/circuit_correspondence.py, both controls passing', os.path.exists(p('tools', 'circuit_correspondence.py'))
        and 'C1 True, C2 True' in at(cd, 77), 'data/b698_correspondence_dominance.txt :77', '1')
    add('ruling (1)', 'DIFFERS at binder 1, none of the 14 rows agreeing', 'DIFFERS at binder 1' in at(cd, 77) and 'AGREE 0 ; DIFFERS 14 of 14 rows' in at(cd, 76),
        'data/b698_correspondence_dominance.txt :76, :77', '1')
    add('ruling (1)', 'SOURCE TEXT at v0.13.0 = 8e3bc76, source against print', 'SOURCE AGAINST PRINT' in at(cd, 77) and first(cd, '8e3bc76') > 0,
        'data/b698_correspondence_dominance.txt :%d, :77' % first(cd, '8e3bc76'), '1')
    add('ruling (1)', 'W-ORD-H2-BRIDGE annotated beneath, binder 1 its open object', 'THE BINDER NAMED IS THE BRIDGE’S OPEN OBJECT' in at(ot, K.B698_BRIDGE_LINE),
        'OPEN_TRAILS :%d' % K.B698_BRIDGE_LINE, '1')
    add('ruling (1)', 'CLAUSE-DOMINANCE 1 of 2 by closure, DIFFERS at binder 1 by correspondence', 'CLAUSE-DOMINANCE: 1 OF 2 BY CLOSURE' in at(cd, 77)
        and 'BY CORRESPONDENCE' in at(cd, 77), 'data/b698_correspondence_dominance.txt :77', '1')
    add('ruling (1)', 'the uses 17, W1 11/6/0, W2 6/4/7, W3 13/4/0, W1 and W3 together named', 'USES 17' in at(ru, 87) and 'THE WIDER CLASS NAMED: W1 AND W3 TOGETHER' in at(ru, 87)
        and 'W1 DISCHARGED 11, RE-PROVED 6, OBSTRUCTED 0' in at(ru, 85), 'data/b698_regularity_uses.txt :85, :87', '1')
    add('ruling (1)', 'W1`s and W2`s and W3`s names as the ruling quotes them', '"C¹ with absolutely integrable second derivative"' in at(ru, 10)
        and '"even C² of rapid decay without compact support"' in at(ru, 12) and '"finite sums of autocorrelations"' in at(ru, 14), 'data/b698_regularity_uses.txt :10, :12, :14', '1')
    pv = g(SI, 'rev-parse', '--short', 'v0.1.2^{commit}')[1].strip()
    tm = g(SI, 'tag', '-l', '--format=%(contents:subject)', 'v0.1.2')[1].strip()
    add('ruling (1)', 'SIDE-simplicity README :9 re-cut and tagged v0.1.2 naming v0.1.1', pv == '967f747' and 'v0.1.1' in tm, 'SIDE-simplicity v0.1.2 peels %s ; '
        'its message %r' % (pv, tm[:90]), '1')
    sp = lines_of(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md'))
    add('ruling (1)', 'SIMPLICITY_OF_RIEMANN_ZEROS :441 rewritten by the generator', '| SIDE-simplicity v0.1.2 |' in at(sp, 441),
        'PLACE-papers phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md :441', '1')
    oc_ = rd(p('data', 'b698_onecopy.txt')) or ''
    add('ruling (1)', 'the stored figure 6 against the real count 18', 'THE TWO TABLES DIFFER IN 18 LINES (the generator`s reading: 6)' in at(oc_.split(NL), 61),
        'data/b698_onecopy.txt :61', '1')
    add('ruling (1)', 'the arithmetic plan`s row appended', 'b698' in (rd(p('data', 'b697_arith_plan.txt')) or ''), 'data/b697_arith_plan.txt (its last rows)', '1')
    add('ruling (1)', 'the b697 weight line written', 'b697' in (line(FI, 9682) or ''), 'FINDINGS :9682', '1')
    sc = rd(p('data', 'b698_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b698_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    for f in ('b698_checks.txt', 'b698_checks_postpush.txt'):
        t = rd(p('data', f)) or ''
        add('ruling (1)', 'suite 122 of 123, G-NOTHING-RAN-AHEAD failing (%s)' % f, 'ARMS RUN : 123. ### LIVE PASSING : 122.' in t and 'G-NOTHING-RAN-AHEAD' in t,
            'data/%s' % f, '1')
    mi = rd(p('data', 'b698_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-21-b698.zip CLEAN with the root line', 'Act root: b698 1db80825' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi
        and 'mirror-refresh-2026-10-21-b698.zip' in mi, 'data/b698_mirror.txt', '1')
    add('ruling (1)', 'four defects, the seat`s, (a)-(d)', len(re.findall(r"^    \([abcd]\) THE SEAT'S", NL.join(df), re.M)) == 4, 'data/b698_defects.txt :6-:32', '1')
    # ### (R309)(2)
    ar = act_root_line('b698')
    add('ruling (2)', 'the root unchanged (data/act_roots.txt`s b698 line)', bool(ar) and ar[-1][1].startswith('1db808250727b615'), 'data/act_roots.txt (b698 %s)'
        % (ar[-1][1][:16] if ar else 'ABSENT'), '1')
    add('ruling (2)', 'the answers bank`s committed bytes', bool(g(ROOT, 'ls-files', 'data/b698_author_answers.json')[1].strip())
        and not g(ROOT, 'status', '--porcelain', 'data/b698_author_answers.json')[1].strip(), 'data/b698_author_answers.json (tracked, clean)', '1')
    add('ruling (2)', 'the counting command`s bank', bool(oc_), 'data/b698_onecopy.txt', '1')
    add('ruling (2)', 'the sealed face', os.path.exists(p(*K.B698_FACE.split('/'))), K.B698_FACE, '1')
    add('ruling (2)', 'the corrigenda bank', os.path.exists(p('data', 'b675_corrigenda.txt')), 'data/b675_corrigenda.txt', '1')
    # ### (R309)(3)
    add('ruling (3)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '2')
    add('ruling (3)', 'b674`s rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '2')
    add('ruling (3)', 'b676`s form (a kernel`s docstrings)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    add('ruling (3)', 'the b670 method', os.path.exists(p('data', 'b670_licensed_table.txt')), 'data/b670_licensed_table.txt', '2')
    add('ruling (3)', 'data/b699_cut.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b699_cut.txt')), 'absent, as ordered', '2')
    add('ruling (3)', 'data/b698_rules.txt row (1)', at(rr, 6).startswith("  (1) A KERNEL'S TAG MOVE"), 'data/b698_rules.txt :6-:9', '2')
    # ### (R309)(4)
    pa = lines_of(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE_v0_7.md'))
    add('ruling (4)', 'the three SIDE-archimedean cells at PATHS_TO_THE_CRITICAL_LINE :285 (held since b693)', '| SIDE-archimedean v0.1.0 |' in at(pa, 285)
        and 'NO PRINT BANK AT v0.1.0' in at(pa, 285) and len(held) == 3, 'PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md :285 (b672`s roster path) ; '
        'data/b698_readme_cut.txt :%s' % ', :'.join(str(i) for i in held), '3')
    add('ruling (4)', 'held since b693', 'held' in (rd(p('data', 'b693_cut.txt')) or '').lower(), 'data/b693_cut.txt', '3')
    pt = lines_of(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md'))
    add('ruling (4)', 'the partner copy`s state for those cells', '| SIDE-archimedean v0.1.0 |' in at(pt, 281), 'PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md :281 '
        '(b672`s roster partner)', '3')
    # ### (R309)(5)
    add('ruling (5)', 'W-ORD-H2-BRIDGE', at(ot, 10257).startswith('(2) **`W-ORD-H2-BRIDGE`**'), 'OPEN_TRAILS :10257', '3')
    add('ruling (5)', 'each binder`s type side by side from data/b698_correspondence_dominance.txt', b1 == 33 and first(cd, '  binder 13  |') > 0,
        'data/b698_correspondence_dominance.txt :33-:%d' % (first(cd, '  binder 13  |') + 2), '3')
    efl = (rd(os.path.join(K.EF_DIR, 'lakefile.lean')) or '') + (rd(os.path.join(K.EF_DIR, 'lakefile.toml')) or '')
    lvl = (rd(os.path.join(K.LV_DIR, 'lakefile.lean')) or '') + (rd(os.path.join(K.LV_DIR, 'lakefile.toml')) or '')
    add('ruling (5)', 'lv-conservation`s lakefile forbidding the import', bool(lvl) and 'lv-conservation' not in efl and 'lv_conservation' not in efl,
        'SIDE-explicit-formula`s lakefile requires no SIDE-lv-conservation ; SIDE-lv-conservation lakefile.lean read (%d chars)' % len(lvl), '3')
    add('ruling (5)', 'data/b699_bridge_plan.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b699_bridge_plan.txt')), 'absent, as ordered', '3')
    add('ruling (5)', 'W-ORD-EPSTEIN-COUNT-LEAN', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(OT) or ''), 'OPEN_TRAILS', '3')
    # ### (R309)(6)
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'listed at the working repository before any delete', '0')
    for repo, b in K.DELETE_REMOTE:
        add('ruling (6)', '%s %s (remote)' % (os.path.basename(repo), b), bool(g(repo, 'branch', '-r', '--list', 'origin/' + b)[1].strip()),
            'the remote-tracking ref origin/%s at the working repository' % b, '0')
    # ### (R309)(7)-(9)
    add('ruling (7)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b698_worklist.py')) or ''), 'tools/b698_worklist.py :25', '5')
    add('ruling (9)', '(R307)(8)`s list for reading 4', 'b700 the reading act, reading 4' in (line(p('data', 'b697_ferry.txt'), 19) or ''), 'data/b697_ferry.txt :19', '5')
    add('ruling (9)', 'b689`s form', os.path.exists(p('data', 'b689_ferry.txt')), 'data/b689_ferry.txt', '5')
    # ### the ferry
    add('ferry C1', 'b698`s entry and trail', (line(FI, K.B698_ENTRY) or '').startswith('## ') and (line(OT, K.B698_TRAIL) or '').startswith('### b698'),
        'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B698_ENTRY, K.B698_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '4')
    add('ferry C5', 'b673`s capture names', os.path.exists(p('data', 'b698_relay_push_out.txt')), 'data/b698_relay_push_out.txt (the form carried)', '5')
    add('ferry C5', 'the b670 form of the mirror', os.path.exists(p('data', 'b698_mirror.txt')), 'data/b698_mirror.txt (the form carried)', '5')
    add('ruling; ferry', 'data/b699_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b699_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b699_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b699_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b699 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R309)(7)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b699_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b699_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b699_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b699_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b699."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    # ### b698's widening carried: the commit reach includes the kernels this act reads; b682's tool unedited
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.LV_DIR, K.EF_DIR, K.ARCH_DIR, 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster') if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b699'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b699')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b699)', 'exec'), ns)
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
        print('usage: b699_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
