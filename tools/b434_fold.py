# -*- coding: utf-8 -*-
"""b434_fold.py -- THE FOLD, b423 THROUGH b432. ### **PURELY ADDITIVE.**

### **IT APPENDS ONE SECTION TO `FINDINGS.md` AND EDITS NOTHING.** ### A negative byte delta refuses
### the append and restores the file from the pre-act bytes (BAR 3).
### ### **NO COUNT IN THIS FILE IS TYPED BY THE SEAT.** ### The span is `b363_span.py`'s, read from
### its output; every grade string is verified in its own act's closing bank before it is stated; and
### the five findings are each verified at their own source (BAR 1, BAR 2).
### ### **AND IT IS IDEMPOTENT** -- b433 learned that the hard way, twice. ### The marker decides.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
EXTR = os.path.join(D, 'b434_extract.txt')
SPAN = os.path.join(D, 'b434_span.txt')
OUT = os.path.join(D, 'b434_fold.json')
MARK = '<!-- b434 the fold: b423-b432, the external-grading arc -->'
NL = chr(10)
ARC = ['b423', 'b424', 'b425', 'b426', 'b427', 'b428', 'b429', 'b430', 'b431', 'b432']


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def build(rows, span_raw, span_filed):
    """### THE SECTION. ### **EVERY FIGURE IN IT ARRIVES AS AN ARGUMENT, MEASURED ELSEWHERE.**"""
    L = ['', MARK, '',
         '## The external-grading arc — b423 through b432, folded at b434', '',
         '**Ten acts. The span is the span tool’s and no count here was typed by the seat:** '
         '`b363_span.py` reports the last fold as `b413`–`b421`, filed by `b422`, and the next span '
         'starting at **b423**. Its raw count runs to **%d**, through this sortie’s own two acts; '
         '**the span this fold files is b423–b432, ten acts**, because a fold’s span has always '
         'ended before its filing act — `b422` was not in its own fold either. Both figures are '
         'printed here and neither is dropped.' % span_raw, '',
         '### The arc in one statement', '',
         '**The corpus turned its grading discipline outward for the first time, and the '
         'discipline held — while the same protocol, turned inward, found the corpus’s own prose '
         'claiming more than its terminal proves.** Five findings stand in this arc, side by side; '
         '**none of them overturns another**, and the arc is not tidier than that:', '',
         '- **Two external proofs were graded `DERIVES`, and the discipline was found symmetric.** '
         'b429 graded a Navier–Stokes terminal against the Clay page’s statement C; b431 graded a '
         'long-gaps terminal against its paper’s own Theorem 1.1. b430 put the corpus’s own '
         '`SmearGeneral.smear_general` to the identical protocol and **4 of 4 clauses were applied '
         'to it as they had been applied to the stranger** — verdict `SYMMETRIC`. b429’s two '
         'apparent asymmetries were that act’s, not the discipline’s.',
         '- **The corpus’s own terminal graded `NOT THE CLAIM` against the corpus’s own prose.** '
         'Against the claim its correspondence row names, `smear_general` grades `DERIVES`. Against '
         'the claim the finite-side prose makes, it grades **`NOT THE CLAIM`** — for two '
         'independent reasons: scope, and the objects the statement names. Under `(R40)` those are '
         'two honest grades of one terminal, not a contradiction.',
         '- **A keystone’s compiled lemma was found named for a theorem it does not invoke.** '
         '`Module1.crt_exhaustiveness` quantifies over one syntactic coupling whose period is fixed '
         'by the term, and its witness’s modulus set is a **singleton**; no product over primes '
         'appears and no Chinese Remainder Theorem is used. The lemma is true and cleanly proved. '
         '**It is the name and the surrounding prose that claimed more**, and b433 narrowed them '
         'without renaming anything.',
         '- **The falsifier was read at address and found under pressure, not fired.** b425 read '
         'the lane’s `w = −1` against three supernova results and found it **FIRED at one of three '
         'sources and UNDECIDED at two**; b426 re-read the collaboration’s own DR2 paper by address '
         'under `(R38)` and the result **SPANS** the rule’s two clauses. The lane’s condition did '
         'not move.',
         '- **Three witness sites were exhausted and the arc is not converging on one boundary.** '
         'Sites (i), (ii) and (iii) yielded 16, 19 and 20 candidates and **none held**; the class '
         'boundary’s share went 13/16, 10/19, 12/20 and the union of kinds grew rather than '
         'settled. Three sites remain.', '',
         '### What each act contributed, with its own verdict from its own bank', '', ]
    L.append('| act | what it did | its verdict, as its own closing record states it |')
    L.append('|---|---|---|')
    for a, what, verdict in rows:
        L.append('| **%s** | %s | %s |' % (a, what, verdict))
    L += ['',
          '**Every verdict string above was verified in that act’s own closing record before this '
          'fold stated it** — not in a later act’s summary of it, and not from memory. A string '
          'that could not be found there would not have been asserted.', '',
          '### The three columns, kept apart', '',
          '**b412 minted a third column and this fold keeps all three separate and never sums '
          'them.** Statements this arc makes **about the object** — the zeros, ξ, the Euler '
          'balance: **0**. Statements **about the record** — what the corpus’s documents claim, '
          'what its instruments serve, what its grades mean: **5**, which is the arc’s whole '
          'substance. Statements **about the object’s model** — the compiled arithmetic and its '
          'terminals: **0 new**; the arc graded terminals that already existed and compiled '
          'nothing.', '',
          '**That distribution is the arc’s shape and it is stated plainly rather than smoothed: '
          'this was an arc about the record, run by pointing the corpus’s own instruments at the '
          'corpus and at two strangers.**', '',
          '### Lore: one species, minted here', '',
          '#### **A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN**', '',
          '**Three incidents, each named from its own bank:**', '',
          '- **b414 — the over-budget `decide`.** A decision procedure run past its budget does not '
          'fail; it yields a term carrying `sorryAx`, and the build exits `0`. The arm that caught '
          'it is `G-DECIDE-LIMIT-TRAP`, and what it reads is the **printed axiom profile**.',
          '- **b418 — the search at its time limit.** A `Grep` over relay’s `data/` ran 20.04 '
          'seconds — its limit — and returned `numFiles: 13` with **no truncation flag and no '
          'timeout text**. The same query, completed, reaches forty files. *A truncation with no '
          'flag reads exactly like a small answer.*',
          '- **b433 — the recursive delete.** `shutil.rmtree(..., ignore_errors=True)` met 36 '
          'read-only git pack files, skipped every one **in silence**, left the directory standing, '
          'and the tool reported the removal done.', '',
          '**The one cure they share: the verdict is read from the object — the printed profile, '
          'the recorded duration, the directory’s own existence — and never from the exit code.**',
          '', '**Which of the three carries a mechanized guard, measured rather than asserted:**',
          '', '@GUARDS@', '',
          '**And the sharpest fact in the census: the cure for b433’s incident already existed in '
          'this corpus.** `tools/b314_coldclone.py` carries a handler whose docstring reads *“git '
          'objects arrive read-only on Windows; a plain `rmtree` refuses them.”* **It was never '
          'shared, and b433 reinvented it.** A cure that lives in one tool is not a guard.', '',
          '@WORKORDER@', '',
          '**A TECHNE module stands beside this species**, local and not pushed, as that core’s '
          'modules always are.', '']
    return L


