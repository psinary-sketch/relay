# -*- coding: utf-8 -*-
"""b461_components.py -- COMPONENT 2: THE RULE APPLIED.

### ### **b396's RULE IS QUOTED AT ITS ADDRESS AND NOT PARAPHRASED**, and the order's disposition
### rule is applied ### **AS WRITTEN, CONJUNCTIVELY**, with the count the other reading would give
### MEASURED AND PRINTED BESIDE IT rather than substituted for it.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def main():
    inv = json.loads(read(os.path.join(D, 'b461_inventory.json')))
    rows = inv['rows']

    rec('=' * 104)
    rec('### COMPONENT 2 -- THE RULE APPLIED.')
    rec('=' * 104)

    # ### b396's RULE, QUOTED AT ITS ADDRESS.
    ot = read(OT).split(NL)
    hit = [(i + 1, l) for i, l in enumerate(ot) if 'keeps nine tenths' in l]
    rec('  ### b396`S RULE, QUOTED AT ITS ADDRESS AND NOT PARAPHRASED:')
    if hit:
        n, l = hit[0]
        m = re.search(r'[^.]*keeps nine tenths[^.]*\.', l)
        rec('      OPEN_TRAILS.md:%d | %s' % (n, (m.group(0) if m else l).strip()[:220]))
    else:
        rec('      ### MISS -- the rule is not at the address the order names.')
    rec('')

    # ### THE DISPOSITION, THE ORDER'S OWN AND CONJUNCTIVE.
    rec('  ### THE DISPOSITION RULE, THE ORDER`S OWN, APPLIED AS WRITTEN:')
    rec('  ###   RETIRED        = never failed at a close ### AND ### no positive control statable')
    rec('  ###   GIVEN CONTROLS = its controls are one-line additions')
    rec('  ###   KEPT AS IS     = it already has both')
    ever = {'G-NOEXTRAKIND', 'G-WRITELIST-KINDS'}
    per, retired, given, kept = [], [], [], []
    for r in rows:
        never = r['name'] not in ever
        nopos = r['const']
        if never and nopos:
            d = 'RETIRED'
            retired.append(r['name'])
        elif r['exercised_today']:
            d = 'KEPT AS IS'
            kept.append(r['name'])
        else:
            d = 'GIVEN CONTROLS'
            given.append(r['name'])
        per.append(d)
    rec('')
    rec('      ### ### **RETIRED : %d.**' % len(retired))
    for n in retired:
        rec('          %-34s -- predicate is the literal `True`; never failed at a close; no control statable'
            % n)
    rec('      ### ### **GIVEN CONTROLS : %d. ### KEPT AS IS : %d.**' % (len(given), len(kept)))
    rec('')

    # ### THE OTHER READING, MEASURED AND PRINTED BESIDE IT -- NEVER SUBSTITUTED.
    disj = [r['name'] for r in rows
            if (r['name'] not in ever) or (r['const']) or (not r['real'])]
    weak = [r['name'] for r in rows if (not r['real']) and (not r['const'])]
    rec('  ### ### **THE OTHER READING, MEASURED AND PRINTED BESIDE THE ONE APPLIED, NOT SUBSTITUTED FOR IT.**')
    rec('  ### The cull the order`s expectations reach for would follow from a DISJUNCTIVE rule -- retire an')
    rec('  ### arm that has never failed ### **OR** ### whose only control is a mutation of the act`s own')
    rec('  ### wording. ### **UNDER THAT READING %d OF %d WOULD RETIRE.**' % (len(disj), len(rows)))
    rec('  ### And the sharper figure inside it: ### **%d ARMS HAVE ONLY A SYNTHETIC CONTROL**, and %d of'
        % (len(weak), len(inv['face_only'])))
    rec('  ### those read ### **NOTHING BUT THE ACT`S OWN FACE** -- they test that the face SAYS a thing,')
    rec('  ### not that the act DID it. ### **WHICH RULE GOVERNS IS THE AUTHOR`S AND IS NOT DECIDED HERE.**')
    rec('')

    rec('  ### ### **BEFORE AND AFTER.**')
    after = len(rows) - len(retired)
    rec('      arms declared before : %d' % len(rows))
    rec('      retired              : %d' % len(retired))
    rec('      given controls       : %d' % len(given))
    rec('      kept as is           : %d' % len(kept))
    rec('      arms declared after  : %d   ### in the successor`s own (G2) block, %d are written'
        % (after, 0))
    rec('      ### **AND THE SUCCESSOR DOES NOT CARRY ALL %d FORWARD:** it declares a SHORTER list, because' % after)
    rec('      ### an arm whose only control is a mutation of this act`s own wording was not written into it')
    rec('      ### where the act had no such sentence to test. ### **THE COUNT THE SUCCESSOR ACTUALLY RUNS IS')
    rec('      ### PRINTED BY THE SUITE ITSELF AND IS NOT TYPED HERE.**')
    rec('=' * 104)

    json.dump(dict(per_arm=per, retired=retired, given=given, kept=kept,
                   before=len(rows), after=after,
                   disjunctive_would_retire=len(disj), synthetic_only=len(weak),
                   face_only=len(inv['face_only']),
                   unexercised=0, neg_failures=0, pos_passes=0),
              io.open(os.path.join(D, 'b461_dispositions.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    io.open(os.path.join(D, 'b461_exercise.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return retired


if __name__ == '__main__':
    main()
    # ### THE SUITE RUNS ITSELF AND APPENDS ITS EXERCISE TABLE TO THE SAME RECORD.
    r = subprocess.run([sys.executable, os.path.join(T, 'b461_checks.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    with io.open(os.path.join(D, 'b461_exercise.txt'), 'a', encoding='utf-8', newline=NL) as fh:
        fh.write(NL + r.stdout)
    ex = json.loads(read(os.path.join(D, 'b461_exercise.json')) or '{}')
    dsp = json.loads(read(os.path.join(D, 'b461_dispositions.json')))
    dsp.update(unexercised=ex.get('unexercised', 0), neg_failures=ex.get('neg_failures', 0),
               pos_passes=ex.get('pos_passes', 0), runs=ex.get('run', 0))
    io.open(os.path.join(D, 'b461_dispositions.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dsp, indent=1, ensure_ascii=False) + NL)
    print(r.stdout[-1600:])
