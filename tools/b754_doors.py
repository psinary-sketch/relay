# -*- coding: utf-8 -*-
"""b754_doors.py -- (R364)(4)(vi): EACH DOOR'S CURRENT for [B] and [A5], read at its main or by gh, data/b754_doors.txt.

THE REMOTE READS, one per command and each its own message's call ((R364)(8): one remote read per command, a retry an event), each written
to the state folder (D:/relay-state/b754/doors/<door>_<kind>.json) with its time:
  python -X utf8 -u tools/b754_doors.py remote <door> description    `gh repo view --json description -q .description`, run in the door's
                                                                     own clone, the repository read from the clone's remote and named by no
                                                                     argument
  python -X utf8 -u tools/b754_doors.py remote <door> main           `git ls-remote origin refs/heads/main` in the door's clone
THE BANK, from the captures (each read today, the run's own date) and from each clone's main by `git show` (no remote read):
  [A5] PLACE-papers' description; [B1] SIDE-explicit-formula's README at main, the lines the draft replaces (:3, :5-:7, :23-:26), and [B2]
  its description; [B3] SIDE-kernel's README :3 with the phrase the draft replaces sought there, and [B4] its description; [B5] HELD by
  the amendment row 3 (4), nothing read for a write; [B6] SIDE-bsd-multiplicity's description and its README's head; [B7] SIDE-trivium's
  description and its README :3-:7. Each README's local main against the remote main the capture read.
WHAT IT QUOTES: the kernels' README lines and the descriptions, as the items' CURRENT ((R364)(5)'s opening sentence). A line or a
description carrying the account the clone's remote names (read at run time, never printed), the leading word of REGISTRY :373's heading
([Q] row (3), read at run time, never printed) or an identifier by tools/standing/outbound.py's forms is cited by its line and digest and
the kind that withheld it, and is not quoted.

  python -X utf8 -u tools/b754_doors.py control      the controls alone
  python -X utf8 -u tools/b754_doors.py dry          the controls and the bank, printed, nothing written
  python -X utf8 -u tools/b754_doors.py run          the controls, then the bank written (the generator committed before its run)
"""
import datetime
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import statedir
import outbound

ACT = 'b754'
SELF = 'tools/%s_doors.py' % ACT
BANK = os.path.join(RELAY, 'data', '%s_doors.txt' % ACT)
CAP = statedir.act_dir(ACT, 'doors')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
CLONES = {'PLACE-papers': PP, 'SIDE-explicit-formula': 'D:/SIDE-explicit-formula', 'SIDE-kernel': 'D:/SIDE-kernel',
          'SIDE-bsd-multiplicity': 'D:/SIDE-bsd-multiplicity', 'SIDE-trivium': 'D:/SIDE-trivium'}
WANT = [('PLACE-papers', 'description'), ('SIDE-explicit-formula', 'description'), ('SIDE-explicit-formula', 'main'),
        ('SIDE-kernel', 'description'), ('SIDE-kernel', 'main'), ('SIDE-bsd-multiplicity', 'description'), ('SIDE-bsd-multiplicity', 'main'),
        ('SIDE-trivium', 'description'), ('SIDE-trivium', 'main')]
# ### the README lines each draft names (data/b754_ferry.txt, (R364)(5)[B1], [B3], [B6], [B7])
README_LINES = {'SIDE-explicit-formula': ('[B1]', [3, 5, 6, 7, 23, 24, 25, 26]), 'SIDE-kernel': ('[B3]', [3]),
                'SIDE-bsd-multiplicity': ('[B6], its draft cut from the README`s own head', list(range(1, 11))),
                'SIDE-trivium': ('[B7], its draft cut from README :3-:7', [3, 4, 5, 6, 7])}
ITEMS = [('[A5]', 'PLACE-papers'), ('[B1] [B2]', 'SIDE-explicit-formula'), ('[B3] [B4]', 'SIDE-kernel'), ('[B5]', None),
         ('[B6]', 'SIDE-bsd-multiplicity'), ('[B7]', 'SIDE-trivium')]


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def run(argv, cwd=None):
    r = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=cwd)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def git(repo, *a):
    rc, out, err = run(['git', '-C', repo] + list(a))
    if rc:
        raise SystemExit('### NOT READ: git -C %s %s: %s' % (repo, ' '.join(a), err[:200]))
    return out


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def cap_path(door, kind):
    return os.path.join(CAP, '%s_%s.json' % (door, kind))


def remote(door, kind):
    if door not in CLONES or (door, kind) not in WANT:
        raise SystemExit('### NOT A READ OF THIS BANK: %s %s (the reads: %s)' % (door, kind, ', '.join('%s %s' % w for w in WANT)))
    clone = CLONES[door]
    t0 = stamp()
    if kind == 'description':
        rc, out, err = run(['gh', 'repo', 'view', '--json', 'description', '-q', '.description'], cwd=clone)
    else:
        rc, out, err = run(['git', '-C', clone, 'ls-remote', 'origin', 'refs/heads/main'])
        out = (out.split() or [''])[0]
    os.makedirs(CAP, exist_ok=True)
    rec = dict(door=door, kind=kind, at=t0, rc=rc, out=out, err=err[:300])
    tmp = cap_path(door, kind) + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, indent=1) + NL)
    os.replace(tmp, cap_path(door, kind))
    print('%s READ %s %s: rc %d, %d characters%s' % (t0, door, kind, rc, len(out), (' ; ' + err[:160]) if rc else ''))
    return rc


