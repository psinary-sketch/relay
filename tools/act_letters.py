# -*- coding: utf-8 -*-
"""act_letters.py -- ONE LETTERING, (R324)(6)(v), standing clauses v5 row (78): the corrigendum tool and the suite import this module, so a
defect's letter has one form from the tool that writes it to the arm that reads it.

b713's event (14): data/b713_corrigendum.json lettered its items "a'" ... "d'" (U+0027) where the suite's G-CORRIGENDUM-ENTERED wanted 'a′'
... 'd′' (U+2032); the two tools each spelt the prime, and the arm failed on a character. Here:
  * SEQ, nth(i), after(prev, k): the letters in order -- (a)-(z), then (a′)-(z′), then (a″)-(z″) -- the prime always U+2032;
  * canon(x): a letter read in any of the three prime forms the record carries (U+0027, U+2019, U+2032) returned in the one form;
  * forms(letters): the prime characters a list of letters uses; mixed(letters): True where a list uses more than one -- a record
    lettered in two forms is refused, and a record in one form (b713's, all U+0027) reads as its canonical letters;
  * read(letters): the canonical letters, or ValueError on a mixed list or a letter outside SEQ.
Pure: no file read, no write.
"""
import re

PRIME, DPRIME = '′', '″'
PRIMES_READ = ("'", '’', PRIME)
BASE = 'abcdefghijklmnopqrstuvwxyz'
SEQ = tuple(BASE) + tuple(c + PRIME for c in BASE) + tuple(c + DPRIME for c in BASE)
LETTER = re.compile(r"^([a-z])(['’′]|['’′]{2}|″)?$")


def nth(i):
    """the i-th letter, from 0: nth(0) 'a', nth(26) 'a′'."""
    return SEQ[i]


def canon(x):
    """a letter in the one form: "a'" and 'a’' and 'a′' all 'a′'; "a''" and 'a″' 'a″'."""
    m = LETTER.match(x or '')
    if not m:
        raise ValueError('not a letter: %r' % (x,))
    p = m.group(2) or ''
    return m.group(1) + ('' if not p else PRIME if len(p) == 1 and p != DPRIME else DPRIME)


def forms(letters):
    """the prime characters used across a list of letters, each by its first character (the double prime U+2033 counted as U+2032's)."""
    out = set()
    for x in letters:
        m = LETTER.match(x or '')
        if m and m.group(2):
            out.add(PRIME if m.group(2) == DPRIME else m.group(2)[0])
    return out


def mixed(letters):
    return len(forms(letters)) > 1


def read(letters):
    """the canonical letters of a record, refusing a record lettered in two forms."""
    if mixed(letters):
        raise ValueError('a mixed lettering: %s in %r' % (sorted(forms(letters)), list(letters)))
    out = [canon(x) for x in letters]
    bad = [x for x in out if x not in SEQ]
    if bad:
        raise ValueError('letters outside the sequence: %r' % bad)
    return out


def after(prev, k):
    """the k letters after a record's last: after(['a', ..., 'n'], 12) is 'o'-'z'; after a list ending 'z', 'a′' follows."""
    prev = read(prev)
    start = SEQ.index(prev[-1]) + 1 if prev else 0
    if start + k > len(SEQ):
        raise ValueError('the sequence ends at %r' % SEQ[-1])
    return list(SEQ[start:start + k])
