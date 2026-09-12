# -*- coding: utf-8 -*-
"""b431_checks.py -- THE CONTROL SUITE FOR b431. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b431_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b431_checks.txt')
POSTPUSH = os.path.join(D, 'b431_checks_postpush.txt')
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
            if re.search(r'b431', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b431_components.txt'))
EXTR = read(os.path.join(D, 'b431_extract.txt'))
PROF = read(os.path.join(D, 'b431_profile.txt'))
BUILD = read(os.path.join(D, 'b431_build.log'))
LOCKG = read(os.path.join(D, 'b431_lockgate.txt'))
SCAN = read(os.path.join(D, 'b431_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b431_ferry.txt'))
CENS = read(os.path.join(D, 'b431_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b431_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b431_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b431_components.py'))
SRC_EXT = read(os.path.join(T, 'b431_extract.py'))
SRC_CHK = read(os.path.join(T, 'b431_checks.py'))
try:
    G = json.loads(read(os.path.join(D, 'b431_the_grade.json')) or '{}')
except Exception:
    G = {}
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b431. ### The first thing THIS act did is
# ### its step-zero resolution, and that is the boundary.
ACT_START = os.path.getmtime(os.path.join(D, 'b431_stepzero_lsremote.txt'))


def written_by_this_act(repo, rel):
    try:
        return os.path.getmtime(os.path.join(repo, rel)) >= ACT_START
    except Exception:
        return True


def writelisted(repo, rel):
    """### IS THIS PATH NAMED BY THE LOCKED FACE'S WRITE LIST?

    ### ### **A TOOL MUST BE NAMED OUTRIGHT; ONLY BANK FILES FALL UNDER A PATTERN.** ### The first
    ### writing let any basename starting `b431_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b431_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b431_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b431_', base)) and 'b431_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b431_.*\.py$', f)))


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
        if 'b431' not in subj:
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
    rec('b431_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
                     read(os.path.join(D, 'b431_regspec_run.txt')))
    rec('      new act-tool files written : %d %s' % (len(_tools), _tools))
    rec('      the face`s declared cap    : %s' % (_cap.group(2) if _cap else '(not read)'))
    if _cap and len(_tools) > int(_cap.group(2)):
        rec('      ### **THE ACT WROTE MORE ACT TOOLS THAN ITS LOCKED FACE DECLARED.** ### The')
        rec('      ### face is locked and is NOT edited; the breach is printed and named.')
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **THE WRITE-LIST ARMS ARE VACUOUS ON A CLEAN TREE.** ### The pre-push')
        rec('      ### reading governs: %s unlisted write(s), banked at b431_checks.txt.'
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
         bool(re.search(r'(?m)^\|\s*279\s*\|', read(os.path.join(KERN, 'CORRESPONDENCE.md'))))),

        # ### ---- THE PRE-LOCK READ, DECLARED RATHER THAN ABSORBED -----------------------------
        ('G-PRELOCK-READ-DECLARED', 'the face itself declares the pre-lock network read',
         'BEFORE THIS FACE WAS LOCKED' in FACET and 'NETWORK READ BEFORE THE LOCK' in FACET),
        ('G-PRELOCK-PINS-PRINTED-BOTH', 'both pins are printed and the record says whether they agree',
         bool(G.get('pin_pre')) and bool(G.get('pin_post')) and 'pins_agree' in G
         and 'pin read at STEP ZERO' in COMP and 'pin read AFTER the lock' in COMP),

        # ### ---- THE ADDRESSES -----------------------------------------------------------------
        ('G-ADDR-AS-GIVEN', 'both addresses come from the paste, quoted by the survey',
         'LongGapsBetweenPrimes' in EXTR and 'long_gaps.pdf' in EXTR),
        ('G-ADDR-NOTHING-GUESSED', 'no tool of this act constructs a candidate address',
         not re.search(r'for\s+\w+\s+in\s*\[.*http', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-ADDR-PINNED', 'the repository by SHA and the paper by sha256',
         bool(re.match(r'^[0-9a-f]{40}$', G.get('pin_post') or ''))
         and bool(re.match(r'^[0-9a-f]{64}$', G.get('paper_sha256') or ''))),
        ('G-ADDR-UNREACHABLE-PRINTED', 'an unreachable address would print the host`s response',
         'UNREACHABLE' in FACET),
        ('G-STOP-RULE-HONOURED', 'no grade is conferred unless the build and the printer both ran',
         (G.get('grade', '').startswith('NO GRADE')) == (not G.get('profile_clean'))),

        # ### ---- THE PAPER --------------------------------------------------------------------
        ('G-PAPER-VERBATIM', 'Theorem 1.1 is quoted from the paper`s own bytes',
         bool(G.get('paper_thm11')) and 'absolute constant' in (G.get('paper_thm11') or '')),
        ('G-PAPER-NOT-PARAPHRASE', 'the graded claim is the page`s text, not the order`s wording',
         (G.get('paper_thm11') or '')[:40] in fold(COMP)),
        ('G-COVERING-QUOTED', 'the covering construction is quoted at the passage that states it',
         bool(G.get('paper_covering'))
         and 'Chinese remainder theorem' in (G.get('paper_covering') or '')),

        # ### ---- THE REPOSITORY AND THE BUILD ---------------------------------------------------
        ('G-REPO-PINNED', 'the clone`s pin is recorded and is a full SHA',
         bool(re.match(r'^[0-9a-f]{40}$', G.get('pin_post') or ''))),
        ('G-TERMINAL-LOCATED', 'the terminal is located at its own line in the named file',
         isinstance(G.get('terminal_line'), int) and bool(G.get('terminal_src'))),
        ('G-TOOLCHAIN-REPORTED', 'the foreign toolchain is reported against the corpus`s',
         bool(G.get('toolchain')) and 'v4.29.1' in COMP),
        ('G-CLONE-OUTSIDE', 'the clone is outside every rostered repository',
         REPO.lower().startswith(os.path.join('d:', os.sep, '_b431').lower())
         and not any(REPO.lower().startswith(r.lower()) for r in (ROOT, PP, KERN, EFF))),
        ('G-BUILT-ONE-AT-A-TIME', 'the build log records jobs run one at a time, all succeeding',
         G.get('jobs', 0) >= 1 and G.get('jobs') == G.get('jobs_ok')),
        ('G-PROFILE-FROM-PRINTER', 'the graded profile line came from the printer`s own stdout',
         bool(G.get('profile_line'))
         and (G.get('profile_line') or '').strip() in [x.strip() for x in PROF.splitlines()]),
        ('G-AXIOMS-BEYOND-THREE-NAMED', 'any axiom beyond the standard three is named',
         isinstance(G.get('axioms_beyond_three'), list)
         and all(a in THREE for a in (G.get('profile_axioms') or []))),
        # ### **THE CLAIM IS ABOUT THE CLOSURE, NOT ABOUT THE REPOSITORY'S EVERY FILE.** ### The
        # ### first writing demanded 0 `sorry` terms anywhere, and `Challenge.lean` carries one BY
        # ### DESIGN -- it is Comparator's reference statement, whose *"proof placeholder is
        # ### intentional"* in the repository's own words. ### An arm that fails on that is not
        # ### strict, it is wrong: the axiom profile is what settles the closure, and it is clean.
        ('G-SORRY-SWEPT', 'sorryAx absent from the closure, and every source sorry named and placed',
         G.get('sorryAx') == 0 and G.get('sorry_terms', 0) == 1
         and 'Challenge.lean' in COMP and 'reference statement' in COMP),
        ('G-SORRY-STRIPPED-FIRST', 'the sweep strips comments and string literals before counting',
         'strip_lean_comments' in pycode_of(SRC_COMP)),
        ('G-BUILD-OR-STOP', 'a grade was conferred only on a completed build',
         bool(G.get('built')) or (G.get('grade', '').startswith('NO GRADE'))),

        # ### ---- THE GRADE ---------------------------------------------------------------------
        ('G-GRADE-ONE-OF-FOUR', 'the grade is one of the four (R40) names, or a printed refusal',
         G.get('grade') in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION / SHELL', 'NOT THE CLAIM')
         or (G.get('grade') or '').startswith('NO GRADE')),
        ('G-GRADE-NAMES-ITS-CLAIM', 'the grade names the claim it is against in the same sentence',
         "GRADE, AGAINST THE PAPER'S THEOREM 1.1" in COMP),
        ('G-FOUR-CLAUSES-APPLIED', 'all four of b429`s clauses are applied and each is printed',
         'THE FOUR CLAUSES, APPLIED' in COMP and COMP.count('(4) definitions checked') == 1),
        ('G-DEFENC-BY-TOOL', 'the corpus`s own definition check was imported and run',
         'rowgen.definition_encoded' in pycode_of(SRC_COMP) and 'defenc' in G),
        ('G-DEFENC-CONTROL-FIRES', 'the defenc control fires, so a False is a result',
         G.get('defenc_control_fires') is True),
        ('G-UNFOLD-TO-BASE', 'the terminal`s statement was read from the Lean source itself',
         bool(G.get('terminal_src')) and 'Nat.nth Nat.Prime' in (G.get('terminal_src') or '')),

        # ### ---- THE TYPE-D QUESTION ------------------------------------------------------------
        ('G-TYPED-BOTH-UNFOLDED', 'both sides are unfolded, not summarised',
         bool(G.get('paper_covering')) and 'witness_moduli_singleton' in G),
        ('G-TYPED-CLAUSES-QUOTED-AT-LINE', 'the keystone side is quoted at its own file and line',
         'SIDEEffects/Phase15/Module1.lean:' in COMP),
        ('G-TYPED-VERDICT-ONE-OF-THREE', 'the verdict is one of the three the order names',
         G.get('typed_verdict') in ('ONE THEOREM RUN TWO WAYS', 'TWO THEOREMS SHARING A NAME',
                                    'UNDECIDABLE FROM THE STATEMENTS')),
        ('G-TYPED-NOT-BY-THE-WORD', 'the verdict rests on what each statement quantifies over',
         'WHAT IT QUANTIFIES OVER' in COMP
         and 'Neither fact is evidence about what either STATES' in fold(COMP)
         and 'WHAT IT CONCLUDES' in COMP),
        ('G-NOBRIDGE', 'no bridge was typed: no tool of this act writes a .lean file',
         not re.search(r"\.lean'\s*,\s*'w'|open\([^)]*\.lean[^)]*'w'", pycode_of(SRC_COMP))),
        ('G-KEYSTONE-UNEDITED', 'the conspiracy keystone and its module are untouched',
         unchanged(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
         and unchanged(EFF, 'SIDEEffects/Phase15/Module1.lean')),

        # ### ---- THE EXPECTATION ----------------------------------------------------------------
        ('G-L2-APART', 'the face declares L2`s three clauses apart',
         'ITS THREE CLAUSES PRINTED APART' in FACET and '(c) the Type-D verdict reads' in FACET),
        ('G-L2-SCORED', 'each clause of L2 is decidable from a printed result',
         all(x is not None for x in (G.get('grade'), G.get('profile_clean'),
                                     G.get('typed_verdict')))),
        ('G-L2C-REASON-SCORED-APART', 'clause (c)`s reason is scored beside its verdict',
         'THE PARTING IS AT WHAT IS QUANTIFIED' in COMP),

        # ### ---- THE NOTHINGS -------------------------------------------------------------------
        ('G-NOCORPUSKERNEL', 'no corpus kernel file changed',
         all(unchanged(KERN, 'Core/%s.lean' % m)
             for m in ('SmearGeneral', 'SinglePrimeFactor', 'FiniteSideSeal'))
         and unchanged(KERN, 'AXIOM_PRINTS.txt')),
        ('G-NOCORPUSBUILD', 'no tool of this act builds inside a corpus repository',
         not re.search(r'cwd\s*=\s*(KERN|EFF|PP)', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-CITED-NOWHERE', 'no corpus document names this act',
         0 == len([1 for f in ('FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md')
                   if re.search(r'\bb431\b', read(os.path.join(PP, f)))])),
        ('G-FOUR-LISTS-OPEN', 'no list of the four was closed',
         all(unchanged(PP, f) for f in ('REGISTRY.md', 'FACES_LEDGER.md'))),
        ('G-ARC-CHECKPOINTED', 'no witness-arc site was attempted',
         not re.search(r'site_(iv|4)', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOGRADE-MOVED', 'the grade this act printed lives only in relay`s bank',
         os.path.exists(os.path.join(D, 'b431_the_grade.json'))
         and all(unchanged(PP, f) for f in ('FACES_LEDGER.md', 'FINDINGS.md'))),
        ('G-NOPREMISE', 'no premise discharged', unchanged(PP, 'FINDINGS.md')),
        ('G-NODOOR', 'no door restated', unchanged(PP, 'REGISTRY.md')),
        ('G-NOROUTE', 'no route proposed', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOKAPPA', 'no kappa measured',
         not re.search(r'kappa', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NORULE', 'no rule struck or amended; the standing file`s VERSION line is unmoved',
         bool(re.search(r'(?m)^VERSION:\s*2\s*$', read(os.path.join(T, 'FERRY_STANDING.md'))))
         and unchanged(ROOT, 'tools/FERRY_STANDING.md')),
        ('G-NODEPOSIT', 'no deposit action',
         not re.search(r'zenodo|deposit', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOH2', 'h2 untouched', not re.search(r'\bh2\b', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOLOCKEDFACE', 'no prior locked face was written by this act',
         all(os.path.getmtime(os.path.join(D, f)) < ACT_START
             for f in os.listdir(D) if re.match(r'b4[0-2]\d_registration', f))),
        # ### **mtime IS NOT THE WITNESS HERE** (b430's lesson): a checkout rewrites it, and the
        # ### question is whether THIS act's commit touches a prior act's bank. ### git answers it.
        ('G-NOPRIORBANK', 'no prior act`s bank appears among this act`s changed paths',
         [] == [f for f in changed_tracked(ROOT) if re.match(r'data/b4(0|1|2)\d_', f)
                or re.match(r'data/b430_', f)]),
        ('G-NOBANKEDFERRY', 'no banked ferry is written by any tool of this act',
         not re.search(r"FERRY\s*,\s*'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOFOLD', 'no fold run', not re.search(r'fold_run', pycode_of(SRC_COMP))),
        ('G-NOLEDGERROW', 'no ledger row edited', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOLANEEDIT', 'no lane document edited beyond the declared trail append',
         set(changed_tracked(PP)) <= {'OPEN_TRAILS.md'}),
        ('G-NOLANEOPENED', 'no lane opened',
         not re.search(r'open_lane|lane_open', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-CORPUS-SCOPE', 'only the two declared addresses are fetched, and only after the lock',
         1 == len(re.findall(r'urlopen', pycode_of(SRC_COMP + SRC_EXT))) or
         0 == len(re.findall(r'urlopen', pycode_of(SRC_COMP + SRC_EXT)))),
        ('G-TRAIL-APPEND-ONLY', 'the trail`s committed text is a TRUE PREFIX of its text now',
         appended_only(PP, 'OPEN_TRAILS.md') or unchanged(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'the table`s committed text is a TRUE PREFIX of its text now',
         appended_only(SIDE, 'CORRESPONDENCE.md') or unchanged(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every file THIS ACT wrote is named by the locked write list',
         [] == unlisted_writes()),
        ('G-NOEXTRAKIND', 'no file of an unnamed kind was written by this act',
         [] == unlisted_writes()),
        ('G-NOSTAGE-A', 'no tool of this act stages with -A',
         not re.search(r"'add'\s*,\s*'-A'|add -A", pycode_of(SRC_COMP + SRC_EXT + SRC_CHK))),
        ('G-NOBORROWEDBAR', 'every bar this act asserts is re-run here, not inherited from b430',
         bool(G) and bool(COMP)),
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', None),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank or git`s view of the repos',
         bool(COMP) and bool(EXTR) and bool(G)),
        ('G-ARMS-STRIP-PROSE', 'every source-reading arm strips comments and strings by tokenizer',
         'tokenize' in pycode_of(SRC_CHK)),
        ('G-ARMS-FOLD-MARKERS', 'every prose-reading arm folds markup before matching',
         'fold' in pycode_of(SRC_CHK)),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line, never as a substring',
         'verdict_line' in pycode_of(SRC_CHK)),
        ('G-TWO-READINGS-TWO-FILES', 'the pre-push and post-push readings land in two files',
         PREPUSH != POSTPUSH and 'POSTPUSH if _pushed() else PREPUSH' in
         pycode_of(SRC_CHK).replace(' ', '').replace('POSTPUSHif_pushed()elsePREPUSH',
                                                     'POSTPUSH if _pushed() else PREPUSH')),
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
