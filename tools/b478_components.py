# -*- coding: utf-8 -*-
"""b478_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (sha256 `037e47fbc78f8378...`).
### The cells, the reverse reads, and the one sentence the table supports.
### ### **NOTHING IS COMPUTED NUMERICALLY; NO LANE OPENS; NO BRIDGE IS TYPED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b478_extract as X  # noqa: E402  ### the cell rule and the reader, IMPORTED not copied

D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []
SITES, KS = X.SITES, X.KS
TITLES = {'i': 'the clause`s quantifier (index: the class)',
          'ii': 'the height coordinate`s enumeration (index: the height)',
          'iii': 'the width coordinate`s union (index: the width)',
          'iv': 'the prime constituent at a widened support (index: the width)',
          'v': 'the representation-dependent constant (index: the representation)',
          'vi': 'the Type-D residue at every finite modulus (index: the modulus)'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


S = json.loads(io.open(os.path.join(D, 'b478_survey.json'), encoding='utf-8').read())
CELLS = {tuple(k.split('|')): v for k, v in S['cells'].items()}


def main():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE FORTY-EIGHT CELLS. ### SIX SITES BY EIGHT CONSTITUENTS.')
    rec('=' * 104)
    rec('    the rule, as the survey tool fixed it before any cell was read:')
    rec('      SAME OBJECT -- the site`s INDEX is the constituent`s own VARIABLE, by the two entries` own text')
    rec('      TOUCHES     -- the site`s statement, if supplied, would constrain that constituent`s grade')
    rec('      APART       -- neither')
    rec('')
    rec('    %-5s %s' % ('', ' '.join('%-11s' % k for k in KS)))
    for s in SITES:
        rec('    (%-3s) %s' % (s, ' '.join('%-11s' % (CELLS[(s, k)]['verdict'].replace('SAME OBJECT', 'SAME-OBJ'))
                                           for k in KS)))
    rec('')
    rec('  ### THE NON-APART CELLS, EACH WITH BOTH SIDES` DECIDING WORDS, VERIFIED VERBATIM:')
    for s in SITES:
        rows = [(k, CELLS[(s, k)]) for k in KS if CELLS[(s, k)]['verdict'] != 'APART']
        if not rows:
            rec('    ### ### **(%s) %s -- NO CELL IS ANYTHING BUT APART.**' % (s, TITLES[s]))
            continue
        rec('    (%s) %s' % (s, TITLES[s]))
        for k, c in rows:
            rec('      x %-3s %-12s' % (k, c['verdict']))
            rec('          the site says        : "%s"   [found in row U1 : %s]' % (c['site_words'], c['site_found']))
            rec('          the constituent says : "%s"   [found in %s : %s]' % (c['k_words'], k, c['k_found']))
    same = [tuple(p.split('|')) for p in S['same_object']]
    touch = [tuple(p.split('|')) for p in S['touches']]
    rec('  ### ### **SAME OBJECT %d -- %s ; TOUCHES %d ; APART %d.**'
        % (len(same), ', '.join('(%s) x %s' % p for p in same), len(touch), 48 - len(same) - len(touch)))
    rec('  ### ### **AND `TOUCHES` IS A RELATION BETWEEN TWO ENTRIES OF THIS RECORD, NOT BETWEEN TWO')
    rec('  ### MATHEMATICAL OBJECTS: it says what would constrain a grade IF a statement were supplied, and')
    rec('  ### it does not say the statement exists. ### NO BRIDGE IS TYPED, AND ROW U1`S LAW IS UNTOUCHED.**')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE TWO REVERSE READS.')
    rec('=' * 104)
    rec('  ### (2a) CONSTITUENTS NO SITE TOUCHES.')
    for k in S['k_untouched']:
        rec('      ### **%s %s**' % (k, S['e0_names'][k]))
    rec('    touched, for contrast : %s' % ', '.join('%s %s' % (k, S['e0_names'][k]) for k in S['k_touched']))
    rec('  ### ### **THREE OF THE EIGHT CONSTITUENTS ARE TOUCHED BY NO SITE OF ROW U1.** ### K3 is the')
    rec('  ### finite places` contribution, whose counting form is compiled and decided at cells; K6 is the')
    rec('  ### decomposition, measured where the identity is covered; K7 is the object and its archimedean')
    rec('  ### unit, in by derivation and under-resolved at bench. ### **THE ROW`S SIX MISSING STATEMENTS')
    rec('  ### WOULD LEAVE ALL THREE EXACTLY WHERE THEIR OWNERS LEFT THEM.**')
    rec('')
    rec('  ### (2b) SITES NO CONSTITUENT TOUCHES.')
    for s in S['s_untouched']:
        rec('      ### **(%s) %s**' % (s, TITLES[s]))
    rec('    touching at least one : %s' % ', '.join('(%s)' % s for s in S['s_touched']))
    rec('  ### ### **AND THAT IS A RESULT, NOT AN OMISSION.** ### The E0 gate unfolds the constituents of')
    rec('  ### the stated clause for the corpus`s FIRST object. ### Site (v) is about a class of')
    rec('  ### representations that does not contain the corpus`s SECOND object, and site (vi) is about a')
    rec('  ### modulus in additive number theory. ### **TWO OF THE SIX SITES BEAR ON NOTHING THE E0 TABLE')
    rec('  ### GRADES, BECAUSE THE TABLE IS ZETA`S AND THEY ARE NOT.**')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 3 -- THE ONE SENTENCE THE TABLE SUPPORTS.')
    rec('=' * 104)
    moved = S['k_touched']
    left = S['k_untouched']
    rec('  ### ### **A PROOF SUPPLYING ALL SIX OF ROW U1`S MISSING STATEMENTS WOULD MOVE THE GRADES OF')
    rec('  ### %s -- AND WOULD LEAVE %s EXACTLY AS THEIR OWNERS LEFT THEM.**'
        % (', '.join(moved), ', '.join(left)))
    rec('  ### Said at length, and no wider than the record`s own vocabulary:')
    rec('    - `K8` the quantifiers is the ONLY constituent any site is SAME OBJECT with, and two sites are:')
    rec('      (i) by the clause`s own words, *"are UNOWNED, and they are the clause"*, and (ii) through the')
    rec('      explicit formula over the zeros. ### **SO THE OPEN PART OF THE STATED CLAUSE AND THE FIRST')
    rec('      TWO SITES OF ROW U1 ARE THE SAME UNOWNED QUANTIFIERS, ENTERED TWICE IN TWO DOCUMENTS.**')
    rec('    - `K1` the class and `K2` the criterion`s sign are touched by three sites between them: a')
    rec('      statement uniform over the class, or across widths, would lift measurements taken per seed')
    rec('      and per cell to the class the criterion quantifies over.')
    rec('    - `K4` the prime sum and `K5` the archimedean distribution are touched by site (iv) alone,')
    rec('      whose own statement asks for a bound on the prime constituent *"against an archimedean')
    rec('      quantity"* -- the two channels named in one sentence.')
    rec('    - `K3`, `K6`, `K7` are touched by no site: the compiled finite side, the decomposition at')
    rec('      covered cells, and the object with its archimedean unit. ### **WHAT ROW U1 IS MISSING IS NOT')
    rec('      WHAT THOSE THREE ARE SHORT OF.**')
    rec('  ### ### **THIS SENTENCE IS ABOUT GRADES IN THIS RECORD. ### IT SAYS NOTHING ABOUT RH, CONFERS NO')
    rec('  ### GRADE, ENTERS NO SITE, AND TYPES NO BRIDGE. ### h2 STANDS WHERE THE DEPOSIT LEFT IT.**')

    io.open(os.path.join(D, 'b478_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(cells=S['cells'], same_object=S['same_object'], touches=S['touches'],
                   k_untouched=left, k_touched=moved, s_untouched=S['s_untouched'],
                   sentence=dict(moved=moved, left=left)),
              io.open(os.path.join(D, 'b478_table.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
