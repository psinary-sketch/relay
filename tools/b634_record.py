# -*- coding: utf-8 -*-
"""b634_record.py -- THE ACT'S RECORD TOOL, UNDER (R244). ### ONE SUBCOMMAND PER BANK.

### ### b634: LANE THREE, ACT SIXTY-ONE -- THE E0 RULE READ FROM ELABORATED TYPES FOR SIDE-explicit-formula AT v0.25, BESIDE THE
### TEXTUAL READING, EVERY DISAGREEMENT CLASSED, THE UNNAMED ROWS READ; THE ACT-ROOT CENSUS PATH AT v0.5; THE CLOSING'S HEAD LINE.
### Subcommands write only `data/b634_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. The generic helpers are b633's record tool's, imported and not copied (its banks are
### named by the caller); ledger appends through b566's guarded `append_to`. The data is tools/b634_worklist.py; the elaborated
### reader is tools/b634_elab.py (Component 3). No platform is called and no registry is read. b628's full intake bank is never
### read here, never staged or committed.
"""
import collections
import difflib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b634_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = R3.SP
SESSION, SESSION_ID = R3.SESSION, R3.SESSION_ID
FACE = 'b634_registration_2026-10-06.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_txt, put_json, jl, jx, rd, _write, _scan, _clean = R3.put_txt, R3.put_json, R3.jl, R3.jx, R3.rd, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
KERNS, KERN_PIN, kern_state = R3.KERNS, R3.KERN_PIN, R3.kern_state

DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b634_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b634 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b634_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b634_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the two work-orders, the build route, the closing form, the reads the ferry names, b633`s lines and record',
         PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12228, 12354, 12356, 12799, K.GATE_WO, K.BINDER_GRAMMAR, K.CLOSING_FORM, K.BUILD_ROUTE]
         + list(range(13219, 13250, 2)), 1500),
        ('FINDINGS: b633`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B633_ENTRY], 600),
        ('relay tools/e0_rule.py: the criterion`s functions, the named lists, MET', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'^(RESTRICTIONS = |MET = |BINDER = |INSTANCE = |def (restriction_case|domain_case|quantified|grade|unlisted_case|data_binder|seam_antecedents|statement_only)\b)'), 200),
        ('relay tools/test_e0_rule.py: its cases', RELAY, PRE_RELAY, 'tools/test_e0_rule.py', ('GREP', r"want\('\(\d+\)"), 160),
        ('relay tools/act_root.py: the census path and its readers', RELAY, PRE_RELAY, 'tools/act_root.py',
         ('GREP', r'^(CENSUS = |def (census_kernels|registry_kernels|page_kernels|repositories)\b)'), 200),
        ('relay tools/test_act_root.py: its cases', RELAY, PRE_RELAY, 'tools/test_act_root.py', ('GREP', r'\(\d+\)'), 160),
        ('relay tools/b633_closing.py: the closing`s head and main', RELAY, PRE_RELAY, 'tools/b633_closing.py',
         ('GREP', r"^(def main|    L = \[|         'b633 -- THE CLOSING RECORD)"), 200),
        ('SIDE-explicit-formula at v0.25: the lakefile', K.KER, K.KER_PIN, 'lakefile.toml', list(range(1, 20)), 200),
        ('SIDE-explicit-formula at v0.25: the aggregator module', K.KER, K.KER_PIN, 'SIDEExplicitFormula.lean', [1], 200),
        ('PLACE-papers: the census at v0.5, its §1 head and its back-matter premise table`s head', PP, PRE_PP, K.CEN5,
         ('GREP', r'^(## §1 |### The named premises|\| row \|)'), 260),
        ('relay data/b633_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b633_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b634 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    T = json.loads(_show(RELAY, PRE_RELAY, 'data/terminal_table.json'))['rows']
    E = [r for r in T if r['repo'] == K.KERNEL]
    L += ['', '### THE TERMINAL TABLE AT relay %s: %d rows ; %s rows %d ; their grades %s ; provenance %s ; statements %s' % (
        PRE_RELAY, len(T), K.KERNEL, len(E), dict(collections.Counter(r['grade'] for r in E)), dict(collections.Counter(r.get('provenance') for r in E)),
        dict(collections.Counter(r['statement_state'] for r in E))),
        '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
        '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b634_reads.txt', L)


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R244) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b634 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
        L.append('### NONE: no prompt has been put to the author in this act.')
    put_txt('b634_author_answers.txt', L)


