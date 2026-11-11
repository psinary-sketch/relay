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

  python -X utf8 -u tools/standing/subject.py control
  python -X utf8 -u tools/standing/subject.py read <ferry path> <begin marker> <end marker> <spec> [<spec> ...]
"""
import io
import re
import subprocess
import sys

PP = 'D:/MY-DOwnloads/PLACE-papers'
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


def ruling(text, begin, end):
    i = text.find(begin)
    j = text.find(end, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        raise SystemExit('### THE SUBJECT READ: THE RULING`S MARKERS NOT FOUND (%r, %r) -- NOTHING READ' % (begin, end))
    return text[i:j]


def cited(text):
    """{(doc, line)} the ruling cites, ranges expanded: `FINDINGS :10784, :10982 and :11072-:11074`."""
    out = set()
    for m in re.finditer(r'(FINDINGS|INSTRUMENTS)(?:\.md)?((?:,? ?(?:and )?:\d+(?:-:\d+)?)+)', text):
        for a, b in re.findall(r':(\d+)(?:-:(\d+))?', m.group(2)):
            out |= {(m.group(1), n) for n in range(int(a), int(b or a) + 1)}
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


def run(specs, text, hs):
    """dict(hits, uncited, multi, nouns, lines): pure over the specs, the ruling's text and the heads."""
    pats = [pattern(s) for s in specs]
    c = cited(text)
    hits = []
    for d, n, l in hs:
        found = [noun for noun, p in pats if p.search(l)]
        if found:
            hits.append((d, n, (d, n) in c, found, l))
    unc = [h for h in hits if not h[2]]
    multi = [h for h in unc if len(h[3]) >= 2]
    nF = sum(1 for h in hs if h[0] == 'FINDINGS')
    L = ['### THE SUBJECT READ: NOUNS %d ; HEADINGS %d ; ENTRY HEADS %d ; HITS %d ; CITED %d ; UNCITED %d ; MATCHING TWO OR MORE %d' % (
        len(pats), nF, len(hs) - nF, len(hits), len(hits) - len(unc), len(unc), len(multi))]
    for noun, p in pats:
        L.append('   noun %-14s %-30s hits %d, uncited %d' % (noun, '/%s/' % p.pattern, sum(1 for h in hits if noun in h[3]), sum(1 for h in unc if noun in h[3])))
    for d, n, _ok, f, l in sorted(unc, key=lambda h: (len(h[3]) < 2, h[0], h[1])):
        L.append('   %s %s :%d [%s] %s' % ('TWO+' if len(f) >= 2 else '    ', d, n, ', '.join(f), l[:130]))
    return dict(hits=len(hits), uncited={(h[0], h[1]) for h in unc}, multi={(h[0], h[1]) for h in multi}, lines=L)


def control(ferry='D:/relay/data/b752_ferry.txt', pp=PP, ref='HEAD'):
    """(ok, lines): (R362) replayed; the floor's six among the uncited; `class` not matching `classes`."""
    t = ruling(io.open(ferry, encoding='utf-8').read(), 'RULING (R362) BEGIN', 'RULING (R362) END')
    r = run(R362_SPECS, t, heads(ref, pp))
    got = [w for w in FLOOR if w in r['uncited']]
    _n, p = pattern('head:class group=class')
    plural = bool(p.search('the classes of the kernel'))
    ok = len(got) == len(FLOOR) and not plural
    return ok, r['lines'] + ['### THE FLOOR: %d OF %d REACHED%s ; `class` TAKES `classes` %s ; THE CONTROL %s' % (
        len(got), len(FLOOR), '' if len(got) == len(FLOOR) else ' (NOT %s)' % [w for w in FLOOR if w not in got], plural, 'AS WANTED' if ok else 'NOT AS WANTED')]


def main(argv):
    if argv[:1] == ['control']:
        ok, L = control()
        print('\n'.join(L))
        return 0 if ok else 1
    if argv[:1] == ['read'] and len(argv) >= 5:
        t = ruling(io.open(argv[1], encoding='utf-8').read(), argv[2], argv[3])
        print('\n'.join(run(argv[4:], t, heads())['lines']))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
