# -*- coding: utf-8 -*-
"""standing/v1370.py -- THE CONTROLS OF v1.37.0, (R370)(5)(iii): THE SUBJECT READ OVER THE LIVE PAPERS, in v1369.py's form.

The ruling's words (relay data/b760_ferry.txt :17): "(iii) THE SUBJECT READ OVER THE LIVE PAPERS: tools/standing/subject.py gains a third
search, the lines of the registry's live papers that name the object's nouns, each printed by path and line, so that a ruling's destinations
are read from it and not from recall. Its control: at PLACE-papers 4ea41948, with the nouns Epstein and Z_Q, the lines of (R369)(9) that carry
either noun are each printed, their count beside 14." tools/standing/subject.py v1.37.0 reads the live papers (live_papers: every `.md` path
REGISTRY names at the ref outside rule [Q] (3)'s section, each by its family to every file of it in the tree, the copies under archive/ and
outputs/ and the four ledgers left out) and searches every line of each (live_items), each hit printed by path, line and nouns and never by its
words. BEFORE is subject.py at BASE, executed as a module of its own; AFTER the working file. Every case reads PLACE-papers through git at a
named ref; nothing is written; no line of a paper is printed.

  (keys)      THE ORDERED CONTROL: at 4ea41948, Epstein and Z_Q, BLOCK D's fourteen keys each by path and line, their count beside 14.
  (copy)      a copy REGISTRY names (outputs/...) is not a live paper.
  (family)    an edition REGISTRY does not name, day1/Which_Structure_Confines_v2_4_0.md, read as its family's.
  (ledgers)   the four ledgers left out of the live papers.
  (section)   rule [Q] (3)'s section skipped for names, found by its heading's digest: its 27 lines at 4ea41948.
  (planted)   a planted noun reaches no live line; a planted live item carrying it is reached, by its place.
  (print)     the print by place: with --quote, no live hit's words printed (BEFORE's run quotes them).
  (read)      the read takes the three searches together: (R370)'s ruling with Epstein and Z_Q at HEAD prints the live papers' lines.
  (diff)      the working subject.py against BASE's: every line removed is one the change names.
  (version)   tools/standing/VERSION moved to v1.37.0.

  python -X utf8 -u tools/standing/v1370.py control [keys|copy|family|ledgers|section|planted|print|read|diff|version ...] [--bank]
"""
import contextlib
import difflib
import io
import os
import sys
import time
import types

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
BASE = '8d99ac80'   # ### the relay's HEAD before this change (b760 component 2, step 14, HANDOFF.md; v1.36.9)
REF = '4ea41948'    # ### PLACE-papers at b758's close, (R369)(9)'s base, as (R370)(5)(iii) names it
SPECS = ('word:Epstein=Epstein', 'sym:Z_Q')
FERRY = os.path.join(D, 'b760_ferry.txt').replace('\\', '/')
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import compilecontrol as CC     # noqa: E402
import figbank as FB            # noqa: E402
import subject as S1            # noqa: E402  (the working file: AFTER)
import v1340 as V               # noqa: E402  (show, free_line)

_MEMO = {}


def base():
    """subject.py at BASE, executed as a module of its own (its __main__ guard keeps main() unrun)."""
    if 'S0' not in _MEMO:
        src = V.show(BASE, 'tools/standing/subject.py')
        m = types.ModuleType('subject_base')
        m.__file__ = os.path.join(S, 'subject.py')
        exec(compile(src, 'subject.py@%s' % BASE, 'exec'), m.__dict__)   # noqa: S102
        _MEMO['S0'] = m
        _MEMO['src0'] = src
    return _MEMO['S0']


def case(L, k, what, before, after, ok_b, ok_a):
    L.append('  (%s) %s' % (k, what))
    L.append('      BEFORE: %s -> %s' % (before, 'AS WANTED' if ok_b else 'NOT AS WANTED'))
    L.append('      AFTER : %s -> %s' % (after, 'AS WANTED' if ok_a else 'NOT AS WANTED'))
    return 1 if ok_b and ok_a else 0


def live(ref=REF):
    if ('live', ref) not in _MEMO:
        _MEMO[('live', ref)] = S1.live_items(ref)
    return _MEMO[('live', ref)]


def papers(ref=REF):
    if ('papers', ref) not in _MEMO:
        _MEMO[('papers', ref)] = S1.live_papers(ref)
    return _MEMO[('papers', ref)]


def _none(m):
    return 'no third search (live_papers %s, live_items %s)' % (hasattr(m, 'live_papers'), hasattr(m, 'live_items'))


