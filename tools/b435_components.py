# -*- coding: utf-8 -*-
"""b435_components.py -- ### **THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES.**

### ### **COMPONENT 1** ### b314's handler quoted at its own file and line, extracted to
### `tools/force_rm.py` with fixtures in both polarities, and the ten call sites named -- each
### repointed or left, with one line of reason. ### The guards are on their own rows.
### ### **COMPONENT 2** ### the pre-push guard's report made to say SKIPPED with its reason;
### fixtures for all three states; then a sweep, BY DESCRIPTION, for other skips that print like
### passes -- counted, and repaired only where the repair is the same one line.
### ### **COMPONENT 3** ### the census of single-tool environmental handlers, with a positive
### control that must find b314's. ### **IT REPAIRS NOTHING.**
"""
import ast
import hashlib
import io
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import force_rm             # noqa: E402

T = os.path.join(ROOT, 'tools')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
MISS = []


def rec(s=''):
    LINES.append(s)
    print(s)


def head(n, title):
    rec('')
    rec('-' * 100)
    rec('  ### (%d) %s' % (n, title))
    rec('-' * 100)


def sha(path):
    return hashlib.sha256(io.open(path, 'rb').read()).hexdigest()


def src(path):
    return io.open(path, encoding='utf-8', errors='replace').read()


# ### **THE PRE-ACT BLOBS, PINNED BEFORE ANY WRITE** -- b433's lesson: when a repair misbehaves,
# ### a digest taken beforehand is what proves the restore was exact.
TOUCH = ['b257_checks.py', 'b372_eol.py', 'b304_hooks.py']
PRE = {f: sha(os.path.join(T, f)) for f in TOUCH}
PREBYTES = {f: io.open(os.path.join(T, f), 'rb').read() for f in TOUCH}


# ----------------------------------------------------------------------------------------------
# ### THE TEN SITES. ### **NAMED HERE, WITH THE CALL AND ITS REASON, BEFORE ANYTHING IS TOUCHED.**
# ----------------------------------------------------------------------------------------------
# ### **THE RULE THE FACE STATES, APPLIED:** ### a site is REPOINTED if its tree can contain a
# ### `.git` directory when it is removed -- that is the only way it holds files git marks
# ### read-only. ### A site is LEFT if every file in its tree was written by that tool with default
# ### permissions, so the only failure mode is a leaked temporary directory and no verdict depends
# ### on the removal. ### **AND WHERE THE DECISIVE FACT SITS IN A CALLED FUNCTION, THE REASON NAMES
# ### THE CALLEE**, so a reader can check the call without trusting this seat.
SITES = [
    ('b257_checks.py', 65, 'GIT-BEARING', False,
     'the tree is `git -C d init`-ed and `add -A`-ed in this same function (lines 58-61), so '
     '`.git/objects` holds blobs git marks read-only'),
    ('b372_eol.py', 123, 'GIT-BEARING', False,
     '`repo` under `tmp` is `git init`-ed, configured, added and committed in `polarity_fixture` '
     '(lines 105-116) -- a real object store, read-only by the time it is removed'),
    ('b372_eol.py', 251, 'PLAIN', True,
     'the tree holds only what `fresh_checkout` wrote, and THE CALLEE USES `git checkout-index '
     '--prefix` (line 84) -- blobs only, no `.git` directory is ever created there'),
    ('b376_lockgate.py', 93, 'PLAIN', True,
     'the fixture writes plain text gate records into `tmp` with `io.open` (lines 84-89) and '
     'creates no repository'),
    ('b378_lockgate.py', 139, 'PLAIN', True,
     'the fixture writes plain text gate records into `tmp` and creates no repository'),
    ('b386_components.py', 422, 'PLAIN', True,
     'the fixture writes backup files the tool itself creates; no repository is initialised'),
    ('gate_hash.py', 115, 'PLAIN', True,
     'the fixture writes a synthetic gate record and a synthetic subject file; no repository'),
    ('repair_snapshot.py', 246, 'PLAIN', True,
     'the sandbox is built by `copytree` of `tools/` and `.githooks/` ONLY (lines 211-214) -- '
     'THE CALLEE NEVER COPIES `.git`, so no read-only object can reach it'),
    ('repair_snapshot.py', 344, 'PLAIN', True,
     'the toy root holds only files the fixture wrote itself -- `tools/toy_in.py`, '
     '`data/out.txt`, `.githooks/pre-push`'),
    ('repair_snapshot.py', 345, 'PLAIN', True,
     'the far root holds only the `.githooks/pre-push` the fixture wrote itself'),
]
GUARD_FILES = {'b376_lockgate.py', 'b378_lockgate.py', 'gate_hash.py'}

# ### **THE REPOINTS, AS EXACT TEXT.** ### Each anchor is unique in its file and is checked to be.
REPOINTS = [
    ('b257_checks.py',
     'from check_harness import Harness, contains   # noqa: E402',
     'from check_harness import Harness, contains   # noqa: E402\nimport force_rm   # noqa: E402',
     'import force_rm   # noqa: E402'),
    ('b257_checks.py',
     '    finally:\n        shutil.rmtree(d, ignore_errors=True)',
     '    finally:\n        force_rm.rmtree(d)',
     '        force_rm.rmtree(d)'),
    ('b372_eol.py',
     'import b303_pins            # noqa: E402',
     'import b303_pins            # noqa: E402\nimport force_rm             # noqa: E402',
     'import force_rm             # noqa: E402'),
    ('b372_eol.py',
     "                          equal=(blob is not None and got is not None and blob == got))\n"
     "        shutil.rmtree(tmp, ignore_errors=True)",
     "                          equal=(blob is not None and got is not None and blob == got))\n"
     "        force_rm.rmtree(tmp)",
     '        force_rm.rmtree(tmp)'),
]


