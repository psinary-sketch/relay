# -*- coding: utf-8 -*-
"""b681_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b681's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged (the transcript reader with both apostrophes, git, the line
### reader, the rule-clause reader), its anchor pointed at this act's ruling; the rows, the banks and the routes are b681's: once
### data/act_roots.txt carries b681's root (a chain row, not a corrigendum row), an answer's print goes to data/b681_defects.txt and to no
### root-named bank ((R282)(2) row 1; (R291)(3)); each answer cut from BEGIN to END around its needle.
### Routes: `check` -> data/b681_citation_check.txt (.json) ; `ferry` -> data/b681_ferry.txt and data/b681_ferry_scan.txt ;
###         `answer <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b681 from b680_citation.py's form; this tool writes only the banks named above.
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
C.ANCHOR, C.TAIL = 'RULING (R291) BEGIN', 'FERRY END (part 1 of 1)'
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
    for f in ('data/b680_closing.txt', 'data/b680_defects.txt', 'data/act_roots.txt', 'tools/act_root.py', 'data/b680_rules_arms.txt',
              'data/b677_tolerance.txt', 'data/b670_work_orders.txt', 'data/b671_narrow_plan.txt', 'tools/b671_narrow.py',
              'data/b671_run2_progress.txt', 'data/b671_narrow_run3_depths.jsonl', 'data/b671_epstein_zeros_narrowed.json.gz',
              'data/b671_epstein_zeros_narrowed_hashes.txt', 'data/b671_large_banks.txt', 'data/b667_epstein_plan.txt',
              'tools/b677_epstein_map_angle.py', 'data/b680_closing_push_out.txt', 'data/b680_rules.txt', 'data/b675_rules.txt',
              'data/b678_rules.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    np_ = rd(p('data', 'b671_narrow_plan.txt')) or ''
    add('ferry read-first', 'data/b671_narrow_plan.txt sections 11-12', re.search(r'^\s*(?:==|###)?\s*11\.', np_, re.M) and re.search(r'^\s*(?:==|###)?\s*12\.', np_, re.M),
        'the section heads 11. and 12.', '2')
    ep = rd(p('data', 'b667_epstein_plan.txt')) or ''
    add('ferry read-first', 'data/b667_epstein_plan.txt sections 11-16', all(re.search(r'^\s*(?:==|###)?\s*%d\.' % n, ep, re.M) for n in range(11, 17)),
        'the section heads 11. to 16.', '2')
    # ### (R291)(1): b680 at its weight
    head = (rd(p('data', 'b680_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line at data/b680_closing.txt :1', head.startswith('b680 closed: relay 75898036, PLACE-papers 6d8b953; suite 84 of 88; root 764d21d6')
        and '4 prompts answered; 8 defects' in head, head[:110], '1')
    po = rd(p('data', 'b680_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed at relay 21cb2735', '75898036..21cb2735' in po, 'data/b680_closing_push_out.txt', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', '75898036', 'b680 record'), (ROOT, 'relay', '21cb2735', 'b680 closing'),
                                  (ROOT, 'relay', '42d26968', 'b680 record'), (PP, 'PLACE-papers', '6d8b953', 'b680 record')):
        s = subject(repo, sha)
        add('ruling (1)-(2)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    for n, needle in ((9076, '*Appended 2026-10-17 by b680 to b679'), (9078, '## Reading 2 of 2')):
        lt = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, lt.startswith(needle), lt[:70], '1')
    for n, needle in ((14678, 'W-ORD-EPSTEIN-COUNT'), (14680, 'W-ORD-LEDGER-SPLIT-RESOLVER'), (14682, '### b680')):
        lt = line(OT, n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in lt, lt[:70], '1')
    dl = rd(p('data', 'b680_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'eight defects (a)-(h), (a) and (e) the navigator`s', [x for x, _o in letters] == list('abcdefgh') and
        [x for x, o in letters if o == 'NAVIGATOR'] == list('ae'), 'data/b680_defects.txt', '1')
    for bank, needle in (('b680_licensed.txt', '361 AGAINST b670`S 372'), ('b680_correspondence.txt', 'BEHIND BY b670`S METHOD 55 AGAINST 54'),
                         ('b680_orders.txt', 'OPEN 38 ; DONE 49 ; NO STATUS 75'), ('b680_methods.txt', 'READY 9 OF 12'),
                         ('b680_arms.txt', 'STANDING ARMS 68 ; SHAPE 39 ; VALUE 29'), ('b680_rules_arms.txt', 'NONE 24'),
                         ('b680_split_price.txt', 'ARCHIVE-3 HELD AT 4565 CITATIONS'), ('b680_mirror.txt', 'CLEAN ON ALL THREE CLAUSES'),
                         ('b680_checks_postpush.txt', 'ARMS RUN : 88. ### LIVE PASSING : 84.'), ('b680_lag.txt', 'THE LARGEST LAG 244 ; THE MEDIAN 96')):
        add('ruling (1)', '%s: "%s"' % (bank, needle), needle in (rd(p('data', bank)) or ''), 'data/%s, its verdict' % bank, '1')
    # ### (R291)(2): the root repair
    try:
        j = json.load(open(p('data', 'b680_act_root.json'), encoding='utf-8'))
    except Exception:
        j = {}
    add('ruling (2)', 'b680`s root recorded relay 42d26968', ((j.get('commit') or {}).get('relay') or '').startswith('42d26968'),
        'data/b680_act_root.json `commit`', '0')
    add('ruling (2)', 'b680`s root 764d21d6 in data/act_roots.txt', any(r[1].startswith('764d21d6') for r in act_root_line('b680')), 'data/act_roots.txt', '0')
    # ### (R291)(3): the count arms
    ck = rd(p('tools', 'b680_checks.py')) or ''
    for arm in ('G-ANSWERS-BANKED', 'G-ANSWERS-CHECKED', 'G-DEFECTS-LETTERED', 'G-ACTROOT-VERIFY'):
        add('ruling (2)-(3)', arm + ' in the sealed suite', ("('%s'," % arm) in ck, 'tools/b680_checks.py ARMS', '1, 5')
    # ### (R291)(5): the object
    ob = rd(p('data', 'b670_work_orders.txt')) or ''
    add('ruling (5)', 'W-ORD-EPSTEIN-BALL-WIDTH`s row as b677 re-entered it', 'W-ORD-EPSTEIN-BALL-WIDTH                     :14264  b667   10    OPEN' in ob,
        'data/b670_work_orders.txt :266', '2')
    add('ruling (12)', 'W-ORD-MAP-ANGLE-FORM`s row, after W-ORD-EPSTEIN-BALL-WIDTH', 'after W-ORD-EPSTEIN-BALL-WIDTH [:14588]' in ob, 'data/b670_work_orders.txt :265', '4')
    hb = rd(p('data', 'b671_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ruling (5)', 'the narrowed bank`s hashes 51d9e6322510b738 and cd3a8ea1dcc7660c', '51d9e6322510b738' in hb and 'cd3a8ea1dcc7660c' in hb,
        'data/b671_epstein_zeros_narrowed_hashes.txt', '2-3')
    for b in ('b681_readfirst.txt', 'b681_narrow_plan.txt', 'b681_narrow_progress.txt', 'b681_narrow.txt', 'b681_narrow_controls.txt',
              'b681_rules.txt', 'b681_tool_repairs.txt', 'b681_epstein_zeros_narrowed.json.gz', 'b681_epstein_zeros_narrowed_hashes.txt'):
        sz = b == 'b681_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    add('ruling (6)(iv)', 'tools/b681_narrow.py -- TO BE WRITTEN, not a cite', not os.path.exists(p('tools', 'b681_narrow.py')), 'absent, as ordered', '2')
    # ### (R291)(9): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b680-root', 'push-b680-hashes', 'push-b680', 'push-b680-closing')),
                         (PP, 'PLACE-papers', ('push-b680-root', 'push-b680'))):
        for b in bs:
            add('ruling (9)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (9)', 'data/b680_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b680_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    add('ruling (11)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b680_worklist.py')) or ''), 'tools/b680_worklist.py', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b678_rules.txt row 1, the suite in three parts', '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS' in (line(p('data', 'b678_rules.txt'), 5) or ''),
        'data/b678_rules.txt :5', '5')
    add('ferry', 'data/b675_rules.txt row 1, the closing a gate step', bool(re.search(r'\(1\)', rd(p('data', 'b675_rules.txt')) or '')), 'data/b675_rules.txt', '5')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '3, 6')
    return R


def _write(L, R, miss):
    for name, data in (('b681_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b681_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b681 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b681_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b681_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b681_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    return bool(act_root_line('b681'))


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
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,5})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b681_', pth):
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
    q = os.path.join(D, 'b681_defects.txt' if after_root() else 'b681_citation_check.txt')
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
        print('usage: b681_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
