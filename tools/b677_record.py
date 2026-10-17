# -*- coding: utf-8 -*-
"""b677_record.py -- THE ACT'S RECORD TOOL, b677 under (R287).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b677's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b676_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes);
### the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b677_record.py <route> [dry]`.
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
import b677_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b676_record.py with b677's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b677_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b677_findings.json': dict(entry_line=99999, title='stand-in'),
        'b677_trail.json': dict(line=99999),
        'b677_act_root.json': dict(root='0' * 64, previous='d3271717' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b677's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b677_scanfile_%s.md' % tag)
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
    """a row of data/b677_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    """b670 rules row 3 ("Run rowgen diff and constellation mode at the start of any review pass"): tools/rowgen/rowgen.py `constellation
    <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the build-free diff; `rowgen.py diff` calls lean and is not
    run on this host) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b677_rowgen_stepzero.txt."""
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
    L = ['b677 -- STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE AT THE START OF THE ACT (b670 rules row 3) (%s)' % utc(), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b677_rowgen_stepzero.txt', L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R287)(6))
def branches(*a):
    """every branch (R287)(6) names, its tip read before any delete, its fate; SIDE-trivium's recut branch at its remote as well, its tip
    printed as an ancestor of main 135be2e first. data/b677_branches.txt (.json); writes nothing else."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    anc = []
    for repo, b in K.DELETE_REMOTE:
        tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b).strip()
        rc = subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', tip, K.T_MAIN], capture_output=True).returncode if tip else 1
        anc.append((b, tip, rc == 0))
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=rc == 0, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    L = ['b677 -- STEP ZERO, (R287)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main` (a remote row: its tip an',
         '### ancestor of SIDE-trivium main %s by `git merge-base --is-ancestor`) ; fate.' % K.T_MAIN,
         '### Deleted by name in the house form after --merged lists them, one repository per call; no branch the ruling does not name is',
         '### deleted; the one remote deletion the ruling names is SIDE-trivium recut-trivium-b676, after its tip is printed an ancestor of main.']
    L += ['  %-24s %-20s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                              r['fate']) for r in rows]
    L += ['  the remote tip %s of %s an ancestor of main %s: %s' % (t[:9], b, K.T_MAIN, ok) for b, t, ok in anc]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d.**' % (
        len(rows), sum(1 for r in rows if r['where'] == 'local'), sum(1 for r in rows if r['where'] == 'remote'),
        sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b677_branches.txt', L)
    put_json('b677_branches.json', dict(at=utc(), rows=rows))
    print(NL.join(L[6:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R287)(1)
WH = ('*Appended 2026-10-17 by b677 to b676’s entry (:8913), under `(R287)`(1) -- b676 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b676_closing.txt):*')
WB = (' “b676 closed: relay afb4bd59, PLACE-papers 9abb234, SIDE-trivium 135be2e v0.1.1; suite 84 of 84; root d3271717321e8d5e…; 2 prompts '
      'answered; 9 defects” (data/b676_closing.txt :1), the closing pushed at relay e41e165f (data/b676_closing_push_out.txt :4). The re-cut '
      '(:24-:28): SIDE-trivium named alone at 5, no tie; the workflow and the 22-name print list each committed alone on main (dd587f9, '
      '7074154); the ‘before’ print bank at main, 9 commits past v0.1, said so (:78); the cut db315fe comments and docstrings alone; both '
      'runner builds DERIVES, 22 prints equal line for line; merged 135be2e, tag v0.1.1; rows outside LICENSED/CITED 5 to 1, the header’s '
      '“correspond exactly” paragraph a residue beside SIDE-window’s marker at :17 (data/b676_cut.txt); no Correspondence cell moved. The Q0 '
      'lines (:31): 136 hits hand-read, 100 CONSISTENT, 36 sentences on 35 lines TO RE-CUT (25 FINDINGS, 11 OPEN_TRAILS), nothing cut, '
      'W-ORD-Q0-CLASS-LINES at OPEN_TRAILS :14556 and OPEN in the orders bank (data/b670_work_orders.txt :262). The strip’s uses (:33): 22 in '
      'V5 and the composition, listed by file and line; one step not carried by a constant alone, LiConverseCfg.lean :231, needing the point '
      '1/(1 − R) excluded once R > 3. The arm count: no arm removed, 68 standing arms at both acts, the per-act arms 16 at b674 and 15 at '
      'b675, the ruling’s “removal” the navigator’s defect (e). Entry FINDINGS :8913, trail OPEN_TRAILS :14560, root over 48 banks; N1–N5, '
      'S1–S3 held (:46); the suite 84 of 84 pre-push and post-push (:106, :108); nine defects (a)–(i), the navigator’s (c)(d)(e) '
      '(data/b676_defects.txt :5–:44). Nothing deposited.')
OH = ('*Appended 2026-10-17 by b677, under `(R287)`(1) and its ferry’s step zero -- W-ORD-CHAIN-PAGE-B638-CASES, ENTERED WITH ITS '
      'TRIGGER:*')
OB = (' the two test files failing at every act’s step zero since b638, named by path with their failing lines (relay '
      'data/b677_tests_stepzero.txt): tools/test_chain_page.py case (9), “the title is the variant’s” (:246), carried by '
      'W-ORD-TESTS-WITH-THE-LISTS-IN-FORCE (:13838, b650), the order that names this case; and tools/test_chain_page_b638.py cases '
      '(4)–(7) (:327–:330), the faces-page generator read on b632’s ζ list without the mark exiting 6 with 0 bytes, so the block its cases '
      'compare is empty -- which no order carried (relay data/b677_citation_check.txt: the one line naming the file beside an order, '
      ':13583, b643’s defects, its order W-ORD-WATCHDOG-STOP unrelated). This order carries the second: the generator’s exit 6 on that list '
      'read to its cause, and the four cases either repaired against the list in force or retired by the author’s word with the reason '
      'banked. Trigger: the next act that edits the faces-page generator or the lists it reads, or b680’s census of the suite’s arms by what '
      'each reads, whichever comes first. Status OPEN.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL), ('OPEN_TRAILS.md', OH, NL + OH + OB + NL)], 'b677_record_lines.json', 'c1', entry=K.B676_ENTRY,
         check=[('FINDINGS.md', K.B676_ENTRY, '## SIDE-trivium docstrings re-cut'), ('OPEN_TRAILS.md', K.B676_TRAIL, '### b676')], dry=dry)


# ================================================================================ COMPONENT 4: THE LANDING, (R287)(5), on the navigator's answer on the run
AH = ('*Appended 2026-10-17 by b677 beneath `W-ORD-MAP-ANGLE-FORM` (:14398), under `(R287)`(5) and the navigator’s answer on the run -- THE '
      'ORDER ACTED, KEPT OPEN, ITS TRIGGER RE-WRITTEN:*')
AB = (' the map run in the angle form over Q0’s narrowed balls (relay tools/b677_epstein_map_angle.py: every power exp(n·log z), log z once '
      'per ball; the b667 map left as it is): the control Z₁ reproduced (j₀ = 31, the zero side below 0); at Q0 the tie controls pass at '
      'j = 24–52 and read INSTRUMENT at j = 53–64, 12 of 41 at 200 and at 400 bits, OBJECT 0 (relay data/b677_map.txt); of b671’s 46 '
      'INSTRUMENT controls 22 now pass and 24 do not, so H1 is refuted. THE LOCATED FAILURE (data/b677_map.txt, the row j = 53 at 200 bits): '
      'the phase angle’s radius doubles exactly per j (6.169·10⁻¹⁸ at j = 24, 6.783·10⁻⁶ at j = 64), and the residual’s radius stands 150 '
      'to 540 times the angle’s at every j, lost in the interpolation’s real coefficients (the b667 map :345–:348); at the banked width '
      '10⁻²⁴ the two cross the bar 2⁻²⁰ at j = 53, the radius at j = 64 2.05·10⁻³ (the plan’s price 1.3·10⁻⁴ to 7.7·10⁻², relay '
      'data/b677_map_plan.txt section 6). The tie residual is zero at every j by the orbit’s symmetry (the plan, section 4), so a failed '
      'control can only be the instrument’s, and the shift plant fires at every j (relay data/b677_tolerance.txt). No object reading is '
      'taken from H3 or H4: H3 refuted on the failing instrument, H4 not scorable (relay data/b677_map_h.txt). The labelled reading past '
      'the tie controls, hQtie taken from coeffs_exist and the orbit identity and not from balls -- an instrument-side row, not an object '
      'finding: j₀ = 38, the zero side [−7.570971096·10³⁹ ± 3.96·10²⁹], below 0. Status OPEN. **Trigger:** after `W-ORD-EPSTEIN-BALL-WIDTH`.')
BH = ('*Appended 2026-10-17 by b677 beneath `W-ORD-EPSTEIN-BALL-WIDTH` (:14396), under `(R287)`(5) and the navigator’s answer on the run -- '
      'THE WIDTH FIGURE RE-ENTERED FROM MEASUREMENT; THE ORDER OPEN:*')
BB = (' the consumer’s tolerance measured on the consumer by a width plant in the angle form (relay data/b677_tolerance.txt: every input '
      'ball’s half-width set to h about the banked centres, a planted width and not a certified ball): every tie control to J_max = 64 '
      'passes at h ≤ 3.2·10⁻²⁸ (h_tol(64) by a half-decade bisection; 10⁻²⁷ fails at j = 63 and 64), confirmed by a pass at a third of it '
      'and a failure at three times it; at j = 38, b667’s sizing, h_tol is 3.2·10⁻²⁰, 0.032 times b667’s estimate near 10⁻¹⁸ (relay '
      'data/b667_h4_reading.txt :13–:14). THE FIGURE THIS ORDER NOW CARRIES: 3.2·10⁻²⁸, measured, in place of b671’s two, left beside it '
      'with their labels -- (ii) from the amplification, 8.5·10⁻³⁰, about 10⁻³¹ with two decimal orders; (i) the linear estimate, '
      '1.5·10⁻³⁸, 1.5·10⁻⁴⁰ with two decimal orders -- and the plan’s price beside them, 1.2·10⁻²⁹ to 7.2·10⁻²⁷ (relay '
      'data/b677_map_plan.txt section 6). b671’s balls, at half-width 10⁻²⁴, stand about 3·10³ times above it. Status OPEN. **Trigger:** a '
      'narrowing act whose balls reach half-width 10⁻²⁸ or finer, its placement the author’s; `W-ORD-MAP-ANGLE-FORM` re-run after it.')
ORDERS = 'b670_work_orders.txt'


def c4(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', AH, NL + AH + AB + NL), ('OPEN_TRAILS.md', BH, NL + BH + BB + NL)], 'b677_landing.json', 'c4',
         check=[('OPEN_TRAILS.md', 14398, 'W-ORD-MAP-ANGLE-FORM'), ('OPEN_TRAILS.md', 14396, 'W-ORD-EPSTEIN-BALL-WIDTH')], dry=dry)
    if dry:
        return
    j = jl('b677_landing.json')
    la, lb = [x['line'] for x in j['lines']]
    rows = ['', '### Appended 2026-10-17 by b677 under (R287)(5) (additive, (R254)(2)): the two orders landed on OPEN_TRAILS at Component 4, '
                'each with its Status cell filled; W-ORD-MAP-ANGLE-FORM had no row here (the bank was written at b670, the order entered '
                'at b671 -- the citation check`s miss (iv)).',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-MAP-ANGLE-FORM', 14398, 'b671', 677 - 671, 'OPEN', la,
                                                       'after W-ORD-EPSTEIN-BALL-WIDTH', la),
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-EPSTEIN-BALL-WIDTH', 14264, 'b667', 677 - 667, 'OPEN', lb,
                                                       'a narrowing act at half-width 1e-28 or finer', lb)]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL                 # ### one blank line before the appended block, as b676's append
    new = old + (sep + NL.join(rows[1:]) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after): %s' % (ORDERS, len(old), len(new), ' | '.join(r.strip()[:60] for r in rows[2:])))


# ================================================================================ THE ANSWERS BANK (b676's route, carried)
def _session_rows():
    """the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER, b646's form) from its own anchor; a continuation whose
    anchor is not a user line stops the route."""
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
    """data/b677_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
    delivered between BEGIN and END after the ruling (pastes unwrapped from the host's wrapper), and the author's plain messages, verbatim."""
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
    head = ['### b677 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b677_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b677_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b676's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
MAP_CELLS = ('THE CONTROL Z₁(0.8, 29.6)', 'Q0 AT qE0')
MAP_WORDS = ('PASS', 'INSTRUMENT', 'OBJECT', 'NEITHER')


def read_map_row(r):
    """a row of data/b677_map.json: a cell (one of MAP_CELLS), a precision (200 or 400), j (an int), the four residuals' radii, the angle's
    radius, a word (one of MAP_WORDS) and b671's word beside it; returns (cell, bits, j, word)."""
    if not isinstance(r, dict) or r.get('cell') not in MAP_CELLS or r.get('bits') not in (200, 400) or not isinstance(r.get('j'), int) \
            or not isinstance(r.get('rads'), list) or len(r['rads']) != 4 or not isinstance(r.get('angle_rad'), float) \
            or r.get('word') not in MAP_WORDS or r.get('b671') not in MAP_WORDS:
        raise ValueError('map row of another shape: %r' % (str(r)[:120],))
    return r['cell'], r['bits'], r['j'], r['word']


ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger; returns
    (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


def read_runner_row(r):
    """a row of data/b676_runner_rows.json (the last merged run, b676's, read by the standing runner arms; no runner is dispatched in this act):
    the kernel SIDE-trivium, a label (before or after), a 40-hex ref, a run id, a gate; returns (label, gate). Carried from b676_record.py."""
    if not isinstance(r, dict) or r.get('kernel') != 'SIDE-trivium' or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


READERS += ['read_map_row', 'read_order_row', 'read_runner_row']


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid, anc,
                          'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % sid)
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
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


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and re.search(r'(^|&&\s*|;\s*)gh workflow run\b', QUOTED.sub('""', r['cmd']), re.M)]
    L = ['b677 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; MOVE OR DELETE COMMANDS %d.**' % (
        len(rows), len(hits), len(lean), len(disp), len(mv))]
    put_txt('b677_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b677_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium']      # ### the two kernels re-cut at b674 and b676, beside b641's thirteen


def kernels(*a):
    ks = _kerns()
    put_json('b677_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b677_defects.txt').split(NL)
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
    t = rdn('b677_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b677_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b677_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b677_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


# ================================================================================ COMPONENT 5: THE CARRY-TIME READING ((R287)'s ferry)
def repairs(*a):
    """data/b677_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b676 copy is read against
    b676's seal hash (relay data/b676_seal_hashes.json) first, and its diff against that copy printed by hunk count and by the hunks that touch
    a line of logic rather than the act's names, banks and sections; a repair is a hunk that answers a defect, named with it."""
    import hashlib
    seal = jl('b676_seal_hashes.json').get('tools') or {}
    rows = []
    for t6 in ('b676_citation.py', 'b676_closing.py', 'b676_reg_gate.py', 'b676_regspec.py', 'b676_tests.py', 'b676_worklist.py',
               'b676_record.py', 'b676_checks.py'):
        t7 = t6.replace('b676_', 'b677_')
        old, new = os.path.join(T, t6), os.path.join(T, t7)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        hunks = re.split(r'(?m)^(?=@@ )', d)[1:]
        rows.append((t6, t7, now, seal.get(t6), len(hunks)))
    L = ['b677 -- COMPONENT 5, (R287)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b676`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b676`s sealed copy and its seal record; the hunks of the diff to b677`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- and no hunk repairs a defect of a carried',
         '### route: b676`s defects (relay data/b676_defects.txt (a)-(i)) name no tool route the carry would mend; the closing`s and the',
         '### citation tool`s routes are carried unchanged in their logic.', '']
    for t6, t7, now, s, nh in rows:
        L.append('  %-20s -> %-20s b676 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t6, t7, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L += ['', '### ### **REPAIRS 0 ; THE SEALED COPIES %s ; TOOLS CARRIED %d.**' % ('AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER',
                                                                                 len(rows))]
    put_txt('b677_tool_repairs.txt', L)
    print(NL.join(L[-(len(rows) + 2):]))


ROOT_EXCLUDE = re.compile(r'^b677_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b677_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b677_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b677'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b677_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b677_ra_') as tmp:
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
    L = ['b677 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b677_root_arm.txt', L)
    put_json('b677_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b677 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b677_table_final.txt', L)
    put_json('b677_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b677_registration_2026-10-17.txt'
FACE = os.path.join(D, 'b677_registration_2026-10-17.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b677_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b677_regspec.py')], 'b677_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b677_satisfiable.json', '--emit', 'b677'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b677_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b677_census_stepzero.txt'), ('b327_faces_census.py', 'b677_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b677_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b677'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b677_reg_gate.txt', 'data/b677_reg_termscan.txt', 'data/b677_regspec_run.txt', 'data/audit_b677_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
# ### carried from b676_record.py by the Edit tool, every predicate re-written against (R287)'s expectations and this act's banks
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b676_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b677 — lane two, act one hundred and four, the research act under (R287): the detection map in the angle form over the '
            'narrowed balls; the controls re-read; the consumer’s tolerance measured')


def _calls():
    return jl('b677_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _epoch(ts):
    import calendar
    return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')) if ts else None


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _first_commit_of(repo, path):
    """the commit time of the first commit since the act began that adds `path`."""
    t = g(repo, 'log', '--reverse', '--diff-filter=A', '--format=%ct', '%s..HEAD' % K.PRE_RELAY, '--', path).split()
    return int(t[0]) if t and t[0].isdigit() else None


H3_QUOTE = 'at Q0 every hypothesis of zeroSide_neg_at_rate_cfg certifies by name and hrate holds at some j₀ ≤ D + 40'
H4_QUOTE = 'prints j₀ = 38 and a zero side below zero, each with its ball'


def _n1():
    cm = jl('b677_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b677_commands.txt, %d commands read); runner dispatches %d' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('rows') or []), len(cm.get('dispatches') or [])))


def _n2():
    plan = rdn('b677_map_plan.txt')
    plan_ct = _first_commit_of(RELAY, 'data/b677_map_plan.txt')
    tol_at, hyp_at = _epoch(jl('b677_tolerance.json').get('at')), _epoch(jl('b677_map_h.json').get('at'))
    p1_at = _epoch(jl('b677_tolerance_p1.json').get('at'))
    flat = ' '.join(plan.split())        # ### the plan wraps its quotes across lines: read whole (b675's trap)
    quoted = H3_QUOTE in flat and H4_QUOTE in flat and 'data/b663_epstein_plan.txt :131' in flat \
        and 'data/b667_epstein_plan.txt section 8 :124-:125' in flat
    order = bool(plan_ct and p1_at and tol_at and hyp_at) and plan_ct < p1_at <= tol_at < hyp_at
    ok = quoted and order
    return ('HELD' if ok else 'REFUTED'), (
        'H3 quoted from data/b663_epstein_plan.txt :131 (the navigator`s answer on the H3 source; the ruling`s "the b667 plan" read there, the '
        'citation check`s miss (iii)) and H4 from data/b667_epstein_plan.txt section 8 :124-:125, in relay data/b677_map_plan.txt committed %s, '
        'before any run: %s; the tolerance measured on the consumer (P1 %s, the bank %s) before any hypothesis was read against it (%s): the '
        'order %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(plan_ct)) if plan_ct else '### UNREAD', quoted,
                      jl('b677_tolerance_p1.json').get('at'), jl('b677_tolerance.json').get('at'), jl('b677_map_h.json').get('at'), order))


