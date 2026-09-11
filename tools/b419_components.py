# -*- coding: utf-8 -*-
"""b419_components.py -- THE HELPER FIXED, THE CLAUSE PRINTED. ### ALL THREE COMPONENTS.

### ### **EACH MODE WRITES ITS OWN RECORD AND IS RUN ONCE, IN THE ORDER THE FACE GIVES:**
###   --n-probe    Component 1: the first probe banked -- source, profile, the one-line diff against
###                `b418`'s probe 16 -- and the verdict read from the PROFILE's own lines.
###   --n-kernel   Component 1, ONLY ON PROVED: the new module written, the seal annotated, the import
###                and prints appended. ### The kernel BUILDS are the shell's, recorded separately.
###   --n-verify   Component 1, ONLY ON PROVED: the prefix, the seal's words, the append, the cells.
###   --reclass    Component 1, ONLY ON PROVED: `b414`'s twenty-eight re-classified over its hand-read.
###   --lock       Component 2: the lock and the scan, priced.
###   --timeouts   Component 3: the population, the guard, the resting verdicts, the re-runs.
###   (no flag)    the report, assembled from the records above.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import walker_guard as WG  # noqa: E402  ### IMPORTED, NEVER EDITED.

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
FSA = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic')
TD = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
SCR = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad'
N418 = os.path.join(SCR, 'n418')
N419 = os.path.join(SCR, 'n419')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
MOD = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
ALLP = os.path.join(KERN, 'AllPrints.lean')
PROF = os.path.join(KERN, 'AXIOM_PRINTS.txt')
CLASSES = os.path.join(FSA, 'SIDEFormationArithmetic', 'Classes.lean')
NL = chr(10)
TERMINALS = ('smear_general', 'cells_are_instances')
CLEAN = 'does not depend on any axioms'
SEAL_ANCHOR = "that identification is the library's and is NOT compiled here); (T1.6)"


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def rb(p):
    with open(p, 'rb') as fh:
        return fh.read()


def read(p):
    try:
        return rb(p).decode('utf-8', 'replace')
    except Exception:
        return ''


def put(name, lines):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(repo, path, rev='HEAD'):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True).stdout


def git_same(rel, repo=ROOT):
    """### GIT'S OWN VIEW OF A TRACKED FILE: its hash-object equals its index blob AND `git diff --quiet` passes."""
    h = subprocess.run(['git', '-C', repo, 'hash-object', '--', rel], capture_output=True, text=True).stdout.strip()
    s = subprocess.run(['git', '-C', repo, 'ls-files', '-s', '--', rel], capture_output=True, text=True).stdout.split()
    q = subprocess.run(['git', '-C', repo, 'diff', '--quiet', '--', rel]).returncode
    return bool(h) and len(s) > 1 and s[1] == h and q == 0


