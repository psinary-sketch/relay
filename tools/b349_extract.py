# -*- coding: utf-8 -*-
"""b349_extract.py -- THE EXTRACT STEP FOR THE ROOM, RELATIVE BEFORE EXTENDED. ### **EVERY READ, TO DISK.**

### ### **WHAT THIS ACT IS READING FOR.** ### The three incidents of the comparison-normalisation species, each at
### its own act, so the sortie's shared normaliser is built over the record rather than over a memory of it -- and so
### that the one the order names can be checked against what the record actually holds. ### The room's own figures at
### the acts that charted them: b334's aim map over both reaching widths, b343's finer grid and its finding that a
### minimum sat at the sealed interval's edge, b344's extension below that edge and its bracketed minimum with the
### standing sentence that a narrower room at a finer grid is a finer chart and not a trend. ### The desk item this
### leg tests, in the fold's own words. ### The seed builder's own lawfulness and phase conditions, since leg (b) may
### not chart a seed it has not checked. ### And the order's own sentences for this leg.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b349_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b349_ferry_2026-09-07.txt')

WANTED = [
    # ### ---- THE SPECIES THE SORTIE'S STEP ZERO CURES, EACH INCIDENT AT ITS OWN ACT
    ('b298 -- two checks agreed and neither of them saw it', d('b298_the_boundary_terminal.txt'),
     "### ### **THE ACT'S OWN EARLIER COMPARISONS DID NOT SEE IT, AND THAT IS THE PART WORTH FILING:**"),
    ('### the comparison that normalised the difference away', d('b298_the_boundary_terminal.txt'),
     '### the BOM), and the comparison against `git HEAD` was ### LINE-CONTENT ### , which normalises'),
    ('b309 -- a CRLF working file against an LF blob', d('b309_the_scaling_trace.txt'),
     '###   ### **(ii) IT COMPARED A CRLF WORKING FILE AGAINST AN LF BLOB.** ### `core.autocrlf` rewrites'),
    ('### named as the b298 family, and the BYTE half cured', d('b309_the_scaling_trace.txt'),
     '###     CLEAN. ### **THAT IS THE b298 FAMILY EXACTLY: A BYTE CHECK DEFEATED BY A BYTE NOBODY MEANT'),
    ('### both sides through one IMPORTED normaliser', d('b309_the_scaling_trace.txt'),
     '###     TO WRITE.** ### Both sides are now normalised through `b302_kernel.normalise`, IMPORTED and'),
    ('the byte-level normaliser that already exists', t('b302_kernel.py'),
     '    """### LEAN\'S STDOUT AS THE BANKED FILE HOLDS IT: LF ENDINGS, ONE TRAILING NEWLINE, NO BOM."""'),
    ('b348 -- the QUOTATION half, still open', d('b348_the_fold.txt'),
     '### ### **AND THE GATE REFUSED ONCE BEFORE IT PASSED**'),
    # ### ---- THE ROOM, AT THE ACTS THAT CHARTED IT
    ('b334 -- the aim map, the room charted over aims', d('b334_the_aim_map.txt'), 'the room'),
    ('b343 -- no crossing at both widths', d('b343_the_maps_next_reach.txt'), 'NO CROSSING'),
    ("b343 -- a minimum at the interval's edge", d('b343_the_maps_next_reach.txt'),
     "### **AND ONE OF THE TWO MINIMA SITS AT THE INTERVAL'S EDGE:** at `a = 40` it is interior (`gamma = 2.0`"),
    ('b344 -- the room extended below the edge and BRACKETED', d('b344_the_floor_priced.txt'), 'BRACKETED'),
    ('b344 -- a finer chart and not a trend', d('b344_the_floor_priced.txt'),
     'A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND'),
    ('b344 -- one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    # ### ---- THE DESK ITEM THIS LEG TESTS, IN THE FOLD'S OWN WORDS
    ("b348 -- the room's bracketed minimum as the located point of maximum tension", d('b348_the_fold.txt'),
     '### **THE LOCATED POINT OF MAXIMUM TENSION.**'),
    ('b348 -- a fold proves nothing', d('b348_the_fold.txt'),
     '### ### ### **A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES. ### IT PROVES NOTHING, DISCHARGES'),
    # ### ---- THE SEED'S OWN LAWFULNESS AND PHASE CONDITIONS, WHICH LEG (b) MAY NOT CHART WITHOUT
    ("b334's seed builder", t('b334_aimmap.py'), 'def seed_aimed('),
    ("### and the map's gate", t('b334_aimmap.py'), 'def gate('),
    ('b328 -- the sign condition is a window, not a threshold', d('b334_the_aim_map.txt'), '45'),
    # ---- THE ORDER
    ('the order -- step zero, the shared normaliser', FERRY,
     'STEP ZERO, this sortie only: one shared normaliser, imported by'),
    ('### the species it names', FERRY, 'quotation is compared \u2014 the b305/b348 species, twice banked and'),
    ('the order -- leg 1', FERRY, 'LEG 1 (b349) \u2014 THE ROOM, RELATIVE BEFORE EXTENDED.'),
    ('### the denominator fixed before any value', FERRY,
     'the room expressed relative to the size of'),
    ('### the artifact sentence, if the minimum moves', FERRY,
     'point of maximum tension was an artifact of absolute'),
    ('### (b) is conditional on (a)', FERRY,
     '(b) Only if (a) leaves the low-height minimum standing in the'),
    ('### a degenerate seed is reported, not charted', FERRY,
     'degenerate seed is reported as degenerate, not charted.'),
    ('### the navigator\'s (L1)', FERRY, '(L1) the'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b349_extract.py -- THE ROOM, RELATIVE BEFORE EXTENDED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
