# -*- coding: utf-8 -*-
"""b307_index_append.py -- TWO KEYS. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### **THE ORDER SAYS `fold rows keyed` AND EVERY RESULT KEYED.** ### This act has two results:
### the fold itself, and the ledger census that licensed a struck phrase by satisfying its own
### `SURVIVES` clause.

### ### **THE MUST-NOT-HIT ARM IS b202's, MEASURED BEFORE AND AFTER:** ### **`current` AND `the
### ### section` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT OBJECTS.**
### ### **AND THE INDEX IS SWEPT FOR STEMS AFTER THE WRITE** (b305's defect, caught at b306).
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
    "    'the-fold': ['the adelic arc', 'the adelic fold', 'the arc statement',\n"
    "                'the b297-b306 fold', 'the lore', 'the instrument suite', 'the desk'],\n"
    "    'handoff-census': ['the ledger census', 'the handoff census',\n"
    "                      'what is missing from the ledger', 'the conditional strike'],\n"
)

ROW_ANCHOR = ("INDEX = [\n"
              "    # (key, act, one-line statement, grade as its own act recorded it, location)\n")
ROW_NEW = (
    "    # ### THE ADELIC ARC FOLDED (b307).\n"
    "    (\"the-fold\", \"b307 (a filings act)\",\n"
    "     \"ten acts, b297-b306, filed into FINDINGS.md as 'THE ADELIC ARC, b297-b306 -- THE\"\n"
    "     \" FOLD', each entry with its grade as its OWN act left it, its scope sentence, and its\"\n"
    "     \" OBSTACLE quoted. ### **THE ARC AS ONE STATEMENT:** the object's two halves now share a\"\n"
    "     \" form and a dilation (one sentence defines a two-radius family at every place, and the\"\n"
    "     \" finite dilation is the archimedean dilation at 1/p under the corpus's own chart); the\"\n"
    "     \" finite side's first-level mass is annihilated exactly when either radius clears its\"\n"
    "     \" threshold; the archimedean instruments compute with vectors OUTSIDE the object's own\"\n"
    "     \" space; and the corpus works at the OPEN end of a single window parameter whose CLOSED\"\n"
    "     \" end is the source's forced positivity. ### Also folded: the arc's four corrections to\"\n"
    "     \" its own readings, each with a WHAT DID NOT MOVE column\",\n"
    "     \"### A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER. ### **NO GRADE MOVES,\"\n"
    "     \" NO ACT IS RE-VERDICTED, NO NEW MATHEMATICS, NO KEYSTONE WRITTEN OR EDITED** -- b299's\"\n"
    "     \" arc keystone is cross-referenced, not duplicated. ### Emitted by tools/b307_fold.py,\"\n"
    "     \" the section's GENERATOR and not its reviewer: 20 quotations, 0 unfindable, each\"\n"
    "     \" checked against the act that ORIGINATED it BEFORE emission -- and two failed on the\"\n"
    "     \" first run, one of them a sentence b303 was quoting from b301, so the gate caught a\"\n"
    "     \" mis-attribution before the document existed. ### FINDINGS.md +80/-0, measured by\"\n"
    "     \" numstat: PURELY ADDITIVE is the measurement, not the assertion. ### **SCOPE: NOTHING\"\n"
    "     \" ABOUT THE IDENTITY, h2, OR THE COMPLETE ROSTER FOLLOWS FROM THE ARC SENTENCE** -- one\"\n"
    "     \" half of the one-signed residual is derived and the other is at bench, and a summary\"\n"
    "     \" may not upgrade a bench result by standing it next to a derived one. ### NO\"\n"
    "     \" AGGREGATION IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)\",\n"
    "     \"data/b307_the_fold.txt; data/b307_fold_run.txt; PLACE-papers/FINDINGS.md;\"\n"
    "     \" CORRESPONDENCE.md row 126\"),\n"
    "    # ### THE LEDGER CENSUS AND THE CONDITIONAL STRIKE (b307).\n"
    "    (\"handoff-census\", \"b307 (a check built to satisfy a conditional strike)\",\n"
    "     \"the ferry scan fired on the ORDER'S OWN CLOSING: U-2, 'a closing sequence asserts that\"\n"
    "     \" a ledger is current', struck at b300. ### **THE STRIKE IS CONDITIONAL AND THE RECORD\"\n"
    "     \" NAMES THE CONDITION:** 'SURVIVES: the same phrase after a check that has COUNTED WHAT\"\n"
    "     \" IS MISSING.' ### No such check existed, which is why the phrase had been unusable\"\n"
    "     \" since b300 and every act since wrote two lists instead. ### tools/b307_handoff_\"\n"
    "     \"census.py counts the arc's acts, the live work-orders and the arc's findings section\"\n"
    "     \" against HANDOFF.md, run BEFORE and AFTER. ### **BEFORE: 26 MISSING -- ten acts,\"\n"
    "     \" fourteen work-orders, one section. ### AFTER: 0**\",\n"
    "     \"### A LICENCE EARNED AND BOUNDED. ### U-2's SURVIVES clause is satisfied FOR THIS\"\n"
    "     \" LEDGER AND NO OTHER. ### **THE CENSUS COUNTS NAMES, NOT UNDERSTANDING** -- a ledger\"\n"
    "     \" naming every act in one line each would pass it and could still be a bad handoff --\"\n"
    "     \" and it says NOTHING about FINDINGS.md, REGISTRY.md, OPEN_TRAILS.md,\"\n"
    "     \" VERIFICATION_LOOM.md or the desk, which were not counted and are not claimed.\"\n"
    "     \" ### **THE ACT NEITHER REFUSED THE ORDER NOR OBEYED IT AS WRITTEN**: it read the\"\n"
    "     \" strike entry, found the strike conditional, and did the work the condition names --\"\n"
    "     \" which is the b299 shape with the sign reversed, the command path reading the ferry and\"\n"
    "     \" finding the ORDER asking for a struck phrase. ### NO GRADE MOVES. ### M-2 UNCHANGED\",\n"
    "     \"data/b307_the_fold.txt; data/b307_census_before.txt; data/b307_census_after.txt;\"\n"
    "     \" data/STRUCK_CLAUSES.md (U-2); CORRESPONDENCE.md row 127\"),\n"
)

NEW_KEYS = ('the-fold', 'handoff-census')
ALIASES = ('the adelic arc', 'the arc statement', 'the lore', 'the desk',
           'the ledger census', 'the conditional strike')
MUST_NOT_HIT = ('current', 'the section')


def no_key(out):
    """### TRUE IFF THE INDEX'S OWN VERDICT LINE SAYS `NO KEY`. ### **LINE-SCOPED** -- b302's D7."""
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
    print('b307 -- THE INDEX KEYS. ### THE FOLD, AND THE CENSUS THAT LICENSED A STRUCK PHRASE.')
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
        print('  %-18s key/row already present : %s / %s' % (k, have_key[k], have_row[k]))
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
        ok = ok and good
        print('    %-18s returns a row : %s  %s' % (k, good, 'PASS' if good else '### FAIL ###'))

    print('  ### THE ALIASES, EACH OF WHICH RETURNED `NO KEY` BEFORE THIS ACT:')
    for q in ALIASES:
        out, _rc = query(q)
        good = not no_key(out)
        ok = ok and good
        print('    %-26s now reaches a row : %s  %s'
              % (q, good, 'PASS' if good else '### FAIL ###'))

    print('  ### MUST-NOT-HIT, RE-MEASURED AFTER THE WRITE:')
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        quiet = no_key(out)
        good = quiet and pre[q]
        ok = ok and good
        print('    %-22s still NO KEY : %s   (and was before : %s)  %s'
              % (q, quiet, pre[q], 'PASS' if good else '### FAIL -- a nearest string became a hit'))
    print('  ### **`current` AND `the section` STAY UNKEYED BECAUSE THEY ARE PROPERTIES AND NOT')
    print('  ### OBJECTS** -- b202\'s own reason. ### **AND b164\'s LIMIT IS NOT RETIRED.**')

    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    _c, sh = ferry_scan.scan_text(io.open(PATH, encoding='utf-8').read(), [], ferry_scan.stems())
    print('  ### THE INDEX SWEPT AFTER THE WRITE (b305\'s defect, not repeated) : %d stem hit(s)'
          % len(sh))
    for h in sh:
        print('      line %d  %s' % (h[1], h[3][:96]))
    ok = ok and not sh
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
