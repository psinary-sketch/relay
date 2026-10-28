# -*- coding: utf-8 -*-
"""standing/readfirst.py -- v1.2.2 ((R332)(2)(iii)): THE READFIRST CLOSURE READER RETIRED; THE HAND LIST THE BANK OF RECORD.

b692's closure reader (tools/circuit_read.py readfirst) wrote data/<act>_readfirst_closure.txt and _diff.txt beside the hand list; b710's
reading 5 recommended the hand list stand alone, and (R332)(2)(iii) retires the closure from b722: data/<act>_readfirst_closure.txt is no
longer written. The arm's reading: the hand list present, unchanged since the commit that first carried it (its step-zero commit), and no
closure bank of the act's own. Nothing written; circuit_read.py stays where it is, its readfirst route no longer called by a close.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

RETIRED_FROM = 'b722'


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
