# -*- coding: utf-8 -*-
"""tools/b756_faults.py -- b756, (R366)(6): THE FAULTS OF data/b755_carried_faults.txt AND data/b755_defects.txt THAT HAVE REPEATED IN TWO ACTS
OR MORE, IN DESCENDING COUNT, read from the banks and not typed. Two counts, each by its own reading:
  - a lettered row (b755's defects (a)-(s); the carried rows (1)-(6), b754's letters): the acts of its REPEAT chain, each link read from the
    row's own tag in data/<act>_defects.txt ("[CLOSE ; REPEAT b754 (a'')]", "REPEAT the class of b753 (s')"), b756's rows that repeat a b755
    row added; distinct acts counted, a link to the same act adding none; a link to an events row or a row not found ends the chain, printed
  - a gate or arm row (the carried rows (8)-(11)): the acts whose suite banks (data/<act>_checks.txt, data/<act>_checks_postpush.txt) list the
    arm among LIVE FAILING, the reading of tools/standing/postseal.py failed_before
The rest of the carried rows (no letter, no arm) are counted by the defects and events banks of b755 and b756 that name their file: the
message's act (b754) and each act whose bank names it.
Controls first: the chain reader on b755 (r) (a link within b755: one act), the arm reader against postseal.failed_before, a planted row.
  python -X utf8 -u tools/b756_faults.py [--bank]
"""
import io
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, 'data')
NL = chr(10)
sys.path.insert(0, HERE)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from standing import postseal as PSL  # noqa: E402

ACT, PREV = 'b756', 'b755'
FIRST = 600   # the earliest act whose banks the readers open
ROW = re.compile(r"^ {4}\(([a-z]+[`'’]*)\) [^\[\n]*\[(?:CLAIM|CLOSE)\s*;\s*([^\]\n]*)\]", re.M)
LINK = re.compile(r"REPEAT (?:the class of )?(?:(b\d{3}) )?(events )?\(([a-z0-9]+[`'’]*)\)")
FAILING = re.compile(r'LIVE FAILING : \d+ \[([^\]]*)\]')
CARRIED = re.compile(r'^ {3,4}\((\d+)\) (.*)$')
B754_LETTER = re.compile(r"b754 \(([a-z]+[`'’]*)\)")
ARM = re.compile(r'\b(G-[A-Z0-9-]+)\b')
FILE = re.compile(r'((?:tools/)?[\w/]*?[\w.-]+\.(?:py|tpl)) :(\d+)')

# ### where each repair would stand, read by the seat from the rows (a place, or why no tool change answers the row)
PLACE = {
    ('b755', 'a'): 'none: the seat`s read of its words (no tool reads a semicolon; seatfile.py :134 the rule)',
    ('b755', 'b'): 'tools/standing/subject.py :249-:253 (the corpus case keyed on fixed line numbers)',
    ('b755', 'c'): 'answered at b755 (commit.py ACT_PHASES; this act commits under component 5)',
    ('b755', 'd'): 'tools/standing/wlist.py :126-:134 (the patterns wider than the ruling)',
    ('b755', 'e'): 'tools/standing/carry.py (the address scan`s N5 heading shifted with the ruling`s name)',
    ('b755', 'f'): 'none: the seat`s order of the restatement',
    ('b755', 'g'): 'none: the seat`s flag read before each route',
    ('b755', 'n'): 'tools/standing/carry.py (a carried cite shifted to a bank absent from the tree, printed at the carry)',
    ('b755', 'o'): 'tools/standing/commit.py (a shared file committed with act_current`s shared_edits not naming it)',
    ('b755', 'p'): 'none: the act module`s own clauses',
    ('b755', 'r'): 'none: the act module`s own clauses',
    ('carried', 1): 'tools/standing/gitwrite.py RUNS_COMMIT (a compile of the one-call tool read as its run)',
    ('carried', 2): 'tools/standing/gitwrite.py (a run of the one-call tool inside a PowerShell block read as no git write)',
    ('carried', 4): 'none: the words of a ruling and of the entry, the seat`s (with row (23))',
    ('carried', 6): 'tools/standing/fold/record.tpl :194, DEFECT_ROW bound to a matcher of one prime (row (12), the same place)',
    ('carried', 23): 'none: the words of a ruling, the author`s (with row (4))',
}


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def norm(letter):
    return re.sub("[`’]", "'", letter)


