# -*- coding: utf-8 -*-
"""b680_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b680's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged (the transcript reader with both apostrophes, git, the line
### reader, the rule-clause reader), its anchor pointed at this act's ruling; the rows, the banks and the routes are b680's: once
### data/act_roots.txt carries b680's root, an answer's print goes to data/b680_defects.txt and to no root-named bank ((R282)(2) row 1); each
### answer cut from BEGIN to END around its needle, the word reader admitting a prefixed BEGIN (b679's repair 3).
### Routes: `check` -> data/b680_citation_check.txt (.json) ; `ferry` -> data/b680_ferry.txt and data/b680_ferry_scan.txt ;
###         `answer <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b680 from b679_citation.py's form; this tool writes only the banks named above.
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
C.ANCHOR, C.TAIL = 'RULING (R290) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause, grep_lines = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed,
                                                                           C.rule_clause, C.grep_lines)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection')
SPLIT_README = 'archive/2026-08-24-ledger-split/README.md'
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
    for f in ('data/b679_closing.txt', 'data/b679_defects.txt', 'data/b679_landing.txt', 'data/b679_q0_membership.txt', 'data/b679_onset.txt',
              'data/b675_hypotheses.txt', 'data/b670_rules.txt', 'data/b670_state.txt', 'data/b670_licensed_table.txt', 'data/b670_work_orders.txt',
              'data/b670_methods.txt', 'data/b670_ceiling.txt', 'data/b672_correspondence_after.txt', 'tools/correspondence_gen.py',
              'data/b674_cut.txt', 'data/b676_cut.txt', 'data/b678_cut.txt', 'tools/b679_checks.py', 'data/b671_tie_diagnostic.txt',
              'data/b677_map.txt', 'data/b671_epstein_zeros_narrowed.json.gz', 'data/b671_epstein_zeros_narrowed_hashes.txt',
              'data/b675_li_bench.txt', 'data/b679_closing_push_out.txt', 'tools/chain_page.py', 'data/b677_tolerance.txt',
              'data/b671_narrow_plan.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    rules = sorted(f for f in os.listdir(D) if re.match(r'^b67\d_rules\.txt$', f))
    want = ['b67%d_rules.txt' % i for i in range(0, 10)]
    add('ferry read-first; ruling (5)(ii)', 'every data/b67N_rules.txt, b670 through b679', rules == want,
        'present %s ; absent %s' % (', '.join(x[:4] for x in rules), ', '.join(x[:4] for x in want if x not in rules) or 'NONE'), '3')
    add('ferry read-first; ruling (6)', 'the ledger split`s README (2026-08-24-ledger-split__README.md)', os.path.exists(os.path.join(PP, *SPLIT_README.split('/'))),
        'PLACE-papers %s (the cited name joins the directory and the file with a double underscore)' % SPLIT_README, '4')
    add('ferry read-first; ruling (6)', 'the split tool by its path', os.path.exists(p('tools', 'ledger_split.py')), 'relay tools/ledger_split.py (b143)', '4')
    # ### (R290)(1): b679 at its weight
    head = (rd(p('data', 'b679_closing.txt')) or '').split(NL)[0]
    quoted = ('b679 closed: relay 6b2a8f78, PLACE-papers 3e375cb, SIDE-explicit-formula 95f8dc8 v0.33; suite 89 of 89; root 5046df1d…; 3 prompts '
              'answered; 5 defects')
    add('ruling (1)', 'the head line at data/b679_closing.txt :1', head.replace('5046df1d1fc69df6…', '5046df1d…') == quoted,
        'equal with the root`s printed prefix 5046df1d1fc69df6… read as the ruling`s 5046df1d…: %s ; the line: %s' % (
            head.replace('5046df1d1fc69df6…', '5046df1d…') == quoted, head[:60]), '1')
    po = line(p('data', 'b679_closing_push_out.txt'), 4) or ''
    add('ruling (1)', 'the closing commit f507c3f7 pushed', '6b2a8f78..f507c3f7' in po, 'data/b679_closing_push_out.txt :4', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', '6b2a8f78', 'b679 record'), (ROOT, 'relay', 'f507c3f7', 'b679 closing'),
                                  (PP, 'PLACE-papers', '3e375cb', 'b679 record'), (KE, 'SIDE-explicit-formula', '95f8dc8', 'b679')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '1')
    for n, needle in ((9048, '*Appended 2026-10-17 by b679 to b678'), (9050, '## The Li converse over the strip')):
        lt = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, lt.startswith(needle), lt[:70], '1')
    for n, needle in ((14648, 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'), (14650, '### b679')):
        lt = line(OT, n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in lt, lt[:70], '1')
    dl = rd(p('data', 'b679_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'five defects (a)-(e), (a)-(c) the navigator`s', [x for x, _o in letters] == list('abcde') and
        [x for x, o in letters if o == 'NAVIGATOR'] == list('abc'), 'data/b679_defects.txt', '1')
    for bank, needle in (('b679_landing.txt', 'DECLARATIONS 20 ; DERIVES 20'), ('b679_prints_compare.txt', 'EQUAL 29 ; DIFFERING 0'),
                         ('b679_q0_membership.txt', 'HExcl BALLS 35 OF 35 EXCLUDING 0, NEGATIVE 35, Z_Q(0) -1'), ('b679_onset.txt', 'ON THE SUBSEQUENCE 94, NEG 94'),
                         ('b679_onset.txt', 'n*` 63676'), ('b679_mirror.txt', 'CLEAN ON ALL THREE CLAUSES'), ('b679_zeta_walk_46ee9a4.txt', 'ζ-NAMING 0 ;')):
        add('ruling (1)', '%s: "%s"' % (bank, needle), needle in (rd(p('data', bank)) or ''), 'data/%s, its verdict' % bank, '1')
    # ### (R290)(2): the faces line
    fl = line(p('data', 'b679_landing.txt'), 59) or ''
    add('ruling (2)', 'the faces line in data/b679_landing.txt', 'THE FACES PAGE`S LINE ON THE LI FACE AT Q0' in fl, 'data/b679_landing.txt :59-:64', '0, 1')
    add('ruling (2)', 'tools/chain_page.py and the faces page', os.path.exists(p('tools', 'chain_page.py')) and os.path.exists(os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')),
        'exists', '1')
    # ### (R290)(3): the count law
    th = ' '.join((rd(p('data', 'b675_hypotheses.txt')) or '').split())
    add('ruling (3)', 'T-COUNT, HCount at Q0, the kernel`s premise P3 as data/b675_hypotheses.txt names it', 'T-COUNT' in th and 'P3' in th and 'Q0Count' in th,
        'data/b675_hypotheses.txt :61, :67', '1')
    # ### (R290)(4): b670's figures
    for bank, n, needle in (('b670_rules.txt', 5, 'ROW 1 -- THE PAIR OF READINGS'), ('b670_licensed_table.txt', 123, 'ROWS OUTSIDE LICENSED OR CITED 372'),
                            ('b672_correspondence_after.txt', 181, 'BEHIND 54'), ('b672_correspondence_after.txt', 182, '(THE GENERATOR`S CLAIM) 0'),
                            ('b670_ceiling.txt', 25, 'EQUAL AT THREE PLACEMENTS'), ('b670_work_orders.txt', 250, 'OPEN 34 ; DONE 46 ; STATUS NOT STATED 69'),
                            ('b670_methods.txt', 88, 'READY 11'), ('b670_state.txt', 5, 'THE STATE LINE')):
        lt = line(p('data', bank), n) or ''
        if bank == 'b670_state.txt':
            lt = line(p('data', bank), 1) or ''
            n = 1
        add('ruling (4); ferry', '%s :%d "%s"' % (bank, n, needle), needle in lt, 'data/%s :%d' % (bank, n), '2')
    for n in (8819, 8851, 8881, 8913, 8943, 9022, 9050):
        lt = line(FIND, n) or ''
        add('ruling (4)(ix)', 'FINDINGS :%d, an entry of b673-b679' % n, lt.startswith('## '), lt[:60], '2')
    for b in ('b680_readfirst.txt', 'b680_rules_arms.txt', 'b680_arms.txt', 'b680_split_price.txt', 'b680_defects.txt'):
        sz = b == 'b680_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    # ### (R290)(8): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b679', 'push-b679-root', 'push-b679-closing')),
                         (PP, 'PLACE-papers', ('push-b679', 'push-b679-root')),
                         (KE, 'SIDE-explicit-formula', ('push-b679-merge', 'strip-variant-b679'))):
        for b in bs:
            add('ruling (8)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (8)', 'data/b679_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b679_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    add('ruling (10)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b679_worklist.py')) or ''), 'tools/b679_worklist.py', '7')
    for rule, cl_, comp in (('R278', (4,), '7'), ('R251', (3,), '7'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C6', 'data/b678_rules.txt row 1, the suite in three parts', '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS' in (line(p('data', 'b678_rules.txt'), 5) or ''),
        'data/b678_rules.txt :5', '6')
    return R


def _write(L, R, miss):
    for name, data in (('b680_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b680_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b680 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b680_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b680_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b680_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    return bool(act_root_line('b680'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` after this act's ruling, cut from BEGIN to END around it; its relay paths, ledger
    lines and commits checked at HEAD; the print appended to the citation bank, or after the root to the defects bank."""
    best, seen = None, False
    for t in C._user_texts():
        if ANCHOR in t:
            seen = True
        u = t.replace('\u2019', "'")
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
        if not ex and re.match(r'^(data|tools)/b680_', pth):
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
    q = os.path.join(D, 'b680_defects.txt' if after_root() else 'b680_citation_check.txt')
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
        print('usage: b680_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
