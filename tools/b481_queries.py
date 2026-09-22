# -*- coding: utf-8 -*-
"""b481_queries.py -- THE NEGATIVE SEARCHES, RUN AND BANKED.
### ### **A HALT IS ONLY A HALT IF THE SEARCH WAS ACTUALLY RUN.** ### Each query below is executed
### over the LIVE corpus and the memory stores, and its answer is the KEY found or `NO KEY`.
### **NOTHING IS FETCHED; NO PLATFORM IS CALLED.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects')
NL = chr(10)
OUT = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def corpus():
    for base, dirs, files in os.walk(PP):
        if 'archive' in base or '.git' in base:
            continue
        for fn in files:
            if fn.endswith('.md'):
                yield os.path.relpath(os.path.join(base, fn), PP), read(os.path.join(base, fn))
    for d in sorted(os.listdir(MEM)):
        p = os.path.join(MEM, d, 'memory')
        if not os.path.isdir(p):
            continue
        for fn in sorted(os.listdir(p)):
            if fn.endswith('.md'):
                yield 'memory[%s]/%s' % (d, fn), read(os.path.join(p, fn))


CORPUS = list(corpus())

QUERIES = [
    ("a (c') validation job, by that name, other than the gate's own trigger",
     lambda l: "validation job" in l and re.search(r"\(c['’′]\)", l)
     and 'Deposit-state reconciliation' not in l),
    ("a state -- cleared, pending, failed -- recorded for a (c') job",
     lambda l: re.search(r"\(c['’′]\)", l)
     and re.search(r'\b(cleared|clearing|pending|failed|passed)\b', l, re.I)
     and 'Deposit-state reconciliation' not in l),
    ('the drafted historical note for record 21432399, written anywhere in the corpus',
     lambda l: 'Historical note: this record deposits the monograph' in l),
    ('a deposited version for Zenodo record 19675356',
     lambda l: '19675356' in l and re.search(r'v\d+\.\d+', l)),
    ('a deposit-state line in the executor memory store',
     lambda l: False),  # ### replaced below: this one is scoped to one store, not the corpus
]


def main():
    print('=' * 96)
    print('b481 -- THE NEGATIVE SEARCHES, RUN OVER %d LIVE FILES.' % len(CORPUS))
    print('=' * 96)
    for q, pred in QUERIES[:4]:
        hits = []
        for name, text in CORPUS:
            for i, l in enumerate(text.split(NL)):
                if pred(l):
                    hits.append('%s:%d' % (name, i + 1))
        OUT.append('QUERY: %s' % q)
        if hits:
            OUT.append('  ### KEY: %s' % ' ; '.join(hits[:6]))
        else:
            OUT.append('  ### NO KEY.')

    # ### ### **THE FIFTH QUERY IS SCOPED TO ONE STORE**, because a corpus-wide hit would answer a
    # ### different question. ### The gate names "both memories (session + executor)".
    other = [d for d in sorted(os.listdir(MEM))
             if os.path.isdir(os.path.join(MEM, d, 'memory')) and d != 'D--']
    pat = re.compile(r'v1\.1\.2|v5\.10\.2|21539167|0e5233f|21520474|v0\.10\.0|93c27ec|21539068', re.I)
    hits = []
    for d in other:
        p = os.path.join(MEM, d, 'memory')
        for fn in sorted(os.listdir(p)):
            for i, l in enumerate(read(os.path.join(p, fn)).split(NL)):
                if pat.search(l):
                    hits.append('memory[%s]/%s:%d' % (d, fn, i + 1))
    OUT.append('QUERY: a deposit-state line in any memory store other than the session store')
    OUT.append('  ### %s' % ('KEY: ' + ' ; '.join(hits[:6]) if hits else 'NO KEY.'))
    OUT.append('  ### stores other than the session store, searched whole : %s'
               % (', '.join(other) or 'NONE'))

    for l in OUT:
        print(l)
    n = sum(1 for l in OUT if 'NO KEY' in l)
    print('')
    print('  ### ### **QUERIES RUN : 5. ### ANSWERED `NO KEY` : %d.**' % n)
    print('  ### ### **EACH WAS EXECUTED OVER FILES ON DISK. ### NOTHING WAS FETCHED.**')
    print('=' * 96)
    io.open(os.path.join(D, 'b481_index_queries.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(OUT) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
