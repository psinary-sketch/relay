# -*- coding: utf-8 -*-
"""b633_worklist.py -- THE ACT'S DATA, UNDER (R243). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b633: LANE THREE, ACT SIXTY -- THE KEYSTONE CENSUS AT v0.5: THE KERNEL COLUMN AT THE ROOT'S LIST, THE FOUR NEW FACES,
### PROVENANCE PER CLUSTER, PHASE 2 READ AGAINST SEC, THE 42 NAMED PREMISES IN BACK MATTER; TWO PREDICATES ENTERED IN THE RULE; THE
### READER AND DELIVERY FORMS AMENDED; THE b630 TEST FROZEN. Here: the pins before the act; the census's paths; the faces; SEC's pin;
### the Phase 2 rows and their syntheses; the intake banks; the ledger lines the record lines address; the rule's two entries.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
SEC = 'D:/SIDE-structural-error-correction'
PRE_PP = 'e67c43b'          # ### PLACE-papers main before the act (b632's record)
PRE_RELAY = '8e6b63cc'      # ### relay main before the act (b632's closing)
STEPZERO = 'aabdee5e'       # ### relay: b632's closing push-out bank, committed at step zero
DATE = '2026-10-06'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}          # ### the lists in force since b632
PROBE = {'zeta': 'b632_probe_out.txt', 'chi': 'b632_chi_probe_out.txt'}       # ### their probes
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R243)(6): THE CENSUS
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
CEN4_PP = '6a3069e'         # ### the PLACE-papers commit that wrote v0.4: the baseline of a dated append since v0.4
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
ROOT_ACT = 'b632'           # ### the act-root line whose repository list the kernel column takes
FACES = [   # ### (R243)(6)(ii): the explicit-formula kernel's faces at v0.22-v0.25, by tag, commit, module prefix (or a declaration)
    ('F1', 'the Platt rung', 'v0.22', 'e939c92', 'SIDEExplicitFormula.PlattRung.', 'SIDEExplicitFormula/PlattRung.lean'),
    ('F2', 'the two_thirds citation', 'v0.23', '98b7668', 'SIDEExplicitFormula.Simplicity.SimpleProportion', 'SIDEExplicitFormula/Simplicity.lean'),
    ('F3', 'the Nyman–Beurling face', 'v0.24', 'aa17442', 'SIDEExplicitFormula.NymanBeurling.', 'SIDEExplicitFormula/NymanBeurling.lean'),
    ('F4', 'the Dedekind instance', 'v0.25', '8c51431', 'SIDEExplicitFormula.Schema.Dedekind.', 'SIDEExplicitFormula/Schema/Dedekind.lean'),
]
SEC_TAG, SEC_COMMIT = 'v0.2.2', '6bf19ab'
PHASE2 = [   # ### (R243)(6)(iv): the Phase 2 rows and the syntheses that carry their claims
    ('R12', '2B', 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md'),
    ('R14', '2D', 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md'),
    ('R16', '2F', 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md'),
    ('R17', '2G', 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md'),
]
INTAKE = ('data/b628_intake_summary.txt', 'data/b628_intake_summary.json')   # ### the ANNEX row's figures: the summary banks, by digest

# ### (R243)(2): THE RULE'S TWO ENTRIES, each with the variable it restricts and its definition's file and line (git grep at the pin)
ENTRIES = [
    dict(head='Alt2', where='SIDE-global-section 17ce9ff, Core/LadderOrientationShadow.lean :95',
         reads='def Alt2 (c : Nat → U4) : Prop := ∀ k, c (k + 2) = mul m1 (c k) -- a condition on c alone', restricts=('c',)),
    dict(head='Alternates', where='SIDE-global-section 17ce9ff, Core/AlternationShadow.lean :33 and Core/SignTransferShadow.lean :47',
         reads='def Alternates (s : Nat → Int) : Prop := ∀ i, s (i + 1) = -s i -- a condition on s alone', restricts=('s',)),
]
MET_PIN = '8e6b63cc'        # ### the author's answer before the seal: MET = the named predicates the table's rule rows carry at this relay pin

# ### the ledger lines the act reads and addresses
B632_ENTRY = 7701           # ### FINDINGS: b632's entry
B632_RECORD = 13195         # ### OPEN_TRAILS: b632's trail record
CRITERION = 12955           # ### OPEN_TRAILS: the domain-condition criterion (b625)
READER_FORM = 12839         # ### OPEN_TRAILS: the second-reader form's clause (b621)
CLOSING_FORM = 13028        # ### OPEN_TRAILS: the closing form, a clause at the record's form (b627)
BINDER_GRAMMAR = 13002      # ### OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, priced (b626)
TESTPIN = 13193             # ### OPEN_TRAILS: the test-pin line, standing (b632)

B630_TEST_PIN = ('v0.24', 'aa17442')    # ### (R243)(4): the b630 test's own pin
B630_LIST_REV = 'e99c6de4'              # ### relay: the commit that wrote b630's ζ list

NEXT_ROUTES = [('b634, W-ORD-GATE-FROM-ELABORATOR (OPEN_TRAILS :13000) if the author`s word falls there, else the (R110) deposit '
                'preparations with the census and the root', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