def apply_repair(fname, old, new, already):
    """### **IDEMPOTENT BY THE NEW TEXT, NOT BY THE ANCHOR'S ABSENCE** (b433's defect, corrected).

    ### Returns one of APPLIED / ALREADY / ### **NOT LOCATED** / ### **AMBIGUOUS**.
    """
    p = os.path.join(T, fname)
    txt = src(p)
    if already in txt:
        return 'ALREADY'
    n = txt.count(old)
    if n == 0:
        MISS.append('%s : anchor NOT LOCATED' % fname)
        return '### NOT LOCATED'
    if n > 1:
        MISS.append('%s : anchor matches %d times' % (fname, n))
        return '### AMBIGUOUS'
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(txt.replace(old, new))
    return 'APPLIED'


def restore(fname):
    io.open(os.path.join(T, fname), 'wb').write(PREBYTES[fname])


# ----------------------------------------------------------------------------------------------
def ruling():
    head(0, "THE RULING THIS ACT EXECUTES, ### **QUOTED FROM THE BANKED PASTE.**")
    ferry = src(os.path.join(D, 'b435_ferry.txt'))
    m = re.search(r'RULING \(R46\).*?It closes at this act.s end\.', ferry, re.S)
    if not m:
        rec('    ### ### **THE RULING WAS NOT LOCATED IN THE BANKED PASTE.**')
        MISS.append('ruling : (R46) not located in b435_ferry.txt')
        return False
    for ln in m.group(0).splitlines():
        rec('      | %s' % ln)
    rec('')
    rec('    ### ### **A CURE THAT LIVES IN ONE TOOL IS NOT A GUARD** -- the ruling`s own words,')
    rec('    ### and this act executes them and does not extend them. ### The extraction it orders')
    rec('    ### is Component 1; the census it orders is Component 3; ### **AND THE CENSUS REPAIRS')
    rec('    ### ### NOTHING**, because the ruling governs what happens to the rest GOING FORWARD.')
    return True


def component_1():
    head(1, "THE HANDLER `b314` ALREADY HAD, QUOTED AT ITS OWN FILE AND LINE.")
    p = os.path.join(T, 'b314_coldclone.py')
    body = src(p).splitlines()
    rec('    tools/b314_coldclone.py, lines 47-50 -- ### **VERBATIM, NOT PARAPHRASED:**')
    rec('')
    for i in range(46, 50):
        rec('      %3d | %s' % (i + 1, body[i]))
    rec('')
    rec('    its one call site in that file  : line 149, `shutil.rmtree(clone, onerror=_force_rm)`')
    rec('    ### ### **WRITTEN AT b314. ### NEVER SHARED. ### REINVENTED AT b433, NINETEEN ACTS'
        ' LATER.**')

    head(2, "THE EXTRACTION: `tools/force_rm.py`, AND ITS FIXTURES IN BOTH POLARITIES.")
    ok, fx = force_rm.self_test(False)
    for ln in fx:
        rec(ln)
    rec('    ### ### **FIXTURE VERDICT : %s**' % ('HELD' if ok else 'NOT HELD'))
    rec('')
    rec('    ### **THE SECOND POLARITY IS THE ONE THAT MATTERS.** ### A helper that swallowed every')
    rec('    ### error would pass the read-only fixture and be WORSE than the bare call it replaced.')
    rec('    ### And the CONTROL above is why the first fixture means anything: the bare `rmtree` was')
    rec('    ### shown to REFUSE that same tree, so the cure is what removed it.')
    if not ok:
        rec('    ### ### **THE EXTRACTION IS REFUSED AND NO SITE IS REPOINTED** -- the face fixed'
            ' this.')
        return False
    return True


def component_1_sites():
    head(3, "THE TEN CALL SITES. ### EACH NAMED, EACH WITH ITS CALL AND ITS REASON.")
    rec('    ### **THE RULE, STATED ON THE LOCKED FACE AND APPLIED HERE WITHOUT EXCEPTION:**')
    rec('    ### REPOINT a site whose tree CAN CONTAIN A `.git` DIRECTORY when it is removed --')
    rec('    ### that is the only way it holds files git marks read-only.')
    rec('    ### LEAVE a site every file of whose tree the tool wrote itself with default')
    rec('    ### permissions: the only failure mode is a leaked temporary directory, and')
    rec('    ### **NO VERDICT DEPENDS ON THE REMOVAL.**')
    rec('    ### ### **THREE MECHANICAL RULES WERE TRIED IN THE SURVEY AND EACH MIS-SORTED A SITE.**')
    rec('    ### So the survey prints evidence and classifies nothing, and ### **THE CALL BELOW IS')
    rec('    ### ### THE SEAT`S, MADE ON THAT EVIDENCE, AND IS SAID TO BE RATHER THAN DRESSED AS A')
    rec('    ### ### MEASUREMENT.** ### A derivation that keeps changing its answer is not one.')
    rec('')
    ordinary = [s for s in SITES if s[0] not in GUARD_FILES]
    guards = [s for s in SITES if s[0] in GUARD_FILES]
    for title, group in (('THE SEVEN ORDINARY SITES, IN FOUR TOOLS', ordinary),
                         ('### **THE THREE GUARD SITES, ON THEIR OWN ROWS** -- they decide '
                          'whether an act may seal', guards)):
        rec('    %s' % title)
        for fname, line, kind, left, why in group:
            rec('      %-22s %-5d %-12s %s'
                % (fname, line, kind, 'LEFT AS WRITTEN' if left else 'REPOINTED'))
            for chunk in wrap(why, 84):
                rec('          %s' % chunk)
        rec('')
    rec('    ### ### **GIT-BEARING : %d   ### LEFT AS WRITTEN : %d   ### TOTAL : %d**'
        % (sum(1 for s in SITES if not s[3]), sum(1 for s in SITES if s[3]), len(SITES)))
    rec('    ### **THE GUARDS ARE REPORTED SEPARATELY AND ARE NOT FOLDED INTO A TOTAL** -- a line')
    rec('    ### that moves inside an instrument deciding whether an act may seal is not one line')
    rec('    ### among ten. ### **ALL THREE ARE LEFT, SO NO GATE CHANGED A BYTE.**')

    head(4, "THE REPOINTS, APPLIED AND MEASURED AGAINST THE PRE-ACT BLOB.")
    results = []
    for fname, old, new, already in REPOINTS:
        r = apply_repair(fname, old, new, already)
        results.append((fname, already.strip(), r))
        rec('    %-22s %-38s %s' % (fname, already.strip()[:38], r))
    bad = [r for r in results if r[2].startswith('###')]
    rec('')
    for fname in ('b257_checks.py', 'b372_eol.py'):
        p = os.path.join(T, fname)
        rec('    %-22s pre %s  ->  post %s   delta %+d bytes'
            % (fname, PRE[fname][:12], sha(p)[:12],
               len(io.open(p, 'rb').read()) - len(PREBYTES[fname])))
    if bad:
        for fname in ('b257_checks.py', 'b372_eol.py'):
            restore(fname)
        rec('    ### ### **A REPOINT DID NOT LAND; BOTH FILES RESTORED FROM THE PINNED BLOB.**')
        return False
    return True


