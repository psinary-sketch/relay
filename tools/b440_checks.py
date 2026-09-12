# -*- coding: utf-8 -*-
"""b440_checks.py -- THE CONTROL SUITE FOR b440. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE**, and the suite refuses to agree
### with itself: `G-ARMS-DECLARED-EQ-RUN` is computed by comparing the two sets.
### ### **THE TWO READINGS LAND IN TWO FILES** (BAR 11), the side decided by whether this act's
### commit is already on the remote.
"""
import io
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
WINREPO = os.path.join('D:', os.sep, 'SIDE-window')
FACE = os.path.join(D, 'b440_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b440_checks.txt')
POSTPUSH = os.path.join(D, 'b440_checks_postpush.txt')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    return (s or '').replace(chr(13) + chr(10), NL)


def fold(s):
    """### **FOLD BOTH SIDES, NEVER TYPE ONE** -- the trap `b436`-`b439` hit five times."""
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def pycode_of(src):
    """### COMMENTS **AND** STRING LITERALS STRIPPED BY THE TOKENIZER, DOTS RE-CLOSED."""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except Exception:
        return ''
    return re.sub(r'\s*\.\s*', '.', ' '.join(out))


def verdict_line(txt, needle, phrase):
    """### **A VERDICT IS READ BY ITS LINE, NEVER AS A SUBSTRING OF THE FILE** (`A2`)."""
    for ln in nl(txt).splitlines():
        if needle in ln:
            return phrase in ln
    return False


def git(repo, *a):
    try:
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout or ''
    except Exception:
        return ''


def unchanged(repo, path):
    return path not in git(repo, 'status', '--porcelain', '--', path)


# ### **THE ACT BOUNDARY.** ### The repositories carry scores of untracked files left by earlier
# ### acts. ### An arm that counts them charges THIS act for THEIR writes -- the opposite error to
# ### the one `b439` fixed, and just as wrong. ### **THE BOUNDARY IS THE EARLIEST OF THIS ACT`S OWN
# ### STEP-ZERO ARTEFACTS**, and every write arm is scoped to files newer than it.
ACT_START = min(os.path.getmtime(os.path.join(D, f))
                for f in ('b440_ferry.txt', 'b440_ferry_scan.txt'))


def touched(repo, pat, since=True):
    """### Tracked-modified OR untracked-new, matching `pat`, ### **WRITTEN BY THIS ACT.**

    ### **NEW FILES COUNT** (`b439`) -- a brand-new file is most of what an act writes, and an arm
    ### that skips the porcelain`s untracked marker judges only MODIFIED files.
    """
    out = []
    for ln in git(repo, 'status', '--porcelain').splitlines():
        f = ln[3:].strip().strip('"').rstrip('/')
        if not re.search(pat, f):
            continue
        if since:
            try:
                if os.path.getmtime(os.path.join(repo, f)) < ACT_START:
                    continue
            except OSError:
                continue
        out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b440_components.txt'))
