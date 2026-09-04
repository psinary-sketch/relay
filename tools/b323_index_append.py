# -*- coding: utf-8 -*-
"""b323_index_append.py -- ONE KEY, TWO ROWS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ALIASES ARE CHOSEN TO AVOID A COLLISION, AND THE COLLISION WAS MEASURED FIRST.** ###
### `the fold` and `the lore` ALREADY resolve -- to `m2-arc-fold` and to the b297-b306 fold's key.
### ### **A FOLD THAT CLAIMED THEM WOULD SILENTLY REDIRECT EVERY QUERY ABOUT AN EARLIER ARC TO THIS
### ### ONE**, so this act takes `the archimedean arc fold`, `b314-b322`, `the instrument arc` and
### `the defective bars` and leaves the two generic aliases where they are.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCONCLUDED`.** ### A reader who asks about the
### arc must be handed, in the same breath, that ### **A FOLD IS A FILING AND NOT A CONCLUSION** ###
### -- no grade moved, no theorem proved by any act in it, and the SIZE of no margin on the domain
### axis certified anywhere.
### ### **`the archimedean membership` STAYS UNKEYED.** ### b321 and b322 both left it so, and a
### fold that claimed it would be filing a verdict nobody reached.
### ### **THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NL = chr(10)

KEY_ANCHOR = "KEYS = {\n"
KEY_NEW = (
    "    'archimedean-arc-fold': ['the archimedean arc fold', 'b314-b322',\n"
    "                             'the instrument arc', 'the nine acts',\n"
    "                             'the defective bars', 'sealed bars found defective',\n"
    "                             'what did the arc establish'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE FOLD ITSELF (b323).\n"
    "    (\"archimedean-arc-fold\", \"b323 (a filings act; nine acts into one section)\",\n"
    "     \"b314 through b322 folded into `FINDINGS.md` as THE ARCHIMEDEAN INSTRUMENT ARC --\"\n"
    "     \" **+154 lines, its sixteenth section, 2709 to 2863 lines**. ### Each entry carries its\"\n"
    "     \" grade AS ITS OWN ACT LEFT IT, its own scope sentence, and an obstacle quoted verbatim\"\n"
    "     \" and verified against the act that ORIGINATED it. ### **THE GATE IS A GENERATOR AND NOT\"\n"
    "     \" A REVIEWER**: a quotation that fails F-QUOTE never reaches the file at all, and\"\n"
    "     \" F-QUOTE carries a DISCRIMINATION arm -- an altered quotation comes back UNFINDABLE.\"\n"
    "     \" ### F-QUOTE 18 of 18; F-COUNT 9 results, 9 obstacles, the arc exactly. ### **THE WRITE\"\n"
    "     \" IS PURELY ADDITIVE AND THAT IS MEASURED**: the pre-append working file AND the blob at\"\n"
    "     \" HEAD are both TRUE BYTE PREFIXES of the result\",\n"
    "     \"### A FOLD IS A FILING AND NOT A CONCLUSION. ### **NO GRADE MOVES. ### NO ACT IS\"\n"
    "     \" RE-VERDICTED. ### NO NEW MATHEMATICS** -- every number in the section was already\"\n"
    "     \" banked by the act that owns it. ### The arc's one statement is filed WITH ITS SCOPE\"\n"
    "     \" PRINTED BESIDE IT: **no theorem is proved by any act in it**, the window decides\"\n"
    "     \" nothing, and **the SIZE of no margin on the domain axis is certified anywhere in the\"\n"
    "     \" arc**. ### W-ORD-ARCH-MEMBERSHIP, W-ORD-PHI-MU-L2 and W-ORD-WINDOW-CLASS all stay\"\n"
    "     \" OPEN. ### Three defects in this act's OWN generator are declared: a missing idempotence\"\n"
    "     \" guard that filed the arc twice before any commit, a sentence asserting a difference its\"\n"
    "     \" own measurement showed was zero, and a log list the runner could not write. ### NO\"\n"
    "     \" AGGREGATION IS STATED. ### M-2 UNCHANGED\",\n"
    "     \"data/b323_the_fold.txt; data/b323_fold_run.txt; data/b323_fold_emitted.md;\"\n"
    "     \" PLACE-papers/FINDINGS.md (the filed section); CORRESPONDENCE.md row 158\"),\n"
    "    # ### THE DEFECTIVE-BARS TABLE (b323).\n"
    "    (\"archimedean-arc-fold\", \"b323 (the table this record had never filed before)\",\n"
    "     \"**THREE TIMES IN NINE ACTS A BAR WAS SEALED BEFORE ANY VALUE AND THE BAR ITSELF TURNED\"\n"
    "     \" OUT WRONG.** ### b319's (B3) reach bar required the rank constant on BOTH axes when the\"\n"
    "     \" domain axis cannot deliver it; b322's (B2) imported two labels that do not partition\"\n"
    "     \" the possibilities; b322's (B5) has branches that are not mutually exclusive and fired\"\n"
    "     \" twice at once. ### **IN NO CASE WAS THE SEALED FILE EDITED.** ### And in all three the\"\n"
    "     \" defect was found **by running the sealed bar and reading what came back**, not by\"\n"
    "     \" revising it: b319 reported an EMPTY reach under a bar it had shown unsatisfiable and\"\n"
    "     \" left the fix as a PROPOSAL; b322 reported the verdict its broken rule computed and then\"\n"
    "     \" TOOK THE WEAKER of the two branches that rule licensed\",\n"
    "     \"### A TABLE OF ONE'S OWN DEFECTS IS NOT A RESULT EITHER. ### **A DEFECT NAMED IN A\"\n"
    "     \" SEALED BAR IS EVIDENCE; A SEALED BAR QUIETLY REWRITTEN IS NOT**, and a record whose\"\n"
    "     \" registrations are only ever reported as having worked is a record that has stopped\"\n"
    "     \" reading them. ### The lore is consolidated with its incidents and SPLIT BY WHAT\"\n"
    "     \" ENFORCES IT: nine rules MECHANIZED, five JUDGEMENT. ### The suite is inventoried at ten\"\n"
    "     \" pieces. ### The archimedean instrument's three certifications are tabled with their\"\n"
    "     \" cells and margins, and **its limits are stated as measurements**: the domain axis's\"\n"
    "     \" rate on both ladders, and a resolving power priced twice, both prices beyond what it\"\n"
    "     \" reaches. ### NO GRADE MOVED. ### M-2 UNCHANGED\",\n"
    "     \"data/b323_the_fold.txt; data/b323_fold_rows.json;\"\n"
    "     \" data/b319_the_stable_rank.txt and data/b322_the_membership.txt (the originating acts);\"\n"
    "     \" CORRESPONDENCE.md row 159\"),\n"
)

NEW_KEYS = ('archimedean-arc-fold',)
ALIASES = ('the archimedean arc fold', 'b314-b322', 'the instrument arc', 'the nine acts',
           'the defective bars', 'sealed bars found defective', 'what did the arc establish')
MUST_NOT_HIT = ('the archimedean membership', 'the window class')


def no_key(out):
    for ln in (out or '').splitlines():
        if ln.strip().startswith('### NO KEY'):
            return True
    return False


def verdict_fixture():
    real = no_key('=====' + NL + '  ### NO KEY.' + NL + '  ### matched no DECLARED key')
    quoted = no_key('    grade    : ... every query that would have found b268 returned NO KEY.')
    return real, quoted


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b323 -- THE INDEX KEY. ### THE ARCHIMEDEAN ARC FOLD.')
    print('=' * 100)
    print('  ### THE COLLISION, MEASURED BEFORE THE ALIASES WERE CHOSEN:')
    for q in ('the fold', 'the lore'):
        out, _rc = query(q)
        print('    %-28s already resolves : %s  ### NOT CLAIMED BY THIS ACT'
              % (q, not no_key(out)))
    print('    ### **A FOLD THAT CLAIMED THEM WOULD SILENTLY REDIRECT EVERY QUERY ABOUT AN EARLIER')
    print('    ### ### ARC TO THIS ONE.**')

    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-36s NO KEY before : %s' % (q, pre[q]))

    have_key = {k: ("'%s'" % k) in txt for k in NEW_KEYS}
    have_row = {k: ('"%s"' % k) in txt for k in NEW_KEYS}
    for k in NEW_KEYS:
        print('  %-24s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
    written = not (all(have_key.values()) and all(have_row.values()))
    if not written:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2

    if written:
        new = txt
        if not all(have_key.values()):
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not all(have_row.values()):
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)

    rv, qv = verdict_fixture()
    print('  VERDICT FIXTURE : fires on the index\'s own NO KEY line : %s ;'
          ' quiet on the phrase quoted inside a row : %s' % (rv, not qv))
    ok = rv and not qv

    print('  ### READ BACK BY QUERYING THE INDEX ITSELF:')
    for k in NEW_KEYS:
        out, rc = query(k)
        good = (not no_key(out)) and (k in out) and rc == 0
        both = out.count('act      :') >= 2
        ok = ok and good and both
        print('    %-24s returns a row : %s ; returns BOTH rows : %s  %s'
              % (k, good, both, 'PASS' if (good and both) else '### FAIL ###'))
    print('  ### **BOTH ROWS ARE REQUIRED.** ### An index that handed back the filing without the')
    print('  ### defective-bars table would be answering *what was filed* and hiding *what the')
    print('  ### filing had to admit*.')

    print('  ### THE ALIASES:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-42s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### ### **G-NOTCONCLUDED -- THE ARM THIS FILE EXISTS FOR.**')
    out, _rc = query('what did the arc establish')
    filing = 'A FOLD IS A FILING AND NOT A CONCLUSION' in out
    notheorem = 'no theorem is proved by any act in it' in out
    nosize = 'SIZE of no margin on the domain axis is certified' in out
    ok = ok and filing and notheorem and nosize
    print('    the answer says a fold is a filing, not a conclusion : %s' % filing)
    print('    ### and that no theorem is proved by any act in the arc : %s' % notheorem)
    print('    ### and that no margin SIZE is certified anywhere       : %s' % nosize)

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-36s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the archimedean membership` STAYS UNKEYED: A FOLD THAT CLAIMED IT WOULD BE')
    print('  ### ### FILING A VERDICT NOBODY REACHED.**')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE : %d stem hit(s)' % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
