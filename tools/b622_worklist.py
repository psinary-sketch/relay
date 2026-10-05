# -*- coding: utf-8 -*-
"""b622_worklist.py -- THE ACT'S DATA, UNDER (R232). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b622: LANE THREE, ACT FORTY-NINE -- THE QUANTIFIER COLUMN: THE GENERATOR READING EACH NODE'S SHAPE FROM ITS LEAN STATEMENT, BOTH
### PAGES RE-EMITTED, THE SIEVE'S HAND MARKS REPLACED; README'S SUPPORTABLE SENTENCE FOR v0.17-v0.21; THE 39 OWED SENTENCES ENTERED AS
### WORK-LIST ITEMS.
### Here: the pins before the act; the five test nodes and their expected shapes ((R232)(4), (N1)); the node lists' names; the 39
### sentences' documents and their work-list or addendum files ((R232)(2)); README's paragraph and the deposit note's refreshed sentence
### ((R232)(3)), in the author's words where the ruling gives them; the sieve's v0.6 wordings ((R232)(4)).
"""
import io
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
PRE_PP = 'f695c98'          # ### PLACE-papers main before the act (b621's correction)
PRE_RELAY = '02fba720'      # ### relay main before the act (b621's closing)
STEPZERO = '92d1b584'       # ### relay: b621's closing push-out bank, committed at step zero
DATE = '2026-10-04'

SV5 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md'      # ### the sieve's current version, unedited
SV6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'      # ### this act's edition
SV_OLDER = ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md',
            'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
OLD_NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PIN = {'zeta': ('v0.20', '914c413'), 'chi': ('v0.21', '1d5d4dd')}
COLUMN_MARK = '# column: quantifier'
LIST_HEAD = {
    'zeta': ['# b622 -- THE ζ NODE LIST WITH THE QUANTIFIER COLUMN, (R232)(4): b602`s list (relay data/b602_nodes_zeta.txt), every line',
             '# unchanged, at its pin v0.20, with the one line `# column: quantifier` appended, by which the generator emits the shape cell',
             '# and the key`s head line (relay tools/chain_page.py, `node_column`). A list without that line emits exactly as before.', '#'],
    'chi': ['# b622 -- THE χ NODE LIST WITH THE QUANTIFIER COLUMN, (R232)(4): b603`s list (relay data/b603_nodes_chi.txt), every line',
            '# unchanged, at its pin v0.21, with the one line `# column: quantifier` appended, by which the generator emits the shape cell',
            '# and the key`s head line (relay tools/chain_page.py, `node_column`). A list without that line emits exactly as before.', '#'],
}

