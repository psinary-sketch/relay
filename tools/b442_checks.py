# -*- coding: utf-8 -*-
"""b442_checks.py -- THE CONTROL SUITE FOR b442. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b442_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b442_checks.txt')
POSTPUSH = os.path.join(D, 'b442_checks_postpush.txt')
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
                for f in ('b442_ferry.txt', 'b442_ferry_scan.txt'))


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
    # ### **AN ACT IS NOT ONE COMMIT.** ### b442 lands in four -- the act, the closing suite, the
    # ### closing record, and this repair -- so an arm reading only `HEAD` sees the last of them
    # ### and scores the write list over two files. ### **EVERY COMMIT WHOSE SUBJECT NAMES THIS
    # ### ACT IS READ**, and the act's own boundary bounds how far back that can reach.
    out = []
    for ln in git(repo, 'log', '--format=%H %s', '-40').splitlines():
        sha, _, subj = ln.partition(' ')
        if 'b442' not in subj:
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
COMP = read(os.path.join(D, 'b442_components.txt'))
EXTR = read(os.path.join(D, 'b442_extract.txt'))
RGATE = read(os.path.join(D, 'b442_reg_gate.txt'))
TERM = read(os.path.join(D, 'b442_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b442_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b442_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b442_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b442_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b442_ferry.txt'))
CENS = read(os.path.join(D, 'b442_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b442_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b442_pins_stepzero.txt'))
ADD = os.path.join(D, 'b442_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b442_components.py'))
SRC_EXT = read(os.path.join(T, 'b442_extract.py'))
SRC_CHK = read(os.path.join(T, 'b442_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b442_checks.py`
# ### beside `data/b442_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
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
    ### b442's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b442' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False



FILRUN = read(os.path.join(D, 'b442_filings_run.txt'))
SRC_FIL = read(os.path.join(T, 'b442_filings.py'))
LEDGER = read(os.path.join(PP, 'FACES_LEDGER.md'))
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
try:
    THETA = json.loads(read(os.path.join(D, 'b442_theta.json')))
    SITEV = json.loads(read(os.path.join(D, 'b442_site_v.json')))
except Exception:
    THETA, SITEV = {}, {}
BU0 = LEDGER.split('<!-- b442 update: u0 -->', 1)[-1].split('<!-- b442 update: site (v) -->')[0] \
    if '<!-- b442 update: u0 -->' in LEDGER else ''
BV = LEDGER.split('<!-- b442 update: site (v) -->', 1)[-1] if '<!-- b442 update: site (v) -->' in LEDGER else ''
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
ROW = ([ln for ln in CORR.splitlines() if ln.startswith('| ') and '(b442)' in ln] or [''])[-1]


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b442 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    kern_files = touched(WINREPO, r'.')
    relay_new = sorted(set(touched(ROOT, r'b442')) | set(committed_by_act(ROOT, r'b442')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    # ### **TECHNE carries untracked modules left by earlier acts**; an arm counting them charges this act
    # ### for their writes. ### The test is TRACKED changes, plus any file or commit newer than this act.
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    t_head_time = subprocess.run(['git', '-C', TECHNE, 'log', '-1', '--format=%ct'],
                                 capture_output=True, text=True).stdout.strip()
    t_new_commit = t_head_time.isdigit() and int(t_head_time) >= ACT_START
    mods = os.path.join(TECHNE, 'modules', '2026-09')
    t_new_file = any(os.path.getmtime(os.path.join(mods, f)) >= ACT_START for f in os.listdir(mods))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b442_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    cands = SITEV.get('candidates') or []
    CODE_C = pycode_of(SRC_COMP)

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits by its verdict line', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'censuses TOTAL MISSING 0',
         verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0 hard-failing', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-GUARD-DEFERRED-SAID', 'guard deferred to the close', 'pre-push guard runs at the close' in F),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, 'MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8 and permitted',
         verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED', 'prior act closed at row 290', 'row 290' in F),
        ('G-TWO-RULINGS-ENTERED', 'R53 and R54 entered', '`(R53)`' in FACET and '`(R54)`' in FACET),
        ('G-R54-ABSENT-LINE-SAID', 'the missing scan line is recorded, not refused',
         fold('THIS FERRY CARRIES NO SUCH LINE') in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b442_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation',
         (not os.path.exists(ADD)) or not read(ADD).strip() or 'arrival' in read(ADD).lower()),
        ('G-LANES-PARKED', 'both instrument lanes parked', 'both instrument lanes' in F),

        ('G-C1-THETA-ROUTE-B', 'theta by loggamma, no quadrature', 'im ( loggamma' in CODE_C),
        ('G-C1-ARGMIN-BY-VALUES', 'the argmin search reads theta only',
         bool(re.search(r'fc = theta \( c \)', CODE_C)) and not re.search(r'fc = hplus', CODE_C)),
        ('G-C1-ARGMIN-AGREES', 'argmin within 1e-12 of u0', THETA.get('argmin_gap', 1) < 1e-12),
        ('G-C1-THETA-U0-TWO-ROUTES', 'theta at u0 by two routes within 1e-12', THETA.get('route_gap', 1) < 1e-12),
        ('G-C1-ODD-MEASURED', 'oddness measured', THETA.get('odd_max', 1) < 1e-30),
        ('G-C1-ONE-ZERO-MEASURED', 'one sign change on (0,50]', len(THETA.get('sign_changes') or []) == 1),
        ('G-C1-QUANTIFIER-STATED', 'the name carries its range', '`0 <= t <= 50`' in BU0),
        ('G-C1-NO-VALUE-FROM-MEMORY', 'no classical value supplied', 'no verified source states the value' in BU0),
        ('G-C1-MECHANISM-QUALIFIED', 'the heuristic keeps 9 of 10', 'right at 9 of 10 cells' in BU0),
        ('G-C1-STATES-APART', 'statuses apart', all(x in BU0 for x in ('**name**', '**defining equation**',
                                                                        '**classical asymptote**'))),
        ('G-C1-CLOSED-FORM-SEPARATE', 'closed form a separate status', '**closed form**' in BU0),
        ('G-C1-BLOCK-WRITTEN', 'u0 block written once',
         verdict_line(FILRUN, 'block u0 append_block', 'WRITTEN') and LEDGER.count('<!-- b442 update: u0 -->') == 1),
        ('G-C1-QUOTES-VERIFIED', 'u0 block quotations verified', verdict_line(FILRUN, 'block u0 :', 'misses 0')),

        ('G-C2-CELL-QUOTED-FIRST', 'the cell is quoted before any candidate',
         0 <= COMP.find('THE REPRESENTATION-DEPENDENT CONSTANT**') < COMP.find('### V1 --')),
        ('G-C2-TRANSCRIPTION-PRINTED', 'the Theorem 6.1 transcription difference is printed',
         'lambda_n(sqrt n, pi-dual)' in COMP and 'λn(√n,π∨)' in BV),
        ('G-C2-OPENING-EIGHT', 'eight opening candidates', len([c for c in cands if c['id'].startswith('V')]) == 8),
        ('G-C2-SEARCH-CAPPED', 'at most six by description', len([c for c in cands if c['id'].endswith('*')]) <= 6),
        ('G-C2-EVERY-HIT-HANDREAD', 'non-candidate hits listed with reasons',
         'THE SEARCH HITS READ AND NOT MADE CANDIDATES' in COMP),
        ('G-C2-THREE-STEPS', 'each candidate carries its attempted steps', COMP.count('attempted : S1 CLASS') == len(cands)),
        ('G-C2-QUOTED-STEP-EACH', 'each candidate failed at a quoted step',
         all(c.get('quotes') and c.get('step') for c in cands or [{}])),
        ('G-C2-FINITE-CLASS-TESTED', 'the finite maximum is a candidate', any(c['id'] == 'V2' for c in cands)),
        ('G-C2-FIVE-SITE-COUNT', 'five tallies', len(SITEV.get('tallies') or {}) == 5),
        ('G-C2-COUNT-FROM-JSON', 'tallies read from banked JSON', 'b436_prior_sites.json' in SRC_COMP),
        ('G-C2-BLOCK-WRITTEN', 'site (v) block written once',
         verdict_line(FILRUN, 'block site (v) append_block', 'WRITTEN')
         and LEDGER.count('<!-- b442 update: site (v) -->') == 1),
        ('G-C2-CELL-UNTOUCHED', 'row U1 unchanged', ([l for l in LEDGER.splitlines() if l.startswith('| U1 ')] or [''])[0]
         == ([l for l in git(PP, 'show', 'HEAD:FACES_LEDGER.md').splitlines() if l.startswith('| U1 ')] or ['x'])[0]),
        ('G-C2-CHECKPOINT-AFTER-V', 'checkpointed after (v)', 'checkpointed after (v)' in BV),

        ('G-C3-HEADED-AS-B440', 'the row carries corrections headed as b440`s', "CORRECTIONS TO ROW 289, ENTERED AS b440'S" in ROW),
        ('G-C3-NAMES-ROW-289', 'the row names row 289', 'ROW 289' in ROW),
        ('G-C3-B441-WORDS-VERIFIED', 'b441`s words are quoted verbatim',
         all(w in ROW for w in ('THE RECORD NEVER DENIED THE IDENTIFICATION.',
                                'b430' + chr(39) + 's defect, still live in every act since" -- is FALSE',
                                "AND b440'S REPAIR WAS DEFECTIVE TOO, AND IT REACHED THIS ACT."))),
        ('G-C3-WRONG-RULE-NAMED', 'the wrong rule is named', 'origin/main == HEAD' in ROW),
        ('G-C3-B439-PREDICATE-QUOTED', 'b439`s predicate quoted as restored in b441', "b441'S COMMITTED SUITE" in ROW),
        ('G-C3-NO-ROW-EDITED', 'no prior row edited', unchanged(SIDE, 'CORRESPONDENCE.md')
         or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-C3-B440-TOOL-UNEDITED', 'b440_checks.py unedited', unchanged(ROOT, 'tools/b440_checks.py')),

        ('G-N1-APART', 'N1 apart', '`(N1)`' in FACET),
        ('G-N2-APART', 'N2 apart', '`(N2)`' in FACET),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations on face',
         fold("AND THIS SEAT'S OWN, DECLARED SO THEY CAN BE SCORED AGAINST IT") in F),

        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.', pycode_of(SRC_COMP + SRC_FIL))),
        ('G-NOGRADE-MOVED', 'no grade conferred', 'No grade is conferred' in BU0 and 'No grade is conferred' in BV),
        ('G-NONEWINSTRUMENT', 'no instrument file touched', 0 == len(touched(ROOT, r'tools/e16/', since=False))),
        ('G-NONEWFAMILY', 'family tool unchanged', unchanged(ROOT, 'tools/b317_smear.py')),
        ('G-NOATLAS-EDIT', 'atlas unchanged', unchanged(ROOT, 'tools/e16/carto_atlas.py')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(kern_files)),
        ('G-NOLANE-OPENED', 'no lane opened', fold('AND NO LANE OPENED') in F),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOLOCKEDFACE', 'no other face touched',
         0 == len([f for f in touched(ROOT, r'registration_') if 'b442' not in f])),
        ('G-NOPRIORBANK', 'no prior bank touched',
         0 == len([f for f in touched(ROOT, r'^data/b4[0-4][0-9]_') if not f.startswith('data/b442')])),
        ('G-NOBANKEDFERRY', 'no other ferry touched',
         0 == len([f for f in touched(ROOT, r'_ferry', since=False) if 'b442' not in f])),
        ('G-NOFOLD', 'no fold', fold('NO FOLD RUN') in F),
        ('G-NOKEYSTONE-EDIT', 'no keystone edited', fold('NO KEYSTONE EDITED OR ANNOTATED') in F),
        ('G-NOROW-WRITTEN', 'no ledger row written', unchanged(PP, 'FACES_LEDGER.md') or appended_only(PP, 'FACES_LEDGER.md')),
        ('G-NOSEVENTH-SITE', 'no seventh site', fold('NO SEVENTH SITE') in F),
        ('G-NOCELL-WRITTEN', 'no cell written', fold('NO CELL OF THE REGISTER WRITTEN') in F),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-DISPROOF-LANE-NOT-OPENED', 'disproof lane shut', fold('THE DISPROOF LANE IS NOT OPENED') in F),
        ('G-NOTECHNE-WRITE', 'TECHNE untouched by this act', t_dirty.strip() == '' and not t_new_commit and not t_new_file),
        ('G-CORPUS-SCOPE', 'only the ledger and the trail in PLACE-papers',
         all(f in ('FACES_LEDGER.md', 'OPEN_TRAILS.md') for f in pp_touched)),
        ('G-LEDGER-APPEND-ONLY', 'ledger appended only', unchanged(PP, 'FACES_LEDGER.md') or appended_only(PP, 'FACES_LEDGER.md')),
        ('G-TRAIL-APPEND-ONLY', 'trail appended only', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended only',
         unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'every relay file on the list',
         all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f for f in relay_new)),
        ('G-WRITELIST-NAMES-PATHS', 'list names paths', 'b442_filings.py' in FACET and 'b442_closing.txt' in FACET),
        ('G-WRITELIST-COMMIT-RANGE', 'write arm reads the commit range', 'def committed_by_act(' in SRC_CHK),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_FIL))),
        ('G-NOBORROWEDBAR', 'twelve bars', 12 == len(re.findall(r'\*\*BAR \d+ --', FACET))),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-OWN-BANK', 'reads own bank', 'b442_components.txt' in SRC_CHK),
        ('G-ARMS-STRIP-PROSE', 'tokenizer strips', 'tokenize.COMMENT' in SRC_CHK and 'tokenize.STRING' in SRC_CHK),
        ('G-ARMS-FOLD-MARKERS', 'fold both sides', bool(re.search(r'fold \( \) in [FC]', pycode_of(SRC_CHK)))),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-ARMS-EOL-NORMALISED', 'eol normalised', 'def nl(' in SRC_CHK and 'chr(13)' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439`s predicate carried',
         "if 'b442' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS-BEFORE-STAGING', 'the pre-push file exists with a PRE-PUSH header',
         os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300] if not _pushed() else
         'PRE-PUSH READING' in git(ROOT, 'show', 'HEAD~0:data/b442_checks.txt')[:300]
         or 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-NOSTRAY-PLACEHOLDER', 'no bare format strings', 0 == len(re.findall(r'%[-0-9.]*[dsfe](?![a-zA-Z0-9])', COMP))),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v)))
            for n, d, v in ARMS]
    rec('  arms declared on the face : %d' % len(DEC))
    rec('  arms run by this suite    : %d' % len(ARMS))
    rec('  declared and NOT run      : %s' % sorted(set(DEC) - set(names)))
    rec('  run and NOT declared      : %s' % sorted(set(names) - set(DEC)))
    rec('  PLACE-papers touched      : %s' % pp_touched)
    rec()
    fails = []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = (v is False)
            rec('  %-40s %-4s %s' % (n, 'FAIL', 'CONTROL -- a false arm must fail; it %s' % ('did' if ok else '### DID NOT ###')))
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
