# -*- coding: utf-8 -*-
"""b710_reading5.py -- (R320)(5), READING 5, THE READING ACT'S OWN PASS: the routes that read the corpus, the kernels and the banks for the four
sections of data/b710_reading5.txt, each route banking its own print as data/b710_r5_<route>.txt (.json); the reading bank itself is the
seat's, by the Write tool, each figure copied from the verdict or the row of the route bank it names (b700's form for reading 4).

### Routes (each one foreground process, each writing only its own banks):
###   `search`     -- (5)(i): the four principles and the seven measures named in the corpus: PLACE-papers *.md at HEAD outside archive/, outputs/
###                   and the two ledgers by `git grep` (paths and line numbers; the lines then read by the Read tool), and every D:/SIDE-* kernel's
###                   *.lean at its HEAD by `git grep` bounded to its tree (the declarations named); data/b710_r5_search.txt (.json).
###   `terminals`  -- (5)(i): each named terminal's statement read at its pin by tools/terminal_table.py `statement`, its grade by the E0 rule
###                   (`rule_reading`) and the terminal table's row beside it; data/b710_r5_terminals.txt (.json).
###   `controls`   -- (5)(i): relay data/ banks named for a control object (Q0, Davenport-Heilbronn, the Epstein forms, the zeta controls) by
###                   file name and verdict line; data/b710_r5_controls.txt (.json).
###   `moves`      -- (5)(ii): the six moves (THE_BRIGHTENING_MOVES :9-:14) and the six axes (INSTRUMENTS :131-:138), each searched in the two
###                   ledgers by its own words and the acts' banks, the ledger lines printed; data/b710_r5_moves.txt (.json).
###   `flip`       -- (5)(iii): the defects banks b700-b709 by class (b700's classes), and each act's readfirst diff (HAND ONLY ... OF WHICH IN
###                   THE CLOSURE ; TEXT ONLY); data/b710_r5_flip.txt (.json).
###   `cost`       -- (5)(iv): the read banks b705-b709 by file, the files read whole, the reads of carried tools; data/b710_r5_cost.txt (.json).
### No paper, kernel or ledger is written by any route. Written by the Write tool at b710.
"""
import collections
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def rd(p):
    return open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def put(name, lines, obj):
    for n, data in (('b710_r5_%s.txt' % name, NL.join(lines) + NL), ('b710_r5_%s.json' % name, json.dumps(obj, indent=1, ensure_ascii=False) + NL)):
        p = os.path.join(D, n)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)


def kernels():
    return sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))


def pp_grep(pattern, *more):
    """[(path, line, text)] of PLACE-papers *.md at HEAD, outside archive/, outputs/ and the two ledgers; `pattern` an extended regex."""
    out = g(PP, 'grep', '-n', '-I', '-E', '-e', pattern, 'HEAD', '--', '*.md', ':!archive/*', ':!outputs/*', ':!FINDINGS.md', ':!OPEN_TRAILS.md', *more)
    rows = []
    for l in out.split(NL):
        m = re.match(r'^HEAD:([^:]+):(\d+):(.*)$', l)
        if m:
            rows.append((m.group(1), int(m.group(2)), m.group(3)))
    return rows


def k_grep(kernel, pattern):
    """[(file, line, text)] of a kernel's *.lean at HEAD (git grep bounded to the kernel's tracked tree; .lake is never read)."""
    out = g('D:/' + kernel, 'grep', '-n', '-I', '-E', '-e', pattern, 'HEAD', '--', '*.lean')
    rows = []
    for l in out.split(NL):
        m = re.match(r'^HEAD:([^:]+):(\d+):(.*)$', l)
        if m:
            rows.append((m.group(1), int(m.group(2)), m.group(3)))
    return rows


# ### (5)(i): what each principle and measure is searched by -- the corpus's own names for them (ENUMERA :213-:216, E_DIFFICULTY_THEOREM :45,
# ### TECHNE_TOOLKIT :208-:221), each a pattern over the papers' lines.
PRINCIPLES = collections.OrderedDict([
    ('Symmetry', r'\*\*S\*\* \(Symmetry\)|Independence, Determination, Symmetry|Symmetry, Independence, Determination|\bSymmetry (constrains|axiom|principle)'),
    ('Independence', r'\*\*I\*\* \(Independence\)|Independence axiom|Independence, Determination|\bIndependence (factors|principle|of the mechanism)'),
    ('Determination', r'\*\*D\*\* \(Determination\)|Determination, Symmetry|Determination[–-]Exhaustiveness|\bDetermination (guarantees|principle|axiom)'),
    ('Exhaustiveness', r'\*\*E\*\* \(Enumeration\)|Exhaustiveness|exhaustive (mechanism|enumeration)|Exhaustive Enumeration'),
])
MEASURES = collections.OrderedDict([
    ('kappa', r'Conservation strength|conservation strength'),
    ('mu', r'Formation measure|formation measure'),
    ('dmu', r'Formation distance|formation distance|Δμ'),
    ('UDT', r'Universal Darkness'),
    ('DE', r'D ?↔ ?E|D<->E|Determination[–-]Exhaustiveness'),
    ('Ostrowski', r'[Dd]omain[ -]Ostrowski|DomainOstrowski'),
    ('EDiff', r'E-Difficulty'),
])
KTERMS = collections.OrderedDict([
    ('Symmetry', r'^(theorem|lemma|def|structure|class|abbrev) +[A-Za-z_.₀-₉]*([Ss]ymmetr|functional_equation|completed[A-Za-z]*_one_sub)'),
    ('Independence', r'^(theorem|lemma|def|structure|class|abbrev) +[A-Za-z_.₀-₉]*([Ii]ndependen|euler_?[Pp]roduct|eulerProduct|crt|[Cc]oprime_filter)'),
    ('Determination', r'^(theorem|lemma|def|structure|class|abbrev) +[A-Za-z_.₀-₉]*([Dd]etermin|DeterminedSystem)'),
    ('Exhaustiveness', r'^(theorem|lemma|def|structure|class|abbrev) +[A-Za-z_.₀-₉]*([Ee]xhaust|[Oo]strowski|[Ee]numerat|e_difficulty)'),
    ('measures', r'^(theorem|lemma|def|structure|class|abbrev) +[A-Za-z_.₀-₉]*([Kk]appa|conservation|formation_(measure|distance)|[Dd]arkness|universal_?[Dd]ark|silence)'),
])


