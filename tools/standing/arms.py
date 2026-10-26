# -*- coding: utf-8 -*-
"""standing/arms.py -- AN ARM READS THE PREVIOUS ACT'S ROOT-NAMED BANKS (the class repair (4)(i) of the toolset act).

The previous act's pre-run figures are read from its committed part banks (data/<prev>_arms_prerun_<part>.txt), each read against the
sha256 its act's root names; a part bank the root does not name, or whose bytes differ from the root's sha256, is refused and counted
apart, never read. Provenance: tools/rule_arms.py :305-:307 (prev_longest from the previous act's combined pre-run bank, which an act
may never write -- the withheld arm of the act before the toolset act) and the arm G-RULE-LONG-PHASE-SPLIT (:534-:538), whose figures
these feed.

  prev_longest(prev, parts) -> dict(longest, parts_read, rows, refused)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

LONGEST = re.compile(r'THE LONGEST PHASE (\d+) s')


def prev_longest(prev, parts, base='arms_prerun', named=None, read=None):
    """the previous act's longest pre-run phase over its root-named part banks. `named` ({relay path: sha256}) and `read` (path -> bytes or
    None) default to the previous act's root and the working tree; a constructed control passes its own."""
    named = A.root_named(prev) if named is None else named

    def _read(rel):
        p = os.path.join(A.RELAY, *rel.split('/'))
        if not os.path.isfile(p):
            return None
        with open(p, 'rb') as f:
            return f.read()
    read = read or _read
    rows, refused, longest, got = [], [], 0, set()
    for p in parts:
        rel = 'data/%s_%s_%s.txt' % (prev, base, p)
        b = read(rel)
        want = named.get(rel)
        have = A.sha256_bytes(b) if b is not None else None
        if want is None:
            refused.append((rel, 'not named by the root'))
        elif have is None:
            refused.append((rel, 'absent'))
        elif have != want:
            refused.append((rel, 'sha256 %s differs from the root`s %s' % (have[:16], want[:16])))
        else:
            phases = [int(x) for x in LONGEST.findall(b.decode('utf-8', 'replace'))]
            got.add(p)
            longest = max([longest] + phases)
        rows.append((rel, (want or '-')[:16], (have or '-')[:16], want is not None and have == want))
    return dict(longest=longest, parts_read=len(got), rows=rows, refused=refused)
