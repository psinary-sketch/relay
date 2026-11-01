# -*- coding: utf-8 -*-
"""standing/pricebank.py -- v1.11.0, THE PRICE BANK'S MEASURED ROW BESIDE EACH ESTIMATE, WHEN A FIELD LANDS, IN I-10'S FORM: a lower bound on a specified implementation, re-measured after the build.
A rooted bank is not edited, so the measured rows stand in data/<act>_price_measured.txt, each beside the estimate it answers, quoted with its bank and line; the next field's act reads them from there.
Written at b731 by the Write tool.

  measured(field, implementation, lines, runs)            a measured row: the lines read from the tree, the runs by id; refused with no run or no lines
  ratio(row, est_lines, est_disp)                         the row beside its estimate, the two ratios each low-high
  reprice(est_lines, est_disp, r)                         an estimate read by a measured ratio, the dispatches rounded out
  rows_text(rows)                                         the bank's table
  v1.12.0, (R342)(2)(ii): estimates(text), measured_rows(text), reprice_read(price_text, measured_text, field, by): the re-price read from the banks, no hand arithmetic
  python -X utf8 tools/standing/pricebank.py reprice <field> <by> <measured-bank>     prints it; the price bank data/b729_count_price.txt
Pure in its arguments; the act's tool writes the bank.
"""
import math
import os
import re
import sys

FORM = 'I-10`s form: a lower bound on a specified implementation, re-measured after the build; a floor on that one route and no estimate of another'


def measured(field, implementation, lines, runs):
    if not lines or not runs:
        raise ValueError('pricebank: %s: a measured row wants its lines read from the tree and its runs by id' % field)
    return dict(field=field, implementation=implementation, lines=int(lines), dispatches=len(runs), runs=list(runs))


def ratio(row, est_lines, est_disp):
    """(lines low, lines high, dispatches low, dispatches high): measured over the estimate's top and bottom."""
    return (row['lines'] / est_lines[1], row['lines'] / est_lines[0], row['dispatches'] / est_disp[1], row['dispatches'] / est_disp[0])


def reprice(est_lines, est_disp, r):
    """the estimate by the ratio, low by low and high by high; dispatches rounded out to whole runs, at least one."""
    return (int(est_lines[0] * r[0]), int(math.ceil(est_lines[1] * r[1])), max(1, int(math.floor(est_disp[0] * r[2]))), max(1, int(math.ceil(est_disp[1] * r[3]))))


EST_ROW = re.compile(r'(?m)^  (\w+)\s+\S.*?\s(\d[\d,]*-\d[\d,]*)(?: \([^)]*\))?\s+(\d+-\d+)\s+(\d+-\d+)\s*$')
MEAS_ROW = re.compile(r'(?m)^  (\w+)\s+(\d+-\d+)\s+(\d+-\d+)\s+(\d+)\s+(\d+)\s+[\d.]+-[\d.]+ ; [\d.]+-[\d.]+\s+\S')
PRICE_BANK = 'data/b729_count_price.txt'


def _pair(s):
    a, b = s.replace(',', '').split('-')
    return int(a), int(b)


def estimates(text):
    """v1.12.0, (R342)(2)(ii): the price bank's table of fields: {field: (est_lines, est_disp)}, read from its rows."""
    return dict((m.group(1), (_pair(m.group(2)), _pair(m.group(3)))) for m in EST_ROW.finditer(text))


def measured_rows(text):
    """the measured bank's rows: {field: (est_lines, est_disp, lines, dispatches)}, read from its table."""
    return dict((m.group(1), (_pair(m.group(2)), _pair(m.group(3)), int(m.group(4)), int(m.group(5)))) for m in MEAS_ROW.finditer(text))


def reprice_read(price_text, measured_text, field, by):
    """the re-price from the two banks alone, no figure typed: `field`'s estimate read by the ratio of `by`'s measured row beside `by`'s own estimate. A field or row the banks lack raises."""
    est, mea = estimates(price_text), measured_rows(measured_text)
    if field not in est or by not in mea:
        raise ValueError('pricebank: %s or %s not in the banks: estimates %s, measured %s' % (field, by, sorted(est), sorted(mea)))
    el, ed, lines, disp = mea[by]
    r = ratio(dict(lines=lines, dispatches=disp), el, ed)
    return reprice(est[field][0], est[field][1], r)


def rows_text(rows):
    """rows: dict(field, est_lines, est_disp, source, row): one line a field, estimate beside measured, the ratio printed."""
    L = ['  %-16s %-14s %-11s %-9s %-11s %-30s %s' % ('field', 'est lines', 'est disp', 'lines', 'dispatches', 'ratio lines ; dispatches', 'the estimate`s source')]
    for x in rows:
        r = ratio(x['row'], x['est_lines'], x['est_disp'])
        L.append('  %-16s %-14s %-11s %-9d %-11d %-30s %s' % (x['field'], '%d-%d' % x['est_lines'], '%d-%d' % x['est_disp'], x['row']['lines'], x['row']['dispatches'],
                                                             '%.3f-%.3f ; %.3f-%.3f' % r, x['source']))
    return L


if __name__ == '__main__':
    if len(sys.argv) != 5 or sys.argv[1] != 'reprice':
        sys.exit(__doc__)
    ROOT_ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    def rd_(rel):
        with open(os.path.join(ROOT_, rel), encoding='utf-8') as f:
            return f.read()
    print('%s by %s`s measured ratio: %d-%d lines, %d-%d dispatches (read from %s and %s)' % ((sys.argv[2], sys.argv[3]) + reprice_read(rd_(PRICE_BANK), rd_(sys.argv[4]), sys.argv[2], sys.argv[3]) + (PRICE_BANK, sys.argv[4])))
