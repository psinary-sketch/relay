# -*- coding: utf-8 -*-
"""test_msplit_b658.py -- THE SENTENCE SPLITTER'S PLANTED CASES, under (R268)(2) (tools/b647_record.py `_MSPLIT`, read by every later sentence
route: b651, b655 and b657's planners).

### b657's defect (a): the split took a closing `**` or `*` after a period as part of the gap between sentences, so the mark belonged to
### neither unit and a cut planned on the units dropped it (relay data/b657_defects.txt (a); ZeroActingPartial.lean at SIDE-lv-conservation
### main 8e3bc76, :104 and :107). The cases: a closing mark after a period stays with its sentence (1)-(4); the split points are the old
### splitter's, the same number of units at the same places (5); no character but whitespace is lost (6); plain sentences split as before (7).
### The positive control is the run against the splitter before the repair (relay data/b658_msplit.txt): (1)-(4) and (6) fail there.
### Usage: python tools/test_msplit_b658.py [path to a b647_record.py] -- the default is tools/b647_record.py.
"""
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'tools', 'b647_record.py')
sys.argv = sys.argv[:1]
_sp = importlib.util.spec_from_file_location('b647_record_under_test', PATH)
B7 = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(B7)
SPLIT = B7._MSPLIT
OLD = re.compile(r'(?<=[.!?])["\'*)\]]*\s+(?=\S)')   # ### the split before the repair, the reference for the split points alone


def units(t):
    return [s for s in SPLIT.split(t.strip()) if s.strip()]


CASES = [
    ('a lone closing `*` after a period (ZeroActingPartial.lean :104`s shape)',
     'neither clause alone yields RH is not compiled.* The programme`s first real step.',
     ['neither clause alone yields RH is not compiled.*', 'The programme`s first real step.']),
    ('a closing `**` after a period (ZeroActingPartial.lean :107`s shape)',
     '**The residue is irreducible by structure.** **Three facts juxtaposed.** Under the premise, the three hold.',
     ['**The residue is irreducible by structure.**', '**Three facts juxtaposed.**', 'Under the premise, the three hold.']),
    ('a closing quote and a closing bracket',
     'He said "stop." Then (it ran.) Next.',
     ['He said "stop."', 'Then (it ran.)', 'Next.']),
    ('four closing marks after a question mark',
     'Is it **(open?)"** Yes.',
     ['Is it **(open?)"**', 'Yes.']),
]
PLAIN = ('One. Two? Three! Four.', ['One.', 'Two?', 'Three!', 'Four.'])


def main():
    res = []
    for i, (what, text, want) in enumerate(CASES, 1):
        got = units(text)
        res.append((i, what, got == want, got))
    texts = [t for _w, t, _x in CASES] + [PLAIN[0]]
    same = all([m.end() for m in SPLIT.finditer(t)] == [m.end() for m in OLD.finditer(t)] for t in texts)
    res.append((5, 'the split points are the old splitter`s: each unit starts where it started', same, None))
    kept = all(re.sub(r'\s', '', ''.join(units(t))) == re.sub(r'\s', '', t) for t in texts)
    res.append((6, 'no character but whitespace is lost by the split', kept, None))
    res.append((7, 'plain sentences split as before', units(PLAIN[0]) == PLAIN[1], units(PLAIN[0])))
    print('test_msplit_b658 -- the splitter at %s' % PATH)
    for n, what, ok, got in res:
        print('  (%d) %s%s ... %s' % (n, what, '' if ok or got is None else ' ; got %r' % (got,), 'PASS' if ok else 'FAIL'))
    nf = sum(1 for r in res if not r[2])
    print('### %d cases, %d failing' % (len(res), nf))
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
