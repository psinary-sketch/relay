# -*- coding: utf-8 -*-
"""b722_address_scan.py -- (R332)(9)(i): NO NEW OCCURRENCE OF THE AUTHOR'S NAME OR E-MAIL ADDRESS. Written whole at b722 by the Write tool.

  scan [--bank]   the previous address read from history -- the author and committer e-mails of relay's commits up to the act's base, less
                  the GitHub noreply form, which must leave exactly one address -- and the author's name read from the monograph's byline
                  (tools/b722_llm_line.py monograph(), at run time); both held in memory, neither printed. Counted, as NEW occurrences:
                  every commit of relay and PLACE-papers from the act's base to HEAD (author and committer names and e-mails, the message,
                  the lines the commit adds), the working trees' added lines not yet committed, and every untracked bank of the act under
                  relay data/ (its whole text). Occurrences already in the history stay as the record and are not read. Printed:
                  "PREVIOUS ADDRESS: <count>" and "THE AUTHOR'S NAME: <count>", each alone, with the places counted by kind -- never the
                  address or the name. THE CONTROLS FIRST: a planted line carrying each, counted 1 each, and a clean line counted 0.
                  --bank writes data/b722_address_scan.txt.
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b722_worklist as K   # noqa: E402

ACT = 'b722'
PP = K.PP
NOREPLY = 'users.noreply.github.com'


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def previous_address():
    """the one address of relay's history up to the act's base that is not the noreply form; anything else refuses."""
    seen = set(x.strip().lower() for x in git(ROOT, 'log', '--format=%ae%n%ce', K.PRE_RELAY).split(NL) if x.strip())
    old = sorted(x for x in seen if not x.endswith(NOREPLY) and '@' in x)
    if len(old) != 1:
        sys.exit('### THE HISTORY CARRIES %d ADDRESSES OTHER THAN THE NOREPLY FORM, NOT ONE -- NOTHING READ' % len(old))
    return old[0]


def author_name():
    import b722_llm_line as LL
    n = (LL.monograph()[5] or '').strip()
    if len(n) < 4:
        sys.exit('### THE BYLINE NOT READ -- NOTHING READ')
    return n


def count(text, needle):
    return text.lower().count(needle.lower())


def added(diff):
    return NL.join(l[1:] for l in diff.split(NL) if l.startswith('+') and not l.startswith('+++'))


def places():
    """(kind, label, text): the new text the act wrote, by place."""
    out = []
    for repo, name, pre in ((ROOT, 'relay', K.PRE_RELAY), (PP, 'PLACE-papers', K.PRE_PP)):
        for h in [x for x in git(repo, 'rev-list', '--reverse', '%s..HEAD' % pre).split(NL) if x.strip()]:
            out.append(('commit fields', '%s %s' % (name, h[:8]), git(repo, 'log', '-1', '--format=%an%n%ae%n%cn%n%ce', h)))
            out.append(('commit message', '%s %s' % (name, h[:8]), git(repo, 'log', '-1', '--format=%B', h)))
            out.append(('commit added lines', '%s %s' % (name, h[:8]), added(git(repo, 'show', '--format=', '--no-color', '--no-ext-diff', h))))
        out.append(('working tree added lines', name, added(git(repo, 'diff', '--no-color', '--no-ext-diff', 'HEAD'))))
    tracked = set(git(ROOT, 'ls-files', '--', 'data/').split(NL))
    for f in sorted(os.listdir(D)):
        p = 'data/' + f
        if f.startswith(ACT + '_') and os.path.isfile(os.path.join(D, f)) and p not in tracked and not f.endswith(('.gz', '.png')):
            out.append(('untracked bank', p, open(os.path.join(D, f), encoding='utf-8', errors='replace').read()))
    return out


def scan(*a):
    t0 = time.time()
    addr, name = previous_address(), author_name()
    ctl = [('a planted line carrying the address', count('x %s y' % addr, addr) == 1 and count('x %s y' % addr, name) == 0),
           ('a planted line carrying the name', count('x %s y' % name, name) == 1 and count('x %s y' % name, addr) == 0),
           ('a clean line', count('the noreply form ' + NOREPLY, addr) == 0 and count('the noreply form ' + NOREPLY, name) == 0)]
    L = ['%s -- (R332)(9)(i): NO NEW OCCURRENCE OF THE AUTHOR`S NAME OR E-MAIL ADDRESS (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '', '### the previous address read from relay`s history to %s (author and committer e-mails less the noreply form: one address), the' % K.PRE_RELAY[:8],
         '### name from the monograph`s byline at run time; both held in memory, neither printed. New text only: the commits from relay %s and' % K.PRE_RELAY[:8],
         '### PLACE-papers %s to HEAD (fields, messages, added lines), the uncommitted added lines, the untracked banks of %s.' % (K.PRE_PP[:8], ACT), '',
         '## THE CONTROLS FIRST']
    L += ['  %-40s %s' % (w, 'AS WANTED' if ok else 'NOT AS WANTED') for w, ok in ctl]
    if not all(ok for _w, ok in ctl):
        print(NL.join(L))
        sys.exit('### A CONTROL NOT AS WANTED -- NOTHING COUNTED')
    P = places()
    by = {}
    na = nn = 0
    for kind, label, text in P:
        x, y = count(text, addr), count(text, name)
        na, nn = na + x, nn + y
        k = by.setdefault(kind, [0, 0, 0])
        k[0] += 1
        k[1] += x
        k[2] += y
    L += ['', '## THE PLACES READ, BY KIND (places ; address ; name)']
    L += ['  %-28s %4d ; %d ; %d' % (k, v[0], v[1], v[2]) for k, v in sorted(by.items())]
    hits = sorted(set('%s %s' % (kind, label) for kind, label, text in P if count(text, addr) or count(text, name)))
    L += ['', '## THE PLACES WITH AN OCCURRENCE (by place, never the text): %s' % ('; '.join(hits) if hits else 'NONE')]
    L += ['', 'PREVIOUS ADDRESS: %d' % na, 'THE AUTHOR`S NAME: %d' % nn, '',
          '### ### **PREVIOUS ADDRESS: %d ; THE AUTHOR`S NAME: %d ; PLACES %d ; CONTROLS 3 OF 3 AS WANTED ; %d s.**' % (na, nn, len(P), int(time.time() - t0))]
    text = NL.join(L)
    if addr in text.lower() or name.lower() in text.lower():
        sys.exit('### THE BANK WOULD CARRY THE ADDRESS OR THE NAME -- NOTHING PRINTED OR WRITTEN')
    print(text)
    if '--bank' in a:
        p = os.path.join(D, '%s_address_scan.txt' % ACT)
        with open(p + '.tmp', 'wb') as fh:
            fh.write((text + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_address_scan.txt' % ACT)
    return na, nn


if __name__ == '__main__':
    fn = dict(scan=scan).get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit('usage: b722_address_scan.py scan [--bank]')
    fn(*sys.argv[2:])