def control_keys():
    L = ['### (keys): THE ORDERED CONTROL, BLOCK D`S KEYS AT PLACE-papers %s WITH EPSTEIN AND Z_Q' % REF]
    b = base()
    items, _fig, ri = b.corpus(REF)
    rb = b.run(SPECS, '', items + ri, quote=False)
    D_ = S1.block_d()
    reach_b = sum(1 for k, p, n in D_ if ('live:' + p, n) in rb['hit'] or (p, n) in rb['hit'])
    ok, out = S1.control_live(REF)
    L += ['      ' + l.strip() for l in out if l.lstrip().startswith(('C', '###'))]
    tail = out[-1]
    return L, case(L, 'keys', 'the third search at %s, %s ; BLOCK D`s keys reached' % (REF, ' '.join(SPECS)),
                   '%s ; the two searches reach %d of %d keys (their hits %d)' % (_none(b), reach_b, len(D_), rb['hits']),
                   tail[tail.index('BLOCK D`S KEYS'):].rstrip(), reach_b == 0 and len(D_) == 14,
                   ok and 'REACHED 14 BESIDE 14' in tail), 1


def control_copy():
    L = ['### (copy): A COPY REGISTRY NAMES IS NOT A LIVE PAPER']
    named, _skip = S1._registry_named(REF)
    copies = sorted(n for n in named if n.startswith(S1.LIVE_OUT))
    P, fig = papers()
    inside = [p for p in P if p.startswith(S1.LIVE_OUT)]
    return L, case(L, 'copy', 'REGISTRY`s named paths at %s under %s' % (REF, ' or '.join(S1.LIVE_OUT)), _none(base()),
                   'named copies %d %s ; live papers under them %d ; the figure named_copies %d' % (len(copies), copies, len(inside), fig['named_copies']),
                   not hasattr(base(), 'live_papers'), len(copies) >= 1 and not inside and fig['named_copies'] == len(copies)), 1


WSC = 'day1/Which_Structure_Confines_v2_4_0.md'


def control_family():
    L = ['### (family): AN EDITION READ AS ITS FAMILY`S']
    named, _skip = S1._registry_named(REF)
    P, _fig = papers()
    fam = S1.family_of(WSC)
    return L, case(L, 'family', '%s at %s' % (WSC, REF), _none(base()),
                   'named itself %s ; its family %s named %s ; a live paper %s' % (WSC in named, fam, fam in named, WSC in P),
                   not hasattr(base(), 'live_papers'), WSC not in named and fam in named and WSC in P), 1


def control_ledgers():
    L = ['### (ledgers): THE FOUR LEDGERS LEFT OUT']
    named, _skip = S1._registry_named(REF)
    P, fig = papers()
    inn = [x for x in S1.LIVE_LEDGERS if x in P]
    nam = [x for x in S1.LIVE_LEDGERS if x in named]
    return L, case(L, 'ledgers', '%s at %s' % (', '.join(S1.LIVE_LEDGERS), REF), _none(base()),
                   'named %d of 4 ; among the live papers %d ; the figure ledgers_left_out %d' % (len(nam), len(inn), fig['ledgers_left_out']),
                   not hasattr(base(), 'live_papers'), not inn and fig['ledgers_left_out'] == len(nam) and len(nam) >= 1), 1


def control_section():
    L = ['### (section): RULE [Q] (3)`S SECTION SKIPPED, FOUND BY ITS HEADING`S DIGEST (no line of it printed)']
    import handoff as HO
    reg = S1.blob('REGISTRY.md', REF)
    k = HO.head_line(reg)
    _n, skip = S1._registry_named(REF)
    planted = ['# a planted line'] + reg
    k2 = HO.head_line(planted)
    return L, case(L, 'section', 'REGISTRY.md at %s' % REF, _none(base()),
                   'the heading at :%d (sha256 opening %s) ; its section skipped, %d lines ; a line planted above: the heading at :%d' % (
                       k, HO.HEAD_DIGEST, skip, k2),
                   not hasattr(base(), 'live_papers'), skip == 27 and k2 == k + 1), 1


def control_planted():
    L = ['### (planted): A PLANTED NOUN, AND A PLANTED LIVE ITEM CARRYING IT']
    li, _fig = live()
    a = S1.run((S1.PLANTED,), '', li, quote=False)
    item = ('live:planted/PLANTED.md', 7, 'a line carrying qzxwvplanted')
    a2 = S1.run((S1.PLANTED,), '', li + [item], quote=True)
    shown = [l for l in a2['lines'] if 'planted/PLANTED.md :7' in l]
    return L, case(L, 'planted', 'the noun %s over the %d live lines at %s, then with one planted item' % (S1.PLANTED, len(li), REF), _none(base()),
                   'hits %d ; with the planted item %d, printed by place %d, its words printed %s' % (
                       a['hits'], a2['hits'], len(shown), any('carrying qzxwvplanted' in l for l in a2['lines'])),
                   not hasattr(base(), 'live_items'), a['hits'] == 0 and a2['hits'] == 1 and len(shown) == 1 and not any('carrying' in l for l in a2['lines'])), 1


def control_print():
    L = ['### (print): THE PRINT BY PLACE (counts alone printed)']
    li, _fig = live()
    a = S1.run(SPECS, '', li, quote=True)
    b = base().run(SPECS, '', li, quote=True)
    frag = [l[:40] for d, n, l in li if (d, n) in a['hit'] and len(l.strip()) >= 20]
    la, lb = NL.join(a['lines']), NL.join(b['lines'])
    leak_a = sum(1 for f in frag if f in la)
    leak_b = sum(1 for f in frag if f in lb)
    return L, case(L, 'print', 'the live hits at %s with quote on, their lines` first 40 characters looked for in the print' % REF,
                   'of %d hits` words, %d printed' % (len(frag), leak_b), 'of %d hits` words, %d printed' % (len(frag), leak_a),
                   len(frag) > 0 and leak_b > 0, len(frag) > 0 and leak_a == 0), 1


