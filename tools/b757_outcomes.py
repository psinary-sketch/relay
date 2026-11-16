# -*- coding: utf-8 -*-
"""tools/b757_outcomes.py -- (R367)(4)-(7): EACH RESULT'S SENTENCE, THE RULING'S TEXT WITH ITS FIELDS FILLED FROM THE ACT'S BANKS AND NOTHING ELSE.

Each sentence is cut at run time from the ferry bank (data/b757_ferry.txt, the clause's quoted text after its outcome's words), and its
angle-bracket fields are filled from the dispatch rows (data/b757_dispatch_rows.json) and the kernel's tree at the built commit, each field
printed with the bank or blob it came from. No sentence is typed here. The outcome of each item is read from its rows by the clause's own
test, printed beside the sentence.

  join     (4): the join's one dispatch, read: the exit file, the axioms print, the lines against the joined print_targets.txt; the outcome and
           its sentence, the reading behind it (the declaration the environment held, in each module declaring it, with the commits that added
           them and the branches holding those commits; the names the workflow's grammar refused, with the bank that first entered them)
  T0, T1   (5): the item's last dispatch, read: the exit file, the item's own names (every `theorem` its Lean file declares at the dispatched
           commit, qualified in the file's namespace) each with an axioms line within the standard three, none naming sorryAx, and the file's
           lines against the clause's stop; the sentence cut from the ferry's T0 or T1 line, the branch and commit in the tag's place ((4):
           "where the join fails ... its sentences name that branch and commit in the tag's place")
  mod24    (6): the route's control dispatch, then the module's last dispatch in SIDE-dirichlet-mod-24, read; units24_iso_signs within the
           standard three (or none), no sorryAx; the riding segment of the compiled sentence kept where mul_eq_add_add_one_iff's line stands
  wide     (7): the wide direction's last dispatch, read: every `theorem` of Schema/Wide/HalfScale.lean and HalfScaleControl.lean at the
           dispatched commit within the standard three, no sorryAx; the compiled sentence's two <name> fields filled in its own order, the
           control's theorem zq_arith_side_re_neg and the direction's wide_detector, the branch and commit in the tag's place
  bank     every item composed so far, written to data/b757_outcomes.txt and data/b757_outcomes.json (written whole at each run, by this tool)
"""
import io
import json
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b757_worklist as K        # noqa: E402

NL = '\n'
ACT = 'b757'
EF = K.EF_DIR
FERRY = os.path.join(D, 'b757_ferry.txt')
ROWS = os.path.join(D, 'b757_dispatch_rows.json')
BANK = os.path.join(D, 'b757_outcomes.txt')
BANKJ = os.path.join(D, 'b757_outcomes.json')
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
MAIN_AT_STEPZERO = '8fbab45d'


