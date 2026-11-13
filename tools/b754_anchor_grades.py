# -*- coding: utf-8 -*-
"""b754_anchor_grades.py -- (R364)(4)(ii): THE ANCHORS' KERNEL TAGS AGAINST THE TERMINAL TABLE, data/b754_anchor_grades.txt.

For each of the 76 anchors of FINDINGS :762-:1083 (parsed by tools/b753_anchors.py's own reader): the Lean names its sentence and tag cite;
each name's grade as data/terminal_table.json holds it, or NOT IN THE TABLE; and a verdict from the ruling's rule, quoted from
data/b754_ferry.txt at run time. Beside it, the 21 rows of data/b753_anchors.txt that name a document standing in no tree, each with the
shelves' listing of (4)(iii). Read from PLACE-papers at HEAD and from the relay's HEAD blobs by `git show`; no remote read; no anchor edited.

WHAT THIS BANK CARRIES OF PLACE-papers ((R364)(5)'s opening sentence and N5, for this act): no ledger line is quoted. An anchor is named by
its heading's name and its line numbers; the Lean names are the kernels' declarations as the anchor cites them; the tag is read for the
one word the rule turns on, kernel-verified, printed as YES or NO. [Q] row (3): the lines it protects (FINDINGS :820-:826, and every line
carrying the leading word of REGISTRY :373's heading with the two lines either side, the word read at run time from REGISTRY at HEAD, held
in no tracked file and never printed) are cited by line and digest (the opening sixteen characters of the line's sha256); an anchor any of
whose lines they protect is printed by its lines, their digests, counts, grades and verdict, and by no name read from it.

THE READING OF THE RULE (the seat's, each a reach, printed before the figures):
  (a) A Lean name an anchor cites: a token between backticks in its sentence or tag lines; a token of the form "<kernel> <version> / <name>"
      read by its part after the last " / ", and "<name> : <type>" by its part before " : ". Not read as a name, and counted by kind: a
      token with a space or a bracket (an expression or a list), a pin (seven hex characters or more), a version (v<digit>...), a path or
      a file (a slash, or .lean .md .py .json .txt), a document's name (capitals with an underscore), a kernel's name (SIDE-...), a Lean
      keyword or tactic. A name-like token OUTSIDE backticks (a dotted name, or a lower-case name with an underscore) is read as a cited
      name only where the table holds it; the others are counted as notation.
  (b) A name's rows: the table's rows whose name equals it, else whose name ends with "." and it (FULL or TAIL, printed). A name whose
      rows carry more than one grade string reads AMBIGUOUS, every grade printed, and decides no verdict.
  (c) A terminal is a name the table holds; a name NOT IN THE TABLE is printed and is not a terminal.
  (d) The grade classes, by the table's own strings, a compound "A \\ B" read by its alternatives: DERIVES-or-INTERFACES where every
      alternative is DERIVES or INTERFACES; ENCODES-CONCLUSION-or-SHELL-or-STIPULATION where every alternative is ENCODES-CONCLUSION,
      ENCODES (its synonym by tools/terminal_table.py :19-:20, whose compound string for ENCODES-CONCLUSION-or-SHELL is
      "ENCODES-CONCLUSION \\ SHELL"), SHELL or STIPULATION. Every other string (CONFLICT, DEF, the dash, PREDICATE-UNLISTED, a compound
      mixing the two classes) is in neither.
  (e) The verdict, in this order: NOT TAGGED kernel-verified; NO TERMINAL CITED; THE TAG STANDS ON A TERMINAL where a terminal of one
      grade is DERIVES-or-INTERFACES; THE TAG OVER ITS TERMINALS where every terminal is of one grade and that grade is
      ENCODES-CONCLUSION-or-SHELL-or-STIPULATION; and where the rule's four do not reach (a terminal CONFLICT, DEF, AMBIGUOUS and no
      other deciding), THE RULE READS NO VERDICT, its grades printed: the ruling's four are quoted and not widened.

  python -X utf8 -u tools/b754_anchor_grades.py control      the controls alone
  python -X utf8 -u tools/b754_anchor_grades.py dry          the controls and the bank, printed, nothing written
  python -X utf8 -u tools/b754_anchor_grades.py run          the controls, then the bank written (the generator committed before its run)
"""
import collections
import copy
import hashlib
import io
import json
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
from b753_anchors import anchors as layer_anchors, LAYER, PP

