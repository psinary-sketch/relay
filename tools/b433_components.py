# -*- coding: utf-8 -*-
"""b433_components.py -- THE FIVE RULINGS EXECUTED.

### **EVERY REPAIR IS MEASURED AGAINST THE PRE-ACT BLOB, AND A REPAIR THAT WOULD REMOVE BYTES IS
### REFUSED AND THE FILE RESTORED.** ### Each is written in the form its own document already uses
### (BAR 2), each original stays findable afterwards (BAR 1), and the byte delta is printed per file.
### ### **NO TERMINAL IS RENAMED AND NO `.lean` FILE IS TOUCHED** (BAR 4). ### **NO GRADE MOVES**
### (BAR 5): defining a grade name is not conferring it.
"""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
RDM = os.path.join(PP, 'README.md')
EXC = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
CONSP = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
FIND = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
BARRIER = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
CLONE = os.path.join('D:', os.sep, '_b431_external')
FACE = os.path.join(D, 'b433_registration_2026-09-12.txt')
FERRY = os.path.join(D, 'b433_ferry.txt')
BLOBS = os.path.join(D, 'b433_preact_blobs.txt')
OUT = os.path.join(D, 'b433_components.txt')
RJSON = os.path.join(D, 'b433_repairs.json')
NL = chr(10)
L, MISS = [], []
G = {'repairs': [], 'notlocated': 0, 'refused': 0}
PREBYTES = {}


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def wrap(text, width=90, indent='      '):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(indent + line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(indent + line)
    return out


def snapshot():
    """### **THE PRE-ACT BYTES, HELD IN MEMORY SO A REFUSED REPAIR CAN BE UNDONE EXACTLY.**"""
    for p in (RDM, EXC, CONSP, FIND, FACES, TRAILS):
        PREBYTES[p] = open(p, 'rb').read() if os.path.exists(p) else b''


def repair(path, label, old, new, must_survive, already=None):
    """### ONE REPAIR, MEASURED. ### RETURNS the delta, or None when it did not run.

    ### ### **THREE WAYS IT CAN FAIL AND EACH IS PRINTED RATHER THAN SWALLOWED:**
    ### `NOT LOCATED` -- the anchor is not in the file, so nothing is attempted;
    ### `REFUSED (negative delta)` -- the write would remove bytes, so the file is RESTORED;
    ### `REFUSED (original gone)` -- the text that had to survive did not, so the file is RESTORED.
    """
    txt = read(path)
    before = len(PREBYTES.get(path, b''))
    # ### **THE TOOL MUST BE RE-RUNNABLE.** ### An act's tools are re-run -- after a defect, after a
    # ### checkout, to refresh a bank -- and a repair that reads its own applied result as
    # ### `NOT LOCATED` would report a clean act as a broken one. ### **ALREADY-APPLIED IS ITS OWN
    # ### OUTCOME, NOT A MISS**, and it carries a zero delta because nothing moved this run.
    # ### ### **AND THE TEST IS `new in txt` ALONE.** ### The first writing asked for `old not in
    # ### txt` as well, which is right for a REPLACEMENT and wrong for an INSERTION: an insertion
    # ### keeps its anchor, so the guard never fired and ### **THE SECOND RUN INSERTED EVERY BLOCK A
    # ### ### SECOND TIME** -- the fourth-grade bullet twice in both vocabulary documents, the
    # ### keystone annotation twice, the trail block twice. ### Caught by comparing the two runs'
    # ### byte deltas, which differed; the files were restored from git and verified byte-for-byte
    # ### against the pinned pre-act digests before this guard was trusted.
    # ### **A MARKING IS NOT FOUND BY LOOKING FOR `new`.** ### Where the repair APPENDS to a row,
    # ### the row is re-read ALREADY MARKED on the next run, so `new` -- the unmarked row plus the
    # ### marking -- is never in the file and the guard never fires. ### **EACH REPAIR THEREFORE
    # ### CARRIES ITS OWN ALREADY-APPLIED NEEDLE**, distinctive to it, and `new` is only the
    # ### fallback for the whole-block insertions where it happens to work.
    if (already or new) in txt:
        say('      %-46s ALREADY APPLIED (idempotent), delta +0' % label)
        G['repairs'].append(dict(file=os.path.relpath(path, PP), label=label,
                                 status='ALREADY APPLIED', delta=0))
        return 0
    if old not in txt:
        say('      %-46s ### NOT LOCATED -- not attempted' % label)
        G['notlocated'] += 1
        G['repairs'].append(dict(file=os.path.relpath(path, PP), label=label,
                                 status='NOT LOCATED', delta=None))
        return None
    out = txt.replace(old, new, 1)
    data = out.encode('utf-8')
    delta = len(data) - before
    bad = None
    if delta < 0:
        bad = 'REFUSED (negative delta)'
    else:
        for s in must_survive:
            if s not in out:
                bad = 'REFUSED (original gone)'
                break
    if bad:
        open(path, 'wb').write(PREBYTES[path])          # ### RESTORED, byte for byte
        say('      %-46s ### %s -- file restored' % (label, bad))
        G['refused'] += 1
        G['repairs'].append(dict(file=os.path.relpath(path, PP), label=label,
                                 status=bad, delta=delta))
        return None
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    say('      %-46s APPLIED   delta %+d bytes' % (label, delta))
    G['repairs'].append(dict(file=os.path.relpath(path, PP), label=label,
                             status='APPLIED', delta=delta,
                             sha256=hashlib.sha256(data).hexdigest()))
    return delta


# ### =============================================================================================
def comp1():
    rule('=')
    say('  COMPONENT 1 -- THE FIVE RULINGS, QUOTED FROM THE BANKED PASTE.')
    rule('=')
    face = read(FACE)
    m = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    say('  ### THE SEAL THIS RUN READ OFF THE LOCKED FACE : %s'
        % (m.group(1) if m else '### NO LOCK BLOCK ###'))
    G['seal_read_from_face'] = m.group(1) if m else None
    say()
    ft = read(FERRY)
    mm = re.search(r'RULINGS, the author.s.*?(?=' + NL + r'{2}LEG 1)', ft, re.S)
    txt = re.sub(r'\s+', ' ', mm.group(0)) if mm else ''
    if not txt:
        MISS.append('the rulings block was not found in the banked ferry')
    for ln in wrap(txt, 92, '    '):
        say(ln)
    G['rulings_quoted'] = bool(txt)
    G['rulings_named'] = sorted(set(re.findall(r'\(R4[1-5]\)', txt)))
    say()
    say('    ### RULINGS NAMED IN THE QUOTED BLOCK : %s' % G['rulings_named'])
    say('    ### **EACH IS EXECUTED AS ITS OWN WORDS SAY AND NONE IS EXTENDED** (`R23`).')
    say()


def comp2():
    rule('=')
    say('  COMPONENT 2 -- (R41): THE FOURTH GRADE DEFINED, ADDITIVELY, IN BOTH DOCUMENTS.')
    rule('=')
    say('    ### **THE FORM IS `(R4)`: PRESERVE BY QUOTATION, REPAIR BY EDIT.** ### Each heading is')
    say('    ### corrected and the words it had are quoted in the note directly beneath it, so the')
    say('    ### original is not lost by being replaced.')
    say()
    fourth = (
        '- **NOT THE CLAIM** — the theorem is sound and its statement is **strictly weaker than the\n'
        '  claim the row makes for it**. Not a shell: it stipulates nothing and it proves what it\n'
        '  says. Not `INTERFACES`: it takes no named premise. It simply does not reach the claim,\n'
        '  and a row that pairs it with that claim is the thing at fault. **A grade is a relation\n'
        '  between a terminal and a named claim** (`(R40)`), so the same terminal may carry\n'
        '  different grades against different claims, both honestly stated.\n')

    # ### ---- README ---------------------------------------------------------------------------
    rdm_old = '### The three grades\n'
    rdm_new = (
        '### The four grades\n'
        '\n'
        '> **`(R41)`, b433, 2026-09-12 — this heading read *"The three grades"*, and the list below\n'
        '> held three. A fourth is added; the three above it are unchanged, word for word.**\n')
    repair(RDM, 'README.md heading corrected', rdm_old, rdm_new, ['The three grades'])
    anchor = ('- **ENCODES-CONCLUSION / SHELL** — the theorem stipulates what the paper claims, or\n'
              '  concludes a placeholder. These are **work-orders, not citations**, and are labelled\n'
              '  as such wherever they appear.\n')
    repair(RDM, 'README.md fourth grade added', anchor, anchor + fourth,
           ['work-orders, not citations'])

    # ### ---- EXCLUSION_ENGINE -------------------------------------------------------------------
    exc_old = '## 0. Reading this paper: the three grades\n'
    exc_new = (
        '## 0. Reading this paper: the four grades\n'
        '\n'
        '> **`(R41)`, b433, 2026-09-12 — this heading read *"Reading this paper: the three grades"*.\n'
        '> A fourth grade is added below; the three that were here are unchanged, word for word.**\n')
    repair(EXC, 'EXCLUSION_ENGINE heading corrected', exc_old, exc_new,
           ['Reading this paper: the three grades'])
    exc_anchor = ('- **ENCODES-CONCLUSION / SHELL** — the kernel writes the conclusion in: a `Bool` '
                  'field assigned `true`, a predicate defined as `fun _ => True`, a hypothesis that '
                  '*is* the claim, an `X = X`. It compiles, it has zero `sorry`, and it certifies '
                  'nothing. **A shell is a work-order, not a citation.**\n')
    exc_fourth = (
        '- **NOT THE CLAIM** — the kernel proves a theorem that is sound and **strictly weaker than '
        'the claim the citation makes for it**. It is not a shell: it stipulates nothing and proves '
        'what it states. It is not `INTERFACES`: it takes no named premise. It does not reach the '
        'claim, and the row that pairs the two is what is at fault. **A grade is a relation between '
        'a terminal and a named claim** (`(R40)`), so one terminal may carry different grades '
        'against different claims, both honestly stated.\n')
    repair(EXC, 'EXCLUSION_ENGINE fourth grade added', exc_anchor, exc_anchor + exc_fourth,
           ['A shell is a work-order, not a citation.'])

    # ### ---- THE TWO INCIDENTS, CITED, AS (R41) REQUIRES -----------------------------------------
    inc = (
        '\n**The fourth grade came from two measurements, and both are cited because a grade '
        'admitted without its occasion is a grade nobody can check.** At **b429** the corpus graded '
        'a proof it did not write and found that *four* grades were available against the stranger '
        'while the corpus had only ever had three — an asymmetry in the instrument, unused there '
        'and so changing no outcome. At **b430** the corpus put its own `SmearGeneral.smear_general` '
        'to the same protocol and the fourth grade *was* needed: the terminal grades `DERIVES` '
        'against the claim its correspondence row names and **`NOT THE CLAIM`** against the claim '
        'its own finite-side prose makes, for two independent reasons — scope, and the objects the '
        'statement names. Both gradings are banked at relay and cited in no corpus document.\n')
    repair(EXC, 'EXCLUSION_ENGINE incidents cited',
           'The third grade is not a hypothetical.',
           inc.lstrip(NL) + '\nThe third grade is not a hypothetical.',
           ['The third grade is not a hypothetical.'])
    say()


def comp3():
    rule('=')
    say('  COMPONENT 3 -- (R42): THE KEYSTONE ANNOTATED IN PLACE. ### THE NAME IS NOT TOUCHED.')
    rule('=')
    say('    ### **`crt_exhaustiveness` KEEPS ITS NAME** -- in the kernel, which this act does not')
    say('    ### open, and in every line of this document. ### `(R42)` says so in its own words.')
    say()
    ann = (
        '\n### **THE COMPILED LEMMA, READ AT ITS STATEMENT** '
        '*(annotation added 2026-09-12, b433, ruling `(R42)`; existing text PRESERVED — this adds a '
        'reading and rewrites nothing, and the lemma is NOT renamed)*\n'
        '\n'
        '`Module1.crt_exhaustiveness` is described above as *CRT exhaustiveness via periodic lift*. '
        'Read at its statement rather than at its name, **the proof is the periodic lift and the '
        'Chinese Remainder Theorem is not invoked in it**:\n'
        '\n'
        '- It quantifies over **one** `StructuralCoupling` — a syntactic term built from finitely '
        'many explicit congruence, divisibility and coprimality conditions, whose `period` is the '
        'lcm of its own moduli and is **fixed by the term**.\n'
        '- Its witness is `to_modular sc = ofPeriodic sc.period`, whose modulus set is '
        '**`moduli := {L}` — a singleton**. No product over primes appears in the statement or in '
        'the witness.\n'
        '- What it therefore establishes is that **a predicate built from finitely many congruence '
        'conditions is a congruence condition modulo the lcm of those moduli**. That is true, '
        'cleanly proved, and narrower than the sentence above.\n'
        '\n'
        '**So the claim this paper makes for the lemma is narrowed to what the proof does.** Where '
        'the text above says the exclusion covers what CRT explains *at every finite modulus*, the '
        'compiled content is the periodic lift **at the coupling\'s own single modulus**; the '
        'general statement about every finite modulus remains a manuscript claim and is not carried '
        'by this terminal. **The name stays** — it names the intuition the section explains, and '
        'renaming it would break every citation that resolves to it. *(Measured at b431 against '
        'a covering construction that does use CRT across π(x) prime moduli; the two statements '
        'part at what is quantified. That reading is banked at relay and cited in no corpus '
        'document.)*\n')
    a = '### II.3 Why CRT explains all the modular constraint\n'
    repair(CONSP, 'conspiracy keystone annotated', a, a + ann,
           ['### II.3 Why CRT explains all the modular constraint',
            'CRT exhaustiveness via periodic lift'])
    src = read(CONSP)
    say('      name `crt_exhaustiveness` still present  : %s' % ('crt_exhaustiveness' in src))
    say('      the original prose sentence still present: %s'
        % ('beyond what the Chinese Remainder Theorem explains at every finite modulus' in src))
    G['r42_name_kept'] = 'crt_exhaustiveness' in src
    say()


def comp4():
    rule('=')
    say('  COMPONENT 4 -- (R43): K3 AND F5 MARKED TO WHAT THE TERMINAL STATES.')
    rule('=')
    say('    ### **THE MARKING IS ADDED TO THE ROW\'S OWN LAST CELL**, so it travels with the row')
    say('    ### and every existing word of the row survives. ### The scope clause is NOT rewritten')
    say('    ### -- BAR 6, and the face says why before the fact.')
    say()
    mark_k3a = (' **`(R43)`, b433 — NARROWED TO THE TERMINAL: of the objects named in this row, '
                '`SmearGeneral.smear_general` (b419) carries NONE. What it states is the model\'s '
                'count — an equation between three `Nat` quantities — over bases with a SINGLE '
                'PRIME FACTOR only. The source\'s construction, the test function at the identity '
                'and the dimension are **what the source\'s trace would require** and are **not '
                'carried by that terminal**; their identification with the model\'s count stays '
                'b310\'s derivation and is not compiled.** |')
    txt = read(FIND)
    k3rows = [(i, ln) for i, ln in enumerate(txt.splitlines(), 1)
              if re.match(r'^\|\s*\*\*K3\*\*', ln)]
    say('      FINDINGS.md rows opening with K3 : %s' % [i for i, _ in k3rows])
    say('      ### **THE ROW MARKED IS THE ONE NAMING THE KERNEL TERMINALS** -- chosen by that')
    say('      ### printed rule and not by position (b430\'s `F5` lesson).')
    target = [(i, ln) for i, ln in k3rows if 'KERNEL TERMINALS' in ln]
    if len(target) != 1:
        say('      ### NOT LOCATED -- the rule chose %d rows, not 1' % len(target))
        G['notlocated'] += 1
    else:
        i, ln = target[0]
        repair(FIND, 'FINDINGS K3 (terminals row) marked', ln, ln.rstrip()[:-1].rstrip() + mark_k3a,
               ['KERNEL TERMINALS', 'the test function at the identity times a dimension'],
               already='NARROWED TO THE TERMINAL: of the objects named in this row')
    mark_k3b = (' **`(R43)`, b433 — NARROWED: these grades are b329\'s and b310\'s. '
                '`SmearGeneral.smear_general` (b419) is NOT among them; it grades `DERIVES` only '
                'against the claim its own correspondence row names, and `NOT THE CLAIM` against '
                'the prose of this anchor.** |')
    txt = read(FIND)
    grow = [(i, ln) for i, ln in enumerate(txt.splitlines(), 1)
            if re.match(r'^\|\s*\*\*K3\*\*', ln) and 'PROVED-GENERAL' in ln]
    if len(grow) == 1:
        i, ln = grow[0]
        repair(FIND, 'FINDINGS K3 (grade row) marked', ln, ln.rstrip()[:-1].rstrip() + mark_k3b,
               ['PROVED-GENERAL (b329)'],
               already='NARROWED: these grades are b329')
    else:
        say('      %-46s ### NOT LOCATED -- %d rows' % ('FINDINGS K3 (grade row) marked', len(grow)))
        G['notlocated'] += 1

    mark_f5 = (' **`(R43)`, b433 — NARROWED TO THE TERMINAL: the scope clause above is TRUE of the '
               'terminals THIS ROW LISTS. `SmearGeneral.smear_general` (b419) is in NEITHER list, '
               'and what it states is the model\'s count over bases with a SINGLE PRIME FACTOR '
               'only — strictly less than "every base p ≥ 2". It is graded `NOT THE CLAIM` against '
               'this row\'s prose and `DERIVES` against the claim its own correspondence row '
               'names (b430).** |')
    txt = read(FACES)
    f5 = [(i, ln) for i, ln in enumerate(txt.splitlines(), 1)
          if re.match(r'^\|\s*\*\*F5\*\*', ln) and 'FiniteSideSeal.lean' in ln]
    say('      FACES_LEDGER rows opening with F5 and naming the module : %s' % [i for i, _ in f5])
    if len(f5) == 1:
        i, ln = f5[0]
        repair(FACES, 'FACES_LEDGER F5 marked', ln, ln.rstrip()[:-1].rstrip() + mark_f5,
               ['GENERAL, over every base p ≥ 2, level, power and index'],
               already='NARROWED TO THE TERMINAL: the scope clause above is TRUE')
    else:
        say('      %-46s ### NOT LOCATED -- %d rows' % ('FACES_LEDGER F5 marked', len(f5)))
        G['notlocated'] += 1
    ft = read(FACES)
    say('      F5\'s scope clause still present, word for word : %s'
        % ('GENERAL, over every base p ≥ 2, level, power and index' in ft))
    G['r43_scope_clause_kept'] = ('GENERAL, over every base p ≥ 2, level, power and index' in ft)
    say()


def comp5():
    rule('=')
    say('  COMPONENT 5 -- THE TRAIL ENTRY GAINS THE FORM-(b) FINDING.')
    rule('=')
    t = read(TRAILS)
    mk = '<!-- b432 the disproof lane restated with a worked case -->'
    say('    b432\'s entry present : %s' % (mk in t))
    say('    it is the last block : %s' % (t.rfind(mk) > t.rfind('<!-- b4') - 1))
    add = (
        '\n<!-- b433 the disproof lane: the form-(b) finding, appended to b432\'s entry -->\n'
        '\n'
        '#### b433 — appended to the entry above, by ruling `(R42)`\'s companion order: the form-(b) '
        'finding, and the symmetry clause beside it\n'
        '\n'
        '**The finding, stated plainly: both of the instruments the record names serve form (a), '
        'and the corpus has no instrument pointed at form (b) at all.** The negative control is run '
        'on an object whose off-line zeros are proved and exhibited, and reports whether the '
        'instrument *sees* one; a universal negative exhibits no object, so there is nothing for a '
        'control of that kind to be run on. The phase condition is stated **at an off-line '
        'quadruple** and is that control\'s calibration, not a second instrument.\n'
        '\n'
        '**The barrier keystone\'s symmetry clause, quoted beside it** (`phase1.5/method/'
        'INVARIANCE_BARRIERS.md`, tool **T1** of the toolkit `T`): *"∃ a reflective FE F(s) = '
        'F(1−s) (self-dual completion), centring the critical line at σ = 1/2 — the s ↔ 1−s '
        'symmetry; the location of the centre."* With real coefficients that symmetry makes an '
        'off-line zero a **quadruple** — `s₀, 1−s₀, s̄₀, 1−s̄₀` — which is why the instrument is '
        'tested at a quadruple and why the phase condition is stated there. The scope is the '
        'keystone\'s: T1 is a tool of `T`, and the keystone\'s claim is about what `T` cannot '
        'establish, not about zeta\'s zeros.\n'
        '\n'
        '**And the sentence this addendum exists to put on the record: the instruments are not '
        'symmetric though the theory is.** The functional equation is symmetric in `s ↔ 1−s`, and '
        'the two forms a disproof could take are duals of one another — an exhibited zero and a '
        'universal negative. The corpus\'s instruments are not: every one of them looks for '
        'something to *see*, and nothing in the record looks for something that cannot *be*. '
        '**This sharpens b428\'s finding — the instrument the corpus holds is of the wrong kind for '
        'one of the two forms, not merely unpointed — and it is not a claim that form (b) is '
        'unreachable, nor any pricing of an instrument for it. ROUTED.**\n'
        '\n'
        '**The lane is not opened by this addendum and its trigger is untouched: the instrument '
        'lane opening.**\n')
    # ### **AND THE APPEND GUARDS ITSELF TOO.** ### comp5 does not go through `repair`, so it had
    # ### no guard at all and appended its block on every run.
    if '<!-- b433 the disproof lane' in t:
        say('      %-46s ALREADY APPLIED (idempotent), delta +0' % 'OPEN_TRAILS form-(b) finding')
        G['repairs'].append(dict(file='OPEN_TRAILS.md', label='form-(b) finding appended',
                                 status='ALREADY APPLIED', delta=0))
        say()
        return
    before = len(PREBYTES.get(TRAILS, b''))
    data = (t.rstrip(NL) + NL + add).encode('utf-8')
    delta = len(data) - before
    if delta < 0 or not t.rstrip(NL).encode('utf-8') == data[:len(t.rstrip(NL).encode('utf-8'))]:
        open(TRAILS, 'wb').write(PREBYTES[TRAILS])
        say('      %-46s ### REFUSED -- file restored' % 'OPEN_TRAILS form-(b) finding')
        G['refused'] += 1
    else:
        open(TRAILS + '.tmp', 'wb').write(data)
        os.replace(TRAILS + '.tmp', TRAILS)
        say('      %-46s APPLIED   delta %+d bytes' % ('OPEN_TRAILS form-(b) finding', delta))
        G['repairs'].append(dict(file='OPEN_TRAILS.md', label='form-(b) finding appended',
                                 status='APPLIED', delta=delta))
    say('      ### **APPEND-ONLY, PROVED**: the prior text is a TRUE PREFIX of the new bytes.')
    say()


def comp6():
    rule('=')
    say('  COMPONENT 6 -- (R44) NOTED AS STANDING; (R45) EXECUTED, SUBSTITUTES CONFIRMED FIRST.')
    rule('=')
    say('    ### **(R44)** -- this act\'s write list is in b432\'s form: tools named, the ritual\'s')
    say('    ### own rewritten files named, and a further tool permitted if the suite declares it.')
    say('    ### **NOTHING IS WRITTEN BY (R44); IT NAMES A FORM AS STANDING.**')
    say()
    say('    ### **(R45)** -- THE SUBSTITUTES ARE CONFIRMED BEFORE ANYTHING IS REMOVED:')
    subs = ['data/b431_paper_pin.txt', 'data/b431_stepzero_lsremote.txt', 'data/b431_build.log',
            'data/b431_profile.txt', 'data/b431_the_grade.json', 'data/b431_components.txt']
    ok = True
    for s in subs:
        p = os.path.join(ROOT, s)
        present = os.path.exists(p)
        tracked = 0 == subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', s],
                                      capture_output=True).returncode
        say('      %-34s present %-5s tracked %s' % (os.path.basename(s), present, tracked))
        ok = ok and present and tracked
    G['substitutes_ok'] = ok
    say('    ### **ALL PRESENT AND TRACKED : %s**' % ok)
    if not ok:
        say('    ### **(R45) NOT EXECUTED.** ### A removal whose substitutes are not committed is a')
        say('    ### deletion, not a substitution. ### The clone stays and the author rules.')
        G['clone_removed'] = False
    elif not os.path.isdir(CLONE):
        say('    ### the clone is already absent; nothing to remove.')
        G['clone_removed'] = True
    else:
        # ### **`ignore_errors=True` HID A REAL FAILURE AND LEFT 36 FILES BEHIND.** ### git marks
        # ### its pack files READ-ONLY, `rmtree` cannot unlink them on Windows, and the flag turned
        # ### every one of those refusals into silence -- the directory survived and the tool said
        # ### nothing. ### **A REMOVAL THAT CANNOT FAIL OUT LOUD IS A REMOVAL NOBODY CAN TRUST.**
        # ### The handler clears the read-only bit and retries; anything it still cannot remove is
        # ### PRINTED.
        def _onerr(func, target, _exc):
            try:
                os.chmod(target, 0o700)
                func(target)
            except Exception as e2:
                MISS.append('could not remove %s : %s' % (target, e2))
        try:
            shutil.rmtree(CLONE, onexc=_onerr)          # ### Python 3.12+
        except TypeError:
            shutil.rmtree(CLONE, onerror=lambda f, t, e: _onerr(f, t, e))
        G['clone_removed'] = not os.path.isdir(CLONE)
        say('    ### removal run. ### **D:/_b431_external present afterwards : %s**'
            % os.path.isdir(CLONE))
        if os.path.isdir(CLONE):
            MISS.append('the clone directory survived its removal')
    say('    ### **AND THE CLONE WAS OUTSIDE EVERY ROSTERED REPOSITORY AND TRACKED BY NOTHING**, so')
    say('    ### its removal changes no repository and loses no committed byte.')
    say()


