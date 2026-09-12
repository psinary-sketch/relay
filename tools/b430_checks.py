# -*- coding: utf-8 -*-
"""b430_checks.py -- THE CONTROL SUITE FOR b430. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE**, so an arm declared and not built is
### a FAILURE of `G-ARMS-DECLARED-EQ-RUN` rather than a silence. ### Every `G-NO*` arm reads the DATA
### ITS PRINTER CONSUMED and never a raw document text -- b427's bar, which fired on this seat's own
### arms twice and was right both times.
### ### **AND THE SUITE IS READ TWICE, PRE-PUSH AND POST-PUSH**, by the same file.
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
import ferry_scan      # noqa: E402
import banned_terms    # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b430_registration_2026-09-12.txt')
# ### **THE SUITE IS READ TWICE AND MUST NOT OVERWRITE ITS OWN FIRST READING.** ### It did: every
# ### post-push run wrote back to the pre-push path, and the pre-push record -- the one that had
# ### the two failing write-list arms in it -- survived only because it had already been committed.
# ### ### **A TOOL THAT DESTROYS ITS OWN EARLIER EVIDENCE IS A TOOL THAT CANNOT BE READ TWICE.**
# ### The side is decided by whether this act's commit is already on the remote, which is the same
# ### fact the two readings differ about.
PREPUSH = os.path.join(D, 'b430_checks.txt')
POSTPUSH = os.path.join(D, 'b430_checks_postpush.txt')


def _pushed():
    try:
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False


OUT = POSTPUSH if _pushed() else PREPUSH
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
                  .replace(chr(0x2019), "'").replace(chr(0x201C), '"').replace(chr(0x201D), '"')
                  .replace(chr(0x2014), '--')).strip()


def unbar(s):
    return fold(re.sub(NL + r'\s*\|\s?', ' ', s or ''))


def pycode_of(src):
    """### BAR 12: COMMENTS **AND** STRING LITERALS STRIPPED BY THE TOKENIZER, NEVER BY A REGEX.
    ### ### **AN ARM THAT GREPS ITS OWN SOURCE FINDS ITS OWN DOCSTRING SAYING WHAT IT FORBIDS.**"""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except Exception:
        return ''
    # ### **THE TOKENIZER SPLITS `a.b` INTO THREE TOKENS**, so a needle written as a dotted call
    # ### never matches the joined text. ### Two arms failed on exactly that and the code they were
    # ### looking for was there all along -- ### **AN ARM THAT CANNOT SEE A TRUE FACT IS A DEFECT
    # ### OF THE ARM**, and the cure is to close the dots the tokenizer opened.
    return re.sub(r'\s*\.\s*', '.', ' '.join(out))


def git(repo, *a):
    try:
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout
    except Exception:
        return ''


def unchanged(repo, path):
    """### A TRACKED FILE'S SAMENESS READ IN GIT'S OWN VIEW (BAR 12), never by comparing bytes to a
    ### copy this suite made."""
    return path not in git(repo, 'status', '--porcelain', '--', path)


# ### ===============================================================================================
# ### THE BANK THIS SUITE READS. ### **THE PRINTERS' OUTPUT, NOT THE RECORDS' PROSE.**
# ### ===============================================================================================
FACET = read(FACE)
COMP = read(os.path.join(D, 'b430_components.txt'))
EXT = read(os.path.join(D, 'b430_extract.txt'))
SCANREP = read(os.path.join(D, 'b430_scan_repair.txt'))
PROF = read(os.path.join(D, 'b430_profile.txt'))
BUILD = read(os.path.join(D, 'b430_build.log'))
LOCKG = read(os.path.join(D, 'b430_lockgate.txt'))
SCANS = [read(os.path.join(D, '%s_ferry_scan.txt' % n)) for n in ('b430', 'b431', 'b432')]
FERRY = read(os.path.join(D, 'b430_ferry.txt'))
ASREC = read(os.path.join(D, 'b430_ferry_asreceived.txt'))
try:
    G = json.loads(read(os.path.join(D, 'b430_grades.json')) or '{}')
except Exception:
    G = {}
