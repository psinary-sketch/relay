# -*- coding: utf-8 -*-
"""b712_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R322)(2): b711's post-seal items -- the five letters entered in its defects bank after its
seal ((g)-(k); the seal's record, relay data/b711_seal_hashes.json, its head 71f1c2a0, carries (a)-(f)) and the two unlettered events of its
suite after the seal (the three trail arms after the late letter; G-ANSWERS-BEFORE-WRITES's positive control that cannot fire) -- answered by one
generated FINDINGS entry in b678's corrigendum form, in the banks' words. Under standing clauses v2 row (52) ((R322)(2)(i)) "the next act's
corrigendum letters it": the five keep b711's letters, the two events are lettered (l) and (m) in this entry; b711's defects bank, its sealed
face (relay data/b711_registration_2026-10-24.txt), its trail record (PLACE-papers OPEN_TRAILS :15808) and every root-named bank unedited.

### Written whole by the Write tool at b712, its items rewritten for b711's record (b708, b711 wrote theirs the same way; the carry's spans,
### data/b712_carry_corrigendum.txt, read by offset and limit). b678's reader `rd` IMPORTED unchanged; its form -- one generated entry, each
### item quoted with its place, the corrected reading and its source, the figures read from their banks and checked before any write, `dry` then
### `land`. Every figure is read, none typed:
###   the letters: data/b711_defects.txt by tools/b712_record.py letters_of; the letters at the seal by letters_at_seal('b711'); each row's line;
###   the two events: their heads beneath EVENTS, UNLETTERED, by line;
###   the failing six: data/b711_checks_postpush.txt's LIVE FAILING list; the declared one: the face's declaration line; the positive control
###   passing: the act part's POSITIVE-CONTROL PASSES list;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15808, its letters read;
###   the repairs: tools/b712_record.py REPAIRS by label, the bank data/b712_tool_repairs.txt carrying each label; the controls
###   data/b712_repair_controls.json by section, its one case NOT AS WANTED (section i) and b712's defect (d) beside it;
###   the supplement: data/b712_independence.txt's verdict line.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b712_record's
### guarded landing, data/b712_corrigendum.txt (.json). The corrigenda bank's row (31) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). It writes those two banks and the one FINDINGS entry.
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
import b712_worklist as K         # noqa: E402
import b712_record as REC         # noqa: E402  ### the guarded landing, the letters readers, REPAIRS

TITLE = ('## Corrigendum to b711’s record after its seal (relay data/b711_defects.txt, data/b711_checks_postpush.txt): five letters after '
         'the seal and two events of its suite, answered under standing clauses v2 row (52)')
POST_LETTERS = list('ghijk')
EVENT_HEADS = (('l', '    THE THREE TRAIL ARMS AFTER THE LATE LETTER (i).'),
               ('m', "    G-ANSWERS-BEFORE-WRITES'S POSITIVE CONTROL CANNOT FIRE."))
FAILING = ['G-ACTROOT-LAST', 'G-READ-RULE-STANDING', 'G-SEALED-AFTER-COMPONENTS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS',
           'G-TRAIL-RESOLVED-EQUAL']
DECLARED_ARM = 'G-READ-RULE-STANDING'
POS_PASSING = ['G-ANSWERS-BEFORE-WRITES']
LABELS = ('(52)', '(53)', '(55)', '(k)', '(i)')
ROW = ('  (31) b711\'s record after its seal (relay data/b711_defects.txt, letters (g)-(k) entered after the seal`s head 71f1c2a0;\n'
       '      data/b711_checks_postpush.txt, LIVE FAILING 6, five beyond the face, one positive control passing): (g) a redirect after the seal, standing;\n'
       '      (h) Independence read by definitions alone, answered by the supplement (data/b712_independence.txt); (i) G-SEALED-AFTER-COMPONENTS\n'
       '      by commit subjects, repaired by the step bank; (j) a root-named bank written after the root, repaired by the membrane; (k) the\n'
       '      head line`s capture names, repaired; (l) the three trail arms after the late letter, repaired by the letters at the seal and NOT\n'
       '      ANSWERED on b711`s banks (b712`s defect (d), for the author`s strike); (m) G-ANSWERS-BEFORE-WRITES`s control, repaired. THE\n'
       '      CORRECTION: relay data/b712_tool_repairs.txt rows (52), (53), (55), (k), (i), their controls data/b712_repair_controls.txt. The\n'
       '      generated corrigendum entry stands at FINDINGS.md :%s.')


def _line_of(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and l.startswith(needle)), 0)


def _row(L, letter):
    """(line, head) of a lettered row: its first line, its head to the first full stop after the owner."""
    n = _line_of(L, '    (%s) ' % letter)
    if not n:
        return 0, ''
    t = L[n - 1].strip()[4:]
    k = t.find('. ')
    return n, (t[:k] if k > 0 else t)


def compose():
    dt = C78.rd(os.path.join(D, 'b711_defects.txt'))
    dl = dt.split(NL)
    letters = [re.match(r'\((\w)\)', x).group(1) for x in REC.letters_of(dt)]
    seal = [re.match(r'\((\w)\)', x).group(1) for x in REC.letters_at_seal('b711')]
    post = [x for x in letters if x not in seal]
    rows = dict((x, _row(dl, x)) for x in post)
    ev_at = _line_of(dl, '### EVENTS, UNLETTERED')
    events = dict((x, _line_of(dl, h, ev_at)) for x, h in EVENT_HEADS)
    pp = C78.rd(os.path.join(D, 'b711_checks_postpush.txt'))
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', pp)
    fails = sorted(x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip())
    mp = re.search(r'### PART act : .*?POSITIVE-CONTROL PASSES 1 \[(.*?)\]', pp)
    pos = sorted(x.strip().strip('"') for x in (mp.group(1) if mp else '').split(',') if x.strip())
    face = ' '.join(C78.rd(os.path.join(ROOT, *K.B710_FACE.split('/'))).split())
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', face)
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    beyond = sorted(a for a in fails if a not in declared)
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    trail = K.B710_TRAIL if ot[K.B710_TRAIL - 1].startswith('### b711') else 0
    dline = next((i + 1 for i in range(trail, min(trail + 60, len(ot))) if ot[i].startswith('**Defects**')), 0) if trail else 0
    tletters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dline - 1]) if dline else []
    rep = dict((r[0], r[1]) for r in REC.REPAIRS)
    tr = C78.rd(os.path.join(D, 'b712_tool_repairs.txt')) if os.path.exists(os.path.join(D, 'b712_tool_repairs.txt')) else ''
    tr_rows = [x for x in LABELS if x in rep and x in tr]
    ctl = REC.jl('b712_repair_controls.json')
    cases = ctl.get('cases') or []
    sec = dict((s, [c for c in cases if c.get('section') == s]) for s in ('i', 'ii', 'iv', 'k', 'i/step'))
    nots = [c for c in cases if not c.get('as_wanted')]
    ok_ctl = len(nots) == 1 and nots[0].get('section') == 'i' and all(c.get('as_wanted') for s in ('ii', 'iv', 'k', 'i/step') for c in sec[s]) \
        and all(sec[s] for s in sec)
    b11 = C78.rd(os.path.join(D, 'b712_defects.txt')).split(NL)
    d11 = _line_of(b11, "    (d) THE NAVIGATOR'S, FOR THE AUTHOR'S STRIKE")
    ind = C78.rd(os.path.join(D, 'b712_independence.txt')).split(NL)
    ind_n = _line_of(ind, '### ### **DECLARATIONS READ ')
    if ind_n:
        ind[ind_n - 1] = ind[ind_n - 1].replace('`', '’')   # ### the bank's backtick possessive, as the entry's apostrophe
    s = dict(letters=letters, seal=seal, post=post, rows=rows, events=events, fails=fails, pos=pos, declared=declared, beyond=beyond,
             trail=trail, defects_line=dline, tletters=tletters, tr_rows=tr_rows, ctl=ok_ctl, n_cases=len(cases), d11=d11, ind_n=ind_n,
             ind_v=ind[ind_n - 1] if ind_n else '')
    bad = [k for k, v in (('the letters after the seal', post == POST_LETTERS), ('the seal`s letters', seal == list('abcdef')),
                          ('every post-seal row', all(rows[x][0] for x in post)), ('the two events', all(events.values()) and ev_at),
                          ('the failing six', fails == FAILING), ('the declared arm', declared == [DECLARED_ARM]),
                          ('the positive control passing', pos == POS_PASSING), ('the trail head', trail),
                          ('the Defects line', tletters == list('abcdefgh')), ('the repair rows banked', tr_rows == list(LABELS)),
                          ('the controls', ok_ctl), ('b712`s defect (d)', d11), ('the supplement`s verdict', ind_n)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (%r)' % (bad, s))
    return s


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _entry_lines(s):
    r = s['rows']
    return [
        TITLE, '',
        ('b711’s seal (2026-10-24T23:50:34Z, relay data/b711_seal_hashes.json, its relay head 71f1c2a0) recorded its defects bank with the '
         'letters (a)-(f); (g)-(k) were lettered after it (relay data/b711_defects.txt :%d, :%d, :%d, :%d, :%d), and its pre-push and post-push '
         'suites read six arms failing (data/b711_checks_postpush.txt), one declared on its face by name (%s), and one positive control '
         'passing (%s). Under standing clauses v2 row (52), (R322)(2)(i), a finding after the seal is the next act’s corrigendum’s to letter: '
         'the five keep the letters b711’s bank gave them, and the two unlettered events of its suite (data/b711_defects.txt :%d, :%d) are '
         'lettered here (l) and (m). b711’s defects bank, its face, its trail record (PLACE-papers OPEN_TRAILS :%d, its Defects line :%d '
         'reading (a)-(h)) and every root-named bank are not edited.' % (
             r['g'][0], r['h'][0], r['i'][0], r['j'][0], r['k'][0], DECLARED_ARM, POS_PASSING[0], s['events']['l'], s['events']['m'],
             s['trail'], s['defects_line'])), '',
        ('**(g) %s** (relay data/b711_defects.txt :%d). A `2>/dev/null` inside a command substitution after the seal, uncounted by the '
         'command bank’s redirect reader. It stands as lettered: standing clauses v2 row (14) is unchanged, and (R322) orders no repair of '
         'the reader; nothing was written by the command.' % (r['g'][1], r['g'][0])), '',
        ('**(h) %s** (relay data/b711_defects.txt :%d). Answered by the Independence supplement at b712’s step zero (relay '
         'data/b712_independence.txt :%d, “%s”), the author’s order W-ORD-READING5-INDEPENDENCE; reading 5’s sealed bank and b711’s '
         'entry are not edited, and the row is restated at b712’s entry.' % (r['h'][1], r['h'][0], s['ind_n'], s['ind_v'].strip('#* ').rstrip('.*'))), '',
        ('**(i) %s** (relay data/b711_defects.txt :%d). G-SEALED-AFTER-COMPONENTS read the act’s commits by their subjects. THE '
         'CORRECTION: the arm reads the act’s step bank (data/b712_steps.json, each commit’s phase named when it is made), relay '
         'data/b712_tool_repairs.txt row (i), its controls data/b712_repair_controls.txt section i/step (b711’s subject reading failing on '
         '7c07c5d4 and df2dd7c0; the step bank’s reading passing; a post-lock commit given a component phase failing).' % (r['i'][1], r['i'][0])), '',
        ('**(j) %s** (relay data/b711_defects.txt :%d). G-ACTROOT-LAST reads every root-named bank’s write time against the root’s '
         '(tools/b711_checks.py root_last_ok); data/b711_locate.txt, restored to its blob, kept a write time after the root’s. THE CORRECTION: the membrane, standing clauses v2 row (53) -- every tool that writes a named bank refuses '
         'once the act’s root is appended (tools/act_membrane.py), locator and read calls write nothing -- relay data/b712_tool_repairs.txt '
         'row (53), its controls section ii.' % (r['j'][1], r['j'][0])), '',
        ('**(k) %s** (relay data/b711_defects.txt :%d). THE CORRECTION: the closing’s head-line builder reads each repository’s record '
         'commit from the act’s last push capture and sends a capture-name failure to the closing’s events section, never the head line '
         '(tools/b712_closing.py head_line, events_section), relay data/b712_tool_repairs.txt row (k), its controls section k (over b711’s '
         'captures the line reads relay 2c200e8d, PLACE-papers df2dd7c, the two name failures in the events section).' % (r['k'][1], r['k'][0])), '',
        ('**(l) THE THREE TRAIL ARMS AFTER THE LATE LETTER** (relay data/b711_defects.txt :%d, an event lettered here). G-TRAIL-LINES-EQUAL-'
         'DEFECTS, G-TRAIL-DEFECTS-EQUAL and G-TRAIL-RESOLVED-EQUAL read the landed trail, (a)-(h), against the bank’s rows after (i)-(k) were '
         'lettered. THE CORRECTION: the three arms read the letters entered before the seal (row (52), relay data/b712_tool_repairs.txt row '
         '(52)). NOT ANSWERED ON b711’S BANKS: the seal’s record carries (a)-(f), so (g) and (h), on b711’s trail, are themselves post-seal, '
         'and the repaired arms read b711’s trail failing -- the one case of %d NOT AS WANTED in data/b712_repair_controls.txt, entered as '
         'b712’s defect (d) (relay data/b712_defects.txt :%d) for the author’s strike; the cut is not moved to make the control pass.' % (
             s['events']['l'], s['n_cases'], s['d11'])), '',
        ('**(m) G-ANSWERS-BEFORE-WRITES’S POSITIVE CONTROL CANNOT FIRE** (relay data/b711_defects.txt :%d, an event lettered here). The '
         'sealed plant appended a prompt the predicate reads as one more, so the mutated copy passed. THE CORRECTION: the plant moves every '
         'mid-act check stamp after the write it governs, and the suite refuses to seal an arm whose mutated copy has not been shown failing '
         '(row (55), relay data/b712_tool_repairs.txt row (55)), its controls section iv (b711’s plant passing, the repaired plant failing).' % (
             s['events']['m'])), '',
        'The sealed face, the defects bank, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH or GRH.', '',
        ('*Filed at b712 on the author’s ruling `(R322)`(2): generated by relay `tools/b712_corrigendum.py`, written whole at b712 in the '
         'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b712_corrigendum.txt`, '
         'the corrigenda bank `data/b675_corrigenda.txt` appended at row (31); it answers b711’s post-seal items.*')]


def bank_lines(s, landed_line=None):
    L = ['b712 -- THE CORRIGENDUM ENTRY FOR b711`S POST-SEAL ITEMS, (R322)(2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the letters %s ; at the seal %s ; after it %s at :%s ; the events (l) :%d, (m) :%d ;' % (
             ''.join(s['letters']), ''.join(s['seal']), ''.join(s['post']), ', :'.join(str(s['rows'][x][0]) for x in s['post']),
             s['events']['l'], s['events']['m']),
         '### failing %s ; declared %s ; beyond the face %s ; positive control passing %s ;' % (s['fails'], s['declared'], s['beyond'], s['pos']),
         '### the trail OPEN_TRAILS :%d, its Defects line :%d letters %s ; the repair rows banked %s ; the controls (%d cases, one NOT AS WANTED in i) %s ;' % (
             s['trail'], s['defects_line'], ''.join(s['tletters']), ' '.join(s['tr_rows']), s['n_cases'], s['ctl']),
         '### b712`s defect (d) data/b712_defects.txt :%d ; the supplement`s verdict data/b712_independence.txt :%d.' % (s['d11'], s['ind_n']), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **SEVEN ITEMS (g)-(m): FIVE REPAIRED OR ANSWERED, (g) STANDING, (l) NOT ANSWERED ON b711`S BANKS (b712`S (d)) ; THE FACE, THE DEFECTS BANK, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
        landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """(R322)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b712', p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(ROW % 'NOT YET WRITTEN')
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b712_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b712_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b712_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=['l', 'm'], post_seal_letters=s['post'],
             events=[h.strip() for _, h in EVENT_HEADS], failing=s['fails'], declared=s['declared'], beyond=s['beyond'], pos=s['pos'],
             trail=s['trail'], defects_line=s['defects_line'], not_answered=['l'], row=31)
    _put('b712_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b712_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
