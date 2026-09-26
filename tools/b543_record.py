# -*- coding: utf-8 -*-
"""b543_record.py -- THE MONOGRAPH READ, ACT TWO, UNDER (R153): THE RECORD.
### `python tools/b543_record.py reads | anchor | census | terms | erratum6 | map | components | desk | trail`

### The monograph is READ, never written. Every act-two row meets exactly one typed row (READING (2)); a row carried from b532
### or b541 must agree with that act's verdict unless marked. FINDINGS takes one append, OPEN_TRAILS one; ERRATA nothing;
### FINDINGS.md:1109 nothing (READING (5)). This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b541_record as A
PP = A.PP
LIVE, DEP, ERR, FIND, OT = A.LIVE, A.DEP, A.ERR, A.FIND, A.OT
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B543_SCRATCH', '')
NL = chr(10)
FTITLE = ('## A Place To Stand read against the RH-anchor: the sentence census and the chapter tier map, act two -- Chapter 26 '
          'to the end, the second half of the map at FINDINGS.md:4834')
HEADING = ('### b543 — the monograph read against the RH-anchor, act two under (R153): Chapter 26 to the end graded, '
           "E-2026-09-25-6 drafted, the chapter tier map completed, CP-1's monograph part closed")
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
rd, jl, outside_bt, md5 = A.rd, A.jl, A.outside_bt, A.md5


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def append_to(path, text):
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def g(repo, *a):
    return subprocess.run(['git', '-C', os.path.join('D:', os.sep, repo)] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ------------------------------------------------------------------------------ READING (7): the reads and the anchor
READS = [('SIDE-kernel', 'v1.5', 'Bridge/TheBridgeComplete.lean', [(157, 165), (215, 251)]),
         ('SIDE-kernel', 'v1.5', 'Kernel/PoissonExhaustion.lean', [(43, 69)]),
         ('SIDE-kernel', 'v1.5', 'Bridge/ConservationBridge.lean', [(1, 10 ** 6)]),
         ('SIDE-kernel', 'v1.5', 'Kernel/Integration.lean', [(212, 229)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/RegisterPentagon.lean', [(82, 83), (106, 107), (139, 140), (189, 195)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/RegisterDepth.lean', [(1, 10 ** 6)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/H2Bridge.lean', [(1, 10 ** 6)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/Seam.lean', [(1, 10 ** 6)])]


def reads():
    L = ['b543 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    cj = jl('b541_census.json')
    L += ['### relay data/b541_census.json : halt %s ; act two live %d ; past-halt deposited %d' % (cj['halt'], cj['halt']['act_two_live'], len(cj['past_halt']))]
    f = rd(FIND).split(NL)
    for n in (4787, 4834, 4884):
        L.append('### FINDINGS.md:%d %s' % (n, f[n - 1][:200]))
    e = rd(ERR).split(NL)
    L += ['', '### ERRATA.md:477-687 -- the headings of E-1 to E-5 (E-2`s is a bold line, not a ## heading)'] + [
        '  :%d %s' % (i + 1, e[i][:200]) for i in range(476, min(687, len(e))) if e[i].startswith('## E-') or e[i].startswith('**`E-')]
    L += ['### relay data/b541_erratum_draft.md : md5 %s, as filed at ERRATA.md:613-687' % md5(os.path.join(D, 'b541_erratum_draft.md'))]
    for repo, pin, path, spans in READS:
        t = g(repo, 'show', '%s:%s' % (pin, path)).replace(chr(13), '').split(NL)
        for a, b in spans:
            b = min(b, len(t))
            L += ['', '### %s %s %s:%d-%d' % (repo, g(repo, 'rev-parse', '--short', pin + '^{commit}').strip(), path, a, b)] + ['  :%d %s' % (i + 1, t[i]) for i in range(a - 1, b)]
    io.open(os.path.join(D, 'b543_reads.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  reads banked : %d lines' % len(L))


ANCHOR = ['SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula.B321.ch_iff_rh', 'SIDEExplicitFormula.RegisterDepth.not_register1',
          'SIDEExplicitFormula.RegisterDepth.register5_output_holds', 'SIDEExplicitFormula.RegisterDepth.lvh2_corrected_iff',
          'SIDEExplicitFormula.RegisterDepth.lv_h2_false_on_strip']


def anchor():
    src = ['import SIDEExplicitFormula.RegisterDepth', ''] + ['#check @' + n for n in ANCHOR]
    p = os.path.join(SCR, 'b543_anchor_check.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = subprocess.run(['git', '-C', KER, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = r.stdout.replace(chr(13), '')
    L = ['b543 -- THE RH-ANCHOR, FRESH #check at SIDE-explicit-formula %s (exit %d)' % (head, r.returncode)] + ['  ' + l for l in out.split(NL) if l.strip()]
    io.open(os.path.join(D, 'b543_anchor.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (2): the grades, typed from the pre-seal read
E1, E3, E4, E5, E6, E914 = 'E-2026-09-25-1', 'E-2026-09-25-3', 'E-2026-09-25-4', 'E-2026-09-25-5', 'E-2026-09-25-6', 'E-2026-09-14-1'
S, H, R = 'STANDS', 'STANDS-AS-HISTORY', 'RESTS'
DEPTHS = ("These registers stand at different depths (b538): the first is false as stated (not_register1); the second is RH restated "
          "(ch_iff_rh); the third is undecided; the fourth, in its Weil form, is equivalent to RH (h2_sign_iff_rh); the fifth's compiled "
          "face holds outright (register5_output_holds).")
# (live line, needle, grade, tier, errata, subject, carried, reason, replacement)
GR = [
    (1708, 'The last axiom', R, 'T0', [E6], E5, '', 'a dated record inaccurate at its own date: the compiled fact is about Mathlib`s completedRiemannZeta₀ (spectral_cannon, deriv_fe), not ξ -- E-5`s kind',
     "The last axiom (schwarz_deriv, in the perpendicular crossing probe) fell when path differentiation of the FOCUS identity showed that the derivative of Mathlib's completedRiemannZeta₀ inherits the functional equation's symmetry -- a fact about completedRiemannZeta₀, the entire part of the completed zeta; the same fact for ξ′ is not compiled."),
    (1708, 'The method`s continuation'.replace('`', "'"), R, 'T2', [E1], E1, 'M-18', 'b532 M-18, listed in E-2026-09-25-1', ''),
    (1763, 'The n₃ = 2 enumeration', H, 'T2', [], '', '', 'the research arc, accurate to its date: output_stage_card is at v1.5 Bridge/CartanBBridge.lean:79', ''),
    (1775, '**The SIDE method.**', S, 'T4', [], '', '', 'the method`s statement', ''),
    (1779, '**The Lean kernel.**', S, 'T2', [], '', 'M-19', 'b532 M-19: route terminals and their profiles, as compiled', ''),
    (1793, '**The five registers.** First', R, 'T2', [E6], '', '', 'register 1 as a register of the premise: as stated it is false (not_register1, b538)',
     "The five registers. First: the universality hypothesis carried by the Universal Silence Theorem -- stated for every essential interface, as the register states it, it is false (not_register1); what Chapter 14 uses is the hypothesis at each interface."),
    (1793, 'Chapter 14 states it plainly', S, 'T2', [], '', '', 'what Chapter 14 and silence_universal state', ''),
    (1793, 'Second: the proposition named', R, 'T2', [E1], E1, 'M-20', 'b532 M-20, listed in E-2026-09-25-1', ''),
    (1793, 'As of kernel v1.3', H, 'T2', [], '', 'M-21', 'b532 M-21 STANDS; a dated "as of" record, printed STANDS-AS-HISTORY under (R153)(2)', ''),
    (1793, 'This is distinct from the Mechanism Theorem', S, 'T2', [], '', '', 'the Mechanism Theorem compiles as logic over abstract types (b542: SIDE_exclusion); the open part named as the premise', ''),
    (1793, 'The input-stage spectral coupling', S, 'T4', [], '', '', 'the input stage certified; the Hilbert–Pólya realization disclaimed, as said', ''),
    (1793, 'Over ℚ the realization space', R, 'T2', [E6], '', '', 'the fifth register`s compiled output face holds outright (register5_output_holds), so it is not the premise in any register',
     "Over ℚ the realization space is infinite-dimensional and no positive pairing is known; the fifth register's compiled output face holds outright (register5_output_holds), so the Hilbert–Pólya content lies beyond that face, and the distance between the two stages is not one register of an equivalent premise."),
    (1793, 'On the detection side', S, 'T0', [], '', '', 'detection_threshold_mono at lv word-pairing-interface c5ef4bc (ZeroActingPartial.lean:105): N₀ monotone -- live line only', ''),
    (1793, 'The construction era', H, 'T2', [], '', '', 'a dated era record (2026-08)', ''),
    (1795, 'These are one premise in five registers', R, 'T2', [E6], '', '', 'the registers stand at four depths (b538), not one premise', DEPTHS),
    (1797, '**The ancestry of the sharpest form.**', S, 'T4', [], '', '', 'citations of the literature', ''),
    (1797, 'The programme`s channel decomposition'.replace('`', "'"), S, 'T2', [], '', '', 'the linearity compiled; the scope stated', ''),
    (1799, '**The compiled shape.**', H, 'T4', [], '', '', 'a dated record (July 2026)', ''),
    (1801, 'The formalization then did', R, 'T2', [E4], E4, '', 'listed in E-2026-09-25-4 (deposited :1787)', ''),
    (1806, '**The unrestricted commutation is false**', S, 'T2', [], '', '', 'the countermodel T3″ compiled', ''),
    (1808, '**What remains, exactly.**', R, 'T2', [E4], E4, '', 'listed in E-2026-09-25-4 (deposited :1794)', ''),
    (1808, 'As of SIDE-lv-conservation v0.6.0', S, 'T0', [], '', '', 'h1_complete_at_Phi at v0.6.0 c80bdc2', ''),
    (1808, 'At v0.4.0 the kernel', H, 'T2', [], '', '', 'a dated record (v0.4.0)', ''),
    (1808, 'C₅-output remains the disclaimed', R, 'T2', [E6], '', '', 'the fifth register`s compiled output face holds outright (register5_output_holds): the disclaimer disclaims a theorem, (R151)(3)',
     "C₅-output's compiled face holds outright (register5_output_holds); what the programme disclaims is the Hilbert–Pólya realization, which that face does not state."),
    (1808, 'The obligation h2 is', S, 'T1-open', [], '', '', 'h2_sign ↔ RiemannHypothesis compiled (h2_sign_iff_rh): the Weil-positivity face is the theorem itself', ''),
    (1808, 'The premise is RH-equivalent', R, 'T1-open', [E4], E4, '', 'listed in E-2026-09-25-4 (deposited :1794, its second row)', ''),
    (1810, '**The registers, compiled.**', H, 'T2', [], '', '', 'a dated record', ''),
    (1810, 'SIDE-lv-conservation now carries', H, 'T2', [], '', '', 'accurate to its date (v0.7.0); compiling the cross-register relations at b538 found the registers at four depths', ''),
    (1810, 'The fourth register`s door stands'.replace('`', "'"), S, 'T1-lit', [], '', '', 'partialPositivity_finiteRange under named premises, which the next sentence names -- live line only', ''),
    (1810, 'At v0.10.0 the fourth register', S, 'T1-lit', [], '', '', 'lowFinset_mem_iff at v0.10.0; the decomposition and tail premises named open', ''),
    (1810, 'And the fifth register`s distance'.replace('`', "'"), S, 'T1-lit', [], '', '', 'certifiedInput_not_zeroRealizing, under a zero existing in the strip', ''),
    (1810, 'None of this discharges h2.', S, 'T4', [], '', '', 'as said', ''),
    (1810, 'The compiled interface, its function-field', S, 'T4', [], '', '', 'held branch; nothing discharges h2 -- live line only', ''),
    (1812, 'Unconditionally verified', R, 'T2', [E6], E5, '', 'names the product-formula chain "through the conservation certificate" (no kernel holds it) and the perpendicular crossing (about completedRiemannZeta₀): E-5`s kinds -- live line only',
     "Verified at pinned public commits with clean profiles are: the seven-class catalogue's count and its per-class algebra about σ, with Ostrowski's classification of the places of ℚ; the product formula for integers and rationals (ProductFormula_Int.lean, ProductFormula_Rat.lean); the derivative of completedRiemannZeta₀ imaginary on the line; the five checkpoint identifications of σ = 1/2, convergent, not independent; the Mellin factorization and its exhaustion statements; the bracket pair; and the eight coupling discharges at the fixed witness, conjoined in h1_complete_at_Phi."),
    (1814, '**The count.**', R, 'T2', [E4], E4, '', 'listed in E-2026-09-25-4 (deposited :1800)', ''),
    (1823, 'The Lean kernel formalizes three routes', R, 'T2', [E1], E1, 'M-23', 'b532 M-23, listed in E-2026-09-25-1', ''),
    (1823, 'Each route compiles independently', S, 'T2', [], '', '', 'each terminal compiles', ''),
    (1823, 'The manuscripts prove the mathematics', R, 'T2', [E1], E1, 'M-24', 'b532 M-24, listed in E-2026-09-25-1', ''),
    (1825, 'The kernel grows route by route', R, 'T2', [E6], E1, '', 'the route terminals do not converge on the zeros` location: Route 3`s premise is RH restated',
     "The kernel grows route by route, each route terminal compiled separately; they bear on σ = 1/2 as algebra about σ (Route 1), a fact about completedRiemannZeta₀ on the line (Route 2), and an implication from a premise that is RH restated (Route 3)."),
    (1829, 'Part IV establishes one result', S, 'T4', [], '', '', 'as said', ''),
    (1829, 'The derivative-level search (§22.5)', S, 'T2', [], '', '', 'per-class reductions compiled (C₁ derives), the joint step named', ''),
    (1831, 'The derivative-level search reduces', S, 'T2', [], '', '', 'as said', ''),
    (1831, 'The simplicity route is therefore', S, 'T4', [], '', '', 'a second strategy under its own open clause, as said', ''),
    (1843, 'TYPE I problems', S, 'T4', [], '', '', 'stated under the conjecture`s heading', ''),
    (1851, 'Each now has a domain Ostrowski', S, 'T4', [], '', '', 'a manuscript reading', ''),
    (1884, 'The proof is a syllogism', S, 'T4', [], '', '', 'the method`s statement; census note: no compiled INHERITS row about ξ exists for any class (b542) -- a note, not an erratum', ''),
    (1900, 'The seven dimensions match', S, 'T4', [], '', '', 'a manuscript reading', ''),
    (1902, 'The exhaustive catalogue certifying', S, 'T4', [], '', '', 'a manuscript reading', ''),
    (1904, 'What is new is the proof', S, 'T4', [], '', '', 'a manuscript reading', ''),
    (1930, '## Appendix A', S, 'T4', [], '', '', 'a heading', ''),
    (1969, '# Verify zero sorry', S, 'T4', [], '', '', 'no sorry term in Kernel/ or Bridge/ code at v1.5', ''),
    (1971, '# Expected output: empty', R, 'T4', [E6], '', '', 'at v1.5 the grep prints lines from doc comments that mention the word (G-SORRY-GREP counts them)',
     "# Expected output: lines from doc comments that mention the word sorry; no sorry term in the compiled code."),
    (2029, '**Domain Ostrowski**', S, 'T4', [], '', '', 'a definition', ''),
    (2063, '**SIDE**', S, 'T4', [], '', '', 'a definition', ''),
    (2069, '**Specification**', S, 'T4', [], '', '', 'a definition', ''),
    (2088, 'No other values of the valence', S, 'T4', [], '', '', 'a manuscript reading', ''),
    (2179, 'v5.7 (2026-07-16)', H, 'T4', [], '', '', 'the version log, dated', ''),
    (2181, 'v5.8 (2026-07-17)', H, 'T0', [], '', '', 'dated; v0.6.0 = c80bdc2 verified', ''),
    (2181, 'The C₄ discharge is told', H, 'T2', [], '', '', 'dated', ''),
    (2181, 'The "seven coupling discharges"', H, 'T4', [], '', '', 'dated', ''),
    (2181, 'No claim about the open premise changed', H, 'T4', [], '', 'M-26', 'b532 M-26 STANDS; the version log, printed STANDS-AS-HISTORY under (R153)(2)', ''),
    (2183, 'v5.9 (2026-07-19)', H, 'T2', [], '', '', 'dated; v0.7.0 = 2d86182, v0.8.0 = 6efa9e5, v0.9.0 = e3d08b6 verified', ''),
    (2183, 'No fundamental changed', H, 'T4', [], '', '', 'dated', ''),
    (2185, 'Profiles in the §25.8 concordance', H, 'T4', [], '', '', 'dated', ''),
    (2185, 'Filed as `ERRATA.md`', H, 'T4', [], '', '', 'dated; E-2026-07-23-1 is in ERRATA', ''),
    (2185, '**(2) Criterion + verified surround sweep:**', H, 'T4', [], '', '', 'dated', ''),
    (2185, '**(3) Kernel-lineage note', H, 'T4', [], '', '', 'dated; v1.4 = f374174 and the five children verified', ''),
    (2189, 'v5.10.1 (2026-07-24', H, 'T2', [], '', '', 'dated; v0.10.0 = 93c27ec verified', ''),
    (2191, 'v5.10.2 (2026-07-24', H, 'T4', [], '', 'M-27', 'b532 M-27 STANDS; the version log, printed STANDS-AS-HISTORY under (R153)(2)', ''),
    (2191, 'The ξ-specific ingredient', H, 'T0', [], '', '', 'dated; vonMangoldt_nonneg and lam_nonneg_of_nonneg resolve (b541)', ''),
    (2193, 'The *registers, compiled* paragraph gains', H, 'T4', [], '', '', 'dated', ''),
    (2193, 'One wording naturalization', H, 'T4', [], '', '', 'dated', ''),
    (2195, 'v5.12 (2026-07-26', H, 'T4', [], '', '', 'dated', ''),
    (2195, 'Evidence-cited to W-TRANSVERSAL', H, 'T4', [], '', '', 'dated', ''),
    (2197, '**R1 §27.3 fifth register:**', H, 'T4', [], '', '', 'dated', ''),
    (2197, '**R3 §25.8-adjacent:**', H, 'T0', [], '', '', 'dated; word-pairing-interface @ c5ef4bc present', ''),
    (2197, '**h2 stays OPEN', H, 'T4', [], '', '', 'dated', ''),
    (2219, 'Four classical theorems certify', S, 'T4', [], '', '', 'the declared default reading', ''),
    (2219, 'This is the proof`s foundation'.replace('`', "'"), S, 'T4', [], '', '', 'the declared default reading', ''),
    (2219, 'The two strategies share', S, 'T4', [], '', '', 'the declared default reading', ''),
    (2219, '**Three compiled routes**', S, 'T2', [], '', '', 'a label; the route terminals compile (as b541 read deposited :123`s label)', ''),
    (2219, 'The Lean 4 kernel formalizes three independent routes', R, 'T2', [E1], E1, 'M-02', 'b532 M-02, listed in E-2026-09-25-1', ''),
    (2219, 'Three routes, three theorems, one conclusion.', R, 'T2', [E6], E1, '', 'the :2219 copy of deposited :123 (E-5 lists the :1607 copy only)',
     "Three route terminals, three theorems -- not one conclusion: Route 3's conclusion is its premise restated (ch_iff_rh)."),
    (2219, '**The one open premise**', S, 'T4', [], '', 'M-03', 'b532 M-03', ''),
    (2219, 'The five registers of the single premise', R, 'T2', [E1, E6], E1, 'M-04',
     'b532 M-04, listed in E-2026-09-25-1 (register 2); beyond b532`s scope, the registers stand at four depths (b538) -- E-6', DEPTHS),
    (2219, 'The SIDE framework', S, 'T4', [], '', '', 'the declared default reading', ''),
    (2219, 'The Lean kernel`s `SIDESystem`'.replace('`s ', "'s "), S, 'T2', [], '', '', 'as compiled -- live line only', ''),
    (2233, '**First**, they verify', R, 'T2', [E6], E914, '', 'Route 1`s per-class exclusion is algebra about σ and names no zero (b542): the list`s items are not shown to produce no off-line zero -- live line only',
     "First, they verify the catalogue's count and, for each class, algebra showing that its stated constraint on a real σ forces σ = 1/2; the step from a zero of ξ to that constraint is not compiled (b542) -- that is Route 1."),
    (2233, '**Second**, they verify', S, 'T0', [], '', '', 'the derivative of completedRiemannZeta₀ on the line (the function named plainly)', ''),
    (2233, '**Third**, they verify', R, 'T2', [E6], E1, '', 'the conservation interface yields RH from a premise that is RH restated -- live line only',
     "Third, they verify that the conservation interface yields RH from a premise that is RH restated (ch_iff_rh) -- Route 3."),
    (2233, 'Three routes, verified independently', R, 'T2', [E6], E1, '', 'the three do not reach one conclusion but under a premise equivalent to RH -- live line only',
     "Three route terminals, verified separately; only under a premise equivalent to RH do they reach one conclusion."),
    (2235, '**What the kernels do not do', S, 'T4', [], '', '', 'as said', ''),
    (2235, 'The monograph names that premise openly', S, 'T4', [], '', '', 'as said', ''),
    (2235, '**The machine checks the reduction', S, 'T1-open', [], '', '', 'h2_sign ↔ RiemannHypothesis compiled', ''),
    (2237, 'THE `h2` REGISTER, VERBATIM', S, 'T1-open', [], '', '', 'the reduction compiled (h2_sign_iff_rh)', ''),
    (2241, '| Route 1 — structural exhaustiveness', R, 'T2', [E6], '', '', 'the terminal and profile stand; the pin cell says v1.7 = 5e668b4, but tag v1.7 is 2957e7d (2026-07-30) and 5e668b4 is a later main commit (2026-08-05)',
     "| Route 1 — structural exhaustiveness, unconditional in Lean | SIDE-kernel — DEPOSIT-PIN v1.5 = 0e5233f; WORKING-HEAD main = 5e668b4 at 2026-08-12 (tag v1.7 = 2957e7d) | structural_exhaustiveness_proved | {propext, Classical.choice, Quot.sound} | COMPILED |"),
    (2242, '| Route 2 — the completed-ζ derivative', S, 'T0', [], '', '', 'as the terminal states', ''),
    (2243, '| Route 3 — RH from the conservation interface', S, 'T2', [], '', '', 'the row states the implication, as b532`s M-16 (its §25.8 twin) was read', ''),
    (2244, '| structural exhaustiveness yields RH', S, 'T2', [], '', '', 'as the terminal states (Integration`s proposition is RH restated, named so at :1562)', ''),
    (2245, '| structural exhaustiveness is equivalent to RH', S, 'T2', [], '', '', 'as the terminal states', ''),
    (2246, '| the formation count', S, 'T2', [], '', '', 'as the terminal states', ''),
    (2247, '| pairwise class exclusion', S, 'T2', [], '', '', 'as the terminal states', ''),
    (2248, '| the register pentagon', S, 'T2', [], '', '', 'structure only, as said; b538 compiled the cross-register relations and found four depths', ''),
    (2249, '| the finite-range positivity certificate', S, 'T1-lit', [], '', '', 'compiled, under its named premises', ''),
    (2250, '### **`h2`, the one open premise**', S, 'T1-open', [], '', '', 'the row that was right: no kernel discharges h2', ''),
    (2260, '*Provenance:', H, 'T4', [], '', '', 'a dated provenance record', ''),
    (2262, '### ERA ANNOTATION (2026-08-14)', H, 'T4', [], '', '', 'a dated era annotation', ''),
    (2264, '**(2)** The `−2` orphan', H, 'T4', [], '', '', 'a dated era annotation', ''),
    (2264, '**(3)** The Day-1 row is repaired', H, 'T4', [], '', '', 'a dated era annotation', ''),
    (2266, '*Provenance:', H, 'T4', [], '', '', 'a dated provenance record', ''),
]
# the navigator`s sentences the needles did not select (READING (1)), graded apart
SUPP = [
    ('Appendix A row 1', '| 1 | s-Darkness of product formula', S, 'T2', [], '', 'the product formula compiled for integers and rationals (ProductFormula_Int.lean, ProductFormula_Rat.lean at v1.5); its s-reading is (∏)^s = 1^s', ''),
    ('Appendix A row 13', '| 13 | GRH for Dirichlet L-functions', R, 'T4', [E6], '', 'GRH does not follow from RH by any theorem the corpus or the literature holds; Chapter 20 carries it under the analogous premise',
     "| 13 | GRH for Dirichlet L-functions | Chapter 21 | Carried by the same method under the analogous premise for L-functions; not a consequence of RH |"),
    ('Appendix A row 15', '| 15 | Seven mechanism classes', S, 'T4', [], '', 'names no terminal; the enumeration is the manuscript`s (b542: the compiled per-class exclusion is algebra about σ)', ''),
    ('Appendix C build line', 'lake build Kernel.Root', S, 'T4', [], '', 'Kernel/Root.lean is a module of the Kernel library at v1.5 (lakefile.lean globs .submodules `Kernel)', ''),
    ('Appendix C axiom grep', 'grep -r "^axiom "', S, 'T4', [], '', 'no line of any .lean file at v1.5 begins "axiom "', ''),
]


def census():
    lr, lsel, lstop = A.census_of(LIVE)
    dr, dsel, dstop = A.census_of(DEP)
    dt = {}
    for r in dsel:
        dt.setdefault(A.nz(r['sentence']), r['line'])
    act2 = lsel[lstop:]
    b532 = {x['id']: x for x in jl('b532_rows.json')['rows']}
    rows, used = [], set()
    for r in act2:
        m = [x for x in GR if x[0] == r['line'] and x[1] in r['sentence']]
        if len(m) != 1:
            sys.exit('### %d TYPED ROWS MEET live :%d %s' % (len(m), r['line'], r['sentence'][:100]))
        ln, nd, grade, tier, errs, subj, carried, reason, rep = m[0]
        used.add((ln, nd))
        if carried and b532.get(carried, {}).get('verdict') not in (grade, 'STANDS' if grade == H else grade):
            sys.exit('### CARRIED %s DISAGREES WITH b532 (%s vs %s)' % (carried, grade, b532.get(carried, {}).get('verdict')))
        rows.append(dict(line=r['line'], dep_line=dt.get(A.nz(r['sentence']), 'LIVE-SOLE'), section=r['section'], hits=r['hits'], sentence=r['sentence'],
                         grade=grade, tier=tier, errata=errs, subject=subj, carried=carried, reason=reason, replacement=rep,
                         vocab_move=(carried and grade == H and b532.get(carried, {}).get('verdict') == 'STANDS')))
    unused = [(x[0], x[1]) for x in GR if (x[0], x[1]) not in used]
    if unused:
        sys.exit('### TYPED ROWS MEETING NO SENTENCE: %s' % unused)
    live = rd(LIVE).split(NL)
    supp = []
    for name, nd, grade, tier, errs, subj, reason, rep in SUPP:
        hits = [i + 1 for i, l in enumerate(live) if nd in l and i + 1 >= 1693]
        if len(hits) != 1:
            sys.exit('### SUPPLEMENTARY %s MEETS %d LINES' % (name, len(hits)))
        supp.append(dict(name=name, line=hits[0], sentence=live[hits[0] - 1].strip(), grade=grade, tier=tier, errata=errs, subject=subj, reason=reason, replacement=rep))
    past = jl('b541_census.json')['past_halt']
    in_rows = [x for x in past if any(A.nz(x['sentence'][:60]) in A.nz(r['sentence']) and r['dep_line'] == x['dep_line'] for r in rows)]
    counts = {k: sum(1 for r in rows if r['grade'] == k) for k in (S, H, R, 'EXCEEDS')}
    by_err = {}
    for r in rows + supp:
        for e in r['errata']:
            by_err[e] = by_err.get(e, 0) + 1
    s273 = [r for r in rows if r['section'] and r['section'].startswith('## 27.3') and r['grade'] == R]
    res = dict(act_two=len(rows), first_line=rows[0]['line'], b541_act_two=jl('b541_census.json')['halt']['act_two_live'], past_halt=len(past),
               past_in_rows=len(in_rows), rows=rows, supplementary=supp, counts=counts, by_erratum=by_err,
               s273=dict(rows=[(r['line'], r['errata']) for r in s273], ids=sorted(set(e for r in s273 for e in r['errata']))),
               tiers={t: sum(1 for r in rows if r['tier'] == t) for t in ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')},
               vocab_moves=[(r['line'], r['carried']) for r in rows if r['vocab_move']])
    put_json('b543_census.json', res)
    print('  act two : %d rows from live :%d (b541 printed %d) ; the past-halt deposited sentences : %d, of them rows here %d'
          % (len(rows), rows[0]['line'], res['b541_act_two'], len(past), len(in_rows)))
    print('  grades %s ; errata %s ; tiers %s' % (counts, by_err, res['tiers']))
    print('  §27.3 RESTS : %s ; ids %s' % (res['s273']['rows'], res['s273']['ids']))
    print('  vocabulary moves (carried STANDS printed STANDS-AS-HISTORY) : %s' % res['vocab_moves'])
    for x in supp:
        print('  SUPPLEMENTARY %-22s :%d %s %s' % (x['name'], x['line'], x['grade'], ','.join(x['errata'])))


# ------------------------------------------------------------------------------ READING (3): the terminals re-read
# (terminal, repo, pin, path, declaration needle, earlier: (bank, vocabulary, value), now value)
TERMS = [
    ('structural_exhaustiveness_proved', 'SIDE-kernel', 'v1.5', 'Bridge/TheBridgeComplete.lean', 'theorem structural_exhaustiveness_proved', ('b539', 'tier', 'T2'), 'T2'),
    ('SpectralCannonFull.spectral_cannon', 'SIDE-kernel', 'v1.5', 'Kernel/SpectralCannonFull.lean', 'theorem spectral_cannon', ('b539', 'tier', 'T0'), 'T0'),
    ('ConservationBridge.riemann_hypothesis', 'SIDE-kernel', 'v1.5', 'Bridge/ConservationBridge.lean', 'theorem riemann_hypothesis', ('b542', 'kind', 'NEITHER (PREM)'), 'NEITHER (PREM)'),
    ('rh_from_structural_exhaustiveness', 'SIDE-kernel', 'v1.5', 'Kernel/Integration.lean', 'theorem rh_from_structural_exhaustiveness', ('b542', 'kind', 'NEITHER (PREM)'), 'NEITHER (PREM)'),
    ('structural_exhaustiveness_iff_rh', 'SIDE-kernel', 'v1.5', 'Kernel/Integration.lean', 'theorem structural_exhaustiveness_iff_rh', ('b542', 'kind', 'NEITHER (PROP)'), 'NEITHER (PROP)'),
    ('SIDEKernel.formation', 'SIDE-kernel', 'v1.5', 'Kernel/Core.lean', 'theorem formation :', ('b539', 'tier', 'T2'), 'T2'),
    ('all_pairs_excluded', 'SIDE-kernel', 'v1.5', 'Bridge/CrossClassExclusion.lean', 'theorem all_pairs_excluded', ('b541', 'tier', 'T2'), 'T2'),
    ('silence_universal', 'SIDE-kernel', 'v1.5', 'Kernel/SilenceTheorem.lean', 'theorem silence_universal', ('b539', 'tier', 'T2'), 'T2'),
    ('h1_complete_at_Phi', 'SIDE-lv-conservation', 'v0.10.0', None, 'theorem h1_complete_at_Phi', ('b540:294', 'tier', 'T0'), 'T0'),
    ('RegisterPentagon', 'SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/RegisterPentagon.lean', 'namespace RegisterPentagon', ('b539', 'tier', 'T2'), 'T2'),
    ('partialPositivity_finiteRange', 'SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/PartialPositivity.lean', 'theorem partialPositivity_finiteRange', ('b540:304', 'tier', 'T1-lit'), 'T1-lit'),
    ('certifiedInput_not_zeroRealizing', 'SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/RegisterPentagon.lean', 'theorem certifiedInput_not_zeroRealizing', ('b542', 'kind', 'NEITHER (ANAL)'), 'NEITHER (ANAL)'),
    ('lowFinset_mem_iff', 'SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/PartialPositivity.lean', 'lemma lowFinset_mem_iff', ('b542', 'kind', 'NEITHER (DEFEQ)'), 'NEITHER (DEFEQ)'),
    ('register5_output_holds', 'SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/RegisterDepth.lean', 'theorem register5_output_holds', ('b542', 'kind', 'NEITHER (ANAL)'), 'NEITHER (ANAL)'),
    ('h2_sign_iff_rh', 'SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/Seam.lean', 'theorem h2_sign_iff_rh', ('b542', 'kind', 'NEITHER (PROP)'), 'NEITHER (PROP)'),
]


def earlier_in_bank(bank, name, vocab, value):
    """### the earlier grade, read FROM its bank -- not from this file"""
    if bank == 'b539':
        d = jl('b539_tiers.json')
        return any(r.get('terminal', '').split('.')[-1] == name.split('.')[-1] and r.get('tier') == value for r in d['ranked'] + d['extra'])
    if bank.startswith('b540:'):
        row = int(bank.split(':')[1])
        return any(r.get('line') == row and r.get('tier') == value for r in jl('b540_tiers.json')['corr'])
    if bank == 'b541':
        return any(name in r['sentence'] and r['tier'] == value for r in jl('b541_census.json')['rows'])
    if bank == 'b542':
        return any(r.get('name', '').split('.')[-1] == name.split('.')[-1] and '%s (%s)' % (r['kind'], r['reason']) == value for r in jl('b542_census.json')['rows'])
    return False


