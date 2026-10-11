# -*- coding: utf-8 -*-
"""test_module_header.py -- THE PLANTED TEST OF tools/module_header.py, under (R259)(2)(c).

### Scratch files written here and drawn from no kernel: (1) a header claiming a theorem the file lacks FAILS; (2) a header matching its file
### PASSES; (3) a header describing a def as proved OVERREACHES; (4) a header describing as proved a theorem whose proof is `sorry`
### OVERREACHES; (5) a RESTATED declaration described as proved OVERREACHES; (6) a theorem another file of the kernel declares is a
### REFERENCE; (7) a name in a clause naming a .lean file is a REFERENCE; (8) a claim wrapped over two lines is read whole; (9) "computed by
### `f` and proved by `decide`" does not describe `f` as proved; (10) a star inside a code span is not emphasis; (11) "Proves `X`" with a
### capital is read; (12) a file with no head `/-!` block has no header.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import module_header as M   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def file_(header, body='theorem real_thm : True := trivial\n'):
    return '/-!\n%s\n-/\nnamespace P\n%s\nend P\n' % (header, body)


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-96s %s' % (label, 'PASS' if cond else '### FAIL'))

    def rows(text, restated=(), others=()):
        return M.rows_of('PLANTED', 'P.lean', text, set(restated), set(others))[1]

    r = rows(file_('This module proves `missing_thm`, the planted claim.'))
    want('(1) a header claiming a theorem the file lacks: FAILS %s' % [x['why'] for x in r], len(r) == 1 and 'no such name' in r[0]['why'])
    r = rows(file_('This module proves `real_thm`.'))
    want('(2) a header matching its file: PASSES (rows %d)' % len(r), r == [])
    r = rows(file_('The value `planted_def` is proved.', 'def planted_def : Nat := 0\n'))
    want('(3) a def described as proved: OVERREACHES %s' % [x['why'] for x in r], len(r) == 1 and 'declares it a def' in r[0]['why'])
    r = rows(file_('Theorem `open_thm` is proved here.', 'theorem open_thm : 1 = 2 := by\n  sorry\n'))
    want('(4) a theorem whose proof is sorry described as proved: OVERREACHES %s' % [x['why'] for x in r],
         len(r) >= 1 and all('`sorry`' in x['why'] for x in r))
    r = rows(file_('This module proves `goldbach`.', 'theorem goldbach : True := trivial\n'), restated=['goldbach'])
    want('(5) a RESTATED declaration described as proved: OVERREACHES %s' % [x['why'] for x in r], len(r) == 1 and 'RESTATED' in r[0]['why'])
    r = rows(file_('This module proves `other_thm` again.'), others=['other_thm'])
    want('(6) a theorem another file of the kernel declares: REFERENCE (rows %d)' % len(r), r == [])
    r = rows(file_('The classes (in `Bridge/Other.lean`) are proved not to occur (`far_thm`).'))
    want('(7) a name in a clause naming a .lean file: REFERENCE (rows %d)' % len(r), r == [])
    r = rows(file_('The planted\nfact `missing_two` is\nproved.'))
    want('(8) a claim wrapped over three lines read whole: FAILS %s' % [x['name'] for x in r], [x['name'] for x in r] == ['missing_two'])
    r = rows(file_('Its grade is computed by `grade` and proved by `decide`.', 'def grade : Nat := 0\n'))
    want('(9) "computed by `grade` and proved by `decide`" does not call `grade` proved (rows %d)' % len(r), r == [])
    r = rows(file_('The three `stormer_*.length` counts are proved by decide.'))
    want('(10) a star inside a code span is not emphasis: no name invented (rows %d)' % len(r), r == [])
    r = rows(file_('Proves `missing_cap`: the planted claim.'))
    want('(11) "Proves `X`" with a capital read: FAILS %s' % [x['name'] for x in r], [x['name'] for x in r] == ['missing_cap'])
    line, r = M.rows_of('PLANTED', 'Q.lean', 'theorem t : True := trivial\n/-! a later block proves `nothing` -/\n')
    want('(12) a file with no head `/-!` block has no header (line %s)' % line, line is None and r == [])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
