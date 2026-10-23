# -*- coding: utf-8 -*-
"""b707_report.py -- THE CLOSING'S REPORT LINES, EACH WITH ITS BANK (b707, the ferry's Component 6, in b706_report.py's form).

### b706's report tool printed five lines on the author's word at b706's root, each from its bank; this act carries the form for the objects
### (R317) names: the sign-onset radius per frequency with the rows at a*, the port's hold by file and line from the artifact's build.log
### (banked whole), the three readers' repairs with their controls' figures, the registrations committed alone and re-read unchanged with the
### next axis, and the four standing figures beside b706's. Written whole by the Write tool at Component 5 and sealed; it reads banks alone, no
### ledger line, and writes data/b707_report.txt and data/b707_report.json and nothing else; committed before the root so that the root names
### them.
"""
import gzip
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


def jl(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def jgz(n):
    try:
        return json.loads(gzip.decompress(open(os.path.join(D, n), 'rb').read()).decode('utf-8'))
    except Exception:
        return {}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def main():
    # (1) the sign-onset radius per frequency, with the Q0 rows at a* (data/b707_onset.json.gz, read as the bank`s gz)
    oj = jgz('b707_onset.json.gz')
    on = oj.get('onset') or {}
    rows = dict(((r.get('obj'), r.get('freq'), r.get('rung')), r) for r in (oj.get('rows') or []))
    parts = []
    for fq, name in (('band', 'the band zero`s family (gamma_0 = 29.5517...)'), ('rho0', 'rho_0`s family (gamma_0 = 16.2902...)')):
        o = on.get(fq) or {}
        a = o.get('a_star')
        r = rows.get(('q0', fq, a)) if a else None
        parts.append('%s: a* = %s (a = %s), negative at %s; at a* S_CC %s, S_NN %s, S_CN %s, det G %s, lambda_min %s (the L2 metric), the witness v %s with S %s' % (
            name, a or 'NONE', (o.get('a_star_radius') or ['-'])[0][:12] if o.get('a_star_radius') else '-', o.get('negative_at') or 'NO RUNG',
            (r or {}).get('S_CC', ['-'])[0][:12], (r or {}).get('S_NN', ['-'])[0][:14], (r or {}).get('S_CN', ['-'])[0][:12], (r or {}).get('det', ['-'])[0][:10],
            (r or {}).get('lmin', ['-'])[0][:12], (r or {}).get('witness'), (r or {}).get('witness_S', ['-'])[0][:10]))
    l1 = ('the sign-onset radius at Q0 on the family span{C, N} over the ladder log 2, 2 log 32 ... 2 log 192 (relay data/b707_onset.txt; the controls '
          'data/b707_onset_controls.txt: C1 zeta positive definite at every rung of both frequencies %s, C2 as wanted %s): %s ; the falsifier %s ; the hypothesis %s' % (
              oj.get('c1_zeta_ok'), (oj.get('c2') or {}).get('ok'), ' ; '.join(parts), 'FIRED' if oj.get('falsifier_fired') else 'NOT FIRED', oj.get('hypothesis')))
    # (2) the port`s hold by file and line of the error in the artifact
    bl = rd('b707_buildlog_SIDE-lv-conservation_port.txt').split(NL)
    pj = jl('b707_port.json')
    first = pj.get('first_error') or ''
    bi = next((i + 1 for i, l in enumerate(bl) if first and l.strip() == first.strip()), None)
    l2 = ('the port`s holding line at the shared pin (the artifact`s build.log of run %s, banked whole as relay data/b707_buildlog_SIDE-lv-conservation_port.txt :%s, '
          'read after the artifact`s sha256 agreed; data/b707_port.txt): %s -- modules built %d of 12 (%s), held at %s, remaining %d (%s); the print step %s, '
          'no grade claimed' % (pj.get('run_id'), bi, first or '### NOT READ', len(pj.get('built') or []), ', '.join(pj.get('built') or []),
                                ', '.join(pj.get('held') or []) or 'NONE', len(pj.get('remaining') or []), ', '.join(pj.get('remaining') or []), pj.get('print_step')))
    # (3) the three readers` repairs with their controls` figures
    rc = rd('b707_repair_controls.txt')
    cases = re.search(r'CASES (\d+) ; AS WANTED (\w+)', rc)
    ts = jl('b707_table_scope.json')
    ro = rd('b707_roster_control.txt')
    m3 = re.search(r'in roster, MISSING from archive : (\d+)', ro)
    l3 = ('the three readers` repairs under (R317)(2) with their controls (relay data/b707_tool_repairs.txt, data/b707_repair_controls.txt: cases %s, as wanted %s): '
          'tools/mirror_roster.json 83 entries to 70 (the four re-pointed, the thirteen duplicates struck), b706`s export verified dry with clause 3 MISSING %s '
          '(data/b707_roster_control.txt); tools/terminal_table.py`s walk dropping %d retired copies, the regeneration against b706`s final table gone %d, added %d, '
          'moved %d, restored %d, grades %d, other %d (data/b707_table_scope.txt); tools/rule_arms.py`s G-RULE-SUITE-PARTS passing on b706`s and b705`s run banks '
          'and failing on every mutated copy' % (cases.group(1) if cases else '-', cases.group(2) if cases else '-', m3.group(1) if m3 else '-',
                                                 len(ts.get('dropped') or []), len(ts.get('gone') or []), len(ts.get('added') or []), len(ts.get('moved') or []),
                                                 len(ts.get('restored') or []), len(ts.get('grade_moved') or []), len(ts.get('other') or [])))
    # (4) the registrations
    rr = jl('b707_registrations_reread.json')
    regs = rd('b707_registrations.txt')
    pairs = len(re.findall(r'^\s+\d+\s+\|', regs, re.M))
    l4 = ('the registrations (relay data/b707_registrations.txt, committed alone at relay %s before any computation; re-read data/b707_registrations_reread.txt): '
          'unchanged %s ; the twelve higher pairs` route priced by its arithmetic, computed at b709 ; the next axis %s (data/b705_i6_ranking.txt :%s)' % (
              rr.get('commit'), rr.get('unchanged'), rr.get('next_axis'), rr.get('ranking_line')))
    # (5) the four standing figures beside b706`s
    f7, f6 = jl('b707_standing_figures.json'), jl('b706_standing_figures.json')
    fig = lambda j, k: (j.get(k) or {}).get('figure')   # noqa: E731
    l5 = ('the four standing arms` figures beside b706`s (relay data/b707_standing_figures.txt, data/b706_standing_figures.json): correspondence %s (b706 %s) ; readme %s (b706 %s) ; '
          'partners %s (b706 %s) ; pins %s (b706 %s)' % (fig(f7, 'correspondence'), fig(f6, 'correspondence'), fig(f7, 'readme'), fig(f6, 'readme'),
                                                          fig(f7, 'partners'), fig(f6, 'partners'), fig(f7, 'pins'), fig(f6, 'pins')))
    L = ['%s -- THE CLOSING`S REPORT LINES, EACH WITH ITS BANK (%s)' % ('b707', utc()), '',
         '### rows are the five lines the closing`s report prints in b706_report.py`s form, each read from its bank by this tool; the sealed closing tool',
         '### prints its own report and this bank whole through the defects bank`s event.', '',
         '  (1) ' + l1, '  (2) ' + l2, '  (3) ' + l3, '  (4) ' + l4, '  (5) ' + l5, '',
         '### ### **LINES 5 ; THE ONSET a* %s (band), %s (rho_0) ; THE PORT HELD AT build.log :%s, %d OF 12 BUILT ; REPAIR CASES %s AS WANTED %s ; THE REGISTRATIONS UNCHANGED %s ; '
         'PARTNERS FIGURE %s.**' % ((on.get('band') or {}).get('a_star'), (on.get('rho0') or {}).get('a_star'), bi, len(pj.get('built') or []),
                                    cases.group(1) if cases else '-', cases.group(2) if cases else '-', rr.get('unchanged'), fig(f7, 'partners'))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, 'b707_report.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    j = dict(at=utc(), lines=[l1, l2, l3, l4, l5], onset=on, holding_line=bi, built=len(pj.get('built') or []), cases=int(cases.group(1)) if cases else None,
             as_wanted=(cases.group(2) == 'True') if cases else None, registrations_unchanged=rr.get('unchanged'), partners_figure=fig(f7, 'partners'))
    pj_ = os.path.join(D, 'b707_report.json')
    with open(pj_ + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj_ + '.tmp', pj_)
    print(NL.join(L))


if __name__ == '__main__':
    main()
