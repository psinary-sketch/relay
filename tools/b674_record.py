# -*- coding: utf-8 -*-
"""b674_record.py -- THE ACT'S RECORD TOOL, b674 under (R284).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b674's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b673_record.py (the helpers, the guarded landing, the readers, the answers route); new here: step zero's
### rowgen and constellation reading (b670's route, carried) and the branches bank; the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b674_record.py <route> [dry]`.
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
import b674_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b673_record.py with b674's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b674_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b674_findings.json': dict(entry_line=99999, title='stand-in'),
        'b674_trail.json': dict(line=99999),
        'b674_act_root.json': dict(root='0' * 64, previous='4f86a025' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
        'b674_mirror.json': dict(zip='stand-in', manifest_md5='0' * 32),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b674's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b674_scanfile_%s.md' % tag)
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
    """a row of data/b674_branches.json: a repository, a branch, its tip (40 hex) and its fate (one of BRANCH_FATES); returns (branch, fate)."""
    if not isinstance(r, dict) or not r.get('repo') or not r.get('branch') or not re.match(r'^[0-9a-f]{40}$', r.get('tip') or '') \
            or r.get('fate') not in BRANCH_FATES:
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
    run on this host) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b674_rowgen_stepzero.txt."""
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
    L = ['b674 -- STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE AT THE START OF THE REVIEW PASS (b670 rules row 3) (%s)' % utc(), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b674_rowgen_stepzero.txt', L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R284)(6))
def branches(*a):
    """every branch (R284)(6) names, its tip read before any delete, its fate; chi-li-b669's tip banked beforehand and its merge into
    SIDE-explicit-formula's main at e36ea31 read. data/b674_branches.txt (.json); writes nothing else."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, tip=tip, merged=merged, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    ci = [r for r in rows if r['branch'] == 'chi-li-b669'][0]
    anc = subprocess.run(['git', '-C', K.KE, 'merge-base', '--is-ancestor', ci['tip'], K.MERGE]).returncode == 0
    L = ['b674 -- STEP ZERO, (R284)(6): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; tip ; listed by `git branch --merged main` ; fate. Deleted by name in the house form after',
         '### --merged lists them, one repository per call; no branch the ruling does not name is deleted.']
    L += ['  %-32s %-20s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['tip'], r['merged'], r['fate']) for r in rows]
    L += ['', '### chi-li-b669`s tip %s (%s), an ancestor of SIDE-explicit-formula`s merge %s: %s' % (
        ci['tip'][:12], 'the built tip of b673' if ci['tip'] == K.CHI_LI_TIP else '### NOT b673`S BUILT TIP', K.MERGE[:12], anc),
          '', '### ### **BRANCHES %d ; MERGED %d ; TO BE DELETED %d.**' % (len(rows), sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b674_branches.txt', L)
    put_json('b674_branches.json', dict(at=utc(), rows=rows, chi_li_ancestor_of_merge=anc))
    print(NL.join(L[4:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R284)(1)-(2)
WH = ('*Appended 2026-10-16 by b674 to b673’s entry (:8819), under `(R284)`(1) and the navigator’s answer on the weight-line misses -- b673 '
      'AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b673_closing.txt):*')
WB = (' “b673 closed: relay 57fdb813, PLACE-papers f755f99, SIDE-explicit-formula e36ea31 v0.32; suite 84 of 84; root 4f86a025…; 7 prompts '
      'answered; 16 defects” (data/b673_closing.txt :1); the closing pushed and read back at relay 6f98c458 (data/b673_closing_push_out.txt '
      ':5); the sealed tools agreeing 8 of 8 (:14); four runs at four tree states, 516803e, b1d4342, 921fb71 and 5050a46 (:24), one dispatch '
      'per tree state (data/b673_rules.txt row 1); the landing DECLARATIONS 29 ; DERIVES 29 (:25); the walk on S5 DECLARATIONS REACHED 254 ; '
      'ζ-NAMING 0 ; THE CONTROL 1 (:26); the hypotheses with H5 held through rh_equiv_mathlib and refuted as text (:53), read as held by '
      '`(R284)`(2); the mirror mirror-refresh-2026-10-16-b673.zip clean on all three clauses with the root line (:56); the suite 84 of 84 '
      'pre-push and post-push (:166-:169); the foreground pre-run in 396 s replacing the detached run the host stopped (relay '
      'data/b673_registration_2026-10-16.txt); sixteen defects (a)-(p), the navigator’s (b)-(e), (g) and (h). Nothing deposited.')
DH = ('*Appended 2026-10-16 by b674 beneath b673’s discharge line (:14478), under `(R284)`(2) -- **`W-ORD-LI-CONVERSE-NATIVE`**, THE '
      'DISCHARGE ON H5 THROUGH rh_equiv_mathlib:*')
DB = (' H5 through rh_equiv_mathlib: the native converse li_nonneg_imp_rh_native and the vendored positivity_implies_RH conclude the two '
      'sides of that bridge, equal as propositions through it and unequal as text (relay data/b673_h5.txt :17-:23); reading (iii) of b673’s '
      'face confirmed and not struck, and the discharge stands on it. The faces page’s drafted line on unequal converses (relay '
      'data/b673_landing.txt :58-:60) is the record of the text side.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL), ('OPEN_TRAILS.md', DH, NL + DH + DB + NL)], 'b674_record_lines.json', 'c1', entry=K.B673_ENTRY,
         check=[('FINDINGS.md', K.B673_ENTRY, '## V4 DERIVES and V5 DERIVES'), ('OPEN_TRAILS.md', K.B673_TRAIL, '### b673'),
                ('OPEN_TRAILS.md', K.DISCHARGE, '`W-ORD-LI-CONVERSE-NATIVE`')], dry=dry)


# ================================================================================ COMPONENT 2: THE TWO DRAFTS, WRITTEN ON THE AUTHOR'S WORD ((R284)(3))
SUP = re.compile(r"Supportable[^*]*?: \*(.+?)\*")                                       # ### b670_record.py :791, unchanged
PLACED = re.compile(r"placed at README\.md :(\d+) and REGISTRY\.md :(\d+): \*(.+?)\*")   # ### b670_record.py :792, unchanged
NEW_SITES = (('README.md', 127), ('REGISTRY.md', 962))
FACES_PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'


def _placement(f, ln):
    l = rd(os.path.join(PP, f)).split(NL)[ln - 1]
    m = (PLACED if f == 'FINDINGS.md' else SUP).search(l)
    s = (m.group(3) if f == 'FINDINGS.md' else m.group(1)) if m else None
    import hashlib
    return l, s, hashlib.sha256(s.encode('utf-8')).hexdigest() if s else None


def _successor():
    rows = [_placement(f, n) for f, n in NEW_SITES]
    if not all("`(R284)`(3)" in l and s for l, s, _h in rows) or len(set(h for _l, _s, h in rows)) != 1:
        sys.exit('### README :127 AND REGISTRY :962 DO NOT CARRY ONE (R284)(3) SENTENCE -- NOTHING WRITTEN')
    return rows[0][1]


PH = ('*Appended 2026-10-16 by b674 to the ceiling’s χ-sentence record (:6354), under `(R284)`(3) and the author’s word on it -- THE CEILING '
      'SENTENCE’S SUCCESSOR, the author’s sentence,')


def c2(*a):
    dry = 'dry' in a
    s = _successor()
    body = (' placed at README.md :%d and REGISTRY.md :%d: *%s* The (R183)(3) sentence it stands beside stays at README.md :125, REGISTRY.md '
            ':960 and here at :6354; the ceiling “RH reduced to a single located clause, reduction machine-verified” stays where it stands, at '
            'README.md :106, unwritten.' % (NEW_SITES[0][1], NEW_SITES[1][1], s))
    land([('FINDINGS.md', PH, NL + PH + body + NL)], 'b674_record_lines_c2.json', 'c2', check=[('FINDINGS.md', 6354, '`(R183)`(3)')], dry=dry)


def ceilingdiff(*a):
    """data/b674_ceiling_diff.txt: rows are sites with before (PLACE-papers at the act's start) and after (the working tree): the (R183)(3)
    sentence at its three placements and the successor at its three, each by its own delimiters, sha256 and bytes; the byte-equality of
    each three-site set printed."""
    import hashlib
    fl = jl('b674_record_lines_c2.json').get('lines') or []
    fline = fl[0]['line'] if fl else None
    if not fline:
        sys.exit('### THE FINDINGS PLACEMENT IS NOT LANDED -- RUN c2 FIRST -- NOTHING WRITTEN')
    rows = []
    for label, f, n_before, n_after in (('(R183)(3)', 'README.md', 125, 125), ('(R183)(3)', 'REGISTRY.md', 960, 960), ('(R183)(3)', 'FINDINGS.md', 6354, 6354),
                                        ('(R284)(3)', 'README.md', None, 127), ('(R284)(3)', 'REGISTRY.md', None, 962), ('(R284)(3)', 'FINDINGS.md', None, fline)):
        before = None
        if n_before:
            old = (_show(PP, K.PRE_PP, f) or '').split(NL)[n_before - 1]
            m = (PLACED if f == 'FINDINGS.md' else SUP).search(old)
            sb = (m.group(3) if f == 'FINDINGS.md' else m.group(1)) if m else None
            before = (len(sb.encode('utf-8')), hashlib.sha256(sb.encode('utf-8')).hexdigest()) if sb else None
        _l, sa, ha = _placement(f, n_after)
        rows.append(dict(sentence=label, site='%s :%s' % (f, n_after), before=before, after=(len(sa.encode('utf-8')), ha) if sa else None))
    eq = dict((lab, len(set(r['after'][1] for r in rows if r['sentence'] == lab and r['after'])) == 1 and
               all(r['after'] for r in rows if r['sentence'] == lab)) for lab in ('(R183)(3)', '(R284)(3)'))
    kept = all(r['before'] == r['after'] for r in rows if r['sentence'] == '(R183)(3)')
    L = ['b674 -- COMPONENT 2, (R284)(3): THE CEILING`S SITES BEFORE AND AFTER (%s)' % utc(), '',
         '### rows are sites: the sentence ; the site ; before (PLACE-papers %s, bytes and sha256 of the sentence by its own delimiters, b670`s) ; '
         'after (the working tree)' % K.PRE_PP]
    L += ['  %-10s %-18s before %-80s after %s' % (r['sentence'], r['site'], ('%d bytes %s' % r['before']) if r['before'] else 'ABSENT',
                                                  ('%d bytes %s' % r['after']) if r['after'] else '### ABSENT') for r in rows]
    L += ['', '### ### **THE (R183)(3) SENTENCE UNCHANGED AT ITS THREE SITES %s ; BYTE-EQUAL %s ; THE SUCCESSOR BYTE-EQUAL AT ITS THREE SITES %s.**' % (
        kept, eq['(R183)(3)'], eq['(R284)(3)'])]
    put_txt('b674_ceiling_diff.txt', L)
    put_json('b674_ceiling_diff.json', dict(at=utc(), rows=rows, kept=kept, equal=eq))
    print(NL.join(L[3:]))


def faces(*a):
    """the faces page re-emitted through its generator from relay data/b674_nodes_zeta.txt and b643's banked probe output (`--from-output`,
    no elaboration), into PLACE-papers; the control first: b649's list into the scratchpad, its sha256 against the committed page's. The diff
    of the written page against the committed one banked by kind. data/b674_faces_diff.txt (.json)."""
    import hashlib
    sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()   # noqa: E731
    page = os.path.join(PP, FACES_PAGE)
    run_ = lambda nodes, out: subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', nodes, '--probe-dir',   # noqa: E731
                                              os.path.join(SP, 'b674_probe'), '--out', out, '--from-output', os.path.join(D, 'b643_probe_out_zeta.txt')],
                                             capture_output=True, text=True, encoding='utf-8', errors='replace')
    committed = sha(page)
    ctl_out = os.path.join(SP, 'b674_page_control.md')
    r0 = run_(os.path.join(D, 'b649_nodes_zeta.txt'), ctl_out)
    ctl = r0.returncode == 0 and sha(ctl_out) == committed
    if not ctl:
        sys.exit('### THE CONTROL DOES NOT EMIT THE COMMITTED PAGE (exit %d) -- NOTHING WRITTEN' % r0.returncode)
    if 'dry' in a:
        print('  the control: b649`s list emits the committed page byte for byte: %s (dry: nothing written)' % ctl)
        return
    r1 = run_(os.path.join(D, 'b674_nodes_zeta.txt'), page)
    d = subprocess.run(['git', '-C', PP, 'diff', '--unified=0', '--', FACES_PAGE], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    faces_line = [l for l in plus if 'equivalent faces, unequal converses' in l]
    L = ['b674 -- COMPONENT 2, (R284)(3): THE FACES PAGE RE-EMITTED THROUGH ITS GENERATOR (%s)' % utc(), '',
         '### the generator: relay tools/chain_page.py `--from-output` relay data/b643_probe_out_zeta.txt (no elaboration, no lean)',
         '### the control: b649`s list (relay data/b649_nodes_zeta.txt) emits the committed page byte for byte: %s (sha256 %s)' % (ctl, committed[:16]),
         '### the written page: from relay data/b674_nodes_zeta.txt (b649`s lines unchanged and one backmatter record), exit %d, sha256 %s' % (
             r1.returncode, sha(page)[:16]),
         '### THE DIFF AGAINST THE COMMITTED PAGE, BY KIND: lines added %d ; lines removed %d ; the faces line among the added %s' % (
             len(plus), len(minus), bool(faces_line)), '', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    L += ['', '### ### **CONTROL %s ; ADDED %d ; REMOVED %d ; THE FACES LINE WRITTEN THROUGH THE BACKMATTER CHANNEL %s.**' % (
        ctl, len(plus), len(minus), bool(faces_line))]
    put_txt('b674_faces_diff.txt', L)
    put_json('b674_faces_diff.json', dict(at=utc(), control=ctl, committed=committed, written=sha(page), added=len(plus), removed=len(minus),
                                          faces_line=bool(faces_line), rc=r1.returncode))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RE-CUT'S RUNS ON THE HOSTED RUNNER (b673's runner, carried)
WINDOW = 'SIDE-window'
WINDOW_DIR = 'D:/SIDE-window'


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """`runner <run id> <ref> <label>`: SIDE-window's run read by its id; the artifact listed, downloaded by its id into memory, its sha256
    against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; the axioms output
    of every AxiomCheck*.lean banked whole. data/b674_runner_SIDE-window_<label>.txt, data/b674_axioms_SIDE-window_<label>.txt and a row of
    data/b674_runner_rows.json. Carried from b673_record.py's runner with the kernel's own print step."""
    import hashlib
    import io as _io
    import zipfile
    run_id, ref, label = int(a[0]), a[1], a[2]
    repo = 'psinary-sketch/' + WINDOW
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=WINDOW, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b674 -- COMPONENT 3, (R284)(4): THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (WINDOW, label.upper(), utc()), '',
         '### the dispatch: at main (the workflow 7c4a2e1), the ref input %s' % ref,
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
    import hashlib as _h
    row['axioms_sha256'] = _h.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    files = re.findall(r'^=== (\S+)', ax, re.M)
    deps = re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)", re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M)
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (row['build_exit'], len(row['errors']))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the print step: files %d (%s) ; terminals printed %d ; axiom-free %d ; sorryAx %d' % (
              len(files), ', '.join(files), len(deps), sum(1 for _n, d in deps if d.startswith('does not')), sum(1 for _n, d in deps if 'sorryAx' in d))]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not any('sorryAx' in d for _n, d in deps)
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d ; SORRYAX %d ; GATE %s.**' % (
        run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']), len(deps),
        sum(1 for _n, d in deps if 'sorryAx' in d), row['gate'])]
    put_txt('b674_runner_SIDE-window_%s.txt' % label, L)
    if row['artifact_sha256']:
        put_txt('b674_axioms_SIDE-window_%s.txt' % label, ax.split(NL))
    j = jl('b674_runner_rows.json') if os.path.isfile(os.path.join(D, 'b674_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('label') != label] + [row]
    put_json('b674_runner_rows.json', dict(rows=rows))
    print(L[-1])


def prints(*a):
    """the 'before' and 'after' axioms outputs compared line for line (the navigator's answer on the SIDE-window build: the merge only where
    they are equal at every line). data/b674_prints_compare.txt."""
    b, f = rdn('b674_axioms_SIDE-window_before.txt'), rdn('b674_axioms_SIDE-window_after.txt')
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b674 -- COMPONENT 3: THE PRINTS BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % utc(), '',
         '### before: relay data/b674_axioms_SIDE-window_before.txt (3dab5f4, %d lines) ; after: relay data/b674_axioms_SIDE-window_after.txt (%d lines)' % (
             len(bl), len(fl)), '### the lines that differ:'] + (['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b674_prints_compare.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE CLOSING TOOL'S REPAIRS AT CARRY ((R284)(5))
def repairs(*a):
    """data/b674_tool_repairs.txt: rows are repairs with the defect they answer; b673's closing tool read against its seal hash (relay
    data/b673_seal_hashes.json) first; each repair shown by the hunks of the diff against that sealed copy that carry it; the H5 pattern run
    both ways on b673's H5 bank."""
    import hashlib
    old, new = os.path.join(T, 'b673_closing.py'), os.path.join(T, 'b674_closing.py')
    seal = (jl('b673_seal_hashes.json').get('tools') or {}).get('b673_closing.py')
    now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
    d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    hunks = re.split(r'(?m)^(?=@@ )', d)[1:]
    pick = lambda keys: [h for h in hunks if any(k in h for k in keys)]   # noqa: E731
    h_rem = pick(('read_remotes', 'REREAD', '_ls(', 'def remote_refs'))
    h_h5 = pick(('H5_LINE', "r'H5: "))
    t = rdn('b673_h5.txt')
    m_new = re.search(r'\*\*H5: ([^*]*?)\.\*\*', t)
    m_old = re.search(r'H5: [^*]*', t)
    L = ['b674 -- COMPONENT 4, (R284)(5): THE CLOSING TOOL`S TWO REPAIRS AT CARRY, AGAINST b673`S SEALED COPY (%s)' % utc(), '',
         '### b673`s sealed copy: tools/b673_closing.py sha256 %s ; the seal`s record %s ; %s' % (now[:16], (seal or '### NONE')[:16],
                                                                                                 'AGREE' if seal == now else '### DIFFER'),
         '### rows are repairs, each with the defect it answers and the diff`s hunks (b673 -> b674) that carry it:', '',
         '  REPAIR 1 -- THE REMOTE READS ONE PER CALL, IN SEQUENCE, AN EMPTY READ RE-READ ALONE BEFORE ANY ROW IS DECLARED. Answers b673 defect (p)',
         '  item 1 (three remotes read empty in one burst, the retry inside the burst) and banks relay data/b674_rules.txt row 1. Hunks %d:' % len(h_rem)]
    L += ['    ' + l for h in h_rem for l in h.rstrip(NL).split(NL)]
    L += ['', '  REPAIR 2 -- THE H5 LINE PRINTS ONE LINE, NOT THE BANK. Answers b673 defect (p) item 2 (the pattern `H5: [^*]*` matched the H5 bank`s',
          '  header and ran to its first asterisk). Hunks %d:' % len(h_h5)]
    L += ['    ' + l for h in h_h5 for l in h.rstrip(NL).split(NL)]
    L += ['  the patterns run on relay data/b673_h5.txt: b673`s `H5: [^*]*` takes %d characters (the bank from its header); b674`s anchored pattern '
          'takes one line, %d characters: "%s"' % (len(m_old.group(0)) if m_old else 0, len(m_new.group(1)) if m_new else 0,
                                                   (m_new.group(1)[:120] + '...') if m_new else '### NOT FOUND')]
    L += ['', '### ### **REPAIRS 2 ; THE SEALED COPY %s ; HUNKS %d AND %d ; THE H5 LINE ONE LINE %s.**' % (
        'AGREE' if seal == now else '### DIFFER', len(h_rem), len(h_h5), bool(m_new))]
    put_txt('b674_tool_repairs.txt', L)
    print(L[-1])