def terms():
    out = []
    for name, repo, pin, path, needle, (bank, vocab, value), now in TERMS:
        files = [path] if path else [f for f in g(repo, 'ls-tree', '-r', '--name-only', pin).split(NL) if f.endswith('.lean')]
        found = None
        for f in files:
            t = g(repo, 'show', '%s:%s' % (pin, f)).replace(chr(13), '').split(NL)
            i = next((k for k, l in enumerate(t) if l.strip().startswith(needle)), None)
            if i is not None:
                j = i
                while j < len(t) - 1 and ':=' not in t[j] and j - i < 12:
                    j += 1
                found = dict(file=f, line=i + 1, statement=NL.join(t[i:j + 1]))
                break
        verified = earlier_in_bank(bank, name, vocab, value)
        out.append(dict(terminal=name, repo=repo, pin=pin, sha=g(repo, 'rev-parse', '--short', pin + '^{commit}').strip(), found=found, earlier=dict(bank=bank, vocab=vocab, value=value),
                        earlier_in_bank=verified, now=now, word=('CARRIED' if now == value else 'MOVED')))
    put_json('b543_terms.json', dict(terms=out))
    for x in out:
        print('  %-8s %-40s %s %s %s:%s  earlier %s %s %s (in its bank %s) ; now %s' % (
            x['word'], x['terminal'], x['repo'], x['sha'], x['found']['file'] if x['found'] else 'NOT FOUND', x['found']['line'] if x['found'] else '',
            x['earlier']['bank'], x['earlier']['vocab'], x['earlier']['value'], x['earlier_in_bank'], x['now']))


