# -*- coding: utf-8 -*-
"""b531_record.py -- COMPONENTS 2-4, THE DESK AND THE TRAIL. ### `python tools/b531_record.py components | desk | trail`
### The premise and terminal are READ from `b531_read.json` (printed by b531_read.py from SIDE-kernel); the statability
### forms from the banked probe `b531_probe.txt`; the scores are READING (7)'s.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


RD = json.loads(read('b531_read.json') or '{}')
PROBE = read('b531_probe.txt')
w = lambda v: 'HELD' if v else 'REFUTED'
GRADE = 'ENCODES-CONCLUSION'
RELATION = 'EQUIVALENT'


def dcl(name):
    return next((d for d in RD.get('decls', []) if d['name'] == name), {})


def probe_errors_at(lines):
    """### the probe's error lines that point at the given source lines of Probe.lean."""
    errs = re.findall(r'Probe\.lean:(\d+):\d+: error', PROBE)
    return [int(e) for e in errs if int(e) in lines]


def example_lines():
    src = PROBE.split('### output')[0]
    ls = src.split(NL)[1:]
    return [i + 1 for i, l in enumerate(ls) if l.startswith('example : Prop')]


def scores():
    ex = example_lines()
    span = set()
    for s in ex:
        span |= set(range(s, s + 4))
    statable = len(ex) == 2 and not probe_errors_at(span)
    prem = ['Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean']
    return dict(example_lines=ex, statable=statable,
                n1=not statable, n2=RELATION != 'EQUIVALENT', n3=GRADE == 'INTERFACES',
                s1=all(RD.get('files_identical', {}).get(f) for f in prem),
                s2=bool(RD.get('riemann_hypothesis_std3_banked')),
                s3=dcl('riemann_hypothesis').get('lines', 99) <= 3)


SKETCH_FWD = [
    '(1) ConservationHypothesis: every sigma that is the real part of a nontrivial zeta zero has a prime p with p^(-sigma) = p^(-(1 - sigma)).',
    '(2) balance_theorem (compiled, Voice1): that equation holds iff sigma = 1/2 -- so every such sigma is 1/2.',
    '(3) rh_from_structural_exhaustiveness / rh_implies_mathlib_rh (compiled): hence Mathlib`s RiemannHypothesis.',
    '(4) rh_imp_h2_sign (compiled at b513, SIDE-explicit-formula): RiemannHypothesis -> h2_sign.',
    '(5) So ConservationHypothesis -> h2_sign; the only cost is that (1)-(3) live in SIDE-kernel and (4) in the other kernel.']
SKETCH_BWD = [
    '(1) h2_sign: 0 <= poleTerm k - primeSum k + archTerm k for every k in classK.',
    '(2) h2_sign -> RH is Weil`s criterion (Weil 1952): positivity over every k = h * h~ with h C^2 compactly supported',
    '    contains the smooth class of the published criterion -- NAMED AT CITE, NOT PINNED; in the kernel it is b513`s',
    '    unproved Prop `h2_sign_imp_rh`, compiled only to f4 (b524-b530).',
    '(3) RH -> StructuralExhaustiveness (compiled, `structural_exhaustiveness_from_rh`): every such sigma is 1/2.',
    '(4) balance_theorem at p = 2 (compiled, `.mpr`): the balance equation holds at the prime 2.',
    '(5) So h2_sign -> ConservationHypothesis, with its first step exactly the open f4.']
STRENGTH = ('ConservationHypothesis carries the whole of RH`s strength: a ten-line lemma about p^(-sigma) turns it into '
            'RH and a two-line composition turns RH back into it, so it is RH restated at the multiplicative place -- a proof '
            'of it would be a proof of RH and nothing lighter.')


