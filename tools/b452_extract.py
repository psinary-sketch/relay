# -*- coding: utf-8 -*-
"""b452_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P6).
### ### Quotations at their lines, bank FIELD NAMES only. No candidate is classified here and no class text is read per candidate."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b452_extract.txt')
L, MISSES = [], []
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]

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
    rec('b452 -- THE SURVEY. ### THE PRE-FACE READS.')
    rec('=' * 100)
    RB = os.path.join(PP, 'phase2', 'method', 'REPARAMETERIZATION_BARRIERS_v0_1.md')
    EE = os.path.join(PP, 'day1', 'Exhaustive_Enumeration.md')
    OTA = os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md')
    rec('')
    rec('(P1) THE REPARAMETERIZATION KEYSTONE, AT ITS ADDRESSES.')
    quote(RB, '## 3. The method class D', 'P1 method class heading')
    quote(RB, '| Method | In D for | Why |', 'P1 table header')
    quote(RB, '| Behavioral / functional evaluation | GL(n) |', 'P1 row GL(n)')
    quote(RB, '| Representation norms, distances, cosine similarity | O(n) | isometry |', 'P1 row O(n)')
    quote(RB, '## 4. The witness pair', 'P1 witness pair heading')
    quote(RB, '## 5. The theorem, and what it says', 'P1 theorem heading')
    quote(RB, '## 7. What this note does not claim', 'P1 non-claims heading')
    quote(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md'), '| `REPARAMETERIZATION_BARRIERS_v0_1` | 2026-08-06 | the two-kinds windows verdict |', 'P1 census pairs it with the verdict')
    rec('')
    rec('(P2) THE TWO-KINDS WINDOWS VERDICT, AT ITS ADDRESSES.')
    quote(EE, '### ERA ANNOTATION (2026-08-14) — bearing on the two-kinds windows, now compiled', 'P2 annotation heading')
    quote(EE, 'the largest **prime-free** window is `(1/2, 2)`, and the largest **one-prime** window is `(1/3, 3)`', 'P2 the two windows', 60)
    quote(OTA, 'support truncation controls width exactly as `2 log a`. `DISTINCT` between the two kinds', 'P2 archive: support-kind', 60)
    quote(OTA, 'The two-kinds windows verdict stands beside it: the support-kind unification is already in hand', 'P2 archive: the verdict stands', 60)
    rec('')
    rec('(P3) THE KIND OF EMPTINESS b404 MINTED FOR THIS QUESTION.')
    B404 = os.path.join(D, 'b404_the_fifth_and_sixth_sites.txt')
    quote(B404, '### **KIND (a) -- EMPTY BECAUSE THERE IS NOTHING TO RANGE OVER.**', 'P3 kind a')
    quote(B404, '### **KIND (b) -- EMPTY BECAUSE THE AVAILABLE UNIFORMITY RANGES OVER A CLASS THAT DOES NOT', 'P3 kind b')
    rec('')
    rec('(P4) THE SIX SITES, BY THE ACTS THAT NAMED THEM.')
    quote(os.path.join(D, 'b355_sortie_closing.txt'), '### **THE FACES LEDGER GAINS ONE ROW, THROUGH ITS OWN WRITER: `U1`, THE UNIFORMITY OBSTRUCTION.**', 'P4 b355 names three')
    quote(os.path.join(D, 'b355_sortie_closing.txt'), '### The shape common to three places where the record needs a statement UNIFORM in an index and holds', 'P4 b355 the shape')
    quote(os.path.join(D, 'b401_the_absent_element_searched.txt'), '**SCOPE: THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE ENTERED.**', 'P4 b401 fourth', 90)
    quote(B404, "**SCOPE: THE FIFTH SITE ENTERED, THE SIXTH ENTERED, AND THE ROW'S LAW STRAINED.**", 'P4 b404 fifth and sixth', 90)
    FL = os.path.join(PP, 'FACES_LEDGER.md')
    quote(FL, '| U1 | U1 -- the uniformity obstruction: three places where the record needs a statement UNIFORM in an index', 'P4 row U1', 120)
    out = subprocess.run(['git', '-C', PP, 'log', '--format=%h %ad %s', '--date=short', '-S', 'U1 -- the uniformity obstruction', '--', 'FACES_LEDGER.md'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip().splitlines()
    rec('      FACES_LEDGER.md commits introducing row U1 : %s' % out[-1:] )
    for s, why in (('(iv) THE PRIME CONSTITUENT', 'P4 (iv)'), ('(v) ', 'P4 (v)'), ('(vi) ', 'P4 (vi)')):
        o = subprocess.run(['git', '-C', PP, 'log', '--format=%h %ad %s', '--date=short', '-S', s, '--', 'FACES_LEDGER.md'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip().splitlines()
        rec('      first commit carrying %-28s : %s' % (repr(s), (o[-1] if o else 'NONE')[:110]))
    quote(os.path.join(PP, 'OPEN_TRAILS.md'), '**The next arc, one act per site of row U1, checkpointed after each:**', 'P4 the arc takes U1`s sites', 80)
    rec('')
    rec('(P5) THE SIX BANKS: FIELD NAMES AND THE KIND TALLY ONLY.')
    for s, p in SITES:
        d = json.load(io.open(os.path.join(D, p), encoding='utf-8'))
        cs = d['candidates']
        rec('      (%s) %-24s candidates %2d ; fields %s ; step fields %s' % (s, p, len(cs), sorted(cs[0].keys()),
                                                                         sorted(cs[0]['steps'][0].keys()) if cs[0].get('steps') else '-'))
    agg = json.load(io.open(os.path.join(D, 'b443r_site_vi.json'), encoding='utf-8'))['aggregate']
    rec('      b443r_site_vi.json aggregate : %s' % agg)
    rec('')
    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '452'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
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
