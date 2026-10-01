# -*- coding: utf-8 -*-
"""b582_record.py -- THE ACT'S RECORD TOOL, UNDER (R192). ### ONE SUBCOMMAND PER BANK.

### ### b582: LANE THREE, ACT TEN -- CP-7 ACT SEVEN, THE EDITION OF GRH_CASCADE, THE CHI PAGE AS ITS SPINE; THE NO-CHAIN RULE
### STANDING. Subcommands write only `data/b582_*` unless the docstring names another file. Every bank is written through
### `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes no platform call. ### The template
### is b581_record.py.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c2be09f'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/spectral/GRH_CASCADE.md'
ED = 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
CHI_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
WL = 'data/b558_editions/GRH_CASCADE.txt'
SE = 'D:/SIDE-effects'
GT = 'D:/SIDE-grh-transfer'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE QUESTION BEFORE THE SEAL NAMED THE FOOTER`S LINE AS :396; the footer "Kernels audited at" is the current version`s :395 '
    '(its :396 is blank). The author answered on the footer`s text, which the question quoted whole; the correction is made at :395 '
    'and every bank names :395.',
    '(b) THE SAME QUESTION LISTED THREE HEADINGS IN THE CEILING`S REACH AND MISSED A FOURTH: :149 "Landau-Siegel Zeros Excluded". '
    'The author`s answer reaches "every over-ceiling phrase"; :149 is corrected under it like :117, :167 and :240, and the record '
    'names it for the author.',
    '(c) TWO ARMS OF THE SUITE`S FIRST RUN WERE NARROWER THAN THE EDITION THEY READ: G-CEILING-CORRECTIONS required each v0.3.5 '
    'wording to be absent from its line, and :149`s correction keeps its heading`s words with the condition appended; '
    'G-RULED-REWRITES looked for "occurs, T2" and :381`s row writes "Compiled, T2: ... occurs". Both predicates were corrected '
    'in the uncommitted suite (the old wording may occur only inside the new; "a Prop in which no character occurs" and "T2" '
    'both present), no bank and no corpus byte changed, and the suite re-run.',
]


def defects():
    put_txt('b582_defects.txt', ['### b582 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [221, 222, 224, 225, 230, 237, 238, 245, 246, 247]
READS = [
    ('relay the GRH_CASCADE work-list, whole', RELAY, 'HEAD', WL, list(range(1, 56))),
    ('PLACE-papers GRH_CASCADE, its head and Status block', PP, PRE_PP, CUR, list(range(1, 46))),
    ('PLACE-papers GRH_CASCADE, the marked, reading and fact lines', PP, PRE_PP, CUR, [123, 141, 143, 260, 262, 264, 381, 382, 385, 388, 393, 395]),
    ('PLACE-papers GRH_CASCADE, its provenance, annotations, tier block and superseding line', PP, PRE_PP, CUR, list(range(401, 470))),
    ('PLACE-papers the chi page at the mirror`s pin, its pin line, nodes 1, 6, 12, 15 and the open line', PP, MIRROR_PIN, CHI_PAGE, [3, 5, 10, 16, 19, 24, 26]),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 7, 8 and the mellin row', PP, MIRROR_PIN, PAGE, [3, 11, 12, 31, 138]),
    ('relay the CP-1b bank, its head and the GRH_CASCADE rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('relay the b555 tier bank, the composite, its Prop, silence_universal`s premise, and the rows', RELAY, 'HEAD', 'data/b555_tiers.txt',
     [20, 21, 22, 23, 25, 27, 28, 31, 115, 116, 195, 196, 219, 220, 227, 228, 288, 289, 290, 294]),
    ('relay the b555 shells bank', RELAY, 'HEAD', 'data/b555_shells.txt', [3, 5, 6, 7]),
    ('relay the b555 ferry, the shells line', RELAY, 'HEAD', 'data/b555_ferry.txt', [95, 96, 97]),
    ('PLACE-papers OPEN_TRAILS, W-ORD-GRH-WEIL and its closing', PP, PRE_PP, 'OPEN_TRAILS.md', [11373, 11780, 11794, 11796, 11798, 11800, 11802]),
    ('PLACE-papers OPEN_TRAILS, the form and its clauses', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 11884, 11902, 11904, 11906, 11908, 11930, 11932,
                                                                                         11934, 11954, 11956, 11958]),
    ('PLACE-papers FINDINGS, b581`s entry', PP, PRE_PP, 'FINDINGS.md', [6546]),
    ('PLACE-papers README, the ceiling', PP, PRE_PP, 'README.md', list(range(104, 122))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b581`s closing push-out, its head', RELAY, 'HEAD', 'data/b581_closing_push_out.txt', list(range(1, 4))),
]
PINS = (('SIDE-kernel', 'v1.2', 'b1407b2'), ('SIDE-kernel', 'v1.5', '0e5233f'), ('SIDE-lv-conservation', 'v0.5.0', '1767bd6'),
        ('SIDE-lv-conservation', 'v0.5.1', 'bc4751e'), ('SIDE-lv-conservation', 'v0.6.0', 'c80bdc2'), ('SIDE-lv-conservation', 'v0.7.0', '2d86182'),
        ('SIDE-grh-transfer', 'v0.5.0', '858cbf6'), ('SIDE-bsd-formation-transfer', 'v0.1.0', '7425d73'),
        ('SIDE-yang-mills-formation', 'v0.1.0', '79e4f45'), ('SIDE-explicit-formula', 'v0.13', 'ac157c1'),
        ('SIDE-explicit-formula', 'v0.14', '4dce7b9'), ('SIDE-explicit-formula', 'v0.15', '21c8c52'))
SHELLS = ('grh_exclusion', 'no_ls_zero')


def _peel(repo, tag):
    p = 'D:/' + repo
    loc = g(p, 'rev-parse', tag + '^{}').strip()
    peeled = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
    rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s' % tag).split(NL) if l.strip()]
    return loc, (peeled or rem or [''])[0]


def reads():
    L = ['b582 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### the fact clause`s read over GRH_CASCADE`s pins, each tag peeled locally and at the remote:')
    for repo, tag, cited in PINS:
        loc, r = _peel(repo, tag)
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, cited, loc[:7], r[:7],
                                                                   'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    loc, r = _peel('SIDE-grh-transfer', 'v0.5.0')
    L += ['### the one DIFFER, read: SIDE-grh-transfer`s footer pin `858cbf6` against its tag v0.5.0 (peeled %s local, %s remote)' % (loc[:7], r[:7]),
          '    git describe --tags 858cbf6 : %s' % g(GT, 'describe', '--tags', '858cbf6').strip(),
          '    commits v0.5.0..858cbf6 : %s ; v0.5.0 an ancestor of 858cbf6 : %s' % (
              g(GT, 'rev-list', '--count', 'v0.5.0..858cbf6').strip(),
              'yes' if subprocess.run(['git', '-C', GT, 'merge-base', '--is-ancestor', 'v0.5.0', '858cbf6']).returncode == 0 else 'no'),
          '    files changed v0.5.0..858cbf6 : %s' % [x for x in g(GT, 'diff', '--name-only', 'v0.5.0', '858cbf6').split(NL) if x.strip()],
          '    .lean files changed : %d' % len([x for x in g(GT, 'diff', '--name-only', 'v0.5.0', '858cbf6').split(NL) if x.endswith('.lean')])]
    L.append('### the empty reading, (R192)(4) on GRH.grh_exclusion and LandauSiegel.no_ls_zero:')
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR))
    L.append('    GRH_CASCADE @ %s : hits for %s : %d' % (PRE_PP, list(SHELLS) + ['LandauSiegel.', 'GRH.grh', 'Structural.lean'],
                                                     sum(cur.count(x) for x in list(SHELLS) + ['LandauSiegel.', 'GRH.grh', 'Structural.lean'])))
    for pin in ('c66f3c5', 'a27415d', 'HEAD'):
        hits = [l for l in g(SE, 'grep', '-n', '-e', SHELLS[0], '-e', SHELLS[1], pin, '--', 'SIDEEffects/Structural.lean').split(NL) if l.strip()]
        L.append('    SIDE-effects %s (%s) Structural.lean :' % (pin, g(SE, 'rev-parse', '--short=7', pin).strip()))
        L += ['        %s' % h.split(':', 1)[1][:200] for h in hits]
    put_txt('b582_reads.txt', L)


# ================================================================================ COMPONENT 1
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
B581_ENTRY = '## CP-7, act six: the edition of THE_UNCONDITIONAL_SURROUND'
B581_TRAIL = '### b581 — lane three, act nine under (R191)'
NOCHAIN_TEXT = ('the suite is not chained after a push in the same command; a push is read back before any suite run; a pre-push bank '
                'overwritten by a failed chain is restored from HEAD and the restoration printed')


def c1_lines():
    """### PLACE-papers FINDINGS (b581's weight) and OPEN_TRAILS (the two carried sentences confirmed; the no-chain rule standing)."""
    Q = _Q()
    form, entry, trail = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.FIND, B581_ENTRY), Q.line_of(Q.OT, B581_TRAIL)
    if not (form == 11864 and entry == 6546 and trail == 11958):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s entry %s trail %s -- NOTHING WRITTEN' % (form, entry, trail))
    heads = dict(
        weight='*Appended 2026-10-01 by b582 to b581’s entry (:%d), under `(R192)`(1) -- b581 AT ITS WEIGHT:*' % entry,
        carried='*Appended 2026-10-01 by b582 to b581’s record (:%d), under the author’s ruling `(R192)`(2) -- THE TWO CARRIED SENTENCES, CONFIRMED AS READ:*' % trail,
        nochain='*Appended 2026-10-01 by b582 to b581’s record (:%d), under the author’s ruling `(R192)`(3) -- THE NO-CHAIN RULE, STANDING:*' % trail,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = [Q.append_to(Q.FIND, '\n%s `phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md` beside v0.4 unedited: 10 rows as 8 sentences '
                                 'citing the zeta page or the bank lines (CP-1b :190, census :23); the surround’s witness standing at its pin, '
                                 'the peeled tag at the remote; the two b450 credits after :137 citing SIGN_ARRANGEMENT_RECONCILIATION by line '
                                 'and the CP-1b :178 credit after the Correspondence table; one stem correction (:187), three ceiling '
                                 'corrections (:23 twice, :179), no fact correction (13 pins agree with their tags); the version line; the '
                                 're-pin last. H28a, H28b (+4 against 4) and H28c held; (N1)-(N5) held. AMC v0.2.4 :293 and :366 corrected by '
                                 'the fact clause to the SIDE-effects toolchain and Mathlib its manifest prints at both pins; PATHS v0.7’s '
                                 'superseding line beneath its section. The fact clause at OPEN_TRAILS :11954, the placement clause at :11956. '
                                 'The suite reads 69 of 69.\n' % heads['weight'])]
    out.append(Q.append_to(Q.OT, '\n%s v0.4 :33 states the reduction the document marks manuscript-resident at its :183, and carries; '
                                 'v0.4 :165 is a negation, and carries. The new archimedean-sign credit beside b454’s annotation at v0.4 :203 is '
                                 'the intended arrangement -- the credit at the claim, the annotation where the era left it.\n' % heads['carried']))
    out.append(Q.append_to(Q.OT, '\n%s %s. Entered as the seat wrote it at b581’s closing (relay `data/b581_closing.txt`, defect (c)).\n'
                                 % (heads['nochain'], NOCHAIN_TEXT)))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b582_c1_lines.json', dict(form=form, entry=entry, trail=trail, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`', 'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`',
       'h2_sign_chi_iff_grh_chi': 'v0.14 = `4dce7b9`', 'EF_lit_chi_holds': 'v0.13 = `ac157c1`', 'h2_sign_cfg_iff_target': 'v0.15 = `21c8c52`',
       'GRH_chi': 'v0.6 = `de1f175`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321', 'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth', 'h2_sign_chi_iff_grh_chi': 'GRHWeil',
      'EF_lit_chi_holds': 'GRHWeil', 'h2_sign_cfg_iff_target': 'Schema', 'GRH_chi': 'GRHWeil'}
