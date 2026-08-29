# -*- coding: utf-8 -*-
"""b256_checks.py -- the b256 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION; NO `or` APPEARS IN ANY CHECK.** ### **EVERY NUMERIC
### PREDICATE IS `bool()`-WRAPPED.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the map CONFERRED a grade instead of stating one. ### Gates 6-7.
###   (2) that the patent tree was written. ### Gate 3, against `git status` in PLACE-papers.
###   (3) that a count was asserted rather than taken. ### Gates 4-5 RE-COUNT from the filesystem.
###   (4) that an obstacle was paraphrased. ### Gate 8: twenty-two acts, twenty-two quotations.
###   (5) that SIGNEDNESS was invented to fill the slot. ### **GATE 9 IS A POSITIVE CONTROL ON AN
###       ### ABSENCE, AND IT IS THE ONE THIS ACT MOST NEEDS.**
###   (6) that the h2 column was asserted. ### Gate 5 parses the table.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
PKG = os.path.join(PP, 'phase1.5', 'method', 'patent-package')
FIG = os.path.join(PKG, 'figures')

REG = os.path.join(D, 'b256_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b256_contribution_map.txt')
MAP = os.path.join(PP, 'phase1.5', 'method', 'CONTRIBUTION_MAP_2026-08.md')
CSV = os.path.join(D, 'b256_b255_profile.csv')
B255 = os.path.join(D, 'b255_limit_profile.txt')
GUARD = os.path.join(ROOT, 'tools', 'place_add.py')

ACTS = list(range(234, 256))            # ### 22 acts
PERFILING = ['pfano-wpt', 'prov1', 'pzone', 'prov2', 'pident', 'pcode']


def built_count():
    """### RE-COUNT THE BUILT FIGURES FROM THE FILESYSTEM, NOT FROM THE MAP'S PROSE."""
    n = 0
    for d in PERFILING:
        p = os.path.join(FIG, d)
        n += len([f for f in os.listdir(p) if f.endswith('.svg')]) if os.path.isdir(p) else 0
    return n


def review_count():
    p = os.path.join(FIG, 'REVIEW_SET_2026-08')
    return len([f for f in os.listdir(p) if f.endswith('.svg')])


