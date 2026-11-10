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
"""
import importlib
import os
import re
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


def main(argv):
    if len(argv) < 3 or argv[1] != 'title':
        sys.exit('usage: armnorm.py title <act>')
    act = __import__('act').act_name(argv[2], 'armnorm.py title', 'usage: armnorm.py title <act>')   # ### v1.32.0, (R362)(7)(vii), b751 (t)
    m = _act_module(act)
    needles = tuple(getattr(m, 'TITLE_NEEDLES', ()) or ())
    cp = cannot_pass(needles)
    print('  %s TITLE_NEEDLES %d ; under a fold of the target alone CANNOT PASS: %s' % (act, len(needles), cp or 'NONE'))
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
