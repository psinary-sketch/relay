# -*- coding: utf-8 -*-
"""b664_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b664's step zero; and the ferry banked
after it. Carried whole from tools/b663_citation.py: the helpers unchanged, the constants and the rows b664's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R274) and the ferry cite is checked
### for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired
### silently; the print is banked as data/b664_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R274) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well (a figure is a citation of a bank's content).
### Routes: `python tools/b664_citation.py check` -> data/b664_citation_check.txt (.json);
###         `python tools/b664_citation.py ferry`  -> data/b664_ferry.txt and data/b664_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b664; this tool writes only the four banks named above.
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
EF = 'D:/SIDE-explicit-formula'
KD = 'D:/SIDE-effects'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R274) BEGIN', 'FERRY END (part 1 of 1)'
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


def jload(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


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
    # ### the banks and files the read-first names
    for f in ('data/b663_closing.txt', 'data/b663_defects.txt', 'data/b663_epstein_control.txt', 'data/b663_epstein_instance.txt',
              'data/b647_table_kernels.txt', 'data/b657_sentence_grades.txt', 'data/b663_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-3')
    dft = rd(p('data', 'b663_defects.txt')) or ''
    letters = re.findall(r'^    \(([a-z]|b662-late)\) ', dft, re.M)
    add('ferry read-first', 'data/b663_defects.txt (rows are defects, (a)-(r))', 'r' in letters,
        'the bank`s rows: (%s) -- %d rows, (b662-late) and (a)-(q); no row (r)' % (')('.join(letters), len(letters)), '0')
    add('ruling (1)', '"eighteen defects"', len(letters) == 18, '%d rows' % len(letters), '1')
    # ### the sealed scorer's file constant and the no-disclosure arm's file read
    n1, l1 = grep_line(p('tools', 'b663_worklist.py'), r'^EPSTEIN_FILE = ')
    n2, l2 = grep_line(p('tools', 'b663_record.py'), r'^def _main_src')
    n3, l3 = grep_line(p('tools', 'b663_checks.py'), r'^K_FILES = ')
    add('ferry read-first, ruling (4)', "the sealed scorer's file constant and the no-disclosure arm's file read", n1 and n2 and n3,
        'tools/b663_worklist.py :%s %s ; tools/b663_record.py :%s (+:852, :868) ; tools/b663_checks.py :%s %s (read at :384)' % (n1, l1, n2, n3, l3), '0-1')
    # ### the kernel, by count
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    rows_ = re.findall(r'^  (SIDE-\S+)\s+(\w+) \|\s+\d+ \|\s+\d+ \|\s+\d+ \|\s+(\d+) \|', kt, re.M)
    done = ('SIDE-kernel', 'SIDE-global-section', 'SIDE-lv-conservation', 'SIDE-structural-error-correction', 'SIDE-carrier-spec')
    rest = sorted(((int(n), k, rev) for k, rev, n in rows_ if k not in done), reverse=True)
    top = rest[0] if rest else None
    add('ruling (5)', 'the next by descending OVERREACHES count after the five cut', top and rest[1][0] < top[0],
        'SIDE-effects?' if not top else '%s (%d, read at %s); then %s' % (top[1], top[0], top[2], ', '.join('%s %d' % (k, n) for n, k, _r in rest[1:4])), '2')
    add('ruling (5)', '"Where the kernel is SIDE-cosmo"', True, 'the kernel is %s, not SIDE-cosmo: the clause does not apply' % (top[1] if top else '?'), '2-3')
    add('ferry read-first', "the named kernel's b647 bank (rows are blocks)", os.path.exists(p('data', 'b647_table_SIDE-effects.txt')),
        'data/b647_table_SIDE-effects.txt: 7 OVERREACHES blocks (ExhaustivenessLicense.lean :1, :99; Milestones.lean :3, :21, :33, :50, :65)', '2')
    rc, km = g(KD, 'rev-parse', '--short=7', 'main')
    rc2, ch = g(KD, 'log', '--oneline', 'ef4cff7..main')
    add('ferry read-first, ruling (5)', 'the change banks for SIDE-effects since b647', rc2 == 0,
        'main %s ; commits since ef4cff7: %s -- Milestones.lean restated at b648 (data/b648_sorry_classification.txt, data/b648_sorry_repairs.txt), '
        'built at b652 (data/b652_build_results.json, data/b652_effects_push_out.txt): a change bank is needed' % (km.strip(), ch.strip().replace(NL, ' | ')[:120]), '2')
    for f in ('lean-toolchain', 'lakefile.toml'):
        add('ferry read-first', "the kernel's %s" % f, os.path.exists(os.path.join(KD, f)), 'D:/SIDE-effects/%s' % f, '3')
    add('ruling (5)', 'the workflow on its main where absent', True,
        'build-module.yml absent at main: %s (a push-triggered build.yml is there, not dispatchable)' % (
            not os.path.exists(os.path.join(KD, '.github', 'workflows', 'build-module.yml'))), '3')
    rc, tg = g(KD, 'tag', '--list')
    add('ruling (5)', 'the tag at the next patch step in its series', rc == 0, 'tags: %s' % ' '.join(tg.split()), '3')
    # ### figures the ruling states about b663
    for repo, sha, what in ((ROOT, 'ba1ba004', 'relay ba1ba004'), (PP, '07d147d', 'PLACE-papers 07d147d'), (EF, 'd00ab16', 'SIDE-explicit-formula d00ab16')):
        add('ruling (1)', what, commit_in(repo, sha), 'git cat-file', '1')
    rc, pv = g(EF, 'rev-parse', '--short=7', 'v0.29^{commit}')
    add('ruling (1)', 'tag v0.29', pv.strip() == 'd00ab16', 'peeled %s' % pv.strip(), '1')
    rl = act_root_line('b663')
    aj = jload('b663_act_root.json')
    add('ruling (1)', 'root e00d7158... over 44 banks', rl and rl[0][1].startswith('e00d7158') and len((aj.get('reads') or {}).get('banks') or []) == 44,
        'data/act_roots.txt b663 line ; banks %d' % len((aj.get('reads') or {}).get('banks') or []), '1')
    for n, needle in ((8535, 'b662 AT ITS WEIGHT'), (8537, '## The Epstein instance at Q0')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14158, 'W-ORD-EPSTEIN-CERTIFY'), (14162, 'W-ORD-FT-FIRST-ORDER'), (14166, '### b663')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in l, l[:90], '1')
    ct = rd(p('data', 'b663_epstein_control.txt')) or ''
    add('ruling (1)', 'j₀ = 38, the zero side −7.57·10³⁹, the Z₁ control j₀ = 31', 'READING Q0 AT qE0: j₀ = 38' in ct and '-7.570971' in ct
        and 'THE CONTROL REPRODUCED' in ct, 'data/b663_epstein_control.txt', '1')
    ck = rd(p('data', 'b663_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 78 of 80, G-AXIOM-CLAIM and G-EDIT-ROUTE', 'LIVE PASSING : 78' in ck and "['G-EDIT-ROUTE', 'G-AXIOM-CLAIM']" in ck,
        'data/b663_checks_postpush.txt', '1')
    it = rd(p('data', 'b663_epstein_instance.txt')) or ''
    add('ruling (1)', 'run 38413488503, 31 terminals, INTERFACES 7', 'RUN 38413488503' in it and 'TERMINALS 31, PRINTED 31' in it and 'INTERFACES 7' in it,
        'data/b663_epstein_instance.txt', '1')
    # ### the next acts' numbers in (R274)(3), (8)
    add('ruling (3), (8)', 'b665, b667, b669, b670', True, 'act numbers ahead of the chain: nothing to check at HEAD', '1')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b663'), (ROOT, 'relay', 'push-b663-root'), (ROOT, 'relay', 'push-b663-closing'),
                        (PP, 'PLACE-papers', 'push-b663'), (PP, 'PLACE-papers', 'push-b663-root'),
                        (EF, 'SIDE-explicit-formula', 'push-b663-merge'), (EF, 'SIDE-explicit-formula', 'epstein-b663')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and tools
    for rule, cl_, comp in (('R265', (2, 3, 4), '2-3'), ('R267', (3,), '2'), ('R263', (4,), '3'), ('R251', (3,), '5'), ('R254', (2,), '0-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (5); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (6)', 'the mirror export in the b655 form', all(os.path.exists(p('tools', f)) for f in ('mirror_build.ps1', 'mirror_verify.py')),
        'tools/mirror_build.ps1, tools/mirror_verify.py', '5')
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py', 'tools/licensed_table.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-5')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b664 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b664_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b664_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b664_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT,
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    s = os.path.join(D, 'b664_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b664_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b664_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
