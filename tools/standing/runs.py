# -*- coding: utf-8 -*-
"""standing/runs.py -- v1.19.0, (R349)(2)(iv), b738 events (2): A RUN TABLE'S LAST ROW READ BEHIND A GUARD, AN EMPTY TABLE PRINTED NO RUNS BY NAME.

b738's G-DERIVATION-GRADED compared its bank's dispatch rows with K.EF_RUNS and then read rows[-1]; on b737's state K.EF_RUNS is () and the
table has no rows, so the two empty lists compared equal, all() over no rows was True, and rows[-1] raised IndexError, counted FAIL among
the DIVERGE. Here the last row is read through last(), and reading() names the state: NO RUNS where the table and the worklist's runs are
both empty, RUNS where the table's run ids are the worklist's in order, DIFFERS otherwise. Pure in its arguments; nothing written.

  last(rows, col)          -> the last row's column, or NO_RUNS
  reading(rows, runs, col) -> (state, note)
"""
NO_RUNS = 'NO RUNS'


def last(rows, col, default=NO_RUNS):
    return rows[-1][col] if rows else default


def reading(rows, runs, col=4):
    ids = [int(r[col]) for r in rows]
    if not rows and not runs:
        return NO_RUNS, 'no dispatch row in the bank and none in the worklist'
    if ids == [int(x) for x in runs]:
        return 'RUNS', '%d rows, the worklist`s runs in order' % len(rows)
    return 'DIFFERS', 'the bank`s runs %s against the worklist`s %s' % (ids[:12], list(runs)[:12])
