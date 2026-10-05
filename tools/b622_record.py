# -*- coding: utf-8 -*-
"""b622_record.py -- THE ACT'S RECORD TOOL, UNDER (R232). ### ONE SUBCOMMAND PER BANK.

### ### b622: LANE THREE, ACT FORTY-NINE -- THE QUANTIFIER COLUMN: THE GENERATOR READING EACH NODE'S SHAPE FROM ITS LEAN STATEMENT, BOTH
### PAGES RE-EMITTED, THE SIEVE'S HAND MARKS REPLACED; README'S SUPPORTABLE SENTENCE FOR v0.17-v0.21; THE 39 OWED SENTENCES ENTERED AS
### WORK-LIST ITEMS.
### Subcommands write only `data/b622_*` unless the docstring names another file; `dry` on the command line routes every b622 bank, the
### work-list entries, README and the sieve's edition to the seat's scratchpad (for `findings` and `trail`, `dry` prints and appends
### nothing; `record_lines dry` prints the ledger lines without appending them). Banks are written by encode, temp file, `os.replace`;
### ledger appends through b566's guarded `append_to`. The data is tools/b622_worklist.py. No platform call. No Lean call: both pages are
### re-emitted from their banked probes. The generator's shape reader is tools/chain_page.py's own (`shape_of`, `node_column`), edited
### after the seal; the subcommands that read it run after that edit. The templates are tools/b621_record.py (the harness) and
### tools/b617_record.py (the sieve's edition). The N5 scorer takes the trail record's expected line (OPEN_TRAILS :12799).
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
import b622_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/37c7fa81-fdbc-49b5-acbe-57f6d60b97ad/scratchpad'
SESSION_ID = '37c7fa81-fdbc-49b5-acbe-57f6d60b97ad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
SESSION_FROM = 0     # ### this session opened on this act's ferry
GEN_FILES = ('tools/chain_page.py', 'tools/test_chain_page_b596.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b622_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b622_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def jx(name):
    return jl(name) if os.path.exists(_p(name)) else {}


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


def _cell(s):
    return R4._cell(_poss(s))


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


DEFECTS = []
DEFECT_SHORT = []
CORRECTION = ''
# ### b621's lesson (its defect (a)): a defect found after the seal is written by the seat into data/b622_defects.json (keys `defects`,
# ### `short`, `correction`), a bank of this act, and read here -- so carrying it needs no edit of this tool after the seal.
_DJ = os.path.join(D, 'b622_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b622 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b622_defects.txt', L)


# ================================================================================ READING (1): THE READS
def _stmt_reads():
    import chain_page as CP
    out = []
    for name, k, want, why in K.TEST_NODES:
        cells, _e = CP.parse(_rel(K.PROBE[k]))
        c = cells.get(name) or {}
        out.append('    %s (%s, the %s page`s banked probe relay data/%s @ %s): %s' % (name, why, k, K.PROBE[k], PRE_RELAY, c.get('statement')))
        mod = (c.get('module') or '').replace('.', '/') + '.lean'
        tag = K.PIN[k][0]
        src = _show(K.KER, tag, mod)
        if src and c.get('line'):
            out.append('      %s @ %s = %s :%d  %s' % (mod, tag, K.PIN[k][1], c['line'], lines_of(src)[c['line'] - 1].strip()[:300]))
    return out


def READS():
    return [
        ('OPEN_TRAILS: the form, the precedence order, the work-order and the DENSITY line, b621`s clause, record and correction', PP, PRE_PP,
         'OPEN_TRAILS.md', [11864, 12228] + list(range(12266, 12297)) + list(range(12839, 12862)), 1700),
        ('relay tools/chain_page.py: the node reader, the backmatter channel, DECL and entry_tag, the emitters and the run', RELAY, PRE_RELAY,
         'tools/chain_page.py', list(range(112, 136)) + list(range(321, 343)) + list(range(465, 490)) + list(range(537, 559)) + list(range(637, 650)), 260),
        ('relay tools/test_chain_page_b596.py, whole', RELAY, PRE_RELAY, 'tools/test_chain_page_b596.py', ('ALL',), 260),
        ('the sieve v0.5: the version line, the shape column`s rule and every row`s shape cell', PP, PRE_PP, K.SV5,
         ('GREP', r'^\*v0\.5, |^- \*\*Shape\*\*|^\| [A-Z]{2}-\d\d \| '), 330),
        ('README: the ceiling sentence, the (R183)(3) paragraph and the deposit note', PP, PRE_PP, 'README.md', list(range(106, 112)) + [125, 154], 2200),
        ('the b558 work-lists` form: GRH_CASCADE`s list head and b603`s addendum beside BALANCE_AND_POSITIVITY`s', RELAY, PRE_RELAY,
         'data/b558_editions/GRH_CASCADE.txt', [1, 2, 3, 4, 5, 6, 7], 400),
        ('b603`s addendum form', RELAY, PRE_RELAY, 'data/b558_editions/BALANCE_AND_POSITIVITY_addendum.txt', ('ALL',), 400),
        ('relay data/b621_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b621_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE)'), 200),
    ]


def reads(*a):
    L = ['b622 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['### the five test nodes` statements, each as its page`s banked probe printed it, and its declaration line in the kernel at the pin']
    L += _stmt_reads()
    L += ['', '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                       g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b622_reads.txt', L)


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
    L = ['### b622 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b622_author_answers.txt', L)


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
    put_json('b622_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B621_ENTRY = '## The second reader’s disagreements applied: the monograph at v5.18'
B621_CLAUSE = '*Appended 2026-10-04 by b621 to W-ORD-SECOND-READER’s form (:12212), under `(R231)`(4) -- THE ROW SAMPLE CARRIES THE TERMINAL’S'
W_HEAD = '*Appended 2026-10-04 by b622 to b621’s entry (:%d), under `(R232)`(1) -- b621 AT ITS WEIGHT, AND THE CONFIRMATIONS:*'
O_HEAD = '*Appended 2026-10-04 by b622 to the form’s clause (:%d), under `(R232)`(1) -- THE OFFER TAKEN, THE BACKING CELL’S LINES:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _weight(entry, offer_line):
    S = {k: v[0] for k, v in json.loads(_rel('b621_scores.json')).items()}
    ME, RJ, RS, SR = (json.loads(_rel(n)) for n in ('b621_mono_edition.json', 'b621_rows.json', 'b621_residue.json', 'b621_sieve_rate.json'))
    RL, FJ, TJ, CJ = (json.loads(_rel(n)) for n in ('b621_record_lines.json', 'b621_findings.json', 'b621_trail.json', 'b621_correction.json'))
    pre, post = (_count_bank(_rel(n)) for n in ('b621_checks.txt', 'b621_checks_postpush.txt'))
    rep = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', _rel('b621_repin_mono.txt'))
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    return ('\n%s A_Place_to_Stand v5.18 beside v5.17 unedited (PLACE-papers cc22481): the enumeration sentence at v5.17 :1218 (the '
            'ferry’s “:1217” v5.16’s line, the navigator’s) rewritten to say each class’s compiled exclusion is a condition on a real σ and '
            'the step from the classes to ξ’s zeros is the located clause, open, citing RH-60 and FINDINGS :7210; the %d residue items in %d '
            'sentences, :2234 by a history line under its dated block; %d further unmarked restatements by the restatement clause, each survey '
            'hit left standing given a reason in the rows bank; %d changes, no sentence-count drift, re-pin %s of %s, the scanner CLEAN at 0 '
            'unexcepted. The rows (relay data/b621_rows.txt): %d of the six kernel-verified rows standing on their terminals’ statements at the '
            'pins (IR :300 and EA :540 naming Integration.lean lines the packet did not print); of the 46 others, %d standing on lines their '
            'backing cells cite, %d moving to the reader’s grade, %d keeping the seat’s as already the lower; four syntheses at their next '
            'versions (Phase 1.2 v0.2, 1.5E v0.2, 2D v0.3, 2G v0.2), no tier moved, 2B and 2F untouched; one fact correction (YM-20’s '
            'retirement line at a27415d, not c66f3c5). The sieve’s rate %d of %d with the five pairs struck, beside %d of %d as keyed. '
            'H55a-H55d %s; N1-N5 and S1-S5 %s. FINDINGS :%d, :%d; OPEN_TRAILS :%d (the form’s clause), :%d (the record), :%d (the correction '
            'line). Relay 02fba720; PLACE-papers f695c98. The suite %d of %d before the push and %d of %d after it -- G-SYN-TIERS and '
            'G-H55B-SCORED failing on one sealed-suite defect, a missing file read as empty bytes against a None test, the claim tested '
            'directly and holding (relay data/b621_tiers_direct.txt), the sealed suite unedited, the record tool’s one edit after the seal '
            'refuting the face’s sentence in its letter -- the seat’s defect (a), repaired in b622’s suite sources. **Confirmed, `(R232)`(1):** '
            'the grades ordered as the grading rule prints them; “a cited line the packet omitted” includes the lines a row’s backing cell '
            'cites; the offer taken -- the next batch’s row sample carries the backing cell’s cited lines beside the terminal statements '
            '(OPEN_TRAILS :%d, appended to the :%d clause). Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, len(RS['m_items']), RS['m_sentences'], sum(1 for c in ME['changes'] if c['id'].startswith('P')), len(ME['changes']),
                rep.group(1), rep.group(2), RJ['kv_stand'], RJ['counts']['stands'], RJ['counts']['moves'], RJ['counts']['unchanged'],
                SR['recomputed'][0], SR['recomputed'][1], SR['orig'][0], SR['orig'][1],
                'HOLD' if all(S[k] == 'HOLDS' for k in ('H55a', 'H55b', 'H55c', 'H55d')) else str([S[k] for k in ('H55a', 'H55b', 'H55c', 'H55d')]),
                allh(('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), RL['lines'][0]['line'], FJ['entry_line'],
                RL['lines'][1]['line'], TJ['line'], CJ['line'], pre[0], pre[1], post[0], post[1], offer_line, RL['lines'][1]['line']))


def _offer(clause_line):
    return ('\n%s the next batch’s synthesis-row sample carries, beside the paper’s cited lines and the statement of any terminal the row '
            'names, the lines the row’s backing cell cites, each printed at its pin without its grade, so the reader is given what the seat '
            'graded there too; offered by b621 beside its clause (FINDINGS :7442), taken by the author (`(R232)`(1)).\n' % (O_HEAD % clause_line))


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
    p = os.path.join(SP if DRY else D, 'b622_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def record_lines(*a):
    """### FINDINGS: b621's weight with the confirmations, addressed to b621's entry; OPEN_TRAILS: the offer taken, addressed to the form's
    ### clause (:12839). The OPEN_TRAILS line is computed first (its line count + 2) so the weight cites it, and checked after."""
    Q = R2._Q()
    entry, cl = Q.line_of(Q.FIND, B621_ENTRY), Q.line_of(Q.OT, B621_CLAUSE)
    if entry != 7442 or cl != 12839:
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s) -- NOTHING WRITTEN' % (entry, cl))
    ot_n = len(lines_of(io.open(Q.OT, encoding='utf-8').read())) + 2
    of, wt = _offer(cl), _weight(entry, ot_n)
    bad = ledger_check(wt, of)
    nd, _n = _nd(wt + of)
    sc, clean = _scan_text(wt + of, 'lines')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s ; the offer expected at :%d' % (
        bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ot_n))
    if DRY:
        print(wt)
        print(of)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    Q.guard_absent(Q.OT, O_HEAD % cl)
    r2 = Q.append_to(Q.OT, of)
    if Q.line_of(Q.OT, O_HEAD % cl) != ot_n:
        sys.exit('### THE OFFER LANDED AT :%s, NOT :%d -- FINDINGS NOT APPENDED' % (Q.line_of(Q.OT, O_HEAD % cl), ot_n))
    r1 = Q.append_to(Q.FIND, wt)
    out = [dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r1),
           dict(file='OPEN_TRAILS.md', head=O_HEAD % cl, line=Q.line_of(Q.OT, O_HEAD % cl), append=r2)]
    put_json('b622_record_lines.json', dict(entry=entry, clause=cl, lines=out, at=utc()))
    print('  FINDINGS.md :%s ; OPEN_TRAILS.md :%s' % (out[0]['line'], out[1]['line']))


