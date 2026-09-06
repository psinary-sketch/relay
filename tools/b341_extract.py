# -*- coding: utf-8 -*-
"""b341_extract.py -- THE EXTRACT STEP FOR THE TWO COEFFICIENTS. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The two emitters that disagree -- the bench's `KEIPER` dictionary at its line
### and the balance keystone's literature column at its lines -- with the keystone's computed column beside them; b327's
### incidental finding and its typed fixture; the pinned source's sentences on Keiper's and Maslanka's computations and
### its references [34] and [40]; ERRATA's partition ruling and the internal-record convention entry's heading; the
### sortie ferry's leg-3 sentences and (L3). ### b283's law: every quotation located at its emitting file and its line
### before it is written anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b341_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def p(n):
    return os.path.join(PP, n)


SRC = d('b327_source_text.txt')
B327 = d('b327_the_faces_ledger.txt')
KEY = p(os.path.join('phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md'))
BENCH = p(os.path.join('internal', 'bench', 'li_bench.py'))
ERR = p('ERRATA.md')
FINDINGS = p('FINDINGS.md')
FERRY = d('b341_ferry_2026-09-06.txt')

WANTED = [
    # ### ---- the two emitters
    ("the bench -- the KEIPER dictionary", BENCH, "KEIPER = {1: '0.0230957089662', 2: '0.0923457352914', 3: '0.2077580993', 4: '0.3687904', 5: '0.5747345'}"),
    ('### its validation print', BENCH, 'print("VALIDATION against Keiper (lambda_n = lambda_A + lambda_Z):")'),
    ('### the bench is an instrument', BENCH, 'BENCH INSTRUMENT (not an argument)'),
    ('the keystone -- the validation head', KEY, '**Validation against the literature** (\u03bb_n, computed = \u03bb_A + \u03bb_Z):'),
    ('### the table head', KEY, '| n | computed \u03bb_n | literature | absdiff |'),
    ('### n = 1', KEY, '| 1 | 0.023095708966121 | 0.02309570896612103 | 3.8e-18 |'),
    ('### n = 2', KEY, '| 2 | 0.092345735228047 | 0.09234573529135263 | 6.3e-11 |'),
    ('### n = 3', KEY, '| 3 | 0.20763892055432 | 0.20763892059268 | 3.8e-11 |'),
    ('### n = 4', KEY, '| 4 | 0.36879047949224 | 0.36879047952 | 2.8e-11 |'),
    ('### n = 5', KEY, '| 5 | 0.57554271446118 | 0.57554271443 | 3.1e-11 |'),
    ("### the residuals track the literature's digits", KEY, '(The residuals track the digits of the *literature* constants quoted, not the computation.)'),
    ('### verified against Keiper at n = 1, 2', KEY, '**Measurements (\u03b6, n \u2264 60; verified against Keiper to ten digits at n = 1, 2; cross-radius consistency to eight decimals at n = 24).**'),
    ('### the channels table, n = 3', KEY, '| 3 | \u22121.01305800766 | 1.22069692822 | 0.207638920554 | 258 |'),
    ('### the channels table, n = 5', KEY, '| 5 | \u22120.882725785736 | 1.4582685002 | 0.575542714461 | 258 |'),
    # ### ---- b327's incidental finding
    ("b327 -- the finding", B327, '### ### **AND ONE INCIDENTAL FINDING, FILED NOT EDITED:** ### the bench\'s own `KEIPER` dict reads'),
    ('### the values', B327, "### `0.2077580993` at `n = 3` and `0.5747345` at `n = 5`, where the balance keystone's literature"),
    ('### the computed values match the keystone', B327, "### column (lines 291 and 293) reads `0.20763892059268` and `0.57554271443`; the computed values match the"),
    ('### a typed fixture, the owner not edited', B327, "### keystone's column and not the dict. ### A typed fixture in an owner instrument; the owner is not"),
    ("### the b327 sum reproduces the keystone's computed column", B327, "### by `1.0` at every `n`. ### The sum `lambda_A + lambda_Z` reproduces the keystone's computed column"),
    ('FINDINGS -- the fixture tabled', FINDINGS, "| **The Li bench versus the keystone** | the bench\u2019s literature dictionary disagrees with the balance keystone\u2019s column at `n = 3` and `n = 5` (b327) | a typed fixture, filed and not edited; the author\u2019s to reconcile. |"),
    # ### ---- the pinned source on the literature
    ("the source -- Keiper's coefficients", SRC, 'computations futher below. Keiper\u2019s coe\ufb03cients equal 1'),
    ('### in terms of (1.1)', SRC, 'n\u03bb\u2212n, in terms of (1.1). Keiper noted'),
    ('### Maslanka computed to 3300', SRC, 'In more recent work K. Maslanka [40] computed \u03bbn for 1 \u2264n \u2264 3300 and empirically stud-'),
    ('### reference [34]', SRC, '[34] J. Keiper, Power series expansions of Riemann\u2019s \u03be-function, Math. Comp. 58 (1992),'),
    ('### reference [40]', SRC, '[40] K. Maslanka, E\ufb00ective method of computing Li\u2019s coe\ufb03cien ts and their properties, Exper-'),
    # ### ---- ERRATA: the partition and the internal-record convention
    ('ERRATA -- the partition ruling', ERR, '**THE RULING, AS RATIFIED:** *"ERRATA is partitioned into a deposit-facing section and an internal-record section by an append-only header line, entries unmoved."* **This block is that header line.**'),
    ('### the internal-record list', ERR, '**INTERNAL-RECORD** \u2014 entries whose own words place them in the corpus\'s internal record:'),
    ('### the convention entry\'s heading', ERR, '## E-2026-09-03-1 \u2014 The archimedean remainder\'s normalization convention is the corpus\'s own, not the source\'s (INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)'),
    ('### a CORRECTED entry\'s form', ERR, '## E-2026-08-24-1 \u2014 REGISTRY\'s Day-1 deposit lines contradicted REGISTRY\'s own `d1-1` row (CORRECTED)'),
    ('### prior wordings retained in place', ERR, '### **Prior wordings are quoted above and retained in place at each site** \u2014 the record does not silently overwrite itself.'),
    ("### the file's own law", ERR, 'Entries are retained across deposits and are never restated to the current'),
    # ### ---- the sortie ferry, leg 3
    ('the sortie -- leg 3', FERRY, 'LEG 3 (b341) \u2014 THE TWO COEFFICIENTS: the Li bench\'s literature'),
    ('### the disagreement named', FERRY, 'dictionary and the balance keystone\'s column disagree at the'),
    ('### read both, locate, decide', FERRY, 'third and fifth coefficients; read both at their emitting files,'),
    ('### under the import bar', FERRY, 'locate the literature values under the import bar, decide which'),
    ('### the ERRATA entry per the partition', FERRY, 'is a transcription defect, and file an ERRATA entry (internal or'),
    ('### owner files untouched', FERRY, 'deposit-facing per the partition) with the owner files untouched.'),
    ('### (L3)', FERRY, 'fourth control holds with the pole constant carried; (L3) the'),
    ('### the bench carries the defect', FERRY, 'bench carries the defect. h2 where the deposit left it; nothing'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b341_extract.py -- THE TWO COEFFICIENTS. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:3]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
