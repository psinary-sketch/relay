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


# ================================================================================ COMPONENT 3: THE ORDER, THE AUTHOR'S WORD AT THE THIRD PROMPT
OH = ('*Appended 2026-10-19 by b688 beneath b687’s trail record (:14894), under `(R298)`(4) and the author’s word at its third prompt -- '
      '`W-ORD-CORRESPONDENCE-CARRIED-AT` ENTERED:*')
OB = (' the Correspondence generator’s “carried at <kernel> <version>” cells (tools/correspondence_gen.py) to read the pin from the carrying '
      'kernel’s source at that version, not from the carried kernel’s current pin. At b688 its dry run would write PATHS_TO_THE_CRITICAL_LINE.md '
      ':298 as “SIDE-li-map = 9e02bc0 (carried at lv-conservation v0.7.0)”, while SIDE-lv-conservation v0.7.0’s RegisterPentagon.lean :44, '
      ':157 and :241 carry 73cee42 (relay data/b688_correspondence_dry.txt); the five cells of that run, two of SIDE-li-map and three of '
      'SIDE-spinor, held unwritten, their state after SIDE-spinor v0.1.2 banked beside it (relay data/b688_correspondence_dry_2.txt). Where a '
      'standing arm compares the licensed table’s pin against the page’s cell, the mismatch is declared on the face by name with this order '
      'as its reason; no arm added. Trigger: before any generator run that writes a page, at the latest the next re-cut act. Status OPEN.')


def order(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b688_orders_lines.json', 'order', entry=K.B687_TRAIL,
         check=[('OPEN_TRAILS.md', K.B687_TRAIL, '### b687 — lane two')], dry=dry)


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
    bg = _bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


def _bg_calls():
    """### b688's repair (defect (e)): the calls the seat sent with the tool's run_in_background parameter, from the ruling's line on -- a
    parameter of the call, not a word of its command, so a reader of the command text alone counts none of them. {(timestamp, command)}."""
    out = set()
    for _i, o, _st, _sid in _session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and (c.get('input') or {}).get('run_in_background'):
                out.add((o.get('timestamp'), (c.get('input') or {}).get('command')))
    return out


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
    detach = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
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
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (b688`s repair) (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
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


# ================================================================================ THE LATE ROUTES (b687's, carried at Component 5 with b688's names)
def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle', 'SIDE-bijection', 'SIDE-class-number-anomaly',
                                   'SIDE-spinor', 'SIDE-li-map']


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    put_json('b688_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-li-map and SIDE-spinor at their tags, written under Components 3 and 4; no kernel written after this read)' % len(ks))


def seal_hashes():
    import hashlib
    rec_ = jl('b688_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b688_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def root_banks_state(banks, rev='HEAD'):
    """G-ROOT-BANKS-COMMITTED's reading (standing from (R291)(4)): for every bank the root names, its git status, whether HEAD carries it and
    whether HEAD's blob equals the working file; HEAD against the remote main (one ls-remote)."""
    import hashlib
    head = g(ROOT, 'rev-parse', rev).strip()
    rem = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    rows = []
    for b in banks:
        st = g(ROOT, 'status', '--porcelain', '--', b).strip()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (head, b)], capture_output=True)
        p = os.path.join(ROOT, *b.split('/'))
        now = open(p, 'rb').read() if os.path.exists(p) else None
        eq = r.returncode == 0 and now is not None and hashlib.sha256(r.stdout).hexdigest() == hashlib.sha256(now).hexdigest()
        rows.append(dict(bank=b, status=st or 'clean', at_head=r.returncode == 0, equal=eq))
    return dict(head=head, remote=rem, rows=rows, clean=all(x['status'] == 'clean' and x['equal'] for x in rows) and bool(rows),
                pushed=bool(head) and head == rem)


ROOT_EXCLUDE = re.compile(r'^b688_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b688_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY)] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b688 -- G-ROOT-BANKS-COMMITTED`S READING: THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ;'
         ' carried by HEAD ; HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b688_root_banks.txt', L)
    put_json('b688_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b688_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### G-ROOT-BANKS-COMMITTED: A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b688'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b688_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b688_ra_') as tmp:
        cp_ = os.path.join(tmp, os.path.basename(bank_))
        b_ = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b_[0] ^= 0x01
        open(cp_, 'wb').write(bytes(b_))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp_)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['b688 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b688_root_arm.txt', L)
    put_json('b688_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b688 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b688_table_final.txt', L)
    put_json('b688_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


# ================================================================================ THE SCORES: (N1)-(N5) OF (R298)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and not the entry; the entry reads the scorer's bank. `scores` writes
# ### data/b688_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there, the bank it waits on named, and
# ### is read at the close by `scores close` into data/b688_scores_close.json, which no ledger line reads.
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b687_closing_push_out.txt')
ARM_ROW = re.compile(r'^  (G-[A-Z0-9-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(OK|### FAILS|.*)$')
LATTICE_ROWS = (69, 70, 88, 89, 107, 108)
KERN_FILES_DOCSTRINGS = ('LiLinearMap.lean', 'PrimeLedgerPositivity.lean', 'SIDESpinor/SpinorLeg.lean')


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _n1():
    cm = jl('b688_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d, each built on the hosted runner (relay '
        'data/b688_commands.txt, %d commands read)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []),
                                                        len(cm.get('rows') or [])))