# ================================================================================ COMPONENT 1: THE 39 SENTENCES ENTERED
def _wl_item(x):
    rr = ('both readers read it BEYOND the ceiling -- the seat (relay data/%s :%d: %s) and the second reader (its line: “%s”)' % (
        x['bank'], x['bank_line'], x['reason'], x['reader_line']) if x['both'] else
          'the seat read it BEYOND the ceiling (relay data/%s :%d: %s), the second reader %s (its line: “%s”)' % (
              x['bank'], x['bank_line'], x['reason'], x['reader'], x['reader_line']))
    return [':%d -- CEILING ITEM (%s)' % (x['line'], x['id']),
            '    the sentence: "%s"' % x['sentence'],
            '    the readings: %s -- relay data/b620_key.json and data/b620_reader_answers.txt' % rr,
            '    what the next edition does: takes the ceiling clause on this sentence (%s), by the author`s answer before b621`s seal (relay '
            'data/b621_author_answers.txt): every sentence either reader read beyond the ceiling takes it at its document`s next edition' % K.CEILING_REF,
            '    informing act: b621 (R231)(3)(iv); routed by (R232)(2)', '']


def _wl_texts():
    items = K.residue_items()
    by = {}
    for x in items:
        by.setdefault(x['doc'], []).append(x)
    out = {}
    for doc, xs in sorted(by.items()):
        fn, kind = K.WL_FILES[doc]
        xs = sorted(xs, key=lambda y: y['line'])
        body = []
        for x in xs:
            body += _wl_item(x)
        tail = ['### %d ceiling item%s (%d distinct line%s).' % (len(xs), '' if len(xs) == 1 else 's', len(set(y['line'] for y in xs)),
                                                                 '' if len(set(y['line'] for y in xs)) == 1 else 's')]
        if kind == 'list':
            head = ['', K.WL_SECTION, '', '### the residue sentences of b621`s record (OPEN_TRAILS :12851) in this document, entered so its next '
                    'edition takes them without a new reading (R232)(2); the lines are those of `%s` at PLACE-papers %s, the document`s '
                    'current edition; the row`s form is b558`s, its terminal cell the item`s id.' % (doc, PRE_PP), '']
        else:
            head = ['b622 -- THE %s WORK-LIST ADDENDUM, CEILING ITEMS FOR ITS NEXT EDITION (under (R232)(2); the document `%s` has no b558 '
                    'work-list; an input to its next edition, not an edition)' % (os.path.basename(doc)[:-3], doc), '',
                    '### the row`s form is b558`s: the line, the item, the sentence quoted, the readings, what the next edition does, the '
                    'informing act; the lines are those of `%s` at PLACE-papers %s.' % (doc, PRE_PP), '']
        out[doc] = (fn, kind, xs, head + body + tail)
    return out, items


def worklists(*a):
    """### data/b558_editions/: each of the seven work-lists gains one dated section appended; seven addendum files are created beside
    ### them. Then data/b622_worklists.txt and its json. `dry` writes every file to the scratchpad instead."""
    T, items = _wl_texts()
    if len(items) != 39 or len(T) != 14:
        sys.exit('### THE ITEMS DO NOT RESOLVE (%d items, %d documents) -- NOTHING WRITTEN' % (len(items), len(T)))
    bad = []
    for doc, (fn, kind, xs, L) in T.items():
        src = lines_of(_show(PP, PRE_PP, doc))
        bad += [(doc, x['line']) for x in xs if x['sentence'] not in src[x['line'] - 1]]
    if bad:
        sys.exit('### SENTENCES NOT ON THEIR LINES %s -- NOTHING WRITTEN' % bad)
    rows, B = [], ['b622 -- COMPONENT 1: THE 39 OWED SENTENCES ENTERED, (R232)(2), %s' % utc(), '',
                   '### each sentence of OPEN_TRAILS :12851 checked on its line at PLACE-papers %s before it was entered: 39 of 39' % PRE_PP, '']
    for doc, (fn, kind, xs, L) in sorted(T.items()):
        dest = os.path.join(SP if DRY else os.path.join(D, K.WL_DIR), fn)
        text = (NL.join(L) + NL).encode('utf-8')
        if kind == 'list':
            src = os.path.join(D, K.WL_DIR, fn)
            before = open(src, 'rb').read()
            if before != (_show(RELAY, PRE_RELAY, 'data/%s/%s' % (K.WL_DIR, fn)) or '').encode('utf-8'):
                sys.exit('### %s MOVED SINCE %s -- NOTHING MORE WRITTEN' % (fn, PRE_RELAY))
            if not before.endswith(b'\n'):
                sys.exit('### %s DOES NOT END IN A NEWLINE -- NOTHING MORE WRITTEN' % fn)
            new = before + text
        else:
            if not DRY and os.path.exists(dest):
                sys.exit('### %s EXISTS -- NOTHING MORE WRITTEN' % fn)
            before, new = b'', text
        _write(dest, new)
        rows.append(dict(doc=doc, file='data/%s/%s' % (K.WL_DIR, fn), kind=kind, before=len(before), after=len(new), sha256=sha(new),
                         items=[dict(id=x['id'], line=x['line']) for x in xs]))
        B.append('  %-8s data/%s/%s -- %d item(s) %s ; bytes %d -> %d ; sha256 %s' % (kind, K.WL_DIR, fn, len(xs),
                                                                                  ', '.join(':%d %s' % (x['line'], x['id']) for x in xs),
                                                                                  len(before), len(new), sha(new)[:16]))
    B += ['', '### ### **ENTERED : %d items in %d files (%d work-lists appended, %d addenda created).**' % (
        sum(len(r['items']) for r in rows), len(rows), sum(1 for r in rows if r['kind'] == 'list'), sum(1 for r in rows if r['kind'] == 'addendum'))]
    put_txt('b622_worklists.txt', B)
    put_json('b622_worklists.json', dict(at=utc(), dry=DRY, files=rows, n_items=sum(len(r['items']) for r in rows)))
    print(B[-1])


# ================================================================================ COMPONENT 1: README
def readme_text(pre):
    """### README after the append: the paragraph beside the (R183)(3) sentence, one blank line between, and the deposit note's live-line
    ### sentence refreshed; every other byte as it stands."""
    ls = pre.split(NL)
    at = [i for i, l in enumerate(ls) if l.startswith(K.R183_MARK)]
    if len(at) != 1 or pre.count(K.DEPOSIT_OLD) != 1:
        return None, at
    new = ls[:at[0] + 1] + ['', K.README_PARA] + ls[at[0] + 1:]
    return NL.join(new).replace(K.DEPOSIT_OLD, K.DEPOSIT_NEW), at