def g(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def ferry():
    return io.open(FERRY, encoding='utf-8').read().replace('\r', '').split(NL)


def clause(n):
    """(line number, text) of the ferry line opening '(n) '."""
    L = ferry()
    hit = [(i + 1, l) for i, l in enumerate(L) if l.startswith('(%d) ' % n)]
    if len(hit) != 1:
        sys.exit('### CLAUSE (%d) NOT READ ONCE IN THE FERRY BANK (%d lines) -- nothing written' % (n, len(hit)))
    return hit[0]


def quoted_after(text, words):
    """the quoted sentence after `words` in the clause's text."""
    i = text.find(words)
    if i < 0:
        return None
    m = re.match(r'\s*"(.*?)"', text[i + len(words):])
    return m.group(1) if m else None


def rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def fill(sentence, fields):
    out = sentence
    for k, v in fields.items():
        out = out.replace('<%s>' % k, str(v))
    left = re.findall(r'<[^<>]+>', out)
    return out, left


def join():
    ln, text = clause(4)
    yes = quoted_after(text, 'THE SENTENCE IF IT COMPILES:')
    no = quoted_after(text, 'THE SENTENCE IF IT DOES NOT:')
    R = rows()
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') in ('join', 'join-repair')]
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    out = ['## (4) THE JOIN (the ferry bank :%d; the sentences cut from it: compiled %d characters, not %d characters)' % (ln, len(yes or ''), len(no or ''))]
    if not disp or not yes or not no:
        out.append('  ### NO JOIN DISPATCH ROWED OR A SENTENCE NOT CUT -- nothing composed')
        return out, None
    d = disp[-1]
    rd = reads.get(int(d['run']))
    if not rd:
        out.append('  ### THE JOIN`S RUN %s NOT READ -- nothing composed' % d['run'])
        return out, None
    targets = rd.get('targets')
    ok = rd.get('build_exit') == '0' and rd.get('built_equal') and not rd.get('stop') and rd.get('axiom_lines') == targets \
        and rd.get('axiom_within') == targets and not rd.get('axiom_missing_n') and not rd.get('sorryAx') and not (rd.get('axioms_refused') or '').strip()
    out.append('  the dispatches: %s' % ', '.join('%d %s run %s at %s' % (x['n'], x['item'], x['run'], x['sha'][:8]) for x in disp))
    out.append('  THE RUN %s READ (data/b757_dispatch_rows.json): exit file %s ; built %s, equal to the dispatched commit %s ; stopped under the hold %s ; '
               'errors %d ; sorry warnings %s ; runner low %s MB' % (d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'),
                                                                   bool(rd.get('stop')), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('runner_low_mb')))
    out.append('  THE AXIOMS PRINT: %s' % rd.get('axioms_print'))
    out.append('  AGAINST THE JOINED print_targets.txt (%s lines): axioms lines %s ; within the standard three %s ; outside %d ; without a line %s ; sorryAx %s' % (
        targets, rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}), rd.get('axiom_missing_n'), rd.get('sorryAx')))
    for l in (rd.get('axioms_refused') or '').split(NL):
        if l.strip():
            out.append('  REFUSED BY THE WORKFLOW`S GRAMMAR (ASCII names alone): %s' % l.strip())
    out.append('  WHAT THE RUN MUST SHOW ((R367)(4)): the exit file 0 ; an axioms line within the standard three for each line ; no line naming sorryAx -> %s' % (
        'SHOWN' if ok else 'NOT SHOWN'))
    rec = dict(item='join', clause_line=ln, run=int(d['run']), sha=d['sha'], shown=ok)
    if ok:
        peel = (rd.get('built_ref') or '')[:8]
        s, left = fill(yes, {'peel': peel, 'run id': d['run'], 'n': rd.get('axiom_lines')})
        rec.update(outcome='COMPILED', sentence=s, unfilled=left)
        out.append('  THE OUTCOME: COMPILED -- main moves to %s by the gated push`s default mode and v0.39 is cut at its read-back' % peel)
    else:
        # ### the break: where the print's import failed, the module named and the line of the declaration the environment already held
        m = re.search(r"import (\S+) failed, environment already contains '([^']+)' from (\S+)", rd.get('axioms_print') or '')
        mod, line, reading = None, None, []
        if m:
            mod, held, other = m.group(1), m.group(2), m.group(3)
            base = held.split('.')
            name = [x for x in base if not re.match(r'^(match_\d+|proof_\d+|eq_\d+)$', x)][-1]
            for mm in (mod, other):
                path = mm.replace('.', '/') + '.lean'
                src = g('show', '%s:%s' % (d['sha'], path)).split(NL)
                decl = [i + 1 for i, l in enumerate(src) if re.match(r'^\s*(noncomputable\s+)?(def|theorem|abbrev|instance|structure)\s+%s\b' % re.escape(name), l)]
                imps = [l.split()[1] for l in src if l.startswith('import ')]
                added = g('log', '--format=%h', '--diff-filter=A', d['sha'], '--', path).split()
                held_by = [b.strip(' *') for b in g('branch', '--contains', added[-1]).split(NL) if b.strip()] if added else []
                reading.append('  %s (%s): `%s` declared at :%s ; imports %s ; added by %s ; that commit held by %s' % (
                    mm, path, name, ', :'.join(str(x) for x in decl) or 'NONE', ', '.join(imps), ', '.join(added) or 'NONE', ', '.join(held_by) or 'NONE'))
                if mm == mod and decl:
                    line = decl[0]
            out.append('  THE BREAK: the print`s import of the %d target modules together failed at %s, whose `%s` the environment already held from %s:' % (
                len((d.get('target') or '').split()), mod, name, other))
            out.extend(reading)
        if mod and line:
            s, left = fill(no, {'module': mod, 'line': line, 'run id': d['run']})
            rec.update(outcome='BROKE', sentence=s, unfilled=left, module=mod, line=line)
            out.append('  THE OUTCOME: THE FAILING OUTCOME ((R367)(4): "any other break is the failing outcome"; the break is not at (ii)`s file, so no second '
                       'dispatch): main stands at %s, no tag cut, the four branches as they stood; (5) built past zq-b730`s tip' % MAIN_AT_STEPZERO)
        else:
            rec.update(outcome='NOT READ', sentence=None, unfilled=None)
            out.append('  ### THE BREAK NOT READ FROM THE PRINT -- no sentence composed')
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")
COEFF = dict(T0=dict(file='SIDEExplicitFormula/Schema/ZQ/Mechanism/NoEuler.lean', stop=360, head='zq_coeff_not_multiplicative',
                     names=('zq_coeff_not_multiplicative',)),
             T1=dict(file='SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', stop=1350, head='cQ_not_nonneg',
                     names=('cQ_not_nonneg', 'cQ_forty_eight')))