def kernels(*a):
    put_json('b634_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ STEP ZERO: THE UNNAMED ROWS ((R244)(2))
def _premises(r):
    from b632_record import rule_full, premise_name
    k, gr, why, prem, head = rule_full(r.get('statement'), r['name'])
    return gr, prem, head, [(b, t, premise_name(t, head)) for b, t in prem]


def unnamed_rows(rows=None):
    """### every INTERFACES row of the table, by provenance and by what the rule's reading names: RETURN (decomposition, the rows
    ### with no head for the premise table to name). A row is in the set when a premise binder the rule reads has no named head, or
    ### when the rule reads no premise at all on a row the table grades INTERFACES (a ledger cell)."""
    rows = rows if rows is not None else _table()
    dec, out = collections.Counter(), []
    for r in rows:
        if r['grade'] != 'INTERFACES':
            continue
        gr, prem, head, named = _premises(r)
        nm = [x[2][0] for x in named]
        if not prem:
            kind = 'no premise the rule reads'
        elif all(nm):
            kind = 'every premise named'
        elif any(nm):
            kind = 'named and unnamed'
        else:
            kind = 'no premise named'
        dec[(r.get('provenance'), kind)] += 1
        if kind != 'every premise named':
            out.append(dict(repo=r['repo'], name=r['name'], provenance=r.get('provenance'), table_grade=r['grade'], rule_grade=gr, kind=kind,
                            binders=[dict(binder=b, type=t, head=x[0], why=x[1]) for b, t, x in named], statement=r.get('statement'),
                            in_scope=r['repo'] == K.KERNEL))
    return dec, out


def unnamed(*a):
    """### (R244)(2), step zero: data/b634_unnamed_rows.txt and its json."""
    T = _table()
    dec, out = unnamed_rows(T)
    I = [r for r in T if r['grade'] == 'INTERFACES']
    rule_rows = sum(v for (p, k), v in dec.items() if p == 'rule')
    L = ['b634 -- STEP ZERO, (R244)(2): THE INTERFACES ROWS WITH NO HEAD FOR THE PREMISE TABLE TO NAME, FROM THE TABLE AT relay %s (%s)' % (
        g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), utc()), '',
         '### the table`s INTERFACES rows: %d (%s)' % (len(I), dict(collections.Counter(r.get('provenance') for r in I))),
         '### by provenance and by what the rule`s reading names:']
    L += ['    %-5s %-28s %d' % (p, k, v) for (p, k), v in sorted(dec.items())]
    L += ['', '### THE RULING`S FIGURE. (R244)(1)-(2) read 22 rows on unnamed heads as 85 - 63: 85 the table`s INTERFACES rows (62 graded by the rule,',
          '### 23 by ledger cells), 63 the 42 heads` rows counted once per named premise over the rule rows alone. By rows, the set the',
          '### ruling`s words define -- INTERFACES on a bare relation or an unnamed predicate, no head for the premise table to name -- is %d:' % len(out),
          '### the rows whose rule reading carries a premise with no named head, and the ledger-graded rows on which the rule reads no premise.',
          '### %d of them are in %s, the act`s scope; the rest are in kernels (R244)(4) leaves to later acts.' % (
              sum(1 for x in out if x['in_scope']), K.KERNEL), '']
    for i, x in enumerate(out, 1):
        L.append('  U%02d %s %-5s %-24s %s :: table %s, rule %s :: %s' % (i, 'IN-SCOPE ' if x['in_scope'] else 'LATER    ', x['provenance'],
                                                                    x['repo'], x['name'], x['table_grade'], x['rule_grade'], x['kind']))
        for b in x['binders']:
            L.append('        %s : %s  -> %s' % (b['binder'], b['type'], b['head'] or ('unnamed: ' + (b['why'] or ''))))
        L.append('        statement: %s' % ' '.join((x['statement'] or '### none').split())[:400])
    L += ['', '### ### **ROWS IN THE SET : %d ; IN SCOPE (%s) : %d ; RULE ROWS AMONG THE INTERFACES : %d.**' % (
        len(out), K.KERNEL, sum(1 for x in out if x['in_scope']), rule_rows)]
    put_txt('b634_unnamed_rows.txt', L)
    put_json('b634_unnamed_rows.json', dict(at=utc(), interfaces=len(I), decomposition={'%s / %s' % k: v for k, v in dec.items()}, rows=out))


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = '*Appended 2026-10-06 by b634 to b633’s entry (:%d), under `(R244)`(1) -- b633 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
HL_HEAD = '*Appended 2026-10-06 by b634 to the closing form, a clause at the record’s form (:%d), under `(R244)`(3) -- THE CLOSING’S HEAD LINE:*'


def _weight():
    U = jl('b634_unnamed_rows.json')
    n_in = sum(1 for x in U['rows'] if x['in_scope'])
    return ('\n%s the keystone census at v0.5 beside v0.4 unedited (PLACE-papers 2c7c6ce): the kernel column across the act root’s 38 '
            'repositories, one ls-remote each; the explicit-formula kernel’s four faces at v0.22-v0.25; a provenance cell on every row; '
            'the Phase 2 rows read against the structural-error-correction kernel at v0.2.2, none naming one of its statements, each '
            'printing why, the bookend’s trigger absent; the intake pilot’s figures by digest; the 42 named premises in back matter with '
            'the 51 MET names; scanner clean, re-pin 34 of 34; both pages one Placement row each, no grade or tier cell moved. The rule '
            '(relay 119b6cbb): Alt2 and Alternates entered as named restrictions, PREDICATE-UNLISTED against the 51; its test 23 of 23, '
            'the four new cases failing on the old rule; six rows moved to derived (98667fac). The b630 test frozen to its pin, 7 of 7 '
            '(f1c9e40f). The 42 heads’ rows sum to 63 against 85 INTERFACES rows; the ruling reads 22 rows on unnamed heads as their '
            'difference -- by rows, the set its words define is %d (relay data/b634_unnamed_rows.txt): rows whose rule reading carries a '
            'premise with no named head, and ledger-graded rows on which the rule reads no premise, %d of them in the explicit-formula '
            'kernel; 63 counts a row once per named premise over the 62 rule rows. Relay 9b6f8d01; PLACE-papers c9e36c2; the root '
            '86573431…f796, b624 to b633 agreeing. The suite 90 of 91 by G-PROVENANCE-CELLS reading the second copy of four rows, the '
            'cells checked directly (relay data/b633_provenance_direct.txt). Nothing deposited; no kernel touched.\n' % (
                W_HEAD % K.B633_ENTRY, len(U['rows']), n_in))


