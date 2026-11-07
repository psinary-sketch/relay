# -*- coding: utf-8 -*-
"""tools/b745_controls.py -- (R355)(4): THE TWO CONTROLS ON ROUTE (K), BUILT ON zq-b730 PAST THE TAG v0.38 (14ca5725). Carried from
tools/b742_offlinezero.py's routes. No lean process runs on this host; every build is the runner's (SIDE-explicit-formula build-module.yml,
dispatched at main, the ref zq-b730's commit). Each dispatch row carries the commit of the author's word that licenses it
(standing.dispatchrows.licence): (R355)(4) in the ferry bank data/b745_ferry.txt, committed at step zero.

  md5s                  each plan bank's md5 against step zero's, and each committed before any Lean commit of b745
  reuse                 b738's clone at CLONE read back: on zq-b730 at the tag's commit (14ca5725), a clone row with its snapshot
  commit <sha> <item>   a commit row, the clone's snapshot beside it
  push <sha>            a push row, the free read taken now, the remote's tip read back
  dispatch <sha> <n> <item> <target>   the licence read, then gh workflow run; the row carrying the free read and the licence; the run id read back
  read <n> <run> <artifact dir>   a read row, verdict from the artifact's files
  errors <artifact dir> error blocks from the run's build.log
  closure <artifact dir> <name>   P6: the name's record in the closure step's out/closure.jsonl.gz -- the programme constants reached, its
                        axioms -- read for the generic theorem by name and for any finite-carrier lemma; every constant printed
  lines                 the measured lines of each order's sections against the plan's estimates (I-10's form), the three-times rule
  bank                  data/b745_controls.txt through standing.figbank: controls first, the dispatches, the lines, the axioms, the grade at the end
"""
import gzip
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
import b745_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import scratchfsck as SF         # noqa: E402

NL = '\n'
REPO = 'psinary-sketch/SIDE-explicit-formula'
CLONE = 'D:/zq-b738'      # ### b738's clone, outside the Temp tree (b737 defect (h)), on zq-b730 at the tag's commit; reused, read back
ROWS = os.path.join(D, 'b745_dispatch_rows.json')
ANSWERS = 'data/b745_ferry.txt'
WORD = '(4) THE BUILDS, on route (K), on zq-b730 past the tag'   # ### the licence's needle: (R355)(4), ferry :15
BANK = os.path.join(RELAY, K.CONTROLS_BANK)
NOTES = os.path.join(RELAY, K.CONTROLS_NOTES)
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
NS_PC = 'SIDEExplicitFormula.Schema.Wide.'
PC_FILE = 'SIDEExplicitFormula/Schema/Wide/PositiveControl.lean'
PC_MODULE = 'SIDEExplicitFormula.Schema.Wide.PositiveControl'
# ### the orders, in build order ((R355)(4)(c): the positive control's before any of the box's); each section (marker, the plan's estimate, names)
ORDERS = (('W-ORD-POSITIVE-CONTROL', K.POSCONTROL_PLAN, PC_FILE, (108, 290),
           (('P1', (40, 90), ('pcCarrier', 'pc_re', 'pc_reflect', 'pcCarrier_finite', 'pcConfig')),
            ('P2', (50, 150), ('pcCarrier_ncard_le', 'pc_N_le', 'pc_one_le_log', 'pc_count')),
            ('P3', (5, 15), ('pc_ne_zero',)),
            ('P4', (8, 20), ('online_imp_liCoeff_nonneg', 'pc_li_nonneg')),
            ('P5', (5, 15), ('pc_online',)))),)
