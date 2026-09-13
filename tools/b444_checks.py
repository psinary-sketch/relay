# -*- coding: utf-8 -*-
"""b444_checks.py -- THE CONTROL SUITE FOR b444. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b444_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b444_checks.txt')
POSTPUSH = os.path.join(D, 'b444_checks_postpush.txt')
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
                for f in ('b444_ferry.txt', 'b444_ferry_scan.txt'))


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
        if 'b444' not in subj:
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
COMP = read(os.path.join(D, 'b444_components.txt'))
EXTR = read(os.path.join(D, 'b444_extract.txt'))
RGATE = read(os.path.join(D, 'b444_reg_gate.txt'))
TERM = read(os.path.join(D, 'b444_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b444_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b444_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b444_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b444_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b444_ferry.txt'))
CENS = read(os.path.join(D, 'b444_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b444_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b444_pins_stepzero.txt'))
ADD = os.path.join(D, 'b444_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b444_components.py'))
SRC_EXT = read(os.path.join(T, 'b444_extract.py'))
SRC_CHK = read(os.path.join(T, 'b444_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b444_checks.py`
# ### beside `data/b444_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
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
    ### b444's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b444' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False



FOLDRUN = read(os.path.join(D, 'b444_fold_run.txt'))
SRC_FOLD = read(os.path.join(T, 'b444_fold.py'))
FND = read(os.path.join(PP, 'FINDINGS.md'))
DIG = read(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md'))
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
try:
    FJ = json.loads(read(os.path.join(D, 'b444_fold.json')))
    CJ = json.loads(read(os.path.join(D, 'b444_decorrelation.json')))
except Exception:
    FJ, CJ = {}, {}
SEC = FND.split('<!-- b444 the fold: b433-b443', 1)[-1] if '<!-- b444 the fold: b433-b443' in FND else ''
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
ROW = ([ln for ln in CORR.splitlines() if ln.startswith('| ') and '(b444)' in ln] or [''])[-1]


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b444 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b444')) | set(committed_by_act(ROOT, r'b444')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b444_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    tracked_tools = [ln[3:] for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines()
                     if ln[3:].startswith('tools/') and 'banked_index' not in ln]
    rows = FJ.get('rows') or []
    CODE = pycode_of(SRC_COMP + SRC_FOLD)

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned before sending, zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, 'MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED', 'prior act closed at row 292', 'row 292' in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b444_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-LANES-PARKED', 'lanes parked', 'both instrument lanes' in F),

        ('G-C1-THREE-SPAN-FIGURES', 'tool, rule and order figures', (FJ.get('span') or {}).get('rule') == 9
         and (FJ.get('span') or {}).get('order') == 11 and (FJ.get('span') or {}).get('tool') is not None),
        ('G-C1-B443-CORRECTED', 'b443`s sentence corrected in the fold', 'b443’s closing called eleven the record’s convention; that was wrong' in SEC),
        ('G-C1-HEADING-TOOL-READABLE', 'the new heading matches the tool`s pattern and it reads b444',
         bool(re.search(r'^## THE WITNESS AND CHANNEL ARC, b433–b443 — THE FOLD\s*$', FND, re.M)) and 'Filed by b444' in SEC),
        ('G-C1-STRINGS-VERIFIED', 'every verdict string verified', FJ.get('verified') == len(rows) == 11
         and all(r['verdict'] in read(os.path.join(D, r['bank'])) for r in rows)),
        ('G-C1-ELEVEN-ROWS', 'eleven rows in the section', sum(1 for ln in SEC.splitlines() if re.match(r'^\| \*\*b4[34]\d\*\* \|', ln)) == 11),
        ('G-C1-B434-AS-FILER', 'b434 marked the prior filer', 'THE PRIOR FOLD`S FILING ACT' in SEC),
        ('G-C1-PRIOR-CLAUSES-CITED', 'prior-fold clauses cited, not folded', 'Folded at b434 and cited, not folded again' in SEC),
        ('G-C1-COLUMNS-APART', 'three columns with counts', '**Statements about the object**' in SEC and '**About the model**' in SEC),
        ('G-C1-ONE-STATEMENT', 'one statement present', '### The arc in one statement' in SEC and FJ.get('one', 'x')[:40] in SEC),
        ('G-C1-WORK-ORDER-FILED', 'span work-order filed with trigger', 'W-ORD-SPAN-HEADING' in SEC and '**Trigger:**' in SEC),
        ('G-C1-DIGEST-REFRESHED', 'digest block written once', DIG.count('<!-- b444 orientation refresh') == 1 and 'NOT LOCATED' not in DIG.split('<!-- b444 orientation refresh')[-1]),
        ('G-C1-FINDINGS-APPEND-ONLY', 'FINDINGS appended only', unchanged(PP, 'FINDINGS.md') or appended_only(PP, 'FINDINGS.md')),

        ('G-C2-TABLE-22', 'twenty-two cells', CJ.get('cells') == 22),
        ('G-C2-ZERO-INHERITED-SAID', 'zero side said inherited', 'THE ZERO CHANNEL IS INHERITED' in COMP),
        ('G-C2-AIM-MAP-APART', 'aim map kept apart', 'KEPT APART' in COMP),
        ('G-C2-T1-PRINTED', 'T1 printed', 'T1 -- THE CORRELATION STRUCTURE' in COMP and bool(CJ.get('t1'))),
        ('G-C2-T2-MATCHES-BANK', 'T2 matches the bank', CJ.get('dev', 1) <= 1e-15),
        ('G-C2-T3-PRINTED', 'T3 printed', 'T3 -- WHAT THE RESIDUAL CARRIES' in COMP and bool(CJ.get('t3'))),
        ('G-C2-BAR-FROM-B437', 'bar is b437`s floor', CJ.get('floor') == 1.49e-08 and '`1.49e-08`' in FACET),
        ('G-C2-VERDICT-BY-RULE', 'verdict follows the fixed rule',
         CJ.get('verdict') == ('STRUCTURE' if any(abs(x[1]) > 1.49e-08 for x in CJ.get('e', [])) else 'NOTHING ABOVE THE FLOOR')),
        ('G-C2-NO-ZERO-CLAIM', 'no zero claim', 'NO CLAIM ABOUT ZEROS IS MADE' in COMP),
        ('G-C2-NO-CELL-COMPUTED', 'no instrument imported or run by the components',
         not re.search(r'import (carto_atlas|b321_window|b317_smear)|mpmath|np\.trapezoid', CODE)),

        ('G-N1-APART', 'N1 apart', '`(N1)`' in FACET),
        ('G-N2-SCORED', 'N2 scorable', CJ.get('verdict') in ('STRUCTURE', 'NOTHING ABOVE THE FLOOR', 'NOT APPLICABLE')),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations on face', fold("AND THIS SEAT'S OWN:") in F),

        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.', CODE)),
        ('G-NOGRADE-MOVED', 'no grade conferred', 'no grade is conferred by a seat' in SEC),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NOINSTRUMENT-WRITE', 'no tracked tool changed', tracked_tools == []),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b444' not in ln])),
        ('G-NOCELL-WRITTEN', 'FACES_LEDGER untouched', unchanged(PP, 'FACES_LEDGER.md')),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-NOTECHNE-WRITE', 'TECHNE untouched', t_dirty.strip() == ''),
        ('G-CORPUS-SCOPE', 'only FINDINGS, the digest and the trail',
         all(f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md') for f in pp_touched)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-DIGEST-APPEND-ONLY', 'digest appended', unchanged(PP, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md')
         or appended_only(PP, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b444' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
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
            rec('  %-40s FAIL CONTROL -- it %s' % (n, 'did' if ok else '### DID NOT ###'))
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
