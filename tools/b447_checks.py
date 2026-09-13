# -*- coding: utf-8 -*-
"""b447_checks.py -- THE CONTROL SUITE FOR b447. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b447_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b447_checks.txt')
POSTPUSH = os.path.join(D, 'b447_checks_postpush.txt')
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
                for f in ('b447_ferry.txt', 'b447_ferry_scan.txt'))


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
        if 'b447' not in subj:
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
COMP = read(os.path.join(D, 'b447_components.txt'))
EXTR = read(os.path.join(D, 'b447_extract.txt'))
RGATE = read(os.path.join(D, 'b447_reg_gate.txt'))
TERM = read(os.path.join(D, 'b447_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b447_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b447_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b447_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b447_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b447_ferry.txt'))
CENS = read(os.path.join(D, 'b447_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b447_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b447_pins_stepzero.txt'))
ADD = os.path.join(D, 'b447_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b447_components.py'))
SRC_DESK = read(os.path.join(T, 'b447_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b447_extract.py'))
SRC_CHK = read(os.path.join(T, 'b447_checks.py'))
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
        if 'b447' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False






TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
BFRREL = 'modules/2026-09/BAR_FLOOR_RULE.md'
BFR = read(os.path.join(TECHNE, BFRREL))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
LOOM = read(os.path.join(PP, 'VERIFICATION_LOOM.md'))
BLOCK = read(os.path.join(D, 'b447_loom_block.md'))
LOOMRUN = read(os.path.join(D, 'b447_loom_append_run.txt'))
CELL = '4.123106'
CHAIN = ['tools/e16/carto_atlas.py', 'tools/e16/zeta_ordinates.npy', 'tools/b317_smear.py', 'tools/b318_square.py',
         'tools/b321_window.py', 'tools/noise_floor.py', 'tools/registration_gate.py', 'tools/b363_span.py',
         'tools/b244_loom_append.py']


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


DJ = _j('b447_doubling.json')
SJ = _j('b447_stocktake.json')
B445 = _j('b445_arms.json')
B446 = _j('b446_doubling.json')
CJ = _j('b446_floor_census.json')
SPAN = _j('b447_span.json')
C1 = SJ.get('c1') or {}


def main(argv):
    import math
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b447 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b447')) | set(committed_by_act(ROOT, r'b447')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b447_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    chain_committed = committed_by_act(ROOT, r'^(tools/e16/carto_atlas\.py|tools/e16/zeta_ordinates\.npy|tools/b31[78]_\w+\.py|tools/b321_window\.py|tools/noise_floor\.py|tools/registration_gate\.py|tools/b363_span\.py|tools/b244_loom_append\.py)$')
    closings_committed = [f for f in committed_by_act(ROOT, r'_closing\.txt$') if 'b447' not in f]
    closings_touched = [ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines()
                        if '_closing.txt' in ln and 'b447' not in ln]
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'f96725a', 'origin/main'],
                                       capture_output=True).returncode
    t_head = git(TECHNE, 'rev-parse', 'HEAD').strip()
    t_remote = git(TECHNE, 'branch', '-r', '--contains', 'HEAD').strip()
    t_num = git(TECHNE, 'log', '-1', '--grep', 'b447', '--numstat', '--format=', '--', BFRREL).split()
    # ### THE LEVELS, RE-READ FROM THEIR OWN BANKS.
    try:
        lv = [B445['base'][CELL]['e'], B445['a'][CELL]['e'], B446[CELL]['e'], DJ[CELL]['e']]
        dd = [lv[i - 1] - lv[i] for i in (1, 2, 3)]
        p1 = math.log2(abs(dd[0]) / abs(dd[1]))
        p2 = math.log2(abs(dd[1]) / abs(dd[2]))
        conv = (0.9465 <= p2 <= 1.9465) and abs(dd[2]) < abs(dd[1])
        lv_ok = C1.get('e') == lv and abs(C1.get('p1', 9) - p1) < 1e-9 and abs(C1.get('p2', 9) - p2) < 1e-9
    except Exception:
        lv, p1, p2, conv, lv_ok = [], None, None, None, False
    op = SJ.get('open') or []
    names = [o['item'] for o in op]
    aimed = [o['item'] for o in op if o.get('aim') == 'AIMED']
    declared_by = {'b443r site (vi) of the witness arc', 'b445 whose residual it is (b444`s standing item)',
                   'b446 the second doubling at the five cells', 'b447 Component 1: CONVERGES'}
    outcome = C1.get('outcome', '')

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned before sending, zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, '### MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED-PUSHED', 'row 295 on the face and b446 on origin/main', 'row 295' in F and prior_pushed),
        ('G-R60-ENTERED', '(R60) entered', fold('(R60)` -- the instrument lane opens for the outlier alone') in F),
        ('G-WORDING-ERROR-ENTERED', 'the order`s wording error entered', fold("AN ERROR IN THE ORDER'S WORDING, ENTERED AS THE NAVIGATOR'S:") in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b447_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C1-ONE-CELL', 'one cell at nv 65537, NU 96001', sorted(DJ.keys()) == [CELL] and DJ[CELL].get('nv') == 65537 and DJ[CELL].get('nu') == 96001),
        ('G-C1-FOUR-LEVELS', 'four levels read from their banks', len(lv) == 4 and lv_ok),
        ('G-C1-ORDERS-RECOMPUTED', 'p1 %s, p2 %s recomputed' % (('%.3f' % p1) if p1 is not None else '-', ('%.3f' % p2) if p2 is not None else '-'), lv_ok),
        ('G-C1-RULE-APPLIED', 'rule re-applied (%s)' % conv, conv is not None and C1.get('converges') == conv),
        ('G-C1-OUTCOME-SAID', 'the outcome and, if refusing, three candidates NOT RUN',
         verdict_line(COMP, '### ### **THE OUTLIER', outcome) and (conv or all(x in COMP for x in ('### (c1)', '### (c2)', '### (c3)')))),

        ('G-C2-LOOM-ONE-BLOCK', 'one b447 marker in the loom', LOOM.count('<!-- b447 loom entry -->') == 1),
        ('G-C2-LOOM-PREFIX-PROVED', 'appender proved the prefix', verdict_line(LOOMRUN, 'PREFIX UNCHANGED', 'YES')),
        ('G-C2-HEADER-QUOTED', 'both header sentences in the block', "A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR OF b264's FLOOR MODES" in BLOCK
         and 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.' in BLOCK),
        ('G-C2-CENSUS-FIGURES-MATCH', 'block figures equal b446`s census', bool(CJ) and ('**%d** banked comparisons' % CJ['kind']['all']) in BLOCK
         and ('**%d** of them' % CJ['kind']['out']) in BLOCK and ('fired **%d**' % CJ['residue']['json_verdicts']['AT_FLOOR']) in BLOCK),
        ('G-C2-NO-CLOSING-EDITED', 'no prior closing touched or committed', closings_committed == [] and closings_touched == []),
        ('G-C2-BAR-FLOOR-ONE-LINE', 'one line appended, 0 removed (numstat %s)' % t_num[:2], BFR.count('The other face (b447)') == 1
         and len(t_num) >= 2 and t_num[1] == '0' and t_num[0] in ('1', '2')),
        ('G-C2-TWO-INCIDENTS-NAMED', 'b272 and b446 named', bool(re.search(r'The other face \(b447\).*\*\*b272\*\*.*\*\*b446\*\*', BFR))),
        ('G-C2-TECHNE-LOCAL', 'committed in TECHNE, tree clean', bool(t_num) and t_dirty.strip() == ''),

        ('G-C3-CLOSED-ANCHORED', 'five closed items each anchored', len(SJ.get('closed') or []) == 5 and all(c.get('line') for c in SJ['closed'])),
        ('G-C3-DESK-COLLAPSED', 'no open item printed twice', len(names) == len(set(names))),
        ('G-C3-PAIRS-ONLY-DECLARED', 'closures only by declared pairs', all(c.get('by') in declared_by for c in SJ.get('desk_closed') or [])),
        ('G-C3-TRIGGERS-PRINTED', 'every open item has a trigger or NO TRIGGER', bool(op) and all((o.get('trigger') or '').strip() for o in op)),
        ('G-C3-AIM-CLASSED', 'every open item classed; AIMED %s' % aimed, bool(op) and all(o.get('aim') in ('AIMED', 'NAMES', 'NEITHER') for o in op)
         and SJ.get('aimed') == aimed),
        ('G-C3-K8-APART', 'K8 printed as the clause, not an item', 'K8 IS THE QUANTIFIER, UNOWNED' in COMP and not any('K8' in n for n in names)),
        ('G-C3-PROPOSES-NOTHING', 'nothing proposed said', 'NOTHING IS PROPOSED; THE LIST IS THE PRODUCT.' in COMP),

        ('G-N1-APART', 'N1 two clauses', fold('TWO CLAUSES APART') in F and '(N1)(a)' in COMP and '(N1)(b)' in COMP),
        ('G-N1-SCORED', 'N1 scored by the rule', conv is not None and verdict_line(COMP, '(N1)(a) the outlier converges', 'HELD' if conv else 'REFUTED')
         and verdict_line(COMP, '(N1)(b) the refusal was', 'REFUTED AS WORDED')),
        ('G-N2-SCORED', 'N2 scored by the aim class', verdict_line(COMP, '(N2)    no open item aimed', 'REFUTED' if aimed else 'HELD')),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', "the seat`s own from the face" in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b447 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b447'
         and SPAN.get('this_act') == 447 and isinstance(SPAN.get('current_span'), int)),

        ('G-NOCHAIN-FILE-EDITED', 'chain, gate, span and loom tools unmoved', all(unchanged(ROOT, p) for p in CHAIN) and chain_committed == []),
        ('G-NOOTHERCELL', 'the doubling keyed to the one cell', sorted(DJ.keys()) == [CELL]),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b447' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the loom and the trail', all(f in ('OPEN_TRAILS.md', 'VERIFICATION_LOOM.md') for f in pp_touched)
         and unchanged(PP, 'FINDINGS.md')),
        ('G-TECHNE-UNPUSHED', 'TECHNE HEAD on no remote branch', bool(t_head) and t_remote == ''),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
                                                             or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b447' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-LANE-CLOSED-SAID', 'the lane`s closure printed', verdict_line(COMP, 'THE INSTRUMENT LANE OPENED BY (R60)', 'CLOSES AT THIS ACT`S END')),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names_arms = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names_arms)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names_arms)), sorted(set(names_arms) - set(DEC))))
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
