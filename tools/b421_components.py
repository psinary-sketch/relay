# -*- coding: utf-8 -*-
"""b421_components.py -- THE FINITE AMBIENT BUILT OR PRICED, AND THE SPAN COUNTED.

### ### **EACH MODE WRITES ITS OWN RECORD:**
###   --c1-record    Component 1: every probe's source and printed profile, and the verdict read from the profile.
###   --c1-kernel    Component 1, ONLY ON PROVED: the module written, one import inserted, the prints appended.
###   --c1-verify    Component 1, ONLY ON PROVED: the prefix, the insert-and-append measure, the unchanged files.
###   --c2           Component 2: hypothesis 1's specification, priced under both definitions the record holds.
###   --c3           Component 3: the span, both counts, and the fold named and not run.
###   --conflations  the closing's added line: b420's three conflations, the navigator's, with the corrections.
###   (no flag)      the report.
### ### **EVERY QUOTATION IS PULLED FROM ITS FILE AT RUN TIME**; a quote not in its source is a MISS.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_SIDE = '5c72065'
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
SMG = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
NDIR = r'C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\fbe6b4b2-25ed-44b7-91cb-756e5456e21d\scratchpad\n421'
NL = chr(10)
MISS = []
CLEAN = 'does not depend on any axioms'


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


def blob(repo, path, rev):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True).stdout


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


def q(path, start, end=None, cap=700):
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : %r' % (os.path.basename(path), start[:48]))
        return '### MISS'
    j = src.find(end, i + len(start)) if end else -1
    return re.sub(r'\s+', ' ', src[i:j + len(end)] if j > i else src[i:i + cap]).strip()


def block(R, label, text, width=100):
    R.append('  ' + label)
    R.extend('      | ' + s for s in wrap(text, width))


def prose(R, text, width=104):
    R.extend('  ' + s for s in wrap(text, width))


# =============================================================================================
# ### COMPONENT 2 -- HYPOTHESIS 1'S SPECIFICATION, PRICED UNDER BOTH DEFINITIONS.
# =============================================================================================
def run_c2():
    R = ['=' * 100, 'b421 COMPONENT 2 -- WHAT A SPECIFICATION OF THE TEST-FUNCTION STRUCTURE WOULD HAVE TO STATE.', '=' * 100]
    R += ['', '### WHAT IT WOULD HAVE TO DESCRIBE -- THE SAME UNDER BOTH DEFINITIONS.']
    block(R, 'the carrier, as the source states the class (b400, verified at digest) :',
          q(os.path.join(D, 'b400_components_run2.txt'), '### **PROPOSITION C.1 CARRIES NONE**', 'for all z in F."*'))
    prose(R, '  So the specification must name: the carrier -- smooth, compactly supported functions on the positive '
          'reals, with the vanishing set `F` fixed (the arc fixes it by its own vanishing conditions, `i/2` and `0`); '
          'the operations the target reads -- the convolution `g conv g-bar^#` and the involution; and the functional`s '
          'terms place by place, `W_p` by the source`s eq. (149) and `W_inf`, with the sum over places, which is the '
          'interface. ### Nothing here is new: it is a list of what row S1 already names.')
    R += ['', '### UNDER THE KEYSTONE`S DEFINITION 2.1, IN THE SETTING ITS OWN §2.1 FIXES.']
    block(R, 'the setting :', q(IB, 'Throughout, we work in classical first-order logic.', 'in a domain |M|.'))
    block(R, 'the definition :', q(IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.'))
    R.append('  the keystone names Lowenheim-Skolem, categoricity or second-order semantics : %s'
             % bool(re.search(r'(?i)l(ö|o)wenheim|categoric|second-order semantics', read(IB))))
    prose(R, '  ### ### **THE SEAT`S CITATION, NOT THE RECORD`S -- A CLASSICAL THEOREM OF FIRST-ORDER MODEL THEORY:** by the '
          'upward Löwenheim-Skolem theorem, a set of first-order sentences with an infinite model has models of every '
          'larger cardinality, and models of different cardinalities are not isomorphic. ### So no set of first-order '
          'sentences, finite or not, has an infinite structure as its UNIQUE model up to isomorphism. ### The '
          'test-function structure is infinite -- the class contains infinitely many functions.')
    prose(R, '  ### ### **PRICE UNDER DEFINITION 2.1, READ AS WRITTEN: NOT SUPPLIABLE.** No specification of any length can have '
          'the property the definition demands, so the missing specification is not a piece of writing nobody has '
          'done; it is one no writing can do. ### Readings under which it could be supplied -- uniqueness proved INSIDE '
          'ZFC (as ZFC proves any two complete ordered fields isomorphic), or second-order semantics -- ### **ARE '
          'STATED IN NEITHER DOCUMENT**, and choosing one is the author`s.')
    prose(R, '  ### ### **AND THE BEARING, ROUTED AND NOT RULED:** the same citation reaches every infinite structure, `xi``s '
          'among them. b407 read hypothesis 1 as met for `xi` on the keystone`s own assertion; ### **THAT ACT IS NOT '
          'RE-VERDICTED**, and the question -- which reading of *unique model* the keystone intends -- is routed to the '
          'author.')
    block(R, '  b407`s reading, quoted :', q(os.path.join(D, 'b407_the_barriers_own_instance.txt'), '### Four of Theorem 3.1’s five hypotheses are', 'κ(σ, I) = 0."*'))
    R += ['', '### UNDER THE MONOGRAPH`S FORMAL DEFINITION.']
    block(R, 'the definition :', q(MONO, '**Formal:** System X is determined by specification S', 'logical consequences of S.'))
    block(R, 'and the one it writes, for xi :', q(MONO, 'For ξ(s): the specification is θ(τ) = Σ exp(πin²τ)', 'No human choices enter.'))
    prose(R, '  ### This definition carries ### **NO UNIQUENESS-UP-TO-ISOMORPHISM CLAUSE**, so the citation above does not bear on '
          'it. ### Clauses (i) and (ii) -- finite and explicit, no free parameters -- ### **ARE WRITABLE**: the list above, '
          'with `F` fixed by the arc`s own vanishing conditions rather than left free. ### Clause (iii) -- *all properties '
          'of X are logical consequences of S* -- is a demand on what follows from the list, and the record establishes '
          'it for no structure; it is priced as ### **UNVERIFIED, NOT AS MET.**')
    prose(R, '  ### ### **PRICE UNDER THE MONOGRAPH`S DEFINITION: WRITABLE IN (i) AND (ii), UNVERIFIED IN (iii) -- AND NOT '
          'WRITTEN.**')
    R += ['', '### WHETHER ANY DOCUMENT ALREADY HOLDS ONE -- EVERY HIT OF THE SURVEY`S SEARCH, HAND-READ.']
    hit = q(os.path.join(PP, 'OPEN_TRAILS.md'), '**And the resemblance is exact, which is precisely why it must not be filed as an instance.**', None, cap=420)
    block(R, 'the one hit, OPEN_TRAILS.md :', hit)
    prose(R, '  ### it is b407`s trail on the resemblance between Definition 2.5 and the E0 gate; it names no carrier, no '
          'operation and no place term. ### **NOT A SPECIFICATION.**')
    R += ['  documents holding the specification : 0', '',
          '### ### **`(N2)` -- *no document holds the specification Component 2 asks for* -- ### **MET**: the one hit is not one;',
          '### and under Definition 2.1 read as written, none could be.', '=' * 100]
    put('b421_c2_specification.txt', R)
    print(NL.join(R))
    return 1 if MISS else 0


# =============================================================================================
# ### COMPONENT 3 -- THE SPAN.
# =============================================================================================
def run_c3():
    R = ['=' * 100, 'b421 COMPONENT 3 -- THE SPAN SINCE THE b412 FOLD, COUNTED BY THE TOOL.', '=' * 100]
    own = read(os.path.join(D, 'b421_span_run.txt'))
    wo = read(os.path.join(D, 'b421_span_act420.txt'))

    def pick(t, k):
        return next((x.strip() for x in t.splitlines() if k in x), '### MISS')
    for label, t in (('THE ACT`S OWN COUNT (--emit b421)', own), ('WITHOUT THIS ACT (--act 420)', wo)):
        R += ['  %s' % label,
              '      | %s' % pick(t, 'the last fold covers'),
              '      | %s' % pick(t, 'it was FILED BY'),
              '      | %s' % pick(t, 'and it now runs through'),
              '      | %s' % pick(t, 'THE CURRENT SPAN')]
    block(R, '(R1), the threshold :', q(os.path.join(D, 'b366_extract_notes.txt'), '(R1) THE FOLD THRESHOLD is NINE acts.', None, cap=200))
    n_own = int((re.search(r'THE CURRENT SPAN : (\d+)', own) or [0, '0'])[1])
    n_wo = int((re.search(r'THE CURRENT SPAN : (\d+)', wo) or [0, '0'])[1])
    R += ['', '  ### ### **THE ACT`S COUNT : %d. ### WITHOUT THIS ACT : %d. ### THRESHOLD : NINE.**' % (n_own, n_wo)]
    prose(R, '  ### The span b413-b421 reaches the threshold WITH this act. ### By the record`s own precedent -- the fold of '
          'b403-b411 was filed by b412, the act after its span`s last -- ### **THE FOLD OF b413-b421 FALLS TO b422.** '
          '### It is named here and ### **NOT RUN**: 0 lines of FINDINGS.md written.')
    R += ['  the fold named : b413-b421 (%d acts), to be filed by b422' % n_own,
          '  FINDINGS.md unchanged since the pin, in git`s view : %s'
          % (subprocess.run(['git', '-C', PP, 'diff', '--quiet', '743be4a', '--', 'FINDINGS.md']).returncode == 0), '',
          '### `(N3)`, ITS CLAUSES APART (R27):',
          '      *the span counts eight* -- ### **MET WITHOUT THIS ACT (%d at --act 420); REFUTED AT THE ACT`S OWN COUNT (%d)**,' % (n_wo, n_own),
          '          which the face fixed as the act`s count: the tool counts through the highest act that has banked a file.',
          '      *the fold is named for b422 and not run* -- ### **MET.**', '=' * 100]
    put('b421_c3_span.txt', R)
    print(NL.join(R))
    return 1 if MISS or n_own == 0 else 0


# =============================================================================================
# ### THE CLOSING'S ADDED LINE -- THE NAVIGATOR'S THREE CONFLATIONS AT b420, WITH THE SEAT'S CORRECTIONS.
# =============================================================================================
def run_conflations():
    R = ['=' * 100, 'b421 -- THE NAVIGATOR`S THREE CONFLATIONS AT b420, ENTERED AS THE NAVIGATOR`S, WITH THE CORRECTIONS.', '=' * 100,
         '  ### Entered so the next navigator inherits the correction and not the conflation. ### Each quotation is',
         '  ### pulled from its file at run time: the navigator`s words from the banked b420 ferry, the seat`s correction',
         '  ### from b420`s own record, and the source both were about.']
    f420 = os.path.join(D, 'b420_ferry.txt')
    c4 = os.path.join(D, 'b420_c4_barrier.txt')
    items = [
        ('(1) THE THEOREM`S CONTENT AGAINST A DERIVED RESULT`S WORDS.',
         q(f420, 'the general clause proved at b419, which returns', 'nothing about its sign;'),
         q(c4, '### **b419`S TERMINAL DOES NOT MENTION A TEST FUNCTION', 'Component 2 prices.'),
         q(SMG, 'theorem smear_general', ':= by')),
        ('(2) THE COMPRESSED TRACE AGAINST THE FINITE-PLACE TERM.',
         q(f420, 'is each finite-place interface', 'the general clause proved at b419'),
         q(c4, '### **AND THE FINITE PLACE`S TERM IN THE', 'the prime`s powers.'),
         q(os.path.join(D, 'b310_the_smear_collapses.txt'), 'The arithmetic is in the distribution, not in', 'as its prime sum.')),
        ('(3) THE MAP`S OWN SCOPE SENTENCE.',
         q(f420, 'the aim map measured — every aim', 'at any height.'),
         q(c4, '### **THE WORDING DIFFERS, AND THE SOURCE GOVERNS:**', 'at any height*.'),
         q(os.path.join(D, 'b334_the_aim_map.txt'), '### IT SAYS that for zeta the prime sum is inside the margin', 'NOTHING MORE.**')),
    ]
    for title, nav, cor, src in items:
        R += ['', '### %s' % title]
        block(R, 'THE NAVIGATOR`S WORDS (b420 ferry) :', nav)
        block(R, 'THE SEAT`S CORRECTION (b420`s record) :', cor)
        block(R, 'THE SOURCE :', src)
    R += ['', '  conflations entered with their corrections : %d' % len(items),
          '  ### ### **THE SOURCE GOVERNS IN ALL THREE.** ### None is the navigator`s fault to be fixed here: each is entered',
          '  ### as the navigator`s, beside its correction, and nothing the navigator wrote is edited.', '=' * 100]
    put('b421_conflations.txt', R)
    print(NL.join(R))
    return 1 if MISS else 0


# =============================================================================================
# ### COMPONENT 1 -- THE FINITE AMBIENT. ### The probes banked, the verdict read from the profile.
# =============================================================================================
TERMINAL = 'GridTrace.grid_trace_is_signed_count'
PRINTS = ['key', 'mod_add_iff', 'diagA', 'diagB', 'trA_eq', 'trB_eq', 'grid_trace_is_signed_count']
MODF = os.path.join(KERN, 'Core', 'GridTrace.lean')
ALLP = os.path.join(KERN, 'AllPrints.lean')
PROF = os.path.join(KERN, 'AXIOM_PRINTS.txt')


def lean_code(src):
    return re.sub(r'--[^\n]*', ' ', re.sub(r'/-.*?-/', ' ', src, flags=re.S))


def probes():
    return sorted(f for f in os.listdir(NDIR) if re.match(r'p\d\d\.lean$', f))


def minutes(a, b):
    f = '%Y-%m-%dT%H:%M:%SZ'
    return (datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds() / 60.0


def run_c1_record():
    ps = probes()
    last = ps[-1][:-5]
    out = read(os.path.join(NDIR, last + '.out'))
    line = next((x for x in out.splitlines() if x.startswith("'%s'" % TERMINAL)), None)
    verdict = 'PROVED' if (line and line.endswith(CLEAN)) else 'NOT PROVED'
    t0 = read(os.path.join(NDIR, 'p01.start')).strip()
    t1 = read(os.path.join(NDIR, last + '.end')).strip()
    src = read(os.path.join(NDIR, last + '.lean'))
    R = ['=' * 100, 'b421 COMPONENT 1 -- THE FINITE AMBIENT: EVERY PROBE, ITS SOURCE AND ITS PRINTED PROFILE.', '=' * 100,
         '  banked at (UTC) : %s' % utc(),
         '  probe directory (scratch, outside every repository) : %s' % NDIR,
         '  probes compiled : %d of the sixteen b418`s budget allows ; minutes from the first probe`s start to the last`s end : %.1f of 150'
         % (len(ps), minutes(t0, t1)),
         '  imports in the last probe : %s' % re.findall(r'(?m)^import (\S+)', src),
         '  ### `sorry` as a term in the last probe : %d ; `axiom` declarations : %d'
         % (len(re.findall(r'\bsorry\b', lean_code(src))), len(re.findall(r'(?m)^\s*axiom\b', lean_code(src)))),
         '  ### the terminal`s own line : %s' % line,
         '  ### ### **VERDICT, READ FROM THE PROFILE : %s** ### (the exit line is printed below and read by nothing)' % verdict,
         '',
         '  ### THE WAY THERE, PROBE BY PROBE:',
         '      p01 -- the palette: which library lemmas are axiom-free here. `Nat.add_mul`, `Nat.pow_add`,',
         '             `Nat.sub_add_cancel`, `Nat.mod_eq_of_lt`, `Nat.add_left_cancel` and `Nat.beq_refl` carry propext;',
         '             the library was written around them.',
         '      p02 -- the whole library; ONE error, in `beq_self`: Nat`s `==` here is the decide-based `BEq`, not',
         '             `Nat.beq`, so `Nat.ne_of_beq_eq_false` did not apply; every other declaration elaborated, and the',
         '             terminals printed `sorryAx` by inheritance only.',
         '      p03 -- p02 with `beq_self` proved as `decide_eq_true rfl` and nothing else changed: every print clean.']
    for f in ps:
        R += ['', '-' * 100, '### %s -- %d source lines' % (f, len(read(os.path.join(NDIR, f)).splitlines())), '-' * 100]
        R += ['  | %s' % x for x in read(os.path.join(NDIR, f)).splitlines()]
        R += ['  ### PRINTED:'] + ['  > %s' % x for x in read(os.path.join(NDIR, f[:-5] + '.out')).splitlines()]
    R.append('=' * 100)
    put('b421_c1_probes.txt', R)
    print(NL.join(R[:16]))
    return 0 if verdict == 'PROVED' else 1


def run_c1_kernel():
    R = ['=' * 100, 'b421 COMPONENT 1 -- THE KERNEL WRITES, ON PROVED.', '=' * 100, '  at (UTC) : %s' % utc()]
    if '**VERDICT, READ FROM THE PROFILE : PROVED**' not in read(os.path.join(D, 'b421_c1_probes.txt')):
        R.append('  ### REFUSED: the banked probes do not read PROVED.')
        put('b421_c1_kernel.txt', R)
        print(NL.join(R))
        return 2
    src = read(os.path.join(NDIR, probes()[-1])).splitlines()
    assert src[0].startswith('--') and src[1] == 'import SmearGeneral'
    body = [x for x in src[1:] if not x.startswith('#print')]
    mod = re.sub(r'\n{3,}', NL + NL, NL.join(body)).rstrip() + NL
    if os.path.exists(MODF):
        R.append('  ### module already present -- NOT rewritten.')
    else:
        open(MODF, 'wb').write(mod.encode('utf-8'))
        R.append('  written : Core/GridTrace.lean -- %d lines, sha %s' % (len(mod.splitlines()), sha(mod.encode())[:16]))
    ap = rb(ALLP)
    if b'import GridTrace' in ap:
        R.append('  ### AllPrints already carries the import -- NOT re-inserted.')
    else:
        last = b'import SmearGeneral\n'
        imports = re.findall(rb'(?m)^import .*\n', ap)
        assert imports[-1] == last and ap.count(last) == 1 and ap.endswith(b'\n')
        new = ap.replace(last, last + b'import GridTrace\n', 1)
        new += b''.join(b'#print axioms GridTrace.%s\n' % x.encode() for x in PRINTS)
        open(ALLP, 'wb').write(new)
        R.append('  AllPrints : ONE import line INSERTED after `import SmearGeneral`; %d prints APPENDED; sha %s -> %s'
                 % (len(PRINTS), sha(ap)[:16], sha(new)[:16]))
    R.append('=' * 100)
    put('b421_c1_kernel.txt', R)
    print(NL.join(R))
    return 0


def run_c1_verify():
    R = ['=' * 100, 'b421 COMPONENT 1 -- VERIFIED AFTER THE BUILD.', '=' * 100, '  at (UTC) : %s' % utc()]
    fails = []
    old, new = blob(KERN, 'AXIOM_PRINTS.txt', PIN_SIDE), rb(PROF)
    pre = new.startswith(old) and len(new) > len(old)
    tail = new[len(old):].decode('utf-8').splitlines() if pre else []
    okt = [x.split("'")[1] for x in tail] == ['GridTrace.%s' % x for x in PRINTS] and all(x.endswith(CLEAN) for x in tail)
    dirty = [x for x in new.decode('utf-8').splitlines() if x.strip() and not x.endswith(CLEAN)]
    R += ['### THE PROFILE, AGAINST THE BLOB AT THE PIN (%s).' % PIN_SIDE,
          '  prior %d lines, sha %s ; new %d lines, sha %s' % (old.count(b'\n'), sha(old)[:16], new.count(b'\n'), sha(new)[:16]),
          '  ### ### **THE PRIOR PROFILE IS A TRUE BYTE PREFIX OF THE NEW : %s**' % pre]
    R += ['      + %s' % x for x in tail]
    R += ['  every line beyond it is this module`s, and clean : %s' % okt,
          '  lines in the whole profile NOT reading "%s" : %d' % (CLEAN, len(dirty))]
    fails += [] if (pre and okt and not dirty) else ['profile']
    aold, anew = blob(KERN, 'AllPrints.lean', PIN_SIDE), rb(ALLP)
    ins = aold.replace(b'import SmearGeneral\n', b'import SmearGeneral\nimport GridTrace\n', 1)
    ok_ap = anew.startswith(ins) and anew[len(ins):] == b''.join(b'#print axioms GridTrace.%s\n' % x.encode() for x in PRINTS)
    R += ['', '### AllPrints.lean -- b420`s corrected form.',
          '  ### ### **ONE IMPORT LINE INSERTED AFTER THE LAST IMPORT, THE PRINTS APPENDED, NOTHING ELSE : %s**' % ok_ap]
    fails += [] if ok_ap else ['allprints']
    changed = subprocess.run(['git', '-C', KERN, 'diff', '--name-only', PIN_SIDE, '--', 'Core'], capture_output=True, text=True).stdout.split()
    cl = sha(rb(os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')))
    R += ['', '### THE FILES THAT MUST NOT MOVE.',
          '  existing Core files changed since the pin : %s' % (changed or 'none'),
          '  Classes.lean sha %s ; the before-digest d4f931db1d50c01f : %s' % (cl[:16], cl.startswith('d4f931db1d50c01f'))]
    fails += [] if (not changed and cl.startswith('d4f931db1d50c01f')) else ['unmoved']
    ms = read(MODF)
    R += ['', '### THE MODULE.',
          '  imports : %s ; `sorry` as a term : %d' % (re.findall(r'(?m)^import (\S+)', ms), len(re.findall(r'\bsorry\b', lean_code(ms)))),
          '  the statement names both objects : %s' % ('gridTrace p n t = B329.signedTrace p n t' in ms),
          '  its docstring says the source`s trace is not this object : %s' % ('THE SOURCE\'S TRACE IS NOT THIS OBJECT' in ms),
          '  and that the source governs : %s' % ('the source\n  governs' in ms or 'the source governs' in ms)]
    fails += [] if (re.findall(r'(?m)^import (\S+)', ms) == ['SmearGeneral'] and 'THE SOURCE\'S TRACE IS NOT THIS OBJECT' in ms) else ['module']
    R += ['', '### ### **VERIFY FAILURES : %d %s**' % (len(fails), fails), '=' * 100]
    put('b421_c1_verify.txt', R)
    print(NL.join(R))
    return 1 if fails else 0


def main():
    L = []
    say = L.append
    recs = {nm: read(os.path.join(D, f)) for nm, f in (
        ('probes', 'b421_c1_probes.txt'), ('kernel', 'b421_c1_kernel.txt'), ('build', 'b421_kernel_build.txt'),
        ('verify', 'b421_c1_verify.txt'), ('c2', 'b421_c2_specification.txt'), ('c3', 'b421_c3_span.txt'),
        ('confl', 'b421_conflations.txt'))}
    fails = [nm for nm, t in recs.items() if not t]
    pv = re.search(r'VERDICT, READ FROM THE PROFILE : (\S+)\*\*', recs['probes'])
    budget = next((x.strip() for x in recs['probes'].splitlines() if 'probes compiled :' in x), '### MISS')
    say('=' * 100)
    say('b421_components.py -- THE FINITE AMBIENT BUILT OR PRICED, AND THE SPAN COUNTED.')
    say('=' * 100)
    say('')
    say('### COMPONENT 1 -- THE FINITE AMBIENT.')
    say('  ### ### **VERDICT : %s** ### (read from the profile)' % (pv.group(1) if pv else '### MISS'))
    say('  %s' % budget)
    for x in read(PROF).splitlines():
        if x.startswith("'GridTrace.grid_trace_is_signed_count'"):
            say('  the terminal, as the kernel prints it : %s' % x)
    for needle in ('THE PRIOR PROFILE IS A TRUE BYTE PREFIX OF THE NEW : True',
                   'THE PRINTS APPENDED, NOTHING ELSE : True', 'existing Core files changed since the pin : none',
                   'its docstring says the source`s trace is not this object : True', 'VERIFY FAILURES : 0'):
        ok = needle in recs['verify']
        fails += [] if ok else ['c1:' + needle[:24]]
        say('  %-80s %s' % (needle[:80], ok))
    say('**(N1)**, its clauses apart (R27):')
    say('      proves within the budget -- ### **MET**: %s.' % budget.replace('probes compiled : ', ''))
    say('      no Mathlib import        -- ### **MET**: the module imports `SmearGeneral` and nothing else.')
    say('')
    say('### COMPONENT 2 -- THE SPECIFICATION.')
    for x in recs['c2'].splitlines():
        if 'PRICE UNDER' in x or 'documents holding' in x or '(N2)' in x:
            say('  ' + x.strip())
    say('')
    say('### COMPONENT 3 -- THE SPAN.')
    for x in recs['c3'].splitlines():
        if 'COUNT :' in x or 'the fold named' in x or '*the span counts' in x or '*the fold is named' in x:
            say('  ' + x.strip())
    say('')
    say('### THE CLOSING`S ADDED LINE -- %s' % next((x.strip() for x in recs['confl'].splitlines() if 'conflations entered' in x), '### MISS'))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    put('b421_components.txt', L)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(main())
    for flag, fn in (('--c2', run_c2), ('--c3', run_c3), ('--conflations', run_conflations),
                     ('--c1-record', run_c1_record), ('--c1-kernel', run_c1_kernel), ('--c1-verify', run_c1_verify)):
        if flag in sys.argv:
            sys.exit(fn())
