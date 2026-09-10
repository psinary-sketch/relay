# -*- coding: utf-8 -*-
"""b407_extract.py -- EXTRACT-TO-DISK. ### EVERY READ THIS ACT MAKES, PULLED BY THE ANCHOR TOOL.

### ### (A) Theorem 3.1's hypotheses and the definitions they rest on -- determined system,
###     interface, target parameter, transmission coefficient, FACTORING THROUGH -- plus the
###     sentence in which the record asserts `kappa = 0` at the corpus's OWN object, Corollary 3.6,
###     and the document's own TIER-1 / TIER-2 scope line.
### ### (B) Row `U1`'s six sites, from the COMMITTED BLOB.
### ### (C) The clause anchor's constituent chain `K1`-`K8` and the E0 gate's halt.
### ### (D) The escape-kind's two values and the record's own examples of each.
### ### (E) `(R20)`'s three limbs and the `SIDE-kernel` question `b392` left standing.
### ### (F) `run_clock`'s own docstring, for the stale-record guard.
### ### (G) The spectral-realization face at both its rows, and the mechanism classes'
###     exhaustiveness sentence.
###
### ### **EVERY WRITE ENCODES BEFORE IT OPENS** (b405), AND ### **NOTHING THIS TOOL WRITES IS EVER
### ### SEARCHED BY A LATER REPAIR** (b406) -- this act makes no in-place repair at all.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b407_extract.txt')
SCRATCH = os.path.join(D, '_b407')
PP = r'D:\MY-DOwnloads\PLACE-papers'
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
DK = os.path.join(PP, 'phase1.5', 'method', 'THE_DIFFICULTY_KINDS.md')
MC = os.path.join(PP, 'day1', 'Seven_Mechanism_Classes.md')
FIND = os.path.join(PP, 'FINDINGS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def write_text(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND** (b405's zero-byte husk)."""
    data = text.encode('utf-8')
    io.open(path, 'wb').write(data)
    return len(data)


def pull(path, hint, label, span=False, width=520):
    try:
        if span:
            ln0, run = AF.find_span(path, hint)
            txt = '\n'.join(run)
        else:
            ln0, txt = AF.find(path, hint)
    except AF.AnchorError as e:
        MISS.append(label)
        say('  ### ANCHOR MISS -- %s' % label)
        say('      hint : %r' % hint)
        say('      %s' % str(e).splitlines()[0][:190])
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln0))
    for ln in txt.splitlines():
        for k in range(0, max(len(ln), 1), width):
            say('      | %s' % ln[k:k + width])
    return txt


