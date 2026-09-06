# -*- coding: utf-8 -*-
"""b337_extract.py -- THE EXTRACT STEP FOR THE WAVE'S HOUSEKEEPING. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### REGISTRY's `d1-1` row (the governing deposit statement, ruled at b145);
### the three ledgers' own deposit statements -- ERRATA's head, the loom's gate-1 pin, the trails' deposit-voice pin;
### every ERRATA entry's heading and the sentence in it that places it deposit-facing or internal-record; the fetch
### tool's record URL (b236, the ruling it executes); the counsel list's receipts item and the deadline board's
### notices line; the nine August TECHNE module files at their first lines; the sortie ferry's leg-2 sentences and
### the two rulings. ### b283's law: every quotation located at its emitting file and its line before it is written
### anywhere else.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PAT = r'D:\MY-DOwnloads\patent-package-BACKUP-2026-08-29'
TC = r'D:\MY-DOwnloads\TECHNE-Core'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b337_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def p(n):
    return os.path.join(PP, n)


REG = p('REGISTRY.md')
ERR = p('ERRATA.md')
LOOM = p('VERIFICATION_LOOM.md')
TRAILS = p('OPEN_TRAILS.md')
FERRY = d('b337_ferry_2026-09-06.txt')
AUG = ['BANKED_MEANINGS_ENGINE.md', 'DECISION_CARD_FORMAT.md', 'DISCRIMINATOR_PROTOCOL.md', 'FACE_OFF_PROTOCOL.md', 'HARNESS_LORE.md',
       'IMPORT_LEDGER.md', 'INDEX.md', 'RENDER_AS_E0.md', 'SIGNEDNESS.md']

WANTED = [
    # ### ---- REGISTRY, the governing statement
    ("REGISTRY -- the d1-1 row", REG, '| d1-1 | A Place to Stand (monograph) | `day1/A_Place_to_Stand.md` | v5.13 |'),
    ('### the Day-1 header', REG, '*Published on Zenodo \u2014 current deposit **v1.1.2**, DOI [10.5281/zenodo.21539167]'),
    # ### ---- the three ledgers' deposit statements
    ("ERRATA -- its head names v1.1.1 as current", ERR, 'publication. The current deposit is the monograph at manuscript **v5.8** /'),
    ('### the DOI it names', ERR, 'Zenodo **v1.1.1** ([10.5281/zenodo.21436278](https://doi.org/10.5281/zenodo.21436278);'),
    ('### entries never restated', ERR, 'Entries are retained across deposits and are never restated to the current'),
    ("the loom -- the gate-1 pin", LOOM, '21539167` returns **v1.1.2 \u00b7 2026-07-24 \u00b7 DOI 10.5281/zenodo.21539167 \u00b7 concept 19675355 \u00b7 11'),
    ('### REGISTRY accurate, ERRATA untouched', LOOM, '### **NO DEPOSIT DEFECT. ERRATA IS UNTOUCHED \u2014 there was no disagreement to file**, and the'),
    ("the trails -- the deposit-voice pin", TRAILS, '**Deposit-voice is pinned** by the read-only fetch of 2026-08-28: Zenodo **v1.1.2**, DOI'),
    # ### ---- every ERRATA entry, and its placing sentence
    ('E-2026-07-23-1', ERR, '## E-2026-07-23-1 \u2014 \u00a718.2 on-line constraint mislabeled Im(\u03be) (should be Re(\u03be))'),
    ('### its claim as deposited', ERR, '**The claim as deposited.** "The constraint function for on-line zeros is **Im(\u03be)** (one condition, codimension 1'),
    ('E-2026-07-12-1', ERR, '## E-2026-07-12-1 \u2014 "zero custom axioms" does not hold, as deposited, of Route 1 and the formation certificates'),
    ('E-2026-07-13-1', ERR, '## E-2026-07-13-1 \u2014 Deposit-frozen count claims: scope verification'),
    ('E-2026-07-18-1', ERR, '## E-2026-07-18-1 \u2014 in-file version stamp lagged the version log (deposited monograph v1.1.0)'),
    ('E-2026-07-27', ERR, '## E-2026-07-27 \u2014 the substrate season (v5.13; audit-trail record, additive synthesis)'),
    ('### additive, no prior claim corrected', ERR, '(no prior claim corrected \u2014 additive;'),
    ('E-2026-08-31-1', ERR, "## E-2026-08-31-1 \u2014 b264's `W-ORD-NTERM-FLOOR` filing claimed a provenance the record contradicts (WITHDRAWN)"),
    ('### no deposited artifact affected', ERR, '### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY.**'),
    ('E-2026-08-24-1', ERR, "## E-2026-08-24-1 \u2014 REGISTRY's Day-1 deposit lines contradicted REGISTRY's own `d1-1` row (CORRECTED)"),
    ('E-2026-08-24-2', ERR, '## E-2026-08-24-2 \u2014 The deposited record TITLES carry a grammar the corpus'),
    ('### no deposit action, nothing written at Zenodo', ERR, '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.'),
    ('E-2026-08-24-3', ERR, '## E-2026-08-24-3 \u2014 The patent deadline board carried a four-month-late wall for two filings (CORRECTED)'),
    ('### no deposited artifact is affected (the board)', ERR, '**No deposited artifact is affected.**'),
    ('E-2026-09-03-1', ERR, "## E-2026-09-03-1 \u2014 The archimedean remainder's normalization convention is the corpus's own, not the source's (INTERNAL RECORD"),
    # ### ---- the fetch tool and the ruling it executes
    ('b236 -- the record URL', t('b236_deposit_fetch.py'), "REC = 'https://zenodo.org/api/records/21539167'"),
    ('### the ruling it executes', t('b236_deposit_fetch.py'), '### THE RULING THIS EXECUTES (the author\'s, 2026-08-28): "The deposit\'s 11 files are fetched'),
    ('### only public identifiers go out', t('b236_deposit_fetch.py'), '### TRANSMISSION DISCIPLINE (b130\'s law): ### ONLY PUBLIC IDENTIFIERS GO OUT -- the record URL'),
    # ### ---- the patent seat's own record of the receipts
    ("the counsel list -- item 3, the receipts", os.path.join(PAT, 'COUNSEL_ITEMS.md'), '| **3** | **NEW-6 / NEW-8 receipts** | standing |'),
    ("### the entity split read on F:", os.path.join(PAT, 'COUNSEL_ITEMS.md'), 'Established 2026-08-30 by reading the file wrappers on `F:`.'),
    ('the deadline board -- the notices copied', os.path.join(PAT, 'OFFICE_DEADLINES_2026-08-30.md'), 'All four notices are now copied into `exports/2026-08-30/NOTICES_AS_READ/`.'),
    ('### enumerate the volumes', os.path.join(PAT, 'OFFICE_DEADLINES_2026-08-30.md'), 'volumes before concluding a file does not exist.**'),
    # ### ---- the sortie ferry, leg 2 and the rulings
    ('the sortie -- leg 2', FERRY, "LEG 2 (b337) \u2014 THE WAVE'S HOUSEKEEPING: the three ledgers"),
    ('### reconciled against a fetch', FERRY, 'reconciled to REGISTRY against a read-only deposit fetch, drift'),
    ('### the ERRATA ruling', FERRY, 'by this paste and strikeable: "ERRATA is partitioned into a'),
    ('### by an append-only header line', FERRY, 'append-only header line, entries unmoved. The nine August'),
    ('### the TECHNE ruling', FERRY, 'TECHNE module files are committed to the canonical local clone,'),
    ('### not pushed', FERRY, 'not pushed."'),
    ('### the receipts', FERRY, 'the patent receipts checked for on disk and their'),
    ('### absence or presence stated', FERRY, 'absence or presence stated. THE RULINGS, the author\'s, ratified'),
] + [('TECHNE August -- %s' % n, os.path.join(TC, 'modules', '2026-08', n), '#') for n in AUG]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec("b337_extract.py -- THE WAVE'S HOUSEKEEPING. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.")
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
        short = path.replace(PP, '<papers>').replace(SIDE, '<side>').replace(PAT, '<patent>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
