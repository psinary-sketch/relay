# -*- coding: utf-8 -*-
"""anchor_from_file.py -- BUILD AN ANCHOR BY READING ITS LINE, NEVER BY TYPING IT.

### ### **THE SPECIES THIS RETIRES, NAMED TWICE AND BUILT NEVER UNTIL NOW.**
### ### An act types a sentence it means to quote, and the sentence it types differs from the sentence the file
### holds -- by a curly apostrophe where the file has a straight one, by two hyphens where the file has an em
### dash, by a marker prefix the file does not use, or by a line break falling inside the phrase. ### **NOT ONE
### ### OF THESE IS A MISSING SENTENCE.** ### Every one is the seat mis-typing a sentence that is there.
### ### **THE COUNT:** ### `b309`-`b313` and `b317` on wrapping (six acts, banked at
### `feedback_needle_anchor_wrapping`); `b348` on a curly apostrophe; `b351` two of twenty-six; `b352` six of
### twenty-six. ### `b352` named the cure -- *build the anchor by READING the line from the file rather than
### typing it* -- and did not build it. ### `b353` applied it BY HAND and got `23` of `23` on the first run.
### ### **THIS FILE IS THAT CURE, BUILT.**
###
### ### **HOW IT WORKS.** ### You give it a file and a HINT -- a short distinctive fragment, typed however you
### like. ### It searches the file with the hint NORMALISED (through the sortie's shared normaliser, so curly
### quotes, dashes, markers and whitespace cannot separate you from your own sentence), finds the line, and
### returns ### **THE LINE AS THE FILE HOLDS IT, BYTE FOR BYTE.** ### That string is the anchor.
###
### ### **THE LIMITS, IN THE HEADER SO IT IS NOT TRUSTED BEYOND THEM:**
### ### **(1) IT CANNOT INVENT A SENTENCE.** ### If the hint matches nothing, it RAISES. ### A hint that
###     matches nothing is a real absence and must be reported as one, not softened into a near miss.
### ### **(2) IT CANNOT CHOOSE BETWEEN MATCHES.** ### If the hint matches more than one line it RAISES and
###     prints them, because an anchor that matches twice anchors nothing.
### ### **(3) IT DOES NOT MAKE A QUOTATION TRUE.** ### It makes the anchor equal to the file's line. ###
###     Whether that line says what the act claims it says is the act's own business, and no tool's.
### ### **(4) A HINT SPANNING A LINE BREAK CANNOT MATCH A SINGLE LINE.** ### `span=True` searches the file
###     with its newlines flattened and returns the WHOLE RUN of lines the hint crosses, as a list -- so the
###     caller learns the sentence wraps instead of learning nothing.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm   # noqa: E402

# ### ==================================================================================================
# ### ### **A DEFECT THIS FILE'S OWN FIXTURE FOUND, ON ITS FIRST RUN, AND THE REASON THE FIXTURE EXISTS.**
# ### `quote_norm` folds an em dash to ### **ONE** ### hyphen. ### A seat typing `--` where the file holds
# ### an em dash therefore STILL MISSES after normalisation -- which is exactly `b352`'s species, and it
# ### means ### **THE SHARED NORMALISER ALONE DOES NOT CURE IT.**
# ### ### **THE CURE IS A DASH-RUN FOLD APPLIED ON TOP OF `quote_norm`, HERE AND NOT IN IT.** ###
# ### `quote_norm` is an owner instrument every act's emitter and checker import; widening it would widen
# ### every comparison in the record. ### **THIS LOOSENING IS SCOPED TO ANCHOR-FINDING, WHERE A FALSE
# ### ### ALARM COSTS A LOST QUOTATION AND A FALSE MATCH IS CAUGHT BY THE NEGATIVE FIXTURES BELOW.**
# ### ==================================================================================================
_DASHRUN = re.compile(r'-+')


def _loose(s):
    """### `quote_norm`'s fold, plus a dash-run collapse. ### USED ONLY TO FIND THE LINE."""
    return _DASHRUN.sub('-', quote_norm.norm(s))


