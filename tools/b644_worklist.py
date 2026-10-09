# -*- coding: utf-8 -*-
"""b644_worklist.py -- THE ACT'S DATA, UNDER (R254). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b644: LANE THREE, ACT SEVENTY-ONE -- THE CHAIN READ AT COMMIT AND SHARED FILES ADDITIVE; THE WATCHDOG STOP; THE HINGES RECOUNTED
### UNDER THE REFINED DEFINITION AND THE CENSUS AT v0.7.1; SIDE-GLOBAL-SECTION'S INTERFACES BUILT; THE TWO ROSTERS; THE SEVEN PATCH
### EDITIONS; THE DEPOSIT DESCRIPTION AS SYNTHESIS, SECOND-READ, THE DRAFT'S FILE SET REPLACED AND HELD; THE LATTICE BANKED. The face is
### sealed after Components 2-7: these tools are written and run before the seal, their edits through the Edit tool, sealed at Component 8.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '93cfd59'          # ### PLACE-papers main before the act (b643's record and correction)
PRE_RELAY = 'a0791790'      # ### relay main before the act (b643's closing)
STEPZERO = 'f09c582a'       # ### relay: b643's closing push-out bank, committed at step zero
CHAIN_COMMIT = '60e1adf4'   # ### relay: (R254)(2), tools/act_root.py at commit and its planted test, alone
ADDITIVE_COMMIT = '0651e7cc'   # ### relay: (R254)(2), the additive arm and its test
WATCH_COMMITS = ('1c4ca202', 'e0cc0904')   # ### relay: (R254)(3), the watchdog stop and its test; the sampler joined before EXIT
CHAIN_TOOL, CHAIN_TEST = 'tools/act_root.py', 'tools/test_act_root_commit_b644.py'
ADD_TOOL, ADD_TEST = 'tools/additive_shared.py', 'tools/test_additive_shared_b644.py'
WATCH_TOOL, WATCH_TEST = 'tools/build_watch.py', 'tools/test_build_watch_b644.py'
DATE = '2026-10-09'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f004d01d-ad93-416c-a916-fe6e52403753/scratchpad'
SP_B643 = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e594f88a-2fab-4757-943d-7ab1bc3de815/scratchpad'
HOLD = 2560

EF, EF_PIN, EF_TAG = 'D:/SIDE-explicit-formula', '82550e4', 'v0.26'
SEC, SEC_PIN = 'D:/SIDE-structural-error-correction', '6bf19ab'

# ### (R254)(5): SIDE-global-section's Interfaces modules, each built against the mathlib4 checkout its banked profile was built with (the
# ### README :26-:31 and :40-:41; relay tools/b239_reprint.py :16-:17 -- five at D:/mathlib4 v4.30.0-rc1 cecd0c4d56, RestrictedTensorLayer1 at
# ### D:/MY-DOwnloads/mathlib4 v4.29.0).
GS_PIN = '17ce9ff'
MATHLIB_MAIN, MATHLIB_LEGACY = 'D:/mathlib4', 'D:/MY-DOwnloads/mathlib4'
IFACES = [('FiniteInstanceIdentity', MATHLIB_MAIN), ('GlobalSection', MATHLIB_MAIN), ('LocalLimit', MATHLIB_MAIN),
          ('PadicFourier', MATHLIB_MAIN), ('PadicStandardAddChar', MATHLIB_MAIN), ('RestrictedTensorLayer1', MATHLIB_LEGACY)]
IFACE_OUT = GS + '/build/interfaces'    # ### the Interfaces' build products (build/ is SIDE-global-section's .gitignore'd tree)

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b643_nodes_zeta.txt', 'chi': 'b643_nodes_chi.txt'}      # ### the lists in force (b643's v0.26 editions)
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN7 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_7.md'
CEN71 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md'
GLOSSARY = 'data/glossary.txt'
GLOSSARY_HINGE_LINE = 80    # ### data/glossary.txt :80, the HINGE entry (R253)(5)(b) and b643's answer; :79 CHAIN
DRAFT = '23228113'

# ### the ledger lines the act reads and addresses
B643_ENTRY = 7995
B643_RECORD = 13567
B643_CORRECTION = 13591
OT_ACT_ROOT = 12210         # ### W-ORD-ACT-ROOT, the chain clause
OT_WATCHDOG = 13563         # ### W-ORD-WATCHDOG-STOP, entered at b643
OT_PATCH = 13397            # ### W-ORD-DAY1-PATCH-VERSIONS
OT_LATTICE, OT_PI1 = 13529, 13531

SEALED = ('b644_worklist.py', 'b644_tests.py', 'b644_record.py', 'b644_checks.py', 'b644_closing.py', 'b644_reg_gate.py', 'b644_regspec.py')
NEXT_ROUTES = [('b645, the author`s word pending ((R254)(11)): the review pass (CP3) -- the licensed-statement table over every kernel '
                'docstring and every keystone claim through the intake form, the cluster, phase and maturity columns its output, the census at '
                'v0.8 -- unless the author`s reading of the description calls for repairs before it', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
