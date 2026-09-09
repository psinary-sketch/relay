# -*- coding: utf-8 -*-
"""role_structure.py -- ### **ROLE READ FROM WHAT A DOCUMENT DRAWS ON, NOT FROM WHAT IT SAYS.**

### ### **WHY THIS EXISTS.** ### `b376` scored the role axis from documents' own statements about
### themselves and found ### **340 OF 349 SAY NOTHING.** ### Four acts widened, corrected and
### re-measured the APPARATUS axis and the role column never moved once. ### **A COLUMN THAT DOES NOT
### ### MOVE UNDER FOUR CORRECTIONS IS NOT A COLUMN WITH A MEASUREMENT PROBLEM. ### IT IS A COLUMN
### ### MEASURING SOMETHING THE CORPUS DOES NOT WRITE DOWN.**

### ### **THE RUBRIC, QUOTED, AND READ STRUCTURALLY.**
###   `KEYSTONES synthesize a cluster AGAINST OTHER AVAILABLE CONTENT -- kernels, other keystones,
###    other clusters`
###   `SUPPORT documents GATHER a subject's research at a point in time`
### ### **SYNTHESIS IS A CLAIM ABOUT REACH:** ### what a document draws on, and whether that reaches
### beyond its own subject. ### **GATHERING IS A CLAIM ABOUT CONFINEMENT:** ### what it draws on lies
### inside one subject.

### ### ### **THE THRESHOLD IS A CHOICE AND IT IS DECLARED, NOT DISCOVERED.** ### The rubric's own
### sentence lists THREE kinds of other content, so ### **ONE FOREIGN TOUCH IS A CITATION AND TWO IS A
### ### COMBINATION.** ### That is set from the wording BEFORE the control runs, and ### **IF THE
### ### CONTROL DISAGREES THE THRESHOLD IS NOT MOVED TO MAKE IT AGREE.**

### ### **WHAT IT IS DEAF TO, AND ALL FOUR ARE REAL:**
###   ### **A DOCUMENT THAT SYNTHESISES WITHOUT CITING** ### is invisible -- the same class the
###     statement-based predicate missed, missed a second way.
###   ### **A DOCUMENT THAT CITES WIDELY AND SYNTHESISES NOTHING** ### scores high: a bibliography, an
###     index or a ledger reaches everywhere by construction. ### **REACH IS NOT ARGUMENT.**
###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT**, which is an ADDRESS standing in for a subject
###     and is exactly the substitution `(R2)` warns about. ### Used because the corpus's clusters are
###     directory-shaped; ### **NAMED HERE AS A WEAKNESS.**
###   ### **A CITATION IT DOES NOT RECOGNISE IS NOT A CITATION TO IT** -- a document named in prose
###     without backticks or a path, a kernel named by a nickname.

### ### **IT RETURNS A MARK AND A REASON. ### IT NEVER RETURNS A CLASS.**
"""
import os
import re

# ### **WHAT COUNTS AS DRAWING ON SOMETHING.** ### Each pattern is a way the corpus actually writes a
# ### reference, taken from the documents and not invented.
KERNEL = re.compile(r'\b(SIDE-[A-Za-z0-9][A-Za-z0-9-]*)\b')
DOCPATH = re.compile(r'`([A-Za-z0-9_./-]+\.md)`|\(([A-Za-z0-9_./-]+\.md)\)')
DOCNAME = re.compile(r'`([A-Z][A-Z0-9_]{3,})`')

# ### **A KERNEL NAME THAT IS NOT A KERNEL.** ### The corpus writes `SIDE-effects` for a repository
# ### and also writes prose like "the SIDE programme"; only the hyphenated repository form counts.
NOT_A_KERNEL = re.compile(r'^SIDE-(programme|program|side)$', re.I)


def own_cluster(rel):
    """### **THE DOCUMENT'S OWN SUBJECT, TAKEN AS ITS DIRECTORY.** ### An address standing in for a
    subject, and the module says so rather than hiding it."""
    d = os.path.dirname(rel.replace(chr(92), '/'))
    return d or '(root)'


def kernels_named(text):
    out = set()
    for m in KERNEL.finditer(text):
        k = m.group(1)
        if not NOT_A_KERNEL.match(k):
            out.add(k)
    return out


def documents_cited(text, index, self_rel):
    """### **OTHER CORPUS DOCUMENTS THIS ONE NAMES**, resolved through an index the CALLER supplies,
    so the module never guesses what the corpus contains."""
    out = set()
    self_base = os.path.basename(self_rel)[:-3] if self_rel.endswith('.md') else ''
    for m in DOCPATH.finditer(text):
        p = (m.group(1) or m.group(2) or '').replace(chr(92), '/')
        base = os.path.basename(p)[:-3]
        if base and base != self_base and base in index:
            out.add(index[base])
    for m in DOCNAME.finditer(text):
        base = m.group(1)
        if base != self_base and base in index:
            out.add(index[base])
    return out


