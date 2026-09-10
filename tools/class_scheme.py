# -*- coding: utf-8 -*-
"""class_scheme.py -- THE BOTH-SCHEME CLASS MATCHER, built b409 by RULING (R25).

### ### **WHY THIS EXISTS.** ### The corpus numbers its seven mechanism classes in ### **TWO**
### ways, and they disagree on six of seven symbols. ### `b408` found the disagreement by meeting
### it: two documents used the corollary's own channel vocabulary about `C3`, and the `C3` they
### meant was not the `C3` the reader would have assumed. ### **A SYMBOL MATCHED WITHOUT ITS SCHEME
### ### IS NOT A CLASS; IT IS TWO CHARACTERS.**
###
### ### **(R25), THE AUTHOR'S:** ### both numberings are kept, every document declares which it
### uses, ### **NO SYMBOL IS RENUMBERED ANYWHERE**, and ### **THE MATCHER READS BOTH SCHEMES AND
### ### PRINTS WHICH IT MATCHED.**
###
### ### **THE TWO SCHEMES, BY THEIR OWN CONTENT AND NOT BY A COINED NAME.**
### ### **THE STAGE INDEX** ### -- attested by the monograph's own class table and, independently,
### ### by `ENUMERA.md`'s canonical-numbering reconciliation:
###     `C1` Schwarz / additive · `C2` Euler / multiplicative · `C3` functional equation ·
###     `C4` modular / PSL2 · `C5` spectral · `C6` Cauchy-Riemann · `C7` Hadamard.
### ### **THE EXCLUSION-ORDER INDEX** ### -- attested by the documents that use it, and tabulated
### ### (as the *Monograph* column) in `Seven_Mechanism_Classes.md`'s own correspondence remark:
###     `C1` functional equation · `C2` additive / reality · `C3` Cauchy-Riemann ·
###     `C4` Euler / multiplicative · `C5` modular / PSL2 · `C6` spectral · `C7` Hadamard.
###
### ### ### **THE REACH, STATED HERE SO THE TOOL IS NOT TRUSTED BEYOND IT.**
### ### ### **IT RESOLVES A SYMBOL ONLY WHEN IT IS TOLD THE SCHEME, OR WHEN THE TEXT PINS IT.** ###
### ### A bare `C4` in a document that declares nothing is ### **NOT RESOLVABLE**, and this returns
### ### `None` rather than a guess. ### **A MATCHER THAT GUESSES WHEN IT CANNOT KNOW IS THE DEFECT
### ### ### `b408` MET, NOT THE CURE FOR IT.**
### ### ### **AND IT DECIDES A DOCUMENT'S SCHEME BY CONTENT, NEVER BY PROVENANCE.** ### Which
### ### document a symbol sits in says nothing; what the document says the symbol IS says everything.
"""
import io
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STAGE = {1: 'Schwarz / additive', 2: 'Euler / multiplicative', 3: 'functional equation',
         4: 'modular / PSL2', 5: 'spectral', 6: 'Cauchy-Riemann', 7: 'Hadamard'}
EXCLUSION = {1: 'functional equation', 2: 'additive / reality', 3: 'Cauchy-Riemann',
             4: 'Euler / multiplicative', 5: 'modular / PSL2', 6: 'spectral', 7: 'Hadamard'}
SCHEMES = {'STAGE': STAGE, 'EXCLUSION-ORDER': EXCLUSION}

# ### The content patterns, one per meaning. ### **THE MEANINGS ARE SHARED; ONLY THE NUMBERS MOVE.**
MEANING = {
    'Schwarz / additive': r'Schwarz|additive|reality',
    'Euler / multiplicative': r'Euler|multiplicativ',
    'functional equation': r'functional[- ]equation|archimedean',
    'modular / PSL2': r'PSL|modular',
    'spectral': r'spectral',
    'Cauchy-Riemann': r'Cauchy|local analytic',
    'Hadamard': r'Hadamard',
    'additive / reality': r'Schwarz|additive|reality',
}
SYM = re.compile(r'C([₁-₇])')
SUB = {'₁': 1, '₂': 2, '₃': 3, '₄': 4, '₅': 5, '₆': 6, '₇': 7}
DECL = re.compile(r'CLASS-NUMBERING SCHEME: (STAGE|EXCLUSION-ORDER)')


def resolve(sym, scheme):
    """### The MEANING of a symbol under a NAMED scheme, or `None` if the scheme is not given.

    ### ### **THE RETURN CARRIES THE SCHEME IT MATCHED UNDER**, because `(R25)` requires the
    ### matcher to print which one it used and a bare meaning would not say.
    """
    n = SUB.get(sym[-1]) if isinstance(sym, str) and sym[-1] in SUB else (
        sym if isinstance(sym, int) else None)
    if n is None or scheme not in SCHEMES:
        return None
    return dict(symbol='C%d' % n, scheme=scheme, meaning=SCHEMES[scheme][n])


def declared_scheme(text):
    """### The scheme a document DECLARES in a head note, or `None`. ### `(R25)`'s own mechanism."""
    m = DECL.search(text or '')
    return m.group(1) if m else None


