# -*- coding: utf-8 -*-
"""b449_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P6).
### ### Lines quoted with their numbers. ### **NOTHING ABOUT THE OBJECT IS COMPUTED HERE**: no bank is counted, no
### test function is formed, no channel is evaluated. Code lines are read; banked scalars are quoted."""
import glob
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
OUT = os.path.join(D, 'b449_extract.txt')
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
    rec('b449 -- THE SURVEY. ### THE PRE-FACE READS, RE-TAKEN FROM THEIR SOURCES.')
    rec('=' * 100)
    OT = os.path.join(PP, 'OPEN_TRAILS.md')

    rec('')
    rec('(P1) THE (R61) RECORD, AT ITS LINES, AND THE SIX BANKS IT NAMES (PATHS AND BYTES ONLY; NOT COUNTED HERE).')
    s = quote(OT, '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->', 'P1 record mark')
    ls = io.open(OT, encoding='utf-8').read().splitlines()
    if s:
        e = s
        while e < len(ls) and not ls[e].startswith('*The partition row in `FINDINGS.md` is not edited'):
            e += 1
        rec('      the record runs OPEN_TRAILS.md:%d-%d (%d lines) ; lines after it : %d' % (s, e + 1, e + 2 - s, len(ls) - e - 1))
    quote(OT, '**What the trigger is waiting for, in the arc’s own count**', 'P1 count sentence', 60)
    for p in ('b424_candidates.json', 'b427_candidates.json', 'b428_candidates.json', 'b436_candidates.json',
              'b442_site_v.json', 'b443r_site_vi.json'):
        fp = os.path.join(D, p)
        rec('      %-24s bytes %s' % (p, os.path.getsize(fp) if os.path.exists(fp) else '### ABSENT'))
    quote(os.path.join(D, 'b443r_the_arc_product.txt'), '**The class boundary, per site, corrected:**', 'P1 b443 per-site report', 60)

    rec('')
    rec('(P2) THE MIRROR: b448`S CHECK, THE ZIP NOW ON DISK, AND HOW THE BUILDER NAMES IT.')
    quote(os.path.join(D, 'b448_closing.txt'), 'mirror           : CLEAN ON ALL THREE CLAUSES at b1656b1', 'P2 b448 closing')
    quote(os.path.join(D, 'b448_r61_mirror.txt'), 'manifest declares source HEAD', 'P2 r61 mirror head')
    MB = os.path.join(T, 'mirror_build.ps1')
    quote(MB, "param([string]$DateTag = (Get-Date -Format 'yyyy-MM-dd'))", 'P2 builder param')
    quote(MB, '$zip = "D:\\MY-DOwnloads\\mirror-refresh-$DateTag.zip"', 'P2 builder zip name')
    quote(MB, 'if (Test-Path $zip) { Remove-Item $zip -Force }', 'P2 builder overwrite')
    tagged = sorted(os.path.basename(x) for x in glob.glob(os.path.join(DL, 'mirror-refresh-2026-09-0*b3*.zip')))
    rec('      zips on disk whose tag carries an act suffix (September) : %d, e.g. %s' % (len(tagged), tagged[:3]))
    z = os.path.join(DL, 'mirror-refresh-2026-09-13.zip')
    rec('      mirror-refresh-2026-09-13.zip present : %s' % os.path.exists(z))

    rec('')
    rec('(P3) THE LOOM`S APPENDER AND ITS LAST ENTRY.')
    quote(os.path.join(T, 'b244_loom_append.py'), 'APPEND ONE HUNK TO THE LOOM', 'P3 appender')
    quote(os.path.join(T, 'b244_loom_append.py'), 'PREFIX UNCHANGED (pure insertion)', 'P3 prefix proof')
    lm = [l for l in io.open(os.path.join(PP, 'VERIFICATION_LOOM.md'), encoding='utf-8-sig').read().splitlines()
          if re.match(r'<!-- b\d+ loom entry -->', l)]
    rec('      loom entry markers : %d ; the last %s' % (len(lm), lm[-1] if lm else None))

    rec('')
    rec('(P4) THE CHAIN`S CODE PATH FOR THE PRIME CHANNEL`S INTEGRAND -- CODE LINES, NOT VALUES.')
    AT = os.path.join(T, 'e16', 'carto_atlas.py')
    SM = os.path.join(T, 'b317_smear.py')
    SQ = os.path.join(T, 'b318_square.py')
    WI = os.path.join(T, 'b321_window.py')
    quote(AT, 'w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))', 'P4 bump profile')
    quote(SM, 'MZ_EXPONENTS = (1.0, 0.5, 0.25)', 'P4 seed widths')
    quote(SQ, 'w = np.interp(u, f.v, f.w, left=0.0, right=0.0)', 'P4 autocorr seed read')
    quote(SQ, 'u = np.linspace(-L, L, int(nv))', 'P4 autocorr u grid')
    quote(SQ, 'v = np.linspace(-2.0 * L, 2.0 * L, ac.size)', 'P4 autocorr v grid')
    quote(WI, 'L = float(v[-1])', 'P4 prime reach')
    quote(WI, 'if ln <= L:', 'P4 prime inclusion')
    quote(WI, 'val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, v, w))', 'P4 prime integrand read')
    quote(os.path.join(T, 'b447_components.py'), 'g = SM.mean_zero_variant(a)', 'P4 b447 code path g')
    quote(os.path.join(T, 'b447_components.py'), 'f = SQ.autocorrelation(g, nv=NV3)', 'P4 b447 code path f')
    a = json.load(io.open(os.path.join(D, 'b447_doubling.json'), encoding='utf-8'))['4.123106']['a']
    rec('      the banked a : %r ; sqrt(17) = %.12f ; a - sqrt(17) = %+.4e   ### arithmetic on the cell`s label, not the object'
        % (a, math.sqrt(17), a - math.sqrt(17)))

    rec('')
    rec('(P5) THE CANDIDATES AS b447 PRICED THEM, AND b448`S NARROWING.')
    C447 = os.path.join(D, 'b447_components.txt')
    quote(C447, "### (c1) THE INTEGRAND`S OWN BEHAVIOUR AT THAT RADIUS", 'P5 c1')
    quote(C447, "### (c2) THE GRID`S ALIGNMENT WITH A FEATURE OF IT", 'P5 c2')
    quote(C447, 'a grid offset the chain does not take as a parameter', 'P5 c2 price')
    quote(os.path.join(D, 'b448_components.txt'), 'THE GROWTH BETWEEN THE FIRST TWO LEVELS, BY THE FACE`S RULE', 'P5 b448 growth')
    quote(os.path.join(D, 'b448_components.txt'), '### ### **THE MEASUREMENT STAYS OPEN, NARROWED TO THE PRIME CHANNEL.**', 'P5 b448 measurement')
    quote(os.path.join(D, 'b447_doubling.json'), '"seconds"', 'P5 b447 wall at 65537')

    rec('')
    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '449'], capture_output=True,
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
