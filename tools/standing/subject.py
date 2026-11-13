# -*- coding: utf-8 -*-
"""standing/subject.py -- v1.33.0, (R363)(7)(i), widening data/b752_rules.txt (12): THE SUBJECT READ.

Before a ruling orders a measurement, plans a build or calls a statement new, the navigator searches the mirror's FINDINGS headings and
INSTRUMENTS entries for the object's nouns and cites what it finds in the ruling's SCOPE READ; at step zero the seat runs the same search from
the ruling's own nouns over FINDINGS' `## ` headings and INSTRUMENTS' `## I-` entry heads at PLACE-papers HEAD and prints every hit the ruling
does not cite, before the citation check. The rule as the navigator restated it at b753 (option 1, 2026-11-11):

  THE MATCH   a word noun by its stem, case ignored, at a word's start (word:<noun>=<stem>); a noun of several words by its head word as a whole
              word, case ignored (head:<noun>=<head word>: `class` takes `class` and not `classes`, b753 defect (k)); a symbol noun as written, case
              kept, at a token's start, up to its opening bracket and the letter after it (sym:b(n) takes `b(n`).
  THE PRINT   every hit the ruling does not cite, those matching two or more nouns first, each noun's count.
  THE CONTROL a floor: (R362) replayed from cQ, negative and class group (with b(n), c(n)) reaches FINDINGS :10858, :11072, :11178, :11359 and
              INSTRUMENTS :750, :758 among its uncited hits. The seat's count is the rule ((R363)-amendment (2): 39 at b753's HEAD).

Sorted by the author's word of 2026-10-18 (data/b682_author_answers.txt :13): the seat's half (this run, printed before the citation check)
TRACEABLE; the navigator's half (the search before a ruling goes out) PROSE (data/b753_stepzero.txt). Reads only; writes nothing.

v1.34.0, (R364)(3)(vii) and the amendment row 3 (2) of data/b754_amendments.json: THE CORPUS WIDENED. Beside FINDINGS' `## ` headings and
INSTRUMENTS' entry heads the read takes (a) the reference layer's level-three headings, FINDINGS :762-:1096 (76 at b754), each with the bold
line beneath it (the first line not blank within three, where it opens `**`); (b) the standing clauses, data/standing_clauses_v9.txt, every line;
(c) the rules banks, data/b*_rules.txt, every line; (d) the lock gate's own rules, the lines of tools/b378_lockgate.py citing a ruling's clause;
(e) the head lines -- the opening line and every line opening `#` -- of the relay's banks of four kinds by name: data/*_derivation.txt,
*_registrations.txt, *_coeffs.txt and *_literature.txt. The relay's are read from its HEAD's blobs. A relay hit prints as `relay:<path> :<line>`.
`quote=False` prints a hit by place and nouns alone (a bank's print, where a line of the reference layer may be one [Q]'s row (3) protects);
the controls and the read print so, the read quoting only with --quote. A relay path the ruling names is read as cited: with its lines, those
lines; with none, the file whole. The controls (`control_corpus`): (R363) replayed with its (9)'s noun, the standing version, reaching
(R345)(2)(iv) where the relay holds it (data/b748_rules.txt :9, tools/b378_lockgate.py :237); "minimal negative" and "class number 3" reaching
data/b721_derivation.txt; two-leg reaching FINDINGS :901 and :979, simplicity :904, a planted noun nothing; each against the corpus before.

  python -X utf8 -u tools/standing/subject.py control
  python -X utf8 -u tools/standing/subject.py read <ferry path> <begin marker> <end marker> <spec> [<spec> ...] [--quote]
"""
import io
import re
import subprocess
import sys

PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = 'D:/relay'
LAYER = (762, 1096)   # ### the reference layer, FINDINGS :762-:1096 ((R364)(3)(vii), the amendment row 3 (2)); a re-cut of [A] replaces a line by a line
FOUR_KINDS = ('derivation', 'registrations', 'coeffs', 'literature')
RULE_CITE = re.compile(r'\(R\d+\)\(')
FLOOR = (('FINDINGS', 10858), ('FINDINGS', 11072), ('FINDINGS', 11178), ('FINDINGS', 11359), ('INSTRUMENTS', 750), ('INSTRUMENTS', 758))
R362_SPECS = ('sym:cQ', 'word:negative=negativ', 'head:class group=class', 'sym:b(n)', 'sym:c(n)')


