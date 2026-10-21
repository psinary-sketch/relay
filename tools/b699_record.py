# -*- coding: utf-8 -*-
"""b699_record.py -- THE ACT'S RECORD TOOL, b699 under (R309).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b699 -- its worklist
### module K, ACT and PREV -- so that its carried routes (the helpers, the guarded landing, rowgen, answers, defects and the late routes)
### write b699's banks under b699's names; a route whose text names b698's ruling is written here afresh. (R262)(2): the one conversion of a
### backtick possessive stays b652's, imported through b698's module. Every python child is started as `python -X utf8`, no environment
### mapping passed.
### Written by the Write tool at b699 in stages: stage one, step zero's routes; Components 1-5 by the Edit tool.
### Routes: `python tools/b699_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b699_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited

R.K, R.ACT, R.PREV, R.SP = K, 'b699', 'b698', K.SP
ACT, PREV = 'b699', 'b698'
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land

READERS = ['read_branch_row']
read_branch_row = R.read_branch_row


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen, answers, defects = R.rowgen, R.answers, R.defects


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R309)(6); b698's form)
def branches(*a):
    """`branches before`: data/b699_branches_before.json -- b698's route, carried (every branch (R309)(6) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b699_branches.txt (.json) --
    each branch's fate read now against the tips banked before, in (R309)(6)'s words."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b699_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R309)(6): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b699_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after.']
    L += ['  %-18s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[4:]))


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b699_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
