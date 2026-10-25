# -*- coding: utf-8 -*-
r"""b711_tests.py -- EVERY TEST FILE UNDER tools/, RUN AT STEP ZERO AND COUNTED, under (R238)(2), standing's standing line (every act runs
every test file under tools/ at step zero and prints the counts, so a failing case is found by the act after the edit that broke it).
Carried from b710_tests.py at b711 under (R321)'s ferry, written whole by the Write tool: the lists in force are b704's zeta list (the faces
page's :3 names it since b704's regeneration, PLACE-papers c9b2e55; b705 to b710 wrote no page) and b651's chi list with b704's and b643's
probes; the bank is data/b711_tests_<stage>.*; a test withheld is read from data/b711_tests_withheld.json (no lean run on this host); each
python test started as `python -X utf8`, no environment mapping passed; one process per test in the FOREGROUND under the 600 s limit. `parts`
gives every file whose b710 run exceeded 450 s a part of its own (data/b684_rules.txt row (1) applied to the test files); `mem` prints the
host's free memory, run before each part starts; `hold` prints the free memory against the 2,560 MB hold and exits 3 where it stands beneath
it, so a part is not run and the figure is printed.

### `run <test> [stage]`: one test per call, its cases counted by the numbered case pattern ((R233)(3), `^  \(\d+\) ` ending PASS or FAIL)
### and, where a test prints no numbered case, its exit code and last line read instead; the result appended to data/b711_tests_<stage>.json.
### `report [stage]`: data/b711_tests_<stage>.txt from it. `parts`, `mem`, `hold`: print only.
"""
import ctypes
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

ZL, ZP = os.path.join(D, 'b704_nodes_zeta.txt'), os.path.join(D, 'b704_probe_out_zeta.txt')   # ### the list the page names at :3 since b704
ZPAGE = os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
CL, CPR = os.path.join(D, 'b651_nodes_chi.txt'), os.path.join(D, 'b643_probe_out_chi.txt')
ARGS = {'test_chain_page.py': [ZL, ZP, ZPAGE, CL, CPR], 'test_g_chain_page.py': [ZL, ZP, ZPAGE],
        'test_e0_rule.py': [SP + '/b637_planted']}
LIMIT = {'test_elab_reader_b634.py': 3000, 'test_asof.py': 580, 'test_chain_page.py': 580}
BUDGET = 300               # ### a part planned at half the limit (b682 defect (b): a part ran 27% over its plan at low memory)
ALONE_ABOVE = 450           # ### data/b684_rules.txt row (1), applied to the test files
PRIOR = 'b710_tests_stepzero.json'
HOLD = 2560                 # ### the host memory hold, the author's word on every host ((R294)(2))
ACT = 'b711'


def bank(stage):
    return os.path.join(D, '%s_tests_%s.json' % (ACT, stage))


def tests():
    return sorted(f for f in os.listdir(T) if f.startswith('test_') and (f.endswith('.py') or f.endswith('.sh')))


def load(stage):
    try:
        return json.load(io.open(bank(stage), encoding='utf-8'))
    except Exception:
        return {}


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def save(stage, j):
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    _membrane(bank(stage))
    with open(bank(stage) + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(bank(stage) + '.tmp', bank(stage))


def withheld():
    try:
        return json.load(io.open(os.path.join(D, '%s_tests_withheld.json' % ACT), encoding='utf-8'))
    except Exception:
        return {}


def free_mb():
    class MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return int(m.ullAvailPhys // (1024 * 1024)), int(m.ullTotalPhys // (1024 * 1024))


def mem(*a):
    f, t = free_mb()
    print('%s  ### THE HOST`S FREE MEMORY %d MB of %d MB%s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), f, t,
                                                             (' -- before part %s' % a[0]) if a else ''), flush=True)
    return f


def hold(*a):
    f = mem(*a)
    if f < HOLD:
        print('%s  ### BENEATH THE HOLD %d MB: THE PART IS NOT RUN ((R294)(2))' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD), flush=True)
        sys.exit(3)
    print('  ### at or above the hold %d MB: the part may start' % HOLD, flush=True)


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
                   last=last[0][:200], args=[os.path.basename(a) for a in ARGS.get(name, [])], output=out, free_mb_after=free_mb()[0])
    save(stage, j)
    print('%s  %-34s exit %d ; cases %d ; passing %d ; failing %s ; %d s ; last: %s' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), name, rc, len(cases), passing, failing or 'NONE', j[name]['seconds'], last[0][:90]), flush=True)


def parts(*a):
    """the tests partitioned by b710's recorded seconds (relay data/b710_tests_stepzero.json): a file above ALONE_ABOVE its own part; the rest
    in parts each planned under BUDGET."""
    prior = {}
    try:
        prior = dict((k, v.get('seconds', 60)) for k, v in json.load(io.open(os.path.join(D, PRIOR), encoding='utf-8')).items())
    except Exception:
        pass
    out, cur, s = [], [], 0
    for n in tests():
        if n in withheld():
            continue
        t = prior.get(n, 60)
        if t > ALONE_ABOVE:
            out.append(([n], t))
            continue
        if cur and s + t > BUDGET:
            out.append((cur, s))
            cur, s = [], 0
        cur.append(n)
        s += t
    if cur:
        out.append((cur, s))
    for i, (ns, s) in enumerate(out, 1):
        print('PART %d (%d s planned%s): %s' % (i, s, ', ALONE' if len(ns) == 1 and s > ALONE_ABOVE else '', ' '.join(ns)))


def report(stage):
    j = load(stage)
    L = ['%s -- %s: EVERY TEST FILE UNDER tools/, RUN AND COUNTED ((R238)(2), standing) (%s)' % (
        ACT, 'STEP ZERO' if stage == 'stepzero' else stage.upper(), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '']
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
    longest = max((j[n]['seconds'] for n in tests() if n in j), default=0)
    L += ['', '### the trees after the runs: relay tracked changes %s ; PLACE-papers tracked changes %s' % (rs.replace(NL, ', ') or 'NONE', ps.replace(NL, ', ') or 'NONE'),
          '### the longest test %d s (the 600 s limit); tests over the 590 s guard, whose part the harness moved to the background: %s' % (
              longest, ' '.join('%s %d s' % (n, j[n]['seconds']) for n in tests() if n in j and j[n]['seconds'] > 590) or 'NONE'),
          '', '### ### **TEST FILES %d ; RUN %d ; WITHHELD %d ; NOT CLEAN %d %s.**' % (len(tests()), sum(n in j for n in tests()),
                                                                                     sum(n in wh and n not in j for n in tests()), len(nf),
                                                                                     ['%s %s' % (n, j[n]['failing'] or 'exit %d' % j[n]['rc']) for n in nf] or '')]
    L += ['', '### THE OUTPUTS, WHOLE:']
    for n in tests():
        if n in j:
            L += ['', '=== %s' % n] + j[n]['output'].rstrip(NL).split(NL)
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, '%s_tests_%s.txt' % (ACT, stage))
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[2:2 + len(tests()) + 5]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'run':
        run(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'stepzero')
    elif len(sys.argv) > 1 and sys.argv[1] == 'report':
        report(sys.argv[2] if len(sys.argv) > 2 else 'stepzero')
    elif len(sys.argv) > 1 and sys.argv[1] == 'parts':
        parts()
    elif len(sys.argv) > 1 and sys.argv[1] == 'mem':
        mem(*sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'hold':
        hold(*sys.argv[2:])
    else:
        print('usage: b711_tests.py run <test> [stage] | report [stage] | parts | mem [part] | hold [part]')
        sys.exit(2)