WHERE = {'h2_sign_iff_rh': 'the zeta page, node 8, line 12', 'ch_iff_rh': 'the zeta page, node 7, line 11',
         'mellin_Phi_eq_zero_of_re_le_one': 'the zeta page, Correspondence row, line 138 (the page`s pin)',
         'h2_sign_chi_iff_grh_chi': 'the chi page, node 12, line 16', 'EF_lit_chi_holds': 'the chi page, node 6, line 10',
         'h2_sign_cfg_iff_target': 'the chi page, node 15, line 19', 'GRH_chi': 'the chi page, node 1, line 5'}
CHI_DECLS = ('h2_sign_chi_iff_grh_chi', 'EF_lit_chi_holds', 'h2_sign_cfg_iff_target', 'GRH_chi')
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the ζ page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
HCHI = '`h2_sign_chi_iff_grh_chi`, %s %s' % (EF, PIN['h2_sign_chi_iff_grh_chi'])
EFC = '`EF_lit_chi_holds`, %s' % PIN['EF_lit_chi_holds']
CFG = '`h2_sign_cfg_iff_target`, %s' % PIN['h2_sign_cfg_iff_target']
GC = '`GRH_chi`, %s' % PIN['GRH_chi']
CHIP = '`%s`' % CHI_PAGE
CPB = 'relay `data/b558_cp1b.txt` :%s'
TIERS = 'relay `data/b555_tiers.txt` :%s'
TD = '`IsEmpty TypeD` over the programme’s own couplings, T2 whatever its profile (b557’s superseding line, `(R167)`(1), %s)'
COMP = 'whose conclusion `GRHStructuralExhaustiveness χ χbar` is a Prop in which no character occurs, T2 (%s)' % (TIERS % '20-:23')

