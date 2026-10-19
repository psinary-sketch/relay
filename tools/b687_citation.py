# -*- coding: utf-8 -*-
"""b687_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b687's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (a90bcdb6); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b687; the rows and the
### banks are b687's.
### Routes: `check` -> data/b687_citation_check.txt (.json) ; `ferry` -> data/b687_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b687 from b686_citation.py's form; this tool writes only the banks named above.
"""
import gzip
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
import b687_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID   # ### this act's session (b677's names df03c73f)
NL = chr(10)
PP, KE, TD = C.PP, C.KE, C.TD
C.ANCHOR, C.TAIL = 'RULING (R297) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
SP = 'D:/SIDE-spinor'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b686_closing.txt', 'data/b686_defects.txt', 'data/b685_count_plan.txt', 'data/b685_count.txt', 'data/b685_count_controls.txt',
              'data/b685_search.txt', 'data/b685_p3.txt', 'data/b685_count_part1.json', 'data/b685_count_part2.json', 'data/b685_count_part4.json',
              'tools/b685_count.py', 'data/b681_epstein_zeros_narrowed.json.gz', 'data/b681_epstein_zeros_narrowed_hashes.txt',
              'data/b681_narrow_controls.txt', 'data/b670_work_orders.txt', 'tools/rule_arms.py', 'data/b686_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    ra = rd(p('tools', 'rule_arms.py')) or ''
    ck = rd(p('tools', 'b686_checks.py')) or ''
    add('ferry read-first', 'tools/rule_arms.py (G-EDIT-ROUTE by line)', 'G-EDIT-ROUTE' in ra,
        'tools/rule_arms.py carries no G-EDIT-ROUTE (%d occurrences); the arm is at tools/b686_checks.py :1045 (%s), its reader tools/edit_route.py'
        % (ra.count('G-EDIT-ROUTE'), "('G-EDIT-ROUTE'" in (line(p('tools', 'b686_checks.py'), 1045) or '')), '1')
    # ### (R297)(1): b686 at its weight
    head = (rd(p('data', 'b686_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b686_closing.txt :1', head == ('b686 closed: relay b0249275, PLACE-papers 9b9a7c6; suite 110 of 110; root '
                                                                                   'c51755eea1318579\u2026; 1 prompt answered; 2 defects'), head[:120], '1')
    po = rd(p('data', 'b686_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay 3e547498 read back', 'b0249275..3e547498' in po and 'read back at the remote: 3e547498' in po,
        'data/b686_closing_push_out.txt', '0-1')
    for repo, nm, sha_, needle in ((ROOT, 'relay', 'b0249275', 'b686 record'), (ROOT, 'relay', '3e547498', 'b686 closing'),
                                   (PP, 'PLACE-papers', '9b9a7c6', 'b686 record'), (PP, 'PLACE-papers', 'f5111a2', 'b686')):
        s = subject(repo, sha_)
        add('ruling (1)', '%s %s' % (nm, sha_), commit_in(repo, sha_) and s.startswith(needle), s[:80], '1')
    add('ruling (1)', 'the citation check 72 of 72', '**CITES CHECKED 72 ; OK 72 ; MISSES 0.**' in (rd(p('data', 'b686_citation_check.txt')) or ''),
        'data/b686_citation_check.txt (its last line)', '1')
    l9258 = line(FIND, 9258) or ''
    add('ruling (1)', 'b685`s weight line at FINDINGS :9258 with its head line quoted', 'by b686 to b685' in l9258 and 'b685 closed: relay ea8e7f49' in l9258,
        l9258[:70], '1')
    sc = json.load(open(p('data', 'b686_scores_close.json'), encoding='utf-8'))
    add('ruling (1)', 'N4 and S2 read at the close into data/b686_scores_close.json; all eight HELD', all(sc[k][0] == 'HELD' for k in
        ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), 'data/b686_scores_close.json', '1')
    add('ruling (1)', 'the rule at data/b686_rules.txt row (1)', "(1) A SCORER READS BANKS AND NOT THE ENTRY" in (line(p('data', 'b686_rules.txt'), 5) or ''),
        'data/b686_rules.txt :5', '1')
    add('ruling (1)', 'the diff in data/b686_tool_repairs.txt', os.path.exists(p('data', 'b686_tool_repairs.txt')), 'exists', '1')
    fl = [line(os.path.join(PP, 'phase1.5', 'structural', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'), n) or '' for n in (628, 629, 630)]
    add('ruling (1)', 'the three FOUNDATIONS cells at v0.2.2', all('SIDE-silence-principle v0.2.2' in x for x in fl), 'FOUNDATIONS_v0_2_5 :628-:630', '1')
    add('ruling (1)', 'the distance 55 by b670`s method and 0 at the generator`s claim', 'AFTER: BEHIND BY b670`S METHOD 55 AGAINST b682`S 55 ; AT THE '
        'GENERATOR`S CLAIM 0 AGAINST b682`S 0' in (line(p('data', 'b686_correspondence_after.txt'), 12) or ''), 'data/b686_correspondence_after.txt :12', '1')
    add('ruling (1)', 'SIDE-spinor named at 3 by the larger table, 15 rows against SIDE-li-map`s 13', 'SIDE-li-map 3 (rows 13), SIDE-spinor 3 (rows 15)'
        in (line(p('data', 'b686_naming.txt'), 57) or ''), 'data/b686_naming.txt :57', '1')
    mg = g(SP, 'rev-parse', '--short', 'v0.1.1^{commit}')[1].strip()
    add('ruling (1)', 'SIDE-spinor merged at aca59d1, tagged v0.1.1', mg.startswith('aca59d1'), 'v0.1.1 -> %s' % mg, '1')
    pr = rd(p('data', 'b686_prints_SIDE-spinor.txt')) or ''
    add('ruling (1)', 'both builds DERIVES, 15 prints equal line for line', 'PRINTS BEFORE 15 LINES ; AFTER 15 LINES ; DIFFERING 0 ; EQUAL LINE FOR LINE True' in
        (rd(p('data', 'b686_closing.txt')) or '') and bool(pr), 'data/b686_closing.txt (the prints line); data/b686_prints_SIDE-spinor.txt', '1')
    sl = g(SP, 'show', 'v0.1.1:SIDESpinor/SpinorLeg.lean')[1].split(NL)   # ### the ruling names the file without its folder
    add('ruling (1)', 'SpinorLeg.lean :21 “(salt-checked)” carried as R4', len(sl) > 20 and '(salt-checked)' in sl[20], (sl[20] if len(sl) > 20 else '')[:80], '1')
    for f in ('b686_checks.txt', 'b686_checks_postpush.txt'):
        add('ruling (1)', 'suite 110 of 110 (%s)' % f, 'ARMS RUN : 110. ### LIVE PASSING : 110. ### LIVE FAILING : 0 .' in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    add('ruling (1)', '89 standing, 21 over the act`s banks', len(C.__dict__) > 0 and 'ACT_ARMS' in (rd(p('tools', 'b686_worklist.py')) or '')
        and (rd(p('tools', 'b686_worklist.py')) or '').count("'G-") == 21, 'tools/b686_worklist.py ACT_ARMS 21', '1')
    add('ruling (1)', 'root c51755ee in the chain', any(r[1].startswith('c51755eea1318579') for r in act_root_line('b686')), 'data/act_roots.txt :64', '1')
    add('ruling (1)', 'over 57 banks', 'BANKS 57 ; CLEAN AND EQUAL AT HEAD 57' in (rd(p('data', 'b686_closing.txt')) or ''), 'data/b686_closing.txt (the root`s banks line)', '1')
    add('ruling (1)', 'the b686 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-18-b686.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b686_mirror_verify.txt')) or '')
        and 'Act root: b686 c51755ee' in (rd(p('data', 'b686_mirror.txt')) or ''), 'the zip; data/b686_mirror_verify.txt; data/b686_mirror.txt', '1')
    dl = rd(p('data', 'b686_defects.txt')) or ''
    add('ruling (1)', 'two defects, both the seat`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [('a', 'SEAT'), ('b', 'SEAT')],
        'data/b686_defects.txt :5-:16', '1')
    add('ruling (1)', '(a) 4 against the live 13; (b) a combine piped into sed', '"differs in 4 lines"' in dl and 'differ in 13 lines' in dl and '`sed -n 0p`' in dl,
        'data/b686_defects.txt :6-:8, :14', '1')
    # ### (R297)(2): the object
    cnt = rd(p('data', 'b685_count.txt')) or ''
    add('ruling (2)', 'a = 0.432572, c = 1.262442 for T ≥ 149', 'a = 0.432571915432 ± 4.33e-41' in (line(p('data', 'b685_count.txt'), 21) or '')
        and 'c = 1.26244217716 ± 1.26e-40' in (line(p('data', 'b685_count.txt'), 23) or ''), 'data/b685_count.txt :21, :23', '2-3')
    ctl3 = line(p('data', 'b685_count_controls.txt'), 3) or ''
    add('ruling (2)', 'a_ζ = 0.228506, c_ζ = 0.800713 for T ≥ 100', 'a_ζ = 0.228505583833' in ctl3 and 'c_ζ = 0.800713497357' in ctl3, 'data/b685_count_controls.txt :3', '2-3')
    ctl = rd(p('data', 'b685_count_controls.txt')) or ''
    add('ruling (2)', 'contains N(T) − main at T = 100, 1000, 10⁴', ctl.count('CONTAINS True') == 3, 'data/b685_count_controls.txt :4-:6', '2-3')
    add('ruling (2)', 'sharper at those heights than HSW Cor 1.2', ctl.count('NOT SHARPER False') == 3, 'data/b685_count_controls.txt :4-:6 (the (Z1) value alone)', '2-3')
    add('ruling (2)', '... than Trudgian 2014 and Backlund`s row at those heights', 'Trudgian' in ctl and ctl.count('NOT SHARPER False') > 3,
        'the controls bank compares each height with (Z1) alone (Trudgian %d times, Backlund`s row named on :3 with T₀ 200, above T = 100); '
        'no comparison with Trudgian 2014 or Backlund`s row is banked at b685' % ctl.count('Trudgian'), '2-3')
    add('ruling (2)', 'P3 “stated, not proved”', 'stated, not proved' in (rd(p('data', 'b685_p3_status.txt')) or ''), 'data/b685_p3_status.txt', '2')
    ot = line(OT, 14832) or ''
    add('ruling (2); ferry', 'W-ORD-EPSTEIN-COUNT`s trigger at OPEN_TRAILS :14832, three readings', '`W-ORD-EPSTEIN-COUNT` (:14678) RE-DATED' in ot
        and '(i) a matched-range comparison' in ot and '(ii) a direct control on the Jensen step' in ot and '(iii) the same for Z_Q at T = 50, 100, 149' in ot,
        ot[:80], '2-3')
    wo = line(p('data', 'b670_work_orders.txt'), 295) or ''
    add('ferry', 'W-ORD-EPSTEIN-COUNT by row in the orders bank', 'W-ORD-EPSTEIN-COUNT' in wo and 'OPEN' in wo and ':14832' in wo, 'data/b670_work_orders.txt :295', '3')
    # ### (R297)(3): the readings' inputs
    plan = rd(p('data', 'b685_count_plan.txt')) or ''
    for n, needle in ((33, '(5) THE TOP EDGE BY BACKLUND'), (55, '(6) THE JENSEN INTEGRAL'), (60, '(7) THE GROWTH BOUND F_{c,r} ON THE CIRCLE')):
        add('ruling (3)', 'data/b685_count_plan.txt step at :%d' % n, needle in (line(p('data', 'b685_count_plan.txt'), n) or ''), needle, '2')
    add('ruling (3)', 'centre c = 1.7, radius r = 2.05', 'c = 1.7, r = 2.05' in (line(p('data', 'b685_count.txt'), 8) or ''), 'data/b685_count.txt :8', '2')
    add('ruling (3)', 'the inner radius the plan names (c − ½, through ℓ = log(r/(c − ½)))', 'log(r/(c − 1/2))' in plan or 'log(r/(c − ½))' in plan,
        'data/b685_count_plan.txt :36 ("2 log(r/(c − 1/2))"), :72-:73', '2')
    add('ruling (3)', 'the ζ instance`s own parameters (c = 1.5, r = 1.98, η = 0.5), beside the disc`s 1.7 and 2.05', 'c = 1.5, r = 1.98, η = 0.5' in ctl3,
        'data/b685_count_controls.txt :3', '2')
    add('ruling (3)', 'the C1 form of b681 (acb.zeta_zero against a narrowed ball)', 'contains acb.zeta_zero(1) True' in (line(p('data', 'b681_narrow_controls.txt'), 3) or ''),
        'data/b681_narrow_controls.txt :3-:12', '2')
    hs = rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''
    gz = p('data', 'b681_epstein_zeros_narrowed.json.gz')
    inner = hashlib.sha256(gzip.open(gz).read()).hexdigest()
    add('ruling (3)', 'b681`s balls through its hashes bank (the .gz and the JSON inside)', sha(gz) in hs and inner in hs, 'data/b681_epstein_zeros_narrowed_hashes.txt :2-:3', '2')
    j = json.load(gzip.open(gz))
    add('ruling (3)', 'b681`s rows are points with balls (163: ON 146, OFF 17, h 1e-30)', len(j['rows']) == 163 and sum(r['kind'] == 'OFF' for r in j['rows']) == 17
        and j['w'] == '1e-30', 'the .gz rows', '2')
    for f in ('b675_hypotheses.txt', 'b679_q0_membership.txt', 'b683_landing.txt'):
        add('ruling (5)', 'the Q0 results to re-read: data/%s' % f, os.path.exists(p('data', f)), 'exists', '3')
    # ### (R297)(6): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (6)', 'SIDE-spinor recut-spinor-b686 at the remote', bool(g(SP, 'ls-remote', '--heads', 'origin', 'recut-spinor-b686')[1].strip()),
        'git ls-remote --heads origin recut-spinor-b686', '0')
    add('ruling (6)', 'data/b686_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b686_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R297)(8) and the ferry's standing cites
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b686_worklist.py')) or ''), 'tools/b686_worklist.py', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1, the closing a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''),
        'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '4')
    add('ferry', 'the 590 s guard and the four parts (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''),
        'data/b684_rules.txt :5', '4')
    add('ferry C4', 'the score routes in the order b686 fixed (data/b686_rules.txt row (1))', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''),
        'data/b686_rules.txt :7-:8', '4')
    add('ferry', 'b673`s capture form (tools/b686_closing.py`s push captures)', os.path.exists(p('data', 'b686_relay_root_push_out.txt')), 'data/b686_relay_root_push_out.txt', '5')
    for b in ('b687_readfirst.txt', 'b687_plan.txt', 'b687_matched.txt', 'b687_jensen_zeta.txt', 'b687_jensen_q0.txt', 'b687_steps.txt', 'b687_controls.txt',
              'b687_p3_status.txt', 'b687_q0_reread.txt', 'b687_tool_repairs.txt'):
        sz = b == 'b687_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b687_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b687_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b687 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b687_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b687_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b687_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b687_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b687."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b687'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b687')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b687)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b687_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
