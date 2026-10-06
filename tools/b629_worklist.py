# -*- coding: utf-8 -*-
"""b629_worklist.py -- THE ACT'S DATA, UNDER (R239). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b629: LANE THREE, ACT FIFTY-SIX -- THE NYMAN–BEURLING CRITERION AS A COMPILED FACE AT v0.24; THE INTAKE FORM ENTERED; THE
### b592 TEST REPAIRED. Here: the pins before the act; the face's module, branch, tag and nodes; the Mathlib pieces it reads; the
### citation's three works with the ferry's recollection beside them; the commit subjects in their full form.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PRE_PP = 'f610d1f'          # ### PLACE-papers main before the act (b628's record)
PRE_RELAY = '75227e9c'      # ### relay main before the act (b628's closing)
PRE_GS = '17ce9ff'          # ### SIDE-global-section main before the act
PRE_KER = '98b7668'         # ### SIDE-explicit-formula main before the act = v0.23
STEPZERO = 'dabf7b95'       # ### relay: b628's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b628_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b628_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
NEW_NODES_ZETA = 'b629_nodes_zeta.txt'
NEW_PROBE_ZETA = 'b629_probe_out.txt'

# ### (R239)(3): the b592 test
TEST_FILE = 'tools/test_chain_page_b592.py'
TEST_CASES = ['(1)', '(2)', '(3)']
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'     # ### b628's full intake bank: untracked before and after, never committed

# ### (R239)(4): the face
FACE_FILE = 'SIDEExplicitFormula/NymanBeurling.lean'
AXCHECK_FILE = 'AxiomCheckNymanBeurling.lean'
FACE_BRANCH = 'nb-b629'
FACE_TAG = 'v0.24'
FACE_NS = 'SIDEExplicitFormula.NymanBeurling'
FACE_NODES = ['SIDEExplicitFormula.NymanBeurling.rhoFun', 'SIDEExplicitFormula.NymanBeurling.rhoFun_measurable',
              'SIDEExplicitFormula.NymanBeurling.rhoFun_memLp', 'SIDEExplicitFormula.NymanBeurling.NB',
              'SIDEExplicitFormula.NymanBeurling.BD', 'SIDEExplicitFormula.NymanBeurling.NymanBeurlingPremise',
              'SIDEExplicitFormula.NymanBeurling.rh_iff_nb', 'SIDEExplicitFormula.NymanBeurling.distN',
              'SIDEExplicitFormula.NymanBeurling.distN_antitone']
TERMINAL = 'SIDEExplicitFormula.NymanBeurling.rh_iff_nb'
PREMISE = 'NymanBeurlingPremise'
MONO = 'SIDEExplicitFormula.NymanBeurling.distN_antitone'
OBLIGATIONS = ['rhoFun_measurable', 'rhoFun_memLp']      # ### the family's two obligations, each discharged or a named field
API = [('Mathlib/MeasureTheory/Function/LpSeminorm/Basic.lean', r'^theorem MemLp\.of_bound|^theorem memLp_const \('),
       ('Mathlib/MeasureTheory/Function/LpSpace/Basic.lean', r'^def toLp \(f : α → E\)'),
       ('Mathlib/MeasureTheory/Function/Floor.lean', r'^theorem measurable_fract'),
       ('Mathlib/Algebra/Order/Floor/Ring.lean', r'^theorem fract_nonneg|^theorem fract_lt_one'),
       ('Mathlib/MeasureTheory/Measure/Lebesgue/Basic.lean', r'^theorem volume_Ioo '),
       ('Mathlib/Topology/Algebra/Module/Basic.lean', r'^def Submodule\.topologicalClosure'),
       ('Mathlib/LinearAlgebra/Span/Defs.lean', r'^theorem span_mono|^theorem span_monotone'),
       ('Mathlib/Topology/MetricSpace/HausdorffDistance.lean', r'^def infDist|^theorem infDist_le_infDist_of_subset'),
       ('Mathlib/NumberTheory/LSeries/RiemannZeta.lean', r'^def RiemannHypothesis')]
# ### the citation: the ferry's recollection, printed beside the registry reads and never copied into the module
RECOLLECTION = dict(nyman='Nyman 1950 (thesis, Uppsala)', beurling='Beurling 1955 (Proc. Natl. Acad. Sci. USA)',
                    baez='Báez-Duarte 2003')
REGISTRY_READS = [('beurling', 'https://api.crossref.org/works/10.1073/pnas.41.5.312'),
                  ('baez', 'https://export.arxiv.org/api/query?id_list=math/0202141'),
                  ('nyman', 'https://api.crossref.org/works?query.bibliographic=Nyman+1950+groups+semigroups+translations&rows=3')]

SUBJ = dict(
    test='b629 (R239)(3) THE b592 TEST REPAIR:',
    lines='b629 (R239)(1)-(2) THE RECORD LINES:',
    face='b629 (R239)(4) THE NYMAN-BEURLING FACE:',
    zeta='b629 (R239)(4) THE ZETA PAGE AT v0.24:',
)
NEXT_ROUTES = [('b630, the Nyman–Beurling bench (the second act)', [
    ('SIDEExplicitFormula.NymanBeurling.distN', KER, FACE_TAG, FACE_FILE, None),
    ('SIDEExplicitFormula.NymanBeurling.distN_antitone', KER, FACE_TAG, FACE_FILE, None)])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
