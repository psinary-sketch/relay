# -*- coding: utf-8 -*-
"""standing/needles.py -- A NEEDLE READ WORD FOR WORD FROM THE FACE (v1.2.0; (R328)(7), b717's event (1), the class FORM). The face's
writer and the arm that reads it take a needle from one table: the face composer writes `line(key, ...)` and the arm asks `carries(face,
key, ...)`, which reads the face unwrapped (each line's leading `###` marks removed and its whitespace collapsed, b703's unwrap), so a
hard wrap through the needle does not hide it and a sentence in the writer's own words is not read as the needle. Provenance: b716's and
b717's faces wrote "the root route run dry once on the pre-root tree (step [2]), READY True" where G-ROOTDRY-READY wanted "the root
route`s dry run READY True" -- the same claim in two forms, the arm failing on both faces (b716 event (2), b717 event (1)).

  NEEDLES {key: template}     line(key, **kw) -> text     carries(text, key, **kw) -> bool     unwrap(text) -> text
"""
import re

NL = '\n'

NEEDLES = {
    'rootdry': 'the root route`s dry run READY {ready}',
}


def unwrap(t):
    """b703's unwrap (tools/b703_checks.py :701-:702), carried: each line's leading `###` marks removed, the lines joined, whitespace
    collapsed."""
    return ' '.join(' '.join(re.sub(r'^\s*(?:###\s*)+', '', l) for l in (t or '').replace('\r', '').split(NL)).split())


def line(key, **kw):
    """the needle the face writes, from the table."""
    return NEEDLES[key].format(**kw)


def carries(text, key, **kw):
    """the face carries the needle word for word, read unwrapped."""
    return unwrap(line(key, **kw)) in unwrap(text)
