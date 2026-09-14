# -*- coding: utf-8 -*-
"""b457_checks.py -- THE CONTROL SUITE FOR b457. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b457_registration_2026-09-14.txt')
PREPUSH = os.path.join(D, 'b457_checks.txt')
POSTPUSH = os.path.join(D, 'b457_checks_postpush.txt')
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
                for f in ('b457_ferry.txt', 'b457_ferry_scan.txt'))


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
    # ### **AN ACT IS NOT ONE COMMIT.** ### b444 lands in four -- the act, the closing suite, the
    # ### closing record, and this repair -- so an arm reading only `HEAD` sees the last of them
    # ### and scores the write list over two files. ### **EVERY COMMIT WHOSE SUBJECT NAMES THIS
    # ### ACT IS READ**, and the act's own boundary bounds how far back that can reach.
    out = []
    for ln in git(repo, 'log', '--format=%H %s', '-40').splitlines():
        sha, _, subj = ln.partition(' ')
        if 'b457' not in subj:
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
COMP = read(os.path.join(D, 'b457_components.txt'))
EXTR = read(os.path.join(D, 'b457_extract.txt'))
RGATE = read(os.path.join(D, 'b457_reg_gate.txt'))
TERM = read(os.path.join(D, 'b457_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b457_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b457_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b457_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b457_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b457_ferry.txt'))
CENS = read(os.path.join(D, 'b457_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b457_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b457_pins_stepzero.txt'))
ADD = os.path.join(D, 'b457_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b457_components.py'))
SRC_DESK = read(os.path.join(T, 'b457_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b457_extract.py'))
SRC_CHK = read(os.path.join(T, 'b457_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b444_checks.py`
# ### beside `data/b444_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
# ### every prefixed entry and charges a declared file as undeclared. ### **BOTH SIDES ARE REDUCED
# ### TO A BASENAME BEFORE THEY ARE COMPARED.**
WRITELIST = [os.path.basename(x) for x in
             re.findall(r'`([A-Za-z0-9_.\-/]+\.(?:py|txt|json|md|lean|npy))`',
                        FACET.split('(W) THE WRITE LIST')[-1].split('(Z) THE NOTHINGS')[0])]
DEC = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', FACET)) - {'G-NO'})


def _pushed():
    """### HAS **THIS ACT'S** WORK REACHED THE REMOTE? ### **CARRIED FROM b439, NOT RETYPED.**

    ### b440 retyped this predicate twice and got it wrong twice. ### Its first writing sought a SHA
    ### in a list of branch NAMES and was never true. ### Its "repair" -- `origin/main == HEAD` -- is
    ### **TRUE BEFORE THIS ACT COMMITS ANYTHING**, because HEAD is then the prior act's pushed commit;
    ### b444's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b457' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False

















def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


