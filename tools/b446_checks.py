# -*- coding: utf-8 -*-
"""b446_checks.py -- THE CONTROL SUITE FOR b446. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b446_registration_2026-09-12.txt')
PREPUSH = os.path.join(D, 'b446_checks.txt')
POSTPUSH = os.path.join(D, 'b446_checks_postpush.txt')
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
                for f in ('b446_ferry.txt', 'b446_ferry_scan.txt'))


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
        if 'b446' not in subj:
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
COMP = read(os.path.join(D, 'b446_components.txt'))
EXTR = read(os.path.join(D, 'b446_extract.txt'))
RGATE = read(os.path.join(D, 'b446_reg_gate.txt'))
TERM = read(os.path.join(D, 'b446_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b446_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b446_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b446_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b446_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b446_ferry.txt'))
CENS = read(os.path.join(D, 'b446_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b446_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b446_pins_stepzero.txt'))
ADD = os.path.join(D, 'b446_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b446_components.py'))
SRC_CEN = read(os.path.join(T, 'b446_census.py'))
SRC_DESK = read(os.path.join(T, 'b446_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b446_extract.py'))
SRC_CHK = read(os.path.join(T, 'b446_checks.py'))
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
        if 'b446' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False





TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODULE = 'modules/2026-09/FLOOR_DOMAIN_RULE.md'
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
CENTXT = read(os.path.join(D, 'b446_floor_census.txt'))
RSCAN1 = read(os.path.join(D, 'b446_ruling_scan.txt'))
RSCAN2 = read(os.path.join(D, 'b446_ruling_r59_scan.txt'))
try:
    DJ = json.loads(read(os.path.join(D, 'b446_doubling.json')))
except Exception:
    DJ = {}
try:
    CJ = json.loads(read(os.path.join(D, 'b446_floor_census.json')))
except Exception:
    CJ = {}
try:
    B445 = json.loads(read(os.path.join(D, 'b445_arms.json')))
except Exception:
    B445 = {}
RJ = DJ.get('report') or {}
FIVE = ['3.158312', '3.461088', '3.605551', '4.061553', '4.123106']
OUTLIER = '4.123106'
FLOOR = 1.49e-08
CHAIN = ['tools/e16/carto_atlas.py', 'tools/e16/zeta_ordinates.npy', 'tools/b317_smear.py',
         'tools/b318_square.py', 'tools/b321_window.py', 'tools/noise_floor.py']


def recompute_c3():
    """### THE FACE'S RULES, RE-APPLIED INDEPENDENTLY OF THE COMPONENTS' OWN APPLICATION."""
    import math
    orders, ok = {}, True
    for k in FIVE:
        e0, e1, e2 = B445['base'][k]['e'], B445['a'][k]['e'], DJ[k]['e']
        p = math.log2(abs(e0 - e1) / abs(e1 - e2))
        orders[k] = p
        c = RJ['c3'][k]
        ok = ok and abs(c['p'] - p) < 1e-9 and c['e0'] == e0 and c['e1'] == e1 and c['e2'] == e2
    oth = sorted(orders[k] for k in FIVE if k != OUTLIER)
    m = (oth[1] + oth[2]) / 2
    refuses = not (m - 0.5 <= orders[OUTLIER] <= m + 0.5)
    span = max(orders.values()) - min(orders.values())
    return ok, orders, refuses, span


