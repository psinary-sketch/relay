# -*- coding: utf-8 -*-
"""b375_rubric.py -- COMPONENT 4: THE RUBRIC APPLIED, MEASURED NOT OPINED.

### ### **`b374`'S AUDIT IS USED UNMODIFIED** -- its `measure` and its `line_of` are IMPORTED and
### called as they stand, and `hedge_audit` under them is untouched. ### **NOT ONE STEM, GRADE TOKEN OR
### TEST IS TUNED FOR THIS SURFACE.**
### ### **THE RUBRIC SAYS A KEYSTONE MAY NOT CARRY HEDGES, OPEN QUESTIONS OR WORKING NOTES.** ### This
### file measures whether they do, ### **AND PRONOUNCES ON NO DOCUMENT.** ### The measurement is the
### product; the disposition is the author's and is a later act.
### ### **THE `SUPPORT` POPULATION IS MEASURED AS THE CONTROL**, so the difference between the layers
### is measured rather than assumed.
### ### **AND THE COMPARISON IS PER THOUSAND SENTENCES AS WELL AS RAW** (`b374`'s rule), because a raw
### total would score the rubric on a fact about file sizes.
### ### **REPAIR NOTHING.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import hedge_audit as HA         # noqa: E402
import b374_hedge as B374        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE THIRD THING THE RUBRIC NAMES IS `OPEN QUESTIONS STATED AS THE DOCUMENT'S OWN`, AND THAT IS
# ### NOT A CLASS `b374` HAD.** ### It is declared here, as this act's own, with its limit printed:
# ### ### **IT CANNOT SEE WHETHER A QUESTION IS THE DOCUMENT'S OWN OR SOMEBODY ELSE'S**, so it requires
# ### the sentence to be SELF-DESCRIBING or to use the record's own open-question vocabulary.
OPENQ = re.compile(r'\b(open question|remains open|still open|we do not know|not yet known|'
                   r'unanswered|is not settled|remains unsettled|an open problem)\b', re.I)
SELFQ = re.compile(r'\b(this document|this paper|this file|we|our)\b', re.I)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def openq(txt):
    out = []
    for s in HA._sentences(txt):
        if OPENQ.search(s):
            out.append(s)
        elif s.rstrip('*`_ ').endswith('?') and SELFQ.search(s) and len(s.split()) >= 8:
            out.append(s)
    return out


def main():
    rec('=' * 100)
    rec('b375 -- COMPONENT 4: THE RUBRIC APPLIED. ### **MEASURED, NOT OPINED.**')
    rec('=' * 100)
    rec('')
    ok, _log = HA.self_test(False)
    rec('  ### the instrument, IMPORTED and untouched : %s' % os.path.basename(HA.__file__))
    rec('  ### `b374`s measurement, IMPORTED and untouched : %s' % os.path.basename(B374.__file__))
    rec('  ### its own fixtures, run here before it is trusted : %s' % ok)
    rec('  ### ### **THE RUBRIC`S THIRD ITEM IS THIS ACT`S OWN PREDICATE AND IS MARKED AS SUCH:**')
    rec('  ###   OPEN QUESTION : %s' % OPENQ.pattern[:120])
    rec('  ###     or a question mark in a self-describing sentence of at least eight words.')
    rec('  ###     ### ### **IT CANNOT SEE WHETHER A QUESTION IS THE DOCUMENT`S OWN OR SOMEBODY')
    rec('  ###     ### ### ELSE`S.** ### That limit is printed with the count.')
    rec('')
    pop = json.load(io.open(os.path.join(D, 'b375_population.json'), encoding='utf-8'))
    rows = {r['file']: r for r in pop['rows']}
    groups = dict(KEYSTONE=[f for f in rows if rows[f]['order_class'] == 'KEYSTONE'],
                  SUPPORT=[f for f in rows if rows[f]['order_class'] == 'SUPPORT'])
    rec('-' * 100)
    rec('  ### THE MEASUREMENT, PER DOCUMENT. ### **KEYSTONE FIRST, THEN THE CONTROL.**')
    rec('-' * 100)
    out, totals = {}, {}
    for label in ('KEYSTONE', 'SUPPORT'):
        rec('')
        rec('    ### **%s** ### -- %d documents' % (label, len(groups[label])))
        rec('    %-58s %7s %7s %7s %7s %9s' % ('document', 'sents', 'hedged', 'openQ', 'notes',
                                               'hedge/k'))
        tt = dict(docs=0, sentences=0, hedged=0, hedged_bare=0, openq=0, notes=0)
        for f in sorted(groups[label]):
            p = os.path.join(PP, f.replace('/', os.sep))
            m = B374.measure(p)
            try:
                txt = io.open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            oq = openq(txt)
            m['openq'] = len(oq)
            m['openq_samples'] = oq[:3]
            m['file'] = f
            m['class'] = label
            out[f] = m
            tt['docs'] += 1
            for k in ('sentences', 'hedged', 'hedged_bare', 'notes'):
                tt[k] += m[k]
            tt['openq'] += len(oq)
            rec('    %-58s %7d %7d %7d %7d %9.1f'
                % (f[:58], m['sentences'], m['hedged'], len(oq), m['notes'], m['per_k']))
        tt['per_k'] = 1000.0 * tt['hedged'] / tt['sentences'] if tt['sentences'] else 0.0
        tt['openq_per_k'] = 1000.0 * tt['openq'] / tt['sentences'] if tt['sentences'] else 0.0
        tt['notes_per_doc'] = tt['notes'] / tt['docs'] if tt['docs'] else 0.0
        rec('    %-58s %7d %7d %7d %7d %9.1f'
            % ('### TOTAL', tt['sentences'], tt['hedged'], tt['openq'], tt['notes'], tt['per_k']))
        totals[label] = tt

    rec('')
    rec('-' * 100)
    rec('  ### THE INSTANCES, QUOTED AND LOCATED. ### **EACH ONE IS IN ITS DOCUMENT.**')
    rec('-' * 100)
    quoted = 0
    for f in sorted(out):
        m = out[f]
        if m['class'] != 'KEYSTONE':
            continue
        if not (m['samples']['hedged'] or m['openq_samples'] or m['samples']['notes']):
            continue
        p = os.path.join(PP, f.replace('/', os.sep))
        rec('')
        rec('    ### `%s`' % f)
        for s in m['samples']['hedged'][:2]:
            ln = B374.line_of(p, s)
            quoted += 1
            rec('      HEDGED         line %-6s | %s' % (ln, s.strip()[:150]))
        for s in m['openq_samples'][:2]:
            ln = B374.line_of(p, s)
            quoted += 1
            rec('      OPEN QUESTION  line %-6s | %s' % (ln, s.strip()[:150]))
        for ln, tok, s in m['samples']['notes'][:2]:
            quoted += 1
            rec('      WORKING NOTE   line %-6d | (%s) %s' % (ln, tok, s[:130]))

    K, S = totals['KEYSTONE'], totals['SUPPORT']
    rec('')
    rec('=' * 100)
    rec('  ### THE TWO LAYERS, RAW AND PER THOUSAND SENTENCES.')
    rec('=' * 100)
    rec('  %-14s %7s %10s %8s %8s %8s %10s %10s'
        % ('population', 'docs', 'sentences', 'hedged', 'openQ', 'notes', 'hedge/k', 'openQ/k'))
    for lbl, tt in (('KEYSTONE', K), ('SUPPORT', S)):
        rec('  %-14s %7d %10d %8d %8d %8d %10.1f %10.1f'
            % (lbl, tt['docs'], tt['sentences'], tt['hedged'], tt['openq'], tt['notes'],
               tt['per_k'], tt['openq_per_k']))
    rec('')
    rec('  ### ### **THE RUBRIC SAYS A KEYSTONE MAY NOT CARRY THESE. ### THIS ACT REPORTS WHETHER THEY')
    rec('  ### ### DO AND PRONOUNCES ON NO DOCUMENT.** ### **NO DOCUMENT IS CALLED DEFECTIVE, DEMOTED,')
    rec('  ### ### OR SAID TO FAIL THE RUBRIC** -- the disposition is the author`s and is a later act.')
    rec('  ### **AND THE CONTROL IS PRINTED BESIDE IT SO THE DIFFERENCE BETWEEN THE LAYERS IS MEASURED')
    rec('  ### RATHER THAN ASSUMED**, which is the order`s own instruction.')
    rec('  ### **NOTHING WAS REPAIRED. ### NO SENTENCE WAS REWRITTEN. ### THE INSTRUMENT WAS NOT TUNED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b375_rubric_notes', LINES)
    io.open(os.path.join(D, 'b375_rubric.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(instrument=os.path.basename(HA.__file__), instrument_selftest=ok,
                        totals=totals, quoted=quoted,
                        documents={k: {kk: vv for kk, vv in v.items() if kk != 'samples'}
                                   for k, v in out.items()},
                        pronouncements=0, documents_repaired=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
