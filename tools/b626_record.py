# -*- coding: utf-8 -*-
"""b626_record.py -- THE ACT'S RECORD TOOL, UNDER (R236). ### ONE SUBCOMMAND PER BANK.

### ### b626: LANE THREE, ACT FIFTY-THREE -- THE PLATT-TRUDGIAN HEIGHT AS A NAMED PREMISE AND THE HEIGHT PAIR, v0.22; THE THREE
### NODES RULED BY THE SEAM AND DATA CLAUSES; THE SECTION-VARIABLE TERMINALS READ; TWO GATE WORK-ORDERS ENTERED.
### Subcommands write only `data/b626_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`; CORRESPONDENCE rows through relay tools/corr_row.py's `write_row`. The data is tools/b626_worklist.py.
### No platform call. The E0 rule as it stood before the act is read from its blob at relay PRE_RELAY. The case counter is (R233)(3)'s
### standing form (OPEN_TRAILS :12889); the N5 scorer takes the trail record's expected line (OPEN_TRAILS :12799).
### b625's defects' sources repaired here: (e) the no-sorry clause counts `sorry` tokens with comments and docstrings stripped; (f)
### the answer helper returns the author's answer after the prompt's question, whole; every ledger text is dry-run before the seal.
"""
import difflib
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
import b626_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
SESSION_ID = 'f5c41941-fa74-40e9-b806-a98e7280e315'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PLANTED = SP + '/b626_planted'
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b626_registration_2026-10-05.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')


def _w(name):
    return os.path.join(SP if DRY else D, name)