def _n2_order():
    """N2's order by commit time: the naming bank before SIDE-li-map's first act commit; both faces rows before the page; R4's ACTION before
    SIDE-spinor's cut."""
    t = dict(naming=_git_ct(RELAY, K.NAMING_COMMIT), limap=_git_ct('D:/SIDE-li-map', K.LIMAP_FIRST), rows=_git_ct(RELAY, K.FACES_ROWS_COMMIT),
             page=_git_ct(PP, K.FACES_PAGE_COMMIT), r4=_git_ct(RELAY, K.R4_COMMIT), cut=_git_ct('D:/SIDE-spinor', K.SPINOR_CUT))
    ok = all(t.values()) and t['naming'] < t['limap'] and t['rows'] < t['page'] and t['r4'] < t['cut']
    return ok, t


def _n2():
    nm, fr, ra = rdn('b688_naming.txt'), rdn('b688_faces_rows.txt'), rdn('b688_residue_actions.txt')
    printed = ('### THE RULE, verbatim with path and line' in nm and '### THE TABLE ROWS, verbatim with path and line' in nm
               and '== THE INPUT ROW' in fr and '== THE SUCCESSOR ROW' in fr and 'THE RE-DERIVED ACTION: RE-CUT:' in ra)
    order_, t = _n2_order()
    ok = printed and order_
    return ('HELD' if ok else 'REFUTED'), (
        'the rule row and the table rows printed from their banks in the naming bank (relay data/b688_naming.txt), both faces rows in theirs '
        '(data/b688_faces_rows.txt) and R4`s re-derived ACTION in data/b688_residue_actions.txt: %s; by commit time, the naming bank (%s) before '
        'SIDE-li-map`s first act commit on main (%s): %s; both faces rows (%s) before the page`s regeneration (PLACE-papers %s): %s; R4`s ACTION '
        '(%s) before SIDE-spinor`s cut (%s): %s' % (
            printed, K.NAMING_COMMIT, K.LIMAP_FIRST, bool(t['naming'] and t['limap'] and t['naming'] < t['limap']), K.FACES_ROWS_COMMIT,
            K.FACES_PAGE_COMMIT, bool(t['rows'] and t['page'] and t['rows'] < t['page']), K.R4_COMMIT, K.SPINOR_CUT,
            bool(t['r4'] and t['cut'] and t['r4'] < t['cut'])))


def _distances():
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', rdn('b688_cut.txt'))
    ms = re.search(r"distance by b670's method (\d+) -> (\d+)", rdn('b688_residue_actions.txt'))
    return ((int(m.group(1)), int(m.group(2))) if m else None), ((int(ms.group(1)), int(ms.group(2))) if ms else None)


def _paths_doc_state():
    pre = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (K.PRE_PP, K.PATHS_DOC)], capture_output=True).stdout
    head = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % K.PATHS_DOC], capture_output=True).stdout
    p = os.path.join(PP, *K.PATHS_DOC.split('/'))
    now = open(p, 'rb').read() if os.path.exists(p) else None
    cr = lambda b: None if b is None else b.replace(b'\r\n', b'\n')   # noqa: E731
    return bool(pre) and cr(pre) == cr(head) == cr(now)


