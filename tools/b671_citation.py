# -*- coding: utf-8 -*-
"""b671_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b671's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b670_citation.py by the Write tool: the helpers unchanged (b670's repaired reader: only the seat's own prompts' results; an answer or
a note), the constants and the rows b671's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R281) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b671_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R281) BEGIN'), never from a scratch copy.
### Routes: `python tools/b671_citation.py check` -> data/b671_citation_check.txt (.json);
###         `python tools/b671_citation.py ferry`  -> data/b671_ferry.txt and data/b671_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b671_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED.
### Written by the Write tool at b671; this tool writes only the banks named above.
"""
import gzip
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
ANCHOR, TAIL = 'RULING (R281) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE)
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
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
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


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    for f in ('data/b670_closing.txt', 'data/b670_defects.txt', 'data/b670_rules.txt', 'data/b670_methods.txt', 'data/b670_state.txt',
              'data/b670_ten_acts.txt', 'data/b670_defects_by_kind.txt', 'data/b670_closing_push_out.txt', 'data/b667_h4_reading.txt',
              'data/b667_epstein_zeros_certified.json.gz', 'data/b667_large_banks.txt', 'data/b667_epstein_counts.txt', 'data/b667_epstein_plan.txt',
              'data/b667_certify_run2.txt', 'tools/b667_epstein_certify.py', 'tools/b667_epstein_map_balls.py', 'data/b663_epstein_control.txt'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    cl = rd(p('data', 'b670_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay 87410d3c, PLACE-papers c740f56, root 0c6086ef... over 44 banks', commit_in(ROOT, '87410d3c') and commit_in(PP, 'c740f56')
        and act_root_line('b670') and act_root_line('b670')[0][1].startswith('0c6086ef')
        and len([i for i in (json.loads(rd(p('data', 'b670_act_root.json')) or '{}').get('items') or []) if i.startswith('data/')]) == 44,
        'git cat-file; data/act_roots.txt b670; data/b670_act_root.json`s data items counted (the text bank prints no count); the closing`s head '
        '"%s" (its relay figure the record push fda49cbc, the closing push 87410d3c after it)' % head[:110], '1')
    for pat, what in (('suite 85 of 85', 'suite 85 of 85'), ('9 defects|8 defects', 'the closing`s defect count (nine with (i) after it)'),
                      (r'ROWS OUTSIDE LICENSED OR CITED 372 \(AT b648 607\)', '372 rows (607 at b648)'), (r'BEHIND 90', '90 of 100 behind'),
                      (r'METHODS 12 ; READY 9 ; NOT READY 1 ; NOT YET USED TWICE 2', 'the methods 9 READY of 12'),
                      (r'ENTRIES 11 ; CANDIDATES 0 ; NOT LOCATED', 'the ZFR search NOT LOCATED'), (r'\(i\) THE SEAT`S: THE CLOSING`S \(iii\)', 'defect (i)'),
                      (r'verification CLEAN', 'the mirror CLEAN')):
        h = grep_lines(p('data', 'b670_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b670_closing.txt :%s' % (h[0][0] if h else None), '1')
    st = rd(p('data', 'b670_state.txt')) or ''
    add('ruling (1)', 'the state line and its distances', 'STATE: reading 1 of 2 at b670' in st and '(i)   372 rows to zero' in st and '(iv)  33 orders' in st,
        'data/b670_state.txt', '1')
    rl = rd(p('data', 'b670_rules.txt')) or ''
    add('ruling (1)', 'data/b670_rules.txt rows 1-5', all(('ROW %d --' % i) in rl for i in range(1, 6)), 'data/b670_rules.txt', '1')
    dft = rd(p('data', 'b670_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    add('ruling (1)', '"nine defects, (a) the navigator`s, (i) entered after the closing"', len(letters) == 8 and letters[0] == ('a', "NAVIGATOR'S")
        and '(i) THE SEAT`S' in cl, 'data/b670_defects.txt (a)-(h): %s; (i) in data/b670_closing.txt after the closing' % ', '.join('(%s) %s' % x for x in letters), '1')
    for n, needle in ((8731, 'b669 AT ITS WEIGHT'), (8733, '## The reading at b670')):
        l = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14360, '### b670'), (14294, 'THE RESEARCH ORDER AFTER b668'), (14158, 'W-ORD-EPSTEIN-CERTIFY'), (14264, 'W-ORD-EPSTEIN-BALL-WIDTH'),
                      (14266, 'THE KERNEL ITEM FOR P1 AND P2'), (14350, 'W-ORD-STATUS-CELLS'), (14358, 'THE ORDER AFTER b670')):
        l = line(OT, n) or ''
        add('ruling (1), (2), (7); ferry', 'OPEN_TRAILS :%d' % n, needle in l, l[:110], '1-5')
    add('ruling (1)', 'chi-li-b669 at b804bf2', g(KE, 'rev-parse', '--short=7', 'chi-li-b669')[1].strip() == 'b804bf2', 'git rev-parse chi-li-b669', '0, 7')
    # ### (R281)(3): the object
    try:
        zj = json.load(gzip.open(p('data', 'b667_epstein_zeros_certified.json.gz')))
        kinds = {}
        for r in zj.get('rows') or []:
            kinds[r.get('kind')] = kinds.get(r.get('kind'), 0) + 1
    except Exception as e:
        zj, kinds = {}, {'error': str(e)}
    add('ruling (3)', 'the 163 points (146 on-line, 17 off-line) as squares of half-width 10^-12 at count 1', kinds.get('ON') == 146 and kinds.get('OFF') == 17
        and zj.get('h') == '1e-12', 'data/b667_epstein_zeros_certified.json.gz: rows %d by kind %s, h %s; the 17 PARTNER rows are the off-line points` '
        'reflections, counted in N(R) = 180 = 146 + 2·17 (data/b663_epstein_control.txt, b667`s dated line) and not among the 163' % (
            len(zj.get('rows') or []), kinds, zj.get('h')), '3')
    h4 = grep_lines(p('data', 'b667_h4_reading.txt'), r'controls 0 of 41|1e-18')
    add('ruling (3); (6) H4', 'hQtie 0 of 41; the tolerance near 10^-18 by line', len(h4) >= 2, 'data/b667_h4_reading.txt :%s' % ', :'.join(str(x[0]) for x in h4), '2')
    v1 = grep_lines(p('data', 'b667_certify_run2.txt'), r'V1 HOLDS|== V1')
    add('ruling (4) (M-on); ferry read-first', 'V1, the functional equation, by line', v1, 'data/b667_certify_run2.txt :%s' % ', :'.join(str(x[0]) for x in v1), '2')
    pl = grep_lines(p('data', 'b667_epstein_plan.txt'), r'^== ?1[1-6]\b|^== 1[1-6]\.')
    add('ferry read-first', 'data/b667_epstein_plan.txt sections 11-16', pl, 'section heads at :%s' % ', :'.join(str(x[0]) for x in pl), '2')
    add('ruling (3), (6) H3', 'the b663 control: j₀ = 38, the zero side below zero', grep_lines(p('data', 'b663_epstein_control.txt'), r'READING Q0 AT qE0: j₀ = 38'),
        'data/b663_epstein_control.txt :86', '4')
    # ### Arb's Hardy function and the real-ball sign test, by function name, in the library the scripts import
    try:
        import flint
        hz = [n for n in dir(flint.acb) if 'hardy' in n.lower()]
        sg = [n for n in ('sgn', '__gt__', '__lt__', 'contains') if hasattr(flint.arb, n)]
        ver = flint.__version__
    except Exception as e:
        hz, sg, ver = [], [], 'unimported: %s' % e
    add('ruling (5) C1; ferry read-first', 'Arb`s Hardy function, by function name', hz, 'python-flint %s: acb methods naming "hardy": %s (Arb`s C function '
        'acb_dirichlet_hardy_z is not wrapped in this binding)' % (ver, hz or 'NONE'), '3')
    add('ferry read-first', 'Arb`s real-ball sign test, by function name', sg, 'python-flint %s arb: %s' % (ver, sg), '3')
    # ### (R281)(8): the census items
    sm = grep_lines(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md'), r'\(R261\)`\(3\)\(d\)')
    sv = grep_lines(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'), r'\(R261\)`\(3\)\(d\)')
    lg = g(PP, 'log', '--format=%s', '-2', '--', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md')[1].split(NL)
    add('ruling (8)(a)', 'SIMPLICITY_OF_RIEMANN_ZEROS.md carries b651`s (R261)(3)(d) line, the v1_1_3 copy not; diverging after b558', sm and not sv
        and len(lg) > 1 and lg[1].startswith('b558'), 'the base copy :%s ; the versioned copy none ; the base copy`s commits before b651`s: "%s"' % (
            sm[0][0] if sm else None, lg[1][:40] if len(lg) > 1 else ''), '1')
    import zipfile
    try:
        man = zipfile.ZipFile('D:/MY-DOwnloads/mirror-refresh-2026-10-14-b670.zip').read('MANIFEST.md').decode('utf-8-sig')
    except Exception:
        man = ''
    cells = dict((m.group(1), m.group(2)) for m in re.finditer(r'^\| (\S+\.md) \| \d+ \| `[0-9a-f]+` \| (\S+) \|', man, re.M))
    for f, v in (('BALANCE_AND_POSITIVITY_v0_9_5.md', 'v0.4.0'), ('ENUMERA_v1_6.md', 'v0.2'), ('THE_KEYSTONE_CENSUS_v0_6.md', '-'),
                 ('THE_KEYSTONE_CENSUS_v0_7.md', '-'), ('THE_KEYSTONE_CENSUS_v0_7_1.md', '-')):
        add('ruling (8)(c)', 'MANIFEST cell %s reads %s' % (f, v), cells.get(f) == v, 'the b670 mirror`s MANIFEST: %s' % cells.get(f), '1')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b670'), (ROOT, 'relay', 'push-b670-root'), (ROOT, 'relay', 'push-b670-closing'),
                        (PP, 'PLACE-papers', 'push-b670'), (PP, 'PLACE-papers', 'push-b670-root'), (KE, 'SIDE-explicit-formula', 'chi-li-b669')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    for rule, cl_, comp in (('R274', (2,), '5'), ('R278', (4,), '0-7'), ('R251', (3,), '7'), ('R254', (2,), '0-7'), ('R277', (6,), '3-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (9)', 'the draft at v5, held', '23228113' in cl and 'v5' in cl, 'data/b670_closing.txt (N5)', '7')
    return R


def _write(L, R, miss):
    for name, data in (('b671_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b671_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b671 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b671_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b671_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b671_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")     # ### defect (g): an answer pasted with the curly apostrophe (NAVIGATOR’S) read as the straight
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b671_', pth):
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
    q = os.path.join(D, 'b671_citation_check.txt')
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
        print('usage: b671_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