def blob(path, ref='HEAD', pp=PP):
    r = subprocess.run(['git', '-C', pp, 'cat-file', '-p', '%s:%s' % (ref, path)], capture_output=True)
    if r.returncode:
        raise SystemExit('### THE SUBJECT READ: %s:%s UNREADABLE (exit %d: %s) -- NOTHING READ' % (ref, path, r.returncode, r.stderr.decode('utf-8', 'replace').strip()[:160]))
    return r.stdout.decode('utf-8', 'replace').replace('\r', '').split('\n')


def heads(ref='HEAD', pp=PP):
    """[(doc, line, text)]: FINDINGS' `## ` headings and INSTRUMENTS' `## I-` entry heads at the ref."""
    F = blob('FINDINGS.md', ref, pp)
    I = blob('phase1.5/method/INSTRUMENTS.md', ref, pp)
    return [('FINDINGS', i, l) for i, l in enumerate(F, 1) if l.startswith('## ')] + [('INSTRUMENTS', i, l) for i, l in enumerate(I, 1) if l.startswith('## I-')]


def layer(ref='HEAD', pp=PP, bounds=LAYER):
    """[(doc, line, text)]: the reference layer's `### ` headings in FINDINGS :a-:b and the bold line beneath each (the first line not blank
    within three after it, where that line opens `**`); (items, headings, bold lines found)."""
    F = blob('FINDINGS.md', ref, pp)
    a, b = bounds
    out, nh, nb = [], 0, 0
    for i in range(a, min(b, len(F)) + 1):
        l = F[i - 1]
        if not l.startswith('### '):
            continue
        nh += 1
        out.append(('FINDINGS', i, l))
        for j in range(i + 1, min(i + 4, len(F) + 1)):
            if F[j - 1].strip():
                if F[j - 1].startswith('**'):
                    nb += 1
                    out.append(('FINDINGS', j, F[j - 1]))
                break
    return out, nh, nb


