# -*- coding: utf-8 -*-
"""standing/dispatchrows.py -- v1.13.0, (R343)(2)(ii), b732 event (1): THE ONE WRITER OF data/<act>_dispatch_rows.json. b732's tool wrote free_mb on its read row alone and gate_ok, which asks it of every
push, dispatch and read row, failed after the lock with the hold read and met. Every row kind carries free_mb and the time of the read before it; a row without one, or under the hold, is refused here, before anything is written.

  free()               the host's free memory now: (mb, utc)
  row(kind, read, **f) a row, read the (mb, utc) pair; refuses a kind it does not know, a pair that is not one, a figure under the hold
  check(rows)          the rows that would be refused, [(index, kind, why)]
  write(path, rows)    the rows written, check() empty or nothing

v1.22.0, (R352)(2)(i), b741 defect (q): A DISPATCH CONDITIONED ON THE AUTHOR'S WORD WAITS ON THE COMMIT THAT CARRIES THAT WORD. b741's dispatch 2
(run 41935365948, 23:38:52Z) rode on the word "(K) kernel route", which no relay commit carried in the answers bank until 1c74cfcf (05:17:32Z).
  licence(bank, needle, by=None)   the earliest relay commit on HEAD's line whose blob of `bank` carries `needle` on one line, committed at or
                                   before `by` (a UTC time) when given: dict(commit, bank, line, committed_at), or Refused naming what is missing
  row('dispatch', read, ...)       refused unless it carries licence=licence(...) re-read here, or unconditioned=True naming why no word is needed

v1.23.0, (R353)(3)(v), b742 defects (k), (l): targets_refused(targets, tree_files, modules) -- a target no .lean file of the tree, or not in the plan's
module list; label(rows) -- the repair commit's label from the dispatch count; series(rows, repo) -- a commit already rowed, a label not the count's,
a target not a module, for rows dated on or after LANDING; check() and write() read series() too.
"""
import calendar
import json
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if T not in sys.path:
    sys.path.insert(0, T)

HOLD = 2560
KINDS = ('commit', 'push', 'push2', 'dispatch', 'dispatch_refused', 'read', 'clone')   # ### v1.17.0: a clone operation is a row of its own


def free():
    import b703_checks as C3
    return C3.free_mb(), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def why(r):
    if r.get('kind') not in KINDS:
        return 'a row kind this writer does not know: %r' % (r.get('kind'),)
    if not isinstance(r.get('free_mb'), int) or not r.get('free_at'):
        return 'no free_mb and free_at from the read before it'
    if r['free_mb'] < HOLD:
        return 'free_mb %d under the hold %d' % (r['free_mb'], HOLD)
    # ### v1.16.0, (R346)(3)(iv), b735 defect (p): a read row naming a scratch clone carries its fsck before and after
    if r['kind'] == 'read' and r.get('clone') and not (r.get('fsck_before') and r.get('fsck_after')):
        return 'a read of %s without its fsck before and after' % r['clone']
    # ### v1.17.0, (R347)(2)(iv), b736 defect (m): a row naming a clone, a read, a dispatch or a clone operation, carries scratchfsck.snapshot
    # ### before and after it: the fsck, the disk's free space and the process listing, so a third loss has its cause's place printed
    if r['kind'] in ('read', 'dispatch', 'clone') and r.get('clone') and not all(isinstance(r.get(k), dict) and 'disk_free_mb' in r[k] and 'procs' in r[k]
                                                                                for k in ('snap_before', 'snap_after')):
        return 'a %s naming %s without its snapshots before and after (fsck, disk free, processes)' % (r['kind'], r['clone'])
    # ### v1.16.0, (R346)(3)(v), b735 defect (n): a watch killed is restarted or the run read in the foreground, the choice in the row
    if r.get('reaped') and r.get('watch') not in ('restarted', 'foreground'):
        return 'a reaped watch with no choice printed, restarted or foreground'
    return None


RELAY = os.path.dirname(T)


class Refused(ValueError):
    pass


def _epoch(utc):
    return calendar.timegm(time.strptime(utc, '%Y-%m-%dT%H:%M:%SZ'))


def licence(bank, needle, by=None, repo=RELAY):
    """the earliest commit on HEAD's first-parent line whose blob of `bank` carries `needle` on one line (and, with `by`, committed at or before it)."""
    log = subprocess.run(['git', '-C', repo, 'log', '--first-parent', '--reverse', '--format=%H %ct', 'HEAD', '--', bank], capture_output=True, text=True).stdout.split('\n')
    limit = _epoch(by) if by else None
    seen = []
    for l in [x for x in log if x.strip()]:
        sha, ct = l.split()[0], int(l.split()[1])
        seen.append(sha[:8])
        if limit is not None and ct > limit:
            break
        blob = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (sha, bank)], capture_output=True).stdout.decode('utf-8', 'replace').replace('\r', '').split('\n')
        hit = [i for i, x in enumerate(blob, 1) if needle in x]
        if hit:
            return dict(commit=sha, bank=bank, line=hit[0], needle=needle, committed_at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ct)))
    raise Refused('### NOT DISPATCHED: no commit %scarries the author`s word %r in %s (its commits on HEAD`s line: %s) -- commit the word to the answers bank first' % (
        ('at or before %s ' % by) if by else '', needle[:80], bank, ', '.join(seen) or 'NONE'))