PC_STATEMENTS = ('pc_count', 'pc_ne_zero', 'pc_li_nonneg', 'pc_online')   # ### the four statements (R355)(4)(a) prints with their axiom lines
GENERIC = 'SIDEExplicitFormula.Schema.Wide.li_nonneg_cfg_imp_online_ne_zero'
FORBIDDEN = ('zqFn', 'zqZeroConfig', 'ZQPremises', '.OffZero.', '.Schema.ZQ.', 'EpsteinZQ', 'LambdaQZeros')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def md5_lines():
    out, ok = [], True
    lean = [l for l in git(CLONE, 'log', '--format=%H %ct', K.ZQ_ENTERING + '..HEAD').split(NL) if l]
    first = min((int(l.split()[1]) for l in lean), default=None)
    for p in K.PLAN_BANKS:
        want = K.PLAN_MD5S[p]
        h = hashlib.md5(open(os.path.join(RELAY, p), 'rb').read()).hexdigest()
        st = int(git(RELAY, 'log', '-1', '--format=%ct', '--', p).strip())
        before = first is None or st < first
        ok = ok and h == want and before
        out.append('  %s md5 %s ; step zero`s %s ; equal %s ; committed %s ; before b745`s first Lean commit (%s) %s' % (p, h, want, h == want, st, first, before))
    out.append('  b745`s Lean commits on zq-b730 past %s: %d' % (K.ZQ_ENTERING[:8], len(lean)))
    return out, ok


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
    if br != K.ZQ_BRANCH or tip != K.ZQ_ENTERING:
        sys.exit('### THE CLONE IS NOT AS ENTERED')


def cmd_commit(sha, item):
    rows = _rows()
    full = git(CLONE, 'rev-parse', sha).strip()
    snap = SF.snapshot(CLONE)
    rows.append(DR.row('commit', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, item=item, sha=full, parent=git(CLONE, 'rev-parse', full + '^').strip(),
                       files=[x for x in git(CLONE, 'show', '--format=', '--name-only', full).split(NL) if x], snap=snap, at=_now()))
    DR.write(ROWS, rows, repo=CLONE)
    print({k_: rows[-1][k_] for k_ in ('item', 'sha', 'parent', 'files', 'free_mb')}, SF.line(snap))


def cmd_push(sha):
    rows = _rows()
    rem = subprocess.run(['git', '-C', CLONE, 'ls-remote', 'origin', 'refs/heads/' + K.ZQ_BRANCH], capture_output=True, text=True).stdout.split()
    full = git(CLONE, 'rev-parse', sha).strip()
    rows.append(DR.row('push', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, sha=full, remote=rem[0] if rem else None, remote_equal=bool(rem) and rem[0] == full, at=_now()))
    DR.write(ROWS, rows, repo=CLONE)
    print(rows[-1])
    if not rows[-1]['remote_equal']:
        sys.exit('### THE REMOTE`S TIP IS NOT THE COMMIT')


def cmd_dispatch(sha, n, item, target):
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT DISPATCHED' % read[0])
    if int(n) > K.MAX_DISPATCHES:
        sys.exit('### DISPATCH %s PAST THE ACT`S %d -- NOT DISPATCHED' % (n, K.MAX_DISPATCHES))
    rows = _rows()
    if any(r['kind'] == 'dispatch' and r['n'] == int(n) for r in rows):
        sys.exit('### DISPATCH %s ROWED ALREADY -- NOT DISPATCHED' % n)
    if int(n) != 1 + sum(1 for r in rows if r['kind'] == 'dispatch'):
        sys.exit('### DISPATCH %s IS NOT THE NEXT IN THE SERIES -- NOT DISPATCHED' % n)
    full = git(CLONE, 'rev-parse', sha).strip()
    bad = DR.targets_refused(target, DR.tree_files(CLONE, full))
    if bad:
        sys.exit('### TARGETS NOT MODULES OF THE TREE AT %s: %s -- NOT DISPATCHED' % (full[:8], bad))
    try:
        lic = DR.licence(ANSWERS, WORD, by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    print('  the licence: %s :%d, committed %s ; free %d MB at %s, the hold %d' % (lic['commit'][:8], lic['line'], lic['committed_at'], read[0], read[1], DR.HOLD))
    r = subprocess.run(['gh', 'workflow', 'run', 'build-module.yml', '--repo', REPO, '--ref', 'main', '-f', 'ref=' + full, '-f', 'target=' + target], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel='SIDE-explicit-formula', item=item, n=int(n), sha=full, target=target, at=read[1], error=(r.stderr or '')[:300]))
    else:
        rid = m.group(1) if m else ''
        if not rid:
            time.sleep(8)
            rid = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', REPO, '--workflow', 'build-module.yml', '--limit', '1', '--json', 'databaseId'], capture_output=True, text=True).stdout)[0]['databaseId']
        rows.append(DR.row('dispatch', read, kernel='SIDE-explicit-formula', item=item, n=int(n), workflow='build-module.yml', at_ref='main', sha=full, target=target, run=int(rid), at=read[1], licence=lic))
    DR.write(ROWS, rows, repo=CLONE)
    print(rows[-1])


