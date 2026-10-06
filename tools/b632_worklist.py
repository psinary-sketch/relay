# -*- coding: utf-8 -*-
"""b632_worklist.py -- THE ACT'S DATA, UNDER (R242). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b632: LANE THREE, ACT FIFTY-NINE -- THE E0 RULE'S GRADES APPLIED TO THE UNGRADED TERMINAL ROWS WITH PROVENANCE, A SECOND
### READER ON SIXTY BEFORE THE PUSH; THE PUBLIC PAGE'S APOSTROPHES, THE RECORD TOOL'S WRITER AND THE b596 CASE (9) REPAIRED. Here: the
### pins before the act; the input bank and its digest; the sample's seed and size; the packet's paths; the lists; the ledger lines the
### record lines address; the subjects; the next act's choices.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
PRE_PP = '3c2062c'          # ### PLACE-papers main before the act (b631's record)
PRE_RELAY = 'af38a0c3'      # ### relay main before the act (b631's closing)
PRE_KER = '8c51431'         # ### SIDE-explicit-formula main before the act = v0.25; this act touches no kernel
STEPZERO = 'a0551aed'       # ### relay: b631's closing push-out bank, committed at step zero
DATE = '2026-10-06'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b630_nodes_zeta.txt', 'chi': 'b631_nodes_chi.txt'}          # ### the lists in force before the act
PROBE = {'zeta': 'b630_probe_out.txt', 'chi': 'b631_chi_probe_out.txt'}       # ### their banked probes
NEW_NODES_CHI = 'b632_nodes_chi.txt'          # ### (R242)(2): b631's list, its backmatter record with plain apostrophes
NEW_NODES_ZETA = 'b632_nodes_zeta.txt'        # ### the commit branch: b630's list carried at pin v0.25, its lines unchanged
NEW_PROBE_ZETA = 'b632_probe_out.txt'         # ### the commit branch: the ζ page's fresh probe
NEW_PROBE_CHI = 'b632_chi_probe_out.txt'      # ### the commit branch: the χ page's fresh probe
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'     # ### b628's full intake bank: untracked before and after, never committed
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R242)(3): W-ORD-TABLE-RULE-GRADES
INPUT_BANK = 'data/b630_table_rule_readings.txt'   # ### b630's rule readings of the 1,799 ungraded rows, cited by its blob's digest
INPUT_REV = 'e99c6de4'                              # ### the relay commit that wrote it
SEED = 632242                                       # ### the sample's seed: the act and the ruling, as b620's 620230
PER_KERNEL = 30                                     # ### thirty from each of the two kernels with the most moves
AGREE_BAR = 0.85                                    # ### (R242)(3): the commit branch at or above it
PACKET_DIR = 'b632_reader_packet'
KEY = 'b632_key.txt'
PROMPT = 'b632_reader_prompt.txt'
ANSWERS = 'b632_reader_answers.txt'
AGREEMENT = 'b632_agreement.txt'
MOVES = 'b632_rule_moves.txt'
WORKING = 'b632_table_working.json'
READER_DIR = 'D:/reader_b632'                       # ### the reader's empty working directory, outside every repository
READER_GRADES = ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION', 'DEF')

# ### the ledger lines the act reads and addresses
RULE_GRADES_LINE = 13133       # ### OPEN_TRAILS: W-ORD-TABLE-RULE-GRADES
SECOND_READER = (12212, 12839, 12863)   # ### OPEN_TRAILS: the second-reader form and its two amendments
N5_LINE = 12799                # ### OPEN_TRAILS: the N5 scorer, standing; the test-pin line is addressed beneath it
BUILD_ROUTE = 13167            # ### OPEN_TRAILS: the build route under the hold, standing (b631)
B631_RECORD = 13169            # ### OPEN_TRAILS: b631's trail record
B631_ENTRY = 7679              # ### FINDINGS: b631's entry
SEAM_ENTRY = 12994             # ### OPEN_TRAILS: b626's seam and data clauses

SUBJ = dict(
    record='b632 step zero (R242)(2) THE RECORD TOOL`S WRITER:',
    chi='b632 step zero (R242)(2) THE CHI PAGE`S APOSTROPHES:',
    packet='b632 (R242)(3) THE READER PACKET:',
    case9='b632 (R242)(2) THE b596 CASE (9) FROZEN:',
    gen='b632 (R242)(3) THE GENERATOR`S PROVENANCE:',
    table='b632 (R242)(3) THE TABLE BY THE RULE:',
    cpage='b632 (R242)(3) THE PAGE GENERATOR`S PROVENANCE CELL:',
)
NEXT_ROUTES = [('b633 on the author`s word: the deposit preparations of the (R110) route; the census at its next version with the kernel '
                'column and the new faces; or W-ORD-GATE-FROM-ELABORATOR', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
