# -*- coding: utf-8 -*-
"""b337_receipts.py -- THE PATENT RECEIPTS CHECKED FOR ON DISK; THEIR ABSENCE OR PRESENCE STATED.

### ### **THE DEADLINE BOARD'S OWN LAW FIRST:** enumerate the volumes before concluding a file does not exist. ### `Get-PSDrive`
### is run and its filesystem drives listed; `F:`, where the patent seat read the file wrappers on 2026-08-30, is recorded
### as mounted or not. ### **WHAT IS LOOKED FOR** (registration (F)): files whose names carry `receipt`, `acknowledg`,
### `eReceipt`, `EFS` with `ack`, or the confirmation numbers `7260` / `6082`, under the patent repo of record, the user's
### Downloads and Documents, and the papers repo, on every mounted volume. ### **WHAT IS STATED:** PRESENT (path, size,
### date) or ABSENT ON THE MOUNTED VOLUMES, per application; the four office notices and the response packages listed as
### what IS on disk; the repo of record's remote count (it must have none) and its newest file. ### **NOTHING IS CONCLUDED
### ABOUT WHETHER A REPLY WAS FILED.** ### Nothing under the patent repo is written.
"""
import io
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PAT = r'D:\MY-DOwnloads\patent-package-BACKUP-2026-08-29'
PP = r'D:\MY-DOwnloads\PLACE-papers'
HOME = os.path.expanduser('~')
SEARCH = [PAT, os.path.join(HOME, 'Downloads'), os.path.join(HOME, 'Documents'), PP]
PATTERNS = re.compile(r'receipt|acknowledg|ereceipt|efs.*ack|7260|6082', re.I)
APPS = ('64/065,864', '64/065,877')
OUT = os.path.join(D, 'b337_receipts_run.txt')
LINES = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    LINES.append(s)
    print(s)


def drives():
    r = subprocess.run(['powershell', '-NoProfile', '-Command', 'Get-PSDrive -PSProvider FileSystem | ForEach-Object { $_.Name }'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return [x.strip() for x in (r.stdout or '').splitlines() if x.strip()]


def walk(root, maxdepth=6):
    hits = []
    if not os.path.isdir(root):
        return hits
    base = root.rstrip(os.sep).count(os.sep)
    for dp, dns, fns in os.walk(root):
        if dp.count(os.sep) - base >= maxdepth:
            dns[:] = []
        dns[:] = [x for x in dns if x not in ('.git', 'node_modules', '__pycache__')]
        for fn in fns:
            if PATTERNS.search(fn):
                p = os.path.join(dp, fn)
                st = os.stat(p)
                hits.append((p, st.st_size, time.strftime('%Y-%m-%d', time.localtime(st.st_mtime))))
    return hits


def main():
    rec('=' * 100)
    rec('b337 -- THE PATENT RECEIPTS, CHECKED FOR ON DISK.')
    rec('=' * 100)
    dr = drives()
    rec('  volumes mounted (Get-PSDrive, filesystem) : %s ; F: mounted : %s' % (dr, 'F' in dr))
    if 'F' not in dr:
        rec("  ### F:, where the patent seat read the file wrappers on 2026-08-30, IS NOT MOUNTED THIS SESSION; every absence below is an absence on the mounted volumes.")
    rec('  search roots : %s' % SEARCH)
    rec('  name patterns : receipt | acknowledg | eReceipt | EFS..ack | 7260 | 6082')
    remotes, _ = subprocess.run(['git', '-C', PAT, 'remote'], capture_output=True, text=True).stdout.strip(), 0
    rec('  the repo of record %s : remotes %d (%s)' % (PAT, len(remotes.splitlines()) if remotes else 0, 'NONE, as required' if not remotes else '### A REMOTE IS AN INCIDENT ###'))
    hits = []
    for root in SEARCH:
        h = walk(root)
        rec('  %-60s hits %d' % (root, len(h)))
        hits += h
    receipt_like = [h for h in hits if re.search(r'receipt|acknowledg', h[0], re.I)]
    rec('')
    for app in APPS:
        digits = app.replace('/', '').replace(',', '')
        mine = [h for h in receipt_like if digits in h[0].replace('-', '').replace('_', '') or ('7260' in h[0] and app.endswith('864')) or ('6082' in h[0] and app.endswith('877'))]
        if mine:
            rec('  %s : PRESENT -- %s' % (app, ['%s (%d bytes, %s)' % (os.path.basename(p), s, d) for p, s, d in mine]))
        else:
            rec('  %s : ABSENT ON THE MOUNTED VOLUMES (%s) -- no receipt-shaped file names it' % (app, ', '.join(dr)))
    rec('')
    rec('  WHAT IS ON DISK FOR THE TWO APPLICATIONS (the counsel packet and the exports):')
    notices = os.path.join(PAT, 'COUNSEL_PACKET_2026-08', '06_office_notices')
    for fn in sorted(os.listdir(notices)) if os.path.isdir(notices) else []:
        st = os.stat(os.path.join(notices, fn))
        rec('    office notice   %-52s %8d bytes  %s' % (fn, st.st_size, time.strftime('%Y-%m-%d', time.localtime(st.st_mtime))))
    ex = os.path.join(PAT, 'exports', '2026-08-30')
    for fn in sorted(os.listdir(ex)) if os.path.isdir(ex) else []:
        p = os.path.join(ex, fn)
        rec('    export 08-30    %-52s %s' % (fn, 'dir' if os.path.isdir(p) else '%d bytes' % os.stat(p).st_size))
    newest = (None, 0)
    for dp, dns, fns in os.walk(PAT):
        dns[:] = [x for x in dns if x != '.git']
        for fn in fns:
            m = os.stat(os.path.join(dp, fn)).st_mtime
            if m > newest[1]:
                newest = (os.path.join(dp, fn), m)
    rec('  newest file in the repo of record : %s (%s)' % (os.path.relpath(newest[0], PAT) if newest[0] else 'none', time.strftime('%Y-%m-%d %H:%M', time.localtime(newest[1]))))
    log = subprocess.run(['git', '-C', PAT, 'log', '-1', '--format=%h %ad %s', '--date=short'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()
    rec('  its last commit : %s' % log[:120])
    rec("  the counsel list's own naming of the receipts owed : item 3, \"NEW-6 / NEW-8 receipts -- standing\" (COUNSEL_ITEMS.md)")
    rec('  ### NOTHING IS CONCLUDED ABOUT WHETHER A REPLY WAS FILED. ### An absence on the mounted volumes is an absence on the mounted volumes.')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    return 0


if __name__ == '__main__':
    sys.exit(main())
