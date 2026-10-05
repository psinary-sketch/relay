# -*- coding: utf-8 -*-
"""b623_worklist.py -- THE ACT'S DATA, UNDER (R233). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b623: LANE THREE, ACT FIFTY -- THE UNPUSHED TAGS SETTLED BY CITATION; THE DE-ALIGNMENT KERNEL'S AXIOM ARTEFACT PRINTED AND ITS
### ROWS ENTERED; FOUR RESEARCH WORK-ORDERS AND ONE ARM ENTERED.
### Here: the pins before the act; the twelve unpushed tags of the census's cells and the ledgers their citations are read in, with the
### citation reader the author ruled before the seal (b611's prose matcher, and a version cell beside the kernel's own cell in a table
### row); the SIDE-structural-error-correction names (the pin, the branch, the tag, the modules, the artefact); the four work-orders'
### wordings ((R233)(4)), in the ruling's words where it gives them.
"""
import io
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'c9e9a9c'          # ### PLACE-papers main before the act (b622's record)
PRE_RELAY = '5d0816dd'      # ### relay main before the act (b622's closing)
STEPZERO = '6cbe1a2a'       # ### relay: b622's closing push-out bank, committed at step zero
DATE = '2026-10-04'

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}        # ### b622's lists, the column's line carried
OLD_NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}    # ### the lists without the column
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}

# ================================================================================ (R233)(5)(a): THE TWELVE TAGS
# ### the census's cells (THE_KEYSTONE_CENSUS_v0_4.md, "unpushed by name"), each (kernel, tag, its commit as the census printed it)
TAGS = [('SIDE-bijection', 'v0.1', 'dd487e6'), ('SIDE-class-coupling', 'v0.1', 'b6a6e86'), ('SIDE-coupling', 'v0.1', '4ab0bf5'),
        ('SIDE-formation-arithmetic', 'v0.1', '7ac35d8'), ('SIDE-meta', 'v0.1', 'e262713'), ('SIDE-meta', 'v0.3', '6bb7b23'),
        ('SIDE-omega-b', 'v0.1', '9c80279'), ('SIDE-orchestrator', 'v0.1', 'f0fcc40'), ('SIDE-residual-bridge', 'v0.1', 'b473d4b'),
        ('SIDE-substrate-cluster', 'v0.1', '5b102b4'), ('SIDE-substrate-cluster', 'v0.2', '9068d3c'), ('SIDE-substrate-cluster', 'v0.4', '06b61c3')]
TAG_KERNELS = sorted(set(k for k, _t, _s in TAGS))
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
# ### the ledgers (R233)(5)(a)'s ferry names for a citation: REGISTRY, FINDINGS, SPIRAL_MAP (its current file and its v0.7 edition), the pages
RULED_LEDGERS = ('REGISTRY.md', 'FINDINGS.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', PAGE, DIR_PAGE)
# ### read and printed beside, never counted: b611's other ledgers (OPEN_TRAILS names every tag in the work-order itself)
BESIDE_LEDGERS = ('OPEN_TRAILS.md', 'ERRATA.md', 'VERIFICATION_LOOM.md', 'README.md')
REGISTRY_NOTE_LINE = 628    # ### the row note naming the tags verified to exist (substrate-cluster v0.4, bijection v0.1)
OT_TAG_REMOTES = 12597      # ### W-ORD-TAG-REMOTES
OT_SEC = 12330              # ### W-ORD-SEC-AXIOM-ARTEFACT


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def prose_rx(repo, tag):
    """### b611's matcher (tools/b611_claims.py, tag_citations), carried: the kernel's name, with or without `SIDE-`, then the tag as a whole
    ### version within 40 characters on one line and no table pipe between (`v0.1` does not match inside `v0.1.0`)."""
    name = repo[len('SIDE-'):]
    return re.compile(r'(?:SIDE-)?%s\b[^|\n]{0,40}?\b%s(?![.\d])' % (re.escape(name), re.escape(tag)))


def cell_hit(line, repo, tag):
    """### the second shape, the author's answer before the seal: a table row with the kernel's own cell (its name, backticks and bold
    ### stripped) followed at once by a version cell that is the tag exactly."""
    if not line.startswith('|'):
        return False
    cells = [c.strip().strip('`*').strip() for c in line.split('|')]
    return any(cells[i] == repo and cells[i + 1] == tag for i in range(len(cells) - 1))


