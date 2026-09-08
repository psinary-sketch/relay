# -*- coding: utf-8 -*-
"""gate_needle.py -- THE ANCHORED GATE ARM, built b363 by the author's order.

### ### **THE SPECIES THIS RETIRES, AND IT IS NOT THE ONE `anchor_from_file.py` RETIRED.** ### That tool
### cured a QUOTATION typed rather than read. ### This one cures the same fault one level out: ### **A GATE
### ### ARM'S NEEDLE TYPED RATHER THAN READ**, and the two failure shapes an arm adds on top of it.
###
### ### **THE THREE SHAPES, EACH BANKED AT ITS OWN ACT:**
### ### **(1) THE TYPED NEEDLE.** ### A suite types the sentence it means to look for and types it wrong --
###     a marker prefix the file does not carry on that line, a noun the file does not use. ### The arm
###     returns `False` and the seat reads a FAILING GATE where the work was correct.
### ### **(2) THE PRESENTATION MISMATCH.** ### The needle is right and the haystack renders it differently:
###     emphasis markers inside the phrase, a line break through the middle of it. ### The arm returns
###     `False` for a reason that has nothing to do with what the arm is asking.
### ### **(3) THE INHERITED NEEDLE.** ### A suite is derived from the previous act's and keeps a needle
###     whose sentence belongs to that act. ### **THIS IS THE WORST OF THE THREE, BECAUSE IT FAILS
###     ### SILENTLY AND LOOKS EXACTLY LIKE (1).**
###
### ### **WHAT THIS FILE DOES ABOUT THEM.** ### `build` takes a file and a hint and returns ### **THE
### ### FILE'S OWN LINE**, delegating to `anchor_from_file.py`, IMPORTED and not reimplemented; it RAISES on
### a hint that matches nothing and on a hint that matches twice. ### `present` builds the needle that way
### and then compares it against the haystack with ### **BOTH SIDES PUT THROUGH ONE NORMALISATION THAT
### ### DISCARDS PRESENTATION.**
### ### ### **SO SHAPE (3) BECOMES A LOUD REFUSAL INSTEAD OF A SILENT `False`**, which is the whole of what
### this file buys over typing the needle carefully.
###
### ### **WHY ITS NORMALISATION IS NOT `gate_text.flat`, AND WHY THAT FILE IS NOT EDITED.** ### `flat`
### strips repeated `###` markers only at the START of a line. ### `b362` printed a quoted phrase across two
### INDENTED lines and a marker sat in the middle of the phrase after flattening, so no comparison could
### find it. ### **THIS FILE STRIPS MARKER RUNS WHEREVER THEY OCCUR**, which is wider -- and the widening is
### scoped HERE rather than written into `gate_text`, because every act's suite imports that one and
### widening it would widen every comparison in the record. ### **THAT IS `b354`'s OWN RULE ABOUT
### ### `quote_norm`, APPLIED TO ITS SUCCESSOR.**
###
### ### ### **THE REACH, STATED HERE SO THIS FILE IS NOT TRUSTED BEYOND IT:**
### ### ### **(1) IT MAKES A NEEDLE EQUAL TO A FILE'S LINE. ### IT DOES NOT MAKE THE ARM RIGHT.**
### ### ### **(2) IT DOES NOT REACH A WRONG ARM** -- one whose predicate tests something other than its
###     label. ### A needle built from a file is still a needle for the wrong question, and no needle tool
###     ever reaches this. ### **THE RECORD HAS TWO OF THESE AND `b363` COUNTS THEM.**
### ### ### **(3) IT DOES NOT REACH A MISSING SENTENCE.** ### An arm that asks a file for something the
###     file genuinely does not carry is an arm DOING ITS JOB. ### **A HELPER THAT MADE SUCH AN ARM QUIET
###     ### WOULD BE A DEFECT AND NOT A CURE**, and the fixtures below hold that polarity on purpose.
### ### ### **(4) A NORMALISATION THAT DISCARDS PRESENTATION CANNOT SEE A DIFFERENCE THAT LIVES ONLY IN
###     ### PRESENTATION.** ### `quote_norm`'s own stated limit, inherited here.
### ### ### **(5) IT DOES NOT LAUNDER A CHANGED WORD.** ### `b355` found the tool refusing a dropped
###     possessive and was right to: ### **A CHANGED WORD IS A CHANGED QUOTATION**, and the negative fixture
###     below is what makes that refusal principled rather than accidental.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm              # noqa: E402
import anchor_from_file as AF  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### MARKER RUNS, WHEREVER THEY OCCUR -- not only at the start of a line. ### See the header for why this
# ### is here and not in `gate_text`.
_MARKERS = re.compile(r'#{2,}')
_EMPH = re.compile(r'\*{1,3}')
_WS = re.compile(r'\s+')


class NeedleError(LookupError):
    """### RAISED ON A MISS AND ON AN AMBIGUITY. ### **BOTH ARE REFUSALS AND NEITHER IS SOFTENED.**"""


