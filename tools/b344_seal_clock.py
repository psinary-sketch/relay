# -*- coding: utf-8 -*-
"""b344_seal_clock.py -- COMPONENT 2: THE SEAL'S OWN CLOCK. ### the census before and after, and the fixtures.

### ### **THE REGISTRATION IS SEALED (section (D)); THIS TOOL MEASURES ITS BARS.** ### The repair itself is an edit to
### `tools/reg_seal.py` BY THE ORDER'S WORDS -- *"have reg_seal.py record the seal's UTC instant inside the seal block
### it writes"* -- made with the editor and not by this tool; what this tool does is ### **CENSUS EVERY EXISTING SEAL
### BEFORE AND AFTER** ### and run the fixtures.
###   `--before`   every sealed file in `data/` verified and its verdict recorded, before the edit.
###   `--after`    the same files verified again; every verdict must match the record, and none may have been rewritten;
###                then the fixtures: a fresh seal carries the clock and verifies; a seal whose clock line is altered
###                STILL verifies, which is the honest limit of the repair and is printed as such.
### ### **NO EXISTING SEAL IS REWRITTEN BY THIS TOOL OR BY THE REPAIR.** ### **THE REPAIR DOES NOT RECOVER b342's LOST
### ### TIMESTAMP**, and makes no act sealed before it checkable by time.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SEALER = os.path.join(ROOT, 'tools', 'reg_seal.py')
BEFORE = os.path.join(D, 'b344_seal_census_before.json')
AFTER = os.path.join(D, 'b344_seal_census_after.json')
MARK = '### THE REGISTRATION SEAL (emitted by tools/reg_seal.py; do not retype).'
CLOCK = '### sealed at (UTC) : '
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def sealed_files():
    out = []
    for n in sorted(os.listdir(D)):
        if not n.endswith('.txt'):
            continue
        p = os.path.join(D, n)
        try:
            t = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        # ### THE MARKER MUST SIT WHERE A SEAL BLOCK PUTS IT -- on its own line under the bar -- and not merely
        # ### appear somewhere in the text. ### The first run of this census took the extract file for a sealed
        # ### registration because that file QUOTES the marker as one of its anchors; declared as this act's (E1).
        if ('=' * 100 + chr(10) + MARK) in t:
            out.append(n)
    return out


def verify(name):
    r = subprocess.run([sys.executable, SEALER, '--verify', os.path.join(D, name)], capture_output=True, text=True, encoding='utf-8', errors='replace')
    o = r.stdout or ''
    return dict(rc=r.returncode, intact='SEAL INTACT' in o, sha256=hashlib.sha256(open(os.path.join(D, name), 'rb').read()).hexdigest())


def census(tag):
    names = sealed_files()
    out = {}
    for n in names:
        out[n] = verify(n)
    rec('  %s : %d sealed files in data/ ; INTACT at %d of them ; every file hashed as it stands'
        % (tag, len(names), sum(1 for v in out.values() if v['intact'])))
    return out


def runfile(base):
    p, k = os.path.join(D, base + '_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, base + '_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    return os.path.basename(p)


def main(argv):
    rec('=' * 100)
    rec("b344 -- COMPONENT 2, THE SEAL'S OWN CLOCK. ### the census of every existing seal, and the fixtures.")
    rec('=' * 100)
    if argv and argv[0] == '--before':
        c = census('BEFORE THE REPAIR')
        io.open(BEFORE, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(c, indent=1))
        src = io.open(SEALER, encoding='utf-8').read()
        rec('  the tool as it stands : %d lines ; it writes no clock (`%s` present : %s)' % (len(src.splitlines()), CLOCK.strip(), CLOCK in src))
        rec('  ### the repair is made with the editor, BY THE ORDER\'S WORDS, after this census.')
        rec('=' * 100)
        runfile('b344_seal_before')
        return 0
    if not (argv and argv[0] == '--after'):
        print(__doc__)
        return 2
    b = json.load(io.open(BEFORE, encoding='utf-8'))
    a = census('AFTER THE REPAIR')
    io.open(AFTER, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(a, indent=1))
    same_verdict = [n for n in b if n in a and a[n]['intact'] == b[n]['intact'] and a[n]['rc'] == b[n]['rc']]
    rewritten = [n for n in b if n in a and a[n]['sha256'] != b[n]['sha256']]
    missing = [n for n in b if n not in a]
    rec('  ### every existing seal gives the SAME verdict before and after : %d of %d ; rewritten : %s ; missing : %s'
        % (len(same_verdict), len(b), rewritten if rewritten else 'none', missing if missing else 'none'))
    src = io.open(SEALER, encoding='utf-8').read()
    rec('  ### the repaired tool writes the clock (`%s` present in its source : %s) ; cmd_verify unchanged in its logic : %s'
        % (CLOCK.strip(), CLOCK in src, 'the hash is still taken over the bytes ABOVE the block' if 'def digest(body)' in src and 'split_body' in src else '### CHANGED ###'))
    # ### the fixtures, on scratch files that are not registrations
    scratch = os.path.join(D, 'b344_seal_fixture.txt')
    io.open(scratch, 'w', encoding='utf-8', newline=chr(10)).write('### a scratch file for b344\'s seal fixtures. ### NOT A REGISTRATION.\n')
    r1 = subprocess.run([sys.executable, SEALER, '--seal', scratch], capture_output=True, text=True, encoding='utf-8', errors='replace')
    txt = io.open(scratch, encoding='utf-8').read()
    has_clock = CLOCK in txt
    stamp = re.search(re.escape(CLOCK) + r'(\S+)', txt)
    v1 = subprocess.run([sys.executable, SEALER, '--verify', scratch], capture_output=True, text=True, encoding='utf-8', errors='replace')
    f1 = has_clock and 'SEAL INTACT' in (v1.stdout or '')
    rec('  FIXTURE 1 -- a fresh seal carries the clock and verifies : clock present %s (%s) ; INTACT %s : %s'
        % (has_clock, stamp.group(1) if stamp else '(none)', 'SEAL INTACT' in (v1.stdout or ''), 'PASS' if f1 else '### FAIL ###'))
    io.open(scratch, 'w', encoding='utf-8', newline=chr(10)).write(txt.replace(stamp.group(1), '1999-01-01T00:00:00Z') if stamp else txt)
    v2 = subprocess.run([sys.executable, SEALER, '--verify', scratch], capture_output=True, text=True, encoding='utf-8', errors='replace')
    f2 = 'SEAL INTACT' in (v2.stdout or '')
    rec('  FIXTURE 2 -- the clock ALTERED and the file STILL verifies : %s' % f2)
    rec('  ###      **AND THAT IS THE HONEST LIMIT OF THE REPAIR: THE CLOCK IS OUTSIDE THE HASH.** ### It records when the')
    rec('  ###      seal was written by a tool that meant to record it; it is not evidence against a seat that would alter it.')
    body = txt[:txt.find('=' * 100 + chr(10) + MARK)]
    io.open(scratch, 'w', encoding='utf-8', newline=chr(10)).write(body + 'tampered\n' + txt[txt.find('=' * 100 + chr(10) + MARK):])
    v3 = subprocess.run([sys.executable, SEALER, '--verify', scratch], capture_output=True, text=True, encoding='utf-8', errors='replace')
    f3 = 'SEAL INTACT' not in (v3.stdout or '')
    rec('  FIXTURE 3 -- the BODY altered and the seal REFUSES (the arm that must still fire) : %s' % f3)
    os.remove(scratch)
    ok = len(same_verdict) == len(b) and not rewritten and not missing and CLOCK in src and f1 and f2 and f3
    rec('')
    rec('  ### ### **WHAT THE REPAIR DOES NOT DO: IT DOES NOT RECOVER b342\'s LOST TIMESTAMP**, and it makes no act')
    rec('  ### sealed before it checkable by time. ### b342\'s `G-ORDER` stays a defective bar with its consequence carried.')
    rec('  ### ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    rf = runfile('b344_seal_after')
    io.open(os.path.join(D, 'b344_seal_clock.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(sealed_before=len(b), sealed_after=len(a), same_verdict=len(same_verdict), rewritten=rewritten, missing=missing,
             clock_in_source=bool(CLOCK in src), fixture_fresh=bool(f1), fixture_clock_outside_hash=bool(f2), fixture_body_refused=bool(f3),
             stamp=stamp.group(1) if stamp else None, ok=bool(ok), run_file=rf), indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