RJ = _j('b457_run.json')
CJ = _j('b457_cells.json')
PJ = _j('b457_gate_price.json')
SPAN = _j('b457_span.json')
MIRROR = read(os.path.join(D, 'b457_mirror.txt'))
RUNTXT = read(os.path.join(D, 'b457_profile_run.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b457_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
COMMIT = '0e5233f011533d09e4799107394c216a915028a1'
TAGOBJ = '922c0fc789d0b530447df12da8967fc8bccb0eb0'
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b457 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b457|banked_index')) | set(committed_by_act(ROOT, r'.')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b457_registration_2026-09-14.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'a7b5ec9', 'origin/main'], capture_output=True).returncode

    def base_text(rel):
        if not unchanged(PP, rel):
            return nl(git(PP, 'show', 'HEAD:%s' % rel))
        for ln in git(PP, 'log', '--format=%H %s', '-10', '--', rel).splitlines():
            if 'b457' in ln:
                return nl(git(PP, 'show', '%s^:%s' % (ln.split(' ', 1)[0], rel)))
        return nl(read(os.path.join(PP, *rel.split('/'))))

    res, res0 = nl(read(os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'))), base_text('phase1.5/proofs/THE_RESIDUE_OF_RH.md')
    rd, rd0 = nl(read(os.path.join(PP, 'README.md'))), base_text('README.md')
    out = (RJ.get('print') or {}).get('stdout', '')
    vv = RJ.get('verdicts') or []

    def verdict_ok():
        for x in vv:
            m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(x['terminal']), out)
            if m:
                want = 'STANDARD THREE' if set(a.strip() for a in m.group(1).split(',')) == STD3 else 'OTHER'
            elif re.search(r"'%s' does not depend on any axioms" % re.escape(x['terminal']), out):
                want = 'OTHER'
            else:
                want = 'NOT PRINTED'
            if want != x['verdict']:
                return False
        return len(vv) == 3

    lock_t = os.path.getmtime(FACE)
    PRIORFILE = r"b4(?!57)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump_json\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'"
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|RUNJ|RUNTXT|BUILDLOG|CELLSJ|PRICEJ|SPEC)\s*="
    carried = [(n, ln.strip()[:80]) for n, s in SRC_ALL.items() for ln in s.splitlines() if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln)]
    fixture = "    dump_json(os.path.join(D, '" + 'b45' + "6_writes.json'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))
    onlist = lambda f: os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
    off_exact = [f for f in relay_new if not onlist(f)]
    kern_clean = all(0 == len(git(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').splitlines())
                     for k in ('SIDE-kernel', 'SIDE-effects', 'SIDE-lv-conservation', 'SIDE-window'))
    pp_allowed = {'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'README.md', 'OPEN_TRAILS.md'}

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-14-b457.zip' in MIRROR
                and verdict_line(MIRROR, 'manifest declares source HEAD', git(PP, 'rev-parse', '--short=7', 'HEAD').strip()))

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned' in FERRY and 'zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, '### MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED-PUSHED', 'row 305 on the face; a7b5ec9 on origin/main', 'row 305' in FACET and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b457_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-LOCKGATE-NOT-REDIRECTED', 'one lock-gate record', not any(re.match(r'b457_lockgate_notes\d+\.txt$', f) for f in os.listdir(D))),
        ('G-RULINGS-ENTERED', 'the three rulings in the ferry, on the face and in the record', all(('(R6%d)' % k) in FERRY and ('(R6%d)' % k) in FACET for k in (6, 7, 8)) and 'RULINGS (R66), (R67), (R68)' in COMP),
        ('G-C1-CLONE-AT-HASH', 'the clone`s HEAD is the tag`s commit', RJ.get('clone_head') == COMMIT and COMMIT in RUNTXT),
        ('G-C1-TAG-OBJECT', 'the clone`s tag object', RJ.get('clone_tag_object') == TAGOBJ and TAGOBJ in RUNTXT),
        ('G-C1-CLEAN-BEFORE', 'clean before anything was added', RJ.get('clean_ok') is True and (RJ.get('clean_before') or '').strip() == ''),
        ('G-C1-PACKAGES-AT-MANIFEST', 'every package at its manifest revision', RJ.get('packages_ok') is True and all(x['match'] for x in RJ.get('packages') or [{'match': False}])),
        ('G-C1-NO-KERNEL-BUILD-COPIED', 'the kernel`s own build not copied', RJ.get('kernel_build_copied') is False),
        ('G-C1-RUN-AFTER-LOCK', 'the run started after the face was sealed', bool(RJ.get('started')) and __import__('datetime').datetime.fromisoformat(RJ['started']).timestamp() > os.path.getmtime(os.path.join(D, 'b457_lockgate.json'))),
        ('G-C1-BANKED-HEADER', 'digest, commit, toolchain, durations in the banked file -- the first predicate`s needle `v4.29.0-rc8` yields %d (lean prints the version without the `v`); the corrected `version 4.29.0-rc8` yields %d'
         % (RUNTXT.count('v4.29.0-rc8'), RUNTXT.count('version 4.29.0-rc8')), all(k in RUNTXT for k in (TAGOBJ, COMMIT, 'toolchain :', 'lake :', 'duration')) and 'version 4.29.0-rc8' in RUNTXT),
        ('G-C1-OUTPUT-VERBATIM', 'the print`s stdout in the banked file byte for byte', bool(out) and out.rstrip(NL) in RUNTXT),
        ('G-C1-VERDICT-FROM-OUTPUT', 'each verdict re-derived from its output line', verdict_ok() and 'never a verdict' in COMP),
        ('G-C1-NO-MATHLIB-REBUILD', 'the log`s Mathlib and remote lines printed', 'Mathlib modules compiled' in COMP and 'remote-contact lines' in COMP and RJ.get('remote_lines') == []),
        ('G-C1-NOTE-OR-TRIGGER', 'the note iff all standard, else the trigger and no note', (RJ.get('all_standard') and RJ.get('banked_ok') and rd.split(NL).count(RJ.get('note') or '@@') == 1 and 'THE SECOND MATTER CLOSES' in COMP)
         or ((not RJ.get('all_standard')) and 'WAVE TRIGGER' in COMP and rd == rd0)),
        ('G-C1-LANE-CLOSED', 'the scratch tree removed and verified absent', RJ.get('scratch_removed') is True and not os.path.exists(os.path.join('D:', os.sep, 'b457-tag-run'))),
        ('G-C1-KERNEL-UNMOVED', 'D:\\SIDE-kernel HEAD, refs, tracked status unmoved', RJ.get('kernel_unmoved') is True and git(KER, 'rev-parse', 'HEAD').strip() == (RJ.get('kernel_before') or {}).get('head')),
        ('G-C2-CELLS-BY-TERM', ':127-130 carry MERGED-BRANCH, each once', all(res.split(NL)[k].count('### **MERGED-BRANCH**') == 1 for k in range(126, 130)) and all(res.split(NL)[126 + i] == x['original'].replace('### **HELD-BRANCH**', '### **MERGED-BRANCH**') for i, x in enumerate(CJ.get('lines') or []))),
        ('G-C2-ORIGINALS-PRESERVED', 'the four lines as they stood in the b457 annotation', len(CJ.get('lines') or []) == 4 and all(x['original'] in res.split('<!-- b457 CURRENCY ANNOTATION')[-1] for x in CJ['lines'])),
        ('G-C2-LICENSE-UNWRITTEN', 'EXHAUSTIVENESS_LICENSE untouched', unchanged(PP, 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md') and 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md' not in pp_committed),
        ('G-C2-REMOVED-ZERO', 'removed zero', CJ.get('removed_zero') is True),
        ('G-C3-SURFACES-VERIFIED', 'every counted record file checksum-verified; the svg excluded', all(x['verified'] for x in PJ.get('surfaces') or [{'verified': False}]) and any(x.get('excluded') for x in PJ.get('surfaces') or [])),
        ('G-C3-YIELDS-PRINTED', 'naming, counted and out-of-reach yields', all(k in COMP for k in ('naming yield', 'out of reach', '| surface | checksum verified | items |'))),
        ('G-C3-PRICE-BY-FORMULA', 'acts re-derived from S, U, P', PJ.get('acts') == max(-(-PJ.get('S', 0) // 20), -(-PJ.get('U', 0) // 2), -(-PJ.get('P', 0) // 12)) and ('THE PRICE: ACTS =' in COMP)),
        ('G-C3-NOT-CAUGHT-STATED', 'what it would not catch', 'WHAT IT WOULD NOT CATCH' in COMP),
        ('G-C3-NOTHING-GRADED', 'no grade in the price record', 'NOTHING WAS GRADED; THE GATE IS NOT BUILT.' in COMP and not re.search(r'\b(DERIVES|INTERFACES|NOT THE CLAIM)\b', json.dumps(PJ))),
        ('G-N1-SCORED', 'N1', '(N1) every route terminal reports the standard three' in COMP),
        ('G-N2-SCORED', 'N2 on S and on the price', '(N2) fewer than forty terminal-naming items' in COMP),
        ('G-SEAT-EXPECTATIONS-SCORED', 'the seat`s own', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'emitted for b457', SPAN.get('emitted_for') == 'b457' and SPAN.get('current_span') == 4),
        ('G-NOGRADE-MOVED', 'no row edited', fold('NO GRADE MOVED ON ANY ROW') in F and unchanged(PP, 'FACES_LEDGER.md') and unchanged(PP, 'REGISTRY.md')),
        ('G-NOKERNEL-WRITE', 'kernels unwritten', kern_clean),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOZENODO-WRITE', 'no Zenodo client', fold('NOTHING WRITTEN AT ZENODO') in F and not re.search(r'zenodo\.org/api|ZENODO_TOKEN|api/deposit', SRC_COMP + SRC_DESK)),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched: no url client, the clone`s only remote the local kernel', not re.search(r'urlopen|requests\.|urllib', CODE) and 'D:\\SIDE-kernel' in (RJ.get('clone_remotes') or '') and 'http' not in (RJ.get('clone_remotes') or '')),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b457' not in ln and 'b369' not in ln and 'b373' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: RESIDUE, README (conditional), the trail', all(f in pp_allowed for f in pp_touched + pp_committed)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list : off %d %s' % (len(off_exact), off_exact), not off_exact),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b457' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'write-target shape %d %s ; control fires %s' % (len(carried), carried, control), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-14-b457, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names_arms = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names_arms)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names_arms)), sorted(set(names_arms) - set(DEC))))
    fails, deferred = [], []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = v is False
            rec('  %-40s FAIL CONTROL -- it %s' % (n, 'did' if ok else '### DID NOT ###'))
            if not ok:
                fails.append(n)
            continue
        if v == 'DEFERRED':
            deferred.append(n)
            rec('  %-40s DEFERRED TO POST-PUSH -- %s' % (n, d))
            continue
        rec('  %-40s %-4s %s' % (n, 'PASS' if v else '### FAIL', d))
        if not v:
            fails.append(n)
    rec('=' * 100)
    rec('  ### ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s' % (len(ARMS) - len(deferred), len(ARMS) - len(deferred) - len(fails), len(fails), fails or ''))
    rec('  ### DEFERRED TO POST-PUSH, COUNTED APART : %d %s' % (len(deferred), deferred or ''))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fails else 'ARMS FAILING'))
    rec('=' * 100)
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    os.replace(OUT + '.tmp', OUT)
    return 0 if not fails else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
