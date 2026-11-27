# -*- coding: utf-8 -*-
"""tools/b770_li_index.py -- b770, (R380)(6): THE TWO INDEX BANKS READ UNDER W-ORD-LI-INDEX (OPEN_TRAILS :18627). A READING; NOTHING
COMPUTED.

The order names two figures for the least index of a negative Li coefficient at the control: 5938 at the papers` repository's
phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md :344 and 10034 at phase1.5/method/INSTRUMENTS.md :664. (R380)(6) (data/b770_ferry.txt
:29): this tool reads those two lines and the heading of FINDINGS :8881; in the relay reports/2026-08-08-completion-registered-depth.md
:65-:86 and data/b675_li_bench.txt :848 with the lines of that bank that define the quantities it names; and INSTRUMENTS :207-:210 and
:226-:234 for the figure 5101; and prints, for each of the three figures, the sentence that defines the quantity it measures, by path and
line. THE LINES ARE TAKEN BY A SEARCH for the figures and the names beside them (each needle's yield printed; one hit wanted, at the line
the ruling cites); no row of a bank of zeros is read or printed (data/b675_li_bench.txt is searched in its comment lines alone, the lines
opening `###`, so none of its rows by n is read).

THE NAVIGATOR'S READING (data/b770_ferry.txt :29), workspace grade, banked as the navigator's and as no banked figure: 5938 the least index
at which the control's Li coefficient, computed from the arithmetic side, is negative with its sign certified; 10034 the least index at
which a partial sum over 360 certified zeros, with a bound for the rest, is certified below 0; 5101 a detection depth set by a threshold on
magnitude; three quantities, the second at no index below the leading one. Read here by printed predicates on the defining sentences'
words (each a check that can fire, with a planted sentence that fails it): where every predicate holds the tool prints AS READ, the seat's
ground for [I1]; where one does not, NOT AS READ with the figure, the ground for [I2]. The seat reads the sentences by hand beside them.

THE CONTROL OF (6): a planted copy of one cited line with its figure changed is read as differing from the bank (its sha256 against the
line's banked sha256); an unchanged copy reads equal.

  control              the controls with the reading, printed; nothing written
  dry                  the reading, printed; nothing written
  write                the reading banked as data/b770_li_index.txt and .json, after the controls, each AS WANTED

The papers` repository is read at the act's start (78685602, data/act_current.json's pre_pp) by `git show`, each file read again at its
HEAD and compared; no git write; no path of a host's folder printed; git's own messages not printed.
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b770_worklist as K   # noqa: E402

ACT, NL = 'b770', '\n'
PP = K.PP
PP_AT = '78685602'   # ### data/act_current.json pre_pp: the papers` repository at the act's start, the ruling's reads (data/b770_ferry.txt :3)
FERRY = os.path.join(D, 'b770_ferry.txt')
OUT_TXT = os.path.join(D, 'b770_li_index.txt')
OUT_JSON = os.path.join(D, 'b770_li_index.json')
NAV_FROM = "THE NAVIGATOR'S READING, workspace grade, printed here as the navigator's and banked as such: "
NAV_TO = " Where the tool's three sentences agree with that reading"
INSTR = 'phase1.5/method/INSTRUMENTS.md'
ARITY = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md'
REPORT = 'reports/2026-08-08-completion-registered-depth.md'
BENCH = 'data/b675_li_bench.txt'

# ### each cite: (its key, the repository, the path, the needle -- the figure with the name beside it --, the line the ruling or the
# ### seat's read gives it, the range read for its sentence, the comment lines alone where True)
CITES = [
    ('5938.arity', 'pp', ARITY, 'ran to its registered depth and returned **first negative index 5938**', 344, (344, 344), False),
    ('5938.report_head', 'relay', REPORT, 'THE ARITHMETIC-SIDE VALIDATION', 1, (1, 1), False),
    ('5938.report_number', 'relay', REPORT, 'FIRST NEGATIVE INDEX = 5938', 65, (65, 65), False),
    ('5938.report_certified', 'relay', REPORT, 'The sign at 5938 is certified', 82, (82, 86), False),
    ('10034.instruments', 'pp', INSTR, 'least n certified below 0 n_obs = 10034', 664, (664, 664), False),
    ('10034.findings', 'pp', 'FINDINGS.md', 'the certified onset n_obs = 10034', 8881, (8881, 8881), False),
    ('10034.bench_head', 'relay', BENCH, 'P_n over the 360 certified points', 4, (3, 7), True),
    ('10034.bench_line', 'relay', BENCH, 'THE LEAST n WITH P_n + U_n CERTIFIED BELOW 0: 10034', 848, (848, 848), True),
    ('5101.magnitude', 'pp', INSTR, 'n ≈ 5101', 209, (207, 210), False),
    ('5101.depth', 'pp', INSTR, 'n_det = (γ²/δ) × log(threshold × background)', 233, (226, 236), False),
]
# ### the navigator's reading as predicates on the defining sentences' words, by figure: (the cite, the words wanted, case kept)
PREDICATES = {
    '5938': [('5938.arity', 'arithmetic-side'), ('5938.arity', 'first negative index'), ('5938.report_certified', 'is certified')],
    '10034': [('10034.instruments', '360 certified points'), ('10034.instruments', 'U_n'), ('10034.instruments', 'certified below 0'),
              ('10034.bench_head', 'U_n'), ('10034.bench_line', 'CERTIFIED BELOW 0')],
    '5101': [('5101.magnitude', 'magnitude form'), ('5101.magnitude', 'five times the background'), ('5101.depth', 'detection'),
             ('5101.depth', 'threshold')],
}
PRIMARY = {'5938': '5938.arity', '10034': '10034.instruments', '5101': '5101.magnitude'}   # ### the cite each figure's [I1] or [I2] gives
# ### b770 (the first run, 01:28:15Z): the needle of 5938 at its figure and the name beside it alone ('first negative index 5938') yields
# ### two lines of INDEX_ARITY, :344 and :451, the second the edition note v0.18 restating it in other words; the cite's needle carries the
# ### words beside the figure at :344. The wider needle's yield is printed at every run beside the cite's.
WIDE = {'5938.arity': ('first negative index 5938', 'the edition note v0.18 at :451 restating the result')}


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def pp_text(rev, path):
    r = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def relay_text(path):
    try:
        with open(os.path.join(RELAY, path), encoding='utf-8') as f:
            return f.read().replace('\r', '')
    except OSError:
        return None


def search(lines, needle, comments_only):
    """the 1-based lines carrying the needle; with comments_only, the lines opening `###` alone are read."""
    return [i for i, l in enumerate(lines, 1) if (not comments_only or l.lstrip().startswith('###')) and needle in l]


def plain(s):
    return re.sub(r'\s+', ' ', s.replace('**', '').replace('\\*', '*').replace('> ', '')).strip()


def sentence(text, needle):
    """the sentence of the joined range carrying the needle, cut at its ends ('. ' or a heading's bar), or the range whole."""
    t = plain(text)
    k = t.find(plain(needle))
    if k < 0:
        return t[:600]
    a = t.rfind('. ', 0, k)
    b = t.find('. ', k)
    a = 0 if a < 0 else a + 2
    b = len(t) if b < 0 else b + 1
    return t[a:b][:600]


def read_cites(texts):
    """{key: dict(...)} from the texts {(repo, path): (text at the act's start, text at HEAD)}."""
    out = {}
    for key, repo, path, needle, want, rg, com in CITES:
        t0, t1 = texts[(repo, path)]
        L = (t0 or '').split(NL)
        hits = search(L, needle, com)
        line = L[want - 1] if t0 and 0 < want <= len(L) else ''
        rng = NL.join(re.sub(r'^\s*(?:>\s*)?#*\s*', '', l) for l in L[rg[0] - 1:rg[1]]) if t0 else ''
        same = t1 is not None and t0 is not None and (t1.split(NL)[want - 1:want] == L[want - 1:want])
        out[key] = dict(repo=repo, path=path, needle=needle, want=want, hits=hits, at_want=hits == [want], line_sha=sha(line),
                        head_equal=same, sentence=sentence(rng, needle) if t0 else '')
    return out


def reading(cites):
    """(state, rows): AS READ where every predicate holds and 10034 is at no index below 5938; NOT AS READ with the figures failing."""
    rows, failing = [], []
    for fig, preds in PREDICATES.items():
        ok = [(k, w, w in cites[k]['sentence']) for k, w in preds]
        rows.append((fig, ok))
        if not all(x[2] for x in ok):
            failing.append(fig)
    order = 10034 >= 5938
    if not order:
        failing.append('order')
    return ('AS READ' if not failing else 'NOT AS READ', rows, failing, order)


def texts_now():
    T_ = {}
    for _k, repo, path, _n, _w, _r, _c in CITES:
        if (repo, path) in T_:
            continue
        if repo == 'pp':
            T_[(repo, path)] = (pp_text(PP_AT, path), pp_text('HEAD', path))
        else:
            t = relay_text(path)
            T_[(repo, path)] = (t, t)
    return T_


def nav_reading():
    with open(FERRY, encoding='utf-8') as f:
        L = f.read().split(NL)
    s = L[29 - 1]
    a, b = s.find(NAV_FROM), s.find(NAV_TO)
    return (s[a + len(NAV_FROM):b].strip() if 0 <= a < b else None), s.startswith('(6) THE TWO INDEX BANKS READ')


def controls(cites):
    res = []

    def c(name, got, ok):
        res.append((name, got, bool(ok)))

    # ### (6)'s control: a planted copy of one cited line with its figure changed reads as differing from the bank
    tx = texts_now()
    t0 = tx[('pp', ARITY)][0] or ''
    line = t0.split(NL)[344 - 1] if t0 else ''
    planted = line.replace('5938', '5939')
    c('(6)`S CONTROL: a planted copy of the cited line of 5938 (INDEX_ARITY :344) with its figure changed to 5939 reads as differing from '
      'the bank`s sha256 of the line ; an unchanged copy reads equal', (planted != line, sha(planted) == cites['5938.arity']['line_sha'],
                                                                        sha(line) == cites['5938.arity']['line_sha']),
      planted != line and sha(planted) != cites['5938.arity']['line_sha'] and sha(line) == cites['5938.arity']['line_sha'])
    # ### the search: a planted text carrying a needle twice yields two hits (refused at the cite), once yields one
    pl = ['a', 'first negative index 5938 here', 'b', 'again first negative index 5938', '### P_n over the 360 certified points']
    c('the search on planted lines: a needle twice yields 2, a comment needle read with the comment lines alone 1, a needle in a row not '
      'opening ### read with them 0', (search(pl, 'first negative index 5938', False), search(pl, 'P_n over the 360', True),
                                       search(pl, 'first negative index 5938', True)),
      search(pl, 'first negative index 5938', False) == [2, 4] and search(pl, 'P_n over the 360', True) == [5]
      and search(pl, 'first negative index 5938', True) == [])
    # ### the predicates can fire: a planted sentence lacking 'arithmetic-side' reads NOT AS READ at 5938 and nothing else
    pc = json.loads(json.dumps(cites))
    pc['5938.arity']['sentence'] = pc['5938.arity']['sentence'].replace('arithmetic-side', 'zero-side')
    st, _r, fl, _o = reading(pc)
    c('the navigator`s reading read by its predicates on a planted sentence lacking the word arithmetic-side: NOT AS READ at 5938 alone',
      (st, fl), st == 'NOT AS READ' and fl == ['5938'])
    st2, _r2, fl2, _o2 = reading(cites)
    c('the predicates on the sentences as read, printed beside the planted fault (the reading itself, not a control of it)', (st2, fl2),
      st2 in ('AS READ', 'NOT AS READ'))
    # ### the sentence's cut on a planted range
    s = sentence('One thing. The arithmetic-side validation returned first negative index 5938. After.', 'first negative index 5938')
    c('the sentence cut on a planted range: the sentence carrying the needle, its neighbours left out', s,
      s == 'The arithmetic-side validation returned first negative index 5938.')
    nav, at29 = nav_reading()
    c('the navigator`s reading cut from data/b770_ferry.txt :29 between its markers', (at29, (nav or '')[:60]),
      at29 and bool(nav) and nav.startswith('5938 is the least index') and nav.endswith('the second at no index below the leading one.'))
    return res


def run(mode):
    tx = texts_now()
    miss = sorted('%s %s' % k for k, v in tx.items() if v[0] is None)
    if miss:
        sys.exit('### A FILE NOT READ: %s -- NOTHING WRITTEN' % miss)
    cites = read_cites(tx)
    st, rows, failing, order = reading(cites)
    nav, _ = nav_reading()
    res = controls(cites)
    nok = sum(1 for r in res if r[2])
    L = ['b770 -- (R380)(6): THE TWO INDEX BANKS READ UNDER W-ORD-LI-INDEX (OPEN_TRAILS :18627); A READING, NOTHING COMPUTED (%s)' % utc(),
         '',
         '### tools/b770_li_index.py: each line taken by a search for its figure and the name beside it, one hit wanted at the line cited; the',
         '### papers` repository read at %s (the act`s start) and at its HEAD, each cited line compared; data/b675_li_bench.txt searched in its' % PP_AT,
         '### comment lines alone, no row of it read. Each sentence cut from the cited range, its markdown`s stars taken out.',
         '']
    for fig in ('5938', '10034', '5101'):
        L.append('## %s' % fig)
        for key, v in cites.items():
            if key.split('.')[0] != fig:
                continue
            where = ('the papers` repository ' if v['repo'] == 'pp' else 'the relay ') + v['path']
            L.append('  %s :%d -- the needle %r: hits %s, at the cited line %s ; at HEAD %s ; the line`s sha256 %s' % (
                where, v['want'], v['needle'], v['hits'], 'YES' if v['at_want'] else 'NO', 'EQUAL' if v['head_equal'] else 'DIFFERS',
                v['line_sha'][:16]))
            L.append('    "%s"' % v['sentence'])
            if key in WIDE:
                tw = tx[(v['repo'], v['path'])][0] or ''
                L.append('    the wider needle %r alone: hits %s (%s)' % (WIDE[key][0], search(tw.split(NL), WIDE[key][0], False), WIDE[key][1]))
        L.append('')
    L.append("## THE NAVIGATOR'S READING, workspace grade, the navigator's and no banked figure (data/b770_ferry.txt :29)")
    L.append('  "%s"' % nav)
    L.append('')
    L.append('## THE PREDICATES ON THE DEFINING SENTENCES, each a word the navigator`s reading asks of the sentence')
    for fig, ok in rows:
        L.append('  %s: %s' % (fig, ' ; '.join('%s %r %s' % (k.split('.', 1)[1], w, 'HOLDS' if h else 'FAILS') for k, w, h in ok)))
    L.append('  the order: 10034 at no index below 5938: %s' % ('HOLDS' if order else 'FAILS'))
    L.append('')
    L.append('## THE CONTROLS')
    for i, (n, g, ok) in enumerate(res, 1):
        L.append('  (%d) %s: %s -> %s' % (i, n, g, 'AS WANTED' if ok else 'NOT AS WANTED'))
    allhit = all(v['at_want'] and v['head_equal'] for v in cites.values())
    L.append('')
    L.append('### ### **THE READING: %s%s ; CITES %d, EACH ONE HIT AT ITS LINE %s, EACH EQUAL AT HEAD %s ; CONTROLS %d OF %d.**' % (
        st, (' (%s)' % ', '.join(failing)) if failing else '', len(cites), all(v['at_want'] for v in cites.values()),
        all(v['head_equal'] for v in cites.values()), nok, len(res)))
    print(NL.join(L))
    if mode != 'write':
        print('### %s, NOTHING WRITTEN' % mode.upper())
        return 0 if nok == len(res) and allhit else 1
    if nok != len(res) or not allhit:
        sys.exit('### A CONTROL OR A CITE NOT AS WANTED -- NOTHING WRITTEN')
    body = NL.join(L) + NL
    with open(OUT_TXT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
    js = dict(act=ACT, at=utc(), pp_at=PP_AT, reading=st, failing=failing, order=order, navigator=nav,
              cites=dict((k, dict((x, y) for x, y in v.items())) for k, v in cites.items()),
              primary=PRIMARY, controls=[[n, ok] for n, _g, ok in res])
    text = json.dumps(js, indent=1, ensure_ascii=False)
    with open(OUT_JSON, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text + NL)
    print('written data/b770_li_index.txt (%d lines) and data/b770_li_index.json' % len(L))
    return 0


if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else ''
    if m not in ('control', 'dry', 'write'):
        sys.exit('usage: b770_li_index.py control|dry|write')
    sys.exit(run(m))
