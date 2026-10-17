# -*- coding: utf-8 -*-
"""b678_record.py -- THE ACT'S RECORD TOOL, b678 under (R288).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b678's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b677_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes);
### the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b678_record.py <route> [dry]`.
"""
import io
import json
import math
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
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b678_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    if STANDIN:
        sys.exit('### A STAND-IN RUN WRITES NO BANK -- NOTHING WRITTEN (%s)' % name)
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank. Carried from b677_record.py with b678's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b678_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b678_findings.json': dict(entry_line=99999, title='stand-in'),
        'b678_trail.json': dict(line=99999),
        'b678_act_root.json': dict(root='0' * 64, previous='cd2137c8' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b678's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b678_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE',
                         stems or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems)
    return [tuple(c) for c in cells], fired


def land(items, bank, tag, entry=None, check=(), expect_cells=(), dry=True):
    for f, ln, needle in check:
        L = rd(FIND if f == 'FINDINGS.md' else OT).split(NL)
        if needle not in L[ln - 1]:
            sys.exit('### %s :%d DOES NOT CARRY %r -- NOTHING WRITTEN' % (f, ln, needle))
    items = [(f, h, conv(t)) for f, h, t in items]
    cells, fired = screens(items, tag, dry)
    if dry:
        for f, h, t in items:
            print('----', f, NL + t)
        return
    if cells != [tuple(x) for x in expect_cells] or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    n = {'FINDINGS.md': len(rd(FIND).split(NL)), 'OPEN_TRAILS.md': len(rd(OT).split(NL))}
    want = {}
    for f, h, t in items:
        want[h] = n[f] + 1 if rd(FIND if f == 'FINDINGS.md' else OT).endswith(NL) else n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        guard_absent(FIND if f == 'FINDINGS.md' else OT, h)
    out = []
    for f, h, t in items:
        path = FIND if f == 'FINDINGS.md' else OT
        r = append_to(path, t)
        got = line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


# ================================================================================ THE READERS, ONE PER ROW SHAPE A ROUTE READS ((R263)(3))
def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


BRANCH_FATES = ('DELETED', 'KEPT')


def read_branch_row(r):
    """a row of data/b678_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


READERS = ['read_score_row', 'read_head', 'read_branch_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b678_rowgen_<stage>.txt, the stage
    `stepzero` or, by argument, `after` (the ruling's rowgen diff after the corrigendum)."""
    stage = 'after' if 'after' in a else 'stepzero'
    R = roster()
    paths = [os.path.join(PP, p) for _n, p in R]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(R) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(R), miss))
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['b678 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % ('STEP ZERO' if stage == 'stepzero' else
                                                                                     'AFTER THE CORRIGENDUM ((R288)(2))', utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b678_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R288)(4))
