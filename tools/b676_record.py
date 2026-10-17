# -*- coding: utf-8 -*-
"""b676_record.py -- THE ACT'S RECORD TOOL, b676 under (R286).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b676's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b675_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes);
### the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b676_record.py <route> [dry]`.
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
import b676_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b675_record.py with b676's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b676_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b676_findings.json': dict(entry_line=99999, title='stand-in'),
        'b676_trail.json': dict(line=99999),
        'b676_act_root.json': dict(root='0' * 64, previous='e4a6c527' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b676's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b676_scanfile_%s.md' % tag)
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
    """a row of data/b676_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    run on this host) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b676_rowgen_stepzero.txt."""
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
    L = ['b676 -- STEP ZERO: ROWGEN DIFF AND CONSTELLATION MODE AT THE START OF THE REVIEW PASS (b670 rules row 3) (%s)' % utc(), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b676_rowgen_stepzero.txt', L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R286)(5))
def branches(*a):
    """every branch (R286)(5) names, its tip read before any delete, its fate; no remote deletion is named this act.
    data/b676_branches.txt (.json); writes nothing else."""
    rows = []
    for repo, bs in K.DELETE:
        for b in bs:
            tip = g(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
            merged = b in g(repo, 'branch', '--merged', 'main', '--list', b)
            rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=merged, fate='DELETED'))
    for r in rows:
        read_branch_row(r)
    L = ['b676 -- STEP ZERO, (R286)(5): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local or remote ; tip ; listed by `git branch --merged main` ; fate.',
         '### Deleted by name in the house form after --merged lists them, one repository per call; no branch the ruling does not name is',
         '### deleted; the ruling names no remote deletion.']
    L += ['  %-24s %-20s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                              r['fate']) for r in rows]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE 0) ; MERGED %d ; TO BE DELETED %d.**' % (
        len(rows), len(rows), sum(1 for r in rows if r['merged']), len(rows))]
    put_txt('b676_branches.txt', L)
    put_json('b676_branches.json', dict(at=utc(), rows=rows))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R286)(1)
WH = ('*Appended 2026-10-17 by b676 to b675’s entry (:8881), under `(R286)`(1) -- b675 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b675_closing.txt):*')
WB = (' “b675 closed: relay cced648a, PLACE-papers 0b51683; suite 83 of 83; root e4a6c52715bf9693…; 4 prompts answered; 13 defects” '
      '(data/b675_closing.txt :1), the closing pushed at relay 7e867b61 (data/b675_closing_push_out.txt :4). The finding (this entry and '
      'the trail at OPEN_TRAILS :14532): Q0 lies outside the kernel’s configuration class at v0.32 -- HStrip holds on all 34 certified real '
      'parts (0.0467 to 0.9533, data/b675_hypotheses.txt :43) and fails for the configuration as a whole by Davenport–Heilbronn at '
      'h(−23) = 3 (:49), the σ > 1 zeros above t = 150; ZeroConfig carries the closed strip as a field of the type (Zeta23/Defs.lean :142 '
      'at e36ea31), so Q0’s zero set is no configuration of that type; the (3c) bound puts every zero in (−1/2, 3/2) at every height, and '
      'HStrip on that strip is the variant hypothesis named for a later act (data/b675_li_plan.txt :136). The bench as observation '
      '(data/b675_closing.txt :26-:27): n_obs = 10034 with T-COUNT (the kernel’s premise P3, HCount Z 10) assumed; n* = 63676, the v0.32 '
      'bound’s onset were HStrip to hold, consumed by nothing; NEG at 102 of 201 n in [n*, n* + 200], the sign following the dominant '
      'pair’s angle; C2′ NEG 0; C2 negative from 15401; H6 n*′ = 358665, n_obs′ = 64065. H1 and H3 refuted as the ruling worded them, '
      'H2 and H4–H6 held; N1–N5 and S1–S3 held (:42); the suite 83 of 83 pre-push and post-push (:123, :125); the closing tool’s four '
      'repairs at carry (:31); the closing dry-run a gate step (data/b675_rules.txt row 1); ten branches deleted, two at their remotes '
      '(data/b675_branches.json). Thirteen defects (a)–(m), the navigator’s (a)–(g) (data/b675_defects.txt :8–:57). The suite’s 83 arms '
      'where b674’s counted 84: no arm was removed -- both suites carry the 68 standing arms whole, and the act arms are minted per act, '
      'b674’s 16 and b675’s 15 (data/b674_checks.txt :6, data/b675_checks.txt :7; relay data/b676_citation_check.txt). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b676_record_lines.json', 'c1', entry=K.B675_ENTRY,
         check=[('FINDINGS.md', K.B675_ENTRY, '## The Li index at Q0'), ('OPEN_TRAILS.md', K.B675_TRAIL, '### b675')], dry=dry)


# ================================================================================ COMPONENT 2: THE NAMING, (R286)(2) -- before any document is named
def _kern_rows():
    """the kernels table's rows (data/b647_table_kernels.txt), each with its OVERREACHES count, and the licensed table's row for each."""
    L = rdn(K.KERNELS_BANK).split(NL)
    out = []
    for i, l in enumerate(L, 1):
        m = re.match(r'^  (SIDE-[\w-]+)\s+([0-9a-f]{7}) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|\s+(\d+) \|', l)
        if m:
            out.append(dict(line=i, text=l, kernel=m.group(1), pin=m.group(2), rows=int(m.group(3)), over=int(m.group(6)),
                            unlic=int(m.group(7)), under=int(m.group(5))))
    return out


def naming(*a):
    """(R286)(2) and N2: the tie-break rule's row and the table rows printed verbatim from their banks; every kernel's standing count read
    from the licensed table (a kernel cut since its read stands at its cut bank's figure); the document named by the descending count and,
    at a tie, by the rule; then the named kernel's workflow directory and print bank read or declared absent -- all before any branch is
    made. data/b676_naming.txt (.json); writes nothing else."""
    rules = rdn(K.RULES_BANK).split(NL)
    i0 = [i for i, l in enumerate(rules) if l.startswith('  (%d) ' % K.TIE_RULE_ROW)][0]
    rule = [rules[i0]]
    for l in rules[i0 + 1:]:
        if not l.startswith('      '):
            break
        rule.append(l)
    lt = rdn(K.TABLE_BANK).split(NL)
    standing = {}
    for i, l in enumerate(lt, 1):
        m = re.match(r'^  (SIDE-[\w-]+) docstrings \(read at ([0-9a-f]{7})\)\s+(\d+) ->\s+(\d+)', l)
        if m:
            standing[m.group(1)] = (i, int(m.group(4)), l)
    window_after = 1 if '### ### **ROWS 6 ; MATCHES AFTER 5 ; CUT IN PART 1 ; THE DISTANCE BEFORE 5, AFTER 1' in rdn('b674_cut.txt') else None
    kr = _kern_rows()
    rank = []
    for r in kr:
        ln, now, _l = standing.get(r['kernel'], (None, None, None))
        if r['kernel'] == 'SIDE-window' and window_after is not None:
            now = window_after
        rank.append((now if now is not None else -1, r['kernel'], ln, r))
    rank.sort(key=lambda x: (-x[0], x[1]))
    top = rank[0][0]
    tied = [x for x in rank if x[0] == top]
    named = tied[0][1] if len(tied) == 1 else None
    wf = g(K.TD, 'ls-tree', '--name-only', 'main', '.github/workflows/').split()
    pshape = lambda ns: (r"'%s\.[A-Za-z0-9_.']+' (depends on axioms|does not depend on any axioms)|^  %s\.[A-Za-z0-9_.']+ +\[" % (ns, ns))   # noqa: E731
    pb = sorted(set(g(ROOT, 'grep', '-lE', pshape('Trivium'), '--', 'data/').split()))
    pw = sorted(set(g(ROOT, 'grep', '-lE', pshape('SIDEWindow'), '--', 'data/').split()))
    pe = sorted(set(g(ROOT, 'grep', '-lE', pshape('SIDEEffects'), '--', 'data/').split()))
    pt = g(K.TD, 'ls-tree', '--name-only', 'main').split()
    L = ['b676 -- COMPONENT 2, (R286)(2): THE RULE ROW AND THE TABLE ROWS, VERBATIM, BEFORE THE DOCUMENT IS NAMED (%s)' % utc(), '',
         '### THE RULE, verbatim with path and line (relay data/%s :%d):' % (K.RULES_BANK, i0 + 1)] + ['    ' + l for l in rule] + [
         '', '### THE TABLE ROWS, verbatim with path and line: the licensed table (relay data/%s) for each kernel of the kernels table' % K.TABLE_BANK,
         '### (relay data/%s), the kernels-table row beside it; a kernel cut since its read stands at its cut bank`s figure (SIDE-window at 1,' % K.KERNELS_BANK,
         '### relay data/b674_cut.txt :49), ordered by the count now standing:']
    for now, k, ln, r in rank:
        L.append('  %2d  %-34s licensed table :%s  "%s"' % (now, k, ln, (standing.get(k) or (0, 0, ''))[2].strip()))
        L.append('      %-34s kernels table :%d  "%s"' % ('', r['line'], r['text'].strip()))
    L += ['', '### THE NAMING: the greatest count standing is %d, carried by %s; %s' % (
        top, ', '.join(x[1] for x in tied), 'no tie, so the tie-break rule (row %d) is not reached; the document named by the descending count '
        '(b652`s order, the rule the re-cut acts have cut by since b655): %s docstrings' % (K.TIE_RULE_ROW, named) if named else
        '### A TIE -- the rule of row %d is applied by its letter in the cut bank' % K.TIE_RULE_ROW),
          '### THE CARRIED CANDIDATE ((R286)(2)): %s docstrings at 5 -- %s' % (K.CANDIDATE, 'THE SAME' if named == K.CANDIDATE else '### NOT THE SAME'),
          '', '### THE NAMED KERNEL`S WORKFLOW DIRECTORY AND PRINT BANK (read before any branch is made):',
          '  %s main %s: .github/workflows/ carries %s -- %s' % (K.CANDIDATE, g(K.TD, 'rev-parse', '--short', 'main').strip(), wf or 'NOTHING',
                                                             'NO build-module.yml (no dispatch input; no print step)' if not any(
                                                                 'build-module' in f for f in wf) else 'a build-module.yml'),
          '  print_targets.txt at its root: %s ; AxiomCheck*.lean at its root: %s' % ('print_targets.txt' in pt, [f for f in pt if f.startswith('AxiomCheck')] or 'NONE'),
          '  relay tracked banks carrying a printed axiom line of a Trivium declaration (git grep -lE over data/, the shapes Lean prints, '
          '"\'Trivium.x\' depends on axioms" and "\'Trivium.x\' does not depend on any axioms", and the print banks` row shape "  Trivium.x  [..."): '
          '%s -- %s' % (pb or 'NONE', 'NO PRINT BANK' if not pb else 'a print bank'),
          '  the controls, the same shapes over two kernels with print banks: SIDEWindow. %d bank(s), b674`s before bank among them %s ; '
          'SIDEEffects. %d bank(s), b664`s print bank among them %s' % (
              len(pw), 'data/b674_axioms_SIDE-window_before.txt' in pw, len(pe), 'data/b664_prints_SIDE-effects.txt' in pe),
          '  its dependency form: lakefile.lean requires mathlib @ "%s" ; lean-toolchain %s' % (
              (re.search(r'@ "([^"]+)"', _show(K.TD, 'main', 'lakefile.lean') or '') or [None, None])[1],
              (_show(K.TD, 'main', 'lean-toolchain') or '').strip()),
          '', '### ### **NAMED %s ; TIED %d ; WORKFLOW build-module.yml %s ; PRINT BANK %s.**' % (
              named or '### NONE', len(tied), 'PRESENT' if any('build-module' in f for f in wf) else 'ABSENT',
              'PRESENT' if pb else 'ABSENT')]
    put_txt('b676_naming.txt', L)
    put_json('b676_naming.json', dict(at=utc(), named=named, tied=[x[1] for x in tied], top=top, workflows=wf, print_banks=pb,
                                      rank=[[x[0], x[1], x[2], x[3]['line']] for x in rank]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE RE-CUT'S RUNS ON THE HOSTED RUNNER (b674's runner, carried)
def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def _targets():
    return [l.strip() for l in (_show(K.TD, K.T_MAIN, 'print_targets.txt') or '').split(NL) if l.strip()]


def runner(*a):
    """`runner <run id> <ref> <label>`: SIDE-trivium's run read by its id; the artifact listed, downloaded by its id into memory, its sha256
    against the platform's digest BEFORE any reading; the build's exit and error lines, the memory log's low and any STOP; the axioms output
    of the print step (one scratch file importing the target's modules, a #print axioms line per name of print_targets.txt) banked whole,
    every name of the list matched to one printed line. data/b676_runner_SIDE-trivium_<label>.txt, data/b676_axioms_SIDE-trivium_<label>.txt
    and a row of data/b676_runner_rows.json. Carried from b674_record.py's runner with the kernel's print list."""
    import hashlib
    import io as _io
    import zipfile
    run_id, ref, label = int(a[0]), a[1], a[2]
    repo = 'psinary-sketch/' + K.CANDIDATE
    rc, out, err = _gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=K.CANDIDATE, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['b676 -- COMPONENT 2, (R286)(2): THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (K.CANDIDATE, label.upper(), utc()), '',
         '### the dispatch: at main (the workflow %s, the print list %s), the ref input %s ; the target `%s`' % (K.T_WORKFLOW, K.T_MAIN, ref, K.T_TARGET)]
    if label == 'before':
        L.append('### THE PRINT BANK AT MAIN, NOT AT A TAG (the navigator`s answer on the `before` bank): main 1aac3a9 is %s commits past v0.1 '
                 '(ec92d62); the run`s main %s is 1aac3a9 with the workflow and print-list commits atop it (%s past v0.1), no .lean byte '
                 'changed' % (g(K.TD, 'rev-list', '--count', 'v0.1..1aac3a9').strip(), K.T_MAIN,
                              g(K.TD, 'rev-list', '--count', 'v0.1..' + K.T_MAIN).strip()))
    L.append('### the run: id %s ; %s ; status %s ; conclusion %s ; %s to %s' % (run_id, run.get('url'), run.get('status'), run.get('conclusion'),
                                                                               run.get('createdAt'), run.get('updatedAt')))
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
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = re.findall(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)", re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax), re.M)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (row['build_exit'], len(row['errors']))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; refused %s' % (len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg),
                                       sum(1 for _n, d in deps if d.startswith('does not')), sum(1 for _n, d in deps if 'sorryAx' in d),
                                       T_.get('axioms_refused.txt', '').strip() or 'NONE')]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not any('sorryAx' in d for _n, d in deps)
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; GATE %s.**' % (
        run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']), len(deps),
        len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), row['gate'])]
    put_txt('b676_runner_SIDE-trivium_%s.txt' % label, L)
    if row['artifact_sha256']:
        put_txt('b676_axioms_SIDE-trivium_%s.txt' % label, ax.split(NL))
    j = jl('b676_runner_rows.json') if os.path.isfile(os.path.join(D, 'b676_runner_rows.json')) else {}
    rows = [r for r in (j.get('rows') or []) if r.get('label') != label] + [row]
    put_json('b676_runner_rows.json', dict(rows=rows))
    print(NL.join(L))


def prints(*a):
    """the 'before' and 'after' axioms outputs compared line for line (the merge only where they are equal at every line).
    data/b676_prints_compare.txt."""
    b, f = rdn('b676_axioms_SIDE-trivium_before.txt'), rdn('b676_axioms_SIDE-trivium_after.txt')
    if not b or not f:
        sys.exit('### A PRINT BANK IS MISSING -- NOTHING WRITTEN')
    bl, fl = b.rstrip(NL).split(NL), f.rstrip(NL).split(NL)
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(bl, fl)) if x != y] + ([('length', len(bl), len(fl))] if len(bl) != len(fl) else [])
    L = ['b676 -- COMPONENT 2: THE PRINTS BEFORE AND AFTER THE CUT, LINE FOR LINE (%s)' % utc(), '',
         '### before: relay data/b676_axioms_SIDE-trivium_before.txt (%s, %d lines) ; after: relay data/b676_axioms_SIDE-trivium_after.txt (%s, %d lines)' % (
             K.T_MAIN, len(bl), K.T_CUT, len(fl)), '### the lines that differ:'] + (['    %s : %s | %s' % d for d in diff] or ['    NONE'])
    L += ['', '### ### **PRINTS BEFORE %d LINES ; AFTER %d LINES ; DIFFERING %d ; EQUAL LINE FOR LINE %s.**' % (len(bl), len(fl), len(diff), not diff)]
    put_txt('b676_prints_compare.txt', L)
    print(L[-1])


def _strip_comments(t):
    """the Lean text with every block comment (nested /- -/, docstrings and module docs included) and every line comment removed, whitespace
    runs collapsed: what the elaborator reads."""
    out, i, depth = [], 0, 0
    while i < len(t):
        if t.startswith('/-', i):
            depth, i = depth + 1, i + 2
            continue
        if depth and t.startswith('-/', i):
            depth, i = depth - 1, i + 2
            continue
        if not depth and t.startswith('--', i):
            j = t.find(NL, i)
            i = len(t) if j < 0 else j
            continue
        if not depth:
            out.append(t[i])
        i += 1
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def cutdiff(*a):
    """(R286)(2): the cut's diff (the print-list main to the cut tip), printed whole; the files it touches; each file's text with its comments
    stripped compared before and after (equal = no line the elaborator reads changed), with a positive control (a one-word code change in
    the after text must make the comparison unequal). data/b676_cut_diff.txt."""
    files = g(K.TD, 'diff', '--name-only', K.T_MAIN, K.T_CUT).split()
    d = g(K.TD, 'diff', '--unified=0', K.T_MAIN, K.T_CUT).replace(chr(13), '')
    rows = []
    for f in files:
        b, n = _show(K.TD, K.T_MAIN, f) or '', _show(K.TD, K.T_CUT, f) or ''
        eq = _strip_comments(b) == _strip_comments(n)
        ctl = _strip_comments(b) == _strip_comments(n.replace('theorem trivium_theorem', 'theorem trivium_theorem_', 1))
        rows.append((f, eq, ctl, 'theorem trivium_theorem' in n))
    plus = [l for l in d.split(NL) if l.startswith('+') and not l.startswith('+++')]
    minus = [l for l in d.split(NL) if l.startswith('-') and not l.startswith('---')]
    L = ['b676 -- COMPONENT 2, (R286)(2): THE CUT`S DIFF, RESTRICTED TO COMMENT AND DOCSTRING LINES (%s)' % utc(), '',
         '### SIDE-trivium %s (main, the print list) -> %s (the cut, recut-trivium-b676); files %s ; lines added %d, removed %d' % (
             K.T_MAIN, K.T_CUT, files, len(plus), len(minus)),
         '### rows are files: the text with every comment stripped equal before and after ; the control (a one-word code change in the after',
         '### text) unequal ; the control`s needle present:']
    L += ['  %-28s CODE EQUAL %s ; CONTROL UNEQUAL %s ; NEEDLE PRESENT %s' % (f, eq, not ctl, nd) for f, eq, ctl, nd in rows]
    L += ['', '### the diff, whole:'] + ['    ' + l for l in d.rstrip(NL).split(NL)]
    ok = files == list(K.T_CUT_FILES) and all(eq and not ctl and nd for _f, eq, ctl, nd in rows)
    L += ['', '### ### **FILES %d ; CODE EQUAL WITH COMMENTS STRIPPED %s ; CONTROLS UNEQUAL %s ; COMMENT AND DOCSTRING LINES ALONE %s.**' % (
        len(files), all(r[1] for r in rows), all(not r[2] for r in rows), ok)]
    put_txt('b676_cut_diff.txt', L)
    print(L[-1])


def corr(*a):
    """(R286)(2): the Correspondence generator (tools/correspondence_gen.py) run `dry full` (the local clones' tags, no remote call; it writes
    nothing), its print banked whole with the count of lines naming the cut kernel. The `run` mode writes b672's own banks
    (data/b672_correspondence_diff.*) and is not run where the dry run changes no cell. data/b676_correspondence_dry.txt."""
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry', 'full'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=560)
    out = ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')
    hits = [l for l in out.split(NL) if re.search(r'(?i)trivium', l)]
    v = [l for l in out.split(NL) if 'CELLS CHANGED' in l][-1:] or ['### NO VERDICT LINE']
    L = ['b676 -- COMPONENT 2, (R286)(2): THE CORRESPONDENCE GENERATOR, DRY, AFTER THE TAG %s (%s)' % (K.T_NEXT_TAG, utc()), '',
         '### relay tools/correspondence_gen.py `dry full`, exit %d ; lines naming SIDE-trivium or Trivium %d ; the generator`s verdict:' % (
             r.returncode, len(hits)), '    ' + v[0].strip(), '', '### the print, whole:'] + ['    ' + l for l in out.rstrip(NL).split(NL)]
    cc = re.search(r'CELLS CHANGED (\d+)', v[0])
    L += ['', '### ### **GENERATOR EXIT %d ; CELLS CHANGED %s ; LINES NAMING THE CUT KERNEL %d ; RUN MODE %s.**' % (
        r.returncode, cc.group(1) if cc else '### UNREAD', len(hits), 'NOT RUN (no cell to change)' if cc and cc.group(1) == '0' and not hits
        else '### TO BE RUN')]
    put_txt('b676_correspondence_dry.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 3: THE Q0 LINES, (R286)(3) -- read and banked, nothing cut
Q_OBJ1 = r'\bQ0\b|\bQ₀\b|Q_0\b|\bEpstein\b'
Q_OBJ2 = (r'\bZ_Q\b|Z_\{?Q\}?|\bZQ\b|disc(riminant)?\.? ?[−-]23|h\([−-]23\)|x\^?2 ?\+ ?xy ?\+ ?6y\^?2|qE0|EpsteinQ0|A0Q|Q0Premises')
Q_CLS = r'configuration|ZeroConfig|WeilConfig|\binstance|\bclass\b|HStrip|H-STRIP|satisf|member|\bstrip\b'
Q_SPLIT = r'(?<=[.;!?])\s+(?=[A-Z`(*§])'
# ### the seat's hand readings: every hit is CONSISTENT with the finding unless listed here, each TO RE-CUT row keyed by (file, line, a needle
# ### of its sentence) with its reason. A needle that matches no hit stops the route.
Q_RECUT = (
    ('FINDINGS.md', 4437, 'two families inside the compiled class', 'Q0 named inside "the compiled class"'),
    ('FINDINGS.md', 4766, 'finite instance of zeroSide_eventually_neg', 'the Q0 witness read as an instance of a theorem over a configuration'),
    ('FINDINGS.md', 4782, 'became an instance of the theorem', 'the Q0 cell read as an instance of the configuration theorem'),
    ('FINDINGS.md', 6024, 'a property of the configuration too', 'the Q0 bank read as "the configuration" (the object named in the line`s first sentence)'),
    ('FINDINGS.md', 6740, 'the Epstein instance at INTERFACES', 'the Epstein instance of the detector`s configuration'),
    ('FINDINGS.md', 6746, 'The Epstein instance', 'Z_Q entered as an instance on premises over a configuration'),
    ('FINDINGS.md', 6778, 'a corpus line on the Epstein configuration', '"the Epstein configuration"'),
    ('FINDINGS.md', 6786, 'the Epstein instance a Correspondence row', 'the Epstein instance a page row'),
    ('FINDINGS.md', 7066, 'at the Epstein configuration', '"the Epstein configuration"'),
    ('FINDINGS.md', 7092, 'at the Epstein configuration', '"the Epstein configuration"'),
    ('FINDINGS.md', 7190, 'the Epstein configuration the detector meets', '"the Epstein configuration"'),
    ('FINDINGS.md', 7246, 'each meeting the Epstein configuration unchanged', '"the Epstein configuration"'),
    ('FINDINGS.md', 7266, 'each holding unchanged at the Epstein configuration', '"the Epstein configuration"'),
    ('FINDINGS.md', 7378, 'fail at the Epstein configuration', '"the Epstein configuration"'),
    ('FINDINGS.md', 7949, 'no construction of its configuration', 'the Epstein count`s "configuration" presumed to exist'),
    ('FINDINGS.md', 8355, 'at the Q0 configuration', '"the Q0 configuration"'),
    ('FINDINGS.md', 8537, 'the detector at the real configuration', 'Q0 as "the real configuration"'),
    ('FINDINGS.md', 8541, 'the instance described as new', 'the Epstein instance named as an instance'),
    ('FINDINGS.md', 8547, 'the list in the configuration', 'Q0`s points as a configuration`s'),
    ('FINDINGS.md', 8549, 'every hypothesis of the rate theorem certified by name', 'every hypothesis of a configuration theorem read as certified at Q0'),
    ('FINDINGS.md', 8555, 'Epstein instance', 'the Epstein instance named as an instance'),
    ('FINDINGS.md', 8561, 'Schema/EpsteinQ0.lean on four named premises', 'the instance on premises over a configuration'),
    ('FINDINGS.md', 8561, 'at a configuration whose target is false', 'Q0 read as a configuration whose target is false'),
    ('FINDINGS.md', 8663, 'the configuration’s points ball-certified', 'Q0`s points as "the configuration`s points"'),
    ('FINDINGS.md', 8669, 'the Q0 configuration the negative control stands on', '"the Q0 configuration"'),
    ('OPEN_TRAILS.md', 9994, 'two families inside the compiled class', 'Q0 named inside "the compiled class"'),
    ('OPEN_TRAILS.md', 12154, 'the Epstein instance at INTERFACES', 'the Epstein instance of the detector`s configuration'),
    ('OPEN_TRAILS.md', 12156, 'the Epstein instance at INTERFACES', 'the Epstein instance of the detector`s configuration'),
    ('OPEN_TRAILS.md', 13493, 'the zero configuration of the Epstein zeta function', 'Z_Q`s zeros as "the zero configuration" to construct'),
    ('OPEN_TRAILS.md', 13525, 'the instance exists at v0.16', 'the Epstein instance named as an instance'),
    ('OPEN_TRAILS.md', 13988, 'at the Q0 configuration', '"the Q0 configuration"'),
    ('OPEN_TRAILS.md', 14160, 'the configuration’s points carry balls', 'Q0`s points as "the configuration`s points"'),
    ('OPEN_TRAILS.md', 14166, 'the Q0 configuration built on premises', '"the Q0 configuration"'),
    ('OPEN_TRAILS.md', 14168, 'The computation at the real configuration', 'Q0 as "the real configuration" (the object named at (2) of the line)'),
    ('OPEN_TRAILS.md', 14178, 'the instance’s declarations', 'the Epstein instance named as an instance'),
    ('OPEN_TRAILS.md', 14266, 'carries the configuration’s points', 'Q0`s points as "the configuration`s points"'),
)
Q_CONSISTENT_STATES = ('outside the kernel', 'no configuration of that type', 'leaves the open strip', 'fails for Q0', 'fails for the configuration',
                       'not on an Epstein configuration', 'CLASS BOUNDARY', 'the obstruction is membership')


def _q0_hits():
    """the survey: every roster table (data/b586_corroboration.txt :34) and the two ledgers at PLACE-papers HEAD, each line carrying an object
    word; a hit is a sentence carrying an object word and a class word, or, where the two sit in different sentences of one line, the line
    (its object sentence and its class sentence). Returns (hits, yields)."""
    o1, o2, cl, sp = re.compile(Q_OBJ1, re.I), re.compile(Q_OBJ2, re.I), re.compile(Q_CLS, re.I), re.compile(Q_SPLIT)
    files = [p for _n, p in roster()] + ['FINDINGS.md', 'OPEN_TRAILS.md']
    hits, y = [], dict(lines_obj1=0, lines_obj2=0, lines_obj=0, lines_obj_and_class=0, sentence_hits=0, line_hits=0, files=len(files))
    for f in files:
        for i, l in enumerate(rd(os.path.join(PP, f)).split(NL), 1):
            a, b = bool(o1.search(l)), bool(o2.search(l))
            y['lines_obj1'] += a
            y['lines_obj2'] += b
            if not (a or b):
                continue
            y['lines_obj'] += 1
            if not cl.search(l):
                continue
            y['lines_obj_and_class'] += 1
            ss = sp.split(l)
            sh = [s.strip() for s in ss if (o1.search(s) or o2.search(s)) and cl.search(s)]
            if sh:
                for s in sh:
                    hits.append(dict(file=f, line=i, kind='sentence', s=s))
                y['sentence_hits'] += len(sh)
            else:
                os_ = [s.strip() for s in ss if o1.search(s) or o2.search(s)][0]
                cs_ = [s.strip() for s in ss if cl.search(s)][0]
                hits.append(dict(file=f, line=i, kind='line', s=os_ + ' [...] ' + cs_))
                y['line_hits'] += 1
    return hits, y


def q0lines(*a):
    """(R286)(3): the Q0 lines -- every hit of the survey with file, line, the sentence and a reading (CONSISTENT with b675's finding, or TO
    RE-CUT), the count printed; nothing cut. data/b676_q0_lines.txt (.json)."""
    hits, y = _q0_hits()
    used = []
    for h in hits:
        h['reading'], h['why'] = 'CONSISTENT', ('the sentence states the finding or a boundary the finding agrees with' if any(
            k in h['s'] for k in Q_CONSISTENT_STATES) else 'names Q0 or the Epstein function without placing it in the kernel`s configuration '
            'class (a witness, a function class, a bench, a window, or a record)')
        for k, (f, n, nd, why) in enumerate(Q_RECUT):
            if h['file'] == f and h['line'] == n and nd in h['s']:
                h['reading'], h['why'] = 'TO RE-CUT', why
                used.append(k)
                break
    miss = [Q_RECUT[k] for k in range(len(Q_RECUT)) if k not in used]
    if miss:
        sys.exit('### A READING`S NEEDLE MATCHES NO HIT -- NOTHING WRITTEN: %s' % miss)
    rc = [h for h in hits if h['reading'] == 'TO RE-CUT']
    L = ['b676 -- COMPONENT 3, (R286)(3): THE Q0 LINES -- EVERY LINE OF THE ROSTER AND THE LEDGERS THAT NAMES Q0 OR THE EPSTEIN INSTANCE AS A '
         'CONFIGURATION, AN INSTANCE OR A MEMBER OF THE KERNEL`S CLASS, OR AS SATISFYING HStrip (%s)' % utc(), '',
         '### the corpus: the 19 roster tables (relay data/b586_corroboration.txt :34) and the two ledgers, FINDINGS.md and OPEN_TRAILS.md, at '
         'PLACE-papers HEAD %s ; nothing cut.' % g(PP, 'rev-parse', '--short', 'HEAD').strip(),
         '### the matchers and their yields (lines): the object, first shape %r: %d ; second shape (Z_Q, the discriminant, the form, the Lean names) '
         '%d ; either %d ; with a class word %r: %d' % (Q_OBJ1, y['lines_obj1'], y['lines_obj2'], y['lines_obj'], Q_CLS, y['lines_obj_and_class']),
         '### a hit is a sentence carrying both (%d) or, where they sit in different sentences of one line, the line (%d); every hit read by hand.' % (
             y['sentence_hits'], y['line_hits']),
         '### the reading: TO RE-CUT where the sentence places Q0 (or the Epstein function) in the kernel`s configuration class -- "the Q0',
         '### configuration", "the Epstein instance" of a theorem over a configuration, its points "the configuration`s" -- which b675`s finding',
         '### contradicts (Zeta23/Defs.lean :142, the strip a field of ZeroConfig); CONSISTENT otherwise, with the reason.',
         '### rows are hits: file :line | kind | reading | the sentence (whole) | why', '']
    for h in hits:
        L.append('  %s :%d | %s | %s | %s | %s' % (h['file'], h['line'], h['kind'], h['reading'], h['s'], h['why']))
    L += ['', '### THE TO RE-CUT ROWS, by file and line (entered as W-ORD-Q0-CLASS-LINES, its trigger "the next re-cut act after b676"):']
    L += ['  %s :%d -- %s' % (h['file'], h['line'], h['why']) for h in rc]
    L += ['', '### ### **HITS %d ; CONSISTENT %d ; TO RE-CUT %d (ON %d LINES: FINDINGS %d, OPEN_TRAILS %d, ROSTER %d) ; NOTHING CUT.**' % (
        len(hits), len(hits) - len(rc), len(rc), len(set((h['file'], h['line']) for h in rc)),
        sum(1 for h in rc if h['file'] == 'FINDINGS.md'), sum(1 for h in rc if h['file'] == 'OPEN_TRAILS.md'),
        sum(1 for h in rc if h['file'] not in ('FINDINGS.md', 'OPEN_TRAILS.md')))]
    put_txt('b676_q0_lines.txt', L)
    put_json('b676_q0_lines.json', dict(at=utc(), yields=y, hits=hits, recut=len(rc)))
    print(L[-1])


NINE_ITEM = 14440           # ### OPEN_TRAILS: b672's nine-kernels item
OH = '*Appended 2026-10-17 by b676, under `(R286)`(3) -- W-ORD-Q0-CLASS-LINES, ENTERED:*'
NH = ('*Appended 2026-10-17 by b676 beneath the nine-kernels item (:14440), under `(R286)`(2) and the navigator’s answer on the ‘before’ '
      'bank -- SIDE-trivium’s FIRST RELAY PRINT BANK, AT ITS TAG:*')


def _c3_items():
    j = jl('b676_q0_lines.json')
    rc = [h for h in j.get('hits') or [] if h['reading'] == 'TO RE-CUT']
    nf, no = sum(1 for h in rc if h['file'] == 'FINDINGS.md'), sum(1 for h in rc if h['file'] == 'OPEN_TRAILS.md')
    nr = len(rc) - nf - no
    nl = len(set((h['file'], h['line']) for h in rc))
    ob = (' the %d sentences on %d ledger lines that place Q0 or the Epstein function in the kernel’s configuration class (“the Q0 '
          'configuration”, “the Epstein instance” of a theorem over a configuration, its points “the configuration’s”) -- %d in FINDINGS, %d in '
          'OPEN_TRAILS, %s in the roster -- which b675’s finding contradicts as worded (FINDINGS :8881: ZeroConfig carries the closed strip as a '
          'field of the type, Zeta23/Defs.lean :142 at SIDE-explicit-formula e36ea31, so Q0’s zero set is no configuration of that type), each '
          'banked by file and line with its sentence and its reason (relay data/b676_q0_lines.txt: %d hits read by hand, %d CONSISTENT); '
          'nothing cut in b676. The ledgers being append-only, each is answered by a correction line addressed to it. Trigger “the next '
          're-cut act after b676”. Status: OPEN.' % (len(rc), nl, nf, no, nr if nr else 'none', len(j.get('hits') or []),
                                                      len(j.get('hits') or []) - len(rc)))
    nb = (' SIDE-trivium is not among the nine; its first relay print bank is the hosted runner’s print of the tree tagged v0.1.1 (peeled '
          '135be2e, the merge of db315fe with the tree unchanged; run 39004541707, relay data/b676_axioms_SIDE-trivium_after.txt: 22 '
          'declarations printed, 10 axiom-free, none on sorryAx), the bank at its tag; the bank of run 39004445565 is at main 7074154 (1aac3a9, '
          '9 commits past v0.1, with the workflow and print-list commits) and not at a tag; the two equal line for line '
          '(data/b676_prints_compare.txt). No roster table carries a SIDE-trivium row (relay data/b676_correspondence_dry.txt: no cell '
          'changed).')
    return [('OPEN_TRAILS.md', OH, NL + OH + ob + NL), ('OPEN_TRAILS.md', NH, NL + NH + nb + NL)]


def c3(*a):
    """(R286)(3) and (2): W-ORD-Q0-CLASS-LINES entered on OPEN_TRAILS, and the print-bank line beneath the nine-kernels item; the guarded
    landing. data/b676_record_lines_c3.json."""
    land(_c3_items(), 'b676_record_lines_c3.json', 'c3', check=[('OPEN_TRAILS.md', NINE_ITEM, 'THE KERNELS WITH NO RELAY PRINT BANK AT THEIR TAG')],
         dry='dry' in a)


def orders(*a):
    """(R286)(3): the order's row appended to the orders bank (data/b670_work_orders.txt, additive under (R254)(2): the bank's bytes before the
    append are a prefix of its bytes after), its Status cell filled, its entry line read from the landing's bank."""
    rl = jl('b676_record_lines_c3.json')
    ln = [x['line'] for x in rl.get('lines') or [] if x['head'] == OH]
    if not ln:
        sys.exit('### THE ORDER HAS NOT LANDED -- NOTHING WRITTEN')
    p = os.path.join(D, 'b670_work_orders.txt')
    old = open(p, 'rb').read()
    if b'W-ORD-Q0-CLASS-LINES' in old:
        sys.exit('### THE ORDER IS IN THE BANK ALREADY -- NOTHING WRITTEN')
    add = (NL + '### Appended 2026-10-17 by b676 under (R286)(3) (additive, (R254)(2)): the order entered on OPEN_TRAILS at Component 3, its '
           'Status cell filled.' + NL + '  %-44s :%-5d  b676   0     %-16s :%-5d  the next re-cut act after b676 [:%d]' % (
               'W-ORD-Q0-CLASS-LINES', ln[0], 'OPEN', ln[0], ln[0]) + NL).encode('utf-8')
    sep = b'' if old.endswith(b'\n') else b'\n'
    new = old + sep + add
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/b670_work_orders.txt: %d bytes -> %d ; the prefix kept %s ; the row: %s' % (
        len(old), len(new), open(p, 'rb').read().startswith(old), add.decode('utf-8').strip().split(NL)[-1]))


