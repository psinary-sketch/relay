# -*- coding: utf-8 -*-
"""b480_components.py -- COMPONENTS 1, 2 AND 3 AGAINST THE b475 LOG, READ AS A SNAPSHOT.
### Run after the seal (sha256 `3ac8813dc4c9db57...`). ### The run is STILL GOING while this reads, so
### every figure carries the snapshot's byte count and time. ### **THE RUN IS NOT STOPPED OR TOUCHED.**
"""
import datetime
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
LOG = os.path.join(D, 'b475_zeta23_build.log')
NL = chr(10)
L = []
FAILED_AT_b473 = ('Zeta23.Hypotheses', 'Zeta23.Defs.Counting', 'Zeta23.Taper.Basic')

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


S = json.loads(read(os.path.join(D, 'b480_survey.json')))
ORDER = [l for l in read(os.path.join(D, 'b475_order.txt')).split(NL) if l.strip()]


def main():
    # ### ### **THE SNAPSHOT IS TAKEN ONCE, BY BYTES, AND EVERY FIGURE BELOW COMES FROM THAT ONE READ.**
    raw = io.open(LOG, 'rb').read()
    at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    text = raw.decode('utf-8', 'replace').replace(chr(13), '')
    lines = text.split(NL)

    rec('=' * 104)
    rec('COMPONENT 1 -- THE BUILD SO FAR. ### b473`S COMPONENT 1 AGAINST A SNAPSHOT.')
    rec('=' * 104)
    rec('    ### ### **THE SNAPSHOT : %d BYTES, READ AT %s ; THE RUN IS STILL GOING.**' % (len(raw), at))
    rec('    (b473 read a finished log of 17,143 bytes; this one is not finished and is not claimed to be.)')

    marks = [(i + 1, l.strip()) for i, l in enumerate(lines) if l.startswith('=== ')]
    head = [m for m in marks if 'START' in m[1] or 'LEAN_NUM_THREADS' in m[1]]
    rec('')
    rec('  ### (1a) THE LAUNCHER`S HEAD, VERBATIM.')
    for n, l in head:
        rec('    :%-5d %s' % (n, l))

    mods = [(i + 1, re.match(r'=== \[(.+?)\] MODULE (\d+) : (\S+)', l.strip()))
            for i, l in enumerate(lines) if l.startswith('=== [') and ' MODULE ' in l]
    mods = [(n, m.group(1), int(m.group(2)), m.group(3)) for n, m in mods if m]
    exits = {}
    for i, l in enumerate(lines):
        m = re.match(r'=== EXIT (\d+) : (\S+)$', l.strip())
        if m:
            exits[m.group(2)] = int(m.group(1))
    rec('')
    rec('  ### (1b) THE PER-MODULE PROGRESS, FROM THE LOG`S OWN MARKERS.')
    rec('    modules STARTED in the snapshot : %d of %d' % (len(mods), len(ORDER)))
    rec('    modules with an EXIT line       : %d' % len(exits))
    done_ok = sum(1 for v in exits.values() if v == 0)
    bad = {k: v for k, v in exits.items() if v != 0}
    rec('    ### ### **EXIT 0 : %d ; NON-ZERO : %d %s**' % (done_ok, len(bad), bad or ''))
    if mods:
        rec('    the last module started : #%d %s at %s' % (mods[-1][2], mods[-1][3], mods[-1][1]))
    rec('    ### ### **MODULES STILL TO START : %d OF %d.**' % (len(ORDER) - len(mods), len(ORDER)))

    rec('')
    rec('  ### (1c) EVERY FAILING MODULE, WITH ITS STDERR -- OR NONE.')
    panics = [(i + 1, l.strip()) for i, l in enumerate(lines)
              if 'PANIC' in l or 'bad_alloc' in l or 'out of memory' in l.lower()]
    if not bad and not panics:
        rec('    ### ### **NONE. ### NO MODULE HAS FAILED IN THIS SNAPSHOT, AND NO MEMORY FAILURE APPEARS')
        rec('    ### ANYWHERE IN IT.**')
    for k, v in bad.items():
        rec('    %-28s EXIT %d' % (k, v))
    for n, l in panics:
        rec('    :%-5d %s' % (n, l[:120]))

    rec('')
    rec('  ### (1d) THE WALL TIME -- AND A DEFECT IN b475`S LAUNCHER, FOUND HERE.')
    stamps = sorted(set(m.group(1) for m in (re.match(r'=== \[(.+?)\] MODULE ', l.strip())
                                             for l in lines) if m))
    rec('    distinct timestamps across the %d MODULE markers : %d %s'
        % (len(mods), len(stamps), stamps if len(stamps) < 4 else ''))
    rec('    ### ### **EVERY MODULE MARKER CARRIES THE SAME INSTANT, THE LAUNCH`S OWN.** ### Inside a')
    rec('    ### parenthesised `FOR` block `cmd` expands `%%time%%` ONCE, WHEN IT PARSES THE BLOCK, so the')
    rec('    ### launcher wrote the launch time on all of them. ### **b475`S ORDER ASKED FOR "a timestamp')
    rec('    ### per module" AND b475`S LAUNCHER DID NOT DELIVER ONE** -- `!time!` was needed where')
    rec('    ### `%%time%%` was written. ### The run is NOT touched to fix it; the defect is named and the')
    rec('    ### elapsed is taken from evidence that does not depend on it.')
    la = json.loads(io.open(os.path.join(D, 'b475_launch.json'), encoding='utf-8-sig').read())
    t0 = datetime.datetime.strptime(la['started_utc'], '%Y-%m-%dT%H:%M:%SZ').replace(
        tzinfo=datetime.timezone.utc)
    tnow = datetime.datetime.strptime(at, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
    tmt = datetime.datetime.fromtimestamp(os.path.getmtime(LOG), datetime.timezone.utc)
    wall = (tnow - t0).total_seconds()
    rec('    launched %s ; snapshot read %s ; the log`s last write %s'
        % (la['started_utc'], at, tmt.strftime('%Y-%m-%dT%H:%M:%SZ')))
    rec('    ### ### **ELAPSED TO THIS SNAPSHOT : %.0f s (%.1f min), FOR %d MODULES STARTED --'
        % (wall, wall / 60.0, len(mods)))
    rec('    ### %.1f s PER MODULE ON AVERAGE, AGAINST THE 6.65 s b476 TIMED FOR ONE CHAIN RUN.**'
        % (wall / max(1, len(mods))))
    rec('    ### ### **AND AT THAT RATE THE %d MODULES STILL TO START ARE ROUGHLY %.0f s (%.0f min) AWAY**'
        % (len(ORDER) - len(mods), (len(ORDER) - len(mods)) * wall / max(1, len(mods)),
           (len(ORDER) - len(mods)) * wall / max(1, len(mods)) / 60.0))
    rec('    ### -- an average over unequal modules, said as an average and not as a deadline.')
    rec('')
    rec('  ### (1e) THE SNAPSHOT`S LAST FORTY LINES, VERBATIM.')
    for k, l in enumerate(lines[-41:], start=max(1, len(lines) - 40)):
        rec('    :%-5d %s' % (k, l[:150]))

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE PROFILES. ### b473`S COMPONENT 2 AGAINST THE SAME SNAPSHOT.')
    rec('=' * 104)
    names = list(S['seventeen']) + list(S['ef'])
    axl = [l for l in lines if 'depends on axioms' in l]
    rec('    lines carrying "depends on axioms" in the snapshot : %d' % len(axl))
    rows = []
    for n in names:
        short = n.split('.')[-1]
        hit = [l for l in axl if ("'%s'" % n) in l or ("'%s'" % short) in l]
        v = 'ABSENT' if not hit else ('STANDARD THREE'
                                      if hit[0].strip().endswith('[propext, Classical.choice, Quot.sound]')
                                      else hit[0].strip())
        rows.append(dict(name=n, verdict=v, line=hit[0].strip() if hit else ''))
        rec('    %-58s %s' % (n, v))
    absent = sum(1 for r in rows if r['verdict'] == 'ABSENT')
    rec('    ### ### **ROWS %d ; ABSENT %d ; CARRYING A PROFILE %d.**' % (len(rows), absent, len(rows) - absent))
    rec('    ### **`ABSENT` IS NOT A PROFILE AND IS NOT ASSUMED TO BE ONE.**')

    remaining = len(ORDER) - len(mods)
    rec('')
    rec('  ### ### **(R82) : NOT YET DECIDABLE.**')
    rec('    ### The profile steps run AFTER every module of the order. ### **%d MODULES OF %d HAVE NOT'
        % (remaining, len(ORDER)))
    rec('    ### STARTED**, so the snapshot carries neither a profile nor a failure to produce one.')
    rec('    ### ### **THIS IS NOT `HOLDS`, AND IT IS NEITHER KIND OF `VOID`.** ### b473`s VOID FOR WANT')
    rec('    ### OF A RUN described a run that had ENDED without producing them; ### **THIS RUN HAS NOT')
    rec('    ### ENDED, AND A VERDICT TAKEN NOW WOULD BE A GUESS WEARING A RULING`S NAME.**')
    rec('    ### ### **(R83) DOES NOT FIRE**, its trigger being (R82) holding.')
    rec('    ### ### **AND THE GRADE DOES NOT MOVE: zeta23 STAYS `DERIVES, CONDITIONAL`, AS b468r LEFT IT.**')

    rec('')
    rec('=' * 104)
    rec('COMPONENT 3 -- (N1) FROM b475, SCORED.')
    rec('=' * 104)
    rec('    the expectation : the serialized run passes the three modules that died in parallel at b473.')
    res = {}
    for m in FAILED_AT_b473:
        pos = ORDER.index(m) + 1
        started = [x for x in mods if x[3] == m]
        code = exits.get(m)
        res[m] = dict(position=pos, started=bool(started), exit=code)
        rec('    %-24s line %-4d in the order ; started %-5s ; ### **EXIT %s**'
            % (m, pos, bool(started), code if code is not None else 'NO EXIT LINE YET'))
    allpass = all(r['exit'] == 0 for r in res.values())
    rec('    ### ### **(N1) : %s**' % ('HELD -- ALL THREE PASSED, EXIT 0, ONE LEAN PROCESS AT A TIME'
                                       if allpass else 'NOT YET SCORABLE / REFUTED -- see the rows'))
    if allpass:
        rec('    ### ### **THE BOUND WAS THE PARALLELISM, NOT THE MODULES.** ### The same three modules that')
        rec('    ### died with `INTERNAL PANIC: out of memory` and `std::bad_alloc` under lake`s own workers')
        rec('    ### compile without complaint when no two Lean processes run at once. ### **NOTHING ABOUT')
        rec('    ### zeta23`S MATHEMATICS CHANGED; ONLY THE NUMBER OF PROCESSES DID.**')

    out = dict(snapshot=dict(bytes=len(raw), read_utc=at, lines=len(lines)),
               started=len(mods), order=len(ORDER), remaining=remaining,
               exits=exits, failures=bad, panics=[p[1] for p in panics], wall_s=wall,
               profiles=rows, absent=absent, r82='NOT YET DECIDABLE', r83='DOES NOT FIRE',
               n1=dict(rows=res, verdict='HELD' if allpass else 'NOT HELD'))
    io.open(os.path.join(D, 'b480_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(out['snapshot'] | dict(started=len(mods), order=len(ORDER), remaining=remaining,
                                     failures=bad, panics=out['panics'], wall_s=wall,
                                     n1=out['n1'], r82=out['r82'], r83=out['r83']),
              io.open(os.path.join(D, 'b480_snapshot.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    json.dump(dict(rows=rows, absent=absent, r82=out['r82'], r83=out['r83']),
              io.open(os.path.join(D, 'b480_profiles.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
