# -*- coding: utf-8 -*-
"""b439_checks.py -- THE CONTROL SUITE FOR b439. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b439_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b439_checks.txt')
POSTPUSH = os.path.join(D, 'b439_checks_postpush.txt')
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
            if re.search(r'b439', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b439_components.txt'))
EXTR = read(os.path.join(D, 'b439_extract.txt'))
LED = read(os.path.join(PP, 'FACES_LEDGER.md'))
WINREPO = os.path.join('D:', os.sep, 'SIDE-window')
ATLAS = read(os.path.join(T, 'e16', 'carto_atlas.py'))
SMEAR = read(os.path.join(T, 'b317_smear.py'))
WINDOW = read(os.path.join(T, 'b321_window.py'))
RGATE = read(os.path.join(D, 'b439_reg_gate.txt'))
TERM = read(os.path.join(D, 'b439_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b439_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b439_reg_satisfiable.txt'))
# ### **THE LOCK GATE WRITES `_notes`, AND AN ARM POINTED AT A FILE THAT DOES NOT EXIST
# ### READS THE EMPTY STRING AND FAILS FOR A REASON THAT IS NOT THE ACT'S.** ### Named
# ### rather than quietly re-pointed, because the same shape -- a needle aimed at an
# ### absent file -- is how an arm comes to prove nothing while looking strict.
LOCKG = read(os.path.join(D, 'b439_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b439_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b439_ferry.txt'))
CENS = read(os.path.join(D, 'b439_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b439_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b439_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b439_components.py'))
SRC_EXT = read(os.path.join(T, 'b439_extract.py'))
SRC_CHK = read(os.path.join(T, 'b439_checks.py'))
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b439. ### The first thing THIS act did is
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
                for f in ('b439_ferry.txt', 'b439_ferry_scan.txt')
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
    ### writing let any basename starting `b439_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b439_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b439_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b439_', base)) and 'b439_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b439_.*\.py$', f)))


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
        if 'b439' not in subj:
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
    rec('b439_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
    _cap = re.search(r'new `relay` act-tool files[^|]*?demand (\d+)\s+cap (\d+)',
                     read(os.path.join(D, 'b439_regspec_run.txt')))
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
        rec('      ### reading governs: %s unlisted write(s), banked at b439_checks.txt.'
            % _pre.group(1))
    rec()

    def corpus(rel):
        return read(os.path.join(PP, rel))

    TRAILS = corpus('OPEN_TRAILS.md')
    CORR = read(os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md'))
    CF = fold(COMP)
    FF = fold(FACET)






    try:
        PRICE = json.loads(read(os.path.join(D, 'b439_price.json')) or '{}')
    except Exception:
        PRICE = {}
    try:
        PROF = json.loads(read(os.path.join(D, 'b439_profile.json')) or '[]')
    except Exception:
        PROF = []
    try:
        WTS = json.loads(read(os.path.join(D, 'b439_weights.json')) or '[]')
    except Exception:
        WTS = []
    try:
        U0 = json.loads(read(os.path.join(D, 'b439_u0.json')) or '{}')
    except Exception:
        U0 = {}
    SRC_EXTP = read(os.path.join(T, 'b439_extract.py'))
    SMEAR = read(os.path.join(T, 'b317_smear.py'))
    C2 = PRICE.get('c2') or {}
    C3 = PRICE.get('c3') or {}

    ARMS = [
        # ---- STEP ZERO AND THE LOCK -------------------------------------------------------------
        ('G-RECEIPT-IN-FULL', 'the paste carries its own part marker and the face says IN FULL',
         'paste ends (part 1 of 1)' in FERRY and 'PART 1 OF 1' in FACET),
        ('G-SCAN-CLEAN', 'the scan`s verdict line reads 0 hits',
         verdict_line(SCAN, '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'both census records read TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING : 0') and verdict_line(FCENS, 'TOTAL MISSING : 0')),
        ('G-STEPZERO-PINS', 'the pin record reads 0 hard-failing',
         verdict_line(PINS, 'REPOS HARD-FAILING : 0')),
        ('G-GUARD-DEFERRED-SAID', 'the face says the guard runs at the close',
         'guard runs' in FF.lower() and 'at the close' in FF.lower()),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXTR, 'MISSES          : 0') or verdict_line(EXTR, 'MISSES : 0')),
        ('G-REG-LOCKED-FIRST', 'the lock-gate record carries the digest the face`s lock block does',
         bool(seal_digest()) and seal_digest()[:16] in LOCKG),
        ('G-LOCKGATE-EIGHT', 'the lock gate read eight gates, all passing, four by digest',
         verdict_line(LOCKG, 'GATES READ : 8. PASSING : 8. FACE-SUBJECT GATES CHECKED BY '
                             'DIGEST : 4.')),
        ('G-SEAL-VERIFIES', 'the seal recomputes by its own tool and all four gates are stamped',
         seal_recomputes()
         and all('GATE SUBJECT SHA256' in x for x in (RGATE, TERM, SPECRUN, AUDIT))),
        ('G-PRIOR-CLOSED', 'the face states the prior act closed, with its row',
         'PRIOR ACT (`b438`) IS' in FACET and 'row 287' in FF),

        # ---- THE RULINGS, THE SLOT, THE LANES ---------------------------------------------------
        ('G-NORULING-RATIFIED', 'this paste ratifies no new ruling and the face says so',
         'RATIFIES NO NEW RULING' in FACET),
        ('G-ADDENDUM-SLOT-DECLARED', '(R50)`s addendum slot is named in the write list',
         'b439_addendum.txt' in FACET and 'PRESENT WHETHER USED' in FACET.upper()),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'and its content is bounded to a verbatim quotation',
         'AND NOTHING ELSE' in FACET and 'never a measurement' in FACET),
        ('G-LANES-PARKED', 'both instrument lanes are parked',
         'both instrument lanes' in FACET and 'PARKED' in FACET),
        ('G-TRIGGER-RESTATED-NOT-ACTED', 'the fired disproof-lane trigger is restated, not acted on',
         'FIRED AT `(R48)`' in FACET and 'NOT ACTED ON' in FACET),

        # ---- COMPONENT 1 -------------------------------------------------------------------------
        ('G-SCALED-VARIABLE-QUOTED', 'the scaled variable is quoted at the atlas`s own line',
         'carto_atlas.py:' in COMP and 't = v / L' in COMP),
        ('G-THREE-WIDTHS-QUOTED', 'the three exponents are quoted at their own line',
         'MZ_EXPONENTS' in COMP and 'b317_smear.py:' in COMP),
        ('G-BOTH-MOMENTS-QUOTED', 'both moment conditions are quoted',
         'np.trapezoid(p, V)' in COMP and 'cosh' in COMP),
        ('G-WHAT-SCALES-NAMED', 'what is scale-invariant and what is not are each named',
         'SCALE-INVARIANT' in COMP and 'NOT SCALE-INVARIANT' in COMP),
        ('G-COEFFS-PRINTED-AT-RADII', 'the coefficients are printed at six radii',
         len(PROF) == 6 and all('c1' in r for r in PROF)),
        ('G-PROFILE-ZERO-LOCATED-AT-RADII', 'and every zero of the profile is printed at each',
         len(PROF) == 6 and all(r.get('zeros') for r in PROF)),
        ('G-DERIVATION-AND-MEASUREMENT-BOTH', 'both a derivation and a measurement are given',
         'A DERIVATION IS NOT A MEASUREMENT' in FACET
         and 'And a derivation is not a measurement' in COMP),
        ('G-C1-VERDICT-PRINTED', 'Component 1 returns one of the three verdicts',
         bool(re.search(r'VERDICT : (FIXED|NOT FIXED|PARTLY)', COMP))),
        ('G-SPREAD-ATTRIBUTED', 'b438`s spread is attributed to the grid or to the object, and the '
         'comparison is against the zero the crossings actually sit on',
         'THE ZERO THEY ACTUALLY SIT ON' in COMP
         and ('SPREAD IS THE OBJECT`S' in COMP or "SPREAD IS THE GRID`S" in COMP)),

        # ---- COMPONENT 2 -------------------------------------------------------------------------
        ('G-WEIGHT-TABLE-PRINTED', 'the weight is printed at every prime power the instrument admits',
         len(WTS) == 10 and '2 log p / sqrt(n)' in COMP),
        ('G-MAXIMIZER-NAMED', 'the maximizer is named',
         bool(re.search(r'THE MAXIMIZER IS `n = \d+`', COMP))),
        ('G-NAVIGATOR-ARITHMETIC-CHECKED', 'the navigator`s arithmetic is checked, not adopted',
         'IS CHECKED AND IT AGREES' in COMP),
        ('G-B438-SENTENCE-QUOTED', 'b438`s sentence is quoted before it is corrected',
         'b438_closing.txt : |' in COMP and 'largest of any prime power' in COMP),
        ('G-B438-CORRECTED-NOT-EDITED', 'and b438`s bank is not edited',
         0 == len([f for f in changed_tracked(ROOT) if re.match(r'data/b438_', f)])
         # ### **THE SENTENCE WRAPS**, so it is matched against the FOLDED record -- the same
         # ### family of needle defect this session has now met four times.
         # ### **AND THE NEEDLE IS FOLDED TOO, NOT RETYPED.** ### `fold()` strips backticks, so
         # ### a needle carrying `b438``S` can never match the text it was copied from. ### This
         # ### is the FIFTH time this session that a retyped needle failed on a true fact.
         # ### **THE RULE IS: FOLD BOTH SIDES, NEVER TYPE ONE.**
         and fold('b438`S BANK IS NOT EDITED') in fold(COMP)),
        ('G-EXPLANATION-VERDICT', 'the explanation gets one of the three verdicts',
         'NEEDS REPLACING' in COMP or 'STANDS' in COMP or 'NEVER LOAD-BEARING' in COMP),
        ('G-POSITION-SCORED-FROM-VALUES', 'the replacement is scored from printed values, with its '
         'exceptions structured rather than counted away',
         bool(re.search(r'SMALLEST `s` CARRIES THE LARGEST `\|term\|` : \d+ OF \d+', COMP))
         and 'THE EXCEPTIONS, AND WHAT THEY HAVE IN COMMON' in COMP),
        ('G-AMPLITUDE-ARGUMENT-SHOWN', 'that the amplitude peaks at the centre is shown, not asserted',
         'Cauchy-Schwarz' in COMP and 'max |f(v)|' in COMP),

        # ---- COMPONENT 3 -------------------------------------------------------------------------
        ('G-U0-SEARCH-PRINTED', 'the search for u0 is printed',
         'THE SEARCH, HAND-READ AT ITS OWN LINE' in COMP),
        ('G-U0-HITS-HANDREAD', 'and every hit on the value is opened at its own line',
         COMP.count('6.2898') >= 3 and 'THE HAND-READ' in COMP),
        ('G-U0-NAMED-OR-NOT', 'the naming question is answered, with provenance counted',
         ('NOT NAMED' in COMP or 'NAMED IN' in COMP)
         and 'ANY OTHER ACT' in COMP),
        ('G-U0-BALANCE-STATED', 'whether u0 is where the two constituents balance is stated',
         'TWO CONSTITUENTS BALANCE' in COMP and 'log pi' in COMP),
        ('G-U0-CLOSED-FORM-ANSWERED', 'and whether the record gives a closed form',
         'NO CLOSED FORM' in COMP.upper()),
        ('G-U0-TWO-ROUTES', 'u0 is located by two routes that share no code',
         'ROUTE A' in COMP and 'ROUTE B' in COMP and bool(U0.get('routeA'))
         and bool(U0.get('routeB'))),
        ('G-U0-TOLERANCE-STATED', 'with a tolerance stated before the comparison',
         'STATED BEFORE THE COMPARISON' in COMP and U0.get('tol') is not None),
        ('G-WHAT-OR-WHERE-SAID', 'and whether the corpus can say what it is or only where',
         'CAN SAY WHERE IT IS' in COMP and 'CANNOT SAY WHAT IT IS' in COMP),

        # ---- COMPONENT 4 -------------------------------------------------------------------------
        ('G-C4-PREMISE-CHECKED', 'the order`s conditional premise is checked before it is answered',
         "THE ORDER`S CONDITIONAL OPENS" in COMP),
        ('G-C4-PRICE-REPORTED', 'a price is reported from the three the order names',
         PRICE.get('c4', {}).get('price') in ('READ', 'MEASUREMENT', 'BUILD')),
        ('G-C4-LANES-ANSWERED', 'and whether either lane blocks it',
         'DOES NOT BLOCK' in COMP and 'BLOCKS THE' in COMP),
        ('G-C4-NOT-OPENED', 'and it is priced, not opened',
         'PRICED. ### NOT OPENED' in COMP or 'PRICED. ' in COMP and 'NOT OPENED' in COMP),
        ('G-THREE-FACTS-NAMED', 'the three finite facts are named',
         all(x in COMP for x in ('**(1) THE ENTERING TERM', '**(2) THE SHELLS',
                                 '**(3) THE WEIGHT TABLE'))),
        ('G-FACT-TWO-QUALIFIED', 'and the second is qualified by Component 1`s answer',
         'QUALIFIED AND MUST NOT BE CARRIED AS b438 LEFT IT' in COMP),
        ('G-NOTHING-BUILT-FOR-THE-KERNEL', 'and nothing is built for the kernel',
         'NOTHING IS BUILT' in COMP and 'NO TERMINAL, NO FILE' in COMP),

        # ---- THE EXPECTATIONS --------------------------------------------------------------------
        ('G-N1-APART', '(N1)`s two clauses are printed apart',
         '(a) the profile is FIXED in s' in COMP and '(b) b438`s 2.27e-04 spread' in COMP),
        ('G-N2-APART', '(N2)`s two clauses are printed apart',
         '(a) the weight explanation needs replacing' in COMP
         and '(b) position is the reason' in COMP),
        ('G-N3-APART', '(N3)`s two clauses are printed apart',
         '(a) the record names u0 nowhere' in COMP
         and '(b) the corpus can say only WHERE' in COMP),
        ('G-N4-APART', '(N4)`s two clauses are printed apart',
         '(a) it prices as a READ' in COMP and '(b) blocked by neither lane' in COMP),

        # ---- THE NOTHINGS ------------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel build log was written',
         not os.path.exists(os.path.join(D, 'b439_build.log'))),
        ('G-NOLEANEDIT', 'no .lean file moved',
         0 == len([f for r in (KERN, EFF, WINREPO) for f in changed_tracked(r)
                   if f.endswith('.lean')])),
        ('G-NOFETCH', 'nothing was fetched',
         not os.path.exists(os.path.join(D, 'b439_locate.txt'))),
        ('G-NOGRADE-MOVED', 'no grade is conferred, moved or minted',
         not re.search(r'\b(?:CONFER|MINT)(?:RED|ED|S)?\s+(?:THE\s+)?GRADE', COMP, re.I)),
        ('G-NOTERMINAL-RENAMED', 'no terminal is renamed',
         not re.search(r'\brenam(?:e|ed|ing)\b\s+(?:the\s+)?terminal', fold(COMP), re.I)),
        ('G-NONEWINSTRUMENT', 'no instrument file moved',
         0 == len([f for f in changed_tracked(ROOT)
                   if os.path.basename(f) in ('b317_smear.py', 'b318_square.py', 'b320_weil.py',
                                              'b321_window.py', 'b333_derive.py',
                                              'noise_floor.py', 'carto_atlas.py')])),
        ('G-NONEWFAMILY', 'no new family is defined',
         unchanged(ROOT, 'tools/b317_smear.py')),
        ('G-NOATLAS-EDIT', 'the atlas is byte-unmoved',
         unchanged(ROOT, 'tools/e16/carto_atlas.py')),
        ('G-NOLADDER-EDIT', 'SIDE-window is byte-unmoved',
         0 == len(changed_tracked(WINREPO)) and 0 == len(untracked_new(WINREPO))),
        ('G-NOLANE-OPENED', 'no lane is opened',
         'both instrument lanes' in FACET and 'NO LANE OPENED' in FF.upper()),
        ('G-NOPREMISE', 'no premise is discharged', 'NO PREMISE DISCHARGED' in FF),
        ('G-NODOOR', 'no door is restated', 'NO DOOR RESTATED' in FF),
        ('G-NOROUTE', 'no route is proposed', 'NO ROUTE PROPOSED' in FF),
        ('G-NOKAPPA', 'no kappa is measured', 'NO KAPPA MEASURED' in FF),
        ('G-NORULE-STRUCK', 'no rule is struck, amended or widened',
         'NO RULE STRUCK, AMENDED OR WIDENED' in FF),
        ('G-NODEPOSIT', 'no deposit action', 'NO DEPOSIT ACTION' in FF),
        ('G-NOH2-MOVED', 'h2 is read and not moved', 'h2 WHERE THE DEPOSIT LEFT IT' in FF),
        ('G-NOLOCKEDFACE', 'no prior locked face moved',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.search(r'b4[0-3]\d_registration', f)])),
        ('G-NOPRIORBANK', 'no prior act`s bank moved, the three ritual-rewritten files excepted',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.match(r'data/b(?!439)\d{3}_', f)
                   and os.path.basename(f) not in ('b369_hooks.txt', 'b369_hygiene.json',
                                                   'b373_pins.json')])),
        ('G-NOBANKEDFERRY', 'no banked ferry moved',
         0 == len([f for f in changed_tracked(ROOT) if f.endswith('_ferry.txt')])),
        ('G-NOFOLD', 'no fold was run',
         not os.path.exists(os.path.join(D, 'b439_fold.json'))),
        ('G-NOKEYSTONE-EDIT', 'no keystone document moved',
         0 == len([f for f in changed_tracked(PP) if 'KEYSTONE' in f.upper()])),
        ('G-NOCELL-WRITTEN', 'FACES_LEDGER.md is byte-unmoved',
         unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOSEVENTH-SITE', 'the register stays frozen at six',
         'FROZEN AT SIX' in FF.upper() and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-ARC-CHECKPOINTED-AFTER-IV', 'the arc stays checkpointed after site (iv)',
         'checkpointed after site `(iv)`' in FACET),
        ('G-FOUR-LISTS-OPEN', 'no list of the four is closed',
         'NO LIST OF THE FOUR CLOSED' in FF),
        ('G-DISPROOF-LANE-NOT-OPENED', 'the disproof lane is not opened',
         'THE DISPROOF LANE IS NOT OPENED' in FF),
        ('G-CORPUS-SCOPE', 'only the two append-only corpus documents moved',
         set(changed_tracked(PP)) <= {'OPEN_TRAILS.md'}
         and set(changed_tracked(KERN)) <= {'CORRESPONDENCE.md'}),
        ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS.md is appended to and not rewritten',
         ('OPEN_TRAILS.md' not in ' '.join(changed_tracked(PP)))
         or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'CORRESPONDENCE.md is appended to and not rewritten',
         ('CORRESPONDENCE.md' not in ' '.join(changed_tracked(KERN)))
         or appended_only(KERN, 'CORRESPONDENCE.md')),

        # ---- THE WRITE LIST ----------------------------------------------------------------------
        ('G-WRITELIST-KINDS', 'this act wrote nothing its locked face does not name',
         0 == len(unlisted_writes())),
        ('G-WRITELIST-NAMES-PATHS', 'the write list names paths, a generator with a bound, and '
         'the addendum slot',
         'PATHS, A GENERATOR WITH A BOUND' in fold(FACET) and 'BOUND `2`' in FACET
         and 'b439_addendum.txt' in FACET),
        ('G-WRITELIST-COUNTS-NEW', 'the write ledger sees NEW files',
         'untracked_new' in SRC_CHK and "startswith('??')" in SRC_CHK),
        ('G-NOSTAGE-A', 'no `git add -A` in this act`s own tools',
         not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_EXTP))),
        ('G-NOBORROWEDBAR', 'every bar on this face is this act`s own',
         12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),

        # ---- THE ARM DISCIPLINE ------------------------------------------------------------------
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', True),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank',
         'b439_components.txt' in SRC_CHK),
        ('G-ARMS-STRIP-PROSE', 'the source-reading arms strip comments and strings by tokenizer',
         'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK),
        ('G-ARMS-FOLD-MARKERS', 'the prose-reading arms fold markup before matching',
         'def fold(' in SRC_CHK),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line',
         'def verdict_line(' in SRC_CHK),
        ('G-ARMS-EOL-NORMALISED', 'banked tables are matched with line endings normalised',
         'def nl(' in SRC_COMP and 'chr(13)' in SRC_EXTP),
        ('G-TWO-READINGS-TWO-FILES', 'the suite writes its two readings to two files',
         'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK and '_pushed()' in SRC_CHK),
        ('G-NOWRAP-MIDTOKEN', 'the components record wraps at word boundaries',
         0 == len([1 for ln in COMP.splitlines()
                   if ln.endswith('-') and len(ln) > 96 and set(ln.strip()) != {'-'}])),
        ('G-NOSTRAY-PLACEHOLDER', 'no format string is printed without its arguments',
         0 == len(re.findall(r'%[-0-9.]*[dsfe](?![a-zA-Z])', COMP))),
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
