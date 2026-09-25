# -*- coding: utf-8 -*-
"""b525_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b525_record.py components | desk | trail`
### Every figure READ from the banks, not retyped; the scores are READINGS (1), (5) and (6)'s, read off the written section.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


FO = json.loads(read('b525_fold.json') or '{}')
LOG = read('b525_run_log.txt')
w = lambda v: 'HELD' if v else 'REFUTED'


def section():
    t = io.open(FIND, encoding='utf-8').read()
    i = t.index(FO['heading'])
    return t[i:]


def wo_rows(sec):
    return [l for l in sec.split(NL) if l.startswith('| `W-ORD-')]


def scores():
    sec = section()
    rows = wo_rows(sec)
    xi = [r for r in rows if r.startswith('| `W-ORD-XI-P7`')]
    wc = [r for r in rows if r.startswith('| `W-ORD-WEIL-CONVERSE`')]
    first_check = LOG.split('### tools/b525_fold.py write')[0]
    return dict(
        n1=FO['span']['lo'] == 517 and FO['span']['hi'] == 524 and FO['span']['acts'] == 8,
        n2=FO['columns']['OBJECT'] == 0,
        n3=len(xi) == 1 and len(wc) == 1 and '(f)(i) = f1 DONE' in wc[0] and 'f2, f3, f4 OPEN' in wc[0],
        s1='**CHECK : PASS**' in first_check and first_check.count('**CHECK :') == 1,
        s2=sum(d['n'] for d in FO['defects']) == 30,
        s3=sec.split('### The three columns')[0].count('*BORDERLINE --') == 4)


def components():
    L = ['=' * 132, 'b525 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE RUN LOG (check, then write):'] + LOG.rstrip(NL).split(NL)
    L += ['', '### THE SECTION AS WRITTEN TO FINDINGS.md:'] + section().rstrip(NL).split(NL) + ['=' * 132]
    io.open(os.path.join(D, 'b525_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b525 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- the fold`s span b%d-b%d, %d acts ; the tool reads %d through this filing act.'
         % (w(sc['n1']), FO['span']['lo'], FO['span']['hi'], FO['span']['acts'], FO['span']['tool_reads']),
         '  **(N2)** ### **%s.** -- columns : %s.' % (w(sc['n2']), FO['columns']),
         '  **(N3)** ### **%s.** -- the section`s work-order rows : %s.' % (w(sc['n3']), [r[:60] for r in wo_rows(section())]),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the check at its first run.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- defects of the span : %d.' % (w(sc['s2']), sum(d['n'] for d in FO['defects'])),
         '  **(S3)** ### **%s.** -- rows with the control-function borderline : %d.'
         % (w(sc['s3']), section().split('### The three columns')[0].count('*BORDERLINE --')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b525_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b525_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b525_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b525 — the witness arc folded, b517–b524; (R135) entered'


def trail():
    sc = scores()
    body = [
        '', HEADING, '',
        '**(R135) ratified.** (1) b524 is entered: (f)(i) proved on variant (B) for every real C⁴ compactly supported φ, each of',
        '(i)–(iii) DERIVES by statement-read; the (f) hypothesis a `Prop` with G the integral. **The kernel\'s named instance is',
        'Mathlib\'s smooth bump; the measured window is an order-7 B-spline; the theorems cover both and the instances differ.**',
        '(2) The fold ran as this act. (3) The order after it is (a) — one numerical act closing `W-ORD-XI-P7` and the',
        'instance discrepancy together, ξ re-read at order 7 on b520\'s widths and both objects re-read on the kernel\'s',
        'smooth-bump φ — then (b), the kernel lane for (f)(ii) on the kernel\'s instance. (4) The B-spline is not constructed',
        'in the kernel.',
        '',
        '**The fold.** `FINDINGS.md` gains **%s** and the digest one block, both appended, prefixes proved: %d verdict strings'
        % (FO['heading'].lstrip('# '), len(FO['quotes'])),
        'matched in their own closings, %d rulings (R126)–(R135) in their ferries, %d defects of the span counted; columns'
        % (sum(r['found'] for r in FO['rulings']), sum(d['n'] for d in FO['defects'])),
        'OBJECT %d, MODEL %d, RECORD %d; the errors block carries (R130)(2)\'s refuted growth claim, (R133)(2)\'s form of words as'
        % (FO['columns']['OBJECT'], FO['columns']['MODEL'], FO['columns']['RECORD']),
        '(R134) corrected it, and (R135)(1)\'s instance discrepancy; the work-orders `W-ORD-XI-P7` (OPEN) and',
        '`W-ORD-WEIL-CONVERSE` ((d) and f1 DONE, f2, f3, f4 OPEN); the host-stop rule filed.',
        '**By this act\'s note, beside the section\'s one statement (appended there, not edited): the numbers it cites were taken',
        'on the order-7 B-spline window and the theorems it cites are proved for every C⁴ φ, the kernel\'s named instance being',
        'the smooth bump — the instances differ.**',
        '',
        '**(N1) %s · (N2) %s · (N3) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. Nothing compiled; nothing at Zenodo'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'written; nothing deposits; no grade conferred; no ERRATA line; row U1 unedited; `h2` where the deposit left it; the',
        'four lists stay OPEN; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b525_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
