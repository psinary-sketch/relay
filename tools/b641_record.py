# -*- coding: utf-8 -*-
"""b641_record.py -- THE ACT'S RECORD TOOL, UNDER (R251). ### ONE SUBCOMMAND PER BANK.

### ### b641: LANE THREE, ACT SIXTY-EIGHT -- THE NEEDLE AND THE ROOT ORDER; THE PROVENANCE OF A PHRASE; THE RESEARCH DISCHARGE -- KEIPER'S
### SEVEN, THE WINDOW'S TWO, THE EPSTEIN COUNT FIELD, THE DEDEKIND PREMISES, THE PATCH VERSIONS -- EACH TO ONE STATUS WITH ITS REASON; THE
### OPENAI/MATH SOURCES READ AND BANKED; W-ORD-STATEMENT-PIN ENTERED.
### Subcommands write only `data/b641_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers
### are b633's, b639's and b640's record tools', imported; ledger appends through b566's guarded `append_to`. No platform is called: the
### only outbound reads of the act are the seat's plain git and https reads, made before the seal, with no identifier of the author.
### The clone of Component 6 is read through `git -C <clone> show HEAD:<path>` alone: nothing in it is built and no interpreter runs from it.
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
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b639_record as R9  # noqa: E402
import b641_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'e594f88a-2fab-4757-943d-7ab1bc3de815'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b641_registration_2026-10-08.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of, _nd, predict_cells, _land = R3.lines_of, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
KERNS_READ = R9.KERNS_READ
STANDIN = os.environ.get('B641_STANDIN') if ('dry' in sys.argv[2:]) else None


def put_txt(name, L):
    _write(os.path.join(SP if DRY else D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(SP if DRY else D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


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
_DJ = os.path.join(D, 'b641_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b641 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b641_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b641_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('relay data/b640_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b640_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
        ('relay data/b640_defects.txt: defects (b) and (h) by line', RELAY, PRE_RELAY, 'data/b640_defects.txt', ('GREP', r'^    \((b|h)\) '), 420),
        ('relay tools/b640_record.py before the repair: Question 1`s needle', RELAY, PRE_RELAY, 'tools/b640_record.py',
         ('GREP', r'^NEEDLES = |RH \(is\|was\|has been\) proved|if q == 1:'), 220),
        ('relay data/b640_reader_handread.txt: the hand-read answers', RELAY, PRE_RELAY, 'data/b640_reader_handread.txt', ('GREP', r'.'), 260),
        ('relay data/b640_reader_answers.txt: the reader`s answer 1, its opening', RELAY, PRE_RELAY, 'data/b640_reader_answers.txt',
         ('GREP', r'^ANSWER 1:'), 300),
        ('relay tools/act_root.py before the rule: where the root is computed', RELAY, PRE_RELAY, 'tools/act_root.py',
         ('GREP', r'^def (root_of|gather|compute|verify)\b|payload = |root = root_of'), 200),
        ('relay data/b640_premise_status.txt: the OPEN rows of the five subjects', RELAY, PRE_RELAY, 'data/b640_premise_status.txt',
         ('GREP', r'^  (KeiperObligations|BoundPremises|WindowObligations|EpsteinPremises|TrivialSummandPremise|EulerFactorPremise) '), 260),
        ('SIDE-explicit-formula: KeiperObligations, its four fields and their definitions', K.EF, K.EF_PIN, K.KEIPER_FILE,
         [23, 24, 25, 101, 102, 103, 107, 108, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127, 128, 129, 130, 133], 220),
        ('SIDE-explicit-formula: BoundPremises, its three fields (the work-order`s lemma (2), OPEN_TRAILS :12380)', K.EF, K.EF_PIN, K.BOUNDS_FILE,
         [12, 13, 14, 15, 16, 17, 98, 101, 107, 108, 109, 110, 111, 112], 220),
        ('SIDE-explicit-formula: WindowObligations, its two fields', K.EF, K.EF_PIN, K.WINDOW_FILE, [19, 20, 21, 22, 172, 173, 177, 178, 180, 181, 182, 183], 220),
        ('SIDE-explicit-formula: EpsteinPremises and its count field', K.EF, K.EF_PIN, K.EPSTEIN_FILE, [12, 13, 38, 39, 40, 41, 42, 43, 44, 51], 220),
        ('SIDE-explicit-formula: HCount, the count`s predicate', K.EF, K.EF_PIN, 'SIDEExplicitFormula/RestBound.lean', [42, 43, 44, 45], 220),
        ('SIDE-explicit-formula: TrivialSummandPremise and EulerFactorPremise at v0.25', K.EF, K.EF_PIN, K.FAMILY_FILE,
         [252, 255, 256, 257, 258, 259, 261, 262, 263, 264, 265, 266, 267], 220),
        ('SIDE-explicit-formula: the terms the Dedekind premises compare', K.EF, K.EF_PIN, 'SIDEExplicitFormula/GRHWeil.lean', [47, 61, 62, 63, 66, 67, 70, 71], 220),
        ('SIDE-explicit-formula: poleTerm, primeSum, archTerm', K.EF, K.EF_PIN, 'SIDEExplicitFormula/B321Identity.lean', [29, 30, 33, 34, 37, 38], 220),
        ('SIDE-explicit-formula: paperFT and gammaBracket', K.EF, K.EF_PIN, 'Zeta23/Defs.lean', [60], 220),
        ('SIDE-explicit-formula: gammaBracket', K.EF, K.EF_PIN, 'Zeta23/ExplicitFormula.lean', [80], 220),
        ('SIDE-explicit-formula: Bulka`s phi, logDeriv, taylorCoeff, riemannXi', K.EF, K.EF_PIN, 'Vendored/Bulka/Lc/LiCriterion/Basic.lean',
         [395, 409, 410, 541, 542, 1252, 1253], 220),
        ('SIDE-explicit-formula lake-manifest.json: the programme`s Mathlib pin', K.EF, K.EF_PIN, 'lake-manifest.json', ('GREP', r'"rev"|"name": "mathlib"'), 200),
        ('Mathlib at the pin: the convolution theorem for integrable functions', K.EF + '/.lake/packages/mathlib', K.MATHLIB_PIN,
         'Mathlib/Analysis/Fourier/Convolution.lean', [87, 88, 89, 119, 120, 121, 160], 200),
        ('Mathlib at the pin: digamma', K.EF + '/.lake/packages/mathlib', K.MATHLIB_PIN, 'Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean',
         [39, 47, 50], 200),
        ('Mathlib at the pin: the bounds on gamma and pi', K.EF + '/.lake/packages/mathlib', K.MATHLIB_PIN, 'Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean',
         [167, 171], 200),
        ('Mathlib at the pin: pi to twenty digits', K.EF + '/.lake/packages/mathlib', K.MATHLIB_PIN, 'Mathlib/Analysis/Real/Pi/Bounds.lean', [190, 206], 200),
        ('OPEN_TRAILS: the form clause, the build lines, the test-pin line, the patch work-order, b640`s record and correction, the Keiper '
         'obligations', PP, PRE_PP, 'OPEN_TRAILS.md', sorted(set(K.FERRY_LINES)), 1400),
        ('FINDINGS: b640`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B640_ENTRY], 400),
    ]


def _dlmf():
    out = []
    for sec, url in sorted(K.DLMF.items()):
        p = os.path.join(SP, 'dlmf_%s.html' % sec)
        b = open(p, 'rb').read() if os.path.exists(p) else None
        out.append((sec, url, hashlib.sha256(b).hexdigest() if b else None, len(b) if b else 0))
    return out


def reads(*a):
    L = ['b641 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)] if isinstance(sel, tuple) else \
            [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L.append('### THE REFERENCES FETCHED BEFORE THE SEAT`S READ (plain https GETs, no header naming the author; the pages kept in the scratchpad):')
    for sec, url, h, n in _dlmf():
        L.append('    DLMF %s  %s  sha256 %s ; %d bytes' % (sec, url, h or '### NOT FETCHED', n))
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b641_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()) + 1, len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R251) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b641 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b641_author_answers.txt', L)
    print('  prompts banked: %d' % n)


def answer_of(k):
    R3.rd = lambda name: rd('b641_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b641_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


def seal_hashes():
    rec_ = jl('b641_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b641 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b641_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R251)(1)-(3) AND (7)
W_HEAD = ('*Appended 2026-10-08 by b641 to b640’s entry (:%d), under `(R251)`(1) -- b640 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*')
CW_HEAD = ('*Appended 2026-10-08 by b641 to b640’s record (:%d), under `(R251)`(2) -- THE CEILING’S SENTENCE IS NOT SUPPORTED, NOT FORBIDDEN; '
           'THE NEEDLE REPAIRED:*')
RO_HEAD = ('*Appended 2026-10-08 by b641, under `(R251)`(3) -- W-ORD-ROOT-ORDER, STANDING, TRIGGER G-ACTROOT-VERIFY:*')
SP_HEAD = ('*Appended 2026-10-08 by b641, under `(R251)`(7) -- W-ORD-STATEMENT-PIN, ENTERED AND PRICED, NOT STARTED, TRIGGER THE NEXT NEW '
           'LOAD-BEARING DECLARATION, ACTED ON THE AUTHOR’S WORD:*')
FORBID = re.compile(r'forbidden', re.I)


def _poss(t):
    """### ledger text: a backtick standing as an apostrophe (a letter on each side) written ’, the guard refusing odd backticks (b629's trap)."""
    return re.sub(r'(?<=[A-Za-z0-9])`(?=[a-z])', '’', t)