def comp7():
    rule('=')
    say('  COMPONENT 7 -- EVERY REPAIR MEASURED AGAINST ITS PRE-ACT BLOB.')
    rule('=')
    pre = {}
    for ln in read(BLOBS).splitlines():
        m = re.match(r'^(\S+)\s+(\d+)\s+([0-9a-f]{64})', ln)
        if m:
            pre[m.group(1).replace('\\', '/')] = (int(m.group(2)), m.group(3))
    say('    %-52s %10s %10s %9s' % ('file', 'before', 'after', 'delta'))
    deltas, allpos = {}, True
    for p in (RDM, EXC, CONSP, FIND, FACES, TRAILS, BARRIER):
        rel = os.path.relpath(p, PP).replace('\\', '/')
        b = pre.get(rel, (None, None))[0]
        a = os.path.getsize(p)
        d = (a - b) if b is not None else None
        deltas[rel] = d
        if d is not None and d < 0:
            allpos = False
        say('    %-52s %10s %10d %+9s' % (rel, b, a, d if d is not None else '?'))
    G['deltas'] = deltas
    G['all_deltas_nonnegative'] = allpos
    say('    ### **EVERY DELTA NON-NEGATIVE : %s**' % allpos)
    say('    ### `INVARIANCE_BARRIERS.md` is listed because this act QUOTES it; its delta is `0`,')
    say('    ### which is the point -- ### **A DOCUMENT QUOTED IS A DOCUMENT UNCHANGED.**')
    say()
    say('    ### AND THE ORIGINALS, EACH STILL FINDABLE AFTER ITS REPAIR:')
    checks = [('README.md', RDM, 'The three grades'),
              ('EXCLUSION_ENGINE.md', EXC, 'Reading this paper: the three grades'),
              ('EXCLUSION_ENGINE.md', EXC, 'A shell is a work-order, not a citation.'),
              ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', CONSP,
               'beyond what the Chinese Remainder Theorem explains at every finite modulus'),
              ('ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', CONSP, 'crt_exhaustiveness'),
              ('FINDINGS.md', FIND, 'the test function at the identity times a dimension'),
              ('FACES_LEDGER.md', FACES, 'GENERAL, over every base p ≥ 2, level, power and index')]
    allkept = True
    for lbl, p, s in checks:
        got = s in read(p)
        allkept = allkept and got
        say('      %-42s %-52s %s' % (lbl, s[:50], got))
    G['all_originals_present'] = allkept
    say('    ### **EVERY ORIGINAL STILL PRESENT : %s**' % allkept)
    say()
    say('    ### THE TALLY:')
    say('      repairs APPLIED      : %d'
        % len([r for r in G['repairs'] if r['status'] == 'APPLIED']))
    say('      repairs NOT LOCATED  : %d' % G['notlocated'])
    say('      repairs REFUSED      : %d' % G['refused'])
    say()


def main(argv):
    rule('=')
    say('b433_components.py -- THE FIVE RULINGS EXECUTED. ### EVERY REPAIR MEASURED.')
    rule('=')
    snapshot()
    comp1()
    comp2()
    comp3()
    comp4()
    comp5()
    comp6()
    comp7()
    rule('=')
    say('  ### MISSES : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    io.open(RJSON + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(G, indent=2, ensure_ascii=False) + NL)
    os.replace(RJSON + '.tmp', RJSON)
    print(txt)
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(RJSON)))
    return 0 if (os.path.exists(OUT) and os.path.exists(RJSON)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
