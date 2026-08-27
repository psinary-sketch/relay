# -*- coding: utf-8 -*-
"""banked_index.py -- THE BANKED-RESULT INDEX (built b160).

### WHY THIS EXISTS. At b154 and again at b158 an act marked an object OPEN --
### the E1/even identification, "owner-quotable only as a reading" -- while the
### derivation sat banked at b35's registration since 2026-08-18. b159 found it.
### ### TWO ACTS DID NOT READ A RESULT THE RECORD ALREADY HELD.
### That is not a calibration error and not a false pass. ### IT IS A READING NOT
### DONE, and no existing law addresses it: the source-read-first law governs HOW
### a source is read, and says nothing about FINDING WHICH OWNER HOLDS A RESULT.

### THE CURE IS AN INDEX, AND THE CONVENTION THAT GOES WITH IT (b160):
### BEFORE AN OBJECT IS MARKED OPEN, NAVIGATOR-ASSERTED, OR REQUIRING A
### CONSTRUCTION, THE INDEX IS QUERIED AND THE QUERY'S RESULT REPORTED.
### An open declared without the query is a claim about the record made without
### reading it.

### THE REACH, STATED HERE AND PRINTED ON EVERY QUERY BECAUSE IT IS THE MOST
### DANGEROUS MISREADING THIS TOOL MAKES AVAILABLE:
### ### ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD.
### The index holds what the scan surfaced and a human read. A future act that
### reads "not in the index" as "not in the corpus" would repeat b158's error
### WITH A TOOL'S AUTHORITY BEHIND IT, which is worse than repeating it without.
### ### QUERYING THE INDEX IS NOT READING THE CORPUS. The convention requires the
### query; it does not license skipping the read.

### AND AN INDEX ENTRY IS A POINTER, NEVER A PROMOTION. Every entry carries the
### grade ITS OWN ACT recorded. ### WHERE THE INDEX AND THE ACT DISAGREE, THE ACT
### WINS. Nothing is re-graded by being indexed.

### THE KEY REPAIR (b164). Retrieval was by SUBSTRING over names and statements,
### and it produced FALSE HITS TWICE IN THREE ACTS: at b161 a harness matched this
### tool's own REFUSAL sentence; at b163 the query "the identity" returned a row
### about the share's physicality because that row's STATEMENT contains the word.
### ### THE CORPUS'S CENTRAL OBJECT HAD NO ROW AT ALL AND THE QUERY STILL SAID HIT.
### THE AMENDED CONVENTION, IN ONE LINE:
### ### RETRIEVAL BY STRING IS NOT RETRIEVAL BY OBJECT.
### Every row carries an explicit KEY; queries match KEYS AND ALIASES ONLY, never
### free text; ### AN UNMATCHED QUERY REPORTS **NO KEY** AND NAMES NO NEAREST
### STRING, because a nearest string is how a miss becomes a false hit.
### ITS LIMIT: ### KEYS CLOSE FALSE HITS. THEY DO NOT CLOSE FALSE MISSES -- an
### object whose key nobody declared is as invisible as before, and this repair
### must not read as a solved problem.

### THE LANE LIMIT, ADDED b181 AFTER b180 RAN EIGHT QUERIES AND GOT EIGHT MISSES:
### ### A LANE WITHOUT KEYS RETURNS MISSES THAT CARRY NO INFORMATION.
### Until b181 every key here was in the density/apportionment lane, so a query
### about the prolate/place lane could only miss -- and a miss reads like a
### finding. b181 added the prolate/place and gate lanes. ### THE LIMIT IS NOT
### RETIRED BY THAT: it now applies to whichever lane is next, and a reader who
### treats this index as covering the corpus will be wrong in the same way for a
### different reason.

Usage:
    python banked_index.py --scan                 candidates, with the curation boundary
    python banked_index.py --query <object> ...   what the record holds about an object
    python banked_index.py --table                the curated index as a markdown table
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
REPORTS = os.path.join(ROOT, 'reports')
GRADE = re.compile(r'\b(DERIVED|DERIVES)\b')

REACH = [
    "  ### REACH: ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD.",
    "  ### The index holds what the scan surfaced and a human read at content.",
    "  ### Querying the index is NOT reading the corpus.",
    "  ### An entry is a POINTER, never a promotion; the grade is its own act's,",
    "  ### and where the index and the act disagree, THE ACT WINS.",
]

# ---------------------------------------------------------------------------
# THE CURATED INDEX, KEYED (b164). Every row was read at content in its own file.
# The `grade` column is quoted from the act that produced the result, never
# re-assigned. ### KEYS ARE DECLARED, NOT DERIVED FROM PROSE.
# ---------------------------------------------------------------------------
KEYS = {
    'identity': ['the identity', 'file e', 'l-identity', 'finite-instance identity', 'h2'],
    'e1-even-bridge': ['e1/even', 'e1 even', 'sector correspondence', 'the bridge'],
    'sector-occupancy': ['sector occupancy', 'arity', 'four sectors'],
    'void-gate': ['void gate', 'the void gate', 'normalization'],
    'apportionment-family': ['apportionment family', 'the family', 'unpinned share'],
    'share-physicality': ["share's physicality", 'physicality', 'physical not gauge'],
    'double-entry': ['double entry', 'certified column double entry'],
    'apportionment-free': ['apportionment-free candidate', 'free end', 'subtract nothing'],
    'selection-criterion': ["file e's requirements", 'selection criterion', 'selection'],
    'refinement-arity': ['refinement arity', 'two-fold four-fold'],
    'exact-reduction': ['exact reduction', 'the two excesses'],
    'apportionment-grade': ["apportionment's grade", 'closed-at-bench'],
    'boundary-license': ['boundary license', 'the boundary', 'carrier edge'],
    'density-collapse': ['collapse to one density', 'the density', 'one density'],
    'mean-zero-kernel': ['mean-zero kernel', 'uniqueness sufficient condition'],
    # ### THE PROLATE/PLACE LANE, ADDED b181. ### BEFORE THIS THE INDEX HELD ONE
    # ### LANE ONLY (density/apportionment), so b180's eight queries returned
    # ### eight misses that LOOKED LIKE EVIDENCE AND WERE NOT.
    'prolate-continuum-positivity': ['prolate continuum positivity', 'continuum positivity',
                                     'prolate positivity'],
    'archimedean-positivity': ['archimedean positivity', 'archimedean-place positivity',
                              'sonin compression', 'sonin trace'],
    'w-union': ['w-union', 'the quadrant', 'nonarchimedean unbounded quadrant',
                'the residue', 't2'],
    'weil-criterion': ['weil criterion', 'the classical equivalence', 'explicit formula',
                       'equation 2', 'weil positivity'],
    'prolate-operator': ['prolate operator', 'ccm prolate', 'scaling hamiltonian',
                         'metaplectic framework'],
    # ### THE ARCHIMEDEAN-SECTOR LANE, ADDED b202. ### ITS ABSENCE HAD A MEASURED COST:
    # ### b199 wrote "the record names NO element of the archimedean Sonin space at all"
    # ### while the crown act had held one for two days, and b201 found it by READING the
    # ### crown act rather than by querying. ### b164's limit was the diagnosis in advance:
    # ### KEYS CLOSE FALSE HITS; THEY DO NOT CLOSE FALSE MISSES.
    'sonin-space': ['sonin space', "sonin's space", 's(1,1)', 's(lambda,lambda)',
                    'the archimedean sonin space'],
    'archimedean-sector': ['archimedean sector', 'the sonin sector', 'the constraint sector',
                           'the compression sector', 'e1 at infinity', 'e1(infinity)',
                           'the archimedean e1', 'plus-one sector', 'the +1 sector'],
    'sonin-eigenfunctions': ['sonin eigenfunctions', 'phi_mu', 'the named eigenfunctions',
                             'negative-eigenvalue eigenfunctions'],
    # ### AND ONE ALIAS DELIBERATELY **NOT** ADDED: the bare word 'prolate'.
    # ### It is ambiguous across prolate-continuum-positivity, prolate-operator and
    # ### sonin-eigenfunctions, and b181's precedent is that the bare 'positivity' MUST
    # ### keep returning NO KEY for exactly that reason. ### A NEAREST STRING IS HOW A MISS
    # ### BECOMES A FALSE HIT.
    # ### THE GATE LANE, ADDED b181.
    'stall-ledger': ['stall ledger', 'the traps', 'salt-check traps', 'the gates'],
    'w-family': ['w-family', 'average-vs-uniform', 'measure-zero escape',
                 'proportion not the whole'],
    'de-branges-refutation': ['de branges', 'hb-positivity', 'conrey-li',
                              'de branges positivity'],
}

INDEX = [
    # (key, act, one-line statement, grade as its own act recorded it, location)
    # ### THE ARCHIMEDEAN-SECTOR LANE'S ROWS (b202). ### EVERY GRADE IS THE ONE ITS OWN ACT
    # ### RECORDED, and two of these are IMPORTS under b146, marked as such with versions.
    ('sonin-space', 'b199 / b201 (imports, read at content)',
     "S(alpha,beta) = {xi in L2(R)_ev : xi = 0 on |q|<=alpha, F_eR xi = 0 on |p|<=beta};"
     " the archimedean one is INFINITE DIMENSIONAL",
     'IMPORT at the source text grade -- CC arXiv 2006.13771v1 (Def 4.4; intro), 24 Jun 2020.'
     ' ### ABOVE BENCH. ### The SPLIT into F-sectors is NOT at this grade',
     'data/b199_archimedean_nonvanishing.txt; data/b201_eigenfunction_exhibit.txt'),
    ('archimedean-sector', 'b200 (the naming census)',
     "THREE distinct spaces carry the name at infinity. ### NAMED BY THE AUTHOR'S FERRY AT"
     " b206: ### THE SONIN SECTOR (the +1 eigenspace of F on the archimedean Sonin space --"
     " THE GLUING SENTENCE'S OBJECT); ### THE CONSTRAINT SECTOR (act 15's constraint span"
     " E+B, v_n^+ -- ORTHOGONAL to the Sonin sector); ### THE COMPRESSION SECTOR (b33's"
     " R-prolate soft-compression modes, G F G on L2_ev)",
     'CENSUS at content, 1656 files. ### THE NAMING IS THE AUTHORS AND IS ROUTED --'
     ' both readings at THE_IDENTITY_CHAIN section 13, NEITHER RECOMMENDED.'
     ' ### The gluing sentence names (A)',
     'data/b200_sector_naming.txt; PLACE-papers phase2/method/THE_IDENTITY_CHAIN.md s13'),
    ('sonin-eigenfunctions', 'b201 / b202 (import, read at content)',
     "phi_mu, the eigenfunctions for the NEGATIVE eigenvalues of W_sa, BELONG TO THE SONIN"
     " SPACE; F_eR phi_mu = xi_mu; phi_mu != 0 by the source's own U_0(mu) = 1",
     'IMPORT at the source text grade -- Connes-Moscovici arXiv 2112.05500v1 (Cor 3.2,'
     ' Lemma 3.1), 10 Dec 2021. ### UPDATED b203: the eigenspace is ONE-DIMENSIONAL'
     ' (Ramis-Richard-Jung-Thomann, C. R. Math. 363 (2025), 1065-1081, DOI'
     ' 10.5802/crmath.780, Lemma 2(ii) -- IMPORT), ### so with commutation F phi = c phi and'
     ' with F^2 = 1 on evens (a FURTHER import, UNSTATED by either source) c = +-1.'
     ' ### SO phi_mu IS an F-eigenvector and lies in E_1 or E_-1. ### WHICH SIGN IS NOT'
     ' STATED -- ### M22 IS NOW A SIGN. ### UPDATED b204: Proposition 7 of the same 2025'
     ' paper gives psi(Lambda) = +-1 at every non-classical eigenvalue -- THE SOURCE'
     ' CONFIRMING c = +-1 AT THEOREM GRADE FOR EVERY Lambda > 0 -- and its section 4.2.3'
     ' EXHIBITS BOTH SIGNS NUMERICALLY (alpha(mu_-2) < 0, alpha(mu_-148) > 0), ### SO AT'
     ' Lambda = sqrt(2) A NAMED ELEMENT HAS c = +1. ### BUT EVERY NUMERIC IS AT tau = 4 pi,'
     ' i.e. Lambda = sqrt(2), AND THE CORPUS S SPACE IS S(1,1), Lambda = 1: ### THE'
     ' STRUCTURE TRANSFERS, THE NUMERICS DO NOT. ### M22 IS NOW sign(alpha) AT tau = 2 pi.'
     ' ### AND THE FENCE: F phi = xi IS NOT F phi = phi --'
     ' the relation is DERIVED from simplicity, not substituted',
     'data/b201_eigenfunction_exhibit.txt; data/b202_sum_test.txt;'
     ' data/b203_transform_convention.txt'),
    ('identity', 'row 24 / file E',
     "the built object's trace equals Weil's ledger on the constrained class at a cell",
     'BOUNDARY: STATED, NOT PROVED, NOT CLAIMED; its truth at complete roster is h2',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean'),
    ('e1-even-bridge', 'b35',
     'xi_n = sqrt(2)*psi_{2n}, so the E1 sector is xi_n with n EVEN and the (-1) sector n ODD',
     "banked read; used at b159 as the bridge's derivation",
     'data/b35_registration_2026-08-18.txt'),
    ('sector-occupancy', 'b159',
     "the layer occupies only two of proj4's four sectors; the +-i sectors are unoccupied",
     'DERIVES (instances) + derived read at owners',
     'data/b159_seam_and_arity.txt; Core/SectorOccupancyShadow.lean'),
    ('void-gate', 'b154',
     'sum_n w_n - A = -resid_N*(sum_n u_n - 1): the gate forces the normalization ALONE',
     'DERIVED (exact algebra); decided at instances in Core',
     'data/b154_apportionment_characterization.txt; Core/ApportionmentShadow.lean'),
    ('apportionment-family', 'b154',
     "the admissible apportionments form a ONE-PARAMETER FAMILY containing b38's as one member",
     'DERIVED',
     'data/b154_apportionment_characterization.txt'),
    ('share-physicality', 'b155',
     'the identity residual moves with the share at rate resid_N; at most one share admits it',
     "DERIVED, conditional on b107's undischarged T-reading",
     'data/b155_nu.txt; Core/ShareDependenceShadow.lean'),
    ('double-entry', 'b156',
     'the column enters the closed equation twice; the entries net to (1 - mu), not cancelling',
     'DERIVED (exact); decided at instances',
     'data/b156_seam_and_joint.txt; Core/DoubleEntryShadow.lean'),
    ('apportionment-free', 'b156',
     'the purely object-side formula equals W+(0): a FAMILY MEMBER, not an escape',
     'DERIVED',
     'data/b156_seam_and_joint.txt'),
    ('selection-criterion', 'b158',
     'no owner-quotable requirement constrains the share; the freedom is DEFINITIONAL',
     'DERIVED (reads at owners); branch (c)',
     'data/b158_selection.txt'),
    ('refinement-arity', 'b158',
     'a two-fold aggregate does not determine a four-fold split',
     'DERIVES (instances)',
     'data/b158_selection.txt; Core/RefinementArityShadow.lean'),
    ('exact-reduction', 'b109',
     "W+ - sigma_even*A = the raw trace's even-share excess minus the eps integral's",
     'DERIVED, exact algebra',
     'data/b109_apportionment_derivation.txt'),
    ('apportionment-grade', 'b107',
     'the joint is CLOSED-AT-BENCH and OPEN-AT-DERIVATION',
     'the two-grade reconciliation, decided at content',
     'data/b107_apportionment.txt'),
    ('boundary-license', 'b151',
     'no license derives; all three routed candidates were reads, and a license needs a construction',
     'branch (b); the negative-read fence rides',
     'data/b151_boundary.txt'),
    ('density-collapse', 'b115',
     "the deviation's window-dependence reduces to a fixed-kernel scale-average of ONE density",
     'DERIVED; decided at instances',
     'data/b115_mechanism.txt; Core/MechanismShadow.lean'),
    ('mean-zero-kernel', 'b116',
     'Phi_K is mean-zero with one sign change, so Psi monotone increasing => the window is unique',
     'DERIVED',
     'data/b116_thirteenth_seam_close.txt'),

    # ### THE PROLATE/PLACE LANE AND THE GATE LANE, ADDED b181.
    # ### EVERY GRADE BELOW IS THE ONE ITS OWN ACT RECORDED. ### A KEY IS A POINTER,
    # ### NEVER A PROMOTION: adding a key for an object the corpus calls UNPROVEN
    # ### does not make it less unproven, and the grade column says so.
    ('prolate-continuum-positivity', 'b180',
     'the object the gamma-04 stall ledger calls RH-equivalent; NAMED TWICE IN THE LIVE '
     'CORPUS AND DEFINED NOWHERE, and it carries NO PLACE QUANTIFIER',
     "UNPROVEN -- the corpus's own word at GAMMA04_ATTEMPT_SPEC.md:34; and b180: the "
     'derivation to the classical equivalence is NOT HELD in the record',
     'data/b180_derivation_search.txt'),
    ('archimedean-positivity', 'b180',
     'the Sonin-compression positivity at the archimedean place',
     'PROVED AT THE ARCHIMEDEAN TRUNCATION; OPEN BEYOND IT -- the record\'s own words',
     'data/b180_derivation_search.txt'),
    ('w-union', 'b180',
     "the (nonArchimedean, unbounded) quadrant -- the record's own name for the distance "
     'between one place\'s term and the sum over all places; technique T2',
     'THE QUADRANT LOCATED; COMPILED axiom-free. ### CARRIED AS AN OPEN OBSTRUCTION, '
     'NOT AS A DERIVATION -- "where every located attempt stops"',
     'data/b180_derivation_search.txt'),
    ('weil-criterion', 'b179',
     'RH <==> sum over ALL PLACES of W_v(g*g-bar-sharp) <= 0 -- eq. (2) of 2006.13771v1',
     'EXTERNAL, quoted at content; credited by that work to A. Weil [33] following '
     'H. Yoshida [34]. ### NOT the corpus\'s result and NOT about one place',
     'data/b179_enforcement_and_equivalence.txt'),
    ('prolate-operator', 'b177',
     'the CCM prolate / metaplectic framework, the scaling Hamiltonian',
     'EXTERNAL, CONFIRMED-AT-CONTENT at 2310.18423 (abs as served 2026-08-25)',
     'data/b177_trim_print_and_citations.txt'),
    ('stall-ledger', 'b181',
     "GAMMA04_ATTEMPT_SPEC.md (d): six salt-check traps that close attempts in advance",
     'SWEPT b181: 3 grounds HELD at content (items 1, 4, 5), 1 external citation '
     'UNRESOLVED (item 3), ### 2 resting on objects NOT LOCATED at content (items 2, 6)',
     'data/b181_gate_sweep.txt'),
    ('w-family', 'b181',
     'the average-vs-uniform wall: a proportion is never the whole (the measure-zero escape)',
     'GROUND HELD AT CONTENT -- owners beyond the gate: HELD_COMPLETER_ASSESSMENT.md:13, '
     'HELD_WPRIMEPHYS_crystallization.md:20, THE_CORNER_MAP.md:24',
     'data/b181_gate_sweep.txt'),
    ('de-branges-refutation', 'b181',
     'the direct HB-positivity route for zeta, closed by a cited external refutation',
     '### EXTERNAL CITATION (Conrey-Li 2000), TWO INTERNAL OWNERS, ### NO BIBLIOGRAPHY '
     'KEY -- unresolved in the b175 backlog. ### AN UNVERIFIED CITATION IS NOT A FALSE ONE',
     'data/b181_gate_sweep.txt'),
]


def scan():
    """### THE MECHANICAL HALF. It surfaces candidates; it does not grade them."""
    hits = []
    for base in (DATA, REPORTS):
        if not os.path.isdir(base):
            continue
        for fn in sorted(os.listdir(base)):
            if not fn.endswith(('.txt', '.md')):
                continue
            p = os.path.join(base, fn)
            try:
                lines = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
            except Exception:
                continue
            for i, L in enumerate(lines, 1):
                if GRADE.search(L):
                    hits.append((fn, i, L.strip()[:96]))
    return hits


