# -*- coding: utf-8 -*-
"""b704_read_arm.py -- G-READ-RULE-STANDING, the standing arm written at b704 on the author's word at the read rule's sort ((R314)(2)).

### The arm reads an act's read bank in the repaired form (data/b<act>_read_calls.txt, written by the record tool's `reads` route from b704 on:
### every Read call with its offset and limit VALUES, the file's lines, the time, and the time of the word that named the cap in the head). It
### recomputes each call's verdict from those columns -- it does not trust the printed label -- and FAILS on any call of a file of two hundred
### lines or more that carries no offset, or no limit, or a limit above two hundred, made at or after the word; a call before the word carrying
### both is the cap's precursor, printed beside the reading and not counted (the author's word at the arm's baseline prompt, b704). From b705 the
### word's time is the act's anchor and every call counts. A bank not in the repaired form reads as a failure (the arm cannot see a limit).
### A read made after an act's closing leaves no row in any bank: that kind stays prose, entered in the defects bank by hand when it occurs.
### Routes: `reading <act>` prints the arm's reading of data/<act>_read_calls.txt ; `negctl` writes data/b704_read_arm_control.txt (the arm over
### the real bank and over mutated copies of it, each as wanted). Written by the Write tool at b704; it writes that one bank.
"""
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
CAP = 200
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROW = re.compile(r'^  (\d+) \| (\S+) \| (\S+) \| offset (\S+) \| limit (\S+) \| (.*?) \| (.*)$')
WORD = re.compile(r'the author`s word at (\S+)\)')


def _int(x):
    return None if x in ('None', '-', '') else int(x)


def parse(text):
    """the bank's rows as dicts, and the word's time from its head; form False where no row of the repaired form is found."""
    L = (text or '').replace(chr(13), '').split(NL)
    m = next((WORD.search(l) for l in L[:6] if WORD.search(l)), None)
    word = m.group(1) if m else None
    rows = [x for x in (_row(l) for l in L) if x]
    return word, rows, bool(rows) and word is not None


def _row(l):
    r = ROW.match(l)
    return dict(line=int(r.group(1)), ts=r.group(2), lines=_int(r.group(3)), offset=_int(r.group(4)), limit=_int(r.group(5)),
                label=r.group(6), path=r.group(7)) if r else None


def verdict(r, word):
    big = r['lines'] is None or r['lines'] >= CAP
    if not big:
        return 'within'
    if r['offset'] is not None and r['limit'] is not None and r['limit'] <= CAP:
        return 'within'
    if r['offset'] is not None and r['limit'] is not None and word and r['ts'] < word:
        return 'precursor'
    return 'offence'


def reading_text(text):
    """(ok, rows, offences, precursors, form) -- the arm's reading of one bank's text."""
    word, rows, form = parse(text)
    off = [r for r in rows if verdict(r, word) == 'offence']
    pre = [r for r in rows if verdict(r, word) == 'precursor']
    return (form and not off), len(rows), off, pre, form


def reading(act):
    p = os.path.join(D, '%s_read_calls.txt' % act)
    text = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return reading_text(text)


def _show(r):
    return 'line %d %s %s lines offset %s limit %s %s' % (r['line'], r['ts'], r['lines'], r['offset'], r['limit'], r['path'])


