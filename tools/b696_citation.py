# -*- coding: utf-8 -*-
"""b696_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b696's step zero, run before any other step
((R306)(6), per b695's (a)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (b97f6790); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b696; the `word` route
### is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b696_citation_check.txt (.json) ; `ferry` -> data/b696_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b696 from b695_citation.py's form; this tool writes only the banks named above.
"""
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
import b696_worklist as K   # noqa: E402

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
    """the 1-based line of the first line carrying the needle, or 0."""
    return next((i + 1 for i, l in enumerate(L) if needle in l), 0)


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    # ### the ferry's read-first list
    for f in ('data/b695_closing.txt', 'data/b695_defects.txt', 'data/b695_cut.txt', 'data/b675_corrigenda.txt', 'tools/rule_arms.py',
              'data/b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt', 'data/b694_witness_plan.txt', 'data/b694_witness.txt',
              'tools/b694_witness_terms.py', 'data/b685_count.txt', 'data/b687_p3_status.txt', 'data/b681_epstein_zeros_narrowed_hashes.txt',
              'data/b677_tolerance.txt', 'data/b695_nodes_zeta.txt', 'data/b695_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b695_closing.txt'))
    add('ferry read-first', 'data/b695_closing.txt :1 the head line', cl[0].startswith('b695 closed: relay aa70ac82'), cl[0][:120], '0')
    df = lines_of(p('data', 'b695_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b695_defects.txt (rows are defects as lettered)', lt == list('abcd'), 'letters %s' % ''.join(lt), '0')
    cu = lines_of(p('data', 'b695_cut.txt'))
    add('ferry read-first', 'data/b695_cut.txt (the tie-break reading by line)', len(cu) > 3 and 'DECIDED AT STEP (iii)' in cu[2],
        'data/b695_cut.txt :3 names the tie-break at step (iii) and cites data/b695_tie.txt, where the reading stands in full', '0')
    co = lines_of(p('data', 'b675_corrigenda.txt'))
    add('ferry read-first', 'data/b675_corrigenda.txt rows (9) and (10) by line', len(co) > 74 and co[66].startswith('  (9) relay data/b694_circuit')
        and co[73].startswith('  (10) relay data/b694_registration'), 'data/b675_corrigenda.txt :67-:73 (row (9)), :74- (row (10))', '0-1')
    ra = lines_of(p('tools', 'rule_arms.py'))
    add('ferry read-first', 'the binary-hashes arm in tools/rule_arms.py by line', first(ra, "'G-RULE-BINARY-HASHES'") > 0,
        'tools/rule_arms.py :%d (the arm`s name), the reading at :%d' % (first(ra, "'G-RULE-BINARY-HASHES'"), first(ra, "bad = [b['path'] for b in bs")), '0-1')
    ph = lines_of(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt'))
    add('ferry read-first', 'b694`s circuit hashes bank, the PNG row by line', len(ph) > 4 and ph[3].strip().startswith('data/b692_circuit_SIDE-lv-conservation_v0.13.0.png | 148025d5'),
        'data/b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt :4', '0-1')
    wt = lines_of(p('data', 'b694_witness.txt'))
    add('ferry read-first', 'data/b694_witness.txt (rows are widths)', len(wt) > 34 and 'FOUND AT WIDTHS 32, 48, 64, 96, 128, 192' in wt[33], 'data/b694_witness.txt :34', '0-2')
    wl = lines_of(p('tools', 'b694_witness_terms.py'))
    add('ferry read-first', 'the witness tool: the truncation height', len(wl) > 57 and wl[53].startswith('R_INT = 4000') and wl[56].startswith("ZETA_T = '151.59'"),
        'tools/b694_witness_terms.py :54 (R_INT = 4000, the archimedean truncation), :57 (ZETA_T = 151.59, the zero list`s top)', '0-2')
    add('ferry read-first', 'the witness tool: the archimedean tail', first(wl, 'def tail_bound') == 266, 'tools/b694_witness_terms.py :%d-:284' % first(wl, 'def tail_bound'), '0-2')
    add('ferry read-first', 'the witness tool: the zero-side tail', first(wl, 'def zero_tail') == 462, 'tools/b694_witness_terms.py :%d-:479' % first(wl, 'def zero_tail'), '0-2')
    bc = lines_of(p('data', 'b685_count.txt'))
    add('ferry read-first', 'data/b685_count.txt (the constants a, c as balls by row)', len(bc) > 23 and '0.432571915432' in bc[20] and '1.26244217716' in bc[22],
        'data/b685_count.txt :21 (a), :23 (c)', '0-2')
    add('ferry read-first', 'data/b687_p3_status.txt', 'DERIVED' in (rd(p('data', 'b687_p3_status.txt')) or ''), 'data/b687_p3_status.txt', '0-2')
    hb = rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ferry read-first', 'data/b681`s hashes bank (the certified height by row)', re.search(r'151\.59|height|HEIGHT', hb),
        'data/b681_epstein_zeros_narrowed_hashes.txt carries %d lines, the two files` sha256 and the chain, and no height row; the height 151.59 stands at '
        'tools/b694_witness_terms.py :57 (ZETA_T)' % len(hb.rstrip(NL).split(NL)), '0-2')
    add('ferry read-first', 'data/b677_tolerance.txt :90', 'P1 WIDTHS 19' in (line(p('data', 'b677_tolerance.txt'), 90) or ''), 'data/b677_tolerance.txt :90', '0-2')
    for n, nd in ((15198, 'W-ORD-WITNESS-TAIL-BALLS'), (15200, 'W-ORD-H2-BRIDGE')):
        add('ferry read-first', 'OPEN_TRAILS :%d' % n, nd in (line(OT, n) or ''), 'OPEN_TRAILS :%d carries %s' % (n, nd), '0-2')
    nz = lines_of(p('data', 'b695_nodes_zeta.txt'))
    add('ferry read-first', 'data/b695_nodes_zeta.txt :734 (the Weil-face line as the page carries it)', len(nz) > 733 and 'the Weil face at Q0' in nz[733],
        'the node list has %d lines; its Weil-face line is :%d; :734 is the page`s line (%s :%d)' % (
            len(nz), first(nz, 'the Weil face at Q0'), K.FACES_PAGE, first(lines_of(os.path.join(PP, K.FACES_PAGE)), 'the Weil face at Q0')), '0-3')
    # ### (R306)(1)
    add('ruling (1)', 'the head line quoted from data/b695_closing.txt :1', cl[0] == ('b695 closed: relay aa70ac82, PLACE-papers 5ed6e31; suite 121 of 122; '
                                                                                   'root a84059769e7dd478\u2026; 2 prompts answered; 4 defects'), cl[0][:120], '1')
    po = rd(p('data', 'b695_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing commit a0478dee pushed and read back at relay main', 'main read back at the remote: a0478dee' in po,
        'data/b695_closing_push_out.txt', '0-1')
    add('ruling (1)', 'b694`s weight line at FINDINGS :9578', (line(FI, 9578) or '').startswith('*Appended 2026-10-20 by b695 to b694'), (line(FI, 9578) or '')[:70], '1')
    add('ruling (1)', 'the corrigendum for (k) and (l) at :9580', 'orrigendum' in (line(FI, 9580) or '')[:300], (line(FI, 9580) or '')[:70], '1')
    add('ruling (1)', 'the corrigenda bank at rows (9) and (10)', len(co) > 74 and co[66].startswith('  (9)') and co[73].startswith('  (10)'), 'data/b675_corrigenda.txt :67, :74', '1')
    ti = rd(p('data', 'b695_tie.txt')) or ''
    add('ruling (1)', 'the tie-break read in its written order, naming SIDE-interfaces at step (iii)', 'DECIDED AT STEP (iii)' in ti and 'SIDE-interfaces' in ti, 'data/b695_tie.txt', '1')
    add('ruling (1)', 'workflow 9b4c484 and print list 58854f0; merged --no-ff at c8bd217, tagged v0.2.1', all(s in NL.join(cu) for s in ('9b4c484', '58854f0', 'c8bd217', 'v0.2.1')),
        'data/b695_cut.txt :4-:7', '1')
    add('ruling (1)', 'runs 39487947819 and 39488049232, 11 prints equal', '39487947819' in cu[8] and '39488049232' in cu[8] and 'EQUAL LINE FOR LINE True' in cu[8],
        'data/b695_cut.txt :9', '1')
    add('ruling (1)', 'the quotation search finding 4 quoting lines, each carried', 'QUOTING LINES 4, EACH A RESIDUE CARRIED' in cu[-2], 'data/b695_cut.txt :24', '1')
    add('ruling (1)', 'the distance 1 to 0', 'THE DISTANCE BEFORE 1, AFTER 0' in cu[-2], 'data/b695_cut.txt :24', '1')
    add('ruling (1)', ':734 the Weil-face line (the page)', 'the Weil face at Q0' in (line(os.path.join(PP, K.FACES_PAGE), 734) or ''), '%s :734' % K.FACES_PAGE, '1')
    add('ruling (1)', 'W-ORD-WITNESS-TAIL-BALLS`s trigger re-read at OPEN_TRAILS :15198', 'W-ORD-WITNESS-TAIL-BALLS' in (line(OT, 15198) or ''), 'OPEN_TRAILS :15198', '1')
    add('ruling (1)', 'W-ORD-H2-BRIDGE annotated at :15200', 'W-ORD-H2-BRIDGE' in (line(OT, 15200) or ''), 'OPEN_TRAILS :15200', '1')
    for f in ('b695_checks.txt', 'b695_checks_postpush.txt'):
        t = rd(p('data', f)) or ''
        add('ruling (1)', 'suite 121 of 122 (%s)' % f, 'ARMS RUN : 122. ### LIVE PASSING : 121.' in t, 'data/%s' % f, '1')
    add('ruling (1)', 'sealed tools 9 of 9', any('AGREE 9 of 9' in l for l in cl), 'data/b695_closing.txt :%d' % first(cl, 'AGREE 9 of 9'), '1')
    ar = act_root_line('b695')
    add('ruling (1)', 'root a8405976 over 74 banks', ar and ar[0][1].startswith('a8405976') and 'BANKS 74' in (rd(p('data', 'b695_root_banks.txt')) or ''),
        'data/act_roots.txt ; data/b695_root_banks.txt', '1')
    mi = rd(p('data', 'b695_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-20-b695.zip CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-20-b695.zip')
        and 'Act root: b695 a8405976' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi, 'the zip; data/b695_mirror.txt', '1')
    sc = rd(p('data', 'b695_scores_close.json')) or ''
    add('ruling (1)', 'N1-N3, N5 and S1-S3 HELD', sc.count('"HELD"') >= 7, 'data/b695_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    # ### (R306)(2)
    pb = open(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0.png'), 'rb').read() if os.path.exists(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0.png')) else b''
    add('ruling (2)', 'b695`s row (9): the corrected path and the equal sha256', hashlib.sha256(pb).hexdigest() == '148025d53c948b89696afe35c035e4655cd7a2a0b9a3b548eb722ee0d710c918'
        and 'data/b694_circuit_SIDE-lv-conservation_v0.13.0.png, sha256' in co[68], 'data/b675_corrigenda.txt :69-:70 ; the file`s sha256 %s' % hashlib.sha256(pb).hexdigest()[:16], '1')
    add('ruling (2)', 'data/b696_tool_repairs.txt -- TO BE WRITTEN, not a cite', not os.path.exists(p('data', 'b696_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R306)(3)
    add('ruling (3)', 'W-ORD-WITNESS-TAIL-BALLS (OPEN_TRAILS :15198)', 'W-ORD-WITNESS-TAIL-BALLS' in (line(OT, 15198) or ''), 'OPEN_TRAILS :15198', '2')
    add('ruling (3)', 'data/b694_witness_plan.txt', os.path.exists(p('data', 'b694_witness_plan.txt')), 'data/b694_witness_plan.txt', '2')
    add('ruling (3)', 'the truncation the b694 tool uses', len(wl) > 54 and wl[53].startswith('R_INT = 4000'), 'tools/b694_witness_terms.py :54', '2')
    add('ruling (3)', 'data/b685_count.txt`s constants a, c as balls', len(bc) > 23 and '4.33e-41' in bc[20] and '1.26e-40' in bc[22], 'data/b685_count.txt :21, :23', '2')
    add('ruling (3)', 'data/b687_p3_status.txt`s status', 'DERIVED' in (rd(p('data', 'b687_p3_status.txt')) or ''), 'data/b687_p3_status.txt', '2')
    add('ruling (3)', 'every width of data/b694_witness.txt', len(wt) > 34 and 'FOUND AT WIDTHS 32, 48, 64, 96, 128, 192' in wt[33], 'data/b694_witness.txt :34', '2')
    for b in ('b696_tails_plan.txt', 'b696_witness_balls.txt'):
        add('ruling (3)', 'data/%s -- TO BE WRITTEN, not a cite' % b, not os.path.exists(p('data', b)), 'absent, as ordered', '2')
    # ### (R306)(4)
    add('ruling (4)', 'the Weil-face line`s tail-bound caveat (the row as it stands)', len(nz) > 167 and 'tail bounds float with a safety factor, not balls (W-ORD-WITNESS-TAIL-BALLS)' in nz[167],
        'data/b695_nodes_zeta.txt :168', '3')
    add('ruling (4)', 'data/b696_faces_rows.txt -- TO BE WRITTEN where discharged', not os.path.exists(p('data', 'b696_faces_rows.txt')), 'absent, as ordered', '3')
    # ### (R306)(5): the branches -- listed before any delete; the deletes follow this check
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (5)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'listed at the working repository before any delete', '0')
    add('ruling (5)', 'data/b695_closing_push_out.txt to be committed (untracked now)', os.path.exists(p('data', 'b695_closing_push_out.txt'))
        and not (g(ROOT, 'ls-files', 'data/b695_closing_push_out.txt')[1] or '').strip(), 'untracked at the working tree', '0')
    # ### (R306)(6)-(8)
    add('ruling (6)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')) and 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b695_worklist.py')) or ''), 'tools/b695_worklist.py', '5')
    add('ruling (8)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '5')
    add('ruling (8)', 'b674`s rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8', '5')
    add('ruling (8)', 'rule (2) of data/b690_rules.txt', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''), 'data/b690_rules.txt :9', '5')
    add('ruling (8)', 'the regularity-uses bank', 'REGULARITY-USES BANK' in (rd(p('data', 'b692_candidates_priced.txt')) or ''), 'data/b692_candidates_priced.txt', '5')
    add('ruling (8)', 'CORRESPONDENCE-DOMINANCE (the eleventh spec row)', 'CORRESPONDENCE-DOMINANCE' in (rd(p('data', 'b695_circuit_spec.txt')) or ''), 'data/b695_circuit_spec.txt', '5')
    add('ruling (8)', 'W-ORD-EPSTEIN-COUNT-LEAN', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(OT) or ''), 'OPEN_TRAILS', '5')
    # ### the ferry
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '2-4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '4')
    add('ferry C5', 'b673`s capture names', os.path.exists(p('data', 'b695_relay_push_out.txt')), 'data/b695_relay_push_out.txt (the form carried)', '5')
    add('ferry C5', 'the b670 mirror form', os.path.exists(p('data', 'b670_mirror.txt')) or os.path.exists(p('data', 'b695_mirror.txt')), 'data/b695_mirror.txt (the form carried)', '5')
    add('ruling; ferry', 'data/b696_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b696_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b696_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b696_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b696 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R306)(6)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b696_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b696_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b696_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b696_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b696."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b696'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b696')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b696)', 'exec'), ns)
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
        print('usage: b696_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
