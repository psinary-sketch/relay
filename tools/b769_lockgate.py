# -*- coding: utf-8 -*-
"""tools/b769_lockgate.py -- b769: THE LOCK GATE WITH THE HANDOFF CENSUS READ AS STOPPED, the ferry's Component 5 under (R379) (data/b769_ferry.txt :179): carried from
tools/b768_lockgate.py by tools/b769_carry.py (data/b769_carry_lockgate.txt) and committed before it runs. b754's lift, from b754's defect
(r'') and the author's answer data/b754_put_11.json, option 2, "Lock gate and census stopped" (2026-11-14T10:23:59.652Z, data/b754_author_answers.txt
:192). ### b769, the carry's note: the substitution b768 -> b769 alone, which moved no citation of b754's banks or of (R364)(5)[H1]
(:3-:5, :11-:12, :105-:106 read after it); the ferry's line at :2, which the shift carried as b769's :100, b768's line under b769's name,
where b769's ferry of 184 lines holds its Component 5 at :179 (the carry's [K2] reader printed it OWN, data/b769_carry_lockgate.txt :11),
set by the Edit tool before any run to b769's :179, which orders "THE LOCK, THE SUITE, THE RECORD, THE MIRROR AND THE PROJECT SET, as the
standing clauses, [K24] and [K29] order them" (:2 here, the notes at :105); N2 named under (R379) (:23).

b378's gate (tools/b378_lockgate.py) is imported and run unedited, except that its second gate, the handoff census of step zero (GATES[1],
data/<act>_census_stepzero.txt), takes as its pass the line tools/b307_handoff_census.py prints since that answer (its STOPPED constant,
"THE HANDOFF COUNT STOPPED by (R364)(5)[H1] (a)") in place of "TOTAL MISSING : 0": (R364)(5)[H1] passed as (a), "the close's count against
the page stops" (data/b754_ferry.txt :42), and the census tool prints no total. The gate keeps its index, so b378's own fixtures, which plant
their modes at the face-subject gates 4, 5 and 6, run as written; the other seven gates, the probe-path refusal, the compile control and the
(R345)(2)(iv) reading are untouched. Before the gate runs, two controls, printed into the gate's notes through the gate's own recorder:
  (A) under b378's phrase, over this act's banks as they stand, the handoff census's gate fails, and each of the other seven gates reads as
      it reads under the lift;
  (B) under the lift, over a temp folder holding copies of the act's gate banks, a planted census bank carrying a total and no STOPPED line
      fails that gate and one carrying the STOPPED line passes it, each of the other seven gates reading as over the act's banks.
A control not as wanted refuses the run before the gate is called: nothing written. The mode `controls` prints the controls and the gates
under the lift and writes nothing. tools/standing/ does not move; b378's file and the templates are unchanged. Written by the Write tool;
committed before its run ((R379) N2, each generator commits before it runs).

  python -X utf8 -u tools/b769_lockgate.py controls b769 <face>
  python -X utf8 -u tools/b769_lockgate.py b769 <face>
"""
import io
import os
import shutil
import stat
import sys
import tempfile

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
sys.path.append(os.path.join(T, 'standing'))
import b378_lockgate as G          # noqa: E402  -- imported, not run: its main() is called below, unedited
import b307_handoff_census as H    # noqa: E402  -- the stopped count's own line, read from the tool that prints it

ACT = 'b769'
IDX = 1
B378 = ('the handoff census', '%s_census_stepzero.txt', 'TOTAL MISSING : 0', False)   # ### b378's gate as it stands (tools/b378_lockgate.py :45)
LIFT = (B378[0], B378[1], H.STOPPED, False)
PLANT_TOTAL = ('b307_handoff_census.py -- planted. ### WHAT IS MISSING FROM `HANDOFF.md`, COUNTED.\n'
               '  ### ### **TOTAL MISSING : 0**\n')
PLANT_STOPPED = ('b307_handoff_census.py -- planted. ### THE COUNT AGAINST `HANDOFF.md`, STOPPED.\n'
                 '  ### ### **%s**\n' % H.STOPPED)


def read_with(act, face, gates, directory=D):
    """b378's read_gates over `gates` in place of its GATES, which are restored after."""
    saved = list(G.GATES)
    try:
        G.GATES[:] = gates
        return G.read_gates(act, face, directory)
    finally:
        G.GATES[:] = saved


def _rm(path):
    def onerr(fn, p, _e):
        os.chmod(p, stat.S_IWRITE)
        fn(p)
    shutil.rmtree(path, onerror=onerr)


def census_line(act, directory=D):
    p = os.path.join(directory, B378[1] % act)
    if not os.path.exists(p):
        return 'ABSENT'
    ls = [l.strip() for l in io.open(p, encoding='utf-8', errors='replace').read().split('\n') if H.STOPPED in l or 'TOTAL MISSING' in l]
    return ' | '.join(ls) if ls else 'NEITHER A STOPPED LINE NOR A TOTAL'


