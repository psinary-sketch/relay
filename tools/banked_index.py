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
    'cost-census': ['the cost census', 'cost census', 'the cost column', 'the typed cost column', 'what moving it one grade would take',
                    'what would it cost to move a face', 'the sorted view', 'the pole-constant relation', 'the pole-constant row', 'row L2',
                    'the phase rule refined', '45 to 135 degrees', 'the addendum to b328'],
    'ferry-standing': ['the standing clauses', 'ferry standing', 'FERRY_STANDING', 'the standing file', 'where are the standing clauses',
                       'the STOP format', 'the stop format', 'the draft ferry', 'DRAFT -- NAVIGATOR EDITS', 'the citation check',
                       'a stale citation', 'what is the STOP format', 'Rule 6'],
    'aim-map': ['the aim-map', 'aim map', 'the aim map', 'the room the arithmetic leaves', 'the chart', 'the chart over aims',
                'the narrowest points', 'the crossing region over aims', 'the softest pair over aims', 'K5 and K6 over aims',
                'soften together', 'what does the aim-map say', 'the reaching leg', 'the covered leg'],
    'archimedean-term-derived': ['the archimedean term derived', 'archimedean term derived', 'the archimedean term',
                                 'the digamma kernel', 'the classical term', 'the principal value', 'the third route',
                                 'the re-rank', 'the factor of two', 'the Gamma factor', 'is the archimedean term derived',
                                 'the new softest constituent', 'the mismatch diagnosed'],
    'clause-stated': ['the clause stated', 'clause stated', 'the open clause', 'the statement of the clause',
                      'the positivity face', 'the fourth register realized', 'the E0 gate', 'the softest constituent',
                      'the lawful class', 'the archimedean distribution', 'the compressed square', 'the aim-map',
                      'what is the open clause', 'the constituents ranked'],
    'discriminating-arc-fold': ['the discriminating arc fold', 'the discriminating-family arc', 'b323-b330',
                                'the eight acts', 'fold b323', 'the negative-control arc', 'what did the arc establish',
                                'the arc as one statement', 'the desk', 'the instrument can say no',
                                'the reconciliation wave', 'the patent receipts'],
    'techne-extraction': ['techne extraction', 'the techne extraction', 'the september extraction', 'techne modules',
                          'the method modules', 'claim-shaped modules', 'the module families', 'modules/2026-09',
                          'the patent note', 'line-ending hygiene', 'the vacuity taxonomy', 'the negative-control protocol'],
    'finite-side-seal': ['finite-side seal', 'the finite-side seal', 'finite side seal', 'the finite-side sealing module',
                         'FiniteSideSeal', 'the exhaustiveness theorem', 'the unit decomposition', 'the scaling shift inverse',
                         'general and per-cell', 'the axiom finding', 'the compact part per cell', 'the scaling part general'],
    'discriminating-family': ['discriminating family', 'the discriminating family', 'the phase condition',
                              'the four-term sum', 'the off-line quadruple', 'the sine-aimed seed',
                              'the odd seed', 'the quadruple sum', 'forty-five degrees', 'the phase threshold',
                              'the negative control under the family', 'sees it'],
    'faces-ledger': ['faces ledger', 'the faces ledger', 'the faces', 'the ledger of faces',
                     'the register pentagon', 'the pentagon', 'the five faces', 'the cascades',
                     'the owed bridges', 'the fixed-point silence', 'the sonin margin', 'the li margin'],
    'li-weil-bridge': ['li-weil bridge', 'the li-weil bridge', 'the li-to-weil bridge', 'the bridge read',
                       'the li coefficients as the weil functional', 'the archimedean channel',
                       'the pole constant', 'one distribution on two families', 'the li test function',
                       'the li family'],
    'the-reach': ['the reach', 'the crossing region', 'both windows extended',
                  'the closure for both', 'the halved kernel', 'the missing half',
                  'the withdrawn crossing', 'a test this family cannot fail',
                  'the aimed family'],
    'epstein-zeros': ['epstein zeros', 'the epstein zeros', 'the on-line epstein zeros',
                      'the completeness census', 'the off-line zeros located',
                      'the epstein library', 'zeros on the line'],
    'negative-control': ['the negative control', 'a failing hypothesis',
                         'does the instrument see a failing hypothesis',
                         'the priced reach', 'the positive control',
                         'the inherited constant', 'what the zeta window was',
                         'can the instrument say no'],
    'epstein': ['epstein', 'the epstein case', 'the epstein zeta',
                'the confinement keystone', 'the class-number-3 form', 'disc -23',
                'the off-line zeros', 'the on-line zero library'],
    'keystones-reread': ['the keystones reread', 'the wall', 'the margin',
                        'did the arc move the wall', 'the two margins',
                        'is the arc space the wall space', 'the bridging statement',
                        'what did the deposit already say'],
    'archimedean-arc-fold': ['the archimedean arc fold', 'b314-b322',
                             'the instrument arc', 'the nine acts',
                             'the defective bars', 'sealed bars found defective',
                             'what did the arc establish'],
    'membership': ['the membership', 'the residual ladder', 'the two realizations',
                   'why is the residual not zero', 'is the unit in the space',
                   'the truncation tail'],
    'resolving-power': ['the resolving power', 'under-resolved',
                        'what would settle it', 'the price of a question',
                        'is it open or under-resolved'],
    'identity-control': ['the identity control', 'theorem four seven',
                        'the remainder integral', 'did the equality hold',
                        'is the exponent settled'],
    'window-opened': ['window opened', 'the places sum', 'the criterion',
                      'did the balance come out negative', 'the prime sum sign',
                      'the explicit formula control'],
    'lawful-function': ['the lawful function', 'the square of the seed',
                        'is the corpus window a g or an f', 'the sonin class membership test',
                        'which cells does theorem one cover'],
    'source-control': ['the source control', 'both sides of the inequality',
                       'the archimedean weil distribution', 'the nonempty reach',
                       'the control that failed first', 'did the control hold'],
    'stable-rank': ['the stable rank', 'why did the rank step',
                   'the eigenvalue one subspace', 'the rank stable subspace',
                   'does the dimension hold still', 'the kernel coverage repair'],
    'forced-sign': ['the forced sign', 'the square form',
                   'is the smear the source trace side', 'is the variant positive definite',
                   'which letter is the corpus window',
                   'why did the mean-zero column change sign'],
    'trace-on-the-object': ['the trace on the space', 'the compressed smeared trace',
                   'is the corpus window in the source class', 'the mean-zero column',
                   'was the prediction small', 'the trace on the object'],
    'archimedean-instrument': ['the truncated space', 'is u_inf in the space',
                   'does the scaling restrict', 'sonin space instrument',
                   'the archimedean instrument', 'which condition breaks'],
    'calibration': ['what the calibration fixes', 'is A independently defined',
                   'the E2 in the bracket', 'the sign only'],
    'rate-corrected': ['the even sector under the source convention',
                   'the envelope becomes a constant', 'the cutoff order',
                   'the rate re-derived'],
    'the-instrument-arc': ['the seven acts', 'b307 to b313',
                    'the arc as one statement', 'the convention erratum'],
    'the-cold-clone': ['the kernel rebuilt from a clone', 'the certification test',
                    'uncertified terminals', 'the coverage answer'],
    'the-exponent': ['the flip', 'the remainder under the source normalization',
                    'did the residue collapse', 'the exponent check'],
    'convention-share-of-the-residue': ['what the convention accounts for',
                    'the decay under the flip', 'the one-power shift'],
    'the-remainder': ['the corpus eps against the source', 'the scaling convention',
                     'the remainder identified', 'is the remainder theirs'],
    'remainder-check-at-a-zero': ['why the cross-check passed',
                     'a check at a zero', 'the invisible factor'],
    'identity-neighbourhood': ['the trace remainder', 'the local weight',
                              'where the content sits', 'the source proof read'],
    'arch-mechanism-untyped': ['trace class', 'the count and the jacobian',
                              'does not type', 'the archimedean instrument price'],
    'smear-collapse': ['the smear', 'the identity term', 'the assembled smear',
                      'the source construction at a finite place'],
    'fixed-point-silence': ['the fixed-point sentence', 'the signed count',
                           'the finite side closure', 'off-ball fixed points'],
    'scaling-trace': ['the scaling trace', 'the compressed trace', 'the smeared trace',
                     'the trace of the scaling action'],
    'no-offball-fixed-point': ['the fixed point', 'the mechanism', 'the unit argument',
                              'p^j minus one'],
    'local-field-instrument': ['the local field', 'untied radii', 'the two radii',
                              'the scaling part', 'the instrument build', 'the frame'],
    'escaped-mass-artifact': ['escaped mass', 'the artifact', 'the fold count',
                             'nothing to fold'],
    'the-fold': ['the adelic arc', 'the adelic fold', 'the arc statement',
                'the b297-b306 fold', 'the lore', 'the instrument suite', 'the desk'],
    'handoff-census': ['the ledger census', 'the handoff census',
                      'what is missing from the ledger', 'the conditional strike'],
    'the-difference': ['the difference', 'the corpus difference',
                      'the imbalance', 'the cell-level imbalance',
                      'the fourth face-off difference'],
    'sweep-scope': ['the sweep scope', 'the shared-target sweep',
                   'the correspondence sweep', 'the stem sweep scope'],
    'arithmetics-entry': ['where the arithmetic enters', 'the arithmetic entry',
                         'the weil distribution', 'the local weil distribution',
                         'the explicit formula'],
    'prime-sum-is-weil': ['the prime sum', 'the adopted prime sum',
                         'the corpus prime side', 'PR summand'],
    'instrument-q-p': ['the instrument', 'the priced instrument',
                      'the q_p instrument', 'the scaling instrument'],
    'demands-shape': ['the demand shape', "the demand's shape",
                     'the per-index demand', 'per-index demand',
                     'termwise agreement', 'the first-level demand'],
    'phi-mu-l2': ['phi mu in l2', 'the archimedean unit membership',
                 'square-integrability of the archimedean unit',
                 'the fourth condition'],
    'smearing-compression': ['the smearing compression', 'smearing over the group',
                            'the finite scaling trace', 'the sonin trace',
                            'the finite analogue of the source move'],
    'uniform-family': ['the uniform family', 'the two-radius family',
                      'the family across places', 'the uniform form',
                      'the archimedean family', 'a pair of radii at every place'],
    'vn-definition-331': ['definition 3.3.1', 'the c0-sequence definition',
                         'the convergent unit sequence', 'von neumann definition 3.3.1'],
    'object-conditions': ['the object conditions', 'object conditions',
                         "the object's standing conditions",
                         'the construction status'],
    'unit-requirement': ['the unit requirement', 'rule arch-unit', 'arch-unit',
                        'space membership suffices', 'what the product asks of a vector'],
    'generator-nonvanishing': ['the generator nonvanishing', 'the canonical generator',
                              'the generic odd place', 'support of u_p',
                              'b226 owed step'],
    'object-completed': ['the object completed', 'the incomplete direct product',
                        'the stated choice across places', 'the constituents table',
                        'the c0 condition', 'term 3 object'],
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
    # ### THE COST CENSUS (b336, leg 1 of the sortie b335-b338).
    ("cost-census", "b336 (a census on the faces ledger, typed; no grade moved)",
     "THE COST CENSUS: for each of the faces ledger's rows, what moving it ONE grade would take, typed as READ / IMPORT / MEASUREMENT /"
     " DERIVATION / CONSTRUCTION (cheapest kind first) with the record's price quoted at its emitter where the record prices the step -- 15 rows"
     " typed, the rows the record prices F1, F2, F7, S1 (the unit's domain factor 3.104e+02 at b322; the exponent's ratio, a twenty-fourth to a fifth, at b321;"
     " the instrument's six acts at b321_run; the crossing widths at b328 and b334), every other row 'no price in the record'; filed as an append-only"
     " block keyed to the row ids through the writer, the sorted view at relay data/b336_cost_sorted.txt. ROW L2, the pole-constant relation between the"
     " Li and positivity faces: the deposit's archimedean channel on the Li family is the archimedean distribution plus the pole constant 1, the two"
     " margins two evaluations of one distribution and not one functional (FINDINGS), separated by the pole constant (b331) -- STATED, cost zero. THE ADDENDUM TO b328's BLOCK: the quadruple's term"
     " 4 |G|^2 cos 2 phi is negative only between 45 and 135 degrees, b334's chart sign column cited.",
     "### NO GRADE MOVED; every existing row byte-identical. ### A COST IS NOT A GRADE, NOT A PLAN, NOT A PREDICTION. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b336_the_cost_census.txt; data/b336_cost_run.txt; data/b336_cost_sorted.txt; data/b336_registration_2026-09-06.txt (sealed before any write);"
     " FACES_LEDGER.md (the b336 cost census block; row L2; the b336 addendum to b328); CORRESPONDENCE.md row 183"),
    # ### THE STANDING CLAUSES, FILED (b335, leg 0 of the sortie b335-b338).
    ("ferry-standing", "b335 (filings only: a standing-clauses file, a scanner check by order, a rule of the executor's format)",
     "THE STANDING CLAUSES OF THE RESEARCH SEAT'S FERRIES, in relay/tools/FERRY_STANDING.md VERSION 1: generated from the 15 banked ferries"
     " b320-b334, 37 clauses measured, 33 STANDING (carried by 8 or more of 15), 4 FREQUENT, NOT STANDING, each with its count and"
     " carriers, the wording b334's ferry's; cited by a ferry as FERRY_STANDING v1. THE FERRY SCAN (tools/ferry_scan.py) checks the citation"
     " against the file's VERSION line and reports NONE / CURRENT / STALE / NO FILE, a STALE citation a hit (exit 1), fixtures of both"
     " polarities built from the loaded version. RULE 6, THE STOP FORMAT (PLACE-papers/protocols/EXECUTOR_RULES.md, appended): the executor's"
     " final message carries the closing summary, the pins, then a block headed DRAFT -- NAVIGATOR EDITS with a draft of the next ferry.",
     "### THE FILE BINDS NOTHING BY ITSELF; A FERRY THAT CITES IT CARRIES ITS CLAUSES BY REFERENCE. ### THE DRAFT BINDS NOTHING: the next act runs"
     " only on the navigator's paste. ### NO GRADE, NO CLAIM, NO TERMINAL. ### M-2 UNCHANGED",
     "tools/FERRY_STANDING.md; data/b335_the_standing_clauses.txt; data/b335_standing_run.txt; data/b335_scan_selftest.txt; data/b335_scan_cite_stale.txt;"
     " data/b335_rule6_run.txt; data/b335_registration_2026-09-06.txt (sealed before any write); PLACE-papers protocols/EXECUTOR_RULES.md Rule 6;"
     " CORRESPONDENCE.md row 182"),
    # ### THE AIM-MAP (b334).
    ("aim-map", "b334 (a computation on the certified instruments; a finite-reach chart over aims; interpreted by nobody)",
     "THE ROOM THE ARITHMETIC LEAVES, CHARTED OVER AIMS: b328's sine-aimed even seed at every height of the sealed grid, for zeta and for the"
     " Epstein function side by side, at the reaching widths a = 40, 81 (the phase past 45 degrees at every off-line aim) and the covered widths"
     " a = 1.3, 1.41 (where the square on the stable cut and the remainder are instruments the record certifies). Per aim, like for like by name:"
     " the archimedean distribution by the derived kernel on two transforms and by the principal-value witness (150); the square at two frames;"
     " the margin as A_z - Tr and as minus the remainder by two quadratures, the identity residual printed; the prime sum by two routes; the"
     " places side gated. THE NARROWEST POINTS: covered_1.3 at gamma 20.000000; covered_1.41 at gamma 33.650101; reaching_40 at gamma 4.000000; reaching_81 at gamma 4.000000. THE CROSSING REGION for Z_Q: a = 40 at gamma 16.290216; a = 81 at gamma 16.290216; a = 81 at gamma 46.960994. (F1) the prime sum inside the margin"
     " at every aim at this reach: MET -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE. (F2) the crossing region contains the banked"
     " off-line zeros' aims: NOT MET -- THE NEGATIVE CONTROL CHARTED. (F3) K5 and K6 soften together over aims: NOT MET (Spearman -0.6158).",
     "### A CHART IS NOT A PROOF. ### THE QUANTIFIER K8 STAYS UNOWNED. ### NO GRADE: THE SOFTEST PAIR GAINS A BEHAVIOUR OVER AIMS, FILED AS THE"
     " CLAUSE'S FIRST CHART. ### Signs certified by the gate; sizes at named resolutions. ### The cost census named as next. ### NO TERMINAL."
     " ### M-2 UNCHANGED",
     "data/b334_the_aim_map.txt; data/b334_chart_run.txt; data/b334_grid_run.txt; data/b334_leg_reaching_40_run.txt; data/b334_leg_reaching_81_run.txt;"
     " data/b334_leg_covered_run.txt; data/b334_registration_2026-09-06.txt (sealed before any seed); FACES_LEDGER.md (the b334 update: S1 / K5, K6;"
     " F7; b328's block); CORRESPONDENCE.md rows 180 and 181"),
    # ### THE ARCHIMEDEAN TERM DERIVED (b333).
    ("archimedean-term-derived", "b333 (a derivation under the import bar; a third route; the re-rank; a sealed bar not met, diagnosed)",
     "THE DERIVATION TOOL'S VERDICT, AS PRINTED, FIRST: MISMATCH at (L3): the corpus's A against the source's (152) as evaluated here. ### Diagnosed: the act's sealed bar paired the third"
     " route, run on the atlas's bump, with b320's table, which b320 computed for its own function autocorrelation(mean_zero_variant(a));"
     " THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED -- the third route ((150) on the real side, mpmath, no corpus code) agrees with the"
     " atlas's own banked channel for the bump at all thirteen cells (worst 1.864e-06) and with b320's two routes applied to the"
     " bump (worst 6.521e-08 / 6.061e-07); (150) on b320's own function agrees with b320's table (worst 6.957e-06 / 2.738e-05)."
     " The sealed bar, as sealed, NOT MET and not rewritten. ### THE CHAIN, its own verdict DERIVES-ON-IMPORT: the stated clause's constituent K5,"
     " the archimedean distribution, derived from the classical term as the pinned source states it (Appendix B: (150) the principal value,"
     " (151) the Gamma factor with its power of pi and its logarithmic derivative against the transform, (152)-(153) the digamma kernel,"
     " W_inf = -W_R) under the corpus's conventions to the atlas's A = (1/2pi) INT hhat [Re psi(1/4 + iu/2) - log pi] du: THE CORPUS'S A IS"
     " THE SOURCE'S W_inf = -W_R, entering (148) as pole + W_inf - PRIME; the factor-of-two hazard of b325 checked from one identity."
     " ### The re-rank under b332's sealed rule: K5 (MEASURED-AT-COVERED-CELLS), K6 (MEASURED-AT-COVERED-CELLS), K1 (MEASURED-ON-FAMILIES), K2 (MEASURED-ON-FAMILIES), K7 (UNDER-RESOLVED-AT-BENCH), K3 (DERIVED-ON-CONTENT), K4 (DERIVED-ON-CONTENT) -- the new softest: K5 and K6",
     "### NO GRADE CONFERRED BEYOND THE DERIVATION'S OWN: DERIVES-ON-IMPORTS, the imports named; MEASURED-ON-FAMILIES NOT CONFERRED (the sealed"
     " bar not met). ### ROUTES AGREEING CERTIFY THAT THE ROUTES AGREE, NOT THE SIZE OF THE TERM. ### THE CLAUSE HAS NOT MOVED; K8 STAYS"
     " UNOWNED. ### The aim-map named as next, its target the new softest; neither it nor this act is the discharge. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b333_the_archimedean_term_derived.txt; data/b333_derive_run.txt; data/b333_diagnose_run.txt; data/b333_rerank_run.txt; data/b333_source.txt;"
     " data/b333_registration_2026-09-06.txt (sealed before any value); FINDINGS.md (the b333 addendum after"
     " clause-stated); FACES_LEDGER.md (the b333 update, row S1 / K5); CORRESPONDENCE.md row 179"),
    # ### THE CLAUSE STATED (b332).
    ("clause-stated", "b332 (a statement act; no proof attempted)",
     "(S) for every g in the source's class (Definition 3.1 with Proposition C.1's vanishing set; b328's seeds inside"
     " it) the places sum of the explicit formula keeps the criterion's sign, SUM_v W_v(g conv g-bar^#) <= 0 -- the"
     " positivity face's realized form, the deposit's refusal to compile the cross-register equivalences quoted"
     " beside it. The places sum unfolded: the finite places' contribution (b310/b329), the prime sum (b306), the"
     " archimedean distribution with its digamma witness (b315/b320), the compressed square plus the remainder that"
     " is the margin (b318/b320/b321). THE E0 GATE HALTS AT K8, the quantifiers, UNOWNED. THE RANKING under the"
     " sealed rule, softest first: K5 (DEFINED-ONLY), K6 (MEASURED-AT-COVERED-CELLS), K1 (MEASURED-ON-FAMILIES), K2 (MEASURED-ON-FAMILIES), K7 (UNDER-RESOLVED-AT-BENCH), K3 (DERIVED-ON-CONTENT), K4 (DERIVED-ON-CONTENT)",
     "### NOT DISCHARGED, NOT WEAKENED, NOT REPLACED; ONE FACE AND NOT THE COMPILED EQUIVALENCE. ### Every grade its"
     " owner's, none conferred. ### The navigator's registered expectation (the remainder softest): NOT MET --"
     " the softest rank is K5, the archimedean distribution. ### The aim-map named as next, for the softest constituent;"
     " neither it nor this act is the discharge. ### NO TERMINAL: analysis over an infinite class. ### M-2 UNCHANGED",
     "D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (anchor clause-stated); FACES_LEDGER.md row S1; the arc keystone's appended"
     " line; data/b332_the_clause_stated.txt; data/b332_statement_rows.json; data/b332_registration_2026-09-06.txt"
     " (sealed before any write); CORRESPONDENCE.md row 178"),
    # ### THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD (b331).
    ("discriminating-arc-fold", "b331 (a filings act)",
     "FINDINGS.md gains the section 'THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD', +144 lines"
     " (2880 -> 3024): the eight acts each with its grade as its own act left it, its own quotation, its scope and its"
     " obstacle quoted; the corrections table; the sealed-bars-found-defective table continued; the seats' declared"
     " defects as their own table; the lore with a TECHNE module beside each mechanized rule; the suite; the desk."
     " ### F-QUOTE 16 quotations, 0 unfindable, the discrimination arm firing; F-COUNT the arc exactly;"
     " PURELY ADDITIVE measured on the working file and on the blob",
     "### A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER. ### NO GRADE MOVED; NO ACT RE-VERDICTED; NO NEW"
     " MATHEMATICS. ### The judgement that each quoted sentence is its act's own voice is the seat's, declared."
     " ### M-2 UNCHANGED",
     "D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (the section); data/b331_fold_emitted.md; data/b331_fold_run.txt;"
     " data/b331_fold_rows.json; data/b331_the_fold.txt; data/b331_registration_2026-09-06.txt (sealed before any"
     " write); CORRESPONDENCE.md row 176"),
    # ### THE ARC AS ONE STATEMENT, WITH ITS SCOPE (b331).
    ("discriminating-arc-fold", "b331 (the arc's six clauses, each an act's own verdict at its own grade)",
     "the instrument can say no (b325, b326, b328); the zeta window is a passed test for the discriminating family"
     " at this reach, and for the arc's family b326's verdict stands (b328); the finite side is compiled, general"
     " where the header says general and per cell where it says per cell (b329); the two margins are two"
     " evaluations of one distribution separated by the pole constant (b324, b327); the object's archimedean unit"
     " is in its space by derivation and priced at bench (b300, b322, unchanged); THE CLAUSE HAS NOT MOVED and no"
     " act in the arc claims otherwise",
     "### A SUMMARY AND NOT A VERDICT. ### The no is a verdict on one family, one instrument, one reach -- nothing"
     " about the method or about zeta; the compiled finite side certifies the model's arithmetic and the counting"
     " form, not the identification with the source's trace and not the compact part beyond the cells; the"
     " margins' relation is a reading under an import bar with the bridge owed. ### NOTHING ABOUT THE IDENTITY,"
     " h2, OR THE ROSTER. ### M-2 UNCHANGED",
     "D:/MY-DOwnloads/PLACE-papers/FINDINGS.md (the section's 'The arc as one statement' and its scope paragraph);"
     " data/b331_the_fold.txt; CORRESPONDENCE.md row 177"),
    # ### THE TECHNE EXTRACTION -- METHOD ONLY, NOT PUSHED (b330).
    ("techne-extraction", "b330 (filings of method into a private core; a hygiene fix at step zero)",
     "20 claim-shaped method modules under modules/2026-09/ in the canonical local TECHNE clone (WHAT IT DOES,"
     " WHEN IT APPLIES, WHAT IT REFUSES, PROVENANCE pulled from the emitting files), a top-level modules/INDEX.md"
     " mapping each to a family (the August three, or VACUITY / REGISTRATION / READING / CERTIFICATION /"
     " NEGATIVE_CONTROL named once) and cross-referencing the August module it extends or supersedes; the August"
     " files untouched and still untracked; the local commit 75ab3ff NOT PUSHED, the remote tip 22739c9"
     " unchanged, the second clone 6e8638a untouched. ### At step zero: .gitattributes in the kernel repository"
     " (SIDE 3cbe47c), the profile equal to its blob on raw bytes after the re-checkout",
     "### METHOD, NOT A RESULT -- NOTHING ABOUT THE PROGRAMME'S OBJECTS ENTERS TECHNE (research-vocabulary sweep 0"
     " hits). ### NOT PUSHED; TECHNE-Core PRIVATE UNTIL ITS PROVISIONALS ARE FILED. ### The patent note lives in the"
     " bank and makes no legal claim. ### The two-clone divergence read, not resolved. ### NO GRADE MOVED; NO GRADE"
     " CONFERRED. ### M-2 UNCHANGED",
     "D:/MY-DOwnloads/TECHNE-Core/modules/2026-09/ (local); data/b330_the_techne_extraction.txt; data/b330_modules_check_run3.txt;"
     " data/b330_techne_verify.txt; data/b330_eol_after.txt; data/b330_registration_2026-09-06.txt (sealed before any"
     " write); CORRESPONDENCE.md row 175"),
    # ### THE FINITE-SIDE SEAL -- THE MODULE AND ITS TWO SCOPES (b329).
    ("finite-side-seal", "b329 (a kernel build of banked derivations)",
     "Core/FiniteSideSeal.lean (B329), vanilla Lean, no imports, no native_decide, no sorry: GENERAL over every"
     " base p >= 2, level, power and index -- the decomposition of a nonzero index as a non-multiple of p times a"
     " power of p with the exponent below the level (existence, uniqueness), the action factoring through the two"
     " parts, p^j - 1 invertible modulo every p^m with the inverse exhibited, the fixed-point congruence forcing"
     " the index into the ball in either congruence (b309's law, compiled). PER CELL, decided over the seven banked"
     " cells and no other -- the compressed smear over the units vanishes (b304's zero in b310's signed-count"
     " form), the not-dead witness, b304's refusal, the polarity controls. ONE exhaustiveness theorem whose"
     " hypotheses name which is which. ### The profile 566 -> 590 prints, all zero-axiom, the banked"
     " profile a true byte prefix",
     "### GENERAL FOR THE SCALING PART, PER CELL FOR THE COMPACT PART -- STATED IN THE MODULE HEADER AND NEVER"
     " AVERAGED. ### Faces ledger F5: PROVED-GENERAL (scaling) / PROVED-AT-CELLS (compact). ### What is compiled"
     " is the model's arithmetic and the counting form of the trace; the identification with the source's trace"
     " is b310's derivation, uncompiled. ### NOTHING ABOUT THE ARCHIMEDEAN PLACE. ### NO GRADE MOVED. ### M-2"
     " UNCHANGED",
     "D:/SIDE-global-section/Core/FiniteSideSeal.lean; AXIOM_PRINTS.txt (B329.*); data/b329_kernel_run.txt;"
     " data/b329_the_finite_side_seal.txt; data/b329_registration_2026-09-05.txt (sealed before any build);"
     " CORRESPONDENCE.md rows 170-174; FACES_LEDGER.md (the b329 update)"),
    # ### THE FINITE-SIDE SEAL -- THE AXIOM FINDING AND THE THREE BARS NOT MET IN THEIR REGISTERED FORM (b329).
    ("finite-side-seal", "b329 (a measurement on the toolchain; three declared deviations)",
     "the core library's lemmas about divisibility, modulus and Nat.Coprime -- and Nat.mul_assoc -- carry"
     " propext (and often Quot.sound), as do omega, simp, ac_rfl and by_cases on divisibility; the audit bar is"
     " zero axioms, so the general theorems are stated as equations with witnesses (NotDiv p u := forall c,"
     " u != p * c; the congruence p^j t = t + p^m c; the ball t = p^m d) and proved from the axiom-free part of"
     " core plus helpers proved by induction. ### THREE REGISTERED BARS NOT MET IN THEIR REGISTERED FORM, SAID:"
     " (T1.4) the coprimality form of 'unit' (primality used nowhere in the module); (T1.6) the factorization"
     " before reduction; (T2.1) the explicit inverse rather than Nat.Coprime",
     "### NOTHING SORRIED, NOTHING WEAKENED SILENTLY; the first draft's general proofs printed [propext,"
     " Quot.sound] and were rewritten BEFORE any profile was written. ### The per-cell arm was not promoted to"
     " cover for a general bar. ### NO GRADE MOVED",
     "data/b329_axiom_probe.txt; data/b329_axiom_probe.lean; tools/b329_axiom_probe.py;"
     " data/b329_the_finite_side_seal.txt (the deviations); CORRESPONDENCE.md row 174"),
    # ### THE DISCRIMINATING FAMILY -- THE CONDITION AND THE SEEDS (b328).
    ("discriminating-family", "b328 (a derivation from the pinned source; a construction)",
     "for f = g * g^7 the four-term sum at an off-line quadruple {rho, conj rho, 1 - rho, 1 - conj rho} is"
     " 4 Re[G(c) G(-c)], c = rho - 1/2, G the seed's transform; for an EVEN seed 4 |G|^2 cos(2 phi),"
     " NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE; an odd component contributes -4 Re G_o^2, negative"
     " only below it. ### Checked against b326's banked four terms at the thirteen arc cells (phases -5.3"
     " to 24.1 degrees, all below the threshold; the arc's sums positive for exactly that reason). ### Two"
     " seeds built on the corpus's bump and aimed at the first off-line Epstein zero: the sine-aimed even"
     " seed at 89 degrees, the cosine-aimed odd seed at 0, widths a = 20, 40, 81, 160, each lawful"
     " (Definition 3.1; the pole conditions g~(0) = g~(1) = 0 measured)",
     "### THE PHASE COMES FROM sinh(delta v): zero on the line, small at narrow widths, set by a sine aimed"
     " at the ordinate. ### (F1) DERIVES; (F2) MET. ### Two sealed bars found defective by running them,"
     " neither edited: (B1) at 1e-9 fails on the square's discretization (1.1e-7, second order in the"
     " correlation grid); (B4) at 1e-10 fails because Simpson straddles a kink in every triple on the native"
     " nodes (exact at 2x; a Gauss-Legendre route meets the bar). ### The lore gains the rule with its gate."
     " ### NO GRADE MOVED",
     "data/b328_the_discriminating_family.txt; data/b328_derive_run.txt; data/b328_build_run.txt;"
     " data/b328_routes_run.txt; tools/b328_family.py; data/b328_registration_2026-09-05.txt (sealed before"
     " any run); CORRESPONDENCE.md row 168"),
    # ### THE DISCRIMINATING FAMILY -- THE CONTROL'S VERDICT (b328).
    ("discriminating-family", "b328 (a computation on the explicit-formula instrument; the verdict)",
     "the negative control under the two seeds at four widths, the places sides computed with NO ZERO and"
     " every sign through the noise-floor gate, the closure with every located zero as corroboration:"
     " **VERDICT: SEES IT** at [['E', 40.0], ['E', 81.0], ['E', 160.0], ['O', 20.0], ['O', 40.0], ['O', 81.0], ['O', 160.0]]. ### THE ZETA CONTROL under the same seeds: see the"
     " bank's cell table -- a flip, had one occurred, is the act's first finding",
     "### A VERDICT ON THIS FAMILY, ON THIS INSTRUMENT, AT THIS REACH -- NOT ON THE METHOD AND NOT ON ZETA."
     " ### b326's DOES NOT SEE IT on the arc's family STANDS; what changed is the family. ### The entailment,"
     " if SEES IT: the finite-instance places sum computed without any zero distinguishes a holding"
     " hypothesis from a failing one on this family, and the zeta window is a passed test FOR THIS FAMILY."
     " ### NOTHING ABOUT TOTALITY, h2 OR THE ROSTER. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b328_family_run.txt; data/b328_family.json; data/b328_cell_*_run.txt; FACES_LEDGER.md (the b328"
     " update); OPEN_TRAILS.md (W-ORD-DISCRIMINATING-FAMILY, updated); CORRESPONDENCE.md row 169"),
    # ### THE FACES LEDGER (b327).
    ("faces-ledger", "b327 (a ledger build, author-authorized 2026-09-04)",
     "PLACE-papers/FACES_LEDGER.md: thirteen rows -- the pentagon's five faces as the deposit states"
     " them, the finite-instance identity, the Sonin margin, the Li margin, the spectral-realization"
     " wall, the fixed-point silence, the two-radius family, the Epstein negative control at b326's"
     " result, and the live row (the Li-to-Weil bridge) -- each with its claim quoted from its"
     " emitting file, graded PROVED / MEASURED / IMPORTED / NAMED-ONLY, its correspondence rows, and"
     " its owed bridges; a cascade section with one of STATED / OWED / NONE for all 78 pairs",
     "### A MAP OF THE PREMISE, NOT A CARRIER OF IT. ### THE LEDGER CERTIFIES NOTHING AND COMPILES"
     " NO EQUIVALENCE -- the deposit's refusal is quoted in its head and governs it; every row's"
     " grade is its owning act's and no row is promoted by its neighbours. ### Rows enter only through"
     " tools/b327_faces_row.py (duplicates refused, notation guarded, every quotation verified against"
     " its emitter before writing, read back after every write). ### The owed bridges by ID:"
     " W-ORD-LI-WEIL-BRIDGE, W-ORD-DISCRIMINATING-FAMILY, W-ORD-LI-FAMILY-CONTROL. ### NO GRADE MOVED",
     "PLACE-papers/FACES_LEDGER.md; FINDINGS.md anchor faces-ledger; data/b327_the_faces_ledger.txt;"
     " data/b327_registration_2026-09-05.txt (sealed before any instrument ran); CORRESPONDENCE.md row 166"),
    # ### THE LI-TO-WEIL BRIDGE READ (b327).
    ("li-weil-bridge", "b327 (a read under the import bar; a derived map with its corroboration)",
     "the source: Lagarias, Li coefficients for automorphic L-functions, arXiv:math/0404394v4, pinned by"
     " hash (restating Bombieri-Lagarias 1999): lambda_n = S_inf(n) - S_f(n) + 1 -- the archimedean place,"
     " the finite places, the pole at s = 0 -- on the Li test family G_n(s) = 1 - (1 - 1/s)^n. ### THE MAP,"
     " derived as a sealed bar and corroborated at n <= 30 to 1.3e-251 by two routes: the deposit's"
     " archimedean channel is lambda_A(n) = S_inf(n) + 1. ### QUESTION ONE (the channel against the"
     " archimedean place): DIFFERENT, constituent quoted -- the constant 1, the log s term of the deposit's own split, the"
     " source's pole at s = 0. ### QUESTION TWO (the Li margin and the Sonin margin as one functional):"
     " DIFFERENT, constituent quoted -- the Li margin's second term is the finite places; the Sonin margin's is the"
     " compressed square, not a zero channel",
     "### ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL: 2 Re(Gamma_R'/Gamma_R), the atlas's"
     " kernel, is what both channels evaluate. ### THE BRIDGE STAYS OWED (W-ORD-LI-WEIL-BRIDGE), typed"
     " more sharply: a relation between the compressed square on the Sonin family and the finite-place"
     " channel on the Li family, or its impossibility. ### The order's if-SAME branch did not fire; the"
     " finite-range certificate says nothing about the Sonin margin on the Li family (no compact support,"
     " outside Theorem 1's class). ### The fourth control priced, not run (W-ORD-LI-FAMILY-CONTROL)."
     " ### NO THEOREM PROVED. ### NO GRADE MOVED. ### THE EQUIVALENCE THE DEPOSIT WITHHOLDS IS NOT STATED",
     "data/b327_bridge_run.txt; data/b327_bridge.json; data/b327_source.txt (the pin); tools/b327_bridge.py;"
     " FACES_LEDGER.md row L1; CORRESPONDENCE.md row 167"),
    # ### THE TWO NOTES, FILED AS CONTACTS (b327).
    ("faces-ledger", "b327 (two contacts in the emerging-programmes ledger; not seeds)",
     "EMERGING_RESEARCH_PROGRAMMES.md, Contacts filed 2026-09-05: the Curie reading of the"
     " eigenvalue-one boundary (the remainder's weight diverging at the boundary as a susceptibility;"
     " one consequence: sensitivity of the remainder to test-function perturbation near the boundary,"
     " checkable on the instrument, not checked); the cubit reading of the 256 rules (each a function on"
     " (Z/2)^3; rule 110's one-set a five-point Fano subset containing two lines, counted by"
     " tools/b327_notes.py; the question which Fano subsets define universal rules, not answered)",
     "### CONTACTS, NOT SEEDS: no promotion criterion, no claim, no grade. ### Provenance: the navigator's"
     " conversation layer, 2026-09-04, ratified by the b327 ferry. ### Filed nowhere research-facing",
     "PLACE-papers/EMERGING_RESEARCH_PROGRAMMES.md (the b327 contacts block); data/b327_notes_run.txt"),
    # ### THE REACH -- THE VERDICT (b326).
    ("the-reach", "b326 (a computation on the explicit-formula instrument; the verdict)",
     "both windows extended with every prime and every representation number to a = 400,"
     " twenty-six cells: **ZETA KEEPS THE PERMITTED SIGN AT EVERY CELL; SO DOES THE EPSTEIN"
     " FUNCTION** -- no crossing at this reach. ### The explicit formula closes for zeta at 26"
     " of 26 and for the Epstein function, with every located off-line zero, at 21 of 21 below"
     " the library's ceiling. ### **VERDICT: DOES NOT SEE IT AT THE ARC'S FAMILY TO a = 400,"
     " AND AT A DECLARED AIMED FAMILY** (cos(omega v) on every bump, omega = 16.290216, the"
     " banked off-line height). ### The navigator's expectation REFUTED in its first half (the"
     " priced crossing was an artefact) and MET in its second (zeta negative throughout)",
     "### A FAMILY VERDICT IS NOT A METHOD VERDICT. ### The reason from the numbers: on"
     " f = g conv g^# the off-line four-term sums come out POSITIVE for a seed whose transform"
     " keeps its sign across the off-line real part (+1.29 of 25.4 at a = 1.3; aimed, 92 to 98"
     " per cent of the zero side and still positive), so the failing function's places sum is"
     " minus a sum of squares plus a positive correction -- the permitted sign for the same"
     " reason zeta's is. ### **THE FAMILY THAT COULD SEE IT NEEDS A SIGN CHANGE ACROSS beta AND"
     " 1 - beta**, priced at one act, not built. ### **THE ENTAILMENT AT EXACTLY ITS SCOPE: the"
     " zeta window at this reach is not a passed test but a test this family cannot fail**; the"
     " arc's *could not have come out otherwise* is true of the library at the arc's cells and,"
     " on this family, of the method to a = 400. ### NOTHING ABOUT h2 OR THE ROSTER. ### NO"
     " GRADE MOVED. ### M-2 UNCHANGED",
     "data/b326_the_reach.txt; data/b326_windows_run.txt; data/b326_closure_run.txt;"
     " data/b326_registration_2026-09-04.txt (sealed before any run); CORRESPONDENCE.md row 164"),
    # ### THE REACH -- THE KERNEL THE CLOSURE DECIDED (b326).
    ("the-reach", "b326 (the closure, and the prior act's kernel)",
     "a derivation written into the registration BEFORE any run: the Epstein archimedean"
     " kernel is 2 Re(gamma_Q'/gamma_Q) = 2 Re psi(1/2 + iu) - 2 log(2pi/sqrt23), exactly as"
     " zeta's atlas kernel is 2 Re(gamma_R'/gamma_R); b325's kernel_q was named as one half of"
     " it. ### **THE CLOSURE DECIDED IT**: derived kernel closes at 21 of 21 cells below the"
     " ceiling; b325's fails at 21 of 21, and at every one the residual equals the missing half"
     " to within the bar (+2.2495 against 2.249540 at a = 3). ### **b325's PRICED CROSSING AT"
     " a ~ 22 WAS THE HALVED CHANNEL'S ARTEFACT AND IS WITHDRAWN**: the true places sum there is"
     " -0.374; the +0.017 reappears under b325's kernel and nowhere else",
     "### **b325 IS NOT RE-VERDICTED.** ### Its DOES NOT SEE IT at the arc's cells stands and"
     " is stronger (the true places sums are twice as negative); what is withdrawn is a PRICE,"
     " by the measurement b325 reported as blocked. ### Its sealed registration is not edited;"
     " the defect is filed as a sealed-bar-found-defective row for the next fold; the internal"
     " confinement keystone gains an appended correcting line with b325's block visible above"
     " it. ### **THE LIBRARY THE ORDER NAMED (two banked off-line zeros) FAILED AT 15 CELLS**"
     " and the fourth link -- completeness -- was walked to fifteen unbanked zeros. ### The"
     " corpus's census is not called wrong: it banked what lay below t = 33. ### NO GRADE MOVED."
     " ### NO ACT RE-VERDICTED. ### M-2 UNCHANGED",
     "data/b326_the_reach.txt; data/b326_closure_run.txt (the link walked); tools/b326_windows.py"
     " (kernel_q_derived, fixture (iv)); data/b326_closure_run_first_defective.txt (kept);"
     " CORRESPONDENCE.md row 165"),
    # ### THE EPSTEIN ZEROS (b326).
    ("epstein-zeros", "b326 (the zero library, two routes, every box)",
     "the Epstein function's zeros on the line to T = 150 by the corpus's own argument-principle"
     " census run at Re s = 1/2, its constants rebound for the height (K = 240, dps = 119 -- the"
     " registered dps 60 FAILED ITS OWN GATE, the cancellation being against the pole term,"
     " e^{pi t/2}/t^2): **146 ZEROS, EVERY ONE AGREED BY AN INDEPENDENT SECOND ROUTE** (Z_Q by"
     " regularized incomplete gammas, mpmath.findroot), 299 of 299 boxes holding exactly their"
     " sign-change count (one close pair 0.015 apart resolved by a finer scan). ### The"
     " completeness census over sigma in [0.52, 1.50] to t = 150: **SEVENTEEN OFF-LINE ZEROS,"
     " FIFTEEN UNBANKED**, each by both routes; 146 + 2 x 17 = 180 against a main term of 178.6",
     "### THE CENSUS'S CAVEAT ANSWERED, NOT WAVED: a line scan counts what lies ON the line, the"
     " box windings say what lies within 0.02 of it, and the completeness census says what lies"
     " off it -- the abscissa 1.50 is where SUM r_Q(k) k^{-3/2} = 1.38 < 2 makes a zero impossible."
     " ### The two banked off-line zeros refine to 0.953260 + 16.290216i and 0.797997 +"
     " 29.551761i inside their rectangles and reappear in the completeness census. ### **THE"
     " CORPUS'S CENSUS IS NOT CALLED WRONG**: it banked what lay below t = 33 and was right; the"
     " confinement keystone's finding is strengthened from two instances to seventeen. ### The"
     " library is COMPLETE TO T = 150 AND NO HIGHER, a cap set by price. ### NO GRADE MOVED",
     "data/b326_epstein_zeros.json; data/b326_zeros_run.txt; data/b326_offline.json;"
     " data/b326_offline_run_150.txt; tools/b326_zeros.py; tools/b326_offline.py;"
     " tools/e16/epstein_census.py (the evaluator, rebound not edited)"),
    # ### THE NEGATIVE CONTROL -- THE VERDICT (b325).
    ("negative-control", "b325 (a read, a pricing, and the run; the verdict)",
     "the archimedean instrument aimed at a hypothesis KNOWN TO FAIL: the Epstein zeta of"
     " x^2 + xy + 6y^2 (disc -23, h = 3), whose corpus census banks two zeros off the line."
     " ### The places sum SUM_v W_v = PR_Q - A_Q is **NEGATIVE AT ALL THIRTEEN OF THE ARC'S"
     " CELLS**, -16.069614947 down to -2.243190916; the order's falsifier asked for the"
     " forbidden POSITIVE sign and no cell gives one. ### **VERDICT: DOES NOT SEE IT AT THE"
     " ARC'S CELLS. THE REGISTERED EXPECTATION IS REFUTED AT THE CURRENT REACH.** ### **AND"
     " THE REASON IS STRUCTURAL**: r_Q(2) = r_Q(3) = 0, so the finite channel is identically"
     " zero until a = 2 and still 0.006348865 against an archimedean 2.249539781 at a = 3."
     " ### **THE REACH IS PRICED**: beyond the arc's cells the sign CROSSES TO POSITIVE AT"
     " a ~ 22 and stays positive at 24, 28, 32, 50, while zeta stays permitted everywhere",
     "### A SCOPE STATEMENT IS NOT A CAPABILITY STATEMENT. ### The instrument does not see"
     " THIS failure AT THE ARC'S CELLS; it is not shown unable to see a failure. ### **THE"
     " CROSSING IS A PRICE, NOT A SEES-IT VERDICT**: the order's verdict needs the zero side"
     " as corroboration and the corpus owns only the OFF-line Epstein zeros (its census began"
     " at sigma = 0.52). ### **WHAT THE ZETA WINDOW WAS, AT EXACTLY ITS SCOPE**: a window"
     " whose sign carried no arithmetic information at the widths it was taken at -- b321"
     " said so before counting, and this act confirms that scope from the outside with an"
     " object whose answer is known. ### NOTHING ABOUT ZETA, h2, OR THE ROSTER. ### NO GRADE"
     " MOVED. ### NO ACT RE-VERDICTED. ### M-2 UNCHANGED",
     "data/b325_the_negative_control.txt; data/b325_run.txt; tools/b325_epstein.py;"
     " data/b325_registration_2026-09-04.txt (section (0) declares the deviation);"
     " CORRESPONDENCE.md row 162"),
    # ### THE NEGATIVE CONTROL -- THE CONTROL THAT FIRED (b325).
    ("negative-control", "b325 (the positive control, and what it caught)",
     "zeta run through the same channels is a control whose correct answer b321 proved: for"
     " a lawful f the zeta places sum is -Z with Z a sum of squared moduli, NEVER POSITIVE."
     " ### At a = 32 it came out +0.003489041. ### **THE CAUSE IS b321_window.PRIMES ="
     " (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)**, copied from the atlas's own prime loop and"
     " sufficient where b321 used it (its widest cell has f supported below 9); at a = 32"
     " the support reaches 1024. ### **WITH EVERY PRIME THE VALUE IS -0.000389214 AND THE"
     " CONTROL PASSES AT EVERY WIDTH TESTED.** ### A second latent defect found and NOT"
     " repaired in the owner: carto_atlas.kernel memoises without keying on its grid --"
     " guarded in the caller, reported",
     "### **b321 IS NOT RE-VERDICTED.** ### At the arc's own cells the eleven-prime and"
     " every-prime channels agree to every printed digit (-0.315810512 at a = 3 from both)."
     " The constant is scope-bound and the scope was never written down; this is the act"
     " where it bit. ### **AND THIS ACT DECLARES THREE FAILINGS OF ITS OWN**: (A) the seat"
     " RAN AHEAD of its own EXECUTION block -- the registration was sealed after the run,"
     " declared as its section (0) with every bar marked [ORDER] or [SEAT, POST-HOC]; (B)"
     " the satisfiability checker REFUSED to seal a mis-typed clause and was right; (C) the"
     " noise-floor gate was first fed adjacent cells rather than a refinement pair, repaired"
     " to the same cell at two resolutions, all three RESOLVED. ### NO GRADE MOVED. ### NO"
     " OWNER INSTRUMENT EDITED. ### M-2 UNCHANGED",
     "data/b325_the_negative_control.txt; data/b325_run.txt (fixtures (viii)-(ix));"
     " data/b325_regspec_run.txt (the refusal); tools/b321_window.py line 51 (the constant);"
     " CORRESPONDENCE.md row 163"),
    # ### THE EPSTEIN CASE, READ AT CONTENT AND PRICED (b325).
    ("epstein", "b325 (the read and the pricing)",
     "the confinement keystone's Epstein case: the principal form x^2 + xy + 6y^2, disc -23,"
     " h(-23) = 3, named in the corpus's own census header. ### The ledger the keystone calls"
     " positive is the LI one (lambda_n) -- positivity of the coefficient sequence, not of"
     " the zeros. ### The zeros come from the corpus's argument-principle census,"
     " epstein_census.py, 2-D by construction: 450 cells over sigma in [0.52, 1.50],"
     " t in [0.5, 33.0], **TWO ZEROS, BOTH OFF THE LINE** (sigma in [0.94, 1.08] at"
     " t in [16.0, 16.5]; sigma in [0.66, 0.80] at t in [29.5, 30.0]). ### **THE PRICING,"
     " TYPED**: the archimedean factor (sqrt23/2pi)^s Gamma(s) is NOT zeta's"
     " pi^-s/2 Gamma(s/2) -- the corpus says so in its own METHOD header -- so the kernel"
     " was BUILT from the quoted factor; the finite side is the coefficient sequence of"
     " -Z_Q'/Z_Q, BUILT from r_Q by Dirichlet inversion (they differ by up to 15.74 below"
     " n = 60); the lawful class TRANSFERS (poles at s = 0, 1; pole term -5.03e-17)",
     "### THE FALSIFIER FITS INSIDE THE ACT; THE TWO NAMED CONTROLS DO NOT. ### The"
     " explicit-formula control is BLOCKED on the on-line zero library, which the corpus"
     " does not own (the census was hunting off-line zeros and started at sigma = 0.52);"
     " Theorem 1's archimedean control does not cover Z_Q at all -- a hypothesis, not a"
     " cost. ### **THE ON-LINE LIBRARY IS PRICED AT ONE ACT WITH THE TOOL ALREADY WRITTEN**:"
     " re-run the census over sigma in [0.45, 0.52] and refine each winding cell. ### The"
     " keystone's own finding -- *the functional equation illuminates the critical line; it"
     " does not confine zeros to it* -- is the PREMISE of this test, not its subject, and"
     " stands unchanged. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b325_the_negative_control.txt; data/b325_extract_notes.txt;"
     " tools/e16/epstein_census.py (METHOD header); tools/e16/epstein_census_bank.jsonl;"
     " PLACE-papers/day1/Which_Structure_Confines.md (the emitting keystone, internal copy);"
     " CORRESPONDENCE.md row 162"),
    # ### THE WALL (b324).
    ("keystones-reread", "b324 (reads and definitional decisions; the wall)",
     "the residue keystone's object and the arc's constructed space, decided constituent by"
     " constituent. ### The keystone's is **the positive space on the zeros** -- *positivity"
     " has no zeros, the operator has no space, and the space is exactly what neither"
     " supplies. The space is the wall* -- defined by the requirement that a self-adjoint"
     " operator's spectrum REALIZE the zeta-zeros. ### The arc's is Connes-Consani's S(1,1):"
     " two homogeneous vanishing conditions on a function and its transform, **with no"
     " operator and no zeros in the definition at all**. ### **VERDICT: DIFFERENT, SEVEN OF"
     " SEVEN**, differing at the FIRST constituent walked. ### **SO NO: THE ARC DID NOT MOVE"
     " THE WALL**, and the second half of the registered expectation does not arise -- an act"
     " that did not build the keystone's object cannot have moved the wall that object IS",
     "### A DIFFERENT VERDICT ON TWO OBJECTS IS NOT A CONFLICT BETWEEN TWO RECORDS. ###"
     " **THE VERDICT RESTS ON NO SHARED WORD**: the order refused resemblance BY NAME and the"
     " registration gave the test -- if the argument would survive replacing one side's term"
     " with a synonym the other does not use, it was resemblance. ### **THE KEYSTONE HAD"
     " ALREADY PLACED THE ARC'S SOURCE**: its realization-candidate map grades"
     " *Connes-Consani (reduces RH to a Weil positivity left open)* among routes that STALL"
     " AT THE REALIZATION CLAUSE. ### **AND A MEASURED PROVENANCE FINDING RIDES WITH IT:**"
     " *the space is the wall*, *the positive space* and **Sonin** -- the name of the arc's"
     " entire space -- EACH APPEAR ZERO TIMES IN THE DEPOSITED MONOGRAPH. ### The deposit is"
     " ms v5.10.2; the wall's naming is v5.13 and INTERNAL. ### NO GRADE MOVED. ### NO ACT"
     " RE-VERDICTED. ### M-2 UNCHANGED",
     "data/b324_the_keystones_reread.txt; data/b324_reread_run.txt;"
     " PLACE-papers/phase1.5/proofs/THE_RESIDUE_OF_RH.md (the emitting keystone);"
     " CORRESPONDENCE.md row 160"),
    # ### THE MARGIN (b324).
    ("keystones-reread", "b324 (reads and definitional decisions; the margin)",
     "the balance keystone's margin against the arc's. ### The keystone's is M(n) :="
     " lambda_Z(n) + lambda_A(n) = lambda_n, positive throughout 1 <= n <= 300, minimum at"
     " n = 1 (lambda_1 = 0.0230957089661), growing like (n/2) ln n. ### The arc's is"
     " W_8(f) - Tr(theta(g) S theta(g)*), equal by Theorem 4.7 to minus a remainder integral:"
     " +0.271444634, +0.285510313, +0.309777648, growing toward the boundary. ### **THEY"
     " DIFFER AT SIX OF SEVEN CONSTITUENTS** -- different index, different decomposition, and"
     " **only the keystone's margin contains the zeros**. ### The seventh keeps it alive: the"
     " monograph names positivity of the Weil functional and lambda_n >= 0 as classical faces"
     " of ONE obligation h2. ### **VERDICT: UNDECIDED**",
     "### EQUIVALENCE OF THE OBLIGATIONS IS NOT EQUIVALENCE OF THE MARGINS. ### **AND THE"
     " BRIDGE IS ABSENT BY DESIGN, NOT BY OVERSIGHT**: the deposit records that the register"
     " pentagon compiles the five faces' structure *while **deliberately not** compiling the"
     " cross-register equivalences, since to compile 'discharge one and you discharge all"
     " five' would be to compile RH-equivalence itself*. ### **THE BRIDGING STATEMENT IS"
     " TYPED AND FILED AS THE ARC'S MOST VALUABLE OPEN ITEM**: a formula carrying the"
     " archimedean margin at a lawful test function to the Li margin at an index n, or a"
     " proof that no such formula exists. ### **ITS HONEST PRICE RIDES WITH IT**: the"
     " keystone's margin is positive AT THE BENCH to n = 300, lambda_Z measured NEGATIVE"
     " across n = 156..186 and 247..287, and Voros's threshold puts discrimination beyond"
     " n ~ 10^18. ### The seven contacts came out 3 CORROBORATED, 4 UNTOUCHED, 0 IN TENSION."
     " ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b324_the_keystones_reread.txt; data/b324_filings_run.txt;"
     " PLACE-papers/phase1.5/spectral/BALANCE_AND_POSITIVITY.md (the emitting keystone);"
     " CORRESPONDENCE.md row 161"),
    # ### THE FOLD ITSELF (b323).
    ("archimedean-arc-fold", "b323 (a filings act; nine acts into one section)",
     "b314 through b322 folded into `FINDINGS.md` as THE ARCHIMEDEAN INSTRUMENT ARC --"
     " **+154 lines, its sixteenth section, 2709 to 2863 lines**. ### Each entry carries its"
     " grade AS ITS OWN ACT LEFT IT, its own scope sentence, and an obstacle quoted verbatim"
     " and verified against the act that ORIGINATED it. ### **THE GATE IS A GENERATOR AND NOT"
     " A REVIEWER**: a quotation that fails F-QUOTE never reaches the file at all, and"
     " F-QUOTE carries a DISCRIMINATION arm -- an altered quotation comes back UNFINDABLE."
     " ### F-QUOTE 18 of 18; F-COUNT 9 results, 9 obstacles, the arc exactly. ### **THE WRITE"
     " IS PURELY ADDITIVE AND THAT IS MEASURED**: the pre-append working file AND the blob at"
     " HEAD are both TRUE BYTE PREFIXES of the result",
     "### A FOLD IS A FILING AND NOT A CONCLUSION. ### **NO GRADE MOVES. ### NO ACT IS"
     " RE-VERDICTED. ### NO NEW MATHEMATICS** -- every number in the section was already"
     " banked by the act that owns it. ### The arc's one statement is filed WITH ITS SCOPE"
     " PRINTED BESIDE IT: **no theorem is proved by any act in it**, the window decides"
     " nothing, and **the SIZE of no margin on the domain axis is certified anywhere in the"
     " arc**. ### W-ORD-ARCH-MEMBERSHIP, W-ORD-PHI-MU-L2 and W-ORD-WINDOW-CLASS all stay"
     " OPEN. ### Three defects in this act's OWN generator are declared: a missing idempotence"
     " guard that filed the arc twice before any commit, a sentence asserting a difference its"
     " own measurement showed was zero, and a log list the runner could not write. ### NO"
     " AGGREGATION IS STATED. ### M-2 UNCHANGED",
     "data/b323_the_fold.txt; data/b323_fold_run.txt; data/b323_fold_emitted.md;"
     " PLACE-papers/FINDINGS.md (the filed section); CORRESPONDENCE.md row 158"),
    # ### THE DEFECTIVE-BARS TABLE (b323).
    ("archimedean-arc-fold", "b323 (the table this record had never filed before)",
     "**THREE TIMES IN NINE ACTS A BAR WAS SEALED BEFORE ANY VALUE AND THE BAR ITSELF TURNED"
     " OUT WRONG.** ### b319's (B3) reach bar required the rank constant on BOTH axes when the"
     " domain axis cannot deliver it; b322's (B2) imported two labels that do not partition"
     " the possibilities; b322's (B5) has branches that are not mutually exclusive and fired"
     " twice at once. ### **IN NO CASE WAS THE SEALED FILE EDITED.** ### And in all three the"
     " defect was found **by running the sealed bar and reading what came back**, not by"
     " revising it: b319 reported an EMPTY reach under a bar it had shown unsatisfiable and"
     " left the fix as a PROPOSAL; b322 reported the verdict its broken rule computed and then"
     " TOOK THE WEAKER of the two branches that rule licensed",
     "### A TABLE OF ONE'S OWN DEFECTS IS NOT A RESULT EITHER. ### **A DEFECT NAMED IN A"
     " SEALED BAR IS EVIDENCE; A SEALED BAR QUIETLY REWRITTEN IS NOT**, and a record whose"
     " registrations are only ever reported as having worked is a record that has stopped"
     " reading them. ### The lore is consolidated with its incidents and SPLIT BY WHAT"
     " ENFORCES IT: nine rules MECHANIZED, five JUDGEMENT. ### The suite is inventoried at ten"
     " pieces. ### The archimedean instrument's three certifications are tabled with their"
     " cells and margins, and **its limits are stated as measurements**: the domain axis's"
     " rate on both ladders, and a resolving power priced twice, both prices beyond what it"
     " reaches. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b323_the_fold.txt; data/b323_fold_rows.json;"
     " data/b319_the_stable_rank.txt and data/b322_the_membership.txt (the originating acts);"
     " CORRESPONDENCE.md row 159"),
    # ### THE LADDER, AND THE TRUNCATION TAIL THAT PREDICTS IT (b322).
    ("membership", "b322 (reads at owners, a definitional decision, and one measurement)",
     "the unit's membership residual run along the DOMAIN ladder at stable rank, and fitted."
     " ### b319 measured it constant at 0.4395 across four GRID refinements and reported a"
     " domain course without fitting it. ### **THE RESIDUAL FALLS AT EVERY STEP** -- 0.797250,"
     " 0.644963, 0.439502, 0.286136, 0.197491 at X = 8 to 128, ranks 20, 37, 69, 133, 262 --"
     " so by a bar sealed BEFORE any definition was unfolded, **THE RESIDUAL IS THE"
     " TRUNCATION'S AND b300's DERIVATION IS NOT CONTRADICTED BY IT**. ### Fitted exponent"
     " **p = -0.519901**, and a SECOND ROUTE SHARING NO CODE predicts it: max x u(x) beyond"
     " X/2 is 1.118582, so u decays like 1/x, so the L2 mass beyond X goes like X^-1/2 --"
     " predicted -0.500000, **AGREE**. ### Eight constituents unfolded side by side, neither in"
     " the other's language; two differ, CONDITION TWO and THE DOMAIN, and **THEY ARE NOT"
     " INDEPENDENT**: the first is what the second produces",
     "### A FALLING COURSE AT FIVE FRAMES IS A FALLING COURSE AT FIVE FRAMES. ### **THE ACT"
     " DID NOT SETTLE THE MEMBERSHIP AND DOES NOT CLAIM TO** -- the arms DISAGREE, the"
     " noise-floor gate REFUSES 4 of 4 steps, and the SIZE of no value on the ladder is"
     " certified. ### **THE RATE HALF OF THE REGISTERED EXPECTATION IS REFUTED**: against"
     " b321's instrument exponent q = -1.324018 by the same fitter on the same domains,"
     " p/q = 0.392669, outside the sealed band [0.5, 2.0]. ### **NO UNIT IS ADOPTED AND NONE"
     " IS REPLACED.** ### b300 stands at DERIVES-on-IMPORTS; b316 and b319 stand at theirs."
     " ### W-ORD-PHI-MU-L2 stays OPEN and the instrument cannot see it. ### NO ACT"
     " RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b322_the_membership.txt; data/b322_components_run.txt;"
     " tools/b322_ladder.py (the emitting file); CORRESPONDENCE.md row 156"),
    # ### THE RULE, AND THE VERDICT THAT TOOK THE WEAKER BRANCH (b322).
    ("resolving-power", "b322 (the verdict, and two of its own sealed bars found defective)",
     "a question is UNDER-RESOLVED, not open, when the candidates sit closer together than the"
     " instrument's distance from the answer -- **AND THE PRICE IS THE RATIO**. ### b321 bought"
     " the rule one act earlier: its identity control HELD and still could not tell two"
     " exponent copies apart, which were 0.000981 to 0.003994 apart where the instrument sat"
     " 0.018808 to 0.023224 from the answer. ### **THIS ACT IS ITS FIRST DELIBERATE"
     " APPLICATION**: the membership question is priced rather than decided -- from"
     " p = -0.519901 and the residual 0.197491 at X = 128, the domain at which it would reach"
     " 0.01 is **X = 3.973e+04, a factor of 3.104e+02** beyond what was reached, labelled as an"
     " extrapolation of a fitted slope",
     "### A QUESTION THAT CARRIES ITS PRICE IS NOT A QUESTION ANSWERED. ### **TWO OF THIS"
     " ACT'S OWN SEALED BARS WERE FOUND DEFECTIVE AND NEITHER WAS EDITED.** ### (B2)'s"
     " dichotomy IS NOT A PARTITION: b316's taper smooths the DISCONTINUITY at the domain's"
     " end and does not restore the mass BEYOND it, so a reading of THE VECTOR means NOT THE"
     " EDGE DISCONTINUITY and not NOT THE TRUNCATION. ### (B5)'s branches ARE NOT MUTUALLY"
     " EXCLUSIVE: two fired at once and the seal did not order them, so the runner's if/elif"
     " chain picked DIFFERENT VECTORS on an ordering that was the tool's and not the seal's."
     " ### **THE ACT TOOK THE WEAKER BRANCH, UNDER-RESOLVED**, because between two branches a"
     " defective rule licenses equally an act may not help itself to the stronger one. ###"
     " W-ORD-ARCH-MEMBERSHIP IS NOT CLOSED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b322_the_membership.txt; data/b322_registration_2026-09-04.txt (sealed);"
     " data/b321_the_window_opened.txt (the incident); CORRESPONDENCE.md row 157"),
    # ### THE SECOND AND THIRD THEOREMS AS CONTROLS (b321).
    ("identity-control", "b321 (two further theorems as controls on the instrument)",
     "the instrument tested against an EQUALITY and against the explicit formula. ###"
     " **THEOREM 4.7 / (83) IS AN EQUALITY**, Tr(theta(f) S) = W_8(f) + INT f(rho^-1)"
     " eps(rho) d*rho, so by cyclicity b320's margin must be exactly minus the remainder"
     " integral. ### Computed with the b313 FLIPPED COPY -- the source's exponent, on b313's"
     " reading of three sites and on no number -- it gives 0.158890, 0.186482, 0.221284 at the"
     " three covered cells. ### **AND THE INSTRUMENT WALKS TOWARD EACH**: the residual along"
     " the domain ladder at a = 1.3 falls 0.896557, 0.306328, 0.112555, 0.047182, 0.023224 --"
     " by a factor of two to three at every step, at all three cells. ### **AND THE EXPLICIT"
     " FORMULA (148) CLOSES AT ALL THIRTEEN CELLS**, residuals 2.2e-09 to 3.6e-05 against the"
     " atlas's own sealed TOL = 1e-03, truncation bound never above 1.1e-11",
     "### A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### **NO THEOREM IS"
     " PROVED HERE** -- the source proved all three. ### **AND THE ORDER'S CONDITIONAL IS"
     " REFUTED: it said this act closes the exponent question by measurement IF the identity"
     " holds. ### IT HELD, AND IT DID NOT.** ### The corpus's own exponent copy passes every"
     " one of the same arms at 3 of 3 cells; the two copies differ by 0.000981, 0.001937,"
     " 0.003994 where the instrument's own distance from the equality is 0.023224, 0.020793,"
     " 0.018808. ### **AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES THAT LIE"
     " CLOSER TOGETHER THAN ITS OWN DISTANCE FROM THE ANSWER.** ### b313's READING stands"
     " alone, where b313 left it. ### **NO BAR WAS MOVED**: one quadrature pair missed the"
     " sealed 1e-06 and the quadrature did more work rather than the bar less. ### NO ACT"
     " RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b321_the_window_opened.txt; data/b321_components_run.txt;"
     " tools/b321_window.py (the emitting file); tools/e16/b313f_qeps_layer.py;"
     " CORRESPONDENCE.md row 154"),
    # ### THE WINDOW, AND WHY ITS SIGN IS NOT EVIDENCE (b321).
    ("window-opened", "b321 (the finite-instance balance on lawful objects)",
     "the places sum of Proposition C.1 computed at the ten cells above a = 2^{1/2}, where the"
     " lawful f = g conv g^# is supported past 2 and the primes enter. ### SUM_v W_v(f) ="
     " PR - A, every sign quoted from an owner, comes out **NON-POSITIVE AT 10 OF 10 CELLS**."
     " ### ### **AND THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE"
     " OF ANYTHING.** ### Two facts collapse it: **(i) THE POLE TERM VANISHES IDENTICALLY**"
     " for a lawful f -- P = f-tilde(0) + f-tilde(1), and Theorem 1's own vanishing conditions"
     " force both to zero, worst measured magnitude of order 1e-16 -- so (148) collapses to"
     " SUM_v W_v = - Z; and **(ii) Z CANNOT BE NEGATIVE**, because f-hat is the squared"
     " modulus of g-hat (b320 measured it, 13 of 13) and the ordinate library holds only zeros"
     " ON the line. ### **SO THE TOTAL IS NON-POSITIVE BEFORE A SINGLE PRIME IS SUMMED**",
     "### A COUNT THAT COULD NOT HAVE COME OUT THE OTHER WAY IS NOT A RESULT. ### **A FINITE"
     " WINDOW AT A FINITE CUTOFF DECIDES NOTHING GLOBAL** -- 10000 ordinates, eleven primes,"
     " thirteen cells of one family, against a criterion that quantifies over every lawful g."
     " ### A zero OFF the line is exactly what would break the sign and this library contains"
     " none by construction. ### **ONE THING HERE IS A REAL MEASUREMENT: THE PRIME SUM CHANGES"
     " SIGN TWICE ALONG THE LADDER** -- positive at 1.5 and 1.7, negative from 1.9 to 2.4,"
     " positive again at 2.8 and 3.0 -- which is where log 2 falls in an oscillating test"
     " function and nothing more. ### **THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL.** ### THE"
     " BALANCE IS INTERPRETED BY NOBODY IN THIS ACT. ### W-ORD-WINDOW-CLASS STAYS OPEN. ### NO"
     " GRADE MOVED. ### M-2 UNCHANGED",
     "data/b321_the_window_opened.txt; data/b321_components_run.txt;"
     " data/b321_registration_2026-09-04.txt (sealed); CORRESPONDENCE.md row 155"),
    # ### THE SQUARE OF THE SEED, AND THE CELLS THE THEOREM COVERS (b320).
    ("lawful-function", "b320 (a construction, and the class test the source defines)",
     "the corpus's seed squared in the source's own convention and tested against the"
     " source's own class definition. ### The adjoint is written once from the involution of"
     " the convolution C*-algebra, g#(rho) = conj(g(rho^-1)) against the MULTIPLICATIVE"
     " measure d*mu, which in v = log rho makes the product the autocorrelation with"
     " transform |g-hat|^2. ### By Definition 3.1 -- positive definite iff f-hat >= 0"
     " pointwise -- **f = g conv g# IS POSITIVE DEFINITE AT 13 OF 13 CELLS**, minima -4.6e-17"
     " to +5.9e-18 against a sealed -1e-09 floor. ### **AND THIS SETTLES b318's READING BY"
     " MEASUREMENT**: b318 found NEITHER test function positive definite, 0 of 13, and read"
     " the corpus's window as a candidate g and not a candidate f. ### The window passes at NO"
     " cell; its square passes at every one. ### **THEOREM 1's COVERED CELLS, NAMED FROM THE"
     " CHECK: 1.3, 1.35, 1.41** -- the support condition is the only one that bites, and the"
     " two vanishing conditions hold at EVERY cell to 1.4e-17..5.7e-16",
     "### A SQUARE LANDING IN THE CLASS OF SQUARES IS NOT A DISCOVERY. ### **SCOPE: this"
     " fixes WHICH CELLS the source's theorem speaks at, and nothing else.** ### **AND THE"
     " CLASS TEST CAN FAIL, WHICH IS THE ONLY REASON ITS PASSING IS WORTH PRINTING**: the same"
     " code path returns min f-hat = -5.85e-01 on b318's wide-minus-narrow fixture. ### **NO"
     " WINDOW IS OPENED** -- the ten uncovered cells are computed and printed as data with no"
     " claim, and the inequality holding there is evidence for nothing, because outside the"
     " hypotheses there is no conclusion to be evidence for. ### **NO UNIT IS USED.** ### NO"
     " ACT RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b320_the_lawful_function.txt; data/b320_components_run.txt;"
     " tools/b320_weil.py and tools/b318_square.py (the emitting files);"
     " CORRESPONDENCE.md row 152"),
    # ### BOTH SIDES, AND THE CONTROL THAT FAILED BEFORE IT HELD (b320).
    ("source-control", "b320 (a computation, and the source's own theorem as its control)",
     "both sides of the source's inequality computed on the stable-rank instrument and checked"
     " where Theorem 1 covers. ### The left side is built from (53) and (38) with its"
     " principal-value constant MEASURED and not remembered -- C_R = 2.415093331442 from two"
     " Gaussian widths agreeing to 4.7e-10, landing on gamma + log(2 pi) = 2.415092731311,"
     " which this act did not put in. ### **THIS ACT'S FIRST REPORTED VERDICT WAS FAILS.** ###"
     " The registration's (B6) fixed a link order before any value existed and the failure"
     " named a constituent: links (1)-(3) clean, **LINK (4), THIS ACT'S OWN IMPLEMENTATION OF"
     " (38), NAMED**. ### After the repair: **W_inf >= SQUARE at all three covered cells,"
     " margins +0.2714, +0.2855, +0.3098, and at 27 of 27 instrument frames.** ### A second"
     " defect in the same function survived the first repair and printed 1.9e9; two new"
     " fixtures fail without each repair, and a SECOND AND INDEPENDENT ROUTE was built",
     "### A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### **NO THEOREM IS"
     " PROVED HERE** -- the source proved Theorem 1 and this act checked that the instrument"
     " does not contradict it where it speaks. ### **NO BAR WAS MOVED, NO CELL DROPPED, NO"
     " TOLERANCE LOOSENED, AND THE REGISTRATION WAS NOT RE-SEALED** -- hash 6f1c1e13..."
     " verifies intact. ### **THE REACH IS NON-EMPTY FOR THE FIRST TIME IN THIS ARC, 3 OF 3,"
     " UNDER A BAR THIS ACT ITSELF CORRECTED** in its registration before any value, per"
     " b319's own proposal. ### **SCOPE: the SIGN of every margin is certified at every frame;"
     " the SIZE at none** -- the noise gate REFUSES 3 of 6 and all three are domain frames."
     " ### **AND THE REGISTERED EXPECTATION IS HALF REFUTED**: the margin was expected to"
     " SHRINK toward the boundary cell and it GROWS. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b320_the_lawful_function.txt; data/b320_corroboration.txt;"
     " data/b320_registration_2026-09-04.txt (sealed); CORRESPONDENCE.md row 153"),
    # ### THE SUBSPACE (b319).
    ("stable-rank", "b319 (an instrument build, act two of the archimedean instrument)",
     "the archimedean instrument's subspace by the source's own eigenvalue-one"
     " characterization. ### The paper's (81) reads P P-hat P = SUM lambda(n)^2"
     " |zeta_n><zeta_n| + R with R the orthogonal projection on Sonin's space, and its page 28"
     " says S(1,1) IS the eigenvalue-one eigenspace -- so the spectrum is {lambda(n)^2}"
     " together with 1 and an eigenvalue is DIMENSIONLESS. ### On the free coordinates the"
     " sandwich is M = I - (hy/h) C^T C. ### **ON THE GRID AXIS THE SELECTED DIMENSION IS 69,"
     " 69, 69, 69 ACROSS N = 2048 TO 16384, WHERE b316's SCHEME GAVE 80, 80, 79, 79** --"
     " rank changes: b316 one, this act zero. ### **AND THE DRIFT FELL WITH IT**: 8.6e-05 to"
     " 4.5e-04 where b318 measured 6.1e-03 to 2.3e-02. ### The threshold TAU = 1e-6 was fixed"
     " from the source and the corpus's banked lambda(0)^2 BEFORE any spectrum was seen, and"
     " then landed in a measured void: largest admitted ~2.0e-07, smallest excluded 5.62e-06",
     "### A RANK THAT HOLDS STILL IS NOT CONVERGENCE. ### **THE GRID HALF OF THE REACH IS"
     " ATTAINED AND THE DOMAIN HALF IS NOT** -- the noise-floor gate REFUSES all six domain"
     " pairs, and the domain rank must grow because the space does (20, 37, 69, 133, 262)."
     " ### **THE SUBSPACE CHANGED**: the stable cut STRICTLY CONTAINS b316's (only-grid 9 to"
     " 12 at every frame, only-stable 0), so the smear is negative at 3 cells where b318 found"
     " 5. ### Structural findings survive: square never negative, the identity re-proved at"
     " 3.3e-06 to 2.6e-05, zeta_n residual 1.0000 on both cuts at all eight frames. ### **THE"
     " UNIT'S RESIDUAL IS A MEASUREMENT WITH NO VERDICT**: 0.4395 constant on the grid axis"
     " where the grid cut drifts -- it holds still, and it is still nowhere near zero. ### NO"
     " ACT RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b319_the_stable_rank.txt; data/b319_components_run.txt;"
     " tools/b319_stable.py (the emitting file); CORRESPONDENCE.md row 150"),
    # ### THE REPAIR, AND THE BAR THAT COULD NOT BE MET (b319).
    ("stable-rank", "b319 (the kernel-coverage repair, and the reach bar's own defect)",
     "the kernel-coverage defect discharged sixteen acts after b315 filed it. ### The profile"
     " was regenerated from source and compared **TO THE GIT BLOB, NOT THE WORKING FILE** --"
     " 33195 bytes each, byte-for-byte identical; the working file is 475 bytes longer, one"
     " per line, which is core.autocrlf and not the kernel. ### Ten Core modules had no"
     " compiled artefact; all ten compiled, 0 build errors. ### 24 imports and 91 print lines"
     " appended. ### **PRINTS 475 TO 566, AND THE OLD PROFILE IS A LITERAL BYTE PREFIX OF THE"
     " NEW ONE.** ### **AXIOM-BEARING TERMINALS AMONG THE 91 NEWLY CERTIFIED: 0**, read off"
     " the printed file. ### The gate now PASSES and its fixtures still show it can fail",
     "### A DEFECT DISCHARGED IS NOT A RESULT: every one of the 91 was already compiling and"
     " nothing was proved by printing it. ### **AND THE REACH IS STILL EMPTY, 0 OF 6, BECAUSE"
     " THE BAR THIS ACT SEALED IS DEFECTIVE** -- (B3) requires the rank constant across BOTH"
     " axes, which on the domain axis is unsatisfiable by the nature of the object. ### The"
     " second scheme was tried as ordered: **on the grid axis pinning selects the IDENTICAL"
     " index set**, and **on the domain axis it admits a direction at eigenvalue-distance"
     " 1.000e+00 from one** -- refuted, not deferred. ### W-ORD-REACH-BAR filed. ### The"
     " registration was sealed with a banned stem in it and then RE-SEALED, superseded hash in"
     " the block. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b319_the_stable_rank.txt; data/b319_coverage_repair.txt; data/b319_pin.txt;"
     " CORRESPONDENCE.md row 151"),
    # ### THE SQUARE (b318).
    ("forced-sign", "b318 (a computation on the instrument as certified)",
     "the source's trace side in its square form, computed on the truncation. ### The paper"
     " says where its positivity lives: the functional is positive definite BY CONSTRUCTION"
     " only when evaluated at f = g conv g^, where it is Tr(theta(g) S theta(g)^) -- a"
     " Hilbert-Schmidt norm squared. ### **CELLS AT WHICH THAT SQUARE IS NEGATIVE ANYWHERE:"
     " 0. ### CELLS AT WHICH b317's SMEAR IS NEGATIVE ANYWHERE: 5.** ### **AND THE FIRST"
     " DIFFERING CONSTITUENT IS PROVED, NOT ASSERTED**: theta(f)^theta(f) = theta(f^ conv f),"
     " so the source's square form is the corpus's smear at the AUTOCORRELATION of the window"
     " where the corpus evaluates it at the window -- two independent code paths agreeing to"
     " 1.9e-06, 4.2e-06 and 3.4e-05 against a sealed bar of one per cent",
     "### ONE STATEMENT HERE IS FINITE-DECIDABLE AND THE ACT SAYS WHICH. ### The square is a"
     " Frobenius norm squared and **square_trace PERFORMS NO SUBTRACTION ANYWHERE**, so its"
     " nonnegativity is arithmetic; **WHAT IS NOT DECIDABLE IS THAT THE SUM IS THE"
     " OPERATOR-THEORETIC NORM**. ### **A POSITIVITY THAT HELD IS NOT A THEOREM CONFIRMED** --"
     " the source proved it; this act checked the truncation does not destroy it. ### **THE"
     " REACH IS EMPTY, 0 OF 6**, and the noise-floor gate REFUSES 6 pairs of 12, all on the"
     " domain axis. ### **THE RANK IS THE GRID-AXIS ERROR, MEASURED**: steps that keep the"
     " rank drift 2.7e-05 to 1.2e-04, the one that changes it (80 to 79) drifts 6.1e-03 to"
     " 2.3e-02. ### W-ORD-RANK-STABLE-SUBSPACE filed; the scheme is SPECIFIED and NOT BUILT."
     " ### **NO UNIT USED. ### W_infinity NOT COMPUTED IN ANY DIRECTION.** ### NO GRADE MOVED."
     " ### M-2 UNCHANGED",
     "data/b318_the_forced_sign.txt; data/b318_components_run.txt;"
     " tools/b318_square.py (the emitting file); CORRESPONDENCE.md row 148"),
    # ### THE LETTER (b318), AND WHAT IT DOES TO b317's SIGN CHANGE.
    ("forced-sign", "b318 (the class of the window, decided)",
     "the corpus's window is a candidate g and NOT a candidate f. ### Decided by the source's"
     " own Definition 3.1 -- f is positive definite when its Fourier transform is pointwise"
     " positive -- applied as a scan at every banked cell. ### **THE MEAN-ZERO VARIANT IS NOT"
     " POSITIVE DEFINITE AT ANY CELL (min f-hat = -1.3119e-01), AND NEITHER IS THE CORPUS'S"
     " INTEGRAL-ONE BUMP (-9.8392e-02): 0 OF 13 FOR BOTH.** ### But Theorem 1 puts its"
     " conditions on g, not on f -- support in [2^-1/2, 2^1/2] and Fourier transform vanishing"
     " at i/2 AND at 0 -- and **THE VARIANT SATISFIES BOTH VANISHING CONDITIONS AT 13 OF 13"
     " AND THEOREM 1's SUPPORT INTERVAL AT 3 OF 13 (a = 1.3, 1.35, 1.41)**",
     "### A DEFINITIONAL FINDING THAT DISSOLVES b317's ANOMALY RATHER THAN RESOLVING IT."
     " ### **THE SIGN CHANGE IS NOT A VIOLATION OF ANYTHING**: the source's positivity is"
     " about Tr(theta(g) S theta(g)^), which stayed positive everywhere, and Tr(theta(f) S) at"
     " an f outside the class carries no promise. ### **b317's NUMBERS ARE RE-LABELLED AND"
     " b317 IS NOT RE-VERDICTED** -- correctly computed values of what it computed; its grade"
     " does not move and its prediction score stands as it stated it. ### The class scan proves"
     " the NEGATIVE only, and the act uses it in that direction alone. ###"
     " W-ORD-WINDOW-CLASS UPDATED, not closed: the question is now WHICH LETTER, and what is"
     " owed is the author's decision. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b318_the_forced_sign.txt; data/b318_rows.json;"
     " data/b318_extract_notes.txt (the source, located); CORRESPONDENCE.md row 149"),
    # ### THE NUMBER (b317, act two of two).
    ("trace-on-the-object", "b317 (a computation on the instrument as certified)",
     "the source's compressed smeared trace, computed on the object's own space. ###"
     " **Tr(theta(f) S) OF THEOREM 4.7, ASSEMBLED FROM eq. (61) AND DEFINITION 4.4 ALONE** --"
     " the scaling action integrated in d*lambda, which by u = x/lambda is the kernel"
     " K(x,u) = f(x/u)/sqrt(xu), compressed by b316's projector and traced. ### Thirteen"
     " banked cells, both test functions, the whole registered cutoff. ### **AGAINST A BAR"
     " SEALED BEFORE ANY VALUE AT ANY BANKED CELL EXISTED (|T| <= |A|/10, scored on the"
     " largest |T| the whole domain sweep produces), THE REGISTERED PREDICTION SCORES AS SMALL"
     " AT 13 CELLS OF 13** -- ratios 0.09318 down to 0.00019, with the narrowest cell at 93"
     " per cent of the bar. ### **AND THE CANCELLATION IS THE BUMP'S OWN, NOT THE"
     " COMPRESSION'S**: the same compression removes 98.6 per cent of the bump's uncompressed"
     " trace and only 55 per cent of the mean-zero variant's",
     "### A NUMBER ON A TRUNCATION, AND ITS LIMITS BELONG IN ITS OWN ENTRY. ### **THE REACH IS"
     " EMPTY** -- no cell meets the joint 5 per cent bar fixed before the run -- ### **AND THE"
     " NOISE-FLOOR GATE REFUSES 8 PAIRS OF 12**, so no point verdict is taken from either"
     " axis and the scoring is a BAND statement. ### The grid-axis drift spike is a RANK STEP"
     " (80 to 79), not a quadrature error. ### **NO UNIT IS USED ANYWHERE IN THE ACT** and the"
     " number MAY NOT BE READ AS b300's -- W-ORD-ARCH-MEMBERSHIP is open. ### NO ACT"
     " RE-VERDICTED. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b317_the_trace_on_the_object.txt; data/b317_components_run.txt;"
     " tools/b317_smear.py (the emitting file); CORRESPONDENCE.md row 146"),
    # ### THE LINK THE NUMBER BROKE (b317).
    ("trace-on-the-object", "b317 (the sign chain's fifth link, measured)",
     "the corpus's window is NOT the source's test-function class. ### b316 registered its"
     " prediction on a chain of five and named each as a way for it to be wrong for a reason"
     " that has nothing to do with the mathematics. ### Four this act cannot touch. ###"
     " **THE FIFTH IT MEASURED, AND THE FIFTH IS FALSE**: the source's eq. (54) requires the"
     " moment INT f(rho) rho^{+-1/2} d*rho to vanish, and the corpus's integral-one bump has"
     " it at 1.003, 1.010 and 1.024 at a = 1.5, 2, 3. ### **AND FIVE OF THE THIRTEEN CELLS"
     " ALSO LEAVE eq. (53)'s SUPPORT CONDITION [1/2, 2].** ### A mean-zero variant built from"
     " three of the corpus's own bumps DOES satisfy both moments, to 2.8e-17",
     "### A MEASUREMENT ABOUT A WINDOW, NOT A VERDICT ON AN ACT. ### **A PREDICTION WHOSE"
     " NUMBER LANDS WHILE A LINK IT RESTS ON IS MEASURED WRONG HAS NOT BEEN CONFIRMED BY THE"
     " LANDING** -- so the prediction SCORED and is NOT CONFIRMED, and the entailment is"
     " bounded: the correspondence may not be read as identifying the corpus's window with the"
     " source's class, because that is the thing this act refused. ### **NO ACT IS"
     " RE-VERDICTED AND NO BANKED MEASUREMENT IS CALLED WRONG** -- naming two quantities"
     " different is a statement about what they are. ### W-ORD-WINDOW-CLASS filed. ### NO"
     " GRADE MOVED. ### M-2 UNCHANGED",
     "data/b317_the_trace_on_the_object.txt; data/b317_rows.json;"
     " data/b316_the_archimedean_instrument.txt (the chain's own bank);"
     " CORRESPONDENCE.md row 147"),
    # ### THE INSTRUMENT (b316, act one of two).
    ("archimedean-instrument", "b316 (an instrument build, with its own fixtures)",
     "a computable truncation of the source's own archimedean space. ### **S(1,1) BUILT FROM"
     " DEFINITION 4.4 AND NOTHING ELSE** -- even functions on [0, X] at N midpoints, with the"
     " source's inner product (eq. 16), transform normalization (eq. 24), scaling exponent"
     " (eq. 61) and two vanishing conditions (eq. 72) as linear constraints. ### **THE FIRST"
     " ARCHIMEDEAN INSTRUMENT THE CORPUS HAS WHOSE VECTORS ARE INSIDE THE OBJECT'S OWN"
     " SPACE.** ### Dimension 914, 1904, 3888, 3887, 5870 at five truncations and GROWING"
     " WITHOUT BOUND, which is the source's *infinite dimensional Sonin's space* appearing as"
     " a measurement. ### **AND THE SOURCE'S SECOND SENTENCE SHARPENED**: the paper says the"
     " scaling action does not restrict; the instrument says WHICH condition breaks --"
     " condition one survives EXACTLY at every dilation, and the whole failure is in the"
     " transform condition, leaking 0.1352 at lambda 1.25 up to 0.4253 at lambda 4",
     "### AN INSTRUMENT BUILD, AND ITS LIMITS BELONG IN ITS OWN ENTRY. ### **IT CAN decide"
     " exactly that a vector supported in the unit interval is orthogonal to the space, and"
     " that condition one survives any dilation at or above one; measure how far a vector"
     " lies outside, with a discrimination arm that FIRES; measure the scaling leakage; apply"
     " the compression; accept either test function.** ### **IT CANNOT DECIDE MEMBERSHIP**"
     " (the next entry), converge to a fixed finite answer under refinement, separate a"
     " truncation effect from a construction effect, or say anything about the p-adic places"
     " -- b285's boundary stands and b309's zero does not travel. ### **NO TRACE COMPUTED AND"
     " NO SMEAR ASSEMBLED**: that is act two, under its own registration. ### NO GRADE MOVED."
     " ### M-2 UNCHANGED",
     "data/b316_the_archimedean_instrument.txt; data/b316_components_run.txt;"
     " tools/b316_instrument.py (the emitting file); CORRESPONDENCE.md row 144"),
    # ### THE REPRODUCTION ARM, AND THE ONE THAT DID NOT CONFIRM (b316).
    ("archimedean-instrument", "b316 (the mandatory reproduction arm)",
     "what the instrument reproduces of what the record already owns. ### **b292 CONFIRMED BY"
     " A SECOND AND INDEPENDENT ROUTE**: the corpus's expansion vectors zeta_n pass condition"
     " one and fail condition two with residual 1.0000 at n = 0,1,2,3 and at every"
     " truncation, where b292 derived the same failure from the source's statement about"
     " psi_n. ### The source's own worked inner product RECOVERED to 0.00e+00. ### **AND"
     " b300's MEMBERSHIP IS *NOT* CONFIRMED**: the derived archimedean unit, built on this"
     " grid by the corpus's own solver, has residual 0.9455, 0.8023, 0.5527, 0.6033, 0.4902"
     " across five truncations -- falling with the domain and nowhere near zero. ### The hard-"
     " cutoff explanation was TESTED AND REFUSED (a smooth taper moves 0.8023 to 0.8020)",
     "### A REPRODUCTION ARM, AND ONE OF ITS FOUR DID NOT CONFIRM. ### **b300 IS NOT"
     " RE-VERDICTED AND IS NOT CALLED WRONG** -- b300's derivation is on the WHOLE LINE and"
     " this is a truncation, and b15's law governs: a finite-place-set object at a finite"
     " cutoff decides nothing global. ### **AND THE CONTROL THAT WOULD HAVE SETTLED THE"
     " CONSTRUCTION COULD NOT FIRE**: the asymptotic check confirms the decay and frequency"
     " but returns 1.1435 and 1.1558 at two NON-eigenvalues against the eigenvalue's 1.1323,"
     " so by b308's law it is reported as NOT-A-CHECK. ### **THREE CAUSES REMAIN AND THIS ACT"
     " CHOOSES NONE.** ### **THE INSTRUMENT IS DECLARED NOT YET CERTIFIED FOR MEMBERSHIP AND"
     " ACT TWO MAY NOT USE IT FOR ONE**; W-ORD-ARCH-MEMBERSHIP filed. ### NO GRADE MOVED. ###"
     " M-2 UNCHANGED",
     "data/b316_the_archimedean_instrument.txt; data/b316_rows.json;"
     " data/b300_the_archimedean_leg.txt (b300's own bank); CORRESPONDENCE.md row 145"),
    # ### THE CALIBRATION READ (b315).
    ("calibration", "b315 (a read at content, at the operation)",
     "the atlas's calibration read AT THE OPERATION, not at the comment. ### **A IS COMPUTED"
     " AT carto_atlas.py:66 AS AN EXPLICIT INTEGRAL OF THE DIGAMMA KERNEL AGAINST THE TEST"
     " FUNCTION, DIVIDED BY 2 pi -- no free constant, no fitted factor, and nothing from any"
     " remainder in it**; the calibration settles the ORIENTATION with which that term enters"
     " the explicit formula, tested at line 117 by abs(residual) <= TOL on Z - (P - PR + A)."
     " ### **AND THAT RESIDUAL CONTAINS NO REMAINDER AT ALL: the E2 in the bracket is the"
     " name of a REGISTERED CLAIM (E1-E4), NOT the archimedean remainder E2 of b38's"
     " identity.** ### **SO THE NEAR-CANCELLATION A + E2 ~ 0 UNDER THE SOURCE'S CONVENTION IS"
     " NOT PRODUCED BY THE CALIBRATION: IT SURVIVES**, worst modulus 0.022509, 1.13% of the"
     " largest modulus of A in the table",
     "### A READ, AND A CORRECTION TO A REASON. ### **b312's SENTENCE AND b313's CAUTION"
     " RESTED ON ONE NAME FOR TWO OBJECTS -- the double-name species b200 named and b219"
     " realised -- AND NEITHER ACT IS RE-VERDICTED.** ### Their numbers stand; b313's REFUSAL"
     " to interpret the column ALSO STANDS, on a stronger ground: not *it might be the"
     " calibration* but **no definition has been stated that would make it mean anything**."
     " ### **A CORRECTION THAT REMOVES A CAUTION IS NOT A LICENCE TO INTERPRET**, and A + E2"
     " is promoted to nothing. ### The independence check runs over the ENCLOSING FUNCTION and"
     " is shown able to find a dependence when one is there. ### NO GRADE MOVED. ### M-2"
     " UNCHANGED",
     "data/b315_the_calibration_and_the_rate.txt; data/b315_components_run.txt;"
     " tools/e16/carto_atlas.py (the emitting file); CORRESPONDENCE.md row 142"),
    # ### THE RATE UNDER THE SOURCE'S EXPONENT (b315).
    ("rate-corrected", "b315 (a derivation, with the bench as its check)",
     "b264's Cauchy-Schwarz-and-Plancherel route re-run with the corrected exponent. ###"
     " **EVERY STEP SURVIVES BUT THE PREFACTOR**: Cauchy-Schwarz bounds the INTEGRAL and the"
     " exponent multiplies it. ### **SO THE MODULUS OF eps_even^src(rho) IS AT MOST C_even ="
     " 132.781908429 -- THE SAME CONSTANT, WITH NO POWER OF rho AT ALL.** ### The sharp rate"
     " keeps its constant and loses one power: **rho^(1/2) eps_even^src -> K_even ="
     " 1.568231065**. ### And along the CUTOFF, by b264's own dilation route (cited, not"
     " re-claimed): **THE EVEN SECTOR STILL VANISHES AT THE SAME LEADING ORDER 1/log a, AND"
     " ONLY THE CONSTANT CHANGES**, because the measure drho/rho absorbs exactly the one power"
     " the flip introduces",
     "### A DERIVATION, AND WHAT IT REPORTS IS A LOSS. ### **THE NEW ENVELOPE IS NOT MERELY"
     " LOOSE, IT IS VACUOUS IN THE LIMIT** -- about 168x above the value at its tightest"
     " converged cell, and getting looser without bound. ### b264 used the old envelope to"
     " CARRY THE TAIL; **a constant is not integrable against drho/rho, so the cutoff constant"
     " has a measured body and NO RIGOROUS TAIL BOUND from this route.** ### The ORDER is"
     " derived and unchanged; the CONSTANT is not certified. W-ORD-SOURCE-TAIL filed. ###"
     " Convergence decided by b264's OWN TWO-AXIS TEST, not a ceiling number. ### **THE"
     " BEARING ON b262's BRANCH IS A BEARING ONLY** -- one archimedean OBJECT is not the"
     " archimedean SIDE, and b242's law governs: a measured rate is not a tail bound. ### M-2"
     " UNCHANGED",
     "data/b315_the_calibration_and_the_rate.txt; data/b315_rows.json;"
     " data/b264_eps_even_decay.txt (the route's owner); CORRESPONDENCE.md row 143"),
    # ### THE INSTRUMENT ARC FOLDED (b314).
    ("the-instrument-arc", "b314 (a filings act)",
     "seven acts -- b307 through b313 -- filed into PLACE-papers/FINDINGS.md as **THE"
     " INSTRUMENT ARC, b307-b313 -- THE FOLD**. ### **14 QUOTATIONS, 0 UNFINDABLE, EVERY ONE"
     " CHECKED AGAINST THE ACT THAT ORIGINATED IT BEFORE EMISSION**, with a discrimination"
     " arm requiring an ALTERED quotation back unfindable. ### FINDINGS.md +100 / -0. ###"
     " The arc as one statement: at a finite place the source's construction returns the test"
     " function at one point times a dimension and carries no arithmetic; the mechanism"
     " producing that silence DOES NOT TYPE at the archimedean place; and the corpus's"
     " remainder is NOT the source's function, differing by a factor of rho whose correction"
     " accounts for 8% to 19% of the residue and no more. ### The author's CONVENTION"
     " ERRATUM ruling executed: ERRATA.md entry **E-2026-09-03-1**, internal record, +28 / -0",
     "### A FILINGS ACT. ### **NO GRADE MOVES, NO ACT IS RE-VERDICTED, AND NOTHING IN THE"
     " SECTION IS NEW MATHEMATICS.** ### Additivity MEASURED by `git diff --numstat`, not"
     " asserted. ### Five falsifiers, all DID NOT FIRE. ### **THE OWNER INSTRUMENT FILES STAY"
     " BYTE-IDENTICAL**, checked before and after the errata entry, on the E1 precedent:"
     " THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF. ### The entry carries a standing"
     " clause -- **a banked remainder value is quotable only with its convention named**. ###"
     " **NOTHING ABOUT THE IDENTITY, h2, OR THE ROSTER FOLLOWS**; the vectors-outside-the-"
     " object hypothesis is NAMED AS A HYPOTHESIS and tested by no act in the arc. ### M-2"
     " UNCHANGED",
     "data/b314_the_fold_and_the_cold_clone.txt; data/b314_fold_emitted.md;"
     " PLACE-papers/FINDINGS.md; PLACE-papers/ERRATA.md E-2026-09-03-1;"
     " CORRESPONDENCE.md row 140"),
    # ### THE KERNEL FROM A COLD CLONE, AND THE COVERAGE ANSWER (b314).
    ("the-cold-clone", "b314 (a certification test)",
     "the kernel repository cloned FRESH from origin at its current pin onto a path outside"
     " the corpus, by the tool itself, and rebuilt from source. ### **build/ IS .gitignored,"
     " SO THE CLONE ARRIVED WITH ZERO COMPILED ARTEFACTS -- THERE WAS NO CACHE TO BE STALE.**"
     " ### elan resolved **v4.29.1 INSIDE the clone against v4.33.1 OUTSIDE it**. ### **84"
     " MODULES ELABORATED FROM SOURCE IN DEPENDENCY ORDER, 0 FAILURES**, AllPrints.lean"
     " re-run, and the regenerated profile compared against the banked blob at HEAD: **RAW"
     " BYTE EQUALITY -- 33195 bytes each, 475 prints, 475 zero-axiom, 0 differing lines, no"
     " byte-order mark and no CRLF on either side.** ### **AND THE COVERAGE QUESTION HAS AN"
     " ANSWER AND IT IS *FOUND*: 25 Core modules sit outside AllPrints.lean, all 25"
     " elaborate, and 91 #print axioms targets in them are NOT IN THE PROFILE AT ALL**",
     "### A CERTIFICATION TEST, AND NOTHING IS REPAIRED BY IT. ### **A COLD CACHE AND A COLD"
     " CHECKOUT ARE NOT A COLD MACHINE** -- one repository, one machine, that machine's own"
     " elan store, OS and CPU; NOT evidence that the corpus reproduces from a clone in"
     " general. ### **IT DOES NOT CONCLUDE THAT THE UNCERTIFIED TERMINALS ARE WRONG, OR"
     " RIGHT** -- a terminal that elaborates with zero axioms is not thereby a terminal worth"
     " certifying. ### The reason is structural: **AllPrints.lean IS A HAND-MAINTAINED IMPORT"
     " LIST AND NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF IT.** ### The first"
     " sweep carried two defects, both this act's own and both declared -- alphabetical order"
     " reported a module as FAILING when its dependency was simply not built yet. ### NO"
     " .lean FILE CREATED OR EDITED; NO MODULE ADDED TO THE CERTIFICATION FILE. ### M-2"
     " UNCHANGED",
     "data/b314_the_fold_and_the_cold_clone.txt; data/b314_coldclone_run.txt;"
     " data/b314_coldclone_rows.json; data/b314_coldrelay_run.txt;"
     " CORRESPONDENCE.md row 141"),
    # ### THE RESIDUE IS NOT THE EXPONENT (b313).
    ("the-exponent", "b313 (a computation, and a negative one)",
     "b312 identified the corpus's archimedean remainder as differing from the source's by a"
     " factor of rho; **THIS ACT RAN THE CHECK b312 FILED AND THE RESIDUE DID NOT COLLAPSE.**"
     " ### In a COPY of the instrument -- the owner files untouched -- the remainder side was"
     " recomputed under the source's exponent, everything else byte-identical."
     " ### **resid = Tr - A - E2 FELL FROM (4.0486, 3.3740, 3.0478, 2.5208, 2.4540, 2.3134)"
     " TO (3.7150, 2.9792, 2.6347, 2.0917, 2.0242, 1.8834)** at a^2 = 2, 3, 4, 8, 9, 12 --"
     " ratios 0.9176 to 0.8141, a shrinkage of 8% to 19% with the order of magnitude kept at"
     " every cell. ### **A AND Tr DO NOT MOVE AT ALL**, measured and not asserted",
     "### A MEASUREMENT, AND A NEGATIVE ONE. ### **IT DOES NOT MEAN THE FLIP WAS WRONG: the"
     " exponent is fixed by the source's own definition and by NOTHING the residue does, and"
     " b312 decided which function the remainder IS by unfolding definitions.** ### **NO"
     " BANKED NUMBER IS CALLED WRONG, NO ACT IS RE-VERDICTED, NO GRADE MOVED, NO TARGET WAS"
     " NAMED AND NO FIT WAS PERFORMED.** ### Controls: the transcribed loop reproduces b38's"
     " month-old banked table to 4.98e-05 (its own display rounding); the copy with the"
     " exponent RESTORED reproduces the owner 78/78 BITWISE; the flip is a pointwise rho"
     " factor to 5.55e-16. ### The third and fourth face-offs are NOT re-read. ### M-2"
     " UNCHANGED",
     "data/b313_the_exponent.txt; data/b313_components_run.txt; data/b313_flip_run.txt;"
     " CORRESPONDENCE.md row 138"),
    # ### WHAT THE CONVENTION DOES ACCOUNT FOR (b313).
    ("convention-share-of-the-residue", "b313 (a measurement at six cells)",
     "the flip is **EXACTLY MULTIPLICATION BY rho**, measured to 5.55e-16 across all 240 grid"
     " points, so every consequence is a one-power shift. ### b264's ladder, re-run under the"
     " flip at its own reach with the noise-floor gate in the path (NRES = 7; even floor modes"
     " 8 and 10, and what excluding them removes PRINTED at 1e-11 to 1e-15): **the even"
     " sector's decay moves from rho^(-3/2) to rho^(-1/2) and b264's measured leading constant"
     " does not move at all** -- the two scaled columns agree to 1.09e-11 at every cell. ###"
     " **AND THE BANKED CROSS-CHECK IS SHOWN INSENSITIVE, AS b312 DERIVED**: eps'(1+) is"
     " BITWISE identical under both conventions",
     "### AN INSTRUMENT FINDING, ROUTED AND NOT FILED. ### **SCOPE: the convention mismatch"
     " accounts for BETWEEN 8% AND 19% OF THE RESIDUE AT SIX CELLS. ### IT DOES NOT ACCOUNT"
     " FOR THE REST, AND NOTHING HERE SAYS WHAT DOES.** ### Routed to the author as an"
     " ERRATA-class candidate on the E1 precedent (E-2026-08-31-1): the owner files untouched,"
     " the correction of record in the bank, because THE RECORD DOES NOT SILENTLY OVERWRITE"
     " ITSELF. ### **WHAT IT WOULD AFFECT IF FILED: every banked number through those three"
     " call paths is a computation of the corpus's own function rather than the source's -- A"
     " STATEMENT ABOUT WHAT THE NUMBERS ARE COMPUTATIONS OF, NOT A CLAIM THAT ANY IS WRONG.**"
     " ### W-ORD-A-PLUS-E2 and W-ORD-CONVENTION-SWEEP filed. ### M-2 UNCHANGED",
     "data/b313_the_exponent.txt; data/b313_rows.json; data/b264_rows.json (the reference"
     " ladder); CORRESPONDENCE.md row 139"),
    # ### THE REMAINDER IS NOT THE SOURCE'S (b312).
    ("the-remainder", "b312 (a decision at definitions)",
     "the corpus's eps and CC's epsilon unfolded to their base objects and compared"
     " constituent by constituent, artefact pinned by sha256 b8e0b54a... BEFORE a word of it"
     " was read. ### **NINE CONSTITUENTS; EIGHT AGREE EXACTLY** -- mode family, auxiliary"
     " vector, analytic continuation, the coefficient lam^2/(1-lam^2), the interval from"
     " 1/rho to 1, the integrand, the value zero at the identity, and the one-sided"
     " derivative. ### **THE NINTH IS THE SCALING ACTION'S NORMALIZATION EXPONENT AND IT"
     " DISAGREES**: CC's eq (61) defines theta(lam)xi(v) := lam^(-1/2) xi(lam^-1 v), unitary,"
     " so at the remainder's argument it is rho^(+1/2), and CC's Lemma 5.4 proof writes that;"
     " the corpus declares theta(a)f(x) = a^(1/2) f(x/a) and its code applies r ** -0.5. ###"
     " **THE TWO FUNCTIONS DIFFER BY A FACTOR OF rho, WHICH IS NOT A SCALAR. ### VERDICT:"
     " DIFFERENT**",
     "### A DECISION AT DEFINITIONS. ### **THIS ACT COMPARED TWO WRITTEN DEFINITIONS AND"
     " COMPUTED NO ARCHIMEDEAN NUMBER. ### IT DOES NOT CALL ANY BANKED MEASUREMENT WRONG, AND"
     " EVERY BANKED RESULT STANDS WHERE ITS OWN ACT LEFT IT.** ### The decision is made by"
     " EXTRACTION (tools/b312_definitions.py, fixtures proving it can report either answer),"
     " because the corpus's own flattener strips non-alphanumerics and cannot see a sign. ###"
     " **THE SOURCE IS SELF-CONSISTENT AT THREE INDEPENDENT PLACES; THE CORPUS DISAGREES WITH"
     " ITSELF** -- its Qeps carries r ** 0.5, matching CC's eq (99), and inside b38_act10.py"
     " the identity's trace side and its remainder side carry opposite exponents. ### The"
     " corpus's stated reason does not reach its conclusion: a support condition fixes a"
     " DOMAIN, not an AMPLITUDE. ### **THE ENTAILMENT DOES NOT RUN** (ordered on SAME only)."
     " ### M-2 UNCHANGED",
     "data/b312_the_remainder.txt; data/b312_components_run.txt; data/b312_source_pin.txt;"
     " CORRESPONDENCE.md row 136"),
    # ### A CHECK TAKEN AT A ZERO CANNOT SEE A FACTOR (b312).
    ("remainder-check-at-a-zero", "b312 (a derivation at definitions)",
     "the corpus's ONE cross-check of its remainder against the source is the one-sided"
     " derivative at the identity, which its header derives and CC's Lemma 5.4 states; the two"
     " agree, and **THE AGREEMENT IS EMPTY**. ### Writing the common integral as F(rho), the"
     " corpus's function is rho^(-1/2) F(rho) and the source's rho^(+1/2) F(rho); the interval"
     " is empty at the identity so F(1) = 0, and the derivative of rho^s F(rho) there is"
     " s F(1) + F'(1) = F'(1) **FOR EVERY s WHATEVER**. ### **A CROSS-CHECK TAKEN AT A ZERO OF"
     " THE FUNCTION CANNOT SEE A MULTIPLICATIVE FACTOR THAT IS FINITE AND NONZERO THERE**",
     "### A DERIVATION ABOUT WHERE A CHECK WAS TAKEN -- NEITHER AN EXCUSE NOR AN ACCUSATION."
     " ### **IT EXPLAINS WHY ONE CHECK WAS INSENSITIVE TO ONE FACTOR; IT IS NOT A CLAIM ABOUT"
     " ANY OTHER CHECK THE CORPUS RAN, AND IT AUDITS NONE OF THEM.** ### The other channel was"
     " checked as ordered: carto_atlas.py fixes its archimedean sign BY THE E2 CALIBRATION and"
     " disclaims any sign claim, **SO THE THING TO BE CHECKED AGAINST IS ITSELF A"
     " CALIBRATION** -- not a complaint about the atlas, which has always disclaimed it. ###"
     " **W-ORD-REMAINDER-EXPONENT IS FILED, NOT RUN**, with its exact check named: re-run the"
     " corpus's identity with the remainder's exponent flipped and nothing else touched, and"
     " compare the residue -- **A COMPUTATION THIS ACT MAY NOT RUN**. ### It inherits"
     " W-ORD-ARCH-NORM-READING (b301), still live. ### NO GRADE MOVED. ### M-2 UNCHANGED",
     "data/b312_the_remainder.txt; tools/e16/carto_atlas.py (the calibrated sign);"
     " data/b301_the_object_completed.txt; CORRESPONDENCE.md row 137"),
    # ### THE SOURCE'S PROOF READ (b311).
    ("identity-neighbourhood", "b311 (a read at content, under the import bar)",
     "CC 2006.13771v1 read at content, artefact pinned by sha256 b8e0b54a... BEFORE a word of"
     " it was read. ### **THE SOURCE DOES NOT EVALUATE THE COMPRESSED TRACE AT INDIVIDUAL"
     " SCALINGS**: it gives the single-scaling trace FORMALLY (Prop 1.5(ii)) and recovers"
     " trace class ONLY after smearing (Prop 1.5(iv)); it isolates a trace-remainder delta"
     " (Def 2.1) and notes that, unlike tau which 'is not a function because of the divergency"
     " at rho = 1', delta IS a function with a JUMP IN ITS FIRST DERIVATIVE at rho = 1; and it"
     " turns that jump into Theorem 3.6's -2 Id + K_I with K_I compact. ### **AND THEOREM 4.7"
     " PINS THE TRACE SIDE TO THE DISTRIBUTION: Tr(theta(f)S) = W_inf(f) + INT f(rho^-1)"
     " eps(rho) d*rho with eps a FUNCTION** -- so the only part of the trace side that is not"
     " an integral against a function is the part at the identity",
     "### AN IMPORT, READ AT CONTENT, AT THE IMPORT BAR. ### **THIS ACT READ STATEMENTS AND"
     " THEIR STATED ROLES; IT VERIFIED NO PROOF OF THE SOURCE'S, AND NOTHING HERE IS EVIDENCE"
     " THAT ANY OF THEM IS CORRECT.** ### 20 fragments located by tools/b311_source.py, 0"
     " unlocated, across pages 1, 2, 8, 10, 11, 12, 13, 18, 26, 27, 47; the tool LOCATES and"
     " does not read. ### **WHAT DOES NOT FOLLOW: that the source's result is ABOUT THE"
     " IDENTITY ALONE** -- eps is not nothing and Theorem 3.6 is about a quadratic form on an"
     " INTERVAL. ### **NO ARCHIMEDEAN NUMBER IS COMPUTED.** ### M-2 UNCHANGED",
     "data/b311_the_identitys_neighbourhood.txt; data/b311_components_run.txt;"
     " data/b311_source_pin.txt; CORRESPONDENCE.md row 134"),
    # ### THE MECHANISM DOES NOT TYPE AT INFINITY (b311).
    ("arch-mechanism-untyped", "b311 (a decision at definitions, and a price)",
     "b310 closed the finite side with one sentence -- Tr(theta(t)Pi) is a SIGNED COUNT of the"
     " off-ball points t fixes. ### **THIS ACT DECIDES, BY DEFINITIONS, THAT IT DOES NOT TYPE"
     " AT THE ARCHIMEDEAN PLACE, AND THE STEP AT WHICH IT PARTS IS THE DIMENSION OF THE"
     " OBJECT'S SPACE**: finite-dimensional at a finite place (a truncation, so theta(t)Pi is"
     " finite rank and the trace is an integer count the first condition kills), and INFINITE"
     " at infinity in CC's own words -- so the single-scaling compression is not trace class"
     " and THERE IS NO COUNT TO TAKE. ### In both cases the map fixes only the origin and the"
     " origin lies in the excluded region, but **the finite local term is an EVALUATION and"
     " the continuous one is a JACOBIAN, and a vanishing condition acts on the first and not"
     " on the second**",
     "### A REFUSAL, NOT A NEGATIVE RESULT. ### **A STATEMENT ABOUT TYPES -- that a question"
     " answered on one side does not parse on the other -- AND THE CORPUS HAS DONE NO"
     " MATHEMATICS AT INFINITY HERE.** ### The navigator's second expectation is REFUTED in"
     " its first half (the compression has NO trace, and where its formal value is a function"
     " it is nonzero) and CONFIRMED in its diagnosis (the difference lives at the identity)."
     " ### **THE RESEMBLANCE BETWEEN A DISCRETE COUNT AND A CONTINUOUS WEIGHT IS NAMED AND"
     " REFUSED AS EVIDENCE; no bridging definition is exhibited or claimed** -- b285's hazard"
     " register named the species: THE WORD SURVIVES; THE OBJECT DOES NOT. ### The price of an"
     " archimedean instrument is typed and estimated at three acts for the truncation and two"
     " for the compression, ONLY IF W-ORD-ARCH-NORM-READING is settled first -- an estimate,"
     " not a commitment. ### The author's W2 window ruling is RECORDED AND NOT APPLIED. ### NO"
     " BRANCH DECIDED. ### M-2 UNCHANGED under its cap",
     "data/b311_the_identitys_neighbourhood.txt; data/b285_archimedean_opening.txt (the hazard"
     " register); data/b310_the_smear_collapses.txt; CORRESPONDENCE.md row 135"),
    # ### THE SMEAR COLLAPSES (b310).
    ("smear-collapse", "b310 (a computation and a derivation)",
     "the source's own construction -- 'one can associate to a test function f the trace"
     " Tr(theta(f) S)' -- assembled on the b308 instrument. ### **AT A FINITE PLACE THE"
     " SCALING PART OF Q_p^x IS p^Z, WHICH IS DISCRETE**, so the source's integral over it is"
     " a SUM over the powers of the prime with the test function evaluated at those powers:"
     " T(w) = SUM over k of w_k Tr(theta(p^k) Pi). ### The weight is SYMBOLIC -- no bump is"
     " chosen, so no class question arises and no price is paid -- and the sum is finite"
     " because the source's test functions are compactly supported. ### **WITH b309's ZEROS AT"
     " EVERY NONZERO POWER, EXACTLY ONE TERM SURVIVES: T(w) = w_0 (p^n - 1)^2.** ### Seven"
     " cells, every carried power, 0 terms surviving away from the identity; the zeros are NOT"
     " substituted in -- every term is formed and added",
     "### A COMPUTATION AND A DERIVATION, general in p, n and the weight, with the seven-cell"
     " table as the CHECK and not the proof. ### **THE SURVIVING TERM CONTAINS THE WEIGHT AT"
     " THE IDENTITY AND THE CONSTRAINED DIMENSION, AND NOTHING ELSE: NO log p, NO SAMPLING AT"
     " THE PRIME'S POWERS, NO DEPENDENCE ON THE WEIGHT AWAY FROM THE IDENTITY** -- measured"
     " with a tail nonzero at every carried power, and with the discriminating arm beside it."
     " ### **SCOPE: this is what the construction returns AT A FINITE PLACE, ON THIS OBJECT,"
     " IN THIS COMPRESSION. ### THE SOURCE WORKS AT THE ARCHIMEDEAN PLACE, WHERE THE GROUP IS"
     " CONTINUOUS AND NONE OF THIS DERIVATION APPLIES** -- named, not derived; b285's boundary"
     " stands. ### b309's zero is CARRIED, not re-derived. ### Two terminals, zero axioms,"
     " certifying ARITHMETIC and NOT the collapse. ### NO AGGREGATION IS STATED. ### M-2"
     " UNCHANGED",
     "data/b310_the_smear_collapses.txt; data/b310_components_run.txt;"
     " SIDE-global-section/Core/SmearCollapseShadow.lean; CORRESPONDENCE.md row 132"),
    # ### THE FIXED-POINT SENTENCE AND ITS BEARING (b310).
    ("fixed-point-silence", "b310 (a derivation, and a bearing that is never a decision)",
     "b304 computed the COMPACT part of the local multiplicative group and found its smear"
     " over the units zero; b309 computed the SCALING part and found it zero at every nonzero"
     " power. ### **THOSE ARE ONE STATEMENT: Tr(theta(t) Pi) IS A SIGNED COUNT OF THE OFF-BALL"
     " POINTS t FIXES, IN THE TWO CONGRUENCES THE OBJECT'S TWO CONDITIONS IMPOSE, WEIGHTED BY"
     " THE EMBEDDING'S HAAR FACTOR.** ### At t = 1 every off-ball point is fixed and the count"
     " is (p^n - 1)^2; at a nonzero power NOTHING off the ball is fixed, because p^k - 1 is a"
     " unit, and the only point fixed is the one place the object must vanish. ### **AT A UNIT"
     " OTHER THAN 1 THE COUNT IS GENERALLY NONZERO -- b304's zero is the SUM over the units,"
     " not a per-unit vanishing, and the two halves are NOT the same kind of zero.** ###"
     " Checked against b304's own trace_scaled at every unit and b309's reduced sum at every"
     " carried power, 0 disagreeing",
     "### A DERIVATION, AND A BEARING THAT IS NEVER A DECISION. ### At a finite place the"
     " source's construction carries NO ARITHMETIC; the prime's contribution lives in the"
     " local distribution the source integrates AGAINST -- eq. (149), read at content by b305"
     " -- which carries the log p and samples at exactly the powers this trace does not read."
     " ### **THE BEARING: THE FINITE SIDE CANNOT SUPPLY THE FIRST-LEVEL MASS THROUGH THE"
     " OBJECT**, the coefficient at p^1 being exactly zero. ### On b263's three properties,"
     " for candidates of THIS CLASS: **(SPEC-1) CANNOT be met** -- the one place it demands"
     " weight is exactly where the zero sits; **(SPEC-3) CAN be met**; **(SPEC-2) IS NOT"
     " DECIDED BY THIS ACT.** ### **SCOPE: NOT A DECISION ON b262's BRANCH** (b262's own"
     " sentence is a REQUIREMENT on the archimedean side and expressly not a claim that it"
     " fails; the disjunction is b263's FORMULATION, not b262's wording); **NOT A VERDICT ON"
     " M-2**, which stays (SPECIFIED-NOT-STATED) under b263's own 'these exclude; they do not"
     " determine'; **NOT A CLAIM THAT THE FINITE SIDE CONTRIBUTES NOTHING** -- a distribution"
     " is not a trace on a space; **AND NOT AN ARGUMENT FOR THE ARCHIMEDEAN BRANCH**, where"
     " this act derives nothing. ### M-2 UNCHANGED",
     "data/b310_the_smear_collapses.txt; data/b263_top_level_silence.txt (SPEC-1..3);"
     " data/b262_junction_limit.txt (its own sentence); CORRESPONDENCE.md row 133"),
    # ### THE SCALING TRACE, COMPUTED (b309).
    ("scaling-trace", "b309 (a computation on the b308 instrument)",
     "Tr(theta(p^k) Pi) for k != 0 -- the compression of the SCALING part of Q_p^x against the"
     " projection onto the object's own space. ### b304 computed the compact part and REFUSED"
     " this one because the model folds it; b308 built the frame where it does not fold and"
     " NAMED this computation without performing it. ### **THE FIRST THING ESTABLISHED IS THAT"
     " THE TRACE IS NOT DEFINED UNTIL AN AMBIENT IS NAMED**: theta(p^k) carries V(n,n) to"
     " V(n-k, n+k), so the composed map is no frame's endomorphism, and the smallest frame"
     " containing both is V(max(n,n-k), max(n,n+k)). ### **THE VALUE: EXACTLY ZERO AT EVERY"
     " NONZERO POWER IN [-2n, 2n] AT ALL SEVEN BANKED CELLS**, by two independent routes -- 34"
     " cell/power pairs by both, 10 by the reduced route only where the ambient exceeds 1024"
     " chart points and the bound is PRINTED. ### 0 disagreeing",
     "### A COMPUTATION, AND ITS VALUE IS ZERO. ### **NOT AN OBSTRUCTION THEOREM, AND NEITHER"
     " A ROUTE NOR AN ANTI-ROUTE** -- the order forbids reading a nonzero as a route and this"
     " act adds that the converse reading is forbidden too. ### **SCOPE: one trace of one map"
     " against one projection, at the cells and powers listed, in the smallest ambient"
     " containing source and target -- a different ambient is a different number.** ### It says"
     " nothing about any other functional on the instrument and nothing about the source's own"
     " functional, which smears against a test function over the whole group: a vanishing of"
     " every individual term is a statement about terms. ### **b273's A at k = n IS A DIFFERENT"
     " OPERATOR; the barrier and the compression are neither extended nor weakened.** ###"
     " NOTHING ABOUT THE ARCHIMEDEAN PLACE (b285's boundary stands). ### NO AGGREGATION IS"
     " STATED. ### M-2 UNCHANGED",
     "data/b309_the_scaling_trace.txt; data/b309_components_run.txt;"
     " tools/b309_scaling_trace.py; tools/b309_components.py; CORRESPONDENCE.md row 130"),
    # ### THE MECHANISM (b309).
    ("no-offball-fixed-point", "b309 (a derivation, with three arithmetic terminals)",
     "WHY the scaling trace vanishes, in TWO REGIMES WITH TWO MECHANISMS. ### ABOVE THE LEVEL"
     " (abs(k) >= n) the object's support and its image's are DISJOINT -- the object vanishes"
     " on the ball, so its support sits at absolute values p^1..p^n and the image's at"
     " p^(1+k)..p^(n+k) -- and **the COMPRESSION is the ZERO OPERATOR**, measured. ### BELOW IT"
     " (1 <= abs(k) <= n-1) **THE SUPPORTS GENUINELY MEET AND THE TRACE IS STILL ZERO**: against"
     " the projector's closed form the trace is a sum over t off the ball of two congruence"
     " indicators in (p^j - 1) t, and **p^j - 1 IS A UNIT**, so each congruence forces t = 0"
     " modulo the grid and modulo the ball's modulus -- and both of those sets are EXACTLY THE"
     " BALL, which the sum excludes. ### **THE SCALING MAP FIXES NOTHING OFF THE BALL, AND THE"
     " ONLY THING IT FIXES IS THE ONE PLACE THE OBJECT MUST VANISH**",
     "### A DERIVATION, GENERAL IN p, n AND k, WITH A FINITE SWEEP AS ITS CHECK -- **AND THE"
     " ACT SAYS WHICH IS WHICH: A SWEEP OVER SEVEN CELLS IS NOT A PROOF OVER ALL OF THEM.**"
     " ### THREE TERMINALS, ALL ZERO AXIOMS, Core/ScalingTraceShadow.lean (vanilla Lean, no"
     " imports, no native_decide, no sorry): B309.frame_arithmetic,"
     " B309.support_ranges_split_at_the_level (BOTH arms -- the meeting arm keeps the disjoint"
     " arm from reading as vacuous), B309.no_offball_fixed_point_of_scaling. ### **EACH RANGES"
     " OVER AN EXPLICIT LIST NAMED IN ITS OWN STATEMENT, SO NONE CAN BE READ AS A LAW ABOUT ALL"
     " p, n, k. ### AND WHAT THEY CERTIFY IS ARITHMETIC AND NOT THE BARRIER: the step from the"
     " counts to the vanishing of the trace is the bank's derivation and IS UNCOMPILED.** ###"
     " Profile 470 -> 473, all zero-axiom, the banked profile a TRUE BYTE PREFIX of the new"
     " one. ### M-2 UNCHANGED",
     "data/b309_the_scaling_trace.txt; data/b309_kernel_run.txt;"
     " SIDE-global-section/Core/ScalingTraceShadow.lean; CORRESPONDENCE.md row 131"),
    # ### THE LOCAL-FIELD INSTRUMENT, ACT ONE (b308).
    ("local-field-instrument", "b308 (an instrument build, act one of the priced item)",
     "the finite model ties two radii to ONE level index -- b21's V_n is p^(-n)Z_p / p^n Z_p"
     " = Z/p^(2n), one n governing both the SUPPORT radius and the CONSTANCY radius. ### This"
     " act UNTIES them and changes nothing else: a frame is a pair (r,s) -- support in"
     " p^{-r}Z_p, constant on cosets of p^s Z_p -- with b21's chart x = p^{-r} m and b21's"
     " Haar giving each cell mass p^{-s}. ### **THE MODEL IS THE POINT r = s = n AND THE"
     " INSTRUMENT IS THE PLANE.** ### The transform carries (r,s) to (s,r); the scaling part"
     " of the multiplicative group acts as theta(p^k) : V(r,s) -> V(r-k, s+k), so BOTH radii"
     " move, their SUM does not, and on chart indices the map is the IDENTITY. ### That is the"
     " direction the model drops. ### Built with a positive control in both polarities on every"
     " operation before it is used, exact Fraction/int/cyclotomic throughout",
     "### AN INSTRUMENT BUILT AND CHECKED -- **NOT A RESULT**. ### The reproduction is the"
     " GATE on the build: the family recovered as SET EQUALITY BOTH DIRECTIONS at every radius"
     " pair in range at five cells (0 disagreeing); the dimension law and the keystone's own"
     " (p^n-1)^2 at the diagonal (0 disagreeing); Tr(Pi) equal to the constrained dimension at"
     " six cells; the compact-part smear zero at all six WITH its mechanism re-derived on the"
     " instrument's own shells; the annihilation criterion at 80 members reached, 0"
     " disagreeing, 50 forced zeros confirmed; b295's two registered witnesses re-valued at"
     " their banked 4/3 and 4/7. ### **EVERY NUMBER IS A BANKED NUMBER RECOMPUTED OR A"
     " CONTROL, AND TWO INSTRUMENTS AGREEING IS A CHECK ON THE INSTRUMENTS RATHER THAN A"
     " PROMOTION OF ANY RESULT.** ### NO GRADE MOVES. ### NO NEW MATHEMATICS. ### **NO"
     " FIRST-LEVEL VALUE AT ANY CELL OR MEMBER THE RECORD DOES NOT ALREADY CARRY** -- that is"
     " a later act under its own registration, named in the bank and left uncomputed. ###"
     " **UNTYING THE RADII REMOVES THE WRAPAROUND; IT DOES NOT REMOVE THE TRUNCATION.** ###"
     " M-2 UNCHANGED",
     "data/b308_the_local_field_instrument.txt; data/b308_instrument_run.txt;"
     " tools/b308_local_field.py; tools/b308_reproduction.py; CORRESPONDENCE.md row 128"),
    # ### THE ESCAPED-MASS ARTIFACT, RETIRED FOR ONE INSTRUMENT (b308).
    ("escaped-mass-artifact", "b308 (a demonstration, and a retirement of one scope)",
     "b21 named it -- U maps V_n INTO V_(n+1) and ESCAPES V_n, so THE MODEL'S mod-N WRAPAROUND"
     " IS EXACTLY THIS ESCAPED MASS FOLDED BACK IN -- and b284 met it and wrote that the"
     " derivation stands because it is on Q_p, where there is nothing to fold. ### **THIS ACT"
     " MAKES THAT SENTENCE A COUNT.** ### The model must read theta(p^k) f back in the frame it"
     " left, which on chart indices is m -> p^k m mod N; the instrument moves the frame"
     " instead. ### **THE MODEL'S COLLIDED ORDERED PAIRS ARE N(p^k - 1), NONZERO AT EVERY CELL"
     " AND EVERY DIRECTION TESTED, BY TWO ROUTES; THE INSTRUMENT'S ARE ZERO BY THE SAME TWO"
     " ROUTES.** ### The escaped mass is exhibited on a vector of the object's own space: b21's"
     " U sends it to V(n+1, n-1), its smallest containing ball is p^{-(n+1)}Z_p at every cell"
     " (b21's own support law, recomputed), the escaped Haar mass is an exact nonzero rational,"
     " and b21's `unitary on L^2(Q_p)` comes out as a normalizing scalar of exactly 1",
     "### **RETIRED FOR THIS INSTRUMENT, AND FOR NOTHING ELSE.** ### **IT IS NOT RETIRED FOR"
     " THE MODEL** -- the model's column is nonzero everywhere and any later act scaling on"
     " Z/p^{2n} meets it again -- **NOR FOR b284**, whose exposure is declared, stands, and is"
     " not re-verdicted. ### It retires neither W-ORD-FIBER-GENERAL, nor the barrier's scope"
     " limit, nor the range law, nor the truncation. ### Exposure was decided BY CALL PATH: an"
     " arm scans for a non-unit pushforward site, this act's own two files carry 5 and ALL are"
     " declared carriers with 0 undeclared in the operational path, and the owners' sites are"
     " ruled one by one. ### **AND THE ARM'S LIMIT IS PART OF THE RESULT: IT FINDS A SHAPE AND"
     " CANNOT TELL A REGROUPING OF AN EXACT FINITE SUM FROM A REPRESENTATION OF A FUNCTION THAT"
     " LEFT ITS LEVEL** -- that judgement is the seat's and no tool made it. ### M-2 UNCHANGED",
     "data/b308_the_local_field_instrument.txt; data/b308_instrument_run.txt;"
     " data/b21_2026-08-18.txt; data/b284_the_scalings_domain.txt; CORRESPONDENCE.md row 129"),
    # ### THE ADELIC ARC FOLDED (b307).
    ("the-fold", "b307 (a filings act)",
     "ten acts, b297-b306, filed into FINDINGS.md as 'THE ADELIC ARC, b297-b306 -- THE"
     " FOLD', each entry with its grade as its OWN act left it, its scope sentence, and its"
     " OBSTACLE quoted. ### **THE ARC AS ONE STATEMENT:** the object's two halves now share a"
     " form and a dilation (one sentence defines a two-radius family at every place, and the"
     " finite dilation is the archimedean dilation at 1/p under the corpus's own chart); the"
     " finite side's first-level mass is annihilated exactly when either radius clears its"
     " threshold; the archimedean instruments compute with vectors OUTSIDE the object's own"
     " space; and the corpus works at the OPEN end of a single window parameter whose CLOSED"
     " end is the source's forced positivity. ### Also folded: the arc's four corrections to"
     " its own readings, each with a WHAT DID NOT MOVE column",
     "### A FILING, AT THE GRADE OF THE ACTS IT FOLDS AND NO HIGHER. ### **NO GRADE MOVES,"
     " NO ACT IS RE-VERDICTED, NO NEW MATHEMATICS, NO KEYSTONE WRITTEN OR EDITED** -- b299's"
     " arc keystone is cross-referenced, not duplicated. ### Emitted by tools/b307_fold.py,"
     " the section's GENERATOR and not its reviewer: 20 quotations, 0 unfindable, each"
     " checked against the act that ORIGINATED it BEFORE emission -- and two failed on the"
     " first run, one of them a sentence b303 was quoting from b301, so the gate caught a"
     " mis-attribution before the document existed. ### FINDINGS.md +80/-0, measured by"
     " numstat: PURELY ADDITIVE is the measurement, not the assertion. ### **SCOPE: NOTHING"
     " ABOUT THE IDENTITY, h2, OR THE COMPLETE ROSTER FOLLOWS FROM THE ARC SENTENCE** -- one"
     " half of the one-signed residual is derived and the other is at bench, and a summary"
     " may not upgrade a bench result by standing it next to a derived one. ### NO"
     " AGGREGATION IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b307_the_fold.txt; data/b307_fold_run.txt; PLACE-papers/FINDINGS.md;"
     " CORRESPONDENCE.md row 126"),
    # ### THE LEDGER CENSUS AND THE CONDITIONAL STRIKE (b307).
    ("handoff-census", "b307 (a check built to satisfy a conditional strike)",
     "the ferry scan fired on the ORDER'S OWN CLOSING: U-2, 'a closing sequence asserts that"
     " a ledger is current', struck at b300. ### **THE STRIKE IS CONDITIONAL AND THE RECORD"
     " NAMES THE CONDITION:** 'SURVIVES: the same phrase after a check that has COUNTED WHAT"
     " IS MISSING.' ### No such check existed, which is why the phrase had been unusable"
     " since b300 and every act since wrote two lists instead. ### tools/b307_handoff_"
     "census.py counts the arc's acts, the live work-orders and the arc's findings section"
     " against HANDOFF.md, run BEFORE and AFTER. ### **BEFORE: 26 MISSING -- ten acts,"
     " fourteen work-orders, one section. ### AFTER: 0**",
     "### A LICENCE EARNED AND BOUNDED. ### U-2's SURVIVES clause is satisfied FOR THIS"
     " LEDGER AND NO OTHER. ### **THE CENSUS COUNTS NAMES, NOT UNDERSTANDING** -- a ledger"
     " naming every act in one line each would pass it and could still be a bad handoff --"
     " and it says NOTHING about FINDINGS.md, REGISTRY.md, OPEN_TRAILS.md,"
     " VERIFICATION_LOOM.md or the desk, which were not counted and are not claimed."
     " ### **THE ACT NEITHER REFUSED THE ORDER NOR OBEYED IT AS WRITTEN**: it read the"
     " strike entry, found the strike conditional, and did the work the condition names --"
     " which is the b299 shape with the sign reversed, the command path reading the ferry and"
     " finding the ORDER asking for a struck phrase. ### NO GRADE MOVES. ### M-2 UNCHANGED",
     "data/b307_the_fold.txt; data/b307_census_before.txt; data/b307_census_after.txt;"
     " data/STRUCK_CLAUSES.md (U-2); CORRESPONDENCE.md row 127"),
    # ### THE CORPUS'S DIFFERENCE IS NOT THE SOURCE'S (b306).
    ("the-difference", "b306 (a decision by definitions)",
     "is the corpus's cell-level imbalance the same object as CC's"
     " arithmetic-minus-trace difference? ### **NO. ### DIFFERENT.** ### CC's is Theorem 1's"
     " inequality W_inf(g*g*) >= Tr(theta(g) S theta(g)*), a SINGLE-PLACE statement whose"
     " finite places enter through eq. (149) and are ZEROED -- not excluded -- by the support"
     " condition ('so that rational primes are not involved'). ### The corpus's is"
     " L - R = -(E2even + junction) at cells a^2 in {2,3,4,8,9,12}, verified against b254's"
     " and b248's own tables. ### **THE FIRST DIFFERING CONSTITUENT IS THE ARCHIMEDEAN SIDE**,"
     " and b291 is the quotation: 'SO NEITHER PAIRED FAMILY LIES IN THE OBJECT'S ARCHIMEDEAN"
     " SPACE.' ### A trace compressed ONTO Sonin's space sums over vectors IN it; the corpus's"
     " sums over vectors provably OUTSIDE it. ### **THE PRIME SIDE DOES MATCH (b305, carried),"
     " cutoff included -- and a difference of two things is the same object only if both"
     " are.** ### Four constituents have NO COUNTERPART at all: the smeared operator, the"
     " compression, W_inf, and the places summed over",
     "### DECIDED BY DEFINITIONS, CONSTITUENT BY CONSTITUENT. ### All three registered"
     " falsifiers HOLD. ### **SCOPE: NO MEASUREMENT IS DISTURBED AND NO GRADE MOVES.** ###"
     " E2even being a different functional says nothing about whether it was measured"
     " correctly; the junction stays DERIVES, E2even stays at bench, b254's (IMBALANCED)"
     " stands, b291's finding stands as its own. ### The source is not criticised: its theorem"
     " is about its own objects at its own window, and **the corpus's window is the"
     " COMPLEMENTARY choice of the same knob -- the source picks its window so no prime"
     " enters, the corpus so every prime up to a^2 does.** ### The corpus's test function is"
     " also outside Theorem 1's class (its bump is normalized to integral 1, so ghat(0) is not"
     " 0), and the source prices exactly that at -c|ghat(0)|^2 with 13 < c < 17 (Thm 6.11)."
     " ### W-ORD-SOURCE-METHOD-APPLICABILITY filed. ### NO AGGREGATION IS STATED. ### M-2"
     " UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b306_the_difference.txt; data/b306_difference_run.txt;"
     " CORRESPONDENCE.md row 124"),
    # ### THE SHARED-TARGET STEM SWEEP (b306).
    ("sweep-scope", "b306 (a scope repair, closing a hole b305 named)",
     "the stem sweep now covers the files EVERY act appends to and NO act swept --"
     " CORRESPONDENCE.md and banked_index.py. ### b305's own words are the specification:"
     " 'the sweep runs over this act's files and not over CORRESPONDENCE.md, so the row was"
     " caught by the bank's hit and not by its own.' ### **THE TOOL REPORTS PER ROW AND DOES"
     " NOT REFUSE**, because a hit in a shared file may be OLDER than the act running, and the"
     " row number is the attribution. ### Three hits on the first run, all one stem:"
     " banked_index.py line 400 (**b305's -- this seat's own, where the fix touched the"
     " generator and not the generated artefact; REPAIRED**); CORRESPONDENCE.md row 101"
     " (b284's, a defect when written since the stem entered the list at b142, which the old"
     " sweep could not see; NOT REWRITTEN); row 2 (predates b142, so not a defect -- a ban is"
     " not retroactive)",
     "### A SCOPE REPAIR, NOT A RESULT. ### **THE BOUNDARY THIS ACT DREW: REPAIR WHAT THIS"
     " SEAT WROTE AND MIS-FIXED; FILE WHAT ANOTHER ACT OWNS** -- the append-only law governs"
     " the difference between CANNOT and WILL NOT. ### The stems are READ from"
     " ferry_scan.stems() and never copied, so a stem added or retired moves the sweep with"
     " it. ### Fixtures on both polarities AND on the row-attribution arm, because a sweep"
     " that found a hit but could not name its row would leave an act unable to tell its own"
     " row from an ancestor's. ### W-ORD-ANCESTOR-ROW-b284 filed as a POINTER, not a repair."
     " ### NO GRADE MOVES. ### M-2 UNCHANGED",
     "data/b306_the_difference.txt; data/b306_stem_scope.txt;"
     " CORRESPONDENCE.md row 125"),
    # ### WHERE THE SOURCE'S ARITHMETIC ENTERS (b305).
    ("arithmetics-entry", "b305 (a read at content, in the source)",
     "in CC (arXiv:2006.13771v1) the primes are carried by the LOCAL WEIL DISTRIBUTION"
     " W_p(f) = (log p) SUM_{m>=1} ( f(p^m) + f#(p^m) ), eq. (149) of Appendix B."
     " ### **SO THE ARITHMETIC ENTERS THROUGH NEITHER THE TEST FUNCTION NOR THE OPERATOR BUT"
     " THROUGH THE DISTRIBUTION THEY ARE PAIRED AGAINST.** ### The operator theta(g) S"
     " theta(g)* contains no prime -- theta is the scaling action, S the Sonin projection, g"
     " a bump -- and its positivity is the A*A shape with A = S theta(g)*. ### The test"
     " function contributes a SUPPORT, which gates WHICH primes appear: the source takes"
     " supp in (1/2,2)'so that rational primes are not involved (see (149))'",
     "### AT CONTENT, b305's OWN READ; artefact sha256 b8e0b54a..., text layer measured"
     " INTACT (0 truncated pages), 11 of 11 quoted fragments located by page index."
     " ### **THIS IS A READ OF A SOURCE AND IS NOT A RESULT OF THE CORPUS.** ### It REFUTES"
     " the registered falsifier (F1) in its first half -- the arithmetic does NOT enter"
     " through the test function -- and confirms its second. ### It settles"
     " W-ORD-FORCED-POSITIVITY: the source never asks its positivity to carry arithmetic;"
     " Theorem 1 is an INEQUALITY between an arithmetic distribution and a forced-positive"
     " trace, and the content is in the difference. ### M-2 UNCHANGED",
     "data/b305_the_arithmetics_entry.txt; data/b305_source_read.txt;"
     " CORRESPONDENCE.md row 122"),
    # ### THE CORPUS'S PRIME SUM IS THE LOCAL WEIL DISTRIBUTION (b305).
    ("prime-sum-is-weil", "b305 (a comparison by definitions)",
     "the corpus's adopted summand w_{p,k} = 2 log p * p^{-k/2} * corr(log p^k) (b260,"
     " adopted b229) IS the k-th term of CC's local Weil distribution W_p under CC's OWN"
     " normalization W_v(f) := W_v(Delta^{-1/2} f): that term is (log p) p^{-k/2} ( f(p^k) +"
     " f(p^{-k}) ), and **the corpus's factor 2 is CC's f + f# collapsed under evenness**."
     " ### Same log p, same p^{-k/2} from the same normalization, same finite index set."
     " ### **AND NOT THE SAME SPECIES AS THE QUOTIENT CHANNEL**: the orbit ratio"
     " (p^n - p^k)/(p^n - 1) is dimensionless, carries neither factor, is silent at the top"
     " level by its own range, and is a WEIGHT applied to a prime term",
     "### DECIDED BY DEFINITIONS, FACTOR BY FACTOR. ### **(F2) HOLDS, MORE STRONGLY THAN IT"
     " WAS REGISTERED -- the same OBJECT, not merely the same species.** ### **SCOPE: HAVING"
     " THE OBJECT IS NOT DOING WITH IT WHAT THE SOURCE DOES.** ### The source pairs W_v"
     " against a compressed trace and proves an inequality; the corpus pairs PR against an"
     " orbit-count channel and measures a separation. ### The quotient channel is NOT demoted"
     " by being a different species -- a weight is not a lesser object than a distribution."
     " ### The match rests on an evenness the corpus records by its factor 2 rather than by a"
     " sentence, and that reading is NAMED. ### NO AGGREGATION IS STATED. ### M-2 UNCHANGED",
     "data/b305_the_arithmetics_entry.txt; data/b260_junction_sign.txt (the PR summand);"
     " data/b220_aggregation_freedom.txt (act 9's range); CORRESPONDENCE.md row 123"),
    # ### THE INSTRUMENT ON Q_p, PRICED AND NOT BUILT (b305).
    ("instrument-q-p", "b305 (a pricing, not a build)",
     "an instrument carrying the SCALING part p^Z of Q_p^x, which the truncated model drops."
     " ### It would compute on locally constant functions of compact support on Q_p -- and"
     " **the corpus's own chart and Haar normalization ALREADY DEFINE THEM**: b280's V_n is"
     " supported in p^{-n}Z_p and constant on cosets of p^n Z_p, a chart point being 'a COSET"
     " OF MEASURE p^{-n} > 0' on which f is constant. ### **THE ONE STRUCTURAL CHANGE IS TO"
     " UNTIE TWO RADII THE MODEL TIES TOGETHER** -- support radius and constancy radius, both"
     " n in V_n -- and the corpus already has b303's two-radius family for the untied pair"
     " and b293's dilation for how scaling moves it. ### Exact arithmetic: mostly Q, since"
     " b293's collapse makes the conditions rational; cyclotomic only for transform values",
     "### A PRICE, AND THIS SEAT'S ESTIMATE: **THREE ACTS FOR THE CORE, FIVE FOR THE"
     " COMPARISON**. ### **IT IS NOT A COMMITMENT, NOT A MEASUREMENT, AND NOT A"
     " RECOMMENDATION TO BUILD.** ### It must reproduce: (1) b293's two conditions, dimension"
     " law and diagonal identification; (2) b304's compact-part zero WITH its mechanism, not"
     " only its value; (3) b297's annihilation criterion and b280's P(k=n)=0 at reachable"
     " cells; and (4) b304's Tr(Pi) = dim Son, so it is shown alive. ### **IT RETIRES THE"
     " ESCAPED-MASS ARTIFACT** (b21, met b284): on Q_p there is no modulus and nothing to"
     " fold. ### It does NOT retire W-ORD-FIBER-GENERAL, the barrier's scope limit, or the"
     " range law. ### M-2 UNCHANGED",
     "data/b305_the_arithmetics_entry.txt; data/b280_the_consequence.txt (the chart and"
     " Haar sentences); data/b284_the_scalings_domain.txt (nothing to fold on Q_p)"),
    # ### THE DEMAND'S SHAPE (b304).
    ("demands-shape", "b304 (a derivation from the specification's own text)",
     "is the per-index first-level demand (SPEC-1) downstream of requiring TERMWISE"
     " agreement with the quotient channel below the top (SPEC-2)? ### **NO.** ### Two"
     " reasons, both in b263's text: (i) SPEC-1's stated ground is S1 + S2 and NAMES SPEC-2"
     " NOWHERE; (ii) at the primes SPEC-1 is about, SPEC-2's range 1 <= k <= n-1 reads"
     " 1 <= k <= 0 and is EMPTY, so there is nothing there for a loosening to loosen."
     " ### Loosening termwise to aggregate DISSOLVES the demand at primes with n_p >= 2 and"
     " DISSOLVES NOTHING at n_p = 1 -- which by S2 carry 73.96% rising to 99.95% of the"
     " separation. ### **THE DEMAND IS DOWNSTREAM OF THE INDEX SET BEING A SINGLE POINT,"
     " NOT OF A CHOICE ABOUT AGREEMENT**, and b262 states that shape outright: the n_p = 1"
     " family are the primes 'whose only level IS the top level'",
     "### DERIVED FROM THE OWNERS' TEXT, NOT ARGUED. ### **NO SPECIFICATION IS LOOSENED BY"
     " THIS ACT -- ONLY THE AUTHOR MAY DO THAT** -- and the two options are assembled as a"
     " DECISION CARD with NO recommendation. ### The barrier still reaches the n_p = 1"
     " places under either option, because the demand there is still a value at the top."
     " ### NO AGGREGATION IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b304_the_demands_shape.txt; data/b263_top_level_silence.txt (SPEC-1..3, S1, S2);"
     " data/b262_junction_limit.txt (the T_top partition)"),
    # ### THE ARCHIMEDEAN UNIT'S SQUARE-INTEGRABILITY (b304).
    ("phi-mu-l2", "b304 (a read at content, in both sources)",
     "the corpus's u_inf is phi_mu at the first even negative eigenvalue, normalized, and"
     " **IT LIES IN L^2(R)**, by two independent routes. ### ROUTE A: phi_mu is an"
     " eigenvector of Wsa; CM defines Wsa as the restriction of Wmax to a subspace with an"
     " explicit Dom Wsa, the ambient space being L^2(R) in CM's own words; and an"
     " eigenvector lies in its operator's domain BY THE DEFINITION OF EIGENVECTOR --"
     " **SO MEMBERSHIP IS DEFINITIONAL AND NOT A DECAY STATEMENT**. ### ROUTE B: CM"
     " Corollary 3.2 puts phi_mu in the Sonin space, and CC defines that space as a subspace"
     " of the Hilbert space L^2(R)_ev. ### The hypothesis was CHECKED and not carried on the"
     " corollary's name: Corollary 3.2 needs mu negative, and b214's printed mu is"
     " -20.48057322913694697",
     "### AT CONTENT, b304's OWN READ OF BOTH SOURCES (arXiv:2112.05500v1 sha256 426114ae...;"
     " arXiv:2006.13771 sha256 b8e0b54a...). ### **W-ORD-PHI-MU-L2 IS DISCHARGED** -- filed"
     " at b300 as 'stated by no owner', and an owner does state it, twice; what was missing"
     " was the READ and not the mathematics. ### **SCOPE: THE OBJECT STILL STANDS ON THREE"
     " CONDITIONS** -- the level-limit premise, W-ORD-ARCH-NORM-READING, and C9/N-OPEN-B --"
     " and A CONDITION DISCHARGED IS NOT THE OBJECT CONSTRUCTED. ### It does NOT put u_inf"
     " in the sector (b201's BRANCH (NO EXHIBIT) stands) and does NOT decide which inner"
     " product the normalization is. ### M-2 UNCHANGED",
     "data/b304_the_demands_shape.txt; CORRESPONDENCE.md row 120;"
     " data/b300_the_archimedean_leg.txt (where it was filed)"),
    # ### THE FINITE ANALOGUE OF THE SOURCE'S MOVE, COMPRESSED (b304).
    ("smearing-compression", "b304 (a decision by definitions, then a computation)",
     "the finite analogue of CC's Tr(theta(f) S) is T(f) = Tr(theta(f) Pi) on Z/N,"
     " N = p^{2n}, with Pi the projection onto Son(p,n). ### **THE BARRIER DOES NOT REACH"
     " IT**: the barrier's operator is a functional of the unit's restriction TO the ball,"
     " where every element of S-bar_p vanishes, while the smeared operator's matrix elements"
     " are supported OFF the ball, where S-bar_p lives. ### The compression was therefore"
     " computed, exact rationals, no float: at (2,1) (2,2) (3,1) (3,2) (5,1) (7,1) the"
     " smeared value against the constant test function on the units is **EXACTLY ZERO AT"
     " ALL SIX, including every one-level place** -- and the zero is DERIVED, not only"
     " measured: SUM_t theta(t) is |U| times the projection onto the unit-invariants, which"
     " are spanned by valuation shells, and every Son vector is orthogonal to every shell",
     "### A COMPUTATION ON THE PART OF THE GROUP THE MODEL CAN CARRY. ### **Q_p^x = p^Z x"
     " Z_p^x, AND ONLY THE Z_p^x PART WAS COMPUTED** -- it acts by permutations, verified at"
     " every t used. ### **THE p^Z PART WAS REFUSED**: it is b21's escaped-mass artifact, met"
     " at b284, and the model would return the genuine object with its escaped mass folded"
     " back onto the ball. ### **AND THE REFUSED PART IS THE PART WITH AN ARCHIMEDEAN"
     " COUNTERPART**, so this zero is NOT 'the finite analogue's value'. ### **IT IS NOT A"
     " BARRIER AND NOT A ROUTE** -- for a general test function the value is SUM_t f(t)"
     " Tr(theta(t) Pi) and those traces are not all zero. ### The barrier is not weakened:"
     " an operator it does not reach is not a counterexample to it. ### M-2 UNCHANGED",
     "data/b304_the_demands_shape.txt; data/b304_smearing_run.txt;"
     " CORRESPONDENCE.md row 121"),
    # ### THE TWO-RADIUS FAMILY ACROSS PLACES (b303).
    ("uniform-family", "b303 (a definition, written across places)",
     "a member is a choice, AT EVERY PLACE v, of a pair of radii (lambda_v, mu_v) -- one"
     " bounding where the function vanishes, one where its transform does -- with"
     " Son_v(lambda_v, mu_v) the functions in that place's own local space vanishing on"
     " abs_v(x) <= lambda_v whose transform vanishes on abs_v(y) <= mu_v, the local space,"
     " the absolute value and the transform each being THAT PLACE'S OWN. ### It restricts to"
     " b293's Son(p,n;a,b) at finite p and to CC Definition 4.4's S(lambda,mu) at infinity."
     " ### **THE CORPUS'S OBJECT IS THE EVERYWHERE-(1,1) MEMBER**, which at every place is"
     " the transform-fixed point of its own dilation orbit -- verified at content vector by"
     " vector at five finite cells, and READ off CC's own identifying sentence at infinity."
     " ### The bridge is b21's chart x = p^(-n) m, THE CORPUS'S OWN, quoted by b293 inside"
     " its own definition of B_e; under it the finite SUM invariant a+b is the archimedean"
     " PRODUCT invariant lambda*mu, and the finite dilation is D_a at a = 1/p",
     "### A DEFINITION, AND ITS GRADE IS A DIVISION: ### **UNIFORM AS A FORM, NOT AS AN"
     " OBJECT.** ### One sentence covers all places because every term delegates to the"
     " place; the instances are structurally different BY A THEOREM -- the sub-level set is a"
     " compact open subgroup at p and provably not one at infinity (b198). ### **A LATER ACT"
     " MAY QUOTE THE FORM AND MAY NOT QUANTIFY OVER THE OBJECTS AS THOUGH THEY WERE ONE KIND"
     " OF THING.** ### W-ORD-UNIFORM-FORM's promotion criterion is met AS TO CONTENT and the"
     " proposal stays UNBANKED-UNTIL-TESTED; PROMOTION IS THE AUTHOR'S. ### The annihilation"
     " criterion remains a statement about members at the FINITE places. ### NO AGGREGATION"
     " IS STATED. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b303_the_uniform_family.txt; data/b303_family_run.txt;"
     " CORRESPONDENCE.md row 118"),
    # ### von NEUMANN'S DEFINITION 3.3.1, READ AT SOURCE (b303).
    ("vn-definition-331", "b303 (a read at content, in the source itself)",
     "quoted whole from the page image: 'A sequence f_alpha, alpha in I, is a C0-sequence, if"
     " and only if f_alpha in H_alpha for all alpha in I, and SUM_(alpha in I) of"
     " abs(norm(f_alpha) - 1) converges.' ### **IT ASKS FOR MEMBERSHIP IN THE LOCAL HILBERT"
     " SPACE AND A CONVERGENT NORM SUM AND FOR NOTHING MORE**, and it makes NO PARTITION OF"
     " I -- no clause distinguishes an archimedean index from a finite one. ### The corpus's"
     " own OCR extract stops dead at 'if and' and the next line is the page number, which is"
     " why the clause had been held THROUGH A READER (b197) since b196",
     "### AT CONTENT, b303's OWN READ, BY A ROUTE INDEPENDENT OF b197's -- and the two agree"
     " WORD FOR WORD. ### **VERDICT: CONFIRMS.** ### b302's execution of RULE ARCH-UNIT"
     " stands on the source's own words, and the conditional b302 wrote against itself is"
     " DISCHARGED. ### **A CONFIRMATION REMOVES AN EXPOSURE; IT DOES NOT ADD A RESULT** --"
     " Q4 stays WITHDRAWN, the sector clause stays DESCRIPTION, b214's c = +1 stays at BENCH."
     " ### SCOPE: ONE DEFINITION. Lemma 4.1.2, Def 4.1.1 and Def 3.3.2 were NOT re-read and"
     " stand at b226's at-source grade. ### M-2 UNCHANGED",
     "data/b303_the_uniform_family.txt; data/b303_source_read.txt;"
     " CORRESPONDENCE.md row 119; artefact sha256"
     " 571060b596af58af35f09f077984a2b747e7acbc52ab6d107ba8b45c761ad0a3, page index 21"),
    # ### THE OBJECT'S STANDING CONDITIONS, WITH THE COUNT CORRECTED (b303).
    ("object-conditions", "b301 and b302, count corrected at b303",
     "the object (x)'_v (S-bar_v, u_v) is CONSTRUCTED CONDITIONALLY on FOUR standing"
     " conditions, each typed: a PREMISE (the level limit, b198 I2); a RESULT"
     " (W-ORD-PHI-MU-L2, phi_mu in L^2(R), stated by no owner); a RULING"
     " (W-ORD-ARCH-NORM-READING, which inner product b226's archimedean normalization is);"
     " and a CONSTRUCTION (C9 / N-OPEN-B, the real fiber's placement). ### **b302's SENTENCE"
     " SAYS THREE AND b302's OWN LIST CARRIES FOUR; THE LIST IS RIGHT.** ### The root is"
     " b301's headline, which counted ONE of its own THREE typed results",
     "### AT b301's AND b302's OWN BANKED GRADES. ### **NO VERDICT MOVES AND NO CONDITION WAS"
     " ADDED OR REMOVED -- ONLY THE COUNT IS CORRECTED**, and it is filed rather than edited"
     " into either act (the append-only law). ### **WHAT SETTLES IT IS b303's SOURCE READ:**"
     " Definition 3.3.1's FIRST conjunct is f_alpha in H_alpha, so W-ORD-PHI-MU-L2 is the"
     " MEMBERSHIP HALF OF DEFINITION 3.3.1 AT INFINITY -- one of the two things the source"
     " asks for, undischarged at one place -- and therefore a condition of the object and not"
     " a debt of a lane. ### Q4 is NOT among the four: it was WITHDRAWN as a requirement."
     " ### M-2 UNCHANGED",
     "data/b303_the_uniform_family.txt; data/b302_the_unit_requirement.txt;"
     " data/b301_the_object_completed.txt"),
    # ### THE UNIT REQUIREMENT (b302).
    ("unit-requirement", "b302 (a ruling executed against quoted text)",
     "what von Neumann's incomplete direct product asks of a CHOSEN VECTOR at each place,"
     " quoted: Definition 3.3.1's `f_alpha in H_alpha for all alpha in I` (at b197's"
     " at-content grade, the corpus's OCR extract being defective exactly there), its norm"
     " clause `SUM_v | ||f_v|| - 1 | CONVERGE`, and Lemma 4.1.2's `||f_a|| = 1`."
     " ### **THAT IS ALL IT ASKS: MEMBERSHIP IN THE LOCAL HILBERT SPACE AND UNIT NORM.**"
     " ### No clause mentions an eigenspace, an operator, a sector or a transform, and"
     " **THE INDEX SET IS NOT PARTITIONED ANYWHERE -- there is no clause distinguishing an"
     " archimedean index from a finite one.** ### So the author's RULE ARCH-UNIT ('A --"
     " space membership suffices'), which executes only if the quoted text supports it,"
     " EXECUTES; the HALT branch was tested and not taken",
     "### THE AUTHOR'S RULING, EXECUTED AGAINST QUOTED TEXT AND STRIKEABLE. ### **WHAT IT"
     " DOES IS NARROW THE ORIGINAL WORDING RATHER THAN FULFIL IT**: the b225 ruling asked"
     " for 'the archimedean unit from the Sonin sector', and that requirement is WITHDRAWN,"
     " the sector clause retained as DESCRIPTION whose establishment is not required by the"
     " construction and is NOT CLAIMED. ### b214's c = +1 at rank 2 stands at BENCH and is"
     " NOT promoted. ### The ruling is named ARCH-UNIT and is NOT applied to the finite"
     " units, where it would have no bite: b226's u_p is a projector image, in E_1 BY"
     " CONSTRUCTION. ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b302_the_unit_requirement.txt; CORRESPONDENCE.md row 117"),
    # ### THE GENERATOR'S NONVANISHING (b268), KEYED AT b302 BECAUSE IT NEVER WAS.
    ("generator-nonvanishing", "b268 (2026-08-31), keyed at b302",
     "4q P_1 f_(1,1) != 0 AT EVERY ODD PRIME p AT LEVEL 1 -- b226's owed step, PAID."
     " ### The route is one line of congruence arithmetic once the owners' objects are"
     " unfolded, and it delivers more than the nonvanishing: **support(u_p) = N - q"
     " EXACTLY**, which b226 had recorded as OBSERVED at six cells and explicitly did NOT"
     " assert as a theorem. ### The hinge is that for ODD q, gcd(q+2, q^2) = 1, so the zero"
     " set is exactly the q multiples of q. ### Controlled exactly in Z[zeta_N] at eight"
     " places -- b226's six plus p = 17 and p = 19 -- with 1039 values reduced modulo Phi_N"
     " and NO floating point deciding anything",
     "### DERIVES-on-IMP, the imports being the owners' own definitions and the BANKED"
     " purity identity, and NO NEW IMPORT -- as b268 graded it. ### **THIS ROW EXISTS"
     " BECAUSE ITS ABSENCE COST TWO ACTS A FALSE OPEN**: b300 and b301 both restated b226's"
     " step as OWED, pulling it from the act that INCURRED it and never asking whether a"
     " later act had PAID it, and every query that would have found b268 returned NO KEY."
     " ### b164's limit stands: keys close false hits, not false misses."
     " ### It pays b226's step and does NOT touch (SPEC-1) -- a support is not a"
     " contribution. ### M-2 UNCHANGED",
     "data/b268_generator_nonvanishing.txt; data/b268_run.txt;"
     " data/b302_the_unit_requirement.txt (the staleness diagnosis)"),
    # ### THE OBJECT COMPLETED (b301).
    ("object-completed", "b301 (construction restatement and its checks)",
     "the object (x)'_v (S-bar_v, u_v) restated with every constituent in one table:"
     " AT FINITE p, S-bar_p is the L^2(Q_p)-closure of the Son tower (b279, CONSTRUCTED),"
     " with u_p = 4q P_1 f_(1,1) at level ell(p) = 2 if p = 2 else 1 -- the exceptional"
     " place being the law's own zero d_1(2,1) = 0; AT INFINITY, S(1,1) from CC Definition"
     " 4.4 with the inner product of CC eq (16), and u_inf = phi_mu at the first even"
     " NEGATIVE eigenvalue, IN that space (b300). ### **OF THE PRODUCT'S EIGHT REQUIREMENTS:"
     " 4 MET (a Hilbert space at every index; a norm-one vector EXISTS at every index; the"
     " C0 condition; the level-limit premise), 3 OPEN (the STATED finite unit's nonvanishing"
     " at the generic odd place; the archimedean unit's SECTOR membership; choice-dependence)"
     " and 1 NOT ASKED -- purity, which belongs to the RESTRICTED TENSOR PRODUCT and not to"
     " von Neumann's incomplete direct product the author's b225 ruling re-scoped term 3 to.**"
     " ### The C0 condition was RE-CHECKED in exact rationals under CC eq (16): it holds"
     " under every reading of the archimedean normalization, and **the corpus's own"
     " half-line picture is the reading that agrees with the source exactly**, keeping"
     " b226's sum at EXACTLY 0; under the plain-INT_R reading the deviation is 1 - 1/sqrt(2)"
     " and Lemma 4.1.2's hypothesis wants a renormalization this act NAMES and does not make",
     "### CONSTRUCTED CONDITIONALLY -- on the level-limit premise (b226, at b198 I2's grade),"
     " on ONE RESULT (b226's OWED generic odd place), on ONE RULING (which inner product the"
     " archimedean normalization is -- W-ORD-ARCH-NORM-READING) and on ONE CONSTRUCTION (the"
     " real fiber's placement, N-OPEN-B). ### **NO GRADE MOVES: every cell carries its owning"
     " act's grade, pulled from that act's file.** ### **NOT A ROUTE. ### NO AGGREGATION IS"
     " STATED. ### THE IDENTITY CHAIN'S TERM-3 ROW DOES NOT MOVE BY THIS ACT** -- it names"
     " the restricted tensor product, three requirements are open, and a row is not moved by"
     " an executor (W-ORD-TERM3-ROW). ### M-2 UNCHANGED (SPECIFIED-NOT-STATED)",
     "data/b301_the_object_completed.txt; data/b301_object_gate.txt;"
     " CORRESPONDENCE.md row 116"),
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
