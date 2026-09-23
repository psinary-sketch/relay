# -*- coding: utf-8 -*-
"""b498_launch.py -- THE BUILD LAUNCHER, IN ITS OWN CONSOLE. ### **b495's LAUNCHER, CARRIED; ONE CONSOLE.**

### This module is the CHILD process. ### `b498_components.py c3` creates it with
### `CREATE_NEW_CONSOLE | CREATE_NEW_PROCESS_GROUP` and returns; it is NOT imported by the act's
### own tools.
### ### **WHAT CHANGED FROM b495, AND WHY.** ### b495's launcher was created `DETACHED_PROCESS`, so
### it had NO console, and Windows gave `lake` and then `lean` -- console programs started from a
### console-less parent -- A FRESH CONSOLE EACH. ### This launcher OWNS ONE console, created for it
### by the flags above, and `lake` and `lean` inherit it: ### **ONE WINDOW, TITLED, NOT THREE.**
### ### **WHAT DID NOT CHANGE.** ### The instant is taken AT THE MARK, per line, from the clock --
### b480's defect (one precomputed instant stamped on every mark) stays repaired. ### The profile is
### run WHETHER OR NOT THE BUILD EXITED 0. ### No environment variable is added: `LEAN_NUM_THREADS`
### is not set, as the face declares.
"""
import io
import os
import subprocess
import sys
import time

KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LOG = os.path.join(D, 'b498_ef_build.log')
PROBE = os.path.join(D, 'b498_printaxioms.lean')
NAMES = ('Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'Zeta23.EF.EF_lit', 'Zeta23.WeilEF.EF_lit_zeta')
TITLE = 'b498 BUILD of SIDE-explicit-formula -- DO NOT CLOSE THIS WINDOW'
NL = chr(10)


def stamp():
    """### ### **THE CLOCK IS READ HERE, AT THE MARK.** ### Not at import, not at launch."""
    t = time.time()
    return '%s.%03d' % (time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t)), int((t % 1) * 1000))


def say(fh, s):
    line = '%s  %s' % (stamp(), s)
    fh.write(line + NL)
    fh.flush()
    try:
        print(line[:200], flush=True)     # ### the console shows progress; the LOG is the record
    except Exception:
        pass


def run(fh, args, cwd, label):
    say(fh, '### ### **BEGIN %s** : %s' % (label, ' '.join(args)))
    p = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding='utf-8', errors='replace', bufsize=1)
    for line in p.stdout:
        say(fh, line.rstrip())
    p.wait()
    say(fh, '### ### **END %s** : EXIT %d' % (label, p.returncode))
    return p.returncode


def main():
    if os.name == 'nt':
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(TITLE)
        except Exception:
            pass
    with io.open(LOG, 'a', encoding='utf-8', newline=NL) as fh:
        say(fh, '=' * 96)
        say(fh, 'b498 -- THE BUILD OF SIDE-explicit-formula, IN ITS OWN CONSOLE. ### NOT READ IN b498.')
        say(fh, 'kernel : %s' % KERNEL)
        say(fh, 'pid    : %d' % os.getpid())
        say(fh, 'title  : %s' % TITLE)
        say(fh, 'LEAN_NUM_THREADS : %s' % os.environ.get('LEAN_NUM_THREADS', '(not set)'))
        say(fh, '### ### **EACH LINE BELOW CARRIES AN INSTANT TAKEN AT THAT LINE** -- b480 repaired.')
        say(fh, '=' * 96)

        rc = run(fh, ['lake', 'build'], KERNEL, 'lake build')

        # ### ### **THE PROFILE IS RUN WHETHER OR NOT THE BUILD EXITED 0.**
        io.open(PROBE, 'w', encoding='utf-8', newline=NL).write(
            'import Zeta23.WeilEF.Main' + NL + NL
            + NL.join('#print axioms %s' % n for n in NAMES) + NL)
        say(fh, '### the probe lives in `relay/data/`, NOT in the kernel.')
        rc2 = run(fh, ['lake', 'env', 'lean', PROBE], KERNEL, 'PrintAxioms on the three names')

        say(fh, '### ### **BUILD EXIT %d ; PROFILE EXIT %d. ### THIS LOG IS THE NEXT ACT`S TO READ.**'
            % (rc, rc2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
