# -*- coding: utf-8 -*-
"""b683_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b683's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling; the answer route is
### b682's, imported from tools/b682_citation.py with its act names pointed at b683; the rows and the banks are b683's.
### Routes: `check` -> data/b683_citation_check.txt (.json) ; `ferry` -> data/b683_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b683 from b682_citation.py's form; this tool writes only the banks named above.
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

NL = chr(10)
PP, KE, TD = C.PP, C.KE, C.TD
C.ANCHOR, C.TAIL = 'RULING (R293) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection', 'D:/SIDE-window', 'D:/SIDE-trivium')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
B681_BANK = 'b681_epstein_zeros_narrowed.json.gz'


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
    for f in ('data/b682_closing.txt', 'data/b682_defects.txt', 'data/b682_rules.txt', 'data/b680_rules_arms.txt', 'data/b680_arms.txt',
              'data/b677_map_plan.txt', 'data/b677_map.txt', 'data/b677_map_h.txt', 'data/b677_tolerance.txt', 'data/b677_defects.txt',
              'tools/b677_epstein_map_angle.py', 'data/b671_tie_diagnostic.txt', 'data/b663_epstein_plan.txt', 'data/b667_epstein_plan.txt',
              'data/' + B681_BANK, 'data/b681_epstein_zeros_narrowed_hashes.txt', 'data/b681_narrow.txt', 'data/b670_work_orders.txt',
              'tools/b682_checks.py', 'data/b675_rules.txt', 'data/b682_closing_push_out.txt', 'tools/b667_epstein_map_balls.py',
              'data/b678_rules.txt', 'data/b680_rules.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    # ### (R293)(1): b682 at its weight
    head = (rd(p('data', 'b682_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line at data/b682_closing.txt :1', head == ('b682 closed: relay d62f7192, PLACE-papers dc5613b; suite 89 of 90; root '
                                                                         '4882d95a927d5417\u2026; 2 prompts answered; 5 defects'), head[:110], '1')
    po = rd(p('data', 'b682_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay fbc1053a', 'd62f7192..fbc1053a' in po and 'read back at the remote: fbc1053a' in po,
        'data/b682_closing_push_out.txt', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'd62f7192', 'b682 record'), (ROOT, 'relay', 'fbc1053a', 'b682 closing'),
                                  (ROOT, 'relay', '60e8de3e', ''), (PP, 'PLACE-papers', 'dc5613b', 'b682 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    add('ruling (1)', 'the generator committed alone at 60e8de3e', g(ROOT, 'show', '--name-only', '--format=', '60e8de3e')[1].split() == ['tools/correspondence_gen.py'],
        'git show --name-only 60e8de3e', '1')
    add('ruling (1)', 'five planted cases as wanted', 'PLANTED CASES 5 ; AS WANTED 5 ; PASS' in (rd(p('data', 'b682_gen_test.txt')) or ''), 'data/b682_gen_test.txt', '1')
    fl = [line(os.path.join(PP, 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'), n) or '' for n in (628, 629, 630)]
    add('ruling (1)', 'FOUNDATIONS :628-:630 SIDE-silence-principle v0.2.1, axiom-free (none) at :628 and :629',
        all('SIDE-silence-principle v0.2.1' in x for x in fl) and all('axiom-free (none)' in x for x in fl[:2]), 'the three rows', '1')
    cb = rd(p('data', 'b682_correspondence_after.txt')) or ''
    add('ruling (1)', 'the distance 55 and 0 after', '55' in cb and bool(cb), 'data/b682_correspondence_after.txt', '1')
    add('ruling (1)', 'the partner table differing in 13 lines', '13' in (rd(p('data', 'b682_correspondence_diff.txt')) or ''), 'data/b682_correspondence_diff.txt', '1')
    for n, needle in ((14742, 'THE AUTHOR’S WORD'), (14744, 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'), (14746, '### b682'), (14714, 'W-ORD-MAP-ANGLE-FORM'),
                      (14694, 'rules without arms 24')):
        lt = line(OT, n) or ''
        add('ruling (1)-(2)', 'OPEN_TRAILS :%d' % n, needle in lt, lt[:70], '1-3')
    add('ruling (1)', 'DISCHARGED at OPEN_TRAILS :14744', 'DISCHARGED' in (line(OT, 14744) or ''), 'the line', '1')
    for n, needle in ((9138, 'b681'), (9140, '## The Correspondence reader')):
        lt = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in lt, lt[:70], '1')
    cut = rd(p('data', 'b682_cut.txt')) or ''
    add('ruling (1)', 'SIDE-bijection tagged v0.2.1, 4 to 0', 'v0.2.1' in cut and 'SIDE-bijection' in cut, 'data/b682_cut.txt', '1')
    add('ruling (1)', 'SIDE-bijection v0.2.1 a tag at the kernel', g('D:/SIDE-bijection', 'rev-parse', '--verify', '-q', 'v0.2.1')[0] == 0, 'git rev-parse v0.2.1', '1')
    add('ruling (1)', '15 prints equal line for line', '15' in (rd(p('data', 'b682_prints_compare.txt')) or ''), 'data/b682_prints_compare.txt', '1')
    add('ruling (1)', 'the author`s word at data/b682_rules.txt row (1)', 'arms for the traceable ones, the seat sorts them' in (rd(p('data', 'b682_rules.txt')) or ''),
        'data/b682_rules.txt :5', '1, 4')
    dl = rd(p('data', 'b682_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'five defects (a)-(e)', [x[0] for x in letters] == list('abcde'), 'data/b682_defects.txt :5-:32 (%s)' % letters, '1')
    add('ruling (1)', 'the ruling`s list of the defects names (a)-(c) of the five', True, 'the ruling quotes three of five; (d) the naming route`s timeout and '
        '(e) the sed command stand in the bank (the latter named in the ruling`s next sentence)', '1')
    add('ruling (1)', 'root 4882d95a chained from b681`s', any(r[1].startswith('4882d95a') for r in act_root_line('b682')), 'data/act_roots.txt', '1')
    mz = 'D:/MY-DOwnloads/mirror-refresh-2026-10-18-b682.zip'
    add('ruling (1)', 'the b682 mirror made: %s' % mz, os.path.exists(mz) and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b682_mirror_verify.txt')) or ''),
        'the zip and data/b682_mirror_verify.txt', '0')
    add('ruling (1)', 'G-EDIT-ROUTE reads `sed -i` alone (tools/edit_route.py :6, :145-:150)', '(S) any `sed -i`' in (line(p('tools', 'edit_route.py'), 6) or ''),
        'tools/edit_route.py :6', '5')
    # ### (R293)(2)-(4): the object, the plan, the run
    tl = line(p('data', 'b677_tolerance.txt'), 90) or ''
    add('ruling (2)', 'h_tol(64) = 3.162e-28 at data/b677_tolerance.txt :90', 'h_tol(64) 3.162e-28' in tl, tl[:90], '2')
    add('ruling (2)', 'b677`s price 1.3e-4 to 7.7e-2 against the bar 9.5e-7', '7.7e-2 (upper) to 1.3e-4 (lower), against the bar 2^-20 = 9.54e-7'
        in (line(p('data', 'b677_map_plan.txt'), 76) or ''), 'data/b677_map_plan.txt :76 (section 6)', '2')
    add('ruling (2)', 'controls passing to j ≈ 47-56 as priced', 'the last passing j:  47 (upper) to 56 (lower)' in (line(p('data', 'b677_map_plan.txt'), 77) or ''),
        'data/b677_map_plan.txt :77', '2')
    mh = rd(p('data', 'b677_map_h.txt')) or ''
    add('ruling (2)', 'H1 and H2 failed at b677', 'H1 REFUTED ; H2 REFUTED' in mh, 'data/b677_map_h.txt :12', '2')
    add('ruling (2)', 'the 163 points narrowed to 1e-30', 'NARROWED TO 1e-30 163 OF 163' in (rd(p('data', 'b681_narrow.txt')) or ''), 'data/b681_narrow.txt (the verdict)', '2')
    hb = rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ruling (2)-(3)', 'the b681 bank with its hashes bank, the chain from b671`s', 'f6613564e9d7fcd5' in hb and '51d9e6322510b738' in hb,
        'data/b681_epstein_zeros_narrowed_hashes.txt :2-:4', '2')
    ob = rd(p('data', 'b670_work_orders.txt')) or ''
    add('ruling (2)', 'W-ORD-MAP-ANGLE-FORM`s row in the orders bank, OPEN at :14714',
        'W-ORD-MAP-ANGLE-FORM                         :14398  b671   10    OPEN             :14714' in ob, 'data/b670_work_orders.txt :286', '2-3')
    for f, n, needle in (('data/b677_map_plan.txt', 17, '== 2. THE MAP'), ('data/b677_map_plan.txt', 68, '== 6. THE PRICE'),
                         ('data/b677_map_plan.txt', 60, '== 5. THE TIES'), ('data/b677_map_plan.txt', 106, '== 8. THE HYPOTHESES')):
        lt = line(p(*f.split('/')), n) or ''
        add('ruling (3)', '%s :%d section' % (f, n), needle in lt, lt[:60], '2')
    add('ruling (3)', 'the 123 control rows of b677', 'ROWS 123 (the b671 list: 41 + 41 + 41) ; NONE DROPPED True' in (rd(p('data', 'b677_map.txt')) or ''),
        'data/b677_map.txt (its last line)', '2-3')
    td = rd(p('data', 'b671_tie_diagnostic.txt')) or ''
    add('ruling (3); N3', 'b671`s list of controls: 123 rows', len(re.findall(r'^  (THE CONTROL Z₁\(0\.8, 29\.6\)|Q0 AT qE0)\s+\d+ j \d+ : ', td, re.M)) == 123,
        'data/b671_tie_diagnostic.txt :7-:129', '3')
    add('ruling (4)', 'the b671 diagnostic`s rule', 'the words (the navigator`s answer on the two readings' in (line(p('data', 'b671_tie_diagnostic.txt'), 5) or ''),
        'data/b671_tie_diagnostic.txt :5', '3')
    h3 = line(p('data', 'b663_epstein_plan.txt'), 131) or ''
    add('ruling (3)', 'H3 at data/b663_epstein_plan.txt :131', 'every hypothesis of zeroSide_neg_at_rate_cfg certifies by name and hrate holds at some j₀ ≤ D + 40' in h3,
        h3.strip()[:90], '2')
    h4 = (line(p('data', 'b667_epstein_plan.txt'), 124) or '') + (line(p('data', 'b667_epstein_plan.txt'), 125) or '')
    add('ruling (3)', 'H4 at data/b667_epstein_plan.txt :124-:125', 'H4' in h4 and 'prints j₀ = 38 and a zero side below zero' in h4, h4.strip()[:90], '2')
    tool = rd(p('tools', 'b677_epstein_map_angle.py')) or ''
    add('ruling (3)', 'the tool: b677`s map, its routes and its bank name', "Q0_CERT = 'b671_epstein_zeros_narrowed.json'" in tool and 'def part1(' in tool,
        'tools/b677_epstein_map_angle.py :38, :589', '2-3')
    add('ruling (4)', 'H5`s instrument-side row of b677 (coeffs_exist and the orbit identity)', 'THE LABELLED READING' in mh and 'j₀ = 38' in mh,
        'data/b677_map_h.txt :9', '3')
    add('ruling (4)', 'hQtie of 41 (J_max - D + 1)', 'hQtie controls 29 of 41' in mh, 'data/b677_map_h.txt :5', '3')
    # ### (R293)(6): the arms
    ra = rd(p('data', 'b680_rules_arms.txt')) or ''
    add('ruling (6)', 'the 24 rules read NONE', 'NONE 24' in ra and len(re.findall(r'^  b6\d\d row \d+ -- ', ra, re.M)) == 24, 'data/b680_rules_arms.txt :32-:58', '4')
    add('ruling (6)', 'the arm form: STANDING in the sealed checks tool', 'STANDING = sorted(set(g2_of(B681_FACE)) - set(B681_ACT_ARMS))' in (line(p('tools', 'b682_checks.py'), 325) or ''),
        'tools/b682_checks.py :325', '4-5')
    add('ruling (6)', 'arms by kind: SHAPE and VALUE', 'SHAPE (a bank`s form, presence or text) or VALUE' in (rd(p('data', 'b680_arms.txt')) or ''), 'data/b680_arms.txt :4-:5', '4')
    # ### (R293)(7): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b682-root', 'push-b682', 'push-b682-closing')), (PP, 'PLACE-papers', ('push-b682-root', 'push-b682')),
                         ('D:/SIDE-bijection', 'SIDE-bijection', ('push-b682-main', 'push-b682-merge', 'recut-bijection-b682'))):
        for b in bs:
            add('ruling (7)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    rr = g('D:/SIDE-bijection', 'ls-remote', '--heads', 'origin', 'recut-bijection-b682')
    add('ruling (7)', 'SIDE-bijection recut-bijection-b682 at the remote', rr[0] == 0 and 'recut-bijection-b682' in rr[1], 'ls-remote --heads: %s' % rr[1].strip()[:60], '0')
    tip = g('D:/SIDE-bijection', 'rev-parse', 'recut-bijection-b682')[1].strip()
    add('ruling (7)', 'its tip an ancestor of main at v0.2.1', bool(tip) and g('D:/SIDE-bijection', 'merge-base', '--is-ancestor', tip, 'v0.2.1')[0] == 0
        and g('D:/SIDE-bijection', 'merge-base', '--is-ancestor', 'v0.2.1', 'main')[0] == 0, 'tip %s' % tip[:12], '0')
    add('ruling (7)', 'data/b682_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b682_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R293)(8)-(10)
    add('ruling (8)', 'test_asof.py 563 s at b682', '563 s' in dl, 'data/b682_defects.txt :13', '0')
    r2 = line(p('data', 'b675_rules.txt'), 9) or ''
    add('ruling (8)', 'data/b675_rules.txt row 2 (a long phase over 450 s splits the next run)', 'A PRE-RUN\'S LONG PHASE SPLITS THE NEXT ONE' in r2 and '450 s'
        in (rd(p('data', 'b675_rules.txt')) or ''), 'data/b675_rules.txt :9-:11 (a pre-run`s phase; the ruling applies it to the test files)', '0')
    add('ruling (10)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b682_worklist.py')) or '') or "DRAFT = '23228113'" in (rd(p('tools', 'b681_worklist.py')) or ''),
        'tools/b681_worklist.py', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b678_rules.txt row 1, the suite in three parts', '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS' in (line(p('data', 'b678_rules.txt'), 5) or ''),
        'data/b678_rules.txt :5', '5')
    add('ferry C5', 'data/b675_rules.txt row 1, the closing a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''),
        'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '6')
    # ### this act's banks, to be written
    for b in ('b683_readfirst.txt', 'b683_map_plan.txt', 'b683_map.txt', 'b683_map_h.txt', 'b683_arms_sort.txt', 'b683_tool_repairs.txt'):
        sz = b == 'b683_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b683_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b683_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b683 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b683_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b683_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b683_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b683_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b683."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b683'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b683')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b683)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b683_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
