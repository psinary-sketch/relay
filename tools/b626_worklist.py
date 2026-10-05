# -*- coding: utf-8 -*-
"""b626_worklist.py -- THE ACT'S DATA, UNDER (R236). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b626: LANE THREE, ACT FIFTY-THREE -- THE PLATT-TRUDGIAN HEIGHT AS A NAMED PREMISE AND THE HEIGHT PAIR, v0.22; THE THREE
### NODES RULED BY THE SEAM AND DATA CLAUSES; THE SECTION-VARIABLE TERMINALS READ; TWO GATE WORK-ORDERS ENTERED.
### Here: the pins before the act; the three nodes of (R236)(2); the five named restrictions with the variables each restricts
### ((R236)(3)); the section-variable terminals ((R236)(4)) and their CORRESPONDENCE cells; the rung's module, its branch, its
### tag and its nodes; the navigator's recollection of the citation, to be checked against the publisher's page.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
PRE_PP = 'dd4f700'          # ### PLACE-papers main before the act (b625's record)
PRE_RELAY = '42677181'      # ### relay main before the act (b625's closing)
PRE_GS = '3528bcf'          # ### SIDE-global-section main before the act
PRE_KER = '1d5d4dd'         # ### SIDE-explicit-formula main before the act = v0.21
STEPZERO = '30376120'       # ### relay: b625's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
NEW_NODES_ZETA = 'b626_nodes_zeta.txt'      # ### b622's ζ list, the pin moved to v0.22, the rung's nodes appended
NEW_PROBE_ZETA = 'b626_probe_out.txt'

E0_FILES = ('tools/e0_rule.py', 'tools/test_e0_rule.py')
# ### (R236)(2): the three nodes, and the node the narrowed seam clause also moves (printed for the author's ruling)
SEAM_NODE = 'SIDEExplicitFormula.B321.h2_sign_imp_rh_of_seam'
DATA_NODES = ('SIDEExplicitFormula.B321.paperFT_growth', 'SIDEExplicitFormula.B321.paperFT_growth_at')
SEAM_ALSO = 'SIDEExplicitFormula.B321.ch_iff_h2_sign_of_seam'
SEAM_CORR = [(383, 'SIDEExplicitFormula.B321.h2_sign_imp_rh_of_seam')]     # ### its one DERIVES cell: CORRESPONDENCE row 383 (line 456)
# ### (R236)(3): the five named restrictions, each with the quantified variables it restricts (its definition's parameters)
RESTRICTS = [('admissible', ('F', 'W'), 'Registers.lean :38'), ('HStrip', ('Z',), 'RestBound.lean :40'),
             ('HCount', ('Z', 'A₀'), 'RestBound.lean :44'), ('is_universal', ('I',), 'RegisterDepth.lean :38'),
             ('IsNontrivialZeroChi', ('χ', 'ρ'), 'Chi/ZeroConfig.lean :48')]
# ### (R236)(4): the terminals CriterionConverse's hχ and h1 reach (relay data/b625_section_vars.txt), and their CORRESPONDENCE cells
SECTION_TERMINALS = ['SIDEExplicitFormula.GRHWeil.h2_sign_chi_imp_grh_chi', 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi']
SECTION_CORR = [(432, 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_imp_grh_chi'), (435, 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_imp_grh_chi'),
                (432, 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi'), (436, 'SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi')]
# ### (R236)(5) as the author answered before the seal: the height rung
RUNG_FILE = 'SIDEExplicitFormula/PlattRung.lean'
AXCHECK_FILE = 'AxiomCheckPlattRung.lean'
RUNG_BRANCH = 'platt-b626'
RUNG_TAG = 'v0.22'
RUNG_NS = 'SIDEExplicitFormula.PlattRung'
RUNG_NODES = ['SIDEExplicitFormula.PlattRung.rh_upto', 'SIDEExplicitFormula.PlattRung.forall_rh_upto_iff_rh',
              'SIDEExplicitFormula.PlattRung.plattTrudgianT', 'SIDEExplicitFormula.PlattRung.PlattTrudgianHeight',
              'SIDEExplicitFormula.PlattRung.rh_upto_platt']
RUNG_TERMINAL = 'SIDEExplicitFormula.PlattRung.rh_upto_platt'
RUNG_PAIR = 'SIDEExplicitFormula.PlattRung.forall_rh_upto_iff_rh'
RECOLLECTION = dict(journal='Bull. London Math. Soc. 53 (2021)', doi='10.1112/blms.12460', T='3·10¹²')
PUBLISHER_URL = 'https://doi.org/10.1112/blms.12460'


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
