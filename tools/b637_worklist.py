# -*- coding: utf-8 -*-
"""b637_worklist.py -- THE ACT'S DATA, UNDER (R247). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b637: LANE THREE, ACT SIXTY-FOUR -- THE BINDER GRAMMAR: THE E0 RULE AS A TOTAL FUNCTION OVER A FINITE CLASSIFICATION, NAMES REMOVED
### FROM THE READING, BOTH READERS RERUN OVER BOTH KERNELS, THE 20 UNNAMED ROWS READ BY CLASS; UPSTREAM ROWS AS KIND; THE MIRROR'S ROSTER AT
### THE CURRENT EDITIONS. Here: the pins before the act; the two kernels and their banks; Lean's binder kinds' source; the lists in force for
### the pages; the census paths and lines; the ledger lines; the roster's additions; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '142c315'          # ### PLACE-papers main before the act (b636's correction beneath its record)
PRE_RELAY = 'f3a2f6b2'      # ### relay main before the act (b636's closing)
STEPZERO = '746e32f4'       # ### relay: b636's closing push-out bank and its first attempt, committed at step zero
DATE = '2026-10-07'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/22cdf84c-42e5-4b4d-b777-6c6a90fcc03e/scratchpad'
PLANTED_DIR = SP + '/b637_planted'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}          # ### the lists in force since b632
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}   # ### the probes in force since b635 (its Pages answer)
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R247)(4)(iii): THE TWO KERNELS, THEIR PINS AND THEIR ELABORATED BANKS. The explicit-formula kernel's bank is the one the table's
# ### generator reads (relay data/elab_types.txt: b634's 927 typed blocks, data/b634_elab_types.txt, identical, with b635's 13 resolved names);
# ### the structural-error-correction kernel's is b636's.
EF_KERNEL, EF, EF_PIN = 'SIDE-explicit-formula', 'D:/SIDE-explicit-formula', '8c51431'
SEC_KERNEL, SEC, SEC_PIN = 'SIDE-structural-error-correction', 'D:/SIDE-structural-error-correction', '6bf19ab'
KERNELS = {EF_KERNEL: dict(path=EF, pin=EF_PIN, tag='v0.25', bank='elab_types.txt', ferry_bank='b634_elab_types.txt'),
           SEC_KERNEL: dict(path=SEC, pin=SEC_PIN, tag='v0.2.2', bank='b636_elab_sec.txt', ferry_bank='b636_elab_sec.txt')}

# ### (R247)(4)(i): LEAN'S BINDER KINDS, READ IN THE TOOLCHAINS' OWN SOURCES (git grep --no-index, the toolchains being no repository)
TOOLCHAINS = {EF_KERNEL: 'D:/elan/toolchains/leanprover--lean4---v4.34.0-rc1', SEC_KERNEL: 'D:/elan/toolchains/leanprover--lean4---v4.29.0-rc8'}
BINDERINFO_FILE = 'src/lean/Lean/Expr.lean'
FIVE_NAMES = ('h', 'H', 'hyp', 'x', 'ξ')            # ### (R247)(4)(ii): the five-name test
H71C_BOUND = 0.02                                   # ### (R247)(4): H71c's 2 %
UNNAMED_BANK = 'b634_unnamed_rows.txt'              # ### the 20 unnamed rows (b634)

# ### (R247)(2): THE UPSTREAM ROWS -- the table's rows the upstream mark reaches and the five Mathlib names (no kernel file declares them;
# ### Mathlib de5ce8a9 NumberTheory/Harmonic/ZetaAsymp.lean :435, :532, :536, :539, :542)
MATHLIB_FIVE = ('completedRiemannZeta₀_one', 'riemannZeta₀', 'riemannZeta₀_one', 'riemannZeta₁', 'riemannZeta₁_one')

# ### the census and its premise table
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
CEN5_PREMISES = (689, 740)  # ### the 42 named premises, their table and its two notes

# ### the ledger lines the act reads and addresses
B636_ENTRY = 7801           # ### FINDINGS: b636's entry
B636_WEIGHT_PRIOR = 7799    # ### FINDINGS: b635 at its weight (b636's line)
B636_RECORD = 13309         # ### OPEN_TRAILS: b636's trail record
B636_CORRECTION = 13333     # ### OPEN_TRAILS: b636's correction beneath its record
CRITERION = 12955           # ### OPEN_TRAILS: the domain-condition criterion (b625); the upstream and name clauses entered beneath it
UNLISTED_LINE = 13221       # ### OPEN_TRAILS: PREDICATE-UNLISTED, standing (b633), beneath the criterion
BINDER_GRAMMAR = 13002      # ### OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, priced (b626)
BUILD_CLAUSE = 12356        # ### OPEN_TRAILS: the build clause, standing (b600)
BUILD_ROUTE = 13167         # ### OPEN_TRAILS: the build route under the hold, standing (b631)
SEAL_RULE = 13307           # ### OPEN_TRAILS: the seal rule restated beneath the build clause, standing (b636)
FERRY_LINES = (11864, 12228, 12354, 12356, 12799, 13167, 13333)

# ### (R247)(5): THE MIRROR'S ROSTER -- the data file the builder reads, appended at its end (no slot moves), the builder unedited by (R96)
ROSTER = 'tools/mirror_roster.json'
ROSTER_ADD = ('day1\\A_Place_to_Stand_v5_18.md', 'phase2\\method\\THE_FINDINGS_AS_THEY_STAND_v0_6.md',
              'phase2\\method\\THE_KEYSTONE_CENSUS_v0_5.md')
BUILDER = 'tools/mirror_build.ps1'

# ### THE SEALED TOOLS -- this act's own tools that take no edit by any means until the act closes ((R246)(3), OPEN_TRAILS :13307); their
# ### sha256 recorded at the seal by the suite (`--seal`, data/b637_seal_hashes.json) and recomputed at the close by G-SEAL-HASHES
SEALED = ('b637_worklist.py', 'b637_tests.py', 'b637_record.py', 'b637_checks.py', 'b637_closing.py', 'b637_reg_gate.py', 'b637_regspec.py')

NEXT_ROUTES = [('b638, on the author`s word: the deposit (the author`s own act, with a mirror rebuilt on the new roster at b638`s close), or '
                'the census at v0.6 with (R247)(2)`s exclusion and the binder-class premise table', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