def search(*a):
    L = ['b710 -- (R320)(5)(i): THE FOUR PRINCIPLES AND THE SEVEN MEASURES NAMED IN THE CORPUS AND THE KERNELS, BY `git grep` AT HEAD (%s)' % utc(), '',
         '### the papers: PLACE-papers *.md at HEAD %s outside archive/, outputs/, FINDINGS.md and OPEN_TRAILS.md; rows are hits: path :line | the' % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
         '### line`s first 140 characters. The kernels: every D:/SIDE-* kernel`s *.lean at its HEAD (git grep bounded to the tracked tree); rows are',
         '### declarations: kernel | file :line | the declaration`s first 140 characters. The lines cited by reading 5 are read again by the Read tool.']
    J = dict(at=utc(), principles={}, measures={}, kernels={})
    for name, pat in list(PRINCIPLES.items()) + list(MEASURES.items()):
        rows = pp_grep(pat)
        by = collections.Counter(p for p, _n, _t in rows)
        key = 'principles' if name in PRINCIPLES else 'measures'
        J[key][name] = [dict(path=p, line=n, text=t[:300]) for p, n, t in rows]
        L += ['', '### %s %s -- the pattern %r -- hits %d in %d files:' % ('THE PRINCIPLE' if key == 'principles' else 'THE MEASURE', name, pat, len(rows), len(by))]
        for p, n, t in rows[:60]:
            L.append('  %s :%d | %s' % (p, n, ' '.join(t.split())[:140]))
        if len(rows) > 60:
            L.append('  ... %d further hits, by file: %s' % (len(rows) - 60, '; '.join('%s %d' % kv for kv in by.most_common(12))))
    ks = kernels()
    for name, pat in KTERMS.items():
        L += ['', '### THE KERNELS, %s -- the pattern %r:' % (name, pat)]
        hits = []
        for k in ks:
            for f, n, t in k_grep(k, pat):
                hits.append(dict(kernel=k, file=f, line=n, text=t[:300]))
        J['kernels'][name] = hits
        L += ['  %-34s %s :%d | %s' % (h['kernel'], h['file'], h['line'], ' '.join(h['text'].split())[:140]) for h in hits[:80]]
        if len(hits) > 80:
            L.append('  ... %d further declarations, by kernel: %s' % (len(hits) - 80, '; '.join('%s %d' % kv for kv in collections.Counter(h['kernel'] for h in hits).most_common(12))))
        L.append('  declarations %d in %d kernels' % (len(hits), len(set(h['kernel'] for h in hits))))
    L += ['', '### ### **PRINCIPLES 4 ; MEASURES 7 ; THE PAPERS` HITS %s ; THE KERNELS READ %d ; DECLARATIONS %s.**' % (
        ', '.join('%s %d' % (k, len(v)) for k, v in list(J['principles'].items()) + list(J['measures'].items())), len(ks),
        ', '.join('%s %d' % (k, len(v)) for k, v in J['kernels'].items()))]
    put('search', L, J)
    print(NL.join(L[-1:]))


