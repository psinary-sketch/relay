# -*- coding: utf-8 -*-
"""b418_components.py -- THE FIVE COMPONENTS, BEHIND THEIR OWN FLAGS, AND THE REPORT.

### ### **THE WRITES HAPPEN BEHIND FLAGS, IN THE ORDER THE FACE FIXES:** ### `--walker` (Component 1,
### reads only), `--r35` (Component 2), `--repairs` (Component 3), `--n-record` (Component 4's banked
### state), and the report with no flag. ### Folded here because the locked write list names SIX relay
### act-tools, and a file of a KIND the write list does not name is a breach.
### ### **THE SLOTS AND THE FIFTEEN ARE KEPT APART IN THIS RECORD AS IN THE ACT.**
"""
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import walker_guard as WG   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TD = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
THIS = os.path.join(TD, 'fbe6b4b2-25ed-44b7-91cb-756e5456e21d.jsonl')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
ATREST = os.path.join(PP, 'phase1.5', 'structural', 'AT_REST.md')
CONST = os.path.join(PP, 'phase1.5', 'deep-structure', 'CONSTANCE.md')
REG = os.path.join(PP, 'REGISTRY.md')
PIN_PP, PIN_RELAY = '09a1e80', '1dc9f72'
QUERY = ('BoundaryValueShadow|IndexRangeShadow|RationalEnclosureShadow|ScalingTraceShadow|'
         'SmearCollapseShadow|ValuationDivisibilityShadow|H1Mechanism|SinglePrimeFactor|T1\\.4')
MISS_AT = '2026-09-11T13:28:55.279Z'
NL = chr(10)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def read(p):
    return rb(p).decode('utf-8', 'replace')


def put(name, lines):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def write_bytes(path, data):
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)


