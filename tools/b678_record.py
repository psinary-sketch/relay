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


# ================================================================================ THE ANSWERS BANK (b677's route, carried)
def _session_rows():
    for sid, anc in ((K.SESSION_ID, K.ANCHOR),) + K.SESSIONS_AFTER:
        start = None
        for i, raw in enumerate(io.open('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, encoding='utf-8', errors='replace'), 1):
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if start is None and anc in raw.replace('’', "'") and o.get('type') == 'user' and not o.get('isCompactSummary'):
                start = i
            if start is not None:
                yield i, o, start, sid
        if start is None and sid != K.SESSION_ID:
            sys.exit('### THE ANCHOR %r IS NOT A USER LINE OF SESSION %s -- NOTHING WRITTEN' % (anc, sid))


def answers(*a):
    """data/b678_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st, sid in _session_rows():
        start = st if sid == K.SESSION_ID else start
        ln = i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i)
        m = o.get('message') or {}
        cs = m.get('content')
        att = o.get('attachment') or {}
        texts = []
        if att.get('type') == 'queued_command' and isinstance(att.get('prompt'), str):
            texts = [att['prompt']]
        elif o.get('type') == 'user' and not o.get('isCompactSummary'):
            texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
            for t in texts:
                if t and not t.lstrip().startswith(('<', 'BEGIN', 'RULING')) and len(t) < 400 and i > st:
                    plain_.append((ln, t.strip()))
        texts = [re.sub(r'(?s)^\s*<pasted_content[^>]*>\s*(.*?)\s*</pasted_content[^>]*>\s*$', r'\1', t or '') for t in texts]
        ask = set(x[1] for x in calls)
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|=")BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
                if K.ANCHOR not in mm.group(1) and 'RULING (' not in mm.group(1)[:20]:
                    words.append((ln, mm.group(1)))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %s, %s)' % (cid, K.SESSION_ID, i, ts))
        for k, q in enumerate(inp.get('questions', []), 1):
            n += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT', None))
        L += ['RESULT (transcript line %s, %s): %s' % (r[0], r[2], r[1]), '']
    W, seen = [], set()
    for i, w in words:
        if w in seen:
            continue
        seen.add(w)
        W += ['### THE AUTHOR`S WORD (transcript line %s), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b678 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b678_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b678_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b677's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
CORR_CITE = '(FINDINGS :8881; Zeta23/Defs.lean :142 at e36ea31)'


def read_runner_row(r):
    """a row of data/b678_runner_rows.json (this act's runs, the named kernel's): the kernel, a label (before or after), a 40-hex ref, a run
    id, a gate; returns (label, gate)."""
    if not isinstance(r, dict) or r.get('kernel') != K.CANDIDATE or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger or pin;
    returns (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


def read_corr_row(r):
    """a written row of data/b678_corrigendum.json: a ledger file, a line (an int), the quote (the sentence verbatim, or the ledger's bytes
    through a cut span's closing backtick, its extension named), and the reading ending in the two cites; returns (file, line)."""
    if not isinstance(r, dict) or r.get('file') not in ('FINDINGS.md', 'OPEN_TRAILS.md') or not isinstance(r.get('line'), int) \
            or not (r.get('quote') or '').strip() or not (r.get('s') or '') or not (r.get('reading') or '').endswith(CORR_CITE) \
            or (r['quote'] != r['s'] and not r.get('extended')):
        raise ValueError('corrigendum row of another shape: %r' % (str(r)[:120],))
    return r['file'], r['line']


READERS += ['read_runner_row', 'read_order_row', 'read_corr_row']


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')


def delete_shape(cmd):
    """(R288)(4), N4: a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bbranch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if 'branch' in r['cmd']]
    L = ['b678 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE (N4: one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(mv),
                                                                          sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b678_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b678_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', K.CANDIDATE]    # ### the kernels re-cut at b674, b676 and this act


def kernels(*a):
    ks = _kerns()
    put_json('b678_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b678_defects.txt').split(NL)
    for i, l in enumerate(L):
        if DEFECT_ROW.match(l):
            j = i + 1
            while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
                j += 1
            m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
            if m:
                out.append(m.group(0)[:-1])
    return out


def defects(*a):
    t = rdn('b678_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b678_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b678_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b678_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


# ================================================================================ COMPONENT 4: THE CARRY-TIME READING ((R288)'s ferry)
def repairs(*a):
    """data/b678_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b677 copy is read against
    b677's seal hash (relay data/b677_seal_hashes.json) first, and its diff against that copy counted by hunks; a repair is a hunk that answers
    a defect, named with it."""
    import hashlib
    seal = jl('b677_seal_hashes.json').get('tools') or {}
    rows = []
    for t7 in ('b677_citation.py', 'b677_closing.py', 'b677_reg_gate.py', 'b677_regspec.py', 'b677_tests.py', 'b677_worklist.py',
               'b677_record.py', 'b677_checks.py'):
        t8 = t7.replace('b677_', 'b678_')
        old, new = os.path.join(T, t7), os.path.join(T, t8)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t7, t8, now, seal.get(t7), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    rp = rows[-1]
    L = ['b678 -- COMPONENT 4, (R288)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b677`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b677`s sealed copy and its seal record; the hunks of the diff to b678`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the one repair below, which answers a',
         '### defect of a carried route.', '']
    for t7, t8, now, s, nh in rows:
        L.append('  %-20s -> %-20s b677 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t7, t8, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L += ['', '  REPAIR 1 -- THE SUITE`S STANDING PARTS TWO, THE ACT`S ONE ((R288)(1), answering b677`s pre-run at 557 s, data/b677_arms_prerun_standing.txt):',
          '  tools/b678_checks.py runs the standing arms in two foreground parts (standing-a: every standing arm but two, over the three arms at',
          '  HEAD, the written files, the public bytes and the prior banks; standing-b: G-ACTROOT-VERIFY and G-SHARED-ADDITIVE, over the act-root',
          '  chain and the shared additive files) and the act`s arms in a third, each part computing only the sources its arms read;',
          '  data/b678_rules.txt row 1.',
          '', '### ### **REPAIRS 1 ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
              'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b678_tool_repairs.txt', L)
    print(NL.join(L[-(len(rows) + 8):]))


ROOT_EXCLUDE = re.compile(r'^b678_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b678_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b678_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b678'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b678_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b678_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b678 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b678_root_arm.txt', L)
    put_json('b678_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b678 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b678_table_final.txt', L)
    put_json('b678_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b678_registration_2026-10-17.txt'
FACE = os.path.join(D, 'b678_registration_2026-10-17.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b665's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b_ = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b_)
            os.replace(p + '.tmp', p)
        return r.returncode, b_.decode('utf-8', 'replace')
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b678_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b678_regspec.py')], 'b678_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b678_satisfiable.json', '--emit', 'b678'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b678_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b678_census_stepzero.txt'), ('b327_faces_census.py', 'b678_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b678_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b678'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b678_reg_gate.txt', 'data/b678_reg_termscan.txt', 'data/b678_regspec_run.txt', 'data/audit_b678_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b677_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
N5_KERNEL = ('.github/workflows/build-module.yml', 'SIDESilencePrinciple/Basic.lean', 'print_targets.txt')


def TRAIL_HEAD():
    return ('### b678 — lane two, act one hundred and five, the re-cut act under (R288): the Q0 lines answered by one corrigendum entry; '
            'SIDE-silence-principle’s docstrings re-cut, v0.2.1')


def _calls():
    return jl('b678_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _epoch(ts):
    import calendar
    return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')) if ts else None


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _ledger_lines_unmoved():
    """N2: each of the 35 ledger lines the corrigendum answers, its text at PLACE-papers before the act and now, byte for byte."""
    cj = jl('b678_corrigendum.json')
    keys = sorted(set((r['file'], r['line']) for r in (cj.get('rows') or []) + (cj.get('carried') or [])))
    pre = dict((f, (_show(PP, K.PRE_PP, f) or '').split(NL)) for f in N5_PP)
    now = dict((f, rd(os.path.join(PP, f)).split(NL)) for f in N5_PP)
    moved = [(f, n) for f, n in keys if n > len(pre[f]) or pre[f][n - 1] != now[f][n - 1]]
    return keys, moved


def _n1():
    cm = jl('b678_commands.json')
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == len(K.T_RUNS)
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b678_commands.txt, %d commands read); the builds on the hosted '
        'runner alone, dispatched %d times, one per tree state (runs %s)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('rows') or []),
                                                                              len(cm.get('dispatches') or []), ', '.join(str(r) for r, _l in K.T_RUNS)))


def _n2():
    cj = jl('b678_corrigendum.json')
    try:
        got = [read_corr_row(r) for r in cj.get('rows') or []]
    except Exception:
        got = []
    keys, moved = _ledger_lines_unmoved()
    adds = _ledger_adds()
    recut = len([h for h in jl('b676_q0_lines.json').get('hits') or [] if h.get('reading') == 'TO RE-CUT'])
    ok = bool(got) and len(got) == recut - len(cj.get('carried') or []) and not moved and len(keys) == 35 \
        and adds.count('## Q0 outside the kernel’s configuration class') == 1
    return ('HELD' if ok else 'REFUTED'), (
        'the 35 ledger lines the corrigendum answers, each read at PLACE-papers %s and now: moved %s; the corrigendum entry the one write that '
        'answers them (FINDINGS :%s, one entry of its title among the lines appended); its rows %d through the reader, the bank`s TO RE-CUT %d '
        'less the carried %d' % (K.PRE_PP, moved or 'NONE', cj.get('entry_line'), len(got), recut, len(cj.get('carried') or [])))


def _cut_fig():
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', rdn('b678_cut.txt'))
    return (m.group(1), m.group(2)) if m else ('?', '?')


def _n3():
    nj = jl('b678_naming.json')
    nt = rdn('b678_naming.txt')
    n_at, first_write = _epoch(nj.get('at')), _git_ct(K.TD, K.T_WORKFLOW)
    order = [nt.find(x) for x in ('### THE ORDER, verbatim', '### THE RULE, verbatim', '### THE TABLE ROWS, verbatim', '### NAMED:')]
    b, a_ = _cut_fig()
    pc = rdn('b678_prints_compare.txt')
    rows = jl('b678_runner_rows.json').get('rows') or []
    try:
        gates = dict(read_runner_row(r) for r in rows)
    except Exception:
        gates = {}
    ok = all(i >= 0 for i in order) and order == sorted(order) and n_at and first_write and n_at < first_write and nj.get('named') == K.CANDIDATE \
        and b != '?' and int(a_) <= int(b) and 'EQUAL LINE FOR LINE True' in pc and gates == {'before': 'DERIVES', 'after': 'DERIVES'}
    return ('HELD' if ok else 'REFUTED'), (
        'the order`s line, the rule row and the table rows printed verbatim before the naming line in relay data/b678_naming.txt (written %s), '
        'before the kernel`s first write (the workflow commit %s, %s); the distance by b670`s method before %s, after %s (data/b678_cut.txt); '
        'the `before` and `after` prints %s (data/b678_prints_compare.txt), both runs %s' % (
            nj.get('at'), K.T_WORKFLOW, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(first_write)) if first_write else '### NONE', b, a_,
            'equal line for line' if 'EQUAL LINE FOR LINE True' in pc else '### NOT EQUAL', gates or '### UNREAD'))


def _n4():
    cm = jl('b678_commands.json')
    shapes = [s for s in cm.get('delete_shapes') or [] if s['deletes']]
    named = [b for _r, bs in K.DELETE for b in bs]
    ok = bool(shapes) and all(len(s['deletes']) == 1 and not s['globs'] for s in shapes) and sorted(d for s in shapes for d in s['deletes']) == sorted(named)
    return ('HELD' if ok else 'REFUTED'), (
        'every branch delete command of step zero: %d commands, each deleting %s, globs in any half %s; the branches deleted %s against the '
        'ruling`s %s (relay data/b678_commands.txt)' % (len(shapes), sorted(set(len(s['deletes']) for s in shapes)),
                                                        sorted(set(c for s in shapes for c in s['globs'])) or 'NONE',
                                                        sorted(d for s in shapes for d in s['deletes']), sorted(named)))


def _n5():
    face = jl('b678_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t_writes = [l for l in g(K.TD, 'log', '--first-parent', '--format=%h', '%s..main' % K.T_PRE_MAIN).split(NL) if l.strip()]
    t_files = sorted(set(x for x in g(K.TD, 'diff', '--name-only', K.T_PRE_MAIN, 'main').split(NL) if x.strip()))
    t_ok = t_files == sorted(N5_KERNEL) and len(t_writes) == 3 and g(K.TD, 'rev-parse', '--short=7', K.T_NEXT_TAG + '^{commit}').strip() == K.T_MERGE
    wf_t = (_show(K.TD, 'main', '.github/workflows/build-module.yml') or '').lower()
    ident = [w for w in ('psinary', 'hotmail', 'seale', 'york', 'orcid', 'secrets.') if w in wf_t]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b678_|audit_b678_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b678_checks as CH
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and t_ok and not ident and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); kernel mains: %s`s written by its three first-parent '
            'commits (the workflow commit, the print-list commit, the docstring merge) and the tag %s, the files %s, %s; every other kernel as the '
            'face read it %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; standing arms added: %s (the act`s arms over its own banks %d); '
            'sealed tools not agreeing %s; relay files of a kind beyond the corrigendum tool, the banks, the act`s tools, the table, the root list, '
            'b677`s push-out bank and the orders bank`s appended row: %s; "patent" in the lines written: %s; an identifier of the author in the '
            'workflow file: %s; outbound requests: the seat`s git reads and pushes, its two dispatches and its run and artifact reads at github.com, '
            'so no identifier of the author placed in a request' % (
                K.DRAFT, K.CANDIDATE, K.T_NEXT_TAG, t_files, t_ok, others_ok, pp_beyond or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS),
                differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', ident or 'NONE'))


def scores(*a):
    TF, RA = jl('b678_table_final.json'), jl('b678_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:600]))
    if 'dry' in a:
        return
    put_json('b678_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    cj = jl('b678_corrigendum.json')
    b, a_ = _cut_fig()
    return ('## Q0 class lines: 36 sentences answered by one corrigendum entry at FINDINGS :%s, %d carried; SIDE-silence-principle re-cut: %s '
            'rows outside LICENSED/CITED to %s, %s' % (cj.get('entry_line', '?'), len(cj.get('carried') or []), b, a_, K.T_NEXT_TAG))


def _finding_text():
    S, J = jl('b678_scores.json'), jl('b678_act_root.json')
    cj = jl('b678_corrigendum.json')
    b, a_ = _cut_fig()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b678_author_answers.txt'), re.M))
    c1 = _rl_lines('b678_record_lines.json') + ['?']
    c2 = _rl_lines('b678_record_lines_c2.json') + ['?']
    c3 = _rl_lines('b678_record_lines_c3.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'The 36 sentences that placed Q0 in the kernel’s configuration class are answered by one generated corrigendum entry (FINDINGS :%s), each '
         'quoted with its corrected reading in one clause citing b675’s finding and the strip field, the 35 ledger lines left as written; and '
         'SIDE-silence-principle’s docstrings now say what its file compiles at its tag %s: of the four rows outside LICENSED or CITED, three '
         'match and one is cut in part (Theorem 8.1’s title standing), the 58 prints equal before and after on the hosted runner. Nothing here '
         'proves RH or GRH.' % (cj.get('entry_line'), K.T_NEXT_TAG), '',
         '*Filed at b678 on the author’s ruling `(R288)`%s. Banks: relay `data/b678_corrigendum.txt`, `data/b678_naming.txt`, `data/b678_cut.txt`, '
         '`data/b678_cut_diff.txt`, `data/b678_prints_compare.txt`, `data/b678_correspondence_dry.txt`, `data/b678_act_root.txt`; the tool '
         '`tools/b678_corrigendum.py`.*' % ((' and the navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed, after one of the seat’s own predicates '
         'was read unwrapped before banking. b677 at its weight (FINDINGS :%s), its run readings printed from their banks by line.' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0]), '',
         '**The corrigendum** (`(R288)`(2)): relay tools/b678_corrigendum.py, committed alone, generated the entry from the bank’s TO RE-CUT '
         'rows: %d written, %d carried, the count equal to the hand count 36; one row quoted through the closing backtick of a code span the '
         'survey had cut (FINDINGS :4437); the rowgen diff after it moved nothing; `W-ORD-Q0-CLASS-LINES` DISCHARGED on the entry (OPEN_TRAILS '
         ':%s), its row in the orders bank with Status and pin.' % (len(cj.get('rows') or []), len(cj.get('carried') or []), c2[0]), '',
         '**The re-cut** (`(R288)`(3)): the next kernel by descending count (b652’s order), SIDE-bijection and SIDE-silence-principle tied at 4, '
         'their counts of any kind equal, the larger table named (48 rows against 30), the order’s line, the rule row and the table rows printed '
         'before any kernel write; the workflow (5d2e587) and the 58-name print list (6968b6c) committed alone on its main; run 39055170313 at '
         'that main, its Lean text v0.2.0’s; the cut 8829bcc on recut-silence-principle-b678, its docstrings alone; run 39055212218; both '
         'DERIVES, the prints equal line for line; merged as 96b3098, tag %s. The distance by b670’s method %s to %s. The generator dry would '
         'change five cells and still read them NO PRINT BANK, its reader not reading this act’s runner banks; not run, carried beneath the '
         'nine-kernels item (OPEN_TRAILS :%s).' % (K.T_NEXT_TAG, b, a_, c3[0]), '',
         '**The tools** (the ferry’s Component 4): carried from b677’s sealed copies with one repair at carry -- the suite’s standing arms in '
         'two foreground parts and the act’s in a third, (R288)(1) (relay data/b678_tool_repairs.txt, data/b678_rules.txt); the closing dry-run a '
         'gate step before the seal.', '',
         '**The root.** b678 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b676’s Q0 survey and b675’s finding (FINDINGS :8881) against the 35 '
         'ledger lines, and b647’s table of SIDE-silence-principle with b670’s licensed table, b674’s rule and b676’s route; it is re-read by the '
         'next re-cut act, which takes the next kernel at its count, and by any reader of the ledgers, who finds the corrected reading in one '
         'place. It strengthens the programme’s offerings of a ledger whose readings of its control object agree with the kernel’s type and of '
         'kernel docstrings that say what they compile.', '',
         '**Carried to:** SIDE-silence-principle’s Theorem 8.1 title and header introduction, SIDE-trivium’s header introduction and SIDE-window’s '
         'Sawtooth marker, for the next re-cut of each kernel; the five Correspondence cells with the generator’s reader (the nine-kernels item); '
         'the strip variant, b679; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the next kernel named by b652’s order and, at the tie, by b674’s row 2 to the larger table (relay data/b678_naming.txt); '
              '(2) each ACTION applied verbatim and not extended, so Theorem 8.1’s title and the header’s introduction stand as residues; (3) '
              'FINDINGS :4437 quoted through the closing backtick of the code span the survey cut, the ledger’s own bytes; (4) the generator’s run '
              'mode not run, its five cells carried, N5 forbidding a roster write in this act')


def _trail_text():
    S, J = jl('b678_scores.json'), jl('b678_act_root.json')
    fj = jl('b678_findings.json')
    cj = jl('b678_corrigendum.json')
    b, a_ = _cut_fig()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b678_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b678_record_lines.json') + ['?']
    c2 = _rl_lines('b678_record_lines_c2.json') + ['?']
    c3 = _rl_lines('b678_record_lines_c3.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R288) ratified.** (1) b677 at its weight. (2) The Q0 lines answered by one corrigendum entry. (3) The licensed table’s next '
             'document cut. (4) The branches. (5) The read-first bank. (6) The draft held at v5. (7) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b677’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-Q0-CLASS-LINES` '
             'discharged), :%s (the print banks beneath the nine-kernels item); this record.' % (c1[0], cj.get('entry_line'), fj.get('entry_line'),
                                                                                                 c2[0], c3[0]), '',
             '**Act root:** b678 `%s` (previous `%s`, b677’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b678_author_answers.txt); none after the root.' % (n_ans, len(_calls())), '',
             '**The corrigendum:** FINDINGS :%s, %d rows, %d carried (relay data/b678_corrigendum.txt).' % (
                 cj.get('entry_line'), len(cj.get('rows') or []), len(cj.get('carried') or [])), '',
             '**The re-cut:** SIDE-silence-principle %s to %s by b670’s method; main 96b3098, tag %s; runs %s; prints equal.' % (
                 b, a_, K.T_NEXT_TAG, ' and '.join(str(r) for r, _l in K.T_RUNS)), '',
             '**The open orders:** `W-ORD-EPSTEIN-BALL-WIDTH` (b681, the narrowing act); `W-ORD-MAP-ANGLE-FORM` (after it); '
             '`W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the strip variant, b679.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b678_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b678_scores.json')
    L = ['=' * 104, 'b678 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b678_defects.txt').rstrip(NL).split(NL)
    put_txt('b678_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b678_scores.json', 'b678_findings.json', 'b678_trail.json', 'b678_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    cj = jl('b678_corrigendum.json')
    c1 = _rl_lines('b678_record_lines.json') + ['?']
    c2 = _rl_lines('b678_record_lines_c2.json') + ['?']
    c3 = _rl_lines('b678_record_lines_c3.json') + ['?']
    L = ['b678 -- THE COMPONENTS, BANKED UNDER (R288).', '',
         '### COMPONENT 0 : the citation check (data/b678_citation_check.txt), step zero (data/b678_ferry.txt, data/b678_readfirst.txt, '
         'data/b678_stepzero.txt, data/b678_tests_stepzero.txt, data/b678_rowgen_stepzero.txt, data/b678_branches.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 1 : b677`s weight FINDINGS :%s' % c1[0],
         '### COMPONENT 2 : the corrigendum (tools/b678_corrigendum.py, data/b678_corrigendum.txt) FINDINGS :%s ; W-ORD-Q0-CLASS-LINES discharged '
         'OPEN_TRAILS :%s ; rowgen after (data/b678_rowgen_after.txt) ; N2 %s' % (cj.get('entry_line'), c2[0], S['N2'][0]),
         '### COMPONENT 3 : the naming (data/b678_naming.txt), the cut (data/b678_cut.txt, data/b678_cut_diff.txt), the runs, the prints '
         '(data/b678_prints_compare.txt), the generator dry (data/b678_correspondence_dry.txt) ; the print banks beneath the nine-kernels item '
         'OPEN_TRAILS :%s ; N3 %s' % (c3[0], S['N3'][0]),
         '### COMPONENT 4 : the carry-time reading (data/b678_tool_repairs.txt), the dry-run steps (data/b678_reg_gate.txt), the seal '
         '(data/b678_seal_hashes.json), the suite, the rules (data/b678_rules.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b678_components.txt', L)
    print(NL.join(L[2:]))


def _land_one(path, head, e, bank, extra):
    if odd_lines(e):
        sys.exit('### ODD BACKTICKS -- NOTHING WRITTEN: %s' % odd_lines(e)[:3])
    guard_absent(path, head)
    r = append_to(path, e)
    ln = read_head(path, head)
    put_json(bank, dict(extra, line=ln, head=head, append=r))
    return ln


def findings(*a):
    t, e = _finding_text()
    e = conv(e)
    dry = 'dry' in a
    cells, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b678_findings.json', dict(title=t))
    j = jl('b678_findings.json')
    j['entry_line'] = ln
    put_json('b678_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells)
        return
    if cells or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b678_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c2': c2, 'naming': naming, 'runner': runner, 'prints': prints,
          'cutdiff': cutdiff, 'corr': corr, 'c3': c3, 'answers': answers, 'commands': commands, 'kernels': kernels, 'defects': defects,
          'repairs': repairs, 'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores,
          'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b678_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