def branches(*a):
    """every branch (R288)(4) names, its tip read before any delete, its fate; no remote deletion is named. data/b678_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    L = ['b678 -- STEP ZERO, (R288)(4): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main --list <name>` ; fate.',
         '### Deleted by name in the house form, each delete command naming one branch with no glob in any half (its --list half naming the',
         '### same branch), one repository per call; no branch the ruling does not name is deleted; the ruling names no remote deletion.']
    L += ['  %-24s %-20s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                              r['fate']) for r in rows]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE 0) ; MERGED %d ; TO BE DELETED %d.**' % (
        len(rows), len(rows), sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b678_branches.txt', L)
    put_json('b678_branches.json', dict(at=utc(), rows=rows))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R288)(1)
WH = ('*Appended 2026-10-17 by b678 to b677’s entry (:8943), under `(R288)`(1) -- b677 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b677_closing.txt):*')
WB = (' “b677 closed: relay 7beac43e, PLACE-papers f614597; suite 85 of 85; root cd2137c837efe204…; 2 prompts answered; 9 defects” '
      '(data/b677_closing.txt :1), the closing pushed at relay da8a46bc (data/b677_closing_push_out.txt :4). The run’s readings as the banks '
      'print them: “Q0 AT qE0 at 200 bits : CONTROLS 41 ; PASS 29 (j 24-52) ; INSTRUMENT 12 ; OBJECT 0 ; NEITHER 0 ; of b671`s INSTRUMENT 23 '
      'now PASS 11 ; the first failing j 53 ; the radius at j = 64 2.051e-03” (data/b677_closing.txt :25, THE RUN); the hypotheses “H1 REFUTED '
      '; H2 REFUTED ; H3 REFUTED ; H4 NOT SCORABLE ; H5 HELD” (:30; data/b677_map_h.txt :12), H3 refuted on a failing instrument with no object '
      'reading taken (:5); the tolerance measured on the consumer, “h_tol(38) 3.162e-20 ; h_tol(64) 3.162e-28” (:28; data/b677_tolerance.txt '
      ':86-:87), the banked width 1e-24 above the second; the instrument-side hQtie row, hQtie taken from coeffs_exist and the orbit identity '
      'and not from balls, j₀ = 38 and the zero side below 0, not an object finding (data/b677_map_h.txt :9); `W-ORD-EPSTEIN-BALL-WIDTH` OPEN, '
      'its width 3.2·10⁻²⁸ re-entered from the measurement and its trigger a narrowing act at half-width 10⁻²⁸ or finer (data/b670_work_orders.txt '
      ':266; OPEN_TRAILS :14590), and `W-ORD-MAP-ANGLE-FORM` OPEN, its trigger after it (:265; :14588). Nine defects (a)–(i), (a)–(d) the '
      'navigator’s (data/b677_defects.txt :5–:44), among them the path data/b663_plan.txt for data/b663_epstein_plan.txt, the seat’s reading '
      'accepted (R288)(1); the seat’s (i), a glob in a delete command’s listing half, its repair this act’s one branch per command. The '
      'pre-run’s standing part at 557 s (data/b677_arms_prerun_standing.txt): the standing arms split into two foreground parts from this '
      'act, entered in relay data/b678_rules.txt. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b678_record_lines.json', 'c1', entry=K.B677_ENTRY,
         check=[('FINDINGS.md', K.B677_ENTRY, '## The detection map in the angle form at Q0'), ('OPEN_TRAILS.md', K.B677_TRAIL, '### b677')], dry=dry)


# ================================================================================ COMPONENT 2: THE ORDER DISCHARGED ON THE CORRIGENDUM, (R288)(2)
ORDERS = 'b670_work_orders.txt'


def _qh(ln):
    return ('*Appended 2026-10-17 by b678 beneath `W-ORD-Q0-CLASS-LINES` (:14556), under `(R288)`(2) -- THE ORDER DISCHARGED ON THE '
            'CORRIGENDUM ENTRY AT FINDINGS :%d:*' % ln)


def c2(*a):
    dry = 'dry' in a
    cj = jl('b678_corrigendum.json')
    ln = cj.get('entry_line')
    if not ln:
        sys.exit('### THE CORRIGENDUM IS NOT LANDED (data/b678_corrigendum.json) -- NOTHING WRITTEN')
    n, nc = len(cj.get('rows') or []), len(cj.get('carried') or [])
    body = (' the 36 sentences on 35 ledger lines that place Q0 in the kernel’s configuration class (relay data/b676_q0_lines.txt) are '
            'answered by one corrigendum entry at FINDINGS :%d, generated by relay tools/b678_corrigendum.py from the bank’s TO RE-CUT rows, '
            'each sentence quoted verbatim with its corrected reading in one clause citing FINDINGS :8881 and Zeta23/Defs.lean :142: %d rows '
            'written, %d carried, the row count equal to the hand count 36 (relay data/b678_corrigendum.txt). No ledger line among the 35 is '
            'rewritten or pinned in place. Status DISCHARGED. Pin: FINDINGS :%d.' % (ln, n, nc, ln))
    head = _qh(ln)
    land([('OPEN_TRAILS.md', head, NL + head + body + NL)], 'b678_record_lines_c2.json', 'c2',
         check=[('OPEN_TRAILS.md', K.Q0_ORDER_LINE, 'W-ORD-Q0-CLASS-LINES'), ('FINDINGS.md', ln, '## Q0 outside the kernel')], dry=dry)
    if dry:
        return
    ol = jl('b678_record_lines_c2.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-17 by b678 under (R288)(2) (additive, (R254)(2)): W-ORD-Q0-CLASS-LINES discharged on the corrigendum entry, '
            'its Status cell filled and the entry`s line its pin.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-Q0-CLASS-LINES', K.Q0_ORDER_LINE, 'b676', 678 - 676, 'DISCHARGED', ol,
                                                       'the corrigendum entry at FINDINGS :%d' % ln, ol)]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after): %s' % (ORDERS, len(old), len(new), rows[1].strip()[:120]))


# ================================================================================ COMPONENT 3: THE NAMING, (R288)(3) -- before any kernel write
def _kern_rows():
    """the kernels table's rows (data/b647_table_kernels.txt): rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED (its header :4)."""
    out = []
    for i, l in enumerate(rdn(K.KERNELS_BANK).split(NL), 1):
        m = re.match(r'^  (SIDE-[\w-]+)\s+([0-9a-f]{7}) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', l)
        if m:
            out.append(dict(line=i, text=l, kernel=m.group(1), pin=m.group(2), rows=int(m.group(3)), under=int(m.group(5)),
                            over=int(m.group(6)), unlic=int(m.group(7))))
    return out


