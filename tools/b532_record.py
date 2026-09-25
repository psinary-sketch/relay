# -*- coding: utf-8 -*-
"""b532_record.py -- COMPONENTS 1, 2 AND 4, THE DESK AND THE TRAIL. ### `python tools/b532_record.py rows | erratum | components | desk | trail | faces`

### COMPONENT 1 (READING (3) of the sealed face): every extracted row (`b532_sentences.json`) carries ONE verdict, hand-read and
### written in `VERDICT` below with its reason: STANDS, RESTS (on E-2026-09-25-1, with the replacement drafted from the
### erratum`s words), or EXCEEDS (with the ceiling sentence beside it). A row the table below does not name REFUSES the run.
### COMPONENT 2: the erratum, drafted, banked to data, NOT filed. COMPONENT 4: the FACES_LEDGER note (appended, `faces`), the
### table`s CONFLICT read as two claims (in the row and the trail), the ceiling sentence printed.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
FL = os.path.join(PP, 'FACES_LEDGER.md')
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EID = 'E-2026-09-25-1'
CORE = ('the kernel`s own `balance_theorem` (Kernel/Voice1.lean) proves that p^(-sigma) = p^(-(1 - sigma)) holds at a prime p '
        'exactly when sigma = 1/2, so `ConservationHypothesis` says that every real part of a nontrivial zero is 1/2: it is RH '
        'restated (%s)' % EID)
CEILING = ('RH and Weil positivity on classK are one Prop apart in the kernel, RH → h2_sign compiled, h2_sign → RH compiled to its '
           "last step; the deposit's Route 3 premise is RH restated, E-2026-09-25-1 drafted.")

S, R, X = 'STANDS', 'RESTS', 'EXCEEDS'
# ### THE HAND-READ VERDICTS. ### (reason ; for RESTS the replacement, drafted from the erratum`s words, not applied)
VERDICT = {
    'M-01': (S, 'an inventory: the three terminals exist and their profiles are the standard three -- true after the erratum', ''),
    'M-02': (R, 'calls Route 3 a route to sigma = 1/2; its input is sigma = 1/2 restated',
             'The Lean 4 kernel formalizes three route terminals, each compiled with zero unproved assertions: Route 1 (structural '
             'exhaustiveness via `structural_exhaustiveness_proved`), Route 2 (codimension analysis via `SpectralCannonFull.spectral_cannon`), '
             'and Route 3, the compiled implication `ConservationBridge.riemann_hypothesis` from `ConservationHypothesis` -- a premise the '
             'kernel`s own `balance_theorem` shows is RH restated (E-2026-09-25-1).'),
    'M-03': (S, 'a pointer to section 27.3; no claim about Route 3', ''),
    'M-04': (R, 'counts the ConservationHypothesis of Route 3 as a register of the premise; it is RH restated',
             'The five registers of the single premise the proof routes through -- the universality hypothesis of `silence_universal`, the '
             'ConservationHypothesis of Route 3 (which the kernel`s own `balance_theorem` shows is RH restated, E-2026-09-25-1), the totality '
             'of realization through places, the balance-to-positivity distance at the multiplicative place, and the spectral-realization '
             'distance -- are gathered as one in section 27.3.'),
    'M-05': (S, 'a different enumeration: "Route 3 (Topological)", the Mobius bundle, not the kernel`s Route 3', ''),
    'M-06': (S, 'an inventory of compiled files and profiles -- true after the erratum', ''),
    'M-07': (S, 'describes the chain exactly: through balance_theorem to StructuralExhaustiveness to RiemannHypothesis -- the erratum`s own route', ''),
    'M-08': (S, 'says the three routes compile independently -- true after the erratum', ''),
    'M-09': (R, 'calls ConservationHypothesis the premise stated at the multiplicative place; it is RH restated',
             '`Bridge/ConservationBridge.lean` defines `ConservationHypothesis` as the proposition that every xi-zero forces the Euler balance '
             'equation at some prime; by Voice 1`s `balance_theorem` that equation holds at a prime exactly when sigma = 1/2, so the '
             'proposition is RH restated, not a premise distinct from it (E-2026-09-25-1).'),
    'M-10': (S, 'the terminal`s statement, quoted', ''),
    'M-11': (S, 'a table row: file, role, sorry and axiom counts -- true after the erratum', ''),
    'M-12': (S, 'a reading-order entry', ''),
    'M-13': (R, 'calls ConservationHypothesis the programme`s one counted premise; it is RH restated',
             '`ConservationHypothesis` in `ConservationBridge.lean` is RH restated by the kernel`s own `balance_theorem` (E-2026-09-25-1) -- '
             'open because RH is open, and as of kernel v1.3 stated identically in kernel and prose.'),
    'M-14': (R, 'true and empty: the chain runs from RH restated to RH',
             'The kernel`s Route 3 closes the chain from the premise to `RiemannHypothesis` in Lean directly -- a chain from RH restated to '
             'RH (E-2026-09-25-1).'),
    'M-15': (S, 'a concordance note on the W-7 change and the profile -- true after the erratum', ''),
    'M-16': (S, 'a concordance row: terminal, file, profile', ''),
    'M-17': (S, 'says the clean status certifies the implication and nothing more -- true, and the erratum`s point', ''),
    'M-18': (R, 'reports work aimed at the Route 3 interface as work on a premise; the premise is RH restated',
             'The method`s continuation past the Day-1 kernel -- aimed at the Route 3 interface, whose premise the kernel`s own '
             '`balance_theorem` shows is RH restated (E-2026-09-25-1) -- is reported in section 27.3.'),
    'M-19': (S, 'an inventory of compiled terminals and profiles -- true after the erratum', ''),
    'M-20': (R, 'THE REGISTER-2 SENTENCE: names ConservationHypothesis as the premise`s second register',
             'Second: the proposition named `ConservationHypothesis` in the kernel`s Route 3 -- every xi-zero forces the Euler balance '
             'equation at some prime -- which the kernel`s own `balance_theorem` shows holds exactly when every such real part is 1/2: RH '
             'restated (E-2026-09-25-1).'),
    'M-21': (S, 'reports the v1.3 alignment of def and prose and the strengthening -- true after the erratum', ''),
    'M-22': (R, 'THE REGISTER-2 SENTENCE: "the premise itself, stated at the multiplicative place"; it is RH restated',
             'This proposition is RH restated by the kernel`s own `balance_theorem` (E-2026-09-25-1); Chapter 13`s Conservation of Spectra '
             'Theorem motivates it but does not discharge it.'),
    'M-23': (R, 'calls the Conservation route a route to sigma = 1/2; its input is sigma = 1/2 restated',
             'The Lean kernel formalizes three route terminals: the structural route via `Bridge.StructuralExhaustiveness`, the codimension '
             'route via the Spectral Cannon chain, and the Conservation route via `ConservationBridge.riemann_hypothesis` taking '
             '`ConservationHypothesis` -- RH restated (E-2026-09-25-1) -- to `RiemannHypothesis`.'),
    'M-24': (R, 'calls Route 3`s hypothesis the one open premise of 27.3; it is RH restated',
             'Conservation of Spectra from Tate`s thesis (Chapter 13) is the certificate that motivates Route 3`s hypothesis, which the '
             'kernel`s own `balance_theorem` shows is RH restated (E-2026-09-25-1), not its discharge.'),
    'M-25': (S, 'a changelog entry recording W-7 -- true after the erratum', ''),
    'M-26': (S, 'says the premise remains RH-equivalent and open -- true, and b531 confirms it in the kernel`s own lemmas', ''),
    'M-27': (S, 'a changelog entry: "RH under the open premise h2" -- true after the erratum', ''),
    'K-01': (R, 'describes Route 3`s input as the conservation clause through the places of Q, in the criterion lineage of Weil and Li; '
             'it is RH restated',
             '... and ConservationBridge.riemann_hypothesis (the compiled implication from ConservationHypothesis, which the kernel`s own '
             'balance_theorem shows is RH restated -- E-2026-09-25-1).'),
    'Z21520474-01': (R, 'THE CEILING SENTENCE, as corrected at b499: for Route 3 the reduction to a single located clause is true and empty',
                     'SIDE-kernel: the machine-verified architecture of the SIDE programme`s route terminals; its Route 3 premise is RH '
                     'restated (E-2026-09-25-1). [DRAFT ONLY: the ceiling`s next wording is the author`s, (R142)(2).]'),
    'Z21520474-02': (R, 'the same sentence as K-01, unchanged by b499`s edits',
                     '... and ConservationBridge.riemann_hypothesis (the compiled implication from ConservationHypothesis, which the '
                     'kernel`s own balance_theorem shows is RH restated -- E-2026-09-25-1).'),
    'Z21539167-01': (R, 'calls ConservationHypothesis an interface whose mathematics is Chapter 13`s; it is RH restated',
                     'A skeptic can run lake build at the pinned kernel commit (SIDE-kernel v1.5 = 0e5233f) and #print axioms at the '
                     'named route theorems (...; ConservationBridge.riemann_hypothesis -- the third is the compiled implication from '
                     'ConservationHypothesis, which the kernel`s own balance_theorem shows is RH restated, E-2026-09-25-1).'),
}


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


SE = json.loads(read('b532_sentences.json') or '{}')
w = lambda v: 'HELD' if v else 'REFUTED'


def graded():
    rows = SE.get('rows', [])
    missing = [r['id'] for r in rows if r['id'] not in VERDICT]
    extra = [k for k in VERDICT if k not in {r['id'] for r in rows}]
    if missing or extra:
        sys.exit('### REFUSED: rows without a verdict %s ; verdicts without a row %s' % (missing, extra))
    return [dict(r, verdict=VERDICT[r['id']][0], reason=VERDICT[r['id']][1], replacement=VERDICT[r['id']][2]) for r in rows]


def counts(g):
    out = {}
    for rec in SE['records']:
        out[rec] = {v: sum(1 for x in g if x['rec'] == rec and x['verdict'] == v) for v in (S, R, X)}
    return out


def rows_cmd():
    g = graded()
    c = counts(g)
    L = ['=' * 132, 'b532 -- COMPONENT 1: THE DEPOSITED SENTENCES, ONE VERDICT EACH.', '=' * 132, '',
         '### COUNTS PER RECORD (STANDS / RESTS / EXCEEDS):']
    for rec, v in c.items():
        L.append('  %-14s %-60s %2d / %2d / %2d' % (rec, SE['records'][rec]['name'][:60], v[S], v[R], v[X]))
    L.append('  %-14s %-60s %2d / %2d / %2d' % ('TOTAL', '', sum(v[S] for v in c.values()), sum(v[R] for v in c.values()), sum(v[X] for v in c.values())))
    L += ['', '### THE RESTS AND EXCEEDS ROWS, IN FULL:']
    for x in g:
        if x['verdict'] in (R, X):
            L += ['', '%s  [%s]  %s' % (x['id'], x['verdict'], x['section']), '  DEPOSITED : ' + x['text'], '  WHY       : ' + x['reason'],
                  '  REPLACEMENT (drafted, not applied) : ' + x['replacement'] if x['verdict'] == R else '  CEILING : ' + CEILING]
    L += ['', '### THE STANDS ROWS, WITH THEIR REASONS:']
    for x in g:
        if x['verdict'] == S:
            L.append('  %-14s %s' % (x['id'], x['reason']))
    L += ['', '### EXCEEDS : %d rows. The ceiling sentence, printed beside: %s' % (sum(v[X] for v in c.values()), CEILING), '=' * 132]
    io.open(os.path.join(D, 'b532_rows.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(rows=g, counts=c), io.open(os.path.join(D, 'b532_rows.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print(NL.join(L[:14]))


def erratum():
    g = graded()
    rests = [x for x in g if x['verdict'] == R]
    by = {}
    for x in rests:
        by.setdefault(x['rec'], []).append(x)
    L = ['## %s — The deposited kernel`s Route 3 premise is equivalent to RH by a ten-line lemma the kernel itself contains '
         '(DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5) — DRAFT, NOT FILED' % EID, '',
         '**Drafted 2026-09-25 (b532), on the author`s ruling (R142)(3), from the read banked at b531 (relay `data/b531_premise.txt`, '
         '`data/b531_components.txt`); TO BE FILED ON THE AUTHOR`S WORD AT THE PASTE AFTER.',
         '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
         '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**', '',
         '**Affected deposits.** *A Place to Stand*, Zenodo v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — '
         'the monograph and the record description; SIDE-kernel v1.5, tag `v1.5` = commit `0e5233f` '
         '([10.5281/zenodo.21520474](https://doi.org/10.5281/zenodo.21520474)) — the record description.', '',
         '**What the kernel says, in its own words.** `Bridge/ConservationBridge.lean` at `0e5233f`: *"def ConservationHypothesis : Prop := '
         '∀ (σ : ℝ), is_xi_zero σ → ∃ (p : Nat) (hp : Nat.Prime p), (prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))"*. '
         '`Kernel/Voice1.lean` at `0e5233f`: *"theorem balance_theorem (p : Nat) (hp : Nat.Prime p) (s : Real) : (prime_as_real p hp) ^ (-s) '
         '= (prime_as_real p hp) ^ (-(1 - s)) <-> s = 1 / 2"*.', '',
         '**The two lemmas, at their pins.** (1) RH from the premise: `ConservationBridge.riemann_hypothesis` (three lines, through '
         '`structural_exhaustiveness_proved` and `balance_theorem`), SIDE-kernel `0e5233f`. (2) The premise from RH: '
         '`techne_kernel_integration.structural_exhaustiveness_from_rh` (Kernel/Integration.lean) followed by `balance_theorem` at the prime '
         '2, SIDE-kernel `0e5233f`; compiled as one theorem, `ch_iff_rh`, in SIDE-explicit-formula at this act`s commit.', '',
         '**The premise is RH restated.** In the kernel`s own words: the premise says that for every real part σ of a nontrivial zero, '
         '*"(prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))"* at some prime, and the kernel proves that equation '
         '*"<-> s = 1 / 2"*. So the premise says every such real part is ½.', '',
         '**The terminal`s grade against each claim** (a grade is a relation between a terminal and a named claim, (R40)): against "R2 '
         'implies RH", DERIVES (`FACES_LEDGER.md` row R2); against RH, INTERFACES on the named premise (`OPEN_TRAILS.md:5523`) — and that '
         'INTERFACES grade on "the open premise h2, carried openly" does not distinguish the premise from the conclusion; against '
         '"h2_sign → RH", ENCODES-CONCLUSION (b531).', '',
         '**The deposited sentences that rest on it** (b532, relay `data/b532_rows.txt`, each with a replacement drafted from this '
         'entry`s words):']
    for rec, xs in by.items():
        L.append('- **%s** — %d sentence(s): %s' % (SE['records'][rec]['name'], len(xs), ', '.join(x['id'] for x in xs)))
        for x in xs:
            L.append('  - `%s`: *"%s"*' % (x['id'], x['text'][:400] + ('…' if len(x['text']) > 400 else '')))
    L += ['', '**What is not corrected.** The monograph`s own Appendix G already says *"the premise remains RH-equivalent and open"*; '
          'this entry does not dispute it and adds that, for register 2, the equivalence is a ten-line lemma inside the kernel. Every '
          'other route terminal, every figure and every other register is untouched.', '',
          '**Status.** DRAFT. Retained at monograph v1.1.2 and SIDE-kernel v1.5 when filed. Whether any Zenodo description is edited '
          'under (R110) is the author`s ruling.']
    t = NL.join(L) + NL
    io.open(os.path.join(D, 'b532_erratum_draft.md'), 'w', encoding='utf-8', newline=NL).write(t)
    print(t)


FACES_NOTE = [
    '', '*__NOTE ON ROW R2 — appended by b532, 2026-09-25, on the author`s ruling (R142)(3); no prior byte of this ledger is edited.__* '
    'Row R2`s cell says *"the converse is not compiled and the face stays open"*. The converse is two lemmas already compiled in the '
    'deposited kernel at SIDE-kernel v1.5 = `0e5233f`: `techne_kernel_integration.structural_exhaustiveness_from_rh` '
    '(`Kernel/Integration.lean`) and `techne_kernel_voice1.balance_theorem` (`Kernel/Voice1.lean`) at the prime 2; the equivalence '
    'is compiled as one theorem, `ch_iff_rh`, in SIDE-explicit-formula (`SIDEExplicitFormula/H2Bridge.lean`, b532). R2 is RH '
    'restated (b531); erratum E-2026-09-25-1 is drafted (relay `data/b532_erratum_draft.md`) and not filed.', '']
CONFLICT = ('The terminal table shows the Route 3 terminal ConservationBridge.riemann_hypothesis in CONFLICT: that is two claims under '
            '(R40), not one claim graded twice -- DERIVES against "R2 implies RH" (FACES_LEDGER.md row R2) and ENCODES-CONCLUSION '
            'against "h2_sign -> RH" (b531).')


def faces():
    before = open(FL, 'rb').read()
    if b'NOTE ON ROW R2' in before:
        sys.exit('### ALREADY PRESENT')
    open(FL, 'ab').write(NL.join(FACES_NOTE).encode('utf-8'))
    after = open(FL, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before))
    print('  FACES_LEDGER.md : %(added)d bytes added, prefix %(prefix)s' % out)
    io.open(os.path.join(D, 'b532_faces_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


def kread():
    return json.loads(read('b532_attempts.json') or '[]'), json.loads(read('b532_profile.json') or '{}'), read('b532_statement.txt')


def first_clean(at):
    ok = [a['attempt'] for a in at if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def scores():
    g = graded()
    at, pr, _ = kread()
    std = pr.get('std3', {})
    rests = [x['id'] for x in g if x['verdict'] == R]
    fn = json.loads(read('b532_faces_notes.txt') or '{}')
    fc = first_clean(at)
    return dict(rests=rests, first_clean=fc,
                n1=len(rests) >= 5 and any(r in rests for r in ('M-20', 'M-21', 'M-22')),
                n2=any(r.startswith('Z21520474') for r in rests),
                n3=fc is not None and fc <= 2 and bool(std) and all(std.values()),
                s1=fc == 1, s2=std.get(NS + 'ch_iff_rh') is True, s3=fn.get('prefix') is True)


def components():
    at, pr, st = kread()
    L = ['=' * 132, 'b532 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### COMPONENT 1: `b532_rows.txt` (counts per record, RESTS rows in full with replacements, STANDS reasons).',
         '### COMPONENT 2: `b532_erratum_draft.md` -- DRAFT, NOT FILED.', '',
         '### COMPONENT 3 -- THE BRIDGE: `SIDEExplicitFormula/H2Bridge.lean`.']
    for a in at:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s' % (a['attempt'], a['exit'], a['errors'], a['seconds']))
    L += ['', '### THE STATEMENTS, FROM THE DECLARATION LINE TO ITS := :'] + st.rstrip(NL).split(NL)
    L += ['', '### THE PROFILE (AxiomCheckBridge.lean):'] + ['  ' + l for l in pr.get('lines', [])]
    L += ['  ### whole-string standard three : %d of %d' % (sum(1 for v in pr.get('std3', {}).values() if v), len(pr.get('std3', {}))),
          '  ### #check : %s' % pr.get('checks')]
    for k, v in (pr.get('prints') or {}).items():
        L.append('  ### #print %s : %s' % (k, ' '.join((v or 'NONE').split())))
    L += ['', '### COMPONENT 4.', '  (a) FACES_LEDGER R2 : %s' % read('b532_faces_notes.txt').strip(), '  (b) ' + CONFLICT,
          '  (c) THE CEILING SENTENCE THE RECORD MAY USE UNTIL THE AUTHOR RULES : "' + CEILING + '"', '=' * 132]
    io.open(os.path.join(D, 'b532_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc = scores()
    _, pr, _ = kread()
    L = ['=' * 104, 'b532 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- RESTS rows %d (%s) ; register-2 sentences of 27.3 among them : %s.'
         % (w(sc['n1']), len(sc['rests']), ', '.join(sc['rests']), [r for r in ('M-20', 'M-21', 'M-22') if r in sc['rests']]),
         '  **(N2)** ### **%s.** -- rows of Z21520474 reading RESTS : %s.' % (w(sc['n2']), [r for r in sc['rests'] if r.startswith('Z21520474')]),
         '  **(N3)** ### **%s.** -- first clean attempt %s (at most 2) ; std3 %d of %d.'
         % (w(sc['n3']), sc['first_clean'], sum(1 for v in pr.get('std3', {}).values() if v), len(pr.get('std3', {}))),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- first clean attempt %s against 1.' % (w(sc['s1']), sc['first_clean']),
         '  **(S2)** ### **%s.** -- ch_iff_rh std3 : %s.' % (w(sc['s2']), pr.get('std3', {}).get(NS + 'ch_iff_rh')),
         '  **(S3)** ### **%s.** -- FACES_LEDGER prior bytes a true prefix : %s.' % (w(sc['s3']), sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b532_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b532_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b532_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b532 — the deposit read against b531; E-2026-09-25-1 drafted; the trivial bridge compiled; (R142) entered'


def trail():
    sc = scores()
    c = counts(graded())
    tot = {v: sum(x[v] for x in c.values()) for v in (S, R, X)}
    at, pr, st = kread()
    m = re.search(r'^theorem ch_imp_h2_sign\b[\s\S]*?:=', st, re.M)
    m2 = re.search(r'^theorem ch_iff_rh\b[\s\S]*?:=', st, re.M)
    body = [
        '', HEADING, '',
        '**(R142) ratified.** (1) b531 is entered as the week\'s most consequential read, and it reads against the programme: the',
        'deposit\'s Route 3 premise is RH restated. The terminal grades ENCODES-CONCLUSION against "h2_sign → RH" and DERIVES',
        'against "R2 → RH"; both stand as relations under (R40). (2) The consequence for the claim ceiling is stated before it is',
        'ruled: for Route 3, "RH reduced to a single located clause, reduction machine-verified" is true and empty; the',
        'non-trivial reduction the programme holds is RH ⟺ Weil positivity on classK, RH → h2_sign compiled and h2_sign → RH',
        'compiled to f4; the ceiling\'s next wording is the author\'s. (3) E-2026-09-25-1 drafted here, filed on the author\'s word',
        'at the paste after; FACES_LEDGER R2 corrected by appended note. (4) The bridge compiled in its trivial direction. (5) The',
        'kernel lane opened for this act and shuts at its close.',
        '',
        '**COMPONENT 1 — the deposited sentences** (relay `data/b532_rows.txt`), from the monograph v1.1.2 (md5 matched to',
        'Zenodo), the kernel record 21520474 as b493 banked it, SIDE-kernel\'s README at v1.5, and the three descriptions as b499',
        'fetched them back: **%d rows — STANDS %d, RESTS ON E-2026-09-25-1 %d, EXCEEDS %d.** The RESTS rows: %s. Each carries a'
        % (sum(tot.values()), tot[S], tot[R], tot[X], ', '.join(sc['rests'])),
        'replacement drafted from the erratum\'s words, not applied. The ferry\'s "register 2" found nothing by name — section 27.3',
        'names its registers by ordinal — so the matcher was widened to the sentences from "Second:" to "Third:"; both runs banked.',
        '',
        '**COMPONENT 2 — E-2026-09-25-1, drafted, not filed** (relay `data/b532_erratum_draft.md`).',
        '',
        '**COMPONENT 3 — the bridge, `SIDEExplicitFormula/H2Bridge.lean`**, compiled at attempt %s, %d of %d theorems the standard'
        % (sc['first_clean'], sum(1 for v in pr.get('std3', {}).values() if v), len(pr.get('std3', {}))),
        'three on the whole string. The premise is restated verbatim (`conservationHypothesis`, SIDE-kernel\'s `is_xi_zero` and',
        '`prime_as_real` unfolded); the form over `zetaZeroConfig` follows from it (`ch_imp_config`), the reverse needing the',
        'classical strip fact that Zeta23 records as not in the kernel.',
        '',
        '```lean',
        m2.group(0) if m2 else '',
        m.group(0) if m else '',
        '```',
        '',
        'The converse `h2_sign_imp_ch` is a Prop, not proved, and `h2_sign_imp_ch_iff` shows it is b513\'s `h2_sign_imp_rh` — f4.',
        '',
        '**COMPONENT 4.** FACES_LEDGER R2 annotated by an appended note citing the two lemmas. ' + CONFLICT,
        '**The claim-ceiling sentence the record may use from this act until the author rules:** "' + CEILING + '"',
        '',
        '**(N1) %s · (N2) %s · (N3) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at this act\'s'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'close.** The kernel is not tagged; nothing filed to ERRATA; nothing at Zenodo written; nothing deposits; no grade',
        'conferred or moved; row U1 unedited; `h2` where the deposit left it — and named now, in the kernel, as what it always',
        'was; the four lists stay OPEN; nothing here is a statement about RH.',
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
    io.open(os.path.join(D, 'b532_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


def main():
    {'rows': rows_cmd, 'erratum': erratum, 'faces': faces, 'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()


if __name__ == '__main__':
    main()
