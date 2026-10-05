# -*- coding: utf-8 -*-
"""b620_record.py -- THE ACT'S RECORD TOOL, UNDER (R230). ### ONE SUBCOMMAND PER BANK.

### ### b620: LANE THREE, ACT FORTY-SEVEN -- THE SECOND READER: THE PACKET BUILT WITHOUT REASONS, GRADES OR ACT NUMBERS; THE READER RUN
### IN A FRESH SESSION THE AUTHOR OPENS; THE AGREEMENT RATES BANKED AND THE DISAGREEMENTS LISTED.
### Subcommands write only `data/b620_*` unless the docstring names another file; `dry` on the command line routes every b620 bank, the
### packet and the prompt to the seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are
### written by encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. Every item of the packet is read from a
### relay bank or a PLACE-papers blob at a pin, and none from recall. No platform call. No Lean call: both pages are re-emitted from their
### banked probes. The templates are tools/b619_record.py and tools/b618_record.py. The N5 scorer takes the trail record's expected line
### (OPEN_TRAILS :12799, the standing line of (R229)(2)).
"""
import ast
import difflib
import io
import json
import os
import random
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = 'ee75fcf'
PRE_RELAY = '958e574c'
STEPZERO = '3408ac33'
DATE = '2026-10-04'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a7f90da7-bccd-48d0-914d-84e76892ff54/scratchpad'
SESSION_ID = 'a7f90da7-bccd-48d0-914d-84e76892ff54'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
SEED = 620230          # ### the shuffle's and the samples' seed, banked in the key
PACKET = 'b620_reader_packet'
PROMPT = 'b620_reader_prompt.txt'
ANSWERS = 'b620_reader_answers.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b620_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    d = os.path.dirname(p)
    if not os.path.isdir(d):
        os.makedirs(d)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b620_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    t = (t or '').replace(chr(13), '')
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


READER_NOTE = ('the reader ran headless from the scratch directory D:\\reader_b620 with no memory, run by the author in the author`s own '
               'terminal, its transcript audited (relay data/b620_reader_run.txt, no contamination); an earlier session which received the '
               'ferry halted without reading the packet (the author`s answer at the hold)')
DEFECTS = [
    '(a) THE SEAT`S, ON THE AUTHOR`S ANSWER AT THE HOLD, AFTER THE SEAL: the face`s (Z) says this act`s record tool takes no edit after the '
    'seal; the author`s answer ordered a note on H54a-H54c of how the reader ran, so the record tool took one edit through the Edit tool '
    '(READER_NOTE, carried into the keying`s H54 lines and the scores), the face`s sentence refuted in its letter. The author`s answer also '
    'ordered the seat to launch the reader itself; that launch was refused by the session`s permission classifier, the seat did not pursue '
    'it, and the author ran the reader in the author`s own terminal.',
    '(b) THE SEAT`S, AT THE AUDIT: relay data/b620_reader_run.txt, the bank the author`s answer ordered, was written by a script in the seat`s '
    'scratchpad (reader_audit.py; a first attempt through a bash heredoc failed on its backslashes before writing anything), not by a '
    'subcommand of this act`s record tool, which had none for it.',
    '(c) THE SEAT`S, AT COMPONENT 6, BEFORE THE RECORD: the N5 scorer carried from b619 lists OPEN_TRAILS in the face`s write list throughout '
    'and compared the changed files exactly; in this act the trail record is OPEN_TRAILS` only write, so before it the scorer read REFUTED '
    'and after it would read HELD -- the converse of the defect the standing repair (OPEN_TRAILS :12799) closes. Corrected through the Edit '
    'tool to count OPEN_TRAILS as written while the record is pending at its expected line; the scores banked again before the record, and '
    'the first scores bank not kept.',
]
DEFECT_SHORT = ['(a) the seat’s: the record tool took one edit after the seal, on the author’s answer at the hold, to carry the note on how the '
                'reader ran into H54a-H54c, the face’s (Z) refuted in its letter; the seat’s own launch of the reader, which the answer also '
                'ordered, was refused by the session’s permission classifier and the author ran it',
                '(b) the seat’s: the reader’s run bank was written by a scratchpad script, not by a subcommand of the record tool',
                '(c) the seat’s: the carried N5 scorer read REFUTED before the trail record, OPEN_TRAILS’ only write in this act, the converse of '
                'the defect the standing repair closes; corrected through the Edit tool to count the pending record as the write, the scores '
                'banked again before the record']


def defects(*a):
    L = ['b620 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b620_defects.txt', L)


# ================================================================================ THE BATCH, ITS BANKS AND ITS DOCUMENTS
MONO = [('v5.14', 'b606_edition_PLACE.txt'), ('v5.15', 'b607_edition_PLACE.txt'), ('v5.16', 'b608_edition_PLACE.txt')]
SIEVE = [('v0.2', 'b604_edition_FINDINGS_STAND.txt'), ('v0.3', 'b605_edition_FINDINGS_STAND.txt'), ('v0.4', 'b609_edition_FINDINGS_STAND.txt'),
         ('v0.5', 'b617_edition_FINDINGS_STAND.txt')]
