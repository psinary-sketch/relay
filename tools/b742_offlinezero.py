# -*- coding: utf-8 -*-
"""tools/b742_offlinezero.py -- (R352)(3)(b) as amended by the author's word (data/b742_author_answers.txt :10, 1f96d4ea): S6, THE INTERPOLATION ROUTE
ON Lambda_Q TO SP4, groups G0-G6 of data/b742_s6_plan.txt (4). Carried from tools/b741_offlinezero.py's routes. No lean process runs on this host; every
build is the runner's (SIDE-explicit-formula build-module.yml, dispatched at main, the ref zq-b730's commit). Each dispatch row carries the commit of
the author's word that licenses it (standing.dispatchrows.licence, v1.22.0), read before `gh workflow run` is called.

  md5s                  the S6 plan bank's md5 against the worklist's, and the plan committed before any Lean commit of b742
  reuse                 b738's clone at CLONE read back: on zq-b730, at the entering tip (3329eaa1), a clone row with its snapshot
  commit <sha> <group>  a commit row, the clone's snapshot beside it
  push <sha>            a push row, the free read taken now, the remote's tip read back
  dispatch <sha> <n> <group> <target>   the licence read, then gh workflow run; the row carrying the free read and the licence; the run id read back
  read <n> <run> <artifact dir>   a read row, verdict from the artifact's files
  errors <artifact dir> error blocks from the run's build.log
  lines                 the measured lines of each group's modules against the estimates, and the three-times rule per group and in all, printed
  bank                  data/b742_offlinezero.txt through standing.figbank: controls first, the dispatches, the lines, the axioms, the grade at the end
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b742_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import scratchfsck as SF         # noqa: E402

NL = '\n'
REPO = 'psinary-sketch/SIDE-explicit-formula'
CLONE = 'D:/zq-b738'      # ### b738's clone, outside the Temp tree (b737 defect (h)), standing on zq-b730 at b741's tip; reused, read back
ROWS = os.path.join(D, 'b742_dispatch_rows.json')
MD5S = ((K.PLAN_BANK, K.PLAN_MD5),)
STATEMENTS_AT = K.C2_PLAN_FIRST[:8]   # ### b742: data/b742_s6_plan.txt's last commit (the note (7.1), 6b282935), before any Lean of b742
ANSWERS = 'data/b742_author_answers.txt'
WORD = 'The author’s word amending (R352)(3)'   # ### the licence's needle (data/b742_s6_plan.txt (5))
BANK = os.path.join(RELAY, K.BUILD_BANK)
ZQ = 'SIDEExplicitFormula/Schema/ZQ/OffZero/'
NS = 'SIDEExplicitFormula.Schema.ZQ.OffZero.'
# ### the groups of data/b742_s6_plan.txt (4), in build order; each (group, modules, the estimate, the printed names); the estimates the plan's (4)
GROUPS = (('G0', ('Frame',), (60, 150), ('lamF', 'lamF_differentiableOn', 'lamF_diffContOnCl_ball', 'zqFn_eq_lamF', 'lamF_min_modulus_zero', 'lamF_li_not_nonneg')),
          ('G1', ('Interp',), (400, 900), ('rootSum_inv_pow_mul_pow', 'kernel_eq', 'sub_discreteCauchy_eq', 'DiffContOnCl.norm_sub_discreteCauchy_le')),
          ('G2', ('Amplify',), (150, 400), ('norm_dcVec_sub_le', 'norm_poly_sub_le', 'DiffContOnCl.norm_sub_le_of_sphere')),
          ('G3', ('Strip',), (270, 660), ('norm_lamM_le', 'lamM_bound_numeric', 'lamF_sphere_le', 'lamM_conj')),
          ('G4', ('NodeBase', 'Nodes0', 'Nodes1', 'Nodes2', 'Nodes3', 'NodesF'), (2300, 3000),
           ('mid_sum_le', 'lamM_sub_shellSum_fine', 'F_n0', 'F_n19')),
          ('G5', ('Omega', 'FrontierData', 'Frontier'), (750, 1600),
           ('omg_inD', 'node_value_le', 'V_all', 'coef_le', 'lp_le', 'margin', 'lamF_frontier_ge')),
          ('G6', ('SP4',), (40, 100), ('zq_offline_zero', 'zq_li_nonneg_fails')))
ROWS_OF = dict((n_, g_) for g_, _m, _e, ns_ in GROUPS for n_ in ns_)
ROUTE = (3970, 6810)        # ### data/b742_s6_plan.txt (4) THE ROUTE IN ALL
CEILING = 3 * ROUTE[1]      # ### the three-times rule on the plan's own figure, data/b742_s6_plan.txt (5): 20,430
SP4_NAMES = ('zq_offline_zero', 'zq_li_nonneg_fails')
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def md5_lines():
    out, ok = [], True
    for p, want in MD5S:
        h = hashlib.md5(open(os.path.join(RELAY, p), 'rb').read()).hexdigest()
        ok = ok and h == want
        out.append('  %s md5 %s ; step zero`s %s ; equal %s' % (p, h, want, h == want))
    lean = [l for l in git(CLONE, 'log', '--format=%H %ct', K.ZQ_ENTERING + '..HEAD').split(NL) if l]
    st = int(git(RELAY, 'log', '-1', '--format=%ct', STATEMENTS_AT).strip())
    first = min((int(l.split()[1]) for l in lean), default=None)
    before = first is None or st < first
    out.append('  the S6 plan bank committed at relay %s, %s ; b742`s Lean commits on zq-b730 %d, the first at %s ; the bank before them %s' % (STATEMENTS_AT, st, len(lean), first, before))
    return out, ok and before


def cmd_md5s():
    out, ok = md5_lines()
    print(NL.join(out))
    if not ok:
        sys.exit('### A BANK MOVED OR THE ORDER BROKEN')


def cmd_reuse():
    if any(r['kind'] == 'clone' for r in _rows()):
        sys.exit('### THE CLONE ROWED ALREADY')
    read = DR.free()
    br = git(CLONE, 'branch', '--show-current').strip()
    tip = git(CLONE, 'rev-parse', 'HEAD').strip()
    dirty = [l for l in git(CLONE, 'status', '--porcelain').split(NL) if l]
    rem = subprocess.run(['git', '-C', CLONE, 'ls-remote', 'origin', 'refs/heads/' + K.ZQ_BRANCH], capture_output=True, text=True).stdout.split()
    before = SF.snapshot(os.path.dirname(CLONE) or 'D:/')
    snap = SF.snapshot(CLONE)
    rows = _rows()
    rows.append(DR.row('clone', read, kernel='SIDE-explicit-formula', branch=br, clone=CLONE, reused=True, tip=tip, tip_entering=tip == K.ZQ_ENTERING,
                       remote=rem[0] if rem else None, remote_equal=bool(rem) and rem[0] == tip, dirty=dirty, snap_before=before, snap_after=snap, at=read[1]))
    DR.write(ROWS, rows)
    print('  %s on %s at %s ; the entering tip %s ; the remote %s ; dirty %s ; %s' % (CLONE, br, tip[:8], tip == K.ZQ_ENTERING, (rem or ['NONE'])[0][:8], dirty or 'NONE', SF.line(snap)))
    if br != K.ZQ_BRANCH or tip != K.ZQ_ENTERING or dirty:
        sys.exit('### THE CLONE IS NOT AS ENTERED')


def cmd_commit(sha, item):
    rows = _rows()
    full = git(CLONE, 'rev-parse', sha).strip()
    snap = SF.snapshot(CLONE)
    rows.append(DR.row('commit', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, item=item, sha=full, parent=git(CLONE, 'rev-parse', full + '^').strip(),
                       files=[x for x in git(CLONE, 'show', '--format=', '--name-only', full).split(NL) if x], snap=snap))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('item', 'sha', 'parent', 'files', 'free_mb')}, SF.line(snap))


def cmd_push(sha):
    rows = _rows()
    rem = subprocess.run(['git', '-C', CLONE, 'ls-remote', 'origin', 'refs/heads/' + K.ZQ_BRANCH], capture_output=True, text=True).stdout.split()
    full = git(CLONE, 'rev-parse', sha).strip()
    rows.append(DR.row('push', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, sha=full, remote=rem[0] if rem else None, remote_equal=bool(rem) and rem[0] == full, at=_now()))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_dispatch(sha, n, item, target):
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT DISPATCHED' % read[0])
    if int(n) > K.MAX_DISPATCHES:
        sys.exit('### DISPATCH %s PAST THE ACT`S %d -- NOT DISPATCHED' % (n, K.MAX_DISPATCHES))
    if any(r['kind'] == 'dispatch' and r['n'] == int(n) for r in _rows()):
        sys.exit('### DISPATCH %s ROWED ALREADY -- NOT DISPATCHED' % n)
    try:
        lic = DR.licence(ANSWERS, WORD, by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    print('  the licence: %s :%d, committed %s' % (lic['commit'][:8], lic['line'], lic['committed_at']))
    r = subprocess.run(['gh', 'workflow', 'run', 'build-module.yml', '--repo', REPO, '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + target], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel='SIDE-explicit-formula', item=item, n=int(n), sha=sha, target=target, at=read[1], error=(r.stderr or '')[:300]))
    else:
        rid = m.group(1) if m else ''
        if not rid:
            time.sleep(8)
            rid = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', REPO, '--workflow', 'build-module.yml', '--limit', '1', '--json', 'databaseId'], capture_output=True, text=True).stdout)[0]['databaseId']
        rows.append(DR.row('dispatch', read, kernel='SIDE-explicit-formula', item=item, n=int(n), workflow='build-module.yml', at_ref='main', sha=sha, target=target, run=int(rid), at=read[1], licence=lic))
    DR.write(ROWS, rows)
    print(rows[-1])


def _art(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def cmd_read(n, run, art):
    if not os.path.exists(os.path.join(art, 'build_exit.txt')):
        print('REFUSED: no build_exit.txt in', art, '(gh run download nests the artifact one level down); nothing written')
        return
    v = json.loads(subprocess.run(['gh', 'run', 'view', str(run), '--repo', REPO, '--json', 'status,conclusion,updatedAt'], capture_output=True, text=True, encoding='utf-8').stdout)
    ex = _art(art, 'build_exit.txt').strip()
    log = _art(art, 'build.log')
    ref = _art(art, 'ref.txt').strip().split()
    errs = [l for l in log.split(NL) if l.startswith('error: ') or (': error:' in l and 'OffZero' in l)]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    ax = [l for l in _art(art, 'axioms.txt').split(NL) if l.strip()]
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', _art(art, 'mem.log'))]
    rows = _rows()
    rows.append(DR.row('read', DR.free(), kernel='SIDE-explicit-formula', n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'], built_ref=ref[0] if ref else None,
                       toolchain=ref[-1] if ref else None, build_exit=ex, verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs[:40], sorry_warnings=len(warn_sorry),
                       axioms_lines=[l for l in ax if 'OffZero' in l or "'" + NS in l or 'error' in l][-30:], sorryAx=any('sorryAx' in l for l in ax),
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact=art))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('n', 'run', 'conclusion', 'build_exit', 'verdict', 'sorry_warnings', 'sorryAx', 'runner_low_mb', 'free_mb')}, 'errors', len(errs))
    for l in rows[-1]['axioms_lines']:
        print('   ', l)


def cmd_errors(art):
    log = _art(art, 'build.log').split(NL)
    out, keep = [], 0
    for l in log:
        if re.search(r'^(error|warning: .*sorry)', l) or ': error' in l:
            keep = 16
        if keep:
            out.append(l)
            keep -= 1
    print(NL.join(out[:300]))
    print('### LOG LINES %d ; ERROR HEADS %d' % (len(log), len([l for l in log if l.startswith('error') or ': error' in l])))


def _lines(mod):
    p = os.path.join(CLONE, ZQ + mod + '.lean')
    return len(io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)) if os.path.exists(p) else None


def lines_table():
    out, tot, over = [], 0, []
    for g, mods, (lo, hi), _names in GROUPS:
        ns = [_lines(m) for m in mods]
        n = None if all(x is None for x in ns) else sum(x or 0 for x in ns)
        tot += n or 0
        if n is not None and n > 3 * hi:
            over.append(g)
        out.append('  %-3s %-40s measured %s ; the estimate %d-%d ; three times %d ; %s' % (g, ', '.join(ZQ + m + '.lean' for m in mods), n, lo, hi, 3 * hi,
                   'NOT WRITTEN' if n is None else 'OVER THREE TIMES, STOPPED' if n > 3 * hi else 'within' if lo <= n <= hi else 'BELOW' if n < lo else 'ABOVE'))
    out.append('  THE ROUTE IN ALL: measured %d ; the estimate %d-%d (data/b742_s6_plan.txt (4)) ; the ratio %.3f-%.3f' % (tot, ROUTE[0], ROUTE[1], tot / ROUTE[1], tot / ROUTE[0]))
    out.append('  THE THREE-TIMES RULE: the ceiling %d lines ; measured %d ; groups over their own figure %s ; %s' % (
        CEILING, tot, ', '.join(over) or 'NONE', 'STOP' if tot > CEILING or over else 'within, the build goes on'))
    return out, tot, over


def cmd_lines():
    print(NL.join(lines_table()[0]))


def _ax_any(reads, name):
    """the axioms line of `name` from the latest KERNEL read whose artifact prints it: (tuple or None, run)."""
    for n in sorted(reads, reverse=True):
        r = reads[n]
        if r.get('build_exit') == '0' and r.get('artifact'):
            a = _ax_of(_art(r['artifact'], 'axioms.txt'), name)
            if a is not None:
                return a, r['run']
    return None, None


def _ax_of(axtext, name):
    """the axioms line of `name` in an axioms.txt: the standard three, a tuple, or None where not printed."""
    m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(name), axtext)
    if m:
        return tuple(x.strip() for x in m.group(1).split(','))
    if re.search(r"'%s' does not depend on any axioms" % re.escape(name), axtext):
        return ()
    return None


def cmd_bank(*notes):
    if not notes:
        p = os.path.join(os.path.dirname(BANK), 'b742_offlinezero_notes.txt')
        notes = sorted((l.strip() for l in io.open(p, encoding='utf-8') if l.startswith('(')), key=lambda l: int(l[1:l.index(')')])) if os.path.exists(p) else ()
    rows = _rows()
    disp = [r for r in rows if r['kind'] == 'dispatch']
    reads = dict((r['n'], r) for r in rows if r['kind'] == 'read')
    ctl_std = _ax_of("'x' depends on axioms: [propext, Classical.choice, Quot.sound]", 'x') == STANDARD
    ctl_none = _ax_of("'y' does not depend on any axioms", 'y') == ()
    ctl_miss = _ax_of('', 'z') is None
    ctl_fig = FB.reading('## THE CONTROLS\n  a\n\n0.123')['ok'] and not FB.reading('0.123\n## THE CONTROLS\n  a')['ok']
    ctl_lic = all(r.get('licence', {}).get('commit', '')[:8] == K.STEPZERO_ANSWERS for r in disp)
    free = DR.free()
    md5, md5_ok = md5_lines()
    tab, tot, over = lines_table()
    L = ['b742 -- W-ORD-ZQ-OFFLINE-ZERO, S6 THE INTERPOLATION ROUTE ON Lambda_Q TO SP4 ((R352)(3)(b) AS AMENDED BY THE AUTHOR`S WORD), BUILT ON zq-b730 FROM 3329eaa1 BY THE RUNNER (%s)' % _now(), '',
         '## THE CONTROLS',
         '  the axioms reader on a constructed standard line: %s ; on a constructed axiom-free line: %s ; on an absent name, None: %s' % (ctl_std, ctl_none, ctl_miss),
         '  the figure-bank reader: the controls first passes, the controls after refused: %s' % ctl_fig] + md5 + [
         '  free memory at this bank: %d MB at %s, the hold %d' % (free[0], free[1], DR.HOLD),
         '  the dispatch rows refused by standing.dispatchrows: %s' % (DR.check(rows) or 'NONE'),
         '  every dispatch row`s licence the author`s word at %s: %s' % (K.STEPZERO_ANSWERS, ctl_lic), '',
         '## THE DISPATCHES: %d OF AT MOST %d, EACH READ BY ITS RUN ID, EACH ROW CARRYING free_mb AND ITS LICENCE' % (len(disp), K.MAX_DISPATCHES)]
    for r in disp:
        rd = reads.get(r['n'], {})
        L.append('  %d | group %-5s | %s | sha %s | run %s | free %d MB | licence %s | %s, exit %s, %d errors, sorry warnings %s, sorryAx %s, runner low %s MB, read at free %s MB' % (
            r['n'], r['item'], ' '.join(t.split('.')[-1] for t in r['target'].split()), r['sha'][:8], r['run'], r['free_mb'], r.get('licence', {}).get('commit', 'NONE')[:8],
            rd.get('verdict', 'UNREAD'), rd.get('build_exit'), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('sorryAx'), rd.get('runner_low_mb'), rd.get('free_mb')))
    L += ['', '## THE LINES, MEASURED AGAINST THE ESTIMATES (I-10`s form), AND THE THREE-TIMES RULE'] + tab + ['',
          '## THE AXIOMS OF EACH PRINTED NAME OF THE BUILD (data/b742_s6_plan.txt (4)), FROM THE LATEST KERNEL READ WHOSE ARTIFACT PRINTS IT']
    built, unbuilt = [], []
    for g, _mods, _e, names in GROUPS:
        for nm in names:
            a, run = _ax_any(reads, NS + nm)
            ok = a is not None and set(a) <= set(STANDARD)
            (built if ok else unbuilt).append(nm)
            L.append('  %-3s %-42s %s (run %s)' % (g, nm, 'NOT BUILT' if a is None else (', '.join(a) or 'none'), run))
    kernel = [r for r in reads.values() if r.get('build_exit') == '0']
    clean = not any(r.get('sorryAx') or r.get('sorry_warnings') for r in kernel)
    first_open = next((nm for _g, _m, _e, ns in GROUPS for nm in ns if nm in unbuilt), None)
    stopped = tot > CEILING or bool(over)
    reached = not stopped and first_open is None and clean
    grade = 'STOPPED BY THE THREE-TIMES RULE (%s, %d LINES)' % (', '.join(over) or 'the ceiling', tot) if stopped else 'REACHED' if reached \
        else 'NOT REACHED AT %s (%s)' % (ROWS_OF[first_open], first_open)
    L += ['', '## THE NOTES (data/b742_offlinezero_notes.txt)'] + ['  ' + x for x in notes] + ['',
          '## THE GRADE',
          '  printed names compiled with the standard three: %d of %d (%s)' % (len(built), len(built) + len(unbuilt), ', '.join(built) or 'none'),
          '  printed names not compiled: %s' % (', '.join('(%s) %s' % (ROWS_OF[x], x) for x in unbuilt) or 'none'),
          '  SP4`s statements: %s' % ' ; '.join('%s %s' % (x, 'COMPILED' if x in built else 'NOT COMPILED') for x in SP4_NAMES),
          '  the axiom line, printed in full for each name above: %s' % ', '.join(STANDARD), '',
          '### ### **SP4 %s ; DISPATCHES %d OF %d ; LINES %d AGAINST %d-%d (THE CEILING %d) ; NAMES %d OF %d.**' % (
              grade, len(disp), K.MAX_DISPATCHES, tot, ROUTE[0], ROUTE[1], CEILING, len(built), len(built) + len(unbuilt))]
    r = FB.write(BANK, NL.join(L))
    print(NL.join(L))
    print('written %s ; figbank: %s' % (K.BUILD_BANK, r['why']))


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'md5s': cmd_md5s, 'reuse': cmd_reuse, 'commit': cmd_commit, 'push': cmd_push, 'dispatch': cmd_dispatch, 'read': cmd_read,
          'errors': cmd_errors, 'lines': cmd_lines, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
