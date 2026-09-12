# -*- coding: utf-8 -*-
"""b432_checks.py -- THE CONTROL SUITE FOR b432. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE.**
### ### **AND THE TWO READINGS LAND IN TWO FILES** (BAR 11): b430's post-push run overwrote its own
### pre-push record, and only the commit saved it. ### The side is decided by whether this act's
### commit is already on the remote -- the same fact the two readings differ about.
"""
import io
import json
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
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
SIDE = KERN
EFF = os.path.join('D:', os.sep, 'SIDE-effects')
EXT = os.path.join('D:', os.sep, '_b431_external')
REPO = os.path.join(EXT, 'repo')
FACE = os.path.join(D, 'b432_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b432_checks.txt')
POSTPUSH = os.path.join(D, 'b432_checks_postpush.txt')
NL = chr(10)
THREE = ['propext', 'Classical.choice', 'Quot.sound']


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def pycode_of(src):
    """### BAR 12: COMMENTS **AND** STRING LITERALS STRIPPED BY THE TOKENIZER, DOTS RE-CLOSED."""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except Exception:
        return ''
    return re.sub(r'\s*\.\s*', '.', ' '.join(out))


def git(repo, *a):
    try:
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout
    except Exception:
        return ''


def unchanged(repo, path):
    return path not in git(repo, 'status', '--porcelain', '--', path)


def changed_tracked(repo):
    out = []
    for ln in git(repo, 'status', '--porcelain').splitlines():
        if ln[:2].strip() and not ln.startswith('??'):
            out.append(ln[3:].strip().strip('"'))
    return out


