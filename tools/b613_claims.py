# -*- coding: utf-8 -*-
"""b613_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R223)(3): THE CLAIMS OF CLUSTER 2B'S SIX PAPERS.

### Every claim is the seat's one-sentence restatement of a paper's sentence, carried with a needle that must occur on the cited line of the
### paper at PLACE-papers a4f16fe; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, confirmed by (R222)(1): kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. A ROUTE is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the
### sieve's five tests in order. A pin RESOLVES, by the rule (R223)(1) confirms, when its commit is in the clone and at the remote.
### TECHNE content the papers cite is carried by pointer alone: the library's name and the sha256 of its tracked-file manifest, never a
### sentence of its body. This module writes nothing: `python tools/b613_claims.py` runs the resolvers and prints.
"""
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
PRE_PP = 'a4f16fe'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAPERS = {
    'SE': ('phase2/philosophy/SILENCE_EMERGENCE.md', 'p2-2', 248),
    'DI': ('phase2/philosophy/DARK_INTERFACE.md', 'p2-24', 249),
    'CG': ('phase2/philosophy/COGNITION.md', 'p2-14', 250),
    'UC': ('phase2/philosophy/UNIFIED_COGNITIVE.md', 'p2-21', 251),
    'IS': ('phase2/method/IDENTITY_SUBSPACE.md', 'p2-22', 252),
    'ID': ('phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 'p2-28', 253),
}
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel pins the papers name, each as cited: key -> (repo, the pin as cited, what the paper names there)
CITED_PINS = {
    'silence': ('SIDE-silence-principle', 'v0.1', 'the Silence Principle, no terminal named (ID :25, :245, :249, :327)'),
    'meta': ('SIDE-meta', 'v0.3', 'a parametric SIDESystem template and a κ predicate, no terminal named (ID :251, :331)'),
}
# ### a terminal named without a pin, read for the record where it stands (not a certifying read)
UNPINNED = {'silence_universal': ('SIDE-kernel', 'main', 'Kernel/SilenceTheorem.lean', 74, 'theorem silence_universal')}

T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
R1 = ('R1', 'DARK', 2, T2, 'the classes’ exclusions, as the sieve reads them, are conditions on a real σ naming no function, so they hold beside the '
                           'Epstein configuration the detector meets at ρ_E', 'RH-60')
R2 = ('R2', 'NOT A ROUTE', None, '—', 'the paper’s own correction of 2026-08-10: the derivations identify the line, sharing one involution, and carry '
                                     'no placement', None)

C = [
    # ---------------------------------------------------------------- SILENCE_EMERGENCE (p2-2)
    ('SE-01', 'SE', 13, 'We call this the Silence Principle', 'SE states a four-step theorem for determined systems with independent structures, '
     'essential interfaces being universal and universal ones silent about behavioral parameters, and names it the Silence Principle.',
     'argument-supported', 'argument', 'the four steps at :81-:86', None),
    ('SE-02', 'SE', 25, 'This has been proved formally in Lean 4 with zero unproved assertions', 'SE states that the product formula builds ξ '
     'without encoding where its zeros sit, and that this is formalized in Lean 4.', 'argument-supported', 'argument', 'the spectral '
     'parameter’s absence from |x|_A = 1 argued at :25; the formalization cited to a preprint, no terminal or pin named', None),
    ('SE-03', 'SE', 29, 'the conservation rank for amino acid identity is κ = 0.94', 'SE reports κ = 0.94 for amino-acid identity under the genetic '
     'code and κ = 0.08 for codon frequency across species.', 'statement-grade', 'statement', 'values given in the paper’s κ terms for cited '
     'literature (:29, :31), no computation shown', None),
    ('SE-04', 'SE', 79, '**Theorem.** Let X be a determined system', 'SE states that if an essential interface is universal, every behavioral '
     'parameter that varies across configurations has κ(P, I) = 0.', 'argument-supported', 'argument', 'the four-step argument at :81-:86', None),
    ('SE-05', 'SE', 92, 'This is close to tautological', 'SE states that its load-bearing step is that what works for all works the same for all, '
     'and calls the step close to tautological.', 'statement-grade', 'statement', 'the paper’s own reading of its step at :92', None),
    ('SE-06', 'SE', 96, 'The principle applies to *coupled* systems', 'SE limits the principle to coupled systems with independent structures '
     'joined by an essential universal interface.', 'statement-grade', 'statement', 'the scope at :96-:104', None),
    ('SE-07', 'SE', 112, 'Reductionism fails not because the system is too complex', 'SE reads the failure of reductionism at scale transitions as '
     'due to the universality of fundamental laws, not to complexity.', 'synthesis-suggested', 'reading', 'a reading at :112-:116', None),
    ('SE-08', 'SE', 120, "Fodor's autonomy is the Silence Principle applied", 'SE reads Fodor’s autonomy of the special sciences as the principle '
     'applied to inter-theoretic interfaces.', 'synthesis-suggested', 'reading', 'a reading at :118-:122', None),
    ('SE-09', 'SE', 147, 'The hard problem is hard because the interface that produces consciousness is essential and universal', 'SE reads the hard '
     'problem of consciousness as a consequence of the principle, given an essential and universal neural-experiential interface.',
     'argument-supported', 'argument', 'premises at :134-:138; the universality of the interface assumed at :143', None),
    ('SE-10', 'SE', 163, '**Not eliminativism.**', 'SE distinguishes its claim from eliminativism, mysterianism, panpsychism and strong emergence.',
     'statement-grade', 'statement', 'the distinctions at :163-:169', None),
    ('SE-11', 'SE', 183, 'But this is ultimately an empirical question, not one settable by theorem.', 'SE states that whether neural structure '
     'and experience are coupled or identical is an empirical question its theorem does not settle.', 'statement-grade', 'statement',
     'the paper’s own scope', None),
    ('SE-12', 'SE', 195, 'because correlation is not derivation', 'SE states that neural correlates of consciousness do not refute the principle, '
     'correlation not being derivation.', 'argument-supported', 'argument', 'the genetic-code analogy at :197-:199', None),
    ('SE-13', 'SE', 215, 'no future neuroscience will derive specific qualia', 'SE states as its falsifiable claim that no future neuroscience will '
     'derive specific qualia from neural patterns through the interface.', 'statement-grade', 'statement', 'the falsifier at :215', None),
    ('SE-14', 'SE', 233, 'This variation is emergence in the precise sense', 'SE reads codon-usage bias as emergence in the silent zone the genetic '
     'code leaves open.', 'synthesis-suggested', 'reading', 'a reading at :233-:235', None),
    ('SE-15', 'SE', 269, 'The Silence Principle does not solve the hard problem of consciousness.', 'SE states that the principle does not solve '
     'the hard problem and explains only its logical structure.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('SE-16', 'SE', 275, 'The consciousness instance is argued by structural analogy.', 'SE states that its mathematical instance is formalized and '
     'its consciousness instance argued by structural analogy.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    # ---------------------------------------------------------------- DARK_INTERFACE (p2-24)
    ('DI-01', 'DI', 28, 'κ(validity, natural language) = 0', 'DI states that natural language carries no information about the validity of a '
     'mathematical argument, κ(validity, natural language) = 0.', 'argument-supported', 'argument', 'the paired examples at :16-:24', None),
    ('DI-02', 'DI', 30, 'Voevodsky (2002) published a proof of the Milnor conjecture', 'DI cites Voevodsky’s Milnor-conjecture error, Hsiang’s '
     'Kepler paper and the contested IUT programme as cases where the medium did not carry correctness.', 'synthesis-suggested', 'reading',
     'a reading of three cases', None),
    ('DI-03', 'DI', 52, 'any essential, universal medium for mathematical communication MUST be dark for validity', 'DI applies the Silence '
     'Principle to state that every essential, universal medium for mathematical communication is dark for validity.', 'argument-supported',
     'argument', 'the chain at :44-:50', None),
    ('DI-04', 'DI', 60, 'The parallel is not metaphorical', 'DI reads natural language and the product formula as instances of one phenomenon, '
     'each essential, universal and dark.', 'synthesis-suggested', 'reading', 'a reading at :56-:60', None),
    ('DI-05', 'DI', 74, 'sieve methods can prove density results', 'DI states that sieve methods give density results, such as at least 40% of the '
     'zeros on the critical line, and not the placement of every zero.', 'theorem-supported', 'theorem', 'Conrey 1989 and Selberg 1942, named',
     None),
    ('DI-06', 'DI', 86, 'Both achieve density without placement.', 'DI reads peer review and the sieve as limited for one reason, each operating '
     'through a dark interface.', 'synthesis-suggested', 'reading', 'a reading at :80-:88', None),
    ('DI-07', 'DI', 92, 'The mathematical content needed for a resolution by exhaustive enumeration', 'DI states that the mathematical content for '
     'resolving RH by exhaustive enumeration existed for decades before it was assembled.', 'statement-grade', 'statement',
     'stated at :92 without an argument', R1),
    ('DI-08', 'DI', 104, 'κ(validity, type system) = 1', 'DI states that the Lean type system transmits validity exactly, κ(validity, type system) '
     '= 1.', 'argument-supported', 'argument', 'argued at :102-:106; DI :177 names the falsifier, a type-correct term of False', None),
    ('DI-09', 'DI', 110, 'the type system achieves brightness by sacrificing universality', 'DI states that the type system is bright for validity '
     'because it is not universal.', 'argument-supported', 'argument', 'the argument at :110', None),
    ('DI-10', 'DI', 119, 'The verified surround (the Lean kernel) certifies the conditional', 'DI states that a kernel certifies the conditional '
     'from structural exhaustiveness to RH and that the companion manuscripts supply the antecedent in natural language.', 'statement-grade',
     'terminal', 'the terminals named by role at :119, not by name or pin', R1),
    ('DI-11', 'DI', 125, 'In a single session (April 2026), the', 'DI reports a worked example from a private library, extended in one session '
     'and compiled without failure; the library is cited here by pointer alone.', 'statement-grade', 'statement', 'TECHNE content, carried '
     'by pointer: TECHNE-Core, its tracked-file manifest sha256 %s', None),
    ('DI-12', 'DI', 135, 'The conservation coefficient κ for amino acid identity under single-nucleotide mutations is 0.94', 'DI reports κ = 0.94 '
     'for amino-acid identity under single-nucleotide mutations and reads peer review as the mathematical analogue of the code’s error '
     'correction.', 'synthesis-suggested', 'reading', 'a reading at :133-:137', None),
    ('DI-13', 'DI', 143, 'dark interfaces are firewalls', 'DI reads the darkness of natural language as protection, letting incorrect but '
     'instructive arguments be expressed.', 'synthesis-suggested', 'reading', 'a reading at :141-:145', None),
    ('DI-14', 'DI', 153, 'No amount of training, scaling, or capability improvement will change the κ of natural language.', 'DI states that a '
     'model working in natural language has κ ≈ 0 for validity whatever its capability, and that a type-checked architecture changes κ.',
     'statement-grade', 'statement', 'stated at :151-:157', None),
    ('DI-15', 'DI', 175, 'The claim κ(validity, natural language) = 0 is falsifiable.', 'DI states that its claim is falsifiable by a feature of '
     'natural language that reliably separates valid from invalid arguments.', 'statement-grade', 'statement', 'the falsifier at :175', None),
    # ---------------------------------------------------------------- COGNITION (p2-14)
    ('CG-01', 'CG', 22, 'This is not a metaphor. It is a metabolic conservation law.', 'CG states that the interface between external stimulation '
     'and internal construction runs at κ ≈ 0 in healthy cognition, as a metabolic conservation law.', 'statement-grade', 'statement',
     'asserted at :22 and :98; CG :327 calls the law approximate, a metabolic constraint', None),
    ('CG-02', 'CG', 24, 'The correlation between Bloom level of assessment and active learning advantage is r = 0.762', 'CG reports r = 0.762 '
     'between the Bloom level of assessment and the active-learning advantage across meta-analytic comparisons from Freeman et al. (2014).',
     'computationally-verified', 'computation', 'the table at :155-:168 and the coefficient at :172, given there as n = 12 excluding one of '
     'the table’s twelve rows', None),
    ('CG-03', 'CG', 68, 'The interface stage should have n₄ = 0', 'CG states a four-stage formation (n₁, n₂, n₃, n₄) whose interface stage has '
     'n₄ = 0 in a well-structured system.', 'statement-grade', 'statement', 'stated at :61-:68', None),
    ('CG-04', 'CG', 98, 'κ(Task-Positive) + κ(Default Mode) ≈ 1', 'CG states κ(Task-Positive) + κ(Default Mode) ≈ 1, enforced by the brain’s '
     'metabolic budget.', 'statement-grade', 'statement', 'stated at :98', None),
    ('CG-05', 'CG', 104, '(n₁, n₂, n₃, n₄) = (Task-Positive, Frontoparietal, Default Mode, 0)', 'CG maps the Task-Positive, Frontoparietal and '
     'Default Mode networks onto the formation stages, with interface n₄ = 0.', 'synthesis-suggested', 'reading', 'CG :329 calls the mapping '
     'an interpretive choice', None),
    ('CG-06', 'CG', 114, "McLuhan's hot/cold distinction maps directly to the conservation coefficient", 'CG maps McLuhan’s hot and cool media '
     'onto κ for content delivery.', 'synthesis-suggested', 'reading', 'the table at :116-:121', None),
    ('CG-07', 'CG', 184, 'concept inventories (targeting n₂ and n₃) show a 56% larger effect', 'CG reports concept inventories showing a 56% larger '
     'effect than traditional exams in Freeman et al. (2014).', 'computationally-verified', 'computation', 'the ratio of its rows, 0.61 to 0.39',
     None),
    ('CG-08', 'CG', 186, 'A 3.9× ratio', 'CG reports the conceptual-to-factual effect ratio in Ruiz-Primo et al. as 3.9.', 'computationally-verified',
     'computation', 'the ratio of its rows, 0.58 to 0.15', None),
    ('CG-09', 'CG', 178, '| n₁ (Remember, Understand) | d = 0.34 | 384 |', 'CG reports mean effect sizes 0.34, 0.53 and 0.73 for the stages n₁, '
     'n₂ and n₃.', 'computationally-verified', 'computation', 'the means of its table rows; its n₂ study count, 261 at :179, is not the sum of '
     'the rows its table lists', None),
    ('CG-10', 'CG', 199, 'The ICAP hierarchy is a conservation profile in disguise.', 'CG reads Chi and Wylie’s ICAP hierarchy as a κ gradient.',
     'synthesis-suggested', 'reading', 'the table at :192-:197', None),
    ('CG-11', 'CG', 210, '**Feeling of Learning** (self-reported): d = −0.30', 'CG cites Deslauriers et al. (2019): test of learning d = +0.36 and '
     'feeling of learning d = −0.30.', 'computationally-verified', 'computation', 'the study, cited', None),
    ('CG-12', 'CG', 226, '**Clause G (Generativity):', 'CG proposes Clause G: dark interfaces are the necessary condition for structural '
     'self-organisation.', 'statement-grade', 'statement', 'proposed at :226; CG :232 reads its data as confirming it', None),
    ('CG-13', 'CG', 246, 'creativity is a transient n₄ > 0 event', 'CG reads creative insight as a transient breach of the conservation law, citing '
     'Beaty et al. (2016).', 'synthesis-suggested', 'reading', 'a reading at :244-:248', None),
    ('CG-14', 'CG', 262, 'The normal conservation law (κ_Default Mode + κ_Task-Positive ≈ 1) breaks', 'CG reads depression as a breakdown of the '
     'network anti-correlation and mindfulness as its restoration.', 'synthesis-suggested', 'reading', 'a reading at :260-:270', None),
    ('CG-15', 'CG', 274, 'the strength of the Default Mode/Task-Positive anti-correlation should predict treatment response', 'CG predicts that the '
     'strength of the network anti-correlation predicts mindfulness treatment response.', 'statement-grade', 'statement', 'a prediction', None),
    ('CG-16', 'CG', 327, '**The conservation law is approximate, not exact.**', 'CG states that in the neural setting its conservation law is '
     'approximate and that its network-to-stage mapping is an interpretive choice.', 'statement-grade', 'statement', 'the paper’s own '
     'limits at :327-:329', None),
    # ---------------------------------------------------------------- UNIFIED_COGNITIVE (p2-21)
    ('UC-01', 'UC', 13, 'r = 0.762 with Bloom-level engagement', 'UC reports r = 0.762 for learning effectiveness and r = 0.656 between '
     'interface darkness and the difficulty of 156 IMO problems.', 'computationally-verified', 'computation', 'reported; the IMO computation '
     'cited to a manuscript (:116)', None),
    ('UC-02', 'UC', 23, 'mean MOHS 29.6 vs. algebra 23.5', 'UC reports combinatorics as the hardest IMO domain, mean MOHS 29.6 against algebra’s '
     '23.5.', 'computationally-verified', 'computation', 'the table at :56-:61', None),
    ('UC-03', 'UC', 65, 'Accuracy: 12/12.', 'UC reports that across twelve IMO 2024–2025 problems AI solved every problem with κ > 0 at the '
     'method-solution interface and failed every one with κ ≈ 0.', 'computationally-verified', 'computation', 'twelve problems, reported', None),
    ('UC-04', 'UC', 80, 'is the signature of a real structural variable, not a coincidence', 'UC reads the agreement of the two datasets as the '
     'signature of one domain-general variable.', 'synthesis-suggested', 'reading', 'a reading at :78-:80', None),
    ('UC-05', 'UC', 88, 'This predicts the Freeman et al. result', 'UC maps bright and dark interfaces onto joint and Task-Positive-only network '
     'engagement.', 'synthesis-suggested', 'reading', 'a reading at :86-:90', None),
    ('UC-06', 'UC', 100, 'AI systems will continue to fail at dark-interface problems', 'UC predicts that AI systems will fail at dark-interface '
     'problems until they build internal models.', 'statement-grade', 'statement', 'a prediction', None),
    ('UC-07', 'UC', 102, '**Cross-domain:** κ will predict outcomes in other cognitive domains', 'UC predicts that κ will predict outcomes in '
     'therapy, creativity and expertise development.', 'statement-grade', 'statement', 'a prediction', None),
    # ---------------------------------------------------------------- IDENTITY_SUBSPACE (p2-22)
    ('IS-01', 'IS', 35, '**Proposition 1.2.** The exponential balance point is σ₀ = 1/2.', 'IS states that n^(−σ) = n^(−(1−σ)) for every n ≥ 2 '
     'holds exactly at σ = 1/2.', 'argument-supported', 'argument', 'the argument at :37', None),
    ('IS-02', 'IS', 53, 'not logically independent: three of them take the involution', 'IS states five convergent constructions of σ = 1/2 and, '
     'corrected, that they are not logically independent, three taking the involution σ ↦ 1 − σ as their definition.', 'synthesis-suggested',
     'reading', 'the convergence reading at :51-:65 with its correction', R2),
    ('IS-03', 'IS', 65, 'No two share logical dependencies beyond the axioms of ℤ.', 'IS states that its five derivations use disjoint machinery '
     'with no shared logical dependencies.', 'statement-grade', 'statement', 'the sentence stands beneath the correction at :53, which says '
     'three share the involution', None),
    ('IS-04', 'IS', 85, 'the identity subspace is empty', 'IS states that the pointwise intersection of the three identity loci is empty and takes the '
     'centered coordinate instead.', 'argument-supported', 'argument', 'the argument at :87-:89', None),
    ('IS-05', 'IS', 129, '**Frobenius completeness.** The Frobenius number g(2,3) = 1', 'IS states that g(2, 3) = 1 makes every integer ≥ 2 a '
     'nonnegative combination of 2 and 3, and that every other coprime pair with a ≥ 2 has g(a, b) ≥ 1.', 'theorem-supported', 'theorem',
     'the Sylvester-Frobenius formula, named at :135; the bound ≥ 1 does not separate {2, 3}, which needs g(a, b) ≥ 2', None),
    ('IS-06', 'IS', 141, '**Proposition 3.2.** The discriminants constructible from {2, 3, −1}', 'IS states that {−1, 2, 3} generate seven nontrivial '
     'quadratic fields ℚ(√d).', 'argument-supported', 'argument', 'the argument at :147', None),
    ('IS-07', 'IS', 155, r'$$(1, 2), \quad (2, 3), \quad (3, 4), \quad (8, 9)$$', 'IS states Størmer’s theorem for {2, 3}: the consecutive smooth '
     'pairs are (1, 2), (2, 3), (3, 4) and (8, 9).', 'theorem-supported', 'theorem', 'Størmer 1897 and Lehmer 1964, named at :157', None),
    ('IS-08', 'IS', 171, 'The {2,3}-smooth integers ≤ 3 are {0, 1, 2, 3}.', 'IS counts the dimension 7 from the {2,3}-smooth integers up to 3, '
     'listed as {0, 1, 2, 3}, and the symmetric index set {−3, …, 3}.', 'argument-supported', 'argument', 'the argument at :167-:173; 0 is '
     'listed among the {2,3}-smooth integers', None),
    ('IS-09', 'IS', 203, '||v||² = Σ|v_n|² = 3 + 2 + 1 + 0 + 1 + 2 + 3 = 12', 'IS states that the Trivium vector has norm squared 12.',
     'argument-supported', 'argument', 'the computation at :203', None),
    ('IS-10', 'IS', 219, 'In particular, T² = −I (not +I)', 'IS states that multiplication by i generates ℤ/4 on the Trivium vector, T² = −I, '
     'the identity returning after four applications.', 'argument-supported', 'argument', 'the argument at :221', None),
    ('IS-11', 'IS', 239, r'\text{spec}(M) = \{0, 0, 0, 0, 0, 0, 12\}', 'IS states that M = vv† has spectrum {0⁶, 12}.', 'argument-supported',
     'argument', 'the argument at :243', None),
    ('IS-12', 'IS', 305, '**Theorem 6.2.** Every prime p > 3 has valence exactly 3 or exactly 7.', 'IS states that every prime p > 3 splits in '
     'exactly 3 or exactly 7 of the seven fields.', 'argument-supported', 'argument', 'the argument at :307-:323', None),
    ('IS-13', 'IS', 331, '(ℤ/24ℤ)* ≅ (ℤ/8ℤ)* × (ℤ/3ℤ)* ≅ (ℤ/2)² × ℤ/2', 'IS states that (ℤ/24)* has order 8 and is (ℤ/2)² × ℤ/2 by the '
     'Chinese Remainder Theorem.', 'theorem-supported', 'theorem', 'the Chinese Remainder Theorem, named at :331', None),
    ('IS-14', 'IS', 355, 'This is the standard criterion for a non-orientable bundle.', 'IS asks whether the fiber bundle over the critical line is '
     'orientable and reads T² = −I as a non-trivial holonomy.', 'statement-grade', 'statement', 'an open question at :353-:355', None),
    ('IS-15', 'IS', 365, 'can be assembled into a proof of this conjecture is an open question', 'IS states that whether its structures assemble '
     'into a resolution of RH is open, and that it establishes the object.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    # ---------------------------------------------------------------- INTERFACE_DARKNESS (p2-28)
    ('ID-01', 'ID', 15, 'interface darkness ($\\kappa = 0$) is a domain-general cognitive variable', 'ID states the cluster’s central '
     'observation, that interface darkness is a domain-general cognitive variable.', 'synthesis-suggested', 'reading', 'the convergence '
     'reading at :15', None),
    ('ID-02', 'ID', 17, "The cluster's epistemic status is empirical regularity.", 'ID states that the cluster’s epistemic status is empirical '
     'regularity.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('ID-03', 'ID', 25, 'kernel-verified in `SIDE-silence-principle v0.1`', 'ID states that the Silence Principle is kernel-verified in '
     'SIDE-silence-principle v0.1.', 'statement-grade', 'terminal', 'no terminal named; the pin v0.1 resolves neither in the clone nor at '
     'the remote, whose tags are v0.1.0 and v0.2.0', None),
    ('ID-04', 'ID', 29, 'Predicted: even careful peer review cannot reliably distinguish valid from invalid arguments', 'ID reads three '
     'historical cases as confirming that peer review cannot reliably separate valid from invalid arguments.', 'synthesis-suggested', 'reading',
     'a reading at :29', None),
    ('ID-05', 'ID', 73, '**Peer review and sieve methods share a barrier.**', 'ID reads peer review and sieve methods as sharing one '
     'density-without-placement barrier.', 'synthesis-suggested', 'reading', 'a reading at :73', None),
    ('ID-06', 'ID', 93, 'The interface between neural activity and subjective experience must be universal', 'ID argues that the '
     'neural-experiential interface must be universal, hence dark for qualia.', 'argument-supported', 'argument', 'the argument at :93',
     None),
    ('ID-07', 'ID', 109, 'their anti-correlation is a conservation law operating across an interface', 'ID states κ_TPN + κ_DMN ≈ 1 in healthy '
     'cognition as an empirical structural finding.', 'statement-grade', 'statement', 'ID :291 calls the conservation form a structural '
     'reinterpretation', None),
    ('ID-08', 'ID', 131, 'Sustained co-activation is pathological (mania, certain psychotic states)', 'ID reads sustained network co-activation as '
     'pathological and transient co-activation as creativity.', 'statement-grade', 'statement', 'stated at :131', None),
    ('ID-09', 'ID', 141, 'Its status is empirical regularity in cognitive systems', 'ID states that Clause G’s status is empirical regularity in '
     'cognitive systems.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('ID-10', 'ID', 187, 'achieves $12/12$ prediction accuracy', 'ID reports the 12/12 accuracy on the IMO 2024–2025 problems with AI performance '
     'data.', 'computationally-verified', 'computation', 'reported; ID :279 calls the data set small', None),
    ('ID-11', 'ID', 193, 'The cluster states a forward prediction for IMO 2026', 'ID states a forward prediction for AI performance on IMO 2026.',
     'statement-grade', 'statement', 'a prediction', None),
    ('ID-12', 'ID', 245, "This cluster's content is empirically anchored rather than kernel-verified.", 'ID states that the cluster’s content is '
     'empirically anchored and not kernel-verified, the principle being its cited anchor.', 'statement-grade', 'statement',
     'the paper’s own scope', None),
    ('ID-13', 'ID', 250, '`silence_universal`; nine instances compiled individually', 'ID names silence_universal in MetaKernel.lean and '
     'Kernel/SilenceTheorem.lean with nine instances compiled.', 'statement-grade', 'terminal', 'named without a pin; the name stands at '
     'SIDE-kernel main, Kernel/SilenceTheorem.lean :74', None),
    ('ID-14', 'ID', 289, 'Specific correlation coefficients are sensitive to the analysis methodology', 'ID states that its correlation '
     'coefficients depend on the re-analysis method, the framework’s predictive content being the load-bearing claim.', 'statement-grade',
     'statement', 'the paper’s own scope', None),
]

ROUTE_ROWS = {'RH-60': 'DARK, test 2'}
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def paper_lines():
    return {k: lines_of(show(v[0])) for k, v in PAPERS.items()}


def techne_pointer():
    """### the pointer to TECHNE-Core: the sha256 of its tracked-file manifest at HEAD (`git ls-tree -r HEAD`), no body read or printed"""
    r = subprocess.run(['git', '-C', TE, 'ls-tree', '-r', 'HEAD'], capture_output=True)
    return hashlib.sha256(r.stdout.replace(b'\r\n', b'\n')).hexdigest() if r.returncode == 0 else None


def claims():
    """### the claims with the pointer filled into DI-11's reason"""
    p = techne_pointer()
    return [c if c[0] != 'DI-11' else c[:7] + (c[7] % p,) + c[8:] for c in C]


def resolve_claims():
    """### every claim's needle on its cited line at the pin: [(id, ok, the line)]"""
    P = paper_lines()
    out = []
    for c in C:
        cid, pk, n, needle = c[0], c[1], c[2], c[3]
        l = P[pk][n - 1] if 0 < n <= len(P[pk]) else ''
        out.append((cid, needle in l, l))
    return out


def cited_pin_state(key):
    """### a cited pin: (key, repo, pin, local commit or '', how the remote holds it or None)"""
    repo, pin, _what = CITED_PINS[key]
    path = 'D:/' + repo
    loc = g(path, 'rev-parse', '--verify', '-q', pin + '^{commit}').strip()
    rem = None
    if loc:
        for l in g(path, 'ls-remote', 'origin', 'refs/tags/*').split(NL):
            if l.startswith(loc):
                rem = 'remote tag %s' % l.split('refs/tags/')[1].replace('^{}', '')
                break
    tags = sorted(x for x in g(path, 'tag', '-l').split(NL) if x.strip())
    return (key, repo, pin, loc[:12], rem, tags)


def unpinned_state(name):
    repo, rev, f, n, needle = UNPINNED[name]
    ls = lines_of(show(f, rev, 'D:/' + repo))
    l = ls[n - 1] if 0 < n <= len(ls) else ''
    return (name, repo, rev, f, n, needle in l, l)


def sieve_rows():
    out = {}
    for l in lines_of(show(SIEVE)):
        m = re.match(r'^\| ((?:RH|FD|CT)-\d\d) \| ', l)
        if m and m.group(1) in ROUTE_ROWS and m.group(1) not in out:
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = (c[4], c[5])
    return out


def grade_ok(c):
    return c[5] in GRADES and c[6] in NEEDS[c[5]] and c[5] != 'kernel-verified'   # ### no pin the papers cite resolves; no row certifies


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:80]) for i, _o, l in bad] or 'NONE'))
    for k in CITED_PINS:
        print('### cited pin %s' % (cited_pin_state(k),))
    for k in UNPINNED:
        print('### unpinned name %s' % (unpinned_state(k)[:6],))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    print('### ids unique: %s ; TECHNE pointer sha256 %s' % (len(set(c[0] for c in C)) == len(C), techne_pointer()))


if __name__ == '__main__':
    main()