def readme(*a):
    """### PLACE-papers README.md: the dated append and the live-line refresh of (R232)(3); the scanner on the result, banked as
    ### data/b622_readme_termscan.txt; data/b622_readme.json. `dry` writes the result to the scratchpad instead."""
    pre = _show(PP, PRE_PP, 'README.md')
    disk = io.open(os.path.join(PP, 'README.md'), encoding='utf-8').read()
    if disk != pre or _show(PP, 'HEAD', 'README.md') != pre:
        sys.exit('### README MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    new, at = readme_text(pre)
    if new is None:
        sys.exit('### THE ANCHORS DO NOT RESOLVE ONCE (%s) -- NOTHING WRITTEN' % at)
    dest = os.path.join(SP, 'README_dry.md') if DRY else os.path.join(PP, 'README.md')
    b = new.encode('utf-8')
    _write(dest, b)
    out = _scan(dest)
    put_txt('b622_readme_termscan.txt', out.rstrip(NL).split(NL))
    nl = new.split(NL)
    para = nl.index(K.README_PARA) + 1
    dep = [i + 1 for i, l in enumerate(nl) if K.DEPOSIT_NEW in l]
    dl = [x for x in difflib.unified_diff(pre.split(NL), nl, 'README.md@%s' % PRE_PP, 'README.md', lineterm='', n=0)]
    put_json('b622_readme.json', dict(at=utc(), dry=DRY, sha256=sha(b), bytes=len(b), r183=at[0] + 1, para=para, deposit=dep, diff=dl,
                                      clean=_clean(out), segs_para=len(_segs(K.README_PARA))))
    print('  README: the (R183)(3) line :%d ; the paragraph :%d ; the deposit note :%s ; scanner %s ; diff lines %d' % (
        at[0] + 1, para, dep, 'CLEAN' if _clean(out) else 'NOT CLEAN', len(dl)))


# ================================================================================ COMPONENT 2: THE GENERATOR
def gen_diff(*a):
    """### the generator edit and its test, printed as their diff against relay PRE_RELAY (data/b622_gen_diff.txt)."""
    d = g(RELAY, 'diff', PRE_RELAY, '--', *GEN_FILES)
    st = g(RELAY, 'diff', '--stat', PRE_RELAY, '--', *GEN_FILES)
    L = ['b622 -- COMPONENT 2: THE GENERATOR EDIT AND ITS TEST, THE DIFF AGAINST relay %s (%s)' % (PRE_RELAY, utc()), '',
         '### ' + (st.strip().split(NL)[-1] if st.strip() else 'NO DIFF'), ''] + d.rstrip(NL).split(NL)
    put_txt('b622_gen_diff.txt', L)
    print(L[2])


def gen_test(*a):
    """### the extended test run and counted (data/b622_gen_test.txt), and H56a scored on its own reads (data/b622_h56a.json)."""
    import chain_page as CP
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_chain_page_b596.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    cases = [l for l in out.split(NL) if re.search(r' (PASS|FAIL)$', l)]
    reads_ = []
    for name, k, want, why in K.TEST_NODES:
        cells, _e = CP.parse(io.open(os.path.join(D, K.PROBE[k]), encoding='utf-8').read().replace(chr(13), ''))
        got = CP.shape_of(name, cells)
        reads_.append(dict(name=name, page=k, want=want, got=got, ok=got == want, why=why))
    h56a = 'HOLDS' if all(x['ok'] for x in reads_) else 'REFUTED'
    L = ['b622 -- COMPONENT 2: THE TEST OF THE GENERATOR`S SHAPE READER, RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), '']
    L += out.rstrip(NL).split(NL)
    L += ['', '### CASES : %d ; PASSING : %d ; FAILING : %d' % (len(cases), sum(1 for c in cases if c.endswith(' PASS')),
                                                              sum(1 for c in cases if c.endswith(' FAIL'))), '',
          '### THE FIVE TEST NODES, READ BY tools/chain_page.py`s shape_of FROM THEIR PAGES` BANKED PROBES:']
    L += ['  %-66s %-5s want %-10s read %-12s %s' % (x['name'], x['page'], x['want'], x['got'], 'AS EXPECTED' if x['ok'] else '### DIFFERS')
          for x in reads_]
    L += ['', '### ### **H56a %s -- the five test nodes read as expected: %d of 5.**' % (h56a, sum(x['ok'] for x in reads_))]
    put_txt('b622_gen_test.txt', L)
    put_json('b622_h56a.json', dict(at=utc(), H56a=h56a, reads=reads_, rc=r.returncode, cases=len(cases),
                                    passing=sum(1 for c in cases if c.endswith(' PASS'))))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE PAGES
def nodes(*a):
    """### data/b622_nodes_zeta.txt and data/b622_nodes_chi.txt: b602's and b603's lists as committed at relay PRE_RELAY, every line kept,
    ### a head and the column's line added."""
    for k in ('zeta', 'chi'):
        src = _rel(K.OLD_NODES[k])
        if not src or src != io.open(os.path.join(D, K.OLD_NODES[k]), encoding='utf-8').read().replace(chr(13), ''):
            sys.exit('### %s DOES NOT RESOLVE AT %s -- NOTHING WRITTEN' % (K.OLD_NODES[k], PRE_RELAY))
        p = _p(K.NODES[k])
        if not DRY and os.path.exists(p):
            sys.exit('### %s EXISTS -- NOTHING WRITTEN' % K.NODES[k])
        text = NL.join(K.LIST_HEAD[k]) + NL + src.rstrip(NL) + NL + K.COLUMN_MARK + NL
        _write(p, text.encode('utf-8'))
        print('  written: %s (%d lines)' % (K.NODES[k], len(text.split(NL)) - 1))


def page(k, tag, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe through this act's list; writes the page only when it
    ### changed; banks data/b622_page_<k>_<tag>.json with every node's shape and the UNCLASSIFIED nodes."""
    import chain_page as CP
    if k not in K.NODES or tag not in ('c3', 'c4'):
        sys.exit('usage: page zeta|chi c3|c4')
    pdir = os.path.join(SP, '_b622_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(_p(K.NODES[k]), pdir, os.path.join(D, K.PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b622_page_%s_%s.json' % (k, tag), dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    elif DRY:
        _write(os.path.join(SP, 'page_%s_%s_dry.md' % (k, tag)), b)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    shapes = {n: meta['cells'][n].get('shape') for n in meta['order']}
    unc = [n for n, s in shapes.items() if s == 'UNCLASSIFIED']
    objs = [n for n, s in shapes.items() if s == '—']
    put_json('b622_page_%s_%s.json' % (k, tag), dict(page=K.PNAME[k], nodes=K.NODES[k], probe=K.PROBE[k], rc=rc, bytes=len(b), sha256=sha(b),
                                                     changed=changed, diff=dl, shapes=shapes, unclassified=unc, objects=objs, dry=DRY,
                                                     at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s ; diff lines %d ; nodes %d ; UNCLASSIFIED %d %s ; objects %d' % (
        k, tag, rc, len(b), changed, secs, len(dl), len(shapes), len(unc), unc, len(objs)))


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b622 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b622_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b622_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


def unclassified(*a):
    """### data/b622_unclassified.txt: every node the reader prints UNCLASSIFIED, its statement, the definitions its fields name read in the
    ### kernel at the page's pin, and the seat's proposal under the author's reading before the seal -- for the author's ruling."""
    import chain_page as CP
    Z, X = jl('b622_page_zeta_c3.json'), jl('b622_page_chi_c3.json')
    unc = [(n, 'zeta') for n in Z['unclassified']] + [(n, 'chi') for n in X['unclassified']]
    L = ['b622 -- THE NODES THE READER PRINTS UNCLASSIFIED, FOR THE AUTHOR`S RULING (%s)' % utc(), '',
         '### the author`s reading before the seal (relay data/b622_author_answers.txt): a premise bundle prints the shape of its strongest '
         'field; the seat prints a proposal by that reading, each field read in the kernel at the page`s pin by the reader`s own rules.', '']
    props = {}
    for n, k in unc:
        cells, _e = CP.parse(_rel(K.PROBE[k]))
        tag, pin = K.PIN[k]
        L.append('### %s (the %s page, %s = %s)' % (n, k, tag, pin))
        L.append('    the statement as the probe printed it: %s' % cells[n]['statement'][:900])
        fields = []
        for path, dn in K.UNCLASSIFIED_READ.get(n, ('', []))[1]:
            src = lines_of(_show(K.KER, tag, path))
            i = next((j for j, l in enumerate(src) if re.match(r'^(noncomputable )?def %s\b' % re.escape(dn), l)), None)
            if i is None:
                L.append('    %s : ### NO SUCH DECLARATION in %s at %s' % (dn, path, tag))
                fields.append(None)
                continue
            body = []
            for l in src[i:]:
                if body and (not l.strip() or l.startswith('/-') or l.startswith('def ') or l.startswith('theorem ')):
                    break
                body.append(l)
            txt = ' '.join(' '.join(body).split())
            prop = re.sub(r'^def \S+(?: \([^()]*\))* : Prop := ', '', txt)
            s = CP._read(prop, {}, {}, {}, set(), 0)
            fields.append(s)
            L.append('    %s @ %s %s :%d -- %s' % (dn, tag, path, i + 1, txt[:600]))
            L.append('        read by the reader`s rules: %s' % (s or 'nothing read'))
        top = CP._top(fields)
        props[n] = top or 'UNCLASSIFIED'
        L += ['    ### THE SEAT`S PROPOSAL: %s -- the strongest field`s shape (%s).' % (props[n], ', '.join(str(f) for f in fields)), '']
    L.append('### ### **UNCLASSIFIED : %d ; PROPOSED : %s.**' % (len(unc), props))
    put_txt('b622_unclassified.txt', L)
    put_json('b622_unclassified.json', dict(at=utc(), nodes=[n for n, _k in unc], proposals=props))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE SIEVE AT v0.6
def _page_nodes(tag='c3'):
    """### short name -> (page, full name, the generator's shape), the ζ page read first."""
    out = {}
    for k in ('zeta', 'chi'):
        P = jl('b622_page_%s_%s.json' % (k, tag))
        for n, s in P['shapes'].items():
            out.setdefault(n.split('.')[-1], (k, n, s))
    return out


def _shape_rows(S5, pn):
    """### every body row naming a page node by its compiled-face column: (line, id, its first page-node declaration, page, full name,
    ### the hand read, the generator's)."""
    rows = []
    for i, rid, c in K.body_rows(S5):
        hit = [x for x in K.faces_of(c) if x.split('.')[-1] in pn]
        if not hit:
            continue
        k, full, s = pn[hit[0].split('.')[-1]]
        hand = c[2]
        rows.append(dict(line=i, id=rid, decl=hit[0], page=k, node=full, hand=hand, gen=s, new_cell='%s %s' % (s, K.MARK_G),
                         same=hand == '%s %s' % (s, K.MARK_H)))
    return rows


def sieve_shapes(*a):
    """### data/b622_sieve_shapes.txt and its json, before the edition: every sieve row naming a page node with its hand read and the
    ### generator's, the differences listed."""
    S5 = lines_of(_show(PP, PRE_PP, K.SV5))
    rows = _shape_rows(S5, _page_nodes())
    allrows = K.body_rows(S5)
    diff = [r for r in rows if not r['same']]
    L = ['b622 -- COMPONENT 4: THE SIEVE`S ROWS NAMING A PAGE NODE, THE HAND READ BESIDE THE GENERATOR`S (%s)' % utc(), '',
         '### the sieve v0.5 @ PLACE-papers %s: %d body rows; %d name a node of the ζ or the χ page by their compiled-face column; %d name none '
         'and keep their hand mark' % (PRE_PP, len(allrows), len(rows), len(allrows) - len(rows)), '']
    L += ['  %-6s :%-4d %-42s %-4s hand %-16s generator %-14s %s' % (r['id'], r['line'], r['decl'][:42], r['page'], r['hand'], r['gen'],
                                                                     'AGREES' if r['same'] else '### DIFFERS') for r in rows]
    L += ['', '### THE DIFFERENCES (%d):' % len(diff)]
    L += ['  %s :%d -- %s -- hand %s ; generator %s' % (r['id'], r['line'], r['node'], r['hand'], r['gen']) for r in diff] or ['  none']
    L += ['', '### ### **ROWS NAMING A PAGE NODE : %d ; AS HAND-READ : %d ; DIFFERING : %d.**' % (len(rows), len(rows) - len(diff), len(diff))]
    put_txt('b622_sieve_shapes.txt', L)
    put_json('b622_sieve_shapes.json', dict(at=utc(), rows=rows, n_rows=len(allrows), diff=[r['id'] for r in diff]))
    print(L[-1])


def _map(n):
    return n + 2 if n >= 3 else n


SEC_TAGS = (('v0.2', R4.BM_TAG), ('v0.3', K.B605_TAG), ('v0.4', K.B609_TAG), ('v0.5', K.B617_TAG))


def _sec(n, S5):
    sec = None
    for name, tag in SEC_TAGS:
        if n >= S5.index(tag) + 1:
            sec = name
    return sec


def _repin(l, sec):
    """### a carried back-matter line, its own-line cells mapped to this file (b617's patterns for v0.2-v0.4, and v0.5's own);
    ### returns (line, [(old, new)])."""
    subs = []

    def f(m):
        o = int(m.group(2))
        subs.append((o, _map(o)))
        return m.group(1) + str(_map(o)) + m.group(3)
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \(:)(\d+)(\) \|)', f, l)
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \| :)(\d+)( \|)', f, l2)
    if sec in ('v0.3', 'v0.4', 'v0.5'):
        l2 = re.sub(r'^(\| :)(\d+)( \| )', f, l2)
    if sec == 'v0.3':
        l2 = re.sub(r'(the clause’s one verdict \(:)(\d+)(\))', f, l2)
    if sec in ('v0.4', 'v0.5'):
        l2 = re.sub(r'(\(:)(\d+)(\))', f, l2)
    if sec == 'v0.5':
        l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \| [A-Z]{2}-\d\d \| :)(\d+)( \|)', f, l2)
        l2 = re.sub(r'(RH-60 at :)(\d+)(\))', f, l2)
    return l2, subs


def _left(l):
    """### every `:n` token a back-matter line keeps after its re-pin, for the audit."""
    return re.findall(r'(?<![\w.]):(\d+)', l)


def sieve_edition(*a):
    """### PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md beside v0.5 (unedited), from v0.5's blob at PRE_PP by line
    ### transforms (carry / rewrite / insert / re-pin); the re-pin step last (`sieve_repin`). Writes the edition and
    ### data/b622_sieve_edition.json; `dry` writes both to the scratchpad instead."""
    S5 = lines_of(_show(PP, PRE_PP, K.SV5))
    if g(PP, 'rev-parse', 'HEAD:' + K.SV5).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.SV5)).strip():
        sys.exit('### v0.5 MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    SJ = jx('b622_sieve_shapes.json')
    if not SJ:
        sys.exit('### THE SHAPES ARE NOT BANKED -- NOTHING WRITTEN')
    dest = os.path.join(SP, 'b622_sieve_dry.md') if DRY else os.path.join(PP, *K.SV6.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    rows = {r['line']: r for r in SJ['rows']}
    diff = [r for r in SJ['rows'] if not r['same']]
    ver = K.VERSION6 % (len(SJ['rows']), len(SJ['rows']) - len(diff), len(diff), ', '.join('%s %s' % (r['id'], r['gen']) for r in diff) or 'none')
    shape_at = [i + 1 for i, l in enumerate(S5) if l == K.SHAPE_OLD]
    if len(shape_at) != 1:
        sys.exit('### THE SHAPE RULE IS NOT ONE LINE (%s) -- NOTHING WRITTEN' % shape_at)
    i604 = S5.index(R4.BM_TAG) + 1
    E, rewd, ins, rep, audit = [], [], [], [], []
    for n in range(1, len(S5) + 1):
        l = S5[n - 1]
        if n == 3:
            E.append(ver)
            ins.append(dict(v6=len(E), text=ver, what='the version line, above v0.5’s'))
            E.append('')
        if n == shape_at[0]:
            E.append(K.SHAPE_NEW)
            rewd.append(dict(v5=n, v6=len(E), old=l, new=K.SHAPE_NEW, frag_old=l, frag_new=K.SHAPE_NEW, what='the shape column’s rule, (R232)(4)'))
        elif n in rows:
            r = rows[n]
            c = K.cells_of(l)
            if c[0] != r['id'] or c[2] != r['hand']:
                sys.exit('### ROW %s AT :%d DOES NOT MATCH ITS BANK -- NOTHING WRITTEN' % (r['id'], n))
            old_cell = '| %s |' % c[2]
            if l.count(old_cell) != 1:
                sys.exit('### ROW %s`S SHAPE CELL IS NOT ONCE ON ITS LINE -- NOTHING WRITTEN' % r['id'])
            s = l.replace(old_cell, '| %s |' % r['new_cell'])
            E.append(s)
            rewd.append(dict(v5=n, v6=len(E), old=l, new=s, frag_old=c[2], frag_new=r['new_cell'], id=r['id'], node=r['node'], page=r['page'],
                             what='%s’s shape, the generator’s read of `%s` on the %s page' % (r['id'], r['node'].split('.')[-1],
                                                                                         'ζ' if r['page'] == 'zeta' else 'χ')))
        elif n >= i604:
            sec = _sec(n, S5)
            s, subs = _repin(l, sec)
            E.append(s)
            if subs:
                rep.append(dict(v5=n, v6=len(E), subs=subs, sec=sec))
            left = _left(s)
            if left:
                audit.append(dict(v5=n, sec=sec, mapped=[x[0] for x in subs], left=[int(x) for x in left]))
        else:
            E.append(l)
        if _map(n) != len(E):
            sys.exit('### THE MAP DRIFTED AT :%d' % n)
    pos = dict(rows={}, version=ins[0]['v6'], shape=rewd[0]['v6'])
    for i, l in enumerate(E, 1):
        m = K.ROW_RE.match(l)
        if m and i < _map(i604):
            pos['rows'][m.group(1)] = i
    E += _sv_bm(S5, rewd, ins, rep, pos, SJ)
    text = NL.join(E) + NL
    b = text.encode('utf-8')
    _write(dest, b)
    ed = text.split(NL)[:-1]
    body6, bm6 = R4._body_and_bm(ed)
    body5, bm5 = R4._body_and_bm(S5)
    J = dict(at=utc(), dry=DRY, path=K.SV6, sha256=sha(b), bytes=len(b), lines=len(ed), v5_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, K.SV5)).strip(),
             n_v5_body=_count([l for _i, l in body5]), n_body=_count([l for _i, l in body6]), n_backmatter=_count([l for _i, l in bm6]),
             n_v5_backmatter=_count([l for _i, l in bm5]), n_full=_count(ed), version_lines=len(_segs(ver)), ruled_insertions=0, credit=0, removals=0,
             rewrite_deltas=[dict(v5=x['v5'], v6=x['v6'], d=len(_segs(x['new'])) - len(_segs(x['old']))) for x in rewd],
             rew=rewd, ins=ins, rep=rep, audit=audit, pos=pos, bm6=ed.index(K.BM_TAG6) + 1, version=ver,
             ceiling_in_body=[(i, m.group(0)) for i, l in body6 for m in CEILING.finditer(l)])
    put_json('b622_sieve_edition.json', J)
    print('  %s : %d lines, sha256 %s ; body v0.5 %d ; v0.6 %d (%+d) ; version %d ; rewrite deltas %s ; back matter %d (v0.5 %d) ; re-pinned '
          'lines %d (cells %d) ; audited lines %d ; ceiling in body %s' % (
              dest, len(ed), J['sha256'][:16], J['n_v5_body'], J['n_body'], J['n_body'] - J['n_v5_body'], J['version_lines'],
              [(x['v5'], x['d']) for x in J['rewrite_deltas'] if x['d']], J['n_backmatter'], J['n_v5_backmatter'], len(rep),
              sum(len(x['subs']) for x in rep), len(audit), J['ceiling_in_body'] or 'none'))


