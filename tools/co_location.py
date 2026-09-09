# -*- coding: utf-8 -*-
"""co_location.py -- ### **DO SOURCES FROM DIFFERENT CLUSTERS SIT IN THE SAME UNIT?**

### ### **WHY THIS EXISTS.** ### `b380` read role as ### **REACH** ### -- how far a document's
### citations go -- and the predicate scored a bibliography above a proof, then failed its control on
### both documents that declare they gather. ### **REACH IS NOT ARGUMENT.** ### The order's replacement
### reads the rubric's verb instead: ### `KEYSTONES synthesize a cluster AGAINST other available
### content` ### is a claim that a document ### **COMBINES** ### them, and the structural trace of
### combining is that the sources ### **SHARE A UNIT.**
### ### ### **A COLLECTION PARTITIONS ITS SOURCES ONE PER ENTRY; A SYNTHESIS CO-LOCATES THEM.**

### ### **THE UNIT IS NOT DEFINED HERE.** ### It was fixed on `b381`'s locked face before any score,
### and this module implements that definition and nothing wider. ### A `UNIT` is exactly one of:
###   ### **ONE LIST ITEM** ### -- a bullet or ordered marker plus its indented continuation lines;
###   ### **ONE TABLE ROW** ### -- a single line opening with a pipe;
###   ### **ONE FENCED BLOCK** ### -- the lines between a pair of fences;
###   ### **ONE PARAGRAPH** ### -- a run of non-blank lines that is none of the above, bounded by a
###     blank line, by a real heading, or by a fence.
### ### **A REAL HEADING CLOSES A UNIT AND IS NOT PART OF ONE** -- `b377`'s test, because the corpus
### writes `### **EMPHASIS**` in running prose and that is a convention, not a heading.

### ### ### **WHY AN ENTRY IS A UNIT OF ITS OWN, AND THIS IS THE WHOLE POINT:** ### under a
### blank-line-only definition a bibliography is ### **ONE PARAGRAPH**, and the most partitioned
### document in the corpus would score as the most combining. ### The order's own sentence names the
### entry as the unit of partition, so ### **AN ENTRY MUST BE A UNIT OR THE PREDICATE MEASURES THE
### ### EXACT OPPOSITE OF WHAT IT IS FOR.**

### ### **WHAT IT IS DEAF TO, AND ALL FIVE ARE REAL:**
###   ### **A DOCUMENT QUOTING MANY SOURCES IN ONE PLACE WITHOUT RELATING THEM SCORES AS SYNTHESIS.**
###     ### The order names this one. ### Two names in a sentence are not an argument between them.
###   ### **A SYNTHESIS THAT RELATES TWO SOURCES ACROSS ADJACENT PARAGRAPHS SCORES AS GATHERING.**
###     ### Co-location cannot see across a paragraph break, and a writer's habit is not an argument.
###   ### **MARKDOWN STRUCTURE STANDS IN FOR RHETORICAL STRUCTURE.** ### A document written in long
###     paragraphs co-locates by formatting; one written in short ones cannot.
###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT** -- `b380`'s, inherited whole, an ADDRESS standing
###     in for a subject and exactly the substitution `(R2)` warns against.
###   ### **A CITATION IT DOES NOT RECOGNISE IS NOT A CITATION TO IT** -- `b380`'s, inherited whole.

### ### **IT RETURNS A MARK AND A REASON. ### IT NEVER RETURNS A CLASS.**
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import role_structure as RS   # noqa: E402

# ### **`b377`'S REAL-HEADING TEST, NOT REBUILT:** ### a hash run followed by space and NOT by `**`.
REAL_HEADING = re.compile(r'^#{1,6}[ \t]+(?!\*\*)')
LIST_ITEM = re.compile(r'^[ \t]*([-*+]|\d+[.)])[ \t]+')
TABLE_ROW = re.compile(r'^[ \t]*\|')
FENCE = re.compile(r'^[ \t]*(```|~~~)')
CONTINUATION = re.compile(r'^[ \t]+\S')

# ### **THE THRESHOLD, FROM THE LOCKED FACE.** ### `partitions` and `co-locates` are claims about how
# ### a document is BUILT -- about most of it -- so the bar is a majority of its source-bearing units.
# ### **A SINGLE-OCCURRENCE RULE WOULD MAKE A BIBLIOGRAPHY WITH ONE `see also` ENTRY A SYNTHESIS.**
THRESHOLD = 0.5


def units(text):
    """### **SPLIT INTO UNITS.** ### Returns `[(kind, first_line_index, [lines])]`, 1-indexed lines.

    ### **THE HEADING IS NOT IN ANY UNIT** and neither is a blank line; every other line is in
    ### exactly one, which is what makes the ratio a ratio.
    """
    lines = text.split(chr(10))
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if REAL_HEADING.match(ln):
            i += 1
            continue
        if FENCE.match(ln):
            start, buf = i + 1, [ln]
            i += 1
            while i < n and not FENCE.match(lines[i]):
                buf.append(lines[i])
                i += 1
            if i < n:
                buf.append(lines[i])
                i += 1
            out.append(('fence', start, buf))
            continue
        if TABLE_ROW.match(ln):
            out.append(('table_row', i + 1, [ln]))
            i += 1
            continue
        if LIST_ITEM.match(ln):
            start, buf = i + 1, [ln]
            i += 1
            while (i < n and lines[i].strip() and CONTINUATION.match(lines[i])
                   and not LIST_ITEM.match(lines[i]) and not TABLE_ROW.match(lines[i])
                   and not FENCE.match(lines[i]) and not REAL_HEADING.match(lines[i])):
                buf.append(lines[i])
                i += 1
            out.append(('list_item', start, buf))
            continue
        start, buf = i + 1, []
        while (i < n and lines[i].strip() and not LIST_ITEM.match(lines[i])
               and not TABLE_ROW.match(lines[i]) and not FENCE.match(lines[i])
               and not REAL_HEADING.match(lines[i])):
            buf.append(lines[i])
            i += 1
        out.append(('paragraph', start, buf))
    return out


def clusters_in(chunk, index, self_rel):
    """### **THE DISTINCT CLUSTERS A UNIT NAMES.** ### The source vocabulary is `b380`'s, IMPORTED
    ### UNCHANGED, so reach and co-location are measured over the same things and the two columns
    ### are commensurable rather than merely adjacent."""
    got = set(RS.kernels_named(chunk))
    for docrel in RS.documents_cited(chunk, index, self_rel):
        got.add(RS.own_cluster(docrel))
    return got


