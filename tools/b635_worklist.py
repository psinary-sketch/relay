# -*- coding: utf-8 -*-
"""b635_worklist.py -- THE ACT'S DATA, UNDER (R245). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b635: LANE THREE, ACT SIXTY-TWO -- THE TWELVE DISAGREEMENTS RULED FOR THE ELABORATED READING AND THE TEXTUAL RULE REPAIRED;
### THE THIRTEEN PHANTOM NAMES RESOLVED OR CORRECTED; THE CASCADE REBUILT; THE MIRROR REFRESHED WITH THE ROOT LINE; THE DEPOSIT
### DESCRIPTION'S ITEMS BANKED, NOTHING DEPOSITED. Here: the pins before the act; the kernel and its pin; the lists in force; the
### twelve and the thirteen; the census and sieve paths; the ledger lines; the mirror's prior build; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
GS = 'D:/SIDE-global-section'
PRE_PP = '9a929ce'          # ### PLACE-papers main before the act (b634's record)
PRE_RELAY = 'f022c6ab'      # ### relay main before the act (b634's closing)
STEPZERO = '677bb154'       # ### relay: b634's closing push-out bank, committed at step zero
DATE = '2026-10-07'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}          # ### the lists in force since b632
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}   # ### b635, the author's answer to the Pages prompt: the fresh probes
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R245)(4): THE KERNEL AND ITS PIN
KERNEL = 'SIDE-explicit-formula'
KER_TAG, KER_PIN = 'v0.25', '8c51431'
KER_PIN_FULL = '8c51431ada7798c65fa26b07ef99a447d7c15735'
HOLD_MB = 2560
CLASSES = ('section variable', 'auto-bound implicit', 'header cut', 'notation or coercion', 'other')   # ### (R244)(4), in its order

# ### (R245)(2): THE TWELVE -- the eleven that move to the elaborated reading, and the row retired as naming no declaration
CHI8 = ['SIDEExplicitFormula.GRHWeil.Generic.' + n for n in (
    'chi_EF_explicitFormulaPaper_of_lit', 'chi_EF_prop_EF_of_lit', 'chi_Tail_eventually_tailInputs', 'chi_Tail_norm_sq_uvec_le',
    'chi_Tail_norm_uvec_le', 'chi_ZeroConfig_finsum_mult_mono', 'chi_ZeroConfig_ncard_le_finsum_mult', 'chi_ZeroConfig_ncard_mono')]
ELEVEN = CHI8 + ['ZerosBound', 'SIDEExplicitFormula.B321.paperFT_growth', 'SIDEExplicitFormula.B321.paperFT_growth_at']
RETIRED_NAMESPACE = 'Finset'
# ### (R245)(4): THE CASCADE
CASCADE = ['SIDEExplicitFormula/SaltCheckDoubling', 'SIDEExplicitFormula/Schema/SaltCheckFamily']

# ### the census, the sieve, the README's paragraph
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'

# ### the ledger lines the act reads and addresses
B634_ENTRY = 7747           # ### FINDINGS: b634's entry
B634_RECORD = 13253         # ### OPEN_TRAILS: b634's trail record
B634_CORRECTION = 13277     # ### OPEN_TRAILS: b634's correction
HEADLINE = 13251            # ### OPEN_TRAILS: the closing's head line, standing (b634)
CLOSING_FORM = 13028        # ### OPEN_TRAILS: the closing form, a clause at the record's form (b627)
MANIFEST_LINE = 12929       # ### OPEN_TRAILS: the mirror's root line in its stage, standing
GATE_WO = 13000             # ### OPEN_TRAILS: W-ORD-GATE-FROM-ELABORATOR (b626)
BINDER_GRAMMAR = 13002      # ### OPEN_TRAILS: W-ORD-BINDER-GRAMMAR, priced (b626)
BUILD_ROUTE = 13167         # ### OPEN_TRAILS: the build route under the hold, standing (b631)
MIRROR_PRIOR_MD5 = '20ed9b0572787dc2a14984922153ff4c'   # ### the 2026-10-04 build's zip md5, the ruling's

NEXT_ROUTES = [('b636, on the author`s word: the deposit (the author`s own act), or W-ORD-BINDER-GRAMMAR with the 20 unnamed rows as its '
                'test set, or the elaborated reader over SIDE-structural-error-correction', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
