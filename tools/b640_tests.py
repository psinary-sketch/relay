# -*- coding: utf-8 -*-
r"""b640_tests.py -- EVERY TEST FILE UNDER tools/, RUN AT STEP ZERO AND COUNTED, under (R238)(2), standing's standing line (every act runs
every test file under tools/ at step zero and prints the counts, so a failing case is found by the act after the edit that broke it).

### `run <test>`: one test per call in the foreground, its output kept whole, its cases counted by the numbered case pattern
### ((R233)(3), `^  \(\d+\) ` ending PASS or FAIL) and, where a test prints no numbered case, its exit code and last line read
### instead and said so; the result appended to data/b640_tests_stepzero.json. `report`: data/b640_tests_stepzero.txt from it.
### Arguments: the tests that take a list, a probe and a page are given the ζ page's list and probe in force (relay
### data/b638_nodes_zeta.txt, data/b635_probe_out_zeta.txt; the χ list and probe beside them) and the page at PLACE-papers HEAD; test_e0_rule.py its planted
### directory under the scratchpad. The tests' own writes are their own (temp directories; test_banned_terms_backmatter.py
### rewrites its two tracked fixtures); the trees' status is read after the run and printed.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/47d34df0-9823-4c9f-9efb-d1daddb7dd61/scratchpad'   # ### b640: b637's planted directory copied here whole (B637Planted.lean sha256 735629f5...)
BANK = os.path.join(D, 'b640_tests_stepzero.json')
COUNT_CASE = r'^  \(\d+\) '
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ZL, ZP = os.path.join(D, 'b638_nodes_zeta.txt'), os.path.join(D, 'b635_probe_out_zeta.txt')   # ### the ζ list in force since b638 (b632's with the glossary mark), its probe b635's (the Pages answer)
ZPAGE = os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
CL, CPR = os.path.join(D, 'b638_nodes_chi.txt'), os.path.join(D, 'b635_probe_out_chi.txt')   # ### the χ list in force since b638, its probe b635's
ARGS = {'test_chain_page.py': [ZL, ZP, ZPAGE, CL, CPR], 'test_g_chain_page.py': [ZL, ZP, ZPAGE],
        'test_e0_rule.py': [SP + '/b637_planted']}
# ### b637: the reader's test runs lean and is launched as a detached process (the build clause, OPEN_TRAILS :12356), so the foreground's
# ### 600 s limit does not bind it; its first run under the carried 580 s limit was stopped by the limit in its lean call (a cold page-in on
# ### this disk; b636 measured 459 s), nothing banked. Its limit is the detached watch's.
LIMIT = {'test_elab_reader_b634.py': 3000}


def tests():
    return sorted(f for f in os.listdir(T) if f.startswith('test_') and (f.endswith('.py') or f.endswith('.sh')))


def load():
    try:
        return json.load(io.open(BANK, encoding='utf-8'))
    except Exception:
        return {}


def save(j):
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(BANK + '.tmp', 'wb').write(b)
    os.replace(BANK + '.tmp', BANK)


def run(name):
    cmd = (['bash', os.path.join(T, name)] if name.endswith('.sh') else [sys.executable, os.path.join(T, name)]) + ARGS.get(name, [])
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT,
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'), timeout=LIMIT.get(name, 580))
    out = (r.stdout or '') + (r.stderr or '')
    cases = [l for l in out.split(NL) if re.match(COUNT_CASE, l)]
    passing = sum(1 for c in cases if c.rstrip().endswith('PASS'))
    failing = [re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')]
    last = [l for l in out.split(NL) if l.strip()][-1:] or ['']
    j = load()
    j[name] = dict(rc=r.returncode, seconds=int(time.time() - t0), cases=len(cases), passing=passing, failing=failing,
                   last=last[0][:200], args=[os.path.basename(a) for a in ARGS.get(name, [])], output=out)
    save(j)
    print('  %-34s exit %d ; cases %d ; passing %d ; failing %s ; %d s ; last: %s' % (name, r.returncode, len(cases), passing, failing or 'NONE',
                                                                                  j[name]['seconds'], last[0][:90]))


def report():
    j = load()
    L = ['b640 -- STEP ZERO: EVERY TEST FILE UNDER tools/, RUN AND COUNTED ((R238)(2), standing) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '']
    for n in tests():
        x = j.get(n)
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
          '', '### ### **TEST FILES %d ; RUN %d ; NOT CLEAN %d %s.**' % (len(tests()), sum(n in j for n in tests()), len(nf),
                                                                        ['%s %s' % (n, j[n]['failing'] or 'exit %d' % j[n]['rc']) for n in nf] or '')]
    L += ['', '### THE OUTPUTS, WHOLE:']
    for n in tests():
        if n in j:
            L += ['', '=== %s' % n] + j[n]['output'].rstrip(NL).split(NL)
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b640_tests_stepzero.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L[2:2 + len(tests()) + 4]))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'run':
        run(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == 'report':
        report()
    else:
        print('usage: b638_tests.py run <test> | report')
        sys.exit(2)
