# -*- coding: utf-8 -*-
"""b632_record.py -- THE ACT'S RECORD TOOL, UNDER (R241). ### ONE SUBCOMMAND PER BANK.

### ### b632: LANE THREE, ACT FIFTY-EIGHT -- THE DEDEKIND ZETA OF ℚ(ζ_q) AS A CONFIGURATION OF THE SCHEMA, ITS TWO PREMISES NAMED,
### v0.25; THE NYMAN–BEURLING DIP RECORDED AS FINITE-RANGE DATA; THE MULTIPLICITY CONSTANT ENTERED AS A REGISTRY ITEM.
### Subcommands write only `data/b632_*` unless the docstring names another file; `dry` on the command line routes WRITES to the
### seat's scratchpad and never the reads. Banks are written by encode, temp file, `os.replace`; ledger appends through b566's
### guarded `append_to`. The data is tools/b632_worklist.py. The registry records of the bench are read by the seat once each, by
### curl with no header, into the scratchpad; this tool reads the captures and never calls a platform. The case counter is (R233)(3)'s.
### b628's full intake bank (relay data/b628_intake_crank_v0_5.txt) is never read here past its header, never staged or committed.
"""
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
import b604_record as R4  # noqa: E402
import b632_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/89dd14e7-e119-4cf8-b592-ceaac809eff2/scratchpad'
SESSION_ID = '89dd14e7-e119-4cf8-b592-ceaac809eff2'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
TABLE_FILES = ('terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json')
FACE = 'b632_registration_2026-10-05.txt'

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
_DJ = os.path.join(D, 'b632_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b632 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b632_defects.txt', L)


COUNT_CASE = r'^  \(\d+\) '


def count_cases(text, case_re=None):
    rx = re.compile(case_re or COUNT_CASE)
    cases = [l for l in (text or '').split(NL) if rx.search(l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the edition form, the precedence and authority orders, the build clause, the N5 line, the Dedekind work-order, '
         'W-ORD-TABLE-RULE-GRADES, the Nyman–Beurling and simplicity work-orders, b630`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
         [11864, 12012, 12228, 12354, 12356, 12799, 12893, 12895, 13133, 13135], 1500),
        ('FINDINGS: b630`s entry', PP, PRE_PP, 'FINDINGS.md', [7657], 600),
        ('SIDE-explicit-formula v0.24: the family, its sum lemma, its q = 3 form and the Dedekind reading`s two premises (Schema/Family.lean)',
         K.KER, 'v0.24', K.FAMILY_FILE, ('GREP', r'^(theorem|def|structure) (finsetSum|finsetSum_productLemma|finsetSum_target_iff|finsetSum_rhs|family|charCfg|familyConfig|FamilyTheorem|family_theorem|familyConfig_arith|family_three|family_three_statement|zeta_rhs_pole|TrivialSummandPremise|EulerFactorPremise|DedekindPremises)\b'), 300),
        ('SIDE-explicit-formula v0.21: the family`s first tag (Schema/Family.lean)', K.KER, 'v0.21', K.FAMILY_FILE,
         ('GREP', r'^(theorem|def|structure) (finsetSum_productLemma|family_theorem|family_three_statement|TrivialSummandPremise|EulerFactorPremise|DedekindPremises)\b'), 300),
        ('SIDE-explicit-formula v0.24: the product lemma (Product.lean)', K.KER, 'v0.24', 'SIDEExplicitFormula/Product.lean',
         ('GREP', r'^(theorem|def) (sum|sum_rhs|sum_target|ProductLemma|productLemma_holds)\b'), 300),
        ('SIDE-explicit-formula v0.24: the ζ configuration`s pole term (Schema/Instances.lean)', K.KER, 'v0.24', 'SIDEExplicitFormula/Schema/Instances.lean',
         ('GREP', r'^def zetaWeilConfig|poleTerm k'), 300),
        ('SIDE-explicit-formula v0.24: the house module form (NymanBeurling.lean)', K.KER, 'v0.24', 'SIDEExplicitFormula/NymanBeurling.lean',
         [1, 2, 3, 4, 5, 25, 26, 27, 28, 29, 30, 31, 32], 200),
        ('relay data/b630_nb_bench.txt: the rows N = 40-49', RELAY, PRE_RELAY, 'data/b630_nb_bench.txt', ('GREP', r'^4\d \| '), 200),
        ('relay data/b630_defects.txt', RELAY, PRE_RELAY, 'data/b630_defects.txt', ('GREP', r'^    \('), 300),
        ('relay data/b630_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b630_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b632 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        if rev is None:      # ### a file read on disk (the local bank), never by git: it is in no commit
            at = 'disk (untracked)'
            p = os.path.join(ROOT, *path.split('/'))
            t = io.open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else None
        else:
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
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                         g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b632_reads.txt', L)


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R241) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
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
    L = ['### b632 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b632_author_answers.txt', L)


def answer_of(k):
    """### the author's answer to the act's k-th prompt (0-based, across calls), whole: cut from the result after its own question's
    ### `"<question>"="` and before the next question's `", "<question>"="`, the questions read from the bank's prompt headers."""
    t = rd('b632_author_answers.txt')
    qs = []
    for blk in re.split(r'^### CALL ', t, flags=re.M)[1:]:
        res = re.search(r'^RESULT \(transcript line \d+\): (.*)', blk, re.M | re.S)     # ### the result runs to the call's end
        for q in re.findall(r'^### PROMPT \d+ \([^)]*\): (.*)$', blk, re.M):
            qs.append((q, ' '.join(res.group(1).split()) if res else ''))
    if len(qs) <= k:
        return 'no answer banked'
    q, r = qs[k]
    a = r.find('"%s"="' % q)
    if a < 0:
        return 'no answer banked'
    a += len(q) + 4
    ends = [r.find('", "%s"="' % q2, a) for q2, r2 in qs if r2 == r and q2 != q] + [r.find('". You can now continue', a), r.find('". Read the answers', a)]
    ends = [e for e in ends if e >= 0]
    return r[a:min(ends)].strip() if ends else r[a:].strip()


def _elide(text):
    """### the author's answer as banked, a sentence carrying one of the scanner's own stems elided and marked so, never reworded."""
    import banned_terms as BT
    rx = re.compile(r'(%s)' % '|'.join(re.escape(s) for s in BT.STEMS), re.I)
    return ' '.join('[a sentence elided here under the scanner’s stem rule, verbatim in the bank]' if rx.search(s) else s
                    for s in re.split(r'(?<=[.;])\s+', text))


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
         'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map')