# ------------------------------------------------------------------------------ COMPONENT 3
def erratum6():
    cj = jl('b543_census.json')
    rows = [r for r in cj['rows'] if E6 in r['errata']] + [dict(r, dep_line='(the table)', section=r['name']) for r in cj['supplementary'] if E6 in r['errata']]
    L = ['## E-2026-09-25-6 — The deposited monograph, read against the RH-anchor from Chapter 26 to its end: sentences that gather the '
         'registers as one premise, read the compiled faces past what they state, or count Route 3 as a route; a pin cell and a build '
         'instruction that do not match their objects (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2) — DRAFT, NOT FILED', '',
         '**Drafted 2026-09-25 (b543), on the author\'s ruling (R153)(7) and (R151)(4)-(5), from the census banked at b543 (relay '
         'data/b543_census.json), the monograph read\'s second act (the heading "## 26.1 The Axiom Journey" to the file\'s end); a further '
         'entry beside E-2026-09-25-1, -4 and -5, extending them without editing them. TO BE FILED only on the author\'s word.',
         '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
         '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**', '',
         '**Affected.** *A Place to Stand*, Zenodo version v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — the '
         'monograph as deposited (PLACE-papers outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md, md5 e90e2d06d5cadc059c62c29a849e9f8c); the live '
         'line day1/A_Place_to_Stand.md v5.13 carries the same sentences where a live line is given; a row marked LIVE-SOLE is the live line\'s '
         'only, corpus-facing, listed so that the live line is corrected with the deposit.', '',
         '**What the kernels say, in their own words.** SIDE-explicit-formula, read fresh at b543: ch_iff_rh : conservationHypothesis ↔ '
         'RiemannHypothesis; h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis; not_register1 : ¬Register1_universalityHypothesis; '
         'register5_output_holds : Register5_output_HilbertPolya. SIDE-kernel v1.5: the per-class exclusions are algebra about a real σ '
         '(TheBridgeComplete.lean:157-196), and no compiled statement takes a zero of ξ to a class\'s constraint (the inheritance census, '
         'b542). SIDE-kernel\'s tag v1.7 is 2957e7d.', '',
         '**The sentences, each with its replacement:**', '']
    for r in rows:
        where = ('A_Place_to_Stand.md:%s at v1.1.2' % r['dep_line']) if r['dep_line'] not in ('LIVE-SOLE', '(the table)') else (
            'LIVE-SOLE, not in the deposit (corpus-facing)' if r['dep_line'] == 'LIVE-SOLE' else 'Appendix A at v1.1.2')
        L += ['- **%s, live :%s** (%s): *"%s"*' % (where, r['line'], r['section'] or '', r['sentence'].replace('`', '').replace('*', '')),
              '  - reads **RESTS** — %s%s.' % (re.sub(r"(?<=[A-Za-z0-9])`s\b", "'s", r['reason']).replace('`', ''),
                                               ('; under %s\'s subject' % r['subject']) if r['subject'] else ''),
              '  - replacement: *"%s"*' % r['replacement'].replace('`', '')]
    L += ['', '**What is not corrected.** Every STANDS and STANDS-AS-HISTORY row of the census; the version log and the era annotations, '
              'read as records of their dates under (R153)(2); the rows the filed errata already list (E-1: M-02, M-04 in part, M-18, M-20, '
              'M-23, M-24; E-4: its four §27.3 lines).', '',
          '**Status.** DRAFT. Not filed. Retained at monograph v1.1.2. The filing is the author\'s word.', '']
    txt = NL.join(L)
    io.open(os.path.join(D, 'b543_erratum_draft.md'), 'w', encoding='utf-8', newline=NL).write(txt)
    put_json('b543_erratum6.json', dict(rows=len(rows), backticks=txt.count('`'), backticks_outside_code=outside_bt(txt)))
    print('  E-2026-09-25-6 draft : %d rows ; backticks %d' % (len(rows), txt.count('`')))


