# -*- coding: utf-8 -*-
"""b376_axes.py -- COMPONENTS 2 AND 3: ### **THE TWO AXES, QUOTED NOT INVENTED, THEN APPLIED.**

### ### **COMPONENT 2 -- THE AXES.**
### **AXIS A** ### -- `synthesizes a cluster against other available content` versus `gathers a subject's
### research at a point in time` -- ### **quoted from the author's rubric as this ferry's predecessor
### recorded it**, not paraphrased here.
### **AXIS B** ### -- `certifies at pins`, meaning ### **a correspondence table naming kernel, terminal,
### pin and grade that a stranger can traverse** ### -- quoted from the taxonomy's own words.
### ### **ONE PREDICATE PER AXIS, EACH FIXTURED IN BOTH POLARITIES, EACH DECLARING WHAT IT IS DEAF TO.**

### ### **COMPONENT 3 -- EVERY DOCUMENT SCORED ON BOTH AXES, INDEPENDENTLY** ### of the three tests that
### produced the three sets. ### Two marks per document, ### **WITH THE SENTENCE THAT DECIDED EACH MARK
### QUOTED**, and ### **`NOT DETERMINABLE` WHERE THE DOCUMENT'S OWN TEXT DOES NOT DECIDE IT.** ### Then
### the four-quadrant table with its populations.

### ### **THE AXES ARE APPLIED INDEPENDENTLY OF EACH OTHER AND OF EVERY TEST.** ### Axis A never reads a
### correspondence table and axis B never reads a self-describing sentence. ### **IF THEY AGREE, THEY
### ### AGREE HAVING BEEN COMPUTED APART.**

### ### **NO CLASS IS RULED, NO DOCUMENT IS RECLASSIFIED AND NO CLASS LINE IS WRITTEN.** ### A mark on an
### axis is a measurement of a document's own text. ### **IT IS NOT A CLASS AND THIS ACT CONFERS NONE.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import hedge_audit              # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
PRIORF = os.path.join(D, 'b375_ferry_2026-09-08.txt')
ORDERF = os.path.join(D, 'b376_ferry_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# =====================================================================================================
# ### **AXIS A -- BUILT FROM THE RUBRIC'S OWN WORDS.**
# ### The rubric's two halves, as the author wrote them:
# ###   `KEYSTONES synthesize a cluster AGAINST OTHER AVAILABLE CONTENT -- kernels, other keystones,
# ###    other clusters`
# ###   `SUPPORT documents GATHER a subject's research AT A POINT IN TIME`
# ### ### **SO AXIS A HAS TWO REQUIREMENTS ON THE SYNTHESIS SIDE, NOT ONE:** ### a synthesising verb AND
# ### an against-other-content object. ### **`synthesizes` ALONE IS NOT THE RUBRIC'S TEST** -- a document
# ### can synthesise its own material and still only gather.
# =====================================================================================================
# ### **AND ONLY A SENTENCE IN WHICH THE DOCUMENT SPEAKS ABOUT ITSELF CAN DECIDE WHAT THE DOCUMENT
# ### ### DOES** (`b375`). ### A sentence about the subject matter decides nothing.
SELF = re.compile(r'\b(this document|this file|this paper|this register|this ledger|this census|'
                  r'this map|this note|this record|this synthesis|this act|this memo|this report|'
                  r'\*\*PURPOSE:?\*\*|purpose of this|what this .{0,20}(is|does)|'
                  r'it organizes|it gathers|it collects|it synthesiz)', re.I)

A_SYNTH_VERB = re.compile(r'\b(synthesiz|synthesis|organiz|reconcil|integrat|unif(?:y|ies|ied)|'
                          r'draws? together|brings? together|assembles? .{0,20}into|'
                          r'cross-system|cross-cluster|panel|constellation)', re.I)
A_AGAINST = re.compile(r'\b(against|across|other (?:keystones|clusters|documents|content|systems)|'
                       r'kernels|clusters|between|compar\w+|corpus-wide|federation|'
                       r'cross-system|cross-cluster|several|multiple)', re.I)
A_GATHER_VERB = re.compile(r'\b(gathers?|collects?|records?|logs?|tracks?|accumulat\w+|'
                           r'working (?:note|paper)|append-only|running record|register of)', re.I)
A_POINT = re.compile(r'\b(at a point in time|as of|snapshot|point-in-time|on 20\d\d-|'
                     r'at the time|current state|so far|to date|running)', re.I)

# =====================================================================================================
# ### **AXIS B -- BUILT FROM THE TAXONOMY'S OWN WORDS AND THE ORDER'S GLOSS OF THEM.**
# ### `Tier K` ### : `claims are backed by a MACHINE-CHECKED KERNEL TERMINAL AT A PIN, Gate-1-graded
# ### (DERIVES, or INTERFACES-with-a-named-premise). Obligation: every such claim states its GRADE .
# ### TERMINAL . PIN.` ### The order's gloss: ### **`a correspondence table naming kernel, terminal, pin
# ### ### and grade THAT A STRANGER CAN TRAVERSE`.**
# ### ### **SO THE UNIT OF AXIS B IS A ROW, AND A ROW MUST CARRY ALL FOUR.** ### Three of four is a row a
# ### stranger cannot traverse, and this predicate scores it as such rather than rounding it up.
# ### ### **AND IT READS EVERY TABLE ROW IN THE DOCUMENT, NOT ONLY ROWS UNDER A HEADING.** ### The census
# ### tested a HEADING and `b376` Component 1 showed what that costs; ### **THIS ONE TESTS CONTENT.**
# =====================================================================================================
B_KERNEL = re.compile(r'\b(SIDE-[A-Za-z0-9-]+|TECHNE[-_A-Za-z0-9]*|PLACE-[A-Za-z0-9-]+)\b')
B_TERMINAL = re.compile(r'`[A-Za-z_][A-Za-z0-9_₀-₉]*(?:\.[A-Za-z_][A-Za-z0-9_₀-₉]*)+`')
B_PIN = re.compile(r'\bv\d+\.\d+(?:\.\d+)?\b|\b[0-9a-f]{7,40}\b')
B_GRADE = re.compile(r'\b(' + '|'.join(re.escape(t) for t in hedge_audit.GRADE_TOKENS)
                     + r'|INTERFACES[A-Za-z-]*|Compiled|COMPILED|DEFINED-ONLY|SUPPORTED-BY[A-Z-]*'
                     + r'|NO TERMINAL|NOT LOCATED)\b')
# ### **THE THIRD MARK AXIS B CAN RETURN.** ### The census itself named a class of documents that name
# ### their terminals ### **IN PROSE** ### rather than in a table (`CONCORDANCE-CARRIED`). ### For those
# ### the apparatus question is ### **NOT DETERMINABLE FROM A TABLE SCAN**, and this predicate says so
# ### instead of scoring them `B-`.
B_PROSE_TERMINAL = re.compile(r'\bKernel Concordance\b|\bnames? (?:its|their) terminals? in prose\b'
                              r'|\bconcordance\b', re.I)

TABLE_ROW = re.compile(r'^\s*\|.*\|\s*$')
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(('git', '-C', PP) + a, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def sentences(txt):
    """### **SPLIT ON SENTENCE ENDS AND ON LINE ENDS**, because a markdown bullet is a sentence."""
    out = []
    for chunk in txt.split(chr(10)):
        c = chunk.strip()
        if not c:
            continue
        for s in re.split(r'(?<=[.!?])\s+', c):
            s = s.strip()
            if len(s) > 8:
                out.append(s)
    return out


