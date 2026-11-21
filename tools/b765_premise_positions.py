# -*- coding: utf-8 -*-
"""b765 under (R375)(6)(a): W-ORD-PREMISE-POSITIONS READ (OPEN_TRAILS :18985), a reading and no build; no order is retired.

THE PREMISES: the W-ORD-PREMISE-* rows of OPEN_TRAILS :13433-:13453 at PLACE-papers' HEAD, each parsed for its order, its premise, its kernel,
path, line and pin; each order's status by tools/standing/orders.py at HEAD. The eighteen OPEN are read; the three CLOSED (retired at b724 by
the author's word) are listed by order and the line that decides them, and given no position. Each trail line is cited by line and digest,
never quoted; no line of PLACE-papers is written.

THE READER, canon XXV (phase1.5/method/THE_METHOD_CANON.md :397, cited by digest) in the order's four, the seat's reading of each position
written as a rule a declaration can be tested against (the seat's words, not the canon's):
  the kernel's declarations are read at its main, comments stripped; a theorem's statement runs from its keyword to its `:=` (or to its first
  equation line `|`); its binders are the bracketed groups before the first top-level `:`, its conclusion what follows; a binder TAKES the
  premise where its type opens with the premise's name, or with any `x.<name>` for a name under a namespace; a declaration is COMPILED where
  its body, to the next declaration, holds no `sorry` and no `admit` (the kernels' builds are not re-run here, a reader's limit, beside the
  control's axioms line from a runner build);
  EQUIVALENT TO THE HYPOTHESIS: a compiled theorem concluding `<premise> <-> RiemannHypothesis` (either order), each explicit binder taking it;
  IMPLIES THE HYPOTHESIS: a compiled theorem concluding RiemannHypothesis whose explicit binders each take the premise (at least one), or
  concluding `<premise> -> RiemannHypothesis` with no explicit binder;
  DERIVED: the premise a closed statement (no binder of its own) and a compiled theorem with no explicit binder concluding it;
  A HYPOTHESIS BY DESIGN ("part of what a theorem is about"): the premise a predicate (binders of its own: a statement about the theorem's
  variables) and a compiled theorem taking it whose conclusion is not the Hypothesis;
  NONE OF THESE COMPILED otherwise. A closed premise taken as a hypothesis is a fact assumed, not a theorem's subject, so it is not by design;
  a theorem concluding the Hypothesis under further explicit hypotheses compiles no relation of the premise alone: each such edge, a compiled
  theorem concluding the Hypothesis whose binders name the premise in any form, is printed with the binders naming it and the others by name.
THE CONSEQUENCE, by the order's own list (OPEN_TRAILS :18985): by design, put to the author for retirement with the reason; derived, carried
with the declaration; of the Hypothesis's strength (equivalent or implies), put for retirement with its position written and one shared
sentence naming Weil positivity on classK; none, the order stands. No order is retired by this act.
THE CONTROL, before the rows ((R375)(6)(a)): Weil positivity on classK, h2_sign of SIDE-explicit-formula at main, read by the same reader,
prints EQUIVALENT TO THE HYPOTHESIS by the declaration that compiles the relation; beside it, that declaration's axioms line in the runner's
axioms file of b765's dispatch 2 (run 44909786283, the standard three). The reader's own planted controls run first.

Routes: `read` prints, writes nothing; `bank` writes data/b765_premise_positions.txt, refused unless this file is committed and unchanged at
the relay's HEAD. Kernel lines are written only as a premise's statement opening (its signature to `:=`, at most 120 characters, masked) and
declarations by name and place."""
import hashlib, io, os, re, subprocess, sys