REWRITES = [
    (38, 'the structural exclusion is genuine in `SIDE-effects` `Phase15/Module1.lean : no_type_d_conspiracies` (CRT exhaustiveness);',
     'the structural exclusion is compiled, programme-type, in `SIDE-effects` `Phase15/Module1.lean : no_type_d_conspiracies` (CRT '
     'exhaustiveness), which states %s;' % (TD % (CPB % '221'))),
    (43, 'reduces to a single carried-open premise — `h2`, realization-totality at the ξ interface — carried openly:',
     'reduces to a carried-open premise for each instance — at ζ `h2_sign`, equivalent to RH (%s), and at each primitive χ ≠ 1 Weil '
     'positivity for χ, equivalent to `GRH_chi` (%s, its explicit formula %s, both instances of %s, as the χ page %s at PLACE-papers '
     '`%s` prints them) — carried openly:' % (H2, HCHI, EFC, CFG, CHIP, MIRROR_PIN)),
    (43, 'while `h2` is the criterion the whole cascade rests on, exactly as RH itself does.',
     'while the open node is %s per primitive χ, by the compiled equivalence the same open statement as Weil positivity for χ, exactly '
     'as `h2_sign` is RH itself.' % GC),
    (141, 'transported to $L(s, \\chi)$ by the character-insensitivity argument — no off-line zero exists.',
     'transported to $L(s, \\chi)$ by the character-insensitivity argument — the argument concludes that no off-line zero exists, and '
     '`silence_universal` is compiled under the programme’s own premise `I.is_universal`, T2-INTERFACES (%s), so the conclusion rests on '
     'a premise the programme has still to establish.' % (CPB % '224')),
    (141, 'and closes under the shared witness (`T3.T3prime_shared_witness`);',
     'and closes under the shared witness (`T3.T3prime_shared_witness`) only through lv’s `h2` at Φ, `mellin Φ (s/2) ≠ 0`, false at every '
     's with re s ≤ 1 (%s), so on the strip it closes nothing;' % MP),
    (143, 'What stays open at this edge is `h2` alone — realization-totality at the ξ interface — carried openly.',
     'What stays open at this edge is the clause itself: lv’s `h2` at Φ is false at every s with re s ≤ 1 (%s), so the goal state closes '
     'nothing on the strip, and the open nodes are `h2_sign`, equivalent to RH (%s), and at each primitive χ ≠ 1 `GRH_chi`, equivalent to '
     'Weil positivity for χ (%s, %s) — carried openly.' % (MP, H2, HCHI, CHIP)),
    (262, '— genuine additive–multiplicative conspiracy exclusion:',
     '— the additive–multiplicative conspiracy exclusion over the programme’s own couplings, programme-type, T2 whatever its profile '
     '(b557’s superseding line, `(R167)`(1), %s, :238):' % (CPB % '237')),
    (388, '| **DERIVES** — the modular-conversion discharge landed at `a27415d` (W-4).',
     '| **DERIVES** its own statement, %s — the modular-conversion discharge landed at `a27415d` (W-4).' % (TD % ((CPB % '245') + ', :246'))),
    (393, '| **DERIVES** at `a27415d` — same terminal as the conspiracy-exclusion row above;',
     '| **DERIVES** at `a27415d` its own statement, %s — same terminal as the conspiracy-exclusion row above;' % (TD % (CPB % '247'))),
]
# ### the readings of (R192)(4) on sentences the work-list does not mark: the composite says what it concludes; silence_universal
# ### names its premise
RULED = [
    (123, 'is verified in `SIDE-grh-transfer` (`grh_structural_exhaustiveness_proved`).',
     'is compiled in `SIDE-grh-transfer` as `grh_structural_exhaustiveness_proved`, %s.' % COMP),
    (260, 'and `grh_structural_exhaustiveness_proved`;', 'and `grh_structural_exhaustiveness_proved`, %s;' % COMP),
    (264, 'and universal Silence (`silence_universal`);',
     'and universal Silence (`silence_universal`, compiled under the programme’s own premise `I.is_universal`, T2-INTERFACES, %s);' % (TIERS % '25')),
    (381, '| DERIVES — Compiled; structural-exhaustiveness analog; full Mathlib-GRH bridge open.',
     '| DERIVES — Compiled, T2: its conclusion `GRHStructuralExhaustiveness χ χbar` is a Prop in which no character occurs (%s); '
     'structural-exhaustiveness analog; full Mathlib-GRH bridge open.' % (TIERS % '20-:23')),
]
RA = 'the programme’s RH argument'
CEILS = [
    (49, 'The Riemann Hypothesis — established in the monograph and verified at the architecture level in SIDE-kernel',
     'The programme’s RH argument — set out in the monograph, its architecture compiled in SIDE-kernel'),
    (49, 'yielding the **Generalized Riemann Hypothesis** (GRH).', 'yielding the programme’s argument for the **Generalized Riemann Hypothesis** (GRH).'),
    (49, 'The cascade continues: no Landau-Siegel zeros', 'The cascade continues, conditional on GRH: no Landau-Siegel zeros'),
    (49, 'Artin\'s primitive root conjecture becomes unconditional;', 'Artin\'s primitive root conjecture stands, Artin conditional on GRH;'),
    (49, 'that establishes the Riemann Hypothesis itself.', 'of %s itself.' % RA),
    (55, 'The claims stand as stated;', 'The claims stand as the programme’s argument states them;'),
    (57, 'The Riemann Hypothesis is the foundational result.', 'The programme’s RH argument is the foundational step.'),
    (57, 'The cascade extends RH through', 'The cascade extends %s through' % RA),
    (59, '**(1) RH** (kernel-verified).', '**(1) RH** (the programme’s argument, its open clause `h2_sign` equivalent to RH by %s).' % H2),
    (59, 'All non-trivial zeros of $\\zeta(s)$ lie', 'The statement: all non-trivial zeros of $\\zeta(s)$ lie'),
    (59, 'The proof: SIDE Exclusion', 'The programme’s argument: SIDE Exclusion'),
    (59, 'verifies this at the architecture level:', 'compiles this argument’s architecture, its Route 3 clause RH restated (%s, E-2026-09-25-1):' % CH),
    (61, 'All non-trivial zeros of every Dirichlet', 'The statement: all non-trivial zeros of every Dirichlet'),
    (61, 'The proof: the same seven', 'The programme’s argument: the same seven'),
    (63, '**(3) Landau-Siegel zeros excluded.** No real zero', '**(3) Landau-Siegel zeros excluded, conditional on GRH.** The statement: no real zero'),
    (63, 'The proof: a Landau-Siegel zero', 'The programme’s argument: a Landau-Siegel zero'),
    (65, '** (unconditional).', '** (conditional on GRH).'),
    (65, 'With GRH established, Artin\'s conjecture becomes unconditional.', 'With GRH open, Artin\'s conjecture stays conditional on it.'),
    (67, '(unconditional).**', '(conditional on GRH).**'),
    (111, 'Every step of the RH proof', 'Every step of %s' % RA),
    (113, 'propagates the entire RH proof structure to GRH.', 'propagates the entire structure of %s to GRH.' % RA),
    (117, '## III. The Structural Proof of GRH', '## III. The Structural Argument for GRH'),
    (119, 'The proof of GRH via SIDE Exclusion follows the same architecture as the RH proof,',
     'The programme’s GRH argument via SIDE Exclusion follows the same architecture as %s,' % RA),
    (145, 'All non-trivial zeros of $L(s, \\chi)$ lie on', 'The programme’s argument concludes that all non-trivial zeros of $L(s, \\chi)$ lie on'),
    (145, 'GRH holds for every Dirichlet character $\\chi$.', 'The programme’s GRH argument concludes GRH for every Dirichlet character $\\chi$.'),
    (145, 'the same proof works for every', 'the same argument works for every'),
    (149, '## IV. Landau-Siegel Zeros Excluded', '## IV. Landau-Siegel Zeros Excluded, Conditional on GRH'),
    (163, 'is closed by the GRH result itself:', 'would be closed by GRH itself, which is open:'),
    (167, '## V. Artin\'s Primitive Root Conjecture (Unconditional)', '## V. Artin\'s Primitive Root Conjecture (Conditional on GRH)'),
    (175, 'with GRH established the implication is unconditional.', 'with GRH open, Artin stays conditional on it.'),
    (179, 'With GRH proved, the conjecture closes.', 'With GRH open, the conjecture stays open.'),
    (203, 'that establish RH.', 'of %s.' % RA),
    (207, 'No mechanism produces off-line zeros for', 'In the programme’s argument, no mechanism produces off-line zeros for'),
    (211, 'These four facts together close the cascade.', 'These four facts together close the cascade in the programme’s argument.'),
    (211, 'RH proves;', 'The programme’s RH argument concludes RH;'),
    (211, 'Hooley\'s implication becomes unconditional (classical reduction);', 'Hooley\'s implication leaves Artin conditional on GRH (classical reduction);'),
    (213, 'that establishes the foundational result.', 'of %s.' % RA),
    (240, '### VIII.3 Load-bearing claims established here', '### VIII.3 Load-bearing claims argued here'),
    (242, '(1) **GRH holds for every Dirichlet character $\\chi$**,', '(1) **The programme’s GRH argument concludes GRH for every Dirichlet character $\\chi$**,'),
    (242, 'The proof is character-uniform:', 'The argument is character-uniform:'),
    (244, '(2) **No Landau-Siegel zero exists for any $L(s, \\chi)$.**', '(2) **No Landau-Siegel zero exists for any $L(s, \\chi)$, conditional on GRH.**'),
    (246, '(3) **Artin\'s primitive root conjecture is unconditional.**', '(3) **Artin\'s primitive root conjecture is conditional on GRH.**'),
    (258, '— RH proof core.', '— RH-core.'),
    (288, '— RH proof core.', '— RH-core.'),
    (310, 'by the same argument that establishes RH for $\\zeta(s)$,', 'by the same argument as %s for $\\zeta(s)$,' % RA),
    (310, 'The proof does not require', 'The argument does not require'),
    (312, '**The classical implications of GRH become unconditional.**', '**The classical implications of GRH stay conditional on it.**'),
    (316, 'the Riemann Hypothesis is not an isolated result but a foundational structural fact',
     '%s is not an isolated argument but a foundational structure' % RA),
    (316, 'is not just RH;', 'is not just its RH argument;'),
    (344, '— RH proof core;', '— RH-core;'),
]
HEADINGS = (117, 149, 167, 240)
FACTS = [(395, 'SIDE-grh-transfer `858cbf6` (v0.5.0);',
          'SIDE-grh-transfer `858cbf6` (v0.5.0 = `bfd2af7` plus one commit, no `.lean` file changed);')]
