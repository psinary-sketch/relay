# -*- coding: utf-8 -*-
"""b258_checks.py -- the b258 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION; NO `or` APPEARS IN ANY CHECK.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a read-only act wrote something. ### Gate 2 checks BOTH heads and BOTH indexes.
###   (2) that the enumeration leaked into the PUBLIC bank. ### **GATE 3 IS THE ONE THIS ACT MOST
###       ### NEEDS, AND IT IS A POSITIVE CONTROL ON AN ABSENCE: the SHA list must be ABSENT from
###       ### the public bank and PRESENT in the private document.**
###   (3) that a count was asserted. ### Gates 4-7 re-derive every headline number from git.
###   (4) that the 29 = 21 + 8 reconciliation was read as evidence. ### **GATE 8 IS THE TAUTOLOGY
###       ### CONTROL: the arithmetic is forced; the SET IDENTITY is not.**
###   (5) that the probes were re-run against the ferry. ### Gate 9.
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
PATH = 'phase1.5/method/patent-package'

REG = os.path.join(D, 'b258_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b258_history_inventory.txt')
PRIV = os.path.join(PP, 'internal', 'HISTORY_INVENTORY_2026-08-29.md')
B257 = os.path.join(D, 'b257_registration_2026-08-29.txt')
SELF = os.path.join(ROOT, 'tools', 'b258_checks.py')

RELAY_HEAD = '11833bae0d437683ada001f622dcd8fcdd46a512'
PP_HEAD = '2bcdff57b03d8ea2015d98d01c4655bc8ee636de'
HELD_OLEAN = ['CouplingArrival', 'DiagonalSection', 'GroupRingGlue',
              'SectorArithmetic', 'StaircaseAddresses', 'TowerInstance']


def g(args, cwd=PP):
    return subprocess.run(['git', '-C', cwd] + args, capture_output=True, text=True).stdout


def hist_paths():
    return sorted({x for x in g(['log', '--all', '--diff-filter=ACMR', '--name-only',
                                 '--format=', '--', PATH]).split('\n') if x.strip()})


def tip_paths():
    return sorted(x for x in g(['ls-files']).split('\n') if x.startswith(PATH + '/'))


def sweep_paths():
    return sorted({x for x in g(['show', '--name-only', '--format=', '--diff-filter=ACMR',
                                 '49cd156', '--', PATH]).split('\n') if x.strip()})


def held_public():
    """### RE-DERIVE THE HEADLINE: how many HELD `.olean` are reachable from relay's origin/main."""
    n = 0
    for f in HELD_OLEAN:
        out = g(['log', 'origin/main', '--diff-filter=ACMR', '--format=%h', '--',
                 'tools/lean/%s.olean' % f], cwd=ROOT)
        if out.strip():
            n += 1
    return n


