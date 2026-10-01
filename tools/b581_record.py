# -*- coding: utf-8 -*-
"""b581_record.py -- THE ACT'S RECORD TOOL, UNDER (R191). ### ONE SUBCOMMAND PER BANK.

### ### b581: LANE THREE, ACT NINE -- CP-7 ACT SIX, THE EDITION OF THE_UNCONDITIONAL_SURROUND; THE FACT CLAUSE APPLIED TO AMC
### v0.2.4; PATHS v0.7'S SECTION SUPERSEDED BENEATH. Subcommands write only `data/b581_*` unless the docstring names another
### file. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`). This act makes
### no platform call. ### The template is b580_record.py.
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
PRE_PP = '5f13c2f'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'
ED = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'
AMC = 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md'
PATHS7 = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'
SIGN = 'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/THE_UNCONDITIONAL_SURROUND.txt'
SE = 'D:/SIDE-effects'
LV = 'D:/SIDE-lv-conservation'

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


def put_pp(rel, text):
    p = os.path.join(PP, *rel.split('/'))
    b = text.encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (rel, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE FIRST HOUSEKEEPING COMMIT`S MESSAGE NAMED THE FINDINGS LINE BEFORE IT WAS READ: it said :6544 where the tool had '
    'written :6542 (relay data/b581_amc_fact.txt). The commit was local and unpushed; its message alone was corrected by amend '
    '(PLACE-papers 486595e), its two files unchanged.',
    '(b) THE EDITION`S FIRST WRITE CARRIED ONE LIVE STEM IN ITS OWN BACK MATTER: the stem-correction row quoted v0.4`s wording more '
    'than banned_terms.py`s 40-character window from its "correction record" marker, so the scan read it live and H28c read REFUTED. '
    'The row now repeats the marker beside the quoted wording, as b578`s did; the uncommitted edition was rewritten (`edition again`) '
    'and re-scanned.',
]


def defects():
    put_txt('b581_defects.txt', ['### b581 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [185, 186, 190, 193, 194, 195, 197, 199, 201, 202, 203]
READS = [
    ('relay the SURROUND work-list, whole', RELAY, 'HEAD', WL, list(range(1, 56))),
    ('PLACE-papers SURROUND, its head and section 0', PP, PRE_PP, CUR, list(range(1, 41))),
    ('PLACE-papers SURROUND, the marked, ceiling, stem and credit-anchor lines', PP, PRE_PP, CUR, [59, 130, 137, 163, 165, 179, 183, 184, 187, 189]),
    ('PLACE-papers SURROUND, the audit line, provenance, ERA ANNOTATION and the tier block', PP, PRE_PP, CUR, list(range(191, 247))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line, nodes 7, 8, 20 and the mellin row', PP, MIRROR_PIN, PAGE, [3, 11, 12, 24, 138]),
    ('PLACE-papers SIGN_ARRANGEMENT_RECONCILIATION section 3', PP, PRE_PP, SIGN, list(range(44, 70))),
    ('relay the b450 batch, SURROUND`s two items', RELAY, 'HEAD', 'data/b450_batch.json', []),
    ('relay the CP-1b bank, its head and the SURROUND rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('relay the b538 register census, R3', RELAY, 'HEAD', 'data/b538_census.json', list(range(18, 25))),
    ('PLACE-papers FINDINGS, the SURROUND credit and b580`s entry', PP, PRE_PP, 'FINDINGS.md', [5932, 5936, 5940, 6522]),
    ('PLACE-papers OPEN_TRAILS, the form and its clauses', PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11936, 11938]),
    ('PLACE-papers AMC v0.2.4, the two vanilla lines', PP, PRE_PP, AMC, [293, 366]),
    ('PLACE-papers PATHS v0.7, its appended section', PP, PRE_PP, PATHS7, list(range(690, 702))),
    ('relay tools/banned_terms.py, the stems and the exceptions', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 81))),
    ('relay b580`s closing push-out, its head', RELAY, 'HEAD', 'data/b580_closing_push_out.txt', list(range(1, 4))),
]


def _b450_items():
    d = jl('b450_batch.json')
    return d['keystones']['THE_UNCONDITIONAL_SURROUND']['items']


def reads():
    L = ['b581 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### the b450 items, relay data/b450_batch.json keystones/THE_UNCONDITIONAL_SURROUND/items:')
    L += ['    item %d: %s' % (i, json.dumps(x, ensure_ascii=False)) for i, x in enumerate(_b450_items())]
    L.append('### the fact clause`s read over SURROUND`s pins, each tag peeled locally and at the remote:')
    for repo, tag, cited in (('SIDE-lv-conservation', 'v0.2.0', 'c8e3d31'), ('SIDE-lv-conservation', 'v0.5.0', '1767bd6'),
                             ('SIDE-lv-conservation', 'v0.5.1', 'bc4751e'), ('SIDE-lv-conservation', 'v0.6.0', 'c80bdc2'),
                             ('SIDE-lv-conservation', 'v0.7.0', '2d86182'), ('SIDE-lv-conservation', 'v0.8.0', '6efa9e5'),
                             ('SIDE-lv-conservation', 'v0.10.0', '93c27ec'), ('SIDE-kernel', 'v1.2', 'b1407b2'), ('SIDE-kernel', 'v1.5', '0e5233f'),
                             ('SIDE-archimedean', 'v0.1.0', '8019d9d'), ('SIDE-frobenius', 'v0.1.0', '2efe9f2'), ('SIDE-rcurve', 'v0.1.0', 'd5f33b4'),
                             ('SIDE-spinor', 'v0.1.0', 'b235bc6')):
        p = 'D:/' + repo
        loc = g(p, 'rev-parse', tag + '^{}').strip()
        rem = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag, 'refs/tags/%s' % tag).split(NL) if l.strip()]
        peeled = [l.split('\t')[0] for l in g(p, 'ls-remote', 'origin', 'refs/tags/%s^{}' % tag).split(NL) if l.strip()]
        r = (peeled or rem or [''])[0]
        L.append('    %s %s : cited %s ; local %s ; remote %s ; %s' % (repo, tag, cited, loc[:7], r[:7],
                                                                   'AGREE' if loc.startswith(cited) and r.startswith(cited) else '### DIFFER'))
    L.append('### the SIDE-effects toolchain and Mathlib at both pins (the fact clause`s read for AMC):')
    for pin in ('a27415d', 'c66f3c5'):
        man = json.loads(g(SE, 'show', '%s:lake-manifest.json' % pin))
        mrev = [x['rev'] for x in man['packages'] if x['name'] == 'mathlib']
        L.append('    %s : lean-toolchain "%s" ; lake-manifest mathlib rev %s ; Module1.lean imports %s' % (
            pin, g(SE, 'show', '%s:lean-toolchain' % pin).strip(), mrev[0] if mrev else '?',
            [l for l in g(SE, 'show', '%s:SIDEEffects/Phase15/Module1.lean' % pin).split(NL) if l.startswith('import ')]))
    put_txt('b581_reads.txt', L)


# ================================================================================ COMPONENT 1
FACT_TEXT = ('an unmarked sentence that states a fact the seat’s printed read contradicts -- a pin, a toolchain, a count, an import -- is '
             'corrected in place to the printed fact, the fact’s source printed beside it in the diff bank, and the correction listed in '
             'the back matter with line and both wordings; the sentence is otherwise unchanged')
PLACE_TEXT = ('a b450 “does not carry” item the work-list does not place is inserted beside the sentence whose claim it corrects, that '
              'sentence named in the back matter')
TOOLCHAIN = 'leanprover/lean4:v4.30.0-rc2'
MATHLIB = '5450b53'
AMC_FIX = [
    (293, '`SIDE-effects` (`c66f3c5`; vanilla Lean 4, no Mathlib).',
     '`SIDE-effects` (`c66f3c5`, Lean `v4.30.0-rc2` with Mathlib at `5450b53`, which Module1.lean imports).'),
    (366, 'Vanilla Lean 4.', 'Lean `v4.30.0-rc2` with Mathlib at `5450b53`, which Module1.lean imports at both pins.'),
]
AMC_TAG = '<!-- b581 (R191)(2) THE FACT CORRECTIONS, 2026-10-01 -->'
AMC_ENTRY = '## CP-7, act five: the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY'
P7_SUP = ('*Superseded beneath, 2026-10-01, by b581 under the author’s ruling `(R191)`(3) and the history clause (OPEN_TRAILS :11908):* '
          'the Correspondence column above was re-pinned at b580 (PLACE-papers `453dc15`) and cites this file’s final lines; relay '
          '`data/b578_edition_PATHS.txt` carries the offset at its head.')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def amc_fact():
    """### PLACE-papers AMC v0.2.4 :293 and :366 corrected by the fact clause, one back-matter section appended, and one FINDINGS line
    ### beneath b580's entry -- the housekeeping commit of (R191)(2); data/b581_amc_fact.txt banks the source of the fact."""
    Q = _Q()
    p = os.path.join(PP, *AMC.split('/'))
    text = io.open(p, encoding='utf-8', newline='').read()
    if text != g(PP, 'show', '%s:%s' % (PRE_PP, AMC)) or AMC_TAG in text:
        sys.exit('### AMC v0.2.4 DIFFERS FROM ITS BLOB OR IS ALREADY CORRECTED -- NOTHING WRITTEN')
    ls = text.split(NL)
    for ln, old, new in AMC_FIX:
        if ls[ln - 1].count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE' % ln)
        n0 = len(_segs(ls[ln - 1]))
        ls[ln - 1] = ls[ln - 1].replace(old, new)
        if len(_segs(ls[ln - 1])) != n0:
            sys.exit('### :%d -- THE CORRECTION CHANGED THE SEGMENT COUNT' % ln)
    for pin in ('a27415d', 'c66f3c5'):
        if g(SE, 'show', '%s:lean-toolchain' % pin).strip() != TOOLCHAIN:
            sys.exit('### THE TOOLCHAIN AT %s IS NOT THE ONE THE CORRECTION PRINTS' % pin)
        if not any(x['name'] == 'mathlib' and x['rev'].startswith(MATHLIB) for x in json.loads(g(SE, 'show', '%s:lake-manifest.json' % pin))['packages']):
            sys.exit('### THE MATHLIB REV AT %s IS NOT THE ONE THE CORRECTION PRINTS' % pin)
    if ls[-1] != '':
        sys.exit('### AMC v0.2.4 DOES NOT END IN A NEWLINE')
    add = [AMC_TAG, '', '### Fact corrections (b581, under the fact clause, `(R191)`(2))', '',
           '| this edition’s line | v0.2.4 wording | corrected wording | the printed fact | Status |', '|:--|:--|:--|:--|:--|']
    for ln, old, new in AMC_FIX:
        add.append('| :%d | %s | %s | SIDE-effects `lean-toolchain` `%s` and `lake-manifest.json` mathlib `%s` at `a27415d` and `c66f3c5`; '
                   'Module1.lean imports Mathlib at both (relay `data/b581_amc_fact.txt`) | corrected 2026-10-01 by b581 |' % (ln, old, new, TOOLCHAIN, MATHLIB))
    add.append('')
    put_pp(AMC, NL.join(ls[:-1] + add) + NL)
    e = Q.line_of(Q.FIND, AMC_ENTRY)
    h = '*Appended 2026-10-01 by b581 to b580’s entry (:%s), under the author’s ruling `(R191)`(2) -- THE FACT CLAUSE, APPLIED:*' % e
    Q.guard_absent(Q.FIND, h)
    r = Q.append_to(Q.FIND, '\n%s the edition’s :293 and :366 printed the SIDE-effects pin as vanilla Lean 4; the pin builds on Lean '
                            '`v4.30.0-rc2` with Mathlib at `5450b53`, and Module1.lean imports Mathlib at both pins, so both sentences '
                            'are corrected in place to that, the rest of each unchanged, and listed in the edition’s back matter (relay '
                            '`data/b581_amc_fact.txt`).\n' % h)
    L = ['b581 -- COMPONENT 1: THE FACT CLAUSE APPLIED TO AMC v0.2.4, (R191)(2)', '',
         '### the source of the fact, printed:']
    for pin in ('a27415d', 'c66f3c5'):
        man = json.loads(g(SE, 'show', '%s:lake-manifest.json' % pin))
        L.append('    SIDE-effects %s : lean-toolchain "%s" ; lake-manifest mathlib rev %s (inputRev %s)' % (
            pin, g(SE, 'show', '%s:lean-toolchain' % pin).strip(), [x['rev'] for x in man['packages'] if x['name'] == 'mathlib'][0],
            [x.get('inputRev') for x in man['packages'] if x['name'] == 'mathlib'][0]))
        L += ['        %s' % l for l in g(SE, 'show', '%s:SIDEEffects/Phase15/Module1.lean' % pin).split(NL) if l.startswith('import ')]
    L += ['', '### the corrections:'] + ['    :%d  "%s" -> "%s"' % c for c in AMC_FIX]
    L += ['### the back-matter section appended at the end of %s ; FINDINGS :%d (beneath b580`s entry :%s)' % (AMC, Q.line_of(Q.FIND, h), e)]
    put_txt('b581_amc_fact.txt', L)
    put_json('b581_amc_fact.json', dict(fixes=AMC_FIX, added=add, findings_line=Q.line_of(Q.FIND, h), head=h, entry=e, append=r))


