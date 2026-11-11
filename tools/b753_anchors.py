# -*- coding: utf-8 -*-
"""b753_anchors.py -- (R363)(5)(iv): THE REFERENCE LAYER'S ANCHORS READ, data/b753_anchors.txt.

FINDINGS' sections I to III (:762 to :1083) carry the stable anchors, each a sentence with its tag, and the layer's own rule for how one
moves (:1084-:1094: the tag edited in place, or the entry marked RETIRED with its reason). For each anchor: its sentence and tag quoted; the
later ledger lines that bear on it, found by the searches below and printed; and a verdict from the printed rule. Read from PLACE-papers at
HEAD by `git show`; no remote read; no anchor is edited: each one moved is carried to the sitting.

THE SEARCHES, over the ledgers outside the layer (FINDINGS before :762 and after :1094; ERRATA whole; REGISTRY's ceiling lines from :951 on):
  (S1) the anchor's slug as written, in any line
  (S2) the slug as an identifier (its hyphens as underscores), in any line, where the slug has two parts or more
  (S3) a document the anchor's tag line names (a name in capitals with an underscore, its version apart), in a heading of FINDINGS or ERRATA
       or in a ceiling line
  (S4) a kernel the anchor names (SIDE-<name>), in a heading of ERRATA
  (S5) every content word of the slug (five letters or more, a stop list apart; two words or more), each as a whole word, in a heading of
       FINDINGS after :1094
  and the tier block of each document the anchor names, found in the tree by its name: its TIER line quoted by its tier alone.
THE RULE, a lexical one: its verdicts are candidates for the sitting, each citing its line.
  MOVED BY A LATER LINE     (a) the anchor's own sentence says what a later ledger line names as not supportable or reworded: the phrases
                            REGISTRY's ceiling lines list after "Not supportable" (read from the lines), a proof of RH said complete, or the
                            wording "two-leg" (REGISTRY :153, :492-:496); or (b) a line found by (S1)-(S5) carries a moving word (RETIRED,
                            refuted, withdrawn, retracted, superseded, STIPULATION, not compiled, not proved, not supportable, named
                            premise, open premise, equivalent to RH, restated) within 240 characters of the key found, an act's own
                            score (a word standing straight after N1-N8) apart; a line found
                            by (S4) alone moves only where it and the anchor's sentence share a named route or a backticked name
  STANDS                    later lines found, none of them moving by (a) or (b)
  NO LATER LINE FOUND       the searches found none

  python -X utf8 -u tools/b753_anchors.py control      the controls alone
  python -X utf8 -u tools/b753_anchors.py run          the controls, the navigator's four, the table, the bank
"""
import io
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import outbound

ACT = 'b753'
PP = 'D:/MY-DOwnloads/PLACE-papers'
BANK = os.path.join(RELAY, 'data', '%s_anchors.txt' % ACT)
LAYER = (762, 1083)
RULE = (1084, 1094)
CEILING_FROM = 951
MOVING = re.compile(r'RETIRED|\brefuted\b|REFUTED|\bwithdrawn\b|\bretracted\b|\bsuperseded\b|STIPULATION|\bnot compiled\b|\bnot proved\b|[Nn]ot supportable|'
                    r'\bnamed premise\b|\bopen premise\b|equivalent to RH\b|\brestated\b')
OLD = re.compile(r'\btwo[- ]leg', re.I)
RH_DONE = re.compile(r'\bRH proved\b|\bproof of RH\b[^.]{0,40}\bcomplete\b', re.I)
STOP = set('''with from that this theorem theorems equals have into over under than then when where which draft pending state verified'''.split())
NAV = (('riemann-hypothesis', 901, 'beside REGISTRY :953 and ERRATA :486'), ('two-leg-completeness', 979, 'beside REGISTRY :953 and ERRATA :486'),
       ('conservation-of-spectra', 897, 'beside FINDINGS :5924'), ('simplicity-riemann-zeros', 905, 'beside FINDINGS :6862'))


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def show(path, rev='HEAD'):
    r = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (rev, path)], capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode:
        raise SystemExit('### NOT READ: PLACE-papers %s:%s' % (rev, path))
    return r.stdout.split('\n')


