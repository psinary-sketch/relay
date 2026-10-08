# -*- coding: utf-8 -*-
"""b639_record.py -- THE ACT'S RECORD TOOL, UNDER (R249). ### ONE SUBCOMMAND PER BANK.

### ### b639: LANE THREE, ACT SIXTY-SIX -- THE DEPOSIT ON THE (R110) ROUTE: THE 50 PREMISE HEADS CLASSED BY STATUS, THE DESCRIPTION IN THE
### READER'S ORDER, THE FILES WITH THEIR DIGESTS, A DRAFT READ BACK FROM THE SERVICE, THE AUTHOR'S WORD, THEN PUBLICATION AND THE DOI
### RECORDED; THE ROSTER AT CENSUS v0.6 AND THE MIRROR REBUILT.
### Subcommands write only `data/b639_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers
### are b633's, b638's and b602's record tools', imported; ledger appends through b566's guarded `append_to`. The data is tools/b639_worklist.py.
### THE (R110) ROUTE (OPEN_TRAILS :9514): the token is read from the environment variable at call time, sent only in the `Authorization`
### header, never printed, logged, banked or passed on a command line; every printed or banked text passes `_tclean()`, and a bank carrying
### the token is REFUSED before it is written. The service is read once per step, its reading printed and banked. No request carries an
### identifier of the author: the User-Agent names the act alone. Nothing publishes before the author's word (`z_publish` refuses without
### the word banked in data/b639_author_answers.txt). b628's full intake bank is never read here, never staged or committed. A stand-in bank
### directory named by the environment variable B639_STANDIN is read before data/ by the record texts' dry runs alone.
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
import urllib.error
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b638_record as R8  # noqa: E402
import b639_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = '47d34df0-9823-4c9f-9efb-d1daddb7dd61'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b639_registration_2026-10-07.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_json_r3, _write, _scan, _clean = R3.put_json, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
STANDIN = os.environ.get('B639_STANDIN') if ('dry' in sys.argv[2:]) else None
KERNS_READ = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-spinor', 'SIDE-effects', 'SIDE-cosmo',
              'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-fano-darkness', 'SIDE-li-map', 'SIDE-rcurve', 'SIDE-grh-transfer')


def _tok():
    return os.environ.get(K.TOKVAR) or ''


def _tclean(s):
    t = _tok()
    s = s if isinstance(s, str) else str(s)
    return s.replace(t, '[TOKEN REDACTED]') if t else s


def put_txt(name, lines):
    b = (NL.join(_tclean(x) for x in lines) + NL).encode('utf-8')
    t = _tok().encode('utf-8')
    if t and t in b:
        sys.exit('### ### **REFUSED TO BANK %s: THE TOKEN STRING IS IN IT.**' % name)
    return R3.put_txt(name, [x.decode('utf-8') for x in [b[:-1]]])


def put_json(name, obj):
    b = json.dumps(obj, indent=1, ensure_ascii=False)
    t = _tok()
    if t and t in b:
        sys.exit('### ### **REFUSED TO BANK %s: THE TOKEN STRING IS IN IT.**' % name)
    return R3.put_txt(name, [b])


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
_DJ = os.path.join(D, 'b639_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b639 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b639_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b639_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table():
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: (R110) ratified -- the route, the token in the environment, every write fetched back; the guard`s token limb', PP, PRE_PP,
         'OPEN_TRAILS.md', list(range(K.R110 - 2, K.R110 + 10)), 1200),
        ('OPEN_TRAILS: the lines the ferry names -- the form of an edition, the precedence order, the authority order, the build clause, the N5 '
         'scorer, the build route, the reader`s clause, the G036 note, b638`s record; W-ORD-ACT-ROOT and the act root in MANIFEST',
         PP, PRE_PP, 'OPEN_TRAILS.md', sorted(set(list(K.FERRY_LINES) + [K.ACT_ROOT_WO, K.MANIFEST_ROOT])), 1600),
        ('FINDINGS: b638`s weight line on b637 and b638`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B638_WEIGHT_PRIOR, K.B638_ENTRY], 700),
        ('README: the ceiling sentence, the supportable paragraphs for v0.17-v0.21 and v0.22-v0.25, the deposit note', PP, PRE_PP, 'README.md',
         list(K.README_SUPPORT) + [K.README_NOTE], 2400),
        ('REGISTRY: the deposit row d1-1 and its record lines', PP, PRE_PP, 'REGISTRY.md', [77, 78, K.REGISTRY_ROW], 900),
        ('relay data/b635_deposit_items.txt, whole', RELAY, PRE_RELAY, 'data/b635_deposit_items.txt', ('GREP', r'.'), 300),
        ('relay data/glossary.txt: the deposit entry and the located clause`s', RELAY, PRE_RELAY, K.GLOSSARY,
         ('GREP', r'^(the deposit|the located clause|the mirror|the act root)\t'), 900),
        ('relay data/act_roots.txt: its last line', RELAY, PRE_RELAY, 'data/act_roots.txt', ('LAST', None), 300),
        ('relay tools/mirror_roster.json as b637 left it: its tail and lastChanged', RELAY, PRE_RELAY, K.ROSTER,
         ('GREP', r'KEYSTONE_CENSUS_v0_5|FINDINGS_AS_THEY_STAND_v0_6|A_Place_to_Stand_v5_18|lastChanged'), 220),
        ('relay tools/mirror_roster.json at the roster edit (%s)' % K.ROSTER_COMMIT, RELAY, K.ROSTER_COMMIT, K.ROSTER,
         ('GREP', r'KEYSTONE_CENSUS_v0_[56]|lastChanged'), 220),
        ('relay tools/mirror_build.ps1 (unedited): its parameter, stage and ROSTER line', RELAY, PRE_RELAY, K.BUILDER,
         ('GREP', r'param\(|mirror-build-|ROSTER|roster-CHANGE'), 200),
        ('relay tools/b616_record.py: the no-disclosure arm`s needle sets (their builders; the needles themselves are read at run time from '
         'TECHNE-Core`s documents and never printed)', RELAY, PRE_RELAY, 'tools/b616_record.py', ('GREP', r'^def (nd_sets|nd_hits)|^METHOD_REL|^TREE_REL'), 200),
        ('relay data/b638_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b638_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
        ('relay data/b574_zenodo_fetch.txt: record 21539167 at v1.1.2, its eleven files with the record`s md5', RELAY, PRE_RELAY,
         'data/b574_zenodo_fetch.txt', ('GREP', r'^### the deposit|^    (id|version|files)|^      [A-Za-z_]+\.(md|html|svg) '), 220),
        ('PLACE-papers the census at v0.6: its premise table`s head and its sum line', PP, PRE_PP, K.CEN6,
         ('GREP', r'^### The named premises the INTERFACES rows rest on, at v0\.6|^\*50 heads carry'), 900),
        ('the ζ page: the equivalence theorem and its two faces with their axioms', PP, PRE_PP, K.PAGE,
         ('GREP', r'^\d+\. `SIDEExplicitFormula\.(B321\.h2_sign_iff_rh|LiCriterionBridge\.(li_nonneg_iff_rh|arith_limit_nonneg_iff_rh))`'), 700),
        ('relay data/b457_profile_run.txt: the route terminals` axiom prints at SIDE-kernel v1.5', RELAY, PRE_RELAY, 'data/b457_profile_run.txt',
         ('GREP', r'^SIDE-kernel tag v1\.5|depends on axioms'), 300),
    ]


def reads(*a):
    L = ['b639 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        elif isinstance(sel, tuple) and sel[0] == 'LAST':
            nums = [max(i + 1 for i, l in enumerate(sl) if l.strip())]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    au = g(K.ZETA23_CLONE, 'show', 'HEAD:' + K.ZETA23_AUDIT)
    al = lines_of(au)
    L += ['### Zeta23`s own record: %s @ %s (the clone at relay data/anthropic-zeta23/formal-math), :80' % (
        K.ZETA23_AUDIT, g(K.ZETA23_CLONE, 'rev-parse', '--short=8', 'HEAD').strip()), '    :80     %s' % ((al[79] if len(al) >= 80 else '### NO SUCH LINE')[:300])]
    L += ['', '### the token`s location: the environment variable %s ; present %s ; not printed, not read beyond its presence here' % (K.TOKVAR, bool(_tok())),
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b639_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()) + 1, len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R249) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b639 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b639_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b639_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b639_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


# ================================================================================ THE SEAL'S HASHES ((R246)(3), OPEN_TRAILS :13307)
def seal_hashes():
    rec_ = jl('b639_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b639 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b639_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 0: THE PREMISE HEADS BY STATUS, (R249)(2)
DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|unsafe|partial)\s+)*(theorem|lemma|def|abbrev|instance|example)\b(.*)$")
OPEN_B, CLOSE_B = '({[⦃', ')}]⦄'
REL = re.compile(r'(↔|(?<![<>:=!])=(?![=>])|≤|<|≠)')


def strip_comments(t):
    """### block comments /- ... -/ (nested) and line comments -- blanked to spaces, every newline kept, so line numbers stand."""
    out, i, depth = [], 0, 0
    while i < len(t):
        if t.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
            continue
        if depth and t.startswith('-/', i):
            depth -= 1
            out.append('  ')
            i += 2
            continue
        if not depth and t.startswith('--', i):
            j = t.find(NL, i)
            j = len(t) if j < 0 else j
            out.append(' ' * (j - i))
            i = j
            continue
        ch = t[i]
        out.append(ch if (ch == NL or not depth) else ' ')
        i += 1
    return ''.join(out)


def _target(t):
    depth, cut = 0, 0
    for i, ch in enumerate(t):
        if ch in OPEN_B:
            depth += 1
        elif ch in CLOSE_B:
            depth -= 1
        elif ch == '→' and depth == 0:
            cut = i + 1
    return t[cut:].strip()


def conclusion(sig):
    """### the text after the last top-level ':' of a signature (before ':='), its last top-level '→' target, any ∀-prefix stripped."""
    depth, last = 0, -1
    for i, ch in enumerate(sig):
        if ch in OPEN_B:
            depth += 1
        elif ch in CLOSE_B:
            depth -= 1
        elif ch == ':' and depth == 0 and sig[i:i + 2] != ':=':
            last = i
    if last < 0:
        return ''
    t = _target(' '.join(sig[last + 1:].split()))
    for _ in range(4):
        m = re.match(r'^∀\s+[^,]*,\s*', t)
        if not m:
            break
        t = _target(t[m.end():])
    return t


def head_tok(t):
    m = re.match(r"([^\W\d][\w'₀-₉]*(?:\.[^\W\d][\w'₀-₉]*)*)", t.lstrip('( '))
    return m.group(1).split('.')[-1] if m else None


def hyp_binders(sig):
    """### the declaration's own hypotheses: every binder the rule types a Prop, instance binders apart (a conditional lemma assumes as much
    ### as it gives, the author's answer before the seal)."""
    import e0_rule as E
    hd = ' '.join(re.sub(r'^\S+', '', re.sub(r'^.*?\b(theorem|lemma|def|abbrev|instance|example)\b\s*', '', sig, count=1), count=1).split())
    try:
        return ['%s : %s' % (b['name'], b['type']) for b in E.binders_of(hd) if b['typing'] == 'prop' and b['kind'] != 'instance']
    except Exception as ex:
        return ['### UNREAD: %s' % ex]


