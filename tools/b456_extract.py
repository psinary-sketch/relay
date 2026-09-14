# -*- coding: utf-8 -*-
"""b456_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE ERRATA ENTRY, THE LIVE NOTE, THE PROFILE AND THE
ROUTED ANNOTATIONS. ### Addresses and quotations only; nothing is written to the corpus here."""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
OUT = os.path.join(D, 'b456_extract.txt')
L, MISSES = [], []
A = os.path.join(PP, 'archive', '2026-08-24-ledger-split')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def quote_text(txt, name, needle, label, show=150):
    hit = [(i + 1, l.strip()) for i, l in enumerate(txt.replace(chr(13), '').split(chr(10))) if needle in l]
    if not hit:
        MISSES.append((label, name, needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (name, i, l[:show]))
    return i


def quote(path, needle, label, show=150):
    try:
        txt = io.open(path, encoding='utf-8-sig', errors='replace').read()
    except Exception:
        txt = ''
    return quote_text(txt, os.path.basename(path), needle, label, show)


def main():
    rec('=' * 100)
    rec('b456 -- THE SURVEY. ### THE ERRATA ENTRY, THE LIVE NOTE, AND THE ROUTED ANNOTATIONS COMPLETED.')
    rec('=' * 100)
    rec('')
    rec('(P1) b455`S BANK: THE CLAIMS AND THE GRADES.')
    quote(os.path.join(D, 'b455_components.txt'), '### DEPOSIT-LEVEL MATTER: C2', 'P1 C2')
    quote(os.path.join(D, 'b455_components.txt'), '### DEPOSIT-LEVEL MATTER: C6', 'P1 C6')
    quote(os.path.join(D, 'b455_components.txt'), '| C5 *"it certifies exactly what it literally states.', 'P1 C5 DERIVES row')
    quote(os.path.join(D, 'b455_components.txt'), 'THE CORRECTED COUNTS: ADDED 8', 'P1 the decided line')
    rec('')
    rec('(P2) ERRATA: ITS TAIL, ITS PARTITION, ITS FORMS.')
    er = io.open(os.path.join(PP, 'ERRATA.md'), encoding='utf-8').read().replace(chr(13), '')
    EL = er.split(chr(10))
    rec('      ERRATA.md lines %d ; last non-blank line %d : %r' % (len(EL), max(i for i, l in enumerate(EL) if l.strip()) + 1, [l for l in EL if l.strip()][-1]))
    quote(os.path.join(PP, 'ERRATA.md'), '## E-2026-09-07-1 —', 'P2 last entry heading', 60)
    quote(os.path.join(PP, 'ERRATA.md'), '**DEPOSIT-FACING** — entries that correct or concern a deposited artifact', 'P2 partition deposit-facing', 90)
    quote(os.path.join(PP, 'ERRATA.md'), '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.', 'P2 E-2026-08-24-2 no-action line')
    rec('      ERRATA.md carries "E-2026-09-14" : %s' % ('E-2026-09-14' in er))
    rec('')
    rec('(P3) THE PIN BESIDE WHICH THE NOTE GOES.')
    quote(os.path.join(PP, 'REGISTRY.md'), '| ### **`SIDE-kernel`** | ### **`v1.5` = `0e5233f`** — the deposited wave;', 'P3 REGISTRY lineage row', 80)
    quote(os.path.join(PP, 'REGISTRY.md'), '| repo | ### **DEPOSIT-PIN** *(what published prose cites)* |', 'P3 its table header', 80)
    quote(os.path.join(PP, 'REGISTRY.md'), '### **PHASE 1.2 — FROZEN** *(verdict recorded 2026-08-14', 'P3 the block after the table', 80)
    quote(os.path.join(PP, 'README.md'), '**Kernel:** [SIDE-kernel](https://github.com/psinary-sketch/SIDE-kernel) — cited by named terminal, not by count.', 'P3 README kernel line', 80)
    quote(os.path.join(PP, 'README.md'), '**Federation:** ~45 further Lean kernels', 'P3 README next line', 60)
    quote(os.path.join(PP, 'README.md'), 'route terminals re-profiled clean at the v1.5 enactment', 'P3 the front door`s profile sentence', 60)
    quote(os.path.join(D, 'b359_fetch_F2.json'), 'All route terminals report {propext, Classical.choice, Quot.sound}', 'P3 the record`s profile sentence', 40)
    rec('')
    rec('(P4) THE DEPOSITED TAG`S TREE, FOR A PROFILE ARTEFACT.')
    tree = git(KER, 'ls-tree', '-r', '--name-only', 'v1.5').split()
    rec('      v1.5 peels to %s ; files %d' % (git(KER, 'rev-parse', '--short', 'v1.5^{commit}').strip(), len(tree)))
    rec('      files whose names carry axiom/profile/print/notes/deposit : %s' % [f for f in tree if re.search(r'(?i)axiom|profile|print|notes|deposit', f)])
    rec('      "depends on axioms" in the tag, by file : %s' % sorted(set(l.split(':')[1] for l in git(KER, 'grep', '-l', '-I', 'depends on axioms', 'v1.5').split())))
    quote_text(git(KER, 'show', 'v1.5:DEPOSIT_v1_2_NOTES.md'), 'SIDE-kernel@v1.5:DEPOSIT_v1_2_NOTES.md', '## v1.2 tag — SHA triple', 'P4 notes heading')
    quote_text(git(KER, 'show', 'v1.5:AxiomCheck_V3B.lean'), 'SIDE-kernel@v1.5:AxiomCheck_V3B.lean', 'Profile expected unchanged.', 'P4 V3B script')
    quote_text(git(KER, 'show', 'v1.5:AxiomCheck_ROUTE1A_C6.lean'), 'SIDE-kernel@v1.5:AxiomCheck_ROUTE1A_C6.lean', 'expected UNCHANGED', 'P4 C6 script')
    rec('')
    rec('(P5) THE STATEMENTS OF A v1.5-ERA RUN ELSEWHERE.')
    quote(os.path.join(A, 'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md'), '`offLine_of_codim_two` profile `{propext, Classical.choice, Quot.sound}`, C₆-model neighbours unmoved', 'P5 loom receipt', 80)
    quote(os.path.join(A, 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'), 'verified unmoved at the deposit `v1.5` = `0e5233f`', 'P5 trail statement', 80)
    rec('')
    rec('(P6) THE ROUTED ITEMS AT THEIR ADDRESSES.')
    quote(os.path.join(A, 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'), "Euler-product consumption at Face E", 'P6 the line b455 decided', 60)
    quote(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'), '::', 'P6 INVARIANCE carries no b454 block (first `::` line, for position)', 40)
    rec('      INVARIANCE_BARRIERS.md carries "b454" : %s ; "T3 Tier-1 scope" block : %s' % (
        'b454' in io.open(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'), encoding='utf-8').read(),
        'bearing on the T3 Tier-1 scope' in io.open(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'), encoding='utf-8').read()))
    quote(os.path.join(PP, 'phase1.5', 'method', 'EXHAUSTIVENESS_LICENSE.md'), '*v0.1 — 2026-07-25 (W-LADDER build; kernel skeleton HELD on branch, main untouched)*', 'P6 EXH:9')
    R = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
    for n in ('| the 𝔽_q anatomy (§6) | same branch |', '| the realization ledger (§6) | same branch |', '| the finite-range inhabitant (§6) | same branch |', '| the eight further rows above | same branch |'):
        quote(R, n, 'P6 RES held cell', 70)
    quote(R, "not a citation in this document, but it names this document's held-branch work", 'P6 RES:145 second term', 70)
    quote(os.path.join(D, 'b454_registration_2026-09-14.txt'), '`RES:145`   -- `The cited held branch` -> `The cited merged branch`', 'P6 b454 face`s term for :145')
    quote(os.path.join(D, 'b454_ferry.txt'), '(a) The eight branch lines: state word', 'P6 the order b454 carried')
    rec('')
    rec('(P7) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '456'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'STARTS AT|THE CURRENT SPAN|UNPARSED', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
