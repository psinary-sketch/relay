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

v1.26.0, (R356)(3)(i), (iii), b745 events (1), N4: the lock phase runs reg_seal.py --lock on the face its gate record names, adds the face and
reads the staged blob back (lock_face, lock_check): the lock block stands in the lock commit or nothing is committed. The act phases (ACT_PHASES:
step zero, component N, pre-root, record, closing) take the seat's words; the subject "<act> <phase>: <words>", the row in the same call.

v1.28.0, (R358)(3)(ii), (iii), (iv), (v), (vii), (viii), b747 defects (b), (d)-(f), (k), (n), (r), (v), (z), (a'):
  (iv) EVERY GIT WRITE THROUGH THE ONE-CALL TOOL: `add <paths>`, `restore <path>` and `delete <branch>` beside the commit phases; every write takes
       the act's write mark (an exclusive file under the relay's .git), and a call made while another write of the act holds it is refused, the
       open one printed (b747 (k): an add and a commit in one message).
  (ii) THE SCAN OVER THE STAGED SET BEFORE EVERY COMMIT: the act's tools/<act>_address_scan.py run before the commit, its four counts printed;
       a count above 0, a control not as wanted, or no foot refuses the commit.
  (v)  THE CARRY BEFORE THE ACT'S FIRST COMMIT: `step zero` refuses while the act's module, worklist or scan tool is not carried.
  (iii) NO STANDING CHANGE AT THE GATE: the gate refuses a staged tools/standing/ path (the repair lands with its version before the gate).
  (vii) THE SATISFIABILITY READ BEFORE THE GATE COMMIT: the gate refuses unless data/audit_<act>_reg_satisfiable.txt reads JOINTLY SATISFIABLE
       stamped against the face; a contradictory clause is printed by name.
  (viii) A STANDING REPAIR WITH THE RECORD'S DRY: a commit staging tools/standing/ files refuses unless data/<act>_standing_dry.txt is staged
       beside them, CLEAN or PENDING, naming each staged standing file at its staged sha256 (tools/standing/standingdry.py).

