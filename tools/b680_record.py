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
import collections
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


ORDER4 = 'W-ORD-LEDGER-SPLIT-RESOLVER'
OH4 = ('*Appended 2026-10-17 by b680 beneath its order `W-ORD-EPSTEIN-COUNT` (:14678), under `(R290)`(6) and the navigator’s answer on '
       'archive-3 -- THE ORDER `W-ORD-LEDGER-SPLIT-RESOLVER` ENTERED, THE LEDGER SPLIT HELD:*')
OB4 = (' the proposed cut FINDINGS :456-:6949 (the record stream through the last entry filed before b600; the reference frames stay) moves the '
       'line cited by 4565 of 4635 FINDINGS :NNNN citation sites (banks 3670, corrigendum 166, ledgers 553, papers 155, roster 21; relay '
       'data/b680_split_price.txt), and no house tool re-pins a line citation; so archive-3 is HELD and the count is the finding. The 23 anchor '
       'citations (FINDINGS#name) are the form that survives a cut unaided, as the 2026-08-24 split kept them. A re-pin tool is struck as a route: '
       'it would rewrite banks that sit under act roots and sealed hashes. The route entered and priced: at the moment of any future cut, a banked '
       'line-offset table, one row -- the cut’s range and the offset it induces -- and a resolver that rowgen, the citation check and the '
       'Correspondence generator consult when they read a FINDINGS :NNNN citation older than the cut; no bank, ledger or paper rewritten. Its '
       'price: one table row written with the cut, one resolver function, and its call added in those three readers. Trigger: on the author’s '
       'word, when FINDINGS’ size asks for it. Status OPEN. Its row in relay data/b670_work_orders.txt, appended additively.')


