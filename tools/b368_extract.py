# -*- coding: utf-8 -*-
"""b368_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE REF IS PRINTED BEFORE ANY QUOTATION**, and every quotation carries it -- `b367`'s `BAR 2`,
### and this act's own `ADDITION ONE`.
### ### **NO `.lean` FILE IS WRITTEN AND NO BUILD IS RUN.** ### This file only reads.
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
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b368_ferry_2026-09-08.txt')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
FRAME = os.path.join(KERNEL, 'SIDEEffects', 'Phase15', 'SIDEFramework.lean')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FOLD = d('b360_the_fold.txt')
B367 = d('b367_the_scaffold_repair.txt')

READS = [
    ('the order -- the act', 'ORDER', FERRY, 'ACT b368 - THE FRONT DOCUMENT RECONCILED, OR PRICED. The'),
    ('the order -- addition one, the live read', 'ORDER', FERRY,
     'ADDITION ONE - THE READ IS LIVE AND ITS REF IS NAMED: the'),
    ('the order -- and why a carried figure will not do', 'ORDER', FERRY,
     'classification; the eighteen absent names are re-derived from'),
    ('the order -- addition two, the four kinds', 'ORDER', FERRY,
     'ADDITION TWO - EACH NAME CLASSIFIED, one row each: PRESENT'),
    ('the order -- never from its own sound', 'ORDER', FERRY,
     'NEVER EXISTED (with the search recorded). No name is'),
    ('the order -- addition three, the two branches', 'ORDER', FERRY,
     'ADDITION THREE - THE REPAIR OR THE PRICE. If the front document'),
    ('the order -- and the lean files untouched in either branch', 'ORDER', FERRY,
     'branch the kernel'),
    ('the order -- addition four, the desk rule', 'ORDER', FERRY,
     'ADDITION FOUR - THE DESK'),
    ('the order -- marks, not verdicts', 'ORDER', FERRY,
     'item is closed by this act; the sweep produces marks, not'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'NAVIGATOR EDITS. The navigator'),

    # ---- THE FRONT DOCUMENT'S OWN EXPORT LINES -----------------------------------------------------
    ('the front document -- what it says the module formalizes', 'FRONT', AGENTS,
     '`SIDEEffects/Structural.lean` formalizes the structural content for nine framework'),
    ('the front document -- the Yang-Mills layer', 'FRONT', AGENTS, '- **Yang-Mills mass gap layer**:'),
    ('the front document -- the GRH layer', 'FRONT', AGENTS, '- **GRH layer**:'),
    ('the front document -- the Landau-Siegel layer', 'FRONT', AGENTS, '- **Landau-Siegel layer**:'),
    ('the front document -- the Type-D layer', 'FRONT', AGENTS,
     '- **Additive-multiplicative / Type-D layer**:'),
    ('the front document -- the BSD layer', 'FRONT', AGENTS, '- **BSD layer**:'),
    ('the front document -- the Artin layer', 'FRONT', AGENTS, '- **Artin layer**:'),
    ('the front document -- the shared engine', 'FRONT', AGENTS, '- **Shared engine**:'),

    # ---- THE KERNEL'S OWN LEDGER -------------------------------------------------------------------
    ('the kernel -- the retirement ledger heading', 'LEDGER', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the kernel -- what the ledger says it lists', 'LEDGER', STRUCT,
     '-- content-free (True-stub or opaque-Prop). Honest status of each'),
    ('the kernel -- the Yang-Mills entry', 'LEDGER', STRUCT,
     '--     Theorem OPEN; no genuine kernel proves the mass gap. Genuine'),
    ('the kernel -- the GRH entry', 'LEDGER', STRUCT,
     'exhaustiveness analog). (Retired: opaque-Prop `grh_exclusion`,'),
    ('the kernel -- the Landau-Siegel entry', 'LEDGER', STRUCT,
     'Classical-reduction from GRH; no dedicated kernel. (Retired:'),
    ('the kernel -- the Type-D entry', 'LEDGER', STRUCT,
     'Milestones.lean. (Retired: `TypeD Nat (fun _ => True) (fun _ => True)`'),
    ('the kernel -- the BSD entry', 'LEDGER', STRUCT,
     '--     `bsd_fully_closed`/`BSD_architecture_fully_closed` decls in those'),
    ('the kernel -- the Artin entry', 'LEDGER', STRUCT,
     'Classical-reduction (Hooley 1967, conditional on GRH); no kernel.'),
    ('the kernel -- the trivial-identity entry, and its pointer', 'LEDGER', STRUCT,
     '--     Retired as a trivial identity; the genuine exclusion engine is'),
    ('the kernel -- the pointer’s own target, located', 'LEDGER', FRAME,
     'theorem SIDE_exclusion'),

    # ---- WHAT THE RECORD ALREADY HOLDS -------------------------------------------------------------
    ('the record -- the front document has not caught up', 'RECORD', TRAILS,
     'caught up: `AGENTS.md` lists 20 "Theorems exported" of which'),
    ('b367 -- the front document is the stale one', 'RECORD', B367,
     'THE SOURCE IS THE HONEST PARTY; THE FRONT DOCUMENT'),

    # ---- THE DESK THIS ACT SWEEPS ------------------------------------------------------------------
    ('the desk -- its own list, as the fold placed it', 'DESK', FOLD,
     'One list, each item with where it stands and what would move it: `M-2` under'),
    ('the desk -- the sentence it filed, opening nothing', 'DESK', FOLD,
     'no move aimed at the'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b368 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b368_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REF, PRINTED BEFORE ANY QUOTATION FROM THE KERNEL.')
    rec('-' * 100)
    b = subprocess.run(['git', '-C', KERNEL, 'rev-parse', '--abbrev-ref', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    h = subprocess.run(['git', '-C', KERNEL, 'rev-parse', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    rec('    SIDE-effects  ref `%s` = `%s`' % (b, h))
    rec('    ### **AND EVERY KERNEL QUOTATION BELOW IS FROM THAT REF.**')
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % str(e).replace(chr(10), ' | ')[:180])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n, differs=bool(differs)))
        rec('')
        rec('  [%-6s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for x in built if x['differs'])
    nled = sum(1 for x in built if x['tag'] == 'LEDGER')
    nfront = sum(1 for x in built if x['tag'] == 'FRONT')
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **LEDGER LINES LOCATED : %d ### / ### FRONT-DOCUMENT LINES LOCATED : %d.**'
        % (nled, nfront))
    rec('  ### **AND NO `.lean` FILE WAS WRITTEN AND NO BUILD WAS RUN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b368_extract_notes', LINES)
    io.open(d('b368_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff,
             ledger_lines=nled, front_lines=nfront, kernel_ref=b, kernel_head=h, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
