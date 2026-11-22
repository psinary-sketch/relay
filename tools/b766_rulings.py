# -*- coding: utf-8 -*-
"""tools/b766_rulings.py -- b766, (R376)(4)(a) and (6): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b765_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). (R376)(11) writes neither REGISTRY, ERRATA, the census,
the register nor the two files of the map, so OPEN_TRAILS is the one file here.

  ledgers c2 dry|write   Component 2 (data/b766_ferry.txt :122, "THE LINES OF (6)"), appended at OPEN_TRAILS' end, no line moving, <DATE> the
                         UTC date of the write: one dated head and under it, each a paragraph of its own, in the ruling's order --
                         [E1] where the certificate's five controls read AS WANTED (data/b766_certificate.txt's foot), its fields from
                           data/b766_certificate.json and the budget's line of data/b766_certificate.txt; where they do not, the write is
                           refused, [E2]'s field being the seat's to write;
                         [M4], and with it the entry line of W-ORD-MAP-MERGE in the form tools/standing/orderstate.py :26 reads, its words
                           (R376)(6)(a)'s;
                         [Q2], one line an order for the eleven (R376)(6)(b) names (data/b766_ferry.txt :32), in its order, each from its row
                           of data/b765_premise_positions.txt (the row's number, its premise, its position A HYPOTHESIS BY DESIGN, no edge to
                           the Hypothesis, its consequence retirement) and the theorem that bank's retirement section names for it;
                         [H5]; [A1].
                         Controls before the write, printed; the roster by tools/standing/orders.py's rule in memory, before and after: the
                         eleven moving from OPEN to CLOSED, W-ORD-MAP-MERGE added OPEN, no other order moving. Bank: data/b766_ledgers_c2.txt
                         and .json, each text by line and sha256; the texts' words printed by the dry run alone.
  ledgers c3 dry|write   Component 3, (R376)(4)(b) and (4)(c) (data/b766_ferry.txt :58-:64), appended at OPEN_TRAILS' end as c2 is, under
                         one dated head: [F1] and [F2], their fields from the read of each one's dispatch (data/b766_dispatch_rows.json: the
                         run, the commit built, each name COMPILED with its axioms print) and from the kernel at the commit. (R376)(4) "Each
                         compiled theorem is read at its statement by the E0 gate before it is entered; its name joins print_targets.txt and
                         its axioms print is banked": each of the fourteen theorems is read at its commit (git show, the text from its name to
                         its first `:=`) and graded by tools/e0_rule.py grade(head, 'theorem'), an exception read UNCLASSED; the texts say
                         DERIVED, so the write is refused unless each grade is DERIVES; each name read in print_targets.txt at its commit.
                         Bank: data/b766_ledgers_c3.txt and .json, each grade by name, file and line.
  ledgers c4 dry|write   Component 3, (R376)(5) (data/b766_ferry.txt :82-:92), appended at OPEN_TRAILS' end as c2 and c3 are, under one
                         dated head: [X1], [X2] and [X3], each one's fields from its reading's bank, read where that bank's controls each
                         read AS WANTED and its PLACE-papers HEAD is the HEAD at the write: [X1] from data/b766_registry_cells.json's sentence
                         (its sixteen figures in the text's order), [X2] from data/b766_lean_join.json (the four counts, the three kernels
                         holding the most of the last, and the navigator's candidate read reproduced where the four counts at 29d4c9b7 equal
                         1,990, 152, 870 and 968, and differing as printed where they do not), [X3] from data/b766_sweep.json (its seven
                         figures); a figure of four digits or more printed with its thousands' commas. Bank: data/b766_ledgers_c4.txt and .json.
  ledgers c5 dry|write   Component 3, (R376)(4)(d) where the closing theorem does not compile at this act (data/b766_ferry.txt :74-:76),
                         appended at OPEN_TRAILS' end as c2 to c4 are, under one dated head: [P2], its fields from the read of the act's last
                         restored dispatch (data/b766_dispatch_rows.json: the run, the commit built with exit 0, each name COMPILED with its
                         axioms print) and from the kernel at that commit. Each compiled theorem is read at its statement by the E0 gate
                         before it is entered ((R376)(4)): every name of SIDEExplicitFormula.Window. in print_targets.txt at the commit, its
                         file found by its declaration line among the Window files there, graded by tools/e0_rule.py grade(head, 'theorem');
                         [P2] states no position, so a grade is printed and the write refused only where a statement is not found or not
                         graded; the population equal both ways to the names the dispatch's read counts; each COMPILED with its axioms
                         within the standard three; a planted gate row and a planted name read as the two checks' failures.
                         Bank: data/b766_ledgers_c5.txt and .json, each grade by name, file and line.
[C7], where Component 4's build from source and the restored build print different axioms files, is a group this tool gains, by an Edit
committed before its run, when that build's read stands.

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
import b766_worklist as K   # noqa: E402

ACT, NL = 'b766', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b766_ferry.txt')
FERRY_SHA = 'c5cac8a5077d0f8c'   # ### data/b766_stepzero.txt :22: the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C1PP = '7a36f281'                # ### PLACE-papers' one commit of the act before this write: the corrigendum (step 5, data/b766_events.txt (32))
WANT = dict(E1=(51, 51), E2=(55, 55), F1=(59, 59), F2=(63, 63), F3=(67, 67), P1=(71, 71), P2=(75, 75), C7=(79, 79), X1=(83, 83),
            X2=(87, 87), X3=(91, 91), M4=(95, 95), Q2=(99, 99), H5=(103, 103), A1=(107, 107))
Q2_LINE = 32                     # ### (R376)(6)(b): the eleven orders named
Q2_OPEN = 'Eleven orders are RETIRED, each a hypothesis by design of the theorem its row names, with no edge to the Hypothesis: '
Q2_SHUT = '. Standing as written'
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
NAME = re.compile(r'W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*')
MERGE = 'W-ORD-MAP-MERGE'
CERT_TXT, CERT_JSON = os.path.join(D, 'b766_certificate.txt'), os.path.join(D, 'b766_certificate.json')
CERT_FOOT = '### ### **THE CERTIFICATE BANKED, [E1]: 5 OF 5 CONTROLS AS WANTED ; THE EXACT FORM WRITTEN.**'
BUDGET_RE = re.compile(r'^  THE BUDGET: constants (\d+), each an equal share of \|S\| / 2: gamma (\d+) digits, log pi (\d+) digits, the log p from '
                       r'(\d+) to (\d+) digits ; SUM \|r\| 10\^-digits ([0-9.]+) < \|S\| / 2 ([0-9.]+): True ; one width for all, (\d+) digits$')
GROUPS = dict(c2=('E1', 'M4', 'Q2', 'H5', 'A1'), c3=('F1', 'F2'), c4=('X1', 'X2', 'X3'), c5=('P2',))
C3PP = '92108a44'                # ### PLACE-papers' last commit of the act before the c4 write: [F1] and [F2] (step 30, data/b766_events.txt (55))
X1_RE = re.compile(r'^(\d+) rows of (\d+) tables \(relay data/b766_registry_cells\.txt\); KEYSTONE (\d+), CLUSTER SYNTHESIS (\d+), APPARATUS (\d+), '
                   r'SOURCE NAMED (\d+), SOURCE NOT NAMED (\d+), WITHDRAWN OR SUPERSEDED (\d+), UNPLACED (\d+); the keystones by phase: the Day 1 '
                   r'cluster (\d+), Phase 1\.2 (\d+), Phase 1\.5 (\d+), method (\d+), Phase 2 (\d+); (\d+) rows filed under a table other than their '
                   r'phase by subject; (\d+) titles flagged$')
CANDIDATE = (1990, 152, 870, 968)   # ### (R376)(5)(b): the navigator's candidate at the relay's 29d4c9b7, printed as the navigator's
EF = K.EF_DIR
C2PP = 'a183880f'                # ### PLACE-papers' last commit of the act before the c3 write: the lines of (6) (step 20, data/b766_events.txt (44))
STD3 = '[propext, Classical.choice, Quot.sound]'
NS = 'SIDEExplicitFormula.Window.'
COEFFS, COEFFS_SHA = 'SIDEExplicitFormula/Window/Coeffs.lean', 'f06bd20ca2854d06'   # ### data/b766_window_data.txt: the data file as written
WINDOW_SHA = '4cbe7be1203883a6'  # ### data/b765_window.txt :26: the bank's sha256 less its final line end, which the data file's head names
C3 = dict(F1=dict(read=1, commit='48d151e3', items=(('SIDEExplicitFormula/Window/PrimeFinite.lean', ('primeTermQ_eq_finite_sum', 'primeTermQ_cQ_eq_finite_sum')),)),
          F2=dict(read=2, commit='d814154e', items=(('SIDEExplicitFormula/Window/Spline.lean', ('contDiff_tpow3', 'contDiff_cubicB', 'contDiff_splineH',
                                                                                                'splineH_eq_zero', 'contDiff_gWin', 'hasCompactSupport_gWin',
                                                                                                'windowKOf_classK', 'windowKOf_eq_zero')),
                                                    ('SIDEExplicitFormula/Window/Instance.lean', ('windowH_contDiff', 'windowH_eq_zero', 'windowK_classK',
                                                                                                  'windowK_eq_zero')))))
DECL = r'^(?:@\[[^\]\n]*\]\s*)?(?:(?:protected|private|nonrec)\s+)*theorem\s+%s(?=[\s(\[{:])'


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


def rdl(name):
    with open(os.path.join(D, name), encoding='utf-8') as f:
        return f.read().replace('\r', '').split(NL)


def ids():
    import b766_address_scan as SC
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


def fill(tpl, values):
    t = tpl
    for ph, v in values:
        if ph not in t:
            die('THE FIELD %r NOT IN ITS TEMPLATE' % ph)
        t = t.replace(ph, v, 1)
    return t


# ================================================================================ THE FIELDS, FROM THE BANKS
def cert_fields():
    """[E1]'s fields: the primes of the combination and the K values from the json, the budget's line from the reading; None where the
    reading's foot is not the five controls AS WANTED."""
    L = rdl('b766_certificate.txt')
    if CERT_FOOT not in L:
        return None, 'the certificate`s foot is not 5 of 5 controls AS WANTED'
    b = [BUDGET_RE.match(l) for l in L]
    b = [x for x in b if x]
    if len(b) != 1:
        return None, 'the budget`s line not read once (%d)' % len(b)
    with open(CERT_JSON, encoding='utf-8') as f:
        js = json.load(f)
    n_p, n_k = int(js['primes']), len(js['K'])
    N, g, lp, p0, p1, tot, half, uni = b[0].groups()
    dg = js['budget']['digits']
    pd = [v for k, v in dg.items() if k.startswith('log ') and k != 'log pi']
    agree = (int(N) == js['budget']['constants'] == len(dg) and int(g) == dg['gamma'] and int(lp) == dg['log pi'] and pd
             and int(p0) == min(pd) and int(p1) == max(pd) and int(uni) == js['budget']['uniform_digits'] and len(pd) == n_p)
    if not agree:
        return None, 'the budget`s line and the json`s budget differ'
    line = ('Euler\'s constant to %s digits, log pi to %s and the logarithm of each prime to between %s and %s, each of the %s constants '
            'an equal share of half of |S| (the sum of the |r| times the half-widths %s against %s), or one width of %s digits for all'
            % (g, lp, p0, p1, '{:,}'.format(int(N)), tot, half, uni))
    return dict(primes='{:,}'.format(n_p), k='{:,}'.format(n_k), budget=line, n_p=n_p, n_k=n_k, foot=True), None


