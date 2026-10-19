# -*- coding: utf-8 -*-
"""b692_parts_probe.py -- (R302)(2)'s repair READ BEFORE IT IS MADE: G-RULE-SUITE-PARTS evaluated in memory over b691's real run banks, the
shared tool tools/rule_arms.py imported and unedited, under three forms of the arm's governing-parts reading:
###   V0  the arm as it stands (tools/rule_arms.py :268, :270, the pattern \\bstanding-[a-z]\\b);
###   V1  the ruling's repair alone: the pattern widened to standing-<letter> or standing-<letter><digit> at :268 and :270;
###   V2  V1 and the comparison read by part family: a governing part is met by itself or by its numbered halves (standing-b by standing-b1 and
###       standing-b2, the split data/b684_rules.txt row (1) orders), every run part one of those.
### and, beside b691's banks, a planted b692 run in the five parts this act runs (data/b692_rules.txt names none). Nothing is edited; the
### print is banked as data/b692_parts_probe.txt by this tool's own write. Written by the Write tool at b692.
"""
import os
import re
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
PAT_V0, PAT_V1 = r'\bstanding-[a-z]\b', r'\bstanding-[a-z][0-9]?\b'


def governing(pat):
    gov = []
    for p in RA._banks('b*_rules.txt', 678):
        rows = [r for r in re.split(r'(?m)^  \((?=\d+\) )', RA._rd(p)) if re.search(pat, r)]
        if rows:
            gov.append((RA._act_of(p), os.path.basename(p), sorted(set(re.findall(pat, ' '.join(rows)))) + ['act']))
    return gov


def family_ok(run_parts, gov_parts):
    fam = lambda p: re.sub(r'(?<=^standing-[a-z])[0-9]$', '', p)   # noqa: E731
    return set(fam(p) for p in run_parts) == set(gov_parts) and all(fam(p) in gov_parts for p in run_parts)


def verdict(R, gov, family):
    R = dict(R, governing=gov)
    if not family:
        ok, read, failing, how = RA.reading('G-RULE-SUITE-PARTS', R)
        return ok, read, failing, how
    bad = []
    for (a, k), ps in R['runs'].items():
        g_ = [x for x in gov if x[0] <= a]
        gp = g_[-1][2] if g_ else None
        if gp is None or not family_ok([p for p, _s in ps], gp) or any(s >= 600 for _p, s in ps):
            bad.append(('b%d' % a, k))
    return not bad, len(R['runs']), len(bad), 'run banks %d ; failing %s' % (len(R['runs']), bad or 'NONE')


def main():
    R = RA.sources('b691', SESSION, 'RULING (R301) BEGIN', FIVE, None, '9fc2c81b', '64936ae')
    R692 = dict(R, runs=RA._with(R['runs'], (692, 'arms_prerun'), [(p, 100) for p in FIVE]))
    L = ['b692 -- (R302)(2): THE SUITE-PARTS ARM READ IN MEMORY BEFORE ITS REPAIR IS MADE, tools/rule_arms.py UNEDITED', '',
         '### rows are forms of the arm: the form | the governing lists it reads | its verdict over b691`s real run banks | over the same with a',
         '### planted b692 run in the five parts this act runs.', '']
    for name, pat, fam in (('V0 the arm as it stands', PAT_V0, False), ('V1 the pattern widened alone', PAT_V1, False),
                           ('V2 the pattern widened, the parts read by family', PAT_V1, True)):
        gov = governing(pat)
        v1, v2 = verdict(R, gov, fam), verdict(R692, gov, fam)
        L += ['  %s' % name, '      governing: %s' % '; '.join('%s from b%d: %s' % (b, a, ps) for a, b, ps in gov),
              '      over b691`s banks: %s (read %d, failing %d) -- %s' % ('PASS' if v1[0] else 'FAIL', v1[1], v1[2], str(v1[3])[-160:]),
              '      with a planted five-part b692 run: %s (read %d, failing %d)' % ('PASS' if v2[0] else 'FAIL', v2[1], v2[2]), '']
    L += ['### ### **THE RULING`S REPAIR ALONE (V1) READS THE SAME GOVERNING LISTS AS V0: NO RULES BANK NAMES standing-b1 OR standing-b2, SO b691`S '
          'BANKS AND A FIVE-PART b692 RUN STILL FAIL; V2 READS THEM AS THE SPLIT OF standing-b.**']
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b692_parts_probe.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L))


def after():
    """`after`: the arm AT HEAD, the repaired tools/rule_arms.py read as it stands -- over b691's real run banks, a planted five-part b692 run,
    and the arm's own planted control (rule_arms.ARMS's plant, which must FAIL); banked as data/b692_parts_after.txt (this act's own run
    banks are read by the suite's pre-run, its count printed there)."""
    import subprocess
    R = RA.sources('b691', SESSION, 'RULING (R301) BEGIN', FIVE, None, '9fc2c81b', '64936ae')
    R692 = dict(R, runs=RA._with(R['runs'], (692, 'arms_prerun'), [(p, 100) for p in FIVE]))
    plant = [pl for nm, _r, _f, pl in RA.ARMS if nm == 'G-RULE-SUITE-PARTS'][0]
    blob = subprocess.run(['git', '-C', ROOT, 'hash-object', os.path.join(T, 'rule_arms.py')], capture_output=True, text=True).stdout.strip()
    L = ['b692 -- (R302)(2): THE SUITE-PARTS ARM AT HEAD AFTER ITS REPAIR (tools/rule_arms.py blob %s)' % blob, '',
         '### rows are the states the arm reads: the state | its verdict | read | failing | the arm`s own reading.', '']
    for name, st, want in (('b691`s three run banks and every earlier act`s', R, True), ('with a planted five-part b692 run', R692, True),
                           ('the arm`s planted control (b678 planted, one part `standing`)', plant(R), False)):
        ok, read, failing, how = RA.reading('G-RULE-SUITE-PARTS', st)
        L.append('  %-62s %s ; read %d ; failing %d ; as wanted %s -- %s' % (name, 'PASS' if ok else 'FAIL', read, failing, ok == want, str(how)[-140:]))
    L += ['', '### ### **b691`S BANKS %s ; THE FIVE-PART b692 RUN %s ; THE PLANTED CONTROL %s.**' % tuple(
        ('PASS' if RA.reading('G-RULE-SUITE-PARTS', s)[0] else 'FAIL') for s in (R, R692, plant(R)))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b692_parts_after.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L))


if __name__ == '__main__':
    after() if sys.argv[1:] == ['after'] else main()