def cmd_scan():
    hits = scan()
    files = len({h[0] for h in hits})
    print("=" * 78)
    print("BANKED-RESULT INDEX -- THE SCAN (candidates only)")
    print("=" * 78)
    print("  grade-word lines found : %d" % len(hits))
    print("  files carrying them    : %d" % files)
    print("  ### CURATED INTO THE INDEX : %d" % len(INDEX))
    print("  ### THE CURATION BOUNDARY IS STATED, NOT HIDDEN: most candidates are")
    print("  ### grade words in prose rather than indexable results, and the")
    print("  ### difference between %d and %d is a HUMAN READ, not a filter."
          % (len(hits), len(INDEX)))
    print("  ### AN INDEX THAT HID ITS OWN SELECTION WOULD BE AN UNSTATED TRUNCATION.")
    for s in REACH:
        print(s)
    return 0


def cmd_query(terms):
    q = " ".join(terms).lower()
    print("=" * 78)
    print("BANKED-RESULT INDEX -- QUERY: %r" % q)
    print("=" * 78)
    # ### KEYED RETRIEVAL: the query must match a DECLARED key or alias.
    # ### It is NEVER matched against statements -- that produced b163's false hit.
    key = None
    for k, aliases in KEYS.items():
        if q == k or q in [a.lower() for a in aliases]:
            key = k
            break
    found = [e for e in INDEX if key is not None and e[0] == key]
    if found:
        print("  ### THE RECORD HOLDS %d INDEXED RESULT(S) ABOUT THIS OBJECT:" % len(found))
        for obj, act, stmt, grade, loc in found:
            print("\n    key      : %s" % obj)
            print("    act      : %s" % act)
            print("    result   : %s" % stmt)
            print("    grade    : %s   ### as its own act recorded it" % grade)
            print("    location : %s" % loc)
    else:
        print("  ### NO KEY.")
        print("  ### The query matched no DECLARED key or alias. No nearest string")
        print("  ### is offered: a nearest string is how a miss becomes a false hit.")
        print("  ### THIS IS NOT A FINDING THAT THE RECORD HOLDS NOTHING.")
    print()
    for s in REACH:
        print(s)
    return 0


def cmd_table():
    print("| key | act | the result, in one line | grade, as its own act recorded it | location |")
    print("|:--|:--|:--|:--|:--|")
    for obj, act, stmt, grade, loc in INDEX:
        print("| `%s` | `%s` | %s | *%s* | `%s` |" % (obj, act, stmt, grade, loc))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == '--scan':
        return cmd_scan()
    if argv[0] == '--query':
        if len(argv) < 2:
            print("  ### --query needs an object name.")
            return 2
        return cmd_query(argv[1:])
    if argv[0] == '--table':
        return cmd_table()
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