def main():
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    say('=' * 100)
    say('b407_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.')
    say('=' * 100)
    ok = AF.self_test(verbose=False)
    say('  anchor tool self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        return 2

    # -------------------------------------------------------------- (A) THE LEMMA
    say()
    say('-' * 100)
    say('### (A) THEOREM 3.1, ITS HYPOTHESES, AND THE DEFINITIONS THEY REST ON.')
    say('-' * 100)
    pull(IB, '**Definition 2.1 (Determined system).**', 'DEF 2.1 -- DETERMINED SYSTEM')
    pull(IB, "The programme's examples include", 'AND ITS EXAMPLES, INCLUDING THE CORPUS`S OBJECT')
    say()
    pull(IB, '**Definition 2.2 (Interface).**', 'DEF 2.2 -- INTERFACE, AND WHAT MAKES ONE ESSENTIAL')
    pull(IB, '**Definition 2.3 (Target parameter).**', 'DEF 2.3 -- TARGET PARAMETER')
    pull(IB, 'For M = \u03be(s): I can be the product formula',
         'AND THE RECORD`S OWN INSTANCE, NAMED IN ITS OWN EXAMPLES')
    say()
    pull(IB, '**Definition 2.4 (Transmission coefficient).**', 'DEF 2.4 -- THE COEFFICIENT')
    pull(IB, '\u03ba = 0 indicates I is *P-dark*', 'AND WHAT `kappa = 0` MEANS')
    say()
    pull(IB, '**Definition 2.5 (Factoring through an interface).**', 'DEF 2.5 -- THE CENTRAL NOTION')
    pull(IB, 'The sentences mentioned in \u03c0_j', 'ITS FIRST CLAUSE -- WHAT A FACTORING STEP MAY '
                                                    'REFERENCE')
    pull(IB, '**Proof \u03c0 factors through I for P** if every inference step',
         'AND WHAT IT TAKES FOR A WHOLE PROOF TO FACTOR')
    say()
    pull(IB, '**Theorem 3.1 (Sieve Ceiling Lemma).**', 'THEOREM 3.1, HYPOTHESES AND CONCLUSION')
    pull(IB, 'That is: \u03c0 can establish', 'AND WHAT IT SAYS THE REACH IS')
    say()
    pull(IB, 'Let I be the product-formula interface',
         '### **THE RECORD ASSERTS `kappa = 0` AT ITS OWN OBJECT** -- Prop 3.5`s setup')
    say()
    pull(IB, '**Corollary 3.6 (Bright-interface access).**', 'COROLLARY 3.6 -- THE REPAIR')
    pull(IB, 'any proof of universality must contain at least one inference step',
         'AND THE NAME, WITH WHAT THE CHANNELS ARE SAID TO BE')
    say()
    pull(IB, 'the **Tier-1** form of the barrier',
         '### **AND THE DOCUMENT`S OWN SCOPE LINE: TIER 1 IS CLAIMED, TIER 2 IS NOT**')

    # -------------------------------------------------------------- (B) THE SIX SITES
    say()
    say('-' * 100)
    say('### (B) ROW `U1`\u2019S SIX SITES, FROM THE COMMITTED BLOB.')
    say('-' * 100)
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                          capture_output=True).stdout.decode('utf-8')
    row = [x for x in blob.split('\n') if x.startswith('| U1 |')]
    assert len(row) == 1
    c5 = row[0].rstrip().split('|')[5]
    write_text(os.path.join(SCRATCH, 'U1_row_at_HEAD.txt'), row[0])
    say('    row U1 at HEAD : %d bytes ; cell 5 : %d bytes'
        % (len(row[0].encode('utf-8')), len(c5.encode('utf-8'))))
    tags = ['**(i) ', '**(ii) ', '**(iii) ', '**(iv) ', '**(v) ', '**(vi) ']
    offs = [(t, c5.find(t)) for t in tags]
    for k, (tag, at) in enumerate(offs):
        end = offs[k + 1][1] if k + 1 < len(offs) else c5.find('**`(i)` \u2014 KIND')
        seg = c5[at:end if end > at else at + 900]
        say('  ### %s   [cell 5 offset %d, %d bytes]'
            % (tag.strip('* '), at, len(seg.encode('utf-8'))))
        for j in range(0, min(len(seg), 1800), 150):
            say('      | %s' % seg[j:j + 150])
        say('      ---')

    # -------------------------------------------------------------- (C) THE CHAIN
    say()
    say('-' * 100)
    say("### (C) THE CLAUSE ANCHOR'S CONSTITUENT CHAIN, AND THE E0 GATE'S HALT.")
    say('-' * 100)
    # ### **THE `K`-ROWS APPEAR IN THREE TABLES AND A PER-ROW ANCHOR IS AMBIGUOUS IN ALL THREE.**
    # ### ### **AN ANCHOR THAT MATCHES TWICE ANCHORS NOTHING**, so the E0 gate's table is located
    # ### by ITS OWN HEADING and its eight rows are taken in file order from there -- which also
    # ### proves the rows read are the GATE's and not the grade table's or the census's.
    head = pull(FIND, '### The E0 gate: every constituent unfolded to its owner',
                'THE E0 GATE, LOCATED BY ITS OWN HEADING')
    src = io.open(FIND, encoding='utf-8').read().split(chr(10))
    i0 = src.index(head.rstrip(chr(10)))
    rows = [(n + 1, x) for n, x in enumerate(src[i0:i0 + 20], start=i0)
            if x.startswith('| **K')][:8]
    say('  ### ITS EIGHT CONSTITUENT ROWS, IN FILE ORDER FROM THAT HEADING:')
    for n, x in rows:
        say('  ### line %d' % n)
        for j in range(0, min(len(x), 1600), 150):
            say('      | %s' % x[j:j + 150])
    if len(rows) != 8:
        MISS.append('THE E0 GATE TABLE (%d rows found, 8 expected)' % len(rows))
    say()
    pull(FIND, "**The gate\u2019s verdict: it halts at K8.**", 'THE HALT, IN THE GATE`S OWN WORDS')
    pull(FIND, '**The places sum, unfolded as the arc realized it**',
         'AND THE CHAIN AS ONE SENTENCE')

    # -------------------------------------------------------------- (D) THE ESCAPE-KIND
    say()
    say('-' * 100)
    say("### (D) THE ESCAPE-KIND'S TWO VALUES, AND THE RECORD'S OWN EXAMPLES OF EACH.")
    say('-' * 100)
    pull(DK, "classifies *why* finite certificates don", 'THE CLASSIFICATION')
    pull(DK, 'TWO escape-kinds suffice', 'THE TWO VALUES, WITH THE RECORD`S OWN EXAMPLES')

    # -------------------------------------------------------------- (E) (R20)
    say()
    say('-' * 100)
    say("### (E) `(R20)`'S LIMBS, AND THE `SIDE-kernel` QUESTION IT LEFT STANDING.")
    say('-' * 100)
    pull(TRAILS, 'THE DEPOSIT RULE, WRITTEN, WITH A CURRENCY OBLIGATION', '(R20), WHOLE')
    say()
    b392 = os.path.join(D, 'b392_closing.txt')
    pull(b392, '`SIDE-kernel` as a deposit line with no current citable record',
         'THE `SIDE-kernel` QUESTION, IN b392`S OWN WORDS', span=True)
    pull(b392, 'CANDIDATE C -- THE TWO RECORDS, AND THE `SIDE-kernel` QUESTION',
         'AND WHERE b392 FILED IT', span=True)

    # -------------------------------------------------------------- (F) run_clock
    say()
    say('-' * 100)
    say('### (F) `run_clock`, FOR THE STALE-RECORD GUARD.')
    say('-' * 100)
    rc = os.path.join(ROOT, 'tools', 'run_clock.py')
    pull(rc, 'WRITE `lines` to the next free path for `stem`',
         '### **THE WRITER ALREADY STAMPS: THE CLOCK IS THE FIRST LINE**')
    pull(rc, 'NO RUN FILE IS EVER OVERWRITTEN BY THIS TOOL', 'AND IT VERSIONS RATHER THAN OVERWRITES')
    say('    ### ### **SO THE STAMP EXISTS AND ONLY THE READER WAS MISSING** -- which is exactly')
    say('    ### what `b406` was bitten by, and exactly what the guard has to supply.')

    # -------------------------------------------------------------- (G) THE FACE
    say()
    say('-' * 100)
    say('### (G) THE SPECTRAL-REALIZATION FACE, AT BOTH ITS ROWS, AND THE EXHAUSTIVENESS SENTENCE.')
    say('-' * 100)
    led = os.path.join(PP, 'FACES_LEDGER.md')
    for rid in ('| R5 |', '| **F4**'):
        line = [x for x in blob.split('\n') if x.startswith(rid)]
        if not line:
            MISS.append('LEDGER ROW %s' % rid)
            say('  ### ROW MISS -- %s' % rid)
            continue
        cells = line[0].rstrip().split('|')
        say('  ### THE ROW %s, CELL BY CELL   [%d cells]' % (rid.strip('| *'), len(cells) - 2))
        for k, c in enumerate(cells):
            if not c.strip() or k in (0, len(cells) - 1):
                continue
            say('      -- cell %d --' % k)
            for j in range(0, min(len(c), 1500), 150):
                say('      | %s' % c[j:j + 150])
        say('      ---')
    say()
    pull(MC, '**Class C\u2085 (multiplicative).**', 'THE MECHANISM CLASS THE FACE BELONGS TO')
    pull(MC, 'every derivation chain from \u03b8 to a zero-location constraint factors through',
         '### **AND THE EXHAUSTIVENESS SENTENCE: NO FOURTH SOURCE**')

    say()
    say('=' * 100)
    say('  ### ### **ANCHOR MISSES : %d** %s' % (len(MISS), MISS or ''))
    say('  ### **NOTHING IS WRITTEN TO ANY LEDGER, BANK, ROW, KEY OR STANDING FILE BY THIS TOOL.**')
    say('=' * 100)
    write_text(OUT, '\n'.join(L) + '\n')
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
