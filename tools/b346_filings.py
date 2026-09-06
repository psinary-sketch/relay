# -*- coding: utf-8 -*-
"""b346_filings.py -- THE ERRATUM'S CONSEQUENCE CLAUSE, FIRED AND APPENDED. ### ONE BLOCK, APPEND-ONLY.

### ### **IT FIRES IF AND ONLY IF THE VERDICT IS `RESOLVED`,** as section (E) of the sealed registration requires;
### otherwise this tool writes nothing at all and says so. ### The block goes on `ERRATA.md` under a `b346` mark,
### against entry `E-2026-09-03-1`; ### **THAT ENTRY IS NOT EDITED AND NO NEW ENTRY IS OPENED.** ### What the block
### records is one thing: the standing clause that entry imposes -- *a banked value of the archimedean remainder is
### quotable only with its convention named* -- now has a MECHANICAL TEST, and the test's measured resolving power
### is stated beside it. ### **NO BANKED NUMBER IS CALLED WRONG AND NO CONVENTION IS CALLED CORRECT.**
### ### Every figure is read from `b346_rate.json`; nothing is typed from memory of a run.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
ERRATA = os.path.join(PP, 'ERRATA.md')
MARK = '<!-- b346 -->'
ENTRY = 'E-2026-09-03-1'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def blob():
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:ERRATA.md'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def block(R):
    rate = R['rate']
    cells = ', '.join(str(c) for c in rate['cells'])
    return [
        '', MARK, '',
        '### CONSEQUENCE OF THE STANDING CLAUSE OF `%s` — filed 2026-09-06 (b346): the clause now has a mechanical test' % ENTRY,
        '',
        ('*The entry above is not edited and no new entry is opened. This block records one thing: the standing clause '
         'that entry imposes can now be applied to a banked value **without reading the code that produced it**.*'),
        '',
        ('**The clause.** *A banked value of the archimedean remainder — `eps`, `eps_even`, `E2`, or any quantity computed '
         'through them — is quotable only with its convention named.* Until now, naming the convention meant reading the '
         'instrument that produced the value: the corpus\'s own applies `r ** -0.5`, the source\'s object carries '
         '`r ** +0.5`, and **the two functions differ by a factor of `ρ`, which is not a scalar** — this entry\'s own '
         'sentence.'),
        '',
        ('**The test.** Because the two functions differ by exactly that factor, their decay exponents along the argument '
         '`ρ` differ by exactly `1.0` — **a separation that is exact by construction and is not a measurement**. b346 '
         'measured the other half: the instrument\'s own uncertainty in that exponent, on the cells b264\'s second axis '
         'marked converged (`ρ = %s`) and on no others. The uncertainty is **`%.6e`**, so the resolving power is '
         '**`%.1f`**, and by b322\'s rule the axis RESOLVES the two conventions. **The convention under which a banked '
         '`eps`-derived value was computed is therefore recoverable from that value\'s own decay.** Applied to the '
         'banked column itself: the local slope at the top of the converged window is `%.9f`, which sits `%.3e` from '
         'the corpus\'s asymptote and `%.3e` from the source\'s — **the banked values carry the corpus\'s own '
         '`r ** -0.5`**, read from the values and from nothing else.'
         % (cells, R['uncertainty'], R['resolving_power'], R['slope_top'], R['d_corpus'], R['d_source'])),
        '',
        ('**What this does not do.** It does not make either convention correct. b312 decided which function the corpus\'s '
         'remainder is **by unfolding definitions**, and b313\'s clause governs: *the exponent is fixed by the source\'s '
         'own definition of the object the corpus imported, and by nothing the residue does* — **and a rate is not a vote '
         'on that either**. This entry already states the banked convention *from the code*; b346 reaches the same '
         'statement *from the values*, by an independent route, and that is the whole of what is added. **No banked number '
         'is called wrong, no act is re-verdicted, and no grade moves.**'),
        '',
        ('*Two limits are carried with the test rather than left implicit. The two evaluators share the prolate layer and '
         'the node counts — a shared engine is a shared error source, and independence of the prolate solver is not '
         'certified. And one of b346\'s own sealed uncertainty arms did no work: a two-point drift-zero is algebraically '
         'the local slope of those two points, so the second estimator collapsed onto the first; b346 tabled that rather '
         'than repairing it, and bounded the understatement by a diagnostic — the whole-window spread gives a resolving '
         'power of `%.1f`, so the verdict clears both readings.*' % rate['resolving_whole']),
        '',
        '*Filed by b346 (relay `data/b346_the_exponent_by_rate.txt`). No deposited artifact is affected.*',
    ]


def main():
    R = json.load(io.open(os.path.join(D, 'b346_rate.json'), encoding='utf-8'))
    rec('=' * 100)
    rec("b346_filings.py -- THE ERRATUM'S CONSEQUENCE CLAUSE. ### APPEND-ONLY, AND ONLY IF THE VERDICT IS RESOLVED.")
    rec('=' * 100)
    rec('  the verdict as the instrument printed it : %s' % R['verdict'])
    if R['verdict'] != 'RESOLVED':
        rec('  ### ### **THE CLAUSE DOES NOT FIRE. ### NOTHING IS WRITTEN IN THE PAPERS REPO AT ALL.**')
        rec('  ### section (E): the figure is carried in this act\'s bank in the rate\'s units and no file moves.')
        st, det, wrote = 'NOT FIRED', 'the verdict is not RESOLVED', []
    else:
        txt = io.open(ERRATA, encoding='utf-8').read()
        if MARK in txt:
            st, det, wrote = 'DUPLICATE', 'mark %s already present -- REFUSED, nothing written' % MARK, []
        elif ('## %s' % ENTRY) not in txt:
            st, det, wrote = 'REFUSED', 'the named entry %s is not in the file' % ENTRY, []
        else:
            hb = blob()
            before = txt
            body = block(R)
            io.open(ERRATA, 'w', encoding='utf-8', newline=chr(10)).write(
                before.rstrip(chr(10)) + chr(10) + chr(10).join(body) + chr(10))
            after = io.open(ERRATA, encoding='utf-8').read()
            pw = after.startswith(before.rstrip(chr(10)))
            pb = (hb is not None) and after.startswith(hb.rstrip(chr(10)))
            # ### THE ENTRY ITSELF MUST BE BYTE-IDENTICAL: its text from its heading to the next heading is unchanged.
            def entry_text(s):
                i = s.index('## %s' % ENTRY)
                j = s.find(chr(10) + '## ', i + 1)
                return s[i:j if j > 0 else len(s)]
            same_entry = entry_text(after) == entry_text(before)
            ok = after.count(MARK) == 1 and pw and pb and same_entry
            st = 'WRITTEN' if ok else 'READ-BACK FAILED'
            det = ('mark %d time(s); append-only working=%s blob=%s; the named entry byte-identical=%s'
                   % (after.count(MARK), pw, pb, same_entry))
            wrote = ['ERRATA.md'] if ok else []
        rec('  ERRATA.md : %s -- %s' % (st, det))
    rec('  ### PLACE-papers files written this run : %d (CAP 1)' % len(wrote))
    rec('=' * 100)
    p, k = os.path.join(D, 'b346_filings_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b346_filings_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b346_filings.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(errata=st, detail=det, mark=MARK, entry=ENTRY, wrote=wrote, verdict=R['verdict'],
             run_file=os.path.basename(p)), indent=1))
    return 0 if st in ('WRITTEN', 'DUPLICATE', 'NOT FIRED') else 1


if __name__ == '__main__':
    sys.exit(main())