def _sv_bm(S5, rewd, ins, rep, pos, SJ):
    q = _cell
    gen_c = (jx('b622_gen_commit.json') or {}).get('commit', '?')
    rows = [x for x in rewd if x.get('id')]
    diff = [x for x in rows if x['frag_old'] != x['frag_new'].replace(K.MARK_G, K.MARK_H)]
    L = ['', '---', '', K.BM_TAG6, '',
         '## Back matter of the v0.6 edition — written 2026-10-04 by b622 under the author’s ruling `(R232)`(4), by the form of `(R187)`(5), its '
         'clauses and the precedence order', '',
         '*This file is v0.6 of THE_FINDINGS_AS_THEY_STAND, written beside v0.5 (`%s`, unedited) from that version’s blob at PLACE-papers %s and '
         'the shapes bank (relay `data/b622_sieve_shapes.txt`) banked before the edition was written; v0.4, v0.3, v0.2 and the current version '
         '(read as v0.1) stand unedited too. The back matter of v0.2, v0.3, v0.4 and v0.5 is carried above whole, its own-line cells re-pinned '
         'to this file’s lines (counted below). Every line cited in this section is this file’s own unless it is marked otherwise.*' % (K.SV5, PRE_PP), '',
         '### The readings, each the seat’s and strikeable', '',
         '- **R-1** a row names a page node when its compiled-face column names, by its last name, a declaration that is a node of the ζ page '
         '(relay `data/b622_nodes_zeta.txt`, at SIDE-explicit-formula v0.20 = 914c413) or of the χ page (relay `data/b622_nodes_chi.txt`, at '
         'v0.21 = 1d5d4dd); the row is read by the first such declaration its column names, the ζ page read first: %d rows.' % len(rows),
         '- **R-2** the generator’s read is the shape cell the page prints for that node (relay `tools/chain_page.py`, `shape_of`, at relay '
         '%s), read at the page’s pin and not at the pin the row cites; the mark (G) stands beside it, the mark (H) beside every hand read kept.' % gen_c,
         '- **R-3** a row whose node the generator prints UNCLASSIFIED takes UNCLASSIFIED (G) as printed, for the author’s ruling; the seat’s '
         'proposal for it is on the trail record (relay `data/b622_unclassified.txt`).',
         '- **R-4** the shape column’s rule in “How the table reads” is rewritten to name both marks; every other line is carried unchanged, '
         'the verdicts, the tests and the registers included.', '',
         '### Removals', '', 'None.', '',
         '### The shapes read by the generator', '',
         '| row | this edition’s line | the page node | page | v0.5’s shape | this edition’s shape | Status |', '|:--|:--|:--|:--|:--|:--|:--|']
    for x in rows:
        L.append('| %s | :%d | `%s` | %s | %s | %s | %s |' % (x['id'], x['v6'], x['node'], 'ζ' if x['page'] == 'zeta' else 'χ', q(x['frag_old']),
                                                             q(x['frag_new']), 'as hand-read' if x not in diff else 'differs from the hand read'))
    L += ['', '### Rewrites -- the shape column’s rule and the rows’ shape cells', '',
          '| this edition’s line | v0.5’s line | v0.5’s wording | this edition’s wording | Status |', '|:--|:--|:--|:--|:--|']
    for x in rewd:
        L.append('| :%d | :%d | %s | %s | %s |' % (x['v6'], x['v5'], q(x['frag_old']), q(x['frag_new']), q(x['what'])))
    L += ['', '### Insertions ordered by the ruling', '', '| this edition’s line | the text | Status |', '|:--|:--|:--|']
    for x in ins:
        L.append('| :%d | %s | %s |' % (x['v6'], q(x['text']), q(x['what'])))
    L += ['', '### Re-pins of v0.5’s back matter', '',
          '%d own-line cells on %d lines of the carried back matter re-pinned to this file’s lines (v0.2’s: %d lines; v0.3’s: %d lines; v0.4’s: %d '
          'lines; v0.5’s: %d lines); every other line carried verbatim.' % (
              sum(len(x['subs']) for x in rep), len(rep), sum(1 for x in rep if x['sec'] == 'v0.2'), sum(1 for x in rep if x['sec'] == 'v0.3'),
              sum(1 for x in rep if x['sec'] == 'v0.4'), sum(1 for x in rep if x['sec'] == 'v0.5')), '',
          '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.6 | `%s` | written at b622 |' % K.SV6,
          '| v0.5 | `%s` | unedited |' % K.SV5] + ['| %s | `%s` | unedited |' % (v, p) for v, p in zip(
              ('v0.4', 'v0.3', 'v0.2', 'the current version, unnumbered (read as v0.1)'), K.SV_OLDER)] + [
          '| the generator and its shape reader | relay `tools/chain_page.py` at relay %s | edited at b622 |' % gen_c,
          '| the ζ page, with the shape column | `%s` | re-emitted at b622 |' % K.PAGE,
          '| the χ page, with the shape column | `%s` | re-emitted at b622 |' % K.DIR_PAGE,
          '| the shapes bank | relay `data/b622_sieve_shapes.txt` | banked at b622 before the edition |',
          '| the sentence-by-sentence diff | relay `data/b622_edition_FINDINGS_STAND.txt` | banked at b622 |', '',
          '### Correspondence', '',
          '| row | this edition’s line | v0.5’s line | the shape at v0.5 | the shape at v0.6 | Status |', '|:--|:--|:--|:--|:--|:--|']
    for x in rows:
        L.append('| %s | :%d | :%d | %s | %s | %s |' % (x['id'], x['v6'], x['v5'], q(x['frag_old']), q(x['frag_new']),
                                                       'the mark replaced' if x not in diff else 'the shape and the mark replaced'))
    L += ['', '### Version history', '',
          '- **v0.6, 2026-10-04 (b622, `(R232)`(4))**: the shape column read by the generator for the %d rows naming a page node -- %d as '
          'hand-read, %d differing (%s) -- and the hand marks kept where a row names none; the shape column’s rule rewritten to name both '
          'marks. v0.5 stands beside it, unedited.' % (len(rows), len(rows) - len(diff), len(diff),
                                                       ', '.join('%s %s' % (x['id'], x['frag_new']) for x in diff) or 'none'),
          '- **v0.5, 2026-10-04 (b617, `(R227)`(4))**: its own version history is carried above.', '']
    return L