def decls_concluding(repo, pin, head):
    files = [l.split(':', 1)[1] for l in g(repo, 'grep', '-l', '-w', head, pin, '--', '*.lean').split(NL) if ':' in l]
    out = []
    for f in files:
        src = strip_comments(g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')).split(NL)
        i = 0
        while i < len(src):
            m = DECL.match(src[i])
            if not m:
                i += 1
                continue
            j, buf = i, []
            while j < len(src) and j < i + 40:
                buf.append(src[j])
                if ':=' in src[j] or re.search(r'\bwhere\s*$', src[j]) or (j > i and src[j].startswith('  |')):
                    break
                j += 1
            sig = ' '.join(' '.join(buf).split(':=')[0].split())
            sig = re.sub(r'\s+where\s*$', '', sig)
            sig = re.sub(r'\s\|\s.*$', '', sig)
            c = conclusion(sig)
            if head_tok(c) == head:
                out.append(dict(file=f, line=i + 1, kind=m.group(1), conclusion=c[:200], text=sig[:240], hyps=hyp_binders(sig),
                                salt=(K.SALT_MARK in f), relation=bool(REL.search(c))))
            i = j + 1
    return out


def inline_of(repo, pin, head):
    out = []
    pat = r'((have|let)\b[^:=]*:\s*\(?([A-Za-z_][A-Za-z0-9_]*\.)*%s\b)|(\bshow\s+\(?([A-Za-z_][A-Za-z0-9_]*\.)*%s\b)' % (re.escape(head), re.escape(head))
    for l in g(repo, 'grep', '-n', '-E', pat, pin, '--', '*.lean').split(NL):
        if l.count(':') >= 3:
            _p, f, ln, t = l.split(':', 3)
            src = strip_comments(g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')).split(NL)
            live = int(ln) <= len(src) and re.search(pat, src[int(ln) - 1]) is not None
            out.append(dict(file=f, line=int(ln), text=' '.join(t.split())[:200], salt=(K.SALT_MARK in f), iff=('↔' in t), live=live))
    return out


def declaration_of(repo, pin, head):
    hits = g(repo, 'grep', '-n', '-E', r'^\s*(structure|class|def|abbrev|inductive|noncomputable def)\s+([A-Za-z_.]*\.)?%s(\s|$|:)' % re.escape(head),
             pin, '--', '*.lean')
    for h in [x for x in hits.split(NL) if x.count(':') >= 3]:
        _pin, f, ln, _t = h.split(':', 3)
        src = g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '').split(NL)
        k = int(ln) - 2
        doc = []
        if k >= 0 and src[k].rstrip().endswith('-/'):
            while k >= 0:
                doc.insert(0, src[k])
                if src[k].lstrip().startswith('/-'):
                    break
                k -= 1
        return dict(file=f, line=int(ln), text=_t.strip()[:200], doc=NL.join(doc))
    return None


def _heads_rows():
    import e0_rule as E
    rows = _table()
    heads, eheads, pins = collections.defaultdict(set), collections.defaultdict(set), {}
    for r in rows:
        if R8._is_up(r) or r['grade'] != 'INTERFACES' or r.get('provenance') not in ('rule', 'rule-elab'):
            continue
        hd, pb = R8._premise_binders(r, E)
        key = (r['repo'], r['name'])
        pins[key] = (r.get('head') or '')[:7]
        for b in pb:
            nm, _w = R8.R7._premise_heads(b, hd)
            if nm:
                (heads if r.get('provenance') == 'rule' else eheads)[nm].add(key)
    return rows, heads, eheads, pins


def _roster_repos():
    import act_root as AR
    return [r for r in AR.repositories() if r not in ('relay', 'PLACE-papers')]


def status(*a):
    """### Component 0, (R249)(2) as the author answered before the seal: the 50 heads -- the census's method, the rule-graded INTERFACES rows'
    ### named premises -- each classed by the first status it meets, in the ruling's order: DISCHARGED IN KERNEL, a construction of the head
    ### outside the SaltCheck files in a kernel its rows sit in (a declaration concluding it with no Prop hypothesis of its own, or an inline
    ### have / let / show of its type inside a proof); DISCHARGED ELSEWHERE, such a construction in another kernel of the root`s list, or a
    ### line of Zeta23`s own record naming the head beside a discharge; CITED, the head`s own declaration carrying T1-lit in its docstring and
    ### no other tier mark (every field cited); OPEN otherwise, each OPEN head`s work-order lines on OPEN_TRAILS printed, or their absence.
    ### Every test each head meets is printed beside its status; the SaltCheck witnesses in the non-vacuity column; the seat's hand-read
    ### of every discharge (K.HANDREAD) beside, for the author's strike. data/b639_premise_status.txt and its json."""
    rows, heads, eheads, pins = _heads_rows()
    H = sorted(h for h in heads if heads[h])
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    aud = lines_of(g(K.ZETA23_CLONE, 'show', 'HEAD:' + K.ZETA23_AUDIT))
    others = _roster_repos()
    res = []
    for h in H:
        keys = sorted(heads[h] | eheads.get(h, set()))
        repos = sorted(set(k for k, _n in keys))
        decls, inl, decl = [], [], None
        for repo in repos:
            pin = sorted(set(pins[k] for k in keys if k[0] == repo))[0]
            path = 'D:/' + repo
            decls += [dict(repo=repo, pin=pin, **x) for x in decls_concluding(path, pin, h)]
            inl += [dict(repo=repo, pin=pin, **x) for x in inline_of(path, pin, h)]
            dd = declaration_of(path, pin, h)
            if dd and decl is None:
                decl = dict(repo=repo, pin=pin, **dd)
        unc = [d for d in decls if not d['salt'] and not d['relation'] and not d['hyps']]
        cond = [d for d in decls if not d['salt'] and (d['relation'] or d['hyps'])]
        salt = [d for d in decls if d['salt']] + [d for d in inl if d['salt']]
        inl_ok = [d for d in inl if not d['salt'] and not d['iff'] and d['live']]
        dik = bool(unc or inl_ok)
        # ### DISCHARGED ELSEWHERE: only for a head the rows' kernel declares (a Mathlib predicate proved of another object elsewhere is not
        # ### this premise's discharge); every other kernel of the root's list read at its main by git grep, and Zeta23's own record
        elsewhere = []
        if decl:
            for o in others:
                if o in repos or not os.path.isdir('D:/' + o):
                    continue
                for d in decls_concluding('D:/' + o, 'main', h):
                    if not d['salt'] and not d['relation'] and not d['hyps']:
                        elsewhere.append(dict(repo=o, pin='main', **d))
                for d in inline_of('D:/' + o, 'main', h):
                    if not d['salt'] and not d['iff'] and d['live']:
                        elsewhere.append(dict(repo=o, pin='main', **d))
        aud_hits = [(i, l.strip()[:240]) for i, l in enumerate(aud, 1) if re.search(r'(?<![\w.])' + re.escape(h) + r'(?![\w])', l)]
        aud_dis = [x for x in aud_hits if re.search(r'discharg', x[1], re.I)]
        doc = (decl or {}).get('doc') or ''
        cited_line = [l.strip() for l in doc.split(NL) if re.search(r'T1[- ]?lit', l)]
        other_tiers = sorted(set(re.findall(K.TIER_MARKS, doc)))
        cited = bool(cited_line) and not other_tiers
        meets = [s for s, ok in zip(K.STATUSES[:3], (dik, bool(elsewhere or aud_dis), cited)) if ok] or ['OPEN']
        st = meets[0]
        wo = [(i, l) for i, l in enumerate(ot, 1) if re.search(r'W-ORD-[A-Z0-9-]+', l) and re.search(r'(?<![\w.])' + re.escape(h) + r'(?![\w])', l)]
        wo_names = sorted(set(m for _i, l in wo for m in re.findall(r'W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*', l)))
        res.append(dict(head=h, status=st, meets=meets, rule=len(heads[h]), elab=len(eheads.get(h, ())), kernels=repos,
                        pins=sorted(set(pins[k] for k in keys)), rows=['%s %s' % k for k in keys],
                        rule_rows=['%s %s' % k for k in sorted(heads[h])], decl=decl, upstream=decl is None,
                        unconditional=unc, inline=inl_ok, conditional=cond, salt=salt, elsewhere=elsewhere, audit=aud_hits, audit_discharge=aud_dis,
                        cited_lines=cited_line, other_tiers=other_tiers, wo_lines=[i for i, _l in wo], wo_names=wo_names,
                        handread=K.HANDREAD.get(h, ''), wo_handread=list(K.WO_HANDREAD.get(h, ()))))
    cnt = collections.Counter(x['status'] for x in res)
    rr = collections.Counter()
    er = collections.Counter()
    for x in res:
        rr[x['status']] += x['rule']
        er[x['status']] += x['elab']
    multi = [x['head'] for x in res if len(x['meets']) > 1]
    elab_only = sorted((h, len(v)) for h, v in eheads.items() if not heads.get(h))
    h2_among = 'h2_sign' in H
    open_ok = all(x['wo_lines'] or True for x in res if x['status'] == 'OPEN')
    h73e = len(res) == 50 and all(x['status'] in K.STATUSES for x in res) and open_ok
    proto = K.PROTO_FIGURE
    moved = sorted((h, proto['members'].get(h), x['status']) for x in res for h in [x['head']] if proto['members'].get(h) != x['status'])
    L = ['b639 -- COMPONENT 0, (R249)(2): THE 50 PREMISE HEADS CLASSED BY STATUS FROM THE KERNELS, BEFORE ANY DESCRIPTION IS WRITTEN (%s)' % utc(), '',
         '### THE HEADS: the census`s method (b637`s premises, the census at v0.6 back matter) -- the rule-graded INTERFACES rows of relay '
         'data/terminal_table.json at relay %s, each premise`s named head; heads %d, rule rows summed %d, rule-elab rows beside %d.' % (
             g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), len(H), sum(x['rule'] for x in res), sum(x['elab'] for x in res)),
         '### the heads carrying rule-elab rows alone, outside the 50 (the census`s method counts the rule-graded rows): %d heads, %d rows -- %s.' % (
             len(elab_only), sum(n for _h, n in elab_only), ', '.join('%s %d' % x for x in elab_only)),
         '### h2_sign among the 50 heads: %s -- the equivalence h2_sign_iff_rh has no premise; h2_sign enters the rows as the clause the theorems '
         'state, and the description names it apart as the open clause.' % h2_among,
         '### THE STATUS, the author`s answers before the seal (data/b639_author_answers.txt): the first of the ruling`s four the head meets --',
         '###   DISCHARGED IN KERNEL: a construction of the head outside the files whose path carries "%s", in a kernel its rows sit in, at the '
         'commit the table read the rows at: a declaration concluding it with no Prop hypothesis of its own and no relation at its top, or an '
         'inline have / let / show of its type inside a proof (an iff apart); a SaltCheck witness shows non-vacuity and discharges nothing.' % K.SALT_MARK,
         '###   DISCHARGED ELSEWHERE: such a construction in another kernel of the act root`s list at its main, for a head the rows` kernel '
         'declares; or a line of Zeta23`s own record (%s) naming the head beside a discharge.' % K.ZETA23_AUDIT,
         '###   CITED: the head`s own declaration carries T1-lit in its docstring and no other tier mark (every field cited, the status of a bundle '
         'its weakest field`s).',
         '###   OPEN: otherwise; each OPEN head`s work-order lines on OPEN_TRAILS printed, or their absence.',
         '### A CORRECTION OF THE SEAT`S OWN FIGURE: the figure put to the author before the seal (%s) came from a prototype whose declaration '
         'reader read a docstring line as a declaration and whose relation test read => as an equation, its conditional test the rule`s premise '
         'outcome alone; the tool reads comments out, => apart, and every Prop hypothesis. The heads whose status moved against that figure: %s.' % (
             proto['figure'], ', '.join('%s %s -> %s' % m for m in moved) or 'NONE'), '']
    for st in K.STATUSES:
        xs = [x for x in res if x['status'] == st]
        L.append('### ### **%s : %d heads ; rule rows %d ; rule-elab rows %d**' % (st, len(xs), rr[st], er[st]))
        for x in xs:
            L.append('  %-28s rule %2d elab %2d | %s | kernels %s @ %s | its declaration %s' % (
                x['head'], x['rule'], x['elab'], ' / '.join(x['meets']), ', '.join(x['kernels']), ', '.join(x['pins']),
                ('%s %s :%d' % (x['decl']['repo'], x['decl']['file'], x['decl']['line'])) if x['decl'] else 'none in the kernel (upstream: Mathlib`s)'))
            L.append('      rows resting on it (rule): %s' % ', '.join(r.split()[-1] for r in x['rule_rows']))
            for d in x['unconditional'][:4]:
                L.append('      CONSTRUCTED: %s %s :%d -- %s' % (d['repo'], d['file'], d['line'], d['text'][:160]))
            for d in x['inline'][:4]:
                L.append('      CONSTRUCTED INLINE: %s %s :%d -- %s' % (d['repo'], d['file'], d['line'], d['text'][:160]))
            for d in x['conditional'][:3]:
                L.append('      conditional (not a discharge): %s :%d -- hypotheses %s%s' % (d['file'], d['line'], d['hyps'][:2], ' ; a relation at its top' if d['relation'] else ''))
            for d in x['salt'][:3]:
                L.append('      non-vacuity (SaltCheck witness): %s :%d -- %s' % (d['file'], d['line'], d['text'][:120]))
            for d in x['elsewhere'][:3]:
                L.append('      CONSTRUCTED ELSEWHERE: %s %s :%d -- %s' % (d['repo'], d['file'], d['line'], d['text'][:140]))
            for i, l in x['audit_discharge'][:2]:
                L.append('      Zeta23`s record %s :%d -- %s' % (K.ZETA23_AUDIT, i, l[:160]))
            if x['cited_lines']:
                L.append('      cited: %s%s' % (x['cited_lines'][0][:200], (' ; other tier marks %s, so not cited whole' % x['other_tiers']) if x['other_tiers'] else ''))
            if st == 'OPEN':
                L.append('      work-orders on OPEN_TRAILS: %s' % ((', '.join(x['wo_names']) + ' at :' + ', :'.join(str(i) for i in x['wo_lines'][:6]))
                                                                 if x['wo_lines'] else '### NO WORK-ORDER NAMES IT'))
                if x['head'] in K.WO_HANDREAD:
                    L.append('      the seat`s hand-read of those lines, for the author`s strike: %s -- %s' % K.WO_HANDREAD[x['head']])
            if x['handread']:
                L.append('      the seat`s hand-read, for the author`s strike: %s' % x['handread'])
        L.append('')
    L += ['### heads meeting more than one discharge test (each classed by the first): %s' % (multi or 'NONE'),
          '### OPEN heads with a work-order line: %d of %d; without: %s' % (
              sum(1 for x in res if x['status'] == 'OPEN' and x['wo_lines']), cnt['OPEN'],
              ', '.join(x['head'] for x in res if x['status'] == 'OPEN' and not x['wo_lines']) or 'NONE'),
          '### the ruling`s named examples: OPEN %s ; CITED %s' % (
              ['%s %s' % (h, next((x['status'] for x in res if x['head'] == h), 'NOT A HEAD')) for h in K.RULING_OPEN],
              ['%s %s' % (h, next((x['status'] for x in res if x['head'] == h), 'NOT A HEAD')) for h in K.RULING_CITED]), '',
          '### ### **HEADS %d ; DISCHARGED IN KERNEL %d ; DISCHARGED ELSEWHERE %d ; CITED %d ; OPEN %d -- RULE ROWS %d / %d / %d / %d. H73e %s.**' % (
              len(res), cnt['DISCHARGED IN KERNEL'], cnt['DISCHARGED ELSEWHERE'], cnt['CITED'], cnt['OPEN'], rr['DISCHARGED IN KERNEL'],
              rr['DISCHARGED ELSEWHERE'], rr['CITED'], rr['OPEN'], 'HOLDS' if h73e else 'REFUTED')]
    put_txt('b639_premise_status.txt', L)
    put_json('b639_premise_status.json', dict(at=utc(), relay=g(RELAY, 'rev-parse', 'HEAD').strip(), heads=res, counts=dict(cnt), rule_rows=dict(rr),
                                              elab_rows=dict(er), h2_among=h2_among, multi=multi, h73e='HOLDS' if h73e else 'REFUTED',
                                              moved_against_figure=moved, figure_put=proto['figure']))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R249)(1)-(2)
W_HEAD = ('*Appended 2026-10-07 by b639 to b638’s entry (:%d), under `(R249)`(1) -- b638 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS, THE '
          'SEAT’S FOUR READINGS CONFIRMED AND THE “proves” EXCEPTION ENTERED BY NAME:*')
M_HEAD = ('*Appended 2026-10-07 by b639 beside the reader’s clause (:%d) and b638’s record (:%d), under `(R249)`(2) and the author’s answers '
          'before b639’s seal -- THE PREMISE TABLE’S STATUS COLUMN, A CENSUS METHOD ITEM, PRICED FOR v0.7, TRIGGER THE AUTHOR’S WORD:*')
P_HEAD = ('*Appended 2026-10-07 by b639, under the author’s answer before b639’s seal (relay data/b639_author_answers.txt) -- '
          'W-ORD-DAY1-PATCH-VERSIONS, PRICED, NOT STARTED, TRIGGER THE AUTHOR’S WORD:*')
COMPANIONS = ('Exhaustive_Enumeration.md', 'Which_Structure_Confines.md', 'Spectral_Inertness.md', 'Seven_Mechanism_Classes.md',
              'Third_Identity_Element.md', 'Silence_of_Foundations.md', 'ONE_PAGE_PROOF.md')


