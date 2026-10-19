# -*- coding: utf-8 -*-
"""b692_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b692's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (2c300355, continued from b689-b691); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed
### at b692.
### Routes: `check` -> data/b692_citation_check.txt (.json) ; `ferry` -> data/b692_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b692 from b691_citation.py's form; this tool writes only the banks named above.
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
import b692_worklist as K   # noqa: E402

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
    # ### the ferry's read-first list
    for f in ('data/b691_closing.txt', 'data/b691_defects.txt', 'data/b691_cut.txt', 'data/b691_correspondence_run_PATHS.txt',
              'data/b691_correspondence_run_RCURVE.txt', 'data/b691_epstein_lines.txt', 'data/b691_orders_triage.txt', 'data/b691_behind.txt',
              'data/b691_arms_added.txt', 'tools/rule_arms.py', 'tools/b678_corrigendum.py', 'data/b690_circuit_spec.txt',
              'data/b691_axioms_SIDE-explicit-formula_after.txt', 'data/b690_nodes_zeta.txt', 'data/b689_runner_SIDE-explicit-formula_run1.txt',
              'data/b518_report.txt', 'data/b691_closing_push_out.txt', 'data/b675_corrigenda.txt', 'data/b676_strip_uses.txt',
              'data/b681_epstein_zeros_narrowed.json.gz', 'data/b680_rules.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    head = (rd(p('data', 'b691_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b691_closing.txt :1', head == ('b691 closed: relay 62a530c6, PLACE-papers 9a0dc76; suite 119 of 121; '
                                                                                   'root 7b052f8b5968b799\u2026; 4 prompts answered; 11 defects'), head[:120], '1')
    po = rd(p('data', 'b691_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing f5318624 pushed and read back', '62a530c6..f5318624' in po and 'read back at the remote: f53186249e37' in po,
        'data/b691_closing_push_out.txt', '0-1')
    add('ruling (1)', 'the root`s control holding', 'THE ONE-BYTE CONTROL CHANGES IT True' in (rd(p('data', 'b691_root_arm.txt')) or ''), 'data/b691_root_arm.txt', '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15012', (line(OT, 15012) or '').startswith('### b691 — lane two'), (line(OT, 15012) or '')[:50], '1')
    add('ruling (1)', 'the components bank N1-N5 HELD', all(('N%d HELD' % i) in (rd(p('data', 'b691_components.txt')) or '') for i in range(1, 6)),
        'data/b691_components.txt', '1')
    for f in ('b691_checks.txt', 'b691_checks_postpush.txt'):
        add('ruling (1)', 'suite 119 of 121 (%s)' % f, 'ARMS RUN : 121. ### LIVE PASSING : 119. ### LIVE FAILING : 2' in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    add('ruling (1)', 'the chain b624 through b691 AGREE', 'b624 AGREE' in (rd(p('data', 'b691_checks_standing-b2.txt')) or '')
        and 'b691 AGREE' in (rd(p('data', 'b691_checks_standing-b2.txt')) or ''), 'data/b691_checks_standing-b2.txt', '1')
    add('ruling (1)', 'the table 0 moved, added, gone', 'rows added 0 ; rows gone 0 ; grade-or-profile changed 0' in (rd(p('data', 'b691_checks_act.txt')) or ''),
        'data/b691_checks_act.txt', '1')
    add('ruling (1)', 'table_gate PASS', 'table_gate: PASS' in (rd(p('data', 'b691_pp_push_out.txt')) or ''), 'data/b691_pp_push_out.txt', '1')
    sc = jload('b691_scores_close.json')
    add('ruling (1)', 'all eight scores HELD', sc and all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')),
        'data/b691_scores_close.json', '1')
    add('ruling (1)', 'the b691 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b691.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b691_mirror_verify.txt')) or '')
        and 'Act root: b691 7b052f8b' in (rd(p('data', 'b691_mirror.txt')) or ''), 'the zip; data/b691_mirror_verify.txt; data/b691_mirror.txt', '1')
    add('ruling (1)', 'the sealed tools 8 of 8', 'AGREE 8 of 8' in (rd(p('data', 'b691_closing.txt')) or ''), 'data/b691_closing.txt', '1')
    dl = rd(p('data', 'b691_defects.txt')) or ''
    add('ruling (1)', 'eleven defects, (a)-(k), lettered', re.findall(r"^    \(([a-z])\) THE ", dl, re.M) == list('abcdefghijk'), 'data/b691_defects.txt', '1')
    add('ruling (1)', 'the declared failure the face names', 'G-RULE-ONE-GIT-WRITE carried failing, as the face declares' in (rd(p('data', 'b691_closing.txt')) or ''),
        'data/b691_closing.txt :244-:245', '1')
    for f, nd in (('b691_cut.txt', 'THE DISTANCE BEFORE 2, AFTER 0 ; TAG v0.1.1'), ('b691_correspondence_run_PATHS.txt', 'LINES CHANGED 3'),
                  ('b691_correspondence_run_RCURVE.txt', 'LINES CHANGED 1'), ('b691_epstein_cut.txt', 'v0.34.1'),
                  ('b691_orders_triage.txt', 'ORDERS 35 ; CARRY 11 ; DISCHARGED-BY-READING 24 ; RETIRE 0'), ('b691_arms_added.txt', 'ARMS ADDED 4')):
        add('ruling (1)', 'the weight line`s bank %s' % f, nd in (rd(p('data', f)) or ''), 'data/%s verdict' % f, '1')
    # ### (R302)(1)(i)-(ii), (2)
    ra = (line(p('tools', 'rule_arms.py'), 268) or '')
    add('ruling (1)(i); (2)', 'the pattern at tools/rule_arms.py :268', r"\bstanding-[a-z]\b" in ra, ra.strip()[:90], '1')
    add('ruling (1)(ii)', 'cb6b7ef and 9a0dc76, the tree 26892785 unchanged', g(PP, 'rev-parse', 'cb6b7ef^{tree}')[1].strip().startswith('26892785')
        and g(PP, 'rev-parse', '9a0dc76^{tree}')[1].strip().startswith('26892785'), 'git rev-parse in PLACE-papers', '1')
    add('ruling (2)', 'tools/b678_corrigendum.py, b678`s form (its _quote) and b690`s generated entry', 'def _quote(f, ln, s):' in (rd(p('tools', 'b678_corrigendum.py')) or '')
        and os.path.exists(p('tools', 'b690_corrigendum.py')), 'tools/b678_corrigendum.py :82; tools/b690_corrigendum.py', '1')
    add('ruling (2)', 'the corrigenda bank', 'corrigend' in (rd(p('data', 'b675_corrigenda.txt')) or '').lower(), 'data/b675_corrigenda.txt', '1')
    # ### (R302)(3)
    add('ruling (3)', 'W-ORD-CIRCUIT-READING at OPEN_TRAILS :14980', 'W-ORD-CIRCUIT-READING' in (line(OT, 14980) or ''), 'OPEN_TRAILS :14980', '2-3')
    add('ruling (3)', 'the spec, nine rows', len(re.findall(r'^  [A-Z-]+\s+reads: ', rd(p('data', 'b690_circuit_spec.txt')) or '', re.M)) == 9,
        'data/b690_circuit_spec.txt :10-:48', '3')
    add('ruling (3)(a)', 'b676`s form (the trivium cut bank)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    add('ruling (3)(a)', 'v0.34 = 8fbc27b; main e5fcda7 = v0.34.1, docstrings since', g(EF, 'rev-parse', 'v0.34^{commit}')[1].startswith('8fbc27b')
        and g(EF, 'rev-parse', 'v0.34.1^{commit}')[1].startswith('e5fcda7') and g(EF, 'rev-parse', 'main')[1].startswith('e5fcda7'),
        'SIDE-explicit-formula rev-parse', '2')
    add('ruling (3)(a)', 'main`s tree built by b691`s after run', g(EF, 'rev-parse', 'main^{tree}')[1].strip() == g(EF, 'rev-parse', 'c5aa058^{tree}')[1].strip()
        and 'id 39312568167' in (rd(p('data', 'b691_runner_SIDE-explicit-formula_after.txt')) or ''), 'main^{tree} = c5aa058^{tree} ; run 39312568167', '2')
    add('ruling (3)(a)', 'the workflow file', g(EF, 'cat-file', '-e', 'main:.github/workflows/build-module.yml')[0] == 0, '.github/workflows/build-module.yml', '2')
    add('ruling (3)(a)', 'b689`s dispatch time', '2026-10-19T12:54:35Z to 2026-10-19T13:01:29Z' in (line(p('data', 'b689_runner_SIDE-explicit-formula_run1.txt'), 4) or ''),
        'data/b689_runner_SIDE-explicit-formula_run1.txt :4', '0')
    nz = rd(p('data', 'b690_nodes_zeta.txt')) or ''
    add('ruling (3)(a)', 'the faces kernels by row: kernel rows and @corr SIDE-lv-conservation', ' | kernel | ' in nz
        and '@corr SIDE-lv-conservation' in (line(p('data', 'b690_nodes_zeta.txt'), 126) or ''), 'data/b690_nodes_zeta.txt :94, :126', '2')
    add('ruling (3)(a)', 'SIDE-lv-conservation at v0.13.0 with a workflow', g(LV, 'rev-parse', 'v0.13.0^{commit}')[1].startswith('8e3bc76')
        and g(LV, 'cat-file', '-e', 'main:.github/workflows/build-module.yml')[0] == 0, 'D:/SIDE-lv-conservation', '2')
    for nm, path, ln in (('Wide.li_nonneg_cfg_imp_online_ne_zero', 'SIDEExplicitFormula/Schema/Wide/StripFree.lean', 157),
                         ('Wide.HCount', 'SIDEExplicitFormula/Schema/Wide/Config.lean', 49), ('h2_sign_iff_rh', 'SIDEExplicitFormula/Seam.lean', 101),
                         ('li_nonneg_imp_rh_native', 'SIDEExplicitFormula/LiConverseNative.lean', 27),
                         ('positivity_implies_RH', 'Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', 413)):
        src = (g(EF, 'show', 'main:' + path)[1].split(NL) + [''] * 500)[ln - 1]
        add('ruling (3)(b)-(c)', nm, nm.split('.')[-1] in src, 'main:%s :%d' % (path, ln), '3')
    add('ruling (3)(b)', 'the faces page`s premise column', 'premises' in (line(os.path.join(PP, K.FACES_PAGE), 3) or ''), 'the faces page :3', '3')
    add('ruling (3)(c)', 'circuit-shorts-control-b692 not yet a branch', not branch_listed(EF, 'circuit-shorts-control-b692'), 'git branch --list', '3')
    add('ruling (3)(d)', 'the defects series b673-b691', all(os.path.exists(p('data', 'b%d_defects.txt' % a)) for a in range(673, 692)), 'data/bNNN_defects.txt', '3')
    ins = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
    add('ruling (3)(e)', 'INSTRUMENTS.md`s entry form', (line(ins, 472) or '').startswith('## I-37') and (line(ins, 474) or '').startswith('**Reads.**')
        and (line(ins, 480) or '').startswith('## I-39'), 'phase1.5/method/INSTRUMENTS.md :472-:474, :480', '4')
    # ### (R302)(4)-(5)
    add('ruling (4)', 'the triage bank`s classes', 'RETIRE 0' in (rd(p('data', 'b691_orders_triage.txt')) or ''), 'data/b691_orders_triage.txt :151 (no RETIRE row)', '4')
    add('ruling (5)', 'W-ORD-EPSTEIN-COUNT-LEAN at OPEN_TRAILS :14892', 'W-ORD-EPSTEIN-COUNT-LEAN' in (line(OT, 14892) or ''), 'OPEN_TRAILS :14892', '6')
    add('ruling (5)(i)', 'b518`s two-property window, none negative', 'P - PR + A negative beyond B (verified) : NONE' in (rd(p('data', 'b518_report.txt')) or '')
        and 'VERIFIED-EST 119 of 119' in (rd(p('data', 'b518_report.txt')) or ''), 'data/b518_report.txt :126-:127', '6')
    su = rd(p('data', 'b676_strip_uses.txt')) or ''
    add('ruling (5)(ii)', 'b676`s strip-uses form (rows are uses; the three classes DISCHARGED / RE-PROVED / OBSTRUCTED are the ruling`s own, '
        'not b676`s)', 'rows are uses: file :line' in su and 'USES 22' in su, 'data/b676_strip_uses.txt :6-:7, :46', '6')
    # ### (R302)(6): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    for repo, b in (('D:/SIDE-rcurve', 'push-b691-main'), ('D:/SIDE-rcurve', 'push-b691-merge'), ('D:/SIDE-rcurve', 'recut-rcurve-b691'),
                    (EF, 'push-b691-epstein-main'), (EF, 'push-b691-epstein-merge'), (EF, 'recut-epstein-b691')):
        add('ruling (6)', 'the kernel branch %s %s (for the prompt)' % (os.path.basename(repo), b), branch_listed(repo, b),
            'git branch --list ; data/b691_cut.txt :5, data/b691_epstein_cut.txt :23, data/b691_closing.txt :240-:242', '0')
    add('ruling (6)', 'data/b691_closing_push_out.txt committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b691_closing_push_out.txt')[0] == 0,
        'tracked (relay 2fb05eaa)', '0')
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b692_worklist.py')) or ''), 'tools/b692_worklist.py', '5')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '2-5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C6', 'rule (1) of data/b690_rules.txt', 'Binds from b691.' in (rd(p('data', 'b690_rules.txt')) or ''), 'data/b690_rules.txt :5-:7', '6')
    add('ruling (9)', 'rule (2) of data/b690_rules.txt (b693`s re-cut)', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '6')
    for b in ('b692_readfirst.txt', 'b692_rules.txt', 'b692_tool_repairs.txt', 'b692_circuit_spec.txt'):
        sz = b == 'b692_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b692_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b692_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b692 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b692_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b692_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b692_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b692_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b692."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b692'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b692')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b692)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b692_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