# ================================================================================ COMPONENT 4: THE STRIP'S USES, (R286)(4) -- read, not attempted
V5F, CPF, CFGF = K.V5_FILE, K.COMP_FILE, 'SIDEExplicitFormula/Schema/LiCfg.lean'
# ### rows: (file, line, needle on that line, the declaration, what is consumed, the step, the bound the step needs, the reading on (-1/2, 3/2)).
# ### The readings are the seat's arithmetic on the step, not compiled; no Lean is written.
STRIP_USES = (
    (V5F, 84, '(h0 : 0 < ρ.re) (h1 : ρ.re < 1)', 'liTerm_re_abs_le_pow', 'the open strip as two binders (supplied at :131 from HStrip)',
     'the per-point bound |Re liTerm n ρ| ≤ 2 (n + 1)² sⁿ / ‖ρ‖²', 'the hypotheses of :88, :94, :95 below', 'as below'),
    (V5F, 88, 'rw [e, Complex.zero_re] at h0', 'liTerm_re_abs_le_pow', 'h0 : 0 < Re ρ', 'ρ ≠ 0', 'ρ ≠ 0 alone',
     'the strip (-1/2, 3/2) contains 0: ρ ≠ 0 must come from elsewhere (0 not a point of the configuration)'),
    (V5F, 94, 'abs_of_pos h0', 'liTerm_re_abs_le_pow', 'h0 : 0 < Re ρ', '|Re ρ⁻¹| = |Re ρ| / ‖ρ‖², the absolute value dropped',
     'Re ρ > 0 as written; the content needs |Re ρ| bounded', 'kept as |Re ρ| / ‖ρ‖² (no sign needed)'),
    (V5F, 95, 'div_le_div_of_nonneg_right h1.le hn2.le', 'liTerm_re_abs_le_pow', 'h1 : Re ρ < 1', '|Re ρ⁻¹| ≤ 1 / ‖ρ‖²', '|Re ρ| ≤ 1',
     '|Re ρ| < 3/2, so |Re ρ⁻¹| ≤ (3/2) / ‖ρ‖²; the constant 2 at :85 still holds (2 (n + 1)² sⁿ - n² sⁿ - (3/2) n ≥ 0 for sⁿ ≥ 1)'),
    (V5F, 125, '(hs : B321.HStrip Z)', 'rest_term_le', 'HStrip Z (binder)', '(V5) per point', 'as :130-:136', 'as below'),
    (V5F, 130, 'have hst : 0 < ρ.re ∧ ρ.re < 1 := hs ρ hmem', 'rest_term_le', 'HStrip Z at the point', 'the open strip at ρ',
     '0 < Re ρ < 1', 'replaced by -1/2 < Re ρ < 3/2'),
    (V5F, 131, 'liTerm_re_abs_le_pow hst.1 hst.2', 'rest_term_le', 'hst.1, hst.2', 'the per-point bound of :84', 'as :84', 'as :88-:95'),
    (V5F, 134, 'have := hst.1', 'rest_term_le', 'hst.1 : 0 < Re ρ', 'ρ ≠ 0 (:132-:136)', 'ρ ≠ 0 alone', 'as :88'),
    (V5F, 147, 'have hstc := Z.strip _ hmem', 'rest_term_le', 'the FIELD ZeroConfig.strip (Zeta23/Defs.lean :142, 0 ≤ Re ρ ≤ 1)',
     'the closed strip at ρ', 'consumed at :150', 'the field itself excludes the object: a configuration with a zero off [0, 1] is no ZeroConfig'),
    (V5F, 150, 'nlinarith [hstc.1, hstc.2]', 'rest_term_le', 'hstc.1, hstc.2', '‖γ(ρ)‖² ≤ (Im ρ)² + 1/4 (γ(ρ) = Im ρ - i (Re ρ - 1/2), '
     'RestBound.lean :140, :145)', '(Re ρ - 1/2)² ≤ 1/4', '(Re ρ - 1/2)² < 1, so ‖γ(ρ)‖² ≤ (Im ρ)² + 1; the constant 2 + 2 (1 + s)² at :157 '
     'still bounds 1 / ‖ρ‖² (1 + ‖γ‖² ≤ 2 + ‖ρ‖² < (2 + 2 (1 + s)²) ‖ρ‖² by :146)'),
    (V5F, 175, '(hs : B321.HStrip Z)', 'remainder_le', 'HStrip Z (binder)', '(V5)', 'as :185', 'as :125'),
    (V5F, 185, 'rest_term_le Z hs hs1 n ρ.2.1 ρ.2.2', 'remainder_le', 'hs', 'every point of the rest', 'as :125', 'as :125'),
    (CPF, 53, '(hs : B321.HStrip Z)', 'exists_dominant_point', 'HStrip Z (binder)', '(V2) on the configuration', 'as :57', 'as :57'),
    (CPF, 57, 'have h0 := (hs σ hσ).1', 'exists_dominant_point', '(hs σ hσ).1 : 0 < Re σ', 'every point ≠ 0 (:55-:59); the orbit step :60-:66 '
     'reads Re ρ ≠ 1/2 and reflect_mem alone', 'σ ≠ 0 alone', 'as :88 (0 lies in the strip)'),
    (CPF, 89, 'have hst := Z.strip ρ hρ', 'dominant_finite', 'the FIELD ZeroConfig.strip', 'the closed strip at ρ', 'consumed at :94', 'as :147'),
    (CPF, 94, 'nlinarith [hst.1]', 'dominant_finite', 'hst.1 : 0 ≤ Re ρ', '(r² - 1) ‖ρ‖² ≤ 1 from r ‖ρ‖ ≤ ‖ρ - 1‖ (:86-:93), so the '
     'ordinates are bounded (:98-:101)', 'Re ρ ≥ 0', 'Re ρ > -1/2 gives (r² - 1) ‖ρ‖² < 2; K = 2 / (r² - 1) in place of 1 / (r² - 1), the window '
     'at :77 widened by that factor; the set finite still'),
    (CPF, 157, '(hs : B321.HStrip Z)', 'li_nonneg_cfg_imp_online', 'HStrip Z (binder)', '(S5)', 'as :164, :216, :244', 'as those rows'),
    (CPF, 164, 'exists_dominant_point Z hs hρ1 hoff', 'li_nonneg_cfg_imp_online', 'hs', '(V2) at the off-line point', 'as :57', 'as :57'),
    (CPF, 216, 'have hst := hs x hxD.1', 'li_nonneg_cfg_imp_online', 'HStrip Z at a dominant point x', 'w ≠ 1 on the dominant set (:213-:232)',
     'as :219, :231', 'as those rows'),
    (CPF, 219, 'have := hst.1', 'li_nonneg_cfg_imp_online', 'hst.1 : 0 < Re x', 'x ≠ 0 (:217-:221)', 'x ≠ 0 alone', 'as :88'),
    (CPF, 231, 'exact div_pos hst.1 (Complex.normSq_pos.mpr hx0)', 'li_nonneg_cfg_imp_online', 'hst.1 : 0 < Re x',
     '0 < Re x⁻¹ against Re x⁻¹ = 1 - R < 0 (:225-:228; R > 1): w = (1 - x⁻¹) / R is never 1', 'no dominant point is the negative real '
     '1 / (1 - R) (Re x ≥ 0 suffices)', 'NOT REACHED BY A CONSTANT: 1 / (1 - R) lies in (-1/2, 0) whenever R > 3, so on (-1/2, 3/2) the step '
     'needs that point excluded by another premise -- the one use of this list the wider strip does not carry by arithmetic alone'),
    (CPF, 244, 'remainder_le Z hc hs hs1', 'li_nonneg_cfg_imp_online', 'hs', '(V5) on the rest', 'as :125', 'as :125-:185'),
)
STRIP_PRODUCERS = ((CPF, 325, 'have hstrip : B321.HStrip (chiZeroConfig χ hχ h1)', 'li_nonneg_chi_imp_grh_chi',
                    'HStrip proved for χ`s configuration from its carrier (:326-:327), S5 applied at :328 -- a producer, not a consumer'),)