def anchors(F):
    """[dict(line, slug, section, sentence_line, sentence, tag_line, tag, tags)] of the layer."""
    out, sec = [], None
    i = LAYER[0] - 1
    while i < LAYER[1]:
        l = F[i]
        if l.startswith('## '):
            sec = l[3:].strip()
        if l.startswith('### '):
            j, sent, sline, tag, tline = i + 1, [], None, None, None
            while j < LAYER[1] and not F[j].startswith('### ') and not F[j].startswith('## '):
                s = F[j].strip()
                if s and s != '---':
                    if re.match(r'^\*[^*]', s) and tag is None:
                        tag, tline = s, j + 1
                    elif tag is None:
                        sent.append(s)
                        sline = sline or j + 1
                j += 1
            m = re.match(r'^\*([^*]+)\*', tag or '')
            out.append(dict(line=i + 1, slug=l[4:].strip(), section=sec, sentence_line=sline, sentence=' '.join(sent), tag_line=tline, tag=tag or '',
                            tags=[x.strip() for x in m.group(1).split('·')] if m else []))
            i = j
            continue
        i += 1
    return out


def not_supportable(R):
    """[(line, phrase)]: the phrases REGISTRY's ceiling lines list after 'Not supportable', each between asterisks."""
    out = []
    for i in range(CEILING_FROM - 1, len(R)):
        m = re.search(r'Not supportable[^:]*:(.*)$', R[i])
        if m:
            out += [(i + 1, p.strip()) for p in re.findall(r'\*([^*]+)\*', m.group(1))]
    return out


def docs_named(tag):
    """the documents a tag line names: names in capitals carrying an underscore, a version suffix apart."""
    out = []
    for m in re.finditer(r'(?<![A-Za-z0-9_`./])([A-Z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+)', tag.split('—', 1)[-1] if '—' in tag else ''):
        n = re.sub(r'(_v\d+(?:_\d+)*)$', '', m.group(1))
        if n not in out and len(n) >= 6:
            out.append(n)
    return out


def kernels_named(a):
    return sorted(set(re.findall(r'\bSIDE-[a-z0-9]+(?:-[a-z0-9]+)*', a['sentence'] + ' ' + a['tag'])))


def slug_words(slug):
    out = []
    for w in slug.split('-'):
        if len(w) >= 5 and w not in STOP and w not in out:
            out.append(w)
    return out


def wordre(s):
    return re.compile(r'(?<![A-Za-z0-9_#-])%s(?![A-Za-z0-9_-])' % re.escape(s))


def search(a, F, E, R):
    """[(ledger, line, key, text)] by (S1)-(S5)."""
    hits, seen = [], set()

    def add(ledger, n, key, text, pos):
        if (ledger, n) not in seen:
            seen.add((ledger, n))
            hits.append((ledger, n, key, text, pos))

    def at(rx_list, l):
        return [m.start() for rx in rx_list for m in rx.finditer(l)]
    s1 = re.compile(r'(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])' % re.escape(a['slug']))
    ident = a['slug'].replace('-', '_')
    s2 = wordre(ident) if a['slug'].count('-') >= 1 else None
    docs = [re.compile(r'(?<![A-Za-z0-9])%s(?![A-Za-z])' % re.escape(d), re.I) for d in docs_named(a['tag'])]
    kern = [wordre(k) for k in kernels_named(a)]
    sw = [re.compile(r'(?<![A-Za-z0-9])%s(?![A-Za-z0-9])' % re.escape(w), re.I) for w in slug_words(a['slug'])]
    for name, L in (('FINDINGS', F), ('ERRATA', E), ('REGISTRY', R)):
        for i, l in enumerate(L):
            n = i + 1
            if name == 'FINDINGS' and LAYER[0] <= n <= RULE[1]:
                continue
            if name == 'REGISTRY' and n < CEILING_FROM:
                continue
            if name == 'REGISTRY' and 'CEILING LINE' not in l and 'Supportable' not in l and 'supportable' not in l:
                continue
            head = l.startswith('#') or name == 'REGISTRY'
            if s1.search(l):
                add(name, n, 'S1', l, at([s1], l))
            elif s2 is not None and s2.search(l):
                add(name, n, 'S2', l, at([s2], l))
            elif head and any(d.search(l) for d in docs):
                add(name, n, 'S3', l, at(docs, l))
            elif name == 'ERRATA' and l.startswith('#') and any(k.search(l) for k in kern):
                add(name, n, 'S4', l, at(kern, l))
            elif name == 'FINDINGS' and n > RULE[1] and l.startswith('## ') and len(sw) >= 2 and all(w.search(l) for w in sw):
                add(name, n, 'S5', l, at(sw, l))
    return hits


