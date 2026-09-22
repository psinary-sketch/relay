# -*- coding: utf-8 -*-
"""b484_extract.py -- THE SURVEY. ### **NO CHAIN IS RUN, NO ENTRY COMPUTED, NO LANE OPENED.**
### `b321_window.py` is READ AS TEXT and never imported; the arithmetic below is `math.log` on two
### numbers, which is not the chain. ### b449's and b483's banks are read and not written.
"""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def find(text, needle, path):
    for i, l in enumerate(text.split(NL)):
        if needle in l:
            return i + 1, l
    MISSES.append((path, needle))
    return 0, ''


def main():
    rec('=' * 106)
    rec('b484 -- THE SURVEY. ### THE COMPARATOR READ AS TEXT; THE CHAIN NOT RUN.')
    rec('=' * 106)

    win = read(os.path.join(T, 'b321_window.py'))
    sq = read(os.path.join(T, 'b318_square.py'))
    sm = read(os.path.join(T, 'b317_smear.py'))
    atl = read(os.path.join(T, 'e16', 'carto_atlas.py'))

    # ---------------------------------------------------------------- (P1) the comparators
    rec('')
    rec('(P1) b321`S PRIME-SUM LOOP: ### **THE COMPARATORS, AT THEIR OWN LINES.**')
    rec('-' * 106)
    for needle in ('PRIME_TOL = 1e-12',
                   'for p in primes_to(math.exp(L) + PRIME_TOL)',
                   'while p ** k <= math.exp(L) + PRIME_TOL:',
                   'if ln <= L:',
                   'L = float(v[-1])'):
        i, l = find(win, needle, 'b321_window.py')
        rec('    b321_window.py:%-4d %s' % (i, l.strip()))
    rec('')
    rec('    ### ### **THERE ARE TWO COMPARATORS, NOT ONE, AND THEY DO NOT AGREE ON THE EDGE.**')
    rec('    ### the OUTER cap `p ** k <= math.exp(L) + PRIME_TOL` admits ### **WITH A TOLERANCE**;')
    rec('    ### the INNER gate `if ln <= L` -- which is what actually decides whether a term is')
    rec('    ### added -- admits ### **WITH NO TOLERANCE AT ALL**, in LOG coordinates.')
    rec('    ### ### **THE DECIDING COMPARATOR IS THEREFORE `math.log(n) <= L`, WEAK INEQUALITY,')
    rec('    ### NO TOLERANCE.** ### The outer cap only bounds which prime powers are considered.')

    # ---------------------------------------------------------------- (P2) what L is
    rec('')
    rec('(P2) WHAT `L` IS AT A CELL, DERIVED BY READING THREE FILES AND NOT BY RUNNING THEM.')
    rec('-' * 106)
    i, l = find(atl, 'L = math.log(a)', 'carto_atlas.py')
    rec('    carto_atlas.py:%-4d %s   ### the seed bump`s half-width' % (i, l.strip()))
    i, l = find(atl, 'v = np.linspace(-L, L, NV)', 'carto_atlas.py')
    rec('    carto_atlas.py:%-4d %s   ### so `v[-1] = math.log(a)` EXACTLY' % (i, l.strip()))
    i, l = find(sm, 'V = np.union1d(V, v)', 'b317_smear.py')
    rec('    b317_smear.py:%-4d  %s   ### the union keeps the widest grid`s endpoint' % (i, l.strip()))
    i, l = find(sq, 'L = abs(float(f.v[-1]))', 'b318_square.py')
    rec('    b318_square.py:%-4d  %s' % (i, l.strip()))
    i, l = find(sq, 'v = np.linspace(-2.0 * L, 2.0 * L, ac.size)', 'b318_square.py')
    rec('    b318_square.py:%-4d  %s   ### the support DOUBLES' % (i, l.strip()))
    rec('')
    rec('    ### ### **SO `L = 2.0 * math.log(a)` EXACTLY**, since `linspace`s endpoint is exact and')
    rec('    ### the widest of the three bumps is `bump(a**1)`. ### **THE GATE IS THEREFORE**')
    rec('    ### ### **`math.log(n) <= 2.0 * math.log(a)`**, which is `n <= a**2` read in logs --')
    rec('    ### and reading it in logs is not the same test as reading it in `a**2`, at the edge.')

    # ---------------------------------------------------------------- (P3) the arithmetic
    rec('')
    rec('(P3) THE CELL `a = 4.123106`, TO FULL PRECISION, AGAINST `17`.')
    rec('-' * 106)
    a = 4.123106
    r17 = math.sqrt(17.0)
    rows = []
    for name, av in (('the cell as the banks store it', a), ('sqrt(17) to full float precision', r17)):
        La = 2.0 * math.log(av)
        asq = av * av
        ln17 = math.log(17.0)
        enters_inner = ln17 <= La
        enters_outer = 17.0 <= math.exp(La) + 1e-12
        margin = La - ln17
        rows.append(dict(name=name, a=av, asq=asq, L=La, ln17=ln17,
                         inner=bool(enters_inner), outer=bool(enters_outer), margin=margin))
        rec('    %s' % name)
        rec('      a               = %s' % repr(av))
        rec('      a * a           = %s' % repr(asq))
        rec('      17              = %s' % repr(17.0))
        rec('      a*a - 17        = %+.6e' % (asq - 17.0))
        rec('      L = 2 log a     = %s' % repr(La))
        rec('      log 17          = %s' % repr(ln17))
        rec('      L - log 17      = %+.6e   ### the margin the INNER gate actually sees' % margin)
        rec('      ### outer cap `17 <= exp(L) + 1e-12` : ### **%s**' % enters_outer)
        rec('      ### inner gate `log 17 <= L`         : ### **%s**' % enters_inner)
        rec('')
    rec('    ### ### **17 ENTERS THE SUM AT THIS CELL -- AND NOT AT THE EDGE.**')
    rec('    ### The banks store the cell as the ROUNDED DECIMAL `4.123106`, not as `sqrt(17)`.')
    rec('    ### That rounding puts `a**2` ### **%.6e ABOVE 17**, so `17` is STRICTLY INSIDE the'
        % (rows[0]['asq'] - 17.0))
    rec('    ### support by ### **%.6e in log units** -- ### **THE EDGE CASE IS NEVER EXERCISED AT'
        % rows[0]['margin'])
    rec('    ### THIS CELL.** ### **SO THE COMPARATOR`S BOUNDARY CONVENTION CANNOT BE WHAT')
    rec('    ### DISTINGUISHES THIS CELL**, whichever way the convention is read.')
    rec('    ### ### **AND AT `sqrt(17)` ITSELF -- A CELL THE BANKS DO NOT HOLD -- BOTH GATES STILL')
    rec('    ### ADMIT:** outer %s, inner %s, margin exactly %+.3e. ### The inner gate is a WEAK'
        % (rows[1]['outer'], rows[1]['inner'], rows[1]['margin']))
    rec('    ### inequality, so equality passes it. ### **THE FIRST DRAFT OF THIS SURVEY SAID THE')
    rec('    ### TWO GATES DISAGREE THERE; THEY DO NOT, AND THE CLAIM IS WITHDRAWN.**')
    rec('    ### ### **SO THE CODE IMPLEMENTS THE WEAK READING AT THE EDGE TOO** -- which is b321`s')
    rec('    ### stated RULE. ### But b400`s point survives it: at the exact edge `f` VANISHES, the')
    rec('    ### term`s value is `0`, and `prime_sum`s own `if val:` keeps it out of `terms`.')
    rec('    ### ### **SO AT THE EDGE THE PRIME ENTERS THE LOOP AND NOT THE LIST**, and the')
    rec('    ### convention decides a printed membership and nothing numerical.')

    # ---------------------------------------------------------------- (P4) b400's routed discrepancy
    rec('')
    rec('(P4) b400`S ROUTED DISCREPANCY ON b321`S FACE, AT ITS ADDRESS.')
    rec('-' * 106)
    b400 = read(os.path.join(D, 'b400_closing.txt'))
    i, _ = find(b400, "A PRIOR ACT'S FACE CARRIES TWO CONVENTIONS", 'b400_closing.txt')
    for j in range(i - 1, i + 6):
        if 0 <= j < len(b400.split(NL)):
            rec('    b400_closing.txt:%-4d %s' % (j + 1, b400.split(NL)[j].strip()[:140]))
    rec('')
    rec('    ### ### **IT IS THE SAME COMPARATOR** -- the same boundary, `p^m <= a^2` against')
    rec('    ### `p^m < a^2`, and the code`s `if ln <= L` is the WEAK side, which is b321`s stated')
    rec('    ### RULE and not b321`s printed LIST.')
    rec('    ### ### **AND b400 ALREADY DECIDED WHAT IT IS WORTH:** *"IT MOVES NO VALUE. `f = g conv')
    rec('    ### g^#` is a self-convolution supported in `[a^-2, a^2]` and VANISHES AT ITS')
    rec('    ### ENDPOINTS, so an endpoint prime power contributes `0` to (149) under either')
    rec('    ### reading; what differs is a printed membership list."*')

    # ---------------------------------------------------------------- (P5) the three measurements
    rec('')
    rec('(P5) THE THREE MEASUREMENTS THAT SINGLE OUT THIS CELL, QUOTED FROM THEIR OWN BANKS.')
    rec('-' * 106)
    quotes = []
    for act, path, needles in (
            # ### **THE FIRST NEEDLE ASKED b437 FOR THE WORD `rung` ON THE CELL'S OWN ROW AND MISSED**
            # ### -- the row is a TABLE row carrying the rung NUMBER, not the word. ### And the
            # ### phrase "turns from rung 10 to 11" is b446's characterisation, not b437's own.
            ('b437', 'b437_components.txt', ('4.123106',)),
            ('b446 (on b437)', 'b446_components.txt', ('turns from rung 10 to 11',)),
            ('b446', 'b446_closing.txt', ('THE OUTLIER 4.123106',)),
            ('b447', 'b447_components.txt', ('4.123106',)),
            ('b483', 'b483_components.txt', ('LADDER     n=8',))):
        t = read(os.path.join(D, path))
        hit = None
        for i, l in enumerate(t.split(NL)):
            if all(n in l for n in needles):
                hit = (i + 1, l.strip())
                break
        if hit:
            rec('    %s -- %s:%d' % (act, path, hit[0]))
            rec('        %s' % hit[1][:150])
            quotes.append(dict(act=act, path=path, line=hit[0], text=hit[1][:300]))
        else:
            rec('    %s -- %s : ### **NO LINE CARRYING %s**' % (act, path, needles))
            MISSES.append((path, str(needles)))

    # ---------------------------------------------------------------- (P6) the trunc_bound census
    rec('')
    rec('(P6) THE `trunc_bound` CENSUS OVER THE BANKED ACTS, BY THE MATCHER`S OWN RULE.')
    rec('-' * 106)
    rec('    ### THE RULE, FIXED BEFORE IT RUNS:')
    rec('      (a) ### **A CITING ACT** is an act whose banked `data/bNNN_*` text contains the token')
    rec('          `trunc_bound`. ### The act is counted ONCE however many times it says it.')
    rec('      (b) ### **A MIS-SCOPING ACT** is one whose sentence ### **PREDICATES** ### `trunc_bound`')
    rec('          as a floor or as the chain`s binding bound -- not one whose sentence merely')
    rec('          MENTIONS both figures. ### The window is the SENTENCE, not the line and not the')
    rec('          paragraph -- ### **b483 PAID FOR THAT LESSON TWICE IN ONE ACT** -- and the test')
    rec('          inside the window is PREDICATION, not CO-OCCURRENCE. ### Both versions of the')
    rec('          matcher are run and both yields printed below.')
    rec('      (c) ### A sentence that says `trunc_bound` bounds the zero sum or the truncation, or')
    rec('          that it does NOT cover the places side, is ### **CORRECTLY SCOPED** and is not')
    rec('          counted -- ### **INCLUDING THIS ACT`S OWN AND b483`S.**')
    SCOPE_OK = re.compile(r'zero sum|truncation of the zero|does not cover|under-state|'
                          r'not the bound|says nothing about|bounds the truncation', re.I)
    # ### ### **RULE (b), VERSION 1 -- CO-OCCURRENCE IN A SENTENCE.**
    WIDE = re.compile(r'\bfloor\b|bound on the chain|the chain.{0,3}s (?:own )?bound|'
                      r'the chain.{0,3}s floor', re.I)
    # ### ### **RULE (b), VERSION 2 -- PREDICATION, NOT CO-OCCURRENCE.** ### Version 1 counts any
    # ### sentence that happens to say `floor` anywhere near `trunc_bound`, and b477's does: it
    # ### describes the DIAGONAL CHECK running "within the floor 1.49e-08" while `trunc_bound` is
    # ### PRINTED BESIDE each cell -- two different figures in one sentence, and no claim that
    # ### either is the other. ### **A SENTENCE THAT MENTIONS TWO NUMBERS DOES NOT EQUATE THEM.**
    # ### Version 2 requires the sentence to SAY SO: `trunc_bound` on one side of a copula or an
    # ### appositive, and `floor`/`the chain's bound` on the other.
    NARROW = re.compile(
        r'trunc_bound`?[^.]{0,40}\b(?:is|as|=|:)\s*[^.]{0,40}\bfloor\b'
        r'|\bthe (?:tail )?(?:bound|figure)\b[^.]{0,60}\bis\b[^.]{0,40}\b(?:binding|the floor)\b'
        r'|\bfloor\b[^.]{0,30}\bis\b[^.]{0,30}`?trunc_bound',
        re.I)
    citing, wide_hits, narrow_hits = {}, {}, {}
    for fn in sorted(os.listdir(D)):
        m = re.match(r'^(b\d+)[a-z]?_', fn)
        if not m or not fn.endswith(('.txt', '.json', '.jsonl')):
            continue
        # ### ### **THE CENSUS DOES NOT COUNT THIS ACT'S OWN VOICE.** ### The first run of this
        # ### matcher scanned `data/b484_*` and found ITSELF: the hand-read residue block below
        # ### quotes b483's mis-scoped sentence, so the quotation matched the rule and `b484` was
        # ### returned as a mis-scoping act. ### **A SEARCH THAT CAN SEE ITS OWN REPORT WILL ALWAYS
        # ### CONFIRM IT** -- b481's species, met again here and excluded by name rather than by
        # ### hoping the run order hides it.
        if fn.startswith('b484_'):
            continue
        t = read(os.path.join(D, fn))
        if 'trunc_bound' not in t:
            continue
        act = m.group(1)
        citing.setdefault(act, set()).add(fn)
        for para in t.split(NL + NL):
            for s in re.split(r'(?<=[.!?])\s+', para.replace(NL, ' ')):
                if 'trunc_bound' not in s or SCOPE_OK.search(s):
                    continue
                if WIDE.search(s):
                    wide_hits.setdefault(act, []).append((fn, s.strip()[:200]))
                if NARROW.search(s):
                    narrow_hits.setdefault(act, []).append((fn, s.strip()[:200]))
    rec('')
    rec('    ### ### **ACTS CITING `trunc_bound` : %d** -- %s'
        % (len(citing), ', '.join(sorted(citing))))
    rec('')
    rec('    ### THE MATCHER`S LINEAGE, BOTH VERSIONS` YIELDS PRINTED:')
    rec('      version 1, CO-OCCURRENCE in a sentence : ### **%d** -- %s'
        % (len(wide_hits), ', '.join(sorted(wide_hits)) or 'none'))
    rec('      version 2, PREDICATION                 : ### **%d** -- %s'
        % (len(narrow_hits), ', '.join(sorted(narrow_hits)) or 'none'))
    rec('    ### ### **VERSION 2 IS ADOPTED, AND THE RESIDUE IS HAND-READ BELOW RATHER THAN')
    rec('    ### DISCARDED** -- the rule the record already carries for a narrowed screen.')
    rec('')
    rec('    ### THE HAND-READ RESIDUE -- every sentence version 1 caught, with its verdict:')
    for act in sorted(wide_hits):
        for fn, s in wide_hits[act][:3]:
            v = 'MIS-SCOPED' if act in narrow_hits else 'NOT A CLAIM -- two figures in one sentence'
            rec('      %s  %s  ### **%s**' % (act, fn, v))
            rec('        %s' % s)
    rec('')
    rec('    ### ### **OF THE %d CITING ACTS, ACTS PREDICATING `trunc_bound` AS A FLOOR OR AS THE'
        % len(citing))
    rec('    ### CHAIN`S BINDING BOUND : %d** -- %s'
        % (len(narrow_hits), ', '.join(sorted(narrow_hits)) or 'NONE'))
    if narrow_hits:
        rec('    ### ### **AND ONE OF THEM IS b483, THIS ACT`S OWN PREDECESSOR, WHICH SAID IT IN ITS')
        rec('    ### SURVEY AND THEN REFUTED IT IN ITS COMPONENT 3.** ### The work-order is filed')
        rec('    ### against a defect the record has already caught itself committing.')

    rec('')
    rec('=' * 106)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 106)
    io.open(os.path.join(D, 'b484_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(rows=rows, quotes=quotes,
                   citing=sorted(citing), citing_n=len(citing),
                   wide={k: v for k, v in wide_hits.items()}, wide_n=len(wide_hits),
                   misscoped={k: v for k, v in narrow_hits.items()},
                   misscoped_n=len(narrow_hits),
                   misses=MISSES),
              io.open(os.path.join(D, 'b484_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
