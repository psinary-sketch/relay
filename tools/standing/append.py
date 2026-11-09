# -*- coding: utf-8 -*-
"""standing/append.py -- v1.30.0, (R360)(3)(ii), (iv): THE AUTHOR-WORDS BANKS APPENDED BY THEIR TOOL.

The files written after the lock by design (standing.act.by_design) are appended by their tools and edited by no hand: the hook's row (65)
refuses an Edit or Write of them after the lock. The answers pair has `record answers` (it appends, v1.30.0); the author-words banks had no
route, so a word after the seal was banked by hand or not at all (b749 events (9): no data/b749_author_words.txt written, the record printing
NONE RECEIVED). This route appends a source file's text to one of them, verbatim, beneath one head naming the source and its sha256, and
rewrites nothing already in the bank. The source is a scratch file the seat writes with the Write tool, holding the author's words as received.

  python -X utf8 -u tools/standing/append.py <act> words|preseal <source file>     data/<act>_author_words.txt | _author_words_preseal.txt
"""
import io
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

KINDS = dict(words='author_words', preseal='author_words_preseal')


def main(argv):
    if len(argv) != 3 or argv[1] not in KINDS or not A.ACT_NAME.match(argv[0]):
        sys.exit(__doc__)
    act, kind, src = argv
    rel = 'data/%s_%s.txt' % (act, KINDS[kind])
    if rel not in A.by_design(act):
        sys.exit('### REFUSED: %s IS NOT IN THE DESIGN LIST -- NOTHING WRITTEN' % rel)
    if not os.path.isfile(src):
        sys.exit('### REFUSED: THE SOURCE %s RESOLVES TO NO FILE -- NOTHING WRITTEN' % src)
    text = io.open(src, encoding='utf-8').read()
    if not text.strip():
        sys.exit('### REFUSED: THE SOURCE IS EMPTY -- NOTHING WRITTEN')
    p = os.path.join(A.RELAY, rel)
    prior = A.rd_path(p)
    new = A.words_append(prior, text, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), os.path.basename(src))
    if not new.startswith(prior.rstrip('\n')):
        sys.exit('### REFUSED: THE APPEND WOULD REWRITE THE BANK -- NOTHING WRITTEN')
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(new)
    os.replace(p + '.tmp', p)
    print('appended to %s: %d line(s) beneath %d; nothing in the bank rewritten' % (rel, len(new.split('\n')) - len(prior.split('\n')), len(prior.split('\n')) - 1 if prior else 0))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
