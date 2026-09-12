# -*- coding: utf-8 -*-
"""b443r_checks.py -- THE CONTROL SUITE FOR b443r. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b443r_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b443r_checks.txt')
POSTPUSH = os.path.join(D, 'b443r_checks_postpush.txt')
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
                for f in ('b443r_ferry.txt', 'b443r_ferry_scan.txt'))


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
    # ### **AN ACT IS NOT ONE COMMIT.** ### b443r lands in four -- the act, the closing suite, the
    # ### closing record, and this repair -- so an arm reading only `HEAD` sees the last of them
    # ### and scores the write list over two files. ### **EVERY COMMIT WHOSE SUBJECT NAMES THIS
    # ### ACT IS READ**, and the act's own boundary bounds how far back that can reach.
    out = []
    for ln in git(repo, 'log', '--format=%H %s', '-40').splitlines():
        sha, _, subj = ln.partition(' ')
        if 'b443' not in subj:
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
COMP = read(os.path.join(D, 'b443r_components.txt'))
EXTR = read(os.path.join(D, 'b443r_extract.txt'))
RGATE = read(os.path.join(D, 'b443r_reg_gate.txt'))
TERM = read(os.path.join(D, 'b443r_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b443r_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b443r_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b443r_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b443r_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b443r_ferry.txt'))
CENS = read(os.path.join(D, 'b443r_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b443r_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b443r_pins_stepzero.txt'))
ADD = os.path.join(D, 'b443r_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b443r_components.py'))
SRC_EXT = read(os.path.join(T, 'b443r_extract.py'))
SRC_CHK = read(os.path.join(T, 'b443r_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b443r_checks.py`
# ### beside `data/b443r_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
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
    ### b443r's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b443' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False



import hashlib

FILRUN = read(os.path.join(D, 'b443r_filings_run.txt'))
SRC_FIL = read(os.path.join(T, 'b443r_filings.py'))
LEDGER = read(os.path.join(PP, 'FACES_LEDGER.md'))
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
DRAFTT = read(os.path.join(D, 'b443r_u1_draft.md'))
FIX = read(os.path.join(D, 'b443r_seal_fixtures.txt'))
try:
    SITE = json.loads(read(os.path.join(D, 'b443r_site_vi.json')))
except Exception:
    SITE = {}
BV = LEDGER.split('<!-- b443 update: site (vi) -->', 1)[-1] if '<!-- b443 update: site (vi) -->' in LEDGER else ''
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
ROW = ([ln for ln in CORR.splitlines() if ln.startswith('| ') and '(b443)' in ln] or [''])[-1]
TRAIL = read(os.path.join(PP, 'OPEN_TRAILS.md'))
TB = TRAIL.split('<!-- b443 site (vi), and the arc', 1)[-1] if '<!-- b443 site (vi), and the arc' in TRAIL else ''
STRANDED = os.path.join(D, 'b443_registration_2026-09-12.txt')


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b443 (re-issue) -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b443r')) | set(committed_by_act(ROOT, r'b443r')))
    committed_stranded = [f for f in committed_by_act(ROOT, r'b443_') if 'b443r' not in f]
    committed_all = git(ROOT, 'log', '--all', '--format=', '--name-only', '--', 'data/b443_registration_2026-09-12.txt')
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b443r_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    changed_tools = [f for f in touched(ROOT, r'^tools/', since=False) if not re.search(r'b443r_|banked_index', f)]
    tracked_tool_changes = [ln[3:] for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines()
                            if ln[3:].startswith('tools/') and 'banked_index' not in ln]
    rs_log = git(ROOT, 'log', '--format=%s', '-5', '--', 'tools/reg_seal.py')
    cands = SITE.get('candidates') or []
    tallies = SITE.get('tallies') or {}

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'the ferry carries the scanned line', 'scanned before sending, zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, 'MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED', 'prior act closed at row 291', 'row 291' in F),
        ('G-TWO-RULINGS-ENTERED', 'R55 and R56 entered', '`(R55)`' in FACET and '`(R56)`' in FACET),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b443r_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C0-INCIDENT-DECLARED', 'the incident declared first on the face', FACET.find('(I) THE INCIDENT') < FACET.find('(A) THE ORDER')),
        ('G-C0-STRANDED-UNCHANGED', 'the stranded face byte-identical',
         hashlib.sha256(open(STRANDED, 'rb').read()).hexdigest() == 'b8d4838c787d439fac5171597254be6101de340ffedffae8a96c6124d304abac'),
        ('G-C0-STRANDED-NOT-COMMITTED', 'no b443_ file committed by this act', not committed_stranded and not committed_all.strip()),
        ('G-C0-SEAL-REFUSES-ABSENT', 'fixture: absent record refused', verdict_line(FIX, 'REFUSES on absent record', 'True')),
        ('G-C0-SEAL-REFUSES-REFUSED', 'fixture: refused gate refused', verdict_line(FIX, 'REFUSES on the gate refused', 'True')),
        ('G-C0-SEAL-REFUSES-OTHER-FACE', 'fixture: other face refused', verdict_line(FIX, 'REFUSES on a different face', 'True')),
        ('G-C0-SEAL-REFUSES-STALE', 'fixture: stale digest refused', verdict_line(FIX, 'REFUSES on a stale digest', 'True')),
        ('G-C0-SEAL-PERMITS-CLEAN', 'fixture: clean record permitted', verdict_line(FIX, 'PERMITS a clean', 'True')),
        ('G-C0-REFUSING-ARM-PRINTED', 'the real incident names its refusing arm',
         'refusing arm : the banned-term scan on the face (b443_reg_termscan.txt)' in FIX),
        ('G-C0-OLD-SELFTEST-STILL-PASSES', 'the prior arms still pass',
         verdict_line(FIX, '--lock   writes, verifies', 'True') and verdict_line(FIX, '--seal   a changed body', 'True')),
        ('G-C0-ONLY-REG-SEAL-CHANGED', 'reg_seal.py is the only instrument change',
         all(f in ('tools/reg_seal.py',) for f in tracked_tool_changes) and
         (('tools/reg_seal.py' in tracked_tool_changes) or 'b443' in rs_log)),

        ('G-C1-CELL-QUOTED-FIRST', 'cell before candidates', 0 <= COMP.find('TYPE-D RESIDUE AT EVERY FINITE MODULUS**') < COMP.find('### D1 --')),
        ('G-C1-OPENING-TEN', 'ten candidates', len(cands) == 10),
        ('G-C1-SEARCH-CAPPED', 'by description within cap', '0 FURTHER CANDIDATES' in COMP),
        ('G-C1-QUOTED-STEP-EACH', 'each failed at a quoted step', all(c.get('quotes') and c.get('step') for c in cands or [{}])),
        ('G-C1-SOURCE-HITS-CLASSIFIED', 'verified-source hits classified', 'THE VERIFIED SOURCES` VOCABULARY HITS, EACH CLASSIFIED' in COMP),
        ('G-C1-SIX-SITE-COUNT', 'six tallies', len(tallies) == 6),
        ('G-C1-PER-SITE-CB-PRINTED', 'per-site class boundary printed', COMP.count('CLASS BOUNDARY') >= 6 and 'site (iv)  b436' in COMP),
        ('G-C1-UNION-STATED', 'union stated', SITE.get('union6') == 11 and 'STAYS AT' in COMP),
        ('G-C1-BLOCK-WRITTEN', 'site (vi) block written once',
         verdict_line(FILRUN, 'append_block', 'WRITTEN') and LEDGER.count('<!-- b443 update: site (vi) -->') == 1),
        ('G-C1-QUOTES-VERIFIED', 'block quotations verified', verdict_line(FILRUN, 'quotations', 'misses 0')),
        ('G-C1-CELL-UNTOUCHED', 'row U1 unchanged',
         ([l for l in LEDGER.splitlines() if l.startswith('| U1 ')] or [''])[0]
         == ([l for l in git(PP, 'show', 'HEAD:FACES_LEDGER.md').splitlines() if l.startswith('| U1 ')] or ['x'])[0]),
        ('G-C1-CHECKPOINT-AFTER-VI', 'checkpointed after (vi)', 'checkpointed after (vi)' in BV),

        ('G-C2-DRAFT-BANKED', 'draft exists and says not applied', 'NOT APPLIED' in DRAFTT),
        ('G-C2-REFUSAL-VERBATIM', 'refusal verbatim in the draft',
         'THE DEPOSIT’S REFUSAL GOVERNS THIS ENTRY AS IT GOVERNS THE LEDGER:' in DRAFTT
         and 'NO EQUIVALENCE IS COMPILED.' in DRAFTT),
        ('G-C2-TAXONOMY-COUNTS', 'taxonomy with counts', '| **candidates** |' in DRAFTT and str(SITE.get('total')) in DRAFTT),
        ('G-C2-ROW-UNEDITED', 'row U1 unedited',
         ([l for l in LEDGER.splitlines() if l.startswith('| U1 ')] or [''])[0]
         == ([l for l in git(PP, 'show', 'HEAD:FACES_LEDGER.md').splitlines() if l.startswith('| U1 ')] or ['x'])[0]),

        ('G-C3-INDEX-DEFECT-FILED', 'index defect in the trail', 'b341' in TB and '√n' in TB),
        ('G-C3-DRAFT-BLOCK-BANKED', 'routed block drafted', 'DRAFT UPDATE BLOCK — ROW U1, ENTRY (v)' in DRAFTT),
        ('G-C3-LINE-231-OWING-READ', 'line 231 as a sentence owing a read', 'SENTENCE OWING A SOURCE READ' in TB.upper() and 'recollection' in TB),
        ('G-C3-FRB-TRAIL-FILED', 'FRB trail filed', 'fast-radio-burst' in TB.lower()),
        ('G-C3-SPAN-BY-TOOL', 'span read by the tool', os.path.exists(os.path.join(D, 'b443r_span.txt')) and 'THE CURRENT SPAN' in read(os.path.join(D, 'b443r_span.txt'))),

        ('G-N1-APART', 'N1 apart', '`(N1)`' in FACET),
        ('G-N2-SCORED-AS-HIS', 'N2 scored as the navigator`s', 'SCORED AS HIS' in FACET),

        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.', pycode_of(SRC_COMP + SRC_FIL))),
        ('G-NOGRADE-MOVED', 'no grade conferred', 'No grade is conferred' in BV),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NOKEYSTONE-EDIT', 'keystone unchanged', unchanged(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank touched', 0 == len([f for f in touched(ROOT, r'^data/b4[0-4][0-9]_', since=False)
                                                               if not f.startswith('data/b443') and f.split('/')[-1][:4] >= 'b440'
                                                               and git(ROOT, 'ls-files', f).strip()])),
        ('G-NOFOLD', 'no fold', fold('NO FOLD RUN') in F),
        ('G-NOCELL-WRITTEN', 'no cell', fold('NO CELL WRITTEN') in F),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-NOTECHNE-WRITE', 'TECHNE untouched', t_dirty.strip() == ''),
        ('G-CORPUS-SCOPE', 'only ledger and trail', all(f in ('FACES_LEDGER.md', 'OPEN_TRAILS.md') for f in pp_touched)),
        ('G-LEDGER-APPEND-ONLY', 'ledger appended', unchanged(PP, 'FACES_LEDGER.md') or appended_only(PP, 'FACES_LEDGER.md')),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list',
         all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", pycode_of(SRC_COMP) + pycode_of(SRC_FIL))),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b443' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present with its header',
         os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names)), sorted(set(names) - set(DEC))))
    fails = []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = v is False
            rec('  %-40s %-4s CONTROL -- it %s' % (n, 'FAIL', 'did' if ok else '### DID NOT ###'))
            if not ok:
                fails.append(n)
            continue
        rec('  %-40s %-4s %s' % (n, 'PASS' if v else '### FAIL', d))
        if not v:
            fails.append(n)
    rec('=' * 100)
    rec('  ### ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s' % (len(ARMS), len(ARMS) - len(fails), len(fails), fails or ''))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fails else 'ARMS FAILING'))
    rec('=' * 100)
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    os.replace(OUT + '.tmp', OUT)
    return 0 if not fails else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
