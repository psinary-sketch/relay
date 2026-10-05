# -*- coding: utf-8 -*-
"""b621_record.py -- THE ACT'S RECORD TOOL, UNDER (R231). ### ONE SUBCOMMAND PER BANK.

### ### b621: LANE THREE, ACT FORTY-EIGHT -- THE SECOND READER'S DISAGREEMENTS RULED BY CLASS AND APPLIED: THE MONOGRAPH AT v5.18, THE
### SYNTHESES RE-GRADED WHERE THE READER WAS RIGHT, THE FORM AMENDED TO SHOW THE READER WHAT THE SEAT GRADED.
### Subcommands write only `data/b621_*` unless the docstring names another file; `dry` on the command line routes every b621 bank and every
### edition to the seat's scratchpad (for `findings` and `trail`, `dry` prints and appends nothing; `record_lines dry` banks the sieve's rate
### in the scratchpad and prints the ledger lines without appending them). Banks are written by encode, temp file, `os.replace`; ledger
### appends through b566's guarded `append_to`. The work-list is tools/b621_worklist.py (data only). No platform call. No Lean call: both
### pages are re-emitted from their banked probes. The templates are tools/b620_record.py (the harness), tools/b609_record.py (the
### monograph's edition, its classification of the carried ceiling hits imported) and tools/b615_record.py (a synthesis's next version).
### The N5 scorer takes the trail record's expected line (OPEN_TRAILS :12799, the standing line of (R229)(2)).
"""
import difflib
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
import b604_record as R4  # noqa: E402
import b621_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = 'e6a3fbf'
PRE_RELAY = '7838dd02'
STEPZERO = 'dd5a86c8'
DATE = '2026-10-04'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5e646bda-5dd5-4aca-9274-32c06d1d3da9/scratchpad'
SESSION_ID = '5e646bda-5dd5-4aca-9274-32c06d1d3da9'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SESSION_FROM = 0     # ### this session opened on this act's ferry
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
M17, M18 = K.M17, K.M18
SV5 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md'
CORR_HEAD = '## Correspondence *(added 2026-08-12'
B606_TAG = '<!-- b606 (R216) THE v5.14 EDITION`S BACK MATTER, 2026-10-03 -->'
B607_TAG = '<!-- b607 (R217) THE v5.15 EDITION`S BACK MATTER, 2026-10-03 -->'
B608_TAG = '<!-- b608 (R218) THE v5.16 EDITION`S BACK MATTER, 2026-10-03 -->'
B609_TAG = '<!-- b609 (R219) THE v5.17 EDITION`S BACK MATTER, 2026-10-03 -->'
BM_TAG18 = '<!-- b621 (R231) THE v5.18 EDITION`S BACK MATTER, 2026-10-04 -->'
B609_MONO_AT = '34b996c9'      # ### the relay commit holding b609's banked edition of v5.17 (data/b609_mono_edition.json)
EDITED = ('15E', '2D', '2G', 'P12')     # ### the syntheses whose rows the rulings move or correct; 2B and 2F keep every row

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b621_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b621_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    return K.lines_of(t)


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


def _poss(s):
    """### a backtick possessive (word`s) becomes ’s for a PLACE-papers file; a code span keeps its backticks."""
    return re.sub(r'(?<=\w)`(?=s\b)', '’', s)


def _rel(n, rev=PRE_RELAY):
    return _show(RELAY, rev, 'data/' + n) or ''


