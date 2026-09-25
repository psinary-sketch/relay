# -*- coding: utf-8 -*-
"""b530_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b530_record.py components | desk | trail`
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
DECAY = ['hasCompactSupport_of_Icc', 'support_deriv_Icc', 'support_iteratedDeriv_Icc', 'paperFT_iteratedDeriv', 'paperFT_decay',
         'paperFT_decay_re', 'paperFT_decay_zero', 'cosWin_support_Icc', 'window_decay_re']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


ATD = json.loads(read('b530_attempts_decay.json') or '[]')
ATR = json.loads(read('b530_attempts_rest.json') or '[]')
PR = json.loads(read('b530_profile.json') or '{}')
VA = json.loads(read('b530_values.json') or '{}')
STMT = read('b530_statement.txt')
w = lambda v: 'HELD' if v else 'REFUTED'


def first_clean(at):
    ok = [a['attempt'] for a in at if a['exit'] == 0 and a['errors'] == 0 and not a['sorry'] and not a.get('stopped_by')]
    return ok[0] if ok else None


def head(name):
    m = re.search(r'^(?:theorem|def) %s\b[\s\S]*?:=' % re.escape(name), STMT, re.M)
    return m.group(0) if m else ''


def z_hyps(stmt):
    """### the binders of a statement that mention the configuration Z, by their types."""
    return sorted(set(t.strip() for t in re.findall(r'\((?:\w+) : ([^()]*\bZ\b[^()]*)\)', stmt)))


def scores():
    std = PR.get('std3', {})
    fd, fr = first_clean(ATD), first_clean(ATR)
    zh = z_hyps(head('rest_bound'))
    return dict(first_clean_decay=fd, first_clean_rest=fr, rest_z_hyps=zh,
                n1=fd is not None and fd <= 3 and all(std.get(NS + n) is True for n in DECAY),
                n2=std.get(NS + 'rest_bound') is True and zh == ['HCount Z A₀', 'HStrip Z'],
                n3=std.get(NS + 'two_delta_lt_one') is True and std.get(NS + 'not_f4_needs') is True,
                n4=bool(VA) and VA['R'] > 100.0 * VA['rest_measured'],
                s1=fd == 1,
                s2=fr is not None and fr <= 3 and len(std) == 30 and all(std.values()),
                s3=bool(VA) and VA['ratio_R_rest'] > 1e10)


