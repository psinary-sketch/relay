# -*- coding: utf-8 -*-
"""b674_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b674's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b673_citation.py by the Write tool: the helpers unchanged (both apostrophes, SESSIONS_AFTER, the after-root redirect of (R282)(2)
row 1: once data/act_roots.txt carries b674's root, an answer's print goes to data/b674_defects.txt and to no root-named bank); the
constants and the rows b674's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R284) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b674_citation_check.txt and read by the suite. A bank the ruling orders written is
### printed TO BE WRITTEN, not a cite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R284) BEGIN'), never from a scratch copy.
### Routes: `python tools/b674_citation.py check` -> data/b674_citation_check.txt (.json);
###         `python tools/b674_citation.py ferry`  -> data/b674_ferry.txt and data/b674_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b674_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b674; this tool writes only the banks named above.
"""
import hashlib
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
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/b895aca8-50cf-4976-9217-c566f780a886.jsonl'
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R284) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE, 'D:/SIDE-window', 'D:/SIDE-trivium')
MIRROR = 'D:/MY-DOwnloads/mirror-refresh-2026-10-16-b673.zip'
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


# ### b670's delimiters, carried from tools/b670_record.py :791-:792 unchanged: the italic run after "Supportable ...:" in README and
# ### REGISTRY; the italic run after "placed at README.md :N and REGISTRY.md :M:" in FINDINGS
SUP = re.compile(r"Supportable[^*]*?: \*(.+?)\*")
PLACED = re.compile(r"placed at README\.md :(\d+) and REGISTRY\.md :(\d+): \*(.+?)\*")


