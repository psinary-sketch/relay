# -*- coding: utf-8 -*-
"""b707_report_root.py -- THE FOUR REPORT LINES THE AUTHOR`S WORD AT THE ROOT NAMES, EACH WITH ITS BANK (b707, the ferry`s Component 6).

### The author`s word at the root`s prompt (data/b707_citation_check.txt, the check of 2026-10-23T03:34:48Z): "The closing`s report prints, each
### in one line with its bank: the onset radius with its eigenvalue and the rung beside it, the zeta control`s least eigenvalue at the same
### radii, the port`s modules built of 15 and the next failing line, and the four standing arms` figures beside b706`s." The sealed
### tools/b707_report.py (sealed before the word, relay data/b707_seal_hashes.json) prints five lines of its own form and takes no edit after
### the seal; this tool, UNSEALED and written by the Write tool after the word (b706`s form: its report tool was written after b706`s root
### answer), prints the four lines the word names, each from its TEXT bank by the row`s own figures -- no compressed bank is opened here.
### Written before the root so that the root names its banks; the sealed closing prints the sealed report`s five lines and the event in the
### defects bank names this bank.
### Writes data/b707_report_root.txt and data/b707_report_root.json and nothing else.
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

LADDER = ['log2', '32', '48', '64', '96', '128', '192']
ROW = re.compile(r'^  (band|rho0) \| (\S+)\s+\| a (\S+) \+- (\S+) \| .*?\| lambda (\S+) \+- (\S+), (\S+) \+- (\S+) \| ([A-Z ]+?BEYOND ITS BOUND)', re.M)


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def rows_of(text):
    """{(frequency, rung): dict(a, a_err, lmin, lmin_err, reading)} from a bank whose rows are rungs."""
    out = {}
    for m in ROW.finditer(text):
        out[(m.group(1), m.group(2))] = dict(a=m.group(3), a_err=m.group(4), lmin=m.group(5), lmin_err=m.group(6), reading=m.group(9).strip())
    return out


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def main():
    on, ctl = rd('b707_onset.txt'), rd('b707_onset_controls.txt')
    q0, zeta = rows_of(on), rows_of(ctl)
    astar = dict(re.findall(r'^  (band|rho0) \| negative at .*? ; a\* = (\S+) \(', on, re.M))
    names = dict(band='the band zero`s family (gamma_0 = 29.5517...)', rho0='rho_0`s family (gamma_0 = 16.2902...)')
    l1, l2, j1, j2 = [], [], {}, {}
    for fq in ('band', 'rho0'):
        a = astar.get(fq)
        i = LADDER.index(a) if a in LADDER else -1
        beside = LADDER[i - 1] if i > 0 else None
        r, rb = q0.get((fq, a), {}), q0.get((fq, beside), {}) if beside else {}
        z, zb = zeta.get((fq, a), {}), zeta.get((fq, beside), {}) if beside else {}
        l1.append('%s: a* = %s (a = %s +- %s), lambda_min %s +- %s (the L2 metric; %s); the rung beside it %s (a = %s), lambda_min %s +- %s (%s)' % (
            names[fq], a, r.get('a', '-'), r.get('a_err', '-'), r.get('lmin', '-'), r.get('lmin_err', '-'), r.get('reading', '-'),
            beside or 'NONE', rb.get('a', '-'), rb.get('lmin', '-'), rb.get('lmin_err', '-'), rb.get('reading', '-')))
        l2.append('%s: at a* = %s lambda_min %s +- %s (%s); at %s lambda_min %s +- %s (%s)' % (
            names[fq], a, z.get('lmin', '-'), z.get('lmin_err', '-'), z.get('reading', '-'), beside or 'NONE', zb.get('lmin', '-'), zb.get('lmin_err', '-'), zb.get('reading', '-')))
        j1[fq] = dict(a_star=a, a=r.get('a'), lmin=r.get('lmin'), lmin_err=r.get('lmin_err'), reading=r.get('reading'), beside=beside, beside_a=rb.get('a'),
                      beside_lmin=rb.get('lmin'), beside_reading=rb.get('reading'))
        j2[fq] = dict(a_star=a, lmin=z.get('lmin'), lmin_err=z.get('lmin_err'), reading=z.get('reading'), beside=beside, beside_lmin=zb.get('lmin'),
                      beside_reading=zb.get('reading'))
    line1 = ('the sign-onset radius at Q0 on the family span{C, N} with its least eigenvalue and the rung beside it (relay data/b707_onset.txt, the rows '
             'by rung): %s' % ' ; '.join(l1))
    line2 = ('the zeta control`s least eigenvalue at the same radii (relay data/b707_onset_controls.txt, C1: the zeta form on the same family, '
             'every rung POSITIVE DEFINITE BEYOND ITS BOUND): %s' % ' ; '.join(l2))
    port = rd('b707_port.txt')
    blog = rd('b707_buildlog_SIDE-lv-conservation_port.txt').split(NL)
    built = re.search(r'modules built (\d+) of (\d+): \[(.*?)\]', port)
    files15 = re.search(r'files built (\d+) of (\d+)', port)
    errs = [l.strip() for l in port.split(NL) if l.strip().startswith('error: SIDELvConservation/')]
    first = errs[0] if errs else '### NO ERROR LINE READ'
    beside_err = next((e for e in errs if ':380:' in e), None)

    def at(e):
        return next((i + 1 for i, l in enumerate(blog) if e and l.strip() == e), None)
    line3 = ('the port`s modules built of 15 and the next failing line (relay data/b707_port.txt; the build log data/b707_buildlog_SIDE-lv-conservation_port.txt): '
             'built %s of the 15 .lean files at 93c27ec (%s of the %s modules: %s), the print step not run, no grade claimed; the next failing line %s '
             '(build.log :%s)%s' % (files15.group(1) if files15 else '-', built.group(1) if built else '-', built.group(2) if built else '-',
                                    built.group(3).replace("'", '') if built else '-', first, at(first),
                                    ('; beside it %s (build.log :%s)' % (beside_err, at(beside_err))) if beside_err else ''))
    figs = rd('b707_standing_figures.txt')
    fr = dict((k, (a_, b_)) for k, a_, b_ in re.findall(r'^  (correspondence|readme|partners|pins)\s+b707 (\S+) ; b706 (\S+) ;', figs, re.M))
    line4 = ('the four standing arms` figures beside b706`s (relay data/b707_standing_figures.txt, by tools/b706_standing_figures.py over b706`s roster; '
             'data/b706_standing_figures.json): %s' % ' ; '.join('%s %s (b706 %s)' % (k, fr.get(k, ('-', '-'))[0], fr.get(k, ('-', '-'))[1])
                                                                for k in ('correspondence', 'readme', 'partners', 'pins')))
    L = ['%s -- THE FOUR REPORT LINES THE AUTHOR`S WORD AT THE ROOT NAMES, EACH WITH ITS BANK (%s)' % ('b707', utc()), '',
         '### rows are the four lines the author`s word at the root`s prompt names (data/b707_citation_check.txt, the check of 2026-10-23T03:34:48Z),',
         '### each read from its text bank by this unsealed tool; the sealed report (data/b707_report.txt) prints its five lines beside.', '',
         '  (1) ' + line1, '  (2) ' + line2, '  (3) ' + line3, '  (4) ' + line4, '',
         '### ### **LINES 4 ; THE ONSET a* %s (band; lambda_min %s), %s (rho_0; lambda_min %s) ; THE ZETA CONTROL lambda_min %s, %s AT THE SAME RADII ; '
         'THE PORT %s OF 15 FILES BUILT, THE NEXT FAILING LINE build.log :%s ; THE FIGURES %s.**' % (
             j1['band']['a_star'], j1['band']['lmin'], j1['rho0']['a_star'], j1['rho0']['lmin'], j2['band']['lmin'], j2['rho0']['lmin'],
             files15.group(1) if files15 else '-', at(first), ', '.join('%s %s' % (k, fr.get(k, ('-', '-'))[0]) for k in ('correspondence', 'readme', 'partners', 'pins')))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b707_report_root.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    j = dict(at=utc(), lines=[line1, line2, line3, line4], onset=j1, zeta=j2, port=dict(files_built=files15.group(1) if files15 else None, modules_built=built.group(1) if built else None,
                                                                                      next_failing=first, next_failing_line=at(first), beside=beside_err, beside_line=at(beside_err)),
             figures=fr)
    pj = os.path.join(D, 'b707_report_root.json')
    with open(pj + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj + '.tmp', pj)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