def components():
    sc = scores()
    L = ['=' * 132, 'b531 -- COMPONENTS 2-4, AS READ.', '=' * 132, '',
         '### COMPONENT 1: `b531_premise.txt` (printed by b531_read.py from SIDE-kernel at 0e5233f and HEAD).',
         '  ConservationHypothesis, from its declaration line to its := :', '  ' + (dcl('ConservationHypothesis').get('head') or ''),
         '  whole:', NL.join('    ' + l for l in (dcl('ConservationHypothesis').get('whole') or '').split(NL)),
         '  the terminal, whole (%d lines):' % dcl('riemann_hypothesis').get('lines', 0),
         NL.join('    ' + l for l in (dcl('riemann_hypothesis').get('whole') or '').split(NL)),
         '  the banked profile (v1.2, before W-7): %s' % (RD.get('banked_profiles') or ['NONE'])[0],
         '', '### COMPONENT 2 -- STATABILITY: %s. The two forms, elaborated as Props by the banked pre-seal probe (b531_probe.txt, '
         'example lines %s, errors at those lines: %s):' % ('STATABLE' if sc['statable'] else 'NOT STATABLE', sc['example_lines'],
                                                           probe_errors_at(set(range(1, 200)) & set(sum([list(range(s, s + 4)) for s in sc['example_lines']], [])))),
         '  (i) VERBATIM: FORALL sigma, (EXISTS t, riemannZeta <sigma, t> = 0 AND NOT (EXISTS n, <sigma, t> = -2 (n + 1)) AND <sigma, t> ≠ 1)',
         '      -> EXISTS p, Nat.Prime p AND (p : R)^(-sigma) = (p : R)^(-(1 - sigma))',
         '  (ii) OVER THE ZERO CONFIGURATION: FORALL rho in zetaZeroConfig.carrier, EXISTS p, Nat.Prime p AND (p : R)^(-Re rho) = (p : R)^(-(1 - Re rho))',
         '  ### no new definition: Mathlib`s riemannZeta, Nat.Prime, Real.rpow, and the kernel`s zetaZeroConfig. ### (ii)`s zero',
         '  ### predicate IsNontrivialZero (zeta = 0, 0 < Re < 1) is definitionally different from is_xi_zero (zeta = 0, not trivial,',
         '  ### not 1). ### Not through zeroSide, primeSum, archTerm, poleTerm or classK: the equation is at a real part, not through',
         '  ### a test function; the nearest channel object is primeSum`s weight Lambda(n) / sqrt n.',
         '  ### b512 CORRECTED at relay/data/b512_components.txt:132-134 (R2 NOT STATABLE, a search for NAMES, not the statement).',
         '', '### COMPONENT 3.',
         '  (a) THE GRADE of `ConservationBridge.riemann_hypothesis` against "h2_sign -> RH": %s.' % GRADE,
         '      deciding: the premise`s unfolding (above) with the compiled `balance_theorem`:',
         NL.join('        ' + l for l in (dcl('balance_theorem').get('head') or '').split(NL)),
         '      -- the premise states sigma = 1/2 of every such sigma, i.e. RH as stated; the terminal takes its conclusion as',
         '      its premise, restated, and never mentions h2_sign. The earlier grades (DERIVES against "R2 implies RH",',
         '      FACES_LEDGER.md:17; INTERFACES against RH, OPEN_TRAILS.md:5523) are relations to other claims, left as they stand.',
         '  (b) THE RELATION: %s as propositions (each equivalent to RH); in the corpus`s holdings ConservationHypothesis =>' % RELATION,
         '      h2_sign derivable now, h2_sign => ConservationHypothesis open exactly at f4.',
         '      ConservationHypothesis => h2_sign:'] + ['        ' + s for s in SKETCH_FWD] + [
         '      h2_sign => ConservationHypothesis:'] + ['        ' + s for s in SKETCH_BWD] + [
         '  (c) YES. ' + STRENGTH,
         '', '### COMPONENT 4 -- THE BRIDGE PRICED.',
         '  ConservationHypothesis => h2_sign : COMPILABLE-NOW in SIDE-explicit-formula -- restate form (i); port balance_theorem',
         '      (Real.rpow_lt_rpow_left_iff, Nat.Prime.one_lt: FOUND by the probe; Real.rpow_right_injective ABSENT at this pin);',
         '      port rh_implies_mathlib_rh (Complex.eta FOUND); compose with rh_imp_h2_sign (FOUND, RHChain.lean:24, std3 at b513).',
         '  h2_sign => ConservationHypothesis : STATABLE-NOT-COMPILED -- ABSENT: `h2_sign_imp_rh` (RHChain.lean:83, a Prop; the',
         '      Weil converse, f4); the remaining RH => ConservationHypothesis COMPILABLE-NOW by the same ports.',
         '  the kernel : SIDE-explicit-formula (holds h2_sign and RiemannHypothesis).',
         '  the pin divergence, a cost : SIDE-kernel Lean v4.29.0-rc8 / Mathlib e960b84 ; SIDE-explicit-formula v4.33.0-rc2 /',
         '      Mathlib 51e6992. No import across; the premise RESTATED, its identity with the deposited one a statement-read,',
         '      every ported name probed again at the newer pin.',
         '=' * 132]
    io.open(os.path.join(D, 'b531_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:30]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b531 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- both statement forms elaborate in the banked probe, no error at their lines : %s ; no new definition.'
         % (w(sc['n1']), sc['statable']),
         '  **(N2)** ### **%s.** -- the relation read : %s (as propositions; in the corpus, one direction open at f4).' % (w(sc['n2']), RELATION),
         '  **(N3)** ### **%s.** -- the grade against "h2_sign -> RH" : %s.' % (w(sc['n3']), GRADE),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- ConservationBridge, XiDef, Voice1 identical pin to HEAD : %s.'
         % (w(sc['s1']), [RD.get('files_identical', {}).get(f) for f in ('Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean')]),
         '  **(S2)** ### **%s.** -- the banked profile, whole string, standard three : %s (banked at v1.2).' % (w(sc['s2']), RD.get('riemann_hypothesis_std3_banked')),
         '  **(S3)** ### **%s.** -- the terminal`s lines from its declaration line : %s.' % (w(sc['s3']), dcl('riemann_hypothesis').get('lines')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b531_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b531_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b531_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b531 — the bridge read: ConservationHypothesis against h2_sign; (R141) entered'


def trail():
    sc = scores()
    body = [
        '', HEADING, '',
        '**(R141) ratified.** (1) b530 is entered; the author grades `rest_bound_closed` and `rest_bound_zeta` DERIVES of',
        'their model statements, the second hypothesis-free for zeta and saying nothing of real parts beyond the strip; f4\'s',
        'obstruction is a theorem (`not_f4_needs`); the seat\'s departures stand. (2) **The converse is paused at its named',
        'obstruction, not abandoned.** W-ORD-WEIL-CONVERSE stays open at f4 with (A) and (B); the status the corpus may state is:',
        '"RH → h2_sign compiled; h2_sign → RH compiled to its last step, which is the uniformity over zeros of largest real part,',
        'exhibited as an inequality and open." The seat\'s pre-seal `#check` probes are standing practice for every kernel act.',
        '(3) The kernel lane turns to W-ORD-H2-BRIDGE, the head of K1, read before it is built. (4) The lane opened for this',
        'act and shuts at its close.',
        '',
        '**COMPONENT 1 — the deposited premise, printed** from SIDE-kernel at v1.5 = `0e5233f` and at HEAD `0256e9e`, the',
        'premise\'s files byte-identical at both (`relay/data/b531_premise.txt`):',
        '',
        '```lean',
        dcl('ConservationHypothesis').get('whole') or '',
        '',
        dcl('riemann_hypothesis').get('whole') or '',
        '```',
        '',
        '`is_xi_zero σ` unfolds to "some t with riemannZeta ⟨σ, t⟩ = 0, ⟨σ, t⟩ not a trivial zero and ≠ 1"; `prime_as_real p hp`',
        'is `(p : ℝ)`. The terminal\'s proof is %d lines; it uses `rh_from_structural_exhaustiveness`,' % dcl('riemann_hypothesis').get('lines', 0),
        '`structural_exhaustiveness_proved`, `conservation_activates_balance` and `balance_theorem`. Its profile is read from the',
        'kernel\'s banked output only (`DEPOSIT_v1_2_NOTES.md`, at v1.2, before W-7): the standard three on the whole string.',
        'A profile at v1.5 is not printed: the closure changed after v1.5 (Voice7) and a pin print needs a checkout and a build.',
        '',
        '**COMPONENT 2 — STATABLE, with no new definition.** The premise elaborates as a Prop in SIDE-explicit-formula from',
        'Mathlib\'s `riemannZeta`, `Nat.Prime` and `Real.rpow` alone — verbatim, and over `zetaZeroConfig.carrier` (whose',
        'predicate `IsNontrivialZero` differs by definition from `is_xi_zero`) — by the banked pre-seal probe',
        '(`relay/data/b531_probe.txt`). No channel object carries it: the balance is an equation at a real part, not a test',
        'function. **b512\'s reading is corrected at its address** (`relay/data/b512_components.txt:132-134`, R2 NOT',
        'STATABLE): b512 searched for the names, not for the statement.',
        '',
        '**COMPONENT 3.** (a) `ConservationBridge.riemann_hypothesis` against "h2_sign → RH": **ENCODES-CONCLUSION**. The',
        'compiled `balance_theorem` — `p ^ (−s) = p ^ (−(1 − s)) ↔ s = 1 / 2` at every prime — makes the premise say of every',
        'real part of a nontrivial zero that it is ½, which is RH as stated: the terminal takes its conclusion as its premise,',
        'restated, and never mentions h2_sign. The earlier grades of the same terminal against other claims — DERIVES against',
        '"R2 implies RH" (`FACES_LEDGER.md:17`), INTERFACES against RH (`OPEN_TRAILS.md:5523`) — stand as written; row R2\'s',
        '"the converse is not compiled" is reported, not edited: RH → ConservationHypothesis is two compiled lemmas composed.',
        '(b) **EQUIVALENT** as propositions, each being equivalent to RH — ConservationHypothesis by compiled lemmas, h2_sign by',
        'b513\'s `rh_imp_h2_sign` one way and Weil\'s criterion (Weil 1952; named at cite, not pinned) the other. In the corpus\'s',
        'own holdings: ConservationHypothesis ⇒ h2_sign is derivable now; h2_sign ⇒ ConservationHypothesis is open exactly at',
        'f4. The five-line sketches of both directions are in `relay/data/b531_components.txt`. (c) Yes. ' + STRENGTH.replace('`', '\''),
        '',
        '**COMPONENT 4 — the bridge priced.** ConservationHypothesis ⇒ h2_sign: COMPILABLE-NOW in SIDE-explicit-formula — the',
        'premise restated, `balance_theorem` and `rh_implies_mathlib_rh` ported (`Real.rpow_lt_rpow_left_iff`,',
        '`Nat.Prime.one_lt`, `Complex.eta` FOUND by the probe; `Real.rpow_right_injective` ABSENT at this pin), composed with',
        '`rh_imp_h2_sign`. h2_sign ⇒ ConservationHypothesis: STATABLE-NOT-COMPILED, ABSENT `h2_sign_imp_rh` (the Weil converse,',
        'f4). The cost of the pin divergence: SIDE-kernel is Lean v4.29.0-rc8 over Mathlib `e960b84`, SIDE-explicit-formula',
        'v4.33.0-rc2 over `51e6992`; neither imports the other, so the premise is restated and its identity with the deposited',
        'one is a statement-read, not a kernel fact.',
        '',
        '**Grades in this act\'s row:** `ConservationBridge.riemann_hypothesis` ENCODES-CONCLUSION against "h2_sign → RH", by',
        'this read; `rest_bound_closed` and `rest_bound_zeta` DERIVES, by (R141)(1).',
        '',
        '**(N1) %s · (N2) %s · (N3) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at this act\'s'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'close.** Nothing compiled; no kernel file written; nothing at Zenodo written; nothing deposits; no grade moved on any',
        'other row; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b531_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
