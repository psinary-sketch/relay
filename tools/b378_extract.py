# -*- coding: utf-8 -*-
"""b378_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **NO LINE NUMBER IN THIS FILE IS TYPED.** ### Each read names a file and a HINT; the anchor
### tool locates the hint and returns the line it actually found. ### **A HINT THAT MATCHES NOTHING,
### ### OR MATCHES TWICE, IS REFUSED** -- and the refusal is the tool working.
"""
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
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b378_ferry_2026-09-08.txt')
B377CLOSE = d('b377_closing.txt')
B377BANK = d('b377_the_unblocked_obligation.txt')
B376BANK = d('b376_the_two_axis_read.txt')
RESIDUE = p('phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
TAX = p('phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

# ### **THE POPULATION IS NAMED FROM `b377`'S BANKED JSON AND NEVER TYPED AS A LIST HERE.**
_BR = json.load(io.open(d('b377_branch.json'), encoding='utf-8'))
UNRESOLVED = []
for _r in _BR['six']:
    _amb = [a['name'] for a in _r['ambiguous']]
    for _n in _r['not_resolved']:
        UNRESOLVED.append(dict(name=_n, doc=_r['file'],
                               kind=('AMBIGUOUS' if _n in _amb else 'DECLARED-NOWHERE'),
                               kernels=([a['kernels'] for a in _r['ambiguous']
                                         if a['name'] == _n] or [[]])[0]))

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b378 - THE REFS WIDENED AND THE CONVENTION SWEPT. The'),
    ('the order -- the draft is adopted with three additions', 'ORDER', FERRY,
     "executor's draft is ADOPTED, with three additions."),
    ('the order -- the lock re-checked if the face is rewritten', 'ORDER', FERRY,
     'gate and RE-CHECKED if the registration is rewritten - b377'),
    ('the order -- addition one, every ref not main', 'ORDER', FERRY,
     'ADDITION ONE - EVERY REF, NOT MAIN: re-run the terminal search'),
    ('the order -- addition one, an upper bound at one ref', 'ORDER', FERRY,
     'the corrected classification and state plainly that the earlier'),
    ('the order -- addition one, the held branch by name', 'ORDER', FERRY,
     'names a held branch in its own text, that branch is searched by'),
    ('the order -- addition two, the two conventions', 'ORDER', FERRY,
     'ADDITION TWO - THE TWO CONVENTIONS: the corpus writes terminal'),
    ('the order -- addition two, a discrimination arm', 'ORDER', FERRY,
     'polarities and a discrimination arm proving it still refuses a'),
    ('the order -- addition two, none is rewritten', 'ORDER', FERRY,
     'documents are correct in their own dialect and none is'),
    ('the order -- addition two, what the narrowness cost', 'ORDER', FERRY,
     "rewritten. State what the earlier predicate's narrowness cost"),
    ('the order -- addition three, the archives', 'ORDER', FERRY,
     'ADDITION THREE - THE ARCHIVES, CONFIRMED AND NOT REMOVED: for'),
    ('the order -- addition three, never by filename', 'ORDER', FERRY,
     'content match - never by filename, since the repository strips'),
    ('the order -- addition three, remove nothing', 'ORDER', FERRY,
     "nothing; the removal is the author's and depends on this"),
    ('the order -- the closing', 'ORDER', FERRY,
     "CLOSING: the lock gate's remaining hole closed as the draft"),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     "the next ferry as DRAFT - NAVIGATOR EDITS. The navigator's"),
    ('the order -- (F2), a non-main ref', 'ORDER', FERRY,
     'thirty-seven; (F2) at least one identifier is found on a'),
    # ---- THE DRAFT THIS ORDER ADOPTS ---------------------------------------------------------------
    ('the draft -- component 1, the names no kernel declares', 'DRAFT', B377CLOSE,
     '### ### ### **COMPONENT 1 -- THE `37` NAMES NO KERNEL DECLARES, WHICH IS THE FINDING THIS ACT'),
    ('the draft -- component 1, five explanations', 'DRAFT', B377CLOSE,
     '### ### THAT IS NOT**, and they are distinguishable by reading: the name is prose and never was a'),
    ('the draft -- component 1, only main was searched', 'DRAFT', B377CLOSE,
     "### ### **AND `b377`'S BRANCH TOOL SEARCHED ONLY `main` AT EACH KERNEL.**"),
    ('the draft -- component 2, close the hole in the tool', 'DRAFT', B377CLOSE,
     "### ### **COMPONENT 2 -- CLOSE THE LOCK GATE'S HOLE IN THE TOOL.**"),
    ('the draft -- component 3, the two by hand', 'DRAFT', B377CLOSE,
     '### ### **COMPONENT 3 -- THE TWO `NOT DETERMINABLE` DOCUMENTS, BY HAND.**'),
    ('the draft -- component 4, the author chooses', 'DRAFT', B377CLOSE,
     '### ### **THIS DRAFT DOES NOT CHOOSE BETWEEN COMPONENT 4 AND THE REST; THE AUTHOR DOES.**'),
    # ---- THE INCIDENT THIS ACT'S STEP ZERO CURES ---------------------------------------------------
    ('b376 -- what the lock gate could not do', 'HOLE', B376BANK,
     '### ### **WHAT THE LOCK GATE STILL CANNOT DO, DECLARED ON THE LOCKED FACE BEFORE IT RAN:** ### it'),
    ('b377 -- the hole hit in practice', 'HOLE', B377BANK,
     '### ### ### **AND THE HOLE `b376` NAMED WAS HIT IN PRACTICE HERE.** ### The registration text'),
    ('b377 -- the predicate had its own share of the defect', 'HOLE', B377BANK,
     '### ### ### **SO THE DEFECT WAS PARTLY THE PREDICATE`S AND NOT THE DOCUMENTS`, AND THIS ACT`S'),
    # ---- THE HELD BRANCH, NAMED BY THE DOCUMENT ITSELF ---------------------------------------------
    ('the held branch -- the document names it in its own text', 'HELD', RESIDUE,
     'The seven branch artifacts and the edge lemma, at their pins with `#print axioms` profiles,'),
    ('the held branch -- the row that cites it', 'HELD', RESIDUE,
     '| the residue, compiled (§7) | `SIDE-lv-conservation`, branch `word-pairing-interface` |'),
    ('the held branch -- the pin the document already calls unreproducible', 'HELD', RESIDUE,
     '| ### **one cited pin fails** |'),
    # ---- THE OBLIGATION ----------------------------------------------------------------------------
    ("the taxonomy -- Tier K and what it obliges", 'TAX', TAX,
     '**Tier K — Keystone-certified.**'),
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
    rec('b378 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
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
        rec('      | %s' % line.strip()[:200])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=n,
                        text=line.rstrip(chr(10))))
    rec('')
    rec('-' * 100)
    rec('  ### THE POPULATION, NAMED FROM `b377`S BANKED JSON AND NOT TYPED HERE.')
    rec('-' * 100)
    kinds = {}
    for u in UNRESOLVED:
        kinds[u['kind']] = kinds.get(u['kind'], 0) + 1
    rec('    unresolved identifiers carried forward : ### **%d** ### %s' % (len(UNRESOLVED), kinds))
    for u in UNRESOLVED:
        rec('      %-46s %-22s %s' % (u['name'][:46], u['kind'],
                                      os.path.basename(u['doc'])[:-3]))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (differing, len(READS)))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO DECLARATION WAS MOVED.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b378_extract_notes', LINES)
    io.open(d('b378_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, unresolved=UNRESOLVED,
                        unresolved_kinds=kinds, built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
