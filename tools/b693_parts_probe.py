# -*- coding: utf-8 -*-
"""b693_parts_probe.py -- (R303)(4): G-RULE-SUITE-PARTS's family comparison (tools/rule_arms.py `met`, the b692 V2 repair, :480-:486) READ IN
MEMORY BEFORE THE SUITE, the shared tool imported and unedited, over b692's real run banks and four planted b693 runs:
###   P1  the six parts this act runs (standing-a, standing-c, standing-b1, standing-b2, standing-b3, act)  -- wanted PASS;
###   P2  the five parts of b692 (standing-b1, standing-b2)                                                -- wanted PASS (the halves);
###   P3  standing-b beside its own numbered part standing-b1 (a family read both whole and split)          -- wanted FAIL;
###   P4  a part over 600 s in the six                                                                      -- wanted FAIL;
### and the arm's own planted control (rule_arms.ARMS's plant) -- wanted FAIL. Where the comparison reads numbered halves alone (P1 failing)
### the ruling orders it repaired to read any numbered subdivision; the probe prints which. Nothing is edited; the print is banked as
### data/b693_parts_probe.txt by this tool's own write. Written by the Write tool at b693 from b692_parts_probe.py's form.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import rule_arms as RA   # noqa: E402  ### the shared tool, imported unedited

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/2c300355-703e-4575-81bc-2631a70202cf.jsonl'
FIVE = ['standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'act']
SIX = ['standing-a', 'standing-c', 'standing-b1', 'standing-b2', 'standing-b3', 'act']


def main():
    R = RA.sources('b692', SESSION, 'RULING (R302) BEGIN', FIVE, None, 'f5318624', '9a0dc76')
    plants = (('P1 the six parts this act runs', [(p, 100) for p in SIX], True),
              ('P2 the five parts of b692 (the halves)', [(p, 100) for p in FIVE], True),
              ('P3 standing-b beside its own numbered part standing-b1', [(p, 100) for p in ['standing-a', 'standing-c', 'standing-b', 'standing-b1', 'act']], False),
              ('P4 the six, standing-b3 at 600 s', [(p, 600 if p == 'standing-b3' else 100) for p in SIX], False))
    plant = [pl for nm, _r, _f, pl in RA.ARMS if nm == 'G-RULE-SUITE-PARTS'][0]
    blob = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD:tools/rule_arms.py'], capture_output=True, text=True).stdout.strip()
    src = open(os.path.join(T, 'rule_arms.py'), encoding='utf-8').read().split(NL)
    L = ['b693 -- (R303)(4): THE SUITE-PARTS ARM`S FAMILY COMPARISON READ IN MEMORY BEFORE THE SUITE, tools/rule_arms.py UNEDITED (blob %s)' % blob[:8], '',
         '### the comparison as it stands, verbatim (tools/rule_arms.py :480-:486):'] + ['    :%d %s' % (i, src[i - 1]) for i in range(480, 487)] + [
         '', '### rows are states the arm reads: the state | its verdict | read | failing | wanted | as wanted | the arm`s own reading.', '']
    res = []
    ok0, read0, fail0, how0 = RA.reading('G-RULE-SUITE-PARTS', R)
    L.append('  %-58s %s ; read %d ; failing %d ; wanted PASS ; as wanted %s -- %s' % ('b692`s real run banks and every earlier act`s', 'PASS' if ok0 else 'FAIL',
                                                                                     read0, fail0, ok0, str(how0)[-150:]))
    res.append(ok0)
    for name, parts, want in plants:
        st = dict(R, runs=RA._with(R['runs'], (693, 'arms_prerun'), parts))
        ok, read, failing, how = RA.reading('G-RULE-SUITE-PARTS', st)
        L.append('  %-58s %s ; read %d ; failing %d ; wanted %s ; as wanted %s -- %s' % (name, 'PASS' if ok else 'FAIL', read, failing,
                                                                                        'PASS' if want else 'FAIL', ok == want, str(how)[-150:]))
        res.append(ok == want)
    ok, read, failing, how = RA.reading('G-RULE-SUITE-PARTS', plant(R))
    L.append('  %-58s %s ; read %d ; failing %d ; wanted FAIL ; as wanted %s -- %s' % ('the arm`s planted control (rule_arms.ARMS)', 'PASS' if ok else 'FAIL',
                                                                                     read, failing, not ok, str(how)[-150:]))
    res.append(not ok)
    six = res[1]
    L += ['', '### THE READING: the comparison groups a part by its family (`standing-<letter>` with one trailing digit dropped) and meets a',
          '### governing part by itself or by TWO OR MORE distinct numbered parts of its family (`len(v) >= 2`), never both -- any numbered',
          '### subdivision, not the halves alone; its comment (:481-:482) names the halves, b692`s case. %s' % (
              'NO REPAIR: the six-part run reads PASS as the comparison stands.' if six else '### THE SIX-PART RUN FAILS: THE REPAIR IS ORDERED.'),
          '', '### ### **THE SIX-PART RUN %s ; THE FIVE %s ; A FAMILY READ BOTH WHOLE AND SPLIT %s ; A PART AT 600 s %s ; THE PLANTED CONTROL %s ; '
          'EVERY STATE AS WANTED %s ; %s.**' % (
              'PASS' if res[1] else 'FAIL', 'PASS' if res[2] else 'FAIL', 'FAIL' if res[3] else '### PASS', 'FAIL' if res[4] else '### PASS',
              'FAIL' if res[5] else '### PASS', all(res), 'NO REPAIR, THE COMPARISON READS ANY NUMBERED SUBDIVISION' if six else 'REPAIR ORDERED')]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b693_parts_probe.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    main()