def _ed(path):
    t = io.open(os.path.join(PP, *path.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return lines_of(t)


def _ed6():
    return lines_of(io.open(os.path.join(SP, 'b622_sieve_dry.md'), encoding='utf-8').read()) if DRY else _ed(K.SV6)


def sieve_termscan(*a):
    """### the scanner (banned_terms.py --new) on v0.6, banked as data/b622_sieve_termscan.txt."""
    out = _scan(os.path.join(SP, 'b622_sieve_dry.md') if DRY else os.path.join(PP, *K.SV6.split('/')))
    put_txt('b622_sieve_termscan.txt', out.rstrip(NL).split(NL))
    print([l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l])


def sieve_carried(E, ed, S5):
    """### every non-blank v0.5 line: carried verbatim at its mapped line, rewritten with both fragments in this file's rewrites table, or
    ### re-pinned (its own-line cells only)."""
    rw = {x['v5']: x for x in E['rew']}
    rp = {x['v5']: x for x in E['rep']}
    bm = NL.join(ed[E['bm6'] - 1:])
    ok, bad = 0, []
    for n in range(1, len(S5) + 1):
        if not S5[n - 1].strip():
            continue
        x6 = _map(n)
        if n in rw:
            x = rw[n]
            good = ed[x6 - 1] == x['new'] and ('| :%d | :%d | %s | %s |' % (x6, n, _cell(x['frag_old']), _cell(x['frag_new']))) in bm
        elif n in rp:
            good = ed[x6 - 1] == _repin(S5[n - 1], _sec(n, S5))[0] and ed[x6 - 1] != S5[n - 1]
        else:
            good = ed[x6 - 1] == S5[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def sieve_bank(*a):
    """### data/b622_edition_FINDINGS_STAND.txt and data/b622_h28.json: the diff with its offset line, the rows, the counts, the ceiling,
    ### the scanner, H28a-H28c and H56c."""
    E = jl('b622_sieve_edition.json')
    ed = _ed6()
    S5 = lines_of(_show(PP, PRE_PP, K.SV5))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    SJ = jl('b622_sieve_shapes.json')
    scan = rd('b622_sieve_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = _clean(scan)
    ok, bad = sieve_carried(E, ed, S5)
    body, bm = R4._body_and_bm(ed)
    bi = set(i for i, _l in body)
    hits = [dict(line=i, hit=m.group(0), kind='body' if i in bi else 'record') for i, l in enumerate(ed, 1) for m in CEILING.finditer(l)]
    beyond = [h for h in hits if h['kind'] == 'body']
    bmt = NL.join(ed[E['bm6'] - 1:])
    P = E['pos']
    h28a_rows = [dict(id='v0.5 :%d' % x['v5'], line=x['v6'], recorded=('| :%d | :%d | ' % (x['v6'], x['v5'])) in bmt) for x in E['rew']]
    gen_rows = [x for x in E['rew'] if x.get('id')]
    rows_cite = all(('| %s | :%d | `%s` |' % (x['id'], x['v6'], x['node'])) in bmt for x in gen_rows) and len(gen_rows) == len(SJ['rows'])
    h28a = 'HOLDS' if all(x['recorded'] for x in h28a_rows) and rows_cite else 'REFUTED'
    body_dn = E['n_body'] - E['n_v5_body']
    allowed = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines'] + sum(abs(x['d']) for x in E['rewrite_deltas'])
    strict = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not beyond else 'REFUTED'
    diff = [x for x in gen_rows if x['frag_old'] != x['frag_new'].replace(K.MARK_G, K.MARK_H)]
    took = all(ed[x['v6'] - 1].count('| %s |' % x['frag_new']) == 1 for x in gen_rows)
    h56c = 'HOLDS' if took and len(gen_rows) == len(SJ['rows']) and len(diff) <= 2 else 'REFUTED'
    kept = [i for i, rid, c in K.body_rows(ed[:E['bm6'] - 1]) if c[2].endswith(K.MARK_H)]
    offs = sorted(set((n, _map(n) - n) for n in (1, 3)))
    L = ['### OFFSET FROM v0.5 (R190)(3): %s -- the offset changes at each v0.5 line printed (v0.5 line, offset); every v0.5 line`s v0.6 '
         'line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b622 -- COMPONENT 4: THE SIEVE AT v0.6, (R232)(4), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v0.5 : PLACE-papers %s @ %s (blob %s), %d lines' % (K.SV5, PRE_PP, E['v5_blob'][:8], len(S5)),
         '### v0.6 : PLACE-papers %s, %d lines, sha256 %s' % (K.SV6, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (P['version'], ed[P['version'] - 1]), '',
         '### THE SHAPE COLUMN`S RULE, PRINTED: :%d %s' % (P['shape'], ed[P['shape'] - 1]), '',
         '### EVERY ROW NAMING A PAGE NODE, ITS SHAPE CELL AT v0.5 AND AT v0.6 (%d rows; %d differing from the hand read):' % (len(gen_rows), len(diff))]
    L += ['  %-6s :%-4d <- :%-4d %-42s %-17s -> %s%s' % (x['id'], x['v6'], x['v5'], x['node'].split('.')[-1], x['frag_old'], x['frag_new'],
                                                         '   ### DIFFERS' if x in diff else '') for x in gen_rows]
    L += ['', '### THE HAND MARKS KEPT (rows naming no page node): %d' % len(kept), '',
          '### EVERY REWRITE (v0.6 line <- v0.5 line, its fragments, the segment change):']
    for x in E['rew']:
        L += ['  :%d <- :%d  %s (%+d)' % (x['v6'], x['v5'], x['what'], len(_segs(x['new'])) - len(_segs(x['old']))),
              '      was : %s' % x['frag_old'], '      now : %s' % x['frag_new']]
    L += ['', '### EVERY INSERTION (v0.6 line, its segments, what orders it):']
    L += ['  :%d (%d) %s' % (x['v6'], len(_segs(x['text'])), x['what']) for x in E['ins']]
    L += ['', '### THE RE-PINS OF THE CARRIED BACK MATTER (%d lines, %d cells: v0.5 line -> v0.6 line, its cells old -> new):' % (
        len(E['rep']), sum(len(x['subs']) for x in E['rep']))]
    L += ['  :%d -> :%d  %s %s' % (x['v5'], x['v6'], x['sec'], ', '.join(':%d -> :%d' % tuple(s) for s in x['subs'])) for x in E['rep']]
    L += ['', '### THE AUDIT, BOTH WAYS: every back-matter line keeping a `:n` token after its re-pin, the tokens it mapped and every token it '
          'left (a left token cites another version`s line, another document`s or a ledger`s, or is a mapped own line):']
    L += ['  :%d %s mapped %s ; left %s' % (x['v5'], x['sec'], x['mapped'], x['left']) for x in E['audit']]
    L += ['', '### EVERY NON-BLANK v0.5 LINE -> ITS v0.6 LINE (%d carried verbatim, rewritten with its fragments recorded, or re-pinned ; '
          'failing %s): line n -> n + 2 from :3, n below :3' % (ok, bad or 'none'),
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v0.5`s BODY %d ; v0.6`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v0.2`s to v0.5`s carried, this act`s own, the history blocks included), printed separately ; the edition whole %d' % (
              E['n_v5_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled insertions %d + rewrites` segment changes %d '
          '+ one version line %d = %d ; the strict count %d' % (body_dn, E['credit'], E['removals'], E['ruled_insertions'],
                                                                sum(abs(x['d']) for x in E['rewrite_deltas']), E['version_lines'], allowed, strict), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling in the body: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on v0.6: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d rewrites) recorded with both wordings; the %d rows naming a page node each '
          'citing its node and page.**' % (h28a, len(h28a_rows), len(gen_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling in the body %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **H56c %s -- every row naming a page node takes the generator`s shape (%d of %d), %d differing from the hand read (bound '
          'two), each printed above.**' % (h56c, sum(1 for x in gen_rows if ed[x['v6'] - 1].count('| %s |' % x['frag_new']) == 1), len(SJ['rows']), len(diff)),
          '### ### **THE SIEVE LANDS: NO SENTENCE HELD.**' if h28a == 'HOLDS' and not bad else '### ### **HELD AT A SENTENCE: see above.**']
    put_txt('b622_edition_FINDINGS_STAND.txt', L)
    put_json('b622_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H56c=h56c, h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed, strict=strict,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, clean=clean, beyond=len(beyond), hits=hits,
                                   carried_ok=ok, carried_bad=bad, n_rows=len(gen_rows), n_diff=len(diff), kept=len(kept)))
    print('H28a %s H28b %s H28c %s H56c %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; beyond %d ; live %s ; rows %d diff %d kept %d' % (
        h28a, h28b, h28c, h56c, ok, bad, body_dn, allowed, strict, len(beyond), live.group(1) if live else None, len(gen_rows), len(diff), len(kept)))


def sieve_repin(*a):
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932), for v0.6. Writes data/b622_repin_sieve.txt."""
    E = jl('b622_sieve_edition.json')
    ed = _ed6()
    S5 = lines_of(_show(PP, PRE_PP, K.SV5))
    P = E['pos']
    checks = []
    for x in E['rep']:
        for o, n in x['subs']:
            checks.append(('carried cell :%d -> :%d (at :%d)' % (o, n, x['v6']), _map(o) == n and (ed[n - 1] == S5[o - 1] or any(
                y['v5'] == o and ed[n - 1] == y['new'] for y in E['rew']))))
    for x in E['rew']:
        checks.append(('rewrite :%d on :%d' % (x['v5'], x['v6']), ed[x['v6'] - 1] == x['new'] and x['v6'] == _map(x['v5'])))
    bm = NL.join(ed[E['bm6'] - 1:])
    for m in re.finditer(r'^\| ([A-Z]{2}-\d\d) \| :(\d+) \|', bm, re.M):
        checks.append(('v0.6`s back matter names %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    for m in re.finditer(r'^\| :(\d+) \| :(\d+) \| ', bm, re.M):
        a_, b_ = int(m.group(1)), int(m.group(2))
        checks.append(('the rewrites table`s :%d <- :%d' % (a_, b_), _map(b_) == a_ and any(y['v6'] == a_ for y in E['rew'])))
    for m in re.finditer(r'^\| :(\d+) \| ', bm, re.M):
        a_ = int(m.group(1))
        checks.append(('a cited line :%d holds text' % a_, bool(ed[a_ - 1].strip())))
    for k in ('version', 'shape'):
        checks.append(('%s on :%d' % (k, P[k]), bool(ed[P[k] - 1].strip())))
    checks.append(('the version line above v0.5`s', ed[P['version'] - 1] == E['version'] and ed[P['version'] + 1] == S5[2]))
    bank = rd('b622_edition_FINDINGS_STAND.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v0.5') and bank.count('### OFFSET FROM') == 1))
    fsha = sha((NL.join(ed) + NL).encode('utf-8'))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and fsha == E['sha256']))
    for m in re.finditer(r'^  ([A-Z]{2}-\d\d) +:(\d+) <- ', bank, re.M):
        checks.append(('the diff bank`s %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    L = ['### b622 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % K.SV6, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b622_repin_sieve.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H56a', 'H56b', 'H56c', 'H56d')
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'day1/A_Place_to_Stand_v5_18.md', K.SV5) + K.SV_OLDER + tuple(K.WL_FILES)
WANT_RELAY = sorted(set(GEN_FILES) | set('data/%s/%s' % (K.WL_DIR, fn) for fn, _k in K.WL_FILES.values()))


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


def readme_ok():
    """### README at HEAD and on disk is the pre-act README with the dated append and the refresh, and nothing else."""
    pre = _show(PP, PRE_PP, 'README.md')
    want, _at = readme_text(pre or '')
    disk = io.open(os.path.join(PP, 'README.md'), encoding='utf-8').read()
    return bool(want) and disk == want and _show(PP, 'HEAD', 'README.md') == want


def n5(trail_line=None, ot=None, *a):
    """### N5, scored by its letter: nothing deposits; no kernel touched; no current version edited beyond README's dated append; no file
    ### written beyond the generator edit and its test, the re-emitted pages, the sieve's v0.6 and its diff bank, the work-list entries, the
    ### README append, the record lines and the trails. ### THE STANDING REPAIR (OPEN_TRAILS :12799): `trail_line` is the line the trail
    ### record's head takes on OPEN_TRAILS; a pending record is counted as OPEN_TRAILS' write."""
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
    face = jl('b622_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state(list(face)).items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if any(jx('b622_page_%s_%s.json' % (k, t)).get('changed') for t in ('c3', 'c4'))]
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', K.SV6] + pages)
    created = sorted(set(x for x in g(PP, 'diff', '--name-only', '--diff-filter=ADR', PRE_PP, 'HEAD').split(NL) if x.strip())
                     | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL)
                           if x.startswith('?? ')))
    cur_ok = all((_show(PP, PRE_PP, p) or '') == (_show(PP, 'HEAD', p) or '') and (_show(PP, PRE_PP, p) or '') == R2.cr0(
        open(os.path.join(PP, *p.split('/')), 'rb').read()).decode('utf-8', 'replace') for p in CURRENTS) and readme_ok()
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith(('b622_', 'audit_b622_', 'terminal_table'))
                              and x != 'data/b621_closing_push_out.txt'))
    relay_ok = all(x in WANT_RELAY for x in relay_beyond)
    if rec_ok and rec_state.startswith('the trail record pending') and 'OPEN_TRAILS.md' not in pp_ch:
        pp_ch = sorted(pp_ch + ['OPEN_TRAILS.md'])   # ### the pending record is OPEN_TRAILS' write when it is the act's only one there
    ok = kern_same and created == [K.SV6] and cur_ok and pp_ch == want_pp and relay_ok and rec_ok
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; kernels unmoved since the face %s; created %s (wanted %s); the current versions and the documents read unedited, '
            'README by its dated append alone %s; PLACE-papers %s (wanted %s); %s; relay beyond the act`s banks and the table %s (allowed: the '
            'generator, its test and the work-list files)' % (kern_same, created, [K.SV6], cur_ok, pp_ch, want_pp, rec_state, relay_beyond))


