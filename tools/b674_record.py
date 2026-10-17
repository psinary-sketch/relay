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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'answers': answers, 'c1': c1, 'c2': c2, 'ceilingdiff': ceilingdiff, 'faces': faces}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b674_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
