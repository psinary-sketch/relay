# -*- coding: utf-8 -*-
"""run_clock.py -- THE RUN FILE'S OWN CLOCK, built b347 by the author's order.

### ### **WHY THIS EXISTS.** ### b342's `G-ORDER` was declared a defective bar because the execution order of an act --
### the registration SEALED before any component ran -- could not be recovered after the fact. ### b344 repaired half
### of it: `reg_seal.py` now writes the seal's UTC instant into the seal block. ### **b345's `(E4)` FOUND THE OTHER
### HALF STILL OPEN, AND FOUND IT BY RUNNING ITS OWN SUITE TWICE:** before the push, file times carried the ordering;
### after it, the checkout had rewritten every mtime to within a fraction of a second and the arm could establish
### nothing. ### **A SEAL COULD BE DATED AND A COMPONENT COULD NOT, SO THE PAIR COULD NOT BE ORDERED.**
###
### ### **WHAT IT DOES.** ### It writes a run file with a header line carrying the instant it was written, in the seal
### block's own notation, and it takes the next number for its stem rather than overwriting a run that already exists.
###
### ### ### **THE REACH, STATED HERE SO THE TOOL IS NOT TRUSTED BEYOND IT:**
### ### ### **THE CLOCK IS OUTSIDE EVERYTHING THAT VERIFIES.** ### Nothing hashes it and nothing checks it against an
### ### independent source. ### It records when a run file was written ### BY A TOOL THAT MEANT TO RECORD IT. ### A
### ### seat that edits the line afterwards produces a consistent file, exactly as `reg_seal.py` says of its own clock.
### ### ### **AND IT RECOVERS NOTHING ABOUT ANY RUN FILE WRITTEN BEFORE IT, b345's `(E4)` INCLUDED. ### IT MAKES NO
### ### ### PAST ACT'S ORDERING CHECKABLE.** ### What it does is make the NEXT act's ordering checkable without
### ### depending on a file time that the next checkout will destroy.
###
### ### **WHY A HEADER LINE AND NOT A SIDECAR:** a sidecar can be lost, and a run file that has lost its clock looks
### exactly like one that never had it. ### **THE LINE TRAVELS WITH THE BYTES THAT ARE COMMITTED.**
"""
import datetime
import io
import os
import re
import sys

CLOCK = '### run at (UTC) : '
NOTE = '   ### NOT COVERED BY ANY HASH; it records when this run file was written.'
STAMP_RX = re.compile(r'^### run at \(UTC\) : (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', re.M)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def next_path(directory, stem, ext='.txt'):
    """### THE NUMBERING THE ACTS ALREADY USE, IN ONE PLACE. ### A second writing run to the same stem takes the next
    ### number; ### **NO RUN FILE IS EVER OVERWRITTEN BY THIS TOOL.**"""
    p, k = os.path.join(directory, stem + ext), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(directory, '%s%d%s' % (stem, k, ext))
    return p


def write(directory, stem, lines, ext='.txt'):
    """### WRITE `lines` to the next free path for `stem`, WITH THE CLOCK AS THE FIRST LINE. ### Returns the path."""
    p = next_path(directory, stem, ext)
    body = CLOCK + stamp() + NOTE + chr(10) + chr(10).join(lines) + chr(10)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
    return p


def read_stamp(path):
    """### THE CLOCK A RUN FILE CARRIES, or `None` if it carries none. ### **A RUN FILE WITHOUT A CLOCK IS NOT A
    ### FAILURE OF THIS TOOL -- IT IS EVERY RUN FILE WRITTEN BEFORE b347, AND THE CENSUS COUNTS THEM.**"""
    try:
        head = io.open(path, encoding='utf-8', errors='replace').read(400)
    except OSError:
        return None
    m = STAMP_RX.search(head)
    return m.group(1) if m else None


def self_test(verbose=True):
    """### THE FIXTURES, BOTH POLARITIES. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.**"""
    import tempfile
    d = tempfile.mkdtemp(prefix='run_clock_')
    ok = True

    def say(s):
        if verbose:
            print(s)

    # ### (1) a file written through the tool carries a parseable clock
    p1 = write(d, 'fixture', ['a line', 'another'])
    s1 = read_stamp(p1)
    a1 = s1 is not None and os.path.basename(p1) == 'fixture.txt'
    say('    (1) written through the tool carries a clock : %s (%s)  %s' % (bool(s1), s1, 'PASS' if a1 else '### FAIL ###'))
    ok = ok and a1
    # ### (2) THE OTHER POLARITY: a file written the old way carries none, and the reader says so
    p2 = os.path.join(d, 'oldstyle.txt')
    io.open(p2, 'w', encoding='utf-8', newline=chr(10)).write('a line' + chr(10))
    a2 = read_stamp(p2) is None
    say('    (2) written the OLD way carries none, and the reader says so : %s  %s' % (a2, 'PASS' if a2 else '### FAIL ###'))
    ok = ok and a2
    # ### (3) a second writing run takes the NEXT number and does not overwrite
    p3 = write(d, 'fixture', ['second run'])
    a3 = os.path.basename(p3) == 'fixture2.txt' and 'a line' in io.open(p1, encoding='utf-8').read()
    say('    (3) a second run takes the next number and the first survives : %s  %s' % (a3, 'PASS' if a3 else '### FAIL ###'))
    ok = ok and a3
    # ### (4) THE DISCRIMINATION ARM: a file whose clock line is MALFORMED reads as no clock, not as a clock
    p4 = os.path.join(d, 'malformed.txt')
    io.open(p4, 'w', encoding='utf-8', newline=chr(10)).write('### run at (UTC) : not-a-time' + chr(10))
    a4 = read_stamp(p4) is None
    say('    (4) a MALFORMED clock reads as no clock : %s  %s' % (a4, 'PASS' if a4 else '### FAIL ###'))
    ok = ok and a4
    for p in (p1, p2, p3, p4):
        try:
            os.remove(p)
        except OSError:
            pass
    try:
        os.rmdir(d)
    except OSError:
        pass
    return ok