def _weight():
    S, GJ, F, GT, AR, MI, H28 = (jl(n_) for n_ in ('b638_scores.json', 'b638_glossary.json', 'b638_structure_fields.json', 'b638_gen_test.json',
                                                  'b638_act_root.json', 'b638_mirror.json', 'b638_h28.json'))
    CJ = jl('b638_census.json')
    I_ = CJ.get('interfaces') or {}
    post = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b638_checks_postpush.txt'))
    pre = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b638_checks.txt'))
    att = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b638_checks_prepush_attempt1.txt'))
    tam = re.search(r'TEST FILES (\d+) ; RUN (\d+) ; NOT CLEAN (\d+)', rd('b638_tests_after.txt'))
    oc, others = ((int(tam.group(2)) - int(tam.group(3))), int(tam.group(1))) if tam else ('?', '?')
    ndef = len([l for l in rd('b638_defects.txt').split(NL) if re.match(r'^    \([a-z]\) ', l)])
    held = lambda ks, w: [k for k in ks if (S.get(k) or [''])[0].startswith(w)]   # noqa: E731
    exc = [x for x in (H28.get('excepted') or []) if x[1] == 'proves']
    return ('\n%s relay data/glossary.txt, %s entries, each a name, a definition and a source, the located clause spelled out as the author '
            'ruled it (relay %s); the field print, %d structure types among b637’s moves, %s fields, %s, so the %s moves resting on the '
            'setup structure of the power limit stand and the rule needed no edit, the second reader’s G036 note at OPEN_TRAILS :%d; the page '
            'generator printing the glossary block when a node list carries the mark, lists without it emitting as before (its test %s of %s; '
            'every test after its commit %s of %s, clean); both pages re-emitted twice, each commit alone, the glossary block alike on both, one Placement row '
            'each after the census; the keystone census at v0.6 beside v0.5 unedited (PLACE-papers 28dec96) -- the plain opening, the '
            'glossary, the provenance column with the upstream rows apart, the premise table at %d heads over %d rows, its residue of %d '
            'printed as it reads, MET and the binder grammar’s classes; H28a %s, H28b %s, H28c %s; the act root at the census v0.6, the root '
            '%s…. H72a, H72c and H72d HOLD; H72b and N2 REFUTED in letter, the premise table’s rows summing to %d (%d rule, %d rule-elab) '
            'against %s graded rows, the %s cell-graded rows outside the census’s method and some rows carrying two premises, the face having '
            'flagged it; %s HELD. FINDINGS :%d; OPEN_TRAILS :%d, :%d. The suite %s of %s before the push and %s of %s after it; defects '
            '(a)-(%s) the seat’s, (a) a scratch delete not verified in the same command, declared on the face; one pre-push run at %s of %s '
            'on empty remote reads kept as an attempt, the network’s. The mirror of 2026-10-07-b638 verified by the navigator -- md5 %s…, '
            'sha256 %s…, %s entries, MANIFEST md5 %s…, %s, the root line b638 %s… -- and the project refreshed with MANIFEST, FINDINGS and '
            'both pages, OPEN_TRAILS refused for the project’s room, nothing changed by the refusal. Confirmed, the seat’s four readings: '
            '“the writing law” as the form of an edition at OPEN_TRAILS :%d with its title clause; one glossary entry each for the act numbers '
            'and the kernel names; no Lean call, the reader’s test not rerun after the seal; the located clause’s “proves” printed verbatim and '
            'excepted from the ceiling check. THE “proves” EXCEPTION, entered by name: the word “proves” in the located clause as the author '
            'ruled it, a kernel proving an equivalence being the word’s right use%s. Nothing deposited; no kernel source touched.\n'
            % (W_HEAD % K.B638_ENTRY, GJ.get('entries'), (GJ.get('commits') or ['?'])[0], len(F.get('types') or []), F.get('fields'),
               'every one a Prop' if F.get('all_prop') else '### NOT ALL PROPS', F.get('pwsetup_moves'), K.G036_NOTE, GT.get('passing'),
               GT.get('cases'), oc, others, len([x for x in CJ.get('ptab') or [] if x['rule']]), CJ.get('sum_rule'), len(CJ.get('residue') or []),
               (S.get('H28a') or ['?'])[0].lower(), (S.get('H28b') or ['?'])[0].lower(), (S.get('H28c') or ['?'])[0].lower(), (AR.get('root') or '?')[:8],
               (CJ.get('sum_rule') or 0) + (CJ.get('sum_elab') or 0), CJ.get('sum_rule'), CJ.get('sum_elab'), I_.get('excluded'), I_.get('cell'),
               ', '.join(held(('N1', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5'), 'HELD')), K.B638_ENTRY, K.READER_CLAUSE, K.B638_RECORD,
               pre.group(2) if pre else '?', pre.group(1) if pre else '?', post.group(2) if post else '?', post.group(1) if post else '?',
               'abcdefghij'[ndef - 1] if ndef else '?', att.group(2) if att else '?', att.group(1) if att else '?', (MI.get('zip_md5') or '?')[:8],
               (MI.get('zip_sha256') or '?')[:8], MI.get('entries'), (MI.get('manifest_md5') or '?')[:8], ' / '.join(x.rstrip('.') for x in MI.get('roster_line') or ['?']),
               (MI.get('root_line') or '?').split()[-1][:8], K.FORM, (' (its census line :%d)' % exc[0][0]) if exc else ''))


def _method_item():
    S = jl('b639_premise_status.json')
    c, r = S.get('counts') or {}, S.get('rule_rows') or {}
    return ('\n%s a named premise is a hypothesis type a kernel theorem takes and does not derive, and the census’s premise heads are not of '
            'one kind. Each head takes one status, computed from the kernels and not assigned by hand, the first it meets in this order: '
            'DISCHARGED IN KERNEL, a construction of the head outside the SaltCheck files in a kernel its rows sit in -- a declaration '
            'concluding it with no hypothesis of its own, or an inline have, let or show of its type inside a proof, as the setup structure of '
            'the power limit is built in the four converse proofs; a SaltCheck witness shows that a structure is not vacuous and nothing more, '
            'and a conditional lemma or an iff concluding a head does not discharge it, since it assumes as much as it gives; DISCHARGED '
            'ELSEWHERE, such a construction, or a recorded discharge, at another kernel’s pin; CITED, when the structure’s docstring cites '
            'every field T1-lit, the status of a bundle being the status of its weakest field; OPEN otherwise, each OPEN head with its '
            'work-order on OPEN_TRAILS or its absence printed. The letter of `(R249)`(2) is corrected to these words by the author’s answers, '
            'the navigator’s drafting. At v0.7 the premise table gains the status column and counts by row over both provenances -- a '
            'cell-graded row entering by the named premise its cell carries, a row with two premises counted once under each head and once in '
            'the total -- so that the table’s sum equals the count of the rows the heads rest on by construction, the discrepancy of b638’s '
            'H72b closes, and a reader sees at once how many premises are open, how many cited, and how many the hypotheses of lemmas '
            'discharged inside the kernels. b639’s print (relay data/b639_premise_status.txt): %d heads -- %d discharged in kernel, %d '
            'elsewhere, %d cited, %d open; their rule rows %d / %d / %d / %d. Price: one census edition with its back matter and the census '
            'reads re-run, the status tool carried into the census act. No census edition at b639.\n' % (
                M_HEAD % (K.READER_CLAUSE, K.B638_RECORD), sum(c.values()), c.get('DISCHARGED IN KERNEL', 0), c.get('DISCHARGED ELSEWHERE', 0),
                c.get('CITED', 0), c.get('OPEN', 0), r.get('DISCHARGED IN KERNEL', 0), r.get('DISCHARGED ELSEWHERE', 0), r.get('CITED', 0), r.get('OPEN', 0)))


def _patch_wo():
    return ('\n%s each of the seven Day 1 companions whose bytes moved after the deposit of v1.1.2 while its version label stood -- %s -- '
            'takes a patch version at its next edition (v2.3 to v2.3.1, and so on) with a dated line naming the edits since the deposit, '
            'the line counts against v1.1.2’s bytes as relay data/b639_deposit_files.txt prints them. No label is edited at b639, which '
            'deposits each live file under its own name, the PLACE-papers commit it is read at and its line-diff count against v1.1.2 '
            'printed in the description, so a reader sees that the label stood still while the text moved. Price: seven dated lines, one '
            'act.\n' % (P_HEAD, ', '.join(x.replace('.md', '') for x in COMPANIONS)))


def record_lines(*a):
    """### Component 1, (R249)(1)-(2): FINDINGS, b638 at its weight (to :7861) with the four readings and the "proves" exception; OPEN_TRAILS,
    ### the census method item priced for v0.7 and W-ORD-DAY1-PATCH-VERSIONS priced, the author's answer."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The keystone census at v0.6 under the reader’s clause')
    if entry != K.B638_ENTRY:
        sys.exit('### b638`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    if not jl('b639_premise_status.json').get('heads'):
        sys.exit('### THE STATUS BANK IS ABSENT -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % K.B638_ENTRY, _weight()), ('OPEN_TRAILS.md', M_HEAD % (K.READER_CLAUSE, K.B638_RECORD), _method_item()),
             ('OPEN_TRAILS.md', P_HEAD, _patch_wo())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(items[1][2] + items[2][2], 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT') if x in allt]
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
    _land(Q, items, 'b639_record_lines.json', K.B638_ENTRY)


# ================================================================================ COMPONENT 1: THE MIRROR, AFTER THE LAST PUSH AND BEFORE THE DRAFT
ZIP = K.MIRROR_ZIP
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % K.MIRROR_TAG)


def mbuild(*a):
    """### the builder, unedited, with -DateTag, after the act's last PLACE-papers push (PLACE-papers HEAD at its remote); it writes the zip in
    ### D:/MY-DOwnloads, its stage in %TEMP% and relay tools/mirror_prevbuild.json (its state). Refuses if the zip or stage exists."""
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED (the builder deletes a same-named one)')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag', K.MIRROR_TAG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b639_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-1500:], r.stderr[-800:], 'exit', r.returncode)


def mroot(*a):
    """### OPEN_TRAILS :12929, standing: "Act root: <act> <root>" from relay data/act_roots.txt's last line added to MANIFEST in its stage, in
    ### MANIFEST's own form, the staged MANIFEST written and the zip's one entry updated in place. At this act the last line is b638's: b639's
    ### own root is computed at its record, over its banks, the draft's read-back among them (the author's answer before the seal)."""
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b638':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b638`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b639_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode,
                                           update_err=ps.stderr.strip()))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    """### relay tools/mirror_verify.py on the zip, all three clauses, run from PLACE-papers (clause 2's ls-remote is cwd-dependent)"""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b639_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-1200:])


def mbank(*a):
    """### data/b639_mirror.txt and its json: the zip's md5, sha256 and size, its file count, the MANIFEST's md5, its ROSTER line and its root
    ### line, the previous build's MANIFEST md5, the verification's verdict; the no-disclosure arm over the zip's file list."""
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    text = man.decode('utf-8-sig').replace(chr(13), '')
    ls = text.split(NL)
    rows = [l for l in ls if re.match(r'^\| [^|:]', l) and not l.startswith('| flat file')]
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    zb = open(ZIP, 'rb').read()
    ver = rd('b639_mirror_verify.txt')
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in ver
    prev_md5 = hashlib.md5(zipfile.ZipFile(K.MIRROR_PREV).read('MANIFEST.md')).hexdigest() if os.path.exists(K.MIRROR_PREV) else None
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    head = next((l for l in ls if l.startswith('Source: PLACE-papers @')), '')
    files = [n for n in names if n != 'MANIFEST.md']
    L = ['b639 -- THE MIRROR, BUILT AFTER THE ACT`S LAST PUSH AND BEFORE THE DRAFT BY THE UNEDITED BUILDER ON THE %d-FILE ROSTER, banked %s' % (
             K.ROSTER_FILES, utc()),
         '### THE ZIP (for the deposit and the author`s project) : %s ; %d bytes ; md5 %s ; sha256 %s' % (
             ZIP, len(zb), hashlib.md5(zb).hexdigest(), hashlib.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; %d bytes ; %d rows ; entries in the zip %d (files %d + MANIFEST)' % (
             hashlib.md5(man).hexdigest(), len(man), len(rows), len(names), len(files)),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'),
         '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SOURCE LINE : %s' % head,
         '### THE PREVIOUS BUILD : %s, MANIFEST md5 %s' % (K.MIRROR_PREV, prev_md5),
         '### THE VERIFICATION (relay data/b639_mirror_verify.txt): %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd),
         '### THE CENSUS AT v0.6 IN THE ZIP: %s' % ('THE_KEYSTONE_CENSUS_v0_6.md' in names),
         '### THE FILE LIST:'] + ['    %s' % n for n in names] + ['### THE MANIFEST, WHOLE:'] + ['    ' + l for l in ls]
    put_txt('b639_mirror.txt', L)
    put_json('b639_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=hashlib.md5(zb).hexdigest(), zip_sha256=hashlib.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=hashlib.md5(man).hexdigest(), rows=len(rows), entries=len(names), files=len(files),
                                      roster_line=rosterl, root_line=rootl[0] if rootl else '', prev_manifest_md5=prev_md5, clean=clean, nd=dict(nd),
                                      source=head, census6='THE_KEYSTONE_CENSUS_v0_6.md' in names))
    for l in L[:10]:
        print(l[:300])


# ================================================================================ COMPONENT 2: THE DEPOSIT BANK, REFRESHED, (R249)(4) PART ONE
def _sup_sentences():
    """### README's supportable sentences as README carries them: the ceiling sentence (:106) and the v0.17-v0.21 and v0.22-v0.25 paragraphs,
    ### each paragraph's italic Supportable sentence cut whole."""
    t = lines_of(io.open(os.path.join(PP, 'README.md'), encoding='utf-8').read().replace(chr(13), ''))
    out = []
    ceil = t[K.README_SUPPORT[0] - 1]
    m = re.match(r'^Supportable: \*(.+)\*$', ceil)
    out.append((K.README_SUPPORT[0], m.group(1) if m else None))
    for n in K.README_SUPPORT[2:]:
        m = re.search(r'Supportable, [^*]*?\*(.+?)\*\s+Not supportable', t[n - 1])
        out.append((n, m.group(1) if m else None))
    ns = re.search(r'Not supportable, unchanged: (\*RH proved\*; .+?\*)\.?$', t[K.README_SUPPORT[-1] - 1])
    return out, (ns.group(1).replace('*', '') if ns else None)


