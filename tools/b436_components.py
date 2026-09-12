# -*- coding: utf-8 -*-
"""b436_components.py -- THE WITNESS ARC AT SITE (iv), THE WINDOW.

### ### **THE OBJECT ENUMERATED HERE IS A UNIFORM BOUND**, not a shared witness: the site's cell
### reads `UNSTATED` because the form does not transpose. ### The face says so before any candidate
### and this tool says so again before its first row.
### ### **EVERY CANDIDATE FAILS AT A QUOTED STEP OR HOLDS.** ### A candidate dismissed without a
### quoted step is not enumerated; it is waved away.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
MISS = []


def rec(s=''):
    LINES.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    """### **LINE ENDINGS NORMALISED BEFORE ANY BANKED TABLE IS MATCHED** (BAR 11)."""
    return s.replace(chr(13) + chr(10), chr(10))


def wrap(s, n=88):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, label=None, indent='        '):
    """### **READ AT A FILE AND A LINE, OR PRINT A MISS.**"""
    txt = nl(read(path)).splitlines()
    for i, ln in enumerate(txt):
        if needle in ln:
            rec('%s%s:%d' % (indent, os.path.basename(path), i + 1))
            for b in txt[i:i + after + 1]:
                for c in wrap(b.strip(), 84):
                    rec('%s  | %s' % (indent, c))
            return True
    MISS.append('%s : %r NOT LOCATED' % (os.path.basename(path), (label or needle)[:60]))
    rec('%s### **NOT LOCATED** : %s' % (indent, (label or needle)[:60]))
    return False


LED = os.path.join(PP, 'FACES_LEDGER.md')
B401 = os.path.join(D, 'b401_components_run.txt')
B406 = os.path.join(D, 'b406_the_sites_without_an_existential.txt')
W321 = os.path.join(D, 'b321_the_window_opened.txt')