def _main_read(m):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        m.main(['read', FERRY, 'RULING (R370) BEGIN', 'RULING (R370) END'] + list(SPECS))
    return buf.getvalue().split(NL)


def control_read():
    L = ['### (read): THE READ TAKES THE THREE SEARCHES TOGETHER, AT HEAD']
    ob, oa = _main_read(base()), _main_read(S1)
    hb = [l for l in ob if l.startswith('### THE SUBJECT READ')]
    ha = [l for l in oa if l.startswith('### THE SUBJECT READ')]
    nlive_b = sum(1 for l in ob if ' live:' in l)
    nlive_a = sum(1 for l in oa if ' live:' in l)
    cut = lambda h: h[0][h[0].index('NOUNS'):h[0].index('; HITS') + 40].strip() if h else 'no head line'   # noqa: E731
    return L, case(L, 'read', 'subject.py read %s RULING (R370) %s' % (FERRY[len(RELAY) + 1:], ' '.join(SPECS)),
                   '%s ; live lines printed %d' % (cut(hb), nlive_b), '%s ; live lines printed %d' % (cut(ha), nlive_a),
                   bool(hb) and 'LIVE PAPER LINES' not in hb[0] and nlive_b == 0, bool(ha) and 'LIVE PAPER LINES' in ha[0] and nlive_a > 0), 1


NAMED = ("nR = len(hs) - nF - nI",
         "L = ['### THE SUBJECT READ: NOUNS %d ; HEADINGS %d ; ENTRY HEADS %d%s ; HITS %d ; CITED %d ; UNCITED %d ; MATCHING TWO OR MORE %d%s' % (",
         "len(pats), nF, nI, ' ; RELAY LINES %d' % nR if nR else '', len(hits), len(hits) - len(unc), len(unc), len(multi),",
         "'' if quote else ' ; PRINTED BY PLACE, NO LINE QUOTED')]",
         "L.append('   %s %s :%d [%s]%s' % ('TWO+' if len(f) >= 2 else '    ', d, n, ', '.join(f), ' ' + l[:130] if quote else ''))",
         "print('\\n'.join(L + L2))",
         "return 0 if ok and ok2 else 1",
         "print('\\n'.join(run(argv[4:], t, items + ri, quote=quote, fig=fig)['lines']))")


def control_diff():
    L = ['### (diff): THE WORKING subject.py AGAINST BASE`S']
    base()
    s0 = _MEMO['src0'].replace('\r', '').split(NL)
    s1 = io.open(os.path.join(S, 'subject.py'), encoding='utf-8').read().replace('\r', '').split(NL)
    d = [l for l in difflib.unified_diff(s0, s1, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    rem = [l[1:] for l in d if l[0] == '-']
    add = [l[1:] for l in d if l[0] == '+']
    odd = [r for r in rem if r not in NAMED and r.strip() not in NAMED]
    return L, case(L, 'diff', 'lines removed and added', 'BASE`s file read, %d lines' % len(s0),
                   '%d removed, %d added ; removed named %d, other %d %s' % (len(rem), len(add), len(rem) - len(odd), len(odd), [o.strip()[:60] for o in odd]),
                   len(s0) > 300, len(rem) > 0 and not odd), 1


def control_version():
    L = ['### (version): THE STANDING VERSION PRINTED']
    ver = io.open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = (V.show(BASE, 'tools/standing/VERSION') or '').strip()
    return L, case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.36.9', ver == 'v1.37.0'), 1


CONTROLS = dict(keys=control_keys, copy=control_copy, family=control_family, ledgers=control_ledgers, section=control_section,
                planted=control_planted, print=control_print, read=control_read, diff=control_diff, version=control_version)
ORDER = ('keys', 'copy', 'family', 'ledgers', 'section', 'planted', 'print', 'read', 'diff', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.37.0, (R370)(5)(iii): THE SUBJECT READ OVER THE LIVE PAPERS (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each case before and after; the free memory read before each; '
           'PLACE-papers read through git at the refs named; no line of a paper, no protected line and not the quoting rule`s word printed; '
           'written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY CASE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case before (tools/standing/subject.py at %s) and after (the working file); nothing written' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(V.free_line())
        try:
            L, gd, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, gd, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, str(e)[:160])], 0, 1
        out += L + ['']
        tg, tn = tg + gd, tn + c
        per.append('(%s) %d of %d' % (k, gd, c))
    out.append('### per change: %s' % ' ; '.join(per))
    out.append('### ### **v1.37.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg,
                                                                                'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        nm = '%s_standing_v1370.txt' % act
        r = FB.write(os.path.join(D, nm), NL.join(out))
        print('written data/%s (figbank: %s)' % (nm, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
