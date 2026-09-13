# -*- coding: utf-8 -*-
"""b450_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P7).
### ### **NO KEYSTONE FILE IS OPENED BY THIS TOOL.** It reads the rule, the census's table, the matcher b395 wrote, b397's
### branch table, the registry's row formats, the reconciling acts' own lines, and b449's filed term changes."""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b450_extract.txt')
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
        return None, ''
    i, l = hit[0]
    rec('      %s:%d | %s' % (os.path.basename(path), i, l[:show]))
    return i, l


def main():
    rec('=' * 100)
    rec('b450 -- THE SURVEY. ### THE PRE-FACE READS. ### NO KEYSTONE OPENED.')
    rec('=' * 100)
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    CEN = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

    rec('')
    rec('(P1) b390`S RULE AT ITS OWN ADDRESS, VERBATIM -- THE SENTENCE THAT STATES IT AND THE SENTENCE THAT APPLIES IT.')
    i, l = quote(OT, 'the rule taken from the order’s own words is *read whole at the canonical drive*', 'P1 b390 rule', 60)
    if i:
        for part in re.split(r'(?<=\.) (?=\*\*|The )', l):
            if 'take the one whose terminals the drive can reach' in part or 'The census’s own release-blocking line settles it' in part:
                rec('        > %s' % part.strip())
    quote(OT, '### **b390 — THE FIRST PROOFREADING PASS (2026-09-09)**', 'P1 b390 heading')
    quote(os.path.join(D, 'b394_the_reconciliation_batched.txt'), 'TAKE THOSE WHOSE TERMINALS THE DRIVE CAN REACH', 'P1 b394 wording')

    rec('')
    rec('(P2) THE CENSUS`S KEYSTONE TABLE AND ITS ERA WORK-LIST, AT THEIR LINES.')
    quote(CEN, '### **THE SIXTEEN KEYSTONES**', 'P2 table heading')
    n = 0
    for k, ln in enumerate(io.open(CEN, encoding='utf-8').read().splitlines(), 1):
        if 73 <= k <= 88 and ln.startswith('| `'):
            n += 1
            rec('      THE_KEYSTONE_CENSUS.md:%d | %s' % (k, ln[:110]))
    rec('      table rows read : %d' % n)
    quote(CEN, '### **(c) THE CURRENCY PICTURE', 'P2 work-list heading')
    for k, ln in enumerate(io.open(CEN, encoding='utf-8').read().splitlines(), 1):
        if 117 <= k <= 126 and ln.startswith('|'):
            rec('      THE_KEYSTONE_CENSUS.md:%d | %s' % (k, ln[:230]))

    rec('')
    rec('(P3) b395`S WIDENED MATCHER, AS CODED, AND ITS PARTITION.')
    X = os.path.join(T, 'b395_extract.py')
    quote(X, "V1 = re.compile(r'`(SIDE-[a-z0-9-]+)`')", 'P3 narrow')
    quote(X, "V2 = re.compile(r'`?(SIDE-[A-Za-z0-9][A-Za-z0-9-]*)`?')", 'P3 wide')
    quote(X, "NOTAREPO = ('SIDE-kernel-session-notes',)", 'P3 not-a-repo')
    quote(os.path.join(D, 'b395_components.txt'), '### residue, HAND-READ and NOT counted : SIDE-internal', 'P3 residue 1')
    quote(os.path.join(D, 'b395_components.txt'), '### residue, HAND-READ and NOT counted : SIDE-Exclusion', 'P3 residue 2')
    quote(os.path.join(D, 'b395_components.txt'), 'it names 10 repository(ies) the drive holds AS GIT REPOSITORIES', 'P3 reach test')
    quote(os.path.join(D, 'b395_components.txt'), '### **NAMES NO TERMINAL     1**', 'P3 partition')

    rec('')
    rec('(P4) b397`S BRANCHES, COUNTED BOTH WAYS, AND THE UNLANDED LIST.')
    B = os.path.join(D, 'b397_closing.txt')
    quote(B, 'SIDE-kernel            derivative-engine', 'P4 the one live')
    quote(B, 'SIDE-lv-conservation   word-pairing-interface     0      3       True    research', 'P4 residue branch merged')
    quote(B, '### **FULLY MERGED, CARRYING NOTHING `main` LACKS : `8`.**', 'P4 eight merged')
    quote(B, '**`exactly_c1_derives`**  (theorem, `Kernel/DerivativeEngine.lean`)', 'P4 decl 1')
    quote(B, '**`onLine_doubleZero_iff_imDeriv_zero`**', 'P4 decl 2')
    quote(B, 'no_onLine_double_iff_transversal', 'P4 decl 3')
    quote(B, 'derivGrade', 'P4 decl 4')

    rec('')
    rec('(P5) THE RECONCILING ACTS, BY THEIR OWN LINES; AND THE REGISTRY`S TWO ROW FORMS.')
    quote(OT, '**THREE KEYSTONES READ IN ONE ACT, CHOSEN BY `b390`’S RULE AND NOTHING ADDED TO IT**', 'P5 b394 trail', 60)
    quote(os.path.join(D, 'b394_the_reconciliation_batched.txt'), '### ### **THE THREE : `GRH_CASCADE`, `FOUNDATIONS_OF_THE_SIDE_PROGRAMME`, `SILENCE_STAGES_DEALIGNMENT`**', 'P5 b394 three')
    quote(os.path.join(D, 'b394_the_reconciliation_batched.txt'), '`4` OF THE CENSUS`S `16` KEYSTONES ARE NOW RECONCILED', 'P5 b394 four of sixteen')
    quote(os.path.join(T, 'b394_extract.py'), "m = re.match(r'\\|\\s*([0-9][^|]*?)\\s*\\|\\s*([^|]*?)\\s*\\|\\s*`([^`]+\\.md)`\\s*\\|'", 'P5 registry row form')
    quote(os.path.join(T, 'b394_extract.py'), "m = re.search(r'Row \\*\\*([0-9][^*]*?)\\*\\* \\(`([^`]+)`\\): version (?:reconciled )?'", 'P5 registry update form')
    quote(os.path.join(D, 'b391_components.txt'), 'IS SUPERSEDED IS A CURRENCY ITEM, NOT A PHANTOM**', 'P5 b391 currency ruling')
    quote(OT, '**THE WIDENED CHECK REPAIRED NOTHING, AND THAT IS THE ANSWER.**', 'P5 b391 trail', 60)
    out = subprocess.run(['git', '-C', PP, 'log', '--format=%h %s', '--since=2026-09-09', '--', 'phase1.5', 'phase2', 'day1'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.splitlines()
    rec('      PLACE-papers commits touching phase1.5/phase2/day1 since 2026-09-09 (subjects only) : %d' % len(out))
    for s in out[:40]:
        rec('        %s' % s[:130])

    rec('')
    rec('(P6) THE FILING: b449`S TERM CHANGES AND THE OUTLIER`S TRAIL ENTRY.')
    quote(os.path.join(D, 'b449_components.txt'), '### step 1 : gross/net 5.000', 'P6 b449 step 1')
    quote(os.path.join(D, 'b449_components.txt'), 'by step 2 it has fallen 20.0-fold', 'P6 b449 twentyfold')
    quote(os.path.join(D, 'b448_components.txt'), '### (c3), the channels cancelling : REFUTED', 'P6 b448 c3')
    quote(os.path.join(D, 'b447_components.txt'), '### (c2) THE GRID`S ALIGNMENT WITH A FEATURE OF IT', 'P6 c2')
    quote(OT, '<!-- b449 the (R61) record ratified, and the outlier`s integrand at its aim -->', 'P6 last trail mark')

    rec('')
    rec('(P7) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '450'], capture_output=True,
                         text=True, encoding='utf-8', errors='replace').stdout
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
