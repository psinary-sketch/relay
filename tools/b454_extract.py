# -*- coding: utf-8 -*-
"""b454_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR (R63) UNDER (R64) AND THE SPAN-HEADING REPAIR.
### ### Quotations at their lines; no ledger search for any finding, no terminal search, no edit is made here
### (those are the components' work, under rules the face fixes first)."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b454_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def quote(path, needle, label, show=170):
    try:
        ls = io.open(path, encoding='utf-8-sig', errors='replace').read().splitlines()
    except Exception:
        ls = []
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, path, needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (os.path.basename(path), i, l[:show]))
    return i


def git(repo, *a):
    p = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.stdout


def main():
    K = lambda rel: os.path.join(PP, *rel.split('/'))
    PATHS = K('phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md')
    EXH = K('phase1.5/method/EXHAUSTIVENESS_LICENSE.md')
    RES = K('phase1.5/proofs/THE_RESIDUE_OF_RH.md')
    IA = K('phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md')
    REG = K('REGISTRY.md')
    CEN = K('phase2/method/THE_KEYSTONE_CENSUS.md')
    FND = K('FINDINGS.md')
    ARC = K('archive/2026-08-24-ledger-split')
    rec('=' * 100)
    rec('b454 -- THE SURVEY. ### (R63) EXECUTED UNDER (R64), AND THE SPAN-HEADING WORK-ORDER REPAIRED.')
    rec('=' * 100)
    rec('')
    rec('(P1) THE TWENTY-NINE, AS b451 GROUPED THEM (data/b451_kinds.json), AND WHAT (R64)(2) WITHDREW.')
    kj = json.load(io.open(os.path.join(D, 'b451_kinds.json'), encoding='utf-8'))
    rec('      counts %s ; by form %s' % (kj['counts'], kj['by_form']))
    forms = {}
    for it in kj['items']:
        forms.setdefault(it['form'], []).append(it['n'])
    for f in sorted(forms):
        rec('      %-26s %2d : items %s' % (f, len(forms[f]), forms[f]))
    rc = [it for it in kj['items'] if 'bd2ae1a' in it['what']]
    rec('      withdrawn by (R64)(2): item %s -- %s / %s' % (rc[0]['n'], rc[0]['keystone'], rc[0]['what']) if rc else '      ### MISS : R_CURVE item')
    if not rc:
        MISSES.append(('P1 R_CURVE item', 'b451_kinds.json', 'bd2ae1a'))
    rec('')
    rec('(P2) THE EIGHT BRANCH LINES AT THEIR ADDRESSES, AND THE FAST-FORWARD TIPS.')
    quote(PATHS, 'The cited held branch `word-pairing-interface` of `SIDE-lv-conservation` EXISTS AND IS SOUND', 'P2 PATHS:420', 110)
    quote(PATHS, 'is compiled as an interface on the held branch (`SIDE-lv-conservation` `word-pairing-interface` @ `66485cb`)', 'P2 PATHS:440', 110)
    quote(EXH, 'SIDE-lv-conservation, held branch `word-pairing-interface`', 'P2 EXH:95', 110)
    quote(EXH, '(HELD on branch `w-ladder-skeleton`, SIDE-effects; main untouched)', 'P2 EXH:101', 110)
    quote(EXH, 'HELD — nothing merged, nothing deposited (governing publication posture)', 'P2 EXH:112', 110)
    quote(RES, 'read from the held branch `word-pairing-interface` (SIDE-lv-conservation; **not merged, nothing deposited**)', 'P2 RES:97', 110)
    quote(RES, '### **HELD-BRANCH — NOT MERGED, NOT DEPOSITED**', 'P2 RES:126', 110)
    quote(RES, '| ### **one cited pin fails** |', 'P2 RES:145', 110)
    for repo, tip in (('SIDE-lv-conservation', '5a14205'), ('SIDE-effects', 'a0dc376')):
        rp = os.path.join('D:', os.sep, repo)
        fp = [c for c in git(rp, 'rev-list', '--first-parent', 'main').split() if c.startswith(tip)]
        rec('      %s : %s on main`s first-parent line : %s ; subject: %s' % (repo, tip, bool(fp), git(rp, 'log', '--format=%s', '-1', tip).strip()[:90]))
        if not fp:
            MISSES.append(('P2 tip', repo, tip))
    rec('')
    rec('(P3) THE ERA FINDINGS AS THE CENSUS NAMES THEM, AND THE LEDGERS (R64)(2) NAMES.')
    for n in ('the `S2` Ostrowski seal as re-stated in the sealed inventory', 'the E-Difficulty cross-link verdict (`DISTINCT`; `κ` NOT claimed)',
              'Face E / keyhole (i)+(iv) as used by the `S`-table; the `T3` Tier-1 scope', 'the sign-face registers, the sealed `S1`–`S6` table, the crossing filing',
              'the two-kinds windows verdict |', '`W_∞` is NOT sign-definite, and the Day-1 §I attribution is repaired to pole-plus-archimedean'):
        quote(CEN, n, 'P3 census row', 120)
    rec('      PLACE-papers commits: b449 %s ; b450 %s' % (git(PP, 'log', '--format=%h %s', '-1', '687aa24').strip()[:60], git(PP, 'log', '--format=%h %s', '-1', '8fc56a1').strip()[:60]))
    for f in sorted(os.listdir(ARC)):
        rec('      archive split file : %s (%d lines)' % (f, len(io.open(os.path.join(ARC, f), encoding='utf-8', errors='replace').read().splitlines())))
    quote(os.path.join(ARC, 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'), 'support truncation controls width exactly as', 'P3 control address', 120)
    rec('')
    rec('(P4) THE ANNOTATION FORMS THE KEYSTONES CARRY.')
    quote(PATHS, '### ERA ANNOTATION (2026-08-12) — bearing on the five identification paths', 'P4 PATHS era form')
    quote(PATHS, '*Provenance: `OPEN_TRAILS.md`, the ray adjudication, 2026-08-11. **This note states a later finding and edits no argument above it.** No claim in this document moves.*', 'P4 PATHS provenance', 80)
    quote(IA, '### ERA ANNOTATION (2026-08-12) — bearing on the index truncation', 'P4 INDEX_ARITY era form')
    quote(RES, '### ERA ANNOTATION (2026-08-12) — bearing on the residue', 'P4 RESIDUE era form')
    quote(K('phase1.5/method/TECHNE_TOOLKIT.md'), '#### **CURRENCY ANNOTATION** *(2026-09-13, b450;', 'P4 b450 currency form', 90)
    quote(K('phase1.5/spectral/GRH_CASCADE.md'), '#### **RECONCILIATION ANNOTATION** *(2026-09-09, b394;', 'P4 b394 form', 90)
    rec('')
    rec('(P5) THE REGISTRY: THE ROW, THE CLUSTERS, THE FORMS, AND THE HEADS.')
    quote(REG, '| 1.5a-7 | Index Arity at the Critical Line | `phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md` | v0.5 |', 'P5 row 1.5a-7', 110)
    quote(IA, 'v0.18, 2026-08-08 (v0.1 2026-07-31;', 'P5 INDEX_ARITY head version', 60)
    quote(REG, '### 1.5A: Alternative Proof Presentations', 'P5 cluster 1.5A')
    quote(REG, '### 1.5H: SIDE Method Papers', 'P5 cluster 1.5H')
    quote(REG, '| 1.5h-8 | Invariance Barriers in Analytic Number Theory |', 'P5 row 1.5h-8', 60)
    quote(REG, '2. When you add a paper, add a row here FIRST.', 'P5 how-to line')
    quote(REG, '## STATUS KEY', 'P5 status key')
    quote(REG, '## Row addition — 2026-07-11 (Phase 1.5A; fold into Phase 1.5 table at next hand edit)', 'P5 row-addition form')
    quote(REG, '## Row update — 2026-07-11 (Phase 1.5D; fold into Phase 1.5 table at next hand edit)', 'P5 row-update form')
    reg = io.open(REG, encoding='utf-8').read()
    for w in ('numbering', 'next in sequence', 'ID convention', 'IDs are'):
        rec('      REGISTRY lines carrying %-20r : %d' % (w, sum(1 for l in reg.splitlines() if w.lower() in l.lower())))
    ids = sorted(set(re.findall(r'\|\s*(1\.5[ah]-\d+)\s*\|', reg)), key=lambda s: (s[:4], int(s.split('-')[1])))
    rec('      ids present, 1.5a : %s' % [i for i in ids if i.startswith('1.5a')])
    rec('      ids present, 1.5h : %s' % [i for i in ids if i.startswith('1.5h')])
    rec('      "1.5a-8" in REGISTRY : %s ; "1.5h-9" in REGISTRY : %s' % ('1.5a-8' in reg, '1.5h-9' in reg))
    quote(EXH, '# The Exhaustiveness License: a graded ladder for "is the catalogue complete?"', 'P5 EXH H1')
    quote(EXH, '*v0.1 — 2026-07-25 (W-LADDER build; kernel skeleton HELD on branch, main untouched)*', 'P5 EXH version line')
    quote(EXH, '## 1. The object: what an exhaustiveness license grades', 'P5 EXH head ends')
    quote(RES, '# The Residue of the Riemann Hypothesis', 'P5 RES H1')
    quote(RES, '*v1.1 — 2026-07-27 (the substrate season absorbed; author-approved; joined the W-1.5 keystone set)*', 'P5 RES version line')
    quote(RES, '## 1. The two-channel anatomy', 'P5 RES head ends')
    rec('')
    rec('(P6) ENUMERA, THE GRADES, AND THE ROSTER.')
    EN = K('phase1.5/method/ENUMERA.md')
    quote(EN, '**The load-bearing claim:** The seven-class catalogue is exhaustive.', 'P6 ENUMERA load-bearing claim', 400)
    quote(REG, '| 1.5h-3 | Exhaustive Enumeration as a Proof Method | `phase1.5/method/ENUMERA.md` | v1.5 |', 'P6 row 1.5h-3', 100)
    quote(K('README.md'), '### The four grades', 'P6 README grades')
    quote(K('README.md'), '- **NOT THE CLAIM** — the theorem is sound and its statement is **strictly weaker than the', 'P6 NOT THE CLAIM')
    quote(os.path.join(T, 'b377_branch.py'), "if n.startswith('SIDE-') and os.path.isdir(os.path.join(p, '.git')):", 'P6 roster rule (b373, carried at b377)')
    kern = sorted(n for n in os.listdir('D:' + os.sep) if n.startswith('SIDE-') and os.path.isdir(os.path.join('D:' + os.sep, n, '.git')))
    rec('      rostered kernels by that rule : %d' % len(kern))
    rec('')
    rec('(P7) THE WORK-ORDER AT ITS OWN ADDRESS, AND THE TOOL IT NAMES.')
    quote(FND, '**W-ORD-SPAN-HEADING.** `tools/b363_span.py` finds fold sections by', 'P7 work-order', 400)
    quote(FND, '## The external-grading arc — b423 through b432, folded at b434', 'P7 the missed heading')
    quote(os.path.join(T, 'b363_span.py'), "for m in re.finditer(r'^## (.*?), b(\\d+)–b(\\d+) — THE FOLD\\s*$', txt, re.M):", 'P7 folds() pattern')
    quote(os.path.join(T, 'b363_span.py'), "heads = [m.start() for m in re.finditer(r'^## .*— THE FOLD\\s*$', txt, re.M)]", 'P7 filed_by() pattern')
    rec('')
    rec('(P8) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '454'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'STARTS AT|runs through|THE CURRENT SPAN|NOTHING WAS WRITTEN', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
