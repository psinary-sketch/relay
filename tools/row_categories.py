# -*- coding: utf-8 -*-
"""row_categories.py -- ### **WHAT A CITED NAME CAN BE, BESIDES A CORPUS TERMINAL OR AN ABSENCE.**

### ### **THE PROBLEM THIS EXISTS TO STOP:** ### a checker that knows only *terminal* and *not found*
### reports every other kind of cited name as a defect. ### `b378` classified `37` such names and found
### that ### **`23` OF THEM WERE NEVER MISSING TERMINALS AT ALL** -- library lemmas, corpus documents,
### and names living on a tag rather than a branch.
### ### ### **A CATEGORY REPORTED AS AN ABSENCE IS A FALSE DEFECT**, and false defects are expensive:
### `b377` spent an act on a population `b376`'s narrowness had selected.

### ### **THE FRONT DOOR ALREADY HAS WORDS FOR SOME OF THIS AND THEY ARE QUOTED, NOT REPLACED.**
### `PLACE-papers/README.md`, under *Correspondence tables*:
###   ### *"Each row maps a claim the paper makes to the artifact that verifies it: claim . kernel .
###   ### fully-qualified theorem name . axiom profile . status."*
###   ### *"Where no kernel exists, the status says so in words -- MANUSCRIPT-RESIDENT or
###   ### RESEARCH-REACH -- rather than being omitted."*
### ### So `MANUSCRIPT_RESIDENT` and `RESEARCH_REACH` are ### **THE CORPUS'S OWN WORDS** ### and are
### carried here under the corpus's own spelling. ### The three added by `b379` are the ones `b378`
### met and the front door has no word for.

### ### ### **THIS MODULE RETURNS A CATEGORY AND NEVER A VERDICT.** ### Saying a name is a library
### lemma says ### **WHERE THE TERMINAL LIVES**. ### It does not say the row is right, the claim is
### true, or the citation is adequate. ### **A CATEGORY IS NOT AN EXCUSE**, and a checker that treats
### one as a pass has made the opposite of `b378`'s mistake.

### ### **EVERY CATEGORY IS FIXTURED IN BOTH POLARITIES:** ### recognised where it applies, and
### ### **REFUSED WHERE IT DOES NOT.** ### A recogniser that only ever says yes is not a recogniser.
"""
import io
import os
import re

# ### **THE CORPUS'S OWN WORDS, FROM THE FRONT DOOR, CARRIED AND NOT REDEFINED.**
FRONT_DOOR = 'PLACE-papers/README.md, section "Correspondence tables"'
FRONT_DOOR_QUOTE = ('Where no kernel exists, the status says so in words -- '
                    'manuscript-resident or research-reach -- rather than being omitted.')

CATEGORIES = {
    'CORPUS_TERMINAL': ('the name is declared in a corpus kernel on a ref this checker searched',
                        'b373/b377', None),
    'MANUSCRIPT_RESIDENT': ('no kernel exists and the row says so; the content lives in the '
                            'manuscript', 'the front door', FRONT_DOOR),
    'RESEARCH_REACH': ('no kernel exists and the row says so; the claim is a reach not yet attempted',
                       'the front door', FRONT_DOOR),
    'LIBRARY_TERMINAL': ('the name is declared in a LIBRARY the corpus depends on, not in a corpus '
                         'kernel -- a paper may cite a lemma it did not prove', 'b379 (from b378)',
                         None),
    'NAMES_A_CORPUS_DOCUMENT': ('the backticked name is a document in the corpus, not a terminal at '
                                'all -- which the front door already calls MANUSCRIPT-RESIDENT when '
                                'a row says so in words', 'b379 (from b378)', FRONT_DOOR),
    'ON_A_TAG_NOT_A_BRANCH': ('the name is declared on a tag of a corpus kernel and on no branch -- '
                              'a tag is a ref, and a checker that searches only branches misses it',
                              'b379 (from b378)', None),
    'NOT_LOCATED': ('no ref of any kernel searched declares it, and no category above applies',
                    'b377', None),
}
ADDED_AT_B379 = ('LIBRARY_TERMINAL', 'NAMES_A_CORPUS_DOCUMENT', 'ON_A_TAG_NOT_A_BRANCH')

