# -*- coding: utf-8 -*-
"""b451_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P6).
### ### Quotations at their lines only. No reconciled set is unioned, no item is grouped, no keystone is opened."""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b451_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def quote(path, needle, label, show=170):
    try:
        ls = io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
    except Exception:
        ls = []
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, path, needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (os.path.basename(path), i, l[:show]))
    return i


def main():
    rec('=' * 100)
    rec('b451 -- THE SURVEY. ### THE PRE-FACE READS.')
    rec('=' * 100)
    rec('')
    rec('(P1) THE POPULATION AND THE THREE RECONCILING BANKS, AT THEIR LINES.')
    quote(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md'), '### **THE SIXTEEN KEYSTONES**', 'P1 census heading')
    quote(os.path.join(D, 'b390_the_proofreading_pass.txt'), 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'P1 b390 bank names its one')
    quote(os.path.join(D, 'b394_the_reconciliation_batched.txt'), '### ### **THE THREE : `GRH_CASCADE`, `FOUNDATIONS_OF_THE_SIDE_PROGRAMME`, `SILENCE_STAGES_DEALIGNMENT`**', 'P1 b394 bank names its three')
    quote(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt'), '**Eligible (11), in census order:**', 'P1 b450 bank names its eleven', 120)
    quote(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt'), '| 14 | `ENUMERA` | EXCLUDED |', 'P1 b450 bank excludes one')
    quote(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt'), '**The batch is complete: 11 of 11 read, no halt.**', 'P1 b450 complete', 80)
    rec('')
    rec('(P2) WHAT b395`S BANK SAYS THE UNREADABLE ONE NEEDS.')
    quote(os.path.join(D, 'b395_the_ceiling_answered.txt'), '`ENUMERA` names no terminal for any route to reach. ### **WHAT IT NEEDS', 'P2 b395 bank need')
    quote(os.path.join(D, 'b395_the_ceiling_answered.txt'), 'IS AN AUTHOR NAMING ITS TERMINAL.**', 'P2 b395 bank need tail')
    quote(os.path.join(D, 'b395_components.txt'), 'so there is nothing to settle and no clone would help', 'P2 b395 no clone')
    quote(os.path.join(D, 'b396_closing.txt'), 'NOT A READING PROBLEM', 'P2 b396 confirms')
    rec('')
    rec('(P3) b450`S ROUTED ITEMS, AT THEIR BANKED ADDRESSES (NOT GROUPED HERE).')
    quote(os.path.join(D, 'b450_components.txt'), 'THE REPAIRS ROUTED, COUNTED APART : 29', 'P3 routed header')
    quote(os.path.join(D, 'b450_components.txt'), '### ### **REPAIRS MADE : 3. ### REPAIRS ROUTED : 29.', 'P3 routed count')
    quote(os.path.join(D, 'b450_batch.json'), '"routed_items"', 'P3 routed items in the batch bank')
    quote(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt'), '**Routed, 29, each with the ruling it needs:**', 'P3 bank sentence', 90)
    rec('')
    rec('(P4) THE LORE MINTED AT b370, AND ITS CURRENT INCIDENTS.')
    LORE = os.path.join(TE, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')
    quote(LORE, '# ', 'P4 lore title')
    quote(LORE, '## The scope of this module', 'P4 lore scope heading')
    quote(os.path.join(D, 'b370_closing.txt'), '`PREDICATE_ONE_SHAPE`', 'P4 b370 mint')
    ls = io.open(LORE, encoding='utf-8').read().splitlines()
    rec('      PREDICATE_ONE_SHAPE.md lines : %d ; the last non-empty begins %r' % (len(ls), [x for x in ls if x.strip()][-1][:50]))
    rec('      TECHNE-Core last commit on it : %s' % subprocess.run(['git', '-C', TE, 'log', '--oneline', '-1', '--', 'modules/2026-09/PREDICATE_ONE_SHAPE.md'],
                                                                   capture_output=True, text=True).stdout.strip())
    rec('')
    rec('(P5) THE INCIDENTS THE FILING NAMES, AT THEIR BANKS.')
    quote(os.path.join(D, 'b391_components.txt'), 'NOBODY RE-MEASURED**, and its matcher is why: it required the version to follow', 'P5 b391 names b390`s version matcher', 150)
    quote(os.path.join(D, 'b395_the_ceiling_answered.txt'), 'BACKTICKED', 'P5 b395 on b394`s matcher')
    quote(os.path.join(D, 'b450_components.txt'), 'T2 as fixed on the face (first header cell exactly `claim`)', 'P5 b450 table-header test')
    quote(os.path.join(D, 'b450_components.txt'), 'S1 yield across the batch : 0 ; S2 yield : 8', 'P5 b450 citation matcher')
    rec('')
    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '451'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'STARTS AT|runs through|THE CURRENT SPAN|NOTHING WAS WRITTEN', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
