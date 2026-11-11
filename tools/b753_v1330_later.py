# -*- coding: utf-8 -*-
"""tools/b753_v1330_later.py -- THE v1.33.0 BANK WITH THE COMMITS AFTER ITS OWN (the author's sixth word (4), 2026-11-11: "The version
stays v1.33.0, and its bank names each commit after its own at which a standing tool changed, with the controls run after it.").

Reads from git the relay commits after v1.33.0's own (C1_STANDING, 7c91353a) that touch tools/standing/, each with the standing files it
changed, and refuses where they are not the worklist's C1_STANDING_LATER; runs tools/standing/v1330.py control (the nine, as that tool prints
them) and tools/standing/roster.py's controls now, after every such commit, the free memory read before each; maps each changed file to the
control that reads it and refuses where a file has none; and writes data/b753_standing_v1330.txt whole through tools/standing/figbank.py:
v1330's lines, then the section naming the later commits and the controls run after them, then v1330's foot as the bank's last line.
Writes nothing else. No identifier of the author is read into any string. Written at b753 by the Write tool.

  python -X utf8 -u tools/b753_v1330_later.py [--bank]
"""
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b753_worklist as K    # noqa: E402
import figbank as FB         # noqa: E402
import roster as RO          # noqa: E402
import v1330 as V            # noqa: E402

NL = '\n'
# ### each standing file a later commit changed, and the control run after it that reads it
CONTROL_OF = {'tools/standing/chain.py': 'v1330.py`s (chain) above, the blob answer and the chain read',
              'tools/standing/v1330.py': 'v1330.py`s nine controls above, the controls tool itself run whole',
              'tools/standing/roster.py': 'the roster`s controls below (tools/standing/roster.py control_lines)'}


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def later():
    """the relay commits after C1_STANDING touching tools/standing/, oldest first: (hash, commit epoch, [standing files changed])."""
    out = []
    for l in _git('log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.C1_STANDING, '--', 'tools/standing').split(NL):
        if l.strip():
            h, ct = l.split()
            fs = [x for x in _git('show', '--name-only', '--format=', h).split() if x.startswith('tools/standing/')]
            out.append((h, int(ct), fs))
    return out


def main(argv):
    lt = later()
    if [h[:8] for h, _c, _f in lt] != [x[:8] for x in K.C1_STANDING_LATER]:
        sys.exit('### THE COMMITS AFTER v1.33.0`S OWN TOUCHING tools/standing/ ARE %s, NOT THE WORKLIST`S %s -- NOTHING WRITTEN' % (
            [h[:8] for h, _c, _f in lt], list(K.C1_STANDING_LATER)))
    unmapped = [(h[:8], f) for h, _c, fs in lt for f in fs if f not in CONTROL_OF]
    if unmapped:
        sys.exit('### A FILE A LATER COMMIT CHANGED HAS NO CONTROL MAPPED: %s -- NOTHING WRITTEN' % unmapped)
    t0 = int(time.time())
    vr = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(S, 'v1330.py'), 'control'], capture_output=True, text=True,
                        encoding='utf-8', errors='replace', cwd=RELAY)
    vl = vr.stdout.replace('\r', '').rstrip(NL).split(NL)
    if vr.returncode != 0 or not vl or not vl[-1].startswith('### ### **v1.33.0: CONTROLS '):
        sys.exit('### v1330.py control DID NOT END ON ITS FOOT (exit %s; last line %r) -- NOTHING WRITTEN' % (vr.returncode, vl[-1:] ))
    foot = vl[-1]
    fl = V.free_line()
    rc, rok = RO.control_lines()
    t1 = int(time.time())
    iso = lambda e: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(e))
    after = all(c < t0 for _h, c, _f in lt)
    sec = ['', '## THE COMMITS AFTER v1.33.0`S OWN AT WHICH A STANDING TOOL CHANGED, EACH WITH THE CONTROLS RUN AFTER IT (the author`s sixth word (4))',
           '  read from git: the relay commits after %s (v1.33.0`s own) touching tools/standing/, oldest first; the version stays v1.33.0 ; '
           'the controls above and below run at %s-%s, after each commit, by tools/b753_v1330_later.py' % (K.C1_STANDING[:8], iso(t0), iso(t1))]
    for h, c, fs in lt:
        sec.append('  %s at %s: %s' % (h[:8], iso(c), ' ; '.join('%s -- read by %s' % (f, CONTROL_OF[f]) for f in fs)))
    sec += ['  every such commit before the controls` run: %s' % after, '', '### THE ROSTER`S CONTROLS, RUN AFTER %s:' % lt[-1][0][:8], fl]
    sec += ['  ' + l for l in rc]
    sec += ['  the roster`s controls all as wanted: %s' % rok, '']
    bank = vl[:-1] + sec + [foot]
    ok = after and rok and foot.endswith('ALL AS WANTED.**')
    print(NL.join(bank))
    if not ok:
        sys.exit('### THE CONTROLS ARE NOT ALL AS WANTED OR A COMMIT FOLLOWS THEIR RUN -- NOTHING WRITTEN')
    if '--bank' in argv:
        r = FB.write(os.path.join(D, 'b753_standing_v1330.txt'), NL.join(bank))
        print('written data/b753_standing_v1330.txt (figbank: %s)' % r['why'])


if __name__ == '__main__':
    main(sys.argv[1:])
