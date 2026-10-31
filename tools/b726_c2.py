# -*- coding: utf-8 -*-
"""b726_c2.py -- (R336)(3): THE C2 BUILD SPLIT PER FIELD ON c2-b725, READ BY RUN ID.

### routes:
###   dry <artifact dir>    the rows and the bank composed and printed, nothing written
###   bank <artifact dir>   data/b726_dispatch_rows.json and data/b726_c2.txt written
### Each run's artifact (build.log, axioms.txt, build_exit.txt, ref.txt, mem.log) is fetched by `gh run download` into <artifact dir>/run<id> where
### it is not there already, and read as data; each status and time by `gh run view <id>`. The free memory figures are the host's, read by the seat
### before each dispatch, typed in DISPATCHES with their times. Nothing here dispatches or runs Lean. Written by the Write tool.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, T)
import b725_c2 as C25      # noqa: E402  ### b725's E0 route, imported unedited
import e0_rule as E0       # noqa: E402

D = os.path.join(os.path.dirname(T), 'data')
BANK, ROWS = os.path.join(D, 'b726_c2.txt'), os.path.join(D, 'b726_dispatch_rows.json')
R = 'psinary-sketch/SIDE-explicit-formula'
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FIRST = 'c9add92f88f38a9cde45a71b4b135529e435ff30'    # ### the split, parent b725's tip
REPAIR = 'ea95a8d07a0ffae2012d715d5e95194cbf4df1ad'   # ### the binders, parent the split
BASE_TIP = '52cbbc11fd97cf3fd3749c1324f42a7041da49aa'
ORDER = (15, 20, 24, 40, 35, 52, 51, 88, 91, 123, 115, 148, 232, 187, 235, 267, 427, 403)   # ### the fields by n0, ascending
# ### (|D|, run, the ref built, the free memory read before the dispatch, its time)
DISPATCHES = ((15, 41147584871, FIRST, 5282, '2026-10-30T23:58:46Z'), (15, 41148340840, REPAIR, 5644, '2026-10-31T00:06:34Z'),
              (20, 41148615288, REPAIR, 5694, '2026-10-31T00:09:25Z'), (24, 41149195356, REPAIR, 5776, '2026-10-31T00:15:18Z'),
              (40, 41149723199, REPAIR, 5583, '2026-10-31T00:20:40Z'), (35, 41149939848, REPAIR, 5498, '2026-10-31T00:23:46Z'),
              (52, 41150124566, REPAIR, 5349, '2026-10-31T00:25:50Z'), (51, 41150327748, REPAIR, 5400, '2026-10-31T00:28:05Z'),
              (88, 41150696282, REPAIR, 5054, '2026-10-31T00:32:01Z'), (91, 41151096621, REPAIR, 5230, '2026-10-31T00:36:29Z'),
              (123, 41151758237, REPAIR, 5285, '2026-10-31T00:44:00Z'), (115, 41152040078, REPAIR, 4961, '2026-10-31T00:47:07Z'),
              (148, 41152352459, REPAIR, 5120, '2026-10-31T00:50:35Z'), (232, 41152579553, REPAIR, 5100, '2026-10-31T00:53:14Z'),
              (187, 41152916381, REPAIR, 4992, '2026-10-31T00:57:23Z'), (235, 41153237700, REPAIR, 4906, '2026-10-31T01:01:10Z'),
              (267, 41153599031, REPAIR, 4874, '2026-10-31T01:05:22Z'), (427, 41154021667, REPAIR, 5113, '2026-10-31T01:10:24Z'))
ID_NOTE = 'the global noreply form, read back by kind before the push'
COMMITS = (dict(kind='commit', kernel='SIDE-explicit-formula', branch='c2-b725', item='(3)', tree_state=2, sha=FIRST, parent=BASE_TIP,
                files=['SIDEExplicitFormula/C2Walk.lean', 'SIDEExplicitFormula/C2Field/M<|D|>.lean (18)', 'print_targets.txt'], identity=ID_NOTE),
           dict(kind='commit', kernel='SIDE-explicit-formula', branch='c2-b725', item='(3)', tree_state=3, sha=REPAIR, parent=FIRST,
                files=['SIDEExplicitFormula/C2Walk.lean'], identity=ID_NOTE))
PUSHES = (dict(kind='push', kernel='SIDE-explicit-formula', branch='c2-b725', sha=FIRST, remote_equal=True, at='2026-10-30T23:58:33Z', free_mb=5493,
               free_at='2026-10-30T23:50:45Z', capture='data/b726_SIDE-explicit-formula_c2-b725_push_out.txt'),
          dict(kind='push', kernel='SIDE-explicit-formula', branch='c2-b725', sha=REPAIR, remote_equal=True, at='2026-10-31T00:06:24Z', free_mb=5644,
               free_at='2026-10-31T00:04:33Z', capture='data/b726_SIDE-explicit-formula_c2-b725_push_out.txt'))


def gh(*a):
    return subprocess.run(['gh'] + list(a) + ['-R', R], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def art(root, run):
    dst = os.path.join(root, 'run%d' % run)
    if not os.path.exists(os.path.join(dst, 'build-module-%d' % run, 'ref.txt')):
        subprocess.run(['gh', 'run', 'download', str(run), '-R', R, '-D', dst], capture_output=True)
    return os.path.join(dst, 'build-module-%d' % run)


def rd(b, f):
    p = os.path.join(b, f)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def read_row(root, n, d, run, sha, nxt):
    v = json.loads(gh('run', 'view', str(run), '--json', 'status,conclusion,createdAt,updatedAt'))
    b = art(root, run)
    log, ax, ex, mem = rd(b, 'build.log'), rd(b, 'axioms.txt'), rd(b, 'build_exit.txt').strip(), rd(b, 'mem.log')
    tr = re.search(r'CERT D=-%d (KERNEL|SORRY)' % d, log)
    al = [l for l in ax.split(NL) if "cert_m%d'" % d in l]
    errs = [l[:160] for l in log.split(NL) if ': error' in l or l.startswith('error:')]
    low = re.search(r'LOW (\d+)', mem)
    sorry = any('sorryAx' in l for l in al) or 'SORRY' == (tr.group(1) if tr else '')
    verdict = ('STOPPED UNDER THE HOLD' if ex == '143' else 'FAILS' if ex != '0' else 'SORRY' if sorry or not tr else 'KERNEL')
    return dict(kind='read', kernel='SIDE-explicit-formula', item='(3) D=-%d' % d, n=n, run=run, status=v.get('status'), conclusion=v.get('conclusion'),
                built_ref=rd(b, 'ref.txt').split(NL)[0].strip(), toolchain='leanprover/lean4:v4.34.0-rc1', build_exit=ex, verdict=verdict, errors=errs,
                axioms_lines=al, sorryAx=sorry, traces={'cert_m%d' % d: tr.group(1) if tr else None}, runner_low_mb=int(low.group(1)) if low else None,
                at=v.get('updatedAt'), free_mb=nxt[0], free_at=nxt[1], artifact='scratchpad run%d (build.log, axioms.txt, mem.log, ref.txt, build_exit.txt)' % run), v


def compose(root):
    rows = [COMMITS[0], PUSHES[0]]
    for n, (d, run, sha, free, fat) in enumerate(DISPATCHES, 1):
        if n == 2:
            rows += [COMMITS[1], PUSHES[1]]
        nxt = (DISPATCHES[n][3], DISPATCHES[n][4]) if n < len(DISPATCHES) else (LAST_FREE[0], LAST_FREE[1])
        rr, v = read_row(root, n, d, run, sha, nxt)
        rows.append(dict(kind='dispatch', kernel='SIDE-explicit-formula', item='(3) D=-%d' % d, n=n, workflow='build-module.yml', at_ref='main', sha=sha,
                         target='SIDEExplicitFormula.C2Field.M%d' % d, run=run, at=v.get('createdAt'), free_mb=free, free_at=fat))
        rows.append(rr)
    return rows


# ### the read after the last dispatch: the free memory before the last run's read
LAST_FREE = (5030, '2026-10-31T01:14:35Z')
# ### the fields not compiled: (|D|, n0, pairs), the counts of the route's mirror (data/b725_c2.txt :28-:30)
LEFT_COUNTS = {267: (4761, 31556), 427: (14161, 109242), 403: (17303, 136930)}


def bank_lines(rows):
    txt = io.open(os.path.join(D, 'b722_c2_statement.txt'), encoding='utf-8').read().replace(chr(13), '')
    head = C25.C2.header_of(txt)
    g, why, _r = E0.grade(head, 'theorem')
    rds = [r for r in rows if r.get('kind') == 'read']
    good = [r for r in rds if r['verdict'] == 'KERNEL']
    k = len(set(r['item'] for r in good))
    done = set(int(r['item'].split('-')[-1]) for r in good)
    left = [d for d in ORDER if d not in done]
    n = len(rds)
    L = ['b726 -- (R336)(3): THE C2 BUILD SPLIT PER FIELD ON c2-b725, ONE JOB PER DISCRIMINANT, EIGHTEEN DISPATCHES AT MOST, EACH READ BY ITS RUN ID (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### Written by tools/b726_c2.py from each run`s own artifact; the rows at data/b726_dispatch_rows.json. No Lean ran on this host; the branch stays a branch.', '',
         '## (1) THE E0 GRADE, RE-READ AT THE HEADER, WHICH THE SPLIT LEFT UNCHANGED (relay tools/e0_rule.py, imported unedited; its self-test %s)' % ('PASS' if E0.self_test() else '### FAIL'),
         '  THE HEADER GRADED: theorem c2_value_law %s' % head, '  THE GRADE: %s -- %s' % (g, why),
         '  ROUTE (B) mirrored equal to the statement at 18 of 18 (data/b725_c2.txt :31); the repair below changes no term, so that row stands unre-run.', '',
         '## (2) THE BRANCH',
         '  tree state 2, %s over %s: the eighteen certificates each in its own module SIDEExplicitFormula/C2Field/M<|D|>.lean, one target per job.' % (FIRST[:8], BASE_TIP[:8]),
         '  dispatch 1 at it (run %d, D=-15) FAILS: C2Walk.lean does not elaborate at rQ (:50) and bL (:64). `(i : Int)` types the binder ahead of a Nat list.' % DISPATCHES[0][1],
         '  So the text b722 banked (data/b722_c2_statement.txt :35, :49) never elaborated, and b725`s empty build log hid that. That bank is not edited; this line names it.',
         '  tree state 3, %s over %s: binder annotations alone at rQ and bL; every term and C2ValueLaw`s header unchanged.' % (REPAIR[:8], FIRST[:8]), '',
         '## (3) THE FIELDS, EACH READ BY ITS RUN ID']
    for r in rds:
        ax = (r.get('axioms_lines') or ['NO AXIOM LINE'])[0]
        L.append('  dispatch %2d  %-10s run %d  ref %s  exit %s  %s  runner low %s MB  | %s' % (
            r['n'], r['item'].replace('(3) ', ''), r['run'], r['built_ref'][:8], r['build_exit'], r['verdict'], r['runner_low_mb'], ax))
    L += ['', '## (4) WHAT THE GRADE COVERS AND WHAT REMAINS',
          '  Compiled: the certificate `cert D n0 v q = true` at the fields above. No sorry, and no axiom at all where the line says so, inside the standard three the ruling names as the ceiling.',
          '  Not compiled: (L1) the sweep is r_Q on [0, n0]; (L2) W(n) = Omega(n) bL(n); the theorem c2_value_law from them. These stand as unproved Props, so C2ValueLaw itself is not compiled at any field.',
          '  The statement`s grade stays E0 DERIVES as graded at (1); a compiled certificate is not a compiled theorem.']
    if left:
        L.append('  FIELDS NOT COMPILED, each printed with its count ((R336)(3)) and carried:')
        for d in left:
            c = LEFT_COUNTS.get(d, (None, None))
            st = [r for r in rds if r['item'] == '(3) D=-%d' % d]
            how = ('its job stopped under the hold at run %d, exit 143, runner low %s MB, no certificate read' % (st[-1]['run'], st[-1]['runner_low_mb'])
                   if st else 'no dispatch: the eighteen were spent, one on the elaboration failure of dispatch 1, and n0 here is the largest of the 18')
            L.append('    D=-%d  n0 %s  pairs %s (data/b725_c2.txt :28-:30): %s' % (d, c[0], c[1], how))
    L += ['', '### ### **THE C2 THEOREM: E0 DERIVES ; ROUTE (B) EQUAL TO THE STATEMENT AT 18 OF 18 ; ON c2-b725 (%s) CERTIFICATES COMPILED AT %d OF 18 BY decide +kernel, %s ; NOT COMPILED: %s ; WHAT REMAINS: (L1), (L2), THE THEOREM ; DISPATCHES %d OF 18 ; NO MAIN, NO TAG.**' % (
        REPAIR[:8], k, 'EACH DEPENDING ON NO AXIOM' if good and all('does not depend on any axioms' in (r.get('axioms_lines') or [''])[0] for r in good) else 'WITHIN THE STANDARD THREE',
        ', '.join('D=-%d' % d for d in left) or 'NONE', n)]
    return L


def main(mode, root):
    rows = compose(root)
    L = bank_lines(rows)
    print(NL.join(L))
    if mode == 'bank':
        for p, s in ((ROWS, '[' + NL + (',' + NL).join('  ' + json.dumps(r, ensure_ascii=False) for r in rows) + NL + ']' + NL), (BANK, NL.join(L) + NL)):
            with open(p + '.tmp', 'wb') as f:
                f.write(s.encode('utf-8'))
            os.replace(p + '.tmp', p)
        print('written data/b726_c2.txt, data/b726_dispatch_rows.json')


if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in ('dry', 'bank'):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
