# -*- coding: utf-8 -*-
"""b640_record.py -- THE ACT'S RECORD TOOL, UNDER (R250). ### ONE SUBCOMMAND PER BANK.

### ### b640: LANE THREE, ACT SIXTY-SEVEN -- THE PREMISE STATUS SPLIT TO FIVE AND THE OPEN PREMISES GIVEN WORK-ORDERS; THE DEPOSIT
### DESCRIPTION'S ASSUMPTION SECTION RECOMPOSED; A SECOND READER FOR LEGIBILITY; THE DRAFT 23228113 UPDATED AND HELD AT THE SAME PROMPT.
### Subcommands write only `data/b640_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers
### are b633's and b639's record tools', imported; the five statuses are tools/premise_status.py's (the shared tool, carried from b639's record
### tool and extended through the Edit tool after the seal); ledger appends through b566's guarded `append_to`.
### THE (R110) ROUTE (OPEN_TRAILS :9514): b639's request function, imported -- the token read from the environment variable at call time, sent
### in the `Authorization` header alone, never printed, logged or banked; no identifier of the author in any request. The draft is updated, never
### published, until the author's word "publish" stands in data/b640_author_answers.txt beneath the deposit prompt.
"""
import collections
import difflib
import hashlib
import html as HT
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b638_record as R8  # noqa: E402
import b639_record as R9  # noqa: E402
import b639_worklist as K9  # noqa: E402
import b640_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = '47d34df0-9823-4c9f-9efb-d1daddb7dd61'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b640_registration_2026-10-08.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of, _nd, predict_cells, _land = R3.lines_of, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
put_txt, put_json, _tok, _tclean, http, _j = R9.put_txt, R9.put_json, R9._tok, R9._tclean, R9.http, R9._j
STANDIN = os.environ.get('B640_STANDIN') if ('dry' in sys.argv[2:]) else None
KERNS_READ = R9.KERNS_READ


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
_DJ = os.path.join(D, 'b640_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b640 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b640_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b640_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def _ps():
    """### the shared status tool; before its five-status edit lands (Component 2, after the seal) a dry run reads the scratchpad prototype, and
    ### a run that writes refuses."""
    try:
        import premise_status as PS
        if hasattr(PS, 'classify5'):
            return PS
    except ImportError:
        pass
    if not DRY:
        sys.exit('### THE STATUS TOOL HAS NO FIVE-STATUS RULE YET -- NOTHING WRITTEN')
    import importlib.util
    spec = importlib.util.spec_from_file_location('premise_status_proto', os.path.join(SP, 'premise_status_proto.py'))
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    return P


# ================================================================================ READING (1): THE READS
def _use_sites(name):
    out = []
    for repo in ('D:/SIDE-explicit-formula', 'D:/SIDE-global-section', 'D:/SIDE-lv-conservation', 'D:/SIDE-carrier-spec', 'D:/SIDE-rcurve',
                 'D:/SIDE-grh-transfer'):
        for l in g(repo, 'grep', '-n', '-w', name, 'main', '--', '*.lean').split(NL)[:8]:
            if l.count(':') >= 3:
                _p, f, ln, t = l.split(':', 3)
                out.append('    %s %s :%s  %s' % (repo.replace('D:/', ''), f, ln, ' '.join(t.split())[:150]))
    return out


def READS():
    return [
        ('relay data/b639_premise_status.txt whole: its summary lines and every head`s line and hand-read', RELAY, PRE_RELAY,
         'data/b639_premise_status.txt', ('GREP', r'^### |^  [A-Za-z]|hand-read'), 400),
        ('relay data/b639_deposit_description.txt whole (sha256 dab9ba5f...), one line', RELAY, PRE_RELAY, 'data/b639_deposit_description.txt',
         ('GREP', r'.'), 120),
        ('OPEN_TRAILS: the criterion (:12955); the second-reader form (:12839, :12863) and its memory isolation (:13223); the method item, the '
         'patch work-order, b639`s record and correction; the work-orders carrying four heads; the form, the precedence order, the authority '
         'order, the build clause, the N5 scorer, the build route', PP, PRE_PP, 'OPEN_TRAILS.md', sorted(set(K.FERRY_LINES)), 1600),
        ('FINDINGS: b639`s weight line on b638 and b639`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B639_WEIGHT_PRIOR, K.B639_ENTRY], 600),
        ('relay tools/e0_rule.py: the domain-condition classes and MET', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         ('GREP', r'domain condition|^MET\b|restriction'), 220),
        ('relay data/b639_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b639_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
        ('relay tools/b639_record.py: the route`s steps for a draft`s files and metadata', RELAY, PRE_RELAY, 'tools/b639_record.py',
         ('GREP', r'^def (z_files|z_meta|z_read|http)|DELETE|PUT|actions/'), 200),
        ('relay tools/b632_record.py: the reader`s staging (the lead, the one-liner, the hold)', RELAY, PRE_RELAY, 'tools/b632_record.py',
         ('GREP', r'^LEAD|^ONE_LINER|^HOLD_PROMPT|claude -p'), 260),
    ]


def reads(*a):
    L = ['b640 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    L.append('### THE USE SITES, git grep -w per name at each kernel`s main: the six heads b639 read witness-only and the four Mathlib predicates')
    for n in ('Alternates', 'HCount', 'IsSign', 'SatisfiesCWeil', 'StepsI', 'StepsMI') + K.MATHLIB_FOUR:
        us = _use_sites(n)
        L.append('  %s (%d sites printed):' % (n, len(us)))
        L += us
    L.append('### THE READER`S STAGING PATTERN: D:\\reader_b632 holds %s' % sorted(os.listdir('D:/reader_b632')) if os.path.isdir('D:/reader_b632') else
             '### D:\\reader_b632 ABSENT')
    L += ['', '### the token`s location: the environment variable %s ; present %s ; not printed' % (K.TOKVAR, bool(_tok())),
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b640_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()) + 2, len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R250) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b640 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b640_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b640_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b640_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


def seal_hashes():
    rec_ = jl('b640_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b640 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b640_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 2: THE STATUS AT FIVE, (R250)(3)
def _facts(PS, x, rows, E):
    """### one head's five-status facts, read from the kernels at the commits the table read its rows at."""
    keys = [tuple(k.split(' ', 1)) for k in x['rows']]
    repos = sorted(set(k for k, _n in keys))
    dv, decls, inl = [], [], []
    for k in [tuple(k.split(' ', 1)) for k in x['rule_rows']]:
        r = rows.get(k)
        if not r:
            dv.append([])
            continue
        hd, pb = R8._premise_binders(r, E)
        mine = [b for b in pb if R8.R7._premise_heads(b, hd)[0] == x['head']]
        try:
            allb = E.binders_of(hd)
        except Exception:
            allb = []
        dv.append(PS.domain_vars(x['head'], hd, mine, allb))
    for repo in repos:
        pin = sorted(set((rows[k].get('head') or '')[:7] for k in keys if k[0] == repo and k in rows))[0]
        decls += [dict(repo=repo, pin=pin, **d) for d in PS.decls_concluding('D:/' + repo, pin, x['head'])]
        inl += [dict(repo=repo, pin=pin, **d) for d in PS.inline_of('D:/' + repo, pin, x['head'])]
    standalone = [d for d in decls if not d['salt'] and not d['relation'] and not d['hyps']]
    for d in standalone:
        nm = re.search(r'\b(?:theorem|lemma|def|abbrev|instance)\s+([^\s({\[:]+)', d['text'])
        d['name'] = nm.group(1) if nm else ''
        d['consumers'] = PS.consumers('D:/' + d['repo'], d['pin'], d['name'], d['file'], d['line']) if d['name'] else []
    inline = [d for d in inl if not d['salt'] and not d['iff'] and d['live']]
    salt = [d for d in decls if d['salt']] + [d for d in inl if d['salt']]
    cited, cl, ot = PS.cited_whole((x.get('decl') or {}).get('doc'))
    return dict(upstream=x['decl'] is None, domain_vars=dv, consumed=[d for d in standalone if d['consumers']], inline=inline, standalone=standalone,
                cited=cited, cited_lines=cl, other_tiers=ot, salt=salt)


def status(*a):
    """### Component 2, (R250)(3) as the author answered before the seal: the 50 heads of b639's bank re-read at their pins and each classed by
    ### the shared tool's five-status rule; every move from b639's four-status read printed with its reason; the DOMAIN heads removed to the
    ### domain-condition list with each row's quantified variables named; the salt-check column beside every head; the seat's hand-reads of
    ### b639 beside. data/b640_premise_status.txt and its json; H74a scored there."""
    import e0_rule as E
    PS = _ps()
    S9 = jl('b639_premise_status.json')
    rows = dict(((r['repo'], r['name']), r) for r in _table())
    res = []
    for x in S9.get('heads') or []:
        f = _facts(PS, x, rows, E)
        st, meets = PS.classify5(f)
        res.append(dict(head=x['head'], status=st, meets=meets, was=x['status'], rule=x['rule'], elab=x['elab'], kernels=x['kernels'],
                        pins=x['pins'], rule_rows=x['rule_rows'], decl=x['decl'], upstream=f['upstream'], domain_vars=f['domain_vars'],
                        consumed=[dict(file=d['file'], line=d['line'], name=d['name'], consumers=d['consumers'][:4]) for d in f['consumed']],
                        inline=[dict(file=d['file'], line=d['line'], text=d['text'][:120]) for d in f['inline']],
                        standalone=[dict(file=d['file'], line=d['line'], name=d['name']) for d in f['standalone']],
                        salt=[dict(file=d['file'], line=d['line'], text=d['text'][:100]) for d in f['salt']], cited=f['cited'],
                        cited_lines=f['cited_lines'], other_tiers=f['other_tiers'], handread9=x.get('handread', ''),
                        wo9=x.get('wo_handread') or []))
    cnt = collections.Counter(x['status'] for x in res)
    rr, er = collections.Counter(), collections.Counter()
    for x in res:
        rr[x['status']] += x['rule']
        er[x['status']] += x['elab']
    four = dict((x['head'], x['status']) for x in res if x['head'] in K.MATHLIB_FOUR)
    h74a = len(res) == 50 and all(x['status'] in K.STATUSES5 for x in res) and all(v == 'DOMAIN' for v in four.values()) and len(four) == 4
    reason = {'DOMAIN': 'a Mathlib predicate every row applies to a quantified variable', 'DISCHARGED': 'a construction a non-witness proof consumes',
              'CITED': 'every field cited T1-lit', 'WITNESSED': 'standalone constructions outside the salt checks, none consumed',
              'OPEN': 'no construction outside the salt checks, no citation of every field'}
    figure = dict(cnt) == K.FIGURE5
    L = ['b640 -- COMPONENT 2, (R250)(3): THE 50 PREMISE HEADS AT FIVE STATUSES, READ FROM THE USE SITE (%s)' % utc(), '',
         '### THE RULE, the author`s answers before the seal (data/b640_author_answers.txt), the first a head meets in this order:',
         '###   DOMAIN: a predicate of Mathlib`s (its declaration outside every kernel) that every row resting on it applies to a variable the row`s '
         'statement quantifies -- not a premise; removed to the domain-condition list below with its variables named.',
         '###   DISCHARGED: a construction outside the SaltCheck files a proof consumes -- an inline have / let / show inside a proof, or a '
         'declaration concluding the head with no Prop hypothesis whose name another declaration uses, outside SaltCheck and AxiomCheck files, the '
         'consumer not itself a witness (its name marking a witness: %s).' % K.WITNESS_NAME,
         '###   CITED: every field T1-lit (the docstring carries T1-lit and no other tier mark).',
         '###   WITNESSED: constructions outside the salt checks, none consumed -- non-vacuity shown, nothing discharged.',
         '###   OPEN: otherwise, a head constructed inside the salt checks alone among them; each takes its work-order (Component 3).',
         '### the kernels read at the commits the terminal table read each head`s rows at; relay %s.' % g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), '']
    for st in K.STATUSES5:
        xs = [x for x in res if x['status'] == st]
        L.append('### ### **%s : %d heads ; rule rows %d ; rule-elab rows %d**' % (st, len(xs), rr[st], er[st]))
        for x in xs:
            L.append('  %-28s rule %2d elab %2d | b639 %-20s -> %-10s | meets %s | salt-check column: %s' % (
                x['head'], x['rule'], x['elab'], x['was'], st, ' / '.join(x['meets']),
                ('%d witness(es), %s' % (len(x['salt']), ', '.join('%s :%d' % (d['file'].split('/')[-1], d['line']) for d in x['salt'][:3]))) if x['salt'] else 'none'))
            if x['was'] != st:
                L.append('      the move: %s -> %s, %s' % (x['was'], st, reason[st]))
            if st == 'DOMAIN':
                L.append('      domain condition, its quantified variables per row: %s' % '; '.join(
                    '%s (%s)' % (r.split(' ', 1)[1].split('.')[-1], ', '.join(v) or '-') for r, v in zip(x['rule_rows'], x['domain_vars'])))
            for d in x['consumed'][:3]:
                L.append('      consumed: %s %s :%d -- used at %s' % (d['name'], d['file'], d['line'], ', '.join('%s (in %s)' % c for c in d['consumers'][:3])))
            for d in x['inline'][:2]:
                L.append('      inline: %s :%d -- %s' % (d['file'], d['line'], d['text'][:110]))
            if st == 'WITNESSED':
                L.append('      standalone, consumed by nothing: %s' % ', '.join('%s (%s :%d)' % (d['name'], d['file'], d['line']) for d in x['standalone']))
            if x['cited_lines']:
                L.append('      cited: %s%s' % (x['cited_lines'][0][:160], (' ; other tier marks %s' % x['other_tiers']) if x['other_tiers'] else ''))
            if x['handread9']:
                L.append('      b639`s hand-read beside: %s' % x['handread9'])
        L.append('')
    L += ['### THE DOMAIN-CONDITION LIST (removed from the premise table): %s' % ', '.join(x['head'] for x in res if x['status'] == 'DOMAIN'),
          '### the four Mathlib predicates (R250)(2) names: %s' % four,
          '### the figure put to the author with the answer (%s) against the tool`s (%s): %s' % (K.FIGURE5, dict(cnt), 'EQUAL' if figure else '### DIFFERS'),
          '### moves from b639`s read: %d' % sum(1 for x in res if x['was'] != x['status']), '',
          '### ### **HEADS %d ; OPEN %d ; CITED %d ; DISCHARGED %d ; WITNESSED %d ; DOMAIN %d -- RULE ROWS %d / %d / %d / %d / %d. H74a %s.**' % (
              len(res), cnt['OPEN'], cnt['CITED'], cnt['DISCHARGED'], cnt['WITNESSED'], cnt['DOMAIN'], rr['OPEN'], rr['CITED'], rr['DISCHARGED'],
              rr['WITNESSED'], rr['DOMAIN'], 'HOLDS' if h74a else 'REFUTED')]
    put_txt('b640_premise_status.txt', L)
    put_json('b640_premise_status.json', dict(at=utc(), heads=res, counts=dict(cnt), rule_rows=dict(rr), elab_rows=dict(er), four=four,
                                              h74a='HOLDS' if h74a else 'REFUTED', figure_equal=figure))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R250)(1)-(2)
W_HEAD = ('*Appended 2026-10-08 by b640 to b639’s entry (:%d), under `(R250)`(1) and (2) -- b639 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS, '
          'AND WHY THE DESCRIPTION HELD:*')
F_HEAD = ('*Appended 2026-10-08 by b640 beneath the domain-condition criterion (:%d), under `(R250)`(3) and the author’s answers before b640’s '
          'seal -- THE PREMISE STATUS AT FIVE, A CLAUSE:*')


def _weight():
    Z, S9, F9, M9, A9 = (jl(n_) for n_ in ('b639_zenodo.json', 'b639_scores.json', 'b639_deposit_files.json', 'b639_mirror.json', 'b639_act_root.json'))
    rd_ = Z.get('read') or {}
    post = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b639_checks_postpush.txt'))
    PS9 = jl('b639_premise_status.json')
    c, r = PS9.get('counts') or {}, PS9.get('rule_rows') or {}
    kinds = collections.Counter(x['kind'].split(' ')[0].rstrip(',') for x in F9.get('files') or [])
    nopen = sum(1 for x in PS9.get('heads') or [] if x['status'] == 'OPEN')
    nowo = sum(1 for x in PS9.get('heads') or [] if x['status'] == 'OPEN' and not x['wo_lines'])
    return ('\n%s the draft %s, a new version %s of record %s, unsubmitted, its reserved DOI %s; %d files -- %d replaced by their current '
            'editions, %d inherited byte-identical, %d added -- all read back with the bank’s sha256 (H73a %s); the description read back with %d '
            'curly quotes straightened by the service and nothing else differing (H73b refuted in letter, the service’s); the no-disclosure arm '
            'at 0 (H73c %s); the status print %d discharged in kernel, %d elsewhere, %d cited, %d open (rule rows %d / %d / %d / %d), the '
            'prompt’s prototype figure 20 / 28 / 2 beside it, the docstring misread the seat’s; H73e refuted in the author’s reading, %d of the %d '
            'open heads with no work-order, printed. The author’s word hold; the draft left unsubmitted; the publish step refusing without the '
            'word. The mirror %s (md5 %s…, %s files, the census at v0.6 in it) built after the Component 1 push and before the draft. FINDINGS '
            ':7883, :7885; OPEN_TRAILS :13395, :13397, :13399, :13427. Relay 8f517800; PLACE-papers 344fc92; the root %s…; the suite %s of %s by '
            'the seat’s (d) and (e), each claim holding; defects (a)-(e) the seat’s; four network bursts kept as attempts. WHY THE DESCRIPTION '
            'HELD, the navigator’s reading and the author’s word: its assumption section listed four general predicates of Mathlib’s (IsOpen, '
            'IsRoot, Prime, StrictMono) among the open assumptions, where each restricts a variable its lemma quantifies; six heads among the '
            'discharged with the sentence beside them that they have only a concrete witness, where a witness discharges nothing; and %d open '
            'heads without a work-order. The opening, the claim ceiling, the located clause, the machine-verified section with its two ERRATA '
            'notes, the files with their digests and the chain through b638 stand as written. Nothing published; no kernel source touched.\n' % (
                W_HEAD % K.B639_ENTRY, rd_.get('id'), K.VERSION, K.RECORD, '10.5281/zenodo.' + str(rd_.get('id')), len(F9.get('files') or []),
                kinds.get('REPLACED', 0), kinds.get('INHERITED', 0), kinds.get('ADDED', 0), (S9.get('H73a') or ['?'])[0], 52, (S9.get('H73c') or ['?'])[0],
                c.get('DISCHARGED IN KERNEL', 0), c.get('DISCHARGED ELSEWHERE', 0), c.get('CITED', 0), c.get('OPEN', 0), r.get('DISCHARGED IN KERNEL', 0),
                r.get('DISCHARGED ELSEWHERE', 0), r.get('CITED', 0), r.get('OPEN', 0), nowo, nopen, os.path.basename(M9.get('zip') or ''),
                (M9.get('zip_md5') or '?')[:8], M9.get('files'), (A9.get('root') or '?')[:8], post.group(2) if post else '?', post.group(1) if post else '?', nowo))


def _five_clause():
    return ('\n%s a head of the premise table takes one of five statuses, computed from the kernels and not assigned by hand, the first it meets in '
            'this order: DOMAIN, a predicate of Mathlib’s that every row resting on it applies to a variable the row’s statement quantifies -- a '
            'domain condition under clause (iii) above, not a premise, removed from the premise table to the domain-condition list with its '
            'variables named; a predicate the kernel itself defines carries the programme’s own content whatever its shape and goes through the '
            'statuses below; DISCHARGED, the hypothesis of an internal lemma handed to it where a proof uses it -- an inline construction, or a '
            'declaration concluding the head with no hypothesis of its own whose name a proof that is not a witness’s uses; CITED, every field '
            'cited T1-lit, the status of a bundle being its weakest field’s; WITNESSED, constructions outside the salt checks and none consumed, '
            'non-vacuity shown and nothing discharged; OPEN otherwise, a premise of the programme’s own with no construction outside the salt '
            'checks and no citation of every field, a head constructed inside the salt checks alone among them, each with its work-order. The '
            'difference between DISCHARGED and WITNESSED is read from the use site. The letter of `(R250)`(3) -- the kernel’s predicates among the '
            'DOMAIN heads, and a salt-check-only head under both OPEN and WITNESSED -- is corrected to these words by the author’s answers, the '
            'navigator’s drafting; the record carries the salt-check column beside every head, non-vacuity and openness being two facts. The '
            'shared tool is relay tools/premise_status.py, its test tools/test_premise_status.py.\n' % (F_HEAD % K.CRITERION))


def record_lines(*a):
    """### Component 1, (R250)(1)-(2): FINDINGS, b639 at its weight with the reading of (2) (to :7885); OPEN_TRAILS, the five-status clause
    ### beneath the criterion (:12955)."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The deposit draft at 23228113')
    if entry != K.B639_ENTRY:
        sys.exit('### b639`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B639_ENTRY, _weight()), ('OPEN_TRAILS.md', F_HEAD % K.CRITERION, _five_clause())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(items[1][2], 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None') if x in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backtick parity odd in: %s ; unread figures: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    _land(Q, items, 'b640_record_lines.json', K.B639_ENTRY)


# ================================================================================ COMPONENT 3: THE WORK-ORDERS, (R250)(4)
WO_HEAD = ('*Appended 2026-10-08 by b640 beneath the five-status clause, under `(R250)`(4) -- THE OPEN PREMISES, ONE WORK-ORDER EACH, PRICED, NOT '
           'STARTED, TRIGGER THE AUTHOR’S WORD:*')


def wo_name(h):
    return 'W-ORD-PREMISE-' + re.sub(r'[^A-Za-z0-9]+', '-', h).strip('-').upper()


def _route(x):
    if x['head'] == 'EpsteinPremises':
        return ('its count field the open part (T3, the local count read off the bench’s zero list) -- a compiled count or a citation of it; its '
                'ef field cited T1-lit (the explicit formula from the literature, Weil 1952 and Bombieri-Lagarias 1999)')
    if x['salt']:
        return 'a construction where a proof uses it (its salt checks show it is not vacuous), a vendored theorem that proves it, or a citation of every field'
    if x['other_tiers'] or x['cited_lines']:
        return 'a citation of every field, or a compiled proof of the fields not cited'
    return 'a compiled proof in its kernel, a vendored theorem that proves it, or a citation of every field'


def _wo_text():
    S = jl('b640_premise_status.json')
    op = [x for x in S.get('heads') or [] if x['status'] == 'OPEN']
    lines = []
    for x in op:
        if x['head'] in K.CARRIED_WO:
            continue
        d = x.get('decl') or {}
        rows = [r.split(' ', 1)[1].split('.')[-1] for r in x['rule_rows']]
        lines.append('- **%s**: the premise %s, %s %s :%s at %s; the rows resting on it (%d): %s; what would discharge it: %s.' % (
            wo_name(x['head']), x['head'], ', '.join(x['kernels']), d.get('file', '(its declaration)'), d.get('line', '-'), ', '.join(x['pins']),
            len(rows), ', '.join(rows), _route(x)))
    cross = ['%s (%s, OPEN_TRAILS :%d)' % (h, w, ln) for h, (w, ln) in sorted(K.CARRIED_WO.items()) if any(x['head'] == h for x in op)]
    t = ('\n%s each open premise of the programme’s own, by the five statuses (relay data/b640_premise_status.txt), takes the line below, '
         'naming the premise, its kernel and pin, the rows resting on it and what would discharge it; the heads already carried by a work-order '
         'are cross-referenced and not duplicated -- %s.\n\n%s\n' % (WO_HEAD, '; '.join(cross), NL.join(lines)))
    return t, op, lines, cross


def workorders(*a):
    """### Component 3, (R250)(4): one work-order line per OPEN head not already carried, appended to OPEN_TRAILS in one block; H74b scored."""
    Q = R2._Q()
    t, op, lines, cross = _wo_text()
    named = [x['head'] for x in op if x['head'] in K.CARRIED_WO or ('**%s**' % wo_name(x['head'])) in t]
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'workorders')
    ticks = t.count('`') % 2
    h74b = len(named) == len(op) and len(op) > 0
    print('  OPEN heads %d ; work-orders written %d ; cross-referenced %d ; without %s ; table cells %s ; nd %s ; scanner %s ; odd backticks %s' % (
        len(op), len(lines), len(cross), sorted(set(x['head'] for x in op) - set(named)) or 'NONE', cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', bool(ticks)))
    if DRY:
        print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or not h74b:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR ODD BACKTICKS, OR A HEAD IS LEFT WITHOUT ITS LINE -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, WO_HEAD)
    r = Q.append_to(Q.OT, t)
    ln = Q.line_of(Q.OT, WO_HEAD)
    L = ['b640 -- COMPONENT 3, (R250)(4): THE OPEN PREMISES` WORK-ORDERS (%s)' % utc(), '', '### the block at OPEN_TRAILS :%s' % ln,
         '### OPEN heads %d ; new work-order lines %d ; cross-referenced to an existing work-order %d (%s)' % (len(op), len(lines), len(cross), '; '.join(cross)),
         '### OPEN heads without a work-order after the block: %s' % (sorted(set(x['head'] for x in op) - set(named)) or 'NONE'), ''] + \
        ['  ' + l for l in lines] + ['', '### ### **OPEN %d ; WITH A WORK-ORDER %d ; WITHOUT %d. H74b %s.**' % (
            len(op), len(named), len(op) - len(named), 'HOLDS' if h74b else 'REFUTED')]
    put_txt('b640_workorders.txt', L)
    put_json('b640_workorders.json', dict(at=utc(), line=ln, append=r, open=len(op), lines=len(lines), cross=cross, named=named,
                                          h74b='HOLDS' if h74b else 'REFUTED', names=[wo_name(x['head']) for x in op if x['head'] not in K.CARRIED_WO]))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE DESCRIPTION RECOMPOSED, (R250)(5)
def _paras(html):
    return re.findall(r'<p>(.*?)</p>', html, re.S)


def _straight(t):
    return t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def _assume_para(old):
    """### the assumption section from the five-status bank: its first sentences (the table, the grades, the premise, the provenance, the census`s
    ### own sum) carried as b639 wrote them, the status sentences rewritten in (R250)(5)`s order."""
    S, W = jl('b640_premise_status.json'), jl('b640_workorders.json')
    by = collections.defaultdict(list)
    for x in S.get('heads') or []:
        by[x['status']].append(x)
    cut = old.find(' Its 50 premise heads are classed here by status')
    head = old[:cut] if cut > 0 else old
    nm = lambda xs: ', '.join(x['head'] for x in xs)   # noqa: E731
    dom = '; '.join('%s (restricting %s)' % (x['head'], ', '.join(sorted(set(v for vs in x['domain_vars'] for v in vs))) or '-') for x in by['DOMAIN'])
    wo = len(W.get('named') or [])
    return (head + ' Read at their pins with five statuses computed from the kernels and not assigned by hand (relay data/b640_premise_status.txt), '
            "the kernels' INTERFACES rows rest on %d open premises of the programme's own, each with its work-order on OPEN_TRAILS (%d of %d) -- %s; "
            '%d cited theorems -- %s; %d hypotheses of internal lemmas discharged where they are used -- %s; %d premises shown non-vacuous by a '
            'witness and not discharged -- %s; and %d domain conditions of general lemmas, which are not assumptions and are listed apart: '
            "Mathlib's predicates restricting a variable the statement quantifies -- %s. A premise is open when no proof in the kernels constructs "
            'it outside a salt check, a file that only shows a premise is not vacuous, and no citation covers every field; it is discharged when a '
            'proof that uses the lemma builds it; it is witnessed when the kernel builds a concrete instance that nothing uses. The census prints this '
            'status column at its next edition, v0.7, pending the author\'s word.' % (
                len(by['OPEN']), wo, len(by['OPEN']), nm(by['OPEN']), len(by['CITED']), nm(by['CITED']), len(by['DISCHARGED']), nm(by['DISCHARGED']),
                len(by['WITNESSED']), nm(by['WITNESSED']), len(by['DOMAIN']), dom))


def _open_para():
    S = jl('b640_premise_status.json')
    op = [x for x in S.get('heads') or [] if x['status'] == 'OPEN']
    carried = ['%s (%s)' % (x['head'], K.CARRIED_WO[x['head']][0]) for x in op if x['head'] in K.CARRIED_WO]
    return ('WHAT REMAINS OPEN. The located clause itself: h2_sign, which no kernel proves and which the theorems that assume it carry as their '
            'premise; it is not among the 50 heads, since the equivalence h2_sign_iff_rh has none. Then the %d open premises above, each with its '
            "work-order on the programme's ledger of open work, OPEN_TRAILS: %s by the work-orders that already carried them, and the other %d each by "
            'its own, named W-ORD-PREMISE- and the premise.' % (len(op), '; '.join(carried), len(op) - len(carried)))


def compose():
    """### the b640 description from the b639 bank: the assumption section and the open section rewritten from the five-status bank, the record`s
    ### note carrying that no claim is added or withdrawn, the root chain`s last line, the mirror`s file line and digest, the composition line;
    ### every other sentence carried; straight quotes throughout. RETURN (html, [(index, old, new, why)])."""
    old = io.open(os.path.join(D, K.B639_DESC), encoding='utf-8').read()
    P = _paras(old)
    new = list(P)
    why = {}
    i_rec = next(i for i, p in enumerate(P) if p.startswith('THE RECORD.'))
    new[i_rec] = P[i_rec].replace(' Nothing in it states that the Riemann Hypothesis holds.',
                                  ' Against v1.1.2, %s. Nothing in it states that the Riemann Hypothesis holds.' % K.NO_CLAIM)
    why[i_rec] = 'the version note: %s ((R250)(5))' % K.NO_CLAIM
    i_as = next(i for i, p in enumerate(P) if p.startswith('WHAT THE KERNELS ASSUME.'))
    new[i_as] = _assume_para(P[i_as])
    why[i_as] = 'the assumption section from the five-status bank ((R250)(5))'
    i_op = next(i for i, p in enumerate(P) if p.startswith('WHAT REMAINS OPEN.'))
    new[i_op] = _open_para()
    why[i_op] = 'the open heads and their work-orders at five statuses (the fact clause: b639`s 29 and 25 no longer hold)'
    i_ce = next(i for i, p in enumerate(P) if p.startswith('THE CENSUS, THE ROOT CHAIN'))
    roots = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()]
    last = roots[-1].split()
    new[i_ce] = re.sub(r'its last line at this description b\d{3} [0-9a-f]+…; the act root of this act, b\d{3},',
                       'its last line at this description %s %s…; the act root of this act, b640,' % (last[0], last[1][:16]), P[i_ce])
    why[i_ce] = 'the root chain`s last line at this description, b639`s (the fact clause)'
    i_fi = next(i for i, p in enumerate(P) if p.startswith('THE FILES'))
    M = jl('b640_mirror.json')
    if M.get('zip_sha256'):
        new[i_fi] = re.sub(r'mirror-refresh-[0-9-]+-b\d{3}\.zip \(the mirror: the (\d+) files', '%s (the mirror: the %s files' % (
            os.path.basename(M['zip']), M.get('files')), P[i_fi])
        new[i_fi] = re.sub(r'(mirror builder; sha256 )[0-9a-f]{64}', r'\g<1>' + M['zip_sha256'], new[i_fi])
        why[i_fi] = 'the mirror rebuilt after this act`s last push: its name and digest ((R250)(7))'
    i_th = next(i for i, p in enumerate(P) if p.startswith('THIS DESCRIPTION'))
    new[i_th] = ("THIS DESCRIPTION was composed at the programme's act b640, an act being one numbered session of the programme's work under the "
                 "author's ruling (b639 the act before it, which composed its first form), from relay data/b639_deposit_items.txt, "
                 'data/b640_premise_status.txt and data/b639_deposit_files.txt with the mirror of data/b640_mirror.txt, and is banked as '
                 'data/%s (github.com/psinary-sketch/relay).' % K.DESC)
    why[i_th] = 'the composition line'
    new = [_straight(p) for p in new]
    html = ''.join('<p>%s</p>' % p for p in new)
    ch = []
    for i, (a, b) in enumerate(zip(P, new)):
        if a != b:
            ch.append((i, a, b, why.get(i, 'straight quotes only' if _straight(a) == b else '### AN UNDECLARED CHANGE')))
    return html, ch


def describe(*a):
    """### data/b640_deposit_description.txt (the HTML exactly as it goes to the service) and data/b640_description_scan.txt with its json: the
    ### paragraph diff against the b639 bank, each change with its reason; the scanner, the glossary-key scan and the no-disclosure arm."""
    html, ch = compose()
    if '’' in html or '“' in html or '”' in html:
        sys.exit('### A CURLY QUOTE SURVIVES -- NOTHING WRITTEN')
    R9.DESC_TERMS = R9.DESC_TERMS + ('Mathlib', 'INTERFACES')
    sc = _desc_scan(html)
    p = os.path.join(SP if DRY else D, K.DESC)
    _write(p, html.encode('utf-8'))
    undecl = [c for c in ch if c[3].startswith('###')]
    L = ['b640 -- COMPONENT 4, (R250)(5): THE DESCRIPTION RECOMPOSED FROM THE FIVE-STATUS BANK, ITS DIFF AGAINST b639`s BANK AND ITS SCANS (%s)' % utc(), '',
         '### the bank: data/%s, %d bytes, sha256 %s ; b639`s data/%s sha256 %s' % (
             K.DESC, len(html.encode('utf-8')), hashlib.sha256(html.encode('utf-8')).hexdigest(), K.B639_DESC,
             hashlib.sha256(open(os.path.join(D, K.B639_DESC), 'rb').read()).hexdigest()),
         '### paragraphs changed %d of %d ; their reasons:' % (len(ch), len(_paras(html)))]
    for i, a_, b_, w in ch:
        L.append('  paragraph %d (%s): %s' % (i + 1, b_[:40], w))
        if not w.startswith('straight'):
            for x in difflib.unified_diff(_straight(a_).split('. '), b_.split('. '), lineterm='', n=0):
                if x[:1] in '+-' and x[:3] not in ('+++', '---'):
                    L.append('      %s' % x[:400])
    L += ['### undeclared changes: %s' % (undecl or 'NONE'),
          '### the scanner: %s ; names undefined: %s ; markup outside the tags: %s ; the no-disclosure arm: %s' % (
              'CLEAN' if sc['clean'] else '### NOT CLEAN', sc['undefined'] or 'NONE', sc['markup'] or 'NONE', sc['nd']), '',
          '### ### **DESCRIPTION %d BYTES ; PARAGRAPHS CHANGED %d ; UNDECLARED %d ; SCANNER %s ; UNDEFINED %d ; NO-DISCLOSURE %d.**' % (
              len(html.encode('utf-8')), len(ch), len(undecl), 'CLEAN' if sc['clean'] else 'NOT CLEAN', len(sc['undefined']), sum(sc['nd'].values()))]
    put_txt('b640_description_scan.txt', L)
    put_json('b640_description_scan.json', dict(at=utc(), sha256=hashlib.sha256(html.encode('utf-8')).hexdigest(), bytes=len(html.encode('utf-8')),
                                                changed=[[i, w] for i, _a, _b, w in ch], undeclared=len(undecl), clean=sc['clean'],
                                                undefined=sc['undefined'], markup=sc['markup'], nd=sc['nd']))
    print(L[-1])


def _desc_scan(html):
    import b616_record as R6
    raw_text = re.sub(r'</?p>', NL, html)
    markup = [m.group(0) for m in re.finditer(r'[<>]|&(?!(amp|lt|gt);)', raw_text)]
    text = HT.unescape(raw_text)
    keys = list(R9._gl())
    decl = set(r['name'].split('.')[-1] for r in _table()) | set(r['name'] for r in _table())
    heads = set(x['head'] for x in jl('b640_premise_status.json').get('heads') or [])
    paths = ' '.join(re.findall(r'[\w./-]+\.(?:md|txt|html|svg|json|zip|lean)\b', text))
    names = sorted(set(m.group(0).strip('`') for p in R8.NAME_PATS for m in re.finditer(p, text)))

    def kernel_declares(n):
        return any(subprocess.run(['git', '-C', rp, 'grep', '-q', '-w', n, pin, '--', '*.lean']).returncode == 0
                   for rp, pin in ((K.EF, K.EF_PIN), ('D:/SIDE-kernel', 'v1.5')))

    def ok(n):
        return (any(n in k or (k in n and len(k) > 1) for k in keys) or any(n in t or t in n for t in R9.DESC_TERMS) or n in heads or n in decl
                or n.split('.')[-1] in decl or re.match(r'^v\d', n) is not None or re.match(r'^E-\d{4}-\d\d-\d\d-\d+$', n) is not None
                or re.match(r'^b\d{3}$', n) is not None or n.startswith('W-ORD-')
                or (n in paths and re.search(r'[\w./-]*%s[\w./-]*\.\w+' % re.escape(n), paths) is not None))
    undefined = [n for n in names if not ok(n)]
    undefined = [n for n in undefined if not (re.search(r'[a-z]_[a-z]|[a-z][A-Z]', n) and kernel_declares(n))]
    p = os.path.join(SP if DRY else D, 'b640_scanfile_description.md')
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    nd = R6.nd_hits(text, R6.nd_sets())[0]
    return dict(names=names, undefined=undefined, markup=markup, clean=_clean(out), nd=dict(nd))


# ================================================================================ COMPONENT 5: THE LEGIBILITY READER, (R250)(6)
LEAD = ('Reader task follows. The packet is at C:\\reader_b640\\packet\\ and your answers go to C:\\reader_b640\\answers.txt. Read only the two '
        'packet files. Do not open any other file on this machine, do not run any command, and do not search the web. Write the answers file, '
        'report that it is written, and stop.')
ONE_LINER = ('Get-Content C:\\reader_b640\\full_prompt.txt -Raw | claude -p --output-format json --allowedTools Read Glob Write --disallowedTools '
             'Bash PowerShell WebFetch WebSearch --permission-mode acceptEdits --setting-sources user --strict-mcp-config > '
             'C:\\reader_b640\\reader_run.log 2> C:\\reader_b640\\reader_run.err')
READER_PROMPT = ('The legibility packet is at C:\\reader_b640\\packet\\ and the prompt at C:\\reader_b640\\full_prompt.txt. Run the reader from a '
                 'directory off D:\\ as at b632; it writes C:\\reader_b640\\answers.txt and closes; then answer here that the bank is there.')


def _plain(html):
    return NL.join(HT.unescape(p) for p in _paras(html)).replace(NL, NL + NL)


def _task():
    return (LEAD + NL + NL +
            'You are an independent reader. You know nothing of the research programme the packet describes, and that is the point. The packet has '
            'two files: description.txt, the description a public deposit of the programme carries, and questions.txt, three questions. Read the '
            'description and answer each question in your own words, from the description alone, in a few sentences each: say what the text says, '
            'not what you know of the mathematics, and say plainly where the text is unclear to you. Write the file C:\\reader_b640\\answers.txt with '
            'exactly three sections, headed ANSWER 1:, ANSWER 2: and ANSWER 3:, each followed by your answer to that question; then a fourth section '
            'headed UNCLEAR: listing any sentence of the description you could not follow, or the word none. Then stop.')


def packet(*a):
    """### the reader's packet staged off D:\\ (C:/reader_b640: packet/description.txt, packet/questions.txt, lead.txt, full_prompt.txt) and its
    ### copy banked in relay (data/b640_reader_packet/, data/b640_reader_prompt.txt); the no-disclosure arm over it; the hold's text printed."""
    import b616_record as R6
    html = open(os.path.join(D, K.DESC), 'rb').read().decode('utf-8')
    desc = _plain(html)
    qs = NL.join('%d. %s' % (i + 1, q) for i, q in enumerate(K.QUESTIONS))
    task = _task()
    nd = R6.nd_hits(desc + NL + qs + NL + task, R6.nd_sets())[0]
    if any(nd.values()):
        sys.exit('### THE PACKET WOULD CARRY TECHNE TEXT -- NOTHING WRITTEN')
    pdir = os.path.join(SP if DRY else D, 'b640_reader_packet')
    os.makedirs(pdir, exist_ok=True)
    for n_, t_ in (('description.txt', desc), ('questions.txt', qs)):
        _write(os.path.join(pdir, n_), (t_ + NL).encode('utf-8'))
    _write(os.path.join(SP if DRY else D, 'b640_reader_prompt.txt'), (task + NL).encode('utf-8'))
    if not DRY:
        rdir = K.READER_DIR
        if os.path.exists(rdir) and os.listdir(rdir):
            sys.exit('### %s EXISTS AND IS NOT EMPTY -- THE READER`S DIRECTORY NOT WRITTEN' % rdir)
        os.makedirs(rdir + '/packet', exist_ok=True)
        for n_, t_ in (('packet/description.txt', desc), ('packet/questions.txt', qs), ('lead.txt', LEAD), ('full_prompt.txt', task)):
            _write(os.path.join(rdir, n_), (t_ + NL).encode('utf-8'))
    L = ['b640 -- COMPONENT 5, (R250)(6): THE LEGIBILITY PACKET, STAGED OFF D:\\ (%s)' % utc(), '',
         '### staged: %s (packet/description.txt %d bytes, packet/questions.txt, lead.txt, full_prompt.txt) ; banked: relay data/b640_reader_packet/, '
         'data/b640_reader_prompt.txt' % (K.READER_DIR, len(desc.encode('utf-8'))),
         '### the description, plain text from data/%s, sha256 %s' % (K.DESC, hashlib.sha256((desc + NL).encode('utf-8')).hexdigest()),
         '### the questions: %s' % ' / '.join(K.QUESTIONS), '### the no-disclosure arm over the packet and the prompt: %s' % dict(nd), '',
         '### THE HOLD, verbatim: %s' % READER_PROMPT, '### the command, beneath it:', '    cd C:\\reader_b640', '    ' + ONE_LINER]
    put_txt('b640_reader_packet.txt', L)
    print(NL.join(L[-5:]))


ANS_RE = re.compile(r'^ANSWER ([123]):\s*(.*?)(?=^ANSWER [123]:|^UNCLEAR:|\Z)', re.M | re.S)
NEEDLES = {
    1: ((r'reduc|equivalen|located clause|single clause|one clause', 'the claim: a reduction of RH to one located clause, machine-verified'),
        (r'(?<!not )(?<!n.t )\bproved?\b.{0,40}\bRiemann Hypothesis\b|\bRH (is|was|has been) proved\b', 'NOT the claim: RH proved')),
    2: ((r'premise|assum|hypothes', 'the assumptions: premises the kernels take'),
        (r'\b25\b|twenty-five|open premises|work-order', 'the open premises counted, with their work-orders')),
    3: ((r'h2_sign|located clause|positivity|sign statement', 'the open clause itself: h2_sign'),
        (r'premise|work-order|open', 'the open premises beside it')),
}


def reader(*a):
    """### on the author's answer: the reader's answers copied from off D:\\ into relay data/b640_reader_answers.txt, each compared to the
    ### description's own sentences by the needles above (each answer must carry what its question's sentences say and nothing they deny), agree /
    ### differ printed with the reader's lines; data/b640_reader_compare.txt and its json, H74c scored where every answer agrees."""
    src = K.READER_ANSWERS
    if not os.path.exists(src):
        sys.exit('### %s IS ABSENT -- NOTHING READ' % src)
    t = io.open(src, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    _write(os.path.join(SP if DRY else D, 'b640_reader_answers.txt'), t.encode('utf-8'))
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in ANS_RE.finditer(t))
    unclear = re.search(r'^UNCLEAR:\s*(.*)\Z', t, re.M | re.S)
    log = os.path.join(K.READER_DIR, 'reader_run.log')
    mem = 'unread'
    if os.path.exists(log):
        lg = io.open(log, encoding='utf-8', errors='replace').read()
        mem = 'memory named in the run log: %s' % bool(re.search(r'MEMORY\.md|memory/', lg))
    L = ['b640 -- COMPONENT 5, (R250)(6): THE READER`S ANSWERS COMPARED TO THE DESCRIPTION`S OWN SENTENCES (%s)' % utc(), '',
         '### the answers: relay data/b640_reader_answers.txt, copied from %s ; the reader`s session: %s' % (src, mem), '']
    res = {}
    for q in (1, 2, 3):
        a_ = ans.get(q, '')
        must, then = NEEDLES[q]
        if q == 1:
            ok = bool(re.search(must[0], a_, re.I)) and not re.search(then[0], a_, re.I)
            reasons = ['%s %s' % (must[1], bool(re.search(must[0], a_, re.I))), '%s absent %s' % (then[1], not re.search(then[0], a_, re.I))]
        else:
            ok = bool(re.search(must[0], a_, re.I)) and bool(re.search(then[0], a_, re.I))
            reasons = ['%s %s' % (must[1], bool(re.search(must[0], a_, re.I))), '%s %s' % (then[1], bool(re.search(then[0], a_, re.I)))]
        res[q] = dict(question=K.QUESTIONS[q - 1], answer=a_, agree=ok, reasons=reasons)
        L += ['### QUESTION %d: %s' % (q, K.QUESTIONS[q - 1]), '    the reader: %s' % (a_ or '### NO ANSWER'),
              '    against the description: %s ; ### %s' % ('; '.join(reasons), 'AGREE' if ok else 'DIFFER'), '']
    k = sum(1 for v in res.values() if v['agree'])
    L += ['### UNCLEAR, the reader`s: %s' % (' '.join(unclear.group(1).split())[:1200] if unclear else '### NONE GIVEN'), '',
          '### ### **AGREE %d OF 3.**' % k]
    put_txt('b640_reader_compare.txt', L)
    put_json('b640_reader_compare.json', dict(at=utc(), answers=res, agree=k, unclear=(unclear.group(1).strip() if unclear else None)))
    print(L[-1])


# ================================================================================ COMPONENT 6: THE MIRROR, AFTER THE LAST PUSH AND BEFORE THE DRAFT'S UPDATE
ZIP = K.MIRROR_ZIP
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % K.MIRROR_TAG)


