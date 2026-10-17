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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c2': c2}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b678_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
