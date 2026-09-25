# -*- coding: utf-8 -*-
"""b539_record.py -- THE CASCADE, ACT ONE: THE RECORD, UNDER (R149).
### `python tools/b539_record.py purpose | sentences | tiers | appendix | erratum | surr | findings | components | desk | trail`

### Every keystone write is ONE append after the file's last byte; no earlier byte changes. The grades of the selected
### sentences and the tiers of the ranked terminals are the seat's statement-reads, typed here beside their reasons, and each
### typed grade must meet exactly one selected sentence (the tool refuses otherwise). This file deletes nothing.
"""
import hashlib, html, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SURR = os.path.join(PP, 'phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md')
FIND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
ATITLE = '## The hub terminals tiered against the anchor tier of (R149), 2026-09-25'
FTITLE = ("## The cascade, act one: the anchor tier, the hub terminals tiered, THE_UNCONDITIONAL_SURROUND §6 and lv-conservation's "
          "description read against the register census")
STITLE = '### Correspondence, tiered under (R149) -- 2026-09-25, b539 (a new table beneath the old, row for row; the table above is unedited)'
HEADING = ('### b539 — the cascade opens under (R149): the anchor tier printed fresh, the hub terminals tiered, SURR §6 and '
           'lv-conservation`s description read against the register census, E-2026-09-25-3 drafted')
E3 = 'E-2026-09-25-3'
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