def _headline():
    return ('\n%s the closing opens with one line -- “<act> closed: relay <sha>, PLACE-papers <sha>[, <kernel> <tag> = <sha>]; suite <p> '
            'of <n>; root <prefix>…; <k> prompts answered; <d> defects” -- so that line relayed alone carries the act when nothing needs '
            'ruling, the rest of the closing attached as its bank. The act’s closing tool writes it from the banks (relay '
            'tools/b634_closing.py and its test), and each act carries the tool forward.\n' % (HL_HEAD % K.CLOSING_FORM))


def record_lines(*a):
    """### FINDINGS: b633's weight (to :7725). OPEN_TRAILS: the head-line clause (to the closing form :13028) -- appended at the end."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The keystone census at v0.5')
    if entry != K.B633_ENTRY:
        sys.exit('### b633`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B633_ENTRY, _weight()), ('OPEN_TRAILS.md', HL_HEAD % K.CLOSING_FORM, _headline())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(allt, 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backtick parity odd in: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                                  ticks or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean or ticks:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b634_record_lines.json', K.B633_ENTRY)


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b634 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def headline_test(*a):
    """### (R244)(3): tools/test_closing_headline_b634.py run and counted (data/b634_headline_test.txt)."""
    _run_test('tools/test_closing_headline_b634.py', 'b634_headline_test')


def actroot_test(*a):
    """### (R244)(4): tools/test_act_root.py run and counted after the census path's edit (data/b634_actroot_test.txt)."""
    _run_test('tools/test_act_root.py', 'b634_actroot_test')


