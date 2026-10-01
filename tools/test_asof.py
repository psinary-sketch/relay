# -*- coding: utf-8 -*-
"""test_asof.py -- THE TEST OF THE SUITE'S AS-OF COMMIT, (R178)(2)(ii), written at b568.

### ### **TWO-SIDED, AS THE RULING ASKS:** a face re-run after its successor PASSES its tree-reading arms at the commit its
### closing push-out bank names; and the SAME arms, pointed (`--as-of`) at a commit where the face's claim is false, still
### FAIL. ### The cases:
###   (1) the bank parser on synthetic banks, both polarities (asof.self_test);
###   (2) the commits read from the two banks: b566 -> ce360e88..., b567 -> d77bb7aa...;
###   (3) b566's suite at its own as-of commit: G-NUMBER-UNCLAIMED, G-PEEK-DECLARED, G-PRIORBANK-UNCHANGED each PASS;
###   (4) b566's suite pointed at b567's close (d77bb7aa), where b567's registration exists and two b56x banks carry b567's
###       appended lines: G-NUMBER-UNCLAIMED FAILS and G-PRIORBANK-UNCHANGED FAILS;
###   (5) b567's suite at its own as-of commit: G-PRIORBANK-UNCHANGED PASSES;
###   (6) b567's suite pointed at 0e50bd19, b567's own commit before the ordered licence line was appended: the ordered
###       append is absent there, so G-PRIORBANK-UNCHANGED FAILS.
### The suites' records go to the directory given as the first argument (default: a fresh temporary directory), never to
### relay/data. Usage: python tools/test_asof.py [<outdir>]
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import asof as AF   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
B566 = 'ce360e88'
B567 = 'd77bb7aa'
B567_G = '0e50bd19'


def run_suite(suite, out, extra=()):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', suite), '--rerun-postpush', out] + list(extra),
                   capture_output=True, env=env)
    txt = open(out, encoding='utf-8').read() if os.path.isfile(out) else ''
    arms = {m.group(1): m.group(2) for m in re.finditer(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\b', txt, re.M)}
    asof = re.search(r'THE AS-OF COMMIT : (.*)$', txt, re.M)
    return arms, (asof.group(1) if asof else 'NOT PRINTED')


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp()
    os.makedirs(outdir, exist_ok=True)
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-100s %s' % (label, 'PASS' if cond else '### FAIL'))

    print('test_asof.py -- (R178)(2)(ii). records under %s' % outdir)
    want('(1) the push-out parser, both polarities on synthetic banks', AF.self_test())
    a6, a7 = AF.relay_asof(ROOT, D, 'b566') or '', AF.relay_asof(ROOT, D, 'b567') or ''
    want('(2) b566`s bank names %s... (read %s)' % (B566, a6[:12]), a6.startswith(B566))
    want('(2) b567`s bank names %s... (read %s)' % (B567, a7[:12]), a7.startswith(B567))

    arms, line = run_suite('b566_checks.py', os.path.join(outdir, 'asof_b566_own.txt'))
    print('    b566 at its own as-of: %s' % line)
    for a in ('G-NUMBER-UNCLAIMED', 'G-PEEK-DECLARED', 'G-PRIORBANK-UNCHANGED'):
        want('(3) b566 at %s: %s PASS (read %s)' % (B566, a, arms.get(a)), arms.get(a) == 'PASS')

    arms, line = run_suite('b566_checks.py', os.path.join(outdir, 'asof_b566_at_b567.txt'), ['--as-of', a7])
    print('    b566 pointed at b567`s close: %s' % line)
    for a in ('G-NUMBER-UNCLAIMED', 'G-PRIORBANK-UNCHANGED'):
        want('(4) b566 pointed at %s (claim false there): %s FAIL (read %s)' % (B567, a, arms.get(a)), arms.get(a) == 'FAIL')

    arms, line = run_suite('b567_checks.py', os.path.join(outdir, 'asof_b567_own.txt'))
    print('    b567 at its own as-of: %s' % line)
    want('(5) b567 at %s: G-PRIORBANK-UNCHANGED PASS (read %s)' % (B567, arms.get('G-PRIORBANK-UNCHANGED')),
         arms.get('G-PRIORBANK-UNCHANGED') == 'PASS')

    g = subprocess.run(['git', '-C', ROOT, 'rev-parse', B567_G], capture_output=True, text=True).stdout.strip()
    arms, line = run_suite('b567_checks.py', os.path.join(outdir, 'asof_b567_at_g.txt'), ['--as-of', g])
    print('    b567 pointed at its own commit before the ordered append: %s' % line)
    want('(6) b567 pointed at %s (the ordered append absent there): G-PRIORBANK-UNCHANGED FAIL (read %s)'
         % (B567_G, arms.get('G-PRIORBANK-UNCHANGED')), arms.get('G-PRIORBANK-UNCHANGED') == 'FAIL')

    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