def norm(s):
    """### THE NORMALISATION THAT DISCARDS PRESENTATION. ### Markers, emphasis and whitespace runs go;
    ### **WORDS DO NOT.** ### A changed word survives it and is therefore still a miss."""
    return _WS.sub(' ', _EMPH.sub(' ', _MARKERS.sub(' ', quote_norm.norm(s)))).strip()


def build(path, hint):
    """### THE NEEDLE, READ FROM THE FILE. ### RETURNS `(lineno, line)`. ### **RAISES `NeedleError` ON A
    ### MISS AND ON AN AMBIGUITY** -- which is how an inherited needle stops being silent."""
    try:
        return AF.find(path, hint)
    except AF.AnchorError as e:
        raise NeedleError('%s :: %s' % (os.path.basename(path), str(e).split(chr(10))[0]))


def present(haystack, path, hint):
    """### BUILD THE NEEDLE FROM `path`, THEN ASK WHETHER `haystack` CARRIES IT.

    ### ### **RETURNS `(bool, lineno, needle)`.** ### The boolean is the arm's answer; the line number and
    ### the needle are printed by the caller so a reader can check the arm rather than trust it.
    ### ### **IT RAISES RATHER THAN RETURNING `False` WHEN THE NEEDLE CANNOT BE BUILT AT ALL**, because a
    ### needle that is not in its own file is a defect in the ARM and not an answer about the haystack.
    """
    n, line = build(path, hint)
    return (norm(line) in norm(haystack)), n, line


def present_needle(haystack, needle):
    """### THE SAME COMPARISON FOR A NEEDLE THE CALLER ALREADY HOLDS. ### **NO BUILD, SO NO RAISE** -- for
    ### an arm whose needle is a phrase rather than a file's line."""
    return norm(needle) in norm(haystack)


def absent_exact(path, line):
    """### THE MUST-FAIL FORM, UNCHANGED IN SEMANTICS: ### **WHOLE-LINE EQUALITY, NEVER SUBSTRING, AND NO
    ### NORMALISATION.** ### A must-fail fixture that normalised would be a must-fail fixture that could be
    ### satisfied by a near miss."""
    for ln in io.open(path, encoding='utf-8', errors='replace').read().split(chr(10)):
        if ln.rstrip() == line.rstrip():
            return False
    return True


# ### ==================================================================================================
# ### THE FIXTURES. ### **THEIR TEXT IS WRITTEN HERE AND DRAWN FROM NO BANK**, so a bank edited later
# ### cannot change what they test.
# ### ==================================================================================================
_FILE = ('### ### **A SENTENCE THIS FILE CARRIES ON ONE LINE.**' + chr(10) +
         '### ### **A SENTENCE THAT RUNS ACROSS A DOUBLED' + chr(10) +
         '### ### MARKER AND MUST STILL BE FOUND.**' + chr(10) +
         "### the corpus's arrays, with a possessive that matters." + chr(10))

# ### **THE RENDERED HAYSTACK DIFFERS FROM THE FILE IN PRESENTATION AND IN NOTHING ELSE:** ### the markers
# ### move, the emphasis splits, a line break falls inside the sentence and the whole thing is indented.
# ### **THE WORDS AND THE PUNCTUATION ARE THE FILE'S.** ### An earlier version of this fixture also changed
# ### a word's case and its full stop, and the tool refused it -- correctly, and the fixture was the thing
# ### that was wrong. ### **A FIXTURE THAT TESTS TWO THINGS AT ONCE TESTS NEITHER.**
_HAY_RENDERED = ('  and here it is again, differently rendered:' + chr(10) +
                 '  ### **A SENTENCE THIS FILE CARRIES ON' + chr(10) +
                 '  ### ### ONE LINE.** ### wrapped by an emitter that indents and re-marks.' + chr(10))
