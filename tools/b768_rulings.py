# -*- coding: utf-8 -*-
"""tools/b768_rulings.py -- b768, (R378)(7): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b767_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R378)(7) and (12) write neither REGISTRY, ERRATA, the
census, the register nor the two files of the map, so OPEN_TRAILS is the one file here.

  ledgers c2 dry|write   Component 2 (data/b768_ferry.txt :97: "THE LINES OF (7), [R2] and [A3]"; :41: "[A3] is entered, one line for
                         (a), (c), (d) and (e), and [R2] for (b)"), appended at OPEN_TRAILS' end, no line moving, <DATE> the UTC date of the
                         write: one dated head and under it, each a paragraph of its own, in the order of the ruling's texts --
                         [R2] (data/b768_ferry.txt :78), as written: W-ORD-NOVEMBER-RIDERS stands in OPEN_TRAILS from b767's [R1] with
                           its entry line in the form tools/standing/orderstate.py :26 reads, and (7)(b) gives it passages with its trigger
                           standing, so no entry line is composed and the order's status is not moved;
                         [A3] (data/b768_ferry.txt :82), as written; it names no order.
                         Neither text carries a field. Controls before the write, printed, among them a planted status word read by the
                         rule (a check that can fire); the roster by tools/standing/orders.py's rule in memory, before and after: no order
                         added and none moving. Bank: data/b768_ledgers_c2.txt and .json, each text by line and sha256; the texts' words
                         printed by the dry run alone.
  ledgers c5 dry|write   Component 3's end, (R378)(4), appended at OPEN_TRAILS' end, no line moving, under one dated head --
                         [P1] (data/b768_ferry.txt :62), where the closing theorem compiles: <commit> the act's last Lean commit at which
                           a restored build read exit 0 by tools/b768_controls.py verdicts() over data/b768_dispatch_rows.json; <name>
                           SIDEExplicitFormula.Window.controlFailureExists, COMPILED in that read; <the print> its axioms print from the
                           read; the plan's four steps (L9c, L11c, L11d, L12) each COMPILED there; every theorem of
                           `SIDEExplicitFormula.Window` in print_targets.txt at the commit found once by its declaration line (its
                           namespaces read from `namespace`, `section` and `end`), read at its statement (from its name to its first `:=`)
                           and graded by tools/e0_rule.py grade(head, 'theorem'), its lexicon extended in this tool by the three types
                           b767 and this act declare (E0_EXTENSION, the shared file not edited), its axioms print from the read; each run
                           of eight digits or more in a printed gate row masked by its length.
                         Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory: W-ORD-LI-ARITH and
                         W-ORD-WINDOW-CERTIFY moving from OPEN to CLOSED, no other moving, none added. Bank: data/b768_ledgers_c5.txt
                         and .json.
[P2], where the closing theorem does not compile, and [C7] or [C8], where the closing build's read gives them, are groups this tool
gains by an Edit committed before its run.

No PLACE-papers line is printed but the texts this tool composes; the account is counted, never printed; no git write.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b768_worklist as K   # noqa: E402

ACT, NL = 'b768', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b768_ferry.txt')
FERRY_SHA = 'f4cc3c93a7a435fd'   # ### data/b768_stepzero.txt :19: the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C1PP = '9c43f4bb'                # ### PLACE-papers' one commit of the act before this write: the corrigendum (step 6, data/b768_events.txt (41))
WANT = dict(P1=(62, 62), P2=(66, 66), C7=(70, 70), C8=(74, 74), R2=(78, 78), A3=(82, 82))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
RIDERS = 'W-ORD-NOVEMBER-RIDERS'
GROUPS = dict(c2=('R2', 'A3'), c5=('P1',))
PLANT_FROM, PLANT_TO = '` GAINS PASSAGES', '` DISCHARGED, GAINS PASSAGES'   # ### the planted status word, read in memory alone


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def today():
    return time.strftime('%Y-%m-%d', time.gmtime())


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def fsha(p):
    try:
        with open(p, 'rb') as f:
            return sha(f.read())[:16]
    except OSError:
        return 'ABSENT'


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def ids():
    import b768_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address())


def account():
    """the account read from the relay's remote at run time (as tools/project_set.py reads it); counted in the texts, never printed."""
    import project_set as PS
    return PS.owner()