ACT = 'b754'
SELF = 'tools/%s_anchor_grades.py' % ACT
BANK = os.path.join(RELAY, 'data', '%s_anchor_grades.txt' % ACT)
NL = '\n'
Q_FIXED = set(range(820, 827))
STANDS_ALT = {'DERIVES', 'INTERFACES'}
OVER_ALT = {'ENCODES-CONCLUSION', 'ENCODES', 'SHELL', 'STIPULATION'}
V_NOT = 'NOT TAGGED kernel-verified'
V_NONE = 'NO TERMINAL CITED'
V_STANDS = 'THE TAG STANDS ON A TERMINAL'
V_OVER = 'THE TAG OVER ITS TERMINALS'
V_NOV = 'THE RULE READS NO VERDICT'
ORDER = [V_STANDS, V_OVER, V_NONE, V_NOT, V_NOV]
TICK = re.compile(r'`([^`]+)`')
NAME = re.compile(r"^[^\W\d][\w.'!?]*$")
HEX = re.compile(r'^[0-9a-f]{7,40}$')
OUTSIDE = re.compile(r"(?<![\w`./-])((?:[A-Z][A-Za-z0-9]*\.)+[A-Za-z_][\w']*|[a-z][a-z0-9]*_[A-Za-z0-9_']+)(?![\w`/-])")
KEYWORDS = set('''decide native_decide def theorem lemma simp rfl norm_num sorry axiom by fun omega ring linarith exact instance structure
class inductive abbrev noncomputable Prop Type True False'''.split())
NOTREE = 'NO FILE OF THAT NAME IN THE TREE'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode:
        raise SystemExit('### NOT READ: git -C %s %s' % (repo, ' '.join(a)))
    return r.stdout


def lines_at(repo, path):
    return git(repo, 'show', 'HEAD:%s' % path).replace('\r', '').split(NL)


def digest(line):
    return hashlib.sha256(line.encode('utf-8')).hexdigest()[:16]


def q_word(R):
    """the leading word of REGISTRY :373's heading, read at run time; never printed."""
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', R[372]) if len(R) > 372 else None
    return m.group(2) if m else None


def protected(F, word):
    out = set(Q_FIXED)
    if word:
        rx = re.compile(r'\b%s\b' % re.escape(word), re.I)
        for k, l in enumerate(F, 1):
            if rx.search(l):
                out |= set(range(max(1, k - 2), min(len(F), k + 2) + 1))
    return out


def index(rows):
    full, tail = collections.defaultdict(list), collections.defaultdict(list)
    for r in rows:
        n = r['name']
        full[n].append(r)
        p = n.split('.')
        for k in range(1, len(p)):
            tail['.'.join(p[k:])].append(r)
    return full, tail


def token_kind(tok):
    """(name, None) or (None, kind)."""
    t = tok.strip()
    if ' / ' in t:
        t = t.rsplit(' / ', 1)[1].strip()
    elif ' : ' in t:
        t = t.split(' : ', 1)[0].strip()
    if re.match(r'^SIDE-[a-z0-9-]+$', t):
        return None, 'a kernel`s name'
    if '/' in t or re.search(r'\.(lean|md|py|json|txt)$', t):
        return None, 'a path or a file'
    if HEX.match(t):
        return None, 'a pin'
    if re.match(r'^v\d', t):
        return None, 'a version'
    if not NAME.match(t) or t.endswith('.'):
        return None, 'an expression or a list'
    if re.match(r'^[A-Z0-9_]+$', t) and '_' in t:
        return None, 'a document`s name'
    if t in KEYWORDS:
        return None, 'a Lean keyword or tactic'
    return t, None


def alts(g):
    return [x.strip() for x in (g or '').split('\\')]


def klass(g):
    a = alts(g)
    if a and all(x in STANDS_ALT for x in a):
        return 'DERIVES-or-INTERFACES'
    if a and all(x in OVER_ALT for x in a):
        return 'ENCODES-CONCLUSION-or-SHELL-or-STIPULATION'
    return None