_ROWS = {}


def rows_of(act):
    if act not in _ROWS:
        _ROWS[act] = dict((norm(m.group(1)), m.group(2).strip()) for m in ROW.finditer(rd(os.path.join(D, '%s_defects.txt' % act))))
    return _ROWS[act]


def chain(act, letter, rows=rows_of):
    """[(act, letter, tag)] from the row back along its REPEAT links; the end's reason last."""
    out, seen = [], set()
    while (act, letter) not in seen:
        seen.add((act, letter))
        tag = rows(act).get(letter)
        if tag is None:
            out.append((act, letter, 'ROW NOT FOUND'))
            break
        out.append((act, letter, tag))
        m = LINK.search(tag)
        if not m:
            break
        if m.group(2):
            out.append((m.group(1) or act, m.group(3), 'AN EVENTS ROW: THE CHAIN ENDS'))
            break
        act, letter = m.group(1) or act, norm(m.group(3))
    return out


def chain_acts(ch):
    return sorted(set(a for a, _l, t in ch if t not in ('ROW NOT FOUND', 'AN EVENTS ROW: THE CHAIN ENDS')), key=lambda a: int(a[1:]))


def forward(prev_letter):
    """b756's rows whose tag repeats b755's row."""
    return [(ACT, l) for l, t in rows_of(ACT).items() if any((m.group(1) == PREV and norm(m.group(3)) == prev_letter and not m.group(2))
                                                             for m in LINK.finditer(t))]


def arm_acts(arm, last=int(ACT[1:])):
    out = []
    for n in range(FIRST, last):
        a = 'b%d' % n
        for f in ('%s_checks.txt' % a, '%s_checks_postpush.txt' % a):
            if any("'%s'" % arm in x or '"%s"' % arm in x for x in FAILING.findall(rd(os.path.join(D, f)))):
                out.append(a)
                break
    return out


def named_acts(path, line):
    """the acts of b755 and b756 whose defects or events bank names the file at the line the message cites (the basename alone met record.tpl
    in banks that cite another of its lines: the reading is the file and its line)."""
    pat = re.compile(re.escape(os.path.basename(path)) + r' :' + line + r'(?!\d)')
    return sorted(set(a for a in (PREV, ACT) for k in ('defects', 'events') if pat.search(rd(os.path.join(D, '%s_%s.txt' % (a, k))))),
                  key=lambda a: int(a[1:]))


def controls():
    L, ok = [], []
    ch = chain('b755', 'r')
    c1 = chain_acts(ch) == ['b755'] and [x[1] for x in ch] == ['r', 'p']
    L.append('  (chain) b755 (r), its link to b755 (p) within the act: acts %s ; letters %s -> %s' % (chain_acts(ch), [x[1] for x in ch], 'AS WANTED' if c1 else 'NOT AS WANTED'))
    ok.append(c1)
    plant = {'b999': {'a': "REPEAT b998 (b')"}, 'b998': {"b'": 'NEW'}}
    ch2 = chain('b999', 'a', rows=lambda a: plant.get(a, {}))
    c2 = chain_acts(ch2) == ['b998', 'b999']
    L.append('  (chain) PLANTED: b999 (a) REPEAT b998 (b`), b998 (b`) NEW: acts %s -> %s' % (chain_acts(ch2), 'AS WANTED' if c2 else 'NOT AS WANTED'))
    ok.append(c2)
    ps = PSL.failed_before(ACT)
    mine = arm_acts(PSL.ARM)
    c3 = set(ps) <= set(mine) and len(mine) >= len(ps)
    L.append('  (arm) %s: postseal.failed_before %d acts (the combined banks) ; this reader %d (combined and post-push) ; the first within the second %s -> %s' % (
        PSL.ARM, len(ps), len(mine), set(ps) <= set(mine), 'AS WANTED' if c3 else 'NOT AS WANTED'))
    ok.append(c3)
    c4 = arm_acts('G-PLANTED-NO-SUCH-ARM') == []
    L.append('  (arm) PLANTED: an arm no bank names: acts %s -> %s' % (arm_acts('G-PLANTED-NO-SUCH-ARM'), 'AS WANTED' if c4 else 'NOT AS WANTED'))
    ok.append(c4)
    return L, ok