v1.28.1, (R358)(3)(iv), b748 defect (k): THE CLOSE'S WRITES THROUGH THE SAME TOOL: `root` among the act phases (the root banks commit);
  `branch <name>`, the act's push branch alone (push-<act>-preroot|record|closing) at HEAD, under the write mark; a relay act commit whose
  staged set is the step bank alone (with the scan's banks) is a step-rows commit: its words must be the rows' own composition
  (subjects.step_rows_words) and it writes no row of its own, so the step bank is clean before the push.

  python -X utf8 -u tools/standing/commit.py <relay|pp> <gate|lock|seal>
  python -X utf8 -u tools/standing/commit.py <relay|pp> branch push-<act>-<preroot|record|closing>
  python -X utf8 -u tools/standing/commit.py relay repair <the words naming the edits>
  python -X utf8 -u tools/standing/commit.py <relay|pp> "component 1" <the words>
  python -X utf8 -u tools/standing/commit.py <relay|pp> add <path> [<path> ...]
  python -X utf8 -u tools/standing/commit.py <relay|pp> restore <path>
  python -X utf8 -u tools/standing/commit.py <relay|pp> delete <branch>
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
if T not in sys.path:
    sys.path.append(T)   # ### v1.26.0: reg_seal.py for lock_check

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
    read.data = data   # ### v1.28.0: the gate's satisfiability read finds the audit and the face beside the banks
    return read


def data_dir(read):
    return getattr(read, 'data', os.path.join(RELAY, 'data'))


def face_stamped(act, data):
    """the satisfiability audit stamped against the act's registration face as it stands (gate_hash.matches), False where either is absent."""
    import glob
    import gate_hash as G
    faces = sorted(glob.glob(os.path.join(data, '%s_registration_*.txt' % act)))
    audit = os.path.join(data, 'audit_%s_reg_satisfiable.txt' % act)
    if not faces or not os.path.isfile(audit):
        return False
    return G.matches(audit, faces[-1])[0] is True


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


def lock_check(face_text, rec):
    """v1.26.0, (R356)(3)(i), b745 events (1), N4: THE LOCK BLOCK IN THE LOCK COMMIT. Pure in its arguments -- the face's text as it stands in
    the commit (the staged blob, or a commit's blob in the controls) and the lock gate's record. The face must carry reg_seal's lock block, and
    the digest of the bytes above it must equal the record's face_sha. Returns the condition lines or raises Refused."""
    import reg_seal as RS
    t = (face_text or '').replace('\r\n', '\n')
    body, banked = RS.split_body(t)
    has = RS.LOCKMARK in t and banked is not None
    dig = RS.digest(body)
    eq = has and dig == (rec or {}).get('face_sha') and banked == dig
    conds = ['  (1) the face %s carries the lock block in the commit: %s' % ((rec or {}).get('face'), 'YES' if has else '### NO'),
             '  (2) the digest of the bytes above it %s against the gate record`s face_sha %s: %s' % (dig[:16], str((rec or {}).get('face_sha'))[:16],
                                                                                                 'EQUAL' if eq else '### NOT EQUAL')]
    if not (has and eq):
        raise Refused('THE LOCK BLOCK IS NOT IN THE LOCK COMMIT: %s' % ' '.join(c.strip() for c in conds if '###' in c))
    return conds


def lock_face(repo, act, read, data, run_seal=True):
    """v1.26.0, (R356)(3)(i): inside the lock tool, between the gate and the lock commit -- reg_seal.py --lock on the face the gate record names,
    where the face carries no lock block yet, the face added to the index, and the staged blob read back through lock_check."""
    rec = read('%s_lockgate.json' % act) or {}
    face = rec.get('face')
    if not face:
        raise Refused('THE GATE RECORD NAMES NO FACE: data/%s_lockgate.json' % act)
    p = os.path.join(data, face)
    with open(p, encoding='utf-8') as f:
        has = (f.read().find('THE REGISTRATION LOCK') >= 0)
    if not has and run_seal:
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--lock', p], capture_output=True, text=True,
                           encoding='utf-8', errors='replace')
        print((r.stdout + r.stderr).rstrip())
        if r.returncode != 0:
            raise Refused('reg_seal.py --lock exit %d on data/%s: the face is not locked' % (r.returncode, face))
    rel = os.path.relpath(p, repo).replace(os.sep, '/')
    a = _git(repo, 'add', '--', rel)
    if a.returncode != 0:
        raise Refused('git add of data/%s exit %d' % (face, a.returncode))
    blob = _git(repo, 'show', ':' + rel).stdout
    conds = lock_check(blob, rec)
    print('\n'.join(['  THE LOCK BLOCK IN THE LOCK COMMIT ((R356)(3)(i)):'] + conds))
    return conds


ACT_PHASES = ('step zero', 'component 1', 'component 2', 'component 3', 'component 4', 'pre-root', 'root', 'record', 'closing')   # ### v1.28.1: root
WRITES = ('add', 'restore', 'delete', 'branch')   # ### v1.28.1: branch, the push-<act>-<stage> branch at HEAD
MARK = os.path.join(RELAY, '.git', 'standing_write_open.json')


# ================================================================================ v1.28.0 (iv): THE WRITE MARK
def _alive(pid):
    """the process `pid` still running (Windows: OpenProcess and its exit code; elsewhere signal 0)."""
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if os.name == 'nt':
        import ctypes
        k = ctypes.windll.kernel32
        h = k.OpenProcess(0x1000, False, pid)
        if not h:
            return False
        code = ctypes.c_ulong()
        ok = k.GetExitCodeProcess(h, ctypes.byref(code))
        k.CloseHandle(h)
        return bool(ok) and code.value == 259
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def mark_refusal(mark, alive):
    """None, or the refusal, for a write while the mark `mark` (its dict, or None) stands and its holder is `alive`. Pure."""
    if not mark:
        return None
    if alive:
        return 'ANOTHER WRITE OF THE ACT IS OPEN: %s (pid %s, since %s) -- one git write per message, every write through this tool' % (
            mark.get('what'), mark.get('pid'), mark.get('at'))
    return None


