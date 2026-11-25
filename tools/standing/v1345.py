# -*- coding: utf-8 -*-
"""standing/v1345.py -- THE CONTROLS OF v1.34.5 ((R364)(5)[M2], parts (a) to (d) and the three families passed on the author's word,
relay data/b754_author_answers.txt :153, 2026-11-13T23:36:45Z; the rules data/b754_rules.txt (13)-(17)), in v1344.py's form: each instance
read through the route as it stood at BASE (relay 0c4cda98, v1.34.4's own commit, read from its blobs) and through the route on disk; AS
WANTED where the old route fails the instance and the new passes it. THE COMPILE CONTROL RUNS FIRST. The free memory is printed before each
control. No write reaches the relay or PLACE-papers. Written at b754 by the Write tool; no identifier of the author is read into any string
here.

  (current)  rule (13), THE CURRENT EDITION: tools/standing/roster.py at main, BASE's route and BASE's added list against the route on
             disk: 82 entries, every edition carried, against 83, Which_Structure_Confines_v2_4_0 in and, by [K30], SPIRAL_MAP_v0_7.md out; the builder's
             json route equal to roster_at; planted families read by their own version lines (a filename edition below the file's line, a
             line not read, a tie, the slot kept); an act before b754 read by the rule it was built under; b753's export at clause 3 CLEAN
             through roster_at at b753, NOT CLEAN through the rule of b754.
  (added)    rule (17), THE THREE FAMILIES: m5-3, m5-4 and m5-2 in tools/mirror_roster_added.json and in the roster at main, at its foot.
  (project)  rules (14) and (16), THE PROJECT SET: tools/mirror_project_set.json read at PLACE-papers 3020ac84, by (b) 5,709,698 bytes and
             by (b) and (d) 4,027,968 (the cuts with the put's heads), as the put printed them (data/b754_agenda.txt :556); every file of the
             set in the archive at main.
  (cuts)     rule (16): tools/standing/cuts.py, its controls (planted ledgers; the record at 3020ac84).
  (builder)  rule (15) and (16): tools/mirror_build.ps1 parsed by PowerShell's own parser at BASE and on disk, 0 errors at both; the
             `project` print under MANIFEST's table and the cuts' write present on disk alone.
  (version)  tools/standing/VERSION moved to v1.34.5.

  python -X utf8 -u tools/standing/v1345.py control [current|added|project|cuts|builder|version ...] [--bank]
"""
import io
import json
import os
import re
import subprocess
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '0c4cda98'   # ### v1.34.4's own commit (b754 component 3, [H1]): the routes before this change
BUILDER = 'tools/mirror_build.ps1'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import roster as RO             # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line)

THREE = ['phase1.5/method/THE_SUBSTRATE.md', 'phase1.5/method/CONCLUSIONS_OF_RECORD.md', 'phase1.5/method/THE_SECOND_EXEMPLAR.md']
PUT = dict(rev='3020ac84', by_b=5709698, by_bd=4027968)   # ### data/b754_agenda.txt :556


def show(rel):
    return V.show(BASE, rel)


