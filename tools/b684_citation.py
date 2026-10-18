# -*- coding: utf-8 -*-
"""b684_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b684's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling; the answer route is
### b682's, imported from tools/b682_citation.py with its act names pointed at b684; the rows and the banks are b684's.
### Routes: `check` -> data/b684_citation_check.txt (.json) ; `ferry` -> data/b684_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b684 from b683_citation.py's form; this tool writes only the banks named above.
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
C.ANCHOR, C.TAIL = 'RULING (R294) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection', 'D:/SIDE-window', 'D:/SIDE-trivium', 'D:/SIDE-class-number-anomaly')
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
    for f in ('data/b683_closing.txt', 'data/b683_defects.txt', 'data/b683_map_h.txt', 'data/b683_landing.txt', 'data/b683_arms_sort.txt',
              'data/b680_rules_arms.txt', 'data/b683_rules_arms.txt', 'tools/rule_arms.py', 'data/b683_arms_prerun.txt', 'data/b683_checks.txt',
              'data/b683_checks_postpush.txt', 'data/b675_rules.txt', 'data/b670_licensed_table.txt', 'data/b647_table_kernels.txt',
              'data/b674_rules.txt', 'data/b674_cut.txt', 'data/b676_cut.txt', 'data/b678_cut.txt', 'data/b674_axioms_SIDE-window_after.txt',
              'data/b676_axioms_SIDE-trivium_after.txt', 'data/b678_axioms_SIDE-silence-principle_after.txt', 'tools/correspondence_gen.py',
              'data/b683_closing_push_out.txt', 'data/b647_table_SIDE-window.txt', 'data/b647_table_SIDE-trivium.txt',
              'data/b647_table_SIDE-silence-principle.txt', 'data/b652_ferry.txt', 'data/b675_hypotheses.txt', 'data/b667_epstein_plan.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    # ### (R294)(1): b683 at its weight
    head = (rd(p('data', 'b683_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line at data/b683_closing.txt :1', head == ('b683 closed: relay c8fc7848, PLACE-papers 31746ff; suite 111 of 111; root '
                                                                         '5fd5cba8d91b028a\u2026; 2 prompts answered; 1 defect'), head[:110], '1')
    po = rd(p('data', 'b683_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay f38ed009', 'c8fc7848..f38ed009' in po and 'read back at the remote: f38ed009' in po,
        'data/b683_closing_push_out.txt', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'c8fc7848', 'b683 record'), (ROOT, 'relay', 'f38ed009', 'b683 closing'),
                                  (PP, 'PLACE-papers', '31746ff', 'b683 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    mt = rd(p('data', 'b683_map.txt')) or ''
    add('ruling (1)', '123 of 123 controls PASS', 'ROWS 123 (the b671 list: 41 + 41 + 41) ; NONE DROPPED True' in mt and mt.count('; PASS       ;') == 123,
        'data/b683_map.txt', '1')
    mh = rd(p('data', 'b683_map_h.txt')) or ''
    add('ruling (1)', 'H1-H5 HELD; the radius 2.073e-09 and 2.063e-09; H3 j0 = 38', 'H1 HELD ; H2 HELD ; H3 HELD ; H4 SCORABLE HELD ; H5 HELD' in mh
        and '200 bits 2.073e-09, 400 bits 2.063e-09' in mh and 'j₀ = 38' in mh, 'data/b683_map_h.txt', '1')
    add('ruling (1)', 'the zero side [-7.5709710957e+39 +/- 2.4e+23]', '[-7.570971095704516e+39 +/- 2.40e+23]' in mh, 'data/b683_map_h.txt :6 (the ruling rounds it)', '1')
    add('ruling (1)', 'P3 stated, not proved, in the hA row', 'BY P3 (Q0Count, a named premise, stated, not proved; open)' in (rd(p('data', 'b683_map_run.txt')) or ''),
        'data/b683_map_run.txt :176 (the hA line)', '1')
    add('ruling (1)', 'the sealed b677 map b21f6926 and the chain 7 of 7', 'b21f6926' in (rd(p('data', 'b683_map_plan.txt')) or '')
        and 'FILES 7 EQUAL 7' in (rd(p('data', 'b683_chain.txt')) or ''), 'data/b683_map_plan.txt; data/b683_chain.txt', '1')
    for n, needle in ((14774, 'W-ORD-MAP-ANGLE-FORM'), (14776, '### b683')):
        lt = line(OT, n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in lt, lt[:70], '1')
    for n, needle in ((9168, 'b682'), (9170, '## The detection map in the angle form')):
        lt = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in lt, lt[:70], '1')
    ra = rd(p('data', 'b683_rules_arms.txt')) or ''
    add('ruling (1)', 'twenty arms; NONE 3 of 24', 'NONE NOW 3' in ra and 'ARMED NOW BY THE WORD 20' in ra, 'data/b683_rules_arms.txt', '1')
    add('ruling (1)', 'rule_arms.py sealed with b683', 'rule_arms.py' in json.dumps((json.load(open(p('data', 'b683_seal_hashes.json'))) or {}).get('tools', {})),
        'data/b683_seal_hashes.json', '1')
    face = rd(p('data', 'b683_registration_2026-10-18.txt')) or ''
    add('ruling (1)', 'seven VACUOUS rule arms on the face', face.count('-- VACUOUS') == 7, 'data/b683_registration_2026-10-18.txt (G2)', '1')
    dl = rd(p('data', 'b683_defects.txt')) or ''
    add('ruling (1)', 'one defect (a), the seat`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [('a', 'SEAT')], 'data/b683_defects.txt :5', '1')
    add('ruling (1)', 'five repairs', 'REPAIRS 5 ; THE SEALED COPIES AGREE' in (rd(p('data', 'b683_tool_repairs.txt')) or ''), 'data/b683_tool_repairs.txt', '1')
    add('ruling (1)', 'standing-a 565 s at the pre-run, 893 MB', 'standing-a : ARMS 87 ; 565 s' in (rd(p('data', 'b683_arms_prerun.txt')) or '')
        and '893 MB' in face, 'data/b683_arms_prerun.txt; the face', '1')
    add('ruling (1)', 'standing-a at b682`s pre-run 180 s', 'standing-a : ARMS 67 ; 180 s' in (rd(p('data', 'b682_arms_prerun.txt')) or ''), 'data/b682_arms_prerun.txt', '1')
    add('ruling (1)', 'the b683 mirror made', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-18-b683.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b683_mirror_verify.txt')) or ''), 'the zip and data/b683_mirror_verify.txt', '0')
    add('ruling (1)', 'root 5fd5cba8 in the chain', any(r[1].startswith('5fd5cba8') for r in act_root_line('b683')), 'data/act_roots.txt', '1')
    # ### (R294)(2): the split, on b675 row 2
    r2 = (rd(p('data', 'b675_rules.txt')) or '')
    pr = rd(p('data', 'b683_arms_prerun.txt')) or ''
    ph = [int(x) for x in re.findall(r'THE LONGEST PHASE (\d+) s', pr)]
    add('ruling (2)', 'data/b675_rules.txt row 2: "a pre-run whose longest phase exceeds 450 s is split" -- b683`s pre-run`s longest PHASE',
        max(ph or [0]) > 450, 'the phases %s s (data/b683_arms_prerun.txt); the PART standing-a 565 s exceeds 450 s, no PHASE does -- the rule row`s trigger '
        'is a phase, the ruling`s figure a part' % ph, '1, 4')
    add('ruling (2)', 'the hold 2560 MB on every host', 'HOLD_MB: "2560"' in (C.rd(os.path.join('D:/SIDE-bijection', '.github', 'workflows', 'build-module.yml')) or ''),
        'SIDE-bijection`s workflow; tools/b684_worklist.py HOLD', '4')
    # ### (R294)(3): the next document
    lt = rd(p('data', 'b670_licensed_table.txt')) or ''
    for n, k in ((103, 'SIDE-class-number-anomaly'), (111, 'SIDE-li-map'), (116, 'SIDE-spinor')):
        add('ruling (3)', 'the licensed table :%d %s at 3' % (n, k), (k + ' docstrings') in (line(p('data', 'b670_licensed_table.txt'), n) or '')
            and '3 ->    3' in (line(p('data', 'b670_licensed_table.txt'), n) or ''), (line(p('data', 'b670_licensed_table.txt'), n) or '').strip()[:80], '2')
    add('ruling (3)', 'b674`s tie-break rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8', '2')
    add('ruling (3)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '2')
    add('ruling (3)', 'correspondence_gen.py`s runner-bank reader', 'AX_NAME = re.compile' in (rd(p('tools', 'correspondence_gen.py')) or ''),
        'tools/correspondence_gen.py', '2')
    # ### (R294)(4): the residues
    for f, a_, b_, needle in (('data/b674_cut.txt', 27, 33, 'does not reach it'), ('data/b676_cut.txt', 35, 43, 'does not reach them'),
                              ('data/b678_cut.txt', 38, 45, 'does not reach it'), ('data/b678_cut.txt', 52, 58, 'reach it')):
        blk = ' '.join((line(p(*f.split('/')), n) or '') for n in range(a_, b_ + 1))
        add('ruling (4)', '%s :%d-:%d, the residue row with its unreached sentence' % (f, a_, b_), needle in blk, ' '.join(blk.split())[:90], '3')
    add('ruling (4)', 'SIDE-window`s Sawtooth header marker at :17', '"(a) ... S_k acts on' in ' '.join((line(p('data', 'b674_cut.txt'), n) or '') for n in (28,))
        and 'the marker at :17' in (line(p('data', 'b674_cut.txt'), 28) or ''), 'data/b674_cut.txt :28', '3')
    add('ruling (4)', 'SIDE-trivium`s "correspond exactly"', '"correspond' in ' '.join((line(p('data', 'b676_cut.txt'), n) or '') for n in (38, 39)),
        'data/b676_cut.txt :38-:39 (the introduction`s "correspond exactly" (:8) and :23)', '3')
    add('ruling (4)', 'SIDE-silence-principle`s Theorem 8.1 title and header introduction', 'Theorem 8.1 (Silence yields Protection)' in
        (rd(p('data', 'b647_table_SIDE-silence-principle.txt')) or '') and 'named here as this act' in (line(p('data', 'b678_cut.txt'), 45) or ''),
        'data/b647_table_SIDE-silence-principle.txt :26; data/b678_cut.txt :41-:45', '3')
    for f, n in (('data/b647_table_SIDE-window.txt', 19), ('data/b647_table_SIDE-trivium.txt', 14), ('data/b647_table_SIDE-silence-principle.txt', 14),
                 ('data/b647_table_SIDE-silence-principle.txt', 29)):
        add('ruling (4)', '%s :%d, the row`s b647 ACTION' % (f, n), 'ACTION   RE-CUT' in (line(p(*f.split('/')), n) or ''), (line(p(*f.split('/')), n) or '').strip()[:70], '3')
    for k, tag in (('SIDE-window', 'v0.5.1'), ('SIDE-trivium', 'v0.1.1'), ('SIDE-silence-principle', 'v0.2.1')):
        tc = g('D:/' + k, 'rev-parse', tag + '^{commit}')[1].strip()
        add('ferry read-first', '%s %s at main' % (k, tag), bool(tc) and tc == g('D:/' + k, 'rev-parse', 'main')[1].strip(), tc[:12], '3')
    # ### (R294)(5): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b683-root', 'push-b683', 'push-b683-closing')), (PP, 'PLACE-papers', ('push-b683-root', 'push-b683'))):
        for b in bs:
            add('ruling (5)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (5)', 'data/b683_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b683_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R294)(7)-(8)
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b683_worklist.py')) or ''), 'tools/b683_worklist.py', '5')
    add('ruling (8)', 'P3 in data/b675_hypotheses.txt', 'P3' in (rd(p('data', 'b675_hypotheses.txt')) or ''), 'data/b675_hypotheses.txt', '5')
    add('ruling (8)', 'N(R) = 180 and the (3c) bound in the b667 plan', '180' in (rd(p('data', 'b667_epstein_plan.txt')) or '') and '(3c)' in (rd(p('data', 'b667_epstein_plan.txt')) or ''),
        'data/b667_epstein_plan.txt', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1, the closing a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''),
        'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '5')
    for b in ('b684_readfirst.txt', 'b684_rules.txt', 'b684_cut.txt', 'b684_residue_actions.txt', 'b684_tool_repairs.txt'):
        sz = b == 'b684_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b684_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b684_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b684 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b684_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b684_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b684_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b684_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b684."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b684'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b684')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b684)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b684_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