def _forbidden_reads():
    """### every occurrence of `forbidden` in the record (FINDINGS and OPEN_TRAILS at PLACE-papers before the act), each with its line and the
    ### object it is said of; and the relay tools and banks tracked before the act that say it, by path and line, for the same read."""
    out = []
    for f in ('FINDINGS.md', 'OPEN_TRAILS.md'):
        for i, l in enumerate(lines_of(_show(PP, PRE_PP, f) or ''), 1):
            for m in FORBID.finditer(l):
                out.append(dict(file=f, line=i, text=l[max(0, m.start() - 170):m.end() + 60]))
    rel = []
    for l in g(RELAY, 'grep', '-n', '-i', 'forbidden', PRE_RELAY, '--', 'tools', 'data', 'reports', 'HANDOFF.md').split(NL):
        if l.count(':') >= 3 and 'anthropic-zeta23' not in l:
            _r, p, n, t = l.split(':', 3)
            rel.append(dict(file=p, line=int(n), text=' '.join(t.split())[:200]))
    return out, rel


# ### the seat's read of each occurrence's object, by file and line: none is said of the ceiling (the read printed in the bank beside each)
FORBID_OBJECTS = {('FINDINGS.md', 967): 'the valences of a prime p > 3 (0, 1, 2, 4, 5, 6 structurally excluded)',
                  ('OPEN_TRAILS.md', 1523): 'figures resting on a definition the executor made',
                  ('OPEN_TRAILS.md', 4655): 'a sign of the prime sum at lawful seeds',
                  ('OPEN_TRAILS.md', 9073): 'running the chain, by an order`s own closing line'}


def _weight():
    rl0 = jl('b640_record_lines.json')
    post = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b640_checks_postpush.txt'))
    pre = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b640_checks.txt'))
    RC, DS, M, A = jl('b640_reader_compare.json'), jl('b640_description_scan.json'), jl('b640_mirror.json'), jl('b640_act_root.json')
    reps = jl('b640_reader_repairs.json').get('repairs') or []
    Z = jl('b640_zenodo.json')
    rd_ = Z.get('read') or {}
    sh = jl('b640_seal_hashes.json')
    nd = len(json.load(io.open(os.path.join(D, 'b640_defects.json'), encoding='utf-8')).get('defects') or [])
    return ('\n%s the second reader`s three questions: the sealed comparison %s of 3, H74c and N3 refuted in letter; by hand 3 of 3 (relay '
            'data/b640_reader_handread.txt); both figures on the record, the difference defect (b). The reader`s UNCLEAR passages repaired in %d '
            'rewrites, the check printing that no figure, name or status moved and a planted bad rewrite caught (data/b640_repair_arm_control.txt). '
            'The description at %s bytes, the scanner %s. The mirror %s verified %s; the draft %s carrying it and the description byte for byte, '
            '%s files at their digests (H74d %s); the draft unpublished on the author`s word. Both pages and the terminal table unchanged. Three '
            'edits after the seal, each on the author`s word, each committed alone, the seal re-run declaring all three (%d amendments). The '
            'suite %s of %s pre-push and %s of %s post-push, G-ACTROOT-VERIFY failing by defect (h) -- the seal re-run after the root was '
            'computed changed a bank the root names -- and the figure stands as the record; nothing relabelled. Defects (a)-(i), %d, as the '
            'seat listed them. Nothing deposited; no kernel source touched. Relay c7c31e0c; PLACE-papers e8320b5; FINDINGS :%d; OPEN_TRAILS :%d '
            'and :%d; the root %s… (previous b639`s).\n' % (
                W_HEAD % K.B640_ENTRY, RC.get('agree'), len(reps), DS.get('bytes'), 'clean' if DS.get('clean') else 'NOT CLEAN',
                os.path.basename(M.get('zip') or ''), 'clean on all three clauses' if M.get('clean') else 'NOT CLEAN', rd_.get('id'),
                rd_.get('n_files'), 'holds' if rd_.get('h74d') else 'refuted', len(sh.get('amendments') or []),
                pre.group(2) if pre else '?', pre.group(1) if pre else '?', post.group(2) if post else '?', post.group(1) if post else '?', nd,
                K.B640_ENTRY, K.B640_RECORD, K.B640_CORRECTION, (A.get('root') or '?')[:16]))


def _ceiling_text():
    occ, rel = _forbidden_reads()
    of_ceiling = [o for o in occ if (o['file'], o['line']) not in FORBID_OBJECTS]
    return ('\n%s the ceiling`s sentence -- that RH is proved -- is NOT SUPPORTED by the corpus, h2_sign being open, and is not a forbidden '
            'sentence: the corpus may name it in order to say it is unsupported, as b640`s second reader did. A needle that tests a text for '
            'the unsupported sentence matches an assertion of it and not a denial of it: Question 1`s needle in relay tools/b640_record.py is '
            'repaired so, every alternative read inside its own sentence with a negation before it read as a denial (relay %s, alone), its test '
            'tools/test_reader_needle_b641.py planting the reader`s own denial (no match) and an assertion (a match) and reading the three '
            'hand-read answers at 3 of 3. Wherever the record says `forbidden` of the ceiling it reads `not supported` after this act; read at '
            'PLACE-papers %s, FINDINGS and OPEN_TRAILS say `forbidden` %d times and none of them of the ceiling (FINDINGS :967, a prime`s '
            'valences; OPEN_TRAILS :1523, figures resting on a definition the executor made; :4655, a sign at lawful seeds; :9073, running the '
            'chain), so no line is re-read and none is edited (relay data/b641_record_lines.txt prints each; %d of the ceiling). No banked '
            'ruling or ferry of b639`s or b640`s carries the word; its use of the ceiling is the navigator`s wording, recorded as the '
            'navigator`s.\n' % (
                CW_HEAD % K.B640_RECORD, K.NEEDLE_COMMIT, PRE_PP, len(occ), len(of_ceiling)))


def _root_order_text():
    return ('\n%s the act root is computed as the last step of an act, after the last declared seal re-run, and no bank the root names is '
            'written after it; any edit after the root is the next act`s. relay tools/act_root.py carries it (relay %s, alone): compute refuses '
            'a root that leaves out the act`s own seal bank when it exists, and banks the root`s time; verify reads a bank the root names whose '
            'file was written after that time as DISAGREE, its bytes unchanged or not; tools/test_act_root_order_b641.py plants a bank write '
            'after the root and expects the arm to fail. Trigger: G-ACTROOT-VERIFY. b640`s root is not recomputed: its line stands with its '
            'recorded defect (h), and b641`s root is appended beneath it.\n' % (RO_HEAD, K.ORDER_COMMIT))


