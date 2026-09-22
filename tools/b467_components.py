# -*- coding: utf-8 -*-
"""b467_components.py -- THE TWO COMPONENTS. ### THE CONCORDANCE READ, AND THE GENERAL SOURCE.

### ### **RUN AFTER THE SEAL.** ### The face is locked at sha256 `2c1cff30be4f532e...` and every
### rule below was declared on it before this file ran.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
MONO = os.path.join(DEP, 'A_Place_to_Stand.md')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
NL = chr(10)
L = []
sys.path.insert(0, T)

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


def lag_line(n):
    """### **A QUOTATION FROM THE EXTRACTION IS PRINTED AS EXTRACTED, AT ITS LINE.**"""
    return read(LAG).split(NL)[n - 1].strip()


SURVEY = json.load(io.open(os.path.join(D, 'b467_survey.json'), encoding='utf-8'))
G = json.load(io.open(os.path.join(D, 'b464_grades.json'), encoding='utf-8'))


# --------------------------------------------------------------------------------------------
def component1():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE CONCORDANCE READ, UNDER (R74).')
    rec('=' * 104)
    rec('')
    rec('  ### (1a) THE CONCORDANCE ITSELF, PARSED FROM THE DEPOSITED FILE.')
    rec('  ' + '-' * 100)
    rows = SURVEY['concordance']
    rec('    section 25.8 at A_Place_to_Stand.md:%d ; ### **ROWS : %d**'
        % (SURVEY['concordance_line'], len(rows)))
    rec('    %-46s %-30s %s' % ('the terminal the row names', 'module', 'the row`s own grade'))
    rec('    ' + '-' * 98)
    for r in rows:
        rec('    %-46s %-30s %s' % (r['theorem'][:46], r['module'][:30], r['axioms'][:24]))
    rec('')
    rec('    ### ### **THE CONCORDANCE\x27s GRADE COLUMN IS `#print axioms` -- A GRADE OF AXIOM')
    rec('    ### DEPENDENCE, NOT OF WHETHER THE THEOREM CARRIES A CLAIM.** ### Six of seven read the')
    rec('    ### three classical axioms and one reads `(none)`. ### **NOT ONE ROW IS GRADED `DERIVES`')
    rec('    ### OR `NOT THE CLAIM` BY THE CONCORDANCE ITSELF**, because that is not what it records.')

    rec('')
    rec('  ### (1b) THE ROW-FINDER, ITS LINEAGE, AND ITS CONTROLS.')
    rec('  ' + '-' * 100)
    rec('    ### **FOUR FORMS WERE RUN AND EVERY YIELD IS ON THE RECORD** (b467_extract.txt):')
    rec('      form 1  token overlap, threshold 2                  -- assigned 3 of 8')
    rec('      form 2  + generic-token drop + OPP precedence        -- IDENTICAL to form 1')
    rec('      form 3  + terminal-name overlap as a VETO            -- assigned 0 of 8')
    rec('      form 4  + camelCase split + stemming, name as a      -- assigned 0 of 8   ### GOVERNS')
    rec('              PREFERENCE with a raised prose-only bar')
    rec('    ### ### **FORM 3 FAILED ITS POSITIVE CONTROL AT 4 OF 7 AND ITS RESULT WAS NOT BANKED.**')
    rec('    ### Two tokenizer bugs it exposed: `ConservationBridge` was never split, so a claim\x27s')
    rec('    ### `conservation` could not meet its own terminal\x27s name; and `pair` never matched')
    rec('    ### `pairs`. ### **AND ONE FINDING THAT IS NOT A BUG:** the `spectral_cannon` row\x27s claim')
    rec('    ### shares NO WORD with its own terminal even after both repairs, so ### **A NAME-OVERLAP')
    rec('    ### VETO IS REFUTED BY THE DEPOSIT ITSELF** and form 4 makes it a preference.')
    rec('    ### ### **FORM 4\x27s CONTROLS : POSITIVE %d of %d ROWS RECOVER THEMSELVES ; NEGATIVE %s.**'
        % (SURVEY['control_fired'], SURVEY['control_rows'],
           'RETURNS `NO ROW`' if SURVEY['negative_control_no_row'] else '### ASSIGNS A ROW'))
    rec('    ### ### **SO THE `NO ROW`s BELOW ARE THE CONCORDANCE\x27s ANSWER AND NOT THE FINDER\x27s.**')

    rec('')
    rec('  ### (1c) THE EIGHT, TWICE, SIDE BY SIDE.')
    rec('  ' + '-' * 100)
    rec('    %-3s %-30s %-34s %-16s %s'
        % ('#', 'at', 'b464: nearest BY NAME @pin', 'b464 grade', 'b467: the concordance'))
    rec('    ' + '-' * 116)
    lin = {x['n']: x for x in SURVEY['lineage']}
    out = []
    for it in G['items']:
        f4 = lin[it['n']]['form4']
        rec('    %-3d %-30s %-34s %-16s %s'
            % (it['n'], ('%s:%d' % (it['surface'], it['line']))[:30], it['terminal'][:34],
               it['grade'], f4))
        out.append(dict(n=it['n'], surface=it['surface'], line=it['line'],
                        b464_terminal=it['terminal'], b464_grade=it['grade'],
                        concordance_row=(None if f4 == 'NO ROW' else f4),
                        concordance_grade=None,
                        final_grade=it['grade'],
                        standin=(f4 == 'NO ROW'),
                        why=lin[it['n']]['why']))
    noRow = sum(1 for o in out if o['standin'])
    rec('')
    rec('    ### ### **THE CONCORDANCE ASSIGNS A ROW TO %d OF THE EIGHT. ### `NO ROW` : %d.**'
        % (8 - noRow, noRow))
    rec('    ### ### **AND THE REASON IS STRUCTURAL, NOT LEXICAL.** ### Section 25.8\x27s seven rows are')
    rec('    ### about the three route terminals, two integration theorems, the formation count and')
    rec('    ### the cross-class exclusion. ### **NOT ONE OF b464\x27s EIGHT SENTENCES IS ABOUT ANY OF')
    rec('    ### THOSE SEVEN SUBJECTS** -- they are about the kernel\x27s redundancy to the manuscript,')
    rec('    ### the Mechanism Theorem\x27s carried forms, the heat trace of a self-adjoint spectrum, a')
    rec('    ### published coupling line, the s-darkness of the product formula, two compiled')
    rec('    ### negatives, and a certified premise with its surround. ### **THE CONCORDANCE IS A')
    rec('    ### TABLE OF SEVEN LOAD-BEARING THEOREMS; IT IS NOT AN INDEX OF THE DEPOSIT\x27s CLAIMS.**')

    rec('')
    rec('  ### (1d) THE DISPOSITION UNDER (R74)\x27s SECOND LIMB.')
    rec('  ' + '-' * 100)
    rec('    ### ### **ALL EIGHT KEEP b464\x27s GRADE, AND EVERY ONE IS LABELLED A STAND-IN.**')
    by = {}
    for o in out:
        by[o['final_grade']] = by.get(o['final_grade'], 0) + 1
    rec('      %s' % ' ; '.join('%s %d' % (k, by[k]) for k in sorted(by)))
    rec('    ### ### **NOT ONE OF THE SIX `NOT THE CLAIM` SENTENCES MOVES**, because a grade can only')
    rec('    ### move against a terminal the concordance assigns, and it assigns none.')
    rec('    ### ### **SO THE SIX REMAIN SIX DEPOSIT-LEVEL MATTERS UNDER `(R66)`, NAMED AND ROUTED**,')
    rec('    ### and the `SHELL` at item 5 remains a seventh. ### **NO ERRATUM IS WRITTEN HERE:**')
    rec('    ### `(R74)` puts `(R65)`\x27s dispositions (i) and (iii) in the act AFTER the read.')
    rec('    ### ### **AND ONE THING (R74) MAKES VISIBLE THAT b464 COULD NOT:** the question `which')
    rec('    ### terminal does the deposit itself assign to this sentence?` ### **HAS NO ANSWER IN THE')
    rec('    ### DEPOSIT FOR ANY OF THE EIGHT.** ### That is a stronger statement than any grade: it')
    rec('    ### is not that the sentences are graded badly, but that ### **THE DEPOSIT PROVIDES NO')
    rec('    ### MAPPING FROM THESE SENTENCES TO ITS OWN KERNEL AT ALL.** ### Routed, not repaired.')
    return out, by, noRow