def open_mark(what, path=MARK):
    """take the act's write mark, exclusively; a mark whose holder has exited is removed and named; a live one refuses."""
    for _ in range(2):
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                with open(path, encoding='utf-8') as f:
                    m = json.load(f)
            except (OSError, ValueError):
                m = dict(what='unreadable mark', pid=None, at='?')
            bad = mark_refusal(m, _alive(m.get('pid')))
            if bad:
                raise Refused(bad)
            print('  a stale write mark removed: %s (pid %s, exited)' % (m.get('what'), m.get('pid')))
            os.remove(path)
            continue
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(dict(what=what, pid=os.getpid(), at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), f)
        return path
    raise Refused('THE WRITE MARK COULD NOT BE TAKEN: %s' % path)


def close_mark(path=MARK):
    try:
        os.remove(path)
    except OSError:
        pass


# ================================================================================ v1.28.0 (ii), (v), (iii), (vii): THE CHECKS BEFORE A COMMIT
def scan_counts(text):
    """(counts dict, controls ok) from the scan's foot, or (None, False) where it carries none. Pure."""
    import re
    m = re.search(r'PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS (\d+) OF (\d+) AS WANTED', text or '')
    if not m:
        return None, False
    c = dict(address=int(m.group(1)), name=int(m.group(2)), previous=int(m.group(3)), orcid=int(m.group(4)), places=int(m.group(5)))
    return c, m.group(6) == m.group(7)


def scan_refusal(text, rc):
    c, ctl = scan_counts(text)
    if rc != 0 or c is None:
        return 'THE SCAN DID NOT RUN TO ITS FOOT (exit %d)' % rc
    if not ctl:
        return 'THE SCAN`S CONTROLS NOT AS WANTED'
    if c['address'] or c['name'] or c['previous'] or c['orcid']:
        return 'THE SCAN FOUND AN OCCURRENCE: address %d, name %d, previous name %d, ORCID %d' % (c['address'], c['name'], c['previous'], c['orcid'])
    return None


def run_scan(act):
    p = os.path.join(T, '%s_address_scan.py' % act)
    if not os.path.isfile(p):
        raise Refused('THE ACT`S SCAN TOOL IS NOT CARRIED: tools/%s_address_scan.py' % act)
    r = subprocess.run([sys.executable, '-X', 'utf8', '-u', p, 'scan', '--bank'], capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=RELAY)
    out = (r.stdout or '') + (r.stderr or '')
    bad = scan_refusal(out, r.returncode)
    foot = [l for l in out.split('\n') if 'PREVIOUS ADDRESS:' in l and '**' in l]
    print('  THE SCAN OVER THE STAGED SET ((R358)(3)(ii)): %s' % (foot[-1].strip() if foot else '### NO FOOT'))
    if bad:
        raise Refused(bad)


def carry_check(act, exists):
    """None, or the refusal, for the act's first commit: its module, worklist and scan tool carried (exists: rel path -> bool). Pure."""
    need = ('tools/acts/%s.py' % act, 'tools/%s_worklist.py' % act, 'tools/%s_address_scan.py' % act)
    miss = [n for n in need if not exists(n)]
    return ('THE CARRY HAS NOT RUN: %s not carried -- the carry runs before the act`s first commit and its scan' % ', '.join(miss)) if miss else None


def gate_standing_refusal(staged):
    std = [n for n in (staged or []) if n.startswith('tools/standing/')]
    return ('A STANDING CHANGE AT THE GATE: %s staged -- a standing repair lands with its version before the gate' % ', '.join(std[:4])) if std else None


def satisfiable_refusal(audit, stamped):
    """None, or the refusal, from the satisfiability audit's text and whether it is stamped against the face as it stands. Pure."""
    if not audit:
        return 'THE SATISFIABILITY READ HAS NOT RUN: data/audit_<act>_reg_satisfiable.txt absent (record gatebanks before the gate commit)'
    v = [l for l in audit.split('\n') if 'VERDICT' in l]
    if not v or 'JOINTLY SATISFIABLE' not in v[-1]:
        bad = [l.strip() for l in audit.split('\n') if 'CONTRADICTORY' in l and 'VERDICT' not in l]
        return 'NOT SATISFIABLE: %s' % ('; '.join(b[:120] for b in bad[:3]) or (v[-1].strip() if v else 'no verdict'))
    if not stamped:
        return 'THE SATISFIABILITY READ IS NOT STAMPED AGAINST THE FACE AS IT STANDS: run record gatebanks again'
    return None