def _match(line, hint):
    return _loose(hint) in _loose(line)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class AnchorError(LookupError):
    """### RAISED ON A MISS AND ON AN AMBIGUITY. ### Both are refusals, and neither is softened."""


def _lines(path):
    return io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))


# ### ==================================================================================================
# ### ### **THE PRESERVATION HAZARD, MECHANIZED IN PART -- ADDED b396, OPT-IN, DEFAULT OFF.**
# ### ### **THE INCIDENT.** ### `b395` needed the live `Simplicity / RH cascade` row of the cluster
# ### table in `SPIRAL_MAP.md`. ### Its needle matched `b388`'s ### **PRESERVED QUOTATION** ### of
# ### the superseded table -- whose row begins with the same cells -- and, meeting it first,
# ### ### **RESOLVED TO IT SILENTLY.** ### An act editing by that anchor would have edited a
# ### quotation the corpus preserved precisely so that it would not change, and that is
# ### ### **FALSIFICATION AND NOT REPAIR.**
# ###
# ### ### **THE RULE:** ### an anchor used to EDIT excludes preserved blocks by construction, and an
# ### anchor resolving inside one is ### **REFUSED RATHER THAN DISAMBIGUATED.** ### Refusing is the
# ### whole point: a caller told `AMBIGUOUS` picks one, and picking is how the quotation gets edited.
# ###
# ### ### **WHY IT IS OPT-IN AND WHY THE DEFAULT DOES NOT MOVE.** ### An anchor used to QUOTE a
# ### preserved block is CORRECT -- that is how an act cites what an earlier act preserved -- and
# ### every existing caller reads. ### **THE HAZARD IS EDITING BY AN ANCHOR, NOT READING BY ONE**,
# ### so the exclusion belongs to the editing caller and to nobody else. ### Turning it on by default
# ### would break correct readers to guard against a mistake they are not making.
# ###
# ### ### **THE MECHANIZED HALF, AND IT IS A FLOOR:** ### a `>`-prefixed line is a structural fact a
# ### tool reads without judgement, and the paper tree carries `1672` such blocks. ### **BUT `>` IS
# ### ### SUFFICIENT AND NOT NECESSARY.** ### A preservation written any other way -- a banner, an
# ### HTML comment, a convention -- is invisible here. ### **THE JUDGEMENT HALF IS NOT CLAIMED AS
# ### ### MECHANIZED**, and a caller that passes `editing=True` has a floor on the hazard rather than
# ### a guard against it.
# ### ==================================================================================================
_PRESERVED = re.compile(r'^\s*>')


def is_preserved_line(line):
    """### **STRUCTURAL ONLY.** ### True for a blockquoted line. ### It says nothing about a
    ### preservation written any other way, and the caller is told so in the header above."""
    return bool(_PRESERVED.match(line))


def find(path, hint, editing=False):
    """### RETURN `(lineno, line_as_the_file_holds_it)` for the ONE line matching `hint` after normalisation.

    ### ### **RAISES `AnchorError` ON ZERO MATCHES AND ON MORE THAN ONE.**
    ### ### **`editing=True` (OPT-IN, ADDED b396) EXCLUDES BLOCKQUOTED LINES AND REFUSES AN ANCHOR
    ### ### THAT RESOLVES ONLY INSIDE ONE.** ### The default is unchanged and no existing caller moves.
    """
    lines = _lines(path)
    hits = [(i, ln) for i, ln in enumerate(lines, 1) if _match(ln, hint)]
    if editing:
        live = [(i, ln) for i, ln in hits if not is_preserved_line(ln)]
        if hits and not live:
            # ### **REFUSED, NOT DISAMBIGUATED.** ### Every match is inside a preserved block, so
            # ### there is no live line to edit and the caller must be told that and not handed one.
            raise AnchorError('REFUSED -- EVERY MATCH IS INSIDE A PRESERVED (BLOCKQUOTED) BLOCK: '
                              '%r in %s -- lines %s' % (hint, path, [i for i, _l in hits]))
        hits = live
    if not hits:
        raise AnchorError('NO LINE MATCHES: %r in %s' % (hint, path))
    if len(hits) > 1:
        raise AnchorError('AMBIGUOUS (%d lines match): %r in %s -- lines %s'
                          % (len(hits), hint, path, [i for i, _l in hits]))
    return hits[0]