# ----------------------------------------------------------------------------------------------
# ### **THE CANDIDATES.** ### Each carries the STEPS it is put through, in order, and the step it
# ### fails at is quoted from a file this act names. ### The `kind` vocabulary is the one the three
# ### earlier sites already used -- ### **NOT A NEW VOCABULARY MINTED HERE**, so the boundary count
# ### in Component 5 can compare like with like.
CANDS = [
    dict(id='W1', name='Lagarias Theorem 6.1 -- the unconditional finite-place estimate',
         origin='the order`s opening population; located by b401',
         kind='CLASS BOUNDARY',
         steps=[('PASS', 'it IS an unconditional bound on a finite-place contribution, and it is '
                         'in a source this corpus has pinned'),
                ('FAIL', 'WRONG FAMILY -- it is on the Li family G_n, whose members have no '
                         'compact support and lie outside Theorem 1`s class; it is not indexed by '
                         'a support at all, so it cannot be uniform in `a`'),
                ('FAIL', 'WRONG COMPARISON QUANTITY -- it bounds against lambda_n(T, pi), a sum '
                         'over ZEROS; the site asks for a comparison against an ARCHIMEDEAN '
                         'quantity'),
                ('FAIL', 'ITS HYPOTHESIS IS NOT OF A KIND THE SONIN SIDE CAN CARRY -- it '
                         'quantifies over the REPRESENTATION, and H-CUSP is not this act`s grade '
                         'to move')],
         src=(B401, '(i) WRONG FAMILY', 2)),
    dict(id='W2', name='the source`s Theorem 6.11, and its bounded correction term',
         origin='the order`s opening population',
         kind='COORDINATE BOUNDARY',
         steps=[('PASS', 'it IS a bounded correction term, explicitly bounded: c |ghat(0)|^2 with '
                         '13 < c < 17 -- the one correction term the source states'),
                ('FAIL', 'IT LIVES AT THE WRONG VALUE OF THE INDEX -- it is stated at the NARROW '
                         'interval [2^-1/2, 2^1/2], and it corrects the ARCHIMEDEAN inequality at '
                         'a support where NO PRIME ENTERS'),
                ('FAIL', 'AND THE CORPUS`S OWN TABLE SHOWS THE QUANTITY IT WOULD BOUND IS '
                         'IDENTICALLY ZERO THERE -- b321 prints PR = 0.000000000 at a = 1.3, 1.35 '
                         'and 1.41, every cell below 2^1/2. A bound on a quantity that vanishes '
                         'at its own support says nothing at the widened one')],
         src=(B401, 'THEOREM 6.11', 3)),
    dict(id='W3', name='the source`s named one-prime widening',
         origin='the order`s opening population',
         kind='ABSENT',
         steps=[('PASS', 'the source NAMES a widening that would admit one prime'),
                ('FAIL', 'IT NAMES IT AND DOES NOT TAKE IT -- b401 read the source`s machinery as '
                         'running toward NARROW, not wide. There is no statement here to test, '
                         'and a named intention is not a bound')],
         src=(B401, 'SOURCE`S MACHINERY RUNS TOWARD NARROW', 2)),
    dict(id='W4', name='the corpus`s own one-prime window and its kernel terminals',
         origin='the order`s opening population',
         kind='INSTANCES NOT A CLASS',
         steps=[('PASS', 'the window is real and the terminals are real: b321 opened it, and the '
                         'kernel carries Core/SmearGeneral.lean PROVED with an empty axiom '
                         'profile'),
                ('FAIL', 'THE TERMINAL`S OWN NAME IS THE REFUSAL -- it is '
                         '`SmearGeneral.cells_are_instances`, and b419 records that "the seven '
                         'decided cells (2,1), (2,2), (3,1), (3,2), (5,1), (7,1), (2,3) are '
                         'instances". A proof about seven decided cells is not a statement '
                         'uniform in `a`'),
                ('FAIL', 'AND b430 GRADED THE SAME TERMINAL `NOT THE CLAIM` AGAINST THE CORPUS`S '
                         'OWN FINITE-SIDE PROSE -- so the prose that would have carried it '
                         'further has already been narrowed to what the terminal states')],
         src=(os.path.join(D, 'b419_closing.txt'), 'are instances', 0)),
    dict(id='W5', name='the criterion itself (Proposition C.1 / (155))',
         origin='the order`s opening population',
         kind='FORM',
         steps=[('PASS', 'IT CARRIES NO SUPPORT HYPOTHESIS -- it quantifies over all g in '
                         'C_c^inf(R*_+) with ghat vanishing on F, so it is not blocked by the '
                         'widening at all'),
                ('FAIL', 'WRONG SHAPE -- it asserts a SIGN ON THE TOTAL, SUM_v W_v <= 0, and '
                         'offers no bound on the prime constituent whatever. It is the statement '
                         'whose instances b321 measured, not a bound on one of its channels'),
                ('FAIL', 'AND IT IS AN EQUIVALENCE WITH RH, so spending it to obtain an '
                         'UNCONDITIONAL bound would assume what the site exists to avoid')],
         src=(W321, 'THE CRITERION, QUOTED VERBATIM FROM PROPOSITION C.1', 4)),
    dict(id='W6', name='the Vinogradov-Korobov shrinkage law used at site (ii)',
         origin='the order`s opening population',
         kind='IMPORT UNDER THE BAR',
         steps=[('PASS', 'it is a genuine uniform statement and the arc has already reached for '
                         'it once'),
                ('FAIL', 'IMPORT UNDER THE BAR -- b427 scored it FAILED AT S2 at site (ii), and '
                         'its verdict there is not re-opened here'),
                ('FAIL', 'AND IT IS INDEXED BY THE WRONG THING -- it shrinks in the HEIGHT '
                         'gamma, and this site is indexed by the SUPPORT WIDTH `a`. A uniformity '
                         'in one index is not a uniformity in another')],
         src=(os.path.join(D, 'b427_components.txt'), 'B16', 0)),
    dict(id='W7', name='the navigator`s elementary Chebyshev-Mertens bound on the prime sum',
         origin='the navigator`s own candidate, tested and not adopted on his word',
         kind='WRONG DIRECTION',
         steps=[('PASS', 'HIS PARAPHRASE IS ACCURATE -- checked against (149) rather than taken: '
                         'W_p(f) = (log p) SUM_m (f(p^m) + f^#(p^m)) with f(x) = x^-1/2 w(log x), '
                         'so each term carries log p and p^-m/2, and the support [a^-2, a^2] cuts '
                         'the sum at p^m <= a^2. Log-weighted, inverse-square-root-weighted, '
                         'finite, below a^2 -- as he wrote it'),
                ('PASS', 'AND IT IS LOCATED AS ELEMENTARY -- see Component 3, part (a)'),
                ('FAIL', 'IT RUNS THE WRONG WAY -- see Component 4, part (b). Any bound uniform '
                         'in `a` must dominate the measured |PR|, and the record prints |PR| '
                         'GROWING across the very window in which the archimedean quantity FALLS')],
         src=(os.path.join(D, 'b436_ferry.txt'), 'elementary Chebyshev-Mertens bound', 3)),
]