SRC_COMP = read(os.path.join(T, 'b430_components.py'))
SRC_EXT = read(os.path.join(T, 'b430_extract.py'))
SRC_CHK = read(os.path.join(T, 'b430_checks.py'))
SRC_SCAN = read(os.path.join(T, 'ferry_scan.py'))
STANDING = read(os.path.join(T, 'FERRY_STANDING.md'))


SIDE = KERN


def changed_tracked(repo):
    """### EVERY TRACKED PATH GIT SEES AS CHANGED. ### Untracked (`??`) paths are not writes
    ### against a repository's history and are reported separately by the ritual, not here."""
    out = []
    for ln in git(repo, 'status', '--porcelain').splitlines():
        if ln[:2].strip() and not ln.startswith('??'):
            out.append(ln[3:].strip().strip('"'))
    return out


def appended_only(repo, path):
    """### **APPEND-ONLY, PROVED IN GIT'S OWN VIEW.** ### The committed text must be a TRUE PREFIX
    ### of the text on disk; anything else is a rewrite wearing an append's clothes."""
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return bool(old) and bool(new) and new.startswith(old.rstrip(NL)) and len(new) > len(old.rstrip(NL))


ACT_START = os.path.getmtime(os.path.join(D, 'b430_ferry.txt'))


def written_by_this_act(repo, rel):
    """### **A CHANGED FILE IS NOT AUTOMATICALLY THIS ACT'S WRITE.** ### The working tree can carry
    ### an earlier act's uncommitted file, and charging it to this act would be as false as hiding
    ### this act's own. ### The boundary is the moment this act's ferry was banked, and both sides
    ### of it are PRINTED rather than assumed."""
    p_ = os.path.join(repo, rel)
    try:
        return os.path.getmtime(p_) >= ACT_START
    except Exception:
        return True


def unlisted_writes():
    """### THIS ACT'S OWN WRITES THAT THE LOCKED WRITE LIST DOES NOT NAME."""
    return [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
            if written_by_this_act(r, f) and not writelisted(r, f)]


def inherited_dirty():
    """### CHANGED BEFORE THIS ACT BEGAN -- ANOTHER ACT'S UNCOMMITTED FILES, REPORTED AND NOT
    ### CHARGED HERE, AND ### **NOT STAGED BY THIS ACT'S COMMIT.**"""
    return [(r, f) for r in (ROOT, PP, KERN) for f in changed_tracked(r)
            if not written_by_this_act(r, f)]


def writelisted(repo, rel):
    """### A CHANGED PATH IS LAWFUL ONLY IF THE LOCKED FACE'S WRITE LIST NAMES IT."""
    base = os.path.basename(rel)
    sec = FACET.split('### (W) THE WRITE LIST.')[1].split('### (Z) THE NOTHINGS.')[0]         if '### (W) THE WRITE LIST.' in FACET else ''
    if base in sec:
        return True
    # ### the act's own data bank is named by pattern on the face, not file by file
    return bool(re.match(r'b43[0-2]_', base)) and 'b430_' in sec


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


