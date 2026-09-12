# -*- coding: utf-8 -*-
"""b436_extract.py -- THE SURVEY FOR SITE (iv), THE WINDOW. ### **WRITTEN BEFORE THE FACE.**

### ### **EVERY ANCHOR IS READ AT ITS OWN FILE AND PRINTED.** ### A miss is printed, never patched,
### and the act's own miss count is the first thing the face reads.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b436_extract.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
READS = [0]
MISS = []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def wrap(s, n=92):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def grab(path, needle, before=0, after=0, label=None):
    """### **READ AT A FILE AND A LINE, OR PRINT A MISS.** ### Returns the matched block."""
    READS[0] += 1
    txt = read(path)
    lines = txt.splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            lo, hi = max(0, i - before), min(len(lines), i + after + 1)
            return (os.path.basename(path), i + 1, lines[lo:hi])
    MISS.append('%s : %r NOT LOCATED' % (os.path.basename(path), (label or needle)[:70]))
    return (os.path.basename(path), 0, [])


def show(path, needle, before=0, after=0, label=None, indent='      '):
    fn, ln, block = grab(path, needle, before, after, label)
    if not block:
        rec('%s### **NOT LOCATED** : %s in %s' % (indent, (label or needle)[:70], fn))
        return []
    rec('%s%s:%d' % (indent, fn, ln))
    for b in block:
        for chunk in wrap(b.strip(), 88):
            rec('%s  | %s' % (indent, chunk))
    return block