def anchor(path, hint):
    """### THE ANCHOR: the file's own line, byte for byte, ready to hand to `needle_pull`."""
    return find(path, hint)[1]


def find_span(path, hint):
    """### FOR A HINT THAT CROSSES A LINE BREAK. ### Returns `(first_lineno, [lines])`.

    ### ### **THIS EXISTS SO A WRAPPED SENTENCE TEACHES THE CALLER THAT IT WRAPS**, instead of returning
    ### nothing and letting the caller conclude the sentence is absent.
    """
    lines = _lines(path)
    n = len(lines)
    # ### ### **SHORTEST RUN FIRST, AND THE FIXTURE IS WHY.** ### Scanning start-first returns the widest
    # ### window that happens to contain the sentence -- the first run beginning at line 1 -- which is a
    # ### match that teaches the caller nothing about where the sentence is. ### **A SPAN THAT REPORTS THE
    # ### ### WRONG START IS WORSE THAN NO SPAN**, so the length is the outer loop.
    for length in range(1, 7):
        for i in range(0, n - length + 1):
            run = lines[i:i + length]
            if _match(' '.join(run), hint):
                return i + 1, run
    raise AnchorError('NO RUN OF LINES MATCHES: %r in %s' % (hint, path))


def self_test(verbose=True):
    """### FIXTURES, BOTH POLARITIES, ON A FILE WRITTEN HERE AND DRAWN FROM NO BANK.

    ### ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM, AND ONE THAT CANNOT PASS IS NOT ONE EITHER.**
    """
    import tempfile

    def say(s):
        if verbose:
            print(s)

    body = (
        '### the first line, plain\n'
        "### a line with a curly apostrophe: the seat’s own words\n"
        '### a line with an em dash — and text after it\n'
        '### ### a line under a doubled marker, with THE PHRASE inside it\n'
        '### a sentence that wraps between the word\n'
        '### boundary and its continuation\n'
        '### a line that repeats: DUPLICATE TOKEN\n'
        '### another line that repeats: DUPLICATE TOKEN\n'
    )
    fd, p = tempfile.mkstemp(suffix='.txt', prefix='anchor_fixture_')
    os.close(fd)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
    r = []
    try:
        # ### POSITIVE: a straight apostrophe typed against a curly one in the file.
        a = anchor(p, "the seat's own words")
        r.append(('a straight apostrophe finds the curly line, and returns the FILE\'s bytes',
                  a == "### a line with a curly apostrophe: the seat’s own words"))
        # ### POSITIVE: two hyphens typed against an em dash.
        a = anchor(p, 'a line with an em dash -- and text after it')
        r.append(('two hyphens find the em-dash line',
                  a == '### a line with an em dash — and text after it'))
        # ### POSITIVE: a hint with no marker finds a line under a doubled marker.
        a = anchor(p, 'a line under a doubled marker, with THE PHRASE inside it')
        r.append(('a marker-free hint finds the doubled-marker line', a.startswith('### ### ')))
        # ### POSITIVE: the span form returns the whole wrapped run.
        n, run = find_span(p, 'a sentence that wraps between the word boundary and its continuation')
        r.append(('a wrapped sentence returns its RUN of lines, and says where it starts',
                  len(run) == 2 and n == 5))
        # ### NEGATIVE: a genuinely absent sentence RAISES.
        try:
            anchor(p, 'a sentence this file does not contain at all')
            r.append(('an absent sentence RAISES', False))
        except AnchorError:
            r.append(('an absent sentence RAISES', True))
        # ### NEGATIVE: an ambiguous hint RAISES rather than picking one.
        try:
            anchor(p, 'DUPLICATE TOKEN')
            r.append(('an ambiguous hint RAISES rather than choosing', False))
        except AnchorError:
            r.append(('an ambiguous hint RAISES rather than choosing', True))
        # ### NEGATIVE: a changed word does NOT match, so the tool cannot launder a wrong quotation.
        try:
            anchor(p, 'a line with an em DASHED -- and text after it')
            r.append(('a CHANGED WORD does not match', False))
        except AnchorError:
            r.append(('a CHANGED WORD does not match', True))
        # ### NEGATIVE: the single-line form REFUSES a hint that crosses a break, rather than guessing.
        try:
            anchor(p, 'a sentence that wraps between the word boundary and its continuation')
            r.append(('the single-line form REFUSES a wrapped hint, and find_span is the way', False))
        except AnchorError:
            r.append(('the single-line form REFUSES a wrapped hint, and find_span is the way', True))
        # ### ==========================================================================
        # ### ### **THE PRESERVATION FIXTURES, ADDED b396, ON b395'S OWN SHAPE.**
        # ### The file below is `SPIRAL_MAP.md` in miniature: a preserved quotation of a
        # ### superseded row, and the live row that supersedes it, both opening on the
        # ### same cells. ### **THE DEFAULT MUST STILL MEET THE QUOTATION FIRST** -- that
        # ### is the hazard, and a fixture that hides it proves nothing.
        # ### ==========================================================================
        body2 = (
            '### the refreshed table below; the prior one is preserved above it\n'
            '> | **Simplicity / RH cascade** | the SUPERSEDED cells | preserved by b388 |\n'
            '\n'
            '| **Simplicity / RH cascade** | the LIVE cells | the row an act would edit |\n'
            '> | **a row that exists ONLY inside a preserved block** | nowhere else |\n'
        )
        fd2, p2 = tempfile.mkstemp(suffix='.md', prefix='anchor_preserve_')
        os.close(fd2)
        io.open(p2, 'w', encoding='utf-8', newline=chr(10)).write(body2)
        try:
            # ### **THE HAZARD, REPRODUCED:** ### the default finds BOTH and calls it ambiguous;
            # ### with only the quotation present it would resolve to the quotation silently.
            try:
                find(p2, '| **Simplicity / RH cascade** |')
                r.append(('the DEFAULT does not distinguish a quotation from the live row', False))
            except AnchorError as e:
                r.append(('the DEFAULT does not distinguish a quotation from the live row',
                          'AMBIGUOUS' in str(e)))
            # ### **THE MODE:** ### editing=True skips the quotation and lands on the live row.
            n2, ln2 = find(p2, '| **Simplicity / RH cascade** |', editing=True)
            r.append(('editing=True EXCLUDES the preserved block and returns the LIVE row',
                      n2 == 4 and ln2.startswith('| **Simplicity')))
            # ### **REFUSED, NOT DISAMBIGUATED:** ### a hint living only inside a preserved
            # ### block raises rather than handing the caller a line to edit.
            try:
                find(p2, 'a row that exists ONLY inside a preserved block', editing=True)
                r.append(('a hint found ONLY inside a preserved block is REFUSED', False))
            except AnchorError as e:
                r.append(('a hint found ONLY inside a preserved block is REFUSED',
                          'PRESERVED' in str(e)))
            # ### **AND THE DEFAULT STILL READS IT**, because quoting a preserved block is
            # ### correct and every existing caller reads rather than edits.
            n3, _l3 = find(p2, 'a row that exists ONLY inside a preserved block')
            r.append(('the DEFAULT still finds a preserved line, so no reader moves', n3 == 5))
        finally:
            try:
                os.remove(p2)
            except OSError:
                pass
    finally:
        try:
            os.remove(p)
        except OSError:
            pass
    for what, ok in r:
        say('    %-68s %s  %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print('usage: python tools/anchor_from_file.py <file> <hint>')
        print('       python tools/anchor_from_file.py --self-test')
        return 2
    if argv[0] == '--self-test':
        return 0 if self_test(True) else 1
    n, ln = find(argv[0], ' '.join(argv[1:]))
    print('line %d' % n)
    print(ln)
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--self-test':
        print('=' * 100)
        print('anchor_from_file.py -- THE FIXTURES, BOTH POLARITIES.')
        print('=' * 100)
        sys.exit(0 if self_test(True) else 1)
    sys.exit(main(sys.argv[1:]))