def c4order(*a):
    """(R290)(6) and the navigator's answer on archive-3: the order on OPEN_TRAILS beneath b680's first order, then its row appended to the
    orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', OH4, NL + OH4 + OB4 + NL)], 'b680_record_lines_order4.json', 'c4order',
         check=[('OPEN_TRAILS.md', 14678, '*Appended 2026-10-17 by b680 beneath b679')], dry=dry)
    if dry:
        return
    ol = jl('b680_record_lines_order4.json')['lines'][0]['line']
    rows = ['### Appended 2026-10-17 by b680 under (R290)(6) and the navigator`s answer on archive-3 (additive, (R254)(2)): W-ORD-LEDGER-SPLIT-RESOLVER '
            'entered, its Status cell filled and its line its pin, its route priced on its line.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % (ORDER4, ol, 'b680', 0, 'OPEN', ol, 'on the author`s word', ol)]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after): %s' % (ORDERS, len(old), len(new), rows[1].strip()[:120]))


# ================================================================================ COMPONENT 3: THE ARMS AND THE RULES, (R290)(5)
VALUE_ARMS = {   # ### an arm reading an object's state -- a hash, a blob id, a remote SHA, a print line, a commit, a tree, a live kernel; every other
    # ### standing arm reads a bank's form, presence or text (SHAPE). Each entry read by hand against the arm's `reads` field.
    'G-PUSHOUT-COMMITTED': 'the step-zero commit`s files and ancestry (git objects)',
    'G-BRANCHES-DELETED': 'the repositories` branch refs, local and remote-tracking',
    'G-LOCAL-BANK-UNTRACKED': 'the git index and log for one path',
    'G-EXPORT-UNTRACKED': 'the git index and log for one path',
    'G-WORKFLOW-FILES': 'the kernel`s main blobs (the workflow before and now, the print list)',
    'G-RUNNER-READ': 'the run`s row: the artifact`s sha256 and the memory low',
    'G-RUNNER-GATE': 'the run`s axioms print lines and the artifact`s digest',
    'G-MERGES-ON-GATE': 'the kernel`s main commit, its parents, the trees and the tag`s peel',
    'G-NO-SORRY-MAIN': 'every kernel`s code at HEAD and its remote',
    'G-AXIOM-CLAIM': 'every kernel`s claims against the banked print lines',
    'G-MODULE-HEADER': 'every kernel`s module headers at HEAD',
    'G-PP-SCOPE': 'PLACE-papers` changed files by git diff',
    'G-CURRENTS-UNEDITED': 'the currents` bytes: working tree, before and HEAD',
    'G-KERNELS-UNTOUCHED': 'every kernel`s main, tags, branches and status',
    'G-INSTRUMENTS-UNEDITED': 'the instruments` bytes: before, working tree and HEAD',
    'G-SHARED-ADDITIVE': 'the shared files` bytes before and now',
    'G-PRIORBANK-UNCHANGED': 'every prior bank`s blob id',
    'G-FINDINGS-APPEND-ONLY': 'FINDINGS` bytes before and now',
    'G-TRAIL-APPEND-ONLY': 'OPEN_TRAILS` bytes before and now',
    'G-SEALED-AFTER-COMPONENTS': 'the commits` times against the lock`s',
    'G-NOTHING-RAN-AHEAD': 'the commits` hashes before the lock',
    'G-SEAL-VERIFIES': 'the face`s sha256 by reg_seal',
    'G-SEAL-HASHES': 'the sealed tools` sha256 now',
    'G-ACTROOT-BANKED': 'the root recomputed from its items',
    'G-ACTROOT-LAST': 'the named banks` write times',
    'G-ACTROOT-VERIFY': 'the chain recomputed at commit with remote reads',
    'G-WRITELIST-KINDS': 'the tracked files written, by git diff',
    'G-ARTEFACTS-NOT-COMMITTED': 'relay`s tracked files',
    'G-LSREMOTE-ONE-PER-REPO': 'the run`s remote calls, counted',
}


def arms(*a):
    """(R290)(5)(i): the census of the sealed suite's standing arms (tools/b679_checks.py STANDING, :311; each arm's `reads` field) by what each
    reads, SHAPE or VALUE; every standing arm once. data/b680_arms.txt (.json)."""
    import importlib
    sys.argv = sys.argv[:1]
    C = importlib.import_module('b679_checks')
    st = list(C.STANDING)
    reads = dict((x[0], x[1]) for x in C.ARMS)
    rows = [(n, 'VALUE' if n in VALUE_ARMS else 'SHAPE', reads.get(n, '### NOT IN THE SUITE'), VALUE_ARMS.get(n, '')) for n in st]
    nv = sum(1 for r in rows if r[1] == 'VALUE')
    L = ['b680 -- COMPONENT 3, (R290)(5)(i): THE STANDING ARMS BY WHAT EACH READS (%s)' % utc(), '',
         '### rows are the sealed suite`s standing arms (tools/b679_checks.py :311, STANDING = b678`s face`s (G2) arms less b678`s act arms), each',
         '### once: its kind -- SHAPE (a bank`s form, presence or text) or VALUE (an object`s state: a hash, a blob id, a remote SHA, a print line, a',
         '### commit, a tree, a live kernel) -- and the bank or object it reads (its `reads` field, the suite`s own words).', '']
    L += ['  %-34s %-5s %s%s' % (n, k, r[:150], ('  [the object: %s]' % v) if v else '') for n, k, r, v in rows]
    L += ['', '### ### **STANDING ARMS %d ; SHAPE %d ; VALUE %d ; EACH ONCE %s.**' % (len(rows), len(rows) - nv, nv, len(set(st)) == len(st))]
    put_txt('b680_arms.txt', L)
    put_json('b680_arms.json', dict(at=utc(), rows=[dict(arm=n, kind=k, reads=r, obj=v) for n, k, r, v in rows], shape=len(rows) - nv, value=nv))
    print(L[-1])


def rulesarms(*a):
    """(R290)(5)(ii): every rule row across the rules banks that exist, once, with its act, its text and the standing arm that enforces it or
    NONE, from the generated index (tools/b680_rules_index.py, committed alone); the NONE rows listed for the author. data/b680_rules_arms.txt."""
    import b680_rules_index as RI
    R = RI.rows()
    seen = set()
    for r in R:
        k = (r['act'], r['row'])
        if k in seen:
            sys.exit('### A RULE ROW TWICE: %s -- NOTHING WRITTEN' % (k,))
        seen.add(k)
    none = [r for r in R if r['arm'] == 'NONE']
    L = ['b680 -- COMPONENT 3, (R290)(5)(ii): THE RULES AND THE STANDING ARMS THAT ENFORCE THEM (%s)' % utc(), '',
         '### rows are rules: act ; row ; bank :line ; its head ; the standing arm or NONE. The rows from tools/b680_rules_index.py (committed alone,',
         '### its output data/b680_rules_index.txt); the banks read: those that exist (b676 and b679 banked no rules file -- the author`s answer at',
         '### step zero, data/b680_defects.txt (a)). No arm is added in this act.', '']
    L += ['  %-5s row %-2d %-28s %-36s %s' % (r['act'], r['row'], '%s :%d' % (r['bank'], r['line']), r['arm'], r['head'][:110]) for r in R]
    L += ['', '### THE NONE ROWS, FOR THE AUTHOR`S DECISION ON WHICH RECEIVE ARMS:'] + ['  %s row %d -- %s' % (r['act'], r['row'], r['head'][:130]) for r in none]
    L += ['', '### ### **RULE ROWS %d ACROSS THE %d BANKS THAT EXIST (b676, b679 BANKED NONE) ; EACH ONCE True ; WITH A STANDING ARM %d ; NONE %d.**' % (
        len(R), len(RI.banks()), len(R) - len(none), len(none))]
    put_txt('b680_rules_arms.txt', L)
    put_json('b680_rules_arms.json', dict(at=utc(), rows=R, none=[[r['act'], r['row']] for r in none]))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE LEDGER SPLIT, PRICED BEFORE IT IS MADE, (R290)(6)
CITE = re.compile(r'FINDINGS(?:\.md)?\s?:(\d{3,5})((?:(?:,| and|,? or|;)\s*:\d{3,5})*)')
ANCHOR_CITE = re.compile(r'FINDINGS(?:\.md)?#[\w-]+')
SPLIT_BOUNDARY_ACT = 600


def _cut_block():
    """the proposed cut in the 2026-08-24 form (relay tools/ledger_split.py; PLACE-papers archive/2026-08-24-ledger-split/README.md :18-:22): the
    record stream moves, the reference frames stay -- FINDINGS` "What this document is", "Epistemic-weight tags" and "How to cite" (:434-:455);
    the block from the first record section after them through the last entry filed before b600."""
    F = rd(FIND).split(NL)
    start = next(i + 1 for i, l in enumerate(F) if l.startswith('## 0. '))
    heads = [i + 1 for i, l in enumerate(F) if l.startswith('## ')]
    end = None
    for h in heads:
        if h <= start:
            continue
        nxt = next((x for x in heads if x > h), len(F) + 1)
        filed = re.search(r'\*Filed at b(\d{3})', NL.join(F[h - 1:nxt - 1]))
        if filed and int(filed.group(1)) >= SPLIT_BOUNDARY_ACT:
            end = h - 1
            break
    return start, end, len(F)


def splitprice(*a):
    """(R290)(6): how line citations into FINDINGS survived the 2026-08-24 split (by anchor and the index of archived headings; the split tool
    re-pins no line citation), every `FINDINGS :NNNN` citation site found by git grep in relay's tracked banks and rowgen's name map and in
    PLACE-papers' tracked papers and ledgers, each with its kind and whether the proposed cut moves the line it cites (a line at or after the
    cut's start moves -- into the archive or upward by the block's length); the anchor citations counted apart. data/b680_split_price.txt."""
    start, end, nlines = _cut_block()
    roster_paths = set(p for _n, p in roster())
    sites = []
    for repo, specs, label in ((ROOT, ['data', 'tools/rowgen'], 'relay'), (PP, ['*.md', '**/*.md'], 'PLACE-papers')):
        # ### bytes, not text mode: text mode turns a stray CR inside a line into a line break (the first run's ValueError)
        out = subprocess.run(['git', '-C', repo, 'grep', '-n', '-I', '-E', r'FINDINGS(\.md)? ?:[0-9]{3,5}', 'HEAD', '--', *specs],
                             capture_output=True).stdout.decode('utf-8', 'replace')
        for raw in out.split(NL):
            if not raw.strip():
                continue
            _h, path, ln, text = raw.split(':', 3)
            if label == 'relay':
                kind = 'rowgen' if path.startswith('tools/rowgen') else ('corrigendum' if 'corrigendum' in path else 'bank')
            else:
                kind = ('ledger' if path in ('FINDINGS.md', 'OPEN_TRAILS.md') else ('archive' if path.startswith('archive/') else
                                                                                   ('roster (the Correspondence cells and tables)' if path in roster_paths else 'paper')))
            for m in CITE.finditer(text):
                for n in [int(m.group(1))] + [int(x) for x in re.findall(r':(\d{3,5})', m.group(2) or '')]:
                    moved = n >= start
                    sites.append(dict(repo=label, path=path, line=int(ln), kind=kind, cited=n, moved=moved))
    anchors = 0
    for repo, specs in ((ROOT, ['data']), (PP, ['*.md', '**/*.md'])):
        out = g(repo, 'grep', '-c', '-I', '-E', r'FINDINGS(\.md)?#[A-Za-z0-9_-]+', 'HEAD', '--', *specs)
        anchors += sum(int(x.rsplit(':', 1)[1]) for x in out.split(NL) if x.strip())
    by = collections.Counter((s['kind'], s['moved']) for s in sites)
    nm = sum(1 for s in sites if s['moved'])
    L = ['b680 -- COMPONENT 4, (R290)(6): THE LEDGER SPLIT PRICED BEFORE IT IS MADE (%s)' % utc(), '',
         '### HOW LINE CITATIONS SURVIVED THE 2026-08-24 SPLIT: by anchor. The README (PLACE-papers archive/2026-08-24-ledger-split/README.md :25-:26):',
         '### "a full index of the headings archived, so a citation resolves in one hop ... papers cite `FINDINGS#anchor-name`"; the split tool',
         '### (relay tools/ledger_split.py) moves byte-exact slices by anchors and writes that index (:84-:87) -- it re-pins NO line citation, and',
         '### no house tool re-pins ":NNNN" citations into FINDINGS. A line citation into a moved block, or below it, shifts.',
         '### THE PROPOSED CUT LINE, in that form (the record stream moves, the reference frames stay): FINDINGS :%d through :%s, the record' % (start, end),
         '### sections from "## 0." through the last entry filed before b%d; FINDINGS has %d lines; every line at or after :%d moves (into the' % (SPLIT_BOUNDARY_ACT, nlines, start),
         '### archive, or upward by %s lines).' % ((end - start + 1) if end else '?'),
         '### THE SITES: every `FINDINGS :NNNN` citation (and its listed continuations) by git grep at HEAD in relay`s data/ and tools/rowgen/ and in',
         '### PLACE-papers` tracked *.md (rowgen`s name map holds none); a site counts once per FINDINGS line it names. Its line number is read',
         '### against today`s FINDINGS: a site banked by an older act cites the line of its own day, which may already differ -- the count prices',
         '### the cut`s shift, not each site`s present accuracy. Kinds: bank, corrigendum, rowgen, roster (the Correspondence cells and tables), paper (the keystones and',
         '### the rest), ledger (FINDINGS and OPEN_TRAILS themselves), archive. Anchor citations (`FINDINGS#name`) %d, counted apart: they survive.' % anchors, '',
         '### BY KIND (sites ; moved by the cut):']
    for k in sorted(set(x for x, _m in by)):
        L.append('  %-46s %6d ; moved %6d' % (k, by[(k, True)] + by[(k, False)], by[(k, True)]))
    L += ['', '### ROWS ARE CITATION SITES (repo path :line ; kind ; the FINDINGS line cited ; moved by the cut):']
    L += ['  %s %s :%d ; %s ; FINDINGS :%d ; %s' % (s['repo'], s['path'], s['line'], s['kind'], s['cited'], 'MOVED' if s['moved'] else 'stays') for s in sites]
    held = nm > 0
    L += ['', '### ### **CITATION SITES %d ; MOVED BY THE CUT %d ; RE-PINNED BY A HOUSE TOOL 0 ; ANCHOR CITATIONS %d (SURVIVE) ; THE CUT FINDINGS :%d-:%s ; '
          'ARCHIVE-3 %s.**' % (len(sites), nm, anchors, start, end, 'HELD AT %d CITATIONS' % nm if held else 'TO BE MADE')]
    put_txt('b680_split_price.txt', L)
    put_json('b680_split_price.json', dict(at=utc(), start=start, end=end, lines=nlines, sites=len(sites), moved=nm, anchors=anchors,
                                           by_kind=dict(('%s|%s' % k, v) for k, v in by.items()), held=held))
    print(NL.join(L[6:9] + L[-1:]))


ROUTES = {'rowgen': rowgen, 'branches': branches, 'faces': faces, 'c1': c1, 'c1order': c1order, 'arms': arms, 'rulesarms': rulesarms,
          'splitprice': splitprice, 'c4order': c4order}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b680_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