def deposit_bank(*a):
    """### data/b639_deposit_items.txt and its json: b635's bank refreshed in the deposit note's own form -- the census at v0.6 with its premise
    ### table's figures and the discrepancy as the census states it, the sieve at v0.6, the root chain by its last line at the bank, the table's
    ### provenance counts at HEAD, the premise heads by status, the mirror, every kernel tag REGISTRY cites peeled at its remote (one ls-remote
    ### per repository), the supportable and not-supportable sentences as README carries them, the record and the token's location; every item
    ### resolved to a path and head at the remote; the no-disclosure arm over the bank."""
    import b616_record as R6
    import b635_record as R5
    cache = {}
    pp_head = g(PP, 'rev-parse', 'HEAD').strip()
    pp_rem = R5._remote(PP, cache).get('refs/heads/main', '')
    relay_head = g(RELAY, 'rev-parse', 'HEAD').strip()
    relay_rem = R5._remote(RELAY, cache).get('refs/heads/main', '')
    items = []

    def item(label, repo, path, head, rem, extra=''):
        ok = bool(head) and head == rem and (path is None or subprocess.run(['git', '-C', repo, 'cat-file', '-e', '%s:%s' % (head, path)]).returncode == 0)
        items.append(dict(label=label, repo=repo.replace('D:/', '').replace('MY-DOwnloads/', ''), path=path, head=head, remote=rem, ok=ok, extra=extra))

    sups, notsup = _sup_sentences()
    item('the supportable sentences as README carries them: the ceiling sentence (:%d) and the v0.17-v0.21 and v0.22-v0.25 paragraphs (:%d, :%d)' % (
        K.README_SUPPORT[0], K.README_SUPPORT[2], K.README_SUPPORT[3]), PP, 'README.md', pp_head, pp_rem,
        'sentences cut whole %d of %d' % (sum(1 for _n, s in sups if s), len(sups)))
    cen = io.open(os.path.join(PP, K.CEN6), encoding='utf-8').read().replace(chr(13), '')
    cen_sum = next((l for l in cen.split(NL) if l.startswith(K.CEN6_SUM_NEEDLE)), None)
    cen_commit = g(PP, 'log', '-1', '--format=%h', '--', K.CEN6).strip()
    item('the keystone census at v0.6, its premise table in its back matter ("%s"), its status column pending at v0.7' % K.CEN6_PREMISES_HEAD[4:],
         PP, K.CEN6, pp_head, pp_rem, 'its commit %s ; the discrepancy as the census states it: %s' % (cen_commit, (cen_sum or '### NOT FOUND').strip('*')))
    item('the sieve at v0.6', PP, K.SIEVE6, pp_head, pp_rem, 'its commit %s' % g(PP, 'log', '-1', '--format=%h', '--', K.SIEVE6).strip())
    roots = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()]
    item('the root chain b624 onward, by its last line at this bank (%s); b639`s own line is computed at its record over the act`s banks, the '
         'draft`s read-back among them, and lands in the next mirror`s MANIFEST' % roots[-1][:80], RELAY, 'data/act_roots.txt', relay_head, relay_rem)
    T = _table()
    prov = R8._prov_counts(T)
    item('the terminal table at HEAD: %d rows, provenance %s' % (len(T), prov), RELAY, 'data/terminal_table.json', relay_head, relay_rem)
    S = jl('b639_premise_status.json')
    item('the premise heads by status (%s): %s ; rule rows %s' % ('relay data/b639_premise_status.txt', S.get('counts'), S.get('rule_rows')),
         RELAY, None, relay_head, relay_rem)
    MI = jl('b639_mirror.json')
    item('the mirror: %s, md5 %s, sha256 %s, %s files + MANIFEST, the census at v0.6 in it %s' % (MI.get('zip'), MI.get('zip_md5'), MI.get('zip_sha256'),
                                                                                              MI.get('files'), MI.get('census6')), RELAY, None, relay_head, relay_rem)
    tags = []
    for k, tg in R5.registry_tags():
        p = 'D:/' + k
        rm = R5._remote(p, cache)
        peel = rm.get('refs/tags/%s^{}' % tg) or rm.get('refs/tags/%s' % tg) or ''
        tags.append(dict(kernel=k, tag=tg, sha=peel, ok=bool(peel)))
    present = bool(_tok())
    L = ['b639 -- (R249)(4) PART ONE: THE DEPOSIT DESCRIPTION`S ITEMS, IN THE DEPOSIT NOTE`S OWN FORM, REFRESHED FROM b635`s BANK, NOTHING '
         'PUBLISHED (%s)' % utc(), '',
         '**Deposit preparations (`(R110)` route), the items.** Each item by its path and its head, the head read back at the remote. **The draft '
         'is the act; publishing is the author`s word.**', '']
    for x in items:
        L.append('- %s -- `%s` %s @ `%s` (remote main `%s`): %s%s' % (x['label'], x['repo'], x['path'] or '', x['head'][:7], x['remote'][:7],
                                                                      'RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', (' -- ' + x['extra']) if x['extra'] else ''))
    L += ['', '- every kernel tag REGISTRY cites, peeled at its remote (%d):' % len(tags)]
    L += ['    `%s` `%s` = `%s` %s' % (t['kernel'], t['tag'], t['sha'], 'RESOLVES' if t['ok'] else '### NOT AT THE REMOTE') for t in tags]
    L += ['', '- the supportable sentences, cut whole from README:'] + ['    :%d %s' % (n, s or '### NOT CUT') for n, s in sups]
    L += ['- the not-supportable sentence, unchanged: %s.' % (notsup or '### NOT CUT'),
          '- the record: Zenodo %s (concept %s), at %s; the new version %s; its title "%s"' % (K.RECORD, K.CONCEPT, K.RECORD_VERSION, K.VERSION, K.TITLE),
          '- the `(R110)` token: its location the environment variable %s; present %s; not printed, not read beyond its presence here.' % (K.TOKVAR,
                                                                                                                                          'YES' if present else 'NO')]
    text = NL.join(L)
    nd = R6.nd_hits(text, R6.nd_sets())[0]
    ok_all = all(x['ok'] for x in items)
    L += ['', '### ### **ITEMS %d ; RESOLVING %d ; TAGS %d ; RESOLVING %d ; NO-DISCLOSURE HITS %s ; TOKEN PRESENT %s ; ls-remote reads %s.**' % (
        len(items), sum(x['ok'] for x in items), len(tags), sum(t['ok'] for t in tags), dict(nd), present, len(cache))]
    put_txt('b639_deposit_items.txt', L)
    put_json('b639_deposit_items.json', dict(at=utc(), items=items, tags=tags, nd=dict(nd), all_resolve=ok_all, token_present=present,
                                             sups=sups, notsup=notsup, cen_sum=cen_sum, cen_commit=cen_commit, prov=prov, rows=len(T),
                                             roots_last=roots[-1], pp_head=pp_head, relay_head=relay_head, lsr=len(cache)))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE FILE LIST, (R249)(4) AND THE AUTHOR'S ANSWERS
def _label(b):
    m = re.search(rb'\bv(\d+\.\d+(?:\.\d+)?)\b', b[:4000])
    return ('v' + m.group(1).decode()) if m else None


def files(*a):
    """### the draft's file list: v1.1.2's eleven, each matched to its document -- replaced by its current edition where the document's bytes
    ### moved after the deposit, kept where they did not -- and the bank's three (the mirror's zip, the census at v0.6, the sieve at v0.6); every
    ### file's source, the PLACE-papers commit it is read at, its sha256, md5 and size, old -> new per document; the seven companions' line-diff
    ### counts against v1.1.2 and their labels; the no-disclosure arm over the file list and the text files' bytes."""
    import b616_record as R6
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    out = []
    for name, md5, src in K.INHERITED:
        dep = K.show_bytes('%s/%s' % (K.DEPOSITED_DIR, name))
        cur = K.show_bytes(src)
        same = hashlib.md5(cur).hexdigest() == md5
        new_name = name if (same or src != K.MONO) else os.path.basename(src)
        last = g(PP, 'log', '-1', '--format=%h %ad', '--date=short', '--', src).strip()
        dl = None
        if not same and name in COMPANIONS + ('ERRATA.md',):
            dl = sum(1 for x in difflib.unified_diff(dep.decode('utf-8', 'replace').split(NL), cur.decode('utf-8', 'replace').split(NL), lineterm='', n=0)
                     if x[:1] in '+-' and x[:3] not in ('+++', '---'))
        out.append(dict(kind='INHERITED, BYTE-IDENTICAL' if same else 'REPLACED BY ITS CURRENT EDITION', old=name, old_md5=md5,
                        old_dep_md5=hashlib.md5(dep).hexdigest() if dep is not None else None, name=new_name, source=src, commit=pp_head,
                        last_commit=last, sha256=hashlib.sha256(cur).hexdigest(), md5=hashlib.md5(cur).hexdigest(), size=len(cur),
                        diff_lines=dl, label_old=_label(dep or b''), label_new=_label(cur), companion=name in COMPANIONS))
    for src in K.BANK3:
        cur = K.show_bytes(src)
        out.append(dict(kind='ADDED (THE BANK`S)', old=None, name=os.path.basename(src), source=src, commit=pp_head,
                        last_commit=g(PP, 'log', '-1', '--format=%h %ad', '--date=short', '--', src).strip(),
                        sha256=hashlib.sha256(cur).hexdigest(), md5=hashlib.md5(cur).hexdigest(), size=len(cur)))
    zb = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else None
    out.append(dict(kind='ADDED (THE BANK`S)', old=None, name=os.path.basename(K.MIRROR_ZIP), source=K.MIRROR_ZIP, commit=None,
                    sha256=hashlib.sha256(zb).hexdigest() if zb else None, md5=hashlib.md5(zb).hexdigest() if zb else None, size=len(zb) if zb else None))
    names = [x['name'] for x in out]
    text_bytes = NL.join(K.show_bytes(x['source']).decode('utf-8', 'replace') for x in out if x['commit'] and x['source'].endswith('.md'))
    sets = R6.nd_sets()
    nd_list = R6.nd_hits(NL.join(names), sets)[0]
    nd_text = R6.nd_hits(text_bytes, sets)[0]
    dup = [n for n, c in collections.Counter(names).items() if c > 1]
    L = ['b639 -- (R249)(4) PART ONE: THE DRAFT`S FILE LIST, AS THE DEPOSIT NOTE NAMES IT AND THE AUTHOR`S ANSWERS MATCH IT (%s)' % utc(), '',
         '### v1.1.2`s eleven files, each matched to its document: a document whose bytes moved after the deposit has a newer edition whatever its '
         'label says, and the current edition is uploaded in its place; a byte-identical one is inherited. Then the bank`s three. Every source read '
         'at PLACE-papers %s (the mirror`s zip from disk).' % pp_head, '']
    for x in out:
        L.append('  %-46s %-32s sha256 %s ; md5 %s ; %s bytes' % (x['name'], x['kind'], x['sha256'], x['md5'], x['size']))
        L.append('      source %s @ %s (its last commit %s)%s%s' % (
            x['source'], x['commit'] or '(disk)', x.get('last_commit') or '-',
            (' ; old -> new: %s md5 %s -> %s' % (x['old'], x['old_md5'], x['md5'])) if x.get('old') else '',
            (' ; label %s -> %s ; %d lines differ from v1.1.2`s bytes' % (x['label_old'], x['label_new'], x['diff_lines'])) if x.get('diff_lines') is not None else ''))
    L += ['', '### names unique: %s ; the no-disclosure arm over the file list %s and over the text files` bytes %s' % (not dup, dict(nd_list), dict(nd_text)),
          '', '### ### **FILES %d ; REPLACED %d ; INHERITED %d ; ADDED %d ; EVERY SHA256 PRINTED %s.**' % (
              len(out), sum(1 for x in out if x['kind'].startswith('REPLACED')), sum(1 for x in out if x['kind'].startswith('INHERITED')),
              sum(1 for x in out if x['kind'].startswith('ADDED')), all(x['sha256'] for x in out))]
    put_txt('b639_deposit_files.txt', L)
    put_json('b639_deposit_files.json', dict(at=utc(), pp_head=pp_head, files=out, nd_list=dict(nd_list), nd_text=dict(nd_text), dup=dup))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE DESCRIPTION, IN THE READER'S ORDER, (R249)(4)(a)-(d)
DESC = 'b639_deposit_description.txt'
# ### the names the description defines in its own sentences (each defined where it enters), beside the glossary's keys
DESC_TERMS = ('DOI', 'Digital Object Identifier', 'Mathlib', 'Lean 4', 'README', 'GRH', 'OPEN', 'CITED', 'DISCHARGED IN KERNEL', 'ELSEWHERE',
              'Zenodo', 'MANIFEST', 'Li', 'Ostrowski', 'THE RECORD', 'WHAT IS CLAIMED', 'WHAT IS MACHINE-VERIFIED', 'WHAT THE KERNELS ASSUME',
              'WHAT REMAINS OPEN', 'THE CENSUS, THE ROOT CHAIN, THE TAGS AND THE TABLE', 'THE FILES', 'DEFINITIONS', 'THIS DESCRIPTION', 'RiemannHypothesis',
              'Platt', 'Trudgian', 'Nyman', 'Beurling', 'Bombieri', 'Lagarias', 'Weil', 'Dirichlet', 'Keiper', 'Epstein', 'Dedekind', 'ZFC')
DEF_KEYS = ('kernel', 'terminal', 'pin', 'SIDE-', 'Zeta23', 'Bulka', 'the terminal table', 'provenance', 'upstream', 'premise', 'DERIVES', 'INTERFACES',
            'T1-lit', 'the act root', 'the mirror', 'the sieve', 'keystone', 'OPEN_TRAILS', 'W-ORD', 'ERRATA', 'REGISTRY', 'FINDINGS', 'relay',
            'PLACE-papers', 'GRH_chi', 'Weil positivity', 'Li positivity', 'arithmetic-limit positivity', 'seam')


def _gl():
    import chain_page as CP
    return dict((k, d.replace('`', '')) for k, d, _s in CP.glossary_entries(os.path.join(D, 'glossary.txt')))


def _page_row(name):
    t = io.open(os.path.join(PP, K.PAGE), encoding='utf-8').read().replace(chr(13), '')
    for i, l in enumerate(t.split(NL), 1):
        if re.match(r'^\d+\. `[^`]*\.%s` — ' % re.escape(name), l):
            tag = re.search(r' — (v[\d.]+ = [0-9a-f]+) — ', l)
            ax = re.search(r'axioms: (\[[^\]]*\])', l)
            return i, tag.group(1) if tag else None, ax.group(1) if ax else None
    return None, None, None


def _b457(name):
    for l in rd('b457_profile_run.txt').split(NL):
        m = re.match(r"^'%s' depends on axioms: (\[.*\])$" % re.escape(name), l.strip())
        if m:
            return m.group(1)
    return None


def _status():
    S = jl('b639_premise_status.json')
    by = collections.defaultdict(list)
    for x in S.get('heads') or []:
        by[x['status']].append(x)
    return S, by


