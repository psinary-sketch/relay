# -*- coding: utf-8 -*-
"""b653_record.py -- THE ACT'S RECORD TOOL, b653 under (R263).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b653's name.
### (R263)(3): every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability spec's planted
### rows (tools/b653_regspec.py) can run each reader over one row of each shape before the seal.
### Routes: `python tools/b653_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7ab48879-b65c-45b3-8af8-abdcd7120d6f/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b653's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b653_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R263)(1)-(3)
WH = ('*Appended 2026-10-12 by b653 to b652’s entry (:8259), under `(R263)`(1) -- b652 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b652_closing.txt):*')
MH = ('*Appended 2026-10-12 by b653 beneath b652’s margin correction (:13898), under `(R263)`(2) -- THE MARGIN RULE ON COMPLETED RUNS, '
      'STANDING FROM b653; SUPERSEDES :13898:*')
SH = ('*Appended 2026-10-12 by b653, under `(R263)`(3) -- THE SEAL ORDER, ONE CLAUSE ADDED: A PLANTED ROW OF EVERY SHAPE A SEALED ROUTE READS, '
      'STANDING FROM b653:*')


def _weight():
    return ('\n' + WH + ' relay 6eaacf29 (the act) and 466886b5 (the closing); PLACE-papers 81fa18a; the root 89e62b16… over 40 banks; the '
            'suite 80 arms, 78 of 80 before and after the push, the two declared failures G-NO-SORRY-MAIN and G-AXIOM-CLAIM. Milestones built '
            'and merged alone on its gate reading -- SIDE-effects main 9a279ac, its three restated lines off main; PerpendicularCrossing built '
            'for its measurement, loss 1,452 MB, the cut branch left unmerged; T3_StepNineBridge stopped beneath the hold, loss at least 1,826 '
            'MB, its branch unmerged, the one sorry on any main at its :108. The cut of 113 blocks in 33 files on a branch, the code byte for '
            'byte the same under comment stripping. The INSTRUMENT verdict with its opening rows, the block table’s identical reading before and '
            'after the cut entered as one of them. The conversion rule with its planted case, the five arms of b651’s defect (n) passing at '
            'HEAD. Twelve defects (relay data/b652_defects.txt), the navigator’s among them the margin term (d) and the sentence-row assumption '
            '(b). The mirror export D:/MY-DOwnloads/mirror-refresh-2026-10-11-b652.zip (MANIFEST md5 ce698d41…, commit 81fa18a). Nothing '
            'deposited.\n')


def _margin_rule():
    return ('\n' + MH + ' a figure read from a stopped run is a lower bound and licenses no start: it reads "at least <x>, UNMEASURED". A '
            'module’s margin needed is the host’s loss from a completed run -- free memory at the start less the host’s low, as the watchdog '
            'prints them; a build on this host starts where the margin seen at the slot’s start reaches that loss, and nowhere else. The hold '
            'stays 2,560 MB on every host. The rule’s opening entries, b652’s two completed runs (relay data/b652_build_margin.txt :34, :36): '
            'Kernel.PerpendicularCrossing 1,452 MB; SIDEEffects.Milestones 1,332 MB. SIDELvConservation.T3_StepNineBridge reads at least 1,826 '
            'MB, UNMEASURED (:38, a stopped run). This supersedes b652’s correction at :13898, whose largest-of-the-attempts term counted '
            'stopped runs.\n')


def _seal_order():
    return ('\n' + SH + ' the registration gate’s satisfiability spec carries one planted row of every shape a sealed route reads -- build '
            'rows, score rows, trail heads with a backtick possessive among them -- and runs each of the record tool’s readers over its row '
            'before the seal, so a sealed tool meets each shape before it is sealed and not after. Its cases: b651’s (m) and (n), a trail head '
            'and an entry title looked up by another conversion than the landing’s; b652’s (l), a score route reading keys its build rows did '
            'not carry. The spec counts its planted rows and refuses to emit where a reader raises or returns nothing.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', MH, _margin_rule()), ('OPEN_TRAILS.md', SH, _seal_order())]
    land(items, 'b653_record_lines.json', 'c1', entry=8259,
         check=[('FINDINGS.md', 8259, '## The build margin at 3 modules'), ('OPEN_TRAILS.md', 13898, 'THE MARGIN TERM CORRECTED')],
         dry='dry' in a)


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b653_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
