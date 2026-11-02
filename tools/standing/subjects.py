# -*- coding: utf-8 -*-
"""standing/subjects.py -- v1.14.0, (R344)(2)(v), b733 events (2), (5): THE COMMIT SUBJECT COMPOSED FROM THE BANK. b733's seal subject said 62 files, copied from b732's line, where its bank read 63, and its lock
commit's subject opened `b733 seal:` where the phase is `lock`. Here the head is the act and the step's phase, and every figure a subject prints is read from the bank that holds it; `check` refuses a typed subject
the composition would not print. The words after the colon stay the seat's where no bank holds them.

  python -X utf8 -u tools/standing/subjects.py <phase> [words]      prints the subject; nothing written
  compose(act, phase, words, read)   -> the subject; read(name) -> the bank's json or text
  check(act, phase, subject, read)   -> [what differs]
"""
import json
import os
import re
import sys

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(os.path.dirname(T), 'data')
PHASES = ('step zero', 'standing', 'component 1', 'component 2', 'component 3', 'component 4', 'component 5', 'gate', 'lock', 'seal', 'pre-root', 'root', 'record', 'closing')


def seal_files(act, read):
    """the seal record's own count of the files it hashes."""
    j = read('%s_seal_hashes.json' % act) or {}
    return len(j.get('hashes') or j.get('tools') or {})


def compose(act, phase, words, read):
    if phase not in PHASES:
        raise SystemExit('### subjects: %r IS NO PHASE OF THE STEP BANK' % phase)
    if phase == 'seal' and read('%s_seal_hashes.json' % act):
        words = 'the sealed tools` hashes, %d files%s' % (seal_files(act, read), (', ' + words) if words else '')
    return '%s %s: %s' % (act, phase, words)


def check(act, phase, subject, read):
    out = []
    want = '%s %s:' % (act, phase)
    if not subject.startswith(want):
        out.append('the subject opens %r, the phase`s head %r' % (subject.split(':')[0] + ':', want))
    m = re.search(r'\b(\d+) files\b', subject)
    if m and phase == 'seal' and int(m.group(1)) != seal_files(act, read):
        out.append('the subject says %s files, the seal bank %d' % (m.group(1), seal_files(act, read)))
    return out


def _read(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding='utf-8') as f:
        return json.load(f) if name.endswith('.json') else f.read()


if __name__ == '__main__':
    sys.path.insert(0, os.path.join(T, 'standing'))
    import act as A
    print(compose(A.current()['act'], sys.argv[1], ' '.join(sys.argv[2:]), _read))
