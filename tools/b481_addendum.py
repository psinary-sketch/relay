# -*- coding: utf-8 -*-
"""b481_addendum.py -- A FINDING FOUND BY THE CLOSING'S OWN NEGATIVE SEARCH, OUTSIDE THE REGISTERED
### POPULATION. ### The face registered FOUR SITES; this reads the WHOLE LIVE CORPUS for the
### SUPERSEDED monograph pin, and separates ### **A PIN** (a citation of the version a document was
### written against -- lawful) from ### **A CLAIM OF CURRENCY** (present tense: "Current:", "current
### deposit", "immutable Zenodo state" -- which REGISTRY contradicts).
### ### **NOTHING IS CORRECTED AND NO SITE IS EDITED. ### (N3) IS NOT RESCORED**: its population is
### the four sites the gate names, and this is not one of them.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


SUP = re.compile(r'21436278|Zenodo\s*\**v1\.1\.1')
# ### ### **THE CURRENCY PREDICATE, STATED BEFORE IT IS RUN.** ### A line claims currency only if it
# ### says so in the PRESENT TENSE about the deposit. ### A line that merely names the version, or
# ### that says "superseded", is a PIN and is NOT counted.
CUR = re.compile(r'\b(Current\s*:|current deposit|currently|CURRENT IMMUTABLE|is the current|'
                 r'now (?:at|carries))', re.I)
SUPERSEDED = re.compile(r'supersed', re.I)
SITES = ('README.md', 'SPIRAL_MAP.md', 'REGISTRY.md')


def main():
    rec('=' * 100)
    rec('b481 ADDENDUM -- THE SUPERSEDED PIN ACROSS THE WHOLE LIVE CORPUS.')
    rec('### ### **OUTSIDE THE REGISTERED POPULATION. ### NOTHING IS CORRECTED.**')
    rec('=' * 100)
    pins, claims, sup = [], [], []
    files = 0
    for base, dirs, fl in os.walk(PP):
        if 'archive' in base or '.git' in base:
            continue
        for fn in fl:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(base, fn)
            rel = os.path.relpath(p, PP).replace(os.sep, '/')
            text = read(p)
            lines = text.split(NL)
            hit = False
            for i, l in enumerate(lines):
                if not SUP.search(l):
                    continue
                hit = True
                # ### ### **THE SENTENCE IS READ, NOT THE LINE.** ### `ERRATA.md`'s head says "The
                # ### current deposit is the monograph at manuscript v5.8 / Zenodo **v1.1.1**" and the
                # ### bank HARD-WRAPS between "current deposit is" and the version -- so a line-wise
                # ### currency test reads the pin without its own verb and files it as a bare pin.
                # ### **THAT IS b-NEEDLE-ANCHOR-WRAPPING, AND IT UNDERCOUNTS IN THE UNSAFE DIRECTION.**
                # ### The window is the whole PARAGRAPH the pin sits in.
                a = i
                while a > 0 and lines[a - 1].strip():
                    a -= 1
                b = i
                while b + 1 < len(lines) and lines[b + 1].strip():
                    b += 1
                para = ' '.join(x.strip() for x in lines[a:b + 1])
                # ### ### **AND THE WINDOW NARROWS AGAIN, FROM PARAGRAPH TO SENTENCE.** ### The
                # ### paragraph window read `INTEGRATED_PROOF.md:14` as a currency claim because the
                # ### paragraph carries a bare monograph pin AND, four hundred characters away, the
                # ### word "currently" -- about simplicity being implied by the trace formula.
                # ### **A PARAGRAPH IS WIDE ENOUGH TO HOLD A PIN AND AN UNRELATED VERB.** ### The
                # ### test is whether the currency word sits in the pin's OWN SENTENCE. ### A DOI
                # ### carries no period-space, so splitting on `. ` cannot cut one in half.
                sent = para
                for s in re.split(r'(?<=[.!?])\s+', para):
                    if SUP.search(s):
                        sent = s
                        break
                row = (rel, i + 1, sent, para)
                if SUPERSEDED.search(sent):
                    sup.append(row)
                elif CUR.search(sent):
                    claims.append(row)
                else:
                    pins.append(row)
            files += 1 if hit else 0

    # ### ### **A QUOTATION IS NOT A CLAIM, AND AN ANNOTATED CLAIM IS NOT AN UNCORRECTED ONE.**
    # ### Two separations, both made by reading the corpus and not by the seat's say-so:
    # ###   (a) a paragraph that QUOTES a stale sentence in order to repair it -- `ERRATA.md:289` --
    # ###       carries the correct figure in the SAME paragraph; and
    # ###   (b) a stale head sentence that a later append ANNOTATES is preserved by the ledger's own
    # ###       append-only law, which is the record working, not drifting.
    CORRECT = re.compile(r'21539167|v1\.1\.2')
    ANNOT = {}
    for f, i, sent, para in claims:
        ft = read(os.path.join(PP, f.replace('/', os.sep)))
        ANNOT[(f, i)] = bool(re.search(r'CURRENCY NOTE|drift repair by appending', ft)) \
            and bool(CORRECT.search(ft))
    quoting = [(f, i, s) for f, i, s, _ in claims if CORRECT.search(s)]
    annotated = [(f, i, s) for f, i, s, _ in claims
                 if not CORRECT.search(s) and ANNOT[(f, i)]]
    live = [(f, i, s) for f, i, s, _ in claims
            if not CORRECT.search(s) and not ANNOT[(f, i)]]
    rec('  live .md files carrying the superseded monograph pin : %d' % files)
    rec('  lines, by kind:')
    rec('    ### **PINS** -- name the version, claim nothing about currency : %d' % len(pins))
    rec('    ### **SUPERSESSION NOTICES** -- say so in the line itself      : %d' % len(sup))
    rec('    ### **CURRENCY CLAIMS** -- present tense about the deposit     : %d' % len(claims))
    rec('')
    rec('  ### THE SUPERSESSION NOTICES, which are the record working correctly:')
    for f, i, s, _ in sup:
        rec('      %s:%d' % (f, i))
        rec('        %s' % s[:150])
    rec('')
    rec('  ### SENTENCES THAT USE THE PRESENT TENSE ABOUT THE DEPOSIT : %d. ### Three kinds,'
        % len(claims))
    rec('  ### separated by reading the corpus and not by the seat`s say-so:')
    rec('')
    rec('    ### (a) ### **QUOTING IN ORDER TO REPAIR** -- the correct figure is in the SAME')
    rec('    ### paragraph, so the paragraph is the record working : %d' % len(quoting))
    for f, i, p in quoting:
        rec('        %s:%d' % (f, i))
        rec('          %s' % p[:180])
    rec('')
    rec('    ### (b) ### **STALE BUT ANNOTATED** -- preserved by an append-only ledger`s own law and')
    rec('    ### corrected by a later append in the same file : %d' % len(annotated))
    for f, i, p in annotated:
        rec('        %s:%d' % (f, i))
        rec('          %s' % p[:180])
    rec('')
    rec('    ### (c) ### **A LIVE, UNANNOTATED CURRENCY CLAIM THAT REGISTRY CONTRADICTS : %d.**'
        % len(live))
    off = []
    for f, i, p in live:
        flag = '' if f in SITES else '   ### NOT A SITE THE GATE NAMES'
        rec('        %s:%d%s' % (f, i, flag))
        rec('          %s' % p[:300])
        if f not in SITES:
            off.append((f, i))
    rec('')
    rec('  ### ### **LIVE CURRENCY CLAIMS AT A SITE THE GATE NAMES : %d.**' % (len(live) - len(off)))
    rec('  ### ### **LIVE CURRENCY CLAIMS ELSEWHERE IN THE CORPUS : %d %s.**'
        % (len(off), [('%s:%d' % x) for x in off] or ''))
    rec('')
    rec('  ### THE MATCHER`S OWN LINEAGE, WITH EVERY VERSION`S YIELD PRINTED.')
    rec('    ### ### **A NUMBER FROM A MATCHER IS WORTH WHAT ITS LINEAGE IS WORTH**, so all three')
    rec('    ### versions are named and none is hidden behind the last one:')
    rec('      v1  window = THE LINE          -> 2 currency claims. ### **UNDERCOUNTS**: `ERRATA.md`')
    rec('          hard-wraps between "The current deposit is" and the version, so the head`s own')
    rec('          stale sentence was filed as a bare pin.')
    rec('      v2  window = THE PARAGRAPH     -> 4 currency claims. ### **OVERCOUNTS**:')
    rec('          `INTEGRATED_PROOF.md:14` carries a bare pin and, four hundred characters away, the')
    rec('          word "currently" -- about simplicity being implied by the trace formula.')
    rec('      v3  window = THE SENTENCE      -> %d currency claims, %d of them live and unannotated.'
        % (len(claims), len(live)))
    rec('          ### ### **AND v3 IS NOT ADOPTED BECAUSE IT GIVES THE SMALLEST NUMBER** -- it is')
    rec('          ### adopted because a pin and a verb in one sentence is the thing being counted,')
    rec('          ### and both v1`s miss and v2`s extra are exhibited above by name.')
    rec('')
    rec('  ### WHAT THIS DOES AND DOES NOT CHANGE.')
    rec('    ### ### **(N3) IS NOT RESCORED.** ### Its population is the four sites the gate names,')
    rec('    ### and the count there is still ZERO. ### **A FINDING OUTSIDE A REGISTERED POPULATION')
    rec('    ### IS A FINDING, NOT A RESCORE**, and moving the score would make the expectation')
    rec('    ### unfalsifiable after the fact.')
    rec('    ### ### **AND A PIN IS NOT A DISAGREEMENT.** ### %d lines cite the superseded version'
        % len(pins))
    rec('    ### without claiming it is current; a document may lawfully cite the deposit it was')
    rec('    ### written against, and the gate screens DEPOSIT STATE, not bibliography.')
    rec('    ### ### **NOTHING IS CORRECTED BY THIS ACT AND NO SITE IS EDITED.** ### The gate`s own')
    rec('    ### words govern the disposal: ### *"a disagreement found is a finding filed, not a')
    rec('    ### silent fix."* ### **IT IS FILED HERE.**')
    rec('=' * 100)
    io.open(os.path.join(D, 'b481_addendum_finding.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