def faults():
    out = []
    for l in sorted(rows_of(PREV), key=lambda x: (len(x), x)):
        ch = chain(PREV, l)
        fw = forward(l)
        acts = sorted(set(chain_acts(ch)) | set(a for a, _ in fw), key=lambda a: int(a[1:]))
        out.append(dict(src='%s (%s)' % (PREV, l), count=len(acts), acts=acts, how='the REPEAT chain %s%s' % (
            ' <- '.join('%s (%s)' % (a, x) for a, x, _t in ch), (' ; repeated at ' + ', '.join('%s (%s)' % f for f in fw)) if fw else ''),
            end=ch[-1][2] if ch[-1][2] in ('ROW NOT FOUND', 'AN EVENTS ROW: THE CHAIN ENDS') else '',
            place=PLACE.get((PREV, l), '')))
    for line in rd(os.path.join(D, '%s_carried_faults.txt' % PREV)).split(NL):
        m = CARRIED.match(line)
        if not m:
            continue
        k, body = int(m.group(1)), m.group(2)
        lm = B754_LETTER.search(body)
        am = ARM.search(body) if k in (8, 9, 10, 11) else None
        fm = FILE.search(body)
        if lm:
            ch = chain('b754', norm(lm.group(1)))
            acts = chain_acts(ch)
            how = 'the REPEAT chain ' + ' <- '.join('%s (%s)' % (a, x) for a, x, _t in ch)
        elif am:
            acts = arm_acts(am.group(1))
            how = 'the suite banks listing %s LIVE FAILING' % am.group(1)
        else:
            acts = sorted(set(['b754'] + (named_acts(fm.group(1), fm.group(2)) if fm else [])), key=lambda a: int(a[1:]))
            how = 'b754`s message%s' % ((' and the defects and events banks of b755 and b756 naming %s :%s' % (os.path.basename(fm.group(1)), fm.group(2))) if fm else '')
        out.append(dict(src='carried (%d)' % k, count=len(acts), acts=acts, how=how, end='', place=PLACE.get(('carried', k)) or (fm.group(0) if fm else body[:90])))
    return sorted(out, key=lambda r: (-r['count'], r['src']))


def main(argv):
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- (R366)(6): THE FAULTS OF data/%s_carried_faults.txt AND data/%s_defects.txt BY THE ACTS THEY STAND IN, DESCENDING (%s)' % (ACT, PREV, PREV, t0), '',
         '### read from the banks by tools/%s_faults.py; the controls first; the four hours of (6) read from the first repair`s start' % ACT, '',
         '## THE CONTROLS, BEFORE ANY COUNT']
    cl, ok = controls()
    L += cl
    L.append('### THE CONTROLS : %d OF %d AS WANTED' % (sum(ok), len(ok)))
    if not all(ok):
        print(NL.join(L))
        return 1
    fs = faults()
    two = [f for f in fs if f['count'] >= 2]
    L += ['', '## THE FAULTS, DESCENDING (count = distinct acts)']
    for f in fs:
        L.append('  %-14s %3d  %s' % (f['src'], f['count'], ', '.join(f['acts'])))
        L.append('      by %s%s' % (f['how'], (' ; ' + f['end']) if f['end'] else ''))
        if f['place']:
            L.append('      the place: %s' % f['place'])
    L += ['', '### ### **THE FAULTS : %d ROWS ; IN TWO ACTS OR MORE %d (%s) ; IN ONE ACT %d.**' % (
        len(fs), len(two), ', '.join('%s %d' % (f['src'], f['count']) for f in two), len(fs) - len(two))]
    print(NL.join(L))
    if '--bank' in argv:
        p = os.path.join(D, '%s_faults.txt' % ACT)
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_faults.txt' % ACT)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