def controls(act, face):
    base = list(G.GATES)
    shape_ok = len(base) == 8 and tuple(base[IDX]) == B378
    lifted = base[:IDX] + [LIFT] + base[IDX + 1:]
    others = [i for i in range(len(base)) if i != IDX]
    a = read_with(act, face, base)
    al = read_with(act, face, lifted)
    a_ok = shape_ok and not a[IDX]['passed'] and all(a[i]['passed'] == al[i]['passed'] for i in others)
    tmp = tempfile.mkdtemp(prefix='b769lg_')
    try:
        for _l, pat, _p, _s in base:
            src = os.path.join(D, pat % act)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(tmp, pat % act))
        cen = os.path.join(tmp, B378[1] % act)
        with open(cen, 'w', encoding='utf-8', newline='\n') as f:
            f.write(PLANT_TOTAL)
        bt = read_with(act, face, lifted, tmp)
        with open(cen, 'w', encoding='utf-8', newline='\n') as f:
            f.write(PLANT_STOPPED)
        bs = read_with(act, face, lifted, tmp)
    finally:
        _rm(tmp)
    removed = not os.path.exists(tmp)
    b_ok = (not bt[IDX]['passed']) and bs[IDX]['passed'] and removed and \
        all(bt[i]['passed'] == al[i]['passed'] and bs[i]['passed'] == al[i]['passed'] for i in others)
    pf = lambda g: 'PASS' if g['passed'] else 'FAIL'   # noqa: E731
    L = ['  ### THE FERRY`S COMPONENT 5 UNDER (R379), b754`S LIFT CARRIED (data/b754_put_11.json, option 2, "Lock gate and census stopped", 2026-11-14T10:23:59.652Z;',
         '  ### data/b754_author_answers.txt :192): b378`s gate %d, %s (data/%s), takes "%s" as its pass in place of "%s";' % (
             IDX, B378[0], B378[1] % act, H.STOPPED, B378[2]),
         '  ### b378`s gate otherwise unedited and its file unchanged (b378`s gate %d as read here %s, wanted %s: %s).' % (
             IDX, tuple(base[IDX]) if len(base) > IDX else 'ABSENT', B378, 'AS WANTED' if shape_ok else '### NOT AS WANTED'),
         '  ### the census bank as it stands: %s' % census_line(act),
         '  ### THE CONTROLS, BEFORE THE GATE:',
         '    (A) b378`s phrase over the act`s banks: the handoff census %s ; the other seven %s ; under the lift %s ; wanted FAIL and the seven' % (
             pf(a[IDX]), [pf(a[i]) for i in others], [pf(al[i]) for i in others]),
         '        equal ; %s' % ('AS WANTED' if a_ok else '### NOT AS WANTED'),
         '    (B) the lift over a temp folder of the act`s gate banks: a census bank carrying a total and no STOPPED line %s ; one carrying' % pf(bt[IDX]),
         '        the STOPPED line %s ; the other seven %s and %s against the act`s banks %s ; the temp folder removed %s ; wanted FAIL, PASS,' % (
             pf(bs[IDX]), [pf(bt[i]) for i in others], [pf(bs[i]) for i in others], [pf(al[i]) for i in others], removed),
         '        the seven equal and removed ; %s' % ('AS WANTED' if b_ok else '### NOT AS WANTED'),
         '  ### the gates under the lift over the act`s banks: %s ; passing %d of %d' % (
             ', '.join('%s %s' % (g['file'], pf(g)) for g in al), sum(1 for g in al if g['passed']), len(al)),
         '  ### ### **THE LIFT`S CONTROLS : %s**' % ('2 OF 2 AS WANTED' if a_ok and b_ok else '### NOT AS WANTED -- THE GATE NOT RUN, NOTHING WRITTEN'),
         '']
    return a_ok and b_ok, L


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    mode = 'run'
    if argv[:1] == ['controls']:
        mode, argv = 'controls', argv[1:]
    if len(argv) < 2 or argv[0] != ACT:
        print('usage: b769_lockgate.py [controls] b769 <face> -- this act`s tool, for b769 alone; nothing read, nothing written')
        return 2
    act, face = argv[0], argv[1]
    if not os.path.exists(face):
        print('### THE FACE DOES NOT EXIST: %s -- nothing read, nothing written' % face)
        return 2
    ok, L = controls(act, face)
    if mode == 'controls' or not ok:
        print('\n'.join(L))
        print('  ### the mode %s: nothing written' % mode)
        return 0 if ok else 2
    for ln in L:
        G.rec(ln)
    G.GATES[IDX] = LIFT
    G.rec('  ### THE LIFT SET: b378`s gate %d reads "%s" ; every other gate as b378 holds it' % (IDX, G.GATES[IDX][2]))
    G.rec('')
    return G.main(argv)


if __name__ == '__main__':
    sys.exit(main())
