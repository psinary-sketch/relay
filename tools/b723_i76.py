# -*- coding: utf-8 -*-
"""b723_i76.py -- (R333)'s addendum (c) and the author's word (3): I-76's DIFFERS READ AT b723. Written whole at b723 by the Write tool.

  run [--bank]   tools/research/reproduce.py's I-76 call (`M.classify(M.enumerate_all())`, tools/b544_probe_part.py, unedited) re-run at
                 b544's pins: the repositories b542_record.REPOS cites by a pin read at that pin, as b544 read them; the eleven it cites by
                 none (read at HEAD) read at the commit their HEAD stood on when b544 banked its count -- the last first-parent commit at or
                 before data/b544_decls.json's own commit time (deb2a187, 2026-09-26T05:45:59Z). REPOS is rebound in memory for the call and
                 restored; no repository is checked out or written. Printed beside each other: the bank's figure (data/b544_decls.json :1,
                 "count"), today's (the call over today's trees, as data/b722_reproduce.txt :143-:146 ran it) and the pinned call's; per
                 repository the bank's rows, today's and the pinned call's. THE NAVIGATOR'S READING, THE INPUTS CLASS, IS CONFIRMED when the
                 pinned call reproduces the bank's figure and every repository's rows, REFUTED otherwise. A CONTROL FIRST: the pinned call
                 with one HEAD repository's pin set back to HEAD moves that repository's rows to today's, as wanted. TECHNE-Core's names
                 never leave memory; its rows are counted, as b544's bank counts them. --bank writes data/b723_i76.txt and .json.
"""
import io
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b542_record as Q          # noqa: E402
import b544_probe_part as M      # noqa: E402

BANK_COMMIT = 'deb2a187'          # ### data/b544_decls.json's commit, b544's


def git(repo, *a):
    return Q.g(repo, *a).strip()   # ### b542's own reader, its paths by Q.rpath


def bank_time():
    return subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%cI', BANK_COMMIT], capture_output=True, text=True).stdout.strip()


def free_mb():
    import ctypes

    class MS(ctypes.Structure):
        _fields_ = [('l', ctypes.c_ulong), ('m', ctypes.c_ulong), ('tp', ctypes.c_ulonglong), ('ap', ctypes.c_ulonglong), ('tf', ctypes.c_ulonglong),
                    ('af', ctypes.c_ulonglong), ('tv', ctypes.c_ulonglong), ('av', ctypes.c_ulonglong), ('ae', ctypes.c_ulonglong)]
    m = MS()
    m.l = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ap // 2 ** 20


def per_repo(ds):
    out = {}
    for x in ds:
        out[x['repo']] = out.get(x['repo'], 0) + 1
    return out


def call(repos):
    """the I-76 call with b542_record.REPOS rebound for its duration: (count, rows per repo, seconds)."""
    keep = Q.REPOS
    t0 = time.time()
    try:
        Q.REPOS = repos
        ds, _fed = M.classify(M.enumerate_all())
    finally:
        Q.REPOS = keep
    return len(ds), per_repo(ds), round(time.time() - t0, 1)


