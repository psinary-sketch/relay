# -*- coding: utf-8 -*-
"""b662_citation.py -- THE CITATION CHECK AS A GATE STEP, (R272)(4), b662's step zero; and the ferry banked after it.

### (R272)(4): before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b662_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R272) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well (a figure is a citation of a bank's content).
### Routes: `python tools/b662_citation.py check` -> data/b662_citation_check.txt (.json);
###         `python tools/b662_citation.py ferry`  -> data/b662_ferry.txt and data/b662_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b662; this tool writes only the four banks named above.
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
KD = 'D:/SIDE-carrier-spec'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R272) BEGIN', 'FERRY END (part 1 of 1)'
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


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
        if ANCHOR not in raw:
            continue
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('type') != 'user' or o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
        for t in texts:
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
    """a named rule's clauses in the ferry bank that carries its ruling."""
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


def mapj():
    try:
        return json.load(io.open(os.path.join(D, 'b661_detection_map.json'), encoding='utf-8'))['cells']
    except Exception:
        return []


def by_t(key):
    out = []
    for tt in ('14.1', '29.6', '50.0', '100.0'):
        out.append(sorted(set(c.get(key) for c in mapj() if c.get('t') == tt)))
    return out


def theta_off():
    v = []
    for c in mapj():
        m = re.match(r'\[?([0-9.]+)', c.get('theta') or '')
        if m:
            v.append(1 - float(m.group(1)))
    return max(v) if v else None


def head_constants():
    t = rd(os.path.join(T, 'b661_map.py')) or ''
    ls = t.split(NL)
    return [(i, l) for i, l in enumerate(ls[:30], 1) if re.match(r'^(GRID_SIGMA|GRID_T|T_HEIGHT|PREC|PREC_RUNG|J_EXTRA|J_MAX|H3_CELL)\b', l)]