def mbuild(*a):
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag', K.MIRROR_TAG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b640_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b639':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b639`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b640_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b640_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-600:])


def mbank(*a):
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rd('b640_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    head = next((l for l in ls if l.startswith('Source: PLACE-papers @')), '')
    files_ = [n for n in names if n != 'MANIFEST.md']
    L = ['b640 -- THE MIRROR, BUILT AFTER THE ACT`S LAST PUSH AND BEFORE THE DRAFT`S UPDATE BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), hashlib.md5(zb).hexdigest(), hashlib.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (hashlib.md5(man).hexdigest(), len(names), len(files_)),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SOURCE LINE : %s' % head, '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b640_mirror.txt', L)
    put_json('b640_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=hashlib.md5(zb).hexdigest(), zip_sha256=hashlib.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=hashlib.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), source=head,
                                      census6='THE_KEYSTONE_CENSUS_v0_6.md' in names))
    for l in L[:8]:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE DRAFT UPDATED THROUGH THE ROUTE, (R250)(7)
ZRES = 'b640_zenodo.json'


def _zres():
    return jl(ZRES)


def _zmerge(cells):
    Rz = _zres()
    Rz.update(cells)
    put_json(ZRES, Rz)


def files(*a):
    """### b639's file bank with the mirror's entry replaced by this act's zip: data/b640_deposit_files.json and its text."""
    F = jl('b639_deposit_files.json')
    M = jl('b640_mirror.json')
    if not M.get('zip_sha256'):
        sys.exit('### NO MIRROR BANKED -- NOTHING WRITTEN')
    out = []
    for x in F.get('files') or []:
        if x['name'] == K.MIRROR_PREV_NAME:
            zb = open(K.MIRROR_ZIP, 'rb').read()
            x = dict(x, name=os.path.basename(K.MIRROR_ZIP), source=K.MIRROR_ZIP, sha256=hashlib.sha256(zb).hexdigest(), md5=hashlib.md5(zb).hexdigest(),
                     size=len(zb), replaces=K.MIRROR_PREV_NAME)
        out.append(x)
    L = ['b640 -- THE DRAFT`S FILE LIST: b639`s, the mirror`s zip replaced by this act`s (%s)' % utc(), ''] + [
        '  %-46s sha256 %s ; md5 %s ; %s bytes%s' % (x['name'], x['sha256'], x['md5'], x['size'], (' ; replaces %s' % x['replaces']) if x.get('replaces') else '')
        for x in out] + ['', '### ### **FILES %d ; REPLACED THIS ACT 1.**' % len(out)]
    put_txt('b640_deposit_files.txt', L)
    put_json('b640_deposit_files.json', dict(at=utc(), files=out, pp_head=F.get('pp_head')))
    print(L[-1])


def z_update(*a):
    """### the route's update of draft 23228113, one step: the files listed once; the b639 zip deleted and this act's uploaded to the bucket; the
    ### metadata read once and PUT once with the description the bank's bytes, every other key carried; nothing published."""
    if not _tok():
        sys.exit('### THE TOKEN IS NOT SET -- NO CALL MADE')
    if _zres().get('update'):
        sys.exit('### THE UPDATE HAS RUN -- IT DOES NOT RUN TWICE')
    base = '%s/deposit/depositions/%s' % (K.API, K.DRAFT)
    st, b = http('GET', base)
    d = _j(b) or {}
    if st != 200 or d.get('submitted') or str(d.get('id')) != K.DRAFT:
        sys.exit('### THE DRAFT IS NOT AN UNSUBMITTED %s (HTTP %d) -- NOTHING DONE' % (K.DRAFT, st))
    bucket = (d.get('links') or {}).get('bucket')
    have = dict((f.get('filename'), f) for f in d.get('files') or [])
    L = ['b640 -- THE (R110) ROUTE, THE DRAFT`S UPDATE (%s)' % utc(), '', '### GET the draft : HTTP %d ; state %s ; submitted %s ; %d files' % (
        st, d.get('state'), d.get('submitted'), len(have))]
    calls = []
    if K.MIRROR_PREV_NAME in have:
        sd, _b = http('DELETE', '%s/files/%s' % (base, have[K.MIRROR_PREV_NAME]['id']))
        calls.append(dict(op='DELETE', name=K.MIRROR_PREV_NAME, status=sd))
        L.append('    DELETE %s : HTTP %d' % (K.MIRROR_PREV_NAME, sd))
    zb = open(K.MIRROR_ZIP, 'rb').read()
    want = next(x for x in jl('b640_deposit_files.json')['files'] if x['name'] == os.path.basename(K.MIRROR_ZIP))
    if hashlib.sha256(zb).hexdigest() != want['sha256']:
        sys.exit('### THE ZIP`S BYTES DIFFER FROM THE BANK`S -- NOT UPLOADED')
    su, bu = http('PUT', '%s/%s' % (bucket, urllib.request.quote(os.path.basename(K.MIRROR_ZIP))), raw=zb)
    ju = _j(bu) or {}
    calls.append(dict(op='PUT', name=os.path.basename(K.MIRROR_ZIP), status=su, checksum=ju.get('checksum')))
    L.append('    PUT    %s : HTTP %d ; the service`s checksum %s' % (os.path.basename(K.MIRROR_ZIP), su, ju.get('checksum')))
    md = dict(d.get('metadata') or {})
    md['description'] = open(os.path.join(D, K.DESC), 'rb').read().decode('utf-8')
    sp, bp = http('PUT', base, body={'metadata': md})
    calls.append(dict(op='PUT metadata', status=sp))
    L.append('    PUT metadata (the description the bank`s; %d keys carried) : HTTP %d' % (len(md), sp))
    if sp != 200:
        L.append('    | %s' % _tclean(bp.decode('utf-8', 'replace'))[:1200])
    bad = [c for c in calls if c['status'] not in (200, 201, 204)]
    L += ['', '### ### **CALLS %d ; FAILED %d ; NOTHING PUBLISHED.**' % (len(calls), len(bad))]
    put_txt('b640_zenodo_update.txt', L)
    _zmerge(dict(update=dict(calls=calls, failed=len(bad), at=utc())))
    print(L[-1])


