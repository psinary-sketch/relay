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


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R309)(1)
WH = ('*Appended 2026-10-21 by b699 to b698’s entry (:9684), under `(R309)`(1) -- b698 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b698_closing.txt):*')
WB = (' “b698 closed: relay f19eccc4, PLACE-papers 1a8d8d1; suite 122 of 123; root 1db808250727b615…; 4 prompts answered; 4 defects” '
      '(data/b698_closing.txt :1), the closing 14a0cb57 pushed and read back at relay main (data/b698_closing_push_out.txt :5). '
      'CORRESPONDENCE-DOMINANCE built as tools/circuit_correspondence.py, its controls passing first -- h2_sign against itself HOLDS at every '
      'binder, the planted binder caught (data/b698_correspondence_dominance.txt :77); the real reading DIFFERS at binder 1, none of the 14 rows '
      'agreeing (:76), the SIDE-lv-conservation side read as SOURCE TEXT at v0.13.0 = 8e3bc76 by the answer’s fallback since no hosted run at '
      'that tag could print residue_irreducible, the verdict qualified as source against print; W-ORD-H2-BRIDGE annotated beneath with binder 1 '
      'named as its open object (OPEN_TRAILS :15294); CLAUSE-DOMINANCE 1 of 2 by closure, DIFFERS at binder 1 by correspondence. The '
      'regularity-uses bank at 17 uses, no Lean: W1 (C¹ with absolutely integrable second derivative) 11 DISCHARGED / 6 RE-PROVED / 0 '
      'OBSTRUCTED, W2 (even C² of rapid decay without compact support) 6 / 4 / 7, W3 (finite sums of autocorrelations) 13 / 4 / 0 '
      '(data/b698_regularity_uses.txt :85), W1 and W3 together named as the wider class for the author’s word (:87). SIDE-simplicity README :9 '
      're-cut and tagged v0.1.2 naming v0.1.1 (peeled 967f747); SIMPLICITY_OF_RIEMANN_ZEROS :441 rewritten by the generator alone on the '
      'one-table roster; the partner copy’s differing lines entered beneath W-ORD-ONE-COPY (OPEN_TRAILS :15296), the generator’s stored figure 6 '
      'against the count 18 (data/b698_onecopy.txt :61). Two rules banked (data/b698_rules.txt :6, :10), row (1) binding from b699, row (2) '
      'bound at b698; the arithmetic plan’s row appended; b697’s weight line written (FINDINGS :9682). All eight scores HELD '
      '(data/b698_scores_close.json); the suite 122 of 123 before and after the push, G-NOTHING-RAN-AHEAD failing undeclared -- section (0) of '
      'the sealed face naming relay 2d19edd and 069778f in words and not by hash (data/b698_checks.txt :11, data/b698_checks_postpush.txt :11), '
      'answered by the generated corrigendum; the root 1db80825; no lean on the host; mirror-refresh-2026-10-21-b698.zip CLEAN with the root '
      'line. Four defects, all the seat’s -- (a) the stale-cell prompt quoting the stored figure 6 without a recount, (b) eight piped reads, one '
      'whole read of a 505-line file and two whole git blobs against the read rule, (c) the two face hashes left undeclared, (d) the record step '
      're-run after the root rewriting the answers bank’s timestamp line, restored by the Edit tool to the committed bytes with its write time '
      'later than the root’s (data/b698_defects.txt :6-:32). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B698_ENTRY,
         check=[('FINDINGS.md', K.B698_ENTRY, '## CLAUSE-DOMINANCE by closure and by correspondence: 1 of 2 by closure'),
                ('OPEN_TRAILS.md', K.B698_TRAIL, '### b698')], dry=dry)


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, c1=c1)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b699_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