SIEVE_FILES = {'cur': ('phase2/method/THE_FINDINGS_AS_THEY_STAND.md', '24e7ff2'), 'v0.2': ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md', PRE_PP),
               'v0.3': ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md', PRE_PP)}
SYN = [   # (row key, the synthesis file, the act's claims module, the cluster)
    ('P12', 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'b611_claims.py', 'Phase 1.2'),
    ('15E', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md', 'b612_claims.py', '1.5E'),
    ('2B', 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 'b613_claims.py', '2B'),
    ('2D', 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md', 'b614_claims.py', '2D'),
    ('2F', 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md', 'b615_claims.py', '2F'),
    ('2G', 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md', 'b616_claims.py', '2G'),
]
GRADES = ('kernel-verified', 'theorem-supported', 'computationally-verified', 'argument-supported', 'synthesis-suggested', 'statement-grade')
RESIDUE = [('b609_residue_seed.txt', 'the seed'), ('b610_residue_addendum.txt', 'the enumeration needle`s addendum'),
           ('b614_second_reader_addendum.txt', 'the silence-principle addendum')]
SEED_DOCS = {'v5.16': ('day1/A_Place_to_Stand_v5_16.md', '3d2f67d'), 'v0.3': ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md', '3d2f67d')}
ACT_RE = re.compile(r'\bb\d{3}\b')
GRADE_RE = re.compile(r'\b(%s)\b' % '|'.join(re.escape(x) for x in GRADES))
MARK_RE = re.compile(r'\b(NOT KIN|KIN|LABEL|DATED|MOVED-IN-MEANING|STANDS)\b')
CEIL_LINES = (106, 111)     # ### README :106, the supportable sentence, and the unsupportable one beside it to its paragraph's end (:111); the
#                             ferry's ":121" is the end of the range the ceiling clause cites (:106-:121), the dated annotations beside it


def _rel(n):
    return _show(RELAY, PRE_RELAY, 'data/' + n) or ''


# ================================================================================ READING (1): THE READS
OT_LINES = [11864, 12212, 12228, 12542, 12673, 12799, 12801]
READS = [
    ('OPEN_TRAILS: the work-order, the batch, the precedence order, the form, the needle line, b619`s standing line and record', PP, PRE_PP,
     'OPEN_TRAILS.md', OT_LINES, 1600),
    ('README: the ceiling sentence', PP, PRE_PP, 'README.md', list(range(CEIL_LINES[0], CEIL_LINES[1] + 1)), 600),
] + [('the diff bank of the monograph`s %s: its section heads' % v, RELAY, PRE_RELAY, 'data/' + b, ('GREP', r'^### '), 220) for v, b in MONO] + [
    ('the diff bank of the sieve`s %s: its section heads' % v, RELAY, PRE_RELAY, 'data/' + b, ('GREP', r'^### '), 220) for v, b in SIEVE] + [
    ('%s: its head and marks' % lab, RELAY, PRE_RELAY, 'data/' + b, ('GREP', r'^(b6\d\d --|### )'), 300) for b, lab in RESIDUE] + [
    ('the synthesis`s grading rule and Correspondence head', PP, PRE_PP, f, ('GREP', r'^(### The grading rule|- \*\*kernel-verified\*\*|## Correspondence|\| claim \|)'), 600)
    for _k, f, _m, _c in SYN] + [
    ('the no-disclosure arm`s needle sets, by name (relay tools/b616_record.py)', RELAY, PRE_RELAY, 'tools/b616_record.py', ('GREP', r'^def nd_'), 200),
    ('relay data/b619_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b619_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ('FINDINGS: b619`s weight and entry', PP, PRE_PP, 'FINDINGS.md', [7402, 7404], 600),
]


def reads(*a):
    L = ['b620 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b620_reads.txt', L)


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
    since = [c for c in calls if c[0] > SESSION_FROM]
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b620 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b620_author_answers.txt', L)


SESSION_FROM = 954   # ### the transcript line before this act's ferry (its paste at :955); b619 shares the session

KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7'}


def kern_state(ks=None):
    out = {}
    for k in (ks or KERNS):
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    put_json('b620_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B619_ENTRY = '## THE_KEYSTONE_CENSUS at v0.4: the six syntheses in their rows with tiers, 42 cells refreshed'
W_HEAD = '*Appended 2026-10-04 by b620 to b619’s entry (:%d), under `(R230)`(1) -- b619 AT ITS WEIGHT:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry):
    j = lambda p: json.loads(_rel(p))   # noqa: E731
    S, RL, FJ, TJ, CJ = j('b619_scores.json'), j('b619_record_lines.json'), j('b619_findings.json'), j('b619_trail.json'), j('b619_census.json')
    S = {k: v[0] for k, v in S.items()}
    pre, post, mid = (_count_bank(_rel(n)) for n in ('b619_checks.txt', 'b619_checks_postpush.txt', 'b619_checks_mid.txt'))
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    H = CJ['h53']
    return ('\n%s THE_KEYSTONE_CENSUS v0.4 beside v0.3, unedited (PLACE-papers 6a3069e): %d cells in %d rows, each old to new with its '
            'source in the mapping banked before the edition (relay data/b619_census.txt); the six syntheses named with path, version and tier '
            '-- Phase 1.2 KC, 1.5E KC, 2B C, 2D C at its v0.2, 2F C, 2G C -- read back equal to their heads; the no-keystone section at the '
            'ANNEX alone, with its reason (REGISTRY :360; OPEN_TRAILS :12595); the kernel-tag column read by ls-remote once per repository, %d '
            'kernels carrying %d unpushed tags, the nine of W-ORD-TAG-REMOTES, each named in its cell; the sieve column at v0.5, the Simplicity '
            '/ RH cascade at 70 rows; re-pin 34 of 34, the scanner clean. The N5 scorer: the record tool committed as sealed (a975611b), then '
            'its parameter with its test (760973ab); n5(trail_line, ot) HELD before and after the trail write at Components 4 and 6, the '
            'sealed form, the test’s positive control, REFUTED then HELD -- the old defect reproduced and the repair shown. H28a-H28c HOLD '
            '(H28a vacuous); H53a-H53d %s; N1-N5 %s; S1-S6 %s; the mid-act run %d of %d by design, the suite %d of %d before the push and '
            '%d of %d after it. FINDINGS :%d, :%d; OPEN_TRAILS :%d (the N5 standing line, addressed to :12356), :%d. Relay 958e574c; '
            'PLACE-papers ee75fcf. Defect (a), the seat’s: two edits of the record tool beyond the ruled one, through the Edit tool, '
            'recorded. Confirmed by the author: b618’s Version cells read as a layer over the rows they point to; the 2B-2G headings placing '
            'their rows, and 1.5a-9 and 1.5a-10 in Phase 1.2 by their provenance; the 2C row at p2-39 to p2-42 with the census at C; the '
            'navigator’s “monograph v5.17 ... SPIRAL_MAP v0.7” already v0.3’s state, the navigator’s; v0.3’s back matter carried whole and '
            'not re-pinned. Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, len(CJ['changes']), len(set(c['row'] for c in CJ['changes'])), len(H['unpushed']), H['n_tags'],
                'HOLD' if all(S[k] == 'HOLDS' for k in ('H53a', 'H53b', 'H53c', 'H53d')) else [S[k] for k in ('H53a', 'H53b', 'H53c', 'H53d')],
                allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5', 'S6'), 'HELD'), mid[0], mid[1], pre[0], pre[1],
                post[0], post[1], RL['lines'][0]['line'], FJ['entry_line'], RL['lines'][1]['line'], TJ['line']))


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b620_scanfile_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', p], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout, re.search(r'^\s*VERDICT\s*: CLEAN\s*$', r.stdout, re.M) is not None


def record_lines(*a):
    """### FINDINGS: b619's weight, addressed to b619's entry, appended at the end."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B619_ENTRY)
    if entry != 7404:
        sys.exit('### THE ADDRESSED LINE MOVED (%s) -- NOTHING WRITTEN' % entry)
    wt = _weight(entry)
    bad = ledger_check(wt)
    nd, _n = _nd(wt)
    sc, clean = _scan_text(wt, 'weight')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(wt)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    r = Q.append_to(Q.FIND, wt)
    out = [dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r)]
    put_json('b620_record_lines.json', dict(entry=entry, lines=out))
    print('  FINDINGS.md :%s' % out[0]['line'])


# ================================================================================ COMPONENT 2: THE EXTRACTION
def _block(lines, head, stop=r'^### '):
    i = next((k for k, l in enumerate(lines) if l.startswith(head)), None)
    if i is None:
        return []
    out = []
    for k in range(i + 1, len(lines)):
        if re.match(stop, lines[k]):
            break
        out.append((k + 1, lines[k]))
    return out


def subs_mono():
    out = []
    for v, b in MONO:
        L = lines_of(_rel(b))
        blk = _block(L, '### EVERY REWRITTEN SENTENCE')
        head = None
        for k, (n, l) in enumerate(blk):
            m = re.match(r'^  (\S+)\s+v5\.\d+ :(\d+) -> v5\.\d+ :(\d+)', l)
            if m:
                head = (m.group(1), int(m.group(2)), int(m.group(3)))
            if l.startswith('      was : ') and k + 1 < len(blk) and blk[k + 1][1].startswith('      now : '):
                out.append(dict(doc='the monograph', edition=v, bank=b, bank_line=n, item=head[0] if head else '?', old_line=head[1] if head else None,
                                new_line=head[2] if head else None, was=l[len('      was : '):], now=blk[k + 1][1][len('      now : '):]))
    return out


def subs_sieve():
    out = []
    cur_f, cur_rev = SIEVE_FILES['cur']
    cur = lines_of(_show(PP, cur_rev, cur_f))
    v2 = lines_of(_show(PP, PRE_PP, SIEVE_FILES['v0.2'][0]))
    v3 = lines_of(_show(PP, PRE_PP, SIEVE_FILES['v0.3'][0]))
    # ### v0.2: the superseded conclusions (MOVED-IN-MEANING), each the current version's lines against the row it now sits in
    L = lines_of(_rel('b604_edition_FINDINGS_STAND.txt'))
    rows = {}
    for n, l in _block(L, '### EVERY ROW, WITH THE EDITION LINE'):
        m = re.match(r'^      v0\.2 : (\| (\S+) \|.*)$', l)
        if m:
            rows.setdefault(m.group(2), (n, m.group(1)))
    for n, l in _block(L, '### THE SUPERSEDED CONCLUSIONS'):
        m = re.match(r'^  (c\d+) :(\d+)-(\d+) -> (\S+) citing', l)
        if m:
            a_, b_ = int(m.group(2)), int(m.group(3))
            out.append(dict(doc='the sieve', edition='v0.2', bank='b604_edition_FINDINGS_STAND.txt', bank_line=n, item=m.group(1),
                            old_line=a_, new_line=None, was=' '.join(cur[a_ - 1:b_]).strip(), now=rows[m.group(4)][1]))
    # ### v0.3: every changed row (its v0.2 line against its v0.3 line) and every other rewrite
    L = lines_of(_rel('b605_edition_FINDINGS_STAND.txt'))
    for n, l in _block(L, '### EVERY CHANGED ROW, PRINTED'):
        m = re.match(r'^  (\S+)\s+v0\.2 :(\d+) -> v0\.3 :(\d+)', l)
        if m:
            a_, b_ = int(m.group(2)), int(m.group(3))
            out.append(dict(doc='the sieve', edition='v0.3', bank='b605_edition_FINDINGS_STAND.txt', bank_line=n, item=m.group(1), old_line=a_,
                            new_line=b_, was=v2[a_ - 1], now=v3[b_ - 1]))
    for n, l in _block(L, '### EVERY OTHER REWRITE'):
        m = re.match(r'^  :(\d+) <- :(\d+)\s', l)
        if m:
            b_, a_ = int(m.group(1)), int(m.group(2))
            out.append(dict(doc='the sieve', edition='v0.3', bank='b605_edition_FINDINGS_STAND.txt', bank_line=n, item=':%d' % b_, old_line=a_,
                            new_line=b_, was=v2[a_ - 1], now=v3[b_ - 1]))
    # ### v0.4 and v0.5: every rewrite's fragments
    for v, b in SIEVE[2:]:
        L = lines_of(_rel(b))
        blk = _block(L, '### EVERY REWRITE')
        head = None
        for k, (n, l) in enumerate(blk):
            m = re.match(r'^  :(\d+) <- :(\d+)\s', l)
            if m:
                head = (int(m.group(2)), int(m.group(1)))
            if l.startswith('      was : ') and k + 1 < len(blk) and blk[k + 1][1].startswith('      now : '):
                out.append(dict(doc='the sieve', edition=v, bank=b, bank_line=n, item=':%d' % head[1], old_line=head[0], new_line=head[1],
                                was=l[len('      was : '):], now=blk[k + 1][1][len('      now : '):]))
    return out


def _papers(mod):
    """### the synthesis act's own paper map and pin, imported from its claims module (each defines them at the top and runs nothing)"""
    import importlib
    M = importlib.import_module(mod[:-3])
    return {k: v[0] for k, v in M.PAPERS.items()}, M.PRE_PP


def _cited(cell):
    """### the paper key and the line numbers a `paper :line` cell cites (ranges expanded, at most 12 lines each)"""
    m = re.match(r'^([A-Z][A-Z0-9]*)\b', cell.strip())
    key = m.group(1) if m else None
    nums = []
    for a_, b_ in re.findall(r':(\d+)(?:\s*[-–]\s*:?(\d+))?', cell):
        a_ = int(a_)
        b_ = int(b_) if b_ else a_
        nums += list(range(a_, min(b_, a_ + 11) + 1))
    return key, sorted(set(nums))


def syn_rows():
    """### every Correspondence row of the six syntheses whose grade is in the vocabulary: (cluster, id, claim, cited, grade)"""
    out = []
    for key, f, mod, clu in SYN:
        papers, pin = _papers(mod)
        t = lines_of(_show(PP, PRE_PP, f))
        i = next(k for k, l in enumerate(t) if l.startswith('## Correspondence'))
        cache = {}
        for l in t[i:]:
            if l.startswith('### '):
                break
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            if len(c) < 5 or not re.match(r'^[A-Z][A-Z0-9]*-\d+$', c[0]) or c[3] not in GRADES:
                continue
            pk, nums = _cited(c[1])
            if pk not in papers:
                continue
            path = papers[pk]
            if path not in cache:
                cache[path] = lines_of(_show(PP, pin, path))
            lines = [(n, cache[path][n - 1]) for n in nums if 0 < n <= len(cache[path])]
            out.append(dict(cluster=clu, key=key, synthesis=f, id=c[0], claim=c[2], cell=c[1], paper=path, pin=pin, lines=lines, grade=c[3]))
    return out


def _sentence(text, word):
    """### the sentence of a line holding a word (the residue banks' own quote preferred; else the line split at sentence ends)"""
    parts = re.split(r'(?<=[.;!?])\s+(?=[A-Z*`(“"])', text)
    for p in parts:
        if word and word.lower() in p.lower():
            return p.strip()
    return text.strip()


def residue():
    out = []
    for b, lab in RESIDUE:
        L = lines_of(_rel(b))
        sect = None
        for k, l in enumerate(L):
            if l.startswith('### v5.16'):
                sect = 'v5.16'
            elif l.startswith('### THE SIEVE') or l.startswith('### the sieve') or l.startswith('### THE SIEVE`S'):
                sect = 'v0.3'
            m = re.match(r'^  :(\d+)\s+(M\d)\s+(NOT KIN|KIN|LABEL|DATED)\s+\[([^\]]*)\]\s*(.*)$', l) if b == RESIDUE[0][0] else None
            if m:
                doc, rev = SEED_DOCS.get(sect or 'v5.16')
                n = int(m.group(1))
                q = L[k + 1].strip() if k + 1 < len(L) and L[k + 1].strip().startswith('“') else None
                if q and not q.startswith('“…'):
                    s = q.strip('“”')
                else:
                    s = _sentence(lines_of(_show(PP, rev, doc))[n - 1], m.group(4))
                out.append(dict(source=lab, bank=b, bank_line=k + 1, doc=doc, rev=rev, line=n, mark=m.group(3), sentence=s))
                continue
            m = re.match(r'^  (\S+\.md) :(\d+)\s+(NOT KIN|KIN)\s+', l)
            if m:
                q = L[k + 1].strip() if k + 1 < len(L) else ''
                out.append(dict(source=lab, bank=b, bank_line=k + 1, doc=m.group(1), rev=None, line=int(m.group(2)), mark=m.group(3),
                                sentence=q.strip('“”') if q.startswith('“') else '?'))
    seen, uniq = set(), []
    for x in out:
        k = (x['doc'], x['line'], x['sentence'])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(x)
    return uniq


def _mask(s, masks, where):
    def rep(m):
        masks.append(dict(where=where, text=m.group(0)))
        return 'b—'
    return ACT_RE.sub(rep, s)


def ceiling():
    ls = lines_of(_show(PP, PRE_PP, 'README.md'))
    return ls[CEIL_LINES[0] - 1:CEIL_LINES[1]]


# ================================================================================ COMPONENT 2: THE PACKET, THE KEY, THE PROMPT
def _eligible(r):
    t = r['claim'] + ' ' + ' '.join(x for _n, x in r['lines'])
    return bool(r['lines']) and not GRADE_RE.search(t) and not ACT_RE.search(t) and not MARK_RE.search(t)


def packet(*a):
    """### data/b620_reader_packet/ (00_README.txt, 01_ceiling.txt, 02_substitutions.txt, 03_rows.txt, 04_residue.txt), data/b620_reader_prompt.txt,
    ### data/b620_key.txt and its json, data/b620_packet.json (the counts, the scans, the no-disclosure arm, H54d)."""
    import b616_record as R6
    rng = random.Random(SEED)
    masks = []
    subs = subs_mono() + subs_sieve()
    rows_all = syn_rows()
    res = residue()
    sample, elig = [], {}
    for k, (key, _f, _m, _c) in enumerate(SYN):
        pool = [r for r in rows_all if r['key'] == key and _eligible(r)]
        elig[key] = (len([r for r in rows_all if r['key'] == key]), len(pool))
        sample += random.Random(SEED + k + 1).sample(pool, 20)
    order_s = list(range(len(subs)))
    rng.shuffle(order_s)
    order_r = list(range(len(sample)))
    rng.shuffle(order_r)
    order_x = list(range(len(res)))
    rng.shuffle(order_x)
    S, R, X, key = [], [], [], dict(seed=SEED, subs=[], rows=[], residue=[], masks=masks)
    for i, j in enumerate(order_s, 1):
        x = subs[j]
        sid = 'S%03d' % i
        S += ['', '%s -- in %s' % (sid, x['doc']), '  FIRST WORDING : %s' % _mask(x['was'], masks, sid), '  SECOND WORDING: %s' % _mask(x['now'], masks, sid)]
        key['subs'].append(dict(id=sid, seat='SAME-OBJECT', **x))
    for i, j in enumerate(order_r, 1):
        r = sample[j]
        rid = 'R%03d' % i
        R += ['', '%s -- %s' % (rid, r['claim']), '  the paper: %s, lines as cited (%s)' % (os.path.basename(r['paper']), r['cell'])]
        R += ['    :%d %s' % (n, t) for n, t in r['lines']]
        key['rows'].append(dict(id=rid, seat=r['grade'], claim_id=r['id'], **{k: r[k] for k in ('cluster', 'key', 'synthesis', 'cell', 'paper', 'pin')}))
    for i, j in enumerate(order_x, 1):
        x = res[j]
        xid = 'X%03d' % i
        X += ['', '%s -- %s, line %d' % (xid, os.path.basename(x['doc']), x['line']), '  %s' % _mask(x['sentence'], masks, xid)]
        key['residue'].append(dict(id=xid, seat='BEYOND' if x['mark'] == 'KIN' else 'AT', **x))
    ce = ceiling()
    files = {
        '00_README.txt': ['The reader`s packet. Five files: this one; 01_ceiling.txt, the ceiling sentence; 02_substitutions.txt, %d pairs of '
                          'wordings; 03_rows.txt, %d claims each with the lines of the paper it cites; 04_residue.txt, %d sentences. The task is in '
                          'the prompt that came with it.' % (len(S) // 4, len(sample), len(res))],
        '01_ceiling.txt': ['The ceiling: what the programme`s documents may say of the Riemann Hypothesis, and what they may not (README.md, lines %d to '
                           '%d).' % CEIL_LINES, ''] + ce,
        '02_substitutions.txt': ['Pairs of wordings. In each pair the FIRST WORDING stood in a document and the SECOND WORDING replaced it.'] + S,
        '03_rows.txt': ['Claims. Each states what a paper claims, followed by the lines of that paper it cites, copied verbatim.'] + R,
        '04_residue.txt': ['Sentences, each with the document and line it stands at.'] + X,
    }
    pdir = os.path.join(DOUT, PACKET)
    for fn, ls in files.items():
        put_txt(PACKET + '/' + fn, ls)
    prompt = PROMPT_TEXT % dict(n_s=len(subs), n_r=len(sample), n_x=len(res), pdir='D:/relay/data/' + PACKET, out='D:/relay/data/' + ANSWERS)
    put_txt(PROMPT, prompt.split(NL))
    put_json('b620_key.json', key)
    KL = ['b620 -- THE KEY, (R230)(2): the seeded shuffle (seed %d, Python random.Random) and every item keyed to its edition, bank line and the '
          'seat`s reading; banked separately from the packet; the reader does not read it.' % SEED, '']
    KL += ['%s %-14s %-5s %-24s bank :%-5s item %-10s seat %s' % (x['id'], x['doc'], x['edition'], x['bank'], x['bank_line'], x['item'], x['seat']) for x in key['subs']]
    KL += ['%s %-4s %-8s %-60s seat %s' % (x['id'], x['key'], x['claim_id'], os.path.basename(x['synthesis']), x['seat']) for x in key['rows']]
    KL += ['%s %-34s %s :%-5s bank %s :%-4s seat %s' % (x['id'], x['source'], os.path.basename(x['doc']), x['line'], x['bank'], x['bank_line'], x['seat'])
           for x in key['residue']]
    KL += ['', '### MASKS (an act number inside an edition`s or a residue sentence`s own wording, shown to the reader as b—): %d -- %s' % (
        len(masks), ', '.join('%s %s' % (m['where'], m['text']) for m in masks) or 'none')]
    put_txt('b620_key.txt', KL)
    ptext = NL.join(NL.join(ls) for ls in files.values()) + NL + prompt
    nd, _n = R6.nd_hits(ptext)
    seat_lines = [l for fn, ls in files.items() for l in ls if not re.match(r'^  (FIRST WORDING|SECOND WORDING)|^  \S|^    :\d+ ', l)]
    scan = dict(act=ACT_RE.findall(ptext), grade=GRADE_RE.findall(NL.join(files['03_rows.txt'] + seat_lines)),
                mark=MARK_RE.findall(NL.join(NL.join(ls) for ls in files.values())),
                grade_in_wordings=GRADE_RE.findall(NL.join(files['02_substitutions.txt'] + files['04_residue.txt'])))
    by_ed = {}
    for x in subs:
        by_ed[x['doc'] + ' ' + x['edition']] = by_ed.get(x['doc'] + ' ' + x['edition'], 0) + 1
    meta = dict(at=utc(), dry=DRY, subs=len(subs), by_edition=by_ed, rows=len(sample), eligible=elig, residue=len(res),
                residue_by_source={lab: sum(1 for x in res if x['source'] == lab) for _b, lab in RESIDUE}, masks=len(masks), nd=nd, scan=scan,
                H54d='HOLDS' if not any(nd.values()) else 'REFUTED',
                files={fn: sha((NL.join(ls) + NL).encode('utf-8')) for fn, ls in files.items()}, prompt_sha=sha((prompt.rstrip(NL) + NL).encode('utf-8')))
    put_json('b620_packet.json', meta)
    print('  substitutions %d %s ; rows %d (eligible %s) ; residue %d %s ; masks %d ; no-disclosure %s ; act pattern %d ; grade words in the rows and the '
          'seat`s lines %d ; marks %d ; grade words inside the editions` and residue sentences` own wordings %d ; H54d %s' % (
              len(subs), by_ed, len(sample), elig, len(res), meta['residue_by_source'], len(masks), nd, len(scan['act']), len(scan['grade']),
              len(scan['mark']), len(scan['grade_in_wordings']), meta['H54d']))


PROMPT_TEXT = '''You are being asked to act as an independent second reader for a research programme's documents. You have no context of the work that produced them, and that is the point: read only the files named below, judge each item on its own words, and write your answers to one file. Do not open, search or read any other file in any repository on this machine, do not run git, and do not change any file except the one answer file named at the end.

The packet is the directory %(pdir)s. Read its five files: 00_README.txt, 01_ceiling.txt, 02_substitutions.txt, 03_rows.txt and 04_residue.txt.

THE CEILING. 01_ceiling.txt holds the programme's ceiling: the sentence its documents may say about the Riemann Hypothesis and the sentence they may not. A wording is BEYOND the ceiling when it says, or plainly implies, more than the supportable sentence -- for example that the hypothesis, or a step the supportable sentence leaves open, is proved, established, settled or resolved.

TASK ONE -- %(n_s)d substitutions (02_substitutions.txt). Each item gives a FIRST WORDING that stood in a document and the SECOND WORDING that replaced it. For each item answer exactly one of:
  SAME-OBJECT -- the second wording speaks of the same object or claim as the first (it may correct, narrow, qualify or restate it) and stays within the ceiling;
  DIFFERENT-OBJECT -- the second wording speaks of a different object or makes a different claim than the first;
  BEYOND-CEILING -- the second wording goes beyond the ceiling.
Give one line of reason.

TASK TWO -- %(n_r)d claims (03_rows.txt). Each item states what a paper claims, followed by the lines of that paper it cites, copied verbatim. Grade each claim by what those cited lines themselves name as its backing, using exactly one of these six grades:
  kernel-verified -- the lines name a machine-checked terminal (a compiled theorem or its file) at a pin, and the statement carries the claim;
  theorem-supported -- the lines name a theorem of the published literature for it;
  computationally-verified -- the lines report a computation;
  argument-supported -- the lines argue the claim;
  synthesis-suggested -- the lines read a pattern across results;
  statement-grade -- the lines state it without argument.
Grade no claim above what its cited lines name as its backing. Give one line of reason.

TASK THREE -- %(n_x)d sentences (04_residue.txt). For each sentence answer AT (within the ceiling) or BEYOND (beyond it). Give one line of reason.

THE ANSWER FILE. Write all your answers to %(out)s, one item per line, in the packet's own order, in exactly this form:
  S001 | SAME-OBJECT | your one line of reason
  R001 | argument-supported | your one line of reason
  X001 | AT | your one line of reason
Every item S001 to S%(n_s)03d, R001 to R%(n_r)03d and X001 to X%(n_x)03d must have exactly one line. Use no other verdict words than those above, and do not put a vertical bar inside a reason. When the file is complete, read it back once to check every item is present, then stop. Do not commit, push or edit anything else.
'''


# ================================================================================ COMPONENT 4: THE KEYING
def _answers():
    out = {}
    for l in lines_of(rd(ANSWERS)):
        m = re.match(r'^\s*([SRX]\d{3})\s*\|\s*([^|]+?)\s*\|\s*(.*)$', l)
        if m:
            out[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
    return out


def keying(*a):
    """### data/b620_agreement.txt and its json: every item keyed back, the seat's reading beside the reader's with the reader's line; the
    ### rates per edition, per synthesis and on the residue; H54a-H54c scored."""
    K = jl('b620_key.json')
    A = _answers()
    L = ['b620 -- COMPONENT 4: THE KEYING, (R230)(2): the reader`s bank (relay data/%s, %d lines read) keyed back by data/b620_key.txt, banked %s' % (
        ANSWERS, len(A), utc()), '']
    missing = [x['id'] for x in K['subs'] + K['rows'] + K['residue'] if x['id'] not in A]
    bad = [i for i, (v, _r) in A.items() if (i[0] == 'S' and v not in ('SAME-OBJECT', 'DIFFERENT-OBJECT', 'BEYOND-CEILING')) or
           (i[0] == 'R' and v not in GRADES) or (i[0] == 'X' and v not in ('AT', 'BEYOND'))]
    L += ['### items missing from the reader`s bank: %s ; verdicts outside the vocabulary: %s' % (missing or 'none', bad or 'none'), '']
    ed = {}
    dis_s = []
    L.append('### PART A -- THE SUBSTITUTIONS, EACH THE SEAT`S READING BESIDE THE READER`S (disagreements printed whole; agreements by id):')
    for x in sorted(K['subs'], key=lambda x: (x['doc'], x['edition'], x['bank_line'])):
        v, r = A.get(x['id'], ('MISSING', ''))
        k = '%s %s' % (x['doc'], x['edition'])
        e = ed.setdefault(k, [0, 0])
        e[1] += 1
        if v == x['seat']:
            e[0] += 1
            continue
        dis_s.append(dict(id=x['id'], doc=x['doc'], edition=x['edition'], bank=x['bank'], bank_line=x['bank_line'], item=x['item'],
                          new_line=x.get('new_line'), seat=x['seat'], reader=v, line=r, was=x['was'], now=x['now']))
        L += ['  %s  %s %s -- %s :%s (item %s, the edition`s line :%s) -- seat %s ; reader %s' % (x['id'], x['doc'], x['edition'], x['bank'], x['bank_line'],
                                                                                         x['item'], x.get('new_line'), x['seat'], v),
              '      was : %s' % x['was'], '      now : %s' % x['now'], '      the reader`s line: %s' % r]
    L.append('')
    L.append('### THE AGREEMENT RATE PER EDITION:')
    for k in sorted(ed):
        L.append('  %-22s %d of %d = %.3f' % (k, ed[k][0], ed[k][1], ed[k][0] / ed[k][1] if ed[k][1] else 0))
    mono = [sum(ed[k][i] for k in ed if k.startswith('the monograph')) for i in (0, 1)]
    siev = [sum(ed[k][i] for k in ed if k.startswith('the sieve')) for i in (0, 1)]
    r_m = mono[0] / mono[1] if mono[1] else 0
    r_s = siev[0] / siev[1] if siev[1] else 0
    L += ['  the monograph, all three: %d of %d = %.3f ; the sieve, all four: %d of %d = %.3f' % (mono[0], mono[1], r_m, siev[0], siev[1], r_s), '']
    L.append('### PART B -- THE SAMPLED ROWS, THE SEAT`S GRADE BESIDE THE READER`S:')
    sy, pairs, dis_r = {}, {}, []
    for x in sorted(K['rows'], key=lambda x: (x['key'], x['id'])):
        v, r = A.get(x['id'], ('MISSING', ''))
        s = sy.setdefault(x['key'], [0, 0])
        s[1] += 1
        if v == x['seat']:
            s[0] += 1
        else:
            pairs[(x['seat'], v)] = pairs.get((x['seat'], v), 0) + 1
            dis_r.append(dict(id=x['id'], key=x['key'], claim_id=x['claim_id'], seat=x['seat'], reader=v, line=r))
        L.append('  %s %-4s %-7s %-10s seat %-24s reader %-24s %s%s' % (x['id'], x['key'], x['claim_id'], x.get('cell', ''), x['seat'], v,
                                                                     '' if v == x['seat'] else '### ', r[:200]))
    ry = sum(s[0] for s in sy.values()) / max(1, sum(s[1] for s in sy.values()))
    L += ['### THE RATE PER SYNTHESIS: %s ; all %d rows: %.3f' % ({k: '%d/%d' % tuple(v) for k, v in sy.items()}, sum(s[1] for s in sy.values()), ry),
          '### THE DISAGREEMENTS BY GRADE PAIR (seat -> reader): %s' % ({'%s -> %s' % k: v for k, v in sorted(pairs.items())} or 'none'), '']
    L.append('### PART C -- THE RESIDUE SENTENCES THE READER READ BEYOND, AND EVERY RESIDUE DISAGREEMENT:')
    beyond, dis_x, agx = [], [], 0
    for x in sorted(K['residue'], key=lambda x: (x['source'], x['doc'], x['line'])):
        v, r = A.get(x['id'], ('MISSING', ''))
        agx += v == x['seat']
        if v == 'BEYOND':
            beyond.append(x['id'])
            L.append('  %s BEYOND -- %s :%d (%s; seat %s) -- %s ; the reader`s line: %s' % (x['id'], x['doc'], x['line'], x['source'], x['seat'], x['sentence'][:300], r[:200]))
        if v != x['seat']:
            dis_x.append(dict(id=x['id'], doc=x['doc'], line=x['line'], source=x['source'], seat=x['seat'], reader=v, line_r=r, sentence=x['sentence']))
    rx = agx / max(1, len(K['residue']))
    L += ['### the residue: the reader read %d BEYOND of %d; agreement with the seat`s marks %d of %d = %.3f' % (len(beyond), len(K['residue']), agx,
                                                                                                          len(K['residue']), rx), '']
    bc = [d for d in dis_s if d['reader'] == 'BEYOND-CEILING' and d['seat'] == 'SAME-OBJECT']
    H = dict(H54a='HOLDS' if r_m >= 0.85 and r_s >= 0.80 else 'REFUTED', H54b='HOLDS' if bc else 'REFUTED', H54c='HOLDS' if ry >= 0.75 else 'REFUTED')
    nd = len(dis_s) + len(dis_r) + len(dis_x)
    L += ['### ### **THE DISAGREEMENTS FOR THE AUTHOR`S RULING : %d** (substitutions %d, of them BEYOND-CEILING where the seat read SAME-OBJECT %d; '
          'rows %d; residue %d)' % (nd, len(dis_s), len(bc), len(dis_r), len(dis_x)),
          '### ### **H54a %s** -- the monograph %.3f (bound 0.85), the sieve %.3f (bound 0.80)' % (H['H54a'], r_m, r_s),
          '### ### **H54b %s** -- BEYOND-CEILING disagreements the seat read SAME-OBJECT: %d %s' % (H['H54b'], len(bc), [('%s %s :%s' % (d['edition'], d['bank'], d['new_line'])) for d in bc[:12]]),
          '### ### **H54c %s** -- the sampled rows %.3f (bound 0.75)' % (H['H54c'], ry),
          '### on H54a-H54c, the author`s note: %s.' % READER_NOTE]
    put_txt('b620_agreement.txt', L)
    put_json('b620_agreement.json', dict(at=utc(), n_answers=len(A), missing=missing, bad=bad, editions={k: v for k, v in ed.items()}, r_m=r_m, r_s=r_s,
                                         mono=mono, sieve=siev, syn=sy, r_y=ry, pairs={'%s -> %s' % k: v for k, v in pairs.items()}, beyond=beyond, r_x=rx,
                                         dis_s=dis_s, dis_r=dis_r, dis_x=dis_x, bc=[d['id'] for d in bc], n_dis=nd, **H))
    for l in L[-5:]:
        print(l)


# ================================================================================ COMPONENT 5: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b620_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b620_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b620_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b620 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b620_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b620_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE SCORES AND THE RECORD
HKEYS = ('H54a', 'H54b', 'H54c', 'H54d')
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
CURRENTS = ('README.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'day1/A_Place_to_Stand_v5_14.md', 'day1/A_Place_to_Stand_v5_15.md',
            'day1/A_Place_to_Stand_v5_16.md', 'day1/A_Place_to_Stand_v5_17.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md') + tuple(f for _k, f, _m, _c in SYN)
S4_EXPECT = {'zeta': False, 'chi': False}   # ### this act writes no document a page`s Placement names


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def R2_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no kernel touched; no edition changed; no file written beyond the packet, the key, the
    ### prompt, the agreement bank, the re-emitted pages, the record lines and the trails. ### THE STANDING REPAIR (OPEN_TRAILS :12799):
    ### `trail_line` is the line the trail record's head takes on OPEN_TRAILS, so the write list is the face's, OPEN_TRAILS in it throughout, and
    ### the record is read at that line once written and as pending while the trails stop short of it."""
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
    Z, X = (jl('b620_page_%s.json' % k) if os.path.exists(_p('b620_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    face = jl('b620_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state(list(face)).items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + [p['page'] for p in (Z, X) if p.get('changed')])
    created = sorted(x for x in g(PP, 'diff', '--name-only', '--diff-filter=ADR', PRE_PP, 'HEAD').split(NL) if x.strip())
    cur_ok = all((_show(PP, PRE_PP, p) or '') == (_show(PP, 'HEAD', p) or '') and (_show(PP, PRE_PP, p) or '') == R2.cr0(
        open(os.path.join(PP, *p.split('/')), 'rb').read()).decode('utf-8', 'replace') for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b620_') and not x.startswith('data/' + PACKET + '/')
                              and not os.path.basename(x).startswith('terminal_table') and x != 'data/b619_closing_push_out.txt'))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])   # ### the pending record is OPEN_TRAILS' write when it is the act's only one there
    ok = kern_same and created == [] and cur_ok and pp_ch == want_pp and relay_beyond == [] and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; kernels unmoved since the face %s; created %s; the batch`s editions and the documents read unedited %s; PLACE-papers %s '
            '(wanted %s); %s; relay beyond the act`s banks, packet, tools and the table %s' % (kern_same, created or 'none', cur_ok, pp_ch, want_pp,
                                                                                            rec_state, relay_beyond))


def scores(*a):
    P = jl('b620_packet.json')
    AG = jl('b620_agreement.json') if os.path.exists(_p('b620_agreement.json')) else {}
    Z, X = (jl('b620_page_%s.json' % k) if os.path.exists(_p('b620_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    arms2 = rd('b620_page_arms_c2.txt')
    rc = [l.split(' ', 1) for l in g(RELAY, 'log', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL) if l.strip()]
    pk = [h for h, s in rc if s.startswith('b620 (R230)(2): the reader`s packet') or s.startswith("b620 (R230)(2): the reader's packet")]
    pk_alone = len(pk) == 1 and all(f.startswith('data/' + PACKET + '/') or f == 'data/' + PROMPT for f in _files(pk[0], RELAY))
    ans_t = R2_epoch(AG.get('at', ''))
    hold = rd('b620_author_answers.txt')
    held = 'The reader packet is at data/b620_reader_packet/' in hold and 'RESULT (transcript line' in hold
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    sc = P.get('scan') or {}
    S = {
        'H54a': (AG.get('H54a', 'REFUTED'), 'the monograph %s (bound 0.85), the sieve %s (bound 0.80); %s' % (AG.get('r_m'), AG.get('r_s'), READER_NOTE)),
        'H54b': (AG.get('H54b', 'REFUTED'), '%d BEYOND-CEILING disagreements the seat read SAME-OBJECT: %s; %s' % (
            len(AG.get('bc') or []), (AG.get('bc') or [])[:12], READER_NOTE)),
        'H54c': (AG.get('H54c', 'REFUTED'), 'the sampled rows %s (bound 0.75); by grade pair %s; %s' % (AG.get('r_y'), AG.get('pairs'), READER_NOTE)),
        'H54d': (P.get('H54d', 'REFUTED'), 'the no-disclosure arm on the packet and the prompt: %s' % P.get('nd')),
        'N1': (('HELD' if not sc.get('act') and not sc.get('grade') and not sc.get('mark') else 'REFUTED'), 'the packet`s scan: act pattern %d, grade words '
               'in the items %d, marks %d (masks applied %d)' % (len(sc.get('act') or []), len(sc.get('grade') or []), len(sc.get('mark') or []), P.get('masks', 0))),
        'N2': (('HELD' if AG.get('r_m', 0) >= 0.85 else 'REFUTED'), 'the monograph`s agreement %s' % AG.get('r_m')),
        'N3': (('HELD' if [d for d in AG.get('dis_s') or [] if d['reader'] == 'BEYOND-CEILING'] else 'REFUTED'), 'BEYOND-CEILING disagreements %d' % (
            len([d for d in AG.get('dis_s') or [] if d['reader'] == 'BEYOND-CEILING']))),
        'N4': (('HELD' if AG.get('r_y', 0) >= 0.75 else 'REFUTED'), 'the sampled-row agreement %s' % AG.get('r_y')),
        'N5': n5v,
        'S1': (('HELD' if pk_alone else 'REFUTED'), 'the packet and the prompt committed alone in relay: %s %s' % (pk_alone, pk)),
        'S2': (('HELD' if held else 'REFUTED'), 'the hold`s one prompt put verbatim and answered (data/b620_author_answers.txt): %s' % held),
        'S3': (('HELD' if not AG.get('missing') and not AG.get('bad') and AG.get('n_answers') else 'REFUTED'), 'the reader`s bank complete: %s answers, missing %s, '
               'outside the vocabulary %s' % (AG.get('n_answers'), len(AG.get('missing') or []), len(AG.get('bad') or []))),
        'S4': (('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] and Z.get('rc') == 0 and X.get('rc') == 0 else 'REFUTED'),
               'the ζ page changed %s, the χ page changed %s' % (Z.get('changed'), X.get('changed'))),
        'S5': (('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED'),
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b620_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


def _title_entry():
    AG = jl('b620_agreement.json')
    return ('## The second reader over the monograph’s three editions, the sieve’s four and the six syntheses: agreement %.3f on the monograph, '
            '%.3f on the sieve, %.3f on 120 sampled rows; %d disagreements listed for the author’s ruling' % (AG['r_m'], AG['r_s'], AG['r_y'], AG['n_dis']))


TRAIL_HEAD = ('### b620 — lane three, act forty-seven under (R230): the second reader -- the packet built without reasons, grades or act numbers, '
              'the reader run in a fresh session the author opened, the agreement rates banked and the disagreements listed')


def _dis_lines(AG, cap=None):
    out = []
    for d in AG['dis_s']:
        out.append('%s %s :%s (%s :%s) seat %s, reader %s' % (d['doc'].replace('the ', ''), d['edition'], d['new_line'], d['bank'].replace('.txt', ''),
                                                            d['bank_line'], d['seat'], d['reader']))
    for d in AG['dis_r']:
        out.append('row %s (%s %s) seat %s, reader %s' % (d['id'], d['key'], d['claim_id'], d['seat'], d['reader']))
    for d in AG['dis_x']:
        out.append('residue %s :%s seat %s, reader %s' % (os.path.basename(d['doc']), d['line'], d['seat'], d['reader']))
    return out[:cap] if cap else out


def _finding_text():
    S, rl, AG, P = jl('b620_scores.json'), jl('b620_record_lines.json'), jl('b620_agreement.json'), jl('b620_packet.json')
    t = _title_entry()
    pk = next((l.split(' ', 1)[0] for l in g(RELAY, 'log', '--format=%h %s', PRE_RELAY + '..HEAD').split(NL) if 'the reader' in l and 'packet' in l), '?')
    e = ['', t, '',
         '*Filed at b620 on the author’s ruling `(R230)`. Banks: relay `data/b620_reader_packet/`, `data/b620_reader_prompt.txt`, `data/b620_key.txt`, '
         '`data/b620_reader_answers.txt`, `data/b620_agreement.txt`, `data/b620_packet.json`. Nothing deposits.*', '',
         '**The packet** (`(R230)`(2), part one), committed alone in relay (%s): %d substitutions from the seven diff banks as pairs of wordings '
         '(the monograph’s v5.14-v5.16, %d; the sieve’s v0.2-v0.5, %d), shuffled by a seeded key banked apart; %d rows, twenty drawn by seed '
         'from each synthesis’s Correspondence, each claim with its paper’s cited lines copied verbatim and the seat’s grade withheld; %d residue '
         'sentences from the seed and the two addenda, unmarked; the ceiling sentence once; no reason, grade or act number (masks %d), the '
         'no-disclosure arm at 0. **The reader**, part two’s input: a fresh session the author opened, which wrote its bank and closed.' % (
             pk, P['subs'], AG['mono'][1], AG['sieve'][1], P['rows'], P['residue'], P['masks']), '',
         '**The keying.** Agreement %d of %d on the monograph (%.3f), %d of %d on the sieve (%.3f), %.3f on the sampled rows, %.3f on the residue '
         'marks; %d disagreements -- %d substitutions, %d of them BEYOND-CEILING where the seat read SAME-OBJECT, %d rows, %d residue sentences -- '
         'listed on the trail record for the author’s ruling; no edition changed.' % (
             AG['mono'][0], AG['mono'][1], AG['r_m'], AG['sieve'][0], AG['sieve'][1], AG['r_s'], AG['r_y'], AG['r_x'], AG['n_dis'], len(AG['dis_s']),
             len(AG['bc']), len(AG['dis_r']), len(AG['dis_x'])), '',
         '**The record line.** b619’s weight at FINDINGS :%d, the five confirmations.' % rl['lines'][0]['line'], '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the work-order b593 entered (OPEN_TRAILS :12212) and the batch and seed b609 named '
         '(:12542, FINDINGS :7182) are run here; the editions the reader read are b606-b608’s (:7104, :7128, :7158) and b604-b617’s (:7060, :7084, '
         ':7186, :7368); the six syntheses’ grades are b611-b616’s (:7240 to :7346) under the grading rule of `(R222)`(1); the residue is the '
         'seat’s list b609, b610 and b614 banked. It strengthens the programme’s offering of editions whose every substitution a reader '
         'with no context of the acts has scored against the ceiling, the agreement banked and every disagreement put to the author.', '',
         '**Next.** Per `(R230)`(3): b621, the author’s rulings on the disagreements applied as editions where ruled, then '
         'W-ORD-QUANTIFIER-COLUMN’s generator. The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; no edition changed; nothing here is a statement about RH, GRH or any zero beyond the compiled '
         'statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b620_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = ('(1) every substitution read SAME-OBJECT by the seat, the form’s clauses each asserting the replacement names its sentence’s object '
              'within the ceiling; (2) the sieve’s v0.2 substitutions are its five superseded conclusions, v0.3’s its changed rows and other '
              'rewrites, v0.4’s and v0.5’s their fragments; (3) the residue’s seat reading BEYOND for KIN and AT for every other mark; (4) “the '
              'enumeration needle (OT :12673)” read as b610’s needle, whose lines are its addendum, :12673 being b614’s silence-principle '
              'reading, the navigator’s citation; (5) act numbers inside the editions’ own wordings masked, each in the key; rows whose claim or '
              'cited lines carry a grade word, an act number or a mark not drawn')


def _trail_text():
    S, fj, rl, AG = jl('b620_scores.json'), jl('b620_findings.json'), jl('b620_record_lines.json'), jl('b620_agreement.json')
    dl = _dis_lines(AG)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R230) ratified.** (1) b619 at its weight; the five readings confirmed. (2) W-ORD-SECOND-READER in two parts, the reader in a fresh '
             'session; H54a-H54d. (3) The act after: b621.', '',
             '**Entered:** FINDINGS.md:%d (b619’s weight), :%d (the entry, with its mutual-light line); this record; relay data/b620_reader_packet/, '
             'data/b620_reader_prompt.txt, data/b620_key.txt, data/b620_reader_answers.txt, data/b620_agreement.txt.' % (rl['lines'][0]['line'],
                                                                                                                        fj['entry_line']), '',
             '**The hold, answered by the author** (relay data/b620_author_answers.txt): the reader’s bank written by a fresh session.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**The disagreements, for the author’s ruling, by edition and line** (%d; both wordings, the seat’s reading and the reader’s line in relay '
             'data/b620_agreement.txt): %s.' % (len(dl), '; '.join(dl) if dl else 'none'), '',
             '**Defects** (relay data/b620_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R230)`(3), b621, the author’s rulings on the disagreements applied as editions where ruled, then W-ORD-QUANTIFIER-COLUMN’s '
             'generator; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:6000])
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b620_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b620_trail.json')['line'])


def desk(*a):
    S = jl('b620_scores.json')
    L = ['=' * 104, 'b620 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H54a-H54d, (R230)(2).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H54 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b620_defects.txt').rstrip(NL).split(NL)
    put_txt('b620_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, AG, P = (jl(n) for n in ('b620_scores.json', 'b620_findings.json', 'b620_trail.json', 'b620_record_lines.json', 'b620_agreement.json',
                                            'b620_packet.json'))
    Z, X = jl('b620_page_zeta.json'), jl('b620_page_chi.json')
    L = ['b620 -- THE COMPONENTS, BANKED UNDER (R230).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b619`s closing push-out relay %s ; push-b619* branches deleted by name '
         '(data/b620_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b620_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b619`s weight FINDINGS :%d' % rl['lines'][0]['line'],
         '### COMPONENT 2 : the packet data/b620_reader_packet/ ; %d substitutions, %d rows, %d residue sentences ; H54d %s' % (P['subs'], P['rows'], P['residue'], S['H54d'][0]),
         '### COMPONENT 3 : the hold, the one prompt answered (data/b620_author_answers.txt) ; S2 %s' % S['S2'][0],
         '### COMPONENT 4 : the keying data/b620_agreement.txt ; the monograph %.3f, the sieve %.3f, the rows %.3f ; %d disagreements ; H54a %s, H54b %s, H54c %s' % (
             AG['r_m'], AG['r_s'], AG['r_y'], AG['n_dis'], S['H54a'][0], S['H54b'][0], S['H54c'][0]),
         '### COMPONENT 5 : the ζ page changed %s, the χ page changed %s ; page arms data/b620_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b621 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b620_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b620_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