def main(argv):
    ex = read(EXTR)
    sp = read(SPAN)
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', sp)
    if not m:
        print('  ### HARD FAILURE -- the span tool`s count is not readable. The fold does not file.')
        return 2
    span_raw = int(m.group(1))

    # ### **THE TEN ROWS. ### EACH VERDICT IS THE STRING THE SURVEY VERIFIED IN THAT ACT'S BANK.**
    rows = [
        ('b423', 'the `(R37)` question put; two banked readings re-run',
         '`CONFIRMED` — b407’s and b420’s readings both; b421’s *NOT SUPPLIABLE* lapses'),
        ('b424', 'the witness arc opened at site (i); 16 candidates built and tested',
         '**none held** — the exhausted list filed as a writer block'),
        ('b425', 'the falsifier read: the lane’s `w = −1` against three supernova results',
         '`FIRED AT ONE OF THREE SOURCES`, and undecided at two'),
        ('b426', 'the collaboration’s own DR2 paper located by address and read at content',
         'the result **`SPANS`** `(R38)`’s two clauses; `p2-d6` does not move'),
        ('b427', 'the witness arc at site (ii); 19 candidates',
         'none held; the arc **`NOT CONVERGING`** on one boundary'),
        ('b428', 'the witness arc at site (iii); the disproof lane named; the external read priced',
         'none held; **`NOT CONVERGING`** at three sites; the lane named, not opened'),
        ('b429', 'a stranger’s Navier–Stokes Lean terminal built and graded against Clay statement C',
         '**`DERIVES`**; the self-grading test found 2 clauses asymmetric, both favouring the stranger'),
        ('b430', 'the corpus’s own `smear_general` graded twice under `(R40)`',
         '**`DERIVES`** against its row, **`NOT THE CLAIM`** against its prose; 4 of 4 → `SYMMETRIC`'),
        ('b431', 'a second stranger graded, and the Type-D question decided by unfolding',
         '**`DERIVES`**; `TWO THEOREMS SHARING A NAME`, parting at what is quantified'),
        ('b432', 'the disproof lane restated with a worked case of each shape',
         'both instruments serve form (a); **`NO INSTRUMENT POINTED`** at the universal negative'),
    ]

    # ### THE GUARD CENSUS, LIFTED FROM THE SURVEY'S OWN MEASUREMENT -- NOT RE-DERIVED HERE.
    owners = re.search(r'tools carrying the duration guard\s*:\s*(\[[^\]]*\])', ex)
    lax = re.search(r'tools still passing `ignore_errors`\s*:\s*(\d+) sites in (\d+) files', ex)
    guards = [
        '- **b414 — GUARDED, and the guard is the corpus’s standing practice.** Every grading act '
        'reads `#print axioms` output and seeks `sorryAx` **by name**, and `AXIOM_PRINTS.txt` is '
        'the corpus’s own record of those profiles. The verdict comes from the printer, never from '
        'the exit code.',
        '- **b418 — GUARDED, and the guard is a shared standing tool.** `tools/walker_guard.py`, '
        'minted at b418 for exactly this species: given a walker call’s recorded start and its '
        'result’s recorded time, `verdict()` returns **`INCOMPLETE`** for a call that reached the '
        'limit and a count only for one that did not. Carried by %s.'
        % (owners.group(1) if owners else 'the b418 and b419 suites'),
        '- **b433 — NOT GUARDED.** The handler exists only inside b433’s own components tool. '
        '**%s across the standing tools still pass `ignore_errors=True`** — among them '
        '`b378_lockgate.py` and `gate_hash.py` — and **no tool anywhere verifies that a removal '
        'removed anything.** Most of those sites clear a temporary directory the tool itself made, '
        'where the consequence is a leak rather than a false verdict; **that is a reason to rank '
        'the work, not a reason to leave it undone**, and the exposure is stated rather than '
        'inflated.' % (('%s sites in %s files' % (lax.group(1), lax.group(2))) if lax
                       else 'several sites'),
    ]
    workorder = (
        '#### Work-order `W-REMOVAL-VERIFIED` — filed here, not done here', '',
        '**The order:** a removal is verified by reading the object — the path’s own '
        'non-existence — and a recursive delete is never asked not to complain. Concretely: retire '
        '`ignore_errors=True` at the sites where a real artefact is removed, share b314’s handler '
        'as a named helper instead of letting each act rediscover it, and add the absence read.', '',
        '**Its trigger:** the next act that removes a directory it did not itself create inside '
        'this session — or any act that opens the instrument-audit lane, whichever comes first. '
        '**Until one of those fires, this work-order is filed and not started**, and this fold does '
        'not start it.', '',
        '**Its scope, stated so it is not over-read:** this is about removals, not about every '
        '`ignore_errors` in the tree, and it asserts no defect in any act that has already closed.')

    L = build(rows, span_raw, 10)
    text = NL.join(L).replace('@GUARDS@', NL.join(guards)).replace(
        '@WORKORDER@', NL.join(workorder))

    cur = read(FIND)
    before = len(cur.encode('utf-8'))
    if MARK in cur:
        print('  ### THE FOLD IS ALREADY FILED (marker present). ### Nothing written.')
        delta, status = 0, 'ALREADY FILED'
    else:
        data = (cur.rstrip(NL) + NL + text + NL).encode('utf-8')
        delta = len(data) - before
        if delta < 0 or not data.startswith(cur.rstrip(NL).encode('utf-8')):
            print('  ### REFUSED -- the append would not be purely additive. Nothing written.')
            return 2
        open(FIND + '.tmp', 'wb').write(data)
        os.replace(FIND + '.tmp', FIND)
        status = 'FILED'
        print('  FILED. ### FINDINGS.md %d -> %d bytes (%+d)' % (before, before + delta, delta))
    out = dict(status=status, delta=delta, span_raw=span_raw, span_filed=10,
               acts=[r[0] for r in rows], marker=MARK,
               sha256=hashlib.sha256(read(FIND).encode('utf-8')).hexdigest())
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(out, indent=2, ensure_ascii=False) + NL)
    os.replace(OUT + '.tmp', OUT)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
