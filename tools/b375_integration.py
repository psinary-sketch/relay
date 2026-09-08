# -*- coding: utf-8 -*-
"""b375_integration.py -- COMPONENT 3: THE INTEGRATION STATE. ### **FOUR COLUMNS, NEVER AVERAGED.**

### ### **(a) WHAT IT SYNTHESIZES ### (b) WHAT IT CITES ### (c) WHAT IT WAITS ON ### (d) WHAT BEARS
### ### ON IT AND IS NOT IN IT.** ### The order forbids averaging them into one status, and
### ### **A SINGLE `INTEGRATION STATUS` WOULD HIDE THE ONLY THING THE FOUR COLUMNS ARE FOR.**
### ### **(a) AND (c) ARE READ FROM THE DOCUMENT'S OWN TEXT AND QUOTED.**
### ### **(b) DISTINGUISHES A NAMED TERMINAL FROM A COUNT**, which is `b372`'s finding made a column.
### ### ### **(d) IS LISTED BY ANCHOR, NEVER SUMMARIZED** -- the order's own words. ### A ledger line
### bears on a keystone when it names one of the keystone's own objects and ### **THE KEYSTONE DOES NOT
### ### NAME THE ACT THAT WROTE IT.**
### ### **WHERE A COLUMN CANNOT BE FILLED FROM THE DOCUMENT'S OWN TEXT IT READS `NOT DETERMINABLE FROM
### ### THE DOCUMENT`, AND NOTHING IS INFERRED TO FILL A CELL.**
### ### **NO KERNEL IS OPENED. ### THE COLUMN RECORDS WHAT THE DOCUMENT NAMES.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import hedge_audit as HA         # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LEDGERS = ['FINDINGS.md', 'FACES_LEDGER.md', 'OPEN_TRAILS.md']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SYNTH = re.compile(r'\b(synthesiz|synthesis|organiz|cross-system|draws together|brings together|'
                   r'consolidat|integrat|against other)\w*', re.I)
WAITS = re.compile(r'\b(owed|open|pending|routed|awaits|awaiting|not yet|outstanding|deferred|'
                   r'unresolved|to be settled|remains open)\b', re.I)
KERNEL = re.compile(r'\b(SIDE-[a-z0-9-]+)\b')
TERMINAL = re.compile(r'`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+|'
                      r'[a-z][a-z0-9_]*_[a-z0-9_]+)`')
COUNT = re.compile(r'(?<![A-Za-z0-9.])(\d{1,5})\s+(?:[a-z-]+\s+){0,2}'
                   r'(terminals?|theorems?|lemmas?|declarations?|prints?)\b', re.I)
ACTNUM = re.compile(r'\bb(\d{2,4})\b')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def col_a(txt):
    sents = [s for s in HA._sentences(txt) if SYNTH.search(s)]
    return sents[:3]


def col_b(txt):
    kern = sorted(set(KERNEL.findall(txt)))
    terms = sorted(set(t for t in TERMINAL.findall(txt) if not t.endswith('.lean')))
    counts = [m.group(0).strip() for m in COUNT.finditer(txt)]
    seen, uc = set(), []
    for c in counts:
        if c not in seen:
            seen.add(c)
            uc.append(c)
    return kern, terms, uc


def col_c(txt):
    return [s for s in HA._sentences(txt) if WAITS.search(s)][:4]


def main():
    rec('=' * 100)
    rec('b375 -- COMPONENT 3: THE INTEGRATION STATE. ### **FOUR COLUMNS, NEVER AVERAGED.**')
    rec('=' * 100)
    rec('')
    pop = json.load(io.open(os.path.join(D, 'b375_population.json'), encoding='utf-8'))
    clus = json.load(io.open(os.path.join(D, 'b375_clusters.json'), encoding='utf-8'))
    rows = {r['file']: r for r in pop['rows']}
    ks = [f for f in rows if rows[f]['order_class'] == 'KEYSTONE']
    where = {}
    for cn, fs in clus['assigned'].items():
        for f in fs:
            where[f] = cn
    rec('  ### keystones by the order`s rubric : %d' % len(ks))
    rec('  ### ### **NO KERNEL IS OPENED. ### COLUMN (b) RECORDS WHAT THE DOCUMENT NAMES, NOT WHETHER')
    rec('  ### ### THE THING NAMED IS THERE** -- that is a check, and this act was not sent to check.')
    rec('')

    # ### the ledger lines, read once.
    led = {}
    for L in LEDGERS:
        p = os.path.join(PP, L)
        try:
            led[L] = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
        except OSError:
            led[L] = []
    rec('  ### the layers read for column (d) : %s' % {k: len(v) for k, v in led.items()})
    rec('')

    out = []
    for f in sorted(ks):
        p = os.path.join(PP, f.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        a = col_a(txt)
        kern, terms, counts = col_b(txt)
        c = col_c(txt)
        # ---- column (d): located by anchor, never summarized -------------------------------------
        objs = set(terms[:40]) | set(kern)
        cn = where.get(f)
        if cn:
            objs.add(cn)
        my_acts = set(ACTNUM.findall(txt))
        anchors = []
        if objs:
            pat = re.compile('|'.join(re.escape(o) for o in sorted(objs, key=len, reverse=True)))
            for L, lines in led.items():
                for i, ln in enumerate(lines, 1):
                    if not pat.search(ln):
                        continue
                    acts = set(ACTNUM.findall(ln))
                    if acts and acts & my_acts:
                        continue          # ### the keystone names that act; it carries it
                    if not acts:
                        continue          # ### an undated line cannot be shown to be uncarried
                    anchors.append(dict(file=L, line=i, acts=sorted(acts)[:3]))
                    if len(anchors) >= 12:
                        break
                if len(anchors) >= 12:
                    break
        rowrec = dict(
            file=f, cluster=(cn or 'UNASSIGNED'),
            a=(a if a else None),
            b=dict(kernels=kern, terminals=terms[:30], counts=counts[:10]),
            c=(c if c else None),
            d=anchors,
            a_state=('read' if a else 'NOT DETERMINABLE FROM THE DOCUMENT'),
            b_state=('read' if (kern or terms or counts) else 'NOT DETERMINABLE FROM THE DOCUMENT'),
            c_state=('read' if c else 'NOT DETERMINABLE FROM THE DOCUMENT'),
            d_state=('anchored' if anchors else 'EMPTY'))
        out.append(rowrec)
        rec('-' * 100)
        rec('  ### `%s`' % f)
        rec('      cluster : %s' % rowrec['cluster'])
        rec('      ### **(a) WHAT IT SYNTHESIZES** : %s' % rowrec['a_state'])
        for s in (a or [])[:2]:
            rec('          | %s' % s.strip()[:170])
        rec('      ### **(b) WHAT IT CITES** : kernels %d ; named terminals %d ; ### **COUNTS %d**'
            % (len(kern), len(terms), len(counts)))
        if kern:
            rec('          kernels   : %s' % ', '.join('`%s`' % k for k in kern[:6]))
        if terms:
            rec('          terminals : %s' % ', '.join('`%s`' % t for t in terms[:6]))
        if counts:
            rec('          ### **COUNTS, WHICH ARE NOT NAMED TERMINALS** : %s'
                % ', '.join('`%s`' % c for c in counts[:6]))
        rec('      ### **(c) WHAT IT WAITS ON** : %s' % rowrec['c_state'])
        for s in (c or [])[:2]:
            rec('          | %s' % s.strip()[:170])
        rec('      ### **(d) WHAT BEARS ON IT AND IS NOT IN IT** : %s (%d anchor(s))'
            % (rowrec['d_state'], len(anchors)))
        for an in anchors[:6]:
            rec('          %s:%d   ### act(s) %s, not named in this document'
                % (an['file'], an['line'], ','.join('b' + x for x in an['acts'])))

    nd = sum(1 for x in out if x['d_state'] == 'anchored')
    rec('')
    rec('=' * 100)
    rec('  ### ### **KEYSTONES WITH A NON-EMPTY COLUMN (d) : %d of %d**' % (nd, len(out)))
    for col in ('a', 'b', 'c'):
        n = sum(1 for x in out if x[col + '_state'] != 'read')
        rec('  ### column (%s) reading `NOT DETERMINABLE FROM THE DOCUMENT` : %d of %d'
            % (col, n, len(out)))
    rec('  ### **THE FOUR COLUMNS ARE NEVER AVERAGED INTO ONE STATUS.**')
    rec('  ### **COLUMN (d) IS LISTED BY ANCHOR AND NOT SUMMARIZED.**')
    rec('  ### **NOTHING WAS INFERRED TO FILL A CELL, AND NO KERNEL WAS OPENED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b375_integration_notes', LINES)
    io.open(os.path.join(D, 'b375_integration.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(keystones=len(out), d_nonempty=nd,
                        not_determinable={c: sum(1 for x in out if x[c + '_state'] != 'read')
                                          for c in ('a', 'b', 'c')},
                        averaged_statuses=0, kernels_opened=0, cells_inferred=0,
                        rows=out,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
