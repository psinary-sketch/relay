# -*- coding: utf-8 -*-
"""b117 -- THE SUPERLATIVE LEDGER'S RETROACTIVE SWEEP.

Judgment-free. Lists every absolute or superlative construction in the
record's shipped prose, with act number and verbatim text. ZERO interpretive
weight: this is an inventory, not a criticism and not evidence of anything.

Stems, as the ferry fixes them: most, deepest, finest, cleanest, first-ever,
strongest, best, thinnest.
"""
import io, os, re, glob, sys

sys.stdout.reconfigure(encoding='utf-8')

STEMS = ['most', 'deepest', 'finest', 'cleanest', 'first-ever',
         'strongest', 'best', 'thinnest']
PAT = re.compile(r'\b(' + '|'.join(STEMS) + r')\b', re.I)

# "most" appears constantly as an adverb ("most of", "at most", "almost").
# The sweep must not silently drop those; it separates them and REPORTS the
# count it set aside, so the reader can see what the filter did.
ADVERBIAL = re.compile(r'\b(at most|most of|almost|mostly|for the most part)\b', re.I)

REPORTS = sorted(glob.glob(r'D:\relay\reports\*.md'))
KEYSTONE = r'D:\MY-DOwnloads\PLACE-papers\phase2\method\THE_GLOBAL_SECTION.md'

ACT = re.compile(r'\bb(\d{2,3})\b')


def scan(path, label):
    hits, setaside = [], 0
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    for ln, line in enumerate(txt.splitlines(), 1):
        for m in PAT.finditer(line):
            span = line[max(0, m.start() - 60):m.end() + 90]
            if ADVERBIAL.search(line[max(0, m.start() - 12):m.end() + 12]):
                setaside += 1
                continue
            hits.append((label, ln, m.group(0).lower(), ' '.join(span.split())))
    return hits, setaside


def main():
    allhits, allset = [], 0
    for p in REPORTS:
        base = os.path.basename(p)
        h, s = scan(p, base)
        allhits += h
        allset += s
    h, s = scan(KEYSTONE, 'THE_GLOBAL_SECTION.md')
    allhits += h
    allset += s

    print("=" * 78)
    print("b117 -- THE SUPERLATIVE LEDGER, RETROACTIVE SWEEP")
    print("  scope: %d relay reports + the keystone" % len(REPORTS))
    print("  stems: %s" % ', '.join(STEMS))
    print("=" * 78)
    print("\n  TOTAL SUPERLATIVE CONSTRUCTIONS FOUND: %d" % len(allhits))
    print("  adverbial uses SET ASIDE and counted, not silently dropped: %d" % allset)
    print("     (at most / most of / almost / mostly / for the most part)")

    bystem = {}
    for _, _, st, _ in allhits:
        bystem[st] = bystem.get(st, 0) + 1
    print("\n  BY STEM:")
    for st in STEMS:
        print("    %-12s %4d" % (st, bystem.get(st, 0)))

    print("\n  THE LEDGER (file : line : stem : verbatim span)")
    print("  " + "-" * 74)
    for f, ln, st, span in allhits:
        print("  %s : %d : %s" % (f, ln, st))
        print("      \"%s\"" % span)

    print("\n  ZERO INTERPRETIVE WEIGHT. This is an inventory. No entry is a")
    print("  criticism, no entry is evidence, and no entry is re-graded by being")
    print("  listed. The convention standing forward: superlatives in shipped")
    print("  prose enter the ledger AT SHIPPING.")


main()
