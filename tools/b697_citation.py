# -*- coding: utf-8 -*-
"""b697_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b697's step zero, run before any other step
((R307)(6)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (b97f6790); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b697; the `word` route
### is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b697_citation_check.txt (.json) ; `ferry` -> data/b697_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b697 from b696_citation.py's form; this tool writes only the banks named above.
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
import b697_worklist as K   # noqa: E402

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


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    page = lines_of(os.path.join(PP, K.FACES_PAGE))
    # ### the ferry's read-first list
    for f in ('data/b696_closing.txt', 'data/b696_defects.txt', 'data/b696_witness_balls.txt', 'data/b696_tails_plan.txt', 'data/b696_faces_rows.txt',
              'data/b695_nodes_zeta.txt', 'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b695_cut.txt', 'data/b690_rules.txt',
              'data/glossary.txt', 'data/b675_li_bench.txt', 'tools/chain_page.py', 'tools/correspondence_gen.py', 'data/b696_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b696_closing.txt'))
    df = lines_of(p('data', 'b696_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b696_defects.txt (rows are defects as lettered)', lt == list('abcd'), 'letters %s' % ''.join(lt), '0')
    wb = lines_of(p('data', 'b696_witness_balls.txt'))
    add('ferry read-first', 'data/b696_witness_balls.txt, the a = 32 row by line', len(wb) > 14 and wb[13].startswith('  N | 32 ') and '3.68e-23' in wb[13],
        'data/b696_witness_balls.txt :14', '0-2')
    tp = lines_of(p('data', 'b696_tails_plan.txt'))
    add('ferry read-first', 'data/b696_tails_plan.txt, the note on where each tail enters', len(tp) > 17 and "THE SUM'S RADIUS" in tp[8] and "THE IDENTITY'S TOLERANCE" in tp[11],
        'data/b696_tails_plan.txt :6-:17 (the sum`s radius :9, the identity`s tolerance :12, the reading :15-:17)', '0-2')
    fr = lines_of(p('data', 'b696_faces_rows.txt'))
    add('ferry read-first', 'data/b696_faces_rows.txt, the successor and the seat`s note by line', len(fr) > 11 and fr[10].startswith('# backmatter:')
        and 'tail bounds as certified balls (b696)' in fr[10] and first(fr, 'THE SEAT`S NOTE FOR THE AUTHOR') > 0,
        'data/b696_faces_rows.txt :11 (the successor), :%d (the seat`s note)' % first(fr, 'THE SEAT`S NOTE FOR THE AUTHOR'), '0-2')
    nz = lines_of(p('data', 'b695_nodes_zeta.txt'))
    add('ferry read-first', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md :734 and data/b695_nodes_zeta.txt :168', len(page) > 733 and 'the Weil face at Q0' in page[733]
        and len(nz) > 167 and 'the Weil face at Q0' in nz[167], 'the page :734 ; the node list :168', '0-2')
    add('ferry read-first', 'data/b674_rules.txt (the tie-break rule by line)', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''),
        'data/b674_rules.txt :8-:11', '0-3')
    cu = lines_of(p('data', 'b695_cut.txt'))
    add('ferry read-first', 'data/b695_cut.txt (its written-order reading by line)', len(cu) > 3 and 'DECIDED AT STEP (iii)' in cu[2],
        'data/b695_cut.txt :3 (the full reading at data/b695_tie.txt :42-:47)', '0-3')
    add('ferry read-first', 'data/b690_rules.txt row (2)', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '0-3')
    gl = lines_of(p('data', 'glossary.txt'))
    add('ferry read-first', 'the glossary`s arithmetic-limit entry (data/glossary.txt by line; README :121)', first(gl, 'arith_limit_nonneg_iff_rh') > 0
        and 'arith_limit_nonneg_iff_rh' in (line(os.path.join(PP, 'README.md'), 121) or ''),
        'data/glossary.txt :%d ; README.md :121' % first(gl, 'arith_limit_nonneg_iff_rh'), '0-4')
    add('ferry read-first', 'data/b675`s Li-face bank by path (the form)', os.path.exists(p('data', 'b675_li_bench.txt')) and os.path.exists(p('data', 'b675_li_readings.txt')),
        'data/b675_li_bench.txt, data/b675_li_readings.txt, data/b675_li_controls.txt', '0-4')
    # ### (R307)(1)
    add('ruling (1)', 'the head line quoted from data/b696_closing.txt :1', cl[0] == ('b696 closed: relay 564e9bb9, PLACE-papers 345da1a; suite 118 of 118; '
                                                                                   'root 8d5b3d9d32ec5804\u2026; 3 prompts answered; 4 defects'), cl[0][:120], '1')
    po = rd(p('data', 'b696_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay main 77b55588', 'main read back at the remote: 77b55588' in po, 'data/b696_closing_push_out.txt', '0-1')
    add('ruling (1)', 'W-ORD-WITNESS-TAIL-BALLS DISCHARGED', 'THE ORDER DISCHARGED' in (wb[-2] if len(wb) > 2 else ''), 'data/b696_witness_balls.txt :33', '1')
    add('ruling (1)', '3.68e-23 and 1.43e-18 ; 4.02e-9 at a = 32', len(wb) > 14 and '(a) 3.68e-23' in wb[13] and 'old radius 1.4319e-18' in wb[13] and '(b) 4.02e-9' in wb[13],
        'data/b696_witness_balls.txt :14', '1')
    add('ruling (1)', 'the zero tail`s float 2.41e-4 at a = 32', 'tail 2.41e-04' in (line(p('data', 'b694_witness.txt'), 15) or ''), 'data/b694_witness.txt :15', '1')
    add('ruling (1)', 'the narrowest margin at a = 32, -7.7752874967979 +- 3.68e-23', len(wb) > 14 and 'S -7.7752874967979 +- 3.68e-23' in wb[13], 'data/b696_witness_balls.txt :14', '1')
    wc = rd(p('data', 'b696_witness_balls_controls.txt')) or ''
    add('ruling (1)', 'zeta 16 of 16, identity 34 of 34, 33 of 33, T1', 'C1 16 OF 16' in wc and 'C3 34 OF 34' in wc and 'SHRINK AS PREDICTED 33 OF 33' in wc
        and 'T1 AS RE-WORDED True' in wc, 'data/b696_witness_balls_controls.txt :71', '1')
    ab = rd(p('data', 'b696_arm_binary.txt')) or ''
    add('ruling (1)', 'G-RULE-BINARY-HASHES 5 of 5', 'CASES 5 ; AS WANTED 5' in ab, 'data/b696_arm_binary.txt', '1')
    for f in ('b696_checks.txt', 'b696_checks_postpush.txt'):
        add('ruling (1)', 'suite 118 of 118 (%s)' % f, 'ARMS RUN : 118. ### LIVE PASSING : 118.' in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = rd(p('data', 'b696_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b696_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    mi = rd(p('data', 'b696_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-20-b696.zip CLEAN with the root line', 'Act root: b696 8d5b3d9d' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi,
        'data/b696_mirror.txt', '1')
    add('ruling (1)', 'four defects, (a)-(c) the navigator`s, (d) the seat`s', lt == list('abcd') and len(re.findall(r"^    \([abc]\) THE NAVIGATOR'S", NL.join(df), re.M)) == 3,
        'data/b696_defects.txt', '1')
    # ### (R307)(2)
    add('ruling (2)', 'the successor`s "± 1.43e-18" and the a = 32 row`s 3.68e-23', len(fr) > 11 and '± 1.43e-18' in fr[10] and len(wb) > 14 and '3.68e-23' in wb[13],
        'data/b696_faces_rows.txt :11 ; data/b696_witness_balls.txt :14', '2')
    add('ruling (2)', 'the plan`s note at b696 (the zero tail entering the identity`s gate)', len(tp) > 17 and 'gates' in tp[12], 'data/b696_tails_plan.txt :12-:14', '2')
    add('ruling (2)', 'b695`s list re-emits the page (the INSTRUMENTS.md row taken up at b695)', 'data/b695_nodes_zeta.txt' in (page[2] if len(page) > 2 else ''),
        'the page :3 names data/b695_nodes_zeta.txt', '2')
    add('ruling (2)', 'data/b697_nodes_zeta.txt -- TO BE WRITTEN where the word is regenerate', not os.path.exists(p('data', 'b697_nodes_zeta.txt')), 'absent, as ordered', '2')
    # ### (R307)(3)
    add('ruling (3)', 'data/b670_licensed_table.txt', os.path.exists(p('data', 'b670_licensed_table.txt')), 'data/b670_licensed_table.txt', '3')
    add('ruling (3)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '3')
    add('ruling (3)', 'b674`s rule as b695 read it', 'DECIDED AT STEP (iii)' in (rd(p('data', 'b695_tie.txt')) or ''), 'data/b695_tie.txt :42-:47', '3')
    add('ruling (3)', 'b676`s form', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '3')
    add('ruling (3)', 'tools/correspondence_gen.py, carried-at cells from the carrying source', 'read_carry' in (rd(p('tools', 'correspondence_gen.py')) or ''),
        'tools/correspondence_gen.py', '3')
    add('ruling (3)', 'data/b697_cut.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b697_cut.txt')), 'absent, as ordered', '3')
    # ### (R307)(4)
    add('ruling (4)', 'README :121 as the glossary cites it', 'README :121' in (gl[first(gl, 'arith_limit_nonneg_iff_rh') - 1] if first(gl, 'arith_limit_nonneg_iff_rh') else ''),
        'data/glossary.txt :%d' % first(gl, 'arith_limit_nonneg_iff_rh'), '4')
    add('ruling (4)', 'the Li face`s n_obs = 10034', '10034' in (rd(p('data', 'b675_li_readings.txt')) or '') + (rd(p('data', 'b675_li_bench.txt')) or ''),
        'data/b675_li_readings.txt / data/b675_li_bench.txt', '4')
    add('ruling (4)', 'the Weil face`s a = 32', 'THE NARROWEST MARGIN AT a = 32' in (wb[-2] if len(wb) > 2 else ''), 'data/b696_witness_balls.txt :33', '4')
    add('ruling (4)', 'data/b697_arith_plan.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b697_arith_plan.txt')), 'absent, as ordered', '4')
    add('ruling (4)', 'the regularity-uses bank', 'REGULARITY-USES BANK' in (rd(p('data', 'b692_candidates_priced.txt')) or ''), 'data/b692_candidates_priced.txt', '4')
    add('ruling (4)', 'CORRESPONDENCE-DOMINANCE', 'CORRESPONDENCE-DOMINANCE' in (rd(p('data', 'b695_circuit_spec.txt')) or ''), 'data/b695_circuit_spec.txt', '4')
    add('ruling (4)', 'W-ORD-EPSTEIN-COUNT-LEAN', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(OT) or ''), 'OPEN_TRAILS', '4')
    # ### (R307)(5)
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (5)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'listed at the working repository before any delete', '0')
    add('ruling (5)', 'data/b696_closing_push_out.txt to be committed (untracked now)', os.path.exists(p('data', 'b696_closing_push_out.txt'))
        and not (g(ROOT, 'ls-files', 'data/b696_closing_push_out.txt')[1] or '').strip(), 'untracked at the working tree', '0')
    # ### (R307)(6)-(8)
    add('ruling (6)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b696_worklist.py')) or ''), 'tools/b696_worklist.py', '6')
    add('ruling (8)', 'b680`s and b690`s reading list', os.path.exists(p('data', 'b680_closing.txt')) and os.path.exists(p('data', 'b690_closing.txt')),
        'data/b680_closing.txt ; data/b690_closing.txt', '6')
    add('ruling (8)', 'the defects banks b673 through b696', all(os.path.exists(p('data', 'b%d_defects.txt' % a)) for a in range(673, 697)),
        'data/b673_defects.txt .. data/b696_defects.txt', '6')
    # ### the ferry
    add('ferry C1', 'b696`s entry and trail', (line(FI, K.B696_ENTRY) or '').startswith('## The Weil-face witness at Q0 with its tail bounds')
        and (line(OT, K.B696_TRAIL) or '').startswith('### b696'), 'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B696_ENTRY, K.B696_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '5')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b696_relay_push_out.txt')), 'data/b696_relay_push_out.txt (the form carried)', '6')
    add('ruling; ferry', 'data/b697_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b697_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b697_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b697_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b697 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R307)(6)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b697_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b697_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b697_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b697_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b697."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b697'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b697')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b697)', 'exec'), ns)
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
        print('usage: b697_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