def negctl(*a):
    real = open(os.path.join(D, 'b704_read_calls.txt'), encoding='utf-8').read()
    word, rows, _f = parse(real)
    after = '%sZ' % time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(time.mktime(time.strptime(word[:19], '%Y-%m-%dT%H:%M:%S')) + 600)) if word else '2099-01-01T00:00:00Z'
    before = '2026-01-01T00:00:00Z'
    real_off = [l for l in real.split(NL) if _row(l) and verdict(_row(l), word) == 'offence']
    clean = NL.join(l for l in real.split(NL) if l not in real_off)
    end = clean.rfind(NL + NL + '### ### **')
    plant = lambda t, row: t[:end] + NL + row + t[end:]   # noqa: E731
    cases = [
        ('the real bank (b704`s, from the word on)', real, None),
        ('a mutated copy, the real bank`s offence rows removed', clean, True),
        ('a mutated copy holding one planted row: 300 lines, offset 1, limit 250, after the word, labelled WITHIN THE RULE',
         plant(clean, '  99991 | %s | 300 | offset 1 | limit 250 | WITHIN THE RULE | planted/limit_above_cap.txt' % after), False),
        ('a mutated copy holding one planted row: 300 lines, no offset, limit 100, after the word',
         plant(clean, '  99992 | %s | 300 | offset None | limit 100 | WITHIN THE RULE | planted/no_offset.txt' % after), False),
        ('a mutated copy holding one planted row: 300 lines, offset 1, no limit, after the word',
         plant(clean, '  99993 | %s | 300 | offset 1 | limit None | WITHIN THE RULE | planted/no_limit.txt' % after), False),
        ('a mutated copy holding one planted precursor: 300 lines, offset 1, limit 250, before the word',
         plant(clean, '  99994 | %s | 300 | offset 1 | limit 250 | WITHIN THE RULE | planted/precursor.txt' % before), True),
        ('a mutated copy holding one planted row under the line floor: 150 lines, no offset, no limit, after the word',
         plant(clean, '  99995 | %s | 150 | offset None | limit None | WITHIN THE RULE | planted/short.txt' % after), True),
        ('b703`s read bank, the form before the repair (no offset or limit values)', open(os.path.join(D, 'b703_read_calls.txt'), encoding='utf-8').read(), False),
    ]
    L = ['b704 -- G-READ-RULE-STANDING: THE ARM`S READING AND ITS CONTROLS ON MUTATED COPIES OF THE REPAIRED BANK`S FORM (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the arm: tools/b704_read_arm.py, its verdict recomputed from each row`s columns (lines, offset, limit, time) against the cap of two hundred',
         '### and the word`s time (%s, the bank`s head). Rows are cases: the copy read | the reading (ok, rows, offences, precursors, form) | as wanted.' % word, '']
    allok = True
    for label, text, want in cases:
        ok, n, off, pre, form = reading_text(text)
        good = (want is None) or (ok == want)
        if want is not None:
            allok = allok and good
        L += ['  %s' % label, '      reading: ok %s ; rows %d ; offences %d ; precursors %d ; the repaired form %s ; %s' % (
            ok, n, len(off), len(pre), form, 'THE REAL READING (no want)' if want is None else 'as wanted (%s) %s' % ('passing' if want else 'failing', good))]
        L += ['      offence  %s' % _show(r) for r in off] + ['      precursor %s' % _show(r) for r in pre]
    ok, n, off, pre, form = reading_text(real)
    L += ['', '### ### **THE REAL READING: %s (ROWS %d ; OFFENCES %d ; PRECURSORS %d) ; EVERY CONTROL AS WANTED %s.**' % (
        'PASS' if ok else 'FAIL', n, len(off), len(pre), allok)]
    if 'dry' not in a:
        p = os.path.join(D, 'b704_read_arm_control.txt')
        open(p + '.tmp', 'wb').write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(NL.join(L[4:]))


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r == 'reading' and len(sys.argv) > 2:
        ok, n, off, pre, form = reading(sys.argv[2])
        print('G-READ-RULE-STANDING over data/%s_read_calls.txt: %s ; rows %d ; offences %d ; precursors %d ; form %s' % (
            sys.argv[2], 'PASS' if ok else 'FAIL', n, len(off), len(pre), form))
        for x in off:
            print('  offence  ' + _show(x))
    elif r == 'negctl':
        negctl(*sys.argv[2:])
    else:
        print('usage: b704_read_arm.py reading <act> | negctl [dry]')
        sys.exit(2)