def component_1_exercise():
    head(5, "THE REPOINTED TOOLS, EXERCISED -- ### **BEHAVIOUR UNCHANGED EXCEPT THE SILENT SKIP.**")
    rec('    ### The two repointed FUNCTIONS are called directly rather than their suites run, so')
    rec('    ### this act exercises the changed line WITHOUT writing a file its list does not name.')
    rec('')
    good = True

    import importlib
    try:
        m257 = importlib.import_module('b257_checks')
        rc_neg = m257.hook_verdict(None, True)
        rc_pos = m257.hook_verdict(None, False)
        v = (rc_neg != 0 and rc_pos == 0)
        rec('    b257_checks.hook_verdict   foreign staged -> rc %s ; clean -> rc %s   ### **%s**'
            % (rc_neg, rc_pos, 'SAME VERDICTS AS BEFORE' if v else '### CHANGED ###'))
        good = good and v
    except Exception as e:                                       # noqa: BLE001
        rec('    ### b257_checks.hook_verdict RAISED : %s' % str(e)[:120])
        good = False

    try:
        m372 = importlib.import_module('b372_eol')
        res = m372.polarity_fixture()
        v = bool(res) and all(isinstance(x, dict) for x in res.values())
        rec('    b372_eol.polarity_fixture  %s   ### **%s**'
            % ({k: val.get('equal') for k, val in res.items()},
               'RAN AND RETURNED ITS FIXTURE' if v else '### CHANGED ###'))
        good = good and v
    except Exception as e:                                       # noqa: BLE001
        rec('    ### b372_eol.polarity_fixture RAISED : %s' % str(e)[:120])
        good = False

    rec('')
    rec('    ### ### **AND THE THING THE REPOINT ACTUALLY BUYS:** ### both trees are `git init`-ed,')
    rec('    ### so both previously left a read-only object store on disk and said nothing. ### They')
    rec('    ### now remove it, and ### **RAISE IF THEY CANNOT** -- which is the silent skip, cured.')
    return good


def wrap(s, n):
    """### **AT WORD BOUNDARIES, NEVER MID-TOKEN** (BAR 10)."""
    out, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


# ----------------------------------------------------------------------------------------------
HOOK_OLD = """        if r.get('skipped'):
            # ### **A SKIP IS NOT A PASS AND IS NOT A FAILURE OF THE GUARD.** ### It is this tool
            # ### refusing to put uncommitted work on a throwaway branch, and it counts as a FAILURE of
            # ### the RUN so nobody reads a skipped exercise as an exercised one.
            fails += 1
            print('  %-22s ### **SKIPPED -- %s. ### THE GUARD IS NOT EXERCISED HERE.**'
                  % (name, r['reason']))"""

HOOK_NEW = """        if r.get('skipped'):
            # ### **A SKIP IS NOT A PASS AND IS NOT A FAILURE OF THE GUARD.** ### It is this tool
            # ### refusing to put uncommitted work on a throwaway branch.
            # ### ### **CORRECTED AT b435.** ### It used to be counted into `fails` -- which kept it
            # ### out of the PASS column at the price of putting it in the FAIL column, so the one
            # ### number a reader quotes said FAILING where nothing had failed. ### **A SKIP IS NOW
            # ### ### ITS OWN COUNT, AND THE VERDICT LINE NAMES ALL THREE STATES**, so no table can
            # ### show a skip as either a pass or a failure. ### (R46)'s sortie, Component 2.
            skips += 1
            print('  %-22s ### **SKIPPED -- %s. ### THE GUARD IS NOT EXERCISED HERE.**'
                  % (name, r['reason']))"""

HOOK_TAIL_OLD = """    print()
    print('  ### REPOS FAILING : %d' % fails)"""

HOOK_TAIL_NEW = """    print()
    print('  ### REPOS FAILING : %d' % fails)
    print('  ### REPOS SKIPPED : %d' % skips)
    # ### **THE ONE LINE A READER IS MEANT TO QUOTE, AND IT CANNOT SHOW A SKIP AS A PASS** (A2).
    print('  ### ### **VERDICT : %s -- %d FAILING, %d SKIPPED, %d EXERCISED AND PASSING**'
          % ('GUARD EXERCISED AND PASSING' if (fails == 0 and skips == 0) else
             ('### NOT FULLY EXERCISED' if fails == 0 else '### GUARD FAILING'),
             fails, skips, exercised))"""