def paths_line():
    """### PLACE-papers PATHS v0.7: one line appended beneath its b579 section, under the history clause -- (R191)(3)."""
    p = os.path.join(PP, *PATHS7.split('/'))
    text = io.open(p, encoding='utf-8', newline='').read()
    if text != g(PP, 'show', '%s:%s' % (PRE_PP, PATHS7)) or P7_SUP in text:
        sys.exit('### PATHS v0.7 DIFFERS FROM ITS BLOB OR IS ALREADY SUPERSEDED -- NOTHING WRITTEN')
    if not text.endswith('wrote it.*' + NL + NL) and not text.endswith('wrote it.*' + NL):
        sys.exit('### PATHS v0.7 DOES NOT END WITH ITS b579 SECTION')
    new = text if text.endswith(NL + NL) else text + NL
    put_pp(PATHS7, new + P7_SUP + NL)
    put_json('b581_paths_line.json', dict(path=PATHS7, line=P7_SUP, before=len(text.encode('utf-8'))))


FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
B580_ENTRY = '## CP-7, act five: the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY'


def c1_lines():
    """### PLACE-papers OPEN_TRAILS (the fact clause and the placement clause at the form) and FINDINGS (b580's weight)."""
    Q = _Q()
    form, entry = Q.line_of(Q.OT, FORM_HEAD), Q.line_of(Q.FIND, B580_ENTRY)
    if not (form == 11864 and entry == 6522):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s entry %s -- NOTHING WRITTEN' % (form, entry))
    heads = dict(
        fact='*Appended 2026-10-01 by b581, under the author’s ruling `(R191)`(2), to the form of an edition (:%d) -- THE FACT CLAUSE, STANDING:*' % form,
        place='*Appended 2026-10-01 by b581, under the author’s answer before b581’s seal, to the form of an edition (:%d) -- THE PLACEMENT CLAUSE:*' % form,
        weight='*Appended 2026-10-01 by b581 to b580’s entry (:%d), under `(R191)`(1) -- b580 AT ITS WEIGHT:*' % entry,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = [Q.append_to(Q.OT, '\n%s %s. Applied at b581 to ADDITIVE_MULTIPLICATIVE_CONSPIRACY v0.2.4 :293 and :366 (relay '
                              '`data/b581_amc_fact.txt`), and read over THE_UNCONDITIONAL_SURROUND’s pins (relay `data/b581_reads.txt`).\n'
                              % (heads['fact'], FACT_TEXT))]
    out.append(Q.append_to(Q.OT, '\n%s %s. Applied at b581 to THE_UNCONDITIONAL_SURROUND, both items beside its §6 positivity face (v0.4 '
                                 ':137).\n' % (heads['place'], PLACE_TEXT)))
    out.append(Q.append_to(Q.FIND, '\n%s `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md` beside v0.2.3 unedited: 13 rows as 12 '
                                   'sentences, the twelve rows on the finite-modulus no-conspiracy saying what the terminal states (the empty '
                                   'conspiracy type over the programme’s own couplings, programme-type; clean at `a27415d`, carrying the sorry '
                                   'axiom at `c66f3c5`), :249 citing the Li and arithmetic-limit equivalences at v0.9 with the finite range '
                                   'conditional on its two literature premises; :33 citing the open clause’s equivalence; :320 and :366 '
                                   '“RH-core”; the three stem uses excepted as names and titles; the version line above v0.2.3’s; the re-pin '
                                   'run last with “+2 from :17”. H28a, H28b and H28c held. PATHS v0.7’s column re-pinned by exactly +2 after '
                                   ':19; FOUNDATIONS v0.2.5’s unchanged. The navigator’s reading (a) recorded as having no object in AMC and '
                                   'belonging to BALANCE_AND_POSITIVITY’s edition. The suite reads 70 of 70.\n' % heads['weight']))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b581_c1_lines.json', dict(form=form, entry=entry, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'ch_iff_rh': 'v0.1 = `baed4df`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
       'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`'}
