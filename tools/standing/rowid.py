# -*- coding: utf-8 -*-
"""standing/rowid.py -- v1.25.0, (R355)(2)(i), b743's [B1]-[B3] (the collision the author's amendment repaired at b744): THE ROW'S ID. b743's sitting
gave its three Epstein rows the IDs 1.5c-16, -17, -18, allocated from the table the rows joined, where REGISTRY already held all three in other tables
(:482, :522, :1091; the file's highest 1.5c-20). A ledger row's ID is now allocated from the file's maximum over every table that carries the prefix,
and a row whose ID the file already holds is refused before the commit: tools/standing/hook.py calls refusals() on every PLACE-papers commit command
(kind ROWID), reading the staged form of each ledger file against HEAD's. A row is a markdown table line whose first cell is an ID
(<prefix>-<n>[letter]); the file's rows that already share an ID stand as found (REGISTRY carries 17 such at b745's step zero, printed by `dups`, not
this act's to repair); the rule binds the rows a commit adds.

  python -X utf8 -u tools/standing/rowid.py next <file> <prefix>          the next ID from the file's maximum over every table
  python -X utf8 -u tools/standing/rowid.py check <base-file> <new-file>  the added rows' IDs against the base; exit 13 on a held ID
  python -X utf8 -u tools/standing/rowid.py dups <file>                   the IDs the file already holds more than once
"""
import collections
import io
import os
import re
import subprocess
import sys

ROW = re.compile(r'^\|\s*([A-Za-z0-9.]+)-(\d+)([A-Za-z]?)\s*\|')
LEDGERS = ('REGISTRY.md', 'ERRATA.md', 'phase1.5/method/INSTRUMENTS.md')   # ### the PLACE-papers files whose rows carry IDs
NL = '\n'


def rows(text):
    """[(line, id, prefix, n)] for every table line whose first cell is an ID."""
    out = []
    for i, l in enumerate((text or '').replace('\r', '').split(NL), 1):
        m = ROW.match(l)
        if m:
            out.append((i, '%s-%s%s' % (m.group(1), m.group(2), m.group(3)), m.group(1), int(m.group(2))))
    return out


def next_id(text, prefix):
    """the next ID for <prefix>: one past the file's maximum over EVERY table carrying the prefix, not the table the row joins."""
    ns = [n for _l, _i, p, n in rows(text) if p == prefix]
    return '%s-%d' % (prefix, (max(ns) if ns else 0) + 1)


RULE_355 = ('THE (R355) RULE BINDS THE LEDGERS ALONE: rows of REGISTRY.md, ERRATA.md and phase1.5/method/INSTRUMENTS.md take an ID one past the '
            'file`s maximum; an order is entered by its W-ORD name and takes no number (v1.27.0, (R357)(3)(iv))')


def ledger_of(path):
    """v1.27.0, (R357)(3)(iv), b746 events (3): the LEDGERS entry the path names, or None. A path is matched on its PLACE-papers-relative
    form (the separators normalised, the PLACE-papers root stripped where it stands)."""
    p = path.replace('\\', '/')
    for f in LEDGERS:
        if p == f or p.endswith('/' + f):
            return f
    return None


def next_refusal(path, prefix):
    """the refusal, by name, of `next` over a file outside LEDGERS -- printing no ID -- or None for a ledger."""
    if ledger_of(path):
        return None
    return ('### REFUSED: %s is not a ledger of the (R355) rule (LEDGERS: %s); no ID printed for prefix %s. %s' % (
        path, ', '.join(LEDGERS), prefix, RULE_355))


def added(base, new):
    """the rows of <new> not in <base> as lines (a moved line is not added): [(line, id, prefix, n)], by multiset of line text."""
    have = collections.Counter(l for l in (base or '').replace('\r', '').split(NL))
    out = []
    nl = (new or '').replace('\r', '').split(NL)
    for r in rows(new):
        t = nl[r[0] - 1]
        if have[t] > 0:
            have[t] -= 1
            continue
        out.append(r)
    return out


def refusals(base, new):
    """[(line, id, why)]: each added row whose ID the base file already holds (in any table), or that a second added row also takes."""
    held = collections.defaultdict(list)
    for l, i, _p, _n in rows(base):
        held[i].append(l)
    out, seen = [], {}
    for l, i, _p, _n in added(base, new):
        if held.get(i):
            out.append((l, i, 'the file already holds %s (base :%s)' % (i, ', :'.join(str(x) for x in held[i]))))
        elif i in seen:
            out.append((l, i, 'a second added row takes %s (:%d)' % (i, seen[i])))
        seen.setdefault(i, l)
    return out


def dups(text):
    c = collections.defaultdict(list)
    for l, i, _p, _n in rows(text):
        c[i].append(l)
    return {i: ls for i, ls in c.items() if len(ls) > 1}


def staged_refusals(repo):
    """for a PLACE-papers commit: each ledger file's staged form (the index) against HEAD's; [(file, line, id, why)]."""
    out = []
    for f in LEDGERS:
        st = subprocess.run(['git', '-C', repo, 'diff', '--cached', '--name-only', '--', f], capture_output=True, text=True).stdout.strip()
        if not st:
            continue
        g = lambda ref: subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (ref, f)], capture_output=True).stdout.decode('utf-8', 'replace')   # noqa: E731
        out += [(f,) + r for r in refusals(g('HEAD'), g(''))]
    return out


def _rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read()


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['next'] and len(a) == 3:
        ref = next_refusal(a[1], a[2])
        if ref:
            print(ref)
            sys.exit(14)
        print(next_id(_rd(a[1]), a[2]))
    elif a[:1] == ['check'] and len(a) == 3:
        r = refusals(_rd(a[1]), _rd(a[2]))
        for l, i, why in r:
            print('  REFUSED :%d %s -- %s' % (l, i, why))
        print('### ROWS ADDED %d ; REFUSED %d' % (len(added(_rd(a[1]), _rd(a[2]))), len(r)))
        sys.exit(13 if r else 0)
    elif a[:1] == ['dups'] and len(a) == 2:
        d = dups(_rd(a[1]))
        for i in sorted(d):
            print('  %s at :%s' % (i, ', :'.join(str(x) for x in d[i])))
        print('### IDS HELD MORE THAN ONCE %d' % len(d))
    else:
        print(__doc__)
        sys.exit(2)
