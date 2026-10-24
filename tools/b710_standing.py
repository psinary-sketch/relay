# -*- coding: utf-8 -*-
"""b710_standing.py -- (R320)(4), W-ORD-STANDING-CLAUSES-BANK (PLACE-papers OPEN_TRAILS :15450) TAKEN UP: the ferry's standing procedural
paragraph and the clauses of Components 5 and 6, as (R319)'s ferry carries them (relay data/b709_ferry.txt :49, :43, :45), written verbatim into
data/standing_clauses_v1.txt, one clause per row, each row numbered and tagged; and the control: the three lines re-assembled from the bank equal
to the ferry as banked at b709, line for line.

### THE CUT: each source line is cut into clauses at "; " and at ". " before a capital, never inside a “...” quotation; a Component line's head
### ("COMPONENT 5 - THE SEAL AND THE SUITE: ") is its own row. Each row stores its clause verbatim on a line of its own (six spaces, then the
### clause) and its separator by name (SEMI "; ", STOP ". ", COLON ": ", END nothing), so the line re-assembles by concatenation.
### THE KIND: STANDING, or ACT where the clause names the act it was written for or its predecessor (b708, b709) or its ruling ((R318), (R319)),
### or quotes the act's own entry title -- an ACT row is that ferry's delta, carried by a later ferry as its own delta, not by version.
### THE TAG, read from the record: a clause naming its own source (a rules bank row, data/bNNN_rules.txt; a ruling's clause, (Rnnn)(k)) is tagged
### with it; otherwise the earliest banked ferry (relay data/bNNN_ferry.txt) whose text carries the clause verbatim, white space joined, names the
### ruling that introduced it; a clause first located in the earliest ferry bank, or located in none, is tagged "carried".
### Routes: `write [dry]` -> data/standing_clauses_v1.txt ; `control` -> data/b710_standing_control.txt (.json). Writes only those banks.
"""
import glob
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = 'b709_ferry.txt'
LINES = ((49, 'the standing procedural paragraph'), (43, 'Component 5, the seal and the suite'), (45, 'Component 6, the record and the mirror'))
BANK = 'standing_clauses_v1.txt'
SEPS = {'SEMI': '; ', 'STOP': '. ', 'COLON': ': ', 'END': ''}
ACT_RX = re.compile(r'\bb70[89]\b|\(R31[89]\)')


def rd(name):
    p = os.path.join(D, name)
    return open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def cut(line):
    """[(clause, sep)]: the head of a Component line, then the clauses at "; " and at ". " before a capital, outside “...”."""
    out = []
    m = re.match(r'^(COMPONENT \d+ - [A-Z ,]+?): ', line)
    rest = line
    if m:
        out.append((m.group(1), 'COLON'))
        rest = line[m.end():]
    depth, start, i = 0, 0, 0
    while i < len(rest):
        ch = rest[i]
        if ch == '“':
            depth += 1
        elif ch == '”':
            depth = max(0, depth - 1)
        elif depth == 0 and rest.startswith('; ', i):
            out.append((rest[start:i], 'SEMI'))
            i += 2
            start = i
            continue
        elif depth == 0 and rest.startswith('. ', i) and i + 2 < len(rest) and rest[i + 2].isupper():
            out.append((rest[start:i], 'STOP'))
            i += 2
            start = i
            continue
        i += 1
    out.append((rest[start:], 'END'))
    return out


def _ws(s):
    return ' '.join(s.split())


def ferries():
    """[(act number, ruling, text joined)] for every banked ferry relay data/bNNN_ferry.txt, in act order."""
    out = []
    for p in glob.glob(os.path.join(D, 'b[0-9][0-9][0-9]_ferry.txt')):
        n = int(os.path.basename(p)[1:4])
        if n > 709:
            continue   # ### the record up to (R319)'s ferry; this act's own ferry is not the clauses' source
        t = open(p, encoding='utf-8', errors='replace').read()
        m = re.search(r'RULING \((R\d+)\)', t)
        out.append((n, m.group(1) if m else None, _ws(t)))
    return sorted(out)


def tag_of(clause, F):
    own = re.findall(r'data/b\d{3}_rules\.txt row \(?\d+\)?|\(R\d+\)\(\d+\)', clause)
    first = next(((n, r) for n, r, t in F if _ws(clause) in t), None)
    loc = 'first carried in data/b%03d_ferry.txt%s' % (first[0], (' under (%s)' % first[1]) if first[1] else '') if first else 'in no banked ferry but b709`s'
    if own:
        return 'SOURCE %s ; %s' % (', '.join(dict.fromkeys(own)), loc), first
    if first and first[0] != F[0][0]:
        return 'RULING (%s) ; %s' % (first[1] or '?', loc), first
    return 'carried ; %s' % loc, first