# ------------------------------------------------------------------------------ COMPONENT 4-5
SPANS = [('Chapter 26', 1693, 1742, 'what compiles and what does not: the axiom journey as a dated record', 'T2'),
         ('PART VI', 1732, 1742, 'the programme', 'T4'),
         ('Chapter 27', 1743, 1817, 'the research path: the premise in five registers, the bracket, the compiled registers (§27.3)', 'T1-open'),
         ('Chapter 28', 1818, 1889, 'extensions: the route terminals (§28.1), the simplicity clause, the E-Difficulty conjecture, the syllogism', 'T2'),
         ('Chapter 29', 1890, 1927, 'the sieve and the exclusion: the circle closed in manuscript', 'T4'),
         ('Appendix A', 1930, 1949, 'the theorem catalogue', 'T4'), ('Appendix B', 1950, 1958, 'formation counts', 'T4'),
         ('Appendix C', 1959, 1982, 'build instructions', 'T4'), ('Appendix D', 1983, 2014, 'computational verification', 'T3'),
         ('Appendix E', 2015, 2076, 'glossary', 'T4'), ('Appendix F', 2077, 2089, 'the valence dichotomy', 'T4'),
         ('Appendix G', 2090, 2208, 'bibliography and the version log, records of their dates', 'T4'),
         ('Appendix H', 2209, 2228, 'how the monograph is organized, with the deposited front matter`s sentences', 'T2'),
         ('Correspondence', 2229, 10 ** 6, 'the back-matter table: route terminals and the h2 row, NONE', 'T1-open')]
