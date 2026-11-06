# -*- coding: utf-8 -*-
"""standing/commit.py -- v1.21.0, (R351)(2)(i), b740 events (1), (2), (4): THE SUBJECT AND THE ROW THAT TRAVEL WITH THEIR COMMIT. One call makes a
gate, lock or seal commit: it composes the subject from the bank (tools/standing/subjects.py), makes the commit and writes its step row, in that
order, with no shell between the subject and the commit (git is run by argument list, so no shell's escape character touches the subject).
Everything that could refuse the row is read before the commit, so a commit and its row never part:
  - the record the subject names must exist: the seal's data/<act>_seal_hashes.json, the lock's data/<act>_lockgate.json;
  - a lock row already in the step bank refuses a second `lock` and a `gate` (the commit after the lock takes `seal`, standing.repeat.one_lock);
  - the composed subject must pass subjects.check(); something must be staged (the add is its own message, one git write per message).
The commit's subject is read back from git and compared with the composed one; the row is written by the record tool's step route.
After a seal commit the post-seal exclude list is printed (tools/standing/hook.py excludes), read before any read ((R351)(2)(iv)).
v1.22.0, (R352)(2)(v): a refusal prints its class, REPEAT of the earlier act's row that carries its head words, or NEW (repeat_of).
v1.23.0, (R353)(3)(ii), b742 events (1)-(2): no subject text is taken for lock, gate and seal; words given refuse the commit. The gate subject
is composed from the index and the banks (subjects.gate_words); the seal and lock subjects are the composer's whole (subjects.check).

v1.24.0, (R354)(2)(ii)-(iii), b743 events (4), (7)-(9): THE REPAIR PHASE. `repair`, between the lock and the seal, for the act module alone, under
three conditions printed in the row: an author's lift banked in the events with its time (a line naming THE LIFT and an HH:MM:SSZ); the hook
restored, the settings file's sha256 now equal to the value the events bank names before the lift; the diff against HEAD confined to
tools/acts/<act>.py and to the lines the events name (":<n>" in the events rows). The head "<act> repair:" (the author's at b743, events (9)),
the seat's words after it naming the edits; the row written as phase `repair`. N4 reads such a commit as a post-lock edit and scores REFUTED.

  python -X utf8 -u tools/standing/commit.py <relay|pp> <gate|lock|seal>
  python -X utf8 -u tools/standing/commit.py relay repair <the words naming the edits>
"""
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
REPOS = {'relay': RELAY, 'pp': 'D:/MY-DOwnloads/PLACE-papers'}
PHASES = ('gate', 'lock', 'seal', 'repair')
RECORD = {'seal': '%s_seal_hashes.json', 'lock': '%s_lockgate.json'}
SETTINGS = 'D:/.claude/settings.json'   # ### the seat's project settings carrying the hook (b743 events (4): its sha256 read before and after each lift)
if S not in sys.path:
    sys.path.insert(0, S)

import subjects as SJ   # noqa: E402


class Refused(Exception):
    pass


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def reader(data):
    def read(name):
        p = os.path.join(data, name)
        if not os.path.exists(p):
            return None
        with open(p, encoding='utf-8') as f:
            return json.load(f) if name.endswith('.json') else f.read()
    return read


def _hash_matches(banked, now):
    """a banked sha256 in full or in the events' short form "1E22BFFE...68FBB2" against the hash now (case ignored)."""
    b, n = banked.upper().replace('…', '...'), (now or '').upper()
    if '...' in b:
        a, z = b.split('...', 1)
        return bool(a) and bool(z) and n.startswith(a) and n.endswith(z)
    return bool(b) and n == b


