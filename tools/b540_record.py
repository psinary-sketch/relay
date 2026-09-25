# -*- coding: utf-8 -*-
"""b540_record.py -- THE CASCADE, ACT TWO: THE RECORD, UNDER (R150).
### `python tools/b540_record.py purpose | file | law | sentences | paths | erratum4 | findings | components | desk | trail`

### Every keystone write is ONE append after the file's last byte, except ERRATA's one declared bullet insert. Tiers and
### sentence grades are the seat's statement-reads, typed beside their reasons; each typed row must meet exactly one live row
### or selected sentence, or the tool refuses. This file deletes nothing.
"""
import html, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERR = os.path.join(PP, 'ERRATA.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SURR = os.path.join(PP, 'phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
FIND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
DEPM = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
NL = chr(10)
MAPH = '### The tier law corrected under (R150), 2026-09-25 -- the RH-anchor named, T1 split (appended by b540; the appendix above is unedited)'
SURRH = '### The tier table corrected under (R150), 2026-09-25 (appended by b540; the table above is unedited)'
PATHSH = '## The tiers of (R149)-(R150), appended 2026-09-25 by b540 -- PATHS tiered against the RH-anchor (no line above this block changes)'
FTITLE = '## The cascade, act two: the tier law corrected, PATHS_TO_THE_CRITICAL_LINE tiered against the RH-anchor'
HEADING = ('### b540 — the cascade`s second act under (R150): E-2026-09-25-3 filed, the tier and the RH-anchor separated, T1 split, '
           'PATHS tiered, E-2026-09-25-4 drafted')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def append_to(path, text):
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def outside_code_backticks(text):
    """### backticks not closed within their own line -- a possessive, or a stray."""
    n = 0
    for l in text.split(NL):
        n += l.count('`') % 2
    return n


# ------------------------------------------------------------------------------ READING (1)
def purpose():
    L = ['b540 -- THE PURPOSE STATEMENTS OF THE KEYSTONES THIS ACT TOUCHES, PRINTED BEFORE ANY WRITE', '']
    for path, ln, head in ((PATHS, 11, '**PURPOSE:**'), (MAP, 8, '**PURPOSE:**'), (SURR, 23, '**Role.**')):
        l = rd(path).split(NL)[ln - 1]
        assert l.startswith(head), (path, l[:40])
        L += ['%s:%d' % (os.path.relpath(path, PP).replace(os.sep, '/'), ln), '  ' + l, '']
    io.open(os.path.join(D, 'b540_purpose.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 1
STATUS3 = ("**Filed 2026-09-25 by b540, the cascade's second act, on the author's ruling (R150)(1), as drafted at relay "
           "data/b539_erratum_draft.md, its bytes unchanged; the heading's words \"DRAFT, NOT FILED\" are the draft's, retained as "
           "drafted. Whether SIDE-lv-conservation's Zenodo description is edited under (R110) is a separate ruling, not taken here.**")
BULLET3 = ("- `E-2026-09-25-3` — *DEPOSIT-FACING FOR SIDE-lv-conservation v0.10.0; CORPUS-FACING FOR THE UNCONDITIONAL SURROUND v0.4* "
           "(appended to this list by b540 under `(R150)`(1))")


def file():
    raw = open(ERR, 'rb').read()
    if b'## E-2026-09-25-3 ' in raw:
        sys.exit('### E-2026-09-25-3 IS ALREADY IN ERRATA -- REFUSING TO FILE IT TWICE.')
    lines = raw.decode('utf-8').split(NL)
    k = next(i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-22-1` —'))
    assert lines[k + 1].strip() == '', lines[k + 1][:60]
    before_lines = list(lines)
    lines = lines[:k + 1] + [BULLET3] + lines[k + 1:]
    open(ERR, 'wb').write(NL.join(lines).encode('utf-8'))
    kept = [l for i, l in enumerate(lines) if i != k + 1] == before_lines
    draft = io.open(os.path.join(D, 'b539_erratum_draft.md'), encoding='utf-8').read()
    w = append_to(ERR, NL + draft.rstrip(NL) + NL + NL + STATUS3 + NL)
    t = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(t) if l.startswith('## E-2026-09-25-3 ')) + 1
    last = next(i for i, l in enumerate(t) if l.startswith('**Filed 2026-09-25 by b540')) + 1
    entry = NL.join(t[first - 1:last])
    res = dict(bullet_line=k + 2, prior_lines_kept=kept, append=w, entry_lines=[first, last],
               entry_equals_draft=(draft.rstrip(NL) in entry), backticks_outside_code=outside_code_backticks(entry))
    put_json('b540_file.json', res)
    print('  bullet inserted at ERRATA.md:%d (prior lines kept %s)' % (k + 2, kept))
    print('  E-2026-09-25-3 at ERRATA.md:%d-%d ; draft bytes carried %s ; backticks outside code spans %d'
          % (first, last, res['entry_equals_draft'], res['backticks_outside_code']))


# ------------------------------------------------------------------------------ COMPONENT 2
FIVE = [('h1_complete_at_Phi', 'a true fact about zeta`s theta kernel `Phi` (its eight coupling facts) that says nothing about the zeros` location'),
        ('C7_finite_type_false', 'a true fact about the growth of `completedRiemannZeta₀` that says nothing about the zeros` location'),
        ('blTerm_nonneg_of_onLine', 'a true fact about the Li terms of zeros already on the line that says nothing about where the zeros are'),
        ('spectral_cannon', 'a true fact about the derivative of `completedRiemannZeta₀` on the line that says nothing about the zeros` location'),
        ('ξ / Dirichlet order-≤1 inputs', 'true growth bounds on `completedRiemannZeta₀` and `completedLFunction` that say nothing about the zeros` location')]
MAP_COUNTS = dict(T0=5, **{'T1-open': 0, 'T1-lit': 1}, T2=6, T3=0, T4=0)
SURR_COUNTS = dict(T0=3, **{'T1-open': 0, 'T1-lit': 1}, T2=7, T3=0, T4=4)


def law():
    tj = jl('b539_tiers.json')
    rk = {r['terminal']: r['tier'] for r in tj['ranked']}
    assert all(rk[n] == 'T0' for n, _ in FIVE) and rk['partialPositivity_finiteRange'] == 'T4'
    new = dict(rk, partialPositivity_finiteRange='T1-lit')
    got = {t: sum(1 for v in new.values() if v == t) for t in MAP_COUNTS}
    assert got == MAP_COUNTS, got
    M = ['', '<!-- b540 (R150) TIER-LAW LINES, 2026-09-25 -->', '', MAPH, '',
         '**The RH-anchor, `(R150)`(2).** The anchor is the subset of T0 that bears on where zeta`s zeros are: **`h2_sign_iff_rh`** '
         '(SIDE-explicit-formula v0.2 = `5c72cad`), **ranked here at the head of the hub terminals**; then `ch_iff_rh`; the register '
         'census theorems `not_register1`, `mellin_Phi_eq_zero_of_re_le_one`, `lvh2_corrected_iff`, `register5_output_holds`; '
         '`b321_identity`; `not_f4_needs`. T0 is a tier -- a theorem stated against Mathlib`s own objects, standard three, no premise, '
         'statement read -- and the anchor is a subset of it; `(R149)`(1) conflated the two, and b539`s (N1) was refuted by that '
         'conflation.', '',
         '**The five ranked terminals that are T0 and not in the RH-anchor, each with its one clause:**', '']
    M += ['- `%s` -- **T0**: %s.' % (n, c) for n, c in FIVE]
    SPACED = [('', '')]
    M += ['', '**T1 split, `(R150)`(3).** `partialPositivity_finiteRange` is **T1-lit**, not T4: it INTERFACES on literature theorems '
              'not yet compiled (Bombieri–Lagarias`s decomposition `ExplicitFormulaDecomp`, Voros`s tail bound `TailBoundPremise`) and '
              'on the numerical `VerifiedZerosTo T`; it becomes T0 when they compile and nothing else changes. T4 is for a claim with no '
              'terminal at all. No ranked terminal is T1-open. `ConservationBridge.riemann_hypothesis` stays **T2**: its premise is RH '
              'restated by the rewording lemma `ch_iff_rh`, so it is ENCODES-CONCLUSION per `(R149)`(2)`s own list (the reading is '
              'flagged for the author, since `(R150)`(3)`s parenthesis read alone would place it at T1-open).', '',
          '**Corrected counts over the twelve ranked terminals:** ' + ' · '.join('%s %d' % kv for kv in MAP_COUNTS.items()) + '.', '']
    w1 = append_to(MAP, NL.join(M))
    su = jl('b539_surr.json')
    srk = {r['line']: r['tier'] for r in su['rows']}
    assert srk[187] == 'T4'
    snew = dict(srk)
    snew[187] = 'T1-lit'
    sgot = {t: sum(1 for v in snew.values() if v == t) for t in SURR_COUNTS}
    assert sgot == SURR_COUNTS, sgot
    S = ['', '<!-- b540 (R150) TIER-TABLE LINES, 2026-09-25 -->', '', SURRH, '',
         '- **`:187` `PartialPositivity.partialPositivity_finiteRange` -- T4 → T1-lit** (`(R150)`(3)): it INTERFACES on literature '
         'theorems not yet compiled (`ExplicitFormulaDecomp`, `TailBoundPremise`) and on `VerifiedZerosTo T`; T4 is for a claim with '
         'no terminal at all.',
         '- **No row of the table above is T1**, so none is re-marked T1-open or T1-lit beyond `:187`. The T4 rows `:175`, `:177`, '
         '`:182`, `:183` have no terminal (a hypothesis field, a pinned `sorry`, a computation with no VERIFIED bank, a manuscript '
         'reduction) and stay T4.',
         '- The T0 rows `:186`, `:188`, `:189` are **T0 and not in the RH-anchor**: true facts about zeta that say nothing about the '
         'zeros` location.', '',
         '**Corrected counts over this table:** ' + ' · '.join('%s %d' % kv for kv in SURR_COUNTS.items()) + '.', '']
    w2 = append_to(SURR, NL.join(S))
    put_json('b540_law.json', dict(map=w1, surr=w2, map_counts=MAP_COUNTS, surr_counts=SURR_COUNTS, map_tiers=new, surr_tiers={str(k): v for k, v in snew.items()}))
    print('  map : %d bytes appended, prefix %s ; counts %s' % (w1['added'], w1['prefix'], MAP_COUNTS))
    print('  SURR : %d bytes appended, prefix %s ; counts %s' % (w2['added'], w2['prefix'], SURR_COUNTS))


# ------------------------------------------------------------------------------ COMPONENT 3 (f)
PAT = [('route3', r'Route 3|Routes 1, 3|riemann_hypothesis|ConservationHypothesis|Conservation route'),
       ('h2', r'\bh2\b'), ('complete proof', r'[Cc]omplete proof|RH outright|completed proof'),
       ('0/0', r'0/0|zero unproved|0 sorry, 0 axioms'), ('three compiled', r'[Tt]hree compiled routes|three independent Lean|compiled routes'),
       ('h2 by content', r'goal\s*⇐|Mellin-nonvanishing|mellin Φ \(s/2\) ≠ 0')]
E1, E3, E4, E914 = 'E-2026-09-25-1', 'E-2026-09-25-3', 'E-2026-09-25-4', 'E-2026-09-14-1'
DEP = {  # deposited sentences PATHS repeats: id -> (where, needle in the deposited text)
    'M-02': ('A_Place_to_Stand.md:123 (b532 M-02)', 'The Lean 4 kernel formalizes three independent routes to σ = 1/2'),
    'M-13': ('b532 M-13, §25.7', None), 'M-14': ('b532 M-14, §25.7', None), 'M-16': ('b532 M-16', None),
    'M-20': ('b532 M-20, §27.3', None), 'M-22': ('b532 M-22, §27.3', None), 'M-26': ('b532 M-26', None),
    'D-1788': ('A_Place_to_Stand.md:1788', 'it pinned the remaining content to a single goal state'),
    'D-1794a': ('A_Place_to_Stand.md:1794', 'and h2 — nonvanishing of the transform at the point in question'),
    'D-1794h1': ('A_Place_to_Stand.md:1794', '**h1 is complete at the witness**'),
    'D-1794h2': ('A_Place_to_Stand.md:1794', 'The obligation h2 is, in each of the classical faces, the theorem itself'),
    'D-1800': ('A_Place_to_Stand.md:1800', 'one goal state, at a cited line of a public kernel')}
OWN = 'PATHS-OWN'
SGR = [  # needle, kind, repeats, verdict, erratum, reason
    ('Three, in SIDE-kernel: structural exhaustiveness', 'REPEATS', 'M-02', 'RESTS', E1, 'Route 3 is RH restated (`ch_iff_rh`); M-02`s replacement reads "three route terminals"'),
    ('three independent Lean compilations of the same conclusion', 'REPEATS', 'M-02', 'RESTS', E1,
     'no two of the three conclude the same thing: Route 3 RH from RH restated, Route 1 a decide-count conjunct (%s), Route 2 a fact about `completedRiemannZeta₀` on the line' % E914),
    ("=The corpus's self-state (the h2 frame, aggregated)", 'OWN', '', '', '', 'a heading (exact match)'),
    ("The premise `h2`'s five doors at their exact depth", 'OWN', '', '', '', 'rectified by the appended block'),
    ('| **centre** | goal state |', 'REPEATS', 'D-1794h1', 'RESTS', E4, 'the centre`s h2 is the goal state`s `mellin Φ (s/2) ≠ 0`, false at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`); lv`s record, E-2026-09-25-3'),
    ('| **R3** | totality-through-places | h2 raw', 'OWN', '', '', '', 'R3 stated and UNDECIDED at b538; rectified by the appended block'),
    ('THE VAJRA-PLINKO PATH MAP', 'OWN', '', '', '', 'a heading'),
    ('| **3 (largest ask)** | R2 Conservation / Tate', 'REPEATS', 'M-13', 'RESTS', E1, 'discharging `ConservationHypothesis` is proving RH: it is RH restated (`ch_iff_rh`)'),
    ('**The goal state.** The programme reduces to', 'REPEATS', 'D-1788', 'RESTS', E4, 'the goal state at the fixed witness is vacuous on the strip (`mellin_Phi_eq_zero_of_re_le_one`)'),
    ('`h2` is the single open premise — and it is a statement, not a count', 'REPEATS', 'M-20', 'RESTS', E1, 'the conservation register is RH restated (`ch_iff_rh`)'),
    ("the goal state's **Mellin-nonvanishing clause**", 'REPEATS', 'D-1794a', 'RESTS', E4, 'that clause is false at every s with re s ≤ 1; its corrected form is RH on the zero configuration (`lvh2_corrected_iff`)'),
    ("These faces are `h2`'s doors", 'OWN', '', '', '', 'rectified by the appended block'),
    ('This is the **nearest-approach** door', 'OWN', '', '', '', 'rectified by the appended block'),
    ('**The fifth register (R5), the farthest door', 'OWN', '', '', '', 'R5-output TRUE-AS-STATED at b538; rectified by the appended block'),
    ('Filed first-class (OPEN_TRAILS O.18, h2-door sitting one)', 'OWN', '', '', '', 'rectified by the appended block'),
    ('| Mechanism exclusion (Routes 1, 3) |', 'REPEATS', 'M-02', 'RESTS', E1, 'Route 3: RH restated (`ch_iff_rh`); Route 1: T2 by the decide-count conjunct and the C₇ stand-in (%s)' % E914),
    ('The methods that *do* close', 'OWN', '', '', '', 'rectified by the appended block'),
    ('Routing R-curve monotonicity *from* the completed proof', 'OWN', '', '', '', 'rectified by the appended block'),
    ('The audit found **zero conditional-frame relapses**', 'OWN', '', '', '', 'an audit record'),
    ("h2 remains the bracket's outstanding obligation", 'REPEATS', 'D-1794a', 'RESTS', E4, 'the bracket`s h2 at the witness is false on the strip, not outstanding'),
    ('`h1_complete_at_Phi` discharges h1', 'REPEATS', 'D-1794h1', 'RESTS', E4, 'h2 at the witness is false on the strip, so it does not stand alone as the open proposition'),
    ('`SIDELvConservation.RegisterPentagon` at **SIDE-lv-conservation v0.7.0', 'OWN', '', '', '', 'rectified by the appended block'),
    ('h1 done, h2 the one open obligation', 'REPEATS', 'D-1794a', 'RESTS', E4, 'the obligation at the witness is false on the strip'),
    ('(v0.4 — ARM 1 census-edition pass', 'OWN', '', '', '', 'a change record of this document'),
    ('| C₅ split — input-stage', 'OWN', '', '', '', 'tiered in the appended block'),
    ('| h1 complete at the witness — the eight coupling facts', 'REPEATS', 'D-1794h1', 'RESTS', E4, 'the status cell`s "h2 outstanding" names a clause false on the strip'),
    ('| **Register pentagon — goal ⇐ h1 ∧ h2**', 'REPEATS', 'D-1788', 'RESTS', E4, '`goalState_sevenClasses_of_h2` is vacuous on the strip'),
    ('| Register pentagon — R2 (ConservationHypothesis) → RiemannHypothesis', 'REPEATS', 'M-16', 'STANDS', '', 'the row grades the terminal INTERFACES on its named premise, which is what it states'),
    ('| Register pentagon — R5 **C₅-distance', 'OWN', '', '', '', 'tiered in the appended block'),
    ('| Route 3 `riemann_hypothesis (h_cons)`', 'REPEATS', 'M-22', 'RESTS', E1, 'its antecedent is RH restated (`ch_iff_rh`), so "discharge h2" here means "prove RH"'),
    ('| T3 goal state `goalState_sevenClasses_of_h2`', 'REPEATS', 'D-1788', 'RESTS', E4, 'lv`s h2 is false on the strip; the corrected face is RH on the strip (`lvh2_corrected_iff`)'),
    ('| R-curve criterion `SIDERCurve', 'OWN', '', '', '', 'tiered in the appended block'),
    ('| GRH / Dirichlet', 'OWN', '', '', '', 'tiered in the appended block'),
    ('| Four σ=1/2 identifications', 'OWN', '', '', '', 'tiered in the appended block'),
    ('**Synthesis — the standing next mathematical target.**', 'OWN', '', '', '', 'rectified by the appended block'),
    ('The only *unconditional* A', 'REPEATS', 'M-14', 'RESTS', E1, 'Route 3`s condition is RH restated (`ch_iff_rh`) and the T3 goal state`s is false on the strip (%s)' % E4),
    ('Every conditional route turns on the one hinge', 'OWN', '', '', '', 'rectified by the appended block'),
    ('This is the sign layer beneath', 'REPEATS', 'D-1794h2', 'STANDS', '', 'the sign closure is RH in the Weil form, now compiled equivalent (`h2_sign_iff_rh`)'),
    ('**The h2 status, for the record (2026-07-26).**', 'REPEATS', 'M-26', 'STANDS', '', 'the monograph`s premise is RH-equivalent and open; nothing at b538 closes it'),
    ('Uniform transversality is the **derivative h2**', 'OWN', '', '', '', 'a separate clause, the simplicity conjecture'),
    ('| Mechanism enumeration (§22.5)', 'OWN', '', '', '', 'ANNEX D`s table'),
]


def segs(lines):
    out, cur, start = [], [], None
    for i, l in enumerate(lines, 1):
        if re.match(r'^\s*(- |```|#|>)', l) or not l.strip() or l.startswith('|'):
            if cur:
                out.append((start, ' '.join(cur)))
            cur, start = [], None
            if l.startswith('|') or re.match(r'^\s*(- |#|>)', l):
                out.append((i, l.strip()))
            continue
        if start is None:
            start = i
        cur.append(l.strip())
    if cur:
        out.append((start, ' '.join(cur)))
    return out


def sentences():
    P = rd(PATHS).split(NL)
    end = next(i for i, l in enumerate(P) if l.startswith('*Cumulative-not-replacing.'))
    rows = []
    for ln, seg in segs(P[:end]):
        parts = [seg] if seg.startswith('|') else [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z*`(\[])', ' '.join(seg.split())) if p.strip()]
        for s in parts:
            rows.append(dict(line=ln, sentence=s, hits=[n for n, p in PAT if re.search(p, s)]))
    yields = {n: sum(1 for r in rows if n in r['hits']) for n, _ in PAT}
    sel = [r for r in rows if r['hits']]
    used = set()
    dep = rd(DEPM)
    for r in sel:
        g = [x for x in SGR if (x[0][1:] == r['sentence'] if x[0].startswith('=') else x[0] in r['sentence'])]
        if len(g) != 1:
            sys.exit('### SELECTED SENTENCE WITHOUT EXACTLY ONE TYPED ROW (%d) at :%d: %s' % (len(g), r['line'], r['sentence'][:160]))
        _, kind, rep, verdict, err, reason = g[0]
        r.update(kind=kind, repeats=rep, verdict=verdict, erratum=err, reason=reason)
        if rep:
            where, needle = DEP[rep]
            r['deposited_where'] = where
            r['deposited_found'] = (needle in dep) if needle else None
        used.add(g[0][0])
    unused = [x[0] for x in SGR if x[0] not in used]
    if unused:
        sys.exit('### A TYPED ROW MEETS NO SELECTED SENTENCE: %s' % unused)
    rep = [r for r in sel if r['kind'] == 'REPEATS']
    counts = {v: sum(1 for r in rep if r['verdict'] == v) for v in ('STANDS', 'RESTS', 'EXCEEDS')}
    by_err = {}
    for r in rep:
        if r['verdict'] == 'RESTS':
            by_err[r['erratum']] = by_err.get(r['erratum'], 0) + 1
    outside = [r for r in rep if r['verdict'] == 'RESTS' and r['erratum'] not in (E1, E3, E914)]
    put_json('b540_sentences.json', dict(read=len(rows), yields=yields, selected=sel, counts=counts, rests_by_erratum=by_err,
                                          own=sum(1 for r in sel if r['kind'] == 'OWN'), outside_coverage=[(r['line'], r['sentence'][:200]) for r in outside]))
    for n, v in yields.items():
        print('  matcher %-15s yield %d' % (n, v))
    print('  sentences read %d ; selected %d ; REPEATS %d ; PATHS-OWN %d' % (len(rows), len(sel), len(rep), len(sel) - len(rep)))
    for r in sel:
        print('  :%-4d %-7s %-8s %-15s %s' % (r['line'], r['kind'], r.get('verdict') or '', r.get('erratum') or '', r['sentence'][:110]))
    print('  REPEATS : %s ; RESTS by erratum : %s' % (counts, by_err))
    print('  ### outside E-2026-09-25-1 / -3 / E-2026-09-14-1 : %d' % len(outside))
    for r in outside:
        print('      :%d  %s' % (r['line'], r['sentence'][:160]))


# ------------------------------------------------------------------------------ COMPONENT 3 (a)-(e)
NA = 'T0, not RH-anchor: '
SIII = {
    131: ('T2', 'Route 3: RH restated (ch_iff_rh); Route 1: T2 by the decide-count conjunct and the C7 stand-in'),
    132: ('T0', NA + '`spectral_cannon` states `(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0`, a fact about the line; the simplicity→RH bridge has no terminal'),
    133: ('T2', 'the model statement `1 - σ = σ → σ = 1/2`; the FE reading is a STIPULATION (Correspondence `:281`)'),
    134: ('T0', NA + '`balance_theorem` is `p^(-s) = p^(-(1-s)) ↔ s = ½` about prime powers'),
    135: ('T2', 'the model quadratic; the indicial reading is a STIPULATION (`:283`)'),
    136: ('T4', 'no terminal'),
    137: ('T2', '`monotone_unique_zero` is one direction over an abstract `V`; that `V` is the R-curve function is carried by the identifier'),
    138: ('T2', '`spinor_forces_half` concludes `w = 0`; two STIPULATIONS carry σ (`:286`)'),
    139: ('T1-lit', '**the equivalence is now compiled in the Weil form -- `h2_sign_iff_rh` (T0, the RH-anchor`s head)**; the Li form`s equivalence is **not compiled** (`R4_positivity_to_RH` INTERFACES on Li`s criterion, not in Mathlib); channel additivity `lam_add` is T2 (stream-level)'),
    140: ('T1-lit', 'the marker `certifiedInput_not_zeroRealizing` INTERFACES on `NontrivialZeroExistsInStrip`, a literature theorem not compiled; the input `C5_input_at_Phi` alone is T0, not RH-anchor'),
    141: ('T2', 'the countermodel and the shared-witness bridge are logic over abstract couplings'),
    142: ('T0', NA + '`C7_finite_type_false`, the growth of `completedRiemannZeta₀`')}
ANNEXA = {
    320: ('T2', 'the decide-count catalogue conjunct and the disclosed C₇ stand-in (%s)' % E914),
    321: ('T0', NA + 'a fact about `completedRiemannZeta₀``s derivative on the line'),
    322: ('T2', 'its antecedent `ConservationHypothesis` is RH restated (`ch_iff_rh`), so "discharge h2" here means "prove RH"'),
    323: ('T2', 'b538: lv`s h2 is false at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`), so the goal state is vacuous on the strip; the corrected face is RH on the strip (`lvh2_corrected_iff`)'),
    324: ('T0', NA + '`h1_complete_at_Phi` certifies the eight coupling facts of `Phi`; nothing about where the zeros are'),
    325: ('T1-lit', '`TailBoundPremise` (Voros) and `ExplicitFormulaDecomp` (Bombieri–Lagarias) are **T1-lit**: literature theorems not yet compiled'),
    326: ('T2', 'one direction over an abstract `V`'),
    327: ('T4', 'no covering terminal; the antecedent is shape C'),
    328: ('T2', 'the χ-family catalogue, χ typed but unused -- Route 1`s shape'),
    329: ('T2', 'model statements with STIPULATIONS; the Sieve has no terminal'),
    330: ('T4', 'per-instance computation with no VERIFIED bank; no covering terminal')}
ANNEXB = {
    378: ('A6', 'T0', NA + '`blTerm_nonneg_of_onLine`, the Li terms of zeros already on the line'),
    379: ('A7', 'T1-lit', '`partialPositivity_finiteRange` INTERFACES on `ExplicitFormulaDecomp`, `TailBoundPremise` (literature, not compiled) and `VerifiedZerosTo T`'),
    381: ('A9', 'T0', NA + 'Mathlib`s `ArithmeticFunction.vonMangoldt_nonneg`; the zero-free-region consequence is classical and not compiled')}
CORR = {
    281: ('T2', 'model statement; STIPULATION'), 282: ('T0', NA + 'prime powers'), 283: ('T2', 'model statement; STIPULATION'),
    284: ('T2', 'one direction over an abstract `V`'), 285: ('T0', NA + 'growth of `completedRiemannZeta₀`'), 286: ('T2', 'two STIPULATIONS'),
    287: ('T0', NA + '`C5_input_at_Phi`; the marker`s row is `:302`'), 288: ('T2', 'stream-level additivity; the η↔Taylor identification is not compiled'),
    289: ('T2', 'logic over a closed system'), 290: ('T2', 'the decide-count conjunct and the C₇ stand-in (%s)' % E914),
    291: ('T2', '`(1 : ℚ) ^ s = 1`, a STIPULATION'), 292: ('T2', '`T2b_mellin_exhaustion` is DEFINITIONAL (`rfl`); the T1 factorization alone is T0'),
    293: ('T2', 'logic over abstract couplings; the pin carries `sorry`'),
    294: ('T0', NA + 'the coupling facts of `Phi`; the status cell`s "h2 outstanding" rests on %s' % E4),
    295: ('T2', '`goalState_sevenClasses_of_h2` is vacuous on the strip (%s)' % E4), 296: ('T0', NA + '`C5_input_at_Phi`'),
    297: ('T2', 'ENCODES-CONCLUSION: its premise is RH restated (`ch_iff_rh`)'),
    298: ('T2', 'the additivity is carried as a premise, stream-level'),
    299: ('T1-lit', 'INTERFACES on Li`s criterion (Bombieri–Lagarias), not in Mathlib'),
    300: ('T2', 'vacuous: its hypothesis `Register1_universalityHypothesis` is false (`not_register1`)'),
    301: ('T2', 'ENCODES-CONCLUSION: `Register5_output_HilbertPolya` holds (`register5_output_holds`), so its bridge premise `Register5_output_HilbertPolya → RiemannHypothesis` is RH itself -- the "disclaimed" face is a theorem (flagged)'),
    302: ('T1-lit', 'INTERFACES on `NontrivialZeroExistsInStrip` (Hardy), not compiled'),
    303: ('T4', 'R3 stated and UNDECIDED at b538; no deciding terminal'), 304: ('T1-lit', 'INTERFACES on literature premises not compiled'),
    305: ('T2', 'arithmetic alone'), 306: ('T2', 'a count of a kernel-defined type'), 307: ('T4', 'no terminal'), 308: ('T4', 'no terminal')}
TIERS = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
SI_READING = ('**§I`s "three compiled routes", read after b531 and b538:** two compiled route terminals, **neither a route to σ = 1/2** -- '
              'Route 1 (`structural_exhaustiveness_proved`, T2: the decide-count conjunct and the C₇ stand-in) and Route 2 '
              '(`spectral_cannon`, T0 and not in the RH-anchor: a fact about `completedRiemannZeta₀` on the line) -- **with Route 3 struck '
              'from the count**: `ConservationBridge.riemann_hypothesis` is the compiled implication from `ConservationHypothesis`, which '
              'is RH restated (`ch_iff_rh`), so it formalizes RH ⇒ RH. **Zero compiled routes to σ = 1/2.** The RH-anchor`s '
              '`h2_sign_iff_rh` is not a route either: it is an equivalence between two open statements.')


def table(src, spec, cols):
    rows = []
    for ln in sorted(spec):
        l = src[ln - 1]
        if not l.startswith('|'):
            sys.exit('### LINE :%d IS NOT A TABLE ROW: %s' % (ln, l[:80]))
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        rows.append(dict(line=ln, cells=c[:cols], tier=spec[ln][-2], reason=spec[ln][-1]))
    return rows


def counts(rows):
    return {t: sum(1 for r in rows if r['tier'] == t) for t in TIERS}


def paths():
    P = rd(PATHS).split(NL)
    siii = table(P, SIII, 1)
    anna = table(P, ANNEXA, 1)
    annb = [dict(line=ln, row=v[0], tier=v[1], reason=v[2]) for ln, v in sorted(ANNEXB.items())]
    for r in annb:
        assert P[r['line'] - 1].startswith('| %s |' % r['row']), P[r['line'] - 1][:30]
    corr = table(P, CORR, 1)
    extrema = sum(len(re.findall(r'4\.062|5\.196|13\.153', l)) for l in P)
    sj = jl('b540_sentences.json')
    L = ['', '<!-- b540 (R150) TIER BLOCK, 2026-09-25 -->', '', PATHSH, '',
         '*Appended by b540 under the author`s ruling `(R150)`, the cascade`s second act. **No line above this block changes.** Each row '
         'that names a terminal is tiered by `(R149)`(2) as `(R150)`(2)-(3) correct it, from the terminal`s statement at its pin: T0 '
         '(stated against Mathlib`s own objects, standard three, no premise; the **RH-anchor** its subset bearing on where zeta`s zeros '
         'are), T1-open, T1-lit, T2 (ENCODES-CONCLUSION, SHELL, FALSE-AS-STATED, vacuous), T3, T4. A premise that is RH restated by a '
         'rewording lemma makes its terminal ENCODES-CONCLUSION, T2 (a reading flagged for the author). Sources: relay '
         '`data/b540_tiers.json`, `data/b540_sentences.json`.*', '',
         '### (a) §I -- the enumerations', '', SI_READING, '',
         '### (b) §III -- the completion-state table, tiered row for row', '', '| line | path | tier | reason |', '|:--|:--|:--|:--|']
    L += ['| :%d | %s | **%s** | %s |' % (r['line'], r['cells'][0], r['tier'], r['reason']) for r in siii]
    L += ['', 'Counts: ' + ' · '.join('%s %d' % kv for kv in counts(siii).items()) + '.', '',
          '### (c) ANNEX A -- the shape-sort, tiered', '', '| line | candidate | tier | reason |', '|:--|:--|:--|:--|']
    L += ['| :%d | %s | **%s** | %s |' % (r['line'], r['cells'][0][:120], r['tier'], r['reason']) for r in anna]
    L += ['', 'Counts: ' + ' · '.join('%s %d' % kv for kv in counts(anna).items()) + '.', '',
          '### (d) ANNEX B -- the rows that name a terminal', '', '| line | row | tier | reason |', '|:--|:--|:--|:--|']
    L += ['| :%d | %s | **%s** | %s |' % (r['line'], r['row'], r['tier'], r['reason']) for r in annb]
    L += ['', 'A1–A5, A8, A10 and B1–B5 name no terminal. Counts: ' + ' · '.join('%s %d' % kv for kv in counts(annb).items()) + '. '
          '**The `(R121)` check:** the withdrawn extrema of the piecewise-linear window family (4.062, 5.196, 13.153; `OPEN_TRAILS.md:10030-10032`) '
          'occur %d times in this document, so no ANNEX B row takes the withdrawal reference; ANNEX B`s "ladder" is the R4 positivity '
          'ladder, a different object.' % extrema, '',
          '### (e) The Correspondence table, tiered row for row', '', '| line | claim | tier | reason |', '|:--|:--|:--|:--|']
    L += ['| :%d | %s | **%s** | %s |' % (r['line'], r['cells'][0][:120].replace('|', '∣'), r['tier'], r['reason']) for r in corr]
    L += ['', 'Counts: ' + ' · '.join('%s %d' % kv for kv in counts(corr).items()) + '.', '',
          '### (f) The sentences that repeat a deposited sentence', '',
          '%d sentences selected by six matchers (Route 3; h2; complete proof; 0/0; three compiled routes; h2 by content); **%d REPEAT a '
          'deposited sentence** -- STANDS %d · RESTS %d · EXCEEDS %d; RESTS by erratum %s -- and %d are PATHS`s own, rectified by this '
          'block. The RESTS rows outside E-2026-09-25-1`s and -3`s coverage repeat the deposited monograph`s §27.3 (`A_Place_to_Stand.md` '
          ':1788, :1794 at v1.1.2), which pins the ledger`s h2 as the Mellin nonvanishing at the witness: **E-2026-09-25-4 is DRAFTED, NOT '
          'FILED** (relay `data/b540_erratum_draft.md`).' % (len(sj['selected']), sum(sj['counts'].values()), sj['counts']['STANDS'],
                                                             sj['counts']['RESTS'], sj['counts']['EXCEEDS'], sj['rests_by_erratum'], sj['own']), '']
    w = append_to(PATHS, NL.join(L))
    w['heading_line'] = rd(PATHS).split(NL).index(PATHSH) + 1
    put_json('b540_tiers.json', dict(siii=siii, annex_a=anna, annex_b=annb, corr=corr, extrema=extrema, si_reading=SI_READING,
                                      counts=dict(siii=counts(siii), annex_a=counts(anna), annex_b=counts(annb), corr=counts(corr))))
    put_json('b540_paths.json', w)
    print('  PATHS : %d bytes appended, prefix %s ; block at line %d' % (w['added'], w['prefix'], w['heading_line']))
    for k, v in (('§III', siii), ('ANNEX A', anna), ('ANNEX B', annb), ('Correspondence', corr)):
        print('  %-15s %s' % (k, counts(v)))
    print('  withdrawn extrema in PATHS : %d' % extrema)


# ------------------------------------------------------------------------------ E-2026-09-25-4
E4ROWS = [  # (id, start needle, end needle (inclusive), replacement)
    ('D-1788', 'The formalization then did what formalization is for', 'to a single goal state.',
     "The formalization then did what formalization is for: it stated the remaining content as a goal state at the fixed witness Φ; "
     "at that witness the goal state's nonvanishing clause mellin Φ (s/2) ≠ 0 is false at every s with re s ≤ 1 "
     "(mellin_Phi_eq_zero_of_re_le_one, SIDE-explicit-formula RegisterDepth.lean at 81ae175), so on the critical strip the remaining "
     "content is carried by the clause's completedRiemannZeta form, which is RH on the zero configuration (lvh2_corrected_iff)."),
    ('D-1794a', '**What remains, exactly.** The bracket', 'nonvanishing of the transform at the point in question.',
     "What remains, exactly. The bracket's two obligations are h1 — the per-class constraints of Chapter 15, instantiated at the fixed "
     "witness — and h2 — nonvanishing of the transform at the point in question; at the fixed witness that nonvanishing is false at "
     "every point with re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one), so on the critical strip the obligation is its completedRiemannZeta "
     "form, RH on the zero configuration (lvh2_corrected_iff)."),
    ('D-1794c', 'The premise is RH-equivalent, and this monograph does not obscure that', 'with the certifiable surround discharged and counted.',
     "The premise is RH-equivalent, and this monograph does not obscure that; what the architecture has achieved is its localization — "
     "to one named proposition, compiled in the Weil form as h2_sign ↔ RiemannHypothesis (h2_sign_iff_rh, SIDE-explicit-formula v0.2) — "
     "while the goal state at the fixed witness, whose nonvanishing clause is false on the strip (mellin_Phi_eq_zero_of_re_le_one), does "
     "not carry it there."),
    ('D-1800', '**The count.** One premise', 'with their ancestry cited.',
     "The count. One premise; five registers; one goal state, at a cited line of a public kernel, whose nonvanishing clause at the fixed "
     "witness is false on the critical strip (mellin_Phi_eq_zero_of_re_le_one) and whose corrected form is RH on the zero configuration "
     "(lvh2_corrected_iff); two theorems bracketing it; a discharge path within the programme — the per-class constraints instantiated "
     "at the fixed witness, with h1 now complete at that witness (all eight discharged) — and its classical faces outside it, with "
     "their ancestry cited.")]


def erratum4():
    dep = rd(DEPM)
    dl = dep.split(NL)
    sj = jl('b540_sentences.json')
    out = [r for r in sj['selected'] if r['kind'] == 'REPEATS' and r['erratum'] == E4]
    rows = []
    for rid, a, b, rep in E4ROWS:
        i = dep.index(a)
        j = dep.index(b, i) + len(b)
        line = dep[:i].count(NL) + 1
        rows.append(dict(id=rid, line=line, text=dep[i:j].replace('**', ''), replacement=rep,
                         repeated_by=[r['line'] for r in out if r['repeats'] == rid or (rid == 'D-1794a' and r['repeats'] in ('D-1794a', 'D-1794h1'))]))
    L = ['## E-2026-09-25-4 — The deposited monograph pins the ledger\'s h2 as the Mellin nonvanishing at the witness and the goal state as '
         'the one remaining content; that clause is false on the critical strip (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2) — DRAFT, NOT FILED', '',
         '**Drafted 2026-09-25 (b540), on the author\'s ruling (R150)(4), from the reading banked at b540 (relay data/b540_sentences.json): '
         'PATHS_TO_THE_CRITICAL_LINE repeats these deposited sentences, and E-2026-09-25-1 (Route 3) and E-2026-09-25-3 (lv-conservation\'s '
         'record and THE UNCONDITIONAL SURROUND) do not cover them. TO BE FILED only on the author\'s word.',
         '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
         '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**', '',
         '**Affected.** *A Place to Stand*, Zenodo version v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — '
         'the monograph, §27.3, as deposited (PLACE-papers outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md).', '',
         '**What the kernel says, in its own words.** SIDE-explicit-formula RegisterDepth.lean at 81ae175, read fresh at b539 and b540: '
         'mellin_Phi_eq_zero_of_re_le_one : ∀ (s : ℂ), s.re ≤ 1 → mellin Phi (s / 2) = 0, with Phi the witness of the deposited §27.3 '
         '(Φ(t) = ((evenKernel 0 t) − 1)/2); lvh2_corrected_iff : (∀ (s : ℂ), 0 < s.re → s.re < 1 → s.re ≠ 1 / 2 → completedRiemannZeta s ≠ 0) '
         '↔ rh_strip; and h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis (v0.2).', '',
         '**The deposited sentences, each with its replacement drafted from those statements:**', '']
    for r in rows:
        L += ['- **%s** (A_Place_to_Stand.md:%d at v1.1.2; repeated by PATHS at %s): *"%s"*' % (r['id'], r['line'],
                                                                                              ', '.join(':%d' % x for x in r['repeated_by']) or 'none of the RESTS rows directly', r['text']),
              '  - reads **RESTS** — the goal state\'s nonvanishing clause at the fixed witness is false at every s with re s ≤ 1.',
              '  - replacement: *"%s"*' % r['replacement']]
    L += ['', '**What is not corrected.** That h1_complete_at_Phi is compiled; the bracket pair; the sentence that the obligation h2 is, in '
              'each of the classical faces, the theorem itself (it STANDS, and in the Weil face it is now compiled equivalent: h2_sign_iff_rh). '
              'This entry is scoped to the deposited sentences PATHS repeats; a whole read of the deposited monograph against the register '
              'census of b538 is the author\'s to order.', '',
          '**Status.** DRAFT. Not filed. Retained at monograph v1.1.2. Whether any Zenodo description is edited under (R110) is the '
          'author\'s ruling; the filing is the author\'s word.', '']
    txt = NL.join(L)
    io.open(os.path.join(D, 'b540_erratum_draft.md'), 'w', encoding='utf-8', newline=NL).write(txt)
    put_json('b540_erratum4.json', dict(rows=rows, backticks_outside_code=outside_code_backticks(txt), backticks=txt.count('`')))
    print('  E-2026-09-25-4 draft : %d rows ; deposited lines %s ; backticks %d' % (len(rows), [r['line'] for r in rows], txt.count('`')))


# ------------------------------------------------------------------------------ COMPONENT 4
def findings():
    tj, sj = jl('b540_tiers.json'), jl('b540_sentences.json')
    c = tj['counts']
    L = ['', FTITLE, '',
         '*Filed at b540 on the author`s ruling `(R150)`. Sources: relay `data/b540_tiers.json`, `data/b540_sentences.json`, '
         '`data/b540_file.json`, `data/b540_erratum_draft.md`.*', '',
         '**E-2026-09-25-3 is FILED** (ERRATA.md:%s-%s, in the DEPOSIT-FACING list at :%s). **The tier and the RH-anchor are two things**: '
         'T0 is a tier, the RH-anchor its subset bearing on where zeta`s zeros are, `h2_sign_iff_rh` at its head; the map`s five T0 '
         'terminals outside it each carry the sentence that they say nothing about the zeros` location. **T1 splits** into T1-open and '
         'T1-lit; `partialPositivity_finiteRange` is T1-lit. Corrected counts: the map`s twelve %s; SURR`s table %s.'
         % (tuple(jl('b540_file.json')['entry_lines']) + (jl('b540_file.json')['bullet_line'], jl('b540_law.json')['map_counts'],
                                                           jl('b540_law.json')['surr_counts'])), '',
         '**PATHS tiered** (its appended block at line %s): §III %s; ANNEX A %s; ANNEX B %s; the Correspondence table %s. §I`s "three '
         'compiled routes" reads: two compiled route terminals, neither a route to σ = 1/2, Route 3 struck (its premise RH restated). '
         'II.7`s equivalence is now compiled in the Weil form (`h2_sign_iff_rh`), the Li form not. The Hilbert–Pólya edge '
         '`R5_output_HilbertPolya_to_RH` is ENCODES-CONCLUSION: its "disclaimed" face `Register5_output_HilbertPolya` is a theorem '
         '(`register5_output_holds`), so the bridge premise is RH itself.'
         % (jl('b540_paths.json').get('heading_line'), c['siii'], c['annex_a'], c['annex_b'], c['corr']), '',
         '**The sentences of PATHS that repeat a deposited sentence:** STANDS %d · RESTS %d · EXCEEDS %d, RESTS by erratum %s; %d further '
         'sentences are PATHS`s own. Those outside E-2026-09-25-1`s and -3`s coverage repeat the deposited monograph`s §27.3; '
         '**E-2026-09-25-4 is DRAFTED, NOT FILED** (relay `data/b540_erratum_draft.md`).'
         % (sj['counts']['STANDS'], sj['counts']['RESTS'], sj['counts']['EXCEEDS'], sj['rests_by_erratum'], sj['own']), '',
         '**Next:** the filing of E-2026-09-25-4 on the author`s word; the next keystone of the cascade is BALANCE_AND_POSITIVITY.', '']
    w = append_to(FIND, NL.join(L))
    w['heading_line'] = rd(FIND).split(NL).index(FTITLE) + 1
    put_json('b540_findings.json', w)
    print('  FINDINGS : %(added)d bytes added, prefix %(prefix)s ; entry at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ desk
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


PRIOR_PP = '2293ca2'
FILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
         'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md']


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    return sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b540_'))


def scores():
    tj, sj, fj = jl('b540_tiers.json'), jl('b540_sentences.json'), jl('b540_file.json')
    head = next((r for r in tj.get('siii', []) if r['line'] == 131), {})
    cite = [r['line'] for r in tj.get('siii', []) if 'h2_sign_iff_rh' in r['reason']]
    ii7 = next((r for r in tj.get('siii', []) if r['line'] == 139), {})
    a325 = next((r for r in tj.get('annex_a', []) if r['line'] == 325), {})
    rep = [r for r in sj.get('selected', []) if r['kind'] == 'REPEATS']
    outside = sj.get('outside_coverage', [])
    kept = {}
    for f in FILES:
        old = blob(PP, '%s:%s' % (PRIOR_PP, f)).decode('utf-8-sig')   # ### both sides BOM-stripped (defect (c))
        new = rd(os.path.join(PP, f))
        kept[f] = subseq(old.replace(chr(13), ''), new) and (f == 'ERRATA.md' or open(os.path.join(PP, f), 'rb').read().startswith(blob(PP, '%s:%s' % (PRIOR_PP, f))))
    same = {f: blob(PP, '%s:%s' % (PRIOR_PP, f)) == open(os.path.join(PP, f), 'rb').read() for f in ('README.md', 'REGISTRY.md')}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b540_') and needle in rd(os.path.join(T, x))]
    ker = {n: git(p, 'status', '--porcelain', '--untracked-files=no') == '' for n, p in
           (('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel'), ('SIDE-lv-conservation', 'D:/SIDE-lv-conservation'))}
    tok = token_count()
    dep = git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''
    return dict(
        n1=head.get('tier') == 'T2' and head.get('reason') == 'Route 3: RH restated (ch_iff_rh); Route 1: T2 by the decide-count conjunct and the C7 stand-in',
        n2=cite == [139] and 'not compiled' in ii7.get('reason', ''),
        n3='`TailBoundPremise` (Voros) and `ExplicitFormulaDecomp` (Bombieri–Lagarias) are **T1-lit**' in a325.get('reason', ''),
        n4=any(r['verdict'] == 'RESTS' and r['erratum'] == E1 for r in rep) and (bool(outside) == os.path.exists(os.path.join(D, 'b540_erratum_draft.md'))),
        outside=outside,
        n5=all(kept.values()), kept=kept,
        n6=all(same.values()) and not zen and all(ker.values()) and tok == 0 and dep, same=same, zenodo_tools=zen, kernels=ker, token=tok, deposit_clean=dep,
        s1=fj.get('backticks_outside_code', 1) == 0, s2=tj.get('extrema', 1) == 0,
        s3=jl('b540_law.json').get('map_counts', {}).get('T4', 1) == 0)


def w(v):
    return 'HELD' if v else 'REFUTED'


def components():
    L = ['=' * 132, 'b540 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### READING (1) -- THE PURPOSE STATEMENTS:']
    L += ['  ' + l for l in rd(os.path.join(D, 'b540_purpose.txt')).rstrip(NL).split(NL)[2:]]
    L += ['', '### THE RH-ANCHOR`S STATEMENTS, FRESH (pre-seal read):'] + ['  ' + l for l in rd(os.path.join(D, 'b540_anchor_statements.txt')).split(NL)
                                                                         if l.startswith('@SIDE') or l.startswith('SIDE')]
    L += ['', '### COMPONENT 1 -- THE FILING : ' + json.dumps(jl('b540_file.json'), ensure_ascii=False)]
    L += ['', '### COMPONENT 2 -- THE TIER LAW : map %s ; SURR %s' % (jl('b540_law.json').get('map_counts'), jl('b540_law.json').get('surr_counts'))]
    tj = jl('b540_tiers.json')
    L += ['', '### COMPONENT 3 -- PATHS (block at line %s) :' % jl('b540_paths.json').get('heading_line'), '  ' + tj.get('si_reading', '')]
    for k in ('siii', 'annex_a', 'annex_b', 'corr'):
        L += ['  %s %s' % (k, tj['counts'][k])] + ['    :%-4d %-7s %s' % (r['line'], r['tier'], r['reason'][:150]) for r in tj[k]]
    sj = jl('b540_sentences.json')
    L += ['', '### (f) THE SENTENCES : read %s ; yields %s ; counts %s ; RESTS by erratum %s ; PATHS-own %s'
          % (sj.get('read'), sj.get('yields'), sj.get('counts'), sj.get('rests_by_erratum'), sj.get('own'))]
    L += ['  :%-4d %-7s %-7s %-15s %s' % (r['line'], r['kind'], r.get('verdict') or '', r.get('erratum') or '', r['sentence'][:150]) for r in sj.get('selected', [])]
    L += ['  outside E-1 / E-3 coverage : %s' % sj.get('outside_coverage')]
    L += ['', '### E-2026-09-25-4 : ' + json.dumps({k: v for k, v in jl('b540_erratum4.json').items() if k != 'rows'}),
          '  rows : %s' % [(r['id'], r['line'], r['repeated_by']) for r in jl('b540_erratum4.json').get('rows', [])]]
    L += ['', '### COMPONENT 4 -- FINDINGS : ' + json.dumps(jl('b540_findings.json'), ensure_ascii=False), '=' * 132]
    io.open(os.path.join(D, 'b540_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    N = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')
    S = ('s1', 's2', 's3')
    tj = jl('b540_tiers.json')
    L = ['=' * 104, 'b540 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- §III :131 T2 : "%s".' % (w(sc['n1']), next((r['reason'] for r in tj.get('siii', []) if r['line'] == 131), '')),
         '  **(N2)** ### **%s.** -- the §III rows citing h2_sign_iff_rh : [139] ; II.7 marks the Li form not compiled. Rows :132, :134, :142 are T0 '
         'by their own terminals, none in the RH-anchor.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- ANNEX A :325 reads TailBoundPremise and ExplicitFormulaDecomp T1-lit.' % w(sc['n3']),
         '  **(N4)** ### **%s.** -- REPEATS rows resting on E-2026-09-25-1 : %d ; outside -1 / -3 coverage : %d, printed, E-2026-09-25-4 drafted.'
         % (w(sc['n4']), sum(1 for r in jl('b540_sentences.json').get('selected', []) if r.get('erratum') == E1), len(sc['outside'])),
         '  **(N5)** ### **%s.** -- prior lines kept, appended blocks after the last prior byte (ERRATA`s bullet the one insert) : %s.' % (w(sc['n5']), sc['kept']),
         '  **(N6)** ### **%s.** -- README, REGISTRY byte-identical %s ; kernels clean %s ; tools naming the platform`s address %s ; token hits %s ; '
         'deposit tree clean %s.' % (w(sc['n6']), sc['same'], sc['kernels'], sc['zenodo_tools'] or 'NONE', sc['token'], sc['deposit_clean']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- backticks outside code spans in the filed entry : %s.' % (w(sc['s1']), jl('b540_file.json').get('backticks_outside_code')),
         '  **(S2)** ### **%s.** -- withdrawn extrema in PATHS : %s.' % (w(sc['s2']), tj.get('extrema')),
         '  **(S3)** ### **%s.** -- the map`s corrected T4 : %s.' % (w(sc['s3']), jl('b540_law.json').get('map_counts', {}).get('T4')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in S].count(True), [sc[k] for k in S].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b540_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b540_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b540_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b540_scores.json', sc)
    print(NL.join(L))


def trail():
    sc, tj, sj = scores(), jl('b540_tiers.json'), jl('b540_sentences.json')
    body = ['', HEADING, '',
            '**(R150) ratified.** (1) E-2026-09-25-3 filed as drafted, its (R110) question left to a separate ruling. (2) T0 is a tier and '
            'the RH-anchor its subset bearing on where zeta`s zeros are; `h2_sign_iff_rh` heads the map. (3) T1 splits into T1-open and '
            'T1-lit. (4) The cascade`s second act is PATHS.', '',
            '**Filed:** E-2026-09-25-3 at `ERRATA.md`:%s-%s, its bullet at :%s. **Corrected by appended lines:** the map (%s) and SURR (%s).'
            % (tuple(jl('b540_file.json')['entry_lines']) + (jl('b540_file.json')['bullet_line'], jl('b540_law.json')['map_counts'], jl('b540_law.json')['surr_counts'])), '',
            '**PATHS tiered** (block at line %s): §III %s; ANNEX A %s; ANNEX B %s; Correspondence %s. §I`s three compiled routes read as two '
            'compiled route terminals, neither a route to σ = 1/2, Route 3 struck. The Hilbert–Pólya edge is ENCODES-CONCLUSION: its '
            '"disclaimed" face is a theorem (`register5_output_holds`).'
            % (jl('b540_paths.json').get('heading_line'), tj['counts']['siii'], tj['counts']['annex_a'], tj['counts']['annex_b'], tj['counts']['corr']), '',
            '**The sentences:** REPEATS STANDS %d · RESTS %d · EXCEEDS %d (RESTS by erratum %s); PATHS-own %d. **E-2026-09-25-4 DRAFTED, NOT '
            'FILED** (relay `data/b540_erratum_draft.md`): the deposited monograph`s §27.3 pins the ledger`s h2 as the Mellin nonvanishing at '
            'the witness.' % (sj['counts']['STANDS'], sj['counts']['RESTS'], sj['counts']['EXCEEDS'], sj['rests_by_erratum'], sj['own']), '',
            '**Next:** the filing of E-2026-09-25-4 on the author`s word; the next keystone, BALANCE_AND_POSITIVITY.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; the ceiling unchanged; '
            'no grade moved on any row; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a '
            'statement about RH.', '']
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b540_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'purpose': purpose, 'file': file, 'law': law, 'sentences': sentences, 'paths': paths, 'erratum4': erratum4,
              'findings': findings, 'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
