# -*- coding: utf-8 -*-
"""standing/v1270.py -- THE CONTROLS OF v1.27.0 ((R357)(3)(i)-(x)), in v1260.py's form: each instance read through the route as it stood before the
repair and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with no failing side.
THE COMPILE CONTROL RUNS FIRST AND BEFORE ANY FIGURE PRINTS ((R345)(2)(i), carried). The route before the repair is read from the blob at BASE (b746's
closing), not from disk. The free memory is read and printed before each control. Each class may be run alone, one per call, in the foreground;
`--bank` writes the whole set, every class run in the one call. Written at b747 by the Write tool.

  python -X utf8 -u tools/standing/v1270.py control [state|hand|reason|rowid|orders|lsr|reader|carry|body|version ...] [--bank]
"""
import io
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = '3f5a33bb'   # ### b746's closing, the toolset as v1.26.0 left it
HOLD = 2560
ORDER_NAME = 'W-ORD-MECHANISM-ATTRIBUTION'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import carry as CY              # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import hook as HK               # noqa: E402
import lsrread as LSRD          # noqa: E402
import orders as O              # noqa: E402
import orderstate as OS         # noqa: E402
import relaypath as RPATH       # noqa: E402
import rootprompt as RP         # noqa: E402
import rowid as RI              # noqa: E402
import sectionput as SP         # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def base_src(rel):
    return show(BASE, rel)


def base_mod(rel, name):
    ns = {'__name__': name, '__file__': os.path.join(RELAY, rel)}
    exec(compile(base_src(rel), '%s@%s' % (name, BASE), 'exec'), ns)
    return ns


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.26.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.27.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.27.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def _refused(fn, *a, **k):
    try:
        r = fn(*a, **k)
        return False, r
    except SystemExit as e:
        return True, str(e)


# ================================================================================ (i) THE ORDER'S STATE FROM THE COMMIT'S PRESENCE
def control_state():
    L, g, n = ['### (state) (R357)(3)(i), b746 events (4): THE ENTERED/CARRIED WORD READ FROM THE ORDER COMMIT`S PRESENCE IN THE GIT LOG, NOT FROM A CONSTANT IN A LOCKED FILE'], 0, 0
    wl = base_src('tools/b746_worklist.py')
    const = re.search(r'(?m)^C3_ORDER_PP = (.*?)\s*(#.*)?$', wl)
    cval = const.group(1) if const else '### NOT FOUND'
    src = base_src('tools/acts/b746.py')
    old_reads = "('entered' if K.C3_ORDER_PP else 'carried')" in src
    L.append('  the route at %s: tools/acts/b746.py composes the word by %s ; tools/b746_worklist.py C3_ORDER_PP = %s' % (
        BASE, "('entered' if K.C3_ORDER_PP else 'carried')" if old_reads else '### THE CONSTANT READ NOT FOUND', cval))
    old_word = 'entered' if cval not in ('None', '', '()') else 'carried'
    # ### present: a commit in the range adds an entry-form line (PLACE-papers 84dbbf3e, W-ORD-EPSTEIN-COUNT-LEAN, a real entry) -- the constant None
    sha = OS.entry_commit('W-ORD-EPSTEIN-COUNT-LEAN', '84dbbf3e~1', '84dbbf3e')
    n += 1
    g += case(L, 'state', 'commit present: W-ORD-EPSTEIN-COUNT-LEAN over PLACE-papers 84dbbf3e~1..84dbbf3e (its entry commit), the constant None as b746 left it',
              'the constant None -> "%s" whatever the log holds' % old_word, 'entry commit %s -> "%s"' % ((sha or 'NONE')[:8], OS.state(sha)),
              old_word != 'entered', OS.state(sha) == 'entered' and bool(sha) and sha.startswith('84dbbf3e'))
    planted = [('f' * 40, ['*Appended 2026-11-08 at the plant: THE ORDER **`%s`** ENTERED by name.' % ORDER_NAME]), ('e' * 40, ['an unrelated line'])]
    ps = OS.entry_commit_in(planted, ORDER_NAME)
    n += 1
    g += case(L, 'state', 'commit present, planted in memory: a log of two commits, the newer adding %s`s entry-form line, the constant None' % ORDER_NAME,
              'the constant None -> "%s"' % old_word, 'entry commit %s -> "%s"' % ((ps or 'NONE')[:8], OS.state(ps)), old_word != 'entered', OS.state(ps) == 'entered')
    ab = OS.entry_commit(ORDER_NAME, '1967382', 'f62d997e')
    n += 1
    g += guard(L, 'state', 'commit absent: b746`s carry replayed, %s over PLACE-papers 1967382..f62d997e (b746`s range), the constant None' % ORDER_NAME,
               'entry commit %s -> "%s"' % (ab or 'NONE', OS.state(ab)), ab is None and OS.state(ab) == 'carried')
    am = io.open(os.path.join(T, 'acts', '%s.py' % A.current().get('act')), encoding='utf-8').read()
    reads_c = len(re.findall(r'(?:K|WL)\.C3_ORDER_PP\b', am))
    n += 1
    g += guard(L, 'state', 'the act module`s composer reads the word through standing/orderstate.py and no worklist constant (the closing`s files line and the record`s figures)',
               'K./WL.C3_ORDER_PP reads %d ; orderstate.entry_commit calls %d' % (reads_c, am.count("entry_commit('W-ORD-MECHANISM-ATTRIBUTION'")),
               reads_c == 0 and am.count("entry_commit('W-ORD-MECHANISM-ATTRIBUTION'") == 2)
    return L, g, n