def q2_rows(L):
    """the eleven of (R376)(6)(b) in its order, each (order, row number, premise, theorem, place) from data/b765_premise_positions.txt;
    a list of the faults beside."""
    s = L[Q2_LINE - 1]
    if Q2_OPEN not in s or Q2_SHUT not in s:
        die('(R376)(6)(b)`S ELEVEN NOT AT data/b766_ferry.txt :%d' % Q2_LINE)
    span = s[s.index(Q2_OPEN) + len(Q2_OPEN):s.index(Q2_SHUT)]
    names = NAME.findall(span)
    P = rdl('b765_premise_positions.txt')
    rows, thms, bad = {}, {}, []
    for l in P:
        m = re.match(r'^    \((\d+)\) (W-ORD-[A-Z0-9-]+) \| (.+)$', l)
        if m:
            cols = [c.strip() for c in (m.group(2) + ' | ' + m.group(3)).split(' | ')]
            rows[m.group(2)] = (m.group(1), cols)
        t = re.match(r'^    (W-ORD-[A-Z0-9-]+) \((.+?)\): A HYPOTHESIS BY DESIGN by (\S+) \((.+?)\)$', l)
        if t:
            thms[t.group(1)] = (t.group(2), t.group(3), t.group(4))
    out = []
    for n in names:
        if n not in rows or n not in thms:
            bad.append('%s: no row or no retirement line' % n)
            continue
        num, c = rows[n]
        ok = (len(c) == 9 and c[4] == 'A HYPOTHESIS BY DESIGN' and c[6] == 'no edge to the Hypothesis'
              and c[7].startswith('put to the author for retirement') and c[8] == 'hand-read AGREES'
              and thms[n][0] == c[1] and c[5].startswith(thms[n][1] + ' (' + thms[n][2] + ')'))
        if not ok:
            bad.append('%s: its row (%s) not as the retirement reads' % (n, num))
        out.append((n, num, c[1], thms[n][1], thms[n][2]))
    if len(names) != 11 or len(set(names)) != 11:
        bad.append('the ruling names %d orders, %d distinct' % (len(names), len(set(names))))
    return out, bad


