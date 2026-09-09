# -*- coding: utf-8 -*-
"""b379_filings.py -- ADDITION THREE: ### **TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE.**

### ### **FILING ONE -- THE VERSION AND CLASS DRIFT.** ### The registry carries the download-layer
### narrative book at one version and one class; other documents carry it at a later version and a
### different class. ### Both sides are quoted with file and line, ### **AND THE PRECEDENCE RULE THE
### CORPUS ITSELF STATES IS NAMED** ### rather than invented here.
### ### ### **THE REGISTRY IS NOT EDITED BY THIS ACT.** ### Under the corpus's own rule the registry
### is what the others reconcile TO, and ### **A SEAT THAT EDITS THE PRECEDENCE SOURCE TO MATCH A
### ### DOCUMENT THAT DRIFTED HAS INVERTED THE RULE IT IS ENFORCING.**

### ### **FILING TWO -- THE POPULATION QUESTION.** ### The document is outside the repository tree by
### ruling, so it was outside the census's population on both axes. ### `b375` swept tracked markdown
### in `PLACE-papers`; this file is not in that sweep and never could have been.
### ### **FILED WHERE THE RULING'S EVIDENCE SITS, SO THE RULING CAN SAY WHETHER IT GOVERNS DOCUMENTS
### ### OUTSIDE THE TREE.**

### ### **NEITHER FILING OPENS WORK ON THE DOCUMENT.** ### It is not read for content, not classified,
### not graded, not moved, not renamed and not repaired. ### **THE ONLY THING READ OFF THE DOWNLOAD
### ### LAYER IS WHICH VERSIONS EXIST AND HOW LARGE THEY ARE**, which is what makes the drift
### measurable rather than asserted.
"""
import hashlib
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
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STEM = 'A_WOUND_UP_ENOUGH_CRANK'
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def q(path, hint, label):
    """### **QUOTED WITH FILE AND LINE, THE ANCHOR READ FROM THE FILE.**"""
    n, line = AF.find(path, hint)
    rel = os.path.relpath(path, PP).replace(os.sep, '/') if path.startswith(PP) \
        else os.path.basename(path)
    rec('    ### **%s** -- `%s` line %d' % (label, rel, n))
    for seg in re.findall(r'.{1,96}(?:\s|$)', line.strip()):
        if seg.strip():
            rec('      | %s' % seg.rstrip())
    return dict(label=label, file=rel, line=n, text=line.strip())