COEFF_BRANCH = 'push-b757-coeff'


def axioms_of(text):
    """{name: (axioms...)} from a #print axioms output, a wrapped line read whole (the controls tool's reader, carried)."""
    out = {}
    for m in AX_DEP.finditer(text or ''):
        out[m.group(1)] = tuple(x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip())
    for m in AX_NONE.finditer(text or ''):
        out[m.group(1)] = ()
    return out


def line_opening(prefix):
    L = ferry()
    hit = [(i + 1, l) for i, l in enumerate(L) if l.startswith(prefix)]
    if len(hit) != 1:
        sys.exit('### THE LINE OPENING %r NOT READ ONCE IN THE FERRY BANK (%d lines) -- nothing written' % (prefix, len(hit)))
    return hit[0]


def declared(src):
    """the `theorem`s a Lean file declares and its namespace path (the `namespace` lines before the first declaration, one name each)."""
    ns, names = [], []
    for l in src.split(NL):
        m = re.match(r'^namespace\s+(\S+)\s*$', l)
        if m and not names:
            ns.append(m.group(1))
        m = re.match(r'^theorem\s+([A-Za-z_][A-Za-z0-9_\']*)', l)
        if m:
            names.append(m.group(1))
    return '.'.join(ns), names


def coeff(item):
    ln, text = line_opening('%s, ' % item)
    c = COEFF[item]
    yes = quoted_after(text, 'IF IT COMPILES:')
    no = quoted_after(text, 'IF IT DOES NOT:')
    out = ['## (5) %s (the ferry bank :%d; the sentences cut from it: compiled %d characters, not %d characters)' % (item, ln, len(yes or ''), len(no or ''))]
    R = rows()
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') == item]
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    if not disp or not yes or not no:
        out.append('  ### NO %s DISPATCH ROWED OR A SENTENCE NOT CUT -- nothing composed' % item)
        return out, None
    d = disp[-1]
    rd = reads.get(int(d['run']))
    out.append('  the dispatches: %s' % ', '.join('%d run %s at %s' % (x['n'], x['run'], x['sha'][:8]) for x in disp))
    if not rd:
        out.append('  ### THE RUN %s NOT READ -- nothing composed' % d['run'])
        return out, None
    src = g('show', '%s:%s' % (d['sha'], c['file']))
    ns, names = declared(src)
    nlines = len(src.rstrip(NL).split(NL)) if src else 0
    q = ['%s.%s' % (ns, n) for n in names]
    axt = io.open(os.path.join(rd['artifact'], 'axioms.txt'), encoding='utf-8', errors='replace').read() if rd.get('artifact') and \
        os.path.exists(os.path.join(rd['artifact'], 'axioms.txt')) else ''
    ax = axioms_of(axt)
    have = [n for n in q if n in ax]
    within = [n for n in have if set(ax[n]) <= set(STANDARD)]
    sorry_lines = [n for n in have if 'sorryAx' in ax[n]]
    built = rd.get('build_exit') == '0' and rd.get('built_equal') and not rd.get('stop')
    ok = bool(built and names and len(have) == len(q) and len(within) == len(q) and not sorry_lines and nlines <= c['stop']
              and all('%s.%s' % (ns, h) in q for h in c['names']))
    out.append('  THE RUN %s READ (data/b757_dispatch_rows.json): exit file %s ; built %s, equal to the dispatched commit %s ; stopped under the hold %s ; '
               'errors %d ; sorry warnings %s' % (d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'), bool(rd.get('stop')),
                                                  len(rd.get('errors') or []), rd.get('sorry_warnings')))
    out.append('  THE ITEM`S FILE %s at %s: %d lines against the stop %d ; namespace %s ; theorems %d' % (c['file'], d['sha'][:8], nlines, c['stop'], ns or 'NONE', len(names)))
    out.append('  ITS NAMES IN THE AXIOMS PRINT (%s): with a line %d of %d ; within the standard three %d ; naming sorryAx %d' % (
        rd.get('axioms_print'), len(have), len(q), len(within), len(sorry_lines)))
    for n in q:
        a = ax.get(n)
        out.append('    %-72s %s' % (n, 'NO AXIOMS LINE' if a is None else '[%s]%s' % (', '.join(a), '' if set(a) <= set(STANDARD) else '  OUTSIDE')))
    out.append('  WHAT THE RUN MUST SHOW ((R367)(5)): a compile outcome, no verdict: the exit file 0 and each of the item`s names within the standard three, '
               'no sorryAx, within %d lines -> %s' % (c['stop'], 'SHOWN' if ok else 'NOT SHOWN'))
    rec = dict(item=item, clause_line=ln, run=int(d['run']), sha=d['sha'], shown=ok, lines=nlines, names=len(q))
    if ok:
        heads = [ax['%s.%s' % (ns, h)] for h in c['names']]
        axs = sorted(set(a for h in heads for a in h), key=lambda a: STANDARD.index(a) if a in STANDARD else 9)
        s, left = fill(yes, {'tag': COEFF_BRANCH, 'peel': d['sha'][:8], 'run id': d['run'], 'axioms': 'axioms: %s' % (', '.join(axs) or 'none')})
        rec.update(outcome='COMPILED', sentence=s, unfilled=left)
        out.append('  THE OUTCOME: COMPILED on %s at %s, the branch and commit in the tag`s place ((4)); zq-b730 not moved (events (17), (18)); no tag cut' % (
            COEFF_BRANCH, d['sha'][:8]))
    else:
        errs = rd.get('errors') or []
        where = None
        for l in errs:
            m = re.search(r'([A-Za-z0-9_/.]+\.lean):(\d+):\d+: error', l)
            if m:
                where = '%s :%s, run %s' % (m.group(1), m.group(2), d['run'])
                break
        if not where:
            where = 'run %s: %s' % (d['run'], 'the build exit %s' % rd.get('build_exit') if not built else '%d of %d names without a line within the standard three' % (
                len(q) - len(within), len(q)))
        s, left = fill(no, {'where it stopped': where})
        rec.update(outcome='NOT COMPILED AT THIS RUN', sentence=s, unfilled=left, where=where)
        out.append('  THE OUTCOME AT THIS RUN: NOT COMPILED (%s); the clause`s stop is %d lines, the file at %d -- the failing sentence stands only where '
                   'the item stops' % (where, c['stop'], nlines))
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