def read_anchor(a, full, tail):
    """the names an anchor cites and their rows; the verdict."""
    text = a['sentence'] + ' ' + a['tag']
    names, skipped = [], collections.Counter()
    for tok in TICK.findall(text):
        n, why = token_kind(tok)
        if n:
            if n not in names:
                names.append(n)
        else:
            skipped[why] += 1
    notation = 0
    for m in OUTSIDE.finditer(re.sub(r'`[^`]*`', ' ', text)):
        n = m.group(1)
        if re.search(r'\.(md|lean|py|json|txt)$', n):
            continue
        if n in full or n in tail:
            if n not in names:
                names.append(n)
        else:
            notation += 1
    cited = []
    for n in names:
        rs = full.get(n) or tail.get(n) or []
        how = 'FULL' if n in full else 'TAIL' if rs else None
        grades = sorted(set(r['grade'] for r in rs))
        cited.append(dict(name=n, how=how, rows=sorted(set((r['repo'], r['name'], r['grade']) for r in rs)), grades=grades))
    kv = any(t.strip().startswith('kernel-verified') for t in a['tags'])
    terms = [c for c in cited if c['rows']]
    if not kv:
        v = V_NOT
    elif not terms:
        v = V_NONE
    elif any(len(c['grades']) == 1 and klass(c['grades'][0]) == 'DERIVES-or-INTERFACES' for c in terms):
        v = V_STANDS
    elif all(len(c['grades']) == 1 and klass(c['grades'][0]) == 'ENCODES-CONCLUSION-or-SHELL-or-STIPULATION' for c in terms):
        v = V_OVER
    else:
        v = V_NOV
    return dict(kv=kv, cited=cited, terms=terms, skipped=skipped, notation=notation, verdict=v)


def rule_quoted(ferry):
    for i, l in enumerate(ferry, 1):
        k = l.find('THE TAG STANDS ON A TERMINAL (')
        if k >= 0:
            e = l.find('NOT TAGGED kernel-verified', k)
            if e > k:
                return i, l[k:e + len('NOT TAGGED kernel-verified')]
    return None, None


def grade_text(c):
    if not c['rows']:
        return 'NOT IN THE TABLE'
    g = ' | '.join(c['grades'])
    return '%s%s (%s, %s)' % ('AMBIGUOUS: ' if len(c['grades']) > 1 else '', g, c['how'], ', '.join(sorted(set(r[0] for r in c['rows']))))


def planted(slug, cite, kv=True):
    return dict(line=0, slug=slug, section='planted', sentence_line=0, sentence='a planted sentence citing `%s`.' % cite if cite else 'a planted sentence.',
                tag_line=0, tag='*%s* -- planted' % ('kernel-verified' if kv else 'theorem-supported'), tags=['kernel-verified' if kv else 'theorem-supported'])


