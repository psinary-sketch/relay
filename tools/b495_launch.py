# -*- coding: utf-8 -*-
"""b495_launch.py -- THE DETACHED BUILD LAUNCHER. ### **b480'S TIMESTAMP DEFECT REPAIRED.**

### b480's launcher computed its timestamp ONCE and stamped every module mark with it, so a log
### that looked like a progress record carried ### **ONE INSTANT REPEATED** and could not say how
### long anything took or in what order it happened. ### ### **THE INSTANT IS TAKEN AT THE MARK**,
### here, per line, from the clock -- never precomputed, never reused.
###
### This module is the child process. ### It is launched detached and it is NOT imported by the
### act's own tools; `b495_push.py` spawns it and returns.
"""
import io
import os
import subprocess
import sys
import time

KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LOG = os.path.join(D, 'b495_ef_build.log')
NAMES = ('Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'Zeta23.EF.EF_lit', 'Zeta23.WeilEF.EF_lit_zeta')
NL = chr(10)


def stamp():
    """### ### **THE CLOCK IS READ HERE, AT THE MARK.** ### Not at import, not at launch, not once
    ### per run. ### b480's log carried a single instant on every line for exactly that reason."""
    t = time.time()
    return '%s.%03d' % (time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(t)), int((t % 1) * 1000))


def say(fh, s):
    fh.write('%s  %s%s' % (stamp(), s, NL))
    fh.flush()


def run(fh, args, cwd, label):
    say(fh, '### ### **BEGIN %s** : %s' % (label, ' '.join(args)))
    p = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding='utf-8', errors='replace', bufsize=1)
    for line in p.stdout:
        # ### ### **EVERY LINE IS STAMPED FROM THE CLOCK AS IT ARRIVES.**
        say(fh, line.rstrip())
    p.wait()
    say(fh, '### ### **END %s** : EXIT %d' % (label, p.returncode))
    return p.returncode


def main():
    with io.open(LOG, 'a', encoding='utf-8', newline=NL) as fh:
        say(fh, '=' * 96)
        say(fh, 'b495 -- THE DETACHED BUILD OF SIDE-explicit-formula. ### THE LOG IS NOT READ IN b495.')
        say(fh, 'kernel : %s' % KERNEL)
        say(fh, 'pid    : %d' % os.getpid())
        say(fh, '### ### **EACH LINE BELOW CARRIES AN INSTANT TAKEN AT THAT LINE** -- b480 repaired.')
        say(fh, '=' * 96)

        rc = run(fh, ['lake', 'build'], KERNEL, 'lake build')

        # ### ### **THE PROFILE IS RUN WHETHER OR NOT THE BUILD EXITED 0.**
        # ### A partial build still profiles what it has, and ### **A LAUNCHER THAT SKIPS THE
        # ### PROFILE ON A NON-ZERO EXIT HANDS THE NEXT ACT NOTHING TO READ.**
        probe = os.path.join(D, 'b495_printaxioms.lean')
        io.open(probe, 'w', encoding='utf-8', newline=NL).write(
            'import Zeta23.WeilEF.Main' + NL + NL
            + NL.join('#print axioms %s' % n for n in NAMES) + NL)
        say(fh, '### the probe lives in `relay/data/`, NOT in the kernel: the kernel`s own file')
        say(fh, '### list is what the face declares, and a probe is this act`s file, not its.')
        rc2 = run(fh, ['lake', 'env', 'lean', probe], KERNEL, 'PrintAxioms on the three names')

        say(fh, '### ### **BUILD EXIT %d ; PROFILE EXIT %d. ### THIS LOG IS b496`S TO READ.**'
            % (rc, rc2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
