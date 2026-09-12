# -*- coding: utf-8 -*-
"""b436_checks.py -- THE CONTROL SUITE FOR b436. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b436_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b436_checks.txt')
POSTPUSH = os.path.join(D, 'b436_checks_postpush.txt')
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
            if re.search(r'b436', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b436_components.txt'))
EXTR = read(os.path.join(D, 'b436_extract.txt'))
LED = read(os.path.join(PP, 'FACES_LEDGER.md'))
B401R = read(os.path.join(D, 'b401_components_run.txt'))
RGATE = read(os.path.join(D, 'b436_reg_gate.txt'))
TERM = read(os.path.join(D, 'b436_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b436_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b436_reg_satisfiable.txt'))
# ### **THE LOCK GATE WRITES `_notes`, AND AN ARM POINTED AT A FILE THAT DOES NOT EXIST
# ### READS THE EMPTY STRING AND FAILS FOR A REASON THAT IS NOT THE ACT'S.** ### Named
# ### rather than quietly re-pointed, because the same shape -- a needle aimed at an
# ### absent file -- is how an arm comes to prove nothing while looking strict.
LOCKG = read(os.path.join(D, 'b436_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b436_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b436_ferry.txt'))
CENS = read(os.path.join(D, 'b436_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b436_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b436_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b436_components.py'))
SRC_EXT = read(os.path.join(T, 'b436_extract.py'))
SRC_CHK = read(os.path.join(T, 'b436_checks.py'))
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b436. ### The first thing THIS act did is
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
                for f in ('b436_ferry.txt', 'b436_ferry_scan.txt')
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
    ### writing let any basename starting `b436_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b436_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b436_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b436_', base)) and 'b436_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b436_.*\.py$', f)))


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
        if 'b436' not in subj:
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
    rec('b436_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
                     read(os.path.join(D, 'b436_regspec_run.txt')))
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
        rec('      ### reading governs: %s unlisted write(s), banked at b436_checks.txt.'
            % _pre.group(1))
    rec()

    def corpus(rel):
        return read(os.path.join(PP, rel))

    TRAILS = corpus('OPEN_TRAILS.md')
    CORR = read(os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md'))
    CF = fold(COMP)
    FF = fold(FACET)



    try:
        CAND = json.loads(read(os.path.join(D, 'b436_candidates.json')) or '{}')
    except Exception:
        CAND = {}
    try:
        SIDES = json.loads(read(os.path.join(D, 'b436_two_sides.json')) or '[]')
    except Exception:
        SIDES = []
    SRC_EXTP = read(os.path.join(T, 'b436_extract.py'))

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
        ('G-GUARD-DEFERRED-SAID', 'the face says the guard is not run at step zero and why',
         'NOT run at step zero' in FF or 'NOT RUN AT STEP ZERO' in FF),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXTR, 'MISSES          : 0') or verdict_line(EXTR, 'MISSES : 0')),
        ('G-REG-LOCKED-FIRST', 'the lock-gate record carries the digest the face`s lock block does',
         bool(seal_digest()) and seal_digest()[:16] in LOCKG),
        ('G-LOCKGATE-EIGHT', 'the lock gate read eight gates, all passing, four by digest',
         verdict_line(LOCKG, 'GATES READ : 8. PASSING : 8. FACE-SUBJECT GATES CHECKED BY '
                             'DIGEST : 4.')),
        ('G-SEAL-VERIFIES', 'the seal recomputes by its own tool and all four gates are stamped '
         'with that digest',
         seal_recomputes()
         and all('GATE SUBJECT SHA256' in x for x in (RGATE, TERM, SPECRUN, AUDIT))
         and all(seal_digest()[:32] in x for x in (RGATE, TERM, SPECRUN, AUDIT))),
        ('G-PRIOR-CLOSED', 'the face states the prior act closed, with its row',
         'PRIOR ACT (`b435`) IS' in FACET and 'row 284' in FF),
        ('G-R47-QUOTED', 'the ruling is in the banked paste and the act obeys its words',
         '(R44) FORBIDS A CLASS' in fold(FERRY)),
        ('G-R47-OBEYED-IN-W', 'the write list names paths and declares its one generator with a '
         'count bound, as (R47) requires',
         'PATHS, NAMED' in FACET and 'NO CLASS' in FACET
         and 'GENERATOR WITH A COUNT BOUND' in FF and 'THE BOUND IS `2`' in FACET),
        ('G-B435-NOT-REVERDICTED', 'b435`s two failing arms are not re-scored here',
         # ### **fold() STRIPS BACKTICKS**, so a needle carrying one can never match the text
         # ### it was copied from. ### Two arms here were written with the face's own backticks
         # ### in them and failed on a true fact -- the same shape as an arm aimed at an absent
         # ### file: ### **IT FAILS FOR A REASON THAT IS NOT THE ACT'S.**
         "b435'S TWO FAILING ARMS ARE NOT RE-VERDICTED" in FF),

        # ---- COMPONENT 1 -----------------------------------------------------------------------
        ('G-CELL-VERBATIM', 'the site`s own cell is quoted verbatim from the ledger',
         '(iv) - KIND: NOT EMPTY. WITNESS: UNSTATED.' in COMP
         and 'a uniform bound is not an object in the family' in CF),
        ('G-B405-REASON-QUOTED', 'b405`s reason for UNSTATED is given',
         'b405`S REASON' in COMP and 'parameter space' in CF),
        ('G-B406-CLAUSE-QUOTED', 'b406`s added clause is quoted at its own line',
         'b406_the_sites_without_an_existential.txt:' in COMP and 'TEN VALUES' in COMP),
        ('G-B401-ABSENCE-QUOTED', 'b401`s located candidate is quoted at its own line',
         'b401_components_run.txt:' in COMP and 'LAGARIAS THEOREM 6.1' in COMP),
        ('G-THREE-GROUNDS-AT-LINES', 'all three grounds are quoted, each at its own line',
         all(g in COMP for g in ('(i) WRONG FAMILY', '(ii) WRONG COMPARISON QUANTITY',
                                 '(iii) ITS HYPOTHESIS IS NOT OF A KIND'))),
        ('G-SEARCH-NOT-REPEATED', 'the act says it builds on b401`s absence rather than re-running '
         'its search',
         'DOES NOT REPEAT ITS SEARCH' in COMP),
        ('G-UNIFORM-BOUND-DECLARED-FIRST', 'the object enumerated is declared a uniform bound '
         'before the first candidate, on the face and in the components record',
         'THE OBJECT THIS ACT ENUMERATES IS A UNIFORM BOUND' in FF
         and COMP.index('UNIFORM BOUND') < COMP.index('W1 ')),

        # ---- COMPONENT 2 -----------------------------------------------------------------------
        ('G-OPENING-POPULATION-SEVEN', 'the opening population is the order`s seven',
         len(CAND.get('candidates', [])) == 7),
        ('G-EACH-READ-AT-SOURCE', 'every candidate carries a quotation at a named file and line',
         7 == len(re.findall(r'the step, at its own file and line:', COMP))),
        ('G-EXTENSION-BY-DESCRIPTION', 'the extension ran by a description fixed before it ran',
         'THE DESCRIPTION, FIXED BEFORE THE SEARCH RAN' in COMP),
        ('G-EXTENSION-CAP-STATED', 'the extension`s cap is stated, and the overflow is counted '
         'rather than quietly truncated',
         bool(re.search(r'THE CAP : \d+ FURTHER HITS', COMP))
         and bool(re.search(r'\d+ FURTHER HITS WERE NOT PRINTED, THE CAP BEING \d+', COMP))),
        ('G-FURTHER-HITS-REASONED', 'every printed extension hit carries the reason it was not '
         'admitted',
         COMP.count('NOT ADMITTED') >= 1
         and 'ADMITTED FROM THE EXTENSION : 0' in COMP),
        ('G-EVERY-CANDIDATE-QUOTED-STEP', 'every candidate is FAILED AT A QUOTED STEP or HELD',
         7 == len([c for c in CAND.get('candidates', [])
                   if c.get('verdict') in ('FAILED AT A QUOTED STEP', 'HELD')])),
        ('G-HELD-COUNT-PRINTED', 'the held count is printed, whatever it is',
         bool(re.search(r'OPENING POPULATION : \d+\. ### HELD : \d+', COMP))),
        ('G-NO-CANDIDATE-ADOPTED-ON-WORD', 'the navigator`s candidate is tested, not adopted',
         'tested and not adopted on his word' in COMP),

        # ---- THE NAVIGATOR`S CANDIDATE ---------------------------------------------------------
        ('G-NAVCAND-PARAPHRASE-CHECKED', 'his paraphrase is checked against (149), not taken',
         'CHECKED AGAINST THE SOURCE RATHER THAN TAKEN' in COMP
         and 'HIS PARAPHRASE IS ACCURATE' in COMP),
        ('G-NAVCAND-PART-A-SCORED', 'part (a) returns a verdict with the search printed',
         'PART (a) VERDICT' in COMP and 'THE SEARCH, AND THE ONE DISTINCTION' in COMP),
        ('G-NAVCAND-SOURCE-CLASS-DRAWN', 'the verified-source / working-log distinction is drawn '
         'explicitly and from the corpus`s own words',
         'REGISTRY-SILENT' in COMP and 'working logs' in COMP),
        ('G-NAVCAND-PART-B-GATED', 'part (b) is run because part (a) located the bound',
         'LOCATED AS ELEMENTARY' in COMP and 'PART (b)' in COMP),
        ('G-COMPARISON-IN-EMITTING-NORMALIZATION', 'the comparison quotes the emitting act`s '
         'normalizations rather than the navigator`s paraphrase',
         'half-line normalization' in COMP and 'np.trapezoid' in COMP
         and 'THE NORMALIZATIONS, QUOTED FROM THE EMITTING ACT' in COMP),
        ('G-BANKED-FIGURES-ONLY', 'the act says the bound`s own growth is not a banked figure and '
         'does not compute one',
         'THE BOUND`S OWN GROWTH IS NOT A BANKED FIGURE' in COMP),
        ('G-RADII-AS-PRINTED', 'the radii are exactly b321`s ten and no other is spoken about',
         len(SIDES) == 10 and all(str(r['a']) in COMP for r in SIDES)),
        ('G-BOTH-SIDES-PRINTED', 'both sides are printed at every radius, with their ratio',
         10 == len(re.findall(r'^\s+[0-9.]+\s+-?[0-9.]+\s+-?[0-9.]+\s+[0-9.]+e[-+]\d+\s*$',
                              COMP, re.M))),
        ('G-WRONG-WAY-AT-PROMINENCE', 'the wrong-way result is stated as a FINDING, not softened',
         'THE BOUND RUNS THE WRONG WAY' in COMP and 'AT FULL PROMINENCE' in COMP),
        ('G-CROSSING-UNDECIDED-SAID', 'the act says the crossing is undecided and why',
         'THE CROSSING IS STILL UNDECIDED' in COMP and 'WINDOW ENDS' in COMP
         and 'A TREND IS NOT A CROSSING' in COMP),
        ('G-WHAT-WOULD-DECIDE-NAMED', 'what would decide it is named, with its price',
         'WHAT WOULD DECIDE IT' in COMP and 'THE INSTRUMENT LANE IS PARKED' in COMP),

        # ---- COMPONENT 3, THE BOUNDARY COUNT ---------------------------------------------------
        ('G-FOUR-SITES-COUNTED', 'four sites are counted, not three',
         4 == len(re.findall(r'^      b4\d\d\s+\(i+v?\)', COMP, re.M))),
        ('G-KINDS-FROM-JSON', 'the earlier sites` kinds come off their own JSON, not this seat',
         'KINDS READ FROM JSON, NEVER TYPED' in COMP
         and os.path.exists(os.path.join(D, 'b436_prior_sites.json'))),
        ('G-UNION-PRINTED', 'the union of kinds is printed for the three and for the four',
         'UNION OF KINDS ACROSS THE THREE EARLIER SITES' in COMP
         and 'UNION ACROSS ALL FOUR' in COMP),
        ('G-SHARED-BOUNDARIES-COUNTED', 'how many of this site`s failures land at an earlier '
         'site`s boundary is counted, and any new kind is named',
         bool(re.search(r'LANDING AT A BOUNDARY AN EARLIER SITE USED : \d+ of \d+', COMP))
         and ('NEW AT THIS SITE' in COMP or not CAND.get('new'))),

        # ---- THE EXPECTATIONS ------------------------------------------------------------------
        ('G-N1-SCORED', '(N1) is scored over the list this act enumerates, by a printed count',
         bool(re.search(r'candidates \d+, held \d+', COMP))),
        ('G-N2-APART', '(N2)`s two clauses are printed and scored apart',
         '(N2), ITS TWO CLAUSES APART' in COMP and '(a) his candidate is LOCATED' in COMP
         and '(b) it fails as a witness ON THE COMPARISON' in COMP),
        ('G-N3-APART', '(N3)`s verdict and its reason are printed and scored apart',
         '(N3), ITS VERDICT AND ITS REASON APART' in COMP
         and '(a) the crossing reads NOT COMPARABLE' in COMP
         and '(b) the reason' in COMP),
        ('G-N3-REASON-DECIDED-BY-RECORD', '(N3)(b) is decided by asking whether a banked act puts '
         'both quantities in one verified relation, and the answer is printed',
         'does any banked act' in CF.lower()
         and 'Z = P - PR + A' in COMP and 'ALL THIRTEEN CELLS' in COMP),

        # ---- THE CELL AND THE ARC --------------------------------------------------------------
        ('G-CELL-ONLY-IF-HELD', 'the cell is written only if a candidate held',
         ('NO CANDIDATE HELD' in COMP) == (CAND.get('held') == 0)),
        ('G-LEDGER-WRITER-ONLY', 'FACES_LEDGER.md is unmoved, no candidate having held',
         (CAND.get('held') == 0) and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-EXHAUSTED-LIST-AS-BLOCK', 'the exhausted list is filed as a block',
         'exhausted list is filed as a block' in CF),
        ('G-ARC-CHECKPOINTED-AFTER-IV', 'the arc is checkpointed after site (iv)',
         'CHECKPOINTED AFTER SITE (iv)' in FF),
        ('G-FOUR-LISTS-OPEN', 'the face declares no list of the four closed',
         'NO LIST OF THE FOUR CLOSED' in FF),

        # ---- THE NOTHINGS ----------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel build log was written by this act',
         not os.path.exists(os.path.join(D, 'b436_build.log'))),
        ('G-NOLEANEDIT', 'no .lean file moved in either kernel',
         0 == len([f for r in (KERN, EFF) for f in changed_tracked(r) if f.endswith('.lean')])),
        ('G-NOFETCH', 'nothing was fetched and no address resolved',
         not os.path.exists(os.path.join(D, 'b436_locate.txt'))),
        ('G-NOGRADE-MOVED', 'no grade is conferred, moved or minted',
         not re.search(r'\b(?:CONFER|MINT)(?:RED|ED|S)?\s+(?:THE\s+)?GRADE', COMP, re.I)),
        ('G-NOTERMINAL-RENAMED', 'no terminal is renamed',
         not re.search(r'\brenam(?:e|ed|ing)\b\s+(?:the\s+)?terminal', CF, re.I)),
        ('G-NOINSTRUMENT-WRITTEN', 'no instrument was written or edited; only this act`s own '
         'tools are new and banked_index is the one edit',
         set(f for f in changed_tracked(ROOT) if f.startswith('tools/'))
         <= {'tools/banked_index.py'}),
        ('G-BOTH-LANES-PARKED', 'the face declares both instrument lanes parked',
         'both instrument lanes PARKED' in FACET),
        ('G-DISPROOF-LANE-SHUT', 'the face says the disproof lane stays shut and untouched',
         'DISPROOF LANE STAYS SHUT AND ITS TRIGGER IS NOT TOUCHED' in FF),
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
        # ### **THREE FILES ARE REWRITTEN BY THE RITUAL'S OWN TOOLS WHENEVER THEY RUN**, and the
        # ### locked face names all three in section (W). ### An arm that charges them as a prior
        # ### act's bank is measuring the ritual, not the act.
        ('G-NOPRIORBANK', 'no prior act`s bank file moved, the three the face names as rewritten '
         'by the ritual`s own tools excepted',
         0 == len([f for f in changed_tracked(ROOT)
                   if re.match(r'data/b(?!436)\d{3}_', f)
                   and os.path.basename(f) not in ('b369_hooks.txt', 'b369_hygiene.json',
                                                   'b373_pins.json')])),
        ('G-NOBANKEDFERRY', 'no banked ferry moved',
         0 == len([f for f in changed_tracked(ROOT) if f.endswith('_ferry.txt')])),
        ('G-NOFOLD', 'no fold was run by this act',
         not os.path.exists(os.path.join(D, 'b436_fold.json'))),
        ('G-NOKEYSTONE-EDIT', 'no keystone document moved',
         0 == len([f for f in changed_tracked(PP) if 'KEYSTONE' in f.upper()])),
        ('G-NOBRIDGE-TYPED', 'the act states that no bridge is typed between any two of the six',
         'NO BRIDGE IS TYPED BETWEEN ANY TWO OF THE SIX' in CF.upper()),
        ('G-ROW-LAW-RESTATED-NOT-EDITED', 'the row`s law is quoted where cited and FACES_LEDGER is '
         'byte-unmoved',
         unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOSEVENTH-SITE', 'no seventh site is entered and the register stays frozen at six',
         'FROZEN AT SIX' in CF.upper() and unchanged(PP, 'FACES_LEDGER.md')),
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
        ('G-WRITELIST-NAMES-PATHS', 'the write list names paths, not a class -- (R47) obeyed, and '
         'b435`s breach not repeated',
         0 == len(unlisted_writes()) and 'PATHS, NAMED' in FACET),
        ('G-WRITELIST-COUNTS-NEW', 'the write ledger sees NEW files, not only modified ones',
         'untracked_new' in SRC_CHK and "startswith('??')" in SRC_CHK),
        ('G-NOSTAGE-A', 'no `git add -A` appears in this act`s own tools',
         not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_EXTP))),
        ('G-NOBORROWEDBAR', 'every bar on this face is this act`s own',
         12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),

        # ---- THE ARM DISCIPLINE ----------------------------------------------------------------
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', True),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank',
         'b436_components.txt' in SRC_CHK),
        ('G-ARMS-STRIP-PROSE', 'the source-reading arms strip comments and strings by tokenizer',
         'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK),
        ('G-ARMS-FOLD-MARKERS', 'the prose-reading arms fold markup before matching',
         'def fold(' in SRC_CHK),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line, never as a substring',
         'def verdict_line(' in SRC_CHK),
        ('G-ARMS-EOL-NORMALISED', 'the banked tables are matched with line endings normalised, '
         'the defect this act`s own survey hit on its first run',
         'LINE ENDINGS NORMALISED BEFORE ANY BANKED TABLE' in SRC_COMP
         and 'chr(13)' in SRC_EXTP),
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
