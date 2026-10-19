# -*- coding: utf-8 -*-
"""b691_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b691's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (2c300355, continued from b689 and b690); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed
### at b691.
### Routes: `check` -> data/b691_citation_check.txt (.json) ; `ferry` -> data/b691_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b691 from b690_citation.py's form; this tool writes only the banks named above.
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
import b691_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
EF = 'D:/SIDE-explicit-formula'
LV = 'D:/SIDE-lv-conservation'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def peel(repo, tag):
    return g(repo, 'rev-parse', '--short', '%s^{commit}' % tag)[1].strip()


def jload(n):
    try:
        return json.load(open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    r3 = rd(p('data', 'b690_reading3.txt')) or ''
    # ### the ferry's read-first list
    for f in ('data/b690_closing.txt', 'data/b690_defects.txt', 'data/b690_reading3.txt', 'data/b690_rules.txt', 'data/b690_circuit_spec.txt',
              'data/b690_arm_seconds.txt', 'data/b690_arms_prerun_standing-b.txt', 'data/b670_licensed_table.txt',
              'data/b647_table_SIDE-archimedean.txt', 'data/b647_table_SIDE-rcurve.txt', 'data/b674_rules.txt', 'data/b683_arms_sort.txt',
              'tools/rule_arms.py', 'tools/correspondence_gen.py', 'data/b688_correspondence_dry.txt', 'data/b688_correspondence_dry_2.txt',
              'data/b690_closing_push_out.txt', 'data/b690_r3_orders.json'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'b690`s rules bank, three rows', re.findall(r'^  \((\d)\) ', rd(p('data', 'b690_rules.txt')) or '', re.M) == ['1', '2', '3'],
        'data/b690_rules.txt :6, :9, :13', '4')
    add('ferry read-first', 'the circuit spec, nine rows', len(re.findall(r'^  [A-Z-]+\s+reads: ', rd(p('data', 'b690_circuit_spec.txt')) or '', re.M)) == 9,
        'data/b690_circuit_spec.txt', '0')
    add('ferry read-first', 'the tie-break rule by line', (line(p('data', 'b674_rules.txt'), 8) or '').startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'),
        'data/b674_rules.txt :8-:11', '2')
    add('ferry read-first', 'the sort rule in its own words, by line', 'TRACEABLE -- its breach leaves a trace' in (line(p('data', 'b683_arms_sort.txt'), 7) or ''),
        'data/b683_arms_sort.txt :3-:8', '4')
    add('ferry read-first', 'the carried-at dry cell', 'NEW SIDE-li-map = 9e02bc0 (carried at lv-conservation v0.7.0)' in (line(p('data', 'b688_correspondence_dry.txt'), 12) or ''),
        'data/b688_correspondence_dry.txt :12 (the file`s :298, the generator`s :302)', '3')
    add('ferry read-first', 'W-ORD-CORRESPONDENCE-CARRIED-AT at OPEN_TRAILS :14922', 'W-ORD-CORRESPONDENCE-CARRIED-AT' in (line(OT, 14922) or '')
        and 'at the latest the next re-cut act' in (line(OT, 14922) or ''), (line(OT, 14922) or '')[:70], '3')
    oj = jload('b690_r3_orders.json')
    add('ferry read-first; ruling (5)', 'the 35 stale orders as reading 3 lists them', oj.get('unsteady') == 35 and len(oj.get('unsteady_names') or []) == 35,
        'data/b690_r3_orders.json (unsteady, unsteady_names)', '4')
    # ### (R301)(1): b690 at its weight
    head = (rd(p('data', 'b690_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b690_closing.txt :1', head == ('b690 closed: relay 55e34098, PLACE-papers 64936ae; suite 114 of 114; root '
                                                                                   '422989da790bc2ed\u2026; 2 prompts answered; 7 defects'), head[:120], '1')
    po = rd(p('data', 'b690_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay 9fc2c81b read back', '55e34098..9fc2c81b' in po and 'read back at the remote: 9fc2c81b' in po,
        'data/b690_closing_push_out.txt', '0-1')
    for nd, what in (('345 ROWS OUTSIDE LICENSED OR CITED (b680 361)', '345 against 361'), ('57 BEHIND (b680 55)', 'Correspondence 57 against 55'), ('ORDERS 165, OPEN 38', 'orders 165, 38 open'),
                     ('LAG MEDIAN 105 (b680 96)', 'lag median 105 against 96'), ('RESIDUES 7, CARRIED 3', 'residues 7, 3 carried'),
                     ('RULES 21 WITH ARMS 13', 'rules 21, 13 with an arm'), ('THE PAIR RULE 1 OF 4', 'the pair rule 1 of 4'),
                     ('2 STILL\n### READING STATED', 'P3 at 3 lines, 2 still reading stated')):
        add('ruling (1)', what, nd in r3, 'data/b690_reading3.txt, its verdict', '1')
    add('ruling (1)', 'the b680 NO TAG rows read BEHIND now', "b680's two NO TAG rows" in r3, 'data/b690_reading3.txt row (3)', '1')
    add('ruling (1)', 'orders 35 open, older than ten acts, no trigger', '| 35 (b670' in r3, 'data/b690_reading3.txt row (9)', '1')
    add('ruling (1)', 'the two traceable rules, live trace, no arm', 'TRACEABLE, LIVE and without an arm 2 (b680 row 1, b685 row 1' in r3,
        'data/b690_reading3.txt row (13)', '1')
    add('ruling (1); (4)', 'EpsteinQ0.lean :106 and :110-:111 stated', 'Schema/EpsteinQ0.lean :106' in r3 and ':110-:111' in r3, 'data/b690_reading3.txt row (16)', '1')
    add('ruling (1); (7)', 'the header`s tag v0.26 = 82550e4', 'v0.26 = `82550e4`' in (line(os.path.join(PP, K.FACES_PAGE), 3) or ''),
        'the faces page :3', '1')
    add('ruling (1)', 'W-ORD-CIRCUIT-READING at OPEN_TRAILS :14980', 'W-ORD-CIRCUIT-READING' in (line(OT, 14980) or ''), 'OPEN_TRAILS :14980', '1')
    for f in ('b690_checks.txt', 'b690_checks_postpush.txt'):
        add('ruling (1)', 'suite 114 of 114 (%s)' % f, 'ARMS RUN : 114. ### LIVE PASSING : 114. ### LIVE FAILING : 0' in (rd(p('data', f)) or ''),
            'data/%s' % f, '1')
    add('ruling (1)', 'the pre-run`s standing-b part at 463 s', '### PART standing-b : ARMS 2 ; 463 s' in (rd(p('data', 'b690_arms_prerun.txt')) or ''),
        'data/b690_arms_prerun.txt', '1')
    add('ruling (1)', 'the act-root chain 340-390 s', 'the act-root chain 387' in (rd(p('data', 'b690_arms_prerun_standing-b.txt')) or '')
        and 'the act-root chain 342' in (rd(p('data', 'b690_checks_standing-b.txt')) or ''), 'the standing-b banks` phase lines', '1')
    sc = jload('b690_scores_close.json')
    add('ruling (1)', 'all eight scores HELD', sc and all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')),
        'data/b690_scores_close.json', '1')
    add('ruling (1)', 'root 422989da', any(r[1].startswith('422989da790bc2ed') for r in act_root_line('b690')), 'data/act_roots.txt', '1')
    add('ruling (1)', 'the b690 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b690.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b690_mirror_verify.txt')) or '')
        and 'Act root: b690 422989da' in (rd(p('data', 'b690_mirror.txt')) or ''), 'the zip; data/b690_mirror_verify.txt; data/b690_mirror.txt', '1')
    dl = rd(p('data', 'b690_defects.txt')) or ''
    add('ruling (1)', 'seven defects, (e) and (f) the navigator`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'SEAT'), ('b', 'SEAT'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'NAVIGATOR'), ('f', 'NAVIGATOR'), ('g', 'SEAT')], 'data/b690_defects.txt', '1')
    # ### (R301)(2): the re-cut
    lt = rd(p('data', 'b670_licensed_table.txt')) or ''
    add('ruling (2)', 'SIDE-archimedean and SIDE-rcurve tied at 2', 'SIDE-archimedean docstrings (read at 8019d9d)                     2 ->    2' in lt
        and 'SIDE-rcurve docstrings (read at d5f33b4)                          2 ->    2' in lt, 'data/b670_licensed_table.txt :100, :113', '2')
    add('ruling (2)', 'b690`s rule (2), the quotation search', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '2')
    add('ruling (2)', 'the two SIDE-li-map residues by line', 'PrimeLedgerPositivity.lean :29-:31' in (line(p('data', 'b688_cut.txt'), 60) or '')
        and 'PrimeLedgerPositivity.lean :51-:54' in (line(p('data', 'b688_cut.txt'), 64) or ''), 'data/b688_cut.txt :60, :64', '2')
    add('ruling (2)', 'b676`s form (the trivium cut bank)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    for k in ('SIDE-archimedean', 'SIDE-rcurve'):
        add('ruling (2)', '%s cloned at D:/' % k, os.path.isdir('D:/%s/.git' % k), 'D:/%s' % k, '2')
    # ### (R301)(3): the generator
    add('ruling (3)', 'RegisterPentagon.lean :44, :157, :241 at lv-conservation v0.7.0 carry 73cee42', all(
        '73cee42' in (g(LV, 'show', 'v0.7.0:SIDELvConservation/RegisterPentagon.lean')[1].split(NL) + [''] * 250)[n - 1] for n in (44, 157, 241)),
        'git show v0.7.0:SIDELvConservation/RegisterPentagon.lean', '3')
    add('ruling (3)', 'the five cells held at b688', 'WRITTEN 0 ; HELD 5' in (rd(p('data', 'b688_correspondence_dry_2.txt')) or ''),
        'data/b688_correspondence_dry_2.txt', '3')
    add('ruling (3)', 'the generator`s claim 0 against reading 3`s 57', 'AT THE GENERATOR`S CLAIM 0' in (rd(p('data', 'b690_r3_corr.txt')) or '')
        and 'BEHIND BY b670`S METHOD 57' in (rd(p('data', 'b690_r3_corr.txt')) or ''), 'data/b690_r3_corr.txt verdict', '3')
    # ### (R301)(4): the Epstein docstrings
    eq = g(EF, 'show', 'main:SIDEExplicitFormula/Schema/EpsteinQ0.lean')[1].split(NL) + [''] * 120
    add('ruling (4)', 'EpsteinQ0.lean :106 (P3) stated, not proved', '(P3) THE LOCAL COUNT WITH A NUMBER** -- stated, not proved; open.' in eq[105],
        'SIDE-explicit-formula main:SIDEExplicitFormula/Schema/EpsteinQ0.lean :106', '4')
    add('ruling (4)', 'EpsteinQ0.lean :110-:111 (the Q0 premises)', '(P1)-(P3) and (P4)' in eq[109] and 'stated, not proved; open.' in eq[110],
        'EpsteinQ0.lean :110-:111', '4')
    add('ruling (4)', 'P3`s status since b687', 'P3: DERIVED' in (rd(p('data', 'b687_p3_status.txt')) or ''), 'data/b687_p3_status.txt :35', '4')
    add('ruling (4); (12)', 'W-ORD-EPSTEIN-COUNT-LEAN at OPEN_TRAILS :14892', 'W-ORD-EPSTEIN-COUNT-LEAN' in (line(OT, 14892) or ''), (line(OT, 14892) or '')[:60], '4')
    # ### (R301)(6)-(8)
    add('ruling (6)', 'the defect (g) case, b690`s methods bank', 'rows 12, READY 9' in (rd(p('data', 'b690_checks_standing-a.txt')) or ''),
        'data/b690_checks_standing-a.txt (G-RULE-METHOD-READINESS)', '4')
    add('ruling (7)', 'the generator`s source for the tag (chain_page.py node_pin)', 'def node_pin(path):' in (line(p('tools', 'chain_page.py'), 87) or ''),
        'tools/chain_page.py :87-:96', '4')
    sb = jload('b690_arm_seconds.json')
    add('ruling (8)', 'the b690 seconds bank, standing-b`s arms', sorted(r['arm'] for r in sb.get('rows') or [] if r['part'] == 'standing-b')
        == ['G-ACTROOT-VERIFY', 'G-SHARED-ADDITIVE'], 'data/b690_arm_seconds.json (standing-b: two arms)', '5')
    # ### (R301)(9): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (9)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (9)', 'data/b690_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b690_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    add('ruling (11)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b690_worklist.py')) or ''), 'tools/b690_worklist.py', '5')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry', 'the split rule (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C6', 'rule (1) of data/b690_rules.txt, binding from b691', 'Binds from b691.' in (rd(p('data', 'b690_rules.txt')) or ''), 'data/b690_rules.txt :5-:7', '6')
    for b in ('b691_readfirst.txt', 'b691_cut.txt', 'b691_behind.txt', 'b691_orders_triage.txt', 'b691_tool_repairs.txt'):
        sz = b == 'b691_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b691_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b691_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b691 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b691_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b691_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b691_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b691_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b691."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b691'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b691')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b691)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b691_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