# ================================================================================ (ii) EVERY QUESTION AFTER THE SEAL THROUGH THE COMPOSER
def _b746_entry():
    F = show('f62d997e', 'FINDINGS.md', repo=PP).split(NL)
    return NL.join(F[14146:14187])


def control_hand():
    L, g, n = ['### (hand) (R357)(3)(ii), b746 events (7): A QUESTION AFTER THE SEAL, THE HALT`S TEXT INCLUDED, RUN THROUGH compose_checked'], 0, 0
    old_has = 'def check_hand' in base_src('tools/standing/rootprompt.py')
    A_ = io.open(os.path.join(D, 'b746_author_answers.txt'), encoding='utf-8').read().split(NL)
    entry = _b746_entry()
    rd = RP.relay_reader()
    L.append('  the entry read: PLACE-papers FINDINGS.md :14147-:14187 at f62d997e (b746`s), %d characters' % len(entry))
    for ln, title in ((34, 'the N4 conflict, the question N3 found'), (27, 'the Order ID halt')):
        q = re.sub(r'^### PROMPT \d+ \([^)]*\): ', '', A_[ln - 1])
        ref, why = _refused(RP.check_hand, q, rd, entry)
        n += 1
        if ln == 34:
            g += case(L, 'hand', 'relay data/b746_author_answers.txt :%d (%s), put at 09:11:51Z outside the composer' % (ln, title),
                      'rootprompt.py at %s: check_hand %s -- the question put unchecked' % (BASE, 'PRESENT' if old_has else 'ABSENT'),
                      ('REFUSED: %s' % why[:260]) if ref else 'PASSED', not old_has,
                      ref and 'The sealed composer takes the entry title' in why)
        else:
            g += guard(L, 'hand', 'relay data/b746_author_answers.txt :%d (%s), put at 09:09:01Z outside the composer: through the check now; it names the entry in no sentence, '
                       'so the check finds nothing in it to refuse -- THE RULING`S "two ... refused" READS ONE: :34 refused, :27 passing, printed' % (ln, title),
                       ('REFUSED: %s' % why[:200]) if ref else 'PASSED, the composed text equal to the question as put', not ref)
    return L, g, n


