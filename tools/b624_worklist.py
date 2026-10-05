# -*- coding: utf-8 -*-
"""b624_worklist.py -- THE ACT'S DATA, UNDER (R234). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b624: LANE THREE, ACT FIFTY-ONE -- THE E0 GATE'S READING OF INDUCTION STEPS, WITH ITS TEST AND THE χ PAGE RE-EMITTED; THE
### ACT ROOT CHAINED FROM THIS ACT AND VERIFIED BY A SUITE ARM.
### Here: the pins before the act; the kernel nodes the clause is tested on; the planted directory; b623's five readings and the
### clauses each resolves ((R234)(1)); the standing MANIFEST line (the author's answer before the seal); the banks the act root
### names.
"""
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KER = 'D:/SIDE-explicit-formula'
PRE_PP = '271de07'          # ### PLACE-papers main before the act (b623's record)
PRE_RELAY = '884d0848'      # ### relay main before the act (b623's closing)
STEPZERO = '313b8e48'       # ### relay: b623's closing push-out bank, committed at step zero
DATE = '2026-10-05'
V021 = ('v0.21', '1d5d4dd')

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
OLD_NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}

E0_FILES = ('tools/e0_rule.py', 'tools/test_e0_rule.py')
ROOT_FILES = ('tools/act_root.py', 'tools/test_act_root.py')
# ### (R234)(2)'s named nodes at v0.21: the product lemma over a Finset and its step lemma, with the match-arm case the clause cuts
CLAUSE_NODES = [('SIDEExplicitFormula.Schema.Family.finsetSum_productLemma', 'SIDEExplicitFormula/Schema/Family.lean', 136),
                ('SIDEExplicitFormula.Schema.Family.finsetSum_insert', 'SIDEExplicitFormula/Schema/Family.lean', 130),
                ('SIDEExplicitFormula.Schema.Family.family_theorem', 'SIDEExplicitFormula/Schema/Family.lean', 213),
                ('SIDEExplicitFormula.PowerWindow.power_contDiff', 'SIDEExplicitFormula/PowerWindow.lean', 139)]
# ### the four ledger cells that grade finsetSum_insert INTERFACES in the table (the table's own reader, at relay 884d0848)
INSERT_CELLS = [('FINDINGS.md', 7058), ('OPEN_TRAILS.md', 12424), ('OPEN_TRAILS.md', 12434), ('OPEN_TRAILS.md', 12438)]

# ### (R234)(1): b623's five readings marked "Resolved by the seat", each as b623's trail record (OPEN_TRAILS :12899) printed it,
# ### and the clause each resolves -- (the line it is re-printed beside, what that line is)
READINGS = [
    (12597, 'W-ORD-TAG-REMOTES', '(1)'),
    (12597, 'W-ORD-TAG-REMOTES', '(2)'),
    (12330, 'W-ORD-SEC-AXIOM-ARTEFACT', '(3)'),
    (12330, 'W-ORD-SEC-AXIOM-ARTEFACT', '(4)'),
    (12899, 'b623`s record, the ferry`s procedural line on the page arm', '(5)'),
]
ACT_ROOT_OT = 12210        # ### W-ORD-ACT-ROOT


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def b623_readings():
    """### the five readings as b623's trail record printed them: {'(1)': text, ...}, read from OPEN_TRAILS :12899's
    ### "Resolved by the seat" line at PLACE-papers PRE_PP."""
    ot = lines_of(show('OPEN_TRAILS.md'))
    line = [l for l in ot[12898:12917] if l.startswith('**Resolved by the seat, for the author’s strike:**')]
    if not line:
        return {}
    body = line[0].split('**Resolved by the seat, for the author’s strike:**', 1)[1].strip().rstrip('.')
    parts = re.split(r'(?:^|;\s)\((\d)\)\s', body)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out['(%s)' % parts[i]] = parts[i + 1].strip().rstrip(';').strip()
    return out