def component_2():
    head(6, "COMPONENT 2 -- ### **THE SKIP THAT PRINTS LIKE A PASS.**")
    p = os.path.join(T, 'b304_hooks.py')
    rec('    the subject : tools/b304_hooks.py, the pre-push guard`s exercise.')
    rec('    ### **THE DEFECT, IN ITS OWN WORDS:** ### the per-repository row already SAYS SKIPPED')
    rec('    ### with its reason -- and then `fails += 1` folds that state into the one number the')
    rec('    ### closing tables quote. ### **SO THE SAME `1` READS AS A FAILURE IN ONE TABLE AND AS')
    rec('    ### ### AN EXERCISED GUARD IN ANOTHER**, and neither reader is wrong about what it says.')
    rec('')
    txt = src(p)
    steps = [
        ('the skip gets its own count, not the failure count', HOOK_OLD, HOOK_NEW, 'skips += 1'),
        ('the totals name all three states', HOOK_TAIL_OLD, HOOK_TAIL_NEW, 'REPOS SKIPPED'),
        ('the counters are initialised', '    fails = 0\n',
         '    fails = 0\n    skips = 0\n    exercised = 0\n', '    skips = 0\n'),
        ('an exercised repository is counted as exercised',
         "        fails += 0 if good else 1\n",
         "        exercised += 1 if good else 0\n        fails += 0 if good else 1\n",
         'exercised += 1 if good else 0'),
        # ### **AND THE EXIT CODE, WHICH TAKING THE SKIP OUT OF `fails` WOULD OTHERWISE BREAK.**
        # ### Before this act a skip returned `1`: wrong word, right refusal. ### Moving it out of
        # ### the failure count would have made a WHOLLY SKIPPED RUN RETURN `0` -- ### **A TOOL
        # ### ASKED NOT TO COMPLAIN REPORTING A SUCCESS IT DID NOT EARN**, b434's own species,
        # ### which this act would have MINTED while curing. ### Three codes, so a caller testing
        # ### `rc == 0` still refuses a skip and a caller can tell it from a failure.
        ('the exit code cannot say 0 on a skipped run',
         "    return 0 if fails == 0 else 1\n",
         "    return 0 if (fails == 0 and skips == 0) else (1 if fails else 2)\n",
         'return 0 if (fails == 0 and skips == 0)'),
    ]
    okall = True
    for label, old, new, already in steps:
        txt = src(p)
        if already in txt:
            rec('    %-52s ALREADY' % label)
            continue
        n = txt.count(old)
        if n != 1:
            rec('    %-52s ### %s' % (label, 'NOT LOCATED' if n == 0 else 'AMBIGUOUS (%d)' % n))
            MISS.append('b304_hooks.py : %s matched %d times' % (label, n))
            okall = False
            continue
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(txt.replace(old, new))
        rec('    %-52s APPLIED' % label)
    rec('')
    rec('    b304_hooks.py  pre %s -> post %s   delta %+d bytes'
        % (PRE['b304_hooks.py'][:12], sha(p)[:12],
           len(io.open(p, 'rb').read()) - len(PREBYTES['b304_hooks.py'])))
    if not okall:
        restore('b304_hooks.py')
        rec('    ### ### **A STEP DID NOT LAND; THE FILE IS RESTORED FROM ITS PINNED BLOB.**')
        return False
    ok = subprocess.run([sys.executable, '-c',
                         'import ast,io;ast.parse(io.open(%r,encoding="utf-8").read())' % p],
                        capture_output=True)
    rec('    the repaired file parses : %s' % ('yes' if ok.returncode == 0 else
                                               '### NO -- %s' % ok.stderr.decode()[:120]))
    if ok.returncode != 0:
        restore('b304_hooks.py')
        rec('    ### ### **RESTORED FROM THE PINNED BLOB.**')
        return False
    return True


def component_2_fixtures():
    head(7, "THE THREE STATES, EXERCISED. ### **PASS, FAIL, SKIPPED -- EACH DISTINGUISHABLE.**")
    rec('    ### The report`s own summary block is run over three synthetic outcome sets, so the')
    rec('    ### fixture reads THE LINE A READER QUOTES and not the code that produced it.')
    rec('')
    body = src(os.path.join(T, 'b304_hooks.py'))
    m = re.search(r"print\('  ### ### \*\*VERDICT : %s.*?exercised\)\)", body, re.S)
    if not m:
        rec('    ### ### **THE VERDICT LINE WAS NOT FOUND IN THE REPAIRED FILE.**')
        MISS.append('b304_hooks.py : verdict line not found after repair')
        return False
    tmpl = m.group(0)
    rows = []
    for label, fails, skips, exercised in (
            ('all four exercised and passing', 0, 0, 4),
            ('### one repository FAILING', 1, 0, 3),
            ('### four SKIPPED -- the step-zero state', 0, 4, 0),
            ('mixed: one failing, one skipped', 1, 1, 2)):
        buf = []
        exec(compile(tmpl.replace("print(", "buf.append(", 1), '<fx>', 'exec'),
             {'buf': buf, 'fails': fails, 'skips': skips, 'exercised': exercised})
        rows.append((label, buf[0]))
        rec('    %-34s -> %s' % (label, buf[0].strip()))
    verdicts = [r[1] for r in rows]
    distinct = len(set(verdicts)) == len(verdicts)
    skip_row = verdicts[2]
    pass_row = verdicts[0]
    ok = (distinct
          and 'NOT FULLY EXERCISED' in skip_row
          and 'EXERCISED AND PASSING' in pass_row
          and 'GUARD FAILING' in verdicts[1])
    rec('')
    rec('    all four verdict lines distinct                     : %s' % distinct)
    rec('    ### **the SKIPPED state cannot be read as a pass**  : %s'
        % ('NOT FULLY EXERCISED' in skip_row))
    rec('    ### **nor as a failure of the guard**               : %s'
        % ('GUARD FAILING' not in skip_row))
    rec('    ### ### **THREE-STATE FIXTURE VERDICT : %s**' % ('HELD' if ok else 'NOT HELD'))
    return ok


