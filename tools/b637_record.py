# -*- coding: utf-8 -*-
"""b637_record.py -- THE ACT'S RECORD TOOL, UNDER (R247). ### ONE SUBCOMMAND PER BANK.

### ### b637: LANE THREE, ACT SIXTY-FOUR -- THE BINDER GRAMMAR: THE E0 RULE AS A TOTAL FUNCTION OVER A FINITE CLASSIFICATION, NAMES REMOVED
### FROM THE READING, BOTH READERS RERUN OVER BOTH KERNELS, THE 20 UNNAMED ROWS READ BY CLASS; UPSTREAM ROWS AS KIND; THE MIRROR'S ROSTER.
### Subcommands write only `data/b637_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic
### helpers are b633's record tool's, imported; ledger appends through b566's guarded `append_to`. The data is tools/b637_worklist.py;
### the rule is tools/e0_rule.py, rewritten at Component 3; the generator tools/terminal_table.py, edited at Component 5. No platform is
### called; no registry is read; nothing deposits. b628's full intake bank is never read here, never staged or committed. A stand-in bank
### directory named by the environment variable B637_STANDIN is read before data/ by the record texts' dry runs alone.
"""
import collections
import copy
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b637_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = '22cdf84c-42e5-4b4d-b777-6c6a90fcc03e'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b637_registration_2026-10-07.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_txt, put_json, _write, _scan, _clean = R3.put_txt, R3.put_json, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
KERNS, KERN_PIN, kern_state, sorry_tokens = R3.KERNS, R3.KERN_PIN, R3.kern_state, R3.sorry_tokens
STANDIN = os.environ.get('B637_STANDIN') if ('dry' in sys.argv[2:]) else None


def _bank_path(name):
    if STANDIN and os.path.exists(os.path.join(STANDIN, name)):
        return os.path.join(STANDIN, name)
    return os.path.join(D, name)


