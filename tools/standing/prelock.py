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
import subprocess
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
PARTS = ('act', 'standing-a', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'standing-c')   # ### the seven b706 split, where an act's own list cannot be read


def parts_of(act):
    """### v1.18.0, (R348)(2)(vi): an act's parts -- the current act's from data/act_current.json, an earlier act's from its own pre-run part banks
    (data/<act>_arms_prerun_<part>.txt); the parts split, the lists read by arm name across them (whole-suite)."""
    try:
        with open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
            cur = json.load(f)
        if cur.get('act') == act and cur.get('parts'):
            return tuple(cur['parts'])
    except (OSError, ValueError):
        pass
    pre = '%s_arms_prerun_' % act
    got = tuple(sorted(n[len(pre):-4] for n in os.listdir(D) if n.startswith(pre) and n.endswith('.txt')))
    return got or PARTS
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
    pairs = [(form % (act, q), mine, q) for q in parts_of(act)] + [('%s_arms_prerun_%s.txt' % (prev, q), theirs, q) for q in parts_of(prev)]
    for name, sink, q in pairs:
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
    dry = os.path.exists(os.path.join(D, '%s_scores_dry.txt' % act))   # ### v1.16.0, (R346)(3)(vi), b735 event (1): the score routes' dry form before the gate clears, the face's order the tool's
    L.append('  the score routes` dry form, data/%s_scores_dry.txt: %s' % (act, 'STANDS' if dry else '### ABSENT: `record scores dry` runs before the gate'))
    # ### v1.24.0, (R354)(2)(i), b743 events (3), (7): every part's sources() exercised in prev mode at the act module's present blob
    S_ = os.path.dirname(os.path.abspath(__file__))
    if S_ not in sys.path:
        sys.path.insert(0, S_)
    import prevdry as PD
    pv_clear, pv = PD.gate(act)
    L += pv
    # ### v1.24.0, (R354)(2)(iv), b743 events (15): the closing's tag requirement read at the pre-lock dry, so an untagged row cannot reach the record
    tag_ok, tag_line = tags(act)
    L.append(tag_line)
    clear = not c['missing'] and not undecl and dry and pv_clear and tag_ok
    L.append('### ### **THE PRE-LOCK COMPARISON : %s** (arms not on the face: %s)' % ('CLEAR' if clear else 'NOT CLEAR', undecl or 'NONE'))
    with open(os.path.join(D, '%s_prelock.txt' % act), 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    return clear, L


def tags(act, events=None, defects=None):
    """v1.24.0, (R354)(2)(iv): (ok, line) -- every row of the events and defects banks tagged as the closing's counter requires (standing.counter.items,
    which raises on an untagged row); texts given are read in place of the banks (a blob read at its commit). A bank not yet written reads as empty."""
    S_ = os.path.dirname(os.path.abspath(__file__))
    if S_ not in sys.path:
        sys.path.insert(0, S_)
    import counter as CN

    def rd_(n):
        p = os.path.join(D, n)
        return rd(n) if os.path.exists(p) else ''
    ev = rd_('%s_events.txt' % act) if events is None else events.replace('\r', '')
    df = rd_('%s_defects.txt' % act) if defects is None else defects.replace('\r', '')
    try:
        it = CN.items(df, ev)
    except ValueError as e:
        return False, '  THE TAGS ((R354)(2)(iv)): ### %s -- the closing would refuse it; tag it before the lock' % str(e).strip('# ')
    return True, '  THE TAGS ((R354)(2)(iv)): every row tagged, %d rows read' % len(it)


def scores_dry_order(act):
    """v1.16.0, (R346)(3)(vi): the commit first carrying data/<act>_scores_dry.txt against the act's lock commit, by ancestry. (first, lock, 'IN ORDER' or 'OUT OF ORDER' or 'NOT READ')."""
    def g(*a):
        return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8').stdout.strip()
    add = g('log', '--format=%h', '--diff-filter=A', '--', 'data/%s_scores_dry.txt' % act).split('\n')[-1]
    lock = g('log', '--format=%h', '--grep=^%s lock: ' % act, '-1')
    if not add or not lock:
        return add, lock, 'NOT READ'
    r = subprocess.run(['git', '-C', RELAY, 'merge-base', '--is-ancestor', add, lock + '~1'])
    return add, lock, 'IN ORDER' if r.returncode == 0 else 'OUT OF ORDER'


def stands(act):
    p = '%s_prelock.txt' % act
    return os.path.exists(os.path.join(D, p)) and '**THE PRE-LOCK COMPARISON : CLEAR**' in rd(p)


if __name__ == '__main__':
    a_ = sys.argv[2] if len(sys.argv) > 2 else json.load(open(os.path.join(D, 'act_current.json'), encoding='utf-8'))['act']
    print(NL.join(lines(compare(a_))[0]))