# ### (R232)(4): the five test nodes, in the ruling's order; "a cell" read as the page's one FINITE rung (reading (iv) on the face)
TEST_NODES = [
    ('SIDEExplicitFormula.KeiperSign.liCoeff_one_pos', 'zeta', 'FINITE', 'a cell: λ₁ > 0, the sign at one index, the Li ladder`s one compiled rung'),
    ('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'zeta', 'UNIVERSAL', 'the located clause`s iff-face at ζ'),
    ('SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh', 'zeta', 'UNIVERSAL', 'the arithmetic limits` iff-face'),
    ('SIDEExplicitFormula.Simplicity.exceptional_mass_le_third', 'zeta', 'DENSITY', 'the proportion`s consequence, an ε–T₀ form over counts'),
    ('SIDEExplicitFormula.Schema.Family.family_theorem', 'chi', 'FAMILY', 'the family theorem over the characters mod q'),
]

# ### the three nodes the reader prints UNCLASSIFIED, with the definitions their fields name, read at the page's pin, for the seat's
# ### proposal under the author's reading before the seal (a premise bundle prints the shape of its strongest field)
UNCLASSIFIED_READ = {
    'Zeta23.WeilEF.EF_lit_zetaZeroConfig': ('zeta', [('Zeta23/ExplicitFormula.lean', 'EF_lit')]),
    'SIDEExplicitFormula.Keiper.KeiperObligations': ('zeta', [('SIDEExplicitFormula/Keiper.lean', n) for n in
                                                               ('BinomialTransform', 'LogDerivSplit', 'StieltjesLog', 'GammaRZetaValues')]),
    'SIDEExplicitFormula.Schema.PlateauRamp.WindowObligations': ('chi', [('SIDEExplicitFormula/Schema/PlateauRamp.lean', n) for n in ('ConvStep', 'Smooth4')]),
}

# ### (R232)(2): the 39 sentences of OPEN_TRAILS :12851, by document; a document with a b558 work-list takes its items in that list
# ### (a dated section appended); one without takes an addendum file in the same folder (relay data/b558_editions/)
WL_DIR = 'b558_editions'
WL_FILES = {
    'clusters/IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19.md': ('IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19_addendum.txt', 'addendum'),
    'clusters/RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19.md': ('RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19_addendum.txt', 'addendum'),
    'internal/CATALOGOS.md': ('CATALOGOS_addendum.txt', 'addendum'),
    'phase1.5/method/A_METHODOLOGY.md': ('A_METHODOLOGY_addendum.txt', 'addendum'),
    'phase1.5/method/ENUMERA_v1_6.md': ('ENUMERA.txt', 'list'),
    'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md': ('INVARIANCE_BARRIERS.txt', 'list'),
    'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md': ('PATHS_TO_THE_CRITICAL_LINE.txt', 'list'),
    'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md': ('THE_UNCONDITIONAL_SURROUND.txt', 'list'),
    'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md': ('SIMPLICITY_OF_RIEMANN_ZEROS.txt', 'list'),
    'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md': ('BALANCE_AND_POSITIVITY.txt', 'list'),
    'phase1.5/spectral/GRH_CASCADE_v0_3_6.md': ('GRH_CASCADE.txt', 'list'),
    'phase2/formation/UNIVERSALITY.md': ('UNIVERSALITY_addendum.txt', 'addendum'),
    'phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md': ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE_addendum.txt', 'addendum'),
    'phase2/philosophy/SILENCE_EMERGENCE.md': ('SILENCE_EMERGENCE_addendum.txt', 'addendum'),
}
WL_SECTION = '### b622 -- (R232)(2), %s: CEILING ITEMS ENTERED BY LINE' % DATE
CEILING_REF = 'README :106-:111; the ceiling clause, OPEN_TRAILS :11906'

# ### (R232)(3): README. The paragraph beside the (R183)(3) sentence, which stays; the author's sentence in the ruling's words.
R183_MARK = "*(Appended under the author's ruling `(R183)`(3)"
README_PARA = (
    "*(Appended under the author's ruling `(R232)`(3), 2026-10-04, b622, beside the `(R183)`(3) sentence directly above, which stays, as do "
    "the `(R146)`(2), `(R174)`(1), `(R176)`(2), `(R177)`(2) and `(R182)`(2) sentences: SIDE-explicit-formula v0.17–v0.21 entered at their "
    "weight, v0.21 = `1d5d4dd`.)* Supportable, the author's sentence: *the simplicity clause stated as a Prop beside h2_sign with no compiled "
    "edge between them (simplicity_iff, v0.17; positivity_not_imp_simplicity, v0.19); Weil positivity of a sum of configurations exactly when "
    "it holds for both parts (productLemma_holds, v0.18) and over a finite family exactly when every member's target holds (family_theorem, "
    "v0.21, q = 3 by rfl); λ₁ > 0 at the standard three (liCoeff_one_pos, v0.20), a single rung; the Keiper identity and bounds carried at "
    "INTERFACES on seven named obligations; the window family defined with two named obligations, independent of the Epstein premises.* "
    "Not supportable, unchanged: *RH proved*; *h2_sign proved*; *λ_n ≥ 0 proved*; *simplicity proved*; *GRH reduced for any modulus "
    "beyond the family theorem's letter*.")
DEPOSIT_OLD = ("the live monograph stands at **v5.13**, the deposit at manuscript **v5.10.2** / Zenodo **v1.1.2**. *Internal since the "
               "deposit: v5.11 (F5/F6) → v5.12 (F7 two-clause accounting) → v5.13 (the substrate season).*")
DEPOSIT_NEW = ("the live monograph stands at **v5.18**, the deposit at manuscript **v5.10.2** / Zenodo **v1.1.2**; the live kernel line "
               "names SIDE-explicit-formula **v0.21** (`1d5d4dd`) beside SIDE-kernel **v1.5** (`0e5233f`). *Internal since the deposit: "
               "v5.11 (F5/F6) → v5.12 (F7 two-clause accounting) → v5.13 (the substrate season) → v5.14–v5.16 (CP-8, b606–b608) → v5.17 "
               "(b609) → v5.18 (b621).* *(Refreshed 2026-10-04 under the author's ruling `(R232)`(3), b622: the live line named v5.13 and "
               "no kernel line.)*")

# ### (R232)(4): the sieve at v0.6
MARK_H, MARK_G = '(H)', '(G)'
SHAPE_OLD = ('- **Shape**: FINITE, UNIVERSAL, LIMIT, DENSITY or FAMILY, hand-read (H) at this edition from the Lean statement for a compiled '
             'row and from the sentence for the others, until W-ORD-QUANTIFIER-COLUMN’s generator read replaces it.')
SHAPE_NEW = ('- **Shape**: FINITE, UNIVERSAL, LIMIT, DENSITY or FAMILY, read by the generator (G) from the Lean statement at its page’s pin '
             'where the row names a node of the ζ or the χ page (relay `tools/chain_page.py`, the pages’ shape column, b622), a node the '
             'generator cannot classify reading UNCLASSIFIED (G) for the author’s ruling, and hand-read (H) where the row names no page node, '
             'from the Lean statement for a compiled row and from the sentence for the others.')
VERSION6 = ('*v0.6, 2026-10-04 -- the shape column read by the generator from the Lean statement at the page’s pin for the %d rows naming '
            'a page node, %d as hand-read and %d not (%s), the hand marks kept where a row names none; v0.5 stands beside it, unedited.*')
BM_TAG6 = '<!-- b622 (R232) THE v0.6 EDITION`S BACK MATTER, 2026-10-04 -->'
B605_TAG = '<!-- b605 (R215) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'
B609_TAG = '<!-- b609 (R219) THE v0.4 EDITION`S BACK MATTER, 2026-10-03 -->'
B617_TAG = '<!-- b617 (R227) THE v0.5 EDITION`S BACK MATTER, 2026-10-04 -->'
ROW_RE = re.compile(r'^\| ([A-Z]{2}-\d\d) \| ')


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').replace(chr(13), '').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def cells_of(row):
    return [x.strip() for x in row.strip().strip('|').split(' | ')]


def body_rows(lines):
    """### (line, id, cells) for every table row of the body (above the first back matter's tag)."""
    cut = lines.index('<!-- b604 (R214) THE v0.2 EDITION`S BACK MATTER, 2026-10-03 -->')
    return [(i, ROW_RE.match(l).group(1), cells_of(l)) for i, l in enumerate(lines[:cut], 1) if ROW_RE.match(l)]


def faces_of(cells):
    """### the declarations a row's compiled-face column names, in order."""
    return re.findall(r'`([^`]+)` @', cells[-1])


def residue_items():
    """### the 39 sentences of b621's record (OPEN_TRAILS :12851), each with its document, line, sentence, both readings and its reason bank
    ### line -- read from b620's key and the reader's answers and b621's residue bank, at relay PRE_RELAY."""
    def rel(n):
        return show(PRE_RELAY, 'data/' + n, ROOT)
    key = json.loads(rel('b620_key.json'))
    res = {x['id']: x for x in key['residue']}
    ans = {}
    for l in lines_of(rel('b620_reader_answers.txt')):
        m = re.match(r'^(X\d{3})\s*\|\s*(\S+)\s*\|\s*(.*)$', l)
        if m:
            ans[m.group(1)] = (m.group(2), m.group(3).strip())
    rs = json.loads(rel('b621_residue.json'))
    banks = {}
    out = []
    for doc, items in sorted(rs['other'].items()):
        for ln, xid, why in items:
            r = res[xid]
            if r['bank'] not in banks:
                banks[r['bank']] = lines_of(rel(r['bank']))
            out.append(dict(id=xid, doc=doc, line=ln, sentence=r['sentence'], seat=r['seat'], mark=r['mark'], reader=ans.get(xid, ('', ''))[0],
                            reader_line=ans.get(xid, ('', ''))[1], bank=r['bank'], bank_line=r['bank_line'],
                            reason=banks[r['bank']][r['bank_line'] - 1].strip(), both=(why == 'both BEYOND')))
    return out