NEAR = 240
SHARED = re.compile(r'\bRoute \d\b|`[^`]{3,}`')
SCORE = re.compile(r'\bN\d\s+$')


def moving_near(text, pos):
    """the moving word of the line standing within NEAR characters of a found key, or None."""
    for m in MOVING.finditer(text):
        if SCORE.search(text[:m.start()]):
            continue  # an act's own score ("N4 REFUTED") is a word about the act, not about the anchor
        if any(abs(m.start() - p) <= NEAR for p in pos):
            return m.group(0)
    return None


def verdict(a, hits, NS):
    """(verdict, the moving lines [(ledger, line, why)])."""
    mv = []
    for n, p in NS:
        if re.search(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(p), a['sentence'], re.I) and not any(x[1] == n for x in mv):
            mv.append(('REGISTRY', n, 'the sentence says "%s", listed there as not supportable' % p))
    if RH_DONE.search(a['sentence']) and not mv:
        mv += [('REGISTRY', n, 'the sentence says RH proved or its proof complete; "%s" listed there as not supportable' % p) for n, p in NS if p.lower() == 'rh proved'][:1]
    if OLD.search(a['sentence']):
        mv.append(('REGISTRY', 153, 'the sentence carries "two-leg", reworded 2026-07-23 (REGISTRY :153, :492-:496)'))
    for led, n, key, text, pos in hits:
        w = moving_near(text, pos)
        if not w:
            continue
        if key == 'S4':
            share = sorted(set(SHARED.findall(a['sentence'])) & set(SHARED.findall(text)))
            if not share:
                continue
            mv.append((led, n, 'S4, the line carrying "%s" and sharing %s with the sentence' % (w, ', '.join(share))))
        else:
            mv.append((led, n, '%s, the line carrying "%s" within %d characters of the key' % (key, w, NEAR)))
    if mv:
        return 'MOVED BY A LATER LINE', mv
    return ('STANDS', []) if hits else ('NO LATER LINE FOUND', [])


def tier_of(doc, tree):
    """(path, the tier letter or None) of a document found in the tree by its name; (None, None) where no file carries the name."""
    c = [p for p in tree if p.endswith('.md') and re.match(r'%s(_v\d+(_\d+)*)?\.md$' % re.escape(doc), p.split('/')[-1], re.I)]
    if not c:
        return None, None
    p = sorted(c, key=lambda x: (len(x.split('/')[-1]), x))[-1]
    for l in show(p)[:60]:
        m = re.search(r'TIER\s+([KCNE])\b', l)
        if m:
            return p, m.group(1)
    return p, None


def q(s, n=300):
    s = s if len(s) <= n else s[:n] + ' [...]'
    return '[WITHHELD: carries an identifier by form]' if outbound.identifiers_in(s) else '"%s"' % s


def load():
    return show('FINDINGS.md'), show('ERRATA.md'), show('REGISTRY.md')