def rootlist(tag, *a):
    """### the act root's repository list at PLACE-papers HEAD, read by tools/act_root.py as it stands on disk, printed with its census
    ### path (data/b634_rootlist_<tag>.txt): before and after the census path's edit."""
    code = ('import sys, json; sys.path.insert(0, %r); import act_root as A; '
            'print(json.dumps(dict(census=A.CENSUS, census_kernels=A.census_kernels("HEAD"), registry=A.registry_kernels("HEAD"), '
            'pages=A.page_kernels("HEAD"), repositories=A.repositories("HEAD"))))' % os.path.join(ROOT, 'tools'))
    r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    J = json.loads(r.stdout)
    L = ['b634 -- THE ACT ROOT`S REPOSITORY LIST, %s THE CENSUS PATH`S EDIT (%s); PLACE-papers HEAD %s' % (
        tag.upper(), utc(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip()), '',
         '### census path : %s' % J['census'], '### census kernels (%d) : %s' % (len(J['census_kernels']), ' '.join(J['census_kernels'])),
         '### registry kernels (%d) ; page kernels (%d)' % (len(J['registry']), len(J['pages'])),
         '### ### **REPOSITORIES : %d** -- %s' % (len(J['repositories']), ' '.join(J['repositories']))]
    if tag == 'after' and os.path.exists(os.path.join(D, 'b634_rootlist_before.json')):
        B = jl('b634_rootlist_before.json')
        L += ['', '### against before: census kernels gained %s, lost %s ; repositories gained %s, lost %s' % (
            sorted(set(J['census_kernels']) - set(B['census_kernels'])) or 'NONE', sorted(set(B['census_kernels']) - set(J['census_kernels'])) or 'NONE',
            sorted(set(J['repositories']) - set(B['repositories'])) or 'NONE', sorted(set(B['repositories']) - set(J['repositories'])) or 'NONE')]
    put_txt('b634_rootlist_%s.txt' % tag, L)
    put_json('b634_rootlist_%s.json' % tag, J)
    print(L[-1])


# ================================================================================ COMPONENT 2: THE KERNEL'S STATE
def modules():
    fs = [f for f in g(K.KER, 'ls-tree', '-r', '--name-only', K.KER_PIN).split(NL)
          if f.endswith('.lean') and (f.startswith('SIDEExplicitFormula/') or f.startswith('Zeta23/') or f == 'SIDEExplicitFormula.lean')]
    return sorted(f[:-5] for f in fs)


def kernel_state(*a):
    """### Component 2: the checkout at the pin and clean; each module's olean present or absent; lake's own up-to-date reading by
    ### `lake build --no-build`, which compiles nothing (data/b634_kernel_state.txt and its json)."""
    head = g(K.KER, 'rev-parse', 'HEAD').strip()
    st = g(K.KER, 'status', '--porcelain', '--untracked-files=no').strip()
    ms = modules()
    pres = {m: os.path.exists(os.path.join(K.KER, '.lake', 'build', 'lib', 'lean', *(m + '.olean').split('/'))) for m in ms}
    t0 = time.time()
    try:
        r = subprocess.run(['lake', 'build', '--no-build'], cwd=K.KER, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=540)
        nb_rc, nb_out = r.returncode, (r.stdout or '') + (r.stderr or '')
    except subprocess.TimeoutExpired:
        nb_rc, nb_out = 'TIMEOUT', ''
    secs = int(time.time() - t0)
    absent = [m for m in ms if not pres[m]]
    L = ['b634 -- COMPONENT 2: THE KERNEL`S STATE, %s AT %s = %s (%s)' % (K.KERNEL, K.KER_TAG, K.KER_PIN, utc()), '',
         '### checkout HEAD %s ; at the pin %s ; tracked changes %s' % (head[:12], head == K.KER_PIN_FULL, st or 'NONE'),
         '### modules at the pin: %d ; oleans present %d ; absent %d %s' % (len(ms), len(ms) - len(absent), len(absent), absent or ''),
         '### `lake build --no-build` (compiles nothing): exit %s in %d s ; its last lines:' % (nb_rc, secs)]
    L += ['    ' + l for l in nb_out.rstrip(NL).split(NL)[-12:]]
    L += ['', '### PER MODULE:'] + ['    %-8s %s' % ('present' if pres[m] else 'ABSENT', m) for m in ms]
    put_txt('b634_kernel_state.txt', L)
    put_json('b634_kernel_state.json', dict(at=utc(), head=head, clean=not st, modules=ms, absent=absent, nobuild_rc=nb_rc, nobuild_secs=secs,
                                            nobuild_tail=nb_out.rstrip(NL).split(NL)[-12:]))
    print(L[2]); print(L[3]); print(L[4])


# ================================================================================ COMPONENT 4: THE TWO READINGS
def _module_vars(module):
    """### the binder names the module's `variable` commands introduce, read from its source at the pin."""
    t = _show(K.KER, K.KER_PIN, module + '.lean') or ''
    out = set()
    for m in re.finditer(r'^variable\b(.*?)(?=^\S)', t + NL + 'x', re.M | re.S):
        out |= set(re.findall(r'[({\[⦃]\s*([^:(){}\[\]⦃⦄]+?)\s*:', m.group(1)))
    names = set()
    for grp in out:
        names |= set(grp.split())
    return names


def _elab_header(e):
    """### the elaborated declaration rendered in the textual rule's syntax: (x : T) {x : T} ⦃x : T⦄ [T] then ' : ' and the rest."""
    parts = []
    for b in e['binders']:
        if b['kind'] == 'explicit':
            parts.append('(%s : %s)' % (b['name'], b['type']))
        elif b['kind'] == 'implicit':
            parts.append('{%s : %s}' % (b['name'], b['type']))
        elif b['kind'] == 'strict-implicit':
            parts.append('⦃%s : %s⦄' % (b['name'], b['type']))
        else:
            parts.append('[%s]' % b['type'])
    return (' '.join(parts) + ' : ' + e['concl']).strip()


def elab_grade(e):
    import e0_rule as E
    kind = 'theorem' if e['kind'] == 'theorem' else 'def'
    gr, why, _b = E.grade(_elab_header(e), kind)
    return gr, why


def _text_binders(head):
    import e0_rule as E
    h2 = E.statement_only(head or '')
    return [mm.groups() for mm in E.BINDER.finditer(h2)], h2 != (head or '')


def classify(row, e, tgrade, egrade):
    """### the class of a disagreement, with the reason printed: section variable, auto-bound implicit, header cut, notation or
    ### coercion, other ((R244)(4), in its order; the first that holds)."""
    from b632_record import rule_full
    _k, _g, _w, _p, head = rule_full(row.get('statement'), row['name'])
    tb, cut = _text_binders(head)
    tnames = set(b for b, _t in tb)
    ehyp = [b for b in e['binders'] if b['kind'] == 'explicit' and re.match(r'h\w*$', b['name'])]
    extra = [b['name'] for b in ehyp if b['name'] not in tnames]
    mod = (row.get('statement_file') or '').split(':')[0][:-5]
    sv = _module_vars(mod) if mod else set()
    if extra and any(x in sv for x in extra):
        return 'section variable', 'the elaborated type carries %s, which the module`s variable command binds and the textual header does not' % (
            [x for x in extra if x in sv])
    tbound = set(re.findall(r"[^\W\d][\w'₀-₉]*", ' '.join(re.findall(r'[({⦃]\s*([^:(){}⦃⦄]+?)\s*:', (head or '').split(' : ')[0]))))
    auto = [b['name'] for b in e['binders'] if b['kind'] == 'implicit' and b['name'] not in tbound and not b['name'].endswith('✝')
            and re.search(r'(?<![\w.])%s(?![\w])' % re.escape(b['name']), head or '')]
    if auto:
        return 'auto-bound implicit', 'implicit binders %s are bound in the elaborated type and free in the textual header' % auto
    if cut or e.get('opened') or len(ehyp) != len(tb):
        return 'header cut', 'the textual header %s; the elaborated header carries %d hypothesis binders against the text`s %d%s' % (
            'is cut where a proof begins' if cut else 'is read whole', len(ehyp), len(tb),
            '; the elaborated telescope opened named ∀-binders of the conclusion' if e.get('opened') else '')
    if [b for b, _t in tb] == [b['name'] for b in ehyp]:
        return 'notation or coercion', 'the same hypothesis binders, their types printed differently: %s' % '; '.join(
            '%s : %s || %s' % (b, ' '.join(t.split())[:80], x['type'][:80]) for (b, t), x in zip(tb, ehyp) if ' '.join(t.split()) != x['type'])[:600]
    return 'other', 'binders text %s against elaborated %s; textual %s, elaborated %s' % ([b for b, _t in tb], [b['name'] for b in ehyp], tgrade, egrade)


def readings(*a):
    """### Component 4: every row of the kernel with its table grade, its textual rule grade and its elaborated rule grade; the
    ### disagreements classed (data/b634_two_readings.txt, data/b634_gate_disagreements.txt and their json); the in-scope unnamed rows
    ### read from their elaborated binders (data/b634_unnamed_read.txt). Nothing moves on the table or a page."""
    from b632_record import rule_full, premise_name
    import b634_elab as EL
    T = [r for r in _table() if r['repo'] == K.KERNEL]
    ET = EL.load_bank()
    rows, dis = [], []
    for r in T:
        e = ET.get(r['name'])
        _k, tg, _why, _p, _h = rule_full(r.get('statement'), r['name']) if r.get('statement') else (None, None, '', [], '')
        tg = tg or 'UNREAD'
        if e is None or e.get('missing'):
            eg = 'NO TYPE'
        else:
            eg, _ew = elab_grade(e)
        agree = tg == eg
        rows.append(dict(name=r['name'], provenance=r.get('provenance'), table=r['grade'], textual=tg, elaborated=eg, agree=agree))
        if not agree and tg != 'UNREAD' and eg != 'NO TYPE':
            cl, why = classify(r, e, tg, eg)
            dis.append(dict(name=r['name'], provenance=r.get('provenance'), table=r['grade'], textual=tg, elaborated=eg, cls=cl, why=why,
                            header=_elab_header(e), statement=' '.join((r.get('statement') or '').split())[:600]))
    both = [x for x in rows if x['textual'] != 'UNREAD' and x['elaborated'] != 'NO TYPE']
    ag = sum(1 for x in both if x['agree'])
    L = ['b634 -- COMPONENT 4: THE TWO READINGS OF %s AT %s, EVERY ROW (%s)' % (K.KERNEL, K.KER_TAG, utc()), '',
         '### rows %d ; read by both %d ; agreeing %d = %.4f ; textual unread (no statement) %d ; elaborated no type %d' % (
             len(rows), len(both), ag, (ag / len(both)) if both else 0, sum(1 for x in rows if x['textual'] == 'UNREAD'),
             sum(1 for x in rows if x['elaborated'] == 'NO TYPE')), '']
    L += ['  %-5s %-70s table %-14s textual %-14s elaborated %-14s %s' % (x['provenance'], x['name'][:70], x['table'], x['textual'], x['elaborated'],
                                                                        'AGREE' if x['agree'] else 'DIFFER') for x in rows]
    put_txt('b634_two_readings.txt', L)
    put_json('b634_two_readings.json', dict(at=utc(), rows=rows, both=len(both), agree=ag))
    cc = collections.Counter(x['cls'] for x in dis)
    D_ = ['b634 -- COMPONENT 4: THE DISAGREEMENTS, CLASSED (%s); for the author`s ruling at the closing, by class' % utc(), '',
          '### ### **DISAGREEMENTS : %d ; BY CLASS : %s.**' % (len(dis), dict((c, cc.get(c, 0)) for c in K.CLASSES)), '']
    for c in K.CLASSES:
        D_ += ['### CLASS: %s (%d)' % (c, cc.get(c, 0))]
        for x in [y for y in dis if y['cls'] == c]:
            D_ += ['  %s (%s) :: table %s ; textual %s ; elaborated %s' % (x['name'], x['provenance'], x['table'], x['textual'], x['elaborated']),
                   '      why: %s' % x['why'], '      elaborated: %s' % x['header'][:600], '      textual:    %s' % x['statement']]
        D_.append('')
    put_txt('b634_gate_disagreements.txt', D_)
    put_json('b634_gate_disagreements.json', dict(at=utc(), disagreements=dis, by_class=dict(cc)))
    U = jl('b634_unnamed_rows.json')
    UL = ['b634 -- COMPONENT 4: THE UNNAMED ROWS READ FROM THEIR ELABORATED BINDERS (%s)' % utc(), '']
    ures = []
    for x in U['rows']:
        if not x['in_scope']:
            UL.append('  %s / %s -- NOT SCORABLE THIS ACT: its kernel is not elaborated under (R244)(4)' % (x['repo'], x['name']))
            ures.append(dict(name=x['name'], repo=x['repo'], scorable=False))
            continue
        e = ET.get(x['name'])
        if e is None or e.get('missing'):
            UL.append('  %s -- NO ELABORATED TYPE' % x['name'])
            ures.append(dict(name=x['name'], repo=x['repo'], scorable=True, classified=False, cls='no type'))
            continue
        hdr = _elab_header(e)
        UL.append('  %s :: %s, table %s, textual %s, elaborated %s' % (x['name'], x['provenance'], x['table_grade'], x['rule_grade'], elab_grade(e)[0]))
        cls_any = []
        import e0_rule as E
        for b in e['binders']:
            t = b['type']
            if E.data_binder(t):
                c = 'data binder'
            elif E.domain_case(t, hdr):
                c = 'domain condition'
            else:
                nm, why = premise_name(t, hdr)
                c = ('named premise: %s' % nm) if nm else ('unnamed: %s' % why)
            cls_any.append(c)
            UL.append('      %-15s %-12s : %s  -> %s' % (b['kind'], b['name'], t[:160], c))
        UL.append('      conclusion: %s' % e['concl'][:300])
        ok = any(not c.startswith('unnamed') for c in cls_any[-len(e['binders']):]) if e['binders'] else False
        UL.append('      ### an elaborated head classified: %s' % ok)
        ures.append(dict(name=x['name'], repo=x['repo'], scorable=True, classified=ok, classes=cls_any))
    sc = [u for u in ures if u['scorable']]
    UL += ['', '### ### **ROWS %d ; IN SCOPE %d ; CLASSIFIED %d ; NOT SCORABLE THIS ACT %d.**' % (
        len(ures), len(sc), sum(1 for u in sc if u.get('classified')), len(ures) - len(sc))]
    put_txt('b634_unnamed_read.txt', UL)
    put_json('b634_unnamed_read.json', dict(at=utc(), rows=ures))
    print(L[2]); print(D_[2]); print(UL[-1])


# ================================================================================ COMPONENT 5: THE TABLE, THE PAGES, THE ROOT
def _table_grades():
    tg = {}
    for r in _table():
        tg.setdefault((r['repo'], r['name']), r['grade'])
    return tg


def table(*a):
    before = _table_grades()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    gmoved = sorted(n for n in set(before) | set(tg) if before.get(n) != tg.get(n))
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b634 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(diff.get('changed') or [])),
         '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
         '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %d ROWS MOVED %s.**' % (
             len(gmoved), dict(collections.Counter('%s -> %s' % (before.get(n), tg.get(n)) for n in gmoved)) or 'EMPTY')]
    L += ['  %s / %-60s %s -> %s' % (n[0], n[1], before.get(n), tg.get(n)) for n in gmoved]
    name = 'b634_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 grade_moved=[list(n) for n in gmoved], files_moved=moved))
    print(L[4])


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from b632's list and probe in force (no Lean), written only where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b634_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b634_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b634_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; cells moved %s' % (k, rc, changed, secs, len(dl), gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b634 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b634_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    save = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        c = TC.control()
    finally:
        CP.E0 = save
    for x in c:
        L.append('    %s (E0 at %s) %s : %s -- exit %d' % (TC.ARM, TC.RELAY_PIN, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b634_page_arms.txt', L)
    for l in L:
        print(l[:240])


ROOT_EXCLUDE = re.compile(r'^b634_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b634_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b634'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b634_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    L = ['b634 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b634_root_arm.txt', L)
    put_json('b634_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', K.CEN4, K.CEN5,
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
sorry_tokens = R3.sorry_tokens
HKEYS = ('H68a', 'H68b', 'H68c', 'H68d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b633_closing_push_out.txt', 'data/act_roots.txt', 'tools/act_root.py', 'tools/test_act_root.py',
              'tools/test_closing_headline_b634.py', 'tools/test_elab_reader_b634.py'}


def n5(trail_line=None, ot=None, *a):
    """### (R244)'s N5, the file-set by PATH; no grade moved on the table or a page."""
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
    face = jl('b634_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md')]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b634_|audit_b634_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    TF = jx('b634_table_final.json')
    no_move = bool(TF) and not TF.get('grade_moved') and all(not (jx('b634_page_%s.json' % k).get('cells_moved') or []) for k in ('zeta', 'chi'))
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and no_move and not tracked_local and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel unmoved against the face %s; no grade moved on the table or a page %s; PLACE-papers %s (beyond the '
            'ledgers: %s); %s; relay beyond the list, matched by path: %s; b628`s local intake bank in any relay commit %s, untracked now %s; '
            'no outbound request was made, so no identifier in one' % (kern_ok, no_move, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE',
                                                                       tracked_local, untracked_local))


def scores(*a):
    import b634_elab as EL
    TR = jx('b634_two_readings.json')
    DG = jx('b634_gate_disagreements.json')
    UR = jx('b634_unnamed_read.json')
    ET = EL.load_bank()
    RA = jx('b634_root_arm.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    T = [r for r in _table() if r['repo'] == K.KERNEL]
    have = sum(1 for r in T if r['name'] in ET and not ET[r['name']].get('missing'))
    a_ok = bool(T) and have == len(T)
    rate = (TR['agree'] / TR['both']) if TR.get('both') else 0
    b_ok = bool(TR) and rate >= 0.95
    dis = DG.get('disagreements') or []
    c_ok = bool(DG) and all(x['cls'] in K.CLASSES and (x['cls'] != 'other' or x['why']) for x in dis)
    sc = [u for u in (UR.get('rows') or []) if u['scorable']]
    ncl = sum(1 for u in sc if u.get('classified'))
    d_ok = bool(sc) and 2 * ncl >= len(sc)
    nall = len(UR.get('rows') or [])
    TF, TB = jx('b634_table_final.json'), jx('b634_rootlist_before.json')
    TA = jx('b634_rootlist_after.json')
    EJ = jx('b634_elab_runs.json')
    HT = jx('b634_elab_test.json')
    S = {
        'H68a': (('HOLDS' if a_ok else 'REFUTED'), 'the elaborated reader gives a type for %d of the table`s %d rows of %s' % (have, len(T), K.KERNEL)),
        'H68b': (('HOLDS' if b_ok else 'REFUTED'), 'agreement %s of %s rows read by both = %.4f' % (TR.get('agree'), TR.get('both'), rate)),
        'H68c': (('HOLDS' if c_ok else 'REFUTED'), 'disagreements %d, by class %s, each with its reason printed' % (len(dis), DG.get('by_class'))),
        'H68d': (('HOLDS' if d_ok else 'REFUTED'), 'of the %d rows the ruling`s words define, %d in scope: classified %d (at least half: %s); %d NOT SCORABLE '
                 'this act (their kernels unelaborated)' % (nall, len(sc), ncl, d_ok, nall - len(sc))),
        'N1': (('HELD' if a_ok else 'REFUTED'), 'as H68a'),
        'N2': (('HELD' if b_ok else 'REFUTED'), 'as H68b'),
        'N3': (('HELD' if c_ok else 'REFUTED'), 'as H68c'),
        'N4': (('HELD' if bool(sc) and ncl >= 11 else 'REFUTED'), 'by its letter, at least 11 classified: %d of the %d in scope (of %d defined by the '
               'ruling`s words; the ruling`s 22 is 85 - 63)' % (ncl, len(sc), nall)),
        'N5': n5v,
        'S1': (('HELD' if TF and not TF.get('grade_moved') else 'REFUTED'), 'the table regenerated at the end moves %s rows' % len(TF.get('grade_moved') or [])),
        'S2': (('HELD' if EJ and all(c.get('free_before', 0) >= K.HOLD_MB for c in EJ.get('calls') or []) else 'REFUTED'),
               'every elaborated call started above the hold: %s calls' % len(EJ.get('calls') or [])),
        'S3': (('HELD' if HT and HT.get('rc') == 0 and HT.get('cases') and HT.get('passing') == HT.get('cases') else 'REFUTED'),
               'the reader`s test %s of %s' % (HT.get('passing'), HT.get('cases'))),
        'S4': (('HELD' if TB and TA and TB['repositories'] == TA['repositories'] else 'REFUTED'),
               'the root`s repository list before %s and after %s the census path`s edit, equal %s' % (
                   len(TB.get('repositories') or []), len(TA.get('repositories') or []), TB.get('repositories') == TA.get('repositories'))),
        'S5': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
    }
    put_json('b634_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b634 — lane three, act sixty-one under (R244): the E0 rule read from elaborated types for SIDE-explicit-formula at v0.25 '
              'beside the textual reading, every disagreement classed, the unnamed rows read; the act-root census path at v0.5; the '
              'closing’s head line')


def _figures():
    TR, DG = jl('b634_two_readings.json'), jl('b634_gate_disagreements.json')
    n = len(TR['rows'])
    r = (TR['agree'] / TR['both']) if TR['both'] else 0
    d = len(DG['disagreements'])
    c = sum(1 for v in DG['by_class'].values() if v)
    return n, r, d, c, TR, DG


def _title_entry():
    n, r, d, c, _t, _d = _figures()
    return ('## The E0 rule from elaborated types for SIDE-explicit-formula at v0.25: %d declarations, agreement %.4f with the textual '
            'reading, %d disagreements in %d classes, the unnamed rows read; the act-root census path at v0.5' % (n, r, d, c))


def _finding_text():
    S, rl, J = jl('b634_scores.json'), jl('b634_record_lines.json'), jl('b634_act_root.json')
    n, r, d, c, TR, DG = _figures()
    U, UR = jl('b634_unnamed_rows.json'), jl('b634_unnamed_read.json')
    sc = [u for u in UR['rows'] if u['scorable']]
    n_ans = len(re.findall(r'^### PROMPT ', rd('b634_author_answers.txt'), re.M))
    KS = jl('b634_kernel_state.json')
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b634 on the author’s ruling `(R244)`%s. Banks: relay `data/b634_elab_types.txt`, `data/b634_two_readings.txt`, '
         '`data/b634_gate_disagreements.txt`, `data/b634_unnamed_rows.txt`, `data/b634_unnamed_read.txt`, `data/b634_kernel_state.txt`, '
         '`data/b634_act_root.txt`. Nothing deposits.*' % ((' and the author’s %d answer%s' % (n_ans, '' if n_ans == 1 else 's')) if n_ans else ''), '',
         '**The elaborated reader** (`(R244)`(4), W-ORD-GATE-FROM-ELABORATOR, OPEN_TRAILS :%d): a meta-program run by lake env lean against the '
         'kernel built at v0.25 = 8c51431, one module’s declarations per call under the hold, printing each declaration’s elaborated type '
         'with its binder kinds; %d modules at the pin, %d oleans absent. The E0 rule applied to the elaborated types by the same '
         'criterion, the header cut at the first anonymous arrow as the text cuts it, beside the textual reading.' % (
             K.GATE_WO, len(KS['modules']), len(KS['absent'])), '',
         '**The two readings:** %d rows of the kernel; %d read by both; agreement %d = %.4f; %d disagreements, by class %s. The textual rule '
         'stays the grading reader; no table or page grade moved; the author rules at the closing which disagreements move.' % (
             n, TR['both'], TR['agree'], r, d, dict((k, DG['by_class'].get(k, 0)) for k in K.CLASSES)), '',
         '**The unnamed rows** (`(R244)`(2)): the set the ruling’s words define is %d rows (the ruling’s 22 being 85 - 63, a count by '
         'premise); %d in this kernel, read from their elaborated binders, %d classified; the rest not scorable until their kernels are '
         'elaborated.' % (len(U['rows']), len(sc), sum(1 for u in sc if u.get('classified'))), '',
         '**The record lines** (`(R244)`(1)-(3)): b633 at its weight (FINDINGS :%d); the closing’s head line (OPEN_TRAILS :%d), the closing '
         'tool edited with its test; tools/act_root.py’s census path at v0.5 with its test, the root’s list printed before and after.' % tuple(
             x['line'] for x in rl['lines']), '',
         '**The root.** b634 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b625’s section-variable finding (relay data/b625_section_vars.txt), '
         'the occasion of the work-order; b632’s rule grades (FINDINGS :7701) and b633’s premise table (FINDINGS :7725), whose rows it reads '
         'a second time. It strengthens the programme’s offering of a grade that names what Lean itself elaborated and not only what the '
         'header’s text shows.', '',
         '**Next.** Per `(R244)`(5): b635, the (R110) deposit preparations, nothing deposited. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


def _next_lines():
    return ['b635 names no kernel terminal; the deposit preparations assemble the census at v0.5, the root chain, the kernel tags and the '
            'table’s provenance counts as the deposit description’s items']


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b634_scores.json', 'b634_findings.json', 'b634_record_lines.json', 'b634_act_root.json'))
    DG = jl('b634_gate_disagreements.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b634_author_answers.txt'), re.M))
    by = ['%s %d' % (k, DG['by_class'].get(k, 0)) for k in K.CLASSES]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R244) ratified.** (1) b633 at its weight. (2) The unnamed rows banked and read. (3) The closing’s head line. (4) '
             'W-ORD-GATE-FROM-ELABORATOR for SIDE-explicit-formula at v0.25; the act-root census path at v0.5. (5) The act after: b635.', '',
             '**Entered:** FINDINGS.md:%d (b633’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the closing’s head line, standing); this '
             'record.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line']), '',
             '**Act root:** b634 `%s` (previous `%s`, b633’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b634_author_answers.txt).' % n_ans, '',
             '**For the author’s ruling at the closing, the disagreements by class** (relay data/b634_gate_disagreements.txt): %s.' % '; '.join(by), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b634_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R244)`(5), b635, the (R110) deposit preparations; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


FOR_AUTHOR = ('(1) the unnamed rows as the set the ruling’s words define, the ruling’s 22 printed as 85 - 63; (2) the rows of other kernels '
              'in that set not scorable until those kernels are elaborated; (3) the elaborated header cut at the first anonymous explicit '
              'binder, so an arrow written in the conclusion stays there as the text has it; (4) agreement counted over the rows both '
              'readers read, the table’s statement-less rows printed apart; (5) the disagreement classes tested in the ferry’s order, the '
              'first that holds taken; (6) lake’s own up-to-date reading taken by `lake build --no-build` beside the oleans’ presence')


def desk(*a):
    S = jl('b634_scores.json')
    L = ['=' * 104, 'b634 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H68a-H68d, (R244)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0] == 'HOLDS' for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0] == 'HELD' for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0] == 'HELD' for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b634_defects.txt').rstrip(NL).split(NL)
    put_txt('b634_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b634_scores.json', 'b634_findings.json', 'b634_trail.json', 'b634_record_lines.json', 'b634_act_root.json'))
    KS = jl('b634_kernel_state.json')
    L = ['b634 -- THE COMPONENTS, BANKED UNDER (R244).', '',
         '### COMPONENT 0 : the process listing ; b633`s closing push-out relay %s ; push-b633* branches deleted by name (data/b634_branches.txt) ; '
         'every test file under tools/ run (data/b634_tests_stepzero.txt) ; the unnamed rows (data/b634_unnamed_rows.txt) ; the suite run at HEAD '
         'before the face (data/b634_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b633`s weight FINDINGS :%d ; the head line :%d ; the closing tool`s head line (data/b634_headline_test.txt) ; '
         'act_root.py`s census path (data/b634_actroot_test.txt, data/b634_rootlist_before.txt, data/b634_rootlist_after.txt)' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the kernel`s state (data/b634_kernel_state.txt): %d modules, %d oleans absent, --no-build exit %s' % (
             len(KS['modules']), len(KS['absent']), KS['nobuild_rc']),
         '### COMPONENT 3 : the elaborated reader (tools/b634_elab.py, data/b634_elab_test.txt) ; data/b634_elab_types.txt ; H68a %s' % S['H68a'][0],
         '### COMPONENT 4 : data/b634_two_readings.txt ; data/b634_gate_disagreements.txt ; data/b634_unnamed_read.txt ; H68b %s, H68c %s, H68d %s' % (
             S['H68b'][0], S['H68c'][0], S['H68d'][0]),
         '### COMPONENT 5 : the pages (data/b634_page_zeta.json, data/b634_page_chi.json) ; page arms data/b634_page_arms.txt ; the root %s' % J['root'][:16],
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b635 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b634_components.txt', L)


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
    put_json('b634_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


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
    put_json('b634_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b634_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-06 by b634 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b634_defects.json -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    if 'dry' in a:
        print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b634_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b634_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