# ================================================================================ (iii) THE CARRIED SENTENCE FROM THE ANSWERS BANK'S REASON
def control_reason():
    L, g, n = ['### (reason) (R357)(3)(iii), b746 events (5): THE CARRIED/ENTERED SENTENCE COMPOSED FROM THE ANSWERS BANK`S REASON, NOT ASSUMED'], 0, 0
    src = base_src('tools/acts/b746.py')
    old = 'carried, the author’s number not given'
    old_in = old in src
    want = 'carried on the defect of events (4), the author’s word to enter by name'
    ans = io.open(os.path.join(D, 'b746_author_answers.txt'), encoding='utf-8').read().replace('\r', '')
    ev = io.open(os.path.join(D, 'b746_events.txt'), encoding='utf-8').read().replace('\r', '')
    new = OS.reason_from(ORDER_NAME, None, ans, ev, 'data/b746_author_answers.txt', 'data/b746_events.txt')
    n += 1
    g += case(L, 'reason', 'b746`s carry replayed: the answers bank (:34 the conflict, :53 the carry word, :50 the word to enter by name) and the events bank ((4) quoting the carry)',
              'tools/acts/b746.py at %s composes "%s" (%s in the source) -- FINDINGS :14149, the number assumed not given' % (BASE, old, 'PRESENT' if old_in else 'ABSENT'),
              '"%s"' % new, old_in, new == want)
    en = OS.reason_from(ORDER_NAME, '0123456789abcdef0123456789abcdef01234567', ans, ev, 'a', 'e')
    n += 1
    g += guard(L, 'reason', 'the entered state: an entry commit given, the sentence names it and no carry', '"%s"' % en, en.startswith('entered by name at PLACE-papers 01234567'))
    return L, g, n


# ================================================================================ (iv) ROWID REFUSES A LEDGER OUTSIDE LEDGERS
def control_rowid():
    L, g, n = ['### (rowid) (R357)(3)(iv), b746 events (3): rowid.py `next` REFUSES BY NAME A FILE OUTSIDE LEDGERS, PRINTING NO ID; THE (R355) RULE BINDS THE LEDGERS, ORDERS BY NAME'], 0, 0
    old = base_mod('tools/standing/rowid.py', 'rowid_base')
    ot = show('HEAD', 'OPEN_TRAILS.md', repo=PP)
    oid = old['next_id'](ot, 'W-ORD')
    ref = RI.next_refusal('OPEN_TRAILS.md', 'W-ORD')
    n += 1
    g += case(L, 'rowid', 'rowid.py next OPEN_TRAILS.md W-ORD (b746`s call at the root, 09:07:58Z)', 'rowid.py at %s prints %s' % (BASE, oid),
              (ref or 'NO REFUSAL')[:220], oid == 'W-ORD-1', bool(ref) and 'W-ORD-1' not in ref and ref.startswith('### REFUSED: OPEN_TRAILS.md is not a ledger'))
    reg = show('HEAD', 'REGISTRY.md', repo=PP)
    nid = RI.next_id(reg, '1.5c') if not RI.next_refusal('REGISTRY.md', '1.5c') else 'REFUSED'
    n += 1
    g += guard(L, 'rowid', 'the positive control: rowid.py next REGISTRY.md 1.5c', 'prints %s' % nid, nid == '1.5c-24')
    L.append('  the rule as data/b747_rules.txt states it: %s' % RI.RULE_355)
    return L, g, n


# ================================================================================ (v) AN ORDER READ FROM ITS ENTRY, NOT FROM A QUOTATION OR A HAND SECTION
HAND_746 = ['', 'The root’s one call, one question (relay data/b746_author_answers.txt), and the author’s words at the root, carried below; the lines above are the composer’s and stand as written.',
            '', '**The attribution order**, the author’s answer at the root, verbatim: “Enter by name, no number: W-ORD-MECHANISM-ATTRIBUTION written to OPEN_TRAILS by its own commit under its W-ORD name, '
            'the title reading “entered”; the entry and the commit subject print the rowid.py halt (OPEN_TRAILS holds no order IDs; W-ORD-1) and the positive control (REGISTRY: 1.5c-24) in place of a number.”']