def account(clone):
    """the owner the clone's remote names, read at run time; never printed."""
    u = git(clone, 'remote', 'get-url', 'origin')
    m = re.search(r'[:/]([^/:]+)/[^/]+?(?:\.git)?/?$', u)
    return m.group(1) if m else None


def q_word():
    R = git(PP, 'show', 'HEAD:REGISTRY.md').replace('\r', '').split(NL)
    m = re.match(r'^(#+)\s*\**\s*([A-Za-z][A-Za-z\-]*)', R[372]) if len(R) > 372 else None
    return m.group(2) if m else None


def withheld(text, acct, word):
    """the kinds that withhold a text from quotation; [] where it may be quoted."""
    k = []
    if acct and acct.lower() in (text or '').lower():
        k.append('the account')
    if word and re.search(r'\b%s\b' % re.escape(word), text or '', re.I):
        k.append('[Q] row (3)')
    k += ['an identifier (%s)' % x for x in outbound.identifiers_in(text or '')]
    return k


def show(text, acct, word):
    w = withheld(text, acct, word)
    return ('WITHHELD by %s, digest %s, %d characters' % (', '.join(w), digest(text), len(text))) if w else '"%s"' % text


def load_caps():
    caps = {}
    for d, k in WANT:
        p = cap_path(d, k)
        if os.path.exists(p):
            caps[(d, k)] = json.load(io.open(p, encoding='utf-8'))
    return caps


def today_ok(rec, today):
    return bool(rec) and rec.get('rc') == 0 and str(rec.get('at', ''))[:10] == today


def ferry_phrase():
    f = git(RELAY, 'show', 'HEAD:data/%s_ferry.txt' % ACT)
    m = re.search(r'\[B3\] SIDE-kernel, README\.md :3, one phrase: "([^"]+)" replaced by', f)
    return m.group(1) if m else None


