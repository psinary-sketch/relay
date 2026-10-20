# -*- coding: utf-8 -*-
"""b693_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b693's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (2c300355, continued from b689-b692); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed
### at b693.
### Routes: `check` -> data/b693_citation_check.txt (.json) ; `ferry` -> data/b693_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b693 from b692_citation.py's form; this tool writes only the banks named above.
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
import b693_worklist as K   # noqa: E402

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
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    # ### the ferry's read-first list
    for f in ('data/b692_closing.txt', 'data/b692_defects.txt', 'data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt', 'data/b692_circuit_bars.txt',
              'data/b692_circuit_dominance.txt', 'data/b692_circuit_controls.txt', 'data/b692_circuit_shorts_branch.txt', 'data/b692_circuit_spec.txt',
              'data/b692_readfirst_diff.txt', 'data/b692_suite_load.txt', 'data/b692_parts_probe.txt', 'data/b692_tool_repairs.txt',
              'tools/b692_record.py', 'tools/b692_closing.py', 'tools/push_gated.sh', 'tools/rule_arms.py', 'data/b670_licensed_table.txt',
              'data/b674_rules.txt', 'data/b690_rules.txt', 'data/b684_rules.txt', 'data/b691_cut.txt', 'tools/correspondence_gen.py',
              'data/b692_closing_push_out.txt', 'tools/b692_corrigendum.py', 'tools/b678_corrigendum.py', 'data/b675_corrigenda.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R303)(1)
    head = (rd(p('data', 'b692_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b692_closing.txt :1', head == ('b692 closed: relay cb41d267, PLACE-papers 62b632f; suite 123 of 123; '
                                                                                   'root f0fd28492c58f143\u2026; 4 prompts answered; 13 defects'), head[:120], '1')
    po = rd(p('data', 'b692_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay 1749abbb', 'cb41d267..1749abbb' in po and 'read back at the remote: 1749abbb68be' in po,
        'data/b692_closing_push_out.txt', '0-1')
    for f in ('b692_checks.txt', 'b692_checks_postpush.txt'):
        t = rd(p('data', f)) or ''
        add('ruling (1)', 'suite 123 of 123, every control behaving (%s)' % f, 'ARMS RUN : 123. ### LIVE PASSING : 123. ### LIVE FAILING : 0' in t
            and 'NEGATIVE-CONTROL FAILURES : 0. ### POSITIVE-CONTROL PASSES : 0' in t, 'data/%s' % f, '1')
    sc = jload('b692_scores_close.json')
    add('ruling (1)', 'all eight scores HELD', sc and all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')),
        'data/b692_scores_close.json', '1')
    ar = act_root_line('b692')
    add('ruling (1)', 'the root f0fd2849 over 88 banks', ar and ar[0][1].startswith('f0fd2849') and len([i for i in jload('b692_act_root.json').get('items', [])
                                                                                                       if i.split()[0].startswith('data/')]) == 88,
        'data/act_roots.txt ; data/b692_act_root.json items naming data/', '1')
    add('ruling (1)', 'the entry at FINDINGS :9462', (line(FI, 9462) or '').startswith('## The dependency-circuit reading'), (line(FI, 9462) or '')[:60], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15110 carrying the root', (line(OT, 15110) or '').startswith('### b692 — lane two')
        and 'f0fd28492c58f14334b1716c4fad0f9b6720223858c57311578219e7072eb5f0' in (rd(OT) or '').split(NL, 15110)[-1][:20000],
        'OPEN_TRAILS :15110 and its Act root line', '1')
    add('ruling (1)', 'the gate CLEAR and 8 of 8 lock gates, no arm declared failing', 'GATE VERDICT : CLEAR' in (rd(p('data', 'b692_reg_gate.txt')) or '')
        and 'GATES READ : 8. ### PASSING : 8.' in (rd(p('data', 'b692_lockgate_notes.txt')) or '')
        and 'DECLARED BEFORE THE LOCK, BY NAME:** NONE.' in (rd(p(*K.B692_FACE.split('/'))) or ''),
        'data/b692_reg_gate.txt ; data/b692_lockgate_notes.txt :65 ; the face', '1')
    add('ruling (1)', '12 sealed tools agreeing at the close', 'AGREE 12 of 12' in (line(p('data', 'b692_closing.txt'), 18) or ''), 'data/b692_closing.txt :18', '1')
    add('ruling (1)', 'the b692 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b692.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b692_mirror_verify.txt')) or '')
        and 'Act root: b692 f0fd2849' in (rd(p('data', 'b692_mirror.txt')) or ''), 'the zip; data/b692_mirror_verify.txt; data/b692_mirror.txt', '1')
    add('ruling (1)', 'circuit-shorts-control-b692 deleted local and remote, -D', 'local GONE ; remote GONE ; DELETED' in (line(p('data', 'b692_closing.txt'), 224) or '')
        and not branch_listed('D:/SIDE-explicit-formula', 'circuit-shorts-control-b692'), 'data/b692_closing.txt :224 ; git branch --list', '1')
    tc = rd(p('data', 'b692_triage_counts.txt')) or ''
    heads = [x.get('head') or '' for x in jload('b692_orders_lines.json').get('lines') or []]
    n_c, n_d = sum(1 for h in heads if '` CARRIED (' in h), sum(1 for h in heads if '` DISCHARGED BY READING (' in h)
    add('ruling (1)', 'the triage WRITTEN TO OPEN_TRAILS as CARRY 11 and DISCHARGED-BY-READING 24, RETIRE 0', (n_c, n_d) == (11, 24),
        'the triage bank`s classes CARRY 11, DISCHARGED-BY-READING 24 (data/b692_triage_counts.txt :6); the OPEN_TRAILS entries written '
        'CARRIED %d, DISCHARGED BY READING %d (data/b692_orders_lines.json heads; OPEN_TRAILS :15040-:15108), one row demoted on the author`s check '
        '(W-ORD-PROBE-HOLD; data/b692_author_answers.txt prompt 4)' % (n_c, n_d), '1')
    add('ruling (1)', 'the triage bank`s classes CARRY 11, DISCHARGED-BY-READING 24, RETIRE 0', 'CARRY 11 ; DISCHARGED-BY-READING 24 ; RETIRE 0' in tc,
        'data/b692_triage_counts.txt :6', '1')
    rb = line(p('data', 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt'), 707) or ''
    add('ruling (1)', 'LOAD`s three highest, Zeta23.reflect 825, Zeta23.ZeroConfig.mk 716, Zeta23.ZeroConfig 716', 'LOAD`S THREE HIGHEST Zeta23.reflect (825), '
        'Zeta23.ZeroConfig.mk (716), Zeta23.ZeroConfig (716)' in rb and 'Zeta23.reflect (825)' in (rd(p('data', 'b692_defects.txt')) or ''),
        'data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt :707 ; data/b692_defects.txt (m) :55, :59-:60', '1')
    for f, nd in (('b692_circuit_dominance.txt', 'CLAUSE-DOMINANCE 1 OF 1 FACES KERNELS REACHED'), ('b692_readfirst_diff.txt', 'LINES DIFFERING 23'),
                  ('b692_suite_load.txt', 'THE FACTOR 1.53'), ('b692_circuit_controls.txt', 'SHORTS 0'),
                  ('b692_circuit_spec.txt', 'SUITE-LOAD'), ('b692_closure_step.txt', 'SIDE-lv-conservation')):
        add('ruling (1)', 'the circuit figure`s bank %s' % f, nd in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    dl = rd(p('data', 'b692_defects.txt')) or ''
    add('ruling (1)', 'thirteen defects, (a)-(m), lettered', re.findall(r"^    \(([a-z])\) THE ", dl, re.M) == list('abcdefghijklm'), 'data/b692_defects.txt', '1')
    add('ruling (1)', '(m): "LOAD led by ." and "1.53. --" in the entry at :9462', 'LOAD led by .' in (rd(FI) or '') and '1.53. --' in (rd(FI) or ''),
        'FINDINGS.md, the entry`s readings and SUITE-LOAD paragraphs', '1')
    add('ruling (1)', 'the closing record`s carried-forward row (i) reading "(a)-(k)"', '(i) The defects (a)-(k)' in (line(p('data', 'b692_closing.txt'), 258) or ''),
        'data/b692_closing.txt :258', '1')
    # ### (R303)(2)
    add('ruling (2)', 'the corrigendum tool in b678`s form (its _quote), b692`s generated entry', 'def _quote(f, ln, s):' in (rd(p('tools', 'b678_corrigendum.py')) or '')
        and os.path.exists(p('tools', 'b692_corrigendum.py')), 'tools/b678_corrigendum.py ; tools/b692_corrigendum.py', '1')
    rec = rd(p('tools', 'b692_record.py')) or ''
    clo = rd(p('tools', 'b692_closing.py')) or ''
    add('ruling (2); ferry', 'THE RECORD TOOL`s carried-forward defects row from a fixed string', '(a)-(k)' in rec,
        'tools/b692_record.py carries no "(a)-(k)" and writes no carried-forward row; the fixed string is the CLOSING tool`s, tools/b692_closing.py :115 '
        '(found there %s)' % ("'    (i) The defects (a)-(k) for the next ruling" in clo), '1')
    add('ruling (2)', 'push_gated.sh: the main and existing-tag modes, no branch mode', (line(p('tools', 'push_gated.sh'), 4) or '').startswith('# usage: push_gated.sh <repo> <push-branch>')
        and '--existing-tag <tag>' in (line(p('tools', 'push_gated.sh'), 44) or '') and 'branch mode' not in (rd(p('tools', 'push_gated.sh')) or ''),
        'tools/push_gated.sh :4, :44', '1')
    add('ruling (2)', 'b691`s defect (d), the cut branches pushed outside the push tool', 'THE CUT BRANCHES PUSHED OUTSIDE THE PUSH TOOL' in (line(p('data', 'b691_defects.txt'), 24) or ''),
        'data/b691_defects.txt :24', '1')
    add('ruling (2)', 'the b692 exception as entered, (i)', "A RULED EXCEPTION AND NOT A SLIP" in (line(p('data', 'b692_defects.txt'), 36) or ''), 'data/b692_defects.txt :36', '1')
    # ### (R303)(3)
    add('ruling (3)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '2')
    add('ruling (3)', 'b674`s tie-break rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '2')
    add('ruling (3)', 'the licensed table`s per-document rows (b648 -> now)', 'PER AGENDA DOCUMENT' in (line(p('data', 'b670_licensed_table.txt'), 89) or ''),
        'data/b670_licensed_table.txt :89-:123', '2')
    add('ruling (3)', 'b676`s form (the trivium cut bank)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    add('ruling (3)', 'rule (2) of data/b690_rules.txt', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '2')
    add('ruling (3)', 'the :301 residue, carry v1.3 = 0bc21c0 against v1.8', 'PATHS_TO_THE_CRITICAL_LINE_v0_7.md :301' in (line(p('data', 'b691_cut.txt'), 22) or '')
        and 'v1.3 = 0bc21c0' in (line(p('data', 'b691_cut.txt'), 26) or ''), 'data/b691_cut.txt :22-:27', '2')
    add('ruling (3)', 'the generator as repaired at b691 (read_carry, CARRIED AT: VERSION DIFFERS)', 'def read_carry(carrier, version, k):' in (rd(p('tools', 'correspondence_gen.py')) or ''),
        'tools/correspondence_gen.py :247, :389', '2')
    # ### (R303)(4)
    pb = rd(p('data', 'b692_arms_prerun_standing-b2.txt')) or ''
    add('ruling (4)', 'the standing-b part ran 461 s at b692`s pre-run (the family`s part standing-b2, the act-root chain)', 'PART standing-b2' in pb and '; 461 s' in pb,
        'data/b692_arms_prerun_standing-b2.txt, its footer', '3')
    add('ruling (4)', 'data/b684_rules.txt row (1)', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (line(p('data', 'b684_rules.txt'), 5) or ''), 'data/b684_rules.txt :5-:12', '3')
    add('ruling (4)', 'the V2 family comparison', 'numbered halves' in (line(p('tools', 'rule_arms.py'), 481) or ''), 'tools/rule_arms.py :480-:486', '3')
    add('ruling (4)', 'data/b692_parts_probe.txt read the halves', 'V2' in (rd(p('data', 'b692_parts_probe.txt')) or ''), 'data/b692_parts_probe.txt', '3')
    # ### (R303)(5): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (5)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (5)', 'data/b692_closing_push_out.txt committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b692_closing_push_out.txt')[0] == 0,
        'tracked (relay %s)' % K.STEPZERO, '0')
    # ### (R303)(7)-(8)
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py', '5')
    cp = rd(p('data', 'b692_candidates_priced.txt')) or ''
    add('ruling (8)', 'W-ORD-EPSTEIN-COUNT-LEAN, the Weil-face witness at Q0, the regularity-uses bank priced in (R302)(5)', 'W-ORD-EPSTEIN-COUNT-LEAN' in cp
        and 'WEIL-FACE WITNESS AT Q0' in cp and 'REGULARITY-USES BANK' in cp, 'data/b692_candidates_priced.txt :1, :6, :18', '5')
    add('ruling (8)', 'the faces kernels the circuit step carried', 'SIDE-lv-conservation' in (rd(p('data', 'b692_closure_step.txt')) or ''), 'data/b692_closure_step.txt', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '2-4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C5', 'rule (1) of data/b690_rules.txt', 'Binds from b691.' in (rd(p('data', 'b690_rules.txt')) or ''), 'data/b690_rules.txt :5-:7', '5')
    add('ferry C5', 'rule (1) of data/b692_rules.txt', 'no amend, rebase or rewrite' in (rd(p('data', 'b692_rules.txt')) or '').lower()
        or 'amend' in (rd(p('data', 'b692_rules.txt')) or '').lower(), 'data/b692_rules.txt (1)', '5')
    for b in ('b693_readfirst.txt', 'b693_tool_repairs.txt', 'b693_cut.txt'):
        sz = b == 'b693_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b693_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b693_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b693 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b693_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b693_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b693_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b693_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b693."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b693'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b693')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b693)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b693_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
