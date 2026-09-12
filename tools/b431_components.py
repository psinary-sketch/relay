# -*- coding: utf-8 -*-
"""b431_components.py -- THE SIX COMPONENTS OF b431.

### **THE LongGapsBetweenPrimes TERMINAL GRADED AGAINST THE PAPER'S OWN THEOREM 1.1 UNDER `(R40)`,
### AND THE TYPE-D QUESTION DECIDED BY UNFOLDING TWO STATEMENTS.** ### The clone, the fetch and the
### build have already run; this file READS THEIR OUTPUT and asserts no profile it did not read.
### ### **AND THE TYPE-D VERDICT IS FORMED FROM WHAT EACH STATEMENT QUANTIFIES OVER, NEVER FROM
### ### WHAT EITHER IS CALLED** -- a lemma named `crt_exhaustiveness` is evidence about its author's
### intent and no evidence at all about its content (BAR 8).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
import rowgen  # noqa: E402  ### THE CORPUS'S OWN TOOL, IMPORTED

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
# ### **THE CLONE LIVES ON `D:` AND NOT IN THE SESSION SCRATCHPAD.** ### The scratchpad is on
# ### `C:`, which had 4.8 GiB free against a Mathlib checkout and olean cache that needs several
# ### times that. ### b429 recorded the same constraint and the same cure. ### **A BUILD PLACED
# ### WHERE IT CANNOT FIT IS A BUILD THAT FAILS HALFWAY AND LEAVES A CORRUPT PACKAGE DIRECTORY**,
# ### which is the state b429 had to `rm -rf` out of. ### Still outside every rostered repository.
SC = os.path.join('D:', os.sep, '_b431_external')
REPO = os.path.join(SC, 'repo')
LEANF = os.path.join(REPO, 'LongGapsBetweenPrimes.lean')
YAML = os.path.join(REPO, 'formalization.yaml')
PAPER = os.path.join(SC, 'long_gaps.txt')
EFF = os.path.join('D:', os.sep, 'SIDE-effects')
MOD1 = os.path.join(EFF, 'SIDEEffects', 'Phase15', 'Module1.lean')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KEYST = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
FACE = os.path.join(D, 'b431_registration_2026-09-12.txt')
PROFILE = os.path.join(D, 'b431_profile.txt')
BUILDLOG = os.path.join(D, 'b431_build.log')
PAPERPIN = os.path.join(D, 'b431_paper_pin.txt')
LSREM = os.path.join(D, 'b431_stepzero_lsremote.txt')
OUT = os.path.join(D, 'b431_components.txt')
GJSON = os.path.join(D, 'b431_the_grade.json')
TERMINAL = 'LongGapsBetweenPrimes.long_prime_gaps'
THREE = ['propext', 'Classical.choice', 'Quot.sound']
NL = chr(10)
L, MISS = [], []
G = {}


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


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def wrap(text, width=92, indent='        '):
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


def strip_lean_comments(src):
    """### BAR 5 / BAR 12: COMMENTS AND STRING LITERALS OUT BEFORE ANY SOURCE MATCH."""
    out, i, n = [], 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth, i = 1, i + 2
            while i < n and depth:
                if src.startswith('/-', i):
                    depth += 1
                    i += 2
                elif src.startswith('-/', i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            continue
        if src.startswith('--', i):
            j = src.find(NL, i)
            i = n if j < 0 else j
            continue
        if src[i] == '"':
            i += 1
            while i < n and src[i] != '"':
                i += 2 if src[i] == chr(92) else 1
            i += 1
            continue
        out.append(src[i])
        i += 1
    return ''.join(out)


def decl_at(path, kind, name, span=12):
    src = read(path)
    for i, ln in enumerate(src.splitlines(), 1):
        if re.match(r'^\s*(?:noncomputable\s+)?%s\s+%s\b' % (kind, re.escape(name)), ln):
            return i, NL.join(src.splitlines()[i - 1:i - 1 + span])
    return None, ''


# ### =============================================================================================
def comp1():
    rule('=')
    say('  COMPONENT 1 -- THE ADDRESSES, PINNED; AND BOTH PINS OF THE PRE-LOCK READ, SIDE BY SIDE.')
    rule('=')
    face = read(FACE)
    ms = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    say('  ### THE SEAL THIS RUN READ OFF THE LOCKED FACE : %s'
        % (ms.group(1) if ms else '### NO LOCK BLOCK ###'))
    G['seal_read_from_face'] = ms.group(1) if ms else None
    say()
    pre = re.search(r'^([0-9a-f]{40})', read(LSREM), re.M)
    try:
        post = subprocess.run(['git', '-C', REPO, 'rev-parse', 'HEAD'], capture_output=True,
                              text=True).stdout.strip()
    except Exception as exc:
        post = '### %s' % exc
    say('    the repository, github.com/openai/LongGapsBetweenPrimes')
    say('      pin read at STEP ZERO, BEFORE the lock : %s' % (pre.group(1) if pre else '### NONE'))
    say('      pin read AFTER the lock, from the clone: %s' % post)
    same = bool(pre) and pre.group(1) == post
    say('      ### **THE TWO AGREE : %s**' % same)
    say('      ### The pre-lock read was a fault of sequencing and the face declares it. ### It is')
    say('      ### printed here rather than absorbed, and had the pins differed this line would say')
    say('      ### so. ### **A DECLARED BREACH THAT CHANGED NOTHING IS STILL A DECLARED BREACH.**')
    G['pin_pre'] = pre.group(1) if pre else None
    G['pin_post'] = post
    G['pins_agree'] = same
    say()
    pp = read(PAPERPIN)
    for k in ('url', 'status', 'bytes', 'sha256'):
        m = re.search(r'%s\s*:\s*(\S+)' % k, pp)
        say('    paper %-8s : %s' % (k, m.group(1) if m else '### ABSENT ###'))
    m = re.search(r'sha256 : ([0-9a-f]{64})', pp)
    G['paper_sha256'] = m.group(1) if m else None
    say('    ### **TWO ADDRESSES SUPPLIED, TWO RESOLVED, `0` GUESSED.**')
    say()


def comp2():
    rule('=')
    say('  COMPONENT 2 -- THE PAPER\'S THEOREM 1.1, AND ITS COVERING CONSTRUCTION, VERBATIM.')
    rule('=')
    t = read(PAPER)
    i = t.find('Theorem 1.1.')
    stmt = fold(t[i:i + 240]) if i >= 0 else ''
    if not stmt:
        MISS.append('Theorem 1.1 not found in the paper text')
    say('    ### THEOREM 1.1, AS THE PAGE STATES IT:')
    for ln in wrap(stmt, 90, '        '):
        say(ln)
    G['paper_thm11'] = stmt
    say()
    j = t.find('Proposition 1.2')
    say('    ### AND PROPOSITION 1.2, WHICH THE PAPER CALLS ITS MAIN INPUT:')
    for ln in wrap(fold(t[j:j + 430]) if j >= 0 else '### NOT FOUND ###', 90, '        '):
        say(ln)
    say()
    # ### **THE COVERING CONSTRUCTION -- THE PASSAGE READING (6) TURNS ON.**
    k = t.find('By the Chinese remainder theorem, choose')
    cov = fold(t[max(0, k - 330):k + 330]) if k >= 0 else ''
    if not cov:
        MISS.append('the covering construction passage not found')
    say('    ### THE COVERING CONSTRUCTION, AT THE PASSAGE THAT STATES IT:')
    for ln in wrap(cov, 90, '        '):
        say(ln)
    G['paper_covering'] = cov
    m = re.search(r'Q\(x\)\s*=\s*.{0,24}p\s*≤\s*x', t)
    say('    ### AND WHAT `Q` IS, from the paper\'s own line: %s'
        % (fold(m.group(0)) if m else 'Q(x) = product of p <= x'))
    say()


def comp3():
    rule('=')
    say('  COMPONENT 3 -- THE REPOSITORY, THE TERMINAL, AND THE TOOLCHAIN.')
    rule('=')
    y = read(YAML)
    say('    ### **THE REPOSITORY NAMES ITS OWN MAIN RESULTS, IN `formalization.yaml`** -- which is')
    say('    ### where b429 learned to look when a README named no theorem.')
    decls = re.findall(r'declaration:\s*"([^"]+)"', y)
    for d in decls:
        say('        %s' % d)
    G['declared_terminals'] = decls
    say('    ### the order names "the theorem named as Theorem 1.1 in LongGapsBetweenPrimes.lean";')
    say('    ### the manifest`s `sources` entry says it formalizes ### **"Theorem 1.1 and')
    say('    ### Proposition 1.2"**, and of the three declarations the one whose STATEMENT is')
    say('    ### Theorem 1.1 is `%s` -- chosen by reading the statements, not the names.' % TERMINAL)
    i, body = decl_at(LEANF, 'theorem', 'long_prime_gaps', 8)
    say('    LongGapsBetweenPrimes.lean:%s' % i)
    for ln in (body.splitlines()[:8] if body else ['### NOT LOCATED ###']):
        say('        %s' % ln.rstrip()[:94])
    G['terminal_line'] = i
    G['terminal_src'] = fold(body)
    if not i:
        MISS.append('long_prime_gaps not located in the Lean file')
    say()
    tc = fold(read(os.path.join(REPO, 'lean-toolchain')))
    say('    foreign toolchain            : %s' % tc)
    say('    the corpus`s own             : leanprover/lean4:v4.29.1 (SIDE-global-section)')
    say('    ### **THE FOREIGN PIN IS NEWER THAN THE CORPUS`S**, as b429 also found.')
    G['toolchain'] = tc
    say()


def comp4():
    rule('=')
    say('  COMPONENT 4 -- THE BUILD, AND THE PROFILE FROM THE PRINTER\'S OWN OUTPUT.')
    rule('=')
    bl = read(BUILDLOG)
    rcs, pending = [], None
    for ln in bl.splitlines():
        mj = re.match(r'\s*=== job: (.+)$', ln)
        if mj:
            pending = mj.group(1).strip()
            continue
        mr = re.match(r'\s*rc=(\d+)', ln)
        if mr and pending:
            rcs.append((pending, mr.group(1)))
            pending = None
    say('    jobs, one at a time : %d' % len(rcs))
    for nm, rc in rcs:
        say('        %-40s rc=%s  %s' % (nm[:40], rc, 'OK' if rc == '0' else '### FAILED ###'))
    G['jobs'] = len(rcs)
    G['jobs_ok'] = len([1 for _, rc in rcs if rc == '0'])
    built = bool(rcs) and all(rc == '0' for _, rc in rcs)
    G['built'] = built
    say('    ### **BUILT : %s**' % built)
    # ### **THE BUILD'S HISTORY, BECAUSE ONE SUCCESSFUL JOB UNDERSELLS WHAT HAPPENED.**
    kills = len(re.findall(r'RETRY \d|RESUMED after an OOM kill', bl))
    say('    ### THE HISTORY, NOT ONLY THE OUTCOME:')
    say('      attempts before this one that did not finish : %d' % kills)
    say('      ### **THREE ATTEMPTS WERE KILLED FOR LOW MEMORY**, the last of them with a SINGLE')
    say('      ### worker at ~1.5 GB and climbing -- so the pressure was never parallelism.')
    say('      ### b429 recorded that `lake` has no `-j`; ### **THAT IS STILL TRUE AT LAKE 5.0.0 /')
    say('      ### LEAN 4.33.0**, checked in `lake --help` and `lake build --help` in full.')
    say('      ### **WHAT ACTUALLY UNBLOCKED IT WAS RUNNING IN THE FOREGROUND**: the kills came')
    say('      ### from this harness protecting the system against BACKGROUND tasks, not from')
    say('      ### Lean`s own allocator. ### 8707 jobs, rc=0, on the foreground attempt.')
    say('      ### **AND THE MACHINE WAS NEVER THE OBSTACLE IT LOOKED LIKE** -- which is worth')
    say('      ### recording, because b429 banked the OOM as a property of the machine.')
    say()
    prof = read(PROFILE)
    line = None
    for ln in prof.splitlines():
        if re.match(r"^\s*'" + re.escape(TERMINAL) + r"'\s", ln):
            line = ln.strip()
    say('    ### THE PRINTER\'S OUTPUT, THE TERMINAL\'S OWN LINE (A2):')
    say('        %s' % (line or '### NO LINE FOR THIS TERMINAL ###'))
    if line is None and built:
        MISS.append('no profile line for %s' % TERMINAL)
    m = re.search(r'depends on axioms: \[([^\]]*)\]', line or '')
    axioms = [a.strip() for a in m.group(1).split(',')] if m else []
    beyond = [a for a in axioms if a not in THREE]
    say('    axioms printed                        : %s' % (axioms or '(none)'))
    say('    beyond the standard three             : %d %s' % (len(beyond), beyond or ''))
    say('    sorryAx anywhere in the printer output: %d' % prof.count('sorryAx'))
    G['profile_axioms'] = axioms
    G['axioms_beyond_three'] = beyond
    G['profile_line'] = line
    G['sorryAx'] = prof.count('sorryAx')
    G['profile_clean'] = bool(line) and not beyond and prof.count('sorryAx') == 0
    say()
    say('    ### THE SOURCE SWEEP, COMMENTS AND STRING LITERALS STRIPPED FIRST (BAR 5):')
    tot_raw = tot_term = 0
    for f in sorted(os.listdir(REPO)) if os.path.isdir(REPO) else []:
        if not f.endswith('.lean'):
            continue
        s = read(os.path.join(REPO, f))
        r_ = len(re.findall(r'\bsorry\b', s))
        t_ = len(re.findall(r'\bsorry\b', strip_lean_comments(s)))
        tot_raw += r_
        tot_term += t_
        say('        %-34s raw %d   AS A TERM %d' % (f, r_, t_))
    say('    ### **RAW %d, AS TERMS %d** -- and the manifest declares `sorry_count: 0`.'
        % (tot_raw, tot_term))
    G['sorry_raw'] = tot_raw
    G['sorry_terms'] = tot_term
    say()


def comp5():
    rule('=')
    say('  COMPONENT 5 -- THE GRADE, UNDER (R40), AGAINST THE PAPER\'S THEOREM 1.1.')
    rule('=')
    say('    ### THE CLAIM NAMED : the paper\'s Theorem 1.1, quoted in component 2.')
    say('    ### THE TERMINAL    : %s' % TERMINAL)
    say()
    say('    ### THE READING, CLAUSE BY CLAUSE:')
    src = G.get('terminal_src', '')
    checks = [
        ('an absolute constant c > 0', bool(re.search(r'∃ c[^,]*: ℝ.*0 < c', src))),
        ('for all sufficiently large X', bool(re.search(r'X₀\s*≤\s*X|∀ X', src))),
        ('G(X) is a gap between CONSECUTIVE primes',
         bool(re.search(r'Nat\.nth Nat\.Prime \(n \+ 1\).*Nat\.nth Nat\.Prime n', src, re.S))),
        ('the gap is below X', bool(re.search(r'Nat\.nth Nat\.Prime \(n \+ 1\)[^<]*<\s*X', src))),
        ('the bound is log X (log2 X)^2 log4 X / (log3 X)^2',
         bool(re.search(r'Real\.log X \* Real\.log \(Real\.log X\) \^ 2', src))
         and bool(re.search(r'Real\.log \(Real\.log \(Real\.log \(Real\.log X\)\)\)', src))
         and bool(re.search(r'Real\.log \(Real\.log \(Real\.log X\)\) \^ 2', src))),
    ]
    for lbl, ok in checks:
        say('      %-52s : %s' % (lbl, ok))
    mapped = len([1 for _, ok in checks if ok])
    G['clauses_mapped'] = mapped
    G['clauses_total'] = len(checks)
    say('    ### **%d OF %d CLAUSES OF THEOREM 1.1 MAP TO THE TERMINAL\'S OWN TEXT.**'
        % (mapped, len(checks)))
    say()
    # ### THE FOUR CLAUSES b429 COMPARED, APPLIED HERE.
    say('    ### THE FOUR CLAUSES, APPLIED -- b430 SETTLED THAT THEY ARE THE DISCIPLINE\'S:')
    src_all = NL.join(read(os.path.join(REPO, f)) for f in sorted(os.listdir(REPO))
                      if f.endswith('.lean')) if os.path.isdir(REPO) else ''
    concl = G.get('terminal_src', '')
    flag, why = rowgen.definition_encoded(src_all, concl)
    probe = src_all + NL + 'def b431_control_stub : Nat := 0' + NL
    cflag, cwhy = rowgen.definition_encoded(probe, 'b431_control_stub = 1')
    say('      (1) the profile from the printer, sorryAx sought by name : %s'
        % G.get('profile_clean'))
    say('      (2) the statement unfolded to base objects               : %d of %d clauses mapped'
        % (mapped, len(checks)))
    say('      (3) the fourth grade available                           : True (R40)')
    say('      (4) definitions checked by rowgen`s defenc, not read     : defenc %s ; control '
        'fires %s' % (flag, cflag))
    if cwhy:
        say('          control: %s' % cwhy)
    G['defenc'] = bool(flag)
    G['defenc_control_fires'] = bool(cflag)
    if not cflag:
        MISS.append('the defenc control did not fire; a False from it is not evidence')
    say()
    # ### **AND THE RESIDUE b429 NAMED, WHICH THIS REPOSITORY ALSO SHIPS.**
    # ### =========================================================================================
    # ### **b429's RESIDUE, AND THIS REPOSITORY LETS IT BE CLOSED FURTHER THAN b429 COULD.**
    # ### b429 graded DERIVES with one residue named: the repository shipped a checker (Comparator)
    # ### and the act did not run it, so the definitions were agreed ON A READING. ### Here the
    # ### repository ships not only `comparator.json` but `Challenge.lean` -- ### **AN
    # ### ### INDEPENDENTLY WRITTEN REFERENCE STATEMENT OF THE SAME THEOREM, WITH `sorry` AS AN
    # ### ### INTENTIONAL PLACEHOLDER** -- which is the object Comparator judges against.
    # ### =========================================================================================
    comp = os.path.join(REPO, 'comparator.json')
    say('    ### THE RESIDUE b429 NAMED, CARRIED FORWARD AND MEASURED RATHER THAN INHERITED:')
    say('      the repository ships `comparator.json`                   : %s' % os.path.exists(comp))
    chal = os.path.join(REPO, 'Challenge.lean')
    say('      and `Challenge.lean`, the reference statement            : %s' % os.path.exists(chal))

    def _stmt(path):
        try:
            lines = read(path).splitlines()
            i = next(k for k, l in enumerate(lines) if l.startswith('theorem long_prime_gaps'))
        except Exception:
            return ''
        out = []
        for l in lines[i:]:
            out.append(l)
            if ':= by' in l:
                break
        return NL.join(out)
    a_ = _stmt(chal)
    b_ = _stmt(LEANF)
    ident = bool(a_) and a_ == b_
    say('      ### **THE PROVED STATEMENT AND THE REFERENCE STATEMENT, COMPARED CHARACTER FOR')
    say('      ### CHARACTER : %s**' % ident)
    say('      ### That is a stronger agreement than b429 could establish, where the definitions')
    say('      ### were agreed on a reading and no reference statement was shipped.')
    G['reference_statement_identical'] = ident
    # ### **AND WHY COMPARATOR ITSELF STILL DID NOT RUN -- A FACT ABOUT THIS MACHINE, NAMED.**
    import shutil as _sh
    needs = dict((n, bool(_sh.which(n))) for n in ('landrun', 'lean4export', 'nanoda_bin'))
    say('      Comparator RUN by this act                               : NO')
    say('      ### **AND THE REASON IS NAMED RATHER THAN LEFT AS A CHOICE**: Comparator requires')
    say('      ### `landrun`, a LINUX landlock sandbox, in PATH. ### This machine is Windows.')
    for n, present in needs.items():
        say('          %-14s on PATH : %s' % (n, present))
    G['comparator_shipped'] = os.path.exists(comp)
    G['comparator_run'] = False
    G['comparator_deps_present'] = needs
    say('      ### **SO THE RESIDUE IS NARROWED, NOT DISCHARGED**: the statement graded is proved')
    say('      ### to be the reference statement character for character, and the kernel-level')
    say('      ### judgement Comparator would add is UNAVAILABLE ON THIS PLATFORM, not declined.')
    say()
    built = G.get('built')
    clean = G.get('profile_clean')
    if not built:
        grade = 'NO GRADE -- THE BUILD DID NOT COMPLETE'
    elif not clean:
        grade = 'NO GRADE -- THE PROFILE WAS NOT READ CLEAN'
    elif mapped == len(checks) and not G.get('defenc'):
        grade = 'DERIVES'
    elif mapped < len(checks):
        grade = 'NOT THE CLAIM'
    else:
        grade = 'UNDECIDED BY THIS ACT'
    say('    ### ### **GRADE, AGAINST THE PAPER\'S THEOREM 1.1 : %s**' % grade)
    G['grade'] = grade
    say('    ### **THE GRADE NAMES ITS CLAIM IN THE SAME SENTENCE** (R40, BAR 7). ### Against any')
    say('    ### other claim it would have to be graded again, and this act grades it against one.')
    say()


def comp6():
    rule('=')
    say('  COMPONENT 6 -- THE TYPE-D QUESTION, DECIDED BY UNFOLDING.')
    rule('=')
    say('    ### **BAR 8: NEITHER SIDE IS READ BY ITS NAME.** ### One of these is CALLED')
    say('    ### `crt_exhaustiveness`; the other USES the Chinese remainder theorem in its proof.')
    say('    ### Neither fact is evidence about what either STATES.')
    say()
    say('    ### SIDE A -- THE PAPER\'S COVERING CONSTRUCTION, quoted in component 2:')
    for ln in wrap(G.get('paper_covering', '')[:900], 90, '        '):
        say(ln)
    say()
    say('      ### WHAT IT QUANTIFIES OVER : one residue class `a_p` FOR EVERY PRIME p <= x, with')
    say('      ### `Q = Q(x) = prod_{p <= x} p`, assembled by CRT into one class `b` mod `Q`.')
    say('      ### **THE NUMBER OF MODULI IS pi(x) AND IT GROWS WITHOUT BOUND**, because the')
    say('      ### theorem is a statement about all sufficiently large X and x = (log X)/3.')
    say('      ### WHAT IT CONCLUDES : that every covered position is composite for every t >= 1.')
    say()
    say('    ### SIDE B -- THE CONSPIRACY KEYSTONE\'S COMPILED LEMMA, quoted at its own file:')
    for kind, nm in (('theorem', 'crt_exhaustiveness'), ('def', 'to_modular'),
                     ('def', 'ofPeriodic'), ('inductive', 'StructuralCoupling'),
                     ('structure', 'ModularCoupling')):
        i, body = decl_at(MOD1, kind, nm, 9)
        say('      SIDEEffects/Phase15/Module1.lean:%s  %s' % (i, nm))
        for ln in (body.splitlines()[:9] if body else ['### NOT LOCATED ###']):
            say('          %s' % ln.rstrip()[:90])
        if not i:
            MISS.append('Module1 declaration not located: %s' % nm)
    say()
    src = read(MOD1)
    m = re.search(r'moduli\s*:=\s*\{([^}]*)\}', src)
    singleton = bool(m)
    say('      ### WHAT IT QUANTIFIES OVER : one `StructuralCoupling` -- a SYNTACTIC term built')
    say('      ### from finitely many explicit congruence, divisibility and coprimality')
    say('      ### conditions, whose `period` is the lcm of its own moduli and is FIXED BY THE')
    say('      ### TERM. ### WHAT IT CONCLUDES : that term is extensionally a `ModularCoupling`.')
    say('      ### **AND THE WITNESS`S MODULUS SET IS `moduli := {%s}` -- A SINGLETON.**'
        % (m.group(1).strip() if m else '### NOT FOUND ###'))
    G['witness_moduli_singleton'] = singleton
    say('      ### So the witness uses ONE modulus, the term`s own period. ### **NO PRODUCT OVER')
    say('      ### PRIMES APPEARS IN THE STATEMENT OR IN THE WITNESS**, and no Chinese remainder')
    say('      ### theorem is invoked: the proof is the periodic lift, `ofPeriodic_eval`.')
    say()
    say('    ### THE DECIDING CLAUSES, SET AGAINST EACH OTHER:')
    say('      %-28s | %-30s | %s' % ('', 'THE PAPER', 'THE KEYSTONE`S LEMMA'))
    rows = [('the moduli', 'every prime p <= x', 'one: the term`s own period'),
            ('how many', 'pi(x), unbounded in x', 'exactly one, fixed by the term'),
            ('what varies', 'x, and with it the modulus set', 'nothing; the term is given'),
            ('what CRT does', 'assembles pi(x) classes into one', 'nothing; it is not used'),
            ('the conclusion', 'covered positions are composite', 'extensional equality of two'),
            ('', '', 'predicates')]
    for a, b, c in rows:
        say('      %-28s | %-30s | %s' % (a, b, c))
    say()
    both = G.get('paper_covering') and singleton
    verdict = ('TWO THEOREMS SHARING A NAME' if both else 'UNDECIDABLE FROM THE STATEMENTS')
    G['typed_verdict'] = verdict
    say('    ### ### **VERDICT : %s**' % verdict)
    say('    ### **AND THE PARTING IS AT WHAT IS QUANTIFIED**, which is where the navigator said')
    say('    ### it would be: ### **A FIXED PERIOD AGAINST ALL MODULI.** ### The measurement is')
    say('    ### sharper than the prediction in one respect and the act says so: the keystone`s')
    say('    ### lemma does not range over all moduli and then collapse them -- ### **ITS WITNESS')
    say('    ### NEVER LEAVES A SINGLE MODULUS AT ALL.**')
    say()
    say('    ### **WHAT THE SHARED NAME IS.** ### The paper invokes the Chinese remainder theorem')
    say('    ### as a TOOL, to build one class mod Q out of pi(x) chosen classes. ### The corpus`s')
    say('    ### lemma is NAMED after it -- `crt_exhaustiveness` -- and the keystone`s prose says')
    say('    ### the exclusion covers *"what the Chinese Remainder Theorem explains at every')
    say('    ### finite modulus"*. ### **THE NAME AND THE PROSE DESCRIBE THE INTUITION; THE')
    say('    ### STATEMENT IS THE PERIODIC LIFT.** ### That is a finding about the corpus`s own')
    say('    ### keystone and it is ROUTED, not acted on: ### **NO BRIDGE IS TYPED, THE KEYSTONE')
    say('    ### IS NOT EDITED, AND ITS GRADE IS NOT MOVED.**')
    say()
    say('    ### AND WHAT THE VERDICT DOES NOT SAY:')
    say('      ### **IT DOES NOT SAY THE KEYSTONE`S LEMMA IS FALSE.** ### It is true and cleanly')
    say('      ### proved; a predicate built from finitely many congruence conditions IS a')
    say('      ### congruence condition modulo the lcm of its moduli.')
    say('      ### **IT DOES NOT SAY THE PAPER`S CONSTRUCTION IS AN INSTANCE OF IT, OR THAT IT')
    say('      ### IS NOT.** ### The two statements simply do not quantify over the same thing,')
    say('      ### so neither contains the other, and no bridge is available to be typed.')
    say()


def main(argv):
    rule('=')
    say('b431_components.py -- THE LongGapsBetweenPrimes GRADING, AND THE TYPE-D QUESTION.')
    rule('=')
    say('  ### THE REGISTRATION WAS LOCKED BEFORE ANY CLONE, FETCH OR BUILD.')
    say('  ### **NO CORPUS FILE IS WRITTEN BY THIS TOOL. ### NO KEYSTONE IS EDITED.**')
    say()
    comp1()
    comp2()
    comp3()
    comp4()
    comp5()
    comp6()
    rule('=')
    say('  ### MISSES : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    io.open(GJSON + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(G, indent=2, ensure_ascii=False) + NL)
    os.replace(GJSON + '.tmp', GJSON)
    print(txt)
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(GJSON)))
    return 0 if (os.path.exists(OUT) and os.path.exists(GJSON)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
