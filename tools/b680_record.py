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


# ================================================================================ THE ANSWERS BANK (b679's route, carried)
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
    """data/b680_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %s), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b680 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b680_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b680_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b679's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger or pin;
    returns (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


READERS += ['read_order_row']


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
    """(R290)(8): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
    c = QUOTED.sub(lambda m: m.group(0).strip('\'"'), cmd)
    dels = re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?branch\s+-[dD]\s+((?:[^\s&;|]+\s*)+)', c) + \
        re.findall(r'\bgit\s+(?:-C\s+\S+\s+)?push\s+origin\s+--delete\s+((?:[^\s&;|]+\s*)+)', c)
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
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    L = ['b680 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d; the reading act dispatches none):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R290)(8): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(mv),
                                                                          sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b680_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b680_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], moves_deletes=[r['n'] for r in mv],
                                        delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle']


def kernels(*a):
    ks = list(_kerns())
    put_json('b680_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula among them: the reading act writes no kernel)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b680_defects.txt').split(NL)
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
    t = rdn('b680_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b680_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b680_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b680_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('THE LEDGER GREP READ AS BYTES (answering the split route`s first run, a ValueError: text mode turned a stray CR inside a banked line into a',
     'line break): tools/b680_record.py splitprice reads git grep`s output as bytes and decodes it, so every citation line is read whole.'),
    ('THE FACES CHECK READS THE NEW RECORD`S OWN TEXT (answering the faces route`s first predicate, which required no backtick on the whole',
     'diff line while the generator joins every backmatter record into one paragraph): tools/b680_record.py faces reads the record by the',
     'generator`s own backmatter reader.'),
]


def repairs(*a):
    """data/b680_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b679 copy is read against
    b679's seal hash (relay data/b679_seal_hashes.json) first, and its diff against that copy counted by hunks."""
    import hashlib
    seal = jl('b679_seal_hashes.json').get('tools') or {}
    rows = []
    for t9 in ('b679_citation.py', 'b679_closing.py', 'b679_reg_gate.py', 'b679_regspec.py', 'b679_tests.py', 'b679_worklist.py',
               'b679_record.py', 'b679_checks.py'):
        t0 = t9.replace('b679_', 'b680_')
        old, new = os.path.join(T, t9), os.path.join(T, t0)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t9, t0, now, seal.get(t9), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    L = ['b680 -- COMPONENT 6, (R290)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b679`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b679`s sealed copy and its seal record; the hunks of the diff to b680`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t9, t0, now, s, nh in rows:
        L.append('  %-20s -> %-20s b679 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t9, t0, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b680_tool_repairs.txt', L)
    print(NL.join(L[-(len(rows) + 10):]))


ROOT_EXCLUDE = re.compile(r'^b680_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b680_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith(BINARY) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b680_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b680'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b680_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b680_ra_') as tmp:
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
    L = ['b680 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b680_root_arm.txt', L)
    put_json('b680_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b680 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b680_table_final.txt', L)
    put_json('b680_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b680_registration_2026-10-17.txt'
FACE = os.path.join(D, 'b680_registration_2026-10-17.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b680_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b680_regspec.py')], 'b680_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b680_satisfiable.json', '--emit', 'b680'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b680_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b680_census_stepzero.txt'), ('b327_faces_census.py', 'b680_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b680_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b680'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b680_reg_gate.txt', 'data/b680_reg_termscan.txt', 'data/b680_regspec_run.txt', 'data/audit_b680_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b679_closing_push_out.txt', 'b670_work_orders.txt', 'b679_landing.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.FACES_PAGE)
READINGS = ('licensed', 'correspondence', 'ceiling', 'orders', 'methods', 'kernels9', 'residues', 'lag', 'outside')
VL = re.compile(r'### ### \*\*(.*?)\*\*')


def TRAIL_HEAD():
    return ('### b680 — lane two, act one hundred and seven, the reading act, reading 2 of 2 under (R290): the nine readings by b670’s methods, '
            'the arms and the rules mapped, the ledger split priced and held, three figures, the faces line on the author’s word')


def _calls():
    return jl('b680_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _verdict(name, needle):
    m = re.search(r'\*\*(.*' + re.escape(needle) + r'.*)\*\*', rdn(name))
    return m.group(1) if m else '### UNREAD'


def _paired(name):
    """N2: the bank's verdict lines, the one that prints b670's figure beside b680's -- a line citation of b670's method, or NOT COMPARABLE."""
    vs = VL.findall(rdn('b680_%s.txt' % name))
    hit = [v for v in vs if 'b670' in v and (re.search(r':\d{2,4}\b', v) or 'NOT COMPARABLE' in v)]
    return hit[0] if hit else None


def _n1():
    cm = jl('b680_commands.json')
    ok = bool(cm) and not cm.get('local_lean') and not cm.get('dispatches')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b680_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _n2():
    got = [(n, _paired(n)) for n in READINGS]
    ok = all(v for _n, v in got)
    return ('HELD' if ok else 'REFUTED'), 'the nine readings, each bank`s verdict line with b670`s figure by a cited line or NOT COMPARABLE: %s' % (
        '; '.join('%s %s' % (n, 'PAIRED' if v and 'NOT COMPARABLE' not in v else ('NOT COMPARABLE' if v else '### UNPAIRED')) for n, v in got))


def _ceiling_now():
    import b670_record as B
    import b674_record as B4
    import b680_readings as RDG
    store = RDG.captured(B)
    B.ceiling()
    T1 = store['b670_ceiling.txt']
    fl = jl('b674_record_lines_c2.json').get('lines') or []
    hs = [B4._placement(f, n)[2] for f, n in (('README.md', 127), ('REGISTRY.md', 962), ('FINDINGS.md', fl[0]['line'] if fl else None))]
    return VL.findall(NL.join(T1))[-1] if VL.findall(NL.join(T1)) else '', hs


def _n3():
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    beyond = [x for x in pp_ch if x not in N5_PP]
    cj = jl('b680_ceiling.json')
    cv, hs = _ceiling_now()
    banked = [r[2] for r in cj.get('successor') or []]
    ceil_ok = 'EQUAL AT THREE PLACEMENTS' in cv and 'HASHES 1 DISTINCT' in cv and cv in (cj.get('ceiling') or '')
    succ_ok = bool(banked) and hs == banked and len(set(hs)) == 1
    fd = rdn('b680_faces_diff.txt')
    faces_ok = 'LINES ADDED 3 ; REMOVED 3' in fd and 'PAGE WRITTEN True' in fd
    ok = not beyond and ceil_ok and succ_ok and faces_ok
    return ('HELD' if ok else 'REFUTED'), (
        'PLACE-papers files written beyond FINDINGS, OPEN_TRAILS and the faces page: %s; the faces page by its generator on the author`s word '
        '(relay data/b680_faces_diff.txt) %s; archive-3 not made; the ceiling sentence at the close "%s" against the bank`s %s; the successor`s '
        'three sites at the close %s, byte-equal to the bank`s %s' % (beyond or 'NONE', faces_ok, cv[:90], cv in (cj.get('ceiling') or ''),
                                                                     [h[:12] for h in hs], succ_ok))


def _n4():
    A, R, I = jl('b680_arms.json'), jl('b680_rules_arms.json'), jl('b680_rules_index.json')
    arms_ = [r['arm'] for r in A.get('rows') or []]
    kinds_ok = all(r.get('kind') in ('SHAPE', 'VALUE') for r in A.get('rows') or [])
    rules_ = [(r['act'], r['row']) for r in R.get('rows') or []]
    idx = [(r['act'], r['row']) for r in I.get('rows') or []]
    armcol_ok = all(r.get('arm') for r in R.get('rows') or [])
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        C = importlib.import_module('b680_checks')
        st = list(C.STANDING)
    finally:
        sys.argv = argv
    ok = bool(arms_) and sorted(arms_) == sorted(set(arms_)) == sorted(st) and kinds_ok and bool(rules_) and sorted(rules_) == sorted(set(rules_)) \
        and sorted(rules_) == sorted(idx) and armcol_ok
    return ('HELD' if ok else 'REFUTED'), (
        'every standing arm once with its kind: %d rows, SHAPE %d, VALUE %d, against the suite`s standing %d (relay data/b680_arms.txt); every '
        'rule row once with an arm or NONE, read by the author`s answer as across the banks that exist: %d rows in %d banks, NONE %d, against '
        'the index`s %d (relay data/b680_rules_arms.txt, data/b680_rules_index.txt)' % (
            len(arms_), A.get('shape', 0), A.get('value', 0), len(st), len(rules_), len(set(r['bank'] for r in R.get('rows') or [])),
            len(R.get('none') or []), len(idx)))


def _n5():
    face = jl('b680_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items()) and 'SIDE-explicit-formula' in face \
        and g(K.KE, 'rev-parse', '--short=7', 'main').strip() == K.K_MAIN
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b680_|audit_b680_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b680_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written, every kernel as the face read it '
            '(SIDE-explicit-formula at %s among them) %s; PLACE-papers beyond FINDINGS, OPEN_TRAILS and the faces page: %s; standing arms added: '
            '%s (the act`s arms over its own banks %d); sealed tools not agreeing %s; relay files of a kind beyond the act`s tools, scripts and '
            'banks, the table, the root list, b679`s push-out bank, the orders bank`s two rows and the landing bank`s one: %s; "patent" in the '
            'lines written: %s; outbound requests: the seat`s git reads and pushes at github.com, so no identifier of the author placed in a '
            'request; the mirror zip outside every repository' % (K.DRAFT, K.K_MAIN, k_ok, pp_beyond or 'NONE', new_arms or 'NONE',
                                                                  len(K.ACT_ARMS), differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b680_table_final.json'), jl('b680_root_arm.json')
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
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b680_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    """the title's figures, each read from its bank: (R290)'s FINDINGS title form."""
    lag = re.search(r'KEYSTONES (\d+) ; WITH A LAG READ (\d+) ; LAGGING \(OBJECT MOVED AFTER THE TEXT\) (\d+) ; THE LARGEST LAG (\d+) ; THE MEDIAN (\d+)',
                    rdn('b680_lag.txt'))
    k9 = jl('b680_kernels9.json').get('rows') or []
    sp = jl('b680_split_price.json')
    od = jl('b680_orders.json')
    me = jl('b680_methods.json')
    return dict(lic=jl('b680_licensed.json').get('total', '?'), corr=jl('b680_correspondence.json').get('behind', '?'),
                op=od.get('open', '?'), dn=od.get('done', '?'), ns=len(od.get('no_status') or []), mc=me.get('ready_code', '?'), mh=me.get('ready', '?'),
                pb=sum(1 for r in k9 if r.get('in_nine') and r.get('held')), res=len(jl('b680_residues.json').get('rows') or []),
                lag=('%s of %s lagging, the largest %s, the median %s' % (lag.group(3), lag.group(1), lag.group(4), lag.group(5))) if lag else '?',
                sh=jl('b680_arms.json').get('shape', '?'), va=jl('b680_arms.json').get('value', '?'),
                rn=len(jl('b680_rules_arms.json').get('none') or []) if 'none' in jl('b680_rules_arms.json') else '?',
                a3=('HELD at %d citations' % sp['moved']) if sp.get('held') else 'made')


def _title():
    f = _figs()
    return ('## Reading 2 of 2: licensed rows %(lic)s against 372; Correspondence %(corr)s against 54; orders %(op)s/%(dn)s/%(ns)s; methods %(mc)s of 12 '
            '(%(mh)s with the hand-read cells); print banks %(pb)s of 9; residues %(res)s; keystone lag %(lag)s; arms SHAPE %(sh)s VALUE %(va)s; '
            'rules without arms %(rn)s; archive-3 %(a3)s' % f)


def _finding_text():
    S, J = jl('b680_scores.json'), jl('b680_act_root.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b680_author_answers.txt'), re.M))
    c1 = _rl_lines('b680_record_lines.json') + ['?']
    co = _rl_lines('b680_record_lines_order.json') + ['?']
    c4 = _rl_lines('b680_record_lines_order4.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    sp = jl('b680_split_price.json')
    e = ['', _title(), '',
         'The second reading of the programme’s own state, each by the method b670 used and with b670’s figure printed beside it. The licensed '
         'table moved from 372 rows outside LICENSED or CITED to %(lic)s; the Correspondence rows behind their kernel stand at %(corr)s against 54, '
         'the generator’s claim at 0 against 0; the orders count %(op)s open, %(dn)s done and %(ns)s with no Status cell, against 34, 46 and 69. '
         'Where b670 made no such reading -- the nine kernels’ print banks, the residues, the keystone lag, the outside-reader test -- the bank '
         'says NOT COMPARABLE and gives the reason, and no new method stands in for b670’s. Nothing here proves RH or GRH.' % f, '',
         '*Filed at b680 on the author’s ruling `(R290)`%s. Banks: relay `data/b680_licensed.txt`, `data/b680_correspondence.txt`, '
         '`data/b680_ceiling.txt`, `data/b680_orders.txt`, `data/b680_methods.txt`, `data/b680_kernels9.txt`, `data/b680_residues.txt`, '
         '`data/b680_lag.txt`, `data/b680_outside.txt`, `data/b680_arms.txt`, `data/b680_rules_arms.txt`, `data/b680_split_price.txt`, '
         '`data/b680_act_root.txt`; the tools `tools/b680_readings.py`, `tools/b680_rules_index.py`.*' % (
             (' and the navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the rules banks of b676 and b679, which '
         'were never written, raised and answered (read across the banks that exist). b679 at its weight (FINDINGS :%s); '
         '`W-ORD-EPSTEIN-COUNT` entered OPEN (OPEN_TRAILS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0], co[0]), '',
         '**The faces line** (`(R290)`(2)): on the author’s word, the Li face over the widened class written through the generator’s backmatter '
         'record with the three repairs the word named, the page regenerated and diffed against the committed one (relay '
         '`data/b680_faces_diff.txt`); T-COUNT named in it.', '',
         '**The readings** (`(R290)`(4)): the methods ready %(mc)s of 12 by b670’s code and %(mh)s with the hand-read cells, against b671’s 11; the '
         'ceiling sentence and its successor byte-equal at their three sites each; print banks at a tag held by %(pb)s of the nine kernels; '
         'residues %(res)s sentences; keystone lag %(lag)s.' % f, '',
         '**The arms and the rules** (`(R290)`(5)): the 68 standing arms, SHAPE %(sh)s and VALUE %(va)s, each once; the 26 rules of the eight '
         'banks that exist, %(rn)s with no standing arm; the index a tool committed alone. No arm added.' % f, '',
         '**The ledger split** (`(R290)`(6)): the 2026-08-24 split kept citations by anchor and its tool re-pins no line citation; the proposed '
         'cut FINDINGS :%s-:%s moves the line cited by %s of %s sites. Archive-3 HELD; on the navigator’s answer the later route is a '
         'banked line-offset table with a resolver, `W-ORD-LEDGER-SPLIT-RESOLVER` (OPEN_TRAILS :%s).' % (
             sp.get('start'), sp.get('end'), sp.get('moved'), sp.get('sites'), c4[0]), '',
         '**The figures** (`(R290)`(7)): the tie diagnostic, the Q0 configuration and the Li index at Q0, each drawn by its own script committed '
         'alone (relay `data/b680_fig_tie.png`, `data/b680_fig_q0.png`, `data/b680_fig_li.png`).', '',
         '**The root.** b680 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b670’s reading act by its own methods, and is re-read by the re-cut '
         'act that acts on the Correspondence rows, by any act that makes archive-3, and by the author’s choice of the rules that receive arms. '
         'It strengthens the programme’s offerings of a self-audit whose figures can be compared across acts.', '',
         '**Carried to:** T-COUNT for Q0 (`W-ORD-EPSTEIN-COUNT`, after b681); the ledger split’s resolver, on the author’s word; the 24 rules '
         'without arms, for the author’s decision; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the split’s cut proposed in the 2026-08-24 form at the b600 boundary, the reference frames kept, so the count prices a cut that '
              'would be made and not the whole ledger; (2) the methods printed both ways, by b670’s code and with the hand-read cells, so b671’s 11 is '
              'compared by its own method; (3) the Li figure’s panel (a) labelled an alias of its 100-step sampling against the period 2π/θ; (4) the '
              'figures drawn with PIL, matplotlib not being installed on this host and nothing installed by the act')


def _trail_text():
    S, J = jl('b680_scores.json'), jl('b680_act_root.json')
    fj = jl('b680_findings.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b680_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b680_record_lines.json') + ['?']
    co = _rl_lines('b680_record_lines_order.json') + ['?']
    c4 = _rl_lines('b680_record_lines_order4.json') + ['?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R290) ratified.** (1) b679 at its weight. (2) The faces line. (3) The order on T-COUNT. (4) The nine readings. (5) The arms and the '
             'rules. (6) The ledger split. (7) The figures. (8) The branches. (9) The read-first bank. (10) The draft held at v5. (11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b679’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-EPSTEIN-COUNT`, OPEN, trigger after b681), '
             ':%s (`W-ORD-LEDGER-SPLIT-RESOLVER`, OPEN, on the author’s word); the faces page’s backmatter record; this record.' % (
                 c1[0], fj.get('entry_line'), co[0], c4[0]), '',
             '**Act root:** b680 `%s` (previous `%s`, b679’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b680_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The readings:** licensed %(lic)s against 372; Correspondence %(corr)s against 54; orders %(op)s/%(dn)s/%(ns)s against 34/46/69; methods '
             '%(mc)s of 12 by b670’s code, %(mh)s with the hand-read cells; print banks %(pb)s of 9; residues %(res)s; keystone lag %(lag)s.' % f, '',
             '**The arms and the rules:** SHAPE %(sh)s, VALUE %(va)s; rules without arms %(rn)s (relay data/b680_rules_arms.txt).' % f, '',
             '**The ledger split:** archive-3 %(a3)s (relay data/b680_split_price.txt).' % f, '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b680_closing.txt).', '',
             '**The open orders:** `W-ORD-EPSTEIN-BALL-WIDTH` (b681, the narrowing act); `W-ORD-MAP-ANGLE-FORM` (after it); '
             '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` (b682, the re-cut act); `W-ORD-EPSTEIN-COUNT` (after b681); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the '
             'author’s word); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b680_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b680_scores.json')
    L = ['=' * 104, 'b680 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b680_defects.txt').rstrip(NL).split(NL)
    put_txt('b680_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b680_scores.json', 'b680_findings.json', 'b680_trail.json', 'b680_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b680_record_lines.json') + ['?']
    co = _rl_lines('b680_record_lines_order.json') + ['?']
    c4 = _rl_lines('b680_record_lines_order4.json') + ['?']
    L = ['b680 -- THE COMPONENTS, BANKED UNDER (R290).', '',
         '### COMPONENT 0 : the citation check (data/b680_citation_check.txt), step zero (data/b680_ferry.txt, data/b680_readfirst.txt, '
         'data/b680_stepzero.txt, data/b680_tests_stepzero.txt, data/b680_rowgen_stepzero.txt, data/b680_branches.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b679`s weight FINDINGS :%s ; the faces line (data/b680_faces_diff.txt) ; W-ORD-EPSTEIN-COUNT OPEN_TRAILS :%s' % (c1[0], co[0]),
         '### COMPONENT 2 : the nine readings (data/b680_licensed.txt ... data/b680_outside.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the arms (data/b680_arms.txt), the rules index (tools/b680_rules_index.py), the rules to arms (data/b680_rules_arms.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 4 : the split priced (data/b680_split_price.txt), archive-3 HELD, W-ORD-LEDGER-SPLIT-RESOLVER OPEN_TRAILS :%s' % c4[0],
         '### COMPONENT 5 : the figures (data/b680_fig_tie.png, data/b680_fig_q0.png, data/b680_fig_li.png), each script committed alone',
         '### COMPONENT 6 : the carry-time reading (data/b680_tool_repairs.txt), the dry-run steps (data/b680_reg_gate.txt), the seal '
         '(data/b680_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b680_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b680_findings.json', dict(title=t))
    j = jl('b680_findings.json')
    j['entry_line'] = ln
    put_json('b680_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b680_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b679's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-17-b680'
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
    put_json('b680_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b680':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b680`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b680_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b680_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b680_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b680 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b680 (the last export b679`s, D:/MY-DOwnloads/mirror-refresh-2026-10-17-b679.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b680_mirror.txt', L)
    put_json('b680_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'faces': faces, 'c1': c1, 'c1order': c1order, 'arms': arms, 'rulesarms': rulesarms,
          'splitprice': splitprice, 'c4order': c4order,
          'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank,
          'answers': answers, 'commands': commands, 'kernels': kernels, 'defects': defects, 'repairs': repairs,
          'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk,
          'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b680_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
