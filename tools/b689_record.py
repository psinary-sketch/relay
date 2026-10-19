# -*- coding: utf-8 -*-
"""b689_record.py -- THE ACT'S RECORD TOOL, b689 under (R299).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b689's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b688_record.py in stages: the helpers, the guarded landing, the readers, step zero's rowgen and branches
### routes and Component 1's weight line and arm reading first; the plan, runner and build routes at Components 2-4; the late routes at
### Component 5. Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b689_record.py
### <route> [dry]`.
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
import b689_worklist as K          # noqa: E402

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
        'b689_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b689_findings.json': dict(entry_line=99999, title='stand-in'),
        'b689_trail.json': dict(line=99999),
        'b689_act_root.json': dict(root='0' * 64, previous='f168527e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b689's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b689_scanfile_%s.md' % tag)
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
    """a row of data/b689_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
    BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES or r.get('where') not in ('local', 'remote'):
        raise ValueError('branch row of another shape: %r' % (r,))
    return r['branch'], r['fate']


def read_runner_row(r):
    """a row of data/b689_runner_rows.json: the kernel, its label, the ref (40 hex), the run id and the gate; returns (kernel, label, gate)."""
    if not isinstance(r, dict) or not re.match(r'^SIDE-[\w-]+$', r.get('kernel') or '') or not re.match(r'^[\w-]+$', r.get('label') or '') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['kernel'], r['label'], r['gate']


def read_use_row(r):
    """a row of data/b689_plan.json's uses: the strip-uses bank's line (9-30), its file :line, the class (one of USE_CLASSES) and the reason;
    returns (row, class)."""
    if not isinstance(r, dict) or not isinstance(r.get('row'), int) or not 9 <= r['row'] <= 30 or not re.match(r'^Li\w+\.lean :\d+$', r.get('at') or '') \
            or r.get('cls') not in USE_CLASSES or not (r.get('why') or '').strip():
        raise ValueError('use row of another shape: %r' % (r,))
    return r['row'], r['cls']


USE_CLASSES = ('DISCHARGED', 'RE-PROVED', 'OBSTRUCTED')
READERS = ['read_score_row', 'read_head', 'read_branch_row', 'read_runner_row', 'read_use_row']


