# -*- coding: utf-8 -*-
"""b371_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE, NEVER TYPED.**

### ### **THE REFS ARE PRINTED BEFORE ANY QUOTATION**, and the construction kernel's are printed twice:
### the working ref and the tag the registry pins, because ### **THE WHOLE OF COMPONENT 1 TURNS ON WHICH
### ### OF THE TWO A NUMBER WAS TRUE AT.**
### ### **NO BUILD IS RUN AND NO `.lean` FILE IS WRITTEN.**
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
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b371_ferry_2026-09-08.txt')
GS_README = os.path.join(GS, 'README.md')
GS_CORR = os.path.join(GS, 'CORRESPONDENCE.md')
GS_PRINTS = os.path.join(GS, 'AXIOM_PRINTS.txt')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
DUR = os.path.join(TC, 'modules', '2026-09', 'DURABILITY_SPLIT.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')
HOOKSRC = t(os.path.join('git-hooks', 'pre-push'))
HOOKS = t('b304_hooks.py')

READS = [
    ('the order -- the act', 'ORDER', FERRY,
     "ACT b371 - THE AUDIT'S FIRST TARGET, THE DESK CLOSED, THE HOOK"),
    ('the order -- (R6), the audit re-scoped', 'ORDER', FERRY,
     '(R6) THE AUDIT IS RE-SCOPED TO WHAT IS CITED. Its first pass is'),
    ('the order -- (R6), the reason recorded', 'ORDER', FERRY,
     'recorded: the rows are the surface a reader traverses and a'),
    ('the order -- (R7), the desk closes', 'ORDER', FERRY,
     '(R7) THE DESK CLOSES ITEMS. An item whose occasion is gone'),
    ('the order -- (R7), a desk that only accumulates', 'ORDER', FERRY,
     'UNCONFIRMED. A desk that only accumulates is a list.'),
    ('the order -- component 1, the two words', 'ORDER', FERRY,
     "kernel's public description names a Core terminal count. Read"),
    ('the order -- component 1, scope-dependent or stale', 'ORDER', FERRY,
     'now carries, and settle it: SCOPE-DEPENDENT (the two words'),
    ('the order -- component 1, the branch', 'ORDER', FERRY,
     'says so plainly enough that a reader would not be misled) or'),
    ('the order -- component 2, listed and not checked', 'ORDER', FERRY,
     'COMPONENT 2 - THE ROW INVENTORY, LISTED AND NOT CHECKED: under'),
    ('the order -- component 2, the criterion', 'ORDER', FERRY,
     'costs, and which rows are highest risk by a stated criterion'),
    ('the order -- component 2, audit nothing', 'ORDER', FERRY,
     'whether the kernel has moved since). Audit nothing.'),
    ('the order -- component 3, durable or struck', 'ORDER', FERRY,
     'COMPONENT 3 - THE HOOK MADE DURABLE OR STRUCK: the pre-push'),
    ('the order -- component 3, not both', 'ORDER', FERRY,
     'reason. Not both, and the choice is made by what the tracked'),
    ("the order -- the navigator's expectation", 'ORDER', FERRY,
     "navigator's expectation: the count claim is SCOPE-DEPENDENT and"),

    # ---- THE CONSTRUCTION KERNEL'S OWN DOCUMENTS -----------------------------------------------------
    ('the kernel README -- the Core line with its breakdown', 'KERNEL', GS_README,
     '- **`Core/`** — the vanilla load-bearing layer:'),
    ('the kernel README -- the assembly print ratio', 'KERNEL', GS_README,
     'assembly, `AXIOM_PRINTS.txt` (250/250). No terminal failed the bar; none is excluded.'),
    ('the kernel README -- the subject sentence', 'KERNEL', GS_README,
     "**Subject:** the construction era's verified Lean material for the global section"),
    ('the kernel README -- the register sentence', 'KERNEL', GS_README,
     '**The register sentence, exactly:**'),
    ('the kernel -- the first printed profile line', 'KERNEL', GS_PRINTS,
     "'ReDerivationShadow.expanding_the_scaling_operator_reconciles_all_three_terms' does not depend"),
    ("the kernel's own correspondence -- the tag count sentence", 'KERNEL', GS_CORR,
     'audit at v0.1.0 (103 + 11 = 114 exactly), and each act'),

    # ---- THE PAPERS REPOSITORY'S OWN PIN OF THAT COUNT ------------------------------------------------
    ('the registry -- the tag, and the count it pins', 'RECORD', REGISTRY,
     '**Subject:** the construction era’s verified Lean material — the finite-place models'),
    # ### **THE TABLE HEADER IS AMBIGUOUS SIX WAYS** -- the loom carries six identically-headed
    # ### concept tables. ### The anchor tool REFUSED it, which is the tool working: an ambiguous
    # ### anchor is not a located line. ### The SECTION HEADING above the first table is unique.
    ('the loom -- the first concept section heading', 'RECORD', LOOM,
     '## Structural skeleton — additive-multiplicative no-conspiracy'),
    ('the loom -- a row naming a kernel and a terminal', 'RECORD', LOOM,
     '| no-type-D exclusion |'),

    # ---- WHAT THE RECORD ALREADY RULED ---------------------------------------------------------------
    ('the lore -- the durability split, in its own words', 'LORE', DUR,
     '**A repair to a TRACKED file travels with a clone. A repair to an UNTRACKED one does not.**'),
    ('the lore -- what a durable fix would be', 'LORE', DUR,
     '**A durable fix for an untracked guard exists and is not free:**'),
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and will '
     'report'),

    # ---- THE GUARD THIS ACT MOVES --------------------------------------------------------------------
    ('the tracked guard -- its first rule', 'HOOK', HOOKSRC,
     '# (i) pushes to origin main only from push-* / repair-* branches;'),
    ('the tracked guard -- its own install line', 'HOOK', HOOKSRC,
     '# Tracked copy: tools/git-hooks/pre-push. Install:'),
    ('the exerciser -- its roster', 'HOOK', HOOKS, "NEG_BRANCH = 'hookcheck-b304'"),
    ('the exerciser -- what it says about the untracked directory', 'HOOK', HOOKS,
     '### ### (1) ### **`.git/hooks/` IS NOT TRACKED BY GIT.**'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b371 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b371_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, path in (('SIDE-global-section', GS), ('PLACE-papers', PP)):
        b = subprocess.run(['git', '-C', path, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        h = subprocess.run(['git', '-C', path, 'rev-parse', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
        lsr = subprocess.run(['git', '-C', path, 'ls-remote', 'origin', 'refs/heads/main'],
                             capture_output=True, text=True).stdout.split()
        lsr = lsr[0] if lsr else ''
        refs[name] = dict(branch=b, head=h, ls_remote=lsr, pinned=(lsr == h))
        rec('    %-22s ref `%s` = `%s`   ### ls-remote equal : %s' % (name, b, h, lsr == h))
    # ### **AND THE TAG, BECAUSE COMPONENT 1 TURNS ON WHICH REF A NUMBER WAS TRUE AT.**
    tags = subprocess.run(['git', '-C', GS, 'tag', '-l'], capture_output=True, text=True).stdout.split()
    rec('    ### **TAGS IN THE CONSTRUCTION KERNEL : %s**' % (tags or 'none'))
    tagref = {}
    for tg in tags:
        pe = subprocess.run(['git', '-C', GS, 'rev-parse', tg + '^{commit}'],
                            capture_output=True, text=True).stdout.strip()
        ahead = subprocess.run(['git', '-C', GS, 'rev-list', '--count', '%s..HEAD' % tg],
                               capture_output=True, text=True).stdout.strip()
        tagref[tg] = dict(commit=pe, head_ahead_by=ahead)
        rec('        `%s` = `%s` ### -- HEAD is `%s` commit(s) ahead of it' % (tg, pe, ahead))
    rec('    ### ### **AND THAT IS THE WHOLE OF COMPONENT 1 IN ONE LINE: A NUMBER TRUE AT A TAG IS NOT')
    rec('    ### ### A NUMBER TRUE AT A HEAD THAT HAS MOVED PAST IT.**')
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
    rec('  ### **AND NO BUILD WAS RUN AND NO `.lean` FILE WAS WRITTEN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b371_extract_notes', LINES)
    io.open(d('b371_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, by_tag=counts,
             refs=refs, tags=tagref, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
