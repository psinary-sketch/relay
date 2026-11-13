# -*- coding: utf-8 -*-
"""standing/hold.py -- v1.25.0, (R355)(2)(ii), b744 events (3), THE TOOLS' [CLAIM ; NEW]: THE HOLD AT THE ROOT. b744's `record root_arm` ran with the
host's free memory at 2,360 MB, beneath the 2,560 MB hold the suite parts refuse themselves under (checks.tpl main, (R294)(2)); the record tool's
dispatch called every route with no reading. The hold now binds every record route as it binds the suite parts: the rendered record tool asks
refuses() before it calls any route, the route refusing itself and printing the figure (exit 3).

  refuses(route, hold=None, free=None) -> True when the host's free memory is beneath the hold (printed); the hold read from data/act_current.json
"""
import json
import os
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)


def hold_mb():
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f:
        return int(json.load(f).get('hold_mb') or 2560)


def free_mb():
    if T not in sys.path:
        sys.path.insert(0, T)
    import b703_checks as C3
    return C3.free_mb()


VOLUMES = ('C:\\', 'D:\\')   # ### v1.33.0, (R363)(7)(vii): the system volume (the temp directory, the harness's application data) and the data volume


def floor_mb():
    """the disk floor in MB, set at step zero in data/act_current.json (disk_floor_mb); the navigator's figure, 5,000 MB on each, where unset."""
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f:
        return int(json.load(f).get('disk_floor_mb') or 5000)


