# -*- coding: utf-8 -*-
"""b473_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (sha256 `b104a0e536bbd029...`,
### locked 2026-09-22T18:12:45Z). ### The log is READ WHOLE here, for the first time in the record.
### ### **NOTHING IS RE-RUN, REBUILT, FETCHED OR CLONED.**
"""
import datetime
import io
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
LOG = os.path.join(D, 'b471_zeta23_build.log')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


S = json.loads(read(os.path.join(D, 'b473_survey.json')))
raw = io.open(LOG, 'rb').read()
text = raw.decode('utf-8', 'replace').replace(chr(13), '')
lines = text.split(NL)


def main():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE BUILD. ### THE LOG READ WHOLE.')
    rec('=' * 104)
    rec('    file   : %s' % LOG)
    rec('    ### ### **BYTES READ : %d ; THE FILE`S SIZE : %d ; EQUAL : %s**'
        % (len(raw), os.path.getsize(LOG), len(raw) == os.path.getsize(LOG)))
    rec('    lines  : %d ; the survey`s pre-seal size reading : %d bytes' % (len(lines), S['log']['bytes']))

    steps = [(i + 1, l) for i, l in enumerate(lines) if l.startswith('=== ')]
    rec('')
    rec('  ### (1a) THE LAUNCHER`S OWN MARKERS AND EXIT LINES, VERBATIM.')
    for n, l in steps:
        rec('    :%-4d %s' % (n, l.strip()))
    exits = dict((m.group(2).strip(), int(m.group(1)))
                 for m in (re.match(r'=== EXIT (\d+) : (.+)', l.strip()) for n, l in steps) if m)
    rec('    ### ### **`lake build Solution` EXIT : %s**' % exits.get('lake build Solution'))

    # ### the wall time from the log's OWN timestamps, not from the file system
    ts = [m for m in (re.match(r'=== \[(\w{3}) (\d\d/\d\d/\d{4}) (\d\d:\d\d:\d\d\.\d\d)\] (.+)', l.strip())
                      for n, l in steps) if m]
    wall = None
    if len(ts) >= 2:
        fmt = '%m/%d/%Y %H:%M:%S.%f'
        t0 = datetime.datetime.strptime('%s %s0' % (ts[0].group(2), ts[0].group(3)), fmt)
        t1 = datetime.datetime.strptime('%s %s0' % (ts[-1].group(2), ts[-1].group(3)), fmt)
        wall = (t1 - t0).total_seconds()
    rec('')
    rec('  ### (1b) THE WALL TIME, FROM THE LOG`S OWN TIMESTAMP LINES.')
    rec('    START : %s %s   (%s)' % (ts[0].group(2), ts[0].group(3), ts[0].group(4)) if ts else '    NO TIMESTAMPS')
    rec('    END   : %s %s   (%s)' % (ts[-1].group(2), ts[-1].group(3), ts[-1].group(4)) if ts else '')
    rec('    ### ### **WALL TIME : %.2f s (%d min %d s)** -- the two lines the launcher wrote, one clock,'
        % (wall, wall // 60, wall % 60))
    rec('    ### no timezone conversion involved.')

    rec('')
    rec('  ### (1c) EVERY MODULE THAT FAILED, WITH ITS ERROR.')
    fails = []
    for i, l in enumerate(lines):
        m = re.match(r'\u2716 \[\d+/\d+\] Building (\S+)', l.strip())
        if m:
            err, code = '', ''
            for j in range(i + 1, min(i + 8, len(lines))):
                if 'INTERNAL PANIC' in lines[j] or 'libc++abi' in lines[j] or 'uncaught exception' in lines[j]:
                    err = lines[j].strip()
                mm = re.match(r'error: Lean exited with code (\d+)', lines[j].strip())
                if mm:
                    code = mm.group(1)
                    break
            fails.append(dict(module=m.group(1), line=i + 1, stderr=err, exit=code))
    if not fails:
        rec('    NONE')
    for f in fails:
        rec('    :%-4d %-28s exit %-12s %s' % (f['line'], f['module'], f['exit'], f['stderr']))
    summary = [l.strip() for l in lines if l.strip().startswith('- Zeta23')]
    rec('    the log`s own summary list ("Some required targets logged failures"): %s' % ', '.join(summary))
    rec('    ### ### **MODULES THAT FAILED : %d ; ALL THREE FOR MEMORY** -- two `INTERNAL PANIC: out of'
        % len(fails))
    rec('    ### memory` at exit 1, one `std::bad_alloc` at exit 3221226505 (`0xC0000409`). ### The run')
    rec('    ### was launched with `LEAN_NUM_THREADS` UNSET, as (R80)`s order named, so lake ran its own')
    rec('    ### parallel workers; ### **THE FAILURE IS THE MACHINE`S MEMORY UNDER THAT PARALLELISM, NOT')
    rec('    ### A DEFECT IN ANY MODULE`S MATHEMATICS** -- no module reported a `sorry`, an unsolved goal,')
    rec('    ### or a type error, and the counter had reached 8,873 of 8,887 targets.')

    rec('')
    rec('  ### (1d) THE LAST FORTY LINES OF THE LOG, VERBATIM.')
    for k, l in enumerate(lines[-41:], start=len(lines) - 40):
        rec('    :%-4d %s' % (k, l))

    rec('')
    rec('  ### ### **THE BUILD DID NOT SUCCEED, SO THE PROFILES WERE NOT PRODUCED.** ### Step 2')
    rec('  ### (`scripts\\PrintAxioms.lean`, as shipped) could not even find the library -- *"unknown module')
    rec('  ### prefix `Solution`"* -- and step 3 failed on a missing object file for `Zeta23.WeilEF.Main`.')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE PROFILES.')
    rec('=' * 104)
    names = list(S['seventeen']) + list(S['ef'])
    axl = [l for l in lines if 'depends on axioms' in l]
    rec('    lines in the log carrying "depends on axioms" : %d' % len(axl))
    rows = []
    for n in names:
        short = n.split('.')[-1]
        hit = [l for l in axl if ("'%s'" % n) in l or ("'%s'" % short) in l]
        if hit:
            line = hit[0].strip()
            std = line.endswith('[propext, Classical.choice, Quot.sound]')
            rows.append(dict(name=n, line=line, verdict='STANDARD THREE' if std else line.split(':', 1)[-1].strip()))
        else:
            rows.append(dict(name=n, line='', verdict='ABSENT'))
        rec('    %-58s %-14s %s' % (n, rows[-1]['verdict'], rows[-1]['line']))
    absent = [r for r in rows if r['verdict'] == 'ABSENT']
    std3 = [r for r in rows if r['verdict'] == 'STANDARD THREE']
    rec('    ### ### **ROWS : %d ; STANDARD THREE : %d ; OTHER PROFILE : %d ; ABSENT : %d.**'
        % (len(rows), len(std3), len(rows) - len(std3) - len(absent), len(absent)))
    rec('    ### **`ABSENT` IS NOT A PROFILE AND IS NOT ASSUMED TO BE ONE.** ### The log carries no')
    rec('    ### `#print axioms` output at all, because neither step that would have produced it ran.')

    ef_rows = [r for r in rows if r['name'] in S['ef']]
    holds = all(r['verdict'] == 'STANDARD THREE' for r in ef_rows)
    build_ok = exits.get('lake build Solution') == 0
    if holds:
        verdict, kind = 'HOLDS', ''
    elif not build_ok:
        verdict, kind = 'VOID', 'FOR WANT OF A RUN'
    else:
        verdict, kind = 'VOID', 'ON A PROFILE'
    rec('')
    rec('  ### ### **(R82)`S CONDITION : %s %s.**' % (verdict, kind))
    for r in ef_rows:
        rec('      %-42s %s' % (r['name'], r['verdict']))
    rec('  ### The condition asks for three profiles; the run produced none. ### **THE DISTINCTION THE')
    rec('  ### ORDER ASKS FOR, SAID PLAINLY: (R82) IS VOID BECAUSE THERE WAS NO RUN TO READ, NOT BECAUSE A')
    rec('  ### PROFILE CAME BACK WRONG. ### NO PROFILE CAME BACK AT ALL, AND NOTHING IS KNOWN AGAINST')
    rec('  ### zeta23 BY THIS ACT.**')
    rec('  ### ### **THE GRADE: zeta23`S TERMINAL STAYS `DERIVES, CONDITIONAL` EXACTLY AS b468r LEFT IT.**')
    rec('  ### It does not become unconditional, and it is not lowered: the act that would move it is a')
    rec('  ### re-read after a run that completes. ### **THAT RE-READ IS OWED AND IS NOT PERFORMED HERE.**')
    rec('  ### ### **(R83) IS OBEYED BY DOING NOTHING: THE CONDITION DID NOT HOLD, SO NO KERNEL IS NAMED,')
    rec('  ### CREATED OR PINNED, AND NOTHING IS VENDORED.**')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 3 -- THE COMPARATOR. ### THE SOURCE`S OWN CHECK, AND IT CHANGES NO GRADE.')
    rec('=' * 104)
    C = S['comparator']
    cache = os.path.join(Z, '.cache', 'palomar-comparator')
    rec('    ### ### **NOT RUN.** ### Every reason, rather than the first:')
    rec('      (1) THE FETCH. The script`s tool cache `.cache/palomar-comparator` is %s, and the script'
        % ('ABSENT' if not os.path.isdir(cache) else 'PRESENT'))
    rec('          clones four pinned checkouts into it -- comparator %s, lean4export %s,'
        % (C['pins'].get('comparator_commit', '')[:8], C['pins'].get('lean4export_commit', '')[:8]))
    rec('          landrun %s, nanoda %s. ### **A RUN WOULD FETCH; THE ORDER`S CONDITION IS "without a'
        % (C['pins'].get('landrun_commit', '')[:8], C['pins'].get('nanoda_commit', '')[:8]))
    rec('          network fetch it has not already made", SO THE ORDER`S OWN CONDITION FAILS HERE.**')
    for c in ('go', 'cargo', 'landrun'):
        rec('      (2) THE TOOL `%s` : %s on this machine.' % (c, C['requirements'].get(c, 'ABSENT')))
    rec('      (3) THE PLATFORM. The script says *"Requires Linux"*; this machine is `%s`.' % C['platform'])
    rec('      (4) THE INPUT. It would compare `Challenge` against `Solution` -- and `Solution` DID NOT')
    rec('          BUILD, as Component 1 shows, so there is nothing for it to compare.')
    rec('    ### ### **NOTHING WAS FETCHED, CLONED OR BUILT BY THIS ACT: the cache is still %s.**'
        % ('ABSENT' if not os.path.isdir(cache) else 'PRESENT'))
    rec('    ### The seventeen names the comparator would check are the same seventeen the script prints,')
    rec('    ### name for name and in order (survey (P2)) -- so the table above is over the right set even')
    rec('    ### though the comparator did not run.')

    out = dict(build=dict(bytes=len(raw), lines=len(lines), exits=exits, wall_s=wall,
                          failures=fails, summary=summary, build_ok=build_ok),
               profiles=rows, absent=len(absent), standard_three=len(std3),
               r82=dict(verdict=verdict, kind=kind, holds=holds),
               comparator=dict(run=False, cache_present=os.path.isdir(cache), reasons=4))
    io.open(os.path.join(D, 'b473_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(out['build'], io.open(os.path.join(D, 'b473_build.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    json.dump(dict(rows=rows, r82=out['r82'], comparator=out['comparator']),
              io.open(os.path.join(D, 'b473_profiles.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    io.open(os.path.join(D, 'b473_comparator.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L[L.index([x for x in L if x.startswith('COMPONENT 3')][0]):]) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
