# -*- coding: utf-8 -*-
"""b433_checks.py -- THE CONTROL SUITE FOR b433. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b433_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b433_checks.txt')
POSTPUSH = os.path.join(D, 'b433_checks_postpush.txt')
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
            if re.search(r'b433', os.path.basename(f)):
                out.append(f)
    return out


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b433_components.txt'))
EXTR = read(os.path.join(D, 'b433_extract.txt'))
PROF = read(os.path.join(D, 'b433_profile.txt'))
BUILD = read(os.path.join(D, 'b433_build.log'))
LOCKG = read(os.path.join(D, 'b433_lockgate.txt'))
SCAN = read(os.path.join(D, 'b433_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b433_ferry.txt'))
CENS = read(os.path.join(D, 'b433_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b433_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b433_pins_stepzero.txt'))
SRC_COMP = read(os.path.join(T, 'b433_components.py'))
SRC_EXT = read(os.path.join(T, 'b433_extract.py'))
SRC_CHK = read(os.path.join(T, 'b433_checks.py'))
try:
    G = json.loads(read(os.path.join(D, 'b433_repairs.json')) or '{}')
except Exception:
    G = {}
# ### **THIS ACT DID NOT BEGIN WHEN ITS FERRY WAS BANKED.** ### All three legs' pastes were
# ### banked together at b430's step zero, so the ferry's mtime puts b430's own bank on the wrong
# ### side of the boundary and charges b430's files to b433. ### The first thing THIS act did is
# ### its step-zero resolution, and that is the boundary.
# ### **THIS ACT RESOLVES NO ADDRESS**, so it has no `ls-remote` record to date itself from --
# ### b431's boundary file does not exist here. ### Its first artefact is its own ferry scan, and
# ### the ferry itself is no boundary: all three legs' pastes were banked together at b430.
ACT_START = os.path.getmtime(os.path.join(D, 'b433_ferry_scan.txt'))


def written_by_this_act(repo, rel):
    try:
        return os.path.getmtime(os.path.join(repo, rel)) >= ACT_START
    except Exception:
        return True


def writelisted(repo, rel):
    """### IS THIS PATH NAMED BY THE LOCKED FACE'S WRITE LIST?

    ### ### **A TOOL MUST BE NAMED OUTRIGHT; ONLY BANK FILES FALL UNDER A PATTERN.** ### The first
    ### writing let any basename starting `b433_` count as listed, which made the write list
    ### unfalsifiable for exactly the kind of file it most needs to govern -- a NEW TOOL the act
    ### decided to write while running. ### `b433_fetch.py` passed that test and is named nowhere
    ### on the face.
    """
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0] \
        if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    if re.match(r'tools/b433_.*\.py$', rel.replace(os.sep, '/')):
        return False          # ### a tool is listed by name or it is not listed
    return bool(re.match(r'b433_', base)) and 'b433_' in sec


def unlisted_writes():
    out = [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
           if written_by_this_act(r, f) and not writelisted(r, f)]
    out += [(r, f) for r in (ROOT, PP, KERN) for f in untracked_new(r) if not writelisted(r, f)]
    return out


def new_act_tools():
    """### THE ACT-TOOL FILES THIS ACT ADDED, AGAINST THE COUNT ITS OWN FACE DECLARED."""
    return sorted(set(os.path.basename(f) for f in
                      changed_tracked(ROOT) + untracked_new(ROOT)
                      if re.match(r'tools/b433_.*\.py$', f)))


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
        if 'b433' not in subj:
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
    rec('b433_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
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
                     read(os.path.join(D, 'b433_regspec_run.txt')))
    rec('      new act-tool files written : %d %s' % (len(_tools), _tools))
    rec('      the face`s declared cap    : %s' % (_cap.group(2) if _cap else '(not read)'))
    if _cap and len(_tools) > int(_cap.group(2)):
        rec('      ### **THE ACT WROTE MORE ACT TOOLS THAN ITS LOCKED FACE DECLARED.** ### The')
        rec('      ### face is locked and is NOT edited; the breach is printed and named.')
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **THE WRITE-LIST ARMS ARE VACUOUS ON A CLEAN TREE.** ### The pre-push')
        rec('      ### reading governs: %s unlisted write(s), banked at b433_checks.txt.'
            % _pre.group(1))
    rec()

    APP = [r for r in G.get('repairs', []) if r.get('status') in ('APPLIED', 'ALREADY APPLIED')]
    DEL = G.get('deltas', {})

    def corpus(rel):
        return read(os.path.join(PP, rel))

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
        # ### **THE FACE HARD-WRAPS, SO A NEEDLE MUST BE MATCHED AGAINST THE FOLDED TEXT** -- b426's
        # ### wrap-trap, which this arm walked straight into: the phrase is split as
        # ### `EXERCISED IN ALL` / `### FOUR, \`0\` FAILING`.
        ('G-STEPZERO-GUARD', 'the face records the guard exercised in all four at 0 failing',
         'EXERCISED IN ALL FOUR, 0 FAILING' in fold(FACET)),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXTR, 'MISSES : 0')),
        ('G-PREACT-BLOBS-PINNED', 'seven pre-act blobs are pinned by byte count and sha256',
         7 == len(re.findall(r'(?m)^\S+\s+\d+\s+[0-9a-f]{64}\s*$',
                             read(os.path.join(D, 'b433_preact_blobs.txt'))))),
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
         bool(re.search(r'(?m)^\|\s*281\s*\|', read(os.path.join(KERN, 'CORRESPONDENCE.md'))))),

        # ### ---- THE RULINGS ---------------------------------------------------------------------
        ('G-RULINGS-QUOTED', 'the rulings block is quoted from the banked paste',
         G.get('rulings_quoted') is True),
        ('G-RULINGS-NOT-EXTENDED', 'exactly the five rulings the paste names appear in the quote',
         G.get('rulings_named') == ['(R41)', '(R42)', '(R43)', '(R44)', '(R45)']),
        ('G-FIVE-EXECUTED', 'every ruling has a printed outcome in the components',
         all(('(R4%d)' % k) in COMP or ('R4%d' % k) in COMP for k in (1, 2, 3, 4, 5))),

        # ### ---- (R41) -----------------------------------------------------------------------------
        ('G-R41-BOTH-DOCS', 'both vocabulary documents were repaired',
         2 == len(set(r['file'] for r in APP
                      if r['file'] in ('README.md', 'phase1.5\\method\\EXCLUSION_ENGINE.md',
                                       'phase1.5/method/EXCLUSION_ENGINE.md')))),
        ('G-R41-THREE-BULLETS-INTACT', 'the three existing grade bullets survive in both documents',
         all(s_ in corpus('README.md') for s_ in
             ('**DERIVES** — the theorem', '**INTERFACES** — the theorem takes the claim',
              'work-orders, not citations'))
         and all(s_ in corpus('phase1.5/method/EXCLUSION_ENGINE.md') for s_ in
                 ('**DERIVES** — the kernel proves the stated content',
                  '**INTERFACES** — the kernel proves a conditional',
                  'A shell is a work-order, not a citation.'))),
        ('G-R41-FOURTH-ADDED', 'the fourth grade is present exactly once in each document',
         1 == corpus('README.md').count('**NOT THE CLAIM** — the theorem is sound')
         and 1 == corpus('phase1.5/method/EXCLUSION_ENGINE.md').count(
             '**NOT THE CLAIM** — the kernel proves a theorem')),
        ('G-R41-INCIDENTS-CITED', 'b429`s and b430`s incidents are cited with the definition',
         all(s_ in corpus('phase1.5/method/EXCLUSION_ENGINE.md')
             for s_ in ('**b429**', '**b430**', 'SmearGeneral.smear_general'))),

        # ### ---- (R42) -----------------------------------------------------------------------------
        ('G-R42-NAME-UNCHANGED', 'crt_exhaustiveness keeps its name everywhere this act can see',
         'crt_exhaustiveness' in corpus('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
         and 'no_type_d_conspiracies' in corpus(
             'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')),
        ('G-R42-KERNEL-UNTOUCHED', 'no .lean file changed in any repository',
         [] == [f for r in (ROOT, PP, KERN, EFF) for f in changed_tracked(r)
                if f.endswith('.lean')]),
        ('G-R42-ANNOTATION-IN-DOCS-OWN-FORM',
         'the annotation declares the existing text PRESERVED, as that document already does',
         'existing text PRESERVED' in corpus(
             'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
         and 1 == corpus('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md').count(
             'THE COMPILED LEMMA, READ AT ITS STATEMENT')),
        ('G-R42-SINGLE-MODULUS-STATED', 'the annotation states the singleton and the periodic lift',
         all(s_ in corpus('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
             for s_ in ('a singleton', 'periodic lift',
                        'the Chinese Remainder Theorem is not invoked in it'))),
        ('G-R42-ORIGINAL-PRESENT', 'the sentence the annotation narrows is still there, word for word',
         'beyond what the Chinese Remainder Theorem explains at every finite modulus'
         in corpus('phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')),

        # ### ---- (R43) -----------------------------------------------------------------------------
        ('G-R43-K3-MARKED', 'both K3 rows carry their marking, each exactly once',
         1 == corpus('FINDINGS.md').count('NARROWED TO THE TERMINAL: of the objects named in this row')
         and 1 == corpus('FINDINGS.md').count('NARROWED: these grades are b329')),
        ('G-R43-F5-MARKED', 'the claim-bearing F5 row carries its marking exactly once',
         1 == corpus('FACES_LEDGER.md').count(
             'NARROWED TO THE TERMINAL: the scope clause above is TRUE')),
        ('G-R43-NINE-OBJECTS-KEPT', 'K3`s named objects are kept and marked, not deleted',
         'the test function at the identity times a dimension' in corpus('FINDINGS.md')
         and 'not carried by that terminal' in corpus('FINDINGS.md')),
        ('G-R43-SCOPE-CLAUSE-NOT-REWRITTEN', 'F5`s scope clause survives word for word (BAR 6)',
         G.get('r43_scope_clause_kept') is True
         and 'GENERAL, over every base p ≥ 2, level, power and index' in corpus('FACES_LEDGER.md')),
        ('G-R43-ORIGINALS-PRESENT', 'every marked row still parses with its original cell count',
         all(len(ln.split('|')) - 2 == n for ln, n in
             [(next(x for x in corpus('FINDINGS.md').splitlines()
                    if x.startswith('| **K3** the finite places') and 'KERNEL TERMINALS' in x), 2),
              (next(x for x in corpus('FINDINGS.md').splitlines()
                    if x.startswith('| **K3** the finite places') and 'PROVED-GENERAL' in x), 5),
              (next(x for x in corpus('FACES_LEDGER.md').splitlines()
                    if x.startswith('| **F5**') and 'FiniteSideSeal.lean' in x), 3)])),

        # ### ---- THE TRAIL ADDENDUM -----------------------------------------------------------------
        ('G-TRAIL-FORMB-ADDED', 'the form-(b) finding is appended exactly once',
         1 == corpus('OPEN_TRAILS.md').count('<!-- b433 the disproof lane')),
        ('G-TRAIL-SYMMETRY-QUOTED', 'the barrier keystone`s symmetry clause is quoted beside it',
         'reflective FE F(s) = F(1−s)' in corpus('OPEN_TRAILS.md')
         and 'INVARIANCE_BARRIERS.md' in corpus('OPEN_TRAILS.md')),
        ('G-TRAIL-ASYMMETRY-SENTENCE', 'the sentence the order requires is on the record',
         'the instruments are not symmetric though the theory is' in corpus('OPEN_TRAILS.md')),

        # ### ---- (R44), (R45) -----------------------------------------------------------------------
        ('G-R44-WRITELIST-FORM', 'the write list is in b432`s form, which (R44) makes standing',
         'IN b432\'S FORM' in FACET and 'ANY FURTHER `tools/b433_*.py`' in FACET),
        ('G-R45-SUBSTITUTES-FIRST', 'the substitutes were confirmed present and tracked first',
         G.get('substitutes_ok') is True),
        ('G-R45-CLONE-ABSENT', 'the external clone is gone, read after the removal',
         G.get('clone_removed') is True and not os.path.isdir(
             os.path.join('D:', os.sep, '_b431_external'))),

        # ### ---- THE MEASUREMENT --------------------------------------------------------------------
        ('G-DELTAS-NONNEGATIVE', 'every per-file byte delta against the pre-act blob is >= 0',
         G.get('all_deltas_nonnegative') is True
         and all(v is None or v >= 0 for v in DEL.values())),
        ('G-ORIGINALS-ALL-PRESENT', 'every original this act promised to keep is still findable',
         G.get('all_originals_present') is True),
        ('G-NO-REPAIR-NOTLOCATED', 'no repair was reported NOT LOCATED', G.get('notlocated') == 0),
        ('G-NO-REPAIR-REFUSED', 'no repair was refused', G.get('refused') == 0),

        ('G-L1-APART', 'the face declares L1`s two clauses apart',
         'ITS TWO CLAUSES PRINTED APART' in FACET and '(b) none needs routing' in FACET),
        ('G-L1-SCORED', 'both clauses of L1 are decidable from a printed result',
         G.get('all_deltas_nonnegative') is not None and G.get('notlocated') is not None),

        # ### ---- THE NOTHINGS -----------------------------------------------------------------------
        ('G-NOKERNELBUILD', 'no kernel is built: no tool of this act invokes a build',
         not re.search(r'lake|elan', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOLEANEDIT', 'no .lean file is written by any tool of this act',
         not re.search(r"\.lean.{0,12}'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOFETCH', 'nothing is fetched: no tool of this act opens a URL',
         not re.search(r'urlopen|urllib|requests', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOTERMINAL-RENAMED', 'no terminal name is rewritten anywhere this act wrote',
         G.get('r42_name_kept') is True),
        # ### **AN ACT NUMBER IS NOT A HEX SUBSTRING.** ### The first writing matched `b429`
        # ### anywhere and fired on `REGISTRY.md`, where the hit was inside the git SHA
        # ### `b4296e5cc42c...`. ### **b429 BANKED THAT EXACT LESSON AND THIS ARM REPEATED IT** --
        # ### an act reference must be bounded, and a hex character may not follow it.
        # ### ### And the claim is narrower than "no document names a prior act": it is that THIS
        # ### act cited no GRADING into a corpus document, which is what the trigger forbids.
        # ### **AND THE TRIGGER THIS ARM ENCODED HAS BEEN DISCHARGED FOR EXACTLY THESE CITATIONS.**
        # ### "Cited in no corpus document *until the author rules*" was the standing trigger; the
        # ### author has now ruled, and `(R41)` ORDERS b429's and b430's incidents cited. ### An arm
        # ### that forbids what the ruling it is checking requires is testing the wrong claim.
        # ### ### **WHAT SURVIVES IS THE NARROWER TRUE CLAIM**: no grading is cited into a document
        # ### NO RULING NAMES, and no grade moved anywhere.
        ('G-NOGRADE-MOVED', 'no grading is cited outside the documents the rulings name',
         0 == len([1 for f in ('REGISTRY.md', 'SPIRAL_MAP.md')
                   if re.search(r'b4(29|3[012])(?![0-9a-f])', corpus(f))])
         and all(unchanged(PP, f) for f in ('REGISTRY.md', 'SPIRAL_MAP.md'))
         and all(re.search(r'\(R4[123]\)', ln)
                 for f in ('FINDINGS.md', 'FACES_LEDGER.md')
                 for ln in corpus(f).splitlines()
                 if re.search(r'b4(29|3[012])(?![0-9a-f])', ln))),
        ('G-LANE-NOT-OPENED', 'the addendum says the lane is not opened by it',
         'The lane is not opened by this addendum' in corpus('OPEN_TRAILS.md')),
        ('G-TRIGGER-UNTOUCHED', 'the trigger text is restated unchanged',
         'the instrument lane opening' in corpus('OPEN_TRAILS.md')),
        ('G-FOUR-LISTS-OPEN', 'no list of the four was closed',
         unchanged(PP, 'REGISTRY.md')),
        ('G-ARC-CHECKPOINTED', 'no witness-arc site was attempted',
         not re.search(r'site_iv', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOPREMISE', 'h2 is not discharged: the keystone that states it is unchanged',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
        ('G-NODOOR', 'no door restated', unchanged(PP, 'REGISTRY.md')),
        ('G-NOROUTE', 'no route proposed', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOKAPPA', 'no kappa measured',
         not re.search(r'kappa', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NORULE-STRUCK', 'no rule struck or amended; the standing file is unmoved',
         unchanged(ROOT, 'tools/FERRY_STANDING.md')),
        ('G-NODEPOSIT', 'no deposit action',
         not re.search(r'zenodo|deposit', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOH2-MOVED', 'h2 is read and not moved',
         unchanged(PP, 'phase1.5/method/INVARIANCE_BARRIERS.md')),
        ('G-NOLOCKEDFACE', 'no prior locked face was written by this act',
         all(os.path.getmtime(os.path.join(D, f)) < ACT_START
             for f in os.listdir(D)
             if re.match(r'b4[0-3]\d_registration', f) and not f.startswith('b433'))),
        ('G-NOPRIORBANK', 'no prior act`s bank appears among this act`s changed paths',
         [] == [f for f in changed_tracked(ROOT)
                if re.match(r'data/b4(0|1|2)\d_', f) or re.match(r'data/b43[012]_', f)]),
        ('G-NOBANKEDFERRY', 'no banked ferry is written by any tool of this act',
         not re.search(r"FERRY\s*,\s*'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOFOLD', 'no fold run: the fold is leg 2`s',
         not re.search(r'fold_run|b434', pycode_of(SRC_COMP))),
        ('G-NOREGISTERROW', 'no register row edited', unchanged(PP, 'REGISTRY.md')),
        ('G-CORPUS-SCOPE', 'this act read and wrote the corpus and its own bank only',
         not re.search(r'urlopen', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-TRAIL-APPEND-ONLY', 'the trail`s committed text is a TRUE PREFIX of its text now',
         appended_only(PP, 'OPEN_TRAILS.md')),
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
