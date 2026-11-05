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
    if w:
        raise Refused('### THE ROW REFUSED, NOTHING WRITTEN: %s' % w)
    return r


def check(rows):
    return [(i, r.get('kind'), why(r)) for i, r in enumerate(rows) if why(r)]


def write(path, rows):
    bad = check(rows)
    if bad:
        raise ValueError('### THE ROWS REFUSED, NOTHING WRITTEN: %s' % bad)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('[\n' + ',\n'.join('  ' + json.dumps(r, ensure_ascii=False) for r in rows) + '\n]\n')
    os.replace(tmp, path)