# ================================================================================ THE AUTHOR'S ANSWERS (b673's route, carried)
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
    """data/b674_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
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
    head = ['### b674 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a) for s, a in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b674_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b674_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b673's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def read_runner_row(r):
    """a row of data/b674_runner_rows.json: SIDE-window, a label (before or after), a 40-hex ref, a run id, a gate; returns (label, gate)."""
    if not isinstance(r, dict) or r.get('kernel') != WINDOW or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


PIN = re.compile(r'(SIDEWindow\.\w+), ((?:SIDEWindow/)?\w+\.lean):(\d+) at v0\.5\.1')


def read_pin_row(t):
    """a pin of data/b674_cut.txt, whitespace joined: a declaration of SIDEWindow, a file and a line at v0.5.1; returns (name, path, line)."""
    m = PIN.fullmatch(t) if isinstance(t, str) else None
    if not m:
        raise ValueError('pin of another shape: %r' % (t,))
    f = m.group(2) if '/' in m.group(2) else 'SIDEWindow/' + m.group(2)
    return m.group(1), f, int(m.group(3))


READERS += ['read_runner_row', 'read_pin_row']


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


MOVE_OR_DELETE = re.compile(r'\bgit\s+(-C\s+\S+\s+)?(mv|rm)\b|\bgit\s+(-C\s+\S+\s+)?branch\s+-[dD]\b|(^|[;&|]\s*|\s)rm\s+-|Remove' + r'-Item|\bos\.remove\b')


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    mv = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    L = ['b674 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1) AND THE MOVES AND DELETES (%s)' % utc(), '',
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
    put_txt('b674_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b674_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


KERNS = None


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + [WINDOW]      # ### SIDE-window is not among b641's thirteen; read beside them (the cut's kernel)


def kernels(*a):
    ks = _kerns()
    put_json('b674_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b674_defects.txt').split(NL)
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
    t = rdn('b674_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b674_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b674_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b674_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b674_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b674_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b674_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b674'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b674_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b674_ra_') as tmp:
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
    L = ['b674 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b674_root_arm.txt', L)
    put_json('b674_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b674 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b674_table_final.txt', L)
    put_json('b674_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b674_registration_2026-10-16.txt'
FACE = os.path.join(D, 'b674_registration_2026-10-16.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b674_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b674_regspec.py')], 'b674_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b674_satisfiable.json', '--emit', 'b674'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b674_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b674_census_stepzero.txt'), ('b327_faces_census.py', 'b674_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b674_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b674'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b674_reg_gate.txt', 'data/b674_reg_termscan.txt', 'data/b674_regspec_run.txt', 'data/audit_b674_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES, (N1)-(N5) OF THE FERRY AND THE SEAT'S (S1)-(S3)
# ### carried from b673_record.py :1131-:1285 by the Edit tool, every predicate re-written against (R284)'s expectations and this act's banks
import collections                 # noqa: E402
import hashlib as _hl              # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b673_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md', FACES_PAGE)


def TRAIL_HEAD():
    return ('### b674 — lane two, act one hundred and one, the re-cut act under (R284): SIDE-window docstrings re-cut to LICENSED/CITED, v0.5.1; '
            'the ceiling successor and the faces line written on the author’s word; the closing tool repaired at carry')


def _calls():
    return jl('b674_author_answers.json').get('calls') or []


def _ledger_adds():
    """the lines the act adds to PLACE-papers' files, read by the diff of the working tree against the act's start (README, REGISTRY and the
    faces page are written mid-file, so a prefix test would read each whole)."""
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _epoch(ts):
    import calendar
    return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')) if ts else None


def _ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t else None


def _prompt_of(header):
    """the prompt the answers bank carries under `header`: (its text, its call's time as an epoch), or (None, None)."""
    L = rdn('b674_author_answers.txt').split(NL)
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


def _ceiling_sites():
    """the (R183)(3) sentence at its three sites and the successor at its three, read at PLACE-papers HEAD by b670's delimiters: two sets of
    (site, sha256)."""
    fl = (jl('b674_record_lines_c2.json').get('lines') or [{}])[0].get('line')
    out = {}
    for lab, sites in (('(R183)(3)', K.CEILING_SITES), ('(R284)(3)', NEW_SITES + (('FINDINGS.md', fl),))):
        rows = []
        for f, n in sites:
            l = ((_show(PP, 'HEAD', f) or '').split(NL) + [''] * 99999)[n - 1] if n else ''
            m = (PLACED if f == 'FINDINGS.md' else SUP).search(l)
            s = (m.group(3) if f == 'FINDINGS.md' else m.group(1)) if m else None
            rows.append(('%s :%s' % (f, n), _hl.sha256(s.encode('utf-8')).hexdigest() if s else None))
        out[lab] = rows
    return out


def _n1():
    cm = jl('b674_commands.json')
    rr = jl('b674_runner_rows.json').get('rows') or []
    try:
        gates = [read_runner_row(r) for r in rr]
    except Exception:
        gates = []
    ok = bool(cm) and not cm.get('local_lean') and len(gates) == len(K.W_RUNS)
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b674_commands.txt); every build on the hosted runner, %d runs '
        'of SIDE-window read by their ids, %s (relay data/b674_runner_rows.json)' % (cm.get('local_lean') if cm else '### UNREAD', len(gates), gates))