STRIP_PRODUCER_LINES = ((CPF, 326, 'unfold B321.HStrip'), (CPF, 328, 'hstrip h s'))      # ### the producer's own lines
STRIP_NAMESAKES = ((CPF, 323, 'fun h s hs h0 h1', 'hs is GRH_chi`s binder for s (a hypothesis on s), not HStrip'),)
STRIP_APART = ((CFGF, 53, 'have hstrip := Z.strip _ hρmem', 'liCoeffCfg_summable (:36)', 'the FIELD, read by summable_indicator_gL '
                '(LiConverseCfg.lean :133-:136, used at :278)', '(Re ρ - 1/2)² ≤ 1/4 at :63 gives the constant 9/4 at :68; on (-1/2, 3/2) with '
                '‖ρ‖ ≥ 1 (:54): 1 + ‖γ‖² ≤ 2 + ‖ρ‖² ≤ 3 ‖ρ‖², the constant 3'),)


def strips(*a):
    """(R286)(4): the Lean lines of V5 (Schema/LiRemainder.lean) and of the composition (Schema/LiConverseCfg.lean) at e36ea31 that consume
    HStrip or the strip field of ZeroConfig, each by file and line with the bound its step needs; every row's needle read on its line by git
    show before the bank is written (a miss stops the route); the docstring lines that name the strip counted apart; the uses outside the two
    files on the composition's path named apart. No Lean written. data/b676_strip_uses.txt (.json)."""
    blobs = dict((f, (_show(K.KE, K.KREV, f) or '').split(NL)) for f in (V5F, CPF, CFGF, K.STRIP_FIELD[0], K.HSTRIP[0]))
    miss = [(f, n, nd) for f, n, nd, *_r in STRIP_USES + STRIP_PRODUCERS + STRIP_PRODUCER_LINES + STRIP_NAMESAKES + STRIP_APART
            if nd not in (blobs[f][n - 1] if n <= len(blobs[f]) else '')]
    sf, hs = blobs[K.STRIP_FIELD[0]][K.STRIP_FIELD[1] - 1].strip(), blobs[K.HSTRIP[0]][K.HSTRIP[1] - 1].strip()
    if miss or not sf.startswith('strip :') or 'def HStrip' not in hs:
        sys.exit('### A ROW`S NEEDLE IS NOT ON ITS LINE AT %s -- NOTHING WRITTEN: %s' % (K.KREV, miss))
    # ### every line of the two files naming hs, HStrip, .strip or hst outside a comment, against the rows: none unlisted
    listed = set((f, n) for f, n, *_r in STRIP_USES + STRIP_PRODUCERS + STRIP_PRODUCER_LINES + STRIP_NAMESAKES)
    cand, doc = [], []
    for f in (V5F, CPF):
        depth = 0
        for i, l in enumerate(blobs[f], 1):
            code = l if depth == 0 else ''
            depth += l.count('/-') - l.count('-/')
            if depth > 0 and '/-' in l and code:
                code = l[:l.index('/-')]
            if re.search(r'\bstrip\b|HStrip|\bhs\b|\bhst\b|\bhstc\b|\bhstrip\b', code) and not code.strip().startswith('--'):
                cand.append((f, i))
            elif re.search(r'(?i)\bstrip\b', l):
                doc.append((f, i))
    unlisted = [c for c in cand if c not in listed]
    L = ['b676 -- COMPONENT 4, (R286)(4): THE STRIP`S USES IN V5 AND THE COMPOSITION AT SIDE-explicit-formula v0.32 (%s), READ AND NOT '
         'ATTEMPTED (%s)' % (K.KREV, utc()), '',
         '### the hypothesis: %s :%d "%s"' % (K.HSTRIP[0], K.HSTRIP[1], hs),
         '### the field: %s :%d "%s" (a field of ZeroConfig: every configuration carries the closed strip)' % (K.STRIP_FIELD[0], K.STRIP_FIELD[1], sf),
         '### the variant a later act states: HStrip on (-1/2, 3/2) (relay data/b675_li_plan.txt :136-:138), the strip (3c) proves at Q0.',
         '### rows are uses: file :line | the line at e36ea31 | the declaration | what is consumed | the step | the bound the step needs | the',
         '### reading on (-1/2, 3/2) (the seat`s arithmetic on the step, not compiled). Every row`s needle read on its line by git show.', '']
    for f, n, nd, decl, what, step, need, var in STRIP_USES:
        L.append('  %s :%d | %s | %s | %s | %s | NEEDS: %s | ON (-1/2, 3/2): %s' % (f.split('/')[-1], n, blobs[f][n - 1].strip(), decl, what,
                                                                                step, need, var))
    L += ['', '### THE PRODUCER (HStrip proved, not consumed):']
    L += ['  %s :%d | %s | %s | %s' % (f.split('/')[-1], n, blobs[f][n - 1].strip(), decl, why) for f, n, nd, decl, why in STRIP_PRODUCERS]
    L += ['  %s :%d | %s | the producer`s own line' % (f.split('/')[-1], n, blobs[f][n - 1].strip()) for f, n, nd in STRIP_PRODUCER_LINES]
    L += ['', '### A NAMESAKE (the name, not the hypothesis):']
    L += ['  %s :%d | %s | %s' % (f.split('/')[-1], n, blobs[f][n - 1].strip(), why) for f, n, nd, why in STRIP_NAMESAKES]
    L += ['', '### APART -- outside the two files, on the composition`s path (named, not counted):']
    L += ['  %s :%d | %s | %s | %s | ON (-1/2, 3/2): %s' % (f.split('/')[-1], n, blobs[f][n - 1].strip(), decl, what, var)
          for f, n, nd, decl, what, var in STRIP_APART]
    L += ['', '### THE COMPLETENESS READ: every code line of the two files naming hs, hst, hstc, hstrip, HStrip or strip: %d ; listed above %d ; '
          'unlisted %s' % (len(cand), len(cand) - len(unlisted), ['%s :%d' % (f.split('/')[-1], n) for f, n in unlisted] or 'NONE'),
          '### the comment and docstring lines naming the strip (prose, not uses): %s' % ', '.join('%s :%d' % (f.split('/')[-1], n) for f, n in doc),
          '', '### ### **USES %d (V5 %d, THE COMPOSITION %d) ; THE FIELD READ AT %d ; ONE STEP NOT REACHED BY A CONSTANT (LiConverseCfg.lean :231) '
          '; PRODUCER %d ; APART %d ; UNLISTED %d ; NO LEAN WRITTEN.**' % (
              len(STRIP_USES), sum(1 for r in STRIP_USES if r[0] == V5F), sum(1 for r in STRIP_USES if r[0] == CPF),
              sum(1 for r in STRIP_USES if 'Z.strip' in r[2]), len(STRIP_PRODUCERS), len(STRIP_APART), len(unlisted))]
    put_txt('b676_strip_uses.txt', L)
    put_json('b676_strip_uses.json', dict(at=utc(), rev=K.KREV, uses=[list(r[:4]) for r in STRIP_USES], unlisted=unlisted, doc=doc))
    print(NL.join(L[-5:]))