def controls(caps, today, acct, word):
    out, ok, n = [], 0, 0

    def case(label, good):
        nonlocal ok, n
        n += 1
        ok += bool(good)
        out.append('  %s : %s' % (label, 'AS WANTED' if good else '### NOT AS WANTED'))

    got = [(d, k) for d, k in WANT if today_ok(caps.get((d, k)), today)]
    case('(1) the remote reads captured, each read today (%s) with exit 0: %d of %d [%s]' % (
        today, len(got), len(WANT), '; '.join('%s %s %s' % (d, k, caps[(d, k)]['at'] if (d, k) in caps else 'ABSENT') for d, k in WANT)), len(got) == len(WANT))
    y = (datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    case('(2) a planted capture read %sT12:00:00Z read as not today: %s' % (y, not today_ok(dict(rc=0, at=y + 'T12:00:00Z', out='x'), today)),
         not today_ok(dict(rc=0, at=y + 'T12:00:00Z', out='x'), today))
    case('(3) the account read from each clone`s remote at run time (not printed): %s ; one account for the five clones %s' % (
        'READ' if acct else '### NOT READ', len(set(account(c) for c in CLONES.values())) == 1), bool(acct) and len(set(account(c) for c in CLONES.values())) == 1)
    pa = withheld('a planted line naming %s/SIDE-kernel' % (acct or 'x'), acct, word)
    pb = withheld('a planted plain line with no name in it', acct, word)
    pc = withheld('a planted line carrying 0000-0002-1825-0097', acct, word)
    case('(4) the withholding reader: a planted line carrying the account withheld by %s ; a plain line withheld by %s ; a line carrying an ORCID`s form withheld by %s' % (
        pa, pb or 'nothing', pc), pa == ['the account'] and pb == [] and pc == ['an identifier (ORCID)'])
    case('(5) [Q] row (3)`s word read from REGISTRY :373 at run time: %s, its length %d, not printed' % ('READ' if word else '### NOT READ', len(word or '')), bool(word))
    ph = ferry_phrase()
    case('(6) the phrase [B3] replaces, read from data/%s_ferry.txt at run time: %s' % (ACT, ('%d characters' % len(ph)) if ph else '### NOT FOUND'), bool(ph))
    a, b = 'a' * 40, 'b' * 40
    s = (main_state(b, a), main_state(a, a), main_state('', a))
    case('(7) the main comparison: a planted remote main differing from the local main reads %s ; the same main %s ; no remote read %s' % s,
         s == ('### DIFFERS', 'EQUAL', '### NOT READ'))
    return out, ok, n, ph


def main_state(rsha, full):
    return 'EQUAL' if rsha and rsha == full else '### DIFFERS' if rsha else '### NOT READ'


def compose(gen):
    today = time.strftime('%Y-%m-%d', time.gmtime())
    caps = load_caps()
    acct = account(PP)
    word = q_word()
    out, ok, n, phrase = controls(caps, today, acct, word)
    L = ['%s -- (R364)(4)(vi): EACH DOOR`S CURRENT FOR [B] AND [A5], read at its main or by gh on %s' % (ACT, today), '',
         '### Written by %s at relay %s (the generator committed before its run) at %s; the descriptions and the remote mains from the captures of' % (SELF, gen, stamp()),
         '### this act`s remote reads, one a command, each read in the door`s own clone; the READMEs by `git show main:README.md` in each clone. A bank',
         '### of this act and no ledger; nothing written to any door. A line naming the account, carrying [Q] row (3)`s word or an identifier is cited',
         '### by digest and not quoted.', '', '## THE CONTROLS, printed before any figure'] + out
    L += ['', '## THE DOORS, by item']
    for item, door in ITEMS:
        if door is None:
            L.append('  %s SIDE-lv-conservation: HELD by the amendment row 3 (4) (data/%s_amendments.json row 3); nothing read for a write and nothing written' % (item, ACT))
            continue
        clone = CLONES[door]
        dsc = caps.get((door, 'description'))
        L.append('  %s %s' % (item, door))
        if dsc:
            L.append('      DESCRIPTION by gh at %s: %s' % (dsc['at'], show(dsc['out'], acct, word) if dsc['rc'] == 0 else '### NOT READ (rc %d)' % dsc['rc']))
        if door in README_LINES:
            why, lines = README_LINES[door]
            local = git(clone, 'rev-parse', '--short=8', 'main')
            full = git(clone, 'rev-parse', 'main')
            rm = caps.get((door, 'main'))
            rsha = (rm or {}).get('out', '')
            L.append('      README.md at main %s ; the remote main %s (ls-remote at %s) : %s' % (
                local, rsha[:8] or 'NOT READ', (rm or {}).get('at', '-'), main_state(rsha, full)))
            R = git(clone, 'show', 'main:README.md').replace('\r', '').split(NL)
            L.append('      the file %d lines ; the lines %s names: %s' % (len(R), why, ', '.join(':%d' % k for k in lines)))
            for k in lines:
                s = R[k - 1] if k <= len(R) else None
                L.append('      :%d %s' % (k, '### NO SUCH LINE' if s is None else show(s, acct, word)))
            if door == 'SIDE-kernel':
                c = R[2].count(phrase) if phrase and len(R) >= 3 else 0
                L.append('      the phrase [B3] replaces, read from the ferry bank: at :3 %d time(s) ; in the file %d time(s)' % (c, sum(l.count(phrase) for l in R) if phrase else 0))
    text = NL.join(L) + NL
    wc = len(re.findall(r'\b%s\b' % re.escape(word), text, re.I)) if word else -1
    ac = text.lower().count(acct.lower()) if acct else -1
    ids = outbound.identifiers_in(text)
    good = wc == 0 and ac == 0 and not ids
    L.insert(L.index('## THE DOORS, by item') - 1, '  (8) over this bank`s text: [Q] row (3)`s word %d, the account %d, identifiers by form %s (wanted 0, 0, none) : %s' % (
        wc, ac, ids or 'none', 'AS WANTED' if good else '### NOT AS WANTED'))
    ok += good
    n += 1
    L += ['', '### ### **THE DOORS READ: [A5] AND [B1] TO [B7], [B5] HELD ; REMOTE READS %d OF %d TODAY ; CONTROLS %d OF %d.**' % (
        sum(1 for w in WANT if today_ok(caps.get(w), today)), len(WANT), ok, n)]
    return ok == n, ok, n, L


def committed():
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)
    return g('ls-files', '--error-unmatch', SELF).returncode == 0 and not g('status', '--porcelain', '--', SELF).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'remote' and len(argv) == 3:
        return remote(argv[1], argv[2])
    if mode not in ('control', 'dry', 'run'):
        raise SystemExit(__doc__)
    done, gen = committed()
    if mode == 'run' and not done:
        raise SystemExit('### REFUSED: %s is not committed or differs from its commit; the generator commits before its run ((R364)(4))' % SELF)
    import hold
    if mode != 'control' and hold.refuses('the doors` current read ((R364)(4)(vi))'):
        return 3
    allok, ok, n, L = compose(gen)
    c0 = L.index('## THE CONTROLS, printed before any figure')
    c1 = L.index('## THE DOORS, by item')
    print(NL.join(L[c0:c1]))
    print('### ### **CONTROLS %d OF %d %s**' % (ok, n, 'AS WANTED' if allok else 'NOT ALL AS WANTED'))
    if mode == 'control':
        return 0 if allok else 1
    if not allok:
        raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NO FIGURE PRINTED, NOTHING BANKED')
    if mode == 'dry':
        print(NL.join(L[c1:]))
        return 0
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(tmp, BANK)
    print('WRITTEN data/%s_doors.txt, %d lines' % (ACT, len(L)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
