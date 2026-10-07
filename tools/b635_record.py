# -*- coding: utf-8 -*-
"""b635_record.py -- THE ACT'S RECORD TOOL, UNDER (R245). ### ONE SUBCOMMAND PER BANK.

### ### b635: LANE THREE, ACT SIXTY-TWO -- THE TWELVE DISAGREEMENTS RULED FOR THE ELABORATED READING AND THE TEXTUAL RULE REPAIRED; THE
### THIRTEEN PHANTOM NAMES RESOLVED OR CORRECTED; THE CASCADE REBUILT; THE MIRROR REFRESHED WITH THE ROOT LINE; THE DEPOSIT DESCRIPTION'S
### ITEMS BANKED, NOTHING DEPOSITED.
### Subcommands write only `data/b635_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic
### helpers are b633's record tool's, imported; ledger appends through b566's guarded `append_to`. The data is tools/b635_worklist.py;
### the elaborated reader is tools/b635_elab.py. No platform is called; the (R110) token is never read beyond its presence, never printed
### and never used. b628's full intake bank is never read here, never staged or committed.
"""
import collections
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b635_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = R3.SP
SESSION, SESSION_ID = R3.SESSION, R3.SESSION_ID
FACE = 'b635_registration_2026-10-07.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_txt, put_json, jl, jx, rd, _write, _scan, _clean = R3.put_txt, R3.put_json, R3.jl, R3.jx, R3.rd, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
KERNS, KERN_PIN, kern_state, sorry_tokens = R3.KERNS, R3.KERN_PIN, R3.kern_state, R3.sorry_tokens

DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b635_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''

# ### the table's stable inputs the generator reads after its edit ((R245)(2)-(3), the author's first answer before the seal)
ELAB_TYPES = 'elab_types.txt'
RETIRE = 'table_retire.json'
REPOINT = 'table_repoint.json'
KERNEL_PREFIXES = ('SIDEExplicitFormula', 'Zeta23', 'Lc', 'Hadamard', 'FunctionsOfOneComplexVariable')   # ### the kernel's own module roots


def defects(*a):
    L = ['b635 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b635_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b635_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b635 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the reads the ferry names, the manifest line, b634`s lines and record', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12354, 12356, 12799, K.MANIFEST_LINE, K.BUILD_ROUTE] + list(range(13251, 13278)), 1500),
        ('FINDINGS: b634`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B634_ENTRY], 600),
        ('relay data/b634_gate_disagreements.txt whole', RELAY, PRE_RELAY, 'data/b634_gate_disagreements.txt', ('GREP', r'.'), 300),
        ('relay data/b634_handread.txt whole', RELAY, PRE_RELAY, 'data/b634_handread.txt', ('GREP', r'.'), 300),
        ('relay data/b634_kernel_stale.txt', RELAY, PRE_RELAY, 'data/b634_kernel_stale.txt', ('GREP', r'^###|^  SIDE'), 300),
        ('relay tools/e0_rule.py: the patterns the three repairs touch', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'^(BINDER = |INSTANCE = |CLASS_PREDS_B625 = |SUPPORT = |def (grade|conclusion|statement_only|domain_case)\b)'), 200),
        ('relay tools/test_e0_rule.py: its cases', RELAY, PRE_RELAY, 'tools/test_e0_rule.py', ('GREP', r"want\('\(\d+\)"), 160),
        ('relay tools/terminal_table.py: the name patterns, the rule reading, the provenance', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r'^(NAME_RE = |PRINT_SRC = |def (rule_reading|provenance|build)\b)'), 200),
        ('relay tools/mirror_build.ps1 (unedited): its parameter, stage, MANIFEST and zip lines', RELAY, PRE_RELAY, 'tools/mirror_build.ps1',
         ('GREP', r'^(param\(|\$stage = |\$man -join|\$zip = |Compress-Archive)'), 200),
        ('PLACE-papers README.md: the (R183)(3) and (R232)(3) paragraphs, the supportable lines, the deposit note', PP, PRE_PP, 'README.md',
         ('GREP', r'^(\*\(Appended under the author.s ruling `\((R183|R232)\)`|Supportable:|Not supportable:|\*\*Deposit note)'), 300),
        ('relay data/act_roots.txt', RELAY, PRE_RELAY, 'data/act_roots.txt', ('GREP', r'^b6'), 200),
        ('relay data/b634_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b634_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b635 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    L += ['', '### the (R110) token`s location, by path alone: the environment variable ZENODO_TOKEN ((R110), OPEN_TRAILS :9514, "the token in the '
          'environment only"); its contents not read here',
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b635_reads.txt', L)


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R245) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b635 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b635_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b635_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b635_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = '*Appended 2026-10-07 by b635 to b634’s entry (:%d), under `(R245)`(1) -- b634 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
CAP_HEAD = '*Appended 2026-10-07 by b635 to b634’s record (:%d), under `(R245)`(1) -- RULE 14’S CAPTURE APPLIED TO AN AS-OF REFUSAL, STANDING:*'


def _weight():
    TR, DG = jl('b634_two_readings.json'), jl('b634_gate_disagreements.json')
    RB = jl('b634_rebuild.json')
    return ('\n%s the elaborated reader over the explicit-formula kernel at v0.25 (relay tools/b634_elab.py, its test 6 of 6): 86 module '
            'calls and 9 resolving calls, types read for 927 of the kernel’s 940 table rows; the textual and elaborated grades agreeing on '
            '%d of %d both read, %.4f; %d disagreements banked by class (relay data/b634_gate_disagreements.txt), the hand-read governing '
            '(relay data/b634_handread.txt: 11 notation or coercion, 1 other); 13 table names no constant carries at the pin. The unnamed rows '
            '20 by rows, 5 in the kernel, 2 of 5 classified by their own unnamed head (OPEN_TRAILS :%d). Doubling, SaltCheckProduct and '
            'Dedekind rebuilt by lake on the author’s word, %d calls, no hold crossed, 28 constants and 0 differences; the reader relaunched '
            'as its own process from call 58 after the host’s stop, the environment’s. tools/act_root.py at the census v0.5, 38 repositories '
            'before and after. Relay c4edac72, closing f022c6ab; PLACE-papers 9a929ce; the root 56ea148d…e571, b624 to b634 agreeing; the '
            'suite 78 of 79 by G-ELAB-TYPES reading the superseded calls beside the 95 governing ones. Nothing deposited; no kernel source '
            'touched; no grade moved.\n' % (W_HEAD % K.B634_ENTRY, TR['agree'], TR['both'], TR['agree'] / TR['both'], len(DG['disagreements']),
                                           K.B634_CORRECTION, len(RB.get('calls') or [])))