def naming(*a):
    """(R288)(3) and N3: the order's line (data/b652_ferry.txt :19), the tie-break rule's row and the table rows printed verbatim from their
    banks; every kernel's standing count read from the licensed table (a kernel cut since its read stands at its cut bank's figure); the
    document named by the descending count and, at a tie, by the rule's letter (rows outside LICENSED/CITED of any kind, then the larger
    table); then the named kernel's workflow directory, print list and print bank read or declared absent -- before any kernel write.
    data/b678_naming.txt (.json)."""
    rules = rdn(K.RULES_BANK).split(NL)
    i0 = [i for i, l in enumerate(rules) if l.startswith('  (%d) ' % K.TIE_RULE_ROW)][0]
    rule = [rules[i0]] + [l for l in __import__('itertools').takewhile(lambda x: x.startswith('      '), rules[i0 + 1:])]
    order_line = rd(os.path.join(D, 'b652_ferry.txt')).split(NL)[18]
    lt = rdn(K.TABLE_BANK).split(NL)
    standing = {}
    for i, l in enumerate(lt, 1):
        m = re.match(r'^  (SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)\s+(\d+) ->\s+(\d+)', l)
        if m:
            standing[m.group(1)] = (i, int(m.group(4)), l)
    cut_since = {}
    for k, bank, needle in K.CUT_SINCE:
        m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', rdn(bank))
        if m and needle in rdn(bank):
            cut_since[k] = (int(m.group(2)), bank)
    rank = []
    for r in _kern_rows():
        ln, now, _l = standing.get(r['kernel'], (None, None, None))
        if r['kernel'] in cut_since:
            now = cut_since[r['kernel']][0]
        rank.append((now if now is not None else -1, r['under'] + r['over'] + r['unlic'], r['rows'], r['kernel'], ln, r))
    rank.sort(key=lambda x: (-x[0], x[3]))
    top = rank[0][0]
    tied = [x for x in rank if x[0] == top]
    by_rule = sorted(tied, key=lambda x: (-x[1], -x[2], x[3]))
    named = by_rule[0][3] if (len(tied) == 1 or (by_rule[0][1], by_rule[0][2]) != (by_rule[1][1], by_rule[1][2])) else None
    wf = g(K.TD, 'ls-tree', '--name-only', 'main', '.github/workflows/').split()
    pt = g(K.TD, 'ls-tree', '--name-only', 'main').split()
    pshape = r"'SIDESilencePrinciple\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)|^  SIDESilencePrinciple\.[A-Za-z0-9_.']+ +\["
    pb = sorted(set(g(ROOT, 'grep', '-lE', pshape, '--', 'data/').split()))
    ctl = sorted(set(g(ROOT, 'grep', '-lE', r"'Trivium\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)", '--', 'data/').split()))
    L = ['b678 -- COMPONENT 3, (R288)(3): THE ORDER, THE RULE ROW AND THE TABLE ROWS, VERBATIM, BEFORE THE DOCUMENT IS NAMED (%s)' % utc(), '',
         '### THE ORDER, verbatim (relay data/b652_ferry.txt :19): ' + order_line.strip(),
         '### THE RULE, verbatim with path and line (relay data/%s :%d):' % (K.RULES_BANK, i0 + 1)] + ['    ' + l for l in rule] + [
         '', '### THE TABLE ROWS, verbatim with path and line: the licensed table (relay data/%s) for each kernel of the kernels table (relay' % K.TABLE_BANK,
         '### data/%s, columns rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED, its header :4); a kernel cut since its read stands at' % K.KERNELS_BANK,
         '### its cut bank`s figure (%s); ordered by the count now standing:' % '; '.join('%s at %d, relay data/%s' % (k, v[0], v[1]) for k, v in cut_since.items())]
    for now, anyk, nrows, k, ln, r in rank:
        L.append('  %2d  %-34s licensed table :%s  "%s"' % (now, k, ln, (standing.get(k) or (0, 0, ''))[2].strip()))
        L.append('      %-34s kernels table :%d  "%s"  (outside of any kind %d ; rows %d)' % ('', r['line'], r['text'].strip(), anyk, nrows))
    L += ['', '### THE NAMING: the greatest count standing is %d, carried by %s.' % (top, ', '.join(x[3] for x in tied))]
    if len(tied) > 1:
        L.append('### A TIE: neither carries a declared suite failure (b677`s suite 85 of 85, relay data/b677_closing.txt :1); the rule of row %d by its '
                 'letter -- rows outside LICENSED/CITED of any kind: %s; %s' % (K.TIE_RULE_ROW, ', '.join('%s %d' % (x[3], x[1]) for x in tied),
                                                                                 'EQUAL, so the larger table: %s' % ', '.join('%s %d rows' % (x[3], x[2]) for x in tied)
                                                                                 if len(set(x[1] for x in tied)) == 1 else 'the greater count'))
    L += ['### NAMED: %s docstrings' % (named or '### NONE'),
          '', '### THE NAMED KERNEL`S WORKFLOW DIRECTORY, PRINT LIST AND PRINT BANK (read before any kernel write):',
          '  %s main %s (tag %s at %s): .github/workflows/ carries %s -- %s' % (
              named, g(K.TD, 'rev-parse', '--short', 'main').strip(), K.T_LAST_TAG, g(K.TD, 'rev-parse', '--short', K.T_LAST_TAG + '^{commit}').strip(),
              wf or 'NOTHING', 'a build-module.yml' if any('build-module' in f for f in wf) else 'NO build-module.yml (no dispatch input; no print step)'),
          '  print_targets.txt at its root: %s ; AxiomCheck*.lean at its root: %s' % ('print_targets.txt' in pt, [f for f in pt if f.startswith('AxiomCheck')] or 'NONE'),
          '  relay tracked banks carrying a printed axiom line of a SIDESilencePrinciple declaration (git grep -lE over data/): %s -- %s' % (
              pb or 'NONE', 'NO PRINT BANK' if not pb else 'a print bank'),
          '  the control, the same shape over SIDE-trivium`s declarations: %d bank(s), b676`s after bank among them %s' % (
              len(ctl), 'data/b676_axioms_SIDE-trivium_after.txt' in ctl),
          '  its dependency form: lakefile.toml, no require (Mathlib-free) %s ; lean-toolchain %s' % (
              'require' not in (_show(K.TD, 'main', 'lakefile.toml') or 'require'), (_show(K.TD, 'main', 'lean-toolchain') or '').strip()),
          '', '### ### **NAMED %s ; TIED %d ; WORKFLOW build-module.yml %s ; PRINT LIST %s ; PRINT BANK %s.**' % (
              named or '### NONE', len(tied), 'PRESENT' if any('build-module' in f for f in wf) else 'ABSENT',
              'PRESENT' if 'print_targets.txt' in pt else 'ABSENT', 'PRESENT' if pb else 'ABSENT')]
    put_txt('b678_naming.txt', L)
    put_json('b678_naming.json', dict(at=utc(), named=named, tied=[x[3] for x in tied], top=top, workflows=wf, print_banks=pb,
                                      rank=[[x[0], x[1], x[2], x[3], x[4]] for x in rank]))
    print(NL.join(L[-16:]))