KERN_PIN = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7',
            'SIDE-cosmo': 'c5cba30', 'SIDE-structural-error-correction': '6bf19ab', 'SIDE-global-section': '17ce9ff'}
WRITTEN_KERNS = ('SIDE-explicit-formula',)   # ### the one this act writes: the instance, on its branch and tag


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
    put_json('b632_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE LEDGER HELPERS
def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def predict_cells(text, ledger):
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
    p = os.path.join(SP if DRY else D, 'b632_scanfile_%s.md' % name)
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
W_HEAD = '*Appended 2026-10-05 by b632 to b630’s entry (:%d), under `(R241)`(1)-(2) -- b630 AT ITS WEIGHT, AND THE DIP READ:*'
CR_HEAD = '*Appended 2026-10-05 by b632 to b630’s record (:%d), under `(R241)`(1) -- A COMMIT SUBJECT CORRECTED BY A DATED ENTRY:*'
BB_HEAD = '*Appended 2026-10-05 by b632 to W-ORD-NYMAN-BEURLING-FACE (:%d), under `(R241)`(2) -- AN ITEM, THE CONJECTURE’S RECORD:*'
MU_HEAD = '*Appended 2026-10-05 by b632 to W-ORD-NYMAN-BEURLING-FACE (:%d), under `(R241)`(2) -- AN ITEM, THE MULTIPLICITY FORM OF THE CONSTANT, REGISTRY-READ:*'
MS_HEAD = '*Appended 2026-10-05 by b632 to W-ORD-SIMPLICITY-FACE (:%d), under `(R241)`(2) -- AN ITEM CROSS-ENTERED, REGISTRY-READ, NOT ASSERTED:*'


def _weight():
    return ('\n%s the kernel’s d_N² for N = 1 … 100 at 128 bits in Arb balls, two runs byte for byte; d_N² decreasing at every step, '
            'certified (distN_antitone reproduced numerically); d_2² = 1 − log 2 exact, d_100² = 0.0102019; against 2λ₁ = 0.0461914 (the '
            'kernel’s liCoeff_one_keiper, the identity 2λ₁ = 2 + γ − log 4π checked in balls), d_N² · log N certified below at N = 41 to '
            '48, lowest 0.04543 at N = 42, and above everywhere else from 2 to 100; the Gram entries cross-checked as plain sums of step '
            'functions in t = 1/x to about 4e-7; N_max the cap of 100. THE DIP, READ (`(R241)`(2)): Burnol’s inequality bounds a lim inf, '
            'and a lim inf says nothing about N = 42; the finite values oscillate about the constant and the bench found one excursion '
            'below it in a hundred -- finite-range data, no inference beyond N = 100, the bench’s no-claim sentence standing; the '
            'expectation that refuted was the navigator’s reading of a lim inf as a finite-range bound. The table: the rows of v0.24 from '
            'the rule (8 DEF, 4 graded without hypothesis, 1 on its named premise), 208 by cells, 1786 ungraded, the 1799 rule readings '
            'banked as W-ORD-TABLE-RULE-GRADES’ input (:13133). The probe prints its reading; the refusal beneath the hold stands since '
            'b568. The suite 84 of 85, the conjecture’s registry search returning no record. Relay 67c8b477; PLACE-papers 056fb19; the '
            'root a31a76c6…, b624 to b630 agreeing. Nothing deposited; no kernel touched.\n' % (W_HEAD % K.B630_ENTRY))


def _subject_fix():
    return ('\n%s relay 02a5d5f1, the table’s housekeeping commit of b630, says the rows of v0.24 read nine DEF; they read 8 DEF, 4 graded '
            'without hypothesis and 1 on its named premise (relay data/b630_table_final.txt). The commit stands as written; this entry is '
            'the correction (b630’s defect (d)).\n' % (CR_HEAD % K.B630_RECORD))


def _bbls():
    return ('\n%s Báez-Duarte, Balazard, Landreau and Saias, “Notes sur la fonction ζ de Riemann, 3”, Advances in Mathematics, 2000 -- '
            'the citation as the author gives it; b630’s arXiv search returned no record of it (relay data/b630_nb_inputs.txt), and a '
            'registry read of the journal’s record is the item. Price: one read in an act that reads registries. Not started.\n' % (BB_HEAD % K.NB_LINE))


def _multiplicity():
    return ('\n%s the recollection, to be read from the record and not copied: Burnol’s constant is a sum over the distinct zeros of '
            'the squared multiplicity over the squared modulus, which equals the sum of 1/|ρ|², that is 2λ₁, exactly when every zero is '
            'simple. If the record bears it, the face’s constant carries the simplicity clause: the conjectured rate at 2λ₁ would say more '
            'than RH, and the limit of d_N² · log N, if it exists, sees multiplicity. Registry-read, not asserted; cross-entered on '
            'W-ORD-SIMPLICITY-FACE (:12012). Not started.\n' % (MU_HEAD % K.NB_LINE))


def _simplicity():
    return ('\n%s the multiplicity form of Burnol’s constant on the Nyman–Beurling face (entered at W-ORD-NYMAN-BEURLING-FACE), a '
            'connection between the fourth face and the simplicity statements of v0.17 and v0.19, to be read from the record before it is '
            'entered anywhere else. The kernel’s positivity_not_imp_simplicity stands as it is; this item does not touch it.\n' % (MS_HEAD % K.SIMPLICITY_LINE))


def record_lines(*a):
    """### FINDINGS: b630's weight with the dip's reading (to :7657). OPEN_TRAILS: the commit-subject correction (to b630's record :13135);
    ### the conjecture's record and the multiplicity form (to :12893); the multiplicity item cross-entered (to :12012)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The Nyman–Beurling distances d_N²')
    if entry != K.B630_ENTRY:
        sys.exit('### b630`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B630_ENTRY, _weight()), ('OPEN_TRAILS.md', CR_HEAD % K.B630_RECORD, _subject_fix()),
             ('OPEN_TRAILS.md', BB_HEAD % K.NB_LINE, _bbls()), ('OPEN_TRAILS.md', MU_HEAD % K.NB_LINE, _multiplicity()),
             ('OPEN_TRAILS.md', MS_HEAD % K.SIMPLICITY_LINE, _simplicity())]
    cells, nd, clean = _guarded(items, 'OPEN_TRAILS.md', 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    print('  backtick parity odd in: %s' % (ticks or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean or ticks:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b632_record_lines.json', K.B630_ENTRY)


# ================================================================================ COMPONENT 2: THE KERNEL READ
def _decl_block(src, name):
    m = re.search(r'^(?:theorem|def|noncomputable def|abbrev|structure|instance) %s\b' % re.escape(name), src, re.M)
    if not m:
        return None, None
    line = src[:m.start()].count(NL) + 1
    rest = src[m.start():]
    end = rest.find(':=')
    w = rest.find('where')
    cut = min([x for x in (end, w) if x >= 0] or [400])
    return line, ' '.join(rest[:cut].split())


def dedekind_read(*a):
    """### before any module: the family's declarations at v0.24 by file and line, their presence at v0.21; Product.lean's lemma; the
    ### ζ configuration's pole term; the premise the product needs at p | q as the kernel states it; the split's two statements as they
    ### will be written (data/b632_dedekind_read.txt and .json)."""
    out = {}
    L = ['b632 -- COMPONENT 2, (R241)(3): THE KERNEL READ, BEFORE ANY MODULE (%s)' % utc(), '']
    fam24, fam21 = _show(K.KER, 'v0.24', K.FAMILY_FILE) or '', _show(K.KER, 'v0.21', K.FAMILY_FILE) or ''
    L.append('### %s at v0.24 (%s) and at v0.21 (%s):' % (K.FAMILY_FILE, g(K.KER, 'rev-parse', '--short=7', 'v0.24^{commit}').strip(),
                                                         g(K.KER, 'rev-parse', '--short=7', 'v0.21^{commit}').strip()))
    for n in K.FAMILY_READ:
        ln, st = _decl_block(fam24, n)
        ln21, _s = _decl_block(fam21, n)
        out[n] = dict(line=ln, statement=st, at_v021=ln21 is not None)
        L.append('    :%-5s %s   [at v0.21: %s]' % (ln, (st or '### NOT DECLARED')[:230], 'present' if ln21 else 'absent'))
    prod = _show(K.KER, 'v0.24', 'SIDEExplicitFormula/Product.lean') or ''
    L += ['', '### SIDEExplicitFormula/Product.lean at v0.24:']
    for n in ('sum', 'sum_rhs', 'sum_target', 'ProductLemma', 'productLemma_holds'):
        ln, st = _decl_block(prod, n)
        out['Product.' + n] = dict(line=ln, statement=st)
        L.append('    :%-5s %s' % (ln, (st or '### NOT DECLARED')[:230]))
    inst = _show(K.KER, 'v0.24', 'SIDEExplicitFormula/Schema/Instances.lean') or ''
    pl = [i + 1 for i, l in enumerate(inst.split(NL)) if 'poleTerm k' in l]
    L += ['', '### the ζ configuration`s pole term at its definition: SIDEExplicitFormula/Schema/Instances.lean :%s -- %s' % (
        pl[:1], (inst.split(NL)[pl[0] - 1].strip() if pl else '### NOT FOUND'))]
    out['pole_line'] = pl[:1]
    L += ['', '### WHAT THE DEDEKIND PRODUCT NEEDS AT p | q, AS THE KERNEL STATES IT (EulerFactorPremise, above): every non-trivial character '
          'mod q, imprimitive ones included, with its primitive inducer`s arithmetic side; and the trivial summand in the family`s form '
          '(TrivialSummandPremise). The act extends them and does not re-declare them.',
          '', '### THE SPLIT, BY THE AUTHOR`S ANSWER BEFORE THE SEAL (data/b632_author_answers.txt), THE STATEMENTS TO BE WRITTEN:',
          '    DedekindConfig q := Product.sum zetaWeilConfig (familyConfig q) -- the trivial summand ζ`s configuration, its pole term carried',
          '    dedekind_instance : h2_sign_cfg (DedekindConfig q) ↔ zetaWeilConfig.target ∧ ∀ χ ∈ family q, GRH_chi χ.primitiveCharacter -- no premise',
          '    dedekind_rhs (hT : TrivialSummandPremise) (hE : EulerFactorPremise q) (k) : (DedekindConfig q).rhs k = (the trivial summand in '
          'the family`s form) + ∑ χ ∈ family q, (archTerm_chi χ k − primeSum_chi χ k) -- each character at its own level, both premises used',
          '    dedekind_three : DedekindTheorem 3 = (the statement at q = 3) -- rfl']
    put_txt('b632_dedekind_read.txt', L)
    put_json('b632_dedekind_read.json', dict(at=utc(), decls=out))
    print('  declarations read %d ; missing %s' % (len(out), [n for n, v in out.items() if isinstance(v, dict) and v.get('line') is None] or 'NONE'))


# ================================================================================ COMPONENT 3: THE INSTANCE
def build_bank(prefix, name, *a):
    """### the detached build calls' watchdog logs (scratchpad <prefix>_<n>.log), banked: data/<name>.txt and .json."""
    calls = []
    L = ['b632 -- THE DETACHED BUILD CALLS AT THE HOLD, %s (%s), one target per call, watched from the foreground' % (prefix, utc()), '']
    for f in _logs(prefix):
        t = io.open(os.path.join(SP, f), encoding='utf-8', errors='replace').read()
        st = re.search(r'^### START (\S+) free (\d+) MB pid (\d+) cmd (.*?) cwd', t, re.M)
        ex = re.search(r'^### EXIT (-?\d+) (\S+) (\d+) s peak (-?\d+)', t, re.M)
        errs = [l for l in t.split(NL) if re.search(r'\berror\b', l, re.I) and not l.startswith('###')]
        low = min([int(x) for x in re.findall(r'^### SAMPLE \S+ free (\d+) MB', t, re.M)] or [-1])
        calls.append(dict(log=f, start=st.group(1) if st else None, free=int(st.group(2)) if st else None, cmd=st.group(4) if st else None,
                          rc=int(ex.group(1)) if ex else None, secs=int(ex.group(3)) if ex else None, low=low, errors=errs[:5]))
        L.append('### %s : %s ; started %s, free %s MB ; exit %s after %s s ; lowest sampled free %s MB ; errors %d' % (
            f, calls[-1]['cmd'], calls[-1]['start'], calls[-1]['free'], calls[-1]['rc'], calls[-1]['secs'], low, len(errs)))
        L += ['    ' + e[:200] for e in errs[:5]]
    L += ['', '### ### **CALLS %d ; ELAPSED %d s IN ALL.**' % (len(calls), sum(c['secs'] or 0 for c in calls))]
    put_txt(name + '.txt', L)
    put_json(name + '.json', dict(at=utc(), calls=calls))
    print(L[-1])


def _logs(prefix):
    return sorted((f for f in os.listdir(SP) if f.startswith(prefix + '_') and f.endswith('.log')), key=lambda f: int(re.findall(r'_(\d+)\.log$', f)[0]))


STD = {'propext', 'Classical.choice', 'Quot.sound'}


def _parse_prints(t):
    return [dict(name=m.group(1), axioms=[x.strip() for x in (m.group(2) or '').split(',') if x.strip()])
            for m in re.finditer(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", t)]


def face_prints(log, *a):
    t = io.open(log, encoding='utf-8', errors='replace').read()
    pr = _parse_prints(t)
    bad = [x['name'] for x in pr if set(x['axioms']) - STD]
    names = [x['name'] for x in pr]
    missing = [n for n in K.FACE_NODES if n not in names]
    L = ['b632 -- COMPONENT 3: THE AXIOM PRINTS OF %s AT %s (%s)' % (K.AXCHECK_FILE, K.FACE_BRANCH, utc()), '']
    L += ['  %-62s %s' % (x['name'], x['axioms'] or 'no axioms') for x in pr]
    L += ['', '### ### **PRINTS %d ; BEYOND THE STANDARD THREE %s ; FACE NODES NOT PRINTED %s ; sorryAx %s.**' % (
        len(pr), bad or 'NONE', missing or 'NONE', 'PRESENT' if 'sorryAx' in t else 'ABSENT')]
    put_txt('b632_prints.txt', L)
    put_json('b632_prints.json', dict(at=utc(), prints=pr, beyond=bad, missing=missing, sorry='sorryAx' in t))
    print(L[-1])


def _face_src(rev):
    return _show(K.KER, rev, K.FACE_FILE) or ''


def face_grades(*a):
    """### the instance's terminals graded by the shared E0 rule from their source headers at the tag (or the branch); dedekind_three's
    ### proof read; the kernel's files changed against v0.24 (data/b632_face.txt and .json)."""
    import e0_rule as E
    rev = K.FACE_TAG if _face_src(K.FACE_TAG) else K.FACE_BRANCH
    src = _face_src(rev)
    out = {}
    for n in K.FACE_NODES:
        short = n.split('.')[-1]
        m = re.search(r'^(theorem|def|structure|abbrev) %s\b(.*?)(:=|where)' % re.escape(short), src, re.M | re.S)
        kind = m.group(1) if m else None
        head = ' '.join(m.group(2).split()) if m else ''
        gr = E.grade(head, 'theorem') if kind == 'theorem' else ('DEF' if kind else None, '', [])
        out[short] = dict(kind=kind, grade=gr[0], why=gr[1], binders=[b for b, _t in gr[2]] if gr and gr[2] else [])
    three = re.search(r'^theorem dedekind_three\b.*?:=\s*(\S+)', src, re.M | re.S)
    files = sorted(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, rev).split(NL) if x.strip())
    sorry = len(re.findall(r'\bsorry\b', re.sub(r'--[^\n]*', '', re.sub(r'/-.*?-/', '', src, flags=re.S))))
    L = ['b632 -- COMPONENT 3: THE INSTANCE`S NODES GRADED BY THE SHARED E0 RULE AT %s (%s)' % (rev, utc()), '']
    L += ['  %-22s %-9s %-16s %s' % (k, v['kind'], v['grade'], v['why'][:140]) for k, v in out.items()]
    L += ['', '### dedekind_three`s proof term: %s' % (three.group(1) if three else '### NOT READ'),
          '### the kernel`s files changed against v0.24: %s ; sorry tokens in the module %d' % (files, sorry), '',
          '### ### **dedekind_instance %s ; dedekind_rhs %s ON %s ; dedekind_three %s BY %s.**' % (
              out.get('dedekind_instance', {}).get('grade'), out.get('dedekind_rhs', {}).get('grade'), out.get('dedekind_rhs', {}).get('why', '')[:120],
              out.get('dedekind_three', {}).get('grade'), three.group(1) if three else None)]
    put_txt('b632_face.txt', L)
    put_json('b632_face.json', dict(at=utc(), rev=rev, nodes=out, three_proof=three.group(1) if three else None, files=files, sorry=sorry))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE CHI LIST AND PAGE
def nodes_new(*a):
    """### the χ node list at v0.25: b622's list (every record line unchanged), the pin moved to v0.25, the instance's nodes placed directly
    ### after DedekindPremises, one backmatter record (data/b632_nodes_chi.txt)."""
    src = rd(K.NODES['chi']).rstrip(NL).split(NL)
    if '# pin: v0.21' not in src:
        sys.exit('### b622`S LIST CARRIES NO `# pin: v0.21` LINE -- NOTHING WRITTEN')
    head = ['# b632 -- THE χ NODE LIST AT v0.25, (R241)(3) and the author`s answer before b632`s seal: b622`s list (relay',
            '# data/b622_nodes_chi.txt, every record line unchanged), the pin moved to v0.25; the Dedekind instance`s nodes placed',
            '# directly after DedekindPremises; one backmatter record. Every cell is elaborated by the generator`s probe at the pin.', '#']
    body = [('# pin: v0.25' if l == '# pin: v0.21' else l) for l in src]
    at = max(i for i, l in enumerate(body) if l.startswith('SIDEExplicitFormula.Schema.Family.DedekindPremises |'))
    why = ('the summed configuration with the trivial summand, ζ`s, its pole term carried', 'the instance`s statement as a Prop',
           'Weil positivity of the summed configuration exactly when RH and every family target hold, no premise',
           'the summed arithmetic side as the Dedekind reading`s, on the two premises', 'the statement at q = 3, by rfl')
    adds = ['%s | kernel | added: (R241)(3), %s' % (n, w) for n, w in zip(K.FACE_NODES, why)]
    out = head + body[:at + 1] + adds + body[at + 1:] + ['# backmatter: ' + K.BACKMATTER]
    put_txt(K.NEW_NODES_CHI, out)
    print('  records carried %d ; inserted %d ; backmatter 1' % (len([l for l in body if l and not l.startswith('#')]), len(adds)))


def page_new(*a):
    """### ONE call in the foreground: the χ page at v0.25 from the new list by a fresh probe (the generator refuses beneath the hold and
    ### prints its reading); the probe's output banked as data/b632_chi_probe_out.txt; the page written where it changed."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    pd = os.path.join(SP, '_b632_probe')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NEW_NODES_CHI), pd, None)
    secs = int(time.time() - t0)
    po = os.path.join(pd, 'chain_page_probe_out.txt')
    if os.path.exists(po) and not DRY and rc == 0:
        _write(os.path.join(D, K.NEW_PROBE_CHI), open(po, 'rb').read().replace(b'\r\n', b'\n'))
    if rc:
        put_json('b632_page_chi.json', dict(rc=rc, log=log, at=utc(), seconds=secs))
        sys.exit('### χ RE-EMIT AT v0.25 FAILED, exit %d: %s' % (rc, log))
    _page_write('chi', pg, fm, secs, rc)


def chilist():
    if os.path.exists(_r(K.NEW_NODES_CHI)) and os.path.exists(_r(K.NEW_PROBE_CHI)):
        return K.NEW_NODES_CHI, K.NEW_PROBE_CHI
    return K.NODES['chi'], K.PROBE['chi']


def zlist():
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


def _page_write(k, pg, fm, secs, rc):
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = _grade_cells(prev.decode('utf-8')), _grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb and not n.startswith('tier:'))
    tmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n) and n in ga and n in gb and n.startswith('tier:'))
    put_json('b632_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, grade_cells=len(gb),
                                           grade_cells_moved=gmoved, tier_cells_moved=tmoved, dry=DRY, at=utc(), free_mb_before=fm, seconds=secs))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d ; grade cells %d, moved %s ; tier cells moved %s' % (
        k, rc, changed, secs, len(dl), len(gb), gmoved or 'NONE', tmoved or 'NONE'))
    for x in dl[:24]:
        print('    ' + x[:240])


def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked list and probe."""
    import chain_page as CP
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = zlist() if k == 'zeta' else chilist()
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b632_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    if rc:
        put_json('b632_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    _page_write(k, pg, fm, secs, rc)


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b632 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        nl, pr = zlist() if k == 'zeta' else chilist()
        r = GCP.arm(os.path.join(D, nl), os.path.join(SP, '_b632_gcp'), os.path.join(D, pr))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', nl, r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
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
    put_txt('b632_page_arms.txt', L)
    for l in L:
        print(l[:240])


def _table_grades():
    T = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    tg = {}
    for r in T['rows']:
        tg.setdefault(r['name'], r['grade'])
    return tg


def table(*a):
    before = _table_grades()
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    moved = [f for f in TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    tg = _table_grades()
    ch = [(x[1] if isinstance(x, list) else x) for x in diff.get('changed') or []]
    gmoved = sorted(n for n in set(before) | set(tg) if before.get(n) != tg.get(n))
    tag = a[0] if a and a[0] != 'dry' else 'table'
    L = ['b632 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows added %d ; gone %d ; grade-or-profile changed %d' % (len(diff.get('added') or []), len(diff.get('gone') or []), len(ch)),
         '### the rows changed, with the grade each now reads:']
    L += ['  %-62s %s' % (n, tg.get(n)) for n in ch] or ['  NONE']
    L += ['### the table files that moved against relay HEAD: %s' % (moved or 'NONE'), '',
          '### ### **THE GRADE COLUMN`S DIFF, THE TABLE BEFORE THIS RUN AGAINST AFTER IT : %s.**' % ('; '.join('%s %s -> %s' % (
              n.split('.')[-1], before.get(n), tg.get(n)) for n in gmoved) or 'EMPTY')]
    name = 'b632_table_%s.txt' % tag
    put_txt(name, L)
    put_json(name.replace('.txt', '.json'), dict(at=utc(), rc=r.returncode, added=diff.get('added') or [], gone=diff.get('gone') or [],
                                                 changed=ch, grade_moved=gmoved, files_moved=moved))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b632_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b632_') and os.path.isfile(os.path.join(D, f))
                  and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b632'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print('\n'.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import act_root as AR
    res = AR.verify()
    J = jl('b632_act_root.json')
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
    L = ['b632 -- COMPONENT 6: THE ACT-ROOT ARM, RUN (%s)' % utc(), '']
    L += ['  %s %s %s' % (act, v, '; '.join(why)) for act, v, why in res]
    L += ['', '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s) ; '
              'the copy`s root differs %s' % (bank, r2, same, J['root'], r2 != J['root']),
          '', '### ### **ACTS %d ; AGREE %d ; THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (
              len(res), sum(v == 'AGREE' for _a, v, _w in res), same == J['root'], r2 != J['root'])]
    put_txt('b632_root_arm.txt', L)
    put_json('b632_root_arm.json', dict(at=utc(), verify=[list(x) for x in res], bank=bank, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md',
            'day1/A_Place_to_Stand_v5_18.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md')
HKEYS = ('H65a', 'H65b', 'H65c', 'H65d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK


def _relay_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(RELAY, 'log', '--reverse', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _alone(repo, files, commits):
    return [h for h, s in commits if _files(h, repo) == sorted(files)]


def sorry_tokens(rev='main'):
    n = 0
    for f in g(K.KER, 'ls-tree', '-r', '--name-only', rev).split(NL):
        if f.endswith('.lean'):
            t = _show(K.KER, rev, f) or ''
            t = re.sub(r'/-.*?-/', '', t, flags=re.S)
            t = re.sub(r'--[^\n]*', '', t)
            n += len(re.findall(r'\bsorry\b', t))
    return n


def _statement_lines_changed():
    """### every .lean file that existed at v0.24 and changed in the explicit-formula kernel since, its code lines (comments and
    ### docstrings stripped) before and after: the files whose code differs. A file the act creates is not a changed statement."""
    out = []
    for f in [x for x in g(K.KER, 'diff', '--name-only', '--diff-filter=M', K.PRE_KER, 'main').split(NL) if x.strip().endswith('.lean')]:
        def code(t):
            t = re.sub(r'/-.*?-/', '', t or '', flags=re.S)
            return [l.rstrip() for l in re.sub(r'--[^\n]*', '', t).split(NL) if l.strip()]
        if code(_show(K.KER, K.PRE_KER, f)) != code(_show(K.KER, 'main', f)):
            out.append(f)
    return out


def n5(trail_line=None, ot=None, *a):
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
    face = jl('b632_kernels_face.json')['kernels']
    now = kern_state(list(face))
    others_ok = all(now[k] == list(v) for k, v in face.items() if k not in WRITTEN_KERNS)
    st = sorry_tokens('main')
    ker_files = sorted(set(x for x in g(K.KER, 'diff', '--name-only', K.PRE_KER, 'main').split(NL) if x.strip()))
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])
    want_pp = sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + [K.PNAME[k] for k in ('zeta', 'chi') if g(PP, 'diff', '--name-only', PRE_PP, 'HEAD', '--', K.PNAME[k]).strip()]))
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not os.path.basename(x).startswith(('b632_', 'audit_b632_', 'terminal_table'))
              and x not in {'data/b630_closing_push_out.txt', 'data/act_roots.txt'}]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ker_ok = ker_files == sorted([K.FACE_FILE, K.AXCHECK_FILE])
    ok = others_ok and st == 0 and ker_ok and pp_ch == want_pp and not beyond and rec_ok and not tracked_local and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; the kernels this act does not write unmoved %s; sorry tokens on the explicit-formula main %d (comments '
            'stripped); the explicit-formula kernel`s files changed %s; PLACE-papers %s; %s; relay beyond the list: %s; b628`s local intake '
            'bank in any relay commit %s, untracked now %s; no registry read this act, so no outbound request' % (
                others_ok, st, ker_files or 'NONE', pp_ch, rec_state, beyond or 'NONE', tracked_local, untracked_local))


def scores(*a):
    FG, PR, PX, PZ = jx('b632_face.json'), jx('b632_prints.json'), jx('b632_page_chi.json'), jx('b632_page_zeta.json')
    TF, RA, RL, KB = jx('b632_table_final.json'), jx('b632_root_arm.json'), jx('b632_record_lines.json'), jx('b632_build.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    nodes = FG.get('nodes') or {}
    inst, rhs, three = nodes.get('dedekind_instance') or {}, nodes.get('dedekind_rhs') or {}, nodes.get('dedekind_three') or {}
    std_ok = bool(PR) and not PR.get('beyond') and not PR.get('sorry') and not PR.get('missing')
    rhs_ok = (rhs.get('grade') or '').startswith('INTERFACES') and sorted(rhs.get('binders') or []) == ['hE', 'hT'] \
        and all(p in (rhs.get('why') or '') for p in K.PREMISES)
    three_ok = FG.get('three_proof') == 'rfl'
    moved = (PZ.get('grade_cells_moved') or []) + (PX.get('grade_cells_moved') or [])
    others = [x for x in moved if not any(x.endswith(n) for n in K.FACE_NODES)]
    T = json.load(io.open(_r('terminal_table.json'), encoding='utf-8'))
    rule = set(r['name'] for r in T['rows'] if r.get('provenance') == 'rule')
    tmoved_bad = [n for n in (TF.get('grade_moved') or []) if n not in rule]
    chi_t = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.DIR_PAGE], capture_output=True).stdout).decode('utf-8')
    lines = RL.get('lines') or []
    landed = len(lines) == 5 and all(x.get('line') for x in lines)
    calls = KB.get('calls') or []
    ver = RA.get('verify') or []
    S = {
        'H65a': (('HOLDS' if std_ok else 'REFUTED'), 'prints %d, beyond the standard three %s, sorryAx %s, nodes not printed %s' % (
            len(PR.get('prints') or []), PR.get('beyond'), PR.get('sorry'), PR.get('missing'))),
        'H65b': (('HOLDS' if rhs_ok else 'REFUTED'), 'scored on dedekind_rhs by the author`s answer: %s on %s' % (rhs.get('grade'), rhs.get('why'))),
        'H65c': (('HOLDS' if three_ok else 'REFUTED'), 'dedekind_three`s proof term %s' % FG.get('three_proof')),
        'H65d': (('HOLDS' if not others and not tmoved_bad else 'REFUTED'), 'page grade cells moved beyond the instance`s %s; table rows moved '
                 'that the table does not mark rule %s' % (others or 'NONE', tmoved_bad or 'NONE')),
        'N1': (('HELD' if std_ok else 'REFUTED'), 'as H65a; the two premises Props, not axioms'),
        'N2': (('HELD' if (inst.get('grade') or '').startswith('INTERFACES') and three_ok else 'REFUTED'),
               'dedekind_instance reads %s (no premise, by the author`s answer); dedekind_three by %s' % (inst.get('grade'), FG.get('three_proof'))),
        'N3': (('HELD' if all(('`%s`' % n) in chi_t for n in K.FACE_NODES) and not others else 'REFUTED'),
               'the χ page carries the instance`s nodes %s; other grade cells moved %s' % (all(('`%s`' % n) in chi_t for n in K.FACE_NODES), others or 'NONE')),
        'N4': (('HELD' if landed and 'Registry-read, not asserted' in _multiplicity() and 'REGISTRY-READ, NOT ASSERTED' in MS_HEAD else 'REFUTED'),
               'the record lines landed %s; the multiplicity item marked registry-read on both trails' % [x.get('line') for x in lines]),
        'N5': n5v,
        'S1': (('HELD' if (inst.get('grade') or '') == 'DERIVES' else 'REFUTED'), 'dedekind_instance reads %s' % inst.get('grade')),
        'S2': (('HELD' if calls and all((c.get('free') or 0) >= 2560 for c in calls) and calls[-1].get('rc') == 0 else 'REFUTED'),
               'build calls %s' % [(c.get('cmd'), c.get('free'), c.get('rc'), c.get('low')) for c in calls]),
        'S3': (('HELD' if K.BACKMATTER[:60] in chi_t else 'REFUTED'), 'the backmatter line on the χ page %s' % (K.BACKMATTER[:60] in chi_t)),
        'S4': (('HELD' if not PZ.get('changed') else 'REFUTED'), 'the ζ page changed %s' % PZ.get('changed')),
        'S5': (('HELD' if ver and all(v[1] == 'AGREE' for v in ver) and [v[0] for v in ver] == ['b624', 'b625', 'b626', 'b627', 'b628', 'b629', 'b630', 'b632'] else 'REFUTED'),
               'the chain %s' % [(v[0], v[1]) for v in ver]),
    }
    put_json('b632_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


# ================================================================================ COMPONENT 5: THE RECORD
TRAIL_HEAD = ('### b632 — lane three, act fifty-eight under (R241): the Dedekind zeta of ℚ(ζ_q) as a configuration of the schema at v0.25; '
              'the Nyman–Beurling dip as finite-range data; the multiplicity constant as a registry item')


def _title_entry():
    FG = jx('b632_face.json')
    n = FG.get('nodes') or {}
    return ('## The Dedekind zeta of ℚ(ζ_q) as a configuration of the schema at v0.25: dedekind_instance %s with no premise, dedekind_rhs '
            '%s on TrivialSummandPremise and EulerFactorPremise, dedekind_three by %s; the Nyman–Beurling dip at N = 41–48 as finite-range '
            'data' % ((n.get('dedekind_instance') or {}).get('grade'), (n.get('dedekind_rhs') or {}).get('grade'), FG.get('three_proof')))


def _finding_text():
    S, rl, PR, FG = (jl(n) for n in ('b632_scores.json', 'b632_record_lines.json', 'b632_prints.json', 'b632_face.json'))
    J, RA, PX = jl('b632_act_root.json'), jl('b632_root_arm.json'), jx('b632_page_chi.json')
    tag = g(K.KER, 'rev-parse', '--short=7', K.FACE_TAG + '^{commit}').strip()
    n = FG['nodes']
    t = _title_entry()
    e = ['', t, '',
         '*Filed at b632 on the author’s ruling `(R241)` and the author’s answer before the seal. Banks: relay `data/b632_dedekind_read.txt`, '
         '`data/b632_build.txt`, `data/b632_prints.txt`, `data/b632_face.txt`, `data/b632_page_chi.json`, `data/b632_table_final.txt`, '
         '`data/b632_act_root.txt`, `data/b632_author_answers.txt`. Nothing deposits.*', '',
         '**The instance** (`(R241)`(3), W-ORD-DEDEKIND-INSTANCE, OPEN_TRAILS :12895): SIDE-explicit-formula v0.25 = %s adds '
         'SIDEExplicitFormula/Schema/Dedekind.lean on the branch %s. DedekindConfig q is the schema’s sum of ζ’s configuration, its pole '
         'term carried, and the family’s summed configuration over the non-trivial characters mod q at their primitive inducers. By the '
         'author’s answer before the seal the ruling’s terminal is split: dedekind_instance -- Weil positivity of the summed configuration '
         'exactly when ζ’s target and every family target hold -- reads %s and takes no premise, the family theorem with the trivial summand '
         'added; dedekind_rhs reads %s on %s, the two premises of (R213)(3)(d) as Family.lean declares them since v0.21, extended and not '
         're-declared, used to read the summed arithmetic side as the Dedekind reading’s sum, each character at its own level. dedekind_three '
         'reads by %s. %d prints, beyond the standard three %s, sorryAx %s. H65a %s, H65b %s, H65c %s, H65d %s.' % (
             tag, K.FACE_BRANCH, n['dedekind_instance']['grade'], n['dedekind_rhs']['grade'], n['dedekind_rhs']['why'], FG.get('three_proof'),
             len(PR['prints']), PR['beyond'] or 'none', 'present' if PR['sorry'] else 'absent', S['H65a'][0], S['H65b'][0], S['H65c'][0], S['H65d'][0]), '',
         '**The schema sentence.** ' + K.BACKMATTER[0].upper() + K.BACKMATTER[1:].replace('`', '’'), '',
         '**The dip** (`(R241)`(1)-(2)): b630’s d_N² · log N below 2λ₁ at N = 41–48 entered at b630’s weight (FINDINGS :%d) as finite-range '
         'data; the conjecture’s record and the multiplicity form of Burnol’s constant entered as registry items on the Nyman–Beurling '
         'trail (OPEN_TRAILS :%d, :%d), the latter cross-entered on the simplicity trail (:%d), registry-read and not asserted; b630’s '
         'commit subject corrected by a dated entry (:%d).' % (rl['lines'][0]['line'], rl['lines'][2]['line'], rl['lines'][3]['line'],
                                                              rl['lines'][4]['line'], rl['lines'][1]['line']), '',
         '**The page, the table and the root.** The χ page at v0.25 with the instance’s nodes and the schema sentence as backmatter '
         '(changed %s); the table regenerated, the instance’s rows from the rule. The root of b632 over %d repositories, %d tags and %d '
         'banks; the chain verified, %s.' % (PX.get('changed'), len(J['reads']['heads']), len(J['reads']['tags']), len(J['reads']['banks']),
                                            ', '.join('%s %s' % (v[0], v[1]) for v in RA['verify'])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b603’s family theorem and its two named obstructions, whose place '
         'it finds -- on the arithmetic side and not on positivity -- and b629’s face, whose dip it records as data. It strengthens the '
         'programme’s offering of one located clause carried across configurations, each premise sitting on the statement that uses it.', '',
         '**Next.** Per `(R241)`(4): b632, W-ORD-TABLE-RULE-GRADES (OPEN_TRAILS :13133) if the author’s word falls there, else the deposit '
         'preparations of the (R110) route as the author names them. The author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds, identifies a sum with a Dedekind zeta function, or locates any zero.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) DedekindConfig q read as ζ’s configuration summed with the family’s, the trivial summand ζ’s with its pole term carried; '
              '(2) the premises of Family.lean extended and not re-declared, as the ferry orders where they exist; (3) the ruling’s '
              'dedekind_instance split by the author’s answer, H65b scored on dedekind_rhs; (4) dedekind_three stated as the equality of '
              'DedekindTheorem 3 with its statement, by rfl, after the family’s q = 3 form; (5) test_chain_page_b596.py case (9) carried, '
              'not repaired: b630’s rule-graded rows join any older ζ list’s Correspondence against relay HEAD’s table')


def _next_lines():
    b = open(_r('b630_table_rule_readings.txt'), 'rb').read() if os.path.exists(_r('b630_table_rule_readings.txt')) else b''
    return ['W-ORD-TABLE-RULE-GRADES names the table’s ungraded rows, its input relay data/b630_table_rule_readings.txt (sha256 %s); no '
            'kernel terminal' % sha(b)]


def _trail_text():
    S, fj, rl, J = (jl(n) for n in ('b632_scores.json', 'b632_findings.json', 'b632_record_lines.json', 'b632_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b632_author_answers.txt'), re.M))
    tag = g(K.KER, 'rev-parse', '--short=7', K.FACE_TAG + '^{commit}').strip()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R241) ratified.** (1) b630 at its weight. (2) The dip read; the multiplicity form a registry item. (3) W-ORD-DEDEKIND-INSTANCE. '
             '(4) The act after: b632.', '',
             '**Entered:** FINDINGS.md:%d (b630’s weight and the dip), :%d (the entry); OPEN_TRAILS.md:%d (the commit subject corrected), :%d '
             '(the conjecture’s record), :%d (the multiplicity form), :%d (cross-entered on the simplicity trail); this record; '
             'SIDE-explicit-formula v0.25 = %s.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], rl['lines'][2]['line'],
                                                    rl['lines'][3]['line'], rl['lines'][4]['line'], tag), '',
             '**Act root:** b632 `%s` (previous `%s`, b630’s; relay data/act_roots.txt).' % (J['root'], J['previous']), '',
             '**Prompts to the author:** %d (relay data/b632_author_answers.txt)%s.' % (
                 n_ans, (': ' + ' / '.join(_elide(answer_of(i))[:400] for i in range(n_ans))) if n_ans else ''), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b632_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R241)`(4), b632, W-ORD-TABLE-RULE-GRADES or the deposit preparations of the (R110) route, as the author names; '
             'the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b632_scores.json')
    L = ['=' * 104, 'b632 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H65a-H65d, (R241)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H65 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b632_defects.txt').rstrip(NL).split(NL)
    put_txt('b632_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n) for n in ('b632_scores.json', 'b632_findings.json', 'b632_trail.json', 'b632_record_lines.json', 'b632_act_root.json'))
    L = ['b632 -- THE COMPONENTS, BANKED UNDER (R241).', '',
         '### COMPONENT 0 : the process listing ; b630`s closing push-out relay %s ; push-b630* branches deleted by name (data/b632_branches.txt) ; '
         'every test file under tools/ run (data/b632_tests_stepzero.txt) ; the suite, its inputs arm repaired, run at HEAD before the face '
         '(data/b632_arms_prerun.txt) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b630`s weight FINDINGS :%d ; the subject correction OPEN_TRAILS :%d ; the conjecture`s record :%d ; the multiplicity '
         'form :%d ; cross-entered :%d' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : data/b632_dedekind_read.txt',
         '### COMPONENT 3 : data/b632_build.txt ; data/b632_prints.txt ; data/b632_face.txt ; v0.25 ; H65a %s, H65b %s, H65c %s' % (
             S['H65a'][0], S['H65b'][0], S['H65c'][0]),
         '### COMPONENT 4 : the χ page at v0.25 (data/b632_page_chi.json, data/b632_nodes_chi.txt, data/b632_chi_probe_out.txt) ; the table ; '
         'page arms data/b632_page_arms.txt ; the root %s ; the arm data/b632_root_arm.txt ; H65d %s' % (J['root'][:16], S['H65d'][0]),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b632 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b632_components.txt', L)



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
    put_json('b632_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b632_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-05 by b632 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b632_defects.json -- NOTHING WRITTEN')
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
    put_json('b632_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b632_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
