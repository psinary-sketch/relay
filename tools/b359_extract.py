# -*- coding: utf-8 -*-
"""b359_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **THIS ACT CLASSIFIES CLAIMS IN TWO LEDGERS AGAINST A THIRD AND AGAINST A FETCH**, and the extract
### IS its evidence: every claim it classifies must be locatable at the file that carries it, and every
### ranking party's sentence must be locatable too, so a `STALE` verdict is a comparison of two lines on
### disk rather than a comparison of a line against a memory.
### ### **BAR 2: A CLAIM THIS ACT CANNOT LOCATE IS NOT CLASSIFIED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
README = os.path.join(PP, 'README.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REG = os.path.join(PP, 'REGISTRY.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- b359, the ledger currency pass', 'ORDER', d('b359_ferry_2026-09-07.txt'),
     'ACT b359 — THE LEDGER CURRENCY PASS. The executor'),
    ('the order -- addition one, the precedence', 'ORDER', d('b359_ferry_2026-09-07.txt'),
     'ADDITION ONE — THE PRECEDENCE IS STATED AND OBEYED: the source'),
    ('the order -- addition two, pins read live', 'ORDER', d('b359_ferry_2026-09-07.txt'),
     'ADDITION TWO — THE PINS ARE READ LIVE, NEVER RECALLED: every'),
    ('the order -- addition three, the mirror carries the repair', 'ORDER', d('b359_ferry_2026-09-07.txt'),
     'ADDITION THREE — THE MIRROR CARRIES WHAT THIS ACT REPAIRED:'),
    ('the order -- nothing is deposited, in any branch', 'ORDER', d('b359_ferry_2026-09-07.txt'),
     'the wave stays parked; NOTHING IS DEPOSITED AND NOTHING IS'),

    # ---- THE PRECEDENCE, AND THE RULE ABOUT PINS ----------------------------------------------------
    ('THE PRECEDENCE -- the front door states it', 'PRECEDENCE', README,
     'later reader can re-run this: REGISTRY > README > SPIRAL_MAP for deposits; disk'),
    ('THE PRECEDENCE -- disk for live pins only, never for deposits', 'PRECEDENCE', README,
     'for live pins only, never for deposits.**'),
    ("THE PIN RULE -- a pin and a head are two objects (REGISTRY's ruling, quoted in the map)",
     'PRECEDENCE', MAP,
     'a repository has a pin the corpus cites in published prose and a head where work continues'),
    ("THE MAP'S OWN RECONCILIATION NOTE", 'PRECEDENCE', MAP,
     '## Reconciliation note — 2026-08-24'),
    ("THE FRONT DOOR'S OWN RECONCILIATION NOTE", 'PRECEDENCE', README,
     'Reconciled to `REGISTRY.md` at content (the precedence source) under the standing'),

    # ---- THE SOURCE OF TRUTH -----------------------------------------------------------------------
    ("REGISTRY -- the governing d1-1 row", 'REGISTRY', REG,
     '| d1-1 | A Place to Stand (monograph) |'),
    ("REGISTRY -- the deposit line, contents per the record itself", 'REGISTRY', REG,
     'Published on Zenodo — current deposit **v1.1.2**'),
    ("REGISTRY -- the last-updated line and its repair", 'REGISTRY', REG,
     '**Last updated:** **2026-08-24** (b145, the census seam'),
    ("REGISTRY -- the rule that REGISTRY is the single source of truth", 'REGISTRY', README,
     '**REGISTRY.md is the single source of truth.**'),

    # ---- THE FRONT DOOR'S CLAIMS -------------------------------------------------------------------
    ('README -- the deposit note for day1', 'README', README,
     '**Deposit note (`day1/`).** Citable deposits: the monograph at manuscript'),
    ('README -- the kernel pin asserted at the top', 'README', README,
     '**Kernel:** [SIDE-kernel](https://github.com/psinary-sketch/SIDE-kernel)'),
    ('README -- REGISTRY described as the single source of truth', 'README', README,
     '| **REGISTRY.md** | The single source of truth.'),
    ('README -- the day1 tree line', 'README', README,
     '├── day1/                ← 7 papers + monograph (live line; see deposit note below)'),

    # ---- THE MAP'S CLAIMS --------------------------------------------------------------------------
    ('MAP -- the frozen Day-1 deposit table, marked as history', 'MAP', MAP,
     '**Frozen Day-1 deposit (history):**'),
    ('MAP -- the historical annotation that the row is not rewritten', 'MAP', MAP,
     'the row is historical and is not rewritten'),
    ('MAP -- the deposit wave table heading', 'MAP', MAP,
     '**Deposit wave (2026-07, current published DOIs):**'),
    ('MAP -- the monograph row in the deposit wave', 'MAP', MAP,
     '| *A Place to Stand* monograph Zenodo v1.1.2 (ms v5.10.2) |'),
    ('MAP -- the kernel row in the deposit wave', 'MAP', MAP,
     '| SIDE-kernel v1.5 (`0e5233f`) |'),
    ('MAP -- the lv-conservation row in the deposit wave', 'MAP', MAP,
     '| SIDE-lv-conservation v0.10.0 (`93c27ec`) |'),
    ('MAP -- the T7 row in the deposit wave', 'MAP', MAP,
     '| T7 matched-arc search | 10.5281/zenodo.21436282 |'),
    ('MAP -- the lv-conservation pin and working head as two columns', 'MAP', MAP,
     '| `SIDE-lv-conservation` | deposit-pin **v0.10.0** (`93c27ec`) · working head'),
    ('MAP -- the SIDE-effects pin', 'MAP', MAP,
     '| ### **`SIDE-effects`** | ### **`main` `afa9ccf`**'),
    ('MAP -- the t7-topology-cmb pin', 'MAP', MAP,
     '| `SIDE-t7-topology-cmb` | v0.3 (`8eb0d5a`) |'),
    ('MAP -- the version line and what v0.6 refreshed', 'MAP', MAP,
     '**v0.6 — July 2026** (revises v0.5 — currency'),
    ('MAP -- the two rows it already corrected in its own note', 'MAP', MAP,
     '**Two rows were stale and are corrected above.**'),

    # ---- THE STANDING RULES ------------------------------------------------------------------------
    ('b358 -- the finding this act carries to the faces ledger', 'RULE', d('b358_the_li_asymptotics.txt'),
     'THE ARCHIMEDEAN HALF IS UNCONDITIONAL, AND BOTH SOURCES SAY SO INDEPENDENTLY'),
    ('b358 -- the zero half has no unconditional bound', 'RULE', d('b358_the_li_asymptotics.txt'),
     'THE ZERO HALF HAS NO UNCONDITIONAL BOUND AT ALL'),
    ('b358 -- the index distance, measured', 'RULE', d('b358_the_li_asymptotics.txt'),
     'THE RATIO, ONE LABELLED DIVISION OF TWO BANKED COUNTS'),
    ('b358 -- the draft this order adopts', 'RULE', d('b358_closing.txt'),
     'b359 -- THE LEDGER CURRENCY PASS. ### **A MECHANICAL ACT'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b359 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b359_extract_notes', LINES)
        return 2
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
            rec('      %s' % str(e)[:150])
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n,
                          differs=bool(differs)))
        rec('')
        rec('  [%-10s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b359_extract_notes', LINES)
    io.open(d('b359_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