def rows():
    f = rd(SRC).split(NL)
    F = ferries()
    R = []
    n = 0
    for ln, what in LINES:
        for clause, sep in cut(f[ln - 1]):
            n += 1
            kind = 'HEAD' if sep == 'COLON' else ('ACT' if (ACT_RX.search(clause) or '“' in clause) else 'STANDING')
            tag, first = tag_of(clause, F)
            R.append(dict(n=n, line=ln, what=what, kind=kind, sep=sep, tag=tag, first=first[0] if first else None, clause=clause))
    return R, F


def write(*a):
    R, F = rows()
    L = ['b710 -- THE STANDING CLAUSES, VERSION 1, BANKED ONCE UNDER (R320)(4) FROM (R319)`S FERRY AS BANKED AT b709 (relay data/b709_ferry.txt) (%s)' % utc(), '',
         'VERSION: 1',
         'THE CITATION FORM: a ferry names "standing clauses v1" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces. KIND: STANDING (carried',
         '### by version), ACT (the act`s own delta in b709`s ferry: it names b708, b709, (R318) or (R319), or quotes the entry title), HEAD (a Component',
         '### line`s head). SEP: the separator after the clause (SEMI "; ", STOP ". ", COLON ": ", END none) -- the source line re-assembles by',
         '### concatenation. TAG: the clause`s own cited source where it names one; else the earliest banked ferry carrying it verbatim (%d ferry banks read,' % len(F),
         '### data/b%03d_ferry.txt to data/b%03d_ferry.txt) with its ruling; "carried" where the first located is the earliest bank or none.' % (F[0][0], F[-1][0])]
    cur = None
    for r in R:
        if r['line'] != cur:
            cur = r['line']
            L += ['', '## LINE %d OF data/b709_ferry.txt -- %s' % (cur, r['what'])]
        L.append('  (%d) %s %s %s' % (r['n'], r['kind'], r['sep'], r['tag']))
        L.append('      ' + r['clause'])
    k = dict((x, sum(1 for r in R if r['kind'] == x)) for x in ('STANDING', 'ACT', 'HEAD'))
    tg = dict((x, sum(1 for r in R if r['tag'].startswith(x))) for x in ('SOURCE', 'RULING', 'carried'))
    L += ['', '### ### **ROWS %d ; STANDING %d ; ACT %d ; HEAD %d ; TAGGED BY THEIR OWN SOURCE %d, BY THE RULING THAT FIRST CARRIED THEM %d, CARRIED %d ; FROM THE THREE LINES :49, :43, :45.**' % (
        len(R), k['STANDING'], k['ACT'], k['HEAD'], tg['SOURCE'], tg['RULING'], tg['carried'])]
    if 'dry' in a:
        print(NL.join(L[:12] + L[-1:]))
        return
    p = os.path.join(D, BANK)
    import subprocess
    tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', 'data/' + BANK], capture_output=True).returncode == 0
    if tracked or (os.path.exists(p) and 'again' not in a):
        sys.exit('### data/%s EXISTS%s -- A VERSION IS WRITTEN ONCE; NOTHING WRITTEN' % (BANK, ' AND IS COMMITTED' if tracked else ' (give `again` while it is uncommitted)'))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


def parse(text):
    """the bank's rows read back: [(n, kind, sep, tag, clause, line)] -- the reader the re-assembly and the arms use."""
    out, cur = [], None
    T = text.split(NL)
    for i, l in enumerate(T):
        m = re.match(r'^## LINE (\d+) OF ', l)
        if m:
            cur = int(m.group(1))
        m = re.match(r'^  \((\d+)\) (STANDING|ACT|HEAD) (SEMI|STOP|COLON|END) (.*)$', l)
        if m and i + 1 < len(T) and T[i + 1].startswith('      '):
            out.append((int(m.group(1)), m.group(2), m.group(3), m.group(4), T[i + 1][6:], cur))
    return out


def reassemble(text):
    """{source line: the line re-assembled from the bank's rows}."""
    out = {}
    for n, kind, sep, tag, clause, ln in parse(text):
        out[ln] = out.get(ln, '') + clause + SEPS[sep]
    return out