def scores(*a):
    A = jx('b622_h56a.json')
    Z3, X3, Z4, X4 = (jx('b622_page_%s_%s.json' % (k, t)) for t in ('c3', 'c4') for k in ('zeta', 'chi'))
    H = jx('b622_h28.json')
    WJ, RJ = jx('b622_worklists.json'), jx('b622_readme.json')
    arms3, arms4 = rd('b622_page_arms_c3.txt'), rd('b622_page_arms_c4.txt')
    rep = rd('b622_repin_sieve.txt')
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    unc = (Z3.get('unclassified') or []) + (X3.get('unclassified') or [])
    objs = (Z3.get('objects') or []) + (X3.get('objects') or [])
    h56b = 'HOLDS' if Z3.get('rc') == 0 and X3.get('rc') == 0 and len(unc) <= 3 else 'REFUTED'
    arms_ok = lambda t: 'PAGE ARMS PASSING : 2 of 2' in t and 'PASSING : 2 of 2.**' in t.split('PAGE ARMS PASSING')[-1]   # noqa: E731
    h28 = (H.get('H28a'), H.get('H28b'), H.get('H28c'))
    h56d = 'HOLDS' if h28 == ('HOLDS', 'HOLDS', 'HOLDS') and arms_ok(arms3) and arms_ok(arms4) else 'REFUTED'
    rc = _relay_commits()
    pc = _pp_commits()
    gen_c = _alone(RELAY, list(GEN_FILES), rc)
    lock = _epoch(re.search(r'locked at \(UTC\) : (\S+)', rd('b622_registration_2026-10-04.txt') or '').group(1)) if re.search(
        r'locked at \(UTC\) : (\S+)', rd('b622_registration_2026-10-04.txt') or '') else None
    gen_after = bool(gen_c) and lock is not None and int(g(RELAY, 'show', '-s', '--format=%ct', gen_c[0]).strip() or 0) > lock
    s2_ctl = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA PASSING : 2 of 2' in arms4
    old = jx('b622_old_lists.json')
    s3 = bool(re.search(r'RE-PIN : (\d+) of \1 citations hold', rep))
    pg = {p: [h for h, s in pc if _files(h) == [p]] for p in (K.PAGE, K.DIR_PAGE)}
    s4 = all(x.get('rc') == 0 for x in (Z3, X3, Z4, X4)) and all(
        len(pg[K.PNAME[k]]) == sum(1 for t in ('c3', 'c4') if jx('b622_page_%s_%s.json' % (k, t)).get('changed')) for k in ('zeta', 'chi'))
    s5 = WJ.get('n_items') == 39 and len(WJ.get('files') or []) == 14 and len(_alone(RELAY, WANT_RELAY_WL, rc)) == 1
    S = {
        'H56a': (A.get('H56a', 'REFUTED'), 'the five test nodes read %s' % [(x['name'].split('.')[-1], x['want'], x['got']) for x in A.get('reads') or []]),
        'H56b': (h56b, 'UNCLASSIFIED across both pages %d %s (bound three); the objects printed — beside them %d' % (len(unc), unc, len(objs))),
        'H56c': (H.get('H56c', 'REFUTED'), 'rows naming a page node %s, each taking the generator`s shape; differing from the hand read %s (bound two)' % (
            H.get('n_rows'), H.get('n_diff'))),
        'H56d': (h56d, 'H28a-H28c on v0.6 %s; the page arms and the frozen control after the column %s and after the sieve %s' % (
            h28, arms_ok(arms3), arms_ok(arms4))),
        'N1': (('HELD' if A.get('H56a') == 'HOLDS' else 'REFUTED'), 'the five test nodes read %s, wanted FINITE, UNIVERSAL, UNIVERSAL, DENSITY, FAMILY' % (
            [x['got'] for x in A.get('reads') or []])),
        'N2': (('HELD' if h56b == 'HOLDS' else 'REFUTED'), 'UNCLASSIFIED %d (bound three); objects — %d' % (len(unc), len(objs))),
        'N3': (('HELD' if (H.get('n_diff') is not None and H['n_diff'] <= 2) else 'REFUTED'), 'sieve rows differing between the hand read and the '
               'generator`s %s (bound two)' % H.get('n_diff')),
        'N4': (('HELD' if h28 == ('HOLDS', 'HOLDS', 'HOLDS') and arms_ok(arms4) else 'REFUTED'), 'H28a-H28c on v0.6 %s; both page arms after the sieve %s' % (
            h28, 'PAGE ARMS PASSING : 2 of 2' in arms4)),
        'N5': n5v,
        'S1': (('HELD' if len(gen_c) == 1 and gen_after else 'REFUTED'), 'the generator edit and its test in one relay commit of their own %s, after '
               'the lock %s' % (gen_c, gen_after)),
        'S2': (('HELD' if s2_ctl and old.get('ok') is True else 'REFUTED'), 'lists without the column: the frozen control %s; b602`s and b603`s lists '
               'against their pages at %s %s' % (s2_ctl, PRE_PP, old.get('detail'))),
        'S3': (('HELD' if s3 else 'REFUTED'), 'the re-pin: %s' % (([l for l in rep.split(NL) if 'RE-PIN :' in l] or ['none'])[0].strip())),
        'S4': (('HELD' if s4 else 'REFUTED'), 'the page passes exit %s ; each changed page committed alone %s' % (
            [x.get('rc') for x in (Z3, X3, Z4, X4)], pg)),
        'S5': (('HELD' if s5 else 'REFUTED'), 'the 39 sentences %s in %d files, one relay commit of their own %s' % (
            WJ.get('n_items'), len(WJ.get('files') or []), _alone(RELAY, WANT_RELAY_WL, rc))),
    }
    put_json('b622_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


WANT_RELAY_WL = sorted('data/%s/%s' % (K.WL_DIR, fn) for fn, _k in K.WL_FILES.values())


def _epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def old_lists(*a):
    """### S2's second limb: b602's and b603's lists, which carry no column line, re-emitted from their probes against their pages at
    ### PRE_PP (before this act) through the generator as edited; data/b622_old_lists.json."""
    import chain_page as CP
    out, ok = [], True
    for k in ('zeta', 'chi'):
        rc, pg, _m, _l = CP.build(os.path.join(D, K.OLD_NODES[k]), os.path.join(SP, '_b622_old'), os.path.join(D, K.PROBE[k]))
        want = R2.cr0(subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, K.PNAME[k])], capture_output=True).stdout)
        got = pg.encode('utf-8') if rc == 0 and pg else b''
        out.append(dict(list=K.OLD_NODES[k], rc=rc, equal=got == want, bytes=len(got), want_bytes=len(want)))
        ok = ok and rc == 0 and got == want
    put_json('b622_old_lists.json', dict(at=utc(), ok=ok, detail=out))
    print('  lists without the column, byte for byte against their pages at %s: %s %s' % (PRE_PP, ok, out))