# --------------------------------------------------------------------------------------------
# ### THE GENERAL SOURCE. ### Every address is the line the survey printed; every quotation is the
# ### extraction's own bytes, garbling included, with the reading stated beside it.
QUOTES = [
    ('the class the theorem quantifies over', 1207),
    ('the source`s own exception, marked by itself', 316),
    ('the completed L-function and its Euler factorization', 318),
    ('the conductor, named', 322),
    ('the finite Euler product', 332),
    ('the functional equation', 345),
    ('the analytic conductor', 467),
    ('the generalization to automorphic pi', 666),
    ('the appendix`s scope sentence', 2781),
    ('the Weil distribution functional', 2806),
    ('the truncation, as the source states it', 2813),
    ('the trace form', 2823),
    ('the places sum', 2829),
    ('the general-pi sentence', 2835),
]

SITES = [
    ('(i)', 'class', 'A COORDINATE OF ONE', 'A CONDITION ON THE TEST FUNCTION',
     'the source names a test-function space and conditions its members: in section 3 the vector '
     'space A of functions holomorphic in the strip with a uniform growth bound, and in the '
     'appendix the space A_delta by analyticity of the Mellin transform in a strip. The class is a '
     'condition on the named test function, exactly as under CC (148).'),
    ('(ii)', 'height', 'OF NO PARAMETER', "THE INSTRUMENT'S TRUNCATION",
     'the only T in the explicit formula is BOUND INSIDE A LIMIT: the prime on the sum means it is '
     'interpreted as lim_{T->inf} sum over |rho| <= T. A bound variable is not a datum. ### AND '
     'THIS SOURCE IS MORE EXPLICIT THAN CC (148), WHICH NAMES NO TRUNCATION AT ALL -- here the '
     'truncation is written down as the interpretation of a conditionally convergent sum.'),
    ('(iii)', 'width', 'OF NO PARAMETER', 'A CONDITION ON THE TEST FUNCTION',
     'THE SOURCE IMPOSES NO SUPPORT CONDITION. Its classes are cut by ANALYTICITY IN A STRIP and a '
     'GROWTH BOUND, not by compact support, so there is no support to have a width. ### THIS IS '
     'WHERE THE GENERAL SOURCE AND CC (148) DIVERGE: under CC the width was a coordinate of f`s '
     'compact support; here there is no such datum.'),
    ('(iv)', 'width', 'OF NO PARAMETER', 'A CONDITION ON THE TEST FUNCTION',
     'the same index of the same absent condition; (iii) and (iv) share this index, which row U1 '
     'already says of itself.'),
    ('(v)', 'representation', 'A PARAMETER', 'A DATUM OF THE REPRESENTATION',
     'the source quantifies over it in its own words -- "For any irreducible cuspidal (unitary) '
     'automorphic representation pi on GL(N)" -- and the whole apparatus, Lambda(s,pi), xi(s,pi), '
     'the Weil functional, is indexed by it. ### UNDER CC (148) THIS SITE WAS OF NO PARAMETER; '
     'under this source it IS the parameter.'),
    ('(vi)', 'modulus', 'A COORDINATE OF ONE', 'A DATUM OF THE REPRESENTATION',
     'Q(pi), "a positive integer called the conductor of the representation", is a datum of the '
     'named parameter pi, and for GL(1) the conductor of a Dirichlet character IS its modulus. ### '
     'AND THE CAVEAT IS PART OF THE VERDICT: row U1`s site (vi) is a modulus of CONGRUENCE in a '
     'sieve statement, not a character conductor, so what is identified here is THE INDEX and not '
     'the statement the index appears in.'),
]