# ================================================================================ THE AUTHOR'S ANSWERS (b675's route, carried)
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
    """data/b676_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; every word of the author
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
    head = ['### b676 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d)%s.' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start,
                ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a) for s, a in K.SESSIONS_AFTER)), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b676_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b676_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b675's, carried by the Edit tool; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def read_runner_row(r):
    """a row of data/b676_runner_rows.json (this act's runs, SIDE-trivium's): the kernel, a label (before or after), a 40-hex ref, a run id, a
    gate; returns (label, gate). Carried from b675_record.py's reader with this act's kernel."""
    if not isinstance(r, dict) or r.get('kernel') != K.CANDIDATE or r.get('label') not in ('before', 'after') \
            or not re.match(r'^[0-9a-f]{40}$', r.get('ref') or '') or not isinstance(r.get('run_id'), int) or r.get('gate') not in ('DERIVES', 'NOT DERIVES'):
        raise ValueError('runner row of another shape: %r' % (r,))
    return r['label'], r['gate']


READING_WORDS = ('CONSISTENT', 'TO RE-CUT')


def read_q0_row(r):
    """a hit of data/b676_q0_lines.json: a file, a line (an int), a kind (sentence or line), the sentence, a reading (one of READING_WORDS)
    and its reason; returns (file, line, reading)."""
    if not isinstance(r, dict) or not r.get('file') or not isinstance(r.get('line'), int) or r.get('kind') not in ('sentence', 'line') \
            or not (r.get('s') or '').strip() or r.get('reading') not in READING_WORDS or not r.get('why'):
        raise ValueError('q0 row of another shape: %r' % (r,))
    return r['file'], r['line'], r['reading']


READERS += ['read_runner_row', 'read_q0_row']


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
    L = ['b676 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES AND THE MOVES AND DELETES (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES, ONE PER TREE STATE (%d):' % len(disp)] + (['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; MOVE OR DELETE COMMANDS %d.**' % (
        len(rows), len(hits), len(lean), len(disp), len(mv))]
    put_txt('b676_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b676_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], moves_deletes=[r['n'] for r in mv]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r in mv:
        print('  MOVE OR DELETE #%d: %s' % (r['n'], r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', K.CANDIDATE]      # ### SIDE-window and the kernel this act cut, beside b641's thirteen


def kernels(*a):
    ks = _kerns()
    put_json('b676_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b676_defects.txt').split(NL)
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
    t = rdn('b676_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b676_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b676_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b676_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


# ================================================================================ COMPONENT 5: THE CARRY-TIME REPAIRS ((R286)'s ferry)
def repairs(*a):
    """data/b676_tool_repairs.txt: rows are repairs with the defect they answer; each carried tool read against b675's seal hash (relay
    data/b675_seal_hashes.json) first; each repair shown by the hunks of the diff against that sealed copy that carry it, and run on real
    banks both ways (the sealed copy's reading beside the repaired one)."""
    import hashlib
    seal = jl('b675_seal_hashes.json').get('tools') or {}
    rows = []
    for t5, t6 in (('b675_citation.py', 'b676_citation.py'), ('b675_closing.py', 'b676_closing.py')):
        old, new = os.path.join(T, t5), os.path.join(T, t6)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t5, now, seal.get(t5), re.split(r'(?m)^(?=@@ )', d)[1:]))
    pick = lambda hunks, keys: [h for h in hunks if any(k in h for k in keys)]   # noqa: E731
    h1 = pick(rows[0][3], ("rfind('BEGIN'", 'b0, e0'))
    h2 = pick(rows[1][3], ('(?:navigator`s )?answer carrying',))
    # ### (1) the mid-act reader on this act's own result: both answers in one result, each cut out by its BEGIN..END
    res = [t for t in __import__('b676_citation')._user_texts() if 'on the print list' in t and 'on the ‘before’ bank' in t]
    whole = res[-1] if res else ''
    cut = []
    for nd in ('on the print list', 'on the ‘before’ bank'):
        k = whole.find(nd)
        b0, e0 = whole.rfind('BEGIN', 0, k), whole.find('END', k)
        cut.append(len(whole[b0:e0 + 3]) if b0 >= 0 and e0 > k else 0)
    # ### (2) the closing's citation line: the sealed needle against this act's citation bank, the repaired one beside it
    cc = rdn(K.CITATION_BANK)
    old_n = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the navigator`s answer carrying '([^']*)'", cc, re.M)
    new_n = re.findall(r"^### \(R278\)\(4\) THE MID-ACT CHECK \([^)]*\): the (?:navigator`s )?answer carrying '([^']*)'", cc, re.M)
    L = ['b676 -- COMPONENT 5, (R286)`S FERRY: THE CARRY-TIME REPAIRS, AGAINST b675`S SEALED COPIES (%s)' % utc(), '']
    for t5, now, s, _h in rows:
        L.append('### b675`s sealed copy: tools/%s sha256 %s ; the seal`s record %s ; %s' % (t5, now[:16], (s or '### NONE')[:16],
                                                                                         'AGREE' if s == now else '### DIFFER'))
    L += ['### rows are repairs, each with the defect it answers, the diff`s hunks (b675 -> b676) that carry it, and its reading on real banks.',
          '### The other differences of the carried tools are the act`s own text (its names, its banks and its sections), not repairs.', '',
          '  REPAIR 1 -- THE MID-ACT CHECK CUTS EACH ANSWER OUT OF A RESULT THAT CARRIES SEVERAL. Answers b675 defect (j) and b676 defect (b)',
          '  (tools/b676_citation.py, made before its seal). Hunks %d:' % len(h1)]
    L += ['    ' + l for h in h1 for l in h.rstrip(NL).split(NL)]
    L += ['  on this act`s result carrying both navigator answers (%d characters): the sealed reading takes the whole result for each needle; the '
          'repaired reading takes %d and %d characters' % (len(whole), cut[0], cut[1])]
    L += ['', '  REPAIR 2 -- THE CLOSING`S CITATION LINE READS THE MID-ACT CHECK`S HEADER IN BOTH WORDINGS. Answers the citation tool`s header',
          '  ("the answer carrying", since the route reads the author`s tool results as well as the navigator`s pasted answers), which the',
          '  sealed needle ("the navigator`s answer carrying") reads as no check at all. Hunks %d:' % len(h2)]
    L += ['    ' + l for h in h2 for l in h.rstrip(NL).split(NL)]
    L += ['  on relay %s: the sealed needle finds %d checks ; the repaired needle finds %d (%s)' % (K.CITATION_BANK, len(old_n), len(new_n),
                                                                                                  '; '.join(new_n) or 'NONE')]
    ok1 = bool(h1) and all(0 < c < len(whole) for c in cut)
    ok2 = bool(h2) and len(new_n) > len(old_n) == 0
    L += ['', '### ### **REPAIRS 2 ; THE SEALED COPIES %s ; HUNKS %d AND %d ; EACH ANSWER CUT FROM ITS RESULT %s ; THE CHECKS READ BY THE CLOSING %s.**' % (
        'AGREE' if all(s == now for _t, now, s, _h in rows) else '### DIFFER', len(h1), len(h2), ok1, ok2)]
    put_txt('b676_tool_repairs.txt', L)
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b676_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands|'
                          r'mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b676_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(K.SHARED_APPENDED))


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if not b_.endswith('.gz') and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b676_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b676'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b676_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith('.gz')][0]
    with tempfile.TemporaryDirectory(prefix='b676_ra_') as tmp:
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
    L = ['b676 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b676_root_arm.txt', L)
    put_json('b676_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b676 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b676_table_final.txt', L)
    put_json('b676_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b676_registration_2026-10-17.txt'
FACE = os.path.join(D, 'b676_registration_2026-10-17.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b676_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b676_regspec.py')], 'b676_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b676_satisfiable.json', '--emit', 'b676'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b676_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b676_census_stepzero.txt'), ('b327_faces_census.py', 'b676_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b676_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b676'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b676_reg_gate.txt', 'data/b676_reg_termscan.txt', 'data/b676_regspec_run.txt', 'data/audit_b676_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
# ### carried from b675_record.py by the Edit tool, every predicate re-written against (R286)'s expectations and this act's banks
import collections                 # noqa: E402
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b675_closing_push_out.txt', 'b670_work_orders.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
N5_TRIVIUM = ('.github/workflows/build-module.yml', 'print_targets.txt', 'Trivium/Bijection.lean')


