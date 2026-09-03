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
    'archimedean-leg': ['the archimedean leg', 'the archimedean unit',
                       'u_inf', 'the chosen archimedean unit',
                       'the archimedean local space', 'the sonin sector'],
    'boundary-terminal': ['the boundary terminal', 'boundary terminal',
                          'the compiled boundary', 'both sides of the boundary'],
    'm2-arc-fold': ['the fold', 'the arc fold', 'b283-b296', 'the m-2 arc',
                    'the second arc'],
    'kernel-plan': ['the kernel plan', 'kernel build', 'what to compile',
                    'the build candidates'],
    'threshold-asymmetry': ['the asymmetry', 'asymmetry', 'the two thresholds',
                            'reading scale', "the operator's reading scale"],
    'criterion-sharpness': ['sharpness', 'the sharpness', 'necessity of the criterion',
                            'vanishing criterion'],
    'second-zero-mechanism': ['second mechanism', 'second zero mechanism',
                              'the first-level pairing', 'the barrier', 'the pairing',
                              'two-radius vanishing criterion'],
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
    # ### THE RULING KEYS, ADDED b244 ON FILING. ### `q-orientation` IS **NOT** REDECLARED:
    # ### it already exists and b244 adds a SECOND ROW under it, so a query returns THE ROUTE
    # ### AND THEN THE RULING, in order. ### Overwriting b241's row would erase the fact that
    # ### the texts underdetermined it, and the index's own law is that a row carries the grade
    # ### ITS OWN ACT recorded.
    'rule-delta-minus': ['rule delta minus', 'd1', 'delta_- sign', 'delta minus sign'],
    'rule-modes': ['rule modes', 'k1', 'mode ceiling', 'seven computable modes'],
    'second-face-off': ['b245', 'the second face-off', 'face-off preconditions'],
    # ### THE TWO-TAILS KEYS, ADDED b246 ON FILING.
    'two-tails': ['the two tails', 'tail parity', 'even and odd tails', 'one object two names'],
    'd-dict': ['d_dict', 'd dictated', 'the dictated deviation', 'sector split diff'],
    # ### THE M-4 STATEMENT KEYS, ADDED b247 ON FILING.
    'm4-statement': ['m-4 statement', 'the m4 theorem', 'trace-class bookkeeping statement',
                     'm4 route'],
    'xi-alpha-question': ['xi alpha', 'xi_n(1) vs alpha', 'the endpoint question',
                          'alpha double name'],
    # ### THE SECOND-OBJECT KEYS (b248) AND THE PRECISION KEYS (b249), ADDED ON FILING.
    # ### b248 OWNS THIS WRITE; b249's FILINGS DEFER TO IT, PER THE PARALLEL HEADER.
    'second-object': ['the second object', 'the two pieces', 'archimedean piece'],
    'e2-arrangement': ['e2 arrangement', 'additive or subtractive', 'eps-regularized meaning'],
    'junction-piece': ['junction piece', 'pr minus theta_q', 'the finite-place pairing'],
    'mode-precision': ['the precision veil', 'extended precision spectrum', 'k3',
                       'veil lifted'],
    't-series': ['the t series', 't(n)', 'sum t(n)', 'partial sums of t'],
    'm4-derivation': ['the m4 derivation', 'm-4 derivation', 'the trace series theorem',
                      'convergence of sum t(n)', 'the endpoint identity', 'mercer identity'],
    's2-decay-route': ['the s2 decay route', 'eigenvalue decay at fixed c', 'factorial decay',
                       'degenerate kernel truncation', 'the zero-import bound'],
    'third-face-off': ['the third face-off', 'third faceoff', 'the columns with m4 paid',
                       'the shortfall decomposed', 'the accounting of L - R'],
    'two-realizations': ['the two-realizations term', 'delta_2real', 'm-2-inf', 'm2inf',
                         'the archimedean identity question', 'quadrature versus mode sum'],
    'mode-sum-limit': ['the mode sum limit', 'does the mode sum converge', 'tr[n] decay',
                       'the corr-weighted mode sum', 'w(n) ~ C/n', 'the archimedean trace series'],
    'm2inf-ruling': ['the m2inf ruling', 'rule m-2-inf', 'q1', 'the r-label match',
                     'which construction denotes', 'the quoted-n law'],
    'quadrature-binding': ['the quadrature binding', 'T.value := A + E2 - Delta_-',
                           'the re-bound realization', 'the mode sum demoted'],
    'fourth-face-off': ['the fourth face-off', 'the identity at cells', 'the bench shadow',
                        'the imbalance profile', 'L - R under the re-binding'],
    'the-balance': ['the balance', 'Delta_- - E2 vs PR - Theta_q', 'E2even vs Theta_q - PR',
                    'the balance residual', 'the two Delta_- realizations'],
    'limit-profile': ['the limit profile', 'the cutoff ladder', 'the balance along a^2',
                      'the junction sawtooth', 'the staircase sawtooth', 'sixteen cells'],
    'contribution-map': ['the contribution map', 'the whole position at grade',
                         'the patent session input', 'the fold-forward ledger',
                         'h2-dependency column', 'the figure candidates'],
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
    # ### THE ARCHIMEDEAN LEG (b300).
    ("archimedean-leg", "b300 (construction from a graded import, and a derivation)",
     "the object's archimedean local space is BUILT from the source's own Definition 4.4 as"
     " S(1,1) = {xi in L^2(R)_ev : xi = 0 on |q|<=1, F_eR xi = 0 on |p|<=1}, with the inner"
     " product and its normalization read at content at CC 2006.13771 eq (16) --"
     " <eta|xi> := (1/2) INT_R eta conj(xi) dx = INT_0^inf eta conj(xi) dx -- and it is a"
     " Hilbert space because CC's R is the ORTHOGONAL PROJECTION onto it, which is the only"
     " thing von Neumann 4.1.1 asks of a local space. ### **AND THE CORPUS'S CHOSEN"
     " ARCHIMEDEAN UNIT u_inf -- phi_mu at the first even NEGATIVE eigenvalue, normalized in"
     " L^2 (b226, from b214's rank-2 measurement) -- IS IN THAT SPACE**, tested against BOTH"
     " conditions: condition one is CM Lemma 3.1's 'zero on [-1,1]' quoted, and condition two"
     " follows from b211's derived eigenrelation F phi_mu = c phi_mu with c = +-1, so"
     " (F_eR phi_mu)(p) = c*0 = 0 there. ### **THE SIGN OF c IS NEVER USED, SO NO BENCH NUMBER"
     " IS LOAD-BEARING.** ### Separately: the 'Sonin sector' (b206's +1 eigenspace of F on the"
     " space) is a PROPER subspace of S(1,1), so sector and space are DIFFERENT objects; and"
     " u_inf is NOT the instrument vector b291/b292 placed OUTSIDE the space -- two"
     " derivations, one from scalar-invariance and one from CC's own orthogonality sentence",
     "### DERIVES-on-IMPORTS, AND THE GRADE NAMES ITS INPUTS -- CM Lemma 3.1; b211's (C3)"
     " chain on I8+I6+I10 at b211's own banked grade. ### **THE CONSTRUCTION IS CONDITIONAL**:"
     " the real fiber's placement in the corpus's adelic object (N-OPEN-B as b287 read it) is"
     " STILL OPEN, and phi_mu in L^2(R) is stated by NO OWNER (W-ORD-PHI-MU-L2) -- b226's own"
     " choice presupposes it. ### **NOT A ROUTE. ### IT UNBLOCKS NOTHING: b221 records the"
     " halt is at the FINITE places, and b226's G-SECTOR at the generic odd place is STILL"
     " OWED.** ### Whether u_inf is in the SECTOR is NOT derived (that needs c = +1 at rank 2,"
     " which stands at BENCH), and which space the factor is remains the b212 ruling's,"
     " provenance the conversation layer. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b300_the_archimedean_leg.txt; data/b300_source_read.txt; data/b300_e0_gate.txt;"
     " CORRESPONDENCE.md row 115"),
    # ### THE KERNEL'S BOUNDARY PAIR (b298).
    ("boundary-terminal", "b270/b280 (function side, printing since b289) / b298 (relaxed side)",
     "the kernel carries BOTH SIDES OF THE BOUNDARY at the cell (2,2). Function side:"
     " B270.absorb_2_2 -- every index lands in the ball at k = n, so a vector vanishing on the ball"
     " kills the pairing. Relaxed side: B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0 --"
     " on Son(2,2; -1,0) the witness w = e_2 - e_6 + e_4 - e_12 has value 4/3, carried without"
     " division as classSize 2 2 = 3 and pairTimesClass 2 2 w = 4. THE TERMINAL NAMES THE CELL AND"
     " THE RADII IN ITS OWN STATEMENT, and its second conjunct decides inMember 2 2 0 0 w = false"
     " -- the object's own space rejects the witness",
     "### DERIVES (b280) and DERIVED (b295, b296), as those acts left them; RE-DECIDED in the"
     " kernel, not discovered there. ### PROFILE: 426 -> 438 prints, all zero-axiom, the 426"
     " pre-existing byte-identical against git HEAD; 12 B298 declarations -- the terminal, its"
     " denominator, six polarity controls, two not-dead witnesses matching b271's banked 4(N-q), a"
     " uniformity control, and the UNAVAILABLE arm at (2,1) where b296's construction collides."
     " ### SCOPE, IN THE ROWS THEMSELVES: THE PAIR CERTIFIES SHARPNESS AT THAT CELL, NOT THE"
     " EQUIVALENCE IN GENERAL -- which quantifies over all levels and places, is not finite, and is"
     " NOT certified by anything in the kernel. ### NOT A ROUTE; M-2 unchanged",
     "SIDE-global-section/Core/BoundaryValueShadow.lean; AXIOM_PRINTS.txt;"
     " data/b298_the_boundary_terminal.txt; CORRESPONDENCE.md rows 112-113"),
    # ### THE ARC'S OWN FILING ROWS (b297).
    ("m2-arc-fold", "b297 (filed) -- the arc is b283-b296, fourteen acts",
     "the M-2 campaign's second arc, folded into FINDINGS.md as one dated section: the tower map"
     " is a filtration and not an action (b283); no dilation preserves the object's space, failing"
     " dually with the units as the leftover (b284); the archimedean space is"
     " (NAMED-NOT-CONSTRUCTED) in the corpus and (SUPPLIED BY SOURCE) as L^2(R)_ev with two"
     " conditions at cutoff [-1,1] (b285-b287); the corpus's two descriptions name one space"
     " (b287); the archimedean product is invariant under dilation and the transform reflects the"
     " family, with S(1,1) self-dual (b288, b291); the instrument vectors are the source's and lie"
     " outside the object's space, with no measurement disturbed (b291, b292); the finite"
     " two-radius family is constructed with the object as its verified diagonal (b293); and the"
     " annihilation criterion is an equivalence whose threshold falls out of the operator's"
     " reading scale (b294-b296)",
     "### FILED (b297). ### The results are THEIR OWNING ACTS', transcribed at the grades those"
     " acts left them; NO GRADE MOVED and NO ACT WAS RE-VERDICTED. ### 36 quotations verified"
     " verbatim against the acts that ORIGINATED them, 0 unfindable, with a discrimination arm."
     " ### FINDINGS.md +194 / -0, purely additive. ### The arc's four corrections to its own"
     " readings are filed as corrections to FACTS, not re-verdicts. ### M-2 unchanged",
     "PLACE-papers/FINDINGS.md section 'THE M-2 CAMPAIGN, b283-b296'; data/b297_the_fold.txt;"
     " CORRESPONDENCE.md rows 108-111"),
    ("kernel-plan", "b297 (filed, not built)",
     "five candidates assessed against two tests -- is it finite-decidable, AND can a terminal's"
     " own statement carry its own scope. The family's definition and dimension law, the diagonal"
     " identification, and the transform-side fiber-sum collapse are all finite-decidable and all"
     " REFUSED on the second test; the function-side index-landing argument is ALREADY BUILT"
     " (BallAbsorptionShadow, printing since b289). ### EXACTLY ONE PASSES BOTH: the existence"
     " statement on a relaxed member -- that Son(2,2; -1,0) contains a vector of value 4/3 --"
     " because a terminal that NAMES THE MEMBER in its own statement carries its scope inherently,"
     " whereas a bare value does not",
     "### FILED, NOT BUILT; the build is THE AUTHOR'S CALL. ### 0 .lean files moved. ### Refusals"
     " are listed with their reasons: everything analysis-bound (b280's S2 closure step, the"
     " chain's one uncompiled link), everything exposed to the escaped-mass artifact (b284, b293),"
     " and every statement quantifying over all levels and places -- including the equivalence"
     " itself. ### WHERE THEY WOULD SIT: inside the existing kernel's Core with correspondence rows"
     " to the barrier terminals, NOT a new repository -- a lane earns a repository when it becomes"
     " independent, and this lane is the identity chain's own",
     "data/b297_the_fold.txt Component 2; PLACE-papers/FINDINGS.md 'The kernel plan'"),
    # ### THE PAIRING/BARRIER LANE (b295, b296).
    ("threshold-asymmetry", "b281 (the form's type) / b296 (the reading scale, measured)",
     "the operator reads its SECOND slot by pointwise evaluation on the ball (scale p^n) and its"
     " FIRST slot only through the fiber sums of the reduction Z/p^{2n} -> Z/p^{2n-1}, one step"
     " coarser than pointwise. EACH THRESHOLD IS THE DISTANCE FROM THAT SLOT'S CONDITION'S OWN"
     " BASE SCALE TO THE SCALE AT WHICH THE OPERATOR READS IT: distance 0 on the function side"
     " (level-free), distance (2n-1)-n = n-1 on the transform side (level-carrying). So the"
     " asymmetry is not between the two conditions but between the two ways the operator reads"
     " its two slots -- b281's `A != A^T` turned into a number",
     "### DERIVED (b296), and the reading scale MEASURED INDEPENDENTLY OF THE CRITERION at 6 of 6"
     " cells with both polarities firing: p^{2n-2} does not determine G_f, p^{2n} does but is not"
     " minimal. ### CONSEQUENCE, MEASURED SEPARATELY: on the object's own space the annihilation"
     " is ONE-SIDED -- the function-side condition alone gives an identically zero form at all six"
     " cells, the transform-side condition alone only at the three n = 1 cells."
     " ### `W-ORD-READING-SCALE-GENERAL`: derivation and measurement not shown to agree outside"
     " the six cells. ### NOT A ROUTE; M-2 unchanged",
     "data/b296_the_asymmetry.txt; data/b296_asymmetry_run.txt; CORRESPONDENCE.md row 107"),
    ("criterion-sharpness", "b295 (sufficiency) / b296 (necessity)",
     "the first-level pairing vanishes identically on Son(p,n; a,b) -- as a FORM, both slots --"
     " IF AND ONLY IF a >= 0 or b >= n-1. Necessity is witnessed by ONE vector per cell covering"
     " the whole region below both thresholds:"
     " h = e_{p^{n-1}} - e_{p^{n-1}+p^{2n-2}} + e_{p^n} - e_{p^n+p^{2n-1}}, with"
     " <A h, h> = 2 p^{n-1} (p-1) / (p^n - 1)",
     "### DERIVED both ways (b295 sufficiency, b296 necessity). Each hypothesis is used exactly"
     " once in the construction: b <= n-2 puts f's two points in one p^{n+b} fiber, a <= -1 puts"
     " g's two points off B_a. ### CONTROLS: 6 of 6 registered values landed exactly (5 by the"
     " general construction, 1 by a registered fallback where the construction collides at (2,1)"
     " and the general arm reports UNAVAILABLE); coverage 30 of 30 live members; both negative"
     " polarities 6/6. ### NOT A ROUTE: every nonzero member weakens the object's FIRST condition"
     " and every witness has mass ON the ball, which that condition forbids. ### M-2 unchanged",
     "data/b296_the_asymmetry.txt; data/b296_asymmetry_run.txt; CORRESPONDENCE.md row 107"),
    # ### THE PAIRING/BARRIER LANE'S FIRST KEY (b295). ### **UNTIL THIS ROW THE LANE HAD NONE,
    # ### SO EVERY QUERY ABOUT IT COULD ONLY MISS -- b181's lane limit, live in a new place.**
    ("second-zero-mechanism", "b270 (the barrier's hypothesis) / b280-b281 (the diagonal) / "
     "b294 (the grid, and the reading corrected at b295) / b295 (the criterion)",
     "the first-level pairing <A .,.> at k = n vanishes IDENTICALLY -- as a FORM, both slots -- on"
     " Son(p,n; a,b) whenever a >= 0 OR b >= n-1; the function-side threshold is the object's own"
     " radius and does not move, the transform-side threshold is n-1 and moves with the level, and"
     " they coincide at level 1 and nowhere else. b294's zero on Son(p,n; -1,0) is DERIVED at"
     " level 1 and is NOT a zero above it: Son(2,2; -1,0) contains e_2-e_6+e_4-e_12 with value 4/3",
     "### DERIVED for sufficiency (b295, from b270's pairing, b281's A, b293's collapse);"
     " ### NECESSITY MEASURED at 80 members over six cells and NOT DERIVED"
     " (W-ORD-CRITERION-NECESSITY). ### b280 and b281 are NOT re-verdicted -- b295 re-measured"
     " every a >= 0 member on the FULL form and got identically zero, 40 of 40."
     " ### NOT A ROUTE: every nonzero member weakens the object's FIRST condition and every"
     " witness has mass ON the ball, which that condition forbids. ### M-2 unchanged",
     "data/b295_the_second_mechanism.txt; data/b295_mechanism_run.txt;"
     " CORRESPONDENCE.md row 106"),
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
    # ### THE RULING ROWS (b244). ### THE `q-orientation` ROW BELOW IS A **SECOND** ROW UNDER
    # ### THAT KEY: b241's ROUTE IS NOT REWRITTEN, so a query returns the route and then the
    # ### ruling. ### An index that erased the route would hide that the texts underdetermined it.
    ('q-orientation', 'b244 (the author ruling; b241 routed it)',
     'RULE Q: O1 -- Q.value := -Theta_q, executed as a documented binding in File E with the '
     'five owner texts cited BY NUMBER: sec 19 comparison; b36_act8.py:175; sec 20(c) closed '
     'form; the recurring (Theta_q - PR) pairing; File E own operator. ### CORRESPONDENCE row 92',
     '### A RULING, NOT A DERIVATION -- the author word, and b241 had ROUTED this and chosen '
     'nothing. ### **THE AGGREGATION IS STILL UNSTATED AND THE BINDING SAYS SO**: the five texts '
     'ORIENT Theta_q inside their own comparisons and NONE assembles it into Q.value. '
     '### **M-2 IS NOT CLOSED BY THIS BINDING.** ### DISCLOSED: O1 SHRINKS the residual -- it is '
     "b240 banked variant V2 -- and it does NOT close it (V2 stays 19x-24x the combined bar, "
     'resid47 untouched). ### The movement was NOT computed in b244',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean (QuotientTrace docstring); '
     'CORRESPONDENCE.md row 92; data/b244_serializing_close.txt'),
    ('rule-delta-minus', 'b244 (the author ruling; b241 filed it)',
     'RULE Delta_-: D1 -- RULE M-1 combination amended to T.value := Tr_full + E2 - Delta_-, '
     "per sec 19 own row 'our object trace = this - Delta_-(g)' and act 8 assembly "
     'RIGHT = (Tr_full + E2 - Dneg) - Thq. ### CORRESPONDENCE row 91',
     '### A RULING, NOT A DERIVATION. ### **Delta_- DEFINITION AND BINDING ARE UNTOUCHED** -- '
     'sec 17 odd-index t(n) series via b37_act9.eps_masked(rr, odd), which b241 verified b240 had '
     'bound correctly. ### **ONLY THE SIGN IN THE COMBINATION MOVED.** ### M-4 remains the '
     'definition open debt and is NOT paid at bench (b242, branch SLOW). ### NO CODE MOVED and it '
     'was PROVED: comment-stripped File E identical to its pre-amendment blob, 19 lines both sides',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean (ArchimedeanE1Trace docstring); '
     'CORRESPONDENCE.md row 91; data/b244_serializing_close.txt'),
    ('rule-modes', 'b244 (the author ruling; b242 measured it)',
     'RULE MODES: K1 -- the DEFINITION stays Lemma F.1 eleven modes; the PER-CELL REALIZATION '
     'reports the SEVEN computable plus A TAIL TERM IN ITS BAR. ### W-ORD-MODE-PRECISION filed '
     '(K3) as the bounded instrument act that closes the ceiling. ### CORRESPONDENCE row 93',
     '### A RULING ON A REALIZATION, NOT ON A DEFINITION. ### THE MEASUREMENT THAT FORCED IT '
     '(b242): lam2 reaches 4.7e-16 at n=7 so float64 carries SEVEN where Lemma F.1 certifies '
     'ELEVEN, and n_last = 6 at EVERY NQ from 500 to 1300 -- more quadrature buys no modes; the '
     'NQ-spread jumps 61x-249x when the first sub-floor mode enters. ### **THE TAIL IS NOT '
     'BOUNDED** -- b242 branch is (SLOW) and the envelope was derived, printed and REFUSED. '
     '### So a bar written per K1 CARRIES AN UNBOUNDED TERM, and b245 must say so in its own words',
     'SIDE-global-section/Interfaces/FiniteInstanceIdentity.lean (ArchimedeanE1Trace docstring); '
     'CORRESPONDENCE.md row 93; data/b242_left_mode_axis.txt'),
    ('second-face-off', 'b244 (named); b245 (the act itself, NOT RUN)',
     "b245 is THE SECOND FACE-OFF. ### PRECONDITIONS: (1) b244 rulings executed -- GREEN; "
     '(2) right-side bars certified -- GREEN with a looseness rider; (3) bar_L in its honest form '
     'per K1 -- **AMBER, and it is the real one**; (4) the banked-meanings discipline -- b245 own '
     'first act; (5) M-2 STILL OPEN. ### TWO GREEN, TWO AMBER, ONE OPEN BY DESIGN',
     '### NOT A RESULT. ### A LIST OF PRECONDITIONS AND NOTHING ELSE -- b245 HAS NOT RUN. '
     '### THE AMBER THAT MATTERS: b245 inherits a bar with an UNBOUNDED TERM in it, and the '
     'direction is already known and against the programme -- bar_L may be 2.4x-2.9x TOO SMALL '
     '(b242 refused extrapolation). ### **A BAR THAT IS TOO SMALL MAKES A SEPARATION LOOK MORE '
     'SIGNIFICANT THAN IT IS.** ### The patent session can slot at any STOP and needs nothing '
     'from b245',
     'data/b244_serializing_close.txt (2.3); reports/2026-08-29-the-serializing-close.md'),
    # ### THE SECOND FACE-OFF'S OWN ROW (b245). ### A SECOND ROW UNDER `second-face-off`:
    # ### b244's row LISTED the preconditions and said the act had not run; this one is the act.
    ('second-face-off', 'b245 (the act, RUN)',
     'the ruled combination L := (Tr_full + E2 - Delta_-) + (-Theta_q) computed for the FIRST '
     'TIME against R := A - PR at the banked six cells, NMODE = 7 per RULE MODES K1. '
     '### BRANCH **(DISSONANT-BEYOND)** by the rule banked before any number. ### |L-R| runs '
     '6.662044 down to 4.072688 against BOUNDED bars 1.028 down to 0.303. ### FOUR of the five '
     'contentful tests PASS (T-A cell profile, T-B NV-invariance, T-C archimedean-only '
     'reduction, T-D mode signature); ### T-E, the bank cross-check, FAILED by 6.78e-02',
     '### THE BRANCH FIRED ON A TEST **THIS EXECUTOR MIS-SPECIFIED**, and the diagnostic (run '
     'AFTER the branch, which it did not touch) names the term to five figures: ### T-E compared '
     'a SEVEN-mode run against b38 bank computed at TEN modes, and the deviation equals '
     'tr[7]+tr[8]+tr[9] at all six cells to 5e-5 -- b38 own rounding floor. ### **T-E DETECTED '
     'THE RULING DOING WHAT IT WAS RULED TO DO, NOT INSTRUMENT DRIFT.** ### THE BRANCH STANDS: a '
     'banked rule is not revised because the executor later understands why it fired. '
     '### **THE M-4 SHADOW WAS THEREFORE *NOT* FILED** -- the ferry conditioned that filing on '
     '(ACCOUNTED) -- though the M-4 SHAPE HOLDS: (L-R)/resid47 = 1.67-1.81 across six cells, an '
     '8.4% spread, with resid47 at 56%-60% of the shortfall and the corpus own -D_dict carrying '
     'the rest. ### NO EVIDENCE AGAINST THE IDENTITY FORM; suspect 4 NOT indicted',
     'data/b245_second_face_off.txt; data/b245_te_diagnosis.txt; '
     'reports/2026-08-29-the-second-face-off.md'),
    # ### THE TWO-TAILS ROWS (b246).
    ('two-tails', 'b246',
     'whether b245 shortfall two terms are the even- and odd-sector tails of ONE mode series, '
     'decided by independent computation from b242 banked per-mode arrays. '
     '### BRANCH **(TWO OBJECTS)** -- all five registered tests FAIL under the primary reading, '
     'and four of them by three to five orders past their bands: T-1 by 1.76-2.62 against a 5e-5 '
     'floor; T-2 by 0.43-1.22; T-3 ratio 4.35-5.85 against the band [1.673, 1.785]; T-4 not '
     'monotone; T-5 fails at five of six cells',
     '### A MEASUREMENT, AND THE STRUCTURAL REASON IS CHECKABLE FROM THE PRINTED COLUMNS: '
     '`resid47` is a shortfall of the **TRACE** series, still at 0.257 at mode 6 and not '
     'converging; `-D_dict` = `E2full + E2even + (PR - Theta_q)` is sector arithmetic on the '
     '**eps** series, which is CONVERGED by mode 6 (per-mode terms reach 3.9e-16 by mode 7). '
     '### **A CONVERGED SERIES HAS NO TAIL**, so -D_dict cannot be one. ### THE TWO TERMS STAY '
     'SEPARATELY OWNED; ### **M-4 COVERS resid47 AND NOT THE OTHER TERM**, and the sentence '
     '"paying M-4 pays the whole bench shortfall" MAY NOT BE WRITTEN on this branch. '
     '### NEAR-MISS REPORTED AS A MISS: alternate reading (R3) lands in the T-3 band at a^2 = 2 '
     'ONLY and drifts 12% low by a^2 = 12 -- a coincidence at the one cell where PR and Theta_q '
     'both vanish. ### **THE NAVIGATOR EXPECTED (ONE OBJECT); THE EXECUTOR EXPECTED (TWO) AND '
     'SAID WHY IN ADVANCE**',
     'data/b246_two_tails.txt; data/b246_tails_run.txt; '
     'reports/2026-08-29-the-two-tails.md'),
    ('d-dict', 'b246 (computed) / act 8 and act 9 (owners) / b241 (the double name found)',
     'D_dict := (Theta_q - PR) + (Delta_- - 2*E2full), sec 20(a) formula printed by both '
     'b37_act9.py:169 and b38_act10.py:188. ### RE-COMPUTED at b246 from b242 per-mode arrays by '
     'parity and matching b38 banked column to ~1e-6 at every cell. ### AND THE SECOND OBJECT '
     'UNDER THE SAME NAME, kept apart: `Dneg_raw` = the RAW ODD-TRACE SLICE (b36_act8.py:172), '
     'and `SECTOR_SPLIT_DIFF := Dneg_raw - Delta_-` -- ### **WHICH IS NOT D_dict AND IS NOT '
     'CALLED SO**',
     '### THE PARITY-SPLIT CROSS-CHECK **PASSED** and it is the one clean cross-check of this '
     'arc -- ### **THE ONE b245 T-E WAS TRYING TO BE**, and it worked because the axes were '
     'MATCHED AND PRINTED BEFORE ANY NUMBER WAS COMPARED (W-ORD-TE-SPEC honoured in form). '
     '### b241 finding stands and is not repealed: "DIFFERENT OBJECTS, SAME NAME, ONE CORPUS." '
     '### sec 19 row fixes the DEFINITION in favour of the eps-mask series; b246 computed BOTH '
     'rather than choosing',
     'data/b246_tails_run.txt (2.3, 2.4); data/b241_residual_ledger.txt (4.5)'),
    # ### THE M-4 STATEMENT ROWS (b247). ### A STATEMENT WITH A NAMED HOLE IS NOT A THEOREM, AND
    # ### THE ROW SAYS SO IN ITS OWN GRADE CELL.
    ('m4-statement', 'b247',
     "M-4 written from its owners with every constituent of t(n) = lambda(n)^2 xi_n(1)^2 / "
     '(1 - lambda(n)^2) unfolded: lambda(n)^2 = mu_{2n}, the EVEN-INDEXED concentration '
     'eigenvalue of the time-and-band limiting operator on L^2[-1,1] at FIXED c = 2*pi '
     '(Slepian-Pollak 1961, pin P1); xi_n(1) = sqrt(2)*psi_{2n}(1) under the half-line norm '
     '(pin P2), the endpoint obtained from the eigenfunction equation and NOT extrapolated. '
     '### THE THEOREM: (i) lambda(n) -> 0 at a STATED RATE, (ii) xi_n(1)^2 bounded or its growth '
     'dominated, (iii) hence sum t(n) converges WITH AN EXPLICIT TAIL ENVELOPE at the K1 cut',
     '### **THE STATEMENT HALTS AT CLAUSE (i)s RATE AND THE MISSING SENTENCE IS NAMED.** '
     '### NO OWNER IN THIS CORPUS STATES A RATE: Lemma F.1 certifies a TRUNCATION (eleven terms '
     'uniform to 1e-11), not a tail; sec 17 NAMES the debt rather than discharging it; and the '
     'bench cannot fill it because lambda(n)^2 reaches the float64 floor at n = 7. '
     '### **AND CLAUSE (ii)s FIRST DISJUNCT IS FALSE ON THE CERTIFIED RANGE** -- xi_n(1)^2 GROWS '
     'from 6.854e-04 to 24.94 across n = 0..6, a factor of about 36,000, so only the '
     '"growth dominated" form is live. ### **NO DERIVATION WAS PERFORMED. M-4 IS NOT PAID, NOT '
     'PAYABLE TODAY, AND NOT NEARLY SO.** ### The route is priced in five steps; S2 (a decay rate '
     'at FIXED c) is the BINDING STEP and nothing in the corpus supplies it',
     'data/b247_m4_statement_and_route.txt; data/b247_statement_reads.txt; '
     'reports/2026-08-29-the-m4-statement-and-route.md'),
    ('xi-alpha-question', 'b247',
     'is xi_n(1) the arcs alpha? ### **VERDICT: (DOUBLE-NAME).** ### xi_n(1) is the value at the '
     'RIGHT endpoint of [-1,1] of a prolate eigenfunction normalized by INT_{-1}^{1} psi^2 = 1 '
     'then scaled by sqrt(2); alpha = psi(1) is the value at the LEFT endpoint of [1, infinity) '
     'for the RRJT eigenfunction whose INT_1^inf psi^2 is FINITE BUT NOT NORMALIZED -- that '
     'integral being the right-hand side of the Wronskian identity itself',
     '### SETTLED BY A DISCRIMINATOR **REGISTERED BEFORE THE NUMBER WAS SEEN**: b212 measured '
     '|alpha_odd|/(pi*Lambda) = 1.0 at every odd eigenvalue, i.e. |alpha| is CONSTANT in the '
     'index, so if xi_n(1) were the same object it would be constant too. ### **MEASURED: '
     'xi_n(1) runs 0.026180 to 4.994344 over the certified range, max/min = 190.77**, against a '
     'forced constant of 0.945442 if the hypothesis held. ### **TWO DIFFERENT DOMAINS, TWO '
     'DIFFERENT ENDPOINTS OF THEM, TWO DIFFERENT NORMALIZATIONS.** ### WHAT IS **NOT** CLAIMED: '
     'that no relation exists -- a transform relating the exterior and interior problems would be '
     'a RESULT owed; this row says only that the two endpoint values are not the same number and '
     'are not defined on the same object',
     'data/b247_m4_statement_and_route.txt (Component 2, A-2); data/b211_alternation_derived.txt; '
     'data/b212_odd_family.txt'),
    # ### THE SECOND-OBJECT ROWS (b248) AND THE PRECISION ROWS (b249). ### b248 OWNS THIS WRITE.
    ('e2-arrangement', 'b248',
     "does 'eps-regularized archimedean E1-trace' mean the eps-corrections SUBTRACT from the raw "
     'trace or ADD? ### **VERDICT: (ADDITIVE-FORCED).** ### THREE ARRANGEMENTS BY THREE OWNERS, '
     'ALL ADDITIVE IN E2: sec 19 brackets [Tr_inf + int g eps]; b36_act8.py:175 parenthesizes '
     '(Tr_full + E2 - Dneg); and the ruled C2+D1 form is Tr_full + E2 - Delta_-. ### b38:182 is '
     'A expression, NOT an arrangement of T -- sec 20(b) reads that same line as the CC-4.7 '
     'REPRODUCTION ERROR against [A + E2]',
     '### QUOTATION-FORCED, NOT ARGUED FROM WHAT THE WORD USUALLY MEANS. ### **THE WORD '
     '"REGULARIZED" NAMES A DIFFERENT SUBTRACTION, AND IT IS UNPERFORMED**: sec 20(b) calls it '
     'the divergent-part subtraction, and b241/b245/b247 located its bench size as resid47 -- '
     'that is M-4, NOT E2. ### **NO DECISION CARD WAS ASSEMBLED**: the card was conditional on '
     '(SUBTRACTIVE-FORCED) and an executor does not manufacture one the texts did not ask for. '
     '### DISCLOSED AT REGISTRATION BEFORE THE VERDICT WAS DRAFTED: the subtractive reading would '
     'have cut L-R by 2*E2 = 1.95 to 3.36, i.e. 45%-50% of the shortfall. ### **THE TEXTS FORCED '
     'THE READING THAT DOES NOT SHRINK IT**',
     'data/b248_second_object.txt (Component 1); reports/2026-08-29-the-second-object.md'),
    ('junction-piece', 'b248',
     'the second object split per cell for the FIRST time: -D_dict = (E2full + E2even) + '
     '(PR - Theta_q). ### THE ARCHIMEDEAN PIECE runs 2.681242 down to 1.595154 and carries '
     '**88% to 100%**; ### THE JUNCTION PIECE runs 0.000000 to 0.244027 and carries **0% to 12%**',
     '### THE REGISTERED PREDICTION IS **HALF RIGHT AND IS REPORTED AS HALF RIGHT**. ### LIMB 1 '
     '(vanishes at a^2 = 2) CONFIRMED exactly -- PR and Theta_q are identically zero there. '
     '### LIMB 2 (grows with the active primes) **REFUTED**: two drops, at a^2 = 4 (0.106484 -> '
     '0.087342) and at a^2 = 9 (0.244027 -> 0.135020). ### **THE PREDICTION TREATED A DIFFERENCE '
     'OF TWO WEIGHTED SUMS AS THOUGH IT WERE A COUNT.** ### NEITHER PIECE IS M-4 -- M-4 covers '
     'resid47 and nothing else (b246, unrevised). ### Piece 2 owner names M-2 again: Theta_q '
     'aggregation into Q.value is STILL UNSTATED',
     'data/b248_split_run.txt; data/b248_second_object.txt (Component 2)'),
    ('mode-precision', 'b249 (K3)',
     'the concentration spectrum and endpoint values measured at EXTENDED PRECISION past the '
     'float64 veil. ### INSTRUMENT: the corpus OWN prolate instrument extended into mpmath '
     '(Gauss-Legendre nodes by Newton, symmetric eigendecomposition), dps 120 / NQ 80, modes '
     'n = 0..12 on the EVEN sub-sequence per pin P1. ### **b205 stepper NOT reused: it is the '
     'RRJT EXTERIOR ODE and b247 ruled it (DOUBLE-NAME).** ### G-REPRO, G-SELF, G-EQ all PASS',
     '### **W-ORD-MODE-PRECISION (K3) DISCHARGED.** ### THE VEIL IS LIFTED: lambda(n)^2 continues '
     'cleanly from 3.85e-16 at n=7 down to 6.50e-38 at n=12, where b242 float64 could see only '
     'noise. ### **G-REPRO TOOK THREE FORMS BEFORE IT WAS RIGHT, AND THE FIRST TWO ARE '
     'DISCLOSED**: a constant tolerance is NOT the ferry criterion of "within float64 own error", '
     'which is mode-dependent; and the comparison is additionally floored by **the PRINTED '
     'PRECISION of b242 bank** (ten significant digits for lambda^2, nine decimals for xi). '
     '### **THAT IS THE THIRD CONSECUTIVE ACT TO MEET A BANK PRINT FLOOR** (b245 met b38 four '
     'decimals, b246 floored at 5e-5), and W-ORD-TE-SPEC is filed for extension to require a '
     'bank PRINTED PRECISION be named alongside its axes',
     'data/b249_mode_precision.txt; data/b249_precision_run.txt; '
     'reports/2026-08-29-the-precision-veil.md'),
    ('t-series', 'b249 (K3)',
     't(n) = lambda(n)^2 xi_n(1)^2/(1-lambda(n)^2) measured to n = 12 at dps 120. ### **BRANCH '
     '(PLUNGES)**: t(n) falls 5.17e-11, 1.12e-14, 1.35e-18, 9.91e-23, 4.65e-27, 1.46e-31, '
     '3.18e-36 -- strictly decreasing from n = 6 onward -- and the partial sums SETTLE at '
     '**22.996475683870529679**. ### xi_n(1) GROWS but only slowly (5.38 -> 7.00 over the newly '
     'reached modes, ratios all under 1.2), so the growth is utterly dominated',
     '### **M-4 TRUE-AT-BENCH**, with the measured rate filed as the derivation target and the '
     'derivation act confirmation RECOMMENDED to the author. ### **AND THE LIMIT IN THE SAME '
     'BREATH: TRUE-AT-BENCH IS A BENCH GRADE AND NOT A THEOREM** -- finitely many modes at one '
     'instrument setting. ### **M-4 IS NOT PAID AND ITS STATEMENT STILL HALTS AT CLAUSE (i) '
     'RATE, EXACTLY WHERE b247 LEFT IT.** ### THE PARTIAL SUM AGREES WITH the corpus '
     "INDEPENDENTLY BANKED eps'(1+) PIN 22.9964757 (b35, 2026-08-18) TO EIGHT SIGNIFICANT "
     'DIGITS -- ### **AND THE PIN WAS NOT FITTED TO.** ### NO EXTRAPOLATION IS BANKED AS A '
     'BOUND; b242 refusal is the precedent and a measured rate is not a tail bound',
     'data/b249_mode_precision.txt; reports/2026-08-29-the-precision-veil.md'),
    ('m4-derivation', 'b250 (derivation at content)',
     'the ONE THEOREM proved at content about the t(n) series, on b247 statement unchanged. '
     '### SIX STEPS: S0 the series identity (eps and t(n) are ONE object, by Leibniz from the '
     'supplied (85), NOT by resemblance -- b247 double-name hazard answered); S1 lambda_n < 1 '
     'strictly (band-limited + compactly supported => entire and vanishing on a set with an '
     'accumulation point => zero); S2 the decay; S3a the per-mode endpoint bound; S3b the '
     'summed Mercer identity; S4 the envelope',
     '### **GRADE: DERIVES-on-IMP, on FOUR named foundational imports (Plancherel, identity '
     'theorem, Schmidt/Eckart-Young, Mercer), ALL TRUSTED-AT-CITE and NONE TOOLED** -- the '
     'residence tree carries NO MATHLIB, which this act verified twice (a filesystem search, '
     'and `Nat.factorial` failing to resolve in the shadow). ### **THE FERRY BEST-CASE TARGET '
     'OF ZERO IMPORTS IS NOT MET AND THE SHORTFALL IS FOUR TEXTBOOK THEOREMS, NAMED.** '
     '### **S3a HALTS AND IS REPORTED AS HALTING** (W-ORD-XI-PERMODE) -- the per-mode '
     'polynomial bound on xi_n(1)^2 needs the Bouwkamp Legendre-coefficient decay, not at '
     'content; the two obvious routes go INVERSE in mu_n, as b247 already measured. ### **THE '
     'THEOREM ROUTES AROUND S3a; IT DOES NOT ANSWER IT**, and the price is paid at S4, where '
     'the MEASUREMENT-FREE envelope bounds the tail by a constant but CANNOT be made to tend '
     'to zero. ### **S3b IS THE FIND, AND IT WAS REGISTERED IN ADVANCE AS A PREDICTION ABOUT '
     'THE CORPUS ITSELF: sum_n lambda(n)^2 xi_n(1)^2 = c/pi + sin(2c)/(2 pi), which at '
     'c = 2 pi is EXACTLY 2 -- RE-DERIVING the corpus OWN banked C0 gate FROM FIRST '
     'PRINCIPLES. A pin carried as a MEASURED NUMBER since b35 is now a THEOREM, and its '
     'c-dependence is known (the clean 2 needs sin(2c) = 0, NOT generic).** ### IMP-3 '
     '(Landau-Widom) is NOT used and is NOT needed; b243 refusal of it at fixed c stands. '
     '### **M-4 pays ONE term of the shortfall. M-2, M-3, M-5 untouched. h2 untouched**',
     'data/b250_m4_derivation.txt; data/b250_derivation_checks.txt; '
     'Core/M4EnvelopeShadow.lean; reports/2026-08-29-the-m4-derivation.md'),
    ('s2-decay-route', 'b250 (derivation at content)',
     'HOW the concentration eigenvalues are shown to decay at FIXED c = 2 pi. ### Q = A*A '
     'with A the finite Fourier transform, so mu_N = s_N(A)^2; Schmidt/Eckart-Young bounds '
     's_N by the error of ANY rank-N approximation; and an ANALYTIC kernel admits degenerate '
     'approximations at a FACTORIAL rate. ### **TWO ROUTES, AND THE DIFFERENCE BETWEEN THEM '
     'IS THE IMPORT LIST**',
     '### **ROUTE (a), ZERO SPECIFIC IMPORTS AND THE ONE THE THEOREM RESTS ON**: the '
     'EXPONENTIAL OWN TAYLOR SERIES, with the two rank-one factors elementary integrals of '
     'powers, giving mu_N <= T(N)^2, T(N) = sum_{m>=N} (2/(2m+1)) c^m/m! at c = 2 pi. '
     '### **NO BESSEL FUNCTION, NO LEGENDRE EXPANSION, NO SPECIAL-FUNCTION IDENTITY.** '
     '### **THIS ROUTE WAS NOT IN THE REGISTRATION and is reported as an IMPROVEMENT on the '
     'registered route, not as it.** ### ROUTE (b), ONE IMPORT (Jacobi-Anger), sharper by '
     'many orders, NOT load-bearing. ### **ITS RANGE CONDITION WAS REGISTERED BEFORE '
     'COMPUTING: the Bessel factorial bound needs z^2/4 < k + 3/2, i.e. k >= 9 at c = 2 pi. '
     'THE COMPUTATION CONFIRMED k >= 9.** ### The join to Lemma F.1 (k = 0..10) OVERLAPS at '
     'k = 9,10 rather than merely abutting -- ### **but F.1 is a TRUNCATION certificate, not '
     'a tail bound, so the join is of certificates of DIFFERENT SPECIES and the theorem does '
     'NOT use the F.1 half.** Route (a) is valid at every N with no range condition. '
     '### Both bounds checked against b249 measured mu_N at N = 9..24 as CONTROLS: both hold '
     'at every N, LOOSE BY MANY ORDERS, and the slack is printed rather than hidden',
     'data/b250_m4_derivation.txt; data/b250_derivation_checks.txt'),
    ('third-face-off', 'b251 (bench computation + one re-attribution)',
     'the bench shortfall L - R computed at six cells with M-4 paid, and decomposed into '
     'THREE NAMED PIECES: Delta_2real (the two-realizations term), 2*E2full - Dneg (the '
     'RULED BINDING C2+D1 own terms, tabulated though NOT a suspect), and the junction piece '
     '(PR - Theta_q). ### Sides under C2+D1, Q := -Theta_q, K1. ### G-INDEP structural (each '
     'quantity from its OWN owner in b38_act10, none re-implemented); G-STAB across NQ = 500, '
     '700, 900 plus ONE refinement at 1100',
     '### **BRANCH (IMPOSTER-NAMED) ON ITS ACCOUNTING LIMB.** ### Delta_2real carries '
     '**60.775% to 69.995% of L - R at EVERY cell** -- the dominant term without exception; '
     'the third piece 30.005%-34.546%; the junction piece 0.000%-5.874%, the smallest of the '
     'three everywhere. ### **MAX LEFTOVER 1.78e-15: NOTHING BEYOND THE THREE NAMED PIECES, '
     'SO (DISSONANT-BEYOND) IS NOT TRIGGERED.** ### **LIMB 2 -- the envelope line -- IS '
     'STRUCK AS INAPPLICABLE, NOT FALSIFIED, AND THE STRIKE WAS BANKED BEFORE THE RUN**: see '
     'two-realizations. ### **THE BARS ARE WIDE AND THE ACT SAYS SO** -- TrTail sits at 43%% '
     'to 71%% of the G-STAB bar, so the identification is CONSISTENT rather than SHARP, and '
     '**the spread does NOT shrink monotonically with NQ**, so convergence of the mode sum '
     'was NOT established. ### **THE FORM IS NOT INDICTED: no act has produced evidence '
     'against T + Q = wInf - wPrimes.** ### A number in this act OWN prose was WRONG and gate '
     '8 caught it -- the share range was read off the run rounded table by taking the LAST '
     'ROW as the minimum instead of scanning the column; corrected to three decimals and '
     'disclosed in the bank section (D.1)',
     'data/b251_third_face_off.txt; data/b251_run.txt; data/b251_meanings.txt; '
     'reports/2026-08-29-the-third-face-off.md'),
    ('two-realizations', 'b251 (re-attribution derived before the run)',
     '### **WHAT THE FACE-OFF `resid47` TERM ACTUALLY IS.** ### Both owners that state the '
     'residue line state the SAME thing -- b38_act10.py:182 `resid = TrN - A - E2N` and '
     'b36_act8.py:184 `resid47 = Tr_full - (A + E2)` -- so ### **resid47 IS ALREADY A '
     'TWO-REALIZATIONS DIFFERENCE**: the archimedean trace built as a MODE SUM (trace_modes, '
     'a corr-weighted dilation overlap) minus the same object built as a QUADRATURE '
     '(left_side, a single U-axis integral with NO mode index), less E2. ### The split: '
     '**resid47(NMODE) = Delta_2real - TrTail(NMODE)**',
     '### **THE NAME `resid47` CONCEALED THE SPECIES. ### IT IS NOT A REMAINDER OR AN ERROR '
     'TERM BUT A DISAGREEMENT BETWEEN TWO DEFINITIONS**, filed as **M-2-inf** with a dossier '
     'OPENED AND NOT DECIDED (b237), stating three readings (R-I quadrature is the object, '
     'R-II mode sum is, R-III they compute different objects and the identity names one) '
     'with **NO preference expressed and no evidence distinguishing them**. ### **THE '
     'DECOMPOSITION ITSELF IS ALGEBRAIC-RESTATEMENT AND WAS DECLARED SO IN THE HASH-GATED '
     'MEANINGS FILE BEFORE THE RUN** -- an identity that cannot fail cannot testify; the '
     'evidence is the SIZE question only. ### **AND b250 ENVELOPE WAS REFUSED FOR THIS TAIL '
     'BEFORE THE RUN, ON b247 DOUBLE-NAME RULING**: 1.158e-14 bounds sum t(n), an ENDPOINT '
     'weight series, while TrTail is a corr-weighted dilation overlap -- two functionals of '
     'the same eigenfunctions with NO derivation between them. ### **THE MEASUREMENT SETTLES '
     'THE SCALE OF THE ERROR AVOIDED: TrTail IS 2.9e12 TO 7.0e12 TIMES LARGER THAN THE '
     'ENVELOPE.** ### b250 is NOT re-verdicted; what was corrected is the ferry APPLICATION '
     'of it',
     'data/b251_m2inf_dossier.txt; data/b251_meanings.txt; data/b251_third_face_off.txt'),
    ('mode-sum-limit', 'b252 (bounded bench act; the b249 instrument extended)',
     'DOES the corr-weighted archimedean mode sum `Tr` converge, and to what? ### Measured at '
     'EXTENDED PRECISION to **N = 20 (prolate index 40, mu_20 = 7.162e-80)**, past the '
     'float64 veil, at all six cells, with the quadrature object `A + E2` computed beside it '
     'from ITS OWN owners. ### Instrument: b249 solve scheme at dps 120 / NQ_e 120, overlaps '
     'by Gauss-Legendre with nodes ON THE TRUE SUPPORT and BARYCENTRIC interpolation',
     '### **BRANCH (DIVERGES/WANDERS) AT EVERY CELL.** ### `S_N` misses the registered '
     '1%-of-|S_N| settling threshold by 7.5x to 11.3x. ### **AND THE THRESHOLD-FREE EVIDENCE IS '
     'THE DECAY LAW: `n*w(n)` RISES AND FLATTENS TOWARD A NONZERO CONSTANT AT EVERY CELL** '
     '(1.876, 1.194, 0.949, 0.635, 0.601, 0.533), i.e. **w(n) ~ C/n**, whose sum diverges '
     'logarithmically; the log form checks against S_20 - S_10 to about 6%. ### **LIMIT IN THE '
     'SAME BREATH: A MEASURED DECAY LAW OVER n = 0..20 IS NOT A THEOREM -- b242 rule, a '
     'measured rate is not a tail bound. ### THE DIVERGENCE IS THE READING THE FORM IMPLIES '
     'AND IS NOT BANKED AS PROVED.** ### **THE EXACT FACT `A_n(0) = 1` FOR EVERY n WAS DERIVED '
     'FROM SOURCE BEFORE THE INSTRUMENT WAS BUILT AND THE INSTRUMENT REPRODUCES IT TO 3.0e-13**; '
     'G-EQ 4.4e-120; G-REPRO-A 3.076e-15 (machine precision); G-SELF agrees to 8.5e-16 up to '
     'n = 15 and **COVERS ONLY THAT RANGE, WHICH THE ACT SAYS RATHER THAN LETTING THE GATE NAME '
     'IMPLY MORE**. ### **AND THE FINDING REGISTERED IN ADVANCE AS AN EXPECTED FAILURE: b38 '
     'FLOAT64 EIGENVECTORS FOR n >= 7 ARE NOISE** -- its tr[n] collapse by up to 62x and wander '
     'non-monotonically while the clean values decay smoothly (b242 n_last = 6, seen from the '
     'other side). ### **CONSEQUENCE FOR b251, FILED AS A FACT NOT A RE-VERDICT: its TrTail(7) '
     'of 0.0805 at a^2 = 2 was built from noise; the clean value over the same modes is 0.801, '
     'TEN TIMES LARGER, and over n = 7..20 it is 2.024. ### b251 BRANCH STANDS AS BANKED (b246 '
     'rule).** ### **AND `Delta_2real := Tr_inf - A - E2` HAS NO LIMIT TO BE: b251 number is a '
     'PARTIAL SUM AT N = 10 AND THE NAME PRESUMED A LIMIT** -- any future act quoting it must '
     'quote its N. ### **NO RULING ON M-2-inf AND NO READING CHOSEN**; the dossier is APPENDED '
     'with the fact, prefix byte-for-byte intact, and the card is CITATION-SHAPED per the '
     'pre-banked MEANS. ### b250 envelope NAMED AND NEVER APPLIED, on b251 precedent',
     'data/b252_mode_sum_limit.txt; data/b252_run.txt; data/b252_meanings.txt; '
     'data/b251_m2inf_dossier.txt; reports/2026-08-29-the-mode-sums-limit.md'),
    ('m2inf-ruling', 'b253 (filings + one ruled re-binding at support-voice)',
     "the author's RULE M-2-inf Q1 executed: the QUADRATURE construction (left_side's "
     'one-axis integral) is the archimedean object the identity left column denotes; the '
     'per-cell realization of C2+D1 RE-BOUND to it; the mode sum (trace_modes) DEMOTED to a '
     'truncation diagnostic under the standing QUOTED-N law. ### **THE DEFINITION DOES NOT '
     'MOVE -- C2, D1, RULE Q O1 and RULE MODES K1 all stand; ONLY THE PER-CELL '
     "REALIZATION'S BINDING MOVED.** ### File E docstring only: comment-stripped HEAD vs "
     'work = **19 code lines both sides, IDENTICAL**. ### CORRESPONDENCE row 94, six cells, '
     'read back',
     '### **THE R-LABEL MATCH IS HALTED AS AMBIGUOUS AND ROUTED TO THE AUTHOR.** ### Q1 '
     'wording is R-I headline verbatim, but Q1 DECLINES R-I consequent (it demotes the mode '
     'sum to a DIAGNOSTIC, not an APPROXIMATION, and b252 refuted the approximation reading), '
     "while the ferry OWN disclosed consequence -- 'removes ... BY DEFINITION' -- is R-III's "
     "('THE SHORTFALL IS AN ARTEFACT OF THE PAIRING RATHER THAN A DEFICIT'). ### **WHAT "
     'TURNS ON IT: UNDER R-I b254 NUMBERS ARE A DEFICIT STILL OWED; UNDER R-III THEY ARE THE '
     'RESIDUE OF A PAIRING ERROR. ### THE TWO READINGS ASSIGN OPPOSITE MEANINGS TO b254 '
     'ENTIRE TABLE.** ### b237 governs -- an executor does not settle a definition. '
     '### R-II is excluded cleanly (Q1 names the quadrature; R-II names the mode sum). '
     '### **THE HALT HALTS THE MATCH ONLY: the re-binding is derived from Q1 OWN WORDS and '
     'the owners lines and does NOT consume the R-label, so every other component executed '
     'in full.** ### **AND THE EXECUTOR REGISTERED THE AMBIGUITY BEFORE WEIGHING THE '
     'DOSSIER TEXT** (registration section (D)). ### Q1 is DEFINITIONAL ONLY; b252 '
     'divergence remains a BENCH READING. ### NO FACE-OFF RAN. ### M-2..M-5 open',
     'data/b253_m2inf_ruling.txt; data/b253_registration_2026-08-29.txt; '
     'Interfaces/FiniteInstanceIdentity.lean; CORRESPONDENCE.md row 94; '
     'reports/2026-08-29-the-m2inf-ruling.md'),
    ('quadrature-binding', 'b253 (derived from the owners lines, shown not asserted)',
     '### **THE RE-BOUND REALIZATION: `T.value := A + E2 - Delta_-`**, `A` being '
     '`b38_act10.left_side` one-axis integral in which NO mode index appears. ### DERIVED: '
     'from `b36_act8.py:184` `resid47 = Tr_full - (A + E2)`, i.e. (i) `Tr_full = A + E2 + '
     'resid47`; with the ruled binding (ii) `T.value := Tr_full + E2 - Delta_-`, substituting '
     'construction for construction gives (iii) `T.value := A + E2 - Delta_-`. ### The '
     'combination is UNCHANGED; only which construction realizes the archimedean trace moved',
     '### ### **AND THE COST DISCLOSED IN THE EXECUTOR OWN VOICE, WHICH THE FERRY DISCLOSURE '
     'DID NOT NAME: `T.value^OLD - T.value^NEW = E2 + resid47` -- THE RE-BINDING REMOVES '
     '`resid47` *AND ONE `E2` TERM*, because the old assembly carried `E2` TWICE (once in the '
     'combination, once inside `Tr_full` comparison against `A + E2`).** ### The ferry '
     'disclosed consequence named `resid47` alone (~61-70% of the measured shortfall per b251 '
     'table, itself a PARTIAL SUM AT N = 11). ### **THE REGISTRATION BANKED THE DUTY TO CHECK '
     'THIS *BEFORE* THE RE-BINDING WAS WRITTEN, SO FINDING IT COULD NOT LOOK LIKE A '
     'CONCESSION MADE AFTER THE FACT.** ### In shortfall algebra: OLD `L - R = resid47 + '
     '2*E2 - Delta_- + (PR - Theta_q)` (exactly b251 measured decomposition); NEW `L - R = '
     'E2 - Delta_- + (PR - Theta_q)`. ### **THE SIZE OF THE REMAINDER IS NOT COMPUTED: THAT '
     'IS A FACE-OFF AND b253 RAN NONE. ### IT IS b254 WORK.**',
     'data/b253_m2inf_ruling.txt; data/b253_filings.txt; '
     'Interfaces/FiniteInstanceIdentity.lean'),
    ('fourth-face-off', 'b254 (bench computation under the re-bound realization)',
     'the identity measured at six cells as the TWO-TERM balance its algebra now is: '
     'L := (A + E2 - Delta_-) + (-Theta_q), R := A - PR, so L - R = (E2 - Delta_-) + '
     '(PR - Theta_q) -- the `A` cancelling identically. ### **THAT COMPOSITION IS '
     'ALGEBRAIC-RESTATEMENT AND WAS LABELLED SO IN THE HASH-GATED MEANINGS FILE BEFORE THE '
     'RUN; the evidence is the SIZES, SIGNS and CELL-PROFILES only.** ### Every term also '
     'tabulated alone; G-INDEP structural; G-STAB at b38 TRIPLE plus one refinement NQ=1100',
     '### **BRANCH (IMBALANCED), AT EVERY CELL, UNDER *BOTH* Delta_- REALIZATIONS.** '
     '### Under (A), the odd eps-MASK (the ruling rider names it): residual -1.001814 to '
     '-0.800154, beyond bars by FOURTEEN ORDERS. ### Under (B), the odd TRACE modes '
     '(b36_act8.py:172, quotable only as Dneg(N = 11, float64 modes, suspect above n = 6)): '
     'residual -0.061581 to -0.533354, beyond bars by 1.50x to 31x -- **and the 1.50x at '
     'a^2 = 2 is reported as marginal rather than rounded away.** ### **SIGN UNIFORMLY '
     'NEGATIVE: SIX CELLS, TWO REALIZATIONS, TWELVE ENTRIES, ONE SIGN.** ### **NEITHER '
     'PROFILE IS MONOTONE IN a^2** and the non-monotonicity is reported, not smoothed. '
     '### (MIXED) is EXCLUDED and the a^2 = 2 row is why: PR = Theta_q = 0 identically -- '
     'the primes vanish -- **and the cell is imbalanced anyway.** ### **THIS IS NOT EVIDENCE '
     'AGAINST THE IDENTITY (b15: a finite cell decides NOTHING global) AND NO DEFICIT '
     'LANGUAGE IS USED (R-III governs). ### IT IS EVIDENCE ABOUT THE *REALIZATION*.** '
     '### h2 stands exactly as open as before',
     'data/b254_fourth_face_off.txt; data/b254_run.txt; data/b254_meanings.txt; '
     'reports/2026-08-29-the-fourth-face-off.md'),
    ('the-balance', 'b254 (both Delta_- realizations computed, neither chosen)',
     '`(Delta_- - E2) ?= (PR - Theta_q)` per cell. ### **Delta_- HAS TWO REALIZATIONS AND '
     'b246 EXPLICITLY DECLINED TO CHOOSE** -- *"Its two realizations remain two objects and '
     'this act computed both rather than choosing"*. ### (A) the odd eps-MASK E2odd '
     '(b37_act9.eps_masked, what sec 17 and File E name); (B) the odd TRACE modes Dneg '
     '(b36_act8.py:172, the only executable assembly -- **and a MODE SUM, hence the object Q1 '
     'demoted**). ### b254 computed BOTH and chose NEITHER, on b246 own precedent',
     '### **THE ALGEBRAIC REDUCTION, DERIVED BEFORE THE RUN: under (A), Delta_- - E2 = '
     'E2odd - (E2even + E2odd) = -E2even, so the balance IS `E2even ?= Theta_q - PR`.** '
     '### At a^2 = 2 that is `E2even ?= 0`, and E2even = 1.001814 is a sum of eps sectors -- '
     '**the cell cannot balance under (A) unless E2even vanishes, and it does not.** '
     '### **A STRUCTURAL FINDING THE BAR COLUMN MADE VISIBLE: under (A) NOTHING IN THE '
     'BALANCE IS A MODE SUM** -- E2even, E2odd, PR and Theta_q are all fixed at the eps and '
     'carto axes and do not move with NQ at all, so (A) bar is the eps mask certificate '
     '(8.882e-16) alone, **and Q1 demotion and b252 divergence are entirely irrelevant to '
     'it -- a stronger reason than the rider own.** ### Under (B) the balance DOES carry a '
     'mode sum, and with it b252 suspicion and b253 QUOTED-N law. ### **THE TWO '
     'REALIZATIONS DISAGREE MATERIALLY (16.3x at a^2 = 2) AND AGREE ON THE VERDICT** -- so '
     'the registered condition that would have made the disagreement the act REAL FINDING '
     'DID NOT FIRE, and it is not claimed. ### **AND ONE OF THIS ACT OWN THREE CHARGES '
     'AGAINST THE RIDER CITATION WAS WITHDRAWN: b246 contains BOTH "by mode 7" and '
     '"CONVERGED BY MODE 6", in two sentences about two quantities. ### THE HARNESS CAUGHT '
     'IT BY REFUSING A GATE WHOSE MUST-FAIL FIXTURE PASSED, AND THE HASH-GATED MEANINGS FILE '
     'WAS *NOT* EDITED (b244/b246 precedent) -- THE GATE WAS FIXED AND THE ERROR DISCLOSED.**',
     'data/b254_fourth_face_off.txt; data/b254_run.txt; data/b246_two_tails.txt'),
    ('limit-profile', 'b255 (bounded bench act; the ladder priced before it was fixed)',
     'the balance measured along the cutoff axis over SIXTEEN cells, a^2 = 2 to 100. '
     '### **THE PRICING RAN FIRST AND KEPT NO BALANCE VALUE**, so the ladder was chosen by '
     'AFFORDABILITY and the order on disk makes that checkable. ### Four cost walls measured: '
     '**(W1) the eps rho-grid ended at a^2 = 12.001 AND FAILED SILENTLY** -- np.interp clamps '
     'rather than raising, so every cell past 12 would have carried a wrong E2 with no error; '
     'rebuilt to rho_max 100.001, EPS_NRHO 240 -> 445. **(W2) Theta_q scaling_matrix is dense '
     'N = p^(2n): a^2 = 100 -> N = 4096, ~22 s; a^2 = 128 -> N = 16384, 2.1 GB, >= 1690 s for '
     'p = 2 alone -- REFUSED ON COST, recorded before any value existed.**',
     '### **BRANCH (MIXED), AND THE SPLIT IS THE FINDING: |resid(A)| ALTERNATES GROW/SHRINK UP '
     'TO a^2 = 20, THEN EIGHT CONSECUTIVE SHRINKS TO a^2 = 100** (1.001813 down to 0.486920, '
     'more than halving). ### **(RELAXES) IS NOT TAKEN: the banked rule forbids reading an '
     'oscillating stretch as a relaxation with an excuse.** ### **THE STRUCTURAL FINDING: THE '
     'JUNCTION (PR - Theta_q) IS A SAWTOOTH LOCKED TO b17 STAIRCASE.** ### Between staircase '
     'steps it RISES -- six transitions, six rises, no exceptions; at steps it FALLS at six of '
     'nine, and on the upper ladder (a^2 >= 20) at ALL FOUR steps while rising at ALL FIVE '
     'non-steps. ### Mechanism read off the columns: PR rises smoothly toward 1 while Theta_q '
     'rises in JUMPS, gaining a level at each step. ### E2even by contrast FALLS MONOTONICALLY '
     'at all sixteen cells. ### **NO SIGN-EVENT, AND THE REASON IS STRUCTURAL: resid = '
     '-(E2even + junction) with BOTH terms positive at every cell, and a sum of two positives '
     'cannot cross zero.** ### **THE EXECUTOR REGISTERED (RELAXES) ON THE LOWER LADDER AND '
     'DECLINED THE UPPER -- THAT IS THE REVERSE OF WHAT HAPPENED, and the falsifier was too '
     'coarse to catch it; both reported.** ### G-REPRO debt of the grid rebuild REGISTERED '
     'BEFORE IT WAS PAID and PAID: worst deviation 5.64e-06 against b254 six cells, inside the '
     '1e-4 band by 18x; b254 NOT re-verdicted. ### **NO FIT, NO SLOPE, NO EXTRAPOLATED LIMIT '
     'IS BANKED (b242 governs). ### THE WORD LIMIT IS IN THE TITLE AND IN NONE OF THE '
     'CONCLUSIONS.** ### Cell-species said: S4 = (2,3,5) is FIXED, so 7 never enters -- the '
     'ladder measures powers of a fixed prime set, not a growing place set',
     'data/b255_limit_profile.txt; data/b255_run.txt; data/b255_pricing.txt; '
     'data/b255_meanings.txt; reports/2026-08-29-the-limit-profile.md'),
    ('contribution-map', 'b256 (reads + one document at support-voice)',
     'the whole research position stated at grade in ONE document, placed at '
     'PLACE-papers/phase1.5/method/CONTRIBUTION_MAP_2026-08.md. ### CLASS LINE: TIER N * '
     'PRIVATE * PATENT-SESSION INPUT * **STATES GRADES, CONFERS NONE**. ### 18 rows, each '
     'carrying grade-today + owner + AIM + h2-dependency + filing touched + figure '
     'candidates; plus the fold-forward ledger b234-b255 with **every obstacle QUOTED from '
     'its owning act** (22 acts, 22 reports, count reconciled); plus two annexes',
     '### **NO GRADE MOVED.** ### h2-dependency: 13 NO, 5 YES (adjacent), and **EVERY '
     'PATENT-FACING ROW IS NO** -- verified by reading the claim-backing table FIRST (its ten '
     'rows are QEC / Fano-Steane / Epstein / spinor / cross-exclusion terminals, none '
     'touching the RH identity). ### **THE YES ROWS ARE MARKED *ADJACENT*: they are the rows '
     'h2 would BEAR ON if it moved, not rows that assume it -- a blanket sentence would have '
     'hidden that and a column shows it.** ### Counts RE-COUNTED from the filesystem: **44 '
     'built** (11+13+7+6+4+3) and **REVIEW_SET_2026-08 = 31**, both matching the session '
     'header exactly; the bare find count of 82 files / 51 unique basenames is reconciled as '
     'STAGING COPIES, not a divergence. ### **AND THE ONE ITEM THE ACT COULD NOT DELIVER, AT '
     'FULL PROMINENCE: SIGNEDNESS (S.I.D.E+S) WAS TO BE *QUOTED* AND IS NOT IN THIS SEAT '
     'REACH OR IN THE CORPUS -- zero occurrences across relay/ and all of PLACE-papers/. ### '
     'RECORDED AS A NAMED SLOT WITH OWNER AND ROUTE, QUOTATION MARKED OWED, NOT PARAPHRASED '
     'AND NOT INVENTED.** ### J1 recorded PARKED-BY-AUTHOR (save); J2 UNPROMOTED CANDIDATE; '
     'no annex-A candidate marked Priority-A. ### **AND A LIVE b148 CONDITION FOUND AND '
     'REPORTED: SEVEN PATENT-SEAT FIGURE DIRECTORIES SIT UNTRACKED IN THE SHARED WORKTREE, '
     'DATED 2026-08-24, HOLDING THE 44 FIGURES AND THE SIX BATCH RECORDS** -- not this act '
     'doing (verified by mtime), not staged by it (place_add.py used), and reported rather '
     'than resolved. ### Hook exercised: CLEAN, 0 foreign hits. ### Mirror rebuilt and '
     'verified CLEAN on all three clauses (40 files, HEAD 2bcdff5 vs ls-remote). ### '
     '**STANDING PRACTICE INSTITUTED: every profile act bank ends with a chart-ready CSV '
     'block of all columns** -- applied retrospectively to b255',
     'PLACE-papers/phase1.5/method/CONTRIBUTION_MAP_2026-08.md; '
     'data/b256_contribution_map.txt; data/b256_b255_profile.csv; '
     'reports/2026-08-29-the-contribution-map.md'),
    ('rule-modes', 'b250 (AMENDING b244/b245; the earlier rows STAND)',
     '### **THE K1 BAR TAIL TERM IS NO LONGER UNBOUNDED.** ### The rows above record that a '
     'bar written per RULE MODES K1 carries an UNBOUNDED term and that b245 must say so in '
     'its own words. ### **THOSE ROWS ARE NOT REWRITTEN AND WERE TRUE WHEN WRITTEN** '
     '(b244 precedent: a second row, not an edit)',
     'b250 S4 bounds the tail: sum_{n>N} t(n) <= (2 - S_N)/(1 - beta_N), and at K1 cut '
     'N = 6 the bound is **1.158e-14 on ZERO SPECIFIC IMPORTS** against a measured tail of '
     '1.116e-14 -- ### **TIGHT TO ABOUT 4%, NOT LOOSE BY ORDERS** (contrast S2 bounds, which '
     'are loose by many orders and are printed that way). ### **AND bar_L AMBER DOES NOT '
     'CLEAR: it was amber for TWO reasons and only ONE is paid.** The bar still reports SEVEN '
     'computable modes against a definition of ELEVEN, a bench-precision fact b249 measured '
     'and b250 did NOT remove. ### AMENDED WHEREVER THE RECORD CARRIES IT (three reports), '
     'ORIGINALS INTACT -- and the W-UNION (nonArchimedean, unbounded) QUADRANT is a '
     '**DIFFERENT OBJECT** and was deliberately NOT amended',
     'data/b250_m4_derivation.txt; reports/2026-08-28-first-face-off.md; '
     'reports/2026-08-29-the-serializing-close.md; reports/2026-08-29-the-second-face-off.md'),
    ('second-object', 'b248 (arrangement + split) / b246 (two objects established)',
     'the second term of the bench shortfall, restated as TWO NAMED PIECES WITH SEPARATE OWNERS: '
     'the ARCHIMEDEAN PIECE (E2full + E2even), sector arithmetic on a CONVERGED series, 88%-100%; '
     'and the JUNCTION PIECE (PR - Theta_q), the finite-place pairing, 0%-12%',
     '### NEITHER PIECE IS M-4. ### **M-4 COVERS resid47 AND NOTHING ELSE** (b246 verdict, '
     'unrevised by b248). ### THE ARRANGEMENT IS (ADDITIVE-FORCED) so the composition is '
     'unchanged from b245/b246. ### **THE TWO NATURES DO NOT SEPARATE AS CLEANLY AS HOPED**: the '
     'archimedean piece is smooth and dominant, but the junction piece is NOT monotone in the '
     'active-prime count, and the mixing is now on the record with its own per-cell table',
     'data/b248_second_object.txt; data/b248_split_run.txt'),
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