def _n3():
    li, sp = _distances()
    dist = bool(li and sp) and li[1] <= li[0] and sp[1] <= sp[0]
    prints = all('EQUAL LINE FOR LINE True' in rdn('b688_prints_%s.txt' % k) for k in ('SIDE-li-map', 'SIDE-spinor'))
    held = all('WRITTEN 0 ; HELD 5' in rdn(b_) for b_ in ('b688_correspondence_dry.txt', 'b688_correspondence_dry_2.txt'))
    runs = [r for r in (jl('b688_commands.json').get('rows') or []) if 'correspondence_gen.py run' in r.get('cmd', '')]
    paths = _paths_doc_state()
    ok = dist and prints and held and not runs and paths
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by b670`s method, SIDE-li-map %s -> %s (relay data/b688_cut.txt) and SIDE-spinor %s -> %s (data/b688_residue_actions.txt), '
        'each at or below: %s; the before and after prints equal line for line for both kernels (data/b688_prints_SIDE-li-map.txt, '
        'data/b688_prints_SIDE-spinor.txt): %s; no Correspondence cell written by hand -- the five cells held by the author`s word in both dry '
        'banks (data/b688_correspondence_dry.txt, _dry_2.txt): %s, the generator`s write route run %d times, PATHS_TO_THE_CRITICAL_LINE.md '
        'before, at HEAD and in the tree equal: %s' % (li[0] if li else '?', li[1] if li else '?', sp[0] if sp else '?', sp[1] if sp else '?', dist,
                                                        prints, held, len(runs), paths))


def _lattice_reading():
    t = rdn('b688_lattice_route.txt')
    try:
        s2 = t[t.index('== 2. THE THREE-POINT CHECK'):t.index('== 3. THE ROWS')]
        s3 = t[t.index('== 3. THE ROWS'):]
    except ValueError:
        return dict(balls=0, overlap=False, named=False, consumed=False, alone=False)
    vals = [l for l in s2.split(NL) if re.search(r'^\s+(s = .*lattice|b667)\s+Re ', l)]
    balls = sum(1 for l in vals if l.count('±') == 2)
    st = rdn('b687_steps.txt').split(NL)
    named = all(re.search(r'^  :%d\s+Z_Q ' % n, s3, re.M) for n in LATTICE_ROWS)
    consumed = all(len(st) >= n and st[n - 1].startswith('  Z_Q ') and '(iv-4)' in st[n - 1] for n in LATTICE_ROWS)
    files = [x for x in g(RELAY, 'show', '--name-only', '--pretty=format:', K.LATTICE_COMMIT).split(NL) if x.strip()]
    return dict(balls=balls, values=len(vals), overlap='THE THREE-POINT CHECK OVERLAP 3 OF 3' in ' '.join(t.replace('###', ' ').split()),
                named=named, consumed=consumed, alone=files == ['data/b688_lattice_route.txt'])


def _n4():
    r = _lattice_reading()
    ok = r['balls'] == 6 == r.get('values') and r['overlap'] and r['named'] and r['consumed'] and r['alone']
    return ('HELD' if ok else 'REFUTED'), (
        'the lattice-sum route`s steps and its three-point check banked (relay data/b688_lattice_route.txt), committed alone at %s: %s; the '
        'check`s values each a ball for both parts, the route`s and b667`s at each point (%d of %s value rows carrying both radii), the overlap '
        'at all three points: %s; the rows of relay data/b687_steps.txt that consumed it named (:%s) and each an (iv-4) row of Z_Q there: %s, %s' % (
            K.LATTICE_COMMIT, r['alone'], r['balls'], r.get('values', 0), r['overlap'], ', :'.join(str(n) for n in LATTICE_ROWS), r['named'],
            r['consumed']))


def _kernel_writes():
    """the act's two kernels: the files written on main since the main before the act, against the files MERGES names; the tag peeled to the
    merge; the docstring files' cut banks reading comment and docstring lines alone."""
    out = {}
    for k, _pre, _tip, merge, tag, before, files in K.MERGES:
        p = 'D:/' + k
        ch = sorted(x for x in g(p, 'diff', '--name-only', before, 'main').split(NL) if x.strip())
        peel = g(p, 'rev-parse', '--short=7', tag + '^{commit}').strip()
        out[k] = dict(files=ch, want=sorted(files), tag=peel == merge[:7], docs='COMMENT AND DOCSTRING LINES ALONE True' in rdn('b688_cut_diff_%s.txt' % k))
    return out


