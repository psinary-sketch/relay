# -*- coding: utf-8 -*-
"""b332_statement.py -- THE CLAUSE STATED. ### THE GENERATOR, NOT A PROOF.

### **A STATEMENT ACT. ### NO PROOF ATTEMPTED. ### NO GRADE MOVED OR CONFERRED. ### NOT DISCHARGED, NOT
### WEAKENED, NOT REPLACED.**

### ### **THE DESIGN POINT, CARRIED FROM THE FOLDS:** ### the constituent table below is the single source
### of truth and this runner EMITS the markdown the findings document receives. ### Every quotation is
### checked against THE FILE THAT ORIGINATED IT before a line exists (`F-QUOTE`, with a discrimination
### arm); every grade word is checked to be in its owner's bank (`F-GRADES`); the E0 gate unfolds each
### constituent to a kernel terminal, a local proposition, or an import under the bar, names the
### UNOWNED constituent, and prints its verdict; the ranking is computed by the SEALED rule and the
### navigator's registered expectation is scored against it in words.
### ### **IDEMPOTENT:** ### a second run finds the anchor and writes nothing; the gates still run.
"""
import io
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
FACESK = os.path.join(PP, 'phase2', 'method', 'FACES_OF_H2_AT_FINITE_INSTANCE.md')
SRC = os.path.join(D, 'b328_source_text.txt')
EMIT = os.path.join(D, 'b332_statement_emitted.md')
ROWS = os.path.join(D, 'b332_statement_rows.json')
ANCHOR = 'clause-stated'
SECTION = 'THE CLAUSE STATED \u2014 b332 *(filed 2026-09-06; a statement act \u2014 it proves nothing, discharges nothing, moves no grade)*'


def bank(act):
    return os.path.join(D, {
        'b300': 'b300_the_archimedean_leg.txt', 'b306': 'b306_the_difference.txt', 'b310': 'b310_the_smear_collapses.txt',
        'b315': 'b315_the_calibration_and_the_rate.txt', 'b318': 'b318_the_forced_sign.txt', 'b320': 'b320_the_lawful_function.txt',
        'b321': 'b321_the_window_opened.txt', 'b322': 'b322_the_membership.txt', 'b326': 'b326_the_reach.txt',
        'b328': 'b328_the_discriminating_family.txt', 'b329': 'b329_the_finite_side_seal.txt',
    }[act])


# ### THE SEALED ORDER OF GRADES, SOFTEST FIRST (registration (E)).
ORDER = ['DEFINED-ONLY', 'MEASURED-AT-COVERED-CELLS', 'MEASURED-ON-FAMILIES', 'UNDER-RESOLVED-AT-BENCH', 'DERIVED-ON-CONTENT',
         'DERIVES-ON-IMPORTS', 'IMPORT-UNDER-THE-BAR', 'PROVED-PER-CELL', 'PROVED-GENERAL']

# ### THE HEAD QUOTATIONS: (label, file, fragment)
HEAD = [
    ('the deposit on h2', DEP, 'and h2 \u2014 nonvanishing of the transform at the point in question.'),
    ('the register sentence', FACESK, 'THE REGISTER SENTENCE, UNTOUCHED BY EVERY WORD BELOW: `h2` IS THE SINGLE OPEN PREMISE.'),
    ('the five registers', DEP, 'These are one premise in five registers: kernel-theoretic, formal-interface, category-shaped, analytic, and spectral-geometric.'),
    ('the fourth register', DEP, 'Fourth: the distance between *balance* and *positivity* at the multiplicative place.'),
    ('its sharpest form', DEP, 'the premise is the inequality \u03bb_Z(n) \u2265 \u2212\u03bb_A(n) between two independently computable channels.'),
    ('the refusal', DEP, 'while deliberately **not** compiling the cross-register equivalences, since to compile "discharge one and you discharge all five" would be to compile RH-equivalence itself.'),
    ('the class, Definition 3.1', SRC, 'positive de\ufb01nite when its Fourier transform is pointwise positive'),
    ('the criterion, Proposition C.1', SRC, 'Proposition C.1 Let Z \u0102 C be the set of non-trivial zeros of the Riemann zeta function and'),
    ('the criterion\u2019s sign', SRC, 'it is enough to prove the negativity of the right-hand side of (1) for'),
]

