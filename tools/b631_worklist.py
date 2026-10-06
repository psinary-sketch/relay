# -*- coding: utf-8 -*-
"""b631_worklist.py -- THE ACT'S DATA, UNDER (R241). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b631: LANE THREE, ACT FIFTY-EIGHT -- THE DEDEKIND ZETA OF ℚ(ζ_q) AS A CONFIGURATION OF THE SCHEMA, ITS TWO PREMISES NAMED, v0.25;
### THE NYMAN–BEURLING DIP RECORDED AS FINITE-RANGE DATA; THE MULTIPLICITY CONSTANT ENTERED AS A REGISTRY ITEM. Here: the pins before
### the act; the instance's module, branch, tag and nodes (the split form of the author's answer before the seal); the lists; the
### subjects; the next act's work-order.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
PRE_PP = '056fb19'          # ### PLACE-papers main before the act (b630's record)
PRE_RELAY = '67c8b477'      # ### relay main before the act (b630's closing)
PRE_GS = '17ce9ff'          # ### SIDE-global-section main before the act
PRE_KER = 'aa17442'         # ### SIDE-explicit-formula main before the act = v0.24
STEPZERO = '1cf71396'       # ### relay: b630's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b630_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b630_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
NEW_NODES_CHI = 'b631_nodes_chi.txt'
NEW_PROBE_CHI = 'b631_chi_probe_out.txt'
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'     # ### b628's full intake bank: untracked before and after, never committed
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R241)(3) and the author's answer before the seal: the instance, split
FACE_FILE = 'SIDEExplicitFormula/Schema/Dedekind.lean'
AXCHECK_FILE = 'AxiomCheckDedekind.lean'
FACE_BRANCH = 'dedekind-b631'
FACE_TAG = 'v0.25'
FACE_NS = 'SIDEExplicitFormula.Schema.Dedekind'
FACE_NODES = [FACE_NS + '.' + n for n in ('DedekindConfig', 'DedekindTheorem', 'dedekind_instance', 'dedekind_rhs', 'dedekind_three')]
INSTANCE = FACE_NS + '.dedekind_instance'
RHS = FACE_NS + '.dedekind_rhs'
THREE = FACE_NS + '.dedekind_three'
PREMISES = ('TrivialSummandPremise', 'EulerFactorPremise')
FAMILY_FILE = 'SIDEExplicitFormula/Schema/Family.lean'
FAMILY_READ = ['finsetSum', 'finsetSum_productLemma', 'finsetSum_target_iff', 'finsetSum_rhs', 'family', 'charCfg', 'familyConfig',
               'FamilyTheorem', 'family_theorem', 'familyConfig_arith', 'family_three', 'family_three_statement', 'zeta_rhs_pole',
               'TrivialSummandPremise', 'EulerFactorPremise', 'DedekindPremises']
BACKMATTER = ('the instance`s positivity equivalence is the family theorem with the trivial summand added and needs no premise; the '
              'two premises are what it costs to read the summed side as the Dedekind zeta`s, and they sit on dedekind_rhs where they '
              'are used. The instance is a statement about the schema`s summed configuration and nothing about any zeta function`s zeros.')

SUBJ = dict(
    lines='b631 (R241)(1)-(2) THE RECORD LINES:',
    face='b631 (R241)(3) THE DEDEKIND INSTANCE:',
    chi='b631 (R241)(3) THE CHI PAGE AT v0.25:',
)
NB_LINE = 12893                # ### OPEN_TRAILS: W-ORD-NYMAN-BEURLING-FACE
SIMPLICITY_LINE = 12012        # ### OPEN_TRAILS: W-ORD-SIMPLICITY-FACE
B630_RECORD = 13135            # ### OPEN_TRAILS: b630's trail record
B630_ENTRY = 7657              # ### FINDINGS: b630's entry
RULE_GRADES_LINE = 13133       # ### OPEN_TRAILS: W-ORD-TABLE-RULE-GRADES
NEXT_ROUTES = [('b632, W-ORD-TABLE-RULE-GRADES (OPEN_TRAILS :13133) if the author`s word falls there, else the deposit preparations of the '
                '(R110) route as the author names them', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