def _n5():
    face = jl('b688_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    kw = _kernel_writes()
    kw_ok = all(v['files'] == v['want'] and v['tag'] and v['docs'] for v in kw.values()) and len(kw) == 2
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b688_|audit_b688_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in K.SHARED_APPENDED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b688_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ob = jl('b688_commands.json').get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf = g('D:/SIDE-li-map', 'show', 'main:.github/workflows/build-module.yml').lower()
    wf_ident = [w for w in IDENT if w in wf]
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and kw_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not ident and not wf_ident and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; the kernel mains '
            'written by the act (SIDE-li-map: %s; SIDE-spinor: %s) its workflow and print-list commits, its docstring merges and its tags alone, '
            'the docstring cuts comment and docstring lines alone, each tag peeled to its merge: %s; standing arms added: %s (the act`s arms over '
            'its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS and the regenerated faces page: %s; relay '
            'files of a kind beyond the act`s banks and tools, the table, the root list, b687`s push-out bank and the shared files appended (%s): '
            '%s; "patent" in the lines written: %s; outbound requests other than git %d, an identifier of the author in %s; in SIDE-li-map`s '
            'workflow file: %s' % (
                K.DRAFT, k_ok, ', '.join(kw.get('SIDE-li-map', {}).get('files') or []), ', '.join(kw.get('SIDE-spinor', {}).get('files') or []),
                kw_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', ', '.join(K.SHARED_APPENDED),
                kinds_beyond or 'NONE', pat or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE', wf_ident or 'NONE'))


def _s_scores():
    import collections
    TF, RA_ = jl('b688_table_final.json'), jl('b688_root_arm.json')
    _r, _n, sh = seal_hashes()
    return {
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))
               if TF else 'waits on the final table (relay data/b688_table_final.json)'),
        'S2': (('HELD' if RA_.get('root_recomputed') == RA_.get('root') and RA_.get('root_copy') != RA_.get('root') and not RA_.get('late') else 'REFUTED')
               if RA_ else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally' if RA_
               else 'waits on the root and its arm (relay data/b688_root_arm.json), computed after the entry'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }


def scores(*a):
    """`scores [dry]` writes data/b688_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b688_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('b688_scores_close.json', dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, 'b688_scores.json')):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('b688_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def scores_line(S):
    """the entry's scores line, composed from the scores bank alone (the act arm G-ENTRY-SCORES-EQUAL composes it the same way and compares)."""
    return '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.'


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b688 — lane two, act one hundred and fifteen, the re-cut act under (R298): SIDE-li-map re-cut, R4 re-derived and applied, the '
            'faces line at Q0 regenerated, the lattice-sum route entered on its check')


def _calls():
    return jl('b688_author_answers.json').get('calls') or []


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    """the ferry's form, its figures read from the cut and residue banks: "<document> re-cut: <rows before> rows outside LICENSED/CITED to
    <rows after><, tag>; R4 <applied, v0.1.2 | carried>; the faces line at Q0 <regenerated with P3 derived | held>; the lattice-sum route
    entered on its three-point check"."""
    li, _sp = _distances()
    r4 = 'applied, v0.1.2' if 'R4 APPLIED, v0.1.2' in rdn('b688_residue_actions.txt') else 'carried'
    fc = 'regenerated with P3 derived' if 'PAGE WRITTEN True' in rdn('b688_faces_diff.txt') else 'held'
    tag = ', v0.1.1' if 'MERGED 9e02bc0, v0.1.1' in rdn('b688_cut.txt') else ''
    return ('## SIDE-li-map re-cut: %s rows outside LICENSED/CITED to %s%s; R4 %s; the faces line at Q0 %s; the lattice-sum route entered on '
            'its three-point check' % (li[0] if li else '?', li[1] if li else '?', tag, r4, fc))


