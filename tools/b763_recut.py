# -*- coding: utf-8 -*-
"""b763 -- (R373)(10): data/b763_recut_inputs.txt, the declarations that compiled, listed by name, with the paper each is an input of:
the Epstein document's next edition for (7); One Page's next edition and the six papers of W-ORD-SIGN-SECTORS for (6).

THE NAMES. (6)'s by statement as tools/b763_outcomes.py's STMTS declares them, a statement's names listed where data/b763_outcomes.json
reads (6) LANDED and that statement compiled, and each of its names stands among the new names of the read of run 44625270777, every new
name there within the standard three (data/b763_dispatch_rows.json). The statement file's nineteen (OP19), which the author's word of
22:18:13Z places with (6), listed where the outcomes read it BUILT and the read of its run holds the nineteen within. (7)'s ten (CF10),
definitions of a Prop with no proof, listed where the outcomes read the statement compiled and the read of its run holds the ten within.
Not listed: the six names of [P1], declared before this act and printed at v0.42 by (6)'s clause; the orders of (8), which (10) names not.

THE PAPERS. One Page's next edition: the edition after day1/ONE_PAGE_PROOF_v2_0.md, b762's ((R373)(1)); the Epstein document's: after
phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, (10)'s keystone; each read present at PLACE-papers HEAD by its path, no line of a
paper read. The six papers of W-ORD-SIGN-SECTORS read at run time from its entry's line in OPEN_TRAILS.md at HEAD (the one line opening
"`W-ORD-SIGN-SECTORS` ENTERED"), cited by line and sha256 and never quoted: the backticked names after its "carried from `<path>` by" and
before "is read at each paper's next edition", each resolved to the one tracked file of that name with .md outside archive/ and outputs/,
the other tracked files bearing the name counted and not read.

usage:
  python -X utf8 -u tools/b763_recut.py controls   the planted controls, printed; nothing written
  python -X utf8 -u tools/b763_recut.py bank       the controls and the list; data/b763_recut_inputs.txt written
"""
import copy
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T_ = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T_)
D = os.path.join(RELAY, 'data')
if T_ not in sys.path:
    sys.path.insert(0, T_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b763_worklist as K   # noqa: E402
import b763_outcomes as O   # noqa: E402  (the names: STMTS, OP19, CF10, P1, B)

NL = '\n'
BANK = os.path.join(D, 'b763_recut_inputs.txt')
OUTJ = os.path.join(D, 'b763_outcomes.json')
ROWS = os.path.join(D, 'b763_dispatch_rows.json')
ONE_PAGE = 'day1/ONE_PAGE_PROOF_v2_0.md'
EPSTEIN = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'
ENTRY_HEAD = '`W-ORD-SIGN-SECTORS` ENTERED'
SIX_RX = re.compile(r"carried from `[^`]+` by (.+?),? is read at each paper's next edition")
NAME_RX = re.compile(r'`([^`]+)`')
RUN_FORM = '44625270777'   # ### the read of (S1)-(S5) with its 48 names (events (50))
SKIP = ('archive/', 'outputs/')


def die(m):
    print('REFUSED: ' + m)
    sys.exit(3)


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout if r.returncode == 0 else ''


def six_of(line):
    """the backticked names between "carried from `<path>` by" and "is read at each paper's next edition"; [] where the clause is absent."""
    m = SIX_RX.search(line or '')
    return NAME_RX.findall(m.group(1)) if m else []


def resolve(stem, rels):
    """the one tracked file <stem>.md outside archive/ and outputs/ (None where there is not exactly one), and how many other tracked
    files bear the name."""
    exact = [r for r in rels if r.rsplit('/', 1)[-1] == stem + '.md' and not r.startswith(SKIP)]
    others = [r for r in rels if r.rsplit('/', 1)[-1].startswith(stem) and r not in exact]
    return (exact[0] if len(exact) == 1 else None), len(others)


def listed(J, rows):
    """((6) rows (key, full names, cited, ok), statement file (names, ok), (7) (names, ok)), each ok read from the outcomes and the reads."""
    rd = dict((str(r.get('run')), r) for r in rows if r.get('kind') == 'read')

    def within(run, names):
        r_ = rd.get(str(run)) or {}
        nn = set((r_.get('new_names') or {}).keys())
        return r_.get('verdict') == 'KERNEL' and r_.get('new_all_within') is True and all(n in nn for n in names)
    form = J.get('form') or {}
    landed = str(form.get('outcome') or '').startswith('LANDED')
    st = dict((s.get('key'), s) for s in form.get('statements') or [])
    six = []
    for k, _s, ns, cited in O.STMTS:
        full = tuple(O.B + n for n in ns)
        six.append((k, full, cited, landed and (st.get(k) or {}).get('compiled') is True and within(RUN_FORM, full)))
    sf = J.get('statement_file') or {}
    sf_run = dict((f_[0], f_[1]) for f_ in sf.get('fields') or []).get('<run id>')
    sf_ok = sf.get('outcome') == 'BUILT' and bool(sf_run) and within(sf_run, O.OP19)
    ar = J.get('arith') or {}
    ar_ok = str(ar.get('outcome') or '').startswith('STATEMENT COMPILED') and bool(ar.get('run')) and within(ar.get('run'), O.CF10)
    return six, (O.OP19, sf_ok, sf_run), (O.CF10, ar_ok, ar.get('run'), ar.get('sha'))


def controls(J, rows):
    out = []
    pl = ('x carried from `a/b.md` by `P`, `Q` and `R`, is read at each paper' + "'" + 's next edition as a reading')
    out.append(('(1) the six-paper reader on a planted clause naming three', six_of(pl), ['P', 'Q', 'R']))
    out.append(('(2) the six-paper reader on a line without the clause', six_of('x carried by `P` and `Q`.'), []))
    out.append(('(3) the resolver: the live file of the name beside an archive copy, a version and a deposit',
                resolve('S', ['archive/x/S.md', 'p/S.md', 'p/S_v1.md', 'outputs/S.md']), ('p/S.md', 3)))
    out.append(('(4) the resolver on two live files of one name refuses', resolve('S', ['p/S.md', 'q/S.md'])[0], None))
    j5 = copy.deepcopy(J)
    for s in (j5.get('form') or {}).get('statements') or []:
        if s.get('key') == 'S2':
            s['compiled'] = False
    out.append(('(5) a statement read not compiled leaves its names unlisted, the others listed',
                [k for k, _f, _c, ok in listed(j5, rows)[0] if ok], ['S1', 'S3', 'S4', 'S5']))
    r6 = copy.deepcopy(rows)
    for r in r6:
        if r.get('kind') == 'read' and str(r.get('run')) == RUN_FORM:
            r['new_names'] = dict((n, v) for n, v in (r.get('new_names') or {}).items() if n != O.B + 'form_parity_split')
    out.append(('(6) a name missing from its run`s read leaves its statement unlisted', [k for k, _f, _c, ok in listed(J, r6)[0] if not ok], ['S4']))
    j7 = copy.deepcopy(J)
    j7['statement_file']['outcome'] = 'NOT BUILT'
    j7['arith']['outcome'] = 'NOT COMPILED'
    l7 = listed(j7, rows)
    out.append(('(7) the statement file read NOT BUILT and (7) read NOT COMPILED leave each unlisted', (l7[1][1], l7[2][1]), (False, False)))
    return [(w, g, e, g == e) for w, g, e in out]


def compose():
    J = json.load(io.open(OUTJ, encoding='utf-8'))
    rows = json.load(io.open(ROWS, encoding='utf-8'))
    rows = rows.get('rows', rows) if isinstance(rows, dict) else rows
    ctl = controls(J, rows)
    P = ['b763 -- (R373)(10): THE DECLARATIONS THAT COMPILED, BY NAME, WITH THE PAPER EACH IS AN INPUT OF (tools/b763_recut.py, %s)'
         % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '## THE CONTROLS']
    for w, g, e, o in ctl:
        P.append('  %s: %r -> %s' % (w, g, 'AS WANTED' if o else 'NOT AS WANTED (wanted %r)' % (e,)))
    n_ok = sum(1 for c in ctl if c[3])
    P.append('**CONTROLS %d OF %d AS WANTED.**' % (n_ok, len(ctl)))
    head = git(K.PP, 'rev-parse', 'HEAD').strip()
    rels = [r for r in git(K.PP, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL) if r.strip().endswith('.md')]
    ot = git(K.PP, 'show', 'HEAD:OPEN_TRAILS.md').split(NL)
    at = [i + 1 for i, l in enumerate(ot) if l.startswith(ENTRY_HEAD)]
    if len(at) != 1:
        die('THE ENTRY OF W-ORD-SIGN-SECTORS READ %d TIMES AT OPEN_TRAILS.md' % len(at))
    line = ot[at[0] - 1]
    six = six_of(line)
    if len(six) != 6:
        die('THE ENTRY`S CLAUSE NAMES %d PAPERS, NOT SIX' % len(six))
    res = [(s,) + resolve(s, rels) for s in six]
    if not all(p for _s, p, _n in res):
        die('A PAPER OF THE SIX RESOLVES TO NO ONE FILE: %s' % [s for s, p, _n in res if not p])
    for p in (ONE_PAGE, EPSTEIN):
        if p not in rels:
            die('%s NOT AT PLACE-papers HEAD' % p)
    s6, sf, ar = listed(J, rows)
    form = J.get('form') or {}
    P += ['', '## THE PAPERS (PLACE-papers at HEAD %s, each read by its path, no line of a paper read)' % head[:8],
          '  ONE PAGE`S NEXT EDITION: the edition after %s' % ONE_PAGE,
          '  THE EPSTEIN DOCUMENT`S NEXT EDITION: the edition after %s' % EPSTEIN,
          '  THE SIX PAPERS OF W-ORD-SIGN-SECTORS, each at its next edition, named by its entry at OPEN_TRAILS.md :%d (sha256 %s, not quoted):'
          % (at[0], sha(line)[:16])]
    for s, p, n in res:
        P.append('    %s: %s (%d other tracked file%s bearing the name, not read)' % (s, p, n, '' if n == 1 else 's'))
    papers6 = ['One Page`s next edition'] + [s for s, _p, _n in res]
    P += ['', '## (6) BUILD ONE: THE FIVE STATEMENTS, LANDED AT SIDE-explicit-formula %s = %s, RUN %s (each new name within the standard three at '
          'run %s and at the landing run); EACH AN INPUT OF: %s' % (form.get('tag'), (form.get('peel') or '')[:8], form.get('run'), RUN_FORM, ', '.join(papers6))]
    for k, full, cited, ok in s6:
        P.append('  (%s) %s: %d declaration%s, the sentence citing %s: %s' % (k, 'LISTED' if ok else 'NOT LISTED', len(full), '' if len(full) == 1 else 's',
                                                                           ', '.join(cited), ', '.join(full)))
    P += ['', '## THE STATEMENT FILE OF W-ORD-STATEMENT-FILE, WITH (6) BY THE AUTHOR`S WORD OF 22:18:13Z (SIDEExplicitFormula/OnePageStatement.lean at %s = %s, '
          'run %s): AN INPUT OF ONE PAGE`S NEXT EDITION' % (form.get('tag'), (form.get('peel') or '')[:8], sf[2]),
          '  %s: %d declarations: %s' % ('LISTED' if sf[1] else 'NOT LISTED', len(sf[0]), ', '.join(sf[0]))]
    P += ['', '## (7) THE CENTRE: THE STATEMENT OF THE CONTROL`S FAILURE, DEFINITIONS OF A PROP WITH NO PROOF (push-b763-arith at %s, run %s): '
          'AN INPUT OF THE EPSTEIN DOCUMENT`S NEXT EDITION' % ((ar[3] or '')[:8], ar[2]),
          '  %s: %d declarations: %s' % ('LISTED' if ar[1] else 'NOT LISTED', len(ar[0]), ', '.join(ar[0]))]
    P += ['', '## NOT LISTED: the six names of [P1] (%s), declared before this act and printed at v0.42 by (6)`s clause; the orders of (8), '
          'which (10) names not' % ', '.join(O.P1)]
    n6 = sum(len(full) for _k, full, _c, ok in s6 if ok)
    k6 = sum(1 for *_x, ok in s6 if ok)
    P += ['', '### ### **THE RECUT INPUTS: (6) %d DECLARATIONS OF %d STATEMENTS FOR %d PAPERS ; THE STATEMENT FILE %d FOR 1 PAPER ; (7) %d FOR 1 PAPER ; '
          'CONTROLS %d OF %d.**' % (n6, k6, len(papers6), len(sf[0]) if sf[1] else 0, len(ar[0]) if ar[1] else 0, n_ok, len(ctl))]
    return P, n_ok == len(ctl)


def main(argv):
    mode = (argv + [''])[0]
    if mode not in ('controls', 'bank'):
        die('usage: controls | bank')
    P, ok = compose()
    if mode == 'controls':
        print(NL.join(P[:P.index('## THE CONTROLS') + 9]))
        return 0
    print(NL.join(P))
    if not ok:
        die('A CONTROL NOT AS WANTED')
    text = NL.join(P) + NL
    with open(BANK + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print('written data/b763_recut_inputs.txt (%d lines, sha256 %s)' % (len(P), sha(text)[:16]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
