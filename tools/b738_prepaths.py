# -*- coding: utf-8 -*-
"""b738 -- THE PROBE-PATH REFUSAL PRINTED BEFORE THE LOCK GATE, N2: standing.probes.refusal over the relay's tracked paths, its controls first,
the bank written whatever it reads. Reads git; writes data/b738_pathrefusal.txt alone. Carried from tools/b737_prepaths.py, the act's names set.

  python -X utf8 -u tools/b738_prepaths.py [--bank]
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'standing'))
import probes as P   # noqa: E402

ACT = 'b738'
BANK = os.path.join(ROOT, 'data', 'b738_pathrefusal.txt')
PLANTS = ('data/b738_probe_act.txt', 'data/b738_checks_act.txt', 'data/b738_exercise_standing-a.json', 'data/b738_mid_exercise_act.json')


def main():
    names = [n for n in subprocess.run(['git', '-C', ROOT, 'ls-files'], capture_output=True, text=True, encoding='utf-8').stdout.split('\n') if n]
    L = ['b738 -- THE PROBE-PATH REFUSAL, N2, READ BEFORE THE LOCK GATE: standing.probes.refusal OVER THE RELAY`S TRACKED PATHS', '', '## THE CONTROLS FIRST']
    good = 0
    for p in PLANTS:
        r, _l = P.refusal(ACT, names + [p])
        good += bool(r)
        L.append('  a planted %-40s refused: %s' % (p, r))
    L += ['### CONTROLS %d OF %d AS WANTED' % (good, len(PLANTS)), '', '## THE PATHS READ']
    refused, lines = P.refusal(ACT, names)
    L += lines
    L += ['', '### ### **THE PROBE-PATH REFUSAL : %s ; %d TRACKED PATHS READ ; CONTROLS %d OF %d.**' % ('REFUSES' if refused else 'CLEAR', len(names), good, len(PLANTS))]
    if '--bank' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(L) + '\n')
    print(L[-1])


if __name__ == '__main__':
    main()
