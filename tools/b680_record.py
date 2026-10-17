# -*- coding: utf-8 -*-
"""b680_record.py -- THE ACT'S RECORD TOOL, b680 under (R290).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b680's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b679_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes, the
### answers bank with b679's word reader); the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b680_record.py <route> [dry]`.
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
import b680_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b679_record.py with b680's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b680_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b680_findings.json': dict(entry_line=99999, title='stand-in'),
        'b680_trail.json': dict(line=99999),
        'b680_act_root.json': dict(root='0' * 64, previous='5046df1d' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b680's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b680_scanfile_%s.md' % tag)
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
    """a row of data/b680_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b680_rowgen_<stage>.txt, the stage
    `stepzero` or, by argument, another name (the ledger split's before and after)."""
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
    L = ['b680 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b680_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R290)(8))
def branches(*a):
    """every branch (R290)(8) names, its tip read before any delete, its fate; the one remote deletion the ruling names (SIDE-explicit-
    formula's strip-variant-b679) read at the remote by one ls-remote and its tip printed as an ancestor of main 95f8dc8 or not; any branch
    under the push-b679 prefix that --merged lists and the ruling does not name, reported and KEPT. data/b680_branches.txt (.json)."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        out = g(repo, 'ls-remote', 'origin', 'refs/heads/' + b).split()
        tip = out[0] if out else ''
        anc = subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', tip, K.K_MAIN], capture_output=True).returncode == 0 if tip else False
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=anc, fate='DELETED'))
    named = set((r['repo'], r['branch']) for r in rows)
    extra = []
    for repo, _bs in K.DELETE:
        for x in g(repo, 'branch', '--merged', 'main', '--format=%(refname:short)').split(NL):
            x = x.strip()
            if x.startswith('push-b679') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b680 -- STEP ZERO, (R290)(8): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; for a local row listed by `git branch --merged main --list <name>`,',
         '### for the remote row its tip an ancestor of main %s by `git merge-base --is-ancestor` ; fate. Deleted by name in the house form, each' % K.K_MAIN,
         '### delete command naming one branch with no glob in any half, one command per call, in sequence; no branch the ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; %s %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'],
                                                  'merged into main' if r['where'] == 'local' else 'ancestor of main %s' % K.K_MAIN, r['merged'],
                                                  r['fate']) for r in rows]
    L += ['', '### branches under the push-b679 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED OR ANCESTOR %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b680_branches.txt', L)
    put_json('b680_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE FACES LINE, (R290)(2) AND THE AUTHOR'S WORD
FACES = os.path.join(PP, K.FACES_PAGE)
LANDING679 = os.path.join(D, 'b679_landing.txt')
REPAIRS_ROW = ('### Appended 2026-10-17 by b680 under (R290)(2) and the author`s word (write through the generator; relay data/b680_author_answers.txt): '
               'the draft above written to THE_CLAUSE_AND_ITS_COMPILED_FACES.md through relay tools/chain_page.py`s backmatter channel from relay '
               'data/b680_nodes_zeta.txt, its content unchanged and its form repaired three ways: (i) the possessives and the prime written with straight '
               'characters, no backtick in the row; (ii) "lies on the line" read "has every zero on the line"; (iii) "(v0.33)" read '
               '"(SIDE-explicit-formula v0.33)". The diff banked at relay data/b680_faces_diff.txt.')


def faces(*a):
    """(R290)(2): the control (b674's list re-emits the committed page byte for byte from b643's banked probe output), then b680's list
    emitted to the scratchpad and diffed against the committed page, then -- not dry -- written to the page by the generator and read back
    equal to the scratch emission; the landing bank of b679 gains one row beneath the draft (additive, (R254)(2)). data/b680_faces_diff.txt."""
    import difflib
    dry = 'dry' in a
    probe = os.path.join(D, 'b643_probe_out_zeta.txt')

    def emit(nodes, out):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', nodes, '--probe-dir', SP, '--out', out,
                            '--from-output', probe], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.returncode
    before = open(FACES, 'rb').read()
    ctl_p, new_p = os.path.join(SP, 'b680_faces_control.md'), os.path.join(SP, 'b680_faces_new.md')
    rc1 = emit(os.path.join(D, 'b674_nodes_zeta.txt'), ctl_p)
    rc2 = emit(os.path.join(D, 'b680_nodes_zeta.txt'), new_p)
    ctl, new = open(ctl_p, 'rb').read(), open(new_p, 'rb').read()
    d = list(difflib.unified_diff(before.decode('utf-8').split(NL), new.decode('utf-8').split(NL), 'committed', 'b680', lineterm='', n=0))
    plus = [l for l in d if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d if l.startswith('-') and not l.startswith('---')]
    import chain_page as CP
    rec = [x for x in CP.backmatter_of(os.path.join(D, 'b680_nodes_zeta.txt')) if 'b680' in x][-1]
    ok = rc1 == 0 and rc2 == 0 and ctl == before and len(plus) >= 1 and '`' not in rec and 'T-COUNT named' in rec \
        and rec in new.decode('utf-8') and rec not in before.decode('utf-8') and all(rec in l for l in plus if 'Li face over the widened class' in l)
    written = False
    if not dry and ok:
        rc3 = emit(os.path.join(D, 'b680_nodes_zeta.txt'), FACES)
        written = rc3 == 0 and open(FACES, 'rb').read() == new
        old = open(LANDING679, 'rb').read()
        if REPAIRS_ROW.encode('utf-8') not in old:
            sep = b'\n' if old.endswith(b'\n') else b'\n\n'
            add = (sep + b'\n' + REPAIRS_ROW.encode('utf-8') + b'\n')
            open(LANDING679 + '.tmp', 'wb').write(old + add)
            os.replace(LANDING679 + '.tmp', LANDING679)
    L = ['b680 -- COMPONENT 1, (R290)(2): THE FACES LINE THROUGH THE GENERATOR, ON THE AUTHOR`S WORD (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py --from-output relay data/b643_probe_out_zeta.txt (no elaboration; no lean on this host)',
         '### the control: b674`s list (relay data/b674_nodes_zeta.txt) re-emits the committed page byte for byte: %s (%d bytes)' % (ctl == before, len(before)),
         '### the new list: relay data/b680_nodes_zeta.txt (b674`s 165 lines unchanged, one backmatter record added); emitted %d bytes, exit %d' % (len(new), rc2),
         '### the diff, committed page -> b680 emission (lines added %d, removed %d):' % (len(plus), len(minus))] + ['    ' + l for l in d] + [
         '', '### the page written by the generator and read back equal to the emission: %s ; the landing bank`s row beneath the draft: %s' % (
             written if not dry else 'DRY', 'appended' if (not dry and ok) else 'DRY'),
         '', '### ### **CONTROL EQUAL %s ; LINES ADDED %d ; REMOVED %d ; THE ROW CARRIES T-COUNT AND NO BACKTICK %s ; PAGE WRITTEN %s.**' % (
             ctl == before, len(plus), len(minus), ok, written)]
    if dry:
        print(NL.join(L[3:]))
        return
    put_txt('b680_faces_diff.txt', L)
    print(NL.join(L[-3:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R290)(1) AND (3)
WH = ('*Appended 2026-10-17 by b680 to b679’s entry (:9050), under `(R290)`(1) -- b679 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b679_closing.txt):*')
WB = (' “b679 closed: relay 6b2a8f78, PLACE-papers 3e375cb, SIDE-explicit-formula 95f8dc8 v0.33; suite 89 of 89; root 5046df1d1fc69df6…; '
      '3 prompts answered; 5 defects” (data/b679_closing.txt :1), the closing pushed at relay f507c3f7 (data/b679_closing_push_out.txt :4). '
      'The readings as the banks print them: WideConfig with the open strip (−1/2, 3/2) and HExcl, every real point of the carrier of positive '
      'real part; V5’, the composition’ and Wide.li_nonneg_cfg_imp_online DERIVES, 49 printed names at the standard three, the 29 v0.32 prints '
      'equal (data/b679_landing.txt, data/b679_prints_compare.txt); C2 fails HExcl and S5’ does not apply to it, C2b has every Li coefficient '
      'nonnegative with 1 off the line, the exclusion of 0 necessary; Q0 meets the widened class with T-COUNT assumed, HExcl read on [−1/2, −1/4] '
      'by the functional equation’s form and on [−1/4, 0] by b667’s route, 35 balls negative, Z_Q(0) = −1 (data/b679_q0_membership.txt); '
      'n*’ = 63676, equal to b675’s n*, the wider strip changing no constant of the bound, n_obs = 10034 below it, 94 of 94 n on V4’s '
      'subsequence in the window NEG (data/b679_onset.txt); the mirror mirror-refresh-2026-10-17-b679.zip CLEAN with the root line; N1–N5 and '
      'S1–S3 HELD. Five defects (a)–(e), (a)–(c) the navigator’s, (d) a cp and (e) a short name shared with ζ’s summability that sent the walk '
      'to 22 ζ-naming declarations before the rename, 0 of 278 after (data/b679_defects.txt). The root module’s import list left unedited, '
      'accepted; the split at w = 1 entered as a later act’s candidate, accepted. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b680_record_lines.json', 'c1', entry=K.B679_ENTRY,
         check=[('FINDINGS.md', K.B679_ENTRY, '## The Li converse over the strip'), ('OPEN_TRAILS.md', K.B679_TRAIL, '### b679')], dry=dry)


ORDERS = 'b670_work_orders.txt'
ORDER = 'W-ORD-EPSTEIN-COUNT'
OH = ('*Appended 2026-10-17 by b680 beneath b679’s trail record (:14650), under `(R290)`(3) -- THE ORDER `W-ORD-EPSTEIN-COUNT` ENTERED, '
      'THE COUNT LAW FOR Z_Q:*')
OB = (' T-COUNT -- HCount at Q0, the kernel’s premise P3 (relay data/b675_hypotheses.txt :61, :67; Schema/EpsteinQ0.lean :104-:108) -- is the '
      'one assumption left under the Q0 test of b679. Two routes, priced and neither begun. (i) A located explicit zero-counting bound for Z_Q, '
      'searched under the names the literature uses for Dedekind zeta functions and Hecke L-functions of class-group characters (Z_Q for the '
      'principal form at D = −23, h = 3, a combination of such L-functions); each candidate entered as LOCATED with its statement and constant '
      'or NOT LOCATED, no result recalled. Its price: one research act`s reading -- the queries, each candidate`s statement read at its source, '
      'and the constant carried to A₀ against the kernel`s A0Q = 10; a located bound discharges T-COUNT at every height. (ii) A certification by '
      'the argument principle on the certified region extended upward under the (3c) bound, priced in b667`s units: b667 counted R = [−0.5, 1.5] '
      '× [0.5, 150] in 1042 segments (N(R) = 180, relay data/b667_epstein_counts.txt :49-:52), each Z_Q value taking M terms, M a fixed part plus a part '
      'linear in the height (tools/b667_epstein_certify.py :106-:107, M_of); a count to height T needs segments growing about as T log T against '
      'b667`s 150 log 150, each segment`s values costing more in proportion to M at that height; it certifies the count only up to T, never for every t -- so (ii) narrows T-COUNT to t > T and does not discharge it alone. '
      'Trigger: after b681. Status OPEN. Its row in relay data/b670_work_orders.txt, appended additively.')


def c1order(*a):
    """(R290)(3): the order on OPEN_TRAILS beneath b679's trail record, then its row appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b680_record_lines_order.json', 'c1order',
         check=[('OPEN_TRAILS.md', K.B679_TRAIL, '### b679')], dry=dry)
    if dry:
        return
    ol = jl('b680_record_lines_order.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-17 by b680 under (R290)(3) (additive, (R254)(2)): W-ORD-EPSTEIN-COUNT entered, its Status cell filled and its '
            'line its pin, both routes priced on its line.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % (ORDER, ol, 'b680', 0, 'OPEN', ol, 'after b681', ol)]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after): %s' % (ORDERS, len(old), len(new), rows[1].strip()[:120]))


ROUTES = {'rowgen': rowgen, 'branches': branches, 'faces': faces, 'c1': c1, 'c1order': c1order}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b680_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