def act_check(act, phase, words):
    """v1.26.0, (R356)(3)(iii), b745 events: every act commit through the tool, its row in the same call. The subject is "<act> <phase>: <words>"
    with words given; the phase one of ACT_PHASES."""
    if phase not in ACT_PHASES:
        raise Refused('the act phase %r is not one of %s' % (phase, ' | '.join(ACT_PHASES)))
    w = (words or '').strip()
    if not w:
        raise Refused('THE ACT COMMIT NAMES NOTHING: the words after "%s %s:" name what the commit carries' % (act, phase))
    if w.startswith('%s ' % act):
        raise Refused('THE WORDS REPEAT THE HEAD: give the words after "%s %s:" only' % (act, phase))
    return '%s %s: %s' % (act, phase, w)


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


def preflight(act, phase, words, repo, rows, read, lock_runner=None):
    """the subject, or Refused before anything is written: the phase, the record it names, the step bank's lock row, the subject's check, the index."""
    if phase in ACT_PHASES:   # ### v1.26.0, (R356)(3)(iii)
        subj = act_check(act, phase, words)
        if phase == 'step zero':   # ### v1.28.0, (R358)(3)(v)
            bad = carry_check(act, lambda n: os.path.isfile(os.path.join(RELAY, n)))
            if bad:
                raise Refused(bad)
        if _git(repo, 'diff', '--cached', '--quiet').returncode == 0:
            raise Refused('nothing staged in %s (the add is its own message)' % repo)
        return subj
    if phase not in PHASES:
        raise Refused('the phase %r is not one of %s' % (phase, ' | '.join(PHASES + ACT_PHASES)))
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
    if phase == 'gate':   # ### v1.28.0, (R358)(3)(iii), (vii)
        bad = gate_standing_refusal(staged) or satisfiable_refusal(read('audit_%s_reg_satisfiable.txt' % act), face_stamped(act, data_dir(read)))
        if bad:
            raise Refused(bad)
    subj = SJ.compose(act, phase, '', read, staged=staged)
    bad = SJ.check(act, phase, subj, read)
    if bad:
        raise Refused('the composed subject faults: %s' % '; '.join(bad))
    if phase == 'lock' and lock_runner is not None:   # ### v1.26.0, (R356)(3)(i): the lock block written and staged inside the tool
        lock_runner()
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


def standing_dry_refusal(repo, act, names):
    """v1.28.0 (viii): None, or the refusal, for the staged `names` -- tools/standing/ staged with the record's dry over it (standingdry.check)."""
    import hashlib
    import standingdry as SD
    if not any(n.startswith('tools/standing/') for n in names):
        return None
    dry_rel = 'data/%s_standing_dry.txt' % act
    dry = _git(repo, 'show', ':' + dry_rel).stdout if dry_rel in names else ''
    sha = {}
    for n in names:
        if n.startswith('tools/standing/'):
            b = subprocess.run(['git', '-C', repo, 'show', ':' + n], capture_output=True).stdout
            sha[n] = hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()
    return SD.check(names, dry, sha)


STAGES = ('preroot', 'record', 'closing')


def branch_refusal(act, verb, name):
    """v1.28.1: None, or the refusal, for a branch create -- the act's push branch alone, push-<act>-<preroot|record|closing>. Pure."""
    if verb != 'branch':
        return None
    if name not in ['push-%s-%s' % (act, s) for s in STAGES]:
        return 'NOT THE ACT`S PUSH BRANCH: %r -- the branch write makes push-%s-<%s> alone' % (name, act, '|'.join(STAGES))
    return None


def rows_only(act, names):
    """v1.28.1: True where the staged set is the step bank alone (with the scan's banks): a step-rows commit, which carries rows and writes
    none of its own (b747's practice), so the step bank is clean before the push. Pure."""
    steps = 'data/%s_steps.json' % act
    beside = {steps, 'data/%s_address_scan.txt' % act, 'data/%s_address_scan_postlock.txt' % act}
    return steps in names and set(names) <= beside


