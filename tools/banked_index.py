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
    # ### THE FACE-OFF KEY, ADDED b240 UNDER ITS CLAUSE (g).
    'first-face-off': ['face-off', 'the face off', 'first face-off', 'l vs r',
                       'the two columns', 'dissonant', 'the separation at bench'],
    # ### THE DEFINITION KEY, ADDED b239 UNDER ITS CLAUSE (f).
    't-value-definition': ['t.value definition', 't value definition', 'rule m-1',
                           'c2 definition', 'documented binding', 'defined-by-ruling'],
    # ### THE BUDGET KEYS, ADDED b238 UNDER ITS CLAUSE (e).
    'error-budget': ['error budget', 'the error budget', 'imp1 budget', 'budget table',
                     'the five sources', 'edge hypothesis'],
    'right-side-error-spec': ['right side error spec', 'the error spec', 'error bars',
                              'pr error bar', 'instrument error spec'],
    # ### THE ASSET KEYS, ADDED b237 UNDER ITS CLAUSE (f).
    'left-side-assets': ['left side assets', 'the assets', 'asset table',
                         'theta_quotient', 'trace_modes', 'the four channels'],
    't-value': ['t.value', 'tvalue', 't value', 'archimedean e1 trace',
                'the definitional ruling'],
    'engine-remaining': ['the engine remaining', 'missing steps', 'm-1 m-5',
                         'the engine size', 'remaining construction'],
    # ### THE COMPREHENSION KEYS, ADDED b236 UNDER ITS CLAUSE (e).
    'comprehension': ['the comprehension read', 'comprehension', 'h1 and h2',
                      'h2 as deposited', 'the mapping', 'deposit-voice read'],
    'demarcation': ['the demarcation', 'demarcation', 'isnt this just weil positivity',
                    'weil positivity question', 'what the corpus adds'],
    # ### THE VOICES AND ATLAS KEYS, ADDED b235 UNDER ITS CLAUSE (e).
    'voices': ['the voices', 'voices', 'deposit-voice', 'support-voice', 'program-voice',
               'three voices', 'phase 1.1 voices'],
    'sign-atlas': ['sign atlas', 'the sign atlas', 'sign-atlas', 'conventions atlas',
                   'w-infinity conventions', 'translation rule'],
    # ### THE FOLD KEY, ADDED b234 UNDER ITS CLAUSE (d). ### NOTE THE COLLISION IT AVOIDS:
    # ### b231 declared `the fold` as an alias of `the-two`, so that string is NOT reused here.
    'fold-forward': ['fold forward', 'the fold-forward', 'fold-forward', 'the arc fold',
                     'findings fold', 'arc live items', 'species catalogue',
                     'b209-b233', 'the identity arc'],
    # ### THE ARRANGEMENT AND BAR KEYS, ADDED b233 UNDER ITS CLAUSE (d).
    'the-arrangement': ['the arrangement', 'arrangement', 'file e minus',
                        'prime term entry sign', 'wprimes sign', 'the combination',
                        'winf minus wprimes'],
    'import-bar': ['import bar', 'the import bar', 'verification column',
                   'verified-at-bench', 'verified-internally', 'trusted-at-cite'],
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
    # ### THE RESIDUAL-LEDGER KEYS, ADDED b241 ON FILING.
    'residual-ledger': ['the residual ledger', 'five terms', 'the five-term ledger',
                        'ledger terms'],
    'e2-ownership': ['e2 ownership', 'the eps double-count', 'eps double count',
                     'e2 double-count'],
    'resid47-reading': ['resid47', 'resid 47', '0 by construction',
                        'zero by construction', 'the substituted reading'],
    'q-orientation': ['q orientation', 'theta_q sign', 'theta_q orientation',
                      'quotient sign', 'q.value orientation'],
    # ### THE LEFT-MODE-AXIS KEY, ADDED b242 ON FILING.
    'left-mode-axis': ['left mode axis', 'mode axis', 'bar_l', 'prolate mode tail',
                       'eigenvalue floor', 'mode truncation'],
    # ### THE IMP-1-ENVELOPE KEY, ADDED b243 ON FILING.
    'imp1-envelope': ['imp1 envelope', 'imp-1 envelope', 'the analytic envelope',
                      'corr second derivative', 'interpolation bound'],
    # ### AND THE ALIASES b241 DELIBERATELY **DOES NOT** ADD, EXTENDING b181's PRECEDENT:
    # ### the bare 'orientation' (ambiguous against sign-atlas, alpha and alternation);
    # ### the bare 'aggregation' (it belongs to quotient-trace, whose row STATES the absence,
    # ### and re-pointing it here would hide the older owner behind the newer route);
    # ### the bare 'e2' (ambiguous against e1-even-bridge and unit-normalized-trace).
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
    ("first-face-off", "b240",
     "the identity's two columns computed at the six banked diagonal a^2 cells under one named"
     " convention, meanings banked and HASHED before the first instrument call:"
     " L := T.value + Q.value := (Tr_full + E2 + Delta-minus) + Theta_q against R := A - PR."
     " ### BRANCH (DISSONANT) AT ALL SIX CELLS, separation 5.85 to 8.09 against combined bars 0.203 to"
     " 0.745 (10.85x to 28.8x). ### AND THE SEPARATION HAS AN EXACT ANATOMY, registered BEFORE the run and"
     " reproduced to 8.9e-16: L - R = 2*E2 + Delta-minus + resid47 + Theta_q + PR, whose LARGEST"
     " term everywhere is resid47 := Tr_full - A - E2 (2.31 to 4.05)",
     "BENCH, PER-CELL, AT A FINITE PLACE SET AND A FINITE CUTOFF -- ### b15: 'a finite-place-set"
     " object at a finite cutoff decides nothing global'. ### THE FORM IS NOT INDICTED: suspects 1"
     " (axes) and 2 (normalizations) account for the whole separation term by term, and the largest term"
     " rides a mode truncation whose tail NOTHING IN THE RECORD BOUNDS (W-ORD-LEFT-MODE-AXIS)."
     " ### THE LEFT SIDE IS THE UNCONVERGED SIDE: its bar is SIX ORDERS above the right's."
     " ### NO GRADE MOVED; no variant was promoted to primary; h2 UNCHANGED",
     "data/b240_meanings.txt; data/b240_faceoff_run.txt; data/b240_diagnostics.txt;"
     " data/b240_first_face_off.txt"),
    ("t-value-definition", "b239",
     "T.value DEFINED BY AUTHOR RULING (RULE M-1): C2, i.e."
     " ArchimedeanE1Trace.value := Tr_full + E2 + Delta-minus -- the three archimedean channels of"
     " the bench instrument at a DIAGONAL a^2 cell. ### Written as a DOCUMENTED BINDING, not a Lean"
     " definition: the three summands have NO formal definitions in this repository, so writing"
     " them as terms would mean inventing three realizations the record does not have. ### THE"
     " FIELD STAYS A DATA PARAMETER; WHAT IS FIXED IS ITS MEANING",
     "DEFINED-BY-RULING (C2), REALIZED PER-CELL AT BENCH, OPEN DEBT M-4 (Delta-minus trace-class"
     " bookkeeping) -- the grade cell of CORRESPONDENCE row 90. ### THE RIDER IS PART OF THE RULING"
     " AND NOT A GLOSS: realization is per-cell at bench, standing until M-4 closes, and is NOT"
     " structural. ### sec 17's own grade for Delta-minus is 'open only in its trace-class"
     " bookkeeping', so value IS DEFINED ONLY AS FAR AS THAT BOOKKEEPING IS. ### The amendment is"
     " docstring-only, verified by stripping every comment and comparing to the HEAD blob:"
     " IDENTICAL   ### as its own act recorded it",
     "SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean; CORRESPONDENCE.md row 90;"
     " data/b239_ruling_executed.txt"),
    ("error-budget", "b238",
     "every error source in the IMP-1 bench priced BY MEASUREMENT. ### FOUR OF FIVE CAME OUT AT"
     " ZERO: A, P and Z carry no grid error (machine epsilon); the zero truncation is invariant"
     " over a factor of 4 in N; the zeros at doubled precision agree to 0.000e+00; and b234's"
     " registered HALF-ORDER EDGE HYPOTHESIS IS REFUTED by direct measurement -- the trapezoid on"
     " the bump's own species matches mpmath.quad to 0.000e+00 at every grid from 2001 to 32001"
     " (Euler-Maclaurin: the flat endpoints cost nothing). ### WHAT REMAINS IS np.interp IN THE"
     " PRIME COLUMN plus a 1.2e-13 float floor, explaining ~97% of every observed residual",
     "measured, not assumed. ### AND A FINDING ABOUT MEASUREMENT ITSELF: the interpolation order"
     " is ERRATIC (1.10/1.22/1.58, 1.27/1.76/3.92) because the evaluation points log p^k are FIXED"
     " while the grid refines -- AN ORDER IS NOT WELL DEFINED FOR A FIXED POINT ON A REFINING"
     " GRID. b233 saw the same ratios; b238 can say why there is no clean exponent to find"
     "   ### as its own act recorded it",
     "data/b238_imp1_budget.txt; data/b238_budget_run.txt"),
    ("right-side-error-spec", "b238",
     "the instrument-layer error spec for PR and A. ### NOT FILED. The ferry files it on"
     " (PROMOTED) only and the branch came out (HELD) -- a spec filed off a failed criterion would"
     " be the same over-reach the criterion exists to prevent. ### WHAT IS RECORDED AS A MEASURED"
     " FACT AND NOT AS A SPEC: A, P and Z are at machine epsilon; PR's error is approx K*h^2 with"
     " K of order 0.15-0.7 at the cells tested",
     "NOT FILED at b238 -- branch (HELD). ### The right side's error bars are MEASURED but NOT YET"
     " CERTIFIED: the numbers are known, the grade is not granted. ### W-ORD-IMP1-ENVELOPE is the"
     " named remainder   ### as its own act recorded it",
     "data/b238_imp1_budget.txt; THE_IDENTITY_CHAIN.md sec 35.1"),
    ("left-side-assets", "b237",
     "everything the corpus holds toward realizing File E's LEFT column (T.value + Q.value) at a"
     " cell. ### FOUR CHANNELS at tools/e16/b38_act10.py: trace_modes (Tr, archimedean, prolate"
     " space), e2_of_grid (E2, the eps bookkeeping), Delta-minus (sec 17's odd-index t(n) series),"
     " and theta_quotient (Theta_q, FINITE, on V_inv). ### AND A NAMING INVERSION: the acts"
     " narrative's LEFT = A - PR is the LEDGER, i.e. File E's RIGHT",
     "REALIZES: 0 / PARTIALLY REALIZES: 4 / DIFFERENT OBJECT: 0 among the channels; sec 25(c)'s"
     " L1+L2+L3 are DIFFERENT OBJECT (inequality links, not realizations -- assembling a BOUND ON"
     " the object, not a VALUE OF it). ### NOTHING REALIZES T.value OR Q.value OUTRIGHT."
     " ### No asset was graded by agreement with the right side   ### as its own act recorded it",
     "data/b237_left_side_assets.txt; tools/e16/b38_act10.py"),
    ("engine-remaining", "b237",
     "the engine's remaining construction as a NAMED SPECIES-TAGGED LIST rather than a frontier:"
     " M-1 [RULING] what T.value IS; M-2 [RESULT or RULING] a statement carrying the quotient"
     " operator onto S-bar_v or u_v into V_inv; M-3 [RESULT] the cited class-richness lemma"
     " (Schwartz-Bruhat, formalization owed to files B-C); M-4 [RESULT] the eps trace-class"
     " bookkeeping; M-5 [CONSTRUCTION] the effective-mode (Shannon) dictionary -- sec 25(c)'s"
     " named MISSING TRANSPORT",
     "FIVE items: one ruling, three results, one construction. ### AND THE NARROWING, WITH BOTH"
     " HALVES: CONFIRMED that Theta_q computes a definite normalized quotient trace at cells on"
     " V_inv, so there is no missing PER-PLACE operator; REFUTED that this bypasses the junction --"
     " sec 18 joint 1 says 'the restricted-product trace is DEFINED BY EXACTLY' the E1-unit's"
     " normalization. ### THE JUNCTION IS AT THE ASSEMBLY, NOT THE PER-PLACE COMPUTATION"
     "   ### as its own act recorded it",
     "data/b237_left_side_assets.txt; narrative sec 18 / sec 25(c)"),
    ("t-value", "b237",
     "the definitional ruling on what File E's T.value IS. ### FOUR CANDIDATES, EACH WITH ITS COST:"
     " (C1) Tr_full alone -- but File E's owner line says eps-REGULARIZED; (C2) Tr_full + E2 +"
     " Delta-minus -- matches the words, inherits Delta-minus's open trace-class bookkeeping;"
     " (C3) Tr(theta(g) S theta(g)*) at CC's S -- ties T to an IMPORT whose model transport FAILS;"
     " (C4) left as a DATA PARAMETER realized per-cell at a pin",
     "RULING ITEM, the author's. ### A DEFINITIONAL RULING, NOT A COMPUTATION -- it cannot settle"
     " itself. ### THE EXECUTOR NAMES THE CANDIDATES AND CHOOSES NONE."
     " ### SUPERSEDED BY RULING 2026-08-28 (b239): the author ruled C2, with a per-cell"
     " instrument-realization rider standing until M-4 closes and M-4 named as the"
     " definition's open debt -- see t-value-definition. ### The dossier's own grade above"
     " is left standing as its act recorded it: a row is a pointer, never a re-grading"
     "   ### as its own act recorded it",
     "data/b237_left_side_assets.txt sec 4a;"
     " SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean"),
    ("comprehension", "b236",
     "h1 and h2 read at DEPOSIT-VOICE from the verified canonical copy (Zenodo v1.1.2, ms v5.10.2,"
     " 11 files md5-matched against Zenodo's published checksums) and mapped to the now-complete"
     " statement. ### THE DEPOSIT'S OWN WORDS: h1 'complete at the witness'; h2 'the theorem"
     " itself: positivity of the Weil functional, lambda_n >= 0 ... RH-equivalent'; sharpest as"
     " 'lambda_Z(n) >= -lambda_A(n)'; the register sentence as 'The one open premise ... five"
     " registers'. ### THE MAPPING: the FOURTH register -- the balance-to-positivity distance at"
     " the multiplicative place -- IS, at a diagonal a^2 cell under one named convention, THE SIGN"
     " OF A - PR",
     "comprehension at support-voice; ### IT DISCHARGES NOTHING -- the deposit's own ceiling"
     " governs ('None of this discharges h2'; 'criterion + verified surround, not end-to-end')."
     " ### AND THE LIMIT IS NAMED: the deposit lists FIVE registers and this maps ONE."
     " ### THE DEPOSIT IS SILENT ON W_inf (zero occurrences, with a positive control) -- a silence,"
     " not a defect; ERRATA untouched   ### as its own act recorded it",
     "data/b236_comprehension_read.txt; THE_IDENTITY_CHAIN.md sec 37;"
     " FACES_OF_H2_AT_FINITE_INSTANCE.md sec 4; outputs/DEPOSITED-v1.1.2/"),
    ("demarcation", "b236",
     "the answer to 'isn't this just Weil positivity', put on the record before anyone asks."
     " ### WHAT IS IMPORTED: CC's eq (2), RH <=> SUM_v W_v(g*g-bar-sharp) <= 0, which CC credit to"
     " A. Weil [33] following Yoshida [34] -- an equivalence, classical, NOT OURS."
     " ### WHAT THE CORPUS ADDS, each with its limit in the same breath: a machine-verified"
     " reduction (limit: criterion + verified surround, NOT end-to-end); a located clause (limit:"
     " locating is not discharging); an unconditional surround (limit: h1 complete AT A WITNESS,"
     " not at totality); lawful instruments (limit: the bar's first use produced a NON-promotion)",
     "program-voice, b236. ### THE CEILING, STATED SO THE SECTION CANNOT BE MISREAD: the corpus has"
     " NOT proved Weil positivity, has NOT weakened it, and has NOT replaced it; the premise"
     " remains RH-equivalent and open in the deposit's own words   ### as its own act recorded it",
     "THE_IDENTITY_CHAIN.md sec 37.2; data/b236_comprehension_read.txt"),
    ("voices", "b235",
     "the three-voice law: DEPOSIT-VOICE (co-deposited texts at their published Zenodo versions,"
     " frozen, errata-only), SUPPORT-VOICE (the Phase-1.1 support layer at working HEAD),"
     " PROGRAM-VOICE (the wider corpus). Every Phase-1.1 sentence names its voice; 'Day 1'"
     " unqualified is RETIRED from active vocabulary. ### The register pins deposit-voice at"
     " Zenodo v1.1.2 / ms v5.10.2 (2026-07-24, 11 files) against support HEAD v5.13 + two era"
     " annotations -- a drift of three manuscript versions",
     "author ruling, standing from b235. ### AND A FINDING THE REGISTER TURNED UP:"
     " outputs/DEPOSITED/A_Place_to_Stand.DEPOSITED.md IS NOT THE DEPOSIT -- its header reads"
     " v5.4, six manuscript versions stale. ### FILED AS A FINDING AND **NOT** TO ERRATA, because"
     " ERRATA is for defects in DEPOSITED TEXT and the deposited text is clean (read-only fetch"
     " matched REGISTRY item for item)   ### as its own act recorded it",
     "data/b235_phase11_conventions.txt; REGISTRY.md d1-1"),
    ("sign-atlas", "b235",
     "SIGN_ARRANGEMENT_RECONCILIATION.md sec 5: ten cells, each a QUOTATION carrying its voice and"
     " version, covering every W_inf / prime-term / arrangement convention in the record."
     " ### THE TRANSLATION RULE, ONE RULE: CC's eq (1) puts the zero-sum on the LEFT with the"
     " places-sum alone on the right, so every local term flips sign -- W_inf^CC = -W_inf^corpus."
     " ### EIGHT corpus-voice cells carry a determinate orientation and ALL EIGHT AGREE:"
     " W_inf = +A, the prime term enters with a MINUS, the combination is A - PR",
     "the atlas DECIDED the File E conditional at b235 and it EXECUTED. ### The deciding sentence"
     " is the corpus's own statement of its open premise, support-voice: 'h2 - the sign of"
     " W_inf - W_2'. ### NO NUMBER WAS CONSULTED: the instrument row is recorded and explicitly"
     " EXCLUDED from the decision, because a sign warranted by a calibration is an instrument"
     " fact, not a text   ### as its own act recorded it",
     "SIGN_ARRANGEMENT_RECONCILIATION.md sec 5; THE_IDENTITY_CHAIN.md sec 34.6;"
     " data/b235_phase11_conventions.txt"),
    ("fold-forward", "b234",
     "the arc b209-b233 folded into FINDINGS.md as sec 0-bis: five anchored entries"
     " (arc-live-items, residue-six-station-migration, arc-species-catalogue,"
     " two-three-connective, import-ledger-surfaced). ### 25 acts, contiguous, reconciled at"
     " content. ### EVERY OBSTACLE IS A QUOTATION FROM ITS OWNING ACT. ### The statements tally"
     " VERIFIED AT CONTENT AT FIVE (b223, b226, b227, b228+b229 as one, b232), plus the"
     " arrangement at one line (b233) and the aggregation open-with-coordinates (b220)",
     "synthesis-suggested (the roll-up); each item carries its OWNING act's grade. ### NO GRADE"
     " MOVED AND NO TAG WAS EDITED -- tested mechanically: the fold DELETED NO LINE, and under"
     " the document's own rule a grade moves only by an in-place tag edit. ### THE ARC PROVED"
     " NOTHING: all five are STATEMENTS, and the identity is exactly as unproved at b233 as at"
     " b209   ### as its own act recorded it",
     "FINDINGS.md sec 0-bis; data/b234_fold_forward.txt; THE_IDENTITY_CHAIN.md secs 27-36"),
    ("the-arrangement", "b233",
     "the prime term's ENTRY SIGN in File E: with both columns defined, File E's right side is"
     " -A - PR while CC's places-sum is -A + PR. ### File E names its fields and writes its"
     " operator but NOWHERE STATES THE OPERATOR'S INTENT. ### The diagnosis, stated and not"
     " adopted: the minus is exactly right under DAY-1's convention (A - PR, the corpus's own"
     " LEFT column) and names no object the corpus computes under CC's -- so FILE E MAY CARRY ONE"
     " CONVENTION IN ITS DOCSTRING AND THE OTHER IN ITS OPERATOR",
     "(iii) UNDERDETERMINED at b233 -- ROUTED TO THE AUTHOR, NO ARRANGEMENT CHOSEN, three outcomes"
     " spelled out and none recommended. ### The identity's statement is ONE-RULING-FROM-COMPLETE."
     " ### No number was consulted: the narrative's 'fails numerically in BOTH conventions' is a"
     " comparison coming out and was named inadmissible   ### as its own act recorded it",
     "data/b233_the_arrangement.txt; THE_IDENTITY_CHAIN.md sec 36;"
     " SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean"),
    ("import-bar", "b233",
     "the author's ruling that imports are VERIFIED where tools reach, not only trusted: the"
     " import ledger carries a verification column (VERIFIED-INTERNALLY / VERIFIED-AT-BENCH /"
     " TRUSTED-AT-CITE) and every TRUSTED-AT-CITE entry carries a work-order if internal"
     " verification is tool-reachable",
     "STANDING from b233. ### ITS FIRST USE PRODUCED A NON-PROMOTION: IMP-1 was put to the bench"
     " and the act's OWN REGISTERED PASS-CRITERION FAILED 15 of 15 cell-axis pairs, so IMP-1 is"
     " held at TRUSTED-AT-CITE with W-ORD-IMP1-BUDGET. ### The sides agree to ~2e-8 relative but"
     " the criterion was the wrong criterion -- and a criterion rewritten after the numbers is not"
     " a criterion. IMP-2 also TRUSTED-AT-CITE (its load is a LABELLING, not bench-reachable) with"
     " W-ORD-IMP2-TAU   ### as its own act recorded it",
     "THE_IDENTITY_CHAIN.md sec 35.1; data/b233_the_arrangement.txt;"
     " data/b233_imp1_bench_run.txt; data/b233_resid_diag_run.txt"),
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
    # ### THE RESIDUAL-LEDGER ROWS (b241). ### EVERY GRADE IS THE ONE b241 RECORDED, AND TWO
    # ### OF THE FOUR ARE ROUTES RATHER THAN RESULTS -- THE ROWS SAY SO IN THEIR OWN GRADE CELL.
    ('residual-ledger', 'b241',
     "b240's five separation terms assigned owners by text: 2*E2 STANDING, Delta_- ROUTED, "
     'resid47 RECONCILED-BY-TEXT (M-4 unpaid size), Theta_q ROUTED, PR STANDING '
     "(b235's atlas). ### ONE RECONCILED, TWO ROUTED, TWO STANDING; NO CORRECTION EXECUTED",
     '### A READ, NOT A RESULT, AND NOT A FACE-OFF: no side was assembled and no column '
     'compared. ### THE LEDGER IS AN ASSIGNMENT OF OWNERS, NOT A MEASUREMENT -- every number '
     "in it is b240's, cited as the QUESTION and never as evidence for a reading. "
     '### IT MOVES NO GRADE AND DISCHARGES NO M-ITEM',
     'data/b241_residual_ledger.txt; reports/2026-08-29-the-residual-ledger.md'),
    ('e2-ownership', 'b241',
     "C2's E2 and the E2 in b38_act10.py's residual line are ONE OBJECT UNDER TWO NAMES "
     "(int g eps / E2 / E2N / E2full) at two mode truncations, 8.99e-15 apart; File E binds "
     'the FUNCTION b38_act10.e2_of_grid and names no grid argument',
     '### ONE OBJECT -- ### BUT **NO CORRECTION WAS FORCED AND NONE EXECUTED**, and the row '
     'exists to stop that being read as a repair. ### THERE IS NO DOUBLE-COUNT ACROSS THE '
     "EQUALS SIGN: C2 carries E2 once, A - PR carries it none. ### b240's 'Tr_full already "
     "carries an E2' does not follow from the arithmetic it cites -- resid47 is DEFINED as "
     'the residue, so the decomposition is vacuous. ### THE REAL DEFECT IS M-4 (the '
     'unperformed divergent-part subtraction) AND IT WAS ALREADY OPEN',
     'data/b241_residual_ledger.txt Component 2; SIDE-global-section/Interfaces/'
     'FiniteInstanceIdentity.lean lines 57-62'),
    ('resid47-reading', 'b241',
     "b37's 'resid47: 0 by construction' is a property of the SUBSTITUTED reading ONLY -- "
     'b37_act9.py contains no trace function and calls none, so there is no raw trace to '
     "differ from CC Thm 4.7's value. ### FOR C2 THE RAW READING GOVERNS AND resid47 IS NOT "
     'ZERO',
     '### NAMED FROM THE TEXTS, NOT ROUTED. ### The warrant is File E line 60, which binds '
     'Tr_full to b38_act10.trace_modes by name, plus sec 20(b): the bench object "is NOT the '
     'REGULARIZED trace". ### THE TWO READINGS ARE MUTUALLY EXCLUSIVE, not merely different. '
     "### CONFIRMS b240's own sentence on this point. ### resid47 is M-4's unpaid size at "
     'bench and is NOT a new engine item',
     'data/b241_residual_ledger.txt Component 3; tools/e16/b37_act9.py:175'),
    ('q-orientation', 'b241',
     "Q.value's entry orientation relative to the prime side is UNDERDETERMINED by the "
     'owner texts; dossier O1 (Q := -Theta_q) / O2 (Q := +Theta_q) / O3 (data parameter) '
     'filed and ROUTED for a decision card. ### Delta_-\'s sign in T rides the same card',
     '### A ROUTE, NOT A RESULT, AND NOTHING WAS CHOSEN. ### sec 19, b36_act8.py:175, '
     'sec 20(c) and the recurring (Theta_q - PR) pairing all ORIENT Theta_q with the prime '
     "side's minus -- ### BUT NONE ASSEMBLES IT INTO Q.value, and quotient-trace records "
     'that the aggregation is UNSTATED (b197, re-confirmed b215). ### FIVE SENTENCES THAT '
     'ORIENT AN OBJECT ARE NOT ONE SENTENCE THAT DEFINES IT. ### DISCLOSED: O1 shrinks the '
     'residual and that is NOT its warrant; no candidate on the list closes the separation',
     'data/b241_residual_ledger.txt Component 4; reports/2026-08-29-the-residual-ledger.md'),
    # ### THE LEFT-MODE-AXIS ROW (b242). ### A BRANCH THAT DID NOT CERTIFY, AND THE ROW SAYS SO
    # ### IN ITS OWN RESULT CELL RATHER THAN LEAVING IT TO THE GRADE.
    ('left-mode-axis', 'b242',
     "the left side's mode axis measured with NQ and NMODE moved SEPARATELY for the first "
     "time. ### BRANCH (SLOW): convergence measured on the certified range (every ratio < 1), "
     'an envelope BEYOND REACH. ### bar_L HELD, NOT CERTIFIED. ### W-ORD-LEFT-MODE-AXIS '
     'DISCHARGED. ### THREE MEASURED FACTS: (i) b240 bar_L is ~94% QUADRATURE and ~6% '
     'truncation -- the bar named for the mode axis was measuring the other one; (ii) float64 '
     'carries SEVEN modes where Lemma F.1 certifies ELEVEN, and n_last = 6 at every NQ from '
     '500 to 1300, so more quadrature buys no modes; (iii) the NQ-spread jumps 61x-249x '
     'exactly when the first sub-floor mode enters the sum',
     '### A MEASUREMENT, NOT A CERTIFICATE, AND NOT A BOUND. ### THE ENVELOPE WAS DERIVED, '
     'PRINTED AND THEN **REFUSED** for three stated reasons: the ratio is RISING over the last '
     'four certified modes; the extrapolation is unverifiable IN PRINCIPLE at this instrument; '
     'and NO OWNER PROVES THE TRACE SERIES CONVERGES AT ALL. ### M-4 IS **NOT** PAID AT BENCH '
     'and NOT re-priced as structural. ### DISCLOSED AND ROUTED TO b244, NOT DRAWN HERE: the '
     'refused extrapolation runs 2.4x-2.9x bar_L at all six cells, i.e. it points at bar_L '
     'being TOO SMALL, and the consequence for any face-off branch is out of this act scope. '
     '### BOTH SEATS REGISTERED EXPECTATIONS WERE WRONG',
     'data/b242_left_mode_axis.txt; data/b242_envelope.txt; '
     'reports/2026-08-29-the-left-mode-axis.md'),
    # ### THE IMP-1-ENVELOPE ROW (b243).
    ('imp1-envelope', 'b243',
     "b238's under-sampled K replaced by an ANALYTIC envelope derived from the bump: "
     'corr(y) = PHI(y/L)/(L*C^2) with PHI := phi*phi UNIVERSAL and cell-independent, so '
     "corr''(y) = PHI''(y/L)/(L^3*C^2) and |dPR| <= (h^2/8)*SUM_j c_j*max|corr''|. "
     '### ||PHI\'\'||_inf = 0.409587060753 (stable to 12 digits over a 20x density range); '
     'C = 0.4439938161680794 (matching b238 mpmath value to 0.000e+00). ### BRANCH (PROMOTED): '
     'all six (cell, axis) pairs within, INCLUDING a^2=3 at NV=6001, the cell that failed b238',
     '### IMP-1 -> **VERIFIED-AT-BENCH with error bars** -- ### A BENCH GRADE, NOT A PROOF OF '
     "CC equation (1), and it moves nothing about h2. ### THE LEDGER CELL UPDATE WAS DEFERRED "
     'TO b244 and is NOT written by b243. ### THE BOUND IS A RIGOROUS WORST CASE AND IS LOOSE: '
     'slack 2.3x at the tightest cell and 1.5e6 at the loosest, and the slack is PRINTED so a '
     'wide margin cannot read as a tight agreement. ### K CANNOT HAVE BEEN WIDENED TOWARD A '
     'RESIDUAL because no residual enters its formula -- a stronger guarantee than b238 refusal '
     'to widen. ### b238 FAILURE WAS REPRODUCED, NOT RE-DESCRIBED (K needed 0.6616 > 0.6363 '
     'banked). ### RIGHT-SIDE ERROR SPEC FILED on (PROMOTED) only',
     'data/b243_imp1_envelope.txt; data/b243_envelope.txt; '
     'reports/2026-08-29-the-imp1-envelope.md'),
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
