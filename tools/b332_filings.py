# -*- coding: utf-8 -*-
"""b332_filings.py -- TWO APPEND-ONLY FILINGS IN PLACE-papers, GENERATED FROM THE ACT'S OWN RECORDS.

### ### (1) `FACES_LEDGER.md` -- row `S1`, the clause stated, written through the writer's `write_row`
### (b327_faces_row.py): duplicates refused, notation guarded, every quotation verified against its emitter,
### read back after the write. ### STATED, with its grade table read from `b332_statement_rows.json`.
### ### (2) the arc keystone `phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md` -- ONE
### appended cross-reference line; no sentence above edited; append-only against the working file and the
### blob at HEAD; idempotent.
### ### Two paths, two run files, numbered on a repeat writing run.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
FACESK = os.path.join(PP, 'phase2', 'method', 'FACES_OF_H2_AT_FINITE_INSTANCE.md')
KEY = os.path.join(PP, 'phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md')
SRC = os.path.join(D, 'b328_source_text.txt')
MARK = '<!-- b332 clause-stated cross-reference -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def row():
    r = json.load(io.open(os.path.join(D, 'b332_statement_rows.json'), encoding='utf-8'))
    table = '; '.join('%s %s: %s' % (k, n, ', '.join('%s (%s)' % (g, o) for g, o, _f in gs)) for k, n, _u, gs, _r in r['constituents'])
    top = r['ranking'][0]
    return dict(
        id='S1',
        cells=[
            'S1 -- the clause stated: for every g in the source\'s class (Definition 3.1, with the vanishing conditions), the places sum of the explicit formula keeps the criterion\'s sign, SUM_v W_v(g conv g-bar^#) <= 0 -- the positivity face\'s realized form, in the arc\'s vocabulary',
            'the fourth: analytic -- R4\'s realized form; STATED, one face and not the compiled equivalence',
            'INTERNAL -- `FINDINGS.md` anchor `clause-stated` (b332); relay `data/b332_the_clause_stated.txt`, `data/b332_statement_rows.json`; the class and the criterion IMPORTED from the source pinned at b328 (Definition 3.1: *"positive de\ufb01nite when its Fourier transform is pointwise positive"*; Proposition C.1, *"RH <=> SUM_v W_v(g conv g-bar^#) <= 0"* in the corpus\'s transcription)',
            'STATED -- no proof attempted, no grade conferred; the deposit\'s words at its head: *"h2 \u2014 nonvanishing of the transform at the point in question"*; the register sentence exact: *"`h2` IS THE SINGLE OPEN PREMISE"*. THE GRADE TABLE, each grade its owner\'s: %s. The open part, unranked: K8 the quantifiers, over the class and over the zeros -- UNOWNED, the clause itself. THE RANKING, softest first under the sealed rule: %s; the navigator\'s registered expectation (the remainder softest) scored %s.'
            % (table, ', '.join('%s (%s)' % (k, g) for _o, k, _n, g, _r in r['ranking']), r['verdict']),
            'CORRESPONDENCE.md: the b332 row, carrying NO TERMINAL (analysis, quantified over an infinite class and over the zeros)',
            'none typed by this act. To R4: this row is R4\'s realized form and confers no equivalence; the deposit\'s refusal governs it. To F1: the same explicit formula, here stated for the whole class and there measured as a control. The aim-map named as next, for the softest constituent %s; neither it nor this act is the discharge.' % top[1],
        ],
        quotes=[(DEP, 'and h2 \u2014 nonvanishing of the transform at the point in question.', False),
                (FACESK, '`h2` IS THE SINGLE OPEN PREMISE.', False),
                (SRC, 'positive de\ufb01nite when its Fourier transform is pointwise positive', False),
                (DEP, 'while deliberately **not** compiling the cross-register equivalences', False)])


def keystone_line():
    return ('\n%s\n\n**Cross-reference, appended 2026-09-06 (b332) and not rewritten:** the open clause is STATED in this arc\u2019s '
            'vocabulary \u2014 the positivity face\u2019s realized form, every constituent unfolded to its owner and graded, the '
            'constituents ranked by grade \u2014 at `FINDINGS.md` anchor `clause-stated` and as row `S1` of `FACES_LEDGER.md`. '
            '**No sentence above was edited and no grade above was moved; the clause is not discharged.**\n' % MARK)


def main():
    fails = []
    rec('=' * 100)
    rec('b332 -- THE FILINGS. ### THE LEDGER ROW THROUGH THE WRITER; THE KEYSTONE\'S APPENDED LINE.')
    rec('=' * 100)
    st, det = W.write_row(row())
    rec('  FACES_LEDGER.md   %-16s %s' % (st, det))
    if st not in ('WRITTEN', 'DUPLICATE'):
        fails.append('FACES_LEDGER')
    before = io.open(KEY, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    if MARK in before:
        rec('  keystone          ALREADY FILED, nothing written (idempotent); mark once : %s' % (before.count(MARK) == 1))
    else:
        new = before.rstrip('\n') + '\n' + keystone_line()
        open(KEY + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(KEY + '.tmp', KEY)
        after = io.open(KEY, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip('\n'))
        pb = after.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
        rec('  keystone          WRITTEN +%d lines ; working TRUE PREFIX %s ; blob TRUE PREFIX %s ; mark once %s' % (len(after.splitlines()) - len(before.splitlines()), pw, pb, after.count(MARK) == 1))
        if not (pw and pb):
            fails.append('KEYSTONE')
    st2 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 : %r ; THE DEPOSIT IS BYTE-UNCHANGED : %s' % (st2, not st2))
    if st2:
        fails.append('DEPOSIT')
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b332_filings_run' if wrote else 'b332_filings_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