def write_route(key, verb, args, act=None):
    """v1.28.0 (iv): an add, a restore or a branch delete, under the act's write mark; Refused where nothing was written."""
    import act as A
    act = act or A.current()['act']
    repo = REPOS[key] if key in REPOS else key
    if verb not in WRITES:
        raise Refused('the write %r is not one of %s' % (verb, ' | '.join(WRITES)))
    if not args:
        raise Refused('THE %s NAMES NOTHING' % verb.upper())
    if any(ch in a for a in args for ch in '*?['):
        raise Refused('A GLOB IN THE %s: name each path (%s)' % (verb.upper(), ' '.join(args)[:80]))
    if verb in ('restore', 'delete', 'branch') and len(args) != 1:
        raise Refused('ONE %s PER CALL' % verb.upper())
    bad = branch_refusal(act, verb, args[0])   # ### v1.28.1
    if bad:
        raise Refused(bad)
    cmd = {'add': ['add', '--'] + list(args), 'restore': ['checkout', '--', args[0]], 'delete': ['branch', '-d', args[0]],
           'branch': ['branch', '--', args[0]]}[verb]
    mark = open_mark('%s %s in %s: %s' % (act, verb, key, ' '.join(args)[:120]))
    try:
        r = _git(repo, *cmd)
    finally:
        close_mark(mark)
    if r.returncode != 0:
        raise Refused('git %s exit %d: %s' % (' '.join(cmd[:2]), r.returncode, (r.stderr or r.stdout).strip()[:200]))
    return (r.stdout + r.stderr).strip()


def run(key, phase, words, act=None, data=None, row_writer=None, after_seal=None, scanner=None):
    """one call: preflight, commit, read back, row. Returns a dict of what was done; Refused where nothing was."""
    import act as A
    act = act or A.current()['act']
    data = data or os.path.join(RELAY, 'data')
    repo = REPOS[key] if key in REPOS else key
    read = reader(data)
    rows = (read('%s_steps.json' % act) or {}).get('rows') or []
    lr = (lambda: lock_face(repo, act, read, data)) if (phase == 'lock' and key == 'relay') else None
    mark = open_mark('%s commit %s in %s' % (act, phase, key)) if row_writer is None else None   # ### v1.28.0 (iv): the act's write mark
    try:
        subj = preflight(act, phase, words, repo, rows, read, lock_runner=lr)
        names = [p for p in _git(repo, 'diff', '--cached', '--name-only').stdout.split('\n') if p]
        bad = standing_dry_refusal(repo, act, names)   # ### v1.28.0 (viii)
        if bad:
            raise Refused(bad)
        only = phase in ACT_PHASES and os.path.abspath(repo) == os.path.abspath(RELAY) and rows_only(act, names)   # ### v1.28.1
        if only:
            head = json.loads(_git(repo, 'show', 'HEAD:data/%s_steps.json' % act).stdout or '{}')
            staged = json.loads(_git(repo, 'show', ':data/%s_steps.json' % act).stdout or '{}')
            want = SJ.step_rows_words(SJ.step_rows_added(head, staged))
            if not want or words.strip() != want:
                raise Refused('A STEP-ROWS COMMIT NAMES ITS ROWS: the words must read %r, given %r' % (want or '(no row staged)', words.strip()))
        if scanner is not False:
            (scanner or run_scan)(act)   # ### v1.28.0 (ii): the scan over the staged set before the commit
        full, back = commit(repo, subj)
    finally:
        if mark:
            close_mark(mark)
    if only:
        rc, out = 0, 'NONE WRITTEN: a step-rows commit carries the rows and writes none of its own (v1.28.1)'
    else:
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
    if argv[1] in WRITES:   # ### v1.28.0 (iv)
        try:
            out = write_route(argv[0], argv[1], argv[2:])
        except Refused as e:
            import act as A
            sys.exit('### commit.py REFUSED, NOTHING WRITTEN: %s ### THE CLASS: %s' % (e, repeat_of(str(e), A.current()['act'])))
        print('  %s %s: %s%s' % (argv[1], argv[0], ' '.join(argv[2:]), ('\n  ' + out) if out else ''))
        return
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
