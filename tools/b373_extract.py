# -*- coding: utf-8 -*-
"""b373_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE REFS ARE PRINTED BEFORE ANY QUOTATION.** ### And this act prints one thing no earlier
### extract has: ### **THE SHAPE OF THE EVIDENCE `(R9)` REQUIRES** -- a row, the commit that introduced
### it, the act that commit names, and the pins record that act banked. ### If any link is missing the
### row is `CITES-AT-AN-UNKNOWN-REF`, and the extract shows the chain rather than asserting it.
### ### **NO BUILD IS RUN, NO `.lean` FILE IS WRITTEN, AND NO ROW IS EDITED BY THIS FILE.**
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


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b373_ferry_2026-09-08.txt')
B372BANK = d('b372_the_first_batch.txt')
B372CLOSE = d('b372_closing.txt')
PINSAMPLE = d('b329_pins_stepzero.txt')
HOOKS = t('b304_hooks.py')
LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
EE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
SEFF = os.path.join(PP, 'internal', 'SIDE_EFFECTS.md')
DEPOSITED = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')
DUR = os.path.join(TC, 'modules', '2026-09', 'DURABILITY_SPLIT.md')

READS = [
    # ---- THE ORDER ----------------------------------------------------------------------------------
    ('the order -- the sortie', 'ORDER', FERRY,
     'CONCURRENCY: SOLO (research seat). SORTIE: two legs in order,'),
    ('the order -- (R9), a citing row names a pin', 'ORDER', FERRY,
     'strikeable: A CITING ROW NAMES A PIN. b372'),
    ('the order -- (R9), the sourcing rule', 'ORDER', FERRY,
     'therefore ADDED to citing rows, and sourced ONLY from the act'),
    ('the order -- (R9), never from the current head', 'ORDER', FERRY,
     'current head, which would date the claim to today rather than'),
    ('the order -- (R9), the unknown-ref mark', 'ORDER', FERRY,
     'is marked CITES-AT-AN-UNKNOWN-REF and left, which is honest and'),
    ('the order -- (R9), priced first', 'ORDER', FERRY,
     'is not a pin. Priced first; if the price does not fit one act,'),
    ('the order -- leg 1, the act', 'ORDER', FERRY,
     'LEG 1 (b373) - THE PINS AND THE STATUS COLUMN. The executor'),
    ('the order -- leg 1 (i), executed or priced', 'ORDER', FERRY,
     'draft is ADOPTED, with two additions. (i) (R9) executed or'),
    ('the order -- leg 1 (i), the count reported plainly', 'ORDER', FERRY,
     'and the count of rows whose act could not be located reported'),
    ('the order -- leg 1 (ii), a claim about what is verified', 'ORDER', FERRY,
     'is a claim about what is verified, not a stale number - each'),
    ('the order -- leg 1 (ii), no grade moved by the seat', 'ORDER', FERRY,
     'consequence routed to the author without any row'),
    ('the order -- leg 1, the hooks tool', 'ORDER', FERRY,
     'moved by the seat. Also: the hooks tool carries a sentence that'),
    ('the order -- leg 2, named and not opened here', 'ORDER', FERRY,
     'LEG 2 (b374) - THE DESCRIPTIVE LAYER, MEASURED NOT OPINED.'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'the next ferry as DRAFT - NAVIGATOR EDITS. The navigator'),

    # ---- WHAT `(R9)` RESTS ON, IN THE ACT THAT FOUND IT ----------------------------------------------
    ("b372's finding -- present at the pin, retired at the head", 'RECORD', B372BANK,
     'AND ONE COMPARISON INSIDE THIS ACT IS THE WHOLE ARGUMENT FOR'),
    ("b372's finding -- the rows that cite without a pin", 'RECORD', B372BANK,
     'THE HEAD**, and the rows that cite them without a pin cannot say which they meant.'),
    ("b372's closing -- the status column named as the sharper item", 'RECORD', B372CLOSE,
     'repaired, as this act did. ### **(b)** ### **THE STATUS COLUMN ITSELF**'),
    ("b372's closing -- what the papers now carry", 'RECORD', B372CLOSE,
     'AND WHAT THE PAPERS NOW CARRY, REPORTED AND NOT REPAIRED'),

    # ---- THE EVIDENCE CHAIN `(R9)` REQUIRES ----------------------------------------------------------
    ("a banked pins record -- the shape the ref is read from", 'CHAIN', PINSAMPLE,
     '--- SIDE-global-section   (D:'),
    ("a banked pins record -- the head that act recorded", 'CHAIN', PINSAMPLE,
     '    local HEAD   : 50200cc7c84512e092bdb9139f3cbfe3a045ed45'),

    # ---- THE SURFACES ROWS SIT ON --------------------------------------------------------------------
    ('the loom -- a row asserting a grade against a retired declaration', 'ROW', LOOM,
     '| no-conspiracy twin primes |'),
    ('the loom -- the row that states its own retirement', 'ROW', LOOM,
     '| GRH exclusion (form) |'),
    ('the engine -- a row grading SHELL', 'ROW', EE,
     '| `mass_gap` / `Massless` |'),
    ('the internal record -- the exclusion kernel as the papers describe it', 'ROW', SEFF,
     '##### *demonstranda*'),
    ('the deposited companion -- a surface no act may edit', 'ROW', DEPOSITED,
     '# The Third Identity Element and Riemann'),

    # ---- THE INSTRUMENT THIS ACT IS LICENSED TO CORRECT -----------------------------------------------
    ('the exerciser -- the sentence b372 made false', 'HOOK', HOOKS,
     'guard is a TRACKED TEXT FILE, so git rewrites its line endings on checkout'),
    ('the exerciser -- its own naming of what it cannot catch', 'HOOK', HOOKS,
     'AND ONE HAZARD THIS TOOL CANNOT CATCH, NAMED RATHER THAN IMPLIED'),

    # ---- WHAT THE RECORD ALREADY RULED ----------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and will '
     'report'),
    ('the lore -- the durability split, in its own words', 'LORE', DUR,
     '**A repair to a TRACKED file travels with a clone. A repair to an UNTRACKED one does not.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b373 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b373_extract_notes', LINES)
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
    rec('  ### ### **AND THE HEADS ARE PRINTED HERE ONLY SO A READER KNOWS WHEN THIS ACT RAN.**')
    rec('  ### ### **NO PIN THIS ACT WRITES COMES FROM ANY OF THEM** -- `(R9)` forbids it, because a')
    rec('  ### ### head dates a claim to today rather than to when it was made.')
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
        rec('  [%-6s] %s' % (tag, label))
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
    rec('  ### **NO BUILD WAS RUN, NO `.lean` FILE WAS WRITTEN, AND NO ROW WAS EDITED BY THIS FILE.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b373_extract_notes', LINES)
    io.open(d('b373_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
