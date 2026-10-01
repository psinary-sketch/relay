# -*- coding: utf-8 -*-
"""table_gate.py -- THE PRE-PUSH TABLE CHECK, (R179)(5), written at b569.

### ### **THE RULING.** *Defect (k) made a check. The terminal table is regenerated and diffed before every PLACE-papers
### push, and a diff in any grade cell refuses the push unless the act's face names that cell; a standing line.*
### ### **THE OCCASION.** b568's defect (k): the act's own ledger lines -- a grade word on a line with a backticked name --
### became grade cells, and the regenerated table moved `ch_iff_rh` to CONFLICT and conferred a grade on `EF_lit_chi`; the
### table's own diff caught it before any push, by the seat's reading and not by a gate.
### ### **WHAT IT DOES.** Regenerates the table's rows IN MEMORY through `terminal_table.build()` -- every repository read as
### committed blobs at its HEAD, PLACE-papers' HEAD being the push branch's tip, checked out by push_gated.sh before the call;
### NO FILE IS WRITTEN -- and compares each (repo, name) row's grade cell with relay HEAD's committed
### `data/terminal_table.json` (the last close's table). A row whose grade differs is a MOVED CELL. A moved cell is allowed
### only when the act's face carries a line `TABLE CELL: <repo> / <name>` naming it; any other moved cell REFUSES.
### Rows added or gone are printed and are not refusals (a new terminal has no prior cell to move).
###   python tools/table_gate.py --repo <PLACE-papers path> [--face <registration>] [--prior <json>] [--now <json>]
### --face defaults to $PUSH_GATED_FACE, else the newest relay data/bNNN_registration_*.txt by act number. --prior and --now
### replace the committed table and the regeneration with fixture files (the test's seam; neither skips the comparison).
### Exit: 0 no unnamed moved cell; 1 a moved cell the face does not name (REFUSED); 2 the table could not be regenerated or
### read, or no face found (REFUSED: a check that cannot read its source refuses).
"""
import contextlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
CELL = re.compile(r'TABLE CELL: (\S+) / (\S+)')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def newest_face():
    best = None
    for f in os.listdir(D):
        m = re.match(r'^b(\d+)_registration_.*\.txt$', f)
        if m and (best is None or int(m.group(1)) > best[0]):
            best = (int(m.group(1)), f)
    return os.path.join(D, best[1]) if best else None


def named_cells(face_text):
    return set((m.group(1), m.group(2)) for m in CELL.finditer(face_text or ''))


def moved(prior_rows, now_rows):
    """### RETURN (moved, added, gone): moved = [(repo, name, was, now)] for rows in both whose grade differs."""
    was = {(r['repo'], r['name']): r.get('grade') for r in prior_rows}
    now = {(r['repo'], r['name']): r.get('grade') for r in now_rows}
    mv = sorted((k[0], k[1], was[k], now[k]) for k in set(was) & set(now) if was[k] != now[k])
    return mv, sorted(set(now) - set(was)), sorted(set(was) - set(now))


def regenerate():
    import terminal_table as TT
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        R = TT.build()
    return None if R is None else R['rows']


def committed_prior():
    r = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/terminal_table.json'], capture_output=True)
    return json.loads(r.stdout.decode('utf-8')).get('rows') if r.returncode == 0 else None


def check(prior_rows, now_rows, face_text):
    mv, add, gone = moved(prior_rows, now_rows)
    names = named_cells(face_text)
    bad = [m for m in mv if (m[0], m[1]) not in names]
    return mv, add, gone, bad


def main(argv):
    get = lambda k: argv[argv.index(k) + 1] if k in argv else None
    face = get('--face') or os.environ.get('PUSH_GATED_FACE') or newest_face()
    print('table_gate: (R179)(5) -- the terminal table regenerated in memory and its grade cells diffed before the push')
    if not face or not os.path.isfile(face):
        print('table_gate: REFUSED -- no face to read (%s)' % face)
        return 2
    face_text = io.open(face, encoding='utf-8', errors='replace').read()
    try:
        prior = json.load(io.open(get('--prior'), encoding='utf-8'))['rows'] if get('--prior') else committed_prior()
        now = json.load(io.open(get('--now'), encoding='utf-8'))['rows'] if get('--now') else regenerate()
    except Exception as e:   # ### a check that cannot read its source refuses
        print('table_gate: REFUSED -- the table could not be read or regenerated: %r' % (e,))
        return 2
    if prior is None or now is None:
        print('table_gate: REFUSED -- the table could not be read or regenerated (prior %s, now %s)'
              % (prior is not None, now is not None))
        return 2
    mv, add, gone, bad = check(prior, now, face_text)
    print('table_gate: face %s ; prior rows %d (%s) ; regenerated rows %d ; rows added %d ; gone %d ; grade cells moved %d ; named on the face %d'
          % (os.path.basename(face), len(prior), get('--prior') or 'relay HEAD data/terminal_table.json', len(now), len(add), len(gone),
             len(mv), len(mv) - len(bad)))
    for m in mv:
        print('table_gate:   %s / %s : %s -> %s%s' % (m[0], m[1], m[2], m[3], '' if m in bad else '   (named: TABLE CELL)'))
    if bad:
        print('table_gate: REFUSED -- %d grade cell(s) moved that the face does not name; NOTHING IS PUSHED' % len(bad))
        return 1
    print('table_gate: PASS -- no grade cell moved that the face does not name')
    return 0


def self_test():
    p = [dict(repo='R', name='a', grade='DERIVES'), dict(repo='R', name='b', grade='ENCODES-CONCLUSION')]
    n_same = [dict(r) for r in p]
    n_mut = [dict(repo='R', name='a', grade='DERIVES'), dict(repo='R', name='b', grade='CONFLICT'), dict(repo='R', name='c', grade='DERIVES')]
    ok = check(p, n_same, '')[3] == []
    ok = ok and [x[1] for x in check(p, n_mut, '')[3]] == ['b']
    ok = ok and check(p, n_mut, '### TABLE CELL: R / b')[3] == []
    ok = ok and check(p, n_mut, '')[1] == [('R', 'c')]
    return ok


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        print('table_gate self-test : %s' % ('PASS' if self_test() else 'FAIL'))
        sys.exit(0 if self_test() else 1)
    sys.exit(main(sys.argv[1:]))
