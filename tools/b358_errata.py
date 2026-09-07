# -*- coding: utf-8 -*-
"""b358_errata.py -- RULING (R2): THE ROUTED ENTRY, FILED. ### **APPEND-ONLY. ### NOTHING ABOVE IS EDITED.**

### ### **THE RULING, QUOTED:** ### *"The routed errata entry is filed in the section the partition assigns
### it."* ### The entry was DRAFTED AND ROUTED by `b357` at `relay/data/b357_errata_draft.txt` and left
### unopened, which is the record's convention; ### **THE AUTHOR HAS NOW RULED IT FILED**, and this tool
### files it.
### ### **WHERE THE PARTITION PUTS IT: `INTERNAL-RECORD`.** ### The partition block's own law is that ###
### *"each entry is placed by its own words (quoted beside its id)"*, and this entry's words are
### `NO DEPOSITED ARTIFACT IS AFFECTED` -- it concerns four of the corpus's own ledgers and no deposited
### text. ### **AND THE PARTITION BLOCK ITSELF IS NOT EDITED**, which is the convention `b341` established
### when it filed `E-2026-09-06-1` after the block without adding a bullet to either list.
### ### **THE ENTRY IS BUILT FROM `b357`'s BANKED READING, NOT RETYPED:** ### the counts, the ledgers and
### the line numbers come from `data/b357_read.json`.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
ERR = os.path.join(PP, 'ERRATA.md')
MARK = '<!-- b358 -->'
EID = 'E-2026-09-07-1'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def blob():
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:ERRATA.md'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''


def entry_lines(C):
    w = C['wider']
    fault = C['attribution_fault']
    memo = C['membership_only']
    where = ', '.join('`%s` line %d' % (r['ledger'], r['line']) for r in w)
    fwhere = ', '.join('`%s`:%d (about %s)' % (r['ledger'], r['line'], r['act']) for r in fault)
    mwhere = ', '.join('`%s`:%d (about %s)' % (r['ledger'], r['line'], r['act']) for r in memo)
    return ['', MARK, '',
            '## %s \u2014 Five passages across all four ledgers credit the Definition 3.1 scan with '
            'establishing class membership, or assert that membership without naming a warrant '
            '(INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)' % EID,
            '',
            '**Filed 2026-09-07 (b358), on the author\'s ruling (R2). Drafted and routed 2026-09-07 by '
            'b357, which read the ledgers and left the entry unopened per the record\'s convention '
            '(relay `data/b357_errata_draft.txt`). Records affected: `FINDINGS.md`, `FACES_LEDGER.md`, '
            'SIDE-global-section `CORRESPONDENCE.md`, relay `tools/banked_index.py`. '
            '### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY.** All four are the corpus\'s own '
            'internal ledgers; no deposited text carries the wording corrected here.',
            '',
            '**What the passages say.** b357 located and classified twelve passages bearing on the '
            'lawfulness of the corpus\'s own test functions, splitting **%d WIDER / %d NARROWER / '
            '%d SILENT**, with none unclassified. The %d wider ones are at %s \u2014 **one in each of the '
            'four ledgers**, which is what made this entry owed rather than optional.'
            % (C['n_wider'], C['n_narrower'], C['n_silent'], C['n_wider'], where),
            '',
            '**What is wrong, and it is the warrant and not the claim.** Every `f` in this family is '
            '**built** as `g \u22c6 g\u266f`, the source\'s own involution. For a true autocorrelation the '
            'Fourier transform is a squared modulus, so pointwise positivity is automatic and '
            '**the Definition 3.1 scan cannot fail on such an object**. What the scan discriminates is '
            'objects built as autocorrelations from objects not built that way \u2014 which b320 showed '
            'with its own control, a wide-minus-narrow fixture returning `min f-hat = -5.85e-01`. '
            '**That is a real check, it passed, and it is what keeps the scan from being vacuous. '
            'It is not a test of class membership.**',
            '',
            '**The two groups, kept apart.** *(1) The attribution fault* \u2014 %d passages naming the scan '
            'as the warrant, by a parenthetical or by the preposition *by*: %s. *(2) Membership asserted '
            'with no warrant named* \u2014 %d passages carrying the same summarised parenthetical: %s.'
            % (len(fault), fwhere, len(memo), mwhere),
            '',
            '**And the sentence that bounds this entry: the wider sentence is not necessarily false.** '
            'The corpus builds `f` with the source\'s support and vanishing conditions, and if the objects '
            'integrated were smooth they would be in the class. Whether the piecewise-linear object the '
            'corpus integrates is in a class defined over `C_c^\u221e` at all is a **separate question** \u2014 '
            'b355\'s `H1`, graded `REFUTABLE` and **routed to the author** \u2014 and this entry does not '
            'decide it. The two must not be merged.',
            '',
            '**The proposed wording, offered and not applied.** Where a passage says the seeds are in the '
            'class *by* the scan, the narrower sentence b355 supports \u2014 and which b355 already put into '
            '`CORRESPONDENCE.md` and `tools/banked_index.py` \u2014 is: *"the seeds are built as '
            'autocorrelations of a piecewise-linear interpolant of a sampled smooth bump, and the scan '
            'confirms the discrete construction behaves like a continuous one within its reach."* '
            '**NO LEDGER IS EDITED BY THIS ENTRY.** The correction of record is this entry and b357\'s '
            'bank, relay `data/b357_what_the_ledgers_say.txt`, following the `E1` precedent '
            '(`E-2026-08-31-1`); whether to repair the five passages in place stays the author\'s.',
            '',
            '**And the record is not uniform, which is worth the reader\'s eye.** `FINDINGS.md` also '
            'carries *"a local proposition per seed (lawful or not), decided by b320\'s scan"* and the '
            '`K1` grade **`MEASURED-ON-FAMILIES (b320)`** \u2014 both careful, and both written while an act '
            'was **grading a constituent**. The widest passage sits in prose that **summarises** what the '
            'arc achieved. The record is more careful where it is grading than where it is narrating.',
            '',
            '**Scope, stated so it is not read wider than it is.** *No banked number is affected* \u2014 every '
            'figure in b320, b328, b334, b343, b344 and b349 stands exactly as banked. *No check is '
            'demoted* \u2014 every check that passed still passed. *No verdict moves and no act is '
            're-verdicted.* *And it is not a claim that any ledger says something false.* '
            'One line number straddles the filing: `tools/banked_index.py:1022` is the line b357 read and '
            'relied on, and appending b357\'s own index key moved that row to `1054`; both are recorded '
            'here by b352\'s straddling rule.',
            '',
            '*Filed by b358 (relay `data/b358_the_li_asymptotics.txt`; the reading is b357\'s, relay '
            '`data/b357_read_run2.txt`). No deposited artifact is affected.*',
            '',
            '---']


def main():
    C = json.load(io.open(os.path.join(D, 'b357_read.json'), encoding='utf-8'))
    txt = io.open(ERR, encoding='utf-8').read()
    before = len(txt.splitlines())
    rec('=' * 100)
    rec('b358 -- RULING (R2): THE ERRATA ENTRY, FILED. ### APPEND-ONLY; THE PARTITION BLOCK UNTOUCHED.')
    rec('=' * 100)
    part = '## THE PARTITION'
    part_block = txt[txt.index(part):] if part in txt else ''
    part_head = part_block.split('<!-- ')[0] if part_block else ''
    if MARK in txt:
        rec('  the mark %s is already present -- DUPLICATE, nothing written.' % MARK)
        wrote = False
        new = txt
    else:
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(entry_lines(C)) + chr(10)
        open(ERR + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(ERR + '.tmp', ERR)
        wrote = True
    back = io.open(ERR, encoding='utf-8').read()
    after = len(back.splitlines())
    b = blob()
    append_only_blob = (not b) or back.startswith(b.rstrip(chr(10)))
    append_only_work = back.startswith(txt.rstrip(chr(10))) if wrote else True
    part_same = (part_head in back) if part_head else True
    nmark = back.count(MARK)
    nid = back.count(EID)
    ok = (nmark == 1 and nid >= 1 and append_only_blob and append_only_work and part_same)
    rec('  entry id                       : %s' % EID)
    rec('  wrote                          : %s' % wrote)
    rec('  mark on disk                   : %d time(s)  (1 required)' % nmark)
    rec('  the id appears                 : %d time(s)' % nid)
    rec('  APPEND-ONLY against the blob    : %s' % append_only_blob)
    rec('  APPEND-ONLY against the working file : %s' % append_only_work)
    rec('  ### **THE PARTITION BLOCK IS UNCHANGED** : %s' % part_same)
    rec('  lines %d -> %d' % (before, after))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('  ### **AND WHAT FILING MEANS: THE RECORD NOW CARRIES THE ENTRY. ### IT DOES NOT EDIT ONE')
    rec('  ### PASSAGE, AND THE FIVE STILL READ AS THEY READ.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b358_errata_run', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