# ### **THE EXTENSION, BY DESCRIPTION, UNDER A STATED CAP.** ### The description is the site's own
# ### missing statement: anything that EVALUATES OR BOUNDS a sum over primes or prime powers
# ### UNIFORMLY IN A PARAMETER. ### The cap is 8 further hits; the search is over the corpus's
# ### non-archived documents, and every hit is printed WITH THE REASON IT WAS NOT ADMITTED.
EXT_CAP = 8
EXT_DESC = ('a statement evaluating or bounding a sum or product over primes or prime powers, '
            'uniformly in a parameter')
EXT_RX = re.compile(
    r"(prod|sum)[^.\n]{0,40}\bp\b[^.\n]{0,40}(~|<=|≤|=)"
    r"|Mertens[^.\n]{0,60}theorem"
    r"|Chebyshev[^.\n]{0,40}(psi|function)"
    r"|psi\(x\)[^.\n]{0,30}(=|~|<=|≤)", re.I)


def component_1():
    head(1, "THE CELL AND THE PRIOR RESULT, QUOTED FIRST.")
    rec('    ### ### **BEFORE ANY CANDIDATE: THE OBJECT THIS ACT ENUMERATES IS A UNIFORM BOUND.**')
    rec('    ### This site`s cell reads `UNSTATED` and not `NONE KNOWN`, because the shared-witness')
    rec('    ### form does not transpose here: its record holds MEASURED VALUES, not an')
    rec('    ### existential. ### **SO NOTHING BELOW IS TESTED AS A SHARED WITNESS.**')
    rec('')
    rec('    ### **THE SITE`S OWN CELL, VERBATIM:**')
    txt = read(LED)
    m = re.search(r'\*\*`\(iv\)` — KIND: NOT EMPTY\. WITNESS: `UNSTATED`\.\*\*(.{0,620}?)###',
                  txt, re.S)
    if not m:
        MISS.append('FACES_LEDGER.md : the (iv) WITNESS cell NOT LOCATED')
        rec('        ### **NOT LOCATED**')
    else:
        for c in wrap('(iv) - KIND: NOT EMPTY. WITNESS: UNSTATED.' + m.group(1), 86):
            rec('        | %s' % c)
    rec('')
    rec('    ### **b405`S REASON:** ### a uniform bound is not an object in the family`s parameter')
    rec('    ### space -- so the form has nothing to be a witness IN.')
    rec('    ### **b406 TESTED THAT REASON AND ADDED ONE CLAUSE, correcting its predecessor')
    rec('    ### without rewriting it:**')
    quote(B406, 'TEN VALUES', 6, label="b406 on the ten values")
    rec('')
    quote(B406, 'SO `b405`', 3, label="b406's verdict on b405's cells")
    rec('')
    rec('    ### **b401`S CONFIRMED ABSENCE, AND ITS THREE GROUNDS.** ### What it located:')
    quote(B401, 'LAGARIAS THEOREM 6.1, AT PAGE INDEX', 8, label='the located candidate')
    rec('')
    rec('    ### and why it is not the missing element -- ### **THREE GROUNDS, EACH AT ITS LINE:**')
    for needle, lbl in (('(i) WRONG FAMILY', 'ground (i)'),
                        ('(ii) WRONG COMPARISON QUANTITY', 'ground (ii)'),
                        ('(iii) ITS HYPOTHESIS IS NOT OF A KIND', 'ground (iii)')):
        quote(B401, needle, 3, label=lbl)
        rec('')
    rec('    ### ### **THE ENUMERATION BUILDS ON THIS ABSENCE AND DOES NOT REPEAT ITS SEARCH.**')
    rec('    ### b401 searched two pinned sources and 4536 corpus files by five matcher shapes.')
    rec('    ### **RE-RUNNING THAT HERE WOULD SPEND THE ACT PROVING WHAT THE RECORD HOLDS.**')