def controls(F, E, R):
    L, ok = [], True

    def case(what, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    A = anchors(F)
    case('(the layer) FINDINGS :762-:1083: (anchors, sections, each with a sentence and a tag line)',
         (len(A), len(set(a['section'] for a in A)), all(a['sentence'] and a['tag'] for a in A)), (76, 3, True))
    case('(the layer) the four the navigator names stand at their lines', [(a['slug'], a['sentence_line']) for a in A if a['slug'] in dict((n[0], 1) for n in NAV)],
         [('conservation-of-spectra', 897), ('riemann-hypothesis', 901), ('simplicity-riemann-zeros', 905), ('two-leg-completeness', 979)])
    case('(the layer`s rule) :1084 its heading, :1094 the RETIRED form', (F[1083].strip(), 'RETIRED' in F[1093]), ('## How findings move', True))
    NS = not_supportable(R)
    case('(the ceiling lines) the phrases listed as not supportable include RH proved and h2_sign proved, the earliest at :955',
         ('RH proved' in [p for _n, p in NS], 'h2_sign proved' in [p for _n, p in NS], min(n for n, _p in NS)), (True, True, 955))
    fa = dict(slug='planted-anchor-one', sentence='X is s-dark.', tag='*theorem-supported* — PLANTED_DOCUMENT v1.0. Kernel: SIDE-planted.', tags=['theorem-supported'])
    FF = [''] * 1100 + ['## A later heading on PLANTED_DOCUMENT', 'a body line naming planted-anchor-one, RETIRED there', 'a line naming planted_anchor_one alone']
    h = search(fa, FF, ['## E-1 -- SIDE-planted at v1'], [''] * 960)
    case('(the searches) a planted anchor: S3 in a later heading, S1 and S2 in body lines, S4 in an ERRATA heading', sorted(x[:3] for x in h),
         [('ERRATA', 1, 'S4'), ('FINDINGS', 1101, 'S3'), ('FINDINGS', 1102, 'S1'), ('FINDINGS', 1103, 'S2')])
    case('(the rule) the planted anchor with its RETIRED line; with that line removed; with no later line',
         (verdict(fa, h, [])[0], verdict(fa, [x for x in h if x[1] != 1102], [])[0], verdict(fa, [], [])[0]), ('MOVED BY A LATER LINE', 'STANDS', 'NO LATER LINE FOUND'))
    case('(the rule) a planted sentence saying RH proved, and one carrying the older wording, no later line beside either',
         (verdict(dict(fa, sentence='RH proved, scoped.'), [], [(955, 'RH proved')])[0], verdict(dict(fa, sentence='Complete in the two-leg sense.'), [], [])[0]),
         ('MOVED BY A LATER LINE', 'MOVED BY A LATER LINE'))
    far = [''] * 1100 + ['a line naming planted-anchor-one ' + 'x' * 600 + ' and far along it something else RETIRED']
    case('(the rule) a moving word 600 characters from the slug in one long line does not move it', verdict(fa, search(fa, far, [], [''] * 960), [])[0], 'STANDS')
    sc = [''] * 1100 + ['a line naming planted-anchor-one beside an act`s score, N4 REFUTED -- four parts sent in one call']
    case('(the rule) an act`s score beside the slug ("N4 REFUTED") does not move it; the slug of a repeated word has one content word',
         (verdict(fa, search(fa, sc, [], [''] * 960), [])[0], slug_words('imo-ai-twelve-of-twelve')), ('STANDS', ['twelve']))
    e4 = ['## E-2 -- Route 3 of SIDE-planted is equivalent to RH by a lemma']
    case('(the rule) an erratum heading naming the anchor`s kernel alone; the same where the sentence names its route',
         (verdict(fa, search(fa, [''] * 1100, e4, [''] * 960), [])[0], verdict(dict(fa, sentence='Route 3 closes.'), search(dict(fa, sentence='Route 3 closes.'), [''] * 1100, e4, [''] * 960), [])[0]),
         ('STANDS', 'MOVED BY A LATER LINE'))
    case('(the searches) (S5) takes whole words of five letters or more: side-kernel-v11-state against a heading saying "restated" and "kernels"',
         [x[2] for x in search(dict(fa, slug='side-kernel-v11-state', tag='*x*'), [''] * 1100 + ['## The kernels restated at v0.26'], [], [''] * 960)], [])
    case('(the searches) the layer`s own lines are not later lines: the slug riemann-hypothesis is not found inside :762-:1094',
         [x for x in search(dict(fa, slug='riemann-hypothesis', tag='*x*'), F, [], [''] * 960) if LAYER[0] <= x[1] <= RULE[1]], [])
    case('(the documents) a tag line`s names, a version apart', docs_named('*kernel-verified* — STORMER_DERIVATION_OMEGA_B; MATTER_AS_ARITHMETIC v0.7; SIMPLICITY_OF_RIEMANN_ZEROS_v1_0.'),
         ['STORMER_DERIVATION_OMEGA_B', 'MATTER_AS_ARITHMETIC', 'SIMPLICITY_OF_RIEMANN_ZEROS'])
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED'))
    return ok, L


def entry_of(F, n):
    """the line of the level-two heading whose entry holds FINDINGS line n."""
    i = n - 1
    while i >= 0 and not F[i].startswith('## '):
        i -= 1
    return i + 1


def compose(gen):
    F, E, R = load()
    tree = [x for x in subprocess.run(['git', '-C', PP, 'ls-tree', '-r', '--name-only', 'HEAD'], capture_output=True, text=True, encoding='utf-8').stdout.split('\n') if x]
    head = subprocess.run(['git', '-C', PP, 'rev-parse', '--short=8', 'HEAD'], capture_output=True, text=True).stdout.strip()
    ok, CL = controls(F, E, R)
    A, NS = anchors(F), not_supportable(R)
    L = ['%s -- (R363)(5)(iv): THE REFERENCE LAYER`S ANCHORS READ -- FINDINGS` sections I to III, each anchor against the later ledger lines (%s)' % (ACT, stamp()[:10]), '',
         '### Written by tools/%s_anchors.py at relay %s (the generator committed before its run) at %s, from PLACE-papers at %s by `git show`; no remote' % (ACT, gen, stamp(), head),
         '### read. A bank of this act and no ledger; no anchor edited: each one moved is carried to the sitting, the layer`s two forms drafted there from the',
         '### later line`s own words. The rule is lexical and its verdicts are candidates: each MOVED cites the line it rests on, for the author`s read.', '',
         '## THE SEARCHES AND THE RULE'] + ['  ' + l for l in __doc__.split('THE SEARCHES, over')[1].split('\n\n  python')[0].split('\n')]
    L[7] = '  THE SEARCHES, over' + L[7][2:]
    L += ['', '## THE LAYER`S OWN RULE FOR HOW AN ANCHOR MOVES (FINDINGS :1084-:1094), quoted',
          '  :1086 %s' % q(F[1085], 400), '  :1094 %s' % q(F[1093], 400),
          '', '## THE CONTROLS, printed before any figure'] + CL
    L += ['', '## THE LINES REGISTRY`S CEILING BLOCK LISTS AS NOT SUPPORTABLE (read from :%d on)' % CEILING_FROM] + ['  REGISTRY :%d *%s*' % x for x in NS]
    rows, res = [], {}
    for a in A:
        hits = search(a, F, E, R)
        v, mv = verdict(a, hits, NS)
        res[a['slug']] = (a, hits, v, mv)
    L += ['', '## THE NAVIGATOR`S READ, TO REPRODUCE OR CORRECT ((R363)(5)(iv))']
    for slug, line, beside in NAV:
        a, hits, v, mv = res[slug]
        named = [x for x in hits if x[2] == 'S1']
        L.append('  %s (:%d), %s: the rule reads %s' % (slug, line, beside, v))
        for led, n in re.findall(r'(REGISTRY|ERRATA|FINDINGS) :(\d+)', beside):
            n = int(n)
            direct = any(x[0] == led and x[1] == n for x in hits) or any(x[0] == led and x[1] == n for x in mv)
            inentry = led == 'FINDINGS' and any(x[0] == 'FINDINGS' and x[1] == entry_of(F, n) for x in hits)
            near = led == 'REGISTRY' and any(x[0] == 'REGISTRY' and abs(x[1] - n) <= 4 for x in list(hits) + list(mv))
            L.append('      %s :%d -- %s' % (led, n, 'REACHED BY THE SEARCH' if direct else ('ITS ENTRY (heading :%d) REACHED BY THE SEARCH' % entry_of(F, n)) if inentry else
                                          ('THE CEILING BLOCK REACHED, at %s' % ', '.join(':%d' % x[1] for x in list(hits) + list(mv) if x[0] == 'REGISTRY' and abs(x[1] - n) <= 4)) if near
                                          else '### NOT REACHED BY THE SEARCHES; the line read by the navigator, not by this rule'))
        L.append('      "no ledger names any of the four since": lines outside the layer carrying the slug as written: %d%s' % (
            len(named), (' -- ' + ', '.join('%s :%d' % (x[0], x[1]) for x in named[:8])) if named else ''))
    L += ['', '## THE ANCHORS: each with its sentence and tag quoted, the later lines found, the verdict']
    tally, moved = {}, []
    for a in A:
        _a, hits, v, mv = res[a['slug']]
        tally[v] = tally.get(v, 0) + 1
        if mv:
            moved.append(a['slug'])
        bykey = {}
        for x in hits:
            bykey[x[2]] = bykey.get(x[2], 0) + 1
        L.append('  %s (:%d, %s) | %s | later lines %d%s' % (a['slug'], a['line'], a['section'].split('.')[0], v, len(hits),
                                                          (' (' + ', '.join('%s %d' % k for k in sorted(bykey.items())) + ')') if hits else ''))
        L.append('      :%s %s' % (a['sentence_line'], q(a['sentence'])))
        L.append('      :%s %s' % (a['tag_line'], q(a['tag'], 220)))
        tiers = []
        for d in docs_named(a['tag']):
            p, t = tier_of(d, tree)
            tiers.append('%s: %s' % (d, ('TIER %s (%s)' % (t, p)) if t else ('no tier line in its opening 60 (%s)' % p) if p else 'NO FILE OF THAT NAME IN THE TREE'))
        if tiers:
            L.append('      the documents named, by their tier blocks: ' + ' ; '.join(tiers))
        for led, n, why in mv[:6]:
            src = dict(FINDINGS=F, ERRATA=E, REGISTRY=R)[led]
            L.append('      MOVED BY %s :%d (%s): %s' % (led, n, why, q(src[n - 1].strip(), 260)))
        if len(mv) > 6:
            L.append('      and %d more moving lines: %s' % (len(mv) - 6, ', '.join('%s :%d' % (x[0], x[1]) for x in mv[6:30])))
        rest = [x for x in hits if not any(m[0] == x[0] and m[1] == x[1] for m in mv)]
        if rest:
            L.append('      later lines not moving by the rule: %s%s' % (', '.join('%s :%d (%s)' % (x[0], x[1], x[2]) for x in rest[:10]), ' and %d more' % (len(rest) - 10) if len(rest) > 10 else ''))
    L += ['', '## CARRIED TO THE SITTING ((R363)(5)(iv), (8)): every anchor moved by a later line',
          '  ' + (', '.join(moved) or 'none'), '',
          '### ### **THE REFERENCE LAYER`S ANCHORS READ: %d ; MOVED BY A LATER LINE %d ; STANDS %d ; NO LATER LINE FOUND %d ; NONE EDITED ; CONTROLS %s.**' % (
              len(A), tally.get('MOVED BY A LATER LINE', 0), tally.get('STANDS', 0), tally.get('NO LATER LINE FOUND', 0), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED')]
    return ok, L


def committed():
    rel = 'tools/%s_anchors.py' % ACT
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)
    return g('ls-files', '--error-unmatch', rel).returncode == 0 and not g('status', '--porcelain', '--', rel).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    if argv[:1] == ['control']:
        ok, L = controls(*load())
        print('\n'.join(L))
        return 0 if ok else 1
    if argv[:1] not in (['run'], ['dry']):
        raise SystemExit(__doc__)
    done, gen = committed()
    if argv[0] == 'run' and not done:
        raise SystemExit('### REFUSED: tools/%s_anchors.py is not committed or differs from its commit; the generator commits before its run ((R363)(5))' % ACT)
    import hold
    if hold.refuses('the anchors read ((R363)(5)(iv))'):
        return 3
    ok, L = compose(gen)
    if argv[0] == 'run':
        if not ok:
            raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NOTHING BANKED')
        tmp = BANK + '.tmp'
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(L) + '\n')
        os.replace(tmp, BANK)
    i = L.index('## THE ANCHORS: each with its sentence and tag quoted, the later lines found, the verdict')
    print('\n'.join(L[L.index('## THE CONTROLS, printed before any figure'):i]))
    print('\n'.join(l[:230] for l in L[i:] if not l.startswith('      ') or l.startswith('      MOVED BY')))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
