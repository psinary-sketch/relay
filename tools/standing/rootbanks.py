# -*- coding: utf-8 -*-
r"""standing/rootbanks.py -- THE ROOT'S REQUIRED BANKS READ AGAINST ITS EXCLUSIONS ((R326)(3)(vi) of the registrations act; defect (j) of the
toolset act): a bank an act's suite requires among the root's items, that the root route's exclusion takes out, is refused at the suite's
import, before any part runs.

The exclusion is the act's root route's own pattern over a bank's basename (the record tool's ROOT_EXCLUDE, passed in), or one built here
from an act and its excluded kinds in the record tools' form, `^<act>_(<kinds>)\.?(txt|json|md|jsonl|)$`. Provenance: the per-act suites'
import check since b706's (j) (`_EXCLUDED_REQUIRED`, e.g. tools/b715_checks.py :187-:189), made one standing function; the toolset act's
carried kind `chain_.*` (b707's) read its required chain-rows bank as excluded until it was narrowed to `chain_half_.*`.

  exclusion(act, kinds, names=()) -> compiled pattern      overlap(required, exclude) -> [paths]
  guard(required, exclude) -> None, or SystemExit naming the overlap
  unlistable(required, act, shared) -> [paths]      guard_listable(required, act, shared) -> None, or SystemExit naming them (v1.9.0, (R339)(2)(iii))
"""
import os
import re


def exclusion(act, kinds, names=()):
    """the root route's exclusion in the record tools' form, from an act, its excluded kinds (a regex alternation) and named banks."""
    return re.compile(r'^' + re.escape(act) + r'_(' + kinds + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


def overlap(required, exclude):
    """the required banks (relay paths) whose basename the exclusion takes out."""
    return [p for p in required if exclude.match(os.path.basename(p))]


def unlistable(required, act, shared=()):
    """the required banks the root route cannot list: it names data/<act>_* alone (the record tool's root_banks), so a bank of another act's name, b728's
    data/b726_mechanisms.txt, can never be among its items and G-ACTROOT-BANKED could never pass (b728 event (9)). `shared` the act's shared banks, named apart."""
    return [p for p in required if not os.path.basename(p).startswith(act + '_') and p not in shared]


def guard_listable(required, act, shared=()):
    """refuse at the suite's import: a SystemExit naming every required bank the root route cannot list."""
    over = unlistable(required, act, shared)
    if over:
        raise SystemExit('### THE ROOT`S REQUIRED BANKS NAME %d BANK(S) THE ROUTE CANNOT LIST ((R339)(2)(iii)): %s' % (len(over), over))


def guard(required, exclude):
    """refuse at import: a SystemExit naming every required bank the exclusion takes out; nothing where there is none."""
    over = overlap(required, exclude)
    if over:
        raise SystemExit('### THE ROOT`S REQUIRED BANKS NAME %d BANK(S) ITS EXCLUSION TAKES OUT (the class repair (3)(vi)): %s ; the exclusion %s' % (
            len(over), over, exclude.pattern))