def disk_free_mb(vols=VOLUMES):
    import shutil
    return dict((v, shutil.disk_usage(v).free // (1024 * 1024)) for v in vols)


KEYS = (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending',
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired')


def restart_pending(read=None):
    """(pending, why): a restart of the operating system pending, read from the two registry keys the servicing stack and the update client
    set (Component Based Servicing\\RebootPending; WindowsUpdate\\Auto Update\\RebootRequired). `read` a planted answer (dict key -> bool)."""
    keys = KEYS
    if read is None:
        import winreg
        read = {}
        for k in keys:
            try:
                winreg.CloseKey(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, k))
                read[k] = True
            except OSError:
                read[k] = False
    hit = [k.split('\\')[-1] for k in keys if read.get(k)]
    return bool(hit), ', '.join(hit) or 'none'


# ### v1.34.0, (R364)(3)(xxi), the amendment rows 1 (1) and 3 (1) (data/b754_amendments.json): THE RESTART FLAG AFTER STEP ZERO. (R363)(7)(vii)
# ### read the flag at step zero alone; b753's close ran with it set and unread (set 2026-11-11T18:12:42Z), and at b754 it was set within the act
# ### (RebootPending 2026-11-12T16:35:36Z, RebootRequired 16:38:07Z) and read at 17:12:56Z after four commits, four restores and a record route
# ### (data/b754_events.txt (5)). refuses() reads it wherever it reads the memory and the volumes -- before each record route, each suite part
# ### (checks.tpl main) and the lock (tools/standing/commit.py) -- and a flag set is an event: printed at once with the time of each key's last
# ### write, the route not run, and the seat going on to the next commit boundary and stopping there for the author's word (the one-call tool
# ### prints the stop at that commit).
def _filetime(t):
    import datetime
    return (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=int(t) // 10)).strftime('%Y-%m-%dT%H:%M:%SZ')


def restart_times():
    """{key name: its last write, UTC} for each restart key that stands (the registry's own key time)."""
    import winreg
    out = {}
    for k in KEYS:
        try:
            h = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, k)
        except OSError:
            continue
        try:
            out[k.split('\\')[-1]] = _filetime(winreg.QueryInfoKey(h)[2])
        finally:
            winreg.CloseKey(h)
    return out


def flag_event(route, pending, why, times):
    """the event line of a flag set, or None where none is."""
    if not pending:
        return None
    return ('%s  ### THE RESTART FLAG SET (%s; the keys last written %s): AN EVENT OF THE ACT -- %s NOT RUN; THE SEAT GOES ON TO THE NEXT '
            'COMMIT BOUNDARY AND STOPS THERE FOR THE AUTHOR`S WORD ((R364)(3)(xxi))' % (
                time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), why, ', '.join('%s %s' % kv for kv in sorted((times or {}).items())) or 'not read', route))


def boundary_line(pending, why, times):
    """the one-call tool's line at a commit: the flag none, or set and this commit the boundary."""
    if not pending:
        return 'THE RESTART FLAG ((R364)(3)(xxi)): none'
    return ('THE RESTART FLAG ((R364)(3)(xxi)): SET (%s; the keys last written %s) -- THIS COMMIT IS THE BOUNDARY: THE SEAT STOPS HERE FOR THE '
            'AUTHOR`S WORD' % (why, ', '.join('%s %s' % kv for kv in sorted((times or {}).items())) or 'not read'))


def refuses(route, hold=None, free=None, disks=None, floor=None, flag=None, times=None):
    """True where the host's free memory is beneath the hold, or (v1.33.0, (R363)(7)(vii)) either volume's free space beneath the disk floor,
    or (v1.34.0, (R364)(3)(xxi)) the restart flag is set; each printed. The seat then stops: no waiting loop. `flag` a planted (pending, why),
    `times` planted key times."""
    h = hold_mb() if hold is None else hold
    fm = free_mb() if free is None else free
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    if fm < h:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: %s NOT RUN ((R355)(2)(ii))' % (stamp, fm, h, route))
        return True
    fl = floor_mb() if floor is None else floor
    dk = disk_free_mb() if disks is None else disks
    low = [(v, mb) for v, mb in sorted(dk.items()) if mb < fl]
    if low:
        print('%s  ### FREE SPACE BENEATH THE DISK FLOOR %d MB: %s -- %s NOT RUN; THE SEAT STOPS ((R363)(7)(vii))' % (
            stamp, fl, ', '.join('%s %d MB' % x for x in low), route))
        return True
    pending, why = restart_pending() if flag is None else flag
    ev = flag_event(route, pending, why, (restart_times() if flag is None else times) if pending else None)
    if ev:
        print(ev)
        return True
    return False


def control():
    """(ok, lines): the floor set above a planted reading, the route refusing; the floor beneath it, the route running; the restart reader
    given a planted answer each way; the live readings printed."""
    r1 = refuses('a planted route', hold=0, free=10 ** 6, disks={'C:\\': 4000, 'D:\\': 600000}, floor=5000, flag=(False, 'none'))
    r2 = refuses('a planted route', hold=0, free=10 ** 6, disks={'C:\\': 30000, 'D:\\': 600000}, floor=5000, flag=(False, 'none'))   # ### v1.34.0: the live flag kept out of the planted readings
    k = r'SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
    p1, w1 = restart_pending({k: True})
    p0, _w0 = restart_pending({})
    live, why = restart_pending()
    # ### v1.34.0, (R364)(3)(xxi): a planted flag after step zero refuses the route with the event and the keys' times; none planted, the route runs
    r3 = refuses('a planted route', hold=0, free=10 ** 6, disks={'C:\\': 30000, 'D:\\': 600000}, floor=5000, flag=(True, 'RebootRequired'),
                 times={'RebootRequired': '2026-11-12T16:38:07Z'})
    r4 = refuses('a planted route', hold=0, free=10 ** 6, disks={'C:\\': 30000, 'D:\\': 600000}, floor=5000, flag=(False, 'none'))
    ok = r1 and not r2 and p1 and not p0 and r3 and not r4
    return ok, ['### (hold) a planted reading C: 4,000 MB under the floor 5,000: %s ; C: 30,000 MB: %s ; a planted restart answer: %s (%s), none planted: %s ; '
                'a planted flag set after step zero: the route %s ; none set: %s ; '
                'LIVE: free %s, floor %d, restart pending %s (%s) ; THE CONTROL %s' % (
                    'REFUSED' if r1 else '### RAN', 'RAN' if not r2 else '### REFUSED', p1, w1, p0, 'REFUSED, THE EVENT PRINTED' if r3 else '### RAN',
                    'RAN' if not r4 else '### REFUSED', disk_free_mb(), floor_mb(), live, why, 'AS WANTED' if ok else 'NOT AS WANTED')]


if __name__ == '__main__':
    if sys.argv[1:2] == ['control']:
        ok, L = control()
        print('\n'.join(L))
        sys.exit(0 if ok else 1)
    sys.exit(__doc__)