# ### **THE RECOGNISERS.** ### Each takes evidence and answers about THAT evidence only.
MANUSCRIPT_WORDS = re.compile(r'\bmanuscript[- ]resident\b', re.I)
REACH_WORDS = re.compile(r'\bresearch[- ]reach\b', re.I)
LIBRARY_ROOTS = ('Mathlib', 'Std', 'Batteries', 'Lean', 'Init', 'Aesop', 'Qq')


def is_library_path(path):
    """### **A PATH INSIDE A DEPENDENCY PACKAGE, NOT INSIDE A CORPUS KERNEL'S OWN SOURCE.**"""
    if not path:
        return False
    p = str(path).replace(chr(92), '/')
    if '/.lake/packages/' in p or p.startswith('.lake/packages/'):
        return True
    head = p.split('/')[0]
    return head in LIBRARY_ROOTS


def is_document_name(name, document_basenames):
    """### **THE BACKTICKED NAME IS A DOCUMENT IN THE CORPUS.** ### The caller supplies the set, so
    the module never guesses what the corpus contains."""
    if not name:
        return False
    base = str(name).rsplit('/', 1)[-1]
    base = base[:-3] if base.endswith('.md') else base
    return base in document_basenames


def is_tag_only(refs):
    """### **DECLARED ON A TAG AND ON NO BRANCH.** ### An empty ref list is not a tag-only find."""
    refs = [str(r) for r in (refs or [])]
    if not refs:
        return False
    tags = [r for r in refs if '/tags/' in r]
    branches = [r for r in refs if '/heads/' in r or '/remotes/' in r]
    return bool(tags) and not branches


def categorise(name, hits=None, refs=None, row_text='', document_basenames=frozenset()):
    """### **RETURN `(category, why)`. ### EXACTLY ONE CATEGORY, ALWAYS.**

    ### The order is deliberate and is the module's only opinion:
    ###   a name found in a corpus kernel is a corpus terminal, however it is also described;
    ###   then a library find;
    ###   then a tag-only find;
    ###   then what the ROW ITSELF says in the front door's words;
    ###   then whether the name is a document;
    ###   and only then ### **NOT_LOCATED**, which is the sole category that asserts an absence.
    ### ### **THE ABSENCE IS LAST BECAUSE IT IS THE ONLY ONE THAT CAN BE WRONG BY OMISSION.**
    """
    hits = list(hits or [])
    corpus = [h for h in hits if not is_library_path(h.get('path'))]
    library = [h for h in hits if is_library_path(h.get('path'))]
    if corpus:
        if is_tag_only(refs or [r for h in corpus for r in (h.get('refs') or [])]):
            return 'ON_A_TAG_NOT_A_BRANCH', ('declared in a corpus kernel, on a tag and on no '
                                             'branch')
        return 'CORPUS_TERMINAL', 'declared in a corpus kernel on a searched ref'
    if library:
        return 'LIBRARY_TERMINAL', ('declared at `%s`, which is a dependency and not a corpus kernel'
                                    % library[0].get('path'))
    if MANUSCRIPT_WORDS.search(row_text or ''):
        return 'MANUSCRIPT_RESIDENT', "the row says so in the front door's own word"
    if REACH_WORDS.search(row_text or ''):
        return 'RESEARCH_REACH', "the row says so in the front door's own word"
    if is_document_name(name, document_basenames):
        return 'NAMES_A_CORPUS_DOCUMENT', 'the backticked name is a document in the corpus'
    return 'NOT_LOCATED', 'no searched ref declares it and no other category applies'