def compose():
    """### the description's HTML, paragraph by paragraph, every figure read from a bank; RETURN (html, the figures it read)."""
    gl = _gl()
    DI, FL, MI = jl('b639_deposit_items.json'), jl('b639_deposit_files.json'), jl('b639_mirror.json')
    S, by = _status()
    sups = dict((n, s) for n, s in DI.get('sups') or [])
    h_line, h_tag, h_ax = _page_row('h2_sign_iff_rh')
    l_line, l_tag, l_ax = _page_row('li_nonneg_iff_rh')
    a_line, a_tag, a_ax = _page_row('arith_limit_nonneg_iff_rh')
    ax457 = [_b457(n) for n in ('structural_exhaustiveness_proved', 'SpectralCannonFull.spectral_cannon', 'ConservationBridge.riemann_hypothesis')]
    ax457 = ax457[0] if len(set(ax457)) == 1 else '### THE THREE PRINTS DIFFER'
    names = lambda xs: ', '.join(x['head'] for x in xs)   # noqa: E731
    op = by.get('OPEN', [])
    op_own, op_ml = [x for x in op if not x['upstream']], [x for x in op if x['upstream']]
    dik = by.get('DISCHARGED IN KERNEL', [])
    hr = collections.defaultdict(list)
    for x in dik:
        hr[(x.get('handread') or '').split(' --')[0]].append(x['head'])
    wo_for = [(x['head'], x['wo_handread'][1].split(' (')[0]) for x in op if (x.get('wo_handread') or [''])[0] == 'FOR IT']
    wo_names = [x['head'] for x in op if (x.get('wo_handread') or [''])[0] == 'NAMES IT']
    wo_names_wo = sorted(set(x['wo_handread'][1].split(' (')[0] for x in op if (x.get('wo_handread') or [''])[0] == 'NAMES IT'))
    n_none = len(op) - len(wo_for) - len(wo_names)
    prov = DI.get('prov') or {}
    tags = ', '.join('%s %s = %s%s' % (t['kernel'], t['tag'], (t['sha'] or '')[:7], '' if t['ok'] else ' (not at its remote)') for t in DI.get('tags') or [])
    fls = FL.get('files') or []

    def fdesc(x):
        if x['kind'].startswith('ADDED'):
            what = {'THE_KEYSTONE_CENSUS_v0_6.md': 'the keystone census at v0.6',
                    'THE_FINDINGS_AS_THEY_STAND_v0_6.md': 'the sieve at v0.6, the table of the programme’s findings by cluster, each row with its verdict'}.get(
                x['name'], 'the mirror: the %s files of the project roster, flat, with a MANIFEST listing them, research history at every stage of edit '
                           'and not definitive where a newer edition supersedes it' % MI.get('files'))
            src = ('PLACE-papers %s' % x['source']) if x.get('commit') else 'built at this act by the programme’s mirror builder'
        elif x['kind'].startswith('INHERITED'):
            what, src = 'byte-identical to v1.1.2’s file', 'PLACE-papers %s' % x['source']
        elif x['old'] != x['name']:
            what, src = 'the monograph at its current edition, replacing v1.1.2’s %s (manuscript v5.10.2)' % x['old'], 'PLACE-papers %s' % x['source']
        elif x.get('companion'):
            what = 'its live file, its label %s unchanged, %d lines differing from v1.1.2’s' % (x.get('label_new'), x.get('diff_lines') or 0)
            src = 'PLACE-papers %s' % x['source']
        else:
            what = 'its current file, %d lines differing from v1.1.2’s' % (x.get('diff_lines') or 0)
            src = 'PLACE-papers %s' % x['source']
        return '%s (%s; %s; sha256 %s)' % (x['name'], what, src, x['sha256'])

    P = []
    P.append('THE RECORD. Version %s of the Zenodo record “%s” (concept DOI 10.5281/zenodo.%s, a DOI being a Digital Object Identifier), the deposit '
             'of A PLACE TO STAND, %s. This version replaces the files of %s that have moved since that deposit by their current editions, adds the '
             'programme’s keystone census at v0.6, its table of findings at v0.6 and a mirror of the corpus, and sets out, in this order, what is '
             'claimed, what is machine-verified, what the kernels assume and what remains open. Nothing in it states that the Riemann Hypothesis '
             'holds.' % (K.VERSION, K.TITLE, K.CONCEPT, gl['A PLACE TO STAND'], K.RECORD_VERSION))
    P.append('WHAT IS CLAIMED. RH is %s, Mathlib being the library of formalised mathematics for the Lean 4 proof assistant. The located clause: '
             '%s. Here classK is %s; h2_sign is %s; and h2_sign_iff_rh is %s.' % (
                 gl['RH'], gl['the located clause'], gl['classK'], gl['h2_sign'], gl['h2_sign_iff_rh']))
    P.append('The programme’s README, the front page of its corpus repository, states the claim in one sentence: “%s” For the versions v0.17 to '
             'v0.25 of the kernel SIDE-explicit-formula it carries two further sentences, quoted whole: “%s” and “%s” A name written with '
             'underscores or with joined capitals, such as h2_sign_iff_rh or PlattTrudgianHeight, is the name of a compiled declaration of the '
             'programme’s kernels and is defined by its statement there.' % (
                 sups.get(K.README_SUPPORT[0]), sups.get(K.README_SUPPORT[2]), sups.get(K.README_SUPPORT[3])))
    P.append('Not supportable, unchanged: %s. Here λ_n are Li’s coefficients, whose non-negativity for every n is compiled as equivalent to RH; '
             'simplicity is the simplicity clause the kernel states as a Prop beside h2_sign (simplicity_iff, v0.17), with no compiled edge '
             'between them; GRH_chi is %s; and the family theorem (family_theorem, v0.21) is compiled for a finite family at modulus q = 3.' % (
                 DI.get('notsup'), gl['GRH_chi']))
    P.append('WHAT IS MACHINE-VERIFIED. The programme’s kernels are Lean 4 repositories, one public repository each under github.com/psinary-sketch, '
             'each cited by named theorem at a pinned commit or tag; a theorem holds at the standard three when Lean’s #print axioms reports '
             'exactly propext, Classical.choice and Quot.sound, the axioms Lean’s own library rests on, so that no sorry, Lean’s mark for a '
             'missing proof, is among them. The equivalence: h2_sign_iff_rh, h2_sign ↔ RiemannHypothesis, both directions and no hypothesis, in '
             'SIDE-explicit-formula, compiled since its tag %s and read at v0.25 (commit %s), axioms %s (the generated page '
             'THE_CLAUSE_AND_ITS_COMPILED_FACES.md, line %s). Beside it, at the same reading, Li positivity, li_nonneg_iff_rh (since %s), and '
             'arithmetic-limit positivity, arith_limit_nonneg_iff_rh (since %s), each compiled as equivalent to RH, axioms %s and %s (lines %s '
             'and %s). The mechanism exclusions: the route terminals of SIDE-kernel at its tag v1.5 (commit 0e5233f; the kernel’s own record, DOI '
             '10.5281/zenodo.21520474) -- structural_exhaustiveness_proved, which states that the kernel’s mechanism type has seven members, that '
             'none of them produces the off-line signature the kernel defines, and Ostrowski’s classification of the places of the rationals, the '
             'exhaustiveness of the seven classes over all mechanisms being the manuscript’s theorem and not compiled (ERRATA E-2026-09-14-1); '
             'SpectralCannonFull.spectral_cannon; and ConservationBridge.riemann_hypothesis, whose premise ConservationHypothesis is RH restated by '
             'a compiled ten-line lemma (ERRATA E-2026-09-25-1) -- each printed by #print axioms at v1.5 as %s (relay data/b457_profile_run.txt).' % (
                 h_tag, K.EF_PIN, h_ax, h_line, l_tag, a_tag, l_ax, a_ax, l_line, a_line, ax457))
    P.append('WHAT THE KERNELS ASSUME. The programme’s terminal table (relay data/terminal_table.json, %d rows) grades each compiled declaration by '
             'reading its statement: DERIVES, %s; INTERFACES, %s. A premise is %s. By provenance, where a row’s grade comes from, the rows are '
             '%d cell, %d rule, %d rule-elab and %d none, with %d rows upstream, declarations outside every kernel, apart. The keystone census at '
             'v0.6 counts the named premises the INTERFACES rows rest on and states its own sum: “%s” Its 50 premise heads are classed here by '
             'status, computed from the kernels at the commits the table read them at and not assigned by hand (relay data/b639_premise_status.txt): '
             '%d OPEN, %d CITED, %d discharged in another kernel, %d DISCHARGED IN KERNEL. OPEN: no construction inside the kernels and no '
             'literature citation of every field -- %d of them the programme’s own named premises (%s) and %d general predicates of Mathlib’s '
             'taken as hypotheses of general lemmas (%s). CITED: a literature theorem carried as a premise with every field cited -- %s. '
             'DISCHARGED IN KERNEL: the hypothesis of an internal lemma, constructed in the same kernel, by a declaration with no hypothesis of its '
             'own or inside a proof, where a theorem uses the lemma -- %s; by the seat’s hand-read, %d of these are built where a theorem hands '
             'them to the lemma (%s), %d are general predicates of Mathlib’s whose instances the kernels construct (%s), and %d have only a '
             'concrete witness that the hypothesis can hold (%s). A construction inside a salt check, a file that only shows a premise is not '
             'vacuous, discharges nothing. The census prints this status column at its next edition, v0.7, pending the author’s word.' % (
                 DI.get('rows'), gl['DERIVES'], gl['INTERFACES'], gl['premise'], prov.get('cell', 0), prov.get('rule', 0), prov.get('rule-elab', 0),
                 prov.get('none', 0), prov.get('upstream', 0), (DI.get('cen_sum') or '').strip('*'), len(op), len(by.get('CITED', [])),
                 len(by.get('DISCHARGED ELSEWHERE', [])), len(dik), len(op_own), names(op_own), len(op_ml), names(op_ml), names(by.get('CITED', [])),
                 names(dik), len(hr['AT A USE']), ', '.join(hr['AT A USE']), len(hr['INSTANCES']), ', '.join(hr['INSTANCES']), len(hr['WITNESS ONLY']),
                 ', '.join(hr['WITNESS ONLY'])))
    if not wo_for and not wo_names:
        sys.exit('### THE STATUS BANK CARRIES NO WORK-ORDER HAND-READ -- NOTHING COMPOSED')
    P.append('WHAT REMAINS OPEN. The located clause itself: h2_sign, which no kernel proves and which the theorems that assume it carry as their '
             'premise; it is not among the 50 heads, since the equivalence h2_sign_iff_rh has none. Then the %d OPEN heads above. The programme’s '
             'ledger of open work, OPEN_TRAILS, carries a work-order for %s; it names %s on the work-order line %s for another purpose, their '
             'quantifier shape; no work-order is entered for the other %d.' % (
                 len(op), '; '.join('%s (%s)' % x for x in wo_for), ' and '.join(wo_names), ', '.join(wo_names_wo), n_none))
    P.append('THE CENSUS, THE ROOT CHAIN, THE TAGS AND THE TABLE. The keystone census at v0.6: PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_6.md '
             'at commit %s (github.com/psinary-sketch/PLACE-papers). The root chain: relay data/act_roots.txt, its last line at this description '
             '%s %s…; the act root of this act, b639, is computed at its record over the act’s banks, this draft’s read-back among them, and lands '
             'in the next mirror’s MANIFEST. The kernel tags the registry cites, each peeled at its remote: %s. The terminal table at relay %s: %d '
             'rows; provenance %d cell, %d rule, %d rule-elab, %d none, and %d upstream rows apart.' % (
                 DI.get('cen_commit'), (DI.get('roots_last') or '').split()[0], (DI.get('roots_last') or '  ').split()[1][:16], tags,
                 (DI.get('relay_head') or '')[:8], DI.get('rows'), prov.get('cell', 0), prov.get('rule', 0), prov.get('rule-elab', 0), prov.get('none', 0),
                 prov.get('upstream', 0)))
    P.append('THE FILES (%d), each with its source and its sha256, read at PLACE-papers commit %s: %s.' % (len(fls), FL.get('pp_head'), '; '.join(fdesc(x) for x in fls)))
    P.append('DEFINITIONS, in the programme’s glossary’s words (relay data/glossary.txt): %s.' % '; '.join('%s -- %s' % (k, gl[k]) for k in DEF_KEYS if k in gl))
    P.append('THIS DESCRIPTION was composed at the programme’s act b639, an act being one numbered session of the programme’s work under the '
             'author’s ruling (b638 the act before it), from relay data/b639_deposit_items.txt, data/b639_premise_status.txt and '
             'data/b639_deposit_files.txt, and is banked as data/%s (github.com/psinary-sketch/relay).' % DESC)
    html = ''.join('<p>%s</p>' % p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') for p in P)
    return html, dict(h=(h_line, h_tag, h_ax), l=(l_line, l_tag, l_ax), a=(a_line, a_tag, a_ax), ax457=ax457, open=len(op), cited=len(by.get('CITED', [])),
                      dik=len(dik), files=len(fls))


def desc_scan(html):
    """### the description's scans: the whole-document scanner over its text; the glossary-key scan -- every internal name (backticked spans,
    ### upper-case tokens, snake_case identifiers, SIDE- names, act numbers, rulings, tiers) inside a glossary key, a term the description
    ### defines, a premise head or a declaration of the table; every glossary key it uses defined in its DEFINITIONS or its own sentences;
    ### characters HTML would read as markup apart from the paragraph tags; the no-disclosure arm."""
    import html as HT
    import b616_record as R6
    raw_text = re.sub(r'</?p>', NL, html)
    markup = [m.group(0) for m in re.finditer(r'[<>]|&(?!(amp|lt|gt);)', raw_text)]
    text = HT.unescape(raw_text)
    keys = list(_gl())
    decl = set(r['name'].split('.')[-1] for r in _table()) | set(r['name'] for r in _table())
    heads = set(x['head'] for x in jl('b639_premise_status.json').get('heads') or [])
    paths = ' '.join(re.findall(r'[\w./-]+\.(?:md|txt|html|svg|json|zip|lean)\b', text))
    names = sorted(set(m.group(0).strip('`') for p in R8.NAME_PATS for m in re.finditer(p, text)))

    def kernel_declares(n):
        return any(subprocess.run(['git', '-C', rp, 'grep', '-q', '-w', n, pin, '--', '*.lean']).returncode == 0
                   for rp, pin in ((K.EF, K.EF_PIN), ('D:/SIDE-kernel', 'v1.5')))

    def ok(n):
        return (any(n in k or (k in n and len(k) > 1) for k in keys) or any(n in t or t in n for t in DESC_TERMS) or n in heads or n in decl
                or n.split('.')[-1] in decl or re.match(r'^v\d', n) is not None or re.match(r'^E-\d{4}-\d\d-\d\d-\d+$', n) is not None
                or re.match(r'^b\d{3}$', n) is not None or (n in paths and re.search(r'[\w./-]*%s[\w./-]*\.\w+' % re.escape(n), paths) is not None))
    undefined = [n for n in names if not ok(n)]
    undefined = [n for n in undefined if not (re.search(r'[a-z]_[a-z]|[a-z][A-Z]', n) and kernel_declares(n))]
    p = os.path.join(SP if DRY else D, 'b639_scanfile_description.md')
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    nd = R6.nd_hits(text, R6.nd_sets())[0]
    return dict(names=names, undefined=undefined, markup=markup, clean=_clean(out), scanner=out[-1600:], nd=dict(nd), chars=len(html),
                bytes=len(html.encode('utf-8')))


def describe(*a):
    """### data/b639_deposit_description.txt -- the description's HTML exactly as it goes to the service, no newline added -- and
    ### data/b639_description_scan.txt with its json: the scanner, the glossary-key scan and the no-disclosure arm over it and the file list."""
    import b616_record as R6
    html, fig = compose()
    sc = desc_scan(html)
    fl = [x['name'] for x in jl('b639_deposit_files.json').get('files') or []]
    ndl = R6.nd_hits(NL.join(fl), R6.nd_sets())[0]
    p = os.path.join(SP if DRY else D, DESC)
    _write(p, html.encode('utf-8'))
    L = ['b639 -- (R249)(4) PART ONE: THE DESCRIPTION, COMPOSED FROM THE BANKS IN THE READER`S ORDER, AND ITS SCANS (%s)' % utc(), '',
         '### the bank: data/%s, %d bytes, sha256 %s, %d paragraphs' % (DESC, sc['bytes'], hashlib.sha256(html.encode('utf-8')).hexdigest(), html.count('<p>')),
         '### the figures read: %s' % fig,
         '### the scanner (tools/banned_terms.py --new over its text): %s' % ('CLEAN' if sc['clean'] else '### NOT CLEAN'),
         '### the glossary-key scan: internal names %d ; outside every glossary key, the description`s own terms, the premise heads and the '
         'table`s declarations: %s' % (len(sc['names']), sc['undefined'] or 'NONE'),
         '### characters markup would read, outside the paragraph tags: %s' % (sc['markup'] or 'NONE'),
         '### the no-disclosure arm over the description %s and over the file list %s' % (sc['nd'], dict(ndl)), '',
         '### ### **DESCRIPTION %d BYTES ; SCANNER %s ; NAMES UNDEFINED %d ; MARKUP %d ; NO-DISCLOSURE %d + %d.**' % (
             sc['bytes'], 'CLEAN' if sc['clean'] else 'NOT CLEAN', len(sc['undefined']), len(sc['markup']), sum(sc['nd'].values()), sum(ndl.values())),
         '', '### THE NAMES READ: %s' % sc['names']]
    if not sc['clean']:
        L += ['', '### THE SCANNER`S TAIL:'] + sc['scanner'].split(NL)
    put_txt('b639_description_scan.txt', L)
    put_json('b639_description_scan.json', dict(at=utc(), sha256=hashlib.sha256(html.encode('utf-8')).hexdigest(), bytes=sc['bytes'], clean=sc['clean'],
                                                undefined=sc['undefined'], markup=sc['markup'], nd_desc=sc['nd'], nd_list=dict(ndl), figures=fig,
                                                names=sc['names']))
    print(L[-3] if sc['clean'] else L[-3])


# ================================================================================ COMPONENT 2: THE (R110) ROUTE -- THE DRAFT, (R249)(4) PART ONE
ZRES = 'b639_zenodo.json'


def http(method, url, body=None, auth=True, raw=None, ctype=None):
    """### one request; the token only in the Authorization header; no identifier of the author in any header."""
    h = {'User-Agent': 'relay-b639/1.0', 'Accept': 'application/json'}
    if auth:
        h['Authorization'] = 'Bearer ' + _tok()
    data = None
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode('utf-8')
        h['Content-Type'] = 'application/json'
    elif raw is not None:
        data = raw
        h['Content-Type'] = ctype or 'application/octet-stream'
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return -1, ('### %s' % e).encode('utf-8')


def _zres():
    return jl(ZRES)


def _zmerge(cells):
    R = _zres()
    R.update(cells)
    put_json(ZRES, R)


def _j(b):
    try:
        return json.loads(b.decode('utf-8'))
    except Exception:
        return None


def z_token(*a):
    """### the token's location confirmed to exist; nothing read beyond its presence and length; no call."""
    t = _tok()
    L = ['b639 -- THE (R110) TOKEN`S LOCATION (%s)' % utc(), '', '### the environment variable %s : set %s ; length %d ; not printed, no call made' % (
        K.TOKVAR, bool(t), len(t))]
    put_txt('b639_zenodo_token.txt', L)
    _zmerge(dict(token=dict(set=bool(t), length=len(t), at=utc())))
    print(L[-1])


def _deposition_digest(j):
    md = (j or {}).get('metadata') or {}
    fs = (j or {}).get('files') or []
    return dict(id=(j or {}).get('id'), state=(j or {}).get('state'), submitted=(j or {}).get('submitted'), title=md.get('title'),
                version=md.get('version'), publication_date=md.get('publication_date'), doi=md.get('prereserve_doi') or (j or {}).get('doi'),
                files=[dict(id=f.get('id'), name=f.get('filename'), md5=f.get('checksum'), size=f.get('filesize')) for f in fs],
                keys=sorted(md))


def z_new(*a):
    """### step NEW: one new version of record 21539167 through the route -- POST actions/newversion on the record (the latest version, its
    ### id the deposition's), the new draft read once at the link the service returns; banked whole (the token absent). Refuses to run twice."""
    R = _zres()
    if (R.get('new') or {}).get('draft_id'):
        sys.exit('### THE DRAFT EXISTS (%s) -- A SECOND NEW VERSION IS NOT MADE' % R['new']['draft_id'])
    if not _tok():
        sys.exit('### THE TOKEN IS NOT SET -- NO CALL MADE')
    base = '%s/deposit/depositions/%s' % (K.API, K.RECORD)
    st, b = http('POST', base + '/actions/newversion')
    j = _j(b)
    L = ['b639 -- THE (R110) ROUTE, STEP NEW: A NEW VERSION OF RECORD %s, AS A DRAFT (%s)' % (K.RECORD, utc()), '',
         '### POST %s/actions/newversion : HTTP %d at %s' % (base.replace(K.API, '/api'), st, utc())]
    cell = dict(newversion=st, at=utc())
    if st not in (200, 201) or not j:
        L += ['    | %s' % _tclean(b.decode('utf-8', 'replace'))[:1200], '### ### **STOP: NO DRAFT MADE BY THIS CALL.**']
        put_txt('b639_zenodo_new.txt', L)
        _zmerge(dict(new=cell))
        sys.exit(2)
    latest = ((j.get('links') or {}).get('latest_draft') or '')
    if not latest and str(j.get('id')) != K.RECORD:
        latest = '%s/deposit/depositions/%s' % (K.API, j.get('id'))     # ### the response is the new draft itself
    if not latest:
        L += ['    | %s' % _tclean(b.decode('utf-8', 'replace'))[:1200], '### ### **STOP: THE RESPONSE NAMES NO DRAFT.**']
        put_txt('b639_zenodo_new.txt', L)
        _zmerge(dict(new=cell))
        sys.exit(2)
    st2, b2 = http('GET', latest)
    d = _j(b2)
    dg = _deposition_digest(d)
    cell.update(latest_draft=latest, get=st2, draft_id=dg['id'], digest=dg, bucket=((d or {}).get('links') or {}).get('bucket'))
    put_json('b639_zenodo_draft_new.json', d or {})
    L += ['### the response: the record %s ; its latest_draft link %s' % (j.get('id'), latest.replace(K.API, '/api')),
          '### GET the draft : HTTP %d ; id %s ; state %s ; submitted %s ; title %s ; version %s ; publication date %s ; reserved DOI %s' % (
              st2, dg['id'], dg['state'], dg['submitted'], dg['title'], dg['version'], dg['publication_date'], dg['doi']),
          '### the draft`s files as the service lists them (%d):' % len(dg['files'])] + ['    %-46s md5 %s ; %s bytes ; id %s' % (
              f['name'], f['md5'], f['size'], f['id']) for f in dg['files']] + [
          '### the metadata keys: %s' % dg['keys'], '', '### ### **DRAFT %s MADE ; %d FILES INHERITED ; NOTHING PUBLISHED.**' % (dg['id'], len(dg['files']))]
    put_txt('b639_zenodo_new.txt', L)
    _zmerge(dict(new=cell))
    print(L[-1])


def z_files(*a):
    """### step FILES: the draft's files made the bank's -- each inherited file the bank replaces deleted, each file the bank names and the draft
    ### lacks uploaded to the draft's bucket from its source bytes; every call's status banked. Refuses without a draft or a file bank."""
    R = _zres()
    nw = R.get('new') or {}
    did, bucket = nw.get('draft_id'), nw.get('bucket')
    FL = jl('b639_deposit_files.json').get('files') or []
    if not did or not bucket or not FL:
        sys.exit('### NO DRAFT, NO BUCKET OR NO FILE BANK -- NOTHING DONE')
    if R.get('files'):
        sys.exit('### THE FILES STEP HAS RUN -- IT DOES NOT RUN TWICE')
    base = '%s/deposit/depositions/%s' % (K.API, did)
    st, b = http('GET', base + '/files')
    have = _j(b) or []
    have_by = dict((f.get('filename'), f) for f in have)
    want = dict((x['name'], x) for x in FL)
    gone = [x['old'] for x in FL if x['kind'].startswith('REPLACED') and x['old'] in have_by and x['old'] != x['name']] + \
           [x['name'] for x in FL if x['kind'].startswith('REPLACED') and x['name'] in have_by]
    L = ['b639 -- THE (R110) ROUTE, STEP FILES: THE DRAFT %s`S FILES MADE THE BANK`S (%s)' % (did, utc()), '',
         '### GET files : HTTP %d ; %d listed' % (st, len(have))]
    calls = []
    for n in gone:
        sd, bd = http('DELETE', '%s/files/%s' % (base, have_by[n]['id']))
        calls.append(dict(op='DELETE', name=n, status=sd))
        L.append('    DELETE %-46s : HTTP %d' % (n, sd))
    now = set(have_by) - set(gone)
    for n, x in want.items():
        if n in now and x['kind'].startswith('INHERITED'):
            L.append('    KEEP   %-46s (inherited, byte-identical; the service`s md5 %s)' % (n, have_by[n].get('checksum')))
            calls.append(dict(op='KEEP', name=n, status=None))
            continue
        src = open(x['source'], 'rb').read() if x['commit'] is None else K.show_bytes(x['source'], x['commit'])
        if hashlib.sha256(src).hexdigest() != x['sha256']:
            L.append('    ### %s : ITS SOURCE BYTES DIFFER FROM THE BANK`S -- NOT UPLOADED' % n)
            calls.append(dict(op='REFUSED', name=n, status=None))
            continue
        su, bu = http('PUT', '%s/%s' % (bucket, urllib.request.quote(n)), raw=src)
        ju = _j(bu) or {}
        calls.append(dict(op='PUT', name=n, status=su, checksum=ju.get('checksum'), size=ju.get('size')))
        L.append('    PUT    %-46s : HTTP %d ; the service`s checksum %s ; %s bytes' % (n, su, ju.get('checksum'), ju.get('size')))
    bad = [c for c in calls if c['op'] in ('DELETE', 'PUT') and c['status'] not in (200, 201, 204)] + [c for c in calls if c['op'] == 'REFUSED']
    L += ['', '### ### **DELETED %d ; UPLOADED %d ; KEPT %d ; FAILED %d.**' % (sum(c['op'] == 'DELETE' for c in calls), sum(c['op'] == 'PUT' for c in calls),
                                                                              sum(c['op'] == 'KEEP' for c in calls), len(bad))]
    put_txt('b639_zenodo_files.txt', L)
    _zmerge(dict(files=dict(calls=calls, at=utc(), failed=len(bad))))
    print(L[-1])


def z_meta(*a):
    """### step META: the draft's metadata PUT once -- every key the draft carries kept, the description the bank's bytes, the version the
    ### author's answer, the title checked equal to the record's, the publication date the day of this step (UTC)."""
    R = _zres()
    did = (R.get('new') or {}).get('draft_id')
    if not did or R.get('meta'):
        sys.exit('### NO DRAFT, OR THE META STEP HAS RUN -- NOTHING DONE')
    desc = open(os.path.join(D, DESC), 'rb').read().decode('utf-8')
    base = '%s/deposit/depositions/%s' % (K.API, did)
    st, b = http('GET', base)
    d = _j(b) or {}
    md = dict(d.get('metadata') or {})
    if md.get('title') != K.TITLE:
        sys.exit('### THE DRAFT`S TITLE IS NOT THE RECORD`S (%r) -- NOTHING WRITTEN' % md.get('title'))
    before = dict(md)
    md['description'] = desc
    md['version'] = K.VERSION
    md['publication_date'] = time.strftime('%Y-%m-%d', time.gmtime())
    if md.get('doi') == '10.5281/zenodo.%s' % K.RECORD:
        md.pop('doi')                          # ### v1.1.2's own DOI is never carried onto the new version; a reserved one is the service's
    changed = sorted(k for k in set(md) | set(before) if md.get(k) != before.get(k))
    sp, bp = http('PUT', base, body={'metadata': md})
    jp = _j(bp) or {}
    L = ['b639 -- THE (R110) ROUTE, STEP META: THE DRAFT %s`S METADATA, PUT ONCE (%s)' % (did, utc()), '',
         '### GET the draft : HTTP %d ; PUT metadata : HTTP %d' % (st, sp),
         '### keys carried %d ; keys changed %s ; the title kept "%s" ; the version %s ; the publication date %s' % (
             len(md), changed, md.get('title'), md.get('version'), md.get('publication_date'))]
    if sp != 200:
        L.append('    | %s' % _tclean(bp.decode('utf-8', 'replace'))[:1500])
    L += ['', '### ### **META %s.**' % ('WRITTEN' if sp == 200 else '### REFUSED BY THE SERVICE')]
    put_txt('b639_zenodo_meta.txt', L)
    _zmerge(dict(meta=dict(get=st, put=sp, changed=changed, version=md.get('version'), publication_date=md.get('publication_date'), at=utc())))
    print(L[-1])


def z_read(*a):
    """### step READ: the draft read back from the service once -- its identifier, title, version, description and file list with the service's
    ### digests -- and every file downloaded once and its sha256 computed; compared to the banks, every difference printed; H73a-H73c scored."""
    import b616_record as R6
    R = _zres()
    did = (R.get('new') or {}).get('draft_id')
    if not did:
        sys.exit('### NO DRAFT -- NOTHING READ')
    base = '%s/deposit/depositions/%s' % (K.API, did)
    st, b = http('GET', base)
    d = _j(b) or {}
    put_json('b639_zenodo_readback.json', d)
    md = d.get('metadata') or {}
    desc_bank = open(os.path.join(D, DESC), 'rb').read()
    desc_back = (md.get('description') or '').encode('utf-8')
    FL = dict((x['name'], x) for x in jl('b639_deposit_files.json').get('files') or [])
    rows = []
    for f in d.get('files') or []:
        n = f.get('filename')
        dl = ((f.get('links') or {}).get('download'))
        sd, bd = http('GET', dl) if dl else (-1, b'')
        s256 = hashlib.sha256(bd).hexdigest() if sd == 200 else None
        want = FL.get(n)
        rows.append(dict(name=n, md5=f.get('checksum'), size=f.get('filesize'), get=sd, sha256=s256, bank=(want or {}).get('sha256'),
                         ok=bool(want) and s256 == want['sha256'] and (f.get('checksum') or '').replace('md5:', '') == want['md5']))
    missing = sorted(set(FL) - set(r['name'] for r in rows))
    extra = [r['name'] for r in rows if r['name'] not in FL]
    h73a = bool(rows) and all(r['ok'] for r in rows) and not missing and not extra
    h73b = desc_back == desc_bank
    dd = []
    if not h73b:
        sm = difflib.SequenceMatcher(None, desc_bank.decode('utf-8'), desc_back.decode('utf-8'))
        dd = [(op, desc_bank.decode('utf-8')[i1:i2][:120], desc_back.decode('utf-8')[j1:j2][:120]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal'][:40]
    sets = R6.nd_sets()
    nd_d = R6.nd_hits(desc_bank.decode('utf-8'), sets)[0]
    nd_l = R6.nd_hits(NL.join(FL), sets)[0]
    h73c = not any(nd_d.values()) and not any(nd_l.values())
    L = ['b639 -- THE (R110) ROUTE, STEP READ: THE DRAFT READ BACK FROM THE SERVICE AND COMPARED TO THE BANKS (%s)' % utc(), '',
         '### GET the draft : HTTP %d ; identifier %s ; state %s ; submitted %s' % (st, d.get('id'), d.get('state'), d.get('submitted')),
         '### title : %s ; version : %s ; publication date : %s ; reserved DOI : %s' % (md.get('title'), md.get('version'), md.get('publication_date'),
                                                                                   (md.get('prereserve_doi') or {}).get('doi') if isinstance(md.get('prereserve_doi'), dict) else md.get('prereserve_doi')),
         '### the description : %d bytes read back against the bank`s %d ; byte for byte %s' % (len(desc_back), len(desc_bank), h73b)]
    L += ['    %s : bank %r ; service %r' % x for x in dd]
    L += ['### the files (%d read back, %d in the bank):' % (len(rows), len(FL))]
    L += ['    %-46s service md5 %s ; %s bytes ; download HTTP %s ; sha256 %s ; bank %s ; %s' % (
        r['name'], r['md5'], r['size'], r['get'], r['sha256'], r['bank'], 'AGREE' if r['ok'] else '### DIFFER') for r in rows]
    L += ['### in the bank, not in the draft: %s ; in the draft, not in the bank: %s' % (missing or 'NONE', extra or 'NONE'),
          '### the no-disclosure arm over the description %s and the file list %s' % (dict(nd_d), dict(nd_l)), '',
          '### ### **H73a %s ; H73b %s ; H73c %s. THE DRAFT %s, %d FILES, NOTHING PUBLISHED.**' % (
              'HOLDS' if h73a else 'REFUTED', 'HOLDS' if h73b else 'REFUTED', 'HOLDS' if h73c else 'REFUTED', d.get('id'), len(rows))]
    put_txt('b639_zenodo_read.txt', L)
    _zmerge(dict(read=dict(get=st, id=d.get('id'), state=d.get('state'), submitted=d.get('submitted'), title=md.get('title'), version=md.get('version'),
                           files=rows, missing=missing, extra=extra, desc_equal=h73b, h73a=h73a, h73b=h73b, h73c=h73c, at=utc(),
                           n_files=len(rows))))
    print(L[-1])
    print(PROMPT % (d.get('id'), len(rows)))


PROMPT = ('The deposit draft is at %s, %d files, description banked at data/b639_deposit_description.txt and read back from the service. '
          'Publishing is yours: answer publish, or hold.')


# ================================================================================ COMPONENT 3: THE WORD, (R249)(4) PART TWO
def _word():
    """### the author's word on the draft, from the answers bank: 'publish', 'hold' or None."""
    t = rd('b639_author_answers.txt')
    blk = [b for b in re.split(r'^### CALL ', t, flags=re.M) if 'Publishing is yours: answer publish, or hold.' in b]
    if not blk:
        return None
    res = re.search(r'^RESULT \(transcript line \d+\): (.*)', blk[-1], re.M | re.S)
    a = (res.group(1) if res else '').split('"="')[-1].lower()
    return 'publish' if re.match(r'\s*publish\b', a) else ('hold' if re.match(r'\s*hold\b', a) else None)


def z_publish(*a):
    """### step PUBLISH, on the author's word alone: the draft published through the route; the record's new version identifier and DOI read
    ### back from the service anonymously and printed."""
    R = _zres()
    did = (R.get('new') or {}).get('draft_id')
    w = _word()
    if w != 'publish':
        sys.exit('### THE AUTHOR`S WORD IS %r, NOT "publish" -- NOTHING PUBLISHED' % w)
    if not did or R.get('publish'):
        sys.exit('### NO DRAFT, OR THE PUBLISH STEP HAS RUN -- NOTHING DONE')
    base = '%s/deposit/depositions/%s' % (K.API, did)
    sp, bp = http('POST', base + '/actions/publish')
    jp = _j(bp) or {}
    L = ['b639 -- THE (R110) ROUTE, STEP PUBLISH: THE DRAFT %s PUBLISHED ON THE AUTHOR`S WORD (%s)' % (did, utc()), '',
         '### POST actions/publish : HTTP %d at %s ; the response`s id %s ; doi %s ; record id %s' % (sp, utc(), jp.get('id'), jp.get('doi'), jp.get('record_id'))]
    if sp not in (200, 202):
        L.append('    | %s' % _tclean(bp.decode('utf-8', 'replace'))[:1500])
        put_txt('b639_zenodo_publish.txt', L)
        _zmerge(dict(publish=dict(status=sp, at=utc())))
        sys.exit(2)
    rid = jp.get('record_id') or jp.get('id')
    got = None
    for n in range(6):
        fs, fb = http('GET', '%s/records/%s' % (K.API, rid), auth=False)
        gj = _j(fb) or {}
        L.append('### anonymous GET /api/records/%s try %d : HTTP %d ; doi %s ; version %s ; title %s' % (
            rid, n + 1, fs, gj.get('doi'), (gj.get('metadata') or {}).get('version'), (gj.get('metadata') or {}).get('title')))
        if fs == 200 and gj.get('doi'):
            got = gj
            break
        time.sleep(10)
    if got:
        put_json('b639_zenodo_record.json', got)
    L += ['', '### ### **PUBLISHED: RECORD %s ; DOI %s ; VERSION %s.**' % (rid, (got or {}).get('doi'), ((got or {}).get('metadata') or {}).get('version'))]
    put_txt('b639_zenodo_publish.txt', L)
    _zmerge(dict(publish=dict(status=sp, record_id=rid, doi=(got or {}).get('doi'), version=((got or {}).get('metadata') or {}).get('version'),
                              title=((got or {}).get('metadata') or {}).get('title'), conceptdoi=(got or {}).get('conceptdoi'), at=utc())))
    print(L[-1])


def z_doi(*a):
    """### the DOI resolved once at its registry (DataCite's REST API, no identifier of the author in the request): the title and version printed;
    ### H73d -- they equal the description's title and version."""
    R = _zres()
    doi = (R.get('publish') or {}).get('doi')
    if not doi:
        sys.exit('### NO DOI BANKED -- NOTHING READ')
    st, b = http('GET', 'https://api.datacite.org/dois/%s' % doi, auth=False)
    j = _j(b) or {}
    at = (j.get('data') or {}).get('attributes') or {}
    titles = [t.get('title') for t in at.get('titles') or []]
    ver = at.get('version')
    url = at.get('url')
    h73d = K.TITLE in titles and ver == K.VERSION
    L = ['b639 -- THE DOI AT ITS REGISTRY, READ ONCE (%s)' % utc(), '',
         '### GET https://api.datacite.org/dois/%s : HTTP %d ; titles %s ; version %s ; url %s ; state %s' % (doi, st, titles, ver, url, at.get('state')),
         '### the description`s title "%s" and version %s' % (K.TITLE, K.VERSION), '', '### ### **H73d %s.**' % ('HOLDS' if h73d else 'REFUTED')]
    put_txt('b639_zenodo_doi.txt', L)
    _zmerge(dict(doi_read=dict(status=st, titles=titles, version=ver, url=url, h73d=h73d, at=utc())))
    print(L[-1])


def z_hold(*a):
    """### on "hold": the draft's identifier banked, nothing published, the service read once to print the draft's state as it leaves it."""
    R = _zres()
    did = (R.get('new') or {}).get('draft_id')
    if _word() != 'hold' or not did:
        sys.exit('### THE WORD IS NOT "hold", OR NO DRAFT -- NOTHING DONE')
    st, b = http('GET', '%s/deposit/depositions/%s' % (K.API, did))
    d = _j(b) or {}
    L = ['b639 -- THE DRAFT HELD ON THE AUTHOR`S WORD (%s)' % utc(), '', '### the draft %s : HTTP %d ; state %s ; submitted %s ; nothing published' % (
        did, st, d.get('state'), d.get('submitted'))]
    put_txt('b639_zenodo_hold.txt', L)
    _zmerge(dict(hold=dict(id=did, state=d.get('state'), submitted=d.get('submitted'), at=utc())))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES, WHERE THE GLOSSARY'S DEPOSIT ENTRY CHANGES THEM
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from the list in force (b638's) and b635's probe (no Lean), written only where it
    ### changed; the free memory printed before the call; the diff read by kind and banked (data/b639_page_<k>.json)."""
    CP = R8._cp()
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, nl), os.path.join(SP, '_b639_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    bank = 'b639_page_%s.json' % k
    if rc:
        put_json(bank, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    if DRY:
        _write(os.path.join(SP, 'b639_page_%s.md' % k), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))

    def kind(x):
        s = x[1:]
        if s.startswith('- **') or s in ('## Glossary',) or s.startswith('*The internal names this document uses'):
            return 'glossary'
        if s.startswith('This page is generated by relay'):
            return 'head line'
        if s.startswith('| keystone naming a node |'):
            return 'placement row'
        if s.startswith('|'):
            return 'correspondence row'
        if s.startswith('#'):
            return 'heading'
        return 'prose' if s.strip() else 'blank'
    kinds = collections.Counter(kind(x) + x[0] for x in dl)
    gl = R8.glossary_lines(pg)
    put_json(bank, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved, kinds=dict(kinds),
                        glossary_lines=len(gl), glossary_sha256=sha((NL.join(gl) + NL).encode('utf-8')) if gl else None, free_mb_before=fm,
                        seconds=secs, nodes=nl, probe=pr, at=utc(), dry=DRY))
    print('  %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d by kind %s ; cells moved %s ; glossary lines %d' % (
        k, rc, changed, secs, len(dl), dict(kinds), gmoved or 'NONE', len(gl)))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b639 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b639_gcp'), os.path.join(D, K.PROBE[k]))
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
    put_txt('b639_page_arms.txt', L)
    for l in L:
        print(l[:240])


# ================================================================================ THE TABLE AT THE END
def table(*a):
    """### the terminal table regenerated; every row whose grade, provenance, mark or kind moved printed (data/b639_table_<tag>.txt, json)."""
    rows0 = _table()
    before = R8.R7._table_state(rows0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = _table()
    after = R8.R7._table_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    tag = a[0] if a and a[0] != 'dry' else 'final'
    files_ = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    L = ['b639 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows %d ; added %d ; gone %d ; grade, provenance, mark or kind moved %d ; the table files that moved against relay HEAD: %s' % (
             len(rows1), len(added), len(gone), len(moved), files_ or 'NONE'),
         '### provenance under the exclusion: %s' % R8._prov_counts(rows1), '### EVERY MOVE:']
    L += ['  MOVED %s / %-62s %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved]
    L += ['  ADDED %s / %s %s' % (k[0], k[1], after[k]) for k in added] + ['  GONE  %s / %s %s' % (k[0], k[1], before[k]) for k in gone]
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone),
                                                                               sum(1 for k in moved if before[k][0] != after[k][0]))]
    if r.returncode:
        L += ['### THE GENERATOR EXITED %d:' % r.returncode] + (r.stdout + r.stderr).rstrip(NL).split(NL)[-15:]
    put_txt('b639_table_%s.txt' % tag, L)
    put_json('b639_table_%s.json' % tag, dict(at=utc(), rc=r.returncode, moved=[[k[0], k[1], list(before[k]), list(after[k])] for k in moved],
                                              added=[list(k) for k in added], gone=[list(k) for k in gone], files_moved=files_,
                                              grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]], prov=R8._prov_counts(rows1)))
    print(L[2])
    print(L[-1])


