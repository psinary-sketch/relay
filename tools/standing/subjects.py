# -*- coding: utf-8 -*-
"""standing/subjects.py -- v1.14.0, (R344)(2)(v), b733 events (2), (5): THE COMMIT SUBJECT COMPOSED FROM THE BANK. b733's seal subject said 62 files, copied from b732's line, where its bank read 63, and its lock
commit's subject opened `b733 seal:` where the phase is `lock`. Here the head is the act and the step's phase, and every figure a subject prints is read from the bank that holds it; `check` refuses a typed subject
the composition would not print. The words after the colon stay the seat's where no bank holds them.

### v1.19.0, (R349)(2)(iii), b738 events (4): the seal subject "85 files" where the bank held 80, typed by hand; the lock's "eight gates" read
### the same way. A count before "files" (seal) or "gates" (lock), in figures or in words, is read against its bank, and tools/standing/hook.py
### refuses a seal or lock commit whose subject check() faults (kind SUBJECT), so the subject is the composition's or the commit does not run.
### v1.20.0, (R350)(2)(ii), b739 events (1): the count was read and the typing was not -- b739's "the sealed tools' hashes, 85 files" was
### refused for its 85, and the same words with 83 would have run. check() now refuses any seal or lock subject not opening with compose()'s text.

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


SCAN_FOOT = re.compile(r'PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES \d+ ; CONTROLS (\d+) OF (\d+)')


def gate_words(act, read, staged):
    """v1.23.0, (R353)(3)(ii), b742 events (1)-(2): the gate subject composed by the tool from the index and the banks, no word of the seat's:
    the staged paths (count and the first six by name), the root-dry bank's READY and row count, the scan bank's foot."""
    staged = list(staged or [])
    names = ', '.join(os.path.basename(p) for p in staged[:6]) + (', and %d more' % (len(staged) - 6) if len(staged) > 6 else '')
    parts = ['%d file%s staged (%s)' % (len(staged), '' if len(staged) == 1 else 's', names)]
    rd = read('%s_root_banks_dry.json' % act)
    if isinstance(rd, dict):
        parts.append('rootdry READY %s, %d banks at %s' % (bool(rd.get('ready')), len(rd.get('rows') or []), str(rd.get('head') or '')[:8]))
    sc = read('%s_address_scan.txt' % act)
    m = SCAN_FOOT.search(sc or '')
    if m:
        parts.append('scan %d, controls %s of %s' % (sum(int(m.group(i)) for i in range(1, 5)), m.group(5), m.group(6)))
    return '; '.join(parts)


def compose(act, phase, words, read, staged=None):
    if phase not in PHASES:
        raise SystemExit('### subjects: %r IS NO PHASE OF THE STEP BANK' % phase)
    if phase == 'gate' and staged is not None:
        return '%s %s: %s' % (act, phase, gate_words(act, read, staged))
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
    # ### v1.20.0, (R350)(2)(ii), b739 events (1): at the seal and the lock the composer is the one route -- the subject opens with compose()'s
    # ### own words for the phase, read from the bank, or it is a typed subject and refused (a typed one carrying the right count included)
    if phase in ('seal', 'lock'):
        head = compose(act, phase, '', read)
        if head.rstrip() == want:
            out.append('no bank composes the %s subject (data/%s_%s)' % (phase, act, 'seal_hashes.json' if phase == 'seal' else 'lockgate.json'))
        elif not subject.startswith(head):
            out.append('a typed %s subject: it does not open with the composer`s %r' % (phase, head[len(want) + 1:][:60]))
        elif subject != head:
            # ### v1.23.0, (R353)(3)(ii), b742 events (1)-(2): the seal subject "b742 seal: the sealed tools` hashes, 96 files, b742 seal: the sealed
            # ### tools` hashes, 96 files, the seal recorded, ..." opened with the composer's words and carried the seat's after them, the head twice;
            # ### the seal and the lock subject is now the composer's whole, nothing after it
            out.append('words after the composer`s %s subject: %r' % (phase, subject[len(head):][:60]))
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