# ----------------------------------------------------------------------------------------------
SKIPWORDS = re.compile(
    r'SKIP|skipped|NOT APPLICABLE|not applicable|NOT EXERCISED|not exercised|'
    r'NOT RUN|not run|cannot be (?:run|exercised)|UNAVAILABLE|unavailable|n/a', re.I)
TOTALWORDS = re.compile(r'FAILING|FAILURES|### FAIL|PASS(?:ING)?\s*:|\bPASSED\b|VERDICT')


def strings_of(path):
    """### **THE TOOL'S OWN PRINTED VOCABULARY -- STRING LITERALS ONLY, COMMENTS DROPPED.**

    ### ### **STRINGS ARE KEPT ON PURPOSE HERE** (BAR 10): what a report SAYS is the evidence, and
    ### a stripper that removed them would leave this arm nothing to read and still let it print a
    ### verdict. ### Comments go, because a comment is not what a reader of the report sees.
    """
    out = []
    try:
        with io.open(path, 'rb') as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.STRING:
                    out.append((tok.start[0], tok.string))
    except Exception:                                            # noqa: BLE001
        return []
    return out


def folded_in(text):
    """### **THE SWEEP'S ONE ARM, OVER ARBITRARY SOURCE** -- so it can be run over the pre-act
    ### bytes as a positive control and over the corpus as the sweep, ### **BY THE SAME CODE.**"""
    hits = []
    try:
        tree = ast.parse(text)
    except Exception:                                            # noqa: BLE001
        return hits
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        for suite in (node.body, node.orelse):
            says_skip = any(isinstance(k, ast.Constant) and isinstance(k.value, str)
                            and SKIPWORDS.search(k.value)
                            for s in suite for k in ast.walk(s))
            if not says_skip:
                continue
            for s in suite:
                for k in ast.walk(s):
                    if (isinstance(k, ast.AugAssign) and isinstance(k.target, ast.Name)
                            and k.target.id in ('fails', 'failures', 'bad', 'errors')
                            and isinstance(k.op, ast.Add)):
                        hits.append(k.lineno)
    return sorted(set(hits))


def component_2_sweep():
    head(8, "THE SWEEP, ### **BY DESCRIPTION** ### -- OTHER SKIPS INDISTINGUISHABLE FROM PASSES.")
    rec('    ### **THE DESCRIPTION, NOT A LIST THIS SEAT TYPED:** ### a tool is a candidate when its')
    rec('    ### own PRINTED VOCABULARY carries a skip-word AND it prints a pass/fail summary -- so')
    rec('    ### a reader of its summary meets a state the rows knew about and the total did not.')
    rec('')
    cands = []
    for fn in sorted(os.listdir(T)):
        if not fn.endswith('.py') or fn.startswith('b435_'):
            continue
        lits = strings_of(os.path.join(T, fn))
        if not lits:
            continue
        skipl = [(ln, s) for ln, s in lits if SKIPWORDS.search(s)]
        totl = [(ln, s) for ln, s in lits if TOTALWORDS.search(s)]
        if skipl and totl:
            cands.append((fn, skipl, totl))
    rec('    tools scanned                                       : %d'
        % len([f for f in os.listdir(T) if f.endswith('.py')]))
    rec('    ### **CANDIDATES -- a skip-word AND a pass/fail summary** : %d' % len(cands))
    rec('')
    rec('    ### **AND THE CANDIDATE SET IS NOT THE FINDING.** ### Most of these print SKIPPED in a')
    rec('    ### row and never total it at all, which is correct as written. ### The finding is the')
    rec('    ### subset where a skip is FOLDED INTO a pass or a fail count -- read by hand below.')
    rec('')
    # ### **PROXIMITY IS NOT CO-BRANCHING.** ### The first version of this arm took any
    # ### `fails += 1` within a few lines of a skip-word -- and its single hit was b304_hooks.py`s
    # ### BYTE-IDENTITY check, four lines above an unrelated print. ### **AN ARM THAT MEASURES
    # ### DISTANCE INSTEAD OF STRUCTURE FINDS NEIGHBOURS, NOT CAUSES.** ### So the branch is read:
    # ### the skip-word and the increment must sit in the SAME `if` body.
    # ### **THE TWO SUITES ARE READ APART** (inside `folded_in`). ### Walking the whole `If` put a
    # ### skip-word in the `else` and an increment in the `if` and called that a fold -- which is
    # ### how `ferry_scan.py:559` was accused of a defect it does not have. ### **A BRANCH IS NOT
    # ### ITS SIBLING**, and an arm that cannot tell them apart is measuring the file, not the code.
    folded = []
    for fn, _skipl, _t in cands:
        for ln in folded_in(src(os.path.join(T, fn))):
            folded.append((fn, ln, 'a failure count'))
    folded = sorted(set(folded))

    # ### **AN EMPTY BUCKET PROVES NOTHING WITHOUT A CONTROL.** ### The same arm is run over
    # ### `b304_hooks.py` AS IT WAS BEFORE THIS ACT TOUCHED IT -- the pinned pre-act bytes. ### If
    # ### it cannot find the defect this act just repaired, ### **THE SWEEP IS BLUNT AND ITS ZERO
    # ### MEANS NOTHING**, and that is said instead of a count.
    ctrl_hits = folded_in(PREBYTES['b304_hooks.py'].decode('utf-8', 'replace'))
    rec('    ### **POSITIVE CONTROL -- the arm over b304_hooks.py AS IT WAS** : %s'
        % ('FOUND the fold at line %d' % ctrl_hits[0] if ctrl_hits else '### NOT FOUND'))
    if not ctrl_hits:
        MISS.append('sweep : the positive control did not find the repaired defect')
        rec('    ### ### **SO NO COUNT IS STATED FOR THE SWEEP.** ### (K) BAR 7`s discipline,')
        rec('    ### applied to this arm as well.')
        return len(cands), None
    rec('')
    rec('    ### ### **SKIPS FOLDED INTO A FAILURE COUNT, BY BRANCH : %d**' % len(folded))
    for fn, ln, what in folded:
        rec('      %-24s line %-5d  `%s` in the same `if` body as a skip-word' % (fn, ln, what))
    if not folded:
        rec('      ### **NONE BEYOND THE ONE THIS ACT REPAIRED.** ### b304_hooks.py matched here')
        rec('      ### before the repair and does not after. ### An empty bucket is reported as')
        rec('      ### plainly as a full one.')
    rec('')
    rec('    ### ### **REPAIRED HERE : 0 FURTHER.** ### The order permits a repair only where it is')
    rec('    ### THE SAME ONE LINE, and no remaining candidate is that. ### **COUNTED AND LEFT : %d**'
        % len(cands))
    rec('    ### and they are left as a COUNT, not as a work item this act pretends to have done.')
    return len(cands), len(folded)