TRAIL_HEAD = ('### b622 — lane three, act forty-nine under (R232): the quantifier column -- the generator reading each node’s shape from its '
              'Lean statement, both pages re-emitted, the sieve’s hand marks replaced; README’s supportable sentence for v0.17–v0.21; the 39 '
              'owed sentences entered as work-list items')
FOR_AUTHOR = ('(1) “a cell” among the five test nodes read as `liCoeff_one_pos`, the ζ page’s one FINITE rung (λ₁ > 0 at one index), '
              'the sieve’s RH-13; (2) the column is switched on by one line of the node list (`# column: quantifier`), carried by this act’s '
              'lists (relay data/b622_nodes_zeta.txt, data/b622_nodes_chi.txt, b602’s and b603’s lists with the line added), so a list '
              'without it emits exactly as before; (3) the reader’s rules -- a premise passed over, an iff or a conjunction at the higher of its '
              'sides in the order FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY, a Prop on the page read through its own statement, a proof binder '
              'passed over, an atom no rule reads left unread; (4) the pages re-emitted a second time after the sieve’s v0.6 by the page clause '
              '(OPEN_TRAILS :12190), their Placement gaining it; (5) a sieve row names a page node by its compiled-face column’s first such '
              'declaration, the ζ page read first, its mark (G); (6) README’s refresh names the internal versions v5.14 to v5.18 by their acts '
              'and the live kernel line in the deposit note; (7) the 39 sentences’ lines are their documents’ current editions’, entered '
              'in the seven work-lists as a dated section and in seven addenda beside them')


def _title_entry():
    Z3, X3, SJ = jx('b622_page_zeta_c3.json'), jx('b622_page_chi_c3.json'), jx('b622_sieve_shapes.json')
    unc = len((Z3.get('unclassified') or []) + (X3.get('unclassified') or []))
    return ('## The quantifier column: five shapes read from the Lean statements at v0.20 and v0.21, %d nodes UNCLASSIFIED, the sieve at '
            'v0.6 with %d hand marks replaced; README’s supportable sentence for v0.17–v0.21' % (unc, len(SJ.get('rows') or [])))