def latest(directory, stem, ext='.txt'):
    """### THE NEWEST RUN OF A STEM, BY ITS OWN CLOCK -- NEVER BY MTIME. ### Added b407.

    ### ### **THE INCIDENT THAT BOUGHT IT.** ### `b406` read a dead run record THREE TIMES. ### This
    ### tool VERSIONS its output (`..._notes.txt`, `..._notes2.txt`, ...) and never overwrites, so a
    ### directory listing sorted by modification time handed the seat an OLDER file than the run
    ### that had just finished; it read `HARD FAILURE` from a dead record while the live run was
    ### passing, and repaired code that was already correct.
    ###
    ### ### **THE CURE IS THE STAMP THE WRITER HAS ALWAYS WRITTEN.** ### `write` puts the clock on
    ### the first line and `read_stamp` reads it back; only the LATEST-BY-STAMP reader was missing.
    ###
    ### ### **AND IT REFUSES RATHER THAN GUESSES.** ### If ANY candidate carries no clock, there is
    ### no total order to take a maximum of, and this returns `(None, None, reason)` -- because a
    ### reader that silently falls back to mtime is the defect, not the cure. ### **A GUARD THAT
    ### ### GUESSES WHEN IT CANNOT KNOW IS THE THING THAT WENT WRONG.**
    ###
    ### Returns `(path, stamp, note)`; `path` is `None` when it refuses, and `note` always says why.
    """
    if not os.path.isdir(directory):
        return None, None, 'no such directory: %s' % directory
    cands = []
    for f in sorted(os.listdir(directory)):
        if not f.endswith(ext):
            continue
        base = f[:-len(ext)]
        if base == stem or (base.startswith(stem) and base[len(stem):].isdigit()):
            cands.append(os.path.join(directory, f))
    if not cands:
        return None, None, 'no run file for stem %r' % stem
    stamped = [(read_stamp(c), c) for c in cands]
    missing = [c for s, c in stamped if s is None]
    if missing:
        return None, None, ('REFUSED -- %d of %d candidate(s) carry no clock: %s'
                            % (len(missing), len(cands),
                               [os.path.basename(m) for m in missing]))
    best = max(stamped)
    return best[1], best[0], ('newest of %d by its own clock' % len(cands))


def latest_self_test(verbose=True):
    """### THE GUARD'S OWN FIXTURES, BOTH POLARITIES. ### Added b407.

    ### ### **THE POSITIVE ARM MUST DISAGREE WITH MTIME OR IT PROVES NOTHING**: the fixture writes
    ### the stamp-newest record FIRST and then back-dates nothing, touching the OLDER file last so
    ### that a mtime reader would return the wrong one. ### **A FIXTURE THAT AGREES WITH THE DEFECT
    ### ### CANNOT CATCH IT.**
    """
    import tempfile
    import time
    d = tempfile.mkdtemp(prefix='run_clock_latest_')
    ok = True

    def say(s):
        if verbose:
            print(s)

    older = os.path.join(d, 'fx.txt')
    newer = os.path.join(d, 'fx2.txt')
    io.open(older, 'w', encoding='utf-8', newline=chr(10)).write(
        CLOCK + '2026-09-10T09:00:00Z' + NOTE + chr(10) + 'the older run' + chr(10))
    io.open(newer, 'w', encoding='utf-8', newline=chr(10)).write(
        CLOCK + '2026-09-10T17:00:00Z' + NOTE + chr(10) + 'the newer run' + chr(10))
    # ### **TOUCH THE OLDER ONE LAST**, so mtime and the clock DISAGREE.
    time.sleep(0.01)
    os.utime(older, None)
    by_mtime = max(cands_for(d), key=os.path.getmtime)
    p, s, note = latest(d, 'fx')
    a1 = (p == newer) and (s == '2026-09-10T17:00:00Z') and (by_mtime == older)
    say('    (5) returns the STAMP-newest while mtime says otherwise : %s  %s'
        % (a1, 'PASS' if a1 else '### FAIL ###'))
    say('        by clock : %s ; by mtime : %s'
        % (os.path.basename(p or '-'), os.path.basename(by_mtime)))
    ok = ok and a1
    # ### THE OTHER POLARITY: one unstamped candidate and it REFUSES.
    io.open(os.path.join(d, 'fx3.txt'), 'w', encoding='utf-8', newline=chr(10)).write('no clock')
    p2, s2, note2 = latest(d, 'fx')
    a2 = p2 is None and 'REFUSED' in note2
    say('    (6) REFUSES rather than guesses when a candidate has no clock : %s  %s'
        % (a2, 'PASS' if a2 else '### FAIL ###'))
    say('        %s' % note2)
    ok = ok and a2
    for f in os.listdir(d):
        try:
            os.remove(os.path.join(d, f))
        except OSError:
            pass
    try:
        os.rmdir(d)
    except OSError:
        pass
    return ok


def cands_for(directory, ext='.txt'):
    """### The fixture's own mtime view, so the two orders can be printed side by side."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(ext)]

if __name__ == '__main__':
    print('run_clock.py -- self-test:')
    sys.exit(0 if self_test() else 1)