def _scan(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout or ''


def _hits(s):
    return [m.group(0) for m in CEILING.finditer(s)]


DEFECTS = [
    '(a) THE SEAT`S, AT THE PRE-PUSH SUITE, AFTER THE RECORD: the suite`s G-SYN-TIERS asks that 2B`s and 2F`s next versions be absent by '
    'testing their sources for None, while the source builder reads every file through cr0, which returns empty bytes for an absent one; '
    'so that arm, and G-H55B-SCORED, which recomputes H55b through it, fail in their letter -- the suite 76 of 78 pre-push, NOT CLEAN in '
    'letter, the arm`s positive control unable to show the species (it fails either way). The claim tested directly: neither next version exists '
    'on disk, at HEAD or in the index, and each edited synthesis`s tier line equals its current one (relay data/b621_tiers_direct.txt); H55b '
    'and N2 stand as scored. The sealed suite is not edited. The trail record, written before the suite, read "none recorded"; the record '
    'tool, committed as sealed (ff6550ee), took one edit through the Edit tool after the seal -- this defect`s text, the direct test and a '
    'correction line -- committed alone, the face`s (Z) refuted in its letter; the correction appended to OPEN_TRAILS addressed to the record.',
]
DEFECT_SHORT = ['(a) the seat’s: the suite’s G-SYN-TIERS tests 2B’s and 2F’s next versions for absence by None where its sources hold an absent '
                'file as empty bytes, so it and G-H55B-SCORED fail in letter, the suite 76 of 78 pre-push; tested directly, neither next version '
                'exists and every edited tier line equals its current one (relay data/b621_tiers_direct.txt); the sealed suite not edited; the '
                'record tool took one edit after the seal to carry the defect, committed alone']


def defects(*a):
    L = ['b621 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b621_defects.txt', L)


# ================================================================================ READING (1): THE READS
def _kv_term_reads():
    out = []
    for rid, k in K.KV.items():
        for repo, rev, path, a, b in k['terms']:
            out.append(('the terminal %s`s row names, read at its pin by statement' % rid, repo, rev, path, list(range(a, b + 1)), 400))
    return out


def _syn_row_reads():
    AG = json.loads(_rel('b620_agreement.json'))
    KEY = json.loads(_rel('b620_key.json'))
    rows = {r['id']: r for r in KEY['rows']}
    out = []
    for key, path in K.SYN.items():
        ids = [rows[d['id']]['claim_id'] for d in AG['dis_r'] if d['key'] == key]
        out.append(('the %s synthesis`s Correspondence at the disagreement rows (%d)' % (key, len(ids)), PP, PRE_PP, path,
                    ('GREP', r'^\| (%s) \|' % '|'.join(re.escape(i) for i in ids)), 900))
    return out


def _mono_read_lines():
    M, _bad = K.resolve_changes()
    return sorted(set([c[1] for c in K.CHANGES if c[0].startswith('C')] + [2234]))


def READS():
    return [
        ('relay data/b620_agreement.txt, whole', RELAY, PRE_RELAY, 'data/b620_agreement.txt', ('ALL',), 420),
        ('OPEN_TRAILS: the form, the second reader, the precedence order, the synthesis clauses, the N5 standing line, b619`s and b620`s '
         'records', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12212, 12228, 12601] + list(range(12799, 12838)), 1600),
        ('the monograph v5.17 at the enumeration sentence and at every monograph line in the residue list', PP, PRE_PP, M17, _mono_read_lines(), 700),
    ] + _syn_row_reads() + _kv_term_reads() + [
        ('the sieve v0.5: RH-60`s row', PP, PRE_PP, SV5, [124], 1200),
        ('FINDINGS: the b609 reading (b610`s, addressed to b609`s entry), b620`s weight line`s address and entry', PP, PRE_PP, 'FINDINGS.md',
         [7210, 7420, 7422], 900),
        ('README: the ceiling sentence', PP, PRE_PP, 'README.md', list(range(106, 112)), 600),
        ('relay data/b620_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b620_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b621 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
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
        L.append('### %s -- %s%s @ %s (%d lines cited, of %d)' % (label, '' if repo in (PP, RELAY) else repo + ' ', path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b621_reads.txt', L)


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
    L = ['### b621 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b621_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7', 'SIDE-effects': 'ef4cff7', 'SIDE-cosmo': 'c5cba30'}


def kern_state(ks=None):
    out = {}
    for k in (ks or KERNS):
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    put_json('b621_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B620_ENTRY = '## The second reader over the monograph’s three editions, the sieve’s four and the six syntheses'
SR_LINE = '*Appended 2026-10-02 by b593 beside b592’s record (:12196), under the author’s ruling `(R203)`(3) -- W-ORD-SECOND-READER'
W_HEAD = '*Appended 2026-10-04 by b621 to b620’s entry (:%d), under `(R231)`(1)-(2) -- b620 AT ITS WEIGHT, AND THE READING OF THE RESULT:*'
C_HEAD = ('*Appended 2026-10-04 by b621 to W-ORD-SECOND-READER’s form (:%d), under `(R231)`(4) -- THE ROW SAMPLE CARRIES THE TERMINAL’S '
          'STATEMENT:*')
STRUCK = ['S356', 'S099', 'S205', 'S129', 'S011']


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def sieve_rate():
    AG = json.loads(_rel('b620_agreement.json'))
    ed = AG['editions']
    struck = [d for d in AG['dis_s'] if d['id'] in STRUCK]
    sv = [k for k in ed if k.startswith('the sieve')]
    a0, n0 = sum(ed[k][0] for k in sv), sum(ed[k][1] for k in sv)
    a1, n1 = sum(ed[k][0] for k in sv if k != 'the sieve v0.2'), sum(ed[k][1] for k in sv if k != 'the sieve v0.2')
    return dict(struck=[dict(id=d['id'], bank=d['bank'], bank_line=d['bank_line'], seat=d['seat'], reader=d['reader']) for d in struck],
                orig=[a0, n0, a0 / n0], recomputed=[a1, n1, a1 / n1], mono=AG['mono'], r_m=AG['r_m'], n_dis=AG['n_dis'],
                n_dis_after=AG['n_dis'] - len(struck), by_edition=ed)


def _weight(entry):
    S = {k: v[0] for k, v in json.loads(_rel('b620_scores.json')).items()}
    AG, P = json.loads(_rel('b620_agreement.json')), json.loads(_rel('b620_packet.json'))
    RL, FJ, TJ = json.loads(_rel('b620_record_lines.json')), json.loads(_rel('b620_findings.json')), json.loads(_rel('b620_trail.json'))
    pre, post = (_count_bank(_rel(n)) for n in ('b620_checks.txt', 'b620_checks_postpush.txt'))
    R = sieve_rate()
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    return ('\n%s The packet (relay ce75ce85): %d substitutions (%d of the monograph, %d of the sieve), %d sampled rows, %d residue sentences, '
            'the ceiling sentence once (README :106-:111; the ferry’s “:121” the navigator’s), %d act numbers inside the editions’ own wordings '
            'masked, the no-disclosure arm 0. The seat’s headless launch refused by the permission classifier; the reader run by the author '
            'from D:\\reader_b620 with the seat’s command -- its tools Read, Glob and Write, Grep and Edit used on its own answer file alone -- '
            'and its transcript reading the packet’s five files and nothing else (relay data/b620_reader_run.txt); %d answers, one per item. '
            'Agreement: the monograph %d of %d (%.3f), the sieve %d of %d (%.3f), H54a %s; one BEYOND-CEILING where the seat read '
            'SAME-OBJECT, v5.16 :1217, “The reduction examines seven mechanism classes and finds that none produces off-line zeros”, the '
            'reader’s line that it states unconditionally what is open at h2, H54b %s; the five sieve v0.2 pairs read DIFFERENT-OBJECT, the '
            'pairs being the seat’s pairing of a superseded prose conclusion with its replacing row, struck from the batch under `(R231)`(3)(ii) '
            'as not substitutions -- the sieve’s rate without them %d of %d (%.3f) beside the original %d of %d (%.3f), no sieve edition '
            '(relay data/b621_sieve_rate.txt); the sampled rows %.3f, H54c %s and N4 %s, the disagreements mostly downward, six kernel-verified '
            'rows read statement-grade, the reader having the papers’ cited lines and not the backing read at the pin -- the packet’s design, '
            'the navigator’s; the residue marks %.3f, %d of %d read BEYOND by the reader; %d disagreements (%d substitutions, %d rows, %d '
            'residue sentences) at OPEN_TRAILS :%d and relay data/b620_agreement.txt. H54d %s; N1-N3 and N5 %s; S1-S5 %s. Relay 7838dd02; '
            'PLACE-papers e6a3fbf. The suite %d of %d before the push and %d of %d after it; no edition changed. Defects (a)-(c), the seat’s. '
            '**The reading, `(R231)`(2):** the second reader is the one check on the form’s substitutions that is not the seat that made them, '
            'and it says: on the editions proper the seat’s substitutions are the reader’s at %.3f and %.3f (%.3f without the struck pairs), '
            'so the form’s judgment is '
            'reproducible by a reader with no reasons; the one sentence it caught is the enumeration sentence -- the object the sieve reads '
            'DARK at RH-60 and the needle of :7210 was written for -- found independently from the wording alone; and the synthesis-row grades '
            'are the place the form rests on something a context-free reader was not given. Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, P['subs'], AG['mono'][1], AG['sieve'][1], P['rows'], P['residue'], P['masks'], AG['n_answers'],
                AG['mono'][0], AG['mono'][1], AG['r_m'], AG['sieve'][0], AG['sieve'][1], AG['r_s'], S['H54a'], S['H54b'],
                R['recomputed'][0], R['recomputed'][1], R['recomputed'][2], R['orig'][0], R['orig'][1], R['orig'][2], AG['r_y'], S['H54c'], S['N4'],
                AG['r_x'], len(AG['beyond']), P['residue'], AG['n_dis'], len(AG['dis_s']), len(AG['dis_r']), len(AG['dis_x']), TJ['line'], S['H54d'],
                allh(('N1', 'N2', 'N3', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), pre[0], pre[1], post[0], post[1],
                AG['r_m'], AG['r_s'], R['recomputed'][2]))


def _clause(sr):
    return ('\n%s the synthesis-row sample carries, beside the paper’s cited lines, the statement of any terminal the row names, printed '
            'from the kernel at the pin without its grade, so the reader grades what the seat graded; the agreement bound for rows stands at '
            '0.75 for the next batch. The packet-design fault at b620 is the navigator’s (`(R231)`(4)).\n' % (C_HEAD % sr))


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
    p = os.path.join(SP if DRY else D, 'b621_scanfile_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    out = _scan(p)
    return out, re.search(r'^\s*VERDICT\s*: CLEAN\s*$', out, re.M) is not None


def record_lines(*a):
    """### data/b621_sieve_rate.txt (the five pairs struck, the rate recomputed beside the original), then FINDINGS: b620's weight with the
    ### reading of (R231)(2), addressed to b620's entry; OPEN_TRAILS: the form's clause, addressed to W-ORD-SECOND-READER (:12212)."""
    Q = R2._Q()
    entry, sr = Q.line_of(Q.FIND, B620_ENTRY), Q.line_of(Q.OT, SR_LINE)
    if entry != 7422 or sr != 12212:
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s) -- NOTHING WRITTEN' % (entry, sr))
    R = sieve_rate()
    L = ['b621 -- COMPONENT 1: THE SIEVE`S RATE RECOMPUTED, (R231)(3)(ii), banked %s' % utc(), '',
         '### THE FIVE PAIRS STRUCK FROM THE BATCH AS NOT SUBSTITUTIONS (the sieve v0.2; each the seat`s pairing of a superseded prose '
         'conclusion with its replacing row, read DIFFERENT-OBJECT by the reader):']
    L += ['  %s -- %s :%d -- seat %s ; reader %s' % (x['id'], x['bank'], x['bank_line'], x['seat'], x['reader']) for x in R['struck']]
    L += ['', '### THE SIEVE`S RATE PER EDITION (relay data/b620_agreement.json at 7838dd02):']
    L += ['  %-22s %d of %d' % (k, v[0], v[1]) for k, v in R['by_edition'].items() if k.startswith('the sieve')]
    L += ['', '### ### **THE SIEVE, ALL FOUR, AS KEYED: %d of %d = %.3f ; WITHOUT THE FIVE STRUCK PAIRS: %d of %d = %.3f.**' % (
        R['orig'][0], R['orig'][1], R['orig'][2], R['recomputed'][0], R['recomputed'][1], R['recomputed'][2]),
          '### the monograph unchanged: %d of %d = %.3f ; the disagreements for the ruling %d, of them struck as not substitutions %d, the rest %d '
          'ruled by class at (R231)(3)(i), (iii) and (iv); no sieve edition.' % (R['mono'][0], R['mono'][1], R['r_m'], R['n_dis'], len(R['struck']),
                                                                             R['n_dis_after'])]
    put_txt('b621_sieve_rate.txt', L)
    put_json('b621_sieve_rate.json', dict(at=utc(), **R))
    wt, cl = _weight(entry), _clause(sr)
    bad = ledger_check(wt, cl)
    nd, _n = _nd(wt + cl)
    sc, clean = _scan_text(wt + cl, 'lines')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if DRY:
        print(wt)
        print(cl)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    Q.guard_absent(Q.OT, C_HEAD % sr)
    r1 = Q.append_to(Q.FIND, wt)
    r2 = Q.append_to(Q.OT, cl)
    out = [dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r1),
           dict(file='OPEN_TRAILS.md', head=C_HEAD % sr, line=Q.line_of(Q.OT, C_HEAD % sr), append=r2)]
    put_json('b621_record_lines.json', dict(entry=entry, sr=sr, lines=out))
    print('  FINDINGS.md :%s ; OPEN_TRAILS.md :%s' % (out[0]['line'], out[1]['line']))


# ================================================================================ COMPONENT 2: THE ROWS
def _ranges(spec):
    """### 'TF :363-:369, :391' -> [(363, 369), (391, 391)]"""
    out = []
    for m in re.finditer(r':(\d+)(?:-:(\d+))?', spec or ''):
        out.append((int(m.group(1)), int(m.group(2) or m.group(1))))
    return out


def _syn_rows():
    texts = {k: lines_of(_show(PP, PRE_PP, p)) for k, p in K.SYN.items()}
    return texts


def rows(*a):
    """### data/b621_rows.txt (Parts A and B) and its json: the six kernel-verified rows each as (claim, the paper's lines, the terminal's
    ### statement at its pin) with the verdict and its reason; the 46 others each with the seat's grade, the reader's, the omitted line if
    ### any and the verdict; the cells the next versions change; H55a. Banked before any edition is written."""
    AG = json.loads(_rel('b620_agreement.json'))
    KEY = json.loads(_rel('b620_key.json'))
    krow = {r['id']: r for r in KEY['rows']}
    texts = _syn_rows()
    bad = K.resolve_rows(texts)
    if bad:
        sys.exit('### THE WORK-LIST`S CELLS DO NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    dis = {d['id']: d for d in AG['dis_r']}
    if set(dis) != set(K.OTHERS) | set(K.KV):
        sys.exit('### THE VERDICTS DO NOT COVER THE 52 ROWS -- NOTHING WRITTEN')

    def syn_row(rid):
        r = krow[rid]
        hit = [(i + 1, l) for i, l in enumerate(texts[r['key']]) if l.startswith('| %s |' % r['claim_id'])]
        return hit[0] if hit else (None, '')

    L = ['b621 -- COMPONENT 2: THE ROWS, (R231)(3)(iii), RE-READ AND BANKED BEFORE ANY EDITION IS WRITTEN (%s)' % utc(), '',
         '### THE RULE, (R231)(3)(iii): for the six kernel-verified rows graded down, the terminal`s statement at its pin printed beside the '
         'paper`s cited lines -- where the statement carries the claim the grade stands with the terminal named in the row, where it does not '
         'the grade moves to what the lines support; for the 46 others the lower grade governs unless the seat names a cited line the packet '
         'omitted, each printed with its reason; ties fall to the lower grade.',
         '### THE ORDER OF THE GRADES (reading R-7): the grading rule`s own order as each synthesis prints it -- %s, highest first.' % ', '.join(K.GRADES),
         '### the synthesis files read at PLACE-papers %s; the papers and the terminals at their pins.' % PRE_PP, '',
         '### PART A -- THE SIX KERNEL-VERIFIED ROWS:']
    kv_out = []
    for rid, k in K.KV.items():
        r, d = krow[rid], dis[rid]
        n, line = syn_row(rid)
        c = K.row_cells(line)
        L += ['', '  %s  %s %s  (%s at its line :%s)  seat %s ; reader %s -- the reader`s line: %s' % (
            rid, r['key'], r['claim_id'], K.SYN[r['key']], n, d['seat'], d['reader'], d['line']),
              '    the claim: %s' % c[2], '    the row`s backing cell: %s' % c[4]]
        ppath, pin, rng = k['paper']
        pt = lines_of(_show(PP, pin, ppath))
        L.append('    the paper`s lines, %s @ %s:' % (ppath, pin))
        for a_, b_, lab in rng:
            for x in range(a_, b_ + 1):
                L.append('      :%-5d [%s] %s' % (x, lab, pt[x - 1][:600] if 0 < x <= len(pt) else '### NO SUCH LINE'))
        L.append('    the terminal`s statement at its pin:')
        for repo, rev, path, a_, b_ in k['terms']:
            tt = lines_of(_show(repo, rev, path))
            L.append('      %s @ %s (%s) %s :%d-:%d' % (os.path.basename(repo), rev, g(repo, 'rev-parse', '--short=12', rev).strip(), path, a_, b_))
            for x in range(a_, b_ + 1):
                L.append('        :%-4d %s' % (x, tt[x - 1] if tt and 0 < x <= len(tt) else '### NO SUCH LINE'))
        L.append('    ### VERDICT: %s at kernel-verified -- %s' % (k['verdict'].upper(), k['reason']))
        kv_out.append(dict(id=rid, key=r['key'], claim=r['claim_id'], verdict=k['verdict'], line=n))
    L += ['', '### PART B -- THE 46 OTHERS (the reader`s grade, the seat`s, the omitted line the seat names if any, the verdict):']
    oth = []
    for d in AG['dis_r']:
        if d['id'] in K.KV:
            continue
        r = krow[d['id']]
        v, om, why = K.OTHERS[d['id']]
        n, line = syn_row(d['id'])
        direction = 'down' if K.GRADES.index(d['reader']) > K.GRADES.index(d['seat']) else 'up'
        new = d['reader'] if v == 'moves' else d['seat']
        L += ['', '  %s  %s %s  %s @ %s  (the synthesis`s line :%s)  seat %s ; reader %s (%s) -- the reader`s line: %s' % (
            d['id'], r['key'], r['claim_id'], r['paper'], r['pin'], n, d['seat'], d['reader'], direction, d['line']),
              '    the omitted line the seat names: %s' % (om or 'none')]
        if om:
            pt = lines_of(_show(PP, r['pin'], r['paper']))
            for a_, b_ in _ranges(om):
                for x in range(a_, b_ + 1):
                    if 0 < x <= len(pt) and pt[x - 1].strip():
                        L.append('      :%-5d %s' % (x, pt[x - 1][:500]))
        L.append('    ### VERDICT: %s -- the grade %s -- %s' % (v.upper(), new, why))
        oth.append(dict(id=d['id'], key=r['key'], claim=r['claim_id'], seat=d['seat'], reader=d['reader'], direction=direction, verdict=v,
                        omitted=om, grade=new, line=n))
    L += ['', '### PART B2 -- THE CELLS THE NEXT VERSIONS CHANGE (grade and backing, old and new), AND THE FACT THE ROWS` RE-READ FOUND:']
    for rid, key, cid, og, ng, ob, nb in K.REGRADES:
        L += ['  %s  %s %s -> %s' % (rid, key, cid, K.NEXT[key][0]), '      was : %s | %s' % (og, ob), '      now : %s | %s' % (ng, nb)]
    for fid, key, cid, old, new, why in K.FACTS:
        L += ['  %s  %s %s (the fact clause) -- %s' % (fid, key, cid, why), '      was : %s' % old, '      now : %s' % new]
    kvs = sum(1 for x in kv_out if x['verdict'] == 'stands')
    cnt = {v: sum(1 for x in oth if x['verdict'] == v) for v in ('stands', 'moves', 'unchanged')}
    bysyn = {k: sum(1 for r in K.REGRADES if r[1] == k) for k in K.SYN}
    h55a = 'HOLDS' if kvs >= 4 else 'REFUTED'
    L += ['', '### THE COUNTS: the kernel-verified rows standing on their terminals` statements %d of %d ; the 46 others: stand %d (on a line '
          'the packet omitted), move %d (to the reader`s lower grade), unchanged %d (the seat`s grade the lower) ; the rows re-graded %d, by '
          'synthesis %s ; the syntheses touched %s ; the rows the act`s re-read corrects by the fact clause %d' % (
              kvs, len(kv_out), cnt['stands'], cnt['moves'], cnt['unchanged'], len(K.REGRADES), bysyn,
              sorted(set(r[1] for r in K.REGRADES) | set(f[1] for f in K.FACTS)), len(K.FACTS)),
          '### ### **H55a %s -- of the six kernel-verified rows, %d stand with the terminal`s statement carrying the claim (bound four).**' % (h55a, kvs)]
    b = put_txt('b621_rows.txt', L)
    put_json('b621_rows.json', dict(at=utc(), kv=kv_out, others=oth, kv_stand=kvs, counts=cnt, regraded=len(K.REGRADES), by_syn=bysyn,
                                    touched=sorted(set(r[1] for r in K.REGRADES) | set(f[1] for f in K.FACTS)), H55a=h55a, sha256=R2.sha(b)))
    print(L[-2][:400])
    print(L[-1])


# ================================================================================ COMPONENT 3: THE RESIDUE
def residue(*a):
    """### data/b621_rows.txt Part C, appended to the rows bank (Parts A and B unchanged, by sha256): the 56 residue disagreements by
    ### document and line with the verdict; the author's answer applied; the monograph's subset counted; the other documents' sentences
    ### listed for their next editions; the restatement survey; data/b621_residue.json."""
    RJ = jl('b621_rows.json')
    cur = open(_p('b621_rows.txt'), 'rb').read()
    if R2.sha(cur) != RJ['sha256']:
        sys.exit('### THE ROWS BANK IS NOT THE ONE BANKED -- NOTHING WRITTEN')
    AG = json.loads(_rel('b620_agreement.json'))
    KEY = json.loads(_rel('b620_key.json'))
    res = {x['id']: x for x in KEY['residue']}
    item_changes = {}
    for c in K.CHANGES:
        for x in c[5]:
            if x.startswith('X'):
                item_changes.setdefault(x, []).append(c[0])
    for x in K.HISTORY_ITEMS:
        item_changes.setdefault(x, []).append('H1')
    mono = lambda r: 'A_Place_to_Stand' in r['doc']   # noqa: E731
    L = ['', '### PART C -- THE RESIDUE, (R231)(3)(iv) AND THE AUTHOR`S ANSWER BEFORE THE SEAL (relay data/b621_author_answers.txt) '
         '-- banked %s' % utc(),
         '### THE RULING`S LETTER: a sentence the reader read BEYOND and the seat AT takes the ceiling clause at its document`s next edition; '
         'a sentence the seat read BEYOND and the reader AT keeps the seat`s reading and stays on the second reader`s list.',
         '### THE AUTHOR`S ANSWER (option 3): every sentence EITHER reader read BEYOND takes the ceiling at its document`s next edition -- the '
         'monograph`s at v5.18 (the 13 both read BEYOND, the one the reader read BEYOND, by a history line beneath since the dated block '
         'governs, and the 19 the seat read BEYOND), the other documents` listed for their next editions; the seat`s BEYOND kept means kept '
         'BEYOND; H55c and N3 scored on the 33.', '',
         '### THE 56 RESIDUE DISAGREEMENTS, BY DOCUMENT AND LINE, WITH THE VERDICT:']
    rows_ = []
    for d in AG['dis_x']:
        r = res[d['id']]
        if mono(r):
            v = 'the ceiling at v5.18 (%s)' % ', '.join(item_changes.get(d['id'], ['### NONE']))
        else:
            v = 'the ceiling at its document`s next edition, listed'
        L.append('  %s  %s :%s (%s; mark %s) seat %s ; reader %s -- %s' % (d['id'], r['doc'], r['line'], r['source'], r['mark'], d['seat'],
                                                                          d['reader'], v))
        rows_.append(dict(id=d['id'], doc=r['doc'], line=r['line'], seat=d['seat'], reader=d['reader'], mono=mono(r), changes=item_changes.get(d['id'], [])))
    agreed = [i for i in AG['beyond'] if res[i]['seat'] == 'BEYOND']
    L += ['', '### THE SENTENCES BOTH READERS READ BEYOND (agreements of the batch, no clause of (R231) naming them; the author`s answer):']
    for i in agreed:
        r = res[i]
        L.append('  %s  %s :%s (%s) -- %s' % (i, r['doc'], r['line'], r['source'], ('the ceiling at v5.18 (%s)' % ', '.join(item_changes.get(i, ['### NONE'])))
                                              if mono(r) else 'the ceiling at its document`s next edition, listed'))
    m_items = sorted(set(K.ITEMS_BOTH + K.ITEMS_READER + K.ITEMS_SEAT))
    m_missing = [i for i in m_items if not item_changes.get(i)]
    sentences = set()
    for c in K.CHANGES:
        if c[0].startswith('C'):
            sentences.add((c[1], next(s for s in _segs(lines_of(_show(PP, PRE_PP, M17))[c[1] - 1]) if c[2] in s or s in c[2] or c[2][:40] in s)))
    m_lines = sorted(set(c[1] for c in K.CHANGES if c[0].startswith('C')) | {2234})
    other = {}
    for d in AG['dis_x']:
        r = res[d['id']]
        if not mono(r):
            other.setdefault(r['doc'], []).append((r['line'], d['id'], 'seat BEYOND, reader AT'))
    for i in agreed:
        r = res[i]
        if not mono(r):
            other.setdefault(r['doc'], []).append((r['line'], i, 'both BEYOND'))
    n_other = sum(len(v) for v in other.values())
    L += ['', '### THE MONOGRAPH`S SUBSET: %d items (both BEYOND %d, the reader`s BEYOND %d, the seat`s BEYOND %d), each answered: %s ; '
          'the ruled changes %d on %d lines and the history line ; the distinct sentences rewritten %d ; items unanswered %s' % (
              len(m_items), len(K.ITEMS_BOTH), len(K.ITEMS_READER), len(K.ITEMS_SEAT), {i: item_changes[i] for i in m_items},
              sum(1 for c in K.CHANGES if c[0].startswith('C')), len(set(c[1] for c in K.CHANGES if c[0].startswith('C'))),
              len(sentences), m_missing or 'none'),
          '', '### THE OTHER DOCUMENTS` SENTENCES, LISTED FOR THEIR NEXT EDITIONS (%d sentences in %d documents; none written in this act):' % (
              n_other, len(other))]
    for doc in sorted(other):
        L.append('  %s : %s' % (doc, '; '.join(':%s (%s, %s)' % (ln, i, how) for ln, i, how in sorted(other[doc], key=lambda x: (x[0] or 0)))))
    # ### the restatement survey: every needle's yield over v5.17's body, and each hit line's fate
    M = lines_of(_show(PP, PRE_PP, M17))
    changed = {}
    for c in K.CHANGES:
        changed.setdefault(c[1], []).append(c[0])
    L += ['', '### THE RESTATEMENT SURVEY (the restatement clause, OPEN_TRAILS :12192): eight needles over v5.17`s body (:1-:%d), every hit '
          'read by hand -- each needle`s yield, then every hit line`s fate:' % (K.M_CORR - 1)]
    hitlines = {}
    for name, pat in K.SURVEY_NEEDLES:
        ls = [i for i, l in enumerate(M[:K.M_CORR - 1], 1) if any(re.search(pat, s, re.I) for s in _segs(l))]
        L.append('  needle %-16s %3d lines' % (name, len(ls)))
        for i in ls:
            hitlines.setdefault(i, []).append(name)
    fates = {'rewritten': 0, 'history': 0, 'kept': 0, 'none': 0}
    for i in sorted(hitlines):
        if i in changed:
            f = 'rewritten (%s)' % ', '.join(changed[i])
            fates['rewritten'] += 1
        elif 2231 <= i <= 2239:
            f = 'the dated block: the history line H1 beneath it'
            fates['history'] += 1
        elif i in K.SURVEY_KEPT:
            f = 'carried -- %s' % K.SURVEY_KEPT[i]
            fates['kept'] += 1
        else:
            f = '### NO FATE'
            fates['none'] += 1
        L.append('    :%-5d [%s] %s' % (i, ','.join(hitlines[i]), f))
    L += ['  ### the hit lines: %d -- rewritten %d, under the history line %d, carried with a reason %d, with no fate %d' % (
        len(hitlines), fates['rewritten'], fates['history'], fates['kept'], fates['none']),
          '', '### ### **THE MONOGRAPH`S RESIDUE SENTENCES AT THE CEILING: %d ITEMS (%d DISTINCT SENTENCES REWRITTEN, ONE ITEM BY THE HISTORY '
          'LINE); THE RESTATEMENT CLAUSE`S SENTENCES %d; THE OTHER DOCUMENTS` %d LISTED.**' % (
              len(m_items), len(sentences), sum(1 for c in K.CHANGES if c[0].startswith('P')), n_other)]
    b = cur + (NL.join(L) + NL).encode('utf-8')
    p = _p('b621_rows.txt')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  appended Part C to %sb621_rows.txt (%d bytes)' % ('DRY ' if DRY else '', len(b)))
    put_json('b621_residue.json', dict(at=utc(), dis=rows_, agreed=agreed, m_items=m_items, item_changes=item_changes, m_missing=m_missing,
                                       m_sentences=len(sentences), m_lines=m_lines, other={k: v for k, v in other.items()}, n_other=n_other,
                                       survey={str(k): v for k, v in hitlines.items()}, fates=fates, rows_sha=RJ['sha256'], sha256=R2.sha(b)))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE MONOGRAPH AT v5.18
VERSION18 = ('**v5.18, 2026-10-04** — under `(R231)`(3)(i), (iv) and (5) and the author’s answer before the seal: the enumeration sentence of '
             '§19.4 at the ceiling, each class’s compiled exclusion read as a condition on a real σ and the step to ξ’s zeros as the located '
             'clause (RH-60 and FINDINGS :7210); every residue sentence either second reader read beyond the ceiling at the ceiling, the one in '
             'the dated block of 2026-08-14 by a history line beneath it; the sentences restating them by the restatement clause; beside v5.17, '
             'which stands unedited; every change is recorded in the back matter.  ')
READINGS18 = [
    ('R-1', 'the next version by the document’s own series is v5.18, written beside v5.17 as day1/A_Place_to_Stand_v5_18.md; its version line '
            'goes above v5.17’s'),
    ('R-2', 'the body is every line above the monograph’s own Correspondence heading, as at v5.17; the back matter of v5.14 to v5.17 is '
            'carried with its own-line cells re-pinned to this file'),
    ('R-3', '(R231)(3)(i)’s sentence is v5.16 :1217, v5.17 :1218, this file’s :1219 -- the ferry’s “:1217” in v5.17 names v5.16’s line, the '
            'navigator’s; its rewrite states that each class’s compiled exclusion is a condition on a real σ and that the step from the classes '
            'to ξ’s zeros is the located clause, citing RH-60 and FINDINGS :7210'),
    ('R-4', 'the residue sentences at the ceiling are those either reader read BEYOND, by the author’s answer before the seal (option 3): 33 '
            'items -- the 13 both readers read beyond, the one the reader read beyond and the seat at, and the 19 the seat read beyond and the '
            'reader at; an item quoting a window takes the ceiling on the sentence its reason names, and on the sentence the reader’s line '
            'names where it names another'),
    ('R-5', 'the ceiling clause takes the object a sentence names, the rest of the sentence unchanged; for a sentence naming C₂ as the Euler '
            'product, the object is C₂’s compiled exclusion, a condition on a real σ in which the Euler product does not enter (RH-60, FINDINGS '
            ':7210); for a sentence settling the catalogue at ξ, the object is the place count Ostrowski closes and the open clause h2 '
            '(OPEN_TRAILS :12072)'),
    ('R-6', 'the restatement clause reaches every unmarked body sentence restating a ruled claim; the survey is eight needles over the body, '
            'every hit read by hand, the hits kept carried with their reasons in relay data/b621_rows.txt and data/b621_edition_PLACE.txt; '
            'the C₂ object’s restatements were surveyed whole by the addendum FINDINGS :7210 names, and are the residue’s own items'),
    ('R-7', 'the dated block of 2026-08-14 (v5.17 :2223-:2239) is one paragraph; the history line goes beneath it, after its blank line, and '
            'names the sentences it answers'),
    ('R-8', 'the carried ceiling hits stand as v5.17 recorded them, each under its named exception, their lines re-pinned; the era '
            'annotation’s carried-by-history row is listed again here, the scanner reading the exceptions of a file’s last back matter'),
]
REPIN18 = [
    r'(\*\*[A-Z0-9-]+\*\* :)(\d+)( \(v5\.1[34567] :)',
    r'^(- :)(\d+)( \(v5\.1[4567] :)',
    r'(with the history line at :)(\d+)()',
    r'(^- :|and :)(\d+)( beneath :)',
    r'(:\d+ beneath :)(\d+)()',
    r'(\*\*H\d+\*\* :)(\d+)( beneath :)',
    r'^(- :)(\d+)(, carried-by-history)',
    r'(here the note is :)(\d+)()',
    r'(the body’s one live stem \(:)(\d+)(\))',
    r'(The depths sentence \(:)(\d+)(, )',
    r'(the scanner’s one live stem at :)(\d+)()',
    r'((?<=[:;,] ):)(\d+)((?= “))',
    r'(^- row \d+ \(v5\.13 :\d+, [^)]*\) — rewritten at :)(\d+)( by )',
    r'(^- row \d+ \(v5\.13 :\d+, [^)]*\) — :)(\d+)( — )',
]


def _w(n):
    return n if n < 19 else (n + 1 if n <= K.HISTORY_AFTER else n + 3)


def _repin(l):
    subs = []
    for pat in REPIN18:
        def f(m):
            o = int(m.group(2))
            subs.append((o, _w(o)))
            return m.group(1) + str(_w(o)) + m.group(3)
        l = re.sub(pat, f, l)
    return l, subs


def _corr_idx(ls):
    return next(i for i, l in enumerate(ls) if l.startswith(CORR_HEAD))


def _ed(path):
    p = os.path.join(SP, os.path.basename(path).replace('.md', '_dry.md')) if DRY else os.path.join(PP, *path.split('/'))
    return lines_of(io.open(p, encoding='utf-8').read())


def _by_line():
    by = {}
    for c in K.CHANGES:
        by.setdefault(c[1], []).append(c)
    return by


def mono_edition(*a):
    """### PLACE-papers day1/A_Place_to_Stand_v5_18.md beside v5.17 (unedited): the version line, the 68 changes, the history line, the
    ### carried back matter re-pinned and this act's appended. Requires the rows bank. Writes the edition and data/b621_mono_edition.json."""
    if not os.path.exists(_p('b621_residue.json')):
        sys.exit('### THE ROWS AND THE RESIDUE ARE NOT BANKED -- NOTHING WRITTEN')
    M, bad = K.resolve_changes()
    if bad:
        sys.exit('### THE CHANGES DO NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    disk = lines_of(io.open(os.path.join(PP, *M17.split('/')), encoding='utf-8').read())
    if disk != M:
        sys.exit('### v5.17 ON DISK IS NOT ITS BLOB AT %s -- NOTHING WRITTEN' % PRE_PP)
    dest = os.path.join(SP, 'A_Place_to_Stand_v5_18_dry.md') if DRY else os.path.join(PP, *M18.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    by = _by_line()
    b6 = M.index(B606_TAG) + 1
    out, rep, seg_d, where = [], [], [], {}
    for i, l in enumerate(M, 1):
        if i == 19:
            out.append(VERSION18)
        s = l
        for c in by.get(i, []):
            if s.count(c[2]) != 1:
                sys.exit('### %s`S FRAGMENT IS NOT ONCE ON :%d -- NOTHING WRITTEN' % (c[0], i))
            s = s.replace(c[2], c[3])
        if i in by:
            seg_d.append(dict(line=i, ids=[c[0] for c in by[i]], d=len(_segs(s)) - len(_segs(l))))
        if i >= b6:
            s2, subs = _repin(s)
            if subs:
                rep.append(dict(v17=i, v18=_w(i), subs=subs))
            s = s2
        out.append(s)
        where[i] = len(out)
        if _w(i) != len(out):
            sys.exit('### THE MAP DRIFTED AT :%d' % i)
        if i == K.HISTORY_AFTER:
            out += [K.HISTORY, '']
    hist_line = K.HISTORY_AFTER + 2
    bm = _mono_bm(M, rep, hist_line)
    out2 = out + bm
    text = NL.join(out2) + NL
    b = text.encode('utf-8')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ci, cm = _corr_idx(out2), _corr_idx(M)
    E = dict(at=utc(), dry=DRY, path=M18, sha256=sha(b), lines=len(out2), where={str(k): v for k, v in where.items()}, version=19,
             history=hist_line, corr=ci + 1, bm=out2.index(BM_TAG18) + 1,
             changes=[dict(id=c[0], line=c[1], line18=_w(c[1]), old=c[2], new=c[3], clause=c[4], items=c[5], why=c[6], cites=c[7]) for c in K.CHANGES],
             seg_d=seg_d, rep=rep, n_body=_count(out2[:ci]), n_cur_body=_count(M[:cm]), n_backmatter=_count(out2[ci:]),
             n_cur_backmatter=_count(M[cm:]), n_full=_count(out2), version_lines=len(_segs(VERSION18)), history_lines=len(_segs(K.HISTORY)),
             credit=0, removals=0, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, M17)).strip(),
             new_hits=[(c[0], _hits(c[3])) for c in K.CHANGES if _hits(c[3])])
    put_json('b621_mono_edition.json', E)
    print('  %s : %d lines, sha256 %s ; body %d (v5.17 %d, %+d) ; version line %d, history line %d (at :%d) ; back matter %d (v5.17 %d) ; '
          'changes %d ; segment deltas %s ; re-pinned lines %d (cells %d) ; ceiling hits in the new wordings %s' % (
              dest, len(out2), E['sha256'][:16], E['n_body'], E['n_cur_body'], E['n_body'] - E['n_cur_body'], E['version_lines'],
              E['history_lines'], hist_line, E['n_backmatter'], E['n_cur_backmatter'], len(K.CHANGES),
              [(x['line'], x['d']) for x in seg_d if x['d']] or 'none', len(rep), sum(len(x['subs']) for x in rep), E['new_hits'] or 'none'))


def _era(M):
    t = M.index(B609_TAG)
    era = next(i + 1 for i, l in enumerate(M) if i > t and l.startswith('- :') and ', carried-by-history — the era annotation' in l)
    return int(re.match(r'^- :(\d+),', M[era - 1]).group(1))


def _mono_bm(M, rep, hist_line):
    q = _poss
    era17 = _era(M)
    by_kind = [('### The enumeration sentence, `(R231)`(3)(i)', [c for c in K.CHANGES if c[4].endswith('(3)(i)')]),
               ('### The residue sentences at the ceiling, `(R231)`(3)(iv) and the author’s answer before the seal',
                [c for c in K.CHANGES if c[0].startswith('C') and not c[4].endswith('(3)(i)')]),
               ('### The sentences restating a ruled claim, by the restatement clause (OPEN_TRAILS :12192)', [c for c in K.CHANGES if c[0].startswith('P')])]
    L = (['---', ''] if M[-1] == '' else ['', '---', '']) + [
        BM_TAG18, '', '## Back matter of v5.18 -- the second reader’s rulings applied, 2026-10-04, under `(R231)`(3)(i), (iv) and (5) and the '
        'author’s answer before the seal', '',
        '*This section records every change v5.18 makes to v5.17, which stands beside it unedited; each line cited is this file’s own. The back '
        'matter of v5.14, v5.15, v5.16 and v5.17 above is carried with its own-line cells re-pinned to this file (%d lines, %d cells; reading '
        'R-2).*' % (len(rep), sum(len(x['subs']) for x in rep)), '',
        '### The act’s readings, each the seat’s and strikeable', '']
    L += ['- **%s** %s.' % (k, q(v)) for k, v in READINGS18]
    for head, cs in by_kind:
        L += ['', head, '']
        for c in cs:
            L.append('- **%s** :%d (v5.17 :%d) — %s — %s — %s — was: “%s” — now: “%s” — cites: %s.' % (
                c[0], _w(c[1]), c[1], q(c[4]), ', '.join(c[5]), q(c[6]), c[2], c[3], q('; '.join(c[7]) or 'the reading its why names')))
    L += ['', '### The history line, by the history clause (OPEN_TRAILS :11908)', '',
          '- **H1** :%d beneath :%d-:%d (v5.17 :2231-:2239), the dated block of 2026-08-14 -- %s -- it answers: %s -- cites: %s.' % (
              hist_line, _w(2231), _w(2239), ', '.join(K.HISTORY_ITEMS), '; '.join('v5.17 :%d (this file’s :%d), %s' % (n, _w(n), q(t))
                                                                                  for n, t in K.HISTORY_COVERS), q('; '.join(K.HISTORY_CITES))),
          '', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228)', '']
    for cid, n, what, how in K.COLLISIONS:
        L.append('- **%s** %s — %s — %s.' % (cid, (':%d (v5.17 :%d)' % (_w(n), n)) if n else 'several lines', q(what), q(how)))
    L += ['', '### Removals', '', '- None: no sentence of v5.17 is removed.', '',
          '### Stem corrections', '',
          '- :%d, carried-by-history — the era annotation of 2026-08-14 (v5.17 :%d, v5.16 :2281, v5.15 :2272, v5.14 :2269, v5.13 :2264), carried '
          'as v5.14 to v5.17 carried it; listed again here because the scanner reads the exceptions of a file’s last back matter.' % (_w(era17), era17),
          '', '### Placement', '', '| object | path | status |', '|:--|:--|:--|',
          '| this edition, v5.18 | `%s` | written at b621 |' % M18, '| v5.17 | `%s` | unedited |' % M17,
          '| the sieve, v0.5, whose row RH-60 the changes cite | `%s` | unedited |' % SV5,
          '| the rows and residue bank | relay `data/b621_rows.txt` | banked before this edition |', '',
          '### Correspondence', '', '| claim, as v5.18 states it | the source | its line | status |', '|:--|:--|:--|:--|',
          '| each class’s exclusion compiles as a condition on a real σ, the Euler product entering none; the step from the classes to ξ’s zeros '
          'is the located clause | the sieve v0.5, RH-60 | :124 | cited at C01 and throughout |',
          '| the seven-class exclusion as compiled is a family of σ-conditions, its joint step RH restated | FINDINGS | :7210 | cited at C01 |',
          '| none_produce and its C₂ case | SIDE-kernel v1.5 = 0e5233f, Bridge/TheBridgeComplete.lean | :198, :157, :159 | cited at C01, C26 |',
          '| the balance for a prime p and a real exponent | SIDE-kernel v1.5 = 0e5233f, Kernel/Voice1.lean | :22 | cited at C02, C28 |',
          '| Conservation of Spectra’s terminal | SIDE-kernel v1.5 = 0e5233f, Kernel/ProductFormula_Rat.lean | :72 | cited at C25, P21 |',
          '| the located clause in its Weil form, equivalent to RH | h2_sign_iff_rh, SIDE-explicit-formula v0.2 = 5c72cad | ζ page node 8 | '
          'cited at H1 |', '', '### Version history', '',
          '- v5.18, 2026-10-04 — under `(R231)`(3)(i), (iv) and (5) and the author’s answer before the seal: the enumeration sentence at the '
          'ceiling (C01); the 33 residue items either second reader read beyond the ceiling at the ceiling (C01-C38, the dated block’s by H1); '
          '30 sentences restating a ruled claim by the restatement clause (P01-P30); the version line; nothing removed; v5.17 unedited beside it.', '']
    return L


def mono_termscan(*a):
    out = _scan(os.path.join(SP, 'A_Place_to_Stand_v5_18_dry.md') if DRY else os.path.join(PP, *M18.split('/')))
    put_txt('b621_mono_termscan.txt', out.rstrip(NL).split(NL))
    print([l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l or 'excepted' in l])


def _h17():
    """### v5.17's body hits, classified as b609 classified them (b609_record._classify17 on its own banked edition)."""
    import b609_record as R9
    E17 = json.loads(_show(RELAY, B609_MONO_AT, 'data/b609_mono_edition.json'))
    M = lines_of(_show(PP, PRE_PP, M17))
    h17, _h16 = R9._classify17(M, E17)
    return h17


def _classify18(ed, E, M):
    h17 = _h17()
    by = {}
    for h in h17:
        by.setdefault(h['line'], []).append(h['kind'])
    inv = {_w(n): n for n in range(1, len(M) + 1)}
    changed = set(c['line'] for c in E['changes'])
    out = []
    for i, l in enumerate(ed[:E['corr'] - 1], 1):
        src = inv.get(i)
        hs = _hits(l)
        for k, hit in enumerate(hs):
            if src is None:
                kind = 'history' if i == E['version'] else 'UNEXCEPTED'
            elif src in changed:
                kind = by.get(src, ['UNEXCEPTED'] * len(hs))[k] if _hits(M[src - 1]) == hs and len(by.get(src, [])) == len(hs) else 'UNEXCEPTED'
            else:
                kind = by[src][k] if len(by.get(src) or []) == len(hs) else 'UNEXCEPTED'
            out.append(dict(line=i, src=src, hit=hit, kind=kind))
    return out, h17


def mono_carried(E, ed, M):
    by = {}
    for c in E['changes']:
        by.setdefault(c['line'], []).append(c)
    rp = {x['v17'] for x in E['rep']}
    ok, bad = 0, []
    for n in range(1, len(M) + 1):
        if not M[n - 1].strip():
            continue
        x = _w(n)
        if n in by:
            s = M[n - 1]
            for c in by[n]:
                s = s.replace(c['old'], c['new'])
            bm = NL.join(ed[E['bm'] - 1:])
            good = ed[x - 1] == s and all(('was: “%s”' % c['old']) in bm and ('now: “%s”' % c['new']) in bm for c in by[n])
        elif n in rp:
            good = ed[x - 1] == _repin(M[n - 1])[0] and ed[x - 1] != M[n - 1]
        else:
            good = ed[x - 1] == M[n - 1]
        ok += good
        if not good:
            bad.append(n)
    hl = ed[E['history'] - 1] == K.HISTORY and ed[E['history'] - 2] == '' and ed[E['history']] == ''
    return ok, bad, hl


def mono_bank(*a):
    """### data/b621_edition_PLACE.txt and data/b621_h28_mono.json: every change old and new, the history line, the collisions, the 33
    ### items' answers, the restatement survey, the map, the counts, the ceiling, the scanner, H28a-H28c and H55c."""
    E = jl('b621_mono_edition.json')
    ed = _ed(M18)
    M = lines_of(_show(PP, PRE_PP, M17))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    RS = jl('b621_residue.json')
    scan = rd('b621_mono_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad, hl = mono_carried(E, ed, M)
    hits, h17 = _classify18(ed, E, M)
    kinds = {k: sum(1 for h in hits if h['kind'] == k) for k in sorted(set(h['kind'] for h in hits))}
    unexc = [h for h in hits if h['kind'] == 'UNEXCEPTED']
    bmt = NL.join(ed[E['bm'] - 1:])
    h28a_rows = [dict(id=c['id'], line=c['line18'], cites=c['cites'], recorded=('was: “%s”' % c['old']) in bmt and ('now: “%s”' % c['new']) in bmt)
                 for c in E['changes']]
    h_rec = ('- **H1** :%d beneath' % E['history']) in bmt and bool(K.HISTORY_CITES)
    h28a = 'HOLDS' if all(x['recorded'] and (x['cites'] or not x['id'].startswith('P')) for x in h28a_rows) and h_rec and hl else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur_body']
    rw = sum(abs(x['d']) for x in E['seg_d'])
    allowed = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines'] + rw
    strict = E['credit'] + E['removals'] + E['history_lines'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not unexc else 'REFUTED'
    n_items = len(RS['m_items'])
    h55c = 'HOLDS' if n_items >= 10 and not RS['m_missing'] and clean and not unexc else 'REFUTED'
    L = ['### OFFSET FROM v5.17 (R190)(3): +0 from :1, +1 from :19, +3 from :%d -- the version line above v5.17`s and the history line with '
         'its blank line after v5.17 :%d; every v5.17 line`s v5.18 line is printed below (the map), and every edition line cited here is the '
         'final file`s own.' % (K.HISTORY_AFTER + 1, K.HISTORY_AFTER), '',
         'b621 -- COMPONENT 4: THE MONOGRAPH`S NEXT VERSION, v5.18, (R231)(3)(i), (iv) AND (5) AND THE AUTHOR`S ANSWER BEFORE THE SEAL, BY THE '
         'FORM, ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v5.17 : PLACE-papers %s @ %s (blob %s), %d lines' % (M17, PRE_PP, E['cur_blob'][:8], len(M)),
         '### v5.18 : PLACE-papers %s, %d lines, sha256 %s' % (M18, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (E['version'], ed[E['version'] - 1]), '',
         '### EVERY CHANGE (%d), WITH ITS CLAUSE, THE ITEMS IT ANSWERS AND WHAT IT CITES:' % len(E['changes'])]
    for c in E['changes']:
        L += ['  %s  v5.17 :%d -> v5.18 :%d -- %s -- %s -- %s' % (c['id'], c['line'], c['line18'], c['clause'], ', '.join(c['items']), c['why']),
              '      was : %s' % c['old'], '      now : %s' % c['new'], '      cites: %s' % ('; '.join(c['cites']) or '(the reading its why names)')]
    L += ['', '### THE HISTORY LINE, PRINTED: v5.18 :%d (beneath the dated block`s paragraph, v5.17 :2231-:2239, after its blank line) %s' % (
        E['history'], ed[E['history'] - 1]),
          '### it answers: %s' % '; '.join('v5.17 :%d (v5.18 :%d), %s' % (n, _w(n), t) for n, t in K.HISTORY_COVERS), '',
          '### THE COLLISIONS (the precedence order, OPEN_TRAILS :12228):']
    L += ['  %s %s -- %s -- %s' % (cid, (':%d (v5.17 :%d)' % (_w(n), n)) if n else 'several lines', what, how) for cid, n, what, how in K.COLLISIONS]
    L += ['', '### THE 33 ITEMS AND THEIR ANSWERS: %s' % RS['item_changes'], '### the items unanswered: %s' % (RS['m_missing'] or 'none'), '',
          '### THE CHANGED BODY LINES (v5.17 numbering): %s' % sorted(set(c['line'] for c in E['changes'])),
          '### SEGMENT CHANGES ON THE CHANGED LINES: %s' % ([(x['line'], x['ids'], x['d']) for x in E['seg_d'] if x['d']] or 'none, every change '
                                                            'keeps its line`s segment count'),
          '### THE CARRIED BACK MATTER RE-PINNED: %d lines, %d cells' % (len(E['rep']), sum(len(x['subs']) for x in E['rep'])), '',
          '### EVERY NON-BLANK v5.17 LINE -> ITS v5.18 LINE (%d carried verbatim, rewritten with both wordings recorded, or re-pinned ; failing '
          '%s ; the history line in place %s):' % (ok, bad or 'none', hl)]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted(((int(k), v) for k, v in E['where'].items()))]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v5.17`s BODY %d ; v5.18`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v5.17`s %d), printed separately ; the edition whole %d' % (E['n_cur_body'], E['n_body'], body_dn, E['n_backmatter'],
                                                                         E['n_cur_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + history lines %d + one version line %d + the changes` '
          'segment changes %d = %d ; the strict count %d' % (body_dn, E['credit'], E['removals'], E['history_lines'], E['version_lines'], rw,
                                                             allowed, strict), '',
          '### THE CEILING, every hit in the body, by kind: %s' % kinds]
    L += ['    :%d (v5.17 :%s) "%s" -- %s' % (h['line'], h['src'], h['hit'], h['kind']) for h in hits]
    L += ['### THE SCANNER (banned_terms.py --new) on v5.18: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'),
          '### the whole-document figure: %d ceiling hits in the body, each carried as v5.17 recorded it, unexcepted %d (v5.17`s %d, its '
          'unexcepted %d)' % (len(hits) - len(unexc), len(unexc), len(h17), sum(1 for h in h17 if h['kind'] == 'UNEXCEPTED')), '',
          '### ### **H28a %s -- every change (%d) recorded with both wordings and citing what it rests on; the history line in place and recorded.**' % (
              h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner %s; ceiling hits unexcepted %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(unexc)),
          '### ### **H55c %s -- the monograph`s residue sentences at the ceiling %d (bound ten; %d distinct sentences rewritten, one item by the '
          'history line), and v5.18 scans %s with %d unexcepted.**' % (h55c, n_items, RS['m_sentences'], 'CLEAN' if clean else 'NOT CLEAN', len(unexc)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' if not bad and hl else '### ### **HELD AT A SENTENCE: see above.**']
    put_txt('b621_edition_PLACE.txt', L)
    put_json('b621_h28_mono.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H55c=h55c, h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed,
                                        strict=strict, rw=rw, backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, clean=clean,
                                        unexcepted=len(unexc), carried_hits=len(hits) - len(unexc), kinds=kinds, hits=hits, carried_ok=ok,
                                        carried_bad=bad, history_in_place=hl, n_items=n_items, m_sentences=RS['m_sentences']))
    print('H28a %s H28b %s H28c %s H55c %s ; carried %d bad %s history %s ; body_dn %d allowed %d strict %d ; live %s ; unexcepted %d ; hits %d' % (
        h28a, h28b, h28c, h55c, ok, bad, hl, body_dn, allowed, strict, live.group(1) if live else None, len(unexc), len(hits)))


def mono_repin(*a):
    """### THE RE-PIN STEP, THE FORM'S LAST, for v5.18. Writes data/b621_repin_mono.txt."""
    E = jl('b621_mono_edition.json')
    ed = _ed(M18)
    M = lines_of(_show(PP, PRE_PP, M17))
    changed = set(c['line'] for c in E['changes'])
    checks = []
    for x in E['rep']:
        for o, n in x['subs']:
            checks.append(('carried cell :%d -> :%d (at :%d)' % (o, n, x['v18']), _w(o) == n and (ed[n - 1] == M[o - 1] or o in changed)))
    bmt = NL.join(ed[E['bm'] - 1:])
    for m in re.finditer(r'^- \*\*([A-Z0-9-]+)\*\* :(\d+) \(v5\.17 :(\d+)\)', bmt, re.M):
        a_, b_ = int(m.group(2)), int(m.group(3))
        checks.append(('this act`s %s cites :%d for v5.17 :%d' % (m.group(1), a_, b_), _w(b_) == a_ and bool(ed[a_ - 1].strip())))
    for c in E['changes']:
        checks.append(('%s`s new wording on :%d' % (c['id'], c['line18']), ed[c['line18'] - 1].count(c['new']) == 1))
    era = re.search(r'^- :(\d+), carried-by-history — the era annotation of 2026-08-14 \(v5\.17 :(\d+),', bmt, re.M)
    checks.append(('the era annotation re-listed at :%s for v5.17 :%s' % (era.group(1) if era else '?', era.group(2) if era else '?'),
                   bool(era) and _w(int(era.group(2))) == int(era.group(1)) and ed[int(era.group(1)) - 1] == M[int(era.group(2)) - 1]))
    hm = re.search(r'^- \*\*H1\*\* :(\d+) beneath :(\d+)-:(\d+)', bmt, re.M)
    checks.append(('the history line H1 at :%s beneath :%s-:%s' % (hm.group(1) if hm else '?', hm.group(2) if hm else '?', hm.group(3) if hm else '?'),
                   bool(hm) and int(hm.group(1)) == E['history'] and ed[E['history'] - 1] == K.HISTORY and int(hm.group(2)) == _w(2231)
                   and int(hm.group(3)) == _w(2239) and ed[_w(2239) - 1] == M[2238]))
    checks.append(('the version line on :19 above v5.17`s', ed[18] == VERSION18 and ed[19] == M[18] and M[18].startswith('**v5.17, 2026-10-03**')))
    checks.append(('the Correspondence heading on :%d' % E['corr'], ed[E['corr'] - 1].startswith(CORR_HEAD)))
    checks.append(('the back-matter tag on :%d' % E['bm'], ed[E['bm'] - 1] == BM_TAG18))
    for t in (B606_TAG, B607_TAG, B608_TAG, B609_TAG):
        checks.append(('the tag carried: %s' % t[5:30], t in ed and ed.index(t) + 1 == _w(M.index(t) + 1)))
    bank = rd('b621_edition_PLACE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v5.17') and bank.count('### OFFSET FROM') == 1))
    fp = os.path.join(SP, 'A_Place_to_Stand_v5_18_dry.md') if DRY else os.path.join(PP, *M18.split('/'))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and sha(open(fp, 'rb').read()) == E['sha256']))
    for m in re.finditer(r'v5\.17 :(\d+) -> v5\.18 :(\d+)', bank):
        checks.append(('the diff bank`s v5.17 :%s -> v5.18 :%s' % (m.group(1), m.group(2)), _w(int(m.group(1))) == int(m.group(2))))
    L = ['### b621 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % M18, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b621_repin_mono.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE SYNTHESES AT THEIR NEXT VERSIONS
def _syn_bm_index(ls):
    return next(i for i, l in enumerate(ls) if l.startswith('## Back matter'))


def _syn_version_index(ls, vold):
    return next(i for i, l in enumerate(ls[:14]) if l.startswith('*%s, ' % vold))


def _tier(ls):
    return ls[2] if len(ls) > 2 else ''


def syn_edition(key, *a):
    """### PLACE-papers <synthesis> at its next version beside the current (unedited): the version line, the re-graded rows' grade and
    ### backing cells, the fact the re-read found, a version-history line beneath the carried history, and this act's back matter; the tier
    ### line read and left. Requires the rows bank. Writes the edition and data/b621_syn_<key>.json."""
    if key not in EDITED:
        sys.exit('### %s: NO ROW OF IT MOVES OR IS CORRECTED -- NO EDITION' % key)
    if not os.path.exists(_p('b621_rows.json')):
        sys.exit('### THE ROWS ARE NOT BANKED -- NOTHING WRITTEN')
    path = K.SYN[key]
    path2, vnew, vold = K.NEXT[key]
    v1 = lines_of(_show(PP, PRE_PP, path))
    disk = lines_of(io.open(os.path.join(PP, *path.split('/')), encoding='utf-8').read())
    if disk != v1:
        sys.exit('### %s ON DISK IS NOT ITS BLOB AT %s -- NOTHING WRITTEN' % (path, PRE_PP))
    bad = K.resolve_rows({key: v1, **{k: lines_of(_show(PP, PRE_PP, p)) for k, p in K.SYN.items() if k != key}})
    if bad:
        sys.exit('### THE CELLS DO NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    dest = os.path.join(SP, os.path.basename(path2).replace('.md', '_dry.md')) if DRY else os.path.join(PP, *path2.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE EDITION EXISTS -- NOTHING WRITTEN')
    RJ = jl('b621_rows.json')
    regs = [r for r in K.REGRADES if r[1] == key]
    facts = [f for f in K.FACTS if f[1] == key]
    out = list(v1)
    vi = _syn_version_index(out, vold)
    nfact = (', and %d row’s cell corrected by the fact clause' % len(facts)) if facts else ''
    ver_new = ('*%s, %s -- written at b621 under `(R231)`(3)(iii) and (5), beside %s: %d rows re-graded where the second reader read them lower '
               'and no line the packet omitted carries the higher grade%s; the tier re-read under the load-bearing clause and unmoved; every '
               'change recorded in the back matter.*' % (vnew, DATE, vold, len(regs), nfact))
    old_ver = out[vi]
    out[vi] = ver_new
    changes = []
    for rid, _k, cid, og, ng, ob, nb in regs:
        i = next(j for j, l in enumerate(out) if l.startswith('| %s |' % cid))
        c = K.row_cells(out[i])
        was = out[i]
        c[3], c[4] = ng, nb
        out[i] = '| ' + ' | '.join(c) + ' |'
        changes.append(dict(kind='regrade', id=rid, claim=cid, line=i + 1, was=was, now=out[i], og=og, ng=ng, ob=ob, nb=nb,
                            why=K.OTHERS[rid][2]))
    for fid, _k, cid, old, new, why in facts:
        i = next(j for j, l in enumerate(out) if l.startswith('| %s |' % cid))
        was = out[i]
        out[i] = out[i].replace(old, new)
        changes.append(dict(kind='fact', id=fid, claim=cid, line=i + 1, was=was, now=out[i], old=old, new=new, why=why))
    vh = out.index('### Version history')
    last = max(j for j in range(vh, len(out)) if out[j].startswith('- **v0.'))
    hist = ('- **%s, %s (b621, `(R231)`(3)(iii) and (5))**: %d rows re-graded, each recorded in this version’s back matter with both cells and '
            'its reason%s; the tier line read under the load-bearing clause and unmoved%s.' % (
                vnew, DATE, len(regs), (', and the fact %s' % ', '.join(f[0] for f in facts)) if facts else '',
                '; v0.2 (b615) moved the Correspondence to the back matter under that clause' if key == '2D' else ''))
    out.insert(last + 1, hist)
    hist_line = last + 2
    while out and out[-1] == '':
        out.pop()
    stood = [x for x in RJ['others'] if x['key'] == key and x['verdict'] in ('stands', 'unchanged')] + [x for x in RJ['kv'] if x['key'] == key]
    bm = ['', '## Back matter of %s — written %s by b621 under the author’s ruling `(R231)`(3)(iii) and (5)' % (vnew, DATE), '',
          '*This section records every change %s makes to %s, which stands beside it unedited; each line cited is this file’s own. The rows were '
          're-read and banked before this file was written (relay data/b621_rows.txt).*' % (vnew, vold), '',
          '### The rows re-graded, `(R231)`(3)(iii): the second reader’s lower grade governs where no line the packet omitted carries the higher', '']
    for c in changes:
        if c['kind'] == 'regrade':
            bm.append('- **%s** :%d (%s) — was: “%s | %s” — now: “%s | %s” — %s.' % (c['claim'], c['line'], c['id'], c['og'], c['ob'], c['ng'], c['nb'],
                                                                              c['why']))
    bm += ['', '### The second reader’s other rows here, standing', '']
    for x in stood:
        why = K.KV[x['id']]['reason'] if x['id'] in K.KV else K.OTHERS[x['id']][2]
        how = ('stands at kernel-verified on its terminal’s statement' if x['id'] in K.KV else
               'stands at %s on %s' % (x['grade'], x['omitted']) if x['verdict'] == 'stands' else 'keeps %s, the lower grade' % x['grade'])
        bm.append('- **%s** :%s (%s) — %s: %s.' % (x['claim'], x['line'], x['id'], how, why))
    if not stood:
        bm.append('- None.')
    bm += ['', '### The tier, re-read under the load-bearing clause (OPEN_TRAILS :12699)', '',
           '- The tier line stands as %s wrote it: no kernel-verified row moves (%s), so the load-bearing reading of the re-read at b615 (relay '
           'data/b615_reread.txt) is unchanged and the Correspondence stays where the tier puts it.' % (
               vold, ', '.join('%s stands' % x['claim'] for x in RJ['kv'] if x['key'] == key) or 'none of its rows reads kernel-verified in the sample')]
    if facts:
        bm += ['', '### Fact corrections', '']
        for c in changes:
            if c['kind'] == 'fact':
                bm.append('- **%s** :%d (%s) — was: “%s” — now: “%s” — %s.' % (c['claim'], c['line'], c['id'], c['old'], c['new'], c['why']))
    bm += ['', '### Placement', '', '| object | path | status |', '|:--|:--|:--|',
           '| this document, %s | `%s` | written at b621 |' % (vnew, path2), '| %s | `%s` | unedited |' % (vold, path),
           '| the rows bank | relay `data/b621_rows.txt` | banked before this document |', '']
    out2 = out + bm
    b = (NL.join(out2) + NL).encode('utf-8')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    bi1, bi2 = _syn_bm_index(v1), _syn_bm_index(out2)
    put_json('b621_syn_%s.json' % key, dict(at=utc(), dry=DRY, key=key, path=path2, v1=path, v1_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, path)).strip(),
                                            sha256=sha(b), lines=len(out2), version=vi + 1, version_old=old_ver, version_new=ver_new,
                                            history=hist_line, history_text=hist, changes=changes, tier_old=_tier(v1), tier_new=_tier(out2),
                                            bm=out2.index(bm[1]) + 1, n_body=_count(out2[:bi2]), n_cur_body=_count(v1[:bi1]),
                                            version_seg_d=len(_segs(ver_new)) - len(_segs(old_ver)),
                                            new_hits=[(c['id'], _hits(c['now'])) for c in changes if _hits(c['now']) != _hits(c['was'])]))
    print('  %s : %d lines, sha256 %s ; %d changes ; the tier line unchanged %s ; body %d (%s %d) ; new ceiling hits %s' % (
        dest, len(out2), sha(b)[:16], len(changes), _tier(v1) == _tier(out2), _count(out2[:bi2]), vold, _count(v1[:bi1]),
        [(c['id'], _hits(c['now'])) for c in changes if _hits(c['now']) != _hits(c['was'])] or 'none'))


def syn_termscan(key, *a):
    J = jl('b621_syn_%s.json' % key)
    p = os.path.join(SP, os.path.basename(J['path']).replace('.md', '_dry.md')) if DRY else os.path.join(PP, *J['path'].split('/'))
    out = _scan(p)
    put_txt('b621_syn_termscan_%s.txt' % key, out.rstrip(NL).split(NL))
    print(key, [l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l])


def syn_bank(key, *a):
    """### data/b621_edition_<key>.txt and data/b621_h28_<key>.json: every change with both cells, the tier lines, the carried lines, the
    ### counts, the scanner, the re-pin of the back matter's own-line cells, H28a-H28c and the tier's fate (H55b)."""
    J = jl('b621_syn_%s.json' % key)
    p = os.path.join(SP, os.path.basename(J['path']).replace('.md', '_dry.md')) if DRY else os.path.join(PP, *J['path'].split('/'))
    ed = lines_of(io.open(p, encoding='utf-8').read())
    if sha((NL.join(ed) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    v1 = lines_of(_show(PP, PRE_PP, J['v1']))
    scan = rd('b621_syn_termscan_%s.txt' % key)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    chl = {c['line']: c for c in J['changes']}
    ok, bad = 0, []
    for i, l in enumerate(v1, 1):
        if not l.strip():
            continue
        if i == J['version']:
            good = ed[i - 1] == J['version_new']
        elif i in chl:
            good = ed[i - 1] == chl[i]['now']
        else:
            j = i if i < J['history'] else i + 1
            good = ed[j - 1] == l
        ok += good
        if not good:
            bad.append(i)
    bmt = NL.join(ed[J['bm'] - 1:])
    h28a_rows = []
    for c in J['changes']:
        if c['kind'] == 'regrade':
            rec = ('was: “%s | %s”' % (c['og'], c['ob'])) in bmt and ('now: “%s | %s”' % (c['ng'], c['nb'])) in bmt and bool(c['why'])
        else:
            rec = ('was: “%s”' % c['old']) in bmt and ('now: “%s”' % c['new']) in bmt
        h28a_rows.append(dict(id=c['id'], claim=c['claim'], line=c['line'], recorded=rec))
    h28a = 'HOLDS' if all(x['recorded'] for x in h28a_rows) and ed[J['history'] - 1] == J['history_text'] else 'REFUTED'
    body_dn = J['n_body'] - J['n_cur_body']
    allowed = abs(J['version_seg_d']) + sum(abs(len(_segs(c['now'])) - len(_segs(c['was']))) for c in J['changes'])
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    unexc = J['new_hits']
    h28c = 'HOLDS' if clean and not unexc else 'REFUTED'
    tier_same = J['tier_old'] == J['tier_new']
    # ### the re-pin: every own-line cell of this act's back matter names the line it cites
    rp = []
    for m in re.finditer(r'^- \*\*([A-Z]{2}-\d\d)\*\* :(\d+) \((R\d{3}|F\d\d)\)', bmt, re.M):
        n = int(m.group(2))
        rp.append(('%s at :%d' % (m.group(1), n), 0 < n <= len(ed) and ed[n - 1].startswith('| %s |' % m.group(1))))
    rp.append(('the version line at :%d' % J['version'], ed[J['version'] - 1] == J['version_new']))
    rp.append(('the history line at :%d' % J['history'], ed[J['history'] - 1] == J['history_text']))
    rp.append(('the tier line at :3', ed[2] == J['tier_old']))
    L = ['b621 -- COMPONENT 4: %s AT ITS NEXT VERSION, (R231)(3)(iii) AND (5)' % key, '',
         '### the current: PLACE-papers %s @ %s (blob %s), %d lines' % (J['v1'], PRE_PP, J['v1_blob'][:8], len(v1)),
         '### the next: PLACE-papers %s, %d lines, sha256 %s' % (J['path'], J['lines'], J['sha256']), '',
         '### THE VERSION LINE :%d' % J['version'], '      was : %s' % J['version_old'], '      now : %s' % J['version_new'], '',
         '### THE CHANGES (%d):' % len(J['changes'])]
    for c in J['changes']:
        L += ['  %s %s :%d (%s)' % (c['id'], c['claim'], c['line'], c['kind']), '      was : %s' % c['was'], '      now : %s' % c['now'],
              '      why : %s' % c['why']]
    L += ['', '### THE VERSION-HISTORY LINE :%d %s' % (J['history'], J['history_text']),
          '### THE TIER LINE :3, the current and the next equal: %s' % tier_same, '      %s' % J['tier_old'][:600], '',
          '### EVERY NON-BLANK LINE OF THE CURRENT CARRIED, CHANGED AS RECORDED, OR THE VERSION LINE: %d ; failing %s' % (ok, bad or 'none'),
          '### THE COUNTS: the body (above the first back-matter heading) %d against the current`s %d (%+d); the allowed %d (the version line`s and '
          'the changed rows` segment changes)' % (J['n_body'], J['n_cur_body'], body_dn, allowed),
          '### THE SCANNER (banned_terms.py --new): live uses %s ; verdict %s ; new ceiling hits on changed lines %s' % (
              live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN', unexc or 'none'),
          '### THE RE-PIN: %s ; %d of %d hold' % ([x for x, okk in rp if not okk] or 'every citation holds', sum(okk for _x, okk in rp), len(rp)), '',
          '### ### **H28a %s -- every change (%d) recorded with both wordings and its reason; the version-history line beneath the carried history.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d against at most %d.**' % (h28b, body_dn, allowed),
          '### ### **H28c %s -- the scanner %s; new ceiling hits %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(unexc)),
          '### ### **THE TIER: %s.**' % ('UNMOVED' if tier_same else 'MOVED'),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' if not bad else '### ### **HELD AT A LINE: see above.**']
    put_txt('b621_edition_%s.txt' % key, L)
    put_json('b621_h28_%s.json' % key, dict(H28a=h28a, H28b=h28b, H28c=h28c, tier_same=tier_same, carried_ok=ok, carried_bad=bad, body_dn=body_dn,
                                           allowed=allowed, clean=clean, live=int(live.group(1)) if live else None, unexcepted=len(unexc),
                                           repin=[sum(okk for _x, okk in rp), len(rp)], h28a_rows=h28a_rows))
    print('%s : H28a %s H28b %s H28c %s ; tier same %s ; carried %d bad %s ; re-pin %d of %d' % (key, h28a, h28b, h28c, tier_same, ok, bad,
                                                                                                sum(okk for _x, okk in rp), len(rp)))


# ================================================================================ COMPONENT 5: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b621_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b621_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b621_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; diff lines %d' % (k, rc, len(b), changed, secs, len(dl)))


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b621 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b621_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b621_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE SCORES AND THE RECORD
HKEYS = ('H55a', 'H55b', 'H55c', 'H55d')
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
EDITIONS = [M18] + [K.NEXT[k][0] for k in EDITED]
CURRENTS = ('README.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'day1/A_Place_to_Stand_v5_14.md', 'day1/A_Place_to_Stand_v5_15.md',
            'day1/A_Place_to_Stand_v5_16.md', M17, 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md', SV5, 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md') + tuple(K.SYN.values())


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def _epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no kernel touched; no current version edited; no file written beyond the edition files,
    ### the rows bank, the diff banks, the re-emitted pages, the record lines and the trails. ### THE STANDING REPAIR (OPEN_TRAILS :12799):
    ### `trail_line` is the line the trail record's head takes on OPEN_TRAILS; the record is read at that line once written and as pending
    ### while the trails stop short of it (b620's trap counted: a pending record is OPEN_TRAILS' write)."""
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
    Z, X = (jl('b621_page_%s.json' % k) if os.path.exists(_p('b621_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    face = jl('b621_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state(list(face)).items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + EDITIONS + [p['page'] for p in (Z, X) if p.get('changed')])
    created = sorted(set(x for x in g(PP, 'diff', '--name-only', '--diff-filter=ADR', PRE_PP, 'HEAD').split(NL) if x.strip())
                     | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL)
                           if x.startswith('?? ')))
    cur_ok = all((_show(PP, PRE_PP, p) or '') == (_show(PP, 'HEAD', p) or '') and (_show(PP, PRE_PP, p) or '') == R2.cr0(
        open(os.path.join(PP, *p.split('/')), 'rb').read()).decode('utf-8', 'replace') for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b621_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b620_closing_push_out.txt'))
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])   # ### the pending record is OPEN_TRAILS' write when it is the act's only one there
    ok = kern_same and created == sorted(EDITIONS) and cur_ok and pp_ch == want_pp and relay_beyond == [] and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; kernels unmoved since the face %s; created %s (wanted the editions %s); the current versions and the documents read '
            'unedited %s; PLACE-papers %s (wanted %s); %s; relay beyond the act`s banks, tools and the table %s' % (
                kern_same, created, sorted(EDITIONS), cur_ok, pp_ch, want_pp, rec_state, relay_beyond))


def _h28_all():
    out = {'mono': jl('b621_h28_mono.json') if os.path.exists(_p('b621_h28_mono.json')) else {}}
    for k in EDITED:
        out[k] = jl('b621_h28_%s.json' % k) if os.path.exists(_p('b621_h28_%s.json' % k)) else {}
    return out


def scores(*a):
    RJ = jl('b621_rows.json')
    RS = jl('b621_residue.json') if os.path.exists(_p('b621_residue.json')) else {}
    H = _h28_all()
    ME = jl('b621_mono_edition.json') if os.path.exists(_p('b621_mono_edition.json')) else {}
    SJ = {k: (jl('b621_syn_%s.json' % k) if os.path.exists(_p('b621_syn_%s.json' % k)) else {}) for k in EDITED}
    Z, X = (jl('b621_page_%s.json' % k) if os.path.exists(_p('b621_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    arms2 = rd('b621_page_arms_c2.txt')
    rep_m = rd('b621_repin_mono.txt')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    h28s = {k: tuple(v.get(x) for x in ('H28a', 'H28b', 'H28c')) for k, v in H.items()}
    h28_all = all(v == ('HOLDS', 'HOLDS', 'HOLDS') for v in h28s.values()) and len(h28s) == 1 + len(EDITED)
    held = (H['mono'].get('carried_bad') == [] and H['mono'].get('history_in_place') is True
            and all(H[k].get('carried_bad') == [] for k in EDITED))
    tiers = {k: H[k].get('tier_same') for k in EDITED}
    untouched = [k for k in K.SYN if k not in EDITED and not os.path.exists(os.path.join(PP, *K.NEXT[k][0].split('/')))]
    h55b = all(v is True for v in tiers.values()) and len(untouched) == len(K.SYN) - len(EDITED)
    # ### S1: the rows bank before any edition -- its stamp and its file before every edition's
    ed_at = [x.get('at') for x in [ME] + list(SJ.values())]
    rows_t = _epoch(RJ.get('at', ''))
    s1 = bool(rows_t) and all(_epoch(t or '') and _epoch(t) >= rows_t for t in ed_at) and all(
        os.path.getmtime(_p('b621_rows.json')) <= os.path.getmtime(os.path.join(PP, *p.split('/'))) for p in EDITIONS if os.path.exists(os.path.join(PP, *p.split('/'))))
    pc = _pp_commits()
    ed_commits = {p: [h for h, s in pc if _files(h) == [p]] for p in EDITIONS}
    s2 = all(len(v) == 1 for v in ed_commits.values())
    s3_syn = {k: H[k].get('repin') for k in EDITED}
    s3 = bool(re.search(r'RE-PIN : (\d+) of \1 citations hold', rep_m)) and all(v and v[0] == v[1] for v in s3_syn.values())
    pg_commits = {x.get('page'): [h for h, s in pc if _files(h) == [x.get('page')]] for x in (Z, X) if x.get('changed')}
    s4 = Z.get('rc') == 0 and X.get('rc') == 0 and all(len(v) == 1 for v in pg_commits.values())
    S = {
        'H55a': (RJ['H55a'], 'of the six kernel-verified rows %d stand with the terminal`s statement carrying the claim (bound four): %s' % (
            RJ['kv_stand'], [(x['id'], x['claim'], x['verdict']) for x in RJ['kv']])),
        'H55b': (('HOLDS' if h55b else 'REFUTED'), 'the tier line of each edited synthesis unchanged %s; the syntheses no row of which moves, no '
                 'edition %s' % (tiers, untouched)),
        'H55c': (H['mono'].get('H55c', 'REFUTED'), 'the monograph`s residue sentences at the ceiling %s items (%s distinct sentences rewritten, one '
                 'item by the history line), the scanner %s with %s unexcepted' % (H['mono'].get('n_items'), H['mono'].get('m_sentences'),
                                                                                  'CLEAN' if H['mono'].get('clean') else 'NOT CLEAN', H['mono'].get('unexcepted'))),
        'H55d': (('HOLDS' if h28_all else 'REFUTED'), 'H28a-H28c per edition: %s' % h28s),
        'N1': (('HELD' if RJ['kv_stand'] >= 4 else 'REFUTED'), 'kernel-verified rows standing on their terminals` statements %d of 6' % RJ['kv_stand']),
        'N2': (('HELD' if h55b else 'REFUTED'), 'the tiers %s; untouched %s' % (tiers, untouched)),
        'N3': (('HELD' if H['mono'].get('H55c') == 'HOLDS' else 'REFUTED'), 'the monograph`s residue sentences at the ceiling %s (bound ten), v5.18 '
               'scans %s with %s unexcepted' % (H['mono'].get('n_items'), 'CLEAN' if H['mono'].get('clean') else 'NOT CLEAN', H['mono'].get('unexcepted'))),
        'N4': (('HELD' if h28_all and held else 'REFUTED'), 'H28a-H28c %s; no sentence held %s' % (h28s, held)),
        'N5': n5v,
        'S1': (('HELD' if s1 else 'REFUTED'), 'the rows bank at %s, before every edition (stamps %s; file times checked)' % (RJ.get('at'), ed_at)),
        'S2': (('HELD' if s2 else 'REFUTED'), 'each edition committed alone in PLACE-papers: %s' % ed_commits),
        'S3': (('HELD' if s3 else 'REFUTED'), 'the re-pin: the monograph %s ; the syntheses %s' % (
            ([l for l in rep_m.split(NL) if 'RE-PIN :' in l] or ['none'])[0].strip(), s3_syn)),
        'S4': (('HELD' if s4 else 'REFUTED'), 'the ζ page exit %s changed %s, the χ page exit %s changed %s; each changed page committed alone %s' % (
            Z.get('rc'), Z.get('changed'), X.get('rc'), X.get('changed'), pg_commits)),
        'S5': (('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED'),
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b621_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


def _title_entry():
    RJ, RS = jl('b621_rows.json'), jl('b621_residue.json')
    docs = sorted(set(r[1] for r in K.REGRADES))
    return ('## The second reader’s disagreements applied: the monograph at v5.18 with the enumeration sentence at the ceiling and %d residue '
            'items read down in %d sentences; %d synthesis rows re-graded across %d documents, %d kernel-verified rows standing on their '
            'terminals’ statements; the form amended' % (len(RS['m_items']), RS['m_sentences'], RJ['regraded'], len(docs), RJ['kv_stand']))


TRAIL_HEAD = ('### b621 — lane three, act forty-eight under (R231): the second reader’s disagreements ruled by class and applied -- the monograph '
              'at v5.18, the syntheses re-graded where the reader was right, the form amended to show the reader what the seat graded')
FOR_AUTHOR = ('(1) the order of the grades for “the lower grade” is the grading rule’s own as the syntheses print it (kernel-verified, '
              'theorem-supported, computationally-verified, argument-supported, synthesis-suggested, statement-grade); it decides one row, R088, '
              'where the seat’s argument-supported keeps; (2) “a cited line the packet omitted” read as a line the row cites in any of its '
              'cells, its paper:line cell or its backing cell, which the packet did not print; the seat names it only where the line carries '
              'the higher grade by the grading rule, and four rows whose omitted lines do not (R012, R042, R103, R110) move; (3) the ferry’s '
              'v5.17 “:1217” is v5.16’s line, the sentence at v5.17 :1218, the navigator’s; (4) a residue item quoting a window takes the '
              'ceiling on the sentence its reason names, and on the one the reader’s line names where that is another; (5) the restatement '
              'clause read as reaching every unmarked body sentence restating a ruled claim, eight needles over the body, every hit read by hand, '
              '30 sentences rewritten and the rest carried each with its reason; (6) the dated block of 2026-08-14 is one paragraph, its history '
              'line beneath it answering :2234 and the two restating sentences beside it; (7) YM-20’s retirement line placed at its own pin, '
              'a27415d, by the fact clause; (8) 2B and 2F take no next version, no row of either moving')


def _finding_text():
    S, rl, RJ, RS, SR = (jl(n) for n in ('b621_scores.json', 'b621_record_lines.json', 'b621_rows.json', 'b621_residue.json', 'b621_sieve_rate.json'))
    H = _h28_all()
    ME = jl('b621_mono_edition.json')
    t = _title_entry()
    pc = _pp_commits()
    ec = {p: ([h for h, s in pc if _files(h) == [p]] or ['?'])[0] for p in EDITIONS}
    e = ['', t, '',
         '*Filed at b621 on the author’s ruling `(R231)` and the author’s answer before the seal. Banks: relay `data/b621_rows.txt` (the rows '
         'and the residue), `data/b621_sieve_rate.txt`, `data/b621_edition_PLACE.txt` and one diff bank per synthesis, '
         '`data/b621_author_answers.txt`. Nothing deposits.*', '',
         '**The rows** (`(R231)`(3)(iii)), banked before any edition: the six kernel-verified rows each printed beside the terminal’s statement '
         'read at its pin, %d of 6 standing on it -- the four of Phase 1.2 on `Integration.lean`, Voice1 and the Spectral Cannon at SIDE-kernel '
         'v1.2, IR :300 and EA :540 naming the file the packet did not print; 2D’s two on SIDE-effects and SIDE-cosmo at their pins; of the '
         '46 others, %d stand on a line the row cites and the packet omitted, %d move to the reader’s lower grade, %d keep the seat’s grade, '
         'the lower; %d rows re-graded in %s.' % (RJ['kv_stand'], RJ['counts']['stands'], RJ['counts']['moves'], RJ['counts']['unchanged'],
                                                  RJ['regraded'], ', '.join('%s %d' % (k, v) for k, v in RJ['by_syn'].items() if v)), '',
         '**The residue** (`(R231)`(3)(iv) and the author’s answer, option 3: every sentence either reader read beyond the ceiling takes it at '
         'its document’s next edition): the monograph’s %d items at v5.18 -- %d distinct sentences rewritten, the dated block’s by a history '
         'line beneath it; the other documents’ %d sentences listed for their next editions on the trail record.' % (
             len(RS['m_items']), RS['m_sentences'], RS['n_other']), '',
         '**The editions.** `day1/A_Place_to_Stand_v5_18.md` beside v5.17 (%s, alone): the enumeration sentence at the ceiling, its compiled '
         'exclusions read as conditions on a real σ and the step to ξ’s zeros as the located clause (RH-60, :7210); %d changes in all, %d '
         'restating a ruled claim by the restatement clause, every survey hit read by hand; collisions by the precedence order; re-pin %s; '
         'the scanner %s, %d unexcepted. The syntheses at their next versions, each alone: %s; every tier line unmoved. The sieve’s rate '
         'without the five struck pairs %d of %d (%.3f) beside %d of %d (%.3f), no sieve edition.' % (
             ec[M18], len(ME['changes']), sum(1 for c in ME['changes'] if c['id'].startswith('P')),
             ([l.split('RE-PIN : ')[1].split(' citations')[0] for l in rd('b621_repin_mono.txt').split(NL) if 'RE-PIN : ' in l] or ['?'])[0],
             'CLEAN' if H['mono'].get('clean') else 'NOT CLEAN', H['mono'].get('unexcepted'),
             '; '.join('%s %s (%s)' % (k, K.NEXT[k][1], ec[K.NEXT[k][0]]) for k in EDITED),
             SR['recomputed'][0], SR['recomputed'][1], SR['recomputed'][2], SR['orig'][0], SR['orig'][1], SR['orig'][2]), '',
         '**The record lines.** b620’s weight with the reading of `(R231)`(2) at FINDINGS :%d; the form’s clause at OPEN_TRAILS :%d, addressed '
         'to :12212: the row sample carries the statement of any terminal a row names, printed at the pin without its grade; the bound for rows '
         '0.75.' % (rl['lines'][0]['line'], rl['lines'][1]['line']), '',
         '**For the next batch, the seat’s, offered beside the clause:** of the 31 rows the reader graded down that are not kernel-verified, '
         '16 stand on lines their own backing cells cite and the packet did not print; a sample carrying those lines beside the cited ones '
         'would give the reader what the seat graded there too.', '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it applies the second reader’s keying (:7422) and re-reads the needle’s reading '
         '(:7210) and the sieve’s RH-60 (:7186), whose rows the monograph’s new sentences cite; the monograph’s editions it extends are b606-b609’s '
         '(:7108, :7132, :7158, :7186); the syntheses it re-grades are b611’s, b612’s, b614’s and b616’s (:7240, :7260, :7300, :7346), the '
         'load-bearing clause b615’s (:7322). It '
         'strengthens the programme’s offering of editions whose sentences two readers have read against the ceiling, every disagreement '
         'ruled by the author and applied as an edition.', '',
         '**Next.** Per `(R231)`(6): b622, W-ORD-QUANTIFIER-COLUMN’s generator with DENSITY, the pages re-emitted and the sieve’s H marks '
         'replaced. The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; no current version edited; nothing here is a statement about RH, GRH or any zero beyond the '
         'compiled statements’ own words.*', '']
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
    put_json('b621_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl, RS, RJ = (jl(n) for n in ('b621_scores.json', 'b621_findings.json', 'b621_record_lines.json', 'b621_residue.json', 'b621_rows.json'))
    pc = _pp_commits()
    ec = {p: ([h for h, s in pc if _files(h) == [p]] or ['?'])[0] for p in EDITIONS}
    other = '; '.join('%s %s' % (doc, ', '.join(':%s' % ln for ln, _i, _h in sorted(v, key=lambda x: (x[0] or 0)))) for doc, v in sorted(RS['other'].items()))
    rows_ = ['', TRAIL_HEAD, '',
             '**(R231) ratified.** (1) b620 at its weight. (2) The reading of the result. (3) The disagreements ruled by class: the enumeration '
             'sentence at the ceiling; the five sieve v0.2 pairs struck and the rate recomputed; the rows by the terminal’s statement and the '
             'lower grade; the residue by its readings. (4) The form amended at :12212. (5) b621, the rulings applied as editions; H55a-H55d. '
             '(6) The act after: b622.', '',
             '**Entered:** FINDINGS.md:%d (b620’s weight and the reading), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the '
             'form’s clause, addressed to :12212); this record; the editions, each committed alone in PLACE-papers -- %s; relay data/b621_rows.txt, '
             'data/b621_sieve_rate.txt, data/b621_edition_PLACE.txt, data/b621_edition_P12.txt, data/b621_edition_15E.txt, '
             'data/b621_edition_2D.txt, data/b621_edition_2G.txt.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'],
                                                                       '; '.join('%s %s' % (p, ec[p]) for p in EDITIONS)), '',
             '**The author’s answer before the seal** (relay data/b621_author_answers.txt): every residue sentence either reader read beyond the '
             'ceiling takes it at its document’s next edition, the seat’s BEYOND kept meaning kept beyond; H55c and N3 scored on the 33.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**The residue sentences listed for their documents’ next editions** (`(R231)`(3)(iv) and the answer; %d sentences, none written in '
             'this act): %s.' % (RS['n_other'], other), '',
             '**Defects** (relay data/b621_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R231)`(6), b622, W-ORD-QUANTIFIER-COLUMN’s generator with DENSITY, the pages re-emitted and the sieve’s H marks '
             'replaced; the author rules on the closing.', '',
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
        print(e[:7000])
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b621_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b621_trail.json')['line'])


def desk(*a):
    S = jl('b621_scores.json')
    L = ['=' * 104, 'b621 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H55a-H55d, (R231)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H55 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b621_defects.txt').rstrip(NL).split(NL)
    put_txt('b621_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, RJ, RS = (jl(n) for n in ('b621_scores.json', 'b621_findings.json', 'b621_trail.json', 'b621_record_lines.json', 'b621_rows.json',
                                            'b621_residue.json'))
    Z, X = jl('b621_page_zeta.json'), jl('b621_page_chi.json')
    H = _h28_all()
    L = ['b621 -- THE COMPONENTS, BANKED UNDER (R231).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b620`s closing push-out relay %s ; push-b620* branches deleted by name '
         '(data/b621_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b621_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b620`s weight FINDINGS :%d ; the form`s clause OPEN_TRAILS :%d ; the sieve`s rate data/b621_sieve_rate.txt' % (
             rl['lines'][0]['line'], rl['lines'][1]['line']),
         '### COMPONENT 2 : the rows data/b621_rows.txt ; kernel-verified standing %d of 6 ; re-graded %d ; H55a %s' % (RJ['kv_stand'], RJ['regraded'], S['H55a'][0]),
         '### COMPONENT 3 : the residue in the same bank ; the monograph`s items %d ; the other documents` sentences listed %d' % (len(RS['m_items']), RS['n_other']),
         '### COMPONENT 4 : v5.18 data/b621_edition_PLACE.txt (H28a %s, H28b %s, H28c %s, H55c %s) ; the syntheses %s ; H55b %s, H55d %s' % (
             H['mono'].get('H28a'), H['mono'].get('H28b'), H['mono'].get('H28c'), S['H55c'][0],
             '; '.join('%s %s (%s)' % (k, K.NEXT[k][1], '/'.join(str(H[k].get(x)) for x in ('H28a', 'H28b', 'H28c'))) for k in EDITED), S['H55b'][0], S['H55d'][0]),
         '### COMPONENT 5 : the ζ page changed %s, the χ page changed %s ; page arms data/b621_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b622 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b621_components.txt', L)


def tiers_direct(*a):
    """### defect (a)'s direct test: every untouched synthesis's next version absent on disk, at HEAD and in the index; every edited one's
    ### tier line equal to its current one's. Writes data/b621_tiers_direct.txt."""
    L = ['b621 -- DEFECT (a)`S DIRECT TEST: THE TIER ARM`S CLAIM READ WITHOUT ITS PREDICATE (%s), PLACE-papers HEAD %s' % (
        utc(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip()), '']
    ok = True
    for k in K.SYN:
        p = K.NEXT[k][0]
        disk = os.path.exists(os.path.join(PP, *p.split('/')))
        head = _show(PP, 'HEAD', p)
        idx = g(PP, 'ls-files', '--', p).strip()
        if k in EDITED:
            t0, t1 = lines_of(_show(PP, PRE_PP, K.SYN[k]))[2], lines_of(head or '')[2] if head else ''
            good = disk and head is not None and t0 == t1
            L.append('  %-4s %s -- on disk %s, at HEAD %s, tracked %s ; its tier line equal to the current one`s %s' % (k, p, disk, head is not None,
                                                                                                                bool(idx), t0 == t1))
        else:
            good = not disk and head is None and not idx
            L.append('  %-4s %s -- on disk %s, at HEAD %s, tracked %s (no row of it moves: no next version)' % (k, p, disk, head is not None, bool(idx)))
        ok = ok and good
    L += ['', '### ### **THE CLAIM %s: no next version for 2B or 2F, and every edited synthesis`s tier line unmoved.**' % ('HOLDS' if ok else 'FAILS')]
    put_txt('b621_tiers_direct.txt', L)
    print(L[-1])


CORR_HEAD = '*Appended 2026-10-04 by b621 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    """### OPEN_TRAILS: the record's defect line corrected, addressed to the record, appended at the end; `dry` prints it."""
    Q = R2._Q()
    rec = Q.line_of(Q.OT, TRAIL_HEAD)
    t = ('\n%s the record’s “Defects: none recorded” was written before the pre-push suite, which read 76 of 78 -- G-SYN-TIERS and '
         'G-H55B-SCORED failing in their letter on one predicate, which tests the next versions of 2B and 2F for absence by None where its '
         'sources hold an absent file as empty bytes. Tested directly, neither next version exists on disk, at HEAD or in the index, and every '
         'edited synthesis’s tier line equals its current one (relay data/b621_tiers_direct.txt), so H55b and N2 stand as scored. The sealed '
         'suite is not edited; the record tool took one edit after the seal to carry the defect, committed alone in relay (relay '
         'data/b621_defects.txt, defect (a)).\n' % (CORR_HEAD % rec))
    bad = ledger_check(t)
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(t)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec)
    r = Q.append_to(Q.OT, t)
    put_json('b621_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec), head=CORR_HEAD % rec, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b621_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
