# -*- coding: utf-8 -*-
"""standing/v1347.py -- THE CONTROLS OF v1.34.7 ((R366)(1)(i) THE NEXT ACT'S LINE and (1)(ii) THE WORDS THAT NAME A BANK NOT KEPT, one
standing change), in v1346.py's form: each instance read through the route as it stood at BASE (relay eac02515, v1.34.6's own commit, read
from its blobs) and through the route on disk; AS WANTED where the old route fails the instance and the new passes it. THE COMPILE CONTROL
RUNS FIRST. The free memory is printed before each control. No write reaches the relay or PLACE-papers: the planted answers bank and the
planted data folder stand in a temporary folder, removed after; b755's banks are read and not written. Written at b756 by the Write tool; no
identifier of the author is read into any string here.

  (next)     tools/standing/nextact.py: the closing's item (a) (carried()) and the entry's "**Next.**" and "**Next:**" lines (entry(), bound
             over the act's composition at tools/standing/fold/record.tpl's foot) read PHRASE, "as the author answers at the root (the answers
             bank)", with the answers bank by its path, the answer's line and words where word() finds one, then the act's words as put;
             over b755's own closing items and answers bank (data/b755_closing.txt :640, data/b755_author_answers.txt), over a planted bank
             answering a prompt headed with the next act, and over b755's worklist NEXT (tools/b755_worklist.py :235); word() unchanged;
             the act's record and closing renders compile, the wrapper bound once after the act's composition and above the main block.
  (n4)       tools/standing/fold/record.tpl's _n4 (the desk's and the scores' N4 line): over a planted data folder holding an act's events
             bank and no post-seal bank, BASE's words read "the events bank for what is found after the seal present"; on disk the words
             name no such bank as kept and read the post-seal bank's path absent; PRESENT where one is planted; the act's render holds the
             corrected words once and BASE's none.
  (version)  tools/standing/VERSION moved to v1.34.7.

  python -X utf8 -u tools/standing/v1347.py control [next|n4|version ...] [--bank]
"""
import io
import os
import re
import shutil
import sys
import tempfile
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = 'eac02515'   # ### v1.34.6's own commit (b755 component 1): the routes before this change
PHRASE = 'as the author answers at the root (the answers bank)'   # ### (R366)(1)(i), the ruling's words (data/b756_ferry.txt :9)
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import fold as F                # noqa: E402
import v1340 as V               # noqa: E402  (show, free_line, _fn_src)


def show(rel):
    return V.show(BASE, rel)