R = 'D:/relay'
PP = 'D:/MY-DOwnloads/PLACE-papers'
EF = 'D:/SIDE-explicit-formula'
BANK = os.path.join(R, 'data', 'b765_premise_positions.txt')
ME = 'tools/b765_premise_positions.py'
NL = '\n'
ROWS = (13433, 13453)
ORDER_LINE = 18985
CANON, CANON_LINE = 'phase1.5/method/THE_METHOD_CANON.md', 397
CONTROL_RUN = 44909786283
CONTROL_AXIOMS = 'D:/b765-runs/ef-%d/build-module-%d/axioms.txt' % (CONTROL_RUN, CONTROL_RUN)
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
RX = re.compile(r'\*\*(W-ORD-PREMISE-[A-Z0-9-]+)\*\*: the premise (\S+), (SIDE-[A-Za-z0-9-]+) (\S+) :(\d+) at ([0-9a-f]+);')
THM = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma)\s+([^\s:({\[]+)')
ANYDECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*'
                     r'(theorem|lemma|def|abbrev|structure|class|instance|inductive|opaque|axiom|example)\b|^\s*(?:end|namespace|section)\b')
BYD, DER, EQV, IMP, NONE = ('A HYPOTHESIS BY DESIGN', 'DERIVED', 'EQUIVALENT TO THE HYPOTHESIS', 'IMPLIES THE HYPOTHESIS', 'NONE OF THESE COMPILED')
ORDER_OF = (BYD, DER, EQV, IMP)   # ### the order's list: by design ; derived ; of the Hypothesis's strength
CONSEQUENCE = {BYD: 'put to the author for retirement with the reason, the theorem it is part of',
               DER: 'carried with the declaration that proves it',
               EQV: 'put to the author for retirement, its position written, with the shared sentence naming Weil positivity on classK',
               IMP: 'put to the author for retirement, its position written, with the shared sentence naming Weil positivity on classK',
               NONE: 'the order stands'}
# ### the seat's hand-read of each premise, written after reading each statement and its theorems at main (scratch premw765.py, premv765.py,
# ### premu765.py, 13:38Z-13:43Z) and before this tool's first run
HAND = {'BoundPremises': NONE, 'Dealigned': BYD, 'DealignedAt': BYD, 'IdempotentAdd': BYD, 'IsEvenFn': BYD, 'IsExpansion': BYD,
        'IsSignedCompletion': BYD, 'IsTrivialPoint': BYD, 'NontrivialZeroExistsInStrip': NONE, 'NotDiv': BYD, 'PerClassExcludes': NONE,
        'Proper': BYD, 'Register4_channelInequality': BYD, 'Register4_positivity': NONE, 'SelfDualFE': BYD, 'ZeroActingPairing': BYD,
        'identity': BYD, 'is_xi_zero': BYD}
# ### the seat's first table, held before the rule was written and banked nowhere: three premises it read otherwise
FIRST_TABLE = {'PerClassExcludes': BYD, 'Register4_channelInequality': NONE, 'ZeroActingPairing': NONE}
sys.path.insert(0, os.path.join(R, 'tools'))
sys.path.insert(0, os.path.join(R, 'tools', 'standing'))
import b765_held_branches as HB   # noqa: E402  (its mask and comment stripper, unchanged)
import orders as OR                # noqa: E402


def git(repo, *a, ok=False):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0 and not ok:
        raise SystemExit('### git %s failed (exit %d) -- nothing written' % (' '.join(a[:2]), r.returncode))
    return r.stdout if r.returncode == 0 else None


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


# ================================================================================ the parse
def groups(rest):
    """(binder groups [(bracket, names, type)], conclusion or None) of a signature's text after the declaration's name."""
    out, i, n, depth, start = [], 0, len(rest), 0, None
    opens, closes = '({[\u2983\u27e8', ')}]\u2984\u27e9'
    while i < n:
        c = rest[i]
        if c in opens:
            if depth == 0:
                start = i
            depth += 1
        elif c in closes:
            depth -= 1
            if depth == 0 and start is not None:
                g = rest[start:i + 1]
                inner, d2, cut = g[1:-1], 0, None
                for j, x in enumerate(inner):
                    if x in opens:
                        d2 += 1
                    elif x in closes:
                        d2 -= 1
                    elif x == ':' and d2 == 0 and inner[j:j + 2] != ':=':
                        cut = j
                        break
                out.append((g[0], inner[:cut].strip() if cut is not None else '', (inner[cut + 1:] if cut is not None else inner).strip()))
                start = None
        elif c == ':' and depth == 0 and rest[i:i + 2] != ':=':
            return out, rest[i + 1:].strip()
        i += 1
    return out, None


def norm(s):
    return re.sub(r'\s+', ' ', s or '').strip()


def theorems_of(text, path):
    """[dict(name, path, line, binders, concl, compiled)] for each theorem or lemma of `text` (comments stripped, lines kept)."""
    L = HB.strip_comments(text.replace('\r', '')).split(NL)
    heads = [k for k, l in enumerate(L) if ANYDECL.match(l)]
    out = []
    for k, l in enumerate(L):
        m = THM.match(l)
        if not m:
            continue
        nxt = next((h for h in heads if h > k), len(L))
        sig, stop = [], False
        for j in range(k, nxt):
            s = L[j]
            if j > k and s.strip().startswith('|'):
                break
            if ':=' in s:
                sig.append(s.split(':=')[0])
                stop = True
                break
            sig.append(s)
        st = norm(' '.join(sig))
        rest = st[st.find(m.group(2)) + len(m.group(2)):]
        b, c = groups(rest)
        body = NL.join(L[k:nxt])
        out.append(dict(name=m.group(2), path=path, line=k + 1, binders=b, concl=norm(c), compiled=not re.search(r'\b(?:sorry|admit)\b', body),
                        closed_sig=stop))
    return out


def head_rx(name):
    last = name.split('.')[-1]
    return re.compile(r'^\s*(?:[^\s.()\[\]{}\u27e8\u27e9:,]+\.)*' + re.escape(last) + r"(?![\w'])")


def applied(t, hx):
    """the binder's type is the premise applied: it opens with the name and holds no arrow, iff, and or or at its top level (so that a
    hypothesis `P x -> RiemannHypothesis` does not take P)."""
    if not hx.match(t):
        return False
    d = 0
    for ch in t:
        if ch in '({[⟨':
            d += 1
        elif ch in ')}]⟩':
            d -= 1
        elif d == 0 and ch in '→↔∧∨':
            return False
    return '->' not in re.sub(r'\([^()]*\)', '', t)


def premise_sig(text, line, name):
    """(signature to `:=` normalized, closed) of the declaration of `name` at or within three lines after `line`."""
    L = HB.strip_comments(text.replace('\r', '')).split(NL)
    last = name.split('.')[-1]
    for k in range(max(0, line - 2), min(len(L), line + 3)):
        m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable)\s+)*(def|abbrev|structure|class|inductive)\s+([^\s:({\[]+)', L[k])
        if m and m.group(2).split('.')[-1] == last:
            buf = []
            for j in range(k, min(k + 12, len(L))):
                buf.append(L[j])
                if ':=' in L[j] or re.search(r'\swhere\s*$', L[j]):
                    break
            st = norm(' '.join(buf).split(':=')[0])
            st = re.sub(r'\swhere$', '', st)
            rest = st[st.find(m.group(2)) + len(m.group(2)):]
            return st, rest.lstrip().startswith(':'), k + 1
    return None, None, None


def positions(name, closed, thms):
    """{position: [theorem]} held by the premise among the compiled theorems `thms`, by the rule of this file's head; and the theorems taking
    it, and its edges to the Hypothesis (compiled theorems taking it and concluding the Hypothesis), each with its other explicit binders."""
    hx = head_rx(name)
    wx = re.compile(r"(?<![\w'])" + re.escape(name.split('.')[-1]) + r"(?![\w'])")
    held = dict((p, []) for p in ORDER_OF)
    takes, edges = [], []
    for t in thms:
        if not t['compiled']:
            continue
        expl = [g for g in t['binders'] if g[0] in ('(', '\u2983')]
        tk = [g for g in t['binders'] if applied(g[2], hx)]
        others = [g for g in expl if not applied(g[2], hx)]
        c = t['concl']
        if tk:
            takes.append(t)
        # ### an edge: a compiled theorem concluding the Hypothesis whose binders name the premise in any form (taken, or inside a
        # ### hypothesis's type), with the binders naming it and the other explicit binders
        ment = [g for g in t['binders'] if wx.search(g[2])]
        if ment and 'RiemannHypothesis' in c:
            edges.append((t, [g[1] or '(anonymous)' for g in ment], [g[1] for g in expl if g not in ment]))
        m1 = re.match(r'^(.+?)\s*\u2194\s*RiemannHypothesis$', c) or re.match(r'^RiemannHypothesis\s*\u2194\s*(.+)$', c)
        if m1 and applied(m1.group(1), hx) and not others:
            held[EQV].append(t)
        if (c == 'RiemannHypothesis' and expl and not others) or (re.match(r'^(.+?)\s*\u2192\s*RiemannHypothesis$', c) and not expl
                                                                     and applied(re.match(r'^(.+?)\s*\u2192', c).group(1), hx)):
            held[IMP].append(t)
        if closed and not expl and hx.match(c) and re.fullmatch(r"(?:[^\s.()\[\]{}:,]+\.)*" + re.escape(name.split('.')[-1]), c):
            held[DER].append(t)
        if not closed and tk and 'RiemannHypothesis' not in c:
            held[BYD].append(t)
    return dict((p, v) for p, v in held.items() if v), takes, edges


def primary(held):
    for p in ORDER_OF:
        if p in held:
            return p
    return NONE


def strength(p):
    return 'OF THE HYPOTHESIS`S STRENGTH' if p in (EQV, IMP) else p


# ================================================================================ the reads
def kernel_theorems(kd, rev, name):
    files = [l.split(':', 1)[1] for l in (git(kd, 'grep', '-l', '-w', name.split('.')[-1], rev, '--', '*.lean', ok=True) or '').split(NL) if l.strip()]
    out = []
    for f in files:
        out += theorems_of(git(kd, 'show', '%s:%s' % (rev, f)) or '', f)
    return out, len(files)


def axioms_line(full):
    if not os.path.exists(CONTROL_AXIOMS):
        return None
    t = io.open(CONTROL_AXIOMS, encoding='utf-8', errors='replace').read()
    m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(full), t)
    return tuple(x.strip() for x in m.group(1).replace('\n', ' ').split(',')) if m else None


def read_premise(order, name, kern, path, line, pin):
    kd = 'D:/' + kern
    held_pin = bool((git(kd, 'rev-parse', '--verify', '-q', pin + '^{commit}', ok=True) or '').strip())
    sig, closed, at = premise_sig(git(kd, 'show', '%s:%s' % (pin, path), ok=True) or '', line, name) if held_pin else (None, None, None)
    main = git(kd, 'rev-parse', '--short=8', 'main').strip()
    thms, nf = kernel_theorems(kd, 'main', name)
    held, takes, edges = positions(name, bool(closed), thms)
    return dict(order=order, name=name, kern=kern, path=path, line=line, pin=pin, held_pin=held_pin, sig=sig, closed=closed, sig_at=at, main=main,
                files=nf, theorems=len(thms), held=held, takes=takes, edges=edges, primary=primary(held))


def control():
    """the reader's own planted controls, then the control of (6)(a)."""
    P = [('def Pp (x : Nat) : Prop := x = x\ntheorem useP (x : Nat) (h : Pp x) : x + 0 = x := by simp\n', 'Pp', BYD),
         ('def Q : Prop := True\ntheorem q_iff : Q \u2194 RiemannHypothesis := sorry\ntheorem q_iff2 : Q \u2194 RiemannHypothesis := \u27e8a, b\u27e9\n', 'Q', EQV),
         ('def Q : Prop := True\ntheorem q_rh (li : Q \u2192 RiemannHypothesis) (h : Q) : RiemannHypothesis := li h\ntheorem q_use (h : Q) : 1 = 1 := rfl\n', 'Q', NONE),
         ('def Q : Prop := True\ntheorem q_holds : Q := trivial\n', 'Q', DER),
         ('def Pp (x : Nat) : Prop := x = x\ntheorem rh_of (x : Nat) (h : Pp x) : RiemannHypothesis := sorry\n', 'Pp', NONE),
         ('def Line.Proper (L : Nat) : Prop := True\ntheorem t (L : Nat) (hp : L.Proper) : 0 = 0 := rfl\n', 'Line.Proper', BYD),
         ('def Q : Prop := True\ntheorem imp : Q \u2192 RiemannHypothesis := fun h => x\n', 'Q', IMP),
         ("def Pp (x : Nat) : Prop := x = x\ntheorem e (T : Nat) (h : Pp T) :\n    T = T\n  | 0 => rfl\n", 'Pp', BYD),
         ("def Pp (x : Nat) : Prop := x = x\ntheorem u (h : Pp' 0) : 0 = 0 := rfl\n", 'Pp', NONE),
         ('def Pp (x : Nat) : Prop := x = x\ntheorem r4 {x : Nat} (li : Pp x → RiemannHypothesis) (h : Pp x) : RiemannHypothesis := li h\n',
          'Pp', NONE)]
    got = []
    for text, nm, want in P:
        _s, closed, _a = premise_sig(text, 1, nm)
        held, _t, _e = positions(nm, bool(closed), theorems_of(text, 'planted'))
        got.append((primary(held), want))
    ok1 = all(a == b for a, b in got)
    L = ['  THE READER`S PLANTED CONTROLS (ten texts: a predicate taken ; a closed statement equivalent, its sorry form refused ; a closed '
         'statement taken and implying the Hypothesis only under another hypothesis ; a closed statement proved ; a predicate implying the '
         'Hypothesis by sorry ; a premise under a namespace taken by dot notation ; a closed statement implying the Hypothesis ; a theorem by '
         'equations ; a primed name not taken ; a predicate implying the Hypothesis only under a hypothesis whose type opens with it, R4`s '
         'shape): %s -> %s' % ([g[0] for g in got], 'AS WANTED' if ok1 else 'NOT AS WANTED')]
    c = read_premise('(the control)', 'h2_sign', 'SIDE-explicit-formula', 'SIDEExplicitFormula/H2Sign.lean', 29, 'main')
    grounds = ['%s %s:%d' % (t['name'], t['path'], t['line']) for t in c['held'].get(EQV, [])]
    ax = axioms_line('SIDEExplicitFormula.B321.h2_sign_iff_rh')
    ok2 = (c['primary'] == EQV and any(t['name'] == 'h2_sign_iff_rh' and t['path'] == 'SIDEExplicitFormula/Seam.lean' and t['line'] == 101
                                       for t in c['held'].get(EQV, [])) and ax is not None and set(ax) <= set(STANDARD))
    L.append('  THE CONTROL OF (R375)(6)(a): Weil positivity on classK, h2_sign of SIDE-explicit-formula (H2Sign.lean :%s at main %s, its statement '
             'opening `%s`, closed %s), read by the same reader over %d theorems in %d files: %s by %s ; the runner`s axioms line for '
             'SIDEExplicitFormula.B321.h2_sign_iff_rh (run %d): %s -> %s' % (
                 c['sig_at'], c['main'], HB.mask(c['sig'] or '')[:120], c['closed'], c['theorems'], c['files'], c['primary'], '; '.join(grounds) or 'NONE',
                 CONTROL_RUN, '[%s]' % ', '.join(ax) if ax else 'NO LINE', 'AS WANTED' if ok2 else 'NOT AS WANTED'))
    return L, ok1 and ok2


def trail():
    T = (git(PP, 'show', 'HEAD:OPEN_TRAILS.md') or '').replace('\r', '').split(NL)
    st = dict(OR.read(OR.trail('HEAD')))
    rows = []
    for n in range(ROWS[0], ROWS[1] + 1):
        m = RX.search(T[n - 1])
        if not m:
            raise SystemExit('### OPEN_TRAILS :%d not parsed as a premise row -- nothing written' % n)
        o = st.get(m.group(1)) or {}
        rows.append((n, digest(T[n - 1]), m.groups(), o.get('status', 'ABSENT'), o.get('decided_at')))
    return T, rows


def self_commit():
    b = git(R, 'hash-object', ME).strip()
    h = (git(R, 'rev-parse', 'HEAD:' + ME, ok=True) or '').strip()
    if b != h or (git(R, 'status', '--porcelain', '--', ME) or '').strip():
        raise SystemExit('### %s differs from its blob at HEAD or is not committed -- the bank refused, nothing written' % ME)
    return git(R, 'rev-parse', '--short=8', 'HEAD').strip(), hashlib.sha256(io.open(os.path.join(R, ME), 'rb').read()).hexdigest()[:16]


def compose(at, tool):
    cl, cok = control()
    if not cok:
        print(NL.join(cl))
        raise SystemExit('### THE CONTROL NOT AS WANTED -- no row read, nothing written')
    T, rows = trail()
    C = (git(PP, 'show', 'HEAD:' + CANON) or '').replace('\r', '').split(NL)
    pph = git(PP, 'rev-parse', '--short=8', 'HEAD').strip()
    opn = [r for r in rows if r[3] == 'OPEN']
    shut = [r for r in rows if r[3] != 'OPEN']
    reads = [dict(read_premise(r[2][0], r[2][1], r[2][2], r[2][3], int(r[2][4]), r[2][5]), row=r[0], dg=r[1]) for r in opn]
    out = ['b765 -- (R375)(6)(a): W-ORD-PREMISE-POSITIONS READ, EACH PREMISE AT ITS STATEMENT AT ITS PIN, GIVEN ITS POSITION UNDER CANON XXV (%s)' % at,
           '',
           '## THE SOURCES',
           '  the order: OPEN_TRAILS :%d (sha256 %s) ; the canon`s positions: %s :%d (sha256 %s) ; the rows: OPEN_TRAILS :%d-:%d, each by line and '
           'digest below ; PLACE-papers at HEAD %s, read by git, no line of it written ; the statuses by tools/standing/orders.py at HEAD' % (
               ORDER_LINE, digest(T[ORDER_LINE - 1]), CANON, CANON_LINE, digest(C[CANON_LINE - 1]), ROWS[0], ROWS[1], pph),
           '  the tool: %s, committed at relay %s, sha256 %s ; its rule of each position stands in its head, the seat`s words' % (ME, tool[0], tool[1]),
           '  the trail`s rows %d: OPEN %d, read below ; CLOSED %d, listed and given no position' % (len(rows), len(opn), len(shut)),
           '',
           '## THE CONTROL, BEFORE THE ROWS'] + cl + ['']
    out.append('## THE ROWS, ONE A PREMISE: the order | the premise | its kernel, path, line and pin (the pin held ; its trail row) | its statement`s '
               'opening at the pin | its position | the declaration that grounds it, at the kernel`s main | its edges to the Hypothesis | the '
               'consequence the order names | the seat`s hand-read')
    agree = 0
    for i, r in enumerate(reads, 1):
        p = r['primary']
        g = r['held'].get(p, [])
        if p == NONE:
            if r['closed'] and r['takes']:
                ground = 'none: a closed statement, taken as an assumed fact by %s' % ', '.join('%s (%s:%d)' % (t['name'], t['path'], t['line'])
                                                                                                  for t in r['takes'][:3])
            elif r['takes']:
                ground = 'none: taken only by theorems concluding the Hypothesis, %s' % ', '.join('%s (%s:%d)' % (t['name'], t['path'], t['line'])
                                                                                                  for t in r['takes'][:3])
            else:
                ground = 'none: no compiled theorem at main takes it'
        else:
            ground = '%s (%s:%d)%s' % (g[0]['name'], g[0]['path'], g[0]['line'], (' and %d more' % (len(g) - 1)) if len(g) > 1 else '')
        eds = '; '.join('%s (%s:%d), naming it in %s, under %s' % (t['name'], t['path'], t['line'], ', '.join(mn), ', '.join(o) or 'no other explicit binder')
                        for t, mn, o in r['edges'][:4]) + ((' ; and %d more' % (len(r['edges']) - 4)) if len(r['edges']) > 4 else '')
        h = HAND.get(r['name'])
        agree += h == p
        out.append('    (%d) %s | %s | %s %s :%d at %s (held %s ; OPEN_TRAILS :%d sha256 %s) | `%s` | %s | %s, at main %s | %s | %s | hand-read %s' % (
            i, r['order'], r['name'], r['kern'], r['path'], r['line'], r['pin'], r['held_pin'], r['row'], r['dg'], HB.mask(r['sig'] or 'NOT READ')[:120],
            p, ground, r['main'], ('edges to the Hypothesis: ' + eds) if eds else 'no edge to the Hypothesis', CONSEQUENCE[p],
            'AGREES' if h == p else 'READS %s' % h))
    out.append('')
    out.append('## THE THREE CLOSED, NO POSITION GIVEN')
    for r in shut:
        out.append('    %s | %s | %s %s :%s at %s | OPEN_TRAILS :%d sha256 %s | %s, decided at OPEN_TRAILS :%s' % (
            r[2][0], r[2][1], r[2][2], r[2][3], r[2][4], r[2][5], r[0], r[1], r[3], r[4]))
    out.append('')
    cnt = dict((k, sum(1 for r in reads if strength(r['primary']) == k)) for k in (BYD, DER, 'OF THE HYPOTHESIS`S STRENGTH', NONE))
    out.append('## THE COUNTS, IN [Q1]`S ORDER')
    out.append('  A HYPOTHESIS BY DESIGN %d ; DERIVED %d ; OF THE HYPOTHESIS`S STRENGTH %d ; none of these compiled %d ; of %d' % (
        cnt[BYD], cnt[DER], cnt['OF THE HYPOTHESIS`S STRENGTH'], cnt[NONE], len(reads)))
    multi = [r['name'] for r in reads if len(r['held']) > 1]
    out.append('  premises holding more than one of the four: %d %s ; the seat`s hand-read agrees with the rule on %d of %d' % (len(multi), multi, agree, len(reads)))
    diff = ['%s (the first table %s, the rule %s)' % (k, v, next(r['primary'] for r in reads if r['name'] == k)) for k, v in sorted(FIRST_TABLE.items())]
    out.append('  the seat`s first table, held before the rule was written and banked nowhere, read three premises otherwise: %s ; the rows above '
               'carry the rule`s reading' % '; '.join(diff))
    out.append('')
    ret = [r for r in reads if r['primary'] in (BYD, EQV, IMP)]
    out.append('## THE ROWS WHOSE CONSEQUENCE IS RETIREMENT, FOR THE ROOT`S QUESTION (no order retired by this act; the author strikes)')
    for r in ret:
        g = r['held'][r['primary']][0]
        out.append('    %s (%s): %s by %s (%s:%d)' % (r['order'], r['name'], r['primary'], g['name'], g['path'], g['line']))
    out.append('')
    out.append('## THE READER`S LIMITS')
    out.append('  COMPILED is read as no sorry and no admit in the declaration`s body at the kernel`s main; the kernels other than SIDE-explicit-formula '
               'are not built by this act, and the control`s declaration is read beside its runner axioms line')
    out.append('  a theorem is found where its file names the premise as a word at main; its statement is read to its `:=` or its first equation line; '
               'a binder takes the premise where its type opens with the name')
    out.append('  "part of what a theorem is about" is read as the rule of the tool`s head: a predicate taken by a compiled theorem not concluding the '
               'Hypothesis; a closed statement taken as a hypothesis is an assumed fact')
    out.append('')
    out.append('### ### **PREMISES %d: A HYPOTHESIS BY DESIGN %d, DERIVED %d, OF THE HYPOTHESIS`S STRENGTH %d, NONE OF THESE COMPILED %d ; THE CONTROL %s ; '
               'NO ORDER RETIRED.**' % (len(reads), cnt[BYD], cnt[DER], cnt['OF THE HYPOTHESIS`S STRENGTH'], cnt[NONE], 'AS WANTED'))
    return out


def main():
    a = sys.argv[1:]
    import datetime
    at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    if a == ['read']:
        print(NL.join(compose(at, ('(read)', '-'))))
    elif a == ['bank']:
        tool = self_commit()
        body = NL.join(compose(at, tool)) + NL
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(body)
        os.replace(BANK + '.tmp', BANK)
        print(body)
        print('written data/b765_premise_positions.txt: %d lines, sha256 %s' % (body.count(NL), hashlib.sha256(body.encode('utf-8')).hexdigest()[:16]))
    elif a == ['control']:
        L, ok = control()
        print(NL.join(L))
        print('### THE CONTROLS %s' % ('AS WANTED' if ok else 'NOT AS WANTED'))
        sys.exit(0 if ok else 1)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
