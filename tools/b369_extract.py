# -*- coding: utf-8 -*-
"""b369_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE REF IS PRINTED BEFORE ANY QUOTATION FROM THE KERNEL**, and every kernel quotation carries
### it -- `(R4)`'s verbatim preservation depends on the quotation being of a NAMED state of the file.
### ### **NO `.lean` FILE IS WRITTEN AND NO BUILD IS RUN.** ### This file only reads.
### ### **AND IT READS THE TWO SENTENCES `b368` WROTE THAT `(R4)` WILL DATE**, so the act meets them
### before it edits rather than after.
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


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b369_ferry_2026-09-08.txt')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
B368 = d('b368_the_front_document_reconciled.txt')
B368C = d('b368_closing.txt')
PINS = t('b303_pins.py')
HOOKS = t('b304_hooks.py')
HOOKSRC = t(os.path.join('git-hooks', 'pre-push'))

READS = [
    # ---- THE ORDER -----------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY, 'ACT b369 - THE LIST REPAIRED, THE ROSTER MENDED, THE PASS'),
    ('the order -- (R4), the list repaired in place', 'ORDER', FERRY,
     '(R4) THE LIST IS REPAIRED IN PLACE. The original list is quoted'),
    ('the order -- (R4), preserve by quotation, repair by edit', 'ORDER', FERRY,
     'the list. Preserve by quotation, repair by edit. The kernel'),
    ('the order -- (R4), the reason recorded', 'ORDER', FERRY,
     'recorded: append-only is right for a ledger, where a reader'),
    ('the order -- (R5), the lacunae filed not invented', 'ORDER', FERRY,
     "(R5) THE RETIREMENT LEDGER'S OWN LACUNAE are filed, not"),
    ('the order -- (R5), what it will not write', 'ORDER', FERRY,
     'does not write retirement history it cannot source - where the'),
    ('the order -- component 1', 'ORDER', FERRY,
     'COMPONENT 1 - (R4) executed against the kernel at a live ref'),
    ('the order -- component 2, the two hygiene items', 'ORDER', FERRY,
     'COMPONENT 2 - THE TWO HYGIENE ITEMS: the exclusion kernel added'),
    ('the order -- component 2, why a hand pin is not enough', 'ORDER', FERRY,
     'that does not name a repository cannot pin it, and a pin taken'),
    ('the order -- component 3, priced and not run', 'ORDER', FERRY,
     'COMPONENT 3 - THE REFINEMENT PASS, PRICED AND NOT RUN. Enumerate'),
    ('the order -- component 3, without reading them for correctness', 'ORDER', FERRY,
     'module docstrings - WITHOUT reading them for correctness. Then'),
    ('the order -- component 3, the criterion', 'ORDER', FERRY,
     'stated criterion (age since last touch, whether the claim names'),
    ('the order -- component 3, the hint from recall', 'ORDER', FERRY,
     "hint to search on, from the navigator's RECALL and NOT from any"),
    ('the order -- component 3, audit nothing', 'ORDER', FERRY,
     'and the ranking; audit nothing.'),
    ('the order -- the closing and the fold', 'ORDER', FERRY,
     'NAVIGATOR EDITS, and it is the FOLD, b361 through b369, nine'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     "The navigator's expectations: (F1) the repair is one edit and"),

    # ---- THE FRONT DOCUMENT, AS IT STANDS BEFORE ANY EDIT ---------------------------------------------
    ('the front document -- the Layer 1 heading', 'FRONT', AGENTS,
     '### Layer 1 — Structural content (stable, `SIDEEffects/`)'),
    ('the front document -- its own count claim, adjacent and NOT in scope', 'FRONT', AGENTS,
     '`SIDEEffects/Structural.lean` formalizes the structural content for nine framework'),
    ('the front document -- the list opener', 'FRONT', AGENTS, 'Named theorems include:'),
    ('the front document -- the Yang-Mills row', 'FRONT', AGENTS, '- **Yang-Mills mass gap layer**:'),
    ('the front document -- the GRH row', 'FRONT', AGENTS, '- **GRH layer**:'),
    ('the front document -- the Landau-Siegel row', 'FRONT', AGENTS, '- **Landau-Siegel layer**:'),
    ('the front document -- the Type-D row', 'FRONT', AGENTS,
     '- **Additive-multiplicative / Type-D layer**:'),
    ('the front document -- the BSD row', 'FRONT', AGENTS, '- **BSD layer**:'),
    ('the front document -- the Artin row', 'FRONT', AGENTS, '- **Artin layer**:'),
    ('the front document -- the Shared engine row', 'FRONT', AGENTS, '- **Shared engine**:'),
    ('the front document -- the row after the list, which bounds the edit', 'FRONT', AGENTS,
     '`SIDEEffects/Milestones.lean` carries the analytic-existence statements'),

    # ---- THE TWO SENTENCES (R4) WILL DATE -------------------------------------------------------------
    ("b368's block -- appended, not edited", 'DATED', AGENTS,
     '*Appended, not edited. Nothing above this line has been changed.'),
    ("b368's block -- the list is left exactly as it was", 'DATED', AGENTS,
     '**It does not export anything.** Every name above appears under a status'),
    ("b368's block -- its own mark", 'DATED', AGENTS,
     '<!-- b368 currency block: layer-1 export list vs source -->'),

    # ---- THE KERNEL ----------------------------------------------------------------------------------
    ('the kernel -- the retirement ledger heading', 'KERNEL', STRUCT,
     '-- RETIREMENT LEDGER (audit Phase S.2–S.4)'),
    ('the kernel -- what the ledger says it lists', 'KERNEL', STRUCT,
     '-- content-free (True-stub or opaque-Prop). Honest status of each'),
    ('the kernel -- the first surviving declaration', 'KERNEL', STRUCT,
     'theorem formation_seven : 2 + 3 + 2 + 0 = 7 := rfl'),
    ('the kernel -- the second surviving declaration', 'KERNEL', STRUCT,
     'theorem no_type_d (α : Type) (coupling modular : α → Prop)'),

    # ---- THE TWO HYGIENE ITEMS, AS THEY STAND ---------------------------------------------------------
    ('the pins roster -- its own list', 'HYGIENE', PINS, "REPOS = ["),
    ('the pins roster -- the last entry before the mend', 'HYGIENE', PINS,
     "('PLACE-papers', r'D:\\MY-DOwnloads\\PLACE-papers'),"),
    ('the hook exerciser -- its own roster', 'HYGIENE', HOOKS,
     "NEG_BRANCH = 'hookcheck-b304'"),
    ('the tracked hook source -- its own first rule', 'HYGIENE', HOOKSRC,
     '# (i) pushes to origin main only from push-* / repair-* branches;'),
    ('the tracked hook source -- the install line it carries', 'HYGIENE', HOOKSRC,
     '# Tracked copy: tools/git-hooks/pre-push. Install:'),

    # ---- WHAT THE RECORD ALREADY HOLDS ---------------------------------------------------------------
    ('b368 -- the hook absence, filed and not repaired', 'RECORD', B368,
     'HAS NO PRE-PUSH HOOK.** ### The other three repositories this programme pushes'),
    ('b368 -- a roster that does not name a repository cannot pin it', 'RECORD', B368C,
     'is filed. ### **A ROSTER THAT DOES NOT NAME A REPOSITORY CANNOT PIN IT.**'),
    ('b368 -- the list is still wrong, and why it was left', 'RECORD', B368,
     'AND THE LIST ITSELF STILL EXPORTS 18 ABSENT NAMES.'),
    ('the record -- the trail entry this act updates', 'RECORD', TRAILS,
     'SCAFFOLD-TERMINALS` — UPDATED 2026-09-08 (b368)'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b369 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b369_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REF, PRINTED BEFORE ANY QUOTATION FROM THE KERNEL.')
    rec('-' * 100)
    b = subprocess.run(['git', '-C', KERNEL, 'rev-parse', '--abbrev-ref', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    h = subprocess.run(['git', '-C', KERNEL, 'rev-parse', 'HEAD'],
                       capture_output=True, text=True).stdout.strip()
    lsr = subprocess.run(['git', '-C', KERNEL, 'ls-remote', 'origin', 'refs/heads/main'],
                         capture_output=True, text=True).stdout.split()
    lsr = lsr[0] if lsr else ''
    rec('    SIDE-effects  ref `%s` = `%s`' % (b, h))
    rec('    ### **`ls-remote` origin/main = `%s` ### -- EQUAL : %s**' % (lsr, lsr == h))
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
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n,
                          differs=bool(differs)))
        rec('')
        rec('  [%-8s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for x in built if x['differs'])
    counts = {}
    for x in built:
        counts[x['tag']] = counts.get(x['tag'], 0) + 1
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **BY TAG : %s**' % counts)
    rec('  ### ### **THE SEVEN LIST ROWS ARE LOCATED BEFORE ANY EDIT, WHICH IS WHAT `(R4)` REQUIRES:**')
    rec('  ### the quotation must be of a state the act can name, not of whatever the file said when')
    rec('  ### the writer happened to open it.')
    rec('  ### **AND NO `.lean` FILE WAS WRITTEN AND NO BUILD WAS RUN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b369_extract_notes', LINES)
    io.open(d('b369_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             kernel_ref=b, kernel_head=h, kernel_ls_remote=lsr, pinned=(lsr == h), built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
