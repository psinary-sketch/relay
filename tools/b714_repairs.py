# -*- coding: utf-8 -*-
"""b714_repairs.py -- THE FIVE REPAIRS OF (R324)(6), THEIR CONTROLS AND THEIR DIFFS, standing clauses v5 rows (73)-(78).

Each repair's control shows two instances of its class, one from the record and one constructed (row (73)):
  (i)   THE AUTHOR'S WORD AFTER THE SEAL (row (74), tools/act_close.py author_words_section, bank_hashes, hand_edits): from the record, b713's
        word on (b) and (e) (relay data/b713_events.txt :36-:47, its lines as the events bank carries them) banked in a planted
        data/b713_author_words.txt under the scratchpad and printed by the shared section the closing tool imports; constructed, a planted
        tool-written bank hashed at its write, edited, and the edit caught against its hashes (and an unedited bank not);
  (ii)  THE ACT'S FIGURES FROM ONE SOURCE (row (75), act_figures, constant_scan): from the record, b713's banks read Next b714, row 90 and a
        range through 713, and b713's sealed suite tools/b713_checks.py scanned at 713 finding the constants it carried; constructed, the
        figures at run time (this act's step bank) and a planted tool carrying a constant caught while its run-time form passes;
  (iii) EVERY STEP OF THE CLOSE IN THE ORDER (row (76), close_steps at v5 row (79), evidence_ok, close_refuses, declared_failures): from the
        record, b713's order replayed refusing at the seal on both -- [2] READY False and [7] the combined pre-run bank absent -- and b712's
        combined pre-run bank read for its failing list; constructed, planted banks for [1]-[7] passing the seal, then [2] made READY False
        and [7] removed, each refused alone;
  (iv)  THE HOOK (row (77)): its two controls banked at step zero (data/b714_hook_control.txt, data/b714_hook_refusals.txt), read here;
  (v)   ONE LETTERING (row (78), tools/act_letters.py): from the record, b713's corrigendum (data/b713_corrigendum.json) read under it and
        passing, its letters the suite's a′-d′; constructed, a mixed lettering refused.
Routes: `controls` -> data/b714_repair_controls.txt (.json); `diffs` -> data/b714_tool_repairs.txt, each repaired tool's diff against HEAD
and each new shared tool by its sha256. Nothing else written; the planted banks live under the scratchpad.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act_close as AC       # noqa: E402
import act_letters as AL     # noqa: E402
import act_membrane as MEM   # noqa: E402
import b714_worklist as K    # noqa: E402

ACT = 'b714'
REPAIRED = ('tools/act_close.py', 'tools/push_gated.sh', 'tools/b714_record.py')
NEW = ('tools/act_letters.py', 'tools/b714_hook.py', 'tools/b714_corrigendum.py', 'tools/b714_repairs.py')


def rd(p):
    return open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else ''


def _put(name, text):
    import b714_record as REC
    p = os.path.join(D, name)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


def _plant_dir():
    p = os.path.join(K.SP, 'b714_repair_controls_%s' % time.strftime('%Y%m%dT%H%M%SZ', time.gmtime()))
    os.makedirs(p)
    return p


def control_i(sp):
    out = []
    ev = rd(os.path.join(D, 'b713_events.txt')).split(NL)
    word = [l[4:] for l in ev[35:47]]
    dd = os.path.join(sp, 'i_record')
    os.makedirs(dd)
    with open(os.path.join(dd, 'b713_author_words.txt'), 'w', encoding='utf-8', newline='') as fh:
        fh.write(NL.join(word) + NL)
    sec = AC.author_words_section('b713', dd)
    ok1 = (sec[0].startswith(AC.AUTHOR_WORDS_HEAD) and len(sec) == 13 and sec[1] == '    ' + word[0]
           and word[0].startswith('The author’s word on (b) and (e)') and word[-1].endswith('the keystone heads act, is named next.'))
    none = AC.author_words_section('b713', os.path.join(sp, 'i_empty_absent'))
    out.append(('(i)', 'RECORD', 'b713`s word on (b) and (e) (data/b713_events.txt :36-:47, 12 lines) banked as a planted '
                'data/b713_author_words.txt and printed by the shared section: head %r, %d lines, the first %r ; where no bank stands: %r'
                % (sec[0][:60], len(sec) - 1, sec[1][:50], none[0][-14:]), ok1 and none[0].endswith('NONE RECEIVED')))
    dc = os.path.join(sp, 'i_constructed')
    os.makedirs(dc)
    a, b = os.path.join(dc, 'b999_closing.txt'), os.path.join(dc, 'b999_record.txt')
    for p in (a, b):
        with open(p, 'w', encoding='utf-8', newline='') as fh:
            fh.write('a tool-written bank\nits second line\n')
    hs = AC.bank_hashes([a, b])
    with open(a, 'w', encoding='utf-8', newline='') as fh:
        fh.write('a tool-written bank\nits second line, edited by hand\n')
    caught = AC.hand_edits(hs)
    out.append(('(i)', 'CONSTRUCTED', 'two planted tool-written banks hashed at their write, one edited after: hand_edits names %s, the '
                'unedited bank not' % [os.path.basename(p) for p, _w, _n in caught],
                [os.path.basename(p) for p, _w, _n in caught] == ['b999_closing.txt']))
    return out


def control_ii(sp):
    out = []
    roots = rd(os.path.join(D, 'act_roots.txt'))
    f13 = AC.act_figures(act='b713', roots_text=roots)
    ok = (f13['next_act'] == 'b714' and f13['own_row'] == 90 and f13['own_row_stands'] and f13['range_last'] == 713
          and f13['range'][0] == 624 and f13['range'][-1] == 713)
    sc = AC.constant_scan(rd(os.path.join(T, 'b713_checks.py')), 713, forms=('needle', 'range'))
    out.append(('(ii)', 'RECORD', 'b713`s banks: next %s, its row %d (stands %s), the range %d-%d ; b713`s sealed suite tools/b713_checks.py '
                'scanned at 713 for the Next needle and the root range: %d line(s) %s' % (
                    f13['next_act'], f13['own_row'], f13['own_row_stands'], f13['range_first'], f13['range_last'], len(sc), sc[:4]),
                ok and len(sc) >= 1))
    fnow = AC.act_figures()
    planted = ("ACT_FIG = AC.act_figures()\nNEXT = '**Next:** ' + ACT_FIG['next_act']\nfor n in ACT_FIG['range']:\n    pass\n")
    planted_bad = "NEXT = '**Next:** b715'\nfor n in range(624, 714):\n    pass\nACT = 'b714'\n"
    s_ok, s_bad = AC.constant_scan(planted, 714), AC.constant_scan(planted_bad, 714)
    okc = (fnow['act'] == ACT and fnow['next_act'] == 'b715' and fnow['own_row'] == 91 and not fnow['own_row_stands']
           and fnow['range_last'] == 713 and s_ok == [] and [w for _l, w in s_bad] == ['the Next needle', 'the root range', 'the act quoted'])
    out.append(('(ii)', 'CONSTRUCTED', 'at run time: act %s, next %s, its row %d (stands %s), the range %d-%d ; a planted tool reading its '
                'figures at run time scans %s, the same tool with its figures typed scans %s' % (
                    fnow['act'], fnow['next_act'], fnow['own_row'], fnow['own_row_stands'], fnow['range_first'], fnow['range_last'],
                    s_ok, s_bad), okc))
    return out


def _miss(act, dd, present=None):
    quals = AC.step_qualifiers()
    return [k for k, _w, e in AC.close_steps() if k < 8 and AC._evidence(e, act, dd)
            and not AC.evidence_ok(AC._evidence(e, act, dd), quals.get(k, ''), present)]


def control_iii(sp):
    out = []
    steps = AC.close_steps()
    quals = AC.step_qualifiers()
    shape = (len(steps) == 25 and [k for k, _w, _e in steps] == list(range(1, 26)) and quals == {2: 'reading ready True'}
             and steps[6][2] == 'data/<act>_arms_prerun.txt' and steps[1][2] == 'data/<act>_root_banks_dry.json')
    ref13 = AC.close_refuses('b713', 8)
    miss13 = _miss('b713', D)
    out.append(('(iii)', 'RECORD', 'v5 row (79) read as %d steps, the qualifiers %s ; b713`s order replayed at the seal [8]: the lower steps '
                'lacking their evidence %s ; the refusal %r' % (len(steps), quals, miss13, ref13[:150]),
                shape and 2 in miss13 and 7 in miss13 and bool(ref13)))
    fails = AC.declared_failures(rd(os.path.join(D, 'b712_arms_prerun.txt')), waiting=())
    out.append(('(iii)', 'RECORD', 'b712`s combined pre-run bank (data/b712_arms_prerun.txt :13) read for the face`s list: %d failing, the '
                'first %s' % (len(fails or []), (fails or [])[:3]), bool(fails) and len(fails) == 42))
    dd = os.path.join(sp, 'iii_constructed')
    os.makedirs(dd)
    for k, _w, e in steps:
        p = AC._evidence(e, 'b999', dd)
        if k < 8 and p:
            with open(p, 'w', encoding='utf-8', newline='') as fh:
                fh.write(json.dumps(dict(ready=True)) + NL if p.endswith('_root_banks_dry.json') else 'planted\n')
    a = AC.close_refuses('b999', 8, dd)
    with open(os.path.join(dd, 'b999_root_banks_dry.json'), 'w', encoding='utf-8', newline='') as fh:
        fh.write(json.dumps(dict(ready=False)) + NL)
    b = AC.close_refuses('b999', 8, dd)
    with open(os.path.join(dd, 'b999_root_banks_dry.json'), 'w', encoding='utf-8', newline='') as fh:
        fh.write(json.dumps(dict(ready=True)) + NL)
    os.remove(os.path.join(dd, 'b999_arms_prerun.txt'))
    c = AC.close_refuses('b999', 8, dd)
    planted = "### ### **ARMS RUN : 3. ### LIVE PASSING : 1. ### LIVE FAILING : 2 ['G-ROOTDRY-READY', 'G-TRAIL-LANDED']**"
    dfl = AC.declared_failures(planted, waiting=('G-TRAIL-LANDED',))
    out.append(('(iii)', 'CONSTRUCTED', 'planted banks for [1]-[7]: the seal %r ; [2] made READY False: %r ; [7] removed: %r ; a planted '
                'pre-run failing two, one waiting on the trail: the face`s list %s' % (a or 'MAY RUN', b[:110], c[:110], dfl),
                a == '' and '[2]' in b and 'NOT AS ITS ROW READS' in b and '[7]' in c and 'ABSENT' in c and dfl == ['G-ROOTDRY-READY']))
    return out


def control_iv(sp):
    hc = rd(os.path.join(D, 'b714_hook_control.txt'))
    hr = rd(os.path.join(D, 'b714_hook_refusals.txt')).strip().split(NL)
    kinds = sorted(set(l.split(' | ')[1] for l in hr if l.count(' | ') >= 2))
    ok_c = 'CASES 16 ; AS WANTED 16' in hc and 'ALL AS WANTED True' in hc
    return [('(iv)', 'CONSTRUCTED', 'the offline control (data/b714_hook_control.txt): CASES 16, AS WANTED 16 -- %s' % ok_c, ok_c),
            ('(iv)', 'RECORD', 'the live control (data/b714_hook_refusals.txt): %d refusals at step zero, kinds %s, each printing its row' % (
                len(hr), kinds), kinds == ['ENV', 'PIPE', 'READ', 'REDIR'])]


def control_v(sp):
    j = json.load(open(os.path.join(D, 'b713_corrigendum.json'), encoding='utf-8'))
    letters = [x['letter'] for x in j.get('lettered') or []]
    got = AL.read(letters)
    want = ['w', 'x', 'y', 'z', 'a′', 'b′', 'c′', 'd′']
    try:
        AL.read(["a'", 'b′'])
        mixed = 'READ (NOT REFUSED)'
    except ValueError as e:
        mixed = 'REFUSED: %s' % e
    seq = AL.after(list('abcdefghijklmn'), 12)
    return [('(v)', 'RECORD', 'b713`s corrigendum (data/b713_corrigendum.json) letters %s read under the one lettering as %s, the suite`s '
             'form %s' % (letters, got, got == want), got == want),
            ('(v)', 'CONSTRUCTED', 'a mixed lettering ["a\'", "b′"]: %s ; the twelve after b713`s (a)-(n): %s' % (mixed, ''.join(seq)),
             mixed.startswith('REFUSED') and ''.join(seq) == 'opqrstuvwxyz')]


def controls():
    sp = _plant_dir()
    rows = control_i(sp) + control_ii(sp) + control_iii(sp) + control_iv(sp) + control_v(sp)
    n_ok = sum(1 for r in rows if r[3])
    L = ['b714 -- THE FIVE REPAIRS` CONTROLS, (R324)(6), standing clauses v5 rows (73)-(78) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are control instances: the repair | RECORD or CONSTRUCTED | what was read | AS WANTED. Each repair shows two instances of its',
         '### class, one from the record and one constructed (row (73)); the planted banks under %s.' % sp, '']
    L += ['  %-5s | %-11s | %s | %s' % (r[0], r[1], r[2], r[3]) for r in rows]
    per = dict((k, (sum(1 for r in rows if r[0] == k and r[1] == 'RECORD' and r[3]) >= 1, sum(1 for r in rows if r[0] == k and r[1] == 'CONSTRUCTED' and r[3]) >= 1))
               for k in ('(i)', '(ii)', '(iii)', '(iv)', '(v)'))
    two = all(a and b for a, b in per.values())
    L += ['', '### ### **CONTROLS %d ; AS WANTED %d ; EVERY REPAIR WITH A RECORD AND A CONSTRUCTED INSTANCE AS WANTED %s.**' % (len(rows), n_ok, two)]
    _put('b714_repair_controls.txt', NL.join(L) + NL)
    _put('b714_repair_controls.json', json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), planted=sp,
                                                      rows=[dict(repair=r[0], kind=r[1], read=r[2], ok=r[3]) for r in rows],
                                                      n=len(rows), ok=n_ok, two_instances=two), indent=1, ensure_ascii=False) + NL)
    print(NL.join(L))
    return 0 if n_ok == len(rows) and two else 1


def diffs():
    L = ['b714 -- THE TOOL REPAIRS, (R324)(6) AND THE CARRY, BY DIFF (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### each repaired tool`s diff against HEAD (git diff, the working tree against the last commit); each new shared tool by its sha256 and',
         '### line count. The repairs: (i)-(iii) tools/act_close.py; (2)`s visibility line tools/push_gated.sh; the weight line`s composer',
         '### tools/b714_record.py _wb (C1); (iv) tools/b714_hook.py (step zero); (v) tools/act_letters.py; the corrigendum tool written whole.', '']
    for p in REPAIRED:
        r = subprocess.run(['git', '-C', ROOT, 'diff', '--no-color', 'HEAD', '--', p], capture_output=True, text=True, encoding='utf-8', errors='replace')
        d = r.stdout.replace(chr(13), '')
        hunks = len(re.findall(r'^@@ ', d, re.M))
        L += ['## %s -- %d hunk(s), +%d -%d' % (p, hunks, len(re.findall(r'^\+(?!\+\+)', d, re.M)), len(re.findall(r'^-(?!--)', d, re.M)))]
        L += d.rstrip(NL).split(NL) if d else ['(no change against HEAD)']
        L += ['']
    for p in NEW:
        full = os.path.join(ROOT, p)
        b = open(full, 'rb').read()
        tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', p], capture_output=True, text=True).returncode == 0
        L += ['## %s -- NEW, %d lines, sha256 %s, %s' % (p, b.count(b'\n'), hashlib.sha256(b).hexdigest(), 'tracked' if tracked else 'untracked')]
    L += ['', '### ### **REPAIRED %d ; NEW %d.**' % (len(REPAIRED), len(NEW))]
    _put('b714_tool_repairs.txt', NL.join(L) + NL)
    print(L[-1])
    return 0


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    sys.exit(controls() if r == 'controls' else diffs() if r == 'diffs' else '### routes: controls | diffs')
