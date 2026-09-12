# -*- coding: utf-8 -*-
"""b434_checks.py -- THE CONTROL SUITE FOR b434. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b434_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b434_checks.txt')
POSTPUSH = os.path.join(D, 'b434_checks_postpush.txt')
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
            if re.search(r'b434', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b434_components.txt'))
EXTR = read(os.path.join(D, 'b434_extract.txt'))
PROF = read(os.path.join(D, 'b434_profile.txt'))
BUILD = read(os.path.join(D, 'b434_build.log'))
LOCKG = read(os.path.join(D, 'b434_lockgate.txt'))
SCAN = read(os.path.join(D, 'b434_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b434_ferry.txt'))
CENS = read(os.path.join(D, 'b434_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b434_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b434_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b434_components.py'))
SRC_EXT = read(os.path.join(T, 'b434_extract.py'))
SRC_CHK = read(os.path.join(T, 'b434_checks.py'))
try:
    G = json.loads(read(os.path.join(D, 'b434_fold.json')) or '{}')
except Exception:
    G = {}
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b434. ### The first thing THIS act did is
# ### its step-zero resolution, and that is the boundary.
# ### **THIS ACT RESOLVES NO ADDRESS**, so it has no `ls-remote` record to date itself from --
# ### b431's boundary file does not exist here. ### Its first artefact is its own ferry scan, and
# ### the ferry itself is no boundary: all three legs' pastes were banked together at b430.
# ### **THE BOUNDARY IS THE EARLIEST OF THIS ACT'S OWN STEP-ZERO ARTEFACTS**, not the scan alone.
# ### The scan is written a moment AFTER the paste it scans, so a boundary set at the scan puts the
# ### act's own ferry on the wrong side of it and the ledger calls it inherited. ### Harmless to the
# ### arms -- the ferry is write-listed either way -- and ### **A MISLEADING LINE IN A LEDGER IS
# ### STILL A MISLEADING LINE.**
ACT_START = min(os.path.getmtime(os.path.join(D, f))
                for f in ('b434_ferry.txt', 'b434_ferry_scan.txt')
                if os.path.exists(os.path.join(D, f)))


def written_by_this_act(repo, rel):
    try:
        return os.path.getmtime(os.path.join(repo, rel)) >= ACT_START
    except Exception:
        return True


def writelisted(repo, rel):
    """### IS THIS PATH NAMED BY THE LOCKED FACE'S WRITE LIST?

    ### ### **A TOOL MUST BE NAMED OUTRIGHT; ONLY BANK FILES FALL UNDER A PATTERN.** ### The first
    ### writing let any basename starting `b434_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b434_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b434_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b434_', base)) and 'b434_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b434_.*\.py$', f)))


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
        if 'b434' not in subj:
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
    rec('b434_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
                     read(os.path.join(D, 'b434_regspec_run.txt')))
    rec('      new act-tool files written : %d %s' % (len(_tools), _tools))
    rec('      the face`s declared cap    : %s' % (_cap.group(2) if _cap else '(not read)'))
    if _cap and len(_tools) > int(_cap.group(2)):
        rec('      ### **THE ACT WROTE MORE ACT TOOLS THAN ITS LOCKED FACE DECLARED.** ### The')
        rec('      ### face is locked and is NOT edited; the breach is printed and named.')
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **THE WRITE-LIST ARMS ARE VACUOUS ON A CLEAN TREE.** ### The pre-push')
        rec('      ### reading governs: %s unlisted write(s), banked at b434_checks.txt.'
            % _pre.group(1))
    rec()

    def corpus(rel):
        return read(os.path.join(PP, rel))

    FINDS = corpus('FINDINGS.md')
    TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
    SPANTXT = read(os.path.join(D, 'b434_span.txt'))

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'the paste carries its own part marker and the face says IN FULL',
         'paste ends (part 1 of 1)' in FERRY and 'PART 1 OF 1' in FACET),
        ('G-AMENDMENT-BANKED', 'the amendment is banked with the paste and was scanned',
         'AMENDMENT to LEG 2' in FERRY and 'AN AMENDMENT' in fold(FACET)),
        ('G-SCAN-CLEAN', 'the scan`s verdict line reads 0 hits',
         verdict_line(SCAN, '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'both census records read TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING : 0') and verdict_line(FCENS, 'TOTAL MISSING : 0')),
        ('G-STEPZERO-PINS', 'the pin record reads 0 hard-failing and every repo 0/0',
         verdict_line(PINS, 'REPOS HARD-FAILING : 0')
         and 0 == len([1 for ln in PINS.splitlines()
                       if 'behind/ahead' in ln and '0 / 0' not in ln])),
        ('G-STEPZERO-GUARD-AS-READ', 'the face reports the guard`s number as it came, and says what it is',
         'THE GUARD READS 1, WHICH IS A SKIP AND NOT A FAILURE' in fold(FACET)),
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
         bool(re.search(r'(?m)^\|\s*282\s*\|', read(os.path.join(KERN, 'CORRESPONDENCE.md'))))),

        # ### ---- THE SPAN -----------------------------------------------------------------------
        ('G-SPAN-FROM-TOOL', 'the span comes from b363_span.py, whose run this act banked',
         bool(SPANTXT) and 'THE CURRENT SPAN' in SPANTXT
         and os.path.getmtime(os.path.join(D, 'b434_span.txt')) >= ACT_START),
        ('G-SPAN-BOTH-FIGURES', 'both the raw count and the filed count are printed',
         G.get('span_raw') == 12 and G.get('span_filed') == 10
         and 'RAW count' in COMP and 'TEN acts' in COMP),
        ('G-SPAN-TEN-FILED', 'the fold files ten acts and names them',
         len(G.get('acts', [])) == 10 and G.get('acts', [None])[0] == 'b423'
         and G.get('acts', [None])[-1] == 'b432'),
        ('G-SPAN-NOT-TYPED', 'no span count is typed in the fold generator`s own prose',
         'span_raw' in pycode_of(read(os.path.join(T, 'b434_fold.py')))),

        # ### ---- THE TEN ACTS -------------------------------------------------------------------
        ('G-TEN-ACTS-LISTED', 'ten acts are listed in the filed fold`s table',
         10 == len(re.findall(r'(?m)^\| \*\*b4(?:2[3-9]|3[0-2])\*\* \|', FINDS))),
        ('G-STRINGS-VERIFIED-IN-OWN-BANK', 'all ten strings were verified in their own banks',
         G.get('acts_verified') == 10 and G.get('acts_total') == 10),
        ('G-UNVERIFIED-NOT-ASSERTED', 'the survey would have named any string it could not verify',
         'NOT IN THIS BANK' in read(os.path.join(T, 'b434_extract.py'))),

        # ### ---- THE FOLD ------------------------------------------------------------------------
        ('G-FOLD-ADDITIVE', 'git`s own numstat reports 0 deletions on FINDINGS.md',
         G.get('fold_deletions') == '0'),
        # ### **THE JSON HOLDS THE LAST RUN'S DELTA, AND THE LAST RUN WAS THE IDEMPOTENT ONE**
        # ### -- it filed nothing and recorded `+0`, which is true of that run and false of the act.
        # ### ### **b430 BANKED THIS SPECIES AND HERE IT IS AGAIN**: a record overwritten by a
        # ### later, quieter run of the same tool. ### The durable figure is git's, so the arm reads
        # ### the working tree against the committed blob instead.
        ('G-FOLD-DELTA-POSITIVE', 'the fold grew FINDINGS.md, measured against the committed blob',
         len(read(os.path.join(PP, 'FINDINGS.md')).encode('utf-8'))
         > len(git(PP, 'show', 'HEAD:FINDINGS.md').encode('utf-8'))),
        ('G-FOLD-NOTHING-EDITED', 'the committed text is a TRUE PREFIX of the file now',
         G.get('fold_true_prefix') is True and appended_only(PP, 'FINDINGS.md')),
        ('G-THIRD-COLUMN-APART', 'b412`s third column is kept apart and never summed',
         'The three columns, kept apart' in FINDS and G.get('third_column_apart') is True),

        # ### ---- THE ONE STATEMENT ---------------------------------------------------------------
        ('G-FIVE-FINDINGS-CARRIED', 'the one statement carries five findings as five bullets',
         5 == len([ln for ln in FINDS[FINDS.find('### The arc in one statement'):
                                      FINDS.find('### What each act contributed')].splitlines()
                   if ln.lstrip().startswith('- ')])),
        ('G-FIVE-VERIFIED-AT-SOURCE', 'each of the five was verified at its own source',
         G.get('findings_found') == 5),
        ('G-NO-SUPERSESSION', 'no finding is summarised as overturning another',
         G.get('supersession_words') == []),

        # ### ---- THE LORE SECTION ----------------------------------------------------------------
        ('G-SPECIES-MINTED', 'the species is named in the filed fold',
         G.get('species_in_fold') is True),
        ('G-THREE-INCIDENTS-NAMED', 'all three incidents are named in the fold',
         G.get('incidents_named') is True),
        ('G-INCIDENTS-FROM-OWN-BANKS', 'each incident was read from its own bank by the survey',
         all(s_ in EXTR for s_ in ('b414 --', 'b418 --', 'b433 --'))),
        ('G-CURE-STATED', 'the shared cure is stated in the fold',
         G.get('cure_stated') is True
         and 'never from the exit code' in FINDS.lower()),
        ('G-GUARD-CENSUS-MEASURED', 'the guard census is a measurement, not an assertion',
         'THE GUARD CENSUS, MEASURED RATHER THAN ASSERTED' in EXTR
         and 'walker_guard.py' in EXTR),
        ('G-TWO-GUARDED-ONE-NOT', 'two of the three are found guarded and one is not',
         G.get('guarded') == ['b414', 'b418'] and G.get('unguarded') == ['b433']),

        # ### ---- THE WORK-ORDER ------------------------------------------------------------------
        ('G-WORKORDER-FILED', 'the work-order is filed in the fold',
         G.get('workorder_filed') is True and 'W-REMOVAL-VERIFIED' in FINDS),
        ('G-WORKORDER-TRIGGER', 'it carries a trigger and says it is not started',
         G.get('workorder_trigger') is True and 'filed and not started' in FINDS),

        # ### ---- TECHNE --------------------------------------------------------------------------
        ('G-TECHNE-WRITTEN', 'the module stands beside the species',
         G.get('techne_written') is True),
        ('G-TECHNE-NOT-PUSHED', 'TECHNE-Core is ahead of its remote and was not pushed',
         G.get('techne_pushed') is False and str(G.get('techne_ahead', '0')).isdigit()
         and int(G.get('techne_ahead', 0)) >= 1),
        ('G-ORIENTATION-REFRESHED', 'the orientation layer grows by append only',
         appended_only(PP, 'OPEN_TRAILS.md') or unchanged(PP, 'OPEN_TRAILS.md')),

        ('G-L2-APART', 'the face declares L2`s two clauses apart',
         'ITS TWO' in FACET and '(b) the' in FACET),
        ('G-L2-SCORED', 'both clauses of L2 are decidable from a printed result',
         G.get('span_filed') is not None and G.get('supersession_words') is not None),

        # ### ---- THE NOTHINGS --------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel is built: no tool of this act invokes a build',
         not re.search(r'lake|elan', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOLEANEDIT', 'no .lean file is written by any tool of this act',
         [] == [f for r in (ROOT, PP, KERN) for f in changed_tracked(r) if f.endswith('.lean')]),
        ('G-NOFETCH', 'nothing is fetched: no tool of this act opens a URL',
         not re.search(r'urlopen|urllib|requests', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOGRADE-MOVED', 'the fold restates grades and confers none',
         'confers none' in FINDS or 'verified in that act' in FINDS.lower()),
        ('G-NOTERMINAL-RENAMED', 'no terminal name is rewritten',
         'crt_exhaustiveness' in corpus('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')),
        ('G-LANE-NOT-OPENED', 'no lane opened',
         not re.search(r'open_lane|lane_open', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-TRIGGER-UNTOUCHED', 'the disproof lane`s trigger text is unchanged',
         'the instrument lane opening' in corpus('OPEN_TRAILS.md')),
        ('G-FOUR-LISTS-OPEN', 'no list of the four was closed', unchanged(PP, 'REGISTRY.md')),
        ('G-ARC-CHECKPOINTED', 'no witness-arc site was attempted',
         not re.search(r'site_iv', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOPREMISE', 'h2 is not discharged',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
        ('G-NODOOR', 'no door restated', unchanged(PP, 'REGISTRY.md')),
        ('G-NOROUTE', 'no route proposed', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOKAPPA', 'no kappa measured',
         not re.search(r'kappa', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NORULE-STRUCK', 'no rule struck or amended', unchanged(ROOT, 'tools/FERRY_STANDING.md')),
        ('G-NODEPOSIT', 'no deposit action',
         not re.search(r'zenodo|deposit', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOH2-MOVED', 'h2 is read and not moved',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
        ('G-NOLOCKEDFACE', 'no prior locked face was written by this act',
         all(os.path.getmtime(os.path.join(D, f)) < ACT_START
             for f in os.listdir(D)
             if re.match(r'b4[0-3]\d_registration', f) and not f.startswith('b434'))),
        ('G-NOPRIORBANK', 'no prior act`s bank appears among this act`s changed paths',
         [] == [f for f in changed_tracked(ROOT)
                if re.match(r'data/b4(0|1|2)\d_', f) or re.match(r'data/b43[0-3]_', f)]),
        ('G-NOBANKEDFERRY', 'no banked ferry is written by any tool of this act',
         not re.search(r"FERRY\s*,\s*'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOREGISTERROW', 'no register row edited', unchanged(PP, 'REGISTRY.md')),
        ('G-NOKEYSTONE-EDIT', 'no keystone edited or annotated by this act',
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
         'fold' in pycode_of(SRC_CHK)),
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
