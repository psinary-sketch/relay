# -*- coding: utf-8 -*-
"""b375_population.py -- COMPONENT 1: THE POPULATION, READ FROM CONTENT AND NEVER FROM A PATH.

### ### **THREE COLUMNS, NEVER MERGED:** ### (1) the document's DECLARED class line, quoted verbatim;
### (2) the ORDER'S class by the order's own rubric, with the sentence that decided it quoted; (3)
### whether `THE_KEYSTONE_CENSUS.md` names it among the sixteen its own test produced.
### ### ### **THE WORD `KEYSTONE` NAMES THREE DIFFERENT TESTS IN THIS RECORD** -- the author-ruled
### taxonomy's `Tier K` (certification at a pin), the order's rubric (synthesis against other content),
### and the existing census's test -- and ### **THIS FILE RECONCILES NONE OF THEM.**
### ### **A DECLARED CLASS IS QUOTED, NEVER OVERWRITTEN AND NEVER TRANSLATED.**
### ### **AND A DOCUMENT WHOSE OWN TEXT DOES NOT DECIDE IT IS `OTHER`, NOT `SUPPORT` BY DEFAULT** --
### defaulting to the larger class would manufacture the census's own answer.
### ### **NOTHING IS REPAIRED AND NOTHING IS RECLASSIFIED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import hedge_audit as HA         # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE DECLARED LINE, AS THE CORPUS WRITES IT.**
DECL = re.compile(r'^\*\*DOCUMENT CLASS\b.*$', re.M)
TIER = re.compile(r'TIER ([A-Z])\b|NOT PLACED')

# ### **A SELF-DESCRIBING SENTENCE IS ONE THAT NAMES THE DOCUMENT ITSELF.** ### The order's rubric
# ### classifies by ### **WHAT THE DOCUMENT DOES**, so only a sentence in which the document speaks
# ### about itself can decide it. ### **A SENTENCE ABOUT THE SUBJECT MATTER DECIDES NOTHING.**
SELF = re.compile(r'\b(this document|this file|this paper|this register|this ledger|this census|'
                  r'this note|this record|this map|this synthesis|this consult|this report)\b|'
                  r'^\*\*PURPOSE:\*\*|\*\*PURPOSE:\*\*', re.I)

# ### the rubric's own words, turned into three finite lists. ### **A WORD OFF A LIST IS INVISIBLE.**
KEY_WORDS = re.compile(r'\b(synthesiz|synthesis|organiz|cross-system|against other|'
                       r'draws together|brings together|consolidat|integrat)\w*', re.I)
SUP_WORDS = re.compile(r'\b(gathers|collects|records the research|working note|consult|seed|'
                       r'dry-run|exploratory|notes on|as of|snapshot|inventory|survey)\w*', re.I)
LED_WORDS = re.compile(r'\b(append-only|running record|ledger|log of|entries are appended|'
                       r'never edited, only appended)\w*', re.I)
BLOCKMARK = re.compile(r'<!--\s*b\d{2,4}\b')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def census_sixteen():
    txt = io.open(CENSUS, encoding='utf-8', errors='replace').read()
    rows = txt.split(chr(10))
    start = None
    for i, ln in enumerate(rows):
        if 'THE SIXTEEN KEYSTONES' in ln:
            start = i
            break
    names = []
    if start is not None:
        for ln in rows[start:start + 40]:
            m = re.match(r'\|\s*`([A-Za-z0-9_]+)`\s*\|', ln)
            if m:
                names.append(m.group(1))
    return set(names)


def declared_line(txt):
    m = DECL.search(txt)
    if not m:
        return None, None
    line = m.group(0).strip()
    t = TIER.search(line)
    tier = ('NOT PLACED' if (t and t.group(0) == 'NOT PLACED')
            else ('TIER ' + t.group(1) if t else 'UNPARSED'))
    return line, tier


def order_class(txt):
    """### **THE ORDER'S RUBRIC, APPLIED TO SELF-DESCRIBING SENTENCES ONLY.**
    ### Returns (class, deciding sentence, why)."""
    n_marks = len(BLOCKMARK.findall(txt))
    sents = HA._sentences(txt)
    self_sents = [s for s in sents if SELF.search(s)]
    # ### LEDGER first: a running append-only record of the programme's own acts.
    for s in self_sents:
        if LED_WORDS.search(s):
            return 'LEDGER', s.strip()[:220], 'a self-describing sentence says it is a running record'
    if n_marks >= 5:
        for s in sents:
            if BLOCKMARK.search(s):
                return ('LEDGER', s.strip()[:220],
                        'the document carries %d dated append-only block marks' % n_marks)
    for s in self_sents:
        if KEY_WORDS.search(s):
            return ('KEYSTONE', s.strip()[:220],
                    "a self-describing sentence says it synthesizes or organizes")
    for s in self_sents:
        if SUP_WORDS.search(s):
            return ('SUPPORT', s.strip()[:220],
                    "a self-describing sentence says it gathers or records research")
    return ('OTHER', None,
            ("the document's own text does not say what it does"
             if not self_sents else
             "the document describes itself but in none of the rubric's terms"))