# ----------------------------------------------------------------------------------------------
# ### **THE CENSUS. ### BY DESCRIPTION, WITH A POSITIVE CONTROL.**
MACHINE = [
    ('a read-only tree',       r'read-only|readonly|S_IWRITE|\bchmod\b'),
    # ### **`429` IS BOUNDED AND QUALIFIED.** ### Written bare, it matched inside the act number
    # ### `b429` -- which is precisely the lesson `b429` itself banked, committed here again by the
    # ### arm that was meant to carry it. ### **AN ACT NUMBER MUST NEVER BE REACHABLE INSIDE A
    # ### LARGER TOKEN**, and the cheapest way to keep that true is to demand the qualifier.
    ('a rate limit',           r'rate.?limit|HTTP\s*429|status\s*429|too many requests|'
                               r'Retry-After|back.?off'),
    ('an encoding or an EOL',  r'\bBOM\b|utf-8-sig|autocrlf|\bCRLF\b|line.ending|'
                               r'UnicodeDecodeError|codec'),
    # ### **`lock` ALONE IS A CORPUS WORD IN THIS CORPUS, NOT A MACHINE ONE** -- the registration
    # ### lock and the lock gate are everywhere, and matching the bare word made every checks
    # ### suite look like a handler for a held file. ### The qualifier is demanded here too.
    ('a lock or a held file',  r'being used by another|WinError\s*32|file is locked|'
                               r'locked by another|held open|PermissionError'),
    ('a time limit',           r'\btimeout\b|time limit|TimeoutExpired'),
    ('a memory ceiling',       r'MemoryError|out of memory|\bOOM\b|memory ceiling'),
    ('a path the OS refuses',  r'MAX_PATH|path too long|filename too long'),
]

# ### **A HANDLER IS A ROUTINE, NOT A TOOL.** ### The first widening read comments anywhere inside
# ### a function body, and a four-hundred-line `main` mentioning `autocrlf` in passing became a
# ### "handler for an encoding". ### **A DESCRIPTION IS WHAT A ROUTINE SAYS IT IS FOR, AT ITS TOP**,
# ### and a routine that handles one machine condition is small. ### Both are demanded.
HANDLER_MAX_LINES = 40
HANDLER_HEAD_LINES = 4


def code_only(path):
    """### **CODE WITH COMMENTS AND STRING LITERALS REMOVED** (BAR 10, the arm discipline).

    ### Dots are re-closed, because the tokenizer splits `a.b` into three tokens and a dotted
    ### needle would otherwise never match -- `b430`'s lesson, carried.
    """
    out = []
    prev = None
    try:
        with io.open(path, 'rb') as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type in (tokenize.COMMENT, tokenize.STRING, tokenize.ENCODING):
                    continue
                if tok.type in (tokenize.NEWLINE, tokenize.NL):
                    out.append(chr(10))
                    prev = None
                    continue
                if prev == '.' or tok.string == '.':
                    out.append(tok.string)
                else:
                    out.append(' ' + tok.string)
                prev = tok.string
    except Exception:                                            # noqa: BLE001
        return ''
    return ''.join(out)


def comments_of(path):
    """### **EVERY COMMENT WITH ITS LINE NUMBER**, so a handler's description can be read where
    ### its author actually wrote it rather than only where a docstring was expected."""
    out = []
    try:
        with io.open(path, 'rb') as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.COMMENT:
                    out.append((tok.start[0], tok.string))
    except Exception:                                            # noqa: BLE001
        return []
    return out


COMMENTS = {}