def _n2():
    cj = jl('b674_citation_check.json')
    rows = cj.get('rows') or []
    # ### a row is [the clause, the cite, OK, what was read, the component]; the cite field read exactly and its OK flag True (a MISS row's
    # ### text may name the same line)
    tie_rows = [r for r in rows if isinstance(r, list) and len(r) == 5 and r[2] is True
                and r[1] in ('data/b670_licensed_table.txt :119', 'data/b670_licensed_table.txt :120')]
    rule_row = [r for r in rows if isinstance(r, list) and len(r) == 5 and r[2] is True and r[1] == 'OPEN_TRAILS :14238']
    printed = _epoch(cj.get('at'))
    tie, tie_t = _prompt_of('Tie')
    drafts, dr_t = _prompt_of('Two drafts')
    named = _ct(K.WD, K.W_WORKFLOW)       # ### SIDE-window's first commit of the act: the document named and its route begun
    written = _ct(PP, '4cb90e0')          # ### PLACE-papers' Component 2 commit: the first site written
    tie_ok = len(tie_rows) == 2 and bool(rule_row) and bool(tie) and ':119-:120' in tie and ':14238' in tie and printed and tie_t \
        and printed < tie_t < named
    land = rdn('b673_landing.txt').split(NL)
    dr_ok = bool(drafts) and 'equivalent faces, unequal converses' in drafts and 'compiled two ways' in drafts and dr_t and dr_t < written \
        and 'THE CEILING SENTENCE' in land[K.LANDING_DRAFTS[0] - 1] and 'THE FACES PAGE' in land[K.LANDING_DRAFTS[1] - 1]
    return ('HELD' if tie_ok and dr_ok else 'REFUTED'), (
        'the two tie rows and the rule`s row printed from their banks by the citation check at %s (relay data/b674_citation_check.txt: '
        'data/b670_licensed_table.txt :119, :120, %d rows; OPEN_TRAILS :14238, %d), raised in the tie prompt at %s, before SIDE-window`s first '
        'commit of the act %s at %s: %s; the two drafts quoted from relay data/b673_landing.txt :%d, :%d in the drafts prompt at %s, before '
        'PLACE-papers 4cb90e0 wrote the first site at %s: %s' % (
            cj.get('at'), len(tie_rows), len(rule_row), time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(tie_t)) if tie_t else '### NONE',
            K.W_WORKFLOW, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(named)) if named else '### NONE', bool(tie_ok),
            K.LANDING_DRAFTS[0], K.LANDING_DRAFTS[1], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(dr_t)) if dr_t else '### NONE',
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(written)) if written else '### NONE', bool(dr_ok)))


