# -*- coding: utf-8 -*-
"""standing/tablescratch.py -- v1.34.0, (R364)(3)(xi), b752 defect (d), b753 defect (d): THE TERMINAL TABLE REGENERATED TO THE ACT'S SCRATCH FOLDER.

The suite's act part ran tools/terminal_table.py, which writes its five files into the relay's data/ (terminal_table.json, its prior copy, its
markdown, its run file and its diff), so every act part left three or more tracked files changed in the tree (b752 (d), b753 (d); b753's close
named the run). The part now regenerates through this module: the generator's own build() and emit(), imported and not copied, the emit pointed
at the act's scratch folder in the state folder on the data volume (D:/relay-state/<act>/terminal_table/), the tracked table and the E/I marks
copied there first so the generator reads its prior and its marks where it reads them; the run file and the diff written beside them; the
scratch table compared with the tracked one, row by row. Nothing under the relay is written. The tracked table moves by its own route, the
record's `table_final`, in a commit of the close.

WHICH TABLE THE READERS NEED: tools/chain_page.py and tools/table_gate.py read data/terminal_table.json at relay HEAD (git show), and
tools/correspondence_gen.py and the record's routes read it in the tree; with the act part no longer writing it, the tree's table is HEAD's,
the last close's, until `table_final` moves it at the close. A reader that wants this act's regeneration reads the scratch folder by `folder()`.

  python -X utf8 -u tools/standing/tablescratch.py <act>     regenerate to the scratch folder and print the comparison (exit: the generator's)
"""
import io
import json
import os
import shutil
import subprocess
import sys

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
if S not in sys.path:
    sys.path.insert(0, S)
import statedir as SD   # noqa: E402
STATE = SD.STATE   # ### the state folder on the data volume, outside every repository ((R364)(3)(xv), (8)), by the one resolver
FILES = ('terminal_table.json', 'terminal_table_prior.json', 'terminal_table.md', 'terminal_table_run.txt', 'terminal_table_diff.json')
NL = '\n'


def folder(act):
    return os.path.join(STATE, act, 'terminal_table')


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def regenerate(act, d=D):
    """(exit, diff): the generator run with its emit pointed at the scratch folder; 8 where its faces refuse, 2 where it builds nothing."""
    out = folder(act)
    os.makedirs(out, exist_ok=True)
    for f in FILES:
        p = os.path.join(out, f)
        if os.path.isfile(p):
            os.remove(p)
    for f in ('terminal_table.json', 'b544_ei.json'):   # ### the prior and the E/I marks, read by emit() where it reads them
        if os.path.isfile(os.path.join(d, f)):
            shutil.copyfile(os.path.join(d, f), os.path.join(out, f))
    if T not in sys.path:
        sys.path.insert(0, T)
    import contextlib
    import terminal_table as TT
    sink = io.StringIO()   # ### the generator's own print, kept whole in its run file (TT.L) and not on the caller's screen
    try:
        with contextlib.redirect_stdout(sink):
            R = TT.build()
    except TT.FacesRefusal as e:
        print('### ### **TERMINAL TABLE REFUSED, NOTHING WRITTEN: %s**' % e)
        return 8, {}
    if R is None:
        return 2, {}
    d0 = TT.D
    TT.D = out
    try:
        with contextlib.redirect_stdout(sink):
            _payload, diff = TT.emit(R)
    finally:
        TT.D = d0
    io.open(os.path.join(out, 'terminal_table_run.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(TT.L) + NL)
    json.dump(diff, io.open(os.path.join(out, 'terminal_table_diff.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    ei = os.path.join(out, 'b544_ei.json')
    if os.path.isfile(ei):
        os.remove(ei)
    return 0, diff


def compare(act, relay=RELAY):
    """dict: the scratch table against the tracked one in the tree, by row (grade, profile, provenance), and the tracked five files' status."""
    sc = os.path.join(folder(act), 'terminal_table.json')
    tr = os.path.join(relay, 'data', 'terminal_table.json')
    a = _rows_state(json.load(io.open(tr, encoding='utf-8'))['rows']) if os.path.isfile(tr) else {}
    b = _rows_state(json.load(io.open(sc, encoding='utf-8'))['rows']) if os.path.isfile(sc) else {}
    st = subprocess.run(['git', '-C', relay, 'status', '--porcelain', '--'] + ['data/' + f for f in FILES], capture_output=True, text=True).stdout
    return dict(tracked=len(a), scratch=len(b), added=sorted(set(b) - set(a)), gone=sorted(set(a) - set(b)),
                moved=sorted(k for k in set(a) & set(b) if a[k] != b[k]), status=[l for l in st.split(NL) if l.strip()])


def main(argv):
    if len(argv) != 1:
        sys.exit(__doc__)
    act = argv[0]
    rc, diff = regenerate(act)
    c = compare(act)
    print('### THE TERMINAL TABLE REGENERATED TO %s: exit %d ; rows %d against the tracked %d ; added %d, gone %d, moved %d ; the tracked five files '
          'in the tree: %s' % (folder(act).replace('\\', '/'), rc, c['scratch'], c['tracked'], len(c['added']), len(c['gone']), len(c['moved']),
                               'CLEAN' if not c['status'] else ' ; '.join(c['status'])))
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