HEADINGS = ('A CONDITION ON THE TEST FUNCTION', 'A DATUM OF THE REPRESENTATION',
            "THE INSTRUMENT'S TRUNCATION")

CC = {'(i)': 'A COORDINATE OF ONE', '(ii)': 'OF NO PARAMETER', '(iii)': 'A COORDINATE OF ONE',
      '(iv)': 'A COORDINATE OF ONE', '(v)': 'OF NO PARAMETER', '(vi)': 'OF NO PARAMETER'}


def component2():
    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE GENERAL SOURCE\x27s PARAMETERS AGAINST THE SIX SITES.')
    rec('=' * 104)
    rec('')
    rec('  ### (2a) THE SOURCE, ITS PIN, AND WHICH STATEMENT IS READ.')
    rec('  ' + '-' * 100)
    rec('    Lagarias, *Li coefficients for automorphic L-functions*, arXiv math/0404394v4,')
    rec('    pinned by b327 and re-verified by b358 at sha256 86f3d3c49f5a889f...')
    rec('    read at the banked extraction b358_source_lagarias0404394.txt')
    rec('    ### ### **THE STATEMENT READ IS THE GENERAL EXPLICIT FORMULA OVER AUTOMORPHIC')
    rec('    ### REPRESENTATIONS** -- the trace form (9.5) and its places sum, with the Weil')
    rec('    ### distribution functional (9.3) and the test-function space -- together with the')
    rec('    ### section-2 data the formula\x27s objects are built from. ### **AND THE SOURCE\x27s OWN')
    rec('    ### SCOPE SENTENCE TRAVELS WITH IT**, printed below at its line.')
    rec('    ### ### **b305\x27s CAVEAT APPLIES TO EVERY LINE HERE:** this is a PDF TEXT LAYER and it')
    rec('    ### garbles ligatures and formulas -- `ﬁ` and `ﬂ` survive as ligatures, subscripts and')
    rec('    ### superscripts are flattened, and line breaks fall inside words. ### **EACH LINE IS')
    rec('    ### PRINTED AS EXTRACTED AND THE READING IS STATED BESIDE IT, NEVER SILENTLY CLEANED.**')
    rec('')
    for label, n in QUOTES:
        rec('    %-50s :%d' % (label, n))
        rec('      %s' % lag_line(n)[:150])

    rec('')
    rec('  ### (2b) WHAT IT QUANTIFIES OVER, AND WHAT DATA OF THE REPRESENTATION IT USES.')
    rec('  ' + '-' * 100)
    rec('    ### ### **PRINTED BEFORE ANY SITE IS PLACED.**')
    rec('    QUANTIFIED OVER:')
    rec('      pi     -- an irreducible cuspidal (unitary) automorphic representation on GL(N)')
    rec('      f / F  -- the test function, in A (holomorphic in 0 < Re(s) < 1, growth O(1/|s|))')
    rec('                or in A_delta (Mellin transform analytic in a strip about the line)')
    rec('      rho    -- the zeros of xi(s,pi), summed with the prime: lim_{T->inf} sum |rho| <= T')
    rec('      nu     -- the places of the field K, archimedean and non-archimedean')
    rec('    DATA OF THE REPRESENTATION THE FORMULA USES:')
    rec('      Q(pi)          -- ### **THE CONDUCTOR**, a positive integer (2.1)')
    rec('      kappa_j(pi)    -- ### **THE GAMMA FACTORS**: L_inf(s,pi) = prod_j Gamma_R(s + kappa_j)')
    rec('      alpha_{p,j}(pi)-- the Satake parameters at the finite places, in the Euler product')
    rec('      a_n(pi)        -- the Dirichlet coefficients of L(s,pi)')
    rec('      epsilon(pi)    -- the root number of the functional equation (2.4)')
    rec('      N              -- the degree; pi^vee -- the contragredient')
    rec('      q(pi,s)        -- ### **THE ANALYTIC CONDUCTOR** (2.14), and it is disclosed here')
    rec('                        rather than left out: ### **IT IS THE ONE QUANTITY IN THIS SOURCE')
    rec('                        THAT TAKES A HEIGHT AS AN ARGUMENT** -- the error term O(log')
    rec('                        q(pi,iT)) -- ### **AND IT SITS IN A REMARK ABOUT ZERO COUNTING,')
    rec('                        N_pi(T), NOT IN THE EXPLICIT FORMULA.** ### The distinction is')
    rec('                        printed rather than leaned on, because (N3) turns on it.')

    rec('')
    rec('  ### (2c) THE SIX INDICES, WITH THE SAME THREE VERDICTS, AND CC (148) BESIDE THEM.')
    rec('  ' + '-' * 100)
    rec('    %-6s %-16s %-22s %-22s %s' % ('site', 'index', 'under CC (148), b464',
                                           'under the general source', 'moved'))
    rec('    ' + '-' * 100)
    moved = 0
    for site, index, verdict, heading, why in SITES:
        m = 'YES' if CC[site] != verdict else '--'
        moved += (CC[site] != verdict)
        rec('    %-6s %-16s %-22s %-22s %s' % (site, index, CC[site], verdict, m))
    rec('')
    for site, index, verdict, heading, why in SITES:
        rec('    %s %s -- ### **%s**' % (site, index, verdict))
        for chunk in re.findall(r'.{1,96}(?:\s|$)', why):
            rec('        %s' % chunk.strip())
    tally = {}
    for _s, _i, v, _h, _w in SITES:
        tally[v] = tally.get(v, 0) + 1
    rec('')
    rec('    ### ### **%s.**' % ' ### '.join('%s %d' % (k, tally[k]) for k in sorted(tally)))
    rec('    ### ### **AND %d OF THE SIX CELLS MOVE AGAINST b464\x27s CC (148) READ.**' % moved)
    rec('    ### ### **THAT IS THE COMPONENT\x27s REAL YIELD:** the six site indices are not properties')
    rec('    ### of `the explicit formula`; ### **THEY ARE PROPERTIES OF WHICH EXPLICIT FORMULA IS')
    rec('    ### READ.** ### A site can be `OF NO PARAMETER` against one pinned source and `A')
    rec('    ### PARAMETER` against another, and b464 said exactly that in advance about site (v).')

    rec('')
    rec('  ### (2d) THE REDUCTION, AS A TEST AND NOT A CLAIM.')
    rec('  ' + '-' * 100)
    rec('    %-6s %-16s %s' % ('site', 'index', 'heading'))
    rec('    ' + '-' * 88)
    none_bucket = []
    for site, index, verdict, heading, why in SITES:
        rec('    %-6s %-16s %s' % (site, index, heading))
        if heading not in HEADINGS:
            none_bucket.append(site)
    rec('')
    rec('    ### ### **INDICES UNDER NONE OF THE THREE HEADINGS : %d %s.**'
        % (len(none_bucket), none_bucket or ''))
    rec('    ### ### **THE HEIGHT FALLS UNDER THE THIRD, AS THE ORDER EXPECTED.**')
    rec('    ### ### **AND THE ORDER\x27s FAILURE CONDITION IS TESTED RATHER THAN ASSUMED AWAY:**')
    rec('    ### *if the general source carries a height or a truncation as a datum, the reading')
    rec('    ### fails.* ### **IT CARRIES BOTH, AND NEITHER AS A DATUM, AND HERE IS EACH:**')
    rec('      (1) THE TRUNCATION IS CARRIED -- explicitly, at line 2813, as the interpretation of a')
    rec('          conditionally convergent sum: `lim T->inf sum |rho| <= T`. ### **T IS BOUND BY THE')
    rec('          LIMIT.** ### It is not an argument of W[f], not an argument of T[f], and not a')
    rec('          datum of any object the formula takes in. ### **THE READING HOLDS.**')
    rec('      (2) A HEIGHT IS CARRIED -- at line 467, in `O(log q(pi,iT))`, where the analytic')
    rec('          conductor q(pi,s) is evaluated at s = iT. ### **THAT IS A HEIGHT AS AN ARGUMENT,')
    rec('          AND IT IS DISCLOSED.** ### But it appears in a REMARK ABOUT THE ZERO-COUNTING')
    rec('          FUNCTION N_pi(T), ### **NOT IN THE EXPLICIT FORMULA THIS COMPONENT READS.**')
    rec('          ### ### **SO THE READING HOLDS FOR THE STATEMENT READ AND WOULD NOT HOLD FOR THE')
    rec('          ### COUNTING FUNCTION**, and that boundary is the honest form of the answer.')
    rec('    ### ### **NO SITE IS ENTERED. ### ROW U1 IS FROZEN AT SIX BY b409 AND IS NOT WRITTEN.**')
    rec('    ### ### **NO BRIDGE IS TYPED.**')
    return tally, moved, none_bucket