def _cut_figures():
    t = rdn('b674_cut.txt')
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+) \(OF ANY KIND (\d+), (\d+)\)', t)
    pins = [' '.join(x.split()) for x in re.findall(r'SIDEWindow\.\w+,\s+(?:SIDEWindow/)?\w+\.lean:\d+\s+at\s+v0\.5\.1', t)]
    return (tuple(int(x) for x in m.groups()) if m else None), pins


def _n3():
    fig, pins = _cut_figures()
    peeled = g(K.WD, 'rev-parse', K.W_TAG + '^{}').strip()
    got = []
    for p in pins:
        try:
            name, f, n = read_pin_row(p)
        except Exception:
            got.append((p, False))
            continue
        l = ((_show(K.WD, K.W_TAG, f) or '').split(NL) + [''] * 9999)[n - 1]
        got.append((p, bool(re.match(r'^\s*(theorem|lemma|def)\s+%s\b' % re.escape(name.split('.', 1)[1]), l))))
    ok = bool(fig) and fig[1] <= fig[0] and fig[3] <= fig[2] and len(pins) == 6 and all(v for _p, v in got) and peeled.startswith(K.W_MERGE)
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by b670`s method before %s, after %s; of any kind %s to %s (relay data/b674_cut.txt); pins %d, each a declaration read at '
        'its line in %s peeled at %s: %s' % (fig[0] if fig else '?', fig[1] if fig else '?', fig[2] if fig else '?', fig[3] if fig else '?',
                                             len(pins), K.W_TAG, peeled[:7], dict(collections.Counter('FOUND' if v else '### NOT AT ITS LINE' for _p, v in got))))


def _n4():
    S = _ceiling_sites()
    old = set(h for _s, h in S['(R183)(3)'])
    new = set(h for _s, h in S['(R284)(3)'])
    ok = len(old) == 1 and None not in old and list(old)[0].startswith(K.CEILING_SHA) and len(new) == 1 and None not in new
    return ('HELD' if ok else 'REFUTED'), (
        'at PLACE-papers HEAD, by b670`s delimiters: the (R183)(3) sentence at %s, sha256 %s, byte-equal %s; the successor, written on the '
        'author`s word, at %s, sha256 %s, byte-equal %s' % (', '.join(s for s, _h in S['(R183)(3)']), sorted(str(h)[:16] for h in old), len(old) == 1,
                                                          ', '.join(s for s, _h in S['(R284)(3)']), sorted(str(h)[:16] for h in new), len(new) == 1))


