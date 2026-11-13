# -*- coding: utf-8 -*-
"""b754_sitting.py -- (R364)(5)[A]: THE REFERENCE LAYER'S PASSED ITEMS WRITTEN, each row banked in data/b754_sitting.json.

THE WORD. The author's answer to the [A] put (data/b754_put_2.json), banked by the answers route at data/b754_author_answers.txt :28
(2026-11-13T20:50:03Z): [A1] form (a), [A2] form (b), [A3] form (a), [A4] form (a), [A5] passed. The tool reads that line at every run and
refuses an item whose label it does not find there.
THE DRAFTS. Each is the ruling's own words, cut from data/b754_ferry.txt at HEAD (:20 to :24) between two exact needles, each needle found
once in its line; [A4]'s closing cites read as the amendment row 3 (3) gives them (b754_agenda.AMEND_A4, found once). The seat changes no
word of a draft: the drafts' date 2026-11-12 stands as the ruling wrote it, and the row carries the date of the write.
THE WRITE. Each write to FINDINGS.md replaces one line by one line ((R364)(5)[A]): the file's line count printed before and after and the
write refused unequal; every line but the item's read byte-equal after it; each line's ending kept. Before it: the CURRENT of each line the
item writes read at PLACE-papers HEAD and compared with the agenda's quoted line (data/b754_agenda.txt at relay HEAD), a mismatch refusing
the item; the file clean against HEAD; none of the item's lines among [Q] row (3)'s lines (the word read at run time from REGISTRY :373 and
never printed). The tool commits nothing: each item's FINDINGS write is committed through the one-call tool in a message of its own.
[A5]. PLACE-papers' description in the form of tools/b736_sitting.py :458-:472, each remote call its own command ((R364)(8)): `a5 read`
(gh in PLACE-papers' clone, the repository named by no argument, captured to the state folder), `a5 write` (the capture of today compared
with the agenda's CURRENT, then `gh repo edit --description <draft>`), `a5 back` (the read-back, compared with the draft, the row banked).

  python -X utf8 -u tools/b754_sitting.py control          the controls alone, nothing written and nothing read remotely
  python -X utf8 -u tools/b754_sitting.py dry <A1..A4>     the controls, the CURRENT against the agenda, the lines composed; nothing written
  python -X utf8 -u tools/b754_sitting.py write <A1..A4>   the same, then FINDINGS.md written and the item's row banked
  python -X utf8 -u tools/b754_sitting.py confirm <A1..A4> after the item's commit: PLACE-papers HEAD touching FINDINGS.md alone, its lines
                                                           the row's; the commit written to the row
  python -X utf8 -u tools/b754_sitting.py a5 <read|write|back>
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import statedir   # noqa: E402
import b754_agenda as AG   # noqa: E402
import b754_doors as DOORS   # noqa: E402

ACT = 'b754'
SELF = 'tools/%s_sitting.py' % ACT
BANK = os.path.join(RELAY, 'data', '%s_sitting.json' % ACT)
CAP = statedir.act_dir(ACT, 'sitting')
PP = AG.PP
FREL = 'FINDINGS.md'
FPATH = os.path.join(PP, FREL)
NL = '\n'
ANSWERS = 'data/%s_author_answers.txt' % ACT
ANSWERS_LINE = 28
WORD_AT = '2026-11-13T20:50:03Z'
WORD_CITE = '%s :%d' % (ANSWERS, ANSWERS_LINE)
# ### the label the author chose at each question of data/b754_put_2.json, and the form it passes
LABELS = {'[A1]': '(a) edited in place (Recommended)', '[A2]': '(b) retired (Recommended)', '[A3]': '(a) edited in place (Recommended)',
          '[A4]': '[A4] (a), [A5] passed (Recommended)'}
FORMS = {'[A1]': '(a)', '[A2]': '(b)', '[A3]': '(a)', '[A4]': '(a)', '[A5]': 'passed'}
LABEL_OF = {'[A5]': '[A4]'}   # ### [A5] answered with [A4] in the put's fourth question
# ### each write: (FINDINGS line, kind, opening needle, closing needle); kinds: 'line' the line replaced whole, 'tags' the line's tag words
# ### replaced and its words after them kept, 'head' the draft put at the line's head with its own words kept after it
SPEC = {'[A1]': [(901, 'line', 'Line :901 replaced by: "', '" Line :902'),
                 (902, 'tags', "Line :902's tag words replaced by \"", '", the deposit sentence')],
        '[A2]': [(979, 'head', 'Line :979 gains at its head, its own words staying after it: "', '" Where [A1] does not pass as (a)')],
        '[A3]': [(897, 'line', 'Line :897 replaced by: "', '" and line :898 by "'),
                 (898, 'line', 'and line :898 by "', '" FORM (b), RETIRED.')],
        '[A4]': [(905, 'line', 'Line :905 replaced by: "', '" and line :906 by "'),
                 (906, 'line', 'and line :906 by "', '" FORM (b), RETIRED.')]}
A2_POINTER = ('the anchor `riemann-hypothesis`', 'REGISTRY :953-:965')   # ### [A2]'s pointer where [A1] does not pass as (a)
TAGS = re.compile(r'^(\*[^*]+\* —) (?=\*\*)')
LINE_CUR = re.compile(r'^    :(\d+) "(.*)"$')
LINE_DIG = re.compile(r'^    :(\d+) BY LINE AND DIGEST ([0-9a-f]{16})')
A5_CUR = re.compile(r'^  CURRENT \(by gh at ([0-9T:\-]+Z), data/b754_doors\.txt\): "(.*)"$')


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def run(argv, cwd=None):
    r = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=cwd)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:16]


# ---------------------------------------------------------------- the word
def word_labels(line):
    """{item: label} from the answers bank's RESULT line: each question opening on its item's tag, the label after its `"="`."""
    out = {}
    parts = line.split('"="')
    for i in range(1, len(parts)):
        q = parts[i - 1]
        j = q.rfind('"[A')
        m = re.match(r'"(\[A\d\])', q[j:]) if j >= 0 else None
        if m:
            out[m.group(1)] = parts[i].split('"', 1)[0]
    return out


def the_word():
    L = AG.git(RELAY, 'show', 'HEAD:%s' % ANSWERS).replace('\r', '').split(NL)
    line = L[ANSWERS_LINE - 1] if len(L) >= ANSWERS_LINE else ''
    if not line.startswith('RESULT (transcript line 11d67961:14163, %s' % WORD_AT[:-1]):
        raise SystemExit('### THE WORD NOT AT %s: the line opens %r -- NOTHING DONE' % (WORD_CITE, line[:80]))
    return word_labels(line)


def word_ok(item, got):
    q = LABEL_OF.get(item, item)
    return got.get(q) == LABELS[q]


# ---------------------------------------------------------------- the drafts
def cut(text, a, b):
    """the words between needle a and needle b, each found once in text; None where either is not found once."""
    if text.count(a) != 1 or text.count(b) < 1:
        return None
    i = text.index(a) + len(a)
    j = text.find(b, i)
    if j < 0 or text.count(b, i) != 1:
        return None
    return text[i:j]


def drafts(FL, a1_form=None):
    """{item: [(line, kind, draft, ferry line)]} cut from the ferry bank; None for a draft whose needles do not meet their line once."""
    out = {}
    for item, specs in SPEC.items():
        n = [x for x in AG.FERRY if x[0] == item][0][1]
        text = AG.draft(FL, item)
        rows = []
        for k, kind, a, b in specs:
            d = cut(text, a, b)
            if d is not None and item == '[A4]' and k == 905:
                d = d.replace(*AG.AMEND_A4) if d.count(AG.AMEND_A4[0]) == 1 else None
            if d is not None and item == '[A2]' and (a1_form or FORMS['[A1]']) != '(a)':
                d = d.replace(*A2_POINTER) if d.count(A2_POINTER[0]) == 1 else None
            rows.append((k, kind, d, n))
        out[item] = rows
    return out


def a5_draft(FL):
    s = AG.draft(FL, '[A5]')
    a = 'DRAFTED: "'
    if s.count(a) != 1 or not s.endswith('"'):
        return None
    return s[s.index(a) + len(a):-1]


# ---------------------------------------------------------------- the file, one line for one line
def split_bytes(data):
    """(parts, count): the file split at b'\\n', each part keeping a b'\\r' it carries; count the lines as a reader counts them."""
    parts = data.split(b'\n')
    return parts, len(parts) - (1 if parts[-1] == b'' else 0)


def get_line(parts, k):
    raw = parts[k - 1]
    return (raw[:-1] if raw.endswith(b'\r') else raw).decode('utf-8')


def put_lines(data, new):
    """data with each line k of `new` replaced, its ending kept; refused where a new line carries a line break."""
    parts, n0 = split_bytes(data)
    for k, s in new.items():
        if '\n' in s or '\r' in s or not (0 < k <= n0):
            raise SystemExit('### NOT ONE LINE FOR ONE LINE at :%d -- NOTHING WRITTEN' % k)
        cr = parts[k - 1].endswith(b'\r')
        parts[k - 1] = s.encode('utf-8') + (b'\r' if cr else b'')
    out = b'\n'.join(parts)
    return out


def check_write(before, after, new):
    """(count before, count after, lines differing outside the item's): the write's own reading."""
    pb, nb = split_bytes(before)
    pa, na = split_bytes(after)
    other = [k for k in range(1, min(len(pb), len(pa)) + 1) if k not in new and pb[k - 1] != pa[k - 1]]
    wrong = [k for k in new if get_line(pa, k) != new[k] or pa[k - 1].endswith(b'\r') != pb[k - 1].endswith(b'\r')]
    return nb, na, other + wrong + ([] if len(pb) == len(pa) else ['parts %d -> %d' % (len(pb), len(pa))])


def compose(item, F, D):
    """[(k, kind, old, new, draft)] for the item over FINDINGS' lines F (text), from its drafts D[item]."""
    out = []
    for k, kind, d, n in D[item]:
        if d is None:
            raise SystemExit('### %s: THE DRAFT FOR :%d NOT CUT FROM data/b754_ferry.txt :%d -- NOTHING DONE' % (item, k, n))
        old = F[k - 1]
        if kind == 'line':
            new = d
        elif kind == 'tags':
            m = TAGS.match(old)
            if not m:
                raise SystemExit('### %s: :%d CARRIES NO TAG WORDS BEFORE ITS BOLD WORDS -- NOTHING DONE' % (item, k))
            new = d + old[len(m.group(1)):]
        elif kind == 'head':
            new = d + ' ' + old
        out.append((k, kind, old, new, d))
    return out


# ---------------------------------------------------------------- the agenda's CURRENT
def agenda_current(A):
    """{(item, line): ('text', words) or ('digest', d)} from the agenda's [A1]-[A4] CURRENT blocks; and [A5]'s (time, words)."""
    out, cur, a5 = {}, None, None
    for l in A:
        m = re.match(r'^(\[A\d\]) ', l)
        if m:
            cur = m.group(1)
            continue
        if l.startswith('## '):
            cur = None
        m1, m2, m3 = LINE_CUR.match(l), LINE_DIG.match(l), A5_CUR.match(l)
        if cur and m1:
            out[(cur, int(m1.group(1)))] = ('text', m1.group(2))
        elif cur and m2:
            out[(cur, int(m2.group(1)))] = ('digest', m2.group(2))
        if cur == '[A5]' and m3:
            a5 = (m3.group(1), m3.group(2))
    return out, a5


def agrees(entry, s):
    if entry is None:
        return False
    return entry[1] == s if entry[0] == 'text' else entry[1] == digest(s)


# ---------------------------------------------------------------- the bank
def rows():
    if not os.path.exists(BANK):
        return {}
    return json.load(io.open(BANK, encoding='utf-8')).get('rows', {})


def bank(R):
    j = {'what': '(R364)(5)[A] the passed items written by %s, one row an item; the word %s (%s); the drafts cut from data/b754_ferry.txt at '
                 'HEAD; the lines cited by FINDINGS line and digest' % (SELF, WORD_CITE, WORD_AT), 'at': stamp(), 'rows': R}
    with open(BANK + '.tmp', 'wb') as f:
        f.write((json.dumps(j, indent=1, ensure_ascii=False, sort_keys=True) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print('  BANKED %s: %d row(s) %s' % (os.path.relpath(BANK, RELAY).replace('\\', '/'), len(R), sorted(R)))


# ---------------------------------------------------------------- the controls
def controls():
    C = []

    def case(name, ok, got):
        C.append(ok)
        print('  (%d) %-78s %s ; %s' % (len(C), name[:78], 'AS WANTED' if ok else 'NOT AS WANTED', got))
    print('### THE CONTROLS (%s)' % SELF)
    FL = AG.ferry_lines()
    D = drafts(FL)
    cuts = [(it, k) for it in D for (k, _kd, d, _n) in D[it] if d]
    case('every needle meets its ferry line once, every draft cut (7 of 7)', len(cuts) == 7, '%d of 7 %s' % (len(cuts), cuts))
    d905 = [d for (k, _kd, d, _n) in D['[A4]'] if k == 905][0] or ''
    case('[A4] :905 carries row 3 (3)`s cites once, the ruling`s form none', d905.count(AG.AMEND_A4[1]) == 1 and '(FINDINGS :6880-:6884)' not in d905,
         'amended %d' % d905.count(AG.AMEND_A4[1]))
    d979 = [d for (k, _kd, d, _n) in D['[A2]'] if k == 979][0] or ''
    D_b = drafts(FL, a1_form='(b)')
    d979b = [d for (k, _kd, d, _n) in D_b['[A2]'] if k == 979][0] or ''
    case('[A2]`s pointer the anchor`s name with [A1] (a); REGISTRY :953-:965 with a planted (b)', A2_POINTER[0] in d979 and A2_POINTER[1] in d979b
         and A2_POINTER[0] not in d979b, 'as passed %s ; planted %s' % (A2_POINTER[0] in d979, A2_POINTER[1] in d979b))
    planted_text = 'x "Line :901 replaced by: "a" Line :902 b "Line :901 replaced by: "c" Line :902'
    case('a needle met twice refuses its cut (planted)', cut(planted_text, 'Line :901 replaced by: "', '" Line :902') is None, 'None')
    W = the_word()
    case('the word read at %s: every item`s label the author chose' % WORD_CITE, all(word_ok(i, W) for i in FORMS), W)
    planted = dict(W, **{'[A2]': '(a) edited in place'})
    case('a planted word with [A2]`s label changed reads not passed as (b)', not word_ok('[A2]', planted), 'word_ok %s' % word_ok('[A2]', planted))
    data = b''.join(b'line %d\r\n' % k for k in range(1, 13))
    after = put_lines(data, {5: 'five'})
    nb, na, bad = check_write(data, after, {5: 'five'})
    case('a planted CRLF file of 12 lines: :5 written, the count equal, its CR kept, the rest byte-equal', nb == na == 12 and not bad
         and after.split(b'\n')[4] == b'five\r', 'count %d -> %d ; differing %s' % (nb, na, bad or 'none'))
    try:
        put_lines(data, {5: 'two\nlines'})
        refused = False
    except SystemExit:
        refused = True
    case('a planted draft carrying a line break refused', refused, 'refused %s' % refused)
    nb2, na2, bad2 = check_write(data, data.replace(b'line 7', b'line 7x'), {5: 'line 5'})
    case('a planted change outside the item`s line read by the check', 7 in bad2, 'differing %s' % bad2)
    case('the tag words read on a planted line; a line with none refused', TAGS.match('*a · b* — **X** y') is not None and TAGS.match('**X** y') is None,
         'matched %r' % (TAGS.match('*a · b* — **X** y').group(1)))
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    cur, a5 = agenda_current(A)
    want = sorted((it, k) for it in SPEC for (k, _kd, _a, _b) in SPEC[it])
    case('the agenda`s CURRENT found for every line the items write (7) and for [A5]', all(w in cur for w in want) and a5 is not None,
         '%d of %d ; [A5] %s' % (sum(1 for w in want if w in cur), len(want), a5[0] if a5 else None))
    e = cur.get(('[A3]', 897))
    case('a planted CURRENT one character apart reads not agreeing', e is not None and not agrees(e, (e[1] + 'x') if e[0] == 'text' else 'x'), 'agrees False')
    word = DOORS.q_word()
    F = AG.lines(PP, 'HEAD', FREL)
    R = AG.lines(PP, 'HEAD', 'REGISTRY.md')
    prot = AG.protected_lines(F, R, word)['FINDINGS.md']
    hit = [k for (_it, k) in want if k in prot]
    case('[Q] row (3): none of the items` lines protected; :820 protected (the word read, not printed)', not hit and 820 in prot and word is not None,
         'items` lines protected %s ; :820 %s' % (hit or 'none', 820 in prot))
    d5 = a5_draft(FL) or ''
    acct = DOORS.account(PP)
    case('[A5]`s draft cut from data/b754_ferry.txt :24, withheld by no kind', bool(d5) and d5.endswith('correction).') and not DOORS.withheld(d5, acct, word),
         '%d characters, digest %s' % (len(d5), digest(d5)))
    ok = sum(C)
    print('### CONTROLS %d OF %d %s' % (ok, len(C), 'AS WANTED' if ok == len(C) else 'NOT AS WANTED'))
    return ok == len(C)


# ---------------------------------------------------------------- an item of [A1]-[A4]
def item_plan(item):
    W = the_word()
    if not word_ok(item, W):
        raise SystemExit('### %s: THE WORD AT %s READS %r, NOT %r -- NOTHING DONE' % (item, WORD_CITE, W.get(item), LABELS[item]))
    D = drafts(AG.ferry_lines())
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    F = AG.lines(PP, 'HEAD', FREL)
    data = open(FPATH, 'rb').read()
    clean = AG.gitq(PP, 'diff', '--quiet', 'HEAD', '--', FREL)[0] == 0
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    cur, _a5 = agenda_current(A)
    plan = compose(item, F, D)
    print('### %s %s, the word %s (%s): label %r' % (item, FORMS[item], WORD_AT, WORD_CITE, LABELS[item]))
    print('  PLACE-papers HEAD %s ; FINDINGS.md clean against HEAD %s ; %d bytes' % (head[:8], clean, len(data)))
    agree = True
    for k, kind, old, new, d in plan:
        a = agrees(cur.get((item, k)), old)
        agree = agree and a
        print('  :%d %s ; CURRENT at HEAD digest %s, %d characters ; the agenda`s %s' % (k, kind, digest(old), len(old), 'AGREES' if a else 'DIFFERS'))
        print('      new digest %s, %d characters ; the draft %d characters (data/b754_ferry.txt :%d)' % (digest(new), len(new), len(d),
                                                                                                    [x for x in AG.FERRY if x[0] == item][0][1]))
        print('      NEW: %s' % new)
    for hk in [x[2] for x in AG.ANCHORS if x[0] == item]:
        print('  the heading :%d stands: %s' % (hk, F[hk - 1]))
    return dict(head=head, data=data, clean=clean, agree=agree, plan=plan, F=F)


def item_write(item, write):
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if item in rows():
        raise SystemExit('### %s HAS ITS ROW ALREADY -- NOTHING DONE' % item)
    P = item_plan(item)
    if not P['clean'] or not P['agree']:
        raise SystemExit('### %s: %s -- NOTHING WRITTEN' % (item, 'FINDINGS.md NOT CLEAN AGAINST HEAD' if not P['clean'] else 'THE CURRENT DIFFERS FROM THE AGENDA'))
    new = dict((k, n) for (k, _kd, _o, n, _d) in P['plan'])
    after = put_lines(P['data'], new)
    nb, na, bad = check_write(P['data'], after, new)
    print('  THE LINE COUNT: before %d ; after %d ; %s ; lines differing beyond the item`s: %s' % (nb, na, 'EQUAL' if nb == na else 'UNEQUAL', bad or 'none'))
    if nb != na or bad:
        raise SystemExit('### %s: NOT ONE LINE FOR ONE LINE -- NOTHING WRITTEN' % item)
    if not write:
        print('  DRY: nothing written')
        return
    at = stamp()
    with open(FPATH + '.tmp', 'wb') as f:
        f.write(after)
    os.replace(FPATH + '.tmp', FPATH)
    back = open(FPATH, 'rb').read()
    nb2, na2, bad2 = check_write(P['data'], back, new)
    print('  WRITTEN %s at %s ; read back: count %d -> %d, differing beyond the item`s %s, bytes %s' % (FREL, at, nb2, na2, bad2 or 'none',
                                                                                                  'EQUAL to the composed' if back == after else 'DIFFER'))
    if back != after or bad2 or nb2 != na2:
        raise SystemExit('### %s: THE READ-BACK DIFFERS -- restore FINDINGS.md through the one-call tool' % item)
    R = rows()
    R[item] = dict(form=FORMS[item], word_at=WORD_AT, word_cite=WORD_CITE, label=LABELS[item], state='WRITTEN, the commit through the one-call tool',
                   findings_head=P['head'], written_at=at, count_before=nb, count_after=na, sha_before=bdigest(P['data']), sha_after=bdigest(after),
                   lines=[dict(line=k, kind=kd, old_digest=digest(o), new_digest=digest(n), old_chars=len(o), new_chars=len(n),
                               draft_cite='data/b754_ferry.txt :%d' % [x for x in AG.FERRY if x[0] == item][0][1], agenda='AGREES')
                          for (k, kd, o, n, _d) in P['plan']],
                   note='the draft`s date 2026-11-12 stands as the ruling wrote it ((R364)(5): the seat changes no word); written %s' % at[:10],
                   confirm=None)
    bank(R)
    print('  then: `commit.py pp add FINDINGS.md`, its commit, then `%s confirm %s`' % (SELF, item.strip('[]')))


def item_confirm(item):
    R = rows()
    r = R.get(item)
    if not r or r.get('confirm'):
        raise SystemExit('### %s: %s -- NOTHING DONE' % (item, 'NO ROW' if not r else 'CONFIRMED ALREADY'))
    head = AG.git(PP, 'rev-parse', 'HEAD').strip()
    files = AG.git(PP, 'show', '--format=', '--name-only', 'HEAD').strip()
    num = AG.git(PP, 'show', '--format=', '--numstat', 'HEAD').strip()
    F = AG.lines(PP, 'HEAD', FREL)
    have = [digest(F[x['line'] - 1]) == x['new_digest'] for x in r['lines']]
    n = len(r['lines'])
    ok = files == FREL and num.split()[:2] == [str(n), str(n)] and all(have) and head != r['findings_head']
    print('### %s CONFIRM: PLACE-papers HEAD %s ; files %s ; numstat %s ; the row`s lines at HEAD %s ; %s' % (
        item, head[:8], files, num.split()[:2], have, 'AS WANTED' if ok else 'NOT AS WANTED'))
    if not ok:
        raise SystemExit('### %s: THE COMMIT DOES NOT CARRY THE ROW -- NOTHING WRITTEN' % item)
    r['confirm'] = 'PLACE-papers %s, FINDINGS.md alone, %d line(s) for %d' % (head[:8], n, n)
    r['state'] = 'PASS'
    bank(R)


# ---------------------------------------------------------------- [A5]
def a5_cap(kind):
    return os.path.join(CAP, 'A5_%s.json' % kind)


def a5_save(kind, rec):
    os.makedirs(CAP, exist_ok=True)
    with io.open(a5_cap(kind) + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, indent=1) + NL)
    os.replace(a5_cap(kind) + '.tmp', a5_cap(kind))


def a5_load(kind):
    p = a5_cap(kind)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else None


def a5(step):
    if not controls():
        raise SystemExit('### THE CONTROLS NOT AS WANTED -- NOTHING DONE')
    if not word_ok('[A5]', the_word()):
        raise SystemExit('### [A5]: THE WORD AT %s DOES NOT READ PASSED -- NOTHING DONE' % WORD_CITE)
    if '[A5]' in rows():
        raise SystemExit('### [A5] HAS ITS ROW ALREADY -- NOTHING DONE')
    d = a5_draft(AG.ferry_lines())
    A = AG.git(RELAY, 'show', 'HEAD:data/%s_agenda.txt' % ACT).replace('\r', '').split(NL)
    _cur, a5c = agenda_current(A)
    today = stamp()[:10]
    gh = ['gh', 'repo', 'view', '--json', 'description', '-q', '.description']
    if step == 'read':
        t0 = stamp()
        rc, out, err = run(gh, cwd=PP)
        a5_save('read', dict(at=t0, rc=rc, out=out, err=err[:300]))
        print('%s READ PLACE-papers description: rc %d, %d characters ; the agenda`s CURRENT (%s) %s' % (t0, rc, len(out), a5c[0],
                                                                                                         'EQUAL' if out == a5c[1] else 'DIFFERS'))
        return
    if step == 'write':
        r = a5_load('read')
        if not r or r['rc'] or r['at'][:10] != today or r['out'] != a5c[1]:
            raise SystemExit('### [A5]: NO READ OF TODAY EQUAL TO THE AGENDA`S CURRENT (%s) -- NOTHING WRITTEN' % (r and (r['at'], r['rc'], r['out'] == a5c[1])))
        if a5_load('write') and a5_load('write')['at'][:10] == today:
            raise SystemExit('### [A5]: WRITTEN ALREADY TODAY (%s) -- read it back' % a5_load('write')['at'])
        t0 = stamp()
        rc, out, err = run(['gh', 'repo', 'edit', '--description', d], cwd=PP)
        a5_save('write', dict(at=t0, rc=rc, out=out[:300], err=err[:300], draft_digest=digest(d)))
        print('%s WRITE PLACE-papers description by gh repo edit: rc %d%s ; the draft %d characters, digest %s' % (t0, rc, (' ; ' + err[:200]) if rc else '',
                                                                                                                  len(d), digest(d)))
        return
    if step == 'back':
        w, r = a5_load('write'), a5_load('read')
        if not w or w['rc']:
            raise SystemExit('### [A5]: NO WRITE TO READ BACK -- NOTHING DONE')
        t0 = stamp()
        rc, out, err = run(gh, cwd=PP)
        a5_save('back', dict(at=t0, rc=rc, out=out, err=err[:300]))
        eq = rc == 0 and out == d
        print('%s READ BACK PLACE-papers description: rc %d, %d characters ; the draft %s' % (t0, rc, len(out), 'EQUAL' if eq else 'DIFFERS'))
        if not eq:
            raise SystemExit('### [A5]: THE READ-BACK DIFFERS -- no row banked')
        R = rows()
        R['[A5]'] = dict(form='passed', word_at=WORD_AT, word_cite=WORD_CITE, label=LABELS['[A4]'], state='PASS',
                         read='by gh %s, digest %s, %d characters, the agenda`s CURRENT (by gh %s) EQUAL' % (r['at'], digest(r['out']), len(r['out']), a5c[0]),
                         compared='EQUAL', draft='data/b754_ferry.txt :24, digest %s, %d characters' % (digest(d), len(d)),
                         written_at=w['at'], confirm='gh read back %s, equal' % t0, findings_head=None)
        bank(R)
        return
    raise SystemExit('usage: %s a5 <read|write|back>' % SELF)


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    cmd = argv[0]
    if cmd == 'control':
        sys.exit(0 if controls() else 1)
    if cmd in ('dry', 'write', 'confirm') and len(argv) == 2 and ('[%s]' % argv[1].strip('[]')) in SPEC:
        item = '[%s]' % argv[1].strip('[]')
        if cmd == 'confirm':
            return item_confirm(item)
        return item_write(item, cmd == 'write')
    if cmd == 'a5' and len(argv) == 2:
        return a5(argv[1])
    raise SystemExit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