def control_orders():
    L, g, n = ['### (orders) (R357)(3)(v), b746 defect (e) and events (6): AN ORDER READ FROM ITS ENTRY, NOT FROM A TOKEN IN A QUOTATION OR A HAND SECTION'], 0, 0
    old = base_mod('tools/standing/orders.py', 'orders_base')
    lines = O.trail('HEAD')
    ro, rn = dict(old['read'](lines)), dict(O.read(lines))
    co = (len(ro), sum(1 for o in ro.values() if o['status'] == 'OPEN'))
    cn = (len(rn), sum(1 for o in rn.values() if o['status'] == 'OPEN'))
    eo, en = ro[ORDER_NAME]['entry'], rn[ORDER_NAME]['entry']
    tl = lines[eo - 1]
    inq = ORDER_NAME in tl and ORDER_NAME not in O.mask(tl)
    n += 1
    g += case(L, 'orders', 'b745`s trail line replayed: PLACE-papers OPEN_TRAILS.md at HEAD, %s' % ORDER_NAME,
              'entry :%d (%s) ; %d orders, %d open' % (eo, 'INSIDE A QUOTATION of the author`s word' if inq else 'outside a quotation', co[0], co[1]),
              'entry :%d (%s) ; %d orders, %d open' % (en, 'outside a quotation: b746`s heading, the order carried' if ORDER_NAME in O.mask(lines[en - 1]) else '### IN A QUOTATION', cn[0], cn[1]),
              inq, ORDER_NAME in O.mask(lines[en - 1]) and cn == co)
    pl = lines + HAND_746
    po, pn = dict(old['read'](pl)), dict(O.read(pl))
    cpo = (len(po), sum(1 for o in po.values() if o['status'] == 'OPEN'))
    cpn = (len(pn), sum(1 for o in pn.values() if o['status'] == 'OPEN'))
    n += 1
    g += case(L, 'orders', 'b746`s hand section replayed: its first form (the author`s answer quoted whole, its halt carrying W-ORD-1) appended in memory beneath the trail',
              '%d orders, %d open ; W-ORD-1 %s' % (cpo[0], cpo[1], 'READ AS AN ORDER' if 'W-ORD-1' in po else 'not read'),
              '%d orders, %d open ; W-ORD-1 %s' % (cpn[0], cpn[1], 'READ AS AN ORDER' if 'W-ORD-1' in pn else 'not read'),
              'W-ORD-1' in po and cpo == (co[0] + 1, co[1] + 1), 'W-ORD-1' not in pn and cpn == cn)
    entry = ['', '*Appended 2026-11-08 at b747 under (R357)(4) (planted in memory): THE ORDER **`%s`** ENTERED by name.' % ORDER_NAME]
    pe = dict(O.read(lines + entry))
    ce = (len(pe), sum(1 for o in pe.values() if o['status'] == 'OPEN'))
    L += ['  THE NAVIGATOR`S FIGURE BESIDE THE READ: (R357)(3)(v) names "207 orders, 72 open, then this act`s entry read as the 208th"; with this act`s entry-form line',
          '      appended in memory the reader reads %d orders, %d open, %s`s entry at :%d -- b746`s own trail names the order outside any quotation (:%d, the heading,' % (
              ce[0], ce[1], ORDER_NAME, pe[ORDER_NAME]['entry'], en),
          '      "carried"), so the order stands among the 207 before this act`s entry and the entry adds no 208th: THE NAVIGATOR`S 208th NOT READ, printed, not forced']
    n += 1
    g += guard(L, 'orders', 'the roll line from the output equals OPEN_TRAILS :17890 byte for byte at HEAD', 'equal %s' % (O.open_line([k for k, o in O.read(lines) if o['status'] == 'OPEN']) == lines[17889]),
               O.open_line([k for k, o in O.read(lines) if o['status'] == 'OPEN']) == lines[17889])
    return L, g, n


# ================================================================================ (vi) NONE OVER ZERO REPOSITORIES
def control_lsr():
    L, g, n = ['### (lsr) (R357)(3)(vi), b746 defect (m): lsrread PRINTS NONE OVER ZERO REPOSITORIES, AND NO ARM READS IT AS FAIL'], 0, 0
    old = base_mod('tools/standing/lsrread.py', 'lsr_base')
    b1 = io.open(os.path.join(D, 'b746_probe_standing-b1.txt'), encoding='utf-8').read().split(NL)
    l24 = b1[23] if len(b1) > 23 else ''
    L.append('  relay data/b746_probe_standing-b1.txt :24: %s' % l24.strip()[:200])
    vo, vn = old['verdict']({}, {}), LSRD.verdict({}, {})
    n += 1
    g += case(L, 'lsr', 'the standing-b1 probe replayed: a part reading zero repositories', 'verdict %s ; %s' % (vo[0], ' ; '.join(vo[1]) or 'no retry'),
              'verdict %s ; %s ; ok() %s' % (vn[0], ' ; '.join(vn[1]), LSRD.ok({}, {})), vo[0] == 'FAIL' and 'FAIL' in l24, vn[0] == 'NONE' and LSRD.ok({}, {}))
    tpl = io.open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'lsr', 'the suite`s arm counts NONE vacuous as it counts CACHED (checks.tpl)', "in ('CACHED', 'NONE') %s" % ("[0] in ('CACHED', 'NONE')" in tpl), "[0] in ('CACHED', 'NONE')" in tpl)
    v3 = LSRD.verdict({'D:/X': 3}, {'D:/X': dict(reads=1, secs=1.0, cached=False)})
    n += 1
    g += guard(L, 'lsr', 'three calls on one repository still FAIL (the arm`s plant)', 'verdict %s' % v3[0], v3[0] == 'FAIL')
    return L, g, n


