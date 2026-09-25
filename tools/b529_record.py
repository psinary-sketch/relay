# -*- coding: utf-8 -*-
"""b529_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b529_record.py components | desk | trail`
### Every figure READ from the banks; the scores are READING (9)'s.
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
NS = 'SIDEExplicitFormula.B321.'
C12 = ['pairTwo_factored', 'pairTwo_near_far', 'nearInt_ge', 'realizedGrowth_eq', 'realizedGrowth_ge_one', 'nearPair_eq',
       'pair_near_sign']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


AT = json.loads(read('b529_attempts.json') or '[]')
PR = json.loads(read('b529_profile.json') or '{}')
RD = json.loads(read('b529_read.json') or '{}')
VA = json.loads(read('b529_values.json') or '{}')
STMT = read('b529_statement.txt')
w = lambda v: 'HELD' if v else 'REFUTED'


def first_clean():
    ok = [a['attempt'] for a in AT if a['exit'] == 0 and a['errors'] == 0 and not a['sorry'] and not a.get('stopped_by')]
    return ok[0] if ok else None


def head(name):
    m = re.search(r'^(?:theorem|def) %s\b[\s\S]*?:=' % re.escape(name), STMT, re.M)
    return m.group(0) if m else ''


def scores():
    fc = first_clean()
    std = PR.get('std3', {})
    return dict(first_clean=fc,
                n1=fc is not None and fc <= 3 and all(std.get(NS + n) is True for n in C12),
                n2=bool(VA) and VA['eps_delta'] < 0.1,
                n3=bool(RD) and RD.get('lemmas_beyond_b524') == [],
                s1=fc is not None and fc <= 2,
                s2=bool(std) and len(std) == 19 and all(std.values()),
                s3=bool(VA) and VA['eps'] < 1e-3)


def components():
    L = ['=' * 132, 'b529 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE INSTALL:', read('b529_install.json').rstrip(NL),
         '', '### THE ATTEMPTS (READING (6)):']
    for a in AT:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s%s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                     (' ; STOPPED -- ' + a['stopped_by']) if a.get('stopped_by') else ''))
        for e in a.get('first_errors', []):
            L.append('      ' + e[:220])
    L += ['', '### THE STATEMENTS, FROM THE DECLARATION LINE TO ITS := :'] + read('b529_statement.txt').rstrip(NL).split(NL)
    L += ['', '### THE PROFILE (AxiomCheckPair.lean):'] + ['  ' + l for l in PR.get('lines', [])]
    L += ['  ### whole-string standard three : %d of %d' % (sum(1 for v in PR.get('std3', {}).values() if v), len(PR.get('std3', {}))),
          '  ### #check : %s' % PR.get('check_prop')]
    for k, v in (PR.get('prints') or {}).items():
        L.append('  ### #print %s : %s' % (k, (v or 'NONE').replace(NL, ' ')))
    L += ['', '### THE VENDORED REFERENCES (N3): lemmas %s ; b524`s %s ; BEYOND b524`s %s'
          % (RD.get('lemma_refs'), RD.get('b524_lemma_refs'), RD.get('lemmas_beyond_b524') or 'NONE'),
          '', '### COMPONENT 3`S NUMBER (READING (7)), Q0`s B-spline instance, a = %s, p = %s:' % (VA.get('a'), VA.get('p'))]
    for k in ('gamma0', 'delta', 'S', 'N', 'absF', 'absF0', 'eps_delta', 'eps_zero', 'eps', 'G', 'bank_growth', 'slope', 'pairEps',
              'c_minus_eps', 'rhs', 'pairTwo_khat', 'pairTwo_formula', 'bank_pair_half', 'near_pair', 'bound_holds_on_instance'):
        L.append('  %-24s %s' % (k, VA.get(k)))
    L += ['  ### the formula and the instrument`s khat share phihat: their agreement checks the transcription of Component 1,',
          '  ### not phihat. ### b522`s banked pair is at the zero`s own ordinate, the kernel`s pairTwo at gamma_0.', '=' * 132]
    io.open(os.path.join(D, 'b529_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc = scores()
    std = PR.get('std3', {})
    L = ['=' * 104, 'b529 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S THREE.', '-' * 104,
         '  **(N1)** ### **%s.** -- first clean attempt : %s (at most 3) ; Components 1 and 2 std3 : %d of %d.'
         % (w(sc['n1']), sc['first_clean'], sum(1 for n in C12 if std.get(NS + n) is True), len(C12)),
         '  **(N2)** ### **%s.** -- eps_delta = |F| / N = %.4e against 0.1 (eps_zero %.4e beside it, not scored).'
         % (w(sc['n2']), VA.get('eps_delta', float('nan')), VA.get('eps_zero', float('nan'))),
         '  **(N3)** ### **%s.** -- vendored lemmas cited %s ; beyond b524`s %s (declared on the face in (C2) before the compile).'
         % (w(sc['n3']), RD.get('lemma_refs'), RD.get('lemmas_beyond_b524') or 'NONE'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- first clean attempt %s against 2.' % (w(sc['s1']), sc['first_clean']),
         '  **(S2)** ### **%s.** -- every theorem in the axiom check std3 : %d of %d.' % (w(sc['s2']), sum(1 for v in std.values() if v), len(std)),
         '  **(S3)** ### **%s.** -- eps %.4e against 1e-3.' % (w(sc['s3']), VA.get('eps', float('nan'))),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3')].count(True), [sc[k] for k in ('n1', 'n2', 'n3')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b529_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b529_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b529_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


HEADING = '### b529 — (f)(ii), the pair\'s term, as far as it derives; (R139) entered'


def trail():
    sc = scores()
    fc = sc['first_clean']
    secs = next((a['seconds'] for a in AT if a['attempt'] == fc), float('nan'))
    std = PR.get('std3', {})
    stmt1 = head('pairTwo_factored')
    body = [
        '', HEADING, '',
        '**(R139) ratified.** (1) b528 is entered: on the kernel\'s plateau ξ is positive beyond its estimated bound at 46 of 46',
        'widths to 60 and Q0 is within reach at none, the tail ESTIMATE 15 to 2000 times B′; (N2) and (N3) REFUTED as ordered; the',
        'four defects entered as declared, D3\'s roundoff floor added to `W-ORD-SMOOTH-TAIL`. (2) **The reason, entered as a',
        'finding about windows:** the exp(−1/x) transition, though C^∞, has a transform near t = 150 about five orders above the',
        'order-7 B-spline\'s; smoother is not better at finite height, and any future instance is chosen by its transform at the',
        'bank\'s height, not by its smoothness class. (3) **Choice (c):** (f)(ii) proceeds for every C⁴ φ ≥ 0 with the realized G',
        'as hypothesis, instance-free; Q0\'s witness stays on the order-7 B-spline, and the corpus cites it so — the kernel\'s',
        'theorems cover the B-spline, the kernel\'s named instance is a function on which Q0 could not be read.',
        '**`W-ORD-BSPLINE-INSTANCE` is filed** (the author\'s): a B-spline ramp of order p constructed in the kernel as a C^(p−2) φ,',
        'so that a compiled witness at a specific ρ can one day cite numbers on its own function; trigger: the act that wants a',
        'compiled witness at Q0, or the author\'s word. Route (a), widening past 60, noted as capped by the prime table at a = 64',
        'and not taken. (4) The kernel lane opened for this act and shuts at its close.',
        '',
        '**COMPONENT 1 — `SIDEExplicitFormula/PairTerm.lean`, new, importing b524\'s window.** The pair\'s term is',
        'term(ρ₀) + term(1 − ρ̄₀), term(ρ) = paperFT k (gammaOf ρ), each of multiplicity one, ρ₀ = ½ + δ + iγ₀ (`pairTwo`); its',
        'images are γ₀ − iδ and γ₀ + iδ. `pairTwo_factored`, for every real φ that is C⁴ with compact support, from its',
        'declaration line to its `:=`:',
        '',
        '```lean',
        stmt1,
        '```',
        '',
        'The proof uses b524\'s factorisation and the kernel\'s `Zeta23.EF.paperFT_weilTest` (for a real h, k̂(z) = ĥ(z)ĥ(−z)).',
        '`pairTwo_near_far`, for **even** φ (the identification needs it; both named instances are even): each of the four values',
        'is (N + F)/2 or (N + F̄)/2, the near factor N = ∫φ(u)cosh(δu)du (`nearInt`) times ½ and the far factor',
        'F = φ̂(2γ₀ − iδ) (`farFT`). With two images the constant is c = 2 (`pairConst`); b524\'s `fConst = 4` counts four.',
        '',
        '**COMPONENT 2 — the near factor bounded below.** `nearInt_ge`: from φ ≥ 0, ∫φ ≤ ∫φ cosh(δu); `realizedGrowth_eq`: b524\'s',
        '`realizedGrowth φ δ` is that ratio, by `rfl`; `realizedGrowth_ge_one`. The near-factor product at the pair (`nearPair`, the',
        'pair\'s term with F = 0) equals N²δ²(δ² − 4γ₀²)/2 (`nearPair_eq`), and `pair_near_sign` fixes its sign: negative for',
        '0 < δ < 2γ₀, φ ≥ 0, ∫φ > 0.',
        '',
        '**COMPONENT 3 — the far factor as a named hypothesis, not proved.** `farSmall γ₀ φ δ ε : Prop := ‖farFT γ₀ φ δ‖ ≤ ε ·',
        'nearInt φ δ`. `pair_bound`: for φ even, ≥ 0, C⁴, compactly supported, ∫φ > 0, γ₀ > 0, δ > 0, ε ≥ 0, under `farSmall` at δ',
        '**and at 0** (the slope −2γ₀·Ĉ(γ₀) carries φ̂(2γ₀)) and ε′ ≤ c: Re(pair\'s term) ≤ −(c − ε′)·δ²·|slope|²·G², with',
        'c = `pairConst` = 2 and ε′ = `pairEps ε δ γ₀` = 2 − (2(1 − (2ε + ε²)) − δ²/(2γ₀²)·(1 + (2ε + ε²)))/(1 + ε)², as Lean prints them.',
        '**Its number, at Q0\'s order-7 B-spline instance at a = 34** (b522\'s window; G checked against b522\'s bank, |diff| %.1e):'
        % VA.get('G_diff', float('nan')),
        'δ = %.5f, N = G = %.10f, |F| = %.3e, **ε_δ = |F|/N = %.3e**; the same Prop at 0, |φ̂(2γ₀)|/∫φ = %.3e; at ε = %.3e,'
        % (VA.get('delta', 0), VA.get('N', 0), VA.get('absF', 0), VA.get('eps_delta', 0), VA.get('eps_zero', 0), VA.get('eps', 0)),
        'ε′ = %.6f and c − ε′ = %.6f; the bound −(c − ε′)δ²|slope|²G² = %.4f beside the instance\'s pair term %.4f (two images).'
        % (VA.get('pairEps', 0), VA.get('c_minus_eps', 0), VA.get('rhs', 0), (VA.get('pairTwo_khat') or [0])[0]),
        'The B-spline is not a kernel object (`W-ORD-BSPLINE-INSTANCE`); the number is a number on it, not a theorem.',
        '',
        '**COMPONENT 4 — the table.** `AxiomCheckPair.lean` prints %d theorems, %d of them the standard three on the whole string;'
        % (len(std), sum(1 for v in std.values() if v)),
        'first clean attempt %s of %d (%.1f s). Grades by statement-read: Component 1 DERIVES, Component 2 DERIVES, Component 3'
        % (fc, len(AT), secs),
        'INTERFACES on the named hypothesis `farSmall`. **`W-ORD-WEIL-CONVERSE`\'s table, re-printed here with f2 marked:**',
        '',
        '| lemma | state |',
        '|:--|:--|',
        '| (d) | DONE at b517 |',
        '| (f1) | DONE at b524 |',
        '| (f2) | b529: Components 1 and 2 DERIVES; Component 3 INTERFACES on `farSmall`, not proved |',
        '| (f3) | OPEN, unchanged |',
        '| (f4) | OPEN, unchanged |',
        '',
        '**(N1) %s · (N2) %s · (N3) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at this act\'s'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'close.** The kernel is not tagged; nothing at Zenodo written; nothing deposits; no grade moved on any other row; row U1',
        'unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.',
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
    io.open(os.path.join(D, 'b529_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