def _finding_text():
    """the FINDINGS entry, composed before the root: its scores line from the scores bank alone (data/b686_rules.txt row (1)); the root is
    carried by the trail record."""
    S = jl('b688_scores.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b688_author_answers.txt'), re.M))
    c1 = _rl_lines('b688_record_lines.json') + ['?']
    oc = _rl_lines('b688_orders_lines.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    li, sp = _distances()
    lr = _lattice_reading()
    e = ['', _title(), '',
         'SIDE-li-map’s three docstring rows outside LICENSED/CITED were re-cut by the b670 method to what its two files compile -- the Li map’s '
         'additivity over integer-valued coefficient streams and its positivity on nonnegative ones, with the real Taylor coefficients of log ξ '
         'and von Mangoldt’s Λ(n) ≥ 0 outside the kernel -- the prints equal before and after, merged and tagged v0.1.1; R4’s ACTION, '
         're-derived from its row’s reason, struck “(salt-checked)” from SpinorLeg.lean’s head, SIDE-spinor v0.1.2, the prints again equal; the '
         'faces line on the Li face at Q0 was regenerated by the generator with the local count T-COUNT (P3) derived, not compiled; and the '
         'lattice-sum route b687 added for Z_Q at σ > 2.5 was entered with its steps and sources, its tail bound marked the seat’s own, on its '
         'three-point check against b667’s route.', '',
         '*Filed at b688 on the author’s ruling `(R298)` and the author’s words at its prompts; %d questions put. Banks: relay '
         '`data/b688_lattice_route.txt`, `data/b688_faces_rows.txt`, `data/b688_faces_diff.txt`, `data/b688_naming.txt`, `data/b688_cut.txt`, '
         '`data/b688_residue_actions.txt`, `data/b688_correspondence_dry.txt`.*' % n_ans, '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answers checked before they were acted '
         'on, the two commit cites outside the route’s repositories tested directly. b687 at its weight (FINDINGS :%s), its head line quoted.' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', checks, c1[0]), '',
         '**The lattice-sum route** (`(R298)`(2)): seven steps, three sourced (the function, the box, the range) and four the seat’s own -- the '
         'shell count 8k, the form’s bound Q0 ≥ 0.95 (m² + n²) from its least eigenvalue 3.5 − √6.5, the tail 8 λ^{−σ} N^{2−2σ}/(2σ − 2) at N = '
         '60, its reading across the ball; the check at s = 2.4 + 50i, 2.45 + 149i and 2.5 overlapping b667’s route at each point, %d values '
         'as balls; the six rows of b687’s steps bank that consumed it (:69, :70, :88, :89, :107, :108) marked as resting on the seat’s bound. '
         'A band counted by the argument principle is now priced from b667’s run record before it runs (relay data/b688_rules.txt row (1)).' % (
             lr['balls']), '',
         '**The faces line** (`(R298)`(3)): the generator’s input row (b680’s node list :167) and its successor printed and raised; on the '
         'author’s word the successor kept the name T-COUNT beside P3; the control re-emitted the committed page byte for byte, then '
         '`tools/chain_page.py` wrote the page from the new list, three lines added and three removed.', '',
         '**The re-cut** (`(R298)`(4)): SIDE-li-map named at 3 alone by b652’s order, no tie for b674’s rule; its workflow and print list '
         'committed on main; the runner before (run 39203745715) and after (run 39203874870) both DERIVES, 14 prints equal; the three ACTIONs '
         'verbatim on `recut-li-map-b688`, comment and docstring lines alone; merged at 9e02bc0, tagged v0.1.1 (v0.1, b515e6b, carried no tag); '
         'the distance by the b670 method %s to %s; the pin row appended beneath the licensed table. The Correspondence write held by the '
         'author’s word: its dry run would name 9e02bc0 as carried at lv-conservation v0.7.0, whose source carries 73cee42, so '
         '`W-ORD-CORRESPONDENCE-CARRIED-AT` is entered (OPEN_TRAILS :%s). Two residues of the kernel carried to its next re-cut.' % (
             li[0] if li else '?', li[1] if li else '?', oc[0]), '',
         '**R4** (`(R298)`(5)): the ACTION re-derived from the row’s reason, “No salt-check file exists at the commit”, and SIDE-spinor’s print '
         'bank at v0.1.1; on the author’s word the parenthesis struck on `recut-spinor-b688r`, :18 read and found to make no such claim; run '
         '39206102962 DERIVES, 15 prints equal; merged at 7e570ee, tagged v0.1.2; the distance %s to %s.' % (sp[0] if sp else '?', sp[1] if sp else '?'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b670’s licensed table, b686’s cut of SIDE-spinor and b687’s '
         'lattice route, and is re-read by the next re-cut act, where SIDE-archimedean and SIDE-rcurve stand at 2 and b674’s rule decides, and by '
         'b690, whose reading 3 reads P3’s new status across every line that names T-COUNT. It strengthens the programme’s offering of kernel '
         'docstrings that say only what their files compile, now for SIDE-li-map and SIDE-spinor, each tagged at its cut with its prints equal.', '',
         '**Carried to:** `W-ORD-CORRESPONDENCE-CARRIED-AT` (before any generator run that writes a page, at the latest the next re-cut act); '
         'SIDE-li-map’s two residues (the survey note’s stale quotation, NonnegStream’s instance named by Λ) for its next re-cut; b689 (the '
         'strip-free Li converse, the w = 1 split); the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) “the T-COUNT clause” of (R298)(3) read as the row’s two phrases naming the count as assumed, the first taking the ruling’s '
              'words and the second dropped, before the author’s word kept the name beside P3 (relay data/b688_faces_rows.txt); (2) “the licensed '
              'table’s pin” set by a row appended beneath relay data/b670_licensed_table.txt; (3) the cut’s after figures the seat’s read of the '
              'rows at the tag against their LICENSED readings; (4) SIDE-li-map’s two residues left as they stand, the ACTIONs applied verbatim and '
              'not extended; (5) SpinorLeg.lean :18 read as stating that no salt-check is carried, so no R4b')


def _trail_text():
    S, J = jl('b688_scores.json'), jl('b688_act_root.json')
    fj = jl('b688_findings.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b688_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b688_record_lines.json') + ['?']
    oc = _rl_lines('b688_orders_lines.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R298) ratified.** (1) b687 at its weight. (2) The lattice-sum route. (3) The faces line. (4) The next document. (5) R4. (6) The '
             'branches. (7) The read-first bank. (8) The draft held at v5. (9) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b687’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the order); the faces page regenerated by the '
             'generator (PLACE-papers %s); this record.' % (c1[0], fj.get('entry_line'), oc[0], K.FACES_PAGE_COMMIT), '',
             '**Act root:** b688 `%s` (previous `%s`, b687’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s (relay data/b688_author_answers.txt); none after the root.' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The kernels:** SIDE-li-map v0.1.1 (peeled 9e02bc0; relay data/b688_cut.txt); SIDE-spinor v0.1.2 (peeled 7e570ee; relay '
             'data/b688_residue_actions.txt).', '',
             '**The route:** relay data/b688_lattice_route.txt; the row beneath b687’s plan.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b688_closing.txt).', '',
             '**The open orders:** `W-ORD-CORRESPONDENCE-CARRIED-AT` (before any generator run that writes a page); `W-ORD-EPSTEIN-COUNT-LEAN` (a '
             'research act after b690); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; '
             '`W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b688_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S, C = jl('b688_scores.json'), jl('b688_scores_close.json')
    L = ['=' * 104, 'b688 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s%s' % (
        k2, S[k2][0], S[k2][1], ('  ### AT THE CLOSE: %s -- %s' % (C[k2][0], C[k2][1])) if (S[k2][0] == 'PENDING' and C.get(k2)) else '')
        for k2 in SCORE_KEYS]
    L += [''] + rdn('b688_defects.txt').rstrip(NL).split(NL)
    put_txt('b688_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b688_scores.json', 'b688_findings.json', 'b688_trail.json', 'b688_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b688_record_lines.json') + ['?']
    oc = _rl_lines('b688_orders_lines.json') + ['?']
    L = ['b688 -- THE COMPONENTS, BANKED UNDER (R298).', '',
         '### COMPONENT 0 : the citation check (data/b688_citation_check.txt), step zero (data/b688_ferry.txt, data/b688_readfirst.txt, '
         'data/b688_stepzero.txt, data/b688_tests_stepzero.txt, data/b688_rowgen_stepzero.txt, data/b688_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b687`s weight FINDINGS :%s ; the lattice-sum route (data/b688_lattice_route.txt), committed alone ; N4 %s' % (c1[0], S['N4'][0]),
         '### COMPONENT 2 : the faces rows (data/b688_faces_rows.txt), the author`s word, the page regenerated (data/b688_faces_diff.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : SIDE-li-map (data/b688_naming.txt, data/b688_cut.txt), v0.1.1 ; the Correspondence held (data/b688_correspondence_dry.txt) ; '
         'the order OPEN_TRAILS :%s ; N3 %s' % (oc[0], S['N3'][0]),
         '### COMPONENT 4 : R4 (data/b688_residue_actions.txt), SIDE-spinor v0.1.2 ; the second dry run (data/b688_correspondence_dry_2.txt)',
         '### COMPONENT 5 : the carry-time reading (data/b688_tool_repairs.txt), the dry-run steps (data/b688_reg_gate.txt), the seal '
         '(data/b688_seal_hashes.json), the suite in four parts ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('b688_components.txt', L)
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
    cells_, fired = screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, 'b688_scores.json')):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(FIND, t, e, 'b688_findings.json', dict(title=t))
    j = jl('b688_findings.json')
    j['entry_line'] = ln
    put_json('b688_findings.json', j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b688_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


FACE_REL = 'data/b688_registration_2026-10-19.txt'
FACE = os.path.join(D, 'b688_registration_2026-10-19.txt')


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written -- converted by conv and run through the screens their landing runs, the needles the face names read in
    each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = _face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b688_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b688_regspec.py')], 'b688_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b688_satisfiable.json', '--emit', 'b688'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b688_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b688_census_stepzero.txt'), ('b327_faces_census.py', 'b688_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b688_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b688'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b688_reg_gate.txt', 'data/b688_reg_termscan.txt', 'data/b688_regspec_run.txt', 'data/audit_b688_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b687's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-19-b688'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag',
                        MIRROR_TAG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b688_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b688':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b688`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = _hl.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b688_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b688_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import zipfile
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b688_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b688 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b688 (the last export b687`s, D:/MY-DOwnloads/mirror-refresh-2026-10-19-b687.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b688_mirror.txt', L)
    put_json('b688_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


# ================================================================================ THE CARRY-TIME READING (the ferry's Component 5)
REPAIRS = [
    ('THE DETACHED-RUN READER (answering this act`s defect (e)): the command bank`s detached list (carried from b687) read the command`s text',
     'for Start-Process, nohup or the word run_in_background, and so counted 0 of the act`s two calls sent with the tool`s run_in_background',
     'parameter; and read inside quoted strings it took the seat`s own search for that word as a third. b688`s reading, in the shared writer',
     '(tools/b688_record.py `capture`, `_bg_calls`, `commands`): every captured row carries the call`s parameter as `bg`; the detached list',
     'is the rows with `bg` or the words read outside quoted strings. The bank prints DETACHED RUNS 2 (#32, #68). No arm reads the list; the',
     'defect is entered, not declared on the face.'),
    ('THE STANDING SET FOR b688 (answering no defect: the act`s objects): the standing arms are b687`s face`s (G2) arms less b687`s act arms, the',
     'twenty rule arms among them, no standing arm added; the runner arms read this act`s runs -- SIDE-li-map before (39203745715) and after',
     '(39203874870), SIDE-spinor after (39206102962) with b686`s after bank at v0.1.1 as its before -- and its merges, 9e02bc0 v0.1.1 and',
     '7e570ee v0.1.2; the step-zero arms read this act`s banks -- five branches, all local.'),
    ('G-WORKFLOW-FILES READ IN EACH KERNEL`S OWN FORM (answering no defect: a kernel of another dependency form): b687`s predicate wanted',
     '`lake env lean out/axioms.lean` and a 15-name list of SIDE-spinor`s alone; SIDE-li-map has no lakefile, and its workflow (7d20a4c) runs',
     'the plain-lean path of SIDE-global-section`s, `LEAN_PATH=build lean out/Axioms.lean`. b688`s predicate reads every kernel the act',
     'merged, each against its own form (the lake path where a lakefile requires Mathlib, the plain path where there is no lakefile), its',
     'print list`s length against the act`s print bank for that kernel, and the files the act wrote on main against MERGES. The diff is',
     'printed whole below.'),
    ('THE FACES PAGE AND G-PP-SCOPE, G-CURRENTS-UNEDITED (answering no defect: the ruling writes the page): (R298)(3) and the author`s word',
     'regenerate THE_CLAUSE_AND_ITS_COMPILED_FACES.md through the generator, so the page leaves CURRENTS (the files read unedited) and joins',
     'the PLACE-papers files G-PP-SCOPE allows (tools/b688_worklist.py PP_WRITTEN); G-FACES-REGENERATED reads the page`s write by the',
     'generator. The diff is printed whole below.'),
]


def _fn_src(src, name):
    """a top-level function's source, from its `def` line to the next top-level line; '' where the tool carries no such function."""
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def _const_src(src, name):
    m = re.search(r'(?ms)^%s = .*?(?=^\S)' % re.escape(name), src)
    return m.group(0) if m else ''


def repairs(*a):
    """data/b688_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b687 copy is read against
    b687's seal hash (relay data/b687_seal_hashes.json) first, and its diff against that copy counted by hunks (NOT YET CARRIED where the
    act has not written it); tools/rule_arms.py and tools/edit_route.py read against the last seal record naming them (unedited in this act);
    the repaired readings' diffs against b687's sealed copies printed whole."""
    import difflib
    import hashlib
    seal = jl('b687_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b687_citation.py', 'b687_closing.py', 'b687_reg_gate.py', 'b687_regspec.py', 'b687_tests.py', 'b687_worklist.py',
               'b687_record.py', 'b687_checks.py'):
        t1 = t0.replace('b687_', 'b688_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        ex = os.path.exists(new)
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout if ex else ''
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:]), ex))
    inst = {}
    for t in ('rule_arms.py', 'edit_route.py'):
        nowh = hashlib.sha256(open(os.path.join(T, t), 'rb').read()).hexdigest()
        acts = [x for x in ('b687', 'b686', 'b685', 'b684', 'b683', 'b682', 'b681') if (jl('%s_seal_hashes.json' % x).get('tools') or {}).get(t)]
        inst[t] = (nowh, acts[0] if acts else None, (jl('%s_seal_hashes.json' % acts[0])['tools'][t]) if acts else None,
                   g(ROOT, 'log', '-1', '--format=%h %cI', '--', 'tools/' + t).strip())
    s7r, s8r = rd(os.path.join(T, 'b687_record.py')), rd(os.path.join(T, 'b688_record.py'))
    s7c, s8c = rd(os.path.join(T, 'b687_checks.py')), rd(os.path.join(T, 'b688_checks.py'))
    nd = []
    for (a7, f7), (a8, f8), s7, s8 in ((('b687_record.py', 'capture'), ('b688_record.py', 'capture'), s7r, s8r),
                                       (('b687_record.py', '(none)'), ('b688_record.py', '_bg_calls'), s7r, s8r),
                                       (('b687_record.py', 'commands'), ('b688_record.py', 'commands'), s7r, s8r),
                                       (('b687_checks.py', 'wf_state'), ('b688_checks.py', 'wf_state'), s7c, s8c),
                                       (('b687_checks.py', 'wf_ok'), ('b688_checks.py', 'wf_ok'), s7c, s8c),
                                       (('b687_checks.py', 'corpus_scope'), ('b688_checks.py', 'corpus_scope'), s7c, s8c)):
        nd += list(difflib.unified_diff(_fn_src(s7, f7).split(NL) if f7 != '(none)' else [], _fn_src(s8, f8).split(NL) if s8 else [],
                                        '%s %s (sealed)' % (a7, f7), '%s %s%s' % (a8, f8, '' if s8 else ' (NOT YET CARRIED)'), n=1, lineterm=''))
    nd += list(difflib.unified_diff(_const_src(s7c, 'CURRENTS').split(NL), _const_src(s8c, 'CURRENTS').split(NL), 'b687_checks.py CURRENTS (sealed)',
                                    'b688_checks.py CURRENTS', n=1, lineterm=''))
    L = ['b688 -- COMPONENT 5, (R298)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b687`S SEALED COPIES (%s)' % utc(), '',
         '### rows are repairs with the defect they answer, after the carried tools: b687`s sealed copy and its seal record; the hunks of the diff',
         '### to b688`s copy. Every hunk is the act`s own text -- its names, its banks, its sections and its predicates over this act`s banks --',
         '### save the repairs below.', '']
    for t0, t1, now, s, nh, ex in rows:
        L.append('  %-20s -> %-20s b687 sealed %s ; the seal`s record %s ; %s ; hunks %s' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh if ex else 'NOT YET CARRIED'))
    for t, (nowh, act, sh, last) in inst.items():
        clean = grc(ROOT, 'diff', '--quiet', 'HEAD', '--', 'tools/' + t) == 0 and grc(ROOT, 'merge-base', '--is-ancestor', last.split()[0], K.PRE_RELAY) == 0
        if sh is None:      # ### no seal record names it: unedited read as the working file equal to HEAD, its last commit before the act
            inst[t] = (nowh, act, nowh if clean else None, last)
        L.append('  %-20s    the standing instrument, unedited in this act: %s ; the last seal record naming it (%s`s) %s ; %s ; its last commit %s%s' % (
            t, nowh[:16], act or 'NONE', (sh or '### NONE')[:16], 'AGREE' if inst[t][2] == nowh else '### DIFFER', last,
            (' ; read by the tree: the working file equal to HEAD and its last commit before the act %s' % clean) if sh is None else ''))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### THE DIFF OF THE REPAIRED READINGS AGAINST b687`S SEALED COPIES (tools/b687_record.py sha256 %s, tools/b687_checks.py sha256 %s), '
          'WHOLE:' % ((seal.get('b687_record.py') or '### NONE')[:16], (seal.get('b687_checks.py') or '### NONE')[:16])]
    L += ['    ' + l for l in nd]
    carried = sum(1 for r in rows if r[5])
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d OF %d ; THE REPAIRED READINGS` DIFF LINES %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n, _e in rows) and all(v[0] == v[2] for v in inst.values()) else '### DIFFER',
        carried, len(rows), len(nd))]
    put_txt('b688_tool_repairs.txt', L)
    print(L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, order=order, faces=faces, naming=naming, runner=runner, prints=prints, cutdiff=cutdiff,
              answers=answers, commands=commands, defects=defects, repairs=repairs, kernels=kernels, rootbanks=rootbanks, root=root,
              root_arm=root_arm, table_final=table_final, scores=scores, desk=desk, components=components, findings=findings, trail=trail,
              drycheck=drycheck, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, mbank=mbank)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b688_record.py %s [dry]' % ' | '.join(ROUTES))
        sys.exit(2)
    fn(*sys.argv[2:])