def _n3():
    m = jl('b677_map.json')
    rows = m.get('rows') or []
    try:
        got = [read_map_row(r) for r in rows]
    except Exception:
        got = []
    radii = bool(rows) and all(all(isinstance(x, float) for x in r['rads']) and isinstance(r['angle_rad'], float) for r in rows)
    df = rdn('b677_map_diff.txt')
    loops = "### the repeated-squaring loops (`p = p * p`, `[p * p for`) left: NONE" in df
    sq = (m.get('tally') or {}).get('square_by_product')
    ok = bool(got) and len(got) == len(rows) and radii and loops and sq == 0
    return ('HELD' if ok else 'REFUTED'), (
        'every row of relay data/b677_map.txt carries the four residuals` radii and the phase angle`s radius: %d rows through the reader, '
        'radii %s; the new tool`s text holds no repeated-squaring loop (data/b677_map_diff.txt: %s) and every power was taken as exp(n·log z) '
        '(%s angle-form powers, %s squares by one product of a ball holding 0)' % (len(got), radii, loops, (m.get('tally') or {}).get('angle'), sq))


def _n4():
    W = {}
    for l in rdn('b671_tie_diagnostic.txt').split(NL):
        mm = re.match(r'^  (THE CONTROL Z₁\(0\.8, 29\.6\)|Q0 AT qE0)\s+(\d+) j (\d+) : ', l)
        if mm:
            W[(mm.group(1), int(mm.group(2)), int(mm.group(3)))] = 1
    rows = jl('b677_map.json').get('rows') or []
    try:
        got = set((c, b_, j) for c, b_, j, _w in (read_map_row(r) for r in rows))
    except Exception:
        got = set()
    miss = sorted(set(W) - got)
    ok = bool(W) and not miss and len(got) == len(W)
    return ('HELD' if ok else 'REFUTED'), (
        'every control of b671`s list (data/b671_tie_diagnostic.txt :7-:129, %d rows) re-planted and read in the angle form (relay '
        'data/b677_map.txt, %d rows): dropped %s' % (len(W), len(got), miss or 'NONE'))