def disk(rel):
    return io.open(os.path.join(RELAY, *rel.split('/')), encoding='utf-8').read().replace('\r', '')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.6): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.34.7): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def both(L, cls, what, at_base, on_disk, holds_base, holds_disk):
    """a case wanted the same at both routes (the plain reading)."""
    ok = bool(holds_base) and bool(holds_disk)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.34.6): %s -> (the same at both is wanted)' % at_base,
          '      AFTER  (v1.34.7): %s -> %s' % (on_disk, 'PASSES' if ok else 'DOES NOT PASS'), '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case of the new route alone (a planted instance the old route has no reading of)."""
    L += ['  (%s) %s' % (cls, what), '      AFTER  (v1.34.7): %s -> %s' % (new, 'AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


# ================================================================================ (next)
def _nextact(src):
    """tools/standing/nextact.py executed from a text, its __file__ the file on disk (so its data folder is the relay's)."""
    ns = dict(__file__=os.path.join(S, 'nextact.py'), __name__='nextact_control')
    exec(compile(src, 'nextact.py', 'exec'), ns)   # noqa: S102
    return ns


def _plant_answers(td):
    """a planted answers bank for b998, its root prompt headed with the next act (b999) and answered by an option."""
    p = os.path.join(td, 'b998_author_answers.txt')
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('### b998 -- THE AUTHOR`S ANSWERS, 1 prompt(s) put by the seat in this act (planted)\n\n'
                '### CALL tool-use id planted (planted)\n'
                '### PROMPT 1 (b999): the planted question: the planted build as b999, or another?\n'
                '  OPTION 1: Planted build as b999 :: the planted build.\n'
                '  OPTION 2: Another :: another.\n'
                'RESULT (planted): Your questions have been answered: "the planted question"="Planted build as b999". You can now continue.\n')
    return p


ITEMS = ['    (a) ### **THE NEXT, AS THE PLANTED RULING ORDERS IT**: the planted build as b999, or another the author names;',
         '        its second line, the module`s words continued.',
         '    (b) The open orders: as they stand.']


def _item_a(items):
    return next((l for l in items if l.startswith('    (a) ')), '')


def control_next():
    L, g, n = ['### (next): (R366)(1)(i), THE ENTRY`S AND THE CLOSING`S LINE FOR THE ACT THAT FOLLOWS'], 0, 0
    act = A.current()['act']
    bo, bn = _nextact(show('tools/standing/nextact.py') or ''), _nextact(disk('tools/standing/nextact.py'))
    cl = disk('data/b755_closing.txt').split(NL)
    k = [i for i, l in enumerate(cl) if l.startswith('### CARRIED FORWARD.')]
    items = cl[k[0] + 1:k[0] + 12] if k else []
    ao, an = _item_a(bo['carried']('b755', items)), _item_a(bn['carried']('b755', items))
    n += 1
    g += case(L, 'next', 'the closing`s item (a) over b755`s own items (data/b755_closing.txt :%d) and answers bank, word() finding no answer '
              'there (its root prompt headed "(Next act)", data/b755_author_answers.txt :32): the ruling`s words and the bank by its path' % (k[0] + 2 if k else 0),
              'BASE`s carried(): the item as the module wrote it ; PHRASE %s ; the bank named %s' % (PHRASE in ao, 'relay data/b755_author_answers.txt' in ao),
              'carried() on disk: PHRASE %s ; the bank named %s ; the module`s words kept as put %s' % (
                  PHRASE in an, 'relay data/b755_author_answers.txt' in an, 'chosen at this act`s root' in an),
              bool(ao) and PHRASE not in ao,
              PHRASE in an and 'relay data/b755_author_answers.txt' in an and 'chosen at this act`s root' in an)
    td = tempfile.mkdtemp(prefix='v1347_')
    try:
        _plant_answers(td)
        wo, wn = bo['word']('b998', td), bn['word']('b998', td)
        po, pn = bo['carried']('b998', ITEMS, td), bn['carried']('b998', ITEMS, td)
        ao, an = _item_a(po), _item_a(pn)
        n += 1
        g += case(L, 'next', 'the closing`s item (a) over a planted bank answering a prompt headed with the next act: the ruling`s words, the '
                  'answer with its line, then the module`s words as put',
                  'BASE`s carried(): the answer alone ; PHRASE %s ; answer %s ; the module`s words %s' % (
                      PHRASE in ao, 'Planted build as b999' in ao, 'or another the author names' in ao),
                  'carried() on disk: PHRASE %s ; the answer with its line %s ; the module`s words as put %s' % (
                      PHRASE in an, (' :%d, the author chose: Planted build as b999' % (wn or (0,))[0]) in an, 'as put: the planted build as b999' in an),
                  bool(ao) and PHRASE not in ao,
                  PHRASE in an and bool(wn) and (' :%d, the author chose: Planted build as b999' % wn[0]) in an and 'as put: the planted build as b999' in an)
        n += 1
        g += guard(L, 'next', 'the planted items` other lines kept in their order (item (a)`s second line, item (b)), the count unchanged',
                   'items in %d, out %d ; second line kept %s ; (b) kept %s' % (len(ITEMS), len(pn), ITEMS[1] in pn, ITEMS[2] in pn),
                   len(pn) == len(ITEMS) and pn[1:] == ITEMS[1:])
        n += 1
        g += both(L, 'next', 'word() unchanged: over b755`s bank and over the planted bank, the same reading at both routes',
                  'BASE: b755 %s ; planted %s' % (bo['word']('b755'), wo), 'on disk: b755 %s ; planted %s' % (bn['word']('b755'), wn),
                  True, bo['word']('b755') == bn['word']('b755') and wo == wn and wn is not None)
    finally:
        shutil.rmtree(td, ignore_errors=True)
    n += 1
    g += guard(L, 'next', 'the planted folder removed after the cases', 'removed %s' % (not os.path.exists(td)), not os.path.exists(td))
    wk = show('tools/b755_worklist.py') or disk('tools/b755_worklist.py')
    m = re.search(r"^NEXT = '(.*)'$", wk, re.M)
    nx = m.group(1) if m else ''
    ent = NL.join(['**The planted paragraph.** words.', '', '**Next.** %s.' % nx, '', '**Next:** %s.' % nx, '', '*The planted foot.*'])
    eo = ent if 'entry' not in bo else bo['entry']('b755', ent)
    en = bn['entry']('b755', ent)
    nl_o = [l for l in eo.split(NL) if l.startswith(('**Next.**', '**Next:**'))]
    nl_n = [l for l in en.split(NL) if l.startswith(('**Next.**', '**Next:**'))]
    rest_same = [l for l in en.split(NL) if not l.startswith(('**Next.**', '**Next:**'))] == [l for l in ent.split(NL) if not l.startswith(('**Next.**', '**Next:**'))]
    n += 1
    g += case(L, 'next', 'the entry`s two forms of the line ("**Next.**" and "**Next:**") over b755`s worklist NEXT (tools/b755_worklist.py :235): '
              'the ruling`s words and the bank, the full stop kept, every other line as composed',
              'BASE: entry() %s ; the lines carrying PHRASE %d of %d' % ('present' if 'entry' in bo else 'absent, the lines as composed', sum(PHRASE in l for l in nl_o), len(nl_o)),
              'entry() on disk: the lines carrying PHRASE and the bank %d of %d ; each ending in a full stop %s ; the other lines unchanged %s' % (
                  sum(PHRASE in l and 'relay data/b755_author_answers.txt' in l for l in nl_n), len(nl_n), all(l.endswith('.') and not l.endswith('..') for l in nl_n), rest_same),
              bool(nl_o) and not any(PHRASE in l for l in nl_o),
              len(nl_n) == 2 and all(PHRASE in l and 'relay data/b755_author_answers.txt' in l and l.endswith('.') and not l.endswith('..') for l in nl_n) and rest_same)
    n += 1
    g += guard(L, 'next', 'entry() read twice equals entry() read once', 'equal %s' % (bn['entry']('b755', en) == en), bn['entry']('b755', en) == en)
    import importlib
    K = importlib.import_module('%s_worklist' % act)
    own = bn['line'](act, K.next_line(text=''))
    n += 1
    g += guard(L, 'next', '%s`s own line, its worklist`s NEXT read through line(): PHRASE once, its bank, the act`s words as put' % act,
               own[:240], own.count(PHRASE) == 1 and ('relay data/%s_author_answers.txt' % act) in own and '; as put: ' in own and K.NEXT in own)
    try:
        text = F.render(act, 'record')
        compile(text, '%s_record.py' % act, 'exec')
        RL = text.split(NL)
        defs = [i for i, l in enumerate(RL) if l.startswith('def _finding_text(')]
        bind = [i for i, l in enumerate(RL) if l.startswith('_finding_text_composed = _finding_text')]
        main = [i for i, l in enumerate(RL) if l.startswith("if __name__ == '__main__':")]
        r_ok = len(bind) == 1 and len(defs) >= 2 and defs[0] < bind[0] < defs[-1] < main[-1] and text.count('NXA7.entry(ACT, e, D)') == 1
        r_why = 'compiles, %d lines ; the composition`s def at :%s ; the wrapper`s binding at :%s ; the wrapper`s def at :%s ; main at :%s' % (
            len(RL), defs[0] + 1 if defs else None, bind[0] + 1 if bind else None, defs[-1] + 1 if defs else None, main[-1] + 1 if main else None)
    except (SyntaxError, F.FoldRefused) as e:
        r_ok, r_why = False, '%s: %s' % (type(e).__name__, str(e)[:120])
    n += 1
    g += guard(L, 'next', '%s`s record render through the template on disk: the wrapper bound once, after the act`s composition and above the main block' % act, r_why, r_ok)
    try:
        ct = F.render(act, 'closing')
        compile(ct, '%s_closing.py' % act, 'exec')
        c_ok, c_why = ct.count("NXA.carried('%s', _carried_items(), D)" % act) == 1, 'compiles, %d lines ; carried() through nextact %d' % (
            ct.count(NL), ct.count("NXA.carried('%s', _carried_items(), D)" % act))
    except (SyntaxError, F.FoldRefused) as e:
        c_ok, c_why = False, '%s: %s' % (type(e).__name__, str(e)[:120])
    n += 1
    g += guard(L, 'next', '%s`s closing render through the template on disk (closing.tpl unchanged), its item (a) through nextact`s carried()' % act, c_why, c_ok)
    return L, g, n


# ================================================================================ (n4)
def _n4_words(tpl_text, data_dir, act='b999'):
    """_n4's words on the post-seal events bank from a template's text: its `ev` line and the value it prints, read over <data_dir>. The
    function's text is cut from its def to the next def (_n5): the template's ⟪SLOT 23⟫ and ⟪SLOT 24⟫ stand at column 0 inside it, where
    v1340's _fn_src stops (the first run of this control, 13:26:30Z, unbanked: words and value not found, three cases NOT AS WANTED)."""
    m = re.search(r'^def _n4\(.*?(?=^def _n5\()', tpl_text, re.M | re.S)
    src = (m.group(0) if m else '').replace('⟪ACT⟫', act)
    ev_m = re.search(r"^\s*ev = (os\.path\.exists\(.*?\))\s*(?:#.*)?$", src, re.M)
    w_m = re.search(r"((?:no )?(?:the )?events bank for what is found after the seal[^%]*%s)", src)
    v_m = re.search(r"('[^']*' if ev else '[^']*')", src)
    if not (ev_m and w_m and v_m):
        return None, 'the reading`s three parts found: ev %s ; words %s ; value %s' % (bool(ev_m), bool(w_m), bool(v_m))
    ev = eval(ev_m.group(1), dict(os=os, D=data_dir, ACT=act))   # noqa: S307  ### the template's own expression
    return w_m.group(1) % eval(v_m.group(1), dict(ev=ev)), ev_m.group(1)   # noqa: S307


def control_n4():
    L, g, n = ['### (n4): (R366)(1)(ii), THE WORDS THAT NAME A BANK NOT KEPT (the desk`s and the scores` N4 line, record.tpl`s _n4)'], 0, 0
    act = A.current()['act']
    to, tn = show('tools/standing/fold/record.tpl') or '', disk('tools/standing/fold/record.tpl')
    desk = disk('data/b755_desk_notes.txt').split(NL)
    td = tempfile.mkdtemp(prefix='v1347_')
    try:
        io.open(os.path.join(td, 'b999_events.txt'), 'w', encoding='utf-8').write('planted events bank\n')
        wo, _eo = _n4_words(to, td)
        wn, en = _n4_words(tn, td)
        n += 1
        g += case(L, 'n4', 'the N4 words over a planted data folder holding an act`s events bank and no post-seal bank: no bank for what is '
                  'found after the seal named as kept',
                  'BASE`s _n4: "%s" (b755`s desk printed it so, data/b755_desk_notes.txt :8 holding "the events bank for what is found after the seal present" %s)' % (
                      wo, len(desk) > 7 and 'the events bank for what is found after the seal present' in desk[7]),
                  '_n4 on disk: "%s"' % ((wn or '')[:260]),
                  bool(wo) and wo.endswith('found after the seal present'),
                  bool(wn) and wn.startswith('no events bank for what is found after the seal') and wn.endswith('relay data/b999_events_postseal.txt absent'))
        io.open(os.path.join(td, 'b999_events_postseal.txt'), 'w', encoding='utf-8').write('planted post-seal bank\n')
        wp, _ep = _n4_words(tn, td)
        n += 1
        g += guard(L, 'n4', 'a post-seal bank planted beside it: printed PRESENT, as a bank the act does not keep', (wp or '')[-80:],
                   bool(wp) and wp.endswith('relay data/b999_events_postseal.txt PRESENT, a bank the act does not keep'))
        n += 1
        g += guard(L, 'n4', 'the predicate on disk reads the post-seal bank`s path, not the act`s events bank', en, bool(en) and '_events_postseal.txt' in en)
    finally:
        shutil.rmtree(td, ignore_errors=True)
    n += 1
    g += guard(L, 'n4', 'the planted folder removed after the cases', 'removed %s' % (not os.path.exists(td)), not os.path.exists(td))
    try:
        text = F.render(act, 'record')
        k_new = text.count('no events bank for what is found after the seal')
        k_old = text.count('the events bank for what is found after the seal %s')
        r_ok, r_why = k_new == 1 and k_old == 0, 'the corrected words %d ; BASE`s words %d' % (k_new, k_old)
    except (SyntaxError, F.FoldRefused) as e:
        r_ok, r_why = False, '%s: %s' % (type(e).__name__, str(e)[:120])
    n += 1
    g += guard(L, 'n4', '%s`s record render: the desk and the scores read one _n4, its words corrected once' % act, r_why, r_ok)
    return L, g, n


# ================================================================================ (version)
def control_version():
    L, g, n = ['### (version): THE STANDING VERSION PRINTED'], 0, 0
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (show('tools/standing/VERSION') or '').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.34.6', ver == 'v1.34.7')
    return L, g, n


CONTROLS = dict(next=control_next, n4=control_n4, version=control_version)
ORDER = ('next', 'n4', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.34.7, (R366)(1)(i) THE NEXT ACT`S LINE AND (1)(ii) THE WORDS THAT NAME A BANK NOT KEPT (%s)' % (
               act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each change`s instances through both routes; the free memory read before each; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.34.7: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1347.txt' % act), NL.join(out))
        print('written data/%s_standing_v1347.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