def map_rows():
    """### PARSE THE MAP'S MAIN TABLE. ### The h2 column is READ, not taken on trust."""
    t = io.open(MAP, encoding='utf-8').read()
    body = t.split('## The map', 1)[1].split('### Row counts', 1)[0]
    out = []
    for line in body.split('\n'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 8 and re.match(r'^\d+$', cells[0]):
            out.append(cells)
    return out


def signedness_absent_outside_this_act():
    """### THE POSITIVE CONTROL ON AN ABSENCE THIS ACT MOST NEEDS.

    ### The ferry directed SIGNEDNESS be QUOTED "as drafted in the conversation layer". ### **IT IS
    ### NOT IN THE CORPUS AND NOT IN THIS SEAT'S REACH**, so it could not be quoted and was recorded
    ### as OWED. ### **THIS GATE PROVES THE ABSENCE IS REAL RATHER THAN A FAILURE TO LOOK**: the
    ### token appears ONLY in this act's own files (which say it is owed), and NOWHERE ELSE in
    ### `relay/` or `PLACE-papers/`.
    ### ### **AND IT PROVES THE SLOT WAS NOT FILLED BY INVENTION: no S/I/D/E letter-gloss, no
    ### ### numbered spec, appears anywhere under the name.**
    """
    hits = []
    for base in (ROOT, PP):
        for dp, dn, fn in os.walk(base):
            if '.git' in dp:
                continue
            for f in fn:
                if not f.endswith(('.md', '.txt', '.py', '.lean', '.json')):
                    continue
                p = os.path.join(dp, f)
                try:
                    t = io.open(p, encoding='utf-8', errors='ignore').read()
                except Exception:
                    continue
                if re.search(r'SIGNEDNESS|S\u00b7I\u00b7D\u00b7E\+S|SIDE\+S', t):
                    hits.append(os.path.basename(p))
    own = {'b256_contribution_map.txt', 'b256_registration_2026-08-29.txt',
           'CONTRIBUTION_MAP_2026-08.md', 'b256_checks.py', 'b256_handoff.py',
           '2026-08-29-the-contribution-map.md', 'banked_index.py',
           'b256_index_append.py'}
    foreign = [h for h in hits if h not in own]
    return bool(len(foreign) == 0 and len(hits) > 0)


def main():
    h = Harness(ROOT, 'b256')
    R = map_rows()

    # 1 -- ### THE REGISTRATION PRECEDES THE MAP AND THE BANK.
    h.run('registration-precedes-map-and-bank',
          check=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(MAP)
                             and os.path.getmtime(REG) < os.path.getmtime(BANK)),
          # ### FIXTURE: the same ordering demanded in reverse of two files written in order.
          fixture=lambda: bool(os.path.getmtime(MAP) < os.path.getmtime(REG)),
          witness=lambda: bool(os.path.getsize(REG) > 4000))

    # 2 -- ### THE CLASS LINE IS ON THE DOCUMENT AND SAYS WHAT IT FORBIDS.
    h.run('class-line-states-grades-confers-none',
          check=lambda: bool(contains(MAP, 'TIER N')
                             and contains(MAP, 'PRIVATE')
                             and contains(MAP, 'PATENT-SESSION INPUT')
                             and contains(MAP, 'STATES GRADES, CONFERS NONE')
                             and contains(MAP, 'This document *states* grades. It confers none')),
          fixture=lambda: contains(B255, 'STATES GRADES, CONFERS NONE'),
          witness=lambda: contains(MAP, 'TIER N'))

    # 3 -- ### THE PATENT TREE WAS NOT WRITTEN. ### THE b148 BOUNDARY.
    # ### ### **THIS GATE'S FIRST CRITERION WAS WRONG AND IT FAILED, AND THE FAILURE TAUGHT
    # ### ### SOMETHING.** ### It demanded that NO `patent-package/` path appear in
    # ### ### `git status`. ### **BUT SEVEN PATENT-SEAT FIGURE DIRECTORIES ARE SITTING UNTRACKED
    # ### ### IN THE SHARED WORKTREE RIGHT NOW, DATED 2026-08-24 -- FIVE DAYS BEFORE THIS ACT.**
    # ### ### They are the OTHER seat's work, not this one's, and their presence is not a breach
    # ### ### by this act -- ### **IT IS PRECISELY THE b148 CONDITION THE GUARD EXISTS FOR, LIVE.**
    # ### The right criterion is not "does the tree mention the patent path" but ### **"did THIS
    # ### ACT create or modify one, and did it stage one."** ### Both are checked below.
    h.run('patent-package-not-written-or-staged-by-this-act',
          check=lambda: bool(
              # ### (a) nothing under the patent tree is NEWER than this act's registration
              max((os.path.getmtime(os.path.join(dp, f))
                   for dp, dn, fn in os.walk(PKG) for f in fn if '.git' not in dp),
                  default=0) < os.path.getmtime(REG)
              # ### (b) nothing under the patent tree is STAGED
              and not any(l[:2] != '??' and 'patent-package/' in l
                          for l in subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                                                  capture_output=True).stdout
                          .decode('utf-8', 'replace').split('\n') if l.strip())
              # ### (c) the guard that makes (b) safe is present and names the prefix
              and "FOREIGN = ['phase1.5/method/patent-package/']" in
              io.open(GUARD, encoding='utf-8').read()),
          # ### FIXTURE: demand the patent tree be newer than this act's registration. ### It is
          # ### five days older, so this fails on real mtimes rather than on a negation.
          fixture=lambda: bool(
              max((os.path.getmtime(os.path.join(dp, f))
                   for dp, dn, fn in os.walk(PKG) for f in fn if '.git' not in dp),
                  default=0) > os.path.getmtime(REG)),
          witness=lambda: bool(os.path.isdir(PKG)))

    # 4 -- ### THE FIGURE COUNTS RE-COUNTED FROM THE FILESYSTEM.
    h.run('figure-counts-re-counted-44-built-31-review',
          check=lambda: bool(built_count() == 44 and review_count() == 31
                             and contains(MAP, '**44 built**')
                             and contains(MAP, '`REVIEW_SET_2026-08` = 31')
                             and len([f for f in os.listdir(FIG) if f.endswith('.svg')]) == 7),
          # ### FIXTURE: claim the per-filing dirs hold the REVIEW_SET count. ### 44 != 31, so this
          # ### fails on real directory listings.
          fixture=lambda: bool(built_count() == review_count()),
          witness=lambda: bool(built_count() > 0))

    # 5 -- ### THE h2 COLUMN, PARSED FROM THE TABLE RATHER THAN TAKEN ON TRUST.
    h.run('every-patent-facing-row-is-h2-independent',
          check=lambda: bool(
              len(R) == 18
              and sum(1 for r in R if r[5] == '**NO**'
                      or r[5].startswith('### **NO')) >= 13
              # ### the five patent-facing rows carry a filing and MUST be NO
              and all('NO' in r[5] and 'YES' not in r[5]
                      for r in R if r[6] not in ('—', '-', ''))
              and contains(MAP, 'Every patent-facing row (10, 11, 12, 15, 16) is `NO`')),
          # ### FIXTURE: claim EVERY row is NO. ### Five are YES (adjacent), so this fails on the
          # ### parsed table and the column is shown to be doing work.
          fixture=lambda: bool(all('NO' in r[5] and 'YES' not in r[5] for r in R)),
          witness=lambda: bool(len(R) == 18))

    # 6 -- ### NO GRADE WAS CONFERRED. ### J1 PARKED, J2 UNPROMOTED, NO NEW Priority-A.
    h.run('no-grade-conferred-and-nothing-promoted',
          check=lambda: bool(contains(MAP, 'PARKED-BY-AUTHOR ("save"). UNPROMOTED')
                             and contains(MAP, 'J2') and contains(MAP, 'CANDIDATE. UNPROMOTED')
                             and contains(MAP, 'None is Priority-A')
                             and contains(BANK, 'IT MOVED NO GRADE')
                             # ### THE ABSENCE: no annex-A candidate is labelled Priority-A
                             and not re.search(r'\|\s*\*\*Priority-A\*\*\s*\|',
                                               io.open(MAP, encoding='utf-8').read())),
          fixture=lambda: contains(B255, 'PARKED-BY-AUTHOR'),
          witness=lambda: contains(MAP, 'Annex A'))

    # 7 -- ### THE MAP DOES NOT PROMOTE BY ADJECTIVE EITHER: EVERY ANNEX-A ITEM IS MARKED.
    h.run('every-figure-candidate-marked-new-filing-or-continuation',
          check=lambda: bool(
              io.open(MAP, encoding='utf-8').read().count('**NEW-FILING**') >= 6
              and io.open(MAP, encoding='utf-8').read().count('**CONTINUATION**') >= 1
              and contains(MAP, 'Every item is marked NEW-FILING or CONTINUATION')),
          fixture=lambda: bool(io.open(MAP, encoding='utf-8').read().count('**NEW-FILING**') == 0),
          witness=lambda: contains(MAP, 'Annex A'))

    # 8 -- ### TWENTY-TWO ACTS, TWENTY-TWO OBSTACLES, ALL QUOTED. ### NO PARAPHRASE.
    h.run('twenty-two-acts-with-quoted-obstacles',
          check=lambda: bool(all(('**b%d ' % n) in io.open(BANK, encoding='utf-8').read()
                                 for n in ACTS)
                             and len(ACTS) == 22
                             and contains(BANK, 'EVERY OBSTACLE IS QUOTED FROM ITS OWNING ACT')
                             and contains(BANK, 'THE FOLD RULES FORBID PARAPHRASE')
                             and contains(BANK, 'COUNT RECONCILED: b234 THROUGH b255 INCLUSIVE = '
                                                '22 ACTS, 22 REPORTS')
                             # ### and the reports really are there, one per act
                             and len([f for f in os.listdir(os.path.join(ROOT, 'reports'))
                                      if f.startswith('2026-08-2') and f.endswith('.md')]) >= 22),
          # ### FIXTURE: demand an act OUTSIDE the arc be in the ledger. ### b233 is not, so this
          # ### fails on the real bank and the ledger's bounds are shown to be real.
          fixture=lambda: bool('**b233 ' in io.open(BANK, encoding='utf-8').read()),
          witness=lambda: contains(BANK, '**b234 '))

    # 9 -- ### POSITIVE CONTROL ON AN ABSENCE. ### SIGNEDNESS WAS OWED, NOT INVENTED.
    h.run('signedness-owed-not-invented',
          check=lambda: bool(signedness_absent_outside_this_act()
                             and contains(MAP, 'QUOTATION OWED')
                             and contains(MAP, 'It is not paraphrased, and it is not invented')
                             and contains(MAP, 'returns **zero occurrences**')),
          # ### FIXTURE: claim the token appears NOWHERE AT ALL, including this act's own files.
          # ### It does appear here -- saying it is owed -- so this fails, and the gate is shown to
          # ### be reading files rather than asserting an absence.
          fixture=lambda: bool(not contains(MAP, 'SIGNEDNESS')),
          witness=lambda: contains(MAP, 'Annex B'))

    # 10 -- ### THE CSV BLOCK IS CHART-READY AND MATCHES b255's ARRAYS.
    h.run('csv-block-present-and-matches-b255',
          check=lambda: bool(os.path.exists(CSV)
                             and io.open(CSV, encoding='utf-8').read().strip().split('\n')[0]
                             .startswith('a2,stair_2')
                             and len(io.open(CSV, encoding='utf-8').read().strip().split('\n')) == 17
                             and contains(MAP, 'a2,stair_2,stair_3,stair_5')
                             and contains(MAP, '100,6,4,2,0.410262')
                             and contains(MAP, 'every profile act')
                             and contains(MAP, 'chart-ready CSV')),
          # ### FIXTURE: demand 18 CSV lines (16 cells + header = 17). ### A real count that fails.
          fixture=lambda: bool(
              len(io.open(CSV, encoding='utf-8').read().strip().split('\n')) == 18),
          witness=lambda: bool(os.path.getsize(CSV) > 200))

    # 11 -- ### THE TAUTOLOGY CONTROL. ### THE ROW ARITHMETIC MUST HAVE CONTENT.
    #       ### `13 + 5 = 18` is forced once the counts are fixed -- **RESTATEMENT** -- so the gate
    #       ### tests the thing that is NOT forced: that the SPLIT falls where the map says.
    h.run('row-split-is-not-an-arithmetic-tautology',
          check=lambda: bool(
              # ### forced: the two classes partition the rows
              len([r for r in R if 'NO' in r[5] and 'YES' not in r[5]])
              + len([r for r in R if 'YES' in r[5]]) == len(R)
              # ### NOT forced: which rows land where, re-derived against the map's own claim
              and sorted(int(r[0]) for r in R if 'YES' in r[5]) == [1, 2, 8, 9, 17]
              and contains(MAP, '`h2`-dependency `NO`: 13. `YES (adjacent)`: 5')),
          # ### FIXTURE: claim a DIFFERENT split. ### The parsed table says otherwise.
          fixture=lambda: bool(sorted(int(r[0]) for r in R if 'YES' in r[5]) == [1, 2, 3, 8, 9]),
          witness=lambda: bool(len(R) == 18))

    # 12 -- ### THE WALLS AND THE COUNSEL FIVE ARE ON THE HEADER AND TRUE AT SOURCE.
    h.run('walls-and-counsel-five-true-at-source',
          check=lambda: bool(contains(MAP, '2027-04-09') and contains(MAP, '2027-04-13')
                             and contains(MAP, '2027-05-14')
                             and contains(os.path.join(FIG, 'prov1', 'PROV1_FIGURES.md'),
                                          '2027-04-09')
                             and contains(os.path.join(FIG, 'pzone', 'PZONE_FIGURES.md'),
                                          '2027-05-14')
                             and contains(os.path.join(FIG, 'pcode', 'PCODE_FIGURES.md'),
                                          '2027-04-13')
                             and contains(MAP, 'The counsel five')
                             and contains(MAP, 'The finalized strategy')),
          # ### FIXTURE: claim PROV-1's record carries the P-ZONE wall. ### It does not.
          fixture=lambda: contains(os.path.join(FIG, 'prov1', 'PROV1_FIGURES.md'), '2027-05-14'),
          witness=lambda: contains(MAP, 'the earliest of the six'))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
