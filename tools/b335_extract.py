# -*- coding: utf-8 -*-
"""b335_extract.py -- THE EXTRACT STEP FOR THE STANDING CLAUSES, FILED. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### The standing clauses as b334's ferry carries them (the reference the
### sortie names), each at its line in that ferry; the same clauses at their lines in the first ferry of the range
### (b320) and in a mid-range ferry (b327), so the file's provenance rests on emitters and not on a seat's memory;
### the executor's rules file where the STOP format is to be filed; the ferry scanner's entry points where the
### citation check is to be added by order; the sortie ferry's own leg-0 sentence. ### b283's law: every quotation
### located at its emitting file and its line before it is written anywhere else.
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

NOTES = os.path.join(D, 'b335_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


F334 = d('b334_ferry_2026-09-06.txt')
F320 = d('b320_ferry_2026-09-04.txt')
F327 = d('b327_ferry_2026-09-05.txt')
F335 = d('b335_ferry_2026-09-06.txt')
RULES = os.path.join(PP, 'protocols', 'EXECUTOR_RULES.md')

WANTED = [
    # ### ---- the reference ferry, b334: the standing clauses at their lines
    ('b334 -- concurrency and the read rule', F334, 'CONCURRENCY: SOLO (research seat; every read through the'),
    ('### the extract-to-disk step', F334, 'extract-to-disk step).'),
    ('### the paste protocol', F334, 'receipt-in-full)'),
    ('### no claim about h2, totality, the roster', F334, 'certified instruments; NO claim about h2, totality, or the'),
    ('### interpreted by nobody', F334, 'softest pair over aims, interpreted by nobody in this act; the'),
    ('### two routes sharing no code', F334, 'never from a seat; every quantity by two routes sharing no'),
    ('### the like-for-like rule', F334, 'code; the like-for-like rule enforced by name (every'),
    ('### normalizations before counts', F334, "species); normalizations before counts; the noise-floor gate"),
    ('### the registration sealed, no counts predicted', F334, 'in the path; registration sealed before any instrument runs,'),
    ('### needles, the stem sweep', F334, 'no counts predicted; needles from the extract file; stem sweep'),
    ('### hedge audit, run files once', F334, 'at extended scope; hedge audit; run files written once per'),
    ('### the suite after the push, nothing deposits', F334, 'path; the suite re-run after the push; nothing deposits.'),
    ('### step zero', F334, 'STEP ZERO: the ferry scan; both censuses; push anything ahead'),
    ('### saying so if nothing is', F334, 'of origin, saying so if nothing is.'),
    ('### closing: rows, keys', F334, 'CLOSING: the correspondence rows; every result keyed; the'),
    ("### M-2, the seam's debt", F334, "per-aim status; M-2's row unchanged under its cap; the seam's"),
    ('### the patent clock, the censuses', F334, 'debt item 1 restated; the patent clock restated; both'),
    ('### the gate, the index, the keys, the order', F334, 'Registration gate; index queried; aim-map keyed. Components'),
    ('### the shadow', F334, 'ordered. THE SHADOW: expected nothing; say so.'),
    ('### the bank and the deviation rule', F334, 'Bank: data/b334_the_aim_map.txt. Deviation rule standing.'),
    ('### execution', F334, 'EXECUTION: ferry scan first; registration sealed before any'),
    ('### the extract step, components in order', F334, 'instrument runs; the extract step for every read; components'),
    ('### the suite, the pins', F334, 'in order; full control suite, re-run after the push; pins by'),
    ('### the hook', F334, 'ls-remote across all three repos; the hook if PLACE-papers is'),
    ('### the mirror, STOP', F334, 'touched; mirror if it moves. STOP.'),
    ('### the foot', F334, 'deposit left it; locks last.'),
    # ### ---- the first ferry of the range, b320
    ('b320 -- concurrency', F320, 'CONCURRENCY: SOLO (research seat; every read through the'),
    ('### step zero at b320', F320, 'STEP ZERO: the ferry scan; the ledger census with its scope;'),
    ('### the registration clause at b320', F320, 'extended scope; hedge audit; registration term-scanned,'),
    ('### nothing deposits at b320', F320, 'beyond the register sentence exact; nothing deposits.'),
    # ### ---- a mid-range ferry, b327
    ('b327 -- closing', F327, 'CLOSING: the correspondence rows by the idempotent tool; every'),
    ('### the shadow at b327', F327, 'ordered. THE SHADOW: expected nothing; say so.'),
    ('### execution at b327', F327, 'EXECUTION: ferry scan first; registration sealed before any'),
    ('### the foot at b327', F327, 'where the deposit left it; locks last.'),
    # ### ---- the sortie ferry: leg 0's own sentence
    ('the sortie -- leg 0', F335, 'LEG 0 (b335) \u2014 THE STANDING CLAUSES, FILED: extract the scope,'),
    ('### into the file, versioned', F335, 'into relay/tools/FERRY_STANDING.md, versioned, with the ferry'),
    ('### the scan checks the citation', F335, 'scan checking that a ferry citing it cites the current'),
    ('### the STOP format', F335, "version; and add to the executor's STOP format a DRAFT of the"),
    ('### DRAFT -- NAVIGATOR EDITS', F335, 'next ferry, marked DRAFT \u2014 NAVIGATOR EDITS. Filings only.'),
    ('### carried by reference', F335, "carried by reference \u2014 and leg 0 puts them in a file so the"),
    # ### ---- the executor's rules file, and the scanner
    ("the executor's rules -- Rule 5, the last rule", RULES, '## Rule 5 \u2014 The two verification legs'),
    ('### Rule 4.9, no git add -A', RULES, '`git add -A` is BANNED in the relay.'),
    ('ferry_scan -- the record it reads', t('ferry_scan.py'), "RECORD = os.path.join(ROOT, 'data', 'STRUCK_CLAUSES.md')"),
    ('### the verdict line', t('ferry_scan.py'), "print('  ### VERDICT: ### **%d HIT(S) REPORTED. ### NOTHING REFUSED, NOTHING EDITED.**'"),
    ('### the reader rules', t('ferry_scan.py'), "print('  ### the clause to strike it, and that quotation hits. ### THE READER RULES.')"),
    ('### the exit code', t('ferry_scan.py'), 'return 1 if (ch or sh) else 0'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b335_extract.py -- THE STANDING CLAUSES, FILED. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
