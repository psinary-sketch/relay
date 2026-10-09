# -*- coding: utf-8 -*-
"""build_watch.py -- THE WATCHDOG WITH THE STOP, W-ORD-WATCHDOG-STOP acted at b644 under (R254)(3).

### The seat's watchdog for ONE detached lean or lake call, carried from the scratchpad's build1.py (b600's standing line, OPEN_TRAILS
### :12356: started after free memory reads above the 2,560 MB hold, a SAMPLE line every 20 s with free memory and the child's working
### set, EXIT last) with the stop (R254)(3) rules:
###   a run whose watchdog samples free memory beneath the hold is STOPPED by PID -- its process tree's command lines printed, then
###   `taskkill /T /F /PID` -- the host freed by the seat's standing procedure (every lean, lake or python process whose parent is gone is
###   stopped by PID with its command line printed; then up to --free-wait seconds for free memory to read at or above the hold), and the
###   run retried once; a retry that samples beneath the hold again (or cannot start above it) is stopped and recorded RUN-BENEATH-HOLD
###   with its low and the module name -- a line in the log and a row appended to the --bank json -- and the watchdog exits 75: the act
###   proceeds with that module unbuilt and names the omission in its closing. No run continues beneath the hold unrecorded.
### The author's answer at b644: the hold stays at 2,560 MB, the seat does not lower it.
###   python tools/build_watch.py [--hold MB] [--start-hold MB] [--interval S] [--free-wait S] [--module NAME] [--bank JSON]
###                               <cwd> <log> <cmd> [args ...]
### --start-hold (default: the hold) is the start check alone; the planted test sets it to 0 and the hold above the host's free memory so
### the run starts and is stopped at its first sample. Exit: the child's code; 75 RUN-BENEATH-HOLD.
"""
import ctypes
import json
import os
import subprocess
import sys
import threading
import time

HOLD = 2560
RBH = 75


class MS(ctypes.Structure):
    _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]


def free_mb():
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return int(m.ullAvailPhys // (1024 * 1024))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def ws_mb(pid):
    try:
        out = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/FO', 'CSV', '/NH'], capture_output=True, text=True).stdout
        return int(out.strip().split('","')[-1].replace('"', '').replace(' K', '').replace(',', '').strip()) // 1024
    except Exception:
        return -1


def processes():
    """### {pid: (ppid, name, command line)} for every process on the host, read through PowerShell's Win32_Process."""
    ps = ('Get-CimInstance Win32_Process | ForEach-Object { "{0}`t{1}`t{2}`t{3}" -f $_.ProcessId,$_.ParentProcessId,$_.Name,'
          '($_.CommandLine -replace "`t"," ") }')
    out = subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-Command', ps], capture_output=True, text=True,
                         encoding='utf-8', errors='replace').stdout
    res = {}
    for l in out.split('\n'):
        x = l.rstrip('\r').split('\t')
        if len(x) >= 3 and x[0].isdigit():
            res[int(x[0])] = (int(x[1]) if x[1].isdigit() else -1, x[2], x[3] if len(x) > 3 else '')
    return res


def tree(pid, procs):
    """### pid and every descendant, parents first."""
    out, todo = [], [pid]
    while todo:
        p = todo.pop(0)
        if p in procs or p == pid:
            out.append(p)
            todo += [c for c, v in procs.items() if v[0] == p and c not in out]
    return out


def stop(pid, f, why):
    """### the stop by PID: the tree's command lines printed, then taskkill /T /F."""
    procs = processes()
    for p in tree(pid, procs):
        v = procs.get(p, (-1, '?', '?'))
        f.write('### STOP pid %d ppid %d %s : %s\n' % (p, v[0], v[1], v[2][:300]))
    r = subprocess.run(['taskkill', '/T', '/F', '/PID', str(pid)], capture_output=True, text=True)
    f.write('### STOPPED-BENEATH-HOLD %s pid %d (%s) taskkill exit %d\n' % (utc(), pid, why, r.returncode))


