# -*- coding: utf-8 -*-
"""b686_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b686's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling; the answer route is
### b682's, imported from tools/b682_citation.py with its act names pointed at b686; the rows and the banks are b686's.
### Routes: `check` -> data/b686_citation_check.txt (.json) ; `ferry` -> data/b686_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b686 from b685_citation.py's form; this tool writes only the banks named above.
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
import b686_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID   # ### this act's session (b677's names df03c73f)
NL = chr(10)
PP, KE, TD = C.PP, C.KE, C.TD
C.ANCHOR, C.TAIL = 'RULING (R296) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection', 'D:/SIDE-window', 'D:/SIDE-trivium', 'D:/SIDE-class-number-anomaly',
                   'D:/SIDE-spinor', 'D:/SIDE-li-map')
FOUND = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b685_closing.txt', 'data/b685_defects.txt', 'data/b685_count_controls.txt', 'data/b685_count.txt', 'data/b685_scores.json',
              'tools/b685_record.py', 'data/b670_work_orders.txt', 'data/b682_correspondence_diff.txt', 'tools/correspondence_gen.py',
              'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b684_cut.txt', 'data/b685_closing_push_out.txt',
              'data/b685_count_plan.txt', 'data/b647_table_kernels.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-3')
    # ### (R296)(1): b685 at its weight
    head = (rd(p('data', 'b685_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b685_closing.txt :1', head == ('b685 closed: relay ea8e7f49, PLACE-papers d201ac8; suite 108 of 109; root '
                                                                                   '3f5aa05397b47486\u2026; 3 prompts answered; 6 defects'), head[:120], '1')
    po = rd(p('data', 'b685_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay 5c051335 read back', 'ea8e7f49..5c051335' in po and 'read back at the remote: 5c051335' in po,
        'data/b685_closing_push_out.txt :4-:5', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'ea8e7f49', 'b685 record'), (ROOT, 'relay', '5c051335', 'b685 closing'),
                                  (PP, 'PLACE-papers', 'd201ac8', 'b685 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    for f in ('b685_checks.txt', 'b685_checks_postpush.txt'):
        add('ruling (1)', 'suite 108 of 109, G-RULE-HEAD-LINE-QUOTED declared (%s)' % f,
            "ARMS RUN : 109. ### LIVE PASSING : 108. ### LIVE FAILING : 1 ['G-RULE-HEAD-LINE-QUOTED']" in (rd(p('data', f)) or ''), 'data/%s :9' % f, '1')
    add('ruling (1)', 'root 3f5aa053 in the chain', any(r[1].startswith('3f5aa05397b47486') for r in act_root_line('b685')), 'data/act_roots.txt :63', '1')
    p3 = rd(p('data', 'b685_p3.txt')) or ''
    add('ruling (1)', 'certified -150 <= t <= 149, at most 4 a window, margin 13.607, the list`s constant 0.878', 'NARROWEST MARGIN 13.607' in p3
        and 'EVERY WINDOW THERE AT MOST 4' in p3 and '0.8781' in p3 and '-150 ≤ t ≤ 149' in p3 and 'THE REMAINDER: t > 149' in p3,
        'data/b685_p3.txt :60-:74 (the bank prints 0.8781)', '1')
    se = rd(p('data', 'b685_search.txt')) or ''
    add('ruling (1)', 'ten candidates, PDFs pinned by sha256, five located', bool(re.search(r'sha256', se)) and 'Trudgian' in se and 'Bombieri' in se,
        'data/b685_search.txt', '1')
    cnt = rd(p('data', 'b685_count.txt')) or ''
    add('ruling (1)', 'a = 0.432572 ± 4e-41, b = 0, c = 1.262442 ± 1e-40; W(150) 8.31 against 50.30', 'a = 0.432571915432 ± 4.33e-41' in cnt
        and 'c = 1.26244217716 ± 1.26e-40' in cnt and 'W(150) = 8.31423262145' in cnt,
        'data/b685_count.txt :23, :30, :35 (radii 4.33e-41 and 1.26e-40, the ruling rounding them)', '1')
    add('ruling (1)', 'H1-H3, H6 HELD, H4 NOT SCORABLE, H5 REFUTED', '(H1 HELD, H2 HELD, H3 HELD, H4 NOT SCORABLE, H5 REFUTED, H6 HELD)' in cnt,
        'data/b685_count.txt :40', '1')
    ctl = rd(p('data', 'b685_count_controls.txt')) or ''
    add('ruling (1)', 'C1 clause (i) PASS, clause (ii) FAIL; P5 [176.14, 183.00] and [208.83, 216.29], shift 32.985022', 'C1 FAIL (clause (i) True, clause (ii) False)' in ctl
        and '176.14425' in ctl and '183.00280' in ctl and '208.829' in ctl and '32.985022' in ctl, 'data/b685_count_controls.txt :7, :16-:19', '1')
    add('ruling (1)', 'P3 kept "stated, not proved"', 'stated, not proved' in (rd(p('data', 'b685_p3_status.txt')) or ''), 'data/b685_p3_status.txt', '1')
    ot14832 = line(OT, 14832) or ''
    add('ruling (1); (8); ferry', 'W-ORD-EPSTEIN-COUNT OPEN at OPEN_TRAILS :14832 with the readings', '`W-ORD-EPSTEIN-COUNT` (:14678) RE-DATED' in ot14832
        and '(i)' in ot14832 and '(ii)' in ot14832 and '(iii)' in ot14832, ot14832[:90], '1')
    wo = line(p('data', 'b670_work_orders.txt'), 295) or ''
    add('ferry', 'W-ORD-EPSTEIN-COUNT by row in the orders bank', 'W-ORD-EPSTEIN-COUNT' in wo and 'OPEN' in wo and ':14832' in wo,
        'data/b670_work_orders.txt :295 (the row b685 appended; :275 b680`s)', '0')
    dl = rd(p('data', 'b685_defects.txt')) or ''
    add('ruling (1)', 'six defects: (a)-(c), (e) the navigator`s, (d), (f) the seat`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'NAVIGATOR'), ('b', 'NAVIGATOR'), ('c', 'NAVIGATOR'), ('d', 'SEAT'), ('e', 'NAVIGATOR'), ('f', 'SEAT')], 'data/b685_defects.txt :5-:34', '1')
    sc = json.load(open(p('data', 'b685_scores.json'), encoding='utf-8'))
    add('ruling (1)', 'N3 NOT SCORABLE; N1, N2, N4, N5, S1-S3 HELD', sc['N3'][0] == 'NOT SCORABLE' and all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N4', 'N5', 'S1', 'S2', 'S3')),
        'data/b685_scores.json', '1')
    add('ruling (1)', 'the b685 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-18-b685.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b685_mirror_verify.txt')) or '')
        and 'Act root: b685 3f5aa053' in (rd(p('data', 'b685_mirror.txt')) or ''), 'the zip; data/b685_mirror_verify.txt :24; data/b685_mirror.txt :6', '0')
    for f, n, needle in (('FINDINGS', 9228, '## The count law for Z_Q'), ('OPEN_TRAILS', 14834, '### b685')):
        lt = line(FIND if f == 'FINDINGS' else OT, n) or ''
        add('ruling (1)', '%s :%d (b685`s entry and trail)' % (f, n), needle in lt, lt[:70], '1')
    # ### (R296)(2): the N4 scorer's circularity
    rt = rd(p('tools', 'b685_record.py')) or ''
    add('ruling (2); ferry', 'the sealed N4 scorer reads the landed entry (tools/b685_record.py :879-:896)', (line(p('tools', 'b685_record.py'), 879) or '').startswith('def _n4():')
        and "fj = jl('b685_findings.json')" in (line(p('tools', 'b685_record.py'), 880) or ''), 'tools/b685_record.py :879-:882', '1')
    add('ruling (2); ferry', 'the entry composes its scores line from the scores bank (tools/b685_record.py :969-:970, :1005)',
        (line(p('tools', 'b685_record.py'), 969) or '').startswith('def _finding_text():') and "'**The scores.** '" in (line(p('tools', 'b685_record.py'), 1005) or ''),
        'tools/b685_record.py :969, :1005', '1')
    add('ruling (2)', 'b685`s sealed copy recorded', 'b685_record.py' in (rd(p('data', 'b685_seal_hashes.json')) or ''), 'data/b685_seal_hashes.json', '1')
    # ### (R296)(3): the three FOUNDATIONS cells
    fl = [line(os.path.join(PP, *FOUND.split('/')), n) or '' for n in (628, 629, 630)]
    add('ruling (3); ferry', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md :628-:630 name SIDE-silence-principle v0.2.1', all('SIDE-silence-principle v0.2.1' in x for x in fl),
        'the file at %s (the ferry names it without its folder)' % FOUND, '2')
    tg = g('D:/SIDE-silence-principle', 'rev-parse', '--short', 'v0.2.2^{commit}')[1].strip()
    add('ruling (3)', 'SIDE-silence-principle v0.2.2 at main', bool(tg) and tg == g('D:/SIDE-silence-principle', 'rev-parse', '--short', 'main')[1].strip(), tg, '2')
    ax = rd(p('data', 'b684_axioms_SIDE-silence-principle_after.txt')) or ''
    ru = rd(p('data', 'b684_runner_SIDE-silence-principle_after.txt')) or ''
    add('ruling (3); ferry', 'the print bank at v0.2.2 by path', bool(ax) and '675679c51a530aad829df80ef39e5dd9348268c2' in ru,
        'data/b684_axioms_SIDE-silence-principle_after.txt, its built commit in data/b684_runner_SIDE-silence-principle_after.txt :3 (675679c, '
        'the tree merged at 716b686 = v0.2.2)', '2')
    add('ruling (3)', 'b682`s 55 and 0', 'AFTER: BEHIND BY b670`S METHOD 55 AGAINST b680`S 55 ; AT THE GENERATOR`S CLAIM 0 AGAINST b680`S 0'
        in (line(p('data', 'b682_correspondence_after.txt'), 12) or ''), 'data/b682_correspondence_after.txt :12', '2')
    add('ferry', 'the b682 form of the cell diff', 'Rows are cells with before and after' in (rd(p('data', 'b682_correspondence_diff.txt')) or ''),
        'data/b682_correspondence_diff.txt :5', '2')
    add('ruling (3)', 'tools/correspondence_gen.py `--diff <stem>`', '--diff <stem>' in (rd(p('tools', 'correspondence_gen.py')) or ''), 'tools/correspondence_gen.py :37', '2')
    cut4 = rd(p('data', 'b684_cut.txt')) or ''
    add('ruling (3)', 'the three cells carried at b684', 'CELLS CHANGED 3' in cut4 and 'no cell by hand' in cut4, 'data/b684_cut.txt :80-:82', '2')
    # ### (R296)(4): the next document
    add('ruling (4); ferry', 'b652`s order (data/b652_ferry.txt :19)', 'the next kernel by descending count under the same rules, then the companions' in (line(p('data', 'b652_ferry.txt'), 19) or ''),
        'data/b652_ferry.txt :19', '3')
    add('ruling (4); ferry', 'b674`s tie-break rule (data/b674_rules.txt :8)', '(2) THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''),
        'data/b674_rules.txt :8-:12', '3')
    add('ruling (4); ferry', 'R3b`s row in data/b684_cut.txt', 'introduction :7-:12   CARRIED (R3b)' in (line(p('data', 'b684_cut.txt'), 72) or ''), 'data/b684_cut.txt :72', '3')
    add('ruling (4)', 'b676`s form (data/b676_cut.txt)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt :1-:9', '3')
    for k in ('SIDE-li-map', 'SIDE-spinor'):
        add('ruling (4)', 'the per-document table of %s' % k, os.path.exists(p('data', 'b647_table_%s.txt' % k)), 'data/b647_table_%s.txt' % k, '3')
    # ### (R296)(5): branches
    for repo, bs in (('D:/relay', ('push-b685-root', 'push-b685', 'push-b685-closing')), (PP, ('push-b685-root', 'push-b685'))):
        for b in bs:
            add('ruling (5)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (5)', 'data/b685_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b685_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R296)(7)-(8)
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b685_worklist.py')) or ''), 'tools/b685_worklist.py', '5')
    for f in ('b685_count_plan.txt', 'b685_count_controls.txt'):
        add('ruling (8)', 'data/%s for b687`s plan' % f, os.path.exists(p('data', f)), 'exists', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1, the closing a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''),
        'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '4')
    add('ferry', 'the 590 s guard and the four parts (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''),
        'data/b684_rules.txt :5', '4')
    for b in ('b686_readfirst.txt', 'b686_rules.txt', 'b686_tool_repairs.txt', 'b686_correspondence_diff.txt', 'b686_cut.txt'):
        sz = b == 'b686_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b686_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b686_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b686 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b686_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b686_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b686_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b686_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b686."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b686'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b686')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b686)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b686_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