def main():
    rec('=' * 100)
    rec('b436 -- THE WITNESS ARC AT SITE (iv), THE WINDOW. ### THE SURVEY.')
    rec('=' * 100)

    # ------------------------------------------------------------------------------------------
    head(0, "THE DIFFERENCE THIS SITE CARRIES, STATED BEFORE ANY CANDIDATE.")
    rec('  ### The order fixes it and the record bears it out: ### **THIS SITE`S CELL READS')
    rec('  ### ### `UNSTATED`, NOT `NONE KNOWN`** -- because the shared-witness form does not')
    rec('  ### transpose here at all. ### Its record holds MEASURED VALUES, not an existential.')
    rec('  ### ### **SO THE OBJECT ENUMERATED IN COMPONENT 2 IS A UNIFORM BOUND**, and not a')
    rec('  ### shared witness in the family`s parameter space.')

    head(1, "THE SITE`S OWN CELL, VERBATIM.")
    led = os.path.join(PP, 'FACES_LEDGER.md')
    txt = read(led)
    READS[0] += 1
    m = re.search(r'\*\*`\(iv\)` — KIND: NOT EMPTY\. WITNESS: `UNSTATED`\.\*\*(.{0,700}?)###', txt, re.S)
    if not m:
        MISS.append('FACES_LEDGER.md : the (iv) WITNESS cell NOT LOCATED')
        rec('      ### **NOT LOCATED** : the (iv) WITNESS cell')
    else:
        rec('      FACES_LEDGER.md, row U1, the `(iv)` WITNESS cell:')
        for chunk in wrap('(iv) — KIND: NOT EMPTY. WITNESS: UNSTATED.' + m.group(1), 88):
            rec('        | %s' % chunk)
    rec('')
    rec('      and the site`s own entry, as b401 wrote it:')
    m2 = re.search(r'\*\*\(iv\) THE PRIME CONSTITUENT AT A WIDENED SUPPORT\*\*(.{0,900}?)###', txt, re.S)
    READS[0] += 1
    if not m2:
        MISS.append('FACES_LEDGER.md : the (iv) entry NOT LOCATED')
        rec('      ### **NOT LOCATED** : the (iv) entry')
    else:
        for chunk in wrap('(iv) THE PRIME CONSTITUENT AT A WIDENED SUPPORT' + m2.group(1), 88):
            rec('        | %s' % chunk)

    head(2, "b405`S AND b406`S REASONS FOR `UNSTATED`.")
    rec('    ### **b405 SET THE CELL.** ### Its reason is the transposition failure:')
    show(led, 'a uniform bound is not an object in the family', 0, 0,
         label="b405's reason: a uniform bound is not an object in the parameter space")
    rec('')
    rec('    ### **b406 TESTED THAT REASON AND GAVE IT ONE MORE CLAUSE**, correcting its')
    rec('    ### predecessor without rewriting it:')
    show(os.path.join(D, 'b406_the_sites_without_an_existential.txt'),
         'TEN VALUES', 0, 6, label="b406 on (iv)'s ten values")
    rec('')
    show(os.path.join(D, 'b406_the_sites_without_an_existential.txt'),
         'SO `b405`', 0, 3, label="b406's verdict on b405's cells")

    head(3, "b401`S CONFIRMED ABSENCE, AND ITS THREE GROUNDS.")
    b401 = os.path.join(D, 'b401_components_run.txt')
    rec('    ### **WHAT b401 LOCATED:**')
    show(b401, 'LAGARIAS THEOREM 6.1, AT PAGE INDEX', 0, 9, label='the located candidate')
    rec('')
    rec('    ### **AND WHY IT IS NOT THE MISSING ELEMENT -- THREE GROUNDS, EACH NAMED:**')
    for needle, lbl in (('(i) WRONG FAMILY', 'ground (i)'),
                        ('(ii) WRONG COMPARISON QUANTITY', 'ground (ii)'),
                        ('(iii) ITS HYPOTHESIS IS NOT OF A KIND', 'ground (iii)')):
        show(b401, needle, 0, 4, label=lbl)
        rec('')
    rec('    ### ### **THE ENUMERATION BELOW BUILDS ON THIS ABSENCE AND DOES NOT REPEAT ITS')
    rec('    ### ### SEARCH.**')

    head(4, "THE OPENING POPULATION, EACH READ AT ITS SOURCE.")
    rec('    ### [P2] THE SOURCE`S THEOREM 6.11, AND ITS BOUNDED CORRECTION TERM:')
    show(b401, 'THEOREM 6.11', 0, 4, label='Theorem 6.11 and its correction term')
    rec('')
    rec('    ### [P3] THE SOURCE`S NAMED ONE-PRIME WIDENING -- NAMED AND NOT TAKEN:')
    show(b401, 'SOURCE`S MACHINERY RUNS TOWARD NARROW', 0, 2, label='the widening named, not taken')
    rec('')
    rec('    ### [P4] THE CORPUS`S OWN ONE-PRIME WINDOW:')
    w321 = os.path.join(D, 'b321_the_window_opened.txt')
    show(w321, 'At the ten cells above', 0, 3, label="b321's window")
    rec('')
    rec('    ### [P5] THE CRITERION ITSELF -- ### **AND IT CARRIES NO SUPPORT HYPOTHESIS:**')
    show(w321, 'THE CRITERION, QUOTED VERBATIM FROM PROPOSITION C.1', 0, 5,
         label='Proposition C.1 / (155)')
    rec('')
    rec('    ### [P6] THE SHRINKAGE LAW USED AT SITE (ii):')
    show(os.path.join(D, 'b427_components.txt'), 'B16', 0, 0, label="b427's B16 verdict")

    head(5, "THE TWO SIDES, AT THE RADII THE RECORD PRINTED. ### **BANKED FIGURES ONLY.**")
    rec('    ### **THE NORMALIZATION, QUOTED FROM THE EMITTING ACT** -- it governs everything')
    rec('    ### below, and the navigator`s paraphrase governs nothing:')
    show(w321, 'half-line normalization', 0, 2, label="b321's half-line normalization")
    rec('')
    rec('    ### and the identity the four channels sit in:')
    show(w321, 'the identity is', 0, 0, label="b321's identity Z = P - PR + A")
    rec('')
    rec('    ### **THE TEN CELLS, COPIED FROM b321`s OWN TABLE:**')
    READS[0] += 1
    # ### **THE BANK IS CRLF ON THIS MACHINE** (`core.autocrlf`, the very condition b435's census
    # ### found six separate cures for). ### A pattern anchored on a bare `\n` after the header
    # ### misses every row, and misses SILENTLY -- zero rows produce zero mismatches. ### The
    # ### line endings are normalised before the table is matched.
    tw = read(w321).replace(chr(13) + chr(10), chr(10))
    mm = re.search(r'a\s+W_inf\s+square\s+margin\s+PR \(primes\)\s+SUM_v W_v\n((?:\s+[0-9].*\n)+)', tw)
    rows = []
    if not mm:
        MISS.append('b321_the_window_opened.txt : the ten-cell table NOT LOCATED')
        rec('      ### **NOT LOCATED** : the ten-cell W_inf/PR table')
    else:
        rec('      %-7s %-16s %-16s %-12s' % ('a', 'W_inf (arch)', 'PR (primes)', '|PR|/W_inf'))
        for ln in mm.group(1).strip().splitlines():
            p = ln.split()
            if len(p) < 5:
                continue
            a, winf, pr = float(p[0]), float(p[1]), float(p[4])
            rows.append((a, winf, pr))
            rec('      %-7s %-16.9f %-16.9f %-12.3e' % (a, winf, pr, abs(pr) / winf))
    if rows:
        rec('')
        rec('      ### ### **W_inf FALLS %0.9f -> %0.9f ACROSS THE WINDOW.**'
            % (rows[0][1], rows[-1][1]))
        rec('      ### ### **|PR| GROWS %0.9f -> %0.9f ACROSS THE SAME WINDOW.**'
            % (abs(rows[0][2]), abs(rows[-1][2])))
        rec('      ### ### **THE RATIO |PR|/W_inf GROWS %0.3e -> %0.3e -- FOUR ORDERS.**'
            % (abs(rows[0][2]) / rows[0][1], abs(rows[-1][2]) / rows[-1][1]))
        rec('      ### **AND THE RECORD`S WINDOW ENDS AT a = %s.**' % rows[-1][0])
        json.dump([dict(a=a, w_inf=w, pr=p, ratio=abs(p) / w) for a, w, p in rows],
                  io.open(os.path.join(D, 'b436_two_sides.json'), 'w', encoding='utf-8'),
                  indent=1)
    rec('')
    rec('    ### **AND THE BUMP`S OWN NORMALIZATION, WHICH IS WHAT MAKES A `UNIFORM IN a`')
    rec('    ### CLAIM MEAN ANYTHING:**')
    show(os.path.join(ROOT, 'tools', 'b355_read.py'), 'w /= np.trapezoid(w, v)', 0, 1,
         label='the bump is L1-normalised')

    head(6, "THE PRIOR SITES` OWN BANKED JSON -- ### **READ, NEVER TYPED.**")
    tallies = {}
    for act, site in (('b424', '(i)'), ('b427', '(ii)'), ('b428', '(iii)')):
        p = os.path.join(D, '%s_candidates.json' % act)
        READS[0] += 1
        try:
            d = json.loads(read(p))
        except Exception as e:                                   # noqa: BLE001
            MISS.append('%s_candidates.json : unreadable (%s)' % (act, str(e)[:60]))
            rec('      ### **UNREADABLE** : %s_candidates.json' % act)
            continue
        tallies[act] = d.get('tally', {})
        rec('      %s  site %-5s candidates %-4s held %-3s kinds %d'
            % (act, site, len(d.get('candidates', [])), d.get('held'), len(d.get('tally', {}))))
        for k, v in sorted(d.get('tally', {}).items()):
            rec('              %-34s %s' % (k, v))
    union = sorted(set().union(*[set(t) for t in tallies.values()]) if tallies else [])
    rec('')
    rec('      ### ### **UNION OF KINDS ACROSS THE THREE EARLIER SITES : %d**' % len(union))
    for k in union:
        rec('          %s' % k)
    json.dump(dict(tallies=tallies, union=union),
              io.open(os.path.join(D, 'b436_prior_sites.json'), 'w', encoding='utf-8'), indent=1)

    head(7, "THE NAVIGATOR`S CANDIDATE -- ### **THE SEARCH, PRINTED. NOTHING DECIDED HERE.**")
    rec('    ### His words, from the banked paste, so the test is against what he wrote:')
    show(os.path.join(D, 'b436_ferry.txt'), 'elementary Chebyshev-Mertens bound', 0, 4,
         label="the navigator's candidate")
    rec('')
    rec('    ### **THE CORPUS SEARCH, BY THE BOUND`S OWN VOCABULARY:**')
    pats = [('Chebyshev psi', r'Chebyshev psi'), ('psi(x) <= or asymptotic', r'psi\(x\)\s*[=~<]'),
            ('Mertens (the theorem, not the conjecture)', r'Mertens'),
            ('von Mangoldt', r'von Mangoldt'), ('an explicit prime-power bound', r'Lambda\(n\)')]
    hits = {}
    for lbl, rx in pats:
        n, where = 0, []
        for root, _d, fs in os.walk(PP):
            if '.git' in root:
                continue
            for f in fs:
                if not f.endswith('.md'):
                    continue
                t = read(os.path.join(root, f))
                c = len(re.findall(rx, t, re.I))
                if c:
                    n += c
                    where.append(os.path.relpath(os.path.join(root, f), PP).replace(os.sep, '/'))
        hits[lbl] = (n, where[:4])
        rec('      %-42s %-5d in %s' % (lbl, n, ', '.join(where[:3]) or '-'))
    json.dump({k: v[0] for k, v in hits.items()},
              io.open(os.path.join(D, 'b436_search.json'), 'w', encoding='utf-8'), indent=1)
    rec('')
    rec('    ### ### **THIS PRINTS WHERE THE VOCABULARY OCCURS AND DECIDES NOTHING.** ### Whether')
    rec('    ### any of these is a STATED, UNCONDITIONAL, UNIFORM BOUND of the navigator`s shape,')
    rec('    ### and whether the documents carrying them are VERIFIED SOURCES or narrative, is')
    rec('    ### Component 2`s work and is done by hand-reading each hit at its own line.')

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
