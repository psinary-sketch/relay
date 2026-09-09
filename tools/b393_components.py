# -*- coding: utf-8 -*-
"""b393_components.py -- THE FIVE CLUSTERS SURFACED, AND TWO PRICINGS.

### ### **THIS FILE EDITS NOTHING.** ### It reads, measures and prices. ### Its product is a list
### the closing message prints, because ### **A FINDING THAT REACHES ONLY THE BANK IS A FINDING THE
### ### NAVIGATOR HAS NOT SEEN** -- which is the whole reason this act exists.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
ERRATA = os.path.join(PP, 'ERRATA.md')
README = os.path.join(PP, 'README.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
B388BANK = os.path.join(D, 'b388_the_map_refreshed.txt')
B391BANK = os.path.join(D, 'b391_the_phantom_repaired.txt')
OUT = os.path.join(D, 'b393_components.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


E = json.load(io.open(os.path.join(D, 'b393_reads.json'), encoding='utf-8'))


# ==================================================================================================
def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- THE FIVE CLUSTERS, SURFACED.')
    bar('=')
    rec('  ### ### **`b388` FOUND THESE AND `b391` REPORTED THEM, AND NEITHER PUT THEM IN FRONT OF')
    rec('  ### ### THE NAVIGATOR.** ### Both measured ### **MEMBERSHIP ONLY.** ### The order names')
    rec('  ### five kinds of change and one of them -- ### *anchor no longer the document a reader')
    rec('  ### meets first* ### -- ### **HAS NEVER BEEN TESTED.** ### It is tested here.')
    rec()
    rec('  ### **THE TEST, AND ITS LIMIT.** ### A cluster changed by anchor if a member it GAINED')
    rec('  ### is a census keystone ### **NEWER** ### than the best anchor ### **AND** ### carrying')
    rec('  ### ### **MORE PINS** -- the census`s own two figures. ### **IT CAN ONLY RANK DOCUMENTS')
    rec('  ### ### THE CENSUS LISTS**, so where an anchor is not among the sixteen the question is')
    rec('  ### ### **UNDECIDABLE FROM THE CENSUS** ### and is reported as that, not as a pass.')
    rec()
    # ### **THE ORDER NAMES TWO SOURCES AND THEY HOLD DIFFERENT THINGS.** ### `b391`'s bank
    # ### records each cluster with its verdict and member count; `b388`'s records the per-document
    # ### assignment that produced it. ### A first form looked for `b391`'s shape in `b388`'s bank
    # ### and found nothing five times over -- ### **A QUOTATION SOUGHT IN THE WRONG ACT IS NOT A
    # ### ### MISSING QUOTATION.**
    b391 = io.open(B391BANK, encoding='utf-8', errors='replace').read().split(chr(10))
    b388 = io.open(B388BANK, encoding='utf-8', errors='replace').read().split(chr(10))
    maplines = io.open(MAP, encoding='utf-8', errors='replace').read().split(chr(10))
    surfaced = []
    for c in E['s1']['clusters']:
        bar()
        rec('  ### **%s** ### -- `%s` by `%d`' % (c['cluster'], c['finding'], c['by']))
        bar()
        # ### **THE QUOTATION FROM THE ACT THAT FOUND IT.**
        q = next((ln for ln in b391
                  if c['cluster'] in ln and re.search(r'\*\*(GREW|NEW)\*\*', ln)), '')
        rec('    ### THE ACT THAT RECORDED IT -- `b391`\'s bank:')
        rec('      > %s' % (flat(q, 190)[3:] if q else '(not found)'))
        # ### **AND THE ORIGINAL FINDING, FROM `b388`'S OWN ASSIGNMENT LINES.**
        orig = [ln for ln in b388 if ('**%s**' % c['cluster']) in ln and '.md' in ln]
        rec('    ### THE ACT THAT FOUND IT -- `b388`\'s bank, %d assignment line(s):' % len(orig))
        for o in orig[:3]:
            rec('      > %s' % flat(o, 150)[3:])
        if c['map_line']:
            rec('    ### THE MAP ROW THAT SEATS IT -- `SPIRAL_MAP.md` line %d:' % c['map_line'])
            rec('      > %s' % flat(maplines[c['map_line'] - 1], 210))
        rec('    ### **WHAT CHANGED:** ### **MEMBERSHIP** ### -- it gained `%d`: %s'
            % (c['by'], ', '.join('`%s`' % g for g in c['gained'])))
        rec('    ### of those, census keystones : %s'
            % (', '.join('`%s`' % g for g in c['gained_keystones']) or 'none'))
        rec('    ### ### **THE ANCHOR QUESTION : %s**' % c['verdict'])
        for k in range(0, min(len(c['why']), 460), 150):
            rec('      %s' % c['why'][k:k + 150])
        surfaced.append(dict(cluster=c['cluster'], finding=c['finding'], by=c['by'],
                             verdict=c['verdict'], gained=c['gained'],
                             keystones=c['gained_keystones'], map_line=c['map_line'],
                             quote=flat(q, 190)[3:] if q else ''))
        rec()
    bar()
    from collections import Counter
    v = Counter(s['verdict'] for s in surfaced)
    rec('  ### ### **THE FIVE, BY VERDICT:**')
    for k in sorted(v):
        rec('      %-26s ### **`%d`**' % (k, v[k]))
    rec('  ### ### ### **FOUR DIFFERENT ANSWERS TO ONE QUESTION, AND THEY ARE NOT ADDED.** ###')
    rec('  ### ### ### Three of them are ways of ### **NOT ANSWERING** ### the anchor question and')
    rec('  ### ### ### only one is an answer to it.')
    rec()
    rec('  ### ### **CHANGED BY ANCHOR : `%d` OF `%d`.**'
        % (v.get('ANCHOR OVERTAKEN', 0), len(surfaced)))
    rec('  ### ### **`(L1)` EXPECTED AT LEAST TWO.**')
    if v.get('ANCHOR OVERTAKEN', 0) < 2:
        rec('  ### ### ### **`(L1)` IS REPORTED REFUTED.** ### **AN UNANSWERABLE CASE IS NOT')
        rec('  ### ### ### PROMOTED INTO AN AFFIRMATIVE ONE TO REACH TWO**, and the locked face')
        rec('  ### ### ### said the count was one before this component ran.')
    else:
        rec('  ### ### ### **`(L1)` IS MET.**')
    rec()
    rec('  ### ### **AND THE SHAPE OF THE UNANSWERABLE IS THE FINDING WORTH THE AUTHOR`S TIME:**')
    rec('  ###   `2` clusters ### **HAVE NO ANCHOR AT ALL** -- `(R17)` named none and `b388` did')
    rec('  ###   not invent one, so ### **A READER MEETING THEM MEETS A MEMBER LIST.**')
    rec('  ###   `1` cluster is ### **ANCHORED ON DOCUMENTS THE KEYSTONE CENSUS DOES NOT LIST**,')
    rec('  ###   while a census keystone joined it -- ### **THE ANCHOR AND THE MEMBERSHIP ARE NOW')
    rec('  ###   ### GRADED ON DIFFERENT SCALES.**')
    rec('  ### ### ### **NO CLUSTER IS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED.** ### THE')
    rec('  ### ### ### RESHAPING IS THE AUTHOR`S.')
    return dict(surfaced=surfaced, by_verdict=dict(v),
                anchor_changed=v.get('ANCHOR OVERTAKEN', 0), reshaped=0,
                l1=(v.get('ANCHOR OVERTAKEN', 0) >= 2))


# ==================================================================================================
def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- THE TWO RECORDS FAILING BOTH LIMBS, PRICED.')
    bar('=')
    s2 = E['s2']
    rec('  ### ### **`(R20)`\'S OBLIGATION:** ### every deposited record ### **EITHER** ### sits at')
    rec('  ### ### a version a citable claim uses ### **OR** ### carries a note saying it is')
    rec('  ### ### historical. ### **THERE IS NO THIRD STATE**, and these two are in it.')
    rec()
    out = {}
    # ---- 21432399 -----------------------------------------------------------------------------
    r = s2['21432399']
    bar()
    rec('  ### **`10.5281/zenodo.21432399`**')
    bar()
    rec('    what it deposited      : ### **%s**' % r['what'])
    rec('    at what version        : ### **manuscript `%s`**' % r['deposited_at'])
    rec('    the repository now     : ### **`%s`** ### (`REGISTRY.md` row `d1-1`, line %d)'
        % (r['repo_now'], r['registry_line']))
    ei, eln = AF.find(ERRATA, 'The deposited monograph (Zenodo record 21432399')
    rec('    its only naming        : `ERRATA.md` line %d' % ei)
    rec('      > %s' % flat(eln, 300))
    rec('    ### ### **FIVE MANUSCRIPT VERSIONS BEHIND THE REPOSITORY, AND THE CITABLE DEPOSIT IS')
    rec('    ### ### A DIFFERENT RECORD ENTIRELY** ### -- `21539167`, at manuscript `v5.10.2`.')
    rec()
    rec('    ### **REMEDY (a) -- A HISTORICAL NOTE ADDED TO THE RECORD.**')
    rec('      requires : ### **ONE LINE IN `REGISTRY.md`\'S DEPOSIT HISTORY** ### naming the')
    rec('      record, its manuscript version, and the record that superseded it. ### The version')
    rec('      is known, so ### **NOTHING NEEDS TO BE LOOKED UP.**')
    rec('      ### **WHAT IT DOES NOT BUY:** ### the record still sits at `v5.8` and a reader who')
    rec('      arrives at the DOI directly ### **STILL MEETS A FIVE-VERSION-OLD MANUSCRIPT.** ###')
    rec('      A note in the corpus does not travel to the platform.')
    rec('    ### **REMEDY (b) -- A NEW VERSION DEPOSITED AT A STATE A CITABLE CLAIM USES.**')
    rec('      requires : ### **A DEPOSIT WAVE** ### -- `(R20)`\'s first limb says a manuscript')
    rec('      wave deposits with its companion papers, so this is ### **NOT A ONE-RECORD ACT**;')
    rec('      and it requires the platform, which ### **HAS ANSWERED NOTHING ON SIX ROUTES SINCE')
    rec('      ### `b389`.**')
    rec('      ### **WHAT IT DOES NOT BUY:** ### it does not make `21432399` current -- ### **A')
    rec('      ### NEW VERSION DOES NOT RETIRE AN OLD RECORD, IT ONLY OUTRANKS IT** -- so the')
    rec('      historical note is still owed afterwards.')
    out['21432399'] = dict(deposited_at=r['deposited_at'], repo_now=r['repo_now'],
                           remedy_a='one line in REGISTRY.md; version known',
                           remedy_b='a deposit wave and a platform that answers',
                           note_still_owed_after_b=True)
    rec()
    # ---- 19675356 -----------------------------------------------------------------------------
    r = s2['19675356']
    bar()
    rec('  ### **`10.5281/zenodo.19675356`**')
    bar()
    rec('    what it deposited      : ### **%s**' % r['what'])
    rec('    at what version        : %s' % r['deposited_at'])
    rec('    the repository now     : ### **`%s`** ### (`REGISTRY.md` row `d1-7`, line %d)'
        % (r['repo_now'], r['registry_line']))
    rec('    its only naming        : `INVARIANCE_BARRIERS.md` line %d ### -- **A BIBLIOGRAPHY'
        % r['cite_line'])
    rec('    ### ENTRY, NOT A DEPOSIT RECORD.**')
    rec('    ### ### ### **AND THAT IS THE WHOLE DIFFERENCE BETWEEN THE TWO.** ### The corpus')
    rec('    ### ### ### records ### **WHAT** ### was deposited and ### **WHERE**, and ### **NOT')
    rec('    ### ### ### AT WHAT VERSION.**')
    rec()
    rec('    ### **REMEDY (a) -- A HISTORICAL NOTE ADDED TO THE RECORD.**')
    rec('      requires : ### **ONE LINE, BUT NOT ONE THIS ACT COULD WRITE** -- a historical note')
    rec('      that cannot say ### *superseded from what* ### is a note that records only that')
    rec('      something old exists. ### It is writable and ### **THIN.**')
    rec('      ### **WHAT IT DOES NOT BUY:** ### it still leaves the corpus unable to say whether')
    rec('      any published claim cites that deposit at that version.')
    rec('    ### **REMEDY (b) -- A NEW VERSION DEPOSITED AT A STATE A CITABLE CLAIM USES.**')
    rec('      requires : ### **A READ NOBODY CAN PERFORM FROM HERE.** ### To deposit `v2.3` as')
    rec('      the current state you must first know what is already there, and ### **THE')
    rec('      ### PLATFORM DOES NOT ANSWER AND THE CORPUS DOES NOT RECORD IT.**')
    rec('      ### **WHAT IT DOES NOT BUY:** ### depositing without a read risks a duplicate version of')
    rec('      something already current, which is ### **A WORSE DEFECT THAN THE ONE IT CURES.**')
    out['19675356'] = dict(deposited_at=None, repo_now=r['repo_now'],
                           remedy_a='one thin line; it cannot say superseded from what',
                           remedy_b='blocked: requires a read nobody can perform',
                           blocked=True)
    rec()
    bar()
    rec('  ### ### **WHAT NEITHER REMEDY BUYS, FOR EITHER RECORD.**')
    bar()
    rec('  ### Neither makes the corpus able to answer ### **"IS THIS DOI SAFE TO CITE?"** ###')
    rec('  ### without a live read, because ### **THE CURRENCY OBLIGATION IS SATISFIED IN THE')
    rec('  ### ### CORPUS AND TESTED AT THE PLATFORM**, and the platform has answered nothing')
    rec('  ### since `b389`. ### `(R20)` is met by a note; ### **A READER IS SERVED BY A RECORD.**')
    rec('  ### ### ### **THE TWO PRICE ASYMMETRICALLY, AND THAT IS THE RESULT:** ### the monograph')
    rec('  ### ### ### record can be noted in one line today; ### **THE SILENCE DEPOSIT CANNOT BE')
    rec('  ### ### ### GIVEN A CURRENT-VERSION REMEDY AT ALL** ### until something records what it')
    rec('  ### ### ### was deposited at.')
    rec('  ### ### **NOTHING IS WRITTEN AT THE PLATFORM. ### NOTHING DEPOSITS. ### NEITHER REMEDY')
    rec('  ### ### IS RECOMMENDED; THE CHOICE IS THE AUTHOR`S.**')
    return out


# ==================================================================================================
def component3():
    bar('=')
    rec('  ### COMPONENT 3 -- `Tier KC`, UNAPPLIED, PRICED.')
    bar('=')
    s3 = E['s3']
    oi, oln = AF.find(TAX, '*Obligation.* **Every load-bearing claim is stated clearly in the '
                           'body**')
    rec('  ### **THE OBLIGATION** -- `THE_DOCUMENT_CLASS_TAXONOMY.md` line %d:' % oi)
    rec('      > %s' % flat(oln, 420))
    rec()
    rec('  ### ### **IT HAS THREE LIMBS, AND THE RECORD ANSWERS ONE.**')
    rec('  ###   (i) ### **GRADE** ### -- each row names its backing in the front door`s')
    rec('  ###   vocabulary. ### **ANSWERED:** ### `b387` banked ### **`%s` ROWS** ### across `9`'
        % s3['rows'])
    rec('  ###   documents, ### **`%s` OF THEM NOT MACHINE-VERIFIED AND LABELLED.**'
        % s3['not_machine'])
    rec('  ###   (ii) ### **PLACEMENT** ### -- the table sits ### *after the front matter, where a')
    rec('  ###   reader meets it.* ### **NOT ANSWERED. ### THE RECORD HOLDS NO TABLE POSITION FOR')
    rec('  ###   ### ANY DOCUMENT.** ### `b387` counted rows; it never asked where they sit.')
    rec('  ###   (iii) ### **COVERAGE** ### -- ### *every* ### load-bearing claim carried by a row.')
    rec('  ###   ### **NOT ANSWERED. ### THE RECORD HOLDS ROW COUNTS AND NOT CLAIM COUNTS**, so')
    rec('  ###   the ratio a reader needs -- claims carried over claims made -- ### **CANNOT BE')
    rec('  ###   ### COMPUTED FROM WHAT IS BANKED.**')
    rec()
    rec('  ### ### **AND THE ONE KEYSTONE `b390` READ WHOLE WOULD FAIL THE PLACEMENT LIMB.**')
    rec('  ### `ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md`: `## Correspondence` at line `%s`,'
        % s3['amc_corr'])
    rec('  ### `## Provenance` at line `%s`, and the standard`s table at line `%s` ### -- **BOTH'
        % (s3['amc_prov'], s3['amc_standard']))
    rec('  ### ### TABLES SIT AT THE END AND THE STANDARD`S IS BELOW THE PROVENANCE.**')
    rec('  ### ### ### **SO THE FIRST DOCUMENT ANYONE WOULD PROPOSE FOR THE CLASS ALREADY FAILS')
    rec('  ### ### ### ONE OF ITS THREE LIMBS**, which is worth knowing before a placement pass is')
    rec('  ### ### ### ordered rather than after.')
    rec()
    rec('  ### ### **THE CHEAP SWEEP, AS A FLOOR AND NOT A VERDICT.**')
    rec('  ###   census keystones found on disk     : ### **`%s`**' % s3['found'])
    rec('  ###   carrying a correspondence table    : ### **`%s`**' % s3['with_table'])
    rec('  ###   carrying a glossary heading        : ### **`%s`**' % s3['with_glossary'])
    rec('  ###   carrying a references/bibliography : ### **`%s`**' % s3['with_bib'])
    rec('  ### ### ### **A HEADING IS NOT A TABLE READ**, and this sweep tests headings. ### It')
    rec('  ### ### ### bounds the FURNITURE limb from below and says ### **NOTHING WHATEVER** ###')
    rec('  ### ### ### about grade, placement or coverage.')
    rec()
    bar()
    rec('  ### ### **THE PRICE.**')
    bar()
    rec('  ### **WHAT IS FREE:** ### the grade limb, for the `9` documents `b387` already read --')
    rec('  ### ### **`%s` ROWS ARE BANKED WITH THEIR BACKING.**' % s3['rows'])
    rec('  ### **WHAT IS CHEAP:** ### the placement limb. ### One sweep over each candidate for the')
    rec('  ### position of its correspondence heading relative to its front matter. ### **MINUTES')
    rec('  ### ### PER DOCUMENT, AND MECHANICAL.**')
    rec('  ### **WHAT IS EXPENSIVE, AND DOMINATES:** ### the coverage limb. ### It requires reading')
    rec('  ### ### **EVERY LOAD-BEARING CLAIM IN THE BODY** ### and deciding, per claim, whether a')
    rec('  ### row carries it. ### That is ### **THE SAME WORK `b390` PRICED AT ROUGHLY HALF AN')
    rec('  ### ### HOUR PER DOCUMENT** -- and `b390` said its own figure was ### **AN')
    rec('  ### ### UNDERESTIMATE**, because its subject had already been reconciled once.')
    rec('  ### ### ### **SO THE CLASS CANNOT BE APPLIED CHEAPLY TO ANY DOCUMENT, AND CANNOT BE')
    rec('  ### ### ### APPLIED AT ALL FROM WHAT IS BANKED.**')
    rec()
    rec('  ### ### **WHAT THE APPLICATION WOULD NEED THAT THE RECORD DOES NOT HOLD:**')
    rec('  ###   (1) ### **A TABLE POSITION PER DOCUMENT** ### -- cheap to get, nobody has it.')
    rec('  ###   (2) ### **A LOAD-BEARING-CLAIM COUNT PER DOCUMENT** ### -- expensive, and ###')
    rec('  ###   **IT IS A JUDGEMENT BEFORE IT IS A COUNT**: what is load-bearing in a paper is')
    rec('  ###   not a string a sweep can find. ### `b380` already proved a related predicate')
    rec('  ###   fails its own control.')
    rec('  ###   (3) ### **A DECLARATION.** ### `b382` ruled that a class ruling must rest on')
    rec('  ###   ### **DECLARATION**, not on structure or prose. ### **THE RECORD HOLDS NO `Tier')
    rec('  ###   ### KC` DECLARATION FOR ANY DOCUMENT, BECAUSE THE CLASS IS ONE DAY OLD.**')
    rec('  ### ### ### **THAT THIRD ITEM IS NOT A COST. ### IT IS A GATE**, and no amount of')
    rec('  ### ### ### measurement opens it.')
    rec()
    rec('  ### ### **PRICED, NOT RUN. ### `0` DOCUMENTS PLACED. ### `0` CANDIDATES NAMED.**')
    return dict(limbs=3, answered=1, rows=s3['rows'], not_machine=s3['not_machine'],
                found=s3['found'], with_table=s3['with_table'],
                with_glossary=s3['with_glossary'], with_bib=s3['with_bib'],
                placed=0, candidates=0)


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b393 -- THE FIVE CLUSTERS, SURFACED; AND TWO PRICINGS.')
    bar('=')
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c3 = component3()
    rec()
    bar('=')
    rec('  1 : clusters %d ; by verdict %s ; changed by anchor %d ; (L1) %s'
        % (len(c1['surfaced']), c1['by_verdict'], c1['anchor_changed'], c1['l1']))
    rec('  2 : records %d ; the Silence deposit`s version is unrecorded : %s'
        % (len(c2), c2['19675356']['blocked']))
    rec('  3 : limbs %d ; answered by the record %d ; placed %d'
        % (c3['limbs'], c3['answered'], c3['placed']))
    rec('  ### **NO DOCUMENT WAS EDITED. ### THE PLATFORM WAS NOT CALLED. ### NOTHING DEPOSITS.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b393_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, run_file=os.path.basename(p),
                   run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b393_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