GRADES = (S, H, R, 'EXCEEDS')


def span_of(line):
    best = None
    for name, a, b, _, _ in SPANS:
        if a <= line <= b and (best is None or (b - a) < (best[2] - best[1])):
            best = (name, a, b)
    return best[0] if best else None


def map_():
    cj, tj = jl('b543_census.json'), jl('b543_terms.json')
    per = {}
    for r in cj['rows']:
        per.setdefault(span_of(r['line']), []).append(r)
    TI = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
    c = cj['counts']
    moved = [x['terminal'] for x in tj['terms'] if x['word'] == 'MOVED']
    L = ['', FTITLE, '',
         '*Filed at b543 on the author`s ruling `(R153)`(7): the second act of the read `(R151)`(4)-(5), under the voice of (R153)(2) and the '
         'posture of (R153)(3). The sentences after the heading "## 26.1 The Axiom Journey" (A_Place_to_Stand.md:1698), read against the '
         'RH-anchor; the deposited front-matter sentences whose live copy is the paragraph at :2219 are rows of it. Bank: relay '
         '`data/b543_census.json`. Nothing in the monograph is edited.*', '',
         '**The census.** %d rows: STANDS %d · STANDS-AS-HISTORY %d · RESTS %d · EXCEEDS %d; RESTS by erratum %s. Supplementary rows the '
         'navigator named outside the selection of the needles: %d, printed in the bank. The terminals re-read at their pins: %d, CARRIED %d, MOVED %d.'
         % (cj['act_two'], c[S], c[H], c[R], c['EXCEEDS'], cj['by_erratum'], len(cj['supplementary']), len(tj['terms']),
            len(tj['terms']) - len(moved), len(moved)), '',
         '| part | load-bearing claim | tier | rows | ' + ' | '.join(TI) + ' | STANDS | AS-HISTORY | RESTS (errata) |',
         '|:--|:--|:--|--:|' + '--:|' * len(TI) + '--:|--:|:--|']
    for name, a, b, claim, tier in SPANS:
        rs = per.get(name, [])
        rests = [r for r in rs if r['grade'] == R]
        errs = sorted(set(e for r in rests for e in r['errata']))
        L.append('| %s | %s | **%s** | %d | %s | %d | %d | %d %s |' % (name, claim, tier, len(rs), ' | '.join(str(sum(1 for r in rs if r['tier'] == t)) for t in TI),
                                                                  sum(1 for r in rs if r['grade'] == S), sum(1 for r in rs if r['grade'] == H), len(rests),
                                                                  ('(' + ', '.join(errs) + ')') if errs else ''))
    L += ['',
          '**What the monograph`s compiled content is about, read whole.** Its compiled content falls into four kinds. The criterion: '
          '`h2_sign` is equivalent to Mathlib`s RiemannHypothesis (`h2_sign_iff_rh`), and the conservation premise of Route 3 is RH '
          'restated (`ch_iff_rh`). The symmetries: the functional-equation reflection of the zeros (Zeta23`s `zeta_reflect_zero`, about '
          'zeta) and the imaginary derivative of `completedRiemannZeta₀` on the line (`spectral_cannon`). The programme`s own types: the '
          'seven-class catalogue, its count and its per-class algebra about a real σ, the formation count, the register pentagon. And '
          'facts about zeta that do not touch location: the zero-free half-plane, the countability of the zeros, the finite windows, the '
          'coupling discharges at the fixed witness. What the proof rests on is one Prop, `h2_sign`, which is equivalent to RH and which '
          'no kernel discharges; the back-matter row that says so, NONE, is the row that was right. What the history records -- the '
          'axiom journey, the research arc, the version log, the era annotations -- is read as records of their dates, and they stand as '
          'such; where a dated sentence named ξ for `completedRiemannZeta₀`, it rests with E-5`s kind.', '',
          '**CP-1, the monograph part, closed.** The monograph *A Place to Stand* is read whole against the RH-anchor at b541 and b543; the '
          'errata it produced are E-2026-09-25-4 (filed at b541), E-2026-09-25-5 (filed at b542) and E-2026-09-25-6 (drafted at b543, NOT '
          'FILED); the Phase 1.2 presentations and the six companion papers remain unread until mirrored.', '',
          '**A correction to b542, carried here.** b542`s closing said the name at FINDINGS.md:1109 is one only TECHNE-Core holds. It is '
          'not: SIDE-kernel declares it at tags v1.0 and v1.1 (MetaKernel.lean:138), and other PLACE-papers files and earlier relay banks '
          'cite it; b542`s check read each repository at its census pin only. The note (R153)(5) orders is therefore held, nothing is '
          'written at :1109, and the author`s word is asked.', '']
    w = append_to(FIND, NL.join(L))
    w['heading_line'] = rd(FIND).split(NL).index(FTITLE) + 1
    put_json('b543_map.json', w)
    print('  FINDINGS : %(added)d bytes added, prefix %(prefix)s ; entry at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ components, desk, trail
def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


PRIOR_PP = '13c186a'
FILES = ['FINDINGS.md', 'OPEN_TRAILS.md']


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    cj, tj = jl('b543_census.json'), jl('b543_terms.json')
    rows = cj.get('rows', [])
    find = lambda ln, nd: next((r for r in rows if r['line'] == ln and nd in r['sentence']), {})
    s273 = cj.get('s273', {})
    new = [e for e in s273.get('ids', []) if e == E6]
    hist = [r for r in rows if r['grade'] == H]
    mono = {f: gitc(PP, 'hash-object', f) == gitc(PP, 'rev-parse', '%s:%s' % (PRIOR_PP, f)) for f in ('day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')}
    mono['deposited md5'] = md5(DEP) == 'e90e2d06d5cadc059c62c29a849e9f8c'
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b543_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b543_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == '' for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section')}
    return dict(
        n1=len(s273.get('rows', [])) >= 3 and len(s273.get('ids', [])) >= 2 and bool(new), n1_detail=s273,
        n2=find(2250, 'the one open premise').get('grade') == S and find(1808, 'The obligation h2 is').get('grade') == S,
        n3=len(hist) >= 20 and not [r for r in hist if r['errata']], n3_count=len(hist),
        n4=bool(tj.get('terms')) and all(x['word'] in ('CARRIED', 'MOVED') and x['found'] and x['earlier_in_bank'] for x in tj['terms'])
        and sum(1 for x in tj['terms'] if x['word'] == 'MOVED') <= 2, n4_moved=[x['terminal'] for x in tj.get('terms', []) if x['word'] == 'MOVED'],
        n5=bool(rows) and not [r for r in rows + cj.get('supplementary', []) if r['grade'] == 'EXCEEDS'],
        n6=all(mono.values()) and blob(PP, '%s:ERRATA.md' % PRIOR_PP) == open(ERR, 'rb').read() and not zen and tok == 0 and all(kernels.values()),
        mono=mono, zen=zen, token=tok, kernels=kernels,
        s1=find(1808, 'The premise is RH-equivalent').get('errata') == [E4],
        s2=find(2243, 'Route 3').get('grade') == S,
        s3=find(1971, 'Expected output').get('grade') == R)


def components():
    cj, tj = jl('b543_census.json'), jl('b543_terms.json')
    L = ['=' * 132, 'b543 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE ANCHOR :'] + ['  ' + l for l in rd(os.path.join(D, 'b543_anchor.txt')).rstrip(NL).split(NL)]
    L += ['', '### COMPONENT 1 -- (a) FINDINGS.md:1109 : HELD (READING (5)) ; (b) the branches : see data/b543_branches.txt',
          '', '### COMPONENT 2 -- THE CENSUS : %d rows from live :%d ; counts %s ; errata %s ; tiers %s' % (cj['act_two'], cj['first_line'], cj['counts'], cj['by_erratum'], cj['tiers']),
          '  §27.3 : %s' % cj['s273'], '  vocabulary moves : %s' % cj['vocab_moves']]
    L += ['  %-5s %-11s %-18s %-7s %-40s %s' % (r['line'], r['dep_line'], r['grade'], r['tier'], ','.join(r['errata']) or '-', r['sentence'][:100]) for r in cj['rows']]
    L += ['  SUPPLEMENTARY :'] + ['  %-22s :%d %s %s %s' % (x['name'], x['line'], x['grade'], ','.join(x['errata']) or '-', x['reason']) for x in cj['supplementary']]
    L += ['', '### THE TERMINALS RE-READ :'] + ['  %-8s %s at %s %s:%s -- earlier %s ; now %s' % (x['word'], x['terminal'], x['sha'], x['found']['file'] if x['found'] else '-',
                                                                                              x['found']['line'] if x['found'] else '-', x['earlier'], x['now']) for x in tj['terms']]
    L += ['', '### COMPONENT 3 -- E-2026-09-25-6 : ' + json.dumps(jl('b543_erratum6.json')), '### COMPONENT 4-5 -- FINDINGS : ' + json.dumps(jl('b543_map.json')), '=' * 132]
    io.open(os.path.join(D, 'b543_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:6]))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b543 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- §27.3`s RESTS rows and ids : %s.' % (w(sc['n1']), sc['n1_detail']),
         '  **(N2)** ### **%s.** -- the back-matter h2 row and the Weil-positivity sentence.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- STANDS-AS-HISTORY rows : %d ; drawing an erratum : none.' % (w(sc['n3']), sc['n3_count']),
         '  **(N4)** ### **%s.** -- MOVED : %s.' % (w(sc['n4']), sc['n4_moved'] or 'none'),
         '  **(N5)** ### **%s.** -- EXCEEDS rows : none.' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- monograph %s ; ERRATA untouched ; tools naming the platform %s ; token hits %s ; kernels clean %s.'
         % (w(sc['n6']), sc['mono'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- "The premise is RH-equivalent ..." reads RESTS on E-4.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- the back-matter Route 3 row reads STANDS.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- Appendix C`s "Expected output: empty" reads RESTS.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THE NAVIGATOR`S READINGS, ROW BY ROW (refutable readings from the ferry, against the census):'] + [
         '  %s' % l for l in reading_checks()] + [
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b543_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b543_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b543_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b543_scores.json', sc)
    print(NL.join(L))


def reading_checks():
    cj = jl('b543_census.json')
    rows = cj['rows']
    f = lambda ln, nd: next((r for r in rows + cj['supplementary'] if r['line'] == ln and nd in r['sentence']), None)
    checks = [('§26.1 axiom-journey sentences STANDS-AS-HISTORY', [f(1708, 'The last axiom'), f(1708, 'continuation')], H),
              ('§27.2 "The Lean kernel ... compiles the three route terminals" RESTS E-1 (Route 3)', [f(1779, 'The Lean kernel')], R),
              ('§27.3 "positivity of the Weil functional" STANDS', [f(1808, 'The obligation h2 is')], S),
              ('§27.3 "The premise is RH-equivalent ..." STANDS', [f(1808, 'The premise is RH-equivalent')], S),
              ('§27.3 "What remains, exactly" RESTS E-4 or E-6', [f(1808, 'What remains, exactly')], R),
              ('§27.3 the register pentagon STANDS-AS-HISTORY', [f(1810, 'SIDE-lv-conservation now carries')], H),
              ('§28.1 three routes RESTS E-1', [f(1823, 'The Lean kernel formalizes three routes')], R),
              ('§28.6 syllogism STANDS', [f(1884, 'The proof is a syllogism')], S),
              ('Appendix A row 1 STANDS', [f(1934, 's-Darkness')], S),
              ('Appendix A row 13 RESTS (same erratum as its Part III premise)', [f(1946, 'GRH for Dirichlet')], R),
              ('Appendix C axiom grep STANDS', [f(1977, '^axiom')], S),
              ('back matter h2 NONE row STANDS', [f(2250, 'the one open premise')], S),
              ('back matter Route 3 row RESTS E-1', [f(2243, 'Route 3')], R),
              ('back matter register pentagon row STANDS', [f(2248, 'register pentagon')], S)]
    out = []
    for label, rs, want in checks:
        got = [r['grade'] + (('/' + ','.join(r['errata'])) if r['errata'] else '') if r else 'NOT IN THE POPULATION' for r in rs]
        ok = all(r and r['grade'] == want for r in rs)
        out.append('%-72s -> %s : %s' % (label, got, 'AS READ' if ok else 'NOT AS READ'))
    return out


def trail():
    sc, cj, tj = scores(), jl('b543_census.json'), jl('b543_terms.json')
    c = cj['counts']
    body = ['', HEADING, '',
            '**(R153) ratified.** (1) The editorial phase. (2) The descriptive voice; STANDS-AS-HISTORY for records of their dates. (3) Earlier '
            'grades re-read before they are carried. (4) The checkpoints CP-1 to CP-8; the act after takes CP-2 and CP-3. (5) FINDINGS.md:1109 -- '
            'HELD: the note would be false (the declaration is public in SIDE-kernel v1.0-v1.1 and cited elsewhere); the author`s word asked. (6) The '
            'two push branches deleted by name. (7) The read`s second act, run here.', '',
            '**The census, act two:** %d rows from live :%d -- STANDS %d · STANDS-AS-HISTORY %d · RESTS %d · EXCEEDS %d; RESTS by erratum %s. '
            '%d terminals re-read at their pins: %s MOVED. **E-2026-09-25-6 DRAFTED, NOT FILED** (relay `data/b543_erratum_draft.md`). The '
            'map`s second half at `FINDINGS.md`:%s.' % (cj['act_two'], cj['first_line'], c[S], c[H], c[R], c['EXCEEDS'], cj['by_erratum'], len(tj['terms']),
                                                     sum(1 for x in tj['terms'] if x['word'] == 'MOVED'), jl('b543_map.json').get('heading_line')), '',
            '**CP-1, the monograph part, closed:** the monograph is read whole against the RH-anchor (b541, b543); its errata E-2026-09-25-4, '
            '-5 (filed) and -6 (drafted); the Phase 1.2 presentations and the six companion papers remain unread until mirrored.', '',
            '**Next:** CP-2 and CP-3 together, from b542`s enumeration; then BALANCE_AND_POSITIVITY.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; no monograph byte changed; '
            'ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is '
            'a statement about RH.', '']
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b543_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'reads': reads, 'anchor': anchor, 'census': census, 'terms': terms, 'erratum6': erratum6, 'map': map_,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
