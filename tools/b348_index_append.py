# -*- coding: utf-8 -*-
"""b348_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTEXPLAINED`.** ### A reader who asks *what does the fold settle*
### must be handed: a fold PROVES NOTHING and moves no grade; the rate axis resolves the two CONVENTIONS and does NOT
### make one correct; the floor is NOT explained; the trail STAYS OWED; the census is a measurement OF the record and
### the gate is PROSPECTIVE; the minted species is a JUDGEMENT RULE and is not enforced; and the failure-mode
### partition is NAMED AND NOT OPENED, with no such partition known to exist. ### **`the fold proves it`, `the
### convention is correct`, `the partition is opened` AND `the census clears the record` STAY UNKEYED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORR = io.open(os.path.join(D, 'b348_corr_run.txt'), encoding='utf-8').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
F = json.load(io.open(os.path.join(D, 'b348_fold.json'), encoding='utf-8'))
C = F['census']

Q = chr(34)
BS = chr(92)
APOS = BS + "'"


def s(x):
    return str(x)


KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'priced-and-resolved-fold': ['the fold b339', 'the priced-and-resolved arc', 'the arc as one statement',\n"
    "                                'use and mention', 'the scanner over prose', 'the census as a finding',\n"
    "                                'the failure-mode partition', 'the judgement rule'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")

ROW_NEW = (
    "    # ### THE PRICED-AND-RESOLVED ARC, b339-b347 -- THE FOLD (b348).\n"
    "    (" + Q + "priced-and-resolved-fold" + Q + ", " + Q + "b348 (a filings act; it proves nothing and moves no grade)" + Q + ",\n"
    "     " + Q + "THE FOLD OF b339-b347: nine acts filed as one section of the findings document, PURELY ADDITIVE, with every quotation located at the act that ORIGINATED" + Q + "\n"
    "     " + Q + " it and -- new in this fold -- THE NO-GRADE-MOVED CLAIM ITSELF MECHANICAL: every grade string had to appear verbatim in the bank of the act it is" + Q + "\n"
    "     " + Q + " attributed to, or the section would not have been written. Quotations failing " + s(F['quotes_failing']) + "; grade anchors failing " + s(F['grades_failing']) + "; " + s(F['lines_added']) + " lines added, nothing" + Q + "\n"
    "     " + Q + " edited. Three further tables from the acts" + APOS + " own declarations: " + s(F['corrections']) + " corrections the acts made to their OWN readings, " + s(F['defective']) + " sealed bars found" + Q + "\n"
    "     " + Q + " defective and tabled rather than edited into passing, " + s(F['seat_defects']) + " defects the seats declared on their own faces. THE ARC AS ONE STATEMENT: a question" + Q + "\n"
    "     " + Q + " priced UNAFFORDABLE by value on one axis was RESOLVED on another the record already held; the deposit" + APOS + "s Li channel and the derived kernel are ONE" + Q + "\n"
    "     " + Q + " DISTRIBUTION ON TWO FAMILIES, measured; the archimedean instrument has a floor the one axis moved does not explain; the room" + APOS + "s minimum is BRACKETED at" + Q + "\n"
    "     " + Q + " the lowest height charted; the clause" + APOS + "s constituents stand as the stated-clause anchor has them. ONE SPECIES MINTED: a scanner over prose cannot tell" + Q + "\n"
    "     " + Q + " use from mention -- a sentence denying a thing contains the thing -- five incidents at b316, b317, b345, b346 and b347" + APOS + "s own arm which found its own" + Q + "\n"
    "     " + Q + " search string. THE CENSUS AS A FINDING: " + C['gated'] + " registrations gated, " + C['fire'] + " would fire, " + C['clear'] + " clear, " + C['nothing'] + " of those carrying nothing for an arm to look at." + Q + ",\n"
    "     " + Q + "### A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES: it proves nothing, discharges nothing, and MOVES NO GRADE -- and in this fold that is CHECKED" + Q + "\n"
    "     " + Q + " rather than asserted. ### THE RATE AXIS RESOLVES THE TWO CONVENTIONS AND DOES NOT MAKE A CONVENTION CORRECT; b313" + APOS + "s clause governs and a rate is not a" + Q + "\n"
    "     " + Q + " vote on it. ### THE FLOOR IS NOT EXPLAINED -- one axis of three was moved and the other two are named, not moved. ### W-ORD-LI-FAMILY-CONTROL STAYS" + Q + "\n"
    "     " + Q + " OWED: the zero side and the finite side are not evaluated. ### THE CENSUS IS A MEASUREMENT OF THE RECORD AND NOT A GRADE ON IT, and the gate it reports" + Q + "\n"
    "     " + Q + " is PROSPECTIVE -- the record" + APOS + "s quiet is mostly the absence of stated numerical bars, not bars checked and approved. ### THE MINTED SPECIES IS A" + Q + "\n"
    "     " + Q + " JUDGEMENT RULE, NOT MECHANIZED, and is deliberately NOT LISTED BESIDE THE MECHANIZED ONES; what would mechanize it is named and not built. ### THE" + Q + "\n"
    "     " + Q + " FAILURE-MODE PARTITION IS NAMED AS A RESEARCH PROPOSAL AND NOT OPENED, AND NO SUCH PARTITION IS KNOWN TO EXIST. ### K8 UNOWNED. ### NO GRADE MOVED." + Q + "\n"
    "     " + Q + " ### NO TERMINAL. ### M-2 UNCHANGED" + Q + ",\n"
    "     " + Q + "data/b348_the_fold.txt; data/b348_fold_run.txt; data/b348_fold_emitted.md;" + Q + "\n"
    "     " + Q + " data/b348_registration_2026-09-07.txt (sealed before any line was emitted into the findings document);" + Q + "\n"
    "     " + Q + " PLACE-papers FINDINGS.md (the appended section); TECHNE-Core modules/2026-09/USE_AND_MENTION.md (local, NOT PUSHED);" + Q + "\n"
    "     " + Q + " CORRESPONDENCE.md row " + R1 + Q + "),\n"
)

ALIASES = ('the fold b339', 'the priced-and-resolved arc', 'the arc as one statement', 'use and mention',
           'the scanner over prose', 'the census as a finding', 'the failure-mode partition', 'the judgement rule')
MUST_NOT_HIT = ('the fold proves it', 'the convention is correct', 'the partition is opened',
                'the census clears the record')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print("b348 -- THE INDEX KEY. ### THE PRICED-AND-RESOLVED ARC, FOLDED.")
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-38s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'priced-and-resolved-fold'" in txt)
    have_row = ('"priced-and-resolved-fold"' in txt)
    print('  priced-and-resolved-fold key/row already present : %s / %s' % (have_key, have_row))
    written = not (have_key and have_row)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if written:
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
    else:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    ok = True
    out, rc = query('priced-and-resolved-fold')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : priced-and-resolved-fold returns %d row(s), 1 required  %s' % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'priced-and-resolved-fold' in o
        ok = ok and g
        print('    %-44s reaches the b348 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTEXPLAINED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES' in out and 'DOES NOT MAKE A CONVENTION CORRECT' in out
    a2 = 'THE FLOOR IS NOT EXPLAINED' in out and 'STAYS' in out and 'OWED' in out
    a3 = 'NOT A GRADE ON IT' in out and 'JUDGEMENT RULE, NOT MECHANIZED' in out
    a4 = 'NOT OPENED, AND NO SUCH PARTITION IS KNOWN TO EXIST' in out and 'NO GRADE MOVED' in out
    ok = ok and a1 and a2 and a3 and a4
    print('    the answer says a fold moves no grade, and no convention is made correct : %s' % a1)
    print('    ### and the floor is not explained, and the trail stays owed              : %s' % a2)
    print('    ### and the census is not a grade, and the rule is not mechanized         : %s' % a3)
    print('    ### and the partition is not opened, and none is known to exist           : %s' % a4)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-38s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
