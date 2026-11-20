# -*- coding: utf-8 -*-
"""standing/armnorm.py -- v1.20.0, (R350)(2)(i), b739 events (3), b727 events (14): AN ARM'S SEARCH PHRASE READ UNDER THE NORMALISATION THE ARM
APPLIES TO ITS TARGET. G-ENTRY-TITLE-FORM folds the title's opening article ("## The" -> "## the", b706's fold) and searched for its needles
unfolded, so a first needle written "## The ..." could not stand in any folded title: the arm could not pass on a correct title. Here the fold
is applied to the needle and the target alike, and `cannot_pass` names, before the lock, every needle the arm's fold would change -- the needle
that the unrepaired arm could never find.

  fold_article(t)              -> t with its opening article folded, b706's form
  cannot_pass(needles, fold)   -> the needles fold(n) != n: under an arm folding its target and not its needles, each is unfindable
  title_ok(title, needles)     -> every needle, folded, in the folded title (the repaired predicate)
  title_ok_old(title, needles) -> every needle, unfolded, in the folded title (the predicate at v1.19.0)
  python -X utf8 -u tools/standing/armnorm.py title <act>   the act's TITLE_NEEDLES read by cannot_pass and against the title its record
                                                            tool composes (the positive control before the lock); nothing written

v1.38.15, (R374)(5) [K6], b763's finding 8 after its lock (b764 events (20)): THE ROSTER FIGURE READ FROM THE ROSTER AT THE CLOSE. b763's needle
carried "84 open to 83", the ruling's WANTED figure typed before the build lines; its title, composed from the roster, read "84 open to 82",
true to data/b763_orders.txt, and the arm failed in both suites on a right entry.
  roster_at_close(act, read)   -> (open before the act, open at the roster's foot) or None: data/<act>_ledgers.json's roster `before_open`
                                  and the OPEN of the last "### ### **ORDERS n ; OPEN m ; CLOSED c ;" line of data/<act>_orders.txt
  at_close(needles, act, read) -> the needles with ROSTER_TOKEN, and any figure typed as "<n> open to <m>", replaced by the roster's figure
                                  at the close; where the act has no roster the needles stand as written, a token among them unfound
"""
import importlib
import json
import os
import re
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(os.path.dirname(T), 'data')
ROSTER_TOKEN = '<THE ROSTER AT THE CLOSE>'
ROSTER_FIGURE = re.compile(r'\b\d+ open to \d+\b')
ROSTER_FOOT = re.compile(r'(?m)^### ### \*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;')


def _read_data(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return ''
    with open(p, encoding='utf-8') as fh:
        return fh.read().replace('\r', '')


def roster_at_close(act, read=None):
    """(open before the act, open at the roster's foot), or None where either bank does not hold its figure."""
    read = read or _read_data
    try:
        lj = json.loads(read('%s_ledgers.json' % act) or '{}')
    except ValueError:
        lj = {}
    ro = (lj.get('roster') or {}) if isinstance(lj, dict) else {}
    feet = ROSTER_FOOT.findall(read('%s_orders.txt' % act) or '')
    b = ro.get('before_open')
    if not feet or not isinstance(b, int) or isinstance(b, bool):
        return None
    return b, int(feet[-1][1])


def at_close(needles, act, read=None):
    fig = roster_at_close(act, read)
    if fig is None:
        return tuple(needles)
    s = '%d open to %d' % fig
    return tuple(ROSTER_FIGURE.sub(s, n.replace(ROSTER_TOKEN, s)) for n in needles)


def fold_article(t):
    """b706's fold of the article (tools/standing/fold/checks.tpl _fold_article), one form for the target and the needle."""
    return re.sub(r'^(## )(The|A|An)( )', lambda m: m.group(1) + m.group(2).lower() + m.group(3), t)


def cannot_pass(needles, fold=fold_article):
    return [n for n in needles if fold(n) != n]


def title_ok(title, needles):
    f = fold_article(title)
    return title.startswith('## ') and all(fold_article(n) in f for n in needles)


def title_ok_old(title, needles):
    f = fold_article(title)
    return title.startswith('## ') and all(n in f for n in needles)


def _act_module(act):
    if T not in sys.path:
        sys.path.insert(0, T)
    return importlib.import_module('acts.%s' % act)


def needles_of(act):
    """v1.38.15, [K6]: the act's TITLE_NEEDLES read by their literal from tools/acts/<act>.py. The act module is a sections file since the fold
    took the tools apart, and no import of it compiles (b764: a SyntaxError at its :877), so the title route read nothing at any act."""
    import ast
    p = os.path.join(T, 'acts', '%s.py' % act)
    if not os.path.exists(p):
        return ()
    with open(p, encoding='utf-8') as fh:
        src = fh.read().replace('\r', '')
    m = re.search(r'(?m)^TITLE_NEEDLES = ', src)
    if not m:
        return ()
    k = m.end()
    while True:
        k = src.find('\n', k + 1)
        if k < 0:
            return ()
        try:
            v = ast.literal_eval(src[m.end():k].strip())
        except (SyntaxError, ValueError):
            continue
        return tuple(v) if isinstance(v, (tuple, list)) else ()


def main(argv):
    if len(argv) < 3 or argv[1] != 'title':
        sys.exit('usage: armnorm.py title <act>')
    act = __import__('act').act_name(argv[2], 'armnorm.py title', 'usage: armnorm.py title <act>')   # ### v1.32.0, (R362)(7)(vii), b751 (t)
    needles = needles_of(act)
    cp = cannot_pass(needles)
    print('  %s TITLE_NEEDLES %d ; under a fold of the target alone CANNOT PASS: %s' % (act, len(needles), cp or 'NONE'))
    fig = roster_at_close(act)
    typed = [n for n in needles if ROSTER_FIGURE.search(n)]
    print('  THE ROSTER AT THE CLOSE ((R374)(5) [K6]): %s ; needles carrying the token %d ; a figure typed in a needle, read from the roster in its '
          'place: %s' % (('%d open to %d' % fig) if fig else 'NONE (no roster figure in the banks: a token stays unfound)',
                         sum(1 for n in needles if ROSTER_TOKEN in n), ', '.join(ROSTER_FIGURE.search(n).group(0) for n in typed) or 'NONE'))
    needles = at_close(needles, act)
    try:
        rec = importlib.import_module('%s_record' % act)
        title = rec._title()
    except Exception as e:   # ### the record tool renders at the close; before it the title is read by the caller
        print('  the composed title: UNREAD (%s)' % str(e)[:120])
        return
    print('  the composed title: %s' % title[:160])
    print('  ### the repaired arm on it: %s ; the arm as at v1.19.0: %s' % ('PASS' if title_ok(title, needles) else 'FAIL',
                                                                         'PASS' if title_ok_old(title, needles) else 'CANNOT PASS' if cp else 'FAIL'))


if __name__ == '__main__':
    main(sys.argv)