def z_read(*a):
    """### the draft read back once: identifier, title, version, description and files, every file downloaded and its sha256 computed; compared to
    ### the banks; H74d (the description equal to the bank up to the service's quote straightening) and N4's files scored."""
    base = '%s/deposit/depositions/%s' % (K.API, K.DRAFT)
    st, b = http('GET', base)
    d = _j(b) or {}
    put_json('b640_zenodo_readback.json', d)
    md = d.get('metadata') or {}
    bank = open(os.path.join(D, K.DESC), 'rb').read().decode('utf-8')
    back = md.get('description') or ''
    FL = dict((x['name'], x) for x in jl('b640_deposit_files.json').get('files') or [])
    rows = []
    for f in d.get('files') or []:
        n = f.get('filename')
        sd, bd = http('GET', (f.get('links') or {}).get('download') or '')
        s256 = hashlib.sha256(bd).hexdigest() if sd == 200 else None
        w = FL.get(n)
        rows.append(dict(name=n, md5=f.get('checksum'), get=sd, sha256=s256, ok=bool(w) and s256 == w['sha256']))
    missing = sorted(set(FL) - set(r['name'] for r in rows))
    exact = back == bank
    h74d = _straight(back) == _straight(bank)
    files_ok = bool(rows) and all(r['ok'] for r in rows) and not missing and len(rows) == len(FL)
    dd = []
    if not exact:
        sm = difflib.SequenceMatcher(None, bank, back)
        dd = [(op, bank[i1:i2][:80], back[j1:j2][:80]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal'][:30]
    L = ['b640 -- THE (R110) ROUTE, THE DRAFT READ BACK AFTER ITS UPDATE (%s)' % utc(), '',
         '### GET the draft : HTTP %d ; identifier %s ; state %s ; submitted %s ; title %s ; version %s ; reserved DOI %s' % (
             st, d.get('id'), d.get('state'), d.get('submitted'), md.get('title'), md.get('version'),
             (md.get('prereserve_doi') or {}).get('doi') if isinstance(md.get('prereserve_doi'), dict) else md.get('prereserve_doi')),
         '### the description : %d characters back against the bank`s %d ; byte for byte %s ; equal up to quote straightening %s' % (
             len(back), len(bank), exact, h74d)] + ['    %s : bank %r ; service %r' % x for x in dd] + [
        '### the files (%d read back, %d in the bank):' % (len(rows), len(FL))] + [
        '    %-46s md5 %s ; download HTTP %s ; sha256 %s ; %s' % (r['name'], r['md5'], r['get'], r['sha256'], 'AGREE' if r['ok'] else '### DIFFER')
        for r in rows] + ['### in the bank, not in the draft: %s' % (missing or 'NONE'), '',
                          '### ### **H74d %s ; EVERY FILE AT ITS DIGEST %s. THE DRAFT %s, %d FILES, NOTHING PUBLISHED.**' % (
                              'HOLDS' if h74d else 'REFUTED', files_ok, d.get('id'), len(rows))]
    put_txt('b640_zenodo_read.txt', L)
    _zmerge(dict(read=dict(get=st, id=d.get('id'), state=d.get('state'), submitted=d.get('submitted'), title=md.get('title'), version=md.get('version'),
                           files=rows, missing=missing, exact=exact, h74d=h74d, files_ok=files_ok, n_files=len(rows), at=utc())))
    print(L[-1])
    print(PROMPT % (d.get('id'), len(rows)))


PROMPT = ('The deposit draft is at %s, %d files, description banked at data/b640_deposit_description.txt and read back from the service. '
          'Publishing is yours: answer publish, or hold.')


def _word():
    t = rd('b640_author_answers.txt')
    blk = [b for b in re.split(r'^### CALL ', t, flags=re.M) if 'data/b640_deposit_description.txt and read back from the service' in b]
    if not blk:
        return None
    res = re.search(r'^RESULT \(transcript line \d+\): (.*)', blk[-1], re.M | re.S)
    a_ = (res.group(1) if res else '').split('"="')[-1].lower()
    return 'publish' if re.match(r'\s*publish\b', a_) else ('hold' if re.match(r'\s*hold\b', a_) else None)


def z_hold(*a):
    if _word() != 'hold':
        sys.exit('### THE WORD IS NOT "hold" -- NOTHING DONE')
    st, b = http('GET', '%s/deposit/depositions/%s' % (K.API, K.DRAFT))
    d = _j(b) or {}
    L = ['b640 -- THE DRAFT HELD ON THE AUTHOR`S WORD (%s)' % utc(), '', '### the draft %s : HTTP %d ; state %s ; submitted %s ; nothing published' % (
        K.DRAFT, st, d.get('state'), d.get('submitted'))]
    put_txt('b640_zenodo_hold.txt', L)
    _zmerge(dict(hold=dict(id=K.DRAFT, state=d.get('state'), submitted=d.get('submitted'), at=utc())))
    print(L[-1])


def z_publish(*a):
    """### on the author's word alone: b639's publish step pointed at this act's banks (R249)(4) PART TWO."""
    if _word() != 'publish':
        sys.exit('### THE AUTHOR`S WORD IS %r, NOT "publish" -- NOTHING PUBLISHED' % _word())
    sys.exit('### PUBLISH: run (R249)(4) PART TWO through b639`s steps with this act`s banks -- the seat asks before the call')


# ================================================================================ COMPONENT 7: THE PAGES, THE TABLE, THE ROOT
def page(k, *a):
    CP = R8._cp()
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b640_%s' % k), os.path.join(D, K.PROBE[k]))
    if rc:
        put_json('b640_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b640_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           free_mb_before=fm, seconds=int(time.time() - t0), at=utc()))
    print('  %s : exit %d ; changed against HEAD %s ; diff lines %d ; cells moved %s' % (k, rc, changed, len(dl), gmoved or 'NONE'))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b640 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b640_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; first differing line %s' % (arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'], r['first_diff']))
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
    put_txt('b640_page_arms.txt', L)
    print(NL.join(l[:200] for l in L))