def citations(repo, tag, texts):
    """### {file: [(line, shape, text)]} over the given ledger texts; shape is 'prose' or 'cell'."""
    rx = prose_rx(repo, tag)
    out = {}
    for f, t in texts.items():
        for i, l in enumerate(lines_of(t), 1):
            if rx.search(l):
                out.setdefault(f, []).append((i, 'prose', l))
            elif cell_hit(l, repo, tag):
                out.setdefault(f, []).append((i, 'cell', l))
    return out


# ================================================================================ (R233)(5)(b): SIDE-structural-error-correction
SEC = 'D:/SIDE-structural-error-correction'
SEC_NAME = 'SIDE-structural-error-correction'
SEC_PIN = ('v0.2.1', '6a4f482')
SEC_TAG = 'v0.2.2'
SEC_BRANCH = 'sec-axiom-b623'
SEC_PUSH = 'push-b623-sec'
SEC_MODULES = ('SIDEStructuralErrorCorrection/Basic.lean', 'SIDEStructuralErrorCorrection/DeAlignment.lean')
SEC_ROOT_MODULE = 'SIDEStructuralErrorCorrection'
SEC_ARTEFACT = 'AxiomCheck.lean'
SEC_SIX = ('DeAlignment.no_domain_covers_line', 'DeAlignment.single_domain_fault_not_logical', 'DeAlignment.dealigned_of_lines_injective',
           'DeAlignment.fano_dealignment_decidable_example', 'DeAlignment.fano_collapsed_line_rejected', 'DeAlignment.fano_two_design')
SEC_NAMED = ('SIDEStructuralErrorCorrection.d_eff_formula', 'SIDEStructuralErrorCorrection.silence_yields_protection')
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
DECL_RX = re.compile(r'^(theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+([A-Za-z_][A-Za-z0-9_.]*)', re.M)


def sec_exports(rev=SEC_PIN[1]):
    """### every declaration of the two modules at the pin, read from the blobs: [(module, line, kind, fully qualified name)]; the
    ### namespace read from the file's own `namespace`/`end` lines."""
    out = []
    for m in SEC_MODULES:
        t = show(m, rev, SEC)
        if t is None:
            return None
        ns = []
        for i, l in enumerate(lines_of(t), 1):
            mm = re.match(r'^namespace\s+(\S+)', l)
            if mm:
                ns.append(mm.group(1))
                continue
            me = re.match(r'^end\s+(\S+)', l)
            if me and ns and ns[-1] == me.group(1):
                ns.pop()
                continue
            md = DECL_RX.match(l)
            if md:
                out.append((m, i, md.group(1), '.'.join(ns + [md.group(2)])))
    return out


# ================================================================================ (R233)(4): THE FOUR WORK-ORDERS, IN THE RULING'S WORDS
WORK_ORDERS = [
    ('W-ORD-PLATT-RUNG', '(i)',
     'the finite-support ladder’s rung at a published height: “every zero of ζ with |Im ρ| ≤ T lies on the line” for the height of a '
     'named numerical verification (Platt–Trudgian’s, to be cited at its DOI when the work-order runs) entered as a T1-lit premise, and '
     'h2_sign_iff_forall_upto’s finite side instantiated at that T, so the kernel carries the numerical tradition’s certificate as a rung '
     'at its honest grade', 'one act, one module, no new analysis'),
    ('W-ORD-NYMAN-BEURLING-FACE', '(ii)',
     'the Nyman–Beurling criterion (density of the dilations of the fractional-part function in L²(0,1)) and Báez-Duarte’s countable '
     'form as a fourth face of the clause, stated as Props over Mathlib’s L² with the equivalence to RH as a T1-lit premise, and its '
     'finite rungs d_N as a bench', 'two acts, the equivalence INTERFACES until a proof is vendored or written'),
    ('W-ORD-DEDEKIND-INSTANCE', '(iii)',
     'the Dedekind zeta of ℚ(ζ_q) as a configuration of the schema by the family theorem, the two named premises of (R213)(3)(d) (the '
     'trivial character’s pole term, the Euler factors at p | q) stated as the instance’s premises in INTERFACES form',
     'one act'),
    ('W-ORD-MARGIN-BENCH', '(iv)',
     'for ζ, the window value at the ordinate of each of the lowest N on-line zeros computed from the prime side to a certified '
     'precision, the minimum over N printed as the positivity margin at height, beside the super-repulsion fit, as a T3/T4 bench with '
     'no claim', 'one act'),
]