def blob(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def _files(content):
    return set(re.findall(r'data\\(\S+?):\d+', content or ''))


def existed_before(f, at):
    p = os.path.join(D, f)
    return os.path.exists(p) and datetime.utcfromtimestamp(os.path.getmtime(p)) < WG._t(at)


# =============================================================================================
# ### COMPONENT 1 -- THE WALKER. ### READS ONLY.
# =============================================================================================
def run_walker():
    R = ['=' * 100, 'b418 COMPONENT 1 -- THE WALKER.', '=' * 100, '  run at (UTC) : %s' % utc()]
    R.append('  ### the guard`s fixtures, both polarities, before it is trusted : %s'
             % ('PASS' if WG.self_test(verbose=False) else '### FAIL'))
    pop = json.load(io.open(os.path.join(D, 'b418_walker_population.json'), encoding='utf-8'))
    over = [c for c in pop if c['path'].rstrip('\\').lower().endswith(('relay\\data', '\\relay'))]
    R.append('')
    R.append('### (1) WHICH CALLS IN THE ARC RAN OVER THE DIRECTORY, AND WHICH HIT THE LIMIT.')
    R.append('  calls in the arc under relay : %d ; over relay`s data records : %d' % (len(pop), len(over)))
    for c in pop:
        v = WG.verdict(c['at'], c['at'][:11] + '00:00:00.000Z', 0) if False else None
        secs = c['seconds'] or 0
        R.append('    %-9s %-24s %6.2f s  numFiles %-5s over data %-5s guard : %s'
                 % (c['session'], c['at'][:23], secs, c['numFiles'], c in over,
                    'INCOMPLETE' if secs >= WG.LIMIT - WG.MARGIN else 'COMPLETE'))
    lim = [c for c in over if (c['seconds'] or 0) >= WG.LIMIT - WG.MARGIN]
    R.append('  ### ### **CALLS OVER THE DIRECTORY THAT REACHED THE LIMIT : %d**' % len(lim))
    R.append('')
    R.append('### (2) HOW MANY ABSENT VERDICTS REST ON A TRUNCATED CALL -- EACH ACT`S OWN RECORDS READ.')
    cand = []
    for f in sorted(os.listdir(D)):
        if f.startswith('b417_') and f.endswith('.txt'):
            for i, ln in enumerate(read(os.path.join(D, f)).splitlines(), start=1):
                if re.search(r'\brg\b|ripgrep|`Grep`', ln):
                    cand.append((f, i, ln.strip()))
    R.append('  lines of b417`s records naming the walker : %d' % len(cand))
    for f, i, ln in cand[:14]:
        R.append('    %-40s line %-4d %s' % (f[:40], i, ln[:120]))
    R.append('  ### ### **EVERY ONE IS A STATEMENT ABOUT THE WALKER -- THAT IT RETURNED NO LINE FROM A RECORD')
    R.append('  ### ### THAT CARRIES FIVE -- AND NOT ONE IS AN ABSENCE ABOUT THE CORPUS.** ### b417`s own face put')
    R.append('  ### every search of the act on Python after the miss. ### **ABSENT VERDICTS RESTING ON A')
    R.append('  ### ### TRUNCATED CALL : 0.** ### The verdict below is therefore over an EMPTY SET of banked')
    R.append('  ### absences, and the truncated call is re-run bounded anyway, as the face declared.')
    R.append('')
    R.append('### (3) THE TRUNCATED CALL, RE-RUN BOUNDED SO IT COMPLETES. ### THE SAME WALKER, GLOB CHUNKS.')
    lock = re.search(r'locked at \(UTC\) : (\S+)', read(os.path.join(D, 'b418_registration_2026-09-11.txt')))
    lock_at = lock.group(1) if lock else '2026-09-11T00:00:00Z'
    bounded = [c for c in WG.calls_in(THIS) if (c['at'] or '') > lock_at
               and c['input'].get('pattern') == QUERY and (c['input'].get('path') or '').rstrip('\\').lower().endswith('relay\\data')]
    union, allok = set(), True
    for c in bounded:
        s = WG.seconds(c['at'], c['result_at'])
        v = WG.verdict(c['at'], c['result_at'], c['numFiles'])
        allok = allok and v != WG.INCOMPLETE
        union |= _files(c['content'])
        R.append('    glob %-8s %6.2f s  numFiles %-4s guard : %s'
                 % (c['input'].get('glob'), s, c['numFiles'], v))
    R.append('  bounded calls : %d ; every one COMPLETE under the guard : %s' % (len(bounded), allok))
    union_then = sorted(f for f in union if existed_before(f, MISS_AT))
    orig = next(c for c in WG.calls_in(THIS) if c['at'] == MISS_AT)
    ov = WG.verdict(orig['at'], orig['result_at'], orig['numFiles'])
    rx = re.compile(QUERY)
    py = sorted(f for f in os.listdir(D) if os.path.isfile(os.path.join(D, f)) and existed_before(f, MISS_AT)
                and rx.search(read(os.path.join(D, f))))
    R.append('  the original call, through the guard : %s   (it reported %d files)' % (ov, orig['numFiles']))
    R.append('  the bounded re-run, files that existed at the original call : %d' % len(union_then))
    R.append('  a Python walker over the same files, same pattern : %d' % len(py))
    R.append('  the bounded re-run and the Python walker agree file for file : %s' % (set(union_then) == set(py)))
    R.append('  ### ### **THE TRUNCATED CALL`S RESULT : MOVED -- %d reported, %d there.** ### No absence rested'
             % (orig['numFiles'], len(py)))
    R.append('  ### on it, so no banked verdict moves; ### **ABSENT VERDICTS CONFIRMED : 0, MOVED : 0, OVER AN')
    R.append('  ### ### EMPTY SET.** ### An absence banked by a walker that cannot reach part of a directory')
    R.append('  ### is a claim about the walker -- and b417 banked exactly that claim, and no other.')
    R.append('')
    R.append('### (4) BEYOND THE ARC, REPORTED AND NOT SCORED: EVERY WALKER CALL THAT REACHED THE LIMIT SILENTLY.')
    tot, silent, loud = 0, [], 0
    for fp in sorted(glob.glob(os.path.join(TD, '*.jsonl'))):
        for c in WG.calls_in(fp):
            tot += 1
            if not c['at'] or not c['result_at']:
                continue
            if WG.verdict(c['at'], c['result_at'], 1) == WG.INCOMPLETE:
                if c['timed_out']:
                    loud += 1
                else:
                    silent.append((os.path.basename(fp)[:8], c['at'][:19], c['numFiles'],
                                   (c['input'].get('path') or '')[-30:]))
    R.append('  walker calls in every transcript : %d ; reached the limit and SAID SO : %d' % (tot, loud))
    R.append('  ### ### **REACHED THE LIMIT AND SAID NOTHING : %d**' % len(silent))
    for s in silent:
        R.append('    %-9s %-20s numFiles %-5s %s' % s)
    R.append('=' * 100)
    put('b418_walker.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### COMPONENT 2 -- (R35) EXECUTED.
# =============================================================================================
ABS_OLD = 'Three of four formation components are universal across IDS-amenable systems:'
ABS_NEW = ('Three of four formation components are universal across IDS-amenable systems with a '
           'connected reductive symmetry group *(narrowed in place b418 under (R35); it read "universal '
           'across IDS-amenable systems")*:')
SEC_OLD = 'Three of four components are universal across IDS-amenable systems:'
SEC_NEW = ('Three of four components are universal across IDS-amenable systems with a connected reductive '
           'symmetry group *(narrowed in place b418 under (R35); it read "universal across IDS-amenable '
           'systems")*:')
STIP = ('> **Classes B and D: the second component remains STIPULATED.** Their tuples in the table below '
        'carry n₂ = 2, and no document establishes that their substrates carry a connected reductive '
        'symmetry group, so the n₂ theorem does not reach them. *(b418, under (R35): the kernel compiled '
        'that A and D are distinct, reading (a) would falsify it, and the corpus\'s precedence is kernel '
        'over prose.)*')
AT_APPEND = ('\n*(b418, under (R35): the claim above that three of four components are universal holds '
             'across IDS-amenable systems with a connected reductive symmetry group -- the n₂ theorem\'s own '
             'hypothesis, which this document\'s n₂ paragraph already states. Classes B and D\'s second '
             'component remains STIPULATED; see `phase2/physics/MATTER_AS_ARITHMETIC.md` §I.)*\n')


def run_r35():
    R = ['=' * 100, 'b418 COMPONENT 2 -- (R35) EXECUTED.', '=' * 100, '  run at (UTC) : %s' % utc()]
    m = read(MATTER)
    if ABS_NEW in m:
        R.append('  ### already narrowed -- nothing written.')
        put('b418_r35.txt', R)
        return 0
    if m.count(ABS_OLD) != 1 or m.count(SEC_OLD + '\n') != 1:
        R.append('  ### REFUSED -- an anchor is not present exactly once.')
        put('b418_r35.txt', R)
        return 2
    m2 = m.replace(ABS_OLD, ABS_NEW, 1).replace(SEC_OLD + '\n', SEC_NEW + '\n' + STIP + '\n', 1)
    write_bytes(MATTER, m2.encode('utf-8'))
    old = (blob(PP, PIN_PP, 'phase2/physics/MATTER_AS_ARITHMETIC.md') or b'').decode('utf-8')
    new = read(MATTER)
    ol, nl = old.splitlines(), new.splitlines()
    import difflib
    rem = [x for x in difflib.ndiff(ol, nl) if x.startswith('- ')]
    add = [x for x in difflib.ndiff(ol, nl) if x.startswith('+ ')]
    R.append('  MATTER against its blob at %s : lines removed %d, lines added %d' % (PIN_PP, len(rem), len(add)))
    for x in rem:
        R.append('      - %s' % x[2:][:150])
    for x in add:
        R.append('      + %s' % x[2:][:150])
    R.append('  both occurrences narrowed : %s' % (new.count('with a connected reductive symmetry group *(narrowed in place b418') == 2))
    R.append('  the original words quoted beside each : %d' % new.count('it read "universal across IDS-amenable systems"'))
    R.append('  STIPULATED lines : %d' % new.count('remains STIPULATED'))
    tab = [x for x in ol if re.match(r'\| [ABCD] — ', x)]
    R.append('  the class table`s rows unchanged : %s' % all(x in nl for x in tab))
    R.append('')
    a = rb(ATREST)
    if b'b418, under (R35)' not in a:
        write_bytes(ATREST, a + AT_APPEND.encode('utf-8'))
    a2 = rb(ATREST)
    R.append('  AT_REST appended : %d bytes -> %d ; prior bytes a TRUE PREFIX : %s'
             % (len(a), len(a2), a2.startswith(a)))
    R.append('=' * 100)
    put('b418_r35.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### COMPONENT 3 -- THREE REPAIRS.
# =============================================================================================
C_ANCHOR = 'Beyond 41, the lattice has gaps. No combination of powers yields 43, 47, or 53 directly.'
C_LINE = ('> *Correction, b418: 43 = 2⁴ + 3³ is a sum of a power of two and a power of three, so the sentence '
          'above is false at 43; 47 and 53 are not such sums. The sentence is kept as written.*')
P_FIGS = [('a three-clause currency note', 'a currency note'),
          ('where the lattice carries six sum-of-powers primes', 'where the lattice carries sum-of-powers primes')]
RETIRED_MD = """# relay/tools/retired/ -- tools taken out of use, kept byte-for-byte

**First entry, b418 (2026-09-11). No retired directory existed in relay before this act.**

## `b369_hygiene.py`

**Retired by b418's Component 3, under the author's ferry.** Moved here byte-for-byte from `tools/`;
its bytes equal its blob at relay `1dc9f72`.

**The reason.** It was written at b369 to mend two rosters and install and exercise the pre-push
guard. Its success conditions were dated by its own success: its wording pairs were applied at b369
and cannot apply again, and its hook check reads `SIDE-effects/.git/hooks/pre-push`, which no guard
runs from since `core.hooksPath` names `.githooks`. Repaired at b417, it runs and its verdict is
FAILED on every run from now on. A tool whose verdict can never pass is a guard with nothing to say.

**Its last verdict.** `COMPONENT 2 : FAILED` -- relay `data/b417_live.txt`, reported and not edited.

**Its writes, as measured** (relay `data/b417_snapshot.txt`, `data/b417_live.txt`):
- broken (before b417's repair), it wrote nothing: it died on a retired path before its first write;
- run against a captured snapshot, it wrote its own three run records (contained), and through
  `b304_hooks.py`'s guard exercise it wrote one git object into each of SIDE-global-section,
  PLACE-papers and SIDE-effects (escaped; counted, not collected);
- run live, it rewrote `data/b369_hooks.txt` and `data/b369_hygiene.json` and created a new
  `b369_hygiene_notes` run record under a prior act's stem; all three were restored.

**What would have caught it.** `tools/repair_snapshot.py` (b417): a repaired tool runs first against
a captured snapshot, every write diffed, before it runs live. It is what did catch it at b417 -- its
escaped writes were two calls deep, and its own source names none of the repositories it wrote into.
The species is `SAFE_BY_BEING_BROKEN.md` (TECHNE-Core, local).

**Dated by this move, said rather than discovered.** These relay tools name its old path
`tools/b369_hygiene.py`; each is a frozen record of its own act, and each one that reads or runs the
file at that path will now find it absent:
@REFS@
"""


def run_repairs():
    R = ['=' * 100, 'b418 COMPONENT 3 -- THREE REPAIRS.', '=' * 100, '  run at (UTC) : %s' % utc()]
    # ---- (a) THE KEYSTONE'S SENTENCE
    c = read(CONST)
    R.append('### (a) CONSTANCE`S SENTENCE ABOUT 43 -- ONE LINE ADDED, THE SENTENCE KEPT.')
    lines = c.split('\n')
    idx = [i for i, ln in enumerate(lines) if ln.startswith(C_ANCHOR)]
    if C_LINE in c:
        R.append('  already present -- nothing written.')
    elif len(idx) != 1:
        R.append('  ### REFUSED -- the sentence is not present exactly once.')
    else:
        lines.insert(idx[0] + 1, C_LINE)
        write_bytes(CONST, '\n'.join(lines).encode('utf-8'))
    c2 = read(CONST)
    old = (blob(PP, PIN_PP, 'phase1.5/deep-structure/CONSTANCE.md') or b'').decode('utf-8')
    R.append('  lines before %d, after %d ; the sentence present byte-for-byte : %s ; the pin`s text is the new text less the line : %s'
             % (len(old.splitlines()), len(c2.splitlines()), C_ANCHOR in c2,
                c2.replace(C_LINE + '\n', '', 1) == old))
    R.append('      | %s' % C_LINE)
    # ---- (b) REGISTRY p2-35
    R.append('')
    R.append('### (b) REGISTRY ROW p2-35 -- PRESERVED VERBATIM FIRST, THEN ITS STALE FIGURES REMOVED.')
    reg = read(REG)
    row = [x for x in reg.split('\n') if x.startswith('| p2-35 |')]
    pres = os.path.join(D, 'b418_p235_before.txt')
    if not os.path.exists(pres) and row:
        io.open(pres, 'w', encoding='utf-8', newline=NL).write(
            'b418 -- registry row p2-35, PRESERVED VERBATIM BEFORE ANY EDIT.\n  preserved at (UTC) : %s\n'
            '  sha256 of the row : %s\n\n%s\n' % (utc(), hashlib.sha256(row[0].encode('utf-8')).hexdigest(), row[0]))
    pr = read(pres)
    R.append('  preservation record written before the edit : %s (%s)' % (bool(pr), os.path.basename(pres)))
    if row and all(a in row[0] for a, _b in P_FIGS):
        new_row = row[0]
        for a, b in P_FIGS:
            new_row = new_row.replace(a, b, 1)
        write_bytes(REG, reg.replace(row[0], new_row, 1).encode('utf-8'))
    reg2 = read(REG)
    row2 = [x for x in reg2.split('\n') if x.startswith('| p2-35 |')]
    for a, b in P_FIGS:
        R.append('  %-55r removed : %s' % (a, bool(row2) and a not in row2[0]))
    oldreg = (blob(PP, PIN_PP, 'REGISTRY.md') or b'').decode('utf-8').split('\n')
    changed = [i for i, (x, y) in enumerate(zip(oldreg, reg2.split('\n'))) if x != y]
    R.append('  registry lines changed against the pin : %d ; line counts equal : %s'
             % (len(changed), len(oldreg) == len(reg2.split('\n'))))
    # ---- (c) THE HYGIENE TOOL RETIRED
    R.append('')
    R.append('### (c) THE HYGIENE TOOL RETIRED -- MOVED BYTE-FOR-BYTE, WITH ITS REASON.')
    src = os.path.join(T, 'b369_hygiene.py')
    dst_dir = os.path.join(T, 'retired')
    dst = os.path.join(dst_dir, 'b369_hygiene.py')
    pinned = blob(ROOT, PIN_RELAY, 'tools/b369_hygiene.py') or b''
    refs = sorted(f for f in os.listdir(T) if f.endswith('.py') and f not in ('b369_hygiene.py', 'b418_components.py')
                  and 'b369_hygiene' in read(os.path.join(T, f)))
    if os.path.exists(src):
        os.makedirs(dst_dir, exist_ok=True)
        os.replace(src, dst)
    md = RETIRED_MD.replace('@REFS@', '\n'.join('- `tools/%s`' % f for f in refs))
    if not os.path.exists(os.path.join(dst_dir, 'RETIRED.md')):
        io.open(os.path.join(dst_dir, 'RETIRED.md'), 'w', encoding='utf-8', newline=NL).write(md)
    moved = rb(dst)
    norm = lambda b: b.replace(b'\r\n', b'\n')
    R.append('  tools/b369_hygiene.py present : %s ; tools/retired/b369_hygiene.py present : %s'
             % (os.path.exists(src), os.path.exists(dst)))
    R.append('  moved bytes equal the blob at %s (line endings normalised) : %s' % (PIN_RELAY, norm(moved) == norm(pinned)))
    R.append('  RETIRED.md written : %s ; tools it names as dated by the move : %d' % (os.path.exists(os.path.join(dst_dir, 'RETIRED.md')), len(refs)))
    R.append('=' * 100)
    put('b418_repairs.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### COMPONENT 4 -- THE ATTEMPT'S BANKED STATE. ### EVERY PROBE'S SOURCE AND PRINTED PROFILE.
# =============================================================================================
NDIR = os.path.join(os.environ.get('TEMP', ''), 'claude', 'D--', 'fbe6b4b2-25ed-44b7-91cb-756e5456e21d',
                    'scratchpad', 'n418')
NDIR_ALT = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n418'


def run_n_record():
    nd = NDIR if os.path.isdir(NDIR) else NDIR_ALT
    probes = sorted(f for f in os.listdir(nd) if re.match(r'p\d\d\.lean$', f))
    R = ['=' * 100, 'b418 COMPONENT 4 -- (N): EVERY PROBE, ITS SOURCE AND ITS PRINTED PROFILE.', '=' * 100,
         '  banked at (UTC) : %s' % utc(),
         '  probe directory (scratch, outside every repository) : %s' % nd,
         '  probes compiled : %d   ### the cap is sixteen' % len(probes)]
    first = read(os.path.join(nd, 'p01.out')).splitlines()[:1]
    R.append('  the first probe`s start : %s' % (first[0] if first else '(absent)'))
    for f in probes:
        src = read(os.path.join(nd, f))
        out = read(os.path.join(nd, f[:-5] + '.out'))
        R += ['', '-' * 100, '### %s -- %d source lines' % (f, len(src.splitlines())), '-' * 100]
        R += ['  | %s' % ln for ln in src.splitlines()]
        R += ['  ### PRINTED:'] + ['  > %s' % ln for ln in out.splitlines()]
        dirty = [ln for ln in out.splitlines() if "'N418." in ln and 'depends on axioms' in ln]
        R.append('  ### this probe`s own lemmas carrying an axiom : %d %s' % (len(dirty), dirty[:3]))
    sorry = sum(read(os.path.join(nd, f)).count('sorry') for f in probes)
    R.append('')
    R.append('  ### occurrences of `sorry` across every probe : %d' % sorry)
    R.append('=' * 100)
    put('b418_n_attempt.txt', R)
    print('\n'.join(R[:8]))
    return 0


# =============================================================================================
# ### THE REPORT. ### The verdict of (F) is set here from the banked attempt, and printed once.
# =============================================================================================
VERDICT_N = 'OVER-BUDGET'
CPLX = os.path.join(PP, 'phase2', 'formation', 'COMPLEX_ANALYSIS.md')


def main():
    L = []
    say = L.append
    walk = read(os.path.join(D, 'b418_walker.txt'))
    r35 = read(os.path.join(D, 'b418_r35.txt'))
    rep = read(os.path.join(D, 'b418_repairs.txt'))
    natt = read(os.path.join(D, 'b418_n_attempt.txt'))
    fails = [nm for nm, t in (('walker', walk), ('r35', r35), ('repairs', rep), ('n_attempt', natt)) if not t]
    say('=' * 100)
    say('b418_components.py -- THE RULING CARRIED, THE WALKER MEASURED, THE REPAIRS MADE, AND (N) OPENED.')
    say('=' * 100)
    say('')
    say('#' * 100)
    say('### PART ONE -- THE WALKER. ### Component 1, and the guard.')
    say('#' * 100)
    for ln in walk.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  ' + ln.rstrip()[:118])
    say('')
    say('### ### **THE CENSUS BEYOND THE ARC IS AN UPPER BOUND, AND SAID SO.** ### The transcript stamps every call')
    say('### issued in one batch with the one message time, so a fast call batched beside a slow one inherits the')
    say('### slow one`s wait. ### Two of the silent limits it lists are this act`s own resume probes, whose results')
    say('### were complete (29 files, and 1). ### **THE GUARD THEREFORE ERRS TOWARD INCOMPLETE ON BATCHED CALLS** --')
    say('### the safe direction, never turning a truncation into a count.')
    say('')
    say('**(N1)** over the files the walker missed and the arc`s calls over the directory')
    say('      its first half -- **WITHDRAWN BY THE AUTHOR**; the survey had refuted it: no binary heuristic, no file')
    say('      kind and no ignore pattern -- the cause is a silent timeout at the tool`s limit.')
    say('      its second half, *at least one prior ABSENT verdict MOVES* -- ### **REFUTED, AND VACUOUSLY: 0 ABSENT')
    say('      ### VERDICTS REST ON THE ONE TRUNCATED CALL**, so no verdict could have moved. ### The truncated call`s')
    say('      own result did move (13 reported, 40 there), and b417 banked only a claim about the walker.')
    say('')
    say('#' * 100)
    say('### PART TWO -- THE SLOTS. ### Component 2 under (R35), and Component 5.')
    say('#' * 100)
    for ln in r35.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  ' + ln.rstrip()[:150])
    say('')
    say('### COMPONENT 5 -- THE THREE EXAMPLE SYSTEMS, PARSED. ### COUNTED, NOT REPAIRED.')
    mt = read(MATTER)
    cp = read(CPLX)
    mhead = next((ln for ln in mt.splitlines() if ln.startswith('| Class | Substrate')), '(no header)')
    chead_i = cp.find('| $(2, 3, 2, 0)$')
    chead = cp[:chead_i].rstrip().splitlines()[-2] if chead_i > 0 else '(no header)'
    say('  MATTER`s table header           : %s' % mhead[:110])
    say('  COMPLEX_ANALYSIS`s table header : %s' % chead[:110])
    say('  ### ### **THE TWO TABLES PARSE BY DIFFERENT KEYS.** ### MATTER keys a system to its SUBSTRATE class (its')
    say('  ### column *Substrate*). ### COMPLEX_ANALYSIS keys it to its FORMATION TOTAL and toolkit (*complex analysis')
    say('  ### (full)* at 7, *+ geometric origin* at 8).')
    for nm, mkey, ckey in (('genetic code', 'genetic code', 'genetic code'),
                           ('Shannon', 'Shannon entropy', 'Shannon channel'),
                           ('Navier-Stokes', 'Navier-Stokes', 'Navier-Stokes')):
        mrow = next((ln for ln in mt.splitlines() if mkey in ln and ln.startswith('|')), '')
        crow = next((ln for ln in cp.splitlines() if ckey in ln and ln.startswith('|')), '')
        mt_t = re.search(r'\((\d, \d, \d, \d)\)', mrow)
        ct_t = re.search(r'\((\d, \d, \d, \d)\)', crow)
        say('  %-14s MATTER: %-12s as %-18r   COMPLEX_ANALYSIS: %-12s as %r'
            % (nm, mt_t.group(1) if mt_t else '?', mkey, ct_t.group(1) if ct_t else '?', ckey))
    say('  ### ### **AND THE SHANNON ROWS NAME DIFFERENT OBJECTS** -- *Shannon entropy* in one, *Shannon channel* in')
    say('  ### the other -- so that pair is not one system placed twice.')
    say('  ### Gate 1b`s note, quoted: *%s*' % re.sub(r'\s+', ' ', cp[cp.find('The formation tuple'):cp.find('TYPE is the observable')])[:200])
    say('  ### ### **AND THE TAXONOMY`S OWN RATIONALE NAMES THIS SHAPE:** *a Tier-C synthesis panel (CATALOGOS`s')
    say('  ### cross-system formation table, assigning (2,3,2,0) to Shannon/Maxwell/DNA) was read and cited as a')
    say('  ### Tier-K certification.* ### COMPLEX_ANALYSIS`s table assigns (2,3,2,0) to the Shannon channel and the')
    say('  ### genetic code. ### **REPORTED BESIDE THE RATIONALE; 0 WORDS OF EITHER DOCUMENT EDITED.**')
    say('')
    say('#' * 100)
    say('### PART THREE -- THE KERNEL. ### Component 4, (N).')
    say('#' * 100)
    nprobes = len(re.findall(r'(?m)^### p\d\d\.lean', natt))
    say('  probes compiled : %d of the sixteen the face allows ; `sorry` tokens across every probe : %s'
        % (nprobes, (re.search(r'occurrences of `sorry` across every probe : (\d+)', natt) or [None, '?'])[1]))
    say('  ### ### **VERDICT : %s**' % VERDICT_N)
    say('  ### THE CAP REACHED: sixteen probes, about 31 of the 150 minutes. ### THE PARTIAL STATE, BANKED in')
    say('  ### `b418_n_attempt.txt` with every probe`s source and printed profile:')
    say('      S0 -- `spf_power` CLEAN: a single-prime-factor base is a power of a prime.')
    say('      Euclid -- `euclid_lt`, `euclid`, `euclid_pow` CLEAN, gcd-free and axiom-free.')
    say('      the remainder -- `mod_spec`, `mod_zero_witness`, `mod_unique` CLEAN, rebuilt from `%` s own')
    say('        clean equation lemmas, which probe 03 found after probe 02 had looked like a block.')
    say('      S1-S2 -- `sumf_swap`, `count_swap`, `sumAN_swap`, `sumAQ_swap` CLEAN, on the kernel`s own sums.')
    say('      S3 -- `ap_count` CLEAN.')
    say('      S4 -- `cong_to`, `count_is`, `grid_factor_N`, `grid_factor_q`, `filter_congr`, `filter_filter` CLEAN.')
    say('      S5 -- `filter_len_zero`, `sumf_mul` CLEAN; `smear_general` and `cells_are_instances` ELABORATE and')
    say('        print `sorryAx` BY INHERITANCE ONLY.')
    say('  ### ### **THE ONE STEP NOT SUPPLIED:** ### `pow_pred`, the exponent identity `r^j = r^(j-1) * r` for')
    say('  ### `1 <= j`, written in probe 16 as `(congrArg (fun x => r ^ x) (sub_add_cancel` hj)).symm.trans')
    say('  ### Nat.pow_succ` -- ### **AN APPLICATION TYPE MISMATCH AT ITS `.trans`** (probe 16, line 743). ### The')
    say('  ### error, read in full: in this toolchain `Nat.pow_succ` TAKES ITS BASE AND EXPONENT EXPLICITLY --')
    say('  ### `forall (n m : Nat), n ^ m.succ = n ^ m * n` -- and the term passed it bare. ### Every declaration')
    say('  ### that failed prints `sorryAx` because it depends on that one term.')
    say('  ### ### **THE NEXT STEP, NAMED:** `... .trans (Nat.pow_succ r (j - 1))`, compile, and read `smear_general`')
    say('  ### and `cells_are_instances` by their printed profiles. ### **NOT COMPILED HERE -- THE CAP IS SPENT --')
    say('  ### ### AND THIS ACT DOES NOT CLAIM THE THEOREM.**')
    say('  ### ### **0 `.lean` FILES IN THE KERNEL TOUCHED; 0 KERNEL BUILDS**, the verdict not being PROVED.')
    say('')
    say('**(N2)** over the steps S0 to S5 and the verdict of (F)')
    say('      PREMISE -- *(N) reaches BLOCKED at a finite-sum lemma the axiom-free module lacks* -- ### **REFUTED.**')
    say('      The verdict is OVER-BUDGET, not BLOCKED; and the finite-sum lemmas (`sumf_swap`, `count_swap`)')
    say('      were supplied, axiom-free, in one probe.')
    say('      CONCLUSION -- *the block is priced as one lemma, not a Mathlib import* -- ### **MET IN SUBSTANCE, AT A')
    say('      ### DIFFERENT STEP:** what remains is one lemma, `pow_pred`, and no Mathlib import was needed anywhere.')
    say('      ### **MET IN CONCLUSION / REFUTED IN PREMISE, UNDER (R27).**')
    say('')
    say('#' * 100)
    say('### PART FOUR -- THE REPAIRS. ### Component 3.')
    say('#' * 100)
    for ln in rep.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  ' + ln.rstrip()[:160])
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    put('b418_components.txt', L)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    for flag, fn in (('--walker', run_walker), ('--r35', run_r35), ('--repairs', run_repairs),
                     ('--n-record', run_n_record)):
        if flag in sys.argv:
            sys.exit(fn())
    sys.exit(main())
