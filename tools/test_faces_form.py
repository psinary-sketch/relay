# -*- coding: utf-8 -*-
"""test_faces_form.py -- THE TEST OF terminal_table`s FACES_LEDGER-LINE FORM, (R181)(2), written at b571.

### (1) a directive `SUPERSEDES FACES_LEDGER :497 for ch_iff_rh:` removes ch_iff_rh`s cell read from FACES_LEDGER line 497;
### (2) a cell of another ledger for the same terminal is kept; (3) the directive line`s own cell for that terminal is
### removed (the line adds no cell); (4) another terminal`s cell on the same FACES_LEDGER line is kept; (5) the pattern reads
### the ruled line`s words, backticked and not; (6) a directive citing a line that holds no cell for its terminal is not hit
### and `faces_refusals` names it; (7) LIVE: a full in-memory regeneration with such a directive injected REFUSES --
### `build` raises FacesRefusal and `main` returns 8 -- and no table file is written (each file`s bytes compared before and
### after). Usage: python tools/test_faces_form.py
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TABLE_FILES = ['terminal_table.json', 'terminal_table.md', 'terminal_table_prior.json', 'terminal_table_run.txt',
               'terminal_table_diff.json']


def digests():
    out = {}
    for f in TABLE_FILES:
        p = os.path.join(ROOT, 'data', f)
        out[f] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    return out


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-100s %s' % (label, 'PASS' if cond else '### FAIL'))

    F, FI = TT.FACES_LABEL, TT.FIND_LABEL
    d = (497, 'ch_iff_rh', FI, 9000)
    a = dict(ledger=F, line=497, grade='ENCODES-CONCLUSION', quote='RH restated')
    b = dict(ledger=FI, line=10, grade='DERIVES', quote='F')
    own = dict(ledger=FI, line=9000, grade='DERIVES', quote='the directive line')
    TT._FACES_HIT.clear()
    out = TT.supersede_faces([a, b, own], 'SIDEExplicitFormula.B321.ch_iff_rh', [d])
    want('(1) the FACES_LEDGER :497 cell is removed for ch_iff_rh (qualified name)', a not in out)
    want('(2) the FINDINGS :10 cell of the same terminal is kept', b in out)
    want('(3) the directive line`s own cell for the terminal is removed', own not in out)
    other = TT.supersede_faces([dict(a)], 'Register2_conservationHypothesis', [d])
    want('(4) another terminal`s cell on FACES_LEDGER :497 is kept', len(other) == 1)
    m1 = TT.FACES_SUP_RE.search('SUPERSEDES FACES_LEDGER :497 for ch_iff_rh: T0 -- the words')
    m2 = TT.FACES_SUP_RE.search('SUPERSEDES FACES_LEDGER :497 for `ch_iff_rh`: T0')
    want('(5) the pattern reads the ruled line, unbackticked and backticked (%s, %s)'
         % (m1 and m1.groups(), m2 and m2.groups()),
         m1 and m2 and m1.groups() == ('497', 'ch_iff_rh') == m2.groups())
    want('(6a) the directive that removed a cell is not refused', TT.faces_refusals([d]) == [])
    bad = (498, 'ch_iff_rh', FI, 9001)
    TT.supersede_faces([dict(a)], 'SIDEExplicitFormula.B321.ch_iff_rh', [bad])
    want('(6b) a directive citing :498 (no cell for ch_iff_rh there) is named by faces_refusals',
         TT.faces_refusals([d, bad]) == [bad])
    # ### (7) LIVE: the whole regeneration, with the bad directive injected beside whatever the ledgers carry
    before = digests()
    TT._FACES_HIT.clear()
    live = TT.faces_directives()
    TT._FACES_DIRECTIVES[:] = [x for x in TT._FACES_DIRECTIVES if x] + [bad, None]
    rc = TT.main()
    after = digests()
    want('(7a) LIVE: main() with the bad directive injected returns 8 (REFUSED) -- read %s' % rc, rc == 8)
    want('(7b) LIVE: no table file written (sha256 of %d files equal before and after)' % len(TABLE_FILES), before == after)
    want('(7c) LIVE: the ledgers` own directives read (%s)' % live, isinstance(live, list))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
