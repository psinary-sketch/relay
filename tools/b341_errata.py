# -*- coding: utf-8 -*-
"""b341_errata.py -- THE ERRATA ENTRY, APPENDED ONLY ON A VERDICT THAT NAMES A CARRIER (registration (D), sealed first).

### ### **ONE BLOCK, APPEND-ONLY, UNDER `<!-- b341 -->`, THE ID `E-2026-09-06-1`, ITS CLASS IN ITS HEADING** in the convention
### entry's form (INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED). ### Both prior wordings quoted at their files and lines
### (read from the extract and the records, never retyped); the carrier named; the two routes' values; the located
### literature with its sources' hashes; NO OWNER FILE IS EDITED -- the correction of record is this act's bank (the E1
### precedent). ### The partition block is not edited. ### On WITHHELD nothing is written.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
ERR = os.path.join(PP, 'ERRATA.md')
MARK = '<!-- b341 -->'
RUN = os.path.join(D, 'b341_errata_run.txt')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def blob():
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:ERRATA.md'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''


def entry_lines(C, L):
    t3, t5 = C['table']['3'], C['table']['5']
    k3, k5 = C['keystone_rows']['3'], C['keystone_rows']['5']
    s1 = L['sources']['S1']
    loc3 = L['sources']['S1']['hits']['3'][0]
    beside5 = [b for b in C['beside']['5'] if b['source'] == 'S1']
    coff = {n: [b for b in C['beside'][str(n)] if b['source'] == 'S3'] for n in (3, 5)}
    srcs = L['sources']
    return ['', MARK, '',
            '## E-2026-09-06-1 \u2014 The Li bench\'s literature dictionary carries transcription defects at the third and fifth coefficients; the balance keystone\'s column does not (INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)',
            '',
            '**Filed 2026-09-06 (b341, leg 3 of the sortie b339\u2013b343). Found 2026-09-05 (b327, an incidental finding, typed a fixture and left unedited). Records affected: `internal/bench/li_bench.py` (its `KEIPER` dictionary, line %d) and, as the other party, `phase1.5/spectral/BALANCE_AND_POSITIVITY.md` (its literature column, lines %d and %d). ### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY.** The bench is an internal instrument and the keystone an internal record; the dictionary enters no computation \u2014 it is printed beside the bench\'s computed values as a validation line \u2014 and no deposited number rests on it.'
            % (C['bench_line'], k3['line'], k5['line']),
            '',
            '**What was wrong.** The two emitters disagree at `n = 3` and `n = 5`, and the record had not said which was right:',
            '',
            '| Site | Prior wording, retained in place | n = 3 | n = 5 |',
            '|:--|:--|:--|:--|',
            '| the bench, line %d | `KEIPER = {1: \'0.0230957089662\', 2: \'0.0923457352914\', 3: \'0.2077580993\', 4: \'0.3687904\', 5: \'0.5747345\'}` | `%s` | `%s` |' % (C['bench_line'], t3['bench'], t5['bench']),
            '| the keystone, lines %d and %d | `%s` and `%s` | `%s` | `%s` |' % (k3['line'], k5['line'], '\\| 3 \\| %s \\| %s \\| %s \\|' % (k3['computed'], k3['literature'], k3['absdiff']), '\\| 5 \\| %s \\| %s \\| %s \\|' % (k5['computed'], k5['literature'], k5['absdiff']), t3['keystone'], t5['keystone']),
            '',
            '**The values, by two routes that share no quadrature** (relay `tools/b341_coefficients.py`): route (A), the bench\'s own definitions executed from its file at its two radii, and route (B), the Li map of `log \u03be` by Taylor differentiation at `s = 1`, agree to `%s` and `%s`:'
            % (t3['dAB'], t5['dAB']),
            '',
            '| n | route (A) | route (B) | the bench\'s dictionary, off by | the keystone\'s column, off by |',
            '|:--|:--|:--|:--|:--|',
            '| 3 | `%s` | `%s` | `%s` | `%s` |' % (t3['A'], t3['B'], t3['bench_off'], t3['keystone_off']),
            '| 5 | `%s` | `%s` | `%s` | `%s` |' % (t5['A'], t5['B'], t5['bench_off'], t5['keystone_off']),
            '',
            '**The literature, under the import bar** (relay `tools/b341_locate.py`; each source fetched read-only by one GET, hashed, its text extracted and banked, no PDF committed). Keiper 1992 (the source\'s [34]; sha256 `%s`, %d bytes) tabulates his coefficients, which are `\u03bb_n / n`: at `n = 3` its row reads `%s` `(\u22122)` at line %d of the banked text \u2014 **LOCATED, and it agrees with the keystone\'s value** (`3 \u00d7 0.0692129735181\u2026 = 0.2076389205543\u2026`); at `n = 5` its row reads `1 15108542892235\u2026 (\u22121)` at line %d, a mantissa the text layer split at its decimal point \u2014 a reading beside the sealed rule, not LOCATED under it, and it too agrees with the keystone (`5 \u00d7 0.115108542892\u2026 = 0.575542714461\u2026`). Maslanka math/0406312 (the source\'s [40]; sha256 `%s`) carries no tabulation at these indices. Coffey math-ph/0505052 (sha256 `%s`) prints `%s` and `%s` at lines %s and %s of its banked text \u2014 six-decimal prints, readings beside the rule, both agreeing with the keystone. **No located source agrees with the dictionary at either index.**'
            % (s1['sha256'], s1['bytes'], loc3['string'], loc3['line'], beside5[0]['line'] if beside5 else 0, srcs['S2']['sha256'], srcs['S3']['sha256'],
               coff[3][0]['string'] if coff[3] else '(none)', coff[5][0]['string'] if coff[5] else '(none)', coff[3][0]['line'] if coff[3] else '-', coff[5][0]['line'] if coff[5] else '-'),
            '',
            '**The verdict, by the rule sealed before any value (relay `data/b341_registration_2026-09-06.txt`, section (D)): %s.** The bench\'s dictionary differs from the two agreeing routes in the fourth significant figure at `n = 3` and the third at `n = 5`; the keystone\'s column agrees with the routes to its printed digits at both, and the keystone\'s own computed column (`%s`, `%s`) agrees with them to fourteen digits. **The dictionary\'s name is not its provenance**: Keiper\'s coefficients are `\u03bb_n / n`, and the dictionary\'s values at `n = 1, 2` are Li\'s `\u03bb_n`, not Keiper\'s; where the two defective entries came from is not determined here.'
            % (C['verdict'], k3['computed'], k5['computed']),
            '',
            '**The correction, and the form it takes.** ### **NO OWNER FILE IS EDITED.** `li_bench.py` and `BALANCE_AND_POSITIVITY.md` stand byte-identical; their prior wordings are quoted above and retained in place. **The correction of record is this entry and b341\'s bank**, relay `data/b341_the_two_coefficients.txt`, following the `E1` precedent (`E-2026-08-31-1`) and the convention entry (`E-2026-09-03-1`): the record says what the dictionary\'s two entries are \u2014 transcription defects \u2014 and what the values are, and a reader of the bench\'s validation line reads it with this entry beside it. FINDINGS\' tabling of the fixture (*the author\'s to reconcile*) is not edited; this entry is the reconciliation on the record, and the author\'s ruling on whether to repair the dictionary in place stays the author\'s.',
            '',
            '**Scope, stated so it is not read wider than it is.** This entry concerns two constants in a validation dictionary of an internal instrument. *It is not a claim that any bench measurement changes* \u2014 the bench\'s computed `\u03bb_n` are reproduced here by two routes \u2014 *not a claim about `\u03bb_n` beyond `n = 5`, and not a retraction.* No grade moves and no act is re-verdicted.',
            '',
            '---']


def main():
    L = []

    def rec(s=''):
        L.append(s)
    rec('=' * 100)
    rec('b341 -- THE ERRATA ENTRY. ### appended only on a naming verdict; the partition block untouched.')
    rec('=' * 100)
    C = json.load(io.open(os.path.join(D, 'b341_coefficients.json'), encoding='utf-8'))
    LJ = json.load(io.open(os.path.join(D, 'b341_locate.json'), encoding='utf-8'))
    txt = io.open(ERR, encoding='utf-8').read()
    hb = blob()
    if not C['names_carrier']:
        rec('  the verdict is %r -- NOTHING WRITTEN, by the sealed rule.' % C['verdict'])
        st = 'NOTHING'
    elif MARK in txt:
        rec('  the mark %s is already present -- DUPLICATE, nothing written.' % MARK)
        st = 'DUPLICATE'
    else:
        body = entry_lines(C, LJ)
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(body) + chr(10)
        open(ERR + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(ERR + '.tmp', ERR)
        st = 'WRITTEN'
    after = io.open(ERR, encoding='utf-8').read()
    pw = after.startswith(txt.rstrip(chr(10)))
    pb = after.replace(chr(13) + chr(10), chr(10)).startswith(hb.replace(chr(13) + chr(10), chr(10)).rstrip(chr(10))) if hb else None
    part = after.index('<!-- b337 partition -->')
    part_block = after[part:after.index(MARK)] if MARK in after else after[part:]
    part_same = part_block.strip() in txt
    rec('  status %s ; mark on disk %d time(s) ; append-only against the working file %s ; against the blob %s ; the partition block unchanged %s ; lines %d -> %d'
        % (st, after.count(MARK), pw, pb, part_same, len(txt.splitlines()), len(after.splitlines())))
    ok = st in ('WRITTEN', 'DUPLICATE', 'NOTHING') and pw and (pb is not False) and part_same and after.count(MARK) <= 1
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    out = RUN if not os.path.exists(RUN) else RUN.replace('_run.txt', '_rerun.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print(chr(10).join(L))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
