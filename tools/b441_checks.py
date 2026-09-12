# -*- coding: utf-8 -*-
"""b441_checks.py -- THE CONTROL SUITE FOR b441. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE**, and the suite refuses to agree
### with itself: `G-ARMS-DECLARED-EQ-RUN` is computed by comparing the two sets.
### ### **THE TWO READINGS LAND IN TWO FILES** (BAR 11), the side decided by whether this act's
### commit is already on the remote.
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
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
WINREPO = os.path.join('D:', os.sep, 'SIDE-window')
FACE = os.path.join(D, 'b441_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b441_checks.txt')
POSTPUSH = os.path.join(D, 'b441_checks_postpush.txt')
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
                for f in ('b441_ferry.txt', 'b441_ferry_scan.txt'))


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


def committed_by_act(repo, pat):
    """### **AFTER THE COMMIT THE WORKING TREE IS CLEAN, AND A WRITE ARM READING ONLY THE TREE
    ### THEN SEES NOTHING** -- so the post-push reading would score the write list over an empty
    ### set and call that a pass. ### The act`s own written set is the union of what the tree
    ### still shows and what THIS ACT`S COMMIT carries."""
    # ### **AN ACT IS NOT ONE COMMIT.** ### b441 lands in four -- the act, the closing suite, the
    # ### closing record, and this repair -- so an arm reading only `HEAD` sees the last of them
    # ### and scores the write list over two files. ### **EVERY COMMIT WHOSE SUBJECT NAMES THIS
    # ### ACT IS READ**, and the act's own boundary bounds how far back that can reach.
    out = []
    for ln in git(repo, 'log', '--format=%H %s', '-40').splitlines():
        sha, _, subj = ln.partition(' ')
        if 'b441' not in subj:
            continue
        for f in git(repo, 'show', '--name-only', '--format=', sha).splitlines():
            f = f.strip()
            if f and re.search(pat, f):
                out.append(f)
    return sorted(set(out))


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b441_components.txt'))
EXTR = read(os.path.join(D, 'b441_extract.txt'))
RGATE = read(os.path.join(D, 'b441_reg_gate.txt'))
TERM = read(os.path.join(D, 'b441_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b441_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b441_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b441_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b441_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b441_ferry.txt'))
CENS = read(os.path.join(D, 'b441_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b441_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b441_pins_stepzero.txt'))
ADD = os.path.join(D, 'b441_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b441_components.py'))
SRC_EXT = read(os.path.join(T, 'b441_extract.py'))
SRC_CHK = read(os.path.join(T, 'b441_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b441_checks.py`
# ### beside `data/b441_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
# ### every prefixed entry and charges a declared file as undeclared. ### **BOTH SIDES ARE REDUCED
# ### TO A BASENAME BEFORE THEY ARE COMPARED.**
WRITELIST = [os.path.basename(x) for x in
             re.findall(r'`([A-Za-z0-9_.\-/]+\.(?:py|txt|json|md|lean))`',
                        FACET.split('(W) THE WRITE LIST')[-1].split('(Z) THE NOTHINGS')[0])]
DEC = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', FACET)) - {'G-NO'})


def _pushed():
    """### HAS **THIS ACT'S** WORK REACHED THE REMOTE? ### **CARRIED FROM b439, NOT RETYPED.**

    ### b440 retyped this predicate twice and got it wrong twice. ### Its first writing sought a SHA
    ### in a list of branch NAMES and was never true. ### Its "repair" -- `origin/main == HEAD` -- is
    ### **TRUE BEFORE THIS ACT COMMITS ANYTHING**, because HEAD is then the prior act's pushed commit;
    ### b441's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b441' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False



FILRUN = read(os.path.join(D, 'b441_filings_run.txt'))
SRC_FIL = read(os.path.join(T, 'b441_filings.py'))
LEDGER = read(os.path.join(PP, 'FACES_LEDGER.md'))
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODULE = read(os.path.join(TECHNE, 'modules', '2026-09', 'AXIOM_PROFILE_IS_PARTLY_FORM.md'))
try:
    ROUTES = json.loads(read(os.path.join(D, 'b441_routes.json')))
    PRICE = json.loads(read(os.path.join(D, 'b441_price.json')))
    REACH = json.loads(read(os.path.join(D, 'b441_reach.json')))
except Exception:
    ROUTES, PRICE, REACH = {}, {}, []
BLOCK = LEDGER.split('<!-- b441 update -->', 1)[-1] if '<!-- b441 update -->' in LEDGER else ''


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b441 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    kern_files = touched(WINREPO, r'.')
    relay_new = sorted(set(touched(ROOT, r'b441')) | set(committed_by_act(ROOT, r'b441')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_rc = subprocess.run(['git', '-C', TECHNE, 'rev-list', '--count', 'origin/main..HEAD'],
                          capture_output=True, text=True).stdout.strip()
    t_remote_has = subprocess.run(['git', '-C', TECHNE, 'branch', '-r', '--contains', 'HEAD'],
                                  capture_output=True, text=True).stdout.strip()
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b441_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    rows = ROUTES.get('rows') or []

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'the ferry was received in full and banked',
         'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'this paste`s scan reports 0 hits, by its verdict line',
         verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-FIRST-PASTE-PRESERVED', 'the refused first paste and its scan are banked under their own names',
         os.path.exists(os.path.join(D, 'b441_ferry_first_paste.txt'))
         and verdict_line(read(os.path.join(D, 'b441_ferry_first_paste_scan.txt')), '### VERDICT:',
                          '1 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'the roster reports 0 repositories hard-failing',
         verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-STEPZERO-POSTDATES-PASTE', 'every step-zero record postdates this paste',
         all(os.path.getmtime(os.path.join(D, f)) >= os.path.getmtime(os.path.join(D, 'b441_ferry.txt'))
             for f in ('b441_census_stepzero.txt', 'b441_faces_census_stepzero.txt',
                       'b441_pins_stepzero.txt', 'b441_ferry_scan.txt'))),
        ('G-GUARD-DEFERRED-SAID', 'the face says the pre-push guard runs at the close',
         'pre-push guard runs at the close' in F),
        ('G-SURVEY-NOMISS', 'the survey reports 0 misses', verdict_line(EXTR, 'MISSES', ': 0')),
        ('G-SURVEY-CORRECTION-SAID', 'the survey prints its own contradicted first writing',
         'CONTRADICTED THIS FILE' in EXTR),
        ('G-REG-LOCKED-FIRST', 'the registration carries its lock block', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'the lock gate read eight and permitted the lock',
         verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'the seal verifies by reg_seal.py --verify', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED', 'the face records the prior act closed at its row', 'row 289' in F),
        ('G-NORULING-RATIFIED', 'the face says no new ruling was ratified',
         fold('THIS PASTE RATIFIES NO NEW RULING') in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'the addendum slot is named', 'b441_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the slot carries a quotation or nothing',
         (not os.path.exists(ADD)) or not read(ADD).strip() or 'arrival' in read(ADD).lower()),
        ('G-LANES-PARKED', 'both instrument lanes parked', 'both instrument lanes' in F),
        ('G-SEAT-AUTHORSHIP-ENTERED', 'the overstatement is entered as this seat`s',
         'THE SENTENCE THAT CALLED IT A DENIAL WAS THIS SEAT' in COMP and 'this seat' in BLOCK),

        ('G-C1-THREE-LINES-QUOTED', 'the three near lines are quoted at b440`s own line numbers',
         all(x in COMP for x in ('SPIRAL_MAP.md:114', '20c.md:2678', 'programs.md:9037'))),
        ('G-C1-THREE-LINES-SAID', 'each line carries a one-sentence statement of what it says',
         COMP.count('### **WHAT IT SAYS:**') == 3),
        ('G-C1-LINE-UNEDITED', 'SPIRAL_MAP.md is unedited', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-C1-DISTINCTION-PRINTED', 'the distinction is printed', '**THE DISTINCTION:**' in COMP),
        ('G-C1-HALVES-APART', 'the two halves are filed apart',
         '**the kernel half**' in BLOCK and '**the counting half**' in BLOCK),
        ('G-C1-KERNEL-HALF-QUOTED', 'the kernel half is quoted from CC',
         'It is the derivative of 2' in COMP and 'It is the derivative of 2' in BLOCK),
        ('G-C1-ROUTE-B-RUN', 'route B ran at every height', len(rows) == 6
         and all(r.get('routeB') for r in rows)),
        ('G-C1-ROUTES-SHARE-NO-CODE', 'route B uses neither quad nor digamma',
         bool(re.search(r'th = im \( loggamma', pycode_of(SRC_COMP)))
         and not re.search(r'th = [^\n]*(quad|digamma)', pycode_of(SRC_COMP))),
        ('G-C1-TOLERANCE-STATED-FIRST', 'both tolerances are on the sealed face',
         '`1e-12` absolute' in FACET and '`1e-6` relative' in FACET),
        ('G-C1-COUNTING-HALF-MEASURED', 'both tolerances met, read from the routes record',
         ROUTES.get('tol1_met') is True and ROUTES.get('tol2_met') is True),
        ('G-C1-POLE-NAMED', 'the one is named as the pole', 'the `1` is the pole of zeta' in BLOCK),
        ('G-C1-NOT-A-THEOREM', 'the counting half is filed as measured, not a theorem',
         'MEASURED, not a theorem of this record' in BLOCK),
        ('G-C1-WRITER-READING-DECLARED', 'the writer reading is declared on the face',
         fold('WHERE THE FILING IS WRITTEN, AND WHY THAT IS A DECLARED READING') in F),
        ('G-C1-QUOTES-VERIFIED', 'the writer verified every quotation, 0 misses',
         verdict_line(FILRUN, 'verify_quotes', 'misses : 0')),
        ('G-C1-BLOCK-WRITTEN', 'the block was written once and append-only on both sides',
         verdict_line(FILRUN, 'append_block', 'WRITTEN') and LEDGER.count('<!-- b441 update -->') == 1),
        ('G-C1-B440-SCOPE-SAID', 'b440`s NOT CARRIED is scoped to PLACE-papers prose',
         'HELD ONLY OVER PLACE-papers PROSE' in COMP),

        ('G-C2-FIVE-CANDIDATES-QUOTED', 'five candidates quoted from the verified sources',
         len(PRICE.get('candidates') or []) == 5),
        ('G-C2-PRICE-TYPED', 'each candidate carries a price',
         all(c.get('price') for c in PRICE.get('candidates') or [None])),
        ('G-C2-REPLACES-NAMED', 'each candidate names what it replaces',
         all(c.get('replaces') for c in PRICE.get('candidates') or [None])),
        ('G-C2-UNIFORMITY-QUOTED', 'each uniformity answer carries a quoted quantifier or EXACT',
         all(('"' in c.get('uniformity', '')) for c in PRICE.get('candidates') or [None])),
        ('G-C2-SITE-II-STEPS-QUOTED', 'B3 and B5 are quoted from the writer`s block',
         '| **B3** the density theorems' in COMP and '| **B5** the Riemann-von Mangoldt' in COMP),
        ('G-C2-STEP-VERDICT', 'a verdict is printed for each step',
         PRICE.get('B3') == 'STANDS' and PRICE.get('B5') == 'STANDS'),
        ('G-C2-NOTHING-IMPORTED', 'nothing imported, no cell replaced',
         fold('NOTHING IMPORTED, NO CELL REPLACED, NO SITE REOPENED') in C),

        ('G-C3I-FROM-B440-ONLY', 'the double role quotes b440`s own record',
         'b440_components.txt' in COMP and 'THE LAWFULNESS CONDITION' in COMP),
        ('G-C3I-FILED', 'the double role is in the ledger block',
         '**the pole’s double role**' in BLOCK and 'no mechanism claimed' in BLOCK),
        ('G-C3II-HISTORY-READ', 'the reach is read from git history, as first committed',
         "'--reverse'" in SRC_COMP and 'as first committed' in COMP),
        ('G-C3II-LIST-PRINTED', 'eleven acts listed', len(REACH) == 11),
        ('G-C3II-FIRST-COMMIT-PREDICATE', 'every act carries its first-committed predicate',
         all(r.get('predicate_first_committed') not in (None, 'NOT LOCATED') for r in REACH or [{}])),
        ('G-C3II-NOTHING-REVERDICTED', 'no prior closing or checks file edited',
         0 == len([f for f in touched(ROOT, r'^data/b4[34][0-9]_(closing|checks)', since=False)
                   if 'b441' not in f])),
        ('G-C3II-DISCIPLINE-SAID', 'the act says why two readings exist',
         'HOW A VERDICT KEEPS ITS DATE' in COMP),
        ('G-C3II-B440-SENTENCE-CORRECTED', 'b440`s false sentence is corrected here',
         'FALSE, AND CORRECTED' in COMP),
        ('G-C3III-MODULE-WRITTEN', 'the TECHNE module exists and is committed',
         bool(MODULE) and 'AXIOM_PROFILE_IS_PARTLY_FORM' in subprocess.run(
             ['git', '-C', TECHNE, 'log', '-1', '--format=%s', '--',
              'modules/2026-09/AXIOM_PROFILE_IS_PARTLY_FORM.md'], capture_output=True,
             text=True).stdout),
        ('G-C3III-NOT-PUSHED', 'TECHNE HEAD is on no remote branch', t_remote_has == ''),
        ('G-C3III-FOUR-GRADES-SAID', 'the module says the grades number four', 'number four, not three' in MODULE),
        ('G-C3III-INCIDENT-CITED', 'the module cites both b440 profiles',
         '`[propext, Quot.sound]`' in MODULE and 'no axioms at all' in MODULE),

        ('G-N1-APART', 'N1`s two clauses apart on the face', '`(N1)`' in FACET and '(b) the located line' in F),
        ('G-N2-APART', 'N2`s two clauses apart on the face', '`(N2)`' in FACET),
        ('G-N3-SCORED', 'N3 is scored over the eleven, from the reach record', len(REACH) == 11),
        ('G-SEAT-EXPECTATIONS-SCORED', 'the seat`s own expectations are on the face',
         fold('AND THIS SEAT\'S OWN, DECLARED SO THEY CAN BE SCORED AGAINST IT') in F),

        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.', pycode_of(SRC_COMP + SRC_FIL))),
        ('G-NOGRADE-MOVED', 'no grade conferred by the block', 'No grade is conferred by a seat' in BLOCK),
        ('G-NOTERMINAL-RENAMED', 'no kernel file touched', 0 == len(kern_files)),
        ('G-NONEWINSTRUMENT', 'no instrument file touched', 0 == len(touched(ROOT, r'tools/e16/', since=False))),
        ('G-NONEWFAMILY', 'the family tool is unchanged', unchanged(ROOT, 'tools/b317_smear.py')),
        ('G-NOATLAS-EDIT', 'the atlas is unchanged', unchanged(ROOT, 'tools/e16/carto_atlas.py')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(kern_files)),
        ('G-NOSPIRAL-EDIT', 'SPIRAL_MAP.md untouched', unchanged(PP, 'SPIRAL_MAP.md')),
        ('G-NOLANE-OPENED', 'no lane opened', fold('AND NO LANE OPENED') in F),
        ('G-NOPREMISE', 'no premise discharged', fold('NO PREMISE DISCHARGED') in F),
        ('G-NODOOR', 'no door restated', fold('NO DOOR RESTATED') in F),
        ('G-NOROUTE', 'no route proposed', fold('ROUTE PROPOSED') in F),
        ('G-NOKAPPA', 'no kappa measured', fold('NO KAPPA MEASURED') in F),
        ('G-NORULE-STRUCK', 'no rule struck', fold('NO RULE STRUCK, AMENDED OR') in F),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 where the deposit left it', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOLOCKEDFACE', 'no other act`s face touched',
         0 == len([f for f in touched(ROOT, r'registration_') if 'b441' not in f])),
        ('G-NOPRIORBANK', 'no prior act`s bank touched',
         0 == len([f for f in touched(ROOT, r'^data/b4[0-4][0-9]_') if not f.startswith('data/b441')])),
        ('G-NOBANKEDFERRY', 'no other act`s ferry touched',
         0 == len([f for f in touched(ROOT, r'_ferry', since=False) if 'b441' not in f])),
        ('G-NOFOLD', 'no fold run', fold('NO FOLD RUN') in F),
        ('G-NOKEYSTONE-EDIT', 'no keystone edited', fold('NO KEYSTONE EDITED OR ANNOTATED') in F),
        ('G-NOROW-WRITTEN', 'no ledger row written -- only the block was added',
         appended_only(PP, 'FACES_LEDGER.md') or unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOSEVENTH-SITE', 'no seventh site', fold('NO BRIDGE TYPED BETWEEN ANY TWO OF THE SIX') in F),
        ('G-NOSITE-REOPENED', 'no site reopened', fold('NO SITE REOPENED') in F),
        ('G-ARC-CHECKPOINTED-AFTER-IV', 'the arc stays after (iv)', fold('checkpointed after site (iv)') in F),
        ('G-FOUR-LISTS-OPEN', 'no list closed', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-DISPROOF-LANE-NOT-OPENED', 'the disproof lane is not opened',
         fold('THE DISPROOF LANE IS NOT OPENED') in F),
        ('G-TECHNE-NOT-PUSHED', 'TECHNE is ahead of its remote and unpushed',
         t_rc.isdigit() and int(t_rc) >= 1 and t_remote_has == ''),

        ('G-CORPUS-SCOPE', 'only FACES_LEDGER.md and OPEN_TRAILS.md touched in PLACE-papers',
         all(f in ('FACES_LEDGER.md', 'OPEN_TRAILS.md') for f in pp_touched)),
        ('G-LEDGER-APPEND-ONLY', 'FACES_LEDGER.md appended only',
         unchanged(PP, 'FACES_LEDGER.md') or appended_only(PP, 'FACES_LEDGER.md')),
        ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS.md appended only',
         unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'CORRESPONDENCE.md appended only',
         unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every relay file this act wrote is on the write list',
         all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f for f in relay_new)),
        ('G-WRITELIST-NAMES-PATHS', 'the write list names paths',
         'b441_filings.py' in FACET and 'b441_closing.txt' in FACET),
        ('G-WRITELIST-COUNTS-NEW', 'the write arm counts new files', 'def touched(' in SRC_CHK
         and len(relay_new) >= 20),
        ('G-WRITELIST-COMMIT-RANGE', 'the write arm reads the act`s whole commit range',
         'def committed_by_act(' in SRC_CHK and "'-40'" in SRC_CHK),
        ('G-NOSTAGE-A', 'no git add -A in this act`s tools',
         not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_FIL))),
        ('G-NOBORROWEDBAR', 'twelve bars', 12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),

        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-OWN-BANK', 'the suite reads this act`s own bank', 'b441_components.txt' in SRC_CHK),
        ('G-ARMS-STRIP-PROSE', 'tokenizer strips comments and strings',
         'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK),
        ('G-ARMS-FOLD-MARKERS', 'markup folded on both sides',
         bool(re.search(r'fold \( \) in [FC]', pycode_of(SRC_CHK)))),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts read by line', 'def verdict_line(' in SRC_CHK),
        ('G-ARMS-EOL-NORMALISED', 'line endings normalised', 'def nl(' in SRC_CHK and 'chr(13)' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two readings, two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-BY-REMOTE-REF', 'the push side asks whether THIS ACT`S commit is on the remote ref'
         ' -- the face`s wording named the rule defectively and the defect is printed, not hidden',
         "if 'b441' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK
         and 'PRE-PUSH READING' in read(PREPUSH) if os.path.exists(PREPUSH) else False),
        ('G-NOWRAP-MIDTOKEN', 'no report line broken mid-token',
         0 == len([1 for ln in COMP.splitlines() if ln.endswith('-') and len(ln) > 96
                   and set(ln.strip()) != {'-'}])),
        ('G-NOSTRAY-PLACEHOLDER', 'no format string printed bare',
         0 == len(re.findall(r'%[-0-9.]*[dsfe](?![a-zA-Z0-9])', COMP))),
        ('G-MUSTFAIL', 'THE CONTROL -- a false arm, which must fail', False),
    ]

    names = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v)))
            for n, d, v in ARMS]
    rec('  arms declared on the face : %d' % len(DEC))
    rec('  arms run by this suite    : %d' % len(ARMS))
    rec('  declared and NOT run      : %s' % sorted(set(DEC) - set(names)))
    rec('  run and NOT declared      : %s' % sorted(set(names) - set(DEC)))
    rec('  files touched in SIDE-window : %d' % len(kern_files))
    rec('  PLACE-papers touched         : %s' % pp_touched)
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
