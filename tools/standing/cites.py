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
  v1.18.0: comparative_hits(bank, text), comparative_rows(rows, read), comparative_unread(hits, rows) -- a bank's comparative sentences
  against the figures of the table they cite, AGREES / CONTRADICTS / UNREAD ((R348)(2)(ii))
  v1.38.6, (R374)(5) [K7]: at_names(text) -- a Lean path, the word at and a name read as a cite of that name at that path (lean_rows)
"""
import os
import re
import subprocess
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


LEAN_PATH = re.compile(r'(?<![\w/.-])[A-Za-z][\w./-]*\.lean\b')
LEAN_NAME = re.compile(r'(?<![\w.-])(?:(?:[A-Z]\w*\.)+[a-z_]\w*[A-Z_]\w*|[a-zA-Z]\w*(?:[A-Z_]\w*)(?:\.[A-Za-z_]\w*)*)')   # ### v1.32.0, (R362)(7)(ix): a namespaced name (Complex.norm_le_...) read whole
# ### v1.32.0, (R362)(7)(ix), b752 step-zero defect (d), REPEAT b751 (d): `inductive` (and class, axiom, opaque) declare a name too; without them the
# ### reader passed over SIDE-kernel's `inductive MechanismClass` (Bridge/TheBridgeComplete.lean :20) and found Layer1's `structure MechanismClass`
LEAN_DECL = r'^\s*(private\s+)?(protected\s+)?(noncomputable\s+)?(theorem|lemma|def|structure|abbrev|instance|inductive|class|axiom|opaque)\s+%s(\s|$|:)'
# ### v1.32.0, (R362)(7)(ix), b751 (d), REPEAT b736 (e): a dotted name whose leading parts are namespaces (each opening on a capital) names the
# ### declaration of its last part (Complex.norm_le_of_forall_mem_frontier_norm_le); a dotted name with a lower-case leading part is a field
NAMESPACED = re.compile(r'^(?:[A-Z]\w*\.)+[A-Za-z_]\w*$')
# ### v1.23.0, b743 step-zero defect (f): an item label (S4', SP1, G5, R4 ...) opening the parenthesis the path stands in, the label and a comma
# ### the last words before the path: the path is the label's cite, and the reader's name pattern (which wants a capital or an underscore after
# ### the first letter) would pass over the label to a declaration further back ("the zeros of zqFn there (S4', Carrier.lean :21)")
LABEL_BEFORE = re.compile(r"\(\s*[A-Z]{1,3}\d+[a-z]?'*\s*,\s*$")


# ### v1.32.0, (R362)(7)(i), b751 defects (e), (h)-(l), REPEAT b750 (f): THE NAVIGATOR'S RULINGS FROM RECALL. b751's ferry named four relay banks
# ### that do not exist (data/b738_sp1.txt, data/b740_s5.txt, data/b741_c7.txt, data/b743_discharge.txt), found only as the act module's rows
# ### happened to name them. Every path the ruling and the ferry name is printed OK or NONE at HEAD, by the text alone: the relay's data/ and tools/
# ### paths and PLACE-papers' document paths; a path of the act's own (data/<act>_*, tools/<act>_*) not yet written printed as such.
FERRY_PATH = re.compile(r'(?<![\w/.-])(?:(?:data|tools)/[\w.\-/]*\w\.(?:txt|json|py|md|tpl|ps1|csv)|(?:phase[\w.]+|day1|internal|archive)/[\w.\-/]*\w\.md|[A-Z][A-Z0-9_]+\.md)\b')


def _pp_tree(pp, rev='HEAD'):
    return [l for l in _tree(pp, rev) if l]


def _wlist_relay(act, relay):
    """the act's (W) list relay patterns (data/<act>_wlist.json), relay/ prefix dropped; [] if the list is not yet written."""
    import json, os
    try:
        pats = json.load(open(os.path.join(relay, 'data', '%s_wlist.json' % act), encoding='utf-8')).get('patterns', [])
    except (OSError, ValueError):
        return []
    return [p[len('relay/'):] for p in pats if p.startswith('relay/')]


def _word_clause(p, words):
    """(repo, clause) of the first (W) word row whose pattern covers the path in the relay or in PLACE-papers, or None."""
    import fnmatch
    for pat, clause in words or ():
        for repo in ('relay', 'PLACE-papers'):
            if fnmatch.fnmatchcase('%s/%s' % (repo, p), pat):
                return repo, clause
    return None


TO_BE_WRITTEN = 'TO BE WRITTEN, '