def controls(F, A, rows, b753, prot):
    out, ok, n = [], 0, 0
    full, tail = index(rows)

    def case(label, good):
        nonlocal ok, n
        n += 1
        ok += bool(good)
        out.append('  %s : %s' % (label, 'AS WANTED' if good else '### NOT AS WANTED'))

    live = collections.Counter(r['grade'] for r in rows)
    out.append('  the live table`s grade strings: %s ; STIPULATION %d' % (', '.join('%s %d' % kv for kv in sorted(live.items())), live.get('STIPULATION', 0)))
    rows2 = copy.deepcopy(rows) + [dict(repo='SIDE-planted', name='Planted.stipulated_terminal', grade='STIPULATION')]
    f2, t2 = index(rows2)
    r = read_anchor(planted('planted-stipulation', 'Planted.stipulated_terminal'), f2, t2)
    case('(1) a planted anchor tagged kernel-verified citing a terminal planted in a copy of the table graded STIPULATION: %s' % r['verdict'], r['verdict'] == V_OVER)
    der = next(x for x in rows if x['grade'] == 'DERIVES')
    r = read_anchor(planted('planted-derives', der['name']), full, tail)
    case('(2) a planted anchor tagged kernel-verified citing %s (%s, graded DERIVES in the live table): %s' % (der['name'], der['repo'], r['verdict']), r['verdict'] == V_STANDS)
    rh = [a for a in A if a['slug'] == 'riemann-hypothesis']
    routes = re.findall(r'`([^`]+)` Route (\d)', rh[0]['sentence']) if rh else []
    found = []
    for nm, k in routes:
        rs = full.get(nm) or tail.get(nm) or []
        found.append('Route %s %s -> %s' % (k, nm, ' | '.join(sorted(set('%s (%s)' % (x['grade'], x['repo']) for x in rs))) or 'NOT IN THE TABLE'))
    held = sum(1 for nm, k in routes if full.get(nm) or tail.get(nm))
    case('(3) the route terminals riemann-hypothesis (:%s) names, each in the table: %d named, %d found [%s]' % (
        rh[0]['line'] if rh else '?', len(routes), held, '; '.join(found)), len(routes) == 3 and held == 3 and sorted(k for _, k in routes) == ['1', '2', '3'])
    r = read_anchor(planted('planted-untagged', der['name'], kv=False), full, tail)
    case('(4) a planted anchor not tagged kernel-verified citing the same DERIVES terminal: %s' % r['verdict'], r['verdict'] == V_NOT)
    r = read_anchor(planted('planted-absent', 'Planted.held_nowhere_zq'), full, tail)
    case('(5) a planted anchor tagged kernel-verified citing a name the table does not hold: %s' % r['verdict'], r['verdict'] == V_NONE)
    con = next((x for x in rows if x['grade'] == 'CONFLICT' and len(set(y['grade'] for y in (full.get(x['name']) or []))) == 1), None)
    if con:
        r = read_anchor(planted('planted-conflict', con['name']), full, tail)
        case('(6) a planted anchor tagged kernel-verified citing %s (graded CONFLICT alone): %s, the rule`s four not reaching it' % (con['name'], r['verdict']), r['verdict'] == V_NOV)
    else:
        case('(6) a CONFLICT terminal of one grade string in the live table: none found', False)
    m = re.search(r'ANCHORS READ: (\d+)', NL.join(b753))
    case('(7) the anchors this reader parses at PLACE-papers HEAD: %d ; data/b753_anchors.txt`s foot %s' % (len(A), m.group(1) if m else 'NOT READ'),
         bool(m) and len(A) == int(m.group(1)) == 76)
    nt = [i for i, l in enumerate(b753, 1) if NOTREE in l]
    case('(8) the rows of data/b753_anchors.txt naming a document in no tree: %d (the ruling`s figure 21)' % len(nt), len(nt) == 21)
    lay = sorted(k for k in prot if LAYER[0] <= k <= LAYER[1])
    pa = [a for a in A if set(range(a['line'], (a['tag_line'] or a['line']) + 1)) & prot]
    case('(9) [Q] row (3): its word read from REGISTRY :373 at run time (%s, its length %d, not printed) ; the layer`s protected lines %d, :820-:826 among them %s ; anchors touching them %d' % (
        'READ' if WORD else '### NOT READ', len(WORD or ''), len(lay), Q_FIXED <= set(lay), len(pa)), bool(WORD) and Q_FIXED <= set(lay) and len(pa) >= 1)
    return out, ok, n


def leak_check(text, F, prot):
    """the bank's text against [Q]: the word's occurrences, and 32-character windows of each protected line found in it."""
    wc = len(re.findall(r'\b%s\b' % re.escape(WORD), text, re.I)) if WORD else -1
    hits = 0
    for k in sorted(prot):
        s = F[k - 1].strip() if 0 < k <= len(F) else ''
        for j in range(0, max(0, len(s) - 32) + 1, 16):
            w = s[j:j + 32]
            if len(w) == 32 and w in text:
                hits += 1
                break
    return wc, hits