# ================================================================================ (vii) THE READERS TAKE A RELAY PATH ONCE
def control_reader():
    L, g, n = ['### (reader) (R357)(3)(vii), b746 defect (p): THE RECORD`S READERS TAKE A PATH ONCE AND REFUSE ONE RESOLVING TO NO FILE, PRINTING IT'], 0, 0
    src = base_src('tools/b698_record.py')   # ### the base reader is b698's rd/rdn, bound by the template at BASE: its two functions read from the blob
    ns = {'__name__': 'r698', 'os': os, 'io': io, 'D': D}
    exec(compile('\n'.join(l for l in src.split(NL) if l.startswith(('def rd(', 'def rdn(', '    return io.open', '    return rd(os.path.join'))), 'b698_rd@' + BASE, 'exec'), ns)
    old = ns['rdn']('data/b746_section1.txt')
    ref, why = _refused(RPATH.rdn, 'data/b746_section1.txt')
    n += 1
    g += case(L, 'reader', "rdn('data/b746_section1.txt') replayed (b746`s N2 score route)", 'b698`s rdn at %s reads %d characters from %s, silently' % (
        BASE, len(old), os.path.join(D, 'data/b746_section1.txt').replace('\\', '/')), ('REFUSED: %s' % why[:200]) if ref else 'READ',
        old == '', ref and 'resolves to no file' in why)
    a, b = RPATH.rdn('b746_section1.txt'), RPATH.rdp('data/b746_section1.txt')
    n += 1
    g += guard(L, 'reader', "the bank by its name (rdn('b746_section1.txt')) and by its relay path (rdp('data/b746_section1.txt')): each joined once, the same text, [S1] PASS on it",
               '%d and %d characters ; equal %s ; [S1] PASS %s' % (len(a), len(b), a == b, '[S1] PASS' in a), a == b and '[S1] PASS' in a)
    tpl = io.open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    n += 1
    g += guard(L, 'reader', 'the record template binds rd and rdn to the standing reader', 'rd, rdn = RPATH.rd, RPATH.rdn %s' % ('rd, rdn = RPATH.rd, RPATH.rdn' in tpl), 'rd, rdn = RPATH.rd, RPATH.rdn' in tpl)
    return L, g, n


# ================================================================================ (viii) THE CARRY BESIDE THE RULING
def control_carry():
    L, g, n = ['### (carry) (R357)(3)(viii), b746 defects (d) and (o): THE CARRY PRINTS EVERY CARRIED ROW AND FIGURE BESIDE THE RULING AND REFUSES WHAT THE RULING DOES NOT NAME'], 0, 0
    old_has = 'def ruled' in base_src('tools/standing/carry.py')
    texts = (show('b15bfdf4', 'tools/acts/b746.py'), show('946cc80a', 'tools/acts/b745.py'), show('b15bfdf4', 'tools/b746_worklist.py'),
             show('946cc80a', 'tools/b745_worklist.py'), show('b15bfdf4', 'data/b746_ferry.txt'))
    Lr, ref = CY.ruled(*texts, subs=(('b745', 'b746'), ('b744', 'b745')))
    L += ['    ' + l for l in Lr if 'REFUSED' in l or 'ruled figures' in l]
    n += 1
    g += case(L, 'carry', 'b746`s carry replayed: tools/acts/b746.py and tools/b746_worklist.py as committed at b746`s step zero (relay b15bfdf4) beside b745`s at 946cc80a, (R356)`s ferry',
              'carry.py at %s: ruled %s -- the G-RUNNER-GATE sections and b745`s run ids carried, nothing refused' % (BASE, 'PRESENT' if old_has else 'ABSENT'),
              'refused %d: %s' % (len(ref), '; '.join('%s %s' % r[:2] for r in ref)), not old_has,
              any(r[0] == 'R2' and r[1] == 'SECTION checks 26' for r in ref) and any(r[0] == 'R3' and r[1] == 'EF_RUNS' for r in ref))
    t7 = tuple(io.open(os.path.join(RELAY, p), encoding='utf-8').read().replace('\r', '') for p in
               ('tools/acts/b747.py', 'tools/acts/b746.py', 'tools/b747_worklist.py', 'tools/b746_worklist.py', 'data/b747_ferry.txt'))
    L7, r7 = CY.ruled(*t7, subs=(('b746', 'b747'), ('b745', 'b746')))
    n += 1
    g += guard(L, 'carry', 'b747`s own carry beside (R357) (the working tree): every carried figure printed, none refused', L7[-1].strip('# *'), not r7)
    return L, g, n


