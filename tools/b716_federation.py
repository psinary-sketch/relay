# -*- coding: utf-8 -*-
"""b716_federation.py -- (R326)(6)(i): THE FEDERATION PIN, PRICED, NOTHING BUILT. Writes data/b716_federation_pin_price.txt.

For every PUBLIC kernel data/b715_pins_census.txt lists (its `--- <repo> (<path>) visibility PUBLIC` rows, the SIDE-* ones): its Mathlib
rev (lake-manifest.json `packages`, name mathlib, `rev`) and its toolchain (lean-toolchain), read from the kernel's own checkout at its HEAD
(the census reads HEAD equal to ls-remote for every one); the revs grouped. Each Mathlib rev's commit date and its own lean-toolchain read
from GitHub's public endpoints WITHOUT AUTHENTICATION (api.github.com commits, raw.githubusercontent.com), a generic User-Agent, no
identifier of the author in any header, URL or payload. The target: the newest rev any kernel carries. For each kernel below it: the
modules a bump would reach (its .lean files importing Mathlib, read from its tree at HEAD) and its own past runs (the public Actions runs
listing, unauthenticated: workflow, conclusion, start and end), the hours priced from them. No dispatch is made; no lean process runs.

  python -X utf8 tools/b716_federation.py          writes the bank and prints its foot
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RELAY, 'data')
NL = '\n'
UA = {'User-Agent': 'relay-price-reader', 'Accept': 'application/vnd.github+json'}
ROW = re.compile(r'^--- (SIDE-[\w-]+)\s+\(([^)]+)\)\s+visibility PUBLIC', re.M)
OWNER = 'psinary-sketch'
MATHLIB = 'leanprover-community/mathlib4'


def git(path, *args):
    r = subprocess.run(['git', '-C', path] + list(args), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return r.read().decode('utf-8', 'replace'), None
    except Exception as e:   # the failure is banked with its URL, never substituted
        return None, '%s: %s' % (type(e).__name__, e)


def iso(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ') if s else None


def main():
    census = open(os.path.join(D, 'b715_pins_census.txt'), encoding='utf-8').read()
    ks = ROW.findall(census)
    rows, calls, fails = [], 0, []
    for name, path in ks:
        head = (git(path, 'rev-parse', 'HEAD') or '').strip()
        man = git(path, 'show', 'HEAD:lake-manifest.json')
        tc = (git(path, 'show', 'HEAD:lean-toolchain') or '').strip() or None
        rev = None
        if man:
            try:
                for p in json.loads(man).get('packages') or []:
                    if p.get('name') == 'mathlib':
                        rev = p.get('rev')
            except ValueError:
                pass
        mods = []
        if rev:
            for f in (git(path, 'ls-tree', '-r', '--name-only', 'HEAD') or '').split(NL):
                if f.endswith('.lean') and not f.startswith('.lake/'):
                    src = git(path, 'show', 'HEAD:' + f) or ''
                    if re.search(r'^\s*import\s+Mathlib', src, re.M):
                        mods.append(f)
        rows.append(dict(name=name, path=path, head=head, rev=rev, toolchain=tc, mods=mods))
    revs = sorted(set(r['rev'] for r in rows if r['rev']))
    info = {}
    for rv in revs:
        t, e = get('https://api.github.com/repos/%s/commits/%s' % (MATHLIB, rv))
        calls += 1
        date = None
        if t:
            try:
                date = json.loads(t)['commit']['committer']['date']
            except (ValueError, KeyError, TypeError):
                pass
        else:
            fails.append(('commits ' + rv[:8], e))
        tt, e2 = get('https://raw.githubusercontent.com/%s/%s/lean-toolchain' % (MATHLIB, rv))
        calls += 1
        if tt is None:
            fails.append(('toolchain ' + rv[:8], e2))
        info[rv] = dict(date=date, toolchain=(tt or '').strip() or None)
    dated = [rv for rv in revs if info[rv]['date']]
    target = max(dated, key=lambda rv: info[rv]['date']) if dated else None
    below = [r for r in rows if r['rev'] and target and r['rev'] != target]
    runs = {}
    for r in below + [x for x in rows if x['rev'] == target]:
        t, e = get('https://api.github.com/repos/%s/%s/actions/runs?per_page=20' % (OWNER, r['name']))
        calls += 1
        rs = []
        if t:
            try:
                for x in json.loads(t).get('workflow_runs') or []:
                    a, b = iso(x.get('run_started_at')), iso(x.get('updated_at'))
                    rs.append(dict(id=x.get('id'), wf=x.get('name'), sha=(x.get('head_sha') or '')[:8], concl=x.get('conclusion'),
                                   start=x.get('run_started_at'), minutes=round((b - a).total_seconds() / 60, 1) if a and b else None))
            except ValueError:
                pass
        else:
            fails.append(('runs ' + r['name'], e))
        runs[r['name']] = rs
    L = ['b716 -- (R326)(6)(i): THE FEDERATION PIN, PRICED; NOTHING BUILT, NO DISPATCH (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows: every PUBLIC kernel of data/b715_pins_census.txt (%d), its Mathlib rev and toolchain read from its own checkout at HEAD; the' % len(rows),
         '### revs grouped, each rev`s date and toolchain from GitHub`s public endpoints, unauthenticated (%d requests, %d failed, each failure' % (calls, len(fails)),
         '### banked); the target the newest rev any kernel carries; for each kernel below it, the modules a bump reaches and its own past runs.',
         '### Written by tools/b716_federation.py.', '']
    L.append('## (1) THE KERNELS, EACH WITH ITS MATHLIB REV AND TOOLCHAIN')
    for r in rows:
        L.append('  %-34s HEAD %s | mathlib %s | toolchain %s | modules importing Mathlib %s' % (
            r['name'], r['head'][:8], (r['rev'] or 'NONE (no Mathlib in its manifest)')[:12] if r['rev'] else 'NONE (no Mathlib in its manifest)',
            r['toolchain'] or '-', len(r['mods']) if r['rev'] else '-'))
    L += ['', '## (2) THE REVS GROUPED']
    for rv in sorted(revs, key=lambda x: info[x]['date'] or ''):
        L.append('  mathlib %s | committed %s | its toolchain %s | kernels %d: %s' % (
            rv[:12], info[rv]['date'] or '### NOT READ', info[rv]['toolchain'] or '### NOT READ',
            sum(1 for r in rows if r['rev'] == rv), ' '.join(r['name'] for r in rows if r['rev'] == rv)))
    L += ['  THE TARGET, the newest rev any kernel carries: %s (%s), toolchain %s' % (
        (target or '### NOT READ')[:12], info.get(target, {}).get('date') if target else '-', info.get(target, {}).get('toolchain') if target else '-'), '']
    L.append('## (3) EACH KERNEL BELOW THE TARGET: THE MODULES A BUMP REACHES, ITS OWN RUNS, THE HOURS')
    tot_min, n_disp, unpriced = 0.0, 0, []
    for r in below:
        rs = runs.get(r['name']) or []
        ok = [x for x in rs if x['concl'] == 'success' and x['minutes'] is not None]
        mx = max((x['minutes'] for x in ok), default=None)
        L.append('  %s at mathlib %s (%s), toolchain %s -> the target %s' % (r['name'], r['rev'][:12], info[r['rev']]['date'] or '?', r['toolchain'],
                                                                    (target or '')[:12]))
        L.append('    modules importing Mathlib %d: %s' % (len(r['mods']), ', '.join(r['mods'][:40]) + (' ...' if len(r['mods']) > 40 else '')))
        L.append('    its own runs (the public listing, newest 20): %d ; successful %d ; the longest successful %s min' % (len(rs), len(ok), mx))
        for x in rs[:6]:
            L.append('      run %s %-14s %s at %s, %s, %s min' % (x['id'], x['wf'], x['concl'], x['sha'], x['start'], x['minutes']))
        n_disp += 1
        tot_min += (mx or 0)
        if mx is None:
            unpriced.append(r['name'])
    L += ['', '## (3b) THE POSITIVE CONTROL: THE KERNEL(S) ALREADY AT THE TARGET, THEIR OWN RUNS']
    for r in [x for x in rows if x['rev'] == target]:
        rs = runs.get(r['name']) or []
        ok = [x for x in rs if x['concl'] == 'success' and x['minutes'] is not None]
        L.append('  %s at mathlib %s, toolchain %s ; its own runs (newest 20): %d ; successful %d ; the longest successful %s min' % (
            r['name'], r['rev'][:12], r['toolchain'], len(rs), len(ok), max((x['minutes'] for x in ok), default=None)))
        for x in rs[:6]:
            L.append('      run %s %-14s %s at %s, %s, %s min' % (x['id'], x['wf'], x['concl'], x['sha'], x['start'], x['minutes']))
    L += ['', '## (4) THE MODULES A BUMP WOULD BREAK: NOT READ -- A HALT, EVERY ROUTE NAMED',
          '  (a) the kernel`s own build logs at the target rev: none exists -- a kernel below the target has never built at it (its runs in (3)',
          '      build its own manifest`s rev); (b) a dry build on the runner: the kernels` build-module.yml builds `inputs.ref` with the manifest',
          '      that ref carries (tools read: D:/SIDE-kernel/.github/workflows/build-module.yml :29-:32 checkout at the ref, :49-:50 `lake exe',
          '      cache get` for that manifest), so a dry build at the target needs a ref whose lake-manifest.json pins the target -- a bump branch',
          '      pushed to each kernel, a write outside (R326)(8)`s (W) list. THE POSITIVE CONTROL: the same workflow at a kernel already at the',
          '      target builds as its runs in (3b) show. The set a bump REACHES is printed per kernel in (3) (its modules importing Mathlib); which',
          '      of them BREAK is the dry builds` first figure, one dispatch per kernel on its bump branch, read by run id with its artifact`s',
          '      sha256, in the act the author rules for the pin.', '',
          '## (5) THE PRICE (THE SEAT`S, FROM (3)): dispatches %d (one per kernel below the target, each its bump branch first); runner time' % n_disp,
          '  at each kernel`s longest successful run, %.0f min in all (%.1f h), the runs sequential on the runner; a kernel with no successful' % (tot_min, tot_min / 60),
          '  run read enters at 0 min and is named here, UNPRICED: %s; the bump branches,' % (', '.join(unpriced) or 'none'),
          '  the manifests` edits and the repairs where a module breaks priced at the act that reads the breakage. Foreground for this act: the',
          '  branches and dispatches 1.0 h, the reads 0.5 h -- about %.1f h with the runner time, inside one act where no module breaks;' % (1.5 + tot_min / 60),
          '  each breaking module adds its own repair, unpriced until read.']
    if fails:
        L += ['', '## THE REQUESTS THAT FAILED (banked, not substituted)'] + ['  %s : %s' % f for f in fails]
    L += ['', '### ### **PUBLIC KERNELS %d ; WITH MATHLIB %d ; REVS %d ; THE TARGET %s ; BELOW IT %d ; DISPATCHES PRICED %d, %.1f RUNNER HOURS ;'
          ' THE MODULES A BUMP WOULD BREAK NOT READ (A HALT: NO REF CARRIES THE BUMP) ; REQUESTS %d, FAILED %d ; NOTHING BUILT.**' % (
              len(rows), sum(1 for r in rows if r['rev']), len(revs), (target or 'NOT READ')[:12], len(below), n_disp, tot_min / 60, calls, len(fails))]
    p = os.path.join(D, 'b716_federation_pin_price.txt')
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(p + '.tmp', p)
    print('bank', p)
    print(L[-1])
    return 0


if __name__ == '__main__':
    sys.exit(main())