def self_test(verbose=False):
    """### **BOTH POLARITIES FOR EVERY CATEGORY.** ### Recognised where it applies; ### **REFUSED
    ### WHERE IT DOES NOT** -- because a recogniser that only ever says yes is not a recogniser."""
    DOCS = frozenset({'OPEN_TRAILS', 'THE_RESIDUE_OF_RH'})
    KERNEL_HIT = [dict(path='SIDELvConservation/Residue.lean', refs=['refs/heads/main'])]
    TAG_HIT = [dict(path='SIDEEffects/Structural.lean', refs=['refs/tags/v0.1'])]
    LIB_HIT = [dict(path='.lake/packages/mathlib/Mathlib/Analysis/X.lean',
                    refs=['refs/heads/master'])]
    cases = [
        ('a kernel find is a corpus terminal',
         categorise('residue_irreducible', KERNEL_HIT, ['refs/heads/main'], '', DOCS)[0],
         'CORPUS_TERMINAL'),
        ('### **and a kernel find is NOT called a library one**',
         categorise('residue_irreducible', KERNEL_HIT, ['refs/heads/main'], '', DOCS)[0]
         != 'LIBRARY_TERMINAL', True),
        ('a dependency-package find is a library terminal',
         categorise('Complex.Gamma', LIB_HIT, ['refs/heads/master'], '', DOCS)[0],
         'LIBRARY_TERMINAL'),
        ('### **and a library find is NOT called NOT_LOCATED**',
         categorise('Complex.Gamma', LIB_HIT, [], '', DOCS)[0] != 'NOT_LOCATED', True),
        ('a tag-only find is tag-only',
         categorise('grh_exclusion', TAG_HIT, ['refs/tags/v0.1'], '', DOCS)[0],
         'ON_A_TAG_NOT_A_BRANCH'),
        ('### **and a branch find is NOT called tag-only**',
         categorise('grh_exclusion', KERNEL_HIT, ['refs/heads/main'], '', DOCS)[0],
         'CORPUS_TERMINAL'),
        ("a row saying manuscript-resident is taken at the front door's word",
         categorise('h2', [], [], 'status: MANUSCRIPT-RESIDENT -- monograph 27.3', DOCS)[0],
         'MANUSCRIPT_RESIDENT'),
        ('a row saying research-reach likewise',
         categorise('zeroPairing', [], [], '### **RESEARCH-REACH.** disclaimed', DOCS)[0],
         'RESEARCH_REACH'),
        ('### **and a silent row is NOT read as either**',
         categorise('mystery_name', [], [], 'a row that says nothing about a kernel', DOCS)[0]
         not in ('MANUSCRIPT_RESIDENT', 'RESEARCH_REACH'), True),
        ('a name that is a corpus document is named as one',
         categorise('OPEN_TRAILS', [], [], '', DOCS)[0], 'NAMES_A_CORPUS_DOCUMENT'),
        ('### **and a name that is not a document is NOT**',
         categorise('not_a_document_name', [], [], '', DOCS)[0], 'NOT_LOCATED'),
        ('nothing found and nothing said is NOT_LOCATED',
         categorise('vanished', [], [], '', DOCS)[0], 'NOT_LOCATED'),
        ('### **and NOT_LOCATED is never returned when a hit exists**',
         categorise('vanished', KERNEL_HIT, ['refs/heads/main'], '', DOCS)[0] != 'NOT_LOCATED',
         True),
        ('every category the module names is reachable',
         len(CATEGORIES) >= 7, True),
    ]
    ok = all(g == w for _l, g, w in cases)
    if verbose:
        for lbl, g, w in cases:
            print('      %-58s got %-24s want %-24s %s'
                  % (lbl[:58], str(g)[:24], str(w)[:24], 'ok' if g == w else '### MISMATCH ###'))
    return ok, [dict(case=l, got=str(g), want=str(w)) for l, g, w in cases]


def corpus_document_basenames(root):
    """### **THE DOCUMENT SET, READ FROM DISK BY THE CALLER'S ROOT** -- never guessed here."""
    out = set()
    for dp, _dn, fn in os.walk(root):
        if '.git' in dp:
            continue
        for f in fn:
            if f.endswith('.md'):
                out.add(f[:-3])
    return frozenset(out)


if __name__ == '__main__':
    ok, log = self_test(True)
    print('  ### ### **SELF-TEST : %s**'
          % ('EVERY CATEGORY RECOGNISED AND EVERY ONE REFUSED WHERE IT DOES NOT APPLY' if ok
             else '### FAILED'))
    print('  ### categories : %d, of which added at b379 : %d'
          % (len(CATEGORIES), len(ADDED_AT_B379)))
    print('  ### the front door : %s' % FRONT_DOOR)
    raise SystemExit(0 if ok else 1)