def main(argv):
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b446 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b446')) | set(committed_by_act(ROOT, r'b446')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b446_registration_2026-09-12.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_CEN + NL + SRC_DESK)
    chain_committed = committed_by_act(ROOT, r'^(tools/e16/carto_atlas\.py|tools/e16/zeta_ordinates\.npy|tools/b31[78]_\w+\.py|tools/b321_window\.py|tools/noise_floor\.py|tools/registration_gate\.py)$')
    try:
        c3ok, orders, refuses, span = recompute_c3()
    except Exception:
        c3ok, orders, refuses, span = False, {}, None, None
    kd = CJ.get('kind') or {}
    ctl = CJ.get('controls') or {}
    c1 = RJ.get('c1') or []
    t_head = git(TECHNE, 'rev-parse', 'HEAD').strip()
    t_remote = git(TECHNE, 'branch', '-r', '--contains', 'HEAD').strip()
    t_tracked = MODULE in git(TECHNE, 'ls-files', MODULE)
    MOD = read(os.path.join(TECHNE, MODULE))
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '0cfa239', 'origin/main'],
                                       capture_output=True).returncode
    n1_line = [ln for ln in COMP.splitlines() if ln.strip().startswith('(N1)    neither')]
    n2_line = [ln for ln in COMP.splitlines() if ln.strip().startswith('(N2)    more than half')]
    share = (kd.get('out', 0) / kd['all']) if kd.get('all') else 0

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned before sending, zero hits' in FERRY),
        ('G-RULINGS-BANKED-CLEAN', 'both rulings banked and 0 hits', verdict_line(RSCAN1, '### VERDICT:', '0 HIT(S) REPORTED')
         and verdict_line(RSCAN2, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, '### MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED-PUSHED', 'row 294 on the face and b445 on origin/main', 'row 294' in F and prior_pushed),
        ('G-R58-AMENDED-ENTERED', '(R58) as amended', fold('the cell that moved without falling among them') in F),
        ('G-R59-ENTERED', '(R59) and the mint', fold('A FLOOR CARRIES THE DOMAIN OF KIND AND THE PARAMETERS OVER WHICH IT WAS MEASURED') in F),
        ('G-ERRORS-ENTERED-AS-OWNERS', 'navigator`s two and the seat`s one', fold("THE NAVIGATOR'S, BY RULING (4):") in F
         and fold("THE NAVIGATOR'S, BY ADDITION (b), IN HIS OWN WORDS:") in F and fold("THE SEAT'S, ENTERED HERE BY THE SEAT:") in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b446_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C1-ORIGIN-QUOTED', 'history quoted by line from sources', 'history quoted from sources : True' in COMP
         and 'tools/noise_floor.py:49 | DEFAULT_FLOOR = math.sqrt(MACHINE_EPS)' in COMP),
        ('G-C1-KIND-DOMAIN-QUOTED', 'the contract of kind quoted', 'ANY ACT READING A COMPUTED SPECTRAL OR MODAL QUANTITY' in COMP),
        ('G-C1-B437-RUNNER', 'b437 named a runner, not a setter', 'RAN the gate at 5.196152, 5.385165, 5.567764' in COMP),
        ('G-C1-PER-CELL-PRINTED', 'fourteen measured cells printed', len(c1) == 14
         and all(re.search(r'^\s+' + re.escape(r['a']) + r' ', COMP, re.M) for r in c1)),
        ('G-C1-ORDER-RULE-APPLIED', 'p* rule re-applied (span %s)' % (('%.2f' % span) if span is not None else '-'),
         span is not None and ((span > 1.0 and RJ.get('pstar') is None and all('no p* taken' in r['how'] for r in c1 if r['a'] not in FIVE))
                               or (span <= 1.0 and RJ.get('pstar') is not None))
         and all(abs(r['err'] - (r['e0'] - RJ['limits'][r['a']])) < 1e-15 for r in c1 if r['a'] in FIVE)),
        ('G-C1-NOFIT', 'no function of radius fitted', 'NO FUNCTION FITTED' in COMP and not re.search(r'polyfit|curve_fit|lstsq', CODE)),
        ('G-C1-UNMEASURED-MARKED', 'eight cells marked NOT MEASURED', len(RJ.get('unmeasured') or []) == 8
         and COMP.count('NOT MEASURED -- below the quoted bar at base') == 8),

        ('G-C2-MATCHER-YIELDS', 'M0-M3 yields printed', all(x in CENTXT for x in ('M0 word-lines :', 'M1 gate verdict instances :',
                                                                              'M2 floor-arm decisions :', 'M3 quoted-threshold comparisons :'))),
        ('G-C2-POSITIVE-CONTROLS', 'b437 and b444 found', bool(ctl.get('pos_b437')) and bool(ctl.get('pos_b444'))),
        ('G-C2-NEGATIVE-CONTROL', 'b272 definitions not counted', bool(ctl.get('neg_b272'))),
        ('G-C2-KIND-CLASSED', 'every comparison classed', kd.get('all') == CJ.get('m1_lines', -1) + CJ.get('m3_lines', -1)),
        ('G-C2-OUT-PRINTED', 'every OUT printed one line each', 'EVERY COMPARISON, ONE LINE EACH' in CENTXT
         and CENTXT.split('EVERY COMPARISON, ONE LINE EACH')[-1].split('THE FLOOR ARM`S DECISIONS')[0].count(' ; OUT ; ') == kd.get('out', -1)),
        ('G-C2-FLOOR-ARM-COUNTED', 'floor-arm decisions counted, residue printed', 'WHAT THE FLOOR ARM DECIDED' in CENTXT
         and isinstance(CJ.get('m2'), int) and (CJ.get('residue') or {}).get('json_verdicts') is not None),
        ('G-C2-RADIUS-VACUOUS', 'radius reading said vacuous', verdict_line(CENTXT, '### radius -- VACUOUS', 'VACUOUS')),
        ('G-C2-NONE-REVERDICTED', 'nothing re-verdicted said', 'NOTHING IS RE-VERDICTED' in CENTXT and 'NOTHING RE-VERDICTED' in COMP),

        ('G-C3-FIVE-CELLS', 'five cells at nv 32769, NU 48001', all(DJ.get(k, {}).get('nv') == 32769 and DJ[k].get('nu') == 48001 for k in FIVE)),
        ('G-C3-THREE-LEVELS', 'e0, e1 read from b445 and e2 from this act', c3ok),
        ('G-C3-ORDER-RULE', 'orders re-computed agree', c3ok and all(abs(RJ['orders'][k] - orders[k]) < 1e-9 for k in FIVE)),
        ('G-C3-OUTLIER-RULE', 'outlier rule re-applied (%s)' % refuses, refuses is not None and RJ.get('outlier_refuses') == refuses),
        ('G-C3-BAR-OUT-OF-KIND', 'every bar comparison labelled out of kind', COMP.count('(the bar quoted outside its kind)') == 5),

        ('G-C4-READABILITY-PRINTED', 'readability test printed', verdict_line(COMP, 'READABLE BY A GATE :', 'READABLE BY A GATE : False')),
        ('G-C4-JUDGEMENT-FILED', 'filed as judgement in the report and the module', 'FILED AS JUDGEMENT, NOT MECHANIZED' in COMP
         and 'FILED AS JUDGEMENT, NOT MECHANIZED' in MOD),
        ('G-C4-TECHNE-LOCAL', 'module committed in TECHNE, tree clean', t_tracked and bool(t_head) and t_dirty.strip() == ''),
        ('G-C4-GATE-UNEDITED', 'registration_gate.py and noise_floor.py unmoved', unchanged(ROOT, 'tools/registration_gate.py')
         and unchanged(ROOT, 'tools/noise_floor.py') and chain_committed == []),

        ('G-N1-SCORED', 'N1 scored on kind, radius vacuous beside', bool(n1_line) and 'REFUTED' in n1_line[0]
         and 'radius reading: no radius domain was stated -- VACUOUS' in COMP),
        ('G-N2-SCORED', 'N2 scored on kind (share %.3f)' % share, bool(n2_line)
         and (('HELD' in n2_line[0]) == (share > 0.5)) and 'radius reading: all lie outside -- VACUOUS' in COMP),
        ('G-N3-APART', 'N3 two clauses scored apart', fold('TWO CLAUSES APART') in F and '(N3)(a)' in COMP and '(N3)(b)' in COMP),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', "the seat`s own from the face" in COMP),
        ('G-ADDITION-A-PRINTED', 'addition (a) with the header quoted', 'ADDITION (a)' in COMP
         and 'IT IS THE DRIFT ARM THAT BITES, NOT THE FLOOR ARM.' in COMP and 'WORD-LINES, PROSE INCLUDED' in COMP),

        ('G-NOCHAIN-FILE-EDITED', 'chain files and the gate tool unmoved', all(unchanged(ROOT, p) for p in CHAIN) and chain_committed == []),
        ('G-NONEWCELL', 'the doubling keyed to exactly the five cells', sorted(k for k in DJ if k != 'report') == sorted(FIVE)),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b446' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail', all(f == 'OPEN_TRAILS.md' for f in pp_touched)),
        ('G-TECHNE-UNPUSHED', 'TECHNE HEAD on no remote branch', bool(t_head) and t_remote == ''),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
                                                             or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b446' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-LANE-CLOSED-SAID', 'the lane`s closure printed', verdict_line(COMP, 'THE INSTRUMENT LANE OPENED BY (R58)', 'CLOSES AT THIS ACT`S END')),
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