def entry_line(date):
    return ('*Appended %s by b766, under the author’s ruling `(R376)`(6)(a) [M4] -- THE ORDER **`%s`**: the 81 lines that SPIRAL_MAP_v0_7.md '
            'alone holds (relay data/b765_map_pair.txt) merged into SPIRAL_MAP.md by a tool whose control reads each of the 93 differing lines '
            'present afterward; SPIRAL_MAP_v0_7.md then standing as an edition; the roster’s rule of the current edition (relay '
            'tools/standing/v1345.py :101-:106) and the check at relay tools/standing/v1340.py :556 taking the one name. Trigger: the act that '
            'writes the registry’s cells. Status: OPEN.*' % (date, MERGE))


# ================================================================================ THE LEDGER
def compose(group, date, base):
    L = ferry()
    X = texts(L)
    TP = dict((k, X[k][2]) for k in X)
    E, miss, extra = {}, [], {}
    keys = GROUPS[group]
    cf, cwhy = cert_fields()
    if cf:
        E['E1'] = fill(TP['E1'], [('<n>', cf['primes']), ('<n>', cf['k']), ('<the budget\'s line>', cf['budget'])])
    else:
        miss.append('[E1]: %s ([E2]`s field the seat`s)' % cwhy)
    E['M4'] = TP['M4']
    extra['M4_entry'] = entry_line(date)
    q2, qbad = q2_rows(L)
    E['Q2'] = [fill(TP['Q2'], [('<the order>', n), ('<name>', '`%s`' % pr), ('<the theorem its row names>', '`%s` (%s)' % (th, pl)), ('<n>', num)])
               for n, num, pr, th, pl in q2]
    if qbad:
        miss.append('[Q2]: %s' % '; '.join(qbad))
    E['H5'], E['A1'] = TP['H5'], TP['A1']
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b766, `(R376)`(4)(a) and (6): the lines the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b766_ferry.txt :50-:52 and :94-:108), appended at the end of the file (its last line :%d), so that no line before them moves: '
            'the certificate banked; the federation map’s name and the order of its merge; the eleven premise orders retired; the reading of a '
            'restore hit; the author’s word on the deposits and the keystones. The lines of the proof and of the three readings are appended '
            'beneath them at Component 3.' % (date, n_ot))
    paras = [head]
    for k in keys:
        if k not in E:
            continue
        if k == 'Q2':
            paras += E['Q2']
        else:
            paras.append(E[k])
        if k == 'M4':
            paras.append(extra['M4_entry'])
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, E=E, miss=miss, text=ot, new=base + NL + ot + NL, head=head, keys=keys, q2=q2, cf=cf, n_ot=n_ot,
                entry=extra['M4_entry'], paras=paras)


def flat(E):
    out = []
    for k, v in E.items():
        if isinstance(v, list):
            out += [('%s.%d' % (k, i + 1), x) for i, x in enumerate(v)]
        else:
            out.append((k, v))
    return out