def row(kind, read, **f):
    r = dict(kind=kind, **f)
    r.update(free_mb=read[0], free_at=read[1])
    w = why(r)
    # ### v1.22.0, (R352)(2)(i): a new dispatch row names the commit licensing it, re-read here at the row's time, or says it needs none
    if not w and kind == 'dispatch':
        lic = r.get('licence')
        if not lic and not r.get('unconditioned'):
            w = 'a dispatch with no licence: the commit carrying the author`s word it rides on (licence()), or unconditioned=<why>'
        elif lic:
            again = licence(lic['bank'], lic['needle'], by=r.get('at') or read[1])
            if again['commit'] != lic['commit']:
                w = 'the licence names %s where the bank`s first commit carrying the word is %s' % (lic['commit'][:8], again['commit'][:8])
    # ### v1.23.0, (R353)(3)(v): a dispatch row carrying its tree (or its kernel path in `repo`) has its targets read against it before it is written
    if not w and kind == 'dispatch' and (r.get('tree') or r.get('repo')):
        files = r.pop('tree', None) or tree_files(r['repo'], r['sha'])
        bad = targets_refused(r.get('target') or '', files, r.get('modules'))
        if bad:
            w = 'targets not modules of the tree at %s: %s' % (str(r.get('sha'))[:8], '; '.join(bad[:3]))
    if w:
        raise Refused('### THE ROW REFUSED, NOTHING WRITTEN: %s' % w)
    return r


# ### v1.23.0, (R353)(3)(v), b742 defects (k), (l): dispatch 4 (run 42061332755) carried the bare names "Interp Frame Strip ... SP4" as its
# ### targets, no module of the tree, and the commit 4c04916c was rowed twice, G4-G6 and again R5, beside the true R5 c2d4f29c. The targets
# ### are now read from the plan's module list and each must name a .lean file in the tree at the dispatched commit; a repair commit's label
# ### is composed from the dispatch count (the repair after dispatch n is Rn); a commit row whose sha is already rowed is refused. Enforced for
# ### rows dated on or after the landing, so the rows of earlier acts read as they were banked.
LANDING = '2026-11-06T00:00:00Z'


def targets_refused(targets, tree_files, modules=None):
    """the target names that are no module of the tree (Dotted.Name -> Dotted/Name.lean in `tree_files`) or, `modules` given (the plan's list),
    not in the plan's list."""
    names = targets.split() if isinstance(targets, str) else list(targets or [])
    files = set(tree_files or ())
    out = []
    for n in names:
        if n.replace('.', '/') + '.lean' not in files:
            out.append('%s: no file %s.lean in the tree' % (n, n.replace('.', '/')))
        elif modules is not None and n not in modules:
            out.append('%s: not in the plan`s module list' % n)
    return out


def tree_files(repo, sha):
    r = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', sha], capture_output=True, text=True)
    return [x for x in r.stdout.split('\n') if x]


def label(rows):
    """the label of the next repair commit: 'R<n>' after n dispatch rows."""
    return 'R%d' % sum(1 for r in rows if r.get('kind') == 'dispatch')


def series(rows, repo=None, since=LANDING):
    """[(index, kind, why)] for the rows dated on or after `since` (the landing; '' reads every row, the controls' replay of b742's bank): a
    commit row's sha already rowed; an R-label not the dispatch count's; a dispatch target that is no module of the tree at its sha (the tree
    read from `repo` when given, else from the row's `tree` list)."""
    def _dated(r):
        return (r.get('free_at') or r.get('at') or '') >= since
    out, shas = [], set()
    for i, r in enumerate(rows):
        if r.get('kind') == 'commit':
            if _dated(r) and r.get('sha') in shas:
                out.append((i, 'commit', 'the commit %s already rowed' % str(r.get('sha'))[:8]))
            elif _dated(r) and str(r.get('item') or '').startswith('R') and r.get('item') != label(rows[:i]):
                out.append((i, 'commit', 'the label %s where the dispatch count composes %s' % (r.get('item'), label(rows[:i]))))
            shas.add(r.get('sha'))
        elif r.get('kind') == 'dispatch' and _dated(r):
            files = r.get('tree') or (tree_files(repo, r['sha']) if repo and r.get('sha') else None)
            if files is not None:
                bad = targets_refused(r.get('target') or '', files, r.get('modules'))
                if bad:
                    out.append((i, 'dispatch', 'targets not modules of the tree: %s' % '; '.join(bad[:3])))
    return out


def check(rows, repo=None):
    return [(i, r.get('kind'), why(r)) for i, r in enumerate(rows) if why(r)] + series(rows, repo)


def write(path, rows, repo=None):
    bad = check(rows, repo)
    if bad:
        raise ValueError('### THE ROWS REFUSED, NOTHING WRITTEN: %s' % bad)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('[\n' + ',\n'.join('  ' + json.dumps(r, ensure_ascii=False) for r in rows) + '\n]\n')
    os.replace(tmp, path)
