# -*- coding: utf-8 -*-
"""standing/titlerule.py -- v1.35.8, (R368)(3): THE TITLE RULE, FROM b757'S HALT AT [22].

The ruling's words (relay data/b758_ferry.txt :13): "THE TITLE RULE, from the halt: an entry's title and a bank's head are composed with the
typographic apostrophe where an apostrophe is meant, and the composer refuses a backtick in either; its control is one planted title."
b757's entry title was composed with two backticks; the landing wrote them as ’ through its one conversion, the findings bank kept the head
raw, and tools/standing/act.py :82 refused the landed line at [22] (data/b757_events.txt; repaired on the reader's side at v1.35.6).

THE COMPOSER. Every ledger write of the record tool goes through b698's module R: `land` (items of (file, head, text), the c1 routes and the
record's other landings) and `_land_one` (the FINDINGS entry and the OPEN_TRAILS trail, the head written beside the line into the act's bank
as its `head`). rebind(R) wraps both once: a head carrying a backtick is refused before anything is converted, screened, guarded, appended
or banked, dry or written, the refusal naming the head and the rule. record.tpl :38 calls rebind(R) at every load of a record tool, the line
count kept for the older acts' line-keyed overrides. The head alone is read: the text beneath a head keeps its code spans, converted as before.

  fault(head) -> None or the refusal's words
  rebind(R)   -> R, its land and _land_one guarded once (a second call leaves them as they are)
Imports the standard library alone; writes nothing.
"""
import functools
import sys

RULE = '(R368)(3)'


def fault(head):
    """None, or the refusal: a backtick in an entry's title or a bank's head, where the typographic apostrophe is meant."""
    h = str(head or '')
    if '`' not in h:
        return None
    k = h.index('`')
    return ('### THE TITLE RULE %s: A BACKTICK IN THE HEAD AT CHARACTER %d (%r) -- AN ENTRY`S TITLE AND A BANK`S HEAD ARE COMPOSED WITH THE '
            'TYPOGRAPHIC APOSTROPHE ’ WHERE AN APOSTROPHE IS MEANT, AND NO CODE SPAN -- NOTHING WRITTEN' % (RULE, k + 1, h[max(0, k - 30):k + 30]))


def _guard_land(fn):
    @functools.wraps(fn)
    def land(items, *a, **k):
        for it in items or ():
            f_ = fault(it[1] if len(it) > 1 else '')
            if f_:
                print(f_, flush=True)
                sys.exit(6)
        return fn(items, *a, **k)
    land.__titlerule__ = True
    return land


def _guard_one(fn):
    @functools.wraps(fn)
    def _land_one(path, head, *a, **k):
        f_ = fault(head)
        if f_:
            print(f_, flush=True)
            sys.exit(6)
        return fn(path, head, *a, **k)
    _land_one.__titlerule__ = True
    return _land_one


def rebind(R):
    """R's land and _land_one guarded once; a second call (the previous act's record tool imported beside the act's) leaves them as they are."""
    if hasattr(R, 'land') and not getattr(R.land, '__titlerule__', False):
        R.land = _guard_land(R.land)
    if hasattr(R, '_land_one') and not getattr(R._land_one, '__titlerule__', False):
        R._land_one = _guard_one(R._land_one)
    return R