M24 = 'D:/SIDE-dirichlet-mod-24'
M24_FILE = 'SIDEDirichletMod24/Units.lean'
M24_HEAD, M24_RIDE = 'units24_iso_signs', 'mul_eq_add_add_one_iff'
M24_TAG = 'v0.2.0'
RIDE_OPEN = '<; with it,'


def mod24():
    """(6): the module's last dispatch in SIDE-dirichlet-mod-24, read; the sentence cut from (6), its riding segment (opening RIDE_OPEN and
    closing at the sentence's last '>') kept, brackets dropped, where the riding statement's line stands within the standard three, and
    dropped where it does not."""
    ln, text = clause(6)
    yes = quoted_after(text, 'IF THE MODULE COMPILES:')
    no = quoted_after(text, 'IF IT DOES NOT:')
    out = ['## (6) THE MODULUS-24 MODULE (the ferry bank :%d; the sentences cut from it: compiled %d characters, not %d characters)' % (ln, len(yes or ''), len(no or ''))]
    R = rows()
    ctl = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') == 'workflow']
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') == 'mod24']
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    for x in ctl:
        rc = reads.get(int(x['run'])) or {}
        out.append('  THE ROUTE`S CONTROL ((6)(i)): dispatch %d run %s at %s, the tree as it stands: exit file %s, axioms lines %s of %s, %s' % (
            x['n'], x['run'], x['sha'][:8], rc.get('build_exit', 'NOT READ'), rc.get('axiom_lines'), rc.get('targets'), rc.get('axioms_print')))
    if not disp or not yes or not no:
        out.append('  ### NO MODULE DISPATCH ROWED OR A SENTENCE NOT CUT -- nothing composed')
        return out, None
    d = disp[-1]
    rd = reads.get(int(d['run']))
    out.append('  the module`s dispatches: %s' % ', '.join('%d run %s at %s' % (x['n'], x['run'], x['sha'][:8]) for x in disp))
    if not rd:
        out.append('  ### THE RUN %s NOT READ -- nothing composed' % d['run'])
        return out, None
    src = subprocess.run(['git', '-C', M24, 'show', '%s:%s' % (d['sha'], M24_FILE)], capture_output=True, text=True, encoding='utf-8',
                         errors='replace').stdout
    ns, names = declared(src)
    q = ['%s.%s' % (ns, n) for n in names]
    axt = io.open(os.path.join(rd['artifact'], 'axioms.txt'), encoding='utf-8', errors='replace').read() if rd.get('artifact') and \
        os.path.exists(os.path.join(rd['artifact'], 'axioms.txt')) else ''
    ax = axioms_of(axt)
    have = [n for n in q if n in ax]
    within = [n for n in have if set(ax[n]) <= set(STANDARD)]
    built = rd.get('build_exit') == '0' and rd.get('built_equal') and not rd.get('stop')
    head, ride = '%s.%s' % (ns, M24_HEAD), '%s.%s' % (ns, M24_RIDE)
    ok = bool(built and head in within and 'sorryAx' not in axt)
    ride_ok = bool(ok and ride in within)
    out.append('  THE RUN %s READ: exit file %s ; built %s, equal %s ; stopped %s ; errors %d ; the print %s' % (
        d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'), bool(rd.get('stop')), len(rd.get('errors') or []),
        rd.get('axioms_print')))
    out.append('  THE MODULE %s at %s: namespace %s ; theorems %d ; with a line %d ; within the standard three (or none) %d' % (
        M24_FILE, d['sha'][:8], ns or 'NONE', len(q), len(have), len(within)))
    for n in q:
        a = ax.get(n)
        out.append('    %-60s %s' % (n, 'NO AXIOMS LINE' if a is None else '[%s]%s' % (', '.join(a) or 'none', '' if set(a) <= set(STANDARD) else '  OUTSIDE')))
    out.append('  WHAT THE RUN MUST SHOW ((R367)(6)): the exit file 0 ; %s within the standard three or none ; no sorryAx -> %s ; the riding statement %s -> %s' % (
        M24_HEAD, 'SHOWN' if ok else 'NOT SHOWN', M24_RIDE, 'SHOWN' if ride_ok else 'NOT SHOWN'))
    rec = dict(item='mod24', clause_line=ln, run=int(d['run']), sha=d['sha'], shown=ok, ride=ride_ok, names=len(q))
    if ok:
        i, j = yes.find(RIDE_OPEN), yes.rfind('>')
        if i < 0 or j < i:
            out.append('  ### THE RIDING SEGMENT NOT FOUND IN THE SENTENCE -- nothing composed')
            return out, None
        s = yes[:i] + (yes[i + 1:j] if ride_ok else '') + yes[j + 1:]
        axs = sorted(set(ax[head]), key=lambda a: STANDARD.index(a) if a in STANDARD else 9)
        s, left = fill(s, {'name': M24_HEAD, 'peel': d['sha'][:8], 'run id': d['run'], 'axioms': 'axioms: %s' % (', '.join(axs) or 'none')})
        rec.update(outcome='COMPILED', sentence=s, unfilled=left, tag=M24_TAG)
        out.append('  THE OUTCOME: COMPILED -- main moves to %s by the gated push`s default mode and %s is cut at its read-back, its peel read back' % (
            d['sha'][:8], M24_TAG))
    else:
        where = None
        for l in rd.get('errors') or []:
            m = re.search(r'([A-Za-z0-9_/.]+\.lean):(\d+):\d+: error', l)
            if m:
                where = '%s :%s, run %s' % (m.group(1), m.group(2), d['run'])
                break
        where = where or 'run %s: the build exit %s' % (d['run'], rd.get('build_exit'))
        s, left = fill(no, {'where it stopped': where})
        rec.update(outcome='NOT COMPILED AT THIS RUN', sentence=s, unfilled=left, where=where)
        out.append('  THE OUTCOME AT THIS RUN: NOT COMPILED (%s)' % where)
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