def run(*a):
    fm = free_mb()
    if fm < 2560:
        sys.exit('### FREE %d MB, UNDER THE 2560 MB HOLD -- NOTHING RUN' % fm)
    bt = bank_time()
    bj = json.load(io.open(os.path.join(D, 'b544_decls.json'), encoding='utf-8'))
    bank_count, bank_per = bj['count'], dict((r, sum(v.values())) for r, v in (bj.get('per_repo') or {}).items())
    heads, pinned = {}, []
    for r, cited, x in Q.REPOS:
        if cited:
            pinned.append((r, cited, x))
            continue
        h = git(r, 'rev-list', '-1', '--first-parent', '--before=%s' % bt, 'HEAD')
        if not h:
            sys.exit('### %s: NO COMMIT AT OR BEFORE %s -- NOTHING RUN' % ('TECHNE-Core' if r == Q.PRIV else r, bt))
        heads[r] = (h, git(r, 'rev-parse', 'HEAD'))
        pinned.append((r, h, x))
    head_repos = [r for r, c, _x in Q.REPOS if not c]
    L = ['b723 -- I-76 READ AT b723 ((R333)`s addendum (c), the author`s word (3)): b544_probe_part AT b544`S PINS (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
         '', '### THE CALL: tools/research/reproduce.py`s I-76 row, `M.classify(M.enumerate_all())` (tools/b544_probe_part.py, unedited), its',
         '### REPOS (tools/b542_record.py) rebound in memory: the %d repositories cited by a pin read at it; the %d cited by none read at the commit' % (
             len(Q.REPOS) - len(head_repos), len(head_repos)),
         '### their HEAD stood on at %s (data/b544_decls.json`s commit %s), the last first-parent commit at or before it. Free %d MB before.' % (bt, BANK_COMMIT, fm),
         '### THE RULE, PRINTED BEFORE THE FIGURES: the inputs class CONFIRMED when the pinned call reproduces the bank`s count and every',
         '### repository`s rows; REFUTED otherwise.', '', '## THE HEAD REPOSITORIES` PINS (b544`s commit ; HEAD now ; moved)']
    for r in head_repos:
        h, now = heads[r]
        if r == Q.PRIV:   # ### the private repository's commits are not printed: its state alone
            L.append('  %-34s %s ; %s ; %s' % ('TECHNE-Core (private)', 'withheld', 'withheld', 'MOVED' if h != now else 'UNMOVED'))
        else:
            L.append('  %-34s %s ; %s ; %s' % (r, h[:10], now[:10], 'MOVED' if h != now else 'UNMOVED'))
    n_pin, per_pin, s_pin = call(pinned)
    n_now, per_now, s_now = call(list(Q.REPOS))
    moved = [r for r in head_repos if heads[r][0] != heads[r][1] and per_pin.get(r) != per_now.get(r)]
    cr = moved[0] if moved else None
    ctl = None
    if cr:
        ctl_repos = [(r, (None if r == cr else c), x) for r, c, x in pinned]
        n_c, per_c, s_c = call(ctl_repos)
        ctl = dict(repo='TECHNE-Core' if cr == Q.PRIV else cr, rows_pinned=per_pin.get(cr), rows_now=per_now.get(cr), rows_control=per_c.get(cr),
                   as_wanted=per_c.get(cr) == per_now.get(cr) and per_c.get(cr) != per_pin.get(cr), seconds=s_c)
    L += ['', '## THE CONTROL FIRST: the pinned call with one moved HEAD repository set back to HEAD']
    L.append('  %s' % ('%s: pinned %s rows, today %s, the control %s -- %s' % (ctl['repo'], ctl['rows_pinned'], ctl['rows_now'], ctl['rows_control'],
                                                                                'AS WANTED' if ctl['as_wanted'] else 'NOT AS WANTED') if ctl else
                       'NONE RUN: no HEAD repository moved its rows (the control has no subject)'))
    L += ['', '## THE FIGURES (the bank ; today ; the pinned call)',
          '  the count                          %5d ; %5d ; %5d   (%.1f s today, %.1f s pinned)' % (bank_count, n_now, n_pin, s_now, s_pin), '',
          '## BY REPOSITORY (the bank ; today ; the pinned call ; the pinned call equal to the bank)']
    neq = []
    for r, c, _x in Q.REPOS:
        b, t, p = bank_per.get(r, 0), per_now.get(r, 0), per_pin.get(r, 0)
        if p != b:
            neq.append(r)
        L.append('  %-34s %5d ; %5d ; %5d ; %s' % ('TECHNE-Core (private)' if r == Q.PRIV else r, b, t, p, 'EQUAL' if p == b else 'DIFFERS'))
    verdict = 'CONFIRMED' if n_pin == bank_count and not neq else 'REFUTED'
    L += ['', '### ### **I-76 AT b544`S PINS: THE BANK %d ; TODAY %d ; THE PINNED CALL %d ; REPOSITORIES EQUAL %d OF %d ; THE CONTROL %s ; THE INPUTS CLASS %s.**' % (
        bank_count, n_now, n_pin, len(Q.REPOS) - len(neq), len(Q.REPOS), ('AS WANTED' if ctl and ctl['as_wanted'] else 'NOT AS WANTED' if ctl else 'NONE'), verdict)]
    text = NL.join(L)
    print(text)
    if '--bank' in a:
        for name, body in (('b723_i76.txt', text + NL), ('b723_i76.json', json.dumps(dict(
                at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), bank_time=bt, bank=bank_count, today=n_now, pinned_call=n_pin,
                head_pins=dict((r, heads[r][0]) for r in head_repos if r != Q.PRIV),
                per_repo=[dict(repo='TECHNE-Core' if r == Q.PRIV else r, bank=bank_per.get(r, 0), today=per_now.get(r, 0), pinned=per_pin.get(r, 0)) for r, _c, _x in Q.REPOS],
                control=ctl, verdict=verdict), indent=1) + NL)):
            p = os.path.join(D, name)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(body.encode('utf-8'))
            os.replace(p + '.tmp', p)
            print('written data/' + name)


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'run':
        sys.exit('usage: b723_i76.py run [--bank]')
    run(*sys.argv[2:])