def main():
    rec('=' * 100)
    rec('b375 -- COMPONENT 1: THE POPULATION. ### **THREE COLUMNS, NEVER MERGED.**')
    rec('=' * 100)
    rec('')
    rec('  ### **THE PREDICATES, DECLARED BEFORE THE SWEEP SO THEY CAN BE DISAGREED WITH:**')
    rec('  ###   A SELF-DESCRIBING SENTENCE : %s' % SELF.pattern[:120])
    rec('  ###     ### ### **ONLY A SENTENCE IN WHICH THE DOCUMENT SPEAKS ABOUT ITSELF CAN DECIDE WHAT')
    rec('  ###     ### ### THE DOCUMENT DOES.** ### A sentence about the subject matter decides nothing.')
    rec('  ###   KEYSTONE words : %s' % KEY_WORDS.pattern[:110])
    rec('  ###   SUPPORT  words : %s' % SUP_WORDS.pattern[:110])
    rec('  ###   LEDGER   words : %s' % LED_WORDS.pattern[:110])
    rec('  ### ### **A WORD OFF A LIST IS INVISIBLE. ### THAT IS THE REACH, NOT A DEFECT HIDDEN**')
    rec('  ### ### (`PREDICATE_ONE_SHAPE`).')
    rec('')
    sixteen = census_sixteen()
    rels = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    rec('-' * 100)
    rec('  ### THE SWEEP. ### **%d TRACKED MARKDOWN DOCUMENTS, INCLUDING ARCHIVES AND THE DEPOSIT.**'
        % len(rels))
    rec('-' * 100)
    out = []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        line, tier = declared_line(txt)
        cls, sent, why = order_class(txt)
        base = os.path.basename(rel)[:-3]
        out.append(dict(file=rel, declared_line=line, declared_tier=tier,
                        order_class=cls, deciding_sentence=sent, why=why,
                        basis=('DECLARED+READ' if line else 'READ'),
                        named_by_existing_census=(base in sixteen),
                        in_clusters_dir=rel.startswith('clusters/'),
                        frozen=(rel.startswith('outputs/') or rel.startswith('archive/'))))
    ndecl = sum(1 for x in out if x['declared_line'])
    rec('    ### ### **DOCUMENTS DECLARING A CLASS : %d ### / ### NOT DECLARING : %d**'
        % (ndecl, len(out) - ndecl))
    tally = {}
    for x in out:
        tally[x['order_class']] = tally.get(x['order_class'], 0) + 1
    rec("    ### ### **THE ORDER'S CLASS, ACROSS THE WHOLE POPULATION : %s**" % tally)
    dt = {}
    for x in out:
        if x['declared_tier']:
            dt[x['declared_tier']] = dt.get(x['declared_tier'], 0) + 1
    rec('    ### ### **THE DECLARED TIERS, AS THE DOCUMENTS THEMSELVES WRITE THEM : %s**' % dt)
    rec('    ### ### **NAMED BY THE EXISTING CENSUS AMONG ITS SIXTEEN : %d**'
        % sum(1 for x in out if x['named_by_existing_census']))

    # ---- the three tests, side by side ------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### THE THREE TESTS, SIDE BY SIDE. ### **THE DISAGREEMENT IS THE PRODUCT.**')
    rec('-' * 100)
    tierK = [x for x in out if x['declared_tier'] == 'TIER K']
    orderK = [x for x in out if x['order_class'] == 'KEYSTONE']
    censK = [x for x in out if x['named_by_existing_census']]
    rec('    ### **TEST (i) -- the author-ruled taxonomy, `Tier K` (certification at a pin):** ### %d'
        % len(tierK))
    rec("    ### **TEST (ii) -- the order's rubric (synthesis against other content):** ### %d"
        % len(orderK))
    rec('    ### **TEST (iii) -- `THE_KEYSTONE_CENSUS.md`s own sixteen:** ### %d' % len(censK))
    sK, sO, sC = (set(x['file'] for x in tierK), set(x['file'] for x in orderK),
                  set(x['file'] for x in censK))
    rec('')
    rec('    ### ### **AGREEMENT BETWEEN THE THREE:**')
    rec('    ###   in all three                : %d' % len(sK & sO & sC))
    rec('    ###   taxonomy `Tier K` only      : %d' % len(sK - sO - sC))
    rec("    ###   the order's rubric only     : %d" % len(sO - sK - sC))
    rec('    ###   the existing census only    : %d' % len(sC - sK - sO))
    rec('    ###   taxonomy and census, not the order : %d' % len((sK & sC) - sO))
    rec('    ###   the order and census, not the taxonomy : %d' % len((sO & sC) - sK))
    rec('    ###   the order and taxonomy, not the census : %d' % len((sO & sK) - sC))
    rec('    ### ### ### **THESE ARE NOT THE SAME PARTITION, AND NOTHING HERE RECONCILES THEM.**')

    # ---- the declarers, quoted ---------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### THE DECLARERS, EACH CLASS LINE QUOTED VERBATIM AND NEVER TRANSLATED.')
    rec('-' * 100)
    for x in out:
        if not x['declared_line']:
            continue
        rec('')
        rec('    `%s`' % x['file'])
        rec('        DECLARED : %s' % x['declared_tier'])
        rec('        | %s' % x['declared_line'][:210])
        rec("        THE ORDER'S CLASS (a SEPARATE column, not a translation) : %s" % x['order_class'])
        if x['deciding_sentence']:
            rec('        | %s' % x['deciding_sentence'][:180])
        else:
            rec('        ### %s' % x['why'])

    # ---- the directory-versus-content disagreements -------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### WHERE THE DIRECTORY SUGGESTS ONE CLASS AND THE CONTENT READS AS ANOTHER.')
    rec('  ### ### **REPORTED AT FULL PROMINENCE AND NOT RECLASSIFIED BY THIS ACT.**')
    rec('-' * 100)
    dis = []
    for x in out:
        if x['in_clusters_dir'] and x['order_class'] != 'KEYSTONE':
            dis.append((x, "it sits under `clusters/` and its own text does not say it synthesizes"))
        if (not x['in_clusters_dir']) and x['order_class'] == 'KEYSTONE' \
                and not x['file'].startswith('archive/'):
            dis.append((x, "its own text says it synthesizes and it does not sit under `clusters/`"))
    for x, why in dis:
        rec('    %-62s %-9s ### %s' % (x['file'][:62], x['order_class'], why))
    rec('    ### ### **DISAGREEMENTS : %d** ### -- each left exactly as it is.' % len(dis))

    rec('')
    rec('=' * 100)
    rec('  ### **NO DOCUMENT WAS REPAIRED, RECLASSIFIED OR REWRITTEN.**')
    rec('  ### **NO DECLARED CLASS WAS OVERWRITTEN OR TRANSLATED.**')
    rec('  ### **AND NO DOCUMENT WAS DEFAULTED TO `SUPPORT`** -- a document whose own text does not')
    rec('  ### decide it is `OTHER` with the reason printed.')
    rec('=' * 100)
    p = run_clock.write(D, 'b375_population_notes', LINES)
    io.open(os.path.join(D, 'b375_population.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(documents=len(out), declared=ndecl, not_declared=len(out) - ndecl,
                        order_tally=tally, declared_tiers=dt,
                        tests=dict(taxonomy_tier_k=sorted(sK), order_rubric=sorted(sO),
                                   existing_census=sorted(sC),
                                   all_three=sorted(sK & sO & sC)),
                        disagreements=[dict(file=x['file'], order_class=x['order_class'], why=w)
                                       for x, w in dis],
                        fifth_words=0, reclassified=0, translated=0,
                        rows=out,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
