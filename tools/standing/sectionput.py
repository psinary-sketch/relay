# -*- coding: utf-8 -*-
"""standing/sectionput.py -- A RECORD BODY GOES THROUGH A BODY FILE (v1.27.0, (R357)(3)(ix), b746 defect (k)).

b746 wrote a record section's body inside a Bash `python -c "..."`: the shell ran the body's backticks as command substitution and
tools/acts/b746.py's record section 4 was written mangled. Here a section's body is read from a file, byte for byte, and put between the
section's marker line and its end line; no body passes through a shell string. The write refuses where the marker is absent or stands twice,
and prints the body's md5 before and after so the put is read back.

  put(text, tool, n, body) -> text           pure: the act module's text with section <tool> <n>'s body replaced
  python -X utf8 -u tools/standing/sectionput.py <act> <tool> <n> <body file> [--write]   without --write a dry print alone
"""
import hashlib
import io
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))
if S not in sys.path:
    sys.path.insert(0, S)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
END = '#⟪END⟫'


def put(text, tool, n, body):
    mk = re.compile(r'(?m)^#⟪SECTION %s %d⟫\n' % (re.escape(tool), int(n)))
    hits = list(mk.finditer(text))
    if len(hits) != 1:
        raise SystemExit('### REFUSED: section %s %s stands %d times in the module, not once' % (tool, n, len(hits)))
    a = hits[0].end()
    e = text.find(END, a)
    if e < 0:
        raise SystemExit('### REFUSED: section %s %s has no end line' % (tool, n))
    if body and not body.endswith('\n'):
        body += '\n'
    return text[:a] + body + text[e:]


def md5(t):
    return hashlib.md5(t.encode('utf-8')).hexdigest()[:12]


def main(argv):
    if len(argv) < 4:
        sys.exit(__doc__)
    act, tool, n, bf = argv[:4]
    mp = os.path.join(RELAY, 'tools', 'acts', '%s.py' % act)
    bp = bf if os.path.isabs(bf) else os.path.join(RELAY, bf)
    for p in (mp, bp):
        if not os.path.isfile(p):
            sys.exit('### REFUSED: %s resolves to no file' % p)
    text = io.open(mp, encoding='utf-8', newline='').read()
    body = io.open(bp, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    new = put(text, tool, n, body)
    print('section %s %s: the body file %s, %d lines, md5 %s' % (tool, n, bf, body.count('\n'), md5(body)))
    if '--write' in argv:
        with open(mp + '.tmp', 'wb') as fh:
            fh.write(new.encode('utf-8'))
        os.replace(mp + '.tmp', mp)
        back = io.open(mp, encoding='utf-8', newline='').read()
        got = put(back, tool, n, '') and back[back.find('#⟪SECTION %s %s⟫\n' % (tool, n)) + len('#⟪SECTION %s %s⟫\n' % (tool, n)):]
        got = got[:got.find(END)]
        print('written tools/acts/%s.py ; read back md5 %s ; %s' % (act, md5(got), 'EQUAL' if got == (body if body.endswith('\n') else body + '\n') else '### DIFFERS'))
    else:
        print('dry: nothing written (module md5 %s -> %s)' % (md5(text), md5(new)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
