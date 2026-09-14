# -*- coding: utf-8 -*-
"""b453_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE FOLD AT SPAN EIGHT.
### ### Quotations at their lines; no verdict string is verified here (that is the components' work)."""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b453_extract.txt')
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
    FND = os.path.join(PP, 'FINDINGS.md')
    DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    rec('=' * 100)
    rec('b453 -- THE SURVEY. ### THE FOLD AT SPAN EIGHT.')
    rec('=' * 100)
    rec('')
    rec('(P1) THE STANDING FOLD FORM, AT THE LAST FOLD.')
    quote(FND, '## THE WITNESS AND CHANNEL ARC, b433–b443 — THE FOLD', 'P1 b444 heading')
    quote(FND, '### The span, act by act, each verdict verified in its own closing bank', 'P1 table heading')
    quote(FND, '### The three columns, kept apart', 'P1 columns heading')
    quote(FND, '*Filed by b444 (relay `data/b444_fold.json`, `data/b444_the_fold.txt`).', 'P1 filed-by line', 80)
    quote(os.path.join(T, 'b444_components.py'), "ok = needle in txt", 'P1 exact-match verification')
    rec('')
    rec('(P2) THE DIGEST UNDER (R31), AND ITS LAST BLOCK.')
    quote(OT, '**And the orientation layer is refreshed under `(R31)`', 'P2 (R31) as carried', 80)
    quote(DIG, '<!-- b444 orientation refresh: the external-grading arc and the witness and channel arc -->', 'P2 digest last marker')
    rec('')
    rec('(P3) THE WORK-ORDER WHOSE TRIGGER THIS FOLD MEETS.')
    quote(FND, '**W-ORD-SPAN-HEADING.** `tools/b363_span.py` finds fold sections', 'P3 work-order', 60)
    quote(FND, '**Trigger:** the next act that opens the instrument lane, or the next fold, whichever comes first.', 'P3 trigger', 60)
    quote(os.path.join(D, 'b449_registration_2026-09-13.txt'), "(R62)` -- the instrument lane opens for one", 'P3 (R62) opened the lane at b449')
    quote(os.path.join(D, 'b449_desk_notes.txt'), 'W-ORD-SPAN-HEADING', 'P3 b449 carried it')
    rec('')
    rec('(P4) WHERE THE RECORD ENTERS ERRORS AS THEIR OWNERS`, AND THE WINDOW`S ENTRIES.')
    quote(OT, '#### Errors entered as their owners’', 'P4 the heading form')
    quote(OT, 'so he took a rounding level for a measured quantity and a domain of kind for a domain of radius', 'P4 b446 kind error', 60)
    quote(os.path.join(D, 'b447_registration_2026-09-12.txt'), "AN ERROR IN THE ORDER'S WORDING, ENTERED AS THE NAVIGATOR'S:", 'P4 b447')
    quote(os.path.join(D, 'b449_registration_2026-09-13.txt'), "TWO ERRORS IN THE ORDER'S WORDING, ENTERED AS THE NAVIGATOR'S:", 'P4 b449')
    quote(os.path.join(D, 'b452_registration_2026-09-14.txt'), "ITS DOMAIN IS A NETWORK'S REPRESENTATIONS.", 'P4 b452 R1 domain')
    for nm in ('error ledger', 'kind-check'):
        n = sum(1 for dp, dn, fn in os.walk(PP) for f in fn if f.endswith('.md') and '.git' not in dp and nm in io.open(os.path.join(dp, f), encoding='utf-8', errors='replace').read().lower())
        rec('      corpus .md files carrying %-14r : %d' % (nm, n))
    rec('')
    rec('(P5) THE RULINGS (R61)-(R64), WHERE THE RECORD HOLDS THEM.')
    quote(OT, '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->', 'P5 (R61) record')
    quote(os.path.join(D, 'b449_closing.txt'), 'THE (R61) RECORD : RATIFIED AT b449', 'P5 (R61) ratified')
    quote(os.path.join(D, 'b449_closing.txt'), 'THE INSTRUMENT LANE OPENED BY (R62) IS CLOSED', 'P5 (R62) closed')
    for r in ('(R63)', '(R64)'):
        hits = [f for f in os.listdir(D) if f.endswith('.txt') and r in io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()]
        rec('      relay data files carrying %s : %d %s' % (r, len(hits), hits[:4]))
    rec('')
    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '453'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
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