def _statement_pin_text():
    return ('\n%s a statement file authored and committed before its proof, carrying the statement with a placeholder that is not a proof '
            '(the statement as a definition of a Prop, no `sorry`), and a kernel check that the proof`s theorem is that statement (the proof '
            'elaborated against the statement file`s Prop, compiled in its own module), beside the salt checks and the E0 gate, not replacing '
            'them. Priced by the seat against the current pins (SIDE-explicit-formula v0.25 = 8c51431, Mathlib %s, %s): two acts -- one for the '
            'form, its checker and a test planting a proof whose theorem differs from its statement (expected to fail), the check compiled as '
            'one module under the hold by the direct route (OPEN_TRAILS :13167); one for the first declaration so pinned -- and none beyond the '
            'declaring act`s own after that. Trigger: the next new load-bearing declaration; acted on the author`s word.\n' % (
                SP_HEAD, K.MATHLIB_PIN[:8], K.EF_TOOLCHAIN.split(':')[-1]))


def record_lines(*a):
    """### Component 1, (R251)(1)-(3) and (7): FINDINGS, b640 at its weight (to :7911); OPEN_TRAILS, the ceiling`s wording with the needle
    ### repaired (to b640's record :13455), W-ORD-ROOT-ORDER and W-ORD-STATEMENT-PIN. Every `forbidden` of the record printed, before and after."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The premise status at five: ')
    if entry != K.B640_ENTRY:
        sys.exit('### b640`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B640_ENTRY, _poss(_weight())), ('OPEN_TRAILS.md', CW_HEAD % K.B640_RECORD, _poss(_ceiling_text())),
             ('OPEN_TRAILS.md', RO_HEAD, _poss(_root_order_text())), ('OPEN_TRAILS.md', SP_HEAD, _poss(_statement_pin_text()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None') if x in allt]
    occ, rel = _forbidden_reads()
    L = ['b641 -- COMPONENT 1, (R251)(1)-(3) AND (7): THE RECORD LINES (%s)' % utc(), '',
         '### (R251)(2): EVERY `forbidden` OF THE RECORD, PRINTED BEFORE AND AFTER (FINDINGS and OPEN_TRAILS at PLACE-papers %s):' % PRE_PP]
    for o in occ:
        obj = FORBID_OBJECTS.get((o['file'], o['line']), '### OF THE CEILING')
        L += ['  %s :%d -- said of: %s' % (o['file'], o['line'], obj), '      before: ...%s...' % o['text'],
              '      after:  %s' % ('unchanged; not of the ceiling, so nothing to re-read' if not obj.startswith('###') else 'reads `not supported`')]
    L += ['### occurrences %d ; said of the ceiling %d' % (len(occ), sum(1 for o in occ if (o['file'], o['line']) not in FORBID_OBJECTS)), '',
          '### beside them, relay`s tools and banks tracked at %s that say it (prior instruments and banks, unedited; none of the ceiling`s '
          'sentence, each a gate or a figure of its own act):' % PRE_RELAY] + ['  %s :%d  %s' % (r['file'], r['line'], r['text']) for r in rel]
    L += ['', '### the lines as they will land:'] + ['  %s -- %s' % (f, h[:150]) for f, h, _t in items]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backtick parity odd in: %s ; unread figures: %s ; forbidden %d (of the ceiling %d)' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', len(occ),
        sum(1 for o in occ if (o['file'], o['line']) not in FORBID_OBJECTS)))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        print(NL.join(L[:12]))
        return
    if cells or any(nd.values()) or not clean or ticks or unread:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    put_txt('b641_record_lines.txt', L)
    _land(Q, items, 'b641_record_lines.json', K.B640_ENTRY)


# ================================================================================ COMPONENT 2: THE PHRASE, (R251)(4)
def _entered(repo, h, phrase):
    """### the file and line a commit brought the phrase in at: its added lines read from the commit's own diff."""
    out = []
    d = g(repo, 'show', '--unified=0', '--format=', h)
    f, n = None, None
    for l in d.split(NL):
        if l.startswith('+++ '):
            f = l[6:] if l.startswith('+++ b/') else l[4:]
        elif l.startswith('@@'):
            m = re.search(r'\+(\d+)', l)
            n = int(m.group(1)) if m else None
        elif l.startswith('+') and n is not None:
            if phrase.lower() in l.lower():
                out.append((f, n, l[1:].strip()))
            n += 1
    return out


def phrase(*a):
    """### Component 2, (R251)(4): `git log -S` of the phrase in relay and PLACE-papers, every commit printed oldest first; the entering commit,
    ### the ruling it names (or that it names none) and the file and line it brought the phrase in at. data/b641_phrase_provenance.txt."""
    L = ['b641 -- COMPONENT 2, (R251)(4): THE PROVENANCE OF "%s", BY git log -S (%s)' % (K.PHRASE, utc()), '']
    res = {}
    for name, repo in (('relay', RELAY), ('PLACE-papers', PP)):
        cs = [l for l in g(repo, 'log', '--reverse', '-S', K.PHRASE, '--format=%H %ad', '--date=short', 'HEAD').split(NL) if l.strip()]
        ci = [l for l in g(repo, 'log', '--reverse', '-i', '-S', K.PHRASE, '--format=%H', 'HEAD').split(NL) if l.strip()]
        L.append('### %s: git log -S "%s" -- %d commit(s) as written; %d ignoring case' % (name, K.PHRASE, len(cs), len(ci)))
        for l in cs:
            h, dt = l.split()
            L.append('    %s %s  %s' % (h[:8], dt, g(repo, 'log', '-1', '--format=%s', h).strip()[:200]))
        if cs:
            h0 = cs[0].split()[0]
            body = g(repo, 'log', '-1', '--format=%B', h0)
            rul = sorted(set(re.findall(r'\(R\d+\)', body)))
            ent = _entered(repo, h0, K.PHRASE)
            L += ['  ### THE ENTERING COMMIT (%s): %s, %s' % (name, h0, g(repo, 'log', '-1', '--format=%ad', '--date=iso', h0).strip()),
                  '      its subject: %s' % body.strip().split(NL)[0][:400],
                  '      the ruling it names: %s' % (', '.join(rul) if rul else 'NONE -- the commit names no ruling (the programme`s rulings are numbered (R1) on from b366)')]
            for f, n, t in ent:
                i = t.lower().find(K.PHRASE)
                L.append('      entered at %s :%d -- ...%s...' % (f, n, t[max(0, i - 160):i + len(K.PHRASE) + 80]))
            if not ent:
                L.append('      ### the phrase not found among the commit`s added lines (a removal or a move)')
            res[name] = dict(commit=h0, date=cs[0].split()[1], rulings=rul, entered=[dict(file=f, line=n) for f, n, _t in ent], commits=len(cs), commits_i=len(ci))
        L.append('')
    first = min((v['date'], k) for k, v in res.items()) if res else None
    L += ['### the earlier entry of the two: %s (%s)' % (first[1], first[0]) if first else '### NO COMMIT CARRIES THE PHRASE',
          '### the navigator`s passing the phrase along without its provenance is recorded as the navigator`s ((R251)(4)).', '',
          '### ### **PHRASE "%s": relay %s ; PLACE-papers %s.**' % (K.PHRASE, (res.get('relay') or {}).get('commit', 'NONE')[:8],
                                                                     (res.get('PLACE-papers') or {}).get('commit', 'NONE')[:8])]
    put_txt('b641_phrase_provenance.txt', L)
    put_json('b641_phrase_provenance.json', dict(at=utc(), phrase=K.PHRASE, repos=res))
    print(L[-1])


