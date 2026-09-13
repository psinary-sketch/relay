# -*- coding: utf-8 -*-
"""b446_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS (P1)-(P8). ### **UNDER (R58) AND (R59).**
### ### Every read is re-taken here from its source and banked before the face is typed; the face declares
### them so none can look discovered later. ### It computes no residual, runs no chain and counts no census
### beyond the one word-count the author's ruling (a) quoted, reproduced so its composition is on record."""
import ast
import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
OUT = os.path.join(D, 'b446_extract.txt')
L = []
MISSES = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def lines_of(path):
    return io.open(path, encoding='utf-8', errors='replace').read().splitlines()


def quote(path, needle, label):
    """### A READ IS A LINE QUOTED WITH ITS NUMBER, OR A MISS PRINTED."""
    ls = lines_of(path)
    hit = [(i + 1, l.rstrip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.relpath(path, ROOT), needle))
        rec('      ### MISS : %s -- %r not in %s' % (label, needle, os.path.relpath(path, ROOT)))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (os.path.relpath(path, ROOT).replace(os.sep, '/'), i, l.strip()[:150]))
    return i


def main():
    rec('=' * 100)
    rec('b446 -- THE SURVEY. ### THE PRE-FACE READS, RE-TAKEN FROM THEIR SOURCES.')
    rec('=' * 100)

    rec('')
    rec('(P1) THE FLOOR`S DEFINITION, FROM THE TOOL THAT DEFINES IT.')
    NF = os.path.join(T, 'noise_floor.py')
    quote(NF, 'noise_floor.py -- THE NOISE-FLOOR GATE (built b272', 'P1 builder')
    quote(NF, 'MACHINE_EPS = 2.220446049250313e-16', 'P1 eps')
    quote(NF, 'DEFAULT_FLOOR = math.sqrt(MACHINE_EPS)', 'P1 floor')
    quote(NF, "b264's bank names `~1.5e-8 ~ sqrt(machine", 'P1 origin')
    import math
    rec('      sqrt(2.220446049250313e-16) = %.16e' % math.sqrt(2.220446049250313e-16))

    rec('')
    rec('(P2) THE DOMAIN THE EMITTING ACT STATED -- OF KIND.')
    quote(NF, 'ANY ACT READING A COMPUTED SPECTRAL OR MODAL QUANTITY', 'P2 contract')
    quote(NF, 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.', 'P2 drift arm header')

    rec('')
    rec('(P3) THE MEASUREMENT THE FLOOR CAME FROM -- b264`S OWN TABLE, AND ITS PARAMETERS.')
    R264 = os.path.join(D, 'b264_run.txt')
    quote(R264, 'THE MODE-RESOLUTION BOUNDARY, MEASURED', 'P3 heading')
    quote(R264, 'lam_n(NQ=700)    lam_n(NQ=1400)', 'P3 parameters')
    ls = lines_of(R264)
    floor_rows = [(i + 1, l.strip()) for i, l in enumerate(ls) if 'NOISE FLOOR -- not an eigenvalue' in l]
    for i, l in floor_rows:
        rec('      data/b264_run.txt:%d | %s' % (i, l))
    rec('      floor-mode rows : %d' % len(floor_rows))
    if len(floor_rows) != 4:
        MISSES.append(('P3 floor rows', 'data/b264_run.txt', 'four rows'))
    quote(R264, 'they sit at `~1.5e-8 ~ sqrt(machine epsilon)`', 'P3 sentence')

    rec('')
    rec('(P4) WHAT b437 DID, AND THE WORD IT USED.')
    E437 = os.path.join(D, 'b437_extract.txt')
    C437 = os.path.join(D, 'b437_closing.txt')
    quote(E437, 'PRICED AT THREE RADII: `a = 1.3`, `1.35`, `1.41`', 'P4 prior radii')
    quote(C437, 'THE FLOOR, PRICED PAST THREE RADII FOR THE FIRST TIME.', 'P4 heading')
    for a in ('a = 5.196152', 'a = 5.385165', 'a = 5.567764'):
        quote(C437, a + '   ratio', 'P4 gate run')
    quote(os.path.join(D, 'b326_windows_run.txt'), 'a = 1.35   zeta RESOLVED', 'P4 small-radius gate run')

    rec('')
    rec('(P5) THE WORD COUNT RULING (a) QUOTED, REPRODUCED -- AND WHAT IT COUNTS.')
    files = []
    for dp, dn, fn in os.walk(D):
        for f in fn:
            if f.endswith('.txt'):
                files.append(os.path.join(dp, f))
    cnt = Counter()
    stems = set()
    shaped = 0
    defn = []
    le_floor = 0
    for p in sorted(files):
        if os.path.basename(p).startswith('b446_'):
            continue
        hit = False
        for l in io.open(p, encoding='utf-8', errors='replace').read().splitlines():
            toks = [t for t in ('RESOLVED', 'DRIFTING', 'AT_FLOOR') if re.search(r'\b%s\b' % t, l)]
            for t in toks:
                cnt[t] += 1
            if toks:
                hit = True
                if '->' in l:
                    shaped += 1
                if 'AT_FLOOR' in toks:
                    defn.append((os.path.relpath(p, ROOT).replace(os.sep, '/'), l.strip()[:120]))
            if '<= floor' in l:
                le_floor += 1
        if hit:
            rel = os.path.relpath(p, D).replace(os.sep, '/')
            m = re.match(r'(?:audit_)?(b\d+)', rel)
            stems.add(m.group(1) if m else rel)
    act_stems = {s for s in stems if re.fullmatch(r'b\d+', s)}
    rec('      over data/**/*.txt, b446`s own files excluded, one line counted once per word it carries:')
    rec('      lines carrying RESOLVED %d ; DRIFTING %d ; AT_FLOOR %d' % (cnt['RESOLVED'], cnt['DRIFTING'], cnt['AT_FLOOR']))
    rec('      distinct stems %d, of which act stems (bNNN) %d and other stems %d' % (len(stems), len(act_stems), len(stems) - len(act_stems)))
    rec('      lines among them carrying a refinement arrow "->" : %d' % shaped)
    rec('      every AT_FLOOR line, read whole:')
    for f, l in defn:
        rec('        %s | %s' % (f, l))
    rec('      gate detail strings "<= floor" (the text the gate prints on an AT_FLOOR verdict) : %d' % le_floor)
    rec('    ### ### **SO THE COUNT RULING (a) QUOTED COUNTS WORD-LINES, PROSE INCLUDED, OVER STEMS NOT ALL ACTS; ITS TWO')
    rec('    ### ### AT_FLOOR LINES ARE DEFINITIONS OF THE ARM, NOT VERDICTS. THE SEAT SUPPLIED THOSE FIGURES UNREAD.**')

    rec('')
    rec('(P6) CAN A GATE READ THE FLOOR`S DOMAIN FROM ITS EMITTING SOURCE?')
    tree = ast.parse(io.open(NF, encoding='utf-8').read())
    names = [t.id for node in tree.body if isinstance(node, ast.Assign) for t in node.targets if isinstance(t, ast.Name)]
    rec('      module-level names bound in noise_floor.py : %s' % names)
    dom = [n for n in names if re.search(r'DOMAIN|KIND|SCOPE|PARAM', n)]
    rec('      of them naming a domain, kind, scope or parameter : %s' % (dom or 'NONE'))
    rec('      NQ = 700 / 1400 appear in noise_floor.py : %s' % ('NQ=700' in io.open(NF, encoding='utf-8').read()))
    quote(NF, '# ### (mode, value at NQ, b264', 'P6 fixture')
    rec('    ### B264_MODES binds b264`s eleven measured mode values and drifts as a SELF-TEST FIXTURE; it binds neither')
    rec('    ### the NQ they were measured at nor the kind of quantity.')
    rec('    ### the kind is prose in the docstring; the parameters are in b264`s bank only.')

    rec('')
    rec('(P7) THE SECOND DOUBLING`S PRICE, FROM b445`S OWN TIMINGS.')
    arms = json.load(io.open(os.path.join(D, 'b445_arms.json'), encoding='utf-8'))
    five = sorted([k for k in arms['a'] if abs(arms['a'][k]['e']) > 1.49e-08], key=float)
    rec('      cells above 1.49e-08 after the first doubling : %s' % five)
    rec('      arm (a) seconds at those cells : %s' % [arms['a'][k]['seconds'] for k in five])
    rec('      moved without falling : %s' % [k for k, s in arms['report']['status']['a'].items() if s == 'MOVES'])

    rec('')
    rec('(P8) THE BAR-FLOOR RULE`S HOMES.')
    quote(os.path.join(T, 'registration_gate.py'), 'THE BAR-FLOOR ARMS, ADDED b347', 'P8 gate')
    tb = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core', 'modules', '2026-09', 'BAR_FLOOR_RULE.md')
    rec('      %s exists : %s' % (tb.replace(os.sep, '/'), os.path.exists(tb)))

    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
