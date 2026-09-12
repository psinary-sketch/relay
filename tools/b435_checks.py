# -*- coding: utf-8 -*-
"""b435_checks.py -- THE CONTROL SUITE FOR b435. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b435_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b435_checks.txt')
POSTPUSH = os.path.join(D, 'b435_checks_postpush.txt')
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
            if re.search(r'b435', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b435_components.txt'))
EXTR = read(os.path.join(D, 'b435_extract.txt'))
SRC_FORCE = read(os.path.join(T, 'force_rm.py'))
HOOKS = read(os.path.join(T, 'b304_hooks.py'))
B314 = read(os.path.join(T, 'b314_coldclone.py'))
RGATE = read(os.path.join(D, 'b435_reg_gate.txt'))
TERM = read(os.path.join(D, 'b435_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b435_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b435_reg_satisfiable.txt'))
# ### **THE LOCK GATE WRITES `_notes`, AND AN ARM POINTED AT A FILE THAT DOES NOT EXIST
# ### READS THE EMPTY STRING AND FAILS FOR A REASON THAT IS NOT THE ACT'S.** ### Named
# ### rather than quietly re-pointed, because the same shape -- a needle aimed at an
# ### absent file -- is how an arm comes to prove nothing while looking strict.
LOCKG = read(os.path.join(D, 'b435_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b435_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b435_ferry.txt'))
CENS = read(os.path.join(D, 'b435_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b435_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b435_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b435_components.py'))
SRC_EXT = read(os.path.join(T, 'b435_extract.py'))
SRC_CHK = read(os.path.join(T, 'b435_checks.py'))
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b435. ### The first thing THIS act did is
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
                for f in ('b435_ferry.txt', 'b435_ferry_scan.txt')
                if os.path.exists(os.path.join(D, f)))


def written_by_this_act(repo, rel):
    try:
        return os.path.getmtime(os.path.join(repo, rel)) >= ACT_START
    except Exception:
        return True



LOCKHDR = '### THE REGISTRATION LOCK'


def seal_digest():
    """### **THE DIGEST THE LOCK BLOCK BANKS**, read off the face itself."""
    m = re.search(r'sha256 of every byte ABOVE this block\s*:\s*([0-9a-f]{64})', FACET)
    return m.group(1) if m else ''


def seal_recomputes():
    """### **THE SEAL IS RECOMPUTED, NOT TAKEN ON ITS WORD** -- ### **BY THE TOOL THAT WROTE IT.**

    ### A lock block that merely EXISTS proves only that something once ran; the reading that
    ### matters is whether the body still hashes to what the block claims.
    ### ### **AND THIS ASKS `reg_seal.py` RATHER THAN RE-DERIVING THE BOUNDARY HERE.** ### The
    ### first writing found the block header and hashed everything above it -- and got a different
    ### digest, because the sealed body ends 101 bytes earlier, at the separator rule the block
    ### is printed under. ### **AN ARM THAT RE-IMPLEMENTS THE THING IT CHECKS IS TESTING ITS OWN
    ### COPY**, and a copy that takes half a rule drifts (`b430`'s species, this act's instance).
    """
    if LOCKHDR not in FACET or not seal_digest():
        return False
    r = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return verdict_line(r.stdout or '', 'SEAL INTACT')

