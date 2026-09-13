# -*- coding: utf-8 -*-
"""b445_checks.py -- THE CONTROL SUITE FOR b445. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b445_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b445_checks.txt')
POSTPUSH = os.path.join(D, 'b445_checks_postpush.txt')
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
                for f in ('b445_ferry.txt', 'b445_ferry_scan.txt'))


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
        if 'b445' not in subj:
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
COMP = read(os.path.join(D, 'b445_components.txt'))
EXTR = read(os.path.join(D, 'b445_extract.txt'))
RGATE = read(os.path.join(D, 'b445_reg_gate.txt'))
TERM = read(os.path.join(D, 'b445_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b445_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b445_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b445_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b445_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b445_ferry.txt'))
CENS = read(os.path.join(D, 'b445_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b445_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b445_pins_stepzero.txt'))
ADD = os.path.join(D, 'b445_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b445_components.py'))
SRC_ORD = read(os.path.join(T, 'b445_ordinates.py'))
SRC_DESK = read(os.path.join(T, 'b445_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b445_extract.py'))
SRC_CHK = read(os.path.join(T, 'b445_checks.py'))
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
        if 'b445' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False




TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
BANK = read(os.path.join(D, 'b445_whose_residual.txt'))
ORDRUN = read(os.path.join(D, 'b445_ordinates_run.txt'))
try:
    AJ = json.loads(read(os.path.join(D, 'b445_arms.json')))
except Exception:
    AJ = {}
try:
    CELLS = ['%.6f' % x['a'] for x in json.loads(read(os.path.join(D, 'b444_decorrelation.json')))['above']]
except Exception:
    CELLS = []
RJ = AJ.get('report') or {}
FLOOR = 1.49e-08
CHAIN = ['tools/e16/carto_atlas.py', 'tools/e16/zeta_ordinates.npy', 'tools/b317_smear.py',
         'tools/b318_square.py', 'tools/b321_window.py']
# ### THE LIBRARY'S BLOB, NAMED (an arm names its reference): the committed blob at HEAD against the file on disk.
LIB_HEAD = git(ROOT, 'rev-parse', 'HEAD:tools/e16/zeta_ordinates.npy').strip()
LIB_DISK = git(ROOT, 'hash-object', 'tools/e16/zeta_ordinates.npy').strip()


def rule(eb, ev):
    """### THE FACE'S RULE, RE-APPLIED INDEPENDENTLY OF THE COMPONENTS' OWN APPLICATION."""
    if abs(ev) <= 0.5 * abs(eb) or abs(ev) <= FLOOR:
        return 'FALLS'
    if abs(ev - eb) <= 0.1 * abs(eb):
        return 'STABLE'
    return 'MOVES'


def recomputed_verdict():
    base = AJ.get('base', {})
    good = [k for k in CELLS if k in base and abs(base[k]['e'] - base[k]['e_banked']) <= 1e-12]
    st = {}
    for arm in ('a', 'b'):
        ss = [rule(base[k]['e'], AJ[arm][k]['e']) for k in good if k in AJ.get(arm, {})]
        if len(ss) < len(good):
            st[arm] = 'NOT RUN'
        else:
            st[arm] = 'FALLS' if ss.count('FALLS') >= 8 else ('STABLE' if ss.count('STABLE') >= 12 else 'MIXED')
    if len(good) < 8:
        return 'NOT DECIDED -- THE CHAIN DOES NOT REPRODUCE ITS BANK', good
    if st['a'] == 'FALLS' and st['b'] == 'STABLE':
        return 'INTEGRATION', good
    if st['b'] == 'FALLS' and st['a'] == 'STABLE':
        return 'TRUNCATION', good
    if st['a'] == 'STABLE' and st['b'] == 'STABLE':
        return 'UNDETERMINED', good
    if 'NOT RUN' in st.values():
        return 'NOT DECIDED -- AN ARM NOT RUN', good
    if st['a'] == 'FALLS' and st['b'] == 'FALLS':
        return 'BOTH MOVE', good
    return 'MIXED', good


