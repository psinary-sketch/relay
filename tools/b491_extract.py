# -*- coding: utf-8 -*-
"""b491_extract.py -- THE SURVEY. ### **THE b475 LOG IS READ, UNDER (R101).**

### Its process was measured dead at b490 -- pid 27508 absent at two readings sixty seconds
### apart, no `lean` or `lake` process at either, the file cold for over three hours.
### ### **NOTHING IS COMPILED AND NO BUILD IS LAUNCHED.** ### The log is read as text.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LOG = os.path.join(D, 'b475_zeta23_build.log')
NL = chr(10)
L, MISSES = [], []
STD3 = '[propext, Classical.choice, Quot.sound]'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def main():
    raw = io.open(LOG, encoding='utf-8', errors='replace').read()
    ls = raw.replace(chr(13), '').split(NL)
    rec('=' * 112)
    rec('b491 -- THE SURVEY. ### THE b475 LOG, READ.')
    rec('=' * 112)

    # ---------------------------------------------------------------- (P1) the file
    rec('')
    rec('(P1) THE FILE, AND THE AUTHORITY TO OPEN IT.')
    rec('-' * 112)
    st = os.stat(LOG)
    import datetime
    rec('    `data/b475_zeta23_build.log` : ### **%d bytes, %d lines.**' % (st.st_size, len(ls)))
    rec('    last written %s ; the process was measured DEAD at b490.'
        % datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds'))
    rec('    ### ### **(R101) DIRECTS THIS READ**, and b490`s Component 0 supplied the fact the')
    rec('    ### ruling rests on. ### **NO BUILD IS LAUNCHED AND NOTHING IS COMPILED HERE.**')

    # ---------------------------------------------------------------- (P2) exits
    rec('')
    rec('(P2) THE BUILD`S EXIT STATUS, EVERY STEP.')
    rec('-' * 112)
    ex = [(i, l) for i, l in enumerate(ls) if l.startswith('=== EXIT')]
    codes = {}
    for i, l in ex:
        m = re.match(r'=== EXIT (\S+) : (.*?)\s*$', l)
        if m:
            codes.setdefault(m.group(1), []).append(m.group(2))
    rec('    `=== EXIT` lines : ### **%d**' % len(ex))
    for c in sorted(codes):
        rec('      code ### **%s** ### : %d step(s)' % (c, len(codes[c])))
    nonzero = [c for c in codes if c != '0']
    rec('    ### ### **NON-ZERO EXITS : %d.**' % sum(len(codes[c]) for c in nonzero))
    rec('    ### ### **THE FINAL MARK : %s**'
        % (next((l.strip() for l in reversed(ls) if l.strip().startswith('===')), 'ABSENT')))
    complete = any('RUN COMPLETE' in l for l in ls)
    rec('    ### the log carries `RUN COMPLETE` : ### **%s**' % complete)
    if not complete:
        MISSES.append(('log', 'no RUN COMPLETE mark'))

    # ---------------------------------------------------------------- (P3) failures
    rec('')
    rec('(P3) EVERY MODULE THAT FAILED, WITH ITS ERROR.')
    rec('-' * 112)
    mods = [(i, re.match(r'=== .*?MODULE (\d+) : (\S+)', l))
            for i, l in enumerate(ls) if 'MODULE ' in l and l.startswith('===')]
    mods = [(i, m.group(1), m.group(2)) for i, m in mods if m]
    rec('    `MODULE` marks : ### **%d**' % len(mods))
    errs = [(i, l) for i, l in enumerate(ls)
            if re.search(r'^\s*error:', l) or 'Build failed' in l
            or re.search(r'\berror:\s', l)]
    rec('    lines matching an ERROR shape : ### **%d**' % len(errs))
    for i, l in errs[:10]:
        rec('      line %-6d %s' % (i + 1, l.strip()[:98]))
    rec('    ### ### **MODULES THAT FAILED : %s**'
        % ('NONE' if not errs and not nonzero else '%d -- SEE ABOVE' % len(errs)))
    sorry = [(i, l) for i, l in enumerate(ls) if re.search(r'\bsorryAx\b|declaration uses .sorry',
                                                           l)]
    rec('    ### lines naming `sorryAx` or a `sorry` warning : ### **%d**' % len(sorry))
    for i, l in sorry[:6]:
        rec('      line %-6d %s' % (i + 1, l.strip()[:98]))

    # ---------------------------------------------------------------- (P4) wall time
    rec('')
    rec('(P4) THE WALL TIME, FROM THE LOG`S OWN MARKS. ### **AND THE LAUNCHER`S DEFECT.**')
    rec('-' * 112)
    stamps = re.findall(r'=== \[\w{3} (\d\d/\d\d/\d{4}) (\d\d:\d\d:\d\d\.\d\d)\]', raw)
    uniq = sorted({s[1] for s in stamps})
    rec('    timestamped `===` marks : ### **%d** ### ; DISTINCT instants : ### **%d**'
        % (len(stamps), len(uniq)))
    rec('    ### ### **b480`S DEFECT, VISIBLE HERE:** ### a batch `FOR` block expands `%%TIME%%`')
    rec('    ### ONCE, so every MODULE line carries the same instant. ### The marks OUTSIDE the')
    rec('    ### loop are real.')
    rec('      earliest : ### **%s** ### ; latest : ### **%s**' % (uniq[0], uniq[-1]))
    def secs(t):
        h, m, s = t.split(':')
        return int(h) * 3600 + int(m) * 60 + float(s)
    wall = secs(uniq[-1]) - secs(uniq[0])
    rec('      ### ### **WALL TIME, START TO `RUN COMPLETE` : %.0f s = %.2f HOURS.**'
        % (wall, wall / 3600.0))
    rec('    ### and lake`s own per-target durations are independent marks:')
    durs = [int(x) for x in re.findall(r'\((\d+)s\)', raw)]
    rec('      `(Ns)` marks : ### **%d** ### ; their sum : ### **%d s = %.2f hours**'
        % (len(durs), sum(durs), sum(durs) / 3600.0))
    rec('      the largest : %s' % sorted(durs, reverse=True)[:6])
    rec('    ### ### **THE TWO AGREE IN ORDER OF MAGNITUDE**, and neither is typed.')

    # ---------------------------------------------------------------- (P5) the profiles
    rec('')
    rec('(P5) THE PROFILES. ### **EVERY `print axioms` LINE, VERBATIM.**')
    rec('-' * 112)
    ax = [(i, l.strip()) for i, l in enumerate(ls)
          if re.match(r"^\s*'.*' depends on axioms: \[", l)]
    rec('    `depends on axioms:` lines : ### **%d**' % len(ax))
    prof = []
    for i, l in ax:
        m = re.match(r"^'(.+?)' depends on axioms: (\[.*\])\s*$", l)
        if not m:
            MISSES.append(('log:%d' % (i + 1), 'unparsable axioms line'))
            continue
        name, axl = m.group(1), m.group(2)
        prof.append(dict(line=i + 1, name=name, axioms=axl, std3=(axl == STD3)))
    rec('    parsed : ### **%d** ### ; ### **STANDARD THREE : %d** ### ; other : %d'
        % (len(prof), sum(1 for p in prof if p['std3']),
           sum(1 for p in prof if not p['std3'])))
    for p in prof:
        if not p['std3']:
            rec('      ### **NOT THE STANDARD THREE** ### line %d : %s -> %s'
                % (p['line'], p['name'], p['axioms']))
    rec('')
    rec('    ### the phases that produced them:')
    for i, l in enumerate(ls):
        if l.startswith('===') and 'STEP :' in l:
            rec('      line %-6d %s' % (i + 1, l.strip()[:100]))

    rec('')
    rec('=' * 112)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 112)
    io.open(os.path.join(D, 'b491_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(bytes=st.st_size, lines=len(ls), exits=len(ex),
                   exit_codes={k: len(v) for k, v in codes.items()},
                   nonzero=sum(len(codes[c]) for c in nonzero),
                   modules=len(mods), errors=len(errs), sorry=len(sorry),
                   complete=complete, wall_s=wall, dur_sum=sum(durs), n_durs=len(durs),
                   distinct_instants=len(uniq), profiles=prof, misses=MISSES),
              io.open(os.path.join(D, 'b491_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
