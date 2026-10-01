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
### (R179)(3), b569 -- THE PER-REPOSITORY LINES, ACROSS TWO REPOSITORIES:
###   (7) b566 at its own lines (relay data/b569_asof_b566.txt): the PLACE-papers, kernel and clone arms PASS;
###   (8) b566 pointed (`--as-of-lines`) at b567's heads for PLACE-papers and the kernel: the same arms FAIL;
###   (9) b567 at its own lines (relay data/b569_asof_b567.txt): its tag, scope, cache and clone arms PASS;
###   (10) b567 pointed at b568's PLACE-papers head and b566's kernel head: its tag and scope arms FAIL.
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

    # ### ### **(R179)(3), b569: THE LINES, ACROSS TWO REPOSITORIES (PLACE-papers and the kernel) AND A CLONE.** ### (7) b566 at
    # ### its own lines (the companion bank): the PLACE-papers arms, the kernel's tag arm and the clone arm PASS; (8) b566
    # ### pointed at lines naming b567's close for both repositories -- PLACE-papers 5340891 (b567's appended lines there,
    # ### the act commit b567's) and the kernel 6baed63 (main beyond v0.9) -- where its claims are false: the same arms FAIL;
    # ### (9) b567 at its own lines: its tag, scope and cache arms PASS; (10) b567 pointed at lines naming b568's
    # ### PLACE-papers close f2e93b0 and b566's kernel e5a5a83: its tag and scope arms FAIL.
    print('  (R179)(3) the as-of lines: the parser on synthetic lines, both polarities -- %s' % AF.self_test())
    r6, s6 = AF.repo_asof(D, 'b566')
    r7, s7 = AF.repo_asof(D, 'b567')
    want('(7) b566`s lines read from %s: PLACE-papers 5ce2895, the kernel e5a5a83, bulka 35df682f'
         % s6, (r6.get('PLACE-papers', '')[:7], r6.get('SIDE-explicit-formula', '')[:7], r6.get('bulka', '')[:8])
         == ('5ce2895', 'e5a5a83', '35df682f'))
    arms, line = run_suite('b566_checks.py', os.path.join(outdir, 'asof_b566_lines_own.txt'))
    for a in ('G-CEILING-APPENDED', 'G-CORPUS-SCOPE', 'G-TAG-READ-BACK', 'G-BULKA-KEPT'):
        want('(7) b566 at its own lines: %s PASS (read %s)' % (a, arms.get(a)), arms.get(a) == 'PASS')

    def false_lines(name, over, base):
        p = os.path.join(outdir, name)
        rows = dict(base, **over)
        open(p, 'w', encoding='utf-8', newline='\n').write(''.join(
            'push_gated: as-of %s %s\n' % (k, v if v not in (AF.DELETED, AF.PRESENT) else v.lower()) for k, v in sorted(rows.items())))
        return p
    f8 = false_lines('lines_b566_at_b567.txt', {'PLACE-papers': r7['PLACE-papers'], 'SIDE-explicit-formula': r7['SIDE-explicit-formula']}, r6)
    arms, line = run_suite('b566_checks.py', os.path.join(outdir, 'asof_b566_lines_false.txt'), ['--as-of-lines', f8])
    for a in ('G-CEILING-APPENDED', 'G-CORPUS-SCOPE', 'G-TAG-READ-BACK'):
        want('(8) b566 pointed at b567`s heads in two repositories (claims false there): %s FAIL (read %s)' % (a, arms.get(a)),
             arms.get(a) == 'FAIL')

    arms, line = run_suite('b567_checks.py', os.path.join(outdir, 'asof_b567_lines_own.txt'))
    for a in ('G-TAG-READ-BACK', 'G-CORPUS-SCOPE', 'G-CACHE-MAIN', 'G-BULKA-DELETED'):
        want('(9) b567 at its own lines (%s): %s PASS (read %s)' % (s7, a, arms.get(a)), arms.get(a) == 'PASS')
    pp568 = subprocess.run(['git', '-C', 'D:/MY-DOwnloads/PLACE-papers', 'rev-parse', 'f2e93b0'], capture_output=True, text=True).stdout.strip()
    f10 = false_lines('lines_b567_false.txt', {'PLACE-papers': pp568, 'SIDE-explicit-formula': r6['SIDE-explicit-formula']}, r7)
    arms, line = run_suite('b567_checks.py', os.path.join(outdir, 'asof_b567_lines_false.txt'), ['--as-of-lines', f10])
    for a in ('G-TAG-READ-BACK', 'G-CORPUS-SCOPE'):
        want('(10) b567 pointed at b568`s PLACE-papers and b566`s kernel (claims false there): %s FAIL (read %s)' % (a, arms.get(a)),
             arms.get(a) == 'FAIL')

    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