def axis_a(txt, strict=True):
    """### **RETURNS `(mark, deciding sentence, why)`. ### `A+` SYNTHESISES AGAINST OTHER CONTENT.**

    ### ### **TWO READINGS, AND THE SECOND IS RUN AND REPORTED, NEVER SUBSTITUTED** (`b373`).
    ### `strict=True` ### requires ### **ONE SELF-DESCRIBING SENTENCE TO CARRY BOTH HALVES**, because the
    ### rubric's own sentence carries both. ### `strict=False` ### allows the two halves to fall in
    ### DIFFERENT self-describing sentences, because a document may split its self-description across
    ### two sentences and still be describing itself.
    ### ### **THE STRICT READING IS THE DECLARED ONE. ### THE BROAD READING IS PRINTED BESIDE IT SO THE
    ### ### COST OF THE STRICTNESS IS VISIBLE RATHER THAN HIDDEN IN A COUNT.**
    """
    ss = [s for s in sentences(txt) if SELF.search(s)]
    synth = gather = None
    if strict:
        for s in ss:
            if synth is None and A_SYNTH_VERB.search(s) and A_AGAINST.search(s):
                synth = s
            if gather is None and A_GATHER_VERB.search(s) and A_POINT.search(s):
                gather = s
    else:
        sv = next((s for s in ss if A_SYNTH_VERB.search(s)), None)
        so = next((s for s in ss if A_AGAINST.search(s)), None)
        gv = next((s for s in ss if A_GATHER_VERB.search(s)), None)
        gp = next((s for s in ss if A_POINT.search(s)), None)
        synth = sv if (sv and so) else None
        gather = gv if (gv and gp) else None
    if synth and not gather:
        return 'A+', synth, 'a self-describing sentence carries a synthesising verb AND an '                             'against-other-content object'
    if gather and not synth:
        return 'A-', gather, "a self-describing sentence carries a gathering verb AND a "                              "point-in-time marker"
    if synth and gather:
        return 'A+', synth, '### **BOTH HALVES FIRE; THE RUBRIC`S SYNTHESIS HALF IS THE STRICTER '                             'AND IT IS SATISFIED** -- the gathering sentence is in the JSON'
    return 'A?', '', 'no self-describing sentence carries either half of the rubric'