def jmax_rule():
    t = rd(os.path.join(T, 'b661_map.py')) or ''
    return [(i, l.strip()) for i, l in enumerate(t.split(NL), 1) if re.search(r'jmax = D \+', l)]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    # ### the banks and files the read-first names
    for f in ('data/b661_closing.txt', 'data/b661_defects.txt', 'data/b661_detection_map.txt', 'data/b661_map_control.txt',
              'data/b647_table_kernels.txt', 'data/b647_table_SIDE-carrier-spec.txt', 'data/b657_sentence_grades.txt',
              'data/b650_same_season_last_year.txt', 'data/b661_closing_push_out.txt', 'data/b661_e1cfg_binding.txt', 'tools/b661_map.py',
              'data/b559_constants.txt'):
        add('ferry read-first / ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-1')
    dft = rd(p('data', 'b661_defects.txt')) or ''
    add('ruling (1), ferry read-first', 'data/b661_defects.txt (a)-(d)', all(re.search(r'^    \(%s\) ' % x, dft, re.M) for x in 'abcd')
        and not re.search(r'^    \(e\) ', dft, re.M), 'four lettered rows, (a) to (d)', '1')
    e2 = line(p('data', 'b559_constants.txt'), 153) or ''
    add('ruling (2), ferry read-first', "b559's (E2) reading", '(E2)' in e2, 'data/b559_constants.txt :153: %s' % e2.strip()[:90], '1')
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    m = re.search(r'^  SIDE-carrier-spec\s+(\w+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', kt, re.M)
    add('ruling (6)', 'SIDE-carrier-spec (9)', m and m.group(5) == '9', 'data/b647_table_kernels.txt: %s' % (m.group(0).strip() if m else 'no row'), '3')
    rev = m.group(1) if m else None
    rc, km = g(KD, 'rev-parse', '--short=7', 'main')
    add('ruling (6)', 'the kernel D:/SIDE-carrier-spec', rc == 0, 'main %s ; b647 read it at %s' % (km.strip(), rev), '3')
    rc, ch = g(KD, 'log', '--oneline', '%s..main' % rev) if rev else (1, '')
    add('ferry read-first', 'the change banks for SIDE-carrier-spec since b647', rc == 0, 'commits on main since %s: %d (%s)' % (
        rev, len([x for x in ch.split(NL) if x.strip()]), 'no change bank needed' if not ch.strip() else 'a change bank is needed'), '3')
    for f in ('lean-toolchain', 'lakefile.lean'):
        add('ferry read-first', "the kernel's %s" % f, os.path.exists(os.path.join(KD, f)), 'D:/SIDE-carrier-spec/%s' % f, '3-4')
    add('ruling (6)', "the workflow on its main where absent", True, 'absent at main: %s' % (not os.path.exists(os.path.join(KD, '.github', 'workflows', 'build-module.yml'))), '4')
    rc, tg = g(KD, 'tag', '--list')
    add('ruling (6)', 'the tag at the next in its series', rc == 0, 'tags: %s' % ' '.join(tg.split()), '4')
    # ### commits, roots, branches
    for repo, sha, what in ((ROOT, '6cca73cf', 'relay 6cca73cf (b661 closing)'), (PP, '13ee2d4', 'PLACE-papers 13ee2d4'),
                            (ROOT, '7ebd1c4d', 'commit 7ebd1c4d (b660, the in-place rewrite)')):
        add('ruling (1), (5)', what, commit_in(repo, sha), 'git cat-file at %s' % repo, '0-1')
    rl = act_root_line('b661')
    add('ruling (1)', 'root 9d223d09...', rl and rl[0][1].startswith('9d223d09'), 'data/act_roots.txt b661 line', '1')
    for repo, b in ((ROOT, 'push-b661'), (ROOT, 'push-b661-root'), (ROOT, 'push-b661-closing'), (PP, 'push-b661'), (PP, 'push-b661-root')):
        add('ferry Component 0', '%s %s' % ('relay' if repo == ROOT else 'PLACE-papers', b), branch_listed(repo, b), 'git branch --list', '0')
    # ### ledger lines and work-orders
    f85 = line(os.path.join(PP, 'FINDINGS.md'), 8485) or ''
    add('ruling (1)', 'FINDINGS :8485 (the b661 entry)', f85.startswith('## The detection-index map at Z'), f85[:80], '1')
    o70 = line(os.path.join(PP, 'OPEN_TRAILS.md'), 14070) or ''
    add('ruling (2)', "OPEN_TRAILS, the map's line", 'THE DETECTION MAP RE-ENTERED' in o70, 'OPEN_TRAILS :14070', '1')
    ot = rd(os.path.join(PP, 'OPEN_TRAILS.md')) or ''
    add('ruling (4)', 'W-ORD-CITATION-CHECK', 'W-ORD-CITATION-CHECK, ENTERED WITH ITS TRIGGER' in (line(os.path.join(PP, 'OPEN_TRAILS.md'), 13840) or ''),
        'OPEN_TRAILS :13840', '1')
    add('ruling (2)', 'W-ORD-E2-SEPARATION (to be entered by this act)', 'W-ORD-E2-SEPARATION' not in ot, 'not yet on OPEN_TRAILS, as it should be', '1')
    add('ruling (9)', 'W-ORD-EPSTEIN-ZQ', 'W-ORD-EPSTEIN-ZQ' in ot, 'OPEN_TRAILS :13493', '6')
    # ### rules
    for rule, cl, comp in (('R265', (2, 3, 4), '3-4'), ('R267', (3,), '3'), ('R263', (4,), '4'), ('R254', (2,), '1'), ('R251', (3,), '6'),
                           ('R271', (4, 5), '2'), ('R270', (8,), '1')):
        ok, how = rule_clause(rule, cl)
        add('ruling / ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl)), ok, how, comp)
    # ### tools and arms
    for f in ('tools/push_gated.sh', 'tools/mirror_build.ps1', 'tools/mirror_verify.py', 'tools/additive_shared.py', 'tools/act_root.py',
              'tools/b655_record.py', 'tools/b657_record.py'):
        add('ruling (5), (7); ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '1-6')
    add('ruling (1), (5)', 'G-SHARED-ADDITIVE and G-AXIOM-CLAIM', all(x in (rd(p('tools', 'b661_checks.py')) or '') for x in ("'G-SHARED-ADDITIVE'", "'G-AXIOM-CLAIM'")),
        'arms of tools/b661_checks.py', '1, 5')
    # ### the shared bank's rewritten line, from git (ruling (5))
    rc, old = g(ROOT, 'show', '58c8d3c8:data/b650_same_season_last_year.txt')
    oldl = [l for l in old.split(NL) if l.startswith("-- the author's confirmation")]
    add('ruling (5)', "the line 7ebd1c4d rewrote, as it stood before", len(oldl) == 1, 'at 7ebd1c4d^ (58c8d3c8): %r' % (oldl[0][:100] if oldl else None), '1')
    add('ruling (5)', "\"its heading line\"", False, "7ebd1c4d rewrote the section's LAST line (\"-- the author's confirmation ...\"), not its heading "
        "line (\"-- THE PROJECT DESCRIPTION'S STATE ...\" stands unchanged): the wording of (5) names another line", '1')
    # ### figures the ruling states about the b661 banks
    D_ = by_t('D')
    add('ruling (1)', 'D = 8, 14, 28, 66 at t = 14.1, 29.6, 50, 100', D_ == [[8], [14], [28], [66]], 'the map json: %s' % D_, '1')
    to = theta_off()
    add('ruling (1)', 'θ within 7.2·10⁻⁴ of 1 in every cell', to is not None and to < 7.2e-4, 'largest 1 - θ %.6g' % (to or -1), '1')
    ctl = rd(p('data', 'b661_map_control.txt')) or ''
    add('ruling (1), N3', 'hrate holds from j = 31 at (0.8, 29.6)', 'hrate first holds at j = 31' in ctl, 'data/b661_map_control.txt', '1-2')
    add('ruling (2)', "\"the sufficient index ... sits near 2³¹ at the control cell\"", False,
        'the control prints the INDEX j = 31 (the window`s power 2^(j+1) = 2^32); the index is 31, not 2^31 -- a figure to read as written '
        'or correct in the trail line', '1')
    add('ruling (2)', "\"J_max = D + 8 was short by half at the control cell\"", False,
        'at (0.8, 29.6) D + 8 = 22 against j = 31: short by 9 indices, 22 of 31 (71 per cent) -- "by half" is not the banks` figure', '1')
    # ### (R272)(3): the one constant
    hc = head_constants()
    jr = jmax_rule()
    add('ruling (3), ferry Component 2', "\"one constant at its head, J_max = 40 for every cell\"", False,
        'tools/b661_map.py`s head carries no J_max constant: %s; J_max is computed per cell at %s from D and J_EXTRA, so one constant '
        'at the head cannot set J_max = 40 for every cell without the rule line changing too' % (
            '; '.join(':%d %s' % (i, l.split('#')[0].strip()) for i, l in hc if 'J_' in l), '; '.join(':%d %s' % x for x in jr)), '2')
    add('ruling (3), N3', 'J_max = 40 at every cell against D', False,
        'D = 66 at t = 100 exceeds 40, so the theorem`s hj : D ≤ j leaves no index to read at the five t = 100 cells; N3`s "at least one cell '
        'per t prints an index" cannot hold at t = 100 under J_max = 40 -- unless J_max = max(40, D + 8) or j ≤ D + 40 is meant', '2')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b662 -- THE CITATION CHECK, (R272)(4), A GATE STEP AT STEP ZERO, RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b662_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b662_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b662_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT,
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    s = os.path.join(D, 'b662_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b662_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b662_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