# ================================================================================ (ix) A RECORD BODY THROUGH A BODY FILE; THE REPEAT REFUSALS
def control_body():
    L, g, n = ['### (body) (R357)(3)(ix), b746 defect (k), REPEAT: A RECORD BODY GOES THROUGH A BODY FILE; THE HOOK`S REFUSALS PRINTED'], 0, 0
    body = "    x_ = 'the `standing` reader'   # ### a backtick pair, as record section 4 carried\n"
    sh = subprocess.run(['bash', '-c', 'printf %%s "%s"' % body.replace('"', '\\"')], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    text = '#⟪SECTION record 4⟫\n    old\n#⟪END⟫\n'
    put = SP.put(text, 'record', 4, body)
    got = put[len('#⟪SECTION record 4⟫\n'):put.find('#⟪END⟫')]
    n += 1
    g += case(L, 'body', 'a section body carrying backticks, as b746`s record section 4 did', 'through a shell double-quoted string (b746`s `python -c "..."`): %r' % sh[:90],
              'through tools/standing/sectionput.py put from the body`s text: %s' % ('EQUAL, byte for byte' if got == body else '### DIFFERS'), sh != body, got == body)
    rows = [l for l in io.open(os.path.join(D, '%s_hook_refusals.txt' % A.current().get('act')), encoding='utf-8').read().split(NL) if l.strip()]
    kinds = {}
    for r in rows:
        k = r.split(' | ')[1] if ' | ' in r else '?'
        kinds[k] = kinds.get(k, 0) + 1
    L.append('  REPEAT: data/%s_hook_refusals.txt, %d refusal(s) by the hook this act so far: %s' % (A.current().get('act'), len(rows), ', '.join('%s %d' % kv for kv in sorted(kinds.items()))))
    L += ['    ' + r[:170] for r in rows]
    for cmd, want in (('python -X utf8 -u tools/standing/orders.py control > /dev/null', 'REDIR'), ('sed -n 1,60p tools/standing/carry.py', 'SED')):
        j = HK.judge('Bash', {'command': cmd}, RELAY)
        n += 1
        g += guard(L, 'body', 'a Bash command of the refused kind %s (an instance this act repeated)' % want, 'judged %s' % (j[0] if j else 'ALLOWED'), bool(j) and j[0] == want)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R357)(3)(x): THE STANDING VERSION PRINTED, ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    old = base_src('tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', old, ver, old == 'v1.26.0', ver == 'v1.27.0')
    return L, g, n


CONTROLS = {'state': control_state, 'hand': control_hand, 'reason': control_reason, 'rowid': control_rowid, 'orders': control_orders, 'lsr': control_lsr,
            'reader': control_reader, 'carry': control_carry, 'body': control_body, 'version': control_version}
ORDER = ('state', 'hand', 'reason', 'rowid', 'orders', 'lsr', 'reader', 'carry', 'body', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.27.0, (R357)(3)(i)-(x): THE ORDER`S STATE FROM THE COMMIT, EVERY QUESTION AFTER THE SEAL THROUGH THE COMPOSER, '
           'THE CARRIED SENTENCE FROM ITS REASON, ROWID OVER THE LEDGERS ALONE, THE ORDER FROM ITS ENTRY, NONE OVER ZERO REPOSITORIES, THE READERS TAKING A PATH ONCE, '
           'THE CARRY BESIDE THE RULING, THE BODY FILE AND THE REPEAT REFUSALS, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### the instances read at their commits; each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.27.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1270.txt' % act), NL.join(out))
        print('written data/%s_standing_v1270.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
