# -*- coding: utf-8 -*-
"""b628_worklist.py -- THE ACT'S DATA, UNDER (R238). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b628: LANE THREE, ACT FIFTY-FIVE -- THE 2/3 THEOREM'S AXIOM PROFILE READ IN ITS OWN KERNEL AND CITED AT two_thirds, v0.23;
### THE INTAKE FORM'S PILOT ON THE ANNEX PAPER; THE CARRIED TEST DEFECT REPAIRED.
### Here: the pins before the act; the Zeta23 pin, its clone and its targets ((R238)(4)); the citation's module, branch and tag; the
### intake's document as the census's latest version names it and the author answered before the seal ((R238)(5)); the commit
### subjects in their full form, so that no arm's match reaches a later commit (b627's defect (g)).
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
FM = 'D:/relay/data/anthropic-zeta23/formal-math'    # ### the upstream clone b625 read (untracked in relay); its remote read once
PRE_PP = '6f8747b'          # ### PLACE-papers main before the act (b627's record)
PRE_RELAY = '4266bc46'      # ### relay main before the act (b627's closing)
PRE_GS = '17ce9ff'          # ### SIDE-global-section main before the act
PRE_KER = 'e939c92'         # ### SIDE-explicit-formula main before the act = v0.22
STEPZERO = 'f3180778'       # ### relay: b627's closing push-out bank, committed at step zero
DATE = '2026-10-05'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b626_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
PROBE = {'zeta': 'b626_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
NEW_NODES_ZETA = 'b628_nodes_zeta.txt'     # ### b626's ζ list, the pin moved to v0.23, one backmatter record
NEW_PROBE_ZETA = 'b628_probe_out.txt'

# ### (R238)(2): the carried test defect
TEST_FILE = 'tools/test_chain_page_b596.py'
TEST_CASE = '(1)'

# ### (R238)(4): route (b), the cross-kernel discharge
ZETA23_PIN = '3635e748'
ZETA23_PIN_FULL = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
ZETA23_TOOLCHAIN = 'leanprover/lean4:v4.33.0-rc2'
ZETA23_MATHLIB = '51e6992efd06126df61a496bebf8f49482a4e129'
ZETA23_CLONE = 'D:/zeta23-b628'                     # ### the clone at the pin, outside every repository the act writes
ZETA23_TARGETS = ['Zeta23.Statement', 'Zeta23.FinalMult']
ZETA23_PRINTS = ['Zeta23.thmB₀_mult', 'Zeta23.ThmB_statement']
ZETA23_ARTEFACT = ('AUDIT.md', 'comparator/PrintAxioms/Multiplicity.lean', 'comparator/Solution/Multiplicity.lean')
CITE_FILE = 'SIDEExplicitFormula/Simplicity.lean'
AXCHECK_FILE = 'AxiomCheckSimplicity.lean'
CITE_BRANCH = 'cite-b628'
CITE_TAG = 'v0.23'
CITE_NODE = 'SIDEExplicitFormula.Simplicity.exceptional_mass_le_third'
CITE_WORDS = 'discharged at its source kernel, not in this one'

# ### (R238)(5) as the author answered before the seal: the intake pilot
INTAKE_DOC = 'D:/MY-DOwnloads/A_WOUND_UP_ENOUGH_CRANK_v0_5.md'     # ### census v0.4 (the latest on D:) row R22, REGISTRY :366
INTAKE_LATER = ('D:/MY-DOwnloads/A_WOUND_UP_ENOUGH_CRANK_v0_6.md', 'D:/MY-DOwnloads/A_WOUND_UP_ENOUGH_CRANK_v0_7.md')
INTAKE_LOCAL = 'b628_intake_crank_v0_5.txt'      # ### the full bank: under data/, untracked, never pushed (the author's answer)
INTAKE_SUMMARY = 'b628_intake_summary.txt'       # ### the summary bank: counts, grades, clusters, work-order lines, the digest
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
CLUSTERS = tuple('R%02d' % i for i in range(1, 23))
VERDICTS = ('BRIGHT', 'DARK', 'NOT A ROUTE')

# ### (R238)(6) and the closing form of (R237)(4): the next act's terminals -- the Nyman–Beurling face names none yet
NEXT_ROUTES = [('W-ORD-NYMAN-BEURLING-FACE (OPEN_TRAILS :12893), b629', [])]

# ### the commit subjects, each in its full form; an arm matches the whole of it (b627's defect (g), repaired)
SUBJ = dict(
    test='b628 (R238)(2) THE TEST REPAIR:',
    lines='b628 (R238)(1)-(3) THE RECORD LINES:',
    cite='b628 (R238)(4) THE CITATION AT two_thirds:',
    intake='b628 (R238)(5) THE INTAKE SUMMARY:',
    zeta='b628 (R238)(4) THE ZETA PAGE AT v0.23:',
    chi='b628 (R238)(4) THE CHI PAGE:',
)


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
