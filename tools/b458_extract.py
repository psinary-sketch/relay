# -*- coding: utf-8 -*-
"""b458_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE RULING ENTRIES.
### ### Addresses, pins, quotations and a FILE INVENTORY only.
### ### **IT DOES NOT SEARCH THE RELAY FILES FOR RULING TEXT -- THAT IS COMPONENT 1's MEASUREMENT.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b458_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def lines(path):
    return io.open(path, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '').split(chr(10))


def at(path, n, label, show=150):
    """### READ A LINE BY ITS NUMBER AND PRINT IT. ### A MISSING LINE IS A MISS, NEVER A BLANK."""
    ls = lines(path)
    if n < 1 or n > len(ls):
        MISSES.append((label, os.path.basename(path), n))
        rec('      ### MISS : %s -- %s:%d out of range (%d lines)' % (label, os.path.basename(path), n, len(ls)))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), n, ls[n - 1].strip()[:show]))
    return ls[n - 1]


def find(path, needle, label, show=150):
    ls = lines(path)
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def main():
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    rec('=' * 100)
    rec('b458 -- THE SURVEY. ### RULINGS (R65) THROUGH (R68) ENTERED AS RECORDS.')
    rec('=' * 100)
    rec('')

    rec('(P1) THE FOUR OPEN_TRAILS MENTIONS THE ORDER NAMES, READ AT THEIR OWN LINE NUMBERS.')
    for n in (6861, 6899, 6913, 6930):
        at(OT, n, 'P1 mention %d' % n)
    rec('      OPEN_TRAILS.md total lines : %d' % (len(lines(OT)) - 1))
    rec('      ### **THE SEAT HAS ALREADY READ THESE FOUR LINES, IN THE RE-SYNC TURN THAT PRECEDED THIS FERRY.**')
    rec('      ### **DECLARED, NOT CONCEALED:** the re-sync reported that no fuller text sits in OPEN_TRAILS.')
    rec('')

    rec('(P2) THE (R61) ENTRY, WHOSE FORM THE ORDER NAMES. ### READ FOR ITS SHAPE, NOT ITS CONTENT.')
    for nd in ('<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->',
               '### (R61) — the failure-mode partition gets a trigger, not a shelf — filed 2026-09-13',
               '**RULING (R61), THE AUTHOR’S, RATIFIED AND STRIKEABLE:',
               '**Trigger: a source enters the record under the import bar'):
        find(OT, nd, 'P2 (R61) form')
    rec('      ### THE FORM, READ OFF IT: comment marker ; `### (Rnn) — <title> — filed <date>` ;')
    rec('      ### a bolded RULING sentence ; the occasion with addresses ; a body ; a closing scope line in italics.')
    rec('')

    rec('(P3) THE CITING LINES OUTSIDE OPEN_TRAILS.')
    at(os.path.join(PP, 'ERRATA.md'), 367, 'P3 ERRATA:367')
    at(os.path.join(PP, 'ERRATA.md'), 385, 'P3 ERRATA:385')
    R = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
    at(R, 204, 'P3 RESIDUE:204')
    at(R, 211, 'P3 RESIDUE:211')
    at(os.path.join(PP, 'README.md'), 17, 'P3 README:17')
    rec('')

    rec('(P4) THE WORK-ORDER THE (R69) ENTRY CLOSES, AT ITS ADDRESS.')
    find(OT, '**W-ORD-MIRROR-ZIP-NAME.**', 'P4 the work-order row')
    rec('      ### **IT SITS INSIDE b449`s TRAIL RECORD, WHICH IS A CLOSED BANK.**')
    rec('      ### **READING DECLARED HERE:** the closure is carried by the (R69) entry, which names and quotes')
    rec('      ### the row at its address; b449`s line is NOT edited. ### b456`s ERA ANNOTATION precedent')
    rec('      ### (INVARIANCE_BARRIERS.md:695) is the same shape: annotate live, cite the frozen line.')
    find(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'), '<!-- b456 ERA ANNOTATION, 2026-09-14 -->', 'P4 the era-annotation precedent')
    rec('')

    rec('(P5) THE RELAY FILE INVENTORY FOR b455-b457. ### **NAMES AND SIZES ONLY; NOT SEARCHED.**')
    inv = sorted(f for f in os.listdir(D) if re.match(r'^b45[5-7]_', f))
    for f in inv:
        rec('      %-46s %8d bytes' % (f, os.path.getsize(os.path.join(D, f))))
    rec('      ### FILES IN THE COMPONENT-1 SEARCH SCOPE : %d' % len(inv))
    rec('      ### **ONE PRIOR READ DECLARED:** in the re-sync turn the seat read `b457_ferry.txt` lines 1-20')
    rec('      ### and its last 5 lines. ### **THAT HEAD CARRIES (R66)`s FULLER TEXT, WHICH THE SEAT HAS')
    rec('      ### THEREFORE ALREADY SEEN.** ### (N1) is scored knowing this, and the declaration is the point:')
    rec('      ### one of the four instances was observed before the face, and it is named rather than counted unseen.')
    rec('      ### No other b455-b457 relay file has been opened for ruling text.')
    rec('')

    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '458'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|UNPARSED|next span STARTS AT|runs through', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