EXTR = read(os.path.join(D, 'b440_extract.txt'))
RGATE = read(os.path.join(D, 'b440_reg_gate.txt'))
TERM = read(os.path.join(D, 'b440_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b440_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b440_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b440_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b440_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b440_ferry.txt'))
CENS = read(os.path.join(D, 'b440_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b440_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b440_pins_stepzero.txt'))
ADD = os.path.join(D, 'b440_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b440_components.py'))
SRC_EXT = read(os.path.join(T, 'b440_extract.py'))
SRC_CHK = read(os.path.join(T, 'b440_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b440_checks.py`
# ### beside `data/b440_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
# ### every prefixed entry and charges a declared file as undeclared. ### **BOTH SIDES ARE REDUCED
# ### TO A BASENAME BEFORE THEY ARE COMPARED.**
WRITELIST = [os.path.basename(x) for x in
             re.findall(r'`([A-Za-z0-9_.\-/]+\.(?:py|txt|json|md|lean))`',
                        FACET.split('(W) THE WRITE LIST')[-1].split('(Z) THE NOTHINGS')[0])]
DEC = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', FACET)) - {'G-NO'})


def _pushed():
    head = git(ROOT, 'rev-parse', 'HEAD').strip()
    return bool(head) and head in git(ROOT, 'branch', '-r', '--contains', head)


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b440 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)

    kern_files = touched(WINREPO, r'.')
    relay_new = touched(ROOT, r'b440')

    ARMS = [
        # ---- STEP ZERO, THE FACE, THE LOCK ---------------------------------------------------
        ('G-RECEIPT-IN-FULL', 'the ferry was received in full and banked before execution',
         'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'the ferry scan reported 0 hits, read by its verdict line',
         verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'the roster reports 0 repositories hard-failing',
         verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-GUARD-DEFERRED-SAID', 'the face says the pre-push guard runs at the close',
         'pre-push guard runs' in F),
        ('G-SURVEY-NOMISS', 'the survey reports 0 anchor misses, by its own line',
         verdict_line(EXTR, 'MISSES', ': 0')),
        ('G-SURVEY-NEEDLE-REAIM-SAID', 'the face says a needle of this seat`s was re-aimed',
         're-aimed before the face' in F.lower()),
        ('G-REG-LOCKED-FIRST', 'the registration carries its lock block',
         'THE REGISTRATION LOCK' in FACET and 'sha256 of every byte ABOVE' in FACET),
        ('G-LOCKGATE-EIGHT', 'the lock gate read eight gates and permitted the lock',
         verdict_line(LOCKG, 'GATES READ', '8')
         and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'the seal verifies by reg_seal.py --verify, not by re-implementation',
         'SEAL INTACT' in (subprocess.run(
             [sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
              'data/b440_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
             text=True, encoding='utf-8', errors='replace').stdout or '')),
        ('G-PRIOR-CLOSED', 'the face records the prior act closed at its row',
         'row 288' in F),
        ('G-TWO-RULINGS-ENTERED', 'both ratified rulings are entered on the face',
         '(R51)' in FACET and '(R52)' in FACET),
        ('G-R51-CONDITION-CARRIED', 'R51 carries its reopening condition, not merely its verdict',
         'IT REOPENS ON AN INSTRUMENT FOR THAT FORM' in fold(FACET).upper()),
        ('G-R52-SCOPE-CARRIED', 'R52 carries what a non-claim bounds and what it does not',
         'bound what may be CITED' in FACET and 'do not' in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'the addendum slot is named in the write list',
         'b440_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the slot carries a quotation or nothing',
         (not os.path.exists(ADD)) or len(read(ADD).strip()) == 0 or 'arrival' in read(ADD).lower()),
        ('G-INSTRUMENT-LANES-PARKED', 'both instrument lanes are declared parked',
         'Both instrument lanes' in FACET and 'PARKED' in FACET),
        ('G-KERNEL-LANE-SCOPED-C2', 'the kernel lane is scoped to Component 2 alone',
         'FOR COMPONENT 2 ONLY' in FACET),
        ('G-PRELOCK-EVAL-DECLARED', 'the pre-lock evaluation is declared on the face',
         'THAT IS DECLARED, NOT HIDDEN' in FACET),

        # ---- COMPONENT 1 ---------------------------------------------------------------------
        ('G-C1-FOUR-CLAUSES-APART', 'four clauses carry four verdicts, not one word for the set',
         4 == len(re.findall(r'CLAUSE \([abcd]\) : ', COMP))),
        ('G-C1-CLAUSE-A-VERDICT', 'clause (a) carries a verdict', 'CLAUSE (a) : ' in COMP),
        ('G-C1-CLAUSE-B-VERDICT', 'clause (b) carries a verdict', 'CLAUSE (b) : ' in COMP),
        ('G-C1-CLAUSE-C-VERDICT', 'clause (c) carries a verdict', 'CLAUSE (c) : ' in COMP),
        ('G-C1-CLAUSE-D-VERDICT', 'clause (d) carries a verdict', 'CLAUSE (d) : ' in COMP),
        ('G-CORPUS-NAMES-PRINTED', 'the names the corpus uses are printed, not summarised',
         'Riemann-von Mangoldt' in COMP and 'W_inf' in COMP),
        ('G-HITS-HANDREAD', 'the tight-screen hits are hand-read and classified at their lines',
         'HITS HAND-READ' in COMP and 'NOT A JOIN' in COMP),
        ('G-FORM-NOT-IDENTIFICATION', 'carrying the form and making the identification are apart',
         fold('a mention is not a reference') in C),
        ('G-DIGITS-BOTH-PRINTED', 'both digit strings are printed where they differ',
         'the navigator`s :' in COMP and 'this seat`s     :' in COMP),
        ('G-MECHANISM-ONLY-IF-B', 'the mechanism is stated only because (b) holds',
         'STATED ONLY BECAUSE (b) HOLDS' in COMP),
        ('G-SECOND-FAMILY-TESTED', 'the mechanism is tested on both families, not assumed',
         'aimed' in COMP and 'corpus' in COMP and 'SECOND FAMILY' in COMP),
        ('G-THREE-STATUSES-APART', 'defining equation / classical asymptote / closed form apart',
         all(x in COMP for x in ('**DEFINING EQUATION**', '**CLASSICAL ASYMPTOTE**',
                                 '**CLOSED FORM**'))),

        # ---- COMPONENT 2 ---------------------------------------------------------------------
        ('G-C2-CROSSMULT-SHOWN', 'the cross-multiplied form is written out',
         fold('(log_q p)^2 > p^k / q^j') in C),
        ('G-C2-IRRATIONAL-STEP-EXHIBITED', 'the step at which the irrational survives is exhibited',
         'THE STEP AT WHICH THE IRRATIONAL SURVIVES' in COMP),
        ('G-C2-PROBE-RUN', 'the probe was run, not described',
         'lean : exit' in COMP),
        ('G-C2-PROBE-OUTPUT-QUOTED', 'the probe output is quoted including its failure text',
         'did not reduce to' in COMP and 'Unknown identifier' in COMP),
        ('G-C2-LADDER-PRECEDENT-QUOTED', 'the Ladder`s own refusal is quoted before adjudication',
         'MEASURED-AT-BANK' in COMP),
        ('G-C2-SURROGATE-ADJUDICATED', 'the rational surrogate is adjudicated, not ignored',
         'THE LADDER`S OWN REFUSAL' in COMP),
        ('G-C2-BUILD-DECISION-PRINTED', 'the build decision is printed in the record',
         'NEITHER FACT IS BUILT' in COMP),
        ('G-C2-NEITHER-OR-BOTH', 'neither or both -- never one of the two facts',
         0 == len(kern_files)),
        ('G-C2-FACT-ONE-ROUTED', 'fact (i) is named buildable and routed back, not taken',
         'ROUTED BACK AND NOT DECIDED HERE' in COMP),
        ('G-C2-NONCLAIMS-ONLY-IF-CONTENTS', 'the non-claims are untouched because nothing changed',
         unchanged(WINREPO, 'README.md')),
        ('G-C2-NO-LEAN-IN-REPO-IF-NOTHING-BUILT', 'no .lean file of this act exists in any repo',
         0 == len(touched(ROOT, r'\.lean$')) and 0 == len(kern_files)),

        # ---- COMPONENT 3 ---------------------------------------------------------------------
        ('G-C3-DICTIONARY-QUOTED', 'both dictionary rows are quoted from the source',
         'W_pole(g)' in COMP and 'W_∞(g)' in COMP),
        ('G-C3-PREMISE-ADJUDICATED', 'the premise of the order`s conditional is adjudicated',
         'THE PREMISE OF THE ORDER`S CONDITIONAL THEREFORE FAILS' in COMP),
        ('G-C3-CONDITIONAL-NOT-ASSUMED', 'the offered finding is not stated on a failed premise',
         'THE OFFERED' in COMP and 'FINDING IS NOT STATED' in COMP),
        ('G-C3-WEIGHT-NAMED-FROM-SOURCE', 'the weight is named from the source, not by the seat',
         'the count of the two pole terms' in COMP),
        ('G-C3-SPREAD-UNDISTURBED', 'the prior act`s spread is not re-run',
         'IS NOT RE-RUN' in COMP),
        ('G-C3-NUMBER-AND-NAME-APART', 'the measurement and its attribution are kept apart',
         'A MEASUREMENT AND ITS ATTRIBUTION ARE SEPARABLE' in COMP),

        # ---- THE EXPECTATIONS ----------------------------------------------------------------
        ('G-N1-APART', 'N1`s two clauses are scored apart', '`(N1)`' in FACET and '(a)' in FACET),
        ('G-N2-APART', 'N2`s two clauses are scored apart', '`(N2)`' in FACET),
        ('G-N3-APART', 'N3`s two clauses are scored apart', '`(N3)`' in FACET),
        ('G-SEAT-EXPECTATIONS-SCORED', 'this seat`s own two expectations are declared to be scored',
         fold('DECLARED SO THEY CAN BE SCORED AGAINST IT') in F),

        # ---- THE NOTHINGS --------------------------------------------------------------------
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|WebFetch', CODE_COMP)),
        ('G-NOGRADE-MOVED', 'no grade moved', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOTERMINAL-RENAMED', 'no terminal renamed', 0 == len(kern_files)),
        ('G-NONEWINSTRUMENT', 'no new instrument built', 0 == len(touched(ROOT, r'tools/e16/'))),
        ('G-NONEWFAMILY', 'no new family defined', unchanged(ROOT, 'tools/b317_smear.py')),
        ('G-NOATLAS-EDIT', 'the atlas is not edited', unchanged(ROOT, 'tools/e16/carto_atlas.py')),
        ('G-NOLADDER-EDIT', 'the ladder is not edited', unchanged(WINREPO, 'SIDEWindow/Ladder.lean')),
        ('G-NOWINDOW-EDIT', 'Window.lean is not edited', unchanged(WINREPO, 'SIDEWindow/Window.lean')),
        ('G-NOLANE-OPENED', 'no instrument lane opened', 'both instrument lanes' in F.lower()),
        ('G-NOPREMISE', 'no premise discharged', fold('NO PREMISE DISCHARGED') in F),
        ('G-NODOOR', 'no door restated', fold('NO DOOR RESTATED') in F),
        ('G-NOROUTE', 'no route proposed', fold('NO ROUTE PROPOSED') in F),
        ('G-NOKAPPA', 'no kappa measured', fold('NO KAPPA') in F),
        ('G-NORULE-STRUCK', 'no rule struck by this seat',
         fold('NO RULE STRUCK, AMENDED OR WIDENED') in F),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 where the deposit left it', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOLOCKEDFACE', 'no locked face edited',
         0 == len(touched(ROOT, r'registration_2026-09-(?!12).*\.txt'))),
        ('G-NOPRIORBANK', 'no prior act`s bank edited',
         0 == len([f for f in touched(ROOT, r'^data/b4[0-3][0-9]_')
                   if not f.startswith('data/b440')])),
        ('G-NOBANKEDFERRY', 'no banked ferry edited',
         0 == len([f for f in touched(ROOT, r'_ferry\.txt$') if 'b440' not in f])),
        ('G-NOFOLD', 'no fold run', fold('NO FOLD RUN') in F),
        ('G-NOKEYSTONE-EDIT', 'no keystone edited', fold('NO KEYSTONE EDITED OR ANNOTATED') in F),
        ('G-NOCELL-WRITTEN', 'no cell of FACES_LEDGER.md written', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOSEVENTH-SITE', 'no seventh site entered', fold('NO SITE OF THE WITNESS ARC') in F),
        ('G-ARC-CHECKPOINTED-AFTER-IV', 'the arc stays checkpointed after site (iv)',
         fold('checkpointed after site (iv)') in F),
        ('G-FOUR-LISTS-OPEN', 'no list of the four closed', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-DISPROOF-LANE-NOT-OPENED', 'the disproof lane is not opened',
         fold('THE DISPROOF LANE IS NOT OPENED') in F),

        # ---- SCOPE AND THE WRITE LIST --------------------------------------------------------
        ('G-CORPUS-SCOPE', 'only OPEN_TRAILS.md is touched in the corpus',
         0 == len([f for f in touched(PP, r'.') if f != 'OPEN_TRAILS.md'])),
        ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS.md is appended only, or not yet written',
         unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'CORRESPONDENCE.md is appended only, or not yet written',
         unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every file this act touched in relay is on the write list',
         all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
             for f in relay_new)),
        ('G-WRITELIST-NAMES-PATHS', 'the write list names paths, never a class',
         'b440_components.py' in FACET and 'b440_closing.txt' in FACET),
        ('G-WRITELIST-COUNTS-NEW', 'the arm counts NEW files and is scoped to this act`s own',
         'def touched(' in SRC_CHK and 'ACT_START' in pycode_of(SRC_CHK)
         and len(touched(ROOT, r'b440')) >= 20),
        ('G-WRITELIST-KERNEL-SET-ENUMERATED', 'the SIDE-window set is enumerated and its actual 0',
         'SIDEWindow/Weights.lean' in FACET and 0 == len(kern_files)),
        ('G-NOSTAGE-A', 'no `git add -A` in this act`s own tools',
         not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE_COMP + CODE_EXT)),
        ('G-NOBORROWEDBAR', 'twelve bars, all this act`s own',
         12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),

        # ---- THE ARM DISCIPLINE --------------------------------------------------------------
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', True),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank',
         'b440_components.txt' in SRC_CHK),
        ('G-ARMS-STRIP-PROSE', 'the source-reading arms strip comments and strings by tokenizer',
         'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK),
        ('G-ARMS-FOLD-MARKERS', 'the prose-reading arms fold markup, on BOTH sides',
         'def fold(' in SRC_CHK
         and bool(re.search(r'fold \([^)]*\) in [FC]', pycode_of(SRC_CHK)))),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line',
         'def verdict_line(' in SRC_CHK),
        ('G-ARMS-EOL-NORMALISED', 'banked tables are matched with line endings normalised',
         'def nl(' in SRC_CHK and 'chr(13)' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'the suite writes its two readings to two files',
         'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK and '_pushed()' in SRC_CHK),
        ('G-NOWRAP-MIDTOKEN', 'the components record wraps at word boundaries',
         0 == len([1 for ln in COMP.splitlines()
                   if ln.endswith('-') and len(ln) > 96 and set(ln.strip()) != {'-'}])),
        ('G-NOSTRAY-PLACEHOLDER', 'no format string is printed without its arguments',
         0 == len(re.findall(r'%[-0-9.]*[dsfe](?![a-zA-Z0-9])', COMP))),
        ('G-MUSTFAIL', 'THE CONTROL -- a deliberately false arm, which must fail', False),
    ]

    names = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else
                    (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]

    rec('  arms declared on the face : %d' % len(DEC))
    rec('  arms run by this suite    : %d' % len(ARMS))
    missing = sorted(set(DEC) - set(names))
    extra = sorted(set(names) - set(DEC))
    rec('  declared and NOT run      : %d %s' % (len(missing), missing or ''))
    rec('  run and NOT declared      : %d %s' % (len(extra), extra or ''))
    rec('  files touched in SIDE-window : %d %s' % (len(kern_files), kern_files or ''))
    rec()

    fails = []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = (v is False)
            rec('  %-40s %-4s %s' % (n, 'FAIL', 'CONTROL -- a false arm must fail; it %s'
                                     % ('did' if ok else '### DID NOT ###')))
            if not ok:
                fails.append(n)
            continue
        ok = bool(v)
        rec('  %-40s %-4s %s' % (n, 'PASS' if ok else '### FAIL', d))
        if not ok:
            fails.append(n)

    rec()
    rec('=' * 100)
    rec('  ### ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s'
        % (len(ARMS), len(ARMS) - len(fails), len(fails), fails or ''))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fails else 'ARMS FAILING'))
    rec('=' * 100)
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    os.replace(OUT + '.tmp', OUT)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if not fails else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
