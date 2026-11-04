# -*- coding: utf-8 -*-
"""standing/subjects.py -- v1.14.0, (R344)(2)(v), b733 events (2), (5): THE COMMIT SUBJECT COMPOSED FROM THE BANK. b733's seal subject said 62 files, copied from b732's line, where its bank read 63, and its lock
commit's subject opened `b733 seal:` where the phase is `lock`. Here the head is the act and the step's phase, and every figure a subject prints is read from the bank that holds it; `check` refuses a typed subject
the composition would not print. The words after the colon stay the seat's where no bank holds them.

### v1.19.0, (R349)(2)(iii), b738 events (4): the seal subject "85 files" where the bank held 80, typed by hand; the lock's "eight gates" read
### the same way. A count before "files" (seal) or "gates" (lock), in figures or in words, is read against its bank, and tools/standing/hook.py
### refuses a seal or lock commit whose subject check() faults (kind SUBJECT), so the subject is the composition's or the commit does not run.

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


WORDS = dict(zip(('one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen '
                  'twenty').split(), range(1, 21)))
COUNT = r'\b(\d+|%s) %s\b'


def _n(tok):
    return int(tok) if tok.isdigit() else WORDS.get(tok.lower())


def lock_gates(act, read):
    """v1.19.0: the lock gate's own count of the gates it read (data/<act>_lockgate.json gates_read)."""
    j = read('%s_lockgate.json' % act) or {}
    return j.get('gates_read') if isinstance(j, dict) else None


def compose(act, phase, words, read):
    if phase not in PHASES:
        raise SystemExit('### subjects: %r IS NO PHASE OF THE STEP BANK' % phase)
    if phase == 'seal' and read('%s_seal_hashes.json' % act):
        words = 'the sealed tools` hashes, %d files%s' % (seal_files(act, read), (', ' + words) if words else '')
    if phase == 'lock' and lock_gates(act, read):
        words = 'face locked, the lock gate`s %d gates%s' % (lock_gates(act, read), (', ' + words) if words else '')
    return '%s %s: %s' % (act, phase, words)


def check(act, phase, subject, read):
    out = []
    want = '%s %s:' % (act, phase)
    if not subject.startswith(want):
        out.append('the subject opens %r, the phase`s head %r' % (subject.split(':')[0] + ':', want))
    alt = '|'.join(WORDS)
    sealed = phase == 'seal' and bool(read('%s_seal_hashes.json' % act))
    for noun, banked, mine in (('files', seal_files(act, read) if sealed else None, phase == 'seal'), ('gates', lock_gates(act, read), phase == 'lock')):
        if not mine:
            continue
        for m in re.finditer(COUNT % (alt, noun), subject, re.I):
            if banked is None:
                out.append('the subject says %s %s, no bank holds the count' % (m.group(1), noun))
            elif _n(m.group(1)) != banked:
                out.append('the subject says %s %s, the bank %d' % (m.group(1), noun, banked))
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