def _finding_text():
    S, rl, A, H, SJ = (jl(n) for n in ('b622_scores.json', 'b622_record_lines.json', 'b622_h56a.json', 'b622_h28.json', 'b622_sieve_shapes.json'))
    Z3, X3, UJ, WJ, RJ = (jl(n) for n in ('b622_page_zeta_c3.json', 'b622_page_chi_c3.json', 'b622_unclassified.json', 'b622_worklists.json',
                                          'b622_readme.json'))
    gc = jx('b622_gen_commit.json').get('commit', '?')
    pc = _pp_commits()
    sv = ([h for h, s in pc if _files(h) == [K.SV6]] or ['?'])[0]
    rm = ([h for h, s in pc if _files(h) == ['README.md']] or ['?'])[0]
    t = _title_entry()
    unc = Z3['unclassified'] + X3['unclassified']
    objs = Z3['objects'] + X3['objects']
    cnt = {}
    for P in (Z3, X3):
        for s in P['shapes'].values():
            cnt[s] = cnt.get(s, 0) + 1
    diff = [r for r in SJ['rows'] if not r['same']]
    e = ['', t, '',
         '*Filed at b622 on the author’s ruling `(R232)` and the author’s answer before the seal. Banks: relay `data/b622_gen_test.txt`, '
         '`data/b622_gen_diff.txt`, `data/b622_sieve_shapes.txt`, `data/b622_unclassified.txt`, `data/b622_edition_FINDINGS_STAND.txt`, '
         '`data/b622_worklists.txt`, `data/b622_author_answers.txt`. Nothing deposits.*', '',
         '**The generator** (`(R232)`(4), W-ORD-QUANTIFIER-COLUMN with DENSITY, OPEN_TRAILS :12266 and :12296): relay `tools/chain_page.py` '
         'reads each node’s shape from its statement as the probe printed it, its leading binders read through premises, iffs and conjunctions '
         'and a Prop on the page read through its own statement, and prints FINITE, UNIVERSAL, LIMIT, DENSITY or FAMILY, UNCLASSIFIED where it '
         'reads nothing, and — for an object, by the author’s answer before the seal; a list carrying one column line takes the cell and one '
         'head line, a list without it emits as before. The edit and its test committed alone at relay %s; the test %d of %d cases; the five '
         'test nodes read %s, H56a %s.' % (gc, A['passing'], A['cases'], ', '.join('%s %s' % (x['name'].split('.')[-1], x['got']) for x in A['reads']), S['H56a'][0]), '',
         '**The pages**, each re-emitted from its banked probe at v0.20 and v0.21 and committed alone, then again after the sieve’s v0.6: '
         '%d nodes in all -- %s; UNCLASSIFIED %d (%s), H56b %s, each for the author’s ruling with the seat’s proposal by the author’s reading '
         '(the strongest field): %s.' % (len(Z3['shapes']) + len(X3['shapes']), ', '.join('%s %d' % (k, cnt.get(k, 0)) for k in
                                                                                         ('FINITE', 'UNIVERSAL', 'LIMIT', 'DENSITY', 'FAMILY', '—', 'UNCLASSIFIED')),
                                         len(unc), ', '.join(n.split('.')[-1] for n in unc), S['H56b'][0],
                                         ', '.join('%s %s' % (n.split('.')[-1], p) for n, p in UJ['proposals'].items())), '',
         '**The sieve at v0.6** (`%s`, %s, alone): the %d rows naming a page node take the generator’s shape, %d as hand-read and %d not (%s); '
         'the hand marks kept on the rest; H28a-H28c %s, H56c %s; re-pin %s.' % (
             K.SV6, sv, len(SJ['rows']), len(SJ['rows']) - len(diff), len(diff), '; '.join('%s %s, hand %s' % (r['id'], r['gen'], r['hand']) for r in diff) or 'none',
             '/'.join(str(H.get(x)) for x in ('H28a', 'H28b', 'H28c')), S['H56c'][0],
             ([l.split('RE-PIN : ')[1].split(' citations')[0] for l in rd('b622_repin_sieve.txt').split(NL) if 'RE-PIN : ' in l] or ['?'])[0]), '',
         '**README** (`(R232)`(3), %s, alone): the author’s supportable sentence for v0.17–v0.21 appended beside the `(R183)`(3) sentence, '
         'which stays, at README :%d; the deposit note’s live line refreshed to v5.18 with the live kernel line; the scanner %s.' % (
             rm, RJ['para'], 'CLEAN' if RJ['clean'] else 'NOT CLEAN'), '',
         '**The 39 owed sentences** (`(R232)`(2)): entered by line in their documents’ b558 work-lists (seven appended) and in addenda beside them '
         '(seven created), relay `data/b558_editions/`, one commit of their own; %d of 39.' % WJ['n_items'], '',
         '**The record lines.** b621’s weight with the confirmations at FINDINGS :%d; the offer taken at OPEN_TRAILS :%d, addressed to the '
         'form’s clause (:12839).' % (rl['lines'][0]['line'], rl['lines'][1]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads by the generator the shapes the sieve’s v0.2 hand-read (b604, :7060) and '
         'v0.5 carried (b617, :7368), and the faces b596 found silent on multiplicity (:6856); the pages it re-emits are b602’s and b603’s; the '
         'test node of DENSITY is b597’s fact correction (OPEN_TRAILS :12296); the README sentence it appends sits beside b573’s (:6354). It '
         'strengthens the programme’s offering of a page on which a finite fact and an infinite equivalence no longer sit unmarked side by '
         'side: the mark is read from the statement, by a tool any reader can re-run.', '',
         '**Next.** Per `(R232)`(5): b623, W-ORD-TAG-REMOTES and W-ORD-SEC-AXIOM-ARTEFACT in one act. The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; no current version edited beyond README’s dated append; nothing here is a statement about RH, '
         'GRH or any zero beyond the compiled statements’ own words.*', '']
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
    put_json('b622_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl, UJ, WJ = (jl(n) for n in ('b622_scores.json', 'b622_findings.json', 'b622_record_lines.json', 'b622_unclassified.json', 'b622_worklists.json'))
    gc = jx('b622_gen_commit.json').get('commit', '?')
    pc = _pp_commits()
    ec = lambda p: ' '.join([h for h, s in pc if _files(h) == [p]]) or '?'   # noqa: E731
    rows_ = ['', TRAIL_HEAD, '',
             '**(R232) ratified.** (1) b621 at its weight; the seat’s readings and offer confirmed. (2) The 39 owed sentences entered as work-list '
             'items. (3) README’s supportable sentence for v0.17–v0.21 and the deposit note’s live line. (4) W-ORD-QUANTIFIER-COLUMN with DENSITY; '
             'H56a-H56d. (5) The act after: b623.', '',
             '**Entered:** FINDINGS.md:%d (b621’s weight and the confirmations), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d '
             '(the offer, addressed to :12839); this record; README.md %s; the pages %s (ζ) and %s (χ); %s %s; relay tools/chain_page.py and '
             'tools/test_chain_page_b596.py %s; relay data/b558_editions/ (the 39 sentences); relay data/b622_nodes_zeta.txt, data/b622_nodes_chi.txt, '
             'data/b622_gen_test.txt, data/b622_sieve_shapes.txt, data/b622_unclassified.txt, data/b622_edition_FINDINGS_STAND.txt, '
             'data/b622_worklists.txt.' % (rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line'], ec('README.md'), ec(K.PAGE), ec(K.DIR_PAGE),
                                            K.SV6, ec(K.SV6), gc), '',
             '**The author’s answer before the seal** (relay data/b622_author_answers.txt): an object prints —, as the tier column does for a '
             'definition; H56b and N2 count the UNCLASSIFIED nodes against the bound of three, the — nodes printed beside them; the UNCLASSIFIED '
             'nodes, premise bundles, are for the author’s ruling at the closing, a bundle reading as its strongest field.', '',
             '**For the author’s ruling, the UNCLASSIFIED nodes with the seat’s proposals** (relay data/b622_unclassified.txt): %s.' % (
                 '; '.join('%s, proposed %s' % (n, p) for n, p in UJ['proposals'].items())), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b622_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R232)`(5), b623, W-ORD-TAG-REMOTES and W-ORD-SEC-AXIOM-ARTEFACT in one act; the author rules on the closing.', '',
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
        print(e[:9000])
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b622_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b622_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-04 by b622 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    """### OPEN_TRAILS: a correction to the record, its text read from data/b622_defects.json (`correction`), addressed to the record and
    ### appended at the end; `dry` prints it. Nothing is written when the bank carries no correction."""
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b622_defects.json -- NOTHING WRITTEN')
    rec = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec, CORRECTION)
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
    put_json('b622_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec), head=CORR_HEAD % rec, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec))


def gen_commit(*a):
    """### data/b622_gen_commit.json: the relay commit holding the generator edit and its test alone, read from relay's log."""
    rc = _relay_commits()
    c = _alone(RELAY, list(GEN_FILES), rc)
    put_json('b622_gen_commit.json', dict(at=utc(), commit=c[0] if len(c) == 1 else None, all=c))
    print('  the generator commit: %s' % c)


def desk(*a):
    S = jl('b622_scores.json')
    L = ['=' * 104, 'b622 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H56a-H56d, (R232)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H56 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b622_defects.txt').rstrip(NL).split(NL)
    put_txt('b622_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, A, H, WJ, RJ = (jl(n) for n in ('b622_scores.json', 'b622_findings.json', 'b622_trail.json', 'b622_record_lines.json', 'b622_h56a.json',
                                                  'b622_h28.json', 'b622_worklists.json', 'b622_readme.json'))
    Z3, X3, Z4, X4 = (jx('b622_page_%s_%s.json' % (k, t)) for t in ('c3', 'c4') for k in ('zeta', 'chi'))
    L = ['b622 -- THE COMPONENTS, BANKED UNDER (R232).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b621`s closing push-out relay %s ; push-b621* branches deleted by name '
         '(data/b622_branches.txt) ; the kept branches untouched ; the suite, its sources repaired, run at HEAD before the face (data/b622_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b621`s weight FINDINGS :%d ; the offer OPEN_TRAILS :%d ; the 39 sentences data/b622_worklists.txt (%d in %d files) ; README '
         ':%d (data/b622_readme.json, scanner %s)' % (rl['lines'][0]['line'], rl['lines'][1]['line'], WJ['n_items'], len(WJ['files']), RJ['para'],
                                                     'CLEAN' if RJ['clean'] else 'NOT CLEAN'),
         '### COMPONENT 2 : the generator data/b622_gen_diff.txt ; its test data/b622_gen_test.txt (%d of %d) ; H56a %s' % (A['passing'], A['cases'], S['H56a'][0]),
         '### COMPONENT 3 : the ζ page changed %s, the χ page changed %s (with the column) ; UNCLASSIFIED %s ; page arms data/b622_page_arms_c3.txt ; '
         'H56b %s' % (Z3.get('changed'), X3.get('changed'), Z3.get('unclassified', []) + X3.get('unclassified', []), S['H56b'][0]),
         '### COMPONENT 4 : v0.6 data/b622_edition_FINDINGS_STAND.txt (H28a %s, H28b %s, H28c %s, H56c %s) ; the pages again by the page clause, '
         'changed %s and %s ; page arms data/b622_page_arms_c4.txt ; H56d %s' % (H['H28a'], H['H28b'], H['H28c'], S['H56c'][0], Z4.get('changed'),
                                                                                X4.get('changed'), S['H56d'][0]),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b623 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b622_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b622_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
