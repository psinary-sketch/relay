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
    'the-nearest-door': ['can the finite side seal be generalised', 'what does the compact part need beyond seven cells', 'what would it cost to prove (N) in the kernel', 'where does the 2T squared threshold come from', 'is the R4 tail still two Mathlib-absent premises', 'what is the smallest step on the nearest door'],
    'the-classification-arc-folded': ['what did the classification arc produce', 'how far behind is the findings digest', 'did the classification arc move a door', 'what would price an import reach', 'which folds carry a one statement', 'what is the routed pile'],
    'the-join-and-the-price': ['what grades an imported equivalence', 'does the E0 gate price the import', 'which free instrument number is next', 'where is the gauge verification banked', 'do the keystone and the placement screen cite each other', 'what is the difference between the two grading vocabularies'],
    'the-imports-classified': ['do the four imported premises factor through the interface', 'does the sieve ceiling lemma apply to the reduction', 'how many rows does the calibration family have', 'what does corollary 3.6 leave in the placement register', 'has the corpus aimed at the density register', 'what is the placement screen'],
    'the-obstacles-dissolved': ['which class numbering does a document use', 'has the modular relation been examined as a channel', 'does the corpus grade kappa by register', 'does the sieve ceiling lemma cover a conditional', 'why is row U1 frozen', 'what would a mathematics-facing gate arm require'],
    'the-other-two-channels': ['has the modular symmetry been examined as a channel', 'what are the other two bright channels', 'why does the corpus have two class numberings', 'what would the reduction be if written as a proof', 'is the fold due', 'do the gate suites have a standing core'],
    'the-barriers-own-instance': ['does the sieve ceiling lemma apply to the corpus reduction', 'is the corpus reduction a formal proof', 'do the uniformity sites name an interface', 'what would make the corollary name a channel', 'is the spectral realization the bright channel', 'how do you find the newest run record'],
    'the-sites-without-an-existential': ['what does the corpus call the barrier between instances and the class', 'what would close a per-instance to universal gap', 'why do the two sites have no shared witness', 'is the finite side compiled in general', 'what is an escape kind', 'was a third coordinate added to the uniformity row'],
    'the-rows-law-restated': ['what is a shared witness in this corpus', 'can the uniformity row tell two kinds of empty apart', 'does any uniformity site have a shared witness', 'is the finite side zero the same at every place', 'was row u1 retired', 'what would it cost to carry the countermodel to an instance'],
    'the-fifth-and-sixth-sites': ['what is the fifth uniformity site', 'is the type-d residue a uniformity obstruction', 'what kinds of empty can a uniformity site be', 'does the corpus study more than one l-function', 'are the two exhaustiveness theorems one theorem', 'can the side-effects axiom profile be read'],
    'the-three-routed-items': ['does the corpus have a rule for a stale figure on a public surface', 'was the side-window terminal count wrong or undated', 'may an act repair another act locked face', 'what did the span counter say about the fold threshold', 'why did the control stop a correct repair', 'is the fifth uniformity site entered'],
    'the-artefact-arc-folded': ['what did the span b385 to b401 put on the board', 'is the fold due and at what count', 'what is the fold threshold and who ruled it', 'which acts of the span found an artefact rather than a limit', 'did the navigator count the span correctly', 'what defects did the seats declare in this span'],
    'the-absent-element-searched': ['is there a bound on the prime sum at a wider support', 'does the record hold an unconditional finite place bound', 'is the li coefficient bound uniform in the prime', 'does the one prime window bound the weil sum', 'is q400 a fourth instance of the uniformity obstruction', 'what does side-window actually prove'],
    'the-bridge-restated': ['what replaces the refuted bridge identity', 'why can the sonin margin not reach the li margin', 'is the sonin margin prime free', 'does proposition c1 apply at the widened window', 'where would a bridge have to live', 'are the two margins one object or two'],
    'the-sign-and-the-refutation': ['is the missing identity true', 'does the sign test refute the bridge identity', 'what is the prime sum on the lawful seeds', 'why is the compressed square not the finite place sum', 'which bound is binding on the lawful class', 'may a later act move a grade inside the e0 ranking'],
    'the-li-weil-bridge': ['does the li-weil bridge assemble', 'what is the missing identity', 'is the sonin margin defined on the li family', 'what are the two margins place-sets', 'what is the smallest next statement toward the clause', 'why is the bridge still owed'],
    'the-unlanded-work': ['what is on the held branches', 'were the held branches already landed', 'what has the programme compiled that it cannot cite', 'is the disclosure rule stale', 'what is the queue and what are its triggers', 'what does the research board say'],
    'the-backtick-swept': ['how many findings rest on a backtick', 'was the sweep itself narrow', 'what is a figure at risk', 'did any figure move when the predicate was widened', 'what does it cost to read the ten reachable keystones', 'can an anchor edit a preserved block'],
    'the-ceiling-answered': ['can the unreachable keystones be read', 'was b394 wrong about the ceiling', 'how many federation repositories does the drive hold', 'which cluster was re-anchored', 'what does a route that reaches zero cost'],
    'the-reconciliation-batched': ['how many keystones are reconciled', 'which keystones were read at b394', 'what does it cost to reconcile a keystone', 'why can most keystones not be reconciled', 'did the batch find a defect in itself'],
    'the-five-clusters-surfaced': ['which five clusters changed', 'did any cluster change its anchor', 'what would it cost to fix the two deposited records', 'what would it cost to apply tier kc', 'why is tier kc still empty'],
    'the-two-rulings-r19-and-r20': ['what is a finished keystone', 'how is a finished keystone cited', 'the deposit rule', 'what deposits and when', 'which deposited records fail the currency obligation'],
    'the-phantom-version-repaired': ['the phantom version pass', 'where did v1.2 come from', 'how many citations named a version that never existed', 'the five clusters read', 'the superseded version citations'],
    'the-first-proofreading-pass': ['the first proofreading pass', 'which keystone was read', 'the methodology paper version citation', 'was the keystone current', 'the map row repaired'],
    'two-maps-two-keys-and-the-layer-unread': ['two maps two keys', 'the deposited layer could not be read', 'is there a written deposit rule', 'the unreached repository', 'b388 was wrong about the kernel'],
    'the-map-refreshed-under-r17': ['the map refreshed under r17', 'the two emergent clusters seated', 'the keystones assigned to clusters', 'the kernel that does not resolve', 'the unreadable rows named by cause'],
    'what-the-keystones-tables-actually-carry': ['what the keystones tables carry', 'nine of the fourteen carry a table', 'the rows that are not machine verified', 'the union names an ungraded carrier', 'the seat memory has no prior blob'],
    'the-guard-made-single-sourced-under-r15': ['one guard one source', 'the guard made single sourced', 'the second tracked guard copy deleted', 'the installer repointed', 'a search uses the rule own words'],
    'the-reservoir-rule-located-and-the-six-on-the-trails': ['the reviewer reservoir rule located', 'the mirror-refresh session protocol', 'the six not-yet-synthesized clusters', 'the paraphrase scored clause by clause', 'the three that waited on nothing'],
    'the-fold-b371-through-b383': ['the fold b371 to b383', 'the re-derivation arc', 'the span was counted', 'a minted rule is not a carried rule', 'four acts of work and eight of re-derivation'],
    'the-standing-standard-read-and-the-sequence-reconciled': ['the standing standard read', 'the sequence reconciled', 'the four tiers', 'the keystone correspondence union', 'the cluster unit'],
    'the-sequence-stopped-and-the-evidence-closed': ['the sequence stopped', 'the evidence closed', 'role must be declared', 'two failed features are evidence not proof', 'the declaration rule priced'],
    'the-control-rebuilt-and-co-location-not-adopted': ['the control rebuilt', 'co-location tested', 'co-location is not adopted', 'the purpose statements', 'two features fail the same distinction'],
    'the-role-axis-read-from-structure': ['the role axis scored structurally', 'role from structure', 'reach is not argument', 'the predicate fails its own control', 'the premise measured not assumed'],
    'the-suspect-column-re-measured': ['the apparatus axis re-scored', 'the suspect column',
                                      'the row categories', 'a category is not an absence',
                                      'the download layer drift'],
    'an-upper-bound-at-one-ref': ['the refs widened', 'an upper bound at one ref',
                                 'the two conventions', 'the archives confirmed',
                                 'a search that cannot run'],
    'the-pin-was-missing': ['the unblocked obligation', 'the pin was the missing element',
                           'the branch applied', 'the role clause', 'the six documents'],
    'every-test-crosses': ['the two axis read', 'every test crosses',
                          'the class ruling evidence', 'the apparatus and the prose',
                          'the floor question'],
    'three-tests-one-word': ['the keystone census', 'three tests one word',
                            'the cluster census', 'the document class',
                            'the integration state'],
    'descriptive-layer-measured': ['the descriptive layer', 'the hedge audit', 'the glossary',
                                  'the bibliography', 'the undated figures',
                                  'the functional equation filing'],
    'rule-outruns-record': ['the pins ruling', 'the sourcing rule', 'the status column',
                           'cites at an unknown ref', 'the writing act'],
    'pin-is-a-date': ['the eol pin', 'the readme figures', 'the first batch',
                     'checked at head', 'the row classification'],
    'count-claim-stale': ['the count claim', 'the first target', 'the row inventory',
                         'the desk closes', 'the hook made durable'],
    'apparatus-arc-fold': ['the apparatus arc', 'the fold b361', 'the span counted',
                          'the three mints', 'the durability split'],
    'list-repaired-in-place': ['the list repaired', 'the list repaired in place',
                              'the original preserved verbatim', 'the roster mended',
                              'the refinement pass priced'],
    'front-document-reconciled': ['the front document reconciled', 'the currency block',
                                 'the layer-1 export list', 'the eighteen absent names',
                                 'the desk freshness rule'],
    'scaffold-not-located': ['the scaffold terminals', 'grh_exclusion', 'no_ls_zero',
                            'twist_cancels', 'the scaffold repair'],
    'dated-arm-sweep': ['the dated-arm sweep', 'the rewrite rule', 'gate_content',
                       'the standing check', 'address predicate'],
    'cuspidality-convention': ['the cuspidality convention', 'the convention is located',
                              'the exceptional case', 'W-ORD-LI-CUSP', 'the owed read'],
    'dated-arm': ['the dated arm', 'a dated arm', 'the copy that did not reproduce',
                  'G-LOCATED', 'the arm that no longer holds'],
    'anchored-gate-arms': ['the anchored gate arms', 'gate_needle', 'the anchored-arm helper',
                           'the needle helper', 'the wrong arm', 'the gate arms counted'],
    'approximation-register': ['the approximation register', 'Nyman-Beurling', 'Baez-Duarte',
                              'the closed span of dilations', 'the distance to the span',
                              'the register read under a cap'],
    'index-condition-decided': ['H-NGEK', 'the held item', 'the index condition',
                               'the archimedean index condition', 'the absolute constant',
                               'the vacuous condition'],
    'uniformity-fold': ['the fold b349', 'the uniformity arc', 'the three that rhyme',
                       'what the checks certify', 'the instrument edge', 'the mirror roster addition',
                       'the span b349', 'the fourth instance'],
    'ledger-currency-pass': ['the ledger currency pass', 'the currency pass', 'the front door',
                            'the federation map', 'the deposit state', 'the precedence',
                            'are the ledgers current', 'the federation pins', 'the mirror roster'],
    'li-asymptotics-circular': ['the li asymptotics', 'the li tail', 'the li coefficients asymptotic',
                               'what would close the tail', 'the detection threshold',
                               'the finite range', 'the circularity check', 'the two channels'],
    'what-the-ledgers-certify': ['what the ledgers say the checks certify', 'the wider sentence',
                                'the narrower sentence', 'the attribution fault',
                                'what the checks certify', 'the ledger read', 'the errata draft',
                                'the construction-confirming scan'],
    'object-or-boundary': ['the object or the boundary', 'the raised axis', 'the quadrature bound',
                          'the instrument edge', 'the sixth rung again', 'six dimensions',
                          'the rank at the bound', 'the control at the raised axis'],
    'what-the-arrays-are': ['what the arrays are', 'the test functions', 'the piecewise-linear object',
                           'the lawfulness checks', 'what the scan certifies', 'the three layers',
                           'the relabelling', 'the smooth bump'],
    'sixth-frame': ['the sixth frame', 'the sixth rung', 'the domain ladder', 'the rank saturation',
                   'the negative residual', 'the last rung', 'the chosen ceiling',
                   'the criterion domain'],
    'width-missing-statement': ['the width coordinate', 'the missing statement', 'Boas-Kac',
                               'the admissible class', 'the test function class', 'a density statement',
                               'the spanning subfamily', 'exhaustion across widths'],
    'floor-fourth-candidate': ['the floor as a fit', 'the fourth candidate', 'the three models',
                              'the model selection', 'a floor or a power law', 'the frame price',
                              'the straddling gate', 'the spectral void'],
    'aim-plane-coordinates': ['the aim plane', 'the partition question', 'the abscissa', 'the height',
                             'the phase window', 'the seed\'s width', 'a finite classification',
                             'a bound on the instrument'],
    'held-axes-priced': ['the held axes', 'the price of the axes', 'the cut\'s threshold', 'the taper',
                        'the rank-preserving band', 'the floor is explained', 'the floor unexplained',
                        'pricing is not measuring'],
    'room-relative': ['the room', 'the relative room', 'the room relative', 'the point of maximum tension',
                      'the shared normaliser', 'the extended height grid', 'the phase window',
                      'a degenerate seed'],
    'priced-and-resolved-fold': ['the fold b339', 'the priced-and-resolved arc', 'the arc as one statement',
                                'use and mention', 'the scanner over prose', 'the census as a finding',
                                'the failure-mode partition', 'the judgement rule'],
    'bar-floor-rule': ['the bar-floor rule', 'the run file\'s clock', 'the flattener', 'the two-routes rule',
                      'the satisfiability audit\'s limit', 'the standing clauses v2', 'the act-number clause',
                      'a bar below its floor', 'arms that are one arm'],
    'exponent-by-rate': ['the exponent by rate', 'the decay rate', 'the even sector', 'the convention',
                         'the rate separates the conventions', 'which convention the banked values carry',
                         'the resolving power in the rate', 'the floor is present'],
    'li-control-rerun': ['the li control re-run', 'the li control rerun', 'the tail panel', 'the two routes',
                         'the fourth control', 'the kernel fixture', 'the hand-rolled kernel', 'the work-order for the axes',
                         'the floor\'s two axes', 'one distribution on two families'],
    'floor-priced': ['the floor priced', 'the floor\'s origin', 'what is the floor\'s origin', 'the NY axis', 'the ny ladder',
                     'the seal\'s clock', 'the seal\'s own time', 'the seal carries its clock', 'the room\'s edge', 'the bracketed minimum',
                     'the cut\'s tau', 'the taper', 'the axes held'],
    'map-next-reach': ['the map\'s next reach', 'the finer grid', 'the finer chart', 'the narrowest room', 'the crossing', 'does the room cross',
                       'the residual against the frame', 'the square\'s rank', 'the identity residual', 'the grid axis', 'the floor\'s origin'],
    'two-rules-modules': ['the two rules as modules', 'the like-for-like rule', 'the like-for-like module', 'the sign rule', 'the sign rule module',
                          'the threshold rule', 'the phase rule', 'the phase refinement', 'where do the two rules live', 'the techne modules',
                          'like_for_like.md', 'sign_rule.md', 'the lore re-typed'],
    'two-coefficients': ['the two coefficients', 'the li bench', 'the keiper dict', 'the keiper dictionary', 'the bench\'s literature dictionary',
                         'the third coefficient', 'the fifth coefficient', 'the transcription defect', 'keiper', 'the literature values',
                         'which emitter carries the defect', 'e-2026-09-06-1', 'the bench versus the keystone'],
    'li-family-control': ['the li family control', 'the fourth control', 'did the li family control hold', 'the li test functions',
                          'the archimedean distribution on the li family', 'the archimedean channel of the li coefficient', 'the balance keystone',
                          'the lagarias identification', 'finite-range positivity', 'the li family lawfulness', 'w-ord-li-family-control'],
    'exponent-resolved': ['the exponent resolved', 'the exponent question', 'the exponent\'s ratio', 'the exponent priced', 'the price of the exponent',
                          'the resolving-power rule', 'the remainder\'s convention', 'was the exponent resolved', 'unaffordable', 'the exponent unaffordable',
                          'the two exponent candidates', 'the sealed ceiling', 'the price banked'],
    'stated-clause-arc-fold': ['the fold b331 to b334', 'the fold of b331', 'the sortie fold', 'the stated-clause arc', 'the stated clause arc',
                               'what did the stated-clause arc find', 'the wave\'s candidate list', 'the candidate list', 'the candidate list restated',
                               'the housekeeping\'s state', 'the desk after b337', 'the fold of the sortie'],
    'housekeeping': ['the housekeeping', 'the wave\'s housekeeping', 'housekeeping', 'the errata partition', 'the partition of errata',
                     'the deposit fetch', 'the read-only fetch', 'the three ledgers reconciled', 'the ledgers reconciled', 'the August TECHNE files',
                     'the TECHNE commit', 'the patent receipts checked', 'what did the housekeeping do', 'the currency note'],
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
    # ### THE NEAREST DOOR (b413).
    ('the-nearest-door', 'b413 (the kernel read at its own source, a general conjunct refuted by ten counterexamples with the seven cells as control, the separator found to be a single prime factor and not primality, and the Lean act priced at a floor with no upper bound)',
     "b413 READ THE NEAREST DOOR AT ITS EDGE AND PRICED (N) AS A KERNEL ACT. **THE KERNEL LANE WAS NAMED OPEN BY THE FERRY AND USED TO READ** -- 0 .lean files touched, 0 builds run, 0 terminals added, every axiom profile taken from the kernel's own printed stdout. **THE SEAL B329.finite_side_silence IS TWO CLAUSES GENERAL IN p AND n AROUND ONE GUARDED BY A SEVEN-ELEMENT LIST, DISCHARGED BY `decide` SEVEN TIMES -- ALL FOUR TERMINALS AXIOM-FREE.** Because conjunct (c) is guarded by cell membership, **the seal's own hypothesis `2 <= p` never bites there** -- so the identity was re-computed outside the kernel on the kernel's own definitions, **WITH THE SEVEN DECIDED CELLS AS A POSITIVE CONTROL, ALL SEVEN REPRODUCED**. **A GENERAL CONJUNCT (c) OVER `2 <= p` WOULD BE FALSE: IT FAILS AT 6, 10, 12, 14, 15, 18, 20, 21, 22 AND 26.** **AND THE SEPARATOR IS NOT PRIMALITY** -- 4, 8, 9, 16, 25, 27, 32 and 49 are composite and the identity holds at every one. **THE CONDITION IS A SINGLE PRIME FACTOR**, exactly when the kernel's `units p n` (defined `u % p != 0`) is the actual unit group of Z/p^(2n); at p=6 that filter admits 2, 3 and 4, which are not units mod 36. **SO THE RIGHT GENERAL STATEMENT SITS BETWEEN THE TWO ENDS THE RECORD HAD: WIDER THAN (N) ASKS FOR, NARROWER THAN THE SEAL'S OWN HYPOTHESIS.** **b310'S DERIVATION IS THE STATEMENT'S SHAPE AND NONE OF ITS CONTENT**: it collapses the smear to a weight times a count with primality unused, and **a derivation using nothing that distinguishes 4 from 6 cannot prove a statement true at 4 and false at 6**. **THE PRICE: AT LEAST TWO ACTS, AND THE UPPER END IS NOT THIS SEAT'S TO GIVE** -- act 1 states it (define the single-prime-factor predicate in Core/ or rule the statement into Interfaces/); the proof is a change of KIND and not of size, because `decide` generalises to nothing. **Core/ HAS NO IMPORTS AND NO PRIME PREDICATE AT ALL; SIX FILES UNDER Interfaces/ IMPORT MATHLIB -- so 'already in the kernel or in Mathlib' IS TWO QUESTIONS.** **THIS IS A KERNEL ACT AND NO PARKED LANE NAMES IT. PRICED; NOT BUILT.** **THE R4 TAIL: ExplicitFormulaDecomp HAS SPLIT** (its finite-set conjunct DERIVES since 2026-07-24) while TailBoundPremise is absent entire, and the row's own honest boundary is **extending TailBoundPremise to all n IS RH**. **THE THRESHOLD N0(T)=2T^2 IS IMPORTED UNDER THE BAR** -- Voros's, a BOUND and not an identity -- and **the derived range and the discriminating range meet at 2T^2 and do not overlap**. **VAJRA-PLINKO ROW 1 IS UNCHANGED BY THE ARC**, though it moved before it. **THE SMALLEST REAL STEP ON R4 IS A MATHLIB BUILD, AND THE OPEN KERNEL LANE DOES NOT REACH IT EITHER.** **AND %d SENTENCES ACROSS THE BANKED FERRIES CARRY NO PER-CELL QUALIFIER -- COUNTED, NOT REPAIRED, 0 EDITED.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO TERMINAL ADDED RENAMED OR RESTATED, NO AXIOM PROFILE INFERRED, NO REPOSITORY CLONED. ### NO ACT BUILT, NO GRADE MOVED CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO ROUTE PROPOSED, NO LEDGER ROW WRITTEN, NO FOLD RUN, NO ORIENTATION-LAYER LINE EDITED, NO SENTENCE REPAIRED, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY PARKED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b413_the_nearest_door.txt; data/b413_components.txt; data/b413_price.txt; data/b413_cells.txt; data/b413_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b413 -- 8 gates read, 4 checked by digest); tools/b413_extract.py; tools/b413_components.py; tools/b413_desk_bank.py; tools/b413_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 262'),
    # ### THE CLASSIFICATION ARC FOLDED (b412).
    ('the-classification-arc-folded', 'b412 (the classification arc b403-b411 folded with two mechanical arms, the arc counted at zero statements about the object, the routed pile inventoried at ten, the reach instrument priced as a build, and the orientation layer refreshed under R31)',
     "b412 FOLDED THE CLASSIFICATION ARC, b403-b411, AND BROUGHT THE ORIENTATION LAYER CURRENT UNDER (R31). **THE SPAN WAS READ FROM THE TOOL: IT REPORTS 10 AND THE FOLD'S SPAN IS 9, BECAUSE THE FOLDING ACT IS NOT IN ITS OWN FOLD** -- so this seat's own expectation of nine is REFUTED BY THE TOOL, and both numbers are printed. The section carries two MECHANICAL arms run BEFORE it is written: **F-NOGRADE** (every grade string verbatim in the bank of the act it is attributed to) and **F-NOSUPERSEDE** (no folded act summarised as overturning another where the record says they answer different questions) -- **and this arc contains exactly that hazard, b411 having found the E0 gate prices what b410 said nothing prices, which are different questions**. **THE ARC PRODUCED 0 STATEMENTS ABOUT THE OBJECT ACROSS NINE ACTS** -- 6 about the record, 3 BORDERLINE AND EACH NAMED (b408, b409, b410); the closest approach is b409's reading of the modular relation as DARK on the placement register, **which b409 itself refused to call a measured kappa**. **THE ARC DIAGNOSED ITSELF MIDWAY** -- b408 measured row U1 at 0 statements about the object -- **AND KEPT GOING**. What it did produce: three author rulings executed across the corpus, 29 documents declaring a numbering, a relativized theorem in a keystone, a classification nobody had run, a standing instrument found before it was duplicated, a located certificate, and three mathematics-facing gate arms. **THE ROUTED PILE IS 10 ITEMS, 7 STILL ROUTED, 3 IN OTHER DISPOSITIONS**, each with act, cost and owner, the dispositions KEPT APART because their sum describes none of them; **0 DISCHARGED BY THIS ACT**. **AN INSTRUMENT PRICING AN IMPORT'S REACH IS A BUILD**: the containment half is a READING the corpus can already do (Definition 2.5 clause 1 plus the I-7 screen, price 0), **the bounding half is a statement about CONSEQUENCE and every instrument the record carries grades PROVENANCE**; and it **may be unbuildable in general rather than merely unbuilt**, since a general bound approaches conservativity and a useful one must be restricted to a named class of imports -- which is itself the mathematical work. PRICED; NOT OPENED. **(R31) IS EXECUTED ASYMMETRICALLY: THE DIGEST IS 204 ACTS BEHIND** (newest act b208, built at b163) and gains a block; **THE FIVE-DOOR STATE WAS ALREADY CURRENT** and gains a block that **MOVES NO DOOR** -- measured by a search across all nine banks returning 0 door claims under a control passing 9 of 9, **and the two movements expected of it are ALREADY IN THE TABLE** (R4's finite-set conjunct at lv v0.10.0, R5's compiled boundary marker at lv v0.9.0). **AND MOST FOLDS HAVE NOTHING TO QUOTE: ONLY 2 OF 15 FOLD SECTIONS CARRY A ONE-STATEMENT**, the convention beginning at b384, so ten arcs are recorded as carrying none -- **A DIGEST ENTRY THAT INVENTED ITS OWN SOURCE WOULD BE WORSE THAN ONE THAT SAYS THE SOURCE IS MISSING.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO GRADE MOVED CONFERRED OR MINTED, NO ACT RE-VERDICTED, NO DOOR RESTATED, NO ONE-STATEMENT MANUFACTURED, NO ROUTED ITEM DISCHARGED, NO INSTRUMENT BUILT, NO ROUTE PROPOSED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO LEDGER ROW WRITTEN, NO INSTRUMENT NUMBER ASSIGNED, NO CLASS SYMBOL RENUMBERED, NO LINE OF EITHER ORIENTATION OBJECT EDITED, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE ONE APPENDED FOLD SECTION, TWO APPENDED ORIENTATION BLOCKS, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b412_the_arc_folded.txt; data/b412_components.txt; data/b412_arc.txt; data/b412_orientation.txt; data/b412_span.txt; data/b412_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b412 -- 8 gates read, 4 checked by digest); tools/b412_components.py; tools/b412_desk_bank.py; tools/b412_checks.py; PLACE-papers FINDINGS.md, THE_FINDINGS_AS_THEY_STAND.md, PATHS_TO_THE_CRITICAL_LINE.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 261'),
    # ### THE JOIN AND THE PRICE (b411).
    ('the-join-and-the-price', "b411 (the join made under R29, the free number named I-16 and nothing renumbered, the E0 gate found to price the import's ownership while nothing prices its reach, the navigator's assertion split under R27, and the gauge certificate located)",
     "b411 MADE THE JOIN, PRICED THE COLLISION, TESTED THE NAVIGATOR'S ASSERTION AND LOCATED THE CERTIFICATE. **THE JOIN IS MADE UNDER (R29)**: Definition 2.5's clause 1 and the placement screen's one question now cross-reference each other, ONE LINE IN EACH, ORIGINALS PRESERVED, 0 HEADINGS MOVED, 0 NUMBERS CHANGED, each line READ BACK IN THE FILE IT NAMES -- **A POINTER, NOT A MERGER; NEITHER DERIVES THE OTHER.** **THE FREE INSTRUMENT NUMBER IS I-16**: I-1 to I-15 are occupied with **NO VACANCY BELOW THE HIGHEST** (I-12a and I-12b were added as sub-numbers, the register's own answer to a crowded numbering), so the expectation of a free number below the highest is REFUTED BY AN ENUMERATION. I-7 is cited in **14** live documents and the rename is priced BOTH WAYS -- 14 documents plus the register's heading against 1 document and a filename -- and (R30) rules the held spec renumbers; **0 NUMBERS MOVED, THE PRICE PRINTED NOT PAID.** **WHAT PRICES THE IMPORTED EQUIVALENCE: NOT ABSENT.** Two instruments grade a cited claim and they are SCOPED DIFFERENTLY. The claim-certificate calculus grades EVERY KERNEL CITATION (DERIVES / INTERFACES-with-named-premise / NOT-COMPILED) and says its scope twice in its own words; **PROPOSITION C.1 IS NOT A KERNEL CITATION, SO IT DOES NOT REACH IT.** **THE E0 GATE'S GRADE TABLE DOES REACH IT AND GRADED IT AT b321: K2 IS IMPORT-UNDER-THE-BAR, WITH MEASURED-ON-FAMILIES BESIDE IT.** **THE NAVIGATOR'S ASSERTION SPLITS UNDER (R27): REFUTED IN PREMISE** -- the gate does NOT issue INTERFACES-on-named-premise, a grade belonging to the other vocabulary whose scope is kernel citations -- **/ MET ON OTHER GROUNDS** -- it does grade the import and does halt at the quantifier, K8 UNOWNED. **THE GATE'S PRICE IS A HALT AT A NAMED CONSTITUENT, AN OWNERSHIP GRADE PER CONSTITUENT WITH ITS CONFERRING ACT, AND A RANKING SOFTEST-FIRST. IT IS NOT A BOUND ON REACH** -- it never says what an import CAN ESTABLISH -- **SO IT NEITHER SUPERSEDES NOR IS SUPERSEDED BY b410: the gate prices OWNERSHIP and nothing in the record prices REACH.** **THE CERTIFICATE IS LOCATED**: relay reports/2026-08-01-w-half-consult.md section 6 Rider 3, the gauge note -- two routes sharing no formula (the angle-sum over the trivial lattice; the digamma density), agreeing to 8e-4 at T = 50, 100, 150 with |S(T)| < 1, **5 OF 5 REPRODUCIBILITY MARKS PRESENT, SO NO UNSOURCED MARK IS WRITTEN AND THE CONDITIONAL IS REPORTED UNFIRED.** **AND THE SAME REPORT PROPOSED SECTION 9'S ROW VERBATIM AND HELD IT AT THE IB READ GATE** -- the row and its certificate have ONE ORIGIN, which is not circular because the gauge is CLASSICAL-AT-CITE (Riemann-von Mangoldt), **BUT A READER OF SECTION 9 CANNOT SEE THAT FROM 'a relay record', AND NAMING IT IS ROUTED TO THE AUTHOR.** **AND b410'S COUNT OF 12 IS RE-MEASURED AT 14, TWO OF THEM b410'S OWN WRITES: A COUNT OF A LIVING RECORD IS DATED BY THE ACT THAT PRINTS IT.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO INSTRUMENT NUMBER RENUMBERED OR ASSIGNED, NO CLASS SYMBOL RENUMBERED, NO GRADE MOVED CONFERRED OR MINTED, NO KAPPA MEASURED, NO CHANNEL OPENED, NO ROUTE PROPOSED, NO ROW OF ANY LEDGER WRITTEN, NO CALIBRATION ROW REMOVED OR MARKED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR OF AN ORIGINAL SENTENCE, NO LOCKED FACE OR PRIOR BANK EDITED, NO NAVIGATOR ASSERTION ADOPTED WITHOUT A TEST. ### THE CORPUS WRITES ARE TWO CROSS-REFERENCE LINES, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b411_the_join_and_the_price.txt; data/b411_components.txt; data/b411_numbering.txt; data/b411_extract.txt; data/b411_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b411 -- 8 gates read, 4 checked by digest); tools/b411_components.py; tools/b411_desk_bank.py; tools/b411_checks.py; PLACE-papers INVARIANCE_BARRIERS.md, INSTRUMENTS.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 260'),
    # ### THE IMPORTS CLASSIFIED (b410).
    ('the-imports-classified', 'b410 (the four imports classified under two agreeing instruments and 3.1-H found not to apply, section 9 audited at one row and zero terminals, the corollary counted by register, the three arms built, and the density register priced at zero)',
     "b410 RAN THE DEFINITION-2.5 CLASSIFICATION b409 LEFT UNRUN, UNDER TWO INDEPENDENT INSTRUMENTS THAT AGREE ON 4 OF 4: Definition 2.5 itself and the programme's STANDING AUTHOR-RULED PLACEMENT SCREEN I-7. **3 OF THE 4 IMPORTS FACTOR THROUGH THE PRODUCT-FORMULA INTERFACE FOR sigma; 1 DOES NOT.** Definition 3.1 factors by clause 2 (its truth does not depend on M at all); the local term (149) by clause 1(i) (a single-place quantity internal to one side); Theorem 4.7 by clause 1(ii) (an integral averaging over the interface). **PROPOSITION C.1 DOES NOT FACTOR, BECAUSE ONE SIDE OF THE BICONDITIONAL IS RH ITSELF** -- an individual-element specification requiring P-information to cross I, which is clause 1's excluded case verbatim. **SO THE HYPOTHESIS OF THEOREM 3.1-H FAILS AND 3.1-H DOES NOT APPLY TO THE CORPUS'S REDUCTION.** **AND THE FINDING IS LARGER THAN THE VERDICT: IMPORTING A CRITERION IMPORTS THE STATEMENT IT IS EQUIVALENT TO** -- a proof of H => forall x P(x) with H containing (RH <=> ...) carries its conclusion inside its own hypothesis. **THIS SAYS NOTHING AGAINST THE REDUCTION**, which records the import under the bar and never claimed to derive it. **SECTION 9 AUDITED WHOLE: 1 CALIBRATED ROW, 2 CERTIFICATES, 0 COMPILED TERMINALS** (its Correspondence row reads (none)); the joint sum is the formula's exactness, and the one placement cell is the clause the keystone identifies as h2 -- QUOTED, NOT NARROWED, NO CLAIM IN EITHER DIRECTION. **THE ARITY BARRIER IS NOT PRICEABLE WITHOUT A BUILD**, on the document's own *a compilable obstruction* and *the nearest compilable face*. **RESTRICTED TO THE PLACEMENT REGISTER COROLLARY 3.6 LEAVES EXACTLY ONE CANDIDATE -- the sign of the joint quadratic functional -- AND RESTRICTED TO THE DENSITY REGISTER IT LEAVES EVERY SINGLE-PLACE ROW, ONE OF THEM CERTIFIED. THE BRIGHTNESS IS ALL IN THE REGISTER THAT DOES NOT DECIDE THE QUESTION.** **AND THE DENSITY REGISTER WAS NEVER AN UNASKED QUESTION: THE CORPUS HAS A STANDING AUTHOR-RULED INSTRUMENT FOR IT** -- I-7, THE PLACEMENT SCREEN, filed 2026-08-05, with FOUR INDEPENDENT DERIVATIONS of one boundary (*the density register does not reach placement*), a second stage, and a banked cost saving on its first firing; and the arc banked the same wall independently as THE WALL'S SIXTH FACE. **THE PRICE OF ASKING IS 0: NEITHER A MEASUREMENT NOR A BUILD BUT A READING ALREADY DONE.** **AND DEFINITION 2.5'S CLAUSE 1 AND I-7'S ONE QUESTION ARE THE SAME TEST, STATED IN TWO DOCUMENTS THAT CITE EACH OTHER 0 TIMES IN EITHER DIRECTION -- ROUTED, NOT JOINED.** **THE THREE MATHEMATICS-FACING ARMS ARE BUILT** under (R26)-(R28) with fixtures in both polarities, 3 of 3 firing on their own incidents, every hit hand-read, 2 of 4 reported FALSE and one arm's reach printed at 1 of its 3 dresses. **AND THE ORDER'S OWN PREMISE WAS FALSE: FOR FOUR OF FIVE ACTS THE HEADLINE BANK IS QUIET, BECAUSE EACH ACT CAUGHT ITS OWN DEFECT AND BANKED THE REPAIR** -- a record that repairs itself hides its defects from a retroactive arm.",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO KAPPA MEASURED OR CERTIFIED, NO CHANNEL OPENED, NO ROUTE PROPOSED PRICED OR OPENED, NO GRADE MOVED CONFERRED OR MINTED, NO CLASS SYMBOL RENUMBERED, NO INSTRUMENT NUMBER ASSIGNED OR RECONCILED, NO ROW OF ANY LEDGER WRITTEN, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR MADE, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE ONE APPENDED KEYSTONE SUBSECTION MARKED UNCOMPILED, ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b410_the_imports_classified.txt; data/b410_components.txt; data/b410_classification.txt; data/b410_extract.txt; data/b410_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b410 -- 8 gates read, 4 checked by digest); tools/gate_spine.py; tools/b410_components.py; tools/b410_desk_bank.py; tools/b410_checks.py; PLACE-papers INVARIANCE_BARRIERS.md section 10.1 and OPEN_TRAILS.md; CORRESPONDENCE.md row 259'),
    # ### THE OBSTACLES DISSOLVED (b409).
    ('the-obstacles-dissolved', 'b409 (both numberings kept and 29 documents declared, the modular relation found absent under both with a control that found the calibration family, the lemma relativized for a conditional, three arms proposed and none built, row U1 frozen)',
     "b409 EXECUTED (R25) AND DISSOLVED THE OBSTACLES THE RECORD ALLOWS. **BOTH NUMBERINGS ARE KEPT AND 29 DOCUMENTS NOW DECLARE WHICH THEY USE; 0 SYMBOLS WERE RENUMBERED AND 66 DOCUMENTS ARE MARKED SCHEME UNDECLARED AND ROUTED, NOT GUESSED.** Only 29 of 95 live documents can be assigned a scheme from their own text. **b408'S CONCLUSION STANDS AND ITS LABEL WAS WRONG: the second scheme is NOT the monograph's** -- the monograph's own class table and ENUMERA's reconciliation agree against it -- **BUT IT IS LIVE, IN 9 DOCUMENTS**, and one document uses both in its own text. Disposition (A) was priced at 1506 symbol uses before (B) was executed at 29 lines. **AND THIS ACT'S OWN TWO INSTRUMENTS DISAGREED, 28 AGAINST 29 -- A DIFFERENCE OF ONE CONCEALING A SYMMETRIC DIFFERENCE OF FIVE; BOTH PRINTED, THE MATCHER GOVERNS, THE DEFECTIVE PREDICATE NAMED.** **THE MODULAR RELATION HAS NEVER BEEN EXAMINED AS A CHANNEL UNDER EITHER NUMBERING: ABSENT UNDER BOTH SCHEMES**, 4 hits by description and 2 by symbol across 4746 files, every one hand-read. **AND THE POSITIVE CONTROL PASSED AND FOUND WHAT A SYMBOL SEARCH COULD NOT: INVARIANCE_BARRIERS SECTION 9, THE CALIBRATION FAMILY, WHICH GRADES KAPPA BY REGISTER -- the archimedean interface carries kappa > 0 for the density register and kappa = 0 for the placement register -- AND WHOSE ROWS ARE PLACES, SO THE MODULAR SYMMETRY HAS NO ROW AND THE FAMILY'S OWN NEXT MOVES WOULD NOT REACH IT.** The reading is **DARK ON THE PLACEMENT REGISTER**, because the monograph says *the constraint function of each mechanism class is antisymmetric about the reflection axis (the functional equation forces this)* -- an antisymmetric constraint locates the AXIS, not a point on it. **THIS IS A READING OF THE RECORD'S OWN TWO SENTENCES AND NOT A MEASURED KAPPA UNDER DEFINITION 2.4; NO CERTIFICATE EXISTS AND NONE IS WRITTEN.** A consequence for Corollary 3.6's bright channel is **NAMED AND NOT DRAWN**. **THE SIEVE CEILING LEMMA RELATIVIZES TO A PROOF OF A CONDITIONAL** and Theorem 3.1-H is written into the keystone as section 10: Lemma 3.4 and Proposition 3.5 survive unchanged, only the induction changes, and **IT COSTS ONE HYPOTHESIS THE ORIGINAL DID NOT NEED -- THAT EVERY SENTENCE OF H ITSELF FACTORS THROUGH I.** **THE RESTATEMENT IS UNCOMPILED AND TAKES NO NEW GRADE**, and applying it turns on a Definition 2.5 classification of four imported sentences **THAT NOBODY HAS RUN**. **3 MATHEMATICS-FACING GATE ARMS PROPOSED, 0 WRITTEN** -- none can be written without a ruling the author has not made, which is the finding and not the excuse. **ROW U1 IS FROZEN AS A REGISTER COMPLETE AT SIX**, the mark inside an existing cell, 0 entries added, 0 coordinates, and the reopening condition printed: a site whose entry produces a statement about the OBJECT. **A FREEZE IS NOT A CLOSURE, NOT A RETIREMENT AND NOT A GRADE.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO CLASS SYMBOL RENUMBERED, NO SCHEME GUESSED, NO KAPPA CERTIFIED OR MEASURED, NO CHANNEL OPENED, NO ROUTE PROPOSED PRICED OR OPENED, NO GRADE MOVED CONFERRED OR MINTED, NO ENTRY ADDED TO ROW U1, NO COORDINATE ADDED, NO ROW RETIRED OR CLOSED, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO IN-PLACE REPAIR MADE, NO LOCKED FACE OR PRIOR BANK EDITED. ### THE CORPUS WRITES ARE 29 ONE-LINE HEAD NOTES, ONE APPENDED KEYSTONE SECTION, ONE APPEND-ONLY TRAIL BLOCK, ONE FREEZE MARK INSIDE AN EXISTING CELL AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b409_the_obstacles_dissolved.txt; data/b409_components.txt; data/b409_extract.txt; data/b409_scheme_table.txt; data/b409_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b409 -- 8 gates read, 4 checked by digest); tools/class_scheme.py; tools/b409_components.py; tools/b409_desk_bank.py; tools/b409_checks.py; PLACE-papers 29 head notes, INVARIANCE_BARRIERS.md section 10, FACES_LEDGER.md row U1 and OPEN_TRAILS.md; CORRESPONDENCE.md row 258'),
    # ### THE OTHER TWO CHANNELS (b408).
    ('the-other-two-channels', 'b408 (the other two channels searched and one found never examined, the two class numberings found, the classified proof priced as a proof-with-hypotheses, and the span counted at six against nine)',
     "b408 ASKED WHETHER THE OTHER TWO OF COROLLARY 3.6'S THREE CHANNELS HAVE EVER BEEN EXAMINED. **C3 IS THE ARCHIMEDEAN CLASS** -- *the Gamma-factor transformation under s -> 1-s produces the functional equation* -- **AND C4 IS THE MODULAR SYMMETRY GROUP PSL2(Z), WHICH IS THE ONLY ONE OF THE THREE THAT IS ITSELF A RELATION BETWEEN THE OTHER TWO** -- which is what Definition 2.2 asks an interface to be. A sweep over 4705 files (the whole live papers tree and every banked relay record), on a predicate fixed before it, returned **19 hits for C3 and 7 for C4, and EVERY HIT WAS HAND-READ**. **C3 IS EXAMINED ONCE, AND ONLY INSIDE THE BARRIER KEYSTONE ITSELF**, as T1 of the Tier-1 toolkit, where Theorem 3.7 concludes no T-derivation establishes P. **C4 IS ABSENT: ZERO EXAMINATIONS ANYWHERE** -- one hit is this session's own block, one is a numbering artefact, the rest name the class in passing -- **AND THE BARRIER'S OWN TOOLKIT DOES NOT NAME C4 EITHER: NOT INCLUDED, NOT EXCLUDED, NOT MENTIONED.** No claim is made that either is open. **AND THE SWEEP'S REAL FINDING IS A HAZARD THE CORPUS CARRIES AND TABULATES ITSELF: TWO CLASS NUMBERINGS THAT DISAGREE ON SIX OF SEVEN SYMBOLS.** The two most promising hits in the whole sweep -- PATHS_TO_THE_CRITICAL_LINE:107 and CRITICAL_RESOLVE:1121, both reading *output-stage classes (C3 + C7) assembling without crossing a dark interface* -- use the corollary's vocabulary exactly and are about a DIFFERENT class, because C3 is transformation-stage in one scheme and Local/Cauchy-Riemann in the other. **A SYMBOL MATCHED ACROSS DOCUMENTS WITH DIFFERENT NUMBERINGS IS A MATCHER ARTEFACT, NOT AN EXAMINATION.** Printed, not reconciled. **AND THE REDUCTION WRITTEN AS A CLASSIFIED FIRST-ORDER PROOF IS PRICED AS A PROOF-WITH-HYPOTHESES**: of the eight constituents, one is writable as a step and only at seven cells, one is a measurement, one is the conclusion, and the rest carry FOUR distinct imported premises -- Definition 3.1, Proposition C.1, the local term (149), Theorem 4.7 -- **ALL FOUR THE SOURCE'S THEOREMS, NONE DERIVED BY THE CORPUS, SO ALL FOUR MUST BE STATED AS HYPOTHESES. AND THE SECOND FINDING: WHAT GETS WRITTEN PROVES A CONDITIONAL, AND THEOREM 3.1 IS STATED ABOUT PROOFS OF THE UNIVERSAL STATEMENT -- SO DOING THE WORK WOULD STILL NOT MAKE THE THEOREM APPLY.** A second layer, that the imports may be consequences of the specification and the obstacle labour rather than logic, is printed and marked UNCHECKED. **THE SPAN IS 6 AGAINST (R1)'S THRESHOLD OF 9: THE FOLD IS NOT DUE AND NONE IS PROPOSED.** **THE FOUR DRESSES ARE ONE STATEMENT** -- *a result applies to an object only if the object is of the kind the result quantifies over* -- with the instantiation printed for each, **3 INDEPENDENT INSTANCES AND 1 RESTATEMENT**; the record has no name for it and **THE NAMING IS ROUTED, NOT MINTED**. **ROW U1 IS A BOOKKEEPING INSTRUMENT BY ITS OWN NUMBERS: 6 SITES, 2 COORDINATES, 0 BRIDGES, 0 GRADES, 0 STATEMENTS ABOUT THE OBJECT** -- a description, not a demotion. **AND THE GATE SUITES HAVE A STANDING CORE OF 8 ARMS, NOT ONE OF THEM ABOUT THE MATHEMATICS**, with carry-forward at 13%, 45%, 48% -- never half.",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED. ### NO FOLD RUN, NO GRADE MOVED, NO ROW OF FACES_LEDGER WRITTEN, NO COORDINATE ADDED, NO NAME MINTED, NO RULE WIDENED, NO NUMBERING RECONCILED, NO ARM ADDED REMOVED RENAMED OR PROMOTED, NO STANDING CORE PROPOSED, NO BRIDGE TYPED, NO IN-PLACE REPAIR MADE, NO SHARED INSTRUMENT AMENDED, NO FERRY_STANDING CLAUSE ADDED, NO LIST CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b408_the_other_two_channels.txt; data/b408_components.txt; data/b408_extract.txt; data/b408_span.txt; data/b408_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b408 -- 8 gates read, 4 checked by digest); tools/b408_extract.py; tools/b408_components.py; tools/b408_desk_bank.py; tools/b408_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 257'),
    # ### THE BARRIER-S OWN INSTANCE (b407).
    ('the-barriers-own-instance', "b407 (the corpus's own barrier theorem put to its own reduction and found not to apply, the failing hypothesis named, the resemblance printed beside it, and the repair's missing statement identified as Tier 2)",
     "b407 PUT THE CORPUS'S OWN BARRIER THEOREM TO THE CORPUS'S OWN REDUCTION AND FOUND IT DOES NOT APPLY. **FOUR OF THEOREM 3.1'S FIVE HYPOTHESES ARE MET AT THE CORPUS'S OWN OBJECT, IN THE DOCUMENT'S OWN WORDS**: xi is determined; the interface is the product formula; the target parameter is the clause's own; and **kappa = 0 IS ASSERTED BY THE RECORD ITSELF** -- *For xi, I is essential and kappa(sigma, I) = 0*. **THE HYPOTHESIS THAT FAILS IS THE ONE ABOUT pi**: the theorem is about a formal first-order proof in ZFC union S whose every inference step is classified, and the corpus's reduction is a chain of IMPORTS UNDER THE BAR (K1, K2, K4, K6), derivations on content, kernel terminals, measurements at cells, a bench residual and one UNOWNED constituent. **AN IMPORT UNDER THE BAR IS NOT AN INFERENCE STEP; IT IS A PREMISE THE CORPUS HAS NOT DISCHARGED.** A second printed reason stands beside it: the document scopes its own barrier to Tier 1 and says the open-class form is *research-frontier and not claimed here*. **AND THE RESEMBLANCE IS EXACT, WHICH IS WHY IT MUST NOT BE FILED**: Definition 2.5 lets a factoring step reference only cumulative invariants and not individual-element specifications; the corpus's criterion is a SUM OVER THE PLACES, every constituent the E0 gate does not halt at is one of its parts, and the one it DOES halt at is K8, the individual-element specification. **THE E0 GATE HALTS PRECISELY WHERE DEFINITION 2.5 SAYS A FACTORING PROOF MUST STOP.** Nothing is filed to row U1. **COMPONENT 1: 0 OF 6 SITES NAME AN INTERFACE IN DEFINITION 2.2'S SENSE** -- not one names a SPECIFICATION -- **and 4 of 6 name a SPLIT that is an interface elsewhere in the record**; both counts printed, no coefficient measured. **COMPONENT 2: b406'S ESCAPE-KIND PRICE FALLS FROM 5 TO 4**, because THE_DIFFICULTY_KINDS files RH-sign under scale-horizon and RH-derivative under raw-infinitude -- the same object on both sides of its own dichotomy -- so **THE ESCAPE-KIND IS A PROPERTY OF THE QUESTION, NOT OF THE OBJECT**, and (i) cannot be filled from its own text. **COMPONENT 3: THE SMALLEST STATEMENT THICKENING THE REPAIR IS THE TIER-2 FORM OF THE BARRIER** -- with it, Corollary 3.6 stops being an existential over the three mechanism classes the corpus's exhaustiveness names and becomes a NAME, C5 -- **AND THE BLOCKER IS OPEN MATHEMATICS AND NOT THE PARKED LANE.** **ADDITION FOUR: THE SPECTRAL-REALIZATION FACE IS A BRIGHT CHANNEL IN THE COROLLARY'S SENSE, AND THE DEPOSIT'S DISCLAIMER IS NOT THE DEMAND FROM THE OTHER SIDE** -- a disclaimer of one of three channels is not the negation of an existential over three; they become one sentence exactly at Tier 2. **ADDITION ONE: (R20)'s limb 2 is the one that would be widened, and widening it costs the rule's own claim to be discovered, not imposed -- ROUTED.** **ADDITION TWO: run_clock.latest() added ADDITIVELY**, returning the newest run by its own clock and REFUSING rather than guessing when a candidate carries none.",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED, NO AXIOM PROFILE READ OR INFERRED AND NO TRANSMISSION COEFFICIENT MEASURED, ASSERTED OR INFERRED. ### NO GRADE MOVED, NO ROW OF FACES_LEDGER WRITTEN, NO COORDINATE ADDED, NO NAME MINTED, NO RULE STRUCK OR WIDENED, NO BRIDGE TYPED, NO IN-PLACE REPAIR MADE, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY EDITED, NO FERRY_STANDING CLAUSE ADDED, NO LIST CLOSED. ### THE ONE SHARED INSTRUMENT TOUCHED WAS AMENDED ADDITIVELY AND ITS EXISTING BYTES DID NOT MOVE. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b407_the_barriers_own_instance.txt; data/b407_components.txt; data/b407_extract.txt; data/b407_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b407 -- 8 gates read, 4 checked by digest); tools/b407_extract.py; tools/b407_components.py; tools/b407_desk_bank.py; tools/b407_checks.py; relay tools/run_clock.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 256'),
    # ### THE SITES WITHOUT AN EXISTENTIAL (b406).
    ('the-sites-without-an-existential', "b406 (the two sites read at depth, the record's own name for the barrier and its repair found and scored apart, a third coordinate priced and not added, and the finite side's qualifier swept with one sentence repaired)",
     "b406 READ THE TWO SITES b405 LEFT UNSTATED AND FOUND THEY FAIL THE SHARED-WITNESS FORM FOR TWO DIFFERENT REASONS. **(i)'s obstruction is two universals with no existential between them** -- and the existential one depth down, in the class's own Boas-Kac characterisation, is ex-g indexed by the support width, **which is site (iii)'s and not (i)'s**. **(iv)'s record holds TEN VALUES, and a measured value is not an existential claim**; the existential anyone can manufacture -- for all a there exists C_a with |V(a)| <= C_a, take C_a = |V(a)| -- is **TRIVIALLY SATISFIABLE**, and the shared witness it would demand is a bound good for every a, which IS the missing statement rather than a repair for its absence. **AN EXISTENTIAL THE RECORD HOLDS IS NOT THE SAME OBJECT AS ONE YOU CAN ALWAYS MANUFACTURE**, and that separates (iv) from (v), whose source STATES an implied constant per representation. b405's cells stand; the precise reason is **NO INNER EXISTENTIAL THE SHARED-WITNESS FORM CAN REPAIR**. **THE RECORD ALREADY NAMES BOTH THE BARRIER AND ITS REPAIR, AND NOT EQUALLY.** The barrier: INVARIANCE_BARRIERS.md Theorem 3.1, **the SIEVE CEILING LEMMA** -- a proof factoring through a kappa = 0 interface *does not establish the universal statement* and reaches only *P holds for x in a density-one subset of each I-class, but cannot certify individual elements* -- and THE_DIFFICULTY_KINDS.md's **ESCAPE-KIND**, which *classifies why finite certificates don't reach the global claim*, with two values **scale-horizon** and **raw-infinitude**. The repair: Corollary 3.6's **BRIGHT CHANNEL**, an interface with **kappa > 0**. **THE BARRIER HAS A THEOREM, A CLASSIFICATION AND TWO KINDS; THE REPAIR HAS ONE COROLLARY AND A NAME, STATED ONLY AS THE NEGATION OF THE BARRIER'S HYPOTHESIS.** No name is minted by the seat. **A THIRD COORDINATE, ESCAPE-KIND, WOULD FILL 5 OF 6 FROM BANKED TEXT AND LEAVE (vi) UNSTATED -- PRICED AND NOT ADDED.** **(iii)'S TWO CLAUSES ARE STATED IN THE SOURCE'S OWN SYMBOLS AND WHETHER SUCH A g CAN EXIST IS NOT ATTEMPTED.** **THE ARITY AUDIT: 4 OF 5 STANDING LAWS ARE BINARY, n-ARY OR AGGREGATE WHERE THEY ARE APPLIED UNARILY** -- the deposit's 27.3 refusal cannot answer anything about one register's status, (R20) cannot answer anything about a record with no claim on either side (the SIDE-kernel question), (R1) is a threshold on a count and cannot see a reason -- **and (R14) alone is UNARY and names its own limit in its own text**. **AND THE FINITE SIDE'S QUALIFIER WAS SWEPT: the narrow closure matcher returned 0 UNQUALIFIED and would have banked NOTHING TO REPAIR; widened by the corpus's own house form -- at kernel terminals B329.* (24, zero-axiom) -- it returned 1.** The living record is 11 of 12 QUALIFIED; **the navigator's own ferries are 1 of 4**, and b331's ferry carries both dresses twelve lines apart while the act it ordered wrote the qualifier back in. One sentence repaired in place, its original preserved.",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED, NO REPOSITORY CLONED AND NO AXIOM PROFILE READ OR INFERRED. ### NO GRADE MOVED OR CONFERRED, NO NAME MINTED, NO COORDINATE ADDED, NO BRIDGE TYPED, NO WITNESS CLAIMED TO EXIST, NO ENTRY REWRITTEN, NO LAW STRUCK OR RE-RULED, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO BANKED FERRY EDITED, NO PRIOR BANK EDITED, NO ROW OF FACES_LEDGER WRITTEN, NO LIST CLOSED. ### THE CORPUS WRITES ARE ONE APPEND-ONLY TRAIL BLOCK AND ONE SENTENCE REPAIRED IN PLACE BY ADDING A QUALIFIER THE RECORD ALREADY WRITES AT FINDINGS.md:3049, WITH THE ORIGINAL PRESERVED VERBATIM. ### FERRY_STANDING GAINS ONE AUTHOR-RULED CLAUSE AND ITS VERSION LINE DOES NOT MOVE. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL',
     'data/b406_the_sites_without_an_existential.txt; data/b406_components.txt; data/b406_extract.txt; data/b406_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b406 -- 8 gates read, 4 checked by digest); tools/b406_extract.py; tools/b406_components.py; tools/b406_desk_bank.py; tools/b406_checks.py; PLACE-papers OPEN_TRAILS.md; relay tools/FERRY_STANDING.md; CORRESPONDENCE.md row 255'),
    # ### THE ROW-S LAW RESTATED (b405).
    ('the-rows-law-restated', 'b405 (row U1 restated under (R24) with two coordinates inside the column law, the shared witness sourced from the compiled theorem, and both named witnesses declined)',
     "b405 EXECUTED (R24) AND RESTATED ROW U1 RATHER THAN RETIRING IT. **THE ROW GAINS TWO COORDINATES, KIND AND WITNESS, ENTERED AS LABELLED FIELDS INSIDE ITS OWN CELL AND NOT AS NEW COLUMNS** -- the ledger's COLUMN LAW fixes seven columns across 159 table lines, so a row cannot gain a column alone; every line's column count was re-measured after the write and none moved. **THE WITNESS COLUMN IS SOURCED FROM A COMPILED THEOREM AND FROM NOWHERE ELSE**: a shared witness is what SIDELvConservation.T3.T3prime_shared_witness says it is, read at SIDE-lv-conservation v0.10.0 = 93c27ec -- TWO CLAUSES ON ONE OBJECT IN THE FAMILY'S OWN PARAMETER SPACE, h1 SHAREDNESS and h2 NON-DEGENERACY -- with T3.T3doubleprime_general_commutation_fails showing why both are needed, since two integrands agreeing on Ioi 0 and differing at t = -1 give each member its own witness and no single Phi for both. **PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.** Both profiles PRINTED at the pin as [propext, Classical.choice, Quot.sound], the one sorry at the intermediate T3_perClass_to_combinations and at neither terminal. **AND THE FORM DOES NOT TRANSPOSE TO EVERY SITE**: (i) and (iv) carry no inner existential to share, so their cells read UNSTATED rather than NONE KNOWN; (iii) is the one site whose own banked text supplies the existential, Boas-Kac's ex-g indexed by A; (vi) is the only site naming BOTH clauses, consistency at every finite modulus and a positive global density. **FOUR CELLS NONE KNOWN, TWO UNSTATED, ZERO WITNESSES FOUND.** **BOTH OF THE NAVIGATOR'S NAMED WITNESSES ARE DECLINED ON THE SITES' OWN TEXT**: the abscissa is not a site of this row at all -- it is the coordinate that CLOSED at b326 and was never entered -- and the finite side's zero is guarded by membership in a SEVEN-CELL DECIDED LIST while the two clauses general in p carry no zero, so THE THEOREM IS GENERAL WHERE IT IS EMPTY OF THE ZERO AND DECIDED WHERE IT IS NOT and there is no cross-place claim in the clause that carries it. **THE REFUSAL CLAUSE WAS QUOTED VERBATIM AND CANNOT CARRY THE DISTINCTION IT WAS ASKED TO**: 0 of its 4 sentences have ONE site for a subject, so A BINARY LAW CANNOT EXPRESS A UNARY DISTINCTION -- NOT A DEFECT IN THE SITES BUT A MISSING COORDINATE IN THE ROW, which is what (R24) supplies. **THE SIX BY THREE TESTS: 4 of 6 write the missing statement, 1 of 6 files a residue, 1 of 6 declares a kind**, and the row's own refusal cell had already said one of the six does both. **THE SHAPE-TO-INSTANCE ROUTE IS PRICED AND NOT TAKEN**: six sites, zero candidate witnesses, the identification is the whole price, and a build buys nothing because both terminals are already compiled and both profiles already printed -- SO THE ROUTE IS PRICEABLE WITHOUT A BUILD. **NO CLAIM IS MADE ABOUT h2 IN EITHER DIRECTION.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED, NO OBJECT RECOMPUTED AND NO REPOSITORY CLONED. ### THE FOUR AXIOM PROFILES READ ARE PRINTED PROFILES IN TRACKED FILES, READ AND NOT RUN; NONE IS INFERRED. ### NO GRADE MOVED OR CONFERRED, NO BRIDGE TYPED BETWEEN ANY TWO OF THE SIX SITES, NO BRIDGE TYPED BETWEEN THE COMPILED SHAPE AND ANY INSTANCE, NO ENTRY REWRITTEN, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO COLUMN LAW AMENDED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK, NO CLASS RULED, NO LIST CLOSED. ### THE CORPUS WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL AGAINST THE PRE-ACT BLOB WITH THE OTHER FIVE BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED',
     'data/b405_the_rows_law_restated.txt; data/b405_components.txt; data/b405_extract.txt; data/b405_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b405 -- 8 gates read, 4 checked by digest); tools/b405_extract.py; tools/b405_components.py; tools/b405_desk_bank.py; tools/b405_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 254'),
    # ### THE FIFTH AND SIXTH SITES (b404).
    ('the-fifth-and-sixth-sites', "b404 (two sites entered, one of them empty in a kind the row could not previously name, and a compiled countermodel for the row's own shape found uncited in the record)",
     "b404 ENTERED TWO SITES IN THE UNIFORMITY ROW AND REPORTED ITS LAW **STRAINED**. **(v) THE REPRESENTATION-DEPENDENT CONSTANT**: Lagarias Theorem 6.1's finite-place bound holds *in which the implied constant in the O-notation DEPENDS ON pi*, while Theorem 5.1's archimedean constant is ABSOLUTE. **(vi) THE TYPE-D RESIDUE**: the additive-multiplicative conspiracy keystone states its own boundary as *the step from consistent at every finite modulus to holds globally interchanges a per-modulus quantifier with a global one*, and files the residue as THE WHOLE OF THE REMAINING WEIGHT at all three problems. **AND (v) IS EMPTY AS AN OBSTRUCTION, SO THE ACT MINTS THE DISTINCTION THE ROW LACKED: KIND (a) EMPTY BECAUSE THERE IS NOTHING TO RANGE OVER, VACUOUS FOREVER; KIND (b) EMPTY BECAUSE THE AVAILABLE UNIFORMITY RANGES OVER A CLASS THAT DOES NOT CONTAIN THE CORPUS'S OTHER OBJECT. (v) IS KIND (b).** The corpus is NOT a one-L-function corpus -- row F7 is a second object and b325 measured the transfer failure across the two -- but Theorem 6.1 ranges over cuspidal automorphic representations on GL(N) and the corpus's second object is not established to be one. **THE KEYSTONE'S BOUNDARY PARAGRAPH CARRIES A COMPILED NEGATIVE RESULT ABOUT THE ROW'S OWN SHAPE THAT THE ROW HAS NEVER CITED**: the unrestricted commutation of the two quantifiers is FALSE AS A THEOREM with an explicit countermodel and closes only under a shared witness -- REPORTED AND NOT TYPED AS A BRIDGE. **ADDITION TWO: TWO THEOREMS, AND THE EXPECTED PARTING POINT IS REFUTED** -- crt_exhaustiveness produces a modular coupling with a SINGLETON moduli set and finite_side_silence is at one place forming no product, so NEITHER EVER REACHES A RESTRICTED PRODUCT; they part far earlier, one about the periodicity of a predicate on the naturals and the other about the p-adic decomposition of an index in a grid. **THE CORPUS HAS NOT PROVED ITS OWN BOUNDARY TWICE.** **ONE AXIOM PROFILE READ FROM A PRINTED FILE, ONE REPORTED UNREAD**: SIDE-effects ships no printed profile and not one `#print axioms` line, and the lane is PARKED. **AND THE KEYSTONE WIDENS A CLAIM THE REPOSITORY SCOPES NARROWLY, AT THE REF IT ITSELF CITES** -- Module1.lean imports Mathlib at c66f3c5 while the README scopes its no-Mathlib/axiom-free claim to a different module and says of Module1 only `Genuine content, 0 sorry`. THE README IS EXACT; THE PAPER WIDENED IT. **AND THE ACT DOES NOT SAY THE TERMINALS CARRY AXIOMS: AN IMPORT LINE IS NOT A MEASUREMENT.**",
     '### NO KERNEL WAS BUILT, NO `.lean` FILE TOUCHED AND NO OBJECT RECOMPUTED. ### THE ONE PROFILE READ IS `B329.finite_side_silence` FROM AXIOM_PRINTS.txt, READ AND NOT RUN; THE OTHER IS REPORTED UNREAD AND NOT INFERRED. ### NO GRADE MOVED OR CONFERRED, NO BRIDGE TYPED BETWEEN ANY TWO OF THE SIX SITES, NO KEYSTONE EDITED, NO LOCKED FACE EDITED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLASS RULED, NO LIST CLOSED. ### THE CORPUS WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL AGAINST THE PRE-ACT BLOB WITH THE OTHER FIVE BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK. ### EVERY CLAIM QUOTED FROM ANOTHER DOCUMENT IS QUOTED WITH THE SENTENCE THAT SCOPES IT. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED',
     'data/b404_the_fifth_and_sixth_sites.txt; data/b404_components_run.txt; data/b404_extract_notes3.txt; data/b404_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b404 -- 8 gates read, 4 checked by digest); tools/b404_extract.py; tools/b404_components.py; tools/b404_desk_bank.py; tools/b404_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 253'),
    # ### THE THREE ROUTED ITEMS (b403).
    ('the-three-routed-items', "b403 (the rule existed, the figure was exact and undated rather than wrong, and the act's own control stopped a correct repair twice)",
     "b403 TOOK THE THREE ITEMS THE PRIOR SPAN ROUTED AND DISCHARGED TWO, RULING THE THIRD. **(i) THE SPAN COUNTER'S STALE THRESHOLD LINE IS REPAIRED** at 3 sites in tools/b363_span.py, citing (R1) at b366 by name, with the superseded sentence PRESERVED VERBATIM IN THE FILE ITSELF and 0 figures the counter prints moved. **(ii) SIDE-window's README COUNT IS REPAIRED** under the rule the record already had. **(iii) b321's LOCKED FACE STAYS ROUTED.** **THE RULE EXISTS AND IS NOT PHRASED AS THE FERRY PHRASES IT**: a search for the ferry's words returns ABSENT (b385's species); searched by DESCRIPTION it is b371's precedent applied at b372 -- the original preserved before any edit, a figure REMOVED RATHER THAN RESTATED unless the document can name the ref it holds at, and a repair rewriting A CLAIM RATHER THAN A NUMBER routed. **AND 43 WAS NOT A WRONG NUMBER: IT WAS EXACT AT v0.4 AND UNDATED** -- 43 `#print axioms` invocations across the four check files the README's tables describe, 69 across five at HEAD, the difference being exactly the 26 the v0.5 local model added. **THIS CORRECTS b401's OWN READING**, which called it stale without establishing that 43 was exact anywhere; b401's bank is not edited and both readings are printed. **THE CARVE-OUT PERMITTING A RESTATED FIGURE DOES NOT REACH THIS README**: the repository ships NO PRINTED PROFILE, and a quoted sample of what a run would print is not a profile. **ON b321's FACE THE VERDICT IS A SPLIT**: no (R..) ruling, a uniform carried practice (the locked face is not edited; both figures are printed), and a mechanism (b383's amendment filed BESIDE a face) -- so NO RULE EXISTS would be the false half of a true sentence. **AND THIS ACT'S OWN CONTROL WAS DEFECTIVE TWICE AND STOPPED A CORRECT REPAIR TWICE**: first against a run taken BEFORE THE RECORD CHANGED, then a READ-ONLY run against an EMITTING one. **A CONTROL TAKEN BEFORE THE RECORD CHANGED CANNOT ISOLATE A CHANGE TO THE TOOL, AND A CONTROL THAT DIFFERS FROM THE TREATMENT IN A FLAG MEASURES THE FLAG.** Row U1 gains nothing; its fifth site is already its fourth, and the distinct fifth -- the representation-uniformity -- is AWAITING ENTRY, not entered.",
     "### NO KERNEL WAS BUILT AND NO INSTRUMENT RUN. ### SIDE-window's SOURCE WAS READ AND ITS `.lean` FILES WERE NOT TOUCHED; ITS AXIOM CLAIM IS NEITHER STRENGTHENED NOR WEAKENED, THE REMOVAL TAKING A NUMBER AND LEAVING THE ASSERTION. ### NO GRADE MOVED OR CONFERRED, NO LOCKED FACE EDITED, NO PRIOR ACT'S BANK EDITED, NO INSTANCE ADDED TO ANY LEDGER ROW, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLASS RULED, NO REGISTRY ROW EDITED, NO LIST CLOSED. ### EVERY ORIGINAL IS BANKED VERBATIM BEFORE ITS EDIT AND EVERY EDIT IS VERIFIED BY RE-READING THE FILE. ### ONE FILE OF A KIND THE FACE DID NOT NAME WAS WRITTEN AND IS PRINTED; 0 SPECIES MINTED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED",
     'data/b403_the_three_routed_items.txt; data/b403_components_run3.txt; data/b403_span_before.txt; data/b403_span_after.txt; data/b403_readme_original.txt; data/b403_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b403 -- 8 gates read, 4 checked by digest); tools/b403_extract.py; tools/b403_components.py; tools/b403_desk_bank.py; tools/b403_checks.py; tools/b363_span.py (repaired); SIDE-window README.md (repaired); PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 252'),
    # ### THE ARTEFACT ARC FOLDED (b402).
    ('the-artefact-arc-folded', 'b402 (the artefact arc folded: seventeen acts, nine of them finding an artefact where a limit had been reported, and four finding the limit real)',
     "b402 FOLDED THE SPAN b385-b401 INTO FINDINGS.md AS **THE ARTEFACT ARC**, PURELY ADDITIVE. THE COUNT IS THE TOOL'S AND NOT THE SEAT'S: the last fold covered b371-b383 and was filed by b384, so the span starts at b385; this act is b402 and IS NOT IN ITS OWN FOLD; the fold covers **17 ACTS** against a threshold of **NINE**, ruled by the author at b366 as (R1). **THE NAVIGATOR'S COUNT WAS SIXTEEN AND IS REFUTED BY ONE SUBTRACTION**, printed beside the tool's rather than quietly replaced. **AND THE COUNTER'S OWN THRESHOLD LINE IS STALE**: b363_span.py prints THERE IS NO DECLARED THRESHOLD IN THE RECORD and carries threshold_declared: false -- true when b363 wrote it, false since b366. A DATED ARM, ROUTED and not repaired; the fold reads the threshold from the ruling and says where it got it. **17 OF 17 HEADLINES LOCATED BY THE ANCHOR TOOL IN THEIR OWN ACTS' BANKS, 0 MISSING**, F-NOGRADE refusing the section entirely had one failed, and no act quoted from a later act's summary of it. **THE ARC'S ONE STATEMENT: in nine of the seventeen acts the finding was that a limit, a count, an absence or a version already on the record was an ARTEFACT OF HOW IT HAD BEEN MEASURED -- and in the four mathematical acts that close the span the limit was REAL, and the work became stating it exactly.** The two halves are the same lesson at two scales: a limit reported by an instrument is a property of the instrument until a second shape has been tried, and the mathematical half tried a second shape and the limit held. The section carries the statement WITH ITS SCOPE BESIDE IT, the act-by-act table, the corrections table, the defective-bars table, and the seats' own declared defects **REACHING b400 AND b401** -- a defect table that stops short of the present is a table that flatters it.",
     '### A FOLD PROVES NOTHING, DISCHARGES NOTHING, OPENS NOTHING AND MOVES NO GRADE. ### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED. ### FINDINGS.md IS APPENDED TO AND NEVER EDITED: the pre-act FILE and the pre-act COMMITTED BLOB are both true prefixes of the result, 0 lines edited and 0 content lost. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED. ### THE SPAN CAME FROM A COUNTER THAT READS AND DOES NOT WRITE, AND THE GENERATOR WOULD HAVE REFUSED HAD ITS OWN ACT LIST DISAGREED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND (Q400) IS NOT OPENED. ### M-2 UNCHANGED',
     'data/b402_the_fold.txt; data/b402_fold_notes.txt; data/b402_span_notes.txt; data/b402_registration_2026-09-10.txt (LOCKED before the fold was written, chained on tools/b378_lockgate.py run as b402 -- 8 gates read, 4 checked by digest); tools/b402_fold.py; tools/b402_regspec.py; tools/b402_reg_gate.py; tools/b402_desk_bank.py; tools/b402_checks.py; PLACE-papers FINDINGS.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 251'),
    # ### THE ABSENT ELEMENT SEARCHED (b401).
    ('the-absent-element-searched', 'b401 (the absent element is absent by search; the kind of element is not; and the uniformity that would have cracked it is vacuous)',
     "b401 SEARCHED FOR (Q400)'S ONE ABSENT ELEMENT RATHER THAN ASSUMING IT ABSENT, AND THE VERDICT IS **PRESENT BUT NOT APPLICABLE**. Five matcher shapes over 4536 corpus files and both pinned sources at content, every yield printed and every residue hand-read. **WHAT IS ABSENT**: any statement evaluating or bounding SUM_p W_p(f) at a^2 >= 2 against an archimedean quantity. **WHAT IS PRESENT**: Lagarias Theorem 6.1 -- *for any irreducible cuspidal unitary automorphic representation on GL(N) there holds* S_f(n,pi) = lambda_n(n,pi) + O(n log n) -- **UNCONDITIONALLY**, and **b358 ALREADY OWNED IT**. **THE ELEMENT IS ABSENT; THE KIND OF ELEMENT IS NOT.** It is not the missing element for three named reasons: WRONG FAMILY (the Li family has no compact support and is not indexed by a support at all); WRONG COMPARISON QUANTITY (it bounds against the incomplete Li coefficient, a sum over ZEROS, not an archimedean quantity); and ITS HYPOTHESIS QUANTIFIES OVER THE REPRESENTATION, holding for the corpus's object only under the source's own convention -- H-CUSP, graded by b358, INHERITED by b361, NOT DECIDED HERE. CC's near-misses are all at the NARROW support and its machinery runs TOWARD NARROW, NOT WIDE; the widening it names it does not take. **ADDITION ONE: UNIFORM -- AND VACUOUSLY.** The correction term O(n log n) CARRIES NO PRIME INDEX AT ALL, so it is uniform in the prime because there is no prime in it to be uniform in -- **A UNIFORMITY THAT HOLDS BECAUSE THE INDEX IS ABSENT IS NOT A UNIFORM BOUND IN THAT INDEX; IT IS A BOUND ABOUT A DIFFERENT OBJECT.** The UNIFORM branch is entered and ITS CONSEQUENCE IS NOT DRAWN: no prime-by-prime opening is priced. The implied constant DEPENDS ON pi, against Theorem 5.1's ABSOLUTE one. **ADDITION TWO: A DIFFERENT OBJECT.** SIDE-window bounds a COUNT of prime powers below an integer bound, at NO SUPPORT AT ALL, and its README says W HAS NOTHING TO DO WITH THE CORPUS'S W_2 / W_inf. Reading it whole found its terminal count STALE AGAINST ITS OWN HEAD -- 43 claimed against 69 `#print axioms` invocations -- ROUTED not repaired. **COMPONENT 2: THE FOURTH SITE ENTERED, WITH ITS SHARED INDEX NAMED** -- (iii) and (iv) share the support width and differ in object, and no bridge is typed between any two of the four.",
     "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED. ### THE SIDE-window AXIOM PROFILE IS READ FROM A PRINTED PROFILE AND NOT FROM A RUN, AND THE ACT DECLARES THAT AS WEAKER. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO EQUIVALENCE COMPILED. ### THE CORPUS WRITES ARE TWO CELLS OF ROW U1, APPENDED TO AND CHECKED CELL BY CELL WITH THE OTHER FIVE BYTE-IDENTICAL, AND ONE APPEND-ONLY TRAIL BLOCK -- 0 CONTENT LOST. ### AN INHERITED HYPOTHESIS IS LEFT INHERITED. ### A STALE COUNT FOUND ON ANOTHER REPOSITORY'S README IS PRINTED AND ROUTED, NOT REPAIRED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED, (Q400) IS NOT OPENED, AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b401_the_absent_element_searched.txt; data/b401_components_run.txt; data/b401_extract_notes.txt; data/b401_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b401 -- 8 gates read, 4 checked by digest); tools/b401_extract.py; tools/b401_regspec.py; tools/b401_reg_gate.py; tools/b401_components.py; tools/b401_desk_bank.py; tools/b401_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 250'),
    # ### THE BRIDGE RESTATED (b400).
    ('the-bridge-restated', 'b400 (the bridge restated: on the lawful families the relation can carry nothing, and what survives is one question at the window)',
     "b400 RESTATED THE OWED BRIDGE AND REACHED THE FOURTH VERDICT ITS ORDER ADMITTED: **TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW**. THE CONSTRAINT SET IS 8 CONSTRAINTS, EACH AT A FILE AND A LINE, 0 FROM THE NAVIGATOR, 2 HELD AT DERIVES. **THE OBSTRUCTION, DERIVED:** on the source's lawful class SUM_p W_p(f) = 0 IDENTICALLY -- zero by the definition of the class, because (149) samples f at p^{+-m} and supp(f) is inside (1/2, 2), the source having chosen its window *so that rational primes are not involved* -- so the Sonin margin is a function of the archimedean place ALONE there. On the Li family lambda_A(n) = S_inf(n) + 1 is already owned in closed form, so the only part of lambda_n a bridge could supply is lambda_Z(n) = -S_f(n), which is NOT the zero function. **A RELATION CARRYING AN OBJECT WHOSE FINITE CHANNEL IS IDENTICALLY ZERO TO ONE WHOSE FINITE CHANNEL IS NOT WOULD HAVE TO SUPPLY THAT CHANNEL FROM OUTSIDE ITSELF: IT IS NOT A TRANSPORT OF A QUANTITY BUT A NEW STATEMENT ABOUT THE PRIMES.** The one candidate the record held was (M), refuted at b399. **AND WHAT THIS DOES NOT SHOW IS STATED IN THE SAME BREATH: IT DOES NOT SHOW THAT NO FORMULA CAN BE WRITTEN**, only that on the lawful families one would carry nothing, and that a correspondence chosen to make an identity come out is COMPILED, NOT DERIVED. **THE BRIDGE IS RESTATED AS (Q400), TYPED AND PRICED AND NOT OPENED:** at a support with a^2 >= 2, where SUM_p W_p(f) is not identically zero, is there a relation between that prime constituent and lambda_Z(n)? THE ONE ABSENT ELEMENT, AND THE ONLY ONE, IS ANY STATEMENT EVALUATING OR BOUNDING SUM_p W_p(f) AT a^2 >= 2 AGAINST AN ARCHIMEDEAN QUANTITY. **THE ORDER'S OWN PHRASE WAS CORRECTED AT SOURCE: THEOREM 1 CARRIES A SUPPORT HYPOTHESIS AND PROPOSITION C.1 CARRIES NONE**, so at the window the bound is gone and the criterion is still in force. **AND THE WINDOW'S CAUTION IS CARRIED WITH THE DISTINCTION THAT KEEPS IT FROM BEING A CLOSURE:** what b321 found forced by the shape of the computation was the TOTAL SUM_v W_v, not the CONSTITUENT SUM_p W_p, which that act printed as a live sign-changing column. **COMPONENT 3: 0 OF 3 LAWFUL SEEDS ADMIT A PRIME POWER, AND THE CENSUS COULD NOT HAVE COME OUT ANY OTHER WAY** -- the least prime power is 2 and the support condition is exactly supp(f) inside (1/2, 2). NO ROW IS PAID, NO GRADE MOVED, NO EQUIVALENCE COMPILED.",
     "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED -- the only arithmetic is prime powers in an interval on the record's own grid, printed against the banked list cell by cell. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO EQUIVALENCE COMPILED. ### THE CORPUS WRITES ARE THREE OWED PAIR ROWS APPENDED TO AND ONE APPEND-ONLY TRAIL BLOCK -- ALL ADDITIVE, 0 CONTENT LOST. ### THE IMPOSSIBILITY IS STATED AT ITS DERIVED SCOPE WITH THE SENTENCE NAMING WHAT IT DOES NOT SHOW BESIDE IT. ### TWO DEFECTS ARE PRINTED RATHER THAN REPAIRED: b321's prime-power rule against its own printed list, and this seat's own step-zero overwrite of b373's banked run record, restored byte-identical to its committed blob. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b400_the_bridge_restated.txt; data/b400_components_run.txt; data/b400_extract_notes3.txt; data/b400_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b400 -- 8 gates read, 4 checked by digest); tools/b400_extract.py; tools/b400_regspec.py; tools/b400_reg_gate.py; tools/b400_components.py; tools/b400_desk_bank.py; tools/b400_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 249'),
    # ### THE SIGN AND THE REFUTATION (b399).
    ('the-sign-and-the-refutation', 'b399 ((M) is refuted: it survives the sign test vacuously and then fails by a printed value at every banked lawful seed)',
     "b399 TESTED (M) BY SIGN AND THEN ATTEMPTED IT, AND **(M) IS REFUTED**. THE SIGN TEST RAN FIRST AND COULD HAVE STOPPED THE ACT: (M) -- *for every g in the source's class, -Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)* -- forces the finite-place sum NONPOSITIVE on the class, because the compressed square is nonnegative AS ARITHMETIC (b318: square_trace PERFORMS NO SUBTRACTION ANYWHERE). THE RECORD'S THREE LAWFUL SEEDS ARE a = 1.30, 1.35, 1.41 -- the only cells inside Theorem 1's support window (b318, 3 of 13) -- AND THE PRIME SUM READS 0.000000000 AT ALL THREE, IN BOTH OF THE RECORD'S PRIME COLUMNS; LAWFUL SEEDS GIVING THE FORBIDDEN SIGN: 0. Every cell where the prime sum changes sign (positive at 1.5 and 1.7, negative 1.9 to 2.4, positive again at 2.8 and 3.0) FAILS that support condition. **SO (M) SURVIVES THE SIGN TEST -- AND VACUOUSLY**, because the zero is an EMPTY SUM and b321 had already written THAT THE COVERED CELLS ARE SILENT IS A FACT ABOUT A SUPPORT AND NOT A FINDING. **THEN THE ATTEMPT**: b318 identifies the compressed square with the smear at the autocorrelation, Theorem 4.7 / (83) is an EQUALITY (b321), so -Tr = -W_8(f) + margin, AND AT a = 1.30 THE LEFT SIDE IS -8.622324442 WHILE THE RIGHT SIDE IS 0.000000000 EXACTLY. **NO NORMALIZATION CLOSES IT** (a positive rescaling cannot map a strictly negative number to zero), **NO SIGN CONVENTION CLOSES IT** (the other reads +8.62 = 0), **AND NO TRUNCATION CLOSES IT** (a Frobenius norm only grows with the frame). GRADED MEASURED-AT-COVERED-CELLS, ITS WEAKEST LINK. WHAT THE REFUTATION BUYS: the margin's identity WAS ALREADY OWNED and it is NOT the prime sum -- Theorem 4.7 makes it minus the remainder integral (0.158889558 / 0.186481766 / 0.221284108) -- and **THE TWO BOUNDS ARE TWO BOUNDS**, Theorem 1's Tr <= W_8 and Proposition C.1's SUM_p W_p <= W_8, ordered on the banked class with the TRACE BOUND BINDING and the PRIME BOUND SLACK BY THE WHOLE OF W_8, on three seeds and not as a theorem. THE SECOND OBSTRUCTION IS UNTOUCHED: the Sonin margin IS NOT DEFINED ON THE LI FAMILY (b327). BOTH PINNED SOURCES WERE VERIFIED BY DIGEST BEFORE A WORD WAS READ. THE OWED ROW IS NOT PAID AND NOT OWED IN THE SAME WAY: THE STATEMENT IT WAS WAITING FOR IS FALSE, and what it needs instead is a different statement THIS ACT DOES NOT NAME.",
     "### NO INSTRUMENT WAS RUN, NO KERNEL BUILT AND NO OBJECT RECOMPUTED -- the only arithmetic is on figures read from the acts that emitted them. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO FACE ROW OF THE LEDGER EDITED. ### THE CORPUS WRITES ARE ONE POINTER IN FINDINGS.md (no cell, no grade, no rank and no verdict sentence edited), THE OWED PAIR ROW'S LAST CELL, THE BRIDGE TRAIL ROW WITH ONE NEW ROW BESIDE IT, AND THREE CONTACTS IN THE EMERGING-PROGRAMMES LEDGER -- ALL ADDITIVE, 0 CONTENT LOST. ### THE GRADE MOVE ADDITION THREE INVITED IS ROUTED, NOT MADE. ### AND THIS ACT'S OWN LOCKED FACE UNDERCOUNTED ITS TOOL FILES BY ONE: BOTH NUMBERS ARE PRINTED AND THE FACE IS NOT EDITED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b399_the_sign_and_the_refutation.txt; data/b399_components_run.txt; data/b399_extract_notes.txt; data/b399_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b399 -- 8 gates read, 4 checked by digest); tools/b399_extract.py; tools/b399_regspec.py; tools/b399_reg_gate.py; tools/b399_components.py; tools/b399_desk_bank.py; tools/b399_checks.py; PLACE-papers FINDINGS.md, FACES_LEDGER.md, OPEN_TRAILS.md and EMERGING_RESEARCH_PROGRAMMES.md; CORRESPONDENCE.md row 248'),
    # ### THE LI-WEIL BRIDGE (b398).
    ('the-li-weil-bridge', 'b398 (the li-weil bridge is undecidable from the record: both halves of the reading are banked, the one missing identity is named and typed a result, and a second obstruction survives it)',
     "b398 TESTED THE DECOMPOSITION READING OF THE LI-WEIL BRIDGE FROM BANKED RESULTS ONLY AND THE VERDICT IS **UNDECIDABLE FROM THE RECORD**. THE PLACE-SETS DIFFER AND THAT IS THE FIRST THING MEASURED: the Sonin margin's is {infinity} AND NOT BY OMISSION -- b197 read Theorem 2 of 2310.18423, THE SEMILOCAL SONIN SPACE IS ONE ARCHIMEDEAN COPY AND FINITE PLACES CONTRIBUTE NO INDEPENDENT SONIN DIRECTIONS -- while the Li margin's is {infinity} UNION {ALL FINITE PLACES} plus a pole term at s = 0 that is not a place at all. **BOTH HALVES OF THE NAVIGATOR'S READING ARE BANKED**: half one is the clause statement's own K3 -- the source's construction on the object returns the test function at the identity times a dimension and no arithmetic (b310) -- at KERNEL TERMINALS B329.* (24, zero-axiom) and B310.*; half two is K4 VERBATIM -- the corpus's prime side IS the source's finite-places sum, FACTOR FOR FACTOR -- DIFFERENT ONLY IN THE CUTOFF WINDOW (b306), an exception CARRIED AND NOT DROPPED, corroborated by b327's derived lambda_Z(n) = -S_f(n). SO THE LEDGER'S OWED ROW IS NARROWER THAN IT LOOKED. **AND THIS ACT'S OWN FIRST TEST GOT IT BACKWARDS**: it read b197's withdrawal of Tr_infinity + SUM_p Tr_p as covering the premise and called the reading REFUTED, and b197 forbids that reading in a sentence written for exactly this case -- THE SEAT READ IT AS IF IT DID AND THE FILE CAUGHT IT. THE CONCLUSION NEEDS EXACTLY ONE IDENTITY: **(M) for every g in the source's class, -Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#) in the source's normalization**, TYPED A RESULT -- not a read (no file states it), not a ruling (it is an identity), not a construction (both sides exist at grades). A SECOND OBSTRUCTION IS INDEPENDENT AND SURVIVES IT: THE SONIN MARGIN IS NOT DEFINED ON THE LI FAMILY (b327: G_n's inverse Mellin transform has no compact support, outside Theorem 1's class), so even with (M) the two sides are ONE FUNCTIONAL ON TWO DISJOINT FAMILIES, AND NO NORMALIZATION FIXES A DOMAIN. THE OWED ROW IS SHARPENED AND STILL OWED, WITH 0 GRADES CONFERRED AND 0 ROWS PAID. **(N) IS NAMED AND NOT ATTEMPTED** -- the compact part of K3 holds FOR EVERY CELL AND NOT AT SEVEN -- with 6 dependencies HELD and 3 ABSENT, and **(N) IS NOT (M)**: (M) moves the bridge, (N) moves the clause. RULING (R23) IS RECORDED and all 3 work-order rows now name a trigger that can fire.",
     "### NOTHING WAS COMPUTED, NO INSTRUMENT WAS RUN AND NO KERNEL WAS BUILT -- the order's own condition, since an act that computes something new has CHANGED THE QUESTION. ### NO GRADE MOVED OR CONFERRED, NO FACE PROMOTED, NO ROW PAID, NO RULE STRUCK OR AMENDED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE EDITED, NO FACE ROW OF THE LEDGER EDITED. ### THE ONLY CORPUS WRITES ARE THE OWED PAIR ROW'S LAST CELL AND THREE TRIGGER CELLS, BOTH ADDITIVE, WITH THE PRE-EDIT LINES PRESERVED VERBATIM AND 0 CONTENT LOST. ### NEITHER PINNED SOURCE IS ON THIS DRIVE AND EVERY SOURCE STATEMENT IS QUOTED AS THE CORPUS QUOTES IT. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE CLAUSE HAS NOT MOVED AND NO COORDINATE IS CLOSED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b398_the_li_weil_bridge.txt; data/b398_components_run.txt; data/b398_extract_notes4.txt; data/b398_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b398 -- 8 gates read, 4 checked by digest); tools/b398_extract.py; tools/b398_regspec.py; tools/b398_reg_gate.py; tools/b398_components.py; tools/b398_desk_bank.py; tools/b398_checks.py; PLACE-papers FACES_LEDGER.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 247'),
    # ### THE UNLANDED WORK (b397).
    ('the-unlanded-work', "b397 (eight of the nine held branches were already landed; the unlanded inventory is four declarations on one branch; and the disclosure rule's own worked instance is stale)",
     "b397 READ THE HELD BRANCHES FOR CONTENT AND FOUND THAT 8 OF THE 9 RESEARCH BRANCHES WERE ALREADY FULLY MERGED INTO main. Only SIDE-kernel/derivative-engine carries commits main does not have. **SO THE HELD / UNMERGED / BRANCH-RESIDENT LANGUAGE IN THOSE KEYSTONES IS A CORRECTION THAT NEVER PROPAGATED: THE WORK LANDED AND THE PROSE DID NOT FOLLOW IT**, b394's species in a new medium, and rewriting the prose is AUTHORING so it is ROUTED. THE COUNTING TRAP IS ON THE RECORD: rev-list --left-right --count main...b puts the MAIN-ONLY count on the left, an earlier form of the survey read it as ahead, and EIGHT MERGED BRANCHES READ AS ONE COMMIT AHEAD -- THE EXACT OPPOSITE OF THE TRUTH -- caught by one branch reading 0 0. The live branch carries 72 declarations of which 4 ARE ABSENT FROM main, tested AGAINST main AND NOT THE MERGE BASE: invariance_barrier and DeterminedBy already stand on main and are citable; 3 are cited by keystones while no default branch carries them; and derivGrade is CITED BY NOTHING. THERE IS NO PRINTED PROFILE ON THE REF -- only a #print axioms SOURCE SCRIPT saying Expected -- so every axiom claim about that branch is NOT BUILT, NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD, and (F1) IS NOT ESTABLISHED, declared on the face before the components ran. THE DISCLOSURE RULE'S OWN WORKED INSTANCE IS STALE: it names word-pairing-interface as the held unmerged branch and that branch is MERGED, so writing the demanded disclosure would PUT A FALSE STATEMENT IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE; NOT STRUCK, NOT AMENDED, ROUTED. 15 ROWS SWEPT, 6 REPAIRED, 8 SWEPT-NOT-REPAIRED, 1 ROUTED, reported apart, 2 documents edited with 0 CONTENT LOST. (F2) IS MET BUT NOT FOR THE REASON GIVEN. RULING (R22) PARKS THE INSTRUMENT-AUDIT LANE and the queue carries 6 ITEMS EACH WITH A TRIGGER, NOTHING OPENED.",
     "### NOTHING WAS MERGED, PUSHED, FETCHED, CREATED OR CHECKED OUT; EVERY REPOSITORY'S BRANCH AND HEAD IS BYTE-IDENTICAL BEFORE AND AFTER; 0 CLONES AND 0 BUILDS. ### NO .lean FILE TOUCHED IN ANY REPOSITORY. ### NO RULE STRUCK OR AMENDED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO KEYSTONE PROSE REWRITTEN. ### THE ONLY CORPUS WRITE IS A STATUS CELL WHERE THE DISCLOSURE IS TRUE, PLUS ONE APPENDED ANNOTATION PER EDITED DOCUMENT PRESERVING THE PRE-EDIT LINES VERBATIM. ### AN UNKNOWN IS REPORTED AS NOT BUILT. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME WITH TRIGGERS. ### M-2 UNCHANGED",
     'data/b397_the_unlanded_work.txt; data/b397_components_run.txt; data/b397_extract_notes.txt; data/b397_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b397 -- 8 gates read, 4 checked by digest); tools/b397_extract.py; tools/b397_regspec.py; tools/b397_reg_gate.py; tools/b397_components.py; tools/b397_desk_bank.py; tools/b397_checks.py; PLACE-papers keystone status cells and OPEN_TRAILS.md; CORRESPONDENCE.md row 246'),
    # ### THE BACKTICK SWEPT (b396).
    ('the-backtick-swept', 'b396 (the backtick swept: 82 at-risk figures across 64 instruments, six re-run and all six confirmed, and three filters discarded before the lock)',
     "b396 MEASURED WHAT b395 LEFT UNMEASURED. THE ORDER'S FIRST INSTRUCTION WAS DISCHARGED BEFORE ANYTHING WAS SWEPT: the detector was run against a fixture carrying ONE NARROW MATCHER WRITTEN THREE WAYS, INCLUDING ONE WITH NO REGEX AT ALL, and ALL THREE WERE FOUND, with a WIDE fixture coming back CLEAN so the fixture shows DISCRIMINATION and not merely firing. A RAW grep IS NOT THE INSTRUMENT: 826 OF 858 FILES IN tools/ CARRY A BACKTICK AND ALMOST EVERY ONE IS PROSE, so the sweep reads by ast and keeps a literal only where it is USED AS A TEST. THE FUNNEL: 856 PARSED, 407 CARRYING A NARROW TEST, 64 CARRYING AN AT-RISK FIGURE, AND 82 AT-RISK FIGURES ACROSS 51 ACTS. THREE FILTERS WERE TRIED AND DISCARDED BEFORE THE LOCK WITH THEIR YIELDS PRINTED -- 374 OF 407, 350 OF 380, 79 OF 82 -- AND THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT: THE NARROW SHAPE IS PERVASIVE AND THE QUESTION HAS NO ANSWER AT INSTRUMENT GRANULARITY, ONLY AT FIGURE GRANULARITY. THE CHEAPEST THREE AND THE MOST EXPOSED THREE SHARE 0 MEMBERS AND ALL SIX WERE RUN. THE UNIT IS THE FIGURE AND NOT THE MATCH COUNT: AN EARLIER FORM READ THE WRONG INPUT AND COMPARED COUNTS WHERE THE FIGURE IS A BOOLEAN, CALLING TWO MOVED, AND BOTH WERE ARTEFACTS OF THE HARNESS. 6 CONFIRMED, 0 MOVED, 1 NARROWNESS WITHOUT CONSEQUENCE, SO (L2) IS REFUTED AS THIS SEAT REGISTERED BEFORE THE LOCK, AND (L3) IS MET BY b395 RATHER THAN BY THIS ACT. A CONFIRMATION IS THE WEAKER RESULT AND 76 FIGURES ARE UNTESTED. THE TEN NOW-REACHABLE KEYSTONES ARE PRICED AND NOT READ AT 28.0 MINUTES, TAKING THE CENSUS FROM 4 OF 16 TO 14 OF 16, AND THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR. THE PRESERVATION HAZARD IS FILED WITH b395'S NEAR MISS AS ITS INCIDENT AND MECHANIZED IN PART: AN OPT-IN DEFAULT-OFF EDITING MODE THAT EXCLUDES BLOCKQUOTED LINES AND REFUSES AN ANCHOR RESOLVING ONLY INSIDE ONE, 12 FIXTURE ARMS 0 FAILING, 144 CALLERS 0 MOVED, WITH THE JUDGEMENT HALF LISTED APART AND NOT CLAIMED AS MECHANIZED.",
     "### NO INSTRUMENT OF ANY PRIOR ACT WAS REPAIRED OR EDITED AND NO CORPUS DOCUMENT WAS EDITED AT ALL. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED, NO PRIOR FACE OR BANK EDITED. ### THE ONLY relay EDIT OUTSIDE THIS ACT'S OWN FILES IS ONE INDEX KEY AND ONE ADDED OPT-IN MODE IN anchor_from_file.py, WITH 0 CALLERS MOVED. ### THE SWEEP'S OWN PREMISE WAS TESTED FIRST. ### EVERY DISCARDED FILTER CARRIES ITS YIELD. ### EVERY WIDENING WAS STATED BEFORE IT RAN. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b396_the_backtick_swept.txt; data/b396_components_run2.txt; data/b396_extract_notes4.txt; data/b396_registration_2026-09-10.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b396 -- 8 gates read, 4 checked by digest); tools/b396_narrow.py; tools/b396_figures.py; tools/b396_extract.py; tools/b396_regspec.py; tools/b396_reg_gate.py; tools/b396_components.py; tools/b396_desk_bank.py; tools/b396_checks.py; tools/anchor_from_file.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 245'),
    # ### THE CEILING ANSWERED (b395).
    ('the-ceiling-answered', 'b395 (the ceiling was an artefact of a matcher: ten of the eleven keystones b394 called unreachable are readable without a clone)',
     "b395 TESTED b394's CEILING AND IT WAS AN ARTEFACT OF b394's OWN MATCHER. b394 REPORTED ELEVEN KEYSTONES UNREACHABLE, 9 BECAUSE NO KERNEL REPOSITORY THEY NAME IS ON THE DRIVE; ITS MATCHER RECOGNISED A BACKTICKED LOWERCASE NAME AND NOTHING ELSE. WIDENED, THE YIELD CHANGES FOR 9 OF THE ELEVEN AND THE DRIVE HOLDS A NAMED REPOSITORY FOR 8 OF THE 8 IT SAID IT HELD NONE FOR, EVERY ONE RESOLVING A HEAD LOCALLY WITH ITS HELD BRANCHES IN THE LOCAL REFS. b394's FACE AND BANK ARE LOCKED AND UNEDITED AND BOTH FIGURES ARE PRINTED -- A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE. THE PARTITION IS 10 ON THE DRIVE AND 1 NAMES NO TERMINAL, SUMMING TO 11, SO (L1) ASKED FOR FOUR AND THE MEASUREMENT IS 10. FOUR ROUTES ARE PRICED IN WHAT THEY BUY: CLONE REACHES 0 FURTHER, A BRANCH-READING RULING REACHES 0 AS A READING ROUTE, ACCEPTING THE CEILING IS REFUTED, AND A FOURTH THE ORDER DID NOT POSE -- REPAIR THE PREDICATE -- REACHES 10 AT THE COST OF ONE MATCHER. (L2) HOLDS BECAUSE ENUMERA NAMES NO TERMINAL FOR ANY ROUTE TO REACH. THE FEDERATION WAS READ LIVE WITH BOTH CONTROLS FIRST: THE CORPUS NAMES 77, THE DRIVE HOLDS 43 AND THE ACCOUNT RESOLVES THE SAME 43, WITH EVERY NEGATIVE RE-READ AND REPORTED ABSENT-OR-PRIVATE NEVER ABSENT. (R21) IS EXECUTED IN THE MAP ROW ITSELF AND ADDITIVELY, THE PRIOR ANCHOR RETAINED AND NOT DEMOTED, WITH THE PRE-EDIT ROW PRESERVED VERBATIM. THE NOTE FOR 21432399 IS DRAFTED AND WRITTEN NOWHERE; 19675356's DEPOSITED VERSION IS RECORDED NOWHERE IN THE CORPUS AND THE SMALLEST RECOVERING READ IS NAMED. NEITHER ANCHORLESS CLUSTER IS DECIDED.",
     "### NO GRADE WAS MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO LIST CLOSED, NO SYNTHESIS WRITTEN, NO ANCHOR INVENTED. ### THE ONLY CORPUS EDIT IS ONE ANCHOR CELL AND ONE APPENDED BLOCK IN SPIRAL_MAP.md. ### EVERY MATCHER'S YIELD IS PRINTED INCLUDING b394'S. ### THE PARTITION'S PARTS SUM TO THE POPULATION. ### READABLE WITHOUT A CLONE IS DEMONSTRATED, NOT ASSERTED. ### BOTH LIVE-READ CONTROLS RAN. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### NO BUILD RUN AND NO REPOSITORY CLONED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b395_the_ceiling_answered.txt; data/b395_components_run2.txt; data/b395_extract_notes7.txt; data/b395_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b395 -- 8 gates read, 4 checked by digest); tools/b395_extract.py; tools/b395_regspec.py; tools/b395_reg_gate.py; tools/b395_components.py; tools/b395_desk_bank.py; tools/b395_checks.py; PLACE-papers SPIRAL_MAP.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 244'),
    # ### THE RECONCILIATION BATCHED (b394).
    ('the-reconciliation-batched', "b394 (three keystones reconciled in one act by b390's rule quoted and not improved; the batch finding a stale citation between two of its own subjects, the corrected-but-unpropagated species recurring; two citations moved forward with the originals preserved; and the method's own ceiling named -- eleven of the remaining twelve are unreachable)",
     "b394 READ THREE KEYSTONES IN ONE ACT, CHOSEN BY b390's RULE QUOTED WITH NOTHING ADDED TO IT -- TAKE THOSE WHOSE TERMINALS THE DRIVE CAN REACH. Of the census's 15 on disk, 4 ARE REACHABLE; 11 ARE EXCLUDED AND EVERY EXCLUSION IS NAMED; ADDITIVE_MULTIPLICATIVE_CONSPIRACY IS SET ASIDE because b390 READ IT WHOLE. THE THREE: GRH_CASCADE, FOUNDATIONS_OF_THE_SIDE_PROGRAMME, SILENCE_STAGES_DEALIGNMENT -- and THE LAST CARRIES NO CORRESPONDENCE TABLE, reported and NOT repaired since WRITING A CORRESPONDENCE TABLE IS AUTHORING, NOT RECONCILING. THE THREE BUCKETS ARE 1 / 1 / 3 AND (L2) IS MET INSIDE THE BATCH: GRH_CASCADE CITES FOUNDATIONS_OF_THE_SIDE_PROGRAMME -- ANOTHER OF THE THREE -- AT v0.1 IN TWO PLACES WHILE THE REGISTRY HAD RECONCILED THAT ROW PAST IT. THAT IS THE CORRECTED-BUT-UNPROPAGATED SPECIES b391 FOUND, RECURRING, AND THE BATCH FOUND ITS OWN DEFECT. THE OLD FORM WAS CONFIRMED IN THE CITED DOCUMENT'S OWN LINEAGE FIRST, because A SUPERSESSION IS NOT A PHANTOM AND IS NOT REPAIRED AS ONE; both citations were moved to the registry's row value with THE ORIGINALS PRESERVED IN AN APPENDED ANNOTATION and 0 LINES REMOVED. 4 REPAIRS ARE ROUTED. THE THREE SPECIES ARE REPORTED APART: 0 PHANTOMS, 2 UNPROPAGATED, 6 SUPERSEDED. 4 OF 16 KEYSTONES ARE NOW RECONCILED, AND 11 OF THE REMAINING 12 CANNOT BE READ BY THIS RULE AT ALL -- THE POPULATION THIS METHOD CAN REACH IS ALREADY NEARLY EXHAUSTED.",
     "### NO GRADE WAS MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, NO LIST CLOSED. ### THE ONLY CORPUS EDIT IS TWO VERSION STRINGS AND ONE APPENDED ANNOTATION IN ONE DOCUMENT. ### THE RULE WAS QUOTED AND NOT IMPROVED. ### EVERY EXCLUSION IS NAMED AND EVERY BUCKET REPORTED. ### BOTH PRICES ARE DECLARED FLOORS AND THE SAMPLE'S BIAS IS NAMED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### NO BUILD RUN. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### M-2 UNCHANGED",
     'data/b394_the_reconciliation_batched.txt; data/b394_components_run2.txt; data/b394_extract_notes2.txt; data/b394_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b394 -- 8 gates read, 4 checked by digest); tools/b394_extract.py; tools/b394_regspec.py; tools/b394_reg_gate.py; tools/b394_components.py; tools/b394_desk_bank.py; tools/b394_checks.py; PLACE-papers phase1.5/spectral/GRH_CASCADE.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 243'),
    # ### THE FIVE CLUSTERS SURFACED (b393).
    ('the-five-clusters-surfaced', 'b393 (the five clusters surfaced to the navigator with what changed in each and a quotation apiece; the anchor question measured for the first time and returning four different answers of which three are ways of not answering it; and the two deposited records and Tier KC priced, with nothing acted on)',
     "b388 FOUND FIVE CLUSTERS CHANGED IN SHAPE AND b391 REPORTED THEM AND BOTH MEASURED MEMBERSHIP ONLY. b393 SURFACED THEM TO THE NAVIGATOR AND MEASURED THE ANCHOR QUESTION FOR THE FIRST TIME, by the census's own two figures DATE AND PIN COUNT, with the test's limit stated: IT CAN ONLY RANK DOCUMENTS THE CENSUS LISTS. THE FIVE RETURN FOUR DIFFERENT ANSWERS AND THE FOUR ARE NOT ADDED: 1 ANCHOR OVERTAKEN (Simplicity / RH cascade, overtaken by PATHS_TO_THE_CRITICAL_LINE), 1 MEMBERSHIP ONLY, 1 ANCHOR NOT A CENSUS KEYSTONE, 2 NO ANCHOR NAMED AT ALL. THREE OF THE FOUR ARE WAYS OF NOT ANSWERING THE QUESTION AND ONLY ONE IS AN ANSWER TO IT, SO (L1) EXPECTED TWO AND IS REPORTED REFUTED. THE TWO DEPOSITED RECORDS FAILING (R20)'s CURRENCY OBLIGATION PRICE ASYMMETRICALLY: 21432399 deposited the monograph at manuscript v5.8 against a repository at v5.13 and CAN BE NOTED IN ONE LINE TODAY; 19675356's DEPOSITED VERSION IS NOT RECORDED ANYWHERE IN THE CORPUS so IT CANNOT BE GIVEN A CURRENT-VERSION REMEDY AT ALL. NEITHER REMEDY BUYS AN ANSWER TO WHETHER A DOI IS SAFE TO CITE WITHOUT A LIVE READ. TIER KC IS PRICED AND STILL EMPTY: ITS OBLIGATION HAS THREE LIMBS AND THE RECORD ANSWERS ONE -- b387's 162 ROWS ANSWER GRADE; PLACEMENT AND COVERAGE ARE UNHELD; THE ONE KEYSTONE b390 READ WHOLE WOULD FAIL THE PLACEMENT LIMB; AND THE APPLICATION NEEDS A DECLARATION, WHICH IS A GATE AND NOT A COST.",
     '### NO CLUSTER WAS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. ### NO DOCUMENT WAS PLACED IN TIER KC AND NO CANDIDATE WAS NAMED. ### NO CLASS RULED, NO DOCUMENT RECLASSIFIED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, NO CORRESPONDENCE ROW EDITED, NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS EDITED AT ALL -- THE ONLY WRITES ARE THE TWO LEDGERS. ### NEITHER REMEDY WAS RECOMMENDED. ### THE CHEAP SWEEP IS A FLOOR AND NOT A VERDICT: A HEADING IS NOT A TABLE READ. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO KEYSTONE WAS RECONCILED. ### M-2 UNCHANGED',
     'data/b393_the_clusters_surfaced.txt; data/b393_components_run.txt; data/b393_extract_notes3.txt; data/b393_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b393 -- 8 gates read, 4 checked by digest); tools/b393_extract.py; tools/b393_regspec.py; tools/b393_reg_gate.py; tools/b393_components.py; tools/b393_desk_bank.py; tools/b393_checks.py; PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row 242'),
    # ### THE TWO RULINGS (b392).
    ('the-two-rulings-r19-and-r20', "b392 (the two rulings written: (R19) names Tier KC, the finished keystone, with an obligation, a citation rule for a stranger, and a guard quoted beside the two failures it exists to prevent; (R20) writes the deposit rule and its currency obligation where the corpus puts deposits, and the census from the corpus's own record finds two records failing both limbs, refuting (L2))",
     "RULING (R19), THE AUTHOR'S: THE FINISHED KEYSTONE IS A NAMED CLASS. Tier KC -- a document that SYNTHESIZES A SUBJECT CLUSTER AND CARRIES THE VERIFICATION APPARATUS -- was added to the standing document-class taxonomy ADDITIVELY, every prior line preserved byte-for-byte. ITS OBLIGATION: every load-bearing claim stated clearly in the body and carried by a row in a CORRESPONDENCE TABLE PLACED AFTER THE FRONT MATTER WHERE A READER MEETS IT, each row naming its backing IN THE FRONT DOOR'S OWN VOCABULARY, plus glossary, bibliography and other tables as needed. ITS CITATION RULE: A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE -- CITE THE SYNTHESIS FOR ORIENTATION, CITE EACH CONCORDANCE ROW AT ITS STATED GRADE. ITS GUARD: THIS CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER, quoted beside the June 2026 formation-universality over-claim and the August 2026 retirement of the scheme that spanned the tiers. NO DOCUMENT IS RECLASSIFIED AND NO CANDIDATE IS NAMED. RULING (R20), THE AUTHOR'S: THE DEPOSIT RULE, WRITTEN INTO REGISTRY.md WITH README.md POINTING AT IT. A MANUSCRIPT WAVE DEPOSITS WITH ITS COMPANION PAPERS; A KERNEL DEPOSITS WHEN A PUBLISHED CLAIM CITES ITS TERMINALS; A PRE-REGISTERED SEARCH DEPOSITS BECAUSE ITS REGISTRATION COMMITTED TO PUBLISHING EVERY OUTCOME. THE CURRENCY OBLIGATION: EVERY DEPOSITED RECORD EITHER SITS AT A VERSION A CITABLE CLAIM USES OR CARRIES A NOTE SAYING IT IS HISTORICAL, WITH NO THIRD STATE. THE RULE IS DESCRIPTIVE BEFORE IT IS PRESCRIPTIVE: the note's three citable records match its three limbs one for one. THE CENSUS WAS TAKEN FROM THE CORPUS'S OWN RECORD AND NOT FROM THE PLATFORM: 16 DOIs known, 6 named by the note, 10 unlisted, 8 passing limb (b) and 2 FAILING BOTH LIMBS, so (L2) EXPECTED THREE AND IS REPORTED REFUTED. ONE RECORD WAS CLEARED ONLY BY AN ELIDED DOI. THE SIDE-kernel FINDING WAS WITHDRAWN AS NOT ESTABLISHED, because PROXIMITY IS NOT ATTACHMENT.",
     '### NO DOCUMENT WAS RECLASSIFIED, NO CLASS LINE WRITTEN ON ANY DOCUMENT AND NO CANDIDATE NAMED. ### NO PRIOR LINE OF THE TAXONOMY, THE REGISTRY OR THE README WAS EDITED AND 0 LINES WERE REMOVED. ### NO REGISTRY ROW, LINEAGE OR DEPOSIT FIGURE EDITED; NO DEPOSIT NOTE ENTRY EDITED OR REMOVED. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE ROW EDITED, NO LIST CLOSED, NO CLUSTER RESHAPED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b392_the_two_rulings.txt; data/b392_components_run4.txt; data/b392_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b392 -- 8 gates read, 4 checked by digest); tools/b392_regspec.py; tools/b392_reg_gate.py; tools/b392_components.py; tools/b392_desk_bank.py; tools/b392_checks.py; PLACE-papers phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md, REGISTRY.md, README.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 241'),
    # ### THE PHANTOM VERSION REPAIRED (b391).
    ('the-phantom-version-repaired', "b391 (the phantom version repaired in 24 of 32 citations with 8 excluded and named, its origin located in the registry's own bundle label and its failure to propagate, the widened check repairing nothing after four tightenings and a hand read, and the five clusters read but not reshaped)",
     "b391 REPAIRED THE PHANTOM VERSION. THE METHODOLOGY PAPER WAS CITED AS A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2 IN 32 INSTANCES ACROSS 13 DOCUMENTS AND THERE IS NO v1.2 -- THE DOCUMENT IS phase1.5/method/A_METHODOLOGY.md AT v0.5.4 AND REGISTRY ROW 1.5h-4 AGREES. THE COUNT WAS RE-MEASURED FROM THE FILES AND IS NOT b390's 28 ACROSS 11, because A COUNT QUOTED FORWARD IS A COUNT NOBODY RE-MEASURED. THE ORIGIN IS IN THE CORPUS'S OWN RECORD: THE REGISTRY ROW CARRIED A BUNDLE LABEL v1.2 AND RECONCILED ITSELF ON 2026-07-16, AND THE CORRECTION NEVER PROPAGATED -- A CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND A DEFECT EVERYWHERE ELSE. 24 CITATIONS WERE REPAIRED AND 8 EXCLUDED EACH WITH ITS REASON: 4 PROVENANCE ENTRIES, 1 PRESERVED BLOCK LINE AND 3 LEDGER LINES REPORTING THE DEFECT, since REPAIRING A REPORT OF AN ERROR ERASES THE REPORT. 0 LINES REMOVED, EVERY LINE COUNT UNCHANGED, AND THE ONLY CHANGE ON EVERY REPAIRED LINE IS THE VERSION. THE WIDENED CHECK REPAIRED 0: ITS SCREEN WAS TIGHTENED FOUR TIMES BEFORE ANY FINDING WAS FILED WITH EVERY YIELD PRINTED, AND ITS FOUR SURVIVING CANDIDATES WERE READ BY HAND -- TWO FALSE POSITIVES AND TWO UNDECIDABLE BECAUSE CONSTANCE.md DECLARES NO MATCHING VERSION IN ITS OWN BYTES. THE 66 SUPERSEDED CITATIONS ARE REPORTED AND LEFT: A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM AND NOT A PHANTOM. THE FIVE CLUSTERS ARE NAMED WITH WHAT CHANGED IN EACH AND 0 WERE RESHAPED.",
     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO REGISTRY ROW EDITED, NO CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS RESHAPED, SPLIT, MERGED, RENAMED OR RE-ANCHORED. ### NO BYTES WERE WRITTEN INTO THE STANDING TAXONOMY AND NO DEPOSIT RULE WAS WRITTEN: A LEG DOES NOT REACH INTO THE NEXT LEG'S SCOPE. ### 0 PROVENANCE ENTRIES EDITED, 0 PRESERVED BLOCKS EDITED, 0 REPORTS OF THE DEFECT EDITED, 0 SUPERSEDED VERSIONS REPAIRED, 0 LINES REMOVED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH. ### M-2 UNCHANGED",
     'data/b391_the_phantom_repaired.txt; data/b391_components_run3.txt; data/b391_extract_notes4.txt; data/b391_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b391 -- 8 gates read, 4 checked by digest); tools/b391_extract.py; tools/b391_regspec.py; tools/b391_reg_gate.py; tools/b391_components.py; tools/b391_desk_bank.py; tools/b391_checks.py; PLACE-papers (24 citation lines across 11 documents) and OPEN_TRAILS.md; CORRESPONDENCE.md row 240'),
    # ### THE FIRST PROOFREADING PASS (b390).
    ('the-first-proofreading-pass', 'b390 (the first proofreading pass: one keystone chosen by a printed rule and read whole; ten of twelve anchors already in it and the middle bucket empty; one citation the record contradicts, found only by reading, corpus-wide and therefore routed; and the one map row b389 routed, repaired with the removed name kept in its own note)',
     "THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO READING PASS. b390 READ ONE KEYSTONE WHOLE. THE SUBJECT WAS CHOSEN BY A RULE STATED BEFORE IT WAS NAMED: the census names TWO and the order asks ONE, so TAKE THE ONE WHOSE TERMINALS THE CANONICAL DRIVE CAN REACH -- THE_RESIDUE_OF_RH's terminals are on a HELD UNMERGED BRANCH and NOT ON main, while every pin ADDITIVE_MULTIPLICATIVE_CONSPIRACY cites resolves; THE ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT. OF 12 ANCHORS, 10 ARE ALREADY IN THE DOCUMENT, 2 ARE ADDITIONS AND 0 ARE CORRECTIONS -- THE MIDDLE BUCKET IS EMPTY AND IS REPORTED AS PLAINLY AS A FULL ONE. (F1) IS MET BY A CORRECTION NO ANCHOR NAMED AND ONLY READING FOUND: THE PAPER CITES A_METHODOLOGY_FOR_DETERMINED_SYSTEMS v1.2 AND THERE IS NO v1.2 -- IT IS AT v0.5.4 AND REGISTRY ROW 1.5h-4 AGREES. IT IS CORPUS-WIDE, 28 CITATIONS ACROSS 11 LIVE DOCUMENTS, SO IT IS RECORDED BY AN APPENDED ANNOTATION AND ROUTED AS A CORPUS-WIDE PASS BECAUSE REPAIRING ONE OF ELEVEN HIDES A SYSTEMIC DEFECT INSIDE A LOCAL TIDY-UP, AND A PROVENANCE ENTRY MUST NOT BE EDITED EVEN BY THAT PASS. OF THE 8 ITEMS b388 AND b389 ROUTED, EXACTLY 1 WAS REPAIRABLE AND IS REPAIRED: SPIRAL_MAP.md's CROSS-DOMAIN FEDERATION COLUMN, WITH THE REMOVED NAME KEPT IN THE ROW'S OWN NOTE UNDER (R4) AND THE LIVE CHECK RE-RUN AND NOT RECALLED. 0 GRADES MOVED, 0 CLASSES CHANGED, 0 CLAIMS WITHDRAWN, 0 LINES DELETED, SS I-IV BYTE-IDENTICAL TO THE PRE-ACT BLOB. THE PASS COST 24 MINUTES AND 1 ACT FOR 1 OF 16 KEYSTONES AND THE PRICE FOR THE REST IS STATED AS A PRICE AND NOT A PLAN, FROM ONE SAMPLE, WITH BOTH WAYS IT IS UNREPRESENTATIVE NAMED.",
     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED AND NEITHER MAP'S (R18) HEAD NOTE WAS TOUCHED. ### 0 REPAIRS WERE MANUFACTURED TO SATISFY AN EXPECTATION AND 0 GRADE WORDS WERE MINTED. ### 0 RULINGS WERE TREATED AS REPAIRS: A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO KERNEL BRANCH MERGED OR CREATED. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH. ### M-2 UNCHANGED",
     'data/b390_the_proofreading_pass.txt; data/b390_components_run.txt; data/b390_extract_notes4.txt; data/b390_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b390 -- 8 gates read, 4 checked by digest); tools/b390_extract.py; tools/b390_regspec.py; tools/b390_reg_gate.py; tools/b390_components.py; tools/b390_desk_bank.py; tools/b390_checks.py; PLACE-papers SPIRAL_MAP.md, phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 239'),
    # ### TWO MAPS TWO KEYS, AND THE LAYER UNREAD (b389).
    ('two-maps-two-keys-and-the-layer-unread', "b389 (the look-see: the cluster syntheses in three populations that do not nest; the deposited layer read live, unanswered on every route, and halted rather than substituted; no written deposit rule located by a search proved twice; the unreached repository undecidable but immaterial, with b388's finding about it withdrawn as wrong; and (R18) applied as one head note per map and nothing else)",
     "RULING (R18), THE AUTHOR'S: TWO MAPS, TWO KEYS. A CLUSTER MAP KEYS ON SUBJECTS AND DOMAINS AND DRIFTS WHEN NOBODY RECORDS; A CONSTELLATION MAP KEYS ON INTERRELATED VERIFIED STATEMENTS AND DRIFTS WHEN NOBODY BUILDS. SPIRAL_MAP.md AND THE_LOAD_BEARING_MAP.md EACH RECEIVED ONE HEAD NOTE AND NOTHING ELSE -- 4 PRIOR HEAD DECLARATIONS PRESERVED, 0 REMOVED, 0 LINES DELETED, 0 LINES CHANGED OUTSIDE EITHER HEAD BLOCK MEASURED AGAINST THE PRE-ACT BLOB -- AND NEITHER MAP IS MERGED INTO THE OTHER. THE CLUSTER SYNTHESES STAND IN THREE POPULATIONS THAT DO NOT NEST: 8 ON DISK, 6 IN THE REGISTRY'S SUPPORT TIER, 7 WHOSE SUBJECT THE MAP'S TABLE CARRIES, NEVER ADDED AND NEVER AVERAGED. THE DEPOSITED LAYER COULD NOT BE ENUMERATED: 0 OF 6 ZENODO ROUTES ANSWERED WITH A POSITIVE CONTROL AT 200 AND A SWEEP OF ALL 17 DOIS RETURNED 0 RECORDS, SO (F2) IS UNTESTED -- NEITHER MET NOR REFUTED -- AND NO FIGURE WAS SUBSTITUTED FROM THE CORPUS. NO WRITTEN DEPOSIT RULE IS LOCATED, BY A SEARCH PROVED BY NAME AND BY CONTENT, WITH THE INTERNAL-UNTIL-FRUIT LAW AND THE SEQUENCING LAW QUOTED AND NAMED AS NOT IT. SIDE-interface-split IS UNDECIDABLE-WITHOUT-CREDENTIALS BUT THE CITING DOCUMENT IS CORRECT AS WRITTEN, BECAUSE PROPOSITION 1 IS VERIFIED IN SIDE-interfaces WHICH RESOLVES; SO b388's ADDITION TO LIST 1 IS WITHDRAWN AS A FALSE DEFECT PRODUCED BY A PREDICATE THAT READ A FUTURE-TENSE MENTION AS A CITATION. AND THIS ACT'S OWN LOCKED FACE CARRIED A WRONG FIGURE, CORRECTED IN THE OPEN WITH BOTH FIGURES PRINTED.",
     '### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS ADDED, SPLIT, MERGED OR RENAMED IN EITHER MAP AND NO PRIOR HEAD WAS REPLACED. ### NOTHING WAS WRITTEN AT ZENODO IN ANY BRANCH AND THIS ACT CARRIED NO WRITE PATH TO THE PLATFORM. ### 0 FIGURES SUBSTITUTED FROM THE CORPUS FOR A LIVE READING. ### 0 ABSENCES CLAIMED WITHOUT A POSITIVE CONTROL. ### THE PRACTICE OBSERVED IS STATED AS OBSERVATION AND NOT AS RULE. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME AND LIST 1 LOSES A MEMBER BY WITHDRAWAL, WHICH IS NOT A CLOSURE. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b389_the_look_see.txt; data/b389_components_run.txt; data/b389_extract_notes3.txt; data/b389_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b389 -- 8 gates read, 4 checked by digest); tools/b389_extract.py; tools/b389_regspec.py; tools/b389_reg_gate.py; tools/b389_components.py; tools/b389_desk_bank.py; tools/b389_checks.py; PLACE-papers SPIRAL_MAP.md, phase1.5/method/THE_LOAD_BEARING_MAP.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 238'),
    # ### THE MAP REFRESHED UNDER (R17) (b388).
    ('the-map-refreshed-under-r17', "b388 (the federation map refreshed in full under (R17): the two emergent clusters seated from quoted moves; the era's unnamed keystones assigned or marked with their evidence; the map re-evaluated and its changes of shape reported not acted on; the prior table preserved verbatim; and the 23 unreadable rows named by cause and routed)",
     "THE FEDERATION MAP IS REFRESHED UNDER THE AUTHOR'S RULING (R17). THE TWO CLUSTERS THAT EXISTED ONLY AS RECLASSIFICATION DESTINATIONS -- theory-space and cross-domain -- ARE NAMED AND SEATED IN SPIRAL_MAP.md, FROM QUOTED REGISTRY MOVES AND FROM NOTHING ELSE: 10 mentions over EXACTLY TWO DESTINATIONS AND NO THIRD, 7 rows recording a move in THEIR OWN STATUS over 4 DISTINCT DOCUMENTS, since A MENTION IS NOT A MOVE. 0 MEMBERS WERE ADDED ON THIS SEAT'S JUDGEMENT and NEITHER CLUSTER CARRIES AN ANCHOR because the ruling names none. THE MAP WAS 97 DAYS OLD AGAINST TODAY AND 85 AGAINST THE REGISTRY'S NEWEST DATE THAT HAS HAPPENED, its forward-looking dates NAMED RATHER THAN USED. 9 OF 11 KEYSTONE-CLASS DOCUMENTS THE OLD TABLE DID NOT NAME ARE ASSIGNED WITH THEIR EVIDENCE PRINTED and 0 BY FILENAME OR DIRECTORY; 2 ARE UNASSIGNED, WHICH IS A PERMITTED AND HONEST OUTCOME AND NOT A DEFECT, NOT OWED, with NO EVIDENCE and NO FIT KEPT APART. 5 CLUSTERS CHANGED SHAPE AND 0 WERE RESHAPED -- THE RESHAPING IS THE AUTHOR'S. ALL 25 KERNELS IN THE MAP'S FEDERATION COLUMNS AND ALL 11 PIN TRIPLES RESOLVE AT THE REF THE MAP NAMES, BUT SIDE-interface-split DOES NOT RESOLVE AT THE ACCOUNT AND THIS ACT CANNOT TELL WHETHER IT IS ABSENT OR PRIVATE. THE PRIOR CLUSTER TABLE IS PRESERVED VERBATIM, 8 OF 8 ROWS RE-READ AFTER THE WRITE, AND NOTHING IS DELETED FROM THE MAP. THE 23 UNREADABLE CORRESPONDENCE ROWS ARE NAMED BY DOCUMENT, LINE AND CAUSE IN 4 GROUPS AND ROUTED, WITH NO ROW EDITED AND NO STATUS ASSIGNED.",
     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO CLASS LINE WRITTEN, NO DECLARATION MOVED, NO REGISTRY ROW EDITED, NO GRADE MOVED, NO CORRESPONDENCE ROW EDITED AND NO LIST CLOSED. ### NO CLUSTER WAS SPLIT, MERGED OR RENAMED. ### NOTHING WAS DELETED FROM THE MAP AND NO SECTION OUTSIDE 4A'S CLUSTER TABLE WAS EDITED. ### NO OTHER CORPUS DOCUMENT WAS WRITTEN INTO. ### 0 MEMBERS ADDED ON A SEAT'S JUDGEMENT; 0 ASSIGNMENTS WITHOUT PRINTED EVIDENCE. ### THE FEDERATION WAS READ LIVE AND NEVER RECALLED. ### UNASSIGNED IS A STATE AND NOT A DEBT. ### THE UNREADABLE ROWS ARE NAMED, NOT READ. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED",
     'data/b388_the_map_refreshed.txt; data/b388_components_notes.txt; data/b388_extract_notes4.txt; data/b388_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b388 -- 8 gates read, 4 checked by digest); tools/b388_extract.py; tools/b388_components.py; tools/b388_desk_bank.py; tools/b388_checks.py; PLACE-papers SPIRAL_MAP.md and OPEN_TRAILS.md; CORRESPONDENCE.md row 237'),
    # ### WHAT THE KEYSTONES` TABLES ACTUALLY CARRY (b387).
    ('what-the-keystones-tables-actually-carry', "b387 (the keystone correspondence union's fourteen located and their rows counted by what backs them; the disagreements between the union and the disk reported and not reconciled; the citation question's bearing stated from practice and not answered; (R16) recorded; and the seat's own memory audited against b386's trim)",
     "THE UNION NAMES FOURTEEN GRADED CORRESPONDENCE TABLES AND 9 OF THE FOURTEEN DOCUMENTS CARRY ONE; 5 CARRY NONE (DOM IFACE SEVEN CNA BALPOS), THE ABSENCE PROVED BY READING EVERY TABLE IN EACH FILE. THE SET IS THE UNION'S OWN keystone-set line AND NOT A PREDICATE OVER THE CORPUS, and the tables were found BY SHAPE AND NEVER BY HEADING -- the predicate WAS WRONG TWICE BEFORE IT WAS RIGHT (a heading test found 7 of 14; a status-column test found 8 and missed R_CURVE_CRITERION, whose column is headed Grade, which is the union's own word). 4 DISAGREEMENTS ARE REPORTED AND 0 RECONCILED: the five with no table; THE UNION POINTS MONO AT 25.8, WHOSE TABLE HAS NO STATUS AND NO GRADE COLUMN, while the monograph's graded table is elsewhere in the same document; two filenames carry a version suffix the union's names do not; and ENGINE'S TABLE IS A WORK-ORDER INSTRUMENT, counted with its shape stated. EVERY ROW IS COUNTED BY WHAT BACKS IT IN THE CORPUS'S OWN WORDS: DERIVES 85, INTERFACES 11, manuscript-resident 10, research-reach 14, shell-or-encodes 19, UNREADABLE 23, AND THE CATEGORIES SUM PER DOCUMENT AND IN TOTAL. EVERY INTERFACES ROW NAMES ITS PREMISE; the unreadable rows are NAMED AND NEVER ASSIGNED. THE ANSWER FROM PRACTICE: 54 OF 162 ROWS (33.3%) ARE NOT MACHINE-VERIFIED AND EVERY ONE IS LABELLED IN THE ROW ITSELF -- A COUNT OF CLAIMED STATUS, SINCE NO KERNEL WAS OPENED. THE BEARING: the standard's three borderlines all turn on READING PARTS OF ONE DOCUMENT DIFFERENTLY and the practice is THE SAME MOVE AT ROW GRANULARITY, so THE PER-ROW PRACTICE EXISTS AND IS IN USE AND WHETHER IT SUPPLIES THE RULE IS THE AUTHOR'S TO SAY; 0 RECOMMENDED. RULING (R16) IS RECORDED WITH ITS REASON. AND THE SEAT'S MEMORY HAS NO PRIOR BLOB, so the comparison used an artifact NAMED AS ONE: 59 shortened hooks, 34 flagged by a screen THAT OVER-REPORTS BY DESIGN, 32 JUDGED COVERED AND 2 JUDGED LOST, the two restored by appending.",
     '### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ROW EDITED, NO STATUS CORRECTED AND NO LIST CLOSED. ### NOTHING WAS CLOSED ON THE DESK AT ALL, BECAUSE A MEASUREMENT IS NOT A CLOSURE. ### NO CORRESPONDENCE TABLE WAS TOUCHED AND THE UNION WAS NOT CORRECTED. ### NO KERNEL WAS OPENED AND NO PRINT AXIOMS RE-RUN, SO EVERY FIGURE IS A COUNT OF CLAIMED STATUS. ### EVERY DISAGREEMENT IS REPORTED AND NONE RECONCILED. ### THE PARTITION SUMS AND THE RESIDUE IS NAMED. ### NOTHING IS RECOMMENDED AND THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND NOT MOVED. ### NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY, WHICH (R16) RULES. ### NO MEMORY ENTRY WAS DELETED AND NO TOPIC FILE REWRITTEN; A RESTORATION APPENDS. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     "data/b387_what_the_tables_carry.txt; data/b387_components_notes7.txt; data/b387_extract_notes3.txt; data/b387_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b387 -- 8 gates read, 4 checked by digest); tools/b387_extract.py; tools/b387_components.py; tools/b387_desk_bank.py; tools/b387_checks.py; PLACE-papers OPEN_TRAILS.md (append-only); the seat's memory directory (two topic files appended to); CORRESPONDENCE.md row 236"),
    # ### THE GUARD MADE SINGLE-SOURCED (b386).
    ('the-guard-made-single-sourced-under-r15', "b386 (the author's ruling (R15) executed: one tracked guard per repository, the installer repointed at it, the exercise passing in all four; the installer's backup defect repaired; the search lesson minted and tested; the navigator's paraphrase corrected)",
     "THE GUARD IS SINGLE-SOURCED UNDER THE AUTHOR'S RULING (R15), ONE GUARD ONE SOURCE. THE SURVEY RAN BEFORE THE LOCK AND COUNTED 9 COPIES ON DISK, NOT TWO -- 5 TRACKED, 4 UNTRACKED, 0 MATCHING NO TRACKED BLOB -- and b385 HAD REPAIRED ONLY ONE OF THEM. b385'S THREE OPTIONS WERE REPRODUCED VERBATIM WITH THEIR LOCATIONS, FROM data/b385_closing.txt AND NOT FROM ITS BANK, WHICH DOES NOT CARRY THEM. OPTION (b) IMPLEMENTS (R15): it leaves EXACTLY ONE TRACKED SOURCE per repository and makes THE INSTALLER READ FROM IT. (a) repairs the text and leaves the topology; (c) is the state the ruling was written to end. NO OPTION WAS RE-WORDED AND NONE INVENTED. relay/tools/git-hooks/pre-push WAS DELETED AFTER ITS RECOVERABILITY WAS PRINTED AND NOT AFTER IT WAS GONE; b304_hooks.py's SOURCE WAS REPOINTED AT .githooks/pre-push; ALL FOUR ROSTERED REPOSITORIES ARE LF-NORMALISED-EQUAL TO THAT SOURCE'S OWN GIT BLOB AND CARRY THE REPAIRED LINE. THE UNTRACKED LEGACY .git/hooks/pre-push COPIES ARE DISPOSED OF BY (R15)'S THIRD CLAUSE AND NOT DELETED, AND THAT JUDGEMENT IS MARKED AS ONE. THE EXERCISE PASSES IN BOTH POLARITIES IN ALL FOUR, REPOS FAILING 0, AND THE FAILING GATE IS CLEARED BY THE REPAIR AND NOT BY THE ARM. THE INSTALLER NEVER OVERWRITES AN EXISTING BACKUP NOW -- STRICTLY STRONGER THAN THE INVARIANT ASKED FOR, NAMED AS A SUBSTITUTION, AND IT FIRED FOR REAL ON THIS ACT'S RUN. THE 3139-BYTE BACKUP b385 DESTROYED IS RECOVERABLE FROM TWO TRACKED BLOBS. THE SEARCH LESSON IS MINTED AND TESTED: A SEARCH FOR A RULE USES THE RULE'S OWN WORDS, NOT THE NAME A READER GAVE IT, and its mechanizable shadow scores b383 2/6 and b385 7/7 attested on the sweep excluding those acts' own records while SEPARATING NOTHING on the contaminated one -- filed MECHANIZED, NECESSARY AND NOT SUFFICIENT. THE NAVIGATOR'S PARAPHRASE IS CORRECTED: THE AUTHORITY IS THE MANIFEST'S DIGEST AND last-commit COLUMNS, NOT THE MANIFEST WHOLESALE.",
     '### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### THE RULE WAS NOT EDITED AND REGISTRY.md WAS READ AND NOT TOUCHED -- THE CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE. ### THE CITATION QUESTION IS AWAITING THE AUTHOR AND WAS NOT MOVED. ### THE RECOVERABILITY PROOF WAS PRINTED BEFORE THE DELETION. ### NO .git/hooks/pre-push WAS DELETED IN ANY REPOSITORY. ### THE FAILING GATE WAS CLEARED BY THE REPAIR AND NOT BY THE ARM. ### THE FACE WAS NOT WIDENED MID-ACT. ### THE TECHNE MODULE IS LOCAL AND NOT PUSHED. ### THE UNTRACKED BACKUPS ARE NAMED, NOT COMMITTED AND NOT DELETED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b386_the_guard_single_sourced.txt; data/b386_components_notes.txt; data/b386_extract_notes2.txt; data/b386_hooks.txt; data/b386_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b386 -- 8 gates read, 4 checked by digest); tools/b386_extract.py; tools/b386_components.py; tools/b386_desk_bank.py; tools/b386_checks.py; relay tools/b304_hooks.py; relay tools/git-hooks/pre-push (DELETED); .githooks/pre-push in all four rostered repositories; TECHNE-Core modules/2026-09/SEARCH_BY_THE_RULES_OWN_WORDS.md (LOCAL, NOT PUSHED); PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 235'),
    # ### THE RULE LOCATED, THE SIX ON THE TRAILS (b385).
    ('the-reservoir-rule-located-and-the-six-on-the-trails', "b385 (the six not-yet-synthesized clusters entered on the trails; the reviewer-reservoir rule located and b383's absence claim refuted; the three that waited on nothing dispatched; the citation question routed)",
     "THE REVIEWER-RESERVOIR RULE IS LOCATED IN REGISTRY.md AT LINE 33, under ## SESSION PROTOCOL -- reviewer mirror-refresh (standing rule, 2026-07-29), and b383'S ABSENCE CLAIM IS REFUTED. b383 SEARCHED FOR THE NAVIGATOR'S NAME FOR THE RULE -- reservoir, reviewer pool, reviewer budget -- AND THE RULE USES NONE OF THOSE WORDS; its control fired and its sweep was honest, so A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED SEARCH FOR THE WRONG STRING. THE NAVIGATOR'S PARAPHRASE WAS SCORED CLAUSE BY CLAUSE: 3 CLAUSES, 2 ACCURATE, 1 OVER-STATED -- the rule makes THE MANIFEST'S md5 AND last-commit COLUMNS the authority and the Currency check widens the disagreement test to three fields, but NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY. AND THE NAME IS NOT IN THE RECORD: the corpus calls it a SESSION PROTOCOL and a standing rule, and A NAME THAT IS NOT IN THE RECORD IS NOT AN ERROR IN THE RULE. THE 6 SUBJECT CLUSTERS WITH NO KEYSTONE ARE ENTERED ON THE TRAILS LEDGER AS NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT, one entry each with the many-to-many rule stated beside every one, and 0 WERE OPENED, RANKED OR PRIORITISED. THE THREE THAT WAITED ON NOTHING ARE EACH DONE OR ROUTED AND NONE PARTLY: the guard's install line REPAIRED UNDER (R4) WITH ITS BEHAVIOUR UNCHANGED; 90 archive files CONFIRMED BY DIGEST AND BY CONTENT AND NEVER BY FILENAME with 0 REMOVED, MOVED OR RENAMED; and the faces ledger ALREADY DONE BY THE RECORD AT b360, CARRIED ON THE DESK FOR TWENTY-FIVE ACTS AFTER IT WAS DONE. THE CITATION QUESTION IS ROUTED AND NOT ANSWERED.",
     "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the four b383 drafted stay ROUTED AND UNAPPLIED. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### REGISTRY.md WAS READ AND NOT TOUCHED AND NO CORPUS DOCUMENT WAS WRITTEN INTO EXCEPT AN APPEND-ONLY TRAIL BLOCK. ### EVERY QUOTED LINE RE-READ AT ITS OWN LINE NUMBER, AND THE ONE LINE THIS ACT REPAIRED UNDER (R4) IS REPORTED IN ITS OWN LINE RATHER THAN COUNTED AS A FAILED RE-READ. ### THE PARAPHRASE WAS SCORED AGAINST THE RULE AND NOT ADOPTED AS ITS TEXT. ### EVERY ABSENCE CLAIM CARRIES A POSITIVE CONTROL. ### NOTHING WAS OPENED, RANKED OR PRIORITISED AND NO SYNTHESIS WAS BEGUN. ### THE GUARD'S BEHAVIOUR IS NOT CHANGED -- ONLY A COMMENT MOVED. ### NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED AND THE MIRROR ROSTER WAS NOT EDITED. ### NOTHING IS RECOMMENDED AND THE CITATION QUESTION REMAINS THE AUTHOR'S. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED",
     'data/b385_the_six_on_the_trails.txt; data/b385_components_notes3.txt; data/b385_extract_notes3.txt; data/b385_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b385 -- 8 gates read, 4 checked by digest); tools/b385_extract.py; tools/b385_components.py; tools/b385_desk_bank.py; tools/b385_checks.py; PLACE-papers OPEN_TRAILS.md (append-only); relay .githooks/pre-push (one comment line under (R4)); CORRESPONDENCE.md row 234'),
    # ### THE FOLD, b371 THROUGH b383 (b384).
    ('the-fold-b371-through-b383', "b384 (the span counted; b371-b383 folded purely additively; the arc's one statement carried from b383)",
     "THE FOLD, b371 THROUGH b383. THE SPAN WAS DECIDED BY THE COUNTER AND NOT BY THIS SEAT: tools/b363_span reads the last fold as b361-b369 filed by b370, so the span starts at b371 and runs through b383 -- 13 acts against b366's author-ruled threshold of nine -- and THE FOLDING ACT IS NOT IN ITS OWN FOLD. F-NOGRADE LOCATED 13 OF 13 HEADLINES BY THE ANCHOR TOOL IN THE BANK OF THE ACT EACH IS ATTRIBUTED TO, and the section would not have been written at all if one were missing; NO ACT IS QUOTED FROM A LATER ACT'S SUMMARY OF IT. ONE SECTION WAS APPENDED TO FINDINGS.md and the committed blob is STILL A TRUE PREFIX. THE ARC'S ONE STATEMENT, CARRIED FROM b383: AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE CORPUS HAD ALREADY RULED AND DID NOT CITE IT ONCE. What it added is b376's TWO-AXIS SEPARATION, b378's facts about kernel identifiers, TWO NEGATIVE RESULTS ABOUT TWO PREDICATES, b382's declaration argument, and b383's correction that THE CONJUNCTION IS EXCLUDED RATHER THAN UNNAMED. AND THE FRESHNESS RULE IT VIOLATED WAS THIS SEAT'S OWN, MINTED AT b368: A MINTED RULE IS NOT A CARRIED RULE. THE ARC HAS TWO UNEQUAL HALVES AND THE FOLD SAYS SO -- FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION.",
     '### NO GRADE WAS MOVED, NO CLASS WAS RULED, NO ACT WAS PROMOTED AND NOTHING WAS DISCHARGED. ### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the four b383 routed stay routed. ### FINDINGS.md WAS APPENDED TO AND NEVER EDITED and no other corpus document was written into. ### THE SPAN WAS COUNTED AND NOT JUDGED. ### F-NOGRADE IS MECHANICAL AND NOT A PROMISE. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     "data/b384_the_fold.txt; data/b384_fold_notes.txt; data/b384_span.json (the counter's emission, run BEFORE the lock); data/b384_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b384 -- 8 gates read, 4 checked by digest); tools/b384_fold.py; tools/b384_desk_bank.py; PLACE-papers FINDINGS.md (ONE APPENDED SECTION) and OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 233"),
    # ### THE STANDARD READ, THE SEQUENCE RECONCILED (b383).
    ('the-standing-standard-read-and-the-sequence-reconciled', "b383 (the standing standard read at content; the eight-act sequence reconciled to it; the author's model banked; four amendments drafted and routed)",
     "THE STANDING STANDARD ALREADY RULED THE CLASS QUESTION. THE_DOCUMENT_CLASS_TAXONOMY, author-ruled 2026-07-28, fixes FOUR TIERS and for each one WHAT IT MUST CARRY AND HOW IT MAY BE CITED: Tier K states grade-terminal-pin and MAY BE CITED AS CERTIFICATION; Tier C organizes certified results and is NEVER CITED AS CERTIFICATION, the standard's own load-bearing rule; Tier N is reference-only; Tier E cites Tier K and nothing cites Tier E. The taxonomy exists to make two failures structurally impossible: a synthesis read as a certification, and a filing-facing framing read as the record. The registry's PHASE ATTRIBUTE section reconciles the rubric's WHEN with the registry's WHERE, now coexisting permanently. THE_LOAD_BEARING_MAP, the keystone correspondence union, ALREADY NAMES 14 GRADED CORRESPONDENCE TABLES. NONE OF THE THREE WAS CITED BY ANY OF THE EIGHT ACTS. THE SEQUENCE RECONCILES AS 3 DUPLICATED AND 5 ADDS, without defence: what it adds is b376's two-axis SEPARATION, b378's facts about kernels at refs, and TWO NEGATIVE RESULTS ABOUT TWO PREDICATES plus a conclusion the standard assumes but nowhere argues. AND THE SEQUENCE VIOLATED THE FRESHNESS RULE THIS SEAT MINTED AT b368: a right belief with no date on it, while the standard that dated it sat author-ruled in the tree. THE NAVIGATOR'S READING IS CORRECTED: the two axes ARE the two tiers, but the conjunction is NOT MERELY UNNAMED -- IT IS EXCLUDED, since the citation rules contradict, the mixed document is disposed of by RULING ONE TIER AND READING THE PARTS APART, and a predecessor scheme was RETIRED for spanning the two. SO THE AUTHOR'S FINISHED KEYSTONE IS A REAL AMENDMENT AND NOT A CLARIFICATION. The author's model is banked verbatim, 11 lines and 0 dropped. FOUR AMENDMENTS DRAFTED AND ROUTED, 0 APPLIED, 0 STANDARDS EDITED. The 6 clusters without a keystone are RESTATED AS NOT-YET-SYNTHESIZED, NOT OWED AND NOT DEFICIENT, with the author's many-to-many rule stated beside the count. The per-document tier sweep is PRICED AND NOT ORDERED at 42 to confirm and 307 to decide from scratch, the judgement NAMED UNPRICED. And the reviewer-reservoir rule COULD NOT BE LOCATED, so (iv) IS ROUTED AS A REQUEST.",
     "### NO STANDARD WAS EDITED AND NO AMENDMENT WAS APPLIED -- the taxonomy, the registry and the union are BYTE-IDENTICAL TO THEIR BLOBS. ### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO GRADE MOVED, NO ACT RE-VERDICTED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### READ AT THE CANONICAL DRIVE, NEVER THE MIRROR. ### EVERY QUOTED LINE RE-READ AT ITS OWN LINE NUMBER AND NO OBLIGATION OR CITATION RULE PARAPHRASED. ### THE READING WAS TESTED AGAINST THE STANDARD'S OWN WORDS AND NOT ADOPTED ON HIS WORD. ### THE RECONCILIATION IS WITHOUT DEFENCE. ### THE AUTHOR'S MODEL IS RECORDED AND NOT APPLIED. ### THE CLUSTER RULE IS STATED BESIDE THE COUNT SO A PLURALITY IS NOT AN ANOMALY AND AN ABSENCE IS NOT A DEFECT. ### THE SWEEP IS PRICED AND NOT ORDERED AND THE UNPRICED PART IS NAMED. ### A SEAT CANNOT RESTATE A RULE IT CANNOT READ. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED",
     'data/b383_the_standard_read.txt; data/b383_components_notes.txt; data/b383_extract_notes3.txt; data/b383_amendment_2026-09-09.txt (banked verbatim, ARRIVED BEFORE THE LOCK); data/b383_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b383 -- 8 gates read, 4 checked by digest); tools/b383_extract.py; tools/b383_components.py; tools/b383_desk_bank.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 232'),
    # ### THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED (b382).
    ('the-sequence-stopped-and-the-evidence-closed', "b382 (the sequence's own account, quoted; the conclusion about method; the exemplar caution; the open items restated)",
     'THE SEQUENCE STOPPED AND THE EVIDENCE CLOSED. The author stopped it and the reason is recorded as the author own: the relating-word feature is NOT BUILT because a third feature would need A SENTENCE UNDERSTOOD RATHER THAN A STRUCTURE MEASURED, WHICH IS A READER AND NOT A PREDICATE. THE ACCOUNT IS QUOTED AND NOT SUMMARISED: 7 acts from the census forward, every claim about a prior act carried by a line from that act own bank RE-READ AT ITS OWN LINE NUMBER, and 0 quotations failed to re-read. THE LOAD-BEARING COUNT WAS RE-MEASURED AND NOT CARRIED: 9 of 349 documents state a role strictly, 26 of 349 broadly, 63 of 404 by purpose statement -- EVEN THE MOST GENEROUS READING FINDS ROLE STATED BY A MINORITY and almost entirely on one side, since only 5 documents declare synthesis. THE CONCLUSION, ABOUT METHOD AND NOT A CLASS: ROLE IS NOT RECOVERABLE FROM A DOCUMENT STRUCTURE AND IS STATED BY TOO FEW DOCUMENTS TO BE RECOVERABLE FROM THEIR PROSE, SO A CLASS RULING MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION -- and ITS LIMIT IS STATED WITH IT: TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF. WHAT A DECLARATION RULE WOULD OBLIGE IS PRICED AND NOT ORDERED: one rule document naming which of the three definitions a declaration declares against; 307 documents lacking a class line, and separately 340 of the 349 saying nothing about their own role so for most the line cannot be written from the document own text -- THE OVERLAP OF THE TWO IS NOT IN THE RECORD AND IS NAMED UNCOUNTED; and a phased application NAMED UNPRICED RATHER THAN ESTIMATED. THE EXEMPLAR CAUTION TRAVELS WITH THE SET: re-derived and not inherited if reused, and NOTHING CURRENTLY RESTS ON IT, measured against b381 banked JSON. THE FOUR LISTS, THE REGISTRY DRIFT, THE SIX CLUSTERS AND THE FLOOR ARE RESTATED OPEN.',
     '### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED, NO DECLARATION RULE ORDERED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### THE RELATING-WORD FEATURE WAS NOT BUILT AND NOT BUILT UNDER ANOTHER NAME. ### THE ACCOUNT IS QUOTED AND EVERY QUOTATION RE-READ AT ITS OWN LINE. ### THE LOAD-BEARING COUNT WAS RE-MEASURED UNDER THREE READINGS AND THE CONCLUSION SURVIVES THE MOST GENEROUS. ### THE OBLIGATIONS ARE PRICED AND NONE IS ORDERED -- A PRICE IS NOT A PROPOSAL -- AND THE PART THE RECORD CANNOT PRICE IS NAMED UNPRICED. ### TWO FAILED FEATURES ARE EVIDENCE AND NOT PROOF. ### THE EVIDENCE FILE WAS FINALISED BY AN APPENDED BLOCK AND NOTHING ABOVE IT WAS EDITED. ### THE TEN UNTRACKED RUN RECORDS ARE NAMED AND STILL UNTRACKED. ### THIS ACT LOCKED FACE MIS-DESCRIBED ITS OWN TOOL CAP AND THE CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b382_the_sequence_stopped.txt; data/b380_ruling_evidence.txt (FINALISED, appended, named complete); data/b382_account_notes3.txt; data/b382_extract_notes2.txt; data/b382_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b382 -- 8 gates read, 4 checked by digest); tools/b382_extract.py; tools/b382_account.py; tools/b382_desk_bank.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 231'),
    # ### THE CONTROL REBUILT, AND CO-LOCATION TESTED (b381).
    ('the-control-rebuilt-and-co-location-not-adopted', 'b381 (the old control weakness measured; the control rebuilt from purpose statements; co-location tested against it and NOT adopted; (R14) recorded)',
     'THE CONTROL REBUILT, AND CO-LOCATION TESTED AND NOT ADOPTED. (R14) IS RECORDED AND NOT APPLIED: the class ruling governs by CONTENT AND ROLE AND NOT BY LOCATION, so the download-layer book is inside its reach and outside the mirroring ruling, both hold and neither is edited into the other; it answers b379 filing, and THE BOOK REGISTRY DRIFT STAYS OPEN AND IS THE AUTHOR OWN. THE OLD CONTROL WEAKNESS IS ONE FINDING AND WAS MEASURED: b380 threshold was 2 and the lowest synthesis-declarer reach was 2, so NO VALUE OF THE THRESHOLD WOULD HAVE FAILED THAT SIDE, while both gathering declarers disagreed. The rebuild scanned the first 40 lines of 404 documents for a sentence in which the document NAMES ITSELF and names a gathering purpose: 61 exemplars, EVERY MATCH TAKEN AND QUOTED AT ITS OWN LINE, NOT ONE CHOSEN BY JUDGEMENT, against a floor of 5, so THE SET CAN FAIL IN BOTH DIRECTIONS. THE MATCHER WAS REPAIRED TWICE AFTER ITS OUTPUT WAS SEEN AND THE LINEAGE IS PRINTED: 169 then 73 then 63 heads. THE UNIT WAS FIXED ON THE LOCKED FACE BEFORE ANY SCORE because under a blank-line-only definition A BIBLIOGRAPHY IS ONE PARAGRAPH AND THE MOST PARTITIONED DOCUMENT WOULD SCORE AS THE MOST COMBINING. CO-LOCATION WAS SCORED ON THE EXEMPLAR SET ALONE BEFORE ANY CORPUS-WIDE NUMBER EXISTED and it DOES NOT SEPARATE: 1 of 5 synthesis exemplars clear the bar and 2 of 61 gathering exemplars clear it too, lowest synthesis ratio 0.000 against highest gathering ratio 1.000, so THE SETS OVERLAP COMPLETELY AND NO THRESHOLD WOULD HAVE SEPARATED THEM. BRANCH PARTLY, NOT ADOPTED, THE CORPUS WAS NOT SCORED, and (F2) IS NOT REACHED. TWO INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION, WHICH IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE.',
     '### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED BY THIS SEAT. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### (R14) IS RECORDED AND NOT APPLIED AND THE REGISTRY-DRIFT FILING STAYS OPEN AND IS THE AUTHOR OWN. ### THE THRESHOLD WAS DECLARED BEFORE THE CONTROL RAN AND WAS NOT MOVED AFTERWARDS TO MAKE IT AGREE. ### THE CONTROL RAN BEFORE ANY CORPUS-WIDE NUMBER EXISTED. ### THE NON-ADOPTION CLAUSE BOUND AND THE CORPUS WAS NOT SCORED. ### NO PRIOR SCORE WAS OVERWRITTEN AND NO QUADRANT TABLE WAS REDRAWN. ### NOT ONE EXEMPLAR WAS ADDED, DROPPED OR RANKED BY JUDGEMENT AND EVERY ONE IS QUOTED AT ITS OWN LINE. ### THE MATCHER LINEAGE IS PRINTED BECAUSE A READER IS OWED IT. ### WHAT THE PREDICATE IS DEAF TO IS DECLARED. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b381_the_control_rebuilt.txt; data/b380_ruling_evidence.txt (updated); data/b381_exemplars_notes4.txt; data/b381_control_notes2.txt; data/b381_verdict_notes4.txt; data/b381_extract_notes.txt; data/b381_registration_2026-09-09.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b381 -- 8 gates read, 4 checked by digest); tools/co_location.py (SHARED, new: the unit splitter fixtured on all three kinds plus a heading and a fence); tools/b381_exemplars.py; tools/b381_control.py; tools/b381_verdict.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 230'),
    # ### THE ROLE AXIS, SCORED STRUCTURALLY (b380).
    ('the-role-axis-read-from-structure', 'b380 (the premise measured; role read from structure; every document re-scored with its prior score kept beside it; the verdict on the method)',
     'THE ROLE AXIS READ FROM STRUCTURE, AND THE PREDICATE FAILS ITS OWN CONTROL. THE PREMISE WAS MEASURED AND NOT ASSUMED: b376 statement-based predicate RE-RUN on the same bytes with a deliberately BROADER reading beside it so the premise could fail -- 340 of 349 documents say nothing about their own role strictly and 323 of 349 broadly, so THE PREMISE SURVIVES ITS OWN WIDENING. Role then read from WHAT A DOCUMENT DRAWS ON through the new SHARED tools/role_structure.py, fixtured in THREE polarities. THE THRESHOLD WAS SET FROM THE RUBRIC OWN WORDING BEFORE THE CONTROL RAN -- one foreign touch is a citation and two is a combination -- AND WAS NOT MOVED AFTERWARDS TO MAKE THE CONTROL AGREE. NO DIRECTION WAS REGISTERED BECAUSE THERE IS NONE: a different method is not a wider one, so NO MONOTONICITY BAR APPLIES. The column moves to A+ 155, A- 84, A? 110: 230 documents out of NOT DETERMINABLE and NOT ONE the other way, 0 prior scores overwritten, and the both-axes quadrant non-empty for the first time at 26, up from 2. AND THE PREDICATE FAILS ITS OWN CONTROL ON THE RUBRIC OWN DISTINCTION, WHICH IS THE FINDING: it agrees with 7 of the 7 declaring SYNTHESIS and with NEITHER OF THE 2 DECLARING GATHERING, because both gatherers gather WIDELY and a citation graph cannot tell gathering widely from synthesising -- THE A- COLUMN IS NOT MEASURING GATHERING, IT IS MEASURING NARROW REACH. VERDICT ON THE METHOD: PARTLY. REACH IS NOT ARGUMENT, so THE A+ COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE A- COLUMN IS UNVALIDATED.',
     '### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED. ### NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED. ### EVERY ABSENCE CARRIES A POSITIVE CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER. ### THE PREDICATE FAILURE IS REPORTED AT FULL PROMINENCE AS A DEFECT IN THE PREDICATE AND NOT IN THE DOCUMENTS. ### WHAT THE PREDICATE IS DEAF TO IS DECLARED, INCLUDING THAT THE DIRECTORY STANDS IN FOR THE SUBJECT. ### EVERY PRIOR SCORE IS KEPT BESIDE THE NEW ONE. ### NO OPTION IS RECOMMENDED and the ruling remains the author. ### THE STRUCTURAL COLUMN IS THIS SEAT THIRD PREDICATE AND NOT A GROUND TRUTH. ### THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED IN THE CORPUS. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2 UNCHANGED',
     'data/b380_the_role_axis_scored_structurally.txt; data/b380_ruling_evidence.txt; data/b380_rescore_notes.txt; data/b380_verdict_notes2.txt; data/b380_extract_notes2.txt; data/b380_registration_2026-09-08.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b380 -- 8 gates read, 4 checked by digest); tools/role_structure.py (SHARED, new: three polarities, and what it is deaf to declared); tools/b380_rescore.py (b376_axes IMPORTED UNMODIFIED and the prior column RE-RUN, not trusted); tools/b380_verdict.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 229'),
    # ### THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS (b379).
    ("the-suspect-column-re-measured", "b379 (the axis-B column b378 named suspect, re-measured; the row categories; two filings about a document outside the tree)",
     "THE SUSPECT COLUMN RE-MEASURED. b376 axis-B predicate required a DOTTED terminal and b378 found NOT ONE citing document uses the dotted convention alone, so the whole "
     " 303-document B- column was suspect. Re-measured with a both-dialect matcher: B+ moves from 20 to 27, 7 gained and NONE LOST. THE DIRECTION WAS REGISTERED BEFORE THE RUN -- "
     " a widened matcher finds more and never fewer, so a document losing a mark would be A DEFECT IN THE INSTRUMENT and reported as one. AND THE MOVEMENT LANDED ENTIRELY IN THE "
     " CORPUS SILENCE: 0 documents moved into the both-axes quadrant, so the correction ENLARGES THE APPARATUS COLUMN AND LEAVES THE ROLE COLUMN EXACTLY WHERE IT "
     " WAS. A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT: row_categories is new and SHARED, carries the front door own MANUSCRIPT-RESIDENT and RESEARCH-REACH, adds the "
     " three b378 met, and reports 14 absences where the old vocabulary reported 37. THE DAY-1 DOCUMENT CARRIES APPARATUS: 45 of 62 identifiers "
     " locate in a corpus kernel. AND THE DOWNLOAD-LAYER BOOK DRIFTS: the registry carries it at v0_5 as NON-KEYSTONE while later documents carry it at v0_6 and v0.7 as a TIER C "
     " NARRATIVE KEYSTONE, with 3 versions on disk -- A CHAIN THAT MOVED AND A PRECEDENCE SOURCE THAT DID NOT.",
     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL AND REGISTRY.md WAS NOT EDITED --"
     " under the corpus own rule the registry is what the others reconcile TO, and a seat that edits the precedence source to match a document that drifted has inverted the"
     " rule it is enforcing. ### NOTHING ON THE DOWNLOAD LAYER WAS WRITTEN, MOVED, RENAMED OR REMOVED and the book was not read for content. ### EVERY ABSENCE CARRIES A POSITIVE"
     " CONTROL THAT FINDS A KNOWN PRESENCE FIRST, AND AN ERROR EXIT IS NOT AN ANSWER. ### THE CATEGORY MODULE RETURNS A CATEGORY AND NEVER A VERDICT; a category is not an"
     " excuse. ### NO OPTION IS RECOMMENDED and the ruling remains the author. ### THE CORRECTED COLUMN IS THIS SEAT SECOND PREDICATE AND NOT A GROUND TRUTH. ### THE FOUR"
     " OPEN LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2"
     " UNCHANGED",
     "data/b379_the_apparatus_axis_rescored.txt; data/b379_rescore_notes.txt; data/b379_survivors_notes.txt; data/b379_hand_notes.txt; data/b379_filings_notes.txt;"
     " data/b379_registration_2026-09-08.txt (LOCKED before any write, chained on tools/b378_lockgate.py run as b379 -- 8 gates read, 4 checked by digest);"
     " tools/row_categories.py (SHARED, new: the front door own words carried, three categories added, fixtured in both polarities); tools/b379_rescore.py (b376_axes"
     " IMPORTED UNMODIFIED and the prior column RE-RUN, not trusted); tools/b379_survivors.py; tools/b379_hand.py; tools/b379_filings.py;"
     " PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 228"),
    # ### THE REFS WIDENED AND THE CONVENTION SWEPT (b378).
    ("an-upper-bound-at-one-ref", "b378 (the terminal search re-run across every ref; the two conventions swept; the archives confirmed and NOT removed)",
     "AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT. b377 searched 43 refs -- one per kernel -- and reported 37 identifiers no kernel "
     " declares. Searching 270 refs behind 209 distinct commits cuts it to 14. Of the rest, 13 are Mathlib names, 7 name a corpus document rather than a "
     " terminal, 2 are declared ONLY ON A TAG and on no branch, and 1 is declared in more than one kernel. AND THE SHARPEST FINDING IS ABOUT THE SEARCH ITSELF: the "
     " first sweep handed git grep a Python-only pattern, every invocation died, the caller read the fatal exit as NO MATCHES, and it reported ZERO FOUND ACROSS 270 REFS -- "
     " a clean confident false answer exposed only by a CONTRADICTION with b377 own record. THE MATCHER NOW ACCEPTS BOTH CONVENTIONS and the sweep found NOT ONE citing "
     " document using the dotted convention alone, so b376 DOTTED-ONLY axis-B predicate COULD NOT HAVE PASSED ANY OF THEM -- WHICH IS WHAT SELECTED THE SIX. 6 of "
     " 6 archive files the mirror carries are CONFIRMED PRESENT by digest AND title line and NEVER by filename. And one NOT DETERMINABLE document "
     " was read by hand: 20 of 37 identifiers locate in exactly one kernel, SO THE HAND READ DECIDES WHAT THE TABLE SCAN COULD NOT.",
     "### NO CLASS WAS RULED, NO DOCUMENT RECLASSIFIED, NO DECLARATION MOVED AND NO LIST CLOSED. ### NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL. ### NO ARCHIVE FILE WAS"
     " REMOVED, MOVED OR RENAMED; the removal is the author and depends on this report. ### NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION: bare and dotted are both"
     " correct in their own dialect. ### AN ABSENCE IS ONLY REPORTED FROM A SEARCH THAT PROVED IT CAN FIND A PRESENCE, and a git exit above 1 is an error and not an answer."
     " ### A NAME DECLARED IN MORE THAN ONE KERNEL IS NOT A TERMINAL A DOCUMENT CAN CITE. ### b376 AXIS-B COLUMN IS NAMED AS SUSPECT AND NOT RE-MEASURED. ### THE FOUR OPEN"
     " LISTS ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### M-2"
     " UNCHANGED",
     "data/b378_the_refs_widened.txt; data/b378_terminals_notes3.txt; data/b378_archives_notes.txt; data/b378_hand_notes.txt; data/b378_lockgate_notes2.txt;"
     " data/b378_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON A LOCK GATE THAT CHECKS WHAT EACH GATE READ -- 8 gates read, 4 checked by digest);"
     " tools/gate_hash.py (SHARED, new: it stamps a gate record with the sha256 of what the gate read); tools/b378_lockgate.py (fixtured in FOUR polarities);"
     " tools/b378_terminals.py (every ref, both conventions, and a positive control that must find a presence before any absence is reported); tools/b378_archives.py;"
     " tools/b378_hand.py; PLACE-papers OPEN_TRAILS.md (append-only); CORRESPONDENCE.md row 227"),
    # ### THE UNBLOCKED OBLIGATION (b377).
    ("the-pin-was-missing", "b377 (one repair-or-route under an obligation the taxonomy already states, plus evidence for a ruling it does NOT make)",
     "THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL. Of the six documents declaring TIER K and scoring no traversable row at b376, several ALREADY CARRY a Correspondence table "
     " with claims, terminals and axiom profiles; what they lack is THE PIN, one of the three things the taxonomy obliges (grade . terminal . pin). b376 predicate demanded all "
     " four in one row and could not see a table whose terminals are bare rather than dotted, SO THAT DEFECT WAS PARTLY THE PREDICATE OWN AND THIS ACT SAYS SO. Under a branch "
     " the order fixed before any document was read, 2 took ARM 1 (a pinned addendum APPENDED, 8 rows, 3 kernels) and 4 took ARM 2 (ROUTED, nothing repaired). "
     " The author role clause is banked verbatim as EVIDENCE: keystones are for clarifying results and exploring ramifications and insights, and should cover any and all pertinent "
     " or interesting materials rather than tunnel vision in explanatory clarity driven by a particular problem at a particular research phase. IT SPEAKS TO THE ROLE AXIS AND NOT "
     " THE APPARATUS AXIS. Two filings, neither opened: the census definition-versus-operation drift, and 6 subject clusters with registry rows and no "
     " keystone. And the banked column-(d) figure 24 of 32 is restated as a FLOOR against a wider question this act names and does not re-measure.",
     "### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO DECLARATION WAS MOVED AND NO LIST WAS CLOSED. ### A DOCUMENT SAYS WHAT IT SAYS. ### EVERY WRITE INTO A DOCUMENT IS AN"
     " APPEND and the committed blob remains a TRUE PREFIX. ### NO TERMINAL WAS WRITTEN WITHOUT BEING LOCATED IN A KERNEL ON DISK, CHECKED THERE AND FOUND TO RESOLVE TO EXACTLY"
     " ONE KERNEL; ONE UNRESOLVED TERMINAL SENT THE WHOLE DOCUMENT TO ARM 2. ### EVERY PIN IS THIS ACT OWN READING OF THAT KERNEL HEAD, never copied from a document or a row."
     " ### NOT DETERMINABLE IS NOT ABSENT. ### THE TWO THE SCAN LEFT UNDECIDED ARE REPORTED AND LEFT, not repaired, not routed as lacking, not counted among the six. ### NO OPTION"
     " CARRIES A PREFERENCE WORD AND THE RULING REMAINS THE AUTHOR. ### BOTH FILINGS ARE FILED AND NEITHER IS OPENED; the census is QUOTED, NOT REPAIRED. ### THE FOUR OPEN LISTS"
     " ARE RESTATED OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE"
     " OBJECT. ### NO COORDINATE IS CLOSED. ### M-2 UNCHANGED",
     "data/b377_the_unblocked_obligation.txt; data/b377_branch_notes3.txt; data/b377_evidence_notes.txt; data/b377_extract_notes.txt;"
     " data/b377_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON b376 LOCK GATE RUN AS b377 -- 7 of 7 pre-lock gates read and passing, INHERITED NOT REBUILT);"
     " tools/b377_branch.py (the branch applied and not chosen; a name declared in two kernels is not a terminal it can write into a row); tools/b377_evidence.py (the role"
     " clause, the five options quoted whole with a bearing line each, and the two filings); PLACE-papers OPEN_TRAILS.md (append-only) and the ARM-1 documents (an APPENDED"
     " Correspondence addendum each, NO EXISTING BYTE CHANGED); CORRESPONDENCE.md row 226"),
    # ### THE TWO-AXIS READ (b376).
    ("every-test-crosses", "b376 (one read over 349 documents on two axes; it produces the evidence a class ruling needs and MAKES NO RULING)",
     "EVERY TEST CROSSES. The corpus three definitions of KEYSTONE each mix two independent axes -- axis A, synthesises against other available content, and axis B, carries a "
     " correspondence table naming kernel, terminal, pin and grade that a stranger can traverse. All 3 tests cross the quadrants and NONE equals either axis, so THE THREE TESTS DO NOT DISAGREE BECAUSE ONE IS WRONG -- "
     " EACH IS ASKING BOTH QUESTIONS AT ONCE. And the corpus own prior attempt does it too: THE_KEYSTONE_CENSUS states three clauses and operationalises two through proxies, DROPS "
     " CLAUSE (iii) ENTIRELY and ADDS A SIZE FLOOR THE DEFINITION NEVER MENTIONS; re-applied at the head its own operation returns 29 where it printed 16. "
     " 20 documents carry a traversable row and 18 of those say nothing about their own role, SO THE APPARATUS AND THE PROSE COME APART; of the 17 declaring TIER K, 9 carry a "
     " traversable row and 6 do not. THE RUBRIC-TEST SET IS A FLOOR AND NOT A POPULATION, and MOST QUALIFIERS QUALIFY ON A CLASS LINE A LATER ACT WROTE INTO THE DOCUMENT. "
     " AND THE LARGEST FACT IS THE SILENCE: 340 of 349 documents DO NOT SAY WHAT THEY ARE.",
     "### NO CLASS WAS RULED, NO DOCUMENT WAS RECLASSIFIED, NO CLASS LINE WAS WRITTEN, NO DOCUMENT WAS REPAIRED AND NO LIST WAS CLOSED. ### A MARK ON AN AXIS IS NOT A CLASS."
     " ### WHICH TEST GOVERNS IS A RULING AND NOT A READ, and this act states the options and what each would oblige WITHOUT RECOMMENDING ONE. ### THE CENSUS WAS QUOTED, NOT REPAIRED."
     " ### NOT DETERMINABLE IS A FULL ANSWER AND WAS NEVER ROUNDED INTO A QUADRANT. ### AXIS A CANNOT TELL A DOCUMENT OWN VOICE FROM A CLASS LINE A LATER ACT ADDED, which is"
     " load-bearing on the floor finding and is printed beside it. ### AXIS B READS THE SHAPE OF A TRAVERSABLE ROW AND NEVER THE TRAVERSAL: NO KERNEL WAS OPENED AND NO PIN RESOLVED."
     " ### WHERE DECLARATION AND APPARATUS AGREE THAT IS REPORTED AS AGREEMENT AND NOT AS CONFIRMATION THAT THE DECLARATIONS ARE CORRECT. ### THE FOUR OPEN LISTS ARE RESTATED"
     " OPEN BY NAME. ### NO NEW TRACKING DOCUMENT WAS CREATED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ###"
     " THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",
     "data/b376_the_two_axis_read.txt; data/b376_prior_notes.txt; data/b376_axes_notes2.txt; data/b376_tests_notes3.txt; data/b376_lockgate_notes2.txt;"
     " data/b376_registration_2026-09-08.txt (LOCKED before any write, CHAINED ON A GATE THAT READS EVERY PRE-LOCK GATE -- 7 of them, fixtured in both polarities);"
     " tools/b376_lockgate.py (the cure for b375 incident: a tool that REFUSES, not a note that remembers); tools/b376_prior.py (the corpus own prior attempt, heard first);"
     " tools/b376_axes.py (two axes quoted from their sources, each fixtured in both polarities, each declaring what it is deaf to); tools/b376_tests.py (the crossings and the floor);"
     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT SCORED BY THIS ACT WAS EDITED); CORRESPONDENCE.md row 225"),
    # ### THE KEYSTONE AND CLUSTER CENSUS (b375).
    ("three-tests-one-word", "b375 (one census over 349 documents; it classifies and repairs nothing, confers no class, moves no grade and closes no list)",
     "THREE TESTS, ONE WORD. The corpus carries three definitions of KEYSTONE and they do not select the same documents: the author-ruled taxonomy Tier K (certification at a pin) selects "
     " 17, the order rubric (synthesis against other content) selects 32, and THE_KEYSTONE_CENSUS own test selects 16 -- and only "
     " 3 documents are in all three. 349 tracked documents were classified from content and never from a path; 42 declare a class line and 307 do not. 6 subject "
     " clusters have registry rows and no keystone. Column (d) of the integration state is non-empty for 24 of 32 keystones. And with b374 audit UNMODIFIED the keystone layer carries "
     " 19.5 hedges per thousand sentences against the support layer 7.7 -- THE OPPOSITE DIRECTION FROM b374 OWN MEASUREMENT ONE ACT AGO, WITH THE SAME INSTRUMENT AND A DIFFERENT DEFINITION.",
     "### NOTHING WAS REPAIRED AND NO CLASS WAS CONFERRED ON A DOCUMENT THAT DECLARES ITS OWN; every declared class line is QUOTED VERBATIM and never overwritten or translated. ### A"
     " DECLARATION OF NOT PLACED IS A DECLARATION and the census does not place those documents. ### WHICH OF THE THREE TESTS GOVERNS IS A RULING AND NOT A READ, and this act "
     " measured all three and reconciled none. ### A MEASUREMENT OF A LAYER IS A MEASUREMENT OF WHICHEVER DEFINITION OF THAT LAYER YOU USED. ### NO CLUSTER WAS ENUMERATED FROM A"
     " DIRECTORY NAME AND NO KEYSTONE WAS ASSIGNED BY RESEMBLANCE; UNASSIGNED is an answer. ### NO CELL WAS INFERRED -- NOT DETERMINABLE FROM THE DOCUMENT is a full answer. ### NO"
     " KERNEL WAS OPENED AND NO CITATION WAS CHECKED. ### NO DOCUMENT IS PRONOUNCED TO FAIL THE RUBRIC; the measurement is the product and the disposition is the author. ### NO LIST"
     " WAS CLOSED -- the four lists b373 and b374 produced are restated OPEN by name. ### NO NEW TRACKING DOCUMENT WAS CREATED; where the census should live is ROUTED. ### NO LEAN"
     " FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",
     "data/b375_the_keystone_and_cluster_census.txt; data/b375_population_notes.txt; data/b375_clusters_notes2.txt; data/b375_integration_notes.txt; data/b375_rubric_notes.txt;"
     " data/b375_registration_2026-09-08_reissued.txt (LOCKED before any write, on the audit exit code AND the registration gate AND the term scan);"
     " data/b375_registration_2026-09-08.txt (THE FIRST FACE, LEFT ON THE RECORD WITH ITS SEAL INTACT: it carried a live struck-stem use this seat did not read before locking);"
     " tools/b375_population.py (three columns, never merged); tools/b375_clusters.py (from the documents and the registry, never from paths);"
     " tools/b375_integration.py (four columns, never averaged; column (d) by anchor); tools/b375_rubric.py (b374 audit UNMODIFIED, with the control beside it);"
     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT CLASSIFIED BY THIS ACT WAS EDITED); CORRESPONDENCE.md row 224"),
    # ### THE DESCRIPTIVE LAYER MEASURED, AND THE FUNCTIONAL EQUATION FILED (b374).
    ("descriptive-layer-measured", "b374 (four measurements and one filing; it repairs nothing, grades no document, modifies no instrument and proves no theorem)",
     "A COUNT OVER PROSE IS A COUNT OF SHAPES AND THE SHAPES ARE NOT FAULTS. The hedge audit was run UNMODIFIED over the keystone corpus and the deposited companions -- a surface it had"
     " never covered. Per thousand sentences the keystones hedge 6.9, the deposited companions 7.6, the working notes 13.3; undated figures run 9.7 against "
     " 8.7. THE GLOSSARY IS ENTIRELY CURRENT and its frozen twin diverges by nothing at all. The bibliography carries 69 entries, 51 pointing at an external work,"
     " and 5 cited nowhere in the corpus but the register itself. The count-and-ref sweep lists 2965 figures across the roster stated without a ref, tag, version or"
     " date IN THEIR OWN SENTENCE. And the functional equation is FILED at the level of the family, with both halves quoted from their own acts.",
     "### NOTHING WAS REPAIRED IN ANY COMPONENT: no sentence rewritten, no entry rewritten, no figure dated, no document graded, no instrument modified. ### A HEDGE IS NOT A FAULT and"
     " the count is not a score; a document that says this is conditional is doing what the record demands everywhere else. ### THE THIRD CLASS IS NAMED UNSOURCED EXPECTATION AND NOT"
     " IMPORTED, because the predicate can see only that the document offers no source -- the second word would claim what the tool cannot see. ### AN EXTERNAL WORK WAS NEVER EXPECTED TO"
     " LIVE IN THIS RECORD, so the bibliography test is stated as: is the entry still cited under that key. ### THE WINDOW FOR A REF IS THE SENTENCE AND THAT IS A DECLARED CHOICE; the"
     " document-wide alternative is named so the author can disagree. ### THE LIST IS THE PRODUCT AND IT IS NOT RANKED, NOT PRIORITISED AND NOT A PLAN. ### THE FILING CARRIES ITS OWN"
     " LIMIT IN ITS BODY AND NOT IN A FOOTNOTE -- none of the reflection is extended to the finite places -- and it joins nothing the two acts did not join. ### NO NEW MATHEMATICS, NO"
     " GRADE CONFERRED OR MOVED, NO BAR SET. ### NO FROZEN SURFACE EDITED. ### NO PIN ADDED. ### CLOSING NOTHING IS THE RIGHT ANSWER FOR A LEG THAT MEASURES AND REPAIRS NOTHING. ### NO"
     " LEAN FILE TOUCHED, NO BUILD RUN. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",
     "data/b374_the_descriptive_layer.txt; data/b374_hedge_notes.txt; data/b374_entries_notes2.txt; data/b374_figures_notes.txt;"
     " data/b374_funceq_notes.txt; data/b374_desk_notes.txt;"
     " data/b374_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b374_hedge.py (the instrument IMPORTED and untouched, with two predicates this act declares as its own); tools/b374_entries.py (four words and no fifth);"
     " tools/b374_figures.py (the sweep, with the ref-window declared); tools/b374_funceq.py (the filing, quotations pulled by anchor and never typed);"
     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO DOCUMENT SWEPT BY THIS LEG WAS EDITED); CORRESPONDENCE.md row 223"),
    # ### THE PINS SOURCED FROM THE WRITING ACT, AND THE STATUS COLUMN LISTED (b373).
    ("rule-outruns-record", "b373 (one ruling executed to exhaustion and writing nothing, one status sweep listed and routed, one licensed instrument corrected; it opens no kernel and moves no grade)",
     "A RULE CAN OUTRUN THE RECORD IT REACHES INTO. Ruling (R9) says a citing row names a pin, sourced ONLY from the act that wrote the row and located in that act own bank, never from the current"
     " head. It was executed over all 119 pinless rows at 2.0 seconds a row, and IT WROTE NO PIN. Not because the price did not fit and not because the seat declined:"
     " BECAUSE THE CHAIN THE RULING REQUIRES DOES NOT CLOSE. 33 of 119 rows have a locatable writing act (28 percent); 86 were introduced by commits whose subject names no"
     " act at all; and the pins instrument that banks a kernel ref begins at b300, later than most rows that need one. THE PAPERS ARE OLDER THAN THE INSTRUMENTS. 10 rows were PINNABLE and every"
     " one of them sits on a deposited companion, an archived snapshot or an append-only ledger entry, which this seat will not rewrite on a citation-hygiene ruling. THE STATUS COLUMN: 6 rows in"
     " two documents assert a grade against a declaration this record has classified retired or absent, and EVERY ONE IS INSIDE THE TWELVE b372 ALREADY FLAGGED -- the sweep of 14974 table rows across"
     " 349 files found no instance outside that set.",
     "### NO PIN WAS WRITTEN TO ANY ROW AND NO PIN WAS TAKEN FROM ANY CURRENT HEAD. ### NO ROW WAS CHECKED AT ANY PIN: adding a pin dates a claim, it does not verify one, and no kernel was opened."
     " ### NO GRADE WAS MOVED BY THIS SEAT; a seat that regrades is a seat that decided what was verified, and the author faces three named choices per row without one being chosen. ### NO DEPOSITED"
     " FILE, NO ARCHIVED FILE AND NO APPEND-ONLY LEDGER ENTRY WAS EDITED -- a deposited companion edited here no longer matches what was deposited, an archive that changes is not an archive, and a"
     " ledger row is a historical statement already dated by the act that wrote it; whether those surfaces should carry pins is ROUTED. ### A ROW NOBODY CAN DATE AND A ROW WHOSE KERNEL WAS NEVER"
     " ROSTERED ARE NOT THE SAME PROBLEM and the reasons are kept apart. ### AN ARM THAT TESTS THE VALUE CANNOT TEST THE SOURCE: 8 correctly-sourced pins equal a current head because their kernel"
     " has not moved, and the locked bar forbids writing them; the bar was obeyed and the tension filed. ### THE THREE-WAY SPLIT IN THE STATUS SWEEP DECIDED ROWS: 3 state their own retirement and"
     " 1 grades a declaration b372 found ALIVE, and neither is the defect. ### NO KERNEL RE-CLASSIFIED. ### NO LEAN FILE TOUCHED, NO BUILD RUN. ### LEG 2 NOT BEGUN. ### NOTHING COMPUTED ABOUT THE"
     " OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",
     "data/b373_the_pins_and_the_status_column.txt; data/b373_extract_notes2.txt; data/b373_pins_notes4.txt; data/b373_status_notes3.txt;"
     " data/b373_desk_notes.txt; data/b373_filing_notes.txt;"
     " data/b373_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b373_pins.py (the sourcing chain, declared before it was run, with every link failure keeping its own name);"
     " tools/b373_status.py (the grade sweep, with the three-way split drawn before the sweep ran); tools/b373_desk.py ((R7));"
     " tools/b304_hooks.py (THE ONE LICENSED OWNER INSTRUMENT, corrected: the sentence b372 made false, with its caveat kept);"
     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO ROW IN ANY PAPER EDITED; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 222"),
    # ### THE EOL PIN, THE README FIGURES, THE FIRST BATCH OF ROW CHECKS (b372).
    ("pin-is-a-date", "b372 (one attribute written in two repositories, one README repaired, twelve rows classified and none repaired; it opens no kernel for a build and adds no pin)",
     "A PIN IS A DATE THAT SURVIVES. The same three declarations -- no_conspiracy_twins, no_conspiracy_goldbach, no_conspiracy_sg -- are PRESENT at the pin a row names and RETIRED at the head, and the"
     " rows citing them without a pin cannot say which they meant. Of the twelve flagged rows, 2 were opened AT A PIN and 10 at the kernel live head under ruling (R8) and are marked"
     " CHECKED-AT-HEAD, which is weaker than a pinned row check and the record says why. Across them 13 named terminals classify RETIRED, 5 PRESENT and 4 ABSENT; every RETIRED verdict"
     " quotes the kernel own retirement ledger and none is an inference from absence. THE THREE README FIGURES DO NOT COUNT THREE DIFFERENT SCOPES: they count ONE QUANTITY -- Core zero-axiom terminals,"
     " one per printed line -- AT THREE DIFFERENT REFS, and each was exact when it was written. At 3fe41b9 the headline, the breakdown, the ratio and the shipped profile all read 212; at"
     " 1f423da all of them moved to 250 except the headline, which was left behind; at the head the profile carries 590. AND NONE OF THE THREE NAMES THE REF IT HOLDS AT. THE"
     " END-OF-LINE ATTRIBUTE IS NOW TRACKED IN ALL 4 ROSTERED REPOSITORIES and a fresh checkout of the tracked guard equals its blob in every one; before this act it was 2 of 4, and the two"
     " that failed were exactly the two without the attribute.",
     "### NO ROW WAS REPAIRED AND NO PIN WAS ADDED TO ANY ROW: (R8) makes the addition of pins a SEPARATE RULING, PRICED AND NOT ATTEMPTED, and the classification is the product. ### NO HEAD WAS"
     " WRITTEN INTO A ROW; every head read is recorded in the act own bank and dated. ### A CHECK AT A HEAD IS WEAKER THAN A CHECK AT A PIN: a pinned check is reproducible by anyone who resolves the"
     " pin, and a check at a head is true of a moving target and only as good as the date beside it. ### THE ORDER PRESENT TEST CANNOT BE FULLY SATISFIED IN EITHER KERNEL READ, BECAUSE NEITHER SHIPS A"
     " PRINTED AXIOM PROFILE: a declaration found alive is recorded PRESENT with its profile NOT LOCATED and is not silently upgraded. ### THE ORDER LABEL AND ITS DESCRIPTION NAMED DIFFERENT FILES: the"
     " label said the exclusion kernel README, which has one count line, no breakdown and ships no profile at all; the object was identified BY THE DESCRIPTION, because a description is checkable"
     " against a file and a label is not, and NOTHING IN THE EXCLUSION KERNEL README WAS REPAIRED. ### THE FIGURE WAS REMOVED RATHER THAN RESTATED, and the layer census was PRESERVED VERBATIM AND"
     " DATED to the ref it holds at; re-deriving that census at the head rewrites a claim and not a number and is ROUTED. ### THE ATTRIBUTE FIXES WHAT THE NEXT CHECKOUT PRODUCES AND NOT THIS DISK: no"
     " repository was renormalised, no working file was deleted to force a checkout and no branch was created or reset. ### 2 rows the previous act counted as pinned carry something that LOOKS"
     " LIKE A PIN AND IS NOT. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS"
     " UNDECIDED. ### M-2 UNCHANGED",
     "data/b372_the_first_batch.txt; data/b372_extract_notes.txt; data/b372_eol_notes2.txt; data/b372_readme_notes2.txt;"
     " data/b372_batch_notes5.txt; data/b372_desk_notes.txt; data/b372_filing_notes.txt;"
     " data/b372_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b372_eol.py (the attribute, asked of git and verified by a fresh checkout into a scratch directory, both polarities);"
     " tools/b372_readme.py (what each figure counts, measured at the ref that introduced it); tools/b372_batch.py (the twelve rows, re-anchored by content and opened at pin or head);"
     " tools/b372_desk.py ((R7), with every closure required to name a killing file resolved by its recorded clock);"
     " relay/.gitattributes and SIDE-effects/.gitattributes (WRITTEN, the pre-existing path-scoped line PRESERVED); SIDE-global-section/README.md (REPAIRED, original in the bank);"
     " PLACE-papers OPEN_TRAILS.md (an append-only block; NO ROW IN ANY PAPER EDITED; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 221"),
    # ### THE FIRST TARGET SETTLED, THE DESK CLOSED, THE GUARD MOVED (b371).
    ("count-claim-stale", "b371 (one settling, one inventory listed and not checked, one guard moved to a tracked path; it opens no kernel for any row and runs no build)",
     "THE ONE CONFIRMED LIVE CLAIM IS STALE, AND IT WAS EXACT WHEN IT WAS WRITTEN. The construction kernel public description named a Core figure of 114; the printed profile carried exactly"
     " that at tag v0.1.0; the repository is 168 commits past that tag and its profile now carries 590. THE TEST WAS FIXED BEFORE THE READ: SCOPE-DEPENDENT requires that the"
     " two words count DIFFERENT THINGS, and STALE is what remains when they count THE SAME THING AT DIFFERENT REFS. They count the same thing -- the zero-axiom print count of Core -- so the verdict is"
     " STALE and not scope-dependent. AND THE ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE AND NOT PROMOTED TO A SCOPE: the record names summands that add to the figure, but they are the"
     " composition of the tag own count, not a subset of a larger present one. THE DESCRIPTION CARRIED NO REF, TAG, VERSION OR DATE AT ALL, which is why the figure read as current. It is repaired, the"
     " original preserved in the bank because a description has no history. THE DESK CLOSED FOR THE FIRST TIME under (R7): 12 items swept, 3 closed, 9 standing, 0 closures refused for want"
     " of a killing file. SCAFFOLD-TERMINALS is CLOSED after b157, b367, b368 and b369. THE GUARD IS MADE DURABLE: .githooks/pre-push, TRACKED, in each of the 4 rostered repositories, exercised in both"
     " polarities with 0 failing. THE ROW INVENTORY: 320 rows name a kernel and a terminal, 201 with a pin and 119 with none, across 349 tracked markdown files.",
     "### THE ROWS ARE LISTED AND NOT CHECKED: ROWS CHECKED 0, KERNELS OPENED 0, and the sweep claims no completeness because a row whose pin is written in a shape the predicate does"
     " not know is reported PINLESS. ### A ROW WITHOUT A PIN CANNOT BE CHECKED THE WAY (R6) SPECIFIES, which checks a row at the kernel and pin the row itself names -- a finding, not a hole in the"
     " sweep. ### 12 rows name a declaration this record has already classified absent: a CROSS-REFERENCE against a banked finding and NOT A CHECK, and a row so flagged is not thereby wrong. ###"
     " ONE OF THE ORDER THREE RANKING FACTORS CANNOT BE FILLED WITHOUT OPENING A KERNEL, so it is recorded NOT FILLED for every row. ### A CLONE IS NOT GUARDED: core.hooksPath is local config in an"
     " untracked .git/config, so a clone carries the guard and still needs one command; MADE DURABLE is the order word for what was done, not a claim that it is done. THE OLD LOCATION IS LEFT INERT --"
     " a safety net and a trap. ### THE KERNEL OWN README IS NOT REPAIRED: its headline says 212, its own breakdown sums to 250, its ratio says 250/250, and the profile it ships"
     " carries 590 -- ROUTED, and it is the SHARPER half because the README travels with a clone and the description does not. ### THE GUARD OWN FRONT MATTER IS NOT REPAIRED EITHER: moving the guard"
     " made its install line wrong, and an act auditing stale surfaces made one. ### NO ITEM CLOSED WITHOUT ITS KILLING FILE AND DATE, and one closure is flagged because its killing file is this act"
     " own. ### NO ACT IS RE-VERDICTED: (R7) reverses a disposition b368, b369 and b370 each carried, and each obeyed the rule it was given -- the author changed the rule. ### NO LEAN FILE TOUCHED, NO"
     " BUILD RUN, NO AXIOM PROFILE RECOMPUTED. ### NOTHING COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2 UNCHANGED",
     "data/b371_the_first_target.txt; data/b371_extract_notes2.txt; data/b371_settle_notes.txt; data/b371_repair_desc_notes2.txt;"
     " data/b371_inventory_notes2.txt; data/b371_hookpath_notes3.txt; data/b371_desk_notes.txt; data/b371_filing_notes2.txt;"
     " data/b371_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b371_settle.py (the two refs, the deciding equality and the coincidence refused); tools/b371_inventory.py (the declared predicate, the sweep and the price);"
     " tools/b371_hookpath.py (the guard moved to a tracked path and exercised); tools/b371_desk.py ((R7), with every closure required to name a killing file);"
     " SIDE-global-section public DESCRIPTION (repaired; original preserved in the bank) and .githooks/pre-push (NEW, TRACKED); tools/b304_hooks.py (the one licensed owner instrument, following the guard);"
     " PLACE-papers OPEN_TRAILS.md (SCAFFOLD-TERMINALS CLOSED, an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 220"),
    # ### THE APPARATUS ARC, b361-b369 -- THE FOLD (b370).
    ("apparatus-arc-fold", "b370 (a fold; it proves nothing, discharges nothing and moves no grade -- plus one owner instrument repaired and three lore modules minted)",
     "THE FOLD, b361 THROUGH b369 -- 9 ACTS, THE SPAN COUNTED AND NOT TYPED. The counter reads the last fold section own filing line off FINDINGS.md and counts"
     " forward, and the section is written ONLY because the count agreed with the range it names. F-NOGRADE HELD: 0 grade strings were not found verbatim in their own act bank."
     " AND THE ATTRIBUTION WAS THE HARD HALF, NOT THE PRESENCE: the grade word SUPPORTED-BY-THE-SOURCE APPLICATION is b366 RULING and not b365 FINDING, and b365 row carries what b365 own bank says."
     " 7 obstacles are quoted, each located in the bank of the act that ORIGINATED it. THE ARC AS ONE STATEMENT: this span produced NO NEW MATHEMATICS about the clause; it produced two results about the"
     " clause SHAPE -- the approximation register located and closed with its obstruction a RATE (b362), and the Li localization archimedean half supported at zeta with a stated constant (b361, b365) --"
     " and its main product was NEITHER: it was making the record checkable by a reader who trusts none of it. SEVEN OF THE NINE ACTS PRODUCED NO RESULT ABOUT THE OBJECT AT ALL. THE THREE MINTS: one"
     " incident does not show you a partition; a predicate that knows one shape finds one shape; and THE DURABILITY SPLIT -- a repair to a tracked file travels with a clone and a repair to an untracked"
     " one does not, so the guards that have caught the most are the ones a fresh clone starts without. 39 reads, 0 without an anchor.",
     "### A FOLD MOVES NO GRADE AND SETTLES NOTHING. ### NO ACT IN THE SPAN IS RE-VERDICTED: every grade is its own act, checked verbatim against that act bank, and the two shape results are left at"
     " the grades their own acts gave them and are NOT PROMOTED. ### THE CLAUSE HAS NOT MOVED AND NO ACT IN THE SPAN CLAIMS OTHERWISE. ### A FOLD THAT LET THE SEVEN APPARATUS ACTS READ AS PROGRESS ON"
     " THE CLAUSE WOULD BE THE EXACT DEFECT THIS SPAN SPENT ITSELF FINDING ELSEWHERE. ### THE FOLD IS PURELY ADDITIVE: 0 existing sections edited, FINDINGS.md before a true prefix of after and"
     " of its committed blob, read BEFORE THE PUSH. ### STEP ZERO: tools/b363_span.py wrote a run file and a JSON under b363 own stem on every run, whoever ran it -- filed twice, fixed never, a revert"
     " both times. IT NOW READS AND DOES NOT WRITE; --emit writes under the CALLER own stem; its act number is read from the record; and A FIXTURE PROVES IT IN BOTH POLARITIES, because an arm that"
     " cannot fail is not an arm. ### THE THREE MINTS EACH STATE THEIR MECHANIZABLE HALF APART: the first has NONE and says so first; the second is caught by re-derivation and NOT by any arm, because"
     " the gate would have been written by the same hand with the same predicate; the third is mechanizable as a DURABLE / NOT DURABLE column and NOT mechanizable as a ranking by what a guard has"
     " caught. ### THE DESK: 9 of 9 CONFIRMED-BY-FILE, 0 CLOSED -- the THIRD act running to report that number with that caveat, and A MEASUREMENT WHOSE RESULT AND WHOSE"
     " CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING. ### TWO ITEMS NAMED AS STILL OWED: the count claim above the repaired list, so THE FRONT DOCUMENT IS NOT NOW CORRECT; and the hook non-"
     " durability, PRICED AND NOT BUILT. ### COMPONENT 5 IS NAMED, PRICED AND NOT OPENED: no repository audited, no surface read for correctness, and THE PROFILE THAT WOULD SETTLE ITS FIRST TARGET IS"
     " NOT OPENED. ### NO LEAN FILE TOUCHED, NO BUILD RUN, NO TECHNE MODULE PUSHED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### M-2"
     " UNCHANGED",
     "data/b370_the_fold.txt; data/b370_extract_notes2.txt; data/b370_span_notes.txt; data/b370_fold_notes.txt;"
     " data/b370_lore_notes.txt; data/b370_desk_notes.txt;"
     " data/b370_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b370_fold.py (F-NOGRADE, the obstacles and the additive bar); tools/b370_lore.py (the three mints); tools/b363_span.py (REPAIRED: reads, does not write, with a two-polarity fixture);"
     " PLACE-papers FINDINGS.md (one fold section, purely additive, 10555 bytes; FACES_LEDGER.md NOT written, no row moved);"
     " TECHNE-Core modules/2026-09 (3 minted, local commit d48d8ac, NOT PUSHED); CORRESPONDENCE.md row 219"),
    # ### THE LIST REPAIRED IN PLACE, THE ROSTER MENDED, THE PASS PRICED (b369).
    ("list-repaired-in-place", "b369 (a bounded edit under ruling (R4), two hygiene repairs and a priced pass; it writes no Lean, runs no build and audits nothing)",
     "THE LAYER-1 EXPORT LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED VERBATIM IN THE SAME FILE. Ruling (R4): append-only is right for a ledger, where a reader reads the file; it is wrong for"
     " a list, where a reader reads the list. 7 export rows were located, quoted verbatim into the currency note, verified byte-for-byte, and ONLY THEN replaced by 3. The repaired list"
     " carries 0 of the names the classification calls absent, by a CONTENT predicate over the rows themselves. THE EDIT IS BOUNDED AND MEASURED: every byte above the rows is its committed blob own"
     " (True) and every byte below them up to the appended note is too (True), both read BEFORE THE PUSH -- AN EDIT IS NOT AN APPEND. The classification was RE-DERIVED for the third time and"
     " AGREES for the third time: of 20 names, 2 declared and 18 absent. AND THE RE-DERIVATION CAUGHT WHAT NOBODY REGISTERED: b368 SHARPER CLAIM IS WRONG. b368 reported one"
     " retired name as having NO LEDGER ENTRY FOR ITS LAYER AT ALL; the ledger carries an entry HEADED BY THAT DECLARATION OWN NAME. b368 predicate required a backtick or a slash before a name and the"
     " ledger names that one as a bare heading -- A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE. Re-derived from the ledger own entry headings: 10 named outright, 2 named only by its slash"
     " abbreviation (kept apart, because reading an abbreviation as naming its expansions is a judgement not a string match), 6 covered only by a layer entry, and 0 not covered at all --"
     " EVERY RETIRED NAME IS REACHED BY THE LEDGER. THE TWO HYGIENE ITEMS ARE DONE: the exclusion kernel is in the pins roster and carries the pre-push hook, byte-identical to the one tracked source"
     " and exercised in BOTH POLARITIES with 0 failing. THE REFINEMENT PASS IS PRICED AND NOT RUN: 50 repositories enumerated LIVE, 48 of them programme material.",
     "### THE FRONT DOCUMENT IS NOT NOW CORRECT: the paragraph above the repaired list still asserts a count of framework consequences and THIS ACT DID NOT TOUCH IT, because the order said the LIST is"
     " corrected and a count is not a name -- which is why the trail is UPDATED and NOT CLOSED. ### THE PRESERVATION IS NOT AN APPEND AND THE ACT DOES NOT CLAIM A PREFIX ARM IT CANNOT HAVE. ### NO ACT"
     " IS RE-VERDICTED: b368 COUNT stands and is confirmed a third time; its SPLIT is corrected, which is a measurement replaced by a better measurement. ### (R5) HOLDS: no retirement reason is supplied"
     " beyond what the kernel own record carries, and where the record is silent the act says the record is silent. ### NO SENTENCE OF b368 BLOCK IS EDITED -- it is NAMED and marked SUPERSEDED, because"
     " a ruling that reverses a disposition dates the prose that announced it. ### TWO OWNER INSTRUMENTS WERE EDITED AND BOTH WERE NAMED ON THE REGISTRATION FACE BEFORE THE EDIT. ### THE TWO HYGIENE"
     " REPAIRS ARE NOT EQUAL IN DURABILITY: the roster mend is TRACKED and survives a clone, the hook install is NOT, because .git/hooks/ is untracked. ### REPOSITORIES AUDITED 0, SURFACES READ FOR"
     " CORRECTNESS 0, REPOSITORIES GRADED 0 -- audit nothing was the cap and it held; a count-SHAPED string is not a claim and an age is not a staleness. ### THE RANKING IS OF"
     " EXPOSURE, NOT OF ERROR, AND WHAT IT CANNOT SEE IS REPORTED: SIDE-effects is NOT on it, because its description carries no count shape and the claim lived in its front document -- a criterion is"
     " only as wide as the surface it reads. ### THE HINT: (H1) CONFIRMED -- exactly one description uses the word construction and it carries the shape 114 zero-axiom terminals; (H2) NOT LOCATED, because deciding it requires"
     " reading the profile, which is the audit. ### THE DESK SWEEP PRODUCED MARKS, NOT VERDICTS: 9 of 9 CONFIRMED-BY-FILE, 0 CLOSED, and the same caveat a second time -- a file that"
     " mentions an item is not a file that confirms it. A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING. ### NO LEAN FILE WRITTEN, NO BUILD RUN, NO AXIOM"
     " PROFILE COMPUTED, NO SUCCESSOR NAMED, NO DESK ITEM CLOSED, NO GRADE CONFERRED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE"
     " CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b369_the_list_repaired.txt; data/b369_extract_notes.txt; data/b369_repair_notes2.txt; data/b369_hygiene_notes.txt;"
     " data/b369_pass_notes5.txt; data/b369_desk_notes.txt; data/b369_filing_notes2.txt;"
     " data/b369_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b369_repair.py (the located rows, the re-derivation, the ledger split and the three bars); tools/b369_hygiene.py (the roster mend and the hook);"
     " tools/b369_pass.py (the live enumeration, the price and the ranking); SIDE-effects at main = 5530d7c327e0d4d57b408fd3fb24be68f5c98722, its front document REPAIRED and no .lean file written;"
     " PLACE-papers OPEN_TRAILS.md (SCAFFOLD-TERMINALS marked REPAIRED IN PLACE, NOT CLOSED, an append-only block; FACES_LEDGER.md NOT written, no row moved);"
     " tools/b303_pins.py and tools/b304_hooks.py (rosters mended); CORRESPONDENCE.md row 218"),
    # ### THE FRONT DOCUMENT RECONCILED, APPEND-ONLY (b368).
    ("front-document-reconciled", "b368 (a live read, a classification and one appended block; it writes no Lean, runs no build and edits no sentence)",
     "THE FRONT DOCUMENT IS RECONCILED BY AN APPENDED CURRENCY BLOCK, AND THE LIST ITSELF IS STILL WRONG. Of the 20 names AGENTS.md exports at Layer 1, 2 are declared in this kernel own"
     " six .lean files and 18 are ABSENT, at SIDE-effects ref main = afa9ccfbddc21e5bbd5ee2a4cbdf23f6a88498dd, pinned by ls-remote before the first classification and unmoved since b367. THE EIGHTEEN WERE"
     " RE-DERIVED AND NOT CARRIED: b367 constant is held in the classifier as a COMPARISON ONLY and is never an input to the count, and the two independent derivations AGREE. EVERY ABSENT NAME IS"
     " RETIRED: RENAMED 0, NEVER EXISTED 0. Each is classified on its own evidence and none from its own sound -- the ledger names the declaration, or its layer entry records the removal, or the"
     " repository own history shows the name present in an earlier commit and gone now, and that third kind is why no name is NEVER EXISTED. RENAMED 0 IS A REFUSAL, NOT AN ABSENCE OF LOOKING: a"
     " successor was accepted only from a declared mapping, the mapping is deliberately empty, and one resemblance -- a retired name and a live one differing only in case -- was MET AND REFUSED. AND"
     " THE NEW FINDING, WHICH NEITHER b157 NOR b367 HAD: THE RETIREMENT LEDGER NAMES ONLY 9 OF THE 18. Another 8 are covered only by their layer entry, which"
     " records that the layer skeletons were retired without listing which, and 1 HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL -- THE LEDGER IS ACCURATE ABOUT WHAT IT SAYS AND INCOMPLETE"
     " ABOUT WHAT IT NAMES, and the third group is the sharper half: there the ledger omits a name, here it omits a whole layer. 32 reads, 0 without an anchor.",
     "### THE DOCUMENT IS ANNOTATED, NOT REPAIRED, AND THE HALF-REPAIR IS THE POINT: the Layer-1 list above the block STILL EXPORTS 18 ABSENT NAMES and this act did not edit it. A"
     " reader who stops at the list is still misled; a reader who reaches the block is not. REPAIRING THE LIST EDITS SENTENCES, AND THAT IS THE AUTHOR DECISION. ### THE BRANCH WAS DECIDED BY THE"
     " CLASSIFICATION, NOT CHOSEN: every exported name has a kind and the kinds partition the list, so the price-and-route branch was UNREACHABLE. ### APPEND-ONLY IS MECHANICAL AND WAS READ BEFORE"
     " THE PUSH: the file before is a true prefix of the file after (True) and of its committed blob (True). ### THE BLOCK EXPORTS NOTHING -- 0 lines in the document own"
     " export shape, 0 absent names outside a status row -- which is a check on the BLOCK, not on the document. ### NO .lean FILE WAS TOUCHED, NO BUILD WAS RUN, NO AXIOM PROFILE WAS COMPUTED"
     " AND NO EXISTING SENTENCE WAS EDITED. ### THE RETIREMENTS ARE REPORTED, NOT ENDORSED. ### THE DESK-FRESHNESS RULE IS FILED as a TECHNE module, LOCAL ONLY, with b367 and b157 as incidents, and"
     " IT STATES ITS OWN LIMIT: a tool can demand that an item CARRY a file and a date, and no tool can check that the named file still confirms it. ### THE SWEEP PRODUCED MARKS, NOT VERDICTS:"
     " 9 of 9 CONFIRMED-BY-FILE, 0 UNCONFIRMED, 0 CLOSED -- and that result is WEAKER THAN IT LOOKS, because a file that mentions an item is not a file that confirms it."
     " ### NO HOOK WAS INSTALLED and the absence of a pre-push hook in SIDE-effects is FILED AS A FINDING. ### NO ACT IS RE-VERDICTED: b157 and b367 are RE-MEASURED. ### NO GRADE IS CONFERRED BY A"
     " SEAT. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b368_the_front_document_reconciled.txt; data/b368_extract_notes2.txt; data/b368_classify_run2.txt; data/b368_reconcile_run2.txt;"
     " data/b368_desk_notes3.txt; data/b368_filing_notes2.txt;"
     " data/b368_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"
     " tools/b368_classify.py (the live ref, the re-derivation and the per-name evidence); tools/b368_reconcile.py (the branch and the append-only arms);"
     " tools/b368_desk.py (the rule and the sweep); SIDE-effects at main = afa9ccfbddc21e5bbd5ee2a4cbdf23f6a88498dd, READ and annotated but with no .lean file written;"
     " SIDE-effects AGENTS.md (one appended currency block); PLACE-papers OPEN_TRAILS.md (SCAFFOLD-TERMINALS marked UPDATED, NOT CLOSED, an append-only block; FACES_LEDGER.md NOT written, no row moved);"
     " TECHNE-Core modules/2026-09/DESK_FRESHNESS.md (local commit 961b9a2, NOT PUSHED); CORRESPONDENCE.md row 217"),
    # ### THE SCAFFOLD REPAIR, NOT LOCATED (b367).
    ("scaffold-not-located", "b367 (a location and a read; it prices nothing, writes no Lean and runs no build)",
     "NOT LOCATED. The scaffold terminals do not exist. Searching the kernel own six .lean files at SIDE-effects ref main = afa9ccf for the names the ledger carries"
     " -- grh_exclusion, twist_cancels, no_ls_zero -- gives 0 LIVE DECLARATIONS. There are 3 mentions and EVERY ONE IS INSIDE A COMMENT: Structural.lean own RETIREMENT LEDGER,"
     " recording that they were removed and why. SIDE-grh-transfer at ref 858cbf6 carries 0 occurrences. THE HINT WAS SCORED AGAINST WHAT WAS FOUND: the kernel and the"
     " structural module CONFIRMED and the two subjects CONFIRMED as the ledger own headings, but THE BRANCH CLAUSE IS CORRECTED (the working head is main and is ahead of both feature branches, with"
     " 0 branches carrying work the read ref lacks), THE COUNT IS CORRECTED (the ledger retires NINE framework consequences; the two subjects carry THREE named declarations), and THE"
     " CHARACTERISATION trivially true IS CORRECTED BY THE KERNEL OWN DISTINCTION -- the audit separates True-valued stubs from opaque-Prop templates and files these two as opaque-Prop. THE HINT"
     " NAMED THE RIGHT TERMINALS AND THE WRONG DEFECT. AND THE RECORD ALREADY FOUND THIS ON 2026-08-25 (b157). THE LIVE DEFECT IS NOT THE SCAFFOLD: the front document AGENTS.md exports 20 named"
     " theorems at Layer 1 of which 18 are ABSENT from the source, exactly b157 figure, unmoved. 35 reads located, 12 anchors differing from the hint that found them.",
     "### NOT LOCATED IS A FULL VERDICT AND NOT A FAILURE OF THE SEARCH. ### THE THREE ROUTES ARE NOT PRICED, CHOSEN OR RECOMMENDED -- all three take the terminal as their input and there is no"
     " terminal; the cap says NOT LOCATED stops the act. ### AND ROUTE (c) IS ALREADY WHAT HAPPENED: the kernel did not price deletion, it deleted, and the retirement ledger IS that route executed."
     " ### NO LEAN FILE IS WRITTEN, NO TERMINAL REPLACED, NO STATEMENT PROVED, NO BUILD RUN, and not one byte of either kernel changed. ### NOTHING IS CLAIMED ABOUT THE MATHEMATICS OF EITHER"
     " SUBJECT: no statement was read, because the kernel holds none. ### THE RETIREMENT IS REPORTED, NOT ENDORSED. ### THE 18-OF-20 FIGURE IS A COUNT AGAINST THE KERNEL OWN SIX .lean FILES AND IS"
     " NOT A CLAIM THAT THE KERNEL IS EMPTY. ### WHAT THE RECORD SANCTIONS IS REPORTED AND NOT RECOMMENDED: of INTERFACES it says this is a legitimate architecture, not a defect, and it uses it at"
     " Route 3 own terminal; and ENCODES-CONCLUSION / SHELL is already classified a work-order, not a citation, so the ban on these two was never a special rule. ### NO ACT IS RE-VERDICTED: b157"
     " finding is CONFIRMED AS STILL LIVE. ### NO GRADE IS CONFERRED BY A SEAT. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE"
     " CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b367_the_scaffold_repair.txt; data/b367_locate_run.txt; data/b367_extract_notes2.txt; data/b367_filing_notes2.txt;"
     " data/b367_registration_2026-09-07.txt (LOCKED before any read of the kernel, on the audit own exit code);"
     " tools/b367_locate.py (the refs, the live-vs-mention split, the front-document count and the bounded sweep);"
     " SIDE-effects at main = afa9ccf and SIDE-grh-transfer at main = 858cbf6, both READ and neither written;"
     " PLACE-papers OPEN_TRAILS.md (SCAFFOLD-TERMINALS marked NOT LOCATED, an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 216"),
    # ### THE DATED-ARM SWEEP (b366).
    ("dated-arm-sweep", "b366 (a classification and a rule; it repairs nothing and rules nothing)",
     "3 DATED ARMS IN THE WHOLE RECORD, OUT OF 1255 ARMS ACROSS 146 GATE SUITES, and 2 of the 3 are ONE SUBSTITUTION FROM STANDING. The third is not harder to"
     " write -- IT IS MISSING ITS CONTENT: its act banked a line number and not the text found there, so there is nothing to look the content up BY. THE SPECIES IS REAL, IT IS CONFIRMED, AND IT IS"
     " NOT A CLASS THIS RECORD IS RIDDLED WITH. The classification is by the author ruling (R2): an arm on the act own artifacts is STANDING and must reproduce; an arm on the living record is a"
     " MOMENT CERTIFICATE unless written by CONTENT rather than by ADDRESS. THE COUNT IS MECHANICAL AND THE CLASSIFICATION IS DECLARED, arm by arm with the code line printed beside it, because a"
     " detector cannot decide whether the file being indexed is the act own artifact or the living record -- that is a question about what a computed path names. 7 lines flagged: 3 DATED,"
     " 1 ADDRESS-SHAPED BUT STANDING (an act indexing its own frozen extraction -- the case that shows the classification cannot be left to a detector), and 3 not address predicates at all."
     " THE DETECTOR FOUND THE ONE CONFIRMED INSTANCE THE RECORD HOLDS, b357 G-LOCATED diagnosed at b364. AND THE REWRITE RULE FELL ON THE HELPER SIDE OF THE ORDER OWN TEST: the substitution is one"
     " call, tools/gate_content.py, with six fixtures in both polarities. 35 reads located, 16 anchors differing from the hint that found them.",
     "### A CLASSIFICATION IS NOT A CURE. ### NO SUITE IS EDITED AND NO DATED ARM IS CURED BY THIS ACT -- a rewrite RULE is a thing a later act applies, and suite files differing from their"
     " committed blobs: 0. ### NO PAST VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED: b363 control is RELABELLED as having measured drift on its dated arms and correctness on its standing ones,"
     " which is not the same thing. ### NO RULING IS MADE BY THIS SEAT: R1, R2 and R3 are the author own and this act executes them. ### THE DETECTOR IS A NET OF THREE NAMED SHAPES AND IS NOT A"
     " DECISION PROCEDURE -- an address predicate written in a shape it does not name would not be found. ### THE COUNT IS OF ARMS THE SUITES REGISTER UNDER A NAME, and 243 registrations whose"
     " name is not a literal are reported as UNATTRIBUTED rather than folded in. ### NO GRADE IS CONFERRED BY A SEAT: (R3) word is the author own, APPLIED and not conferred, and it grades the"
     " ARCHIMEDEAN half and nothing else. ### NO PROOF IS VERIFIED. ### b358 CIRCULARITY FINDING IS UNTOUCHED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO FACE IS PROMOTED. ### NO COORDINATE"
     " IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b366_the_dated_arm_sweep.txt; data/b366_sweep_run.txt; data/b366_extract_notes2.txt; data/b366_faces_row_run.txt; data/b366_mint_notes.txt;"
     " data/b366_registration_2026-09-07.txt (LOCKED before any write, on the audit own exit code, with the pre-lock survey declared on its face);"
     " tools/b366_sweep.py (the count, the detector and the declared classification); tools/gate_content.py (the rewrite rule, six fixtures, both polarities);"
     " TECHNE-Core modules/2026-09/DATED_ARM.md (local-only at 42e41dd, NOT pushed; kept BESIDE modules/2026-09/WRONG_ARM.md and not inside it);"
     " PLACE-papers FACES_LEDGER.md (row U1, an UPDATE BLOCK through the ledger own writer, applying (R3)); CORRESPONDENCE.md row 215"),
    # ### THE OWED READ, PAID (b365).
    ("cuspidality-convention", "b365 (a read; it computes nothing, verifies no proof and moves no grade)",
     "THE CONVENTION IS LOCATED AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF. Lagarias math/0404394v4 states results for irreducible cuspidal representations and the corpus object"
     " is the trivial representation of GL(1), which the same paper marks as its own exception. THE PAPER NAMES A CONVENTION FOR IT AND SAYS WHY IT IS FORCED -- it removes the poles at s = 0 and"
     " s = 1 for that case and concludes that its completed function is entire IN ALL CASES. AND IT CARRIES THE EXCEPTION THROUGH ITS OWN CUSPIDAL-HYPOTHESIS RESULTS, which a hypothesis line alone"
     " would have hidden: Lemma 4.3 is stated for a cuspidal representation and applied to the exception by a Remark printed beneath it, and Lemma 4.2 hypothesis says cuspidal while its own"
     " conclusion defines a term that is 1 exactly when the representation is the trivial one. THE CONSTANT AND THE ERROR TERM ARE DERIVED INDEPENDENTLY OF CUSPIDALITY: C1 depends on N and the"
     " conductor alone, the implied constant is ABSOLUTE in the paper own word, AND THE PAPER PRINTS C1 FOR THE EXCEPTION AS A NUMBER in the paragraph after Theorem 5.1. A PAPER THAT COMPUTES A"
     " THEOREM OWN CONSTANT FOR A CASE IS APPLYING THE THEOREM TO THAT CASE. SO THE LOCALIZATION IS SUPPORTED AT ZETA, WITH A STATED CONSTANT. AND WHAT IN THIS RECORD RESTS ON IT IS A NEGATIVE ANSWER: a bounded"
     " pass found 3 of the ledger 16 blocks citing b358 or b361, every one an update to row U1, and NO BANKED NUMBER OF THIS RECORD IS COMPUTED FROM THEOREM 5.1 CONSTANT."
     " 37 reads located, 17 anchors differing from the hint that found them, 16 source lines located at the pinned rendering.",
     "### NO GRADE MOVES IN EITHER DIRECTION: H-CUSP stands where b358 left it and b361 decision stands where b361 left it, and A READ THAT SUPPORTS A GRADE DOES NOT RAISE IT. ### THE SUPPORT IS"
     " BY THE PAPER OWN APPLICATION AND NOT BY ITS OWN QUANTIFIER: the theorem hypothesis line still says irreducible cuspidal and the paper never re-states it to admit the exception; what it does"
     " instead is APPLY it, which is weaker and is what the quotations support. ### NO PROOF IS VERIFIED -- this act read what the paper states, checked no derivation, and could not; A LOCATED"
     " STATEMENT IS NOT A PROVED ONE. ### b358 CIRCULARITY FINDING IS UNTOUCHED and nothing here bears on the zero channel. ### NO SOURCE WAS FETCHED and the rendering seam stands. ### THE"
     " THRESHOLD IS PROPOSED AT 9 ACTS AND NOT RULED, with the spread 4 to 16 printed beside it. ### THE MINT SHIPS NO ARM and claims no audit. ### NOTHING WAS COMPUTED"
     " ABOUT THE OBJECT. ### NO ACT IS RE-VERDICTED. ### NO FACE IS PROMOTED. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b365_the_owed_read_paid.txt; data/b365_read_run2.txt; data/b365_extract_notes2.txt; data/b365_mint_notes.txt; data/b365_filing_notes.txt;"
     " data/b365_registration_2026-09-07.txt (LOCKED before the read, on the audit own exit code, with the pre-lock search declared on its face);"
     " the pinned rendering at data/b358_source_lagarias0404394.txt (pinned b327, re-verified b358, NOT re-fetched here);"
     " TECHNE-Core modules/2026-09/WRONG_ARM.md (local-only at 86a0dc1, NOT pushed);"
     " PLACE-papers OPEN_TRAILS.md (W-ORD-LI-CUSP marked PAID; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 214"),
    # ### THE COPY THAT DID NOT REPRODUCE, DIAGNOSED AND NOT REPAIRED (b364).
    ("dated-arm", "b364 (a diagnosis; it repairs nothing and decides nothing that is the author own)",
     "THE COPY WAS INNOCENT AND THE BRANCH IS REAL. b363 found b357 copy reporting a failing gate where b357 banked none. b364 ran the BANKED SUITE tools/b357_checks.py AT ITS OWN"
     " LOCATION, UNEDITED, and it reports the same GATES FAILING : 1 ['G-LOCATED'] -- the same arm and the same four rows. THE FAILURE HAS NOTHING TO DO WITH COPYING, PATHS OR A"
     " WORKING DIRECTORY. THE PREDICATE IS QUOTED FROM ITS OWN SUITE AND NOT PARAPHRASED (5 lines located by the anchor tool). THE ARM CERTIFIES TWO THINGS AND ONLY ONE HAS"
     " FAILED: (a) that every row b357 classified is still findable at its own ledger NOW, located by the row OWN TEXT -- rows re-located at their ledgers : 12 of 12 ; unclassified : 0; and (b) that any row whose LINE NUMBER moved is"
     " declared in b357 own bank with both numbers -- and THAT HALF CANNOT HOLD AND CANNOT BE MADE TO, because it compares a number computed now against a literal in a bank written once, in an"
     " append-only file that may never be edited. 4 rows have moved: FACES_LEDGER.md 140 to 141; FACES_LEDGER.md 176 to 177; banked_index.py 1022 to 1232; banked_index.py 613 to 823. b357 declared two of them itself, the ones its own index append caused, and could not"
     " declare the rest. THE SPECIES IS NAMED: A DATED ARM -- an arm whose pass condition is a literal in a frozen file, compared against a quantity recomputed at every run, is dated by"
     " construction; it does not become wrong, it becomes old. 21 reads located, 10 anchors differing from the hint that found them.",
     "### A DIAGNOSIS IS NOT A CURE. ### NO VERDICT IS WITHDRAWN AND NO ACT IS RE-VERDICTED: b357 verdict was true when it was banked, and what is recorded is that RE-RUNNING that suite today"
     " no longer reproduces it, and why. ### NO ARM IS REPAIRED AND NO SUITE, BANK, INDEX OR RUN FILE IS EDITED -- diagnose, do not repair-to-pass, and every file read is proved byte-identical to"
     " its committed blob at both ends. ### b357 FINDING IS UNTOUCHED: which passages say what, and the 5 wider / 6 narrower / 1 silent split, rest on the half that still holds at every row."
     " ### A DATED ARM IS NOT A WRONG ARM: a wrong arm was wrong the day it was written and a dated arm was right the day it was written, and they need different cures. ### NO CURE IS PROPOSED:"
     " the filing names the author choices and prefers none. ### THE OTHER FIVE SUITES WERE NOT AUDITED for arms of this shape and are not claimed clean. ### THE ABSOLUTE-PATH WORK-ORDER IS NOT"
     " RESTATED, because this is not its incident. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO GRADE IS CONFERRED BY A SEAT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED."
     " ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b364_the_copy_that_did_not_reproduce.txt; data/b364_diagnose_run.txt; data/b364_filing_notes.txt; data/b364_extract_notes2.txt;"
     " data/b364_registration_2026-09-07.txt (LOCKED before any read of the suite and before any run of it, on the audit own exit code);"
     " tools/b364_diagnose.py (the predicate, both runs and the unchanged bar); tools/b364_filing.py (the filing);"
     " PLACE-papers OPEN_TRAILS.md (FINDING-DATED-ARM, an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 213"),
    # ### THE ANCHORED GATE ARMS, COUNTED AND NOT ASSERTED (b363).
    ("anchored-gate-arms", "b363 (a tool, a count and a filing; it computes nothing about the object)",
     "BUILT AND FOUND NARROWER THAN THE RULE IT WAS PROPOSED UNDER. tools/gate_needle.py takes a typed hint, returns the FILE OWN LINE, and compares under a"
     " normaliser both sides pass through, stripping marker runs WHEREVER THEY OCCUR and not only at line start -- seven fixtures, both polarities, including an"
     " arm that SHOULD fire and still does. THE POPULATION IS COUNTED AND NOT TAKEN FROM THE DRAFT: the three acts own headline figures, located by the anchor"
     " tool at their own banks, are FOUR, TWO and FIVE, summing to 11; 11 arms were enumerated one by one, each pinned to the bank line that"
     " describes it; AND THE TOOL REFUSES TO EMIT IF THE TWO DISAGREE. The draft claimed 13 and was wrong about its own banks. THE HELPER WOULD HAVE REACHED"
     " 7 OF 11, against the draft estimate of nine or ten. THE FOUR IT DOES NOT REACH SPLIT INTO TWO KINDS: TWO ARE WRONG ARMS (A3, A10), whose predicates test"
     " something other than what their labels name, and TWO ARE MISSING SENTENCES (A6, A9), arms that were RIGHT. THE CONTROL IS THE BANKED SUITES, UNEDITED:"
     " six copied, run, deleted in a finally, 5 OF 6 reproducing their own act verdict, the exception (b357, G-LOCATED) reported at full prominence."
     " THE HELPER WAS EXERCISED OVER 152 DECLARED NEEDLES: 152 BUILT, 0 REFUSED. 28 reads located, 20 anchors differing from the hint that found them.",
     "### A SHARPER INSTRUMENT IS NOT A RESULT. ### NO ARM WAS ACTUALLY RETIRED: the census says what the helper WOULD HAVE reached had it existed, and the"
     " banked suites are byte-identical to what their acts left. ### NO BANKED SUITE WAS EDITED. ### 7 OF 11 IS NOT A RATE AND NOT A FORECAST -- it is a count"
     " over eleven named arms in three named acts. ### THE HELPER DOES NOT REACH THE WRONG-ARM SPECIES, and the act says so rather than letting a fraction imply"
     " it: A NEEDLE BUILT FROM A FILE IS STILL A NEEDLE FOR THE WRONG QUESTION. ### AND IT MUST NOT REACH A MISSING SENTENCE: a helper that quietened A6 or A9"
     " would be a defect and not a cure. ### THE CLASSIFICATION IS DECLARED DATA AND NOT INFERRED FROM PROSE. ### THE TRAIL ENTRY IS FILED AND NOT PAID, AND"
     " NAMING A READ IS NOT PERFORMING ONE. ### NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED. ### NO ACT IS RE-VERDICTED. ### NOTHING WAS COMPUTED"
     " ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b363_the_anchored_gate_arms.txt; data/b363_trail_notes.txt; data/b363_census_run3.txt; data/b363_extract_notes2.txt;"
     " data/b363_registration_2026-09-07.txt (LOCKED before any write, on the audit own exit code);"
     " tools/gate_needle.py (the shared helper); tools/b363_census.py (the count, the classification and the control);"
     " PLACE-papers OPEN_TRAILS.md (W-ORD-LI-CUSP, an append-only block; FACES_LEDGER.md NOT written, no row moved); CORRESPONDENCE.md row 212"),
    # ### THE APPROXIMATION REGISTER, READ UNDER A CAP (b362).
    ("approximation-register", "b362 (a read and a pricing; it computes nothing and adopts nothing)",
     "LOCATED BUT NOT WORTH OPENING at the reach this record can afford. The classical criterion and the variant restricting its family to the naturals were"
     " located at pinned sources (5 addresses attempted, 5 fetched, every one hashed) and quoted with their hypotheses unfolded one by one; the"
     " navigator\'s hint was treated as a SEARCH STRING AND NEVER AS A SOURCE and comes out CONFIRMED, WITH ONE CORRECTION -- the space, which the source"
     " itself flags as a modified form of an original set elsewhere. THE STRUCTURAL FINDING: A FINITE INSTANCE HERE IS AN UNCONDITIONAL UPPER BOUND, since"
     " the quantity\'s definition mentions no zero and no hypothesis and an infimum over a subset is at least the infimum over the whole -- SO THIS REGISTER"
     " DOES NOT CARRY THE SHORTFALL THE WINDOW ACT FOUND IN THE POSITIVITY REGISTER. THE SHORTFALL IT CARRIES INSTEAD IS THE RATE: the criterion is a"
     " statement about a LIMIT and an UNCONDITIONAL theorem bounds the finite side away from zero at every reach, while the only UPPER bound located is"
     " CIRCULAR AT (i), made under the hypothesis in its source\'s own words. So what is unconditional here is the OBSTRUCTION and what would be progress"
     " is CONDITIONAL. 37 reads located, 7 anchors differing from the hint that found them.",
     "### THE REGISTER IS LOCATED AND PINNED AND IS NOT ADOPTED. ### NO FACE IS PROMOTED. ### NO GRADE IS CONFERRED BY A SEAT: the ledger row grades an"
     " IMPORT at cite and says the corpus holds nothing here. ### NOTHING WAS COMPUTED AND NO DISTANCE WAS EVALUATED at any index, by any route, at any"
     " precision. ### A LOCATED STATEMENT IS NOT A PROVED ONE, and a criterion located is not a criterion the corpus holds. ### AN UNCONDITIONAL FINITE"
     " SIDE IS NOT A ROUTE: it is the one thing here better than the positivity register\'s and it buys nothing, because the question was never about"
     " any finite index. ### NOT WORTH OPENING IS A JUDGEMENT ABOUT WHAT THIS RECORD CAN AFFORD AND NOT ABOUT THE MATHEMATICS. ### THE PRICING WAS NOT"
     " ATTEMPTED AND WAS THEN PRICED: the record holds no value, no control and no fixture here, the literature\'s numbers are at a reference this act did"
     " NOT fetch, and an instrument with no control is a number with no standing. ### THE SEARCH IS NOT A SURVEY and what was not located is AN ABSENCE OF"
     " READING. ### NO BRIDGE IS TYPED to any other instance, in either direction. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE"
     " CLAUSE HAS NOT MOVED. ### NO ACT IS RE-VERDICTED. ### M-2 UNCHANGED",
     "data/b362_the_approximation_register.txt; data/b362_read2.txt; data/b362_extract_notes2.txt; data/b362_locate_run.txt;"
     " data/b362_registration_2026-09-07.txt (LOCKED before any read, search or fetch, on the audit\'s own exit code);"
     " the pinned renderings at data/b362_source_*.txt;"
     " PLACE-papers FACES_LEDGER.md (row N1, a NEW row); CORRESPONDENCE.md row 211"),
    # ### THE HELD ITEM, QUOTED THEN BRANCHED (b361).
    ("index-condition-decided", "b361 (a read and one square of zero; it proves nothing and confers no grade)",
     "THE INDEX CONDITION ON THE ARCHIMEDEAN CHANNEL IS VACUOUS FOR THE CORPUS\'S OBJECT: K(pi_triv) = 0, so Lagarias\'s Theorem 5.1,"
     " whose implied constant is ABSOLUTE, holds at every index the corpus computes and its error term O(N(K(pi)+1)) collapses to O(1). b358 left"
     " it UNDECIDABLE-FROM-THE-RECORD under its own cap -- DETERMINED IS NOT COMPUTED -- and named one evaluation as what would decide it. THE"
     " BRANCH WAS FIXED BY THE ORDER BEFORE THE QUOTATION WAS SEEN and the registration was LOCKED BEFORE ANY READ, with the locked face declaring"
     " that this seat had read the item\'s bank one act earlier and that RECOLLECTION IS NEVER A SOURCE FOR A VALUE. The definition is located AT"
     " CONTENT in the pinned source ((2.1), (2.2), (2.3), (5.3)); the source states its own completed L-function for the trivial representation and"
     " states its conductor; at N = 1 these force the archimedean parameter to zero, and (5.3) gives the constant. 35 reads, 0 without an anchor,"
     " 16 anchors differing from the hint that found them. AND THE THING NO SEAT WROTE DOWN: the source\'s own introduction already gives the same"
     " asymptotic for all n >= 1 at (1.12), but with an implied constant that DEPENDS ON pi -- so the index condition was always the price of the"
     " ABSOLUTE constant, and nobody had put the two statements side by side, including b358, which quoted (5.1) and not (1.12).",
     "### AN INDEX CONDITION DECIDED IS NOT A BOUND PROVED, AND IT IS NOT A CLOSED TAIL: the tail is closed by the ZERO channel, which has NO"
     " UNCONDITIONAL BOUND AT ALL. ### THE CIRCULARITY FINDING IS UNTOUCHED -- the tail bound asserts the hypothesis, and no decision here changes"
     " that. ### THE VALUE IS NOT QUOTED FROM THE SOURCE: it is an IDENTIFICATION of two of the source\'s own displayed formulae, and the source"
     " writes neither the parameter nor the constant for this representation anywhere. ### H-CUSP IS INHERITED AND NOT DECIDED: Theorem 5.1 is"
     " stated for an irreducible CUSPIDAL representation and the corpus\'s object is the one the source marks as its exception; b358 graded that"
     " question and this act stands on that grade. ### A VACUOUS CONDITION IS NOT AN OBSTRUCTION REMOVED -- a condition that costs nothing to"
     " satisfy was never the obstruction. ### NO GRADE IS CONFERRED BY A SEAT; the row grade NAMED-ONLY stands. ### NO ACT IS RE-VERDICTED. ### NO"
     " COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",
     "data/b361_the_held_item.txt; data/b361_read5.txt; data/b361_extract_notes.txt;"
     " data/b361_registration_2026-09-07.txt (LOCKED before any read, on the audit\'s own exit code);"
     " the source pinned at b358, data/b358_source_lagarias0404394.txt;"
     " PLACE-papers FACES_LEDGER.md (row U1, an appended UPDATE BLOCK); CORRESPONDENCE.md row 210"),
    # ### THE UNIFORMITY ARC, b349-b359 -- THE FOLD (b360).
    ("uniformity-fold", "b360 (a filings act; it proves nothing and moves no grade)",
     "THE FOLD OF b349-b359: 11 acts filed as one section of the findings document, PURELY ADDITIVE, 180 lines added and nothing above them"
     " edited. THE SPAN IS COUNTED, NOT TYPED: the emitter reads the last fold section\'s own filing line off FINDINGS.md and finds each act\'s bank on disk,"
     " and refuses to emit if the counted span and the result table disagree. F-QUOTE 0 failing; F-NOGRADE 0 failing, the no-grade-moved claim"
     " mechanical as b348 built it. The extract located 68 of 68 reads, 39 anchors differing from the hint that found them."
     " THE ARC AS ONE STATEMENT, at the grade the acts support: the archimedean instrument\'s EDGE is located at the quadrature bound and the floor is still"
     " unexplained; the exponent resolved on the rate axis; the partition UNDECIDED with its coordinates failing in different ways and the abscissa closed"
     " by a sum already in the record; the width statement an equivalence at each fixed support and not across supports; the Li tail circular; the"
     " lawfulness checks confirming the construction rather than testing the class; and THE CLAUSE HAS NOT MOVED. THE THREE THAT RHYME -- the clause\'s"
     " quantifier (b332), the height coordinate\'s enumeration (b351), the width coordinate\'s union (b353) -- with b358\'s localization as a FOURTH ENTRY OF THE"
     " SAME KIND and NOT a fifth obstruction. AND THE AUTHOR\'S RULING EXECUTED: FACES_LEDGER.md added to the mirror roster, 41 rows to 42, appended at"
     " the END so no existing slot changes.",
     "### A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES: it proves nothing, discharges nothing, and MOVES NO GRADE -- checked, not asserted."
     " ### THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, AND NO BRIDGE IS TYPED between them in either direction; the deposit\'s own refusal to"
     " compile cross-register equivalence is quoted at the deposited file. ### AN EDGE LOCATED IS NOT A FLOOR EXPLAINED: b350\'s THE FLOOR IS"
     " UNEXPLAINED stands and b352\'s UNDER-RESOLVED AS A FIT stands. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS"
     " NOT MOVED. ### THE ROSTER ROW IS A CARRYING DECISION AND NOTHING ELSE: carrying a ledger in an archive says nothing about whether what the"
     " ledger says is true, and the addition reaches the archive from this rebuild forward and does NOT place it in any prior mirror. ### THE SPAN\'S"
     " CLOSING SENTENCE IS A STATEMENT ABOUT THIS BOARD AND NOT A CLAIM THAT NO MOVE EXISTS, and it opens nothing. ### NO GRADE MOVED. ### NO BAR"
     " MOVED. ### NO ACT RE-VERDICTED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b360_the_fold.txt; data/b360_fold_run4.txt; data/b360_fold_emitted.md; data/b360_extract_notes2.txt;"
     " data/b360_registration_2026-09-07.txt (LOCKED before any write, on the audit\'s own exit code);"
     " PLACE-papers FINDINGS.md (the appended section); relay tools/mirror_roster.json (the author\'s ruling executed);"
     " CORRESPONDENCE.md row 209"),
    # ### THE LEDGER CURRENCY PASS (b359).
    ("ledger-currency-pass", "b359 (a read, a fetch and a pin sweep; it computes nothing and deposits nothing)",
     "NO DRIFT IS FOUND. Nine claims located and classified across the front door and the federation map -- 7 CURRENT, 2 SILENT, 0 STALE, none unclassified -- and SIX"
     " ASSERTED FEDERATION PINS READ LIVE BY ls-remote, all six resolving on the first attempt and all six MATCHING. THE PRECEDENCE IS THE FRONT DOOR'S OWN, QUOTED AND"
     " OBEYED: \"REGISTRY > README > SPIRAL_MAP for deposits; disk for live pins only, never for deposits\" -- so every deposit claim was ranked against REGISTRY, every"
     " pin went to ls-remote and nowhere else, and NO DEPOSIT FIELD WAS CHECKED AGAINST DISK. THE READ-ONLY FETCH, two GETs, both HTTP 200, both hashed (sha256"
     " 903356429b0876d7..., 11796 bytes): version v1.1.2, DOI 10.5281/zenodo.21539167, concept 10.5281/zenodo.19675355, published 2026-07-24, n_files 11, is_last True"
     " -- five fields against REGISTRY's governing d1-1 row and FIVE AGREEMENTS, and THE CONCEPT DOI RESOLVES TO THE SAME RECORD AND THAT RECORD IS is_last, SO NO"
     " LATEST-VERSION POINTER HAS DRIFTED. The bundle description and the count agree: REGISTRY says the monograph + 6 companions + ONE_PAGE_PROOF + ERRATA + two"
     " graphics, eleven items, and the platform returns eleven. THE TWO SILENT CLAIMS ARE THE JUDGEMENT THAT COULD HAVE GONE THE OTHER WAY: the map's frozen Day-1"
     " table and its v0.6 changelog line both name superseded versions and both are marked as history, and the locked face fixed in advance that a document saying"
     " THIS WAS TRUE THEN is not saying THIS IS TRUE NOW. THE PINS: SIDE-kernel v1.5 0e5233f from both documents; SIDE-lv-conservation deposit-pin v0.10.0 93c27ec AND"
     " working head 2f71068 as TWO OBJECTS IN ONE CELL, each resolved against its own ref; SIDE-effects main afa9ccf; SIDE-t7-topology-cmb v0.3 8eb0d5a. SO NOTHING IS"
     " APPENDED to README.md or SPIRAL_MAP.md and both are left BYTE-IDENTICAL, because a currency pass that finds no drift and writes a note anyway is noise. AND ONE"
     " THING THE PASS FOUND THAT NOBODY ASKED FOR: FACES_LEDGER.md IS NOT IN THE MIRROR ROSTER -- the roster holds 41 source paths, README, SPIRAL_MAP, REGISTRY,"
     " ERRATA and FINDINGS among them, and the faces ledger is not, so the one file this act writes to the papers repo DOES NOT REACH THE MIRROR AT ALL; the roster is"
     " NOT changed and the question is routed to the author.",
     "### A LEDGER RECONCILED IS NOT A LEDGER VERIFIED: named fields against a named ranking party, named pins against live remotes, and neither document read for the"
     " correctness of anything else. ### NINE CLAIMS AND SIX PINS THIS SEAT CHOSE ARE NOT A CENSUS of a 152-line front door and a 438-line map, and a stale claim not"
     " looked for is not counted. ### NOT THAT THE DEPOSIT IS CORRECT -- only that the ledgers agree with it and with each other. ### NOT THAT THE PLATFORM'S RECORD IS"
     " RIGHT: a hash fixes the bytes it returned and nothing more. ### NOT THAT A PIN THAT RESOLVES TODAY WILL RESOLVE TOMORROW, which is why the order said read"
     " live. ### AND THE MIRROR PASSING ITS THREE CLAUSES SAYS NOTHING ABOUT WHETHER WHAT IT CARRIES IS TRUE. ### NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT"
     " ZENODO. ### REGISTRY.md IS READ, NOT WRITTEN. ### NO SENTENCE IS EDITED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO COORDINATE IS CLOSED."
     " ### THE PARTITION STAYS UNDECIDED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b359_the_currency_pass.txt; data/b359_pass_run.txt; data/b359_pass.json;"
     " data/b359_fetch_run.txt and data/b359_fetch.json (two GETs, hashed);"
     " data/b359_fetch_F1.json and data/b359_fetch_F2.json (the bytes the platform returned);"
     " data/b359_extract_notes2.txt (34 of 34 located, 23 anchors differing from their hints);"
     " data/b359_registration_2026-09-07.txt (LOCKED on the audit's own exit code, with its three pre-lock reads declared);"
     " data/b359_mirror.txt (clean on all three clauses, rebuilt AFTER the write);"
     " PLACE-papers FACES_LEDGER.md (row U1's second update block, b358's finding localized);"
     " CORRESPONDENCE.md row 208"),
    # ### THE LI ASYMPTOTICS, READ UNDER A CAP (b358).
    ("li-asymptotics-circular", "b358 (a read and a pricing under a cap; it computes nothing)",
     "EXISTS BUT CIRCULAR. The deposit's finite range is its own sentence -- partialPositivity_finiteRange (v0.8.0) certifies lambda_n >= 0 for n up to Voros's"
     " detection threshold N_0(T) approx 2T^2, a certificate reaching exactly to where discrimination would begin AND NO FURTHER -- and this act asked the"
     " literature, under the import bar, what would close the rest. SEVEN STATEMENTS LOCATED AND PINNED; ONE meets all four conditions locked before any source"
     " was opened (Voros's (17), the tame form for lambda_n); IT FIRES AT ALL THREE LOCKED CIRCULARITY QUESTIONS, and the source says so in its own abstract:"
     " \"For n -> infinity we obtain that if (and only if) the Hypothesis is true, lambda_n ~ n(A log n + B)\", with the derivation opening \"all the zeros lie on"
     " the critical line\". AND THE SPLIT IS EXACT, WHICH IS SHARPER THAN SAYING THE ASYMPTOTIC ASSUMES RH: on the decomposition the record already holds (b327),"
     " THE ARCHIMEDEAN CHANNEL HAS AN UNCONDITIONAL ASYMPTOTIC WITH AN EXPLICIT ERROR TERM FROM BOTH SOURCES INDEPENDENTLY -- Voros's (24) \"unconditionally\", to"
     " all orders, and Lagarias's Theorem 5.1 with an ABSOLUTE implied constant and an explicit index n >= K(pi) -- WHILE THE ZERO CHANNEL HAS NO UNCONDITIONAL"
     " BOUND AT ALL, Theorem 6.1 reducing it unconditionally and bounding it only at \"If the Riemann hypothesis holds for L(s,pi) then...\". SO THE ONE PART OF"
     " THE DECOMPOSITION THAT WOULD CLOSE THE TAIL IS THE PART THE HYPOTHESIS CONTROLS. 4 of 7 statements are circular and 3 are not, AND NOT ONE OF THE THREE"
     " NON-CIRCULAR ONES IS A SHAPE: everything about lambda_n itself is conditional, everything unconditional is about a part. Bombieri-Lagarias Cor 1(c),"
     " quoted inside Voros, is the one statement running in the useful direction and it demands its bound FOR EVERY n. EIGHT HYPOTHESES GRADED TWICE AND NEVER"
     " MERGED: 8 of 8 MET on the sources' own objects; on the corpus's, 3 MET and 5 UNDECIDABLE-FROM-THE-RECORD. THE PRICING: THERE IS NO INDEX BEYOND WHICH THE"
     " LOCATED SHAPE WOULD ACT, because it acts only on the branch its own condition selects; the two banked figures bracketing the demand are n = 300 computed"
     " and n approx 1e18 before a violating zero could register, one labelled division giving 3.33e+15 -- A DISTANCE IN INDEX AND NOT A PRICE IN WALL TIME."
     " Sources pinned: Voros math/0506326 sha256 dd360dab..., 178832 bytes; LAGARIAS math/0404394v4 sha256 86f3d3c4..., 423379 bytes, WHICH IS THE RECORD'S OWN"
     " b327 PIN RE-VERIFIED BYTE FOR BYTE; Coffey math-ph/0505052 searched and not quoted; Bombieri-Lagarias 1999 NOT FETCHED (HTTP 404), as the faces ledger"
     " already recorded, so its corollary is used at one remove and said to be.",
     "### A STATEMENT LOCATED IS NOT A STATEMENT APPLIED, AND THIS ACT APPLIES NONE: no argument constructed, no bound proved, no theorem extended, sharpened or"
     " combined. ### FIVE ADDRESSES, FOUR FETCHED, ONE OF THOSE A DUPLICATE SURFACE -- AN ABSENCE OF READING IS NOT AN ABSENCE OF LITERATURE, and a statement this"
     " act did not look for is not counted. ### NOT A DISCOVERY ABOUT THE LITERATURE: both sources write the conditionality in their own abstracts, and what is"
     " new is only that the record now holds it pinned with the split located at the line. ### NOT THAT NO UNCONDITIONAL TAIL BOUND EXISTS AND NOT THAT NONE"
     " COULD. ### NOT THAT THE FIVE UNDECIDABLE GRADES ARE PERMANENT: H-NGEK is undecidable ONLY BECAUSE THIS ACT'S OWN CAP FORBADE ONE EVALUATION, which is"
     " NAMED AND NOT ORDERED. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE TWO FACES' EQUIVALENCE IS NOT COMPILED. ### NO CLASS IS"
     " DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b358_the_li_asymptotics.txt; data/b358_read_run3.txt; data/b358_read.json;"
     " data/b358_locate_run.txt and data/b358_locate.json (the fetch and the hashes);"
     " data/b358_source_voros0506326.txt and data/b358_source_lagarias0404394.txt (the pinned texts);"
     " data/b358_extract_notes2.txt (33 of 33 located, 18 anchors differing from their hints);"
     " data/b358_registration_2026-09-07.txt (LOCKED on the audit's own exit code, BEFORE any source was opened);"
     " PLACE-papers FACES_LEDGER.md (row U1's update block) and ERRATA.md (E-2026-09-07-1, ruling R2);"
     " CORRESPONDENCE.md rows 206 and 207 (207 is ruling R1's correction row)"),
    # ### WHAT THE LEDGERS SAY THE CHECKS CERTIFY (b357).
    ("what-the-ledgers-certify", "b357 (a read of four ledgers; it computes nothing and edits nothing)",
     "SOME ROWS SAY IT. Twelve passages located and classified across FINDINGS.md, FACES_LEDGER.md, CORRESPONDENCE.md and tools/banked_index.py,"
     " NONE UNCLASSIFIED, splitting 5 WIDER / 6 NARROWER / 1 SILENT -- and THE FIVE WIDER REACH ALL FOUR LEDGERS, which is what made the erratum owed"
     " rather than optional: FINDINGS.md:3039 (b328), FACES_LEDGER.md:140 (b328), FACES_LEDGER.md:176 (b334), CORRESPONDENCE.md:251 (b332),"
     " tools/banked_index.py:1022 (b332) -- A STRADDLING READING, DECLARED BY b352\'S RULE: 1022 is the line the act READ and RELIED ON, and appending"
     " this very key moved that row to 1054, which is where a later reader finds it. THE TWO FINDINGS ARE KEPT APART, AS THE SEAL REQUIRED BEFORE ANY ROW WAS READ: (1) THE ATTRIBUTION FAULT, 3"
     " rows, crediting the Definition 3.1 scan with establishing membership by a parenthetical or by the preposition BY; (2) MEMBERSHIP ASSERTED WITH"
     " NO WARRANT NAMED, 2 rows carrying the same summarised parenthetical. THE CONSEQUENCE, STATED ONCE: CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE"
     " CONSTRUCTION, AND THE SCAN CONFIRMS IT RATHER THAN TESTING IT -- every f is built as g conv g-sharp, for a true autocorrelation the transform is"
     " a squared modulus so positivity is automatic and the scan CANNOT FAIL, and what it discriminates is arithmetic that has gone wrong, which is"
     " what b320\'s own wide-minus-narrow control at min f-hat = -5.85e-01 shows and why the scan is not vacuous. AN INDEPENDENT TEST WOULD REQUIRE AN"
     " OBJECT NOT BUILT AS AN AUTOCORRELATION; NO ACT HAS NEEDED ONE AND NONE IS ORDERED HERE. An ERRATA entry is DRAFTED AND ROUTED and NOTHING IS"
     " WRITTEN TO ERRATA.md. AND THE ACT MADE A FRESH INSTANCE OF ITS OWN SUBJECT: its first run grouped the five wider rows by GREPPING THIS SEAT\'S"
     " OWN COMMENTARY for the word ATTRIBUTION and mis-grouped 2 of 5 -- b348\'s use-and-mention species -- so the grouping is now DECLARED DATA, row"
     " by row, and the superseded run is kept UNEDITED with the verdict, the twelve statuses and the five wider rows IDENTICAL in both.",
     "### THE WIDER SENTENCE IS NOT NECESSARILY FALSE, AND THE ACT DOES NOT SAY IT IS: the corpus builds f with the source\'s support and vanishing"
     " conditions, and WHAT IS WRONG IN THE THREE IS THE WARRANT, NOT THE CLAIM. ### THE MEMBERSHIP QUESTION IS NOT DECIDED -- whether the"
     " piecewise-linear object is in a class defined over smooth functions is b355\'s H1, graded REFUTABLE and ROUTED, and it stands exactly there."
     " ### TWELVE PASSAGES THIS SEAT CHOSE ARE NOT A CENSUS: nothing mechanical enumerated the candidates, so a row that says the wider sentence and"
     " was not looked for is NOT COUNTED. ### THE CORRECTION IS DRAFTED, NOT MADE. ### NO ROW IS EDITED. ### NO BANKED NUMBER IS AFFECTED. ### NO"
     " CHECK IS DEMOTED -- every check that passed still passed. ### NO ACT IS RE-VERDICTED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED."
     " ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b357_what_the_ledgers_say.txt; data/b357_read_run2.txt; data/b357_read.json;"
     " data/b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt (the first grouping, kept unedited);"
     " data/b357_errata_draft.txt (DRAFTED AND ROUTED, NOT OPENED); data/b357_extract_notes.txt;"
     " data/b357_registration_2026-09-07.txt (sealed on the audit\'s own exit code, before the reading was classified);"
     " CORRESPONDENCE.md row 205"),
    # ### THE OBJECT OR THE BOUNDARY (b356).
    ("object-or-boundary", "b356 (one frame, one parameter re-tuned, deliberately)",
     "THE BOUNDARY. b354 found the sixth rung\'s residual negative AND the rank saturated at the quadrature bound IN THE SAME STEP, and separated"
     " them nowhere. b356 raises NY from 512 to 1024 -- a value the record had already used, being a rung of b344\'s own ladder -- with nothing else"
     " moved. THE CONTROL RAN FIRST AND LICENSED EVERYTHING ELSE: the FIFTH rung under the raised axis has rank 262 EXACTLY as banked and its trace"
     " reproduces b320 to 4.895e-04 worst against a bar of 1e-3 whose floor is b344\'s own measured 9.753e-05 move of THIS axis over EXACTLY this step"
     " -- the observed move being 5.02 times that floor, so a bar set AT the floor would have failed on a correct computation. THE RANK AT THE RAISED"
     " AXIS IS 518 AGAINST A BOUND OF 1024, where b354 measured 512 against 512 and extrapolated to about 516: THE EXTRAPOLATION WAS ACCURATE TO TWO."
     " AND THE RESIDUAL RETURNS POSITIVE AT EVERY COVERED CELL: -2.760e-04 becomes +1.085e-02, -2.215e-04 becomes +9.723e-03, -1.686e-04 becomes"
     " +8.801e-03. SO b354\'S SIXTH RUNG WAS THE INSTRUMENT\'S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS EDGE NOW LOCATED AT X = 256 WITH"
     " NY = 512. AND SIX DIMENSIONS DECIDED THE SIGN: the cut needs 518 and at NY = 512 it got 512, and the six it could not have turned +1.08e-02"
     " into -2.76e-04 -- a change larger than the residual itself, from ONE PART IN EIGHTY-SIX of the cut. The run took 264.6 s against a chosen"
     " ceiling of 1800 s.",
     "### TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE, AND THIS ACT HAS TWO: nothing here says the residual is positive in the limit, and b344\'s own"
     " ladder shows the trace still moving at NY = 2048. ### A SIGN THAT RETURNS UNDER ONE RAISE IS NOT A SIGN THAT IS SAFE. ### b354 IS NOT"
     " RE-VERDICTED -- it named its own ambiguity, could not have resolved it, and its figures stand exactly as banked and are used here. ### THE"
     " RAISED FRAME IS COMPARABLE TO b354\'S SIXTH RUNG AND TO NOTHING ELSE: comparing it to the banked fifth-rung residual moves TWO parameters at"
     " once, and the act refuses that comparison by name. ### b339\'S SIDE-READING IS NOT WITHDRAWN -- b354\'s evidence against it is removed here, so"
     " it returns to where b339 left it, a reading its own act labelled, neither confirmed nor refuted. ### THE FLOOR QUESTION IS EXACTLY WHERE b352"
     " LEFT IT: no fit was ordered and NO SCORE IS REPORTED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR"
     " MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b356_the_boundary.txt; data/b356_raised_run2.txt; data/b356_raised.json;"
     " data/b356_axis.json (b344\'s ladder, read for the bar\'s floor);"
     " data/b356_registration_2026-09-07.txt (sealed on the audit\'s own exit code, before the instrument ran);"
     " CORRESPONDENCE.md row 204"),
    # ### WHAT THE ARRAYS ARE (b355).
    ("what-the-arrays-are", "b355 (a read and a filing; it computes nothing and moves nothing)",
     "THE RECORD DOES STATE WHAT ITS ARRAYS ARE, AT THE LINE WHERE IT MAKES THEM, WITH ITS REASON -- and b353, which graded the smoothness hypothesis"
     " REFUTABLE and said the record did not settle it, did not look at that line. THREE LAYERS, EACH AT AN EMITTING LINE: the GENERATING FORMULA at"
     " carto_atlas.py:49 is exp(-1/(1-t^2)) on the unit interval, the textbook Cc-infinity bump, so the formula the code writes down IS in the class;"
     " the SAMPLED ARRAY at :45 and :50 is that formula at NV nodes divided by its own TRAPEZOID integral; and the OBJECT INTEGRATED at"
     " b317_smear.py:136 is np.interp between nodes and zero outside, stated in words at :126 and given its reason at :128 -- the function this act"
     " integrates is the function the corpus\'s number was formed from. SO THE CHOICE WAS MADE FOR INTERNAL CONSISTENCY WITH BANKED NUMBERS AND NOT FOR"
     " MEMBERSHIP IN THE SOURCE\'S CLASS. H1 and H3 are answered SEPARATELY: H1 fails on what the object IS, H3 is undecided on how far the looking"
     " went, and H3\'s grade stands undisturbed. AND THE DISTINCTION FIXED BEFORE ANY CHECK WAS LOOKED AT: for a true autocorrelation the transform is"
     " the squared modulus and positivity is AUTOMATIC, so A SCAN APPLIED TO AN OBJECT BUILT AS AN AUTOCORRELATION IS NOT AN INDEPENDENT TEST OF CLASS"
     " MEMBERSHIP. The checks one by one: b320\'s 13 of 13 USED BOTH; b320\'s Theorem 1 conditions and covered-cell naming USED NEITHER; b328\'s"
     " lawfulness and every aimed seed at b334, b343, b344 and b349 USED BOTH. NO ACT IN THE FAMILY EVER TESTED CLASS MEMBERSHIP INDEPENDENTLY OF THE"
     " CONSTRUCTION. VERDICT: THE RECORD STATES IT.",
     "### A RELABELLING IS NOT A DEMOTION: every banked number stands exactly as banked, nothing here recomputes one or contradicts one, and every"
     " check that passed still passed -- what changes is the sentence describing what passing established. ### THE OLD READING was that the seeds are"
     " in the source\'s class; THE READING THIS ACT SUPPORTS is that they are built as autocorrelations of a piecewise-linear interpolant of a sampled"
     " smooth bump, and the scan confirms the discrete construction behaves like a continuous one within its reach. THE SECOND IS NARROWER AND IT IS"
     " TRUE; THE FIRST WAS NEVER MEASURED. ### NOT that the two objects give different numbers -- NO ACT HAS MEASURED THE DIFFERENCE. ### NOT that the"
     " corpus chose badly: it chose for a stated reason. ### NO VERDICT IS MOVED BY THIS ACT; whether any turns on the difference is a reading, and the"
     " author moves rows. ### b353\'s width sentence is CONFIRMED AND NOT STRENGTHENED and the partition stays UNDECIDED. ### NO CLASS IS DISCHARGED."
     " ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b355_what_the_arrays_are.txt; data/b355_read_run2.txt; data/b355_extract_notes3.txt;"
     " data/b355_registration_2026-09-07.txt (sealed before the reading was turned into a verdict);"
     " tools/e16/carto_atlas.py:45,49,50; tools/b317_smear.py:126,128,136; CORRESPONDENCE.md row 203"),
    # ### THE SIXTH FRAME (b354).
    ("sixth-frame", "b354 (one new rung, on the existing instrument, nothing re-tuned)",
     "THE SIXTH RUNG OF THE DOMAIN LADDER, WHICH b352 PRICED AND DID NOT RUN, RUN AT (N, X, NY) = (32768, 256, 512). THE ARM THAT LICENSED IT FIRST: the"
     " FIFTH rung recomputed reproduces b320\'s banked values to 0.000e+00 RELATIVE at all three cells, and the sixth frame\'s identity control is"
     " 0.000e+00 against a bar of 1e-9 whose floor is dim*eps = 7.1e-12 -- SO THE SIXTH RUNG IS NOT A BROKEN COMPUTATION. AND ITS RESIDUAL IS NEGATIVE AT"
     " EVERY COVERED CELL (-2.76e-04, -2.21e-04, -1.69e-04), where the five banked rungs had fallen by ratios 0.34, 0.37, 0.42, 0.49 approaching one"
     " half: THE RESIDUAL DID NOT SETTLE ONTO A FLOOR, IT CROSSED ZERO. AND THE SIXTH RUNG IS ALSO THE FIRST AT WHICH THE RANK IS LIMITED BY NY RATHER"
     " THAN BY X -- the banked ranks 20, 37, 69, 133, 262 extrapolate to about 516 and the observed rank is 512, which is NY exactly, short by about"
     " four dimensions out of five hundred. SO THE SIGN CHANGE AND THE INSTRUMENT\'S BOUNDARY ARRIVE IN THE SAME STEP. THE SEALED CRITERION IS UNDEFINED"
     " THERE (log of a negative residual), so NO SIX-FRAME SCORE EXISTS AND NONE IS REPORTED; refitting FIVE frames reproduces b352\'s banked scores to"
     " 3e-12, so b352 is EXTENDED and not re-verdicted. The chosen ceiling was 900 s and the run took 212.1 s, the FIRST MEASURED WALL"
     " THIS LADDER HAS. VERDICT by the letter of the sealed condition: FLOOR UNDER-RESOLVED STILL, for a reason the branch did not anticipate.",
     "### THE SIGN CHANGE AND THE RANK SATURATION HAPPEN AT THE SAME RUNG AND THIS ACT SEPARATES THEM NOWHERE: nothing here decides whether the object"
     " crosses zero or whether the instrument stopped being able to say. ### THE INSTRUMENT DID NOT FAIL -- its own controls hold EXACTLY at that rung."
     " ### A CRITERION THAT RETURNED NOTHING IS NOT A CRITERION THAT SAID SOMETHING, and it is TABLED, NOT EDITED: a linear-space fit would fit these"
     " six numbers and would be A SECOND CRITERION chosen after seeing the first fail. ### b339\'S SIDE-READING IS NOT WITHDRAWN -- its own act labelled"
     " it a reading, and the evidence against it arrives exactly at the instrument\'s boundary. ### THE SEALED BRANCH RULE HAS NO SLOT FOR A FIT THAT"
     " DOES NOT EXIST, and that absence is filed and TABLED. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR"
     " MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b354_the_sixth_frame.txt; data/b354_sixth_run3.txt; data/b354_sixth.json;"
     " data/b354_sixth_run_first_nan_scores.txt (the run banked as it stood);"
     " data/b354_registration_2026-09-07.txt (sealed before the instrument ran);"
     " tools/anchor_from_file.py (the sortie\'s step zero); CORRESPONDENCE.md row 202"),
    # ### THE WIDTH COORDINATE'S MISSING STATEMENT (b353).
    ("width-missing-statement", "b353 (a read under the import bar and a pricing; it computes nothing)",
     "A STATEMENT EXISTS, AND IT DOES NOT CLOSE THE WIDTH COORDINATE. It is in the corpus\'s OWN source -- arXiv 2006.13771v1, Connes-Consani, Weil"
     " positivity and Trace formula the archimedean place, pinned at sha256 b8e0b54ade8535cf3ca633d1ef325bfc..., 1213504 bytes, graded"
     " TRUSTED-AT-CITE. ITS PROPOSITION 2, BOAS-KAC: for f in Cc^infty(R) supported in [-A, A], pointwise positivity of the Fourier transform is"
     " EQUIVALENT to f = g conv g-star for some g supported in [-A/2, A/2]. THAT IS STRONGER THAN THE DENSITY STATEMENT THE ORDER ASKED FOR -- it"
     " EXHAUSTS the admissible class rather than approximating it -- AND EVERY CONCLUSION IT GIVES IS AT THE SAME A IT WAS GIVEN, while the criterion"
     " it serves quantifies over the union of ALL supports. SO AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS. The hypotheses"
     " graded TWICE and never merged: against the source\'s class all four are MET; against the corpus\'s constructed objects H1 (smoothness) is"
     " REFUTABLE -- the record\'s own word for its test functions is PIECEWISE LINEAR -- H3 (pointwise positivity) is UNDECIDABLE FROM THE RECORD"
     " because the corpus\'s test is a scan and says so itself, and H4 (the vanishing conditions) is MET ONLY TO A MEASURED TOLERANCE. The missing"
     " statement is typed and is UNPRICEABLE from banked figures, because the work it names is a proof and not a run.",
     "### A LOCATED STATEMENT IS NOT A PROVED ONE, AND A CHECKED HYPOTHESIS IS NOT A DISCHARGED OBLIGATION. ### THE WIDTH COORDINATE IS NOT CLOSED BY"
     " THIS ACT, no class is proved or spanned, and the partition b351 left UNDECIDED STAYS UNDECIDED. ### H1 BEING REFUTABLE AGAINST THE ARRAYS IS"
     " NOT A FINDING THAT THE CORPUS\'S RESULTS ARE WRONG: it is a finding that the record does not say what its arrays are meant to be, and that"
     " question is routed and not answered. ### THE SEARCH IS NOT A SURVEY -- one source was read at content, and the absence of a crossing statement"
     " is AN ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ###"
     " NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b353_the_missing_statement.txt; data/b353_read_run.txt; data/b353_extract_notes.txt;"
     " data/b353_source.json (the pin and the search); data/b353_registration_2026-09-07.txt"
     " (sealed before one hypothesis was graded); CORRESPONDENCE.md row 201"),
    # ### THE FLOOR'S FOURTH CANDIDATE (b352).
    ("floor-fourth-candidate", "b352 (a refit of banked figures; nothing recomputed)",
     "THE IDENTITY RESIDUAL REFITTED UNDER THREE MODELS SEALED BEFORE ANY FIT -- M1 = A X^-p (k=2), M2 = A X^-p + c (k=3), M3 = A X^-p + B X^-(p+1) (k=3) --"
     " all by ONE criterion, least squares on log R, with M1 reproducing b322\'s own fit_power at every cell to 1e-9 (the fitter IMPORTED) so that the"
     " three scores are comparable. VERDICT: THE FLOOR IS UNDER-RESOLVED AS A FIT. The five frames DO separate a constant floor from a faster-decaying"
     " correction -- M2 beats M3 at every cell -- but M2 against M1 is preferred at a = 1.3 by less than the bar, decisively at a = 1.35, and REJECTED at"
     " a = 1.41 by 7.01. AND THE REASON IS THE CRITERION AND NOT THE DATA: at n = 5 a third parameter costs 20 AICc units against a bar of 2, so S must"
     " fall by a factor of 54.6 to break even and the winner turns on the penalty. The fitted constant is POSITIVE at all three cells and passes the"
     " second bar at all three, refuting the seat\'s registered expectation. THE PRICE OF SETTLING IT IS ONE MORE FRAME: the binding cell needs 6 where"
     " the record holds 5, the next rung is X = 256, N = 32768, AND THAT SITS INSIDE THE CEILING b339 SEALED AT X = 512 -- affordable where b339\'s own"
     " question was not. Component 3 filed the spectral void\'s width as the MEASURED 10.62 with b350 named, and minted the straddling-gate rule.",
     "### A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING: a fit ranks descriptions of five numbers and measures nothing. ### WHAT THIS ACT"
     " COULD NOT HAVE SEEN IS PRINTED PER CELL -- a true floor below the fit\'s own scatter at the last rung would pass no arm here. ### NO ACT IS"
     " RE-VERDICTED: b339\'s UNAFFORDABLE STANDS, b346 stands, b350 stands, b351\'s UNDECIDED stands. ### b339\'S SIDE-READING IS RESTATED AS FIT-DEPENDENT"
     " AND IS NOT WITHDRAWN -- its own act labelled it that seat\'s reading. ### THE FRAME PRICE IS A PRICE AND NOT A PREDICTION, and the act does not"
     " run it. ### NO CLASS IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b352_the_fourth_candidate.txt; data/b352_fit_run6.txt; data/b352_filings_run.txt;"
     " data/b352_registration_2026-09-07.txt (sealed before one model was fitted);"
     " PLACE-papers OPEN_TRAILS.md (the W-ORD-VOID-WIDTH block); TECHNE-Core STRADDLING_GATE.md (local-only);"
     " tools/registration_gate.py (the straddle arm, appended); CORRESPONDENCE.md row 200"),
    # ### THE PARTITION QUESTION (b351).
    ("aim-plane-coordinates", "b351 (a read under a ceiling; it computes nothing)",
     "THE AIM PLANE\'S COORDINATES READ FOR WHETHER THE RECORD CAN BOUND THEM, under the sealed distinction that A BOUND ON THE INSTRUMENT IS NOT A"
     " BOUND ON THE COORDINATE. THE ABSCISSA: BOUNDED BY AN ARGUMENT -- b326\'s summed bound SUM r_Q(k) k^(-3/2) = 1.38 < 2 confines every zero of"
     " Lambda_Q to (-0.5, 1.5), a statement about ALL zeros, banked since the completeness census and never cited for the aim plane. THE SEED\'S PHASE:"
     " BOUNDED BY AN ARGUMENT and finitely cut -- for an EVEN seed the quadruple\'s term is 4 G^2 cos(2 phi), the coordinate lives on a circle, and the"
     " sign cuts it at exactly 45 and 135 degrees; ONE class survives, the vanishing transform, which the sign condition cannot see. THE HEIGHT: BOUNDED"
     " ONLY BY A MEASUREMENT -- sixty boxes over t in [0.5, 150], the count closing at 180 against a main term of 178.6, and nothing claimed above it;"
     " AND ITS ONLY METHOD PRODUCES INSTANCES WHOSE COUNT THE MAIN TERM SAYS NEVER RUN OUT, so the price of 0.40134 boxes per unit of height"
     " (60 further boxes to T = 300, in boxes because the record printed no wall) BUYS INSTANCES WHILE THE MISSING STATEMENT NEEDS A CLASS. THE SEED\'S"
     " WIDTH: NOT BOUNDED, and worse off than the height -- the square and remainder are NOT REACHED at the charted widths, the remainder evaluator"
     " changes sign past rho = 100, and for Z_Q the record\'s own words are NOT AN INSTRUMENT THE RECORD HAS, so its missing statement is UNPRICEABLE"
     " from banked figures and its pricing unpriceable too. VERDICT: UNDECIDED, both other branches SHOWN UNREACHABLE.",
     "### UNDECIDED IS A STATEMENT ABOUT THE RECORD AND NOT ABOUT THE OBJECT: the aim plane may well admit a finite classification, and this act says"
     " only that the record contains neither one nor a proof that there is none. ### NO PARTITION WAS CONSTRUCTED, NO CLASS PROVED SILENT, NO INSTRUMENT"
     " WRITTEN, and nothing computed beyond one labelled division of two banked counts. ### A COORDINATE BEING BOUNDED IS NOT THE MARGIN BEING SAFE"
     " THERE, and no margin was measured at any aim. ### TWO CLOSED COORDINATES ARE NOT HALF A CLASSIFICATION, because a classification of a product is"
     " not two classifications of two factors. ### THE PHASE\'S FINITE CUT IS STATED FOR AN EVEN SEED, the condition b328 states it under. ### NO CLASS"
     " IS DISCHARGED. ### THE CLAUSE HAS NOT MOVED. ### NO GRADE MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b351_the_partition_question.txt; data/b351_read_run.txt; data/b351_extract_notes2.txt;"
     " data/b351_registration_2026-09-07.txt (sealed before one coordinate was judged);"
     " CORRESPONDENCE.md row 199"),
    # ### THE FLOOR'S TWO HELD AXES, PRICED (b350).
    ("held-axes-priced", "b350 (a pricing act; it moves nothing and measures nothing)",
     "THE FLOOR\'S TWO HELD AXES PRICED FROM b344\'S PRINTED FIGURES, with no frame built and nothing re-run. THE COST is the same for both --"
     " 89.35 seconds of wall per value tried, summed from the walls b344 printed over its sealed ladder -- because a move is a ladder either way, and"
     " what it buys is ONE value. THE ROOM is priceable for the threshold and not for the taper: the intersection across the rungs of (largest dropped,"
     " smallest kept) is (2.144048e-07, 2.277535e-06), a factor of 10.62 wide, with the corpus\'s own tau inside it, free to fall by 4.66 or rise"
     " by 2.28 with the same rank. The taper\'s constants are printed as constants with nothing beside them, so NO ROOM FOR IT IS PRICEABLE AT ALL, and"
     " the act prices the pricing instead: two ladders, 178.70 seconds, AND EVEN THAT WOULD GIVE A DIFFERENCE AND NOT A ROOM. WHAT EACH MOVE WOULD"
     " CONFOUND, in the sealed words of the act that declined it: the threshold confounds the RANK with the FLOOR; the taper confounds the INSTRUMENT with"
     " the OBJECT. VERDICT: THE FLOOR IS UNEXPLAINED. The trail W-ORD-FLOOR-HELD-AXES is RESTATED, NOT DISCHARGED.",
     "### PRICING IS NOT MEASURING, and a price is a statement about what an act would cost made by an act that does not perform it: no frame was built,"
     " no ladder run, no cell evaluated and NO AXIS MOVED. ### A RANK-PRESERVING BAND IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL -- the same"
     " subspace kept does not mean the same residual, and b344 printed no residual at a second threshold. ### THE FLOOR IS UNEXPLAINED: the one axis moved"
     " does not account for it and for the two held axes the record contains NO measurement of the residual at all. ### THE TRAIL IS RESTATED, NOT"
     " DISCHARGED -- its price half is paid and its measurement half is not, and A TRAIL IS NOT DISCHARGED BY PAYING THE CHEAPER HALF OF IT. ### NO GRADE"
     " MOVED. ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b350_the_two_held_axes.txt; data/b350_price_run.txt; data/b350_filings_run.txt;"
     " data/b350_registration_2026-09-07.txt (sealed before one price was computed);"
     " PLACE-papers OPEN_TRAILS.md (the b350 block); CORRESPONDENCE.md row 198"),
    # ### THE ROOM, RELATIVE BEFORE EXTENDED (b349).
    ("room-relative", "b349 (a second measure of banked figures, then three new heights)",
     "THE ROOM MEASURED RELATIVE TO THE TERMS IT SITS BETWEEN, the denominator fixed before any value as the LARGER of the two terms so the ratio cannot be"
     " inflated by a small one. On the 54 aims already charted, reading and running no seed: THE MINIMUM SURVIVES AT BOTH WIDTHS -- absolute and relative"
     " minima both at gamma = 2.5 at a = 40, and both at gamma = 1.25 at a = 81 -- SO THE LOCATED POINT OF MAXIMUM TENSION IS NOT AN ARTIFACT OF ABSOLUTE"
     " MEASUREMENT. And the relative measure IS FLATTER at both widths (8028 against 4336 at a = 40; 23707 against 20395 at a = 81),"
     " so the navigator\'s expectation is half met and half refuted and the halves point opposite ways. PART (b) THEREFORE RAN: three sealed heights at"
     " a = 81, every seed checked for lawfulness by the source\'s Definition 3.1 AND for its phase inside b328\'s WINDOW of 45 to 135 degrees --"
     " ALL THREE LAWFUL, ALL THREE IN THE WINDOW, NONE DEGENERATE. NO CROSSING on the extended grid, and the minimum stays at gamma = 1.25, INTERIOR IN"
     " BOTH MEASURES. The sortie\'s step zero also built tools/quote_norm.py, one normaliser imported by both sides of every quotation comparison, over"
     " the species banked at b298, b309 and b348.",
     "### ONE MEASURE AGREEING WITH ANOTHER IS WEAKER THAN EITHER BEING RIGHT, and the relative measure is a DIFFERENT measure and not a better one."
     " ### NO CROSSING IS CLAIMED AT ANY HEIGHT. ### A NARROWER ROOM AT A LOWER HEIGHT IS A LOWER HEIGHT AND NOT A TREND: below gamma = 1 the room moves"
     " very little across three heights while the dip at 1.25 sits an order of magnitude under all of them, a local feature and not a descent. ### THREE"
     " LAWFUL SEEDS MEAN THESE THREE DID NOT DEGENERATE; THEY DO NOT MEAN THE CONSTRUCTION NEVER DOES. ### THE SQUARE AND THE REMAINDER ARE NOT REACHED"
     " AT THIS WIDTH. ### THE ORDER NAMED A b305 INCIDENT THIS SEAT COULD NOT LOCATE AND NONE WAS MANUFACTURED. ### NO GRADE MOVED. ### NO BAR MOVED."
     " ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b349_the_room_relative.txt; data/b349_relative_run.txt; data/b349_extend_run.txt;"
     " data/b349_registration_2026-09-07.txt (sealed before one relative value was computed and before any new seed);"
     " tools/quote_norm.py (the sortie\'s shared normaliser); CORRESPONDENCE.md row 197"),
    # ### THE PRICED-AND-RESOLVED ARC, b339-b347 -- THE FOLD (b348).
    ("priced-and-resolved-fold", "b348 (a filings act; it proves nothing and moves no grade)",
     "THE FOLD OF b339-b347: nine acts filed as one section of the findings document, PURELY ADDITIVE, with every quotation located at the act that ORIGINATED"
     " it and -- new in this fold -- THE NO-GRADE-MOVED CLAIM ITSELF MECHANICAL: every grade string had to appear verbatim in the bank of the act it is"
     " attributed to, or the section would not have been written. Quotations failing 0; grade anchors failing 0; 135 lines added, nothing"
     " edited. Three further tables from the acts\' own declarations: 3 corrections the acts made to their OWN readings, 3 sealed bars found"
     " defective and tabled rather than edited into passing, 2 defects the seats declared on their own faces. THE ARC AS ONE STATEMENT: a question"
     " priced UNAFFORDABLE by value on one axis was RESOLVED on another the record already held; the deposit\'s Li channel and the derived kernel are ONE"
     " DISTRIBUTION ON TWO FAMILIES, measured; the archimedean instrument has a floor the one axis moved does not explain; the room\'s minimum is BRACKETED at"
     " the lowest height charted; the clause\'s constituents stand as the stated-clause anchor has them. ONE SPECIES MINTED: a scanner over prose cannot tell"
     " use from mention -- a sentence denying a thing contains the thing -- five incidents at b316, b317, b345, b346 and b347\'s own arm which found its own"
     " search string. THE CENSUS AS A FINDING: 333 registrations gated, 52 would fire, 281 clear, 276 of those carrying nothing for an arm to look at.",
     "### A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES: it proves nothing, discharges nothing, and MOVES NO GRADE -- and in this fold that is CHECKED"
     " rather than asserted. ### THE RATE AXIS RESOLVES THE TWO CONVENTIONS AND DOES NOT MAKE A CONVENTION CORRECT; b313\'s clause governs and a rate is not a"
     " vote on it. ### THE FLOOR IS NOT EXPLAINED -- one axis of three was moved and the other two are named, not moved. ### W-ORD-LI-FAMILY-CONTROL STAYS"
     " OWED: the zero side and the finite side are not evaluated. ### THE CENSUS IS A MEASUREMENT OF THE RECORD AND NOT A GRADE ON IT, and the gate it reports"
     " is PROSPECTIVE -- the record\'s quiet is mostly the absence of stated numerical bars, not bars checked and approved. ### THE MINTED SPECIES IS A"
     " JUDGEMENT RULE, NOT MECHANIZED, and is deliberately NOT LISTED BESIDE THE MECHANIZED ONES; what would mechanize it is named and not built. ### THE"
     " FAILURE-MODE PARTITION IS NAMED AS A RESEARCH PROPOSAL AND NOT OPENED, AND NO SUCH PARTITION IS KNOWN TO EXIST. ### K8 UNOWNED. ### NO GRADE MOVED."
     " ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b348_the_fold.txt; data/b348_fold_run.txt; data/b348_fold_emitted.md;"
     " data/b348_registration_2026-09-07.txt (sealed before any line was emitted into the findings document);"
     " PLACE-papers FINDINGS.md (the appended section); TECHNE-Core modules/2026-09/USE_AND_MENTION.md (local, NOT PUSHED);"
     " CORRESPONDENCE.md row 196"),
    # ### THE THREE REPAIRS AND THE TWO RULES (b347).
    ("bar-floor-rule", "b347 (an instrument act; it decides nothing about the mathematics)",
     "THE BAR-FLOOR RULE, MINTED OVER BOTH SPECIES: a numerical bar is stated with the floor of the object it tests, and a bar below that floor is"
     " UNINFORMATIVE RATHER THAN STRICT; and a bar with several arms is stated with what makes the arms independent, since arms that are algebraically one"
     " arm are one arm. It is b322\'s resolving-power rule one level down. Minted from two banked incidents: b345 sealed a fixture demanding 1e-25 of a"
     " routine whose truncation left it a floor near 4.4e-18, so at its own threshold it rejected the correct copy too; b346 sealed an uncertainty whose"
     " second estimator was algebraically its first, so one arm sat at machine level and another was structurally zero. Mechanized as two arms in"
     " registration_gate.py beside the index-query arm, six fixtures in both polarities; the census over 333 registrations found 52 that would fire and"
     " 281 clear, of which 276 carry nothing for the arms to look at. AND THE ACT DID NOT EXEMPT ITSELF: its own sealed registration fires on one arm and"
     " carries it. THE OTHER TWO REPAIRS: run_clock.py gives a run file the instant it was written -- 370 run files in the record carried none before it;"
     " and gate_text.py repairs the flattener in one place, its reach measured statically at 1 arm and reported as a LOWER BOUND. The satisfiability"
     " audit\'s numerical limit is named in its own output and PRICED at 20 registrations of hand reading. FERRY_STANDING v2 written by its generator,"
     " counts re-measured live, the act-number clause in its own section marked AUTHOR-RULED, NOT MEASURED.",
     "### A SHARPER INSTRUMENT IS NOT A RESULT, and nothing in this act decides anything about the mathematics: no frame built, no cell evaluated, no"
     " object measured. ### THE CLOCK DOES NOT REACH BACKWARDS -- every run file written before it carries none and cannot be given one, and b345\'s (E4)"
     " stands exactly as b345 declared it. ### THE AUDIT\'S NUMERICAL LIMIT IS NAMED AND PRICED, NOT CLOSED; no numerical checker is built. ### THE GATE"
     " MATCHES TEXT and cannot tell a floor from the words of one -- a registration that writes UNPRICED beside every bar passes and has priced nothing."
     " ### NO PAST ACT IS RE-VERDICTED, no past copy of the flattener is edited, and no registration the new arms would fire on is touched. ### THE SCAN"
     " WAS NOT TAUGHT THE ACT-NUMBER CLAUSE, so it binds a reader and not a tool. ### THE MODULES ARE PRIVATE AND NOT PUSHED. ### NO GRADE MOVED."
     " ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b347_the_three_repairs.txt; data/b347_repairs_run.txt (the first run file in the corpus carrying its own clock);"
     " data/b347_registration_2026-09-06.txt (sealed before any tool was touched and before any module was written);"
     " data/b347_order_2026-09-06.txt; tools/run_clock.py; tools/gate_text.py; tools/registration_gate.py (the two arms);"
     " tools/FERRY_STANDING.md (v2); TECHNE-Core modules/2026-09/BAR_FLOOR_RULE.md and TWO_ROUTES.md (local, NOT PUSHED);"
     " CORRESPONDENCE.md row 195"),
    # ### THE EXPONENT BY RATE (b346).
    ("exponent-by-rate", "b346 (a premise tested, then a different axis measured)",
     "THE EXPONENT BY RATE: b339 priced the split between the exponent\'s two candidates BY VALUE and banked it UNAFFORDABLE, with a side reading"
     " that the residual descends to a FLOOR. b346 TESTED that premise rather than assuming it: b339\'s own sealed limit arithmetic puts the fitted"
     " limit ABOVE BOTH candidates at every covered cell, and b344\'s ladder converges in NY with the whole remaining travel from the corpus\'s own"
     " NY = 512 equal to 0.1105 of b339\'s floor there. A FLOOR IS PRESENT, SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE. Then a different axis:"
     " the even sector\'s decay along the ARGUMENT, where b315 measured the rate moving a full power while along the cutoff it does not move at all."
     " The two conventions came from b313\'s copy-maker unedited, on the 6 cells b264\'s own second axis marked converged; their ratio is the"
     " argument itself at every cell, so THE SEPARATION IN THE EXPONENT IS EXACTLY 1.0 AND IS EXACT BY CONSTRUCTION, NOT MEASURED. What was measured is"
     " the instrument\'s uncertainty in the rate, 1.571945e-02, a resolving power of 63.6, the noise-floor gate RESOLVED at both conventions."
     " VERDICT: RESOLVED ON THIS AXIS. The local slope at the top of the converged window is -1.490930810, sitting 9.069e-03 from the corpus\'s"
     " asymptote and 9.909e-01 from the source\'s: THE BANKED VALUES CARRY THE CORPUS\'S OWN r ** -0.5, read from the values and from nothing else."
     " The standing clause of E-2026-09-03-1 therefore acquires a MECHANICAL TEST, appended to ERRATA.md under a b346 mark with the entry byte-identical.",
     "### A RESOLVING POWER IS A PROPERTY OF THE INSTRUMENT: it says the axis can tell two objects apart, and nothing about which of them the mathematics"
     " requires. ### NO CONVENTION IS DECLARED CORRECT. b312 decided which function the corpus\'s remainder is BY UNFOLDING DEFINITIONS, and b313\'s clause"
     " governs: the exponent is fixed by the source\'s own definition of the object the corpus imported, and a rate is not a vote on that any more than"
     " a residue was. ### THE FLOOR IS NOT EXPLAINED: one of its three named origins has been priced and the cut\'s tau and the taper are named, not moved."
     " ### THE TWO EVALUATORS SHARE AN ENGINE -- the prolate layer and the node counts, which b313\'s copy-maker declares deliberately -- so independence"
     " of the prolate solver is NOT certified. ### AND ONE OF THIS ACT\'S OWN SEALED UNCERTAINTY ARMS COLLAPSED: a two-point drift-zero is algebraically"
     " the local slope of those two points, so the second estimator became the first and (u2) was structurally zero; TABLED AND NOT REPAIRED, the sealed"
     " file unedited, the understatement bounded by a labelled whole-window diagnostic giving a resolving power of 6.2. ### NO GRADE MOVED."
     " ### NO BAR MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b346_the_exponent_by_rate.txt; data/b346_rate_run.txt; data/b346_filings_run.txt;"
     " data/b346_registration_2026-09-06.txt (sealed before one slope was fitted and before the flipped copy was run once);"
     " data/b346_ruling_2026-09-06.txt (this act\'s number and the author\'s framing note); PLACE-papers ERRATA.md (the b346 block against E-2026-09-03-1);"
     " CORRESPONDENCE.md row 194"),
    # ### THE LI CONTROL, RE-RUN (b345).
    ("li-control-rerun", "b345 (a control re-run under a new bar with the tail rule fixed first)",
     "THE LI CONTROL RE-RUN: b340 asked two things of every index -- the identity, and the drift between two sealed quadratures. The identity held;"
     " the drift did not, because the sealed refinement route put Gauss-Legendre on an infinite panel with a logarithmic tail. b345 registered ITS OWN"
     " bar with the tail rule FIXED BEFORE ANY VALUE as TANH-SINH -- the rule b340\'s own diagnosis named -- and required its two routes to share no"
     " code: route A is b340\'s theta route imported unedited, route B is fresh in the u variable with the transform factor as the complex power"
     " Re[1 - ((s-1)/s)^n] and a HAND-ROLLED digamma. VERDICT, BY THE SEALED RULE: A FOURTH CONTROL HOLDS at 22 of 22 tabulated indices --"
     " worst identity miss 7.47e-26 against 1e-9 max(1, |lambda_A|), worst drift between routes 1.27e-17, every index RESOLVED,"
     " the pole constant L_n[log s] its own column and equal to 1 to 1.42e-39. AND ONE SEALED FIXTURE FAILED AT ITS OWN THRESHOLD: section (C)"
     " sealed a recurrence to |w| >= 20 with Stirling through B_10 AND a fixture threshold of 1.0e-25 in the same paragraph; the"
     " truncation\'s first dropped term leaves a floor near 4.394e-18, so at 1.0e-25 the fixture rejects the CORRECT copy too and separates"
     " nothing. Carrying only the recurrence to |w| >= 300 brings the same routine to 3.929e-32, which locates the defect in one named half.",
     "### A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### THE LI FAMILY IS NOT IN THE LAWFUL CLASS -- three of three of Theorem 1\'s"
     " conditions fail -- so Theorem 1\'s inequality and the Sonin margin DO NOT APPLY, and the Sonin margin is not defined on this family at all."
     " ### b340\'s BAR IS NOT REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED: a re-run under a new bar is a new measurement, not a correction."
     " ### THE ZERO SIDE AND THE FINITE SIDE ARE NOT EVALUATED, SO W-ORD-LI-FAMILY-CONTROL STAYS OWED and is paid at its archimedean constituent"
     " only. ### THE DEPOSIT\'S FINITE-RANGE POSITIVITY IS THE DEPOSIT\'S, restated at its scope; positivity in a finite range is not evidence of the"
     " kind the criterion respects. ### THE FAILED FIXTURE IS TABLED, NOT REPAIRED INTO PASSING, AND CONFERS NOTHING. ### NO GRADE MOVED."
     " ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b345_the_li_control_rerun.txt; data/b345_control_run.txt; data/b345_filings_run.txt;"
     " data/b345_registration_2026-09-06.txt (sealed before the tail panel was integrated once and before the second route was written);"
     " data/b345_control_draft_unsealed_params_stopped.txt (a draft at parameters this act did not seal, stopped, no value used);"
     " PLACE-papers FACES_LEDGER.md (row L1 update block) and OPEN_TRAILS.md (W-ORD-FLOOR-HELD-AXES);"
     " CORRESPONDENCE.md row 193"),
    # ### THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE (b344).
    ("floor-priced", "b344 (one axis of three moved; a tool repair; a chart extended)",
     "THE FLOOR PRICED ON ONE AXIS: of the three origins b339 named for the identity residual's floor -- the fixed NY, the cut's tau, the taper -- NY was"
     " moved over the ladder [128, 256, 512, 1024, 2048] at the reference frame, the other two HELD AND PRINTED at every rung. The stable-cut rank is CONSTANT at"
     " 69 across the whole ladder, so NY does not move the rank. The residual MOVES with NY: the span across the ladder is 1.239e-02 against"
     " b339's floor of +0.006389645 at that cell, so by the sealed rule the movement is OF THE SIZE THE FLOOR REQUIRES. Beside the verdict and labelled: the increments fall"
     " by a factor near four, so the residual converges in NY, and from the corpus's own NY = 512 the remaining travel is about a ninth of the floor."
     " THE SEAL'S OWN CLOCK: reg_seal.py repaired by the order's words to record the seal's UTC instant inside the block, additions-only, with all"
     " 66 existing seals verifying identically before and after and none rewritten; filed as modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md,"
     " committed locally at 023a7bb, the remote unmoved, NOT PUSHED. THE ROOM'S EDGE: the grid extended below b343's edge at a = 81 only --"
     " BRACKETED, the minimum interior at gamma = 1.25, room +0.000026234, no crossing on the seventeen-height grid.",
     "### ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO AXES HELD, AND THE FLOOR IS NOT EXPLAINED. ### A REPAIRED SEAL TOOL"
     " CERTIFIES NOTHING ABOUT THE ACTS SEALED BEFORE IT, AND IT DOES NOT RECOVER b342's LOST TIMESTAMP. ### THE CLOCK IS OUTSIDE THE HASH AND SAYS SO."
     " ### A NARROWER ROOM AT A FINER GRID IS A FINER CHART AND NOT A TREND. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b344_the_floor_priced.txt; data/b344_ny_run.txt; data/b344_edge_run.txt; data/b344_seal_after_run.txt; data/b344_module_run.txt;"
     " data/b344_registration_2026-09-06.txt (sealed before any rung, before the tool was touched, and before any seed below the edge);"
     " data/b344_ruling_2026-09-06.txt (this act's number); TECHNE-Core modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md (local);"
     " CORRESPONDENCE.md row 192"),
    # ### THE MAP'S NEXT REACH (b343, leg 5 of the sortie b339-b343).
    ("map-next-reach", "b343 (a chart at a finer grid, and a measurement of the instrument at three frames)",
     "THE MAP'S NEXT REACH: the aim-map's quantities at thirteen heights from gamma = 2.0 to 8.0 in half-unit steps, at both reaching widths a = 40 and"
     " a = 81, by b334's own code imported and not edited, the noise-floor gate on every sign -- NO CROSSING at a = 40 ; NO CROSSING at a = 81 (a = 40.0 narrowest at gamma = 2.50, +0.000083595 ; a = 81.0 narrowest at gamma = 2.00, +0.000090027);"
     " the two heights shared with b334's coarse grid reproduce its banked values to 0.000e+00. AND THE IDENTITY RESIDUAL AT ONE AIMED SEED"
     " (a = 1.41, gamma = 33.650101) across the reference frame and the two larger grid-axis frames, N = [4096, 8192, 16384] at fixed X = 32 and NY = 512,"
     " the remainder under both conventions each named: the stable-cut rank constant at 69, and the residual changed across the doublings and NOTHING is concluded about b339's floor.",
     "### A FINER CHART IS A FINER CHART. ### THE REACHING WIDTHS ARE OUTSIDE THE SQUARE'S AND THE EPS EVALUATOR'S REACH, AND NEITHER WAS EVALUATED"
     " THERE. ### THE DRAFT'S EXPECTATION THAT THE RESIDUAL GROWS WITH RANK CANNOT BE SCORED ON THE AXIS IT NAMES, WHICH HOLDS THE RANK FIXED."
     " ### NO GRADE MOVED; K6 STAYS MEASURED-AT-COVERED-CELLS. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b343_the_maps_next_reach.txt; data/b343_fine_40_run.txt; data/b343_fine_81_run.txt; data/b343_crossing_run.txt; data/b343_frames_run.txt;"
     " data/b343_registration_2026-09-06.txt (sealed before any seed at a new height); FACES_LEDGER.md (the b343 update, row S1/K6);"
     " CORRESPONDENCE.md row 191"),
    # ### THE TWO RULES AS MODULES (b342, leg 4 of the sortie b339-b343).
    ("two-rules-modules", "b342 (a filings act: two method modules, private, local, NOT PUSHED; a re-typing block)",
     "THE TWO RULES AS TECHNE MODULES, as the executor's draft states them: LIKE_FOR_LIKE.md (a comparator is named with the function it was"
     " computed for; a bar sealed against a banked table names the table's function; a mismatch is refused -- b333's incident, b334's comparator)"
     " and SIGN_RULE.md (a threshold rule is stated with its sign condition; a phase past the threshold is not a negative term -- b334's hundred"
     " positive-term aims), the sign-rule module carrying the b328 refinement (S_4 negative exactly between 45 and 135 degrees; b336's addendum);"
     " the index appended by one block; every existing module byte-identical; committed locally at 43ef56a, the remote at 22739c9 before and"
     " after, NOT PUSHED. FINDINGS gains one appended block re-typing the two lore lines from TOOL to MODULE, the fold's lines untouched.",
     "### THE MODULES BIND NOTHING; THEY STATE THE GRADE THEIR OWNING ACTS CARRY AND CONFER NONE. ### PRIVATE, LOCAL, NOT PUSHED. ### THE FOLD'S"
     " LINES UNTOUCHED. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b342_the_two_rules_as_modules.txt; data/b342_modules_run.txt; data/b342_lore_run.txt; data/b342_executor_draft_2026-09-06.txt;"
     " data/b342_registration_2026-09-06.txt (sealed before any write, with its post-seal marking); TECHNE-Core modules/2026-09/LIKE_FOR_LIKE.md,"
     " SIGN_RULE.md, modules/INDEX.md (local); FINDINGS.md (the b342 addendum); CORRESPONDENCE.md row 190"),
    # ### THE TWO COEFFICIENTS (b341, leg 3 of the sortie b339-b343).
    ("two-coefficients", "b341 (a transcription filed: two routes, the literature under the import bar, an internal-record erratum)",
     "THE TWO COEFFICIENTS: THE BENCH CARRIES THE DEFECT at n = [3, 5] -- the bench's KEIPER dictionary reads 0.2077580993 and 0.5747345 at n = 3, 5 where two routes"
     " sharing no quadrature (the bench's own definitions; the Li map of log xi by Taylor differentiation) give 0.20763892055432 and 0.57554271446117"
     " (off by 0.000119 and 0.000808); the balance keystone's literature column agrees with the routes to its printed digits; Keiper 1992"
     " LOCATED under the import bar at n = 3 and agreeing with the keystone (his lambda_n / n), readings beside the rule at n = 5 (Keiper's split mantissa;"
     " Coffey's six decimals) agreeing too; no located source agrees with the dictionary. Filed as E-2026-09-06-1, INTERNAL RECORD, appended after the"
     " partition block; the owner files untouched; the navigator's (L3) MET.",
     "### NO BENCH MEASUREMENT CHANGES (the dictionary enters no computation). ### NO DEPOSITED ARTIFACT IS AFFECTED. ### NO OWNER FILE IS EDITED."
     " ### THE DICTIONARY'S NAME IS NOT ITS PROVENANCE. ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b341_the_two_coefficients.txt; data/b341_coefficients_run2.txt; data/b341_locate_run3.txt; data/b341_source_text_*.txt; data/b341_registration_2026-09-06.txt"
     " (sealed before any fetch); ERRATA.md (E-2026-09-06-1); CORRESPONDENCE.md row 189"),
    # ### THE LI FAMILY CONTROL (b340, leg 2 of the sortie b339-b343).
    ("li-family-control", "b340 (a control at one constituent, on a family outside the lawful class)",
     "THE LI FAMILY CONTROL: the Li test functions built from the pinned source's (3.2) in the corpus's half-line normalization, NOT in the lawful"
     " class (three of three of Theorem 1's conditions failing, the applicable and inapplicable certifications stated); the archimedean distribution on"
     " them by the derived kernel, I(n) = (1/2pi) INT Re G_n(1/2+iu) h_+(u) du, two quadratures gated by the noise floor, at the balance keystone's"
     " indices, against the deposit's channel lambda_A(n) by the bench's own definitions with the pole constant carried as its own column and b327's"
     " identity lambda_A = S_inf + 1 as the bar; worst |I + 1 - lambda_A| = 7.47e-26, worst drift 0.0115. THE DIFFERING CONSTITUENT: the bar fails at 22 of 22 tabulated indices."
     " The finite-range positivity restated at its scope beside the values (the certificate the deposit's, its premises open).",
     "### A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT. ### THE LI FAMILY IS NOT IN THE LAWFUL CLASS; THE SONIN MARGIN IS NOT DEFINED ON IT."
     " ### THE ZERO SIDE AND THE FINITE SIDE STAY OWED (W-ORD-LI-FAMILY-CONTROL). ### NO GRADE MOVED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b340_the_li_family_control.txt; data/b340_control_run*.txt; data/b340_control.json; data/b340_registration_2026-09-06.txt (sealed before the"
     " instrument); FACES_LEDGER.md (the b340 update, row L1 and the pair F1-L1); CORRESPONDENCE.md row 188"),
    # ### THE EXPONENT PRICED (b339, leg 1 of the sortie b339-b343).
    ("exponent-resolved", "b339 (a pricing act under b322's sealed rule; no frame built)",
     "THE EXPONENT PRICED: the domain the remainder instrument needs to split the two exponent candidates (rho ** +0.5, the source's; rho ** -0.5,"
     " the corpus's) priced at every covered cell from b320's domain ladder and b321's separation -- the identity residual fitted by b322's fit_power,"
     " the split criterion R <= s/2, the price X_req = 128 (R(128)/(s/2))^(1/p) -- against a ceiling X = 512 sealed before the price: a = 1.3: X_req 2358 (ratio 18.42); a = 1.35: X_req 1451 (ratio 11.33); a = 1.41: X_req 812 (ratio 6.34)."
     " UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED; NO FRAME BUILT; NO REMAINDER EVALUATED AT A NEW DOMAIN. The side"
     " reading on the same five frames puts the margin's limit above both candidates at every cell, so the price is an under-estimate and the floor is"
     " what the next pricing must price.",
     "### A PRICE IS NOT A PREDICTION. ### NO CANDIDATE PREFERRED. ### THE QUESTION STAYS UNDER-RESOLVED, NOT OPEN, BY b322's RULE. ### NO BAR MOVED."
     " ### THE ERRATUM E-2026-09-03-1 UNTOUCHED. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b339_the_exponent_resolved.txt; data/b339_price_run.txt; data/b339_price.json; data/b339_limit_run.txt; data/b339_registration_2026-09-06.txt"
     " (sealed before the price); FACES_LEDGER.md (the b339 update, rows F2 and S1/K6); CORRESPONDENCE.md row 187"),
    # ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD (b338, leg 3 of the sortie b335-b338).
    ("stated-clause-arc-fold", "b338 (a filings act: the fold of four acts, purely additive)",
     "THE FOLD, b331 THROUGH b334: one section appended to FINDINGS.md (+114 lines, 3116 -> 3230) by a committed generator --"
     " F-QUOTE at every quotation against the originating act, F-COUNT the arc exactly, F-MODULES every rule by module or by tool on disk, the"
     " working file and the blob true prefixes of the result; four results at their own grades (b331 FILED; b332 STATED; b333 DERIVES-ON-IMPORTS"
     " for K5, MEASURED-ON-FAMILIES not conferred; b334 MEASURED on a grid at this reach), four obstacles, four corrections, three sealed bars"
     " found defective and tabled, the lore typed MODULE / TOOL / JUDGEMENT, the suite this arc added; THE DESK'S FIRST ITEM the wave's"
     " candidate list restated (b324's six, b331's addition, this arc's typed candidates) with the housekeeping's state as b337 stated it"
     " beside it. THE ARC AS ONE STATEMENT: the clause stated whole and not discharged; its softest constituent derived under the import bar;"
     " the room charted over aims; the clause not moved.",
     "### A FILING, NOT A RESULT; THE ONE STATEMENT A SUMMARY AND NOT A VERDICT. ### THE WAVE IS THE AUTHOR'S; THE LIST IS TYPED, NOT RANKED."
     " ### NO GRADE MOVED. ### A CHART IS NOT A PROOF. ### NO TERMINAL. ### M-2 UNCHANGED",
     "data/b338_the_fold.txt; data/b338_fold_run.txt; data/b338_fold_emitted.md; data/b338_fold_rows.json; data/b338_registration_2026-09-06.txt"
     " (sealed before the generator); FINDINGS.md (THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD); CORRESPONDENCE.md rows 185 and 186"),
    # ### THE WAVE'S HOUSEKEEPING (b337, leg 2 of the sortie b335-b338).
    ("housekeeping", "b337 (housekeeping: filings and checks; no claim, no grade, no deposit action)",
     "THE THREE LEDGERS (ERRATA.md, VERIFICATION_LOOM.md, OPEN_TRAILS.md) RECONCILED TO REGISTRY AGAINST ONE READ-ONLY FETCH of the public record"
     " (v1.1.2, published 2026-07-24, DOI 10.5281/zenodo.21539167, 11 files): REGISTRY's d1-1 row agrees on every field, the local canonical copy matches the"
     " published MD5s at 11 of 11; the loom and the trails CURRENT; ERRATA's head (v1.1.1 as current) DRIFT, repaired by an APPENDED currency"
     " note, the head not edited. THE ERRATA PARTITION per the author's ruling ratified by the sortie paste: one appended block, five entries"
     " DEPOSIT-FACING and five INTERNAL-RECORD by their own words, entries unmoved. THE NINE AUGUST TECHNE MODULE FILES committed at 4c0a6af in the"
     " canonical local clone by explicit list, the remote unchanged, NOT PUSHED. THE PATENT RECEIPTS: ABSENT ON THE MOUNTED VOLUMES (C, D) for"
     " both applications; F: not mounted this session; the four office notices and the 2026-08-30 response packages present; the repo of record"
     " has no remote.",
     "### NO DEPOSIT ACTION; NOTHING WAS WRITTEN AT ZENODO. ### NO ENTRY MOVED OR EDITED. ### TECHNE NOT PUSHED. ### NOTHING IS CONCLUDED ABOUT WHETHER"
     " A REPLY WAS FILED. ### NO GRADE, NO CLAIM, NO TERMINAL. ### M-2 UNCHANGED",
     "data/b337_the_housekeeping.txt; data/b337_fetch_run.txt; data/b337_record.json; data/b337_errata_run.txt; data/b337_techne_run.txt;"
     " data/b337_receipts_run.txt; data/b337_registration_2026-09-06.txt (sealed before any tool); PLACE-papers ERRATA.md (the b337 partition block);"
     " TECHNE-Core local commit 4c0a6af; CORRESPONDENCE.md row 184"),
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