def repair_check(act, words, rows, events, settings_now, names, old_lines):
    """v1.24.0, (R354)(2)(ii): the repair phase's three conditions, pure in its arguments -- the step rows, the events text, the settings file's
    sha256 now, the staged names and the HEAD-side line numbers the staged diff touches. Returns (subject, the condition lines) or raises Refused."""
    import re
    ev = (events or '').replace('\r', '')
    if not any(r.get('phase') == 'lock' for r in rows):
        raise Refused('NO LOCK ROW: the repair phase stands between the lock and the seal')
    if any(r.get('phase') == 'seal' for r in rows):
        raise Refused('A SEAL ROW STANDS: the repair phase stands before the seal')
    if not (words or '').strip():
        raise Refused('THE REPAIR NAMES NO EDIT: the words after "%s repair:" name the edits and the lift' % act)
    lines = ev.split('\n')
    lifts = [i for i, l in enumerate(lines) if re.search(r'\bTHE LIFT\b', l) and re.search(r'\b\d\d:\d\d:\d\dZ\b', l)]
    c1 = bool(lifts)
    pre = [m.group(1) for l in lines[:lifts[0]] for m in re.finditer(r'settings\.json sha256 ([0-9A-Fa-f]{6,}(?:(?:\.\.\.|…)[0-9A-Fa-f]{4,})?)', l)] if c1 else []
    c2 = bool(pre) and _hash_matches(pre[-1], settings_now)
    named = sorted(set(int(m.group(1)) for l in lines for m in re.finditer(r'(?<![\w/.]):(\d{2,5})\b', l)))
    mod = 'tools/acts/%s.py' % act
    c3 = list(names) == [mod] and bool(old_lines) and set(old_lines) <= set(named)
    conds = ['  (1) the author`s lift banked in the events with its time: %s' % (('%d LIFT row(s), the first: %s' % (len(lifts), lines[lifts[0]].strip()[:90])) if c1 else '### NONE'),
             '  (2) the hook restored, %s now %s against the value banked before the lift %s: %s' % (SETTINGS, (settings_now or 'UNREAD')[:16], (pre[-1] if pre else 'NONE'), 'EQUAL' if c2 else '### NOT EQUAL'),
             '  (3) the diff against HEAD: files %s ; lines %s ; the lines the events name %s: %s' % (list(names), sorted(old_lines), named[:12], 'CONFINED' if c3 else '### NOT CONFINED')]
    if not (c1 and c2 and c3):
        raise Refused('THE REPAIR`S CONDITIONS NOT MET: %s' % ' '.join(c.strip() for c in conds if '###' in c))
    return '%s repair: %s' % (act, words.strip()), conds


def staged_lines(repo):
    """(names, the HEAD-side line numbers the staged diff touches), from `git diff --cached -U0`."""
    import re
    names = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]
    old = []
    for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))? \+\d+(?:,\d+)? @@', _git(repo, 'diff', '--cached', '-U0').stdout, re.M):
        a, n = int(m.group(1)), int(m.group(2)) if m.group(2) is not None else 1
        old += list(range(a, a + n)) if n else [a]
    return names, old


def settings_sha():
    import hashlib
    try:
        return hashlib.sha256(open(SETTINGS, 'rb').read()).hexdigest().upper()
    except OSError:
        return None


def preflight(act, phase, words, repo, rows, read):
    """the subject, or Refused before anything is written: the phase, the record it names, the step bank's lock row, the subject's check, the index."""
    if phase not in PHASES:
        raise Refused('the phase %r is not one of %s' % (phase, ' | '.join(PHASES)))
    if phase == 'repair':   # ### v1.24.0, (R354)(2)(ii)
        if os.path.abspath(repo) != os.path.abspath(RELAY):
            raise Refused('the repair phase is the relay`s alone (the act module)')
        names, old = staged_lines(repo)
        subj, conds = repair_check(act, words, rows, read('%s_events.txt' % act) or '', settings_sha(), names, old)
        print('\n'.join(['  THE REPAIR PHASE`S CONDITIONS ((R354)(2)(ii)):'] + conds))
        return subj
    if phase in RECORD and not read(RECORD[phase] % act):
        raise Refused('THE RECORD THE SUBJECT NAMES DOES NOT EXIST: data/%s' % (RECORD[phase] % act))
    if phase in ('lock', 'gate') and any(r.get('phase') == 'lock' for r in rows):
        raise Refused('A LOCK ROW STANDS: the commit after the lock takes phase `seal`, and the seal record must exist first')
    # ### v1.23.0, (R353)(3)(ii), b742 events (1)-(2): the tool takes no subject text for lock, gate and seal; the subject is the composer's whole
    if (words or '').strip():
        raise Refused('SUBJECT TEXT GIVEN FOR %s: the commit tool composes the %s subject from the banks and takes no words (%r)' % (phase.upper(), phase, words.strip()[:60]))
    staged = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p] if phase == 'gate' else None
    subj = SJ.compose(act, phase, '', read, staged=staged)
    bad = SJ.check(act, phase, subj, read)
    if bad:
        raise Refused('the composed subject faults: %s' % '; '.join(bad))
    if _git(repo, 'diff', '--cached', '--quiet').returncode == 0:
        raise Refused('nothing staged in %s (the add is its own message)' % repo)
    return subj