def _relay(args, relay=RELAY):
    r = subprocess.run(['git', '-C', relay] + list(args), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def relay_items(rref='HEAD', relay=RELAY):
    """[(doc, line, text)] of the relay at rref, and {source: count}: (b) the standing clauses, (c) the rules banks, (d) the lock gate's rule
    lines, (e) the head lines of the banks of four kinds."""
    names = (_relay(['ls-tree', '-r', '--name-only', rref, '--', 'data/', 'tools/b378_lockgate.py'], relay) or '').split('\n')
    pick = []
    for n in names:
        base = n.rsplit('/', 1)[-1]
        if n == 'data/standing_clauses_v9.txt':
            pick.append((n, 'clauses'))
        elif re.match(r'^data/b\d+_rules\.txt$', n):
            pick.append((n, 'rules'))
        elif n == 'tools/b378_lockgate.py':
            pick.append((n, 'lockgate'))
        elif n.startswith('data/') and '/' not in n[5:] and any(base.endswith('_%s.txt' % k) for k in FOUR_KINDS):
            pick.append((n, 'heads'))
    out, by = [], {}
    for n, kind in pick:
        t = _relay(['show', '%s:%s' % (rref, n)], relay)
        if t is None:
            continue
        rows = []
        for i, l in enumerate(t.split('\n'), 1):
            if kind in ('clauses', 'rules') and l.strip():
                rows.append(i)
            elif kind == 'lockgate' and RULE_CITE.search(l):
                rows.append(i)
            elif kind == 'heads' and (i == 1 or l.startswith('#')) and l.strip():
                rows.append(i)
        L = t.split('\n')
        out += [('relay:' + n, i, L[i - 1]) for i in rows]
        by[kind] = by.get(kind, 0) + len(rows)
        by[kind + ' files'] = by.get(kind + ' files', 0) + 1
    return out, by


def corpus(ref='HEAD', pp=PP, rref='HEAD', relay=RELAY):
    """(items, figures): v1.34.0's corpus whole -- the headings and entry heads, the reference layer with its bold lines, the relay's four sources."""
    hs = heads(ref, pp)
    ly, nh, nb = layer(ref, pp)
    ri, by = relay_items(rref, relay)
    fig = dict(headings=sum(1 for h in hs if h[0] == 'FINDINGS'), entry_heads=sum(1 for h in hs if h[0] == 'INSTRUMENTS'), layer_headings=nh,
               layer_bold=nb, **dict((k.replace(' ', '_'), v) for k, v in by.items()))
    return hs + ly, fig, ri


def ruling(text, begin, end):
    i = text.find(begin)
    j = text.find(end, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        raise SystemExit('### THE SUBJECT READ: THE RULING`S MARKERS NOT FOUND (%r, %r) -- NOTHING READ' % (begin, end))
    return text[i:j]


RELAY_CITE = re.compile(r'(?<![A-Za-z0-9_./-])((?:data|tools)/[A-Za-z0-9_./-]*[A-Za-z0-9_-]\.(?:txt|py|json|md))((?:,? ?(?:and )?:\d+(?:-:\d+)?)*)')


def cited(text):
    """{(doc, line)} the ruling cites, ranges expanded: `FINDINGS :10784, :10982 and :11072-:11074`; v1.34.0, a relay path's lines
    (`data/b713_coeffs.txt :13-:14`) as ('relay:<path>', n), and a relay path named with no line as ('relay:<path>', None), the file whole."""
    out = set()
    for m in re.finditer(r'(FINDINGS|INSTRUMENTS)(?:\.md)?((?:,? ?(?:and )?:\d+(?:-:\d+)?)+)', text):
        for a, b in re.findall(r':(\d+)(?:-:(\d+))?', m.group(2)):
            out |= {(m.group(1), n) for n in range(int(a), int(b or a) + 1)}
    for m in RELAY_CITE.finditer(text):
        d = 'relay:' + m.group(1)
        pairs = re.findall(r':(\d+)(?:-:(\d+))?', m.group(2))
        if not pairs:
            out.add((d, None))
        for a, b in pairs:
            out |= {(d, n) for n in range(int(a), int(b or a) + 1)}
    return out


def pattern(spec):
    kind, _, rest = spec.partition(':')
    noun, _, key = rest.partition('=')
    if kind == 'word':
        return noun, re.compile(r'(?<![A-Za-z0-9])' + re.escape(key or noun), re.I)
    if kind == 'head':
        return noun, re.compile(r'(?<![A-Za-z0-9])' + re.escape(key or noun) + r'(?![A-Za-z0-9])', re.I)
    if kind == 'sym':
        sym = noun[:noun.index('(') + 2] if '(' in noun else noun
        return noun, re.compile(r'(?<![A-Za-z0-9])' + re.escape(sym))
    raise SystemExit('### THE SUBJECT READ: A SPEC OF NO KIND: %s (word:, head:, sym:)' % spec)


def run(specs, text, hs, quote=True, fig=None):
    """dict(hits, hit, uncited, multi, lines): pure over the specs, the ruling's text and the items. v1.34.0: an item of the relay counted
    apart; `quote=False` prints each uncited hit by its place and nouns and no word of its line; `fig` the corpus's figures, printed."""
    pats = [pattern(s) for s in specs]
    c = cited(text)
    hits = []
    for d, n, l in hs:
        found = [noun for noun, p in pats if p.search(l)]
        if found:
            hits.append((d, n, (d, n) in c or (d, None) in c, found, l))
    unc = [h for h in hits if not h[2]]
    multi = [h for h in unc if len(h[3]) >= 2]
    nF = sum(1 for h in hs if h[0] == 'FINDINGS')
    nI = sum(1 for h in hs if h[0] == 'INSTRUMENTS')
    nR = len(hs) - nF - nI
    L = ['### THE SUBJECT READ: NOUNS %d ; HEADINGS %d ; ENTRY HEADS %d%s ; HITS %d ; CITED %d ; UNCITED %d ; MATCHING TWO OR MORE %d%s' % (
        len(pats), nF, nI, ' ; RELAY LINES %d' % nR if nR else '', len(hits), len(hits) - len(unc), len(unc), len(multi),
        '' if quote else ' ; PRINTED BY PLACE, NO LINE QUOTED')]
    if fig:
        L.append('   THE CORPUS: ' + ' ; '.join('%s %d' % (k.replace('_', ' '), v) for k, v in sorted(fig.items())))
    for noun, p in pats:
        L.append('   noun %-14s %-30s hits %d, uncited %d' % (noun, '/%s/' % p.pattern, sum(1 for h in hits if noun in h[3]), sum(1 for h in unc if noun in h[3])))
    for d, n, _ok, f, l in sorted(unc, key=lambda h: (len(h[3]) < 2, h[0], h[1])):
        L.append('   %s %s :%d [%s]%s' % ('TWO+' if len(f) >= 2 else '    ', d, n, ', '.join(f), ' ' + l[:130] if quote else ''))
    return dict(hits=len(hits), hit={(h[0], h[1]) for h in hits}, uncited={(h[0], h[1]) for h in unc}, multi={(h[0], h[1]) for h in multi},
                cited_hits={(h[0], h[1]) for h in hits if h[2]}, lines=L)


def control(ferry='D:/relay/data/b752_ferry.txt', pp=PP, ref='HEAD'):
    """(ok, lines): (R362) replayed; the floor's six among the uncited; `class` not matching `classes`."""
    t = ruling(io.open(ferry, encoding='utf-8').read(), 'RULING (R362) BEGIN', 'RULING (R362) END')
    r = run(R362_SPECS, t, heads(ref, pp), quote=False)
    got = [w for w in FLOOR if w in r['uncited']]
    _n, p = pattern('head:class group=class')
    plural = bool(p.search('the classes of the kernel'))
    ok = len(got) == len(FLOOR) and not plural
    return ok, r['lines'] + ['### THE FLOOR: %d OF %d REACHED%s ; `class` TAKES `classes` %s ; THE CONTROL %s' % (
        len(got), len(FLOOR), '' if len(got) == len(FLOOR) else ' (NOT %s)' % [w for w in FLOOR if w not in got], plural, 'AS WANTED' if ok else 'NOT AS WANTED')]


PLANTED = 'head:planted noun=qzxwvplanted'


def _state(r, w):
    return ('HIT, CITED' if w in r['cited_hits'] else 'HIT, UNCITED') if w in r['hit'] else 'NO HIT'


def control_corpus(ferry753='D:/relay/data/b753_ferry.txt', ferry754='D:/relay/data/b754_ferry.txt', pp=PP, ref='HEAD', relay=RELAY, rref='HEAD'):
    """(ok, lines): v1.34.0's controls, (R364)(3)(vii) and the amendment row 3 (2), each over the corpus before (the `## ` headings and the
    entry heads alone) and after (the corpus whole); every hit printed by its place, no line quoted."""
    old = heads(ref, pp)
    items, fig, ri = corpus(ref, pp, rref, relay)
    new = items + ri
    t363 = ruling(io.open(ferry753, encoding='utf-8').read(), 'RULING (R363) BEGIN', 'RULING (R363) END')
    t364 = ruling(io.open(ferry754, encoding='utf-8').read(), 'RULING (R364) BEGIN', 'RULING (R364) END')
    L = ['### THE SUBJECT READ`S CORPUS, v1.34.0: ' + ' ; '.join('%s %d' % (k.replace('_', ' '), v) for k, v in sorted(fig.items())), ]
    res = []

    def case(name, want_text, got_text, ok):
        res.append(ok)
        L.append('   CASE %-28s WANTED %s ; READ %s -- %s' % (name, want_text, got_text, 'AS WANTED' if ok else 'NOT AS WANTED'))

    # (1) (R363) replayed with the noun of its (9), the standing version: the rule it missed, (R345)(2)(iv), where the relay holds it
    sp = ('head:standing version=version',)
    a, b = run(sp, t363, old, quote=False), run(sp, t363, new, quote=False)
    W = (('relay:data/b748_rules.txt', 9), ('relay:tools/b378_lockgate.py', 237))
    case('(R363)(9) -> (R345)(2)(iv)', 'the rules bank`s row and the lock gate`s rule line uncited hits after, no hit before',
         'before %s ; after %s ; hits before %d, after %d' % ([_state(a, w) for w in W], [_state(b, w) for w in W], a['hits'], b['hits']),
         all(w in b['uncited'] for w in W) and not any(w in a['hit'] for w in W))
    # (2) the nouns of (R364)(2)(ii): data/b721_derivation.txt a hit
    sp = ('head:minimal negative=minimal', 'head:class number 3=class')
    a, b = run(sp, t363, old, quote=False), run(sp, t363, new, quote=False)
    ha = sorted(n for d, n in a['hit'] if d == 'relay:data/b721_derivation.txt')
    hb = sorted((n, _state(b, ('relay:data/b721_derivation.txt', n))) for d, n in b['hit'] if d == 'relay:data/b721_derivation.txt')
    case('minimal negative, class no. 3', 'data/b721_derivation.txt a hit after, none before', 'before %s ; after %s' % (ha, hb), bool(hb) and not ha)
    # (3) row 3 (2): two-leg at :901 and :979, the bold lines beneath the anchors at :900 and :978
    sp = ('head:two-leg',)
    a, b = run(sp, t364, old, quote=False), run(sp, t364, new, quote=False)
    W = (('FINDINGS', 901), ('FINDINGS', 979))
    case('row 3 (2) two-leg', 'FINDINGS :901 and :979 hits after, neither before',
         'before %s ; after %s' % ([_state(a, w) for w in W], [_state(b, w) for w in W]), all(w in b['hit'] for w in W) and not any(w in a['hit'] for w in W))
    two_leg = b
    # (4) row 3 (2): simplicity at the anchor :904
    sp = ('word:simplicity=simplicit',)
    a, b = run(sp, t364, old, quote=False), run(sp, t364, new, quote=False)
    w = ('FINDINGS', 904)
    case('row 3 (2) simplicity', 'FINDINGS :904 a hit after, none before', 'before %s ; after %s' % (_state(a, w), _state(b, w)), w in b['hit'] and w not in a['hit'])
    # (5) row 3 (2): a planted noun standing in no anchor -- no hit in the layer, nor in the corpus whole
    ly = [x for x in items if x[0] == 'FINDINGS' and LAYER[0] <= x[1] <= LAYER[1]]
    p1, p2 = run((PLANTED,), t364, ly, quote=False), run((PLANTED,), t364, new, quote=False)
    case('row 3 (2) planted noun', 'no hit in the layer`s %d items nor in the corpus`s %d' % (len(ly), len(new)), 'hits %d and %d' % (p1['hits'], p2['hits']),
         p1['hits'] == 0 and p2['hits'] == 0)
    # (6) the layer's headings as the amendment row 3 (2) counts them
    case('the layer`s headings', '76 `### ` headings in FINDINGS :762-:1096, each with a bold line', 'headings %d ; bold lines %d' % (fig['layer_headings'], fig['layer_bold']),
         fig['layer_headings'] == 76 and fig['layer_bold'] == 76)
    # (7) the floor of (R362) over the corpus whole: the six still among the uncited
    r = run(R362_SPECS, ruling(io.open('D:/relay/data/b752_ferry.txt', encoding='utf-8').read(), 'RULING (R362) BEGIN', 'RULING (R362) END'), new, quote=False)
    got = [x for x in FLOOR if x in r['uncited']]
    case('the floor over the corpus whole', '6 of 6 among the uncited', '%d of %d ; hits %d' % (len(got), len(FLOOR), r['hits']), len(got) == len(FLOOR))
    # (8) the print by place: with quote=False no hit's words in the print; with quote=True the same hits' words there (the guard's own control)
    q = run(('head:two-leg',), '', new, quote=True)
    frag = [l[:40] for d, n, l in new if (d, n) in q['hit'] and len(l.strip()) >= 20]
    nq = run(('head:two-leg',), '', new, quote=False)
    leak = sum(1 for f in frag if any(f in x for x in nq['lines']))
    shown = sum(1 for f in frag if any(f in x for x in q['lines']))
    case('the print by place', 'quote off: 0 of the hits` words printed ; quote on: all', 'off %d of %d ; on %d of %d' % (leak, len(frag), shown, len(frag)),
         bool(frag) and leak == 0 and shown == len(frag))
    ok = all(res)
    L.append('### THE CORPUS`S CONTROLS: %d OF %d AS WANTED ; %s' % (sum(res), len(res), 'AS WANTED' if ok else 'NOT AS WANTED'))
    return ok, L


def main(argv):
    if argv[:1] == ['control']:
        ok, L = control()
        ok2, L2 = control_corpus()
        print('\n'.join(L + L2))
        return 0 if ok and ok2 else 1
    if argv[:1] == ['read'] and len(argv) >= 5:
        quote = '--quote' in argv
        argv = [a for a in argv if a != '--quote']
        t = ruling(io.open(argv[1], encoding='utf-8').read(), argv[2], argv[3])
        items, fig, ri = corpus()
        print('\n'.join(run(argv[4:], t, items + ri, quote=quote, fig=fig)['lines']))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
