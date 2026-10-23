# -*- coding: utf-8 -*-
"""b708_report.py -- THE FOUR REPORT LINES THE FERRY`S COMPONENT 6 NAMES, EACH WITH ITS BANK, WRITTEN AFTER THE AUTHOR`S WORD AT THE ROOT (b708).

### data/b708_rules.txt row (1): an act`s closing report tool is not among the tools sealed at Component 5; it is written by the Write tool after
### the author`s word at the root`s prompt names the report`s lines, run before the act root is computed so that the root names its bank, and the
### sealed closing tool prints the report`s lines from that bank. The author`s word at the root (data/b708_citation_check.txt, the check of
### 2026-10-23T17:52:13Z): "Root: 1, compute the root now. The unsealed report tool written and run with the ferry`s four lines (the probe`s moved
### sigs, the 11 mentions, the cut`s distances, the four figures beside b707`s), its bank among the root`s banks". Each line is read from its TEXT
### bank by the row`s own figures; no compressed bank is opened here. UNSEALED: tools/b708_worklist.py SEALED names no report tool.
### Writes data/b708_report.txt and data/b708_report.json and nothing else.
"""
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def need(m, k=1):
    return m.group(k) if m else '### NOT READ'


def main():
    pc = rd('b708_probe_compare.txt')
    m1 = re.search(r'CELLS COMPARED (\d+) ; EQUAL (\d+) ; DIFFERING (\d+) ; SIGS MOVED (\d+) (\[[^\]]*\])? ?; THE PAGE ([A-Z ]+)', pc)
    pr = rd('b708_probe_run.txt')
    m1b = re.search(r'RUN (\d+) \(probe\) ; CONCLUSION (\w+) ; THE PROBE ARTIFACT (\w+) ; THE STEP (RAN|### NOT RUN) ; ERROR LINES (\d+) ; PROBE CELLS (\d+) OF (\d+) ; MISSING (\d+)', pr)
    line1 = ('the probe`s moved sigs (relay data/b708_probe_compare.txt, the probe of run %s through the workflow`s step at v0.37 against b704`s probe bank, cell by cell): '
             'cells compared %s, equal %s, differing %s, sigs moved %s%s; the page %s; the step %s, %s of %s cells read, %s missing (relay data/b708_probe_run.txt)' % (
                 need(m1b, 1), need(m1, 1), need(m1, 2), need(m1, 3), need(m1, 4), (' ' + m1.group(5)) if (m1 and m1.group(5)) else '', need(m1, 6).strip().lower(),
                 need(m1b, 4), need(m1b, 6), need(m1b, 7), need(m1b, 8)))
    cr = rd('b708_cells_reread.txt')
    m2 = re.search(r'MENTIONS (\d+) ; EQUAL (\d+) \((\d+) CARRIED FROM b706, (\d+) RE-READ THIS ACT\) ; DIFFERS (\d+) ; UNBANKED (\d+) \(no kernel and no tag named (\d+)\)', cr)
    rows = [l.strip() for l in cr.split(NL) if l.startswith('  ') and ' | tag ' in l]
    line2 = ('the 11 mentions` readings (relay data/b708_cells_reread.txt, the two unbanked mentions of b706`s reach bank re-read against the entry-tag print at v0.17, '
             'data/b708_prints_v0.17.txt, the nine b706 read equal carried): mentions %s, equal %s (%s carried, %s re-read this act), differs %s, unbanked %s (no kernel and '
             'no tag named by the line: %s) -- %s' % (need(m2, 1), need(m2, 2), need(m2, 3), need(m2, 4), need(m2, 5), need(m2, 6), need(m2, 7),
                                                      ' ; '.join(r.split(' | ')[0] + ' :' + r.split(' | ')[1].split(' :')[-1] + ' ' + r.split(' | ')[-1] for r in rows)))
    ct = rd('b708_cut.txt')
    m3 = re.search(r'THE DISTANCE BY THE b670 METHOD: BEFORE (\d+), AFTER (\d+) ; ROWS APPLIED (\d+) ; HELD (\d+) \(CORRESPONDENCE CELLS\) ; QUOTING LINES (\d+) ENTERED AS RESIDUES', ct)
    m3b = re.search(r'THE CONTROL, THE MATCHES ROWS: (\d+) at the base ; standing now (\d+) ; no longer standing (.*)$', ct, re.M)
    line3 = ('the cut`s distances (relay data/b708_cut.txt, day1/Spectral_Inertness.md by the b670 method, each non-MATCHES row`s STATED text searched at the base and now): '
             'before %s, after %s; rows applied %s, held %s (the Correspondence cells); the MATCHES rows %s at the base and %s standing now, lost %s; the quotation search '
             'before the cut`s commit entering %s quoting lines as residues (relay data/b708_quote.txt)' % (
                 need(m3, 1), need(m3, 2), need(m3, 3), need(m3, 4), need(m3b, 1), need(m3b, 2), need(m3b, 3), need(m3, 5)))
    figs = rd('b708_standing_figures.txt')
    fr = dict((k, (a_, b_)) for k, a_, b_ in re.findall(r'^  (correspondence|readme|partners|pins)\s+b708 (\S+) ; b707 (\S+) ;', figs, re.M))
    line4 = ('the four standing arms` figures beside b707`s (relay data/b708_standing_figures.txt, by tools/b706_standing_figures.py over b706`s roster against '
             'data/b707_standing_figures.json): %s' % ' ; '.join('%s %s (b707 %s)' % (k, fr.get(k, ('-', '-'))[0], fr.get(k, ('-', '-'))[1])
                                                                for k in ('correspondence', 'readme', 'partners', 'pins')))
    L = ['%s -- THE FOUR REPORT LINES THE FERRY`S COMPONENT 6 NAMES, EACH WITH ITS BANK, BY THE UNSEALED REPORT TOOL AFTER THE AUTHOR`S WORD AT THE ROOT (%s)' % ('b708', utc()), '',
         '### rows are the four lines (the ferry`s Component 6; the author`s word at the root`s prompt, data/b708_citation_check.txt, the check of 2026-10-23T17:52:13Z),',
         '### each read from its text bank by this unsealed tool (data/b708_rules.txt row (1)); the sealed closing prints them from this bank.', '',
         '  (1) ' + line1, '  (2) ' + line2, '  (3) ' + line3, '  (4) ' + line4, '',
         '### ### **LINES 4 ; SIGS MOVED %s OF %s ; MENTIONS %s, EQUAL %s, DIFFERS %s, UNBANKED %s ; THE DISTANCE %s TO %s ; THE FIGURES %s AGAINST b707`S %s.**' % (
             need(m1, 4), need(m1, 1), need(m2, 1), need(m2, 2), need(m2, 5), need(m2, 6), need(m3, 1), need(m3, 2),
             ', '.join('%s %s' % (k, fr.get(k, ('-', '-'))[0]) for k in ('correspondence', 'readme', 'partners', 'pins')),
             ', '.join(fr.get(k, ('-', '-'))[1] for k in ('correspondence', 'readme', 'partners', 'pins')))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b708_report.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    j = dict(at=utc(), lines=[line1, line2, line3, line4], moved=need(m1, 4), compared=need(m1, 1), mentions=dict(n=need(m2, 1), equal=need(m2, 2), differs=need(m2, 5), unbanked=need(m2, 6)),
             distance=dict(before=need(m3, 1), after=need(m3, 2)), figures=fr)
    pj = os.path.join(D, 'b708_report.json')
    with open(pj + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj + '.tmp', pj)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
