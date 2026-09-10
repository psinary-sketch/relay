# -*- coding: utf-8 -*-
"""b405_extract.py -- EXTRACT-TO-DISK. ### EVERY READ THIS ACT MAKES, PULLED BY THE ANCHOR TOOL
### AND WRITTEN TO A FILE BEFORE ONE WORD OF THE ACT IS TYPED.

### ### **WHAT IT PULLS.**
### ### (A) The compiled countermodel and its closed half, at the pin the corpus cites -- statement
###     whole, from the file as `git show` hands it back at `v0.10.0`, NOT from the working tree.
### ### (B) Its axiom profile, from a PRINTED profile in the repository's own tracked transcript.
### ### (C) The finite side's terminal, its cell list, and the theorem that carries the zero.
### ### (D) Row `U1` whole, from the COMMITTED BLOB, split into its seven cells by the column law.
### ### (E) The emitting banks the row names, at the sentences the row quotes from them.
### ### (F) The ledger's COLUMN LAW, because a row cannot gain a column alone.
###
### ### **WHAT IT DOES NOT DO.** ### It builds nothing, runs no kernel, and reads no working tree
### where a pin exists. ### **A FILE AT A PIN IS READ AT THE PIN.**
###
### ### **AND ONE DEFECT THIS FILE ITSELF SUFFERED, RECORDED IN ITS OWN HEADER.** ### A patch script
### ### opened this file `'w'` and then hit an encode error mid-write. ### **`open(..., 'w')`
### ### TRUNCATES BEFORE IT ENCODES**, so the failure left a ZERO-BYTE HUSK where the tool had been
### ### -- the species `b328` banked for `json.dump`, recurring on a plain text write. ### The cure
### ### is the same one and it is used for every write below: ### **ENCODE FIRST, WRITE BYTES.**
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402

OUT = os.path.join(ROOT, 'data', 'b405_extract.txt')
SCRATCH = os.path.join(ROOT, 'data', '_b405')

LV = r'D:\SIDE-lv-conservation'
GS = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
PIN_TAG = 'v0.10.0'

LINES = []


def say(s=''):
    LINES.append(s)
    print(s)


def write_text(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.** ### See the header."""
    data = text.encode('utf-8')
    io.open(path, 'wb').write(data)
    return len(data)


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError('git %s in %s : %s' % (args, repo, r.stderr[:200]))
    return r.stdout


def materialise(repo, ref, path, name):
    """### **A FILE AT A PIN IS READ AT THE PIN.** ### `git show` to disk, then anchor on THAT."""
    blob = git(repo, 'show', '%s:%s' % (ref, path))
    dst = os.path.join(SCRATCH, name)
    io.open(dst, 'wb').write(blob)
    say('    materialised  : %s  <-  %s@%s:%s  (%d bytes)'
        % (name, os.path.basename(repo), ref, path, len(blob)))
    return dst


def pull(path, hint, label, span=False):
    """### Pull one quotation BY THE TOOL. ### A miss RAISES and is reported as a miss."""
    try:
        if span:
            ln0, run = AF.find_span(path, hint)
            txt = '\n'.join(run)
        else:
            ln0, txt = AF.find(path, hint)
    except AF.AnchorError as e:
        say('  ### ANCHOR MISS -- %s' % label)
        say('      hint : %r' % hint)
        say('      %s' % str(e).splitlines()[0][:200])
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln0))
    for ln in txt.splitlines():
        say('      | %s' % ln)
    return txt


def block(path, first_hint, last_hint, label):
    """### Pull a RUN of lines between two anchors, BOTH found by the tool."""
    try:
        i, _a = AF.find(path, first_hint)
        j, _b = AF.find(path, last_hint)
    except AF.AnchorError as e:
        say('  ### BLOCK MISS -- %s' % label)
        say('      %s' % str(e).splitlines()[0][:200])
        return None
    src = io.open(path, encoding='utf-8').read().splitlines()
    if j < i:
        say('  ### BLOCK MISS -- %s : the end anchor precedes the start (%d < %d)' % (label, j, i))
        return None
    say('  ### %s   [lines %d..%d of %s]' % (label, i, j, os.path.basename(path)))
    for ln in src[i - 1:j]:
        say('      | %s' % ln)
    return '\n'.join(src[i - 1:j])


