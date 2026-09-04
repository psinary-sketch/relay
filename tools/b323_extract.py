# -*- coding: utf-8 -*-
"""b323_extract.py -- THE EXTRACT STEP FOR A FILINGS ACT. ### **NINE ACTS, READ AT THEIR OWN FILES.**

### ### **A FOLD READS NOTHING BUT THE RECORD, AND THAT IS WHAT MAKES ITS READING RULE STRICT.**
### There is no artefact to pin here and no PDF to page in. ### **THE HAZARD IS THE OPPOSITE ONE:**
### a fold summarises nine acts, and the cheapest way to write it is from memory of having written
### them. ### **b283's LAW IS THE ANSWER AND IT IS MECHANICAL: ### A NEEDLE IS PULLED FROM THE FILE
### ### THAT EMITTED THE SENTENCE, NEVER FROM A FILE THAT QUOTES IT** -- and for this act every
### sentence's emitter is a different act's bank.

### ### ### **THIS FILE IS NOT THE GATE.** ### It records the reads. ### The gate is `F-QUOTE` in
### `b323_fold.py`, which checks every quotation against ### **THE ACT THAT ORIGINATED IT** ### and
### which ### **GENERATES** ### the markdown rather than checking it afterwards. ### b314's own
### sentence, carried: ### *"A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE; ONE
### THAT GENERATES THE WRITING CANNOT EMIT ONE."*
### ### **SO A QUOTATION THAT FAILS `F-QUOTE` NEVER REACHES `FINDINGS.md` AT ALL**, and this file
### exists so that the reads are on disk before the generator runs, not instead of it.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b323_extract_notes.txt')

# ### **THE NINE ACTS AND THEIR OWN BANKS.** ### The bank is the act's own voice; a run file is its
# ### tool's, and a correspondence row is the table's. ### **THE FOLD READS THE BANK.**
BANKS = [
    ('b314', 'b314_the_fold_and_the_cold_clone.txt', 'THE FOLD AND THE COLD CLONE'),
    ('b315', 'b315_the_calibration_and_the_rate.txt', 'THE CALIBRATION AND THE RATE'),
    ('b316', 'b316_the_archimedean_instrument.txt', 'THE ARCHIMEDEAN INSTRUMENT'),
    ('b317', 'b317_the_trace_on_the_object.txt', 'THE TRACE ON THE OBJECT'),
    ('b318', 'b318_the_forced_sign.txt', 'THE FORCED SIGN'),
    ('b319', 'b319_the_stable_rank.txt', 'THE STABLE RANK'),
    ('b320', 'b320_the_lawful_function.txt', 'THE LAWFUL FUNCTION AND THE CONTROL'),
    ('b321', 'b321_the_window_opened.txt', 'THE WINDOW OPENED'),
    ('b322', 'b322_the_membership.txt', 'THE MEMBERSHIP'),
]

# ### **THE SENTENCES THIS ACT INTENDS TO CARRY, EACH WITH THE ACT THAT MUST OWN IT.** ### The
# ### extract prints the WHOLE LINE each sits on, with its line number, so the fold's quotation can
# ### be read in its own context before it is lifted out of it.
WANTED = [
    ('b314', 'BYTE-FOR-BYTE EQUAL TO THE BANKED BLOB'),
    ('b314', 'MODULES SIT OUTSIDE THE CERTIFICATION FILE, ALL 25 ELABORATE, AND 91'),
    ('b315', 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    ('b315', "UNDER THE SOURCE'S EXPONENT THE ENVELOPE BECOMES A CONSTANT"),
    ('b315', 'AT THE SAME LEADING ORDER'),
    ('b316', 'THE INSTRUMENT EXISTS'),
    ('b316', "b300's MEMBERSHIP IS NOT CONFIRMED"),
    ('b316', 'ALL of its mass outside the space, at every truncation'),
    ('b317', 'THE NUMBER EXISTS'),
    ('b317', 'A NUMBER THAT LANDS WHERE A BROKEN CHAIN SAID'),
    ('b317', 'removes'),
    ('b318', 'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT'),
    ('b318', "THE CORPUS'S WINDOW IS A CANDIDATE"),
    ('b319', 'THE KERNEL-COVERAGE DEFECT IS DISCHARGED'),
    ('b319', 'THE BAR THIS ACT SEALED IS DEFECTIVE'),
    ('b319', 'THE CUT SITS INSIDE A REAL SPECTRAL SEPARATION'),
    ('b320', '27 OF 27 FRAMES'),
    ('b320', "FIRST REPORTED VERDICT WAS `FAILS`"),
    ('b321', 'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER'),
    ('b321', 'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE'),
    ('b321', 'AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES'),
    ('b322', 'THE RESIDUAL FALLS, AT EVERY STEP OF THE DOMAIN LADDER'),
    ('b322', "SO THE VERDICT IS `UNDER-RESOLVED`, AND IT CARRIES ITS PRICE"),
    ('b322', 'DICHOTOMY IS NOT A PARTITION'),
    ('b322', 'THE ACT TAKES THE WEAKER OF THE TWO'),
]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b323_extract.py -- THE EXTRACT STEP. ### **NINE ACTS, EACH READ AT ITS OWN BANK.**')
    rec('=' * 100)
    rec('  ### **b283\'s LAW, MECHANICAL HERE:** ### every sentence below is read at the act that')
    rec('  ### EMITTED it. ### **A QUOTATION OF A QUOTATION IS NOT A SOURCE**, and for a fold the')
    rec('  ### temptation is to write from memory of having written the acts.')
    rec('')

    text = {}
    missing_files = 0
    rec('-' * 100)
    rec('### (A) THE NINE BANKS, WITH THEIR SIZES.')
    rec('-' * 100)
    rec('    %-6s %-46s %-10s %-8s' % ('act', 'bank', 'bytes', 'lines'))
    for act, fn, _title in BANKS:
        p = os.path.join(D, fn)
        if not os.path.exists(p):
            missing_files += 1
            rec('    %-6s %-46s ### **NOT PRESENT**' % (act, fn))
            continue
        t = io.open(p, encoding='utf-8', errors='replace').read()
        text[act] = t
        rec('    %-6s %-46s %-10d %-8d' % (act, fn, len(t.encode('utf-8')), len(t.splitlines())))
    rec('    ### ### **BANKS NOT PRESENT : %d**' % missing_files)

    rec('')
    rec('-' * 100)
    rec('### (B) THE SENTENCES, EACH IN THE WHOLE LINE IT SITS ON, AT ITS OWN ACT.')
    rec('-' * 100)
    missing = 0
    for act, frag in WANTED:
        t = text.get(act, '')
        hits = [(i + 1, ln) for i, ln in enumerate(t.splitlines()) if frag in ln]
        rec('')
        rec('### ==== %s | %r' % (act, frag))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND IN %s**' % act)
            continue
        for n, ln in hits[:3]:
            rec('    | line %-5d %s' % (n, ln))
        if len(hits) > 3:
            rec('    | ### ... and %d further occurrence(s) in the same act' % (len(hits) - 3))
    rec('')
    rec('  ### ### **SENTENCES NOT FOUND AT THEIR OWN ACT : %d**' % missing)

    rec('')
    rec('-' * 100)
    rec('### (C) THE NO-GRADE-MOVED BASELINE, TAKEN BEFORE ANYTHING IS WRITTEN.')
    rec('-' * 100)
    rec('  ### **A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD.** ### The check that it moved no')
    rec('  ### grade cannot be a promise; it is the git blob of `FINDINGS.md` before the append')
    rec('  ### against the file after it, and `b323_fold.py` runs it as a TRUE-PREFIX test.')
    fp = os.path.join(r'D:\MY-DOwnloads\PLACE-papers', 'FINDINGS.md')
    if os.path.exists(fp):
        cur = io.open(fp, encoding='utf-8', errors='replace').read()
        rec('  FINDINGS.md before this act : %d bytes, %d lines'
            % (len(cur.encode('utf-8')), len(cur.splitlines())))
        heads = [ln for ln in cur.splitlines() if ln.startswith('## ')]
        rec('  sections present before the append : %d' % len(heads))
        for h in heads[-4:]:
            rec('      %s' % h[:96])
    else:
        rec('  ### **FINDINGS.md NOT PRESENT -- HARD FAILURE**')
        missing += 1
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return 0 if not (missing or missing_files) else 5


if __name__ == '__main__':
    sys.exit(main())