def compose(gen, head_pp):
    F = lines_at(PP, 'FINDINGS.md')
    R = lines_at(PP, 'REGISTRY.md')
    global WORD
    WORD = q_word(R)
    prot = protected(F, WORD)
    A = layer_anchors(F)
    table = json.loads(git(RELAY, 'show', 'HEAD:data/terminal_table.json'))
    tblob = git(RELAY, 'rev-parse', 'HEAD:data/terminal_table.json').strip()[:12]
    rows = table['rows']
    b753 = lines_at(RELAY, 'data/b753_anchors.txt')
    ferry = lines_at(RELAY, 'data/%s_ferry.txt' % ACT)
    ceil = lines_at(RELAY, 'data/%s_ceiling.txt' % ACT)
    out, ok, n = controls(F, A, rows, b753, prot)
    full, tail = index(rows)
    rl, rule = rule_quoted(ferry)
    L = ['%s -- (R364)(4)(ii): THE ANCHORS` KERNEL TAGS AGAINST THE TERMINAL TABLE -- FINDINGS :%d-:%d, each anchor`s cited Lean names graded by data/terminal_table.json (%s)' % (ACT, LAYER[0], LAYER[1], stamp()[:10]), '',
         '### Written by %s at relay %s (the generator committed before its run) at %s, from PLACE-papers at %s and the relay`s HEAD by `git show`' % (SELF, gen, stamp(), head_pp),
         '### (data/terminal_table.json blob %s, generated by %s under %s); no remote read. A bank of this act and no ledger; no anchor edited;' % (tblob, table.get('generated_by'), table.get('ruling')),
         '### the anchors reading OVER are named for [L10]. No ledger line is quoted: an anchor by its heading`s name and lines, the tag by the one word',
         '### the rule turns on; [Q] row (3)`s lines by line and digest.', '',
         '## THE RULE, quoted from data/%s_ferry.txt :%s ((R364)(4)(ii))' % (ACT, rl), '  ' + (rule or '### NOT FOUND IN THE FERRY BANK'), '',
         '## THE READING OF THE RULE, the seat`s, each a reach'] + ['  ' + l for l in __doc__.split('each a reach, printed before the figures):\n')[1].split('\n\n  python')[0].split(NL)]
    L += ['', '## THE CONTROLS, printed before any figure'] + out
    figs, tally, over, nov = [], collections.Counter(), [], []
    yld = collections.Counter()
    for a in A:
        span = set(range(a['line'], (a['tag_line'] or a['line']) + 1))
        r = read_anchor(a, full, tail)
        tally[r['verdict']] += 1
        yld['names'] += len(r['cited'])
        yld['terminals'] += len(r['terms'])
        yld['not in the table'] += len(r['cited']) - len(r['terms'])
        yld['ambiguous'] += sum(1 for c in r['terms'] if len(c['grades']) > 1)
        yld['notation outside backticks'] += r['notation']
        for k, v in r['skipped'].items():
            yld['not read as a name: ' + k] += v
        pl = sorted(span & prot)
        if pl:
            figs.append('  :%d-:%d PROTECTED BY [Q] ROW (3), lines %s by digest %s | kernel-verified %s | names %d, terminals %d, grades [%s] | %s' % (
                a['line'], a['tag_line'] or a['line'], ', '.join(':%d' % k for k in pl), ', '.join(digest(F[k - 1]) for k in pl),
                'YES' if r['kv'] else 'NO', len(r['cited']), len(r['terms']), ' ; '.join(' | '.join(c['grades']) for c in r['terms']), r['verdict']))
            if r['verdict'] == V_OVER:
                over.append('the anchor at :%d (protected, by line)' % a['line'])
            if r['verdict'] == V_NOV:
                nov.append('the anchor at :%d (protected, by line)' % a['line'])
            continue
        figs.append('  %s (:%d, sentence :%s, tag :%s) | kernel-verified %s | names %d, terminals %d | %s' % (
            a['slug'], a['line'], a['sentence_line'], a['tag_line'], 'YES' if r['kv'] else 'NO', len(r['cited']), len(r['terms']), r['verdict']))
        for c in r['cited']:
            figs.append('      %s -> %s' % (c['name'], grade_text(c)))
        if r['verdict'] == V_OVER:
            over.append('%s (:%d)' % (a['slug'], a['line']))
        if r['verdict'] == V_NOV:
            nov.append('%s (:%d)' % (a['slug'], a['line']))
    L += ['', '## THE NAME READING`S YIELD, over the %d anchors (printed for the hand read; no condition)' % len(A)]
    L += ['  %s %d' % kv for kv in sorted(yld.items())]
    L += ['', '## THE ANCHORS: each by its heading`s name and lines, kernel-verified YES or NO, its cited names with their grades, the verdict'] + figs
    L += ['', '## FOR [L10]: THE ANCHORS READING THE TAG OVER ITS TERMINALS', '  ' + (', '.join(over) or 'none'),
          '', '## THE ANCHORS THE RULE`S FOUR DO NOT REACH (THE RULE READS NO VERDICT), for the author`s read', '  ' + (', '.join(nov) or 'none')]
    ci = [i for i, l in enumerate(ceil, 1) if '(4)(iii)' in l and 'CARRIED' in l]
    ca = [i for i, l in enumerate(ceil, 1) if l.strip().startswith('CARRIED, to an act after')]
    carried = bool(ci)
    L += ['', '## THE 21 ROWS OF data/b753_anchors.txt NAMING A DOCUMENT IN NO TREE, AND THE SHELVES` LISTING OF (4)(iii)',
          '  the shelves` listing of (4)(iii) %s (data/%s_ceiling.txt %s): %s' % (
              'is CARRIED by the ceiling to an act after the walk and the build' if carried else '### is not read as carried',
              ACT, ', '.join(':%d' % i for i in sorted(set(ci + ca))) or 'no line',
              'no listing stands to seek in and none is put in its place; each name below waits for that listing, NOT SOUGHT' if carried else 'the halt stands')]
    names_all = []
    heads = {}
    for i, l in enumerate(b753, 1):
        m = re.match(r'^  ([a-z0-9][\w-]*) \(:(\d+), ([IVX]+)\) \| ', l)
        if m:
            heads[i] = (m.group(1), int(m.group(2)))
        if NOTREE in l:
            k = max([j for j in heads if j < i] or [0])
            slug, at = heads.get(k, ('?', 0))
            a = next((x for x in A if x['line'] == at), None)
            span = set(range(at, ((a or {}).get('tag_line') or at) + 1))
            nm = re.findall(r'([A-Z][A-Za-z0-9_]+): ' + NOTREE, l)
            if span & prot:
                L.append('  data/b753_anchors.txt :%d, under the anchor at :%d (protected by [Q] row (3), by line): %d document(s) in no tree -- NOT SOUGHT' % (i, at, len(nm)))
            else:
                names_all += nm
                L.append('  data/b753_anchors.txt :%d, under %s (:%d): %s -- NOT SOUGHT' % (i, slug, at, ', '.join(nm)))
    L.append('  distinct names printed %d' % len(set(names_all)))
    tot = sum(tally.values())
    L += ['', '### ### **THE ANCHORS READ: %d ; %s ; THE SUM %d, EQUAL %s ; NONE EDITED ; THE 21 ROWS NOT SOUGHT, (4)(iii) CARRIED ; CONTROLS %d OF %d.**' % (
        len(A), ' ; '.join('%s %d' % (v, tally.get(v, 0)) for v in ORDER), tot, tot == len(A), ok, n)]
    text = NL.join(L) + NL
    wc, hits = leak_check(text, F, prot)
    good = wc == 0 and hits == 0
    k = L.index('## THE CONTROLS, printed before any figure') + 1 + len(out)
    L.insert(k, '  (10) [Q] row (3) over this bank`s text: the word`s occurrences %d, protected lines with a 32-character window found in it %d (wanted 0 and 0) : %s' % (
        wc, hits, 'AS WANTED' if good else '### NOT AS WANTED'))
    ok += good
    n += 1
    L[-1] = L[-1].replace('CONTROLS %d OF %d' % (ok - good, n - 1), 'CONTROLS %d OF %d' % (ok, n))
    return ok == n, ok, n, L