def _art(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def _ax_of(axtext, name):
    """the axioms line of `name` in an axioms.txt: the standard three, a tuple, or None where not printed (a wrapped line read whole)."""
    m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(name), axtext)
    if m:
        return tuple(x.strip() for x in m.group(1).split(','))
    if re.search(r"'%s' does not depend on any axioms" % re.escape(name), axtext):
        return ()
    return None


def _names():
    return [NS_PC + n for _o, _p, _f, _e, secs in ORDERS for _s, _e2, ns in secs for n in ns]


def cmd_read(n, run, art):
    if not os.path.exists(os.path.join(art, 'build_exit.txt')):
        print('REFUSED: no build_exit.txt in', art, '(gh run download nests the artifact one level down); nothing written')
        return
    v = json.loads(subprocess.run(['gh', 'run', 'view', str(run), '--repo', REPO, '--json', 'status,conclusion,updatedAt,headSha'], capture_output=True, text=True, encoding='utf-8').stdout)
    ex = _art(art, 'build_exit.txt').strip()
    log = _art(art, 'build.log')
    ref = _art(art, 'ref.txt').strip().split()
    errs = [l for l in log.split(NL) if l.startswith('error: ') or ': error' in l]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    axt = _art(art, 'axioms.txt')
    ax = dict((nm, _ax_of(axt, nm)) for nm in _names())
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', _art(art, 'mem.log'))]
    rows = _rows()
    rows.append(DR.row('read', DR.free(), kernel='SIDE-explicit-formula', n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'], built_ref=ref[0] if ref else None,
                       toolchain=ref[-1] if ref else None, build_exit=ex, verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs[:40], sorry_warnings=len(warn_sorry),
                       axioms=dict((k_.split('.')[-1], list(v_) if v_ is not None else None) for k_, v_ in ax.items()), sorryAx='sorryAx' in axt,
                       closure_log=_art(art, 'closure_log.txt')[:300], closure=os.path.exists(os.path.join(art, 'closure.jsonl.gz')),
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact=art))
    DR.write(ROWS, rows, repo=CLONE)
    print({k_: rows[-1][k_] for k_ in ('n', 'run', 'conclusion', 'built_ref', 'build_exit', 'verdict', 'sorry_warnings', 'sorryAx', 'runner_low_mb', 'free_mb', 'closure')}, 'errors', len(errs))
    for nm, a in ax.items():
        print('    %-58s %s' % (nm, 'NOT PRINTED' if a is None else '[%s]' % ', '.join(a)))
    for l in errs[:20]:
        print('  ERR', l[:300])


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


def closure_of(art, name):
    p = os.path.join(art, 'closure.jsonl.gz')
    if not os.path.exists(p):
        return None
    with gzip.open(p, 'rt', encoding='utf-8') as fh:
        for l in fh:
            l = l.strip()
            if l.startswith('{') and '"n"' in l:
                r = json.loads(l)
                if r.get('n') == name:
                    return r
    return None


def closure_lines(art, name):
    r = closure_of(art, name)
    if r is None:
        return ['  the record of %s in %s: ABSENT' % (name, os.path.join(art, 'closure.jsonl.gz'))], None
    c = sorted(r.get('c') or [])
    gen = GENERIC in c
    forb = [x for x in c if any(f in x for f in FORBIDDEN)]
    fin = [x for x in c if re.search(r'finite|Finite|card|ncard|pc[A-Z_]', x.split('.')[-1])]
    L = ['  the record of %s: module %s ; kind %s ; line %s ; axioms [%s] ; programme constants reached %d' % (name, r.get('m'), r.get('k'), r.get('l'), ', '.join(r.get('a') or []), len(c)),
         '  the generic theorem %s by name in the closure: %s' % (GENERIC, gen),
         '  constants of Z_Q, its zeros or OffZero (%s): %s' % (', '.join(FORBIDDEN), forb or 'NONE'),
         '  constants whose names speak of finiteness, cardinality or the control (each read by hand below): %s' % (fin or 'NONE'),
         '  every programme constant reached, one a line:'] + ['    ' + x for x in c]
    return L, dict(generic=gen, forbidden=forb, finite_named=fin, reached=len(c), axioms=r.get('a'))


