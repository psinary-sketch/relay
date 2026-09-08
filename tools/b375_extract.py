# -*- coding: utf-8 -*-
"""b375_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### ### **THIS EXTRACT CARRIES THE THING THAT DECIDES WHAT THE CENSUS CAN MEAN:** ### the corpus
### ### **ALREADY HAS AN AUTHOR-RULED DOCUMENT-CLASS TAXONOMY**, and its `Tier K` is defined by
### ### **CERTIFICATION AT A PIN**, not by synthesis. ### The order's `KEYSTONE` is defined by
### ### **SYNTHESIS AGAINST OTHER CONTENT.** ### And `THE_KEYSTONE_CENSUS.md` used a THIRD test.
### ### **THREE TESTS, ONE WORD** -- so all three are pulled here, verbatim, before anything is
### classified, and the registration fixes how they are kept apart.
### ### **NO DOCUMENT IS REPAIRED, NO CLASS IS CONFERRED AND NO ROW IS EDITED BY THIS FILE.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
GS = os.path.join('D:', os.sep, 'SIDE-global-section')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

REPOS = [('relay', ROOT), ('SIDE-global-section', GS), ('PLACE-papers', PP), ('SIDE-effects', SE)]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b375_ferry_2026-09-08.txt')
TAX = p('phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
REGY = p('REGISTRY.md')
CENSUS = p('phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
TRAILS = p('OPEN_TRAILS.md')
CLUS = p('clusters', 'RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ----------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b375 - THE KEYSTONE AND CLUSTER CENSUS. Number not claimed'),
    ('the order -- the four lists stay open', 'ORDER', FERRY,
     'ordered before any disposition runs; the four lists b373 and'),
    ('the order -- the scope', 'ORDER', FERRY,
     'SCOPE: READS and CLASSIFICATION only. NO document repaired, NO'),
    ('the order -- no class conferred on a declarer', 'ORDER', FERRY,
     'class conferred on a document that declares its own, NO'),
    ('the order -- the rubric, support', 'ORDER', FERRY,
     'as the census own test: SUPPORT documents gather a subject'.replace(' own', "'s own")),
    ('the order -- the rubric, keystones', 'ORDER', FERRY,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('the order -- the rubric, may not carry those', 'ORDER', FERRY,
     'other clusters - and may not carry those. Both are in ongoing'),
    ('the order -- component 1, from content never from a path', 'ORDER', FERRY,
     'COMPONENT 1 - THE POPULATION, read from content and never from'),
    ('the order -- component 1, declared or read', 'ORDER', FERRY,
     'DECLARED (the document own class line, quoted) or READ (from'.replace(' own', "'s own")),
    ('the order -- component 1, the directory disagreement', 'ORDER', FERRY,
     'is reported at full prominence and NOT reclassified by this'),
    ('the order -- component 2, the clusters', 'ORDER', FERRY,
     'COMPONENT 2 - THE CLUSTERS: enumerate the subject clusters the'),
    ('the order -- component 2, unassigned rather than resemblance', 'ORDER', FERRY,
     'cannot be identified from its own text is reported UNASSIGNED'),
    ('the order -- component 3, four columns kept apart', 'ORDER', FERRY,
     'COMPONENT 3 - THE INTEGRATION STATE, four columns kept apart'),
    ('the order -- component 3, what bears on it and is not in it', 'ORDER', FERRY,
     'BEARS ON IT AND IS NOT IN IT - material in the findings layer,'),
    ('the order -- component 3, not determinable', 'ORDER', FERRY,
     'own text, it reads NOT DETERMINABLE FROM THE DOCUMENT and the'),
    ('the order -- component 4, the rubric applied', 'ORDER', FERRY,
     'COMPONENT 4 - THE RUBRIC APPLIED, measured not opined: for each'),
    ('the order -- component 4, the control population', 'ORDER', FERRY,
     'SUPPORT documents as the control population, so the difference'),
    ('the order -- component 5, what the census does not know', 'ORDER', FERRY,
     'COMPONENT 5 - WHAT THE CENSUS DOES NOT KNOW, stated plainly:'),
    ('the order -- the closing, no new tracking document', 'ORDER', FERRY,
     'for where it should live - the census does not create a new'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     "The navigator's expectations, registered here: (F1) fewer than"),
    ('the order -- (F2) and (F3)', 'ORDER', FERRY,
     'one cluster has support documents and no keystone; (F3) column'),

    # ---- THE FIRST TEST: THE AUTHOR-RULED TAXONOMY, IN ITS OWN WORDS ----------------------------------
    ('the taxonomy -- why it exists', 'TAXONOMY', TAX,
     'The taxonomy exists to make two failures structurally impossible'),
    ('the taxonomy -- Tier K, certified at a pin', 'TAXONOMY', TAX,
     '**Tier K — Keystone-certified.**'),
    ('the taxonomy -- Tier C, cluster-synthesis', 'TAXONOMY', TAX,
     '**Tier C — Cluster-synthesis.**'),
    ('the taxonomy -- Tier N, notes and exploratory', 'TAXONOMY', TAX,
     '**Tier N — Notes / exploratory.**'),
    ('the taxonomy -- Tier E, filing-facing', 'TAXONOMY', TAX,
     '**Tier E — Filing-facing.**'),
    ('the taxonomy -- its own declared class line', 'TAXONOMY', TAX,
     '**DOCUMENT CLASS (K/C/N/E — the AUTHOR-RULED standard, 2026-07-28): TIER C**'),
    ("the registry -- the tier legend, presumptive by class", 'TAXONOMY', REGY,
     '**Document-tier legend (2026-07-28; Tier E added 2026-08-08'),

    # ---- THE SECOND TEST: THE EXISTING KEYSTONE CENSUS -----------------------------------------------
    ("the existing census -- its own class test", 'CENSUS', CENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the existing census -- the sixteen', 'CENSUS', CENSUS,
     'The corrected figure is 16, and the correction is recorded rather than the raw number'),

    # ---- THE DECLARERS AND THE REFUSERS --------------------------------------------------------------
    ('a ledger -- its declaration REFUSING a tier', 'DECLARED', TRAILS,
     '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): ### NOT PLACED'),
    ('a cluster synthesis -- the shape of a cluster document', 'CLUSTER', CLUS, '# '),
    ('the registry -- the support tier that names the clusters', 'CLUSTER', REGY,
     '## SUPPORT TIER: Cluster Syntheses + Consults (clusters/)'),
    ('the registry -- a phase section heading', 'CLUSTER', REGY, '### 1.5C: Spectral & Structural Core'),

    # ---- WHAT THE RECORD ALREADY RULED ---------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and will '
     'report'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b375 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b375_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, path in REPOS:
        b = subprocess.run(['git', '-C', path, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        h = subprocess.run(['git', '-C', path, 'rev-parse', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        st = subprocess.run(['git', '-C', path, 'status', '--porcelain'],
                            capture_output=True, text=True).stdout.strip()
        refs[name] = dict(branch=b, head=h, dirty=bool(st))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, b, h[:12], bool(st)))
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        if not os.path.exists(path):
            rec('  ### ### **NO SUCH FILE** : %s -- %s' % (label, path))
            bad += 1
            continue
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e).replace(chr(10), ' | ')[:200])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n,
                          differs=bool(differs), text=line.rstrip()))
        rec('')
        rec('  [%-9s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:230])
    ndiff = sum(1 for x in built if x['differs'])
    counts = {}
    for x in built:
        counts[x['tag']] = counts.get(x['tag'], 0) + 1
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **BY TAG : %s**' % counts)
    rec('  ### ### **AND THE THREE TESTS ARE NOW ALL IN ONE FILE, VERBATIM, BEFORE ANY CLASSIFICATION:**')
    rec('  ### ### the taxonomy`s `Tier K` (certified at a pin), the order`s `KEYSTONE` (synthesizes a')
    rec('  ### ### cluster), and the existing census`s test (external results + a correspondence table +')
    rec('  ### ### cited by its spine). ### **THREE TESTS, ONE WORD.**')
    rec('  ### **NO DOCUMENT WAS REPAIRED, NO CLASS WAS CONFERRED AND NO ROW WAS EDITED.**')
    rec('=' * 100)
    q = run_clock.write(D, 'b375_extract_notes', LINES)
    io.open(d('b375_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, built=built,
             run_file=os.path.basename(q), run_clock=run_clock.read_stamp(q)), indent=1))
    print('  written: %s' % os.path.basename(q))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