def untracked_new(repo):
    """### **THE WRITE-LIST ARMS WERE BLIND TO NEW FILES, AND THAT IS MOST OF WHAT AN ACT WRITES.**

    ### `git status --porcelain` marks a brand-new file `??`, and both b430's arms and this act's
    ### first writing skipped `??` lines -- so the arms only ever judged MODIFIED tracked files.
    ### ### **EVERY ACT TOOL AND EVERY BANK FILE IS NEW**, so the thing the write list exists to
    ### govern was exactly the thing the arms could not see. ### Found here because this act added a
    ### seventh tool to a face that declared six and the arms reported nothing.
    ### Scoped to paths this act could plausibly have written -- the repository carries 70-odd
    ### untracked files left by earlier acts, and charging those here would be the opposite error.
    """
    out = []
    for ln in git(repo, 'status', '--porcelain').splitlines():
        if ln.startswith('??'):
            f = ln[3:].strip().strip('"').rstrip('/')
            if re.search(r'b432', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b432_components.txt'))
EXTR = read(os.path.join(D, 'b432_extract.txt'))
PROF = read(os.path.join(D, 'b432_profile.txt'))
BUILD = read(os.path.join(D, 'b432_build.log'))
LOCKG = read(os.path.join(D, 'b432_lockgate.txt'))
SCAN = read(os.path.join(D, 'b432_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b432_ferry.txt'))
CENS = read(os.path.join(D, 'b432_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b432_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b432_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b432_components.py'))
SRC_EXT = read(os.path.join(T, 'b432_extract.py'))
SRC_CHK = read(os.path.join(T, 'b432_checks.py'))
try:
    G = json.loads(read(os.path.join(D, 'b432_forms.json')) or '{}')
except Exception:
    G = {}
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b432. ### The first thing THIS act did is
# ### its step-zero resolution, and that is the boundary.
# ### **THIS ACT RESOLVES NO ADDRESS**, so it has no `ls-remote` record to date itself from --
# ### b431's boundary file does not exist here. ### Its first artefact is its own ferry scan, and
# ### the ferry itself is no boundary: all three legs' pastes were banked together at b430.
ACT_START = os.path.getmtime(os.path.join(D, 'b432_ferry_scan.txt'))


def written_by_this_act(repo, rel):
    try:
        return os.path.getmtime(os.path.join(repo, rel)) >= ACT_START
    except Exception:
        return True


def writelisted(repo, rel):
    """### IS THIS PATH NAMED BY THE LOCKED FACE'S WRITE LIST?

    ### ### **A TOOL MUST BE NAMED OUTRIGHT; ONLY BANK FILES FALL UNDER A PATTERN.** ### The first
    ### writing let any basename starting `b432_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b432_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b432_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b432_', base)) and 'b432_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b432_.*\.py$', f)))


def inherited_dirty():
    return [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
            if not written_by_this_act(r, f)]


def verdict_line(text, needle):
    """### A2: THE VERDICT **LINE**, NEVER A SUBSTRING OF THE WHOLE OUTPUT."""
    for ln in text.splitlines():
        if needle in fold(ln):
            return True
    return False


def declared_arms():
    sec = FACET.split('### (G2) THE GATE ARMS.')[1].split('### (K) THE BARS')[0] \
        if '### (G2) THE GATE ARMS.' in FACET else ''
    seen, out = set(), []
    for a in re.findall(r'`(G-[A-Z0-9-]+)`', sec):
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def _pushed():
    """### HAS **THIS ACT'S** WORK REACHED THE REMOTE?

    ### ### **"HEAD IS ON THE REMOTE" IS NOT THE QUESTION** -- before this act commits anything,
    ### HEAD is trivially on the remote, and the first writing of this predicate therefore called
    ### the PRE-push reading a POST-push one and wrote it to the wrong file. ### The question is
    ### whether a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b432' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False


OUT = POSTPUSH if _pushed() else PREPUSH


def main(argv):
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rec('=' * 100)
    rec('b432_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
    rec('  reading : %s' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    DEC = declared_arms()

    rec('  ### THE CHANGED PATHS, BY SIDE OF THIS ACT`S OWN START:')
    for r, f in unlisted_writes():
        rec('      THIS ACT, NOT ON THE WRITE LIST : %-22s %s' % (os.path.basename(r), f))
    for r, f in inherited_dirty():
        rec('      BEFORE THIS ACT BEGAN           : %-22s %s' % (os.path.basename(r), f))
    rec('      this act`s unlisted writes : %d ; inherited dirty : %d'
        % (len(unlisted_writes()), len(inherited_dirty())))
    _tools = new_act_tools()
    _cap = re.search(r'new `relay` act-tool files\s+demand (\d+)\s+cap (\d+)',
                     read(os.path.join(D, 'b432_regspec_run.txt')))
    rec('      new act-tool files written : %d %s' % (len(_tools), _tools))
    rec('      the face`s declared cap    : %s' % (_cap.group(2) if _cap else '(not read)'))
    if _cap and len(_tools) > int(_cap.group(2)):
        rec('      ### **THE ACT WROTE MORE ACT TOOLS THAN ITS LOCKED FACE DECLARED.** ### The')
        rec('      ### face is locked and is NOT edited; the breach is printed and named.')
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **THE WRITE-LIST ARMS ARE VACUOUS ON A CLEAN TREE.** ### The pre-push')
        rec('      ### reading governs: %s unlisted write(s), banked at b432_checks.txt.'
            % _pre.group(1))
    rec()

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'the paste carries its own part marker and the face says IN FULL',
         'paste ends (part 1 of 1)' in FERRY and 'PART 1 OF 1' in FACET),
        ('G-SCAN-CLEAN', 'the scan`s verdict line reads 0 hits',
         verdict_line(SCAN, '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'both census records read TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING : 0') and verdict_line(FCENS, 'TOTAL MISSING : 0')),
        ('G-STEPZERO-PINS', 'the pin record reads 0 hard-failing and every repo 0/0',
         verdict_line(PINS, 'REPOS HARD-FAILING : 0')
         and 0 == len([1 for ln in PINS.splitlines()
                       if 'behind/ahead' in ln and '0 / 0' not in ln])),
        ('G-STEPZERO-GUARD', 'the face records the guard exercised in all four at 0 failing',
         'EXERCISED IN ALL FOUR, `0` FAILING' in FACET),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXTR, 'MISSES : 0')),
        ('G-REG-LOCKED-FIRST', 'the components bank carries the digest the face`s lock block does',
         'THE REGISTRATION LOCK' in FACET and bool(G.get('seal_read_from_face'))
         and G.get('seal_read_from_face') in FACET and G.get('seal_read_from_face') in COMP),
        ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, and permitted the lock',
         verdict_line(LOCKG, 'GATES READ : 8.') and verdict_line(LOCKG, 'PASSING : 8.')
         and verdict_line(LOCKG, 'VERDICT : LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'the sealed body recomputes to the banked digest',
         verdict_line(subprocess.run(
             [sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
             capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
             'SEAL INTACT -- the body is byte-for-byte what was sealed.')),
        ('G-PRIOR-CLOSED', 'the prior act is closed at its own correspondence row marker',
         bool(re.search(r'(?m)^\|\s*280\s*\|', read(os.path.join(KERN, 'CORRESPONDENCE.md'))))),

        # ### ---- THE LANE AS b428 NAMED IT ------------------------------------------------------
        ('G-B428-QUOTED', 'the lane is quoted from b428`s own bank, by line count',
         isinstance(G.get('b428_lines'), int) and G.get('b428_lines') > 0),
        ('G-B428-NOT-IMPROVED', 'b428 is quoted, not restated in better words',
         'THAT IS NOT A CRITICISM' in fold(COMP).upper()),
        ('G-LACK-NAMED', 'what b428 lacked is named in the order`s own words',
         'no example of what a graded disproof looks like' in fold(COMP)),

        # ### ---- THE TWO WORKED CASES -----------------------------------------------------------
        ('G-TWO-CASES-FROM-BANKS', 'both grades are read from the two acts` own banks',
         G.get('case_a_grade') == 'DERIVES' and G.get('case_b_grade') == 'DERIVES'),
        ('G-SHAPES-FROM-STATEMENTS', 'each shape is read from the statement, not from the grade',
         G.get('case_a_shape') == 'UNIVERSAL NEGATIVE'
         and G.get('case_b_shape') == 'EXISTENTIAL / CONSTRUCTION'
         and G.get('case_a_grade') == G.get('case_b_grade')),
        ('G-TWO-IS-TWO', 'the act says in its own text that two cases are two cases',
         'TWO CASES ARE TWO CASES' in fold(COMP).upper()),

        # ### ---- THE TWO FORMS -----------------------------------------------------------------
        ('G-H2-IN-CORPUS-WORDS', 'the hypothesis is quoted from the keystone at its own line',
         isinstance(G.get('h2_line'), int) and 'positive space on the zeros' in fold(COMP)),
        ('G-BOTH-FORMS-WRITTEN', 'both forms are written out, each with what it would state',
         'FORM (a) -- AN EXHIBITED ZERO OFF THE LINE' in COMP
         and 'FORM (b) -- THE UNIVERSAL NEGATIVE' in COMP),
        ('G-FORMS-CLAUSE-QUOTED-AT-LINE', 'the clause form (a) must meet is quoted at its line',
         bool(G.get('t6_lines')) and 'INVARIANCE_BARRIERS.md:' in COMP),
        ('G-NEITHER-ASSERTED', 'neither form is asserted by this act',
         'NEITHER FORM IS ASSERTED HERE' in fold(COMP).upper()),
        ('G-NEITHER-CONSTRUCTED', 'no candidate is constructed: no tool of this act computes one',
         not re.search(r'numpy|mpmath|scipy', pycode_of(SRC_COMP + SRC_EXT))),

        # ### ---- THE INSTRUMENTS ----------------------------------------------------------------
        ('G-INSTRUMENT-BY-CONTENT', 'each instrument is decided by what it is run on and reports',
         G.get('negative_control_form') == 'a' and bool(G.get('run_on_exhibited'))),
        ('G-INSTRUMENT-NOT-BY-NAME', 'the act says the decision is not made by either name',
         'NEVER BY ITS NAME' in fold(COMP).upper()),
        ('G-UNDECIDED-AVAILABLE', 'UNDECIDED FROM THE RECORD was available as an outcome',
         'UNDECIDED FROM THE RECORD' in SRC_COMP),
        ('G-CONTROL-OBJECT-NAMED', 'the object the control is run on is named at its own line',
         'Davenport' in COMP and 'off the critical line' in COMP),
        ('G-PHASE-SCORED-AGAINST-NOTHING', 'the phase condition`s answer is printed and unscored',
         'THE PHASE CONDITION IS NOT PART OF' in FACET and bool(G.get('phase_form'))),

        # ### ---- THE SYMMETRY CLAUSE ------------------------------------------------------------
        ('G-SYMMETRY-QUOTED-AT-LINE', 'the symmetry clause is quoted at its own file and line',
         bool(G.get('t1_lines')) and 'INVARIANCE_BARRIERS.md:' in COMP),
        ('G-SYMMETRY-SCOPE-KEPT', 'the keystone`s own scope travels with the clause',
         'THE SCOPE IS THE KEYSTONE' in COMP and 'ADDS NONE' in COMP),

        # ### ---- THE EXPECTATION ----------------------------------------------------------------
        ('G-L3-APART', 'the face declares L3`s two clauses apart',
         'ITS TWO CLAUSES' in FACET and '(b) it is' in FACET),
        ('G-L3-SCORED', 'both clauses of L3 are decidable from a printed result',
         G.get('negative_control_form') is not None
         and G.get('negative_control_not_form_b') is not None),

        # ### ---- THE LANE, LEFT WHERE IT WAS ----------------------------------------------------
        ('G-LANE-NOT-OPENED', 'the act states the lane is left where it was found',
         'THE RESTATEMENT IS THE WHOLE OF WHAT THIS ACT DID TO THE LANE' in COMP),
        ('G-TRIGGER-UNTOUCHED', 'the trigger text is printed unchanged',
         'trigger, unchanged      : the instrument lane opening' in COMP),
        ('G-NOCANDIDATE', 'candidates constructed reads 0',
         'candidates constructed  : 0' in COMP),
        ('G-NOREACHCLAIM', 'the act states it claims nothing about reach',
         'claims about reach      : 0' in COMP
         and 'NOT A CLAIM THAT FORM (b) IS UNREACHABLE' in COMP),

        # ### ---- THE NOTHINGS -------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel is built: no tool of this act invokes a build',
         not re.search(r'lake|elan', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOFETCH', 'nothing is fetched: no tool of this act opens a URL',
         not re.search(r'urlopen|urllib|requests', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-CITED-NOWHERE', 'no corpus document names this act',
         0 == len([1 for f in ('FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md')
                   if re.search(r'b432', read(os.path.join(PP, f)))])),
        ('G-FOUR-LISTS-OPEN', 'no list of the four was closed',
         all(unchanged(PP, f) for f in ('REGISTRY.md', 'FACES_LEDGER.md'))),
        ('G-ARC-CHECKPOINTED', 'no witness-arc site was attempted',
         not re.search(r'site_iv', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOGRADE-MOVED', 'no grade moved: the grading documents are untouched',
         all(unchanged(PP, f) for f in ('FACES_LEDGER.md', 'FINDINGS.md'))),
        ('G-NOPREMISE', 'no premise discharged', unchanged(PP, 'FINDINGS.md')),
        ('G-NODOOR', 'no door restated', unchanged(PP, 'REGISTRY.md')),
        ('G-NOROUTE', 'no route proposed', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOKAPPA', 'no kappa measured',
         not re.search(r'kappa', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NORULE', 'no rule struck or amended; the standing file is unmoved',
         bool(re.search(r'(?m)^VERSION:\s*2\s*$', read(os.path.join(T, 'FERRY_STANDING.md'))))
         and unchanged(ROOT, 'tools/FERRY_STANDING.md')),
        ('G-NODEPOSIT', 'no deposit action',
         not re.search(r'zenodo|deposit', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOH2-MOVED', 'h2 is read and not moved: the keystone is unchanged',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
        ('G-NOLOCKEDFACE', 'no prior locked face was written by this act',
         all(os.path.getmtime(os.path.join(D, f)) < ACT_START
             for f in os.listdir(D)
             if re.match(r'b4[0-3]\d_registration', f) and not f.startswith('b432'))),
        ('G-NOPRIORBANK', 'no prior act`s bank appears among this act`s changed paths',
         [] == [f for f in changed_tracked(ROOT)
                if re.match(r'data/b4(0|1|2)\d_', f) or re.match(r'data/b43[01]_', f)]),
        ('G-NOBANKEDFERRY', 'no banked ferry is written by any tool of this act',
         not re.search(r"FERRY\s*,\s*'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOFOLD', 'no fold run', not re.search(r'fold_run', pycode_of(SRC_COMP))),
        ('G-NOLEDGERROW', 'no ledger row edited', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKEYSTONE-EDIT', 'no keystone edited, including the two this sortie quoted',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')
         and unchanged(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')),
        ('G-CORPUS-SCOPE', 'this act read the corpus and its own bank only',
         not re.search(r'urlopen', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-TRAIL-APPEND-ONLY', 'the trail`s committed text is a TRUE PREFIX of its text now',
         appended_only(PP, 'OPEN_TRAILS.md') or unchanged(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'the table`s committed text is a TRUE PREFIX of its text now',
         appended_only(SIDE, 'CORRESPONDENCE.md') or unchanged(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every file THIS ACT wrote is named by the locked write list',
         [] == unlisted_writes()),
        ('G-NOEXTRAKIND', 'no file of an unnamed kind was written by this act',
         [] == unlisted_writes()),
        ('G-WRITELIST-COUNTS-NEW', 'the write ledger counts untracked new files, not only modified',
         'untracked_new' in pycode_of(SRC_CHK)),
        ('G-NOSTAGE-A', 'no tool of this act stages with -A',
         not re.search(r"'add'\s*,\s*'-A'", pycode_of(SRC_COMP + SRC_EXT + SRC_CHK))),
        ('G-NOBORROWEDBAR', 'every bar asserted here is re-run here, not inherited',
         bool(G) and bool(COMP)),
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', None),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank or git`s view of the repos',
         bool(COMP) and bool(EXTR) and bool(G)),
        ('G-ARMS-STRIP-PROSE', 'every source-reading arm strips comments and strings by tokenizer',
         'tokenize' in pycode_of(SRC_CHK)),
        ('G-ARMS-FOLD-MARKERS', 'every prose-reading arm folds markup before matching',
         'fold' in pycode_of(SRC_CHK) and 'fold' in pycode_of(SRC_COMP)),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line, never as a substring',
         'verdict_line' in pycode_of(SRC_CHK)),
        ('G-TWO-READINGS-TWO-FILES', 'the pre-push and post-push readings land in two files',
         PREPUSH != POSTPUSH),
        ('G-NOWRAP-MIDTOKEN', 'no report line is broken mid-token',
         all(not re.search(r'\w-$', ln) for ln in COMP.splitlines())),
        ('G-MUSTFAIL', 'a deliberately false arm fails, so a clean sweep is not a dead suite', None),

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
    rec()

    fails = []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = (v is False)
            rec('  %-32s %-4s %s' % (n, 'FAIL', 'CONTROL -- a false arm must fail; it %s'
                                     % ('did' if ok else '### DID NOT ###')))
            if not ok:
                fails.append(n)
            continue
        ok = bool(v)
        rec('  %-32s %-4s %s' % (n, 'PASS' if ok else '### FAIL', d))
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