def axis_b(txt):
    """### **RETURNS `(mark, deciding row, why)`. ### `B+` CARRIES A ROW A STRANGER CAN TRAVERSE.**"""
    best, best_n = None, -1
    for line in txt.split(chr(10)):
        if not TABLE_ROW.match(line):
            continue
        if re.match(r'^\s*\|[\s:|-]+\|\s*$', line):
            continue
        have = (bool(B_KERNEL.search(line)), bool(B_TERMINAL.search(line)),
                bool(B_PIN.search(line)), bool(B_GRADE.search(line)))
        n = sum(have)
        if n > best_n:
            best_n, best = n, (line.strip(), have)
    if best and best_n == 4:
        return 'B+', best[0], 'a table row names kernel, terminal, pin and grade together'
    if B_PROSE_TERMINAL.search(txt) and (best is None or best_n < 4):
        miss = ''
        if best:
            names = ('kernel', 'terminal', 'pin', 'grade')
            miss = ' (best row carries %s)' % ', '.join(n for n, h in zip(names, best[1]) if h)
        return 'B?', (best[0] if best else ''), \
            '### **NAMES TERMINALS IN PROSE OR CARRIES A CONCORDANCE**, so a table scan cannot ' \
            'decide it' + miss
    if best:
        names = ('kernel', 'terminal', 'pin', 'grade')
        return 'B-', best[0], 'no row carries all four; the best row carries %s' \
            % (', '.join(n for n, h in zip(names, best[1]) if h) or 'none of the four')
    return 'B-', '', 'the document carries no table row at all'


# ---------------------------------------------------------------------------------- THE FIXTURES
FIX_A_POS = ("**PURPOSE:** this document synthesizes the cluster against the other keystones and "
             "the kernels available to it.")
FIX_A_NEG = ("**PURPOSE:** this document gathers the subject's research as of 2026-08-01 and "
             "records the working notes.")
FIX_B_POS = ("| II.1 the fixed point | SIDE-archimedean v0.1.0 | "
             "`SIDEArchimedean.archimedean_forces_half` | `{propext}` | **DERIVES** |")
FIX_B_NEG = "| a claim | some prose | another cell | and a fourth |"


def fixtures(verbose=True):
    """### **BOTH POLARITIES FOR BOTH AXES, ON LINES DRAWN FROM REAL CORPUS SHAPES.**
    ### ### **A PREDICATE THAT HAS ONLY EVER SAID YES IS NOT A PREDICATE.**"""
    res = [
        ('axis A, positive', axis_a(FIX_A_POS)[0], 'A+'),
        ('axis A, negative', axis_a(FIX_A_NEG)[0], 'A-'),
        ('axis A, silent', axis_a('The zeta function has a pole at one.')[0], 'A?'),
        ('axis B, positive', axis_b(FIX_B_POS)[0], 'B+'),
        ('axis B, negative', axis_b(FIX_B_NEG)[0], 'B-'),
        ('axis B, no table', axis_b('Plain prose with no table.')[0], 'B-'),
    ]
    ok = all(got == want for _l, got, want in res)
    if verbose:
        for lbl, got, want in res:
            rec('      %-22s got %-4s want %-4s  %s'
                % (lbl, got, want, 'ok' if got == want else '### MISMATCH ###'))
    return ok, res