def cmd_closure(art, name):
    L, f = closure_lines(art, name)
    print(NL.join(L))


def _section_lines(path):
    """the lines of each `/-! ## <S>` section of the module, the header (doc comment and imports) apart: {section: n}, total."""
    if not os.path.exists(path):
        return None, None
    t = io.open(path, encoding='utf-8').read().rstrip(NL).split(NL)
    marks = [(i, re.match(r'^/-! ## (\w+)', l).group(1)) for i, l in enumerate(t) if re.match(r'^/-! ## (\w+)', l)]
    out = {'header': marks[0][0] if marks else len(t)}
    for j, (i, s) in enumerate(marks):
        end = marks[j + 1][0] if j + 1 < len(marks) else len(t)
        out[s] = end - i
    return out, len(t)


def lines_table():
    out, res = [], {}
    for order, _plan, f, (lo, hi), secs in ORDERS:
        sl, tot = _section_lines(os.path.join(CLONE, f))
        out.append('  %s, %s:' % (order, f))
        if sl is None:
            out.append('    NOT WRITTEN')
            res[order] = (None, False)
            continue
        out.append('    the header (doc comment, imports, namespaces) %d lines' % sl['header'])
        for s, (a, b), _ns in secs:
            n = sl.get(s)
            out.append('    %-3s measured %s ; the estimate %d-%d ; %s' % (s, n, a, b, 'NOT WRITTEN' if n is None else 'within' if a <= n <= b else 'BELOW' if n < a else 'ABOVE'))
        over = tot > 3 * hi
        out.append('    IN ALL: measured %d (the file, every line) ; the estimate %d-%d ; the ratio %.3f-%.3f ; three times %d ; %s' % (
            tot, lo, hi, tot / hi, tot / lo, 3 * hi, 'OVER THREE TIMES, STOPPED' if over else 'within the three-times rule'))
        res[order] = (tot, over)
    return out, res


def cmd_lines():
    print(NL.join(lines_table()[0]))