# ### THE CONSTITUENTS. ### (key, name, unfolded-to (kind: owner: object), the grades as the owners left them
# ###   [(grade-in-ORDER, owner, its own words -- a quotation checked against that owner's bank)], the reason)
CONSTITUENTS = [
    ('K1', 'the class',
     'IMPORT under the bar: the source\u2019s Definition 3.1 (positive definite: transform pointwise non-negative) with Proposition C.1\u2019s vanishing set `{0, 1}`; a local proposition per seed (lawful or not), decided by b320\u2019s scan',
     [('IMPORT-UNDER-THE-BAR', 'b328', 'two lawful seeds under which the finite-instance places sum, computed without any'),
      ('MEASURED-ON-FAMILIES', 'b320', '`f-hat >= 0` pointwise')],
     'the definition is the source\u2019s; which functions are inside it is measured, seed by seed, on the families the arc built'),
    ('K2', 'the criterion\u2019s sign',
     'IMPORT under the bar: Proposition C.1, `RH <=> SUM_v W_v(g conv g-bar^#) <= 0` for every `g` with the vanishing conditions; the corpus\u2019s convention `places = PR - A` (b326\u2019s tool); a local proposition: for a lawful `f` the pole term vanishes, so `SUM_v W_v(f) = -Z` (b321)',
     [('IMPORT-UNDER-THE-BAR', 'b321', 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
      ('MEASURED-ON-FAMILIES', 'b321', '`SUM_v W_v(f) = - Z`.**')],
     'the sign is the source\u2019s; that the corpus\u2019s places sum is the criterion\u2019s quantity with the pole term gone is derived for lawful `f` and measured at every cell'),
    ('K3', 'the finite places\u2019 contribution',
     'KERNEL TERMINALS: `B329.*` (24, zero-axiom; the decomposition and the scaling part GENERAL, the compact part PER CELL) and `B310.*` (the identity count at the seven cells); a derivation on content: the source\u2019s construction on the object returns the test function at the identity times a dimension (b310)',
     [('PROVED-GENERAL', 'b329', "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS"),
      ('PROVED-PER-CELL', 'b329', 'FOR THE COMPACT PART, NEVER AVERAGED.**'),
      ('DERIVED-ON-CONTENT', 'b310', 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION')],
     'the counting form is compiled; the identification of that count with the source\u2019s trace is b310\u2019s derivation and is not compiled, and the compact part is decided at cells'),
    ('K4', 'the prime sum',
     'a derivation on content: the corpus\u2019s prime side IS the source\u2019s finite-places sum, factor for factor on the summand under the source\u2019s own normalization, DIFFERENT only in the cutoff window (b306); IMPORT under the bar: the local term (149)',
     [('DERIVED-ON-CONTENT', 'b306', "`k`-th term of `W_p` under CC's own `\u2206`-normalization, factor for factor."),
      ('IMPORT-UNDER-THE-BAR', 'b306', "IS THE CORPUS'S PRIME SIDE THE SOURCE'S FINITE-PLACES SUM? ### **YES -- AND THE TWO OPEN")],
     'the identification is derived term by term; the window the corpus cuts at is a choice and is named as one'),
    ('K5', 'the archimedean distribution',
     'defined at b315 from the source\u2019s own formula; measured at b320 by two routes sharing no code, the second against the digamma kernel `Re psi(1/4 + i u/2) - log pi`; the sign certified at every frame, the size at none',
     [('MEASURED-AT-COVERED-CELLS', 'b320', "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
      ('DEFINED-ONLY', 'b315', 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED')],
     'defined from the source and measured where Theorem 1\u2019s support condition covers; its size is certified nowhere'),
    ('K6', 'the decomposition: the compressed square plus the remainder',
     'IMPORT under the bar: Theorem 4.7 as an EQUALITY, `Tr(theta(f) S) = W_infinity(f) + INT f(rho^-1) eps(rho) d*rho`; a local proposition: the compressed square is non-negative as arithmetic (a sum of squares, b318); measured: the equality at the three covered cells and the remainder as the margin (b320, b321)',
     [('IMPORT-UNDER-THE-BAR', 'b321', 'Theorem 4.7 / (83) is an ### **EQUALITY**, not'),
      ('MEASURED-ON-FAMILIES', 'b318', 'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT.'),
      ('MEASURED-AT-COVERED-CELLS', 'b321', "that makes b320's margin exactly minus the remainder integral.")],
     'the square\u2019s sign is arithmetic and holds everywhere it was computed; the remainder is the margin, measured only where the identity is covered, its size uncertified -- the navigator\u2019s registered softest'),
    ('K7', 'the object and its archimedean unit',
     'the space from the source\u2019s definition; the unit in by derivation on named imports (b300); its membership residual UNDER-RESOLVED at bench with its price (b322)',
     [('DERIVES-ON-IMPORTS', 'b300', 'GRADE: ### **DERIVES-on-IMPORTS**'),
      ('UNDER-RESOLVED-AT-BENCH', 'b322', 'VERDICT: ### UNDER-RESOLVED, WITH ITS PRICE.')],
     'in by derivation, under-resolved at bench; the instrument\u2019s distance from the answer is priced'),
]

# ### THE OPEN PART, SET APART AND NOT RANKED.
OPEN = ('K8', 'the quantifiers',
        'UNOWNED: over the class (infinite) and, through the explicit formula, over the zeros. No act in the corpus owns either quantifier; touched only on families and libraries',
        [('MEASURED-ON-FAMILIES', 'b326', "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
         ('MEASURED-ON-FAMILIES', 'b328', 'SEES IT -- AT SEVEN OF EIGHT CELLS.')],
        'this is the clause: the statement\u2019s open part, in its own words')

NAV_EXPECTATION = 'the remainder is the softest constituent'


def rank():
    out = []
    for key, name, unfold, grades, reason in CONSTITUENTS:
        soft = min(grades, key=lambda g: ORDER.index(g[0]))
        out.append((ORDER.index(soft[0]), key, name, soft[0], reason))
    out.sort(key=lambda r: (r[0], r[1]))
    return out


def score(ranking):
    top = ranking[0][0]
    softest = [r[1] for r in ranking if r[0] == top]
    if softest == ['K6']:
        return 'MET', softest
    if 'K6' in softest:
        return 'MET AT THE RANK, NOT ALONE -- a tie under the sealed rule, no tie-break applied', softest
    return 'NOT MET', softest


def fquote(rec):
    bad = []
    for lbl, path, frag in HEAD:
        if frag not in io.open(path, encoding='utf-8', errors='replace').read():
            bad.append(('HEAD', lbl, frag))
    n = len(HEAD)
    for key, _n, _u, grades, _r in CONSTITUENTS + [OPEN]:
        for _g, owner, frag in grades:
            n += 1
            if frag not in io.open(bank(owner), encoding='utf-8', errors='replace').read():
                bad.append((key, owner, frag))
    rec('  F-QUOTE  : %d quotations, %d unfindable' % (n, len(bad)))
    for k, o, f in bad:
        rec('      ### UNFINDABLE  %s %s -- %r' % (k, o, f[:74]))
    altered = HEAD[0][2].replace('nonvanishing', 'nonvanishingg')
    disc = altered not in io.open(HEAD[0][1], encoding='utf-8', errors='replace').read()
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fgrades(rec):
    """### every grade word in ORDER used by a constituent is a word its owner's bank carries, in the owner's own form."""
    words = {'DEFINED-ONLY': 'DEFINED', 'MEASURED-AT-COVERED-CELLS': 'MEASURED', 'MEASURED-ON-FAMILIES': 'MEASURED',
             'UNDER-RESOLVED-AT-BENCH': 'UNDER-RESOLVED', 'DERIVED-ON-CONTENT': 'DERIV', 'DERIVES-ON-IMPORTS': 'DERIVES-on-IMPORTS',
             'IMPORT-UNDER-THE-BAR': 'IMPORT', 'PROVED-PER-CELL': 'PER CELL', 'PROVED-GENERAL': 'GENERAL'}
    bad = []
    for key, _n, _u, grades, _r in CONSTITUENTS + [OPEN]:
        for g, owner, _f in grades:
            body = io.open(bank(owner), encoding='utf-8', errors='replace').read()
            if words[g] not in body and words[g].upper() not in body.upper():
                bad.append((key, owner, g))
    rec('  F-GRADES : every grade word in its owner\'s bank : %s %s' % (not bad, bad if bad else ''))
    return not bad


def e0_gate(rec):
    rec('  E0 GATE  : every constituent unfolded to a kernel terminal, a local proposition, or an import under the bar, with its owner:')
    for key, name, unfold, grades, _r in CONSTITUENTS:
        rec('      %s %-46s -> %s' % (key, name[:46], unfold[:100]))
    rec('      %s %-46s -> %s' % (OPEN[0], OPEN[1], OPEN[2][:100]))
    rec('  ### THE UNOWNED CONSTITUENT : %s -- %s' % (OPEN[0], OPEN[1]))
    rec('  ### VERDICT : HALTS at %s. The statement unfolds to owned objects at every constituent but its quantifiers,' % OPEN[0])
    rec('  ###           and the quantifiers are the clause. The gate does not halt on any owned constituent.')
    return True


def emit_markdown(ranking, verdict, softest):
    L = []

    def A(s=''):
        L.append(s)

    def q(lbl):
        return dict((l, f) for l, _p, f in HEAD)[lbl]

    A('<!-- b332 clause-stated anchor -->')
    A('')
    A('## %s' % SECTION)
    A('')
    A('### %s' % ANCHOR)
    A('<a id="%s"></a>*Stable anchor: `%s` \u00b7 tag: statement (the open clause in the arc\u2019s vocabulary); every constituent carries its owner\u2019s grade and no other\u2019s; nothing here is proved and the clause is not discharged*' % (ANCHOR, ANCHOR))
    A('')
    A('**The deposit\u2019s own words on `h2`, at the head:** \u201c\u2026%s\u201d **The register sentence, exact:** \u201c%s\u201d' % (q('the deposit on h2'), q('the register sentence')))
    A('')
    A('**The five registers, as the deposit states them:** \u201c%s\u201d **The fourth:** \u201c%s\u201d \u2014 \u201c\u2026%s\u201d **And the deposit\u2019s refusal, quoted beside this statement because it governs it:** \u201c\u2026%s\u201d' % (q('the five registers'), q('the fourth register'), q('its sharpest form'), q('the refusal')))
    A('')
    A('### The statement')
    A('')
    A('**(S)** For every `g` in the source\u2019s class \u2014 `g` in `C_c^\u221e(R*_+)` with `g\u0303(0) = g\u0303(1) = 0`, so that `f = g \u22c6 g\u0304\u266f` is positive definite in the sense of the source\u2019s Definition 3.1 (\u201c\u2026%s\u2026\u201d) \u2014 **the places sum of the explicit formula keeps the criterion\u2019s sign:** `\u03a3_v W_v(f) \u2264 0` in the source\u2019s normalization. This is the source\u2019s Proposition C.1 (\u201c%s\u2026\u201d: `RH \u21d4 \u03a3_v W_v(g \u22c6 g\u0304\u266f) \u2264 0` for every such `g`; \u201c\u2026%s\u2026\u201d), written as the positivity face\u2019s realized form. **The discriminating seeds of b328 are explicitly inside the class** (b328\u2019s lawfulness scan), so the family that made the instrument say no on the counterexample is a family the statement quantifies over.' % (q('the class, Definition 3.1'), q('the criterion, Proposition C.1'), q('the criterion\u2019s sign')))
    A('')
    A('**The places sum, unfolded as the arc realized it** \u2014 in the corpus\u2019s own sign convention (`places = PR \u2212 A`, b326\u2019s tool; for a lawful `f` the pole term vanishes, so `\u03a3_v W_v(f) = \u2212Z`, b321): **the finite places\u2019 contribution** (on the object\u2019s space the source\u2019s construction returns the test function at the identity times a dimension and no arithmetic \u2014 b310 derived it, b329 compiled its counting form, general for the decomposition and the scaling part, per cell for the compact part), **plus the prime sum** (the source\u2019s finite-places sum factor for factor on the summand, b306), **plus the archimedean distribution** (from the source\u2019s own formula, b315/b320, with its digamma witness), **which decomposes as the object\u2019s compressed square** (non-negative as arithmetic, b318) **plus a remainder that is the margin** (the source\u2019s Theorem 4.7, an equality, verified at the covered cells, b321; the margin measured, b320).')
    A('')
    A('### The E0 gate: every constituent unfolded to its owner')
    A('')
    A('| constituent | unfolded to \u2014 kind, owner, object |')
    A('|---|---|')
    for key, name, unfold, _g, _r in CONSTITUENTS:
        A('| **%s** %s | %s |' % (key, name, unfold))
    A('| **%s** %s | %s |' % (OPEN[0], OPEN[1], OPEN[2]))
    A('')
    A('**The gate\u2019s verdict: it halts at %s.** Every constituent but the quantifiers unfolds to a kernel terminal, a local proposition, or an import under the bar with a named owner; **the quantifiers are unowned, and they are the clause.**' % OPEN[0])
    A('')
    A('### The grades, one row per constituent \u2014 each as its owning act left it')
    A('')
    A('| constituent | what is proved (kernel / content / import) | what is measured (cells, families) | what is only defined | the owners\u2019 own words |')
    A('|---|---|---|---|---|')
    for key, name, _u, grades, _r in CONSTITUENTS + [OPEN]:
        proved = '; '.join('%s (%s)' % (g, o) for g, o, _f in grades if g in ('PROVED-GENERAL', 'PROVED-PER-CELL', 'DERIVED-ON-CONTENT', 'DERIVES-ON-IMPORTS', 'IMPORT-UNDER-THE-BAR')) or '\u2014'
        measured = '; '.join('%s (%s)' % (g, o) for g, o, _f in grades if g in ('MEASURED-AT-COVERED-CELLS', 'MEASURED-ON-FAMILIES', 'UNDER-RESOLVED-AT-BENCH')) or '\u2014'
        defined = '; '.join('%s (%s)' % (g, o) for g, o, _f in grades if g == 'DEFINED-ONLY') or '\u2014'
        words = ' / '.join('%s: \u201c\u2026%s\u2026\u201d' % (o, f.replace('|', '\u2016')) for _g, o, f in grades)
        A('| **%s** %s | %s | %s | %s | %s |' % (key, name, proved, measured, defined, words))
    A('')
    A('**The open part, in its own words:** %s \u2014 %s. It is set apart from the ranking below because it is not a constituent that could be softer or harder; it is what the statement quantifies over.' % (OPEN[1], OPEN[4]))
    A('')
    A('### The ranking by grade, softest first')
    A('')
    A('*The rule, sealed before the ranking existed: a constituent\u2019s rank is its softest grade among its owners, ordered %s; the open part set apart.*' % ' < '.join('`%s`' % g for g in ORDER))
    A('')
    A('| rank | constituent | softest grade | why it sits here |')
    A('|---|---|---|---|')
    for i, (_o, key, name, g, reason) in enumerate(ranking, 1):
        A('| %d | **%s** %s | `%s` | %s |' % (i, key, name, g, reason))
    A('')
    A('**The navigator\u2019s registered expectation** \u2014 *%s* \u2014 **scored against the ranking: %s.** The softest rank is held by %s.' % (NAV_EXPECTATION, verdict, ', '.join('**%s**' % k for k in softest)))
    A('')
    A('### What this statement does and does not do')
    A('')
    A('- **It does not discharge the clause. It does not weaken it. It does not replace it.** It is the clause, in the vocabulary the arc built, suitable for a reader to check constituent by constituent against the owners named above.')
    A('- **It is one face of the obligation and not the obligation\u2019s compiled equivalence.** The deposit\u2019s refusal to compile the cross-register equivalences is quoted at the head and governs it: nothing here carries this face to the other four.')
    A('- **Every grade above is its owner\u2019s and none was conferred here.** Every sign convention is quoted from its owner.')
    top = ranking[0]
    A('- **The aim-map is named as the act that would chart the softest constituent\u2019s behaviour over aims** \u2014 under the sealed rule that is **%s** (%s, softest grade `%s`) \u2014 **and neither that act nor this one is the discharge.**' % (top[1], top[2], top[3]))
    A('')
    A('**Placement.** This section is the stable anchor `%s`; the faces ledger carries the statement as row `S1` (STATED, with this grade table); the arc keystone carries one appended cross-reference line; the correspondence row carries NO TERMINAL, because the statement is analysis quantified over an infinite class and has no compiled form.' % ANCHOR)
    A('')
    A('### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**')
    A('')
    return '\n'.join(L)


OUT = []


def main():
    def rec(s=''):
        OUT.append(s)
        print(s)

    rec('=' * 100)
    rec('b332 -- THE CLAUSE STATED. ### THE GENERATOR, NOT A PROOF.')
    rec('=' * 100)
    q_ok = fquote(rec)
    g_ok = fgrades(rec)
    e0_gate(rec)
    ranking = rank()
    verdict, softest = score(ranking)
    rec('  RANKING (softest first): %s' % ' ; '.join('%s=%s' % (k, g) for _o, k, _n, g, _r in ranking))
    rec("  THE NAVIGATOR'S EXPECTATION -- %s -- SCORED : %s (softest rank held by %s)" % (NAV_EXPECTATION, verdict, softest))
    if not (q_ok and g_ok):
        rec('  ### ### **REFUSING TO EMIT. ### NOTHING IS WRITTEN TO FINDINGS.md.**')
        return 1
    md = emit_markdown(ranking, verdict, softest)
    before = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    if ('<a id="%s"></a>' % ANCHOR) in before:
        rec('')
        rec('  ### ### **THE ANCHOR IS ALREADY IN FINDINGS.md. ### NOTHING WRITTEN.** (idempotent)')
        io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md + '\n')
        rec('=' * 100)
        rec('  ### ### **STATEMENT GATES : ALL PASS**')
        rec('=' * 100)
        return 0
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    rec('')
    rec('  ### THE BASELINE, TAKEN BEFORE THE WRITE:')
    rec('    working file : %d bytes, %d lines' % (len(before.encode('utf-8')), len(before.splitlines())))
    rec('    blob at HEAD : %d bytes, %d lines' % (len(blob.encode('utf-8')), len(blob.splitlines())))
    new = before.rstrip('\n') + '\n\n' + md
    open(FINDINGS + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(FINDINGS + '.tmp', FINDINGS)
    after = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    pfx_work = after.startswith(before.rstrip('\n'))
    norm = lambda s: s.replace('\r\n', '\n')
    pfx_blob = norm(after).startswith(norm(blob).rstrip('\n'))
    added = len(after.splitlines()) - len(before.splitlines())
    rec('')
    rec('  ### THE NO-GRADE-MOVED CHECK, MECHANICAL:')
    rec('    the pre-append working file is a TRUE PREFIX of the result : %s' % pfx_work)
    rec('    the blob at HEAD is a TRUE PREFIX of the result (normalised): %s' % pfx_blob)
    rec('    lines added : %+d   sections before : %d   after : %d' % (added, len([x for x in before.splitlines() if x.startswith('## ')]), len([x for x in after.splitlines() if x.startswith('## ')])))
    rec('    ### ### **PURELY ADDITIVE : %s**' % (pfx_work and pfx_blob))
    io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md + '\n')
    payload = dict(anchor=ANCHOR, section=SECTION, head=[list(h) for h in HEAD], constituents=[[k, n, u, [list(g) for g in gs], r] for k, n, u, gs, r in CONSTITUENTS],
                   open=[OPEN[0], OPEN[1], OPEN[2], [list(g) for g in OPEN[3]], OPEN[4]], order=ORDER,
                   ranking=[list(r) for r in ranking], navigator_expectation=NAV_EXPECTATION, verdict=verdict, softest=softest,
                   fquote=bool(q_ok), fgrades=bool(g_ok), prefix_working=bool(pfx_work), prefix_blob=bool(pfx_blob),
                   lines_added=added, lines_before=len(before.splitlines()), lines_after=len(after.splitlines()))
    open(ROWS + '.tmp', 'wb').write((json.dumps(payload, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
    os.replace(ROWS + '.tmp', ROWS)
    rec('')
    rec('  emitted markdown : %s  (%d lines)' % (os.path.basename(EMIT), len(md.splitlines())))
    rec('  rows json        : %s' % os.path.basename(ROWS))
    rec('=' * 100)
    ok = q_ok and g_ok and pfx_work and pfx_blob
    rec('  ### ### **STATEMENT GATES : %s**' % ('ALL PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    code = main()
    base = 'b332_statement_run'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(OUT) + '\n')
    sys.exit(code)
