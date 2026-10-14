# -*- coding: utf-8 -*-
"""b671_epstein_map_narrowed.py -- THE b663 CONTROL RUN ONCE ON THE NARROWED BALLS, under (R281)(6) H3 and the ferry's Component 4.

### tools/b667_epstein_map_balls.py is imported UNEDITED and run by its own main; two of its module names are reassigned before it runs, and
### nothing else: Q0_CERT (:32), the bank its reader q0_list (:146-:155) reads, pointed at this act's narrowed list
### (data/b671_epstein_zeros_narrowed.json.gz, rows of b667's shape: kind, idx, re, im, h, count); and put's bank name (:571), so the print
### lands in data/b671_epstein_control_narrowed.txt (.json) and b667's bank is not written. No computation line of the map is changed; its
### file's sha256 is printed before the run and banked with this wrapper's text as the diff (`diff` route). No lean; no kernel file read.
### Usage: `python -X utf8 tools/b671_epstein_map_narrowed.py diff` -> data/b671_map_narrowed_diff.txt ; `run` -> the map, once.
"""
import hashlib
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
MAP = os.path.join(ROOT, 'tools', 'b667_epstein_map_balls.py')
NARROWED = 'b671_epstein_zeros_narrowed.json'          # ### the reader appends '.gz' (map :150)
BANK = 'b671_epstein_control_narrowed'
NL = chr(10)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diff():
    me = io.open(os.path.abspath(__file__), encoding='utf-8').read()
    L = ['b671 -- THE MAP`S DIFF FOR ITS ONE RUN ON THE NARROWED BALLS (N4): tools/b667_epstein_map_balls.py imported unedited, sha256 %s; the two '
         'names reassigned by this wrapper and nothing else:' % sha(MAP), '',
         '  Q0_CERT : b667_epstein_zeros_certified.json -> %s (the reader`s bank; map :32, read at :150 with `.gz` appended)' % NARROWED,
         '  put`s bank name : b667_epstein_control_balls -> %s (map :571; b667`s bank not written)' % BANK, '',
         '### NO COMPUTATION LINE CHANGED: the map`s file is not edited (its sha256 above, read again after the run in the control bank`s head).', '',
         '### the wrapper, whole (tools/b671_epstein_map_narrowed.py):'] + me.split(NL)
    p = os.path.join(ROOT, 'data', 'b671_map_narrowed_diff.txt')
    open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(NL.join(L[:7]))


def run():
    import b667_epstein_map_balls as MB
    before = sha(MAP)
    MB.Q0_CERT = NARROWED
    orig_put = MB.put
    MB.put = lambda recs, name=BANK: orig_put(recs, name)
    MB.say('### b671: the map tools/b667_epstein_map_balls.py (sha256 %s) run once on data/%s.gz by tools/b671_epstein_map_narrowed.py, '
           'Q0_CERT and put`s bank reassigned, no computation line changed (data/b671_map_narrowed_diff.txt)' % (before, NARROWED))
    MB.main()
    if sha(MAP) != before:
        print('### THE MAP`S FILE CHANGED DURING THE RUN')


if __name__ == '__main__':
    {'diff': diff, 'run': run}.get(sys.argv[1] if len(sys.argv) > 1 else '', lambda: print('usage: diff | run'))()
