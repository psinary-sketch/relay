# -*- coding: utf-8 -*-
"""standing/cites.py -- A CITATION READ FROM A TABLE, NOT CARRIED BY SUBSTITUTION ((R335)(2)(v), b724's event (18)): the mirror bank's prose
cited "(Rnnn)(5)" for the roster read from PLACE-papers main and "(Rnnn)(2)(iii)" for the MANIFEST control; the template's ruling
token renders the current act's ruling, so each carry moved the numbers off the clauses that ordered those routes (b724's (R334)(5) is
its lv negation). Written at b725 by the Write tool (v1.5.0).

THE TABLE: each route's citation is the (act, clause) that ordered it, fixed here and rendered as that act's ruling with the clause --
  mirror.roster    b715, (R325)(5): the roster read from PLACE-papers main at the build (b715's ruling, the mirror's roster route)
  mirror.manifest  b721, (R331)(2)(iii): the MANIFEST control at the build commit (tools/standing/ v1.2.1)
and one row read from the current act's ferry, not fixed: mirror.prevbuild, the (W) clause naming tools/mirror_prevbuild.json -- the
ruling's top-level item whose clause carries that name (b725: (R335)(5)); where no clause carries it the citation reads
"(### NOT IN THE FERRY)", never a carried number.

  cite(key, act=None) -> '(Rnnn)(n)...'     check(text, act) -> [(key, cited, wanted)] the table's keys whose citation the text misplaces
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

TABLE = {
    'mirror.roster': ('b715', '(R325)', '(5)'),
    'mirror.manifest': ('b721', '(R331)', '(2)(iii)'),
}
READ = {'mirror.prevbuild': 'mirror_prevbuild'}
TOP = re.compile(r'^\((\d+)\) ', re.M)
RUL = re.compile(r'RULING (\(R\d+\))')


CLAUSE = re.compile(r'\(R(\d{3})\)\((\d+)\)')
INSTRUMENT = re.compile(r'\bI-(\d{1,3})\b')
FIGURE = re.compile(r'\b(\d[\d,]*(?:-\d[\d,]*)?) (lines|dispatches)\b')


def word_rows(word, read=None, act=None):
    """v1.11.0: a word's cites beyond paths, ledger lines and commits, read as a ruling's are, each row (kind, what, ok): a clause (Rnnn)(k) against that ruling's item (k) in its act's ferry; an instrument I-n against
    PLACE-papers' document; a figure of lines or dispatches against the banks of the act and the act before. read(path relative to the relay) -> text; the banks found by listing data/."""
    read = read or (lambda rel: A.rd(rel[len('data/'):]))
    act = act or A.current().get('act')
    ferries = sorted((f for f in os.listdir(A.D) if re.match(r'^b\d{3}_ferry\.txt$', f)), reverse=True)[:16]
    rows = []
    for rn, k in sorted(set(CLAUSE.findall(word or ''))):
        t = next((x for x in (read('data/' + f) for f in ferries) if ('RULING (R%s) BEGIN' % rn) in x), '')
        rows.append(('clause', '(R%s)(%s)' % (rn, k), bool(re.search(r'(?m)^\(%s\) ' % k, t))))
    try:
        ins = open(os.path.join(os.path.dirname(A.RELAY), 'MY-DOwnloads', 'PLACE-papers', 'phase1.5', 'method', 'INSTRUMENTS.md'), encoding='utf-8', errors='replace').read()
    except OSError:
        ins = ''
    for n in sorted(set(INSTRUMENT.findall(word or ''))):
        rows.append(('instrument', 'I-%s' % n, bool(re.search(r'(?m)^## I-%s\b' % n, ins))))
    acts = (act, 'b%d' % (int(act[1:]) - 1))
    banks = '\n'.join(read('data/' + f) for f in sorted(os.listdir(A.D)) if f[:5] in [x + '_' for x in acts] and f.endswith('.txt') and 'author_answers' not in f and 'ferry' not in f and 'commands' not in f)
    for num, unit in sorted(set(FIGURE.findall(word or ''))):
        rows.append(('figure', '%s %s' % (num, unit), bool(re.search(r'(?<![\d,.])%s(?![\d,])' % re.escape(num), banks))))
    return rows


def ferry_cite(act, needle):
    """the ruling's own number and the top-level item (n) of the act's ferry whose text carries `needle`; None where none does."""
    t = A.rd('%s_ferry.txt' % act)
    r = RUL.search(t or '')
    i = (t or '').find(needle)
    if not r or i < 0:
        return None
    heads = [m for m in TOP.finditer(t) if m.start() <= i]
    return '%s(%s)' % (r.group(1), heads[-1].group(1)) if heads else None


def cite(key, act=None):
    if key in TABLE:
        _a, rul, cl = TABLE[key]
        return rul + cl
    act = act or A.current().get('act')
    return ferry_cite(act, READ[key]) or '(### NOT IN THE FERRY)'


def check(text, act=None):
    """the mirror bank's three citations read from its text by their anchors, against the table: [(key, cited, wanted)] where they differ."""
    anchors = {'mirror.roster': r'THE ROSTER READ FROM PLACE-papers MAIN AT THE BUILD \(((?:\(R\d+\))(?:\(\w+\))*)',
               'mirror.prevbuild': r'named in \(W\) \(((?:\(R\d+\))(?:\(\w+\))*)\)',
               'mirror.manifest': r'### ((?:\(R\d+\))(?:\(\w+\))*)`S MANIFEST CONTROL'}
    out = []
    for k, rx in anchors.items():
        m = re.search(rx, text or '')
        if m and m.group(1) != cite(k, act):
            out.append((k, m.group(1), cite(k, act)))
    return out
