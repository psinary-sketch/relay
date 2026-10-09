# -*- coding: utf-8 -*-
"""b645_worklist.py -- THE ACT'S DATA, UNDER (R255). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b645: LANE THREE, ACT SEVENTY-TWO -- THE REVIEW PASS OPENED: THE LICENSED-STATEMENT TABLE BUILT AND TESTED; THE SEAM ROWS, THE
### LOAD-BEARING MAP, SIDE-EXPLICIT-FORMULA'S DOCSTRINGS AT v0.26 AND THE MONOGRAPH'S CLAIMS EACH TO ONE VERDICT; THE CENSUS'S CLUSTER,
### PHASE AND MATURITY COLUMNS DEFINED; NO EDITION RE-CUT; THE DEPOSIT HELD. The face is sealed after Components 2-6: these tools are
### written and run before the seal, their edits through the Edit tool, sealed at Component 7.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '6871ba2'          # ### PLACE-papers main before the act (b644's record)
PRE_RELAY = 'bd1387be'      # ### relay main before the act (b644's closing)
STEPZERO = '32d4fecd'       # ### relay: b644's closing push-out bank, committed at step zero
DATE = '2026-10-09'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f004d01d-ad93-416c-a916-fe6e52403753/scratchpad'
HOLD = 2560

EF, EF_PIN, EF_TAG = 'D:/SIDE-explicit-formula', '82550e4', 'v0.26'
EF_PKG = 'SIDEExplicitFormula'
ELAB_BANK = 'b643_elab_ef.txt'      # ### the elaborated reader's statement bank for SIDE-explicit-formula at v0.26 (b643, Component 3)

# ### (R255)(6): the hold retry at step zero -- the six Interfaces modules (b644's K.IFACES) and the reader's test
IFACE_MODS = ('FiniteInstanceIdentity', 'GlobalSection', 'LocalLimit', 'PadicFourier', 'PadicStandardAddChar', 'RestrictedTensorLayer1')
HOLD_TEST = 'test_elab_reader_b634.py'

# ### the documents of the opening slice ((R255)(4))
MAP = 'phase1.5/method/THE_LOAD_BEARING_MAP.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
SEAM_ROWS = (('FINDINGS.md', 7595), ('OPEN_TRAILS.md', 13033))
SEAM_DECL = ('SIDEExplicitFormula/Seam.lean', 84, 'SIDEExplicitFormula.B321.rh_strip_imp_rh_holds')
SEAM_PRINT = 'b536_profile.json'    # ### the seam's axiom print, relay data/b536_profile.json (b536, v0.2 = 5c72cad)

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b643_nodes_zeta.txt', 'chi': 'b643_nodes_chi.txt'}      # ### the lists in force (b643's v0.26 editions)
PROBE = {'zeta': 'b643_probe_out_zeta.txt', 'chi': 'b643_probe_out_chi.txt'}
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
CEN71 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_7_1.md'
GLOSSARY = 'data/glossary.txt'
DRAFT = '23228113'

# ### the ledger lines the act reads and addresses
B644_ENTRY = 8025
B644_RECORD = 13599
B644_CORRECTION = 13627

SEALED = ('b645_worklist.py', 'b645_tests.py', 'b645_record.py', 'b645_checks.py', 'b645_closing.py', 'b645_reg_gate.py', 'b645_regspec.py',
          'licensed_table.py')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None