# ================================================================================ COMPONENTS 3-5: THE RESEARCH DISCHARGE, (R251)(5)
def _docstring(text_lines, n):
    """### the /-- ... -/ docstring block directly above line n (1-based) of a Lean file, joined; '' when none."""
    i = n - 2
    while i >= 0 and not text_lines[i].strip():
        i -= 1
    if i < 0 or not text_lines[i].rstrip().endswith('-/'):
        return ''
    j = i
    while j >= 0 and '/--' not in text_lines[j]:
        j -= 1
    return ' '.join(' '.join(text_lines[j:i + 1]).split()) if j >= 0 else ''


# ### THE EDIT AFTER THE SEAL, on the author's answers at Components 3, 4 and 5: a premise the seat has computed false is not OPEN --
# ### TrivialSummandPremise takes the sixth status, REFUTED-BY-COMPUTATION, the witness class and the value printed beside it; EulerFactorPremise
# ### stays OPEN with its counterexample and its sufficient condition beside it; dedekind_rhs keeps the grade its statement reads and takes the
# ### annotation; and one OPEN_TRAILS block carries the sixth status's clause and the four work-orders the answers name (`workorders`).
AUTHOR_STATUS = {'D1': 'REFUTED-BY-COMPUTATION'}
AUTHOR_NOTES = {
    'D1': ['WITNESS CLASS : every k : R -> C real, nonnegative, continuous, not identically zero and supported in (-log 2, log 2)',
           'VALUE : poleTerm k = paperFT k (i/2) + paperFT k (-i/2) = INT k(u) (e^(-u/2) + e^(u/2)) du > 0, while both prime sums are 0 and the '
           'Gamma terms are equal, so the premise would need poleTerm k = 0 (the seat`s computation, not compiled)'],
    'D2': ['COUNTEREXAMPLE : q = 6, the odd character mod 6 induced from conductor 3; for k supported in (-log 2, log 2) the prime terms agree and '
           'the Gamma terms differ by log 2 times (1/2 pi) INT paperFT k = log 2 k(0), nonzero when k(0) is (the seat`s computation, not compiled)',
           'SUFFICIENT CONDITION : every non-trivial character mod q primitive (q = 3 among them), both sides then reading the same character at the '
           'same level'],
}
RHS_NOTE = ('the row resting on both: dedekind_rhs (SIDE-explicit-formula 8c51431, SIDEExplicitFormula/Schema/Dedekind.lean :59) -- its grade '
            'unchanged, read from its statement; annotated: on a premise refuted by computation at b641 (W-ORD-DEDEKIND-RHS-RESTATE)')


def _status(o):
    return AUTHOR_STATUS.get(o['key'], o['status'])


def _ob_block(o):
    L = []
    t = lines_of(_show(K.EF, K.EF_PIN, o['file']) or '') if o['file'].endswith('.lean') else []
    L.append('### (%s) %s -- the field: %s' % (o['key'], o['head'], o['field']))
    if t:
        L.append('    at SIDE-explicit-formula %s %s :%d : %s' % (K.EF_PIN, o['file'], o['line'], t[o['line'] - 1].strip()))
        if o['defline'] != o['line']:
            L.append('    its definition :%d : %s' % (o['defline'], t[o['defline'] - 1].strip()))
        L.append('    its docstring : %s' % (_docstring(t, o['defline']) or '### NONE ABOVE THE DEFINITION'))
    L += ['    the seat`s read : %s' % o['read'], '    STATUS : %s%s' % (_status(o), ' (the author`s answer at Component 5; the worklist`s %s)' % o['status']
                                                                    if o['key'] in AUTHOR_STATUS else ''), '    REASON : %s' % o['reason'],
          '    DISCHARGER : %s' % o['discharger']]
    L += ['    %s' % n for n in AUTHOR_NOTES.get(o['key'], [])]
    if o['candidate']:
        L.append('    CANDIDATE NEW DECLARATION (raised as a prompt, written nowhere) : %s' % o['candidate'])
    return L


def _n3(obs):
    """### (R251)(5) and N3: exactly one status of the three, a reason line, a discharger, none reading presumed."""
    return [o['key'] for o in obs if o['status'] not in K.STATUSES or not o['reason'].strip() or not o['discharger'].strip()
            or 'presum' in (o['read'] + o['reason']).lower()]


def _component(comp, name, title, extra=None):
    obs = [o for o in K.OBLIGATIONS if o['comp'] == comp and (extra is None or o['key'] in extra)]
    L = ['b641 -- COMPONENT %d, (R251)(5): %s (%s)' % (comp, title, utc()), '',
         '### each obligation printed with its field and docstring at its pin; the seat`s read of what would discharge it -- a theorem in the kernels '
         '(named, its axiom print read), a literature theorem (the reference read, the statement matched), or neither -- and exactly one of '
         'DISCHARGED, CITED, OPEN, with its reason in one sentence and its discharger named; a candidate new declaration printed as a statement '
         'and raised as a prompt, written nowhere.', '']
    if comp == 3:
        L += ['### the seven, as the kernel names them where the proofs stop (OPEN_TRAILS :%d, W-ORD-KEIPER-FACE): KeiperObligations` four '
              '(lemma (1)) and BoundPremises` three (lemma (2)).' % K.KEIPER_WO, '']
    for o in obs:
        L += _ob_block(o) + ['']
    bad = _n3(obs)
    cnt = collections.Counter(o['status'] for o in obs)
    L += ['### the references fetched (scratchpad, digest): %s' % '; '.join('DLMF %s %s' % (s, (h or '-')[:16]) for s, _u, h, _n in _dlmf())] if comp == 3 else []
    L += ['### ### **OBLIGATIONS %d ; DISCHARGED %d ; CITED %d ; OPEN %d ; WITHOUT ONE STATUS AND A REASON %s ; CANDIDATE DECLARATIONS %d.**' % (
        len(obs), cnt['DISCHARGED'], cnt['CITED'], cnt['OPEN'], bad or 'NONE', sum(1 for o in obs if o['candidate']))]
    put_txt(name + '.txt', L)
    put_json(name + '.json', dict(at=utc(), obligations=[dict((k, o[k]) for k in ('key', 'head', 'field', 'file', 'line', 'status', 'reason',
                                                                                 'discharger', 'candidate')) for o in obs],
                                  counts=dict(cnt), without=bad))
    print(L[-1])
    return obs


def keiper(*a):
    """### Component 3: Keiper's seven. data/b641_keiper_status.txt and its json."""
    _component(3, 'b641_keiper_status', 'KEIPER`S SEVEN, EACH TO ONE STATUS WITH ITS REASON')


def window_epstein(*a):
    """### Component 4: the window's two and the Epstein count field. data/b641_window_epstein_status.txt and its json."""
    _component(4, 'b641_window_epstein_status', 'THE WINDOW`S TWO AND THE EPSTEIN COUNT FIELD, EACH TO ONE STATUS WITH ITS REASON')


def _label_at_head(f):
    t = _show(PP, 'HEAD', 'day1/' + f) or ''
    m = re.search(r'\*\*Version (v?\d+(?:\.\d+)+)\*\*|\bVersion:?\s*\**\s*(v?\d+(?:\.\d+)+)|\b(v\d+\.\d+(?:\.\d+)?)\b', t)
    return (next(x for x in m.groups() if x) if m else None), hashlib.sha256(t.encode('utf-8')).hexdigest()