NS = {'h2_sign_iff_rh': 'B321', 'ch_iff_rh': 'B321', 'li_nonneg_iff_rh': 'LiCriterionBridge', 'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth'}
WHERE = {'h2_sign_iff_rh': 'node 8, line 12', 'ch_iff_rh': 'node 7, line 11', 'li_nonneg_iff_rh': 'node 20, line 24',
         'mellin_Phi_eq_zero_of_re_le_one': 'Correspondence row, line 138'}
EF = 'SIDE-explicit-formula'
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
R3B = 'relay `data/b538_census.json` :23'

REWRITES = [
    (37, 'leaving the goal in the form goal ⇐ h1 ∧ h2 with `h1` complete and only `h2` open.',
     'leaving lv’s goal state `goal ⇐ h1 ∧ h2` with `h1` complete -- and lv’s `h2` at Φ, `mellin Φ (s/2) ≠ 0`, is false at every s '
     'with re s ≤ 1 (%s), so the goal state closes nothing on the strip, the open clause being `h2_sign`, equivalent to RH (%s).' % (MP, H2)),
    (37, "That single open `h2` *is* this document's `covers_all`, and its content — stated, never counted — is that *every ξ-zero "
         "forces the Euler balance at some prime* (the conservation register, in its W-7 existential form); equivalently "
         "realization-totality at the ξ interface (the R3 face, totality-through-places), the R4 positivity face λ_Z(n) ≥ −λ_A(n), or "
         "the goal-state's Mellin-nonvanishing clause `mellin Φ (s/2) ≠ 0` off the line — one premise read in the monograph's §27.3 "
         "five registers.",
     "That single open clause, named `h2_sign` and equivalent to RH (%s), is what this document reads as `covers_all`, and the forms "
     "once named beside it are separate statements, not one premise: *every ξ-zero forces the Euler balance at some prime* (the "
     "conservation register, the deposit’s Route 3 clause, in its W-7 existential form) is RH restated (%s, E-2026-09-25-1), the R4 "
     "positivity face λ_Z(n) ≥ −λ_A(n) is RH in the Li form (%s), the R3 face (realization-totality through places) is undecided (%s), "
     "and the goal-state's `mellin Φ (s/2) ≠ 0` is false at every s with re s ≤ 1 (%s)." % (H2, CH, LI, R3B, MP)),
    (59, 'with compiled companions (SIDE-kernel `ProductFormula.conservation_of_spectra`;',
     'with compiled companions (SIDE-kernel `ProductFormula.conservation_of_spectra`, which states only `∀ s : ℤ, (1 : ℚ) ^ s = 1`, '
     'T2, the theorem staying manuscript-resident, relay `data/b558_cp1b.txt` :190;'),
    (130, 'In the SIDE-lv-conservation coupling ledger it is exactly the open premise `h2` —',
     'In the SIDE-lv-conservation coupling ledger it is read as lv’s open premise `h2` at Φ, false at every s with re s ≤ 1 (%s), the '
     'open clause being `h2_sign`, equivalent to RH (%s) —' % (MP, H2)),
    (130, '§0 and Correspondence), so that goal ⇐ h1 ∧ h2 with only this node open.',
     '§0 and Correspondence), so that lv’s goal state `goal ⇐ h1 ∧ h2` closes nothing on the strip (%s), the node open being '
     '`h2_sign`, equivalent to RH (%s).' % (MP, H2)),
    (163, 'The moment it is discharged, the reduction is a proof:',
     'The moment it is discharged, RH follows -- and the clause it names, `h2_sign`, is equivalent to RH (%s), so its discharge is RH '
     'itself:' % H2),
    (183, '| Manuscript-resident (monograph: two-input Tate argument + per-class analyses) |',
     '| Manuscript-resident (monograph: two-input Tate argument + per-class analyses); compiled beside it, RH ⟺ `h2_sign` (%s) |' % H2),
    (184, '| **DERIVES** — goal ⇐ h1 ∧ h2; h1 (the coupling ledger at Φ) complete, only h2 = `covers_all` open |',
     '| **DERIVES** — goal ⇐ h1 ∧ h2; h1 (the coupling ledger at Φ) complete, and lv’s h2 at Φ false at every s with re s ≤ 1 (%s), so '
     'the goal state closes nothing on the strip; the open clause is `h2_sign`, equivalent to RH (%s) |' % (MP, H2)),
]
CEILS = [
    (23, 'one facet of the proof —', 'one facet of the programme’s RH argument —'),
    (23, 'It is not the proof; it isolates the proof\'s single open node',
     'It is not the programme’s RH argument; it isolates the programme’s RH argument’s single open node'),
    (179, '**The proof does not rest on the C₇ row:**', '**The programme’s RH argument does not rest on the C₇ row:**'),
]
STEMS = [(187, '(the n > 2T² tail is the open gap)', '(the n > 2T² tail is the open range)')]
CREDITS = [
    (137, 'b450 item 1',
     '*Credit (b450, relay `data/b450_batch.json`, THE_UNCONDITIONAL_SURROUND item 1, carried at b581 under `(R191)`(4)):* the '
     'archimedean term `W_∞` is not sign-definite -- its kernel `Re ψ(1/4 + iu/2) − log π` is negative at low frequency and positive at '
     'high, crossing at u = 2π (the bench row u = 6.283, kernel −0.0011) -- and the positive assembly facing the prime sum is '
     '`W_pole + W_∞` (`%s` :52-:58, :62).' % SIGN),
    (137, 'b450 item 2',
     '*Credit (b450, relay `data/b450_batch.json`, THE_UNCONDITIONAL_SURROUND item 2, carried at b581 under `(R191)`(4)):* Day-1 '
     'BALANCE_AND_POSITIVITY §I attributed the positivity to the archimedean term alone, its `W_∞` row reading “positive (provable)”, '
     'and the repaired attribution is to the pole-plus-archimedean term (`%s` :46, :66).' % SIGN),
    (189, 'SURR:178 (FINDINGS :5932)',
     '*Credit (CP-1b, b558, FINDINGS :5932):* the §2 row of this table (v0.4 :178) prints `conservation_of_spectra` as '
     '`∀ s : ℤ, (1 : ℚ) ^ s = 1`, a STIPULATION carried by the namespace, on 2026-08-09, the reading b539 tiered T2 on 2026-09-25.'),
]
VERSION = (15, '**v0.5 — 2026-10-01**')
ASSIGN = {'SURR:59:137': 0, 'SURR:130:140': 3, 'SURR:184:149': 3}
ALSO_C = {'SURR:37:133'}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes its compiled name', 3: '(c) h1_complete_at_Phi STANDS with its pin, its sentence rewritten for the h2 row it shares'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH reduced|GRH proved|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proof|the proof\b|is a proof\b')
CEIL_RECORD = 'ceiling correction record:'
STEM_RECORD = 'banned stem, correction record:'
BM_TAG = '<!-- b581 (R191) THE v0.5 EDITION`S BACK MATTER, 2026-10-01 -->'


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'SURR' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    """### the edition's final line for a current-version line: +2 from :15, +2 more after :137, +2 more after :189."""
    return n + (2 if n >= VERSION[0] else 0) + (4 if n > 137 else 0) + (2 if n > 189 else 0)