# ================================================================================ COMPONENT 3: THE RUNS ON THE HOSTED RUNNER (b676's runner, carried)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <run id> <ref> <label>`: the named kernel's run read by its id; the artifact listed, downloaded by its id into memory, its sha256
    against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; the axioms output
    of the print step banked whole, every name of the list matched to one printed line. data/b678_runner_<kernel>_<label>.txt,
    data/b678_axioms_<kernel>_<label>.txt and a row of data/b678_runner_rows.json. Carried from b676_record.py's runner."""
    import hashlib
    import io as _io
    import zipfile
    run_id, ref, label = int(a[0]), a[1], a[2]
    repo = 'psinary-sketch/' + K.CANDIDATE
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=K.CANDIDATE, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b678 -- COMPONENT 3, (R288)(3): THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (K.CANDIDATE, label.upper(), utc()), '',
         '### the dispatch: at main (the workflow %s, the print list %s), the ref input %s ; the target `%s`' % (K.T_WORKFLOW, K.T_MAIN, ref, K.T_TARGET)]
    if label == 'before':
        L.append('### THE PRINT BANK AT MAIN: main %s is the tag %s (%s) with the workflow and print-list commits atop it (%s past %s), no .lean '
                 'byte changed' % (K.T_MAIN, K.T_LAST_TAG, K.T_PRE_MAIN, g(K.TD, 'rev-list', '--count', '%s..%s' % (K.T_LAST_TAG, K.T_MAIN)).strip(),
                                   K.T_LAST_TAG))
    L.append('### the run: id %s ; %s ; status %s ; conclusion %s ; %s to %s' % (run_id, run.get('url'), run.get('status'), run.get('conclusion'),
                                                                               run.get('createdAt'), run.get('updatedAt')))
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('size_in_bytes'), sha, digest or '### NONE GIVEN', 'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)", re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (row['build_exit'], len(row['errors']))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; refused %s' % (len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg),
                                       sum(1 for _n, d in deps if d.startswith('does not')), sum(1 for _n, d in deps if 'sorryAx' in d),
                                       T_.get('axioms_refused.txt', '').strip() or 'NONE')]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not any('sorryAx' in d for _n, d in deps)
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; GATE %s.**' % (
        run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']), len(deps),
        len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), row['gate'])]
    put_txt('b678_runner_%s_%s.txt' % (K.CANDIDATE, label), L)
    if row['artifact_sha256']:
        put_txt('b678_axioms_%s_%s.txt' % (K.CANDIDATE, label), ax.split(NL))
    j = jl('b678_runner_rows.json') if os.path.isfile(os.path.join(D, 'b678_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('label') != label] + [row]
    put_json('b678_runner_rows.json', dict(rows=rows))
    print(NL.join(L))


def prints(*a):
    """the 'before' and 'after' axioms outputs compared line for line (the merge only where they are equal at every line).
    data/b678_prints_compare.txt."""
    b, f = rdn('b678_axioms_%s_before.txt' % K.CANDIDATE), rdn('b678_axioms_%s_after.txt' % K.CANDIDATE)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b678 -- COMPONENT 3: THE PRINTS BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % utc(), '',
         '### before: relay data/b678_axioms_%s_before.txt (%s, %d lines) ; after: relay data/b678_axioms_%s_after.txt (%s, %d lines)' % (
             K.CANDIDATE, K.T_MAIN, len(bl), K.CANDIDATE, K.T_CUT, len(fl)), '### the lines that differ:'] + (['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b678_prints_compare.txt', L)
    print(L[-1])


def _strip_comments(t):
    """the Lean text with every block comment (nested /- -/, docstrings and module docs included) and every line comment removed, whitespace
    runs collapsed: what the elaborator reads."""
    out, i, depth = [], 0, 0
    while i < len(t):
        if t.startswith('/-', i):
            depth, i = depth + 1, i + 2
            continue
        if depth and t.startswith('-/', i):
            depth, i = depth - 1, i + 2
            continue
        if not depth and t.startswith('--', i):
            j = t.find(NL, i)
            i = len(t) if j < 0 else j
            continue
        if not depth:
            out.append(t[i])
        i += 1
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


CONTROL_NEEDLE = 'theorem silence_yields_protection'


def cutdiff(*a):
    """(R288)(3): the cut's diff (the print-list main to the cut tip), printed whole; the files it touches; each file's text with its comments
    stripped compared before and after (equal = no line the elaborator reads changed), with a positive control (a one-word code change in
    the after text must make the comparison unequal). data/b678_cut_diff.txt."""
    files = g(K.TD, 'diff', '--name-only', K.T_MAIN, K.T_CUT).split()
    d = g(K.TD, 'diff', '--unified=0', K.T_MAIN, K.T_CUT).replace(chr(13), '')
    rows = []
    for f in files:
        b, n = _show(K.TD, K.T_MAIN, f) or '', _show(K.TD, K.T_CUT, f) or ''
        eq = _strip_comments(b) == _strip_comments(n)
        ctl = _strip_comments(b) == _strip_comments(n.replace(CONTROL_NEEDLE, CONTROL_NEEDLE + '_', 1))
        rows.append((f, eq, ctl, CONTROL_NEEDLE in n))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b678 -- COMPONENT 3, (R288)(3): THE CUT`S DIFF, RESTRICTED TO COMMENT AND DOCSTRING LINES (%s)' % utc(), '',
         '### %s %s (main, the print list) -> %s (the cut, %s); files %s ; lines added %d, removed %d' % (
             K.CANDIDATE, K.T_MAIN, K.T_CUT, K.T_BRANCH, files, len(plus), len(minus)),
         '### rows are files: the text with every comment stripped equal before and after ; the control (a one-word code change in the after',
         '### text) unequal ; the control`s needle present:']
    L += ['  %-34s CODE EQUAL %s ; CONTROL UNEQUAL %s ; NEEDLE PRESENT %s' % (f, eq, not ctl, nd) for f, eq, ctl, nd in rows]
    L += ['', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    ok = files == list(K.T_CUT_FILES) and all(eq and not ctl and nd for _f, eq, ctl, nd in rows)
    L += ['', '### ### **FILES %d ; CODE EQUAL WITH COMMENTS STRIPPED %s ; CONTROLS UNEQUAL %s ; COMMENT AND DOCSTRING LINES ALONE %s.**' % (
        len(files), all(r[1] for r in rows), all(not r[2] for r in rows), ok)]
    put_txt('b678_cut_diff.txt', L)
    print(L[-1])


def corr(*a):
    """(R288)(3): the Correspondence generator (tools/correspondence_gen.py) run `dry full` (the local clones' tags, no remote call; it writes
    nothing), its print banked whole with the count of lines naming the cut kernel; the run mode only where the dry run changes a cell.
    data/b678_correspondence_dry.txt."""
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry', 'full'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=560)
    out = ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')
    hits = [l for l in out.split(NL) if re.search(r'(?i)silence-principle|SIDESilencePrinciple', l)]
    v = [l for l in out.split(NL) if 'CELLS CHANGED' in l][-1:] or ['### NO VERDICT LINE']
    L = ['b678 -- COMPONENT 3, (R288)(3): THE CORRESPONDENCE GENERATOR, DRY, AFTER THE TAG %s (%s)' % (K.T_NEXT_TAG, utc()), '',
         '### relay tools/correspondence_gen.py `dry full`, exit %d ; lines naming the cut kernel %d ; the generator`s verdict:' % (
             r.returncode, len(hits)), '    ' + v[0].strip(), '', '### the print, whole:'] + ['    ' + l for l in out.rstrip(NL).split(NL)]
    cc = re.search(r'CELLS CHANGED (\d+)', v[0])
    L += ['', '### ### **GENERATOR EXIT %d ; CELLS CHANGED %s ; LINES NAMING THE CUT KERNEL %d ; RUN MODE %s.**' % (
        r.returncode, cc.group(1) if cc else '### UNREAD', len(hits), 'NOT RUN (no cell to change)' if cc and cc.group(1) == '0' and not hits
        else '### TO BE RUN')]
    put_txt('b678_correspondence_dry.txt', L)
    print(L[-1])


NH = ('*Appended 2026-10-17 by b678 beneath the nine-kernels item (:14440), under `(R288)`(3) -- SIDE-silence-principle’s FIRST RELAY RUNNER '
      'PRINT BANKS, AT v0.2.0’S LEAN TEXT AND AT ITS TAG v0.2.1:*')
NB = (' SIDE-silence-principle, “at v0.2.0 (3 cells)” among the nine, is printed by the hosted runner at both trees of its re-cut (relay '
      'data/b678_cut.txt): run 39055170313 at 6968b6c, its Lean text v0.2.0’s (the workflow and the print list committed atop it, no .lean '
      'byte), and run 39055212218 at the cut 8829bcc, merged as 96b3098 and tagged v0.2.1 -- 58 of 58 declarations printed in each, DERIVES, '
      'the prints equal line for line (relay data/b678_axioms_SIDE-silence-principle_before.txt, data/b678_axioms_SIDE-silence-principle_after.txt). '
      'The Correspondence generator, run dry after the tag, would change 5 cells in FOUNDATIONS_OF_THE_SIDE_PROGRAMME :628-:630 and still read '
      'them “NO PRINT BANK AT v0.2.1”, its print-bank reader not reading these runner banks (relay data/b678_correspondence_dry.txt); its run '
      'mode is not run in this act, and the five cells are carried here with the reader.')


def c3(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', NH, NL + NH + NB + NL)], 'b678_record_lines_c3.json', 'c3',
         check=[('OPEN_TRAILS.md', 14440, 'THE KERNELS WITH NO RELAY PRINT BANK AT THEIR TAG')], dry=dry)


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c2': c2, 'naming': naming, 'runner': runner, 'prints': prints,
          'cutdiff': cutdiff, 'corr': corr, 'c3': c3}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b678_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