def TRAIL_HEAD():
    return ('### b676 — lane two, act one hundred and three, the re-cut act under (R286): SIDE-trivium’s docstrings re-cut, v0.1.1; the Q0 '
            'lines read and banked; the strip’s uses in V5 and the composition listed')


def _calls():
    return jl('b676_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', *N5_PP)
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _epoch(ts):
    import calendar
    return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S')) if ts else None


def _prompt_of(header):
    """the prompt the answers bank carries under `header`: (its text, its call's time as an epoch), or (None, None)."""
    L = rdn('b676_author_answers.txt').split(NL)
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


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _n1():
    cm = jl('b676_commands.json')
    ok = bool(cm) and not cm.get('local_lean')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s (relay data/b676_commands.txt, %d commands read); the builds on the hosted '
        'runner alone, dispatched %d times, one per tree state (runs %s)' % (cm.get('local_lean') if cm else '### UNREAD', len(cm.get('rows') or []),
                                                                              len(cm.get('dispatches') or []), ', '.join(str(r) for r, _l in K.T_RUNS)))


def _n2():
    nj = jl('b676_naming.json')
    nt = rdn('b676_naming.txt')
    n_at = _epoch(nj.get('at'))
    first_branch = _git_ct(K.TD, K.T_WORKFLOW)
    rule_i, table_i, named_i = nt.find('### THE RULE, verbatim'), nt.find('### THE TABLE ROWS, verbatim'), nt.find('### THE NAMING:')
    wf_i = nt.find('### THE NAMED KERNEL`S WORKFLOW DIRECTORY AND PRINT BANK (read before any branch is made)')
    ok = bool(nj) and 0 <= rule_i < table_i < named_i < wf_i and n_at and first_branch and n_at < first_branch and nj.get('named') == K.CANDIDATE
    return ('HELD' if ok else 'REFUTED'), (
        'the rule row (relay data/b674_rules.txt :8) and the table rows (data/b670_licensed_table.txt, data/b647_table_kernels.txt) printed '
        'verbatim before the naming line in relay data/b676_naming.txt (written %s); the workflow directory and the print bank read there '
        'and declared absent; the first kernel write (the workflow commit %s, %s) and every branch after it: the order %s' % (
            nj.get('at'), K.T_WORKFLOW, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(first_branch)) if first_branch else '### NONE', bool(ok)))