def census():
    head(9, "COMPONENT 3 -- ### **THE SHARED-CURE CENSUS.** ### ONCE, AND IT REPAIRS NOTHING.")
    rec('    ### **THE DESCRIPTION:** ### a routine whose own docstring or heading names a condition')
    rec('    ### of the MACHINE rather than of the corpus -- a read-only tree, a rate limit, an')
    rec('    ### encoding, a lock, a time limit, a memory ceiling, a path the OS refuses -- and that')
    rec('    ### is defined in a single tool and referenced by no other.')
    rec('    ### ### **THE POPULATION IS THE CORPUS AS THIS ACT FOUND IT: A CENSUS MUST NOT'
        ' COUNT THE CENSUS.**')
    rec('    ### This act`s own tools are excluded, and `force_rm.py` -- this act`s ANSWER --'
        ' is')
    rec('    ### reported apart from the findings, below.')
    rec('')
    found = []
    for fn in sorted(os.listdir(T)):
        # ### **THE POPULATION IS THE CORPUS AS THIS ACT FOUND IT.** ### This act's own tools are
        # ### out: a census must not count the census, and `force_rm.py` is this act's answer, not
        # ### one of the findings. ### It is reported below on its own, as evidence the cure landed.
        if not fn.endswith('.py') or fn.startswith('b435_') or fn == 'force_rm.py':
            continue
        p = os.path.join(T, fn)
        COMMENTS[fn] = comments_of(p)
        try:
            tree = ast.parse(src(p))
        except Exception:                                        # noqa: BLE001
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            doc = ast.get_docstring(node) or ''
            # ### **A HANDLER DESCRIBED ONLY IN A COMMENT IS STILL DESCRIBED.** ### b433's own
            # ### removal handler carries a comment and no docstring, so a docstring-only census
            # ### would have missed the very incident that produced (R46).
            lo, hi = node.lineno, getattr(node, 'end_lineno', node.lineno) or node.lineno
            if (hi - lo) > HANDLER_MAX_LINES:
                continue                    # ### a tool, not a handler
            near = [c for ln, c in COMMENTS.get(fn, [])
                    if lo <= ln <= lo + HANDLER_HEAD_LINES]
            desc = doc + chr(10) + chr(10).join(near)
            if not desc.strip():
                continue
            for label, rx in MACHINE:
                m = re.search(rx, desc, re.I)
                if m:
                    first = (doc.strip().splitlines() or near or [''])[0]
                    found.append((fn, node.name, node.lineno, label, m.group(0), first))
                    break

    # ### **THE POSITIVE CONTROL, RUN BEFORE ANY COUNT IS SPOKEN** (BAR 7).
    ctrl = [f for f in found if f[0] == 'b314_coldclone.py' and f[1] == '_force_rm']
    rec('    ### **POSITIVE CONTROL -- it must find b314`s `_force_rm`** : %s'
        % ('FOUND at %s:%d' % (ctrl[0][0], ctrl[0][2]) if ctrl else '### NOT FOUND'))
    if not ctrl:
        rec('    ### ### **THE CENSUS IS VOID AND NO COUNT IS STATED.** ### A census that cannot')
        rec('    ### find the one the order names is not a census. ### (K) BAR 7.')
        MISS.append('census : positive control did not find b314 _force_rm')
        return None
    rec('')

    # ### **"LIVES IN A SINGLE TOOL" IS MEASURED, NOT ASSUMED** -- and ### **A MENTION IS NOT A
    # ### REFERENCE.** ### b434 banked that lesson about call sites and this arm committed it
    # ### anyway: matching the bare name counted THIS ACT'S OWN QUOTATION of `_force_rm` as four
    # ### tools using it, and counted a handler named `blob` as referenced by 282.
    # ### ### **THE TEST IS WHETHER ANOTHER TOOL CAN OBTAIN THE HANDLER** -- `from M import H`,
    # ### or `import M` together with `M.H` -- read from CODE with comments and strings stripped,
    # ### so a quotation cannot vote. ### **AND THIS ACT'S OWN TOOLS ARE EXCLUDED: A CENSUS MUST
    # ### NOT COUNT THE CENSUS.**
    others_src = {fn: code_only(os.path.join(T, fn)) for fn in os.listdir(T)
                  if fn.endswith('.py') and not fn.startswith('b435_') and fn != 'force_rm.py'}
    rows = []
    for fn, name, lineno, label, matched, first in found:
        mod = fn[:-3]
        users = []
        for ofn, otxt in others_src.items():
            if ofn == fn:
                continue
            from_import = re.search(r'from\s+%s\s+import\s+[^\n]*\b%s\b'
                                    % (re.escape(mod), re.escape(name)), otxt)
            dotted = (re.search(r'\bimport\s+%s\b' % re.escape(mod), otxt)
                      and re.search(r'\b%s\s*\.\s*%s\b' % (re.escape(mod), re.escape(name)), otxt))
            if from_import or dotted:
                users.append(ofn)
        rows.append((fn, name, lineno, label, matched, first, users))

    single = [r for r in rows if not r[6]]
    shared = [r for r in rows if r[6]]
    rec('    handlers of a MACHINE condition found, by description : %d' % len(rows))
    rec('    ### ### **OF THOSE, LIVING IN A SINGLE TOOL AND NOWHERE ELSE : %d**' % len(single))
    rec('    referenced from another tool (already shared)        : %d' % len(shared))
    rec('')
    rec('    ### **THE CENSUS, AND WHAT EACH ONE HANDLES:**')
    for fn, name, lineno, label, matched, first, _u in sorted(single):
        rec('      %-24s %-20s line %-5d  %-22s matched on `%s`'
            % (fn, name, lineno, label, matched))
        for chunk in wrap(re.sub(r'^#+\s*', '', first)[:190], 76):
            rec('            %s' % chunk)
    if shared:
        rec('')
        rec('    ### **ALREADY REACHABLE FROM ANOTHER TOOL, SO NOT SINGLE-TOOL** -- and the tools')
        rec('    ### that obtain it are NAMED, so the claim is checkable rather than asserted:')
        for fn, name, lineno, label, _m, _f, u in sorted(shared):
            rec('      %-24s %-20s line %-5d  %-20s used by %s'
                % (fn, name, lineno, label, ', '.join(sorted(u)[:3])
                   + (' (+%d more)' % (len(u) - 3) if len(u) > 3 else '')))
    # ### **A COUNT FROM A LEXICAL DESCRIPTION IS A CANDIDATE COUNT UNTIL IT IS READ.** ### Eleven
    # ### rows were read one by one; three describe something that is not a machine condition at
    # ### all, and they are named rather than quietly dropped -- ### **MAKING THE CORPUS LOOK WORSE
    # ### THAN IT IS IS AS MUCH A DEFECT AS MAKING IT LOOK BETTER** (b434).
    NOT_A_HANDLER = {
        ('b372_batch.py', 'last_declared'):
            'READ-ONLY here means it does not WRITE history -- a discipline, not a machine state',
        ('b389_extract.py', 'probe'):
            'READ-ONLY here means a request with no method or body -- access discipline, not a file',
        ('b372_eol.py', 'polarity_fixture'):
            'a FIXTURE that exercises `autocrlf`; it demonstrates the condition, it does not cure it',
    }
    genuine = [r for r in single if (r[0], r[1]) not in NOT_A_HANDLER]
    rec('')
    rec('    ### **AND THE ELEVEN READ ONE BY ONE, BECAUSE A DESCRIPTION MATCHES WORDS:**')
    for (f, n), why in sorted(NOT_A_HANDLER.items()):
        rec('      %-24s %-20s ### NOT A HANDLER' % (f, n))
        for chunk in wrap(why, 74):
            rec('            %s' % chunk)
    rec('    ### ### **CANDIDATES %d  ->  GENUINE SINGLE-TOOL ENVIRONMENTAL HANDLERS : %d**'
        % (len(single), len(genuine)))

    # ### **(N2)(b), SCORED BY GROUPING RATHER THAN BY ASSERTION.**
    fams = {}
    for r in genuine:
        fams.setdefault(r[3], []).append(r)
    rec('')
    rec('    ### ### **THE SAME CONDITION MET INDEPENDENTLY, BY ACT:**')
    met_twice = []
    for label, rs in sorted(fams.items(), key=lambda kv: -len(kv[1])):
        acts = sorted({f[:4] for f, _n, _l, _lb, _m, _fi, _u in rs})
        rec('      %-24s %d tool(s), %d act(s) : %s'
            % (label, len(rs), len(acts), ', '.join(acts)))
        if len(acts) > 1:
            met_twice.append((label, acts, rs))
    rec('')
    rec('    ### ### **REPAIRED ON THE STRENGTH OF THIS CENSUS : 0.** ### (K) BAR 8 -- the census')
    rec('    ### is the product, and (R46) governs what happens to the rest going forward.')
    rec('')
    rec('    ### **THE TOOL THIS ACT ITSELF CREATED IS NOT IN THE POPULATION ABOVE**, and here is')
    rec('    ### the evidence it is a guard and not another single-tool cure:')
    fr_users = [f for f in os.listdir(T) if f.endswith('.py') and not f.startswith('b435_')
                and re.search(r'\bforce_rm\s*\.\s*rmtree\b', code_only(os.path.join(T, f)))]
    rec('      force_rm.py              rmtree               obtained by : %s'
        % (', '.join(sorted(fr_users)) or '### NOBODY'))
    return single, genuine, met_twice