def cmd_bank(*notes):
    if not notes:
        notes = sorted((l.strip() for l in io.open(NOTES, encoding='utf-8') if l.startswith('(')), key=lambda l: int(l[1:l.index(')')])) if os.path.exists(NOTES) else ()
    rows = _rows()
    disp = [r for r in rows if r['kind'] == 'dispatch']
    reads = dict((r['n'], r) for r in rows if r['kind'] == 'read')
    ctl_std = _ax_of("'x' depends on axioms: [propext,\n Classical.choice, Quot.sound]", 'x') == STANDARD
    ctl_none = _ax_of("'y' does not depend on any axioms", 'y') == ()
    ctl_miss = _ax_of('', 'z') is None
    ctl_fig = FB.reading('## THE CONTROLS\n  a\n\n0.123')['ok'] and not FB.reading('0.123\n## THE CONTROLS\n  a')['ok']
    ctl_lic = bool(disp) and all(r.get('licence', {}).get('needle') == WORD for r in disp)
    free = DR.free()
    md5, md5_ok = md5_lines()
    tab, res = lines_table()
    kern = [r for n_, r in sorted(reads.items()) if r.get('build_exit') == '0']
    last = kern[-1] if kern else None
    L = ['b745 -- (R355)(4): THE TWO CONTROLS ON ROUTE (K), BUILT ON zq-b730 PAST THE TAG v0.38 (14ca5725) BY THE RUNNER (%s)' % _now(), '',
         '## THE CONTROLS',
         '  the axioms reader on a constructed standard line (wrapped): %s ; on a constructed axiom-free line: %s ; on an absent name, None: %s' % (ctl_std, ctl_none, ctl_miss),
         '  the figure-bank reader: the controls first passes, the controls after refused: %s' % ctl_fig] + md5 + [
         '  free memory at this bank: %d MB at %s, the hold %d' % (free[0], free[1], DR.HOLD),
         '  the dispatch rows refused by standing.dispatchrows: %s' % (DR.check(rows, CLONE) or 'NONE'),
         '  every dispatch row`s licence (R355)(4) at the ferry bank: %s' % ctl_lic, '',
         '## THE DISPATCHES: %d OF AT MOST %d, EACH READ BY ITS RUN ID, EACH ROW CARRYING free_mb AND ITS LICENCE' % (len(disp), K.MAX_DISPATCHES)]
    for r in disp:
        rd = reads.get(r['n'], {})
        L.append('  %d | %-6s | %s | sha %s | run %s | free %d MB | licence %s | %s, exit %s, %d errors, sorry warnings %s, sorryAx %s, runner low %s MB, read at free %s MB' % (
            r['n'], r['item'], ' '.join(t.split('.')[-1] for t in r['target'].split()), r['sha'][:8], r['run'], r['free_mb'], r.get('licence', {}).get('commit', 'NONE')[:8],
            rd.get('verdict', 'UNREAD'), rd.get('build_exit'), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('sorryAx'), rd.get('runner_low_mb'), rd.get('free_mb')))
    L += ['', '## THE LINES, MEASURED AGAINST THE PLANS` ESTIMATES (I-10`S FORM), AND THE THREE-TIMES RULE'] + tab + ['',
          '## THE AXIOMS OF EACH PRINTED NAME, IN FULL, FROM THE LAST KERNEL READ (run %s)' % (last['run'] if last else 'NONE')]
    built = []
    for order, _p, _f, _e, secs in ORDERS:
        for s, _e2, ns in secs:
            for nm in ns:
                a = (last or {}).get('axioms', {}).get(nm)
                ok = a is not None and set(a) <= set(STANDARD) and not (last or {}).get('sorryAx')
                if ok:
                    built.append(nm)
                L.append('  %-3s %-58s %s' % (s, NS_PC + nm, 'NOT BUILT' if a is None else '[%s]' % (', '.join(a) or 'none')))
    clo, cf = (closure_lines(last['artifact'], NS_PC + 'pc_online') if last else (['  NO KERNEL READ'], None))
    L += ['', '## P6: THE DEPENDENCY PRINT OF pc_online`S CLOSURE (the closure step`s out/closure.jsonl.gz, run %s)' % (last['run'] if last else 'NONE')] + clo
    pc_built = all(x in built for x in PC_STATEMENTS)
    p6 = bool(cf) and cf['generic'] and not cf['forbidden']
    pc_over = res.get('W-ORD-POSITIVE-CONTROL', (None, False))[1]
    grade_pc = 'STOPPED BY THE THREE-TIMES RULE' if pc_over else 'BUILT' if pc_built and p6 else 'NOT BUILT AT %s' % next(
        (s for _o, _p, _f, _e, secs in ORDERS[:1] for s, _e2, ns in secs if any(n not in built for n in ns)), 'P6')
    L += ['', '## THE NOTES (%s)' % K.CONTROLS_NOTES] + ['  ' + x for x in notes] + ['',
          '## THE GRADE, EACH ORDER ITS OWN',
          '  W-ORD-POSITIVE-CONTROL: the four statements %s ; the dependency print: the generic theorem by name %s, constants of Z_Q %s ; %s' % (
              ' ; '.join('%s %s' % (x, 'COMPILED' if x in built else 'NOT COMPILED') for x in PC_STATEMENTS), cf['generic'] if cf else 'UNREAD',
              (cf['forbidden'] or 'NONE') if cf else 'UNREAD', grade_pc),
          '  the axiom line, printed in full for each compiled name above: %s' % ', '.join(STANDARD), '',
          '### ### **W-ORD-POSITIVE-CONTROL %s ; DISPATCHES %d OF %d ; LINES %s AGAINST 108-290 ; NAMES COMPILED %d OF %d.**' % (
              grade_pc, len(disp), K.MAX_DISPATCHES, res.get('W-ORD-POSITIVE-CONTROL', (None,))[0], len(built), len(_names()))]
    r = FB.write(BANK, NL.join(L))
    print(NL.join(L))
    print('written %s ; figbank: %s' % (K.CONTROLS_BANK, r['why']))


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'md5s': cmd_md5s, 'reuse': cmd_reuse, 'commit': cmd_commit, 'push': cmd_push, 'dispatch': cmd_dispatch, 'read': cmd_read,
          'errors': cmd_errors, 'closure': cmd_closure, 'lines': cmd_lines, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
