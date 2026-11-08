# -*- coding: utf-8 -*-
"""standing/orderstate.py -- AN ORDER'S STATE READ FROM THE RECORD, NOT FROM A CONSTANT (v1.27.0, (R357)(3)(i) and (iii)).

(i)  the word "entered" or "carried" is read from the order commit's presence in PLACE-papers' git log: a commit in BASE..HEAD whose diff
     of OPEN_TRAILS.md adds the order's entry-form line ("*Appended ... THE ORDER **`W-ORD-...`**"). No file tracked at a lock carries it.
(iii) the carried state's sentence is composed from the answers bank's reason and the events bank's row naming it, not assumed: an author's
     word opening "Carry the order" read in the answers bank, the events row quoting it, and an earlier word opening "Enter by name".

  orderstate.py state NAME BASE [HEAD]            the sha of the order's entry commit in BASE..HEAD, or NONE, and the word
  orderstate.py reason NAME BASE ACT [HEAD]       the sentence, from data/<ACT>_author_answers.txt and data/<ACT>_events.txt
It reads and prints; it writes nothing.
"""
import os
import re
import subprocess
import sys

NL = '\n'
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ENTRYFORM = re.compile(r'^\*Appended[^\n]*?THE ORDER \*\*`(W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*)`')
WORD = re.compile(r'(?m)^### THE AUTHOR`S WORD \(transcript line (\d+)\), BEGIN to END, verbatim:\n(.*)$')
EVROW = re.compile(r'(?m)^    \((\d+)\) (.*)$')


def entry_commit_in(rows, name):
    """pure: rows [(sha, [added lines])] in log order (newest first); the newest sha adding the order's entry-form line, or None."""
    for sha, added in rows:
        if any((ENTRYFORM.match(l) or [None, None])[1] == name for l in added):
            return sha
    return None


def log_rows(base, head='HEAD', repo=PP):
    """[(sha, [lines added to OPEN_TRAILS.md])] for each commit in base..head touching it, newest first (one git read)."""
    out = subprocess.run(['git', '-C', repo, 'log', '--format=@@C %H', '-p', '--unified=0', '--no-color', '%s..%s' % (base, head),
                          '--', 'OPEN_TRAILS.md'], capture_output=True)
    if out.returncode != 0:
        raise SystemExit('### REFUSED: git log %s..%s in %s failed: %s' % (base, head, repo, out.stderr.decode('utf-8', 'replace').strip()))
    rows = []
    for l in out.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL):
        if l.startswith('@@C '):
            rows.append((l[4:].strip(), []))
        elif rows and l.startswith('+') and not l.startswith('+++'):
            rows[-1][1].append(l[1:])
    return rows


def entry_commit(name, base, head='HEAD', repo=PP):
    return entry_commit_in(log_rows(base, head, repo), name)


def state(sha):
    return 'entered' if sha else 'carried'


def reason_from(name, sha, answers, events, answers_bank, events_bank):
    """pure: the sentence for the order's state. Entered: by its commit. Carried: on the events row quoting the author's carry word,
    with the author's earlier word to enter by name where one stands; carried with no carry word: says so."""
    if sha:
        return 'entered by name at PLACE-papers %s, its entry commit read from the git log' % sha[:8]
    words = [(int(m.group(1)), m.group(2).strip(), answers[:m.start()].count(NL) + 2) for m in WORD.finditer(answers)]
    carry = [w for w in words if w[1].startswith('Carry the order') and name in w[1]] or [w for w in words if w[1].startswith('Carry the order')]
    if not carry:
        return 'carried, no word of the author’s to carry it read in %s' % answers_bank
    c = carry[-1]
    ev = [int(m.group(1)) for m in EVROW.finditer(events) if c[1][:60] in m.group(2)]
    enter = [w for w in words if w[0] < c[0] and w[1].startswith('Enter by name')]
    s = 'carried on the defect of events (%s)' % ev[0] if ev else 'carried on the author’s word (%s :%d), no events row quoting it' % (answers_bank, c[2])
    if enter:
        s += ', the author’s word to enter by name'
    return s


def reason(name, base, act, head='HEAD'):
    ab, eb = 'data/%s_author_answers.txt' % act, 'data/%s_events.txt' % act
    rd = lambda p: open(os.path.join(RELAY, p), encoding='utf-8').read().replace('\r', '')
    for p in (ab, eb):
        if not os.path.isfile(os.path.join(RELAY, p)):
            raise SystemExit('### REFUSED: %s resolves to no file (%s)' % (p, os.path.join(RELAY, p)))
    sha = entry_commit(name, base, head)
    return sha, reason_from(name, sha, rd(ab), rd(eb), ab, eb)


def main(argv):
    if len(argv) >= 3 and argv[0] == 'state':
        sha = entry_commit(argv[1], argv[2], argv[3] if len(argv) > 3 else 'HEAD')
        print('%s %s..%s: entry commit %s ; the word: %s' % (argv[1], argv[2], argv[3] if len(argv) > 3 else 'HEAD', sha or 'NONE', state(sha)))
        return 0
    if len(argv) >= 4 and argv[0] == 'reason':
        sha, s = reason(argv[1], argv[2], argv[3], argv[4] if len(argv) > 4 else 'HEAD')
        print('%s: entry commit %s ; %s' % (argv[1], sha or 'NONE', s))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