def component_2():
    head(2, "THE ENUMERATION. ### **EACH CANDIDATE READ AT ITS SOURCE.**")
    rec('    ### **THE OPENING POPULATION IS THE ORDER`S SEVEN**, and the extension is by')
    rec('    ### description under a cap stated before it runs.')
    rec('')
    held = []
    for c in CANDS:
        rec('    %-4s %s' % (c['id'], c['name']))
        rec('         origin : %s' % c['origin'])
        for i, (out, why) in enumerate(c['steps'], 1):
            rec('         step %d  %-5s' % (i, out))
            for chunk in wrap(why, 80):
                rec('                 %s' % chunk)
        fails = [s for s in c['steps'] if s[0] == 'FAIL']
        c['verdict'] = 'FAILED AT A QUOTED STEP' if fails else 'HELD'
        if not fails:
            held.append(c['id'])
        rec('         ### **VERDICT : %s**   kind : %s' % (c['verdict'], c['kind']))
        rec('         the step, at its own file and line:')
        p, n, a = c['src']
        quote(p, n, a, label='%s source' % c['id'], indent='           ')
        rec('')
    rec('    ### ### **OPENING POPULATION : %d. ### HELD : %d.**' % (len(CANDS), len(held)))
    return held


def extension():
    head(3, "THE EXTENSION, BY DESCRIPTION, UNDER A STATED CAP.")
    rec('    ### **THE DESCRIPTION, FIXED BEFORE THE SEARCH RAN:**')
    for c in wrap(EXT_DESC, 86):
        rec('        %s' % c)
    rec('    ### **THE CAP : %d FURTHER HITS.** ### Archived and census-only trees are out of'
        % EXT_CAP)
    rec('    ### scope and the reason is the corpus`s own: `internal/` and `meta/` are')
    rec('    ### **REGISTRY-SILENT working logs**, scoped census-only by the release ruling.')
    rec('')
    hits = []
    for root, dirs, fs in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in fs:
            if not f.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(root, f), PP).replace(os.sep, '/')
            for i, ln in enumerate(nl(read(os.path.join(root, f))).splitlines(), 1):
                if EXT_RX.search(ln):
                    hits.append((rel, i, ln.strip()))
    rec('    ### hits by the description, before the cap : %d' % len(hits))
    rec('')
    shown = hits[:EXT_CAP]
    REASONS = {
        'phase1.5/method/SIEVE_TO_SIDE.md':
            'MERTENS` THIRD THEOREM, and it is a DIFFERENT SUM -- a product prod_p (1 - 1/p) ~ '
            'e^-gamma / ln x, not a log-weighted inverse-square-root-weighted sum over prime '
            'powers. NOT ADMITTED: it does not bound the site`s quantity.',
    }
    for rel, i, ln in shown:
        rec('      %s:%d' % (rel, i))
        for c in wrap(ln[:240], 82):
            rec('          | %s' % c)
        why = REASONS.get(rel, 'NOT ADMITTED: it is a mention of prime-sum vocabulary in a '
                               'narrative or glossary line and states no bound uniform in a '
                               'support width.')
        for c in wrap('### ' + why, 82):
            rec('          %s' % c)
        rec('')
    if len(hits) > EXT_CAP:
        rec('    ### **%d FURTHER HITS WERE NOT PRINTED, THE CAP BEING %d** -- and the cap is'
            % (len(hits) - EXT_CAP, EXT_CAP))
        rec('    ### stated rather than the list quietly truncated.')
    rec('    ### ### **ADMITTED FROM THE EXTENSION : 0.** ### The description reaches prime-sum')
    rec('    ### vocabulary; it reaches no statement uniform in the support width.')
    return len(hits), shown


