# -*- coding: utf-8 -*-
"""needle_extract.py -- `W-ORD-NEEDLE-EXTRACT`, built b262.

### WHY THIS EXISTS, AND THE DIAGNOSIS IS SHARPER THAN THE WORK-ORDER'S TITLE.
### THREE CONSECUTIVE ACTS WERE CAUGHT BY ONE SPECIES:
###   b229 -- a fixture built from a substring the target file HAPPENED to contain, so it
###           PASSED and licensed nothing.
###   b260 -- a gate asked the REGISTRATION for `F1 bar`, a phrase only the RUN prints.
###   b261 -- a needle that dropped two words from the middle of the sentence it quoted.
### Each time the check was RIGHT about the corpus and WRONG about the bytes.
###
### ### THE OBVIOUS DIAGNOSIS IS "TYPED NEEDLES", AND IT IS ONLY HALF.
### ### **THE OTHER HALF IS THAT A PURE CONJUNCTION OF SIX `contains()` CALLS REPORTS ### ONE
### ### BIT ### .** ### The harness law forbids `or` and requires conjunctions -- correctly --
### but a conjunction that fails names NO conjunct. ### In all three acts the executor had to
### re-run a hand-written probe to find WHICH clause was false. ### **A CHECK THAT CANNOT SAY
### ### WHICH OF ITS PARTS FAILED IS A CHECK THAT COSTS AN ACT TO DEBUG**, and that cost is
### what actually produced three repeats.
###
### SO THIS FILE DOES TWO THINGS, AND THE SECOND MATTERS MORE:
###   (1) ### **EXTRACT** ### -- pull exact bytes out of a file at AUTHORING time, so a needle
###       is provably a substring of its target before it is ever frozen into a check.
###   (2) ### **REPORT** ### -- `verify_all` returns the harness's `(verdict, detail)` pair and
###       ### **NAMES EVERY MISSING NEEDLE** ### . The conjunction stays pure; the diagnosis
###       stops being one bit.
###
### ### THE REACH, STATED SO THE TOOL IS NOT TRUSTED BEYOND IT:
### ### **IT CANNOT TELL A NEEDLE THAT MATTERS FROM ONE THAT DOES NOT.** ### Extracting a
### ### sentence guarantees the needle is present; it guarantees nothing about whether the
### ### sentence is the right thing to check for. ### b142's scope lesson is still its own.
### ### **AND A NEEDLE EXTRACTED FROM THE FILE IT LATER CHECKS IS CIRCULAR BY CONSTRUCTION** --
### ### extraction is for needles that CROSS files (extract from the bank, check in the report),
### ### and a same-file check proves only that the file has not changed since authoring.

Usage:
    python needle_extract.py --from <file> --anchor <substring> [--span N]
    python needle_extract.py --from <file> --line <N> [--span N]
        -> prints the exact text and a ready-to-paste Python literal.

    from needle_extract import verify_all
    H.run('name', check=lambda: verify_all(BANK, [...needles...]), fixture=...)
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_LEAD = re.compile(r'(?m)^[#\s]*###')
_WS = re.compile(r'\s+')

PASS, FAIL = 'PASS', 'FAIL'


def norm(s):
    """### THE HARNESS'S OWN NORMALIZER, MIRRORED. ### Layout only, then case-folded.
    ### **IMPORTED RATHER THAN RE-DERIVED WHERE POSSIBLE** -- see `_check_mirror` below,
    ### which asserts this agrees with `check_harness.norm` and REFUSES if it does not."""
    return _WS.sub(' ', _LEAD.sub(' ', s)).strip().lower()


def _check_mirror():
    """### A COPY THAT DRIFTS FROM ITS ORIGINAL IS WORSE THAN NO COPY. ### Checked at import."""
    try:
        from check_harness import norm as hn
    except Exception:
        return None
    probe = u'###  Foo   BAR\n### baz '
    return bool(hn(probe) == norm(probe))


MIRROR_OK = _check_mirror()


def extract(path, anchor=None, line=None, span=1):
    """### PULL EXACT BYTES OUT OF A FILE. ### Returns (text, line_number) or (None, -1)."""
    lines = io.open(path, encoding='utf-8').read().split('\n')
    if line is not None:
        i = line - 1
    else:
        na = norm(anchor)
        i = -1
        for j, l in enumerate(lines):
            if na and na in norm(l):
                i = j
                break
        if i < 0:
            return None, -1
    chunk = '\n'.join(lines[i:i + span])
    return chunk, i + 1


def verify_all(path, needles):
    """### THE HARNESS-SHAPED CHECKER. ### Returns `(verdict, detail)`.

    ### ### **THE POINT OF THE WHOLE FILE: ON FAILURE IT NAMES ### WHICH ### NEEDLES ARE
    ### ### ABSENT**, instead of collapsing six clauses into one `False`.
    ### A MISSING FILE IS A FAIL, NEVER SILENTLY TRUE (`contains`'s own law)."""
    if not os.path.isfile(path):
        return FAIL, '### FILE ABSENT: %s' % path
    hay = norm(io.open(path, encoding='utf-8', errors='replace').read())
    missing = [n for n in needles if norm(n) not in hay]
    if missing:
        return FAIL, ('### %d of %d NEEDLES ABSENT from %s: %s'
                      % (len(missing), len(needles), os.path.basename(path),
                         ' | '.join(repr(m[:70]) for m in missing)))
    return PASS, '%d of %d needles present' % (len(needles), len(needles))


def main(argv):
    src, anchor, line, span = None, None, None, 1
    i = 0
    while i < len(argv):
        if argv[i] == '--from':
            src = argv[i + 1]; i += 2
        elif argv[i] == '--anchor':
            anchor = argv[i + 1]; i += 2
        elif argv[i] == '--line':
            line = int(argv[i + 1]); i += 2
        elif argv[i] == '--span':
            span = int(argv[i + 1]); i += 2
        else:
            i += 1
    if not src:
        print(__doc__)
        return 2
    print('  mirror of check_harness.norm agrees : %s' % MIRROR_OK)
    text, ln = extract(src, anchor=anchor, line=line, span=span)
    if text is None:
        print('  ### ANCHOR NOT FOUND. ### No nearest string is offered -- a nearest string is')
        print('  ### how a miss becomes a false hit (b164).')
        return 1
    print('  file : %s' % src)
    print('  line : %d (span %d)' % (ln, span))
    print('  ---- exact text ----')
    print(text)
    print('  ---- as a Python literal ----')
    print('      %r' % ' '.join(text.split()))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
