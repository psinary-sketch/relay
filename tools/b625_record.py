# -*- coding: utf-8 -*-
"""b625_record.py -- THE ACT'S RECORD TOOL, UNDER (R235). ### ONE SUBCOMMAND PER BANK.

### ### b625: LANE THREE, ACT FIFTY-TWO -- THE 2/3 THEOREM VENDORED FROM Zeta23 INTO SIDE-explicit-formula AT v0.22 AND
### exceptional_mass_le_third RE-READ; THE 33 LEDGER-AGAINST-RULE NODES CLASSED UNDER THE DOMAIN-CONDITION CRITERION; THE ROOT'S
### LIST WIDENED.
### Subcommands write only `data/b625_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b625_worklist.py. No platform call. The E0 rule as it stood before the act is read from
### its blob at relay PRE_RELAY, never from memory. The case counter is (R233)(3)'s standing form (OPEN_TRAILS :12889); the N5 scorer
### takes the trail record's expected line (OPEN_TRAILS :12799).
### b624's defects' sources repaired here: (b) the data module names nodes in their namespaces (relay e6781b18); (d) every head this
### tool compares with a ledger line is compared after the ledger's own possessive conversion; (e) a control's bank line and the
### pattern that reads it are one format string (CONTROL_FMT).
"""
import difflib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b625_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PLANTED = SP + '/b625_planted'
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b625_registration_2026-10-05.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')


def _w(name):
    """### where a bank is WRITTEN: the scratchpad under `dry`, relay data otherwise."""
    return os.path.join(SP if DRY else D, name)


def _r(name):
    """### where a bank is READ: relay data, always."""
    return os.path.join(D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _w(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_r(name), encoding='utf-8'))


def jx(name):
    return jl(name) if os.path.exists(_r(name)) else {}