def score(rel, text, index):
    """### **RETURN `(mark, reason, evidence)`.** ### `A+` synthesis, `A-` gathering, `A?` silent.

    ### The rule, from the rubric and stated before it ran:
    ###   ### **`A+`** ### -- reach beyond its own subject in ### **AT LEAST TWO DISTINCT PLACES**,
    ###     counting each foreign cluster it cites into and each kernel it names.
    ###   ### **`A-`** ### -- it draws on something, and that reach is under two.
    ###   ### **`A?`** ### -- it draws on nothing this predicate can see.
    """
    mine = own_cluster(rel)
    ks = kernels_named(text)
    docs = documents_cited(text, index, rel)
    foreign = set(own_cluster(d) for d in docs) - {mine}
    reach = sorted(foreign) + sorted(ks)
    ev = dict(own_cluster=mine, kernels=sorted(ks), documents=len(docs),
              foreign_clusters=sorted(foreign), reach=len(reach))
    if len(reach) >= 2:
        return 'A+', ('reaches beyond its own subject in %d places : %s'
                      % (len(reach), ', '.join(reach[:6]))), ev
    if docs or ks:
        return 'A-', ('draws on %d document(s) and %d kernel(s), reaching beyond its own subject in '
                      '%d place(s)' % (len(docs), len(ks), len(reach))), ev
    return 'A?', 'it draws on nothing this predicate can see', ev


# ---- THE FIXTURES ----------------------------------------------------------------------------------
FIX_INDEX = {'THE_METHOD_CANON': 'phase1.5/method/THE_METHOD_CANON.md',
             'GRH_CASCADE': 'phase1.5/spectral/GRH_CASCADE.md',
             'INSTRUMENTS': 'phase1.5/method/INSTRUMENTS.md'}
FIX_SYNTH = ('It reads `GRH_CASCADE` against `SIDE-kernel` and `SIDE-lv-conservation`.' + chr(10))
FIX_GATHER = ('This note collects the `INSTRUMENTS` material for the method cluster.' + chr(10))
FIX_SILENT = ('A page of prose that names nothing at all, in no directory but its own.' + chr(10))


def self_test(verbose=False):
    """### **THREE POLARITIES, BECAUSE THE PREDICATE HAS THREE ANSWERS.** ### A predicate that can
    only say yes is not a predicate, and one that can only say yes and no cannot report silence."""
    HERE = 'phase1.5/method/A_TEST.md'
    cases = [
        ('a document reaching a foreign cluster AND kernels -- ### **A+**',
         score(HERE, FIX_SYNTH, FIX_INDEX)[0], 'A+'),
        ('a document drawing only inside its own directory -- ### **A-**',
         score(HERE, FIX_GATHER, FIX_INDEX)[0], 'A-'),
        ('a document drawing on nothing -- ### **A?**',
         score(HERE, FIX_SILENT, FIX_INDEX)[0], 'A?'),
        ('### **one kernel alone is a citation, not a combination -- A-**',
         score(HERE, 'It cites `SIDE-kernel` and nothing else.' + chr(10), FIX_INDEX)[0], 'A-'),
        ('### **two kernels are a combination -- A+**',
         score(HERE, 'It cites `SIDE-kernel` and `SIDE-rcurve`.' + chr(10), FIX_INDEX)[0], 'A+'),
        ('a prose mention of the programme is not a kernel',
         'SIDE-programme' in kernels_named('the SIDE-programme at large'), False),
        ('a document does not cite itself',
         'A_TEST' in str(documents_cited('see `A_TEST`', {'A_TEST': HERE}, HERE)), False),
        ('an unknown name is not a citation',
         len(documents_cited('see `NOT_IN_THE_INDEX`', FIX_INDEX, HERE)), 0),
    ]
    ok = all(g == w for _l, g, w in cases)
    if verbose:
        for lbl, g, w in cases:
            print('      %-62s got %-5s want %-5s %s'
                  % (lbl[:62], str(g)[:5], str(w)[:5], 'ok' if g == w else '### MISMATCH ###'))
    return ok, [dict(case=l, got=str(g), want=str(w)) for l, g, w in cases]


def build_index(root):
    """### **THE DOCUMENT INDEX, READ FROM DISK BY THE CALLER'S ROOT.** ### Never guessed here."""
    idx = {}
    for dp, _dn, fn in os.walk(root):
        if '.git' in dp:
            continue
        for f in fn:
            if f.endswith('.md'):
                rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/')
                idx.setdefault(f[:-3], rel)
    return idx


if __name__ == '__main__':
    ok, log = self_test(True)
    print('  ### ### **SELF-TEST : %s**'
          % ('ALL THREE MARKS REACHABLE, AND THE REJECTIONS HOLD' if ok else '### FAILED'))
    raise SystemExit(0 if ok else 1)