def ferry_paths(text, act, relay, pp, words=None):
    """[(path, repo, state)] for every path the text names, once each in order: state OK (present at HEAD), NONE, THE ACT'S OWN, TO BE WRITTEN
    (the act's own prefix, or a path the act's (W) list covers -- e.g. the next act's rules named by form), or TO BE WRITTEN, <clause> (a path
    a (W) word row orders and no tree holds).
    v1.34.0, (R364) amendment row 3 (6), data/b754_stepzero.txt THE READERS' LIMITS: a bare name (no folder) is read by the trees, not taken for
    PLACE-papers': standing at the relay's root, the relay's; standing in PLACE-papers, PLACE-papers'; in both, repo 'both'; in neither and
    ordered written by a clause (the worklist's W_WORDS, `words` to plant them), TO BE WRITTEN with that clause; otherwise NONE."""
    import fnmatch
    rt, pt = set(_pp_tree(relay)), _pp_tree(pp)
    pset = set(pt)
    wl = _wlist_relay(act, relay)
    if words is None:
        import os, sys
        s = os.path.dirname(os.path.abspath(__file__))
        if s not in sys.path:
            sys.path.insert(0, s)
        words = __import__('wlist').word_rows(act, relay)
    out, seen = [], set()
    for m in FERRY_PATH.finditer(text or ''):
        p = m.group(0)
        if p in seen:
            continue
        seen.add(p)
        if p.startswith(('data/', 'tools/')):
            own = p.startswith(('data/%s_' % act, 'tools/%s_' % act, 'tools/acts/%s.' % act))
            wc = _word_clause(p, words)
            if p in rt:
                st = 'OK'
            elif own:
                st = 'THE ACT`S OWN, TO BE WRITTEN'
            elif wc:
                st = TO_BE_WRITTEN + wc[1]
            elif any(fnmatch.fnmatchcase(p, w) for w in wl):
                st = 'THE ACT`S OWN, TO BE WRITTEN'
            else:
                st = 'NONE'
            out.append((p, 'relay', st))
        elif '/' not in p:
            in_r, in_p = p in rt, p in pset or any(f.endswith('/' + p) for f in pt)
            if in_r or in_p:
                out.append((p, 'both' if in_r and in_p else ('relay' if in_r else 'PLACE-papers'), 'OK'))
            else:
                wc = _word_clause(p, words)
                out.append((p, wc[0] if wc else 'neither', (TO_BE_WRITTEN + wc[1]) if wc else 'NONE'))
        else:
            hit = p in pset or any(f.endswith('/' + p) for f in pt)
            out.append((p, 'PLACE-papers', 'OK' if hit else 'NONE'))
    return out


def _tree(repo, rev):
    r = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', rev], capture_output=True)
    if r.returncode:
        raise ValueError('cites: %s has no tree at %s' % (repo, rev))
    return r.stdout.decode('utf-8', 'replace').split('\n')


def _decl(repo, rev, name):
    r = subprocess.run(['git', '-C', repo, 'grep', '-l', '-E', LEAN_DECL % re.escape(name.split('.')[-1]), rev, '--', '*.lean'], capture_output=True)
    return [l.split(':', 1)[1] for l in r.stdout.decode('utf-8', 'replace').split('\n') if ':' in l]


