# -*- coding: utf-8 -*-
"""standing/actmodule.py -- v1.12.0, (R342)(2)(i): THE ACT MODULE RENDERED FROM THE STANDING TEMPLATES AND THE ACT'S OWN SECTIONS, NOT REWRITTEN BY HAND.

b731's applier rewrote section checks 40 of tools/acts/b731.py whole; the section also held a standing arm's function, research_reproduces_ok, and the arm's row stayed and its function went
(b731 events (1)-(3)). Here the carried module is the base, and the act's own sections stand in a file of their own, tools/<act>_sections.txt, each block under its marker line as the module carries it.
The render puts each own block over the base's block of the same marker and refuses, writing nothing, where a block dropped a top-level function that anything left in the module still reads.
The rendered module then goes through reportdry.bank, step [5a], over the seven tools. Written at b732 by the Write tool.

  blocks(text) -> [(key, start, end)]            the module's blocks, key (kind, tool, first), end past the end line
  compose(base, own) -> text                     own's blocks over base's; a block base lacks appended
  dropped(base, text) -> {name: [readers]}       a function base's blocks define, the render's do not, and the lines that still read it
  render(act, base_ref, write=False)             base at the commit named; own from tools/<act>_sections.txt
  python -X utf8 tools/standing/actmodule.py render <act> <base-ref> [--write]
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fold as F   # noqa: E402

DEF = re.compile(r'(?m)^(?:def|class) (\w+)\b')


class RenderRefused(Exception):
    pass


def blocks(text):
    out, i = [], 0
    while True:
        m = F.SECTION.search(text, i)
        if not m:
            return out
        e = text.find(F.END, m.end())
        if e < 0:
            raise RenderRefused('actmodule: %s %s %s has no end line' % m.group(1, 2, 3))
        i = e + len(F.END)
        out.append(((m.group(1), m.group(2), int(m.group(3))), m.start(), i))


def compose(base, own):
    b = dict((k, (s, e)) for k, s, e in blocks(base))
    put, extra = {}, []
    for k, s, e in blocks(own):
        if k in b:
            put[b[k][0]] = (b[k][1], own[s:e])
        else:
            extra.append(own[s:e])
    out, i = [], 0
    for s in sorted(put):
        out.append(base[i:s])
        i, txt = put[s]
        out.append(txt)
    out.append(base[i:])
    tail = ''.join(extra)
    return ''.join(out) + (('' if out[-1].endswith('\n') else '\n') + tail if tail else '')


def _defs(text):
    return set(n for k, s, e in blocks(text) for n in DEF.findall(text[s:e]))


def dropped(base, text):
    """every function base's blocks define and text's do not, where anything left in text reads the name; the lines that read it."""
    gone = _defs(base) - _defs(text)
    out = {}
    for n in sorted(gone):
        rx = re.compile(r'(?<![\w.])%s\b' % re.escape(n))
        hits = [l.strip()[:120] for l in text.split('\n') if rx.search(l) and not l.lstrip().startswith('#')]
        if hits:
            out[n] = hits
    return out


def base_text(act, ref):
    r = subprocess.run(['git', '-C', F.ROOT, 'show', '%s:tools/acts/%s.py' % (ref, act)], capture_output=True)
    if r.returncode:
        raise RenderRefused('actmodule: no tools/acts/%s.py at %s' % (act, ref))
    return r.stdout.decode('utf-8')


def render(act, ref, write=False):
    base = base_text(act, ref)
    own = F._rd(os.path.join(F.TOOLS_DIR, '%s_sections.txt' % act))
    text = compose(base, own)
    d = dropped(base, text)
    if d:
        raise RenderRefused('actmodule: REFUSED, NOTHING WRITTEN: the render dropped %s' % '; '.join('%s, still read at: %s' % (n, h[0]) for n, h in d.items()))
    if write:
        p = os.path.join(F.TOOLS_DIR, 'acts', '%s.py' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write(text.encode('utf-8'))
        os.replace(p + '.tmp', p)
    return text, len(blocks(own)), len(blocks(text))


def main(argv):
    if len(argv) < 3 or argv[0] != 'render':
        sys.exit(__doc__)
    try:
        text, n, m = render(argv[1], argv[2], '--write' in argv)
    except RenderRefused as e:
        sys.exit(str(e))
    print('actmodule: %s rendered over %s: own blocks %d, the module`s blocks %d, %d lines, dropped NONE%s' % (argv[1], argv[2], n, m, text.count('\n'), ' ; WRITTEN tools/acts/%s.py' % argv[1] if '--write' in argv else ' ; dry, nothing written'))


if __name__ == '__main__':
    main(sys.argv[1:])