def main():
    rec('=' * 100)
    rec('b376 -- COMPONENTS 2 AND 3: ### **THE TWO AXES, QUOTED NOT INVENTED, THEN APPLIED.**')
    rec('=' * 100)
    rec('')

    # ------------------------------------------------------------ COMPONENT 2: THE QUOTED SOURCES
    rec('-' * 100)
    rec('  ### COMPONENT 2 (a) -- THE AXES IN THEIR SOURCES` OWN WORDS, ANCHORED BY THE TOOL.')
    rec('-' * 100)
    quotes = {}
    for tag, path, hint in (
        ('AXIS A -- the SUPPORT half', PRIORF,
         "as the census's own test: SUPPORT documents gather a subject's"),
        ('AXIS A -- the KEYSTONE half', PRIORF,
         'questions and working notes. KEYSTONES synthesize a cluster'),
        ('AXIS A -- and may not carry those', PRIORF,
         'other clusters - and may not carry those. Both are in ongoing'),
        ('AXIS B -- Tier K, in the taxonomy', TAX,
         '**Tier K — Keystone-certified.** A document whose load-bearing claims are backed'),
        ('AXIS B -- the order`s gloss', ORDERF,
         'AXIS B - certifies at pins, meaning a correspondence table'),
        ('AXIS B -- what a stranger must traverse', ORDERF,
         'naming kernel, terminal, pin and grade that a stranger can'),
    ):
        n, line = AF.find(path, hint)
        quotes[tag] = dict(file=os.path.basename(path), line=n, text=line.strip())
        rec('    ### **%s** -- `%s` line %d' % (tag, os.path.basename(path), n))
        rec('      | %s' % line.strip()[:150])
    rec('')
    rec('    ### ### **BOTH AXES ARE NOW ON THIS PAGE IN WORDS THIS SEAT DID NOT CHOOSE.**')

    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 (b) -- THE PREDICATES, AND WHAT EACH ONE IS DEAF TO.')
    rec('-' * 100)
    rec('    ### **AXIS A** ### fires `A+` only when ### **ONE SELF-DESCRIBING SENTENCE CARRIES BOTH**')
    rec('    ### a synthesising verb AND an against-other-content object, because the rubric`s')
    rec('    ### sentence carries both: ### `synthesize a cluster AGAINST OTHER AVAILABLE CONTENT`.')
    rec('    ###   synthesising verbs : %s' % A_SYNTH_VERB.pattern[:100])
    rec('    ###   against-other      : %s' % A_AGAINST.pattern[:100])
    rec('    ###   gathering verbs    : %s' % A_GATHER_VERB.pattern[:100])
    rec('    ###   point-in-time      : %s' % A_POINT.pattern[:100])
    rec('    ### ### **AXIS A IS DEAF TO:** ### a document that synthesises against other content and')
    rec('    ###     ### **NEVER SAYS SO ABOUT ITSELF** -- it scores `A?`, not `A-`; a synonym off the')
    rec('    ###     list; a self-describing sentence that describes ### **ONE SECTION** ### rather than')
    rec('    ###     the whole; and ### **A CLASS LINE ADDED BY A LATER ACT**, which it will read as the')
    rec('    ###     document`s own words because on the page it is (`PREDICATE_ONE_SHAPE`).')
    rec('')
    rec('    ### **AXIS B** ### fires `B+` only when ### **ONE TABLE ROW CARRIES ALL FOUR** ### of kernel,')
    rec('    ### terminal, pin and grade -- the four the order names as what a stranger must traverse.')
    rec('    ###   kernel   : %s' % B_KERNEL.pattern[:100])
    rec('    ###   terminal : %s' % B_TERMINAL.pattern[:100])
    rec('    ###   pin      : %s' % B_PIN.pattern[:100])
    rec('    ###   grade    : %s' % B_GRADE.pattern[:100])
    rec('    ### ### **AXIS B IS DEAF TO:** ### a correspondence table whose ### **PIN IS A DATE** ### and')
    rec('    ###     not a tag or a hash; a terminal written without backticks; ### **WHETHER THE PIN')
    rec('    ###     ### RESOLVES** -- it reads the SHAPE of a traversable row, not the traversal; and')
    rec('    ###     ### **WHETHER THE ROW IS TRUE.** ### `b373` measured resolution and this does not.')
    rec('    ### ### ### **AND IT RETURNS `B?` RATHER THAN `B-` FOR A DOCUMENT THAT NAMES TERMINALS IN')
    rec('    ### ### ### PROSE**, because the census itself named that architecture as its own class and')
    rec('    ### ### ### a table scan is the wrong instrument for it.')

    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 (c) -- THE FIXTURES, BOTH POLARITIES, BEFORE EITHER PREDICATE IS TRUSTED.')
    rec('-' * 100)
    ok, fx = fixtures(True)
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('BOTH POLARITIES HELD ON BOTH AXES' if ok else '### FAILED ###'))
    if not ok:
        rec('    ### REFUSING TO SCORE A CORPUS WITH A PREDICATE THAT FAILS ITS OWN FIXTURES.')
        run_clock.write(D, 'b376_axes_notes', LINES)
        return 2

    # ------------------------------------------------------------------ COMPONENT 3: THE SCORING
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 3 -- EVERY DOCUMENT SCORED ON BOTH AXES, INDEPENDENTLY.')
    rec('-' * 100)
    rels = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    scored = []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        am, asent, awhy = axis_a(txt, strict=True)
        amb, asentb, awhyb = axis_a(txt, strict=False)
        bm, brow, bwhy = axis_b(txt)
        scored.append(dict(file=rel, base=os.path.basename(rel)[:-3],
                           axis_a=am, a_sentence=asent[:300], a_why=awhy,
                           axis_a_broad=amb, a_sentence_broad=asentb[:300], a_why_broad=awhyb,
                           axis_b=bm, b_row=brow[:300], b_why=bwhy,
                           quadrant='%s%s' % (am, bm),
                           quadrant_broad='%s%s' % (amb, bm)))
    rec('    documents scored : %d   ### **EACH ON BOTH AXES, AND EACH AXIS COMPUTED WITHOUT'
        % len(scored))
    rec("    ### **SIGHT OF THE OTHER`S ANSWER.**")
    ta, tab, tb = {}, {}, {}
    for x in scored:
        ta[x['axis_a']] = ta.get(x['axis_a'], 0) + 1
        tab[x['axis_a_broad']] = tab.get(x['axis_a_broad'], 0) + 1
        tb[x['axis_b']] = tb.get(x['axis_b'], 0) + 1
    rec('    ### **AXIS A, THE STRICT READING (one sentence carries both halves) : %s**' % ta)
    rec('    ### **AXIS A, THE BROAD READING  (two sentences may share the work) : %s**' % tab)
    rec('    ### **AXIS B                                                        : %s**' % tb)
    rec('')
    rec('    ### ### **THE STRICTNESS COSTS %d DOCUMENTS ON THE SYNTHESIS SIDE AND %d ON THE GATHERING'
        % (tab.get('A+', 0) - ta.get('A+', 0), tab.get('A-', 0) - ta.get('A-', 0)))
    rec('    ### ### SIDE**, and the cost is printed rather than absorbed. ### **BOTH READINGS ARE RUN;')
    rec('    ### ### NEITHER IS SUBSTITUTED FOR THE OTHER** (`b373`). ### The STRICT reading is the one')
    rec('    ### ### the quadrant table below uses, because ### **THE RUBRIC`S OWN SENTENCE CARRIES BOTH')
    rec('    ### ### HALVES IN ONE BREATH**; ### the BROAD reading is tabled beside it.')
    rec('')
    rec('    ### ### ### **AND THE FIRST THING BOTH READINGS AGREE ON IS THE SIZE OF `A?`.** ### %d of'
        % ta.get('A?', 0))
    rec('    ### ### ### %d documents ### **DO NOT SAY WHAT THEY ARE**, on the strict reading, and %d do'
        % (len(scored), tab.get('A?', 0)))
    rec('    ### ### ### not on the broad one. ### **THE CORPUS IS LARGELY SILENT ABOUT ITS OWN ROLE, AND')
    rec('    ### ### ### THAT SILENCE IS THE MEASUREMENT** -- not a hole in the sweep.')

    rec('')
    rec('    ### **THE FOUR QUADRANTS, AND THE `NOT DETERMINABLE` CLASSES BESIDE THEM:**')
    rec('')
    quad = {}
    for x in scored:
        quad[x['quadrant']] = quad.get(x['quadrant'], 0) + 1
    order = ['A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?']
    gloss = {
        'A+B+': 'synthesises against other content AND carries a traversable row',
        'A+B-': 'synthesises against other content, carries no traversable row',
        'A-B+': 'gathers at a point in time, YET carries a traversable row',
        'A-B-': 'gathers at a point in time, carries no traversable row',
        'A+B?': 'synthesises; the apparatus question is not decidable by a table scan',
        'A-B?': 'gathers; the apparatus question is not decidable by a table scan',
        'A?B+': 'says nothing about itself; carries a traversable row',
        'A?B-': 'says nothing about itself; carries no traversable row',
        'A?B?': 'neither axis is decided by the document`s own text',
    }
    rec('      %-6s %-6s %s' % ('cell', 'count', 'what the cell means'))
    rec('      %s' % ('-' * 96))
    tot = 0
    for k in order:
        n = quad.get(k, 0)
        tot += n
        rec('      %-6s %-6d %s' % (k, n, gloss[k]))
    rec('      %s' % ('-' * 96))
    rec('      %-6s %-6d ### **AND %d IS THE WHOLE SWEEP, SO THE TABLE IS A PARTITION.**'
        % ('total', tot, len(scored)))
    stray = sorted(set(quad) - set(order))
    if stray:
        rec('      ### ### **CELLS OUTSIDE THE DECLARED NINE : %s**' % stray)

    rec('')
    rec('    ### **AND THE SAME TABLE UNDER THE BROAD READING OF AXIS A, PRINTED BESIDE IT:**')
    quadb = {}
    for x in scored:
        quadb[x['quadrant_broad']] = quadb.get(x['quadrant_broad'], 0) + 1
    rec('      %-6s %-8s %-8s %s' % ('cell', 'strict', 'broad', 'movement'))
    rec('      %s' % ('-' * 96))
    for k in order:
        a, b = quad.get(k, 0), quadb.get(k, 0)
        rec('      %-6s %-8d %-8d %s'
            % (k, a, b, ('same' if a == b else '### %+d' % (b - a))))
    rec('      %s' % ('-' * 96))
    rec('      %-6s %-8d %-8d ### **BOTH PARTITION THE SAME %d DOCUMENTS.**'
        % ('total', sum(quad.values()), sum(quadb.values()), len(scored)))

    rec('')
    rec('    ### ### **THE FOUR QUADRANTS PROPER, WITH THE UNDECIDED HELD OUT AND NOT ROUNDED IN:**')
    four = sum(quad.get(k, 0) for k in ('A+B+', 'A+B-', 'A-B+', 'A-B-'))
    rec('    ###   decided on both axes : ### **%d** ### of %d' % (four, len(scored)))
    rec('    ###   undecided on at least one axis : ### **%d**' % (len(scored) - four))
    rec('    ### ### **THE UNDECIDED ARE NOT A RESIDUE TO BE SWEPT INTO A QUADRANT.** ### They are')
    rec('    ### ### documents whose own text does not answer the question, and ### **THAT IS A')
    rec('    ### ### MEASUREMENT, NOT A FAILURE OF THE SWEEP.**')

    rec('')
    rec('    ### **`(E2)` AS THIS FACE REGISTERED IT:** ### the `A-B+` quadrant -- a document that')
    rec('    ### carries a full traversable row but says nothing about synthesising -- holds ### **%d**.'
        % quad.get('A-B+', 0))
    if quad.get('A-B+', 0) or quad.get('A?B+', 0):
        rec('    ### ### **AND THE APPARATUS-WITHOUT-THE-PROSE POPULATION, COUNTING `A?B+` TOO, IS %d.**'
            % (quad.get('A-B+', 0) + quad.get('A?B+', 0)))
        rec('    ### ### **THAT IS THE MORE INTERESTING RESULT IF IT IS LARGE**, as the face said before')
        rec('    ### ### the measurement, ### **BECAUSE IT MEANS THE APPARATUS AND THE PROSE COME APART.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b376_axes_notes', LINES)
    io.open(os.path.join(D, 'b376_axes.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(quotes=quotes, fixtures_ok=ok,
                        fixtures=[dict(label=l, got=g, want=w) for l, g, w in fx],
                        scored=scored, axis_a_tally=ta, axis_a_broad_tally=tab,
                        axis_b_tally=tb, quadrants=quad, quadrants_broad=quadb,
                        decided_both=four, run_file=os.path.basename(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
