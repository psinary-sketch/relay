# -*- coding: utf-8 -*-
"""standing/readfirst.py -- v1.2.2 ((R332)(2)(iii)): THE READFIRST CLOSURE READER RETIRED; THE HAND LIST THE BANK OF RECORD.

b692's closure reader (tools/circuit_read.py readfirst) wrote data/<act>_readfirst_closure.txt and _diff.txt beside the hand list; b710's
reading 5 recommended the hand list stand alone, and (R332)(2)(iii) retires the closure from b722: data/<act>_readfirst_closure.txt is no
longer written. The arm's reading: the hand list present, unchanged since the commit that first carried it (its step-zero commit), and no
closure bank of the act's own. Nothing written; circuit_read.py stays where it is, its readfirst route no longer called by a close.

### v1.8.0, (R338)(2)(iv)(b): THE READFIRST BANK WRITTEN BY THE TOOL WITH ITS SECTION TITLES FIXED -- b727's hand bank wrote "ALSO READ, FOR THE
### ACT'S OWN NEEDS" where G-READFIRST-CITED reads OWN_TITLE, and the arm failed at every run (b727 event (5)). `compose` takes the rows and
### writes the two titles itself; `regenerate` reads a banked list's rows back, so the control replays b727's bank; the bank stays hand-rowed,
### its rows the act's, in data/<act>_readfirst_rows.json.
  python -X utf8 tools/standing/readfirst.py write <act>        data/<act>_readfirst_rows.json -> data/<act>_readfirst.txt; refused where it stands
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

RETIRED_FROM = 'b722'
FERRY_TITLE = "## THE FERRY'S READ-FIRST LIST"
OWN_TITLE = "## THE ACT'S OWN BEYOND THE LIST"
NL = '\n'


def compose(head, ferry, own, note=()):
    """the bank's text from its rows: the head lines, then the two sections under the fixed titles. Pure in its arguments; refuses an empty
    ferry list, the section the arm reads."""
    if not ferry:
        raise ValueError('readfirst: no row of the ferry`s list')
    return NL.join(list(head) + [''] + list(note) + ([''] if note else []) + [FERRY_TITLE] + ['  ' + r for r in ferry] + ['', OWN_TITLE] + ['  ' + r for r in own]) + NL


def regenerate(text):
    """a banked list read back through compose: its head, and its rows by section, whatever the sections' banked titles. Pure in its argument."""
    ls = text.replace('\r', '').split(NL)
    heads = [i for i, l in enumerate(ls) if l.startswith('## ')]
    fi = [i for i in heads if 'READ-FIRST LIST' in ls[i]][0]
    oi = [i for i in heads if i > fi][0]
    nxt = ([i for i in heads if i > oi] + [len(ls)])[0]
    rows = lambda a, b: [l[2:] for l in ls[a:b] if l.startswith('  ')]
    return compose(ls[:ls.index('')], rows(fi + 1, oi), rows(oi + 1, nxt))


def write(act):
    """data/<act>_readfirst_rows.json (head, note, ferry, own) composed to data/<act>_readfirst.txt; refused where the bank stands, the bank
    being unchanged from its first commit (hand_ok)."""
    p = os.path.join(A.D, '%s_readfirst.txt' % act)
    if os.path.exists(p):
        raise SystemExit('readfirst: %s stands; hand_ok reads it unchanged from its first commit' % p)
    with io.open(os.path.join(A.D, '%s_readfirst_rows.json' % act), encoding='utf-8') as f:
        j = json.load(f)
    t = compose(j['head'], j['ferry'], j['own'], j.get('note') or ())
    with open(p + '.tmp', 'wb') as f:
        f.write(t.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  written data/%s_readfirst.txt: ferry rows %d ; own rows %d' % (act, len(j['ferry']), len(j['own'])))


def _first_commit(rel):
    out = A.gs('relay', 'log', '--format=%H', '--diff-filter=A', '--', rel) or ''
    cs = [c for c in out.split('\n') if c.strip()]
    return cs[-1] if cs else None


def hand_ok(act, closure_dir=None):
    """dict(ok, hand, unchanged, first, closure): the hand list data/<act>_readfirst.txt present and byte-equal to its first commit, and no
    data/<act>_readfirst_closure.txt (closure_dir may name another directory to read for the closure bank, for a plant)."""
    rel = 'data/%s_readfirst.txt' % act
    p = os.path.join(A.D, '%s_readfirst.txt' % act)
    hand = os.path.isfile(p)
    first = _first_commit(rel) if hand else None
    now = open(p, 'rb').read().replace(b'\r', b'') if hand else None
    then = A.blob(first, rel) if first else None
    unchanged = hand and then is not None and then.replace(b'\r', b'') == now
    closure = os.path.isfile(os.path.join(closure_dir or A.D, '%s_readfirst_closure.txt' % act))
    return dict(ok=bool(hand and unchanged and not closure), hand=hand, unchanged=bool(unchanged), first=(first or '')[:8], closure=closure)


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != 'write':
        raise SystemExit('usage: readfirst.py write <act>')
    write(sys.argv[2])
