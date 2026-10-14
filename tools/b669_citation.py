# -*- coding: utf-8 -*-
"""b669_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b669's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b668_citation.py by the Write tool: the helpers unchanged, the constants and the rows b669's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R279) and the ferry cite is checked
### for existence at HEAD (the kernel at its tag v0.30, Mathlib at the pin de5ce8a9 by git grep in the kernel's package checkout) and the misses
### printed; a miss is raised to the author before the component that cites it runs, not repaired silently; the print is banked as
### data/b669_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R279) BEGIN'), never from a scratch copy.
### Routes: `python tools/b669_citation.py check` -> data/b669_citation_check.txt (.json);
###         `python tools/b669_citation.py ferry`  -> data/b669_ferry.txt and data/b669_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b669_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED.
### Written by the Write tool at b669; this tool writes only the banks named above.
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
KD = 'D:/SIDE-explicit-formula'
KG = 'D:/SIDE-grh-transfer'
ML = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PIN, KTAG = 'de5ce8a9', 'v0.30'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R279) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KD, KG, 'D:/SIDE-cosmo')
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
    """the session's user texts; with results, also the tool results (where an AskUserQuestion answer lands) -- the ferry reads the user
    messages alone, so a tool's own print naming the anchors is never taken for the paste."""
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        if o.get('type') == 'user':
            for t in ([cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']):
                yield t
            for c in (cs if isinstance(cs, list) else []) if results else []:
                if isinstance(c, dict) and c.get('type') == 'tool_result':
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


def grep_line(path, pat):
    t = rd(path) or ''
    for i, l in enumerate(t.split(NL), 1):
        if re.search(pat, l):
            return i, l.strip()
    return None, None


def kdecl(rev, kind_name, paths=('SIDEExplicitFormula',)):
    """a declaration `kind name` at the kernel's rev, by git grep bounded to its source tree: [(file, line)]."""
    rc, o = g(KD, 'grep', '-n', '-E', r'^(noncomputable )?(@\[[^]]*\] )?(%s)\b' % kind_name, rev, '--', *paths)
    return [(l.split(':')[1], l.split(':')[2]) for l in o.split(NL) if l.count(':') >= 2]


def mdecl(kind_name, path):
    rc, o = g(ML, 'grep', '-n', '-E', r'^(@\[[^]]*\] )?(noncomputable )?(%s)\b' % kind_name, 'HEAD', '--', path)
    return [(l.split(':')[1], l.split(':')[2]) for l in o.split(NL) if l.count(':') >= 2]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    for f in ('data/b668_closing.txt', 'data/b668_defects.txt', 'data/b569_bulka_generic.txt', 'data/b572_lemmas.txt',
              'data/b668_closing_push_out.txt', 'data/b668_scores.json', 'data/b668_findings.json'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-6')
    tens = rd(p('data', 'b660_ten_acts.txt')) or ''
    add('ferry read-first', 'data/b660_ten_acts.txt (rows are acts; the χ-Li converse row)', re.search(r'χ-Li|chi-Li', tens, re.I) is not None,
        'the bank exists (%d lines); its rows are defects ("one per line: act and letter, seat, kind", :6), and no row names the χ-Li converse; '
        'the χ-Li converse is priced at OPEN_TRAILS :11732 (b570) and :11796 (b574, REMAINDER 1)' % len(tens.split(NL)), '2')
    cl = rd(p('data', 'b668_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay bfc407e5, PLACE-papers f691545, root f716a8e4...', commit_in(ROOT, 'bfc407e5') and commit_in(PP, 'f691545')
        and act_root_line('b668') and act_root_line('b668')[0][1].startswith('f716a8e4'), 'git cat-file; data/act_roots.txt b668; the closing`s head "%s"' % head[:120], '1')
    for pat, what in (('suite 82 of 83', 'suite 82 of 83'), (r"LIVE FAILING : 1 \['G-MERGES-ON-GATE'\]", 'G-MERGES-ON-GATE declared by name'),
                      ('PARENT BLOCKS 6 ; SENTENCE ROWS 57 ; GRADED 14', 'six blocks, 57 rows, 14 OVERREACHES'),
                      ('CUT COMMITS 3 IN 3 FILES', 'one commit per file in three files'), ('run 38587853597', 'run 38587853597'),
                      ('G-AXIOM-CLAIM BEFORE: CONTRADICTED 0 ; AFTER: CONTRADICTED 0', 'G-AXIOM-CLAIM 0 before and after'),
                      ('CLEAN on all|verification CLEAN', 'the mirror CLEAN'), ('AGREE 8 of 8', 'the sealed tools at the close')):
        n, _l = grep_line(p('data', 'b668_closing.txt'), pat)
        add('ruling (1)', what, n is not None, 'data/b668_closing.txt :%s' % n, '1')
    rr = json.loads(rd(p('data', 'b668_runner_rows.json')) or '{}')
    r0 = (rr.get('rows') or [{}])[0]
    add('ruling (1)', 'branch tip d487072, merge 6e149db, tag v0.5.1 peeled', (r0.get('ref') or '').startswith('d487072') and (r0.get('merged') or '').startswith('6e149db')
        and r0.get('tag') == 'v0.5.1' and g(KG, 'rev-parse', '--short=7', 'v0.5.1^{commit}')[1].strip() == '6e149db', 'data/b668_runner_rows.json; git rev-parse v0.5.1^{commit}', '1')
    dft = rd(p('data', 'b668_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    add('ruling (1)', '"five defects, (b) the navigator`s"', len(letters) == 5 and [l for l, w in letters if w == "NAVIGATOR'S"] == ['b'],
        'data/b668_defects.txt rows: %s' % ', '.join('(%s) %s' % x for x in letters), '1')
    fi = rd(os.path.join(PP, 'FINDINGS.md')) or ''
    n4 = re.search(r'N4 (\w+)', fi[fi.find('## SIDE-grh-transfer’s docstrings at 14'):] if '## SIDE-grh-transfer’s docstrings at 14' in fi else '')
    sc = json.loads(rd(p('data', 'b668_scores.json')) or '{}')
    add('ruling (1), (6)', 'the FINDINGS entry`s N4 cell PENDING, the scores bank HELD', n4 and n4.group(1) == 'PENDING' and (sc.get('N4') or [''])[0] == 'HELD',
        'FINDINGS :8677`s entry reads N4 %s ; data/b668_scores.json N4 %s' % (n4.group(1) if n4 else '?', (sc.get('N4') or ['?'])[0]), '0')
    for n, needle in ((8675, 'b667 AT ITS WEIGHT'), (8677, '## SIDE-grh-transfer’s docstrings')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14290, 'CONSUMERS-AND-TOLERANCES'), (14292, 'MID-ACT'), (14294, 'THE RESEARCH ORDER'), (14296, 'A CENSUS ITEM'),
                      (14298, 'A CELL-REFRESH ITEM'), (14300, '### b668'), (11609, 'THE CONVERSE RE-PRIC'), (11732, 'W-ORD-GRH-WEIL'),
                      (11796, 'REMAINDER 1')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1), (3); ferry', 'OPEN_TRAILS :%d' % n, needle in l, l[:100], '1-2')
    l11609 = line(os.path.join(PP, 'OPEN_TRAILS.md'), 11609) or ''
    add('ruling (3)', 'OPEN_TRAILS :11609`s (V1)-(V4), the power-sum lemma at (V4)', all('(V%d)' % i in l11609 for i in (1, 2, 3, 4)), 'OPEN_TRAILS :11609', '2')
    l6136 = line(os.path.join(PP, 'FINDINGS.md'), 6136) or ''
    add('ferry read-first', 'FINDINGS :6136 (Bulka`s route)', 'bulka' in l6136.lower(), 'FINDINGS :6136 names %s' % (re.findall(r'bulka/[\w-]+', l6136)[:1] or 'no Bulka'), '2')
    # ### the kernel at its tag
    km = g(KD, 'describe', '--tags', 'main')[1].strip()
    add('ruling (2)-(4)', 'SIDE-explicit-formula at v0.30 (main), v0.31 the next tag', km == KTAG and not g(KD, 'tag', '--list', 'v0.31')[1].strip(),
        'git describe --tags main: %s ; v0.31 not yet listed' % km, '2-4')
    for what, kn, paths, rev in (('LiWeil.lean`s LiCoeff', 'def LiCoeff', ('SIDEExplicitFormula',), KTAG),
                                 ('LiWeil.lean`s rh_imp_li_nonneg', 'theorem rh_imp_li_nonneg', ('SIDEExplicitFormula',), KTAG),
                                 ('li_nonneg_iff_rh at v0.9', 'theorem li_nonneg_iff_rh', ('SIDEExplicitFormula',), 'v0.9'),
                                 ('li_coeff_eq_taylorCoeff (the ferry`s "LiCriterion")', 'theorem li_coeff_eq_taylorCoeff', ('SIDEExplicitFormula',), KTAG),
                                 ('riemannXi (the ferry`s "LiCriterion")', 'def riemannXi', ('Vendored', 'SIDEExplicitFormula'), KTAG),
                                 ('Chi/ZeroConfig.lean`s chiZeroConfig', 'def chiZeroConfig', ('SIDEExplicitFormula',), KTAG),
                                 ('h2_sign_chi_iff_grh_chi at v0.14', 'theorem h2_sign_chi_iff_grh_chi', ('SIDEExplicitFormula',), 'v0.14'),
                                 ('Config.lean`s WeilConfig', 'structure WeilConfig', ('SIDEExplicitFormula',), KTAG),
                                 ('ZeroConfig (Zeta23)', 'structure ZeroConfig', ('Zeta23',), KTAG)):
        hits = kdecl(rev, kn, paths)
        add('ruling (2); ferry read-first', what, hits, '%s: %s' % (rev, '; '.join('%s :%s' % h for h in hits[:3]) or 'NOT FOUND'), '2')
    add('ferry read-first', 'PageConverses.lean', g(KD, 'cat-file', '-e', '%s:SIDEExplicitFormula/PageConverses.lean' % KTAG)[0] == 0,
        '%s:SIDEExplicitFormula/PageConverses.lean' % KTAG, '2')
    mpin = (json.loads(g(KD, 'show', '%s:lake-manifest.json' % KTAG)[1] or '{}').get('packages') or [])
    mrev = [x.get('rev') for x in mpin if x.get('name') == 'mathlib']
    add('ruling (3)', 'Mathlib at de5ce8a9', mrev and mrev[0].startswith(PIN) and g(ML, 'rev-parse', 'HEAD')[1].startswith(PIN),
        'lake-manifest at %s: %s ; the package checkout at %s' % (KTAG, mrev, g(ML, 'rev-parse', '--short=8', 'HEAD')[1].strip()), '2')
    for what, kn, path in (('the completed L-function of a Dirichlet character', 'def completedLFunction', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean'),
                           ('its functional equation', 'theorem completedLFunction_one_sub', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean'),
                           ('its differentiability', 'lemma differentiable_completedLFunction', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean')):
        hits = mdecl(kn, path)
        add('ferry read-first', what, hits, 'Mathlib %s %s: %s' % (PIN, path, '; '.join(':%s %s' % (h[0], h[1][:70]) for h in hits[:2]) or 'NOT FOUND'), '2')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b668'), (ROOT, 'relay', 'push-b668-root'), (ROOT, 'relay', 'push-b668-closing'),
                        (PP, 'PLACE-papers', 'push-b668'), (PP, 'PLACE-papers', 'push-b668-root'), (KG, 'SIDE-grh-transfer', 'push-b668-workflow'),
                        (KG, 'SIDE-grh-transfer', 'push-b668-merge'), (KG, 'SIDE-grh-transfer', 'docstrings-cut-SIDE-grh-transfer')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (4)', 'branch chi-li-b669 not yet made', not branch_listed(KD, 'chi-li-b669'), 'git branch --list chi-li-b669 in SIDE-explicit-formula', '3')
    # ### rules and orders
    for rule, cl_, comp in (('R278', (3, 4, 5), '0-6'), ('R251', (3,), '6'), ('R254', (2,), '0-6')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py', 'tools/b663_epstein_map.py'):
        add('ferry; the b663 plan form', f, os.path.exists(p(*f.split('/'))), 'exists', '0-6')
    add('ruling (3)', 'the b663 plan form (data/b663_epstein_plan.txt)', os.path.exists(p('data', 'b663_epstein_plan.txt')), 'exists', '2')
    add('ruling (5)', 'the draft at v5, held', 'v5' in cl and '23228113' in cl, 'data/b668_closing.txt (N5): draft 23228113, v5, unsubmitted', '6')
    return R


def _write(L, R, miss):
    for name, data in (('b669_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b669_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b669 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b669_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b669_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b669_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer) -- its relay paths, ledger lines and commits checked at HEAD,
    the print appended to the citation bank with the answer named."""
    best = None
    for t in _user_texts():
        if needle in t and "NAVIGATOR'S ANSWER" in t:
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b669_', pth):
            rows_.append(('path, this act`s bank the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for led, n in sorted(set(re.findall(r'\b(FINDINGS|OPEN_TRAILS)\b[^:]{0,20}:(\d{4,5})', best))):
        rows_.append(('line', '%s :%s' % (led, n), line(os.path.join(PP, led + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS) or commit_in(ML, h)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b669_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the navigator`s answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best))]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k, w) for k, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                       (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b669_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
