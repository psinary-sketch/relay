# -*- coding: utf-8 -*-
"""b379_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
TC = os.path.join(DL, 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b379_ferry_2026-09-08.txt')
B378CLOSE = d('b378_closing.txt')
B378BANK = d('b378_the_refs_widened.txt')
README = p('README.md')
REGISTRY = p('REGISTRY.md')
HARVEST = p('phase1.5', 'method', 'CRANK_HARVEST_LIST.md')
PATIDX = p('phase1.5', 'method', 'patent-package', '00_INDEX.md')
LOOMARCH = p('archive', '2026-08-24-ledger-split',
             'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')
TAX = p('phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b379 - THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS. The'),
    ('the order -- the standing positive-control clause', 'ORDER', FERRY,
     'gate and re-checked if the registration is rewritten; every'),
    ('the order -- the standing error-exit clause', 'ORDER', FERRY,
     'presence first; an error exit is not an answer. The instrument'),
    ('the order -- addition one, the direction registered first', 'ORDER', FERRY,
     'ADDITION ONE - THE DIRECTION IS REGISTERED BEFORE THE RUN: a'),
    ('the order -- addition one, bounded below', 'ORDER', FERRY,
     'corrected population is bounded below by the prior figure and'),
    ('the order -- addition one, both columns side by side', 'ORDER', FERRY,
     'corrected quadrant table with both the prior and corrected'),
    ('the order -- addition one, which options it weakens', 'ORDER', FERRY,
     "columns side by side. State which of the ruling's options the"),
    ('the order -- addition two, the row categories', 'ORDER', FERRY,
     'ADDITION TWO - THE ROW CATEGORIES, from what b378 found: a'),
    ('the order -- addition two, manuscript-resident', 'ORDER', FERRY,
     'a row may name a corpus document rather than a terminal, which'),
    ('the order -- addition two, a category is not an absence', 'ORDER', FERRY,
     "already has one, so a checker stops reporting a category as an"),
    ('the order -- addition three, the two filings', 'ORDER', FERRY,
     'ADDITION THREE - TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE,'),
    ('the order -- addition three, the registry is not edited', 'ORDER', FERRY,
     'and file the drift for the author - the registry is not edited'),
    ('the order -- addition three, outside the tree by ruling', 'ORDER', FERRY,
     'outside the census population on both axes.'.replace('census p', "census's p")),
    ('the order -- addition three, neither filing opens work', 'ORDER', FERRY,
     'can say whether it governs documents outside the tree. Neither'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'this act found. The navigator'),
    ('the order -- (F2), a document moves into the quadrant', 'ORDER', FERRY,
     'prior figure; (F2) at least one document moves into the'),
    # ---- THE DRAFT THIS ORDER ADOPTS ---------------------------------------------------------------
    ('the draft -- component 1, the suspect column re-measured', 'DRAFT', B378CLOSE,
     '### ### ### **COMPONENT 1 -- THE SUSPECT COLUMN, RE-MEASURED.**'),
    ('the draft -- component 1, the interesting number', 'DRAFT', B378CLOSE,
     '### ### **THE INTERESTING NUMBER IS NOT THE NEW'),
    ('the draft -- component 2, the fourteen that survive', 'DRAFT', B378CLOSE,
     '### ### **COMPONENT 2 -- THE `14` THAT SURVIVE, CLASSIFIED ONE MORE STEP.**'),
    ('the draft -- component 3, the other not-determinable document', 'DRAFT', B378CLOSE,
     '### ### **COMPONENT 3 -- THE OTHER `NOT DETERMINABLE` DOCUMENT.**'),
    ('the draft -- component 4, and how silence would be read', 'DRAFT', B378CLOSE,
     '### ### **THIS DRAFT DOES NOT CHOOSE BETWEEN COMPONENTS 1-3 AND COMPONENT 4; THE AUTHOR DOES**'),
    ('b378 -- the column named suspect and not re-measured', 'DRAFT', B378BANK,
     '###     ### **`b376`S ENTIRE AXIS-B COLUMN** -- `303` documents scored `B-` on that predicate.'),
    # ---- THE FRONT DOOR'S OWN WORDS ----------------------------------------------------------------
    ('the front door -- what a correspondence row maps', 'FRONT', README,
     'Each row maps a claim the paper makes to the artifact that verifies it: **claim ·'),
    ('the front door -- manuscript-resident and research-reach', 'FRONT', README,
     'exists, the status says so in words — *manuscript-resident* or *research-reach* —'),
    ('the front door -- the day-1 companions name terminals in prose', 'FRONT', README,
     "with one; the day-1 companions instead name their terminals in prose, carried by"),
    ('the front door -- the three grades', 'FRONT', README, '### The three grades'),
    ('the precedence rule -- REGISTRY is the single source of truth', 'FRONT', README,
     '1. **REGISTRY.md is the single source of truth.** Update it whenever you update a paper.'),
    ('the precedence rule -- reconciled to REGISTRY at content', 'FRONT', README,
     '*Reconciled to `REGISTRY.md` at content (the precedence source) under the standing'),
    # ---- THE DRIFT ---------------------------------------------------------------------------------
    ('the registry -- the ANNEX heading', 'DRIFT', REGISTRY,
     '## ANNEX: Download-Layer (non-keystone, outside the repo tree)'),
    ('the registry -- the ANNEX caption', 'DRIFT', REGISTRY,
     '*Files that live on `D:\\MY-DOwnloads\\` outside `PLACE-papers`. Non-keystone, not for'),
    ('the registry -- the row itself, at v0_5', 'DRIFT', REGISTRY,
     '| `A_WOUND_UP_ENOUGH_CRANK_v0_5.md` (`D:\\MY-DOwnloads\\`) | Crank/scratch exploratory'),
    ('the later claim -- the harvest list calls it a Tier C narrative keystone', 'DRIFT', HARVEST,
     '*Tier N, private, attorney-facing. 2026-07-28. The paragraphs of'),
    ('the later claim -- the crank stays downstream of the patent gate', 'DRIFT', HARVEST,
     '*Grade: Tier N harvest routing list; the CRANK'),
    ('the later claim -- the patent index carries v0_7 as the narrative keystone', 'DRIFT', PATIDX,
     '**4 · ORIENTATION ONLY, FENCED.** `A_WOUND_UP_ENOUGH_CRANK` v0.7 (the narrative keystone,'),
    # ---- THE TAXONOMY THE RULING IS ABOUT ----------------------------------------------------------
    ("the taxonomy -- Tier K and what it obliges", 'TAX', TAX, '**Tier K — Keystone-certified.**'),
    ('the taxonomy -- Tier C, which certifies nothing', 'TAX', TAX,
     '**Tier C — Cluster-synthesis.** A document that **organizes** certified results'),
    # ---- THE LORE ----------------------------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and '
     'will report'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    rec('=' * 100)
    rec('b379 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec('  ### anchor_from_file fixtures : %s' % (AF.self_test() if hasattr(AF, 'self_test') else True))
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        dirty = bool(git(repo, 'status', '--porcelain'))
        refs[name] = dict(branch=br, head=hd, dirty=dirty)
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, br, hd, dirty))
    rec('')
    rec('  ### **AND THE DOCUMENT ADDITION THREE IS ABOUT LIVES OUTSIDE EVERY ONE OF THEM**, on the')
    rec('  ### download layer. ### Its versions on disk, enumerated and not typed:')
    for n in sorted(os.listdir(DL)):
        if n.startswith('A_WOUND_UP_ENOUGH_CRANK'):
            rec('      %-44s %d bytes' % (n, os.path.getsize(os.path.join(DL, n))))
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-6s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=None,
                            text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:210])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=n,
                        text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (differing, len(READS)))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO REGISTRY ROW WAS TOUCHED.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b379_extract_notes', LINES)
    io.open(d('b379_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
