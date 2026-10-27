# -*- coding: utf-8 -*-
"""b716_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R326)(2): b715's events after its seal (relay data/b715_events.txt, eleven starting
lines) and b715's seventeen defects (relay data/b715_defects.txt, (a)-(q)), answered by one generated FINDINGS entry in b678's corrigendum
form, in the banks' words, every item carrying a column NEW or REPEAT with the act and letter of its class. Nine events are lettered as
defects, each with its owner, (r)-(z) after b715's seventeen letters, the letters from tools/act_letters.py (the one lettering the suite
imports too); two are entered as records, unlettered. Each of b715's defects where the hook refused the call is marked REFUSED BY THE HOOK
(read from its head), and the repeat fraction is printed with and without them. Each lettered item names the repair of (R326)(3) that
takes it up, by its line in relay data/b716_ferry.txt, or reads "carried" with its reason; the repairs' diffs and two-instance controls
are banked at Component 2 in data/b716_tool_repairs.txt. b715's events bank, its defects bank, its sealed face, its trail record
(PLACE-papers OPEN_TRAILS :16006) and every root-named bank unedited.

### THE NEW OR REPEAT COLUMN: an item is REPEAT where an earlier act's lettered row, or a row of the corrigenda bank (relay
### data/b675_corrigenda.txt, rows (1)-(35)), carries an item of its class; the column names the act, its letter and the bank and line or
### row, and the row's text is read and its needle checked before any write. The evidence set is the corrigenda bank's rows, the defects
### banks of b691-b714 at the lines named, and b715's replay findings (data/b715_replay.txt) -- b715's own defects named their classes by
### earlier acts' pre-seal letters, which the corrigenda bank (post-seal letters alone) does not carry. NEW where none carries one.
### Written whole by the Write tool at b716 in b715's form (tools/b715_corrigendum.py, carried by diff to this path and then rewritten, its
### data b714's); b678's reader `rd` IMPORTED unchanged. Routes: `dry` -> the entry printed through the screens, nothing written; `land` ->
### the entry appended to FINDINGS through b716_record's guarded landing, data/b716_corrigendum.txt (.json). The corrigenda bank's row (36)
### is appended by the seat through the Edit tool from the line this tool prints (ROW). It writes those two banks and the one FINDINGS entry.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion
import b716_worklist as K         # noqa: E402
import b716_record as REC         # noqa: E402  ### the guarded landing, the letters reader
import act_letters as AL          # noqa: E402  ### the one lettering

TITLE = ('## Corrigendum to b715’s record (relay data/b715_events.txt and data/b715_defects.txt): eleven events and seventeen defects, '
         'each NEW or REPEAT, nine events lettered (r)-(z), six defects refused by the hook, under (R326)(2)')
PREV_LETTERS = list('abcdefghijklmnopq')
REFUSED_WANT = list('acefhi')
CORRIGENDA_LAST = 35
# ### the repairs of (R326)(3) by their lines in relay data/b716_ferry.txt
FERRY_LINES = {'3(i)': 12, '3(ii)': 13, '3(iii)': 14, '3(iv)': 15, '3(v)': 16, '3(vi)': 17}
FERRY_NEEDLES = {'3(i)': '(i) AN ARM READS ITS ALLOWANCES FROM THE RULING', '3(ii)': '(ii) THE SEAL COMMITS WHAT IT HASHES',
                 '3(iii)': '(iii) THE VERIFIER READS THE BUILDER', '3(iv)': '(iv) THE ANSWERS ROUTE READS EVERY WORD',
                 '3(v)': '(v) A WORD AFTER A SEALED COMPOSITION', '3(vi)': '(vi) THE ROOT’S REQUIRED BANKS READ AGAINST ITS EXCLUSIONS'}

# ### the classes, each (act, letter, source, line or row, needle): source 'row' reads the corrigenda bank's row; otherwise the path's line
C_B714H = ('b714', 'h', 'data/b714_defects.txt', 42, "(h) THE SEAT'S: ONE COMMAND WITH A PIPE")
C_B714I = ('b714', 'i', 'data/b714_defects.txt', 45, "(i) THE SEAT'S: ONE READ CALL WITH NO LIMIT")
C_B714K = ('b714', 'k', 'data/b714_defects.txt', 54, "(k) THE SEAT'S: ONE READ CALL WITH A LIMIT ABOVE TWO HUNDRED")
C_B714Q = ('b714', 'q', 'data/b714_defects.txt', 94, "(q) THE NAVIGATOR'S: A WORD THAT ASSUMED THE SEAL COULD WITHHOLD AN ARM")
C_B691C = ('b691', 'c', 'data/b691_defects.txt', 19, "(c) THE SEAT'S: TWO GIT WRITES IN ONE MESSAGE")
C_B706F = ('b706', 'f', 'data/b706_defects.txt', 39, "(f) THE SEAT'S: A PREMISE PUT TO THE AUTHOR BEFORE ITS MEASUREMENT")
C_B704G = ('b704', 'g', 'data/b704_defects.txt', 34, "(g) THE NAVIGATOR'S: THE README'S KERNEL LINE CITED AT :160, WHERE IT STANDS AT :162")
C_B712F = ('b712', 'f', 'data/b712_defects.txt', 22, "(f) THE SEAT'S: THE FIRST PROMPT'S ANSWER CHECKED BY THE TOOL AFTER IT WAS ACTED ON")
C_B713E = ('b713', 'e', 'data/b713_defects.txt', 25, "(e) THE SEAT'S: THE STEP BANK OUT OF COMMIT ORDER")
C_B701H = ('b701', 'h', 'row', 18, "lettered (h), THE SEAT'S -- relay data/audit_b701_reg_satisfiable.txt, 219 lines, read with a limit and no offset")
C_B708E = ('b708', 'its unlettered event', 'row', 29, 'G-CLOSING-DRY-STEP on the string "### NO VERDICT LINE"')
C_B710M = ('b710', 'm', 'row', 31, '(m) G-ANSWERS-BEFORE-WRITES`s control, repaired')
C_B714R = ('b714', 'r', 'row', 35, '(r) the entry`s head clause composed against the author`s word')
C_B706M = ('b706', 'm', 'row', 27, "the mirror NOT CLEAN on clause 3 by its roster's 17 retired names ((m), THE NAVIGATOR'S)")
C_F1 = ('b714 and b713', 'F-1', 'data/b715_replay.txt', 80, "F-1 [b714, b713 ; object (5)] THE SEAL'S RECORD NAMES A RELAY HEAD")

HOOK_HELD = ('the hook refused the call before it ran, so the rule held and nothing ran; the refusal bank it wrote is the class b715’s '
             '(R325)(4)(iii) repaired (the standing hook writes to an excluded bank from b715’s Component 3), and (R326)(3) names no repair')
# ### b715's defects: (letter, the head's needle, the owner, the repair's (R326) clause or None, the item's words, the column, the reason where carried)
DEFECTS = (
    ('a', 'TWO COMMANDS WITH A PIPE, REFUSED BY THE HOOK', 'THE SEAT’S', None, 'two commands with a pipe', C_B714H, HOOK_HELD),
    ('b', 'TWO GIT WRITES IN ONE MESSAGE', 'THE SEAT’S', None, 'two git writes in one message', C_B691C,
     'the seat’s sequencing, sent by no tool; (R326)(3) names no repair, and each stage and commit since stands in its own message'),
    ('c', 'A READ WITH NO LIMIT, REFUSED BY THE HOOK', 'THE SEAT’S', None, 'a read with no limit', C_B714I, HOOK_HELD),
    ('d', 'A TOOLSET RULED WITHOUT ITS MEASUREMENT', 'THE NAVIGATOR’S', None, 'a toolset ruled without its measurement', C_B706F,
     'the author’s word (1) at b715 took the core under conditions (a)-(d) and withdrew (R325)(3)(v)’s clause for the coverage table; no '
     'tool is repaired for a ruling'),
    ('e', 'A READ WITH A LIMIT ABOVE TWO HUNDRED, REFUSED', 'THE SEAT’S', None, 'a read with a limit above two hundred', C_B714K, HOOK_HELD),
    ('f', 'ONE COMMAND WITH A PIPE, REFUSED', 'THE SEAT’S', None, 'one command with a pipe', C_B714H, HOOK_HELD),
    ('g', 'A TIME WRITTEN WITHOUT READING THE CLOCK', 'THE SEAT’S', None, 'a time written without reading the clock', None,
     'both lines corrected by the Edit tool before any commit carried them; no tool writes the time, and (R326)(3) names no repair'),
    ('h', 'A READ WITH A LIMIT ABOVE TWO HUNDRED, REFUSED', 'THE SEAT’S', None, 'a read with a limit above two hundred', C_B714K, HOOK_HELD),
    ('i', 'A READ WITH NO LIMIT, REFUSED', 'THE SEAT’S', None, 'a read with no limit', C_B714I, HOOK_HELD),
    ('j', 'THE CARRIED ROOT EXCLUSION READ A REQUIRED BANK AS EXCLUDED', 'THE SEAT’S', '3(vi)',
     'the carried root exclusion reading a required bank as excluded', None, None),
    ('k', 'THE READ-FIRST BANK CITES THE FERRY', 'THE SEAT’S', None, 'the read-first bank citing the ferry’s list at the wrong line', C_B704G,
     'the bank stands unedited, its row naming the line; the line is the seat’s, written by no tool, and (R326)(3) names no repair'),
    ('l', 'THE AUTHOR\'S TWO WORDS ACTED ON BEFORE THEIR TOOL CHECK', 'THE SEAT’S', None, 'the author’s two words acted on before their tool check',
     C_B712F, 'the order of check before act is the seat’s; (R326)(3)(iv) repairs the reading of the words by their heads and not that order'),
    ('m', 'FOURTEEN READS OF FILES OF TWO HUNDRED LINES OR MORE GIVEN ONE BOUND', 'THE SEAT’S', None,
     'fourteen reads of files of two hundred lines or more given one bound', C_B701H,
     'the hook reads the limit alone (row (77)) and the read bank’s arm finds the rest; (R326)(3) names no repair'),
    ('n', 'THE STEP-ZERO LISTING WRITTEN OUT OF THE HOUSE FORM', 'THE SEAT’S', None, 'the step-zero listing written out of the house form', None,
     'restated in the house form before b715’s lock; (R326)(3) names no repair'),
    ('o', 'THE PINS TOOL WIDENED WITHOUT READING THE LOCK GATE', 'THE SEAT’S', None, 'the pins tool widened without reading the lock gate that reads it',
     None, 'repaired at b715 by the pins tool’s gate route; (R326)(3) names no further repair'),
    ('p', 'THE WIDENED CENSUS NAMED PRIVATE REPOSITORIES', 'THE SEAT’S', None, 'the widened census naming private repositories and reading a fork as a kernel',
     None, 'the regenerated census (data/b715_pins_census.txt) carries one PRIVATE row, PLACE-papers (:27), of b714’s four-repository roster '
     'and no fork; b715’s events (5) and (11), entered here as records, stand for the author’s word on the names the history and the closing carry'),
    ('q', 'AN ARM READING A ROW BY A READER OTHER THAN THE ONE THAT PRINTED IT', 'THE SEAT’S', None,
     'an arm reading a row by a reader other than the one that printed it', C_B708E,
     'repaired at b715 (the arm’s pattern the closing’s own); (R326)(3) names no further repair'),
)
# ### b715's events lettered: (events line, the head's needle, the owner, the repair's clause or None, the item's words, the column, the reason where carried)
LETTERED = (
    (3, 'THE SEAL RECORDED A RELAY HEAD THAT DOES NOT CARRY TWO TOOLS IT SEALED', 'THE SEAL TOOL’S AND THE SEAT’S', '3(ii)',
     'the seal recording a relay head that does not carry two tools it sealed', C_F1, None),
    (7, "THE NAVIGATOR'S: WORD (3)(c) READ ONE SHARED MATHLIB REV", 'THE NAVIGATOR’S', None, 'word (3)(c) reading one shared Mathlib rev', C_B714Q,
     'ruled at b715’s root by the author’s word (b), each kernel read at its own manifest’s rev; no tool is repaired for a ruling'),
    (9, "THE ANSWERS ROUTE'S WORD MATCHER MISSED THE AUTHOR'S WORD (2)", 'THE ANSWERS ROUTE’S', '3(iv)',
     'the answers route’s matcher missing a word sent in an option’s notes', None, None),
    (11, "THE ENTRY'S CARRIED CLAUSE STANDS SUPERSEDED BY THE ROOT WORD (b)", 'THE RECORD TOOL’S', '3(v)',
     'the entry’s carried clause standing superseded by the root word', C_B714R, None),
    (27, "THE TRAIL'S TWO CLAUSES STAND STALE AGAINST THE ROOT WORD", 'THE RECORD TOOL’S', '3(v)',
     'the trail’s two clauses standing stale against the root word', C_B714R, None),
    (33, "THE SEAT'S: TWO PUSH BRANCHES DELETED OUTSIDE (R325)(9)'S LIST", 'THE SEAT’S', '3(i)',
     'two push branches deleted outside the ruling’s list', None, None),
    (39, "G-ANSWERS-BEFORE-WRITES CANNOT PASS ON THIS ACT'S ANSWERS BANK", 'THE ARM’S', '3(i)',
     'G-ANSWERS-BEFORE-WRITES counting one prompt where the act put four', C_B710M, None),
    (45, "THE SEAT'S: TWO COMMITS WITHOUT A STEP ROW UNTIL THE POST-PUSH SUITE", 'THE SEAT’S', None,
     'two commits without a step row until the post-push suite', C_B713E,
     'the rows added by the step route naming each commit; (R326)(3) names no repair, and this act enters a step’s row after its commits'),
    (52, "THE MIRROR'S VERIFICATION NOT CLEAN AT CLAUSE 3", 'THE VERIFIER’S, AND THE SEAT’S PLANNING MISS', '3(iii)',
     'the mirror’s verification NOT CLEAN at clause 3 by the verifier’s base roster', C_B706M, None),
)
# ### the records: (events line, the head's needle, the words, the column)
RECORDS = (
    (18, "THE PRE-ROOT PUSH CARRIES 4660aea0'S FIRST CENSUS", 'the pre-root push carrying the first census’s blob in the history', None),
    (64, "THE CLOSING'S BRANCH LISTING NAMES ONE PRIVATE REPOSITORY", 'the closing’s branch listing naming one private repository', None),
)
ROW = ('  (36) b715\'s record (relay data/b715_events.txt, eleven starting lines, and data/b715_defects.txt, (a)-(q)): b715`s seventeen\n'
       '      defects each NEW or REPEAT, (a), (c), (e), (f), (h), (i) REFUSED BY THE HOOK, (j) by (R326)(3)(vi), the rest carried; the events\n'
       '      lettered (r) the seal recording a relay head that does not carry two tools it sealed, the seal tool`s and the seat`s, by (3)(ii);\n'
       '      (s) word (3)(c) reading one shared Mathlib rev, the navigator`s, carried; (t) the answers route`s matcher missing a word sent in an\n'
       '      option`s notes, the answers route`s, by (3)(iv); (u) the entry`s carried clause and (v) the trail`s two clauses standing against\n'
       '      the root word, the record tool`s, by (3)(v); (w) two push branches deleted outside the ruling`s list, the seat`s, and (x)\n'
       '      G-ANSWERS-BEFORE-WRITES counting one prompt where the act put four, the arm`s, both by (3)(i); (y) two commits without a step row,\n'
       '      the seat`s, carried; (z) the mirror`s verification NOT CLEAN at clause 3, the verifier`s, by (3)(iii). Records, unlettered: :18,\n'
       '      :64. NEW OR REPEAT: REPEAT %s ; THE REPEAT FRACTION %s.\n'
       '      THE CORRECTION: the standing toolset at v1.1.0 of (R326)(3), its diffs and controls data/b716_tool_repairs.txt. The generated\n'
       '      corrigendum entry stands at FINDINGS.md :%s.')


def _flat(t):
    return re.sub(r'\s+', ' ', t)


def _corrigenda_rows():
    """the corrigenda bank's rows by number, each row's lines joined and its whitespace collapsed."""
    rows, cur = {}, None
    for l in C78.rd(os.path.join(D, 'b675_corrigenda.txt')).replace(chr(13), '').split(NL):
        m = re.match(r'^  \((\d+)\) ', l)
        if m:
            cur = int(m.group(1))
            rows[cur] = l
        elif cur is not None and l.startswith('      '):
            rows[cur] += ' ' + l.strip()
        elif not l.strip() or l.startswith('###'):
            cur = None
    return dict((k, _flat(v)) for k, v in rows.items())


def _col_ok(c, cr):
    if not c:
        return True
    _act, _letter, src, where, needle = c
    if src == 'row':
        return _flat(needle) in cr.get(where, '')
    L = C78.rd(os.path.join(ROOT, src)).replace(chr(13), '').split(NL)
    return len(L) >= where and needle in L[where - 1]


def _refused(heads):
    return [x for x in PREV_LETTERS if 'REFUSED' in heads.get(x, '')]


def compose():
    ev = C78.rd(os.path.join(D, 'b715_events.txt')).replace(chr(13), '').split(NL)
    starts = [i for i, l in enumerate(ev, 1) if re.match(r'^\(\d+\) ', l)]
    want_starts = sorted([x[0] for x in LETTERED] + [x[0] for x in RECORDS])
    heads = dict((n, re.sub(r'^\(\d+\) ', '', ev[n - 1])) for n in starts)
    miss_heads = [x[0] for x in LETTERED if not heads.get(x[0], '').startswith(x[1])] + \
                 [x[0] for x in RECORDS if not heads.get(x[0], '').startswith(x[1])]
    dt = C78.rd(os.path.join(D, 'b715_defects.txt'))
    rows = REC.letters_of(dt)
    prev = [re.match(r"\(([a-z]'?)\)", x).group(1) for x in rows]
    dheads = dict((re.match(r"\(([a-z]'?)\)", x).group(1), x) for x in rows)
    miss_d = [d[0] for d in DEFECTS if d[1] not in dheads.get(d[0], '')]
    refused = _refused(dheads)
    letters = AL.after(prev, len(LETTERED)) if prev == PREV_LETTERS else []
    cr = _corrigenda_rows()
    cols = [x[5] for x in DEFECTS] + [x[5] for x in LETTERED] + [x[3] for x in RECORDS]
    bad_cols = [(c[0], c[1], c[2], c[3]) for c in cols if not _col_ok(c, cr)]
    f16 = C78.rd(os.path.join(D, 'b716_ferry.txt')).split(NL)
    ferry_ok = [k for k, n in FERRY_LINES.items() if not (len(f16) >= n and f16[n - 1].startswith(FERRY_NEEDLES[k]))]
    s = dict(starts=starts, heads=heads, prev=prev, letters=letters, refused=refused, corrigenda_last=max(cr) if cr else 0)
    bad = [k for k, v in (('the eleven starting lines', starts == want_starts), ('each event`s head', not miss_heads),
                          ('b715`s seventeen letters', prev == PREV_LETTERS), ('each defect`s head', not miss_d),
                          ('the six refused by the hook', refused == REFUSED_WANT), ('the nine letters after them', letters == list('rstuvwxyz')),
                          ('each REPEAT`s line or row and needle', not bad_cols), ('each repair`s ferry line', not ferry_ok),
                          ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, max(cr) == CORRIGENDA_LAST if cr else False)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (event heads missed %s ; defect heads missed %s ; refused %s ; columns %s ; '
                 'starts %s ; ferry %s)' % (bad, miss_heads, miss_d, refused, bad_cols, starts, ferry_ok))
    return s


def _column(c):
    if not c:
        return 'NEW (no row of the evidence set carries its class)'
    act, letter, src, where, _n = c
    what = ('%s (%s)' % (act, AL.canon(letter))) if re.match(r"^[a-z]'?$", letter) else ('%s, %s' % (act, letter))
    place = ('relay data/b675_corrigenda.txt row (%d)' % where) if src == 'row' else ('relay %s :%d' % (src, where))
    return 'REPEAT of %s, %s' % (what, place)


def fraction():
    """(REPEAT, all) with the refused; (REPEAT, all) without them; (REPEAT, all) among the lettered (b715's defects and the events lettered)."""
    items = [(d[0] in REFUSED_WANT, bool(d[5]), True) for d in DEFECTS] + [(False, bool(x[5]), True) for x in LETTERED] + \
            [(False, bool(x[3]), False) for x in RECORDS]
    ra, na = sum(1 for _r, c, _l in items if c), len(items)
    rw, nw = sum(1 for r, c, _l in items if c and not r), sum(1 for r, _c, _l in items if not r)
    rl, nl = sum(1 for _r, c, l in items if c and l), sum(1 for _r, _c, l in items if l)
    return ra, na, rw, nw, rl, nl


def fraction_words():
    ra, na, rw, nw, rl, nl = fraction()
    return ('%d of %d (%.2f) with the six refused by the hook ; %d of %d (%.2f) without them ; among the lettered %d of %d (%.2f)' % (
        ra, na, ra / float(na), rw, nw, rw / float(nw), rl, nl, rl / float(nl)))


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _repair_words(r, why):
    if not r:
        return 'CARRIED: %s.' % why
    return ('TAKEN UP BY (R326)(%s (relay data/b716_ferry.txt :%d); its diff and its two-instance control in relay '
            'data/b716_tool_repairs.txt.' % (r.replace('(', ')(', 1), FERRY_LINES[r]))


def _entry_lines(s):
    L = [TITLE, '',
         ('b715’s defects bank (relay data/b715_defects.txt) carries seventeen letters (a)-(q), and its events bank (relay '
          'data/b715_events.txt) eleven starting lines (:%s), entered after its seal and not lettered, for this act’s corrigendum under '
          'standing clauses v2 row (52). Each item carries NEW or REPEAT, a REPEAT naming the earlier act and letter of its class and the '
          'bank line or the row of relay data/b675_corrigenda.txt that records it; the evidence set is that bank’s rows (1)-(%d), the '
          'defects banks of b691-b714 at the lines named, and b715’s replay findings. The six defects whose heads read a refusal, (%s), are '
          'marked REFUSED BY THE HOOK: each stands as the seat’s attempt, and the record shows the rule held. Nine events are lettered '
          'as defects, each with its owner, (r)-(z) after b715’s letters, by relay tools/act_letters.py; two are entered as records. '
          'Each lettered item names the repair of (R326)(3) that takes it up, or reads CARRIED with its reason. b715’s events and defects '
          'banks, its face, its trail record (PLACE-papers OPEN_TRAILS :%d) and every root-named bank are not edited.' % (
              ', :'.join(str(n) for n in s['starts']), s['corrigenda_last'], ', '.join(s['refused']), K.B711_TRAIL)), '',
         '**b715’s defects:**', '']
    for (x, _h, own, r, words, col, why) in DEFECTS:
        mark = ' REFUSED BY THE HOOK.' if x in s['refused'] else ''
        L += ['**(%s) %s** (relay data/b715_defects.txt; %s; %s).%s %s' % (x, words[0].upper() + words[1:], own, _column(col), mark,
                                                                          _repair_words(r, why)), '']
    L += ['**b715’s events, lettered:**', '']
    for (n, _h, own, r, words, col, why), x in zip(LETTERED, s['letters']):
        L += ['**(%s) %s** (relay data/b715_events.txt :%d; %s; %s). %s' % (x, words[0].upper() + words[1:], n, own, _column(col),
                                                                            _repair_words(r, why)), '']
    L += ['**Records, unlettered:** ' + '; '.join(':%d %s (%s)' % (n, w, _column(c)) for n, _h, w, c in RECORDS) +
          ' (relay data/b715_events.txt), each carried for the author’s word.', '',
          '**The repeat fraction:** REPEAT %s.' % fraction_words(), '',
          'The sealed face, the events and defects banks, the trail record and every root-named bank are not edited -- this entry is their '
          'correction. Nothing here proves RH or GRH.', '',
          ('*Filed at b716 on the author’s ruling `(R326)`(2): generated by relay `tools/b716_corrigendum.py`, written whole at b716 in the '
           'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), its letters from relay `tools/act_letters.py`, '
           'banked as relay `data/b716_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (36); it answers b715’s '
           'events and defects.*')]
    return L


def bank_lines(s, landed_line=None):
    ra, na, rw, nw, rl, nl = fraction()
    L = ['b716 -- THE CORRIGENDUM ENTRY FOR b715`S EVENTS AND DEFECTS, (R326)(2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the starting lines :%s ; b715`s letters %s ; refused by the hook %s ; the letters after them %s ;' % (
             ', :'.join(str(n) for n in s['starts']), ''.join(s['prev']), ''.join(s['refused']), ''.join(s['letters'])),
         '### every REPEAT`s line or row read and its needle found ; the repairs` ferry lines :12-:17 ; the corrigenda bank`s last row (%d).' % (
             s['corrigenda_last']), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: b715`S DEFECTS %d (REFUSED BY THE HOOK %d) ; EVENTS LETTERED %d (r)-(z) ; RECORDS %d ; REPAIRS NAMED %d, CARRIED %d ; '
              'REPEAT %d OF %d WITH THE REFUSED, %d OF %d WITHOUT ; THE FACE, THE EVENTS AND DEFECTS BANKS, THE TRAIL AND THE ROOT-NAMED BANKS '
              'UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                  na, len(DEFECTS), len(s['refused']), len(LETTERED), len(RECORDS),
                  sum(1 for d in DEFECTS if d[3]) + sum(1 for x in LETTERED if x[3]),
                  sum(1 for d in DEFECTS if not d[3]) + sum(1 for x in LETTERED if not x[3]), ra, na, rw, nw,
                  landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b716', p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def _row_text(ln):
    ra, na, rw, nw, rl, nl = fraction()
    return ROW % ('%d of %d' % (ra, na), '%.2f, without the six refused by the hook %d of %d (%.2f), among the lettered %d of %d' % (
        ra / float(na), rw, nw, rw / float(nw), rl, nl), ln)


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(_row_text('NOT YET WRITTEN'))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b716_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b716_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b716_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE,
             defects=[dict(letter=x, owner=o, refused=(x in s['refused']), repair=r, ferry_line=FERRY_LINES.get(r) if r else None,
                           column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:4]) if c else None), carried=(why if not r else None))
                      for (x, _h, o, r, _w, c, why) in DEFECTS],
             lettered=[dict(letter=x, line=n, owner=o, repair=r, ferry_line=FERRY_LINES.get(r) if r else None,
                            column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:4]) if c else None), carried=(why if not r else None))
                       for (n, _h, o, r, _w, c, why), x in zip(LETTERED, s['letters'])],
             records=[dict(line=n, column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:4]) if c else None)) for n, _h, _w, c in RECORDS],
             starts=s['starts'], refused=s['refused'], row=36, fraction=list(fraction()))
    _put('b716_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(_row_text(ln))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