def score(rel, text, index):
    """### **RETURN `(mark, reason, evidence)`.** ### `C+` co-locates, `C-` partitions, `C?` silent.

    ###   ### **`C+`** ### -- MORE THAN HALF its source-bearing units carry two or more clusters.
    ###   ### **`C-`** ### -- some do, but not more than half.
    ###   ### **`C?`** ### -- no unit carries a source at all.
    """
    us = units(text)
    bearing, colocating, kinds, examples = 0, 0, {}, []
    for kind, ln, buf in us:
        cs = clusters_in(chr(10).join(buf), index, rel)
        if not cs:
            continue
        bearing += 1
        kinds[kind] = kinds.get(kind, 0) + 1
        if len(cs) >= 2:
            colocating += 1
            if len(examples) < 3:
                examples.append(dict(kind=kind, line=ln, clusters=sorted(cs)[:6]))
    ratio = (float(colocating) / bearing) if bearing else 0.0
    ev = dict(units=len(us), source_bearing_units=bearing, colocating_units=colocating,
              ratio=round(ratio, 4), bearing_kinds=kinds, examples=examples)
    if bearing == 0:
        return 'C?', 'no unit in it carries a source this predicate can see', ev
    if ratio > THRESHOLD:
        return 'C+', ('%d of its %d source-bearing units carry two or more clusters (%.1f%%)'
                      % (colocating, bearing, 100.0 * ratio)), ev
    return 'C-', ('only %d of its %d source-bearing units carry two or more clusters (%.1f%%), so it '
                  'partitions' % (colocating, bearing, 100.0 * ratio)), ev


# ---- THE FIXTURES ----------------------------------------------------------------------------------
FIX_INDEX = {'THE_METHOD_CANON': 'phase1.5/method/THE_METHOD_CANON.md',
             'GRH_CASCADE': 'phase1.5/spectral/GRH_CASCADE.md',
             'INSTRUMENTS': 'phase1.5/method/INSTRUMENTS.md',
             'THE_SUBSTRATE': 'phase1.5/method/THE_SUBSTRATE.md'}
