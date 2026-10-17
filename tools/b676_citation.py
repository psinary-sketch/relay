# -*- coding: utf-8 -*-
"""b676_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b676's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b675_citation.py by the Write tool: the helpers unchanged (both apostrophes, SESSIONS_AFTER, the after-root redirect of (R282)(2)
row 1: once data/act_roots.txt carries b676's root, an answer's print goes to data/b676_defects.txt and to no root-named bank); the
constants and the rows b676's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R286) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b676_citation_check.txt and read by the suite. A bank the ruling orders written is
### printed TO BE WRITTEN, not a cite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R286) BEGIN'), never from a scratch copy.
### Routes: `python tools/b676_citation.py check` -> data/b676_citation_check.txt (.json);
###         `python tools/b676_citation.py ferry`  -> data/b676_ferry.txt and data/b676_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b676_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b676; this tool writes only the banks named above.
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
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KE = 'D:/SIDE-explicit-formula'
TD = 'D:/SIDE-trivium'
KREV = 'e36ea31'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/fcdfb5b9-96dd-44c6-84e3-cd8d0d0ba63d.jsonl'
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R286) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE, TD, 'D:/SIDE-window')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.replace(chr(13), '')


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else None


def line(p, n):
    t = rd(p)
    ls = t.split(NL) if t is not None else []
    return ls[n - 1] if 0 < n <= len(ls) else None


def kline(path, n, repo=KE, rev=KREV):
    """a kernel file's line n at rev, read by git show (the kernel is not built or checked out here)."""
    rc, o = g(repo, 'show', '%s:%s' % (rev, path))
    ls = o.split(NL) if rc == 0 else []
    return ls[n - 1] if 0 < n <= len(ls) else None