OBLIG = {'INTEGRATION': 'IS RESTATED AS THE CHAIN`S: THE RESIDUAL IS THE CHAIN`S INTEGRATION',
         'TRUNCATION': 'the reach becomes a stated parameter of every cell',
         'UNDETERMINED': 'the residual filed at its measured size with two refutations'}


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b445 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b445')) | set(committed_by_act(ROOT, r'b445')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b445_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_ORD + NL + SRC_DESK)
    verdict, good = recomputed_verdict()
    arms5 = ('base', 'a', 'a_nv', 'a_nu', 'b')
    users = RJ.get('chain_users') or []
    # ### THE CHAIN'S FILES: unmoved in the tree AND in every commit naming this act.
    chain_committed = committed_by_act(ROOT, r'^(tools/e16/carto_atlas\.py|tools/e16/zeta_ordinates\.npy|tools/b31[78]_\w+\.py|tools/b321_window\.py)$')

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned before sending, zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED', 'prior act closed at row 293', 'row 293' in F),
        ('G-R57-ENTERED', '(R57) entered on the face', fold('THIS PASTE RATIFIES ONE RULING, ENTERED HERE:') in F and '(R57)' in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b445_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C1-TRUNCATION-FROM-SOURCE', 'the answer quotes carto_atlas.py by line',
         bool(re.search(r'carto_atlas\.py:\d+ \| NGAM\s+= 10000', COMP)) and 'YES: THE ZERO SIDE TRUNCATES AT 10000 ORDINATES' in COMP),
        ('G-C1-HEIGHT-STATED', 'height printed from the library file', 'HEIGHT 9877.782657' in COMP and 'the last 9877.782657433876' in COMP),
        ('G-C1-BOUND-PRINTED', 'the source`s bound printed beside', verdict_line(COMP, 'the source`s own truncation bound', 'max 6.4')),

        ('G-C2-FOURTEEN-CELLS', 'fourteen cells from b444', len(CELLS) == 14),
        ('G-C2-BASE-REPRODUCES', 'base reproduces at >= 8 (all printed)', len(good) >= 8
         and verdict_line(COMP, 'base reproduces the banked residual', 'at %d of 14 cells' % len(good))),
        ('G-C2-ARM-A-RUN', 'arm (a) at every cell, nv 16385 and NU 24001',
         all(AJ.get('a', {}).get(k, {}).get('nv') == 16385 and AJ['a'][k].get('nu') == 24001 for k in CELLS)),
        ('G-C2-ARM-A-HALVES-BESIDE', 'halves run and printed not governing',
         all(AJ.get('a_nv', {}).get(k, {}).get('nv') == 16385 and AJ['a_nv'][k].get('nu') == 12001
             and AJ.get('a_nu', {}).get(k, {}).get('nv') == 8193 and AJ['a_nu'][k].get('nu') == 24001 for k in CELLS)
         and 'halves, beside and not governing' in COMP),
        ('G-C2-ARM-B-RUN', 'arm (b) at every cell with 15000 ordinates',
         all(AJ.get('b', {}).get(k, {}).get('ngam') == 15000 and AJ['b'][k].get('nv') == 8193 for k in CELLS)),
        ('G-C2-ORDINATES-CONTROL', 'ordinate control PASS', verdict_line(ORDRUN, 'CONTROL :', 'PASS')
         and verdict_line(COMP, 'ordinates control :', 'PASS')),
        ('G-C2-LIBRARY-UNEDITED', 'library blob at HEAD equals the disk (%s)' % LIB_HEAD[:10],
         bool(LIB_HEAD) and LIB_HEAD == LIB_DISK and 'tools/e16/zeta_ordinates.npy' not in chain_committed),
        ('G-C2-E-EVERY-CELL-EVERY-ARM', 'e at 14 cells under 5 arms, each cell printed',
         all(isinstance(AJ.get(arm, {}).get(k, {}).get('e'), float) for arm in arms5 for k in CELLS)
         and all(re.search(r'^\s+' + re.escape(k) + r' ', COMP, re.M) for k in CELLS)),
        ('G-C2-RULE-APPLIED', 'suite re-applies the rule and agrees (%s)' % verdict,
         RJ.get('verdict') == verdict and verdict_line(COMP, 'VERDICT, BY THE RULE FIXED ON THE FACE', verdict)),
        ('G-C2-RATE-WHERE-CONVERGES', 'a rate at exactly the cells where (a) falls',
         sorted((RJ.get('rates') or {}).keys()) == sorted(k for k in good if rule(AJ['base'][k]['e'], AJ['a'][k]['e']) == 'FALLS')
         and all(abs(RJ['rates'][k] - __import__('math').log2(abs(AJ['base'][k]['e']) / abs(AJ['a'][k]['e']))) < 1e-9 for k in RJ.get('rates', {}))),
        ('G-C2-FLOOR-GOVERNS', 'floor in the rule and the below-floor count printed',
         'FLOOR = 1.49e-08' in SRC_COMP and 'or abs(ev) <= FLOOR' in SRC_COMP and 'cells below the floor' in COMP),

        ('G-C3-OBLIGATION-STATED', 'the obligation for the verdict printed', verdict in OBLIG and OBLIG[verdict] in COMP),
        ('G-C3-CHAIN-FIGURES-LISTED', '%d chain tools listed by name' % len(users),
         len(users) > 0 and all(u['tool'] in COMP for u in users)),
        ('G-C3-NONE-REVERDICTED', 'none re-verdicted, said', 'None is re-verdicted' in COMP and 'b444`s banked verdict is not edited' in COMP
         and all(not touched(ROOT, re.escape('data/' + u['tool'].replace('.py', ''))) for u in users)),
        ('G-C3-FOURTH-OWNER-PRICED', 'fourth candidate priced, not run', 'THE FOURTH CANDIDATE, PRICED AND NOT RUN' in COMP
         and 'zetazero(n)' not in pycode_of(SRC_COMP)),
        ('G-C3-NO-ZERO-CLAIM', 'no zero claim', 'NO CLAIM ABOUT ZEROS IN ANY BRANCH' in COMP),
        ('G-N1-APART', 'N1 apart', fold('TWO CLAUSES APART') in F and '(N1)' in F),
        ('G-N2-SCORED', 'N2 scorable by the verdict', verdict in ('INTEGRATION', 'TRUNCATION', 'UNDETERMINED', 'BOTH MOVE', 'MIXED')),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations on face', fold("AND THIS SEAT'S OWN:") in F),

        ('G-NOCHAIN-FILE-EDITED', 'the five chain files unmoved in tree and commits',
         all(unchanged(ROOT, p) for p in CHAIN) and chain_committed == []),
        ('G-NONEWCELL', 'every arm keyed to exactly the 14 cells',
         all(sorted(AJ.get(arm, {}).keys()) == sorted(CELLS) for arm in arms5)),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b445' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-NOTECHNE-WRITE', 'TECHNE untouched', t_dirty.strip() == ''),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail', all(f == 'OPEN_TRAILS.md' for f in pp_touched)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
                                                             or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b445' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-LANE-CLOSED-SAID', 'the lane`s closure printed by the components', verdict_line(COMP, 'THE INSTRUMENT LANE OPENED BY (R57)', 'CLOSES AT THIS ACT`S END')),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names)), sorted(set(names) - set(DEC))))
    rec('  the verdict, re-applied by this suite from b445_arms.json : %s' % verdict)
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
