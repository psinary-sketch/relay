# -*- coding: utf-8 -*-
"""b675_record.py -- THE ACT'S RECORD TOOL, b675 under (R285).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b675's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b674_record.py (the helpers, the guarded landing, the readers, step zero's rowgen route); new here: the
### branches bank with the remote deletions named apart; the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b675_record.py <route> [dry]`.
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
import b675_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b674_record.py with b675's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b675_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b675_findings.json': dict(entry_line=99999, title='stand-in'),
        'b675_trail.json': dict(line=99999),
        'b675_act_root.json': dict(root='0' * 64, previous='34e0e30f' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b675's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b675_scanfile_%s.md' % tag)
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
    """a scores row: key N1..N5, H1..H6 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text)."""
    if not re.match(r'^(N[1-5]|H[1-6]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
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
    """a row of data/b675_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    run on this host) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b675_rowgen_stepzero.txt."""
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
    L = ['b675 -- STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE AT THE START OF THE REVIEW PASS (b670 rules row 3) (%s)' % utc(), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b675_rowgen_stepzero.txt', L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R285)(3))
def branches(*a):
    """every branch (R285)(3) names, its tip read before any delete, its fate; the remote deletions named apart, each tip read from the
    remote-tracking ref; chi-li-b669's remote tip printed as an ancestor of SIDE-explicit-formula's main e36ea31 before its deletion.
    data/b675_branches.txt (.json); writes nothing else."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for repo, b in K.DELETE_REMOTE:
        tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b).strip()
        merged = ('origin/' + b) in g(repo, 'branch', '-r', '--merged', 'main', '--list', 'origin/' + b)
        rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=merged, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    ci = [r for r in rows if r['branch'] == 'chi-li-b669'][0]
    anc = subprocess.run(['git', '-C', K.KE, 'merge-base', '--is-ancestor', ci['tip'], K.MERGE]).returncode == 0
    L = ['b675 -- STEP ZERO, (R285)(3): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main` (-r for a remote) ; fate.',
         '### Deleted by name in the house form after --merged lists them, one repository per call; no branch the ruling does not name is',
         '### deleted. The remote deletions are the outward writes (R285)(3) names: SIDE-window recut-window-b674 and SIDE-explicit-formula',
         '### chi-li-b669, each by `git push origin --delete <name>` alone in its own call.']
    L += ['  %-24s %-20s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                              r['fate']) for r in rows]
    L += ['', '### chi-li-b669`s remote tip %s (%s), an ancestor of SIDE-explicit-formula`s main %s: %s' % (
        ci['tip'][:12], 'the built tip of b673' if ci['tip'] == K.CHI_LI_TIP else '### NOT b673`S BUILT TIP', K.MERGE[:12], anc),
          '', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d.**' % (
              len(rows), sum(1 for r in rows if r['where'] == 'local'), sum(1 for r in rows if r['where'] == 'remote'),
              sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b675_branches.txt', L)
    put_json('b675_branches.json', dict(at=utc(), rows=rows, chi_li_ancestor_of_main=anc))
    print(NL.join(L[6:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R285)(1)
WH = ('*Appended 2026-10-16 by b675 to b674’s entry (:8851), under `(R285)`(1) -- b674 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b674_closing.txt), ITS COMMITS AS THE CORRIGENDA BANK CORRECTS THEM (relay data/b675_corrigenda.txt):*')
WB = (' “b674 closed: relay 7d432c88, PLACE-papers 4cb90e0, SIDE-window e5b737a v0.5.1; suite 84 of 84; root 34e0e30f0034da57…; 6 prompts '
      'answered; 14 defects” (data/b674_closing.txt :1) -- the head line’s two commits are the pushes before the root (the seal and '
      'Component 2, b674’s defect (l)); the record’s commits are relay 92e003e7 and PLACE-papers 6b95ac8, the closing pushed at relay '
      '27992411 (data/b675_corrigenda.txt row 1). The re-cut: SIDE-window’s rows outside LICENSED/CITED from 6 to 1 of any kind, by b670’s '
      'method 5 to 1 (data/b674_closing.txt :27); the Sawtooth header’s marker at :17 left for the next re-cut of that kernel '
      '(data/b674_cut.txt :28); both runner builds DERIVES, 3dab5f4 before and 22bf840 after, the prints equal line for line (:28-:33), merged '
      'as e5b737a, tag v0.5.1 (:36); the sealed tools agreeing 8 of 8 (:14). The ceiling successor written beside the `(R183)`(3) sentence, '
      'which stands unchanged, at README :127, REGISTRY :962 and FINDINGS :8849, byte-equal (:22); the faces line through the generator '
      '(:23). The entry at FINDINGS :8851, the trail at OPEN_TRAILS :14508; the root 34e0e30f… chained from 4f86a025… over 45 banks; N1–N5 '
      'and S1–S3 held (:52); the mirror mirror-refresh-2026-10-17-b674.zip clean with the root line (:42); the suite 84 of 84 pre-push and '
      'post-push (:157, :159). Fourteen defects (a)–(m) and (e′), the navigator’s (a)–(d) and (e′) as the defects bank letters them '
      '(data/b674_defects.txt :7–:32). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b675_record_lines.json', 'c1', entry=K.B674_ENTRY,
         check=[('FINDINGS.md', K.B674_ENTRY, '## SIDE-window docstrings re-cut'), ('OPEN_TRAILS.md', K.B674_TRAIL, '### b674')], dry=dry)


# ================================================================================ COMPONENT 2: THE HYPOTHESES AT Q0, (R285)(5)
def zeros():
    """the narrowed list, read through its committed .gz: the .gz's sha256 and the JSON inside it compared with b671's hashes bank before any
    row is read; returns (the JSON, the two digests)."""
    import gzip
    import hashlib
    raw = open(os.path.join(D, K.ZEROS_GZ), 'rb').read()
    inner = gzip.decompress(raw)
    hg, hj = hashlib.sha256(raw).hexdigest(), hashlib.sha256(inner).hexdigest()
    if hg != K.ZEROS_GZ_SHA or hj != K.ZEROS_JSON_SHA:
        sys.exit('### THE NARROWED LIST DIFFERS FROM b671`S HASHES BANK: .gz %s, JSON %s -- NOTHING READ' % (hg[:16], hj[:16]))
    return json.loads(inner.decode('utf-8')), hg, hj


def hypotheses(*a):
    """(R285)(5): HStrip (RestBound.lean :40) read against the real part of every off-line ball and its reflection 1 - conj ρ, each with its
    sign relative to 0 and 1, the on-line rows' real part read as the string the bank carries; HCount (:44) read against the count law
    data/b667_epstein_plan.txt pins, and where none is pinned, T-COUNT named with its formula and source and carried as an ASSUMPTION.
    Balls in Arb at 256 bits: σ = [re ± h]. Writes data/b675_hypotheses.txt (.json) alone; no sum is computed here."""
    from flint import arb, ctx
    ctx.prec = 256
    Z, hg, hj = zeros()
    rows = Z['rows']
    on = [r for r in rows if r['kind'] == 'ON']
    off = [r for r in rows if r['kind'] == 'OFF']
    on_half = all(r['re'] == '0.5' for r in on)
    out = []
    for r in off:
        s = arb(r['re'], r['h'])
        for which, x in (('ρ', s), ('1 - conj ρ', 1 - s)):
            pos, below = bool(x > 0), bool(x < 1)
            out.append(dict(idx=r['idx'], point=which, re=x.str(30, radius=True), t=r['im'][:24], above_0=pos, below_1=below,
                            strip=pos and below))
    held = all(o['strip'] for o in out)
    lo = min(out, key=lambda o: float(arb(o['re'].split(' +/-')[0].strip('[')).mid()))
    hi = max(out, key=lambda o: float(arb(o['re'].split(' +/-')[0].strip('[')).mid()))
    kl = [_show(K.KE, K.KREV, K.LEAN[k][0]).split(NL)[K.LEAN[k][1] - 1].strip() for k in ('HStrip', 'HCount', 'A0Q', 'Q0Count')]
    L = ['b675 -- COMPONENT 2, (R285)(5): THE KERNEL`S HYPOTHESES READ AT Q0, BEFORE ANY SUM (%s)' % utc(), '',
         '### rows are hypotheses with their reading and source. The object: relay data/%s (sha256 %s, EQUAL to b671`s hashes bank :3), the JSON '
         'inside it %s (EQUAL to :2); %d rows, ON %d, OFF %d, half-width w = %s; balls in Arb at 256 bits, σ = [re ± h]. The kernel at '
         'SIDE-explicit-formula %s (v0.32), read by git show.' % (K.ZEROS_GZ, hg[:16], hj[:16], len(rows), len(on), len(off), Z['w'], K.KREV), '',
         '== HStrip, as RestBound.lean :40 states it: "%s"' % kl[0],
         '   the on-line rows: %d, every real part the string "0.5" as the bank carries it: %s -- in (0, 1)' % (len(on), on_half),
         '   the off-line balls and their reflections 1 - conj ρ (the orbit member of S5`s exists_dominant_point, Schema/LiConverseCfg.lean :53),',
         '   each real part with its sign relative to 0 and to 1 (rows are points: idx ; point ; Re as a ball ; t ; Re > 0 ; Re < 1):']
    L += ['     %2d  %-11s %-44s t %-24s  > 0 %-5s  < 1 %-5s' % (o['idx'], o['point'], o['re'], o['t'], o['above_0'], o['below_1']) for o in out]
    L += ['   THE CERTIFIED POINTS: %d off-line balls and %d reflections, every real part strictly between 0 and 1: %s; the least %s (idx %d, %s), '
          'the greatest %s (idx %d, %s).' % (len(off), len(off), held, lo['re'], lo['idx'], lo['point'], hi['re'], hi['idx'], hi['point']),
          '   THE STATEMENT`S REACH: HStrip quantifies over every point of the carrier, with no height. The certified list reaches t = 150 alone',
          '   (b667`s region R = [-0.5, 1.5] × [0.5, 150], N(R) = 180 = the list, relay data/b667_epstein_counts.txt :52; P2 Q0Complete, '
          'Schema/EpsteinQ0.lean :100).',
          '   Above 150 two facts bound the reading: (a) no zero of Z_Q at σ ≥ 3/2, at any height -- (3c)`s tail bound is a bound in σ alone,',
          '   |Z_Q(s) - 2| ≤ Z_Q(3/2) - 2 = [1.54841378141857 +/- 1.08e-15] < 2 (relay data/b667_epstein_plan.txt :247-:248, data/b667_epstein_counts.txt',
          '   :34), and by Λ_Q(s) = Λ_Q(1 - s) with Γ zero-free (data/b667_epstein_plan.txt :10) none at σ ≤ -1/2 off the real axis; (b) Q0 has',
          '   class number h(-23) = 3 > 1 (data/b667_epstein_plan.txt :8), and Davenport and Heilbronn (1936) proved that the Epstein zeta function',
          '   of a positive definite binary form of class number above 1 has infinitely many zeros in σ > 1 (J. London Math. Soc. 11; cited, not',
          '   read from a pinned copy) -- above t = 150, since R counts none below it; each such zero ρ and its reflection 1 - conj ρ (σ < 0)',
          '   lie outside the open strip (0, 1).',
          '   THE READING: HStrip HOLDS ON EVERY CERTIFIED POINT (H1 as written, on the balls: HELD) AND FAILS FOR Q0`S CONFIGURATION AS A WHOLE,',
          '   by (b): Q0 lies outside the kernel`s configuration class (R285)(8) names, the bound marked as NOT APPLYING to Q0 at v0.32, the',
          '   sums of (6)-(7) observation alone. The variant hypothesis named for a later act (entered in the plan bank): HStrip on the',
          '   strip (-1/2, 3/2), which (a) proves at Q0 at every height; rest_term_le (Schema/LiRemainder.lean :125) uses the open strip',
          '   through |Re ρ⁻¹| ≤ 1/‖ρ‖² and the lower bound on ‖ρ‖, and its constant changes with the strip. RAISED as one prompt before (6).', '',
          '== HCount, as RestBound.lean :44 states it: "%s"' % kl[1],
          '   a count law for Z_Q pinned in data/b667_epstein_plan.txt: NONE (292 lines; its counts are the region and square counts, == 1, 4, 11).',
          '   T-COUNT, named by (R285)(5): the kernel`s premise P3 at Q0 -- "%s" with "%s" (Schema/EpsteinQ0.lean :104, :108), that is' % (kl[3], kl[2]),
          '   N(t, t + 1) ≤ 10 log(|t| + 3) for every real t, N counting Im in (t, t + 1] with multiplicity; its reason relay data/b663_a0_list.txt',
          '   :6-:9 (the listed points` own A₀ = 1; 10 a round margin for the unlisted zeros above 150, whose count in (t, t + 1] grows like',
          '   (1/π) log t), "stated, not proved; open". CARRIED AS AN ASSUMPTION OF THE BENCH ON THE FACE, NOT AS A THEOREM: every tail bound',
          '   of (6)(ii) and (6)(iv) names it. On the certified points it holds with A₀ = 1 (data/b663_a0_list.txt :5).', '',
          '### ### **HStrip ON THE CERTIFIED POINTS: HELD (%d of %d real parts in (0, 1)) ; HStrip FOR Q0`S CONFIGURATION: FAILS (Davenport-Heilbronn, '
          'above t = 150) ; HCount: T-COUNT ASSUMED (P3, A₀Q = 10) ; THE BOUND AT v0.32: NOT APPLYING TO Q0 ; RAISED BEFORE (6).**' % (
              sum(o['strip'] for o in out), len(out))]
    put_txt('b675_hypotheses.txt', L)
    put_json('b675_hypotheses.json', dict(at=utc(), gz_sha=hg, json_sha=hj, on=len(on), on_half=on_half, off=len(off), points=out,
                                          certified_strip=held, configuration_strip='FAILS (Davenport-Heilbronn 1936, h(-23) = 3)',
                                          t_count='ASSUMED: P3 HCount Z 10'))
    print(NL.join(L[-3:]))


# ================================================================================ COMPONENT 5: THE CLOSING TOOL'S REPAIRS AT CARRY, (R285)(2)
def repairs(*a):
    """data/b675_tool_repairs.txt: rows are repairs with the defect they answer; b674's closing tool read against its seal hash (relay
    data/b674_seal_hashes.json) first; each repair shown by the hunks of the diff against that sealed copy that carry it, and run on real
    banks both ways (the sealed copy's reading beside the repaired one)."""
    import hashlib
    sys.argv = [sys.argv[0]]
    import b675_closing as C
    old, new = os.path.join(T, 'b674_closing.py'), os.path.join(T, 'b675_closing.py')
    seal = (jl('b674_seal_hashes.json').get('tools') or {}).get('b674_closing.py')
    now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
    d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    hunks = re.split(r'(?m)^(?=@@ )', d)[1:]
    pick = lambda keys: [h for h in hunks if any(k in h for k in keys)]   # noqa: E731
    h1, h2 = pick(('def remote_tag', 'remote_tag(')), pick(('VLINE', 'def vline', 'vline('))
    h3, h4 = pick(('def citation_line', 'citation_line()')), pick(('CAPTURES', '_back(', 'IS NOT THE RECORD'))
    # ### (1) the tag rows: SIDE-window's lightweight v0.5.0, its remote line as b674's defect (m) quotes it (refs/tags/v0.5.0 aacb4151584a)
    loc = g(K.WD, 'rev-parse', 'v0.5.0^{commit}').strip()
    planted = {'refs/heads/main': 'x', 'refs/tags/v0.5.0': loc}
    C._REMOTE[K.WD] = planted
    rem_new, kind = C.remote_tag(K.WD, 'v0.5.0')
    rem_old = planted.get('refs/tags/v0.5.0^{}', '')
    # ### (2) the verdict line on b674's prints bank
    pc = rdn('b674_prints_compare.txt')
    m_old = re.search(r'PRINTS BEFORE[^*]*', pc)
    v_new = C.vline(pc)
    # ### (3) the citation line from this act's banks; b674's parenthesis, the seat's text, as its sealed copy carries it
    cl = C.citation_line()
    hand = "(the seven misses raised and answered, the navigator`s (a)-(d) and (e`))" in rd(old)
    # ### (4) the head line on b674's banks (its captures named against the house form) and on b673's (named in it)
    h674, h673 = C.head_line(act='b674'), C.head_line(act='b673')
    L = ['b675 -- COMPONENT 5, (R285)(2): THE CLOSING TOOL`S REPAIRS AT CARRY, AGAINST b674`S SEALED COPY (%s)' % utc(), '',
         '### b674`s sealed copy: tools/b674_closing.py sha256 %s ; the seal`s record %s ; %s' % (now[:16], (seal or '### NONE')[:16],
                                                                                                 'AGREE' if seal == now else '### DIFFER'),
         '### rows are repairs, each with the defect it answers, the diff`s hunks (b674 -> b675) that carry it, and its reading on real banks:', '',
         '  REPAIR 1 -- THE TAG ROWS READ A LIGHTWEIGHT TAG AT ITS OWN LINE. Answers b674 defect (m)(1). Hunks %d:' % len(h1)]
    L += ['    ' + l for h in h1 for l in h.rstrip(NL).split(NL)]
    L += ['  on SIDE-window`s v0.5.0 (local peeled %s; the remote`s line as (m) quotes it, refs/tags/v0.5.0 with no peeled line): the sealed '
          'reading %r -> %s ; the repaired %s (%s) -> %s' % (loc[:12], rem_old, 'AGREE' if loc and loc == rem_old else 'DIFFER', rem_new[:12], kind,
                                                            'AGREE' if loc and loc == rem_new else 'DIFFER')]
    L += ['', '  REPAIR 2 -- A BANK`S VERDICT LINE, NOT ITS TITLE. Answers b674 defect (m)(2). Hunks %d:' % len(h2)]
    L += ['    ' + l for h in h2 for l in h.rstrip(NL).split(NL)]
    L += ['  on relay data/b674_prints_compare.txt: the sealed pattern `PRINTS BEFORE[^*]*` takes %d characters from the title ("%s..."); the '
          'repaired reading takes the verdict line: "%s"' % (len(m_old.group(0)) if m_old else 0, (m_old.group(0)[:60] if m_old else ''), v_new)]
    L += ['', '  REPAIR 3 -- THE CITATION LINE READ FROM THE BANKS, NO CREDIT BY THE SEAT`S HAND. Answers b674 defect (m)(3). Hunks %d:' % len(h3)]
    L += ['    ' + l for h in h3 for l in h.rstrip(NL).split(NL)]
    L += ['  the sealed copy carries the hand-written parenthesis: %s ; the repaired line on this act`s banks: %s' % (hand, cl)]
    L += ['', '  REPAIR 4 -- THE CAPTURES IN b673`S FORM, THE HEAD LINE READING THE RECORD`S CAPTURE WITH ITS BRANCH AND ITS TIP`S SUBJECT. Answers',
          '  b674 defect (l). Hunks %d:' % len(h4)]
    L += ['    ' + l for h in h4 for l in h.rstrip(NL).split(NL)]
    L += ['  the repaired head line on b674`s banks (captures named against the form): %s' % h674,
          '  the repaired head line on b673`s banks (captures named in the form): %s' % h673]
    ok1 = loc and rem_new == loc and rem_old != loc
    ok2 = bool(m_old) and 'EQUAL LINE FOR LINE True' in v_new and len(m_old.group(0)) > len(v_new)
    ok3 = hand and 'the misses as the bank lists them' in cl
    ok4 = h674.count('IS NOT THE RECORD`S CAPTURE') == 2 and '57fdb813' in h673 and 'f755f99' in h673
    L += ['', '### ### **REPAIRS 4 ; THE SEALED COPY %s ; HUNKS %d, %d, %d AND %d ; THE LIGHTWEIGHT TAG AGREES %s ; THE VERDICT LINE READ %s ; THE '
          'CITATION LINE FROM THE BANKS %s ; THE CAPTURES CHECKED BOTH WAYS %s.**' % ('AGREE' if seal == now else '### DIFFER', len(h1), len(h2), len(h3),
                                                                                   len(h4), bool(ok1), bool(ok2), bool(ok3), bool(ok4))]
    put_txt('b675_tool_repairs.txt', L)
    print(L[-1])


# ================================================================================ THE AUTHOR'S ANSWERS (b674's route, carried)
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
    """data/b675_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
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
    head = ['### b675 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a) for s, a in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b675_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b675_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b674's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
BENCH_SIGNS = ('NEG', 'NONNEG', 'UNDECIDED')


def read_bench_row(r):
    """a row of data/b675_li_bench.json: n (an int), P and P + U as Arb ball strings, U, the sign (one of BENCH_SIGNS), P's radius (a float);
    returns (n, sign)."""
    if not isinstance(r, dict) or not isinstance(r.get('n'), int) or r.get('sign') not in BENCH_SIGNS or '+/-' not in (r.get('P') or '') \
            or '+/-' not in (r.get('PU') or '') or not isinstance(r.get('rad'), float) or not r.get('U'):
        raise ValueError('bench row of another shape: %r' % (r,))
    return r['n'], r['sign']


def read_runner_row(r):
    """a row of data/b674_runner_rows.json, the last merged run's bank (the standing runner arms read it, no runner this act): SIDE-window,
    a label (before or after), a 40-hex ref, a run id, a gate; returns (label, gate). Carried from b674_record.py :606-:611."""
    if not isinstance(r, dict) or r.get('kernel') != 'SIDE-window' or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


READERS += ['read_bench_row', 'read_runner_row']


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
    L = ['b675 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1) AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; MOVE OR DELETE COMMANDS %d.**' % (
        len(rows), len(hits), len(lean), len(mv))]
    put_txt('b675_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b675_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window']      # ### SIDE-window beside b641's thirteen (its branches deleted at step zero)


def kernels(*a):
    ks = _kerns()
    put_json('b675_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b675_defects.txt').split(NL)
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
    t = rdn('b675_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b675_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b675_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b675_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b675_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b675_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b675_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b675'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b675_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b675_ra_') as tmp:
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
    L = ['b675 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b675_root_arm.txt', L)
    put_json('b675_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b675 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b675_table_final.txt', L)
    put_json('b675_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b675_registration_2026-10-16.txt'
FACE = os.path.join(D, 'b675_registration_2026-10-16.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b675_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b675_regspec.py')], 'b675_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b675_satisfiable.json', '--emit', 'b675'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b675_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b675_census_stepzero.txt'), ('b327_faces_census.py', 'b675_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b675_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b675'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b675_reg_gate.txt', 'data/b675_reg_termscan.txt', 'data/b675_regspec_run.txt', 'data/audit_b675_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3), (H1)-(H6)
# ### carried from b674_record.py :846-:1086 by the Edit tool, every predicate re-written against (R285)'s expectations and this act's banks
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
HK = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6')
SCORE_KEYS = NK + SK + HK
N5_RELAY_DATA = ('act_roots.txt', 'b674_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b675 — lane two, act one hundred and two, the research act under (R285): the Li index at Q0, Q0 outside the kernel’s '
            'configuration class at v0.32; the bench as observation; the closing tool repaired at carry')


def _calls():
    return jl('b675_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _epoch(ts):
    import calendar
    return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')) if ts else None


def _prompt_of(header):
    """the prompt the answers bank carries under `header`: (its text, its call's time as an epoch), or (None, None)."""
    L = rdn('b675_author_answers.txt').split(NL)
    ts = None
    for i, l in enumerate(L):
        m = re.match(r'^### CALL tool-use id \S+ \(session \S+, transcript line \S+, (\S+)\)', l)
        if m:
            ts = m.group(1)
        if l.startswith('### PROMPT ') and ('(%s):' % header) in l:
            j = i + 1
            while j < len(L) and not L[j].startswith(('### PROMPT ', 'RESULT ')):
                j += 1
            return NL.join(L[i:j]), _epoch(ts)
    return None, None


PLAN_SOURCES = (':180-:181', ':192', ':165-:166', ':183-:191', ':222', ':295', ':27', 'Schema/EpsteinQ0.lean :104, :108',
                'data/b667_epstein_plan.txt :247-:248', 'data/b667_epstein_counts.txt :52')


def _bench():
    return jl('b675_li_bench.json'), jl('b675_li_controls.json'), jl('b675_li_constants.json'), jl('b675_hypotheses.json')


def _n1():
    cm = jl('b675_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b675_commands.txt, %d commands read); no runner dispatched '
        'this act; the kernel read by git show alone' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('rows') or [])))


def _n2():
    H = jl('b675_hypotheses.json')
    plan, plan_t = _prompt_of('The plan')
    hs, hs_t = _prompt_of('HStrip at Q0')
    C = jl('b675_li_constants.json')
    h_at, c_at = _epoch(H.get('at')), _epoch(C.get('at'))
    pl = rdn('b675_li_plan.txt')
    srcs = [s_ for s_ in PLAN_SOURCES if s_ in pl]
    ok = len(H.get('points') or []) == 34 and H.get('off') == 17 and h_at and hs_t and plan_t and c_at and h_at < hs_t < plan_t < c_at \
        and len(srcs) == len(PLAN_SOURCES)
    return ('HELD' if ok else 'REFUTED'), (
        'the 17 off-line real parts and their 17 reflections printed from the balls at %s (relay data/b675_hypotheses.txt), raised in the HStrip '
        'prompt at %s; the plan`s constants each with its source (%d of %d named sources found in relay data/b675_li_plan.txt) raised in the '
        'plan prompt at %s; the first sum (the bench`s part 1) at %s: the order %s' % (
            H.get('at'), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(hs_t)) if hs_t else '### NONE', len(srcs), len(PLAN_SOURCES),
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(plan_t)) if plan_t else '### NONE', C.get('at'), bool(ok)))


def _n3():
    B, _c, _k, _h = _bench()
    rows = B.get('rows') or []
    try:
        got = [read_bench_row(r) for r in rows]
    except Exception:
        got = []
    tool = rd(os.path.join(T, 'b675_li_bench.py'))
    exp_form = '(L * n).exp()' in tool and '** n' not in tool.split('def P(')[1].split('def ')[0]
    ok = bool(got) and len(got) == len(rows) and all(r['rad'] > 0 for r in rows) and exp_form and B.get('undecided') == 0
    return ('HELD' if ok else 'REFUTED'), (
        'every banked P_n a ball with its radius (%d rows through the reader, radius at the largest n %s); every power exp(n·log z) '
        '(tools/b675_li_bench.py `P`: %s); the comparison P_n + U_n against 0 with U_n inside it and the radius beside it, UNDECIDED %s' % (
            len(got), B.get('rad_hi'), exp_form, B.get('undecided')))


def _n4():
    _b, X, _k, _h = _bench()
    c2p, c2, h6 = X.get('C2prime') or {}, X.get('C2') or {}, X.get('H6') or {}
    o = (h6.get('order_onsets') or {})
    ok = c2p.get('neg_count') == 0 and c2p.get('undecided') == 0 and c2.get('least_neg') and o.get('n_star') and o['n_star'][0] < o['n_star'][1] \
        and o.get('n_obs') and o['n_obs'][0] < o['n_obs'][1]
    return ('HELD' if ok else 'REFUTED'), (
        'C2′ (the instrument): NEG %s, UNDECIDED %s over [1, %s]; C2 as written (an object reading): the least NEG %s, predicted from idx 1 %s; '
        'H6: the onsets ordered, n* %s and n_obs %s (relay data/b675_li_controls.txt)' % (
            c2p.get('neg_count'), c2p.get('undecided'), (c2p.get('range') or ['', ''])[1], c2.get('least_neg'),
            (c2.get('predicted_onset_idx1') or {}).get('n'), o.get('n_star'), o.get('n_obs')))


def _n5():
    face = jl('b675_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ke_main = g(K.KE, 'rev-parse', 'main').strip() == K.MERGE
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b675_|audit_b675_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b675_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and ke_main and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written: every kernel as the face read it '
            '%s, SIDE-explicit-formula`s main at %s %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; standing arms added: %s (the act`s '
            'arms over its own banks %d); sealed tools not agreeing %s; relay files of a kind beyond the banks, the act`s tools, the table, the '
            'root list and b674`s push-out bank: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes and '
            'the two remote branch deletions (R285)(3) names at github.com, and one web search whose query is the theorem`s words alone, so no '
            'identifier of the author placed in a request' % (
                K.DRAFT, others_ok, K.MERGE[:7], ke_main, pp_beyond or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE',
                kinds_beyond or 'NONE', pat or 'NONE'))


def _h():
    B, X, C, H = _bench()
    w, h6 = B.get('window') or {}, X.get('H6') or {}
    c2p = X.get('C2prime') or {}
    b, b6 = C.get('bench') or {}, C.get('h6') or {}
    return {
        'H1': ('REFUTED AS HStrip AT Q0; HELD ON THE BALLS', 'every off-line ball`s real part and its reflection`s strictly in (0, 1), %d of 34 (relay '
               'data/b675_hypotheses.txt); HStrip for Q0`s configuration fails above t = 150 (Davenport-Heilbronn, h(-23) = 3): Q0 outside the '
               'kernel`s class at v0.32, the landing of (R285)(8) the navigator`s answer took' % sum(1 for p in H.get('points') or [] if p.get('strip'))),
        'H2': ('HELD', 'n* = %s printed with its constants, each with its Lean line: R %s, s %s, K %s, C %s (relay data/b675_li_constants.json, '
               'data/b675_li_readings.txt (H2)) -- the v0.32 bound`s onset, were HStrip to hold' % (b.get('n_star'), b.get('R'), b.get('s'), b.get('K'), b.get('C'))),
        'H3': ('REFUTED AT EVERY n; READ ALONG THE SUBSEQUENCE', 'over [%s, %s]: NEG %s of %s, the least NEG %s, the longest runs %s, UNDECIDED %s '
               '-- an observation; the clause at every n the navigator`s (relay data/b675_defects.txt (a))' % (
                   (w.get('window') or ['', ''])[0], (w.get('window') or ['', ''])[1], w.get('neg_count'), w.get('n'), w.get('least_neg'), w.get('longest'),
                   w.get('undecided'))),
        'H4': ('HELD' if B.get('n_obs') and B.get('n_star') and B['n_obs'] <= B['n_star'] else 'REFUTED',
               'n_obs %s ≤ n* %s, an observation; λ_n < 0 at n_obs under T-COUNT' % (B.get('n_obs'), B.get('n_star'))),
        'H5': ('HELD' if c2p.get('neg_count') == 0 and c2p.get('undecided') == 0 else 'REFUTED',
               'read on C2′ (the navigator`s answer on the control): NEG %s, UNDECIDED %s' % (c2p.get('neg_count'), c2p.get('undecided'))),
        'H6': ('HELD' if h6.get('n_star') and h6.get('n_obs') else 'REFUTED', 'n*′ %s (s′ %s, C′ %s), n_obs′ %s; the orderings %s' % (
            h6.get('n_star'), b6.get('s'), b6.get('C'), h6.get('n_obs'), h6.get('order_onsets'))),
    }


def scores(*a):
    TF, RA = jl('b675_table_final.json'), jl('b675_root_arm.json')
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
    S.update(_h())
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:600]))
    if 'dry' in a:
        return
    put_json('b675_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    B = jl('b675_li_bench.json')
    w = B.get('window') or {}
    return ('## The Li index at Q0: HStrip fails for the configuration, held on the 34 certified real parts; the v0.32 bound’s onset, were '
            'HStrip to hold, n* = %s; the certified onset n_obs = %s; P_n + U_n negative at %s of %s n over [n*, n* + 200]; T-COUNT assumed' % (
                B.get('n_star', '?'), B.get('n_obs', '?'), w.get('neg_count', '?'), w.get('n', '?')))


def _finding_text():
    S, J = jl('b675_scores.json'), jl('b675_act_root.json')
    B, X, C, H = _bench()
    w, h6, c2p, c2 = B.get('window') or {}, X.get('H6') or {}, X.get('C2prime') or {}, X.get('C2') or {}
    b = C.get('bench') or {}
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b675_author_answers.txt'), re.M))
    c1 = _rl_lines('b675_record_lines.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'Q0’s certified zeros give its Li coefficient a certified sign: λ_n < 0 at n = %s, the least such n, and at runs of n after it '
         'as the sign follows the dominant pair’s angle, under the count law T-COUNT, which is assumed; '
         'the kernel’s composition bound at v0.32 does not apply to Q0, whose configuration leaves the open strip above t = 150 '
         '(Davenport–Heilbronn), so its onset n* = %s is printed as the bound’s, were HStrip to hold, and tests nothing. Nothing here proves '
         'RH or GRH.' % (B.get('n_obs', '?'), B.get('n_star', '?')), '',
         '*Filed at b675 on the author’s ruling `(R285)` and the navigator’s answers (%d questions in %d calls). Banks: relay '
         '`data/b675_hypotheses.txt`, `data/b675_li_plan.txt`, `data/b675_li_bench.txt`, `data/b675_li_controls.txt`, '
         '`data/b675_li_readings.txt`, `data/b675_tool_repairs.txt`, `data/b675_rules.txt`, `data/b675_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and each raised before the component '
         'citing it; the mid-act checks of `(R278)`(4), %d prints, the last %s of %s OK. b674 at its weight, its closing’s head line quoted and '
         'its commits corrected by relay data/b675_corrigenda.txt (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), mids[-1][1] if mids else '?',
             mids[-1][0] if mids else '?', c1[0]), '',
         '**The hypotheses** (`(R285)`(5)): HStrip (RestBound.lean :40) holds on every certified point -- the 17 off-line balls and their '
         'reflections, real parts from 0.0467 to 0.9533 -- and fails for Q0’s configuration as a whole: h(−23) = 3, and an Epstein zeta '
         'function of class number above 1 has infinitely many zeros in σ > 1 (Davenport–Heilbronn 1936), above t = 150. HCount (:44) has no '
         'count law pinned in b667’s plan; T-COUNT is the kernel’s premise P3, HCount Z 10 (Schema/EpsteinQ0.lean :104, :108), assumed. '
         'The (3c) tail bound puts every zero in −1/2 < σ < 3/2 at every height.', '',
         '**The plan** (`(R285)`(6)): every constant traced to its Lean line before any sum; the proof’s C = 2(2 + 2(1 + s)²)·Σ m/(1 + |γ|²) '
         '(LiRemainder :180–:181), s as the proof chooses it (LiConverseCfg :192); U_n an inequality on (−1/2, 3/2) through the kernel’s '
         'own identity one_sub_pow_expand (:27) and T-COUNT.', '',
         '**The bench** (`(R285)`(7)): P_n over the 360 certified points in Arb balls at 256 bits, every power exp(n·log z); n* = %s (R %s, '
         's %s, C %s); n_obs = %s; over [n*, n* + 200] NEG at %s of %s n, the least %s, the sign following 2cos(nθ) -- the composition bounds '
         'λ_n only along V4’s subsequence, and the window reads it there.' % (B.get('n_star', '?'), (b.get('R') or '?')[:24], (b.get('s') or '?')[:24],
                                                                              (b.get('C') or '?')[:22], B.get('n_obs', '?'), w.get('neg_count', '?'),
                                                                              w.get('n', '?'), w.get('least_neg', '?')), '',
         '**The controls**: C2′, every off-line orbit on the line, NEG %s and UNDECIDED %s -- the instrument as algebra requires; C2 as written, '
         'an object reading, NEG from %s, idx 1’s term predicting %s; H6, the dominant pair removed, n*′ = %s and n_obs′ = %s, both onsets '
         'later than the bench’s.' % (c2p.get('neg_count', '?'), c2p.get('undecided', '?'), c2.get('least_neg', '?'),
                                      (c2.get('predicted_onset_idx1') or {}).get('n', '?'), h6.get('n_star', '?'), h6.get('n_obs', '?')), '',
         '**The closing tool** (`(R285)`(2)): carried from b674’s sealed copy with four repairs at carry -- the lightweight tag read at its own '
         'line, a bank’s verdict line read and not its title, the citation line read from the banks, the record’s captures checked by '
         'branch and tip -- each run both ways on real banks (relay data/b675_tool_repairs.txt); dry-run as a gate step before the seal.', '',
         '**The root.** b675 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act reads b673’s composition at Q0 and b671’s narrowed balls, and b667’s (3c) '
         'bound in σ alone; it is re-read by b677’s research act on the map’s angle form, which narrows the same balls, and by a later act on '
         'the variant hypothesis. It strengthens the programme’s offering of certified objects against which compiled theorems are read: '
         'Q0’s Li coefficient is now certified negative at a named n under one stated assumption, and the kernel’s class is read against '
         'the object before its bound is applied.', '',
         '**Carried to:** the variant hypothesis HStrip on (−1/2, 3/2) and its question, which of V5’s steps use the strip’s width (relay '
         'data/b675_li_plan.txt section 7), to a later act; T-COUNT, assumed; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero beyond the certified list.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) ρ1 of S5’s by_contra fixed at qE0, so s = (s1 + R)/2 with s1 = r (relay data/b675_li_plan.txt section 2 (ii)); (2) U_n’s count '
              'over the unit intervals from k = 149 with each interval’s far-end bound (section 2 (iv)); (3) C2’s predicted onset read by the '
              'sufficient rule R′ⁿ > 358 (relay data/b675_li_controls.txt); (4) the act’s date taken as the author’s, 2026-10-16, while UTC '
              'passed 2026-10-17 during the act')


