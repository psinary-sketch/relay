# -*- coding: utf-8 -*-
"""standing/amend.py -- v1.17.0, (R347)(2)(i), b736 events (1): THE FACE THAT DID NOT FOLLOW THE AMENDMENT.

The author's word at a prompt that widens or narrows a ruling clause is an amendment row, banked in data/<act>_amendments.json; the face's (W)
row and N5's text are regenerated from the ruling plus its amendment rows before the lock, the regeneration printed. b736's word amending
(R346)(4) widened the writes to the PLACE-papers file each passed item names; the worklist carried three doors from 02:07Z, the face's (W) row,
composed from the ruling's clauses alone (standing.faceform.clause_writes), did not, and N5 read REFUTED on it.

  data/<act>_amendments.json = {"rows": [{"at": utc, "clause": "(R346)(4)", "words": the author's words verbatim, "widens": [paths], "narrows": [paths]}]}
  writes(ruling, rows) -> [paths]           the ruling's clause-ordered files, each amendment's widened paths added and its narrowed paths removed
  missing(ruling, rows, face) -> [paths]    the files writes() names that the face's (W) list does not cover (faceform.w_missing's reading)
  w_row(ruling, rows, face) -> str or None  the regenerated (W) row naming them; None where the face covers every one
  n5_clause(ruling, rows, face) -> str      N5's write clause regenerated: the files beyond the face's (W) list the amended ruling orders, or none
  regenerate(act, ruling, face) -> lines    the printed regeneration: the rows read, the files, the (W) row, N5's clause
Pure in its arguments but regenerate, which reads the act's bank; nothing written.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import faceform as FF   # noqa: E402

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def bank_path(act, relay=RELAY):
    return os.path.join(relay, 'data', '%s_amendments.json' % act)


def rows_of(act, relay=RELAY):
    p = bank_path(act, relay)
    if not os.path.exists(p):
        return []
    with io.open(p, encoding='utf-8') as f:
        return list(json.load(f).get('rows') or [])


def writes(ruling, rows):
    out = set(FF.clause_writes(ruling))
    for r in rows or ():
        out |= set(r.get('widens') or ())
    for r in rows or ():
        out -= set(r.get('narrows') or ())
    return sorted(out)


def _split(p):
    """(repository, path): a path written `PLACE-papers/...` or `SIDE-x/...` is that repository's, a bare path the relay's."""
    for pre in ('relay/', 'PLACE-papers/'):
        if p.startswith(pre):
            return pre[:-1], p[len(pre):]
    m = re.match(r'(SIDE-[\w-]+)/(.*)$', p)
    return (m.group(1), m.group(2)) if m else ('relay', p)


def _covered(p, face):
    """the face's (W) list read as the scorer reads it: tools/act_close.py w_patterns and w_allows, a backticked path carrying its repository.
    b736's row named the three doors bare (`phase2/method/...`), a form w_patterns does not read, and N5 counted them beyond the list."""
    sys.path.insert(0, os.path.join(RELAY, 'tools'))
    import act_close as AC
    repo, rel = _split(p)
    return AC.w_allows(rel, AC.w_patterns(face or ''), repo)


def missing(ruling, rows, face):
    return [p for p in writes(ruling, rows) if not _covered(p, face)]


def w_row(ruling, rows, face):
    miss = missing(ruling, rows, face)
    if not miss:
        return None
    shown = ' '.join('`%s/%s`' % _split(p) for p in miss)
    return '### | the ruling`s clauses and its amendment rows, read by the composer (v1.17.0) | %s |' % shown


def n5_clause(ruling, rows, face):
    miss = missing(ruling, rows, face)
    return ('no file written beyond the (W) list regenerated from the ruling and its %d amendment row%s' % (len(rows or ()), '' if len(rows or ()) == 1 else 's')
            + ('' if not miss else ' ; THE FACE LACKS %s' % ', '.join(miss)))


def regenerate(act, ruling, face, rows=None, relay=RELAY):
    rows = rows_of(act, relay) if rows is None else rows
    L = ['### THE (W) REGENERATION ((R347)(2)(i)): the ruling`s clauses plus %d amendment row%s, data/%s_amendments.json' % (len(rows), '' if len(rows) == 1 else 's', act)]
    for r in rows:
        L.append('  %s %s widens %s narrows %s' % (r.get('at'), r.get('clause'), r.get('widens') or 'none', r.get('narrows') or 'none'))
    L.append('  the files ordered: %d ; the face lacks: %s' % (len(writes(ruling, rows)), missing(ruling, rows, face) or 'none'))
    L.append('  the (W) row: %s' % (w_row(ruling, rows, face) or 'none owed, the face covers every file'))
    L.append('  N5: %s' % n5_clause(ruling, rows, face))
    return L