def ledgers(group, mode):
    from standing import orders as O
    from standing import orderstate as OS
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(group, date, base)
    E, new, TP = C['E'], C['new'], C['TP']
    I, acct = ids(), account()
    eq = {}
    for k, v in flat(E):
        tk = k.split('.')[0]
        eq[k] = bool(re.fullmatch(pattern(TP[tk]), v, re.S)) and (NL + v + NL) in (NL + C['text'] + NL)
    left = sorted(set(m for m in FIELD.findall(C['text'])))
    ticks = [k + 1 for k, l in enumerate(C['text'].split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before = dict(O.read(base.split(NL)))
    after = dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    eleven = sorted(n for n, *_r in C['q2'])
    open_b = sum(1 for n in before if st(before, n) == 'OPEN')
    open_a = sum(1 for n in after if st(after, n) == 'OPEN')
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(C['text'], I, acct)
    present = [k for k, v in flat(E) if v in base] + ([MERGE] if MERGE in base else [])
    em = OS.ENTRYFORM.match(C['entry'])
    cf = C['cf'] or {}
    ctl = [('PLACE-papers` HEAD the corrigendum`s commit %s, the act`s one commit there before this write (%s)' % (C1PP, pp_head[:8]), pp_head.startswith(C1PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq, key=lambda x: (x.split('.')[0], int((x.split('.') + ['0'])[1]))))),
            bool(eq) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(C['miss']) or 'none missing'), not C['miss']),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts, and not %s, in OPEN_TRAILS before the write (%s)' % (MERGE, present or 'none'), not present),
           ('[E1]: the certificate`s foot 5 of 5 AS WANTED, primes %s, K values %s, the budget`s line agreeing with the json`s budget' % (
               cf.get('primes'), cf.get('k')), bool(cf.get('foot'))),
           ('[Q2]: the eleven of (R376)(6)(b), each a row A HYPOTHESIS BY DESIGN, no edge to the Hypothesis, its consequence retirement, its '
            'theorem the retirement section`s (%d lines)' % len(E['Q2']), len(E['Q2']) == 11 and not any(m.startswith('[Q2]') for m in C['miss'])),
           ('[M4]: the entry line in the form tools/standing/orderstate.py :26 reads, naming %s (%s)' % (MERGE, em.group(1) if em else None),
            bool(em) and em.group(1) == MERGE),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: the eleven moving OPEN -> CLOSED and no other order moving (moved %d: %s)' % (
               len(moved), [(n, st(before, n), st(after, n)) for n in moved if n not in eleven] or 'the eleven alone'),
            moved == eleven and all(st(before, n) == 'OPEN' and st(after, n) == 'CLOSED' for n in eleven)),
           ('the roster: %s added OPEN and no other order added (added %s)' % (MERGE, [(n, st(after, n)) for n in added]),
            added == [MERGE] and st(after, MERGE) == 'OPEN')]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R376)(4)(a) AND (6), GROUP %s: OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
         '### tools/b766_rulings.py ledgers %s; PLACE-papers HEAD %s; the texts from the ferry bank (data/b766_ferry.txt, sha256 %s), the fields from'
         % (group, pp_head[:8], FERRY_SHA),
         '### data/b766_certificate.json and .txt (sha256 %s, %s) and data/b765_premise_positions.txt (sha256 %s); <DATE> %s; each text by line and'
         % (fsha(CERT_JSON), fsha(CERT_TXT), fsha(os.path.join(D, 'b765_premise_positions.txt')), date),
         '### sha256 here; no PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  open before %d -> after %d ; orders %d -> %d ; added %s' % (open_b, open_a, len(before), len(after), [(n, st(after, n)) for n in added] or 'none'),
          '  statuses moving: %s' % ([(n, st(before, n), st(after, n)) for n in moved] or 'none')]
    nl_ = new.split(NL)
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(C['text'])[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', C['head'])] + [(k, v) for k, v in flat(E)] + [('M4 entry', C['entry'])]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    n_lines = len(C['paras']) - 1
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([E1], [M4] AND ITS ORDER`S ENTRY LINE, '
          '[Q2] x %d, [H5], [A1]) ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              group.upper(), n_lines, len(E['Q2']), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(C['text'])
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b766_ledgers_%s.txt' % group), os.path.join(D, 'b766_ledgers_%s.json' % group)
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
                                      sha_after=sha(new)[:16], text_sha=sha(C['text'])[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in flat(E)),
                            entry_line=[nl_.index(C['entry']) + 1, sha(C['entry'])[:16]], head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]],
                            keys=list(C['keys']), q2=[list(r) for r in C['q2']],
                            roster=dict(before_open=open_b, after_open=open_a, added=added, moved=[[n, st(before, n), st(after, n)] for n in moved]),
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))


# ================================================================================ COMPONENT 3: [F1] AND [F2], THE E0 GATE BEFORE THEM
def read_row(n):
    with open(os.path.join(D, 'b766_dispatch_rows.json'), encoding='utf-8') as f:
        rows = json.load(f)
    rr = [r for r in rows if r.get('kind') == 'read' and r.get('n') == n]
    return rr[-1] if rr else None


def e0_read(commit, path, short):
    """the theorem's statement at the commit, from its name to its first `:=`, graded by tools/e0_rule.py; None where it is not found."""
    import e0_rule as E0
    src = git(EF, 'show', '%s:%s' % (commit, path))
    m = re.search(DECL % re.escape(short), src, re.M)
    if not m:
        return None
    end = src.find(':=', m.end())
    head = src[m.end():end] if end > 0 else ''
    try:
        g, why, _b = E0.grade(head, 'theorem')
    except Exception as ex:   # noqa: BLE001
        g, why = 'UNCLASSED', ' '.join(str(ex).split())[:300]
    return dict(line=src.count(NL, 0, m.start()) + 1, head=' '.join(head.split()), grade=g, why=' '.join(str(why).split()))


def c3_fields():
    gates, miss, runs = [], [], {}
    for key in GROUPS['c3']:
        spec = C3[key]
        r = read_row(spec['read'])
        if not r:
            miss.append('[%s]: no read of dispatch %d in data/b766_dispatch_rows.json' % (key, spec['read']))
            continue
        runs[key] = r.get('run')
        st = dict((x[0], (x[1], x[2])) for x in (r.get('names') or []))
        pt = set(x.strip() for x in git(EF, 'show', '%s:print_targets.txt' % spec['commit']).split(NL))
        built = str(r.get('built_ref') or '').startswith(spec['commit']) and str(r.get('build_exit')) == '0'
        for path, shorts in spec['items']:
            for s in shorts:
                full = NS + s
                e = e0_read(spec['commit'], path, s) or {}
                state, ax = st.get(full, (None, None))
                gates.append(dict(key=key, name=full, commit=spec['commit'], path=path, line=e.get('line'), grade=e.get('grade', 'NOT READ'),
                                  why=e.get('why', ''), head=e.get('head', ''), state=state, axioms=ax, target=full in pt, run=r.get('run'),
                                  built=built))
    cs = git(EF, 'show', '%s:%s' % (C3['F2']['commit'], COEFFS), raw=True)
    coeffs = dict(sha=sha(cs)[:16] if cs else 'ABSENT', head=bool(cs) and WINDOW_SHA in cs[:4096].decode('utf-8', 'replace'))
    fields = {}
    if 'F1' in runs:
        fields['F1'] = [('<name>', '`%sprimeTermQ_eq_finite_sum` (with `primeTermQ_cQ_eq_finite_sum`, its reading at cQ)' % NS),
                        ('<commit>', '%s (SIDEExplicitFormula/Window/PrimeFinite.lean, built by runner run %s with the restore on)' % (
                            C3['F1']['commit'], runs['F1'])),
                        ('<the print>', '%s, each name as printed in that run (relay data/b766_dispatch_rows.json)' % STD3)]
    if 'F2' in runs:
        fields['F2'] = [('<commit>', '%s (SIDEExplicitFormula/Window/Coeffs.lean, Spline.lean and Instance.lean, built by runner run %s with the '
                                     'restore on)' % (C3['F2']['commit'], runs['F2'])),
                        ('<names>', '`windowH_contDiff`, `windowH_eq_zero`, `windowK_classK` and `windowK_eq_zero` of `SIDEExplicitFormula.Window`, '
                                    'which follow from eight theorems of Spline.lean that hold for every choice of weights,'),
                        ('<the print>', '%s for each of the twelve, as printed in that run (relay data/b766_dispatch_rows.json)' % STD3)]
    return fields, gates, miss, coeffs, runs


def ledgers_c3(mode):
    from standing import orders as O
    group, date = 'c3', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    TP = dict((k, v[2]) for k, v in texts(ferry()).items())
    fields, gates, miss, coeffs, runs = c3_fields()
    E = dict((k, fill(TP[k], fields[k])) for k in GROUPS[group] if k in fields)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b766, `(R376)`(4)(b) and (4)(c): the lines the ruling orders for OPEN_TRAILS where the theorems of (4)(b) and (4)(c) '
            'compile** (relay data/b766_ferry.txt :58-:64), appended at the end of the file (its last line :%d), so that no line before them moves: '
            'each theorem read at its statement by the E0 gate (relay tools/e0_rule.py) before it is entered, each graded DERIVES, its name in '
            'print_targets.txt at its commit and its axioms print banked (relay data/b766_dispatch_rows.json and data/b766_ledgers_c3.txt). The '
            'lines of the later steps of (4)(d) and of the three readings are appended beneath them later in Component 3.' % (date, n_ot))
    paras = [head] + [E[k] for k in GROUPS[group] if k in E]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before, after = dict(O.read(base.split(NL))), dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    grades = {}
    for g in gates:
        grades[g['grade']] = grades.get(g['grade'], 0) + 1
    n_all = sum(len(s) for k in GROUPS[group] for _p, s in C3[k]['items'])
    ctl = [('PLACE-papers` HEAD the act`s last commit there before this write, the lines of (6) %s (%s)' % (C2PP, pp_head[:8]), pp_head.startswith(C2PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq))), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('THE E0 GATE: each of the %d theorems read at its statement at its commit and graded (%s), each DERIVES' % (
               n_all, ', '.join('%s %d' % kv for kv in sorted(grades.items()))),
            len(gates) == n_all and all(g['line'] and g['grade'] == 'DERIVES' for g in gates)),
           ('each name in print_targets.txt at its commit (absent: %s)' % ([g['name'] for g in gates if not g['target']] or 'none'),
            bool(gates) and all(g['target'] for g in gates)),
           ('each name COMPILED in the read of its dispatch, built at its commit with exit 0, its axioms %s (runs %s)' % (STD3, runs),
            bool(gates) and all(g['state'] == 'COMPILED' and g['axioms'] == STD3 and g['built'] for g in gates)),
           ('[F2]: %s at %s its sha256 %s as data/b766_window_data.txt banks it (%s), its head naming the bank`s sha256 %s (%s)' % (
               COEFFS, C3['F2']['commit'], COEFFS_SHA, coeffs['sha'], WINDOW_SHA, coeffs['head']),
            coeffs['sha'] == COEFFS_SHA and coeffs['head']),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R376)(4)(b) AND (4)(c), GROUP C3: OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b766_rulings.py ledgers c3; PLACE-papers HEAD %s; the texts from the ferry bank (data/b766_ferry.txt, sha256 %s), the fields from'
         % (pp_head[:8], FERRY_SHA),
         '### data/b766_dispatch_rows.json (sha256 %s) and SIDE-explicit-formula at %s and %s; <DATE> %s; each text by line and sha256 here; no'
         % (fsha(os.path.join(D, 'b766_dispatch_rows.json')), C3['F1']['commit'], C3['F2']['commit'], date),
         '### PLACE-papers line printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE E0 GATE (tools/e0_rule.py grade(head, \'theorem\'), the head the statement from the name to its first `:=`, read at the commit)']
    P += ['  [%s] %-58s %s %s :%s ; GRADE %s ; %s ; %s ; target %s' % (
        g['key'], g['name'], g['commit'], g['path'], g['line'], g['grade'], g['why'] or '-', g['state'], g['target']) for g in gates]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    nl_ = new.split(NL)
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in GROUPS[group] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C3: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([F1], [F2]) ; THE E0 GATE %d OF %d '
          'DERIVES ; CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(paras) - 1, sum(1 for g in gates if g['grade'] == 'DERIVES'), n_all, sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b766_ledgers_c3.txt'), os.path.join(D, 'b766_ledgers_c3.json')
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
                            keys=list(GROUPS[group]), runs=runs, coeffs=coeffs,
                            e0=[dict((x, g[x]) for x in ('key', 'name', 'commit', 'path', 'line', 'grade', 'why', 'state', 'axioms', 'target')) for g in gates],
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))