def _pin_blocks(cut):
    """each MATCHES row of the cut bank read whole and unwrapped, from its `pin:` to the next row (a cite that wraps to its next line read
    as one, b675's trap): the pin texts."""
    blocks = re.split(r'(?m)^(?=  Trivium/\S+\.lean:\d+)', cut.split('### THE DISTANCE BY')[0])[1:]
    return [' '.join(b.split('pin:', 1)[1].split()) for b in blocks if 'after MATCHES' in b and 'pin:' in b]


def _n3():
    cut = rdn('b676_cut.txt')
    v = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', cut)
    pc = rdn('b676_prints_compare.txt')
    rows = jl('b676_runner_rows.json').get('rows') or []
    try:
        gates = dict(read_runner_row(r) for r in rows)
    except Exception:
        gates = {}
    pins = _pin_blocks(cut)
    pin_ok = len(pins) == 4 and all(re.search(r':\d+', p_) for p_ in pins)
    ok = bool(v) and int(v.group(2)) <= int(v.group(1)) and 'EQUAL LINE FOR LINE True' in pc and gates == {'before': 'DERIVES', 'after': 'DERIVES'} \
        and pin_ok and 'MERGED 135be2e, v0.1.1 ; PRINTS EQUAL' in cut
    return ('HELD' if ok else 'REFUTED'), (
        'the distance by b670`s method before %s, after %s (relay data/b676_cut.txt); the four pinned rows each citing a path and line at the '
        'peeled tag v0.1.1 (135be2e) %s; the `before` and `after` prints %s (data/b676_prints_compare.txt), both runs %s' % (
            v.group(1) if v else '?', v.group(2) if v else '?', pin_ok, 'equal line for line' if 'EQUAL LINE FOR LINE True' in pc else '### NOT EQUAL',
            gates or '### UNREAD'))