def _comment_only(rev_a, rev_b, f):
    """every changed line of `f` between the two revisions lies inside a Lean comment at its own side (a docstring, a block comment or a
    line comment): read by the diff's hunks against each side's comment spans."""
    def spans(rev):
        t = _show(K.WD, rev, f) or ''
        inside, out, depth = set(), [], 0
        for i, l in enumerate(t.split(NL), 1):
            j, start_depth = 0, depth
            code = False
            while j < len(l):
                if depth == 0 and l.startswith('--', j):
                    break
                if l.startswith('/-', j):
                    depth += 1
                    j += 2
                    continue
                if depth and l.startswith('-/', j):
                    depth -= 1
                    j += 2
                    continue
                if depth == 0 and not l[j].isspace():
                    code = True
                j += 1
            if not code or start_depth:
                inside.add(i)
            out.append(l)
        return inside
    a_in, b_in = spans(rev_a), spans(rev_b)
    d = g(K.WD, 'diff', '--unified=0', rev_a, rev_b, '--', f)
    bad = []
    for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', d, re.M):
        a0, an, b0, bn = int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1)
        bad += ['-%d' % i for i in range(a0, a0 + an) if i not in a_in] + ['+%d' % i for i in range(b0, b0 + bn) if i not in b_in]
    return bad