def pin(text, tight=True, window=40):
    """### Decide a text's scheme BY CONTENT: for each symbol, which scheme's meaning follows it.

    ### ### **TIGHT STOPS AT THE NEXT SYMBOL**, because a document listing its classes in a row
    ### gives every symbol its neighbour's content otherwise -- the artefact `b409` printed rather
    ### than reported. ### Returns `(stage_hits, exclusion_hits, evidence)`.
    """
    st = ex = 0
    ev = []
    for m in SYM.finditer(text or ''):
        n = SUB[m.group(1)]
        rest = text[m.end():m.end() + window]
        if tight:
            nxt = SYM.search(rest)
            if nxt:
                rest = rest[:nxt.start()]
        hit_s = re.search(MEANING[STAGE[n]], rest, re.I)
        hit_e = re.search(MEANING[EXCLUSION[n]], rest, re.I)
        if hit_s and not hit_e:
            st += 1
            if len(ev) < 3:
                ev.append(('STAGE', (m.group(0) + rest).replace(chr(10), ' ')[:56]))
        elif hit_e and not hit_s:
            ex += 1
            if len(ev) < 3:
                ev.append(('EXCLUSION-ORDER', (m.group(0) + rest).replace(chr(10), ' ')[:56]))
    return st, ex, ev


def scheme_of(text):
    """### The scheme of a text: its DECLARATION first, then its content, then `None`.

    ### ### **`None` IS A VERDICT AND NOT A FAILURE.** ### `(R25)` marks such a document
    ### `SCHEME UNDECLARED` and ### **ROUTES IT, RATHER THAN GUESSING.**
    """
    d = declared_scheme(text)
    if d:
        return d, 'DECLARED in a head note'
    st, ex, _ev = pin(text)
    if st > ex:
        return 'STAGE', 'pinned by content, %d against %d' % (st, ex)
    if ex > st:
        return 'EXCLUSION-ORDER', 'pinned by content, %d against %d' % (ex, st)
    if st == ex == 0:
        return None, 'SCHEME UNDECLARED -- no symbol is pinned by its own text'
    return None, 'TIED -- %d against %d, and a tie is not a reading' % (st, ex)


def self_test(verbose=True):
    """### THE FIXTURES, BOTH POLARITIES. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.**"""
    ok = True

    def say(s):
        if verbose:
            print(s)

    # ### (1) POSITIVE, SCHEME ONE: the same symbol resolves to the STAGE meaning.
    r1 = resolve('C₄', 'STAGE')
    a1 = r1 and r1['meaning'] == 'modular / PSL2' and r1['scheme'] == 'STAGE'
    say('    (1) C4 under the STAGE index      -> %-24s %s'
        % (r1['meaning'] if r1 else None, 'PASS' if a1 else '### FAIL ###'))
    ok = ok and bool(a1)
    # ### (2) POSITIVE, SCHEME TWO: the SAME symbol resolves to a DIFFERENT meaning.
    r2 = resolve('C₄', 'EXCLUSION-ORDER')
    a2 = r2 and r2['meaning'] == 'Euler / multiplicative'
    say('    (2) C4 under the EXCLUSION index  -> %-24s %s'
        % (r2['meaning'] if r2 else None, 'PASS' if a2 else '### FAIL ###'))
    ok = ok and bool(a2)
    # ### (3) THE OTHER POLARITY: no scheme given, and it REFUSES rather than guessing.
    r3 = resolve('C₄', None)
    a3 = r3 is None
    say('    (3) C4 with NO scheme given       -> %-24s %s'
        % ('REFUSED (None)' if a3 else r3, 'PASS' if a3 else '### FAIL ###'))
    ok = ok and a3
    # ### (4) THE DISCRIMINATION ARM: the two schemes DISAGREE on this symbol, and the tool says so.
    a4 = bool(r1) and bool(r2) and r1['meaning'] != r2['meaning']
    say('    (4) and the two readings DIFFER   -> %-24s %s'
        % ('%s vs %s' % (r1['meaning'][:9], r2['meaning'][:9]) if a4 else 'same',
           'PASS' if a4 else '### FAIL ###'))
    ok = ok and a4
    # ### (5) A text that PINS itself is read from its content, under each scheme in turn.
    t_stage = 'C₃ (functional equation) and C₄ (Modular/PSL₂)'
    t_excl = 'C₁ — Functional equation. C₄ — Euler product.'
    s5, w5 = scheme_of(t_stage)
    s6, w6 = scheme_of(t_excl)
    a5 = s5 == 'STAGE' and s6 == 'EXCLUSION-ORDER'
    say('    (5) content pins each text        -> %-10s / %-16s %s'
        % (s5, s6, 'PASS' if a5 else '### FAIL ###'))
    ok = ok and a5
    # ### (6) THE OTHER POLARITY AGAIN: a text with a bare symbol is UNDECLARED, not guessed.
    s7, w7 = scheme_of('the C₄ obstruction is discussed at length below')
    a6 = s7 is None and 'UNDECLARED' in w7
    say('    (6) a bare symbol is UNDECLARED   -> %-24s %s'
        % (w7[:24], 'PASS' if a6 else '### FAIL ###'))
    ok = ok and a6
    # ### (7) A DECLARATION OVERRIDES CONTENT-PINNING, which is the whole point of (R25).
    s8, w8 = scheme_of('CLASS-NUMBERING SCHEME: EXCLUSION-ORDER' + chr(10)
                       + 'C₃ (functional equation)')
    a7 = s8 == 'EXCLUSION-ORDER' and 'DECLARED' in w8
    say('    (7) a head-note declaration wins  -> %-24s %s'
        % (s8, 'PASS' if a7 else '### FAIL ###'))
    ok = ok and a7
    return ok


if __name__ == '__main__':
    print('class_scheme.py -- self-test (both polarities on every arm):')
    sys.exit(0 if self_test() else 1)