def ceiling_sentence(path, n):
    """b670's reading (iii): the (R183)(3) sentence at a placement, taken by that placement's own delimiters and hashed alone (UTF-8)."""
    l = line(path, n) or ''
    m = (PLACED if path.endswith('FINDINGS.md') else SUP).search(l)
    s = (m.group(3) if path.endswith('FINDINGS.md') else m.group(1)) if m else ''
    return s, hashlib.sha256(s.encode('utf-8')).hexdigest() if s else None


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b673_closing.txt', 'data/b673_defects.txt', 'data/b673_landing.txt', 'data/b673_h5.txt', 'data/b670_state.txt',
              'data/b670_rules.txt', 'data/b671_rules.txt', 'data/b672_rules.txt', 'data/b673_rules.txt', 'data/b670_work_orders.txt',
              'tools/correspondence_gen.py', 'data/b673_closing_push_out.txt', 'tools/b673_closing.py', 'tools/rowgen/rowgen.py',
              'tools/act_root.py', 'tools/push_gated.sh', 'tools/ferry_scan.py', 'tools/licensed_table.py'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-6')
    # ### (R284)(1): b673 at its weight
    cl = rd(p('data', 'b673_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay 6f98c458 (the closing), PLACE-papers f755f99, SIDE-explicit-formula e36ea31, tag v0.32 peeled e36ea31',
        commit_in(ROOT, '6f98c458') and commit_in(PP, 'f755f99') and commit_in(KE, 'e36ea31')
        and g(KE, 'rev-parse', 'v0.32^{commit}')[1].strip().startswith('e36ea31'), 'git cat-file; rev-parse v0.32^{commit}', '1')
    block = ('relay 6f98c458 (closing), read back at the remote | PLACE-papers f755f99: entry FINDINGS :8819, trail record OPEN_TRAILS :14482 | '
             'SIDE-explicit-formula e36ea31, tag v0.32')
    add('ruling (1)', '"the closing`s summary block, quoted verbatim": "%s..."' % block[:90], block in cl,
        'data/b673_closing.txt does not carry the block: it was written before its own closing commit 6f98c458, its head line reads "%s"; the '
        'block quoted is the seat`s report of the close, its figures each in the closing`s own lines -- RAISED' % head[:150], '1')
    for pat, what in ((r'relay 57fdb813, PLACE-papers f755f99, SIDE-explicit-formula e36ea31 v0\.32', 'the record pushes and the merge, read back'),
                      (r'suite 84 of 84', 'suite 84 of 84'), (r'root 4f86a02506f47b9f', 'root 4f86a025...'), (r'16 defects', 'defects 16'),
                      (r'post-push : ARMS RUN : 84\. ### LIVE PASSING : 84\.', 'post-push 84 of 84'),
                      (r'\(N1\) HELD \(N2\) HELD \(N3\) HELD', 'N1-N5 HELD'), (r'\(S1\) HELD \(S2\) HELD \(S3\) HELD', 'S1-S3 HELD'),
                      (r'### AGREE 8 of 8', 'the eight sealed tools agree'), (r'CLEAN ON ALL THREE CLAUSES', 'the mirror CLEAN')):
        h = grep_lines(p('data', 'b673_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b673_closing.txt :%s' % (h[0][0] if h else None), '1')
    ar = act_root_line('b673')
    n_items = len([i for i in (json.loads(rd(p('data', 'b673_act_root.json')) or '{}').get('items') or []) if i.startswith('data/')])
    add('ruling (1)', 'act root b673 4f86a025... over 54 banks, chained from b672`s 41f49fc1...', ar and ar[0][1].startswith('4f86a025')
        and ar[0][2].startswith('41f49fc1') and n_items == 54, 'data/act_roots.txt b673 ; data/b673_act_root.json`s data items %d' % n_items, '1')
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-16-b673.zip, root line in MANIFEST', os.path.exists(MIRROR)
        and 'Act root: b673 4f86a025' in (rd(p('data', 'b673_mirror.txt')) or ''), MIRROR, '1')
    dl = rd(p('data', 'b673_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-p])\) THE ([A-Z']+?)'S", dl, re.M)
    nav = [x for x, o in letters if o == 'NAVIGATOR']
    add('ruling (1)', 'defects (a)-(p), "(b)-(e) the navigator`s"', [x for x, _o in letters] == list('abcdefghijklmnop') and nav == list('bcde'),
        'data/b673_defects.txt: sixteen lettered rows %s; the navigator`s %s -- (g) and (h) are the navigator`s as well (the answers on V4 and '
        'V5) -- RAISED' % ([x for x, _o in letters] == list('abcdefghijklmnop'), nav), '1')
    lt = rd(p('data', 'b673_landing.txt')) or ''
    add('ruling (1)', 'the landing bank "DECLARATIONS 29 ; DERIVES 29"', 'DECLARATIONS 29 ; DERIVES 29' in lt, 'data/b673_landing.txt', '1')
    wj = json.loads(rd(p('data', 'b673_zeta_walk.json')) or '{}')
    add('ruling (1)', 'the walk on S5: 0 ζ-naming of 254 reached, the control firing', wj.get('zeta') == [] and wj.get('reached') == 254
        and (wj.get('control_zeta') or 0) >= 1, 'data/b673_zeta_walk.json', '1')
    rj = json.loads(rd(p('data', 'b673_runner_rows.json')) or '{}')
    refs = [(r.get('ref') or '')[:7] for r in rj.get('rows') or []]
    add('ruling (1)', 'four dispatches at 516803e, b1d4342, 921fb71, 5050a46', sorted(refs) == sorted(['516803e', 'b1d4342', '921fb71', '5050a46']),
        'data/b673_runner_rows.json refs %s' % refs, '1')
    add('ruling (1)', '"one dispatch per tree state" banked', 'one dispatch per tree state' in (rd(p('data', 'b673_rules.txt')) or ''),
        'data/b673_rules.txt row 1', '1')
    h = grep_lines(p('data', 'b673_registration_2026-10-16.txt'), r'396 s')
    add('ruling (1)', 'the foreground pre-run in 396 s', h, 'data/b673_registration_2026-10-16.txt :%s' % (h[0][0] if h else None), '1')
    for n, needle in ((8819, '## V4 DERIVES and V5 DERIVES'),):
        l = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14482, '### b673'), (14478, '`W-ORD-LI-CONVERSE-NATIVE`'), (14480, '`W-ORD-PRINT-TARGETS`'), (14238, 'THE TIE AT COUNT')):
        l = line(OT, n) or ''
        add('ruling (1), (2), (4)', 'OPEN_TRAILS :%d' % n, needle in l, l[:110], '1-3')
    # ### (R284)(2): H5 and the discharge line
    hj = json.loads(rd(p('data', 'b673_h5.json')) or '{}')
    add('ruling (2)', 'H5 through rh_equiv_mathlib: the two sides of the bridge', (hj.get('bridge') or {}).get('carries_vendored_whitespace_removed') is True,
        'data/b673_h5.json bridge', '1')
    dline = line(OT, 14478) or ''
    add('ruling (2)', 'the discharge line carrying "H5 through rh_equiv_mathlib" -- TO BE WRITTEN where it does not already',
        True, 'OPEN_TRAILS :14478 carries it %s; Component 1 appends the line' % ('H5 through rh_equiv_mathlib' in dline), '1')
    # ### (R284)(3): the two drafts and the ceiling's three sites
    for n, needle in ((48, "THE CEILING SENTENCE'S SUCCESSOR"), (58, "THE FACES PAGE'S LINE ON UNEQUAL CONVERSES")):
        l = line(p('data', 'b673_landing.txt'), n) or ''
        add('ruling (3)', 'data/b673_landing.txt :%d' % n, needle in l, l.strip()[:90], '2')
    hs = []
    for f, n in (('README.md', 125), ('REGISTRY.md', 960), ('FINDINGS.md', 6354)):
        s, hx = ceiling_sentence(os.path.join(PP, f), n)
        hs.append(hx)
        add('ruling (3)', 'the ceiling at %s :%d' % (f, n), '`(R183)`(3)' in (line(os.path.join(PP, f), n) or '') and hx, '%s :%d sha256 %s' % (
            f, n, (hx or '')[:16]), '2')
    add('ruling (3)', 'the three sites byte-equal', len(set(hs)) == 1 and hs[0], 'one sha256 %s' % (hs[0] or '')[:16], '2')
    rg = rd(p('tools', 'rowgen', 'rowgen.py')) or ''
    add('ruling (3)', '"the ceiling`s present text at its three sites as rowgen locates them"', 'ceiling' in rg.lower(),
        'tools/rowgen/rowgen.py carries no ceiling locator (it reads roster tables); b670 located the three sites by its own route, relay '
        'data/b670_ceiling.txt, re-read here at README :125, REGISTRY :960 and FINDINGS :6354 -- RAISED', '2')
    add('ruling (3)', 'the ceiling`s anchor "RH reduced to a single located clause, reduction machine-verified"',
        'RH reduced to a single located clause, reduction machine-verified' in (line(os.path.join(PP, 'README.md'), 106) or ''), 'README.md :106', '2')
    add('ruling (3)', '"the faces line written at THE_CLAUSE_AND_ITS_COMPILED_FACES.md at the node the landing bank names"',
        re.search(r'\bnode\s+`[^`]+`', line(p('data', 'b673_landing.txt'), 58) or '') is not None,
        'the landing bank names the page`s generator and no node (:58, "candidate node text for THE_CLAUSE_AND_ITS_COMPILED_FACES.md`s '
        'generator"); the page is generated from its nodes bank (b673 defect (e)) -- RAISED', '2')
    add('ruling (3)', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', os.path.exists(os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')), 'PLACE-papers', '2')
    # ### (R284)(4): the tie and its rule
    st = rd(p('data', 'b670_state.txt')) or ''
    add('ruling (4); ferry read-first', '"the distance rows from data/b670_state.txt" (the ferry: "rows are documents with their distances")',
        'SIDE-window' in st and 'SIDE-trivium' in st,
        'data/b670_state.txt`s rows are the four readings and carries neither kernel; the per-document distances are relay '
        'data/b670_licensed_table.txt :119 (SIDE-trivium docstrings 5 -> 5) and :120 (SIDE-window docstrings 5 -> 5) -- RAISED', '3')
    for n, needle in ((119, 'SIDE-trivium docstrings'), (120, 'SIDE-window docstrings')):
        l = line(p('data', 'b670_licensed_table.txt'), n) or ''
        add('ruling (4)', 'data/b670_licensed_table.txt :%d' % n, needle in l and re.search(r'\b5 ->\s+5\b', l), l.strip()[:100], '3')
    hits = []
    for f in ('b670_rules.txt', 'b671_rules.txt', 'b672_rules.txt', 'b673_rules.txt'):
        hits += ['%s :%d' % (f, i) for i, _l in grep_lines(p('data', f), r'(?i)\btie\b')]
    add('ruling (4)', 'the tie rule`s row in the rules banks (b670-b673)', False if not [h for h in hits if 'b672_rules.txt :7' not in h] else True,
        'no rules bank carries the tie rule (%s, a consumer`s tolerance on the b663 map`s tie test, not this tie); the rule stands at OPEN_TRAILS '
        ':14238 (b666, "where two kernels stand at the same OVERREACHES count ... the kernel carrying a declared suite failure is cut ahead"), '
        'its measure relay data/b647_table_kernels.txt; by the ruling`s own clause the tie is raised as one prompt with the two distances, '
        'nothing cut before the answer' % (hits or 'no row'), '3')
    for k in ('SIDE-window', 'SIDE-trivium'):
        add('ruling (4)', '%s and its licensed table data/b647_table_%s.txt' % (k, k), os.path.isdir('D:/' + k)
            and os.path.exists(p('data', 'b647_table_%s.txt' % k)), 'D:/%s' % k, '3')
    add('ruling (4); (N5)', 'the cut "to LICENSED/CITED" of a docstrings document, against N5`s "no kernel main written" and the ferry`s '
        '"no file written beyond the named document"', False,
        'the named document is a kernel`s docstrings (data/b647_table_SIDE-window.txt, data/b647_table_SIDE-trivium.txt: rows are docstrings '
        'and module headers of the kernel`s .lean files, each with its ACTION, "RE-CUT: <the new text>"); a cut writes the kernel`s .lean '
        'files, which b666 did on a branch, built on the hosted runner and merged to the kernel`s main -- N5`s "no kernel main written" '
        'forbids the merge, and the ferry names no runner build -- RAISED before Component 3', '3')
    # ### (R284)(5)-(9)
    add('ruling (5)', 'defect (p): the closing`s burst and its H5 pattern', '(p) THE SEAT\'S, AT THE CLOSE' in dl, 'data/b673_defects.txt (p)', '4')
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b673-root', 'push-b673', 'push-b673-closing')),
                         (PP, 'PLACE-papers', ('push-b673-root', 'push-b673')), (KE, 'SIDE-explicit-formula', ('push-b673-merge', 'chi-li-b669'))):
        for b in bs:
            add('ruling (6)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (6)', 'chi-li-b669 merged into main at e36ea31', g(KE, 'merge-base', '--is-ancestor', 'chi-li-b669', 'e36ea31')[0] == 0,
        'merge-base --is-ancestor chi-li-b669 e36ea31', '0')
    for b in ('b674_readfirst.txt', 'b674_branches.txt', 'b674_cut.txt', 'b674_ceiling_diff.txt', 'b674_tool_repairs.txt', 'b674_rules.txt'):
        add('ruling (4)-(7); ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, not os.path.exists(p('data', b)), 'absent, as ordered', '0-4')
    add('ruling (8)', 'the draft at v5, held', '23228113' in (rd(p('tools', 'b673_worklist.py')) or ''), 'tools/b673_worklist.py DRAFT', '6')
    add('ruling (9)', 'the composition`s bound Σ_D m − c·r_maxⁿ + C(n+1)²sⁿ, c = 1/4', 'C (n + 1)^2 s^n' in (rd(p('data', 'b673_v4v5_plan.txt')) or '')
        and json.loads(rd(p('data', 'b673_v4_control.json')) or '{}').get('c') == '1/4', 'data/b673_v4v5_plan.txt == 4; data/b673_v4_control.json', '6')
    for rule, cl_, comp in (('R278', (4,), '0-6'), ('R251', (3,), '6'), ('R254', (2,), '0-6')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    return R


def _write(L, R, miss):
    for name, data in (('b674_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b674_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b674 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b674_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b674_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b674_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b674's root."""
    return bool(act_root_line('b674'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b674_', pth):
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
    q = os.path.join(D, 'b674_defects.txt' if after_root() else 'b674_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the navigator`s answer carrying %r, %d characters; its cites checked at HEAD before the seat '
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
        print('usage: b674_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
