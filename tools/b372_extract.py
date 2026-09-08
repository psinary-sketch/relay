# -*- coding: utf-8 -*-
"""b372_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE REFS ARE PRINTED BEFORE ANY QUOTATION**, and this act prints them for FIVE repositories,
### ### **AND THE EXCLUSION KERNEL'S TAGS**, because ### **COMPONENT 3 OPENS A KERNEL AT A PIN FOR THE
### ### PINNED ROWS AND AT A HEAD FOR THE PINLESS ONES, AND (R8) MAKES THAT DIFFERENCE THE PRODUCT.**
### ### **NO BUILD IS RUN AND NO `.lean` FILE IS WRITTEN. NO ROW IS REPAIRED IN THIS ACT.**
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
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

REPOS = [('relay', ROOT), ('SIDE-global-section', GS), ('PLACE-papers', PP), ('SIDE-effects', SE)]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b372_ferry_2026-09-08.txt')
GA_RELAY = os.path.join(ROOT, '.gitattributes')
GA_GS = os.path.join(GS, '.gitattributes')
GA_PP = os.path.join(PP, '.gitattributes')
GS_README = os.path.join(GS, 'README.md')
GS_PRINTS = os.path.join(GS, 'AXIOM_PRINTS.txt')
SE_README = os.path.join(SE, 'README.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
SPIRAL = os.path.join(PP, 'SPIRAL_MAP.md')
LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
EE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
DUR = os.path.join(TC, 'modules', '2026-09', 'DURABILITY_SPLIT.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b372 - THE README, THE EOL PIN, AND THE FIRST BATCH.'),
    ('the order -- (R8), a row without a pin', 'ORDER', FERRY,
     'strikeable: A ROW WITHOUT A PIN IS NOT CHECKABLE THE WAY THE'),
    ('the order -- (R8), the head is recorded in the bank', 'ORDER', FERRY,
     "kernel's live head, and the head is recorded in the checking"),
    ('the order -- (R8), CHECKED-AT-HEAD is weaker', 'ORDER', FERRY,
     'CHECKED-AT-HEAD, which is weaker than a pinned row'),
    ('the order -- (R8), pins are a separate ruling', 'ORDER', FERRY,
     'separate ruling, priced and not attempted.'),
    ('the order -- component 1, first because it protects', 'ORDER', FERRY,
     'COMPONENT 1 - THE EOL PIN, first because it protects the rest:'),
    ('the order -- component 1, the verification named', 'ORDER', FERRY,
     "tracked file's working bytes equal its blob's after a fresh"),
    ('the order -- component 1, say so rather than writing twice', 'ORDER', FERRY,
     'checkout. Where a repository already carries it, say so rather'),
    ('the order -- component 2, the object as the order names it', 'ORDER', FERRY,
     'COMPONENT 2 - THE README, WHICH TRAVELS WITH A CLONE: the'),
    ('the order -- component 2, the three-clause description', 'ORDER', FERRY,
     "exclusion kernel's README states a headline figure, a breakdown"),
    ('the order -- component 2, removed rather than restated', 'ORDER', FERRY,
     'the bank, and a figure REMOVED rather than restated unless the'),
    ('the order -- component 2, route a claim', 'ORDER', FERRY,
     'document can name the ref it holds at. If the repair requires'),
    ('the order -- component 3, the twelve', 'ORDER', FERRY,
     'COMPONENT 3 - THE FIRST BATCH under (R6) and (R8): the twelve'),
    ('the order -- component 3, the four terminals', 'ORDER', FERRY,
     'axiom profile read from a printed profile), RETIRED (the'),
    ('the order -- component 3, no repairs', 'ORDER', FERRY,
     'rows is reported and routed.'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     "navigator's expectations: (F1) the README's three figures count"),

    # ---- COMPONENT 1: WHAT THE FOUR ROSTERED REPOSITORIES ALREADY CARRY -----------------------------
    ('the attribute -- relay, and its scope', 'EOL', GA_RELAY,
     'snapshots/** text eol=lf'),
    ('the attribute -- the construction kernel, the rule', 'EOL', GA_GS,
     '* text=auto eol=lf'),
    ('the attribute -- the construction kernel, why it is there', 'EOL', GA_GS,
     '# eol=lf makes checkout match storage, as the papers repository'),
    ('the attribute -- the papers repository, the rule', 'EOL', GA_PP,
     '* text=auto eol=lf'),
    ('the attribute -- the papers repository, why it is there', 'EOL', GA_PP,
     '# eol=lf makes checkout match storage. Do not remove without'),

    # ---- COMPONENT 2: THE TWO CANDIDATE READMES, READ AT CONTENT ------------------------------------
    ('the construction README -- the headline and its breakdown', 'README', GS_README,
     '- **`Core/`** '),
    ('the construction README -- the assembly print ratio', 'README', GS_README,
     'assembly, `AXIOM_PRINTS.txt` (250/250). No terminal failed the bar'),
    ('the construction kernel -- the first printed profile line', 'README', GS_PRINTS,
     "'ReDerivationShadow.expanding_the_scaling_operator_reconciles_all_three_terms' does not depend"),
    ('the exclusion README -- its subject sentence', 'README', SE_README,
     'Lean 4 kernel for the SIDE Exclusion method: the abstract exclusion'),
    ('the exclusion README -- its ONE count line', 'README', SE_README,
     '3 theorems, 3 sorrys (each at a marked analytic boundary), 0 axioms.'),

    # ---- COMPONENT 3: THE TWELVE ROWS, EACH ANCHORED BY ITS OWN CONTENT ------------------------------
    ('row 01 -- the registry, Yang-Mills, PINNED', 'ROW', REGISTRY,
     '| p2-31 | The Yang-Mills Mass Gap via SIDE Exclusion |'),
    ('row 02 -- the spiral map, the exclusion kernel, PINNED', 'ROW', SPIRAL,
     '*(merged 2026-08-14)*'),
    ('row 03 -- the loom, no-conspiracy twins', 'ROW', LOOM,
     '| no-conspiracy twin primes |'),
    ('row 04 -- the loom, no-conspiracy Goldbach', 'ROW', LOOM,
     '| no-conspiracy Goldbach |'),
    ('row 05 -- the loom, no-conspiracy Sophie Germain', 'ROW', LOOM,
     '| no-conspiracy Sophie Germain |'),
    ('row 06 -- the loom, side_exclusion', 'ROW', LOOM,
     '| `side_exclusion` | '),
    ('row 07 -- the loom, Yang-Mills mass gap (form)', 'ROW', LOOM,
     '| Yang-Mills mass gap (form) |'),
    ('row 08 -- the loom, GRH exclusion (form)', 'ROW', LOOM,
     '| GRH exclusion (form) |'),
    ('row 09 -- the engine, mass_gap / Massless', 'ROW', EE,
     '| `mass_gap` / `Massless` |'),
    ('row 10 -- the engine, bsd_full, PINNED', 'ROW', EE,
     '| `bsd_full` / `RankMismatch` / `MismatchMechanism` |'),
    ('row 11 -- the engine, no_conspiracy_twins', 'ROW', EE,
     '| `no_conspiracy_twins` / `TwinFinite` |'),
    ('row 12 -- the conspiracy paper, the three instantiations, PINNED', 'ROW', AMC,
     '| Per-conjecture instantiations |'),

    # ---- WHAT THE RECORD ALREADY RULED --------------------------------------------------------------
    ('the lore -- the durability split, in its own words', 'LORE', DUR,
     '**A repair to a TRACKED file travels with a clone. A repair to an UNTRACKED one does not.**'),
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
    rec('b372 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b372_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, path in REPOS + [('SIDE-kernel', SK)]:
        b = subprocess.run(['git', '-C', path, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        h = subprocess.run(['git', '-C', path, 'rev-parse', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        st = subprocess.run(['git', '-C', path, 'status', '--porcelain'],
                            capture_output=True, text=True).stdout.strip()
        refs[name] = dict(branch=b, head=h, dirty=bool(st))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, b, h[:12], bool(st)))
    rec('')
    rec('  ### ### **THE EXCLUSION KERNEL`S TAGS -- (R8) MAKES THE DIFFERENCE BETWEEN A PIN AND A HEAD')
    rec('  ### ### THE WHOLE OF COMPONENT 3.**')
    tags = subprocess.run(['git', '-C', SE, 'tag', '-l'], capture_output=True, text=True).stdout.split()
    tagref = {}
    for tg in tags:
        pe = subprocess.run(['git', '-C', SE, 'rev-parse', tg + '^{commit}'],
                            capture_output=True, text=True).stdout.strip()
        ahead = subprocess.run(['git', '-C', SE, 'rev-list', '--count', '%s..HEAD' % tg],
                               capture_output=True, text=True).stdout.strip()
        tagref[tg] = dict(commit=pe, head_ahead_by=ahead)
        rec('    `%s` = `%s` ### -- HEAD is `%s` commit(s) ahead of it' % (tg, pe[:12], ahead))
    rec('')
    rec('  ### **AND THE PINS THE PINNED ROWS NAME, RESOLVED HERE AND NOT LATER:**')
    named = {}
    for pin in ('afa9ccf', 'c66f3c5', 'a27415d', 'phase-1.5-module-1-v2', 'v0.1'):
        r = subprocess.run(['git', '-C', SE, 'rev-parse', pin + '^{commit}'],
                           capture_output=True, text=True)
        val = r.stdout.strip() if r.returncode == 0 else ''
        named[pin] = dict(resolves=bool(val), commit=val)
        rec('    `%-24s` resolves in the exclusion kernel : %-5s %s' % (pin, bool(val), val[:12]))
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
        rec('  [%-7s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:230])
    ndiff = sum(1 for x in built if x['differs'])
    counts = {}
    for x in built:
        counts[x['tag']] = counts.get(x['tag'], 0) + 1
    ga = {k: os.path.exists(os.path.join(v, '.gitattributes')) for k, v in REPOS}
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **BY TAG : %s**' % counts)
    rec('  ### ### **`.gitattributes` PRESENT, BY REPOSITORY : %s**' % ga)
    rec('  ### **THE EXCLUSION KERNEL CARRIES NO `.gitattributes` -- SO THERE IS NO LINE TO ANCHOR')
    rec('  ### ### THERE, AND THAT ABSENCE IS A MEASUREMENT, NOT A FAILED READ.**')
    rec('  ### **NO BUILD WAS RUN, NO `.lean` FILE WAS WRITTEN, NO ROW WAS REPAIRED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b372_extract_notes', LINES)
    io.open(d('b372_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, tags=tagref, named_pins=named, built=built,
             gitattributes_present=ga,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