def old_roster():
    """tools/standing/roster.py as BASE left it, executed from its blob under another name, its added list read from BASE's blob of
    tools/mirror_roster_added.json (the list the route read at BASE)."""
    src = show('tools/standing/roster.py')
    m = types.ModuleType('roster_base')
    m.__file__ = os.path.join(S, 'roster.py')
    exec(compile(src, 'BASE:tools/standing/roster.py', 'exec'), m.__dict__)
    lst = json.loads(show('tools/mirror_roster_added.json') or '{"files": []}')
    m.added = lambda: [p.replace('\\', '/') for p in lst['files']]
    return m


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.4): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.5): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    """a case wanted the same at both routes (the plain reading)."""
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.4): %s -> (the same at both is wanted)' % at_base,
          '      AFTER  (v1.34.5): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case of the new route alone (a planted instance the old route has no reading of)."""
    L += ['  (%s) %s' % (cls, what), '      AFTER  (v1.34.5): %s -> %s' % (new, 'AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


# ================================================================================ (current)
def control_current():
    L, g, n = ['### (current): RULE (13), THE CURRENT EDITION ((R364)(5)[M2] (a))'], 0, 0
    OM = old_roster()
    tree = RO.main_tree('main')
    ro = OM.resolve(OM.base(), tree, OM.added())[0]
    rn = RO.roster_at('main')
    w24, sm, sm7 = 'day1/Which_Structure_Confines_v2_4_0.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md'
    n += 1
    g += case(L, 'current', 'the roster at main: entries ; Which_Structure_Confines v2.4.0 in ; the map`s one name SPIRAL_MAP.md in and its edition v0.7 out ((R379)(8) [K30], v1.38.30)',
              'BASE`s route and added list: %d ; %s ; %s' % (len(ro), w24 in ro, sm in ro and sm7 in ro),
              'roster_at(main) on disk: %d ; %s ; %s' % (len(rn), w24 in rn, sm in rn and sm7 not in rn),
              w24 not in ro and sm in ro, len(rn) == 83 and w24 in rn and sm in rn and sm7 not in rn)
    _L, rj = RO.print_lines()
    _Lo, rjo = OM.print_lines()
    n += 1
    g += case(L, 'current', 'the builder`s json route (print_lines) carries the roster roster_at reads, one edition a family where decided',
              'BASE`s print_lines: %d entries, SPIRAL_MAP.md and its v0.7 both %s' % (len(rjo), sm in rjo and sm7 in rjo),
              'print_lines on disk: %d entries, equal to roster_at(main) %s' % (len(rj), rj == rn), sm in rjo and sm7 in rjo, rj == rn)
    # ### planted families, read through apply_current with a reader planted in memory
    b = ['a.md', 'x/FAM.md', 'b.md', 'x/FAM_v0_9.md']
    tr = list(b)

    def rd(lines_by_path):
        return lambda p: lines_by_path.get(p, [])
    by_line = {'x/FAM.md': ['# FAM', 'v0.5 -- the current'], 'x/FAM_v0_9.md': ['# FAM', 'v0.3']}
    r1, rows1 = RO.apply_current(b, tr, 'PLANTED', rd(by_line))
    ro1 = OM.resolve(b, tr)[0]
    n += 1
    g += case(L, 'current', 'a planted family whose filename edition v0.9 carries the line v0.3 beside an unversioned file carrying v0.5: '
              'the file of the line v0.5 carried alone, at the family`s first slot',
              'BASE`s resolve: %s' % ro1, 'apply_current: %s' % r1, ro1 == b, r1 == ['a.md', 'x/FAM.md', 'b.md'])
    by_late = {'x/FAM.md': ['# FAM', 'v0.3'], 'x/FAM_v0_9.md': ['# FAM', 'v0.9']}
    r1b, _rw = RO.apply_current(b, tr, 'PLANTED', rd(by_late))
    n += 1
    g += guard(L, 'current', 'the same family with the later line in the later slot: the current edition takes the first slot, no other slot moves',
               'apply_current: %s' % r1b, r1b == ['a.md', 'x/FAM_v0_9.md', 'b.md'])
    miss = {'x/FAM.md': ['# FAM', 'no version line here'], 'x/FAM_v0_9.md': ['# FAM', 'v0.9']}
    r2, rows2 = RO.apply_current(b, tr, 'PLANTED', rd(miss))
    und2 = [x for x in rows2 if not x[4] and len(x[1]) > 1]
    n += 1
    g += guard(L, 'current', 'a file of the family with no version line read: the family UNDECIDED, both editions carried as the rule of b715 carries them',
               'apply_current: %s ; undecided %s' % (r2, [x[0] for x in und2]), r2 == b and [x[0] for x in und2] == ['x/FAM.md'])
    tie = {'x/FAM.md': ['# FAM', 'v0.5'], 'x/FAM_v0_9.md': ['v0.5']}
    r3, rows3 = RO.apply_current(b, tr, 'PLANTED', rd(tie))
    n += 1
    g += guard(L, 'current', 'two files of the family sharing the top line v0.5: UNDECIDED, both carried, the tie printed',
               'apply_current: %s ; %s' % (r3, [x[5] for x in rows3 if x[0] == 'x/FAM.md']),
               r3 == b and any(x[0] == 'x/FAM.md' and x[4] is None and x[5].startswith('a tie') for x in rows3))
    ed = {'x/FAM.md': ['# FAM'] + ['a line of the body'] * 41 + ['*v0.7, 2026-11-01: an edition note past the head`s forty lines'],
          'x/FAM_v0_9.md': ['v0.3']}
    r4, _rw = RO.apply_current(b, tr, 'PLANTED', rd(ed))
    n += 1
    g += guard(L, 'current', 'a file whose head carries no version line and whose edition note does (the [M2] put`s second shape): read by the note',
               'apply_current: %s' % r4, r4 == ['a.md', 'x/FAM.md', 'b.md'])
    prev = A.prev_of(A.current()['act'])
    r53, r54 = RO.roster_at('main', act=prev), RO.roster_at('main', act='b754')
    n += 1
    g += case(L, 'current', 'the act gate: a build of %s read by the rule it was built under (b715 with b753`s [M1]) and the added list as %s built it '
              '(the list`s added_at), of b754 by rule (13) with the three families' % (prev, prev),
              'BASE`s route at main: %d entries' % len(ro),
              'roster_at(main, act=%s) %d entries, equal to BASE`s route %s, the three families in it %s ; act=b754 %d, equal to roster_at(main) %s' % (
                  prev, len(r53), r53 == ro, [p in r53 for p in THREE], len(r54), r54 == rn),
              True, r53 == ro and not any(p in r53 for p in THREE) and r54 == rn)
    L[-3] = '      BEFORE (v1.34.4): BASE`s route at main: %d entries -> (no gate at BASE; the rule of b715 for every act)' % len(ro)
    # ### the record: b753's export at clause 3 (the (3iii) replay of tools/standing/controls.py), through the act's own rule and through b754's
    import mirror_verify as MV
    import zipfile
    bj, bhead = RO.build_joins(prev)
    out = A.jl('%s_mirror_build.json' % prev).get('out') or ''
    mz = re.search(r'^built: (.+)$', out, re.M)
    zp = mz.group(1).strip() if mz else None
    names = [x for x in zipfile.ZipFile(zp).namelist() if x != 'MANIFEST.md'] if (zp and os.path.isfile(zp)) else None
    n += 1
    if names is None:
        g += guard(L, 'current', '%s`s export %s' % (prev, zp), 'ABSENT', False)
    else:
        c_at, _m = MV.clause3(names, paths=RO.roster_at(bhead, act=prev), source='roster_at')
        c_now, _m = MV.clause3(names, paths=RO.roster_at(bhead, act='b754'), source='roster_at')
        g += case(L, 'current', '%s`s export at clause 3 at its source head %s: through the roster it was built under CLEAN ; through b754`s roster '
                  '(rule (13) and the three families) NOT CLEAN (the (3iii) replay of tools/standing/controls.py reads it at act=%s)' % (prev, bhead[:12], prev),
                  'roster_at(%s) with no act, read as b754`s: CLEAN %s' % (bhead[:12], c_now),
                  'roster_at(%s, act=%s): CLEAN %s' % (bhead[:12], prev, c_at), not c_now, c_at)
    return L, g, n


# ================================================================================ (added)
def control_added():
    L, g, n = ['### (added): RULE (17), THE THREE FAMILIES ((R364)(5)[M2] with the amendment row 3 (7))'], 0, 0
    OM = old_roster()
    ro = OM.resolve(OM.base(), RO.main_tree('main'), OM.added())[0]
    rn = RO.roster_at('main')
    n += 1
    g += case(L, 'added', 'm5-3, m5-4 and m5-2 in the added list and in the roster at main, in the list`s order at the roster`s foot',
              'BASE: in the list %s ; in the roster %s' % ([p in OM.added() for p in THREE], [p in ro for p in THREE]),
              'on disk: in the list %s ; the roster`s foot %s' % ([p in RO.added() for p in THREE], rn[-3:] == THREE),
              not any(p in ro for p in THREE), all(p in RO.added() for p in THREE) and rn[-3:] == THREE)
    return L, g, n


# ================================================================================ (project)
def control_project():
    L, g, n = ['### (project): RULES (14) AND (16), THE PROJECT SET ((R364)(5)[M2] (b), (d))'], 0, 0
    import cuts as CU
    at_base = show('tools/mirror_project_set.json')
    rows, by_b, by_bd, cut_rows, _fig, meta = RO.project(PUT['rev'], 'b754')
    f_b = next((b for nm, b, _w in rows if nm == 'FINDINGS.md'), 0) or 0
    put_bd = by_b - f_b + CU.nbytes(CU.AGENDA_HEAD + meta['fbody']) + CU.nbytes(CU.AGENDA_HEAD + meta['obody'])
    n += 1
    g += case(L, 'project', 'the Project set at PLACE-papers %s: by (b) ; by (b) and (d), the cuts with the put`s three-line heads (data/b754_agenda.txt :556)' % PUT['rev'],
              'tools/mirror_project_set.json at BASE: %s, no route' % ('PRESENT' if at_base else 'ABSENT'),
              'roster.py project: %d ; %d (with this tool`s heads %d)' % (by_b, put_bd, by_bd), not at_base,
              by_b == PUT['by_b'] and put_bd == PUT['by_bd'])
    rows_m, _b, _bd, _c, _f, _m = RO.project('main', None, with_cuts=False)
    miss = [nm for nm, _b2, w in rows_m if w.startswith('###')]
    files = [nm for nm, _b2, _w in rows_m if nm != 'MANIFEST']
    n += 1
    g += guard(L, 'project', 'at main: every file of the set in the archive, each family once (SPIRAL_MAP.md and its v0.7 one row)',
               '%d files, not in the archive %s, SPIRAL_MAP rows %d' % (len(files), miss or 'none', sum(1 for x in files if 'SPIRAL_MAP' in x)),
               not miss and len(files) == len(set(files)) and sum(1 for x in files if 'SPIRAL_MAP' in x) == 1)
    return L, g, n


# ================================================================================ (cuts)
def control_cuts():
    L, g, n = ['### (cuts): RULE (16), THE PROJECT`S CUTS ((R364)(5)[M2] (d))'], 0, 0
    import cuts as CU
    at_base = show('tools/standing/cuts.py')
    ok, out = CU.control()
    L += ['      ' + x for x in out]
    n += 1
    g += case(L, 'cuts', 'the two cuts written by one standing route from the ledgers at a commit, refusing where a needle is missing',
              'tools/standing/cuts.py at BASE: %s' % ('PRESENT' if at_base else 'ABSENT, no route'),
              'tools/standing/cuts.py on disk: %s' % (out[-1].strip('# *.') if out else ''), not at_base, ok)
    return L, g, n


# ================================================================================ (builder)
PARSE = ("$t = [Console]::In.ReadToEnd(); $e = $null; $k = $null; "
         "[void][System.Management.Automation.Language.Parser]::ParseInput($t, [ref]$k, [ref]$e); Write-Output $e.Count")
CALLS = (re.compile(r'\$rosterTool project \$head'), re.compile(r'\$cutTool write \$cutDir \$head'))


def parse_errors(text):
    r = subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-Command', PARSE], input=text, capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'(\d+)\s*$', r.stdout or '')
    return int(m.group(1)) if (r.returncode == 0 and m) else 'NOT READ (%s)' % (r.stderr or '').strip()[:120]


def control_builder():
    L, g, n = ['### (builder): RULES (15) AND (16), THE BUILDER`S TWO CALLS (tools/mirror_build.ps1)'], 0, 0
    old = (show(BUILDER) or '').lstrip('﻿').replace('\r', '')   # ### the blob carries its byte-order mark, as the disk file read with utf-8-sig does not
    new = io.open(os.path.join(RELAY, *BUILDER.split('/')), encoding='utf-8-sig').read().replace('\r', '')
    po, pn = parse_errors(old), parse_errors(new)
    n += 1
    g += both(L, 'builder', 'PowerShell`s own parser over the builder: errors', 'at BASE: %s' % po, 'on disk: %s' % pn, po == 0, pn == 0)
    co, cn = [bool(rx.search(old)) for rx in CALLS], [bool(rx.search(new)) for rx in CALLS]
    n += 1
    g += case(L, 'builder', 'the Project set printed under MANIFEST`s table ; the two cuts written beside the archive',
              'at BASE: %s' % co, 'on disk: %s' % cn, not any(co), all(cn))
    lo, ln = old.split(NL), new.split(NL)
    kept = [l for l in lo if l not in ln]
    n += 1
    g += both(L, 'builder', 'every line of the builder at BASE stands on disk (the change adds lines and removes none)',
              'lines at BASE %d' % len(lo), 'lines on disk %d ; lines of BASE not on disk %d' % (len(ln), len(kept)), True, not kept)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.4', ver == 'v1.34.5')
    return L, g, n


CONTROLS = dict(current=control_current, added=control_added, project=control_project, cuts=control_cuts, builder=control_builder,
                version=control_version)
ORDER = ('current', 'added', 'project', 'cuts', 'builder', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.5, (R364)(5)[M2] PASSED, PARTS (a) TO (d) AND THE THREE FAMILIES (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each change`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.34.5: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1345.txt' % act), NL.join(out))
        print('written data/%s_standing_v1345.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