HERE = 'phase1.5/proofs/A_TEST.md'

# ### **A SYNTHESIS:** ### one paragraph holding two clusters, so every bearing unit co-locates.
FIX_SYNTH = ('It reads `GRH_CASCADE` against `SIDE-kernel`, and the two disagree about the tail.'
             + chr(10))
# ### **A COLLECTION:** ### the SAME two sources, one per entry. ### **THE RATIO IS WHAT SEPARATES
# ### THEM, AND A BLANK-LINE-ONLY SPLITTER WOULD SCORE THIS EXACTLY LIKE THE ONE ABOVE.**
FIX_COLL = (chr(10).join(['- `GRH_CASCADE` -- the cascade note.',
                          '- `SIDE-kernel` -- the kernel.',
                          '- `INSTRUMENTS` -- the instrument list.']) + chr(10))
FIX_TABLE = (chr(10).join(['| name | note |',
                           '| `GRH_CASCADE` | the cascade |',
                           '| `SIDE-kernel` | the kernel |']) + chr(10))
FIX_SILENT = 'A page of prose that names nothing at all.' + chr(10)


def self_test(verbose=False):
    """### **BOTH POLARITIES, ON ALL THREE KINDS OF UNIT, PLUS A HEADING AND A FENCE.** ### A splitter
    that only ever makes paragraphs would score every collection as a synthesis, so the splitter is
    fixtured before the predicate that rides on it."""
    heading_doc = ('# A heading' + chr(10) + 'A paragraph under it.' + chr(10))
    fenced = ('```' + chr(10) + 'code `GRH_CASCADE` `SIDE-kernel`' + chr(10) + '```' + chr(10))
    two_paras = ('Names `GRH_CASCADE`.' + chr(10) + chr(10) + 'Names `SIDE-kernel`.' + chr(10))
    cases = [
        ('a paragraph holding two clusters -- ### **C+**',
         score(HERE, FIX_SYNTH, FIX_INDEX)[0], 'C+'),
        ('### **THE SAME SOURCES ONE PER LIST ENTRY -- C-**',
         score(HERE, FIX_COLL, FIX_INDEX)[0], 'C-'),
        ('### **THE SAME SOURCES ONE PER TABLE ROW -- C-**',
         score(HERE, FIX_TABLE, FIX_INDEX)[0], 'C-'),
        ('a document naming nothing -- ### **C?**',
         score(HERE, FIX_SILENT, FIX_INDEX)[0], 'C?'),
        ('a list item is its own unit',
         [k for k, _l, _b in units(FIX_COLL)], ['list_item'] * 3),
        ('a table row is its own unit',
         [k for k, _l, _b in units(FIX_TABLE)], ['table_row'] * 3),
        ('a real heading is in no unit',
         [k for k, _l, _b in units(heading_doc)], ['paragraph']),
        ('a fence is one unit',
         [k for k, _l, _b in units(fenced)], ['fence']),
        ('### **THE DEAFNESS THE ORDER NAMES: TWO SOURCES IN SEPARATE PARAGRAPHS DO NOT CO-LOCATE**',
         score(HERE, two_paras, FIX_INDEX)[0], 'C-'),
        ('the ratio of the collection is at or below the threshold',
         score(HERE, FIX_COLL, FIX_INDEX)[2]['ratio'] <= THRESHOLD, True),
        ('the ratio of the synthesis is above it',
         score(HERE, FIX_SYNTH, FIX_INDEX)[2]['ratio'] > THRESHOLD, True),
    ]
    ok = all(g == w for _l, g, w in cases)
    if verbose:
        for lbl, g, w in cases:
            print('      %-70s got %-14s want %-14s %s'
                  % (lbl[:70], str(g)[:14], str(w)[:14], 'ok' if g == w else '### MISMATCH ###'))
    return ok, [dict(case=l, got=str(g), want=str(w)) for l, g, w in cases]


if __name__ == '__main__':
    ok, log = self_test(True)
    print('  ### ### **SELF-TEST : %s**'
          % ('ALL THREE MARKS REACHABLE, ALL THREE UNIT KINDS SPLIT, AND THE COLLECTION IS NOT A '
             'SYNTHESIS' if ok else '### FAILED'))
    raise SystemExit(0 if ok else 1)