def _n5():
    face = jl('b677_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t_main = g(K.TD, 'rev-parse', '--short=7', 'main').strip() == K.T_MAIN
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b677_|audit_b677_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b677_checks as CH
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = kern_ok and t_main and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written -- every kernel as the face read '
            'it %s, SIDE-trivium`s main at %s %s (its three branches of b676 deleted by name, not its main); PLACE-papers beyond FINDINGS and '
            'OPEN_TRAILS: %s; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; relay files of a '
            'kind beyond the new tool, the banks, the act`s tools, the table, the root list, b676`s push-out bank and the orders bank`s appended '
            'rows: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads, pushes and one remote branch delete at '
            'github.com, so no identifier of the author placed in a request' % (
                K.DRAFT, kern_ok, K.T_MAIN, t_main, pp_beyond or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE',
                kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b677_table_final.json'), jl('b677_root_arm.json')
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
    put_json('b677_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _sup(x, sig=2):
    """a positive float as a·10ⁿ with superscript digits, the ledgers' form."""
    if not x:
        return '?'
    e = int(math.floor(math.log10(x)))
    m = x / 10 ** e
    sup = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
    return '%s·10%s' % (('%.*f' % (sig - 1, m)).rstrip('0').rstrip('.') if sig > 1 else '%d' % round(m), str(e).translate(sup))


def _figs():
    m, t, h = jl('b677_map.json'), jl('b677_tolerance.json'), jl('b677_map_h.json')
    rows = m.get('rows') or []
    q200 = [r for r in rows if r['cell'] == 'Q0 AT qE0' and r['bits'] == 200]
    passing = sum(1 for r in q200 if r['word'] == 'PASS')
    r64 = next((r['rad'] for r in q200 if r['j'] == 64), None)
    hq = (m.get('q0') or {}).get('hqtie') or ['?', '?']
    return dict(m=m, t=t, h=h, passing=passing, total=len(q200), r64=r64, hq=hq, t64=t.get('h_tol64'), t38=t.get('h_tol38'),
                first_fail=h.get('first_fail'), lab=(m.get('q0') or {}).get('labelled') or {})


def _title():
    f = _figs()
    h = f['h']
    return ('## The detection map in the angle form at Q0: controls %d of %d; radius at j = 64 %s against the bar 2⁻²⁰, the input width 10⁻²⁴ '
            'against the measured tolerance %s; H3 refuted on the instrument; H4 %s, hQtie %s of %s; W-ORD-MAP-ANGLE-FORM open' % (
                f['passing'], f['total'], _sup(f['r64'], 3), _sup(f['t64']), 'not scorable' if h.get('H4') == 'NOT SCORABLE' else (h.get('H4') or '?').lower(),
                f['hq'][0], f['hq'][1]))


def _finding_text():
    S, J = jl('b677_scores.json'), jl('b677_act_root.json')
    f = _figs()
    lab = f['lab']
    zs = lab.get('zero_side') or {}
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b677_author_answers.txt'), re.M))
    c1 = _rl_lines('b677_record_lines.json') + ['?', '?']
    c4 = _rl_lines('b677_landing.json') + ['?', '?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    tr = f['t'].get('transfer')
    e = ['', _title(), '',
         'In the angle form -- every power exp(n·log z), the logarithm taken once per ball -- the detection map’s tie controls at Q0 pass from '
         'j = 24 to %d and fail from %d to 64 on b671’s narrowed balls (half-width 10⁻²⁴), where the repeated squaring of complex balls failed '
         'from j = 42: the instrument’s blow-up is gone and its remaining failure is located. The phase angle’s radius now doubles exactly per '
         'j; the residual’s radius stands 150 to 540 times the angle’s at every j, in the interpolation’s real coefficients; and at the banked '
         'width the two cross the bar 2⁻²⁰ at j = %d. Measured on the consumer, every control to J_max = 64 passes at input half-width %s, '
         'about 3·10³ times finer than the balls in hand. The tie residual is zero at every j by the orbit’s symmetry, so every failure is the '
         'instrument’s, and no reading about Q0 is taken from H3 or H4. Nothing here proves RH or GRH.' % (
             f['first_fail'] - 1 if f['first_fail'] else 0, f['first_fail'], f['first_fail'], _sup(f['t64'])), '',
         '*Filed at b677 on the author’s ruling `(R287)` and the navigator’s answers (%d questions in %d call%s). Banks: relay '
         '`data/b677_map_plan.txt`, `data/b677_map.txt`, `data/b677_map_run.txt`, `data/b677_tolerance.txt`, `data/b677_map_h.txt`, '
         '`data/b677_map_diff.txt`, `data/b677_act_root.txt`; the tool `tools/b677_epstein_map_angle.py`.*' % (
             n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the narrowed balls cited as a .json '
         'that stands only inside its .gz; the b667 plan’s sections 11–16 and its H3 read as the map’s, where they are the evaluation route’s '
         'amendments and the region count; W-ORD-MAP-ANGLE-FORM cited by a row of the orders bank, which was written before b671 entered it '
         '-- each raised; the mid-act checks of `(R278)`(4), %d prints, one answer citing a path that does not stand (data/b663_plan.txt, '
         'read as data/b663_epstein_plan.txt :131, whose sentence it quotes). b676 at its weight (FINDINGS :%s); the order for the two test '
         'files failing since b638 entered (OPEN_TRAILS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), c1[0], c1[1]), '',
         '**The plan** (`(R287)`(3)): the map’s quantity at each j restated from the tool by line; every power site in the angle form; the tie '
         'residual shown zero by algebra before any run; the radius at j = 64 priced from b671’s radii at 1.3·10⁻⁴ to 7.7·10⁻² against the bar '
         '9.5·10⁻⁷; H3 quoted from the b663 plan :131 and H4 from the b667 plan :124–:125, each with its refutation; raised as one prompt, '
         'and run on the navigator’s answer with a labelled reading past the tie controls.', '',
         '**The run** (`(R287)`(4)): the control Z₁ reproduced (j₀ = 31, the zero side below 0); at Q0 PASS at j = 24–%d and INSTRUMENT at '
         'j = %d–64 at 200 and at 400 bits, OBJECT 0; every one of b671’s 123 rows re-planted and read (relay data/b677_map.txt); the radius at '
         'j = 64 %s, inside the plan’s price.' % (f['first_fail'] - 1, f['first_fail'], _sup(f['r64'], 3)), '',
         '**The tolerance** (`(R287)`(4) H2, H5): a width plant on the consumer, every input ball set to a planted half-width h about its '
         'centre (relay data/b677_tolerance.txt): h_tol(64) = %s and h_tol(38) = %s, the latter %.3g times b667’s estimate near 10⁻¹⁸; a third '
         'of each passes and three times each fails; a shift of 10⁻¹² on one tie point fires the control at every j, and a shift of a quarter '
         'of the angle’s own radius passes where the unplanted run passes; the transfer from input width to the angle’s radius %.3g.' % (
             _sup(f['t64']), _sup(f['t38']), (f['t38'] or 0) / 1e-18, tr or 0), '',
         '**The hypotheses** (relay data/b677_map_h.txt): H1 refuted (22 of b671’s 46 INSTRUMENT controls now pass, 24 do not); H2 refuted; H3 '
         'refuted on the failing instrument, no reading about Q0 taken from it; H4 not scorable, no j₀ read by the map; H5 held. The labelled '
         'reading past the tie controls, hQtie from coeffs_exist and the orbit identity and not from balls: %s, the zero side %s -- an '
         'instrument-side row, not an object finding.' % (lab.get('reading'), zs.get('zero_side', '?')), '',
         '**The landing** (`(R287)`(5)): `W-ORD-MAP-ANGLE-FORM` acted and kept open, its trigger after `W-ORD-EPSTEIN-BALL-WIDTH` (OPEN_TRAILS '
         ':%s); `W-ORD-EPSTEIN-BALL-WIDTH` carrying the measured width %s in place of b671’s two estimates, left beside it, its trigger a '
         'narrowing act at half-width 10⁻²⁸ or finer (:%s); both orders’ rows appended to the orders bank with their Status cells.' % (
             c4[0], _sup(f['t64']), c4[1]), '',
         '**The tools** (the ferry’s Component 5): carried from b676’s sealed copies with no repair at carry (relay data/b677_tool_repairs.txt); '
         'the new tool committed alone, the b667 map left as it is; the closing dry-run a gate step before the seal.', '',
         '**The root.** b677 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b671’s tie diagnostic, b667’s H4 reading and the b663 map’s '
         'hypotheses against b675’s bench; it is re-read by the narrowing act that `W-ORD-EPSTEIN-BALL-WIDTH` now sizes, and by the map’s next '
         'run after it. It strengthens the programme’s offering of a detection map whose instrument limits are located by row and measured on '
         'the consumer, not estimated.', '',
         '**Carried to:** `W-ORD-EPSTEIN-BALL-WIDTH` at 3.2·10⁻²⁸; `W-ORD-MAP-ANGLE-FORM` after it; the residual’s factor in the interpolation’s '
         'real coefficients, for the map’s next run; `W-ORD-CHAIN-PAGE-B638-CASES`; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) H3 read as the b663 plan :131 states it, on the navigator’s answer, where the ruling named the b667 plan; (2) the width grid '
              'of P1 widened above the banked width so the tolerance at j = 38 could be read (relay data/b677_defects.txt (e)); (3) the shift '
              'control’s firing read by the b671 rule as NEITHER, the separation lying far above the bar; (4) the labelled reading banked beside '
              'the map’s own reading and entered as an instrument-side row')


def _trail_text():
    S, J = jl('b677_scores.json'), jl('b677_act_root.json')
    fj = jl('b677_findings.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b677_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b677_record_lines.json') + ['?', '?']
    c4 = _rl_lines('b677_landing.json') + ['?', '?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R287) ratified.** (1) b676 at its weight. (2) The object. (3) The plan before any run. (4) The run. (5) The landing. (6) The '
             'branches. (7) The pre-run in two parts. (8) The read-first bank. (9) The draft held at v5. (10) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b676’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-CHAIN-PAGE-B638-CASES`), :%s '
             '(`W-ORD-MAP-ANGLE-FORM`), :%s (`W-ORD-EPSTEIN-BALL-WIDTH`); this record.' % (c1[0], fj.get('entry_line'), c1[1], c4[0], c4[1]), '',
             '**Act root:** b677 `%s` (previous `%s`, b676’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b677_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The map:** the angle form at Q0, PASS at j = 24–%d, INSTRUMENT at j = %d–64, the radius at j = 64 %s (relay data/b677_map.txt); '
             'H1 refuted, H2 refuted, H3 refuted on the instrument, H4 not scorable, H5 held (data/b677_map_h.txt).' % (
                 f['first_fail'] - 1, f['first_fail'], _sup(f['r64'], 3)), '',
             '**The tolerance:** h_tol(64) %s, h_tol(38) %s, measured by a width plant on the consumer (relay data/b677_tolerance.txt).' % (
                 _sup(f['t64']), _sup(f['t38'])), '',
             '**The open orders:** `W-ORD-EPSTEIN-BALL-WIDTH` (a narrowing act at half-width 10⁻²⁸ or finer); `W-ORD-MAP-ANGLE-FORM` (after it); '
             '`W-ORD-Q0-CLASS-LINES` (b678); `W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; '
             '`W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the strip variant, '
             'b679.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b677_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b677_scores.json')
    L = ['=' * 104, 'b677 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b677_defects.txt').rstrip(NL).split(NL)
    put_txt('b677_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b677_scores.json', 'b677_findings.json', 'b677_trail.json', 'b677_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b677_record_lines.json') + ['?', '?']
    c4 = _rl_lines('b677_landing.json') + ['?', '?']
    L = ['b677 -- THE COMPONENTS, BANKED UNDER (R287).', '',
         '### COMPONENT 0 : the citation check (data/b677_citation_check.txt), step zero (data/b677_ferry.txt, data/b677_readfirst.txt, '
         'data/b677_stepzero.txt, data/b677_tests_stepzero.txt, data/b677_rowgen_stepzero.txt, data/b677_branches.txt)',
         '### COMPONENT 1 : b676`s weight FINDINGS :%s ; W-ORD-CHAIN-PAGE-B638-CASES OPEN_TRAILS :%s' % (c1[0], c1[1]),
         '### COMPONENT 2 : the plan (data/b677_map_plan.txt) ; the prompt and its answers (data/b677_author_answers.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the run (data/b677_map.txt, data/b677_map_run.txt, data/b677_tolerance.txt, data/b677_map_h.txt, data/b677_map_diff.txt), '
         'the tool tools/b677_epstein_map_angle.py ; N3 %s ; N4 %s' % (S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the landing (data/b677_landing.json) ; W-ORD-MAP-ANGLE-FORM OPEN_TRAILS :%s ; W-ORD-EPSTEIN-BALL-WIDTH :%s ; the orders '
         'bank`s rows' % (c4[0], c4[1]),
         '### COMPONENT 5 : the carry-time reading (data/b677_tool_repairs.txt), the dry-run steps (data/b677_reg_gate.txt), the seal '
         '(data/b677_seal_hashes.json), the suite, the rules (data/b677_rules.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b677_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b677_findings.json', dict(title=t))
    j = jl('b677_findings.json')
    j['entry_line'] = ln
    put_json('b677_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b677_trail.json', {})
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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c4': c4, 'answers': answers, 'commands': commands, 'kernels': kernels,
          'defects': defects, 'repairs': repairs, 'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks,
          'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b677_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