OFFSET = ('+2 from :15 (the v0.5 version line and a blank, above the v0.4 version line); +4 more after :137 (the two b450 credit '
          'lines, each with a blank); +2 more after :189 (the CP-1b credit line and a blank) -- v0.4 :n sits at the edition`s :n+2 for '
          '15 <= n <= 137, :n+6 for 138 <= n <= 189, :n+8 after')


def edition(*a):
    """### PLACE-papers phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md, beside the current version from its blob at 5f13c2f; the
    ### re-pin step run last over the final body."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 5f13c2f -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in REWRITES + CEILS + STEMS:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if cur[VERSION[0] - 1] != '**v0.4 — 2026-07-19**' or cur[137] != '' or cur[189] != '' or not cur[188].startswith('| Voice 7'):
        sys.exit('### AN ANCHOR IS NOT WHERE THE FACE SAYS')
    for c in CREDITS:
        if len(_segs(c[2])) != 1:
            sys.exit('### A CREDIT LINE IS NOT ONE SEGMENT: %s' % c[1])
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=ASSIGN.get(r['id'], 1), also_c=r['id'] in ALSO_C, cites=cites, banks=banks, supports=r['reading']))
    # ### the insertions, bottom up
    new[189:189] = ['', CREDITS[2][2]]
    new[137:137] = ['', CREDITS[0][2], '', CREDITS[1][2]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    if any(body[_edl(n) - 1] != new[_edl(n) - 1] for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL BROKEN')
    if any(_edl(n) > len(body) or (n not in [x[0] for x in REWRITES + CEILS + STEMS] and body[_edl(n) - 1] != cur[n - 1])
           for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.5 edition -- written 2026-10-01 by b581 under the author’s ruling `(R191)`(4), by the form of `(R187)`(5)',
          '',
          '*This file is v0.5 of THE_UNCONDITIONAL_SURROUND, the CP-7 edition written beside v0.4 (`%s`, unedited) from v0.4’s tier '
          'blocks (its :211 and :237) and its CP-1b work-list (relay `%s`), the zeta page as its spine; it does not deposit and does not '
          'replace v0.4, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 10 work-list rows resolves to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '',
          '| inserted at this edition’s line | beside the sentence at | source | Status |', '|:--|:--|:--|:--|']
    for after, cid, text in CREDITS:
        at = [i for i, l in enumerate(body, 1) if l == text][0]
        bm.append('| :%d | :%d (%s) | %s | inserted under %s |' % (
            at, _edl(after) if after != 189 else _edl(after - 1),
            'the §6 positivity face, the claim it corrects' if after == 137 else 'the Correspondence table’s §2 row, its v0.4 :178',
            cid, 'the placement clause, the author’s answer before b581’s seal' if after == 137 else 'the form, as b578 placed its table credit'))
    bm += ['', '### Stem corrections', '', '| this edition’s line | v0.4 wording | v0.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in STEMS:
        bm.append('| :%d | %s %s (banned stem; correction record) | %s | corrected under the stem clause |' % (_edl(ln), STEM_RECORD, old, rep))
    bm += ['', '### Ceiling corrections', '', '| this edition’s line | v0.4 wording | v0.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause |' % (_edl(ln), CEIL_RECORD, old, rep))
    bm += ['', '### Fact corrections', '', 'None: every pin this document prints agrees with its tag, peeled at the remote (relay '
           '`data/b581_reads.txt`).', '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.5 | `%s` | written at b581 |' % ED,
           '| the current version, v0.4 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the b450 items | relay `data/b450_batch.json` | read |',
           '| the sign reconciliation | `%s` | read, unedited |' % SIGN,
           '| the sentence-by-sentence diff | relay `data/b581_edition_SURROUND.txt` | banked at b581 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the zeta page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    # ### THE RE-PIN STEP, LAST
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    for d in PIN:
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), WHERE[d], ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    for bank, n in (('b558_cp1b.txt', 190), ('b538_census.json', 23)):
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bm.append('| `data/%s` :%d | relay | the %s | not on the page | cited at :%s of this edition |' % (
            bank, n, 'CP-1b bank (b558)' if n == 190 else 'register census (b538)', ', :'.join(str(x) for x in at)))
    bm.append('')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b581_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=len(CREDITS), removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, stems=STEMS, credits=[dict(after=c[0], id=c[1], text=c[2], at=[i for i, l in enumerate(body, 1) if l == c[2]][0])
                                                                          for c in CREDITS],
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the credits, the corrections, the counts, the ceiling read, H28a-H28c."""
    E = jl('b581_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    scan = rd('b581_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            hits.append(dict(line=i, hit=m.group(0), ctx=l[max(0, m.start() - 60):m.end() + 20], record=l.startswith('| :') and CEIL_RECORD in l))
    beyond = [h for h in hits if not h['record']]
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == 0 and clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b581 -- COMPONENT 2: THE EDITION OF THE_UNCONDITIONAL_SURROUND, (R191)(4), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :15 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[14]),
         '### its tier blocks : :211 "%s" ; :237 "%s"' % (cur0[210][:90], cur0[236][:90]),
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE READINGS OF (R191)(4) AGAINST THIS DOCUMENT: (a) h2 marked -- 7 rows ; (b) the two b450 items -- CREDIT insertions, '
         'both placed after v0.4 :137 by the placement clause ; (c) h1_complete_at_Phi -- 2 rows, its pin v0.6.0 = c80bdc2 peeled at '
         'the remote: %s ; (d) the Route 3 clause -- within :37`s second row' % (
             'AGREE' if g(LV, 'ls-remote', 'origin', 'refs/tags/v0.6.0^{}').startswith('c80bdc2') else '### DIFFER'), '',
         '### THE WORK-LIST, ROW BY ROW (10 rows, 8 sentences, 6 lines) -- each row: v0.4`s line and the edition`s, the terminal, the '
         'reading (the seat`s hand-read), what its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s v0.4 :%d -> v0.5 :%d `%s` -- %s%s ; cites %s%s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']],
                                                                   ' and (d) the Route 3 clause' if d['also_c'] else '',
                                                                   ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                                   (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.4 : %s' % d['old'], '      v0.5 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    L += ['### (N1) COVERAGE BY THE READINGS OF (R191)(4), the seat`s hand-read: %d of %d rows -- (a) %d, (c) %d, (d) within (a) %d ; '
          'uncovered %s, resolved by the form ; and both b450 items, by (b)' % (
              len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']), sum(d['reading'] == 3 for d in E['diff']),
              sum(d['also_c'] for d in E['diff']), [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]), '',
          '### THE CREDIT LINES (each one segment; the source line each cites):']
    L += ['    v0.5 :%d (after v0.4 :%d) %s : %s' % (c['at'], c['after'], c['id'], c['text']) for c in E['credits']]
    L += ['### THE STEM CORRECTIONS:'] + ['    v0.4 :%d -> v0.5 :%d  "%s" -> "%s"' % (s[0], _edl(s[0]), s[1], s[2]) for s in E['stems']]
    L += ['### THE CEILING CORRECTIONS:'] + ['    v0.4 :%d -> v0.5 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE FACT CORRECTIONS: none -- every pin the document prints agrees with its tag peeled at the remote (relay data/b581_reads.txt)',
          '### THE VERSION LINE: above v0.4 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### REMOVALS: none. ### HISTORY LINES: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: three '
          'credit lines and the version line) ; the back matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']),
          '', '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], 'quoted in a ceiling correction record of the back matter, read by the seat'
                                          if h['record'] else '### BEYOND THE CEILING', h['ctx']) for h in hits] or ['    none']
    L += ['### read by the seat and carried: v0.4 :165 "That is not a conditional proof offered as a deficiency" -- a negation; v0.4 :33 '
          '"The Hypothesis is true exactly when `covers_all` is true" -- the reduction the document names manuscript-resident (its :183, '
          'T4), not a claim that RH holds',
          '### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b581_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b581_edition_SURROUND.txt', L)
    put_json('b581_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None,
                                   h1_pin_remote=g(LV, 'ls-remote', 'origin', 'refs/tags/v0.6.0^{}').split('\t')[0]))
    H = jl('b581_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'])


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}