def _capture():
    return ('\n%s from b635 on, an as-of call (relay tools/asof_lines.py) that refuses has its whole output kept as '
            '<act>_closing_asof_attempt1.txt before a second call, as rule 14 keeps a refused push’s capture; b634’s first as-of call '
            'refused and its output was not kept, so what it read cannot be read now -- its second call wrote the six lines (relay '
            'data/b634_closing_push_out.txt).\n' % (CAP_HEAD % K.B634_RECORD))


def record_lines(*a):
    """### FINDINGS: b634's weight (to :7747). OPEN_TRAILS: rule 14's capture for an as-of refusal (to b634's record :13253)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The E0 rule from elaborated types')
    if entry != K.B634_ENTRY:
        sys.exit('### b634`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B634_ENTRY, _weight()), ('OPEN_TRAILS.md', CAP_HEAD % K.B634_RECORD, _capture())]
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
    _land(Q, items, 'b635_record_lines.json', K.B634_ENTRY)


# ================================================================================ THE ELABORATED READING (shared by the components)
def _elab_header(e):
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
    return E.grade(_elab_header(e), 'theorem' if e['kind'] == 'theorem' else 'def')[:2]


def text_grade(statement, name):
    import terminal_table as TT
    return TT.rule_reading(statement, name)[1]


# ================================================================================ COMPONENT 2: THE TWELVE
RULED = {}   # ### filled from b634's banks by `twelve`: the ruled grade of each row (R245)(2)


def twelve(*a):
    """### (R245)(2): each of the twelve printed with its table grade, its textual and elaborated grades at b634 and the ruled grade; the
    ### retire list written for the row naming no declaration (data/table_retire.json, the generator's input after its edit)."""
    import b634_elab as EL4
    B = EL4.load_bank()
    DG = jl('b634_gate_disagreements.json')['disagreements']
    T = {r['name']: r for r in _table() if r['repo'] == K.KERNEL}
    L = ['b635 -- COMPONENT 2, (R245)(2): THE TWELVE, EACH WITH ITS READINGS AND THE RULED GRADE (%s)' % utc(), '']
    rows = []
    for x in DG:
        n = x['name']
        e = B.get(n)
        if n == K.RETIRED_NAMESPACE:
            ruled, why = 'RETIRED', 'a namespace and not a terminal: the row names no declaration ((R245)(2))'
        elif n in K.CHI8:
            ruled, why = x['elaborated'], 'the conclusion is type_of%: the elaborated type is the statement, its binders take the criterion'
        elif n == 'ZerosBound':
            ruled, why = x['elaborated'], 'the binder hfAnalytic, nested two deep, read: a premise on AnalyticOnNhd'
        else:
            ruled, why = 'DERIVES', 'Integrable read under its qualified name: a domain condition under clause (iii)'
        rows.append(dict(name=n, provenance=T[n].get('provenance'), table=T[n]['grade'], textual=x['textual'], elaborated=x['elaborated'], ruled=ruled, why=why))
        L += ['  %-70s %-5s table %-12s textual %-12s elaborated %-20s RULED %s' % (n, T[n].get('provenance'), T[n]['grade'], x['textual'],
                                                                                    x['elaborated'], ruled), '      %s' % why]
    L += ['', '### ### **THE TWELVE : %d ; RULED FOR THE ELABORATED READING %d ; RETIRED %d ; MOVES ON THE TABLE (rule rows whose ruled grade '
          'differs from the table) %d.**' % (len(rows), sum(1 for r in rows if r['ruled'] != 'RETIRED'), sum(1 for r in rows if r['ruled'] == 'RETIRED'),
                                             sum(1 for r in rows if r['provenance'] == 'rule' and r['ruled'] != r['table']))]
    put_txt('b635_twelve.txt', L)
    put_json('b635_twelve.json', dict(at=utc(), rows=rows))
    if not DRY:
        cur = json.load(io.open(os.path.join(D, RETIRE), encoding='utf-8')) if os.path.exists(os.path.join(D, RETIRE)) else dict(retire=[])
        if not any(x['name'] == K.RETIRED_NAMESPACE for x in cur['retire']):
            cur['retire'].append(dict(repo=K.KERNEL, name=K.RETIRED_NAMESPACE, act='b635', ruling='(R245)(2)',
                                      cite='relay data/b634_handread.txt (12); FINDINGS :%d' % K.B634_ENTRY,
                                      why='a namespace and not a terminal: the row names no declaration'))
        _write(os.path.join(D, RETIRE), (json.dumps(cur, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        print('  written: %s' % RETIRE)
    print(L[-1])


def rule_test(*a):
    """### (R245)(2): the rule's three repairs printed against its blob at the act's pre-relay pin; test_e0_rule.py run and counted."""
    old = (_show(RELAY, PRE_RELAY, 'tools/e0_rule.py') or '').split(NL)
    new = io.open(os.path.join(ROOT, 'tools', 'e0_rule.py'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, 'e0_rule.py@%s' % PRE_RELAY, 'e0_rule.py', lineterm='', n=0))
    put_txt('b635_rule_diff.txt', ['b635 -- (R245)(2): THE RULE`S THREE REPAIRS, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), ''] + dl)
    _run_test('tools/test_e0_rule.py', 'b635_rule_test', SP + '/b635_planted_rule')


def gen_test(*a):
    """### the generator's edit, the author's first answer before the seal: tools/test_terminal_table_b635.py run and counted."""
    old = (_show(RELAY, PRE_RELAY, 'tools/terminal_table.py') or '').split(NL)
    new = io.open(os.path.join(ROOT, 'tools', 'terminal_table.py'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, 'terminal_table.py@%s' % PRE_RELAY, 'terminal_table.py', lineterm='', n=0))
    put_txt('b635_gen_diff.txt', ['b635 -- THE GENERATOR`S EDIT, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), ''] + dl)
    _run_test('tools/test_terminal_table_b635.py', 'b635_gen_test')


def _table_state():
    out = {}
    for r in _table():
        out.setdefault((r['repo'], r['name']), (r['grade'], r.get('provenance'), r.get('mark') or ''))
    return out


def table(*a):
    """### the terminal table regenerated; every row whose grade, provenance or mark moved printed before and after; rows added and gone."""
    before = _table_state()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _table_state()
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    tag = a[0] if a and a[0] != 'dry' else 'table'
    files = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    L = ['b635 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade, provenance or mark moved %d ; the table files that moved against relay HEAD: %s' % (
             len(added), len(gone), len(moved), files or 'NONE'),
         '### by kind: %s' % dict(collections.Counter('%s -> %s' % (before[k], after[k]) for k in moved)), '']
    L += ['  MOVED %s / %-62s %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved]
    L += ['  ADDED %s / %-62s %s' % (k[0], k[1], after[k]) for k in added]
    L += ['  GONE  %s / %-62s %s' % (k[0], k[1], before[k]) for k in gone]
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d.**' % (len(moved), len(added), len(gone))]
    if r.returncode:
        L += ['### THE GENERATOR EXITED %d:' % r.returncode] + (r.stdout + r.stderr).rstrip(NL).split(NL)[-15:]
    name = 'b635_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, moved=[[k[0], k[1], list(before[k]), list(after[k])] for k in moved],
                                                 added=[list(k) for k in added], gone=[list(k) for k in gone], files_moved=files,
                                                 grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def agree(*a):
    """### (R245)(2), H69a: the eleven at the elaborated rerun (data/b635_elab_rerun11.txt) against the repaired textual rule and the table."""
    import b635_elab as EL
    RR = EL.parse(rd('b635_elab_rerun11.txt'))
    TW = {x['name']: x for x in jl('b635_twelve.json')['rows']}
    T = {r['name']: r for r in _table() if r['repo'] == K.KERNEL}
    L = ['b635 -- COMPONENT 2, H69a: THE ELEVEN AT THE RERUN, THE REPAIRED TEXTUAL RULE BESIDE THEM (%s)' % utc(), '']
    res = []
    for n in K.ELEVEN:
        e = RR.get(n)
        eg = elab_grade(e)[0] if e and not e['missing'] else 'NO TYPE'
        tg = text_grade(T[n].get('statement'), n) if n in T else None
        tb = T.get(n, {})
        how = 'agrees by deferral (type_of%)' if tg == 'DEFERRED' else ('agrees' if tg == eg else 'DIFFERS')
        ok = eg == TW[n]['ruled'] and (tg == eg or tg == 'DEFERRED') and (tb.get('grade') == eg or tb.get('provenance') == 'cell')
        res.append(dict(name=n, elaborated=eg, textual=tg, ruled=TW[n]['ruled'], table=tb.get('grade'), provenance=tb.get('provenance'), ok=ok))
        L.append('  %-70s elaborated %-20s repaired textual %-12s ruled %-20s table %s (%s) -- %s%s' % (
            n, eg, tg, TW[n]['ruled'], tb.get('grade'), tb.get('provenance'), how, '' if ok else ' ### NOT AS RULED'))
    L += ['', '### ### **AS RULED AND AGREEING : %d of %d.**' % (sum(1 for x in res if x['ok']), len(res))]
    put_txt('b635_agree.txt', L)
    put_json('b635_agree.json', dict(at=utc(), rows=res))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE THIRTEEN
PHANTOM_SOURCES = ('AxiomCheck*.lean',)


def phantom(*a):
    """### (R245)(3): each name the table cites with no constant behind it, printed with the line that introduced it (the kernel's
    ### `#print axioms` line the table reads, its commit by `git log -S`, one call each; the ledger line naming its full form); the cause
    ### read; a truncated name re-pointed (old -> new) in data/table_repoint.json; a name existing nowhere given a correction entry and
    ### retired (none expected by the reads). Banked as data/b635_phantom_names.txt and its json."""
    import b634_elab as EL4
    B = EL4.load_bank()
    names = [n for n, e in B.items() if e['missing']]
    prints = []
    for f in g(K.KER, 'ls-tree', '--name-only', K.KER_PIN).split(NL):
        if re.match(r'^AxiomCheck.*\.lean$', f):
            for i, l in enumerate(lines_of(_show(K.KER, K.KER_PIN, f) or ''), 1):
                m = re.match(r'^\s*#print\s+axioms\s+(\S+)', l)
                if m:
                    prints.append((f, i, m.group(1)))
    import terminal_table as TT
    find = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    L = ['b635 -- COMPONENT 3, (R245)(3): THE THIRTEEN NAMES THE TABLE CITES WITH NO CONSTANT BEHIND THEM (%s)' % utc(), '',
         '### the table reads these rows from the kernel`s `#print axioms` lines (tools/terminal_table.py PRINT_SRC, whose name pattern',
         '### [A-Za-z_][A-Za-z0-9_.\u2019\']* stops at the first character outside it -- ℝ, ₀, ₁): each name below is the head of a printed name', '']
    out, repoint = [], []
    for n in names:
        hits = [(f, i, full) for f, i, full in prints if full != n and full.startswith(n) and TT.PRINT_SRC.match('#print axioms ' + full)
                and TT.PRINT_SRC.match('#print axioms ' + full).group(1) == n]
        exact = [(f, i, full) for f, i, full in prints if full == n]
        fulls = sorted(set(h[2] for h in hits))
        if len(fulls) == 1:
            full = fulls[0]
            f, i, _x = hits[0]
            log = g(K.KER, 'log', '--reverse', '--format=%h %cI %s', '-S', full, K.KER_PIN, '--', f).strip().split(NL)
            intro = log[0][:120] if log and log[0] else '### NOT FOUND'
            led = ['FINDINGS :%d' % (j + 1) for j, l in enumerate(find) if full in l][:2] + ['OPEN_TRAILS :%d' % (j + 1) for j, l in enumerate(ot) if full in l][:2]
            kind = 'TRUNCATED -> RE-POINTED'
            res = dict(name=n, kind=kind, full=full, source='%s :%d' % (f, i), commit=intro, ledger=led or ['no ledger line names the full form'])
            repoint.append(dict(repo=K.KERNEL, old=n, new=full, act='b635', ruling='(R245)(3)', cite='SIDE-explicit-formula %s %s :%d, introduced %s' % (
                K.KER_PIN, f, i, intro.split()[0] if intro[:1] != '#' else '?'), why='the table`s name pattern stops at a non-ASCII identifier character'))
        elif exact:
            f, i, _x = exact[0]
            log = g(K.KER, 'log', '--reverse', '--format=%h %cI %s', '-S', n, K.KER_PIN, '--', f).strip().split(NL)
            intro = log[0][:120] if log and log[0] else '### NOT FOUND'
            kind = 'UPSTREAM, OUTSIDE THE READER`S IMPORTS'
            res = dict(name=n, kind=kind, full=n, source='%s :%d' % (f, i), commit=intro, ledger=['the name is printed whole; the reader`s module '
                                                                                                  'choice did not import its Mathlib module'])
        else:
            res = dict(name=n, kind='EXISTS NOWHERE', full=None, source=None, commit=None, ledger=[])
        out.append(res)
        L += ['  %s' % n, '      %s%s' % (res['kind'], (' -> ' + res['full']) if res.get('full') and res['full'] != n else ''),
              '      source: %s ; introduced: %s' % (res.get('source'), res.get('commit')), '      ledger: %s' % '; '.join(res.get('ledger') or [])]
    c = collections.Counter(x['kind'] for x in out)
    L += ['', '### ### **THE THIRTEEN : %d ; %s ; NONE DROPPED.**' % (len(out), dict(c))]
    put_txt('b635_phantom_names.txt', L)
    put_json('b635_phantom_names.json', dict(at=utc(), names=out))
    if not DRY:
        _write(os.path.join(D, REPOINT), (json.dumps(dict(repoint=repoint), indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        print('  written: %s (%d entries)' % (REPOINT, len(repoint)))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES AND THE README
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from b632's list and probe in force (no Lean), written only where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b635_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b635_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
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
    put_json('b635_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; cells moved %s' % (k, rc, changed, secs, len(dl), gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b635 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b635_gcp'), os.path.join(D, K.PROBE[k]))
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
    put_txt('b635_page_arms.txt', L)
    for l in L:
        print(l[:240])


README_HEAD = ('*(Appended under the author\'s ruling `(R245)`(5)(ii), 2026-10-07, b635, beside the `(R232)`(3) sentence directly above, which '
               'stays, as do the `(R146)`(2), `(R174)`(1), `(R176)`(2), `(R177)`(2), `(R182)`(2) and `(R183)`(3) sentences: SIDE-explicit-formula '
               'v0.22–v0.25 entered at their weight, v0.25 = `8c51431`.)*')
README_TEXT = (' Supportable, the seat\'s sentence for the author\'s strike: *RH up to the Platt–Trudgian height stated as rh_upto and carried at '
               'INTERFACES on its one named premise PlattTrudgianHeight (rh_upto_platt, v0.22); the simple-zero proportion two_thirds cited from '
               'its source kernel, with its axioms read there, and not proved in this one (SimpleProportion, v0.23); RH ⟺ the Nyman–Beurling '
               'condition carried at INTERFACES on NymanBeurlingPremise (rh_iff_nb, v0.24); Weil positivity for the Dedekind configuration of '
               'modulus q exactly when the ζ target holds and GRH_chi holds for every member of the family (dedekind_instance, v0.25; '
               'dedekind_three at q = 3), its right-hand side split into the trivial character\'s term and the family\'s carried at INTERFACES on '
               'TrivialSummandPremise and EulerFactorPremise (dedekind_rhs).* Not supportable, unchanged: *RH proved*; *h2_sign proved*; '
               '*λ_n ≥ 0 proved*; *simplicity proved*; *GRH reduced for any modulus beyond the family theorem\'s letter*.')


def readme(*a):
    """### (R245)(5)(ii): README's supportable paragraph extended for v0.22-v0.25 in the (R183)(3) form, appended after the (R232)(3)
    ### paragraph and before `## Structure`, the not-supportable sentence unchanged; the scanner run; nothing else moves."""
    p = os.path.join(PP, 'README.md')
    raw = open(p, 'rb').read()
    t = raw.decode('utf-8')
    if README_HEAD in t:
        sys.exit('### THE APPEND STANDS ALREADY -- NOTHING WRITTEN')
    anchor = t.find('\n## Structure')
    i232 = t.find("*(Appended under the author's ruling `(R232)`(3)")
    if anchor < 0 or i232 < 0 or i232 > anchor:
        sys.exit('### THE ANCHORS ARE NOT WHERE THE READS FOUND THEM -- NOTHING WRITTEN')
    nlc = '\r\n' if '\r\n' in t else '\n'
    para = README_HEAD + README_TEXT
    new = t[:anchor] + nlc + para + nlc + t[anchor:] if not t[:anchor].endswith(nlc + nlc) else t[:anchor] + para + nlc + nlc + t[anchor + len(nlc):]
    sc, clean = _scan_text(para, 'readme')
    nd, _n = _nd(para)
    cells = predict_cells(para, 'README.md')
    print('  scanner %s ; no-disclosure %s ; table cells %s ; bytes %d -> %d' % ('CLEAN' if clean else 'NOT CLEAN', nd, cells or 'NONE', len(raw), len(new.encode('utf-8'))))
    if DRY:
        print(para)
        return
    if not clean or any(nd.values()) or cells:
        sys.exit('### THE APPEND WOULD CARRY A STEM, TECHNE TEXT OR A TABLE CELL -- NOTHING WRITTEN')
    if not new.startswith(t[:anchor]) or not new.endswith(t[anchor:]):
        sys.exit('### THE EDIT WOULD MOVE A BYTE OUTSIDE THE APPEND -- NOTHING WRITTEN')
    _write(p, new.encode('utf-8'))
    ls = new.replace('\r', '').split('\n')
    line = next(i + 1 for i, l in enumerate(ls) if l.startswith(README_HEAD[:60]))
    put_json('b635_readme.json', dict(at=utc(), line=line, head=README_HEAD, bytes_before=len(raw), bytes_after=len(new.encode('utf-8')),
                                      sha256=sha(new.encode('utf-8'))))
    print('  README :%d' % line)


# ================================================================================ COMPONENT 5: THE DEPOSIT BANK
def _remote(repo_path, cache):
    if repo_path not in cache:
        r = subprocess.run(['git', '-C', repo_path, 'ls-remote', 'origin'], capture_output=True)
        cache[repo_path] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in r.stdout.decode('utf-8', 'replace').split(NL) if '\t' in l)
    return cache[repo_path]


# ### ### **b636, (R246)(2)(iii): THE TAG MATCHER READS THE REGISTRY'S TAG FORM ALONE AND NOTHING IN PROSE.** ### b635's matcher took every
# ### backticked vN.N[.N] on a one-kernel line as a cited tag and read REGISTRY :705's prose ("`ab6f269` prices the `v0.5` matching-
# ### certificate target") as a SIDE-window tag. The REGISTRY's tag form, read off its tag lines: the version bound to a commit (`vX` = `sha`,
# ### = commit / = peeled `sha`, `vX`, HEAD `sha`, `vX`/`sha`), the version after the word tag (tag `vX`), or the version alone in a table
# ### cell (| `vX` |); emphasis marks between are read through. A version in running text with none of these is prose and no tag.
# ### tools/test_registry_tags_b636.py is its test, :705's sentence its negative case.
TAG_FORM = re.compile(r'(?:\btag\s*\**\s*`(v\d+(?:\.\d+){1,2})`'
                      r'|`(v\d+(?:\.\d+){1,2})`\**\s*(?:=\s*(?:commit\s+|peeled\s+)?|,\s*HEAD\s+|/)\**`[0-9a-f]{7,40}`'
                      r'|\|\s*\**\s*`(v\d+(?:\.\d+){1,2})`\s*\**\s*\|)')


def registry_tags(text=None):
    """### every (kernel, tag) pair REGISTRY names on one line: a `SIDE-...` repository and a backticked `vN.N[.N]` tag in the REGISTRY's tag
    ### form (b636, TAG_FORM). `text` given, it is read in place of REGISTRY.md at PLACE-papers' working tree."""
    t = (text if text is not None else io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8').read()).replace(chr(13), '')
    pairs = set()
    for i, l in enumerate(t.split(NL), 1):
        ks = set(re.findall(r'\b(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)\b', l))
        tags = set(next(x for x in m.groups() if x) for m in TAG_FORM.finditer(l))
        if len(ks) == 1 and tags:
            k = ks.pop()
            for tg in tags:
                pairs.add((k, tg))
    return sorted(pairs)


def deposit(*a):
    """### (R245)(5)(ii)-(iv): data/b635_deposit_items.txt, the deposit description's items in the deposit note's own form, every item
    ### resolved to a path and head at the remote (one ls-remote per repository); the token's presence confirmed and nothing else;
    ### the no-disclosure arm over the bank."""
    import b616_record as R6
    cache = {}
    pp_head = g(PP, 'rev-parse', 'HEAD').strip()
    pp_rem = _remote(PP, cache).get('refs/heads/main', '')
    relay_head = g(RELAY, 'rev-parse', 'HEAD').strip()
    relay_rem = _remote(RELAY, cache).get('refs/heads/main', '')
    items = []

    def item(label, repo, path, head, rem, extra=''):
        ok = bool(head) and head == rem and (path is None or subprocess.run(['git', '-C', repo, 'cat-file', '-e', '%s:%s' % (head, path)]).returncode == 0)
        items.append(dict(label=label, repo=repo.replace('D:/', '').replace('MY-DOwnloads/', ''), path=path, head=head, remote=rem, ok=ok, extra=extra))

    t = io.open(os.path.join(PP, 'README.md'), encoding='utf-8').read().replace(chr(13), '')
    sup = [l for l in t.split(NL) if re.match(r"^\*\(Appended under the author's ruling `\((R183|R232|R245)\)`", l)]
    item('the supportable sentence for v0.17-v0.25 as README carries it: the (R183)(3), (R232)(3) and (R245)(5)(ii) paragraphs', PP, 'README.md', pp_head, pp_rem,
         ' / '.join(re.sub(r'^\*\(Appended under the author.s ruling `(\(R\d+\)`\(\d+\)(?:\(\w+\))?).*', r'\1', l) for l in sup))
    item('the keystone census at v0.5, its 42-premise table in its back matter (§ "The named premises the INTERFACES rows rest on")', PP, K.CEN5, pp_head, pp_rem)
    item('the sieve at v0.6', PP, K.SIEVE6, pp_head, pp_rem)
    roots = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()]
    item('the root chain b624 onward, by its last line at this bank (%s); b635`s own line lands at its record and in the mirror`s MANIFEST' % roots[-1][:80],
         RELAY, 'data/act_roots.txt', relay_head, relay_rem)
    T = _table()
    pv = collections.Counter(r.get('provenance') for r in T)
    item('the terminal table after (R245)(2) and (3): %d rows, provenance %s' % (len(T), dict(pv)), RELAY, 'data/terminal_table.json', relay_head, relay_rem)
    tags = []
    for k, tg in registry_tags():
        p = 'D:/' + k
        if not os.path.isdir(p):
            tags.append(dict(kernel=k, tag=tg, peel=None, ok=False, why='no clone'))
            continue
        ref = _remote(p, cache)
        peel = ref.get('refs/tags/%s^{}' % tg) or ref.get('refs/tags/%s' % tg)
        tags.append(dict(kernel=k, tag=tg, peel=peel, ok=bool(peel)))
    env_user = subprocess.run(['powershell', '-NoProfile', '-Command', "[bool][Environment]::GetEnvironmentVariable('ZENODO_TOKEN','User')"],
                              capture_output=True, text=True).stdout.strip()
    present = bool(os.environ.get('ZENODO_TOKEN')) or env_user == 'True'
    L = ['b635 -- (R245)(5)(ii)-(iv): THE DEPOSIT DESCRIPTION`S ITEMS, IN THE DEPOSIT NOTE`S OWN FORM, NOTHING DEPOSITED (%s)' % utc(), '',
         '**Deposit preparations (`(R110)` route), the items.** Each item by its path and its head, the head read back at the remote. '
         '**Nothing deposits; the deposit is the author`s own act at a time the author names.**', '']
    for x in items:
        L.append('- %s -- `%s` %s @ `%s` (remote main `%s`): %s%s' % (x['label'], x['repo'], x['path'] or '', x['head'][:7], (x['remote'] or '')[:7],
                                                                       'RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', (' -- ' + x['extra']) if x['extra'] else ''))
    L += ['', '- every kernel tag REGISTRY cites, peeled at its remote (%d):' % len(tags)]
    L += ['    `%s` `%s` = `%s` %s' % (x['kernel'], x['tag'], (x['peel'] or '')[:40], 'RESOLVES' if x['ok'] else '### ' + x.get('why', 'NOT AT THE REMOTE'))
          for x in tags]
    L += ['', '- the not-supportable sentence, unchanged: *RH proved*; *h2_sign proved*; *λ_n ≥ 0 proved*; *simplicity proved*; *GRH reduced for '
          'any modulus beyond the family theorem`s letter*.',
          '- the `(R110)` token: its location the environment variable ZENODO_TOKEN; present %s; not printed, not read beyond its presence, '
          'no call made with it.' % ('YES' if present else 'NO')]
    text = NL.join(L)
    nd = R6.nd_hits(text, R6.nd_sets())[0]
    ok_all = all(x['ok'] for x in items) and all(x['ok'] for x in tags)
    L += ['', '### ### **ITEMS %d ; RESOLVING %d ; TAGS %d ; RESOLVING %d ; NO-DISCLOSURE HITS %s ; TOKEN PRESENT %s.**' % (
        len(items), sum(1 for x in items if x['ok']), len(tags), sum(1 for x in tags if x['ok']), dict(nd), present)]
    put_txt('b635_deposit_items.txt', L)
    put_json('b635_deposit_items.json', dict(at=utc(), items=items, tags=tags, nd=dict(nd), all_resolve=ok_all, token_present=present,
                                             lsr={k.replace('D:/', ''): 1 for k in cache}))
    print(L[-1])


# ================================================================================ COMPONENT 6: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b635_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b635_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b635'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b635_act_root.json')
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
    L = ['b635 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b635_root_arm.txt', L)
    put_json('b635_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ COMPONENT 7: THE MIRROR
TAG = DATE
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % TAG
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % TAG)
PREV_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-04.zip'


def mbuild(*a):
    """### the builder, unedited, with -DateTag, after the act's last push (PLACE-papers HEAD at its remote); it writes the zip in
    ### D:/MY-DOwnloads, its stage in %TEMP% and relay tools/mirror_prevbuild.json (its state). Refuses if the zip or stage exists."""
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED (the builder deletes a same-named one)')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag', TAG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b635_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-1500:], r.stderr[-800:], 'exit', r.returncode)


def mroot(*a):
    """### OPEN_TRAILS :12929, standing: the line "Act root: <act> <root>" from relay data/act_roots.txt's last line added to MANIFEST in
    ### its stage, in MANIFEST's own form, by b614's stage pattern -- the staged MANIFEST written and the zip's one entry updated in place."""
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b635':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b635`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    body = text.rstrip('\r\n')
    out = body + sep + sep + line + sep
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b635_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode,
                                           update_err=ps.stderr.strip()))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    """### relay tools/mirror_verify.py on the zip, all three clauses, run from PLACE-papers (clause 2's ls-remote is cwd-dependent)"""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b635_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-1200:])


def mbank(*a):
    """### data/b635_mirror.txt and its json: the zip's md5, sha256 and size, its file count, the MANIFEST's md5 and its root line, the
    ### previous build's MANIFEST md5, the verification's verdict; the no-disclosure arm over the zip's file list."""
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    text = man.decode('utf-8-sig').replace(chr(13), '')
    ls = text.split(NL)
    rows = [l for l in ls if re.match(r'^\| [^|:]', l) and not l.startswith('| flat file')]
    rootl = [l for l in ls if l.startswith('Act root: ')]
    zb = open(ZIP, 'rb').read()
    ver = rd('b635_mirror_verify.txt')
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in ver
    prev_md5 = hashlib.md5(zipfile.ZipFile(PREV_ZIP).read('MANIFEST.md')).hexdigest() if os.path.exists(PREV_ZIP) else None
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    head = next((l for l in ls if l.startswith('Source: PLACE-papers @')), '')
    L = ['b635 -- THE MIRROR, BUILT AFTER THE ACT`S LAST PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP (for the author`s upload) : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), hashlib.md5(zb).hexdigest(), hashlib.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; %d bytes ; %d rows ; entries in the zip %d (files %d + MANIFEST)' % (
             hashlib.md5(man).hexdigest(), len(man), len(rows), len(names), len([n for n in names if n != 'MANIFEST.md'])),
         '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SOURCE LINE : %s' % head,
         '### THE PREVIOUS BUILD : %s, MANIFEST md5 %s (the ruling`s figure %s)' % (PREV_ZIP, prev_md5, K.MIRROR_PRIOR_MD5),
         '### THE VERIFICATION (relay data/b635_mirror_verify.txt): %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd),
         '### THE FILE LIST:'] + ['    %s' % n for n in names] + ['### THE MANIFEST, WHOLE:'] + ['    ' + l for l in ls]
    put_txt('b635_mirror.txt', L)
    put_json('b635_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=hashlib.md5(zb).hexdigest(), zip_sha256=hashlib.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=hashlib.md5(man).hexdigest(), rows=len(rows), entries=len(names), root_line=rootl[0] if rootl else '',
                                      prev_manifest_md5=prev_md5, clean=clean, nd=dict(nd), source=head))
    for l in L[:9]:
        print(l[:300])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', K.CEN4, K.CEN5, 'day1/A_Place_to_Stand_v5_18.md', K.SIEVE6)
HKEYS = ('H69a', 'H69b', 'H69c', 'H69d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b634_closing_push_out.txt', 'data/act_roots.txt', 'tools/e0_rule.py', 'tools/test_e0_rule.py', 'tools/terminal_table.py',
              'tools/test_terminal_table_b635.py', 'data/' + ELAB_TYPES, 'data/' + RETIRE, 'data/' + REPOINT}


def n5(trail_line=None, ot=None, *a):
    """### (R245)'s N5, the file-set by PATH; the mirror and its bank; the token unused."""
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
    face = jl('b635_kernels_face.json')['kernels']
    now = kern_state(list(face))
    kern_ok = all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', K.PAGE, K.DIR_PAGE)]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b635_|audit_b635_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    gen_edit = 'tools/terminal_table.py' in relay_ch
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local and not gen_edit
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel`s tracked tree unmoved against the face %s; PLACE-papers %s (beyond the ledgers, README and the pages: '
            '%s); %s; relay beyond the list, matched by path: %s; the generator edited %s (the author`s answer: N5 refuted in letter by it, '
            'its omission the navigator`s); b628`s local intake bank in any relay commit %s, untracked now %s; no call made with the token; no '
            'outbound request carried an identifier' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', gen_edit, tracked_local,
                                                         untracked_local))


def scores(*a):
    AG, PH, MJ, DJ = jx('b635_agree.json'), jx('b635_phantom_names.json'), jx('b635_mirror.json'), jx('b635_deposit_items.json')
    RT, TF, RA = jx('b635_rule_test.json'), jx('b635_table_final.json'), jx('b635_root_arm.json')
    RP = jx('b635_phantom_types.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    ag = AG.get('rows') or []
    a_ok = len(ag) == 11 and all(x['ok'] for x in ag)
    ph = PH.get('names') or []
    b_ok = len(ph) == 13 and all(x['kind'] in ('TRUNCATED -> RE-POINTED', 'UPSTREAM, OUTSIDE THE READER`S IMPORTS') or x.get('entry') for x in ph)
    c_ok = bool(MJ) and MJ.get('root_line', '').startswith('Act root: b635 ') and MJ.get('manifest_md5') != K.MIRROR_PRIOR_MD5
    d_ok = bool(DJ) and DJ.get('all_resolve') is True
    S = {
        'H69a': (('HOLDS' if a_ok else 'REFUTED'), 'the eleven as ruled and agreeing at the rerun: %d of %d (data/b635_agree.txt)' % (
            sum(1 for x in ag if x['ok']), len(ag))),
        'H69b': (('HOLDS' if b_ok else 'REFUTED'), 'the thirteen: %s, none dropped (data/b635_phantom_names.txt)' % dict(
            collections.Counter(x['kind'] for x in ph))),
        'H69c': ((('HOLDS' if c_ok else 'REFUTED') if MJ else 'PENDING'), ('the MANIFEST carries %r ; its md5 %s against the 2026-10-04 '
                 'build`s %s' % (MJ.get('root_line'), MJ.get('manifest_md5'), K.MIRROR_PRIOR_MD5)) if MJ else
                 'the mirror is built after the act`s last push; scored at the closing from data/b635_mirror.json'),
        'H69d': (('HOLDS' if d_ok else 'REFUTED'), 'items resolving %s of %s, tags %s of %s' % (
            sum(1 for x in DJ.get('items') or [] if x['ok']), len(DJ.get('items') or []), sum(1 for x in DJ.get('tags') or [] if x['ok']),
            len(DJ.get('tags') or []))),
        'N1': (('HELD' if a_ok else 'REFUTED'), 'as H69a'),
        'N2': (('HELD' if b_ok else 'REFUTED'), 'as H69b, by its letter: a resolution line or a correction entry each'),
        'N3': ((('HELD' if MJ.get('root_line', '').startswith('Act root: b635 ') and MJ.get('manifest_md5') != K.MIRROR_PRIOR_MD5 else 'REFUTED')
                if MJ else 'PENDING'),
               ('the root line %s ; 20ed9b05… is the 2026-10-04 MANIFEST`s md5 (the ruling`s H69c), compared with this MANIFEST`s %s; the zip`s md5 %s' % (
                   bool(MJ.get('root_line')), MJ.get('manifest_md5'), MJ.get('zip_md5'))) if MJ else 'as H69c: scored at the closing'),
        'N4': (('HELD' if d_ok and not any((DJ.get('nd') or {}).values()) else 'REFUTED'), 'every item resolving %s ; the no-disclosure arm %s' % (
            d_ok, DJ.get('nd'))),
        'N5': n5v,
        'S1': (('HELD' if RT and RT.get('rc') == 0 and RT.get('passing') == RT.get('cases') and RT.get('cases', 0) >= 26 else 'REFUTED'),
               'the rule`s test %s of %s, its old 23 cases kept' % (RT.get('passing'), RT.get('cases'))),
        'S2': (('HELD' if RP and RP.get('typed') == RP.get('of') else 'REFUTED'), 'the re-pointed full names typed by the reader: %s of %s' % (
            RP.get('typed'), RP.get('of'))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': ((('HELD' if MJ.get('clean') else 'REFUTED') if MJ else 'PENDING'), ('the mirror verifies on all three clauses %s' % MJ.get('clean'))
               if MJ else 'scored at the closing from the mirror`s verification'),
        'S5': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
    }
    put_json('b635_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b635 — lane three, act sixty-two under (R245): the twelve disagreements ruled for the elaborated reading and the textual '
              'rule repaired; the thirteen phantom names resolved; the cascade rebuilt; the mirror refreshed with the root line; the '
              'deposit description’s items banked, nothing deposited')


def _figures():
    TA, PH = jl('b635_table_elab.json'), jl('b635_phantom_names.json')
    k = len(TA.get('grade_moved') or [])
    c = collections.Counter(x['kind'] for x in PH['names'])
    return k, c.get('TRUNCATED -> RE-POINTED', 0), c.get('EXISTS NOWHERE', 0), TA, PH


def _title_entry():
    k, r_, c_, _ta, _ph = _figures()
    return ('## The elaborated reading applied to %d rows of SIDE-explicit-formula and the textual rule repaired on three patterns; %d '
            're-pointed and %d retired table names; the mirror at %s with the b635 root; the deposit description’s items banked, nothing '
            'deposited' % (k, r_, c_ + 1, DATE))


def _finding_text():
    S, rl, J = jl('b635_scores.json'), jl('b635_record_lines.json'), jl('b635_act_root.json')
    k, r_, c_, TA, PH = _figures()
    DJ, RM = jl('b635_deposit_items.json'), jl('b635_readme.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b635_author_answers.txt'), re.M))
    t = _title_entry()
    up = dict(upstream=sum(1 for r in _table() if r.get('mark') == 'upstream'))
    e = ['', t, '',
         '*Filed at b635 on the author’s ruling `(R245)` and the author’s %d answers, two before the seal and two after. Banks: relay `data/b635_twelve.txt`, '
         '`data/b635_agree.txt`, `data/b635_table_elab.txt`, `data/b635_phantom_names.txt`, `data/b635_deposit_items.txt`, '
         '`data/b635_act_root.txt`. Nothing deposits.*' % n_ans, '',
         '**The twelve** (`(R245)`(2)): ruled for the elaborated reading -- the eight chi_* rows by type_of%%, ZerosBound by its binder nested two '
         'deep, the paperFT_growth pair by the qualified Integrable, the row named Finset retired as naming no declaration. The textual rule '
         'repaired on three patterns with a test case each (type_of%% deferred to the elaborated type, nested binders, qualified class names); '
         'the generator, by the author’s answer, grades the kernel’s rows without a ledger cell from the elaborated types, provenance '
         '“rule-elab” where the elaborated grade differs from the textual or the textual defers. %d rows moved, the 35 statement-less rows the '
         'reader types among them (%s rows of the table marked upstream); H69a %s.' % (k, up.get('upstream', '?'), S['H69a'][0]), '',
         '**The thirteen** (`(R245)`(3)): %s -- the twelve truncated each the head of a name the kernel’s `#print axioms` lines print, the table’s name pattern '
         'stopping at its first non-ASCII character; re-pointed old → new by the generator’s map, each citing its print line and commit; '
         'none exists nowhere; H69b %s.' % (dict(collections.Counter(x['kind'].replace('`', '’') for x in PH['names'])), S['H69b'][0]), '',
         '**The cascade** (`(R245)`(4)): SaltCheckDoubling and Schema/SaltCheckFamily rebuilt by lake under the hold, 7 constants and 0 '
         'differences, lake reading every target up to date.', '',
         '**README** (`(R245)`(5)(ii)): the supportable paragraph for v0.22–v0.25 appended at :%d, the not-supportable sentence unchanged.' % RM.get('line', 0), '',
         '**The pages:** both re-emitted from b632’s lists and a fresh probe each, by the author’s answer after the seal; the page '
         'printer, by a second answer, marks a row at any provenance but the cells’ as itself; the χ page’s Correspondence moves '
         '%d cells; both page arms pass (relay data/b635_page_chi.json, data/b635_page_arms.txt).' % len(jl('b635_page_chi.json')['cells_moved']), '',
         '**The deposit items** (`(R245)`(5)(ii)-(iv)): %d of %d items and %d of %d kernel tags resolving at their remotes, the one '
         'unresolved pair a prose version target the tag matcher read as a tag (relay data/b635_deposit_tag_residue.txt); the '
         'no-disclosure arm at 0; the token located and unused; nothing deposits. H69d %s in letter.' % (
             sum(x['ok'] for x in DJ['items']), len(DJ['items']), sum(x['ok'] for x in DJ['tags']), len(DJ['tags']), S['H69d'][0]), '',
         '**The record lines** (`(R245)`(1)): b634 at its weight (FINDINGS :%d); rule 14’s capture for an as-of refusal, standing '
         '(OPEN_TRAILS :%d).' % tuple(x['line'] for x in rl['lines']), '',
         '**The root.** b635 over %d repositories, %d tags and %d banks; its chain verified inside the suite; the mirror carries its line.' % (
             len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b634’s twelve disagreements and thirteen names (FINDINGS :7747) and '
         'b632’s rule grades (FINDINGS :7701), whose kernel rows it grades a second time from Lean’s own types; b633’s census (FINDINGS '
         ':7725), whose head it banks for the deposit. It strengthens the programme’s offering of a table whose grades name what Lean '
         'elaborated and whose every row names a declaration that exists.', '',
         '**Next.** Per `(R245)`(6): b636 on the author’s word -- the deposit, the author’s own act; or W-ORD-BINDER-GRAMMAR with the 20 '
         'unnamed rows as its test set; or the elaborated reader over SIDE-structural-error-correction.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


def _next_lines():
    return ['b636 names no kernel terminal; the deposit is the author’s own act, W-ORD-BINDER-GRAMMAR’s test set is the 20 unnamed rows, and '
            'the elaborated reader over SIDE-structural-error-correction reads that kernel’s rows when ruled']


FOR_AUTHOR = ('(1) the thirteen read as truncations by the table’s ASCII name pattern and re-pointed, not as renames, the one upstream name '
              'typed from its Mathlib module; the pattern itself left for the author’s word; (2) the ruled grade of the paperFT_growth pair '
              'DERIVES, the cell grade unmoved; (3) “rule-elab” where the elaborated grade differs from the repaired textual reading or the '
              'textual defers, “rule” where they agree; (4) the upstream mark a field beside the grade, a module outside the kernel’s roots; '
              '(5) the root chain item read at the bank’s writing, b635’s own line in the record and the MANIFEST; (6) the README sentence '
              'the seat’s, for the author’s strike')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b635_scores.json', 'b635_findings.json', 'b635_record_lines.json', 'b635_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b635_author_answers.txt'), re.M))
    MJ = jx('b635_mirror.json')
    rows_ = ['', TRAIL_HEAD, '',
             '**(R245) ratified.** (1) b634 at its weight. (2) The twelve ruled for the elaborated reading. (3) The thirteen resolved. (4) The '
             'cascade rebuilt. (5) The deposit preparations. (6) The act after: b636.', '',
             '**Entered:** FINDINGS.md:%d (b634’s weight), :%d (the entry); OPEN_TRAILS.md:%d (rule 14’s capture, standing); this record; '
             'README.md :%d.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], jl('b635_readme.json')['line']), '',
             '**Act root:** b635 `%s` (previous `%s`, b634’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b635_author_answers.txt).' % n_ans, '',
             '**The mirror:** built after the last push; its zip and MANIFEST digests in relay data/b635_mirror.txt, banked at the closing%s.' % (
                 '' if not MJ else ''), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b635_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, S[k2][0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R245)`(6), b636 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b635_scores.json')
    L = ['=' * 104, 'b635 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H69a-H69d, (R245)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0] == 'HOLDS' for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0] == 'HELD' for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0] == 'HELD' for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b635_defects.txt').rstrip(NL).split(NL)
    put_txt('b635_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b635_scores.json', 'b635_findings.json', 'b635_trail.json', 'b635_record_lines.json', 'b635_act_root.json'))
    L = ['b635 -- THE COMPONENTS, BANKED UNDER (R245).', '',
         '### COMPONENT 0 : the process listing ; b634`s closing push-out relay %s ; push-b634* deleted by name (data/b635_branches.txt) ; the cascade '
         'rebuilt (data/b635_rebuild.txt, data/b635_kernel_clean.txt) ; every test file run (data/b635_tests_stepzero.txt) ; the suite at HEAD before '
         'the face (data/b635_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b634`s weight FINDINGS :%d ; rule 14`s capture :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the twelve (data/b635_twelve.txt) ; the rule repaired (data/b635_rule_diff.txt, data/b635_rule_test.txt) ; the generator '
         '(data/b635_gen_diff.txt, data/b635_gen_test.txt) ; the table (data/b635_table_elab.txt) ; the rerun (data/b635_agree.txt) ; H69a %s' % S['H69a'][0],
         '### COMPONENT 3 : data/b635_phantom_names.txt ; the table (data/b635_table_phantom.txt) ; H69b %s' % S['H69b'][0],
         '### COMPONENT 4 : the pages (data/b635_page_zeta.json, data/b635_page_chi.json) ; README :%d ; page arms data/b635_page_arms.txt' % jl('b635_readme.json')['line'],
         '### COMPONENT 5 : data/b635_deposit_items.txt ; H69d %s' % S['H69d'][0],
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; the root %s' % (fj['entry_line'], tj['line'], J['root'][:16]),
         '### COMPONENT 7 : the mirror (data/b635_mirror.txt) ; H69c %s ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             S['H69c'][0], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b635_components.txt', L)


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
    put_json('b635_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
    put_json('b635_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b635_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-07 by b635 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b635_defects.json -- NOTHING WRITTEN')
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
    put_json('b635_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b635_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