def patch_versions(*a):
    """### Component 5, the patch versions (OPEN_TRAILS :13397): each of the seven companions with its label in b639's file bank, its label read
    ### at PLACE-papers HEAD, the lines differing from v1.1.2 as b639 printed them, and its patch version resolved. data/b641_patch_versions.txt."""
    bank = rd('b639_deposit_files.txt')
    rows = []
    for f in K.COMPANIONS:
        m = re.search(r'source day1/%s @ (\w+) \(its last commit (\w+) ([\d-]+)\) ; old -> new: .*? ; label (\S+) -> (\S+) ; (\d+) lines differ'
                      % re.escape(f), bank)
        if not m:
            rows.append(dict(file=f, ok=False))
            continue
        lab, now_sha = _label_at_head(f)
        last = g(PP, 'log', '-1', '--format=%h %ad', '--date=short', 'HEAD', '--', 'day1/' + f).strip()
        old = m.group(5)
        nums = old.lstrip('v').split('.')
        patch = 'v' + '.'.join(nums + ['1']) if len(nums) == 2 else 'v' + '.'.join(nums[:-1] + [str(int(nums[-1]) + 1)])
        rows.append(dict(file=f, ok=True, read_at=m.group(1), last=m.group(2), last_date=m.group(3), label=old, label_head=lab, diff=int(m.group(6)),
                         patch=patch, head_last=last, moved_since=last.split()[0][:7] != m.group(2)[:7]))
    o = next(x for x in K.OBLIGATIONS if x['key'] == 'P1')
    L = ['b641 -- COMPONENT 5, (R251)(5): W-ORD-DAY1-PATCH-VERSIONS (OPEN_TRAILS :%d), THE SEVEN PATCH VERSIONS RESOLVED (%s)' % (K.PATCH_WO, utc()), '',
         '### the source of each: relay data/b639_deposit_files.txt (the label as deposited and the lines differing from v1.1.2`s bytes), the label '
         'read at PLACE-papers HEAD and the file`s last commit there; the patch version: the label`s next patch number (v2.3 -> v2.3.1).', '']
    for r in rows:
        if not r['ok']:
            L.append('  %-30s ### NOT FOUND IN b639`S FILE BANK' % r['file'])
            continue
        L.append('  %-30s label %s (b639`s bank, read @ %s, its last commit %s %s) ; at HEAD %s (last commit %s)%s ; %d lines differ from v1.1.2 ; '
                 'PATCH VERSION %s' % (r['file'], r['label'], r['read_at'], r['last'], r['last_date'], r['label_head'], r['head_last'],
                                       ' ### MOVED SINCE b639' if r['moved_since'] else '', r['diff'], r['patch']))
    L += ['', '### STATUS : %s' % o['status'], '### REASON : %s' % o['reason'], '### DISCHARGER : %s' % o['discharger'], '',
          '### ### **COMPANIONS %d ; RESOLVED %d ; LABELS WRITTEN 0.**' % (len(rows), sum(1 for r in rows if r['ok']))]
    put_txt('b641_patch_versions.txt', L)
    put_json('b641_patch_versions.json', dict(at=utc(), rows=rows, status=o['status'], reason=o['reason'], discharger=o['discharger']))
    print(L[-1])