def _trail_text():
    S, J = jl('b675_scores.json'), jl('b675_act_root.json')
    fj = jl('b675_findings.json')
    B, X, C, H = _bench()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b675_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b675_record_lines.json')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R285) ratified.** (1) b674 at its weight, the head line’s commits corrected in a corrigenda bank. (2) The closing tool’s three '
             'readings repaired at carry and its captures named. (3) The branches. (4) The object. (5) The hypotheses read at Q0. (6) The plan. '
             '(7) The bench. (8) The landing. (9) The read-first bank. (10) The draft held at v5. (11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b674’s weight), :%s (the entry); this record.' % (c1[0] if c1 else '?', fj.get('entry_line')), '',
             '**Act root:** b675 `%s` (previous `%s`, b674’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b675_author_answers.txt); none after the root.' % (n_ans, len(_calls())), '',
             '**The bench:** n* = %s (were HStrip to hold), n_obs = %s, the window NEG %s of %s; C2′ NEG %s; H6 n*′ = %s, n_obs′ = %s; T-COUNT '
             'assumed (P3).' % (B.get('n_star'), B.get('n_obs'), (B.get('window') or {}).get('neg_count'), (B.get('window') or {}).get('n'),
                               (X.get('C2prime') or {}).get('neg_count'), (X.get('H6') or {}).get('n_star'), (X.get('H6') or {}).get('n_obs')), '',
             '**The open orders:** `W-ORD-MAP-ANGLE-FORM` (b677); `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; '
             '`W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; the variant '
             'hypothesis HStrip on (−1/2, 3/2) to a later act.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b675_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b675_scores.json')
    L = ['=' * 104, 'b675 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b675_defects.txt').rstrip(NL).split(NL)
    put_txt('b675_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b675_scores.json', 'b675_findings.json', 'b675_trail.json', 'b675_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b675_record_lines.json') + ['?']
    L = ['b675 -- THE COMPONENTS, BANKED UNDER (R285).', '',
         '### COMPONENT 0 : the citation check (data/b675_citation_check.txt), step zero (data/b675_ferry.txt, data/b675_readfirst.txt, '
         'data/b675_corrigenda.txt, data/b675_stepzero.txt, data/b675_tests_stepzero.txt, data/b675_rowgen_stepzero.txt, data/b675_branches.txt)',
         '### COMPONENT 1 : b674`s weight FINDINGS :%s, its commits as data/b675_corrigenda.txt corrects them' % c1[0],
         '### COMPONENT 2 : the hypotheses at Q0 (data/b675_hypotheses.txt) ; H1 %s' % S['H1'][0],
         '### COMPONENT 3 : the plan (data/b675_li_plan.txt), raised before any sum ; N2 %s' % S['N2'][0],
         '### COMPONENT 4 : the bench (data/b675_li_bench.txt), the controls (data/b675_li_controls.txt), the readings (data/b675_li_readings.txt) ; '
         'N3 %s ; N4 %s' % (S['N3'][0], S['N4'][0]),
         '### COMPONENT 5 : the closing tool`s repairs (data/b675_tool_repairs.txt), the rules (data/b675_rules.txt), the dry-run steps '
         '(data/b675_reg_gate.txt), the seal (data/b675_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b675_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b675_findings.json', dict(title=t))
    j = jl('b675_findings.json')
    j['entry_line'] = ln
    put_json('b675_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b675_trail.json', {})
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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'hypotheses': hypotheses, 'answers': answers, 'repairs': repairs,
          'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root, 'root_arm': root_arm, 'table_final': table_final,
          'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail,
          'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b675_record.py %s' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