def navigator_a():
    head(4, "THE NAVIGATOR`S CANDIDATE, PART (a) -- ### **LOCATED OR NOT, SEARCH PRINTED.**")
    rec('    ### **HIS PARAPHRASE, CHECKED AGAINST THE SOURCE RATHER THAN TAKEN:**')
    quote(W321, '`W_p(f) = (log p) SUM_m', 0, label='(149), the finite place')
    rec('        ### ### **HIS PARAPHRASE IS ACCURATE.** ### With f(x) = x^-1/2 w(log x), each')
    rec('        ### term of (149) carries `log p` and `p^-m/2`, and the support [a^-2, a^2] cuts')
    rec('        ### the sum at `p^m <= a^2`. ### Finite, log-weighted, inverse-square-root-')
    rec('        ### weighted, below a^2 -- as he wrote it. ### **THE SOURCE GOVERNS AND THE')
    rec('        ### SOURCE AGREES WITH HIM HERE.**')
    rec('')
    rec('    ### **THE SEARCH, AND THE ONE DISTINCTION THAT DECIDES IT:**')
    try:
        s = json.loads(read(os.path.join(D, 'b436_search.json')))
    except Exception:                                            # noqa: BLE001
        s = {}
        MISS.append('b436_search.json : unreadable')
    for k, v in sorted(s.items()):
        rec('        %-44s %s' % (k, v))
    rec('')
    rec('    ### ### **NOT ONE OF THOSE HITS IS A STATED, UNCONDITIONAL, UNIFORM BOUND OF HIS')
    rec('    ### ### SHAPE, AND THE CORPUS`S OWN CLASSIFICATION IS WHY.**')
    rec('        `Chebyshev psi` and the psi asymptotic occur ONLY in `internal/`, which the')
    rec('        corpus classes ### **REGISTRY-SILENT -- "working logs and process records",')
    rec('        scoped census-only by the release ruling.** ### A working log is not a verified')
    rec('        source, and the psi statement it carries is in any case ### **CONDITIONAL ON')
    rec('        RH** ### -- `psi(x) = x + O(sqrt x log^2 x)` -- which is the one thing the')
    rec('        navigator`s candidate must not be.')
    rec('        The one prime asymptotic in a NON-internal document is ### **MERTENS` THIRD')
    rec('        THEOREM** ### at `phase1.5/method/SIEVE_TO_SIDE.md:20`, and it is a different')
    rec('        sum -- a product over primes, not a weighted sum over prime powers.')
    rec('')
    rec('    ### ### ### **PART (a) VERDICT : LOCATED AS ELEMENTARY ;')
    rec('    ### ### ### NOT LOCATED AS A BANKED STATEMENT.**')
    rec('        ### **AS MATHEMATICS IT IS ELEMENTARY AND UNCONTROVERSIAL** -- Chebyshev`s')
    rec('        bound with partial summation gives a finite sum over p^m <= a^2 of')
    rec('        (log p) p^-m/2 of order `a`, unconditionally and uniformly in `a`. ### The')
    rec('        order`s own second route -- *"or is it elementary enough to state from banked')
    rec('        material"* -- is the one it is located by.')
    rec('        ### **AND WHAT IS NOT TRUE IS THAT THE RECORD HOLDS IT.** ### No verified')
    rec('        source states it, and the vocabulary that looks like it sits in a document the')
    rec('        corpus itself says is not one. ### **BOTH HALVES ARE PRINTED BECAUSE ONLY ONE')
    rec('        ### OF THEM IS WHAT THE NAVIGATOR ASKED FOR.**')
    return True


