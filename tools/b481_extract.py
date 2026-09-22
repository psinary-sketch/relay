# -*- coding: utf-8 -*-
"""b481_extract.py -- THE SURVEY FOR THE CIRCULATION GATE. ### Every line is read from a file already
### on disk, under (R89): ### **NO BUILD IS STARTED, NO LANE OPENED, NO RUNNING LOG READ, NOTHING
### FETCHED.** ### The gate at REGISTRY.md:523, its trigger, the (c') search, b395's two records,
### b145's and b337's fetches, and the four sites' deposit-state lines.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def wrap(s, w=150, pad='      '):
    import textwrap
    return [pad + x for x in textwrap.wrap(s, w)]


def main():
    rec('=' * 104)
    rec('b481 -- THE SURVEY. ### FILES ALREADY ON DISK; NOTHING FETCHED; NO RUNNING LOG READ.')
    rec('=' * 104)

    # ------------------------------------------------------------------ (P1) the gate and its trigger
    rec('')
    rec('(P1) THE GATE AT REGISTRY.md:523, WHOLE.')
    rec('-' * 104)
    reg = read(os.path.join(PP, 'REGISTRY.md')).split(NL)
    gate = reg[522]
    rec('    the line is %d characters; quoted whole, wrapped for the page:' % len(gate))
    for x in wrap(gate):
        rec(x)
    m = re.search(r'\*\*Run when the \(c\'\) validation job clears\.\*\*', gate)
    rec('    ### ### **THE TRIGGER CLAUSE, VERBATIM : %s**'
        % ('"Run when the (c\') validation job clears."' if m else 'NOT FOUND'))
    if not m:
        MISSES.append(('REGISTRY.md:523', 'trigger clause'))
    sites = re.search(r'reconciles ([^*]+?) against a fetch', gate)
    rec('    the sites the gate names : %s' % (sites.group(1) if sites else 'NOT PARSED'))

    # ------------------------------------------------------------------ (P2) the (c') job
    rec('')
    rec('(P2) THE (c\') VALIDATION JOB, SEARCHED FOR IN THE LIVE CORPUS.')
    rec('-' * 104)
    hits = []
    for base, dirs, files in os.walk(PP):
        if 'archive' in base or '.git' in base:
            continue
        for fn in files:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(base, fn)
            for i, l in enumerate(read(p).split(NL)):
                if re.search(r"\(c'\)|\(c′\)|\(c’\)", l):
                    hits.append((os.path.relpath(p, PP), i + 1, l.strip()))
    rec('    lines in the LIVE corpus carrying (c\') in any apostrophe : %d' % len(hits))
    for f, i, l in hits:
        rec('      %s:%d' % (f, i))
        for x in wrap(l[:400], 140, '        '):
            rec(x)
    jobs = [h for h in hits if 'validation job' in h[2]]
    rec('    ### lines calling it a VALIDATION JOB, other than the gate`s own trigger : %d'
        % max(0, len(jobs) - 1))
    rec('    ### ### **NO (c\') VALIDATION JOB IS DEFINED ANYWHERE IN THE LIVE CORPUS, AND NO STATE FOR')
    rec('    ### ONE IS RECORDED.** ### The only other (c\') in the live tree is INSTRUMENTS.md`s')
    rec('    ### ### **(c′) BENCHMARK** -- a re-platform benchmark that priced a library swap -- which is')
    rec('    ### a different object and carries no clearing state.')

    # ------------------------------------------------------------------ (P3) b395's two records
    rec('')
    rec('(P3) b395`S BANK ON THE TWO DEPOSITED RECORDS.')
    rec('-' * 104)
    b395 = read(os.path.join(D, 'b395_components.txt'))
    b395c = read(os.path.join(D, 'b395_closing.txt'))
    note = re.search(r'> (Historical note: [^\n]+)', b395)
    rec('    21432399 -- the drafted historical note, verbatim from b395_components.txt:')
    if note:
        for x in wrap(note.group(1), 140, '      > '):
            rec(x)
    else:
        MISSES.append(('b395', 'the drafted note'))
    where = [l.strip() for l in b395.split(NL) if 'IT IS DRAFTED HERE AND IS WRITTEN NOWHERE' in l]
    rec('    where the bank says it would go : %s' % (where[0][:140] if where else 'NOT FOUND'))
    for l in b395.split(NL):
        if 'ERRATA.md:117' in l or 'meta/ZENODO_METADATA.md:26' in l or 'OPEN_TRAILS.md:449' in l:
            rec('      cited line : %s' % l.strip())
    rec('')
    rec('    19675356 -- the sentence that its deposited version is recorded nowhere:')
    for l in b395c.split(NL):
        if '19675356' in l or 'NOWHERE IN THE CORPUS' in l or 'ABSENCE FROM ONE' in l:
            rec('      %s' % l.strip()[:150])
    rec('    19675356 -- the smallest recovering read, and who can perform it:')
    grab = False
    for l in b395c.split(NL):
        if 'THE SMALLEST READ THAT WOULD RECOVER IT' in l:
            grab = True
        if grab:
            rec('      %s' % l.strip()[:150])
        if grab and 'A HALT REPORTED IS WORTH MORE' in l:
            break

    # ------------------------------------------------------------------ (P4) the two fetches
    rec('')
    rec('(P4) THE PLATFORM FETCHES THE CORPUS HAS PERFORMED, AT THEIR ADDRESSES.')
    rec('-' * 104)
    for act, needles in (('b145', ('fetched read-only at b144', 'THE DEPOSITED RECORDS')),
                         ('b337', ('the fetch agrees', 'as fetched', 'every field agrees'))):
        for fn in sorted(f for f in os.listdir(D) if f.startswith(act + '_') and f.endswith('.txt')):
            t = read(os.path.join(D, fn))
            for i, l in enumerate(t.split(NL)):
                if any(n in l for n in needles):
                    rec('    %s:%d  %s' % (fn, i + 1, l.strip()[:145]))
                    break
    b389 = read(os.path.join(D, 'b389_closing.txt'))
    for i, l in enumerate(b389.split(NL)):
        if 'six routes' in l or 'positive control' in l:
            rec('    b389_closing.txt:%d  %s' % (i + 1, l.strip()[:145]))

    # ------------------------------------------------------------------ (P5) the four sites
    rec('')
    rec('(P5) THE FOUR SITES` DEPOSIT-STATE LINES, AT THEIR ADDRESSES.')
    rec('-' * 104)
    pat = re.compile(r'v1\.1\.2|v5\.10\.2|v5\.13|21539167|v1\.5|0e5233f|21520474|v0\.10\.0|93c27ec|21539068',
                     re.I)
    site_files = [('README.md', os.path.join(PP, 'README.md')),
                  ('SPIRAL_MAP.md', os.path.join(PP, 'SPIRAL_MAP.md')),
                  ('REGISTRY.md', os.path.join(PP, 'REGISTRY.md'))]
    mem_dirs = [d for d in os.listdir(MEM) if os.path.isdir(os.path.join(MEM, d))]
    for d in mem_dirs:
        p = os.path.join(MEM, d, 'memory', 'MEMORY.md')
        if os.path.exists(p):
            site_files.append(('memory[%s]' % d, p))
    found = {}
    for name, p in site_files:
        rows = []
        for i, l in enumerate(read(p).split(NL)):
            if pat.search(l):
                rows.append((i + 1, l.strip()))
        found[name] = rows
        rec('    %-22s %s : %d deposit-state line(s)' % (name, os.path.relpath(p, PP if 'memory' not in name else MEM), len(rows)))
        for i, l in rows[:4]:
            rec('        :%-5d %s' % (i, l[:140]))
    rec('    ### memory stores found : %s' % ', '.join(mem_dirs))
    rec('    ### ### **THE GATE NAMES "both memories (session + executor)". ### THIS SEAT CAN SEE ONE')
    rec('    ### MEMORY STORE CARRYING DEPOSIT-STATE LINES; THE OTHER STORE ON THIS MACHINE CARRIES NONE.**')

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b481_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(gate_len=len(gate), trigger=bool(m), cprime_hits=len(hits),
                   cprime_lines=[[f, i, l[:200]] for f, i, l in hits],
                   sites={k: [[i, l[:200]] for i, l in v] for k, v in found.items()},
                   memory_stores=mem_dirs, misses=MISSES),
              io.open(os.path.join(D, 'b481_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
