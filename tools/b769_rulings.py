# -*- coding: utf-8 -*-
"""tools/b769_rulings.py -- b769, (R379)(4): THE TEXTS OF THE RULING ENTERED IN OPEN_TRAILS, BY GROUP.

Carried in form from tools/b768_rulings.py's ledgers route (the texts read from the ferry bank between their marker lines and checked
against their lines; the file appended at its end, its bytes at HEAD a prefix of its new bytes; the controls before the write; the ledger
banked by line and sha256) by the Write tool, and committed before its run (N2). New at b769: the ruling's texts carry alternatives,
"<A | B>" and "<A: ... | B: ...>", which no earlier ferry carried. Each is resolved here to the form the banks give: a branch equal to the
form's label, or opening with the label and ': ', entered without the label, as [C9]'s "<where [B1] stands, this sentence: ...>" reads;
the chosen branch read as a substring of the ruling's text; the fields of that branch alone filled. The resolver reads every '<' as a
bracket and is used on [X4] and [M5] alone; a later group confirms it on its own texts by a control of its own.

  ledgers c2 dry|write   Component 2 (data/b769_ferry.txt :18-:19 and :52-:58), appended at OPEN_TRAILS' end, no line moving, under
                         one dated head, each a paragraph of its own --
                         [X4] (:53) in its WRITTEN form: its fields from data/b769_registry_block.json (the block's first line, its
                           rows and tables, KEYSTONE, the keystones by phase, the rows no earlier block reads), cross-read with that
                           bank's own x4 composition; REGISTRY at the papers` repository's HEAD equal by sha256 and lines to the block's
                           written bytes; the block's six controls and five guards each as wanted;
                         [M5] (:57) in its DISCHARGED form: its fields from data/b769_map_merge.json (the 81 and the 93), cross-read
                           with that bank's m5 words; SPIRAL_MAP.md at HEAD equal by sha256 to the merge's written bytes and the edition
                           unchanged from N3's reference; the merge's pre-controls and controls each as wanted, 93 present; [K30]
                           committed with its control AS WANTED at its line of data/b769_repair_controls.txt, VERSION at the relay's
                           HEAD its version.
                         Where a form's condition does not hold, a control reads NOT AS WANTED and nothing is written: the other form
                         is composed by an Edit committed before a run. Controls before the write, printed, among them three that can
                         fire: [M5]'s CARRIED form, its fields planted, read by the rule in memory as leaving the order OPEN; a
                         resolution by a label the text does not carry refused; an entered text with one literal word changed read
                         unequal. The roster by tools/standing/orders.py's rule in memory: W-ORD-MAP-MERGE moving from OPEN to CLOSED,
                         no other moving, none added. Bank: data/b769_ledgers_c2.txt and .json, each text by line and sha256; the
                         texts' words printed by the dry run alone.
[C9] (REGISTRY), [B1] or [B2], [A4], and Component 3's and 4's texts are groups this tool gains by an Edit committed before its run.

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
import b769_worklist as K   # noqa: E402

ACT, NL = 'b769', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b769_ferry.txt')
FERRY_SHA = '20ab92c5b57a9b5c'   # ### data/b769_stepzero.txt :12-:13 and data/b769_events.txt (1): the ferry bank's sha256
OT = 'OPEN_TRAILS.md'
C2PP = '9aab5f65'                # ### the papers` repository's last commit of the act before this write: the map's merge (step 18, events (54))
WANT = dict(X4=(53, 53), M5=(57, 57), C9=(61, 61), B1=(65, 65), B2=(69, 69), E2=(73, 85), F2=(89, 89), E3=(93, 105), F3=(109, 109),
            E4=(113, 125), F4=(129, 129), E5=(133, 145), F5=(149, 149), R3=(153, 153), V1=(157, 157), A4=(161, 161))
FIELD = re.compile(r'<[A-Za-z][^<>\n]*>')
MERGE_ORDER = 'W-ORD-MAP-MERGE'
GROUPS = dict(c2=('X4', 'M5'))
FORMS = dict(X4='WRITTEN', M5='DISCHARGED')     # ### the form each text takes where its condition holds
PLANT_FORM = ('M5', 'CARRIED', ('92', '93'))     # ### the planted form, read in memory alone: the control read 92 of 93 lines present
PLANT_WORD = ('no title changed', 'no title edited')   # ### one literal word of [X4] changed, read in memory alone
REG_BANK, MAP_BANK = os.path.join(D, 'b769_registry_block.json'), os.path.join(D, 'b769_map_merge.json')
CTL_BANK = os.path.join(D, 'b769_repair_controls.txt')
REG, MAP, MAP_OLD = 'REGISTRY.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md'
PHASES = (('THE DAY 1 CLUSTER', 'the Day 1 cluster'), ('PHASE 1.2', 'Phase 1.2'), ('PHASE 1.5', 'Phase 1.5'),
          ('METHOD, PHASE 2 IN TIME', 'method'), ('PHASE 2', 'Phase 2'))   # ### the block bank's phase keys and the words its x4 gives them


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


def jload(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def ids():
    import b769_address_scan as SC
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


def outer(tpl):
    """[(start, end, inner)] for each outermost <...> of a template, nested brackets balanced."""
    out, depth, start = [], 0, None
    for i, ch in enumerate(tpl):
        if ch == '<':
            if depth == 0:
                start = i
            depth += 1
        elif ch == '>' and depth:
            depth -= 1
            if depth == 0:
                out.append((start, i + 1, tpl[start + 1:i]))
    return out


def branches(inner):
    """the inner text split at ' | ' outside nested brackets; one item where it carries none."""
    out, depth, cur, i = [], 0, '', 0
    while i < len(inner):
        ch = inner[i]
        depth += (ch == '<') - (ch == '>')
        if depth == 0 and inner.startswith(' | ', i):
            out.append(cur)
            cur, i = '', i + 3
            continue
        cur += ch
        i += 1
    return out + [cur]


def resolve(tpl, label):
    """the template with each alternative (an outermost <...> holding ' | ') resolved to the branch `label` names -- a branch equal to
    the label, or opening with the label and ': ', entered without the label. Returns (text, [the chosen branches], None) or (None, [],
    why)."""
    out, at, chosen, alts = [], 0, [], 0
    for s, e, inner in outer(tpl):
        bs = branches(inner)
        if len(bs) < 2:
            continue
        alts += 1
        hit = [b for b in bs if b == label] + [b[len(label) + 2:] for b in bs if b.startswith(label + ': ')]
        if len(hit) != 1:
            return None, [], 'the label %r names %d branches of an alternative' % (label, len(hit))
        out += [tpl[at:s], hit[0]]
        chosen.append(hit[0])
        at = e
    if not alts:
        return None, [], 'no alternative in the text'
    return ''.join(out + [tpl[at:]]), chosen, None


def fill(tpl, values):
    t = tpl
    for ph, v in values:
        if ph not in t:
            die('THE FIELD %r NOT IN ITS TEMPLATE' % ph)
        t = t.replace(ph, v, 1)
    return t


# ================================================================================ THE FORMS' CONDITIONS AND FIELDS
def x4_fields():
    """[X4]'s WRITTEN fields from the block's bank, and its condition: REGISTRY at HEAD the block's written bytes, its controls and
    guards each as wanted, the keystones by phase summing to KEYSTONE."""
    R = jload(REG_BANK)
    reg = git(PP, 'show', 'HEAD:' + REG, raw=True)
    kp = R.get('keystones_by_phase') or {}
    counts = ', '.join('%s %d' % (w, len(kp.get(k) or [])) for k, w in PHASES)
    vals = [('<line>', str(R['block_first_line'])), ('<n>', str(R['rows'])), ('<n>', str(R['tables'])),
            ('<n>', str(R['counts']['KEYSTONE'])), ('<the counts>', counts), ('<n>', str(R['not_read_by_an_earlier_block']))]
    cond = [('REGISTRY at the papers` repository`s HEAD the block`s written bytes: sha256 %s against %s, lines %d against %d' % (
                sha(reg)[:16], R['file_sha_after'], reg.count(b'\n'), R['registry_lines_after']),
             sha(reg)[:16] == R['file_sha_after'] and reg.count(b'\n') == R['registry_lines_after']),
            ('the block`s controls %d of %d and guards %d of %d as wanted' % (
                sum(1 for _w, o in R['controls'] if o), len(R['controls']), sum(1 for _w, o in R['guards'] if o), len(R['guards'])),
             len(R['controls']) == 6 and len(R['guards']) == 5 and all(o for _w, o in R['controls'] + R['guards'])),
            ('the keystones by phase (%s) summing to KEYSTONE %d, the bank`s phases those named here (%s)' % (
                counts, R['counts']['KEYSTONE'], sorted(kp)),
             sorted(kp) == sorted(k for k, _w in PHASES) and sum(len(v) for v in kp.values()) == R['counts']['KEYSTONE'])]
    return vals, cond, R['x4'].replace('`', "'")


def m5_fields():
    """[M5]'s DISCHARGED fields from the merge's bank, and its condition: SPIRAL_MAP.md at HEAD the merge's written bytes, the edition
    unchanged from N3's reference, the merge's pre-controls and controls as wanted with 93 present, [K30] committed with its control."""
    M = jload(MAP_BANK)
    pre_pp = jload(os.path.join(D, 'act_current.json'))['pre_pp']
    smap = git(PP, 'show', 'HEAD:' + MAP, raw=True)
    old_h, old_r = git(PP, 'show', 'HEAD:' + MAP_OLD, raw=True), git(PP, 'show', '%s:%s' % (pre_pp, MAP_OLD), raw=True)
    k30 = [r for r in K.STANDING_REPAIRS if r[0] == '[K30]']
    ver = git(RELAY, 'show', 'HEAD:tools/standing/VERSION').strip()
    with open(CTL_BANK, encoding='utf-8') as f:
        cl = f.read().replace('\r', '').split(NL)
    want_line = '### ### **[K30] THE CONTROL AS WANTED: THE FAULT READ BEFORE AND CLEAN AFTER: True.**'
    k30_line = (cl + [''] * 999)[k30[0][4] - 1].rstrip() if k30 else ''
    vals = [('<n>', str(M['differing_old'])), ('<n>', str(M['differing']))]
    # ### the merge bank counts lines as b765 counts them, the text split at its line ends with the empty piece after the last kept
    # ### (data/b769_map_merge.json "pre": "SPIRAL_MAP.md 548, as b765 counts them"), so its count is the line ends and one; the first
    # ### dry read the line ends alone against it and held (data/b769_events.txt (59))
    cond = [('SPIRAL_MAP.md at HEAD the merge`s written bytes: sha256 %s against %s, lines as b765 counts them %d against %d (line ends %d)' % (
                sha(smap)[:16], M['sha_after'], smap.count(b'\n') + 1, M['lines_after'], smap.count(b'\n')),
             sha(smap)[:16] == M['sha_after'] and smap.count(b'\n') + 1 == M['lines_after']),
            ('SPIRAL_MAP_v0_7.md at HEAD its bytes at N3`s reference %s: sha256 %s, %s, the bank`s %s' % (
                pre_pp[:8], sha(old_h)[:16], sha(old_r)[:16], M['old_sha']),
             bool(old_h) and old_h == old_r and sha(old_h)[:16] == M['old_sha']),
            ('the merge`s pre-controls %d of %d and controls %d of %d as wanted, %d of %d differing lines present, %d the edition alone held' % (
                sum(1 for _w, o in M['pre'] if o), len(M['pre']), sum(1 for _w, o in M['controls'] if o), len(M['controls']),
                len(M['present']), M['differing'], M['differing_old']),
             all(o for _w, o in M['pre'] + M['controls']) and len(M['pre']) == 6 and len(M['controls']) == 5
             and len(M['present']) == M['differing'] == 93 and M['differing_old'] == 81),
            ('[K30] committed: the worklist`s row %s, VERSION at the relay`s HEAD %s, its control`s verdict at data/b769_repair_controls.txt :%s' % (
                (k30[0][1], k30[0][2]) if k30 else 'NONE', ver, k30[0][4] if k30 else '-'),
             bool(k30) and k30[0][1] == ver and k30_line == want_line)]
    return vals, cond, M['m5']


# ================================================================================ THE LEDGER
def compose(group, date, base):
    X = texts(ferry())
    TP = dict((k, X[k][2]) for k in X)
    keys = GROUPS[group]
    x4v, x4c, x4w = x4_fields()
    m5v, m5c, m5w = m5_fields()
    V, COND, WORDS = dict(X4=x4v, M5=m5v), dict(X4=x4c, M5=m5c), dict(X4=x4w, M5=m5w)
    R, E, CH, WHY = {}, {}, {}, {}
    for k in keys:
        R[k], CH[k], WHY[k] = resolve(TP[k], FORMS[k])
        if R[k] is not None:
            E[k] = fill(R[k], V[k])
    n_ot = len(base.split(NL)) - 1
    head = ('**Dated head, %s, b769, `(R379)`(4)(a) and (4)(b): the lines the ruling orders for OPEN_TRAILS at Component 2** (relay '
            'data/b769_ferry.txt :18-:19 and :52-:58), appended at the end of the file (its last line :%d), so that no line before them '
            'moves: the block of the registry by [X4], in the form its controls gave; the merge of the map by [M5], in the form its '
            'control and the key gave. The lines of the cluster`s source record and of the author`s rulings are appended beneath them '
            'later in Component 2.' % (date, n_ot))
    paras = [head] + [E[k] for k in keys if k in E]
    ot = NL.join(sum(([p, ''] for p in paras), []))[:-1]
    return dict(X=X, TP=TP, R=R, E=E, CH=CH, WHY=WHY, V=V, COND=COND, WORDS=WORDS, text=ot, new=base + NL + ot + NL, head=head,
                keys=keys, n_ot=n_ot, paras=paras)


def ledgers(group, mode):
    from standing import orders as O
    date = today()
    base = at_head(OT)
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    C = compose(group, date, base)
    E, new, TP, R, text = C['E'], C['new'], C['TP'], C['R'], C['text']
    I, acct = ids(), account()
    eq = dict((k, R[k] is not None and bool(re.fullmatch(pattern(R[k]), v, re.S)) and (NL + v + NL) in (NL + text + NL))
              for k, v in E.items())
    sub = dict((k, bool(C['CH'][k]) and all(b in TP[k] for b in C['CH'][k])) for k in C['keys'])
    cross = dict(X4=(C['WORDS']['X4'] in E.get('X4', '')), M5=(C['WORDS']['M5'] in E.get('M5', '')))
    left = sorted(set(FIELD.findall(text)) | set(x for x in ('<', '>') if x in text))
    ticks = [k + 1 for k, l in enumerate(text.split(NL)) if l.count('`') % 2]
    st = lambda R_, n: (R_.get(n) or {}).get('status')   # noqa: E731
    bl, nl_ = base.split(NL), new.split(NL)
    before, after = dict(O.read(bl)), dict(O.read(nl_))
    moved = sorted((n, st(before, n), st(after, n)) for n in after if n in before and st(before, n) != st(after, n))
    added = sorted(n for n in after if n not in before)
    hf = O.hand_flags(nl_)
    in_hand = [i + 1 for i in range(C['n_ot'], len(hf)) if hf[i]]
    ib, ia, it = idcount(base, I, acct), idcount(new, I, acct), idcount(text, I, acct)
    present = [k for k, v in E.items() if v in base]
    m5_status = O._status(O.mask(E.get('M5', '')), MERGE_ORDER)
    x4_names = sorted(set(O.NAME.findall(O.mask(E.get('X4', '')))))
    # ### the three planted checks, in memory alone
    pk, pform, pvals = PLANT_FORM
    p_tpl, _pc, p_why = resolve(TP[pk], pform)
    p_line = fill(p_tpl, list(zip(('<n>', '<n>'), pvals))) if p_tpl else ''
    p_status = O._status(O.mask(p_line), MERGE_ORDER) if p_line else None
    p_after = dict(O.read(bl + [p_line])) if p_line else {}
    q_tpl, _qc, q_why = resolve(TP['M5'], 'WRITTEN')
    w_line = E.get('X4', '').replace(PLANT_WORD[0], PLANT_WORD[1], 1)
    w_eq = bool(R.get('X4')) and w_line != E.get('X4') and bool(re.fullmatch(pattern(R['X4']), w_line, re.S))
    cond = [('[%s] %s: %s' % (k, FORMS[k], w), o) for k in C['keys'] for w, o in C['COND'][k]]
    ctl = [('the papers` repository`s HEAD the act`s last commit there before this write, the map`s merge %s (%s)' % (C2PP, pp_head[:8]),
            pp_head.startswith(C2PP)),
           ('OPEN_TRAILS` bytes at HEAD a prefix of its new bytes: no line moves', new.startswith(base))] + cond + [
           ('each alternative resolved to its form, the chosen branches each a substring of the ruling`s text: %s' % (
               ' '.join('%s %s %s' % (k, FORMS[k], sub[k]) for k in C['keys'])),
            all(sub.values()) and all(R[k] is not None for k in C['keys'])),
           ('each text as entered equals the ruling`s with its form chosen and its fields filled, each whole in the appended text: %s' % (
               ' '.join('%s %s' % (k, eq.get(k)) for k in C['keys'])), len(eq) == len(C['keys']) and all(eq.values())),
           ('each text`s fields as the banks composed them: [X4] the block bank`s x4, [M5] the merge bank`s m5 (%s)' % (
               ' '.join('%s %s' % (k, cross[k]) for k in C['keys'])), all(cross.values())),
           ('no field and no bracket left in the appended text (%s)' % (left or 'none'), not left),
           ('each appended line`s backticks even (odd at %s)' % (ticks or 'none'), not ticks),
           ('the identifiers` counts and the account`s equal before and after, and 0 in the appended text (the account read from the relay`s remote, '
            'never printed)', ib == {k: ia[k] - it[k] for k in ia} and not any(it.values()) and acct is not None),
           ('none of the texts in OPEN_TRAILS before the write (%s)' % (present or 'none'), not present),
           ('%s in OPEN_TRAILS before the write, OPEN by the rule, its entry at :%s' % (MERGE_ORDER, (before.get(MERGE_ORDER) or {}).get('entry')),
            st(before, MERGE_ORDER) == 'OPEN'),
           ('[M5] gives %s the status %s by the rule; [X4] names no order (%s)' % (MERGE_ORDER, m5_status, x4_names or 'none'),
            m5_status == ('CLOSED', 'DISCHARGED') and not x4_names),
           ('PLANTED: [M5] in its CARRIED form, read 92 of 93 planted, reads %s and leaves the order %s, read in memory alone' % (
               p_status, st(p_after, MERGE_ORDER)), p_status == ('OPEN', 'CARRIED') and st(p_after, MERGE_ORDER) == 'OPEN'),
           ('PLANTED: [M5] resolved by a label its text does not carry (WRITTEN) is refused (%s)' % (q_why or 'NOT REFUSED'),
            q_tpl is None and bool(q_why)),
           ('PLANTED: [X4] with one literal word changed (%r for %r) reads unequal to the ruling`s (%s)' % (
               PLANT_WORD[1], PLANT_WORD[0], 'EQUAL' if w_eq else 'UNEQUAL'), bool(w_line) and not w_eq),
           ('the appended lines outside a hand section (inside at %s)' % (in_hand or 'none'), not in_hand),
           ('the roster: %s moving from OPEN to CLOSED by [M5]`s status word, no other moving, none added (moved %s ; added %s)' % (
               MERGE_ORDER, moved or 'none', added or 'none'), moved == [(MERGE_ORDER, 'OPEN', 'CLOSED')] and not added)]
    ok = all(o for _w, o in ctl)
    P = ['%s -- (R379)(4)(a) AND (4)(b), GROUP %s: [X4] AND [M5], OPEN_TRAILS, APPENDED AT ITS END (%s)' % (ACT, group.upper(), utc()), '',
         '### tools/b769_rulings.py ledgers %s; the papers` repository at HEAD %s; the texts from the ferry bank (data/b769_ferry.txt, sha256 %s);'
         % (group, pp_head[:8], FERRY_SHA),
         '### the fields from data/b769_registry_block.json (sha256 %s) and data/b769_map_merge.json (sha256 %s); <DATE> %s; each text by line'
         % (fsha(REG_BANK), fsha(MAP_BANK), date),
         '### and sha256 here; no line of the papers` repository printed but the texts composed.', '', '## THE CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE FORMS', '  ' + ' ; '.join('[%s] %s, %d alternatives resolved' % (k, FORMS[k], len(C['CH'][k])) for k in C['keys'])]
    P += ['', '## THE ROSTER BY tools/standing/orders.py`S RULE IN MEMORY (printed)',
          '  orders %d -> %d ; statuses moving %s ; added %s' % (len(before), len(after), moved or 'none', added or 'none')]
    first = C['n_ot'] + 2
    P += ['', '## THE FILE: OPEN_TRAILS.md | lines %d -> %d | the appended text from :%d | its sha256 %s | the file`s sha256 %s -> %s' % (
        C['n_ot'], len(nl_) - 1, first, sha(text)[:16], sha(base)[:16], sha(new)[:16])]
    rows = [('head', C['head'])] + [(k, E[k]) for k in C['keys'] if k in E]
    P += ['', '## THE PARAGRAPHS BY LINE'] + ['  %-10s :%d (sha256 %s)' % (k, nl_.index(v) + 1, sha(v)[:16]) for k, v in rows]
    P += ['', '### ### **THE LEDGERS, GROUP %s: OPEN_TRAILS APPENDED, NO LINE MOVING ; %d LINES UNDER ONE HEAD ([X4] %s, [M5] %s) ; CONTROLS '
          '%d OF %d AS WANTED ; %s.**' % (group.upper(), len(C['paras']) - 1, FORMS['X4'], FORMS['M5'], sum(1 for _w, o in ctl if o), len(ctl),
                                          ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD')]
    print(NL.join(P))
    if mode == 'dry':
        print(NL + '### THE TEXT APPENDED TO OPEN_TRAILS.md (the dry run`s print alone):')
        print(text)
        return 0 if ok else 1
    if not ok:
        die('A CONTROL NOT AS WANTED')
    lb, lj = os.path.join(D, 'b769_ledgers_%s.txt' % group), os.path.join(D, 'b769_ledgers_%s.json' % group)
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    if any(idcount(NL.join(P), I, acct).values()):
        die('AN IDENTIFIER OR THE ACCOUNT IN THE BANK')
    with open(os.path.join(PP, OT), 'wb') as f:
        f.write(new.encode('utf-8'))
    if fsha(os.path.join(PP, OT)) != sha(new)[:16]:
        die('THE WRITTEN FILE IS NOT ITS COMPOSITION')
    put(lb, NL.join(P) + NL)
    put(lj, json.dumps(dict(at=utc(), act=ACT, group=group, date=date, pp_head=pp_head, forms=dict((k, FORMS[k]) for k in C['keys']),
                            fields=dict((k, [[ph, v] for ph, v in C['V'][k]]) for k in C['keys']),
                            file=dict(path=OT, lines_before=C['n_ot'], lines_after=len(nl_) - 1, first_new=first, sha_before=sha(base)[:16],
                                      sha_after=sha(new)[:16], text_sha=sha(text)[:16], prefix=new.startswith(base)),
                            entered=dict((k, [nl_.index(v) + 1, sha(v)[:16]]) for k, v in E.items()),
                            head=[nl_.index(C['head']) + 1, sha(C['head'])[:16]], keys=list(C['keys']),
                            roster=dict(moved=[list(x) for x in moved], added=added),
                            controls=[[w, o] for w, o in ctl]), ensure_ascii=False, indent=1) + NL)
    print('written OPEN_TRAILS.md ; %s and .json' % os.path.relpath(lb, RELAY).replace(os.sep, '/'))
    return 0


def main(argv):
    if len(argv) != 3 or argv[0] != 'ledgers' or argv[1] not in GROUPS or argv[2] not in ('dry', 'write'):
        sys.exit(__doc__)
    return ledgers(argv[1], argv[2])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