def main():
    rec('=' * 100)
    rec('b379 -- ADDITION THREE: ### **TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE.**')
    rec('=' * 100)
    rec('')

    # ------------------------------------------------------------------ WHAT IS ACTUALLY ON DISK
    rec('-' * 100)
    rec('  ### WHAT IS ACTUALLY ON THE DOWNLOAD LAYER. ### **ENUMERATED, NOT ASSUMED.**')
    rec('-' * 100)
    versions = []
    for n in sorted(os.listdir(DL)):
        if n.startswith(STEM) and n.endswith('.md'):
            p = os.path.join(DL, n)
            b = io.open(p, 'rb').read()
            versions.append(dict(name=n, bytes=len(b), sha256=hashlib.sha256(b).hexdigest()))
            rec('    %-44s %8d bytes   sha256 `%s`' % (n, len(b), versions[-1]['sha256'][:16]))
    rec('    ### ### **VERSIONS PRESENT : %d**' % len(versions))
    rec('    ### **AND NOT ONE OF THEM WAS OPENED FOR CONTENT BY THIS ACT.** ### The bytes were')
    rec('    ### hashed and the names were listed; ### **THE BOOK WAS NOT READ, CLASSIFIED OR GRADED.**')

    # ---------------------------------------------------------------------------- FILING ONE
    rec('')
    rec('-' * 100)
    rec('  ### FILING ONE -- THE VERSION AND CLASS DRIFT.')
    rec('-' * 100)
    rec('  ### **WHAT THE REGISTRY SAYS:**')
    reg = []
    reg.append(q(os.path.join(PP, 'REGISTRY.md'),
                 '## ANNEX: Download-Layer (non-keystone, outside the repo tree)',
                 'the ANNEX heading'))
    reg.append(q(os.path.join(PP, 'REGISTRY.md'),
                 '*Files that live on `D:\\MY-DOwnloads\\` outside `PLACE-papers`. Non-keystone, '
                 'not for', 'the ANNEX caption'))
    reg.append(q(os.path.join(PP, 'REGISTRY.md'),
                 '| `A_WOUND_UP_ENOUGH_CRANK_v0_5.md` (`D:\\MY-DOwnloads\\`) | Crank/scratch '
                 'exploratory', 'the row itself'))
    rec('')
    rec('  ### **WHAT OTHER DOCUMENTS SAY:**')
    later = []
    later.append(q(os.path.join(PP, 'phase1.5', 'method', 'CRANK_HARVEST_LIST.md'),
                   '*Tier N, private, attorney-facing. 2026-07-28. The paragraphs of',
                   'the harvest list, on the class'))
    later.append(q(os.path.join(PP, 'phase1.5', 'method', 'CRANK_HARVEST_LIST.md'),
                   '*Grade: Tier N harvest routing list; the CRANK',
                   'the harvest list, on the gate'))
    later.append(q(os.path.join(PP, 'phase1.5', 'method', 'patent-package', '00_INDEX.md'),
                   '**4 · ORIENTATION ONLY, FENCED.** `A_WOUND_UP_ENOUGH_CRANK` v0.7 '
                   '(the narrative keystone,', 'the patent index, at the latest version'))
    rec('')
    rec('  ### ### **THE DRIFT, STATED PLAINLY:**')
    rec('  ###   the registry names ### **`v0_5`** ### and calls it ### **NON-KEYSTONE, NOT FOR')
    rec('  ###   ### PUBLICATION**;')
    rec('  ###   the harvest list names ### **`v0_6`** ### and calls it a ### **`TIER C` NARRATIVE')
    rec('  ###   ### KEYSTONE**;')
    rec('  ###   the patent index names ### **`v0.7`** ### and calls it ### **THE NARRATIVE KEYSTONE**,')
    rec('  ###   travelling ### **FENCED, FOR BACKGROUND COMPREHENSION ONLY**;')
    rec('  ###   and ### **%d VERSIONS SIT ON THE DISK.**' % len(versions))
    rec('  ### ### ### **SO THE DRIFT IS NOT A PAIR OF DOCUMENTS DISAGREEING. ### IT IS A CHAIN THAT')
    rec('  ### ### ### MOVED AND A PRECEDENCE SOURCE THAT DID NOT**, which is `(E3)` as this act`s')
    rec('  ### ### ### face registered it.')

    rec('')
    rec('  ### **THE PRECEDENCE RULE THE CORPUS STATES, QUOTED AND NOT INVENTED:**')
    prec = []
    prec.append(q(os.path.join(PP, 'README.md'),
                  '1. **REGISTRY.md is the single source of truth.** Update it whenever you update '
                  'a paper.', 'the front door, on precedence'))
    prec.append(q(os.path.join(PP, 'README.md'),
                  '*Reconciled to `REGISTRY.md` at content (the precedence source) under the '
                  'standing', 'the front door, naming it the precedence source'))
    rec('')
    rec('  ### ### ### **UNDER THAT RULE THE REGISTRY IS WHAT THE OTHERS MUST RECONCILE TO**, so the')
    rec('  ### ### ### documents that moved ahead of it are the ones out of step -- ### **AND THAT IS')
    rec('  ### ### ### A STATEMENT ABOUT PRECEDENCE, NOT ABOUT WHICH DESCRIPTION IS CORRECT.** ### The')
    rec('  ### registry may be stale and the later documents may be right; ### **THE RULE SAYS WHERE')
    rec('  ### ### THE ANSWER IS RECORDED, NOT WHAT THE ANSWER IS.**')
    rec('  ### ### **FILED FOR THE AUTHOR. ### THE REGISTRY IS NOT EDITED BY THIS ACT** -- a seat that')
    rec('  ### edits the precedence source to match a document that drifted has inverted the rule it')
    rec('  ### is enforcing, and ### **THE CHOICE BETWEEN UPDATING THE ROW AND CORRECTING THE OTHERS')
    rec('  ### ### IS THE AUTHOR`S.**')

    # ---------------------------------------------------------------------------- FILING TWO
    rec('')
    rec('-' * 100)
    rec('  ### FILING TWO -- THE POPULATION QUESTION, FILED WHERE THE RULING`S EVIDENCE SITS.')
    rec('-' * 100)
    P375 = json.load(io.open(os.path.join(D, 'b375_population.json'), encoding='utf-8'))
    AX = json.load(io.open(os.path.join(D, 'b376_axes.json'), encoding='utf-8'))
    RS = json.load(io.open(os.path.join(D, 'b379_rescore.json'), encoding='utf-8'))
    inpop = [x for x in AX['scored'] if STEM in x['file']]
    rec('  ### the census population, as `b375` built it : ### **%d tracked markdown documents in')
    rec('  ### `PLACE-papers`** -- and that is the population `b376` scored on both axes and `b379`')
    rec('  ### re-scored on the apparatus axis.')
    rec('  ###   documents in that population : %d' % len(AX['scored']))
    rec('  ###   ### **THE DOWNLOAD-LAYER BOOK AMONG THEM : %d**' % len(inpop))
    rec('  ### ### ### **IT IS OUTSIDE THE REPOSITORY TREE BY RULING, SO IT WAS OUTSIDE THE')
    rec('  ### ### ### POPULATION ON BOTH AXES -- NOT SCORED `B-`, NOT SCORED `A?`, BUT NEVER')
    rec('  ### ### ### CONSIDERED AT ALL.**')
    rec('  ### **AND THAT IS UNLIKE EVERY OTHER OMISSION THIS SEQUENCE HAS FOUND.** ### `b376`s')
    rec('  ### narrowness scored documents wrongly; ### **THIS DOCUMENT WAS NEVER SCORED**, and no')
    rec('  ### widening of a matcher would have reached it.')
    rec('')
    rec('  ### **WHY IT IS FILED WITH THE RULING`S EVIDENCE:** ### the ruling `b376` and `b377`')
    rec('  ### assembled evidence for is about ### **WHAT `KEYSTONE` NAMES.** ### One document outside')
    rec('  ### the tree is described by the corpus as a ### **NARRATIVE KEYSTONE** ### in one place and')
    rec('  ### as ### **NON-KEYSTONE** ### in another. ### **SO THE RULING HAS TO SAY WHETHER IT')
    rec('  ### ### GOVERNS DOCUMENTS OUTSIDE THE TREE**, and if it does, the census`s population is')
    rec('  ### not the ruling`s population.')
    rec('  ### ### **THE OPTIONS THIS RAISES ARE NOT ENUMERATED HERE AND NONE IS RECOMMENDED.** ### The')
    rec('  ### fact is filed; ### **THE RULING IS THE AUTHOR`S.**')
    rec('')
    rec('  ### ### **NEITHER FILING OPENS WORK ON THE DOCUMENT.** ### It was not read for content, not')
    rec('  ### classified, not graded, not moved, not renamed and not repaired, and ### **NOTHING ON')
    rec('  ### ### THE DOWNLOAD LAYER WAS WRITTEN.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b379_filings_notes', LINES)
    io.open(os.path.join(D, 'b379_filings.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(stem=STEM, versions=versions, n_versions=len(versions),
                        registry=reg, later=later, precedence=prec,
                        population=len(AX['scored']), in_population=len(inpop),
                        rescored=RS['swept'],
                        registry_edited=False, download_layer_written=False,
                        document_opened=False, filings=2,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