def jl(name):
    try:
        return json.load(io.open(_bank_path(name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    try:
        return io.open(_bank_path(name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b637_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b637 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b637_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b637_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table(rev=None):
    if rev:
        return json.loads(subprocess.run(['git', '-C', ROOT, 'show', '%s:data/terminal_table.json' % rev], capture_output=True).stdout.decode('utf-8'))['rows']
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b637 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def _diff(path, rev, bank, title):
    old = (_show(RELAY, rev, path) or '').split(NL)
    new = io.open(os.path.join(ROOT, *path.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, '%s@%s' % (os.path.basename(path), rev), os.path.basename(path), lineterm='', n=0))
    put_txt(bank, ['b637 -- %s, THE DIFF AGAINST relay %s (%s)' % (title, rev, utc()), '',
                   '### lines removed %d ; added %d' % (sum(1 for x in dl if x[:1] == '-' and not x.startswith('---')),
                                                        sum(1 for x in dl if x[:1] == '+' and not x.startswith('+++'))), ''] + dl)


# ================================================================================ READING (1): THE READS
def READS():
    EFp = K.KERNELS[K.EF_KERNEL]
    return [
        ('OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, the criterion and PREDICATE-UNLISTED beneath it, the lines the ferry names, b636`s record and its '
         'correction, the seal rule', PP, PRE_PP, 'OPEN_TRAILS.md', [K.BINDER_GRAMMAR, K.CRITERION, K.UNLISTED_LINE, K.SEAL_RULE, K.B636_RECORD]
         + list(K.FERRY_LINES), 1800),
        ('FINDINGS: b636`s weight line on b635 and b636`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B636_WEIGHT_PRIOR, K.B636_ENTRY], 600),
        ('relay tools/e0_rule.py after b636: the h-prefix test, the criterion`s clauses, the named lists, MET, grade()', RELAY, PRE_RELAY,
         'tools/e0_rule.py', ('GREP', r"^(BINDER = |DOMAIN = |SPLITS = |CLASS_PREDS = |INSTANCE = |CLASS_PREDS_B625 = |SUPPORT = |RESTRICTIONS = |"
                                    r"MET = |NAMED_PRED = |DATA_ATOM = |DATA_TYPE = |SEAMS = |def \w+)"), 220),
        ('relay tools/test_e0_rule.py: its cases', RELAY, PRE_RELAY, 'tools/test_e0_rule.py', ('GREP', r'^###   \(\d+\)'), 200),
        ('relay data/b634_elab_types.txt (the ferry`s explicit-formula bank): its head', RELAY, PRE_RELAY, 'data/b634_elab_types.txt', [1, 3, 4], 220),
        ('relay data/elab_types.txt (the bank the generator reads, terminal_table.py ELAB_TYPES): its head', RELAY, PRE_RELAY, 'data/elab_types.txt',
         [1, 2, 3], 220),
        ('relay data/b636_elab_sec.txt: its head', RELAY, PRE_RELAY, 'data/b636_elab_sec.txt', [1, 3, 4], 220),
        ('relay data/b634_unnamed_rows.txt: the 20', RELAY, PRE_RELAY, 'data/b634_unnamed_rows.txt', ('GREP', r'^  U\d\d |^### ### '), 220),
        ('relay data/terminal_table.json at f3a2f6b2: grades and provenance by kernel', RELAY, PRE_RELAY, 'data/terminal_table.json', ('TABLE', None), 300),
        ('PLACE-papers the census at v0.5: the 42 named premises, their table and notes', PP, PRE_PP, K.CEN5,
         list(range(K.CEN5_PREMISES[0], K.CEN5_PREMISES[1] + 1)), 260),
        ('relay tools/mirror_roster.json: the roster the builder reads (git grep for the roster`s file names)', RELAY, PRE_RELAY, K.ROSTER,
         ('GREP', r'A_Place_to_Stand_v5|FINDINGS_AS_THEY_STAND|KEYSTONE_CENSUS|lastChanged'), 220),
        ('relay tools/mirror_build.ps1: the roster read (the builder, unedited by (R96))', RELAY, PRE_RELAY, K.BUILDER,
         ('GREP', r'mirror_roster\.json|ROSTER'), 200),
        ('relay tools/terminal_table.py: the elaborated reading, the provenance and the upstream mark', RELAY, PRE_RELAY, 'tools/terminal_table.py',
         ('GREP', r"^(ELAB_KERNEL|ELAB_TYPES|ELAB_BANKS|ELAB_ROOTS|KERNEL_ROOTS) = |r\['mark'\] = 'upstream'|^def (provenance|rule_reading|elab_reading)"), 220),
        ('relay data/b636_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b636_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
        ('relay data/b636_closing_push_out_attempt1.txt (committed at step zero)', RELAY, STEPZERO, 'data/b636_closing_push_out_attempt1.txt',
         ('GREP', r'.'), 200),
    ]


def _binderinfo():
    """### Lean's BinderInfo constructors, by git grep in each toolchain's Lean sources (--no-index: a toolchain is no repository)."""
    out = []
    for kern, tc in sorted(K.TOOLCHAINS.items()):
        r = subprocess.run(['git', 'grep', '--no-index', '-n', '-E', r'^inductive BinderInfo|^  \| (default|implicit|strictImplicit|instImplicit)$',
                            '--', K.BINDERINFO_FILE], capture_output=True, cwd=tc)
        ls = r.stdout.decode('utf-8', 'replace').replace(chr(13), '').strip().split(NL)
        out.append((kern, tc, [l for l in ls if l.strip()]))
    return out


def reads(*a):
    L = ['b637 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'TABLE':
            rows = json.loads(t).get('rows', [])
            c = collections.Counter((r['repo'], r['grade'], r.get('provenance')) for r in rows)
            L.append('### %s -- %s @ %s (%d rows; by kernel, grade and provenance:)' % (label, path, at, len(rows)))
            for k_, n_ in sorted(c.items(), key=lambda x: (x[0][0], -x[1])):
                L.append('    %-34s %-22s %-10s %d' % (k_[0], k_[1], k_[2], n_))
            continue
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### LEAN`S BINDER KINDS, git grep --no-index in each toolchain`s Lean sources:']
    for kern, tc, ls in _binderinfo():
        L.append('  %s -- %s/%s:' % (kern, tc, K.BINDERINFO_FILE))
        L += ['    ' + l for l in ls] or ['    ### NO SUCH LINE']
    import terminal_table as TT
    a, b = TT.elab_bank(os.path.join(D, 'b634_elab_types.txt')), TT.elab_bank(os.path.join(D, 'elab_types.txt'))
    same = sum(1 for n in a if n in b and (a[n]['binders'], a[n]['concl'], a[n]['kind']) == (b[n]['binders'], b[n]['concl'], b[n]['kind']))
    L += ['', '### THE EXPLICIT-FORMULA BANKS: the ferry names data/b634_elab_types.txt, the generator reads data/elab_types.txt (ELAB_TYPES): '
          'b634`s bank %d declarations, the generator`s %d; every b634 declaration in the generator`s bank with an identical block %d of %d; the '
          'generator`s own %d (b635`s resolved names). The rerun reads the generator`s.' % (len(a), len(b), same, len(a), len(set(b) - set(a))),
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b637_reads.txt', L)


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R247) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b637 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b637_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b637_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b637_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE SEAL'S HASHES ((R246)(3), OPEN_TRAILS :13307)
def seal_hashes():
    rec_ = jl('b637_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b637 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b637_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES AND THE ROSTER
W_HEAD = '*Appended 2026-10-07 by b637 to b636’s entry (:%d), under `(R247)`(1) -- b636 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
UP_HEAD = ('*Appended 2026-10-07 by b637 beneath the domain-condition criterion (:%d), under `(R247)`(2) -- UPSTREAM ROWS A KIND AND NOT A '
           'GRADE, STANDING:*')
NM_HEAD = ('*Appended 2026-10-07 by b637 beneath the domain-condition criterion (:%d), under `(R247)`(3) -- A BINDER’S NAME NO PART OF ITS '
           'READING, STANDING:*')


def _weight():
    TR, SC, SH, P2 = jl('b636_two_readings_sec.json'), jl('b636_scores.json'), jl('b636_seal_hashes.json'), jl('b636_phase2_read.json')
    AR, TB = jl('b636_act_root.json'), jl('b636_table_sec.json')
    chk = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b636_checks.txt'))
    held = [k for k in ('H70a', 'H70b', 'H70c', 'H70d') if (SC.get(k) or [''])[0] == 'HOLDS']
    nk = [k for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5') if (SC.get(k) or [''])[0] == 'HELD']
    return ('\n%s SIDE-structural-error-correction at v0.2.2 = 6bf19ab read by the generalised reader, the textual and elaborated readings '
            'agreeing on %d of %d declarations with a statement, the remaining one without a statement; %d of its rows at provenance rule-elab; the '
            'Phase 2 rows re-read, %d triggers; the name patterns reading Lean identifiers whole and the tag matcher reading the REGISTRY’s tag '
            'form alone; the seal’s hash arm recording %d sealed tools and comparing them, each agreeing; %d of 4 hypotheses holding (H70c '
            'vacuously, zero disagreements), %d of 10 expectations held; the suite %s of %s. The closing push’s first refusal kept as relay '
            'data/b636_closing_push_out_attempt1.txt by rule 14, the second push succeeding; the as-of line at OPEN_TRAILS :%d. The seat’s three '
            'readings confirmed by the author: the tag form as repaired; the plain requests to github.com read as the ls-remote reads and the '
            'pushes; the sealed set as the seat listed it. The mirror mirror-refresh-2026-10-07.zip verified by the navigator (md5 76d0eab9…, '
            'sha256 3cb13712…, MANIFEST md5 3691017f…, its root line at :81) and the project refreshed from it. Root b636 %s…%s; relay '
            'fb177036 and closing f3a2f6b2, PLACE-papers e70e044 and 142c315. Nothing deposited; no kernel source touched.\n'
            % (W_HEAD % K.B636_ENTRY, TR.get('agree', 0), TR.get('both', 0), TB.get('sec_rule_elab', 0), len(P2.get('triggers') or []),
               len(SH.get('tools') or {}), len(held), len(nk), chk.group(2) if chk else '?', chk.group(1) if chk else '?', K.B636_CORRECTION,
               (AR.get('root') or '?')[:8], (AR.get('root') or '????')[-4:]))


def _upstream_clause():
    return ('\n%s a row of the terminal table whose declaration lives outside every kernel -- the rows the upstream mark reaches, and the five '
            'Mathlib names the widened name patterns brought in, riemannZeta₀ among them -- is a kind and not a terminal: its grade cell reads '
            '— with the kind upstream, its provenance none, and it is excluded from every grade count the census and the deposit bank print; '
            'the generator prints its counts before and after the exclusion. The programme grades what its kernels state; Mathlib’s theorems '
            'are cited, not graded. Entered by b637 as the author’s ruling words it; the generator’s edit and its test in relay.\n' % (UP_HEAD % K.CRITERION))


def _name_clause():
    return ('\n%s the textual rule read a hypothesis binder when its name began with h and not otherwise, which is how chi_Tail’s H : TailHyp '
            'escaped it. A binder’s name is no part of its reading: the criterion is a function of the binder’s kind (explicit, implicit, '
            'instance, strict-implicit), its type (a Prop or data), the Prop’s form (a structure of premises about a fixed object; a named '
            'predicate restricting a variable the same statement quantifies; a membership, non-membership, finiteness or non-emptiness '
            'condition; a seam antecedent; the conclusion itself) and the MET list (:%d) -- and of nothing the author typed as a name. This is '
            'the clause W-ORD-BINDER-GRAMMAR (:%d) compiles; the classification and the rule rewritten over it in relay.\n'
            % (NM_HEAD % K.CRITERION, K.UNLISTED_LINE, K.BINDER_GRAMMAR))


def record_lines(*a):
    """### FINDINGS: b636's weight (to :7801). OPEN_TRAILS: the upstream clause and the name clause beneath the criterion (:12955)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The elaborated reader over SIDE-structural-error-correction at v0.2.2: ')
    if entry != K.B636_ENTRY:
        sys.exit('### b636`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B636_ENTRY, _weight()), ('OPEN_TRAILS.md', UP_HEAD % K.CRITERION, _upstream_clause()),
             ('OPEN_TRAILS.md', NM_HEAD % K.CRITERION, _name_clause())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(''.join(t for f, _h, t in items if f == 'OPEN_TRAILS.md'), 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
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
    _land(Q, items, 'b637_record_lines.json', K.B636_ENTRY)


def roster(*a):
    """### (R247)(5): the roster's diff against relay f3a2f6b2 and the builder's blob against it, read after the seat's Edit (data/b637_roster.txt)."""
    old = json.loads(_show(RELAY, PRE_RELAY, K.ROSTER))
    new = json.load(io.open(os.path.join(ROOT, *K.ROSTER.split('/')), encoding='utf-8'))
    of, nf = old['files'], new['files']
    added = nf[len(of):] if nf[:len(of)] == of else None
    exists = [(f, os.path.exists(os.path.join(PP, *f.split('\\')))) for f in (added or [])]
    tracked = [(f, bool(g(PP, 'ls-files', '--', f.replace('\\', '/')).strip())) for f in (added or [])]
    bld = g(RELAY, 'diff', '--name-only', PRE_RELAY, '--', K.BUILDER).strip() + g(RELAY, 'diff', '--name-only', '--', K.BUILDER).strip()
    L = ['b637 -- (R247)(5): THE MIRROR`S ROSTER, READ AFTER THE EDIT (%s)' % utc(), '',
         '### files before %d ; after %d ; the old list a prefix of the new %s (no slot moves) ; appended %s' % (len(of), len(nf), added is not None, added),
         '### each appended file present in PLACE-papers %s ; tracked %s' % (exists, tracked),
         '### the superseded versioned files kept: %s' % [f for f in of if re.search(r'A_Place_to_Stand_v5_17|FINDINGS_AS_THEY_STAND_v0_4|KEYSTONE_CENSUS_v0_3', f)],
         '### lastChanged %s -> %s ; _history %s' % (old.get('lastChanged'), new.get('lastChanged'), 'changed' if old.get('_history') != new.get('_history') else 'unchanged'),
         '### the builder tools/mirror_build.ps1 against f3a2f6b2 and on disk: %s' % ('### EDITED' if bld else 'unedited'),
         '', '### ### **ROSTER %d -> %d FILES ; APPENDED %d, EACH TRACKED %s ; BUILDER %s.**' % (
             len(of), len(nf), len(added or []), all(t for _f, t in tracked) if tracked else False, 'EDITED' if bld else 'UNEDITED')]
    put_txt('b637_roster.txt', L)
    put_json('b637_roster.json', dict(at=utc(), before=len(of), after=len(nf), appended=added, prefix=added is not None,
                                      tracked=dict(tracked), builder_edited=bool(bld), last_changed=[old.get('lastChanged'), new.get('lastChanged')]))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE CLASSIFICATION
# ### (R247)(4)(i): the classes, kind × typing × form, each with its outcome -- fixed here, in the act's record tool, before the rule is
# ### rewritten; the rule's own CLASSES list is tested against this bank at Component 3.
FORMS = (('itself', 'the conclusion itself', 'conclusion'),
         ('domain', 'a membership, non-membership, non-emptiness, finiteness, order or (in)equality condition, a listed property or a '
                    'compiled split`s case (criterion (ii); DOMAIN, SPLITS)', 'domain condition'),
         ('restriction', 'a restriction on a variable the statement quantifies -- a class predicate, a support inclusion or a named '
                         'restriction (criterion (iii); RESTRICTIONS)', 'domain condition'),
         ('unlisted', 'a named predicate on quantified variables, neither listed nor met (PREDICATE-UNLISTED; MET)', 'unlisted'),
         ('met', 'a named predicate on quantified variables that MET holds -- the forward guard (OPEN_TRAILS :13221), a premise until '
                 'the author rules the name a restriction', 'premise'),
         ('premise', 'any other Prop: a structure of premises or a named Prop about a fixed object', 'premise'))
NF = len(FORMS)
CLASSES = ([('B01', 'explicit', 'data', '—', 'data'), ('B02', 'implicit', 'data', '—', 'data'), ('B03', 'strict-implicit', 'data', '—', 'data'),
            ('B04', 'instance', 'a class', 'Fact', 'premise'), ('B05', 'instance', 'a class', 'any class but Fact (criterion (i))', 'domain condition')]
           + [('B%02d' % (6 + NF * i + j), k, 'Prop', f[1], f[2]) for i, k in enumerate(('explicit', 'implicit', 'strict-implicit'))
              for j, f in enumerate(FORMS)]
           + [('B%02d' % (6 + 3 * NF), 'antecedent', 'Prop', 'a seam (SEAMS)', 'seam'),
              ('B%02d' % (7 + 3 * NF), 'antecedent', 'Prop', 'any other antecedent: a plain implication between open statements, a domain '
                                                               'antecedent', 'conclusion'),
              ('B%02d' % (8 + 3 * NF), 'existential', 'any', 'a binder of an existential in the conclusion', 'conclusion')])
FIVE_CLS = 'B%02d' % (6 + [f[0] for f in FORMS].index('premise'))     # ### an explicit Prop binder whose form is a premise

# ### one planted declaration per class: (class, the binder under test, the declaration's text, the grade the rule must read). The binder
# ### under test is never named h; the five-name test plants one hypothesis under five names.
_PROP = {'itself': ('(n : Nat) %s : ∀ m : Nat, m + n = n + m := c', '∀ k : Nat, k + n = n + k', 'ENCODES-CONCLUSION'),
         'domain': ('(n : Nat) %s : n = n := rfl', '0 < n', 'DERIVES'),
         'restriction': ('(f : ℝ → ℝ) %s : f = f := rfl', 'Continuous f', 'DERIVES'),
         'unlisted': ('(f : ℕ → ℂ) (s : ℂ) %s : f = f ∧ s = s := ⟨rfl, rfl⟩', 'LSeriesSummable f s', 'PREDICATE-UNLISTED'),
         'met': ('(f : ℝ → ℝ) %s : f = f := rfl', 'Monotone f', 'INTERFACES'),
         'premise': ('%s : True := trivial', 'NontrivialZeroExistsInStrip', 'INTERFACES')}
_BR = {'explicit': '(c : %s)', 'implicit': '{c : %s}', 'strict-implicit': '⦃c : %s⦄'}


def planted():
    """### RETURN [(class, binder, decl name, text, grade)] -- one declaration per class, the five-name test and the no-class control."""
    out = [('B01', 'n', 'b01', 'theorem b01 (n : Nat) : n = n := rfl', 'DERIVES'),
           ('B02', 'n', 'b02', 'theorem b02 {n : Nat} : n = n := rfl', 'DERIVES'),
           ('B03', 'n', 'b03', 'theorem b03 ⦃n : Nat⦄ : n = n := rfl', 'DERIVES'),
           ('B04', 'c', 'b04', 'theorem b04 (p : Nat) [c : Fact (Nat.Prime p)] : p = p := rfl', 'INTERFACES'),
           ('B05', '', 'b05', 'theorem b05 (N : Nat) [NeZero N] : N = N := rfl', 'DERIVES')]
    for i, k in enumerate(('explicit', 'implicit', 'strict-implicit')):
        for j, f in enumerate(FORMS):
            cid = 'B%02d' % (6 + NF * i + j)
            tpl, ty, gr = _PROP[f[0]]
            out.append((cid, 'c', cid.lower(), 'theorem %s %s' % (cid.lower(), tpl % (_BR[k] % ty)), gr))
    out += [('B%02d' % (6 + 3 * NF), '→', 'b%02d' % (6 + 3 * NF), 'theorem b%02d : rh_strip_imp_rh → True := fun _ => trivial' % (6 + 3 * NF), 'INTERFACES'),
            ('B%02d' % (7 + 3 * NF), '→', 'b%02d' % (7 + 3 * NF), 'theorem b%02d (n : Nat) : 0 < n → n ≠ 0 := Nat.pos_iff_ne_zero.mp' % (7 + 3 * NF), 'DERIVES'),
            ('B%02d' % (8 + 3 * NF), 'c', 'b%02d' % (8 + 3 * NF), 'theorem b%02d : ∃ (n : Nat) (c : 0 < n), n = 1 := ⟨1, Nat.one_pos, rfl⟩' % (8 + 3 * NF), 'DERIVES')]
    names = {'h': 'h', 'H': 'H', 'hyp': 'hyp', 'x': 'x', 'ξ': 'xi'}
    for nm in K.FIVE_NAMES:
        out.append(('FIVE', nm, 'five_%s' % names[nm], 'theorem five_%s (%s : NontrivialZeroExistsInStrip) : True := trivial' % (names[nm], nm), 'INTERFACES'))
    out.append(('NONE', 'c', 'noclass', 'theorem noclass (c : SomeUndeclaredBareName) : True := trivial', 'NO CLASS'))
    return out


PLANTED_FILE = 'B637Planted.lean'


def planted_text():
    p = planted()
    body = ['-- b637 planted module (relay tools/b637_record.py classes, (R247)(4)(i)): one declaration per binder class, the five-name test and',
            '-- the no-class control. Read by the rule as text, never built. Each declaration`s expected class and grade is fixed in relay',
            '-- data/b637_binder_classes.json before the rule reads it.', 'namespace PlantedB637', '']
    for cid, b, dn, txt, gr in p:
        body += ['-- %s : binder %s ; the grade the rule must read: %s' % (cid, b or '[inst]', gr), txt, '']
    return NL.join(body + ['end PlantedB637', ''])


def classes(*a):
    """### Component 2: Lean's binder kinds printed from the toolchains' sources; the class table with its outcomes; one planted declaration
    ### per class written under the scratchpad with its expected class and grade fixed in data/b637_binder_classes.txt and its json BEFORE any
    ### reading -- this subcommand imports no rule and reads no planted declaration."""
    assert 'e0_rule' not in sys.modules, 'the rule must not be read here'
    text = planted_text()
    b = text.encode('utf-8')
    os.makedirs(K.PLANTED_DIR, exist_ok=True)
    pth = os.path.join(K.PLANTED_DIR, PLANTED_FILE)
    if not DRY:
        _write(pth, b)
    L = ['b637 -- COMPONENT 2, (R247)(4)(i): THE BINDER CLASSIFICATION -- KIND × TYPING × FORM, EACH CLASS WITH ITS OUTCOME; ONE PLANTED '
         'DECLARATION PER CLASS, ITS EXPECTED CLASS AND GRADE FIXED HERE BEFORE THE RULE READS IT (%s)' % utc(), '',
         '### LEAN`S BINDER KINDS (BinderInfo), git grep --no-index in each toolchain`s Lean sources:']
    for kern, tc, ls in _binderinfo():
        L.append('  %s -- %s/%s:' % (kern, tc, K.BINDERINFO_FILE))
        L += ['    ' + l for l in ls]
    L += ['### the grammar`s kinds: the four Lean kinds of a header binder or of the conclusion`s leading telescope (default read as explicit), '
          'and two positions in the conclusion -- the antecedent of its top-level implication, a binder of an existential in it. An auto-bound '
          'implicit and a section variable reach the elaborated header as implicit or explicit binders and take those kinds there; the textual '
          'header does not carry them.', '',
          '### THE CLASSES (%d):' % len(CLASSES), '  | class | kind | typing | form | outcome | its grade effect |', '  |:--|:--|:--|:--|:--|:--|']
    for cid, kind, typ, form, out in CLASSES:
        eff = {'data': 'none: an object', 'domain condition': 'none: a domain condition', 'premise': 'INTERFACES', 'seam': 'INTERFACES',
               'unlisted': 'PREDICATE-UNLISTED', 'conclusion': ('ENCODES-CONCLUSION' if form == 'the conclusion itself' else 'none: part of the conclusion')}[out]
        L.append('  | %s | %s | %s | %s | %s | %s |' % (cid, kind, typ, form, out, eff))
    L += ['', '### THE GRADE: a binder in a class whose form is the conclusion itself -- ENCODES-CONCLUSION; else one whose outcome is unlisted -- '
          'PREDICATE-UNLISTED; else one whose outcome is premise or seam -- INTERFACES; else DERIVES; a definition DEF; a type_of% conclusion '
          'DEFERRED. A binder that reaches no class is a bug of the grammar, printed as such, and no grade.', '',
          '### THE PLANTED DECLARATIONS, %s (%d bytes, sha256 %s), written before any reading:' % (pth.replace('\\', '/'), len(b), sha(b))]
    P = planted()
    for cid, bn, dn, txt, gr in P:
        L.append('  %-5s binder %-6s expected class %-5s grade %-20s %s' % (cid, bn or '[inst]', cid if cid.startswith('B') else (FIVE_CLS if cid == 'FIVE' else 'NONE'),
                                                                         gr, txt))
    L += ['', '### ### **CLASSES %d ; PLANTED DECLARATIONS %d (one per class %d, the five-name test %d, the no-class control 1) ; EXPECTATIONS FIXED '
          'BEFORE ANY READING.**' % (len(CLASSES), len(P), sum(1 for x in P if x[0].startswith('B')), sum(1 for x in P if x[0] == 'FIVE'))]
    put_txt('b637_binder_classes.txt', L)
    put_json('b637_binder_classes.json', dict(at=utc(), classes=[dict(id=c[0], kind=c[1], typing=c[2], form=c[3], outcome=c[4]) for c in CLASSES],
                                              planted_file=pth.replace('\\', '/'), planted_sha256=sha(b), planted_bytes=len(b),
                                              planted=[dict(cls=(FIVE_CLS if c == 'FIVE' else c), binder=bn, decl=dn, text=txt, grade=gr,
                                                            test=('five-name' if c == 'FIVE' else ('no-class control' if c == 'NONE' else 'class')))
                                                       for c, bn, dn, txt, gr in P]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RULE
def _planted_reads(E):
    """### every planted declaration read by rule module E: RETURN [dict(decl, want_cls, want_grade, got_cls, got_grade, ok)]."""
    J = jl('b637_binder_classes.json')
    src = io.open(J['planted_file'], encoding='utf-8').read() if os.path.exists(J.get('planted_file', '')) else ''
    out = []
    for p in J.get('planted') or []:
        m = re.search(r'^theorem ' + re.escape(p['decl']) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
        head = ' '.join(m.group(1).split()) if m else ''
        try:
            gr = E.grade(head, 'theorem')[0]
            bs = E.binders_of(head) if hasattr(E, 'binders_of') else []
            b = [x for x in bs if x['name'] == p['binder'] or (p['binder'] == '' and x['kind'] == 'instance')]
            gc = b[0]['cls'] if b else None
        except Exception as e:
            gr, gc = ('NO CLASS' if type(e).__name__ == 'BinderUnclassed' else 'RAISED %s' % type(e).__name__), None
        want_cls = None if p['test'] == 'no-class control' else p['cls']
        ok = (gr == p['grade']) and (gc == want_cls)
        out.append(dict(decl=p['decl'], test=p['test'], binder=p['binder'], want_cls=want_cls, want_grade=p['grade'], got_cls=gc, got_grade=gr, ok=ok))
    return out


def rule_test(*a):
    """### Component 3, after the rule's rewrite through the Edit tool: the rule's diff against relay f3a2f6b2; test_e0_rule.py and
    ### test_e0_existential.py run and counted by the case pattern, the planted directory the test's first argument."""
    _diff('tools/e0_rule.py', PRE_RELAY, 'b637_rule_diff.txt', 'THE E0 RULE REWRITTEN AS A TOTAL FUNCTION OVER THE CLASSIFICATION, tools/e0_rule.py')
    _diff('tools/test_e0_rule.py', PRE_RELAY, 'b637_rule_test_diff.txt', 'THE RULE`S TEST EXTENDED, tools/test_e0_rule.py')
    _diff('tools/test_e0_existential.py', PRE_RELAY, 'b637_existential_test_diff.txt', 'THE EXISTENTIAL TEST, tools/test_e0_existential.py')
    _run_test('tools/test_e0_rule.py', 'b637_rule_test', K.PLANTED_DIR)
    _run_test('tools/test_e0_existential.py', 'b637_existential_test')


_LAUNCH = '''import importlib.util, runpy, sys
spec = importlib.util.spec_from_file_location('e0_rule', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
sys.modules['e0_rule'] = m; sys.path.insert(0, sys.argv[2]); t = sys.argv[3]; sys.argv = [t] + sys.argv[4:]
try:
    runpy.run_path(t, run_name='__main__')
except SystemExit as e:
    print('### exit', e.code)
'''


def rule_control(*a):
    """### the extended test run against the rule as it stood (relay f3a2f6b2's blob, loaded in place of the module): the cases it fails,
    ### printed (data/b637_rule_control.txt)."""
    d = tempfile.mkdtemp()
    old = os.path.join(d, 'e0_rule.py')
    _write(old, (_show(RELAY, PRE_RELAY, 'tools/e0_rule.py') or '').encode('utf-8'))
    ln = os.path.join(d, 'launch.py')
    _write(ln, _LAUNCH.encode('utf-8'))
    out = []
    for t, args in (('tools/test_e0_rule.py', [K.PLANTED_DIR]), ('tools/test_e0_existential.py', [])):
        r = subprocess.run([sys.executable, ln, old, os.path.join(ROOT, 'tools'), os.path.join(ROOT, *t.split('/'))] + args, capture_output=True,
                           text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        o = (r.stdout or '') + (r.stderr or '')
        n, p = count_cases(o)
        fails = [l.strip()[:150] for l in o.split(NL) if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]
        out.append((t, n, p, fails, o))
    L = ['b637 -- COMPONENT 3: THE EXTENDED TESTS RUN AGAINST THE RULE AS IT STOOD (relay %s`s tools/e0_rule.py, loaded in place of the module) '
         '(%s)' % (PRE_RELAY, utc()), '']
    for t, n, p, fails, o in out:
        L += ['### %s : cases %d ; passing %d ; failing %d' % (t, n, p, n - p)] + ['    ' + f for f in fails] + ['']
    L += ['### THE OUTPUTS, WHOLE:']
    for t, n, p, fails, o in out:
        L += ['=== %s' % t] + o.rstrip(NL).split(NL)
    put_txt('b637_rule_control.txt', L)
    put_json('b637_rule_control.json', dict(at=utc(), runs=[dict(test=t, cases=n, passing=p, failing=fails) for t, n, p, fails, _o in out]))
    print(NL.join(L[2:2 + sum(2 + len(x[3]) for x in out)]))


def planted_read(*a):
    """### H71a-H71b on the planted set: every planted declaration read by the rewritten rule against its expectation fixed at Component 2
    ### (data/b637_planted_read.txt and its json); the five-name test's readings counted."""
    import e0_rule as E
    J = jl('b637_binder_classes.json')
    src = io.open(J['planted_file'], 'rb').read() if os.path.exists(J.get('planted_file', '')) else b''
    rows = _planted_reads(E)
    five = [x for x in rows if x['test'] == 'five-name']
    L = ['b637 -- COMPONENT 3: THE PLANTED DECLARATIONS READ BY THE REWRITTEN RULE (%s)' % utc(), '',
         '### the planted file %s, sha256 %s ; the bank`s %s ; equal %s' % (J.get('planted_file'), sha(src), J.get('planted_sha256'), sha(src) == J.get('planted_sha256')),
         '### the rule`s class table equal to the bank`s: %s' % ([list(c) for c in E.CLASSES] == [[c['id'], c['kind'], c['typing'], c['form'], c['outcome']] for c in J['classes']]), '']
    L += ['  %-8s %-17s binder %-6s want %-5s %-20s got %-5s %-20s %s' % (x['decl'], x['test'], x['binder'] or '[inst]', x['want_cls'], x['want_grade'],
                                                                     x['got_cls'], x['got_grade'], 'AS WANTED' if x['ok'] else '### NOT AS WANTED') for x in rows]
    cls_rows = [x for x in rows if x['test'] == 'class']
    L += ['', '### the five-name test: names %s ; readings %s ; distinct %d' % ([x['binder'] for x in five], [(x['got_cls'], x['got_grade']) for x in five],
                                                                             len(set((x['got_cls'], x['got_grade']) for x in five))),
          '### ### **CLASSES REACHED AS WANTED %d of %d ; THE NO-CLASS CONTROL %s ; THE FIVE NAMES READ %d DISTINCT OUTCOME(S).**' % (
              sum(1 for x in cls_rows if x['ok']), len(cls_rows), 'PRINTED AS A BUG' if any(x['test'] == 'no-class control' and x['ok'] for x in rows) else '### NOT AS WANTED',
              len(set((x['got_cls'], x['got_grade']) for x in five)))]
    put_txt('b637_planted_read.txt', L)
    put_json('b637_planted_read.json', dict(at=utc(), rows=rows, sha_equal=(sha(src) == J.get('planted_sha256')),
                                            table_equal=([list(c) for c in E.CLASSES] == [[c['id'], c['kind'], c['typing'], c['form'], c['outcome']] for c in J['classes']]),
                                            five=[(x['got_cls'], x['got_grade']) for x in five]))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE RERUN
def _textual_head(statement):
    import terminal_table as TT
    m = TT._DECL_KW.match(statement or '')
    if not m:
        return None, None
    if m.group(1) not in ('theorem', 'lemma'):
        return 'def', ''
    return 'theorem', ' '.join(re.sub(r'^\S+', '', statement[m.end():], count=1).split())


def _elab_head(e):
    parts = []
    for k, b, t in e['binders']:
        parts.append({'explicit': '(%s : %s)', 'implicit': '{%s : %s}', 'strict-implicit': '⦃%s : %s⦄'}.get(k, '[%s%s]') % ((b, t) if k != 'instance' else ('', t)))
    return (' '.join(parts) + ' : ' + e['concl']).strip()


def _read(E, kind, head):
    """### one reading: RETURN (grade, binders with classes, bug) -- the bug the BinderUnclassed text when a binder reaches no class."""
    if kind is None:
        return 'UNREAD', [], None
    if kind == 'def':
        return 'DEF', [], None
    bs = E.binders_of(head)
    try:
        return E.grade(head, 'theorem')[0], bs, None
    except Exception as e:
        return 'NO CLASS', bs, str(e)


def _new_table_rows(E, rows):
    """### the table's rows re-graded in memory by the generator's own provenance() under rule module E (nothing written)."""
    import terminal_table as TT
    save = sys.modules.get('e0_rule')
    sys.modules['e0_rule'] = E
    TT._ELAB.clear()
    try:
        R = copy.deepcopy(rows)
        for r in R:
            if not r.get('grade_cells'):
                r['grade'], r['provenance'] = 'UNGRADED', 'none'
            r.pop('mark', None)
        TT.provenance(R, None)
        return R
    finally:
        if save is not None:
            sys.modules['e0_rule'] = save


def _old_rule():
    import importlib.util
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'e0_rule_old.py')
    _write(p, (_show(RELAY, PRE_RELAY, 'tools/e0_rule.py') or '').encode('utf-8'))
    spec = importlib.util.spec_from_file_location('e0_rule', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _premise_heads(b, head):
    """### a premise binder's named head by the census's reading (b632_record.premise_name), or None and why."""
    import b632_record as R32
    return R32.premise_name(b['type'], head)


def rerun(*a):
    """### Component 4, (R247)(4)(iii): the textual reader over both kernels' table statements and the elaborated reading over both banks
    ### under the rewritten rule -- every binder classed (H71a), every grade compared to the committed table (relay f3a2f6b2's), every move
    ### printed with its class and reader (H71c, the whole table's graded rows and both kernels'), the 20 unnamed rows printed by class (H71d),
    ### the two readers' agreement per kernel. Banked as data/b637_rerun.txt and its json."""
    import e0_rule as E
    import terminal_table as TT
    committed = _table(PRE_RELAY)
    L, J = [], dict(at=utc(), kernels={})
    bugs, nbind = [], collections.Counter()
    L += ['b637 -- COMPONENT 4: THE RERUN UNDER THE REWRITTEN RULE -- BOTH READERS OVER BOTH KERNELS (%s)' % utc(), '']
    for kern in (K.EF_KERNEL, K.SEC_KERNEL):
        kr = [r for r in committed if r['repo'] == kern]
        bank = TT.elab_bank(os.path.join(D, K.KERNELS[kern]['bank']))
        rows, cls = [], collections.Counter()
        for r in kr:
            kind, head = _textual_head(r.get('statement'))
            tg, tb, tbug = _read(E, kind, head)
            e = bank.get(r['name'])
            if e is None or e.get('missing'):
                eg, eb, ebug = 'NO TYPE', [], None
            elif e['kind'] != 'theorem':
                eg, eb, ebug = 'DEF', [], None
            else:
                eg, eb, ebug = _read(E, 'theorem', _elab_head(e))
            for rdr, bs in (('textual', tb), ('elaborated', eb)):
                for b in bs:
                    nbind[(kern, rdr)] += 1
                    cls[(rdr, b['cls'])] += 1
                    if not b['cls']:
                        bugs.append((kern, rdr, r['name'], b['kind'], b['name'], b['type'][:90], b['how']))
            rows.append(dict(name=r['name'], provenance=r.get('provenance'), table=r['grade'], textual=tg, elaborated=eg,
                             tbug=tbug, ebug=ebug, agree=(tg == eg)))
        both = [x for x in rows if x['textual'] not in ('UNREAD', 'DEFERRED') and x['elaborated'] not in ('NO TYPE',)]
        ag = sum(1 for x in both if x['agree'])
        nd = sum(1 for x in rows if x['textual'] == 'DEFERRED')
        J['kernels'][kern] = dict(rows=rows, both=len(both), agree=ag, ratio=(ag / len(both)) if both else 0, deferred=nd,
                                  classes=dict(('%s|%s' % k_, v) for k_, v in cls.items()))
        L += ['### %s (%s = %s; elaborated bank relay data/%s): rows %d ; read by both %d ; agreeing %d = %.4f ; the textual reader deferring '
              '(a type_of%% conclusion, the elaborated type the statement) %d, not counted as read' % (
                  kern, K.KERNELS[kern]['tag'], K.KERNELS[kern]['pin'], K.KERNELS[kern]['bank'], len(rows), len(both), ag, (ag / len(both)) if both else 0, nd)]
        L += ['    binders by reader and class: %s' % ' '.join('%s/%s %d' % (k_[0][0], k_[1], v) for k_, v in sorted(cls.items(), key=lambda x: (x[0][0], str(x[0][1]))))]
        L += ['    disagreeing: %s' % ([(x['name'], x['textual'], x['elaborated']) for x in both if not x['agree']][:40] or 'NONE'), '']
    # ### the moves: the generator's provenance() on the committed rows, under the old rule and the new, in memory
    old_R, new_R = _new_table_rows(_old_rule(), committed), _new_table_rows(E, committed)
    o = dict(((r['repo'], r['name']), r) for r in old_R)
    n = dict(((r['repo'], r['name']), r) for r in new_R)
    cs = dict(((r['repo'], r['name']), r) for r in committed)
    same_old = sum(1 for k_ in cs if (o[k_]['grade'], o[k_].get('provenance')) == (cs[k_]['grade'], cs[k_].get('provenance')))
    graded = [k_ for k_ in cs if cs[k_].get('provenance') in ('rule', 'rule-elab')]
    moves = []
    for k_ in sorted(cs):
        if (n[k_]['grade'], n[k_].get('provenance')) != (cs[k_]['grade'], cs[k_].get('provenance')):
            r = cs[k_]
            reader = 'elaborated' if n[k_].get('provenance') == 'rule-elab' else ('textual' if n[k_].get('provenance') == 'rule' else n[k_].get('provenance'))
            if reader == 'elaborated':
                e = TT.elab_bank(os.path.join(D, K.KERNELS.get(k_[0], {}).get('bank', 'elab_types.txt'))).get(k_[1])
                head = _elab_head(e) if e else ''
            else:
                head = _textual_head(r.get('statement'))[1] or ''
            bs = E.binders_of(head) if head else []
            why = [('%s %s : %s' % (b['cls'], b['name'], b['type'][:70])) for b in bs if b['outcome'] in ('premise', 'seam', 'unlisted')]
            moves.append(dict(repo=k_[0], name=k_[1], old=[cs[k_]['grade'], cs[k_].get('provenance')], new=[n[k_]['grade'], n[k_].get('provenance')],
                              reader=reader, classes=why, grade_moved=(cs[k_]['grade'] != n[k_]['grade'])))
    gm = [m for m in moves if m['grade_moved']]
    both_k = [k_ for k_ in graded if k_[0] in (K.EF_KERNEL, K.SEC_KERNEL)]
    gm_k = [m for m in gm if m['repo'] in (K.EF_KERNEL, K.SEC_KERNEL)]
    L += ['### THE MOVES -- the generator`s provenance() over the committed table`s rows (relay %s) in memory: under the rule as it stood %d of %d '
          'rows reproduce the committed grade and provenance; under the rewritten rule %d rows move, %d in grade' % (PRE_RELAY, same_old, len(cs), len(moves), len(gm)),
          '### graded rows (rule / rule-elab) %d ; grade moves %d = %.2f %% ; in the two kernels %d graded, %d moved = %.2f %%' % (
              len(graded), len(gm), 100.0 * len(gm) / max(1, len(graded)), len(both_k), len(gm_k), 100.0 * len(gm_k) / max(1, len(both_k))),
          '### by (old, new) grade: %s ; by reader: %s' % (dict(collections.Counter((m['old'][0], m['new'][0]) for m in gm)), dict(collections.Counter(m['reader'] for m in moves))), '']
    for m in moves:
        L.append('  %-30s %-66s %-24s -> %-24s [%s] %s' % (m['repo'], m['name'][:66], '/'.join(m['old']), '/'.join(m['new']), m['reader'], '; '.join(m['classes'])[:300]))
    # ### the 20 unnamed rows, by class
    U = []
    for l in rd(K.UNNAMED_BANK).split(NL):
        mm = re.match(r'^  (U\d\d) (\S+)\s+(\S+)\s+(\S+)\s+(.*?) :: ', l)
        if mm:
            U.append(dict(id=mm.group(1), scope=mm.group(2), prov=mm.group(3), repo=mm.group(4), name=mm.group(5).strip()))
    L += ['', '### THE 20 UNNAMED ROWS (relay data/%s), EACH BY CLASS UNDER THE REWRITTEN RULE:' % K.UNNAMED_BANK]
    resid, Uout = [], []
    for u in U:
        r = cs.get((u['repo'], u['name']), {})
        kind, head = _textual_head(r.get('statement'))
        g_, bs, bug = _read(E, kind, head) if kind else ('UNREAD', [], None)
        prem = [b for b in bs if b['outcome'] in ('premise', 'seam', 'unlisted')]
        named = [(b, _premise_heads(b, head)) for b in prem]
        unnamed = [(b, w) for b, (nm, w) in named if not nm]
        taken = bool(r) and (kind == 'def' or (bs is not None and not bug))
        if g_ == 'INTERFACES' and unnamed:
            resid.append(u['id'])
        Uout.append(dict(u, table=r.get('grade'), grade=g_, taken=taken, binders=[dict(name=b['name'], kind=b['kind'], type=b['type'][:120], cls=b['cls'], outcome=b['outcome'])
                                                                                    for b in bs], premises=[(b['name'], (nm or '-'), (w or '')) for b, (nm, w) in named]))
        L.append('  %s %-9s %-26s %-60s table %-12s rule %-18s takes a class %s' % (u['id'], u['scope'], u['repo'], u['name'][:60], r.get('grade'), g_, taken))
        for b in bs:
            L.append('        %-5s %-15s %-12s %s' % (b['cls'], b['kind'], b['name'], b['type'][:110]))
        for b, (nm, w) in named:
            L.append('        premise %s : head %s%s' % (b['name'], nm or '-- UNNAMED', (' (%s)' % w) if w else ''))
    L += ['', '### the unnamed rows taking a class: %d of %d ; INTERFACES on a premise with no nameable head (the premise table`s residue under '
          '"unnamed"): %d %s' % (sum(1 for x in Uout if x['taken']), len(Uout), len(resid), resid)]
    L += ['', '### ### **BINDERS READ %d (textual %d, elaborated %d) ; REACHING NO CLASS %d ; GRADE MOVES %d OF %d GRADED ROWS = %.2f %% ; UNNAMED ROWS '
          'CLASSED %d OF %d, %d REMAINING ON AN UNNAMED HEAD.**' % (
              sum(nbind.values()), sum(v for k_, v in nbind.items() if k_[1] == 'textual'), sum(v for k_, v in nbind.items() if k_[1] == 'elaborated'),
              len(bugs), len(gm), len(graded), 100.0 * len(gm) / max(1, len(graded)), sum(1 for x in Uout if x['taken']), len(Uout), len(resid))]
    if bugs:
        L += ['', '### THE BINDERS REACHING NO CLASS (bugs of the grammar):'] + ['  %s' % (x,) for x in bugs]
    J.update(binders=dict(('%s|%s' % k_, v) for k_, v in nbind.items()), bugs=[list(x) for x in bugs], moves=moves, graded=len(graded),
             grade_moves=len(gm), kernels_graded=len(both_k), kernels_grade_moves=len(gm_k), old_reproduces=same_old, rows=len(cs),
             unnamed=Uout, residue=resid)
    put_txt('b637_rerun.txt', L)
    put_json('b637_rerun.json', J)
    print(L[-1])


# ================================================================================ COMPONENT 5: THE GENERATOR, THE TABLE, THE PREMISES, THE PAGES
def gen_test(*a):
    """### the upstream exclusion's edit: tools/terminal_table.py against relay f3a2f6b2; tools/test_terminal_table_b637.py run and counted."""
    _diff('tools/terminal_table.py', PRE_RELAY, 'b637_gen_diff.txt', 'THE GENERATOR`S UPSTREAM EXCLUSION, (R247)(2)')
    _run_test('tools/test_terminal_table_b637.py', 'b637_gen_test')


def _table_state(rows=None):
    out = {}
    for r in (rows if rows is not None else _table()):
        out.setdefault((r['repo'], r['name']), (r['grade'], r.get('provenance'), r.get('mark') or '', r.get('kind') or ''))
    return out


def _counts(rows, exclude):
    c = collections.Counter()
    for r in rows:
        if exclude and (r.get('kind') == 'upstream' or r.get('mark') == 'upstream' or (r['repo'] == K.EF_KERNEL and r['name'] in K.MATHLIB_FIVE)):
            continue
        c[(r['grade'], r.get('provenance'))] += 1
    return c


def table(*a):
    """### the terminal table regenerated; every row whose grade, provenance, mark or kind moved printed with its cause -- the rewritten rule,
    ### the upstream exclusion, other; the grade counts before and after the exclusion printed (data/b637_table_<tag>.txt and its json)."""
    rows0 = _table()
    before = _table_state(rows0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = _table()
    after = _table_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    RJ = jl('b637_rerun.json')
    rule_moves = set((m['repo'], m['name']) for m in RJ.get('moves') or [])

    def cause(k):
        if after.get(k, ('',) * 4)[3] == 'upstream' or before.get(k, ('',) * 4)[3] == 'upstream':
            return 'the upstream exclusion'
        if k in rule_moves:
            return 'the rewritten rule'
        return 'other'
    tag = a[0] if a and a[0] != 'dry' else 'regen'
    files = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    cb, ca, ca_x = _counts(rows0, False), _counts(rows1, False), _counts(rows1, True)
    L = ['b637 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade, provenance, mark or kind moved %d ; the table files that moved against relay HEAD: %s' % (
             len(added), len(gone), len(moved), files or 'NONE'),
         '### by cause: %s' % dict(collections.Counter(cause(k) for k in moved + added + gone)),
         '### grade counts before the regeneration: %s' % dict(sorted(cb.items(), key=lambda x: str(x[0]))),
         '### grade counts after, every row: %s' % dict(sorted(ca.items(), key=lambda x: str(x[0]))),
         '### grade counts after, the upstream rows excluded ((R247)(2)): %s ; upstream rows %d' % (
             dict(sorted(ca_x.items(), key=lambda x: str(x[0]))), sum(1 for x in rows1 if x.get('kind') == 'upstream')), '']
    L += ['### EVERY MOVE:']
    L += ['  MOVED %s / %-62s %s -> %s  [%s]' % (k[0], k[1], before[k], after[k], cause(k)) for k in moved]
    L += ['  ADDED %s / %-62s %s  [%s]' % (k[0], k[1], after[k], cause(k)) for k in added]
    L += ['  GONE  %s / %-62s %s  [%s]' % (k[0], k[1], before[k], cause(k)) for k in gone]
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d ; UPSTREAM ROWS %d.**' % (
        len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]), sum(1 for x in rows1 if x.get('kind') == 'upstream'))]
    if r.returncode:
        L += ['### THE GENERATOR EXITED %d:' % r.returncode] + (r.stdout + r.stderr).rstrip(NL).split(NL)[-15:]
    name = 'b637_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, moved=[[k[0], k[1], list(before[k]), list(after[k])] for k in moved],
                                                 added=[list(k) for k in added], gone=[list(k) for k in gone], files_moved=files,
                                                 grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]],
                                                 causes={'%s|%s' % k: cause(k) for k in moved + added + gone},
                                                 counts_before={'%s|%s' % k: v for k, v in cb.items()}, counts_after={'%s|%s' % k: v for k, v in ca.items()},
                                                 counts_after_excluded={'%s|%s' % k: v for k, v in ca_x.items()},
                                                 upstream=sum(1 for x in rows1 if x.get('kind') == 'upstream')))
    print(NL.join(L[2:7])); print(L[-1])


def _census_premise_table():
    """### the census at v0.5's printed premise table (:693-:736): {head: (kernels, b632 count, now count)}."""
    t = K.show(K.CEN5) or ''
    out = {}
    for l in lines_of(t)[K.CEN5_PREMISES[0] - 1:K.CEN5_PREMISES[1]]:
        m = re.match(r'^\| (\S+) \| ([^|]*) \| [^|]* \| (\d+) → (\d+)', l)
        if m:
            out[m.group(1)] = (m.group(2).strip(), int(m.group(3)), int(m.group(4)))
    return out


def premises(*a):
    """### Component 5, (R247)(4)(iv): the 42-premise table recomputed beside the old -- the census's own method (the rule-graded INTERFACES
    ### rows, each premise's named head by the census's reader) under the rewritten rule over the regenerated table, the upstream rows excluded;
    ### and beside it the binder-class premise table (rule and rule-elab rows, every premise binder by its class, named or unnamed). Banked as
    ### data/b637_premises.txt and its json."""
    import e0_rule as E
    import terminal_table as TT
    rows = [r for r in _table() if r.get('kind') != 'upstream']
    old = _census_premise_table()
    heads = collections.defaultdict(set)
    byclass = collections.defaultdict(set)
    unnamed = set()
    for r in rows:
        if r['grade'] != 'INTERFACES' or r.get('provenance') not in ('rule', 'rule-elab'):
            continue
        if r.get('provenance') == 'rule-elab':
            e = TT.elab_bank(os.path.join(D, K.KERNELS.get(r['repo'], {}).get('bank', 'elab_types.txt'))).get(r['name'])
            head = _elab_head(e) if e else ''
        else:
            head = _textual_head(r.get('statement'))[1] or ''
        for b in E.binders_of(head):
            if b['outcome'] not in ('premise', 'seam'):
                continue
            nm, _w = _premise_heads(b, head)
            key = (r['repo'], r['name'])
            byclass[b['cls']].add(key)
            if nm and r.get('provenance') == 'rule':
                heads[nm].add(key)
            elif nm:
                heads['%s (rule-elab)' % nm].add(key)
            else:
                unnamed.add(key)
    rule_heads = dict((h, v) for h, v in heads.items() if not h.endswith('(rule-elab)'))
    elab_heads = dict((h[:-len(' (rule-elab)')], v) for h, v in heads.items() if h.endswith('(rule-elab)'))
    L = ['b637 -- COMPONENT 5: THE NAMED PREMISES RECOMPUTED BESIDE THE CENSUS AT v0.5`S 42 (%s); the upstream rows excluded' % utc(), '',
         '### THE CENSUS`S METHOD (rule-graded INTERFACES rows, each premise`s named head by b632_record.premise_name): heads %d, rows summed %d '
         '(the census at v0.5: 42 heads, 63 rows summed)' % (len(rule_heads), sum(len(v) for v in rule_heads.values())), '',
         '  | named premise | the census at v0.5 (b632 → v0.5) | now, rule rows | now, rule-elab rows |', '  |:--|:--|:--|:--|']
    for h in sorted(set(old) | set(rule_heads) | set(elab_heads)):
        o = old.get(h)
        L.append('  | %s | %s | %d | %d |' % (h, ('%d → %d' % (o[1], o[2])) if o else '—', len(rule_heads.get(h, ())), len(elab_heads.get(h, ()))))
    L += ['', '### THE BINDER-CLASS PREMISE TABLE (rule and rule-elab INTERFACES rows; a row counted once per class it rests on):']
    L += ['  %-5s %4d rows' % (c, len(v)) for c, v in sorted(byclass.items())]
    L += ['  premises with no nameable head ("unnamed"): %d rows' % len(unnamed), '',
          '### ### **HEADS %d (the census`s 42) ; ROWS SUMMED %d (the census`s 63) ; RULE-ELAB HEADS %d ; UNNAMED ROWS %d.**' % (
              len(rule_heads), sum(len(v) for v in rule_heads.values()), len(elab_heads), len(unnamed))]
    put_txt('b637_premises.txt', L)
    put_json('b637_premises.json', dict(at=utc(), old={h: list(v) for h, v in old.items()}, rule_heads={h: sorted('%s|%s' % k for k in v) for h, v in rule_heads.items()},
                                        elab_heads={h: sorted('%s|%s' % k for k in v) for h, v in elab_heads.items()},
                                        by_class={c: len(v) for c, v in byclass.items()}, unnamed=sorted('%s|%s' % k for k in unnamed)))
    print(L[-1])


def census_counts(*a):
    """### Component 5, (R247)(4)(v): the census's premise table and provenance counts re-read with (R247)(2)'s exclusion, banked for v0.6
    ### (data/b637_census_counts.txt and its json); no census edition."""
    rows = _table()
    up = [r for r in rows if r.get('kind') == 'upstream']
    pv = lambda rs: dict(collections.Counter(r.get('provenance') for r in rs))   # noqa: E731
    byk = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        byk[r['repo']][0] += 1
        if r.get('kind') != 'upstream':
            byk[r['repo']][1] += 1
    P = jl('b637_premises.json')
    L = ['b637 -- COMPONENT 5, (R247)(4)(v): THE CENSUS`S COUNTS UNDER THE UPSTREAM EXCLUSION, BANKED FOR v0.6, NO CENSUS EDITION (%s)' % utc(), '',
         '### the table`s rows %d ; upstream %d ; graded rows counted %d' % (len(rows), len(up), len(rows) - len(up)),
         '### provenance, every row: %s' % pv(rows), '### provenance, the upstream rows excluded: %s' % pv([r for r in rows if r.get('kind') != 'upstream']),
         '### grade counts, every row: %s' % dict(collections.Counter(r['grade'] for r in rows)),
         '### grade counts, the upstream rows excluded: %s' % dict(collections.Counter(r['grade'] for r in rows if r.get('kind') != 'upstream')),
         '### INTERFACES rows, every row %d ; excluded %d ; rule-graded excluded %d' % (
             sum(1 for r in rows if r['grade'] == 'INTERFACES'), sum(1 for r in rows if r['grade'] == 'INTERFACES' and r.get('kind') != 'upstream'),
             sum(1 for r in rows if r['grade'] == 'INTERFACES' and r.get('kind') != 'upstream' and r.get('provenance') in ('rule', 'rule-elab'))),
         '### the premise table (data/b637_premises.txt): heads %d, rows summed %d, unnamed rows %d' % (
             len(P.get('rule_heads') or {}), sum(len(v) for v in (P.get('rule_heads') or {}).values()), len(P.get('unnamed') or [])), '',
         '### BY KERNEL, rows and rows counted under the exclusion:'] + ['  %-36s %4d %4d' % (k, v[0], v[1]) for k, v in sorted(byk.items())]
    L += ['', '### THE UPSTREAM ROWS:'] + ['  %s / %s' % (r['repo'], r['name']) for r in up]
    L += ['', '### ### **ROWS %d ; UPSTREAM %d ; COUNTED %d.**' % (len(rows), len(up), len(rows) - len(up))]
    put_txt('b637_census_counts.txt', L)
    put_json('b637_census_counts.json', dict(at=utc(), rows=len(rows), upstream=len(up), provenance_all=pv(rows),
                                             provenance_excluded=pv([r for r in rows if r.get('kind') != 'upstream']),
                                             by_kernel={k: v for k, v in byk.items()}, upstream_rows=['%s|%s' % (r['repo'], r['name']) for r in up]))
    print(L[-1])


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from b632's list and b635's probe in force (no Lean), written only where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b637_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b637_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
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
    kinds = collections.Counter(('correspondence row' if x[1:].startswith('|') else ('heading' if x[1:].startswith('#') else 'prose')) + x[0]
                                for x in dl)
    put_json('b637_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           kinds=dict(kinds), free_mb_before=fm, seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d by kind %s ; cells moved %s' % (k, rc, changed, secs, len(dl), dict(kinds),
                                                                                                         gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b637 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b637_gcp'), os.path.join(D, K.PROBE[k]))
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
    put_txt('b637_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b637_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b637_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b637'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b637_act_root.json')
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
    L = ['b637 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b637_root_arm.txt', L)
    put_json('b637_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'README.md', K.CEN4, K.CEN5, K.MONO, K.SIEVE6)
HKEYS = ('H71a', 'H71b', 'H71c', 'H71d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b636_closing_push_out.txt', 'data/b636_closing_push_out_attempt1.txt', 'data/act_roots.txt', 'tools/e0_rule.py',
              'tools/test_e0_rule.py', 'tools/test_e0_existential.py', 'tools/terminal_table.py', 'tools/test_terminal_table_b637.py', K.ROSTER}


def n5(trail_line=None, ot=None, *a):
    """### (R247)'s N5, the file-set by PATH; no sealed tool's hash differs; the kernels untouched; nothing deposits."""
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
    face = jl('b637_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE)]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b637_|audit_b637_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local and not differ
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel`s tracked tree unmoved against the face %s; PLACE-papers %s (beyond the ledgers and the pages: %s); %s; '
            'relay beyond the list, matched by path: %s; the sealed tools` hashes not agreeing %s; b628`s local intake bank in any relay commit %s, '
            'untracked now %s; no identifier of the author in any outbound request' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE',
                                                                                      differ or 'NONE', tracked_local, untracked_local))


def _vac(ok, n, word):
    """### a score over an empty population says VACUOUS in its verdict (b636's defect (a))."""
    return ('%s, VACUOUSLY' % word) if (ok and n == 0) else word


def scores(*a):
    PR, RR, RT, RC = jl('b637_planted_read.json'), jl('b637_rerun.json'), jl('b637_rule_test.json'), jl('b637_rule_control.json')
    TF, RA, GT, RO = jl('b637_table_final.json'), jl('b637_root_arm.json'), jl('b637_gen_test.json'), jl('b637_roster.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    prow = PR.get('rows') or []
    cls_rows = [x for x in prow if x['test'] == 'class']
    nb = sum((RR.get('binders') or {}).values())
    a_plant = bool(cls_rows) and all(x['ok'] for x in cls_rows) and PR.get('table_equal') is True and PR.get('sha_equal') is True
    a_kern = bool(RR) and nb > 0 and not RR.get('bugs')
    a_ok = a_plant and a_kern
    five = PR.get('five') or []
    b_ok = len(five) == len(K.FIVE_NAMES) and len(set(tuple(x) for x in five)) == 1
    gm, gr = RR.get('grade_moves', 0), RR.get('graded', 0)
    ratio = gm / gr if gr else 0
    c_ok = bool(RR) and gr > 0 and ratio <= K.H71C_BOUND and all(m['classes'] for m in (RR.get('moves') or []) if m['grade_moved'])
    U = RR.get('unnamed') or []
    d_ok = len(U) == 20 and all(x['taken'] for x in U)
    _r, _n, sh = seal_hashes()
    S = {
        'H71a': (('HOLDS' if a_ok else 'REFUTED'), 'the planted set: %d of %d classes reached as wanted, the class table equal to the bank %s, the planted file '
                 'the bank`s %s (data/b637_planted_read.txt); both kernels: %d binders read by both readers, %d reaching no class (data/b637_rerun.txt)' % (
                     sum(1 for x in cls_rows if x['ok']), len(cls_rows), PR.get('table_equal'), PR.get('sha_equal'), nb, len(RR.get('bugs') or []))),
        'H71b': (('HOLDS' if b_ok else 'REFUTED'), 'the five-name test reads %d distinct outcome(s) over %d names: %s' % (
            len(set(tuple(x) for x in five)), len(five), five)),
        'H71c': ((_vac(c_ok, gm, 'HOLDS') if c_ok else 'REFUTED'), '%d grade moves of %d graded rows = %.2f %% against the bound %.0f %%; in the two kernels %d of '
                 '%d; each move printed with its class (data/b637_rerun.txt)' % (gm, gr, 100.0 * ratio, 100 * K.H71C_BOUND, RR.get('kernels_grade_moves', 0),
                                                                                 RR.get('kernels_graded', 0))),
        'H71d': (('HOLDS' if d_ok else 'REFUTED'), 'of the %d unnamed rows %d take a class; %d remain INTERFACES on a premise with no nameable head: %s' % (
            len(U), sum(1 for x in U if x['taken']), len(RR.get('residue') or []), RR.get('residue'))),
        'N1': (('HELD' if a_kern else 'REFUTED'), 'as H71a over both kernels: %d binders, %d reaching no class' % (nb, len(RR.get('bugs') or []))),
        'N2': (('HELD' if b_ok else 'REFUTED'), 'as H71b'),
        'N3': (('HELD' if c_ok else 'REFUTED'), 'as H71c'),
        'N4': (('HELD' if d_ok else 'REFUTED'), 'as H71d, its first clause'),
        'N5': n5v,
        'S1': (('HELD' if RT and RT.get('rc') == 0 and RT.get('passing') == RT.get('cases') and RT.get('cases', 0) >= 26 + len(CLASSES) else 'REFUTED'),
               'the rule`s test %s of %s, its 26 cases and one per class beside the five-name test and the no-class control' % (RT.get('passing'), RT.get('cases'))),
        'S2': (('HELD' if RC and any(r['test'].endswith('test_e0_rule.py') and r['failing'] for r in RC.get('runs') or []) else 'REFUTED'),
               'the rule as it stood fails the new cases: %s' % [(r['test'], len(r['failing'])) for r in (RC.get('runs') or [])]),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) and RO and RO.get('builder_edited') is False else 'REFUTED'),
               'the sealed tools` hashes at the record: %s; the builder unedited %s' % (dict(collections.Counter(v for _t, v in sh)), RO.get('builder_edited') is False)),
    }
    put_json('b637_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b637 — lane three, act sixty-four under (R247): the binder grammar, the E0 rule a total function over a finite classification '
              'with names removed from the reading; both readers rerun over both kernels; the 20 unnamed rows read by class; upstream rows as kind; '
              'the mirror’s roster at the current editions')


def _figures():
    RR, PR, CC, RO, PM = (jl(n_) for n_ in ('b637_rerun.json', 'b637_planted_read.json', 'b637_census_counts.json', 'b637_roster.json', 'b637_premises.json'))
    return dict(k=len(CLASSES), m=RR.get('grade_moves', 0), u=len(RR.get('residue') or []), p=CC.get('upstream', 0), RR=RR, PR=PR, CC=CC, RO=RO, PM=PM)


def _title_entry():
    f = _figures()
    return ('## The binder grammar: %d classes, the E0 rule total over them with names removed from the reading, %d grades moved across the '
            'table, the 20 unnamed rows classed with %d unnamed heads remaining; %d upstream rows as kind; the mirror’s roster at v5.18, v0.6, v0.5'
            % (f['k'], f['m'], f['u'], f['p']))


def _finding_text():
    S, rl, J = jl('b637_scores.json'), jl('b637_record_lines.json'), jl('b637_act_root.json')
    f = _figures()
    RR, PM, TF = f['RR'], f['PM'], jl('b637_table_regen.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b637_author_answers.txt'), re.M))
    t = _title_entry()
    kk = RR.get('kernels') or {}
    e = ['', t, '',
         '*Filed at b637 on the author’s ruling `(R247)`%s. Banks: relay `data/b637_binder_classes.txt`, `data/b637_planted_read.txt`, '
         '`data/b637_rerun.txt`, `data/b637_premises.txt`, `data/b637_census_counts.txt`, `data/b637_table_regen.txt`, `data/b637_roster.txt`, '
         '`data/b637_act_root.txt`. Nothing deposits.*' % ((' and the author’s %d answers' % n_ans) if n_ans else ''), '',
         '**The classification** (Component 2): Lean’s four binder kinds read in the toolchains’ own sources and two positions of the conclusion '
         '(an antecedent of its implication, a binder of an existential in it); typing a Prop or data, read from the type alone with a lexicon of '
         'the heads the population applies, each at its declaration’s file and line; the Prop’s form in the criterion’s order; %d classes, each '
         'with its outcome, and one planted declaration per class whose expected class and grade were fixed before the rule read it.' % f['k'], '',
         '**The rule** (Component 3): relay tools/e0_rule.py rewritten as a total function over the classes, the name-prefix test removed; a '
         'binder that reaches no class raises and is printed as a bug, never graded; the planted set read %d of %d as wanted, the five names '
         'h, H, hyp, x and ξ reading one outcome. H71a %s, H71b %s.' % (
             sum(1 for x in f['PR'].get('rows') or [] if x['test'] == 'class' and x['ok']), sum(1 for x in f['PR'].get('rows') or [] if x['test'] == 'class'),
             S.get('H71a', ['?'])[0], S.get('H71b', ['?'])[0]), '',
         '**The rerun** (Component 4): both readers over both kernels, %d binders, none reaching no class; the two readings agree on %s of %s '
         'explicit-formula rows read by both and %s of %s structural-error-correction rows; %d grade moves of %d graded rows, each a premise '
         'the old name test did not read (an H, a self, a structure of premises named otherwise); H71c %s. The 20 unnamed rows each take a class, '
         '%d remaining on a premise with no nameable head. H71d %s.' % (
             sum((RR.get('binders') or {}).values()), kk.get(K.EF_KERNEL, {}).get('agree'), kk.get(K.EF_KERNEL, {}).get('both'),
             kk.get(K.SEC_KERNEL, {}).get('agree'), kk.get(K.SEC_KERNEL, {}).get('both'), f['m'], RR.get('graded', 0), S.get('H71c', ['?'])[0],
             f['u'], S.get('H71d', ['?'])[0]), '',
         '**The table and the premises** (Component 5): the upstream rows a kind with the grade cell —, %d of them, excluded from every grade '
         'count; the table regenerated, %d rows moving; the census’s named premises recomputed beside its 42, %d heads now over %d rows; the '
         'census’s counts under the exclusion banked for v0.6, no census edition.' % (
             f['p'], len(TF.get('moved') or []), len(PM.get('rule_heads') or {}), sum(len(v) for v in (PM.get('rule_heads') or {}).values())), '',
         '**The mirror’s roster** (`(R247)`(5)): %s files to %s, the current editions appended beside the superseded ones, the builder unedited.' % (
             f['RO'].get('before'), f['RO'].get('after')), '',
         '**The record lines** (`(R247)`(1)-(3)): b636 at its weight (FINDINGS :%s); the upstream clause and the name clause beneath the '
         'criterion (OPEN_TRAILS :%s, :%s).' % tuple(x.get('line') for x in (rl.get('lines') or [{}, {}, {}])[:3]), '',
         '**The root.** b637 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b633’s census (FINDINGS :7725) at its named premises and b634’s and b636’s '
         'readers (FINDINGS :7747, :7801) under a rule that reads both banks’ binders by kind; b625’s criterion (OPEN_TRAILS :12955) and b633’s '
         'forward guard (:13221) are compiled as classes. It strengthens the programme’s offering of a table whose grades read what a statement '
         'assumes, by the binder’s kind and form and not by its name.', '',
         '**Next.** Per `(R247)`(6): b638 on the author’s word -- the deposit, the author’s own act, with a mirror rebuilt on the new roster at its '
         'close; or the census at v0.6 with the upstream exclusion and the binder-class premise table.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


def _next_lines():
    return ['b638 names no kernel terminal; the deposit is the author’s own act, and the census at v0.6 reads the table it is given']


FOR_AUTHOR = ('(1) the binders of a statement read as Lean’s: the header’s groups and the conclusion’s leading telescope, a binder inside an '
              'existential’s body part of the conclusion (test_e0_existential’s seventh case re-pointed to it); (2) a type’s typing read with a '
              'lexicon of the heads the population applies, an application of an unlisted name read as a named predicate and so marked, a '
              'one-letter type bound nowhere read as a section or auto-bound type variable; (3) a met named predicate on quantified variables its '
              'own class, a premise under MET until ruled; (4) the explicit-formula bank the generator reads, relay data/elab_types.txt, b634’s '
              'blocks identical; (5) the upstream rows the mark reaches and the five Mathlib names')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b637_scores.json', 'b637_findings.json', 'b637_record_lines.json', 'b637_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b637_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or [{}, {}, {}])
    rows_ = ['', TRAIL_HEAD, '',
             '**(R247) ratified.** (1) b636 at its weight. (2) Upstream rows as kind. (3) The name no part of a binder’s reading. (4) '
             'W-ORD-BINDER-GRAMMAR. (5) The mirror’s roster. (6) The act after: b638.', '',
             '**Entered:** FINDINGS.md:%s (b636’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the upstream clause, standing), :%s (the name '
             'clause, standing); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line') if len(ls) > 1 else None,
                                                  ls[2].get('line') if len(ls) > 2 else None), '',
             '**Act root:** b637 `%s` (previous `%s`, b636’s; relay data/act_roots.txt).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b637_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b637_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R247)`(6), b638 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b637_scores.json')
    L = ['=' * 104, 'b637 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H71a-H71d, (R247)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0].startswith('HOLDS') for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0].startswith('HELD') for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0].startswith('HELD') for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b637_defects.txt').rstrip(NL).split(NL)
    put_txt('b637_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b637_scores.json', 'b637_findings.json', 'b637_trail.json', 'b637_record_lines.json', 'b637_act_root.json'))
    ls = rl.get('lines') or [{}, {}, {}]
    L = ['b637 -- THE COMPONENTS, BANKED UNDER (R247).', '',
         '### COMPONENT 0 : the process listing ; b636`s closing push-out and its first attempt relay %s ; push-b636* deleted by name '
         '(data/b637_branches.txt) ; every test file run (data/b637_tests_stepzero.txt) ; the suite at HEAD before the face (data/b637_arms_prerun.txt) ; '
         'the sealed tools` hashes at the seal (data/b637_seal_hashes.json) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b636`s weight FINDINGS :%s ; the upstream clause :%s ; the name clause :%s ; the roster (data/b637_roster.txt)' % tuple(
             x.get('line') for x in ls[:3]),
         '### COMPONENT 2 : the classification (data/b637_binder_classes.txt)',
         '### COMPONENT 3 : the rule (data/b637_rule_diff.txt, data/b637_rule_test.txt, data/b637_rule_control.txt, data/b637_planted_read.txt) ; '
         'H71a %s ; H71b %s' % (S['H71a'][0], S['H71b'][0]),
         '### COMPONENT 4 : the rerun (data/b637_rerun.txt) ; H71c %s ; H71d %s' % (S['H71c'][0], S['H71d'][0]),
         '### COMPONENT 5 : the generator (data/b637_gen_diff.txt, data/b637_gen_test.txt) ; the table (data/b637_table_regen.txt) ; the premises '
         '(data/b637_premises.txt) ; the pages (data/b637_page_zeta.json, data/b637_page_chi.json) ; page arms data/b637_page_arms.txt ; the census '
         'counts data/b637_census_counts.txt',
         '### COMPONENT 6 : FINDINGS :%s (the entry) ; OPEN_TRAILS :%s (the record) ; the root %s ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj.get('entry_line'), tj.get('line'), (J.get('root') or '')[:16], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b637_components.txt', L)


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
    put_json('b637_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
    put_json('b637_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b637_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-07 by b637 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b637_defects.json -- NOTHING WRITTEN')
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
    put_json('b637_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'planted', 'planted_text', 'seal_hashes', 'root_banks', 'answer_of', 'n5'):
        print('usage: b637_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