# ### the ceiling-shaped sentences the seat read and carried, by the current version's line: hedged, true, a dated history entry,
# ### or the tier block (R192)(4) keeps
CARRIED = {
    25: 'conditional: “once GRH is established”',
    35: 'the analog, not GRH: the structural-exhaustiveness analog said compiled in the repository',
    61: 'the analog, not GRH: “(structural-exhaustiveness analog kernel-verified …)”, its first sentence',
    65: 'true: Hooley (1967) proved the implication GRH ⇒ Artin',
    141: 'the class exclusions as compiled: “no mechanism class produces an off-line zero”, its first sentence',
    159: 'hedged: “a classical reduction that inherits the open piece of GRH”',
    161: 'conditional: “once GRH places every non-trivial zero …”; “a corollary of the GRH result (an open reconciliation …)”',
    171: 'true: Hooley proved GRH ⇒ Artin; “the proof” is Hooley’s',
    173: 'hedged: “at the structural-exhaustiveness level … the full Mathlib-GRH bridge still open … to the extent GRH is established”',
    306: 'RH named as a node, not asserted',
    312: 'conditional and hedged after its corrected head: “once GRH is established”, “to the degree GRH is established”',
    405: 'a dated history entry (v0.3.5), carried under the history clause',
    415: 'a dated history entry (v0.3), carried under the history clause',
}
NAMES = [(39, 'the Yang-Mills problem’s own name and a retired stub’s name, 3 uses'), (268, 'the Yang-Mills problem’s own name and a retired stub’s name, 3 uses'),
         (392, 'the Yang-Mills problem’s own name, 2 uses'), (415, 'the Yang-Mills problem’s own name, 1 use, in a dated history entry')]
