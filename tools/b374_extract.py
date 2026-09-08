# -*- coding: utf-8 -*-
"""b374_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THIS LEG READS A SURFACE THE HEDGE AUDIT HAS NEVER COVERED** -- the keystone corpus and the
### deposited companions -- so the extract carries the definitions those documents give of themselves:
### the census's own class test, the bibliography's own name-identity law, the glossary's own heading.
### ### ### **AND BOTH HALVES OF THE FUNCTIONAL-EQUATION FILING ARE PULLED FROM THE ACTS THAT STATED
### ### THEM**, including the sentence that says how far those acts did NOT go.
### ### **NO BUILD IS RUN, NOTHING IS REPAIRED, AND NO ENTRY IS REWRITTEN BY THIS FILE.**
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


def t(n):
    return os.path.join(ROOT, 'tools', n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b374_ferry_2026-09-08.txt')
CENSUS = p('phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
BIB = p('BIBLIOGRAPHY.md')
APTS = p('day1', 'A_Place_to_Stand.md')
DEP = p('outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
B291 = d('b291_the_involution.txt')
B293 = d('b293_family_run.txt')
HEDGE = t('hedge_audit.py')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ----------------------------------------------------------------------------------
    ('the order -- leg 2, the act', 'ORDER', FERRY,
     'LEG 2 (b374) - THE DESCRIPTIVE LAYER, MEASURED NOT OPINED.'),
    ('the order -- (i), the hedge audit unmodified', 'ORDER', FERRY,
     '(i) Run the hedge audit, unmodified, over the keystone corpus'),
    ('the order -- (i), a surface it has never covered', 'ORDER', FERRY,
     'and the deposited companions - a surface it has never covered -'),
    ('the order -- (i), the three things reported', 'ORDER', FERRY,
     'and report per document: hedged sentences located and quoted,'),
    ('the order -- (i), classify and repair nothing', 'ORDER', FERRY,
     'working notes sitting inside synthesis text. Classify; repair'),
    ('the order -- (ii), the glossary and the bibliography', 'ORDER', FERRY,
     '(ii) The translation glossary and the bibliography: each entry'),
    ('the order -- (ii), the four words', 'ORDER', FERRY,
     'in the record, classified CURRENT / RENAMED / RETIRED /'),
    ('the order -- (iii), the count-and-ref sweep', 'ORDER', FERRY,
     '(iii) A count-and-ref sweep across every descriptive surface'),
    ('the order -- (iii), the list is the product', 'ORDER', FERRY,
     'version or date is listed. The list is the product; nothing is'),
    ('the order -- (iv), the filing', 'ORDER', FERRY,
     '(iv) File, as a filing and not a campaign: the functional'),
    ('the order -- (iv), both halves quoted', 'ORDER', FERRY,
     "corpus's object is the self-dual point of that reflection -"),
    ('the order -- (iv), nothing claimed beyond', 'ORDER', FERRY,
     'with both halves quoted from their own acts and NOTHING claimed'),
    ('the order -- the sortie closing', 'ORDER', FERRY,
     'CLOSING for the sortie: one paragraph per leg; the trails'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'the next ferry as DRAFT - NAVIGATOR EDITS. The navigator'),
    ('the order -- (L2)', 'ORDER', FERRY,
     'locatable writing act; (L2) the keystones carry fewer hedges'),

    # ---- THE DOCUMENTS THAT DEFINE THE SCOPE ---------------------------------------------------------
    ("the census -- its own class test for KEYSTONE", 'SCOPE', CENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the census -- the sixteen, and the correction it records', 'SCOPE', CENSUS,
     'The corrected figure is 16, and the correction is recorded rather than the raw number'),
    ('the census -- the deposited companions as their own class', 'SCOPE', CENSUS,
     "Day-1's prose-terminal architecture -- its own class, NOT a failure of (ii)."
     .replace('--', '—')),
    ('the bibliography -- its own name-identity law', 'SCOPE', BIB,
     '**THE NAME-IDENTITY LAW GOVERNS THIS FILE.**'),
    ('the bibliography -- the cite-key rule', 'SCOPE', BIB,
     '**CITE-KEY RULE: the arXiv ID is canonical.**'),
    ('the glossary -- its heading, in the living document', 'SCOPE', APTS,
     '## Appendix E: Glossary'),
    ('the deposited companion -- the frozen twin of that document', 'SCOPE', DEP,
     '# The Third Identity Element and Riemann'),

    # ---- THE TWO ACTS THE FILING QUOTES --------------------------------------------------------------
    ('b291 -- the reflection, derived', 'FILING', B291,
     'THEREFORE `F_eR : S(lambda, mu) -> S(mu, lambda)`'),
    ('b291 -- the grade it carries and the import it names', 'FILING', B291,
     'GRADE: ### DERIVES-on-IMPORT ### -- the import being CC'),
    ('b291 -- the self-dual member', 'FILING', B291,
     "THE CORPUS'S ARCHIMEDEAN MEMBER IS SELF-DUAL."),
    ('b291 -- the diagonal met at most once', 'FILING', B291,
     'EACH DILATION ORBIT MEETS THE DIAGONAL AT MOST ONCE.'),
    ('b291 -- how far it does NOT go', 'FILING', B291,
     'AND NONE OF THIS IS EXTENDED TO THE FINITE PLACES.'),
    ('b293 -- the finite two-radius family, constructed', 'FILING', B293,
     'b293 -- THE FINITE TWO-RADIUS FAMILY.'),

    # ---- THE INSTRUMENT, RUN UNMODIFIED --------------------------------------------------------------
    ('the hedge audit -- its own hedge stems', 'INSTRUMENT', HEDGE, 'HEDGE_STEMS = ('),
    ('the hedge audit -- its own grade tokens', 'INSTRUMENT', HEDGE, 'GRADE_TOKENS = ('),

    # ---- WHAT THE RECORD ALREADY RULED ----------------------------------------------------------------
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
    rec('b374 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b374_extract_notes', LINES)
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
        rec('  [%-10s] %s' % (tag, label))
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
    rec('  ### **NO BUILD WAS RUN, NOTHING WAS REPAIRED AND NO ENTRY WAS REWRITTEN BY THIS FILE.**')
    rec('=' * 100)
    q = run_clock.write(D, 'b374_extract_notes', LINES)
    io.open(d('b374_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, built=built,
             run_file=os.path.basename(q), run_clock=run_clock.read_stamp(q)), indent=1))
    print('  written: %s' % os.path.basename(q))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