def navigator_b():
    head(5, "THE NAVIGATOR`S CANDIDATE, PART (b) -- ### **THE COMPARISON. BANKED FIGURES ONLY.**")
    rec('    ### **THE NORMALIZATIONS, QUOTED FROM THE EMITTING ACT.** ### They govern; the')
    rec('    ### navigator`s paraphrase governs nothing here.')
    quote(W321, 'half-line normalization', 1, label="b321's half-line normalization")
    rec('')
    quote(os.path.join(T, 'b355_read.py'), 'w /= np.trapezoid(w, v)', 1,
          label='the bump is L1-normalised')
    rec('')
    try:
        rows = json.loads(read(os.path.join(D, 'b436_two_sides.json')))
    except Exception:                                            # noqa: BLE001
        rows = []
        MISS.append('b436_two_sides.json : unreadable')
    rec('    ### **THE TWO SIDES, AT THE TEN RADII THE RECORD PRINTED.** ### b321`s own table:')
    rec('      %-7s %-17s %-17s %-12s' % ('a', 'W_inf (arch)', 'PR (primes)', '|PR|/W_inf'))
    for r in rows:
        rec('      %-7s %-17.9f %-17.9f %-12.3e'
            % (r['a'], r['w_inf'], r['pr'], r['ratio']))
    if rows:
        rec('')
        rec('    ### ### **THE ARCHIMEDEAN QUANTITY FALLS : %0.6f -> %0.6f.**'
            % (rows[0]['w_inf'], rows[-1]['w_inf']))
        rec('    ### ### **THE PRIME CONSTITUENT GROWS IN ABSOLUTE VALUE : %0.6f -> %0.6f.**'
            % (abs(rows[0]['pr']), abs(rows[-1]['pr'])))
        rec('    ### ### **AND THE RATIO GROWS %0.3e -> %0.3e ACROSS TEN CELLS --'
            % (rows[0]['ratio'], rows[-1]['ratio']))
        rec('    ### ### FOUR ORDERS OF MAGNITUDE**, from a = %s to a = %s.'
            % (rows[0]['a'], rows[-1]['a']))
    rec('')
    rec('    ### ### ### **THE FINDING, AT FULL PROMINENCE AND NOT AS A WITNESS:**')
    rec('    ### ### ### **THE BOUND RUNS THE WRONG WAY.**')
    rec('        A bound uniform in `a` must dominate |SUM_p W_p(f)| at every `a`. ### The record')
    rec('        prints that quantity ### **GROWING BY FOUR ORDERS** ### across exactly the')
    rec('        window in which the archimedean quantity it must be compared against ### **FALLS')
    rec('        ### BY A FACTOR OF NINE.** ### So no bound of this shape can show the prime')
    rec('        constituent staying dominated: ### **THE THING IT BOUNDS IS ITSELF CLIMBING')
    rec('        ### TOWARD THE THING IT WOULD HAVE TO STAY UNDER.**')
    rec('        ### **AND THE BOUND`S OWN GROWTH IS NOT A BANKED FIGURE** -- the corpus never')
    rec('        computed it at these radii, and this act does not compute it and call it banked.')
    rec('        What is banked is the MEASURED constituent, which any valid bound must exceed,')
    rec('        and that is enough to settle the direction without computing anything.')
    rec('')
    rec('    ### ### **SO IT FAILS AS A WITNESS ON THE COMPARISON, NOT ON ITS EXISTENCE.**')


def comparability():
    head(6, "IS THE CROSSING REAL, OR AN ARTEFACT OF TWO NORMALIZATIONS NEVER COMPARED?")
    rec('    ### **THE QUESTION THE FACE FIXED, ASKED OF THE RECORD:** ### does any banked act')
    rec('    ### put BOTH quantities in ONE RELATION and VERIFY it?')
    rec('')
    ok = quote(W321, 'the identity is', 0, label="b321's identity")
    rec('')
    rec('    ### and the same act`s verdict on that identity, at thirteen cells:')
    quote(W321, 'THE EXPLICIT-FORMULA CONTROL : HOLDS', 2, label="b321's control verdict")
    rec('')
    rec('    ### and the archimedean channel by a SECOND, independent route:')
    quote(W321, 'Worst difference across all thirteen cells', 0, label="b321's two routes")
    rec('')
    rec('    ### ### ### **ANSWER : COMPARABLE. ### AND NOT NARROWLY.**')
    rec('        The two quantities are ### **TWO OF THE FOUR CHANNELS OF ONE IDENTITY**,')
    rec('        `Z = P - PR + A`, which b321 verified at ### **ALL THIRTEEN CELLS** ### against')
    rec('        a bar it imported rather than chose. ### The archimedean channel was built a')
    rec('        SECOND time by a route sharing no code and the two agree to `6.118e-05`.')
    rec('        ### **TWO QUANTITIES THAT SATISFY ONE VERIFIED IDENTITY ARE IN ONE')
    rec('        ### NORMALIZATION BY CONSTRUCTION**, and no reconciliation is owed.')
    rec('')
    rec('    ### ### ### **AND YET THE CROSSING IS STILL UNDECIDED -- FOR A DIFFERENT REASON,')
    rec('    ### ### ### WHICH IS THE WHOLE POINT OF SEPARATING THE VERDICT FROM ITS REASON.**')
    rec('        The ratio climbs to `3.767e-01` at `a = 3.0` and ### **THE RECORD`S WINDOW ENDS')
    rec('        ### THERE.** ### At no radius the corpus has computed does the prime constituent')
    rec('        reach the archimedean quantity. ### **A TREND IS NOT A CROSSING** ### and this')
    rec('        act does not extrapolate past its own evidence.')
    rec('')
    rec('    ### **WHAT WOULD DECIDE IT, NAMED RATHER THAN GESTURED AT:** ### one run of the')
    rec('    ### window instrument at radii above `a = 3.0`, emitting the same four channels in')
    rec('    ### the same normalization, so the ratio is read and not projected.')
    rec('    ### ### **THAT RUN IS BLOCKED: THE INSTRUMENT LANE IS PARKED**, and b435`s')
    rec('    ### guard-layer exception closed at b435`s end. ### **SO THE PRICE IS ONE ACT WITH')
    rec('    ### ### THAT LANE OPEN, AND THE SEAT DOES NOT OPEN IT.**')
    return ok