# ### (5)(i): the terminals read for each principle and measure -- kernel, file, line (from data/b710_r5_search.txt), its reading's role.
TERMS = (
    ('Symmetry', 'SIDE-meta', 'SIDEMeta/Meta/SIDESystem.lean', 74, 'the predicate S'),
    ('Symmetry', 'SIDE-meta', 'SIDEMeta/Meta/SIDESystem.lean', 142, 'the parametric conservation theorem, S its whole content'),
    ('Symmetry', 'SIDE-kernel', 'Kernel/Layer1.lean', 8, 'the certificate`s symmetry field'),
    ('Symmetry', 'SIDE-kernel', 'Kernel/Focus.lean', 34, 'the functional equation at the kernel'),
    ('Independence', 'SIDE-meta', 'SIDEMeta/Meta/SIDESystem.lean', 56, 'the predicate I'),
    ('Independence', 'SIDE-kernel', 'Kernel/Layer1.lean', 17, 'the certificate`s independence field'),
    ('Determination', 'SIDE-meta', 'SIDEMeta/Meta/SIDESystem.lean', 65, 'the predicate D'),
    ('Determination', 'SIDE-kernel', 'Kernel/TypeLevel.lean', 15, 'determination collapse'),
    ('Determination', 'SIDE-kernel', 'Kernel/Cascade/SieveCeiling.lean', 69, 'the determined system`s slot'),
    ('Exhaustiveness', 'SIDE-meta', 'SIDEMeta/Meta/SIDESystem.lean', 85, 'the predicate E'),
    ('Exhaustiveness', 'SIDE-kernel', 'Kernel/Layer1.lean', 30, 'the SIDE exclusion syllogism'),
    ('Exhaustiveness', 'SIDE-kernel', 'Bridge/TheBridgeComplete.lean', 249, 'the structural exhaustiveness the monograph cites'),
    ('kappa', 'SIDE-meta', 'SIDEMeta/Meta/Kappa.lean', 61, 'kappa as a predicate'),
    ('kappa', 'SIDE-kernel', 'Kernel/Cascade/SieveCeiling.lean', 48, 'kappa three-valued'),
    ('UDT', 'SIDE-formation-procedure', 'SIDEFormationProcedure/Basic.lean', 136, 'the interface count zero, a Bool'),
    ('UDT', 'SIDE-kernel', 'Kernel/SilenceTheorem.lean', 74, 'the silence theorem'),
    ('Ostrowski', 'SIDE-kernel', 'Kernel/Cascade/SieveCeiling.lean', 279, 'the domain Ostrowski'),
    ('EDiff', 'SIDE-kernel', 'Kernel/Cascade/SieveCeiling.lean', 298, 'the E-Difficulty equivalence (skeleton)'),
    ('EDiff', 'SIDE-kernel', 'MetaKernel.lean', 187, 'the E-Difficulty conjecture as a type'),
    ('Ostrowski', 'SIDE-kernel', 'Bridge/OstrowskiBridge.lean', 94, 'Ostrowski`s classification, exhaustive'),
)


def _qualified(text, line):
    """the declaration at `line` (1-based) of a file's text: (keyword, qualified name), the namespaces open at that line read by
    `namespace X` / `end X` above it."""
    L = text.split(NL)
    stack = []
    for l in L[:line - 1]:
        m = re.match(r'^namespace\s+(\S+)', l)
        if m:
            stack.append(m.group(1))
            continue
        m = re.match(r'^end\s+(\S+)\s*$', l)
        if m and stack and stack[-1] == m.group(1):
            stack.pop()
    m = re.match(r'^(theorem|lemma|def|structure|class|abbrev|inductive)\s+([^\s(:{\[]+)', L[line - 1])
    if not m:
        return None, None
    return m.group(1), '.'.join(stack + [m.group(2)])


def _table_rows(J, short):
    out = []

    def walk(x):
        if isinstance(x, dict):
            nm = x.get('name') or x.get('terminal') or ''
            if isinstance(nm, str) and (nm == short or nm.endswith('.' + short)):
                out.append(x)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(J)
    return out