def lean_rows(text, trees, near=110):
    """v1.12.0, (R342)(2)(iii): every Lean path the text names, against the trees at their pins, [(where, what, reading, ok)]. A path no tree holds is one failing row. The instance (R342) names is not of that kind:
    (R341)(4)'s Chi/Generic.lean stands in the tree, and the declaration it was cited for, chiZeroConfig, stands in Chi/ZeroConfig.lean; so a declaration named just before a path, inside its sentence, and
    declared elsewhere is a failing row too. A word no tree declares is no declaration and takes no row. trees: [(repo, rev)]."""
    files = [(repo, rev, f) for repo, rev in trees for f in _tree(repo, rev)]
    cache, rows = {}, []
    clauses = lean_clauses(text)
    ats = at_names(text)
    wt = _at_masked(text, ats)
    for k_, m in enumerate(LEAN_PATH.finditer(text or '')):
        p, line = m.group(0), text.count('\n', 0, m.start()) + 1
        hits = [f for _r, _v, f in files if f == p or f.endswith('/' + p)]
        rows.append((':%d' % line, p, 'in the tree at %s' % ', '.join(sorted(set(h for h in hits))) if hits else 'ABSENT FROM THE TREE AT ITS PIN', bool(hits)))
        if not hits:
            continue
        cl = clauses.get(k_)
        if k_ in ats:
            # ### v1.38.6, (R374)(5) [K7]: the name after its path, by the word at, is that path's cite; one no tree declares takes no row
            name = ats[k_][0]
            if name not in cache:
                cache[name] = sorted(set(f for repo, rev in trees for f in _decl(repo, rev, name)))
            if cache[name]:
                rows.append((':%d' % line, '%s at %s (the name after its path)' % (name, p), 'declared at %s' % ', '.join(cache[name]), bool(set(cache[name]) & set(hits))))
                if cl is None or len(cl) == 1:
                    continue
        if cl is not None and len(cl) > 1:
            # ### v1.34.0, (R364)(3)(iv), b751 (d), b752 (d), b753 (e): a clause of several paths read as a clause, once, at its first path
            if k_ == cl[0]:
                rows += _clause_rows(text, cl, files, trees, cache, near, wt)
            continue
        w = wt[max(wt.rfind('\n', 0, m.start()) + 1, m.start() - near):m.start()]
        w = re.split(r'\.lean\b|[.;:] |\)', w)[-1]   # ### v1.18.0, (R348)(4), b738 step zero: a closed parenthesis ends the window, its names the path before it's ("Zeros.lean (..., zqZeroConfig :319), Continuation.lean")
        if LABEL_BEFORE.search(w):   # ### v1.23.0, b743 step-zero defect (f): "(S4', Carrier.lean :21)" -- the path cited for the item label opening its parenthesis; no name before it is read
            continue
        for name in reversed(LEAN_NAME.findall(w)):     # ### the nearest declaration before the path is the one it is cited for; a dotted name is a field and no declaration
            if '.' in name and not NAMESPACED.match(name):
                continue
            # ### v1.32.0, (R362)(7)(ix): a namespaced name is read only where it is joined to the path ("Complex.norm_le_... at Mathlib's AbsMax.lean
            # ### :405", b751 :11); one a comma parts from the path is an item of a list (b740 :29, "Real.exp_bound and the trigonometric bounds by
            # ### name, Analysis/SpecialFunctions/Stirling.lean") and is passed over as v1.31.0 passed over every dotted name.
            if '.' in name and ',' in w[w.rfind(name) + len(name):]:
                continue
            if name not in cache:
                cache[name] = sorted(set(f for repo, rev in trees for f in _decl(repo, rev, name)))
            at = cache[name]
            if at:
                rows.append((':%d' % line, '%s beside %s' % (name, p), 'declared at %s' % ', '.join(at), bool(set(at) & set(hits))))
            break   # ### v1.18.0, (R348)(4), b738 step zero: the nearest identifier is the one cited, declared or not; one no tree declares (a name the act builds,
            #   ### "S3 min_modulus_zero on AbsMax.lean :405") takes no row and stops the read, where before it passed to S2's DiffContOnCl
    return rows


# ### v1.38.6, (R374)(5) [K7], b763 defects (c), REPEAT b753 (e), b763 misses (8): THE NAME AFTER ITS PATH. (R373)'s SCOPE READ wrote
# ### "Schema/Wide/HalfScale.lean at wide_detector, Schema/Wide/HalfScaleControl.lean :1-:35, PowerWindow.lean :42-:47, ..." (data/b763_ferry.txt
# ### :3); the reader reads the names before a path, so wide_detector fell in the window of the clause of three after it and the check halted
# ### (data/b763_citation_check.txt :93), though HalfScale.lean :277 declares it. A path, its line cites if any, the word at and a name of the
# ### reader's form is a cite of that name at that path: one row, the name against that path alone, and the path's own window before it not read;
# ### the name masked, by spaces of its length, from every later window. A word after at that no tree declares (a commit, "the", "port") takes no
# ### row and leaves the path read as before. Over the ferries b700 to b799 the shape stands once, at b763 :3.
AT_NAME = re.compile(r'((?:\s*:\d+(?:\s*[-–]\s*:?\d+)?)*\s+at\s+`?)([A-Za-z_][\w.\']*)')


def at_names(text):
    """{index of a LEAN_PATH match: (name, start, end)}: each path followed, past its line cites, by the word at and a name of LEAN_NAME's
    form (a dotted one namespaced, as the window reads it); a sentence's closing point is not the name's."""
    out = {}
    for k, m in enumerate(LEAN_PATH.finditer(text or '')):
        a = AT_NAME.match(text, m.end())
        if not a:
            continue
        name = a.group(2).rstrip('.')
        if not LEAN_NAME.fullmatch(name) or ('.' in name and not NAMESPACED.match(name)):
            continue
        out[k] = (name, a.start(2), a.start(2) + len(name))
    return out