WIDE_FILES = ('SIDEExplicitFormula/Schema/Wide/HalfScale.lean', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean')
WIDE_CONTROL, WIDE_DIRECTION = 'zq_arith_side_re_neg', 'wide_detector'


def wide():
    """(7): the wide direction's last dispatch, read; every `theorem` of its two files at the dispatched commit with an axioms line within the
    standard three, none naming sorryAx; the compiled sentence cut from (7), its first <name> the control's theorem and its second the
    direction's, in the order the sentence gives them, the branch and commit in the tag's place as (4) orders for (5) (the join having
    failed, no main moved and no tag cut); a failing run printed with its break, the stop sentence composed only where the item stops."""
    ln, text = clause(7)
    yes = quoted_after(text, 'IF IT COMPILES:')
    priced = quoted_after(text, 'IF IT IS PRICED AND NOT BUILT:')
    out = ['## (7) THE ONE DIRECTION OVER THE WIDER STRIP (the ferry bank :%d; the sentences cut from it: compiled %d characters, priced and not built %d '
           'characters)' % (ln, len(yes or ''), len(priced or ''))]
    R = rows()
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') == 'wide']
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    if not disp or not yes or not priced:
        out.append('  ### NO wide DISPATCH ROWED OR A SENTENCE NOT CUT -- nothing composed')
        return out, None
    d = disp[-1]
    rd = reads.get(int(d['run']))
    out.append('  the dispatches: %s' % ', '.join('%d run %s at %s' % (x['n'], x['run'], x['sha'][:8]) for x in disp))
    if not rd:
        out.append('  ### THE RUN %s NOT READ -- nothing composed' % d['run'])
        return out, None
    q, nlines, per = [], 0, []
    for f in WIDE_FILES:
        src = g('show', '%s:%s' % (d['sha'], f))
        ns, names = declared(src)
        n_ = len(src.rstrip(NL).split(NL)) if src else 0
        nlines += n_
        per.append('%s (%d lines, namespace %s, theorems %d)' % (f, n_, ns or 'NONE', len(names)))
        q += ['%s.%s' % (ns, n) for n in names]
    axt = io.open(os.path.join(rd['artifact'], 'axioms.txt'), encoding='utf-8', errors='replace').read() if rd.get('artifact') and \
        os.path.exists(os.path.join(rd['artifact'], 'axioms.txt')) else ''
    ax = axioms_of(axt)
    have = [n for n in q if n in ax]
    within = [n for n in have if set(ax[n]) <= set(STANDARD)]
    sorry_lines = [n for n in have if 'sorryAx' in ax[n]]
    built = rd.get('build_exit') == '0' and rd.get('built_equal') and not rd.get('stop')
    ctl = [n for n in q if n.endswith('.' + WIDE_CONTROL)]
    dirn = [n for n in q if n.endswith('.' + WIDE_DIRECTION)]
    ok = bool(built and q and len(have) == len(q) and len(within) == len(q) and not sorry_lines and len(ctl) == 1 and len(dirn) == 1)
    out.append('  THE RUN %s READ (data/b757_dispatch_rows.json): exit file %s ; built %s, equal to the dispatched commit %s ; stopped under the hold %s ; '
               'errors %d ; sorry warnings %s' % (d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'), bool(rd.get('stop')),
                                                  len(rd.get('errors') or []), rd.get('sorry_warnings')))
    out.append('  THE ITEM`S FILES at %s: %s ; %d lines in all, against the price 250-550 (the navigator`s) and 350-800 (the seat`s), data/b757_price.txt' % (
        d['sha'][:8], ' ; '.join(per), nlines))
    out.append('  ITS NAMES IN THE AXIOMS PRINT (%s): with a line %d of %d ; within the standard three %d ; naming sorryAx %d' % (
        rd.get('axioms_print'), len(have), len(q), len(within), len(sorry_lines)))
    for n in q:
        a = ax.get(n)
        out.append('    %-72s %s' % (n, 'NO AXIOMS LINE' if a is None else '[%s]%s' % (', '.join(a) or 'none', '' if set(a) <= set(STANDARD) else '  OUTSIDE')))
    out.append('  WHAT THE RUN MUST SHOW ((R367)(7)): the exit file 0 and each of the item`s names within the standard three, no sorryAx, %s and %s among '
               'them -> %s' % (WIDE_CONTROL, WIDE_DIRECTION, 'SHOWN' if ok else 'NOT SHOWN'))
    rec = dict(item='wide', clause_line=ln, run=int(d['run']), sha=d['sha'], shown=ok, lines=nlines, names=len(q), dispatches=len(disp))
    if ok:
        axs = sorted(set(ax[ctl[0]]), key=lambda a: STANDARD.index(a) if a in STANDARD else 9)
        s = yes.replace('<name>', WIDE_CONTROL, 1).replace('<name>', WIDE_DIRECTION, 1)
        s, left = fill(s, {'tag': COEFF_BRANCH, 'peel': d['sha'][:8], 'run id': d['run'], 'axioms': 'axioms: %s' % (', '.join(axs) or 'none')})
        rec.update(outcome='COMPILED', sentence=s, unfilled=left, direction_axioms=list(ax[dirn[0]]))
        out.append('  THE OUTCOME: COMPILED on %s at %s, the branch and commit in the tag`s place as (4) orders for (5); no main moved and no tag cut' % (
            COEFF_BRANCH, d['sha'][:8]))
        out.append('  %s`s own axioms: [%s]' % (WIDE_DIRECTION, ', '.join(ax[dirn[0]]) or 'none'))
    else:
        where = None
        for l in rd.get('errors') or []:
            m = re.search(r'([A-Za-z0-9_/.]+\.lean):(\d+):\d+: error', l)
            if m:
                where = '%s :%s, run %s' % (m.group(1), m.group(2), d['run'])
                break
        where = where or 'run %s: %s' % (d['run'], 'the build exit %s' % rd.get('build_exit') if not built else '%d of %d names without a line within '
                                         'the standard three' % (len(q) - len(within), len(q)))
        rec.update(outcome='NOT COMPILED AT THIS RUN', sentence=None, unfilled=None, where=where)
        out.append('  THE OUTCOME AT THIS RUN: NOT COMPILED (%s); the stop sentence of (7) is composed only where the item stops' % where)
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


def t0():
    return coeff('T0')


def t1():
    return coeff('T1')


def bank():
    lines, recs = [], []
    for fn in (join, t0, t1, mod24, wide):
        o, r = fn()
        lines += o + ['']
        if r:
            recs.append(r)
    head = ['%s -- (R367)(4)-(7): EACH RESULT`S SENTENCE, THE RULING`S TEXT WITH ITS FIELDS FILLED FROM THE ACT`S BANKS (tools/b757_outcomes.py)' % ACT, '']
    tail = ['### ### **THE OUTCOMES: %s.**' % ' ; '.join('%s %s' % (r['item'].upper(), r['outcome']) for r in recs)]
    txt = NL.join(head + lines + tail) + NL
    with open(BANK, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    tmp = BANKJ + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(recs, f, ensure_ascii=False, indent=1)
        f.write(NL)
    os.replace(tmp, BANKJ)
    print(txt)
    print('written data/b757_outcomes.txt and data/b757_outcomes.json (%d items)' % len(recs))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] not in ('join', 'T0', 'T1', 'mod24', 'wide', 'bank'):
        sys.exit(__doc__)
    if a[0] in ('join', 'T0', 'T1', 'mod24', 'wide'):
        o, _r = dict(join=join, T0=t0, T1=t1, mod24=mod24, wide=wide)[a[0]]()
        print(NL.join(o))
    else:
        bank()
