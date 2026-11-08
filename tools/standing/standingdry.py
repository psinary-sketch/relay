# -*- coding: utf-8 -*-
"""standing/standingdry.py -- v1.28.0, (R358)(3)(viii), b747 defects (r), (v): A STANDING REPAIR LANDS WITH THE RECORD'S DRY COMPOSITION RUN OVER IT.

v1.27.0's repair (7) (relaypath.rdn refusing a path to no file) landed without the record's dry composition run over it, and the dry, first
run at Component 4, halted on banks the root and the close write (the events bank, the answers bank, the answer check, the pre-lock bank), which
the record read strictly. `run(act)` runs the record's dry compositions (`fold.py record findings dry`, `fold.py record scores dry` read for its
first halt without writing: the scores route's dry is not run, it writes its bank) over the tools as they stand, and banks the reading in
data/<act>_standing_dry.txt with the sha256 of every tools/standing/ file that differs from HEAD: a halt on a bank a component of the act writes
before the record (its corrigendum, its section banks) is PENDING, named; a halt on a bank the root or the close writes (CLOSE_LATE), or a
Traceback, is NOT CLEAN. tools/standing/commit.py refuses a commit staging tools/standing/ files unless this bank is staged beside them, reads
CLEAN or PENDING, and names each staged standing file at its staged blob's sha256.

  python -X utf8 -u tools/standing/standingdry.py run          data/<act>_standing_dry.txt
"""
import hashlib
import os
import re
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
CLOSE_LATE = ('events', 'author_answers', 'answer_check', 'prelock', 'scores', 'scores_close', 'act_root', 'root_arm', 'root_banks', 'closing',
              'desk_notes', 'checks', 'checks_postpush', 'mirror', 'mirror_verify', 'report', 'trail', 'findings', 'components', 'table_final')
HALT = re.compile(r'### REFUSED: (\S+) resolves to no file')
FOOT = re.compile(r'^### ### \*\*THE STANDING DRY: (CLEAN|PENDING|NOT CLEAN)\b', re.M)
FILEROW = re.compile(r'^  (tools/standing/\S+) sha256 ([0-9a-f]{64})$', re.M)


def classify(act, out, rc):
    """('CLEAN' | 'PENDING' | 'NOT CLEAN', [lines]) for one dry composition's output and exit, pure in its arguments."""
    if rc == 0:
        return 'CLEAN', ['exit 0']
    if 'Traceback' in out:
        last = [l for l in out.split(NL) if l.strip()][-1:]
        return 'NOT CLEAN', ['a Traceback: %s' % (last[0][:200] if last else '?')]
    m = HALT.search(out)
    if not m:
        return 'NOT CLEAN', ['exit %d with no named halt: %s' % (rc, out.strip()[-200:])]
    name = m.group(1)
    stem = name[len(act) + 1:] if name.startswith(act + '_') else name
    stem = re.sub(r'\.(txt|json)$', '', stem)
    if stem in CLOSE_LATE:
        return 'NOT CLEAN', ['a strict read of %s, a bank the root or the close writes: the record must read it optional' % name]
    return 'PENDING', ['a halt on %s, a bank a component of the act writes before the record: PENDING' % name]


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def changed_standing():
    names = sorted(set(p for p in (_git('diff', '--name-only', 'HEAD', '--', 'tools/standing/').stdout.split(NL)
                                   + _git('ls-files', '--others', '--exclude-standard', '--', 'tools/standing/').stdout.split(NL)) if p.strip()))
    return [(n, hashlib.sha256(open(os.path.join(RELAY, n), 'rb').read().replace(b'\r\n', b'\n')).hexdigest()) for n in names if os.path.isfile(os.path.join(RELAY, n))]


def run(act=None):
    sys.path.insert(0, S)
    import act as A
    act = act or A.current()['act']
    L = ['%s -- (R358)(3)(viii): THE RECORD`S DRY COMPOSITION RUN OVER THE STANDING REPAIR (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the record tool rendered from the templates as they stand and its dry compositions run: `record findings dry`. A halt on a bank a component',
         '### writes before the record is PENDING; a strict read of a bank the root or the close writes, or a Traceback, is NOT CLEAN.', '',
         '## THE STANDING FILES THE DRY RAN OVER (differing from HEAD or new), sha256 of the LF bytes']
    files = changed_standing()
    L += ['  %s sha256 %s' % (n, h) for n, h in files] or ['  NONE']
    verdicts = []
    for args in (['record', 'findings', 'dry'],):
        r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.join(S, 'fold.py')] + args, capture_output=True, text=True, encoding='utf-8',
                           errors='replace', cwd=RELAY, timeout=590)
        v, why = classify(act, (r.stdout or '') + (r.stderr or ''), r.returncode)
        verdicts.append(v)
        L += ['', '## `fold.py %s`: exit %d -> %s' % (' '.join(args), r.returncode, v)] + ['  ' + w for w in why]
    final = 'NOT CLEAN' if 'NOT CLEAN' in verdicts else ('PENDING' if 'PENDING' in verdicts else 'CLEAN')
    L += ['', '### ### **THE STANDING DRY: %s ; FILES %d ; COMPOSITIONS %d.**' % (final, len(files), len(verdicts))]
    b = (NL.join(L) + NL).encode('utf-8')
    p = os.path.join(D, '%s_standing_dry.txt' % act)
    with open(p + '.tmp', 'wb') as f:
        f.write(b)
    os.replace(p + '.tmp', p)
    print(NL.join(L))
    print('written data/%s_standing_dry.txt' % act)
    return final


def check(names, dry_text, staged_sha):
    """None, or the fault, for a commit staging `names`: where a tools/standing/ file is staged, the dry bank staged beside it, its foot CLEAN or
    PENDING, and each staged standing file named at its staged sha256 (staged_sha: name -> sha256 of the staged blob's LF bytes). Pure."""
    std = [n for n in names if n.startswith('tools/standing/')]
    if not std:
        return None
    if not dry_text:
        return 'tools/standing/ staged (%s) without the record`s dry over it: data/<act>_standing_dry.txt not staged' % ', '.join(std[:4])
    m = FOOT.search(dry_text)
    if not m:
        return 'the standing dry bank carries no foot'
    if m.group(1) == 'NOT CLEAN':
        return 'the standing dry reads NOT CLEAN'
    rows = dict(FILEROW.findall(dry_text))
    off = [n for n in std if rows.get(n) != staged_sha.get(n)]
    if off:
        return 'staged standing files not at the sha256 the dry ran over: %s' % ', '.join(off[:4])
    return None


if __name__ == '__main__':
    if sys.argv[1:2] != ['run']:
        sys.exit(__doc__)
    sys.exit(0 if run() != 'NOT CLEAN' else 1)