def free_host(f, hold, wait):
    """### the seat's standing procedure: orphans stopped by PID with their command lines, then a wait for the hold."""
    procs = processes()
    names = ('lean.exe', 'lake.exe', 'python.exe', 'python3.exe')
    me = os.getpid()
    orphans = [p for p, v in procs.items() if v[1].lower() in names and v[0] not in procs and p != me]
    for p in orphans:
        f.write('### ORPHAN STOPPED pid %d %s : %s\n' % (p, procs[p][1], procs[p][2][:300]))
        subprocess.run(['taskkill', '/T', '/F', '/PID', str(p)], capture_output=True)
    f.write('### HOST FREED %s : orphans stopped %d ; free %d MB\n' % (utc(), len(orphans), free_mb()))
    t0 = time.time()
    while free_mb() < hold and time.time() - t0 < wait:
        time.sleep(min(5, max(wait, 0.5)))
    f.write('### HOST READ %s : free %d MB after %d s (hold %d)\n' % (utc(), free_mb(), int(time.time() - t0), hold))


def attempt(n, cwd, cmd, f, hold, start_hold, interval):
    """### one run: (rc, low, stopped)."""
    fm = free_mb()
    if fm < start_hold:
        f.write('### REFUSED attempt %d %s free %d MB below the hold %d -- NOT STARTED\n' % (n, utc(), fm, start_hold))
        return None, fm, True
    t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    f.write('### START attempt %d %s free %d MB pid %d cmd %s cwd %s\n' % (n, utc(), fm, p.pid, ' '.join(cmd), cwd))
    peak, low, stopped = [0], [fm], [False]
    done = threading.Event()

    def sampler():
        while not done.wait(interval):
            w, fr = ws_mb(p.pid), free_mb()
            peak[0], low[0] = max(peak[0], w), min(low[0], fr)
            f.write('### SAMPLE %s free %d MB child working set %d MB\n' % (utc(), fr, w))
            if fr < hold and p.poll() is None:
                stopped[0] = True
                stop(p.pid, f, 'free %d MB beneath the hold %d' % (fr, hold))
                return

    threading.Thread(target=sampler, daemon=True).start()
    for raw in p.stdout:
        f.write(raw.decode('utf-8', 'replace').rstrip('\r\n') + '\n')
    rc = p.wait()
    done.set()
    f.write('### EXIT %d %s %d s peak %d MB low %d MB free %d MB%s\n' % (rc, utc(), int(time.time() - t0), peak[0], low[0], free_mb(),
                                                                       ' (stopped beneath the hold)' if stopped[0] else ''))
    return rc, low[0], stopped[0]


def opt(a, name, default, kind=int):
    if name in a:
        i = a.index(name)
        v = kind(a[i + 1])
        del a[i:i + 2]
        return v
    return default


def main(argv):
    a = list(argv)
    hold = opt(a, '--hold', HOLD)
    start_hold = opt(a, '--start-hold', hold)
    interval = opt(a, '--interval', 20.0, float)
    wait = opt(a, '--free-wait', 300.0, float)
    module = opt(a, '--module', '', str)
    bank = opt(a, '--bank', '', str)
    cwd, log, cmd = a[0], a[1], a[2:]
    f = open(log, 'a', encoding='utf-8', buffering=1)
    rc, low, stopped = attempt(1, cwd, cmd, f, hold, start_hold, interval)
    if not stopped:
        return rc
    free_host(f, hold, wait)
    rc2, low2, stopped2 = attempt(2, cwd, cmd, f, hold, start_hold, interval)
    if not stopped2:
        f.write('### RETRY HELD the hold: exit %s, low %d MB (the first attempt stopped at a low of %d MB)\n' % (rc2, low2, low))
        return rc2
    lo = min(low, low2)
    f.write('### RUN-BENEATH-HOLD module %s low %d MB hold %d %s -- the module unbuilt, the omission named in the closing\n' % (
        module or '?', lo, hold, utc()))
    f.write('### EXIT %d %s RUN-BENEATH-HOLD\n' % (RBH, utc()))
    if bank:
        try:
            j = json.load(open(bank, encoding='utf-8'))
        except Exception:
            j = dict(rows=[])
        j['rows'].append(dict(module=module, low=lo, lows=[low, low2], hold=hold, at=utc(), log=log.replace('\\', '/'), cmd=cmd, cwd=cwd))
        open(bank + '.tmp', 'w', encoding='utf-8', newline='\n').write(json.dumps(j, indent=1, ensure_ascii=False) + '\n')
        os.replace(bank + '.tmp', bank)
    return RBH


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
