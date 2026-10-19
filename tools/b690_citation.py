# -*- coding: utf-8 -*-
"""b690_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b690's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (2c300355, b689's continued); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b690.
### Routes: `check` -> data/b690_citation_check.txt (.json) ; `ferry` -> data/b690_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b690 from b689_citation.py's form; this tool writes only the banks named above.
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
import b690_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = 'RULING (R300) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
EF = 'D:/SIDE-explicit-formula'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def peel(repo, tag):
    return g(repo, 'rev-parse', '--short', '%s^{commit}' % tag)[1].strip()


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b689_closing.txt', 'data/b689_defects.txt', 'data/b689_faces_rows.txt', 'data/b689_q0_reread.txt', 'data/b680_licensed.txt',
              'data/b680_correspondence.txt', 'data/b680_orders.txt', 'data/b680_methods.txt', 'data/b680_lag.txt', 'data/b680_residues.txt',
              'data/b680_rules_arms.txt', 'data/b683_arms_sort.txt', 'data/b686_cut.txt', 'data/b688_cut.txt', 'tools/b678_corrigendum.py',
              'tools/correspondence_gen.py', 'tools/licensed_table.py', 'tools/b680_readings.py', 'data/b688_nodes_zeta.txt',
              'data/b689_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    for f in ('b674', 'b675', 'b677', 'b678', 'b680', 'b681', 'b682', 'b684', 'b685', 'b686', 'b687', 'b688'):
        add('ferry read-first; ruling (3)', 'the rules bank data/%s_rules.txt' % f, os.path.exists(p('data', '%s_rules.txt' % f)), 'exists', '2')
    add('ferry read-first; ruling (3)', 'no rules bank at b676, b679, b683 or b689 (the census reads b683_rules_arms.txt beside)',
        not any(os.path.exists(p('data', '%s_rules.txt' % a)) for a in ('b676', 'b679', 'b683', 'b689')) and os.path.exists(p('data', 'b683_rules_arms.txt')),
        'absent; data/b683_rules_arms.txt present', '2')
    add('ferry read-first', 'data/b689_defects.txt (e) by line', (line(p('data', 'b689_defects.txt'), K.B689_DEFECT_E) or '').startswith('    (e) THE SEAT'),
        'data/b689_defects.txt :38', '0-1')
    add('ferry read-first; ruling (2)', 'the command by its command-bank line', '#177 |' in (line(p('data', 'b689_commands.txt'), K.B689_CMD_LINE) or '')
        and 'sed -n 3p' in (line(p('data', 'b689_commands.txt'), K.B689_CMD_LINE) or ''), 'data/b689_commands.txt :238 (#177)', '1')
    add('ferry read-first', 'b689`s faces rows by row', (line(p('data', 'b689_faces_rows.txt'), 12) or '').startswith('== THE CURRENT ROW')
        and (line(p('data', 'b689_faces_rows.txt'), 15) or '').startswith('== THE SUCCESSOR ROW'), 'data/b689_faces_rows.txt :12-:13, :15-:16', '2')
    add('ferry read-first', 'the sort rule (TRACEABLE / PROSE)', 'TRACEABLE -- its breach leaves a trace' in (line(p('data', 'b683_arms_sort.txt'), 7) or ''),
        'data/b683_arms_sort.txt :6-:8', '3')
    add('ferry read-first; ruling (3)', 'R3b by line', (line(p('data', 'b686_cut.txt'), 49) or '').startswith('  R3b  SIDESilencePrinciple/Basic.lean:1'),
        'data/b686_cut.txt :49', '2')
    add('ferry read-first; ruling (3)', 'the two SIDE-li-map residues by line', 'PrimeLedgerPositivity.lean :29-:31' in (line(p('data', 'b688_cut.txt'), 60) or '')
        and 'PrimeLedgerPositivity.lean :51-:54' in (line(p('data', 'b688_cut.txt'), 64) or ''), 'data/b688_cut.txt :60, :64', '2')
    add('ferry read-first', 'the faces kernels as the generator`s input names them', (line(os.path.join(PP, K.FACES_PAGE), 3) or '').find('data/b688_nodes_zeta.txt') > 0,
        'the faces page :3 names relay data/b688_nodes_zeta.txt; its rows naming kernels :5, :87, :126, :145, :165, :167', '3')
    ins = os.path.join(PP, 'phase1.5/method/INSTRUMENTS.md')
    add('ferry read-first', 'INSTRUMENTS.md`s entry form', (line(ins, 13) or '').startswith('## I-1 '), 'phase1.5/method/INSTRUMENTS.md :13-:25', '3')
    # ### (R300)(1): b689 at its weight
    head = (rd(p('data', 'b689_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b689_closing.txt :1', head == ('b689 closed: relay c975b150, PLACE-papers a5b86a5; suite 115 of 116; root '
                                                                                   '7b2d6772a03792f6\u2026; 2 prompts answered; 5 defects'), head[:120], '1')
    po = rd(p('data', 'b689_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay c8afcb43 read back', 'c975b150..c8afcb43' in po and 'read back at the remote: c8afcb43' in po,
        'data/b689_closing_push_out.txt', '0-1')
    add('ruling (1)', 'v0.34 peeled 8fbc27b, main at it', peel(EF, 'v0.34') == '8fbc27b' and g(EF, 'rev-parse', '--short', 'main')[1].strip() == '8fbc27b',
        'git -C D:/SIDE-explicit-formula', '1')
    add('ruling (1)', 'run 39255737373, 11 new names DERIVES', 'LANDED 11 OF 11 DERIVES AT THE STANDARD THREE' in (rd(p('data', 'b689_landing.txt')) or ''),
        'data/b689_landing.txt', '1')
    add('ruling (1)', '13 DISCHARGED, 9 RE-PROVED, 0 OBSTRUCTED', 'THE COUNT: 22 of 22 classified ; DISCHARGED 13' in (rd(p('data', 'b689_plan.txt')) or ''),
        'data/b689_plan.txt == 2', '1')
    add('ruling (1)', 'the grade INTERFACES, the check agreeing, salt PASS', 'THE E0 CHECK INTERFACES, AGREE ; SALT-CHECK PASS' in (rd(p('data', 'b689_grade.txt')) or ''),
        'data/b689_grade.txt verdict', '1')
    add('ruling (1)', '8 of 8 constants, n*` 63676', 'ROWS 8 ; EQUAL OR OVERLAPPING 8' in (rd(p('data', 'b689_constants.txt')) or ''), 'data/b689_constants.txt', '1')
    add('ruling (1)', 'the corrigendum at FINDINGS :9342, the corrigenda bank row (3)', 'Corrigendum to b688' in (line(FIND, 9342) or '')
        and '(3) PLACE-papers FINDINGS.md :9320' in (rd(p('data', 'b675_corrigenda.txt')) or ''), 'FINDINGS :9342 ; data/b675_corrigenda.txt', '1')
    for f in ('b689_checks.txt', 'b689_checks_postpush.txt'):
        add('ruling (1)', 'suite 115 of 116, G-EDIT-ROUTE failing (%s)' % f, "ARMS RUN : 116. ### LIVE PASSING : 115. ### LIVE FAILING : 1 ['G-EDIT-ROUTE']"
            in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = json.load(open(p('data', 'b689_scores_close.json'), encoding='utf-8'))
    add('ruling (1)', 'all eight scores HELD', all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), 'data/b689_scores_close.json', '1')
    add('ruling (1)', 'root 7b2d6772 over 53 banks', any(r[1].startswith('7b2d6772a03792f6') for r in act_root_line('b689'))
        and 'BANKS 53 ; CLEAN AND EQUAL AT HEAD 53' in (rd(p('data', 'b689_root_banks.txt')) or ''), 'data/act_roots.txt; data/b689_root_banks.txt', '1')
    add('ruling (1)', 'the b689 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b689.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b689_mirror_verify.txt')) or '')
        and 'Act root: b689 7b2d6772' in (rd(p('data', 'b689_mirror.txt')) or ''), 'the zip; data/b689_mirror_verify.txt; data/b689_mirror.txt', '1')
    dl = rd(p('data', 'b689_defects.txt')) or ''
    add('ruling (1)', 'five defects, (c) the navigator`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'SEAT'), ('b', 'SEAT'), ('c', 'NAVIGATOR'), ('d', 'SEAT'), ('e', 'SEAT')], 'data/b689_defects.txt', '1')
    add('ruling (1)', 'three carry faults caught by the pre-run', 'The pre-run found two faults of the seat`s carry' in (rd(p(*K.B689_FACE.split('/'))) or ''),
        'data/b689_registration_2026-10-19.txt section (0) (two predicate faults and one wrapped needle)', '1')
    # ### (R300)(2): the corrigendum
    add('ruling (2)', 'b689`s face, its declared count line', 'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:** NONE.' in (rd(p(*K.B689_FACE.split('/'))) or ''),
        'data/b689_registration_2026-10-19.txt, section (0)', '1')
    add('ruling (2)', 'the corrigenda bank at row (3), row (4) free', '  (3) PLACE-papers' in (rd(p('data', 'b675_corrigenda.txt')) or '')
        and '  (4) ' not in (rd(p('data', 'b675_corrigenda.txt')) or ''), 'data/b675_corrigenda.txt', '1')
    add('ruling (2)', 'b689`s corrigendum tool (b678`s form)', os.path.exists(p('tools', 'b689_corrigendum.py')), 'tools/b689_corrigendum.py', '1')
    # ### (R300)(3): reading 2's banks
    for f, nd in (('b680_licensed.txt', 'ROWS OUTSIDE LICENSED OR CITED 361'), ('b680_orders.txt', 'ORDERS '), ('b680_methods.txt', 'READY'),
                  ('b680_lag.txt', 'KEYSTONES 19'), ('b680_residues.txt', 'RESIDUES 5')):
        add('ruling (3)', 'reading 2`s figure in data/%s' % f, nd in (rd(p('data', f)) or ''), 'its verdict line', '2')
    add('ruling (3)', 'W-ORD-ONE-COPY`s 13 differing lines', 'read live at PLACE-papers HEAD the tables differ in 13 lines' in (line(p('data', 'b686_correspondence_diff.txt'), 154) or ''),
        'data/b686_correspondence_diff.txt :154', '2')
    add('ruling (3)', 'tools/chain_page.py, the generator', os.path.exists(p('tools', 'chain_page.py')), 'exists', '2')
    # ### (R300)(4)
    add('ruling (4)', 'W-ORD-CIRCUIT-READING not yet entered', 'W-ORD-CIRCUIT-READING' not in (rd(OT) or ''), 'OPEN_TRAILS', '3')
    add('ruling (4); (9)', 'W-ORD-EPSTEIN-COUNT-LEAN at OPEN_TRAILS :14892', 'W-ORD-EPSTEIN-COUNT-LEAN' in (line(OT, 14892) or ''), (line(OT, 14892) or '')[:60], '3')
    # ### (R300)(6): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    for repo, b in K.DELETE_REMOTE:
        add('ruling (6)', '%s origin/%s (the remote)' % (os.path.basename(repo), b), g(repo, 'branch', '-r', '--list', 'origin/' + b)[1].strip(),
            'git branch -r --list', '0')
    add('ruling (6)', 'data/b689_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b689_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R300)(8)-(9)
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b689_worklist.py')) or ''), 'tools/b689_worklist.py', '5')
    lt = rd(p('data', 'b670_licensed_table.txt')) or ''
    add('ruling (9)', 'SIDE-archimedean and SIDE-rcurve tied at 2', 'SIDE-archimedean docstrings (read at 8019d9d)                     2 ->    2' in lt
        and 'SIDE-rcurve docstrings (read at d5f33b4)                          2 ->    2' in lt, 'data/b670_licensed_table.txt :100, :113', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '4')
    add('ferry', 'the four parts (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    for b in ('b690_readfirst.txt', 'b690_reading3.txt', 'b690_circuit_spec.txt', 'b690_rules.txt', 'b690_tool_repairs.txt'):
        sz = b == 'b690_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b690_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b690_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b690 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b690_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b690_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b690_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b690_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b690."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b690'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b690')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b690)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b690_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
