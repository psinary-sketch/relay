# -*- coding: utf-8 -*-
"""b619_test_n5.py -- THE N5 SCORER'S TEST, UNDER (R229)(2). ### WRITTEN AFTER THE SEAL, AS THE FACE'S READING (iii) DECLARES.

### The repaired N5 scorer (tools/b619_record.py `n5(trail_line, ot)`) is run before and after a trail write and must read the same
### verdict. `c4` runs it on the trails as they stand and on a copy with the trail record's head appended at its expected line, in the
### seat's scratchpad (no ledger is written); `c6-before` and `c6-after` run it around the real trail write at Component 6. Beside each
### repaired run, the scorer as sealed (the blob of relay a975611b, the record tool committed as it stands at the seal) is run the same
### way: OPEN_TRAILS changes at Component 1, so the sealed form -- OPEN_TRAILS wanted only once the trail record is banked -- reads
### REFUTED before the write and HELD after it, and the test reads that difference as its positive control. The sealed form's banks are
### read from a scratchpad directory holding a copy of the kernels' face and, for its "after", a stand-in trail bank. Banks
### data/b619_test_n5.txt and data/b619_test_n5.json, the runs appended in order.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import time
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b619_record as REC  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
SEALED = 'a975611b'
SP = REC.SP
OTP = os.path.join(REC.PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def ot_text():
    return io.open(OTP, encoding='utf-8', errors='replace').read().replace(chr(13), '')


def sealed_module(trail_bank):
    """### the record tool as sealed, loaded from its committed blob, its b619 banks read from a scratchpad directory"""
    src = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/b619_record.py' % SEALED], capture_output=True).stdout.decode('utf-8')
    m = types.ModuleType('b619_record_sealed')
    m.__file__ = os.path.join(ROOT, 'tools', 'b619_record.py')
    argv0 = sys.argv
    sys.argv = ['b619_record.py', 'n5']
    try:
        exec(compile(src, 'b619_record.py@%s' % SEALED, 'exec'), m.__dict__)
    finally:
        sys.argv = argv0
    d = os.path.join(SP, '_b619_test_n5_%s' % ('after' if trail_bank else 'before'))
    os.makedirs(d, exist_ok=True)
    shutil.copyfile(os.path.join(D, 'b619_kernels_face.json'), os.path.join(d, 'b619_kernels_face.json'))
    tb = os.path.join(d, 'b619_trail.json')
    if trail_bank:
        open(tb + '.tmp', 'wb').write((json.dumps(dict(line=None, stand_in=True)) + NL).encode('utf-8'))
        os.replace(tb + '.tmp', tb)
    m.DOUT = d
    return m, os.path.exists(tb)


def bank(runs):
    rep = [r for r in runs if r['form'] == 'repaired']
    same = len(set(r['verdict'] for r in rep)) == 1 and len(rep) >= 2
    sealed = [r for r in runs if r['form'] == 'sealed']
    summ = ('the repaired scorer read %s at %s; the sealed form read %s' % (
        sorted(set(r['verdict'] for r in rep)), [r['stage'] for r in rep], [(r['stage'], r['verdict']) for r in sealed]))
    L = ['b619 -- THE N5 SCORER`S TEST, (R229)(2): the repaired scorer run before and after a trail write, the scorer as sealed beside it', '']
    for r in runs:
        L.append('  %-10s %-8s trail line %-6s the trails` lines %-6s -> %s -- %s' % (r['stage'], r['form'], r['trail_line'], r['ot_lines'], r['verdict'],
                                                                                 r['detail'][-260:]))
    L += ['', '### ### **THE N5 TEST : %s.** %s' % ('THE SAME VERDICT BEFORE AND AFTER THE TRAIL WRITE' if same else 'THE VERDICT DIFFERS', summ)]
    for name, b in (('b619_test_n5.txt', (NL.join(L) + NL).encode('utf-8')),
                    ('b619_test_n5.json', (json.dumps(dict(runs=runs, same=same, summary=summ, at=utc()), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L))


def runs_so_far():
    p = os.path.join(D, 'b619_test_n5.json')
    return json.load(io.open(p, encoding='utf-8'))['runs'] if os.path.exists(p) else []


def run(stage, text, trail_line, written):
    out = []
    v, det = REC.n5(trail_line, text)
    out.append(dict(stage=stage, form='repaired', trail_line=trail_line, ot_lines=len(REC.lines_of(text)), verdict=v, detail=det, at=utc()))
    m, tb = sealed_module(written)
    sv, sdet = m.n5()
    out.append(dict(stage=stage, form='sealed', trail_line=None, ot_lines=len(REC.lines_of(text)), verdict=sv, detail=sdet, stand_in_trail_bank=tb,
                    at=utc()))
    return out


def c4(*a):
    t = ot_text()
    tl = len(REC.lines_of(t)) + 2
    runs = run('c4-before', t, tl, False)
    t2 = t + NL + REC.TRAIL_HEAD + NL     # ### the record's head at its expected line, in a copy: no ledger written
    runs += run('c4-after', t2, tl, True)
    bank(runs)


def c6(stage, *a):
    if stage not in ('before', 'after'):
        sys.exit('usage: c6 before|after trail_line=N')
    tl = [int(x.split('=')[1]) for x in a if x.startswith('trail_line=')]
    if not tl:
        sys.exit('### NO EXPECTED LINE GIVEN -- NOTHING RUN')
    t = ot_text()
    runs = runs_so_far() + run('c6-' + stage, t, tl[0], stage == 'after')
    bank(runs)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'c4':
        c4(*sys.argv[2:])
    elif cmd == 'c6':
        c6(*sys.argv[2:])
    else:
        print('usage: b619_test_n5.py c4 | c6 before|after trail_line=N')
        sys.exit(2)