def rd(name):
    p = _r(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    return K.lines_of(t)


def _rel(n, rev=PRE_RELAY):
    return _show(RELAY, rev, 'data/' + n) or ''


def _scan(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout or ''


def _clean(out):
    return re.search(r'^\s*VERDICT\s*: CLEAN\s*$', out, re.M) is not None


def _write(path, b):
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b625_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b625 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b625_defects.txt', L)


# ================================================================================ THE CASE COUNTER, (R233)(3)'s standing form
COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    """### a test's cases are the lines its own case pattern matches, never its summary lines (OPEN_TRAILS :12889)."""
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the vendor work-order, the E0 induction work-order, the form, the precedence order, the act root, the authority '
         'order, the build clause, the N5 line, b624`s record lines, record and correction', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12210, 12228, 12290, 12292, 12354, 12356, 12436, 12438, 12799] + list(range(12919, 12954)), 1500),
        ('FINDINGS: b624`s weight line and entry; the step lemma`s cell', PP, PRE_PP, 'FINDINGS.md', [7058, 7510, 7512], 600),
        ('relay data/b624_e0_nodes.txt, whole', RELAY, PRE_RELAY, 'data/b624_e0_nodes.txt', ('ALL',), 300),
        ('relay tools/e0_rule.py after f648d5a5: the domain pattern, the binder pattern, the class predicates and the grade function',
         RELAY, PRE_RELAY, 'tools/e0_rule.py', [45, 55, 65] + list(range(232, 250)), 300),
        ('SIDE-explicit-formula v0.17: structure SimpleProportion and exceptional_mass_le_third', K.KER, K.V017[0],
         'SIDEExplicitFormula/Simplicity.lean', list(range(40, 50)), 300),
        ('SIDE-explicit-formula main: the same lines', K.KER, 'main', 'SIDEExplicitFormula/Simplicity.lean', list(range(40, 50)), 300),
        ('SIDE-explicit-formula main: the vendored set`s head-line form (Zeta23/Defs.lean)', K.KER, 'main', 'Zeta23/Defs.lean',
         list(range(1, 16)), 300),
        ('SIDE-explicit-formula main: the vendoring commit`s subject', K.KER, 'main', 'GIT-LOG', ('LOG', K.VENDOR_COMMIT), 300),
        ('SIDE-explicit-formula main: lakefile.toml and lean-toolchain', K.KER, 'main', 'lakefile.toml', ('ALL',), 300),
        ('SIDE-explicit-formula main: lean-toolchain', K.KER, 'main', 'lean-toolchain', ('ALL',), 300),
        ('anthropics/formal-math at v1.0 = 3635e748: thmB₀_mult', K.UP, K.UP_PIN, K.UP_FILE, list(range(343, 355)), 300),
        ('anthropics/formal-math at v1.0: FinalMult.lean`s imports', K.UP, K.UP_PIN, K.UP_FILE, ('GREP', r'^import '), 300),
        ('anthropics/formal-math at v1.0: lakefile.toml', K.UP, K.UP_PIN, 'lakefile.toml', ('ALL',), 300),
        ('anthropics/formal-math at v1.0: lean-toolchain', K.UP, K.UP_PIN, 'lean-toolchain', ('ALL',), 300),
        ('relay tools/act_root.py: the census reader and the repository list', RELAY, PRE_RELAY, 'tools/act_root.py', list(range(65, 82)), 300),
        ('relay data/act_roots.txt', RELAY, PRE_RELAY, 'data/act_roots.txt', ('ALL',), 300),
        ('the census v0.4`s kernel column head', PP, PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', [41, 43], 400),
        ('REGISTRY`s kernel rows (a kernel`s name alone in a row`s first or second cell)', PP, PRE_PP, 'REGISTRY.md', [562, 563, 703, 715, 716, 717, 718], 200),
        ('the two pages` pin sentences', PP, PRE_PP, K.PAGE, [3], 600),
        ('the χ page`s pin sentence', PP, PRE_PP, K.DIR_PAGE, [3], 600),
        ('relay data/b624_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b624_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b625 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if isinstance(sel, tuple) and sel[0] == 'LOG':
            s = g(repo, 'log', '-1', '--format=%h %ad %s', '--date=short', sel[1]).strip()
            L.append('### %s -- %s (1 line)' % (label, sel[1]))
            L.append('    %s' % s[:width])
            continue
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        elif isinstance(sel, tuple) and sel[0] == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b625_reads.txt', L)


def act_from():
    """### the transcript line at which this act's ferry was pasted (the first user message carrying `RULING (R235) BEGIN`)."""
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R235) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    since = [c for c in calls if c[0] > act_from()]
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b625 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in since:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not since:
        L.append('### NONE YET: no prompt has been put to the author in this act.')
    put_txt('b625_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab'}


def kern_state(ks=None):
    out = {}
    for k in (ks or KERNS):
        p = 'D:/' + k
        tags = {}
        for l in g(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [g(p, 'rev-parse', '--short=7', 'main').strip(), tags,
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
                  g(p, 'status', '--porcelain', '--untracked-files=no').strip()]
    return out


def kernels(*a):
    put_json('b625_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ STEP ZERO: (R235)(5), THE SECTION VARIABLES
PROP_CLASSES = ('Fact', 'NeZero', 'Nonempty', 'BorelSpace', 'IsAddHaarMeasure', 'IsHermitian', 'IsPrimitive')
REL = re.compile(r'(?:=|≠|<|≤|>|≥|∈|∉|↔|∀|∃|⊆)')   # ### an arrow alone is no evidence: ℝ → ℝ and U → U → Prop are not Props


def _groups(text):
    """### the binder groups of a `variable` line: [(bracket, names, type)]."""
    out, i, n = [], 0, len(text)
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    while i < n:
        if text[i] in pairs:
            depth, j = 0, i
            while j < n:
                if text[j] in pairs:
                    depth += 1
                elif text[j] in pairs.values():
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            inner = text[i + 1:j]
            if ':' in inner and text[i] != '[':
                nm, ty = inner.split(':', 1)
                out.append((text[i], nm.split(), ty.strip()))
            elif text[i] == '[':
                if re.match(r'^\s*\w+\s*:', inner):
                    nm, ty = inner.split(':', 1)
                    out.append(('[', nm.split(), ty.strip()))
                else:
                    out.append(('[', [], inner.strip()))
            i = j + 1
        else:
            i += 1
    return out


_PROP_DEFS = {}


def _prop_head(repo, head):
    """### the kernel's own declaration of `head` as a Prop (structure, class, def or abbrev typed `: Prop`), by git grep at main."""
    key = (repo, head)
    if key not in _PROP_DEFS:
        out = g(repo, 'grep', '-n', '-E', r'^(structure|class|def|abbrev) %s( [^:.]*)?(\([^)]*\)[^:]*)*: Prop' % re.escape(head), 'main', '--', '*.lean')
        _PROP_DEFS[key] = out.strip().split(NL)[0] if out.strip() else ''
    return _PROP_DEFS[key]


def _prop_typed(repo, br, ty):
    """### (is it a Prop?, the basis printed)."""
    head = re.findall(r'[^\W\d][\w\'.₀-₉]*', ty)
    h0 = head[0] if head else ''
    last = h0.split('.')[-1]
    if br == '[' and (h0 in PROP_CLASSES or last in PROP_CLASSES):
        return True, 'an instance of the Prop class %s' % last
    if last in PROP_CLASSES:
        return True, 'the Prop predicate %s' % last
    if REL.search(ty):
        return True, 'a relation or quantifier in its type'
    d = _prop_head(repo, last) if last else ''
    if d:
        return True, 'declared a Prop at %s' % d.split(':', 3)[1] + ':' + d.split(':', 3)[2]
    return False, ''


def _scope_end(src_lines, start):
    """### the line (1-based) closing the namespace or section enclosing line `start`."""
    depth = 0
    for i in range(start, len(src_lines)):
        l = src_lines[i].strip()
        if re.match(r'^(namespace|section)\b', l) or (l.startswith('noncomputable section')):
            depth += 1
        elif re.match(r'^end\b', l):
            depth -= 1
            if depth < 0:
                return i + 1
    return len(src_lines)


def section_vars(*a):
    """### (R235)(5): git grep over the census's kernels and SIDE-explicit-formula at main for `variable` and `include` lines; every
    ### Prop-typed binder printed with its file and line, its basis, and the graded terminals in its scope (the table's graded rows
    ### and the pages' nodes declared after it and before its namespace or section closes), each marked whether its statement
    ### names the variable (an instance by the variable it constrains) or an `include` brings it in (data/b625_section_vars.txt)."""
    import act_root as AR
    ks = AR.census_kernels(PRE_PP)
    repos = ks + ['SIDE-explicit-formula']
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    graded = {}
    for r in T['rows']:
        if r['grade'] != 'UNGRADED':
            graded.setdefault((r['repo'], r['statement_file']), []).append(r)
    pages = set()
    for k in ('zeta', 'chi'):
        for l in rd(K.NODES[k]).split(NL):
            if l.strip() and not l.startswith('#'):
                pages.add(l.split()[0])
    L = ['b625 -- STEP ZERO, (R235)(5): THE PROP-TYPED SECTION VARIABLES AND `include` LINES, BY git grep AT main (%s)' % utc(), '',
         '### repositories grepped: %d -- the census v0.4`s kernel column (%d kernels, read at PLACE-papers %s) and SIDE-explicit-formula. '
         'The ruling names "the nine census kernels"; the column names %d (the navigator`s figure, printed).' % (len(repos), len(ks), PRE_PP, len(ks)),
         '### a variable is Prop-typed when its type is an instance of a Prop class (%s), carries a relation or quantifier, or names a '
         'declaration the repository types `: Prop`; it reaches a terminal declared in its scope when the terminal`s statement names it '
         '(an instance: names the variable it constrains) or an `include` line names it.' % ', '.join(PROP_CLASSES), '']
    hits, props, reach = 0, [], []
    for k in repos:
        p = 'D:/' + k
        if not os.path.isdir(p + '/.git'):
            L.append('### %s : NO CLONE' % k)
            continue
        out = g(p, 'grep', '-n', '-E', r'^\s*(variable|include)\b', 'main', '--', '*.lean')
        files = {}
        for l in out.split(NL):
            if l.strip():
                _m, f, n, txt = l.split(':', 3)
                files.setdefault(f, []).append((int(n), txt))
        for f, rows in sorted(files.items()):
            src = lines_of(g(p, 'show', 'main:' + f).replace(chr(13), ''))
            includes = [(n, txt) for n, txt in rows if txt.strip().startswith('include')]
            for n, txt in rows:
                hits += 1
                if txt.strip().startswith('include'):
                    L.append('  %s %s:%d  %s' % (k, f, n, txt.strip()[:160]))
                    continue
                for br, names, ty in _groups(txt.strip()[len('variable'):]):
                    ok, basis = _prop_typed(p, br, ty)
                    if not ok:
                        continue
                    end = _scope_end(src, n)
                    args = names or re.findall(r'(?<![\w.])([^\W\d][\w\'₀-₉]*)$', ty.strip()) or re.findall(r'\s([^\W\d][\w\'₀-₉]*)', ' ' + ty)
                    inc = [x for x in includes if n < x[0] <= end and set(x[1].split()[1:]) & set(names)]
                    terms = []
                    for r in graded.get((k, f), []):
                        short = r['name'].split('.')[-1]
                        dl = [i + 1 for i, l in enumerate(src) if re.match(r'^\s*(?:private\s+)?(?:theorem|lemma) %s(?![\w\'])' % re.escape(short), l)]
                        if not dl or not (n < dl[0] <= end):
                            continue
                        st = r.get('statement') or ''
                        names_in = [v for v in (names or args) if re.search(r'(?<![\w.\'])%s(?![\w\'₀-₉])' % re.escape(v), st)]
                        terms.append((r['name'], r['grade'], dl[0], bool(names_in or inc), r['name'] in pages))
                    props.append((k, f, n))
                    rch = [t for t in terms if t[3]]
                    if rch:
                        reach.append((k, f, n, br, names, ty, rch))
                    L.append('  %s %s:%d  %s%s : %s%s -- PROP-TYPED (%s); scope to :%d; graded terminals in scope %d, reached %d%s' % (
                        k, f, n, br, ' '.join(names) or '(anonymous)', ty[:90], {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}[br], basis, end,
                        len(terms), len(rch), (' -- ' + '; '.join('%s %s :%d%s' % (t[0].split('.')[-1], t[1], t[2], ' (page node)' if t[4] else '')
                                                               for t in rch)[:600]) if rch else ''))
    L += ['', '### ### **`variable`/`include` LINES %d ; PROP-TYPED BINDERS %d ; THOSE REACHING A GRADED TERMINAL %d.**' % (hits, len(props), len(reach))]
    put_txt('b625_section_vars.txt', L)
    put_json('b625_section_vars.json', dict(at=utc(), repos=repos, lines=hits, prop_typed=[list(x) for x in props],
                                            reaching=[dict(repo=x[0], file=x[1], line=x[2], bracket=x[3], names=x[4], type=x[5],
                                                           terminals=[list(t) for t in x[6]]) for x in reach]))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = '*Appended 2026-10-05 by b625 to b624’s entry (:%d), under `(R235)`(1) -- b624 AT ITS WEIGHT:*'
C_HEAD = '*Appended 2026-10-05 by b625 to W-ORD-E0-INDUCTION (:%d), the E0 rule’s line, under `(R235)`(2) -- THE DOMAIN-CONDITION CRITERION, A CLAUSE:*'
L_HEAD = '*Appended 2026-10-05 by b625 to W-ORD-ACT-ROOT (:%d), under `(R235)`(3) -- THE ROOT’S REPOSITORY LIST, A CLAUSE:*'
P_HEAD = '*Appended 2026-10-05 by b625 to W-ORD-ACT-ROOT (:%d), under `(R235)`(3) -- THE CENSUS’S KERNEL COLUMN, A PRICED ITEM:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    pre, post = _count_bank(_rel('b624_checks.txt')), _count_bank(_rel('b624_checks_postpush.txt'))
    DJ = json.loads(_rel('b624_defects.json'))
    return ('\n%s the E0 clause (relay f648d5a5): the rule reads the statement’s binders alone, a header with a proof inside it cut where '
            'its first arm begins -- procedural, power_contDiff’s header having run into the next theorem’s binders; non-membership a '
            'domain condition; a binder whose type equals the conclusion up to its bound variables reading ENCODES-CONCLUSION; the test '
            '13 of 13, the clause’s three cases failing against the rule as it stood; over 193 page nodes one grade moved, the step lemma '
            'of the family form, the table and every page grade cell unmoved, the χ page’s premises annotation on that row dropped '
            '(PLACE-papers 2eca533). The act root: relay tools/act_root.py and its test (8c9d9a52) 6 of 6; b624’s root '
            '1beaba22024ee00a17cd8bf5c9c670a0744c738d6f5c999601c0900feed85cb5 over 34 repositories, 27 cited tags at their remotes and '
            '32 banks, the chain’s opening line in relay data/act_roots.txt, the arm AGREE, the one-byte control changing it; relay and '
            'PLACE-papers pushed once mid-act so every named head was at its remote. H58b-H58d hold; H58a and N1 refuted in their letter on '
            'the step lemma by the non-membership reading, the navigator’s, as answered; N2-N5, S1-S5 held. FINDINGS :7510, :7512; '
            'OPEN_TRAILS :12919-:12927 (b623’s five readings beside their clauses), :12929 (the MANIFEST standing line), :12931 (the record '
            'with the root), :12953 (the correction). The suite %d of %d before the push and %d of %d after it, by the seat’s defects (c), '
            '(d) and (e), each claim tested directly and holding; defects (a)-(f) the seat’s (relay data/b624_defects.txt, %d entries), (f) '
            'a citation written from recall (OPEN_TRAILS :12188 for b591’s existential clause; the correction at :12953 to FINDINGS :6768 '
            'and OPEN_TRAILS :12174) -- the seat’s, and the same fault the navigator’s rule names for itself: cited lines are read, not '
            'remembered. The three prompts’ answers stand as banked. Nothing deposited; no kernel touched.\n'
            % (W_HEAD % entry, pre[0], pre[1], post[0], post[1], len(DJ['defects'])))


def _clause():
    return ('\n%s a binder of a statement is a domain condition, and does not enter the grade, when it is one of -- (i) an instance '
            'binder whose class is not Fact; (ii) a membership, non-membership, non-emptiness or finiteness condition on an object the '
            'statement names; (iii) a restriction on a variable the same statement quantifies universally (the test function’s support, '
            'parity, smoothness or integrability; a real’s positivity; a natural’s bound) -- the restriction being part of the '
            'quantifier’s domain and not a premise about the analytic object. A binder is a premise, and the grade INTERFACES on it, when '
            'it asserts a Prop about a fixed object the kernel names and does not derive (a structure of premises, an EF_lit_* '
            'hypothesis, a Fact instance, a Summable or HasSum of the kernel’s own series). The 33 nodes of relay data/b624_e0_nodes.txt '
            'are read under the clause with each binder printed and classed (i)-(iii) or premise, the grade following the class; a node '
            'whose binder fits no clause is printed for the author’s ruling at the closing and keeps the ledger’s grade until then. Where '
            'the rule’s reading after the clause agrees with the ledger, the node is closed in the bank; where it still differs, the '
            'ledger cell takes a dated correction entry in its own form naming the node, the old grade, the new and the clause -- no cell '
            'edited in place. Entered by b625 as the author’s ruling words it; the rule’s edit, its test and the classes banked in relay '
            '(data/b625_e0_classes.txt).\n' % (C_HEAD % K.E0_LINE))


def _rootlist():
    return ('\n%s the census’s kernel column does not name SIDE-explicit-formula, the kernel both pages pin, so b624’s root does not '
            'carry its head. The act root’s repository list from b625 is the union of the census’s kernel column, REGISTRY’s kernel rows '
            'and every kernel a page pins, with relay and PLACE-papers; the b624 line of relay data/act_roots.txt stands as written (the '
            'chain takes appends and no edits), the b625 line carrying “list widened: +<kernel> ...” in its own form, one name per kernel '
            'the list gains.\n' % (L_HEAD % K.ACT_ROOT_OT))


def _census_item():
    return ('\n%s the census’s kernel column takes SIDE-explicit-formula at the census’s next version (THE_KEYSTONE_CENSUS v0.5), the '
            'kernel both pages pin; the root reads it from b625 on by the clause above. **Price:** one cell in the rows whose pages and '
            'syntheses name the kernel, at the census’s next version. **Trigger:** the census’s next version, the author’s word. Priced, '
            'not started.\n' % (P_HEAD % K.ACT_ROOT_OT))


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def predict_cells(text, ledger):
    """### the grade cells the terminal table's tight reader (grade_cells, v3 attachment) takes from `text` appended to `ledger`,
    ### the FINDINGS-form directive's own line excepted for its terminal: [(line offset, name, grade)]."""
    import terminal_table as TT
    out = []
    for i, ln in enumerate(text.split(NL)):
        if not TT.GRADE_RE.search(ln):
            continue
        own = TT.FIND_SUP_RE.search(ln) if ledger == 'FINDINGS.md' else None
        for off, seg in TT._segments(ln):
            gs_ = [(m.start(), m.end(), m.group(1)) for m in TT.GRADE_RE.finditer(seg)]
            names = TT._names_on(seg)
            for g0, g1, gr in gs_:
                best, bd = None, None
                for a0, b0, nm in names:
                    d = abs((g0 - b0) if g0 >= b0 else (a0 - g1))
                    if d <= TT.WINDOW and (bd is None or d < bd):
                        best, bd = nm, d
                if best is not None and not (own and (best == own.group(2) or best.endswith('.' + own.group(2)))):
                    out.append((i, best, gr))
    return out


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b625_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _land(Q, items, bank, entry=None):
    """### append each (file, head, text) in order, each landing line checked against the line computed before it."""
    want = {}
    n = {'FINDINGS.md': len(lines_of(io.open(Q.FIND, encoding='utf-8').read().replace(chr(13), ''))),
         'OPEN_TRAILS.md': len(lines_of(io.open(Q.OT, encoding='utf-8').read().replace(chr(13), '')))}
    for f, h, t in items:
        want[h] = n[f] + 2
        n[f] += len(t.strip(NL).split(NL)) + 1
    for f, h, _t in items:
        Q.guard_absent(Q.FIND if f == 'FINDINGS.md' else Q.OT, h)
    out = []
    for f, h, t in items:
        path = Q.FIND if f == 'FINDINGS.md' else Q.OT
        r = Q.append_to(path, t)
        got = Q.line_of(path, h)
        out.append(dict(file=f, head=h, line=got, append=r))
        if got != want[h]:
            put_json(bank, dict(entry=entry, lines=out, at=utc(), stopped=True))
            sys.exit('### %s LANDED AT :%s, NOT :%d -- STOPPED' % (h[:60], got, want[h]))
    put_json(bank, dict(entry=entry, lines=out, at=utc()))
    print('  ' + ' ; '.join('%s :%s' % (x['file'], x['line']) for x in out))


def record_lines(*a):
    """### FINDINGS: b624's weight (to its entry :7512). OPEN_TRAILS: the domain-condition clause (to :12436), the root-list clause
    ### and the census item (to :12210). No line carries a grade word beside a backticked name (the table's reader predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The E0 gate at induction steps: ')
    if entry != K.B624_ENTRY:
        sys.exit('### b624`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', C_HEAD % K.E0_LINE, _clause()),
             ('OPEN_TRAILS.md', L_HEAD % K.ACT_ROOT_OT, _rootlist()), ('OPEN_TRAILS.md', P_HEAD % K.ACT_ROOT_OT, _census_item())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(allt, 'OPEN_TRAILS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    print('  table cells these lines would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b625_record_lines.json', entry)


# ================================================================================ COMPONENT 1: THE CORRECTION ENTRIES
X_HEAD = '*Appended 2026-10-05 by b625 to :%d, under `(R235)`(2) -- A CORRECTION ENTRY, THE DOMAIN-CONDITION CRITERION:*'


def _correction_text(f, n):
    """### one cell's correction entry: the dated head (no name, no grade word), then the directive line in the table's own form --
    ### the FINDINGS form (its own line adds no cell) or the trail-line form (its own line carries the new grade as its cell) --
    ### naming the node, the old grade, the new and the clause; the old grade word set beyond the reader's window from every name."""
    form = 'SUPERSEDES FINDINGS :%d for `finsetSum_insert`: DERIVES' % n if f == 'FINDINGS.md' else \
        'SUPERSEDES OPEN_TRAILS :%d for `finsetSum_insert`: DERIVES' % n
    tail = ('-- the node SIDEExplicitFormula.Schema.Family.finsetSum_insert (SIDE-explicit-formula v0.21 = 1d5d4dd, Schema/Family.lean '
            ':130), its one binder h : a ∉ s classed (ii) under the domain-condition criterion of the author’s ruling (R235)(2) -- a '
            'non-membership condition on the Finset s the statement names -- so the grade follows the class; the old grade, read at :%d '
            'on that binder as a hypothesis, was INTERFACES; the new, the shared E0 rule’s since relay f648d5a5, agrees; relay '
            'data/b625_e0_classes.txt; :%d stands unedited above.' % (n, n))
    return '\n%s\n%s %s\n' % (X_HEAD % n, form, tail)


def corrections(*a):
    """### (R235)(2): the four cells grading finsetSum_insert INTERFACES (FINDINGS :7058, OPEN_TRAILS :12424, :12434, :12438) each take a
    ### dated correction entry in its own form, appended to its own ledger; the table's cells predicted before anything lands."""
    Q = R2._Q()
    for f, n in K.INSERT_CELLS:
        t = lines_of(io.open(os.path.join(PP, f), encoding='utf-8').read().replace(chr(13), ''))
        if 'finsetSum_insert' not in t[n - 1] or 'INTERFACES' not in t[n - 1]:
            sys.exit('### %s :%d DOES NOT CARRY THE CELL -- NOTHING WRITTEN' % (f, n))
    items = [(f, X_HEAD % n, _correction_text(f, n)) for f, n in K.INSERT_CELLS]
    pred = [(f, n, predict_cells(t, f)) for (f, n), (_f, _h, t) in zip(K.INSERT_CELLS, items)]
    allt = ''.join(t for _f, _h, t in items)
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'corrections')
    print('  predicted cells per entry: %s ; no-disclosure hits: %s ; scanner %s' % ([(f, n, c) for f, n, c in pred], nd, 'CLEAN' if clean else 'NOT CLEAN'))
    want = [(f, n, [] if f == 'FINDINGS.md' else [(2, 'finsetSum_insert', 'DERIVES')]) for f, n in K.INSERT_CELLS]
    if DRY:
        for _f, _h, t in items:
            print(t)
        print('  predicted as designed: %s' % (pred == want))
        return
    if pred != want or any(nd.values()) or not clean:
        sys.exit('### AN ENTRY WOULD MAKE A CELL OTHER THAN DESIGNED, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b625_corrections.json')


# ================================================================================ COMPONENT 2: THE CLASSES, THE RULE AND ITS TEST
def e0_module(rev=None):
    """### tools/e0_rule.py at relay `rev` (None: the working file), loaded as a module of its own."""
    if rev is None:
        import e0_rule as E
        return E
    src = _show(RELAY, rev, 'tools/e0_rule.py')
    m = types.ModuleType('e0_rule_%s' % rev)
    exec(compile(src, 'e0_rule@%s' % rev, 'exec'), m.__dict__)
    return m


def e0_before(*a):
    """### the grade function and the patterns it reads, printed from tools/e0_rule.py at relay PRE_RELAY, before the edit."""
    src = _show(RELAY, PRE_RELAY, 'tools/e0_rule.py')
    sl = lines_of(src)
    keep = [i + 1 for i, l in enumerate(sl) if re.match(r'^(DOMAIN|BINDER|CLASS_PREDS) =|^def (grade|class_case|split_case)\(', l)]
    gi = [i + 1 for i, l in enumerate(sl) if l.startswith('def grade(')][0]
    nums = sorted(set(keep) | set(range(gi, gi + 18)))
    L = ['b625 -- COMPONENT 2: THE E0 RULE`S GRADE FUNCTION BEFORE THE EDIT, tools/e0_rule.py @ relay %s (%s; blob %s)' % (
        PRE_RELAY, utc(), g(RELAY, 'rev-parse', '%s:tools/e0_rule.py' % PRE_RELAY).strip()[:12]), '']
    L += ['    :%-4d %s' % (n, sl[n - 1]) for n in nums]
    put_txt('b625_e0_before.txt', L)


def _headers(rule):
    """### both pages re-emitted from their banked probes through the generator with `rule` as its E0 module: ({(page, node): (header,
    ### kind)}, {page: emitted text})."""
    import chain_page as CP
    seen, pages = {}, {}
    save = CP.E0
    CP.E0 = rule
    try:
        for k in ('zeta', 'chi'):
            rc, pg, meta, _log = CP.build(os.path.join(D, K.NODES[k]), tempfile.mkdtemp(), os.path.join(D, K.PROBE[k]))
            pages[k] = pg if rc == 0 else None
            for n, c in (meta or {}).get('cells', {}).items():
                if c.get('source_header') is not None:
                    seen[(k, n)] = (c['source_header'], c['kind'])
    finally:
        CP.E0 = save
    return seen, pages


def _table_grades():
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault(r['name'], r['grade'])
    return tg


def e0_classes(*a):
    """### (R235)(2): the 33 nodes of relay data/b624_e0_nodes.txt, each header read at its pin through the generator (the rule
    ### as it stood at PRE_RELAY), each binder printed with its type and classed by the seat (K.CLASS), the grade following the class
    ### beside the ledger's (the table's) and the rule's before the edit: AGREE (closed in the bank), CORRECTED (the ledger's cells
    ### take a correction entry) or FOR THE AUTHOR`S RULING (a binder no clause reaches, or no binder) -- data/b625_e0_classes.txt and
    ### .json."""
    old = e0_module(PRE_RELAY)
    seen, _p = _headers(old)
    heads = {}
    for (k, n), (h, kind) in seen.items():
        heads.setdefault(n, (h, kind, k))
    dis = json.loads(_rel('b624_e0_nodes.json'))['disagreements']
    tg = _table_grades()
    L = ['b625 -- COMPONENT 2, (R235)(2): THE 33 LEDGER-AGAINST-RULE NODES CLASSED UNDER THE DOMAIN-CONDITION CRITERION (%s)' % utc(), '',
         '### each node`s header read at its pin through the page generator from the banked probes (relay data/%s, data/%s); every '
         'hypothesis binder the rule reads printed with its type; each classed by the seat -- (i) an instance binder whose class is not '
         'Fact, (ii) a membership, non-membership, non-emptiness or finiteness condition on an object the statement names, (iii) a '
         'restriction on a variable the statement quantifies universally, premise, or NONE (no clause reaches it) -- with its reason; '
         'the grade following the class beside the ledger`s (the table`s grade, from its cells) and the rule`s before the edit (relay %s).'
         % (K.PROBE['zeta'], K.PROBE['chi'], PRE_RELAY), '']
    rows = []
    for x in dis:
        n = x['name']
        h, kind, k = heads[n]
        gb = old.grade(h, 'theorem')
        binders = []
        for b, t in gb[2]:
            c, why = K.CLASS.get(K.norm(t), ('NONE', 'no class entered by the seat'))
            binders.append(dict(binder=b, type=K.norm(t), cls=c, why=why))
        if n in K.NO_BINDER:
            cg, verdict, why_v = None, 'FOR THE AUTHOR`S RULING', K.NO_BINDER[n]
        elif any(b['cls'] == 'NONE' for b in binders):
            cg, verdict, why_v = None, 'FOR THE AUTHOR`S RULING', 'a binder no clause reaches; the ledger`s grade kept until the ruling'
        else:
            cg = 'INTERFACES' if any(b['cls'] == 'premise' for b in binders) else 'DERIVES'
            agree = cg.split('-')[0] == tg[n].split('-')[0]
            verdict, why_v = ('AGREE', 'closed in the bank') if agree else ('CORRECTED', 'the ledger`s cells take a dated correction entry')
        rows.append(dict(name=n, page=k, ledger=tg[n], rule_before=gb[0], class_grade=cg, verdict=verdict, why=why_v, binders=binders))
        L.append('### %s (%s page) -- ledger %s ; rule before %s ; the class`s grade %s ; ### %s (%s)' % (
            n, k, tg[n], gb[0], cg or '--', verdict, why_v))
        for b in binders:
            L.append('    %-8s : %-52s %-8s %s' % (b['binder'], b['type'][:52], b['cls'], b['why']))
        if not binders:
            L.append('    (no hypothesis binder read)')
    na = sum(r['verdict'] == 'AGREE' for r in rows)
    nc = sum(r['verdict'] == 'CORRECTED' for r in rows)
    nu = sum(r['verdict'] == 'FOR THE AUTHOR`S RULING' for r in rows)
    L += ['', '### THE CORRECTED: ' + ('; '.join('%s -- ledger %s, the class %s' % (r['name'].split('.')[-1], r['ledger'], r['class_grade'])
                                                 for r in rows if r['verdict'] == 'CORRECTED') or 'none'),
          '### FOR THE AUTHOR`S RULING AT THE CLOSING: ' + ('; '.join('%s -- %s' % (r['name'].split('.')[-1], r['why'][:160])
                                                                      for r in rows if r['verdict'] == 'FOR THE AUTHOR`S RULING') or 'none'),
          '', '### ### **NODES %d ; AGREEING %d ; CORRECTED %d ; FOR THE AUTHOR`S RULING %d ; BINDERS CLASSED %d (i) %d (ii) %d (iii) %d premise %d NONE %d.**' % (
              len(rows), na, nc, nu, sum(len(r['binders']) for r in rows),
              *(sum(b['cls'] == c for r in rows for b in r['binders']) for c in ('(i)', '(ii)', '(iii)', 'premise', 'NONE')))]
    put_txt('b625_e0_classes.txt', L)
    put_json('b625_e0_classes.json', dict(at=utc(), rows=rows, agree=na, corrected=nc, unclassed=nu))
    print(L[-1])


def e0_diff(*a):
    d = g(RELAY, 'diff', PRE_RELAY, '--', *K.E0_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *K.E0_FILES)
    L = ['b625 -- COMPONENT 2: THE E0 RULE`S CRITERION AND ITS TEST, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.rstrip(NL).split(NL)[-1].strip() if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b625_e0_diff.txt', L)
    print(L[2])


CONTROL_FMT = '### THE POSITIVE CONTROL: the same test with tools/e0_rule.py as it stood at relay %s (exit %d): cases %d, passing %d, failing %s'
CONTROL_RE = r'^### THE POSITIVE CONTROL: the same test with tools/e0_rule\.py as it stood at relay (\w+) \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$'


def e0_test(*a):
    """### tools/test_e0_rule.py run with the planted directory, counted by its case pattern; run again with the rule as it stood at
    ### PRE_RELAY (its blob loaded in place of the working file) as the positive control: data/b625_e0_test.txt and .json."""
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONPATH=os.path.join(ROOT, 'tools'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_e0_rule.py'), PLANTED], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, COUNT_CASE)
    old = tempfile.mkdtemp()
    open(os.path.join(old, 'e0_rule.py'), 'wb').write(_show(RELAY, PRE_RELAY, 'tools/e0_rule.py').encode('utf-8'))
    shutil.copy(os.path.join(ROOT, 'tools', 'test_e0_rule.py'), os.path.join(old, 'test_e0_rule.py'))
    r2 = subprocess.run([sys.executable, os.path.join(old, 'test_e0_rule.py'), PLANTED], capture_output=True, text=True, encoding='utf-8',
                        errors='replace', env=env)
    out2 = (r2.stdout or '') + (r2.stderr or '')
    n2, p2 = count_cases(out2, COUNT_CASE)
    failed2 = [re.match(r'^  (\(\d+\))', l).group(1) for l in out2.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
    planted = [l.strip() for l in out.split(NL) if l.strip().startswith('planted: ')]
    L = ['b625 -- COMPONENT 2: tools/test_e0_rule.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          CONTROL_FMT % (PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b625_e0_test.txt', L)
    put_json('b625_e0_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, planted=planted,
                                       control=dict(rc=r2.returncode, cases=n2, passing=p2, failing=failed2)))
    print(L[-3])
    print(L[-1])


def e0_nodes(*a):
    """### every header both pages grade, graded by the rule before (relay PRE_RELAY) and after (the working file): the grades and
    ### premise lists that move; the 33 re-read; every page node whose table grade differs from the rule's read after the edit
    ### (data/b625_e0_nodes.txt and .json)."""
    old, new = e0_module(PRE_RELAY), e0_module(None)
    seen, _p = _headers(new)
    heads = {}
    for (k, n), (h, kind) in seen.items():
        heads.setdefault(n, (h, kind, k))
    rows = []
    for n, (h, kind, k) in sorted(heads.items()):
        kk = 'theorem' if kind == 'theorem' else 'def'
        a_, b_ = old.grade(h, kk), new.grade(h, kk)
        rows.append(dict(name=n, page=k, kind=kind, before=a_[0], after=b_[0], why_before=a_[1], why_after=b_[1]))
    tg = _table_grades()
    the33 = set(x['name'] for x in json.loads(_rel('b624_e0_nodes.json'))['disagreements'])
    dis = [dict(name=r['name'], page=r['page'], table=tg[r['name']], rule=r['after']) for r in rows
           if r['kind'] == 'theorem' and tg.get(r['name']) not in (None, 'UNGRADED') and tg[r['name']].split('-')[0] != r['after'].split('-')[0]]
    moved = [r for r in rows if r['before'] != r['after']]
    premv = [r for r in rows if r['before'] == r['after'] and r['why_before'] != r['why_after']]
    L = ['b625 -- COMPONENT 2: EVERY NODE THE PAGES GRADE, GRADED BY THE E0 RULE BEFORE (relay %s) AND AFTER THE CRITERION (%s)' % (PRE_RELAY, utc()), '',
         '### distinct nodes graded %d ; grades moved %d (outside the 33: %d) ; premise lists moved with the grade unmoved %d' % (
             len(rows), len(moved), sum(r['name'] not in the33 for r in moved), len(premv)), '']
    L += ['### GRADES MOVED:'] + ['  %-62s %s -> %s%s' % (r['name'], r['before'], r['after'], '' if r['name'] in the33 else ' ### OUTSIDE THE 33') for r in moved]
    L += ['', '### PREMISE LISTS MOVED, THE GRADE UNMOVED:'] + ['  %-62s %s: %s -> %s' % (r['name'], r['after'], r['why_before'][:90], r['why_after'][:90])
                                                          for r in premv]
    L += ['', '### PAGE NODES WHOSE TABLE GRADE (FROM LEDGER CELLS) DIFFERS FROM THE RULE`S READ AFTER THE CRITERION:']
    L += ['  %-62s %-5s table %s ; rule %s' % (x['name'], x['page'], x['table'], x['rule']) for x in dis] or ['  NONE']
    L += ['', '### ### **NODES %d ; GRADES MOVED %d, ALL AMONG THE 33 %s ; DISAGREEMENTS NOW %d.**' % (
        len(rows), len(moved), all(r['name'] in the33 for r in moved), len(dis))]
    put_txt('b625_e0_nodes.txt', L)
    put_json('b625_e0_nodes.json', dict(at=utc(), rows=rows, moved=[r['name'] for r in moved], premise_moved=[r['name'] for r in premv],
                                        disagreements=dis))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE CLOSURE
def closure(*a):
    """### (R235)(4): the upstream commit carrying thmB₀_mult read at its remote (one ls-remote: the tag v1.0's peel) and pinned;
    ### FinalMult.lean's import closure at the pin listed by file with line counts, each module marked VENDORED (byte-identical in
    ### SIDE-explicit-formula's Zeta23/ at main) or NEW, the Mathlib and Batteries imports separated; both repositories' toolchains
    ### and Mathlib pins compared; the twenty-module and hold conditions read; free memory read (data/b625_closure.txt and .json).
    ### Nothing is copied."""
    lsr = g(K.UP, 'ls-remote', 'origin')
    refs = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in lsr.split(NL) if '\t' in l)
    peel = refs.get('refs/tags/%s^{}' % K.UP_TAG) or refs.get('refs/tags/%s' % K.UP_TAG)
    src = _show(K.UP, K.UP_PIN, K.UP_FILE) or ''
    at = lines_of(src)[K.UP_LINE - 1] if src else ''
    seen, stack, ext = {}, ['Zeta23.FinalMult'], {}
    while stack:
        m = stack.pop()
        if m in seen:
            continue
        t = _show(K.UP, K.UP_PIN, m.replace('.', '/') + '.lean')
        if t is None:
            seen[m] = None
            continue
        seen[m] = t
        for i in re.findall(r'^import\s+(\S+)', t, re.M):
            if i.startswith(('Mathlib', 'Batteries', 'Lean', 'Std', 'Init')):
                ext.setdefault(i, []).append(m)
            else:
                stack.append(i)
    loc = sorted(k for k, v in seen.items() if v is not None)
    missing = sorted(k for k, v in seen.items() if v is None)
    rows = []
    for m in loc:
        p = m.replace('.', '/') + '.lean'
        kb = _show(K.KER, 'main', p)
        state = 'NEW' if kb is None else ('VENDORED' if kb.replace(chr(13), '').endswith(seen[m].replace(chr(13), '')) or seen[m] in kb else 'VENDORED, BODY DIFFERS')
        rows.append(dict(module=m, file=p, lines=len(lines_of(seen[m])), state=state))
    new = [r for r in rows if r['state'] == 'NEW']
    tc_up, tc_k = (_show(K.UP, K.UP_PIN, 'lean-toolchain') or '').strip(), (_show(K.KER, 'main', 'lean-toolchain') or '').strip()
    def mathlib_rev(repo, rev):
        try:
            man = json.loads(_show(repo, rev, 'lake-manifest.json') or '{}')
        except ValueError:
            return None
        return ([p.get('rev') for p in man.get('packages', []) if p.get('name') == 'mathlib'] or [None])[0]
    mu, mk = mathlib_rev(K.UP, K.UP_PIN), mathlib_rev(K.KER, 'main')
    fm = R2.free_mb()
    import chain_page as CP
    over = len(loc) > K.MAX_MODULES
    L = ['b625 -- COMPONENT 3, (R235)(4): THE CLOSURE OF Zeta23/FinalMult.lean, LISTED BEFORE ANY COPY (%s)' % utc(), '',
         '### the upstream: anthropics/formal-math (the clone relay data/anthropic-zeta23/formal-math, untracked); one ls-remote: tag %s '
         'peels at the remote to %s ; the pin %s ; equal %s' % (K.UP_TAG, peel, K.UP_PIN, peel == K.UP_PIN),
         '### %s :%d at the pin: %s' % (K.UP_FILE, K.UP_LINE, at.strip()),
         '### the vendored set: SIDE-explicit-formula %s (%s), Zeta23/ at main' % (K.VENDOR_COMMIT, g(K.KER, 'log', '-1', '--format=%s', K.VENDOR_COMMIT).strip()[:120]),
         '', '### THE CLOSURE, BY FILE (module ; lines ; state against the vendored set):']
    L += ['  %-52s %6d  %s' % (r['module'], r['lines'], r['state']) for r in rows]
    if missing:
        L += ['', '### imports not found at the pin (outside the project): %s' % missing]
    L += ['', '### THE EXTERNAL IMPORTS (Mathlib, Batteries), SEPARATED: %d distinct' % len(ext)]
    L += ['  %s' % i for i in sorted(ext)]
    L += ['', '### THE TOOLCHAINS: upstream %s (Mathlib %s, its manifest) ; SIDE-explicit-formula %s (Mathlib %s, its manifest) ; toolchains '
              'equal %s ; Mathlib equal %s' % (tc_up, mu, tc_k, mk, tc_up == tc_k, mu == mk),
          '### THE CONDITIONS OF (R235)(4): modules in the closure %d (the limit %d) -- %s ; of them vendored already %d, NEW %d (%d lines) ; '
          'the hold: free memory now %d MB (the hold %d MB), no module built' % (
              len(loc), K.MAX_MODULES, 'EXCEEDS' if over else 'within', len(rows) - len(new), len(new), sum(r['lines'] for r in new), fm, CP.HOLD_MB),
          '', '### ### **CLOSURE %d MODULES (%d LINES) ; NEW %d ; THE TWENTY-MODULE CONDITION %s ; %s.**' % (
              len(loc), sum(r['lines'] for r in rows), len(new), 'FAILS' if over else 'HOLDS',
              'THE ACT HOLDS AT COMPONENT 3, NO COPY MADE' if over else 'THE VENDOR MAY PROCEED')]
    put_txt('b625_closure.txt', L)
    put_json('b625_closure.json', dict(at=utc(), peel=peel, pin=K.UP_PIN, line=at.strip(), modules=rows, external=sorted(ext), missing=missing,
                                       toolchain=dict(upstream=tc_up, kernel=tc_k, mathlib_upstream=mu, mathlib_kernel=mk),
                                       free_mb=fm, hold_mb=CP.HOLD_MB, over=over, new=len(new), lsr=1))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RE-PRICED ITEM, BY THE AUTHOR'S ANSWER
RP_HEAD = '*Appended 2026-10-05 by b625 to W-ORD-VENDOR-FINALMULT (:12290), under the author’s answer at b625’s hold -- RE-PRICED, TWO ROUTES, NEITHER STARTED:*'


def _repriced_text():
    CL = jl('b625_closure.json')
    tc = CL['toolchain']
    return ('\n%s the listing (relay data/b625_closure.txt) shows a port, not a vendor: %d modules of the closure outside the vendored set, '
            '%d lines, %d distinct Mathlib and Batteries imports, across a toolchain step (upstream %s with Mathlib %s; the kernel %s with '
            'Mathlib %s), so every module is a build against a different Mathlib and the %d byte-identical modules already vendored are no '
            'guide to the rest. **Route (a), the port:** the closure split by directory, under twenty new modules per act, the toolchain '
            'question settled in the opening act, at the listing’s figures. **Price:** not fewer than five acts. **Route (b), the '
            'cross-kernel discharge:** Zeta23 at v1.0 = 3635e748 prints #print axioms on thmB₀_mult in its own build, the print banked with '
            'the peeled SHA, and SimpleProportion’s two_thirds field carries a head-line citation to that pin and print, the grade staying '
            'INTERFACES with the field’s discharge recorded at its source kernel. **Price:** one act, no port, no claim moved. **Trigger:** '
            'the author’s word between them; neither starts at b625.\n' % (
                RP_HEAD, CL['new'], sum(r['lines'] for r in CL['modules'] if r['state'] == 'NEW'), len(CL['external']), tc['upstream'],
                (tc['mathlib_upstream'] or '')[:8], tc['kernel'], (tc['mathlib_kernel'] or '')[:8], len(CL['modules']) - CL['new']))


def repriced(*a):
    """### the author's answer at the hold: W-ORD-VENDOR-FINALMULT re-priced on OPEN_TRAILS with two routes, appended at the end and
    ### addressed to :12290 (data/b625_repriced.json); no table cell (predicted)."""
    Q = R2._Q()
    t = _repriced_text()
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'repriced')
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, [('OPEN_TRAILS.md', RP_HEAD, t)], 'b625_repriced.json')