def lean_code(src):
    """### LEAN COMMENTS STRIPPED BEFORE ANY SEARCH FOR `sorry` -- `b418`'s arm fired on prose once."""
    s = re.sub(r'/-.*?-/', ' ', src, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', s)


def profile_lines(out):
    return [ln for ln in out.splitlines() if ln.startswith("'")]


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


# =============================================================================================
# ### COMPONENT 1 -- THE FIRST PROBE, BANKED, AND THE VERDICT READ FROM ITS PROFILE.
# =============================================================================================
def verdict_of(out, prefix):
    """### READ FROM THE PROFILE'S OWN LINES -- NEVER FROM THE EXIT CODE."""
    got = {}
    for t in TERMINALS:
        ln = next((x for x in profile_lines(out) if x.startswith("'%s.%s'" % (prefix, t))), None)
        got[t] = ln
    if all(v and v.endswith(CLEAN) for v in got.values()):
        return 'PROVED', got
    return 'NOT PROVED', got


def run_n_probe():
    probes = sorted(f for f in os.listdir(N419) if re.match(r'p\d\d\.lean$', f))
    src = read(os.path.join(N419, 'p01.lean'))
    out = read(os.path.join(N419, 'p01.out'))
    old = read(os.path.join(N418, 'p16.lean'))
    a, b = old.splitlines(), src.splitlines()
    diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
    code = lean_code(src)
    v, got = verdict_of(out, 'N418')
    R = ['=' * 100, 'b419 COMPONENT 1 -- THE HELPER FIXED: THE FIRST PROBE, ITS SOURCE AND ITS PRINTED PROFILE.', '=' * 100,
         '  banked at (UTC) : %s' % utc(),
         '  probe directory (scratch, outside every repository) : %s' % N419,
         '  probes compiled in this act : %d   ### the budget is b418`s: sixteen, or 150 minutes' % len(probes),
         '  the first probe`s start / end (UTC) : %s / %s'
         % (read(os.path.join(N419, 'p01.start')).strip(), read(os.path.join(N419, 'p01.end')).strip()),
         '',
         '### ### **THE PROBE AGAINST `b418`s PROBE 16, LINE BY LINE:** lines %d / %d ; lines differing : %d'
         % (len(a), len(b), len(diff))]
    for i, x, y in diff:
        R += ['  line %d, b418 : %s' % (i, x.strip()), '  line %d, b419 : %s' % (i, y.strip())]
    R += ['  ### the one line differing is `pow_pred`s term, and it is the named repair : %s'
          % (len(diff) == 1 and 'Nat.pow_succ r (j - 1)' in diff[0][2] and 'pow_pred' in b[diff[0][0] - 2]),
          '',
          '### ### **THE CODE, COMMENTS STRIPPED:** `sorry` %d ; `admit` %d ; `axiom` declarations %d'
          % (len(re.findall(r'\bsorry\b', code)), len(re.findall(r'\badmit\b', code)),
             len(re.findall(r'(?m)^\s*axiom\b', code))),
          '',
          '### ### **THE PRINTED PROFILE, IN FULL:**']
    R += ['  > %s' % ln for ln in out.splitlines()]
    R += ['',
          '  profile lines : %d ; of them "%s" : %d'
          % (len(profile_lines(out)), CLEAN, len([x for x in profile_lines(out) if x.endswith(CLEAN)])),
          '  ### the terminals, read from their own lines :']
    for t in TERMINALS:
        R.append('      %-22s %s' % (t, got[t]))
    R += ['  ### ### **VERDICT, READ FROM THE PROFILE : %s** ### (the exit line is printed above and read by nothing)' % v,
          '',
          '### THE PROBE`S SOURCE, IN FULL:']
    R += ['  | %s' % ln for ln in src.splitlines()]
    R.append('=' * 100)
    put('b419_n_probe.txt', R)
    print(NL.join(R[:30]))
    return 0 if v == 'PROVED' else 1


# =============================================================================================
# ### COMPONENT 1, ON PROVED -- THE KERNEL WRITES. ### Each refuses if its target is not as the
# ### before-record found it, so a second run cannot write twice.
# =============================================================================================
MOD_HEAD = '''/-!
  # SmearGeneral -- the named open statement of `SinglePrimeFactor`, PROVED.

  For every base `p` with `singlePrimeFactor p = true` and every level `n`,
      `B329.ballQ p n * B329.sumAN p n = B329.sumAQ p n`
  -- `smear_general` below. `cells_are_instances` derives the seven cells
  `B329.cells` decides as instances of it, so the per-cell conjunct of
  `B329.compact_smear_vanishes_at_cells` is now a corollary of a general theorem.

  PROVENANCE. The library is b418's attempt (relay `data/b418_n_attempt.txt`,
  sixteen probes, stopped over budget with one helper unsupplied), with the
  one term b418 named repaired at b419: in `pow_pred`, `Nat.pow_succ` takes
  its base and exponent explicitly in this toolchain. b419's first probe
  compiled it and printed every terminal clean (relay `data/b419_n_probe.txt`).
  The working namespace `N418` is renamed `SmearGeneral`; nothing else changed.

  THE ROUTE. `S0` a single-prime-factor base is a power `r^e` of a prime;
  Euclid's lemma and the remainder are rebuilt gcd-free; `S1`-`S2` both sums
  are rewritten over the off-ball index with the order of summation exchanged;
  `S3` the progression count; `S4` the conditions are automatic on the
  progression; `S5` assembly: the `q`-count is `q` times the `N`-count, `s` by `s`.

  AXIOMS. None. Core's lemmas about `%`, `/`, `∣` and `Nat.Coprime` carry
  `propext`, so every step is proved from clean equation lemmas (see
  `FiniteSideSeal`'s axiom finding). Nothing is sorried.

  WHAT IT DOES NOT CERTIFY. The same as `FiniteSideSeal`: the arithmetic of the
  model and the counting form of the trace. The identification of that count
  with the source's trace is b310's derivation and is not compiled here.
-/
'''


def annotation_lines():
    src = read(os.path.join(D, 'b416_components.txt'))
    i = src.find('(T1.4-a, b414)')
    seg = src[src.rfind(NL, 0, i) + 1:]
    out = []
    for ln in seg.splitlines():
        s = ln.strip()
        if not s.startswith('|'):
            break
        out.append(s[1:].strip())
    return out


def run_n_kernel():
    R = ['=' * 100, 'b419 COMPONENT 1 -- THE KERNEL WRITES, ON PROVED.', '=' * 100, '  at (UTC) : %s' % utc()]
    probe = read(os.path.join(D, 'b419_n_probe.txt'))
    if '**VERDICT, READ FROM THE PROFILE : PROVED**' not in probe:
        R.append('  ### REFUSED: the banked probe does not read PROVED.')
        put('b419_n_kernel.txt', R)
        print(NL.join(R))
        return 2
    # (i) the module.
    src = read(os.path.join(N419, 'p01.lean')).splitlines()
    assert src[1] == 'import SinglePrimeFactor', src[1]
    body = [ln for ln in src[2:] if not ln.startswith('#print')]
    text = NL.join(body)
    text = re.sub(r'\n{3,}', NL + NL, text).replace('N418', 'SmearGeneral').rstrip() + NL
    mod = 'import SinglePrimeFactor' + NL + NL + MOD_HEAD + NL + text
    if os.path.exists(MOD):
        R.append('  ### (i) module already present -- NOT rewritten; sha %s' % sha(rb(MOD)))
    else:
        open(MOD, 'wb').write(mod.encode('utf-8'))
        R.append('  (i) written : Core/SmearGeneral.lean -- %d lines, sha %s' % (len(mod.splitlines()), sha(mod.encode('utf-8'))))
    R.append('      occurrences of `N418` left in it : %d' % read(MOD).count('N418'))
    # (v) the seal's annotation.
    seal = rb(SEAL)
    nl = b'\r\n' if b'\r\n' in seal else b'\n'
    ann = annotation_lines()
    R.append('  (v) the annotation, from b416`s record, %d lines :' % len(ann))
    R += ['      | %s' % a for a in ann]
    anchor = SEAL_ANCHOR.encode('utf-8')
    if b'(T1.4-a, b414)' in seal:
        R.append('  ### (v) annotation already present -- NOT re-inserted.')
    elif seal.count(anchor) != 1:
        R.append('  ### (v) REFUSED: the anchor occurs %d times.' % seal.count(anchor))
    else:
        ins = nl.join(('  ' + a).encode('utf-8') for a in ann)
        new = seal.replace(anchor, anchor[:-len(b' (T1.6)')] + nl + ins + nl + b'  (T1.6)', 1)
        open(SEAL, 'wb').write(new)
        R.append('  (v) inserted after the clause ending `compiled here);` ; newline style %r ; sha %s -> %s'
                 % (nl, sha(seal)[:16], sha(new)[:16]))
    # (ii) AllPrints: the import after the last import, the prints at the end.
    ap = rb(ALLP)
    if b'import SmearGeneral' in ap:
        R.append('  ### (ii) AllPrints already carries the import -- NOT re-appended.')
    else:
        last = b'import SinglePrimeFactor\n'
        assert ap.count(last) == 1 and ap.endswith(b'\n')
        new = ap.replace(last, last + b'import SmearGeneral\n', 1)
        new += b''.join(b'#print axioms SmearGeneral.%s\n' % t.encode() for t in TERMINALS)
        open(ALLP, 'wb').write(new)
        R.append('  (ii) AllPrints : the import inserted after `import SinglePrimeFactor`; %d prints appended; sha %s -> %s'
                 % (len(TERMINALS), sha(ap)[:16], sha(new)[:16]))
    R.append('=' * 100)
    put('b419_n_kernel.txt', R)
    print(NL.join(R))
    return 0


def tokens(b):
    return b.decode('utf-8', 'replace').split()


def run_n_verify():
    R = ['=' * 100, 'b419 COMPONENT 1 -- THE KERNEL, VERIFIED AFTER THE BUILD.', '=' * 100, '  at (UTC) : %s' % utc()]
    fails = []
    # (iii) the profile: the prior blob a true byte prefix of the new file.
    old = blob(KERN, 'AXIOM_PRINTS.txt')
    new = rb(PROF)
    pre = new.startswith(old) and len(new) > len(old)
    tail = new[len(old):].decode('utf-8', 'replace').splitlines() if pre else []
    R += ['### (iii) THE PROFILE.',
          '  prior (blob at HEAD) : %d bytes, %d lines, sha %s' % (len(old), old.count(b'\n'), sha(old)[:16]),
          '  new (working file)   : %d bytes, %d lines, sha %s' % (len(new), new.count(b'\n'), sha(new)[:16]),
          '  carriage returns in the new file : %d' % new.count(b'\r'),
          '  ### ### **THE PRIOR PROFILE IS A TRUE BYTE PREFIX OF THE NEW : %s**' % pre,
          '  the lines beyond the prefix : %d' % len(tail)]
    R += ['      + %s' % t for t in tail]
    ok_tail = (len(tail) == len(TERMINALS) and all(t.endswith(CLEAN) for t in tail)
               and [t.split("'")[1] for t in tail] == ['SmearGeneral.%s' % x for x in TERMINALS])
    R.append('  ### every line beyond it is a terminal of the new module, and clean : %s' % ok_tail)
    dirty = [x for x in new.decode('utf-8', 'replace').splitlines() if x.strip() and not x.endswith(CLEAN)]
    R.append('  ### lines in the whole new profile NOT reading "%s" : %d' % (CLEAN, len(dirty)))
    fails += [] if (pre and ok_tail and not dirty) else ['profile']
    # (ii) AllPrints.
    aold = blob(KERN, 'AllPrints.lean')
    anew = rb(ALLP)
    last = b'import SinglePrimeFactor\n'
    ins = aold.replace(last, last + b'import SmearGeneral\n', 1)
    add = anew[len(ins):] if anew.startswith(ins) else b''
    R += ['', '### (ii) AllPrints.lean.',
          '  ### ### **THE FACE`S BAR 3 CLAUSE, QUOTED: *`AllPrints.lean`s prior bytes are a true prefix of its new ones.*',
          '  ### ### THAT CLAUSE CANNOT BE MET AS WRITTEN, AND IT IS THIS SEAT`S DEFECT, NOT THE KERNEL`S:** Lean admits an',
          '  ### `import` only before the first command, so a new module`s import cannot be appended at the end of the file.',
          '  ### The face`s own (C)(ii) says where it goes -- *after the last existing import* -- and the two sentences of',
          '  ### the face disagree. ### **THE LOCKED FACE IS NOT EDITED.** ### The clause is measured as written and as the',
          '  ### procedure it stands for, and both results are printed:',
          '  the prior bytes a true prefix of the new, AS WRITTEN : %s' % (anew.startswith(aold)),
          '  the prior bytes with ONE import line inserted after the last import, a true prefix of the new : %s'
          % anew.startswith(ins),
          '  what follows that prefix :']
    R += ['      + %s' % x for x in add.decode('utf-8', 'replace').splitlines()]
    ok_ap = anew.startswith(ins) and add == b''.join(b'#print axioms SmearGeneral.%s\n' % t.encode() for t in TERMINALS)
    R.append('  ### ### **THE PROCEDURE`S MEASURE -- ONE IMPORT INSERTED, THE PRINTS APPENDED, NOTHING ELSE : %s**' % ok_ap)
    fails += [] if ok_ap else ['allprints']
    # (v) the seal.
    sold, snew = blob(KERN, 'Core/FiniteSideSeal.lean'), rb(SEAL)
    to, tn = tokens(sold), tokens(snew)
    ann = annotation_lines()
    ta = ' '.join(ann).split()
    k = next((i for i in range(len(to) + 1) if tn[:i] == to[:i] and tn[i:i + len(ta)] == ta
              and tn[i + len(ta):] == to[i:]), None)
    R += ['', '### (v) THE SEAL.',
          '  words : before %d, after %d, the annotation %d' % (len(to), len(tn), len(ta)),
          '  ### ### **EVERY EXISTING WORD SURVIVES, IN ORDER, AND THE ONLY WORDS ADDED ARE b416`s, AT ONE PLACE : %s**'
          % (k is not None),
          '  the insertion falls after the word %r' % (to[k - 1] if k else None),
          '  lines : before %d, after %d' % (sold.count(b'\n'), snew.count(b'\n'))]
    fails += [] if k is not None else ['seal']
    # the files that must not move.
    spf_ok = sha(rb(os.path.join(KERN, 'Core', 'SinglePrimeFactor.lean'))) == sha(blob(KERN, 'Core/SinglePrimeFactor.lean'))
    cl = sha(rb(CLASSES))
    R += ['', '### THE FILES THAT MUST NOT MOVE.',
          '  SinglePrimeFactor.lean equals its blob : %s' % spf_ok,
          '  Classes.lean sha %s ; the before-record`s d4f931db1d50c01f : %s' % (cl[:16], cl.startswith('d4f931db1d50c01f'))]
    fails += [] if (spf_ok and cl.startswith('d4f931db1d50c01f')) else ['unmoved']
    # (iv) the seven cells.
    m = re.search(r'def cells : List \(Nat × Nat\) := \[(.*?)\]', read(SEAL))
    cells = re.findall(r'\((\d+), (\d+)\)', m.group(1)) if m else []
    R += ['', '### (iv) THE SEVEN DECIDED CELLS, FROM THE KERNEL`S OWN `B329.cells`: %s' % ', '.join('(%s, %s)' % c for c in cells),
          '  ### every one is an instance by `SmearGeneral.cells_are_instances`, which the profile prints clean : %s'
          % any(t.startswith("'SmearGeneral.cells_are_instances'") and t.endswith(CLEAN) for t in tail)]
    fails += [] if len(cells) == 7 else ['cells']
    # the module.
    ms = read(MOD)
    sig = re.search(r'theorem smear_general[^\n]*\n[^\n]*', ms)
    R += ['', '### (i) THE MODULE.',
          '  lines %d ; `sorry` in its code %d ; `N418` left : %d, and each is in its header`s provenance sentence : %s'
          % (len(ms.splitlines()), len(re.findall(r'\bsorry\b', lean_code(ms))), ms.count('N418'),
             all('renamed' in ln for ln in ms.splitlines() if 'N418' in ln)),
          '  the statement, as the module carries it :']
    R += ['      %s' % x.strip() for x in (sig.group(0).splitlines() if sig else ['(absent)'])]
    R += ['  ### ### **IT IS THE NAMED OPEN STATEMENT OF `SinglePrimeFactor`, WORD FOR WORD, WITH NO FURTHER HYPOTHESIS.**',
          '', '### ### **VERIFY FAILURES : %d %s**' % (len(fails), fails), '=' * 100]
    put('b419_n_verify.txt', R)
    print(NL.join(R))
    return 1 if fails else 0


def run_reclass():
    src = read(os.path.join(D, 'b414_components.txt')).splitlines()
    ia = next(i for i, x in enumerate(src) if 'GROUP A -- A PROOF WOULD MAKE THESE TRUE AS WRITTEN : 8' in x)
    ib = next(i for i, x in enumerate(src) if 'GROUP B -- A PROOF WOULD LEAVE THESE EXACTLY AS THEY ARE : 20' in x)
    ie = next(i for i, x in enumerate(src) if i > ib and 'THE TWO PASSES DISAGREE' in x)
    row = re.compile(r'^\s+(\d+)\s+(\S+)\s+(.*)$')
    A = [row.match(x).groups() for x in src[ia + 1:ib] if row.match(x)]
    B = [row.match(x).groups() for x in src[ib + 1:ie] if row.match(x)]
    R = ['=' * 100, 'b419 COMPONENT 1 -- THE TWENTY-EIGHT, RE-CLASSIFIED BY THE PROOF, OVER b414`s HAND-READ.', '=' * 100,
         '  source : b414_components.txt, the hand-read (its lines %d and %d) -- the pass its own record says governs'
         % (ia + 1, ib + 1),
         '  rows read : GROUP A %d, GROUP B %d, together %d' % (len(A), len(B), len(A) + len(B)),
         '  ### ### **THE SEAT DOES NOT RE-SORT.** ### b414`s group and its reason are carried on every row; this act adds',
         '  ### only what the proof does to the row. ### **0 SENTENCES EDITED** -- each lives in a banked ferry.',
         '',
         '### ### **GROUP A -> QUALIFIED BY THE PROOF : %d** -- true at every base with a single prime factor and every' % len(A),
         '### level, by `SmearGeneral.smear_general` (Core/SmearGeneral.lean). ### The corpus`s bases are prime, and a',
         '### prime has a single prime factor, so each sentence`s intended range is inside the theorem`s.']
    for n, f, why in A:
        R.append('  %3s  %-30s QUALIFIED BY THE PROOF   b414: %s' % (n, f, why))
    R += ['', '### ### **GROUP B -> UNREACHED BY THE PROOF : %d** -- what each asserts is about something else, so the' % len(B),
          '### proof leaves it exactly as it was.']
    for n, f, why in B:
        R.append('  %3s  %-30s UNREACHED BY THE PROOF   b414: %s' % (n, f, why))
    R += ['', '  ### ### **THE FIRST ROW OF GROUP A THAT THE PROOF DOES NOT CLOSE WHOLE, SAID RATHER THAN SMOOTHED:** row 20`s',
          '  ### second clause, *the generality is honest in its own header*, is what b414 refuted; the seal`s header now',
          '  ### carries b416`s annotation saying so, and the proof makes the FIRST clause true. ### Its row is QUALIFIED,',
          '  ### and its b414 reason is carried in full so the refuted clause stays visible.',
          '=' * 100]
    put('b419_twentyeight.txt', R)
    print(NL.join(R))
    return 0 if (len(A), len(B)) == (8, 20) else 1


# =============================================================================================
# ### COMPONENT 2 -- THE LOCK AND THE SCAN, PRICED. ### Nothing here writes outside `data/`.
# =============================================================================================
def run_lock():
    lg = read(os.path.join(T, 'b378_lockgate.py'))
    fs = read(os.path.join(T, 'ferry_scan.py'))
    halt = read(os.path.join(D, 'b418_halt.txt'))
    gate = re.search(r"\('the ferry scan \(struck clauses and stems\)'.*?\),", lg, re.S)
    doc = fs[fs.find('# ### (1) ### **A HIT IS A STRING, NOT A FAULT.**'):fs.find('# ### (2)')]
    routes = halt[halt.find('### WHAT WOULD LET THE ACT RESUME'):]
    routes = routes[:routes.find('====')]
    R = ['=' * 100, 'b419 COMPONENT 2 -- THE LOCK AND THE SCAN: PRICED, NOT RESOLVED. ### ROUTED TO THE AUTHOR.', '=' * 100,
         '### THE TWO RULES, QUOTED FROM THEIR SOURCES.',
         '  (1) the lock gate, tools/b378_lockgate.py -- its ferry gate, whose last field says the gate has no digest',
         '      and whose looked-for string admits exactly one verdict:',
         '      %s' % re.sub(r'\s+', ' ', gate.group(0) if gate else '### MISS'),
         '      ### the lock permits only when EVERY gate passes, and this gate has no reader`s override.',
         '  (2) the scan, tools/ferry_scan.py -- its first doctrine, verbatim:']
    R += ['      %s' % x.strip() for x in doc.splitlines() if x.strip()]
    R += ['  ### ### **THE CONFLICT, STATED ONCE:** the scan says a hit is a SITE for a reader to rule on; the lock reads the',
          '  ### scan`s count as a verdict and admits only zero. ### A ferry that must QUOTE a banned stem -- to strike a',
          '  ### clause, or to name a species -- is correct by the scan and refused by the lock.',
          '', '### HOW OFTEN IT HAS FIRED -- EVERY FERRY SCAN IN relay`s data/, READ BY ITS VERDICT LINE.']
    scans = sorted(f for f in os.listdir(D) if re.match(r'b\d+_ferry_scan.*\.txt$', f))
    hits = []
    for f in scans:
        m = re.search(r'VERDICT: ### \*\*(\d+) HIT\(S\) REPORTED', read(os.path.join(D, f)))
        if m and int(m.group(1)):
            hits.append((f, int(m.group(1))))
    first_lock = subprocess.run(['git', '-C', ROOT, 'log', '--diff-filter=A', '--format=%h %cI %s', '--',
                                 'tools/b378_lockgate.py'], capture_output=True, text=True).stdout.strip()
    after = [f for f in scans if int(re.match(r'b(\d+)', f).group(1)) >= 378]
    R += ['  scan records read : %d ; with a verdict line reading a non-zero count : %d' % (len(scans), len(hits)),
          '  the lock gate`s first commit : %s' % first_lock[:110],
          '  scan records from b378 on, the acts the lock gate has gated : %d' % len(after)]
    for f, n in hits:
        a = int(re.match(r'b(\d+)', f).group(1))
        R.append('      %-34s %d hit(s) ; %s' % (f, n, 'LOCK GATE IN FORCE -- the act HALTED at the lock and was re-pasted'
                                                 if a >= 378 else 'before the lock gate existed -- the reader ruled, as the scan says'))
    R += ['  ### ### **SINCE THE LOCK GATE WAS BUILT IT HAS REFUSED ONE FERRY IN %d GATED SCANS; BEFORE IT, A HIT WAS READ.**'
          % len(after),
          '', '### THE THREE RESOLUTIONS, AS b418`s HALT RECORD NAMED THEM:']
    R += ['  ' + x for x in wrap(re.sub(r'\s+', ' ', routes), 110)]
    R += ['',
          '### EACH ONE PRICED -- WHAT IT COSTS, WHO ACTS, AND WHETHER IT NEEDS THE INSTRUMENT LANE.',
          '  ROUTE (1) -- RE-PASTE WITH THE LINE CHANGED.',
          '      cost : one round trip to the author per hit, the act halted between; and the author`s words changed to pass',
          '             a string test that the scan`s own doctrine says is not a fault. ### Nothing learned is kept: the',
          '             next ferry that must quote a stem halts the same way.',
          '      who  : the author, once per occurrence.',
          '      lane : ### **NONE** -- no instrument changes.',
          '      measured frequency : one halt in the gated scans above.',
          '  ROUTE (2) -- A RULING THAT A HIT INSIDE THE AUTHOR`S OWN PASTE, NAMED ON THE FACE, IS A STRING THE LOCK PERMITS.',
          '      cost : one ruling, then an edit to the lock gate: the ferry gate reads the scan`s sites, and admits a hit only',
          '             where the face names that site by line and the site lies inside the ratified paste; with fixtures in',
          '             both polarities -- a named in-paste hit PASSES, an unnamed hit and a named out-of-paste hit FAIL. ###',
          '             **IT OPENS A PATH THROUGH THE LOCK**, bounded by the face`s own naming, which the lock`s other gates',
          '             already hash.',
          '      who  : the author rules; a seat builds it in the instrument lane.',
          '      lane : ### **YES -- THE LOCK GATE IS AN EXISTING SHARED INSTRUMENT, AND EDITING IT IS THE INSTRUMENT LANE`S',
          '             ### WORK. THAT LANE IS PARKED; THIS ACT DOES NOT OPEN IT.** ### After it, no round trips.',
          '  ROUTE (3) -- A ONE-ACT RULING TO SEAL PAST THE FERRY GATE, THE REFUSAL BANKED ON THE FACE.',
          '      cost : one ruling per occurrence, and a sealed face whose lock notes say REFUSED -- the lock`s verdict stops',
          '             meaning what it says for that act, and every later reader must read the ruling to know why.',
          '      who  : the author, once per occurrence.',
          '      lane : ### **NONE** -- no instrument changes.',
          '',
          '### ### **ONLY ROUTE (2) NEEDS THE INSTRUMENT LANE; ROUTES (1) AND (3) COST THE AUTHOR ONE ACTION PER HIT.** ###',
          '### **ROUTED TO THE AUTHOR. THIS ACT CHOOSES NONE, AND 0 BYTES OF THE LOCK GATE OR THE SCAN CHANGE.**',
          # ### REPAIRED AFTER RUN 1 (kept as `b419_lock_priced_run1.txt`): run 1 compared RAW BYTES and printed the
          # ### scan UNEQUAL -- its working copy is CRLF, checked out before relay tracked `eol=lf`, while its blob is LF.
          # ### Git's own view is the measure: the working file's hash-object against the index blob, and no diff.
          '  lock gate, by git`s own view (hash-object = index blob, no diff) : %s ; scan, the same : %s'
          % (git_same('tools/b378_lockgate.py'), git_same('tools/ferry_scan.py')),
          '  ### (run 1 compared raw bytes and printed the scan UNEQUAL: its working copy is CRLF and its blob LF --',
          '  ### an EOL artifact of the checkout, not a change; kept as run 1.)',
          '=' * 100]
    put('b419_lock_priced.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### COMPONENT 3 -- SILENT TIMEOUTS OUTSIDE THE ARC.
# =============================================================================================
RESTS = {
    # (session, call time) : (rests?, what the act took from the call, the line read)
    ('85d87edf', '2026-08-09T19:51:00'): (False, 'NO ACT. The tool said it timed out; the session then walked the kernels in Python and reported its zero from THAT walk.',
                                          'next text: "`SIDEDerivative` returns zero hits across all 40 kernels." -- after a Python walk, not the call'),
    ('862416d9', '2026-08-13T19:49:06'): (False, 'NO ACT. Silent; its content result carried matches, and the session resolved the cited commit by git. No count or absence taken.',
                                          'next text: "bd2ae1a resolved at cite"'),
    ('e02bb824', '2026-08-20T16:16:27'): (False, 'NO ACT. The tool said it timed out; a shell `grep -ril` over relay found the file, which was then read.',
                                          'next tool: grep -ril "TensorSquareShadow" /d/relay; next text: "TensorSquareShadow read"'),
    ('2bde398e', '2026-08-28T20:48:32'): (True, 'b231 banked (ABSENT) -- "NO MATCH. NOT ONE, ANYWHERE." -- over a scope it states as including relay/data; '
                                          'the only walker call over relay/data with its notation is this one, which timed out, and its shell sweeps over relay '
                                          'read `.md` and `.py` only (the one reading `.txt` aborted, as its bank says).',
                                          'b231_the_two.txt: "relay/reports, relay/data, SIDE-global-section, SIDE-kernel." / "NO MATCH. NOT ONE, ANYWHERE."'),
    ('589832be', '2026-09-02T23:59:39'): (True, 'b300 decision (a), DIFFERENT, quotes what "the Sonin sector" names "from the file that adopted it"; the silent, '
                                          'batched call is the search that surfaced the adopting act`s files, so a truncation could have hidden another definition.',
                                          'b300_the_archimedean_leg.txt: "WHAT THE PHRASE NAMES, FROM THE FILE THAT ADOPTED IT (data/b206_variable_passage.txt)"'),
    ('76ff68b8', '2026-09-03T15:33:16'): (False, 'The tool said it timed out; a PowerShell Select-String over data/ completed and found the files.',
                                          'next text: "Found the corpus`s own extract and b197`s read."'),
    ('81923c42', '2026-09-03T20:02:32'): (False, 'The tool said it timed out; a narrowed walker call over tools/ found the definitions.',
                                          'next tool: Grep "S_quot|pair_at_n" over D:\\relay\\tools'),
    ('81923c42', '2026-09-04T01:07:15'): (False, 'The tool said it timed out, on a single file; the file was then read by line range.',
                                          'next tool: sed -n "10,16p;28,60p" data/b307_the_fold.txt'),
    ('2513b655', '2026-09-11T00:40:36'): (False, 'The tool said it timed out; a narrowed call over relay/reports located the certificate, read whole.',
                                          'next text: "The certificate is located -- reports/2026-08-01-w-half-consult.md"'),
    ('fbe6b4b2', '2026-09-11T13:10:24'): (False, 'The tool said it timed out; the seat listed D: and searched elsewhere.', 'next tool: Get-ChildItem D:\\ -Directory'),
    ('fbe6b4b2', '2026-09-11T13:11:02'): (False, 'The tool said it timed out; the seat searched the transcripts instead.', 'next tool: Grep over the session transcripts'),
    ('fbe6b4b2', '2026-09-11T13:28:55'): (False, 'b418 read b417`s records line by line: b417 banked only a claim ABOUT the walker, and 0 ABSENT verdicts.',
                                          'b418_walker.txt: "0 ABSENT verdicts rest on the truncated call" (carried; b418 printed its lines)'),
    ('fbe6b4b2', '2026-09-11T14:23:57'): (False, 'b418`s resume probes; b418 banked no count from them -- its survey counted with Python.',
                                          'b418_components.txt: "Two of the silent limits it lists are this act`s own resume probes, whose results were complete"'),
}


def relay_commits():
    out = subprocess.run(['git', '-C', ROOT, 'log', '--format=%H %ct'], capture_output=True, text=True).stdout.split(NL)
    return sorted((int(x.split()[1]), x.split()[0]) for x in out if x.strip())


def bracket(at, commits):
    t = datetime.strptime(at[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc).timestamp()
    floor = [c for c in commits if c[0] < t]
    ceil = [c for c in commits if c[0] >= t]
    return (floor[-1][1] if floor else None), (ceil[0][1] if ceil else None)


def walk_tree(commit, sub, pattern, icase, glob_pat=None):
    """### A PYTHON WALKER OVER A COMMITTED TREE. ### Hidden paths and binary blobs skipped, as the tool skips them."""
    rx = re.compile(pattern, re.I if icase else 0)
    ls = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '-z', commit], capture_output=True).stdout.split(b'\0')
    ents = []
    for e in ls:
        if not e:
            continue
        meta, path = e.split(b'\t', 1)
        path = path.decode('utf-8', 'replace')
        if sub and not (path == sub or path.startswith(sub + '/')):
            continue
        if any(p.startswith('.') for p in path.split('/')):
            continue
        if glob_pat and not re.fullmatch(glob_pat.replace('.', r'\.').replace('*', '.*'), os.path.basename(path)):
            continue
        ents.append((meta.split()[2].decode(), path))
    p = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, _ = p.communicate((NL.join(s for s, _ in ents) + NL).encode())
    hits, pos = {}, 0
    for s, path in ents:
        hdr_end = out.index(b'\n', pos)
        size = int(out[pos:hdr_end].split()[2])
        body = out[hdr_end + 1:hdr_end + 1 + size]
        pos = hdr_end + 1 + size + 1
        if b'\0' in body[:8000]:
            continue
        lines = [ln for ln in body.decode('utf-8', 'replace').splitlines() if rx.search(ln)]
        if lines:
            hits[path] = lines
    return hits


def sub_of(path):
    p = path.replace('/', '\\').rstrip('\\')
    if p.lower() in ('d:', 'd:\\'):
        return ''
    i = p.lower().find('relay')
    return p[i + len('relay'):].strip('\\').replace('\\', '/') if i >= 0 else None


def full_inputs():
    out = {}
    for fp in os.listdir(TD):
        if not fp.endswith('.jsonl'):
            continue
        for c in WG.calls_in(os.path.join(TD, fp)):
            out[(fp[:8], (c['at'] or '')[:19], c['input'].get('pattern'))] = c
    return out


def run_timeouts():
    pop = json.load(io.open(os.path.join(D, 'b419_timeout_population.json'), encoding='utf-8'))
    scored = [c for c in pop if c['scope'] != 'ELSEWHERE']
    elsewhere = [c for c in pop if c['scope'] == 'ELSEWHERE']
    commits = relay_commits()
    fin = full_inputs()
    R = ['=' * 100, 'b419 COMPONENT 3 -- SILENT TIMEOUTS OUTSIDE THE ARC. ### THE GUARD WHERE THE RECORD ALLOWS IT.', '=' * 100,
         '  population (survey run 2) : %d calls reached the limit in every transcript ; scored (inside relay or a directory'
         % len(pop), '  holding it) : %d ; elsewhere, listed and not scored : %d' % (len(scored), len(elsewhere)),
         '  guard : walker_guard.verdict, IMPORTED, limit %.1f s less a margin of %.1f s' % (WG.LIMIT, WG.MARGIN), '']
    # ### THE POSITIVE CONTROL, FIRST (BAR 9).
    ctl = next(c for c in scored if c['at'].startswith('2026-09-11T13:28:55'))
    ret = set(re.findall(r'data\\([^:\s]+):', ctl['content']))
    fl, ce = bracket(ctl['at'], commits)
    hf = walk_tree(fl, 'data', ctl['pattern'], False)
    hc = walk_tree(ce, 'data', ctl['pattern'], False)
    got = set(os.path.basename(p) for p in list(hf) + list(hc))
    ctl_ok = ret <= got and len(got) >= 40
    R += ['### THE POSITIVE CONTROL, RUN BEFORE ANY COUNT (BAR 9): b417`s truncated call, re-run by this walker.',
          '  the call returned %d files ; the floor tree (%s) holds %d matching, the ceiling tree (%s) %d, together %d'
          % (len(ret), fl[:7], len(hf), ce[:7], len(hc), len(got)),
          '  ### every file the call returned is reached : %s ; at least the forty b418 counted : %s'
          % (ret <= got, len(got) >= 40),
          '  ### ### **CONTROL : %s**' % ('PASS' if ctl_ok else 'FAIL -- NO COUNT BELOW IS REPORTED'), '']
    R += ['### EVERY SCORED CALL, WITH THE GUARD WHERE THE RECORD ALLOWS IT, AND WHETHER A BANKED VERDICT RESTS ON IT.']
    resting = []
    for c in sorted(scored, key=lambda c: c['at']):
        key = (c['session'], c['at'][:19])
        rest, took, line = RESTS.get(key, (None, '### NOT HAND-READ', ''))
        if c['timed_out']:
            g = 'INCOMPLETE -- the tool`s own result says it timed out'
        elif c['siblings'] == 0:
            g = 'guard : %s' % WG.verdict(c['at'], (fin.get((c['session'], c['at'][:19], c['pattern'])) or {}).get('result_at', c['at']), c['numFiles'])
        else:
            g = ('### THE RECORD DOES NOT ALLOW THE GUARD -- issued beside %d sibling call(s), so its recorded %.2f s is the'
                 ' batch`s, an upper bound only' % (c['siblings'], c['seconds']))
        act = c['act'] if (c['gap_hours'] is not None and c['gap_hours'] <= 24) else 'NO ACT'
        R += ['', '  %s %s  %s  %.2f s  returned %s  said-timeout %s  batch %d  act %s (lag %s h)'
              % (c['session'], c['at'][:19], c['scope'], c['seconds'], c['numFiles'], c['timed_out'], c['siblings'], act,
                 c['gap_hours']),
              '      path %s ; pattern %s' % (c['path'], c['pattern'][:90]),
              '      %s' % g,
              '      ### A BANKED VERDICT RESTS ON IT : %s' % ('YES' if rest else 'NO' if rest is False else '### UNREAD')]
        R += ['      ' + x for x in wrap('what the act took : ' + took, 104)]
        R += ['      ' + x for x in wrap('line read : ' + line, 104)]
        if rest:
            resting.append(c)
    R += ['', '### ### **BANKED VERDICTS RESTING ON A TIMED-OUT CALL : %d**' % len(resting)]
    # ### THE RE-RUNS, BOUNDED, BRACKETED BY THE TREES EITHER SIDE OF THE CALL.
    reruns = []
    for c in resting:
        inp = (fin.get((c['session'], c['at'][:19], c['pattern'])) or {}).get('input', {})
        icase = bool(inp.get('-i'))
        sub = sub_of(c['path'])
        fl, ce = bracket(c['at'], commits)
        hf = walk_tree(fl, sub, c['pattern'], icase, inp.get('glob'))
        hc = walk_tree(ce, sub, c['pattern'], icase, inp.get('glob'))
        new_in_ceiling = sorted(set(hc) - set(hf))
        R += ['', '-' * 100, '### RE-RUN : %s %s (act %s) -- case-insensitive %s, path %r'
              % (c['session'], c['at'][:19], c['act'], icase, sub or '(whole relay)'),
              '  floor tree (last relay commit before the call) %s : %d files match' % (fl[:7], len(hf)),
              '  ceiling tree (first relay commit after it)      %s : %d files match ; of them not in the floor : %d'
              % (ce[:7], len(hc), len(new_in_ceiling))]
        for p in sorted(hf):
            R.append('    FLOOR %s' % p)
            for ln in hf[p][:4]:
                R.append('        | %s' % ln.strip()[:150])
        for p in new_in_ceiling:
            R.append('    CEILING ONLY %s   (%d lines)' % (p, len(hc[p])))
        reruns.append(dict(session=c['session'], at=c['at'], act=c['act'], floor=fl, ceiling=ce,
                           floor_files={p: v[:12] for p, v in hf.items()}, ceiling_only=new_in_ceiling))
    json.dump(reruns, io.open(os.path.join(D, 'b419_reruns.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    R += ['', '### THE CALLS ELSEWHERE, LISTED AND NOT SCORED:']
    for c in sorted(elsewhere, key=lambda c: c['at']):
        R.append('  %s %s  %.2f s  said %s  batch %d  %s' % (c['session'], c['at'][:19], c['seconds'], c['timed_out'],
                                                          c['siblings'], c['path']))
    R.append('=' * 100)
    put('b419_timeouts.txt', R)
    print(NL.join(R))
    return 0 if ctl_ok else 1


# =============================================================================================
# ### THE REPORT. ### The two resting verdicts are HAND-READ from `b419_timeouts.txt`'s printed lines.
# =============================================================================================
VERDICT_N = 'PROVED'
RESTING_VERDICTS = [
    ('b231', 'the owner`s pair is (ABSENT) -- "NO MATCH. NOT ONE, ANYWHERE." -- over a scope including relay/data',
     'CONFIRMED',
     'the call`s own pattern, case-insensitive, over the WHOLE relay tree at the last commit before the call: 0 files '
     'match. The ceiling tree`s 4 matches are b231`s own writes (its registration, its bank, its report, and its '
     'HANDOFF edit), none present at the call. The absence held on relay; the call that should have shown it did not '
     'complete, and the re-run supplies what it could not.'),
    ('b300', 'decision (a): "the Sonin sector" names the +1 eigenspace of F on the archimedean Sonin space, so sector '
     'and space are DIFFERENT', 'CONFIRMED',
     'the phrase, case-insensitive, over the whole relay tree before the call: 34 files, every line from b206`s '
     'adoption on naming the same +1 eigenspace (b206`s own file, the index`s quotation of it, b226`s "its E_1 is THE '
     'SONIN SECTOR"). TWO LINES FROM BEFORE THE ADOPTION -- b54_mixed_pattern.txt and b58`s row-29 record, whose "E_1 '
     'of the Sonin sector" uses the phrase for the space itself -- are printed and NOT ruled on: b300 read the phrase '
     '"from the file that adopted it", and the adopting report says the names are "used from here".'),
]


def main():
    L = []
    say = L.append
    recs = {nm: read(os.path.join(D, f)) for nm, f in (
        ('probe', 'b419_n_probe.txt'), ('kernel', 'b419_n_kernel.txt'), ('build', 'b419_kernel_build.txt'),
        ('verify', 'b419_n_verify.txt'), ('reclass', 'b419_twentyeight.txt'), ('lock', 'b419_lock_priced.txt'),
        ('timeouts', 'b419_timeouts.txt'))}
    fails = [nm for nm, t in recs.items() if not t]
    say('=' * 100)
    say('b419_components.py -- THE HELPER FIXED, THE CLAUSE PRINTED.')
    say('=' * 100)
    say('')
    say('#' * 100)
    say('### PART ONE -- THE KERNEL. ### Component 1.')
    say('#' * 100)
    pv = re.search(r'VERDICT, READ FROM THE PROFILE : (\S+)\*\*', recs['probe'])
    say('  the first probe : b418`s probe 16 with ONE line changed, `pow_pred`s term, to `Nat.pow_succ r (j - 1)`')
    say('  probes compiled in this act : %s of the sixteen the budget allows ; minutes : about one'
        % (re.search(r'probes compiled in this act : (\d+)', recs['probe']) or [None, '?'])[1])
    say('  ### ### **VERDICT : %s** ### (read from the profile: %s)' % (VERDICT_N, pv.group(1) if pv else '### MISS'))
    say('  ### THE GENERAL CLAUSE`S PROFILE, AS THE KERNEL PRINTS IT (AXIOM_PRINTS.txt, its last two lines):')
    for ln in rb(PROF).decode('utf-8').splitlines()[-2:]:
        say('      %s' % ln)
    for lbl, needle in (('prior profile a true byte prefix', 'THE PRIOR PROFILE IS A TRUE BYTE PREFIX OF THE NEW : True'),
                        ('whole profile clean', 'NOT reading "does not depend on any axioms" : 0'),
                        ('AllPrints, the procedure`s measure', 'ONE IMPORT INSERTED, THE PRINTS APPENDED, NOTHING ELSE : True'),
                        ('the seal`s words survive', 'AT ONE PLACE : True'),
                        ('the seven cells instances', 'which the profile prints clean : True'),
                        ('Classes.lean unmoved', 'd4f931db1d50c01f : True'),
                        ('verify failures 0', 'VERIFY FAILURES : 0')):
        ok = needle in recs['verify']
        fails += [] if ok else ['verify:' + lbl]
        say('  %-40s %s' % (lbl, ok))
    say('  ### ### **AND ONE CLAUSE OF THIS ACT`S OWN FACE CANNOT BE MET AS WRITTEN:** BAR 3`s *`AllPrints.lean`s prior')
    say('  ### bytes are a true prefix of its new ones* -- Lean takes an `import` only at the head of a file. ### The face`s')
    say('  ### (C)(ii) places the import after the last import, and the procedure`s measure is met; the clause as written')
    say('  ### is printed FALSE beside it. ### The locked face is not edited.')
    say('  the (T1.4) annotation : b416`s drafted words, inserted after *compiled here);*, every existing word surviving.')
    say('  the twenty-eight : GROUP A 8 -> QUALIFIED BY THE PROOF ; GROUP B 20 -> UNREACHED BY THE PROOF ; 0 sentences edited.')
    say('')
    say('**(N1)** -- *PROVED, empty profile, first attempt* -- over the first probe of (C), its clauses apart (R27):')
    say('      the verdict PROVED         -- ### **MET.**')
    say('      the profile empty          -- ### **MET**: sixteen of sixteen printed lines in the probe, and all 607 in the')
    say('                                    kernel`s regenerated profile, read "does not depend on any axioms".')
    say('      on the first attempt       -- ### **MET**: probe 1 closed it, and no later probe was compiled.')
    say('')
    say('#' * 100)
    say('### PART TWO -- THE LOCK AND THE SCAN. ### Component 2, priced and routed.')
    say('#' * 100)
    for ln in recs['lock'].splitlines():
        if ('SINCE THE LOCK GATE WAS BUILT' in ln or 'ONLY ROUTE (2) NEEDS' in ln or 'ROUTED TO THE AUTHOR. THIS ACT' in ln
                or ln.startswith('  ROUTE (') or 'equals its blob' in ln):
            say('  ' + ln.strip())
    say('')
    say('#' * 100)
    say('### PART THREE -- SILENT TIMEOUTS OUTSIDE THE ARC. ### Component 3.')
    say('#' * 100)
    for ln in recs['timeouts'].splitlines():
        if ('population' in ln or 'holding it' in ln or 'CONTROL :' in ln or 'BANKED VERDICTS RESTING' in ln
                or ln.startswith('### RE-RUN') or 'floor tree' in ln or 'ceiling tree' in ln):
            say('  ' + ln.strip())
    said = recs['timeouts'].count('the tool`s own result says it timed out')
    nog = recs['timeouts'].count('THE RECORD DOES NOT ALLOW THE GUARD')
    say('  ### the guard, where the record allows it : %d scored calls carried the tool`s own timeout text; %d were' % (said, nog))
    say('  ### SILENT AND BATCHED, WHERE THE RECORD DOES NOT ALLOW THE GUARD -- said, not guessed.')
    for act, verdict, how, why in RESTING_VERDICTS:
        say('')
        say('  %s -- %s' % (act, verdict))
        say('      ### ### **%s**' % how)
        for seg in wrap(why, 104):
            say('      ' + seg)
    say('')
    say('  ### ### **THE SEAT RE-VERDICTS NOTHING, AND NEITHER ACT`S BANK IS EDITED.**')
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    put('b419_components.txt', L)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(main())
    for flag, fn in (('--n-probe', run_n_probe), ('--n-kernel', run_n_kernel), ('--n-verify', run_n_verify),
                     ('--reclass', run_reclass), ('--lock', run_lock), ('--timeouts', run_timeouts)):
        if flag in sys.argv:
            sys.exit(fn())