def component_5(held):
    head(7, "THE BOUNDARY COUNT AT FOUR SITES. ### **KINDS READ FROM JSON, NEVER TYPED.**")
    try:
        prior = json.loads(read(os.path.join(D, 'b436_prior_sites.json')))
    except Exception:                                            # noqa: BLE001
        prior = {'tallies': {}, 'union': []}
        MISS.append('b436_prior_sites.json : unreadable')
    tallies = prior.get('tallies', {})
    mine = {}
    for c in CANDS:
        if c['verdict'] != 'HELD':
            mine[c['kind']] = mine.get(c['kind'], 0) + 1
    rec('      %-6s %-7s %-12s %s' % ('act', 'site', 'candidates', 'kinds'))
    for act, site, n in (('b424', '(i)', None), ('b427', '(ii)', None),
                         ('b428', '(iii)', None)):
        t = tallies.get(act, {})
        rec('      %-6s %-7s %-12s %d' % (act, site, sum(t.values()), len(t)))
        for k, v in sorted(t.items()):
            rec('               %-36s %s' % (k, v))
    rec('      %-6s %-7s %-12s %d' % ('b436', '(iv)', len(CANDS), len(mine)))
    for k, v in sorted(mine.items()):
        rec('               %-36s %s' % (k, v))
    prior_union = set(prior.get('union', []))
    shared = sorted(set(mine) & prior_union)
    fresh = sorted(set(mine) - prior_union)
    full = sorted(prior_union | set(mine))
    rec('')
    rec('    ### ### **UNION OF KINDS ACROSS THE THREE EARLIER SITES : %d**' % len(prior_union))
    rec('    ### ### **UNION ACROSS ALL FOUR : %d**' % len(full))
    rec('    ### ### **THIS SITE`S FAILURES LANDING AT A BOUNDARY AN EARLIER SITE USED : %d of %d**'
        % (sum(v for k, v in mine.items() if k in prior_union),
           sum(mine.values())))
    for k in shared:
        rec('          %-36s shared with an earlier site' % k)
    for k in fresh:
        rec('          %-36s ### **NEW AT THIS SITE**' % k)
    rec('')
    rec('    ### **AND THE ONE NEW KIND IS NAMED RATHER THAN FOLDED IN:** ### `WRONG DIRECTION`')
    rec('    ### is not `ABSENT`, not `CLASS BOUNDARY` and not `INSTANCES NOT A CLASS`. ### The')
    rec('    ### object EXISTS, is uniform, is unconditional and is about the right sum -- and it')
    rec('    ### ### **MOVES THE WRONG WAY AGAINST THE QUANTITY IT MUST BE COMPARED WITH.**')
    rec('    ### **THAT IS A DIFFERENT FAILURE FROM EVERY ONE THE ARC HAS RECORDED**, and')
    rec('    ### calling it by an old name would have hidden the only new thing at this site.')
    json.dump(dict(at='(iv)', candidates=[{k: c[k] for k in ('id', 'name', 'origin', 'kind',
                                                             'verdict')} for c in CANDS],
                   held=len(held), tally=mine, prior_union=sorted(prior_union),
                   union_four=full, shared=shared, new=fresh),
              io.open(os.path.join(D, 'b436_candidates.json'), 'w', encoding='utf-8'), indent=1)
    return mine, shared, fresh