def _user_texts(results=True):
    """the session's user texts; with results, the results of the seat's own prompts alone (b670 defect (e))."""
    ask = set()
    for raw in (r for s in (SESSION,) + SESSIONS_AFTER for r in io.open(s, encoding='utf-8', errors='replace')):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        for c in (cs if isinstance(cs, list) else []):
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                ask.add(c.get('id'))
        if o.get('type') == 'user':
            for t in ([cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']):
                yield t
            for c in (cs if isinstance(cs, list) else []) if results else []:
                if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                    t = c.get('content')
                    yield ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for t in _user_texts(results=False):
        i, j = t.find(ANCHOR), t.find(TAIL)
        if i >= 0 and j > i:
            best = t[i:j + len(TAIL)].replace(chr(13), '')
    if best is None:
        sys.exit('### THE RULING IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    return best


def commit_in(repo, sha):
    rc, _o = g(repo, 'cat-file', '-e', sha + '^{commit}')
    return rc == 0


def subject(repo, sha):
    return g(repo, 'log', '-1', '--format=%s', sha)[1].strip()


def branch_listed(repo, b):
    rc, o = g(repo, 'branch', '--list', b)
    return bool(o.strip())


def rule_clause(rule, clauses):
    for f in sorted(os.listdir(D)):
        if f.endswith('_ferry.txt'):
            t = rd(os.path.join(D, f))
            if t and ('RULING (%s) BEGIN' % rule) in t:
                body = t[t.index('RULING (%s) BEGIN' % rule):]
                return all(('(%d)' % c) in body for c in clauses), 'data/%s' % f
    return False, 'no ferry bank carries RULING (%s)' % rule


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    ls = [l.split() for l in t.split(NL) if l.strip()]
    return [l for l in ls if l[0] == act]


def grep_lines(path, pat, flags=0):
    t = rd(path) or ''
    return [(i, l.strip()) for i, l in enumerate(t.split(NL), 1) if re.search(pat, l, flags)]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b675_closing.txt', 'data/b675_defects.txt', 'data/b675_hypotheses.txt', 'data/b675_li_plan.txt', 'data/b675_rules.txt',
              'data/b674_rules.txt', 'data/b670_licensed_table.txt', 'data/b674_cut.txt', 'data/b674_tool_repairs.txt',
              'data/b675_tool_repairs.txt', 'tools/correspondence_gen.py', 'data/b670_work_orders.txt', 'data/b675_closing_push_out.txt',
              'data/b671_tie_diagnostic.txt', 'data/b667_h4_reading.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-6')
    tabs = sorted(f for f in os.listdir(D) if re.match(r'^b647_table_.*\.txt$', f))
    add('ferry read-first', 'the per-kernel tables data/b647_table_*.txt', len(tabs) >= 21, '%d files (the kernels table and %d kernels)' % (
        len(tabs), len(tabs) - 1), '2')
    # ### (R286)(1): b675 at its weight
    cl = rd(p('data', 'b675_closing.txt')) or ''
    head = cl.split(NL)[0]
    quoted = 'b675 closed: relay cced648a, PLACE-papers 0b51683; suite 83 of 83; root e4a6c52715bf9693\u2026; 4 prompts answered; 13 defects'
    add('ruling (1)', 'the head line quoted at data/b675_closing.txt :1', head == quoted, 'character for character: %s' % (head == quoted), '1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'cced648a', 'b675 record'), (ROOT, 'relay', '7e867b61', 'b675 closing'),
                                  (PP, 'PLACE-papers', '0b51683', 'b675 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s, its subject opening "%s"' % (nm, sha, needle), commit_in(repo, sha) and s.startswith(needle), s[:80], '1')
    for f, n, needle in (('FINDINGS.md', 8881, '## The Li index at Q0: HStrip fails'), ('OPEN_TRAILS.md', 14532, '### b675')):
        l = line(os.path.join(PP, f), n) or ''
        add('ruling (1)', '%s :%d' % (f, n), needle in l, l[:90], '1')
    for pat, what in ((r'HStrip ON THE CERTIFIED POINTS: HELD \(34 of 34', 'HStrip on the 34 certified real parts'),
                      (r'FAILS \(Davenport-Heilbron', 'HStrip fails for the configuration by Davenport-Heilbronn'),
                      (r'n\* \(WERE HStrip TO HOLD\) 63676 ; n_obs 10034', 'n* 63676, n_obs 10034'),
                      (r'NEG 102 OF 201', 'NEG at 102 of 201 n'),
                      (r"C2′: NEG 0", 'C2′ NEG 0'), (r'THE LEAST NEG 15401', 'C2 negative from 15401'),
                      (r'n\*′ 358665, n_obs′ 64065', 'H6 n*′ 358665, n_obs′ 64065'),
                      (r'\(H1\) REFUTED.*\(H3\) REFUTED', 'H1 and H3 refuted as worded'),
                      (r'\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD', 'N1-N5, S1-S3 HELD'),
                      (r'pre-push : ARMS RUN : 83\. ### LIVE PASSING : 83', 'suite 83 of 83 pre-push'),
                      (r'post-push : ARMS RUN : 83\. ### LIVE PASSING : 83', 'suite 83 of 83 post-push'),
                      (r'REPAIRS 4 ;', 'the closing tool`s four repairs')):
        h = grep_lines(p('data', 'b675_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b675_closing.txt :%s' % (h[0][0] if h else None), '1')
    hy = rd(p('data', 'b675_hypotheses.txt')) or ''
    add('ruling (1)', 'the real parts 0.0467 to 0.9533 and h(-23) = 3', '[0.04673952' in hy and '[0.95326047' in hy and 'h(-23) = 3' in hy,
        'data/b675_hypotheses.txt :43 (the least 0.04673952..., the greatest 0.95326047..., rounded to four places as the ruling quotes '
        'them), :49 (h(-23) = 3)', '1')
    sl = kline('Zeta23/Defs.lean', 142) or ''
    add('ruling (1), (4)', 'Zeta23/Defs.lean :142 at %s, the strip a field of ZeroConfig' % KREV, sl.strip().startswith('strip :'), sl.strip(), '1, 4')
    hl = kline('SIDEExplicitFormula/RestBound.lean', 40) or ''
    add('ferry read-first', 'SIDEExplicitFormula/RestBound.lean :40 at %s' % KREV, 'def HStrip' in hl, hl.strip()[:90], '4')
    lp = grep_lines(p('data', 'b675_li_plan.txt'), r'THE VARIANT HYPOTHESIS FOR A LATER ACT')
    add('ruling (1), (4)', 'the variant hypothesis named in data/b675_li_plan.txt', lp, 'data/b675_li_plan.txt :%s' % (lp[0][0] if lp else None), '4')
    rl = rd(p('data', 'b675_rules.txt')) or ''
    add('ruling (1); ferry C5', 'rules row 1, the closing dry-run as a gate step', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in rl,
        'data/b675_rules.txt :5', '1, 5')
    br = json.loads(rd(p('data', 'b675_branches.json')) or '{}').get('rows') or []
    add('ruling (1)', 'ten branches deleted, two at their remotes', len(br) == 10 and sum(1 for r in br if r['where'] == 'remote') == 2,
        'data/b675_branches.json: %d rows, %d remote' % (len(br), sum(1 for r in br if r['where'] == 'remote')), '1')
    dl = rd(p('data', 'b675_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-m])\) THE ([A-Z']+?)'S", dl, re.M)
    nav = [x for x, o in letters if o == 'NAVIGATOR']
    add('ruling (1)', 'thirteen defects (a)-(m), (a)-(g) the navigator`s', len(letters) == 13 and nav == list('abcdefg'),
        'data/b675_defects.txt: %d lettered rows; the navigator`s %s' % (len(letters), nav), '1')
    c4, c5 = grep_lines(p('data', 'b674_checks.txt'), r'the standing arms .* 68 ; carried here 68'), grep_lines(p('data', 'b675_checks.txt'), r'the standing arms .* 68 ; carried here 68')
    a4 = len(re.findall(r"'G-[A-Z0-9-]+'", c4[0][1])) if c4 else -1
    a5 = len(re.findall(r"'G-[A-Z0-9-]+'", c5[0][1])) if c5 else -1
    nc4, nc5 = grep_lines(p('data', 'b674_checks.txt'), r'standing arms not carried here: NONE'), grep_lines(p('data', 'b675_checks.txt'), r'standing arms not carried here: NONE')
    add('ruling (1)', '"the arm named and the bank that records its removal" (84 to 83)', False,
        'no arm was removed: both suites carry the 68 standing arms whole (data/b674_checks.txt :%s, data/b675_checks.txt :%s, "standing arms '
        'not carried here: NONE" at :%s and :%s); the act`s own arms are minted per act and not carried ((R264)(2)) -- b674`s %d, b675`s %d '
        '(84 = 68 + 16, 83 = 68 + 15); no bank records a removal because none took place -- RAISED' % (
            c4[0][0] if c4 else None, c5[0][0] if c5 else None, nc4[0][0] if nc4 else None, nc5[0][0] if nc5 else None, a4, a5), '0-1')
    # ### (R286)(2): the re-cut
    tr = rd(p('data', 'b674_rules.txt')) or ''
    add('ruling (2)', 'the tie-break rule of data/b674_rules.txt', '(2) THE TIE-BREAK BEYOND THE COUNT' in tr, 'data/b674_rules.txt row (2), :8', '2')
    l119 = line(p('data', 'b670_licensed_table.txt'), 119) or ''
    add('ruling (2)', 'SIDE-trivium docstrings at 5 rows outside LICENSED/CITED', 'SIDE-trivium docstrings' in l119 and re.search(r'\b5 ->\s+5\b', l119),
        'data/b670_licensed_table.txt :119', '2')
    cut = rd(p('data', 'b674_cut.txt')) or ''
    add('ruling (2)', 'the b674 residue: SIDE-window`s Sawtooth header marker at :17', 'the marker at :17' in cut, 'data/b674_cut.txt', '2')
    add('ruling (2)', 'the b670 method (tools/b670_record.py :519)', 'OVERREACHES and UNLICENSED' in (line(p('tools', 'b670_record.py'), 519) or ''),
        'tools/b670_record.py :519', '2')
    ni = line(OT, 14440) or ''
    add('ruling (2)', 'the nine-kernels item', 'THE KERNELS WITH NO RELAY PRINT BANK AT THEIR TAG' in ni and '9 kernels' in ni,
        'OPEN_TRAILS :14440 (b672, under (R282)(7))', '2')
    add('ruling (2)', 'SIDE-trivium main 1aac3a9, the table`s read pin', g(TD, 'rev-parse', 'main')[1].startswith('1aac3a9'), 'rev-parse main', '2')
    add('ruling (2)', 'SIDE-trivium`s last tag v0.1', g(TD, 'rev-parse', 'v0.1^{commit}')[1].startswith('ec92d62'),
        'v0.1 peeled ec92d62; main 1aac3a9 is %s commit(s) past it' % g(TD, 'rev-list', '--count', 'v0.1..main')[1].strip(), '2')
    # ### (R286)(3)
    add('ruling (3)', 'W-ORD-Q0-CLASS-LINES -- TO BE WRITTEN, not a cite', 'W-ORD-Q0-CLASS-LINES' not in (rd(OT) or ''), 'absent from OPEN_TRAILS, as ordered', '3')
    # ### (R286)(4): the merged proof
    add('ruling (4)', 'SIDE-explicit-formula v0.32 at e36ea31', g(KE, 'rev-parse', 'v0.32^{commit}')[1].startswith('e36ea31'), 'rev-parse', '4')
    for f in ('SIDEExplicitFormula/Schema/LiRemainder.lean', 'SIDEExplicitFormula/Schema/LiConverseCfg.lean'):
        add('ruling (4)', '%s at %s' % (f, KREV), g(KE, 'cat-file', '-e', '%s:%s' % (KREV, f))[0] == 0, 'git cat-file', '4')
    # ### (R286)(5): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b675', 'push-b675-root', 'push-b675-closing')),
                         (PP, 'PLACE-papers', ('push-b675', 'push-b675-root'))):
        for b in bs:
            add('ruling (5)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (5)', 'data/b675_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b675_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R286)(6)-(8) and the banks the ruling orders written
    for b in ('b676_readfirst.txt', 'b676_cut.txt', 'b676_q0_lines.txt', 'b676_strip_uses.txt', 'b676_tool_repairs.txt'):
        sz = b == 'b676_readfirst.txt'
        add('ruling (2)-(6); ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written by this act after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz
            else 'absent, as ordered', '0-5')
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b675_worklist.py')) or ''), 'tools/b675_worklist.py :24', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '3')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    return R


def _write(L, R, miss):
    for name, data in (('b676_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b676_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b676 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    text = ferry_text()
    q = os.path.join(D, 'b676_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b676_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b676_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b676's root."""
    return bool(act_root_line('b676'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b676_', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        elif not ex and 'bNNN' in pth:
            rows_.append(('path, a placeholder of a form for later acts -- not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b676_defects.txt' if after_root() else 'b676_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it%s:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best),
                            ' (after the root: printed to the defects bank, (R282)(2) row 1)' if after_root() else '')]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k, w) for k, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**%s' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                         (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '',
                                                                         ' -- VACUOUS: no cite to check.' if not rows_ else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b676_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