# ================================================================================ STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE (b670's route, carried)
def roster():
    """the 19 roster tables of data/b586_corroboration.txt :34, at the paths that bank read (carried from b670_record.py :548-:552)."""
    L = rdn('b586_corroboration.txt').split(NL)
    names = [x.strip(" '") for x in L[33].split(': ', 1)[1].strip('[]').split(',')]
    rows = dict((l.split('|')[1].strip(), l.split('|')[2].strip()) for l in L if l.startswith('| ') and not l.startswith('| document'))
    return [(n, rows[n]) for n in names]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b689_rowgen_<stage>.txt."""
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
    L = ['b689 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b689_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R299)(6))
def branches(*a):
    """every branch (R299)(6) names, its tip read before any delete, its fate; any branch under the push-b688 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b689_branches.txt (.json)."""
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
            if (x.startswith('push-b688') or x.endswith('-b688') or x.endswith('-b688r')) and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b689 -- STEP ZERO, (R299)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per message, in sequence; no branch',
         '### the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches of b688 that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED OF b688 %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b689_branches.txt', L)
    put_json('b689_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R299)(1)
WH = ('*Appended 2026-10-19 by b689 to b688’s entry (:9314), under `(R299)`(1) -- b688 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b688_closing.txt), ITS DEFECT (f) REPAIRED BY A GENERATED CORRIGENDUM ENTRY:*')
WB = (' “b688 closed: relay 4bee98dc, PLACE-papers c3af808; suite 116 of 117; root f168527e8655305c…; 4 prompts answered; 6 defects” '
      '(data/b688_closing.txt :1), the closing pushed and read back at relay 007d4ead (data/b688_closing_push_out.txt). SIDE-li-map’s three '
      'docstring rows outside LICENSED/CITED went to 0, comment and docstring lines alone, both builds on the hosted runner, 14 prints equal '
      'before and after (data/b688_prints_SIDE-li-map.txt), merged at 9e02bc0 and tagged v0.1.1, with b515e6b named as v0.1 carrying no tag '
      'and the pin row beneath the licensed table (data/b670_licensed_table.txt :285); two SIDE-li-map residues carried -- '
      'PrimeLedgerPositivity.lean :29-:31 quoting a removed line of LiLinearMap.lean, and NonnegStream’s docstring :51-:54 naming the real-valued '
      'Λ as an instance of an integer stream (data/b688_cut.txt). The Correspondence cells held on the author’s word, '
      '`W-ORD-CORRESPONDENCE-CARRIED-AT` at OPEN_TRAILS :14922, both dry runs banked. R4 applied: “(salt-checked)” struck at SpinorLeg.lean :21 '
      'and nothing else, :18 making no such claim, so no R4b; 15 prints equal (data/b688_prints_SIDE-spinor.txt), merged at 7e570ee, tagged '
      'v0.1.2. The faces line regenerated with the amendment “the local count T-COUNT (P3) derived ..., not compiled” after the control '
      're-emitted the old page byte for byte. The lattice-sum route entered with seven steps, its tail bound marked as the seat’s own, the '
      'three-point check against b667’s route overlapping at all three, the six consuming rows of b687’s steps bank named '
      '(data/b688_lattice_route.txt). Suite 116 of 117 pre-push and post-push, G-RULE-HEAD-LINE-QUOTED declared by name -- the quote correct by '
      'the citation check’s row, the arm matching one unbroken string against a quote pasted over three lines; all eight scores HELD; root '
      'f168527e over 61 banks; mirror-refresh-2026-10-19-b688.zip CLEAN with the root line; the eight sealed tools’ hashes matching at the close. '
      'Six defects, every one the seat’s (data/b688_defects.txt): (a) the piped push of recut-li-map-b688; (b) a commit message calling the print '
      'bank absent where the bank says present; (c) a duplicated section of the citation bank, fixed before commit; (d) a prompt mixing the '
      'file’s line numbers with the generator’s; (e) two waits backgrounded, the command bank’s reader repaired; (f) the entry at :9314 '
      'saying two commit cites were tested directly (its citation sentence, :9320) where the citation bank tests three, found after the seal -- '
      'repaired at b689 by the generated corrigendum entry that follows, the sealed entry itself unedited. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b689_record_lines.json', 'c1', entry=K.B688_ENTRY,
         check=[('FINDINGS.md', K.B688_ENTRY, '## SIDE-li-map re-cut'), ('OPEN_TRAILS.md', K.B688_TRAIL, '### b688')], dry=dry)


# ================================================================================ COMPONENT 1: THE ARM'S READING AT HEAD, (R299)(2)
def _arm_inputs(act):
    """rule_arms.sources' two inputs for G-RULE-HEAD-LINE-QUOTED, read the way rule_arms.py :228-:229 reads them: the act's ferry bank and the
    previous act's closing :1."""
    n = int(act[1:])
    return dict(ferry=rdn('%s_ferry.txt' % act), prev_head=(rdn('b%d_closing.txt' % (n - 1)).split(NL) or [''])[0])


def armread(*a):
    """the arm G-RULE-HEAD-LINE-QUOTED read through tools/rule_arms.py's own `reading` at HEAD (the shared tool imported, not copied) against
    b688's ferry bank and this act's; then its planted case (rule_arms.py :466-:467) over each, which must fail. Prints only, unless `bank`:
    then the reading is appended to data/b689_tool_repairs.txt's ARM READING section by the Edit tool's hand, not here -- this route writes
    nothing."""
    import rule_arms as RA
    out = []
    for act in ('b688', 'b689'):
        R = _arm_inputs(act)
        ok, n, bad, how = RA.reading('G-RULE-HEAD-LINE-QUOTED', R)
        Rp = dict(R, prev_head=R['prev_head'] + ' planted')
        pok, _pn, pbad, _ph = RA.reading('G-RULE-HEAD-LINE-QUOTED', Rp)
        out.append((act, ok, n, bad, how, pok))
        print('  %s : the arm %s (count %d, failing %d) -- %s ; the planted case %s' % (act, 'PASSES' if ok else 'FAILS', n, bad, how,
                                                                                    'FIRES' if not pok else 'DOES NOT FIRE'))
    print('### ### **THE ARM AT HEAD: b688 %s ; b689 %s ; THE PLANTED CASE FIRES ON BOTH %s.**' % (
        'OK' if out[0][1] else 'FAILS', 'OK' if out[1][1] else 'FAILS', all(not x[5] for x in out)))


ROUTES = dict(rowgen=rowgen, branches=branches, c1=c1, armread=armread)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b689_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