def pstatus(*a):
    """### Component 5: the Dedekind premises each to one status with its reason, and the premise status file regenerated as
    ### data/b641_premise_status.txt beside b640's by b640's status reader (its banks' names made b641's), each head of (R251)(5) carrying its
    ### obligations' statuses beneath it; the diff against b640's printed by row."""
    import b640_record as R40
    saved = (R40.put_txt, R40.put_json)
    got = {}
    R40.put_txt = lambda name, L: got.__setitem__(name.replace('b640_', 'b641_'), L)
    R40.put_json = lambda name, j: got.__setitem__(name.replace('b640_', 'b641_'), j)
    try:
        R40.status()
    finally:
        R40.put_txt, R40.put_json = saved
    L, J = got['b641_premise_status.txt'], got['b641_premise_status.json']
    by = collections.defaultdict(list)
    for o in K.OBLIGATIONS:
        by[o['head']].append(o)
    out = []
    for l in L:
        if l.startswith('b640 -- COMPONENT 2'):
            l = 'b641 -- COMPONENT 5, (R251)(5): THE PREMISE STATUS REGENERATED BY b640`S READER, THE OBLIGATIONS OF (5) BENEATH THEIR HEADS' + l[l.index(' ('):]
        out.append(l)
        m = re.match(r'^  (\S+)\s+rule ', l)
        if m and m.group(1) in by:
            for o in by[m.group(1)]:
                out.append('      (R251)(5) %s %s: %s -- %s' % (o['key'], o['field'], _status(o), o['reason']))
    old = [l for l in lines_of(rd('b640_premise_status.txt'))]
    strip_ = lambda ls: [l for l in ls if not l.startswith(('b640 -- COMPONENT 2', 'b641 -- COMPONENT 5', '### the kernels read at the commits'))
                         and not l.startswith('      (R251)(5)')]   # noqa: E731
    dif = [x for x in difflib.unified_diff(strip_(old), strip_(out), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    heads0 = dict((x['head'], x['status']) for x in jl('b640_premise_status.json').get('heads') or [])
    heads1 = dict((x['head'], x['status']) for x in J.get('heads') or [])
    moved = sorted(h for h in set(heads0) | set(heads1) if heads0.get(h) != heads1.get(h))
    added = sum(1 for l in out if l.startswith('      (R251)(5)'))
    out += ['', '### THE DEDEKIND PREMISES, (R251)(5), EACH TO ONE STATUS WITH ITS REASON:']
    for o in [o for o in K.OBLIGATIONS if o['comp'] == 5 and o['key'].startswith('D')]:
        out += [''] + _ob_block(o)
    out += ['', '### %s' % RHS_NOTE]
    out += ['', '### THE DIFF AGAINST b640`S data/b640_premise_status.txt, BY ROW (title and timestamp lines and the (R251)(5) lines aside): %d line(s)' % len(dif)]
    out += ['    ' + x[:300] for x in dif[:200]]
    out += ['### heads whose status moved: %s ; (R251)(5) lines beneath their heads: %d' % (moved or 'NONE', added), '',
            '### ### **HEADS %d ; STATUS MOVED %d ; ROWS DIFFERING %d ; THE DEDEKIND PREMISES %s.**' % (
                len(heads1), len(moved), len(dif), ', '.join('%s %s' % (o['head'], _status(o)) for o in K.OBLIGATIONS if o['key'] in ('D1', 'D2')))]
    J = dict(J, at=utc(), obligations=dict((h, [dict(key=o['key'], status=_status(o)) for o in os_]) for h, os_ in by.items()), diff=dif,
             moved=moved, dedekind=[dict([(k, o[k]) for k in ('key', 'head', 'reason', 'discharger', 'candidate')] + [('status', _status(o)),
                                         ('notes', AUTHOR_NOTES.get(o['key'], []))]) for o in K.OBLIGATIONS if o['key'] in ('D1', 'D2')],
             rhs_note=RHS_NOTE)
    put_txt('b641_premise_status.txt', out)
    put_json('b641_premise_status.json', J)
    print(out[-1])


# ================================================================================ COMPONENT 6: THE OPENAI/MATH READ, (R251)(6)
def _oai(path):
    r = subprocess.run(['git', '-C', K.CLONE, 'show', 'HEAD:' + path], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def oai(*a):
    """### Component 6: the named files of the clone read from its commit (git show; the working tree`s checkout is partial on this machine),
    ### printed in full where short and by the named fields where long; the two Mathlib pins side by side. data/b641_openai_math_read.txt. No
    ### line of it enters a ledger or a paper; their results stay theirs."""
    head = g(K.CLONE, 'rev-parse', 'HEAD').strip()
    url = g(K.CLONE, 'remote', 'get-url', 'origin').strip()
    L = ['b641 -- COMPONENT 6, (R251)(6): THE OPENAI/MATH SOURCES, READ FROM THE FILES THEMSELVES (%s)' % utc(), '',
         '### the clone: %s from %s, commit %s (%s) ; shallow, not built, no lake run, no interpreter run from it; read by git show HEAD:<path>' % (
             K.CLONE, url, head, g(K.CLONE, 'log', '-1', '--format=%cI', head).strip()),
         '### THEIR RESULTS STAY THEIRS: no line about the collection enters OPEN_TRAILS, FINDINGS or any paper this act; the navigator reads this '
         'bank and rules at b642.', '']
    for p in K.OAI_FILES:
        t = _oai(p)
        L.append('=== %s (%s bytes at the commit, sha256 %s)' % (p, len(t.encode('utf-8')) if t is not None else '### ABSENT',
                                                               hashlib.sha256(t.encode('utf-8')).hexdigest()[:16] if t is not None else '-'))
        if t is None:
            continue
        if p.endswith('lake-manifest.json'):
            j = json.loads(t)
            L += ['    %-34s rev %s ; inputRev %s' % (x['name'], x.get('rev'), x.get('inputRev')) for x in j.get('packages') or []]
        elif p.endswith('formalization.yaml'):
            ls = lines_of(t)
            pick = [i for i, l in enumerate(ls) if re.match(r'^(version|project|status|review|automation):', l)]
            for i in pick:
                blk = [ls[i]] + [x for x in ls[i + 1:i + 6] if x.startswith(' ') and not x.strip().startswith('- comparator_config')][:4]
                L += ['    :%d  %s' % (i + 1 + k, x) for k, x in enumerate(blk)]
            q = [i for i, l in enumerate(ls) if 'QuasiRiemannHypothesis.json' in l]
            for i in q:
                L += ['    :%d  %s' % (i + 1 + k, ls[i + k]) for k in range(3)]
        else:
            L += ['    ' + x for x in lines_of(t)]
        L.append('')
    theirs = next((x for x in json.loads(_oai('lean/lake-manifest.json') or '{}').get('packages') or [] if x['name'] == 'mathlib'), {})
    ours = next((x for x in json.loads(_show(K.EF, K.EF_PIN, 'lake-manifest.json') or '{}').get('packages') or [] if x['name'] == 'mathlib'), {})
    L += ['### THE TWO MATHLIB PINS, SIDE BY SIDE:',
          '    openai/math lean/lake-manifest.json @ %s : mathlib %s ; toolchain %s' % (head[:12], theirs.get('rev'), (_oai('lean/lean-toolchain') or '').strip()),
          '    SIDE-explicit-formula lake-manifest.json @ %s : mathlib %s ; toolchain %s' % (K.EF_PIN, ours.get('rev'), (_show(K.EF, K.EF_PIN, 'lean-toolchain') or '').strip()),
          '    the same commit: %s' % (theirs.get('rev') == ours.get('rev')), '',
          '### ### **CLONE %s ; FILES READ %d OF %d ; MATHLIB %s AGAINST %s.**' % (head[:12], sum(1 for p in K.OAI_FILES if _oai(p) is not None),
                                                                            len(K.OAI_FILES), (theirs.get('rev') or '?')[:8], (ours.get('rev') or '?')[:8])]
    put_txt('b641_openai_math_read.txt', L)
    put_json('b641_openai_math_read.json', dict(at=utc(), clone=K.CLONE, url=url, commit=head, theirs=theirs.get('rev'), ours=ours.get('rev'),
                                                files=[p for p in K.OAI_FILES if _oai(p) is not None]))
    print(L[-1])


# ================================================================================ THE AUTHOR'S ANSWERS AT COMPONENTS 3-5: THE OPEN_TRAILS BLOCK
FIVE_CLAUSE = 13429           # ### OPEN_TRAILS: b640's five-status clause, beneath the domain-condition criterion
SIX_HEAD = ('*Appended 2026-10-08 by b641 beneath the five-status clause (:%d), under the author’s answer at b641’s Component 5 -- THE SIXTH STATUS, '
            'REFUTED-BY-COMPUTATION:*' % FIVE_CLAUSE)
PD_HEAD = ('*Appended 2026-10-08 by b641, under the author’s answer at b641’s Component 4 -- W-ORD-PLATEAURAMP-DOCSTRING, NOT STARTED, TRIGGER THE '
           'FIRST UNDERSTATES ROW OF THE REVIEW PASS:*')
EZ_HEAD = ('*Appended 2026-10-08 by b641, under the author’s answer at b641’s Component 4 -- W-ORD-EPSTEIN-ZQ, PRICED IN b641’S CLOSING, TRIGGER A '
           'RULING TO BUILD IT:*')
DR_HEAD = ('*Appended 2026-10-08 by b641, under the author’s answer at b641’s Component 5 -- W-ORD-DEDEKIND-RHS-RESTATE, NOT STARTED, TRIGGER THE '
           'PROVING ACT:*')
NV_HEAD = ('*Appended 2026-10-08 by b641, under the author’s answer at b641’s Component 5 -- W-ORD-PREMISE-NONVACUITY, STANDING, TRIGGER ANY NEW '
           'PREMISE STRUCTURE:*')


def _wo_items():
    return [
        ('OPEN_TRAILS.md', SIX_HEAD,
         '\n%s a premise the seat has computed false is not OPEN: it takes REFUTED-BY-COMPUTATION, a sixth status beside the five, its witness class '
         'and the value that refutes it printed in its bank; the status is the seat`s computation and is not compiled -- it stands until a kernel '
         'theorem compiles the refutation or the premise is restated. It is assigned from the computation, not by the shared tool`s rule over '
         'the kernels. At b641 TrivialSummandPremise takes it (relay data/b641_premise_status.txt: the witness class every real, nonnegative, '
         'continuous k not identically zero and supported in (-log 2, log 2); the value, its pole term positive where the premise needs it 0). '
         'The census at v0.7 carries it.\n' % SIX_HEAD),
        ('OPEN_TRAILS.md', PD_HEAD,
         '\n%s SIDE-explicit-formula v0.25 (8c51431) SIDEExplicitFormula/Schema/PlateauRamp.lean :19-:20 reads that Mathlib at the pin holds the '
         'convolution theorem for the transform for Schwartz functions only; Mathlib at the pin, de5ce8a9, holds Real.fourier_mul_convolution_eq '
         'for integrable functions (Mathlib/Analysis/Fourier/Convolution.lean :119), at real frequency (relay data/b641_window_epstein_status.txt, '
         'W1). The docstring is edited under ruling in the review pass; no kernel byte is touched at b641.\n' % PD_HEAD),
        ('OPEN_TRAILS.md', EZ_HEAD,
         '\n%s EpsteinPremises’ count field stays OPEN, its discharger the construction of Z_Q, the zero configuration of the Epstein zeta '
         'function of x^2 + xy + 6y^2 (discriminant -23), which Mathlib at the pin does not hold (relay data/b641_window_epstein_status.txt, E1); '
         'the price is the seat`s, printed in relay data/b641_closing.txt.\n' % EZ_HEAD),
        ('OPEN_TRAILS.md', DR_HEAD,
         '\n%s TrivialSummandPremise is restated so that the pole term is carried rather than required to vanish, and dedekind_rhs is re-proved on '
         'the restated premise. Until then dedekind_rhs keeps the grade its statement reads and its row is annotated: on a premise refuted by '
         'computation at b641; the pages’ cells for it are not edited, and the correction is a dated entry in the form of ERRATA at b641`s '
         'closing. EulerFactorPremise`s counterexample at the modulus 6 and its sufficient condition (every non-trivial character primitive) are '
         'recorded beside it (relay data/b641_premise_status.txt).\n' % DR_HEAD),
        ('OPEN_TRAILS.md', NV_HEAD,
         '\n%s every premise structure in the premise table takes a non-vacuity read -- a witness exists, or the premise is marked UNWITNESSED -- '
         'before a theorem resting on it takes the interface grade; the existing table is read once under it at b642.\n' % NV_HEAD),
    ]


def workorders(*a):
    """### the author's answers at Components 3-5: the sixth status's clause beneath the five-status clause and the four work-orders, appended to
    ### OPEN_TRAILS in the order of the answers; data/b641_workorders.json."""
    Q = R2._Q()
    items = [(f, h, _poss(t)) for f, h, t in _wo_items()]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'workorders')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    oai_ = [n for n in OAI_NEEDLES if n in allt]
    print('  table cells: %s ; nd %s ; scanner %s ; odd backticks %s ; the collection named %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN',
                                                                                              ticks or 'NONE', oai_ or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or oai_:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS -- NOTHING WRITTEN')
    _land(Q, items, 'b641_workorders.json', FIVE_CLAUSE)


# ================================================================================ THE TABLE AND THE ROOT
def table(*a):
    import b638_record as R8
    rows0 = _table()
    before = R8.R7._table_state(rows0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = _table()
    after = R8.R7._table_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b641 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d' % (utc(), r.returncode), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(rows1), len(added), len(gone), len(moved)),
         '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b641_table_final.txt', L)
    put_json('b641_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b641_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b641_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    """### (R251)(3): the act root, the last step of the act -- after the last declared seal re-run; no bank it names is written after it."""
    banks = root_banks()
    print('  banks named: %d ; the seal bank among them %s' % (len(banks), 'data/b641_seal_hashes.json' in banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b641'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the root recomputed from its banked items offline and a one-byte change on a copy of one bank moving it; and the local part of
    ### verify -- every bank the root names unchanged and none written after the root -- read without a remote (the remote reads are the suite's).
    ### Writes data/b641_root_arm.* , which the root does not name."""
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b641_act_root.json')
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
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b641 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; banks named %d ; changed or written after the root: %s' % (J.get('at'), len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b641_root_arm.txt', L)
    put_json('b641_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


# ================================================================================ THE SCORES AND THE RECORD
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
SIX_BANKS = ('b641_phrase_provenance', 'b641_keiper_status', 'b641_window_epstein_status', 'b641_patch_versions', 'b641_premise_status',
             'b641_openai_math_read')
N5_ALLOWED = {'data/b640_closing_push_out.txt', 'data/act_roots.txt', K.NEEDLE_TOOL, K.NEEDLE_TEST, K.ORDER_TOOL, K.ORDER_TEST}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
OAI_NEEDLES = ('openai', 'OpenAI', 'Quasi-Riemann', 'QuasiRiemann', 'seven_eighths', 'Comparator')


def TRAIL_HEAD():
    return ('### b641 — lane three, act sixty-eight under (R251): the needle and the root order; the provenance of a phrase; Keiper’s seven, the '
            'window’s two, the Epstein count field, the Dedekind premises and the patch versions each at one status with its reason; the '
            'an outside repository’s sources read and banked in relay')


def _test_of(name):
    x = jl('b641_tests_stepzero.json').get(name) or {}
    return x.get('rc'), x.get('cases'), x.get('passing')


def _oai_in_ledgers():
    """### every byte this act appends to FINDINGS and OPEN_TRAILS, searched for the collection's names."""
    hits = []
    for f in N5_PP:
        pre = R2.cr0(subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, f)], capture_output=True).stdout) or b''
        now = R2.cr0(open(os.path.join(PP, f), 'rb').read())
        add = now[len(pre):].decode('utf-8', 'replace') if now.startswith(pre) else now.decode('utf-8', 'replace')
        hits += ['%s: %s' % (f, n) for n in OAI_NEEDLES if n in add]
    return hits


def n5(trail_line=None):
    ot_text = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD():
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD() not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d' % trail_line
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b641_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b641_|audit_b641_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    six = [b for b in SIX_BANKS if not os.path.exists(os.path.join(D, b + '.txt'))]
    oai_hits = _oai_in_ledgers()
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not differ and not six and not oai_hits and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposited (no platform called); the kernels unmoved %s; PLACE-papers %s (beyond: %s); %s; relay beyond the act`s own '
            'banks and tools, the needle repair and its test, the root-order edit and its test: %s; the six banks absent: %s; sealed tools not '
            'agreeing %s; the collection named in the ledgers` appends: %s; b628`s bank untracked %s; no identifier of the author in any outbound '
            'request' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', six or 'NONE', differ or 'NONE', oai_hits or 'NONE',
                         untracked_local))


def scores(*a):
    TF, RA, ST, PH = (jl(n_) for n_ in ('b641_table_final.json', 'b641_root_arm.json', 'b641_tests_stepzero.json', 'b641_phrase_provenance.json'))
    tl = [x for x in a if x.startswith('trail_line=')]
    _r, _n, sh = seal_hashes()
    nd_rc, nd_n, nd_p = _test_of('test_reader_needle_b641.py')
    ro_rc, ro_n, ro_p = _test_of('test_act_root_order_b641.py')
    clean_tests = [n for n, x in ST.items() if x.get('rc') == 0 and not x.get('failing')]
    obs = [o for o in K.OBLIGATIONS]
    bad = _n3(obs)
    banked = all(os.path.exists(os.path.join(D, b + '.txt')) for b in ('b641_keiper_status', 'b641_window_epstein_status', 'b641_patch_versions',
                                                                       'b641_premise_status'))
    texts = ''.join(rd(b + '.txt') for b in ('b641_keiper_status', 'b641_window_epstein_status', 'b641_patch_versions', 'b641_premise_status'))
    each = all(('### (%s) ' % o['key']) in texts or o['key'] == 'P1' for o in obs) and '### STATUS : ' in rd('b641_patch_versions.txt')
    reps = PH.get('repos') or {}
    S = {
        'N1': (('HELD' if nd_rc == 0 and nd_n == 3 and nd_p == 3 else 'REFUTED'),
               'the repaired needle`s test %s of %s: the planted denial no match, the planted assertion a match, the three hand-read answers 3 of 3' % (nd_p, nd_n)),
        'N2': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and not RA.get('late') else 'REFUTED') if RA else 'PENDING',
               'b641`s root recomputed from its banked items %s and every bank it names unchanged and unwritten after it %s, read locally; the '
               'remote reads are the suite`s (G-ACTROOT-VERIFY, pre-push and post-push)' % (RA.get('root_recomputed') == RA.get('root'), not RA.get('late'))),
        'N3': (('HELD' if banked and each and not bad else 'REFUTED'),
               'obligations and premises %d, each one of %s with a reason and a discharger: without %s ; none presumed ; each printed in its bank %s' % (
                   len(obs), '/'.join(K.STATUSES), bad or 'NONE', each)),
        'N4': (('HELD' if reps and all(v.get('commit') for v in reps.values()) else 'REFUTED'),
               'the entering commits: %s ; the rulings they name: %s' % (dict((k, (v.get('commit') or '')[:8]) for k, v in reps.items()),
                                                                         dict((k, v.get('rulings') or 'none named') for k, v in reps.items()))),
        'N5': n5(int(tl[0].split('=')[1]) if tl else None),
        'S1': (('HELD' if nd_rc == 0 and nd_p == nd_n == 3 and ro_rc == 0 and ro_p == ro_n == 5 else 'REFUTED'),
               'the needle`s test %s of %s and the root-order test %s of %s, each committed alone with its edit' % (nd_p, nd_n, ro_p, ro_n)),
        'S2': (('HELD' if ST and len(clean_tests) == len(ST) else 'REFUTED'), 'every test file clean at step zero: %d of %d' % (len(clean_tests), len(ST))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED') if TF else 'PENDING',
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED') if RA else 'PENDING',
               'the root recomputed equal and the one-byte control moving it'),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED'), 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b641_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:260]))


TITLE = ('## The needle and the root order; the provenance of a phrase; Keiper’s seven, the window’s two, the Epstein count field, the Dedekind '
         'premises and the patch versions each at one status with its reason; an outside repository’s sources read and banked in relay')
# ### the author's answer before the seal (prompt 1, option 2): (R251)(6) governs -- the title and the trail head carry the neutral clause, no
# ### collection is named and no other ledger line is about it; the ferry's title is the navigator's, recorded as such in the defect bank.


def _finding_text():
    S, rl, J, PH = (jl(n_) for n_ in ('b641_scores.json', 'b641_record_lines.json', 'b641_act_root.json', 'b641_phrase_provenance.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b641_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    cnt = collections.Counter(o['status'] for o in K.OBLIGATIONS)
    rp = PH.get('repos') or {}
    e = ['', TITLE, '',
         '*Filed at b641 on the author’s ruling `(R251)` and the author’s answers (%d). Banks: relay `data/b641_phrase_provenance.txt`, '
         '`data/b641_keiper_status.txt`, `data/b641_window_epstein_status.txt`, `data/b641_patch_versions.txt`, `data/b641_premise_status.txt`, '
         '`data/b641_act_root.txt`.*' % n_ans, '',
         '**The needle** (Component 0, `(R251)`(2)): Question 1’s needle in relay tools/b640_record.py repaired so that it matches an assertion of '
         'the unsupported sentence and not a denial of it, every alternative read inside its own sentence (relay %s, alone); its test plants the '
         'reader’s denial (no match) and an assertion (a match) and reads the three hand-read answers at 3 of 3. N1 %s.' % (
             K.NEEDLE_COMMIT, (S.get('N1') or ['?'])[0]), '',
         '**The root order** (Component 0, `(R251)`(3)): relay tools/act_root.py refuses a root that leaves out the act’s seal bank and reads a '
         'bank written after the root as DISAGREE (relay %s, alone; its test 5 of 5); b640’s root stands with its defect (h), b641’s appended '
         'beneath it. N2 %s.' % (K.ORDER_COMMIT, (S.get('N2') or ['?'])[0]), '',
         '**The phrase** (Component 2, `(R251)`(4)): entered in PLACE-papers at %s and in relay at %s, each commit naming %s; printed with the '
         'line it entered on (relay data/b641_phrase_provenance.txt). N4 %s.' % (
             (rp.get('PLACE-papers') or {}).get('commit', '?')[:8], (rp.get('relay') or {}).get('commit', '?')[:8],
             ' and '.join(sorted(set(', '.join(v.get('rulings') or ['no ruling']) for v in rp.values()))) or '?', (S.get('N4') or ['?'])[0]), '',
         '**The research discharge** (Components 3-5, `(R251)`(5)): %d obligations and premises read at SIDE-explicit-formula 8c51431 with '
         'Mathlib at its pin and the references fetched -- %d discharged, %d cited, %d open, each with its reason in one sentence and its '
         'discharger named; Keiper’s seven are KeiperObligations’ four and BoundPremises’ three (OPEN_TRAILS :12380). The four Keiper '
         'identities read true by the kernel’s definitions and unproved past their first index; the bounds need thirty digits that neither '
         'Mathlib nor the references read (DLMF 5.2.3, twenty digits) supply; the window’s convolution step is reachable from Mathlib’s '
         'convolution theorem for integrable functions, which the pin holds although PlateauRamp’s docstring reads it for Schwartz '
         'functions only; the Epstein count is a hypothesis with no construction of its configuration; TrivialSummandPremise is false as '
         'stated by the seat’s computation (the pole term is positive at a bump supported inside (-log 2, log 2)), and EulerFactorPremise '
         'holds where every non-trivial character is primitive and fails at the modulus 6; the patch versions are resolved and not written. '
         'Every candidate declaration was put to the author as a statement and written nowhere. N3 %s.' % (
             len(K.OBLIGATIONS), cnt['DISCHARGED'], cnt['CITED'], cnt['OPEN'], (S.get('N3') or ['?'])[0]), '',
         '**The record lines** (`(R251)`(1)-(3), (7)): b640 at its weight (FINDINGS :%s); the ceiling’s sentence not supported and not forbidden, '
         'the record carrying no `forbidden` of it (OPEN_TRAILS :%s); W-ORD-ROOT-ORDER (:%s); W-ORD-STATEMENT-PIN priced at two acts (:%s).' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line')), '',
         '**The root.** b641 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b640’s status print (FINDINGS :7911) field by field for the heads (5) names, '
         'and b631’s Dedekind instance (Schema/Dedekind.lean) by the truth of its two premises; it strengthens the programme’s offering of an '
         'assumption list a reader can check -- what each open premise would take to close, and which of them cannot close as stated.', '',
         '**Next.** Per `(R251)`(8): b642, the author’s word pending, the census at v0.7 with the status column from (5), read by the second reader.', '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a status reads a kernel’s constructions, its proofs and the '
         'references read, and confers nothing.*', '']
    return TITLE, NL.join(e)


FOR_AUTHOR = ('(1) Keiper’s seven read as KeiperObligations’ four fields and BoundPremises’ three, the obligations OPEN_TRAILS :12380 names; '
              '(2) the needle repaired in b640’s record tool, where it stands, with its test beside it; (3) the record’s `forbidden` read in FINDINGS '
              'and OPEN_TRAILS, no line of the ceiling found, so the reading line appended and nothing edited; (4) the act root computed after the '
              'last bank it names and before the record lines that carry it; (5) the outside repository’s files read from the clone’s objects, its working '
              'tree’s checkout being partial on this machine')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b641_scores.json', 'b641_findings.json', 'b641_record_lines.json', 'b641_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b641_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R251) ratified.** (1) b640 at its weight. (2) The ceiling’s wording and the needle. (3) W-ORD-ROOT-ORDER. (4) The phrase’s '
             'provenance. (5) The research discharge. (6) An outside repository’s sources read and banked in relay, entering no ledger. (7) W-ORD-STATEMENT-PIN. (8) The act after: b642.', '',
             '**Entered:** FINDINGS.md:%s (b640’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the ceiling’s wording), :%s (W-ORD-ROOT-ORDER), :%s '
             '(W-ORD-STATEMENT-PIN); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line')), '',
             '**Act root:** b641 `%s` (previous `%s`, b640’s; relay data/act_roots.txt), computed after the last bank it names.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b641_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): b642 names no kernel terminal; the census’s status column reads the banks of (5).', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b641_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R251)`(8), b642, the author’s word pending; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b641_scores.json')
    L = ['=' * 104, 'b641 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rd('b641_defects.txt').rstrip(NL).split(NL)
    put_txt('b641_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b641_scores.json', 'b641_findings.json', 'b641_trail.json', 'b641_record_lines.json', 'b641_act_root.json'))
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}]
    cnt = collections.Counter(o['status'] for o in K.OBLIGATIONS)
    L = ['b641 -- THE COMPONENTS, BANKED UNDER (R251).', '',
         '### COMPONENT 0 : step zero (data/b641_tests_stepzero.txt, data/b641_arms_prerun.txt, the seal`s hashes) ; the needle %s ; the root order %s' % (
             K.NEEDLE_COMMIT, K.ORDER_COMMIT),
         '### COMPONENT 1 : b640`s weight FINDINGS :%s ; the ceiling`s wording OPEN_TRAILS :%s ; W-ORD-ROOT-ORDER :%s ; W-ORD-STATEMENT-PIN :%s' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line')),
         '### COMPONENT 2 : the phrase (data/b641_phrase_provenance.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 3 : Keiper`s seven (data/b641_keiper_status.txt)',
         '### COMPONENT 4 : the window`s two and the Epstein count field (data/b641_window_epstein_status.txt)',
         '### COMPONENT 5 : the Dedekind premises and the patch versions (data/b641_premise_status.txt, data/b641_patch_versions.txt) ; '
         'obligations %d : discharged %d, cited %d, open %d ; N3 %s' % (len(K.OBLIGATIONS), cnt['DISCHARGED'], cnt['CITED'], cnt['OPEN'], S['N3'][0]),
         '### COMPONENT 6 : the openai/math read (data/b641_openai_math_read.txt), the clone at %s' % K.CLONE,
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'))]
    put_txt('b641_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    e = _poss(e)
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE ENTRY -- NOTHING WRITTEN')
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    oai_ = [n for n in OAI_NEEDLES if n in e]
    print('  table cells: %s ; nd %s ; scanner %s ; the collection named: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', oai_ or 'NONE'))
    if 'dry' in a:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or oai_:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b641_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _poss(_trail_text())
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE RECORD -- NOTHING WRITTEN')
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    oai_ = [n for n in OAI_NEEDLES if n in e]
    print('  table cells: %s ; nd %s ; scanner %s ; the collection named: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', oai_ or 'NONE'))
    if 'dry' in a:
        print(e[:6000])
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or oai_:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b641_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b641_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-08 by b641 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD())
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    if 'dry' in a:
        print(t)
        return
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b641_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


# ================================================================================ THE DISPATCHER
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'seal_hashes', 'answer_of', 'n5', 'put_txt', 'put_json', 'TRAIL_HEAD',
                                                          'act_from', 'READS', 'root_banks'):
        print('usage: b641_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