# ------------------------------------------------------------------------------ READING (1)
def purpose():
    m = rd(MAP).split(NL)
    s = rd(SURR).split(NL)
    L = ['b539 -- THE PURPOSE STATEMENTS OF THE KEYSTONES THIS ACT TOUCHES, PRINTED BEFORE ANY WRITE', '',
         'phase1.5/method/THE_LOAD_BEARING_MAP.md:8', '  ' + m[7], '',
         'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md:23', '  ' + s[22], '',
         'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md:25', '  ' + s[24]]
    assert m[7].startswith('**PURPOSE:**') and s[22].startswith('**Role.**')
    io.open(os.path.join(D, 'b539_purpose.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 3
PAT = [('h2', r'\bh2\b'), ('covers_all', r'covers_all'), ('mellin Phi', r'mellin\s*(Phi|Φ)|Mellin witness Phi|Mellin-nonvanishing'),
       ('goal', r'goal\s*⇐|goal state|goal-state'), ('h1 complete / open', r'\bh1\b|h1-complete|h1_complete|open obligation|complete at the witness')]


def segments(text):
    """### bullets, code fences and headings break sentences (READING (6))."""
    out, cur = [], []
    for l in text.split(NL):
        if re.match(r'^\s*(- |```|#)', l) or not l.strip():
            if cur:
                out.append(' '.join(cur))
            cur = []
            if l.strip() and not l.strip().startswith('```'):
                cur = [l.strip()]
            continue
        cur.append(l.strip())
    if cur:
        out.append(' '.join(cur))
    return out


def sents(text):
    res = []
    for seg in segments(text):
        t = ' '.join(seg.split())
        res += [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z*`(\[])', t) if p.strip()]
    return res


def blocks():
    S = rd(SURR).split(NL)
    d = json.loads(rd(os.path.join(D, 'b499_fetchback_21539068.json')))
    lv = html.unescape(re.sub(r'<[^>]+>', NL, d['metadata']['description']))
    return [('SURR §5', 'ordered', 'THE_UNCONDITIONAL_SURROUND.md:112-118', NL.join(S[111:118])),
            ('SURR §6', 'ordered', 'THE_UNCONDITIONAL_SURROUND.md:122-141', NL.join(S[121:141])),
            ('lv 21539068 title', 'ordered', 'relay data/b499_fetchback_21539068.json metadata.title', d['metadata']['title']),
            ('lv 21539068 description', 'ordered', 'relay data/b499_fetchback_21539068.json metadata.description', lv),
            ('SURR §0', 'outside', 'THE_UNCONDITIONAL_SURROUND.md:37', S[36]),
            ('SURR Correspondence', 'outside', 'THE_UNCONDITIONAL_SURROUND.md:184', S[183])]


R_H2 = ('lv`s h2 is `mellin Phi (s / 2) ≠ 0` at the fixed witness Phi, and `mellin_Phi_eq_zero_of_re_le_one` '
        '(SIDE-explicit-formula RegisterDepth.lean at 81ae175) proves it FALSE at every s with re s ≤ 1')
GRADES = [  # (needle, grade, reason, replacement drafted for E-2026-09-25-3 or '')
    ('The node: `covers_all` (the one open premise)', 'STANDS', 'the heading names the kernel`s open field; no T0 result touches it', ''),
    ('covers_all : ∀ x, P x → ∃ C ∈ classes, C.produces x', 'STANDS',
     'the field as stated at SIDE-kernel v1.2 `Kernel/Layer1.lean`; b538 does not touch it', ''),
    ('In the SIDE-lv-conservation coupling ledger it is exactly the open premise `h2`', 'RESTS',
     R_H2 + '; `covers_all` is a hypothesis field over the kernel`s catalogue, a different Prop; with h2 false on the strip, '
     'goal ⇐ h1 ∧ h2 is vacuous there, so the node is not lv`s h2',
     "In the SIDE-lv-conservation coupling ledger the premise written h2 is mellin Phi (s / 2) ≠ 0 at the fixed witness Phi, and "
     "that clause is false at every s with re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one, SIDE-explicit-formula RegisterDepth.lean at "
     "81ae175): the ledger's goal ⇐ h1 ∧ h2 is vacuous on the critical strip, and its h2 is not this node. The strip clause with "
     "completedRiemannZeta in its place is RH on the kernel's zero configuration (lvh2_corrected_iff)."),
    ('The monograph\'s assembly step (9)', 'STANDS', 'a reading of the manuscript`s step (9); no T0 result touches it', ''),
    ('Its equivalent formulations are the register faces', 'RESTS',
     'as compiled, R1 is FALSE-AS-STATED (`not_register1`) and R5-output TRUE-AS-STATED (`register5_output_holds`), so the Lean '
     'faces are not equivalent formulations of one open premise; the equivalence is the monograph`s registers`, not these sentences`',
     "Its equivalent formulations are the register faces the monograph collects in §27.3 as \"one premise in five registers\". Their "
     "Lean faces in SIDELvConservation.RegisterPentagon are not equivalent formulations as stated: R1 is false (not_register1), "
     "R5-output holds unconditionally (register5_output_holds), R3 is undecided, and the goal-state's nonvanishing clause at the "
     "witness is false on the strip (SIDE-explicit-formula RegisterDepth.lean at 81ae175)."),
    ('It does **not** land the cross-register *equivalences*', 'STANDS',
     'R3 is still the open edge: stated at b538 and UNDECIDED, not decided either way', ''),
    ('`covers_all` is the statement that it reaches the region with them', 'STANDS', 'a reading; no T0 result touches it', ''),
    ('the Euler product\'s reach into the strip is precisely `covers_all`', 'STANDS', 'a reading; no T0 result touches it', ''),
    ('SIDE-lv-conservation: the Conservation-route growth interface and the h1-complete coupling ledger', 'STANDS',
     '`h1_complete_at_Phi` is compiled; the title claims no more', ''),
    ('this kernel fixes it as one compiled goal state', 'RESTS',
     'the goal state at the kernel`s witness needs `mellin Phi (s / 2) ≠ 0`, which is false at every s with re s ≤ 1 '
     '(`mellin_Phi_eq_zero_of_re_le_one`), so the compiled goal state cannot carry the clause on the strip',
     "Rather than leaving that clause as prose, this kernel states a goal state around it and machine-checks everything provable "
     "around it; at the kernel's fixed witness Phi the goal state's nonvanishing clause mellin Phi (s/2) ≠ 0 is false at every s with "
     "re s ≤ 1, so on the critical strip the clause is carried by its completedRiemannZeta form, which is RH on the zero "
     "configuration (lvh2_corrected_iff, SIDE-explicit-formula RegisterDepth.lean at 81ae175)."),
    ('WHAT IT CONTAINS. h1_complete_at_Phi', 'STANDS', 'the eight coupling facts are compiled at Phi, as said', ''),
    ('The one deliberately open obligation is the clause itself', 'RESTS',
     'the kernel`s docstrings (lv `RegisterPentagon.lean:19-21`, v0.6.0 `CouplingsAtPhi.lean:415-416`) locate it as h2 = '
     '`mellin Phi (s / 2) ≠ 0`, which is not open but false at every s with re s ≤ 1',
     "The one deliberately open obligation is the clause itself; the kernel's docstrings locate it at h2 = mellin Phi (s/2) ≠ 0, "
     "which is false as stated at every s with re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one); the open clause is its "
     "completedRiemannZeta form, RH on the strip (lvh2_corrected_iff)."),
    ('discharges the certifiable surround as the coupling ledger `h1` complete at the assembly point Φ', 'RESTS',
     R_H2 + ', so "only h2 open" names a clause that is false on the strip',
     "The SIDE-lv-conservation terminal SIDELvConservation.h1_complete_at_Phi (v0.6.0 = c80bdc2, profile {propext, Classical.choice, "
     "Quot.sound}, grade DERIVES) compiles the coupling ledger h1 at the assembly point Φ; the ledger's goal ⇐ h1 ∧ h2 has h1 "
     "complete and its h2, mellin Φ (s/2) ≠ 0, false at every s with re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one), so the ledger "
     "does not carry this document's node on the strip."),
    ('That single open `h2` *is* this document\'s `covers_all`', 'RESTS',
     R_H2 + '; it is not covers_all and not equivalent to the other registers; its corrected form is `rh_strip` by `lvh2_corrected_iff`',
     "This document's covers_all is not the ledger's h2: that h2, the goal-state's clause mellin Φ (s/2) ≠ 0, is false at every s "
     "with re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one); with completedRiemannZeta in its place the strip clause is RH on the zero "
     "configuration (lvh2_corrected_iff), and the conservation register is RH restated (ch_iff_rh)."),
    ('| The surround is settled — kernel witness (§0, §6)', 'RESTS', R_H2 + ', so the status cell`s "only h2 = covers_all open" does not hold',
     "DERIVES — h1 (the coupling ledger at Φ) compiled complete; the ledger's h2, mellin Φ (s/2) ≠ 0, is false at every s with "
     "re s ≤ 1 (mellin_Phi_eq_zero_of_re_le_one), and it is not covers_all."),
]


def sentences():
    rows = []
    for name, scope, where, text in blocks():
        for s in sents(text):
            hits = [n for n, p in PAT if re.search(p, s)]
            rows.append(dict(block=name, scope=scope, where=where, sentence=s, hits=hits))
    yields = {n: sum(1 for r in rows if n in r['hits']) for n, _ in PAT}
    sel = [r for r in rows if r['hits']]
    used = set()
    for r in sel:
        g = [x for x in GRADES if x[0] in r['sentence']]
        if len(g) != 1:
            sys.exit('### SELECTED SENTENCE WITHOUT EXACTLY ONE GRADE (%d): %s' % (len(g), r['sentence'][:200]))
        r['grade'], r['reason'], r['replacement'] = g[0][1], g[0][2], g[0][3]
        used.add(g[0][0])
    unused = [x[0] for x in GRADES if x[0] not in used]
    if unused:
        sys.exit('### A TYPED GRADE MEETS NO SELECTED SENTENCE: %s' % unused)
    counts = {}
    for r in sel:
        k = (r['block'].split()[0] if r['scope'] == 'ordered' else 'outside', r['grade'])
        counts.setdefault(r['scope'], {}).setdefault(r['block'], {}).setdefault(r['grade'], 0)
        counts[r['scope']][r['block']][r['grade']] += 1
    put_json('b539_sentences.json', dict(read=len(rows), yields=yields, selected=sel, counts=counts))
    for n, v in yields.items():
        print('  matcher %-20s yield %d' % (n, v))
    print('  sentences read %d ; selected %d' % (len(rows), len(sel)))
    for i, r in enumerate(sel, 1):
        print('  %2d [%s | %s] %-7s %s' % (i, r['block'], r['scope'], r['grade'], r['sentence'][:150]))
    print('  counts : %s' % json.dumps(counts, ensure_ascii=False))


# ------------------------------------------------------------------------------ COMPONENT 2
TIERS = {  # the map's ranked terminal (as its cell names it) -> (tier, reason, profile source)
    'h1_complete_at_Phi': ('T0', 'DERIVES at lv v0.6.0 `c80bdc2`; its statement (the eight couplings at `Phi`) unfolds to facts about '
                                 'Mathlib`s `evenKernel` and `mellin`, no premise; T0 by criterion, NOT in (R149)(1)`s list. The map`s '
                                 'claim cell "only h2 open" is T2: it rests on lv`s h2, FALSE-AS-STATED at re s ≤ 1',
                           'lv v0.6.0 `CouplingsAtPhi.lean:417` docstring; SURR Correspondence `:184`'),
    'RegisterPentagon': ('T2', 'STRUCTURE at lv v0.7.0 `2d86182`; its faces include R1 FALSE-AS-STATED, R5-output TRUE-AS-STATED and '
                                '`goalState_sevenClasses_of_h2`, vacuous on the strip (b538)', 'SURR Correspondence `:185`'),
    'conservation_of_spectra': ('T2', 'DERIVES of `∀ s : ℤ, (1 : ℚ) ^ s = 1` (`one_zpow`) at SIDE-kernel v1.2 -- a STIPULATION: '
                                       'the conservation reading is carried by the namespace (SURR Correspondence `:178`)',
                                'SURR Correspondence `:178`'),
    'SIDEKernel.formation': ('T2', '`2 + 3 + 2 + 0 = 7` by `decide` at SIDE-kernel v1.2 `Kernel/Core.lean:53` -- arithmetic alone; '
                                    'the classification is carried by the identifier', 'SURR Correspondence `:180` (axiom-free)'),
    'C7_finite_type_false': ('T0', 'DERIVES at lv v0.5.1 `bc4751e`: `¬ ∃ C A, ∀ s, ‖completedRiemannZeta₀ s‖ ≤ C * exp (A * ‖s‖)` -- '
                                    'Mathlib`s object, no premise; T0 by criterion, NOT in (R149)(1)`s list', 'SURR Correspondence `:189`'),
    'partialPositivity_finiteRange': ('T4', 'INTERFACES at lv v0.8.0 `6efa9e5` on `VerifiedZerosTo T` (numerical), '
                                             '`ExplicitFormulaDecomp` and `TailBoundPremise` (classical, Mathlib-absent, not compiled); '
                                             'none is T0 or h2_sign, so the weakest link is a premise with no terminal (T1 if the '
                                             'author counts named classical premises as "named and open")', 'SURR Correspondence `:187`'),
    'blTerm_nonneg_of_onLine': ('T0', 'DERIVES at lv v0.8.0 `6efa9e5`: for a zero of Mathlib`s `riemannZeta` with re = 1/2, '
                                       '`0 ≤ (1 - (1 - 1/ρ)^n).re` -- Mathlib`s objects, no premise; T0 by criterion, NOT in '
                                       '(R149)(1)`s list', 'SURR Correspondence `:186`'),
    'type_I_has_ostrowski': ('T2', 'DERIVES at SIDE-kernel v1.2 `MetaKernel.lean:145`: modus tollens over an abstract `Domain` whose '
                                    '`Fintype` is unused -- logic alone ("exhaustiveness decorative", the map`s own cell)',
                             'VERIFICATION_LOOM-archive-1 `:60`'),
    'silence_universal': ('T2', 'INTERFACES on `I.is_universal` at SIDE-kernel v1.2: an abstract lemma about programme structures; its '
                                 'universal form, R1, is FALSE-AS-STATED (`not_register1`, b538)', 'VERIFICATION_LOOM-archive-1 `:413` (axiom-free)'),
    'spectral_cannon': ('T0', 'DERIVES at SIDE-kernel v1.2: `(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0` -- stated against '
                               'Mathlib`s `completedRiemannZeta₀`, not a ξ (Mathlib has none); T0 by criterion, NOT in (R149)(1)`s '
                               'list; its Route-2 reading as ξ is carried by the identifier', 'VERIFICATION_LOOM-archive-1 `:1018`'),
    'ξ / Dirichlet order-≤1 inputs': ('T0', 'DERIVES at lv v0.4.0 / v0.5.0: growth bounds on Mathlib`s `completedRiemannZeta₀` '
                                             '(`exists_norm_completedRiemannZeta₀_le_exp`) and `completedLFunction` '
                                             '(`exists_norm_completedLFunction_le_exp`), no premise but `χ ≠ 1`; T0 by criterion, NOT '
                                             'in (R149)(1)`s list', 'SURR Correspondence `:188`'),
    'ConservationBridge.riemann_hypothesis': ('T2', 'INTERFACES on `ConservationHypothesis` at SIDE-kernel v1.3/v1.5: that premise is '
                                                     'RH restated (`ch_iff_rh`, b531-b532), so the terminal is ENCODES-CONCLUSION',
                                              'relay `data/b532_profile_log.txt`'),
}
EXTRA = [  # terminals the ferry names that the ranked list does not rank
    ('h2_sign_iff_rh', 'SIDE-explicit-formula v0.2 = `5c72cad`', 'T0', 'the anchor tier; fresh line equal to its bank (component 1)'),
    ('goalState_sevenClasses_of_h2', 'lv v0.10.0 `RegisterPentagon.lean:215`', 'T2',
     'vacuous on the strip: its hypothesis `mellin Phi (s / 2) ≠ 0` is false at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`)'),
    ('structural_exhaustiveness_proved', 'SIDE-kernel v1.5 `0e5233f`', 'T2',
     'its catalogue conjunct is `Fintype.card MechanismClass = 7` by `decide` (E-2026-09-14-1) and C₇ is a disclosed stand-in '
     '(PATHS §ANNEX A `:320`); THE_KEYSTONE_CENSUS carries no C7 line (grep, 0 hits)')]


def ranked():
    rows = []
    for i, l in enumerate(rd(MAP).split(NL)[23:35], 24):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        term = re.search(r'`([^`]+)`', c[1])
        name = term.group(1) if term else c[1].split('(')[0].strip()
        if c[1].startswith('ξ'):
            name = 'ξ / Dirichlet order-≤1 inputs'
        rows.append(dict(line=i, rank=c[0].replace('*', ''), terminal=name, cell=c[1], pin=c[2], grade=c[3].replace('*', ''), citing=c[4]))
    return rows


def tiers():
    rows = ranked()
    for r in rows:
        if r['terminal'] not in TIERS:
            sys.exit('### RANKED TERMINAL WITHOUT A TIER: %s' % r['terminal'])
        r['tier'], r['reason'], r['profile'] = TIERS[r['terminal']]
    if len(rows) != len(TIERS):
        sys.exit('### TIERS TYPED FOR TERMINALS THE LIST DOES NOT RANK')
    counts = {t: sum(1 for r in rows if r['tier'] == t) for t in ('T0', 'T1', 'T2', 'T3', 'T4')}
    put_json('b539_tiers.json', dict(ranked=rows, extra=[dict(zip(('terminal', 'pin', 'tier', 'reason'), e)) for e in EXTRA], counts=counts,
                                      anchors=jl('b539_anchor.json').get('rows', [])))
    for r in rows:
        print('  %-3s %-40s %s -- %s' % (r['rank'], r['terminal'][:40], r['tier'], r['reason'][:90]))
    for e in EXTRA:
        print('  --  %-40s %s -- %s' % (e[0], e[2], e[3][:90]))
    print('  ### RANKED LIST TIER COUNTS : %s' % counts)


def appendix():
    tj, aj = jl('b539_tiers.json'), jl('b539_anchor.json')
    L = ['', '<!-- b539 (R149) APPENDIX, 2026-09-25 -->', '', ATITLE, '',
         '*Appended by b539 under the author`s ruling `(R149)` (the cascade, act one). **No earlier byte of this map changes**; the '
         'ranked list (A) above keeps its grades, and this appendix sets the tier of `(R149)`(2) beside each, with the reason in one '
         'clause: the terminal`s own grade at its pin, and the tier of the weakest link between it and Mathlib. A terminal whose '
         'statement, read at its pin, is about Mathlib`s own objects with no premise meets the T0 criterion and is flagged where '
         '`(R149)`(1)`s anchor list does not name it -- whether the list widens is the author`s. Profiles are the corpus`s own prints '
         'at the pin, each source named; the anchor tier`s are from a fresh run at SIDE-explicit-formula `%s` (relay '
         '`data/b539_anchor_log.txt`).*' % aj.get('head', '')[:7], '',
         '**The anchor tier, `(R149)`(1), fresh:**', '', '| anchor | module · pin | `#print axioms` (fresh, equal to its bank) | statement |',
         '|:--|:--|:--|:--|']
    for r in aj.get('rows', []):
        L.append('| `%s` | `%s` · %s | %s | `%s` |' % (r['name'].split('.')[-1], r['module'], r['pin'], r['fresh'].split("' ", 1)[1],
                                                     (r['check'] or '').replace('|', '∣')))
    L += ['| R3 | lv v0.10.0 `RegisterPentagon.lean:139-140` | -- | **UNDECIDED** (the census, `FINDINGS.md:4787`) |', '',
          '**The ranked list (A), tiered:**', '', '| rank | terminal | pin | grade (kept) | tier | reason | profile source |',
          '|:--|:--|:--|:--|:--|:--|:--|']
    for r in tj['ranked']:
        L.append('| %s | `%s` | %s | %s | **%s** | %s | %s |' % (r['rank'], r['terminal'], r['pin'], r['grade'], r['tier'],
                                                              r['reason'].replace('|', '∣'), r['profile']))
    L += ['', '**Tier counts over the ranked list:** ' + ' · '.join('%s %d' % (k, v) for k, v in tj['counts'].items()) + '.', '',
          '**Terminals the ferry names that the ranked list does not rank (not counted above):**', '',
          '| terminal | pin | tier | reason |', '|:--|:--|:--|:--|']
    for e in tj['extra']:
        L.append('| `%s` | %s | **%s** | %s |' % (e['terminal'], e['pin'], e['tier'], e['reason']))
    L += ['', '**What `h1_complete_at_Phi` certifies after b538.** That Mathlib`s theta-kernel function `Phi = (evenKernel 0 − 1)/2` '
              'satisfies the eight coupling facts of Ch. 15 -- realness, Mellin nonvanishing on re s > 1, theta inversion, the modular '
              'laws, the heat trace of {n²}, holomorphy, and the entire order-≤1 completion. It certifies nothing about zeros in the '
              'strip: the witness`s Mellin integral vanishes at every s with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`), so h1 ∧ h2 '
              'at Phi holds at no s of the strip, and the ledger`s h1 is complete at a witness that witnesses nothing there.', '',
          '*The map`s (B) inventory and (C) h2-reach figure above are not edited; where they call `h2` "the single carried-open '
          'premise", lv`s h2 is FALSE-AS-STATED on the strip and its corrected form is RH on the zero configuration '
          '(`lvh2_corrected_iff`); the deposit-facing sentences are read in relay `data/b539_erratum_draft.md` (E-2026-09-25-3, '
          'DRAFT, NOT FILED). Nothing deposits.*', '']
    w = append_to(MAP, NL.join(L))
    w['heading_line'] = rd(MAP).split(NL).index(ATITLE) + 1
    put_json('b539_appendix.json', w)
    print('  map : %(added)d bytes added, prefix %(prefix)s ; the appendix at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ the erratum draft
def erratum():
    sj = jl('b539_sentences.json')
    rest = [r for r in sj['selected'] if r['grade'] == 'RESTS']
    L = ['## E-2026-09-25-3 — The ledger\'s h2 is false on the critical strip; the sentences that call it the one open premise, or '
         'identify it with covers_all, rest on it (DEPOSIT-FACING FOR SIDE-lv-conservation v0.10.0; CORPUS-FACING FOR THE UNCONDITIONAL '
         'SURROUND v0.4) — DRAFT, NOT FILED', '',
         '**Drafted 2026-09-25 (b539), on the author\'s ruling (R149)(4)-(5), from the register census of b538 (FINDINGS.md:4787) and '
         'the reading banked at b539 (relay data/b539_sentences.json); TO BE FILED only on the author\'s word at the act after.',
         '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
         '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**', '',
         '**Affected.** SIDE-lv-conservation v0.10.0, Zenodo record 21539068 ([10.5281/zenodo.21539068](https://doi.org/10.5281/zenodo.21539068)) '
         '— the record title and description, as b499 fetched them back (relay data/b499_fetchback_21539068.json; b535 edited other '
         'records only). The corpus document THE_UNCONDITIONAL_SURROUND.md v0.4 (REGISTRY 1.5a-6, REVIEW, not deposited) — §0 line 37, '
         '§6, and its Correspondence row at line 184.', '',
         '**What the kernel says, in its own words.** SIDE-explicit-formula RegisterDepth.lean at 81ae175, each at the standard three or '
         'fewer, read fresh at b539: mellin_Phi_eq_zero_of_re_le_one : ∀ (s : ℂ), s.re ≤ 1 → mellin Phi (s / 2) = 0, with Phi the '
         'ledger\'s own witness (lv T1_MellinFactorization.lean:26, restated verbatim); lvh2_corrected_iff : (∀ (s : ℂ), 0 < s.re → '
         's.re < 1 → s.re ≠ 1 / 2 → completedRiemannZeta s ≠ 0) ↔ rh_strip; not_register1 : the R1 face is false; '
         'register5_output_holds : the R5-output face holds unconditionally. Mathlib\'s mellin is a Bochner integral, zero where its '
         'integrand is not integrable, and Phi grows like t^(−1/2)/2 near 0.', '',
         '**The sentences, each with its replacement drafted from those statements** (b539 read %d sentences in the ordered scope and '
         'the adjacent block; the RESTS rows follow; the STANDS rows are in the bank):' % len(sj['selected']), '']
    for i, r in enumerate(rest, 1):
        L += ['- **%s** (%s, %s): *"%s"*' % (r['block'], r['where'], 'ordered scope' if r['scope'] == 'ordered' else 'adjacent, outside the '
                                                                                                                       'ordered scope', r['sentence']),
              '  - reads **RESTS** — %s.' % re.sub(r"(?<=[A-Za-z0-9])`s\b", "'s", r['reason']).replace('`', ''),
              '  - replacement: *"%s"*' % r['replacement']]
    L += ['', '**What is not corrected.** That h1_complete_at_Phi is compiled; that covers_all is the kernel\'s open field; the '
              'manuscript\'s own readings of the node (§6\'s analytic and Euler-product faces, step (9)); R3, which stays UNDECIDED. '
              'No sentence was found to EXCEED.', '',
          '**Status.** DRAFT. Not filed. Retained at SIDE-lv-conservation v0.10.0 and THE_UNCONDITIONAL_SURROUND v0.4. Whether any '
          'Zenodo description is edited under (R110) is the author\'s ruling; the filing is the author\'s word at the act after.', '']
    txt = NL.join(L)
    io.open(os.path.join(D, 'b539_erratum_draft.md'), 'w', encoding='utf-8', newline=NL).write(txt)
    bt = len(re.findall(r"[A-Za-z]`s\b", txt))
    put_json('b539_erratum.json', dict(rests=len(rest), backtick_possessives=bt, bytes=len(txt.encode('utf-8'))))
    print('  erratum draft : %d RESTS rows ; backtick possessives %d ; %d bytes' % (len(rest), bt, len(txt.encode('utf-8'))))


# ------------------------------------------------------------------------------ COMPONENT 4
SURR_TIERS = {  # SURR Correspondence line -> (tier, reason, rests-on)
    175: ('T4', 'a hypothesis field, not a theorem; its discharge is manuscript-resident', 'covers_all'),
    176: ('T2', 'axiom-free and abstract -- logic alone over the kernel`s catalogue; it consumes `covers_all` as its hypothesis', 'covers_all'),
    177: ('T4', 'the pin `T3_perClass_to_combinations` carries `sorryAx`; the closure step has no terminal', 'covers_all'),
    178: ('T2', '`conservation_of_spectra` is `(1 : ℚ) ^ s = 1`, a STIPULATION; `T2b` DEFINITIONAL; `T1_...factors_through_mellin` alone '
               'is T0 by criterion', ''),
    179: ('T2', 'three of the five voices are one map `1 - σ = σ`, voice6 ENCODES-CONCLUSION, the C₇ stand-in ENCODES-CONCLUSION', ''),
    180: ('T2', '`2 + 3 + 2 + 0 = 7` by `decide`: arithmetic alone', ''),
    181: ('T2', 'a count of a kernel-defined type; the Stein / Cousin-I pillar set aside open', ''),
    182: ('T4', 'computational, with no VERIFIED bank named', ''),
    183: ('T4', 'manuscript-resident; no terminal', 'covers_all'),
    184: ('T2', 'the terminal is T0 by criterion, but the status cell`s "only h2 = covers_all open" rests on lv`s h2, FALSE-AS-STATED at '
               're s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`)', 'lv`s h2'),
    185: ('T2', 'the pentagon`s faces include R1 FALSE-AS-STATED, R5-output TRUE-AS-STATED, and `goalState_sevenClasses_of_h2` vacuous on '
               'the strip', 'lv`s h2'),
    186: ('T0', 'Mathlib`s zeros of `riemannZeta`, no premise; by criterion, not in `(R149)`(1)`s list', ''),
    187: ('T4', 'INTERFACES on three named premises, none compiled, none T0 or h2_sign', ''),
    188: ('T0', 'Mathlib`s `completedLFunction`, no premise but `χ ≠ 1`; by criterion, not in `(R149)`(1)`s list', ''),
    189: ('T0', 'Mathlib`s `completedRiemannZeta₀`, no premise; by criterion, not in `(R149)`(1)`s list', '')}


def surr():
    S = rd(SURR).split(NL)
    L = ['', '<!-- b539 (R149) TIER TABLE, 2026-09-25 -->', '', STITLE, '',
         '*Appended by b539 under `(R149)`(2)-(4): one row per row of the Correspondence table at `:175-189`, each with its claim as '
         'stated there, its terminal at its pin, the status cell`s grade kept, the tier of `(R149)`(2) with its reason, and '
         'E-2026-09-25-3 (relay `data/b539_erratum_draft.md`, DRAFT, NOT FILED) where the row rests on lv`s h2 or on `covers_all`. '
         '**No byte above this block changes.***', '',
         '| line | claim (as stated above) | terminal · pin | tier | reason | rests on | erratum |', '|:--|:--|:--|:--|:--|:--|:--|']
    rows = []
    for ln in range(175, 190):
        c = [x.strip() for x in S[ln - 1].strip().strip('|').split('|')]
        tier, reason, rests = SURR_TIERS[ln]
        rows.append(dict(line=ln, claim=c[0], kernel=c[1], terminal=c[2][:160], tier=tier, rests=rests))
        L.append('| :%d | %s | %s · %s | **%s** | %s | %s | %s |' % (ln, c[0], c[2][:160].replace('|', '∣'), c[1], tier, reason,
                                                                     rests or '--', E3 if rests else '--'))
    counts = {t: sum(1 for r in rows if r['tier'] == t) for t in ('T0', 'T1', 'T2', 'T3', 'T4')}
    L += ['', '**Tier counts over this table:** ' + ' · '.join('%s %d' % (k, v) for k, v in counts.items())
          + ' ; rows referencing E-2026-09-25-3: %d.' % sum(1 for r in rows if r['rests']), '']
    w = append_to(SURR, NL.join(L))
    w.update(rows=rows, counts=counts, heading_line=rd(SURR).split(NL).index(STITLE) + 1)
    put_json('b539_surr.json', w)
    print('  SURR : %d bytes added, prefix %s ; table at line %d ; counts %s' % (w['added'], w['prefix'], w['heading_line'], counts))


# ------------------------------------------------------------------------------ COMPONENT 5
def findings():
    tj, sj, su = jl('b539_tiers.json'), jl('b539_sentences.json'), jl('b539_surr.json')
    oc = sj['counts'].get('ordered', {})
    def c(block, g):
        return oc.get(block, {}).get(g, 0)
    surr_s = sum(c(b, 'STANDS') for b in oc if b.startswith('SURR'))
    surr_r = sum(c(b, 'RESTS') for b in oc if b.startswith('SURR'))
    lv_s = sum(c(b, 'STANDS') for b in oc if b.startswith('lv'))
    lv_r = sum(c(b, 'RESTS') for b in oc if b.startswith('lv'))
    ex = sum(c(b, 'EXCEEDS') for b in oc)
    out = sj['counts'].get('outside', {})
    out_r = sum(v.get('RESTS', 0) for v in out.values())
    L = ['', FTITLE, '',
         '*Filed at b539 on the author`s ruling `(R149)`. The anchor tier, the load-bearing map`s ranked terminals, and the sentences '
         'of THE_UNCONDITIONAL_SURROUND and of lv-conservation`s deposited description that carry the h2 frame, read against the '
         'register census (`FINDINGS.md:4787`). Sources: relay `data/b539_anchor.json`, `data/b539_tiers.json`, '
         '`data/b539_sentences.json`, `data/b539_erratum_draft.md`.*', '',
         '**The anchor tier, fresh.** All %d anchor theorems of `(R149)`(1) re-profiled at SIDE-explicit-formula `%s`, each line '
         'equal to its bank; R3 carried UNDECIDED.' % (len(jl('b539_anchor.json').get('rows', [])), jl('b539_anchor.json').get('head', '')[:7]), '',
         '**The hub terminals tiered** (THE_LOAD_BEARING_MAP, appendix at line %s): over the map`s twelve ranked terminals, '
         % jl('b539_appendix.json').get('heading_line') + ' · '.join('%s **%d**' % (k, v) for k, v in tj['counts'].items())
         + '. The T0 rows meet the criterion by their statements -- `h1_complete_at_Phi`, `C7_finite_type_false`, '
           '`blTerm_nonneg_of_onLine`, `spectral_cannon`, the order-≤1 inputs -- and none is in `(R149)`(1)`s list, which the map '
           'does not rank; whether the list widens is the author`s. `ConservationBridge.riemann_hypothesis` and '
           '`goalState_sevenClasses_of_h2` are T2.', '',
         '**THE_UNCONDITIONAL_SURROUND §5-§6 and lv-conservation`s description, read.** In the ordered scope: SURR **STANDS %d · '
         'RESTS %d**; lv **STANDS %d · RESTS %d**; **EXCEEDS %d**. Outside the ordered scope, SURR §0 `:37` and Correspondence `:184` '
         'read RESTS %d. The RESTS sentences are the ones that call lv`s h2 the one open premise or identify it with `covers_all`; '
         'lv`s h2 is FALSE-AS-STATED on the strip (`mellin_Phi_eq_zero_of_re_le_one`) and its corrected face is RH on the zero '
         'configuration (`lvh2_corrected_iff`). lv`s description does not contain the words "h2" or "h1 complete, h2 open".'
         % (surr_s, surr_r, lv_s, lv_r, ex, out_r), '',
         '**SURR`s Correspondence, tiered** (line %s of that document): ' % su.get('heading_line')
         + ' · '.join('%s %d' % (k, v) for k, v in su['counts'].items()) + '.', '',
         '**E-2026-09-25-3 is DRAFTED, NOT FILED** (relay `data/b539_erratum_draft.md`). **Next:** the act after decides the filing on '
         'the author`s word; the next keystone of the cascade is PATHS (`PATHS_TO_THE_CRITICAL_LINE.md`).', '']
    w = append_to(FIND, NL.join(L))
    w['heading_line'] = rd(FIND).split(NL).index(FTITLE) + 1
    w.update(surr_stands=surr_s, surr_rests=surr_r, lv_stands=lv_s, lv_rests=lv_r, exceeds=ex, outside_rests=out_r)
    put_json('b539_findings.json', w)
    print('  FINDINGS : %(added)d bytes added, prefix %(prefix)s ; entry at line %(heading_line)d' % w)
    print('  ordered : SURR STANDS %d RESTS %d ; lv STANDS %d RESTS %d ; EXCEEDS %d ; outside RESTS %d' % (surr_s, surr_r, lv_s, lv_r, ex, out_r))


# ------------------------------------------------------------------------------ desk
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    return sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b539_'))


PRIOR_PP = 'c658a55'


def scores():
    tj, fj, aj = jl('b539_tiers.json'), jl('b539_findings.json'), jl('b539_anchor.json')
    t0 = [r['terminal'] for r in tj.get('ranked', []) if r['tier'] == 'T0']
    ex = {e['terminal']: e['tier'] for e in tj.get('extra', [])}
    rk = {r['terminal']: r['tier'] for r in tj.get('ranked', [])}
    files = {'THE_LOAD_BEARING_MAP.md': 'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'THE_UNCONDITIONAL_SURROUND.md': 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
             'FINDINGS.md': 'FINDINGS.md', 'OPEN_TRAILS.md': 'OPEN_TRAILS.md'}
    prefix = {k: open(os.path.join(PP, v), 'rb').read().startswith(blob(PP, '%s:%s' % (PRIOR_PP, v))) for k, v in files.items()}
    same = {f: blob(PP, '%s:%s' % (PRIOR_PP, f)) == open(os.path.join(PP, f), 'rb').read() for f in ('ERRATA.md', 'README.md', 'REGISTRY.md')}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b539_') and needle in rd(os.path.join(T, x))]
    ker = {n: git(p, 'status', '--porcelain', '--untracked-files=no') == '' for n, p in
           (('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel'), ('SIDE-lv-conservation', 'D:/SIDE-lv-conservation'))}
    kheads = dict(sef=git('D:/SIDE-explicit-formula', 'rev-parse', 'HEAD').startswith('81ae175'))
    tok = token_count()
    dep = git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''
    anc = aj.get('rows', [])
    b321 = next((r['check'] for r in anc if r['name'].endswith('b321_identity')), '') or ''
    return dict(
        n1=len(t0) == 1 and t0 == ['h2_sign_iff_rh'], t0=t0,
        n2=ex.get('goalState_sevenClasses_of_h2') == 'T2' and rk.get('ConservationBridge.riemann_hypothesis') == 'T2',
        n3=fj.get('surr_rests', 0) >= 2 and fj.get('lv_rests', 0) >= 1 and fj.get('exceeds', 1) == 0,
        n4=all(prefix.values()), prefix=prefix,
        n5=all(same.values()) and not zen and all(ker.values()) and all(kheads.values()) and tok == 0 and dep,
        same=same, zenodo_tools=zen, kernels=ker, token=tok, deposit_clean=dep,
        s1=bool(anc) and all(r['equal'] for r in anc) and not aj.get('diffs'),
        s2='EF_lit_zetaZeroConfig' in b321,
        s3=jl('b539_erratum.json').get('backtick_possessives', 1) == 0)


def w(v):
    return 'HELD' if v else 'REFUTED'


def components():
    L = ['=' * 132, 'b539 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### READING (1) -- THE PURPOSE STATEMENTS:']
    L += ['  ' + l for l in rd(os.path.join(D, 'b539_purpose.txt')).rstrip(NL).split(NL)[2:]]
    aj = jl('b539_anchor.json')
    L += ['', '### COMPONENT 1 -- THE ANCHOR TIER, FRESH at SIDE-explicit-formula %s (exit %s, %s s):' % (aj.get('head', '')[:12], aj.get('exit'), aj.get('seconds'))]
    for r in aj.get('rows', []):
        L += ['  %s -- %s -- %s' % (r['name'], 'EQUAL TO ITS BANK' if r['equal'] else 'DIFFERS', r['fresh']), '      #check %s' % r['check']]
    L += ['  ' + aj.get('r3', '')]
    tj = jl('b539_tiers.json')
    L += ['', '### COMPONENT 2 -- THE RANKED LIST, TIERED (map appendix at line %s):' % jl('b539_appendix.json').get('heading_line')]
    L += ['  %-4s %-40s %s -- %s' % (r['rank'], r['terminal'][:40], r['tier'], r['reason']) for r in tj.get('ranked', [])]
    L += ['  --   %-40s %s -- %s' % (e['terminal'], e['tier'], e['reason']) for e in tj.get('extra', [])]
    L += ['  counts : %s' % tj.get('counts')]
    sj = jl('b539_sentences.json')
    L += ['', '### COMPONENT 3 -- THE SENTENCES: read %s ; yields %s' % (sj.get('read'), sj.get('yields'))]
    L += ['  %-8s [%s | %s] %s' % (r['grade'], r['block'], r['scope'], r['sentence'][:200]) for r in sj.get('selected', [])]
    L += ['  erratum draft : ' + json.dumps(jl('b539_erratum.json'))]
    su = jl('b539_surr.json')
    L += ['', '### COMPONENT 4 -- SURR`S TABLE, TIERED (line %s) : %s' % (su.get('heading_line'), su.get('counts'))]
    L += ['', '### COMPONENT 5 -- FINDINGS : ' + json.dumps(jl('b539_findings.json'), ensure_ascii=False), '=' * 132]
    io.open(os.path.join(D, 'b539_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    N = ('n1', 'n2', 'n3', 'n4', 'n5')
    S = ('s1', 's2', 's3')
    fj = jl('b539_findings.json')
    L = ['=' * 104, 'b539 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S FIVE.', '-' * 104,
         '  **(N1)** ### **%s.** -- T0 in the ranked list : %s ; `h2_sign_iff_rh` is not ranked by the map.' % (w(sc['n1']), sc['t0']),
         '  **(N2)** ### **%s.** -- goalState_sevenClasses_of_h2 T2 ; ConservationBridge.riemann_hypothesis T2.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- SURR RESTS %s ; lv RESTS %s ; EXCEEDS %s.' % (w(sc['n3']), fj.get('surr_rests'), fj.get('lv_rests'), fj.get('exceeds')),
         '  **(N4)** ### **%s.** -- prior bytes a prefix : %s.' % (w(sc['n4']), sc['prefix']),
         '  **(N5)** ### **%s.** -- ERRATA, README, REGISTRY byte-identical : %s ; kernels clean : %s ; b539 tools naming the platform`s '
         'address %s ; token hits %s ; deposit tree clean %s.' % (w(sc['n5']), sc['same'], sc['kernels'], sc['zenodo_tools'] or 'NONE',
                                                                 sc['token'], sc['deposit_clean']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- every anchor line equal to its bank.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- b321_identity`s statement names zeroSide, b321Norm, poleTerm, primeSum and archTerm; '
         '`EF_lit_zetaZeroConfig` enters its proof (`B321Identity.lean:47`), not its statement.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- backtick possessives in the draft : %s.' % (w(sc['s3']), jl('b539_erratum.json').get('backtick_possessives')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in S].count(True), [sc[k] for k in S].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b539_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b539_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b539_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b539_scores.json', sc)
    print(NL.join(L))


def trail():
    sc, tj, fj = scores(), jl('b539_tiers.json'), jl('b539_findings.json')
    body = ['', HEADING, '',
            '**(R149) ratified.** The cascade: keystones, their Correspondence tables and kernels reconciled from the most verified '
            'claims outward; the anchor tier fixed; five tiers T0-T4 appended beside the grades, never replacing them; one or two '
            'keystones per act, hubs first; the K-programme absorbed; this act the opening step.', '',
            '**The anchor tier, fresh** at SIDE-explicit-formula `81ae175`: all eight theorems equal to their banks; R3 UNDECIDED.', '',
            '**The hub terminals tiered** (`phase1.5/method/THE_LOAD_BEARING_MAP.md`, appendix at line %s): %s. Five ranked '
            'terminals meet the T0 criterion by statement and none is on `(R149)`(1)`s list, which the map does not rank.'
            % (jl('b539_appendix.json').get('heading_line'), ' · '.join('%s %d' % kv for kv in tj['counts'].items())), '',
            '**SURR §5-§6 and lv`s description read:** SURR STANDS %d · RESTS %d; lv STANDS %d · RESTS %d; EXCEEDS %d; outside the '
            'ordered scope RESTS %d. **E-2026-09-25-3 DRAFTED, NOT FILED** (relay `data/b539_erratum_draft.md`); SURR`s Correspondence '
            'tiered in a table beneath the old (line %s); the FINDINGS entry at line %s.'
            % (fj['surr_stands'], fj['surr_rests'], fj['lv_stands'], fj['lv_rests'], fj['exceeds'], fj['outside_rests'],
               jl('b539_surr.json').get('heading_line'), fj.get('heading_line')), '',
            '**Next:** the filing of E-2026-09-25-3 on the author`s word; the next keystone, PATHS.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; nothing filed to '
            'ERRATA; the ceiling unchanged; no grade moved on any row; row U1 unedited; `h2` where the deposit left it; the four '
            'lists stay OPEN; nothing here is a statement about RH.', '']
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b539_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'purpose': purpose, 'sentences': sentences, 'tiers': tiers, 'appendix': appendix, 'erratum': erratum, 'surr': surr,
              'findings': findings, 'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