def control(*a):
    bank = rd(BANK)
    f = rd(SRC).split(NL)
    ra = reassemble(bank)
    R = []
    for ln, what in LINES:
        got = ra.get(ln, '')
        R.append(dict(line=ln, what=what, equal=got == f[ln - 1], chars=len(f[ln - 1]), got_chars=len(got)))
    rows_ = parse(bank)
    if bank.count('and no pipe in any command') != 1:
        sys.exit('### THE NEG CONTROL`S NEEDLE IS NOT IN THE BANK ONCE -- NOTHING WRITTEN')
    neg = bank.replace('and no pipe in any command', 'and no pipe in a command', 1)
    neg_eq = reassemble(neg).get(49, '') == f[48]
    ver = re.search(r'^VERSION: (\d+)$', bank, re.M)
    L = ['b710 -- COMPONENT 2, (R320)(4): THE RE-ASSEMBLY CONTROL -- THE THREE LINES OF (R319)`S FERRY RE-ASSEMBLED FROM data/standing_clauses_v1.txt AGAINST THE FERRY AS BANKED AT b709 (%s)' % utc(), '',
         '### rows are source lines: the line of relay data/b709_ferry.txt | what it is | its characters | the re-assembled characters | EQUAL. The bank`s',
         '### rows read back by its own parser (tools/b710_standing.py parse): %d ; its version line %s. The NEG control: one clause altered in a copy of the' % (len(rows_), ver.group(1) if ver else 'NONE'),
         '### bank ("no pipe in any command" to "no pipe in a command"), the paragraph re-assembled from it compared again.', '']
    L += ['  :%d | %-40s | %5d | %5d | EQUAL %s' % (r['line'], r['what'], r['chars'], r['got_chars'], r['equal']) for r in R]
    L += ['  NEG: the altered copy`s :49 re-assembled EQUAL %s (wanted False)' % neg_eq]
    ok = all(r['equal'] for r in R) and not neg_eq and bool(ver) and ver.group(1) == '1'
    L += ['', '### ### **LINES 3 ; EQUAL LINE FOR LINE %s ; THE NEG COPY DIFFERS %s ; ROWS %d ; VERSION 1 %s ; THE CONTROL AS WANTED %s.**' % (
        all(r['equal'] for r in R), not neg_eq, len(rows_), bool(ver) and ver.group(1) == '1', ok)]
    if 'dry' not in a:
        for name, data in (('b710_standing_control.txt', (NL.join(L) + NL)), ('b710_standing_control.json', json.dumps(dict(at=utc(), rows=R, neg_equal=neg_eq, ok=ok, n=len(rows_)), indent=1) + NL)):
            p = os.path.join(D, name)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(data.encode('utf-8'))
            os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))
    if not ok:
        sys.exit(1)


def readers(*a):
    """data/b710_standing_readers.txt (.json), (R320)(4): the readers of the ferry's text repointed to read the bank by version, each read on three
    texts -- one naming "standing clauses v1", one naming a version not banked ("standing clauses v2"), one naming none -- the ferry scan
    (tools/ferry_scan.py bank_citation_check) and the citation tool (tools/b710_citation.py standing_rows); G-RECEIPT-IN-FULL is the suite's and
    is read at Component 5 by the suite's own pre-run."""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan as FS
    import b710_citation as CI
    texts = (('names v1', 'the ferry carries standing clauses v1 and its deltas'), ('names v2, not banked', 'the ferry carries standing clauses v2'),
             ('names none', 'the ferry carries its procedural paragraph in full'))
    want_fs = {'names v1': 'CURRENT', 'names v2, not banked': 'NO BANK', 'names none': 'NONE'}
    want_ci = {'names v1': [True], 'names v2, not banked': [False], 'names none': []}
    R, ok = [], True
    for name, t in texts:
        fs = FS.bank_citation_check(t)[0]
        got = []
        CI.standing_rows(t, lambda where, what, o, how, comp: got.append(bool(o)))
        r = dict(text=name, ferry_scan=fs, ferry_scan_wanted=want_fs[name], citation=got, citation_wanted=want_ci[name])
        r['as_wanted'] = fs == want_fs[name] and got == want_ci[name]
        ok = ok and r['as_wanted']
        R.append(r)
    L = ['b710 -- COMPONENT 2, (R320)(4): THE READERS OF THE FERRY`S TEXT REPOINTED TO READ THE STANDING CLAUSES BY VERSION, EACH ON THREE TEXTS (%s)' % utc(), '',
         '### rows are texts: the text | the ferry scan`s reading (wanted) | the citation tool`s rows (wanted) | AS WANTED. The banks present: %s.' % FS.bank_versions(), '']
    L += ['  %-22s | ferry_scan %-8s (wanted %-8s) | citation %-8s (wanted %-8s) | %s' % (r['text'], r['ferry_scan'], r['ferry_scan_wanted'], r['citation'], r['citation_wanted'],
                                                                                         'AS WANTED' if r['as_wanted'] else '### NOT AS WANTED') for r in R]
    L += ['', '### ### **TEXTS 3 ; READERS 2 (THE FERRY SCAN, THE CITATION TOOL) ; AS WANTED %s ; G-RECEIPT-IN-FULL READ AT COMPONENT 5.**' % ok]
    if 'dry' not in a:
        for name, data in (('b710_standing_readers.txt', NL.join(L) + NL), ('b710_standing_readers.json', json.dumps(dict(at=utc(), rows=R, ok=ok), indent=1) + NL)):
            p = os.path.join(D, name)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(data.encode('utf-8'))
            os.replace(p + '.tmp', p)
    print(NL.join(L[4:]))
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    fn = {'write': write, 'control': control, 'readers': readers}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b710_standing.py write [dry] | control [dry] | readers [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