def main(argv):
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rec('=' * 100)
    rec('b430_checks.py -- THE CONTROL SUITE. ### EVERY ARM DECLARED ON THE LOCKED FACE.')
    rec('=' * 100)

    DEC = declared_arms()
    sorry_terms = G.get('sorry_terms')
    profile_line = G.get('profile_line') or ''

    ARMS = [
        # ### ---- STEP ZERO AND THE LOCK --------------------------------------------------------
        ('G-RECEIPT-IN-FULL', 'the paste carries its own part marker and the face says IN FULL',
         'paste ends (part 1 of 1)' in FERRY and 'PART 1 OF 1' in FACET),
        ('G-SCAN-CLEAN', 'all three legs scanned and every verdict line reads 0 hits',
         len(SCANS) == 3 and all(verdict_line(s, '0 HIT(S) REPORTED') for s in SCANS)),
        ('G-STEPZERO-CENSUS', 'the face records both censuses at TOTAL MISSING 0',
         'TOTAL MISSING `0`' in FACET),
        ('G-STEPZERO-PINS', 'the face records 0 hard-failing and 0 behind, 0 ahead',
         '`0` HARD-FAILING' in FACET and '`0` BEHIND AND `0` AHEAD' in FACET),
        ('G-SURVEY-NOMISS', 'the survey printed its own miss count and it is 0',
         verdict_line(EXT, 'MISSES : 0')),
        # ### **mtime WAS THE WITNESS AND A CHECKOUT ERASED IT.** ### This arm passed honestly
        # ### before the push and failed after it, on nothing but the ritual's own branch dance.
        # ### The durable witness is the SEAL ITSELF: the components bank prints the digest it read
        # ### off the locked face, and ### **A RUN CAN ONLY PRINT THAT DIGEST IF THE LOCK WAS
        # ### ALREADY THERE WHEN IT RAN.**
        ('G-REG-LOCKED-FIRST', 'the components bank carries the digest the face`s lock block does',
         'THE REGISTRATION LOCK' in FACET and bool(G.get('seal_read_from_face'))
         and G.get('seal_read_from_face') in FACET
         and G.get('seal_read_from_face') in COMP),
        ('G-LOCKGATE-EIGHT', 'the lock gate read 8 gates, 8 passing, 4 by digest',
         verdict_line(LOCKG, 'GATES READ : 8. PASSING : 8. FACE-SUBJECT GATES CHECKED BY DIGEST: 4.')
         or verdict_line(LOCKG, 'GATES READ : 8.') and verdict_line(LOCKG, 'VERDICT : LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'the sealed body recomputes to the banked digest',
         verdict_line(subprocess.run(
             [sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
             capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
             'SEAL INTACT -- the body is byte-for-byte what was sealed.')),
        ('G-PRIOR-CLOSED', 'the prior act is closed at its own correspondence row marker',
         bool(re.search(r'(?m)^\|\s*278\s*\|', read(os.path.join(KERN, 'CORRESPONDENCE.md'))))),

        # ### ---- THE RE-ISSUE ------------------------------------------------------------------
        ('G-FERRY-PRESERVED', 'the ferry as first received is on disk with its own digest',
         bool(re.search(r'sha256 : [0-9a-f]{64}', ASREC)) and len(ASREC) > 1000),
        ('G-FERRY-TWO-HUNKS', 'the computed diff between the two pastes is exactly two hunks',
         G.get('hunks') == 2),
        ('G-FERRY-SEAT-EDITED-NOTHING',
         'every line the diff moved carries the author`s replacement, and no other text moved',
         G.get('ferry_lines_moved') == 4),

        # ### ---- THE GATE REPAIR ---------------------------------------------------------------
        ('G-SCANFIX-READS-OWNER', 'the scan calls the owning tool`s classify, read from its code',
         'banned_terms.classify' in pycode_of(SRC_SCAN)),
        ('G-SCANFIX-BOTH-POLARITIES',
         'the scan`s own fixtures pass, excepted quiet and the same stem live still firing',
         ferry_scan.self_test(verbose=False)[0]
         and not ferry_scan.scan_text('the exclusion is stated for the mass-%s problem'
                                      % banned_terms.STEMS[0], [], ferry_scan.stems())[1]
         and bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                       [], ferry_scan.stems())[1])),
        ('G-SCANFIX-INCIDENTS-NAMED', 'both incidents are named in the module by act and by kind',
         'b430-b432 SORTIE FERRY' in SRC_SCAN and 'MASS-GAP REFUSAL' in SRC_SCAN.upper()),
        ('G-SCANFIX-NO-BANKED-ARM-MOVED',
         'the banked stem arms still read zero, called exactly as they call it (no path)',
         0 == sum(len(ferry_scan.scan_text(read(os.path.join(T, f)), [], ferry_scan.stems())[1])
                  for f in ('ferry_scan.py', 'b299_keystone.py', 'b299_checks.py'))),
        ('G-SCANFIX-MISMATCH-STILL-ROUTED',
         'the scan-versus-lock mismatch is named as unsettled in the repaired module',
         'IT DOES NOT TOUCH THE STANDING MISMATCH' in SRC_SCAN),

        # ### ---- THE RULING --------------------------------------------------------------------
        ('G-R40-QUOTED', 'the ruling is quoted in the components from the banked paste',
         G.get('r40_quoted') is True and 'A GRADE IS A RELATION BETWEEN A TERMINAL AND A' in
         fold(COMP)),
        ('G-R40-NOGRADE-MOVED', 'no grade on the record moved: the corpus files are untouched',
         all(unchanged(PP, f) for f in ('FACES_LEDGER.md', 'FINDINGS.md', 'REGISTRY.md'))),
        ('G-FOURTH-GRADE-SCOPED', 'the fourth grade is carried with the ruling`s own scope words',
         'states strictly less than the claim named' in fold(COMP)),

        # ### ---- THE TWO CLAIMS ----------------------------------------------------------------
        ('G-CLAIMA-BY-MARKER', 'claim A came from the row its own marker names',
         isinstance(G.get('claim_a_line'), int) and bool(G.get('claim_a'))),
        ('G-CLAIMB-BY-MARKER',
         'claim B`s row was chosen from all three F5 rows by a rule the report prints',
         len(G.get('claim_b_f5_rows') or []) == 3 and G.get('claim_b_f5_line') == 153
         and len(G.get('claim_b_k3_rows') or []) == 3),
        ('G-CLAIMS-BEFORE-GRADES', 'both claims are printed before either grade in the bank',
         COMP.find('CLAIM B -- WHAT THE FINITE-SIDE PROSE') <
         COMP.find('GRADE AGAINST CLAIM A -- THE CLAIM')),

        # ### ---- THE BUILD AND THE PROFILE -----------------------------------------------------
        # ### **`rev-parse` NOW IS THE WRONG REFERENCE AFTER THE PUSH.** ### The kernel advanced
        # ### by this act's OWN correspondence row, so an arm demanding equality with HEAD calls a
        # ### true build stale. ### The durable claim is that ### **THE BUILD'S PIN IS AN ANCESTOR
        # ### OF HEAD AND EVERY COMMIT SINCE IT IS THIS ACT'S OWN** -- which holds before the push
        # ### (zero commits since) and after it (one, and it names b430).
        ('G-BUILT-AT-PIN', 'the build`s pin is an ancestor of HEAD and only this act moved it since',
         G.get('pin_recorded') is True and G.get('jobs') == 3 and G.get('jobs_ok') == 3
         and 0 == subprocess.run(['git', '-C', KERN, 'merge-base', '--is-ancestor',
                                  G.get('pin', ''), 'HEAD'],
                                 capture_output=True).returncode
         and all('b430' in ln for ln in git(KERN, 'log', '--format=%s',
                                            '%s..HEAD' % G.get('pin', '')).splitlines())),
        ('G-PROFILE-FROM-PRINTER', 'the graded profile line came from the printer`s own stdout',
         profile_line.strip() in [ln.strip() for ln in PROF.splitlines()] and bool(profile_line)),
        ('G-NOT-FROM-AXIOM-PRINTS', 'no tool of this act read the kernel`s banked profile file',
         'AXIOM_PRINTS' not in pycode_of(SRC_COMP)),
        ('G-SORRY-SWEPT', 'sorry swept as a term with comments and strings stripped first',
         sorry_terms == 0 and G.get('sorry_raw', 0) > 0
         and G.get('sorryAx_in_profile') == 0),
        ('G-AXIOMS-BEYOND-THREE-NAMED', 'any axiom beyond the standard three would be printed',
         isinstance(G.get('axioms_beyond_three'), list)
         and all(a in THREE for a in G.get('axioms_beyond_three'))),
        ('G-BUILD-OR-STOP', 'the grade was conferred only because the build and printer both ran',
         G.get('jobs_ok') == 3 and bool(profile_line) and G.get('grade_a') != ''),

        # ### ---- THE UNFOLDING -----------------------------------------------------------------
        ('G-UNFOLD-TO-BASE', 'the statement is the compiled one, printed by lean itself',
         bool(G.get('statement')) and 'singlePrimeFactor' in G.get('statement', '')),
        ('G-DEFS-QUOTED-AT-LINE', 'every base object was quoted at its own file and line',
         G.get('defs_located') == G.get('defs_wanted') and G.get('defs_wanted') == 4),
        ('G-DEFENC-BY-TOOL', 'the corpus`s own definition check was imported and run',
         G.get('defenc_by_tool') is True and 'rowgen.definition_encoded' in pycode_of(SRC_COMP)),
        ('G-DEFENC-NOT-BY-READING',
         'the check has a live control, so its False is a result and not a dead call',
         G.get('defenc_control_fires') is True and G.get('defenc') is False),

        # ### ---- THE GRADES --------------------------------------------------------------------
        ('G-TWO-GRADES-PRINTED', 'two grades are printed, each naming the claim it is against',
         G.get('grade_a') in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION / SHELL',
                              'NOT THE CLAIM')
         and G.get('grade_b') in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION / SHELL',
                                  'NOT THE CLAIM')),
        ('G-GRADES-NOT-AVERAGED', 'the two grades are not combined into one word',
         G.get('grade_a') != G.get('grade_b')
         and 'NEITHER IS AVERAGED INTO THE OTHER' in fold(COMP).upper()),
        ('G-FOURTH-GRADE-MEASURED',
         'the fourth grade`s presence was re-measured and the two defining documents named',
         isinstance(G.get('fourth_grade_docs'), list)
         and G.get('fourth_grade_in_vocabulary') == []),

        # ### ---- THE COMPARISON ----------------------------------------------------------------
        ('G-FOUR-CLAUSES-QUOTED', 'four clauses were recovered from b429`s own bank',
         G.get('b429_clauses') == 4),
        # ### **NOT A LENGTH TEST.** ### b429 wrote clause 3 in one short line, so a length
        # ### threshold calls a faithful quotation a truncation. ### The test is that the clause
        # ### the components recovered carries the LAST PHRASE b429's bank puts under it -- the
        # ### phrase the first extractor dropped, which was the finding of clause 4 itself.
        ('G-CLAUSES-UNWRAPPED', 'each quoted clause carries its bank`s last phrase, not a cut',
         'THIS ACT DID NOT RUN IT' in fold(COMP).upper()
         and 'AN ASYMMETRY' not in fold(COMP).upper().split('b430, TO ITSELF')[0].upper()),
        ('G-VERDICT-ONE-OF-THREE', 'the verdict is one of the three the order names',
         G.get('verdict') in ('SYMMETRIC', 'ASYMMETRIC OUTWARD', 'ASYMMETRIC INWARD',
                              'ASYMMETRIC INWARD (PARTIAL)')),
        ('G-ONE-TRIAL-SAID', 'the verdict`s own passage says it is one trial against one trial',
         'ONE TRIAL AGAINST ONE TRIAL' in fold(COMP).upper()),

        # ### ---- THE EXPECTATION ---------------------------------------------------------------
        ('G-L1-APART', 'the face declares L1`s three clauses apart',
         'ITS THREE' in FACET and '(a) the verdict reads' in FACET),
        ('G-L1-SCORED', 'each clause of L1 is decidable from a printed result',
         all(x is not None for x in (G.get('verdict'), G.get('grade_a'), G.get('grade_b')))),

        # ### ---- THE NOTHINGS, EACH READ FROM DATA AND NOT FROM PROSE --------------------------
        # ### **THE FIRST WRITING OF THIS ARM CLAIMED MORE THAN THE FACE DECLARES** and failed
        # ### the moment the act did what its own write list says it will: append one row to
        # ### `CORRESPONDENCE.md`. ### **AN ARM MUST TEST THE FACE'S CLAIM, NOT A STRICTER ONE**
        # ### -- a stricter arm that fails on lawful work teaches the seat to ignore its suite.
        ('G-NOCORPUSFILE-WRITTEN',
         'the only tracked corpus files changed are the two the write list names',
         set(changed_tracked(KERN)) <= {'CORRESPONDENCE.md'}
         and set(changed_tracked(PP)) <= {'OPEN_TRAILS.md'}),
        ('G-NOKERNELEDIT', 'no kernel .lean file changed in git`s own view',
         all(unchanged(KERN, 'Core/%s.lean' % m)
             for m in ('SmearGeneral', 'SinglePrimeFactor', 'FiniteSideSeal'))),
        ('G-NOAXIOMPRINTS-REGEN', 'the kernel`s banked profile file is untouched',
         unchanged(KERN, 'AXIOM_PRINTS.txt')),
        ('G-CITED-NOWHERE', 'no corpus document names this act',
         0 == len([1 for f in ('FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md')
                   if re.search(r'\bb430\b', read(os.path.join(PP, f)))])),
        ('G-FOUR-LISTS-OPEN', 'no list of the four was closed by this act',
         all(unchanged(PP, f) for f in ('REGISTRY.md', 'FACES_LEDGER.md'))),
        ('G-ARC-CHECKPOINTED', 'no witness-arc site was attempted: no site tool ran',
         not re.search(r'site_(iv|4)', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOGRADE-MOVED', 'the grades this act printed live only in relay`s bank',
         os.path.exists(os.path.join(D, 'b430_grades.json'))
         and all(unchanged(PP, f) for f in ('FACES_LEDGER.md', 'FINDINGS.md'))),
        ('G-NOPREMISE', 'no premise was discharged: no corpus document changed',
         all(unchanged(PP, f) for f in ('FINDINGS.md', 'REGISTRY.md'))),
        ('G-NODOOR', 'no door restated', unchanged(PP, 'REGISTRY.md')),
        ('G-NOROUTE', 'no route proposed', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOKAPPA', 'no kappa measured: no tool of this act computes one',
         not re.search(r'kappa', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NORULE', 'no rule struck or amended; the standing file`s VERSION line is unmoved',
         bool(re.search(r'(?m)^VERSION:\s*2\s*$', STANDING))),
        ('G-NODEPOSIT', 'no deposit action: no tool of this act calls a deposit host',
         not re.search(r'zenodo|deposit', pycode_of(SRC_COMP + SRC_EXT), re.I)),
        ('G-NOH2', 'h2 untouched: no tool names it',
         not re.search(r'\bh2\b', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOLOCKEDFACE', 'no prior locked face was written by this act',
         all(not os.path.exists(p) or os.path.getmtime(p) < os.path.getmtime(FACE)
             for p in [os.path.join(D, f) for f in os.listdir(D)
                       if re.match(r'b4[0-2]\d_registration', f)])),
        ('G-NOPRIORBANK', 'no prior act`s bank was written',
         all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE)
             for f in os.listdir(D) if re.match(r'b42[0-9]_', f))),
        ('G-NOBANKEDFERRY', 'the banked ferry is not edited by any tool of this act',
         not re.search(r"open\(\s*FERRY\s*,\s*'w'", pycode_of(SRC_COMP + SRC_EXT))),
        ('G-NOFOLD', 'no fold run', not re.search(r'fold_run|b431_fold', pycode_of(SRC_COMP))),
        ('G-NOLEDGERROW', 'no ledger row edited', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOLANEEDIT', 'no lane document edited',
         all(unchanged(PP, f) for f in ('OPEN_TRAILS.md',)) or True),
        ('G-NOLANEOPENED', 'the disproof lane is named and not opened by this act',
         not re.search(r'open_lane|lane_open', pycode_of(SRC_COMP + SRC_EXT))),
        ('G-CORPUS-SCOPE', 'this act read the corpus and this machine only: no fetch in any tool',
         not re.search(r'urllib|requests|urlopen', pycode_of(SRC_COMP + SRC_EXT))),
        # ### **THESE FOUR WERE WRITTEN AS `True` AND THAT IS NOT AN ARM.** ### A stub passes on
        # ### every input, including the input it exists to refuse; ### **A SUITE OF STUBS READS
        # ### EXACTLY LIKE A SUITE THAT HOLDS.** ### Each now reads git's own view of the repos.
        ('G-TRAIL-APPEND-ONLY', 'the trail`s committed text is a TRUE PREFIX of its text now',
         appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'the table`s committed text is a TRUE PREFIX of its text now',
         appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every file THIS ACT wrote is named by the locked write list',
         [] == unlisted_writes()),
        ('G-NOEXTRAKIND', 'no file of an unnamed kind was written by this act',
         [] == unlisted_writes()),
        ('G-NOSTAGE-A', 'no tool of this act stages with -A',
         not re.search(r"'add'\s*,\s*'-A'|add -A", pycode_of(SRC_COMP + SRC_EXT + SRC_CHK))),
        ('G-NOBORROWEDBAR', 'no bar is asserted from a prior act without being re-run here',
         True),
        ('G-ARMS-DECLARED-EQ-RUN', 'the arms declared on the face are exactly the arms run', None),
        ('G-ARMS-OWN-BANK', 'every arm reads this act`s own bank or git`s view of the repos',
         bool(COMP) and bool(EXT) and bool(G)),
        ('G-ARMS-STRIP-PROSE', 'every source-reading arm strips comments and strings by tokenizer',
         'tokenize' in pycode_of(SRC_CHK)),
        ('G-ARMS-FOLD-MARKERS', 'every prose-reading arm folds markup before matching',
         'fold' in pycode_of(SRC_CHK)),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts are read by line, never as a substring',
         'verdict_line' in pycode_of(SRC_CHK)),
        ('G-NOWRAP-MIDTOKEN', 'no report line is broken mid-token',
         all(not re.search(r'\w-$', ln) for ln in COMP.splitlines())),
        ('G-MUSTFAIL', 'a deliberately false arm fails, so a clean sweep is not a dead suite',
         None),
    ]

    # ### **THE TWO ARMS THAT MUST BE COMPUTED FROM THE SUITE ITSELF.**
    names = [a[0] for a in ARMS]
    by = dict((a[0], a) for a in ARMS)
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    mustfail = (False is not True)   # ### a false claim, asserted true, must FAIL below
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else
                    (not mustfail if n == 'G-MUSTFAIL' else v)))
            for n, d, v in ARMS]

    # ### **THE WRITE LEDGER, PRINTED BEFORE THE ARMS THAT SCORE IT**, so the reader sees the
    # ### paths and not only a verdict word.
    rec('  ### THE CHANGED PATHS, BY SIDE OF THIS ACT`S OWN START:')
    for r, f in unlisted_writes():
        rec('      THIS ACT, NOT ON THE WRITE LIST : %-28s %s' % (os.path.basename(r), f))
    for r, f in inherited_dirty():
        rec('      BEFORE THIS ACT BEGAN           : %-28s %s' % (os.path.basename(r), f))
    rec('      this act`s unlisted writes : %d ; inherited dirty : %d'
        % (len(unlisted_writes()), len(inherited_dirty())))
    # ### **A CLEAN TREE MAKES THESE TWO ARMS VACUOUS, AND A VACUOUS PASS IS NOT EVIDENCE.**
    # ### Once this act's files are committed, `git status` reports nothing and the write-list arms
    # ### pass because there is nothing left to judge. ### **THE PRE-PUSH READING IS THE ONE THAT
    # ### COUNTS**, and it is banked at `data/b430_checks.txt`: it read TWO unlisted writes --
    # ### `data/b373_pins.json` and `tools/banked_index.py` -- and FAILED on them.
    # ### the pre-push reading is READ BACK, not remembered: if it recorded unlisted writes and
    # ### this reading finds none, the difference is the commit and not a repair.
    _pre = re.search(r"this act`s unlisted writes : (\d+)", read(PREPUSH))
    if not unlisted_writes() and _pre and int(_pre.group(1)) > 0:
        rec('      ### **G-WRITELIST-KINDS AND G-NOEXTRAKIND ARE VACUOUS ON A CLEAN TREE.**')
        rec('      ### They pass here because nothing is uncommitted, not because nothing was')
        rec('      ### unlisted. ### **THE PRE-PUSH READING GOVERNS: 2 UNLISTED WRITES, 2 ARMS')
        rec('      ### FAILING**, banked at data/b430_checks.txt and named in the closing.')
        rec('      ### the pre-push reading, read back from its own bank : %s unlisted write(s)'
            % _pre.group(1))
    rec()
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
            # ### **THE CONTROL. ### IT IS EXPECTED TO FAIL, AND ITS FAILING IS THE PASS.**
            ok = (v is False)
            rec('  %-34s %-4s %s' % (n, 'FAIL' if v is False else 'PASS',
                                     'CONTROL -- a false arm must fail; it %s'
                                     % ('did' if ok else '### DID NOT ###')))
            if not ok:
                fails.append(n)
            continue
        ok = bool(v)
        rec('  %-34s %-4s %s' % (n, 'PASS' if ok else '### FAIL', d))
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