WORD = None


def committed():
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)
    return g('ls-files', '--error-unmatch', SELF).returncode == 0 and not g('status', '--porcelain', '--', SELF).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    mode = argv[0] if argv else ''
    if mode not in ('control', 'dry', 'run'):
        raise SystemExit(__doc__)
    done, gen = committed()
    if mode == 'run' and not done:
        raise SystemExit('### REFUSED: %s is not committed or differs from its commit; the generator commits before its run ((R364)(4))' % SELF)
    import hold
    if mode != 'control' and hold.refuses('the anchors` kernel tags read ((R364)(4)(ii))'):
        return 3
    head_pp = git(PP, 'rev-parse', '--short=8', 'HEAD').strip()
    allok, ok, n, L = compose(gen, head_pp)
    c0 = L.index('## THE CONTROLS, printed before any figure')
    c1 = next(i for i, l in enumerate(L) if l.startswith('## THE NAME READING`S YIELD'))
    print(NL.join(L[c0:c1]))
    print('### ### **CONTROLS %d OF %d %s**' % (ok, n, 'AS WANTED' if allok else 'NOT ALL AS WANTED'))
    if mode == 'control':
        return 0 if allok else 1
    if not allok:
        raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NO FIGURE PRINTED, NOTHING BANKED')
    if mode == 'dry':
        print(NL.join(L[c1:]))
        return 0
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(tmp, BANK)
    print('WRITTEN data/%s_anchor_grades.txt, %d lines' % (ACT, len(L)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
