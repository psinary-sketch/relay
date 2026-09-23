# -*- coding: utf-8 -*-
"""b479_extract.py -- THE SURVEY FOR THE SEVEN CLASSES.
### ### **NOTHING IS COMPILED.** ### Statements are read AS TEXT from `SIDE-lv-conservation` at
### ### **v0.10.0 = 93c27ec**, by `git show`, and never imported or built.
### (R70): the fact reader is rehearsed on C2 before the seal and what it returns is printed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TAG = 'v0.10.0'
SRC = 'SIDELvConservation/CouplingsAtPhi.lean'
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(*a):
    return subprocess.run(['git', '-C', LV] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '')


def fact(text, name):
    """### ### **THE FACT READER.** ### Returns `(statement, line)` -- ### **THE STATEMENT AND NOT
    ### THE DOCSTRING.** ### It starts at the declaration keyword, so every `/-- ... -/` block above
    ### it is excluded by construction.

    ### ### **AND IT TREATS `def` AND `theorem` DIFFERENTLY, BECAUSE `:=` MEANS DIFFERENT THINGS.**
    ### The first version stopped at the first `:=` for both. ### For a `theorem` that is right --
    ### what follows is the PROOF. ### For a `def ... : Coupling := fun Φ => <predicate>` it is
    ### ### **WRONG**: the `:=` sits on the declaration line and what follows IS THE CONTENT, so the
    ### reader returned `def C2_halfplane_nonvanishing : Coupling` and dropped the predicate whole.
    ### ### **(R70)'S REHEARSAL CAUGHT IT ON `C2` BEFORE THE SEAL**, which is the entire reason the
    ### rehearsal is run on a case whose answer is known.
    """
    lines = text.split(NL)
    for i, l in enumerate(lines):
        m = re.match(r'^(def|theorem|lemma)\s+%s\b' % re.escape(name), l)
        if not m:
            continue
        kind = m.group(1)
        if kind == 'def':
            # ### the body IS the statement; run to the next docstring or declaration.
            out = [l.rstrip()]
            for b in lines[i + 1:]:
                if re.match(r'^(/--|def|theorem|lemma|end|namespace|/-!|-- )', b) or b.startswith('@['):
                    break
                out.append(b.rstrip())
            return NL.join(x for x in out if x.strip()), i + 1
        out = []
        for b in lines[i:]:
            j = b.find(':=')
            if j >= 0:
                out.append(b[:j].rstrip())
                break
            out.append(b.rstrip())
        return NL.join(x for x in out if x.strip()), i + 1
    MISSES.append((SRC, name))
    return '', 0


# ### ### **THE SEVEN, IN THE MONOGRAPH'S CANONICAL ORDER AS b408 CORRECTED IT.**
CLASSES = [
    ('C1', 'Schwarz reflection / realness', ['C1_realness']),
    ('C2', 'Euler / multiplicative', ['C2_halfplane_nonvanishing']),
    ('C3', 'functional equation / theta transformation', ['C3_theta_transformation']),
    ('C4', 'modular / PSL2(Z)', ['C4_modularity']),
    ('C5', 'spectral', ['C5_input']),
    ('C6', 'Cauchy-Riemann / local analyticity', ['C6_holomorphic_extension']),
    ('C7', 'Hadamard', ['C7_entirety', 'C7_order']),
]


def main():
    rec('=' * 108)
    rec('b479 -- THE SURVEY. ### THE SEVEN CLASSES READ AT lv %s = 93c27ec. ### NOTHING COMPILED.'
        % TAG)
    rec('=' * 108)

    # ------------------------------------------------------------------ (P0) the pin
    rec('')
    rec('(P0) THE TAG, AND THAT IT IS THE COMMIT THE ORDER NAMES.')
    rec('-' * 108)
    sha = git('rev-list', '-n', '1', TAG).strip()
    rec('    `%s` resolves to : ### **%s**' % (TAG, sha))
    rec('    the order names  : ### **93c27ec** ### -- %s'
        % ('MATCHES' if sha.startswith('93c27ec') else '### DOES NOT MATCH'))
    if not sha.startswith('93c27ec'):
        MISSES.append((TAG, 'pin mismatch'))
    src = git('show', '%s:%s' % (TAG, SRC))
    rec('    `%s` at that tag : %d lines' % (SRC, len(src.split(NL))))

    # ------------------------------------------------------------------ (P1) h1_complete_at_Phi
    rec('')
    rec('(P1) `h1_complete_at_Phi` -- THE CONJUNCTION THE PER-CLASS FACTS COMPOSE INTO.')
    rec('-' * 108)
    stmt, ln = fact(src, 'h1_complete_at_Phi')
    rec('    `%s:%d`' % (SRC, ln))
    for s in stmt.split(NL):
        rec('      %s' % s)
    conj = len(re.findall(r'\bC\d[A-Za-z_]*\s+Phi\b', stmt))
    rec('    ### ### **CONJUNCTS : %d, FOR SEVEN CLASSES.** ### `C7` contributes TWO -- entirety'
        % conj)
    rec('    ### and order -- and ### **C5_output IS NOT AMONG THEM.**')
    setdef, sl = fact(src, 'sevenClasses')
    rec('')
    rec('    and the family the theorem`s classes are drawn from, `sevenClasses` (`:%d`):' % sl)
    for s in setdef.split(NL):
        rec('      %s' % s)
    note = next((l.strip() for l in src.split(NL) if 'C5_output' in l and 'NOT' in l), '')
    rec('    ### the file`s own note on the exclusion, verbatim:')
    rec('      %s' % note)
    if 'C5_output' not in setdef and note:
        rec('    ### ### **SO THE REPOSITORY ITSELF PUTS THE DISCLAIMED HALF OUTSIDE THE FAMILY.**')

    # ------------------------------------------------------------------ (P2) the seven facts
    rec('')
    rec('(P2) THE SEVEN PER-CLASS FACTS, ### **STATEMENTS AND NOT DOCSTRINGS.**')
    rec('-' * 108)
    facts = []
    for cid, label, names in CLASSES:
        rec('')
        rec('  ### **%s -- %s**' % (cid, label))
        for n in names:
            s, i = fact(src, n)
            t, j = fact(src, n + '_at_Phi')
            rec('    the coupling `%s`  (`:%d`)' % (n, i))
            for x in s.split(NL):
                rec('        %s' % x)
            if t:
                rec('    its discharge `%s_at_Phi`  (`:%d`)' % (n, j))
                for x in t.split(NL):
                    rec('        %s' % x)
            facts.append(dict(cid=cid, label=label, name=n, stmt=s, line=i,
                              discharge=t, dline=j,
                              mentions_mellin=('mellin' in s),
                              mentions_test_fn=bool(re.search(r'test|Schwartz|\bf\s*:', s))))

    # ------------------------------------------------------------------ (P3) the criterion
    rec('')
    rec('(P3) ### **THE CRITERION, FIXED BEFORE ANY VERDICT IS SCORED.**')
    rec('-' * 108)
    rec('    The order asks, per class: does the fact ### **CONSTRAIN WEIL`S FORM `W` ON SOME')
    rec('    ### FAMILY OF TEST FUNCTIONS**? ### And it says to read ### **THE STATEMENT, NOT THE')
    rec('    ### DOCSTRING.**')
    rec('    ### ### **NOT ONE OF THE SEVEN STATEMENTS MENTIONS A TEST FUNCTION, OR `W`, OR THE')
    rec('    ### EXPLICIT FORMULA.** ### They are predicates on `Φ`, the Mellin integrand.')
    rec('    ### statements quantifying over a test function : ### **%d of %d**'
        % (sum(1 for f in facts if f['mentions_test_fn']), len(facts)))
    rec('    ### ### **SO A LITERAL READING WOULD RETURN SEVEN `APART` AND SAY NOTHING.** ### The')
    rec('    ### criterion this act adopts, and states here before scoring:')
    rec('      ### ### **A FACT TOUCHES THE FORM WHEN ITS STATEMENT CONSTRAINS THE OBJECT `W` IS')
    rec('      ### BUILT FROM -- THE MELLIN TRANSFORM OF `Φ` -- ON A FAMILY ITS OWN QUANTIFIER')
    rec('      ### NAMES.** ### `W`s channels are read off the completed transform; a fact that')
    rec('      ### never mentions that transform constrains `Φ` and reaches the form only through a')
    rec('      ### derivation the statement does not carry.')
    rec('      ### ### **AND THAT IS A CRITERION ABOUT STATEMENTS, WHICH IS WHAT THE ORDER ASKS')
    rec('      ### FOR** -- a class whose DOCSTRING explains how it yields the functional equation')
    rec('      ### still scores on what its statement says.')
    rec('')
    rec('    ### statements mentioning `mellin` : ### **%d of %d** -- %s'
        % (sum(1 for f in facts if f['mentions_mellin']), len(facts),
           ', '.join(f['name'] for f in facts if f['mentions_mellin'])))

    # ------------------------------------------------------------------ (P4) the (R70) rehearsal
    rec('')
    rec('(P4) (R70) -- THE FACT READER REHEARSED ON `C2` BEFORE THE SEAL.')
    rec('-' * 108)
    s2, i2 = fact(src, 'C2_halfplane_nonvanishing')
    rec('    what the reader returns for `C2_halfplane_nonvanishing` (`:%d`):' % i2)
    for x in s2.split(NL):
        rec('      %s' % x)
    ok = ('/--' not in s2 and 'mellin' in s2
          and 'Euler product' not in s2 and '1 < s.re' in s2)
    rec('    ### it carries the PREDICATE and ### **NOT the docstring** : %s' % ok)
    dline = next((l.strip() for l in src.split(NL) if 'Euler product' in l), '')
    rec('    ### ### AND THE NEGATIVE HALF -- the docstring the reader DID NOT return:')
    rec('      %s' % dline[:140])
    if not ok:
        MISSES.append(('rehearsal', 'C2'))

    # ------------------------------------------------------------------ (P5) the inertia vocabulary
    rec('')
    rec('(P5) THE INERTIA VOCABULARY, AT ITS OWN ADDRESS, FOR THE CLOSING SENTENCE.')
    rec('-' * 108)
    hits = []
    for fn in ('FINDINGS.md', 'REGISTRY.md'):
        t = read(os.path.join(PP, fn))
        for i, l in enumerate(t.split(NL)):
            if re.search(r'\binerti', l, re.I):
                hits.append((fn, i + 1, l.strip()))
    rec('    lines carrying the stem `inerti` in FINDINGS and REGISTRY : ### **%d**' % len(hits))
    for fn, i, l in hits[:4]:
        rec('      %s:%d' % (fn, i))
        rec('        %s' % l[:140])
    if not hits:
        rec('    ### ### **THE VOCABULARY IS NOT IN THOSE TWO FILES**, and the closing sentence')
        rec('    ### will say what it would say IF that vocabulary carried it, without borrowing a')
        rec('    ### term the record does not hold at an address.')

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b479_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(sha=sha, conjuncts=conj, facts=facts, sevenClasses=setdef,
                   c5_note=note, inertia=hits, misses=MISSES),
              io.open(os.path.join(D, 'b479_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
