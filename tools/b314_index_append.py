# -*- coding: utf-8 -*-
"""b314_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER NAMES BOTH: ### *fold rows and cold-clone keyed*.**

### ### **THE MUST-NOT-HIT ARM IS b202's: ### `the kernel` AND `coverage` STAY UNKEYED.** ### The
### first is the object itself and this act certified a REBUILD of it, not a result about it; the
### second is a bare property, and ### **AN INDEX THAT ANSWERED `coverage` WOULD BE OFFERING A
### ### COUNT OF UNCERTIFIED TERMINALS AS THOUGH IT WERE A VERDICT ON WHAT THE KERNEL COVERS.**
### ### **AND `the fold` IS DELIBERATELY NOT IN THAT ARM: ### IT ALREADY HITS SOMETHING THIS ACT
### ### DID NOT PUT THERE**, and a must-not-hit arm over an already-hit query fails for somebody
### else's reason -- a control that reports the wrong act.
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
    "    'the-instrument-arc': ['the seven acts', 'b307 to b313',\n"
    "                    'the arc as one statement', 'the convention erratum'],\n"
    "    'the-cold-clone': ['the kernel rebuilt from a clone', 'the certification test',\n"
    "                    'uncertified terminals', 'the coverage answer'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE INSTRUMENT ARC FOLDED (b314).\n"
    "    (\"the-instrument-arc\", \"b314 (a filings act)\",\n"
    "     \"seven acts -- b307 through b313 -- filed into PLACE-papers/FINDINGS.md as **THE\"\n"
    "     \" INSTRUMENT ARC, b307-b313 -- THE FOLD**. ### **14 QUOTATIONS, 0 UNFINDABLE, EVERY ONE\"\n"
    "     \" CHECKED AGAINST THE ACT THAT ORIGINATED IT BEFORE EMISSION**, with a discrimination\"\n"
    "     \" arm requiring an ALTERED quotation back unfindable. ### FINDINGS.md +100 / -0. ###\"\n"
    "     \" The arc as one statement: at a finite place the source's construction returns the test\"\n"
    "     \" function at one point times a dimension and carries no arithmetic; the mechanism\"\n"
    "     \" producing that silence DOES NOT TYPE at the archimedean place; and the corpus's\"\n"
    "     \" remainder is NOT the source's function, differing by a factor of rho whose correction\"\n"
    "     \" accounts for 8%% to 19%% of the residue and no more. ### The author's CONVENTION\"\n"
    "     \" ERRATUM ruling executed: ERRATA.md entry **E-2026-09-03-1**, internal record, +28 / -0\",\n"
    "     \"### A FILINGS ACT. ### **NO GRADE MOVES, NO ACT IS RE-VERDICTED, AND NOTHING IN THE\"\n"
    "     \" SECTION IS NEW MATHEMATICS.** ### Additivity MEASURED by `git diff --numstat`, not\"\n"
    "     \" asserted. ### Five falsifiers, all DID NOT FIRE. ### **THE OWNER INSTRUMENT FILES STAY\"\n"
    "     \" BYTE-IDENTICAL**, checked before and after the errata entry, on the E1 precedent:\"\n"
    "     \" THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF. ### The entry carries a standing\"\n"
    "     \" clause -- **a banked remainder value is quotable only with its convention named**. ###\"\n"
    "     \" **NOTHING ABOUT THE IDENTITY, h2, OR THE ROSTER FOLLOWS**; the vectors-outside-the-\"\n"
    "     \" object hypothesis is NAMED AS A HYPOTHESIS and tested by no act in the arc. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b314_the_fold_and_the_cold_clone.txt; data/b314_fold_emitted.md;\"\n"
    "     \" PLACE-papers/FINDINGS.md; PLACE-papers/ERRATA.md E-2026-09-03-1;\"\n"
    "     \" CORRESPONDENCE.md row 140\"),\n"
    "    # ### THE KERNEL FROM A COLD CLONE, AND THE COVERAGE ANSWER (b314).\n"
    "    (\"the-cold-clone\", \"b314 (a certification test)\",\n"
    "     \"the kernel repository cloned FRESH from origin at its current pin onto a path outside\"\n"
    "     \" the corpus, by the tool itself, and rebuilt from source. ### **build/ IS .gitignored,\"\n"
    "     \" SO THE CLONE ARRIVED WITH ZERO COMPILED ARTEFACTS -- THERE WAS NO CACHE TO BE STALE.**\"\n"
    "     \" ### elan resolved **v4.29.1 INSIDE the clone against v4.33.1 OUTSIDE it**. ### **84\"\n"
    "     \" MODULES ELABORATED FROM SOURCE IN DEPENDENCY ORDER, 0 FAILURES**, AllPrints.lean\"\n"
    "     \" re-run, and the regenerated profile compared against the banked blob at HEAD: **RAW\"\n"
    "     \" BYTE EQUALITY -- 33195 bytes each, 475 prints, 475 zero-axiom, 0 differing lines, no\"\n"
    "     \" byte-order mark and no CRLF on either side.** ### **AND THE COVERAGE QUESTION HAS AN\"\n"
    "     \" ANSWER AND IT IS *FOUND*: 25 Core modules sit outside AllPrints.lean, all 25\"\n"
    "     \" elaborate, and 91 #print axioms targets in them are NOT IN THE PROFILE AT ALL**\",\n"
    "     \"### A CERTIFICATION TEST, AND NOTHING IS REPAIRED BY IT. ### **A COLD CACHE AND A COLD\"\n"
    "     \" CHECKOUT ARE NOT A COLD MACHINE** -- one repository, one machine, that machine's own\"\n"
    "     \" elan store, OS and CPU; NOT evidence that the corpus reproduces from a clone in\"\n"
    "     \" general. ### **IT DOES NOT CONCLUDE THAT THE UNCERTIFIED TERMINALS ARE WRONG, OR\"\n"
    "     \" RIGHT** -- a terminal that elaborates with zero axioms is not thereby a terminal worth\"\n"
    "     \" certifying. ### The reason is structural: **AllPrints.lean IS A HAND-MAINTAINED IMPORT\"\n"
    "     \" LIST AND NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF IT.** ### The first\"\n"
    "     \" sweep carried two defects, both this act's own and both declared -- alphabetical order\"\n"
    "     \" reported a module as FAILING when its dependency was simply not built yet. ### NO\"\n"
    "     \" .lean FILE CREATED OR EDITED; NO MODULE ADDED TO THE CERTIFICATION FILE. ### M-2\"\n"
    "     \" UNCHANGED\",\n"
    "     \"data/b314_the_fold_and_the_cold_clone.txt; data/b314_coldclone_run.txt;\"\n"
    "     \" data/b314_coldclone_rows.json; data/b314_coldrelay_run.txt;\"\n"
    "     \" CORRESPONDENCE.md row 141\"),\n"
)

NEW_KEYS = ('the-instrument-arc', 'the-cold-clone')
ALIASES = ('the seven acts', 'b307 to b313', 'the arc as one statement',
           'the convention erratum', 'the kernel rebuilt from a clone',
           'the certification test', 'uncertified terminals', 'the coverage answer')
MUST_NOT_HIT = ('the kernel', 'coverage')


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
    print('b314 -- THE INDEX KEYS. ### THE FOLD, AND THE COLD CLONE.')
    print('=' * 100)
    print('  ### MUST-NOT-HIT, MEASURED BEFORE THE WRITE:')
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-22s NO KEY before : %s' % (q, pre[q]))

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
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + (ROW_NEW % ()), 1)
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
        ok = ok and good
        print('    %-24s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-34s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`the kernel` AND `coverage` STAY UNKEYED.** ### This act certified a REBUILD of')
    print('  ### the kernel and did not produce a result about it; and an index answering')
    print('  ### `coverage` would be offering a count of uncertified terminals as though it were a')
    print('  ### verdict on what the kernel covers, which is the reading the act refuses.')
    print('  ### **AND `the fold` IS DELIBERATELY NOT IN THIS ARM: IT ALREADY HITS SOMETHING THIS')
    print('  ### ACT DID NOT PUT THERE**, and a must-not-hit arm over an already-hit query fails')
    print('  ### for somebody else\'s reason.')

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