def num(n):
    return '{:,}'.format(int(n))


def jbank(name):
    with open(os.path.join(D, name), encoding='utf-8') as f:
        return json.load(f)


def c4_fields(pp_head):
    """[X1] to [X3]'s fields from their readings' banks; each bank read where its controls each read AS WANTED and its PLACE-papers HEAD
    is the HEAD at the write."""
    fields, miss, src = {}, [], {}
    for key, name in (('X1', 'b766_registry_cells.json'), ('X2', 'b766_lean_join.json'), ('X3', 'b766_sweep.json')):
        try:
            j = jbank(name)
        except (OSError, ValueError) as ex:
            miss.append('[%s]: data/%s not read (%s)' % (key, name, type(ex).__name__))
            continue
        ctl = j.get('controls') or []
        good = bool(ctl) and all(bool(c[1]) for c in ctl)
        src[key] = dict(bank='data/' + name, sha=fsha(os.path.join(D, name)), controls=len(ctl), good=good, pp_head=j.get('pp_head'))
        if not good or not pp_head.startswith(str(j.get('pp_head'))):
            miss.append('[%s]: data/%s controls %s, PLACE-papers HEAD %s against %s' % (key, name, good, j.get('pp_head'), pp_head[:8]))
            continue
        if key == 'X1':
            m = X1_RE.match(j.get('sentence', ''))
            if not m:
                miss.append('[X1]: the sentence of data/%s not in its form' % name)
                continue
            fields['X1'] = [('<n>', num(x)) for x in m.groups()]
        elif key == 'X2':
            four = tuple(int(x) for x in (j.get('at_nav_rev') or {}).get('four') or ())
            top = j.get('top') or []
            if len(four) != 4 or len(top) < 3:
                miss.append('[X2]: data/%s holds no four counts at 29d4c9b7 or fewer than three kernels' % name)
                continue
            names = ', '.join('%s %s' % (k, num(v)) for k, v in top[:2]) + ' and %s %s' % (top[2][0], num(top[2][1]))
            fields['X2'] = [('<n>', num(j['decls'])), ('<n>', num(j['paper'])), ('<n>', num(j['pages_alone'])), ('<n>', num(j['neither'])),
                            ('<names with counts>', names),
                            ('<reproduced | differing as printed>', 'reproduced' if four == CANDIDATE else 'differing as printed')]
            src[key]['four_at_29d4c9b7'] = four
        else:
            fields['X3'] = [('<n>', num(j[k])) for k in ('entries', 'named', 'carried', 'not_carried', 'no_keystone', 'nameless', 'nameless_lines')]
    return fields, miss, src