def terminals(*a):
    import terminal_table as TT
    J = json.load(open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    L = ['b710 -- (R320)(5)(i): THE TERMINALS OF THE FOUR PRINCIPLES AND THE MEASURES, EACH READ AT ITS KERNEL`S HEAD AND TAG, ITS GRADE FROM THE STATEMENT (%s)' % utc(), '',
         '### rows are terminals: the principle or measure | kernel | the tag at HEAD (or the latest tag and whether the file is unchanged since it) |',
         '### file :line | the keyword and the qualified name | the grade by the shared E0 rule on the statement (tools/terminal_table.py rule_reading:',
         '### a theorem by its header, a definition DEF) | the terminal table`s rows for the name (relay data/terminal_table.json) | the statement.', '']
    rows = []
    for princ, k, f, ln, role in TERMS:
        repo = 'D:/' + k
        text = g(repo, 'show', 'HEAD:' + f)
        kw, qn = _qualified(text, ln)
        tags = [t for t in g(repo, 'tag', '--points-at', 'HEAD').split() if t]
        last = g(repo, 'describe', '--tags', '--abbrev=0', 'HEAD').strip()
        same = bool(last) and g(repo, 'rev-parse', '%s:%s' % (last, f)).strip() == g(repo, 'rev-parse', 'HEAD:' + f).strip()
        st = TT.statement(repo, 'HEAD', qn) if qn else None
        try:
            kind, grade = TT.rule_reading((st or {}).get('text', ''), qn) if st else (None, None)
        except Exception as e:   # ### the E0 rule refuses a binder its lexicon does not list: the refusal is the reading, no grade minted
            kind, grade = 'theorem', 'UNCLASSED BY THE E0 RULE (%s)' % ' '.join(str(e).split())[:120]
        tr = _table_rows(J, qn.split('.')[-1]) if qn else []
        trg = sorted(set('%s %s' % (r.get('repo') or r.get('kernel') or '', r.get('grade') or r.get('cell') or '') for r in tr))[:4]
        r = dict(principle=princ, kernel=k, file=f, line=ln, role=role, keyword=kw, name=qn, tags_at_head=tags, last_tag=last, unchanged_since_last=same,
                 statement=(st or {}).get('text'), kind=kind, grade=grade, table=trg)
        rows.append(r)
        L.append('  %-14s | %-24s | %s | %s :%d | %s %s | grade %s | table %s' % (
            princ, k, ('tag ' + ','.join(tags)) if tags else ('latest %s, file unchanged %s' % (last or 'NONE', same)), f, ln, kw, qn, grade, trg or 'NO ROW'))
        L.append('      %s' % ' '.join(((st or {}).get('text') or '### NOT READ').split())[:400])
    L += ['', '### ### **TERMINALS READ %d ; STATEMENTS READ %d ; GRADES %s ; TABLE ROWS FOR %d.**' % (
        len(rows), sum(1 for r in rows if r['statement']), ', '.join('%s %d' % kv for kv in collections.Counter(r['grade'] or 'NONE' for r in rows).most_common()),
        sum(1 for r in rows if r['table']))]
    put('terminals', L, dict(at=utc(), rows=rows))
    print(NL.join(L[6:]))


# ### (5)(i): a control object for a principle is an object the programme computed on that violates the principle and keeps the others, its
# ### figures banked -- as Q0 (the Epstein zeta of x^2 + xy + 6y^2: a functional equation, no Euler product) is the control for the Euler
# ### product. Searched for each principle by the words a bank would use for such an object; each hit file read by name and its verdict line.
CONTROL_TERMS = collections.OrderedDict([
    ('Symmetry', (r'no functional equation', r'without (a|the) functional equation', r'functional equation (absent|fails|broken)', r'lacks? (a|the) functional equation',
                  r'asymmetric control', r'symmetry[- ]broken control')),
    ('Independence', (r'\bQ0\b', r'Davenport', r'no Euler product', r'without an Euler product', r'Epstein')),
    ('Determination', (r'free parameter', r'underdetermined', r'E_h\b', r'Lagarias', r'deformation parameter')),
    ('Exhaustiveness', (r'no domain Ostrowski', r'catalogue (cannot|can not) be (closed|completed|shown complete)', r'Continuum Hypothesis', r'open catalogue', r'no Ostrowski')),
])


def _data_grep(pat):
    out = g(ROOT, 'grep', '-l', '-I', '-i', '-E', '-e', pat, 'HEAD', '--', 'data/*.txt')
    return [l.split(':', 1)[1] for l in out.split(NL) if l.startswith('HEAD:')]


def _verdict(path):
    t = rd(os.path.join(ROOT, *path.split('/')))
    m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', t)
    return ' '.join(m[-1].split())[:200] if m else '### NO VERDICT LINE'


def controls(*a):
    L = ['b710 -- (R320)(5)(i): THE CONTROL OBJECTS FOR THE FOUR PRINCIPLES, SEARCHED IN THE RELAY BANKS AT HEAD (%s)' % utc(), '',
         '### the search: `git grep -l -i -E` over relay data/*.txt at HEAD %s for each pattern; rows are patterns: the pattern | the banks naming it' % g(ROOT, 'rev-parse', '--short', 'HEAD').strip(),
         '### (count, the first twelve). A control object is named where a bank computes on an object that violates the principle and keeps the',
         '### others; the candidates` verdict lines printed for the reading.']
    J = dict(at=utc(), principles={})
    for princ, pats in CONTROL_TERMS.items():
        L += ['', '### %s:' % princ.upper()]
        J['principles'][princ] = {}
        for pat in pats:
            fl = sorted(set(_data_grep(pat)))
            J['principles'][princ][pat] = fl
            L.append('  %-60s | banks %4d | %s' % (pat, len(fl), ', '.join(fl[:12])))
            if princ != 'Independence' and 0 < len(fl) <= 25:   # ### the lines themselves, where the hit set is small enough to read whole
                out = g(ROOT, 'grep', '-n', '-I', '-i', '-E', '-e', pat, 'HEAD', '--', *fl)
                for l in out.split(NL)[:40]:
                    m = re.match(r'^HEAD:([^:]+):(\d+):(.*)$', l)
                    if m:
                        L.append('      %s :%s | %s' % (m.group(1), m.group(2), ' '.join(m.group(3).split())[:150]))
    cand = ['data/b703_q0_band.txt', 'data/b707_onset.txt', 'data/b709_grid.txt', 'data/b709_pairs.txt', 'data/b705_detection.txt', 'data/b705_window.txt']
    L += ['', '### THE INDEPENDENCE CONTROL`S BANKS, BY THEIR VERDICT LINES:'] + ['  %s | %s' % (c, _verdict(c)) for c in cand]
    dh = k_grep('SIDE-kernel', r'^(theorem|lemma|def|structure|inductive|abbrev) +[A-Za-z_.]*([Ww]itness|[Dd]avenport|\bdh\b|DH)')
    L += ['', '### THE KERNEL`S WITNESS FILE (SIDE-kernel, the Davenport-Heilbronn witness named at Kernel/Cascade/SieveCeiling.lean :355):'] + [
        '  %s :%d | %s' % (f, n, ' '.join(t.split())[:140]) for f, n, t in dh]
    J['independence_banks'] = dict((c, _verdict(c)) for c in cand)
    J['dh_kernel'] = [dict(file=f, line=n, text=t) for f, n, t in dh]
    L += ['', '### ### **PRINCIPLES 4 ; PATTERNS %d ; THE BANKS NAMING EACH PRINCIPLE`S PATTERNS: %s.**' % (
        sum(len(v) for v in CONTROL_TERMS.values()), ' ; '.join('%s %d' % (p, len(set(sum(J['principles'][p].values(), [])))) for p in CONTROL_TERMS))]
    put('controls', L, J)
    print(NL.join(L[5:]))


# ### (5)(ii): each of the six moves (THE_BRIGHTENING_MOVES :9-:14) and the six axes (INSTRUMENTS :131-:138), with the identifiers by which the
# ### ledgers name the acts and orders that tried it (its validated instance's own words, and the words b705's ranking used at the clause).
MOVES = collections.OrderedDict([
    ('move: inversion-change', ('W-MINE-QUADRATIC', 'inversion-change', 'centered inversion')),
    ('move: cover-ascent', ('cover-ascent', 'W-SUBSTRATE', 'W-SIGN-7', 'metaplectic altitude')),
    ('move: subspace-restriction', ('subspace-restriction', 'partialPositivity_finiteRange', 'classKsum', 'W-ORD-CLASSK-WIDENING')),
    ('move: parameter-deformation', ('parameter-deformation', 'W3-1-CHILD', 'W-DENINGER', 'sign-onset radius')),
    ('move: structure-transport', ('structure-transport', 'Waldspurger', 'W-TRANSPORT')),
    ('move: region-compression', ('region-compression', 'W-UNION', 'finiteRange')),
    ('axis (a): identity-element re-centering', ('re-centering', 'notched window', 'W-ORD-WITNESS-TAIL-BALLS')),
    ('axis (b): cover', ('W-SIGN-7', 'zeroActing alone', 'metaplectic altitude')),
    ('axis (c): distinguished subspace', ('classK`', 'classKsum', 'h2_sign_sum', 'W-ORD-CLASSK-WIDENING-HELD')),
    ('axis (d): deformation parameter', ('E_h', 'W-DENINGER', 'support radius', 'sign-onset radius')),
    ('axis (e): representation coordinates', ('THE_CORNER_MAP', 'representation coordinates', 'Toeplitz')),
    ('axis (f): reading / composition order', ('THE_CHIASMUS_PATTERN', 'chiasmus', 'faces_join')),
])


LEDGERS = ('FINDINGS.md', 'OPEN_TRAILS.md', 'archive/2026-08-24-ledger-split/FINDINGS-archive-1-entries-through-2026-08-20c.md',
           'archive/2026-08-24-ledger-split/FINDINGS-archive-2-entries-2026-08-21-and-22.md',
           'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-1-seam-records-through-nineteenth.md',
           'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md')


def moves(*a):
    L = ['b710 -- (R320)(5)(ii): THE SIX MOVES AND THE SIX AXES IN THE TWO LEDGERS, BY THEIR OWN NAMES (%s)' % utc(), '',
         '### the ledgers: PLACE-papers FINDINGS.md and OPEN_TRAILS.md at HEAD %s; rows are identifiers: the move or axis | the identifier | the ledger |' % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
         '### its lines (count, the first three and the last three line numbers). The lines the table cites are read again by the Read tool.']
    J = dict(at=utc(), rows=[])
    for mv, ids in MOVES.items():
        L += ['', '### %s:' % mv]
        for ident in ids:
            for led in LEDGERS:
                out = g(PP, 'grep', '-n', '-F', '-e', ident, 'HEAD', '--', led)
                lines = [int(l.split(':')[2]) for l in out.split(NL) if l.startswith('HEAD:') and l.split(':')[2].isdigit()]
                J['rows'].append(dict(move=mv, ident=ident, ledger=led, lines=lines))
                if lines or not led.startswith('archive/'):
                    L.append('  %-30s | %-40s | lines %4d | first %s | last %s' % (ident, led.replace('archive/2026-08-24-ledger-split/', 'archive/'), len(lines), lines[:3], lines[-3:]))
    L += ['', '### ### **MOVES 6 ; AXES 6 ; IDENTIFIERS %d ; LEDGER LINES NAMING THEM %d.**' % (sum(len(v) for v in MOVES.values()), sum(len(r['lines']) for r in J['rows']))]
    put('moves', L, J)
    print(NL.join(L[-1:]))


# ### (5)(iii): b700's classes (relay data/b700_r4_defects.txt :10-:45), each read here by the words its rows carry, first match in this order;
# ### a row no class's words reach prints UNCLASSED for the hand.
CLASSES = (
    ('A FOREGROUND RUN PASSED TO THE BACKGROUND OR RUN WITHOUT ITS GUARD', r'BACKGROUND|PROCESS POOL|POOLS|PAST THE 600|GUARD'),
    ('A LEAN PROCESS ON THIS HOST', r'LEAN PROCESS RAN|RAN LEAN|INVOKE LEAN'),
    ('A DELETE OUT OF THE HOUSE FORM', r'DELETE|GLOB IN A BRANCH|GLOB IN THE'),
    ('sed IN ANY FORM', r'\bsed\b'),
    ('A REDIRECT OF A STREAM', r'REDIRECT'),
    ('A GIT WRITE OUT OF THE HOUSE FORM', r'GIT WRITE|PUSH(ED)? (PIPED|OUTSIDE)|AMEND|TWO GIT WRITES|A PUSH'),
    ('A FILE WRITTEN OUTSIDE THE EDIT AND WRITE TOOLS', r'\bcp\b|WRITE CALL|HEREDOC|OVERWRITTEN BY|WRITTEN BY PYTHON|OVERWROTE|A TRACKED PRIOR BANK'),
    ('A READ OUTSIDE THE READ TOOL', r'READ WHOLE|WHOLE READ|READS? OF FILES|SHELL FILTER|SHELL GREP|SHELL`S grep|INTERPRETER`S PRINT|INTERPRETER.S PRINT|PIPES? IN|A PIPE|LINES READ|OFFSET|python -c|ONE-LINE (PROGRAM|INTERPRETER)'),
    ('THE ROOT`S BANKS AND ORDER', r'ROOT-NAMED|AFTER THE ROOT|THE ROOT`S|ROOT ROUTE'),
    ('A SEALED TOOL`S DEFECT FOUND AFTER THE SEAL, LEFT AS IT STANDS', r'AFTER THE SEAL|POST-SEAL|SEALED (TOOL|ARM|NEEDLE)'),
    ('A FACE OR GATE DECLARATION WRONG', r'FACE|DECLAR|COUNTED NOUN|PREDICTION'),
    ('A MID-ACT CHECK READING SEVERAL ANSWERS OR THE WRONG SCOPE', r'MID-ACT CHECK|ANSWER CHECK'),
    ('THE NAVIGATOR`S: A CITE, PATH, NAME OR COUNT THE BANKS DO NOT CARRY', r'THE NAVIGATOR.S.*(CITE|PATH|NAME|COUNT|READ-FIRST|KIND|CARRY|FILE|BANK)'),
    ('THE NAVIGATOR`S: A PLAN, ORDER OR WORDING THAT CANNOT MEET ITS OWN TEST', r'THE NAVIGATOR.S'),
    ('A FIGURE, LINE OR CITE NOT READ FROM ITS BANK', r'NOT READ FROM|RECOUNT|FROM MEMORY|MISREAD|READ AS A|WITHOUT THE KERNEL|MISSTAT|STALE'),
    ('A STEP OUT OF ITS ORDER OR NOT TAKEN', r'ORDER|NOT RUN|BEFORE THE|LATE|NOT CARRIED|NOT TAKEN'),
    ('A TOOL`S OR ROUTE`S FIRST FORM WRONG, CAUGHT BY ITS OWN RUN BEFORE THE SEAL', r'FIRST FORM|FIRST RUN|OWN ROW|CAUGHT BY|FIRST DRY|CARRIED (TOOL|SUITE)|CARRY'),
)


_RO, _FF, _ST, _FG, _MC, _SE, _GW, _BG, _FD = ('A READ OUTSIDE THE READ TOOL', 'A TOOL`S OR ROUTE`S FIRST FORM WRONG, CAUGHT BY ITS OWN RUN BEFORE THE SEAL',
                                               'A STEP OUT OF ITS ORDER OR NOT TAKEN', 'A FIGURE, LINE OR CITE NOT READ FROM ITS BANK',
                                               'A MID-ACT CHECK READING SEVERAL ANSWERS OR THE WRONG SCOPE', 'A SEALED TOOL`S DEFECT FOUND AFTER THE SEAL, LEFT AS IT STANDS',
                                               'A GIT WRITE OUT OF THE HOUSE FORM', 'A FOREGROUND RUN PASSED TO THE BACKGROUND OR RUN WITHOUT ITS GUARD',
                                               'A FACE OR GATE DECLARATION WRONG')
# ### the seat's hand sort of the 31 rows the words do not reach, each read on its row's head (data/b710_r5_flip.txt's first print): (act, letter) -> class
HAND = {('b702', 'a'): _RO, ('b702', 'b'): _ST, ('b702', 'c'): _FG, ('b702', 'f'): _RO,
        ('b703', 'a'): _RO, ('b703', 'b'): _RO, ('b703', 'c'): _FF, ('b703', 'f'): _FF, ('b703', 'g'): _FF, ('b703', 'i'): _RO, ('b703', 'j'): _RO,
        ('b704', 'a'): _RO, ('b704', 'd'): _RO, ('b704', 'e'): _RO, ('b704', 'h'): _RO, ('b704', 'i'): _RO, ('b704', 'm'): _RO, ('b704', 'o'): _RO, ('b704', 'p'): _FF,
        ('b705', 'a'): _RO, ('b705', 'c'): _RO, ('b705', 'j'): _FF, ('b705', 'm'): _ST, ('b705', 'n'): _MC, ('b705', 'o'): _SE,
        ('b706', 'd'): _MC, ('b706', 'f'): _ST, ('b706', 'g'): _GW, ('b706', 'l'): _SE,
        ('b707', 'b'): _BG, ('b707', 'i'): _FD}
_NC, _NP = 'THE NAVIGATOR`S: A CITE, PATH, NAME OR COUNT THE BANKS DO NOT CARRY', 'THE NAVIGATOR`S: A PLAN, ORDER OR WORDING THAT CANNOT MEET ITS OWN TEST'
# ### the hand's corrections of the word sort, each read on its row's head (the second print): the word sort's class is shown beside in the bank
HAND.update({('b701', 'b'): _ST, ('b704', 'c'): _RO, ('b704', 'f'): _NC, ('b704', 'k'): _NP, ('b704', 'q'): _NP, ('b705', 'h'): _NC, ('b705', 'k'): _NC,
             ('b707', 'a'): _RO, ('b707', 'e'): _NC, ('b708', 'a'): _RO, ('b708', 'f'): _NC, ('b709', 'a'): _FG})
# ### the hand reading of the rows the path match names as caught: b701 (a) names data/b698_rules.txt as the read rule it breached, b703 (a)
# ### names data/b681_narrow.txt as the bank read outside the rule -- neither arose from the path's absence from its act's hand list.
HAND_NOT_CAUGHT = {('b701', 'a'), ('b703', 'a')}


def _defect_rows(act):
    L = rd(os.path.join(D, '%s_defects.txt' % act)).split(NL)
    out = []
    for i, l in enumerate(L):
        m = re.match(r'^    \(([a-z]{1,2})\) (.*)$', l)
        if m:
            j = i + 1
            body = [m.group(2)]
            while j < len(L) and L[j].startswith('        ') and not re.match(r'^    \([a-z]{1,2}\) ', L[j]):
                body.append(L[j].strip())
                j += 1
            out.append((m.group(1), m.group(2)[:150], ' '.join(body)))
    return out


def _diff_verdict(act):
    t = rd(os.path.join(D, '%s_readfirst_diff.txt' % act))
    m = re.search(r'THE HAND LIST (\d+) PATHS ; THE TEXT CITES (\d+) ; BOTH (\d+) ; LINES DIFFERING (\d+) \(HAND ONLY (\d+), OF WHICH IN THE CLOSURE (\d+) ; TEXT ONLY (\d+)\)', t)
    text_only = [l.split()[1] for l in t.split(NL) if l.startswith('  > ')]
    hand_out = [l.split()[1] for l in t.split(NL) if l.startswith('  < ') and 'outside the closure' in l]
    return (dict(zip(('hand', 'text', 'both', 'differing', 'hand_only', 'hand_in_closure', 'text_only'), [int(x) for x in m.groups()])) if m else {}), text_only, hand_out


def flip(*a):
    L = ['b710 -- (R320)(5)(iii): THE READFIRST FLIP -- THE DEFECTS b700-b709 BY CLASS, AND EACH ACT`S HAND LIST AGAINST THE COMPUTED CLOSURE (%s)' % utc(), '',
         '### the defects: every lettered row of relay data/b700_defects.txt .. data/b709_defects.txt, each sorted into b700`s classes (relay',
         '### data/b700_r4_defects.txt :10-:45) by the words the class`s rows carry, first match in this route`s order, an unreached row UNCLASSED for the',
         '### hand. The flip: each act`s data/bNNN_readfirst_diff.txt verdict (the hand list against tools/circuit_read.py readfirst`s closure);',
         '### a defect the closure would have caught = a lettered row naming a path its act`s diff lists as TEXT ONLY (cited by the ruling, absent from',
         '### the hand list); a defect the flip would have risked = a row naming a hand-only path OUTSIDE the closure.', '']
    J = dict(at=utc(), acts={}, classes=collections.Counter())
    tot = dict(defects=0, caught=0, risked=0)
    sums = collections.Counter()
    for n in range(700, 710):
        act = 'b%d' % n
        rows = _defect_rows(act)
        dv, text_only, hand_out = _diff_verdict(act)
        caught, risked, cls = [], [], []
        own = re.compile(r'(^|/)%s_' % act)   # ### the act's own banks and tools are its outputs, not its read-first inputs
        text_only = [p for p in text_only if not own.search(p) and not p.startswith('data/b%d_' % (n + 1))]
        hand_out = [p for p in hand_out if not own.search(p)]
        for letter, head, body in rows:
            c = HAND.get((act, letter)) or next((name for name, rx in CLASSES if re.search(rx, head) or re.search(rx, body[:400])), 'UNCLASSED')
            cls.append((letter, c, head))
            J['classes'][c] += 1
            if any(os.path.basename(p) in body for p in text_only) and (act, letter) not in HAND_NOT_CAUGHT:
                caught.append(letter)
            if any(os.path.basename(p) in body for p in hand_out):
                risked.append(letter)
        for k in dv:
            sums[k] += dv[k]
        tot['defects'] += len(rows)
        tot['caught'] += len(caught)
        tot['risked'] += len(risked)
        J['acts'][act] = dict(defects=len(rows), diff=dv, text_only=text_only, hand_outside=hand_out, caught=caught, risked=risked,
                              classes=[dict(letter=l_, cls=c, head=h) for l_, c, h in cls])
        L.append('### %s: defects %d ; the diff %s ; TEXT ONLY %s ; HAND ONLY OUTSIDE THE CLOSURE %s ; caught by the closure %s ; risked by the flip %s' % (
            act, len(rows), dv or 'NO VERDICT', text_only, hand_out, caught or 'NONE', risked or 'NONE'))
        L += ['    %s (%s) %s -- %s' % (act, l_, c, h[:110]) for l_, c, h in cls]
        sums['text_only_prior'] += len(text_only)
        sums['hand_outside_prior'] += len(hand_out)
    L += ['', '### THE DEFECTS BY CLASS, b700-b709:'] + ['  %-80s %d' % (c, k) for c, k in J['classes'].most_common()]
    L += ['', '### THE DIFFS SUMMED OVER THE TEN ACTS: %s' % dict(sums)]
    share = (sums['text_only_prior'] / float(sums['text_only_prior'] + sums['both'])) if (sums['text_only_prior'] + sums['both']) else 0.0
    L += ['### the share of the ruling`s cited prior paths the hand lists missed (TEXT ONLY, the act`s own outputs excluded, %d, over that + BOTH %d): %.3f' % (
        sums['text_only_prior'], sums['both'], share),
          '### the hand lists` paths outside the closure (what a flip to the computed list would drop): %d' % sum(len(v['hand_outside']) for v in J['acts'].values())]
    L += ['', '### ### **ACTS 10 ; DEFECTS %d ; CLASSES %d (UNCLASSED %d) ; CAUGHT BY THE CLOSURE %d ; RISKED BY THE FLIP %d ; TEXT ONLY %d OF %d CITED ; HAND ONLY OUTSIDE THE CLOSURE %d.**' % (
        tot['defects'], len(J['classes']), J['classes'].get('UNCLASSED', 0), tot['caught'], tot['risked'], sums['text_only_prior'], sums['text_only_prior'] + sums['both'],
        sums['hand_outside_prior'])]
    J['classes'] = dict(J['classes'])
    J['totals'] = dict(tot, share=share, sums=dict(sums))
    put('flip', L, J)
    print(NL.join([l for l in L if 'UNCLASSED --' in l] + [l for l in L if l.startswith('  ') and not l.startswith('    ')] + L[-4:]))


CARRIED = ('record', 'checks', 'closing', 'regspec', 'reg_gate', 'corrigendum', 'tests', 'citation', 'worklist', 'report')


def cost(*a):
    L = ['b710 -- (R320)(5)(iv): THE COST READING -- THE READ VOLUME BY FILE FROM THE READ BANKS OF b705-b709 (%s)' % utc(), '',
         '### the banks: relay data/b705_read_calls.txt .. data/b709_read_calls.txt (b704`s route: rows are Read calls -- transcript line | time | the',
         '### file`s lines read then | offset | limit | the verdict | path). A call`s volume: the lines it returned -- the file`s lines from the offset',
         '### to the limit, the whole where neither is given (the tool`s cap of two thousand lines). A whole read: neither offset nor limit. A read',
         '### the carry-by-diff rule (data/b709_rules.txt row (1), binding from b709) would have removed: a call on a carried tool of its own act or the',
         '### previous act (tools/bNNN_<record|checks|closing|regspec|reg_gate|corrigendum|tests|citation|worklist|report>.py) outside b709`s rule`s spans.', '']
    RX = re.compile(r'^\s+(\d+) \| (\S+) \| (\S+) \| offset (\S+) \| limit (\S+) \| (.*?) \| (.*)$')
    J = dict(at=utc(), acts={})
    allc, allv, whole = collections.Counter(), collections.Counter(), collections.Counter()
    tot_calls, tot_vol, carried_calls, carried_vol = 0, 0, 0, 0
    for n in range(705, 710):
        act = 'b%d' % n
        rows = []
        for l in rd(os.path.join(D, '%s_read_calls.txt' % act)).split(NL):
            m = RX.match(l)
            if m:
                lines = int(m.group(3)) if m.group(3).isdigit() else 0
                off = int(m.group(4)) if m.group(4).isdigit() else None
                lim = int(m.group(5)) if m.group(5).isdigit() else None
                vol = max(0, min(lines, (off or 1) - 1 + (lim if lim else 2000)) - ((off or 1) - 1))
                p = m.group(7).replace('\\', '/')
                short = re.sub(r'^.*?/(relay|PLACE-papers|SIDE-[^/]+|memory)/', r'\1/', p)
                rows.append(dict(path=short, lines=lines, offset=off, limit=lim, vol=vol, verdict=m.group(6)))
        prev = 'b%d' % (n - 1)
        car = [r for r in rows if re.search(r'tools/(%s|%s)_(%s)\.py$' % (act, prev, '|'.join(CARRIED)), r['path'])]
        c = collections.Counter(r['path'] for r in rows)
        v = collections.Counter()
        for r in rows:
            v[r['path']] += r['vol']
            allc[r['path']] += 1
            allv[r['path']] += r['vol']
            if r['offset'] is None and r['limit'] is None:
                whole[r['path']] += 1
        tot_calls += len(rows)
        tot_vol += sum(r['vol'] for r in rows)
        carried_calls += len(car)
        carried_vol += sum(r['vol'] for r in car)
        J['acts'][act] = dict(calls=len(rows), volume=sum(r['vol'] for r in rows), files=len(c), carried_calls=len(car), carried_volume=sum(r['vol'] for r in car),
                              top=v.most_common(5))
        L.append('### %s: calls %d ; lines returned %d ; files %d ; calls on carried tools %d (lines %d) ; the top five by lines: %s' % (
            act, len(rows), sum(r['vol'] for r in rows), len(c), len(car), sum(r['vol'] for r in car), '; '.join('%s %d' % kv for kv in v.most_common(5))))
    L += ['', '### THE FILES BY LINES RETURNED OVER THE FIVE ACTS (the top fifteen):'] + ['  %-90s calls %3d ; lines %6d' % (p, allc[p], k) for p, k in allv.most_common(15)]
    L += ['', '### THE FILES READ WHOLE MOST OFTEN (neither offset nor limit; the top fifteen):'] + ['  %-90s whole %3d' % (p, k) for p, k in whole.most_common(15)]
    L += ['', '### ### **ACTS 5 ; CALLS %d ; LINES RETURNED %d ; CALLS ON CARRIED TOOLS %d (LINES %d, %.1f%% OF THE VOLUME) -- THE READS THE CARRY-BY-DIFF RULE WOULD HAVE REMOVED ; THE TOP THREE BY LINES %s.**' % (
        tot_calls, tot_vol, carried_calls, carried_vol, 100.0 * carried_vol / tot_vol if tot_vol else 0.0, '; '.join('%s %d' % kv for kv in allv.most_common(3)))]
    J.update(calls=tot_calls, volume=tot_vol, carried_calls=carried_calls, carried_volume=carried_vol, top=allv.most_common(15), whole=whole.most_common(15))
    put('cost', L, J)
    print(NL.join(L[7:]))


if __name__ == '__main__':
    fn = {'search': search, 'terminals': terminals, 'controls': controls, 'moves': moves, 'flip': flip, 'cost': cost}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b710_reading5.py search | terminals | controls | moves | flip | cost')
        sys.exit(2)
    fn(*sys.argv[2:])
