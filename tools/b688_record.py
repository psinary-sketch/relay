# -*- coding: utf-8 -*-
"""b688_record.py -- THE ACT'S RECORD TOOL, b688 under (R298).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b688's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b687_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes, the
### answers route, the command bank with G-EDIT-ROUTE's repaired reading -- its previous-act window b687's capture in this same session, from
### its post-push combine to (R298)'s line --, the defects, the carry-time reading) and b686_record.py (the naming, the runner, the prints and
### the cut's diff, each taking its kernel as an argument) in stages: the step-zero and Component 1 routes first; the faces, naming, cut and
### residue routes at Components 2-4; the late routes at Component 5.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b688_record.py <route> [dry]`.
"""
import io
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
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b688_worklist as K          # noqa: E402

SP = K.SP
STANDIN = 'standin' in sys.argv[2:]          # ### the dry-run step's stand-ins, by argument (environment variables left as they are)
RELAY = ROOT


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
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b688_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b688_findings.json': dict(entry_line=99999, title='stand-in'),
        'b688_trail.json': dict(line=99999),
        'b688_act_root.json': dict(root='0' * 64, previous='898a4100' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b688's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b688_scanfile_%s.md' % tag)
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
    """a row of data/b688_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


def read_runner_row(r):
    """a row of data/b688_runner_rows.json: the kernel, its label (before or after), the ref (40 hex), the run id and the gate; returns
    (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_runner_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b688_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
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
    L = ['b688 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b688_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R298)(6))
def branches(*a):
    """every branch (R298)(6) names, its tip read before any delete, its fate; any branch under the push-b687 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b688_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith('push-b687') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b688 -- STEP ZERO, (R298)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no branch',
         '### the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches under the push-b687 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b688_branches.txt', L)
    put_json('b688_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R298)(1)
WH = ('*Appended 2026-10-19 by b688 to b687’s entry (:9286), under `(R298)`(1) -- b687 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b687_closing.txt), P3 STANDING DERIVED, NOT COMPILED:*')
WB = (' “b687 closed: relay 24b23df1, PLACE-papers 51d3aac; suite 114 of 115; root 898a41008e25cfe2…; 7 prompts answered; 8 defects” '
      '(data/b687_closing.txt :1), the closing pushed and read back at relay de011ebd (data/b687_closing_push_out.txt). Reading (i) on T ≥ e '
      'gave a_e = 0.218287, b_e = 0, c_e = 1.731426, below every located bound at e, 10, 100, 1000 and 10⁴ -- Hasanalizade-Shen-Wong at 9.3675 '
      'and at Bellotti-Wong’s corrected 9.4925, Trudgian 2014, Platt-Trudgian 2015, and Backlund’s row where it applies -- entered as a reading '
      'under the author’s amendment, with the crossovers printed (Platt-Trudgian 2015 below the derived bound beyond T ≈ 1.28·10⁵, Trudgian '
      '2014 beyond T ≈ 1.44·10⁶, Hasanalizade-Shen-Wong beyond T ≈ 5.9·10²⁹) (data/b687_matched.txt). Readings (ii)-(iii): J(T) below S(T) '
      'and the counts at ρ′ = 1.4, 1.6, 1.8 below their bounds for ζ at T = 100, 1000, 10⁴ at the derivation’s c = 1.5, r = 1.98 and at 1.7, '
      '2.05 beside, and for Z_Q at 50, 100, 149, the band (150, 151.59] counted by the argument principle at two zeros, both on the line; the '
      'literal inner disc vacuous for ζ (data/b687_jensen_zeta.txt, data/b687_jensen_q0.txt). Reading (iv): 114 of 114 intermediate '
      'inequalities holding, the narrowest margin 0.058 on the Jensen circle’s envelope (data/b687_steps.txt); C1 and C2 as planted; the '
      'composition holding HCount at every t > 149, the narrowest margin 41.98 on [150, 151.5], κ₁ = 1.18 < 10 (data/b687_composition.txt). '
      'P3 entered as “DERIVED — constants certified in balls, analytic steps sourced by line, intermediate inequalities checked against computed '
      'values at sample heights, the ζ instance inside the located bounds at matched range, not compiled” (data/b687_p3_status.txt); '
      '`W-ORD-EPSTEIN-COUNT` DISCHARGED-BY-DERIVATION at OPEN_TRAILS :14890, `W-ORD-EPSTEIN-COUNT-LEAN` at :14892, trigger “a research act '
      'after b690”; the Q0 results of b675, b679 and b683 re-read (data/b687_q0_reread.txt). Suite 114 of 115 pre-push and post-push, '
      'G-EDIT-ROUTE declared by name -- the arm now reading sed in any form and finding the seat’s five reads; all eight scores HELD; root '
      '898a4100 over 54 banks; mirror-refresh-2026-10-19-b687.zip CLEAN with the root line. Eight defects: (a) the seat’s five sed reads; '
      '(b)-(f) the navigator’s five (the arm’s file, the untested comparison claim, “Platt-Trudgian 2021”, Z_Q’s parameters on ζ, the vacuous '
      'disc); (g) the band priced at minutes and taking about 1.2 hours, the 590 s guard stopping two calls before any bank was lost; (h) the '
      'seat’s lattice-sum route for σ > 2.5, added where b667’s Z_Q route stops at 2.5 and checked against it at three points -- entered at '
      'b688 on its check (relay data/b688_lattice_route.txt). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b688_record_lines.json', 'c1', entry=K.B687_ENTRY,
         check=[('FINDINGS.md', K.B687_ENTRY, '## The b685 derivation tested'), ('OPEN_TRAILS.md', K.B687_TRAIL, '### b687')], dry=dry)


# ================================================================================ COMPONENT 2: THE FACES LINE, (R298)(3) AND THE AUTHOR'S WORD
def faces(*a):
    """b680's form: the control (b680's list re-emits the committed page byte for byte), the emission of data/b688_nodes_zeta.txt, both by
    tools/chain_page.py --from-output data/b643_probe_out_zeta.txt into the scratchpad (no lean); the diff banked as data/b688_faces_diff.txt;
    with `write`, the page written by the generator itself (its --out the page) and read back equal to the emission."""
    import difflib
    import hashlib
    page = os.path.join(PP, K.FACES_PAGE)
    probe = os.path.join(ROOT, *K.PROBE.split('/'))

    def emit(nodes, out):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', os.path.join(ROOT, *nodes.split('/')),
                            '--probe-dir', SP, '--out', out, '--from-output', probe], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.returncode, ((r.stdout or '') + (r.stderr or '')).strip().split(NL)[-1:]
    committed = open(page, 'rb').read()
    head = g(PP, 'show', 'HEAD:' + K.FACES_PAGE).encode('utf-8')
    cpath, npath = os.path.join(SP, 'b688_faces_control.md'), os.path.join(SP, 'b688_faces_emit.md')
    rc0, t0 = emit(K.NODES_PRE, cpath)
    ctl = open(cpath, 'rb').read() if os.path.exists(cpath) else b''
    control = rc0 == 0 and ctl == committed
    rc1, t1 = emit('data/b688_nodes_zeta.txt', npath)
    new = open(npath, 'rb').read() if os.path.exists(npath) else b''
    d = list(difflib.unified_diff(committed.decode('utf-8').split(NL), new.decode('utf-8').split(NL), 'committed', 'b688', n=0, lineterm=''))
    add = sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in d if l.startswith('-') and not l.startswith('---'))
    written, back = False, False
    if 'write' in a:
        if not control or rc1 != 0:
            sys.exit('### THE CONTROL OR THE EMISSION FAILED -- THE PAGE IS NOT WRITTEN')
        rc2, t2 = emit('data/b688_nodes_zeta.txt', page)
        written = rc2 == 0
        back = open(page, 'rb').read() == new
    row = rd(os.path.join(ROOT, 'data', 'b688_nodes_zeta.txt')).split(NL)[K.NODES_ROW - 1]
    L = ['b688 -- COMPONENT 2, (R298)(3): THE FACES LINE THROUGH THE GENERATOR, ON THE AUTHOR`S WORD (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py --from-output relay %s (no elaboration; no lean on this host)' % K.PROBE,
         '### the control: b680`s list (relay %s) re-emits the committed page byte for byte: %s (%d bytes ; exit %d ; the committed page equal to HEAD`s '
         'blob %s)' % (K.NODES_PRE, control, len(ctl), rc0, committed.replace(b'\r\n', b'\n') == head.replace(b'\r\n', b'\n')),
         '### the new list: relay data/b688_nodes_zeta.txt (b680`s 172 lines, :167 replaced by the amended row, every other line unchanged); emitted '
         '%d bytes, exit %d, sha256 %s' % (len(new), rc1, hashlib.sha256(new).hexdigest()[:16]),
         '### the diff, committed page -> b688 emission (lines added %d, removed %d):' % (add, rem)] + ['    ' + l for l in d] + [
         '', '### the page written by the generator and read back equal to the emission: %s' % (back if 'write' in a else 'NOT YET (dry)'),
         '### the row carries T-COUNT beside P3 and no backtick: %s' % ('T-COUNT (P3) derived' in row and '`' not in row), '',
         '### ### **CONTROL EQUAL %s ; LINES ADDED %d ; REMOVED %d ; PAGE WRITTEN %s.**' % (control, add, rem, written and back)]
    if 'write' in a:
        put_txt('b688_faces_diff.txt', L)
    print(NL.join(L[2:6] + L[-4:]))


# ================================================================================ COMPONENT 3: THE NAMING, (R298)(4) -- before any kernel write (b686's)
import itertools                   # noqa: E402


def _kern_rows():
    """the kernels table's rows (data/b647_table_kernels.txt): rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED (its header :4)."""
    out = []
    for i, l in enumerate(rdn(K.KERNELS_BANK).split(NL), 1):
        m = re.match(r'^  (SIDE-[\w-]+)\s+([0-9a-f]{7}) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', l)
        if m:
            out.append(dict(line=i, text=l, kernel=m.group(1), pin=m.group(2), rows=int(m.group(3)), under=int(m.group(5)),
                            over=int(m.group(6)), unlic=int(m.group(7))))
    return out


def _cut_figure(t, k):
    """a kernel's figure after its cut, read from its cut bank: b684's bank carries four kernels -- the named one's verdict line and the
    residues' re-read rows '<kernel> before n (<bank>) ; after m'; a bank of one kernel, its own verdict line."""
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', t)
    if k == 'SIDE-class-number-anomaly' or 'RESIDUES' not in t or k == 'SIDE-spinor':
        return int(m.group(2)) if m else None
    sec = re.search(r'%s before (\d+) \([^)]*\) ; after (\d+)' % re.escape(k), t)
    return int(sec.group(2)) if sec else None


def naming(*a):
    """(R298)(4) and N2: the order's line (data/b652_ferry.txt :19), the tie-break rule's row and the table rows printed verbatim from their
    banks; every kernel's standing count read from the licensed table (a kernel cut since its read stands at its cut bank's figure); the
    document named by the descending count and, at a tie, by the rule's letter; then the named kernel's workflow directory, print list and
    print bank read or declared absent -- before any kernel write. data/b688_naming.txt (.json). Carried from b686_record.py's naming."""
    rules = rdn(K.RULES_BANK).split(NL)
    i0 = [i for i, l in enumerate(rules) if l.startswith('  (%d) ' % K.TIE_RULE_ROW)][0]
    rule = [rules[i0]] + [l for l in itertools.takewhile(lambda x: x.startswith('      '), rules[i0 + 1:])]
    order_line = rd(os.path.join(D, 'b652_ferry.txt')).split(NL)[18]
    lt = rdn(K.TABLE_BANK).split(NL)
    standing = {}
    for i, l in enumerate(lt, 1):
        m = re.match(r'^  (SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)\s+(\d+) ->\s+(\d+)', l)
        if m:
            standing[m.group(1)] = (i, int(m.group(4)), l)
    cut_since = {}
    for k, bank, needle in K.CUT_SINCE:
        t = rd(os.path.join(ROOT, *bank.split('/')))
        f = _cut_figure(t, k) if needle in t else None
        if f is not None:
            cut_since[k] = (f, bank)
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
    td = 'D:/' + named if named else None
    wf = g(td, 'ls-tree', '--name-only', 'main', '.github/workflows/').split() if td else []
    pt = g(td, 'ls-tree', '--name-only', 'main').split() if td else []
    pb = sorted(set(g(ROOT, 'grep', '-lE', r"'LiLinearMap\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)", '--', 'data/').split())) \
        if named == 'SIDE-li-map' else []
    tags = sorted(g(td, 'tag', '--list').split(), key=lambda x: [int(n) for n in re.findall(r'\d+', x)]) if td else []
    lf = (_show(td, 'main', 'lakefile.lean') or '') + (_show(td, 'main', 'lakefile.toml') or '') if td else ''
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    L = ['b688 -- COMPONENT 3, (R298)(4): THE ORDER, THE RULE ROW AND THE TABLE ROWS, VERBATIM, BEFORE THE DOCUMENT IS NAMED (%s)' % utc(), '',
         '### THE ORDER, verbatim (relay data/b652_ferry.txt :19): ' + order_line.strip(),
         '### THE RULE, verbatim with path and line (relay data/%s :%d):' % (K.RULES_BANK, i0 + 1)] + ['    ' + l for l in rule] + [
         '', '### THE TABLE ROWS, verbatim with path and line: the licensed table (relay data/%s) for each kernel of the kernels table (relay' % K.TABLE_BANK,
         '### data/%s, columns rows | MATCHES | UNDERSTATES | OVERREACHES | UNLICENSED, its header :4); a kernel cut since its read stands at' % K.KERNELS_BANK,
         '### its cut bank`s figure (%s); ordered by the count now standing:' % '; '.join('%s at %d, relay %s' % (k, v[0], v[1]) for k, v in cut_since.items())]
    for now, anyk, nrows, k, ln, r in rank:
        L.append('  %2d  %-34s licensed table :%s  "%s"' % (now, k, ln, (standing.get(k) or (0, 0, ''))[2].strip()))
        L.append('      %-34s kernels table :%d  "%s"  (outside of any kind %d ; rows %d)' % ('', r['line'], r['text'].strip(), anyk, nrows))
    L += ['', '### THE NAMING: the greatest count standing is %d, carried by %s%s.' % (
        top, ', '.join(x[3] for x in tied), ' alone, so no tie and the rule of row %d not reached' % K.TIE_RULE_ROW if len(tied) == 1 else '')]
    if len(tied) > 1:
        L.append('### A TIE: the rule of row %d by its letter -- rows outside LICENSED/CITED of any kind: %s' % (
            K.TIE_RULE_ROW, ', '.join('%s %d (rows %d)' % (x[3], x[1], x[2]) for x in tied)))
    L += ['### NAMED: %s docstrings' % (named or '### NONE'),
          '', '### THE NAMED KERNEL`S WORKFLOW DIRECTORY, PRINT LIST AND PRINT BANK (read before any kernel write):',
          '  %s main %s ; its tags %s, the last %s: .github/workflows/ carries %s -- %s' % (
              named, g(td, 'rev-parse', '--short', 'main').strip(), tags or 'NONE', tags[-1] if tags else 'NONE (no tag at any commit)',
              wf or 'NOTHING', 'a build-module.yml' if any('build-module' in f for f in wf) else 'NO build-module.yml (no dispatch input; no print step)'),
          '  print_targets.txt at its root: %s ; AxiomCheck*.lean at its root: %s ; its tracked files %s' % (
              'print_targets.txt' in pt, [f for f in pt if f.startswith('AxiomCheck')] or 'NONE', pt),
          '  relay tracked banks carrying a printed axiom line of a LiLinearMap declaration (git grep -lE over data/): %s -- %s' % (
              pb or 'NONE', 'NO PRINT BANK' if not pb else 'a print bank'),
          '  its dependency form: no lakefile at main (%s) ; Mathlib by a require clause %s ; lean-toolchain %s ; its build path the plain-lean one of '
          'SIDE-global-section`s workflow (LEAN_PATH=build lean, module by module in import order)' % (
              not lf, bool(req), (_show(td, 'main', 'lean-toolchain') or '').strip()),
          '', '### ### **NAMED %s ; TIED %d ; WORKFLOW build-module.yml %s ; PRINT LIST %s ; PRINT BANK %s ; TAGS %d.**' % (
              named or '### NONE', len(tied), 'PRESENT' if any('build-module' in f for f in wf) else 'ABSENT',
              'PRESENT' if 'print_targets.txt' in pt else 'ABSENT', 'PRESENT' if pb else 'ABSENT', len(tags))]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('b688_naming.txt', L)
    put_json('b688_naming.json', dict(at=utc(), named=named, tied=[x[3] for x in tied], top=top, workflows=wf, print_banks=pb, tags=tags,
                                      rank=[[x[0], x[1], x[2], x[3], x[4]] for x in rank]))
    print(NL.join(L[-12:]))


# ================================================================================ THE RUNS, THE PRINTS, THE CUT'S DIFF (b686's routes, per kernel)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: the kernel's run read by its id; the artifact listed, downloaded by its id into
    memory, its sha256 against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP;
    the axioms output of the print step banked whole, every name of the list matched to one printed line. data/b688_runner_<kernel>_<label>.txt,
    data/b688_axioms_<kernel>_<label>.txt and a row of data/b688_runner_rows.json. Carried from b686_record.py's runner."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b688 -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; %s to %s' % (run_id, run.get('url'), run.get('status'), run.get('conclusion'),
                                                                           run.get('createdAt'), run.get('updatedAt'))]
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
    read_runner_row(row)
    put_txt('b688_runner_%s_%s.txt' % (kernel, label), L)
    if row['artifact_sha256']:
        put_txt('b688_axioms_%s_%s.txt' % (kernel, label), ax.split(NL))
    j = jl('b688_runner_rows.json') if os.path.isfile(os.path.join(D, 'b688_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('b688_runner_rows.json', dict(rows=rows))
    print(NL.join(L))


def prints(*a):
    """`prints <kernel> <before bank> <after bank>`: the 'before' and 'after' axioms outputs compared line for line (the merge only where they are
    equal at every line). data/b688_prints_<kernel>.txt."""
    kernel, bb, ab = a[0], a[1], a[2]
    b, f = rdn(bb), rdn(ab)
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b688 -- THE PRINTS OF %s BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % (kernel, utc()), '',
         '### before: relay data/%s (%d lines) ; after: relay data/%s (%d lines)' % (bb, len(bl), ab, len(fl)), '### the lines that differ:'] + (
             ['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b688_prints_%s.txt' % kernel, L)
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


def cutdiff(*a):
    """`cutdiff <kernel> <base> <tip> <branch> <control needle> <file...>`: the cut's diff printed whole; the files it touches; each file's text
    with its comments stripped compared before and after (equal = no line the elaborator reads changed), with a positive control (a one-word
    code change in the after text must make the comparison unequal). data/b688_cut_diff_<kernel>.txt."""
    kernel, base, tip, branch, needle, want = a[0], a[1], a[2], a[3], a[4], list(a[5:])
    td = 'D:/' + kernel
    files = g(td, 'diff', '--name-only', base, tip).split()
    d = g(td, 'diff', '--unified=0', base, tip).replace(chr(13), '')
    rows = []
    for f in files:
        b, n = _show(td, base, f) or '', _show(td, tip, f) or ''
        eq = _strip_comments(b) == _strip_comments(n)
        ctl = _strip_comments(b) == _strip_comments(n.replace(needle, needle + '_', 1))
        rows.append((f, eq, ctl, needle in n))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b688 -- THE CUT`S DIFF OF %s, RESTRICTED TO COMMENT AND DOCSTRING LINES (%s)' % (kernel, utc()), '',
         '### %s %s (main) -> %s (the cut, %s); files %s ; lines added %d, removed %d' % (kernel, base, tip, branch, files, len(plus), len(minus)),
         '### rows are files: the text with every comment stripped equal before and after ; the control (a one-word code change in the after',
         '### text, %r) unequal ; the control`s needle present:' % needle]
    L += ['  %-34s CODE EQUAL %s ; CONTROL UNEQUAL %s ; NEEDLE PRESENT %s' % (f, eq, not ctl, nd) for f, eq, ctl, nd in rows]
    L += ['', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    ok = files == want and all(eq and not ctl and nd for _f, eq, ctl, nd in rows)
    L += ['', '### ### **FILES %d ; CODE EQUAL WITH COMMENTS STRIPPED %s ; CONTROLS UNEQUAL %s ; COMMENT AND DOCSTRING LINES ALONE %s.**' % (
        len(files), all(r[1] for r in rows), all(not r[2] for r in rows), ok)]
    put_txt('b688_cut_diff_%s.txt' % kernel, L)
    print(L[-1])


# ================================================================================ THE ANSWERS BANK (b687's route, carried)
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
    """data/b688_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
    every word of the author delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim; a word opened by
    BEGIN with no END noted (b687's route)."""
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
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and o.get('type') == 'assistant':
                calls.append((ln, c['id'], c['input'], o.get('timestamp')))
                ask.add(c['id'])
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask and o.get('type') == 'user':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')
                results[c.get('tool_use_id')] = (ln, t, o.get('timestamp'))
                texts.append(t)
        for t in texts:
            for mm in re.finditer(r'(?s)(?:\A\s*|="|="\(for the seat, verbatim\):\s*)BEGIN\s*(.*?)\s*END(?=\s*\Z|")', t or ''):
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
    for cid, (i, t, _ts) in results.items():
        for mm in re.finditer(r'="BEGIN(?:(?!END").)*?"(?=, "|\.\s|$)', t or '', re.S):
            if not re.search(r'END"\s*$', mm.group(0)):
                W += ['### NOTE (transcript line %s): a word opened by BEGIN and carrying NO END marker -- %r ... %r; its text is the RESULT line '
                      'above.' % (i, mm.group(0)[2:80], mm.group(0)[-60:]), '']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b688 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b688_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b688_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE COMMAND BANK (b687's route, carried)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402

SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID


def _anchor_ts(anchor):
    for ln in io.open(SESSION, encoding='utf-8', errors='replace'):
        if anchor in ln:
            try:
                j = json.loads(ln)
            except ValueError:
                continue
            if j.get('type') == 'user' and not j.get('isCompactSummary'):
                return j.get('timestamp')
    return None


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')
SED = re.compile(r'(^|[;&|(]\s*|\s)sed\s')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def sed_cmd(cmd):
    """data/b685_rules.txt row (2): a command carrying sed in any form, read outside quoted strings."""
    return SED.search(QUOTED.sub('""', cmd)) is not None


PREV_ACT, PREV_ANCHOR = 'b687', 'RULING (R297) BEGIN'
SED_KIND = 'R sed in any form (data/b685_rules.txt row (2))'


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act (b687's repair, carried): b687's capture AFTER ITS POST-PUSH SUITE -- every command of this
    session from the call that combined b687's post-push parts into data/b687_checks_postpush.txt up to (R298)'s line (the two acts share
    the session), its closing's commands among them."""
    rows = ER.capture(SESSION, PREV_ANCHOR, SUBAGENTS)
    end = _anchor_ts(K.ANCHOR)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV_ACT in r['cmd'] and '--combine' in r['cmd']]
    if not first or not end:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE OR THIS ACT`S ANCHOR IS NOT IN THE CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV_ACT, r['src'])) for r in rows if first[0] <= r['ts'] < end]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


def edit_route_offences(rows):
    """the arm's offences (b687's repair): tools/edit_route.py's arms (unchanged) and, beside them, sed in any form (data/b685_rules.txt row
    (2)), read outside quoted strings; [(row, [(kind, text)])] for the offending rows."""
    out = []
    for r in rows:
        o = list(ER.offences(r['cmd']))
        if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd']) and not any(k.startswith('S sed') for k, _ in o):
            o.append((SED_KIND, r['cmd'].split(NL)[0][:120]))
        if o:
            out.append((r, o))
    return out


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|--delete\b|(^|[;&|]\s*|\s)rm\s+-|Remove'
                            + r'-Item|\bos\.remove\b')


def delete_shape(cmd):
    """(R298)(6): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
    names = [n for d in dels for n in d.split()]
    return names, [ch for ch in '*?[' if ch in c]


IDENT = ('psinary', 'hotmail', 'seale', 'york', 'orcid', '0009-0008')


def outbound():
    """the act's outbound requests other than git: every WebSearch query, WebFetch URL and subagent prompt from the ruling's line on."""
    out = []
    for i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') in ('WebSearch', 'Agent', 'WebFetch'):
                inp = c.get('input') or {}
                text = inp.get('query') or inp.get('prompt') or inp.get('url') or ''
                out.append(dict(line=i, tool=c['name'], ts=o.get('timestamp'), text=text))
    for r in out:
        r['identifiers'] = [w for w in IDENT if w in r['text'].lower()]
    return out


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'Start-Process|\bnohup\b|run_in_background', r['cmd'])]
    seds = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and sed_cmd(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    ob = outbound()
    L = ['b688 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (b687`s repaired window): %s commands of session %s from %s to (R298)`s '
              'line, its offences printed whole (%d):' % (len(prev), K.SESSION_ID[:8], prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN (%d):' % len(detach)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R298)(6): one branch per command, no glob in any half): ' + ('; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git (web searches, subagent prompts and fetches), each with the author`s identifiers found in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; '
              'MOVE OR DELETE COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(mv), sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl),
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    put_txt('b688_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b688_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        prev=dict(act=PREV_ACT, session=K.SESSION_ID, rows=len(prev),
                                                  offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        seds=[r['n'] for r in seds], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes], outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b688_defects.txt').split(NL)
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
    t = rdn('b688_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b688_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, faces=faces, naming=naming, runner=runner, prints=prints, cutdiff=cutdiff,
              answers=answers, commands=commands, defects=defects)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b688_record.py %s [dry]' % ' | '.join(ROUTES))
        sys.exit(2)
    fn(*sys.argv[2:])