# ================================================================================ COMPONENT 4: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b639_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b639_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks() + [K.GLOSSARY]
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b639'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b639_act_root.json')
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
    L = ['b639 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b639_root_arm.txt', L)
    put_json('b639_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
HKEYS = ('H73a', 'H73b', 'H73c', 'H73d', 'H73e')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b638_closing_push_out.txt', 'data/act_roots.txt', K.GLOSSARY, K.ROSTER, 'tools/mirror_prevbuild.json'}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md', K.PAGE, K.DIR_PAGE)
N5_PP_ON_PUBLISH = ('README.md', 'REGISTRY.md')


def _token_logged():
    """### the token's string in any bank of this act, any tool of this act, or this session's transcript: the files where it is found."""
    t = _tok()
    if not t:
        return ['### THE TOKEN IS NOT SET -- NOT CHECKED']
    tb = t.encode('utf-8')
    hits = [f for f in os.listdir(D) if f.startswith('b639_') and tb in open(os.path.join(D, f), 'rb').read()]
    hits += [f for f in os.listdir(os.path.join(ROOT, 'tools')) if f.startswith('b639_') and tb in open(os.path.join(ROOT, 'tools', f), 'rb').read()]
    if os.path.exists(SESSION) and tb in open(SESSION, 'rb').read():
        hits.append('the session transcript')
    return hits


