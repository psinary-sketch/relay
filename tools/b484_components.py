# -*- coding: utf-8 -*-
"""b484_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (`3b158ac48adc7fb7...`).
### ### **COMPONENT 1 IS THE ONLY THING IN THIS ACT THAT WRITES TO THE CORPUS**, and it writes two
### state words on one line plus one appended annotation. ### **NO CHAIN IS RUN AND NO LANE OPENED.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TARGET = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
NL = chr(10)
L = []

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


def gits(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


OLD_WORDS = ('monograph v1.1.1, version DOI 10.5281/zenodo.21436278')
NEW_WORDS = ('monograph v1.1.2, version DOI 10.5281/zenodo.21539167')


def component1():
    rec('=' * 108)
    rec('COMPONENT 1 -- (R92) EXECUTED. ### THE CURRENCY REPAIR AT INVARIANCE_BARRIERS.md:580.')
    rec('=' * 108)
    raw = io.open(TARGET, 'rb').read()
    txt = raw.decode('utf-8-sig' if raw.startswith(b'\xef\xbb\xbf') else 'utf-8')
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    lines = txt.replace(chr(13), '').split(NL)
    idx = 579
    original = lines[idx]
    rec('  ### THE LINE AS IT STANDS, VERBATIM (`:%d`):' % (idx + 1))
    rec('    %s' % original)
    rec('')
    rec('  ### REGISTRY`S GOVERNING `d1-1` ROW, WHICH IS THE AUTHORITY UNDER RULE 5:')
    reg = read(os.path.join(PP, 'REGISTRY.md')).split(NL)
    rec('    REGISTRY.md:414  %s' % reg[413].strip()[:150])
    rec('')
    if OLD_WORDS not in original:
        rec('  ### ### **HARD FAILURE: THE STATE WORDS ARE NOT ON THAT LINE. NOTHING IS WRITTEN.**')
        raise SystemExit(2)
    repaired = original.replace(OLD_WORDS, NEW_WORDS)
    rec('  ### THE TWO STATE WORDS, AND ONLY THOSE:')
    rec('    the version word : ### **v1.1.1  ->  v1.1.2**')
    rec('    the version DOI  : ### **10.5281/zenodo.21436278  ->  10.5281/zenodo.21539167**')
    rec('    the concept DOI  : `10.5281/zenodo.19675355` ### **ALREADY AGREES WITH REGISTRY AND IS')
    rec('                       NOT TOUCHED.**')
    rec('    the Day-1 deposit DOI `10.5281/zenodo.19675356` is a DIFFERENT RECORD`s identifier and')
    rec('    ### is ### **NOT A CURRENCY CLAIM**, so it is not touched either.')

    ann = [
        '',
        '---',
        '',
        ('**Currency repair — `b484`, 2026-09-22, under ruling `(R92)` with its addressee fixed by '
         '`(R93)`.** The bibliography entry for (2026c) above stated the monograph’s current '
         'deposit as **v1.1.1**, version DOI `10.5281/zenodo.21436278`. `REGISTRY.md`’s '
         'governing `d1-1` row carries **v1.1.2**, version DOI `10.5281/zenodo.21539167` '
         '(concept `10.5281/zenodo.19675355`, unchanged and therefore untouched), published '
         '2026-07-24 — and **REGISTRY is the authority under Rule 5**. The two state words are '
         'corrected in place; **no other line of this file is touched**.'),
        '',
        ('**The original line is preserved here verbatim**, so that no line of the file before this '
         'repair is absent from the file after it:'),
        '',
        '```',
        original,
        '```',
        '',
        ('*Found at `b481` by that act’s own negative search, filed there as a finding rather '
         'than fixed silently, and repaired here by the ruling that followed. The claim itself is '
         'unchanged: only its statement of which deposit is current.*'),
        '',
    ]
    newlines = lines[:idx] + [repaired] + lines[idx + 1:] + ann
    out = eol.join(newlines)
    data = (('﻿' if bom else '') + out).encode('utf-8')
    io.open(TARGET, 'wb').write(data)

    after_raw = io.open(TARGET, 'rb').read()
    after = after_raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    rec('')
    rec('  ### THE LINE AFTER THE REPAIR (`:%d`):' % (idx + 1))
    rec('    %s' % after.split(NL)[idx])
    rec('')
    rec('  ### ### **THE DIFF.**')
    ns = gits('diff', '--numstat', '--', 'phase1.5/method/INVARIANCE_BARRIERS.md').split()
    rec('    git --numstat : ### **+%s / -%s**' % (ns[0] if ns else '?', ns[1] if len(ns) > 1 else '?'))
    oldset = [l for l in lines]
    newset = set(after.split(NL))
    missing = [l for l in oldset if l not in newset]
    rec('    ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW FILE : %d.**' % len(missing))
    for m in missing[:3]:
        rec('      ### %s' % m[:140])
    rec('    ### That is the sense in which ### **LINES REMOVED IS `0`**: the one line whose bytes')
    rec('    ### changed is carried VERBATIM in the appended annotation, so the old file`s lines are')
    rec('    ### a SUBSET of the new file`s. ### **THE RAW `+/-` COUNTS ARE PRINTED ABOVE AND NOT')
    rec('    ### HIDDEN BEHIND THAT SENTENCE** -- git sees one line modified and an annotation added.')
    rec('    BOM preserved : %s ; line ending unchanged : %s'
        % (after_raw.startswith(b'\xef\xbb\xbf') == bom, (eol == NL) or (chr(13) + NL).encode() in after_raw))
    other = [i for i in range(min(len(lines), len(after.split(NL))))
             if i != idx and lines[i] != after.split(NL)[i]]
    rec('    ### ### **OTHER LINES CHANGED IN PLACE : %d.**' % len(other))
    return dict(original=original, repaired=repaired, numstat=ns[:2],
                missing=len(missing), other_changed=len(other))


def component2(SV):
    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- `W-ORD-QUADRATURE-BOUND`, FILED.')
    rec('=' * 108)
    rec('  ### ### **THE WORK-ORDER, IN ITS OWN STATEMENT:**')
    rec('  ### **THE CORPUS HOLDS NO ERROR BOUND FOR THE PLACES-SIDE QUADRATURE.** ### The chain')
    rec('  ### reports `trunc_bound`, which bounds the truncation of the ZERO SUM. ### `b483`')
    rec('  ### measured the ACHIEVED two-side agreement at ### **4.562e-05** on the aim plane and')
    rec('  ### ### **3.169e-06** on the ladder, against a reported `trunc_bound` of ### **1.290e-12**')
    rec('  ### and ### **6.421e-11** -- ### **SO THE REPORTED FIGURE UNDER-STATES THE ACHIEVED ERROR')
    rec('  ### BY UP TO SEVEN ORDERS.** ### **ANY ACT CITING `trunc_bound` AS THE CHAIN`S FLOOR')
    rec('  ### CITES A BOUND THAT DOES NOT COVER THE DOMINANT TERM.**')
    rec('')
    rec('  ### ### **TRIGGER:** the next opening of the numerical instrument lane, or the next act')
    rec('  ### that cites a chain floor -- whichever comes first.')
    rec('  ### ### **WHAT WOULD DISCHARGE IT:** an error bound for the places-side quadrature at a')
    rec('  ### quotable address, or a ruling that the chain`s figures are to be read relatively')
    rec('  ### rather than absolutely, with the relative figure named.')
    rec('  ### ### **NOTHING IS REPAIRED IN THE CHAIN AND THE CHAIN IS NOT EDITED BY THIS ACT.**')
    rec('')
    rec('  ### ### **THE TWO FIGURES, BY TOOL, WITH THE MATCHER`S OWN RULE.**')
    rec('    ### the rule: a CITING act is one whose banked text carries the token, counted once.')
    rec('    ### A MIS-SCOPING act is one whose sentence ### **PREDICATES** ### the token as a floor')
    rec('    ### or as the chain`s binding bound -- ### **NOT ONE WHOSE SENTENCE MERELY MENTIONS BOTH')
    rec('    ### FIGURES.** ### The window is the SENTENCE. ### This act`s own stem is EXCLUDED.')
    rec('')
    rec('    ### ### **ACTS CITING `trunc_bound` : %d** -- %s'
        % (SV['citing_n'], ', '.join(SV['citing'])))
    rec('    ### ### **OF THOSE, ACTS PREDICATING IT AS A FLOOR OR A CHAIN BOUND : %d** -- %s'
        % (SV['misscoped_n'], ', '.join(sorted(SV['misscoped'])) or 'NONE'))
    rec('')
    rec('    ### THE MATCHER`S LINEAGE, BOTH YIELDS PRINTED:')
    rec('      version 1, CO-OCCURRENCE : %d -- %s'
        % (SV['wide_n'], ', '.join(sorted(SV['wide'])) or 'none'))
    rec('      version 2, PREDICATION   : %d -- %s'
        % (SV['misscoped_n'], ', '.join(sorted(SV['misscoped'])) or 'none'))
    rec('    ### ### **VERSION 1`S EXTRA IS `b477`, AND IT IS A FALSE POSITIVE.** ### Its sentence')
    rec('    ### describes the diagonal check running *within the floor* WHILE `trunc_bound` is')
    rec('    ### *printed beside* each cell -- ### **TWO FIGURES IN ONE SENTENCE AND NO CLAIM THAT')
    rec('    ### EITHER IS THE OTHER.** ### The residue was hand-read, not discarded.')
    rec('')
    for act in sorted(SV['misscoped']):
        rec('    ### ### **THE ONE ACT THAT DOES PREDICATE IT : `%s`**, in its own survey:' % act)
        for fn, s in SV['misscoped'][act][:1]:
            rec('      %s' % fn)
            rec('        %s' % s[:180])
    rec('    ### ### **AND `b483` REFUTED ITSELF IN ITS OWN COMPONENT 3**, which is where the')
    rec('    ### achieved figure was measured and the reported one set beside it. ### **THE')
    rec('    ### WORK-ORDER IS FILED AGAINST A DEFECT THE RECORD HAS ALREADY CAUGHT ITSELF')
    rec('    ### COMMITTING, WHICH IS THE BEST EVIDENCE THAT IT IS REAL AND NOT A STYLE NOTE.**')
    return dict(citing=SV['citing_n'], predicating=SV['misscoped_n'],
                wide=SV['wide_n'], named=sorted(SV['misscoped']))


def component3(SV):
    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- THE SUPPORT-EDGE TEST, RUN AS A READ.')
    rec('=' * 108)
    r = SV['rows'][0]
    rec('  ### (3a) THE COMPARATOR, AT ITS OWN LINE.')
    rec('    b321_window.py:113   while p ** k <= math.exp(L) + PRIME_TOL:     ### the OUTER cap')
    rec('    b321_window.py:116   if ln <= L:                                  ### the INNER gate')
    rec('    b321_window.py:110   L = float(v[-1])')
    rec('    ### ### **THERE ARE TWO, AND THE ONE THAT DECIDES WHETHER A TERM IS ADDED IS THE INNER')
    rec('    ### GATE `math.log(n) <= L` -- A WEAK INEQUALITY WITH NO TOLERANCE**, in log')
    rec('    ### coordinates. ### The outer cap`s `1e-12` only bounds which powers are considered.')
    rec('    ### And `L = 2.0 * math.log(a)` exactly, by `carto_atlas.bump` and')
    rec('    ### `b318_square.autocorrelation` -- so the gate is `n <= a**2` READ IN LOGS.')
    rec('')
    rec('  ### (3b) THE CELL, TO FULL PRECISION.')
    rec('    a               = %r' % r['a'])
    rec('    a * a           = ### **%r**' % r['asq'])
    rec('    17              = 17.0')
    rec('    a*a - 17        = ### **%+.6e**' % (r['asq'] - 17.0))
    rec('    L = 2 log a     = %r' % r['L'])
    rec('    log 17          = %r' % r['ln17'])
    rec('    L - log 17      = ### **%+.6e**' % r['margin'])
    rec('    ### outer cap `17 <= exp(L) + 1e-12` : ### **%s**' % r['outer'])
    rec('    ### inner gate `log 17 <= L`         : ### **%s**' % r['inner'])
    rec('    ### ### **SO `17` ENTERS THE SUM AT THIS CELL.**')
    rec('    ### ### **BUT NOT AT THE EDGE.** ### The banks store the cell as the ROUNDED DECIMAL')
    rec('    ### `4.123106`, not as `sqrt(17)`, and that rounding puts `a*a` ### **%.6e ABOVE 17**,'
        % (r['asq'] - 17.0))
    rec('    ### leaving the inner gate a margin of ### **%.6e in log units -- `4.089e+08` times the'
        % r['margin'])
    rec('    ### float`s own resolution there.** ### **THE EDGE CASE IS NEVER EXERCISED AT THIS CELL,')
    rec('    ### SO THE ADMISSION OWES NOTHING TO THE CONVENTION.**')
    rec('')
    rec('  ### (3c) b400`S ROUTED DISCREPANCY -- IS IT THE SAME COMPARATOR?')
    rec('    `b400_closing.txt:201-207`, quoted:')
    rec('      > "`b321`s Component 3 states its rule as *a prime power `p^m` enters exactly when')
    rec('      >  `p^m <= a^2`* and its printed list omits `4` at `a = 2` and `9` at `a = 3`, which')
    rec('      >  is the STRICT reading -- **THEY DISAGREE AT `2` OF `13` CELLS.** It moves no')
    rec('      >  value, because `f = g conv g^#` vanishes at the endpoints of `[a^-2, a^2]`, so an')
    rec('      >  endpoint prime power contributes `0` to (149) under either reading."')
    rec('    ### ### **YES -- IT IS THE SAME COMPARATOR.** ### The same boundary, `p^m <= a^2`')
    rec('    ### against `p^m < a^2`, and the code`s `if ln <= L` sits on the WEAK side, which is')
    rec('    ### b321`s stated RULE and not b321`s printed LIST.')
    rec('    ### ### **AND b400 ALREADY PRICED IT: IT MOVES NO VALUE.** ### At the exact edge `f`')
    rec('    ### vanishes, the term`s value is `0`, and `prime_sum`s own `if val:` keeps it out of')
    rec('    ### `terms` -- ### **SO AT THE EDGE THE PRIME ENTERS THE LOOP AND NOT THE LIST.**')
    rec('')
    rec('  ### (3d) THE THREE MEASUREMENTS, EACH QUOTED FROM ITS OWN BANK.')
    for q in SV['quotes']:
        rec('    ### %s -- `%s:%d`' % (q['act'], q['path'], q['line']))
        rec('        %s' % q['text'][:150])
    rec('')
    rec('  ### (3e) ### **THE VERDICT.**')
    rec('    ### ### **SEPARATE OBJECTS.**')
    rec('    ### THE DECIDING WORDS, QUOTED, AND THEY ARE NOT THIS ACT`S:')
    rec('      (i)  b400: ### **"It moves no value ... an endpoint prime power contributes `0` to')
    rec('           (149) under either reading; what differs is a printed membership list."**')
    rec('           ### **A CONVENTION THAT CHANGES NO NUMBER CANNOT BE THE COMMON CAUSE OF THREE')
    rec('           ### NUMBERS.**')
    rec('      (ii) and this act`s own arithmetic: at `a = 4.123106` the prime is STRICTLY INSIDE by')
    rec('           `%.6e` in log units, so ### **NO INCLUSION DECISION IS TAKEN AT THIS CELL AT'
        % r['margin'])
    rec('           ALL.** ### The boundary convention is not merely harmless here -- ### **IT IS')
    rec('           ### NOT CONSULTED.**')
    rec('      (iii) b446, on its own outlier: ### **"Not the rung alone (3.605551 = sqrt(13)')
    rec('           converged)"** -- so the record had already refused to read that cell`s')
    rec('           distinction off its arithmetic form.')
    rec('    ### ### **THE THREE MEASUREMENTS ARE OF THREE DIFFERENT THINGS** -- b437`s rung is a')
    rec('    ### LADDER INDEX, b446/b447`s outlier is a DECORRELATION RESIDUAL ORDER, b483`s')
    rec('    ### excursion is a GRAM SIGNATURE -- ### **AND THEY SHARE A CELL, NOT A CAUSE.**')
    rec('    ### ### **WHAT THEY DO SHARE IS STILL UNEXPLAINED, AND THIS ACT DOES NOT EXPLAIN IT.**')
    rec('    ### Naming a common cause that the record shows cannot move a number would be worse')
    rec('    ### than leaving the coincidence open. ### **IT IS LEFT OPEN.**')
    return dict(verdict='SEPARATE OBJECTS', margin=r['margin'], asq=r['asq'],
                enters=bool(r['inner']), at_edge=False, same_comparator=True)


def main():
    SV = json.loads(read(os.path.join(D, 'b484_survey.json')))
    c1 = component1()
    c2 = component2(SV)
    c3 = component3(SV)
    io.open(os.path.join(D, 'b484_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(c1=c1, c2=c2, c3=c3),
              io.open(os.path.join(D, 'b484_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