def _at_masked(text, ats):
    t = text or ''
    for _n, s, e in sorted(ats.values(), key=lambda x: -x[1]):
        t = t[:s] + ' ' * (e - s) + t[e:]
    return t


# ### v1.34.0, (R364)(3)(iv), b751 (d), b752 (d), b753 (e), three acts running: THE CLAUSE OF SEVERAL LEAN PATHS. The reader paired each path
# ### with the nearest name before it, so "the rQ and cQ ... (EpsteinZQ.lean :59; LogDeriv.lean :63-:65)" paired cQ with the first path and
# ### halted. A clause is a run of paths joined by line cites, semicolons, commas or "and" alone; where it carries as many declared names before
# ### it as paths, the reader pairs them in order; otherwise it reads every name against every path of the clause and halts where no path
# ### holds a name. A clause of one path is read as before.
CLAUSE_JOIN = re.compile(r'^(?:\s*(?::\d+(?:\s*[-–]\s*:?\d+)?|[;,]|and))*\s*$')


def lean_clauses(text):
    """{path index: [indices of its clause]} over LEAN_PATH's matches in order: consecutive paths whose text between is CLAUSE_JOIN."""
    ms = list(LEAN_PATH.finditer(text or ''))
    out, cur = {}, []
    for i, m in enumerate(ms):
        if cur and CLAUSE_JOIN.match(text[ms[cur[-1]].end():m.start()]) and '\n' not in text[ms[cur[-1]].end():m.start()]:
            cur.append(i)
        else:
            cur = [i]
        for j in cur:
            out[j] = cur
    return out


def _clause_rows(text, cl, files, trees, cache, near, wtext=None):
    ms = list(LEAN_PATH.finditer(text or ''))
    first = ms[cl[0]]
    paths = [ms[i].group(0) for i in cl]
    line = text.count('\n', 0, first.start()) + 1
    held = dict((p, set(f for _r, _v, f in files if f == p or f.endswith('/' + p))) for p in paths)
    wt = text if wtext is None else wtext   # ### v1.38.6, [K7]: the window read with each name after its path masked
    w = wt[max(wt.rfind('\n', 0, first.start()) + 1, first.start() - near):first.start()]
    w = re.split(r'\.lean\b|[.;:] |\)', w)[-1]
    if LABEL_BEFORE.search(w):
        return []
    names = []
    for name in LEAN_NAME.findall(w):
        if '.' in name and not NAMESPACED.match(name):
            continue
        if name not in cache:
            cache[name] = sorted(set(f for repo, rev in trees for f in _decl(repo, rev, name)))
        if cache[name] and name not in names:
            names.append(name)
    if not names:
        return []
    rows = []
    if len(names) == len(paths):
        for name, p in zip(names, paths):
            at = cache[name]
            rows.append((':%d' % line, '%s beside %s (paired in order in a clause of %d paths)' % (name, p, len(paths)), 'declared at %s' % ', '.join(at), bool(set(at) & held[p])))
    else:
        every = set().union(*held.values())
        for name in names:
            at = cache[name]
            rows.append((':%d' % line, '%s against every path of a clause of %d (%s)' % (name, len(paths), ', '.join(paths)),
                         'declared at %s' % ', '.join(at), bool(set(at) & every)))
    return rows


# ### v1.18.0, (R348)(2)(ii), b737 (v): THE SENTENCE AGAINST ITS OWN TABLE. A bank's comparative sentence ("leads", "trails", "largest", "lowest" and
# ### their kin) is read against the figures of the table it cites, each AGREES or CONTRADICTS, before the lock; a comparative word in a bank the act
# ### names with no reading row is UNREAD. The rows name the figures by bank and line, never by the sentence's own numbers.
COMPARATIVE = re.compile(r'(?<!\bat )\b(leads?|trails?|largest|highest|greatest|lowest|least|smallest)\b(?!\s+to\b)', re.I)   # ### "at least" and "leads to" no comparison
_ABOVE = ('lead', 'leads', 'largest', 'highest', 'greatest')
_BELOW = ('trail', 'trails', 'lowest', 'least', 'smallest')


# ### v1.34.0, (R364)(3), b754 defect (k): A NOUN IS NOT A COMPARISON. v1.18.0 read the pattern's words in any sense; b754's defects row (g)
# ### named b753's record heading by the noun "trail" and the citation check halted on it as an UNREAD comparison (17:09:30Z). "lead" and "trail"
# ### after a determiner or a possessive ("the trail", "b753's trail", "its leads") are nouns, printed apart; the superlatives ("the least",
# ### "the largest") stay comparisons, a determiner being their own form.
NOUN = re.compile(r"(?:\b(?:the|a|an|its|their|this|that|each|every|whose|one)\s+|['`]s\s+)(leads?|trails?)\b", re.I)


