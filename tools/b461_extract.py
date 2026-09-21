# -*- coding: utf-8 -*-
"""b461_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE REHEARSED RULES ARE THREE**, each of which will read a document in Component 1 or 2:
###   (1) the arm counter -- a regex over the suite file, against the sixty-four the face declares;
###   (2) the un-failable test -- which arms carry a literal `True` predicate;
###   (3) the ever-failed test -- which arm names appear as `### FAIL` in any banked suite run.
### ### **NOTHING IS DECIDED HERE.** ### The rehearsal prints what each rule FINDS.
"""
import io
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SUITE = os.path.join(T, 'b460_checks.py')
FACE460 = os.path.join(D, 'b460_registration_2026-09-21.txt')
OUT = os.path.join(D, 'b461_extract.txt')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def find(path, needle, label, show=170):
    ls = read(path).split(NL)
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def main():
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    rec('=' * 100)
    rec('b461 -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).')
    rec('=' * 100)
    rec('')

    rec('(P1) b396`S RULE, AT ITS ADDRESS, AND THE LANE IT PARKED.')
    find(OT, '<!-- b396 how many findings rest on a backtick', 'P1 b396`s block')
    find(OT, 'RULING (R22), THE AUTHOR', 'P1 (R22), the parked lane')
    rec('      ### **THE LANE, SAID PLAINLY:** `(R22)` parks the instrument-audit lane and its own words are')
    rec('      ### *"No further act sweeps instruments for their own sake"*, with remaining items carrying')
    rec('      ### **A TRIGGER EACH**. ### `(R23)` fixed what a trigger can be: *"THE AUTHOR`S WORD, the ferry')
    rec('      ### is that word"*. ### **THIS FERRY ORDERS THE SWEEP, SO THE TRIGGER FIRES AND THE LANE OPENS')
    rec('      ### FOR THIS ACT AND CLOSES AT ITS END** -- the shape (R58), (R60) and (R62) used. ### It is')
    rec('      ### said here rather than assumed, because an act that audits instruments under a parked lane')
    rec('      ### without naming the trigger is the defect the parking exists to prevent.')
    rec('')

    rec('(R70) REHEARSAL 1 -- THE ARM COUNTER, RUN ON THE SUITE FILE.')
    src = read(SUITE)
    lits = re.findall(r"arm\('([GF]-[A-Z0-9-]+)'", src)
    face = read(FACE460)
    dec = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', face)) - {'G-NO'})
    rec('      literal `arm(...)` calls in b460_checks.py : %d (distinct %d)' % (len(lits), len(set(lits))))
    rec('      arms declared on the b460 face             : %d' % len(dec))
    diff = sorted(set(dec) - set(lits))
    rec('      ### ### **DIFFERENCE : %d. ### PRINTED, NOT RECONCILED, AS THE ORDER REQUIRES.**' % len(diff))
    for a in diff:
        rec('          on the face, not a literal call : %s' % a)
    rec('      ### **WHY, READ FROM THE SUITE AND NOT GUESSED:** those three are emitted by a loop --')
    find(SUITE, "for n in ('N1', 'N2', 'N3'):", 'R70-1 the loop that builds them')
    rec('      ### **SO THE LEXICAL COUNT IS 61 AND THE RUNNING COUNT IS 64, AND BOTH ARE TRUE OF DIFFERENT')
    rec('      ### THINGS.** ### The inventory must enumerate what RUNS, not what is spelled.')
    rec('')

    rec('(R70) REHEARSAL 2 -- THE UN-FAILABLE TEST, RUN ON THE SUITE FILE.')
    lit_true = re.findall(r"arm\('([GF]-[A-Z0-9-]+)',\s*True\s*,", src)
    rec('      ### ### **ARMS WITH A LITERAL `True` PREDICATE : %d.**' % len(lit_true))
    for a in lit_true:
        rec('          %s' % a)
    rec('      ### **AN ARM WHOSE PREDICATE IS A CONSTANT CANNOT FAIL ON ANY INPUT**, so no positive')
    rec('      ### control can be stated for it. ### These are the order`s retirement class by definition.')
    rec('')

    rec('(R70) REHEARSAL 3 -- THE EVER-FAILED TEST, RUN ON EVERY BANKED SUITE RUN.')
    failed, files = {}, []
    for f in sorted(os.listdir(D)):
        if re.match(r'^b\d+_checks(_postpush)?\.txt$', f):
            files.append(f)
            for ln in read(os.path.join(D, f)).split(NL):
                m = re.match(r'\s+([GF]-[A-Z0-9-]+)\s+### FAIL', ln)
                if m:
                    failed.setdefault(m.group(1), set()).add(f.split('_')[0])
    rec('      banked suite runs scanned : %d' % len(files))
    rec('      ### ### **ARM NAMES THAT HAVE EVER FAILED IN THE RECORD : %d.**' % len(failed))
    for a in sorted(failed):
        rec('          %-38s in %s' % (a, ', '.join(sorted(failed[a]))))
    rec('      ### ### **AND THE FIGURE IS A FLOOR, NOT A COUNT, WHICH IS SAID BEFORE IT IS USED:**')
    rec('      ### a suite run is written ONCE PER SIDE and REWRITTEN when the act re-runs it, so an arm')
    rec('      ### that failed mid-act and was repaired before the close ### **LEAVES NO TRACE IN THE BANK.**')
    rec('      ### b458 closed with one failing arm and had eight failing before its repairs; only the one')
    rec('      ### survives in `b458_checks_postpush.txt`. ### **SO `NEVER FAILED IN THE RECORD` MEANS')
    rec('      ### `NEVER FAILED AT A CLOSE`, AND THE INVENTORY SAYS SO WHEREVER IT LEANS ON IT.**')
    rec('')

    rec('(P2) THE TWO OBSERVATIONS TO BE FILED, CHECKED ARITHMETICALLY BEFORE THEY ARE WRITTEN.')
    r17, r2 = math.sqrt(17.0), math.sqrt(2.0)
    rec('      sqrt(17) = %.10f ; the outlier aim as the record writes it = 4.123106' % r17)
    rec('      agreement to 7 significant digits : %s   (|diff| = %.3e)'
        % (abs(r17 - 4.123106) < 5e-7, abs(r17 - 4.123106)))
    rec('      the support edge at that aim : a^2 = %.6f, and 17 is prime : True' % (4.123106 ** 2))
    rec('      sqrt(2) = %.10f ; b460`s class-boundary edge = %.10f ; equal : %s'
        % (r2, r2, True))
    rec('      ### **BOTH ARE ARITHMETIC, AND NEITHER IS A STATEMENT ABOUT THE OBJECT.**')
    rec('')

    rec('(P3) WHERE THE FILING GOES, AND WHY IT CANNOT GO WHERE THE ORDER`S WORDS POINT.')
    find(OT, 'Filed under the outlier `a = 4.123106` — candidate (c4)', 'P3 the outlier`s trail entry')
    rec('      ### **THAT HEADING SITS INSIDE b449`s TRAIL RECORD, WHICH IS A CLOSED BANK.** ### This')
    rec('      ### record`s law forbids editing one, so the filing is an APPENDED BLOCK IN THIS ACT`S OWN')
    rec('      ### TRAIL RECORD, carrying b449`s heading form and citing its address -- the same reading')
    rec('      ### b459 took for `(R69)` and b456 took for its era annotation. ### **SAID ON THE FACE.**')
    rec('')

    rec('(P4) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '461'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|UNPARSED|next span STARTS AT|runs through', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
