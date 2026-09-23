# -*- coding: utf-8 -*-
"""b488_extract.py -- THE SURVEY. ### **NOTHING IS RE-FOLDED AND NOTHING IS RE-SCORED.**
### (R98) directs that b486's arc section be written into `FINDINGS.md` FROM b486's OWN BANK.
### This survey reads that bank, reads the standing fold FORM from the two folds already in
### `FINDINGS.md`, reads the span tool's CURRENT reading, and reads `corr_row.py`'s prior
### behaviour from its own header. ### **IT WRITES NOTHING.**
"""
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
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
NL = chr(10)
L, MISSES = [], []

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


def main():
    rec('=' * 108)
    rec('b488 -- THE SURVEY. ### (R98)`S SECTION, AND THE ROW WRITER`S PRIOR BEHAVIOUR.')
    rec('=' * 108)

    # ---------------------------------------------------------------- (P1) b486's bank
    rec('')
    rec('(P1) b486`S OWN BANK -- THE ONLY SOURCE COMPONENT 1 MAY DRAW ON.')
    rec('-' * 108)
    fold = read(os.path.join(D, 'b486_the_fold.txt'))
    ot = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    i = ot.find('### b486 ')
    j = ot.find('### b487 ', i + 1) if i >= 0 else -1
    trail = ot[i:j] if i >= 0 and j > i else ''
    rec('    `data/b486_the_fold.txt`      : %d bytes, %d lines' % (len(fold), fold.count(NL)))
    rec('    b486`s trail record           : %d bytes %s'
        % (len(trail), '' if trail else '### **NOT FOUND**'))
    if not fold:
        MISSES.append(('b486_the_fold.txt', 'absent'))
    if not trail:
        MISSES.append(('OPEN_TRAILS.md', 'b486 record not delimited'))

    # the eleven acts, in filing order, as the bank numbers them
    acts = re.findall(r'### \*\*\s*(\d+)\. (b\d+[a-z]?)\*\* -- (.+)', fold)
    rec('    ### ### **THE SPAN, BY FILING, AS b486`S BANK NUMBERS IT : %d ACT(S).**' % len(acts))
    rec('      %s' % ', '.join(a[1] for a in acts))
    if len(acts) != 11:
        MISSES.append(('b486_the_fold.txt', 'expected eleven acts, got %d' % len(acts)))

    clauses = re.findall(r'### \*\*\((\d)\)\*\* (.+)', fold)
    cited = re.findall(r'--- cited from ### \*\*([^*]+)\*\*', fold)
    rec('    ### digest clauses : ### **%d** ### ; each with a cited act : ### **%s**'
        % (len(clauses), len(clauses) == len(cited)))
    for (n, txt), c in zip(clauses, cited):
        rec('      (%s) %-72s -- %s' % (n, txt[:72], c.strip()))
    if len(clauses) != 6:
        MISSES.append(('b486_the_fold.txt', 'expected six clauses, got %d' % len(clauses)))

    rulings = re.findall(r'^    (R\d+)\s+(b\d+[a-z]?)\s+(.+)$', fold, re.M)
    rec('    ### rulings in the span, as the bank tables them : ### **%d**' % len(rulings))
    rec('      %s' % ', '.join(r[0] for r in rulings))
    if len(rulings) != 13:
        MISSES.append(('b486_the_fold.txt', 'expected thirteen rulings, got %d' % len(rulings)))

    defects = re.findall(r'^    (b\d+[a-z]?)\s{4,}(.+)$', fold, re.M)
    rec('    ### acts recording a defect of their own instruments : ### **%d**' % len(defects))
    if len(defects) != 7:
        MISSES.append(('b486_the_fold.txt', 'expected seven defect rows, got %d' % len(defects)))

    # ---------------------------------------------------------------- (P2) the standing form
    rec('')
    rec('(P2) THE STANDING FOLD FORM, READ FROM THE FOLDS ALREADY IN `FINDINGS.md`.')
    rec('-' * 108)
    fnd = read(os.path.join(PP, 'FINDINGS.md'))
    heads = [(k + 1, l) for k, l in enumerate(fnd.split(NL))
             if l.startswith('## ') and 'THE FOLD' in l.upper()]
    rec('    fold sections present : ### **%d**' % len(heads))
    for k, l in heads:
        rec('      FINDINGS.md:%-5d %s' % (k, l.strip()[:110]))
    last = heads[-1][0] if heads else 0
    sub = [l.strip() for l in fnd.split(NL)[last:] if l.startswith('### ')]
    rec('    ### the LAST fold`s subsection headings, which b488 follows:')
    for s in sub:
        rec('        %s' % s)
    rec('    FINDINGS.md : %d bytes, %d lines. ### **THE SECTION IS APPENDED AT THE END.**'
        % (len(fnd), fnd.count(NL)))
    # ### ### **THE PREDICATE`S FIRST VERSION WAS WRONG AND (R70)`S REHEARSAL CAUGHT IT.**
    # ### It looked for `b474` in the last heading. ### **A FOLD SECTION`S HEADING NAMES THE
    # ### SPAN IT FOLDS, NOT THE ACT THAT FILED IT** -- b474 filed `b464-b473`, so its own
    # ### number appears nowhere in the heading and a true record scored as a MISS.
    # ### The check now reads the span`s LAST ACT, which is what the heading carries.
    if 'b473' not in (heads[-1][1] if heads else ''):
        MISSES.append(('FINDINGS.md', 'the last fold section does not end at b473'))
    rec('    ### ### **AND `b486` MUST NOT ALREADY BE A FOLD SECTION:** occurrences of a')
    rec('    ### heading naming it : ### **%d**'
        % len([1 for _, l in heads if 'b486' in l or 'b475' in l]))

    # ---------------------------------------------------------------- (P3) the span tool, BEFORE
    rec('')
    rec('(P3) THE SPAN TOOL`S READING, BEFORE THE SECTION IS WRITTEN.')
    rec('-' * 108)
    r = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    txt = (r.stdout or '').replace(chr(13), '')
    before = {}
    # ### ### **AND THE SPAN-TOOL PATTERNS WERE WRONG TOO, ON THE SAME REHEARSAL.** ### They
    # ### were written from what the tool was expected to print, not from what it prints.
    # ### Both returned nothing, and ### **(N1) CANNOT BE SCORED BY A PATTERN THAT MATCHES
    # ### NOTHING** -- a blank is not a reading. ### Read from the tool`s actual lines.
    for key, pat in (('last_fold', r'the last fold covers\s*:\s*(b\d+[a-z]? - b\d+[a-z]?)'),
                     ('folds', r'FOLDS RUN : (\d+)'),
                     ('span', r'THE CURRENT SPAN : (\d+) ACT')):
        m = re.search(pat, txt)
        before[key] = m.group(1) if m else ''
    for l in txt.split(NL):
        if 'LAST FOLD' in l.upper() or 'CURRENT SPAN' in l.upper() or 'FOLDS' in l.upper():
            rec('      %s' % l.strip()[:104])
    rec('    ### ### **BEFORE : last fold %s ; folds %s ; current span %s.**'
        % (before['last_fold'] or '?', before['folds'] or '?', before['span'] or '?'))
    rec('    ### ### **(N1) IS REFUTABLE BY THIS SAME READING TAKEN AFTER THE WRITE.**')

    # ---------------------------------------------------------------- (P4) corr_row.py
    rec('')
    rec('(P4) `corr_row.py`, AS IT STANDS -- ITS PRIOR BEHAVIOUR, QUOTED FROM ITS OWN HEADER.')
    rec('-' * 108)
    cr = read(os.path.join(T, 'corr_row.py'))
    doc = cr.split('"""')[1] if cr.count('"""') >= 2 else ''
    lim = [l.strip() for l in cr.split(NL) if l.strip().startswith('# ###')]
    rec('    `tools/corr_row.py` : %d bytes, %d lines' % (len(cr), cr.count(NL)))
    rec('    ### the header`s declared limits, verbatim:')
    for l in lim:
        rec('        %s' % l[2:][:100])
    rec('    ### ### **AND NOTHING IN THOSE LIMITS MENTIONS THE ROW NUMBER.** ### The tool')
    rec('    ### validates cell COUNT and EMPTINESS and reads the row back; it never looks at')
    rec('    ### what number the first cell carries, and it appends unconditionally.')
    rec('      `write_row` appends and reads back : ### **%s**'
        % ('VERDICT     : WRITTEN, verified by read-back' in cr))
    rec('      any check on an existing row number : ### **%s**'
        % bool(re.search(r'already (?:in|exists)|duplicate|taken', cr, re.I)))
    if re.search(r'already (?:in|exists)|duplicate', cr, re.I):
        MISSES.append(('corr_row.py', 'a number check already present'))

    ledger = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', ledger, re.M)]
    rec('    the ledger `CORRESPONDENCE.md` : rows ### **%d** ### ; highest ### **%d**'
        % (len(nums), max(nums) if nums else 0))
    rec('    ### the next free number : ### **%d**' % ((max(nums) if nums else 0) + 1))
    rec('    ### ### **(N2) IS REFUTABLE BY THE GUARD`S FIRST RUN:** its positive control')
    rec('    ### offers an EXISTING number and must be refused ### **WITHOUT REPAIR.**')

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b488_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(acts=acts, clauses=clauses, cited=[c.strip() for c in cited],
                   rulings=rulings, defects=defects, span_before=before,
                   subheads=sub, ledger_rows=len(nums), ledger_max=max(nums) if nums else 0,
                   misses=MISSES),
              io.open(os.path.join(D, 'b488_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