def ledgers_c4(mode):
    from standing import orders as O
    group, date = 'c4', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    TP = dict((k, v[2]) for k, v in texts(ferry()).items())
    fields, miss, src = c4_fields(pp_head)
    E = dict((k, fill(TP[k], fields[k])) for k in GROUPS[group] if k in fields)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b766, `(R376)`(5): the lines the ruling orders for OPEN_TRAILS for the three readings toward the keystone set** '
            '(relay data/b766_ferry.txt :82-:92), appended at the end of the file (its last line :%d), so that no line before them moves: each '
            'text\'s fields from its reading\'s bank (relay data/b766_registry_cells.json, data/b766_lean_join.json and data/b766_sweep.json), each '
            'bank\'s controls AS WANTED; no line of REGISTRY, of the census or of a paper written. The lines of the later steps of (4)(d) are '
            'appended beneath them later in Component 3.' % (date, n_ot))
    paras = [head] + [E[k] for k in GROUPS[group] if k in E]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before, after = dict(O.read(base.split(NL))), dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    planted = fill(TP['X3'], [('<n>', '1')] * 7)
    ctl = [('PLACE-papers` HEAD the act`s last commit there before this write, [F1] and [F2] %s (%s)' % (C3PP, pp_head[:8]), pp_head.startswith(C3PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each reading`s bank read, its controls each AS WANTED and its PLACE-papers HEAD the HEAD now: %s' % (
               '; '.join('%s %s %s controls %d %s' % (k, v['bank'], v['sha'], v['controls'], v['good']) for k, v in sorted(src.items()))),
            len(src) == 3 and all(v['good'] for v in src.values())),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq))), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('the field matcher`s planted control: [X3] filled with seven planted figures read equal to its template, and a planted word in it not',
            bool(re.fullmatch(pattern(TP['X3']), planted, re.S)) and not re.fullmatch(pattern(TP['X3']), planted + ' planted', re.S)),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R376)(5), GROUP C4: OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b766_rulings.py ledgers c4; PLACE-papers HEAD %s; the texts from the ferry bank (data/b766_ferry.txt, sha256 %s), the fields from'
         % (pp_head[:8], FERRY_SHA),
         '### the three readings` banks (named in the controls with their sha256); <DATE> %s; each text by line and sha256 here; no PLACE-papers line'
         % date,
         '### printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    nl_ = new.split(NL)
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in GROUPS[group] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C4: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([X1], [X2], [X3]) ; CONTROLS %d OF %d '
          'AS WANTED ; %s.**' % (len(paras) - 1, sum(1 for _w, o in ctl if o), len(ctl),
                                 ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b766_ledgers_c4.txt'), os.path.join(D, 'b766_ledgers_c4.json')
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
                            keys=list(GROUPS[group]), sources=src,
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))