def _n5():
    face = jl('b674_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    moves = [(l.split()[0], l.split()[1:]) for l in g(K.WD, 'log', '--first-parent', '--format=%h %p', K.W_PRE_MAIN + '..main').split(NL) if l.strip()]
    main_ok = [m[0] for m in moves] == [K.W_MERGE, K.W_WORKFLOW] and moves[0][1] == [K.W_WORKFLOW, K.W_CUT] and moves[1][1] == [K.W_PRE_MAIN]
    wfiles = sorted(x for x in g(K.WD, 'diff', '--name-only', K.W_PRE_MAIN, 'main').split(NL) if x.strip())
    wf_ok = wfiles == sorted((K.W_WORKFLOW_FILE,) + K.W_CUT_FILES)
    comment = dict((f, _comment_only(K.W_WORKFLOW, K.W_CUT, f)) for f in K.W_CUT_FILES)
    prints_eq = 'EQUAL LINE FOR LINE True' in rdn('b674_prints_compare.txt')
    ke_moves = g(K.KE, 'rev-parse', 'main').strip() == K.MERGE
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b674_|audit_b674_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b674_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and main_ok and wf_ok and not any(comment.values()) and prints_eq and ke_moves and not pp_beyond and not kinds_beyond \
        and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written but N5`s amendment: SIDE-window`s '
            'main moved by %s (the workflow commit, parent %s, and the merge, parents %s) %s, its files %s %s, the cut`s changed lines outside a '
            'comment %s, the prints equal %s, tag %s; SIDE-explicit-formula`s main at %s %s; every kernel as the face read it %s; PLACE-papers '
            'beyond the ledgers, the three sites and the faces page: %s; standing arms added: %s (the act`s arms over its own banks %d); sealed '
            'tools not agreeing %s; relay files of a kind beyond the banks, the act`s tools, the table, the root list and b673`s push-out bank: '
            '%s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes and the gh workflow, run and artifact '
            'calls to the author`s own repositories at github.com, no search made, so no identifier of the author placed in a request' % (
                K.DRAFT, [m[0] for m in moves], moves[1][1] if len(moves) > 1 else '?', moves[0][1] if moves else '?', main_ok, wfiles, wf_ok,
                dict((f, v or 'NONE') for f, v in comment.items()), prints_eq, K.W_TAG, K.MERGE[:7], ke_moves, others_ok, pp_beyond or 'NONE',
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b674_table_final.json'), jl('b674_root_arm.json')
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
    put_json('b674_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _title():
    fig, _p = _cut_figures()
    return ('## SIDE-window docstrings re-cut: %s rows outside LICENSED/CITED to %s; the ceiling successor written at three sites; the faces '
            'line written; the closing tool repaired at carry' % ((fig[2], fig[3]) if fig else ('?', '?')))


def _finding_text():
    S, J = jl('b674_scores.json'), jl('b674_act_root.json')
    fig, pins = _cut_figures()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b674_author_answers.txt'), re.M))
    c1 = _rl_lines('b674_record_lines.json') + ['?'] * 2
    c2 = _rl_lines('b674_record_lines_c2.json') + ['?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'SIDE-window’s docstrings now say what its theorems compile: of the six rows outside LICENSED/CITED, five MATCH at v0.5.1, each pinned '
         'to a declaration at its line, and one header is cut in part; the ceiling’s next sentence and the faces page’s line on unequal '
         'converses are written on the author’s word. Nothing here proves RH or GRH.', '',
         '*Filed at b674 on the author’s ruling `(R284)` and the navigator’s answers (%d questions in %d calls, and the author’s word on the '
         'drafts). Banks: relay `data/b674_cut.txt`, `data/b674_prints_compare.txt`, `data/b674_ceiling_diff.txt`, `data/b674_faces_diff.txt`, '
         '`data/b674_tool_repairs.txt`, `data/b674_rules.txt`, `data/b674_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and each raised and answered; the mid-act '
         'checks of `(R278)`(4), %d prints, the last %s of %s OK. b673 at its weight, its closing’s head line quoted (FINDINGS :%s); the '
         'discharge on H5 through rh_equiv_mathlib (OPEN_TRAILS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids), mids[-1][1] if mids else '?',
             mids[-1][0] if mids else '?', c1[0], c1[1]), '',
         '**The tie** (`(R284)`(4)): SIDE-trivium and SIDE-window at five rows outside LICENSED or CITED each, neither with a declared suite '
         'failure, so b666’s rule (OPEN_TRAILS :14238) left it standing; raised, and broken by the navigator’s answer: the greater count of '
         'rows outside of any kind, UNDERSTATES counted (relay data/b674_rules.txt row 2), SIDE-window.', '',
         '**The re-cut** (`(R284)`(4) and the answers on the cut’s route and the build): the hosted runner’s workflow committed alone on '
         'SIDE-window’s main (7c4a2e1); the docstrings and module headers cut on recut-window-b674 (22bf840), built before at 3dab5f4 and after '
         'at the tip, 69 terminals each, every one axiom-free, the prints equal line for line; merged alone as e5b737a, tag v0.5.1. The '
         'distance by b670’s method %s to %s; of any kind %s to %s; pins %d. The one row left: the Sawtooth header’s ACTION covered one of '
         'its two claims and was applied verbatim, not extended.' % ((fig or ('?',) * 4)[0], (fig or ('?',) * 4)[1], (fig or ('?',) * 4)[2],
                                                                    (fig or ('?',) * 4)[3], len(pins)), '',
         '**The drafts** (`(R284)`(3), the author’s word “write both”): the successor beside the (R183)(3) sentence, which stays, at README.md '
         ':127, REGISTRY.md :962 and FINDINGS :%s, byte-equal at the three; the faces line through the page’s generator, b649’s list '
         'unchanged and one backmatter record added, the control emitting the committed page byte for byte.' % c2[0], '',
         '**The closing tool** (`(R284)`(5)): carried from b673’s sealed copy with its two repairs at carry, the remote reads one per call '
         'with an empty read re-read alone (relay data/b674_rules.txt row 1), the H5 line one line.', '',
         '**The root.** b674 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b670’s licensed table and b647’s SIDE-window table, and closes '
         'five of SIDE-window’s six rows there; it re-reads b673’s landing drafts and enters them where the author’s word placed them; it is '
         're-read by the next re-cut act, where SIDE-trivium stands at five, and by the b680 reading act. It strengthens the programme’s '
         'offering of kernels whose prose says no more than their compiled theorems: SIDE-window’s docstrings now name the theorem each '
         'claim cites.', '',
         '**Carried to:** SIDE-trivium’s five rows to the next re-cut act; the Sawtooth header’s marker (:17) to a ruling on the ACTION; the '
         'branch recut-window-b674 to the next ferry’s delete list; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero: the ceiling successor names an implication whose premise is not proved.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the after state of the six rows read by the seat at v0.5.1 against each row’s LICENSED reading, the table regenerator not '
              'run for SIDE-window (relay data/b674_cut.txt); (2) the Sawtooth header’s ACTION applied verbatim, covering one of its two claims, '
              'banked as cut in part and not extended; (3) no line written against the nine-kernels item, SIDE-window not among its nine '
              '(relay data/b674_defects.txt (e’)); (4) `(R284)`(6)’s delete read in the house form, the local branch: chi-li-b669’s branch at '
              'SIDE-explicit-formula’s remote stands at 5050a46, a delete at the remote not named')


def _trail_text():
    S, J = jl('b674_scores.json'), jl('b674_act_root.json')
    fj = jl('b674_findings.json')
    fig, pins = _cut_figures()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b674_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b674_record_lines.json')
    c2 = _rl_lines('b674_record_lines_c2.json')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R284) ratified.** (1) b673 at its weight. (2) H5 through rh_equiv_mathlib. (3) The two drafts, written on the author’s word. '
             '(4) The re-cut. (5) The closing tool repaired at carry. (6) The branches. (7) The read-first bank. (8) The draft held at v5. '
             '(9) The act after.', '',
             '**Entered:** FINDINGS.md:%s (b673’s weight), :%s (the successor’s placement), :%s (the entry); OPEN_TRAILS.md:%s (the discharge '
             'on H5 through rh_equiv_mathlib); README.md :127, REGISTRY.md :962; THE_CLAUSE_AND_ITS_COMPILED_FACES.md regenerated; this record.' % (
                 c1[0] if c1 else '?', c2[0] if c2 else '?', fj.get('entry_line'), c1[1] if len(c1) > 1 else '?'), '',
             '**Act root:** b674 `%s` (previous `%s`, b673’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b674_author_answers.txt), and the author’s word on the drafts; '
             'none after the root.' % (n_ans, len(_calls())), '',
             '**The re-cut:** SIDE-window, rows outside LICENSED/CITED %s to %s (the b670 distance %s to %s), pins %d at v0.5.1 (e5b737a); runs '
             '38988546013 before and 38988610526 after, the prints equal line for line.' % (
                 (fig or ('?',) * 4)[2], (fig or ('?',) * 4)[3], (fig or ('?',) * 4)[0], (fig or ('?',) * 4)[1], len(pins)), '',
             '**The open orders:** `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at the b680 reading act; SIDE-trivium’s five rows to the next '
             're-cut act.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b674_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b674_scores.json')
    L = ['=' * 104, 'b674 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b674_defects.txt').rstrip(NL).split(NL)
    put_txt('b674_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b674_scores.json', 'b674_findings.json', 'b674_trail.json', 'b674_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b674_record_lines.json') + ['?'] * 2
    c2 = _rl_lines('b674_record_lines_c2.json') + ['?']
    fig, pins = _cut_figures()
    L = ['b674 -- THE COMPONENTS, BANKED UNDER (R284).', '',
         '### COMPONENT 0 : the citation check (data/b674_citation_check.txt), step zero (data/b674_ferry.txt, data/b674_readfirst.txt, '
         'data/b674_stepzero.txt, data/b674_tests_stepzero.txt, data/b674_rowgen_stepzero.txt, data/b674_branches.txt)',
         '### COMPONENT 1 : b673`s weight FINDINGS :%s ; the discharge line OPEN_TRAILS :%s' % (c1[0], c1[1]),
         '### COMPONENT 2 : the successor at README :127, REGISTRY :962, FINDINGS :%s (data/b674_ceiling_diff.txt) ; the faces line '
         '(data/b674_faces_diff.txt) ; N2 %s ; N4 %s' % (c2[0], S['N2'][0], S['N4'][0]),
         '### COMPONENT 3 : the re-cut of SIDE-window (data/b674_cut.txt), %s to %s of any kind, pins %d ; runs before and after '
         '(data/b674_runner_rows.json), the prints equal (data/b674_prints_compare.txt) ; merged e5b737a, v0.5.1 ; N3 %s' % (
             (fig or ('?',) * 4)[2], (fig or ('?',) * 4)[3], len(pins), S['N3'][0]),
         '### COMPONENT 4 : the closing tool`s two repairs (data/b674_tool_repairs.txt)',
         '### COMPONENT 5 : the dry-run step (data/b674_reg_gate.txt), the seal (data/b674_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b674_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b674_findings.json', dict(title=t))
    j = jl('b674_findings.json')
    j['entry_line'] = ln
    put_json('b674_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b674_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b655 form; b673's routes, carried)
MIRROR_TAG = '2026-10-17-b674'
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
    put_json('b674_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b674':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b674`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b674_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b674_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b674_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b674 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE MOVES: none this act; the roster`s files as before',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b674_mirror.txt', L)
    put_json('b674_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'answers': answers, 'c1': c1, 'c2': c2, 'ceilingdiff': ceilingdiff, 'faces': faces,
          'runner': runner, 'prints': prints, 'repairs': repairs, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root,
          'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components,
          'findings': findings, 'trail': trail, 'drycheck': drycheck, 'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b674_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
