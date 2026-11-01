# -*- coding: utf-8 -*-
"""standing/pricebank.py -- v1.11.0, THE PRICE BANK'S MEASURED ROW BESIDE EACH ESTIMATE, WHEN A FIELD LANDS, IN I-10'S FORM: a lower bound on a specified implementation, re-measured after the build.
A rooted bank is not edited, so the measured rows stand in data/<act>_price_measured.txt, each beside the estimate it answers, quoted with its bank and line; the next field's act reads them from there.
Written at b731 by the Write tool.

  measured(field, implementation, lines, runs)            a measured row: the lines read from the tree, the runs by id; refused with no run or no lines
  ratio(row, est_lines, est_disp)                         the row beside its estimate, the two ratios each low-high
  reprice(est_lines, est_disp, r)                         an estimate read by a measured ratio, the dispatches rounded out
  rows_text(rows)                                         the bank's table
Pure in its arguments; the act's tool writes the bank.
"""
import math

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


def rows_text(rows):
    """rows: dict(field, est_lines, est_disp, source, row): one line a field, estimate beside measured, the ratio printed."""
    L = ['  %-16s %-14s %-11s %-9s %-11s %-30s %s' % ('field', 'est lines', 'est disp', 'lines', 'dispatches', 'ratio lines ; dispatches', 'the estimate`s source')]
    for x in rows:
        r = ratio(x['row'], x['est_lines'], x['est_disp'])
        L.append('  %-16s %-14s %-11s %-9d %-11d %-30s %s' % (x['field'], '%d-%d' % x['est_lines'], '%d-%d' % x['est_disp'], x['row']['lines'], x['row']['dispatches'],
                                                             '%.3f-%.3f ; %.3f-%.3f' % r, x['source']))
    return L
