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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'naming': naming, 'runner': runner, 'prints': prints, 'cutdiff': cutdiff,
          'corr': corr}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b676_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
