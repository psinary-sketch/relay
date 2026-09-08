# -*- coding: utf-8 -*-
"""gate_content.py -- THE REWRITE RULE: AN ADDRESS PREDICATE BECOMES A CONTENT PREDICATE.

### ### **THE RULE, IN ONE LINE:** ### where an arm reads a file's line AT A STORED NUMBER, it reads the
### file's line BY THE TEXT IT EXPECTS THERE INSTEAD.
###     ### **BEFORE:** ### `io.open(p).read().splitlines()[rec['line'] - 1]`
###     ### **AFTER :** ### `gate_content.line_by_content(p, rec['text'])`
### ### **AND THAT IS WHY THIS FILE IS A HELPER AND NOT A WORK-ORDER.** ### `b366`'s order fixed the form
### by a test -- a fixture-backed helper IF the substitution is one line of shared code, a work-order with
### its price if it is not -- and it is one line.
### ### **THE HELPER IS A WRAPPER AND SAYS SO.** ### `anchor_from_file.find` (`b354`) already returns a
### file's own line from a hint; this file NAMES the substitution, carries the fixtures that show what it
### changes, and adds nothing to the search.
### ### ### **WHAT THE SUBSTITUTION BUYS, EXACTLY:** ### an address predicate silently reads a DIFFERENT
### ### LINE when the file moves; a content predicate reads the SAME LINE at a new number, and RAISES when
### ### the text is genuinely gone. ### **THE FIXTURES BELOW SHOW BOTH, AND THE SECOND IS THE ONE THAT
### ### MATTERS: A REWRITE THAT ONLY EVER QUIETENED ARMS WOULD BE A SOFTENER** (`b348`).
### ### **WHAT IT DOES NOT BUY, AND THE HEADER SAYS SO RATHER THAN LETTING IT BE ASSUMED:**
###   ### (1) ### **IT DOES NOT MAKE THE ARM RIGHT.** ### An arm asking the wrong question by address
###     asks the wrong question by content (`b365`'s `WRONG_ARM`).
###   ### (2) ### **IT CANNOT BE APPLIED WHERE NO CONTENT WAS BANKED.** ### An arm whose record carries a
###     line number and no text has nothing to look up BY, and the substitution is unavailable until a
###     text is derived and banked first.
###   ### (3) ### **IT IS NOT A CURE FOR AN ARM THAT SHOULD BE DATED.** ### `b366`'s `(R2)` decides which
###     arms ought to be standing; this file only makes the writing possible.
###   ### (4) ### **AND IT MOVES NO PAST SUITE.** ### The rule is for arms written from here on.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import anchor_from_file as AF   # noqa: E402


class ContentError(LookupError):
    """### RAISED WHERE THE TEXT IS NOT THERE, OR IS THERE TWICE. ### **NEVER RETURNS A GUESS.**"""


def line_by_content(path, text):
    """### THE SUBSTITUTION. ### **RETURNS `(lineno, line)` FOUND BY WHAT THE LINE SAYS, NOT BY WHERE IT
    ### SAT.** ### Raises `ContentError` if the text is absent or ambiguous."""
    try:
        return AF.find(path, text)
    except AF.AnchorError as e:
        raise ContentError('%s :: %s' % (os.path.basename(path), str(e).split(chr(10))[0]))


def line_by_address(path, lineno):
    """### THE SHAPE BEING REPLACED, WRITTEN OUT ONCE SO THE FIXTURES CAN COMPARE THEM.
    ### **THIS IS NOT FOR USE IN AN ARM.** ### It is here to be the control."""
    lines = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    if not 1 <= lineno <= len(lines):
        raise IndexError('line %d outside %s' % (lineno, os.path.basename(path)))
    return lineno, lines[lineno - 1]


# ### ==================================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES. ### THEIR TEXT IS WRITTEN HERE AND DRAWN FROM NO BANK**, so a
# ### file edited later cannot change what they test.
# ### ==================================================================================================
_SENTENCE = 'THE ROW THIS ARM WAS WRITTEN ABOUT.'
_BEFORE = ('a first line' + chr(10) + 'a second line' + chr(10) + _SENTENCE + chr(10) +
           'a line after' + chr(10))
_MOVED = ('an inserted line' + chr(10) + 'another inserted line' + chr(10) +
          'a first line' + chr(10) + 'a second line' + chr(10) + _SENTENCE + chr(10) +
          'a line after' + chr(10))
_GONE = ('a first line' + chr(10) + 'a second line' + chr(10) +
         'THE ROW THIS ARM WAS WRITTEN ABOUT, REWORDED.' + chr(10) + 'a line after' + chr(10))
_TWICE = (_SENTENCE + chr(10) + 'a middle line' + chr(10) + _SENTENCE + chr(10))


def self_test(verbose=True):
    """### **BOTH POLARITIES, AND THE SECOND POLARITY IS THE POINT.**"""
    import tempfile
    tmp = tempfile.mkdtemp(prefix='gate_content_')

    def put(name, body):
        p = os.path.join(tmp, name)
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
        return p

    before, moved, gone, twice = (put('before.txt', _BEFORE), put('moved.txt', _MOVED),
                                  put('gone.txt', _GONE), put('twice.txt', _TWICE))
    r = []

    # ### (1) ON AN UNMOVED FILE THE TWO AGREE. ### **THE SUBSTITUTION IS NOT A CHANGE OF ANSWER.**
    na, la = line_by_address(before, 3)
    nc, lc = line_by_content(before, _SENTENCE)
    r.append(('on an unmoved file, address and content return the same line',
              (na, la) == (nc, lc)))

    # ### (2) ### **ON A MOVED FILE THE ADDRESS READS THE WRONG LINE AND SAYS NOTHING.**
    _n, wrong = line_by_address(moved, 3)
    r.append(('### on a MOVED file the address predicate reads a DIFFERENT line, silently',
              wrong.strip() != _SENTENCE))

    # ### (3) ### **AND THE CONTENT PREDICATE FINDS IT, AT ITS NEW NUMBER.**
    n2, l2 = line_by_content(moved, _SENTENCE)
    r.append(('### and the content predicate finds it at its new number', n2 == 5 and l2 == _SENTENCE))

    # ### (4) ### **AND WHEN THE TEXT IS GENUINELY GONE IT RAISES.** ### An arm that went quiet here
    # ### would be a softener, and b348 forbids softening a needle.
    try:
        line_by_content(gone, _SENTENCE)
        r.append(('### a genuinely CHANGED sentence RAISES, it does not go quiet', False))
    except ContentError:
        r.append(('### a genuinely CHANGED sentence RAISES, it does not go quiet', True))

    # ### (5) AND AN AMBIGUOUS ONE RAISES RATHER THAN CHOOSING.
    try:
        line_by_content(twice, _SENTENCE)
        r.append(('a text present twice RAISES rather than choosing', False))
    except ContentError:
        r.append(('a text present twice RAISES rather than choosing', True))

    # ### (6) AND THE CONTROL STILL FAILS THE WAY A CONTROL SHOULD.
    try:
        line_by_address(before, 99)
        r.append(('the address form still raises on an out-of-range line', False))
    except IndexError:
        r.append(('the address form still raises on an out-of-range line', True))

    for what, ok in r:
        if verbose:
            print('    %-70s %-6s %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


if __name__ == '__main__':
    print('gate_content.py -- self-test (both polarities):')
    sys.exit(0 if self_test() else 1)