# ================================================================================ GROUP c5: [P2]
C4PP = '2d9d51ae'                # ### PLACE-papers' last commit of the act before the c5 write: [X1], [X2] and [X3] (step 50, data/b766_events.txt (77))
C5 = dict(read=14, commit='3c67b8b5', lemmas=12)   # ### data/b766_plan.txt :22-:60: twelve lemmas; dispatch 14 the act's last restored build (13 stopped under the hold, not scored)
P2_PRINCIPAL = ('primeTermQ_eq_finite_sum', 'windowH_contDiff', 'windowH_eq_zero', 'windowK_classK', 'windowK_eq_zero', 'windowK_log_kt',
                'cQ_eq_comb', 'poleTerm_windowK_intH', 'archTermQ_windowK_k0')
THM = re.compile(r'^(?:@\[[^\]\n]*\]\s*)?(?:(?:protected|private|nonrec)\s+)*theorem\s+([^\s(\[{:]+)', re.M)
WIN_DIR = 'SIDEExplicitFormula/Window/'
AX3 = {'propext', 'Classical.choice', 'Quot.sound'}


def ax_within(ax):
    s = str(ax or '').strip()
    if not (s.startswith('[') and s.endswith(']')):
        return False
    return set(x.strip() for x in s[1:-1].split(',') if x.strip()) <= AX3


def gate_ok(gates):
    return bool(gates) and all(g['line'] and g['grade'] not in ('NOT READ', 'UNCLASSED') for g in gates)


def c5_fields():
    r = read_row(C5['read'])
    if not r:
        return {}, [], ['[P2]: no read of dispatch %d in data/b766_dispatch_rows.json' % C5['read']], [], None, {}
    commit = C5['commit']
    st = dict((x[0], (x[1], x[2])) for x in (r.get('names') or []))
    built = str(r.get('built_ref') or '').startswith(commit) and str(r.get('build_exit')) == '0'
    pt = [x.strip() for x in git(EF, 'show', '%s:print_targets.txt' % commit).split(NL) if x.strip().startswith(NS)]
    where = {}
    files = [p.strip() for p in git(EF, 'ls-tree', '--name-only', commit, WIN_DIR).split(NL) if p.strip().endswith('.lean')]
    for p in files:
        for m in THM.finditer(git(EF, 'show', '%s:%s' % (commit, p))):
            where.setdefault(m.group(1), []).append(p)
    gates = []
    for full in pt:
        s = full[len(NS):]
        paths = where.get(s, [])
        e = (e0_read(commit, paths[0], s) if len(paths) == 1 else None) or {}
        state, ax = st.get(full, (None, None))
        gates.append(dict(name=full, path=paths[0] if len(paths) == 1 else ('NOT FOUND' if not paths else 'IN %d FILES' % len(paths)),
                          line=e.get('line'), grade=e.get('grade', 'NOT READ'), why=e.get('why', ''), head=e.get('head', ''),
                          state=state, axioms=ax, built=built))
    read_names = sorted(n for n in st if n.startswith(NS))
    fields = dict(P2=[('<n>', str(C5['lemmas'])),
                      ('<commit>', '%s on push-b766-proof (built by runner run %s with the restore on; the %d theorems of '
                                   '`SIDEExplicitFormula.Window` each read by the E0 gate, relay data/b766_ledgers_c5.txt)' % (
                                       commit, r.get('run'), len(pt))),
                      ('<names>', "L1 `primeTermQ_eq_finite_sum`, L2 the data file Coeffs.lean, L3 `windowH_contDiff`, L4 `windowH_eq_zero`, "
                                  "L5 `windowK_classK` and `windowK_eq_zero`, L6 the K values (`windowK_log_kt`), L7 the values of cQ "
                                  "(`cQ_eq_comb`), L8 the pole term (`poleTerm_windowK_intH`) and, of L9, its first part, the archimedean term "
                                  "by Gauss's integral with k(0) as data (`archTermQ_windowK_k0`)"),
                      ('<its name in the plan>', "L9 the archimedean term as the combination, its integral J in the B-spline basis and its sums "
                                                 "as the combination's coefficients, and after it L10 the enclosures, L11 `window_arith_neg` "
                                                 "and L12 `controlFailureExists`"),
                      ("<the error's opening line | not sent>", 'not sent')])
    return fields, gates, [], read_names, r, dict(files=len(files), where=len(where))