VERSION = (19, '*v0.3.6 — 2026-10-01*')
ASSIGN = {'GRH:43:169': 1, 'GRH:143:177': 1, 'GRH:141:171': 2}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) the chi-side as the open piece, rewritten to what landed',
                2: '(c) silence_universal names its premise'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|[Tt]he proof\b|same proof\b|is a proof\b|GRH (?:is )?established|'
                     r'becomes? unconditional|is unconditional|\([Uu]nconditional\)|kernel-verified\)\.')
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
BM_TAG = '<!-- b582 (R192) THE v0.3.6 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b558_cp1b.txt', 221), ('b558_cp1b.txt', 224), ('b558_cp1b.txt', 237), ('b558_cp1b.txt', 245), ('b558_cp1b.txt', 247),
            ('b555_tiers.txt', 20), ('b555_tiers.txt', 25))


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'GRH' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :19 (the version line and a blank)."""
    return n + (2 if n >= VERSION[0] else 0)


OFFSET = ('+2 from :19 (the v0.3.6 version line and a blank, above the v0.3.5 version line); no other insertion -- v0.3.5 :n sits at the '
          'edition`s :n+2 for n >= 19')


def _all_changes():
    return REWRITES + RULED + CEILS + FACTS


def edition(*a):
    """### PLACE-papers phase1.5/spectral/GRH_CASCADE_v0_3_6.md, beside the current version from its blob at c2be09f; the re-pin step
    ### run last over the final body."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE c2be09f -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in _all_changes():
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if cur[VERSION[0] - 1] != '*v0.3.5 — 2026-07-23*':
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=ASSIGN.get(r['id'], 0), cites=cites, banks=banks, supports=r['reading']))
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(i - (2 if i >= VERSION[0] + 2 else 0) for i, _ in hits) - set(CARRIED))
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.3.6 edition -- written 2026-10-01 by b582 under the author’s ruling `(R192)`(4), by the form of `(R187)`(5)',
          '',
          '*This file is v0.3.6 of GRH_CASCADE, the CP-7 edition written beside v0.3.5 (`%s`, unedited) from v0.3.5’s tier block (its :437, '
          'with the superseding line at its :467, both standing) and its CP-1b work-list (relay `%s`), the χ page as its spine and the ζ page '
          'for sentences on ζ; it does not deposit and does not replace v0.3.5, and its promotion is CP-8’s. Every line cited below is this '
          'file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 10 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '',
          'None: the work-list places no CREDIT row and relay `data/b450_batch.json` holds no item for this document.', '',
          '### Rewrites under the readings of `(R192)`(4), sentences the work-list does not mark', '',
          '| this edition’s line | the object | v0.3.6 adds | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in RULED:
        bm.append('| :%d | %s | %s | rewritten under `(R192)`(4) |' % (
            _edl(ln), '`silence_universal`' if 'silence' in old else '`grh_structural_exhaustiveness_proved`',
            'its premise `I.is_universal`, T2-INTERFACES' if 'silence' in old else 'its conclusion, a Prop in which no character occurs, T2'))
    bm += ['', '### Stem corrections', '', 'None: the banned-stem scan of v0.3.5 reads no live use (relay `data/b582_reads.txt`).', '',
           '### Names and titles excepted', '', '| this edition’s line | the use | Status |', '|:--|:--|:--|']
    for ln, what in NAMES:
        bm.append('| :%d | %s | excepted under the name-and-title exception, carried |' % (_edl(ln), what))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.3.5 wording | v0.3.6 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause%s |' % (_edl(ln), CEIL_RECORD, old, rep,
                                                                                 ', a heading' if ln in HEADINGS else ''))
    bm += ['', '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | %s %s | carried as read |' % (_edl(ln), CARRY_RECORD, CARRIED[ln]))
    bm += ['', '### Fact corrections', '', '| this edition’s line | v0.3.5 wording | v0.3.6 wording | the printed fact | Status |', '|:--|:--|:--|:--|:--|']
    for ln, old, rep in FACTS:
        bm.append('| :%d | %s | %s | SIDE-grh-transfer tag v0.5.0 peels to `bfd2af7` locally and at the remote; `858cbf6` is one commit past '
                  'it, changing logs and `.gitignore` only (relay `data/b582_reads.txt`) | corrected under the fact clause |' % (_edl(ln), old, rep))
    bm += ['', '### The readings of `(R192)`(4) with no sentence to write', '',
           '| object | the read | Status |', '|:--|:--|:--|',
           '| `GRH.grh_exclusion`, `LandauSiegel.no_ls_zero` | cited by no sentence of v0.3.5; at SIDE-effects `c66f3c5` theorems over opaque '
           'Props, at `a27415d` and HEAD retired to comments (`Structural.lean` :79, :84; relay `data/b582_reads.txt`) | no object, nothing written |',
           '| `twisted_balance_at_unramified_prime` | its sentences carried at T0 | stands |',
           '| the tier block and the superseding line | v0.3.5 :437 and :467, at this edition’s :%d and :%d | stand |' % (_edl(437), _edl(467)),
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.3.6 | `%s` | written at b582 |' % ED,
           '| the current version, v0.3.5 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (CHI_PAGE, MIRROR_PIN),
           '| the ζ page | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the tier bank | relay `data/b555_tiers.txt` | read |',
           '| the sentence-by-sentence diff | relay `data/b582_edition_GRH.txt` | banked at b582 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    # ### THE RE-PIN STEP, LAST
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the %s | not on a page | cited at :%s of this edition |' % (
            bank, n, 'CP-1b bank (b558)' if bank.startswith('b558') else 'tier bank (b555)', ', :'.join(str(x) for x in at) or '### NONE'))
    bm.append('')
    full = body + bm
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b582_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, ruled=RULED, facts=FACTS, carried={str(k): v for k, v in CARRIED.items()}, names=NAMES,
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                       bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def _chi_sentences(body):
    """### body sentences citing the chi page: naming the page or a chi-page declaration at its pin."""
    out = []
    for i, l in enumerate(body, 1):
        for s in _segs(l):
            if CHI_PAGE in s or any(('`%s`' % d) in s and PIN[d] in s for d in CHI_DECLS):
                out.append(dict(line=i, hchi=('`h2_sign_chi_iff_grh_chi`' in s and PIN['h2_sign_chi_iff_grh_chi'] in s), text=s[:200]))
    return out


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, H28a-H28c."""
    E = jl('b582_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    body = ed[:cut - 1]
    scan = rd('b582_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| :') and (CEIL_RECORD in l or CARRY_RECORD in l))
                    else 'carried' if (i < cut and i in carried_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 20]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == 0 and clean and not beyond) else 'REFUTED'
    chi = _chi_sentences(body)
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b582 -- COMPONENT 2: THE EDITION OF GRH_CASCADE, (R192)(4), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :19 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[18]),
         '### its tier block : :437 "%s"' % cur0[436][:110],
         '### its superseding line : :467 "%s"' % cur0[466][:110],
         '### its version history : the Provenance entries v0.3.5 (:405), v0.3.4 (:407), v0.3.3 (:409), v0.3.2 (:411), v0.3.1 (:413), v0.3 (:415)',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE READINGS OF (R192)(4) AGAINST THIS DOCUMENT: (a) the chi-side as the open piece -- 2 rows (:43, :143), rewritten to '
         'EF_lit_chi_holds (v0.13), h2_sign_chi_iff_grh_chi (v0.14) and h2_sign_cfg_iff_target (v0.15), the open node GRH_chi per chi ; '
         '(b) grh_structural_exhaustiveness_proved -- no work-list row; its 3 sentences (:123, :260, :381) rewritten ; (c) silence_universal '
         '-- 1 row (:141) and 1 unmarked sentence (:264) ; (d) grh_exclusion / no_ls_zero -- no object (0 hits; the kernel read in '
         'data/b582_reads.txt) ; (e) twisted_balance_at_unramified_prime -- carried ; (f) :437 and :467 -- carried', '',
         '### THE WORK-LIST, ROW BY ROW (10 rows, 8 sentences, 7 lines) -- each row: v0.3.5`s line and the edition`s, the terminal, the '
         'reading (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v0.3.5 :%d -> v0.3.6 :%d `%s` -- %s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                     ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                     (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.3.5 : %s' % d['old'], '      v0.3.6 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N1) COVERAGE BY THE READINGS OF (R192)(4), the seat`s hand-read: %d of %d rows -- (a) %d, (c) %d ; uncovered %s, resolved by the form'
          % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']), sum(d['reading'] == 2 for d in E['diff']),
             [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]), '',
          '### THE RULED REWRITES (readings (b), (c), sentences the work-list does not mark):']
    L += ['    v0.3.5 :%d -> v0.3.6 :%d  "%s" -> "%s"' % (r[0], _edl(r[0]), r[1], r[2]) for r in E['ruled']]
    L += ['### THE CEILING CORRECTIONS (%d, on %d lines; %d of them headings):' % (len(E['ceils']), len(set(c[0] for c in E['ceils'])),
                                                                               sum(1 for c in E['ceils'] if c[0] in HEADINGS))]
    L += ['    v0.3.5 :%d -> v0.3.6 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE CEILING-SHAPED SENTENCES READ AND CARRIED (%d lines):' % len(CARRIED)]
    L += ['    v0.3.5 :%d -> v0.3.6 :%d  %s' % (n, _edl(n), CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE FACT CORRECTIONS (%d):' % len(E['facts'])]
    L += ['    v0.3.5 :%d -> v0.3.6 :%d  "%s" -> "%s" ; source: the peeled tag, local and remote, and the one commit past it, printed in '
          'data/b582_reads.txt' % (f[0], _edl(f[0]), f[1], f[2]) for f in E['facts']]
    L += ['### NAMES AND TITLES EXCEPTED (the name-and-title exception):'] + ['    v0.3.5 :%d -> v0.3.6 :%d  %s' % (n, _edl(n), w) for n, w in NAMES]
    L += ['### THE VERSION LINE: above v0.3.5 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### CREDIT LINES: none. ### HISTORY LINES: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: the version '
          'line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CHI PAGE, CITED BY %d BODY SENTENCES (%d of them h2_sign_chi_iff_grh_chi at its pin):' % (len(chi), sum(c['hchi'] for c in chi))]
    L += ['    :%d %s %s...' % (c['line'], '[h2_sign_chi_iff_grh_chi]' if c['hchi'] else '', c['text'][:150]) for c in chi]
    L += ['', '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b582_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on a page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b582_edition_GRH.txt', L)
    put_json('b582_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   chi=chi, n_ceils=len(E['ceils']), n_ceil_lines=len(set(c[0] for c in E['ceils'])), n_facts=len(E['facts'])))
    H = jl('b582_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'],
          'live', H['live'], 'chi', len(chi), 'ceils', H['n_ceils'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6'}


def scores():
    H, E = jl('b582_h28.json'), jl('b582_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    differ = rd('b582_reads.txt').count('### DIFFER')
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
    nchi, nh = len(H['chi']), sum(c['hchi'] for c in H['chi'])
    S = dict(
        N1=('HELD' if H['covered'] >= 7 else 'REFUTED', 'the readings of (R192)(4) cover %d of the 10 MOVED rows by the seat`s hand-read '
            '(the chi-side reading :43 and :143, silence_universal :141); uncovered %s, resolved by the form' % (H['covered'], H['uncovered'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N3=('HELD' if nchi >= 2 and nh >= 1 else 'REFUTED', '%d body sentences cite the chi page, %d of them h2_sign_chi_iff_grh_chi at v0.14 = 4dce7b9'
            % (nchi, nh)),
        N4=('HELD' if H['n_ceils'] >= 1 and H['n_facts'] == 0 else 'REFUTED', 'the ceiling clause corrects %d phrases on %d lines (its first '
            'half holds); the fact clause finds %d (the footer`s SIDE-grh-transfer pin, :395; reads bank DIFFER lines %d), so its second half '
            'fails' % (H['n_ceils'], H['n_ceil_lines'], H['n_facts'], differ)),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current GRH_CASCADE unedited (%s); PLACE-papers changed at %s' % ('held' if kmain == V015 and heads_ok else '### MOVED',
                                                                                                'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if H['covered'] == 3 and len(H['uncovered']) == 7 else 'REFUTED', '(N1) refuted at 3 of 10; the seven uncovered rows '
            'resolved by the form'),
        S2=('HELD' if n2 and H['body_dn'] == 1 and H['allowed'] == 1 else 'REFUTED', 'H28a-H28c held; the body +1 against 1'),
        S3=('HELD' if nchi >= 2 and nh >= 2 else 'REFUTED', 'the :43 and :143 rewrites both cite h2_sign_chi_iff_grh_chi at its pin'),
        S4=('HELD' if H['n_ceils'] >= 1 and H['n_facts'] == 1 and differ == 1 else 'REFUTED', '(N4) refuted on its second half alone: one '
            'fact correction, :395'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the files changed are the three its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered'], chi=nchi, ceils=H['n_ceils']),
    )
    put_json('b582_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:150]))


TITLE_HEAD = ('## CP-7, act seven: the edition of GRH_CASCADE from its tier block and work-list, the χ-side cited to the Dirichlet page')
TITLE = TITLE_HEAD + '; written as v0.3.6 beside v0.3.5, no sentence held'
TRAIL_HEAD = ('### b582 — lane three, act ten under (R192): CP-7 act seven -- the edition of GRH_CASCADE written beside the current, the '
              'χ page as its spine; the no-chain rule standing')


def records_pp():
    Q = _Q()
    S, H, E, C1 = jl('b582_scores.json'), jl('b582_h28.json'), jl('b582_edition.json'), jl('b582_c1_lines.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b582 on the author’s ruling `(R192)`. Banks: relay `data/b582_edition_GRH.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b582_edition.json`, `data/b582_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R192)`(4)): `%s`, v0.3.6, written beside v0.3.5 (`%s`, unedited) from v0.3.5’s tier block and its CP-1b '
         'work-list, the χ page as its spine. The 10 work-list rows resolve to 8 sentences on 7 lines, each rewritten in place: the open '
         'piece named per instance -- at ζ the clause equivalent to RH, at each primitive χ the χ-criterion equivalent to `GRH_chi`, cited '
         'to the Dirichlet page by name and pin; lv’s goal state said to close nothing on the strip; `silence_universal`’s premise named; '
         'the finite-modulus no-conspiracy said to state the empty conspiracy type over the programme’s own couplings, programme-type. '
         'Three further sentences on the GRH composite say that its conclusion is a Prop in which no character occurs, and one further '
         'sentence names `silence_universal`’s premise, as the ruling reads them. One footer pin is corrected by the fact clause. No '
         'sentence is removed and none held.' % (ED, CUR), '',
         '**A finding of the edition: the ceiling.** GRH_CASCADE’s current version states GRH, RH and the downstream conjectures as '
         'proved or established at %d places on %d lines -- four of them headings -- and the edition brings each to the ceiling, the '
         'object named and the rest of the sentence unchanged; %d further ceiling-shaped sentences, hedged, conditional or true, are read '
         'and carried, each listed in the back matter.' % (H['n_ceils'], H['n_ceil_lines'], len(CARRIED)), '',
         '**The counts.** v0.3.5 %d sentences; v0.3.6 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 10 rows by the readings of `(R192)`(4): %d.' % (H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The record lines** (`(R192)`(1)-(3)): b581’s weight (FINDINGS :%d); the two carried sentences confirmed (OPEN_TRAILS :%d); the '
         'no-chain rule standing (:%d).' % (ln['weight'], ln['carried'], ln['nochain']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R192)`(5): the edition of R_CURVE_CRITERION by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.3.5, README, REGISTRY and both pages unwritten; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R192) ratified.** (1) b581 at its weight. (2) The two carried sentences confirmed as read. (3) The no-chain rule, standing. '
            '(4) The edition of GRH_CASCADE by the form, the χ page as its spine, six readings entered. (5) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b581’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the carried sentences), :%d (the no-chain rule), '
            'this record; PLACE-papers `%s` (created).' % (ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['carried'], ln['nochain'], ED), '',
            '**Answered before the seal, by the author:** the ceiling clause reaches every over-ceiling phrase of the document, sentences and '
            'headings, each taking the object it names, hedged sentences carried as read; the footer’s SIDE-grh-transfer pin corrected by '
            'the fact clause; the reading on `GRH.grh_exclusion` and `LandauSiegel.no_ls_zero` has no object and nothing is written for it.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** the reading on the two Structural.lean shells is the navigator’s, and the read differs from its wording: at '
            'SIDE-effects `c66f3c5` both are theorems over opaque Props (balance → ¬off-line), not `fun _ => True`; at `a27415d` and HEAD both are '
            'retired to comments (`Structural.lean` :79, :84). No seat memory record carries the old wording; it entered at b555’s ferry (relay '
            '`data/b555_ferry.txt` :95-:96). The question before the seal missed one heading in the ceiling’s reach, v0.3.5 :149, corrected under '
            'the answer’s “every over-ceiling phrase” (defect (b)).', '',
            '**Next:** per `(R192)`(5), CP-7 act eight, b583 -- the edition of R_CURVE_CRITERION by the same form, H28a-H28c scored; the '
            'author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b582_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b582_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b582_findings.json')['entry_line'], jl('b582_trail.json')['line'])


def desk():
    S = jl('b582_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b582 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b582_defects.txt').rstrip(NL).split(NL)
    put_txt('b582_desk_notes.txt', L)


def components():
    S, H, C1, fj, tj = (jl('b582_scores.json'), jl('b582_h28.json'), jl('b582_c1_lines.json'), jl('b582_findings.json'), jl('b582_trail.json'))
    ln = C1['lines']
    L = ['b582 -- THE COMPONENTS, BANKED UNDER (R192).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b581`s closing push-out relay eb1301d3 ; push-b581* branches deleted by '
         'name (data/b582_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b581`s weight FINDINGS :%d ; the two carried sentences OPEN_TRAILS :%d ; the no-chain rule :%d' % (
             ln['weight'], ln['carried'], ln['nochain']),
         '### COMPONENT 2 : the edition %s ; 8 sentences rewritten, 4 ruled rewrites, %d ceiling corrections on %d lines, 1 fact correction, '
         'the version line, 0 removals ; data/b582_edition_GRH.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['n_ceils'], H['n_ceil_lines'], H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of R_CURVE_CRITERION ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b582_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b582_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
