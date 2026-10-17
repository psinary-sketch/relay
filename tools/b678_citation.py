# -*- coding: utf-8 -*-
"""b678_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b678's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged (the transcript reader with both apostrophes, git, the line
### reader, the rule-clause reader), its anchor pointed at this act's ruling; the rows, the banks and the routes are b678's: once
### data/act_roots.txt carries b678's root, an answer's print goes to data/b678_defects.txt and to no root-named bank ((R282)(2) row 1); each
### answer cut from BEGIN to END around its needle.
### Routes: `check` -> data/b678_citation_check.txt (.json) ; `ferry` -> data/b678_ferry.txt and data/b678_ferry_scan.txt ;
###         `answer <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b678; this tool writes only the banks named above.
"""
import io
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
KREV = 'e36ea31'
C.ANCHOR, C.TAIL = 'RULING (R288) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause, grep_lines = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed,
                                                                           C.rule_clause, C.grep_lines)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection')
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
    for f in ('data/b677_closing.txt', 'data/b677_defects.txt', 'data/b677_map_h.txt', 'data/b677_tolerance.txt', 'data/b670_work_orders.txt',
              'data/b676_q0_lines.txt', 'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b676_cut.txt', 'data/b674_cut.txt',
              'tools/correspondence_gen.py', 'data/b675_rules.txt', 'data/b677_rules.txt', 'data/b677_closing_push_out.txt',
              'data/b648_recut_order.txt', 'data/b647_table_kernels.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-4')
    tabs = sorted(f for f in os.listdir(D) if re.match(r'^b647_table_.*\.txt$', f))
    add('ferry read-first', 'the per-document tables data/b647_table_*.txt', len(tabs) >= 21, '%d files' % len(tabs), '3')
    # ### (R288)(1): b677 at its weight
    head = (rd(p('data', 'b677_closing.txt')) or '').split(NL)[0]
    quoted = 'b677 closed: relay 7beac43e, PLACE-papers f614597; suite 85 of 85; root cd2137c837efe204\u2026; 2 prompts answered; 9 defects'
    add('ruling (1)', 'the head line quoted at data/b677_closing.txt :1', head == quoted, 'character for character: %s' % (head == quoted), '1')
    for repo, nm, sha, needle in ((ROOT, 'relay', '7beac43e', 'b677 record'), (ROOT, 'relay', 'da8a46bc', 'b677 closing'),
                                  (PP, 'PLACE-papers', 'f614597', 'b677 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s, its subject opening "%s"' % (nm, sha, needle), commit_in(repo, sha) and s.startswith(needle), s[:80], '1')
    po = line(p('data', 'b677_closing_push_out.txt'), 4) or ''
    add('ruling (1)', 'the closing pushed at relay da8a46bc', '7beac43e..da8a46bc' in po, 'data/b677_closing_push_out.txt :4', '0-1')
    for n, needle in ((24, '### THE RUN ((R287)(4)'), (25, 'Q0 at 200 bits'), (28, '### THE TOLERANCE'), (30, '### THE HYPOTHESES')):
        add('ruling (1); ferry', 'data/b677_closing.txt :%d, THE RUN section' % n, (line(p('data', 'b677_closing.txt'), n) or '').lstrip().startswith(needle.lstrip()),
            (line(p('data', 'b677_closing.txt'), n) or '')[:70], '0-1')
    add('ruling (1)', 'the hypotheses at data/b677_map_h.txt :12', 'H1 REFUTED ; H2 REFUTED ; H3 REFUTED ; H4 NOT SCORABLE ; H5 HELD' in (line(p('data', 'b677_map_h.txt'), 12) or ''),
        'data/b677_map_h.txt :12', '0-1')
    add('ruling (1)', 'the tolerance at data/b677_tolerance.txt :86-:87', 'h_tol 3.162e-20' in (line(p('data', 'b677_tolerance.txt'), 86) or '')
        and 'h_tol 3.162e-28' in (line(p('data', 'b677_tolerance.txt'), 87) or ''), 'data/b677_tolerance.txt :86-:87', '0-1')
    for n, nm in ((265, 'W-ORD-MAP-ANGLE-FORM'), (266, 'W-ORD-EPSTEIN-BALL-WIDTH'), (262, 'W-ORD-Q0-CLASS-LINES')):
        add('ruling (1)-(2); ferry', '%s by row at data/b670_work_orders.txt :%d' % (nm, n), (line(p('data', 'b670_work_orders.txt'), n) or '').strip().startswith(nm),
            (line(p('data', 'b670_work_orders.txt'), n) or '').strip()[:90], '0-2')
    dl = rd(p('data', 'b677_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'nine defects (a)-(i), (a)-(d) the navigator`s', [x for x, _o in letters] == list('abcdefghi') and
        [x for x, o in letters if o == 'NAVIGATOR'] == list('abcd'), 'data/b677_defects.txt: %s' % ''.join(x for x, _o in letters), '1')
    add('ruling (1)', 'defect (c): the path data/b663_plan.txt for data/b663_epstein_plan.txt', 'data/b663_plan.txt' in dl and
        not os.path.exists(p('data', 'b663_plan.txt')) and os.path.exists(p('data', 'b663_epstein_plan.txt')), 'data/b677_defects.txt (c)', '1')
    pr = rd(p('data', 'b677_arms_prerun_standing.txt')) or ''
    add('ruling (1)', 'the pre-run`s standing part at 557 s', 'the run took 557 s' in pr, 'data/b677_arms_prerun_standing.txt', '0, 4')
    rl5 = rd(p('data', 'b675_rules.txt')) or ''
    add('ruling (1)', '(R285)(2)`s rule row: data/b675_rules.txt row 2', "(2) A PRE-RUN'S LONG PHASE SPLITS THE NEXT ONE" in rl5, 'data/b675_rules.txt :9', '0, 4')
    add('ruling (1)', 'data/b678_rules.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b678_rules.txt')), 'absent, as ordered', '0')
    # ### (R288)(2): the Q0 lines
    q0 = grep_lines(p('data', 'b676_q0_lines.txt'), r'TO RE-CUT 36 \(ON 35 LINES: FINDINGS 25, OPEN_TRAILS 11')
    add('ruling (2)', '36 sentences on 35 lines, 25 in FINDINGS and 11 in OPEN_TRAILS', q0, 'data/b676_q0_lines.txt :%s' % (q0[0][0] if q0 else None), '2')
    fl = line(FIND, 8881) or ''
    add('ruling (2); ferry', 'FINDINGS :8881, the b675 finding', fl.startswith('## The Li index at Q0'), fl[:70], '2')
    sl = (g(KE, 'show', '%s:Zeta23/Defs.lean' % KREV)[1].split(NL) + [''] * 142)[141]
    add('ruling (2); ferry', 'Zeta23/Defs.lean :142 at e36ea31, the strip field', sl.strip().startswith('strip :'), sl.strip()[:70], '2')
    add('ruling (2)', 'tools/b678_corrigendum.py -- TO BE WRITTEN', not os.path.exists(p('tools', 'b678_corrigendum.py')), 'absent, as ordered', '2')
    ql = line(OT, 14556) or ''
    add('ruling (2)', 'W-ORD-Q0-CLASS-LINES at OPEN_TRAILS :14556', 'W-ORD-Q0-CLASS-LINES' in ql, ql[:70], '2')
    # ### (R288)(3): the next document
    tr = rd(p('data', 'b674_rules.txt')) or ''
    add('ruling (3)', 'the tie-break rule of data/b674_rules.txt', '(2) THE TIE-BREAK BEYOND THE COUNT' in tr and '(2) THE TIE-BREAK' in (line(p('data', 'b674_rules.txt'), 8) or ''),
        'data/b674_rules.txt :8', '3')
    for f, nd in (('b674_cut.txt', 'marker at :17'), ('b676_cut.txt', "SIDE-trivium's header introduction (:8, :23 at v0.1.1)")):
        flat = ' '.join(re.sub(r'(?m)^\s*(?:###\s*)+', '', rd(p('data', f)) or '').split())     # ### banks wrap their cites: read unwrapped
        add('ruling (3)', 'the residue named in data/%s' % f, nd in flat, 'data/%s (read unwrapped)' % f, '3')
    add('ruling (3)', 'tools/correspondence_gen.py', os.path.exists(p('tools', 'correspondence_gen.py')), 'exists', '3')
    for b in ('b678_cut.txt', 'b678_readfirst.txt'):
        sz = b == 'b678_readfirst.txt'
        add('ruling (3), (5)', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-3')
    # ### (R288)(4): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b677', 'push-b677-root', 'push-b677-closing')),
                         (PP, 'PLACE-papers', ('push-b677', 'push-b677-root'))):
        for b in bs:
            add('ruling (4)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (4)', 'data/b677_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b677_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R288)(6)-(7) and the rules
    add('ruling (6)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b677_worklist.py')) or ''), 'tools/b677_worklist.py', '5')
    add('ruling (7)', 'data/b676_strip_uses.txt (22 uses) and LiConverseCfg.lean :231', 'USES 22' in (rd(p('data', 'b676_strip_uses.txt')) or '') and
        ':231' in (rd(p('data', 'b676_strip_uses.txt')) or ''), 'data/b676_strip_uses.txt :46', '5')
    add('ruling (7)', 'W-ORD-EPSTEIN-BALL-WIDTH at the width b677 measured', '3.2·10⁻²⁸' in (line(OT, 14590) or ''), 'OPEN_TRAILS :14590', '5')
    add('ferry C4', 'data/b675_rules.txt row 1, the closing dry-run as a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in rl5, 'data/b675_rules.txt :5', '4')
    add('ferry C4', 'data/b677_rules.txt row 1', '(1) THE SUITE IN TWO FOREGROUND PARTS' in (rd(p('data', 'b677_rules.txt')) or ''), 'data/b677_rules.txt :5', '4')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '2')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    return R


def _write(L, R, miss):
    for name, data in (('b678_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b678_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b678 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    text = C.ferry_text()
    q = os.path.join(D, 'b678_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b678_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b678_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    return bool(act_root_line('b678'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` after this act's ruling, cut from BEGIN to END around it; its relay paths, ledger
    lines and commits checked at HEAD; the print appended to the citation bank, or after the root to the defects bank."""
    best, seen = None, False
    for t in C._user_texts():
        if ANCHOR in t:
            seen = True
        u = t.replace('’', "'")
        if seen and needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION AFTER THE RULING -- NOTHING WRITTEN' % needle)
    k = best.find(needle)
    b0, e0 = best.rfind('BEGIN', 0, k), best.find('END', k)
    if b0 >= 0 and e0 > k:
        best = best[b0:e0 + 3]
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b678_', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b678_defects.txt' if after_root() else 'b678_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it%s:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best),
                            ' (after the root: printed to the defects bank, (R282)(2) row 1)' if after_root() else '')]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k_, w) for k_, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**%s' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                         (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '',
                                                                         ' -- VACUOUS: no cite to check.' if not rows_ else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b678_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