def commit(repo, subj):
    """the commit by argument list; (full sha, the subject read back)."""
    r = _git(repo, 'commit', '-q', '-m', subj)
    if r.returncode != 0:
        raise Refused('git commit exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[:200]))
    full = _git(repo, 'rev-parse', 'HEAD').stdout.strip()
    back = _git(repo, 'log', '-1', '--format=%s', full).stdout.rstrip('\n')
    return full, back


def record_row(key, phase, full):
    """the row by the record tool's own step route (data/<act>_steps.json, its bank hashes kept by that tool)."""
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(S, 'fold.py'), 'record', 'step', key, phase, full],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout + r.stderr).strip()


def run(key, phase, words, act=None, data=None, row_writer=None, after_seal=None):
    """one call: preflight, commit, read back, row. Returns a dict of what was done; Refused where nothing was."""
    import act as A
    act = act or A.current()['act']
    data = data or os.path.join(RELAY, 'data')
    repo = REPOS[key] if key in REPOS else key
    read = reader(data)
    rows = (read('%s_steps.json' % act) or {}).get('rows') or []
    subj = preflight(act, phase, words, repo, rows, read)
    full, back = commit(repo, subj)
    rc, out = (row_writer or record_row)(key, phase, full)
    done = dict(act=act, repo=key, phase=phase, commit=full, subject=subj, read_back=back, equal=back == subj, row_exit=rc, row=out,
                rowed=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    if phase == 'seal':
        done['excludes'] = (after_seal or excludes)()
    return done


def repeat_of(msg, act, data=None):
    """v1.22.0, (R352)(2)(v), b741 event (1): a refusal printed with its class: the latest earlier act's events or defects row carrying the
    refusal's head words (the text before its first colon), "REPEAT of <act> event (<n>)" / "defect (<x>)", or NEW where none does."""
    import re
    data = data or os.path.join(RELAY, 'data')
    head = msg.split(':')[0].strip()
    n = int(act[1:])
    hits = []
    for f in os.listdir(data):
        m = re.match(r'^b(\d+)_(events|defects)\.txt$', f)
        if not m or int(m.group(1)) >= n:
            continue
        with open(os.path.join(data, f), encoding='utf-8', errors='replace') as fh:
            for l in fh.read().replace('\r', '').split('\n'):
                r = re.match(r"^    \(((?:[a-z]'?)|\d+)\) ", l)
                if r and head and head in l:
                    hits.append((int(m.group(1)), m.group(2)[:-1], r.group(1)))
    if not hits:
        return 'NEW'
    a, kind, x = max(hits)
    return 'REPEAT of b%d %s (%s)' % (a, kind, x)


def excludes():
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', os.path.join(S, 'hook.py'), 'excludes'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or r.stderr).strip()


def main(argv):
    if len(argv) < 2 or argv[0] not in REPOS:
        sys.exit(__doc__)
    try:
        d = run(argv[0], argv[1], ' '.join(argv[2:]))
    except Refused as e:
        import act as A
        sys.exit('### commit.py REFUSED, NOTHING COMMITTED, NO ROW WRITTEN: %s ### THE CLASS: %s' % (e, repeat_of(str(e), A.current()['act'])))
    print('  commit %s %s' % (d['repo'], d['commit'][:8]))
    print('  subject   : %s' % d['subject'])
    print('  read back : %s -- %s' % (d['read_back'], 'EQUAL' if d['equal'] else '### NOT EQUAL'))
    print('  row       : %s (exit %d)' % (d['row'], d['row_exit']))
    if 'excludes' in d:
        print(d['excludes'])
    if not d['equal'] or d['row_exit'] != 0:
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
