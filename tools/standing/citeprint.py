# -*- coding: utf-8 -*-
"""standing/citeprint.py -- v1.28.0, (R358)(3)(xi), b747 defect (w): A PRINTED SOURCE LINE IS THE WHOLE LINE.

b747's section bank printed cite (11), data/b725_interference.txt :11, cut at its 170th character ("8: 4 2 4 1 ;" where the line runs on to
"12: 4 4 6 0"); the printer was the seat's scratch (a [:170] slice). The section banks of b748 print their cites through `lines()`, which prints
each line whole, and `check()` reads a printed cite back against its source and refuses a line that is not the whole line.

  lines(src_lines, a, b) -> ['      NNNNN  <the whole line>', ...]
  check(printed, src_lines, n) -> None | the fault
"""

FMT = '      %5d  %s'


def lines(src_lines, a, b=None):
    b = b or a
    if not (1 <= a <= b <= len(src_lines)):
        raise SystemExit('citeprint: lines :%d-:%d outside the source`s %d lines' % (a, b, len(src_lines)))
    return [FMT % (n, src_lines[n - 1].rstrip('\r\n')) for n in range(a, b + 1)]


def check(printed, src_lines, n):
    """None where the printed text is the whole source line n, else the fault (a cut, a difference, a line outside the source)."""
    if not (1 <= n <= len(src_lines)):
        return 'line :%d outside the source`s %d lines' % (n, len(src_lines))
    s = src_lines[n - 1].rstrip('\r\n').rstrip()
    p = (printed or '').rstrip()
    if p == s:
        return None
    if s.startswith(p):
        return 'CUT at character %d of %d' % (len(p), len(s))
    return 'DIFFERS from the source line'