def main():
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    say('=' * 100)
    say('b405_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.')
    say('=' * 100)

    ok = AF.self_test(verbose=False)
    say('  anchor tool self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        say('  ### REFUSING TO QUOTE THROUGH A TOOL THAT FAILS ITS OWN FIXTURES.')
        return 2

    # ------------------------------------------------------------------ (A) THE PIN
    say()
    say('-' * 100)
    say('### (A) THE COMPILED COUNTERMODEL, AT THE PIN THE CORPUS CITES.')
    say('-' * 100)
    head = git(LV, 'rev-parse', 'HEAD').decode().strip()
    pin = git(LV, 'rev-parse', '%s^{}' % PIN_TAG).decode().strip()
    say('    repo          : SIDE-lv-conservation   ### NOT ON THE FOUR-REPO ROSTER')
    say('    working HEAD  : %s' % head)
    say('    %-13s : %s' % (PIN_TAG, pin))
    say('    ### **THE PIN IS THE REF THE PAPER CITES; THE WORKING HEAD IS %s.**'
        % ('THE SAME' if head == pin else 'AHEAD OF IT'))
    t3 = materialise(LV, PIN_TAG, 'SIDELvConservation/T3_StepNineBridge.lean', 'T3_at_pin.lean')
    say()
    pull(t3, 'theorem T3prime_shared_witness (\U0001d49e : Set Coupling) (s : \u2102) '
             '(h1 : \u2200 C \u2208 \U0001d49e, C Phi) (h2 : mellin Phi (s / 2) \u2260 0) : '
             '\u2203 \u03a6 : \u211d \u2192 \u2102, (\u2200 C \u2208 \U0001d49e, C \u03a6) \u2227 '
             'mellin \u03a6 (s / 2) \u2260 0 := \u27e8Phi, h1, h2\u27e9',
         "T3' -- THE CLOSED HALF, STATEMENT AND PROOF WHOLE", span=True)
    say()
    block(t3, 'theorem T3doubleprime_general_commutation_fails', 'let C2 : Coupling',
          "T3'' -- THE COUNTERMODEL, STATEMENT WHOLE AND ITS DATA")

    # ------------------------------------------------------------------ (B) THE PROFILE
    say()
    say('-' * 100)
    say('### (B) ITS AXIOM PROFILE, FROM A PRINTED PROFILE IN THE REPOSITORY ITSELF.')
    say('-' * 100)
    vt = materialise(LV, PIN_TAG, 'VERIFICATION_TRANSCRIPT.md',
                     'VERIFICATION_TRANSCRIPT_at_pin.md')
    say()
    block(vt, "'SIDELvConservation.T3.T3prime_shared_witness'",
          'Neither carries `sorryAx`', 'THE PRINTED PROFILE BLOCK -- BOTH TERMINALS')
    pull(vt, 'T3_StepNineBridge.lean:92:8: declaration uses',
         'THE ONE PINNED SORRY, WHERE IT SITS -- THE v0.2.0 ADDENDUM RUN')
    say()
    say('    ### **THE PROFILE IS PRINTED, NOT RUN HERE.** ### The transcript is a TRACKED file at')
    say('    ### the pin and its axiom block is the stdout of a `#print axioms` run the repository')
    say('    ### banked. ### **THE INSTRUMENT LANE IS PARKED AND NOTHING WAS BUILT.**')

    # ------------------------------------------------------------------ (C) THE FINITE SIDE
    say()
    say('-' * 100)
    say("### (C) THE FINITE SIDE'S TERMINAL, ITS CELL LIST, AND THE THEOREM CARRYING THE ZERO.")
    say('-' * 100)
    seal = os.path.join(GS, 'Core', 'FiniteSideSeal.lean')
    prints = os.path.join(GS, 'AXIOM_PRINTS.txt')
    say('    file          : %s' % seal)
    pull(seal, 'def cells : List (Nat', 'THE CELL LIST, WHOLE')
    say()
    block(seal, 'theorem finite_side_silence', 'fun hc => ?_\u27e9',
          'THE TERMINAL, STATEMENT WHOLE')
    say()
    block(seal, 'theorem compact_smear_vanishes_at_cells', 'sumAQ c.1 c.2) = true',
          'THE ZERO ITSELF -- THE SMEAR THEOREM, STATEMENT WHOLE')
    say()
    block(seal, '(a) GENERAL -- `t = u * p^j`',
          'with the cell list as the hypothesis, each cell decided',
          "THE DOCSTRING'S OWN LABELLING OF THE THREE CLAUSES")
    say()
    pull(prints, "'B329.finite_side_silence'", 'THE PRINTED PROFILE -- THE TERMINAL')
    pull(prints, "'B329.compact_smear_vanishes_at_cells'", 'THE PRINTED PROFILE -- THE ZERO')

    # ------------------------------------------------------------------ (D) ROW U1
    say()
    say('-' * 100)
    say('### (D) ROW `U1` WHOLE, FROM THE COMMITTED BLOB, BY THE COLUMN LAW.')
    say('-' * 100)
    led = materialise(PP, 'HEAD', 'FACES_LEDGER.md', 'FACES_LEDGER_at_HEAD.md')
    src = io.open(led, encoding='utf-8').read().splitlines()
    rows = [(i, l) for i, l in enumerate(src) if l.startswith('| U1 |')]
    if len(rows) != 1:
        say('  ### ROW MISS -- %d lines start `| U1 |`' % len(rows))
        return 2
    idx, row = rows[0]
    cells = row.rstrip().split('|')
    say('    row line      : %d   bytes %d   pipe-pieces %d'
        % (idx + 1, len(row.encode('utf-8')), len(cells)))
    for k, c in enumerate(cells):
        if k in (0, len(cells) - 1):
            continue
        say('    cell %d  : %d bytes' % (k, len(c.encode('utf-8'))))
    write_text(os.path.join(SCRATCH, 'U1_row_at_HEAD.txt'), row)
    for k in (5, 7):
        dst = os.path.join(SCRATCH, 'U1_cell%d.txt' % k)
        write_text(dst, cells[k].replace(' ### ', '\n### '))
        say('    ### cell %d written to %s -- its own `###` markers turned into line breaks FOR'
            % (k, os.path.basename(dst)))
        say('    ### READING ONLY. ### The ledger holds the cell on ONE line and this act writes')
        say('    ### it back on one line.')
    say()
    say('    ### THE SIX SITES, LOCATED BY THEIR OWN OPENING MARKERS IN CELL 5:')
    c5 = cells[5]
    for tag in ['**(i) ', '**(ii) ', '**(iii) ', '**(iv) ', '**(v) ', '**(vi) ']:
        at = c5.find(tag)
        say('      %-9s : %s' % (tag.strip('* '),
                                 ('at offset %d' % at) if at >= 0 else '### NOT FOUND ###'))

    # ------------------------------------------------------------------ (E) THE BANKS
    say()
    say('-' * 100)
    say('### (E) THE EMITTING BANKS THE ROW NAMES, AT THE SENTENCES IT QUOTES.')
    say('-' * 100)
    b332 = os.path.join(ROOT, 'data', 'b332_the_clause_stated.txt')
    b351 = os.path.join(ROOT, 'data', 'b351_the_partition_question.txt')
    b353 = os.path.join(ROOT, 'data', 'b353_the_missing_statement.txt')
    pull(b332, 'the quantifiers -- over the class, infinite, and through the explicit formula over',
         '(i) THE CLAUSE, IN b332 -- THE QUANTIFIERS', span=True)
    say()
    pull(b351, 'THE ABSCISSA WAS ALREADY CLOSED, AND HAS BEEN SINCE b326',
         "THE ABSCISSA, IN b351 -- THE NAVIGATOR'S FIRST CANDIDATE WITNESS", span=True)
    pull(b351, 'one convergent series did what sixty boxes of argument principle could not',
         'THE ABSCISSA AND THE HEIGHT, SET APART BY b351 ITSELF', span=True)
    pull(b351, 'SO RUNNING THE CENSUS ### ### HIGHER BUYS MORE INSTANCES, AND A CLASS IS NOT'
               ' MADE OF INSTANCES', '(ii) THE HEIGHT, IN b351', span=True)
    say()
    pull(b353, 'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS',
         '(iii) THE WIDTH, IN b353', span=True)
    pull(b353, 'There exists g in Cc^infty(R)',
         "(iii) THE INNER EXISTENTIAL, IN BOAS-KAC'S OWN WORDS AS b353 QUOTES THEM", span=True)

    # ------------------------------------------------------------------ (F) THE COLUMN LAW
    say()
    say('-' * 100)
    say('### (F) THE COLUMN LAW -- BECAUSE A ROW CANNOT GAIN A COLUMN ALONE.')
    say('-' * 100)
    pull(led, '**THE COLUMN LAW.**', "THE LEDGER'S COLUMN LAW, WHOLE")
    body = [l for l in src if l.startswith('|') and set(l.replace('|', '').strip()) not in
            (set(), set('-'), set('- '))]
    seven = [l for l in body if l.rstrip().count('|') == 8]
    say('    table lines in the file                     : %d' % len(body))
    say('    of them, EXACTLY the seven-column shape     : %d' % len(seven))
    say('    ### **A NEW COLUMN IS AN EDIT TO EVERY ONE OF THEM, AND THE LAW SAYS ROWS ARE')
    say('    ### WRITTEN ONLY BY `b327_faces_row.py`.** ### An APPEND INSIDE an existing cell is')
    say('    ### what `b401` and `b404` did to this row and is what this act does; it is a')
    say('    ### RESTATEMENT of a cell, not the writing of a row, and the column count does not move.')

    # ------------------------------------------------------------------ (G) THE ROUTE
    say()
    say('-' * 100)
    say("### (G) WHERE THE CORPUS ITSELF PUTS THE SHARED WITNESS'S SECOND CLAUSE.")
    say('-' * 100)
    ot = os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                      'OPEN_TRAILS-archive-2-historical-landings-and-programs.md')
    pull(ot, 'The joint, located exactly.', "THE CORPUS ON T3'S TWO CLAUSES", span=True)
    say()
    say('    ### **QUOTED AND NOT ENDORSED.** ### This act reads where the record puts the')
    say('    ### second clause. ### **IT MAKES NO CLAIM ABOUT `h2` IN EITHER DIRECTION**, and')
    say('    ### `h2` stands exactly where the deposit left it.')

    say()
    say('=' * 100)
    say('### THE SURVEY IS ON DISK. ### NOTHING IS WRITTEN TO ANY LEDGER BY THIS TOOL.')
    say('=' * 100)
    write_text(OUT, '\n'.join(LINES) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