def n5(trail_line=None, ot=None, *a):
    """### (R249)'s N5, the file-set by PATH; nothing published before the word; the token not printed or logged; no kernel source touched; no
    ### sealed tool's hash differs; no identifier of the author in any outbound request beyond the record's own metadata."""
    if isinstance(trail_line, str):
        trail_line = int(trail_line.split('=')[-1])
    ot_text = ot if ot is not None else io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD():
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD() not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d (the trails end at :%d)' % (trail_line, len(ot_lines))
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b639_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    word = _word()
    pp_allowed = N5_PP if word == 'publish' else tuple(x for x in N5_PP if x not in N5_PP_ON_PUBLISH)
    pp_beyond = [x for x in pp_ch if x not in pp_allowed]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b639_|audit_b639_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    Z = _zres()
    pub = Z.get('publish') or {}
    read_at = (Z.get('read') or {}).get('at')
    word_ok = (not pub) or (word == 'publish' and bool(read_at) and pub.get('at', '') >= read_at)
    logged = _token_logged()
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local and not differ and word_ok and not logged
    return ('HELD' if ok else 'REFUTED',
            'nothing published before the author`s word %s (the word %s; published %s); the token in no bank, tool or transcript %s; every '
            'kernel`s tracked tree unmoved against the face %s; PLACE-papers %s (beyond the ledgers, %sthe pages: %s); %s; relay beyond the list, '
            'matched by path: %s; the sealed tools` hashes not agreeing %s; b628`s local intake bank in any relay commit %s, untracked now %s; '
            'no identifier of the author in any outbound request beyond the record`s own metadata (the route`s User-Agent names the act alone)' % (
                word_ok, word, bool(pub), logged or 'NONE', kern_ok, pp_ch, 'README and REGISTRY on publish, ' if word == 'publish' else '',
                pp_beyond or 'NONE', rec_state, beyond or 'NONE', differ or 'NONE', tracked_local, untracked_local))


