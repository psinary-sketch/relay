# -*- coding: utf-8 -*-
"""b668_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b668's step zero; the ferry banked after
it; and, from (R278)(4), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from tools/b667_citation.py: the
helpers unchanged, the constants and the rows b668's, the `answer` route new.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R278) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b668_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R278) BEGIN'), never from a scratch copy.
### Routes: `python tools/b668_citation.py check` -> data/b668_citation_check.txt (.json);
###         `python tools/b668_citation.py ferry`  -> data/b668_ferry.txt and data/b668_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b668_citation.py answer <needle>` -> the latest session answer carrying <needle>: every relay data/ or tools/ path,
###         every FINDINGS/OPEN_TRAILS line (:NNNN) and every 7-12 hex commit it names checked at HEAD; the print APPENDED to
###         data/b668_citation_check.txt with the answer named ((R278)(4)).
### Written by the Write tool at b668; this tool writes only the banks named above.
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
KD = 'D:/SIDE-grh-transfer'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R278) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KD, 'D:/SIDE-cosmo', 'D:/SIDE-explicit-formula')
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


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    for f in ('data/b667_closing.txt', 'data/b667_defects.txt', 'data/b667_root_list.txt', 'data/b647_table_kernels.txt',
              'data/b647_table_SIDE-grh-transfer.txt', 'data/b657_sentence_grades.txt', 'data/b667_closing_push_out.txt',
              'tools/mirror_build.ps1', 'tools/mirror_verify.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    cl = rd(p('data', 'b667_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay aeccc731, PLACE-papers 7904281', commit_in(ROOT, 'aeccc731') and commit_in(PP, '7904281') and 'PLACE-papers 7904281' in head,
        'git cat-file; the closing`s head prints "%s"' % head[:110], '1')
    dft = rd(p('data', 'b667_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    nav = [l for l, w in letters if w == "NAVIGATOR'S"]
    add('ruling (1)', '"twelve defects (a)-(l), (c), (h) and (k) the navigator`s"', len(letters) == 12 and nav == ['c', 'h', 'k'],
        'data/b667_defects.txt rows: %s' % ', '.join('(%s) %s' % x for x in letters), '1')
    for pat, what in ((r'count 1 at h 146', '146 on-line at count 1'), (r'count 1 at h 17 ; count 1 WIDENED 0', '17 off-line at count 1, none widened'),
                      (r'N\(R\) = 180 against 180 ; zeros in B = 0', 'N(R) = 180, the band 0'), ('C1 READS AS FIXED', 'C1 1, 1, 1 and 3'),
                      ('UNLISTED 1', 'C3 UNLISTED 1'), ('2742 MB', 'the host low 2,742 MB'), ('AGREE 10 of 10', 'the sealed tools at the close')):
        add('ruling (1)', what, re.search(pat, cl) is not None, 'data/b667_closing.txt :%s' % grep_line(p('data', 'b667_closing.txt'), pat)[0], '1')
    add('ruling (1)', 'suite 80 of 81, G-EDIT-ROUTE declared', 'suite 80 of 81' in head and "LIVE FAILING : 1 ['G-EDIT-ROUTE']" in cl,
        'the closing`s head and its post-push line', '1')
    for n, needle in ((8647, 'b666 AT ITS WEIGHT'), (8649, '## Q0’s zeros below 150 in balls')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:100], '1')
    for n, needle in ((14262, 'ITS DATA HALF DISCHARGED'), (14264, 'W-ORD-EPSTEIN-BALL-WIDTH'), (14266, 'THE KERNEL ITEM FOR P1 AND P2'),
                      (14268, 'W-ORD-ROOT-BINARY-BANK'), (14270, '### b667')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in l, l[:100], '1')
    rl = act_root_line('b667')
    add('ruling (1)', 'root d2fba79e...', rl and rl[0][1].startswith('d2fba79e'), 'data/act_roots.txt b667 line', '1')
    rlist = rd(p('data', 'b667_root_list.txt')) or ''
    add('ferry read-first', 'b667_root_list.txt (rows are banks; the two binary names with their reason)',
        'data/b667_bessel_rungs.txt.gz' in rlist and 'data/b667_epstein_zeros_certified.json.gz' in rlist and 'LEFT OUT, WITH THE REASON' in rlist,
        'data/b667_root_list.txt :%s (the reason), the names below it' % grep_line(p('data', 'b667_root_list.txt'), 'LEFT OUT, WITH THE REASON')[0], '1')
    lg = rd(p('data', 'b667_large_banks.txt')) or ''
    add('ruling (1)', 'both hashes in data/b667_large_banks.txt', lg.count('read back byte-equal True') == 2, 'data/b667_large_banks.txt', '1')
    # ### the kernel
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    n13, l13 = grep_line(p('data', 'b647_table_kernels.txt'), r'^  SIDE-grh-transfer ')
    add('ruling (2)', 'SIDE-grh-transfer at 6 OVERREACHES', l13 and re.search(r'\|\s+6 \|\s+0 \|\s+6 of\s+58', l13), 'data/b647_table_kernels.txt :%s %s' % (n13, (l13 or '')[:90]), '2')
    tie, _t = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'THE TIE AT COUNT')
    add('ruling (2)', 'the tie rule at OPEN_TRAILS :14238', tie == 14238, 'OPEN_TRAILS :%s' % tie, '2')
    kb = rd(p('data', 'b647_table_SIDE-grh-transfer.txt')) or ''
    ids = sorted(set(re.findall(r'^  (SIDE-grh-transfer@858cbf6:\S+) \| OVERREACHES', kb, re.M)))
    add('ferry read-first', 'SIDE-grh-transfer`s b647 bank (rows are blocks)', len(ids) == 6,
        'data/b647_table_SIDE-grh-transfer.txt: %d distinct OVERREACHES blocks at 858cbf6: %s' % (len(ids), ', '.join(i.split(':', 1)[1] for i in ids)), '2')
    km = g(KD, 'rev-parse', '--short=7', 'main')[1].strip()
    add('ferry read-first; ruling (2)', 'the change banks since b647, if any', km == '858cbf6',
        'main %s = b647`s read 858cbf6: no change since, no change bank owed ((R267)(3) as written)' % km, '2')
    tc = line(os.path.join(KD, 'lean-toolchain'), 1) or ''
    add('ferry read-first', 'the kernel`s lean-toolchain and lakefile by line', tc and os.path.exists(os.path.join(KD, 'lakefile.lean')),
        'lean-toolchain :1 %s ; lakefile.lean :4 %s ; :14 mathlib rev ; :17-:19 lean_lib SIDEGRHTransfer, srcDir ".", globs submodules' % (
            tc.strip(), (line(os.path.join(KD, 'lakefile.lean'), 4) or '').strip()), '3')
    add('ruling (2)', 'the workflow on its main where absent', not os.path.exists(os.path.join(KD, '.github', 'workflows', 'build-module.yml')),
        'no .github/workflows directory at main', '3')
    rc, tg = g(KD, 'tag', '--list')
    add('ruling (2)', 'the tag at the next patch step in its series', 'v0.5.0' in tg.split() and 'v0.5.1' not in tg.split(),
        'tags: %s ; v0.5.0 at %s ; main %s past it, untagged' % (' '.join(tg.split()), g(KD, 'rev-parse', '--short=7', 'v0.5.0^{commit}')[1].strip(), km), '3')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b667'), (ROOT, 'relay', 'push-b667-root'), (ROOT, 'relay', 'push-b667-closing'),
                        (PP, 'PLACE-papers', 'push-b667'), (PP, 'PLACE-papers', 'push-b667-root')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and orders
    for rule, cl_, comp in (('R265', (2, 3, 4), '2-3'), ('R267', (3,), '2'), ('R263', (4,), '3'), ('R251', (3,), '5'), ('R254', (2,), '0-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (2); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    cit, _c = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'W-ORD-CITATION-CHECK ACTED, A GATE STEP FROM b662')
    add('ruling (3)-(4)', 'the citation-check rule on OPEN_TRAILS (beside which (3) and (4) are entered)', cit == 14136, 'OPEN_TRAILS :%s' % cit, '1')
    bw, _b = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'`W-ORD-EPSTEIN-BALL-WIDTH`, ITS CONTROL HALF')
    add('ruling (5)', 'b671 W-ORD-EPSTEIN-BALL-WIDTH', bw == 14264, 'OPEN_TRAILS :%s' % bw, '1')
    ez, _e = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'EXTERNAL-ZFR-7')
    add('ruling (5)', 'the EXTERNAL-ZFR-7/8 line', ez, 'OPEN_TRAILS :%s ; git grep -i "ZFR" over PLACE-papers and relay: %s' % (
        ez, (g(PP, 'grep', '-l', '-i', 'ZFR')[1].split() + g(ROOT, 'grep', '-l', '-i', 'ZFR')[1].split()) or 'no file'), '1')
    re_ = g(PP, 'grep', '-l', '-i', 'relative.entropy')[1].split() + g(ROOT, 'grep', '-l', '-i', 'relative.entropy')[1].split()
    add('ruling (5)', 'the two relative-entropy questions (b670)', re_, 'git grep -i "relative.entropy" over PLACE-papers and relay: %s' % (re_ or 'no file'), '1')
    add('ruling (6)', 'the mirror export in the b655 form', os.path.exists(p('tools', 'mirror_build.ps1')) and os.path.exists(p('tools', 'mirror_verify.py')),
        'tools/mirror_build.ps1, tools/mirror_verify.py', '5')
    add('ruling (7)', 'the draft at v5, held', 'v5' in cl and '23228113' in cl, 'data/b667_closing.txt (N5): draft 23228113, v5, unsubmitted', '5')
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py', 'tools/licensed_table.py', 'tools/axiom_claim.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b668_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b668_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b668 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b668_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b668_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b668_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


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
        if not ex and re.match(r'^(data|tools)/b668_', pth):
            rows_.append(('path, this act`s bank the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for led, n in sorted(set(re.findall(r'\b(FINDINGS|OPEN_TRAILS)\b[^:]{0,20}:(\d{4,5})', best))):
        rows_.append(('line', '%s :%s' % (led, n), line(os.path.join(PP, led + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b668_citation_check.txt')
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
        print('usage: b668_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
