# -*- coding: utf-8 -*-
"""b630_worklist.py -- THE ACT'S DATA, UNDER (R240). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b630: LANE THREE, ACT FIFTY-SEVEN -- THE NYMAN–BEURLING DISTANCES d_N² IN ARB BALLS BESIDE 2λ₁ FROM THE KERNEL; NEW ROWS
### GRADED FROM THE RULE WITH PROVENANCE; HELPER ROWS AS OBJECTS; THE PROBE HOLD; THE OUTBOUND-IDENTIFIER LINE. Here: the pins
### before the act; the lists; the thirteen rows the rule grades and the four helpers; the table's baseline; the bench's named
### precision, cap and digit rule; the kernel's λ₁; the registry reads with the ferry's recollection beside them; the subjects.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
PRE_PP = '655e2d2'          # ### PLACE-papers main before the act (b629's record)
PRE_RELAY = '89fa8fd0'      # ### relay main before the act (b629's closing)
PRE_GS = '17ce9ff'          # ### SIDE-global-section main before the act
PRE_KER = 'aa17442'         # ### SIDE-explicit-formula main = v0.24; this act writes no kernel
STEPZERO = '63433a93'       # ### relay: b629's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b629_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b629_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
NEW_NODES_ZETA = 'b630_nodes_zeta.txt'
NEW_PROBE_ZETA = 'b630_probe_out.txt'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'     # ### b628's full intake bank: untracked before and after, never committed

# ### (R240)(3)-(4): the table and the list
FACE_TAG = 'v0.24'
NS = 'SIDEExplicitFormula.NymanBeurling.'
FACE_FILE = 'SIDEExplicitFormula/NymanBeurling.lean'
FACE_NODES = [NS + n for n in ('rhoFun', 'rhoFun_measurable', 'rhoFun_memLp', 'NB', 'BD', 'NymanBeurlingPremise', 'rh_iff_nb',
                               'distN', 'distN_antitone')]
HELPERS = [(NS + 'unitMeasure', 'def', 'the measure, Lebesgue restricted to (0, 1)'),
           (NS + 'rhoFun_bound', 'theorem', 'the bound |rhoFun θ x| ≤ 1 + |θ|'),
           (NS + 'rho', 'def', 'the family`s class in L²(0, 1)'),
           (NS + 'constOne', 'def', 'the constant 1 in L²(0, 1)')]
RULE_ROWS = sorted(FACE_NODES + [h[0] for h in HELPERS])      # ### the thirteen rows of v0.24 the rule grades in this act
TABLE_BASELINE = '75227e9c'   # ### relay: the table before v0.24 (1994 rows); a row absent there with no ledger cell takes the rule
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R240)(5): the probe hold
HOLD_MB = 2560
PROBE_TEST = 'tools/test_chain_page_b630.py'

# ### (R240)(6): the bench
PREC = 128                    # ### bits; every ball at this working precision
N_CAP = 100                   # ### the largest N computed; N_max is the largest N <= N_CAP whose ball keeps six digits
REL_DIGITS = 6                # ### six certified digits: rad(d_N²) <= 10^-6 · |mid(d_N²)|
LICOEFF = dict(file='SIDEExplicitFormula/Keiper.lean', tag='v0.20', name='liCoeff_one_keiper',
               want='LiWeil.LiCoeff 1 = 1 + Real.eulerMascheroniConstant / 2 - Real.log (4 * Real.pi) / 2')
RECOLLECTION = dict(
    bbls='Báez-Duarte, Balazard, Landreau and Saias conjectured d_N² ~ C / log N with C = Σ_ρ 1/|ρ|² = 2 + γ − log 4π',
    burnol='Burnol proved lim inf d_N² log N ≥ C')
REGISTRY_READS = [('bbls', 'https://export.arxiv.org/api/query?search_query=au:Balazard+AND+au:Saias+AND+abs:Nyman&max_results=5'),
                  ('burnol', 'https://export.arxiv.org/api/query?search_query=au:Burnol+AND+abs:Nyman&max_results=5')]

SUBJ = dict(
    lines='b630 (R240)(1)-(4) THE RECORD LINES:',
    table='b630 (R240)(3)-(4) THE TABLE AND THE LIST:',
    probe='b630 (R240)(5) THE PROBE HOLD:',
    zeta='b630 (R240)(4) THE ZETA PAGE AT v0.24 WITH THE HELPERS:',
)
DEDEKIND_LINE = 12895          # ### OPEN_TRAILS: W-ORD-DEDEKIND-INSTANCE, the two premises of (R213)(3)(d)
NEXT_ROUTES = [('b631, W-ORD-DEDEKIND-INSTANCE (OPEN_TRAILS :12895)', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