def main():
    rec('=' * 100)
    rec('b435 -- THE CURE SHARED, AND THE SKIPS THAT PRINT LIKE PASSES. ### THE COMPONENTS.')
    rec('=' * 100)
    rec('  ### **THIS RECORD IS WRITTEN BY THIS RUN.** ### `run_clock` stamps it, so a reader can')
    rec('  ### tell it from a previous run`s file left on disk when a tool raised (BAR 11, b434).')
    rec('  ### pre-act blobs pinned before any write:')
    for f in TOUCH:
        rec('      %-22s %s' % (f, PRE[f]))

    rule_ok = ruling()
    step2 = component_1()
    sites_ok = component_1_sites() if step2 else False
    ex_ok = component_1_exercise() if sites_ok else False
    c2 = component_2()
    fx = component_2_fixtures() if c2 else False
    ncand, nfolded = component_2_sweep()
    cen = census()

    rec('')
    rec('=' * 100)
    rec('  ### ### **THE COMPONENTS, SCORED.**')
    rec('=' * 100)
    for label, v in (("the ruling is quoted from the banked paste", rule_ok),
                     ('the shared tool holds both polarities', step2),
                     ('the ten sites named, called and reasoned', sites_ok),
                     ('the repointed tools behave as before', ex_ok),
                     ('the guard report distinguishes three states', c2),
                     ('the three-state fixtures hold', fx),
                     ('the census is not void', cen is not None)):
        rec('    %-52s %s' % (label, 'HELD' if v else '### NOT HELD'))
    rec('')
    rec('  ### ### **(N1) at least two of the ten sites are correct as written and are left**')
    left = sum(1 for s in SITES if s[3])
    rec('      left as written : %d of %d   ### ### **%s**'
        % (left, len(SITES), 'HELD' if left >= 2 else '### REFUTED'))
    if cen is not None:
        single, genuine, met_twice = cen
        rec('  ### ### **(N2), ITS TWO CLAUSES SCORED APART** (R27).')
        rec('      (a) the census finds MORE THAN THREE single-tool cures')
        rec('          candidates %d, genuine %d   ### ### **%s**'
            % (len(single), len(genuine),
               'HELD' if len(genuine) > 3 else '### REFUTED'))
        rec('      (b) at least one handles a failure ANOTHER ACT HAS ALREADY MET INDEPENDENTLY')
        if met_twice:
            label, acts, rs = met_twice[0]
            rec('          ### **%s -- met independently by %d acts: %s**'
                % (label, len(acts), ', '.join(acts)))
            for f, n, ln, _lb, _m, _fi, _u in sorted(rs):
                rec('            %-24s %-20s line %d' % (f, n, ln))
            rec('          ### ### **HELD** -- and it is not a near miss: %d separate acts each'
                % len(acts))
            rec('          ### wrote their own cure for the same machine condition.')
        else:
            rec('          ### ### **NOT FOUND -- REFUTED.**')
    rec('')
    rec('  ### MISSES : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b435_components', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