def table(*a):
    rows0 = _table()
    before = R8.R7._table_state(rows0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = _table()
    after = R8.R7._table_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b640 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d' % (utc(), r.returncode), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(rows1), len(added), len(gone), len(moved)),
         '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b640_table_final.txt', L)
    put_json('b640_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b640_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b640_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b640'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b640_act_root.json')
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
    L = ['b640 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s)' % utc(), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b640_root_arm.txt', L)
    put_json('b640_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES AND THE RECORD
HKEYS = ('H74a', 'H74b', 'H74c', 'H74d')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b639_closing_push_out.txt', 'data/act_roots.txt', 'tools/mirror_prevbuild.json', K.STATUS_TOOL, K.STATUS_TEST}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE)


def TRAIL_HEAD():
    return ('### b640 — lane three, act sixty-seven under (R250): the premise status at five and the open premises given work-orders; the deposit '
            'description’s assumption section recomposed and read by a second reader; the draft 23228113 updated and held at the same prompt')


def n5(trail_line=None, *a):
    if isinstance(trail_line, str):
        trail_line = int(trail_line.split('=')[-1])
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
    face = jl('b640_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b640_|audit_b640_)', x) or re.match(r'^data/b640_reader_packet/', x)
                                          or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    Z = _zres()
    word = _word()
    word_ok = not Z.get('publish') or word == 'publish'
    logged = [f for f in os.listdir(D) if f.startswith('b640_') and _tok() and _tok().encode() in open(os.path.join(D, f), 'rb').read()] if _tok() else []
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not differ and word_ok and not logged and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing published before the word %s (the word %s); the token in no bank %s; the kernels unmoved %s; PLACE-papers %s (beyond: %s); %s; '
            'relay beyond the list: %s; sealed tools not agreeing %s; b628`s bank untracked %s; no identifier of the author in any outbound request' % (
                word_ok, word, logged or 'NONE', kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', differ or 'NONE', untracked_local))


def scores(*a):
    PS, W, RC, Z, TF, RA, ST = (jl(n_) for n_ in ('b640_premise_status.json', 'b640_workorders.json', 'b640_reader_compare.json', ZRES,
                                                   'b640_table_final.json', 'b640_root_arm.json', 'b640_tests_stepzero.json'))
    rd_ = Z.get('read') or {}
    tl = [x for x in a if x.startswith('trail_line=')]
    _r, _n, sh = seal_hashes()
    bld = g(RELAY, 'diff', '--name-only', PRE_RELAY, '--', K.BUILDER).strip()
    k_before = (jl('b640_reader_compare_first.json') or RC).get('agree')
    k_after = RC.get('agree')
    reps = jl('b640_reader_repairs.json').get('repairs') or []
    clean_tests = [n for n, x in ST.items() if x.get('rc') == 0 and not x.get('failing')]
    pt = jl('b640_status_test.json')
    S = {
        'H74a': (PS.get('h74a', 'PENDING'), 'the 50 heads at five statuses %s ; the four Mathlib predicates %s' % (PS.get('counts'), PS.get('four'))),
        'H74b': (W.get('h74b', 'PENDING'), 'OPEN heads with a work-order %s of %s' % (len(W.get('named') or []), W.get('open'))),
        'H74c': (('HOLDS' if k_after == 3 else 'REFUTED') if RC else 'PENDING', 'the reader agreeing %s of 3 before repair and %s after ; repairs %d' % (
            k_before, k_after, len(reps))),
        'H74d': (('HOLDS' if rd_.get('h74d') else 'REFUTED') if rd_ else 'PENDING', 'the description back equal up to quote straightening %s ; '
                 'byte for byte %s' % (rd_.get('h74d'), rd_.get('exact'))),
        'N5': n5(int(tl[0].split('=')[1]) if tl else None),
        'S1': (('HELD' if pt.get('rc') == 0 and pt.get('passing') == pt.get('cases') and pt.get('cases', 0) >= 5 else 'REFUTED'),
               'the status tool`s test %s of %s, one planted head per outcome' % (pt.get('passing'), pt.get('cases'))),
        'S2': (('HELD' if ST and len(clean_tests) == len(ST) else 'REFUTED'), 'every test file clean at step zero: %d of %d' % (len(clean_tests), len(ST))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal and the control moving it'),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) and not bld else 'REFUTED'),
               'the sealed tools` hashes %s ; the builder unedited %s' % (dict(collections.Counter(v for _t, v in sh)), not bld)),
    }
    S['N1'] = (('HELD' if S['H74a'][0] == 'HOLDS' else 'REFUTED'), 'as H74a')
    S['N2'] = (('HELD' if S['H74b'][0] == 'HOLDS' else 'REFUTED'), 'as H74b')
    S['N3'] = (('HELD' if (k_before or 0) >= 2 and k_after == 3 else 'REFUTED') if RC else 'PENDING',
               'the reader %s of 3 before repair, %s after' % (k_before, k_after))
    S['N4'] = (('HELD' if rd_.get('h74d') and rd_.get('files_ok') else 'REFUTED') if rd_ else 'PENDING',
               'the description up to quote straightening %s ; every file at its digest %s' % (rd_.get('h74d'), rd_.get('files_ok')))
    put_json('b640_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:260]))


def _title_entry():
    PS, RC, Z = jl('b640_premise_status.json'), jl('b640_reader_compare.json'), _zres()
    c = PS.get('counts') or {}
    pub = Z.get('publish') or {}
    return ('## The premise status at five: %d open with work-orders, %d cited, %d discharged, %d witnessed, %d domain; the deposit description’s '
            'assumption section recomposed and read by a second reader, %s of 3 agreeing; the draft 23228113 updated and %s' % (
                c.get('OPEN', 0), c.get('CITED', 0), c.get('DISCHARGED', 0), c.get('WITNESSED', 0), c.get('DOMAIN', 0), RC.get('agree', '?'),
                ('published at DOI %s' % pub.get('doi')) if pub.get('doi') else 'held'))


def _finding_text():
    S, rl, J, PS, W, RC, DS, MI = (jl(n_) for n_ in ('b640_scores.json', 'b640_record_lines.json', 'b640_act_root.json', 'b640_premise_status.json',
                                                      'b640_workorders.json', 'b640_reader_compare.json', 'b640_description_scan.json', 'b640_mirror.json'))
    Z = _zres()
    rd_ = Z.get('read') or {}
    c, r = PS.get('counts') or {}, PS.get('rule_rows') or {}
    n_ans = len(re.findall(r'^### PROMPT ', rd('b640_author_answers.txt'), re.M))
    t = _title_entry()
    ls = (rl.get('lines') or []) + [{}, {}]
    e = ['', t, '',
         '*Filed at b640 on the author’s ruling `(R250)` and the author’s answers (%d). Banks: relay `data/b640_premise_status.txt`, '
         '`data/b640_workorders.txt`, `data/b640_description_scan.txt`, `data/b640_reader_compare.txt`, `data/b640_zenodo_read.txt`, '
         '`data/b640_mirror.txt`, `data/b640_act_root.txt`.*' % n_ans, '',
         '**The status at five** (Component 2): the 50 heads re-read at their pins and classed by the shared tool, relay tools/premise_status.py, '
         'its test one planted head per outcome -- %d open, %d cited, %d discharged, %d witnessed, %d domain (rule rows %d / %d / %d / %d / %d), '
         'every move from b639’s read printed with its reason; the four general predicates of Mathlib’s read domain conditions; the salt-check '
         'column beside every head. H74a %s.' % (c.get('OPEN', 0), c.get('CITED', 0), c.get('DISCHARGED', 0), c.get('WITNESSED', 0), c.get('DOMAIN', 0),
                                                  r.get('OPEN', 0), r.get('CITED', 0), r.get('DISCHARGED', 0), r.get('WITNESSED', 0), r.get('DOMAIN', 0),
                                                  (S.get('H74a') or ['?'])[0]), '',
         '**The work-orders** (Component 3): OPEN_TRAILS :%s, one line per open premise not already carried (%s lines), the four carried heads '
         'cross-referenced; open heads with a work-order %s of %s. H74b %s.' % (W.get('line'), W.get('lines'), len(W.get('named') or []), W.get('open'),
                                                                                   (S.get('H74b') or ['?'])[0]), '',
         '**The description** (Component 4): its assumption section recomposed from the five-status bank, its open section re-read by the fact '
         'clause, its note carrying that no claim is added or withdrawn, every other sentence carried with straight quotes; %s bytes, the '
         'scanner %s, every internal name defined.' % (DS.get('bytes'), 'clean' if DS.get('clean') else 'NOT CLEAN'), '',
         '**The second reader** (Component 5): a fresh session off D:\\ given the description alone and three questions; %s of 3 agreeing with '
         'the description’s sentences. H74c %s.' % (RC.get('agree'), (S.get('H74c') or ['?'])[0]), '',
         '**The draft** (Component 6): the mirror rebuilt after the act’s last push (%s, md5 %s), its zip replacing b639’s in draft %s and the '
         'description replaced through the route; read back, %s files, every file at its digest %s; H74d %s. The author’s word %s.' % (
             os.path.basename(MI.get('zip') or ''), MI.get('zip_md5'), K.DRAFT, rd_.get('n_files'), rd_.get('files_ok'), (S.get('H74d') or ['?'])[0], _word()), '',
         '**The record lines** (`(R250)`(1)-(3)): b639 at its weight with the reading of (2) (FINDINGS :%s); the five-status clause beneath the '
         'criterion (OPEN_TRAILS :%s).' % (ls[0].get('line'), ls[1].get('line')), '',
         '**The root.** b640 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b639’s status print (FINDINGS :7885) under the five statuses and carries the '
         'census method item (OPEN_TRAILS :13395) toward v0.7; it strengthens the programme’s offering of a deposit whose assumptions a reader '
         'outside the programme can count -- what is open, what is cited, what is discharged, what is only witnessed, and what is no assumption at all.', '',
         '**Next.** Per `(R250)`(8): b641 on the author’s word, the census at v0.7 with the five-status column, or the open premises taken up one at '
         'a time beginning with Keiper’s obligations; the author rules on the closing.', '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a status reads a kernel’s constructions and their use.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) the reader staged at C:/reader_b640, off D:\\, its answers copied into relay; (2) the description’s open section and its root '
              'and composition lines re-read by the fact clause beside the ruled assumption section, each change printed with its reason; (3) the '
              'shared status tool carried from b639’s record tool and extended through the Edit tool, each step committed alone; (4) the reader’s '
              'answers compared by needles drawn from the description’s own sentences, the reader’s lines printed beside')


def _trail_text():
    S, fj, rl, J, W = (jl(n_) for n_ in ('b640_scores.json', 'b640_findings.json', 'b640_record_lines.json', 'b640_act_root.json', 'b640_workorders.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b640_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R250) ratified.** (1) b639 at its weight. (2) Why the description held. (3) The status at five. (4) The work-orders. (5) The '
             'description recomposed. (6) The legibility reader. (7) The draft updated and held. (8) The act after: b641.', '',
             '**Entered:** FINDINGS.md:%s (b639’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the five-status clause), :%s (the work-orders); this '
             'record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), W.get('line')), '',
             '**The deposit:** draft %s updated, its word %s.' % (K.DRAFT, _word()), '',
             '**Act root:** b640 `%s` (previous `%s`, b639’s; relay data/act_roots.txt).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b640_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): b641 names no kernel terminal; the open premises’ work-orders name their kernels and pins.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b640_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R250)`(8), b641 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b640_scores.json')
    L = ['=' * 104, 'b640 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper() if k2.startswith('H') else k2, S[k2][0], S[k2][1])
                                                           for k2 in SCORE_KEYS]
    L += [''] + rd('b640_defects.txt').rstrip(NL).split(NL)
    put_txt('b640_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J, W = (jl(n_) for n_ in ('b640_scores.json', 'b640_findings.json', 'b640_trail.json', 'b640_record_lines.json', 'b640_act_root.json',
                                             'b640_workorders.json'))
    ls = (rl.get('lines') or []) + [{}, {}]
    L = ['b640 -- THE COMPONENTS, BANKED UNDER (R250).', '',
         '### COMPONENT 0 : step zero (data/b640_tests_stepzero.txt, data/b640_arms_prerun.txt, the seal`s hashes)',
         '### COMPONENT 1 : b639`s weight FINDINGS :%s ; the five-status clause OPEN_TRAILS :%s' % (ls[0].get('line'), ls[1].get('line')),
         '### COMPONENT 2 : the status at five (data/b640_premise_status.txt, data/b640_status_test.txt) ; H74a %s' % S['H74a'][0],
         '### COMPONENT 3 : the work-orders OPEN_TRAILS :%s (data/b640_workorders.txt) ; H74b %s' % (W.get('line'), S['H74b'][0]),
         '### COMPONENT 4 : the description (data/b640_deposit_description.txt, data/b640_description_scan.txt)',
         '### COMPONENT 5 : the reader (data/b640_reader_packet.txt, data/b640_reader_compare.txt) ; H74c %s' % S['H74c'][0],
         '### COMPONENT 6 : the mirror (data/b640_mirror.txt) ; the draft (data/b640_zenodo_update.txt, data/b640_zenodo_read.txt) ; H74d %s ; the word %s' % (
             S['H74d'][0], _word()),
         '### COMPONENT 7 : the pages, the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'))]
    put_txt('b640_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  table cells: %s ; nd %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b640_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  table cells: %s ; nd %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:6000])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b640_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b640_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-08 by b640 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


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
    put_json('b640_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


def status_test(*a):
    """### Component 2: tools/test_premise_status.py run and counted (data/b640_status_test.txt and its json)."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_premise_status.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    n, p = R3.count_cases(out)
    put_txt('b640_status_test.txt', ['b640 -- tools/test_premise_status.py RUN AND COUNTED (%s); exit %d' % (utc(), r.returncode), ''] + out.rstrip(NL).split(NL)
            + ['', '### CASES : %d ; PASSING : %d' % (n, p)])
    put_json('b640_status_test.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p))
    print('  exit %d ; cases %d ; passing %d' % (r.returncode, n, p))


# ================================================================================ THE DISPATCHER
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'seal_hashes', 'answer_of', 'n5', 'put_txt', 'put_json', 'http', 'compose',
                                                          'desc_scan', 'TRAIL_HEAD', 'act_from'):
        print('usage: b640_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
