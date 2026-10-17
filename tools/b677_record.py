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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c4': c4}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b677_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
