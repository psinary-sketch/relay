# -*- coding: utf-8 -*-
"""b670_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b670's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b669_citation.py by the Write tool: the helpers unchanged, the constants and the rows b670's; the answer route's ledger pattern widened to
a run of line numbers after one ledger name (b669's defect (b)).

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R280) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b670_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R280) BEGIN'), never from a scratch copy.
### Routes: `python tools/b670_citation.py check` -> data/b670_citation_check.txt (.json);
###         `python tools/b670_citation.py ferry`  -> data/b670_ferry.txt and data/b670_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b670_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED.
### Written by the Write tool at b670; this tool writes only the banks named above.
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
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R280) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE, 'D:/SIDE-grh-transfer', 'D:/SIDE-cosmo')
ACTS = tuple('b%d' % i for i in range(660, 670))
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


def grep_lines(path, pat, flags=0):
    t = rd(path) or ''
    return [(i, l.strip()) for i, l in enumerate(t.split(NL), 1) if re.search(pat, l, flags)]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    for a in ACTS:
        for kind in ('closing', 'defects'):
            f = 'data/%s_%s.txt' % (a, kind)
            add('ferry read-first; ruling (2)', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-2')
    for f in ('data/b668_b670_items.txt', 'data/b647_table_kernels.txt', 'data/b669_closing_push_out.txt', 'tools/rowgen/rowgen.py',
              'tools/licensed_table.py', 'tools/mirror_build.ps1', 'tools/mirror_verify.py'):
        add('ferry; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-7')
    cl = rd(p('data', 'b669_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay e527a09e, PLACE-papers 165a645, root 613c17a9...', commit_in(ROOT, 'e527a09e') and commit_in(PP, '165a645')
        and act_root_line('b669') and act_root_line('b669')[0][1].startswith('613c17a9'), 'git cat-file; data/act_roots.txt b669; the closing`s head "%s"' % head[:110], '1')
    for pat, what in (('suite 82 of 82', 'suite 82 of 82'), (r'H1 HELD ; H2 HELD ; H3 HELD ; H4 HELD', 'H1-H4'),
                      (r'ζ-NAMING 0', 'the walk, none ζ-naming'), (r'92 declarations reached', '92 declarations reached')):
        h = grep_lines(p('data', 'b669_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b669_closing.txt :%s' % (h[0][0] if h else None), '1')
    lj = json.loads(rd(p('data', 'b669_chi_li_landing.json')) or '{}')
    mg = lj.get('merge') or {}
    add('ruling (1)', 'merged at 115abfe, tag v0.31; chi-li-b669 at b804bf2', (mg.get('sha') or '').startswith('115abfe') and mg.get('tag') == 'v0.31'
        and g(KE, 'rev-parse', '--short=7', 'v0.31^{commit}')[1].strip() == '115abfe' and g(KE, 'rev-parse', '--short=7', 'chi-li-b669')[1].strip() == 'b804bf2',
        'data/b669_chi_li_landing.json merge; git rev-parse v0.31^{commit}, chi-li-b669', '1, 6')
    lc = g(KE, 'show', 'chi-li-b669:SIDEExplicitFormula/Schema/LiConverseCfg.lean')[1].split(NL)
    add('ruling (1)', 'V4 open at LiConverseCfg.lean :129, V5 at :139', len(lc) > 139 and lc[128].strip() == 'sorry' and lc[138].strip() == 'sorry',
        'chi-li-b669:SIDEExplicitFormula/Schema/LiConverseCfg.lean :129 %r, :139 %r' % (lc[128].strip() if len(lc) > 128 else None,
                                                                                        lc[138].strip() if len(lc) > 138 else None), '1')
    dft = rd(p('data', 'b669_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    add('ruling (1)', '"four defects, (a) the navigator`s"', len(letters) == 4 and [l for l, w in letters if w == "NAVIGATOR'S"] == ['a'],
        'data/b669_defects.txt rows: %s' % ', '.join('(%s) %s' % x for x in letters), '1')
    for n, needle in ((8703, 'THE N4 CELL'), (8705, 'b668 AT ITS WEIGHT'), (8707, '## The Li coefficient over the configuration')):
        l = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14324, '### b669'), (14238, 'THE TIE'), (14290, 'CONSUMERS-AND-TOLERANCES'), (14292, 'MID-ACT'), (12090, 'W-ORD-CONSTELLATION-RERUN')):
        l = line(OT, n) or ''
        add('ruling (1), (3); ferry', 'OPEN_TRAILS :%d' % n, needle in l, l[:100], '1-3')
    wo = grep_lines(OT, r'W-ORD-')
    add('ferry read-first', 'OPEN_TRAILS at every line carrying "W-ORD-" (rows are orders)', wo, '%d lines carry "W-ORD-"' % len(wo), '3')
    # ### the review-pass rule for rowgen diff and constellation mode, by its line
    rg = grep_lines(OT, r'rowgen diff', re.I) + grep_lines(FIND, r'rowgen diff', re.I)
    rp = [x for x in grep_lines(OT, r'review pass', re.I) if re.search(r'rowgen|constellation', x[1], re.I)]
    add('ruling (3)(i); ferry read-first', 'the review-pass rule for rowgen diff and constellation mode, by its line', rg or rp,
        'the lines naming "rowgen diff" (OPEN_TRAILS and FINDINGS, case-insensitive): %s; review-pass lines naming rowgen or constellation: %d. '
        'The line found is W-ORD-CONSTELLATION-RERUN`s items (:12090 its head, b587 under (R197)(4)): constellation mode over the 19 roster '
        'tables of relay data/b586_corroboration.txt, a rowgen diff per table -- an order over the roster tables, not a review-pass agenda; the '
        'review pass opened at b645 (OPEN_TRAILS :13633) with tools/licensed_table.py. A reading for the author' % (
            ', '.join(':%d' % i for i, _l in rg) or 'NONE', len(rp)), '3')
    # ### the pair and the criteria the ruling sets at b663
    pair = [x for x in grep_lines(OT, r'two consecutive reading acts|reading 1 of 2|consecutive reading', re.I)] + \
        [x for x in grep_lines(FIND, r'two consecutive reading acts|reading 1 of 2|consecutive reading', re.I)]
    b663 = ' '.join(rd(p('data', f)) or '' for f in os.listdir(D) if f.startswith('b663_') and f.endswith('.txt'))
    add('ruling (3)', 'the pair the author set at b663 (two consecutive reading acts agreeing)', pair or re.search(r'consecutive reading', b663, re.I),
        'no ledger line and no b663 bank carries it (OPEN_TRAILS, FINDINGS, data/b663_*.txt searched for "two consecutive reading acts", '
        '"consecutive reading", "reading 1 of 2"); FINDINGS :1489 is an older calibration of "two consecutive acts"', '3')
    crit = grep_lines(OT, r'method.readiness|NOT YET USED TWICE|methods? (is|are) READY', re.I) + grep_lines(FIND, r'method.readiness|NOT YET USED TWICE', re.I)
    add('ruling (4)', 'the method-readiness criteria of b663', crit or re.search(r'method.readiness|readiness', b663, re.I),
        'no ledger line and no b663 bank carries them (searched for "method-readiness", "readiness", "NOT YET USED TWICE"); the ruling`s own '
        'clause (4) states three cells -- acts used, inputs and outputs banked, a failure mode recorded -- and the three readings', '4')
    # ### the ceiling sentence's placements
    ce_r = grep_lines(os.path.join(PP, 'README.md'), r'^\*\(Appended under the author.s ruling|^\*\(Reworded under the author.s ruling')
    ce_g = grep_lines(os.path.join(PP, 'REGISTRY.md'), r'THE CEILING LINE|^\*\(Appended under the author.s ruling')
    add('ruling (3)(iii); ferry read-first', 'the ceiling sentence at README, REGISTRY and FINDINGS', ce_r and ce_g,
        'README carries %d ceiling sentences (:%s to :%s), REGISTRY %d (:%s to :%s); FINDINGS :6206 records the (R176)(2) placement; which '
        'sentence the comparison reads is the reading`s to state' % (len(ce_r), ce_r[0][0] if ce_r else '-', ce_r[-1][0] if ce_r else '-', len(ce_g),
                                                                    ce_g[0][0] if ce_g else '-', ce_g[-1][0] if ce_g else '-'), '3')
    # ### the next kernel after "the seven cut"
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    cut = ['SIDE-kernel', 'SIDE-global-section', 'SIDE-lv-conservation', 'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-effects',
           'SIDE-cosmo', 'SIDE-grh-transfer']
    add('ruling (8)', '"the next kernel by count ... after the seven cut"', False,
        'the kernels cut since b647 are eight by the re-cut acts` banks: the six b666`s G-KERNEL-NAMED reads as cut (SIDE-kernel, '
        'SIDE-global-section, SIDE-lv-conservation, SIDE-structural-error-correction, SIDE-carrier-spec, SIDE-effects), SIDE-cosmo at b666 and '
        'SIDE-grh-transfer at b668; all eight rows in data/b647_table_kernels.txt: %s' % all(('  %s ' % k) in kt for k in cut), '8')
    # ### the census and cell-refresh items the ruling names
    for what, pat, src in (('lv-conservation`s UNRESOLVED rows', r'UNRESOLVED-CELL 1', 'data/b657_sentence_grades.txt'),
                           ('SIDE-effects` Milestones blocks', r'Milestones', None), ('carrier-spec`s README heading', r'README', 'data/b662_closing.txt'),
                           ('SIDE-cosmo`s untagged main', r'untagged', 'data/b666_closing.txt'), ('SIDE-grh-transfer`s ASCII cells', r'A CELL-REFRESH ITEM', None),
                           ('SIDE-grh-transfer`s 858cbf6', r'858cbf6', None), ('EpsteinQ0`s decimal literals', r'THE KERNEL ITEM FOR P1 AND P2', None),
                           ('K4', r'\bK4\b', None)):
        hits = grep_lines(p(*src.split('/')), pat) if src else grep_lines(OT, pat)
        add('ruling (5)', what, hits, '%s :%s' % (src or 'OPEN_TRAILS', ', :'.join(str(h[0]) for h in hits[-3:]) or 'NONE'), '5')
    it = rd(p('data', 'b668_b670_items.txt')) or ''
    add('ruling (5)', 'the items bank: item 1 EXTERNAL-ZFR-7/8 with its trigger (a); item 2 the flag', 'ITEM 1 -- EXTERNAL-ZFR-7/8' in it and 'Triggers: (a)' in it
        and 'ITEM 2 -- THE TWO RELATIVE-ENTROPY QUESTIONS' in it, 'data/b668_b670_items.txt', '5')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b669'), (ROOT, 'relay', 'push-b669-root'), (ROOT, 'relay', 'push-b669-closing'),
                        (PP, 'PLACE-papers', 'push-b669'), (PP, 'PLACE-papers', 'push-b669-root'), (KE, 'SIDE-explicit-formula', 'push-b669-merge'),
                        (KE, 'SIDE-explicit-formula', 'chi-li-b669')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    for rule, cl_, comp in (('R278', (3, 4, 5), '0-7'), ('R251', (3,), '7'), ('R254', (2,), '0-7')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (6)', 'the draft at v5, held', '23228113' in cl and 'v5' in cl, 'data/b669_closing.txt (N5)', '7')
    return R


def _write(L, R, miss):
    for name, data in (('b670_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b670_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b670 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b670_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b670_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b670_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer) -- its relay paths, ledger lines (every line number in a run
    after one ledger name) and commits checked at HEAD, the print appended to the citation bank with the answer named."""
    best = None
    for t in _user_texts():
        if needle in t and "NAVIGATOR'S ANSWER" in t:
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b670_', pth):
            rows_.append(('path, this act`s bank the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b670_citation_check.txt')
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
        print('usage: b670_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