def idcount(text, I, acct):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'), account=low.count(acct.lower()) if acct else -1)


def at_head(path):
    b = git(PP, 'show', 'HEAD:' + path, raw=True)
    with open(os.path.join(PP, *path.split('/')), 'rb') as f:
        w = f.read()
    if not b or b != w:
        die('%s: ITS WORKING FILE IS NOT ITS BYTES AT HEAD (%d, %d bytes)' % (path, len(b), len(w)))
    if b'\r' in b or not b.endswith(b'\n'):
        die('%s: CARRIAGE RETURNS OR NO FINAL LINE END' % path)
    return b.decode('utf-8')


# ================================================================================ THE TEXTS
def ferry():
    with open(FERRY, 'rb') as f:
        b = f.read()
    if sha(b)[:16] != FERRY_SHA:
        die('THE FERRY BANK IS NOT ITS STEP-ZERO BYTES (sha256 %s)' % sha(b)[:16])
    return b.decode('utf-8').split(NL)


def texts(L):
    """{key: (first line, last line, text)} for each piece between '---- [K] ...' and '---- end [K]'; the lines checked against WANT."""
    out = {}
    for i, l in enumerate(L):
        m = re.match(r'^---- \[([A-Z]\d*)\] ', l)
        if m:
            k = m.group(1)
            j = L.index('---- end [%s]' % k, i)
            out[k] = (i + 2, j, NL.join(L[i + 1:j]))
    got = dict((k, (a, b)) for k, (a, b, _t) in out.items())
    if got != WANT:
        die('THE RULING`S TEXTS NOT AT THEIR LINES: %s' % sorted(set(got.items()) ^ set(WANT.items())))
    return out


def pattern(tpl):
    pat = re.escape(tpl)
    for ph in sorted(set(FIELD.findall(tpl)), key=len, reverse=True):
        pat = pat.replace(re.escape(ph), '(.+?)')
    return pat


# ================================================================================ THE LEDGER
def compose(group, date, base):
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    keys = GROUPS[group]
    E = dict((k, TP[k]) for k in keys)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b768, `(R378)`(7): the lines the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b768_ferry.txt :41, :77-:79 and :81-:83), appended at the end of the file (its last line :%d), so that no line before '
            'them moves: the passages the order of the November riders gains, in two parts, by [R2]; the author’s rulings of 2026-11-23 '
            'and 2026-11-24 by [A3]. The lines of the proof and of the closing build from source are appended beneath them at Component 3 '
            'and after.' % (date, n_ot))
    paras = [head] + [E[k] for k in keys]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, text=ot, new=base + NL + ot + NL, head=head, keys=keys, n_ot=n_ot, paras=paras)


def ledgers(group, mode):
    from standing import orders as O
    from standing import orderstate as OS
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(group, date, base)
    E, new, TP, text = C['E'], C['new'], C['TP'], C['text']
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    fields_in = sorted(k for k in C['keys'] if FIELD.findall(TP[k]))
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base.split(NL), new.split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    riders_entry = [i + 1 for i, l in enumerate(bl) if (OS.ENTRYFORM.match(l) or [None, None])[1] == RIDERS]
    r2_status = O._status(O.mask(E['R2']), RIDERS)
    a3_names = sorted(set(O.NAME.findall(E['A3'])))
    planted = E['R2'].replace(PLANT_FROM, PLANT_TO, 1)
    p_status = O._status(O.mask(planted), RIDERS) if planted != E['R2'] else None
    p_after = dict(O.read(bl + [planted]))
    ctl = [('PLACE-papers` HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]),
            pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in C['keys'] if k in eq)), len(eq) == len(C['keys']) and all(eq.values())),
           ('neither text carries a field in the ruling (with fields %s), and no field is left in the appended text (%s)' % (
               fields_in or 'none', left or 'none'), not fields_in and not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[R2]`s order %s in OPEN_TRAILS before the write, OPEN by the rule, its entry line in the form tools/standing/orderstate.py :26 reads '
            'at %s' % (RIDERS, ['%d' % x for x in riders_entry] or 'none'),
            RIDERS in before and st(before, RIDERS) == 'OPEN' and len(riders_entry) == 1),
           ('[R2] gives %s no status word by the rule (%s): its trigger stands and the order stays OPEN; [A3] names no order (%s)' % (
               RIDERS, r2_status or 'none', a3_names or 'none'), r2_status is None and not a3_names),
           ('PLANTED: [R2] with a status word set after the order`s name, read in memory alone, reads a status (%s) and moves the order to %s' % (
               p_status, st(p_after, RIDERS)), bool(p_status) and p_status[0] == 'CLOSED' and st(p_after, RIDERS) == 'CLOSED'),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R378)(7), GROUP %s: [R2] AND [A3], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
         '### tools/b768_rulings.py ledgers %s; PLACE-papers HEAD %s; the texts from the ferry bank (data/b768_ferry.txt, sha256 %s); <DATE> %s;'
         % (group, pp_head[:8], FERRY_SHA, date),
         '### each text by line and sha256 here; no PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), added or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', C['head'])] + [(k, E[k]) for k in C['keys']]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([R2], [A3]) ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (group.upper(), len(C['paras']) - 1, sum(1 for _w, o in ctl if o), len(ctl),
                                 ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b768_ledgers_%s.txt' % group), os.path.join(D, 'b768_ledgers_%s.json' % group)
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1, first_new=first, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()),
                            head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]], keys=list(C['keys']),
                            roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