def _n4():
    q = jl('b676_q0_lines.json')
    try:
        got = [read_q0_row(h) for h in q.get('hits') or []]
    except Exception:
        got = []
    su = rdn('b676_strip_uses.txt')
    uses = re.findall(r'^  (\S+\.lean) :(\d+) \| ', su.split('### THE PRODUCER')[0], re.M)
    ok = bool(got) and len(got) == len(q.get('hits') or []) and 'UNLISTED 0 ; NO LEAN WRITTEN' in su and len(uses) == len(jl('b676_strip_uses.json').get('uses') or [0])
    return ('HELD' if ok else 'REFUTED'), (
        'every Q0 hit through the reader with a file, a line, the sentence and a reading: %d of %d (relay data/b676_q0_lines.txt, %d TO RE-CUT); '
        'every strip use cited by file and line: %d rows (data/b676_strip_uses.txt), unlisted %s' % (
            len(got), len(q.get('hits') or []), q.get('recut', 0), len(uses), 'UNLISTED 0' in su))


def _n5():
    face = jl('b676_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    t_writes = [l for l in g(K.TD, 'log', '--first-parent', '--format=%h', '%s..main' % K.T_PRE_MAIN).split(NL) if l.strip()]
    t_files = sorted(set(x for x in g(K.TD, 'diff', '--name-only', K.T_PRE_MAIN, 'main').split(NL) if x.strip()))
    t_ok = t_files == sorted(N5_TRIVIUM) and len(t_writes) == 3 and g(K.TD, 'rev-parse', '--short=7', K.T_NEXT_TAG + '^{commit}').strip() == '135be2e'
    wf_t = (_show(K.TD, 'main', '.github/workflows/build-module.yml') or '').lower()
    ident = [w for w in ('psinary', 'hotmail', 'seale', 'york', 'orcid', 'secrets.') if w in wf_t]
    ke_main = g(K.KE, 'rev-parse', 'main').strip() == K.MERGE
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b676_|audit_b676_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b676_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = others_ok and t_ok and ke_main and not ident and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); kernel mains: SIDE-trivium`s main written by its three '
            'first-parent commits (the workflow commit, the print-list commit, the docstring merge) and the tag %s, the files %s, %s, as N5 '
            'amended reads it; every other kernel as the face read it %s, SIDE-explicit-formula`s main at %s %s; PLACE-papers beyond FINDINGS '
            'and OPEN_TRAILS: %s; standing arms added: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; relay files of a '
            'kind beyond the banks, the act`s tools, the table, the root list, b675`s push-out bank and the orders bank`s appended row: %s; '
            '"patent" in the lines written: %s; an identifier of the author in the workflow file: %s; outbound requests: the seat`s git reads '
            'and pushes, its two dispatches and its run and artifact reads at github.com, so no identifier of the author placed in a request' % (
                K.DRAFT, K.T_NEXT_TAG, t_files, t_ok, others_ok, K.MERGE[:7], ke_main, pp_beyond or 'NONE', new_arms or 'NONE', len(K.ACT_ARMS),
                differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE', ident or 'NONE'))


def scores(*a):
    TF, RA = jl('b676_table_final.json'), jl('b676_root_arm.json')
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
    put_json('b676_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _cut_fig():
    m = re.search(r'THE DISTANCE BEFORE (\d+), AFTER (\d+)', rdn('b676_cut.txt'))
    return (m.group(1), m.group(2)) if m else ('?', '?')


def _title():
    q = jl('b676_q0_lines.json')
    b, a_ = _cut_fig()
    nu = len(re.findall(r'^  \S+\.lean :\d+ \| ', rdn('b676_strip_uses.txt').split('### THE PRODUCER')[0], re.M))
    return ('## SIDE-trivium docstrings re-cut: %s rows outside LICENSED/CITED to %s, %s; Q0 lines read: %s, %s to re-cut; the strip’s uses in V5 '
            'and the composition listed: %d' % (b, a_, K.T_NEXT_TAG, len(q.get('hits') or []) or '?', q.get('recut', '?'), nu))


def _finding_text():
    S, J = jl('b676_scores.json'), jl('b676_act_root.json')
    q = jl('b676_q0_lines.json')
    b, a_ = _cut_fig()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b676_author_answers.txt'), re.M))
    c1 = _rl_lines('b676_record_lines.json') + ['?']
    c3 = _rl_lines('b676_record_lines_c3.json') + ['?', '?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    mids = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    rc = [h for h in q.get('hits') or [] if h['reading'] == 'TO RE-CUT']
    nu = len(re.findall(r'^  \S+\.lean :\d+ \| ', rdn('b676_strip_uses.txt').split('### THE PRODUCER')[0], re.M))
    e = ['', _title(), '',
         'SIDE-trivium’s docstrings and module header now say what the kernel compiles at its tag %s: of the five rows outside LICENSED or CITED, '
         'four match and one is cut in part (the header’s list re-cut, its introduction’s “correspond exactly” standing), the 22 prints equal '
         'before and after on the hosted runner; the corpus carries %d sentences that place Q0 in the kernel’s configuration class, which b675’s '
         'finding contradicts, banked for the next re-cut act and not cut; and the variant hypothesis HStrip on (−1/2, 3/2) now has its %d uses '
         'listed by Lean line, one of which (LiConverseCfg.lean :231) a wider strip does not carry by a constant. Nothing here proves RH or GRH.' % (
             K.T_NEXT_TAG, len(rc), nu), '',
         '*Filed at b676 on the author’s ruling `(R286)` and the navigator’s answers (%d questions in %d call%s). Banks: relay '
         '`data/b676_naming.txt`, `data/b676_cut.txt`, `data/b676_cut_diff.txt`, `data/b676_prints_compare.txt`, `data/b676_q0_lines.txt`, '
         '`data/b676_strip_uses.txt`, `data/b676_tool_repairs.txt`, `data/b676_act_root.txt`.*' % (n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- the ruling’s “the arm named and the bank '
         'that records its removal”: no arm was removed, the standing 68 carried whole and the act arms minted per act, b674’s 16 and b675’s 15 '
         '-- entered by the fact clause; the mid-act checks of `(R278)`(4), %d prints for the two answers, the first two reading their one result '
         'whole and the last of each with %s missed. b675 at its weight, its closing’s head line quoted (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', len(mids),
             'none' if mids and all(m_[2] == '0' for m_ in mids[-2:]) else '### SOME', c1[0]), '',
         '**The re-cut** (`(R286)`(2)): the rule row and the table rows printed from their banks before the document was named; SIDE-trivium the '
         'greatest count standing (5, no tie; the rule of b674’s row 2 not reached); its workflow directory carrying build.yml alone and no relay '
         'print bank, read before any branch; on the navigator’s answers, build-module.yml and print_targets.txt (22 names) committed alone on '
         'its main (dd587f9, 7074154, no .lean byte), the `before` run at that main (39004445565, the print bank AT MAIN, 1aac3a9 being 9 '
         'commits past v0.1), the cut on recut-trivium-b676 (db315fe, the text with every comment stripped unchanged), the `after` run '
         '(39004541707), both DERIVES, 22 prints equal line for line; merged as 135be2e, tag %s peeled 135be2e at the remote. The distance by '
         'b670’s method %s to %s. No roster table carries a SIDE-trivium row, so no Correspondence cell moved; the `after` bank entered against '
         'the nine-kernels item (OPEN_TRAILS :%s).' % (K.T_NEXT_TAG, b, a_, c3[1]), '',
         '**The Q0 lines** (`(R286)`(3)): the 19 roster tables and the two ledgers searched by two object shapes and a class shape, every hit read '
         'by hand: %d hits, %d CONSISTENT, %d TO RE-CUT on %d ledger lines (FINDINGS %d, OPEN_TRAILS %d, the roster none); nothing cut; '
         '`W-ORD-Q0-CLASS-LINES` entered (OPEN_TRAILS :%s), its trigger the next re-cut act after b676, its row in the orders bank with Status '
         'OPEN.' % (len(q.get('hits') or []), len(q.get('hits') or []) - len(rc), len(rc), len(set((h['file'], h['line']) for h in rc)),
                    sum(1 for h in rc if h['file'] == 'FINDINGS.md'), sum(1 for h in rc if h['file'] == 'OPEN_TRAILS.md'), c3[0]), '',
         '**The strip’s uses** (`(R286)`(4)): from SIDE-explicit-formula at e36ea31, %d uses of HStrip or the field ZeroConfig.strip '
         '(Zeta23/Defs.lean :142) in V5 (Schema/LiRemainder.lean) and the composition (Schema/LiConverseCfg.lean), each with the bound its step '
         'needs and its reading on (−1/2, 3/2): the constants of V5 stand or widen by a factor; ρ ≠ 0 must come from elsewhere, the strip holding '
         '0; and w ≠ 1 on the dominant set (LiConverseCfg.lean :231) needs the negative real 1/(1 − R) excluded once R > 3. No Lean written.' % nu, '',
         '**The tools** (the ferry’s Component 5): carried from b675’s sealed copies with two repairs at carry -- the mid-act check cutting each '
         'answer from a result that carries several, and the closing’s citation line reading the check’s header in both wordings -- each run '
         'on real banks (relay data/b676_tool_repairs.txt); the closing dry-run a gate step before the seal.', '',
         '**The root.** b676 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b647’s table of SIDE-trivium and b670’s licensed table, b674’s route '
         'and rule, and b675’s finding (FINDINGS :8881) against every ledger line before it; it is re-read by the next re-cut act, which takes '
         '`W-ORD-Q0-CLASS-LINES`, and by b679’s research act on the strip variant, which states it from relay data/b676_strip_uses.txt. It '
         'strengthens the programme’s offerings of kernel docstrings that say what they compile and of a corpus whose readings of its control '
         'object agree with the kernel’s type.', '',
         '**Carried to:** SIDE-trivium’s header introduction (:8, :23 at %s) and SIDE-window’s Sawtooth marker at :17, for the next re-cut of '
         'their kernels; `W-ORD-Q0-CLASS-LINES`; the strip variant, b679; the draft held at v5.' % K.T_NEXT_TAG, '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the document named by the descending count, no tie at 5 so the rule of b674’s row 2 not reached (relay data/b676_naming.txt); '
              '(2) the ACTIONs applied verbatim and not extended, so the header’s introduction stands as b674 left SIDE-window’s marker; (3) the '
              'Q0 reading TO RE-CUT wherever a sentence names Q0’s zero set “the configuration” or the Epstein file “the instance”, CONSISTENT '
              'where it names Epstein as a witness, a function class or a boundary; (4) the merge carrying print_targets.txt, the one non-comment '
              'file, by the navigator’s answer on the print list')


def _trail_text():
    S, J = jl('b676_scores.json'), jl('b676_act_root.json')
    fj = jl('b676_findings.json')
    q = jl('b676_q0_lines.json')
    b, a_ = _cut_fig()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b676_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b676_record_lines.json')
    c3 = _rl_lines('b676_record_lines_c3.json')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R286) ratified.** (1) b675 at its weight. (2) The re-cut in b674’s form. (3) The Q0 reading. (4) The variant hypothesis, read and '
             'not attempted. (5) The branches. (6) The read-first bank. (7) The draft held at v5. (8) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b675’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-Q0-CLASS-LINES`), :%s (the print bank beneath '
             'the nine-kernels item); this record.' % (c1[0] if c1 else '?', fj.get('entry_line'), c3[0] if c3 else '?', c3[1] if len(c3) > 1 else '?'), '',
             '**Act root:** b676 `%s` (previous `%s`, b675’s; relay data/act_roots.txt), computed after the last bank it names, every one of them '
             'LF.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b676_author_answers.txt); none after the root.' % (n_ans, len(_calls())), '',
             '**The re-cut:** SIDE-trivium %s to %s by b670’s method; main 135be2e, tag %s; runs %s; prints equal.' % (
                 b, a_, K.T_NEXT_TAG, ' and '.join(str(r) for r, _l in K.T_RUNS)), '',
             '**The Q0 lines:** %d hits, %d TO RE-CUT, nothing cut (relay data/b676_q0_lines.txt); **the strip’s uses:** relay '
             'data/b676_strip_uses.txt.' % (len(q.get('hits') or []), q.get('recut', 0)), '',
             '**The open orders:** `W-ORD-Q0-CLASS-LINES` (the next re-cut act after b676); `W-ORD-MAP-ANGLE-FORM` (b677); `W-ORD-PRINT-TARGETS`; '
             '`W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; `W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; the ledger split at '
             'the b680 reading act; the strip variant, b679.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b676_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b676_scores.json')
    L = ['=' * 104, 'b676 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b676_defects.txt').rstrip(NL).split(NL)
    put_txt('b676_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b676_scores.json', 'b676_findings.json', 'b676_trail.json', 'b676_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b676_record_lines.json') + ['?']
    c3 = _rl_lines('b676_record_lines_c3.json') + ['?', '?']
    L = ['b676 -- THE COMPONENTS, BANKED UNDER (R286).', '',
         '### COMPONENT 0 : the citation check (data/b676_citation_check.txt), step zero (data/b676_ferry.txt, data/b676_readfirst.txt, '
         'data/b676_stepzero.txt, data/b676_tests_stepzero.txt, data/b676_rowgen_stepzero.txt, data/b676_branches.txt)',
         '### COMPONENT 1 : b675`s weight FINDINGS :%s' % c1[0],
         '### COMPONENT 2 : the naming (data/b676_naming.txt), the cut (data/b676_cut.txt, data/b676_cut_diff.txt), the runs, the prints '
         '(data/b676_prints_compare.txt), the generator dry (data/b676_correspondence_dry.txt) ; N2 %s ; N3 %s' % (S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the Q0 lines (data/b676_q0_lines.txt) ; W-ORD-Q0-CLASS-LINES OPEN_TRAILS :%s ; the print bank beneath the nine-kernels '
         'item :%s ; N4 %s' % (c3[0], c3[1], S['N4'][0]),
         '### COMPONENT 4 : the strip`s uses (data/b676_strip_uses.txt)',
         '### COMPONENT 5 : the carry-time repairs (data/b676_tool_repairs.txt), the dry-run steps (data/b676_reg_gate.txt), the seal '
         '(data/b676_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b676_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b676_findings.json', dict(title=t))
    j = jl('b676_findings.json')
    j['entry_line'] = ln
    put_json('b676_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b676_trail.json', {})
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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'naming': naming, 'runner': runner, 'prints': prints, 'cutdiff': cutdiff,
          'corr': corr, 'q0lines': q0lines, 'c3': c3, 'orders': orders, 'strips': strips, 'answers': answers, 'commands': commands,
          'kernels': kernels, 'defects': defects, 'repairs': repairs, 'root': root, 'root_arm': root_arm, 'table_final': table_final,
          'gatebanks': gatebanks, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail,
          'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b676_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
