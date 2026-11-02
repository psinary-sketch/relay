# -*- coding: utf-8 -*-
"""standing/prelock.py -- v1.13.0, (R343)(2)(i), b732 event (3): THE PRE-LOCK FAILING-LIST COMPARISON. A pending arm hid a dead one: b732's G-RUNNER-GATE and G-DELETES-ONE-BRANCH
failed at the probes before its lock, and the failing lists were read against b731's only after it. The act's probes (data/<act>_checks_<part>.txt, every part) are read against the
previous act's pre-run lists (data/<prev>_arms_prerun_<part>.txt) by arm name, and every arm newly failing printed by name BEFORE THE LOCK GATE, the gate NOT CLEAR while one of them is
not named on the face. A ruling's own arm (G-R343-ENTERED against G-R342-ENTERED) is the same arm. The list is whole-suite: an arm a part moved is not newly failing.

  python -X utf8 -u tools/standing/prelock.py print [<act>]
        the comparison, printed, nothing written
  gate(act, face)     the registration gate's route: writes data/<act>_prelock.txt, returns (clear, lines)
  stands(act)         the seal's reading: the bank stands and its foot reads CLEAR
"""
import json
import os
import re
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
PARTS = ('act', 'standing-a', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'standing-c')
ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(?:PASS|FAIL|[A-Z]+)\s+(?:PASS|FAIL|[A-Z]+)\s+(?:PASS|FAIL|[A-Z]+)\s+[0-9.]+\s+(.*)$')
RULING_ARM = re.compile(r'^G-R[0-9]+-')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def prev_of(act):
    return 'b%d' % (int(act[1:]) - 1)


def failing(text):
    """the arms a suite bank's rows print as failing, a declared failure among them, {name: verdict}."""
    out = {}
    for l in text.split(NL):
        m = ROW.match(l)
        if m and m.group(2).startswith('### FAILS'):
            out[m.group(1)] = m.group(2)
    return out


def rows_of(text):
    return [m.group(1) for m in map(ROW.match, text.split(NL)) if m]


def norm(name):
    return RULING_ARM.sub('G-R<ruling>-', name)


def compare(act, prev=None, form='%s_probe_%s.txt'):
    """dict(act, prev, missing parts, failing and previous failing, each whole-suite, newly [(part, arm, verdict)]). `form` the act's banks: the probes by default."""
    prev = prev or prev_of(act)
    mine, theirs, missing, arms, part_of = {}, {}, [], 0, {}
    for q in PARTS:
        pa, pb = form % (act, q), '%s_arms_prerun_%s.txt' % (prev, q)
        for name, sink in ((pa, mine), (pb, theirs)):
            if not os.path.exists(os.path.join(D, name)):
                missing.append(name)
                continue
            t = rd(name)
            f = failing(t)
            sink.update(f)
            if sink is mine:
                arms += len(rows_of(t))
                part_of.update((a, q) for a in f)
    was = set(norm(a) for a in theirs)
    newly = [(part_of[a], a, mine[a]) for a in sorted(mine) if norm(a) not in was]
    return dict(act=act, prev=prev, missing=missing, arms=arms, mine=mine, theirs=theirs, newly=newly)


def lines(c, face=None):
    L = ['%s -- THE PRE-LOCK FAILING-LIST COMPARISON, (R343)(2)(i): THE ACT`S PROBES AGAINST %s`S PRE-RUN LISTS, BY ARM NAME, A RULING`S OWN ARM THE SAME ARM ACROSS ACTS' % (c['act'], c['prev']),
         '  arms read %d ; failing here %d ; failing at %s`s pre-run %d ; banks absent %s' % (c['arms'], len(c['mine']), c['prev'], len(c['theirs']), c['missing'] or 'NONE')]
    undecl = []
    for q, a, v in c['newly']:
        on = None if face is None else (a in face)
        if on is False:
            undecl.append(a)
        L.append('  NEWLY FAILING  %-34s %-12s %s%s' % (a, q, v, '' if on is None else (' ; ON THE FACE' if on else ' ; NOT ON THE FACE')))
    L.append('  ### NEWLY FAILING %d%s' % (len(c['newly']), '' if c['newly'] else ': NONE'))
    return L, undecl


def gate(act, face):
    """the gate's step: clear where every bank reads and every arm newly failing is on the face; the bank written either way, its foot the verdict."""
    c = compare(act)
    L, undecl = lines(c, face)
    clear = not c['missing'] and not undecl
    L.append('### ### **THE PRE-LOCK COMPARISON : %s** (arms not on the face: %s)' % ('CLEAR' if clear else 'NOT CLEAR', undecl or 'NONE'))
    with open(os.path.join(D, '%s_prelock.txt' % act), 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    return clear, L


def stands(act):
    p = '%s_prelock.txt' % act
    return os.path.exists(os.path.join(D, p)) and '**THE PRE-LOCK COMPARISON : CLEAR**' in rd(p)


if __name__ == '__main__':
    a_ = sys.argv[2] if len(sys.argv) > 2 else json.load(open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['act']
    print(NL.join(lines(compare(a_))[0]))
