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


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'naming': naming, 'runner': runner, 'prints': prints, 'cutdiff': cutdiff,
          'corr': corr, 'q0lines': q0lines, 'c3': c3, 'orders': orders, 'strips': strips}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b676_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
