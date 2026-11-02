# -*- coding: utf-8 -*-
"""standing/dispatchrows.py -- v1.13.0, (R343)(2)(ii), b732 event (1): THE ONE WRITER OF data/<act>_dispatch_rows.json. b732's tool wrote free_mb on its read row alone and gate_ok, which asks it of every
push, dispatch and read row, failed after the lock with the hold read and met. Every row kind carries free_mb and the time of the read before it; a row without one, or under the hold, is refused here, before anything is written.

  free()               the host's free memory now: (mb, utc)
  row(kind, read, **f) a row, read the (mb, utc) pair; refuses a kind it does not know, a pair that is not one, a figure under the hold
  check(rows)          the rows that would be refused, [(index, kind, why)]
  write(path, rows)    the rows written, check() empty or nothing
"""
import json
import os
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if T not in sys.path:
    sys.path.insert(0, T)

HOLD = 2560
KINDS = ('commit', 'push', 'push2', 'dispatch', 'dispatch_refused', 'read')


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
    # ### v1.16.0, (R346)(3)(v), b735 defect (n): a watch killed is restarted or the run read in the foreground, the choice in the row
    if r.get('reaped') and r.get('watch') not in ('restarted', 'foreground'):
        return 'a reaped watch with no choice printed, restarted or foreground'
    return None


def row(kind, read, **f):
    r = dict(kind=kind, **f)
    r.update(free_mb=read[0], free_at=read[1])
    w = why(r)
    if w:
        raise ValueError('### THE ROW REFUSED, NOTHING WRITTEN: %s' % w)
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