# ================================================================================ COMPONENT 5: THE TABLE, THE PAGES, THE ROOT
def table(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    L = ['b625 -- COMPONENT 5: THE TERMINAL TABLE REGENERATED AFTER THE CORRECTION ENTRIES AND THE CRITERION (%s); exit %d' % (utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d %s' % (len(diff.get('added') or []), len(diff.get('gone') or []),
                                                                         len(diff.get('changed') or []), diff.get('changed') or ''),
         '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'),
         '', '### ### **THE GRADE COLUMN`S DIFF : %s.**' % ('EMPTY' if not (diff.get('changed') or diff.get('added') or diff.get('gone'))
                                                          else '; '.join(str(x)[:200] for x in (diff.get('changed') or [])) or 'ROWS ADDED OR GONE')]
    put_txt('b625_table.txt', L)
    put_json('b625_table.json', dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                     changed=diff.get('changed') or [], files_moved=moved))
    print(L[-1])


def _grade_cells(text):
    """### a page's grade column: {name: grade} from its node lines' and its correspondence rows' grade cells."""
    out = {}
    for l in (text or '').split(NL):
        m = re.match(r'^\| `([^`]+)` \| [^|]+ \| ([A-Z][A-Z-]*) \|', l)
        if m:
            out['corr:' + m.group(1)] = m.group(2)
        m2 = re.match(r'^\d+\. `([^`]+)` — .* — E0: ([A-Z][A-Z-]*) — tier: (.*?) — axioms: ', l)
        if m2:
            out['node:' + m2.group(1)] = m2.group(2)
            out['tier:' + m2.group(1)] = m2.group(3)
    return out


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; its grade cells compared to the prior emission (the
    ### page at HEAD); written only when it changed (data/b625_page_<k>.json)."""
    import chain_page as CP
    if k not in K.NODES:
        sys.exit('usage: page zeta|chi')
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b625_%s' % k), os.path.join(D, K.PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b625_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b625_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s' % (k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE'))
    for x in dl:
        print('    ' + x[:240])


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b625 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b625_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b625_page_arms.txt', L)
    for l in L:
        print(l[:240])


ROOT_EXCLUDE = re.compile(r'^b625_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    """### the data/ banks the act wrote and names in its root: every relay data/b625_* bank on disk now, but those a later step
    ### rewrites."""
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b625_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root_test(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_act_root.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out, COUNT_CASE)
    L = ['b625 -- COMPONENT 5: tools/test_act_root.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt('b625_root_test.txt', L)
    put_json('b625_root_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p))
    print(L[-1])


def root(*a):
    """### tools/act_root.py compute b625 over the act's banks, written: data/act_roots.txt (+1 line), data/b625_act_root.json and .txt."""
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b625'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the act-root arm run by the record tool after the root: verify over data/act_roots.txt (one ls-remote per repository), and
    ### the one-byte control on a copy of one named bank (data/b625_root_arm.txt and .json)."""
    import act_root as AR
    res = AR.verify()
    J = jl('b625_act_root.json')
    bank = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank))
    shutil.copy(os.path.join(ROOT, *bank.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank, AR.sha256_file(cp)) if it.split()[0] == bank else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    L = ['b625 -- COMPONENT 5: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s (%s) with its first byte changed; the root recomputed over the copy %s ; over the bank %s '
              '(the banked root %s) ; the copy`s root differs %s' % (bank, cp.replace('\\', '/'), r2, same, J['root'], r2 != J['root']),
          '### ls-remote calls by the arm, per repository: %d repositories, at most %d each' % (len(AR.LSR), max(AR.LSR.values()) if AR.LSR else 0),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b625_root_arm.txt', L)
    put_json('b625_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, copy=cp, root_copy=r2, root_recomputed=same,
                                        root=J['root'], lsr=dict(AR.LSR)))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H59a', 'H59b', 'H59c', 'H59d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
E0_SUBJECT = 'b625 (R235)(2)'
ROOT_SUBJECT = 'b625 (R235)(3)'
CONTROL_FAILING = ['(9)', '(13)', '(14)', '(15)']


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _alone(repo, files, commits):
    return [h for h, s in commits if _files(h, repo) == sorted(files)]


def _epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _lock():
    m = re.search(r'locked at \(UTC\) : (\S+)', rd(FACE) or '')
    return _epoch(m.group(1)) if m else None


def _after_lock(repo, h):
    lk = _lock()
    return lk is not None and int(g(repo, 'show', '-s', '--format=%ct', h).strip() or 0) > lk


def emlt():
    """### exceptional_mass_le_third read at SIDE-explicit-formula main by the rule as it now stands: (grade, why, named fields of each
    ### premise structure, the fields at v0.17)."""
    import e0_rule as E
    def at(rev):
        src = _show(K.KER, rev, 'SIDEExplicitFormula/Simplicity.lean') or ''
        m = re.search(r'^theorem exceptional_mass_le_third(.*?):=', src, re.M | re.S)
        s = re.search(r'^structure SimpleProportion : Prop where\n((?:  .*\n)+)', src, re.M)
        return (' '.join(m.group(1).split()) if m else None), (re.findall(r'^  (\w+) :', s.group(1), re.M) if s else [])
    h, f = at('main')
    h0, f0 = at(K.V017[1])
    gr = E.grade(h or '', 'theorem')
    return gr[0], gr[1], f, f0, h == h0


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no sorry on any main (the explicit-formula kernel's, by git grep); the vendored
    ### files on the tagged branch alone (none made); no file written beyond the vendored closure and its AxiomCheck module, the rule
    ### edit and its tests, the two banks, the namespace repair, the suite repairs, the correction entries, the re-emitted pages, the
    ### table, the roots line, the record lines and the trails. The trail record's expected line a parameter (OPEN_TRAILS :12799); a
    ### pending record is OT's write."""
    if isinstance(trail_line, str):
        trail_line = int(trail_line.split('=')[-1])
    ot_text = ot if ot is not None else io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD:
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d (the trails end at :%d)' % (trail_line, len(ot_lines))
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b625_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = now == {k: list(v) for k, v in face.items()}
    sorry = g(K.KER, 'grep', '-n', '-w', '-E', r'sorry', 'main', '--', '*.lean')
    sorry_lines = [l for l in sorry.split(NL) if l.strip() and not re.search(r'--.*\bsorry\b|/-|sorryAx|`sorry`|no sorry|sorry-free', l)]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if jx('b625_page_%s.json' % k).get('changed')]
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b625_', 'audit_b625_', 'terminal_table'))
                              and x != 'data/b624_closing_push_out.txt'))
    allowed = set(K.E0_FILES) | {'data/act_roots.txt', 'tools/b624_worklist.py'}
    beyond = [x for x in relay_beyond if x not in allowed]
    ok = kern_ok and pp_ch == want_pp and not beyond and rec_ok and not sorry_lines
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel read unmoved (main, tags by peel, branches, status) %s -- no vendored file on any branch; '
            'sorry lines on the explicit-formula main %d; PLACE-papers %s (wanted %s); %s; relay beyond the list: %s (the list: the rule '
            'and its test, the banks, the namespace repair, the roots line, the table, the act`s own tools)' % (
                kern_ok, len(sorry_lines), pp_ch, want_pp, rec_state, beyond or 'NONE'))


def scores(*a):
    CL, CX, EN, ET = jx('b625_closure.json'), jx('b625_e0_classes.json'), jx('b625_e0_nodes.json'), jx('b625_e0_test.json')
    TB, PZ, PX, RA, RT, AJ = (jx('b625_table.json'), jx('b625_page_zeta.json'), jx('b625_page_chi.json'), jx('b625_root_arm.json'),
                              jx('b625_root_test.json'), jx('b625_act_root.json'))
    SV, CO = jx('b625_section_vars.json'), jx('b625_corrections.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    held = bool(CL.get('over'))
    hold_why = ('the act held at Component 3 by (R235)(4): the closure %d modules (%d not vendored), over the twenty-module limit; '
                'no module copied or built' % (len(CL.get('modules') or []), CL.get('new', 0)))
    eg, ewhy, ef, ef0, esame = emlt()
    moved_cells = [x for x in (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or []) if 'exceptional_mass_le_third' not in x]
    rc = _relay_commits()
    e0c = _alone(RELAY, list(K.E0_FILES), rc)
    arc = _alone(RELAY, list(K.ROOT_FILES), rc)
    the33 = set(x['name'] for x in json.loads(_rel('b624_e0_nodes.json'))['disagreements'])
    lw = [l for l in rd('act_roots.txt').split(NL) if l.startswith('b625 ')]
    added = sorted(set((AJ.get('reads') or {}).get('heads') or {}) - set((jx('b624_act_root.json').get('reads') or {}).get('heads') or {}))
    tchg = TB.get('changed') or []
    tnames = sorted(set(str(x[1]) if isinstance(x, list) and len(x) > 1 else str(x) for x in tchg))
    ver = RA.get('verify') or []
    S = {
        'H59a': ('NOT SCORABLE', hold_why) if held else ('REFUTED', 'the vendor not landed'),
        'H59b': ('NOT SCORABLE', hold_why) if held else ('REFUTED', 'the vendor not landed'),
        'H59c': ('NOT SCORABLE', hold_why + '; exceptional_mass_le_third reads %s at main on %s, its premise`s named fields %s as at v0.17 %s' % (
            eg, ewhy, ef, ef0)) if held else ('REFUTED', 'the vendor not landed'),
        'H59d': (('HOLDS' if not moved_cells else 'REFUTED'), 'page grade cells moved: %s (the χ page`s step lemma by the ruled correction '
                                                              'entries, no vendor)' % (moved_cells or 'NONE')),
        'N1': (('HELD' if not held else 'REFUTED'), 'the closure %d modules against the limit 20; no module built' % len(CL.get('modules') or [])),
        'N2': (('HELD' if eg == 'DERIVES' or len(ef) < len(ef0) else 'REFUTED'),
               'exceptional_mass_le_third at main reads %s on %s; SimpleProportion`s named fields %s, at v0.17 %s -- %s' % (
                   eg, ewhy, ef, ef0, 'the act held at Component 3' if held else 'after the vendor')),
        'N3': (('HELD' if CX.get('agree', 0) >= 25 and CX.get('unclassed', 99) <= 4 else 'REFUTED'),
               'agreeing %s, corrected %s, for the author`s ruling %s' % (CX.get('agree'), CX.get('corrected'), CX.get('unclassed'))),
        'N4': (('HELD' if SV and not SV.get('reaching') else 'REFUTED'), 'Prop-typed section variables %d, reaching a graded terminal %d: %s' % (
            len(SV.get('prop_typed') or []), len(SV.get('reaching') or []),
            '; '.join('%s %s:%d %s' % (x['repo'], x['file'], x['line'], ' '.join(x['names']) or x['type'][:40]) for x in SV.get('reaching') or [])[:900])),
        'N5': n5v,
        'S1': (('HELD' if len(e0c) == 1 and _after_lock(RELAY, e0c[0]) and ET.get('cases') and ET.get('cases') == ET.get('passing')
                and sorted((ET.get('control') or {}).get('failing') or []) == sorted(CONTROL_FAILING) else 'REFUTED'),
               'the rule and its test in one relay commit of their own %s after the lock; the test %s of %s; the rule as it stood fails %s' % (
                   e0c, ET.get('passing'), ET.get('cases'), (ET.get('control') or {}).get('failing'))),
        'S2': (('HELD' if len(EN.get('moved') or []) == 29 and set(EN.get('moved') or []) <= the33 and CX.get('agree') == 29 else 'REFUTED'),
               'grades moved %d, all among the 33 %s; agreeing after the clause %s' % (len(EN.get('moved') or []), set(EN.get('moved') or []) <= the33,
                                                                                      CX.get('agree'))),
        'S3': (('HELD' if held and os.path.exists(_r('b625_closure.txt')) and kern_state(['SIDE-explicit-formula']) ==
                {k: list(v) for k, v in jl('b625_kernels_face.json')['kernels'].items() if k == 'SIDE-explicit-formula'} else 'REFUTED'),
               'the closure over the limit %s; the listing banked; the explicit-formula kernel as at the face (no branch, no file)' % held),
        'S4': (('HELD' if len(arc) == 1 and _after_lock(RELAY, arc[0]) and RT.get('cases') and RT.get('cases') == RT.get('passing')
                and len(((AJ.get('reads') or {}).get('heads') or {})) == 38 and ver and all(v[1] == 'AGREE' for v in ver)
                and lw and ('list widened: ' + ' '.join('+' + x for x in added)) in lw[0] else 'REFUTED'),
               'act_root.py and its test in one relay commit of their own %s; the test %s of %s; repositories %d; the arm %s; the b625 line %s' % (
                   arc, RT.get('passing'), RT.get('cases'), len(((AJ.get('reads') or {}).get('heads') or {})), [(v[0], v[1]) for v in ver],
                   (lw[0][150:] if lw else 'ABSENT'))),
        'S5': (('HELD' if len(CO.get('lines') or []) == 4 and tnames == [K.INSERT] else 'REFUTED'),
               'the correction entries %s; the table rows changed %s' % ([(x['file'], x['line']) for x in CO.get('lines') or []], tnames or 'NONE')),
    }
    put_json('b625_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b625 — lane three, act fifty-two under (R235): the 2/3 theorem’s closure listed and held; the 33 ledger-against-rule '
              'nodes classed under the domain-condition criterion; the root’s list widened')


def _answer():
    t = rd('b625_author_answers.txt')
    m = re.findall(r'^RESULT \(transcript line \d+\): (.*)$', t, re.M)
    return m[-1] if m else 'no answer banked'


def _title_entry():
    CL, CX, AJ = jx('b625_closure.json'), jx('b625_e0_classes.json'), jx('b625_act_root.json')
    eg, _w, ef, _f0, _s = emlt()
    return ('## The 2/3 theorem held at its closure: %d modules of Zeta23 at 3635e748, %d not vendored, over the twenty-module limit; '
            'exceptional_mass_le_third at %s on %d named field; the 33 ledger-against-rule nodes classed, %d agreeing, %d corrected, %d for '
            'ruling; the root over %d repositories' % (len(CL.get('modules') or []), CL.get('new', 0), eg, len(ef), CX.get('agree', 0),
                                                       CX.get('corrected', 0), CX.get('unclassed', 0), len(((AJ.get('reads') or {}).get('heads') or {}))))


def _finding_text():
    S, rl, CX, EN, ET, CL = (jl(n) for n in ('b625_scores.json', 'b625_record_lines.json', 'b625_e0_classes.json', 'b625_e0_nodes.json',
                                             'b625_e0_test.json', 'b625_closure.json'))
    CO, TB, J, RA, SV = jl('b625_corrections.json'), jl('b625_table.json'), jl('b625_act_root.json'), jl('b625_root_arm.json'), jl('b625_section_vars.json')
    PZ, PX = jx('b625_page_zeta.json'), jx('b625_page_chi.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    arc = (_alone(RELAY, list(K.ROOT_FILES), rc) or ['?'])[0]
    pc = _pp_commits()
    pgz = ' '.join(h for h, s in pc if _files(h) == [K.PAGE]) or 'none'
    pgx = ' '.join(h for h, s in pc if _files(h) == [K.DIR_PAGE]) or 'none'
    t = _title_entry()
    unc = [r for r in CX['rows'] if r['verdict'] == 'FOR THE AUTHOR`S RULING']
    added = sorted(set(J['reads']['heads']) - set(jl('b624_act_root.json')['reads']['heads']))
    e = ['', t, '',
         '*Filed at b625 on the author’s ruling `(R235)` and the author’s answer at the hold. Banks: relay `data/b625_section_vars.txt`, '
         '`data/b625_e0_classes.txt`, `data/b625_e0_diff.txt`, `data/b625_e0_test.txt`, `data/b625_e0_nodes.txt`, `data/b625_closure.txt`, '
         '`data/b625_table.txt`, `data/b625_act_root.txt`, `data/b625_root_arm.txt`, `data/act_roots.txt`, `data/b625_author_answers.txt`. '
         'Nothing deposits.*', '',
         '**The closure** (`(R235)`(4), W-ORD-VENDOR-FINALMULT, OPEN_TRAILS :12290): the upstream tag v1.0 read at its remote, peeling to '
         '3635e748, the 2/3 theorem at Zeta23/FinalMult.lean :350 there. Its import closure at the pin: %d modules, %d lines; %d of them '
         'already in the explicit-formula kernel’s vendored set (52d8cf9) and %d not; %d external imports, Mathlib and Batteries, '
         'listed apart; the toolchains %s and %s. The closure exceeds the twenty-module limit, so the act held at Component 3 with the '
         'listing banked before any copy, the free memory read (%d MB), no module built, nothing copied, no branch made. The author’s '
         'answer at the hold: %s. H59a-H59c %s, %s, %s.' % (
             len(CL['modules']), sum(r['lines'] for r in CL['modules']), len(CL['modules']) - CL['new'], CL['new'], len(CL['external']),
             CL['toolchain']['upstream'], CL['toolchain']['kernel'], CL['free_mb'], _answer()[:400], S['H59a'][0], S['H59b'][0], S['H59c'][0])
         + (' The work-order re-priced by that answer with two routes, the port and the cross-kernel discharge, neither started '
            '(OPEN_TRAILS :%d).' % jx('b625_repriced.json')['lines'][0]['line'] if jx('b625_repriced.json') else ''), '',
         '**The 33 nodes** (`(R235)`(2)): each binder printed and classed -- %d agreeing with the ledger after the criterion and closed in '
         'the bank; %d corrected, the step lemma of the family form, its four cells each taking a dated correction entry in the table’s '
         'own supersession form (FINDINGS :%d; OPEN_TRAILS :%d, :%d, :%d); %d printed for the author’s ruling, keeping the ledger’s grade: '
         '%s. The shared E0 rule edited after the seal where the criterion needed a pattern it lacked -- a Fact instance read as a '
         'premise, non-emptiness and finiteness as domain conditions, continuity, integrability and the support inclusion on a variable '
         'the statement quantifies, five named restrictions read at their pins, a bounded quantifier’s range read through to its body -- '
         'with its test, one case per clause, alone (relay %s): the test %d of %d by its case pattern, the rule as it stood failing %s. '
         'Over the page nodes %d grades moved, every one among the 33.' % (
             CX['agree'], CX['corrected'], CO['lines'][0]['line'], CO['lines'][1]['line'], CO['lines'][2]['line'], CO['lines'][3]['line'],
             CX['unclassed'], '; '.join('%s -- %s' % (r['name'].split('.')[-1], r['why'][:150]) for r in unc), e0c, ET['passing'], ET['cases'],
             ET['control']['failing'], len(EN['moved'])), '',
         '**The table and the pages.** The table regenerated: %s. The ζ page re-emitted from its banked probe (PLACE-papers %s), the χ page '
         '(PLACE-papers %s); page grade cells moved %s. H59d %s.' % (
             '; '.join(str(x)[:160] for x in TB['changed']) or 'no row moved', pgz, pgx,
             (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or []) or 'none', S['H59d'][0]), '',
         '**The section variables** (`(R235)`(5)): %d variable or include lines over %d repositories, %d Prop-typed binders, %d reaching '
         'a graded terminal (relay data/b625_section_vars.txt), banked for the closing.' % (
             SV['lines'], len(SV['repos']), len(SV['prop_typed']), len(SV['reaching'])), '',
         '**The act root** (`(R235)`(3)): relay `tools/act_root.py` reads its repositories as the union of the census’s kernel column, '
         'REGISTRY’s kernel rows and every kernel a page pins (relay %s, with its test); the root of b625 over %d repositories, %d tags and '
         '%d banks, its line carrying “list widened: %s”; the chain verified, %s.' % (
             arc, len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks']), ' '.join('+' + x for x in added),
             ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The record lines** (`(R235)`(1)-(3)): b624’s weight at FINDINGS :%d; the criterion at OPEN_TRAILS :%d; the root-list clause '
         ':%d; the census item :%d.' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b596’s face at the proportion (W-ORD-SIMPLICITY-FACE, the '
         'premise named because the 2/3 theorem’s module lay outside the vendored set) and finds the gap priced at OPEN_TRAILS :12290 '
         'wider than one module; it re-reads b624’s entry (:7512) node by node, giving its 33 printed disagreements a ruled criterion and '
         'closing all but four; and it gives b624’s root (OPEN_TRAILS :12931) its successor over the kernel both pages pin. It strengthens '
         'the programme’s offering of a grade a reader can recompute from a statement alone, and of a record whose every act can be '
         'checked against the remotes by one hash.', '',
         '**Next.** Per `(R235)`(6): b626, W-ORD-PLATT-RUNG (OPEN_TRAILS :12891). The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; nothing here is a statement about RH, GRH or any zero.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  table cells the entry would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b625_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) “the nine census kernels” read as the census v0.4’s kernel column, which names 32, grepped whole with SIDE-explicit-'
              'formula; (2) “a restriction on a variable the same statement quantifies universally” read as one the statement binds and its '
              'conclusion mentions, b570’s reading of the class clause kept, so its named negative case stands; (3) a named predicate on '
              'the statement’s own variables classed by its definition read at its pin -- admissible, HStrip, HCount, is_universal, '
              'IsNontrivialZeroChi -- and entered in the rule as named restrictions with file and line, as SPLITS enters its splits; (4) a '
              'bounded quantifier’s range read as no condition on a named object, so register3_of_one_lt_re’s binder is a premise on Phi; '
              '(5) the correction entries in the table’s supersession forms, the trail-line form carrying the new grade as its cell; (6) '
              '“REGISTRY’s kernel rows” read as the rows whose first or second cell is a kernel’s name alone, adding SIDE-carrier-spec, '
              'SIDE-fano-darkness and SIDE-li-map beside SIDE-explicit-formula; “every kernel a page pins” the kernel each page’s pin '
              'sentence names; (7) the twenty-module limit read on the whole closure, the not-vendored part printed beside it')


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b625_scores.json', 'b625_findings.json', 'b625_record_lines.json', 'b625_act_root.json'))
    CX, CO, CL = jl('b625_e0_classes.json'), jl('b625_corrections.json'), jl('b625_closure.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    arc = (_alone(RELAY, list(K.ROOT_FILES), rc) or ['?'])[0]
    unc = [r for r in CX['rows'] if r['verdict'] == 'FOR THE AUTHOR`S RULING']
    rows_ = ['', TRAIL_HEAD, '',
             '**(R235) ratified.** (1) b624 at its weight. (2) The domain-condition criterion, a clause. (3) The root’s repository list. '
             '(4) W-ORD-VENDOR-FINALMULT, held at its closure. (5) The section-variable check. (6) The act after: b626.', '',
             '**Entered:** FINDINGS.md:%d (b624’s weight), :%d (the entry, with its mutual-light line), :%d (a correction entry); '
             'OPEN_TRAILS.md:%d (the criterion, to :12436), :%d (the root-list clause, to :12210), :%d (the census item, priced), :%d, :%d, '
             ':%d (correction entries); this record; relay tools/e0_rule.py and tools/test_e0_rule.py %s; relay tools/act_root.py and '
             'tools/test_act_root.py %s; relay data/act_roots.txt; relay data/b625_e0_classes.txt, data/b625_closure.txt, '
             'data/b625_section_vars.txt.' % (rl['lines'][0]['line'], fj['entry_line'], CO['lines'][0]['line'], rl['lines'][1]['line'],
                                              rl['lines'][2]['line'], rl['lines'][3]['line'], CO['lines'][1]['line'], CO['lines'][2]['line'],
                                              CO['lines'][3]['line'], e0c, arc), '',
             '**Act root:** b625 `%s` (previous `%s`, b624’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**The hold, and the author’s answer** (relay data/b625_author_answers.txt): the closure %d modules, %d not vendored; %s.%s' % (
                 len(CL['modules']), CL['new'], _answer()[:500],
                 (' The work-order re-priced with two routes, neither started: OPEN_TRAILS :%d.' % jx('b625_repriced.json')['lines'][0]['line'])
                 if jx('b625_repriced.json') else ''), '',
             '**For the author’s ruling:** %s.' % ('; '.join('%s -- %s' % (r['name'], r['why']) for r in unc) or 'none'), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b625_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R235)`(6), b626, W-ORD-PLATT-RUNG (OPEN_TRAILS :12891); the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  table cells the record would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:9000])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b625_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b625_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b625 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b625_defects.json -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b625_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b625_scores.json')
    L = ['=' * 104, 'b625 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H59a-H59d, (R235)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H59 : HOLDS %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** '
          '### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
              sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'NOT SCORABLE' for k in HKEYS),
              sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK),
              sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b625_defects.txt').rstrip(NL).split(NL)
    put_txt('b625_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b625_scores.json', 'b625_findings.json', 'b625_trail.json', 'b625_record_lines.json', 'b625_act_root.json'))
    CX, CO, CL = jl('b625_e0_classes.json'), jl('b625_corrections.json'), jl('b625_closure.json')
    L = ['b625 -- THE COMPONENTS, BANKED UNDER (R235).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b624`s closing push-out relay %s ; push-b624* branches deleted by '
         'name (data/b625_branches.txt) ; the namespace repair relay %s ; the section variables data/b625_section_vars.txt ; the suite run at '
         'HEAD before the face (data/b625_arms_prerun.txt)' % (STEPZERO, K.NSREPAIR),
         '### COMPONENT 1 : b624`s weight FINDINGS :%d ; the criterion OPEN_TRAILS :%d ; the root-list clause :%d ; the census item :%d ; '
         'the correction entries %s' % (rl['lines'][0]['line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                        ', '.join('%s :%d' % (x['file'], x['line']) for x in CO['lines'])),
         '### COMPONENT 2 : data/b625_e0_classes.txt (agreeing %d, corrected %d, for ruling %d) ; data/b625_e0_diff.txt ; data/b625_e0_test.txt ; '
         'data/b625_e0_nodes.txt' % (CX['agree'], CX['corrected'], CX['unclassed']),
         '### COMPONENT 3 : data/b625_closure.txt (%d modules, %d not vendored) ; the hold ; H59a %s, H59b %s' % (
             len(CL['modules']), CL['new'], S['H59a'][0], S['H59b'][0]),
         '### COMPONENT 4 : not run -- the act held at Component 3 ; H59c %s' % S['H59c'][0],
         '### COMPONENT 5 : the table data/b625_table.txt ; the pages data/b625_page_zeta.json, data/b625_page_chi.json ; page arms '
         'data/b625_page_arms.txt ; the root %s (data/act_roots.txt, data/b625_act_root.txt) ; the arm data/b625_root_arm.txt ; H59d %s' % (
             J['root'][:16], S['H59d'][0]),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b626 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b625_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b625_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