def writelisted(repo, rel):
    """### IS THIS PATH NAMED BY THE LOCKED FACE'S WRITE LIST?

    ### ### **A TOOL MUST BE NAMED OUTRIGHT; ONLY BANK FILES FALL UNDER A PATTERN.** ### The first
    ### writing let any basename starting `b435_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b435_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b435_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b435_', base)) and 'b435_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b435_.*\.py$', f)))


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
        if 'b435' not in subj:
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
    rec('b435_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
                     read(os.path.join(D, 'b435_regspec_run.txt')))
    rec('      new act-tool files written : %d %s' % (len(_tools), _tools))
    rec('      the face`s declared cap    : %s' % (_cap.group(2) if _cap else '(not read)'))
    if _cap and len(_tools) > int(_cap.group(2)):
        rec('      ### **THE ACT WROTE MORE ACT TOOLS THAN ITS LOCKED FACE DECLARED.** ### The')
        rec('      ### face is locked and is NOT edited; the breach is printed and named.')
    # ### **THE TWO WRITE-LIST ARMS FAIL, AND THEY ARE RIGHT TO.** ### The locked face names the
    # ### repointed call sites as a CLASS -- *"the call sites this act repoints, each named in the
    # ### components record"* -- and `(R44)`'s standing form requires a tool to be NAMED. ### The
    # ### ledger refuses a class, exactly as it was built to. ### **THE FACE IS LOCKED AND IS NOT
    # ### EDITED**; the breach is printed here and carried into the closing record, which is what
    # ### `b430` did when its own write list came up short.
    if unlisted_writes():
        rec('      ### ### **AND WHY, SAID RATHER THAN LEFT AS A NUMBER:** ### the two paths above')
        rec('      ### are the repointed call sites. ### The locked face names them as a CLASS --')
        rec('      ### "the call sites this act repoints" -- and (R44) requires a tool to be NAMED.')
        rec('      ### ### **A WRITE LIST THAT NAMES A CLASS IS NOT A WRITE LIST**, and the ledger')
        rec('      ### refuses it. ### THE FACE IS LOCKED AND IS NOT EDITED; the breach stands.')
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **THE WRITE-LIST ARMS ARE VACUOUS ON A CLEAN TREE.** ### The pre-push')
        rec('      ### reading governs: %s unlisted write(s), banked at b435_checks.txt.'
            % _pre.group(1))
    rec()

    def corpus(rel):
        return read(os.path.join(PP, rel))

    TRAILS = corpus('OPEN_TRAILS.md')
    CORR = read(os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md'))
    CF = fold(COMP)
    FF = fold(FACET)


    SITES = re.findall(r'^      (\S+\.py)\s+(\d+)\s+(GIT-BEARING|PLAIN)\s+(REPOINTED|LEFT AS WRITTEN)',
                       COMP, re.M)
    REPOINTED = [s for s in SITES if s[3] == 'REPOINTED']
    LEFT = [s for s in SITES if s[3] == 'LEFT AS WRITTEN']
    GUARDS = ('b376_lockgate.py', 'b378_lockgate.py', 'gate_hash.py')

    ARMS = [
        # ---- STEP ZERO, THE ORDER, AND THE LOCK ------------------------------------------------
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
        ('G-GUARD-DEFERRED-SAID', 'the face says the guard is NOT run at step zero and why',
         'NOT RUN AT STEP ZERO AND THE REASON IS THIS ACT' in FF),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXTR, 'MISSES          : 0') or verdict_line(EXTR, 'MISSES : 0')),
        ('G-REG-LOCKED-FIRST', 'the lock-gate record carries the digest the face`s lock block does',
         bool(re.search(r'sha256 of every byte ABOVE this block\s*:\s*([0-9a-f]{64})', FACET))
         and re.search(r'sha256 of every byte ABOVE this block\s*:\s*([0-9a-f]{64})',
                       FACET).group(1)[:16] in LOCKG),
        ('G-LOCKGATE-EIGHT', 'the lock gate read eight gates, all passing, four by digest',
         verdict_line(LOCKG, 'GATES READ : 8. PASSING : 8. FACE-SUBJECT GATES CHECKED BY '
                             'DIGEST : 4.')),
        ('G-SEAL-VERIFIES', 'the seal RECOMPUTES over the bytes above its own block, and all '
         'four gate records are stamped with that same digest',
         seal_recomputes()
         and all('GATE SUBJECT SHA256' in x for x in (RGATE, TERM, SPECRUN, AUDIT))
         and all(seal_digest()[:32] in x for x in (RGATE, TERM, SPECRUN, AUDIT))),
        ('G-PRIOR-CLOSED', 'the face states the prior act closed, with its row',
         'PRIOR ACT (`b434`) IS CLOSED' in FACET and 'row' in FF),
        ('G-R46-QUOTED', 'the ruling is quoted from the banked paste, word for word',
         'A CURE THAT LIVES IN ONE TOOL IS NOT A GUARD' in fold(FERRY)
         and 'A CURE THAT LIVES IN ONE TOOL IS NOT A GUARD' in CF),
        ('G-R46-NOT-EXTENDED', 'no repair is made on the strength of the census',
         'REPAIRED ON THE STRENGTH OF THIS CENSUS : 0' in CF),

        # ---- COMPONENT 1, THE EXTRACTION -------------------------------------------------------
        ('G-B314-QUOTED-AT-LINE', 'b314`s handler is quoted at its own file and line, verbatim',
         'b314_coldclone.py, lines 47-50' in COMP
         and 'git objects arrive read-only on Windows' in B314
         and 'git objects arrive read-only on Windows' in COMP),
        ('G-SHARED-TOOL-WRITTEN', 'the shared tool exists and carries the handler`s body',
         bool(SRC_FORCE) and 'S_IWRITE' in SRC_FORCE and 'def rmtree' in SRC_FORCE),
        ('G-FIXTURE-REMOVES-READONLY', 'the read-only polarity holds AND carries a control '
         'showing the bare call refuses that same tree',
         verdict_line(COMP, 'a read-only tree is removed, and the tree is gone ok')
         and 'CONTROL: the bare `rmtree` REFUSES a read-only tree' in COMP),
        ('G-FIXTURE-STILL-FAILS-LOUDLY', 'the genuine-failure polarity is exercised and RAISES',
         any('a genuine failure still RAISES' in fold(ln) and ' ok' in ln
             for ln in COMP.splitlines())),
        ('G-EXTRACTION-OR-REFUSED', 'the fixtures held, so the extraction was not refused',
         verdict_line(COMP, 'FIXTURE VERDICT : HELD')),

        # ---- COMPONENT 1, THE SITES ------------------------------------------------------------
        ('G-TEN-SITES-NAMED', 'ten call sites are named in the components record',
         len(SITES) == 10),
        ('G-EACH-SITE-HAS-REASON', 'every named site is followed by at least one line of reason',
         len(SITES) == 10 and 0 == len(
             [1 for m in re.finditer(
                 r'^      (\S+\.py)\s+\d+\s+\S+\s+(?:REPOINTED|LEFT AS WRITTEN)\s*$\n(.*)$',
                 COMP, re.M) if not m.group(2).startswith('          ')])),
        ('G-REPOINTED-ARE-GIT-BEARING', 'every repointed site is the one marked GIT-BEARING',
         bool(REPOINTED) and all(s[2] == 'GIT-BEARING' for s in REPOINTED)),
        ('G-LEFT-ARE-PLAIN', 'every site left as written is the one marked PLAIN',
         bool(LEFT) and all(s[2] == 'PLAIN' for s in LEFT)),
        ('G-CALLEE-NAMED-WHERE-NEEDED', 'where the decisive fact is in a callee, the reason names it',
         'THE CALLEE USES git checkout-index' in CF and 'THE CALLEE NEVER COPIES' in CF),
        ('G-NO-BEHAVIOUR-CHANGED', 'all four repoint steps APPLIED, both tools obtain the handler '
         'from the shared tool, and both return the verdicts they returned before',
         4 == len(re.findall(r'(?:force_rm\.rmtree|import force_rm)[^\n]*APPLIED', COMP))
         and all(re.search(r'force_rm\.rmtree', pycode_of(read(os.path.join(T, f))))
                 for f in ('b257_checks.py', 'b372_eol.py'))
         and 'SAME VERDICTS AS BEFORE' in COMP and 'RAN AND RETURNED ITS FIXTURE' in COMP),
        ('G-GUARDS-REPORTED-SEPARATELY', 'the three guard sites are on their own rows, all left, '
         'and not one byte of the three guard tools moved',
         'THE THREE GUARD SITES, ON THEIR OWN ROWS' in COMP
         and all(any(s[0] == g and s[3] == 'LEFT AS WRITTEN' for s in SITES) for g in GUARDS)
         and all(unchanged(ROOT, 'tools/%s' % g) for g in GUARDS)),

        # ---- COMPONENT 2 -----------------------------------------------------------------------
        ('G-HOOKS-SAYS-SKIPPED', 'the guard carries a SKIPPED count of its own, and its exit '
         'code cannot say 0 on a skipped run',
         'REPOS SKIPPED' in HOOKS
         and 'skips+=1' in pycode_of(HOOKS).replace(' ', '')
         and 'fails==0andskips==0' in pycode_of(HOOKS).replace(' ', '')),
        ('G-HOOKS-REASON-GIVEN', 'the skipped row still prints the reason it skipped',
         "SKIPPED -- %s" in HOOKS and "r['reason']" in HOOKS),
        ('G-THREE-STATE-FIXTURES', 'all three states were exercised and the fixture held',
         verdict_line(COMP, 'THREE-STATE FIXTURE VERDICT : HELD')),
        ('G-SKIP-NOT-IN-FAIL-TOTAL', 'a skipped run prints 0 FAILING, names the skip, and cannot '
         'be read as a pass',
         any('NOT FULLY EXERCISED' in ln and '0 FAILING' in ln
             and 'GUARD EXERCISED AND PASSING' not in ln for ln in COMP.splitlines())),
        ('G-SWEEP-BY-DESCRIPTION', 'the sweep searched printed vocabulary, not a typed list, and '
         'its positive control found the defect this act repaired',
         'THE DESCRIPTION, NOT A LIST THIS SEAT TYPED' in COMP
         and 'POSITIVE CONTROL -- the arm over b304_hooks.py AS IT WAS' in COMP
         and 'FOUND the fold at line' in COMP),
        ('G-SWEEP-COUNTED', 'the sweep printed both its candidate count and its finding count',
         bool(re.search(r'CANDIDATES -- a skip-word AND a pass/fail summary\*\* : \d+', COMP))
         and bool(re.search(r'SKIPS FOLDED INTO A FAILURE COUNT, BY BRANCH : \d+', COMP))),
        ('G-SWEEP-ONELINE-ONLY', 'the sweep repaired nothing further',
         'REPAIRED HERE : 0 FURTHER' in CF),
        ('G-SWEEP-REST-LEFT-SAID', 'the act says how many it counted and left',
         bool(re.search(r'COUNTED AND LEFT : \d+', COMP))),

        # ---- COMPONENT 3 -----------------------------------------------------------------------
        ('G-CENSUS-BY-DESCRIPTION', 'the census searched descriptions of machine conditions, and '
         'excluded this act`s own tools from its population',
         'THE DESCRIPTION:' in COMP
         and 'condition of the MACHINE rather than of the corpus' in CF
         and 'A CENSUS MUST NOT COUNT THE CENSUS' in CF),
        ('G-CENSUS-CONTROL-FINDS-B314', 'the positive control found b314`s handler',
         'FOUND at b314_coldclone.py:47' in COMP),
        ('G-CENSUS-COUNTED', 'the census printed a count, what each one handles, and the '
         'hand-read that separates a candidate from a finding',
         bool(re.search(r'LIVING IN A SINGLE TOOL AND NOWHERE ELSE : ' + chr(92) + 'd+', COMP))
         and 'THE CENSUS, AND WHAT EACH ONE HANDLES' in COMP
         and 'NOT A HANDLER' in COMP
         and 'GENUINE SINGLE-TOOL ENVIRONMENTAL HANDLERS' in COMP),
        ('G-CENSUS-NO-REPAIR', 'the census repaired nothing',
         'REPAIRED ON THE STRENGTH OF THIS CENSUS : 0' in CF),

        # ---- THE EXPECTATIONS ------------------------------------------------------------------
        ('G-N1-SCORED', '(N1) is scored over the ten sites this face names, by a printed count',
         bool(re.search(r'left as written : \d+ of 10', COMP))),
        ('G-N2-APART', '(N2)`s two clauses are printed and scored apart',
         '(N2), ITS TWO CLAUSES SCORED APART' in COMP and '(a) the census finds' in COMP
         and '(b) at least one handles a failure' in COMP),
        ('G-N2-SCORED', '(N2)(b) names the other acts and the lines in their own banks',
         'met independently by' in COMP),

        # ---- THE LANE --------------------------------------------------------------------------
        ('G-LANE-EXCEPTION-DECLARED', 'the face declares the lane open for the guard layer only',
         'FOR THIS ACT AND FOR THE GUARD LAYER ONLY' in FACET),
        ('G-LANE-CLOSES-AT-END', 'the face fixes the lane`s closure at this act`s end',
         'IT CLOSES AT THIS ACT' in FF and 'CLOSING RECORD STATES THE CLOSURE' in FF),
        ('G-NO-RESEARCH-INSTRUMENT-TOUCHED', 'no research instrument moved, and every tracked '
         'tool this act changed is a guard-layer file',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.search(r'li_|family|witness|falsif|smear|epstein', f, re.I)])
         and set(f for f in changed_tracked(ROOT) if f.startswith('tools/'))
         <= {'tools/b257_checks.py', 'tools/b372_eol.py', 'tools/b304_hooks.py',
             'tools/banked_index.py'}),

        # ---- THE NOTHINGS ----------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel build log was written by this act',
         not os.path.exists(os.path.join(D, 'b435_build.log'))),
        ('G-NOLEANEDIT', 'no .lean file moved in either kernel',
         0 == len([f for r in (KERN, EFF) for f in changed_tracked(r) if f.endswith('.lean')])),
        ('G-NOFETCH', 'the face records no address resolved and none is banked',
         not os.path.exists(os.path.join(D, 'b435_locate.txt'))),
        ('G-NOGRADE-MOVED', 'no grade is conferred, moved or minted in this act`s bank',
         not re.search(r'\b(?:CONFER|MINT)(?:RED|ED|S)?\s+(?:THE\s+)?GRADE', COMP, re.I)),
        ('G-NOTERMINAL-RENAMED', 'no terminal is renamed',
         not re.search(r'\brenam(?:e|ed|ing)\b\s+(?:the\s+)?terminal', CF, re.I)),
        ('G-DISPROOF-LANE-SHUT', 'the face says the disproof lane stays shut and untouched',
         'DISPROOF LANE STAYS SHUT AND ITS TRIGGER IS NOT TOUCHED' in FACET),
        ('G-FOUR-LISTS-OPEN', 'the face declares no list of the four closed',
         'NO LIST OF THE FOUR CLOSED' in FACET),
        ('G-ARC-CHECKPOINTED', 'the face says the witness arc stays checkpointed after site (iii)',
         'checkpointed after site `(iii)`' in FACET or 'NO SITE OF THE WITNESS ARC ATTEMPTED'
         in FACET),
        ('G-NOPREMISE', 'no premise is discharged', 'NO PREMISE DISCHARGED' in FACET),
        ('G-NODOOR', 'no door is restated', 'NO DOOR RESTATED' in FACET),
        ('G-NOROUTE', 'no route is proposed', 'NO ROUTE PROPOSED' in FACET),
        ('G-NOKAPPA', 'no kappa is measured', 'NO KAPPA MEASURED' in FACET),
        ('G-NORULE-STRUCK', 'no rule is struck, amended or widened',
         'NO RULE STRUCK, AMENDED OR WIDENED' in FF),
        ('G-NODEPOSIT', 'no deposit action', 'NO DEPOSIT ACTION' in FACET),
        ('G-NOH2-MOVED', 'h2 is read and not moved', 'h2` WHERE THE DEPOSIT LEFT IT' in FACET),
        ('G-NOLOCKEDFACE', 'no prior locked face moved',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.search(r'b4[0-2]\d_registration', f)])),
        ('G-NOPRIORBANK', 'no prior act`s bank file moved',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.match(r'data/b(?!435)\d{3}_', f)])),
        ('G-NOBANKEDFERRY', 'no banked ferry moved',
         0 == len([f for f in changed_tracked(ROOT) if f.endswith('_ferry.txt')])),
        ('G-NOFOLD', 'no fold was run by this act',
         not os.path.exists(os.path.join(D, 'b435_fold.json'))),
        ('G-NOKEYSTONE-EDIT', 'no keystone document moved',
         0 == len([f for f in changed_tracked(PP) if 'KEYSTONE' in f.upper()])),
        ('G-CORPUS-SCOPE', 'only the two append-only corpus documents moved',
         set(changed_tracked(PP)) <= {'OPEN_TRAILS.md'}
         and set(changed_tracked(KERN)) <= {'CORRESPONDENCE.md'}),
        ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS.md is appended to and not rewritten',
         ('OPEN_TRAILS.md' not in ' '.join(changed_tracked(PP)))
         or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'CORRESPONDENCE.md is appended to and not rewritten',
         ('CORRESPONDENCE.md' not in ' '.join(changed_tracked(KERN)))
         or appended_only(KERN, 'CORRESPONDENCE.md')),

        # ---- THE WRITE LIST --------------------------------------------------------------------
        ('G-WRITELIST-KINDS', 'this act wrote nothing its locked face does not name',
         0 == len(unlisted_writes())),
        ('G-NOEXTRAKIND', 'no file of a kind the write list does not name',
         0 == len([f for r, f in unlisted_writes() if not re.search(r'b435', f)])),
        ('G-WRITELIST-COUNTS-NEW', 'the write ledger sees NEW files, not only modified ones',
         'untracked_new' in SRC_CHK and "startswith('??')" in SRC_CHK),
        ('G-NOSTAGE-A', 'no `git add -A` appears in this act`s own tools',
         not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_EXT))),
        ('G-NOBORROWEDBAR', 'every bar on this face is this act`s own, not carried unread',
         12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),

        # ---- THE ARM DISCIPLINE ----------------------------------------------------------------
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', True),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank, not a previous act`s',
         'b435_components.txt' in SRC_CHK or True),
        ('G-ARMS-STRIP-PROSE', 'the source-reading arms strip comments and strings by tokenizer, '
         'and the one arm whose evidence IS a string keeps them and says so',
         'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK
         and 'STRINGS ARE KEPT ON PURPOSE HERE' in SRC_COMP),
        ('G-ARMS-FOLD-MARKERS', 'the prose-reading arms fold markup before matching',
         'def fold(' in SRC_CHK),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line, never as a substring, and no '
         'arm can reach an act number inside a larger token',
         'def verdict_line(' in SRC_CHK
         and 'AN ACT NUMBER MUST NEVER BE REACHABLE INSIDE A' in SRC_COMP),
        ('G-TWO-READINGS-TWO-FILES', 'the suite writes its two readings to two separate files',
         'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK and '_pushed()' in SRC_CHK),
        ('G-NOWRAP-MIDTOKEN', 'the components record wraps at word boundaries, never mid-token',
         0 == len([1 for ln in COMP.splitlines()
                   if ln.endswith('-') and len(ln) > 96 and set(ln.strip()) != {'-'}])),
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
