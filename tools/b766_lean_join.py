# -*- coding: utf-8 -*-
"""tools/b766_lean_join.py -- b766, (R376)(5)(b): THE LEAN JOINED TO THE PAPERS. A reading and no build: no line of REGISTRY, of the
census or of a paper is written.

Carried from tools/b756_constellation.py, its readers imported as committed: the roster's current editions and the table sections of each
(population(): tools/standing/roster.py json, every Correspondence heading to the next heading of its level, b586's four start lines located
today), the table row (is_row) and the names a row gives (terminal_names, b589's form over rowgen's LEAN_NAME). Written by the Write tool at
b766's Component 3 and committed before its first run, dry included (N2).

  dry      the join, the controls and the figures printed; nothing written
  write    the same; where every control reads AS WANTED, data/b766_lean_join.txt and .json

THE DECLARATIONS: the rows of data/terminal_table.json as committed at the relay's HEAD (git show, never the working file), one a (kernel,
name) pair, with its statement file. THE PAPERS' TABLES: each roster edition carrying a correspondence table (a table row naming a terminal),
the two generated pages set apart, and the names of each of its table rows. THE GENERATED PAGES: THE_CLAUSE_AND_ITS_COMPILED_FACES.md and
THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md (tools/chain_page.py :60, :68), each read whole at PLACE-papers HEAD, every backticked name of
b589's form on any line. A NAME NAMES A DECLARATION where it equals the declaration's full name or a dot-suffix of it; a name naming
declarations of more than one kernel names each, and such names are counted and printed. THE FOUR COUNTS, by kernel and in all: the
declarations; NAMED BY A PAPER'S TABLE; ON A GENERATED PAGE ALONE (named on a page and by no paper's table); BY NEITHER, listed by statement
file. THE NAVIGATOR'S CANDIDATE, a workspace count printed as the navigator's: 1,990 declarations, 152, 870 and 968, with the tables as b756
read them and the terminal table at the relay's 29d4c9b7; the seat's figures govern, and the join is printed again with the terminal table
at 29d4c9b7 beside them, the papers read at PLACE-papers HEAD in both.
CONTROLS ((R376)(5)(b)): a planted declaration named in a planted row moves the paper count by one and the total by one and no other count;
the same declaration with no row moves the neither count by one and no other. Beside them: the population's files equal in the working tree
to their bytes at PLACE-papers HEAD (git diff --quiet HEAD); the identifiers and the protected word 0 in the bank.

No PLACE-papers line is printed: the bank carries declaration names, kernel names, statement files and document keys; no git write.
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b756_constellation as B56   # noqa: E402  ### b756's readers as committed
import b761_registry as R61        # noqa: E402  ### the identifiers and the protected word, as committed

ACT, NL = 'b766', '\n'
PP = B56.PP
BANK = os.path.join(D, 'b766_lean_join.txt')
BJSON = os.path.join(D, 'b766_lean_join.json')
PAGES = ('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md')
NAV = (1990, 152, 870, 968)   # ### (R376)(5)(b): the navigator's candidate, printed as the navigator's
NAV_REV = '29d4c9b7'
PLANT_DECL = dict(repo='SIDE-planted', name='SIDEPlanted.zz_b766_planted_decl', statement_file='SIDEPlanted/Planted.lean')
PLANT_ROW = '| planted | `zz_b766_planted_decl` | SIDE-planted |'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout


def table_at(rev):
    rc, b = git(RELAY, 'show', '%s:data/terminal_table.json' % rev)
    if rc or not b:
        die('THE TERMINAL TABLE NOT READ AT %s' % rev)
    J = json.loads(b.decode('utf-8'))
    out, seen = [], set()
    for x in J['rows']:
        k = (x['repo'], x['name'])
        if k in seen:
            continue
        seen.add(k)
        sf = x.get('statement_file')
        out.append(dict(repo=x['repo'], name=x['name'], statement_file=sf if sf and sf != 'None' else '(no statement file)'))
    return out, len(J['rows']), hashlib.sha256(b).hexdigest()[:16]


def papers():
    full = B56.population()
    pop = [d for d in full if d['rows'] and d['path'].split('/')[-1] not in PAGES]
    in_pop = [p for p in PAGES if any(d['path'].split('/')[-1] == p and d['rows'] for d in full)]
    rc = subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--'] + [d['path'] for d in pop]).returncode
    out = []
    for d in pop:
        lines = io.open(os.path.join(PP, *d['path'].split('/')), encoding='utf-8', errors='replace').read().replace('\r', '').split(NL)
        names, seen = set(), set()
        for a, b in d['secs']:
            for i in range(a, b + 1):
                if i in seen or i - 1 >= len(lines):
                    continue
                seen.add(i)
                if B56.is_row(lines[i - 1]):
                    names.update(B56.terminal_names(lines[i - 1]))
        out.append(dict(key=d['key'], path=d['path'], names=sorted(names), rows=d['rows']))
    return out, rc, len(full), in_pop


def pages():
    out = []
    for p in PAGES:
        rc, b = git(PP, 'show', 'HEAD:' + p)
        if rc or not b:
            die('THE GENERATED PAGE %s NOT READ AT HEAD' % p)
        txt = b.decode('utf-8', 'replace').replace('\r', '')
        names = set()
        for l in txt.split(NL):
            names.update(B56.terminal_names(l))
        out.append(dict(page=p, names=sorted(names), lines=txt.count(NL)))
    return out


def join(decls, paper_names, page_names):
    ix = {}
    for i, d in enumerate(decls):
        parts = d['name'].split('.')
        for j in range(len(parts)):
            ix.setdefault('.'.join(parts[j:]), set()).add(i)

    def hit(names):
        got, amb = set(), []
        for n in names:
            s = ix.get(n, set())
            if len(set(decls[i]['repo'] for i in s)) > 1:
                amb.append(n)
            got |= s
        return got, amb
    P, ap = hit(paper_names)
    G, ag = hit(page_names)
    alone = G - P
    neither = set(range(len(decls))) - P - G
    return dict(P=P, G=G, alone=alone, neither=neither, amb_paper=sorted(ap), amb_page=sorted(ag))


def four(decls, j):
    return (len(decls), len(j['P']), len(j['alone']), len(j['neither']))


def by_kernel(decls, j):
    k = {}
    for i, d in enumerate(decls):
        r = k.setdefault(d['repo'], [0, 0, 0, 0])
        r[0] += 1
        r[1] += i in j['P']
        r[2] += i in j['alone']
        r[3] += i in j['neither']
    return k


def run(mode):
    head = git(RELAY, 'rev-parse', '--short=8', 'HEAD')[1].decode().strip()
    pph = git(PP, 'rev-parse', '--short=8', 'HEAD')[1].decode().strip()
    decls, nrows, tsha = table_at('HEAD')
    ndecls, nnrows, ntsha = table_at(NAV_REV)
    pap, wt_rc, npop, in_pop = papers()
    pg = pages()
    paper_names = sorted(set(n for d in pap for n in d['names']))
    page_names = sorted(set(n for d in pg for n in d['names']))
    J = join(decls, paper_names, page_names)
    F = four(decls, J)
    JN = join(ndecls, paper_names, page_names)
    FN = four(ndecls, JN)
    K = by_kernel(decls, J)
    top = sorted(K.items(), key=lambda kv: (-kv[1][3], kv[0]))[:3]
    # ### THE CONTROLS
    J2 = join(decls + [PLANT_DECL], sorted(set(paper_names) | set(B56.terminal_names(PLANT_ROW))), page_names)
    F2 = four(decls + [PLANT_DECL], J2)
    J3 = join(decls + [PLANT_DECL], paper_names, page_names)
    F3 = four(decls + [PLANT_DECL], J3)
    L = R61.at_head().split(NL)[:-1]
    qw = R61.qword(L)
    I = R61.ids()
    same = 'REPRODUCED' if FN == NAV else 'DIFFERING AS PRINTED'
    P = ['%s -- (R376)(5)(b): THE LEAN JOINED TO THE PAPERS (%s)' % (ACT, utc()), '',
         '### tools/b766_lean_join.py %s; the relay HEAD %s, data/terminal_table.json there %d rows (sha256 %s), %d (kernel, name) pairs; '
         'PLACE-papers HEAD %s; a reading: no line of a paper written or printed.' % (mode, head, nrows, tsha, len(decls), pph), '',
         '## THE POPULATION: the roster`s current editions with a table section %d (tools/standing/roster.py json, b756`s population()); '
         'carrying a correspondence table, the two generated pages set apart, %d; the generated pages among those carrying one: %s; names read '
         'from their table rows %d distinct' % (npop, len(pap), ', '.join(in_pop) or 'none', len(paper_names)),
         '## THE GENERATED PAGES (tools/chain_page.py), each whole at HEAD: %s' % ' ; '.join(
             '%s %d lines, %d names' % (x['page'], x['lines'], len(x['names'])) for x in pg) + ' ; %d distinct' % len(page_names), '',
         '## THE FOUR COUNTS IN ALL: DECLARATIONS %d ; NAMED BY A PAPER`S TABLE %d ; ON A GENERATED PAGE ALONE %d ; BY NEITHER %d' % F,
         '  names naming declarations of more than one kernel, each counted for each: by the papers %d (%s) ; by the pages %d (%s)' % (
             len(J['amb_paper']), ', '.join(J['amb_paper'][:30]) or '-', len(J['amb_page']), ', '.join(J['amb_page'][:30]) or '-'),
         '## WITH THE TERMINAL TABLE AT THE RELAY`S %s, WHERE THE NAVIGATOR READ IT (%d rows, sha256 %s, %d pairs), THE PAPERS AT HEAD: '
         'DECLARATIONS %d ; PAPER %d ; PAGE ALONE %d ; NEITHER %d' % ((NAV_REV, nnrows, ntsha, len(ndecls)) + FN),
         '## THE NAVIGATOR`S CANDIDATE, a workspace count printed as the navigator`s (the tables as b756 read them, the terminal table at %s): '
         'DECLARATIONS %d ; PAPER %d ; PAGE ALONE %d ; NEITHER %d -- %s (at %s beside it: %s)' % (
             (NAV_REV,) + NAV + (same, NAV_REV, ', '.join('%d for %d' % (a, b) for a, b in zip(FN, NAV)))), '',
         '## BY KERNEL: declarations | named by a paper`s table | on a generated page alone | by neither']
    for repo, r in sorted(K.items(), key=lambda kv: (-kv[1][0], kv[0])):
        P.append('  %-34s %5d | %5d | %5d | %5d' % (repo, r[0], r[1], r[2], r[3]))
    P += ['', '## THE PAPERS` TABLES: document | names read | declarations they name']
    for d in pap:
        jj = join(decls, d['names'], [])
        P.append('  %-60s %4d | %4d' % (d['key'][:60], len(d['names']), len(jj['P'])))
    P += ['', '## BY NEITHER, LISTED BY FILE (kernel | statement file | count: the names, each its last component)']
    byf = {}
    for i in sorted(J['neither']):
        d = decls[i]
        byf.setdefault((d['repo'], d['statement_file']), []).append(d['name'].split('.')[-1])
    for (repo, sf), ns in sorted(byf.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        P.append('  %s | %s | %d: %s' % (repo, sf, len(ns), ', '.join(ns)))
    ctl = [('a planted declaration named in a planted row: %s -> %s, the paper count and the total each by one, no other' % (F, F2),
            F2 == (F[0] + 1, F[1] + 1, F[2], F[3])),
           ('the same declaration with no row: %s -> %s, the neither count and the total each by one, no other' % (F, F3),
            F3 == (F[0] + 1, F[1], F[2], F[3] + 1)),
           ('the population`s %d files equal in the working tree to PLACE-papers HEAD (git diff --quiet HEAD exit %d)' % (len(pap), wt_rc),
            wt_rc == 0),
           ('the four counts sum: paper + page alone + neither = declarations (%d + %d + %d = %d)' % (F[1], F[2], F[3], F[0]),
            F[1] + F[2] + F[3] == F[0])]
    text = NL.join(P)
    bad = R61.idcount(text, I) + (1 if qw.lower() in text.lower() else 0) + sum(text.count(x) for x in ('Users\\', 'Users/'))
    ctl.append(('the identifiers, the protected word and a profile path 0 in the bank (%d)' % bad, bad == 0))
    ok = all(o for _w, o in ctl)
    P += ['', '## THE CONTROLS'] + ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    sentence = ('of %d declarations in the terminal table, %d are named by a paper`s Correspondence table, %d on a generated page alone and %d '
                'by neither (relay data/b766_lean_join.txt), the kernels holding the most of the last: %s; the navigator`s candidate 152, 870 and '
                '968 of 1,990 %s') % (F + (', '.join('%s %d' % (k, r[3]) for k, r in top), 'reproduced' if same == 'REPRODUCED' else 'differing as printed'))
    P += ['', '## [X2]`S FIELDS: %s' % sentence, '',
          '### ### **THE LEAN JOINED TO THE PAPERS: DECLARATIONS %d ; PAPER %d ; PAGE ALONE %d ; NEITHER %d ; THE CANDIDATE %s ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (F + (same, sum(1 for _w, o in ctl if o), len(ctl),
                                      ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD, NOTHING WRITTEN'))]
    final = NL.join(P) + NL
    if R61.idcount(final, I) or qw.lower() in final.lower():
        die('AN IDENTIFIER OR THE PROTECTED WORD IN THE PRINT')
    print(final, end='')
    if mode != 'write' or not ok:
        return 0 if ok else 1
    JS = dict(at=utc(), act=ACT, relay_head=head, pp_head=pph, terminal_rows=nrows, terminal_sha=tsha, decls=F[0], paper=F[1], pages_alone=F[2],
              neither=F[3], at_nav_rev=dict(rev=NAV_REV, rows=nnrows, sha=ntsha, four=list(FN)), nav=list(NAV), candidate=same,
              by_kernel={k: v for k, v in K.items()}, top=[[k, r[3]] for k, r in top], ambiguous_paper=J['amb_paper'], ambiguous_page=J['amb_page'],
              papers=[dict(key=d['key'], names=len(d['names'])) for d in pap], sentence=sentence, controls=[[w, o] for w, o in ctl])
    put(BANK, final)
    put(BJSON, json.dumps(JS, ensure_ascii=False, indent=1) + NL)
    print('written data/b766_lean_join.txt (%d lines) and .json' % len(final.split(NL)))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] not in (['dry'], ['write']):
        sys.exit(__doc__)
    sys.exit(run(a[0]))