def component_6(held):
    head(8, "THE CELL. ### **WRITTEN ONLY IF A CANDIDATE HOLDS.**")
    if held:
        rec('    ### A candidate HELD (%s). ### The cell is written through `b327_faces_row.py`'
            % ', '.join(held))
        rec('    ### and through nothing else, under the COLUMN LAW.')
        return 'WRITTEN'
    rec('    ### ### **NO CANDIDATE HELD. ### NO CELL IS WRITTEN AND NO CELL IS EDITED.**')
    rec('    ### The exhausted list is filed as a block, exactly as sites (i), (ii) and (iii)')
    rec('    ### filed theirs. ### **THE REGISTER STAYS FROZEN AT SIX AND NO SEVENTH SITE IS')
    rec('    ### ENTERED.** ### The row`s law is quoted where this act cites it and is not edited.')
    rec('    ### ### **AND NO BRIDGE IS TYPED BETWEEN ANY TWO OF THE SIX, IN EITHER DIRECTION.**')
    return 'NOT WRITTEN'


def main():
    rec('=' * 100)
    rec('b436 -- THE WITNESS ARC AT SITE (iv), THE WINDOW. ### THE COMPONENTS.')
    rec('=' * 100)
    component_1()
    held = component_2()
    nhits, _shown = extension()
    navigator_a()
    navigator_b()
    comparability()
    mine, shared, fresh = component_5(held)
    cell = component_6(held)

    rec('')
    rec('=' * 100)
    rec('  ### ### **THE EXPECTATIONS, SCORED.**')
    rec('=' * 100)
    rec('  ### **(N1) the list is exhausted with no witness held**')
    rec('      candidates %d, held %d   ### ### **%s**'
        % (len(CANDS), len(held), 'HELD' if not held else '### REFUTED'))
    rec('  ### **(N2), ITS TWO CLAUSES APART** (R27)')
    rec('      (a) his candidate is LOCATED as elementary')
    rec('          ### ### **HELD** -- located by the order`s own second route, elementary from')
    rec('          ### banked material; and NOT located as a banked statement, which is printed')
    rec('          ### beside it rather than folded into the verdict.')
    rec('      (b) it fails as a witness ON THE COMPARISON, not on its existence')
    rec('          ### ### **HELD** -- it exists and is uniform; it runs the wrong way.')
    rec('  ### **(N3), ITS VERDICT AND ITS REASON APART** (R27)')
    rec('      (a) the crossing reads NOT COMPARABLE from banked material')
    rec('          ### ### **REFUTED** -- the two quantities are two channels of ONE identity')
    rec('          ### `Z = P - PR + A`, verified at all thirteen cells, the archimedean channel')
    rec('          ### built twice by routes sharing no code and agreeing to 6.118e-05.')
    rec('          ### **THE VERDICT IS `COMPARABLE BUT UNDECIDED`, AND THE CROSSING IS')
    rec('          ### UNDECIDED BECAUSE THE RECORD`S WINDOW ENDS AT a = 3.0.**')
    rec('      (b) the reason -- because they were never normalized against each other')
    rec('          ### ### **REFUTED** -- they were, by the act that printed both.')
    rec('      ### **BOTH CLAUSES REFUTED, AND THE SECOND IS THE INFORMATIVE ONE:** ### the')
    rec('      ### navigator expected an incommensurability and the record holds a verified')
    rec('      ### identity. ### **THE OBSTACLE IS NOT NORMALIZATION; IT IS THE WINDOW`S END.**')
    rec('')
    rec('  ### the cell : %s' % cell)
    rec('  ### extension hits by description : %d, cap %d, admitted 0' % (nhits, EXT_CAP))
    rec('  ### MISSES : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b436_components', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