def components():
    L = ['=' * 132, 'b530 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE INSTALL:', read('b530_install.json').rstrip(NL)]
    for nm, at in (('DecayBound', ATD), ('RestBound', ATR)):
        L += ['', '### THE ATTEMPTS, %s (READING (6)):' % nm]
        for a in at:
            L.append('  attempt %d : exit %d ; %d error lines ; %.1f s' % (a['attempt'], a['exit'], a['errors'], a['seconds']))
            for e in a.get('first_errors', []):
                L.append('      ' + e[:220])
    L += ['', '### THE STATEMENTS, FROM THE DECLARATION LINE TO ITS := :'] + STMT.rstrip(NL).split(NL)
    L += ['', '### THE PROFILE (AxiomCheckRest.lean):'] + ['  ' + l for l in PR.get('lines', [])]
    L += ['  ### whole-string standard three : %d of %d' % (sum(1 for v in PR.get('std3', {}).values() if v), len(PR.get('std3', {})))]
    for k, v in (PR.get('checks') or {}).items():
        L.append('  ### #check %s : %s' % (k, v))
    for k, v in (PR.get('prints') or {}).items():
        L.append('  ### #print %s : %s' % (k, ' '.join((v or 'NONE').split())))
    L += ['', '### THE HYPOTHESES OF rest_bound THAT MENTION Z : %s' % z_hyps(head('rest_bound')),
          '', '### COMPONENT 3`S NUMBERS (READING (7)), Q0`s B-spline instance, a = %s, p = %s:' % (VA.get('a'), VA.get('p'))]
    for k in ('gamma0', 'L', 'delta', 'int_abs_g', 'int_abs_g4', 'windowA', 'zeros_banked', 'A0_measured', 'zeta3Sum', 'R',
              'rest_measured', 'rest_terms', 'pair_orbit_abs', 'pair_orbit_signed', 'ratio_R_rest', 'ratio_R_pair', 'exceeds_100',
              'G', 'G_over_exp', 'exp_L', 'exp_2dL', 'two_delta', 'note'):
        L.append('  %-20s %s' % (k, VA.get(k)))
    L += ['=' * 132]
    io.open(os.path.join(D, 'b530_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:12]))


def desk():
    sc = scores()
    std = PR.get('std3', {})
    L = ['=' * 104, 'b530 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- DecayBound first clean attempt : %s (at most 3) ; its nine theorems std3 : %d of 9.'
         % (w(sc['n1']), sc['first_clean_decay'], sum(1 for n in DECAY if std.get(NS + n) is True)),
         '  **(N2)** ### **%s.** -- rest_bound std3 : %s ; its hypotheses mentioning Z : %s.'
         % (w(sc['n2']), std.get(NS + 'rest_bound'), sc['rest_z_hyps']),
         '  **(N3)** ### **%s.** -- two_delta_lt_one std3 : %s ; not_f4_needs std3 : %s.'
         % (w(sc['n3']), std.get(NS + 'two_delta_lt_one'), std.get(NS + 'not_f4_needs')),
         '  **(N4)** ### **%s.** -- R %.4e against 100 x the measured rest %.4f (R / rest %.4e).'
         % (w(sc['n4']), VA.get('R', 0), VA.get('rest_measured', 0), VA.get('ratio_R_rest', 0)),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- DecayBound first clean attempt %s against 1.' % (w(sc['s1']), sc['first_clean_decay']),
         '  **(S2)** ### **%s.** -- RestBound first clean attempt %s (at most 3) ; std3 %d of %d.'
         % (w(sc['s2']), sc['first_clean_rest'], sum(1 for v in std.values() if v), len(std)),
         '  **(S3)** ### **%s.** -- R / rest %.4e against 1e10.' % (w(sc['s3']), VA.get('ratio_R_rest', 0)),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b530_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b530_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(sc, io.open(os.path.join(D, 'b530_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1, ensure_ascii=False)
    print(NL.join(L))


HEADING = '### b530 — f3, the other zeros bounded above, with its limit printed; (R140) entered'


def trail():
    sc = scores()
    std = PR.get('std3', {})
    body = [
        '', HEADING, '',
        '**(R140) ratified.** (1) b529 is entered: (f)(ii) compiled as far as it derives — the pair\'s algebra and the near factor',
        'DERIVES, the far factor an INTERFACE on `farSmall` with its number at the witness (ε_δ = 3.9e-5, bound −201.81 against',
        '−201.85); the seat\'s three declared departures stand as correct readings of the kernel against a looser ferry. (2) f3 is',
        'stated with H-STRIP and H-COUNT as hypotheses and its limit printed: the rest is allowed e^L by H-STRIP alone while the',
        'pair grows e^{2δL}, so for δ below ½ the assembly f4 does not close from f3 with H-STRIP alone; f4\'s remaining need',
        '(H-MAX, or an argument that avoids it) priced and not attempted. (3) The kernel lane opened for this act and shuts at',
        'its close.',
        '',
        '**COMPONENT 1 — (d\'), `SIDEExplicitFormula/DecayBound.lean`, new.** p integrations by parts (b524\'s `ibp_step`,',
        'iterated) and (d) give, for g real, C^p, supported in [−L, L], at every complex z:',
        '',
        '```lean',
        head('paperFT_decay'),
        '```',
        '',
        'the ferry\'s form for Re z ≠ 0 (`paperFT_decay_re`), (d) as p = 0 (`paperFT_decay_zero`), and the window through b524\'s',
        'factorisation (`window_decay_re`). `DecayBound` first clean at attempt %s.' % sc['first_clean_decay'],
        '',
        '**COMPONENT 2 — the rest, `SIDEExplicitFormula/RestBound.lean`, new.** For an abstract zero configuration, under the',
        'named hypotheses `HStrip` (real parts in (0, 1)) and `HCount` (the kernel\'s local count, with multiplicity), the sum of',
        'm_ρ·‖k̂(γ_ρ)‖ over the zeros outside the pair\'s orbit {ρ₀, 1 − ρ̄₀, ρ̄₀, 1 − ρ₀} is at most `restR`:',
        '',
        '```lean',
        head('rest_bound'),
        '```',
        '',
        '`restR γ₀ φ L A₀` = 768·A₀·A²·e^L·(γ₀² + 1)²·Σ_m (1 + |m|)^(−3), A = ∫|cos(γ₀·)φ| + ∫|(cos(γ₀·)φ)⁗|, p fixed at 4, the',
        'window\'s own order. The orbit, not the two zeros the ferry names, is excluded: k̂ is even, so for a configuration symmetric',
        'under conjugation the conjugates carry the pair\'s own terms; the bound never uses the exclusion, and `finite_rest_bound`',
        'bounds every finite set of zeros by the same R. **Two corollaries, ungraded, the author\'s to rule:** `rest_bound_closed`',
        '— H-STRIP is not needed, the closed strip being a field of every `ZeroConfig`; `rest_bound_zeta` — for `zetaZeroConfig`',
        'no hypothesis at all, H-COUNT being the kernel\'s proved `zetaZeroConfig_local_count`. It bounds a sum over zeta\'s zeros',
        'by the kernel\'s own count and says nothing about their real parts beyond the strip. `RestBound` first clean at attempt %s.'
        % sc['first_clean_rest'],
        '',
        '**COMPONENT 3 — the comparison, printed.** `realizedGrowth_le_exp`: G ≤ e^{δL} (φ ≥ 0 on [−L, L]), so the pair grows at',
        'most like e^{2δL} against the rest\'s e^L; `two_delta_lt_one`: δ < ½ gives 2δ < 1; `f4_needs δ` — e^L ≤ C·e^{2δL} for all',
        'large L — fails for every δ < ½ (`not_f4_needs`) and holds for δ ≥ ½ (`f4_needs_of_half_le`). The ferry\'s lower bound',
        '"G at least e^{δL} times the edge fraction" is not compiled; measured, G/e^{δL} = %.4f at a = 34. **At Q0\'s order-7' % VA.get('G_over_exp', 0),
        'B-spline, a = 34:** A = %.4e, A₀ = %.1f measured on the bank below 150 (NOT PROVED for Q0), R = %.4e; the measured'
        % (VA.get('windowA', 0), VA.get('A0_measured', 0), VA.get('R', 0)),
        'rest (%d banked terms below 150 outside the orbit) %.3f; **R / rest = %.3e**; the pair\'s orbit %.3f, R / pair = %.3e;'
        % (VA.get('rest_terms', 0), VA.get('rest_measured', 0), VA.get('ratio_R_rest', 0), VA.get('pair_orbit_abs', 0), VA.get('ratio_R_pair', 0)),
        'e^L = %.2f against e^{2δL} = %.2f, 2δ = %.5f.' % (VA.get('exp_L', 0), VA.get('exp_2dL', 0), VA.get('two_delta', 0)),
        '',
        '**COMPONENT 4 — f4\'s remaining need, priced, not attempted.** (A) `HMax Z` — a zero of maximal real part, the',
        'supremum of real parts attained — stated as a Prop, its status UNKNOWN in the kernel and in the record. (B) Without',
        'H-MAX: with δ* the supremum of Re ρ − ½, every zero has |Re ρ − ½| ≤ δ*, so the rest is allowed e^{2δ*L}; a sequence ρ_n',
        'with δ_n → δ* (Mathlib\'s `exists_seq_tendsto_sSup`, FOUND) gives pairs growing e^{2δ_n L}, with the width L_n chosen so',
        'that (δ* − δ_n)L_n → 0 against the count at height γ_n (`zetaZeroConfig_local_count`, FOUND); the rest bound with ½',
        'replaced by δ* (this act\'s `finite_rest_bound` with its strip argument widened) ABSENT as a compiled statement; the',
        'pair\'s lower bound with its L-dependence (slope, G, A) controlled uniformly along the sequence ABSENT.',
        '',
        '**COMPONENT 5 — the table.** `AxiomCheckRest.lean` prints %d theorems, %d the standard three on the whole string. Grade'
        % (len(std), sum(1 for v in std.values() if v)),
        'by statement-read: `rest_bound` DERIVES of its model statement under the two named hypotheses H-STRIP and H-COUNT.',
        '**`W-ORD-WEIL-CONVERSE`\'s table, re-printed here with f3 marked:**',
        '',
        '| lemma | state |',
        '|:--|:--|',
        '| (d) | DONE at b517; (d\') at b530 |',
        '| (f1) | DONE at b524 |',
        '| (f2) | b529: Components 1 and 2 DERIVES; Component 3 INTERFACES on `farSmall` |',
        '| (f3) | b530: DERIVES under H-STRIP and H-COUNT (`rest_bound`) |',
        '| (f4) | OPEN; (A) H-MAX, UNKNOWN; (B) the sequence route, two lemmas ABSENT |',
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s. **The kernel lane shuts at'
        % (w(sc['n1']), w(sc['n2']), w(sc['n3']), w(sc['n4']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        'this act\'s close.** The kernel is not tagged; nothing at Zenodo written; nothing deposits; no grade moved on any other',
        'row; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.',
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
    io.open(os.path.join(D, 'b530_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