_HAY_ABSENT = '  a haystack that simply does not carry it at all.' + chr(10)


def self_test(verbose=True):
    """### BOTH POLARITIES. ### **AND THE POSITIVE POLARITY INCLUDES AN ARM THAT SHOULD FIRE AND STILL
    ### DOES**, which the order required and which is the polarity a helper of this kind loses first."""
    import tempfile

    def say(s):
        if verbose:
            print(s)

    tmp = tempfile.mkdtemp(prefix='gate_needle_')
    p = os.path.join(tmp, 'fixture.txt')
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(_FILE)
    r = []

    # ### (1) THE NEEDLE IS BUILT FROM THE FILE AND FOUND IN A DIFFERENTLY RENDERED HAYSTACK.
    ok, _n, _needle = present(_HAY_RENDERED, p, 'A SENTENCE THIS FILE CARRIES ON ONE LINE')
    r.append(('a needle built from the file is found in a differently rendered haystack', ok))

    # ### (2) ### **THE ARM THAT SHOULD FIRE, AND STILL DOES.**
    ok2, _n, _needle = present(_HAY_ABSENT, p, 'A SENTENCE THIS FILE CARRIES ON ONE LINE')
    r.append(('### and an arm whose sentence is ABSENT still FIRES', not ok2))

    # ### (3) A HINT THAT MATCHES NOTHING IN ITS OWN FILE RAISES, RATHER THAN ANSWERING FALSE.
    try:
        present(_HAY_RENDERED, p, 'A SENTENCE NO FILE HERE CARRIES')
        r.append(('a hint absent from its own file RAISES', False))
    except NeedleError:
        r.append(('a hint absent from its own file RAISES', True))

    # ### (4) AND SO DOES ONE THAT MATCHES TWICE.
    p2 = os.path.join(tmp, 'twice.txt')
    io.open(p2, 'w', encoding='utf-8', newline=chr(10)).write('the same line' + chr(10) + 'the same line' + chr(10))
    try:
        build(p2, 'the same line')
        r.append(('an ambiguous hint RAISES', False))
    except NeedleError:
        r.append(('an ambiguous hint RAISES', True))

    # ### (5) THE WRAPPED SENTENCE, WHICH `gate_text.flat` LOSES WHEN THE CONTINUATION IS INDENTED.
    hay_wrapped = ('    ### ### A SENTENCE THAT RUNS ACROSS A DOUBLED' + chr(10) +
                   '    ### ### MARKER AND MUST STILL BE FOUND.' + chr(10))
    r.append(('a phrase wrapped through an INDENTED marker is still found',
              present_needle(hay_wrapped, 'A SENTENCE THAT RUNS ACROSS A DOUBLED MARKER AND MUST STILL BE FOUND')))

    # ### (6) ### **AND A CHANGED WORD IS STILL A MISS.** ### b355's lesson: a tool that matched a dropped
    # ### possessive would LAUNDER A WRONG QUOTATION.
    r.append(('### a DROPPED POSSESSIVE is still a MISS',
              not present_needle("### the corpus's arrays, with a possessive that matters.",
                                 'the corpus arrays, with a possessive that matters')))

    # ### (7) AND THE MUST-FAIL FORM IS NOT NORMALISED.
    r.append(('the must-fail form is whole-line and un-normalised',
              absent_exact(p, '### ### A SENTENCE THIS FILE CARRIES ON ONE LINE.')
              and not absent_exact(p, '### ### **A SENTENCE THIS FILE CARRIES ON ONE LINE.**')))

    for what, ok3 in r:
        say('    %-66s %-6s %s' % (what, ok3, 'PASS' if ok3 else '### FAIL ###'))
    return all(ok3 for _w, ok3 in r)


if __name__ == '__main__':
    print('gate_needle.py -- self-test (both polarities):')
    sys.exit(0 if self_test() else 1)