def main():
    h = Harness(ROOT, 'b258')
    HP, TP, SW = hist_paths(), tip_paths(), sweep_paths()

    # 1 -- ### THE REGISTRATION PRECEDES BOTH OUTPUTS.
    h.run('registration-precedes-both-outputs',
          check=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(BANK)
                             and os.path.getmtime(REG) < os.path.getmtime(PRIV)),
          # ### FIXTURE: the same ordering demanded in reverse of two files written in order.
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(REG)),
          witness=lambda: bool(os.path.getsize(REG) > 3000))

    # 2 -- ### READ-ONLY. ### BOTH HEADS UNCHANGED, BOTH INDEXES EMPTY.
    h.run('read-only-both-heads-unchanged-nothing-staged',
          check=lambda: bool(g(['rev-parse', 'HEAD'], cwd=ROOT).strip() == RELAY_HEAD
                             and g(['rev-parse', 'HEAD']).strip() == PP_HEAD
                             and g(['diff', '--cached', '--name-only'], cwd=ROOT).strip() == ''
                             and g(['diff', '--cached', '--name-only']).strip() == ''),
          # ### FIXTURE: demand the WORKTREES be clean too. ### They are not -- this act wrote two
          # ### new untracked documents -- so this fails on the real state, not on a negation.
          fixture=lambda: bool(g(['status', '--porcelain'], cwd=ROOT).strip() == ''),
          witness=lambda: bool(len(RELAY_HEAD) == 40))

    # 3 -- ### THE DISCLOSURE RULE HELD. ### POSITIVE CONTROL ON AN ABSENCE.
    #      ### The enumeration must be ABSENT from the PUBLIC bank and PRESENT in the private doc.
    h.run('enumeration-absent-from-public-bank-present-in-private',
          check=lambda: bool(
              # ### the private document carries the SHA list and the file lists
              len(re.findall(r'\b[0-9a-f]{12}\b',
                             io.open(PRIV, encoding='utf-8').read())) > 400
              and contains(PRIV, 'PZONE-FIG-1_code-design-pipeline.svg')
              # ### THE ABSENCE: the public bank carries neither
              and len(re.findall(r'\b[0-9a-f]{12}\b',
                                 io.open(BANK, encoding='utf-8').read())) == 0
              and not contains(BANK, 'PZONE-FIG-1_code-design-pipeline.svg')
              and contains(BANK, 'THE ENUMERATION LIVES IN THE PRIVATE TREE')),
          # ### FIXTURE: demand the SHA list be in the public bank too. ### It is deliberately not,
          # ### so this fails -- and that failure is the rule working.
          fixture=lambda: bool(len(re.findall(r'\b[0-9a-f]{12}\b',
                                              io.open(BANK, encoding='utf-8').read())) > 400),
          witness=lambda: bool(os.path.getsize(PRIV) > 5000))

    # 4 -- ### THE (a) COUNTS, RE-DERIVED FROM GIT.
    h.run('place-papers-counts-re-derived',
          check=lambda: bool(len(HP) == 29 and len(TP) == 21 and len(SW) == 8
                             and len(g(['log', '--all', '--diff-filter=ACMR', '--format=%H',
                                        '--', PATH]).split()) == 5
                             and contains(BANK, '**29**') and contains(BANK, '**21**')
                             and contains(BANK, '**5**')),
          # ### FIXTURE: claim tip and history agree. ### 21 != 29, so this fails on real counts.
          fixture=lambda: bool(len(HP) == len(TP)),
          witness=lambda: bool(len(HP) > 0))

    # 5 -- ### THE SET IDENTITY: the 8 not-at-tip ARE the 49cd156 sweep. ### 8 for 8.
    h.run('gone-set-is-exactly-the-b148-sweep',
          check=lambda: bool(sorted(set(HP) - set(TP)) == SW and len(SW) == 8
                             and contains(BANK, 'IDENTICAL')
                             and contains(BANK, '8 FOR 8, SET FOR SET')),
          # ### FIXTURE: claim the gone-set is the TIP set. ### It is disjoint from it.
          fixture=lambda: bool(sorted(set(HP) - set(TP)) == TP),
          witness=lambda: bool(len(SW) == 8))

    # 6 -- ### THE HEADLINE, RE-DERIVED: SIX HELD `.olean` ON PUBLIC `origin/main`.
    h.run('six-held-oleans-reachable-from-public-main',
          check=lambda: bool(held_public() == 6
                             and g(['log', 'origin/main', '--diff-filter=ACMR', '--format=%h',
                                    '--', 'reports/2026-08-13-carrier-build-act1.md'],
                                   cwd=ROOT).strip() == ''
                             and contains(BANK, 'SIX OF THE EIGHT HELD-CARRIER PATHS ARE '
                                                'REACHABLE FROM `origin/main`')),
          # ### FIXTURE: claim all EIGHT are public. ### Two are on the local branch only.
          fixture=lambda: bool(held_public() == 8),
          witness=lambda: bool(held_public() > 0))

    # 7 -- ### THE (c) CITATION COUNTS AND THEIR NAMED FALSE-POSITIVE CLASSES.
    h.run('citation-web-counts-and-false-positive-classes-named',
          check=lambda: bool(contains(BANK, '22,038') and contains(BANK, '**723**')
                             and contains(BANK, '**DISTINCT PLACE-papers COMMITS CITED   : 490**')
                             and contains(BANK, '42.1%')
                             and contains(BANK, 'NAMED AND SUBTRACTED RATHER THAN SILENTLY KEPT')
                             and contains(BANK, '1,382')
                             and len(g(['log', '--all', '--format=%H']).split()) == 1165),
          # ### FIXTURE: claim PLACE-papers has a different history size. ### It has 1165.
          fixture=lambda: bool(len(g(['log', '--all', '--format=%H']).split()) == 1164),
          witness=lambda: contains(BANK, '490'))

    # 8 -- ### THE TAUTOLOGY CONTROL. ### THE ARITHMETIC IS FORCED; THE SET IDENTITY IS NOT.
    h.run('reconciliation-arithmetic-is-forced-set-identity-is-not',
          check=lambda: bool(
              # ### FORCED: |history| - |tip| = |difference| holds for ANY two nested sets
              len(HP) - len(TP) == len(set(HP) - set(TP))
              # ### NOT FORCED: that the difference equals the sweep. ### Shown by a counterexample
              # ### on arbitrary sets of the same sizes.
              and sorted(set(HP) - set(TP)) == SW
              and sorted(set(HP[:29]) - set(HP[:21])) != SW
              and contains(BANK, 'AND IT IS EXACT')),
          # ### FIXTURE: the vacuous form -- |A|-|B| == |A-B| on arbitrary nested sets, which is
          # ### true by construction and therefore asserts nothing.
          fixture=lambda: bool(len({1, 2, 3}) - len({1, 2}) != len({1, 2, 3} - {1, 2})),
          witness=lambda: bool(len(HP) - len(TP) == 8))

    # 9 -- ### THE PROBES WERE NOT RE-RUN. ### THE NAVIGATOR'S VERDICT IS CITED.
    h.run('probes-cited-not-re-run',
          check=lambda: bool(contains(BANK, 'were **NOT** re-run')
                             and contains(BANK, "navigator's 2026-08-29 verdict is cited")
                             and contains(REG, 'NOT RE-TESTED')
                             # ### THIS CONJUNCT'S FIRST FORM WAS WRONG AND THE GATE FAILED ON IT.
                             # ### It banned the STRING `HTTP nnn` from the bank outright -- but the
                             # ### bank legitimately CITES b257's verdict ("b257 probed it: HTTP
                             # ### 200"), and ### **A CRUDE STRING BAN CANNOT TELL CITING A PRIOR
                             # ### PROBE FROM RUNNING A NEW ONE.** ### Same species as b256's gate 3
                             # ### and b255's negative conjuncts: a matcher forbidding a token the
                             # ### act legitimately carries.
                             # ### ### **THE FIX TESTS THE ACT, NOT THE PROSE: this act's own
                             # ### ### tooling must contain NO network capability at all.**
                             # ### AND THE FIX'S OWN FIRST FORM FAILED TOO, FOR A THIRD REASON
                             # ### WORTH NAMING: it searched this file for a regex whose LITERAL
                             # ### TEXT SITS IN THIS FILE, so ### **THE MATCHER MATCHED ITS OWN
                             # ### PATTERN DEFINITION.** ### b248 matched inside a COMMENT, b253
                             # ### inside a DATA STRING, and this inside ITS OWN REGEX -- the same
                             # ### family, third variant. ### **IMPORT LINES CANNOT SELF-MATCH.**
                             and not re.search(r'^\s*import\s+(urllib|requests|http|socket)\b',
                                               io.open(SELF, encoding='utf-8').read(), re.M)
                             and not re.search(r'^\s*from\s+(urllib|requests|http|socket)\b',
                                               io.open(SELF, encoding='utf-8').read(), re.M)
                             # ### and where HTTP is mentioned, it is attributed to b257
                             and contains(BANK, 'b257 probed it: HTTP 200')),
          # ### FIXTURE: demand this checks file itself be free of the word `probe`. ### It is full
          # ### of it -- so this fails on the real file rather than on a negation of the check.
          fixture=lambda: bool('probe' not in io.open(SELF, encoding='utf-8').read()),
          witness=lambda: contains(BANK, 'navigator'))

    # 10 -- ### NO RECOMMENDATION, AND b257's HALT IS NOT QUIETLY RESUMED.
    h.run('no-recommendation-and-b257-halt-untouched',
          check=lambda: bool(contains(BANK, 'NO RECOMMENDATION IS MADE')
                             and contains(BANK, 'does not smuggle a recommendation in as a')
                             and contains(BANK, 'THAT GUARD QUESTION\n### ### IS STILL OPEN')
                             and len(tip_paths()) == 21),
          # ### FIXTURE: claim the tip was cleaned. ### It was not -- b257 halted -- so this fails.
          fixture=lambda: bool(len(tip_paths()) == 0),
          witness=lambda: contains(BANK, 'b257'))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
