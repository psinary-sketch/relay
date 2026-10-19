# -*- coding: utf-8 -*-
"""b688_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b688's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (a90bcdb6, b687's continued); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b688.
### Routes: `check` -> data/b688_citation_check.txt (.json) ; `ferry` -> data/b688_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b688 from b687_citation.py's form; this tool writes only the banks named above.
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
import b688_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = 'RULING (R298) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
SP = 'D:/SIDE-spinor'
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
    for f in ('data/b687_closing.txt', 'data/b687_defects.txt', 'data/b687_p3_status.txt', 'data/b687_q0_reread.txt', 'data/b687_steps.txt',
              'tools/b687_readings.py', 'data/b667_epstein_plan.txt', 'data/b649_nodes_zeta.txt', 'tools/chain_page.py',
              'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b686_cut.txt', 'tools/correspondence_gen.py',
              'data/b687_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'chain_page.py`s input as the tool read it at the page`s last write', os.path.exists(p('data', 'b680_nodes_zeta.txt'))
        and 'data/b680_nodes_zeta.txt' in (line(os.path.join(PP, K.FACES_PAGE), 3) or ''), 'the page :3 names relay data/b680_nodes_zeta.txt', '2')
    add('ferry read-first', 'SIDE-spinor`s print bank at v0.1.1 by path', os.path.exists(p('data', 'b686_axioms_SIDE-spinor_after.txt'))
        and os.path.exists(p('data', 'b686_prints_SIDE-spinor.txt')), 'data/b686_axioms_SIDE-spinor_after.txt, data/b686_prints_SIDE-spinor.txt', '4')
    # ### (R298)(1): b687 at its weight
    head = (rd(p('data', 'b687_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b687_closing.txt :1', head == ('b687 closed: relay 24b23df1, PLACE-papers 51d3aac; suite 114 of 115; root '
                                                                                   '898a41008e25cfe2\u2026; 7 prompts answered; 8 defects'), head[:120], '1')
    po = rd(p('data', 'b687_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay de011ebd read back', '24b23df1..de011ebd' in po and 'read back at the remote: de011ebd' in po,
        'data/b687_closing_push_out.txt', '0-1')
    mt = rd(p('data', 'b687_matched.txt')) or ''
    add('ruling (1)', 'a_e = 0.218287, b_e = 0, c_e = 1.731426', 'a_e = 0.218287209229' in mt and 'c_e = 1.73142622655' in mt, 'data/b687_matched.txt section 1', '1')
    add('ruling (1)', 'below every located bound at e, 10, 100, 1000 and 10⁴', mt.count('SHARPER THAN EVERY LOCATED BOUND (the T ≥ e bound): True') == 5,
        'data/b687_matched.txt section 3', '1')
    add('ruling (1)', 'the crossovers 1.28·10⁵, 1.44·10⁶, 5.9·10²⁹', 'PT15|e        T* = 127847' in mt and 'TR14|e        T* = 1.44094e+06' in mt
        and 'HSW|e         T* = 5.93937e+29' in mt, 'data/b687_matched.txt :74, :78, :80', '1')
    jz, jq = rd(p('data', 'b687_jensen_zeta.txt')) or '', rd(p('data', 'b687_jensen_q0.txt')) or ''
    add('ruling (1)', 'readings (ii)-(iii) holding, the inner disc VACUOUS for ζ', 'ζ: EVERY DISC READING HOLDS' in jz and 'VACUOUS' in jz
        and 'Z_Q: EVERY DISC READING HOLDS AT 50, 100, 149' in jq, 'data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt verdict lines', '1')
    b3 = json.load(open(p('data', 'b687_readings_part3.json'), encoding='utf-8'))
    add('ruling (1)', 'the band (150, 151.59] at two zeros both on the line', b3.get('count') == 2 and b3.get('complete') and len(b3.get('zeros') or []) == 2,
        'data/b687_readings_part3.json', '1')
    st = rd(p('data', 'b687_steps.txt')) or ''
    add('ruling (1)', '114 of 114, the narrowest margin 0.058 on the envelope', '114 OF 114 INTERMEDIATE INEQUALITIES HOLD' in st and 'margin 0.057746' in st,
        'data/b687_steps.txt :107, its verdict', '1')
    cp = rd(p('data', 'b687_composition.txt')) or ''
    add('ruling (1)', 'the composition: 41.98 on [150, 151.5], κ₁ = 1.18', '41.9784' in cp and '[150, 151.5]' in cp and 'κ1 1.18345' in cp,
        'data/b687_composition.txt', '1')
    add('ruling (1)', 'P3 entered in (R297)(5)`s words', K.NEXT and 'DERIVED — constants certified in balls' in (rd(p('data', 'b687_p3_status.txt')) or ''),
        'data/b687_p3_status.txt', '1')
    for n, needle in ((14890, 'DISCHARGED-BY-DERIVATION'), (14892, 'a research act after b690')):
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in (line(OT, n) or ''), (line(OT, n) or '')[:70], '1')
    for f in ('b687_checks.txt', 'b687_checks_postpush.txt'):
        add('ruling (1)', 'suite 114 of 115, G-EDIT-ROUTE declared (%s)' % f, "ARMS RUN : 115. ### LIVE PASSING : 114. ### LIVE FAILING : 1 ['G-EDIT-ROUTE']"
            in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = json.load(open(p('data', 'b687_scores_close.json'), encoding='utf-8'))
    add('ruling (1)', 'all eight scores HELD', all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), 'data/b687_scores_close.json', '1')
    add('ruling (1)', 'root 898a4100 over 54 banks', any(r[1].startswith('898a41008e25cfe2') for r in act_root_line('b687'))
        and 'BANKS 54 ; CLEAN AND EQUAL AT HEAD 54' in (rd(p('data', 'b687_root_banks.txt')) or ''), 'data/act_roots.txt; data/b687_root_banks.txt', '1')
    add('ruling (1)', 'the b687 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b687.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b687_mirror_verify.txt')) or '')
        and 'Act root: b687 898a4100' in (rd(p('data', 'b687_mirror.txt')) or ''), 'the zip; data/b687_mirror_verify.txt; data/b687_mirror.txt', '1')
    dl = rd(p('data', 'b687_defects.txt')) or ''
    add('ruling (1)', 'eight defects, (a) (g) (h) the seat`s, (b)-(f) the navigator`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'SEAT'), ('b', 'NAVIGATOR'), ('c', 'NAVIGATOR'), ('d', 'NAVIGATOR'), ('e', 'NAVIGATOR'), ('f', 'NAVIGATOR'), ('g', 'SEAT'), ('h', 'SEAT')],
        'data/b687_defects.txt :5-:66', '1')
    add('ruling (1)', '(g) at :48, (h) at :57', (line(p('data', 'b687_defects.txt'), 48) or '').startswith('    (g)')
        and (line(p('data', 'b687_defects.txt'), 57) or '').startswith('    (h)'), 'data/b687_defects.txt :48, :57', '1')
    add('ruling (1)', 'the band taking about 1.2 hours', 'Ten R3 calls in all' in dl, 'data/b687_defects.txt (g) (the calls 01:02-02:02Z)', '1')
    # ### (R298)(2): the lattice route
    rs = rd(p('tools', 'b687_readings.py')) or ''
    add('ruling (2); ferry', 'the lattice route by line (tools/b687_readings.py :168-:203)', (line(p('tools', 'b687_readings.py'), 173) or '').startswith('def zq_lattice')
        and 'LAT_N = 60' in (line(p('tools', 'b687_readings.py'), 168) or ''), 'tools/b687_readings.py :168, :173, :196', '1')
    add('ruling (2)', 'the three-point check against b667`s route', 'the lattice sum against b667`s at 2.4 + 50i' in (rd(p('data', 'b687_controls.txt')) or ''),
        'data/b687_controls.txt (route) rows', '1')
    add('ruling (2); ferry', 'the rows of data/b687_steps.txt that consumed it (the Z_Q (iv-4) rows)', all('Z_Q' in (line(p('data', 'b687_steps.txt'), n) or '')
        and '(iv-4)' in (line(p('data', 'b687_steps.txt'), n) or '') for n in (69, 70, 88, 89, 107, 108)), 'data/b687_steps.txt :69, :70, :88, :89, :107, :108', '1')
    add('ruling (2)', 'the b687 plan bank to take a row beneath', os.path.exists(p('data', 'b687_plan.txt')), 'data/b687_plan.txt', '1')
    ep = rd(p('data', 'b667_epstein_plan.txt')) or ''
    add('ferry', 'b667`s Z_Q route to σ = 2.5 by section (T4 for |μ| ≤ 2)', '== 16. THE SECOND RUN' in ep and 'for |μ| ≤ 2' in ep,
        'data/b667_epstein_plan.txt section 16 (:267-:285), section 2 (:22-:54); tools/b667_epstein_certify.py :152-:153', '1')
    add('ruling (2)', 'a band priced from b667`s run record', os.path.exists(p('data', 'b667_epstein_certify_run.txt')) or 'segments' in (rd(p('data', 'b687_readings_part3.json')) or ''),
        'b667`s run record or b687`s banked square times (data/b687_readings_part3.json)', '1')
    # ### (R298)(3): the faces line
    nr = line(p('data', 'b680_nodes_zeta.txt'), K.NODES_ROW) or ''
    add('ruling (3)', 'the generator`s input row (b680) naming T-COUNT as assumed', 'the local count assumed' in nr and 'T-COUNT named' in nr,
        'data/b680_nodes_zeta.txt :167', '2')
    add('ruling (3)', 'written at b680 through the generator', 'b680' in (rd(p('data', 'b680_faces_diff.txt')) or '') and 'PAGE WRITTEN True' in (rd(p('data', 'b680_faces_diff.txt')) or ''),
        'data/b680_faces_diff.txt', '2')
    add('ruling (3)', 'the page carries the row once', (rd(os.path.join(PP, K.FACES_PAGE)) or '').count('T-COUNT named') == 1, K.FACES_PAGE, '2')
    # ### (R298)(4): the next document
    lt = rd(p('data', 'b670_licensed_table.txt')) or ''
    add('ruling (4)', 'SIDE-li-map at 3 the carried candidate', 'SIDE-li-map docstrings (read at b515e6b)                          3 ->    3' in lt,
        'data/b670_licensed_table.txt :111', '3')
    add('ruling (4)', 'b674`s tie-break rule', '(2) THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '3')
    add('ruling (4)', 'b652`s order', 'the next kernel by descending count under the same rules, then the companions' in (line(p('data', 'b652_ferry.txt'), 19) or ''),
        'data/b652_ferry.txt :19', '3')
    add('ruling (4)', 'the per-document table of SIDE-li-map', os.path.exists(p('data', 'b647_table_SIDE-li-map.txt')), 'data/b647_table_SIDE-li-map.txt', '3')
    add('ruling (4)', 'b676`s form', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '3')
    # ### (R298)(5): R4
    ct = rd(p('data', 'b686_cut.txt')) or ''
    add('ruling (5); ferry', 'R4`s row and its ACTION by line', 'R4   SIDESpinor/SpinorLeg.lean:21 (header)' in (line(p('data', 'b686_cut.txt'), 51) or '')
        and 'the ACTION verbatim, :15-:18' in (line(p('data', 'b686_cut.txt'), 43) or ''), 'data/b686_cut.txt :42-:46, :51-:53', '4')
    sl = g(SP, 'show', 'v0.1.1:SIDESpinor/SpinorLeg.lean')[1].split(NL)
    add('ruling (5)', 'SpinorLeg.lean :21 “(salt-checked)”', len(sl) > 20 and '(salt-checked)' in sl[20], (sl[20] if len(sl) > 20 else '')[:80], '4')
    add('ruling (5)', 'b684`s form (data/b684_residue_actions.txt)', os.path.exists(p('data', 'b684_residue_actions.txt')), 'data/b684_residue_actions.txt', '4')
    tg = g(SP, 'rev-parse', '--short', 'v0.1.1^{commit}')[1].strip()
    add('ruling (5)', 'SIDE-spinor at v0.1.1 on main, v0.1.2 free', tg == g(SP, 'rev-parse', '--short', 'main')[1].strip() and not g(SP, 'tag', '--list', 'v0.1.2')[1].strip(),
        'v0.1.1 %s' % tg, '4')
    # ### (R298)(6): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (6)', 'data/b687_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b687_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R298)(8)-(9)
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b687_worklist.py')) or ''), 'tools/b687_worklist.py', '6')
    for f in ('b679_strip_plan.txt', 'b676_strip_uses.txt'):
        add('ruling (9)', 'data/%s for b689`s plan' % f, os.path.exists(p('data', f)), 'exists', '6')
    sp_ = rd(p('data', 'b679_strip_plan.txt')) or ''
    add('ruling (9)', 'b679_strip_plan.txt section 11 (the w = 1 split)', re.search(r'(?m)^== 11\.', sp_) is not None, 'data/b679_strip_plan.txt section 11', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry', 'the four parts (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    for b in ('b688_readfirst.txt', 'b688_lattice_route.txt', 'b688_cut.txt', 'b688_residue_actions.txt', 'b688_tool_repairs.txt'):
        sz = b == 'b688_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b688_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b688_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b688 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b688_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b688_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b688_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b688_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b688."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b688'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b688')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b688)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b688_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
