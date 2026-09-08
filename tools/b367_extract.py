# -*- coding: utf-8 -*-
"""b367_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE SUBJECT OF THIS ACT IS A KERNEL'S OWN TEXT**, and `BAR 1` of the locked registration fixes
### that a terminal this act cannot locate is reported ### **NOT LOCATED** ### and is never described from
### the navigator's recall.
### ### **AND `BAR 2`: EVERY QUOTATION CARRIES THE REF IT CAME FROM.** ### A quotation without its ref is
### a quotation from a repository and not from a state.
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
GRHK = os.path.join('D:', os.sep, 'SIDE-grh-transfer')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b367_ferry_2026-09-07.txt')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
README = os.path.join(PP, 'README.md')
FIND = os.path.join(PP, 'FINDINGS.md')

READS = [
    # ---- THE ORDER AND ITS CAP ---------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY, 'ACT b367 - THE SCAFFOLD REPAIR: READ AND PRICED, NEVER A'),
    ('the order -- the cap', 'ORDER', FERRY, 'CAP, quoted in the registration: ONE act; a location, a read'),
    ('the order -- NOT LOCATED stops the act', 'ORDER', FERRY,
     'statement proved; NOT LOCATED stops the act, as the draft'),
    ('the order -- the hint is recall and NOT a file', 'ORDER', FERRY,
     'ADDITION ONE - THE HINT, AND ITS STATUS. The navigator asserts'),
    ('the order -- (H1) and (H2)', 'ORDER', FERRY,
     'from RECALL and NOT from any file: the kernel is SIDE-effects;'),
    ('the order -- (H3), the two subjects', 'ORDER', FERRY,
     'excluding the generalized hypothesis and excluding an'),
    ('the order -- (H4), the branch', 'ORDER', FERRY,
     "exceptional real zero; and the kernel's working head may sit on"),
    ('the order -- and why the ref must be stated', 'ORDER', FERRY,
     'act read, since a read of main would miss a head that is not'),
    ('the order -- addition two, what must be quoted', 'ORDER', FERRY,
     'ADDITION TWO - WHAT THEY ARE, quoted: each terminal'),
    ('the order -- and the full-prominence clause', 'ORDER', FERRY,
     'restriction quoted from wherever the record states it. If any'),
    ('the order -- addition three, the three routes', 'ORDER', FERRY,
     'ADDITION THREE - THE THREE ROUTES, priced separately and none'),
    ('the order -- route (b) and the architecture it names', 'ORDER', FERRY,
     'premise named in the row, which the record calls a legitimate'),
    ('the order -- addition four, the recommendation is the author’s', 'ORDER', FERRY,
     'ADDITION FOUR - THE RECOMMENDATION IS THE AUTHOR'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'registered here: (F1) the terminals are located, on a non-main'),

    # ---- THE KERNEL'S OWN TEXT ---------------------------------------------------------------------
    ("the kernel -- the module's own title", 'KERNEL', STRUCT, 'SIDE-EFFECTS — STRUCTURAL CONTENT'),
    ('the kernel -- what the audit found the skeletons were', 'KERNEL', STRUCT,
     'A Phase S.2–S.4 audit found those skeletons were either True-valued'),
    ('the kernel -- and the other shape, which is the one that matters here', 'KERNEL', STRUCT,
     '(a theorem taking its conclusion'),
    ('the kernel -- they compiled clean and said nothing', 'KERNEL', STRUCT,
     '0 sorry and 0 axioms but said nothing about their named problems,'),
    ('the kernel -- the retirement ledger, its own heading', 'KERNEL', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the kernel -- the GRH entry', 'KERNEL', STRUCT,
     'exhaustiveness analog). (Retired: opaque-Prop `grh_exclusion`,'),
    ('the kernel -- the Landau-Siegel entry', 'KERNEL', STRUCT,
     'Classical-reduction from GRH; no dedicated kernel. (Retired:'),
    ('the kernel -- where the genuine GRH content lives instead', 'KERNEL', STRUCT,
     'Genuine GRH content is the separate SIDE-grh-transfer kernel (real'),

    # ---- THE KERNEL'S FRONT DOCUMENT ---------------------------------------------------------------
    ('the front document -- its GRH layer line', 'FRONT', AGENTS,
     '- **GRH layer**: `twist_cancels`, `formation_preserved_grh`, `grh_exclusion`'),
    ('the front document -- its Landau-Siegel layer line', 'FRONT', AGENTS,
     '- **Landau-Siegel layer**: `no_ls_zero`'),
    ('the front document -- and what it says the module formalizes', 'FRONT', AGENTS,
     '`SIDEEffects/Structural.lean` formalizes the structural content for nine framework'),

    # ---- WHAT THE RECORD ALREADY HELD --------------------------------------------------------------
    ("the record -- the ferry's own premise, already superseded once", 'RECORD', TRAILS,
     "THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED"),
    ('the record -- they are retired and gone', 'RECORD', TRAILS,
     '*scaffold-pattern, citation-banned*. ### **They are retired and gone**, per'),
    ('the record -- the front document has not caught up', 'RECORD', TRAILS,
     'caught up: `AGENTS.md` lists 20 "Theorems exported" of which'),
    ('the record -- and the ban stands anyway', 'RECORD', TRAILS,
     'exist cannot be cited — **and it stands anyway, because a name can return.***'),

    # ---- THE RECORD'S OWN GRADING VOCABULARY, WHICH IS THE THREE ROUTES ----------------------------
    ('the record -- DERIVES', 'ROUTES', README,
     '- **DERIVES** — the theorem'),
    ('the record -- INTERFACES, and the architecture it sanctions', 'ROUTES', README,
     '- **INTERFACES** — the theorem takes the claim as a **named hypothesis**, discharged'),
    ('the record -- and that it is legitimate, not a defect', 'ROUTES', README,
     'elsewhere and identified in the row. This is a legitimate architecture, not a'),
    ('the record -- ENCODES-CONCLUSION / SHELL, which is what these were', 'ROUTES', README,
     '- **ENCODES-CONCLUSION / SHELL** — the theorem stipulates what the paper claims, or'),
    ('the record -- and that those are work-orders, not citations', 'ROUTES', README,
     'as such wherever they appear.'),
    ('the record -- INTERFACES used at its own route terminal', 'ROUTES', README,
     'ConservationBridge.riemann_hypothesis` (Route 3 — an INTERFACES terminal on the open'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def head(repo):
    r = subprocess.run(['git', '-C', repo, 'rev-parse', '--abbrev-ref', 'HEAD'],
                       capture_output=True, text=True)
    b = (r.stdout or '').strip()
    r2 = subprocess.run(['git', '-C', repo, 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True)
    return b, (r2.stdout or '').strip()


def main():
    rec('=' * 100)
    rec('b367 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b367_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### BAR 2 -- THE REFS THIS ACT READ, NAMED BEFORE ANYTHING IS QUOTED FROM THEM.')
    rec('-' * 100)
    refs = {}
    for lbl, repo in (('SIDE-effects (the kernel)', KERNEL),
                      ('SIDE-grh-transfer (where the ledger points)', GRHK),
                      ('PLACE-papers (the record)', PP)):
        b, h = head(repo)
        refs[os.path.basename(repo)] = dict(branch=b, head=h)
        rec('    %-42s ref `%s` at `%s`' % (lbl, b, h))
    rec('    ### ### **EVERY QUOTATION BELOW CARRIES THE REF ITS FILE WAS READ AT.**')
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
    ndiff = sum(1 for b in built if b['differs'])
    nker = sum(1 for b in built if b['tag'] in ('KERNEL', 'FRONT'))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec("  ### ### **LINES LOCATED INSIDE THE KERNEL ITSELF : %d** ### -- everything this act says about"
        % nker)
    rec('  ### the kernel is one of these, and none is retyped.')
    rec('  ### **AND NO `.lean` FILE WAS WRITTEN AND NO BUILD WAS RUN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b367_extract_notes', LINES)
    io.open(d('b367_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, kernel_lines=nker,
             refs=refs, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
