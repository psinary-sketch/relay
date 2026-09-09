# -*- coding: utf-8 -*-
"""b376_prior.py -- COMPONENT 1: ### **THE CORPUS'S OWN PRIOR ATTEMPT, HEARD FIRST.**

### The order: ### **read the census document that carries the third test at content. ### Quote whatever
### definition it states, verbatim, with its location; state what test it ACTUALLY APPLIES, read from its
### OPERATION and not from its prose; and state whether the two agree.**

### ### **THIS IS NOT A COUNT AND IT DOES NOT OUTVOTE ONE.** ### If the census states a definition
### explicitly, that definition is the corpus's own prior attempt at the ruling this act is gathering
### evidence for, and it is ### **QUOTED INTO THE EVIDENCE** ### rather than outvoted by any tally.

### ### **`READ FROM ITS OPERATION` IS TAKEN LITERALLY.** ### The stated definition is read from `§0`'s
### table. ### The applied test is read THREE ways, all from the document itself:
###   (1) the `OPERATIONALISED:` line -- what the detector was TOLD to test;
###   (2) the recorded detector output and the hand-correction the census applied AFTER it;
###   (3) ### **THE OPERATIONALISED PREDICATE RE-APPLIED HERE, NOW, OVER THE SAME CORPUS**, and its
###       membership compared against the census's own printed list.
### ### **(3) IS THE ONE THAT CANNOT BE ARGUED WITH**, because it runs the census's own stated operation
### and prints where the census's own answer and its own operation part company.

### ### **NO DOCUMENT IS REPAIRED, NO CLASS IS RULED, NO ROW IS EDITED AND THE CENSUS IS NOT TOUCHED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE CENSUS'S OWN OPERATIONALISATION, TRANSCRIBED INTO CODE FROM ITS OWN WORDS.**
# ###   `(i) = an ``Abstract`` heading or an ORCID block`
# ###   `(ii) = a heading matching ``correspondence``
# ###   `size floor ``6 KB``
# ### ### **AND NOTHING ELSE, BECAUSE THE LINE SAYS NOTHING ELSE.** ### Clause `(iii)` of the stated
# ### definition has ### **NO OPERATIONAL COUNTERPART ON THAT LINE AT ALL**, and that absence is a
# ### finding this tool prints rather than a hole this tool fills.
OP_I_ABSTRACT = re.compile(r'^#{1,6}[ \t]*.*\babstract\b', re.I | re.M)
OP_I_ORCID = re.compile(r'\bORCID\b', re.I)
OP_II_CORR = re.compile(r'^#{1,6}[ \t]*.*\bcorrespondence\b', re.I | re.M)
OP_SIZE_FLOOR = 6 * 1024

# ### **THE HAND-CORRECTION THE CENSUS RECORDED, WHICH IS NOT ON THE OPERATIONALISED LINE.**
LOGS_REMOVED = ('OPEN_TRAILS', 'FINDINGS', 'VERIFICATION_LOOM', 'CONVERGENCE')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(('git', '-C', PP) + a, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def quote(hint):
    """### **THE ANCHOR IS READ FROM THE FILE. ### THE LINE NUMBER IS NEVER TYPED.**"""
    n, line = AF.find(CENSUS, hint)
    return n, line


def census_sixteen():
    """### **THE CENSUS'S OWN PRINTED ANSWER, PARSED FROM ITS OWN TABLE, NOT RETYPED.**"""
    n, _ = quote('### **THE SIXTEEN KEYSTONES** *(last content update = git log,')
    txt = io.open(CENSUS, encoding='utf-8', errors='replace').read().split(chr(10))
    names = []
    for row in txt[n:]:
        if row.startswith('---') or row.startswith('## '):
            break
        m = re.match(r'^\|\s*`([^`]+)`\s*\|', row)
        if m:
            names.append(m.group(1))
    return names


def apply_operation(rels):
    """### **THE CENSUS'S OWN OPERATIONALISED PREDICATE, RE-APPLIED, EXACTLY AS ITS LINE WRITES IT.**"""
    out = []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            raw = io.open(p, 'rb').read()
            txt = raw.decode('utf-8', 'replace')
        except OSError:
            continue
        i_abs = bool(OP_I_ABSTRACT.search(txt))
        i_orc = bool(OP_I_ORCID.search(txt))
        ii = bool(OP_II_CORR.search(txt))
        size = len(raw)
        out.append(dict(file=rel, base=os.path.basename(rel)[:-3],
                        clause_i=(i_abs or i_orc), by_abstract=i_abs, by_orcid=i_orc,
                        clause_ii=ii, bytes=size, over_floor=(size >= OP_SIZE_FLOOR),
                        operational_keystone=((i_abs or i_orc) and ii and size >= OP_SIZE_FLOOR)))
    return out


