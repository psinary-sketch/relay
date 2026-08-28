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
    # ### THE PROLATE-ARC LANE, ADDED b216. ### ITS ABSENCE HAD A MEASURED COST AND THE
    # ### COST WAS RECORDED SIX TIMES: b210, b211, b212, b213, b214 and b215 each queried
    # ### the objects their own act was about and each got misses. ### b211's five
    # ### (alpha, beta, psi, wronskian, alternation) are the list this act was sent to close.
    'alpha': ['alpha', 'the connection coefficient', 'connection coefficient',
              'alpha(mu)', 'psi(lambda)'],
    'beta': ['beta', 'the spectral determinant', 'spectral determinant',
             'the connection coefficient beta', 'f(tau,mu)'],
    'psi': ['psi', 'the asymptotic solution', 'psi_mu', 'the sine solution',
            'the cosine solution'],
    'wronskian-identity': ['wronskian', 'the wronskian identity', 'wronskian identity',
                           'the wronskian gate', 'alpha beta prime'],
    'alternation': ['alternation', 'the alternation', 'sign alternation',
                    'alternates'],
    'the-ladder': ['the ladder', 'rank ladder', 'the rank ladder', 'i^k ladder',
                   'the orientation bits', 'orientation bits', 'epsilon and orientation'],
    'odd-family': ['odd family', 'the odd family', 'odd eigenfunctions', 'parity',
                   'the parity families'],
    'transform-convention': ['transform convention', 'the transform convention',
                             'fourier convention', 'the exponent sign'],
    'eigenfunction-scale': ['eigenfunction scale', 'the eigenfunction scalar',
                            'eigenfunction scalar', 'xi normalization'],
    # ### THE TERM-2 LANE, ADDED b216. ### b215's four misses were EVERY OBJECT THAT ACT
    # ### WAS ABOUT, and 'class richness' had missed in every query since b188.
    'class-richness': ['class richness', 'the class-richness lemma', 'classrichness',
                       'class-richness'],
    'file-d': ['file d', 'the quotient trace file', 'the missing file'],
    'quotient-trace': ['quotient trace', 'term 2', 'the quotient channel', 'tau_q'],
    'weil-ledger': ['weil ledger', 'the atlas columns', 'w_infinity', 'the ledger'],
    # ### THE FILING LANE, ADDED b216 -- two objects that are NOT results and whose rows
    # ### say so on their face.
    'parked-note': ['the parked note', 'parked note', 'the external note',
                    'note to rrt', 'the rrt note'],
    'naming-ruling': ['the naming ruling', 'naming ruling', "term 3's archimedean factor",
                      'term 3 archimedean factor'],
    # ### THE TERM-3 / CELL-ASSEMBLY LANE, ADDED b221 UNDER ITS CLAUSE (g).
    # ### b219 AND b220 FOUND THE INDEX KEYED BY VERDICTS AND NOT BY SUBJECTS;
    # ### b221 FOUND THE SHARPEST CASE -- 'restricted tensor' RETURNED NO KEY AT TEN ACTS,
    # ### INCLUDING b193 AND b194 THEMSELVES, THE ACTS THAT PLANNED AND THEN RETIRED IT.
    'restricted-tensor-retired': ['restricted tensor', 'restricted-tensor',
                                  'restricted tensor product', 'term 3 plan'],
    'e1-unit-purity': ['e1 unit purity', 'e1-unit purity', 'schmidt purity',
                       'schmidt-pure', 'mixed-forced', 'e1 units'],
    'unit-normalized-trace': ['unit-normalized trace', 'unit normalized trace',
                              'restricted-tensor trace'],
    'weil-ledger-target': ['weil ledger target', 'cell-level target', 'ledger value',
                           'log p convention'],
    # ### THE SIGN AND IMPORT KEYS, ADDED b232 UNDER ITS CLAUSE (e).
    'sign-of-a': ['sign of a', 'the sign of a', 'sign of A', 'winf sign',
                  'archimedean sign', 'cc convention', 'the cc convention',
                  'w_infinity sign', 'sign dictionary'],
    'import-ledger': ['import ledger', 'the import ledger', 'imports',
                      'imported statement', 'named import', 'imp-1', 'imp-2'],
    # ### THE FACTOR KEY, ADDED b231 UNDER ITS CLAUSE (e).
    'the-two': ['the two', 'the factor 2', 'factor 2', 'the factor two',
                'folded mirror', 'folded mirror term', 'the fold', 'evenness',
                'two-ended sum', 'mirror term'],
    'staircase': ['the staircase', 'staircase', 'effective cutoff', 'active places',
                  'active-place set'],
    'aggregation': ['the aggregation', 'aggregation', 'cell-level assembly', 'assembly'],
    # ### THE CLASSICAL-SOURCE AND RANGE-LAW KEYS, ADDED b222 UNDER ITS CLAUSE (g).
    'von-neumann-product': ['von neumann', 'von neumann 1939', 'c0-sequence', 'c0 sequence',
                            'incomplete direct product', 'infinite direct products'],
    'range-law-species': ['range law', 'range-law species', 'the range law',
                          'carried past its range'],
    'residue-four-faces': ['residue keystone', 'four faces', 'four faces of the residue',
                           'the four-way wall'],
    # ### THE LEVEL-TOWER KEYS, ADDED b223/b224 UNDER THEIR CLAUSE (d).
    'level-limit-standing': ['level limit', 'level-limit', 'the level limit',
                             'arrival depth', 'd1 law', 'level tower'],
    'tower-iota': ['tower', 'the tower', 'iota', 'connecting map', 'exact tower',
                   'sector arithmetic', 'iota-stable'],
    'segre-open-cells': ['segre', 'segre question', 'segre work-order',
                         'quadric system', 'open cells'],
    # ### THE CLOSE'S KEYS, ADDED b225 UNDER ITS CLAUSE (c).
    'quarter-density': ['quarter density', 'quarter-density', 'one quarter',
                        'sector density'],
    'mersenne-curio': ['mersenne', 'mersenne curio', 'perfect number', 'the curio'],
    'm21-decided': ['m21', 'the re-scope', 're-scope', 'decided-by-re-scope',
                    'stated choice'],
    'archimedean-sector-invariant': ['wanted poster', 'w-ord', 'sector invariant',
                                     'd1 infinity'],
    # ### AND THE ALIASES DELIBERATELY **NOT** ADDED, EXTENDING b181's PRECEDENT:
    # ### the bare 'prolate' (ambiguous across three keys -- b181's own reason, unchanged);
    # ### the bare 'sign' (ambiguous across alpha, alternation, the-ladder and b205's
    # ### discrepancy); the bare 'the identity' is already taken by row 24 and is NOT
    # ### reused for the Wronskian identity. ### A NEAREST STRING IS HOW A MISS BECOMES A
    # ### FALSE HIT, AND THAT SENTENCE IS OLDER THAN THIS ACT.
}