def _r(name):
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
_DJ = os.path.join(D, 'b626_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b626 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b626_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the rung`s work-order, the criterion and the vendor re-priced, the correction entries, the form, the precedence '
         'order, the authority order, the build clause, the N5 line', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12228, 12354, 12356, 12799, 12891, 12955, 12961, 12962, 12964, 12965, 12967, 12968, 12970], 1500),
        ('FINDINGS: b625`s entry', PP, PRE_PP, 'FINDINGS.md', [7532, 7537], 600),
        ('relay data/b625_e0_classes.txt: the three nodes for ruling', RELAY, PRE_RELAY, 'data/b625_e0_classes.txt',
         ('GREP', r'(h2_sign_imp_rh_of_seam|paperFT_growth)'), 300),
        ('relay data/b625_section_vars.txt, whole', RELAY, PRE_RELAY, 'data/b625_section_vars.txt', ('ALL',), 400),
        ('relay tools/e0_rule.py after 576891c5: the domain list, the five entries and the grade function', RELAY, PRE_RELAY,
         'tools/e0_rule.py', ('GREP', r'^DOMAIN =|dict\(head=|^def grade|^def domain_case|^def restriction_case'), 300),
        ('relay tools/test_e0_rule.py: its cases', RELAY, PRE_RELAY, 'tools/test_e0_rule.py', ('GREP', r"want\('\(\d+\)"), 200),
        ('SIDE-explicit-formula v0.21: the support pair at DetectionRegion.lean', K.KER, 'v0.21', 'SIDEExplicitFormula/DetectionRegion.lean',
         [29, 30, 47, 52], 300),
        ('SIDE-explicit-formula v0.21: the zero predicate', K.KER, 'v0.21', 'Zeta23/Statement.lean', [54], 300),
        ('SIDE-explicit-formula v0.21: the vendored RH bridge', K.KER, 'v0.21', 'Vendored/Bulka/Lc/LiCriterion/RHBridge.lean', [42, 43, 44, 45, 46], 300),
        ('SIDE-explicit-formula v0.21: the house form of a named-premise structure (Simplicity.lean)', K.KER, 'v0.21',
         'SIDEExplicitFormula/Simplicity.lean', [1, 2, 3, 40, 41, 45], 300),
        ('SIDE-explicit-formula v0.21: its AxiomCheck lines', K.KER, 'v0.21', 'AxiomCheckSimplicity.lean', ('GREP', r'exceptional_mass|SimpleProportion'), 300),
        ('SIDE-explicit-formula v0.21: CriterionConverse`s variable block and the terminals in its scope', K.KER, 'v0.21',
         'SIDEExplicitFormula/Chi/CriterionConverse.lean', [26, 264, 270], 300),
        ('SIDE-global-section: the cells of the section-variable terminals and of the seam node', K.GS, K.PRE_GS, 'CORRESPONDENCE.md', [456, 458, 505, 508, 509], 500),
        ('relay tools/act_root.py: the repository list', RELAY, PRE_RELAY, 'tools/act_root.py', ('GREP', r'^def (repositories|registry_kernels|page_kernels)'), 300),
        ('relay data/act_roots.txt', RELAY, PRE_RELAY, 'data/act_roots.txt', ('ALL',), 300),
        ('relay data/b625_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b625_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b626 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
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
    put_txt('b626_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R236) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def _calls():
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
    return [c for c in calls if c[0] > act_from()], results


def answers(*a):
    since, results = _calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b626 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b626_author_answers.txt', L)


def answer_of(k):
    """### b625's defect (f), repaired: the author's answer to the act's k-th prompt (0-based), after the question, whole."""
    t = rd('b626_author_answers.txt')
    m = re.findall(r'^RESULT \(transcript line \d+\): (.*)$', t, re.M)
    if len(m) <= k:
        return 'no answer banked'
    r = m[k].split('"="', 1)[-1]
    return r.split('". Read the answers carefully', 1)[0].strip()


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7',
            'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab'}
WRITTEN_KERNS = ('SIDE-explicit-formula', 'SIDE-global-section')   # ### the two this act writes: the rung (tagged branch), the CORRESPONDENCE rows


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
    put_json('b626_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE LEDGER HELPERS
def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def predict_cells(text, ledger):
    """### the grade cells the terminal table's tight reader takes from `text` appended to `ledger`, the FINDINGS-form directive's
    ### own line excepted for its terminal: [(line offset, name, grade)]."""
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
    p = os.path.join(SP if DRY else D, 'b626_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _land(Q, items, bank, entry=None):
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


def _guarded(items, ledger, name):
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(allt, ledger)
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, name)
    print('  table cells these lines would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    return cells, nd, clean


# ================================================================================ COMPONENT 1: THE RECORD LINES
B625_ENTRY = 7537
CRITERION_OT = 12955
RUNG_OT = 12891
W_HEAD = '*Appended 2026-10-05 by b626 to b625’s entry (:%d), under `(R236)`(1) -- b625 AT ITS WEIGHT:*'
CL_HEAD = '*Appended 2026-10-05 by b626 to the domain-condition criterion (:%d), under `(R236)`(2) and the author’s answer before b626’s seal -- THE SEAM AND DATA CLAUSES:*'
RD_HEAD = '*Appended 2026-10-05 by b626 to the domain-condition criterion (:%d), under `(R236)`(3) -- THE SEAT’S THREE READINGS, CONFIRMED, AND THE PREDICATE-VARIABLE CLAUSE:*'
MM_HEAD = '*Appended 2026-10-05 by b626 to W-ORD-PLATT-RUNG (:%d), under the author’s answer before b626’s seal -- THE PAIR’S NAME AND ITS STATEMENT, THE NAVIGATOR’S:*'
GE_HEAD = '*Appended 2026-10-05 by b626, under `(R236)`(4) -- W-ORD-GATE-FROM-ELABORATOR, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD:*'
BG_HEAD = '*Appended 2026-10-05 by b626, under `(R236)`(4) -- W-ORD-BINDER-GRAMMAR, PRICED, NOT STARTED, THE TRIGGER THE AUTHOR’S WORD:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    pre, post = _count_bank(_rel('b625_checks.txt')), _count_bank(_rel('b625_checks_postpush.txt'))
    DJ = json.loads(_rel('b625_defects.json'))
    return ('\n%s the closure of Zeta23/FinalMult.lean at v1.0 = 3635e748: 135 modules, 46,256 lines, 57 already in the kernel '
            'byte-identical (52d8cf9), 78 new (28,151 lines), the toolchains v4.33.0-rc2 with Mathlib 51e6992e against v4.34.0-rc1 with '
            'Mathlib de5ce8a9; nothing copied, built, branched or tagged; the work-order re-priced at OPEN_TRAILS :12970 on two routes, the '
            'port at not fewer than five acts and the cross-kernel discharge at one, neither started; exceptional_mass_le_third INTERFACES '
            'on two_thirds. The 33 nodes (relay data/b625_e0_classes.txt): 29 agreeing and closed; the family form’s step lemma corrected at '
            'its four cells by dated entries (FINDINGS :7534; OPEN_TRAILS :12961, :12964, :12967), its table row DERIVES, no other row '
            'moved; 3 for ruling, ruled at `(R236)`(2). The E0 rule edited after the seal (relay 576891c5), its test 16 of 16, the rule as '
            'it stood failing the new cases alone; 29 grades moved on the pages, all within the 33. The root over 38 repositories, '
            'REGISTRY’s kernel rows adding SIDE-carrier-spec, SIDE-fano-darkness and SIDE-li-map beside SIDE-explicit-formula -- the '
            'ruling’s single name the navigator’s understatement; b625’s root 8c1c76ba…98f5, b624 and b625 verifying; the act_root.py edit '
            'the widening required, N5 refuted on its wording, the navigator’s, the edit ratified. The census’s kernel column naming 32 '
            'kernels and not nine, the navigator’s conflation of the unpushed-tag count with the kernel count. H59a-H59c NOT SCORABLE by '
            'the hold; H59d refuted on its wording by the step lemma’s correction, the navigator’s; N1, N2, N4, N5 REFUTED, N1-N2 by the '
            'hold and the navigator’s limit set without the listing, N4 by the section-variable finding; N3, S1-S5 HELD. Relay 42677181; '
            'PLACE-papers dd4f700. The suite %d of %d before the push and %d of %d after it by the seat’s defects (a)-(c), each claim '
            'tested directly and holding; defects (a)-(f) the seat’s (relay data/b625_defects.txt, %d entries); the SIDE-frobenius double '
            'read kept as _attempt1 and re-run alone. Nothing deposited; no kernel touched.\n'
            % (W_HEAD % entry, pre[0], pre[1], post[0], post[1], len(DJ['defects'])))


def _clauses():
    return ('\n%s (i) SEAM ANTECEDENTS: a Prop that is the antecedent of a top-level implication in a statement’s conclusion is read as '
            'the rule reads a binder when it is itself a named implication between open statements -- a seam, the kernel’s own “_of_seam” '
            'marker -- entered in the rule by name and pin with the principle written beside the entry, so the next seam is added by the '
            'principle and not by a name match: an entry is a Prop the kernel names whose definition, read at its pin, is an implication '
            'between open statements and which no theorem of the kernel derives. A plain A → B between open statements is the kernel’s '
            'result and keeps DERIVES. The ruling as first worded read every antecedent; measured before the seal over the 193 page '
            'nodes it moved 14 plain implications DERIVES to INTERFACES, and the author narrowed it (relay data/b626_author_answers.txt). '
            'Its instance: h2_sign_imp_rh_of_seam INTERFACES on rh_strip_imp_rh, as its cells grade it; its one DERIVES cell takes a dated '
            'correction. (ii) DATA BINDERS: a binder whose type is not a Prop -- a function, a real, a natural, a character -- is an object '
            'of the statement and not a hypothesis whatever its name; its instances paperFT_growth and paperFT_growth_at, h : ℝ → ℂ not '
            'entering. Both read into relay tools/e0_rule.py after b626’s seal, with tests on the three nodes and on planted cases.\n'
            % (CL_HEAD % CRITERION_OT))


def _readings():
    ents = '; '.join('%s restricting %s (%s)' % (h, ' and '.join(v), w) for h, v, w in K.RESTRICTS)
    return ('\n%s confirmed by the author: (1) b570’s rule that a restriction counts as a domain condition on a variable the conclusion '
            'mentions, kept; (2) the five named predicates read as domain conditions from their definitions and entered in the rule with '
            'file and line, with the clause that each entry names the quantified variable it restricts -- a predicate on a fixed object '
            'the kernel names is a premise and not a domain condition, so an entry that cannot name its variable is struck from the list; '
            'printed with their variables: %s; none struck; (3) a binder of the form ∀ C ∈ sevenClasses, C Phi read by its body as a '
            'premise about the fixed Phi.\n' % (RD_HEAD % CRITERION_OT, ents))


def _mismatch():
    return ('\n%s the work-order here and `(R236)`(5) named “the finite side of the h2_sign_iff_forall_upto pair instantiated at that '
            'T”; read at SIDE-explicit-formula v0.21 (DetectionRegion.lean :29), that finite side, h2_sign_upto L₀, is Weil positivity '
            'on the windows whose support lies in [−L₀, L₀] -- L₀ a support bound, not a zero height -- and a verification of every zero '
            'with |Im ρ| ≤ T on the line implies it at no L₀, a compactly supported window’s transform being entire. Both were written from '
            'the pair’s name and not its statement at :29 -- the navigator’s. The seat’s reading, confirmed by the author and entered here: '
            'an instantiation of h2_sign_upto at T would credit Platt and Trudgian with a statement they did not verify. The rung built '
            'instead, by the author’s answer before the seal: a height pair, rh_upto T and its join to RiemannHypothesis, definitional, '
            'each zero having finite height, so it carries no analytic content; the rung’s weight is the premise’s and nothing else. The '
            'support pair stands untouched.\n' % (MM_HEAD % RUNG_OT))


def _gate_elab():
    return ('\n%s Items: the shared E0 rule reads each terminal’s elaborated type from a #check print at the pin, so section variables, '
            'instance binders and auto-bound implicits enter the reading by construction and the textual header cut retires; the '
            'textual rule kept beside it until the two agree on every page node. **Price:** one act per kernel build under the hold. '
            '**Trigger:** the author’s word; the finding of relay data/b625_section_vars.txt (36 Prop-typed section binders, 20 reaching '
            'a graded terminal) its occasion. Not started.\n' % GE_HEAD)


def _binder_grammar():
    return ('\n%s Items: the finite classification of binder kinds from Lean’s own binder forms (explicit, implicit, strict implicit, '
            'instance, auto-bound, section variable, arrow antecedent, existential), the domain-condition criterion stated as a total '
            'function over it, one planted module per kind. **Price:** one act, no build. **Trigger:** the author’s word. Not started.\n' % BG_HEAD)


def record_lines(*a):
    """### FINDINGS: b625's weight (to its entry :7537). OPEN_TRAILS: the seam and data clauses and the three readings (to the
    ### criterion :12955), the pair's mismatch (to :12891), the two gate work-orders. No line makes a table cell (predicted)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The 2/3 theorem held at its closure: ')
    if entry != B625_ENTRY:
        sys.exit('### b625`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % entry, _weight(entry)), ('OPEN_TRAILS.md', CL_HEAD % CRITERION_OT, _clauses()),
             ('OPEN_TRAILS.md', RD_HEAD % CRITERION_OT, _readings()), ('OPEN_TRAILS.md', MM_HEAD % RUNG_OT, _mismatch()),
             ('OPEN_TRAILS.md', GE_HEAD, _gate_elab()), ('OPEN_TRAILS.md', BG_HEAD, _binder_grammar())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    _land(Q, items, 'b626_record_lines.json', entry)


# ================================================================================ CORRESPONDENCE ROWS (COMPONENTS 2 AND 3)
CORR = os.path.join(K.GS, 'CORRESPONDENCE.md')


def _rownums():
    return [int(m.group(1)) for m in re.finditer(r'^\|\s*(\d+)\s*\|', io.open(CORR, encoding='utf-8').read(), re.M)]


def _corr_cells(num, sup, name, grade, why, act_line):
    short = name.split('.')[-1]
    return [str(num),
            '**%s’S GRADE UNDER THE SUPERSESSION RULE** (b626, %s): this row’s grade cell replaces row %d’s for this terminal alone; '
            'row %d stands unedited above. %s' % (short, act_line, sup, sup, why),
            '`SIDE-explicit-formula` (v0.21 = 1d5d4dd) : `%s`' % name,
            'the axiom print of row %d, unchanged' % sup,
            'SUPERSEDES row %d: %s -- `%s`' % (sup, grade, name),
            'Written 2026-10-05 (b626) through relay tools/corr_row.py; the rule is `supersede` in relay tools/terminal_table.py.']


def _corr_rows(kind):
    if kind == 'seam':
        pairs = [(sup, n, 'INTERFACES', 'Read under the seam clause of `(R236)`(2)(i): its antecedent rh_strip_imp_rh, a named implication '
                  'between open statements, is a premise; its other cells grade it so (relay data/b626_e0_nodes.txt).',
                  'under the author’s ruling (R236)(2) and the answer before b626’s seal') for sup, n in K.SEAM_CORR]
    else:
        pairs = [(sup, n, 'INTERFACES', 'Read under `(R236)`(4): CriterionConverse’s section variables hχ : χ.IsPrimitive and h1 : χ ≠ 1 '
                  'reach it (relay data/b625_section_vars.txt) and are premises; the grade did not name them (relay '
                  'data/b626_section_terminals.txt).', 'under the author’s ruling (R236)(4)') for sup, n in K.SECTION_CORR]
    nxt = max(_rownums()) + 1
    return [_corr_cells(nxt + i, sup, n, gr, why, al) for i, (sup, n, gr, why, al) in enumerate(pairs)]


def _corr_land(kind, bank, *a):
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import corr_row as CR
    rows = _corr_rows(kind)
    text = NL.join('| ' + ' | '.join(c) + ' |' for c in rows)
    import terminal_table as TT
    pred = []
    for ln in text.split(NL):
        for off, seg in TT._segments(ln):
            for m in TT.GRADE_RE.finditer(seg):
                nm = [x for x in TT._names_on(seg)]
                pred.append((ln.split('|')[1].strip(), m.group(1), [x[2] for x in nm]))
    nd, _n = _nd(text)
    sc, clean = _scan_text(text, 'corr_%s' % kind)
    print('  rows %s ; grade words by row %s ; no-disclosure hits %s ; scanner %s' % ([r[0] for r in rows], pred, nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(text)
        return
    if any(nd.values()) or not clean or any(len(p[2]) != 1 for p in pred) or len(pred) != len(rows):
        sys.exit('### A ROW WOULD MAKE MORE THAN ITS ONE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    out = []
    for cells in rows:
        code, msg = CR.write_row(CORR, cells)
        out.append(dict(row=int(cells[0]), supersedes=int(cells[4].split('row ')[1].split(':')[0]), name=cells[2].split('`')[-2], code=code))
        if code != 0:
            put_json(bank, dict(rows=out, at=utc(), stopped=True))
            sys.exit('### corr_row refused row %s (code %d): %s' % (cells[0], code, msg))
    put_json(bank, dict(rows=out, at=utc()))
    print('  CORRESPONDENCE rows written: %s' % [(x['row'], x['supersedes']) for x in out])


def seam_rows(*a):
    """### (R236)(2)(i) and the answer: h2_sign_imp_rh_of_seam's one DERIVES cell (CORRESPONDENCE row 383) superseded to INTERFACES."""
    _corr_land('seam', 'b626_seam_rows.json', *a)


def section_terminals(*a):
    """### (R236)(4): the terminals in CriterionConverse's scope that hχ or h1 reach (relay data/b625_section_vars.json), each with its
    ### statement, its ledger grade and cells, and whether the grade names the variables (data/b626_section_terminals.txt and .json)."""
    SV = json.loads(_rel('b625_section_vars.json'))
    reach = [x for x in SV['reaching'] if x['file'].endswith('CriterionConverse.lean') and set(x['names']) & {'hχ', 'h1'}]
    terms = sorted(set(t[0] for x in reach for t in x['terminals']))
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    rows = {r['name']: r for r in T['rows']}
    L = ['b626 -- COMPONENT 3, (R236)(4): THE TERMINALS CriterionConverse`s SECTION VARIABLES hχ AND h1 REACH (%s)' % utc(), '',
         '### from relay data/b625_section_vars.json: %s' % ['%s:%d %s' % (x['file'], x['line'], ' '.join(x['names'])) for x in reach], '']
    out = []
    for n in terms:
        r = rows.get(n, {})
        cells = r.get('grade_cells') or []
        names_it = any(re.search(r'hχ|h1\b|IsPrimitive|≠ 1', c.get('quote') or '') and c.get('grade') == 'INTERFACES' for c in cells)
        out.append(dict(name=n, statement=r.get('statement'), grade=r.get('grade'), cells=[(c['ledger'], c['line'], c['grade']) for c in cells],
                        names_variables=names_it, verdict='CLOSED' if names_it else 'CORRECTED'))
        L.append('### %s -- ledger %s ; the grade names hχ or h1 %s ; ### %s' % (n, r.get('grade'), names_it, 'CLOSED' if names_it else 'CORRECTED'))
        L.append('    statement: %s' % ' '.join((r.get('statement') or '').split())[:300])
        L += ['    cell: %s :%d %s' % c for c in out[-1]['cells']]
    L += ['', '### ### **TERMINALS %d ; CLOSED %d ; CORRECTED %d.**' % (len(out), sum(x['verdict'] == 'CLOSED' for x in out),
                                                                       sum(x['verdict'] == 'CORRECTED' for x in out))]
    put_txt('b626_section_terminals.txt', L)
    put_json('b626_section_terminals.json', dict(at=utc(), terminals=out))
    print(L[-1])


def section_rows(*a):
    """### (R236)(4): each corrected terminal's DERIVES cells superseded to INTERFACES on hχ and h1, one CORRESPONDENCE row per cell."""
    _corr_land('section', 'b626_section_rows.json', *a)


# ================================================================================ COMPONENT 2: THE CLAUSES, THE RULE AND ITS TEST
def e0_module(rev=None):
    if rev is None:
        import e0_rule as E
        return E
    src = _show(RELAY, rev, 'tools/e0_rule.py')
    m = types.ModuleType('e0_rule_%s' % rev)
    exec(compile(src, 'e0_rule@%s' % rev, 'exec'), m.__dict__)
    return m


def e0_before(*a):
    src = _show(RELAY, PRE_RELAY, 'tools/e0_rule.py')
    sl = lines_of(src)
    keep = [i + 1 for i, l in enumerate(sl) if re.match(r'^(DOMAIN|BINDER|RESTRICTIONS) =|^def (grade|domain_case|restriction_case)\(|^    dict\(head=', l)]
    gi = [i + 1 for i, l in enumerate(sl) if l.startswith('def grade(')][0]
    nums = sorted(set(keep) | set(range(gi, gi + 21)))
    L = ['b626 -- COMPONENT 2: THE E0 RULE`S GRADE FUNCTION BEFORE THE EDIT, tools/e0_rule.py @ relay %s (%s; blob %s)' % (
        PRE_RELAY, utc(), g(RELAY, 'rev-parse', '%s:tools/e0_rule.py' % PRE_RELAY).strip()[:12]), '']
    L += ['    :%-4d %s' % (n, sl[n - 1]) for n in nums]
    put_txt('b626_e0_before.txt', L)


def _headers(rule):
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


def e0_diff(*a):
    d = g(RELAY, 'diff', PRE_RELAY, '--', *K.E0_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *K.E0_FILES)
    L = ['b626 -- COMPONENT 2: THE E0 RULE`S SEAM AND DATA CLAUSES AND THEIR TEST, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.rstrip(NL).split(NL)[-1].strip() if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b626_e0_diff.txt', L)
    print(L[2])


CONTROL_FMT = '### THE POSITIVE CONTROL: the same test with tools/e0_rule.py as it stood at relay %s (exit %d): cases %d, passing %d, failing %s'
CONTROL_RE = r'^### THE POSITIVE CONTROL: the same test with tools/e0_rule\.py as it stood at relay (\w+) \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$'
CONTROL_FAILING = ['(16)', '(17)', '(18)', '(19)']


def e0_test(*a):
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
    L = ['b626 -- COMPONENT 2: tools/test_e0_rule.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p), '',
          CONTROL_FMT % (PRE_RELAY, r2.returncode, n2, p2, failed2)]
    put_txt('b626_e0_test.txt', L)
    put_json('b626_e0_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, planted=planted,
                                       control=dict(rc=r2.returncode, cases=n2, passing=p2, failing=failed2)))
    print(L[-3])
    print(L[-1])


def e0_nodes(*a):
    """### every header both pages grade, by the rule before (relay PRE_RELAY) and after: the grades and premise lists that move,
    ### each printed beside its table grade; the disagreements after (data/b626_e0_nodes.txt and .json)."""
    old, new = e0_module(PRE_RELAY), e0_module(None)
    seen, _p = _headers(new)
    heads = {}
    for (k, n), (h, kind) in seen.items():
        heads.setdefault(n, (h, kind, k))
    tg = _table_grades()
    rows = []
    for n, (h, kind, k) in sorted(heads.items()):
        kk = 'theorem' if kind == 'theorem' else 'def'
        a_, b_ = old.grade(h, kk), new.grade(h, kk)
        rows.append(dict(name=n, page=k, kind=kind, before=a_[0], after=b_[0], why_before=a_[1], why_after=b_[1], table=tg.get(n)))
    moved = [r for r in rows if r['before'] != r['after']]
    premv = [r for r in rows if r['before'] == r['after'] and r['why_before'] != r['why_after']]
    ruled = set([K.SEAM_NODE] + list(K.DATA_NODES))
    dis = [dict(name=r['name'], page=r['page'], table=r['table'], rule=r['after']) for r in rows
           if r['kind'] == 'theorem' and r['table'] not in (None, 'UNGRADED') and r['table'].split('-')[0] != r['after'].split('-')[0]]
    L = ['b626 -- COMPONENT 2: EVERY NODE THE PAGES GRADE, BY THE E0 RULE BEFORE (relay %s) AND AFTER THE SEAM AND DATA CLAUSES (%s)' % (PRE_RELAY, utc()), '',
         '### distinct nodes graded %d ; grades moved %d (the three ruled %d, others %d) ; premise lists moved with the grade unmoved %d' % (
             len(rows), len(moved), sum(r['name'] in ruled for r in moved), sum(r['name'] not in ruled for r in moved), len(premv)), '']
    L += ['### GRADES MOVED:'] + ['  %-62s %s -> %s (table %s)%s ; %s' % (r['name'], r['before'], r['after'], r['table'],
                                                                      '' if r['name'] in ruled else ' ### NOT A RULED NODE', r['why_after'][:110]) for r in moved]
    L += ['', '### PREMISE LISTS MOVED, THE GRADE UNMOVED:'] + ['  %-62s %s: %s -> %s' % (r['name'], r['after'], r['why_before'][:80], r['why_after'][:80]) for r in premv]
    L += ['', '### PAGE NODES WHOSE TABLE GRADE DIFFERS FROM THE RULE`S READ AFTER THE CLAUSES:']
    L += ['  %-62s %-5s table %s ; rule %s' % (x['name'], x['page'], x['table'], x['rule']) for x in dis] or ['  NONE']
    L += ['', '### ### **NODES %d ; GRADES MOVED %d ; OUTSIDE THE THREE RULED %d (%s) ; DISAGREEMENTS NOW %d.**' % (
        len(rows), len(moved), sum(r['name'] not in ruled for r in moved), ', '.join(r['name'].split('.')[-1] for r in moved if r['name'] not in ruled) or 'none',
        len(dis))]
    put_txt('b626_e0_nodes.txt', L)
    put_json('b626_e0_nodes.json', dict(at=utc(), rows=rows, moved=[r['name'] for r in moved], premise_moved=[r['name'] for r in premv],
                                        disagreements=dis))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE RUNG
def publisher(*a):
    """### the publisher's page, read once by the seat (its capture written to the scratchpad as b626_publisher_capture.txt), printed
    ### beside the navigator's recollection: the DOI, the journal reference and the height (data/b626_publisher.txt and .json)."""
    cap = os.path.join(SP, 'b626_publisher_capture.txt')
    t = io.open(cap, encoding='utf-8').read() if os.path.exists(cap) else ''
    doi = (re.search(r'10\.1112/blms\.\d+', t) or re.search(r'x^', '')) if t else None
    jr = re.search(r'(Bull(?:etin)?\.? (?:of the )?London Math(?:ematical)?\.? Soc(?:iety)?\.?[^\n]{0,80})', t)
    hT = re.findall(r'(3\s*[·⋅x×\*]\s*10\s*\^?\s*\{?12\}?|3\s*[·⋅x×\*]\s*10¹²|3000175332800|3\.000175332800\s*[·⋅x×]\s*10\^?\{?12\}?)', t)
    J = dict(at=utc(), source=K.PUBLISHER_URL, capture_bytes=len(t.encode('utf-8')), doi=doi.group(0) if doi else None,
             journal=jr.group(1).strip() if jr else None, heights=sorted(set(hT)), recollection=K.RECOLLECTION)
    L = ['b626 -- COMPONENT 4: THE PUBLISHER`S PAGE, READ ONCE (%s)' % utc(), '',
         '### source %s ; capture %d bytes (the seat`s single read, relay never holds the page)' % (K.PUBLISHER_URL, J['capture_bytes']),
         '### the DOI read: %s ; the recollection: %s ; equal %s' % (J['doi'], K.RECOLLECTION['doi'], J['doi'] == K.RECOLLECTION['doi']),
         '### the journal read: %s ; the recollection: %s' % (J['journal'], K.RECOLLECTION['journal']),
         '### the height read: %s ; the recollection: %s' % (J['heights'] or 'NOT FOUND ON THE PAGE', K.RECOLLECTION['T'])]
    put_txt('b626_publisher.txt', L)
    put_json('b626_publisher.json', J)
    for l in L[2:]:
        print(l)


def build_bank(*a):
    """### the detached build calls' watchdog logs (scratchpad b626_build_<n>.log), banked: data/b626_build.txt and .json."""
    logs = sorted(f for f in os.listdir(SP) if re.match(r'b626_build_\d+\.log$', f))
    calls = []
    L = ['b626 -- COMPONENT 4: THE DETACHED BUILD CALLS AT THE HOLD (%s), one module per call, watched from the foreground' % utc(), '']
    for f in logs:
        t = io.open(os.path.join(SP, f), encoding='utf-8', errors='replace').read()
        st = re.search(r'^### START (\S+) free (\d+) MB pid (\d+) cmd (.*?) cwd', t, re.M)
        ex = re.search(r'^### EXIT (-?\d+) (\S+) (\d+) s peak (-?\d+)', t, re.M)
        errs = [l for l in t.split(NL) if re.search(r'error', l, re.I) and not l.startswith('###')]
        calls.append(dict(log=f, start=st.group(1) if st else None, free=int(st.group(2)) if st else None, cmd=st.group(4) if st else None,
                          rc=int(ex.group(1)) if ex else None, secs=int(ex.group(3)) if ex else None, peak=int(ex.group(4)) if ex else None,
                          errors=errs[:5]))
        L.append('### %s : %s ; started %s, free %s MB ; exit %s after %s s, peak %s MB ; errors %d' % (
            f, calls[-1]['cmd'], calls[-1]['start'], calls[-1]['free'], calls[-1]['rc'], calls[-1]['secs'], calls[-1]['peak'], len(errs)))
        L += ['    ' + e[:200] for e in errs[:5]]
    put_txt('b626_build.txt', L)
    put_json('b626_build.json', dict(at=utc(), calls=calls))


def prints(*a):
    """### the AxiomCheck module's output (the last build log whose command is `lake env lean AxiomCheckPlattRung.lean`), parsed: every
    ### #print axioms line with its axioms; sorryAx anywhere refuses (data/b626_prints.txt and .json)."""
    logs = sorted(f for f in os.listdir(SP) if re.match(r'b626_build_\d+\.log$', f))
    t = ''
    for f in logs:
        s = io.open(os.path.join(SP, f), encoding='utf-8', errors='replace').read()
        if K.AXCHECK_FILE in s.split(NL)[0] + (re.search(r'^### START .*$', s, re.M).group(0) if re.search(r'^### START .*$', s, re.M) else ''):
            t = s
    out = []
    for m in re.finditer(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", t):
        out.append(dict(name=m.group(1), axioms=[x.strip() for x in (m.group(2) or '').split(',') if x.strip()]))
    std = {'propext', 'Classical.choice', 'Quot.sound'}
    bad = [x for x in out if set(x['axioms']) - std]
    L = ['b626 -- COMPONENT 4: THE AXIOM PRINTS OF AxiomCheckPlattRung.lean AT THE BRANCH (%s)' % utc(), '']
    L += ['  %-62s %s' % (x['name'], x['axioms'] or 'no axioms') for x in out]
    L += ['', '### ### **PRINTS %d ; BEYOND THE STANDARD THREE %d %s ; sorryAx %s.**' % (len(out), len(bad), [x['name'] for x in bad] or '',
                                                                                         'PRESENT' if 'sorryAx' in t else 'ABSENT')]
    put_txt('b626_prints.txt', L)
    put_json('b626_prints.json', dict(at=utc(), prints=out, beyond=[x['name'] for x in bad], sorry='sorryAx' in t))
    print(L[-1])


def nodes_new(*a):
    """### the ζ node list at v0.22: b622's list (every record line unchanged), the pin moved to v0.22, the rung's five declarations
    ### appended (data/b626_nodes_zeta.txt)."""
    src = rd(K.NODES['zeta']).rstrip(NL).split(NL)
    if '# pin: v0.20' not in src:
        sys.exit('### b622`S LIST CARRIES NO `# pin: v0.20` LINE -- NOTHING WRITTEN')
    head = ['# b626 -- THE ζ NODE LIST AT v0.22, (R236)(5) and the author`s answer before b626`s seal: b622`s list (relay',
            '# data/b622_nodes_zeta.txt, every record line unchanged), the pin moved to v0.22; the five declarations of',
            '# SIDEExplicitFormula/PlattRung.lean appended -- the height rung, its pair and its named premise. Every cell is elaborated',
            '# by the generator`s probe at the pin, never typed here.', '#']
    body = [('# pin: v0.22' if l == '# pin: v0.20' else l) for l in src]
    adds = ['%s | kernel | added: (R236)(5), %s' % (n, why) for n, why in zip(K.RUNG_NODES, (
        'the height rung as a Prop', 'the height pair, definitional', 'the published height', 'the named premise (T1-lit)',
        'the rung at INTERFACES on the premise'))]
    put_txt(K.NEW_NODES_ZETA, head + body + adds)


def page_new(*a):
    """### ONE call in the foreground: the ζ page at v0.22 from the new list by a fresh probe (the checkout at v0.22, free memory
    ### above the hold); the probe's output banked as data/b626_probe_out.txt; the page written where it changed
    ### (data/b626_page_zeta.json)."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b626_probe')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_ZETA), pd, None)
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY:
        _write(os.path.join(D, K.NEW_PROBE_ZETA), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    if rc:
        put_json('b626_page_zeta.json', dict(rc=rc, log=log, at=utc(), seconds=secs))
        sys.exit('### ζ RE-EMIT AT v0.22 FAILED, exit %d: %s' % (rc, log))
    _page_write('zeta', pg, fm, secs, rc, meta)


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe (the ζ page from b626's list and probe once they exist)."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b626_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b626_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc, meta)


def zlist():
    """### the ζ page's list and probe in force: b626's once both are banked, else b622's list and b602's probe."""
    if os.path.exists(_r(K.NEW_NODES_ZETA)) and os.path.exists(_r(K.NEW_PROBE_ZETA)):
        return K.NEW_NODES_ZETA, K.NEW_PROBE_ZETA
    return K.NODES['zeta'], K.PROBE['zeta']


def _grade_cells(text):
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


def _shapes(text):
    out = {}
    for l in (text or '').split(NL):
        m = re.match(r'^\d+\. `([^`]+)` — .* — shape: ([A-Z—-]+|—) — ', l)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def _page_write(k, pg, fm, secs, rc, meta):
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb)
    gadded = sorted(n for n in gb if n not in ga)
    sh = _shapes(pg)
    put_json('b626_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, grade_cells_added=gadded, shapes={n: sh.get(n) for n in K.RUNG_NODES},
                                           dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s, added %d' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', len(gadded)))
    for x in dl[:30]:
        print('    ' + x[:240])


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    L = ['b626 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else (K.NODES[k], K.PROBE[k])
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b626_gcp'), os.path.join(D, pr))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', nl, r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    save = CP.E0
    CP.E0 = e0_module(TC.RELAY_PIN)       # ### b625's defect (b), repaired: the carried control freezes the E0 rule at its own pin
    try:
        c = TC.control()
    finally:
        CP.E0 = save
    for x in c:
        L.append('    %s (E0 at %s) %s : %s -- exit %d' % (TC.ARM, TC.RELAY_PIN, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b626_page_arms.txt', L)
    for l in L:
        print(l[:240])


def table(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    ch = [(x[1] if isinstance(x, list) else x) for x in diff.get('changed') or []]
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b626 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads (b625`s defect (a), repaired: the grade read from the table, not the diff):']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the rows added: %s' % [(x[1] if isinstance(x, list) else x) for x in diff.get('added') or []],
          '### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF : %s.**' % ('; '.join('%s %s' % (n.split('.')[-1], tg.get(n)) for n in ch) or 'EMPTY')]
    name = 'b626_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grades={n: tg.get(n) for n in ch}, files_moved=moved))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b626_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b626_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b626'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import act_root as AR
    res = AR.verify()
    J = jl('b626_act_root.json')
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
    L = ['b626 -- COMPONENT 5: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '### ls-remote calls by the arm, per repository: %d repositories, at most %d each' % (len(AR.LSR), max(AR.LSR.values()) if AR.LSR else 0),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b626_root_arm.txt', L)
    put_json('b626_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root'],
                                        lsr=dict(AR.LSR)))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H60a', 'H60b', 'H60c', 'H60d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
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


def sorry_tokens(rev='main'):
    """### b625's defect (e), repaired: `sorry` tokens at the explicit-formula kernel's `rev`, comments and docstrings stripped."""
    n = 0
    for f in g(K.KER, 'ls-tree', '-r', '--name-only', rev).split(NL):
        if f.endswith('.lean'):
            t = _show(K.KER, rev, f) or ''
            t = re.sub(r'/-.*?-/', '', t, flags=re.S)
            t = re.sub(r'--[^\n]*', '', t)
            n += len(re.findall(r'\bsorry\b', t))
    return n


def n5(trail_line=None, ot=None, *a):
    """### N5 by its letter: nothing deposits; no sorry on any main (tokens, comments stripped); no kernel file edited outside the
    ### tagged branch; no file written beyond the rung module and its AxiomCheck lines, the rule edit and its tests, the two banks,
    ### the suite repairs, the correction entries, the re-emitted pages, the table, the roots line, the record lines and the trails."""
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
    face = jl('b626_kernels_face.json')['kernels']
    now = kern_state(list(face))
    others_ok = all(now[k] == list(v) for k, v in face.items() if k not in WRITTEN_KERNS)
    st = sorry_tokens('main')
    ker_files = sorted(set(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').split(NL) if x.strip()))
    ker_ok = ker_files == sorted([K.RUNG_FILE, K.AXCHECK_FILE]) or ker_files == []
    gs_files = sorted(set(x for x in g(K.GS, 'diff', '--name-only', K.PRE_GS, 'main').split(NL) if x.strip()))
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    want_pp = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + [K.PNAME[k] for k in ('zeta', 'chi') if g(PP, 'diff', '--name-only', PRE_PP, 'HEAD', '--', K.PNAME[k]).strip()]))
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b626_', 'audit_b626_', 'terminal_table'))
                              and x != 'data/b625_closing_push_out.txt'))
    beyond = [x for x in relay_beyond if x not in set(K.E0_FILES) | {'data/act_roots.txt'}]
    ok = others_ok and st == 0 and ker_ok and gs_files in ([], ['CORRESPONDENCE.md']) and pp_ch == want_pp and not beyond and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the kernels this act does not write unmoved %s; sorry tokens on the explicit-formula main %d (comments '
            'stripped); the explicit-formula kernel`s files changed since v0.21 %s; SIDE-global-section %s; PLACE-papers %s; %s; relay '
            'beyond the list: %s' % (others_ok, st, ker_files or 'NONE', gs_files or 'NONE', pp_ch, rec_state, beyond or 'NONE'))


def _rung_grade():
    import e0_rule as E
    src = _show(K.KER, K.RUNG_TAG, K.RUNG_FILE) or ''
    m = re.search(r'^theorem rh_upto_platt(.*?):=', src, re.M | re.S)
    h = ' '.join(m.group(1).split()) if m else ''
    return E.grade(h, 'theorem') if h else ('UNREAD', '', [])


def scores(*a):
    EN, ET, PR, ST = jx('b626_e0_nodes.json'), jx('b626_e0_test.json'), jx('b626_prints.json'), jx('b626_section_terminals.json')
    PZ, PX, RA, AJ = jx('b626_page_zeta.json'), jx('b626_page_chi.json'), jx('b626_root_arm.json'), jx('b626_act_root.json')
    TF = jx('b626_table_final.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    rg = _rung_grade()
    prem = [b for b, _t in rg[2]] if rg[0] == 'INTERFACES' else []
    prem_types = rg[1]
    moved = EN.get('moved') or []
    ruled = set([K.SEAM_NODE] + list(K.DATA_NODES))
    others = [n for n in moved if n not in ruled]
    rows = {r['name']: r for r in EN.get('rows') or []}
    seam_ok = (rows.get(K.SEAM_NODE) or {}).get('after') == 'INTERFACES'
    data_ok = all((rows.get(n) or {}).get('after') == 'DERIVES' and ' h :' not in ' ' + (rows.get(n) or {}).get('why_after', '') for n in K.DATA_NODES)
    sh = PZ.get('shapes') or {}
    new_shapes = {n: sh.get(n) for n in K.RUNG_NODES}
    page_moved = [x for x in (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or [])]
    ruled_moves = [x for x in page_moved if any(x.endswith(n) for n in list(ruled) + K.SECTION_TERMINALS + [K.SEAM_ALSO])]
    other_moves = [x for x in page_moved if x not in ruled_moves]
    corrected = [t for t in ST.get('terminals') or [] if t['verdict'] == 'CORRECTED']
    rc = _relay_commits()
    e0c = _alone(RELAY, list(K.E0_FILES), rc)
    ver = RA.get('verify') or []
    S = {
        'H60a': (('HOLDS' if PR and not PR.get('beyond') and not PR.get('sorry') and any(x['name'] == K.RUNG_TERMINAL for x in PR.get('prints') or [])
                  else 'REFUTED'), 'prints %d, beyond the standard three %s, sorryAx %s' % (len(PR.get('prints') or []), PR.get('beyond'), PR.get('sorry'))),
        'H60b': (('HOLDS' if rg[0] == 'INTERFACES' and len(rg[2]) == 1 and 'PlattTrudgianHeight' in prem_types else 'REFUTED'),
                 'rh_upto_platt reads %s on %s' % (rg[0], prem_types)),
        'H60c': (('HOLDS' if not other_moves else 'REFUTED'), 'page grade cells moved %s; of them by the ruled corrections and clauses %s; others %s' % (
            page_moved or 'NONE', ruled_moves or 'NONE', other_moves or 'NONE')),
        'H60d': (('HOLDS' if new_shapes and all(v == 'FINITE' for v in new_shapes.values()) else 'REFUTED'), 'the rung`s nodes by the quantifier column: %s' % new_shapes),
        'N1': (('HELD' if PR and not PR.get('beyond') and not PR.get('sorry') else 'REFUTED'), 'prints beyond the standard three %s ; sorryAx %s' % (
            PR.get('beyond'), PR.get('sorry'))),
        'N2': (('HELD' if rg[0] == 'INTERFACES' and len(rg[2]) == 1 and 'PlattTrudgianHeight' in prem_types else 'REFUTED'), 'rh_upto_platt %s on %s' % (rg[0], prem_types)),
        'N3': (('HELD' if seam_ok and data_ok and len(others) <= 4 else 'REFUTED'), 'the seam node %s; the data nodes without h %s; other grades moved %d: %s' % (
            seam_ok, data_ok, len(others), others)),
        'N4': (('HELD' if len(corrected) <= 3 else 'REFUTED'), 'terminals needing a correction entry %d: %s' % (len(corrected), [t['name'] for t in corrected])),
        'N5': n5v,
        'S1': (('HELD' if len(e0c) == 1 and _after_lock(RELAY, e0c[0]) and ET.get('cases') and ET.get('cases') == ET.get('passing')
                and sorted((ET.get('control') or {}).get('failing') or []) == sorted(CONTROL_FAILING) else 'REFUTED'),
               'the rule and its test in one relay commit %s after the lock; the test %s of %s; the rule as it stood fails %s' % (
                   e0c, ET.get('passing'), ET.get('cases'), (ET.get('control') or {}).get('failing'))),
        'S2': (('HELD' if sorted(moved) == sorted(list(ruled) + [K.SEAM_ALSO]) else 'REFUTED'), 'grades moved: %s' % moved),
        'S3': (('HELD' if len(corrected) == 2 and len(jx('b626_section_rows.json').get('rows') or []) == 4 else 'REFUTED'),
               'terminals corrected %s; CORRESPONDENCE rows %s' % ([t['name'].split('.')[-1] for t in corrected],
                                                                   [(x['row'], x['supersedes']) for x in jx('b626_section_rows.json').get('rows') or []])),
        'S4': (('HELD' if rg[0] == 'INTERFACES' and PR and not PR.get('beyond') and g(K.KER, 'rev-parse', K.RUNG_TAG + '^{commit}').strip()
                and jx('b626_publisher.json').get('doi') == K.RECOLLECTION['doi'] else 'REFUTED'),
               'v0.22 at %s; the DOI read %s' % (g(K.KER, 'rev-parse', '--short=7', K.RUNG_TAG + '^{commit}').strip(), jx('b626_publisher.json').get('doi'))),
        'S5': (('HELD' if ver and all(v[1] == 'AGREE' for v in ver) and [v[0] for v in ver] == ['b624', 'b625', 'b626'] else 'REFUTED'),
               'the chain %s' % [(v[0], v[1]) for v in ver]),
    }
    put_json('b626_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b626 — lane three, act fifty-three under (R236): the Platt–Trudgian height as a named premise and the height pair at '
              'v0.22; the seam and data clauses; the section-variable terminals read; two gate work-orders entered')


def _T():
    src = _show(K.KER, K.RUNG_TAG, K.RUNG_FILE) or ''
    m = re.search(r'^def plattTrudgianT : ℝ := (.*)$', src, re.M)
    return m.group(1).strip() if m else '?'


def _title_entry():
    EN, ST = jx('b626_e0_nodes.json'), jx('b626_section_terminals.json')
    return ('## The Platt–Trudgian height as a named premise at v0.22, the height pair rh_upto at T = %s, INTERFACES on one structure; '
            'the seam and data clauses, %d grades moved; %d section-variable terminals read, %d corrected' % (
                _T(), len(EN.get('moved') or []), len(ST.get('terminals') or []), sum(t['verdict'] == 'CORRECTED' for t in ST.get('terminals') or [])))


def _finding_text():
    S, rl, EN, ET, ST = (jl(n) for n in ('b626_scores.json', 'b626_record_lines.json', 'b626_e0_nodes.json', 'b626_e0_test.json',
                                         'b626_section_terminals.json'))
    PR, PB, J, RA, PZ = jl('b626_prints.json'), jl('b626_publisher.json'), jl('b626_act_root.json'), jl('b626_root_arm.json'), jx('b626_page_zeta.json')
    SR, MR = jx('b626_section_rows.json'), jx('b626_seam_rows.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    tagc = g(K.KER, 'rev-parse', '--short=7', K.RUNG_TAG + '^{commit}').strip()
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b626 on the author’s ruling `(R236)` and the author’s two answers before the seal. Banks: relay `data/b626_publisher.txt`, '
         '`data/b626_build.txt`, `data/b626_prints.txt`, `data/b626_e0_diff.txt`, `data/b626_e0_test.txt`, `data/b626_e0_nodes.txt`, '
         '`data/b626_section_terminals.txt`, `data/b626_table_final.txt`, `data/b626_act_root.txt`, `data/b626_root_arm.txt`, '
         '`data/b626_author_answers.txt`. Nothing deposits.*', '',
         '**The rung** (`(R236)`(5), W-ORD-PLATT-RUNG, OPEN_TRAILS :12891, as the author answered before the seal): the publisher’s page '
         'read once -- the DOI %s, the journal %s, the height %s, beside the navigator’s recollection (%s, %s, T = %s). SIDE-explicit-formula '
         'v0.22 = %s adds SIDEExplicitFormula/PlattRung.lean: rh_upto T, every nontrivial zero with |Im ρ| ≤ T on the line; the height '
         'pair forall_rh_upto_iff_rh, (∀ T, rh_upto T) ↔ RiemannHypothesis, at no premise -- definitional, each zero having finite '
         'height, so it carries no analytic content and joins the rung to RiemannHypothesis by the quantifier alone; the structure '
         'PlattTrudgianHeight T carrying rh_upto T as a T1-lit premise; and the rung rh_upto_platt at T = %s, INTERFACES on that '
         'structure alone. Its weight is the premise’s and nothing else: the numerical tradition’s result enters the kernel as a named '
         'premise, not as a theorem of it. The finite side of the support pair, h2_sign_upto, is not instantiated -- its bound is a '
         'support bound, not a height (OPEN_TRAILS :%d). %d prints, beyond the standard three %s, sorryAx %s. H60a %s, H60b %s, H60d %s.' % (
             PB.get('doi'), PB.get('journal'), PB.get('heights') or 'not printed on the page', K.RECOLLECTION['journal'], K.RECOLLECTION['doi'],
             K.RECOLLECTION['T'], tagc, _T(), rl['lines'][3]['line'], len(PR['prints']), PR['beyond'] or 'none', 'present' if PR['sorry'] else 'absent',
             S['H60a'][0], S['H60b'][0], S['H60d'][0]), '',
         '**The three nodes** (`(R236)`(2), narrowed by the author’s answer before the seal): the rule reads a seam antecedent -- a named '
         'implication between open statements, entered by name and pin with its principle -- as a binder, and a data binder not at all '
         '(relay %s): the test %d of %d by its case pattern, the rule as it stood failing %s. Over the page nodes %d grades moved: %s. '
         'h2_sign_imp_rh_of_seam reads INTERFACES on rh_strip_imp_rh and its one DERIVES cell takes a dated correction (CORRESPONDENCE '
         'row %s); ch_iff_h2_sign_of_seam, the same seam, reads INTERFACES against its DERIVES cells, printed for the author’s ruling. '
         'The clause as first worded would have moved 14 plain implications more; measured before the seal, it was narrowed.' % (
             e0c, ET['passing'], ET['cases'], ET['control']['failing'], len(EN['moved']),
             ', '.join('%s %s' % (n.split('.')[-1], next((r['after'] for r in EN['rows'] if r['name'] == n), '?')) for n in EN['moved']),
             ', '.join(str(x['row']) for x in MR.get('rows') or [])), '',
         '**The section-variable terminals** (`(R236)`(4)): %d terminals in CriterionConverse’s scope that hχ and h1 reach, their grades not '
         'naming them -- each takes dated correction rows to INTERFACES on them (CORRESPONDENCE rows %s); the [NeZero N] instances domain '
         'conditions under clause (i).' % (len(ST['terminals']), ', '.join(str(x['row']) for x in SR.get('rows') or [])), '',
         '**The pages, the table and the root.** The ζ page re-emitted at v0.22 from a fresh probe, the rung’s nodes appended (shapes %s); '
         'the table regenerated: %s. The root of b626 over %d repositories, %d tags and %d banks; the chain verified, %s.' % (
             PZ.get('shapes'), '; '.join('%s %s' % (n.split('.')[-1], v) for n, v in (jx('b626_table_final.json').get('grades') or {}).items()) or 'no row moved',
             len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks']), ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The record lines** (`(R236)`(1)-(4)): b625’s weight at FINDINGS :%d; the seam and data clauses at OPEN_TRAILS :%d; the readings '
         'confirmed with the predicate-variable clause :%d; the pair’s mismatch beside the rung’s work-order :%d; W-ORD-GATE-FROM-ELABORATOR '
         ':%d and W-ORD-BINDER-GRAMMAR :%d, priced.' % tuple(x['line'] for x in rl['lines']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b559-b560’s support pair (DetectionRegion.lean) and finds its bound a '
         'support bound, not a height, so the rung at a published height needs a pair of its own; it re-reads b625’s three nodes for ruling '
         'and closes them under two clauses; and it gives b625’s section-variable finding its first corrections and its work-order. It '
         'strengthens the programme’s offering of a ladder whose rungs are carried at their honest grade, the numerical tradition’s '
         'certificate a named premise and never a theorem of the kernel.', '',
         '**Next.** Per `(R236)`(6): b627, W-ORD-MARGIN-BENCH (OPEN_TRAILS :12897). The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds, or that any zero lies off the line or on it beyond the '
         'published height the premise names.*', '']
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
    put_json('b626_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) the rung built as a height pair by the author’s answer, the structure a Prop carrying rh_upto at the published height '
              'as its one field and the height a definition beside it, so the terminal’s premise binder reads as a premise; (2) the seam '
              'clause entered with its one entry, rh_strip_imp_rh, and its principle; (3) a data binder read lexically as a number type, '
              'Prop or Type, an arrow chain of those or a Dirichlet character; (4) the section-variable terminals’ corrections as '
              'CORRESPONDENCE supersession rows, one per terminal and row superseded; (5) the carried b592 control re-run with the E0 rule '
              'loaded from its own pin; (6) the rung’s nodes appended at the end of b622’s ζ list, the pin moved to v0.22')


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b626_scores.json', 'b626_findings.json', 'b626_record_lines.json', 'b626_act_root.json'))
    EN, ST = jl('b626_e0_nodes.json'), jl('b626_section_terminals.json')
    SR, MR = jx('b626_section_rows.json'), jx('b626_seam_rows.json')
    rc = _relay_commits()
    e0c = (_alone(RELAY, list(K.E0_FILES), rc) or ['?'])[0]
    dis = EN.get('disagreements') or []
    rows_ = ['', TRAIL_HEAD, '',
             '**(R236) ratified.** (1) b625 at its weight. (2) The seam and data clauses, the seam narrowed by the author’s answer. (3) The '
             'three readings confirmed. (4) The section-variable terminals and two work-orders. (5) W-ORD-PLATT-RUNG, as a height pair by '
             'the author’s answer. (6) The act after: b627.', '',
             '**Entered:** FINDINGS.md:%d (b625’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the clauses), :%d (the readings), :%d (the '
             'pair’s mismatch, to :12891), :%d (W-ORD-GATE-FROM-ELABORATOR), :%d (W-ORD-BINDER-GRAMMAR); this record; relay tools/e0_rule.py '
             'and tools/test_e0_rule.py %s; SIDE-global-section CORRESPONDENCE rows %s; SIDE-explicit-formula v0.22 = %s.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                 rl['lines'][4]['line'], rl['lines'][5]['line'], e0c, ', '.join(str(x['row']) for x in (MR.get('rows') or []) + (SR.get('rows') or [])),
                 g(K.KER, 'rev-parse', '--short=7', K.RUNG_TAG + '^{commit}').strip()), '',
             '**Act root:** b626 `%s` (previous `%s`, b625’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**The author’s two answers before the seal** (relay data/b626_author_answers.txt): the rung -- %s; the arrow clause -- %s.' % (
                 answer_of(0)[:700], answer_of(1)[:900]), '',
             '**For the author’s ruling:** %s.' % ('; '.join('%s -- the table %s from its cells, the rule %s' % (x['name'], x['table'], x['rule'])
                                                           for x in dis) or 'no disagreement'), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b626_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R236)`(6), b627, W-ORD-MARGIN-BENCH (OPEN_TRAILS :12897); the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
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
    put_json('b626_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b626_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b626 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b626_defects.json -- NOTHING WRITTEN')
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
    put_json('b626_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def desk(*a):
    S = jl('b626_scores.json')
    L = ['=' * 104, 'b626 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H60a-H60d, (R236)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H60 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b626_defects.txt').rstrip(NL).split(NL)
    put_txt('b626_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b626_scores.json', 'b626_findings.json', 'b626_trail.json', 'b626_record_lines.json', 'b626_act_root.json'))
    EN, ST = jl('b626_e0_nodes.json'), jl('b626_section_terminals.json')
    L = ['b626 -- THE COMPONENTS, BANKED UNDER (R236).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b625`s closing push-out relay %s ; push-b625* branches deleted by '
         'name (data/b626_branches.txt) ; the suite, b625`s defects` sources repaired, run at HEAD before the face (data/b626_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b625`s weight FINDINGS :%d ; the clauses OPEN_TRAILS :%d ; the readings :%d ; the mismatch :%d ; the work-orders :%d, :%d' % (
             tuple(x['line'] for x in rl['lines'])),
         '### COMPONENT 2 : data/b626_e0_diff.txt ; data/b626_e0_test.txt ; data/b626_e0_nodes.txt (grades moved %d) ; the seam row data/b626_seam_rows.json' % len(EN['moved']),
         '### COMPONENT 3 : data/b626_section_terminals.txt (%d read, %d corrected) ; data/b626_section_rows.json' % (
             len(ST['terminals']), sum(t['verdict'] == 'CORRECTED' for t in ST['terminals'])),
         '### COMPONENT 4 : data/b626_publisher.txt ; data/b626_build.txt ; data/b626_prints.txt ; v0.22 ; H60a %s, H60b %s' % (S['H60a'][0], S['H60b'][0]),
         '### COMPONENT 5 : the ζ page at v0.22 (data/b626_page_zeta.json, data/b626_nodes_zeta.txt, data/b626_probe_out.txt) ; the table ; page arms '
         'data/b626_page_arms.txt ; the root %s ; the arm data/b626_root_arm.txt ; H60c %s, H60d %s' % (J['root'][:16], S['H60c'][0], S['H60d'][0]),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b627 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b626_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b626_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