# ================================================================================ GROUP c5: [P1]
C2PP = 'eea70a2d'                # ### PLACE-papers' last commit of the act before the c5 write: the lines of (7) (step 22, data/b768_events.txt (54))
EF, EFK = K.EF_DIR, 'SIDE-explicit-formula'
NS = 'SIDEExplicitFormula.Window.'
WIN_DIR = 'SIDEExplicitFormula/Window/'
STD3 = '[propext, Classical.choice, Quot.sound]'
AX3 = {'propext', 'Classical.choice', 'Quot.sound'}
DROWS = os.path.join(D, 'b768_dispatch_rows.json')
STEP_ITEMS = ('a', 'b', 'c', 'd', 'e')
CLOSING = 'controlFailureExists'   # ### (R378)(4)(e): the proof of ControlFailureExists (SIDEExplicitFormula/ControlFailureExists.lean :23)
STEPS = (('L9c', 'archJ_comb'), ('L11c', 'arith_eq_comb'), ('L11d', 'window_arith_neg'), ('L12', 'controlFailureExists'))   # ### (4)(b)-(e)
LI, WC = 'W-ORD-LI-ARITH', 'W-ORD-WINDOW-CERTIFY'   # ### [P1]'s two orders, each DISCHARGED by its text
DECL_RE = re.compile(r'^(?:@\[[^\]\n]*\]\s*)?(?:(?:protected|private|nonrec)\s+)*(?:theorem|lemma)\s+([^\s(\[{:]+)')
NS_RE, SEC_RE, END_RE = re.compile(r'^namespace\s+(\S+)\s*$'), re.compile(r'^section(?:\s+\S+)?\s*$'), re.compile(r'^end(?:\s+\S+)?\s*$')
DIGITS = re.compile(r'\d{8,}')
# ### the E0 rule's lexicon extended in this tool, the shared tools/e0_rule.py not edited (tools/b767_rulings.py :397-:402's form): the
# ### two types b767 declared and the one this act declares, each data, each read at its declaration line at the commit
E0_EXTENSION = {'LPEntry': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Window/LogBounds.lean :16 (structure, b767)'),
                'LPTree': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Window/LogBounds.lean :24 (inductive, b767)'),
                'AWin': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Window/ArithFrame.lean :30 (structure, b768)')}
E0_EXT_DECL = {'LPEntry': ('SIDEExplicitFormula/Window/LogBounds.lean', 16, 'structure LPEntry where'),
               'LPTree': ('SIDEExplicitFormula/Window/LogBounds.lean', 24, 'inductive LPTree where'),
               'AWin': ('SIDEExplicitFormula/Window/ArithFrame.lean', 30, 'structure AWin where')}
_EXT = {}


def masked(s):
    """each run of eight digits or more replaced by its length, so that no chunk's value or datum enters a printed row."""
    return DIGITS.sub(lambda m: '#%d-digits' % len(m.group(0)), str(s))


def fill(tpl, values):
    t = tpl
    for ph, v in values:
        if ph not in t:
            die('THE FIELD %r NOT IN ITS TEMPLATE' % ph)
        t = t.replace(ph, v, 1)
    return t


def e0_extend():
    """the extension laid over the shared lexicon once; returns the keys the shared lexicon held before it (wanted none)."""
    import e0_rule as E0
    if 'held' not in _EXT:
        _EXT['held'] = sorted(k for k in E0_EXTENSION if k in E0.LEXICON)
        E0.LEXICON.update(E0_EXTENSION)
    return _EXT['held']


def drows():
    with open(DROWS, encoding='utf-8') as f:
        return json.load(f)


def ax_within(ax):
    s = str(ax or '').strip()
    if not (s.startswith('[') and s.endswith(']')):
        return False
    return set(x.strip() for x in s[1:-1].split(',') if x.strip()) <= AX3


def gate_ok(gates):
    return bool(gates) and all(g['line'] and g['grade'] not in ('NOT READ', 'UNCLASSED') for g in gates)


def decls(src):
    """{full name: [line, ...]} for each theorem or lemma of a Lean source, its namespaces read from `namespace`, `section` and `end`."""
    stack, out = [], {}
    for i, l in enumerate(src.split(NL)):
        m = NS_RE.match(l)
        if m:
            stack.append(m.group(1))
            continue
        if SEC_RE.match(l):
            stack.append(None)
            continue
        if END_RE.match(l):
            if stack:
                stack.pop()
            continue
        m = DECL_RE.match(l)
        if m:
            out.setdefault('.'.join([s for s in stack if s] + [m.group(1)]), []).append(i + 1)
    return out


def e0_at(src, line):
    """the theorem's statement at its declaration line, from its name to its first `:=`, graded by tools/e0_rule.py."""
    import e0_rule as E0
    e0_extend()
    L = src.split(NL)
    m = DECL_RE.match(L[line - 1])
    start = sum(len(x) + 1 for x in L[:line - 1]) + m.end()
    end = src.find(':=', start)
    head = src[start:end] if end > 0 else ''
    try:
        g, why, _b = E0.grade(head, 'theorem')
    except Exception as ex:   # noqa: BLE001
        g, why = 'UNCLASSED', ' '.join(str(ex).split())[:300]
    return dict(line=line, grade=g, why=' '.join(str(why).split()))


def p1_fields(R):
    import b768_controls as C
    V = C.verdicts(R)
    lk = V['last_kernel']
    if not lk:
        return dict(miss='[P1]: no restored read exiting 0 in data/b768_dispatch_rows.json')
    commit = str(lk.get('built_ref'))[:8]
    st = dict((x[0], (x[1], x[2])) for x in (lk.get('names') or []))
    built = str(lk.get('build_exit')) == '0' and lk.get('verdict') == 'KERNEL' and bool(lk.get('built_equal'))
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('kernel') == EFK]
    dn = [r.get('n') for r in disp if int(r['run']) == int(lk['run'])]
    later = [r.get('n') for r in disp if dn and r.get('n', 0) > dn[0] and r.get('item') in STEP_ITEMS]
    closing = [r for r in disp if r.get('item') == 'closing']
    pt = [x.strip() for x in git(EF, 'show', '%s:print_targets.txt' % commit).split(NL) if x.strip().startswith(NS)]
    files = [p.strip() for p in git(EF, 'ls-tree', '--name-only', commit, WIN_DIR).split(NL) if p.strip().endswith('.lean')]
    where, srcs = {}, {}
    for p in files:
        srcs[p] = git(EF, 'show', '%s:%s' % (commit, p)).replace('\r', '')
        for full, lines in decls(srcs[p]).items():
            for ln in lines:
                where.setdefault(full, []).append((p, ln))
    gates = []
    for full in pt:
        loc = where.get(full, [])
        e = e0_at(srcs[loc[0][0]], loc[0][1]) if len(loc) == 1 else {}
        state, ax = st.get(full, (None, None))
        gates.append(dict(name=full, path=loc[0][0] if len(loc) == 1 else ('NOT FOUND' if not loc else 'IN %d PLACES' % len(loc)),
                          line=e.get('line'), grade=e.get('grade', 'NOT READ'), why=e.get('why', ''), state=state, axioms=ax, built=built))
    ext = [(k, p, ln, p in srcs and len(srcs[p].split(NL)) >= ln and srcs[p].split(NL)[ln - 1] == want)
           for k, (p, ln, want) in sorted(E0_EXT_DECL.items())]
    steps = [(lab, nm, st.get(NS + nm, (None, None))) for lab, nm in STEPS]
    cl_state, cl_ax = st.get(NS + CLOSING, (None, None))
    fields = [('<name>', '`%s%s`' % (NS, CLOSING)), ('<commit>', commit), ('<the print>', str(cl_ax))]
    return dict(fields=fields, gates=gates, read_names=sorted(n for n in st if n.startswith(NS)), lk=lk, built=built, later=later,
                closing=closing, files=len(files), commit=commit, steps=steps, cl=(cl_state, cl_ax), ext=ext, held=e0_extend(),
                dn=dn[0] if dn else None)