def ledgers_c5(mode):
    from standing import orders as O
    group, date = 'c5', today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    TP = dict((k, v[2]) for k, v in texts(ferry()).items())
    fields, gates, miss, read_names, r, scan = c5_fields()
    E = dict((k, fill(TP[k], fields[k])) for k in GROUPS[group] if k in fields)
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b766, `(R376)`(4)(d): the line the ruling orders for OPEN_TRAILS where the closing theorem does not compile at '
            'this act** (relay data/b766_ferry.txt :74-:76), appended at the end of the file (its last line :%d), so that no line before it '
            'moves: each compiled theorem of the Lean of this act read at its statement by the E0 gate (relay tools/e0_rule.py) before it is entered, '
            'its name in print_targets.txt at its commit and its axioms print banked (relay data/b766_dispatch_rows.json and '
            'data/b766_ledgers_c5.txt). Where the closing build from source and the restored build print different axioms files, [C7] is '
            'appended beneath it in Component 4.' % (date, n_ot))
    paras = [head] + [E[k] for k in GROUPS[group] if k in E]
    text = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    new = base + NL + text + NL
    I, acct = ids(), account()
    eq = dict((k, bool(re.fullmatch(pattern(TP[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL)) for k, v in E.items())
    left = sorted(set(FIELD.findall(text)))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R, n: (R.get(n) or {}).get('status')   # noqa: E731
    before, after = dict(O.read(base.split(NL))), dict(O.read(new.split(NL)))
    moved = sorted(n for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(new.split(NL))
    in_hand = [i + 1 for i in range(n_ot, len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    grades, axs = {}, {}
    for g in gates:
        grades[g['grade']] = grades.get(g['grade'], 0) + 1
        axs[str(g['axioms'])] = axs.get(str(g['axioms']), 0) + 1
    pop = sorted(g['name'] for g in gates)
    plant_gate = gate_ok([dict(gates[0], line=None, grade='NOT READ')] + gates[1:]) if gates else True
    plant_pop = (pop + [NS + 'b999_planted']) == read_names
    run = r.get('run') if r else None
    ctl = [('PLACE-papers` HEAD the act`s last commit there before this write, [X1] to [X3] %s (%s)' % (C4PP, pp_head[:8]), pp_head.startswith(C4PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base)),
           ('each text as entered equals the ruling`s with its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq[k]) for k in sorted(eq))), len(eq) == len(GROUPS[group]) and all(eq.values())),
           ('every text of the group composed (%s)' % ('; '.join(miss) or 'none missing'), not miss),
           ('no field left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('THE RUN: dispatch %d read, built at %s with exit 0 (run %s)' % (C5['read'], C5['commit'], run), bool(gates) and all(g['built'] for g in gates)),
           ('THE POPULATION: the names of %s in print_targets.txt at %s (%d) equal both ways to those the read of dispatch %d names (%d)' % (
               NS, C5['commit'], len(pop), C5['read'], len(read_names)), bool(pop) and pop == read_names),
           ('THE E0 GATE: each of the %d theorems found once by its declaration line among the %d Window files at the commit, read at its statement '
            'and graded (%s)' % (len(gates), scan.get('files', 0), ', '.join('%s %d' % kv for kv in sorted(grades.items()))), gate_ok(gates)),
           ('each COMPILED in the read, its axioms within %s, sorryAx in none (the prints: %s)' % (
               STD3, '; '.join('%s %d' % kv for kv in sorted(axs.items()))),
            bool(gates) and all(g['state'] == 'COMPILED' and ax_within(g['axioms']) for g in gates)),
           ('the nine names the text gives each in the population and COMPILED (absent: %s)' % (
               [s for s in P2_PRINCIPAL if NS + s not in pop] or 'none'), all(NS + s in pop for s in P2_PRINCIPAL)),
           ('PLANTED: a gate row with no statement read as the gate`s failure, and a planted name as the population`s (%s, %s)' % (
               'FAILED' if not plant_gate else 'PASSED', 'DIFFER' if not plant_pop else 'EQUAL'), not plant_gate and not plant_pop),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: no order moving and none added (moved %s ; added %s)' % (
               [(n, st(before, n), st(after, n)) for n in moved] or 'none', added or 'none'), not moved and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R376)(4)(d), GROUP C5: [P2], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, utc()), '',
         '### tools/b766_rulings.py ledgers c5; PLACE-papers HEAD %s; the text from the ferry bank (data/b766_ferry.txt, sha256 %s), the fields from'
         % (pp_head[:8], FERRY_SHA),
         '### data/b766_dispatch_rows.json (sha256 %s) and SIDE-explicit-formula at %s; <DATE> %s; the text by line and sha256 here; no'
         % (fsha(os.path.join(D, 'b766_dispatch_rows.json')), C5['commit'], date),
         '### PLACE-papers line printed but the text composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE E0 GATE (tools/e0_rule.py grade(head, \'theorem\'), the head the statement from the name to its first `:=`, read at %s)' % C5['commit']]
    P += ['  %-60s %s :%s ; GRADE %s ; %s ; %s %s' % (g['name'], g['path'], g['line'], g['grade'], g['why'] or '-', g['state'], g['axioms'])
          for g in gates]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    nl_ = new.split(NL)
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        n_ot, len(nl_) - 1, n_ot + 2, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', head)] + [(k, E[k]) for k in GROUPS[group] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP C5: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINE UNDER ONE HEAD ([P2]) ; THE E0 GATE %d OF %d READ ; '
          'CONTROLS %d OF %d AS WANTED ; %s.**' % (
              len(paras) - 1, sum(1 for g in gates if g['line']), len(gates), sum(1 for _w, o in ctl if o), len(ctl),
              ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b766_ledgers_c5.txt'), os.path.join(D, 'b766_ledgers_c5.json')
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
                            keys=list(GROUPS[group]), run=run, commit=C5['commit'],
                            e0=[dict((x, g[x]) for x in ('name', 'path', 'line', 'grade', 'why', 'state', 'axioms')) for g in gates],
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))


def main(argv):
    what, group, mode = (argv + ['', '', ''])[:3]
    if what != 'ledgers' or group not in GROUPS or mode not in ('dry', 'write'):
        sys.exit(__doc__)
    if group == 'c3':
        ledgers_c3(mode)
    elif group == 'c4':
        ledgers_c4(mode)
    elif group == 'c5':
        ledgers_c5(mode)
    else:
        ledgers(group, mode)


if __name__ == '__main__':
    main(sys.argv[1:])
