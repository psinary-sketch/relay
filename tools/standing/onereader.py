# -*- coding: utf-8 -*-
"""standing/onereader.py -- v1.28.0, (R358)(3)(i), b747 events (4), N3: THE ONE READER OF A SCORE THAT READS THE ROOT PROMPT.

b747's scores, written before the root (data/b747_scores.json), read N3 REFUTED on its last clause alone, "the root prompt`s sentences about the
entry not the composer`s: UNREAD (no root prompt banked yet)"; the record and the trail were composed from that bank, and the close, reading the
same clause over the banked prompt, read N3 HELD: two readings of one score. The repair: a score whose every clause but the root prompt's is
clean, read before the root prompt is banked, is PENDING -- the record and the trail carry PENDING, and the close's reading, made once over the
banked prompt, is the one entered. No bank is written after the root for it.

  verdict(ok, scope) -> 'HELD' | 'PENDING' | 'REFUTED'
     ok     the route's whole reading (every clause, the root prompt's among them)
     scope  the route's locals: where it carries `ok_rest` (every clause but the root prompt's) and `unb_` (the root prompt's reading: None while
            no prompt is banked, [] when clean, a list of faults otherwise), the one reader decides; where it does not (every act module before
            b748, rendered from the same template), the verdict is the route's own, HELD or REFUTED, unchanged.
"""

ROOT_UNREAD = 'UNREAD (no root prompt banked yet)'


def verdict(ok, scope=None):
    s = scope or {}
    if ok:
        return 'HELD'
    if 'ok_rest' in s and 'unb_' in s:
        if s['ok_rest'] and s['unb_'] is None:
            return 'PENDING'
    return 'REFUTED'


def one_reading(pre, close):
    """the readings of one score in the record (the pre-root bank) and at the close: (one, why). One reading where they agree, or where the
    pre-root reading is PENDING and the close's is the one entered; two readings where the pre-root bank carries a verdict the close contradicts."""
    p, c = (pre or [None])[0], (close or [None])[0]
    if p == c:
        return True, 'the record and the close read %s' % p
    if p == 'PENDING' and c in ('HELD', 'REFUTED'):
        return True, 'the record reads PENDING, the close`s %s the one entered' % c
    return False, 'TWO READINGS: the record %s, the close %s' % (p, c)