def expectations(out, by, noRow, tally, moved, none_bucket):
    rec('')
    rec('=' * 104)
    rec('THE EXPECTATIONS, SCORED.')
    rec('=' * 104)
    n1_moved = sum(1 for o in out if not o['standin'] and o['b464_grade'] == 'NOT THE CLAIM')
    sc = {}
    sc['N1'] = dict(navigator='at least three of the six move to DERIVES or INTERFACES under the '
                              'concordance’s terminal, and at most three survive as matters',
                    verdict='REFUTED -- %d OF THE SIX MOVE' % n1_moved,
                    note='the concordance assigns a row to %d of the eight, so there is no terminal '
                         'to re-grade any of them against; all six survive as matters and the SHELL '
                         'survives as a seventh' % (8 - noRow))
    sc['N2'] = dict(navigator='(v) is A PARAMETER, (vi) A COORDINATE OF ONE, (ii) stays OF NO PARAMETER',
                    verdict='HELD ON ALL THREE',
                    note='pi is quantified over in the source’s own words; Q(pi) is its conductor '
                         'and for GL(1) the conductor is the modulus; the only T is bound in a limit')
    sc['N3'] = dict(navigator='every index falls under one of the three headings and none under none',
                    verdict='HELD -- %d under none' % len(none_bucket),
                    note='and the failure condition was tested: the source carries the truncation '
                         'explicitly and carries a height in q(pi,iT), and NEITHER is a datum of the '
                         'explicit formula — the height sits in a remark about N_pi(T)')
    sc['seat'] = dict(
        N1='REFUTED, and the seat argued it on the face BEFORE the read -- it predicted 0 of 6 would '
           'move, on the ground that section 25.8’s seven rows are about none of the eight '
           'subjects. ### THE PREDICTION IS EXACT',
        N2='HELD on all three, as the seat expected',
        N2b='THE SEAT’S FOURTH PREDICTION, WHICH THE ORDER DID NOT ASK FOR: that (iii) and (iv) '
            'would move from A COORDINATE OF ONE to OF NO PARAMETER, because the general source’s '
            'test class is cut by analyticity and a growth bound and not by compact support. '
            '### HELD -- both moved',
        N3='HELD, and the seat named the one risk in advance: the analytic conductor q(pi,iT). '
           '### It is disclosed and it does not overturn the reading')
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, sc[k]['navigator']))
        rec('       ### ### **%s**' % sc[k]['verdict'])
        for chunk in re.findall(r'.{1,94}(?:\s|$)', sc[k]['note']):
            rec('       %s' % chunk.strip())
    rec('')
    rec('  ### ### **THE SEAT\x27s OWN, FROM THE FACE:**')
    for k in ('N1', 'N2', 'N2b', 'N3'):
        rec('    (%s)' % k)
        for chunk in re.findall(r'.{1,94}(?:\s|$)', sc['seat'][k]):
            rec('        %s' % chunk.strip())
    return sc


def main():
    out, by, noRow = component1()
    tally, moved, none_bucket = component2()
    sc = expectations(out, by, noRow, tally, moved, none_bucket)
    rec('')
    rec('=' * 104)
    rec('  ### ### **NO BRIDGE TYPED. ### NO SITE ENTERED. ### ROW U1 UNEDITED. ### NO ERRATUM')
    rec('  ### ### DRAFTED. ### KERNELS READ, NOT RUN. ### `h2` WHERE THE DEPOSIT LEFT IT.**')
    rec('=' * 104)
    io.open(os.path.join(D, 'b467_components.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(items=out, by_grade=by, no_row=noRow, rows=len(SURVEY['concordance']),
                   control_fired=SURVEY['control_fired'], control_rows=SURVEY['control_rows']),
              io.open(os.path.join(D, 'b467_concordance.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(dict(sites=[dict(site=s, index=i, verdict=v, heading=h, why=w)
                          for s, i, v, h, w in SITES],
                   tally=tally, moved_against_cc=moved, cc=CC, none_bucket=none_bucket,
                   headings=list(HEADINGS)),
              io.open(os.path.join(D, 'b467_params.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(sc, io.open(os.path.join(D, 'b467_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
