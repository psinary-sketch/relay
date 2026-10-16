# -*- coding: utf-8 -*-
r"""b674_tests.py -- EVERY TEST FILE UNDER tools/, RUN AT STEP ZERO AND COUNTED, under (R238)(2), standing's standing line (every act runs
every test file under tools/ at step zero and prints the counts, so a failing case is found by the act after the edit that broke it).
Carried from b673_tests.py at b674 under (R284), written whole by the Write tool (no copy, no redirect under tools/): the lists in force are
b649's zeta list (data/b649_nodes_zeta.txt) and b651's chi list (data/b651_nodes_chi.txt) with b643's probes, unchanged; the bank is
data/b674_tests_<stage>.*; a test withheld is read from data/b674_tests_withheld.json (this act: no lean run on this host, (R284)'s ferry);
each python test is started as `python -X utf8`, no environment mapping passed. By (R284)'s ferry the tests run one process per test in
the FOREGROUND under the 600 s limit: `parts` prints a partition of the tests by b673's recorded seconds into parts each under the limit,
and each part is run in one foreground call as one `run` per test.

### `run <test> [stage]`: one test per call, its output kept whole, its cases counted by the numbered case pattern
### ((R233)(3), `^  \(\d+\) ` ending PASS or FAIL) and, where a test prints no numbered case, its exit code and last line read
### instead and said so; the result appended to data/b674_tests_<stage>.json. `report [stage]`: data/b674_tests_<stage>.txt from it.
### Arguments: the tests that take a list, a probe and a page are given the zeta page's list and probe in force and the page at PLACE-papers
### HEAD; test_e0_rule.py its planted directory under b643's scratchpad. The tests' own writes are their own (temp directories;
### test_banned_terms_backmatter.py rewrites its two tracked fixtures); the trees' status is read after the run and printed.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e594f88a-2fab-4757-943d-7ab1bc3de815/scratchpad'   # ### b643: b637's planted directory copied here whole (B637Planted.lean sha256 735629f5...)
COUNT_CASE = r'^  \(\d+\) '
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ZL, ZP = os.path.join(D, 'b649_nodes_zeta.txt'), os.path.join(D, 'b643_probe_out_zeta.txt')
ZPAGE = os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
CL, CPR = os.path.join(D, 'b651_nodes_chi.txt'), os.path.join(D, 'b643_probe_out_chi.txt')
ARGS = {'test_chain_page.py': [ZL, ZP, ZPAGE, CL, CPR], 'test_g_chain_page.py': [ZL, ZP, ZPAGE],
        'test_e0_rule.py': [SP + '/b637_planted']}
LIMIT = {'test_elab_reader_b634.py': 3000, 'test_asof.py': 580}   # ### every foreground run under the 600 s limit ((R284)'s ferry)
BUDGET = 540                      # ### a part's planned seconds, beneath the 600 s limit


def bank(stage):
    return os.path.join(D, 'b674_tests_%s.json' % stage)


def tests():
    return sorted(f for f in os.listdir(T) if f.startswith('test_') and (f.endswith('.py') or f.endswith('.sh')))


def load(stage):
    try:
        return json.load(io.open(bank(stage), encoding='utf-8'))
    except Exception:
        return {}


def save(stage, j):
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(bank(stage) + '.tmp', 'wb').write(b)
    os.replace(bank(stage) + '.tmp', bank(stage))


def withheld():
    try:
        return json.load(io.open(os.path.join(D, 'b674_tests_withheld.json'), encoding='utf-8'))
    except Exception:
        return {}


def run(name, stage):
    if name in withheld():
        print('%s  %-34s ### WITHHELD: %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), name, withheld()[name]), flush=True)
        return
    cmd = (['bash', os.path.join(T, name)] if name.endswith('.sh') else [sys.executable, '-X', 'utf8', os.path.join(T, name)]) + ARGS.get(name, [])
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=LIMIT.get(name, 580))
        rc, out = r.returncode, (r.stdout or '') + (r.stderr or '')
    except subprocess.TimeoutExpired as e:
        rc, out = -9, ((e.stdout or b'').decode('utf-8', 'replace') if isinstance(e.stdout, bytes) else (e.stdout or '')) + NL + '### TIMED OUT AT %d s' % LIMIT.get(name, 580)
    cases = [l for l in out.split(NL) if re.match(COUNT_CASE, l)]
    passing = sum(1 for c in cases if c.rstrip().endswith('PASS'))
    failing = [re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')]
    last = [l for l in out.split(NL) if l.strip()][-1:] or ['']
    j = load(stage)
    j[name] = dict(rc=rc, seconds=int(time.time() - t0), cases=len(cases), passing=passing, failing=failing,
                   last=last[0][:200], args=[os.path.basename(a) for a in ARGS.get(name, [])], output=out)
    save(stage, j)
    print('%s  %-34s exit %d ; cases %d ; passing %d ; failing %s ; %d s ; last: %s' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), name, rc, len(cases), passing, failing or 'NONE', j[name]['seconds'], last[0][:90]), flush=True)


def parts(*a):
    """the tests partitioned by b673's recorded seconds (relay data/b673_tests_stepzero.json) into parts each planned under BUDGET; a test
    b673 did not time is planned at 60 s; a test planned alone above the budget is a part of its own."""
    prior = {}
    try:
        prior = dict((k, v.get('seconds', 60)) for k, v in json.load(io.open(os.path.join(D, 'b673_tests_stepzero.json'), encoding='utf-8')).items())
    except Exception:
        pass
    out, cur, s = [], [], 0
    for n in tests():
        if n in withheld():
            continue
        t = prior.get(n, 60)
        if cur and s + t > BUDGET:
            out.append((cur, s))
            cur, s = [], 0
        cur.append(n)
        s += t
    if cur:
        out.append((cur, s))
    for i, (ns, s) in enumerate(out, 1):
        print('PART %d (%d s planned): %s' % (i, s, ' '.join(ns)))


def report(stage):
    j = load(stage)
    L = ['b674 -- %s: EVERY TEST FILE UNDER tools/, RUN AND COUNTED ((R238)(2), standing) (%s)' % (
        'STEP ZERO' if stage == 'stepzero' else stage.upper(), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '']
    wh = withheld()
    for n in tests():
        x = j.get(n)
        if x is None and n in wh:
            L.append('  %-34s ### WITHHELD: %s' % (n, wh[n]))
            continue
        if x is None:
            L.append('  %-34s ### NOT RUN' % n)
            continue
        how = ('numbered cases %d, passing %d, failing %s ; its own last line: %s' % (x['cases'], x['passing'], x['failing'] or 'none', x['last'][:90])
               if x['cases'] else 'no numbered case printed; exit and last line read: %s' % x['last'][:120])
        L.append('  %-34s exit %d ; %s ; %d s%s' % (n, x['rc'], how, x['seconds'], (' ; args ' + ' '.join(x['args'])) if x['args'] else ''))
    rs = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--untracked-files=no'], capture_output=True, text=True).stdout.strip()
    ps = subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--untracked-files=no'], capture_output=True, text=True).stdout.strip()
    nf = [n for n in tests() if n in j and (j[n]['rc'] != 0 or j[n]['failing'])]
    L += ['', '### the trees after the runs: relay tracked changes %s ; PLACE-papers tracked changes %s' % (rs.replace(NL, ', ') or 'NONE', ps.replace(NL, ', ') or 'NONE'),
          '', '### ### **TEST FILES %d ; RUN %d ; WITHHELD %d ; NOT CLEAN %d %s.**' % (len(tests()), sum(n in j for n in tests()),
                                                                                     sum(n in wh and n not in j for n in tests()), len(nf),
                                                                                     ['%s %s' % (n, j[n]['failing'] or 'exit %d' % j[n]['rc']) for n in nf] or '')]
    L += ['', '### THE OUTPUTS, WHOLE:']
    for n in tests():
        if n in j:
            L += ['', '=== %s' % n] + j[n]['output'].rstrip(NL).split(NL)
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b674_tests_%s.txt' % stage)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[2:2 + len(tests()) + 4]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'run':
        run(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'stepzero')
    elif len(sys.argv) > 1 and sys.argv[1] == 'report':
        report(sys.argv[2] if len(sys.argv) > 2 else 'stepzero')
    elif len(sys.argv) > 1 and sys.argv[1] == 'parts':
        parts()
    else:
        print('usage: b674_tests.py run <test> [stage] | report [stage] | parts')
        sys.exit(2)