def main():
    rec('=' * 100)
    rec('b376 -- COMPONENT 1: ### **THE CORPUS`S OWN PRIOR ATTEMPT, HEARD FIRST.**')
    rec('=' * 100)
    rec('')
    rec('  ### **THE DOCUMENT, LOCATED AT CONTENT:** ### `%s`'
        % os.path.relpath(CENSUS, PP).replace(os.sep, '/'))
    rec('  ### ### **IT IS QUOTED AND NOT TOUCHED.**')
    rec('')

    # ------------------------------------------------------------------ (1) THE STATED DEFINITION
    rec('-' * 100)
    rec('  ### (1) THE DEFINITION IT STATES. ### **VERBATIM, WITH ITS LOCATION.**')
    rec('-' * 100)
    stated = {}
    for tag, hint in (('KEYSTONE', '| ### **KEYSTONE** | (i) states results for external readers'),
                      ('KEYSTONE-CANDIDATE', '| ### **KEYSTONE-CANDIDATE** | (i) + (iii)'),
                      ('SUPPORT', '| **SUPPORT** | working papers, notes, consults')):
        n, line = quote(hint)
        stated[tag] = dict(line=n, text=line.strip())
        rec('    ### **%s** -- `THE_KEYSTONE_CENSUS.md` line %d' % (tag, n))
        rec('      | %s' % line.strip())
    nh, lh = quote('## §0 — THE CATEGORY, DEFINED BEFORE COUNTING')
    rec('')
    rec('    ### its own heading, line %d :' % nh)
    rec('      | %s' % lh.strip())
    rec('    ### ### **SO THE CENSUS DOES STATE A DEFINITION EXPLICITLY, AND STATES IT BEFORE COUNTING,')
    rec('    ### ### AND SAYS WHY: ### `so the count is reproducible`.**')
    rec('    ### ### ### **THIS IS THE CORPUS`S OWN PRIOR ATTEMPT AT THE RULING. ### IT IS EVIDENCE IN')
    rec('    ### ### ### THIS ACT, NOT A CANDIDATE TO BE OUTVOTED BY A TALLY.**')

    # ------------------------------------------------------- (2) THE OPERATIONALISATION IT PRINTS
    rec('')
    rec('-' * 100)
    rec('  ### (2) WHAT IT SAYS IT APPLIES. ### **THE `OPERATIONALISED` LINE, VERBATIM.**')
    rec('-' * 100)
    no, lo = quote('**OPERATIONALISED:** (i) = an `Abstract` heading or an ORCID block')
    rec('    `THE_KEYSTONE_CENSUS.md` line %d :' % no)
    rec('      | %s' % lo.strip())

    rec('')
    rec('    ### **CLAUSE BY CLAUSE, THE STATED TEST AGAINST ITS OWN OPERATIONALISATION:**')
    rec('')
    rec('      %-6s %-52s %s' % ('clause', 'what the definition says', 'what the operation does'))
    rec('      %s' % ('-' * 96))
    mapping = [
        ('(i)', 'states results for external readers',
         'an `Abstract` heading OR an ORCID block'),
        ('(ii)', 'closes with a Correspondence table naming its terminals',
         'a heading matching `correspondence`'),
        ('(iii)', "is cited by its cluster's spine or the trunk",
         '### ### **NOTHING. ### NOT OPERATIONALISED AT ALL.**'),
        ('--', '### ### **NOTHING. ### THE DEFINITION NAMES NO SIZE.**',
         'a size floor of `6 KB`'),
    ]
    for c, s, o in mapping:
        rec('      %-6s %-52s %s' % (c, s[:52], o))
    rec('')
    rec('    ### ### **THREE DIVERGENCES, AND EACH IS A DIFFERENT KIND:**')
    rec('    ### ### **(a) `(i)` IS REPLACED BY A PROXY.** ### `states results for external readers` is a')
    rec('    ###     judgement about the writing; ### **AN `Abstract` HEADING IS A TYPOGRAPHIC FACT.** ### A')
    rec('    ###     document can state results for external readers in plain prose and fail the proxy, and')
    rec('    ###     a document can carry an `Abstract` heading over notes and pass it.')
    rec('    ### ### **(b) `(ii)` IS NARROWED FROM A TABLE TO A HEADING.** ### The definition requires a')
    rec('    ###     Correspondence table ### **NAMING ITS TERMINALS**; ### the operation requires only that')
    rec('    ###     ### **A HEADING WITH THAT WORD EXISTS.** ### The naming half is not tested.')
    rec('    ### ### **(c) `(iii)` IS DROPPED AND A SIZE FLOOR IS ADDED.** ### The citation clause -- the')
    rec('    ###     only clause in the definition that looks OUTSIDE the document -- ### **HAS NO')
    rec('    ###     ### OPERATIONAL COUNTERPART**, and a criterion the definition never mentions is')
    rec('    ###     applied in its place.')
    rec('    ### ### ### **SO THE OPERATION IS NOT A NARROWING OF THE DEFINITION. ### IT IS A DIFFERENT')
    rec('    ### ### ### TEST THAT OVERLAPS IT.**')

    # ---------------------------------------------- (3) THE CORRECTION THE CENSUS APPLIED BY HAND
    rec('')
    rec('-' * 100)
    rec('  ### (3) AND A FOURTH TEST, APPLIED AFTER THE DETECTOR AND RECORDED BY THE CENSUS ITSELF.')
    rec('-' * 100)
    nc, lc = quote('> **The detector returned 20 for KEYSTONE.')
    rec('    `THE_KEYSTONE_CENSUS.md` line %d :' % nc)
    for seg in re.findall(r'.{1,92}(?:\s|$)', lc.strip()):
        rec('      | %s' % seg.rstrip())
    rec('')
    rec('    ### ### **THE CENSUS RAN ITS OPERATION, GOT `20`, AND THEN REMOVED FOUR BY A RULE THAT IS')
    rec('    ### ### NOT ON THE OPERATIONALISED LINE** -- ### `logs, which §0 assigns to SUPPORT`. ### That')
    rec('    ### ### rule is in the stated definition`s SUPPORT row and in no operational clause.')
    rec('    ### ### ### **THE CENSUS THEREFORE APPLIED THE STATED DEFINITION AND ITS OPERATIONALISATION')
    rec('    ### ### ### AT DIFFERENT MOMENTS, TO DIFFERENT ENDS, AND SAID SO.** ### The honesty is on the')
    rec('    ### ### ### record; ### **THE MIXING IS THE FINDING.**')

    # ------------------------------------------------ (4) THE OPERATION RE-APPLIED, HERE AND NOW
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE OPERATION RE-APPLIED. ### **ITS OWN PREDICATE, ITS OWN CORPUS, RUN HERE.**')
    rec('-' * 100)
    rels = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    scored = apply_operation(rels)
    op_set = [x for x in scored if x['operational_keystone']]
    sixteen = census_sixteen()
    rec('    documents swept (tracked markdown, PLACE-papers)     : %d' % len(scored))
    rec("    the census`s own printed answer                      : %d" % len(sixteen))
    rec('    ### **ITS OWN OPERATION, RE-APPLIED AT THE HEAD**        : ### **%d**' % len(op_set))
    rec('')
    op_bases = set(x['base'] for x in op_set)
    six = set(sixteen)
    reproduced = sorted(six & op_bases)
    lost = sorted(six - op_bases)
    gained = sorted(op_bases - six)
    rec('    ### **OF THE SIXTEEN, REPRODUCED BY THE OPERATION : %d ### / ### NOT REPRODUCED : %d**'
        % (len(reproduced), len(lost)))
    rec('    ### **AND THE OPERATION RETURNS %d DOCUMENT(S) THE CENSUS DID NOT NAME.**' % len(gained))
    rec('')
    if lost:
        rec('    ### ### **NAMED BY THE CENSUS, REFUSED BY THE CENSUS`S OWN OPERATION -- WITH WHY:**')
        byb = {}
        for x in scored:
            byb.setdefault(x['base'], x)
        for b in lost:
            x = byb.get(b)
            if not x:
                rec('      %-44s ### NOT FOUND IN THE TRACKED SWEEP AT THE HEAD' % b)
                continue
            why = []
            if not x['clause_i']:
                why.append('no `Abstract` heading and no ORCID block')
            if not x['clause_ii']:
                why.append('no heading matching `correspondence`')
            if not x['over_floor']:
                why.append('under the 6 KB floor (%d bytes)' % x['bytes'])
            rec('      %-44s %s' % (b[:44], '; '.join(why) or 'no reason -- it passes'))
    if gained:
        rec('')
        rec('    ### ### **RETURNED BY THE OPERATION, NOT NAMED BY THE CENSUS:**')
        for b in gained:
            rec('      %s' % b)
    rec('')
    rec('    ### ### **AND THE FOUR THE CENSUS REMOVED BY HAND, TESTED AGAINST ITS OWN OPERATION:**')
    for nm in LOGS_REMOVED:
        hits = [x for x in scored if nm in x['base']]
        for h in hits[:2]:
            rec('      %-44s operation says : %s'
                % (h['base'][:44], 'KEYSTONE' if h['operational_keystone'] else 'not keystone'))

    # ---------------------------------------------------------------------- (5) DO THE TWO AGREE
    rec('')
    rec('-' * 100)
    rec('  ### (5) DO THE STATED DEFINITION AND THE APPLIED TEST AGREE.')
    rec('-' * 100)
    agree = (len(lost) == 0 and len(gained) == 0)
    rec('    ### ### **ANSWER : %s**'
        % ('THEY AGREE' if agree else 'NO. ### THEY DO NOT AGREE, AND THEY DO NOT AGREE IN FOUR PLACES'))
    rec('    ### **(a)** ### clause `(iii)` of the stated definition is ### **NEVER APPLIED**.')
    rec('    ### **(b)** ### a size floor the stated definition ### **NEVER MENTIONS** ### is applied.')
    rec('    ### **(c)** ### clauses `(i)` and `(ii)` are applied ### **THROUGH PROXIES THAT ARE NOT THEM.**')
    rec('    ### **(d)** ### and the published figure is the operation`s output ### **CORRECTED BY HAND**')
    rec('    ###     ### **WITH A CLAUSE FROM THE STATED DEFINITION`S OTHER ROW.**')
    rec('')
    rec('    ### ### ### **AND HERE IS WHY THIS COMPONENT COMES FIRST.** ### The stated definition is')
    rec('    ### ### ### **NOT ONE TEST.** ### Its clause `(ii)` -- a correspondence table naming')
    rec('    ### ### ### terminals -- is ### **THE APPARATUS QUESTION.** ### Its clauses `(i)` and `(iii)`')
    rec('    ### ### ### -- states results for external readers, is cited by its cluster`s spine -- are')
    rec('    ### ### ### ### **THE ROLE QUESTION.** ### They are joined by `and`, so a document must')
    rec('    ### ### ### satisfy both to pass, ### **AND A DOCUMENT THAT FAILS IS NOT TOLD WHICH ONE IT')
    rec('    ### ### ### FAILED.**')
    rec('    ### ### ### ### **THE CONFLICT THE THREE TESTS PRODUCE WAS ALREADY INSIDE THE FIRST ONE.**')
    rec('    ### This is `(E1)` as the face registered it, and it is met by quotation, not by count.')
    rec('')
    rec('    ### **WHAT THIS COMPONENT IS DEAF TO:** ### it reads the census AS WRITTEN AT THE HEAD. ### If')
    rec('    ### the census`s sixteen were correct against the corpus AS IT STOOD ON `2026-08-12`, a')
    rec('    ### document edited since would show here as a divergence that was never one. ### **THAT IS')
    rec('    ### ### A LIMIT OF THIS READ AND IT IS NOT REPAIRED HERE** ### (`b372`: a figure that was')
    rec('    ### exact is not a figure that is wrong).')
    rec('=' * 100)

    p = run_clock.write(D, 'b376_prior_notes', LINES)
    io.open(os.path.join(D, 'b376_prior.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(stated=stated, stated_heading_line=nh,
                        operationalised_line=no, operationalised_text=lo.strip(),
                        correction_line=nc, correction_text=lc.strip(),
                        mapping=[dict(clause=c, states=s, operates=o) for c, s, o in mapping],
                        swept=len(scored), census_named=sixteen,
                        operation_returns=sorted(op_bases),
                        reproduced=reproduced, not_reproduced=lost, extra=gained,
                        agree=agree, scored=scored,
                        run_file=os.path.basename(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