INDEX = [
    # (key, act, one-line statement, grade as its own act recorded it, location)
    # ### THE CLOSE'S ROWS (b225).
    ("quarter-density", "b57/b198 (finite) / b211-b212 (archimedean) / b225 (filed)",
     "each F-sector carries one quarter: at odd q EXACTLY one quarter at every level"
     " (shape d,d,d,d); at q = 2^n one quarter up to a single dimension with the surplus"
     " always in E_i (shape d,d,d+1,d), density -> 1/4; and at infinity the ladder form"
     " gives each sector RANK DENSITY 1/4",
     "### TWO GRADES, KEPT SEPARATE AND NOT FUSED. Finite places: DERIVES from the closed"
     " forms, re-derived exactly at 13 cells by b223. Archimedean:"
     " DERIVATION-ON-IMPORTS (b211/b212), from the ladder FORM only -- b214 two measured"
     " bits are BENCH and are not used. ### ONE QUARTER APPEARS TWICE; IT IS NOT SHOWN TO BE"
     " THE SAME QUARTER. Feeds keystone 1.5a-7 AT THE WAVE; 1.5a-7 is not edited",
     "FINDINGS.md#quarter-density-law; data/b225_serializing_close.txt"),
    ("mersenne-curio", "b225",
     "d_1(2,n)/2 is a perfect number exactly when 2^(n-1) - 1 is a Mersenne prime; n = 3,"
     " 4, 6, 8 give 6, 28, 496, 8128, the first four perfect numbers in order",
     "### CURIO, NOT A FINDING, AND NOT PROMOTABLE. It is Euclid theorem applied to a"
     " closed form the corpus already had: d_1(2,n) = 2^(n-1)(2^(n-1)-1) is the Euclid"
     " shape doubled. ### IT SAYS NOTHING ABOUT THE PROLATE SPECTRUM, THE SONIN SPACE,"
     " OR h2",
     "FINDINGS.md#mersenne-curio"),
    ("m21-decided", "b194 (minted) / b222 (priced) / b225 (decided)",
     "M21 -- a build ingredients unqueried -- closes as DECIDED-BY-RE-SCOPE: direction A is"
     " OPENED as a new plan, term 3 re-scoped to von Neumann incomplete direct product on a"
     " STATED CHOICE of norm-one unit per finite place, archimedean unit from the Sonin"
     " sector under the b212 ruling",
     "### THE AUTHOR RULING, carried by ferry 2026-08-28. A RULING, NOT A DERIVATION, and"
     " the provenance line travels with it. ### b194 retirement of the pure-inclusion plan"
     " STANDS AS HISTORY AND IS NOT REPEALED -- purity is not required by the new plan and"
     " no inclusion maps are used. ### THE NEXT ACT IS THE STATED CHOICE AND b225 DID NOT"
     " RUN IT",
     "THE_IDENTITY_CHAIN.md sec 29; data/b225_serializing_close.txt"),
    ("archimedean-sector-invariant", "the 2026-08-21 deficit act / b225 (disposed)",
     "the wanted poster asks for a regularization-invariant INTEGER sector invariant"
     " d_1(infinity), independent of grid and scale, with roster (0, 11, 126, 2282, 12512,"
     " 37800)",
     "### LEFT STANDING at b225; TRIGGER STILL NONE. ### THE SONIN ARC DOES NOT ANSWER IT:"
     " the arc supplies a RANK DENSITY in an infinite-dimensional space, and the poster"
     " wants an INTEGER DIMENSION. ### A DENSITY IS NOT A DIMENSION, and the poster own"
     " sentence says the integer is the kind of finite-level dimension"
     " real_no_compact_open_addSubgroup FORBIDS R to have",
     "reports/2026-08-21-deficit-comparison.md; FINDINGS.md#w-ord-archimedean-sector-invariant"),
    # ### THE LEVEL-TOWER ROWS (b223, b224).
    ("level-limit-standing", "b57 / b198 (I3) laws / b223 (measured)",
     "d_1(p,n) is positive at every level n >= 2 for p = 2 and every n >= 1 for odd p;"
     " the ONLY zero anywhere is the cell (2,1), the arrival depth. Laws: place-2"
     " 4d = q(q-2); odd 4d = (q-1)^2",
     "DERIVES (b57, longhand general in n). ### b223 RE-DERIVED d_1 EXACTLY in Z[zeta_N] at"
     " 13 cells -- p=2 n=1..8 and p=3 n=1..5 -- reproducing all six banked rows first and"
     " agreeing with the law at 13 of 13; a norm-one unit is exhibited at every reached cell"
     " with d_1 > 0, with S u = q u verified exactly where N <= 1024",
     "data/b223_level_limit_two_places.txt; tools/e16/b223_level_limit.py"),
    ("tower-iota", "b65 (L1)/(L2) / b101 / b198 (I2)",
     "the tower map is iota: Son(p,n) -> Son(p,n+1) by the chart refinement"
     " m'' = p m + p^{2n+1} j, values copied; S+ iota = p iota S so M+ iota = iota M, and"
     " THE FOUR SECTORS ARE IOTA-STABLE ON THE NOSE; S-bar is the L2-closure of the union,"
     " so each E_lam(S-bar) is the closure of its level tower",
     "AVAILABLE-AT-EVERY-FINITE-PLACE (b198 I2), derived with p, q, n FREE; the instance"
     " decided at p = 2 and kernel-checked in Z[zeta_16] (TowerInstance, COMPILED)."
     " ### infinity HAS NO TOWER -- real_no_compact_open_addSubgroup, PROVED",
     "data/b198_nonvanishing.txt; data/b101_registration_2026-08-22.txt"),
    ("segre-open-cells", "the purity report work-order / b224",
     "does ANY nonzero Schmidt-pure vector hide in E1 at the d_1 > 2 cells (5,1), (2,3),"
     " (3,2)? The pencil generalizes to a quadric system on P^{d1-1}",
     "### b224 ran the work-order by a degree-D surjectivity certificate, exact in"
     " Q(zeta_N): the variety is EMPTY iff (S_{D-2})^M -> S_D is surjective."
     " ### G-REPRO reproduced (2,2) MIXED-FORCED by this route before any open cell."
     " ### (5,1): VERDICT (NONE) -- 60 quadrics span S_2 exactly, rank 10 of 10."
     " ### The certificate is ONE-DIRECTIONAL: failure to certify is UNDECIDED, never"
     " a claim that a pure vector exists",
     "data/b224_segre_three_cells.txt; tools/e16/b224_segre.py"),
    # ### THE CLASSICAL-SOURCE AND RANGE-LAW ROWS (b222).
    ("von-neumann-product", "b196 / b197 (source read) / b222 (re-verified at source)",
     "von Neumann 1939 Definition 4.1.1 builds the incomplete direct product from ANY"
     " C0-sequence from an equivalence class; PURITY, ELEMENTARITY AND A CANONICAL CHOICE ARE"
     " NOWHERE REQUIRED, and norm-one is not demanded per factor",
     "EXTERNAL, read at the SOURCE DOCUMENT (Compositio Mathematica t.6 (1939) pp.1-77, the"
     " numdam PDF, extract on disk). ### Re-verified against the definition own words at b222."
     " ### CORRECTNESS IS NOT APPLICABILITY: whether E1(S-bar_v) admits a C0-sequence is"
     " UNDECIDED and the record does not say",
     "data/ext_b196_vonneumann1939_extract.txt; data/b196_term3_requirement.txt;"
     " data/b197_values_and_c0.txt"),
    ("range-law-species", "b197 (named, three instances) / b222 (a fourth)",
     "a finding carried past its own stated range; its mark is that the limiting sentence is"
     " present in the source and was not carried with the quote",
     "NAMED at b197 with three instances (b194, b195, b194-again-at-the-wrong-index)."
     " ### b222 RECORDS A FOURTH: b221 quoted the purity report at source and did not carry"
     " its range law, writing PROVED ABSENT where the record says REFUTED AT THE BANKED CELLS"
     " AND UNDECIDED AT THE LEVEL-LIMIT. ### THE GUARD IS b197 OWN: THE RANGE CLAUSE TRAVELS"
     " WITH THE QUOTE",
     "data/b197_values_and_c0.txt; data/b222_rescope_inputs.txt"),
    ("residue-four-faces", "the 2026-07-28 crank illumination map (C7)",
     "the four faces of the residue -- algebraic, topological, analytic, deformation --"
     " located in Book IV; ONE ROW IN ONE MAP",
     "### RECORDED ABSENT AS AN OBJECT at b222: there is NO keystone document holding them,"
     " and NOTHING in the record reads them against the purity report mechanism."
     " ### FACES_OF_H2_AT_FINITE_INSTANCE.md is a DIFFERENT object (Tier N, question grade)"
     " and names no such face. ### No pattern is asserted",
     "reports/2026-07-28-crank-illumination-map.md line 15"),
    # ### THE TERM-3 / CELL-ASSEMBLY LANE (b221). Grades are the ones their own acts recorded.
    ("restricted-tensor-retired", "b193 (planned) / b194 (RETIRED)",
     "the restricted-tensor construction for term 3 is RETIRED AT ITS OWN FALSIFIER, on"
     " three independent grounds; the maps CANNOT BE FORMED -- that is not a weaker"
     " isometry, it is an ABSENT MAP",
     "RETIRED, NOT PATCHED, at b194, on the owner read of the 2026-08-19 purity report."
     " ### NO ALTERNATIVE CONSTRUCTION IS PROPOSED; a re-scope is the author's."
     " ### b194 filed M21 (a build's ingredients unqueried) as its own lesson",
     "data/b193_restricted_tensor_one.txt; data/b194_restricted_tensor_two.txt"),
    ("e1-unit-purity", "the 2026-08-19 purity act / b194 / b221",
     "at the banked cells: (2,1) NO-UNIT (d1=0); (3,1) and (2,2) MIXED-FORCED -- E1 contains"
     " NO NONZERO PURE VECTOR AT ALL, and at (2,2) none over ANY field extension;"
     " (5,1),(2,3),(3,2) MIXED-generic",
     "DECIDED with exact witness minors in Z[zeta_9] and Q(zeta_16)[t]; the FORCED grade at"
     " (3,1) and (2,2), the generic grade elsewhere. ### Existence at d1 > 2 is OPEN and its"
     " own act says so",
     "reports/2026-08-19-e1-unit-purity.md; data/b194_restricted_tensor_two.txt"),
    ("unit-normalized-trace", "act 7 sec 4 (named) / b220 (misread) / b221 (read at source)",
     "act 7 sec 4 NAMES it as what a future theorem would state and DOES NOT DEFINE IT --"
     " it says neither what it traces, nor over which space, nor normalized how",
     "### A NAME, NOT A DEFINITION, read at SOURCE at b221. ### b220 called it the most"
     " promising named route and WAS WRONG -- the route was retired at b194, twenty-six acts"
     " earlier (see restricted-tensor-retired)",
     "reports/2026-08-18-w-construction-1-act-7.md sec 4;"
     " data/b221_cell_level_assembly.txt"),
    ("weil-ledger-target", "File E / b221",
     "the ledger CELL-LEVEL target -- its value, coefficients, normalization and log p"
     " convention -- is ABSENT from the record; the ledger exists only as a TYPE, two"
     " unconstrained reals per cell",
     "### ABSENCE RECORDED at b221 as term 2 FOURTH debt. File E own header: THIS FILE"
     " STATES; IT DOES NOT PROVE. ### The only log p in the record is b10 QUESTION-grade"
     " Lefschetz wonder, no promotion either way."
     " ### SUPERSEDED IN PART BY b229 (2026-08-28): the PRIME side is now ADOPTED-BY-RULING"
     " as wPrimes(a); the ABSENCE now covers wInf ONLY. ### The b221 grade above is left"
     " standing as its own act recorded it -- a row is a pointer, never a re-grading",
     "SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean;"
     " data/b221_cell_level_assembly.txt; data/b229_statement_adopted.txt"),
    ("sign-of-a", "b232",
     "the archimedean column's sign: wInf = -A, DERIVED from Connes-Consani's own equation (1)"
     " (arXiv 2006.13771, 'Weil positivity and Trace formula: the archimedean place') set beside"
     " the instrument's docstring arrangement committed before any answer. ### The corpus carries"
     " TWO W_inf conventions -- Day-1's (= +A) and CC's (= -A) -- and File E binds to CC's;"
     " SIGN_ARRANGEMENT_RECONCILIATION and act 12 compare DIFFERENT PAIRS and do not conflict",
     "(FORCED) at b232, DERIVES-BY-CITATION with IMP-2 as the import; the finite-place matching"
     " named as a sub-assumption (CC's finite-place formula is not in the retrieved text)."
     " ### THE STANDING-CLAUSE CHECK IS SHOWN: the sign came from a source display, NOT from act"
     " 12's residual collapse, which is quoted as what the act refused to use. ### wInf(a) := -A(a)"
     " ADOPTED; the ledger's statement is COMPLETE AT CELL LEVEL -- every column defined, nothing"
     " proved",
     "data/b232_sign_of_A.txt; THE_IDENTITY_CHAIN.md sec 34;"
     " SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean"),
    ("import-ledger", "b232",
     "the enumerated list of statements the corpus USES but did not derive and does not own."
     " IMP-1: the two-ended classical prime sum (Weil 1952, CC's own [33]), carrying b231's fold"
     " -- the reason b231's verdict was (PARTIAL). IMP-2: CC's explicit-formula arrangement"
     " (2006.13771 eq. 1), carrying b232's sign derivation",
     "OPENED at b232 as THE_IDENTITY_CHAIN.md sec 35. ### HEAD SENTENCE: imports are enumerated"
     " like axioms and NEVER wear the corpus's grade   ### as its own act recorded it",
     "THE_IDENTITY_CHAIN.md sec 35; data/b232_sign_of_A.txt"),
    ("the-two", "b231",
     "the adopted target's factor 2 read as the FOLDED MIRROR TERM -- the k<0 half of a"
     " two-ended sum laid onto the k>0 half. ### VERDICT (PARTIAL): the evenness HOLDS"
     " (bump w depends on t only through t^2, so corr is even -- and np.convolve(w,w) is a"
     " CONVOLUTION that coincides with the autocorrelation ONLY because of it) and the fold"
     " identity is FREE and compiled; but NO OWNER IN ANY OF THE FOUR TREES WRITES THE"
     " TWO-ENDED SUM in any notation, so the provenance is an IMPORT and is listed as one",
     "(PARTIAL) at b231. ### The algebra DERIVES at the zero-axiom bar"
     " (FoldedMirrorShadow, 14 terminals); ### the identification of wPrimes with a folded"
     " two-ended sum is IMPORT-DEPENDENT, below owned-derivation grade. ### The log p quarry"
     " is untouched and b10's 'no promotion either way' stands",
     "data/b231_the_two.txt; SIDE-global-section/Core/FoldedMirrorShadow.lean;"
     " CORRESPONDENCE.md row 89"),
    ("staircase", "b16 / b17",
     "one archimedean bound a sets every place effective cutoff n_p(a) ="
     " #{k >= 1 : p^k <= a^2}; D(a) ranges over all places with n_p(a) >= 1, so THE ACTIVE"
     " PLACE SET IS FINITE at every cell",
     "DEFINITIONAL, on disk, and the diagonal section is compiled (D-yes, f967f10)."
     " ### INDEXED BY A DIAGONAL CELL a^2 -- NOT by a (p,n) local cell, and b221 records"
     " that confusing the two is the double-name species",
     "data/b17_2026-08-18.txt; data/b16_2026-08-18.txt"),
    ("aggregation", "b197 / b215 / b220",
     "no statement assembles the quotient channel per-place values into the single real"
     " Q.value at a diagonal cell; the admissible set is EVERY function from a cell to R",
     "### UNSTATED at b197, re-confirmed b215. ### b220 measured the freedom: C-TYPE demands"
     " NOTHING, C-NORM bearing is NOT STATED, C-FINITE WIDENS it, and C-WEIL is NOT"
     " AVAILABLE (no exact statement, and circular -- it is h2). ### The RESULT route is"
     " blocked in principle; a RULING or an identity-independent constraint is wanted",
     "data/b197_values_and_c0.txt; data/b215_term2_statement_before_file.txt;"
     " data/b220_aggregation_freedom.txt"),
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
    # ### THE PROLATE-ARC LANE'S ROWS (b216). ### EVERY GRADE IS THE ONE ITS OWN ACT
    # ### RECORDED. ### NO ROW HERE PROMOTES ANYTHING.
    ('alpha', 'b205 / b210 / b212 / b214',
     'the connection coefficient: at an eigenvalue psi = alpha * y_I, so alpha = '
     'psi(x0)/y_I(x0); |alpha| = pi*Lambda at every eigenvalue in BOTH parity families',
     'BENCH for the magnitude (b210 even, b212 odd, measured 1.0 to twelve figures). '
     '### THE ABSOLUTE SIGN AT mu_-2 WAS b205 DISCREPANCY AND IS **DECIDED AT b214** by '
     'F phi / phi = +1, ### CONVENTION-FREE. ### b212 note: |alpha_odd| = pi*Lambda was the '
     "FERRY's prediction and the executor registered dissent and WAS WRONG",
     'data/b205_sign_at_our_parameter.txt; data/b210_wronskian_gate.txt; '
     'data/b212_odd_family.txt; data/b214_orientation_bits.txt'),
    ('beta', 'b205 (instrument) / b211 / b212',
     'beta = (x^2-1) W(psi, y_I), CONSTANT in x, its zeros the eigenvalues; at x0 = sqrt2 '
     'the weight is 1 so beta IS the paper F there',
     'IMPORT for the definition -- RRT sec 4.2.2 (C. R. Math. 363 (2025), DOI '
     '10.5802/crmath.780), read at source. ### THE SIMPLICITY OF ITS ZEROS **DERIVES** at '
     'b211 (even) and b212 (odd) on premises (i) and (ii) -- ### AND THAT IS THE PAPER OWN '
     'OPEN CONJECTURE (sec 4.2.2: "We conjecture that the zeros of F are simple")',
     'tools/e16/b205_prolate.py; data/b211_alternation_derived.txt; data/b212_odd_family.txt'),
    ('psi', 'b205 (instrument) / b212',
     'the solution fixed by its behaviour at infinity: EVEN ~ -sin(tau x)/x, '
     'ODD ~ -cos(tau x)/x, leading coefficient mu-INDEPENDENT (V_0 = 1)',
     'IMPORT for the even D_tau form -- RRT sec 4.2.2, quoted. ### THE ODD D_tau FORM IS AN '
     '**EXECUTOR INFERENCE** from a variant the paper DELEGATES ("It is only a change of '
     'notations. We leave it to the reader"), ### NOT A QUOTATION -- b212 graded it as one '
     'and G-REPRO-ODD tested it rather than trusting it',
     'tools/e16/b205_prolate.py; tools/e16/b212_odd.py; data/b212_odd_family.txt'),
    ('wronskian-identity', 'b211 (even) / b212 (odd)',
     'alpha(mu_k) * beta_prime(mu_k) = INTEGRAL_1^inf psi^2 dx, with c_0 = +1 in BOTH '
     'parity families; the right side is an integral of a square and is strictly positive',
     'DERIVED AT CONTENT in seven steps, ON NAMED IMPORTS (I1-I11 at b211; re-earned on the '
     'cosine solution at b212). ### NOT A PROOF FROM NOTHING. ### Measured first at BENCH '
     'grade at b210 (residuals to 1e-16) and DERIVED afterwards',
     'data/b210_wronskian_gate.txt; data/b211_alternation_derived.txt; '
     'data/b212_odd_family.txt'),
    ('alternation', 'b207 (bench) / b211 / b212 (derived)',
     'sign(alpha_k) alternates at consecutive eigenvalues within each parity family',
     'BENCH at b207 (six eigenvalues, tau = 2 pi). ### **DERIVES** at b211 on premise (ii) '
     '(beta entire of order <= 1/2) plus the derived simplicity; re-earned for the odd '
     'family at b212. ### Core shadows: AlternationShadow (row 83), SignTransferShadow '
     '(row 84)',
     'data/b207_alternation.txt; data/b211_alternation_derived.txt; data/b212_odd_family.txt'),
    ('the-ladder', 'b212 (form) / b214 (bits)',
     'by merged rank the Fourier eigenvalue runs c_k = -(-i)^k, i.e. epsilon = -1 with '
     'orientation i^{-k}, under the b19 transform convention',
     'BENCH. ### THE FORM was fixed at b212 UP TO TWO BITS and the shadow proved they are '
     'underdetermined by alternation alone (row 85, alt2_does_not_imply_stepsI). ### THE '
     'BITS were MEASURED at b214 from F phi / phi directly. ### epsilon IS CONVENTION-FREE; '
     'THE ORIENTATION FLIPS under the conjugate convention. ### A grade above bench wants an '
     'ANALYTIC evaluation of F phi at one point',
     'data/b212_odd_family.txt; data/b214_orientation_bits.txt; '
     'Core/LadderOrientationShadow.lean (rows 85, 86)'),
    ('odd-family', 'b212',
     'the cos-asymptotic family; c^2 = -1 from F^2 = parity on odds gives c = +-i, both '
     'values occur, so E_i(S(1,1)) and E_-i(S(1,1)) are NONZERO',
     'DERIVES ON NAMED IMPORTS. ### c = +-i has NO MISSING STEP because RRT Lemma 2 carries '
     'NO PARITY RESTRICTION while Prop 7 says "even" -- ### the paper restricts where it '
     'means to. ### Under the author ruling this is a fact about term 3 archimedean unit',
     'data/b212_odd_family.txt; PLACE-papers phase2/method/THE_IDENTITY_CHAIN.md s23'),
    ('transform-convention', 'b203 (named) / b214 (pinned)',
     "b19 centered DFT F[j,k] = exp(2*pi*i*m_j*m_k/N)/sqrt(N), positive exponent, self-dual "
     'scaling; continuum limit (F f)(y) = INT f(x) e^{+2 pi i x y} dx',
     'ADOPTED, NOT DERIVED. ### THE KEYSTONE "F^2 = parity, F^4 = 1" DOES NOT PICK THE SIGN '
     '-- both exponents satisfy it. ### b203: the two conventions AGREE ON EVENS and '
     'CONJUGATE ON ODDS, so the even bit is convention-free and the odd bit travels with its '
     'convention. ### The record contains both signs (b19 positive; b71 chi_inf conjugate)',
     'data/b19_2026-08-18.txt; data/b203_transform_convention.txt; '
     'data/b214_orientation_bits.txt'),
    ('eigenfunction-scale', 'b202',
     "xi_mu two normalizations in CM differing by -1/pi -- the third of the three distinct "
     'things the corpus had been calling "normalization"',
     'THE OWNER IS b202 AND THE AMBIGUITY IS THE SOURCE OWN, resolved by its own cited '
     'authors. ### DISTINCT from G1 operator/index normalization and from the transform '
     'convention; b203 separated the three and named this one',
     'data/b202_sum_test.txt; data/b203_transform_convention.txt'),
    # ### THE TERM-2 LANE'S ROWS (b216).
    ('quotient-trace', 'act 9 (longhand) / b197 / b215',
     'tau_q * p^(k/2) = (p^n - p^k)/(p^n - 1); the quotient channel CONVERGES TO WEIL '
     'COEFFICIENTS AT THE LEVEL LIMIT; per place, per level',
     'LONGHAND **PROVED** (act 9), every banked integer re-derived; volume normalization '
     'FORCED (act 7); a vanilla Core shadow HELD at Core/QuotientLemmaShadow.lean, zero '
     'axioms. ### THE FORMALIZATION IS ABSENT AND THE DEBT IS "WRITE IT AT ALL" (b189). '
     '### AND **THE AGGREGATION IS UNSTATED**: no statement assembles the per-place values '
     'into the single real Q.value at a cell (b197, re-confirmed b215)',
     'data/b197_values_and_c0.txt; data/b215_term2_statement_before_file.txt'),
    ('file-d', 'b189 / b215',
     'the file File E names as term 2 owner. ### IT DOES NOT EXIST, and it cannot be '
     'written because the statement it would carry cannot be written',
     'ABSENT. ### "THERE IS NO FILE D. THERE ARE ALSO NO FILES A, B OR C" (b189). '
     '### b215 HALTED at the statement gate: the missing sentence is THE AGGREGATION, and it '
     'WANTS A RULING OR A RESULT, NOT A READ. ### b215 also found a SECOND, independent '
     'blocker: the Interfaces layer cannot be compiled in this environment (no built Mathlib; '
     'v4.30.0-rc1 against the repo v4.29.1)',
     'data/b189_roster_and_scope.txt; data/b215_term2_statement_before_file.txt'),
    ('class-richness', 'file E (at cite) / M16 / b215',
     "term 2 named premise, carried AT CITE by File E owner line",
     '### ITS CITATION EXACT STATEMENT IS **UNREAD** -- M16, quoted: "the class-richness '
     'lemma at cite, OWNER UNREAD". ### b215 SPLIT THE ITEM INTO TWO PARTS: (a) read the '
     'citation, (b) discharge the lemma -- ### YOU CANNOT DISCHARGE WHAT YOU HAVE NOT READ. '
     '### It is a HYPOTHESIS carrying its name, never to be discharged by trivial',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean; '
     'data/b215_term2_statement_before_file.txt'),
    ('weil-ledger', 'File E / the act-12 dictionary',
     'W_infinity and the prime sum at the cell -- the atlas certified columns in the CC sign '
     'convention',
     'AS FILE E RECORDS IT: a DATA PARAMETER, stated and not proved. ### File E own header: '
     '"THIS FILE STATES; IT DOES NOT PROVE"',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean'),
    # ### THE FILING LANE ROWS (b216) -- ### NEITHER OF THESE IS A RESULT, AND BOTH ROWS SAY SO.
    ('parked-note', 'b213',
     'the draft note to the source authors: filled from its named banks, placed private at '
     'PLACE-papers phase2/notes/, class line TIER N / DRAFT / NOT CIRCULATED',
     '### A FILING, NOT A RESULT. ### PARKED-BY-RULING and NOT discharged-by-posture -- the '
     'item asked for a posture ruling and the answer is that NO POSTURE IS RULED. '
     '### NOTHING SENT, NO CONTACT ATTEMPTED. ### Trigger: reopen only on the author explicit '
     'ask',
     'data/b213_note_filled_and_parked.txt; '
     'PLACE-papers phase2/notes/DRAFT_note_to_RRT_2026-08-27.md'),
    ('naming-ruling', 'the author, 2026-08-27 (filed b212)',
     "term 3 archimedean factor is the archimedean Sonin space S(1,1); its E_1 is THE SONIN "
     'SECTOR; the CONSTRAINT and COMPRESSION sectors are bench objects that do not enter the '
     'identity; b159 constrained-class statements remain as filed and do not govern S(1,1)',
     '### PROVENANCE: THE CONVERSATION LAYER. ### NOT A DERIVATION. ### NOT CITABLE AS '
     'EVIDENCE ABOUT THE SECTOR. ### STRIKEABLE. ### It settles a NAME, not a fact -- that '
     'the Sonin sector is nonzero is b211 derivation, and the ruling ATTACHES that result to '
     'term 3 without supplying evidence for it',
     'data/b212_odd_family.txt; PLACE-papers phase2/method/THE_IDENTITY_CHAIN.md s13; '
     'PLACE-papers phase2/method/THE_CODOMAIN_SPECIFICATION.md s1'),
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