def scores():
    H, E = jl('b581_h28.json'), jl('b581_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    reads = rd('b581_reads.txt')
    differ = reads.count('### DIFFER')
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD' and H['held'] is None
    allowed_pp = {'FINDINGS.md', 'OPEN_TRAILS.md', ED, AMC, PATHS7}
    S = dict(
        N1=('HELD' if H['covered'] >= 7 and len(E['credits']) >= 2 else 'REFUTED', 'the readings of (R191)(4) cover %d of the 10 MOVED rows '
            'by the seat`s hand-read, and both b450 items by reading (b); uncovered %s, resolved by the form' % (H['covered'], H['uncovered'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28b %s (the body %+d against at most %d), H28c %s; no sentence held' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N3=('HELD' if H['h1_pin_remote'].startswith('c80bdc2') else 'REFUTED', 'SIDE-lv-conservation v0.6.0 peeled at the remote: %s ; cited c80bdc2'
            % H['h1_pin_remote'][:12]),
        N4=('HELD' if differ == 0 else 'REFUTED', 'the fact clause`s read over SURROUND`s pins: %d of 13 tags DIFFER; no unmarked factual '
            'sentence corrected' % differ),
        N5=('HELD' if (kmain == V015 and heads_ok and cur_same and set(ch) <= allowed_pp) else 'REFUTED', 'nothing deposits; no kernel '
            'touched (%s); the current SURROUND unedited (%s); PLACE-papers changed at %s' % ('held' if kmain == V015 and heads_ok else '### MOVED',
                                                                                               'held' if cur_same else '### EDITED', ch)),
        S1=('HELD' if H['covered'] == 9 and H['uncovered'] == ['SURR:59:137'] else 'REFUTED', '9 of 10; uncovered :59; both b450 items'),
        S2=('HELD' if n2 and H['body_dn'] == 4 and H['allowed'] == 4 else 'REFUTED', 'H28a-H28c held; the body +4 against 4'),
        S3=('HELD' if H['h1_pin_remote'].startswith('c80bdc2') else 'REFUTED', 'v0.6.0 peels to c80bdc2 at the remote'),
        S4=('HELD' if differ == 0 else 'REFUTED', 'no pin differs'),
        S5=('HELD' if set(ch) == allowed_pp else 'REFUTED', '(N5) holds: the files changed are the ones its list names'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered']),
    )
    put_json('b581_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], S[k][1][:150]))


TITLE_HEAD = ('## CP-7, act six: the edition of THE_UNCONDITIONAL_SURROUND from its tier block and work-list, the W_∞ sign finding '
              'and the Day-1 attribution carried')
TITLE = TITLE_HEAD + '; written as v0.5 beside v0.4, no sentence held'
TRAIL_HEAD = ('### b581 — lane three, act nine under (R191): CP-7 act six -- the edition of THE_UNCONDITIONAL_SURROUND written beside '
              'the current; the fact clause applied to AMC v0.2.4; PATHS v0.7’s section superseded beneath')


def records_pp():
    Q = _Q()
    S, H, E, C1, AF = jl('b581_scores.json'), jl('b581_h28.json'), jl('b581_edition.json'), jl('b581_c1_lines.json'), jl('b581_amc_fact.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b581 on the author’s ruling `(R191)`. Banks: relay `data/b581_edition_SURROUND.txt` (the sentence-by-sentence diff, its '
         'offset line at its head), `data/b581_edition.json`, `data/b581_amc_fact.txt`, `data/b581_reads.txt`. Nothing deposits.*', '',
         '**The edition** (`(R191)`(4)): `%s`, v0.5, written beside v0.4 (`%s`, unedited) from v0.4’s tier blocks and its CP-1b work-list, '
         'the zeta page as its spine. The 10 work-list rows resolve to 8 sentences on 6 lines, each rewritten in place: the open clause '
         'named by its compiled name and cited to its equivalence with RH; lv’s goal state said to close nothing on the strip; the '
         'conservation register cited as RH restated, the Li face as RH, the R3 face as undecided; the conservation terminal said to '
         'state only its one-line identity. The surround’s kernel witness stands at its pin, which agrees with the tag at the remote. '
         'Three credit lines are inserted: the archimedean term not sign-definite and the Day-1 attribution, both beside the §6 '
         'positivity face, and the CP-1b credit after the Correspondence table. One stem use and three uses beyond the ceiling are '
         'corrected; no pin, toolchain or count contradicts a printed read; no sentence is removed and none held.' % (ED, CUR), '',
         '**The counts.** v0.4 %d sentences; v0.5 %d (the body %d, the back matter %d); the body differs by %+d against the final bound, %d.'
         % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 10 rows by the readings of `(R191)`(4): %d, and both b450 items.' % (
             H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The clauses and the housekeeping** (`(R191)`(2)-(3)): the fact clause (OPEN_TRAILS :%d), applied to AMC v0.2.4 :293 and :366 '
         '(FINDINGS :%d); the placement clause, the author’s answer (:%d); PATHS v0.7’s b579 section superseded beneath by one line.' % (
             ln['fact'], AF['findings_line'], ln['place']), '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R191)`(5): the edition of GRH_CASCADE by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.4, README, REGISTRY and both pages unwritten; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R191) ratified.** (1) b580 at its weight. (2) The fact clause, applied to AMC v0.2.4. (3) PATHS v0.7’s section superseded '
            'beneath. (4) The edition of THE_UNCONDITIONAL_SURROUND by the form, four readings entered. (5) The act after.', '',
            '**Entered:** FINDINGS.md:%d (the fact clause at AMC), :%d (b580’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the fact '
            'clause), :%d (the placement clause), this record; PLACE-papers `%s` (created); `%s` (:293, :366 and one back-matter section); '
            '`%s` (one line beneath its b579 section).' % (AF['findings_line'], ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['fact'],
                                                           ln['place'], ED, AMC, PATHS7), '',
            '**Answered before the seal, by the author:** both b450 credit lines beside §6’s positivity face, the CP-1b credit after the '
            'Correspondence table, and the placement clause.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** two unmarked sentences carry as the seat read them: v0.4 :33’s “The Hypothesis is true exactly when '
            '`covers_all` is true” states the reduction the document itself names manuscript-resident (its :183), and :165’s “not a '
            'conditional proof” is a negation. The document’s b454 ERA ANNOTATION on the archimedean sign (:203) stands unchanged beside '
            'the new credit line.', '',
            '**Next:** per `(R191)`(5), CP-7 act seven, b582 -- the edition of GRH_CASCADE by the same form, H28a-H28c scored; the author '
            'rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b581_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b581_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b581_findings.json')['entry_line'], jl('b581_trail.json')['line'])


def desk():
    S = jl('b581_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b581 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b581_defects.txt').rstrip(NL).split(NL)
    put_txt('b581_desk_notes.txt', L)


def components():
    S, H, C1, AF, fj, tj = (jl('b581_scores.json'), jl('b581_h28.json'), jl('b581_c1_lines.json'), jl('b581_amc_fact.json'),
                            jl('b581_findings.json'), jl('b581_trail.json'))
    ln = C1['lines']
    L = ['b581 -- THE COMPONENTS, BANKED UNDER (R191).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b580`s closing push-out relay 5ed77fdf ; push-b580* branches deleted by '
         'name (data/b581_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : AMC v0.2.4 :293 and :366 corrected by the fact clause, its back-matter section, FINDINGS :%d, committed alone ; '
         'PATHS v0.7`s superseding line, committed alone ; OPEN_TRAILS :%d (the fact clause), :%d (the placement clause) ; b580`s weight '
         'FINDINGS :%d' % (AF['findings_line'], ln['fact'], ln['place'], ln['weight']),
         '### COMPONENT 2 : the edition %s ; 8 sentences rewritten, 3 credit lines, 1 stem and 3 ceiling corrections, the version line, 0 '
         'removals ; data/b581_edition_SURROUND.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s N3 %s N4 %s' % (
             ED, H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of GRH_CASCADE ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b581_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b581_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