def ledgers_c5(mode):
    from standing import orders as O
    group, date = 'c5', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    TP = dict((k, v[2]) for k, v in texts(ferry()).items())
    R = drows()
    p1 = p1_fields(R)
    E, miss = {}, []
    if p1.get('miss'):
        miss.append(p1['miss'])
        p1 = dict(gates=[], read_names=[], lk={}, built=False, later=[], closing=[], files=0, commit=None, steps=[], cl=(None, None),
                  ext=[], held=['NOT READ'], dn=None)
    else:
        E['P1'] = fill(TP['P1'], p1['fields'])
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b768, `(R378)`(4): the line the ruling orders for OPEN_TRAILS where the closing theorem compiles** (relay '
            'data/b768_ferry.txt :61-:63), appended at the end of the file (its last line :%d), so that no line before it moves: each '
            'compiled theorem of the Lean of this act read at its statement by the E0 gate (relay tools/e0_rule.py) before it is entered, '
            'its name in print_targets.txt at its commit and its axioms print banked (relay data/b768_dispatch_rows.json and '
            'data/b768_ledgers_c5.txt). Where the closing build from source and the restored build print different axioms files, [C7] is '
            'appended beneath it; where the closing build and its repeat each stop under the hold, [C8].' % (date, n_ot))
    paras = [head] + [E[k] for k in GROUPS[group] if k in E]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    before, after = dict(O.read(base.split(NL))), dict(O.read(new.split(NL)))
    moved = sorted((n, st(before, n), st(after, n)) for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    gates = p1['gates']
    grades, axs = {}, {}
    for g in gates:
        grades[g['grade']] = grades.get(g['grade'], 0) + 1
        axs[str(g['axioms'])] = axs.get(str(g['axioms']), 0) + 1
    pop = sorted(g['name'] for g in gates)
    plant_gate = gate_ok([dict(gates[0], line=None, grade='NOT READ')] + gates[1:]) if gates else True
    plant_pop = (pop + [NS + 'b999_planted']) == p1['read_names']
    lk = p1['lk'] or {}
    cl_state, cl_ax = p1['cl']
    want_moved = [(LI, 'OPEN', 'CLOSED'), (WC, 'OPEN', 'CLOSED')]
    ctl = [('PLACE-papers` HEAD the act`s last commit there before this write, the lines of (7) %s (%s)' % (C2PP, pp_head[:8]),
            pp_head.startswith(C2PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in GROUPS[group] if k in eq)), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('[P1]: THE RUN: dispatch %s read, built at %s equal with exit 0, KERNEL (run %s)' % (p1['dn'], p1['commit'], lk.get('run')),
            p1['built']),
           ('[P1]: <commit> the act`s last restored read exiting 0 by verdicts(): dispatch %s at %s; no step dispatched after it (%s); the '
            'closing build rows %d' % (p1['dn'], p1['commit'], p1['later'] or 'none', len(p1['closing'])), bool(p1['commit']) and not p1['later']),
           ('[P1]: <name> %s%s COMPILED in the read (%s), <the print> its axioms %s within %s' % (NS, CLOSING, cl_state, cl_ax, STD3),
            cl_state == 'COMPILED' and ax_within(cl_ax)),
           ('[P1]: the plan`s four steps each COMPILED in the read (%s)' % (
               ' '.join('%s %s %s' % (lab, nm, s[0]) for lab, nm, s in p1['steps']) or 'none'),
            len(p1['steps']) == len(STEPS) and all(s[0] == 'COMPILED' and ax_within(s[1]) for _l, _n, s in p1['steps'])),
           ('[P1]: THE POPULATION: the names of %s in print_targets.txt at %s (%d) equal both ways to those the read names (%d)' % (
               NS, p1['commit'], len(pop), len(p1['read_names'])), bool(pop) and pop == p1['read_names']),
           ('[P1]: THE E0 RULE`S LEXICON extended in this tool, tools/e0_rule.py not edited: %s each data, each read at its declaration line at the '
            'commit (%s), none held by the shared lexicon before (held: %s)' % (
                ', '.join(sorted(E0_EXTENSION)), ' '.join('%s :%d %s' % (k, ln, ok_) for k, _p, ln, ok_ in p1['ext']) or 'none', p1['held'] or 'none'),
            len(p1['ext']) == len(E0_EXTENSION) and all(x[3] for x in p1['ext']) and not p1['held']),
           ('[P1]: THE E0 GATE: each of the %d theorems found once by its declaration line among the %d Window files at the commit, read at its '
            'statement and graded (%s)' % (len(gates), p1['files'], ', '.join('%s %d' % kv for kv in sorted(grades.items()))), gate_ok(gates)),
           ('[P1]: each COMPILED in the read, its axioms within %s, sorryAx in none (the prints: %s)' % (
               STD3, '; '.join('%s %d' % kv for kv in sorted(axs.items()))),
            bool(gates) and all(g['state'] == 'COMPILED' and ax_within(g['axioms']) for g in gates)),
           ('PLANTED: a gate row with no statement read as the gate`s failure, and a planted name as the population`s (%s, %s)' % (
               'FAILED' if not plant_gate else 'PASSED', 'DIFFER' if not plant_pop else 'EQUAL'), not plant_gate and not plant_pop),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: %s and %s moving from OPEN to CLOSED by [P1]`s status words, no other moving, none added (moved %s ; added %s)' % (
               LI, WC, moved or 'none', added or 'none'), moved == want_moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R378)(4), GROUP C5: [P1], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b768_rulings.py ledgers c5; PLACE-papers HEAD %s; the texts from the ferry bank (data/b768_ferry.txt, sha256 %s), the fields from'
         % (pp_head[:8], FERRY_SHA),
         '### data/b768_dispatch_rows.json (sha256 %s) and SIDE-explicit-formula at %s; <DATE> %s; each text by line and sha256 here; no'
         % (fsha(DROWS), p1['commit'], date),
         '### PLACE-papers line printed but the texts composed; each run of eight digits or more in a gate row masked by its length.', '',
         '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE E0 GATE (tools/e0_rule.py grade(head, \'theorem\'), the head the statement from the name to its first `:=`, read at %s)'
          % p1['commit']]
    P += [masked('  %-60s %s :%s ; GRADE %s ; %s ; %s %s' % (g['name'], g['path'], g['line'], g['grade'], g['why'] or '-', g['state'], g['axioms']))
          for g in gates]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    nl_ = new.split(NL)
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in GROUPS[group] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C5: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINE UNDER ONE HEAD ([P1]) ; THE E0 GATE %d OF %d '
          'READ ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(paras) - 1, sum(1 for g in gates if g['line']), len(gates), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b768_ledgers_c5.txt'), os.path.join(D, 'b768_ledgers_c5.json')
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head,
                            file=dict(path=OT, lines_before=n_ot, lines_after=len(nl_) - 1, first_new=n_ot + 2, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()), head=[nl_.index(head) + 1, sha(head)[:16]],
                            keys=list(GROUPS[group]), run=lk.get('run'), commit=p1['commit'],
                            e0=[dict((x, masked(g[x]) if x == 'why' else g[x]) for x in ('name', 'path', 'line', 'grade', 'why', 'state', 'axioms'))
                                for g in gates],
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    if argv[1] == 'c5':
        return ledgers_c5(argv[2])
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
