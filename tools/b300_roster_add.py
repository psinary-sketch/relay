# -*- coding: utf-8 -*-
"""b300_roster_add.py -- RULING (4): THE ARC KEYSTONE JOINS THE REVIEWER MIRROR'S ROSTER.

### **APPEND-ONLY, IDEMPOTENT, AND READ BACK FROM DISK.**

### ### **WHY A TOOL AND NOT AN EDIT.** ### b183: the roster was an OUTPUT written as though it
### were an INPUT, and a row added at b182 changed nothing while the mirror verified ### **CLEAN
### AT 33 FILES WITHOUT THE FILE IN IT.** ### The lesson is not "edit carefully"; it is
### ### **WRITE THE INPUT, THEN READ IT BACK, THEN BUILD FROM WHAT WAS READ.**

### ### **AND THE COLLISION CHECK IS RUN HERE RATHER THAN LEFT TO THE BUILDER'S `throw`.** ### The
### export is FLAT (b144): two roster paths with the same leaf silently share one slot, and the
### MANIFEST still verifies clean because clause 1 checks the export against ITSELF. ### **A NEW
### ROW IS EXACTLY WHEN THAT CAN HAPPEN, SO THE LEAF NAMESPACE IS COUNTED BEFORE AND AFTER.**
"""
import collections
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SEP = chr(92)                      # ### the roster stores repo-relative WINDOWS paths
NEW = SEP.join(['phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'])
NOTE = (" ### b300: THE ARC KEYSTONE ADDED BY THE AUTHOR'S RULING (4) OF THE b300 FERRY -- the"
        " document b299 wrote. ### APPENDED AT THE END SO NO EXISTING ROW CHANGES ITS SLOT:"
        " order is significant and the first entry wins the plain slot.")

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def leaves(files):
    return [f.split(SEP)[-1] for f in files]


def collisions(files):
    return {k: v for k, v in collections.Counter(leaves(files)).items() if v > 1}


def main():
    print('=' * 100)
    print('b300 -- THE ROSTER, PER RULING (4).')
    print('=' * 100)
    j = json.load(io.open(ROSTER, encoding='utf-8'))
    before = list(j['files'])
    print('  roster rows before          : %d' % len(before))
    print('  leaf collisions before      : %s' % (collisions(before) or 'none'))

    src = os.path.join(PP, NEW.replace(SEP, os.sep))
    exists = os.path.exists(src)
    print('  the file the row points at  : %s' % NEW)
    print('  exists on disk              : %s   bytes: %s'
          % (exists, os.path.getsize(src) if exists else '-'))
    if not exists:
        print('  ### HARD FAILURE -- REFUSING TO ADD A ROSTER ROW FOR A FILE THAT IS NOT THERE.')
        print('  ### The builder would print MISSING and CONTINUE, and the export would verify')
        print('  ### CLEAN without it -- which is b182/b183 exactly.')
        return 2

    if NEW in before:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN. (idempotent)')
        print('  leaf collisions now         : %s' % (collisions(before) or 'none'))
        print('=' * 100)
        return 0

    j['files'].append(NEW)
    j['lastChanged'] = '2026-09-02'
    j['_history'] = j['_history'] + NOTE
    data = (json.dumps(j, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    open(ROSTER + '.tmp', 'wb').write(data)
    os.replace(ROSTER + '.tmp', ROSTER)

    back = json.load(io.open(ROSTER, encoding='utf-8'))
    after = back['files']
    # ### THE COLLISION TEST IS ### DIFFERENTIAL ### , AND THE FIRST VERSION OF IT WAS NOT.
    # ### **THE ROSTER ALREADY CARRIES TWO `README.md` LEAVES BY DESIGN** -- the repo front door
    # ### and the ledger-split archive's -- and the builder resolves them by the b144 rule
    # ### (parent-directory + '__' + leaf), with the first entry winning the plain slot.
    # ### ### **A TEST DEMANDING ZERO COLLISIONS FAILS ON A CONDITION THIS ACT DID NOT CREATE AND
    # ### ### CANNOT FIX, AND FAILING THERE WOULD TEACH THE NEXT READER TO IGNORE IT.**
    # ### So the question is the one this act can answer: ### **DOES THIS ROW ADD A COLLISION?**
    cb, ca = collisions(before), collisions(after)
    added = {k: v for k, v in ca.items() if k not in cb or v > cb[k]}
    ok = (NEW in after and len(after) == len(before) + 1
          and after[:len(before)] == before and not added)
    print('  ### READ BACK FROM DISK:')
    print('    roster rows after         : %d' % len(after))
    print('    last row                  : %s' % after[-1])
    print('    the new row is present    : %s' % (NEW in after))
    print('    every prior row unmoved   : %s' % (after[:len(before)] == before))
    print('    leaf collisions before    : %s   ### PRE-EXISTING, BUILDER-RESOLVED (b144)'
          % (cb or 'none'))
    print('    leaf collisions after     : %s' % (ca or 'none'))
    print('    collisions ADDED BY THIS ROW : %s' % (added or 'none'))
    print('    %s' % ('PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE ROW IS ON DISK AND THE FLAT NAMESPACE STILL HAS ROOM FOR IT.')
    print('  ### It does not mean the mirror was rebuilt. ### THAT IS THE NEXT STEP AND IT IS')
    print('  ### VERIFIED ON ALL THREE CLAUSES, NOT ON THIS ONE.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