def _noun_spans(l):
    return [m.span(1) for m in NOUN.finditer(l)]


def comparative_hits(name, text):
    """[(bank, line, word)]: every comparative word of a bank's text, by the line it stands on; v1.34.0: a noun use read apart."""
    out = []
    for i, l in enumerate((text or '').split('\n'), 1):
        ns = _noun_spans(l)
        out += [(name, i, m.group(1).lower()) for m in COMPARATIVE.finditer(l) if m.span(1) not in ns]
    return out


def comparative_nouns(name, text):
    """[(bank, line, word)]: the pattern's words used as nouns, printed apart from the comparisons."""
    return [(name, i, l[a:b].lower()) for i, l in enumerate((text or '').split('\n'), 1) for a, b in _noun_spans(l)]


def figure(spec, read):
    """one figure, ('line', bank, line, regex) -> float(group 1) on that line; or a column, ('table', bank, first line, regex) -> {group 1: float(group 2)}
    over the consecutive lines from the first that match. read(bank) -> text."""
    kind, bank, line, pat = spec
    L = (read(bank) or '').split('\n')
    if kind == 'line':
        m = re.search(pat, L[line - 1]) if 0 < line <= len(L) else None
        if not m:
            raise ValueError('%s :%d does not read %r' % (bank, line, pat))
        return float(m.group(1))
    out = {}
    for l in L[line - 1:]:
        m = re.search(pat, l)
        if not m:
            break
        out[m.group(1)] = float(m.group(2))
    if not out:
        raise ValueError('%s :%d opens no row of %r' % (bank, line, pat))
    return out


def verdict(word, subject, values, better='higher'):
    """AGREES or CONTRADICTS: the subject's figure against every other figure given. "leads"/"largest" kin hold where the subject's figure is the best
    of them, "trails"/"lowest" kin where it is the worst; best is the higher figure (better='higher') or the lower ('lower'). A superlative of size
    ("largest", "lowest") reads the figure itself, better ignored."""
    w = word.lower()
    s, others = values[subject], [v for k, v in values.items() if k != subject]
    if not others:
        raise ValueError('no figure beside the subject`s')
    if w in ('largest', 'highest', 'greatest'):
        ok = all(s > o for o in others)
    elif w in ('lowest', 'least', 'smallest'):
        ok = all(s < o for o in others)
    else:
        hi = better == 'higher'
        above = all((s > o) if hi else (s < o) for o in others)
        below = all((s < o) if hi else (s > o) for o in others)
        ok = above if w in _ABOVE else below
    return 'AGREES' if ok else 'CONTRADICTS'


def comparative_rows(rows, read):
    """each row dict(at=(bank, line), word, subject, figures=[(name, spec)] or a ('table', ...) spec, better) read:
    [(bank, line, word, subject, {name: figure}, AGREES | CONTRADICTS | UNREAD, why)]."""
    out = []
    for r in rows:
        bank, line = r['at']
        try:
            f = r['figures']
            vals = figure(f, read) if isinstance(f, tuple) else dict((n, figure(s, read)) for n, s in f)
            if r['subject'] not in vals:
                raise ValueError('the subject %s has no figure' % r['subject'])
            out.append((bank, line, r['word'], r['subject'], vals, verdict(r['word'], r['subject'], vals, r.get('better', 'higher')), r.get('note', '')))
        except (ValueError, IndexError, KeyError) as e:
            out.append((bank, line, r.get('word'), r.get('subject'), {}, 'UNREAD', str(e)))
    return out


def comparative_unread(hits, rows):
    """the hits no reading row covers, by bank, line and word."""
    have = set((b, l, (w or '').lower()) for b, l, w, *_r in rows)
    return [h for h in hits if h not in have]


def next_clause(text):
    """v1.14.0, (R344)(2)(viii), b733 event (8): the clause of a ruling that names the next act, read from the ruling's text: the last numbered item carrying the words. Pure in its argument."""
    r = RUL.search(text or '')
    body = (text or '').split('RULING %s END' % (r.group(1) if r else ''))[0]
    hits = [m.group(1) for m in re.finditer(r'(?m)^\((\d+)\) .*$', body) if re.search(r'\bb\d{3}\b.*\bthen\b|[Tt]he act after this one|next act', m.group(0))]
    return '%s(%s)' % (r.group(1), hits[-1]) if r and hits else None


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