def _vac(ok, n, word):
    return ('%s, VACUOUSLY' % word) if (ok and n == 0) else word


def scores(*a):
    Z, PS, MI, TF, RA, ST = (jl(n_) for n_ in (ZRES, 'b639_premise_status.json', 'b639_mirror.json', 'b639_table_final.json', 'b639_root_arm.json',
                                               'b639_tests_stepzero.json'))
    rd_ = Z.get('read') or {}
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    word = _word()
    dr = Z.get('doi_read') or {}
    _r, _n, sh = seal_hashes()
    bld = g(RELAY, 'diff', '--name-only', PRE_RELAY, '--', K.BUILDER).strip() + g(RELAY, 'diff', '--name-only', '--', K.BUILDER).strip()
    ro = g(RELAY, 'show', '--name-only', '--format=', K.ROSTER_COMMIT).split()
    clean_tests = [n for n, x in ST.items() if x.get('rc') == 0 and not x.get('failing')]
    S = {
        'H73a': (('HOLDS' if rd_.get('h73a') else 'REFUTED') if rd_ else 'PENDING', 'every file in the draft read back with the bank`s sha256: %s of %s agree; '
                 'missing %s; extra %s' % (sum(1 for r in rd_.get('files') or [] if r['ok']), len(rd_.get('files') or []), rd_.get('missing'), rd_.get('extra'))),
        'H73b': (('HOLDS' if rd_.get('h73b') else 'REFUTED') if rd_ else 'PENDING', 'the description read back byte for byte equal to the bank %s' % rd_.get('h73b')),
        'H73c': (('HOLDS' if rd_.get('h73c') else 'REFUTED') if rd_ else 'PENDING', 'the no-disclosure arm at 0 on the description and the file list %s' % rd_.get('h73c')),
        'H73d': (('HOLDS' if dr.get('h73d') else 'REFUTED') if dr else ('HOLDS, VACUOUSLY -- HELD, NOTHING PUBLISHED' if word == 'hold' else 'PENDING'),
                 'the DOI at its registry: titles %s, version %s' % (dr.get('titles'), dr.get('version'))),
        'H73e': (PS.get('h73e', 'PENDING'), 'the 50 heads each one status from the kernels: %s ; rule rows %s' % (PS.get('counts'), PS.get('rule_rows'))),
        'N5': n5v,
        'S1': (('HELD' if ro == [K.ROSTER] and MI.get('census6') and MI.get('clean') else 'REFUTED'),
               'the roster edit committed alone %s (%s); the mirror carrying the census at v0.6 %s, verified clean %s' % (ro == [K.ROSTER], ro, MI.get('census6'), MI.get('clean'))),
        'S2': (('HELD' if len(clean_tests) == len(ST) and ST else 'REFUTED'), 'every test file clean at step zero: %d of %d' % (len(clean_tests), len(ST))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) and not bld else 'REFUTED'),
               'the sealed tools` hashes at the record: %s; the builder unedited %s' % (dict(collections.Counter(v for _t, v in sh)), not bld)),
    }
    S['N1'] = (('HELD' if S['H73a'][0] == 'HOLDS' and S['H73e'][0] == 'HOLDS' else 'REFUTED'), 'as H73a and H73e')
    S['N2'] = (('HELD' if S['H73b'][0] == 'HOLDS' else 'REFUTED'), 'as H73b')
    S['N3'] = (('HELD' if S['H73c'][0] == 'HOLDS' else 'REFUTED'), 'as H73c')
    S['N4'] = (('HELD' if dr.get('h73d') else 'REFUTED') if dr else ('HELD, VACUOUSLY -- NOTHING PUBLISHED' if word == 'hold' else 'PENDING'), 'as H73d')
    put_json('b639_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 5: THE RECORD
def TRAIL_HEAD():
    return ('### b639 — lane three, act sixty-six under (R249): the deposit on the (R110) route, the 50 premise heads classed by status, the '
            'description in the reader’s order, the files with their digests, a draft read back from the service, the author’s word; the roster '
            'at census v0.6 and the mirror rebuilt')


def _title_entry():
    Z = _zres()
    pub, rd_ = Z.get('publish') or {}, Z.get('read') or {}
    if pub.get('doi'):
        return ('## The deposit on the (R110) route: version %s, DOI %s, %d files with digests read back, the description from the bank; the census at '
                'v0.6 and the root chain through b638 in the description, b639’s root at its record' % (pub.get('version'), pub.get('doi'), rd_.get('n_files', 0)))
    return '## The deposit draft at %s, %d files, held on the author’s word' % (rd_.get('id'), rd_.get('n_files', 0))


def _finding_text():
    S, rl, J = jl('b639_scores.json'), jl('b639_record_lines.json'), jl('b639_act_root.json')
    Z, PS, MI, FL, DS = _zres(), jl('b639_premise_status.json'), jl('b639_mirror.json'), jl('b639_deposit_files.json'), jl('b639_description_scan.json')
    rd_, pub, dr = Z.get('read') or {}, Z.get('publish') or {}, Z.get('doi_read') or {}
    c, r = PS.get('counts') or {}, PS.get('rule_rows') or {}
    n_ans = len(re.findall(r'^### PROMPT ', rd('b639_author_answers.txt'), re.M))
    t = _title_entry()
    fl = FL.get('files') or []
    lines = rl.get('lines') or []
    e = ['', t, '',
         '*Filed at b639 on the author’s ruling `(R249)` and the author’s answers (%d). Banks: relay `data/b639_premise_status.txt`, '
         '`data/b639_deposit_items.txt`, `data/b639_deposit_files.txt`, `data/b639_deposit_description.txt`, `data/b639_zenodo_read.txt`, '
         '`data/b639_mirror.txt`, `data/b639_act_root.txt`.*' % n_ans, '',
         '**The premise heads by status** (`(R249)`(2), Component 0): the census’s 50 heads classed from the kernels, each by the first status it '
         'meets in the ruling’s order as the author’s answers read it -- %d discharged in kernel, %d elsewhere, %d cited, %d open; their rule rows '
         '%d / %d / %d / %d. A salt-check witness discharges nothing; a conditional lemma or an iff discharges nothing; a bundle is cited only '
         'when every field is. The seat’s hand-read beside each discharge and each work-order line. H73e %s.' % (
             c.get('DISCHARGED IN KERNEL', 0), c.get('DISCHARGED ELSEWHERE', 0), c.get('CITED', 0), c.get('OPEN', 0), r.get('DISCHARGED IN KERNEL', 0),
             r.get('DISCHARGED ELSEWHERE', 0), r.get('CITED', 0), r.get('OPEN', 0), (S.get('H73e') or ['?'])[0]), '',
         '**The mirror** (Component 1, after the last push and before the draft): %s, md5 %s, %s files and MANIFEST, the census at v0.6 in it, '
         'verified %s.' % (os.path.basename(MI.get('zip') or ''), MI.get('zip_md5'), MI.get('files'), 'clean on all three clauses' if MI.get('clean') else 'NOT CLEAN'), '',
         '**The draft** (Component 2): a new version of record %s, version %s, the title kept; %d files -- %d replaced by their current editions, '
         '%d inherited byte-identical, %d added -- each with its sha256 in the bank; the description composed from the banks in the reader’s '
         'order, %s bytes, the scanner %s and every internal name defined; read back from the service as draft %s: H73a %s, H73b %s, H73c %s.' % (
             K.RECORD, K.VERSION, len(fl), sum(1 for x in fl if x['kind'].startswith('REPLACED')), sum(1 for x in fl if x['kind'].startswith('INHERITED')),
             sum(1 for x in fl if x['kind'].startswith('ADDED')), DS.get('bytes'), 'clean' if DS.get('clean') else 'NOT CLEAN', rd_.get('id'),
             (S.get('H73a') or ['?'])[0], (S.get('H73b') or ['?'])[0], (S.get('H73c') or ['?'])[0]), '',
         ('**The word and the publication** (Component 3): the author answered publish; record %s published, DOI %s, version %s; the DOI read at '
          'its registry, titles %s, version %s: H73d %s. README’s deposit note, REGISTRY’s deposit row and the glossary’s deposit entry take the '
          'new version and DOI in their own dated forms, each committed alone.' % (pub.get('record_id'), pub.get('doi'), pub.get('version'),
                                                                                    dr.get('titles'), dr.get('version'), (S.get('H73d') or ['?'])[0]))
         if pub.get('doi') else '**The word** (Component 3): the author answered hold; the draft %s left as the service leaves an unpublished draft, '
                                'nothing published. H73d %s.' % (rd_.get('id'), (S.get('H73d') or ['?'])[0]), '',
         '**The record lines** (`(R249)`(1)-(2)): b638 at its weight (FINDINGS :%s); the census method item, priced for v0.7 (OPEN_TRAILS :%s); '
         'W-ORD-DAY1-PATCH-VERSIONS, priced (:%s).' % tuple((lines + [{}, {}, {}])[i].get('line') for i in range(3)), '',
         '**The root.** b639 over %d repositories, %d tags and %d banks, the draft’s read-back among them; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it carries b635’s deposit preparations (FINDINGS :7771) and b638’s census (:7861) to the '
         'deposit, and reads the census’s premise table (:7861) by status, the census’s method item priced for its next edition. It strengthens the '
         'programme’s offering of a deposit a mathematician outside the programme can read in order -- what is claimed, what is machine-verified, '
         'what the kernels assume, what remains open.', '',
         '**Next.** Per `(R249)`(5): b640 on the author’s word, the census at v0.7 with the status column, or the per-cluster fact-item editions of '
         'Phase 1.2 under the reader’s clause; the author rules on the closing.', '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a status reads a kernel’s constructions and a docstring’s tiers.*', '']
    return t, NL.join(e)


FOR_AUTHOR = ('(1) the record the monograph’s, 21539167, as README’s deposit note and REGISTRY’s d1-1 row name it; (2) the mechanism exclusions '
              'read as SIDE-kernel v1.5’s route terminals README :15 names, with README :16’s and the record’s limits beside; (3) the monograph '
              'uploaded under its edition’s own name, A_Place_to_Stand_v5_18.md, the companions and ERRATA under their v1.1.2 names; (4) the '
              'publication date the day of the draft’s metadata step (UTC); (5) the description in the record’s own HTML paragraph form, a '
              'paragraph per part; (6) the seat’s hand-read of the discharges and the work-order lines, printed beside the computed status; (7) '
              'the figure put to the author before the seal corrected by the tool’s comment-reading, 20 / 28 / 2 to 19 / 29 / 2, both printed')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b639_scores.json', 'b639_findings.json', 'b639_record_lines.json', 'b639_act_root.json'))
    Z = _zres()
    n_ans = len(re.findall(r'^### PROMPT ', rd('b639_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rd_, pub = Z.get('read') or {}, Z.get('publish') or {}
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R249) ratified.** (1) b638 at its weight. (2) The premise table’s status column ruled, the 50 heads classed by status, the census '
             'method item. (3) The roster and the mirror. (4) The deposit on the (R110) route, in two parts with the author’s word between them. (5) '
             'The act after: b640.', '',
             '**Entered:** FINDINGS.md:%s (b638’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the census method item), :%s '
             '(W-ORD-DAY1-PATCH-VERSIONS); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line')), '',
             '**The deposit:** record %s, draft %s, %s files read back%s.' % (
                 K.RECORD, rd_.get('id'), rd_.get('n_files'), (', published as %s, DOI %s' % (pub.get('version'), pub.get('doi'))) if pub.get('doi')
                 else ', held on the author’s word, nothing published'), '',
             '**Act root:** b639 `%s` (previous `%s`, b638’s; relay data/act_roots.txt).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b639_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): b640 names no kernel terminal; the census at v0.7 reads the status bank’s kernels at their pins.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b639_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**The mirror:** built after the act’s last PLACE-papers push and before the draft, by the unedited builder on the %d-file roster; its '
             'digests in relay data/b639_mirror.txt.' % K.ROSTER_FILES, '',
             '**Next:** per `(R249)`(5), b640 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b639_scores.json')
    L = ['=' * 104, 'b639 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H73a-H73e, (R249)(4) and (2).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0].startswith('HOLDS') for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0].startswith('HELD') for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0].startswith('HELD') for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b639_defects.txt').rstrip(NL).split(NL)
    put_txt('b639_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J, Z = (jl(n_) for n_ in ('b639_scores.json', 'b639_findings.json', 'b639_trail.json', 'b639_record_lines.json', 'b639_act_root.json', ZRES))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    rd_, pub = Z.get('read') or {}, Z.get('publish') or {}
    L = ['b639 -- THE COMPONENTS, BANKED UNDER (R249).', '',
         '### COMPONENT 0 : the process listing ; b638`s closing push-out relay %s ; push-b638* deleted by name (data/b639_branches.txt) ; the roster '
         'relay %s ; the premise heads by status (data/b639_premise_status.txt), H73e %s ; every test file run (data/b639_tests_stepzero.txt) ; the '
         'suite at HEAD before the face (data/b639_arms_prerun.txt) ; the sealed tools` hashes at the seal ; b628`s local intake bank untracked' % (
             STEPZERO, K.ROSTER_COMMIT, S['H73e'][0]),
         '### COMPONENT 1 : b638`s weight FINDINGS :%s ; the census method item OPEN_TRAILS :%s ; W-ORD-DAY1-PATCH-VERSIONS :%s ; the mirror '
         '(data/b639_mirror.txt)' % (ls[0].get('line'), ls[1].get('line'), ls[2].get('line')),
         '### COMPONENT 2 : the deposit bank (data/b639_deposit_items.txt) ; the files (data/b639_deposit_files.txt) ; the description '
         '(data/b639_deposit_description.txt, data/b639_description_scan.txt) ; the draft %s (data/b639_zenodo_*.txt) ; H73a %s ; H73b %s ; H73c %s' % (
             rd_.get('id'), S['H73a'][0], S['H73b'][0], S['H73c'][0]),
         '### COMPONENT 3 : the word %s ; %s ; H73d %s' % (_word(), ('published %s, DOI %s' % (pub.get('version'), pub.get('doi'))) if pub.get('doi')
                                                         else 'nothing published', S['H73d'][0]),
         '### COMPONENT 4 : the pages (data/b639_page_*.json) ; page arms data/b639_page_arms.txt ; the root %s' % ((J.get('root') or '')[:16]),
         '### COMPONENT 5 : FINDINGS :%s (the entry) ; OPEN_TRAILS :%s (the record) ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b639_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  table cells the entry would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b639_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
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
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b639_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b639_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-07 by b639 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b639_defects.json -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD())
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
    put_json('b639_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


# ================================================================================ THE DISPATCHER
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'seal_hashes', 'answer_of', 'n5', 'put_txt', 'put_json', 'strip_comments',
                                                          'conclusion', 'head_tok', 'hyp_binders', 'decls_concluding', 'inline_of', 'declaration_of',
                                                          'http', 'h73', 'desc_scan'):
        print('usage: b639_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
