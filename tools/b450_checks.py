# -*- coding: utf-8 -*-
"""b450_checks.py -- THE CONTROL SUITE FOR b450. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b450_registration_2026-09-13.txt')
PREPUSH = os.path.join(D, 'b450_checks.txt')
POSTPUSH = os.path.join(D, 'b450_checks_postpush.txt')
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
                for f in ('b450_ferry.txt', 'b450_ferry_scan.txt'))


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
        if 'b450' not in subj:
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
COMP = read(os.path.join(D, 'b450_components.txt'))
EXTR = read(os.path.join(D, 'b450_extract.txt'))
RGATE = read(os.path.join(D, 'b450_reg_gate.txt'))
TERM = read(os.path.join(D, 'b450_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b450_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b450_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b450_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b450_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b450_ferry.txt'))
CENS = read(os.path.join(D, 'b450_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b450_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b450_pins_stepzero.txt'))
ADD = os.path.join(D, 'b450_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b450_components.py'))
SRC_DESK = read(os.path.join(T, 'b450_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b450_extract.py'))
SRC_CHK = read(os.path.join(T, 'b450_checks.py'))
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
        if 'b450' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False









CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
B450MARK = '<!-- b450 the eligible set re-measured, and the batch read -->'
REPAIRED = ['phase1.5/method/TECHNE_TOOLKIT.md', 'phase2/method/E_DIFFICULTY_THEOREM.md']


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


EJ = _j('b450_eligible.json')
BJ = _j('b450_batch.json')
RJ = _j('b450_repairs.json')
V = BJ.get('verdict') or {}
SPAN = _j('b450_span.json')
MIRROR = read(os.path.join(D, 'b450_mirror.txt'))
RULE = 'take the one whose terminals the drive can reach'


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b450 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b450')) | set(committed_by_act(ROOT, r'b450')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b450_registration_2026-09-13.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '3d8b726', 'origin/main'], capture_output=True).returncode
    trails = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    blk = trails[trails.find(B450MARK):] if B450MARK in trails else ''
    t_dirty = git(os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core'), 'status', '--porcelain', '--untracked-files=no').strip()

    # ### RE-DERIVED: the census population and the eligible count.
    cen = [l for i, l in enumerate(read(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')).splitlines(), 1) if 73 <= i <= 88 and l.startswith('| `')]
    pop = len(cen)
    rows = EJ.get('rows') or []
    elig = [r['k'] for r in rows if r.get('state') == 'ELIGIBLE']
    recon = [r['k'] for r in rows if r.get('state') == 'RECONCILED']
    excl = [r for r in rows if r.get('state') == 'EXCLUDED']
    reach_live = True
    for r in rows:
        if r.get('state') == 'ELIGIBLE':
            ok = any(os.path.isdir(os.path.join('D:' + os.sep, n, '.git')) for n in r.get('on_drive', []))
            reach_live = reach_live and ok
    order_ok = BJ.get('order') == [c.split('`')[1] for c in cen if c.split('`')[1] in elig]
    ks = BJ.get('keystones') or {}
    A_, S_, N_ = 'ALREADY SAYS IT', 'SAYS SOMETHING NOW SUPERSEDED', 'DOES NOT CARRY IT'
    tot = dict((b, sum(ks[k]['buckets'][b] for k in ks)) for b in (A_, S_, N_)) if ks else {}
    sp = dict((s, sum(len(ks[k]['species'][s]) for k in ks)) for s in ('phantom', 'unpropagated', 'superseded')) if ks else {}
    made = RJ.get('made') or []
    # ### the repairs, re-read from the files against the pre-act blob.
    rep_ok, lineage_ok = True, True
    for rel in REPAIRED:
        cur = read(os.path.join(PP, rel)).replace(chr(13) + chr(10), NL).split(NL)
        base = git(PP, 'show', ('HEAD~0:' if not post else 'HEAD~1:') + rel)
        if post:
            base = subprocess.run(['git', '-C', PP, 'log', '--format=%H', '-2', '--', rel], capture_output=True, text=True).stdout.split()
            base = git(PP, 'show', base[1] + ':' + rel) if len(base) > 1 else ''
        pre = base.replace(chr(13) + chr(10), NL).split(NL)
        diff = [j for j, (x, y) in enumerate(zip(pre, cur), 1) if x != y]
        mine = [m['line'] for m in made if rel.endswith(m['k'] + '.md')]
        rep_ok = rep_ok and bool(pre) and sorted(diff) == sorted(mine) and len(cur) >= len(pre) and \
            all(pre[j - 1].replace('v0.2', 'v0.5.4', 1) == cur[j - 1] for j in diff) and '<!-- b450 CURRENCY ANNOTATION, 2026-09-13 -->' in NL.join(cur)
    am = read(os.path.join(PP, 'phase1.5', 'method', 'A_METHODOLOGY.md'))
    lineage_ok = bool(re.search(r'\bv0\.2\b', am)) and all(m['was'] == 'v0.2' and m['now'] == 'v0.5.4' for m in made)
    reg218 = read(os.path.join(PP, 'REGISTRY.md')).splitlines()[217]
    n1 = 'HELD' if (len(elig) >= 8 and len(elig) != 4) else 'REFUTED'
    largest = [b for b in tot if tot[b] == max(tot.values())] if tot else []
    n2a = 'HELD' if largest == [N_] else ('REFUTED AS WORDED -- a tie' if N_ in largest else 'REFUTED')
    n2b = 'HELD' if sp.get('unpropagated', 0) >= 1 else 'REFUTED'

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-13-b450.zip' in MIRROR
                and verdict_line(MIRROR, 'manifest declares source HEAD', git(PP, 'rev-parse', '--short=7', 'HEAD').strip()))

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
        ('G-PRIOR-CLOSED-PUSHED', 'row 298 on the face; 3d8b726 on origin/main', 'row 298' in F and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b450_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-RULE-VERBATIM-ON-FACE', 'b390`s sentence on the face equals its source line', RULE in FACET and RULE in trails.splitlines()[4445]
         and 'The census’s own release-blocking line settles it' in FACET),
        ('G-RULE-DIFFERENCES-PRINTED', 'D1 and D2 on the face and in the components', '(D1)' in FACET and '(D2)' in FACET and '(D1)' in COMP and '(D2)' in COMP),
        ('G-WANTED-NOT-APPLIED', 'W1 and W2 printed; no keystone excluded by either', '(W1)' in FACET and '(W2)' in FACET
         and not any('PARTIAL' in r.get('why', '') and r.get('state') == 'EXCLUDED' for r in rows) and not any('pin' in r.get('why', '').lower() for r in excl)),
        ('G-C1-POPULATION-FROM-CENSUS', 'population %d re-read from the census' % pop, pop == 16 and EJ.get('population') == pop and len(rows) == pop),
        ('G-C1-RECONCILED-BY-ACTS', 'reconciled %s' % recon, sorted(recon) == sorted(['ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'GRH_CASCADE', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'SILENCE_STAGES_DEALIGNMENT'])
         and 'none is a later reconciliation' in COMP),
        ('G-C1-WIDE-MATCHER-CARRIED', 'b395`s V2 carried verbatim', "V2 = re.compile(r'`?(SIDE-[A-Za-z0-9][A-Za-z0-9-]*)`?')" in SRC_COMP),
        ('G-C1-REACH-LIVE', 'every eligible names a .git repository on the drive', reach_live and bool(elig)),
        ('G-C1-EXCLUSIONS-REASONED', 'every exclusion carries a reason', all(r.get('why') for r in excl) and len(excl) == pop - len(recon) - len(elig)),
        ('G-C1-ELIGIBLE-NAMED', 'eligible %d named in the components' % len(elig), bool(elig) and all(k in COMP for k in elig)
         and verdict_line(COMP, 'THE ELIGIBLE REMAINDER, IN CENSUS ORDER', ': %d**' % len(elig))),
        ('G-C1-BOARD-FIGURE-BESIDE', 'the board`s twelve beside the measured unread', verdict_line(COMP, 'the board`s "twelve unread"', 'measured unread')),
        ('G-C2-CENSUS-ORDER', 'batch order equals census order', order_ok),
        ('G-C2-EVERY-ELIGIBLE-READ', 'all %d read' % len(elig), sorted(ks) == sorted(elig) and verdict_line(COMP, 'THE BATCH IS COMPLETE', 'UNREAD REMAINDER : NONE')),
        ('G-C2-TABLE-TWO-SHAPES', 'T1, T2 and TW yields printed per keystone', all(('t1' in ks[k] and 't2_rows' in ks[k] and 'tw_rows' in ks[k]) for k in ks)
         and 'THE DEFECTIVE PREDICATE IS NAMED' in COMP),
        ('G-C2-BUCKETS-PER-KEYSTONE', 'buckets per keystone sum across the batch', bool(tot) and all(set(ks[k]['buckets']) == {A_, S_, N_} for k in ks)
         and tot == V.get('buckets')),
        ('G-C2-BUCKETS-EMPTY-REPORTED', 'each bucket reported FULL or EMPTY', all(verdict_line(COMP, '      %-32s' % b, 'FULL' if tot.get(b) else 'EMPTY') for b in (A_, S_, N_))),
        ('G-C2-SPECIES-APART', 'three species printed apart; no sum', sp == V.get('species') and 'phantom      :' in COMP and 'unpropagated :' in COMP
         and 'superseded   :' in COMP and not re.search(r'(?i)species (?:sum|total)', COMP)),
        ('G-C2-REPAIRS-IN-LINEAGE', 'v0.2 in A_METHODOLOGY`s bytes; registry row 218 at v0.5.4', lineage_ok and '`phase1.5/method/A_METHODOLOGY.md` | v0.5.4 |' in reg218),
        ('G-C2-REPAIRS-ONLY-VERSION', 'the repaired files differ from the blob on the repaired lines only, by the version', rep_ok and len(made) == 3),
        ('G-C2-REPAIRS-ANNOTATED', 'originals preserved in the annotation', all(m.get('annotated') for m in made)
         and all(m['original'][:60] in ' '.join(read(os.path.join(PP, r)).split()) for m in made for r in REPAIRED if r.endswith(m['k'] + '.md'))),
        ('G-C2-NO-LINE-REMOVED', 'lines removed 0', all(m.get('removed') == 0 for m in made)),
        ('G-C2-EXCLUDED-REPAIRS-REASONED', 'every excluded candidate reasoned', all(e.get('why') for e in RJ.get('excluded') or [])),
        ('G-C2-ROUTED-APART', 'routed counted apart from made', verdict_line(COMP, 'REPAIRS MADE :', 'REPAIRS ROUTED : %d' % V.get('routed', -1)) and V.get('made') == len(made)),
        ('G-C2-NO-TABLE-WRITTEN', 'no table written; only the two keystones touched in PLACE-papers beside the trail',
         all(f in REPAIRED + ['OPEN_TRAILS.md'] for f in pp_touched + pp_committed)),
        ('G-C2-HALT-OR-COMPLETE', 'complete, or a halt naming the remainder', V.get('complete') is True),
        ('G-C2-TIMES-AS-FLOORS', 'times printed as floors', verdict_line(COMP, 'TIMES, BOTH FLOORS', 'per keystone')),
        ('G-FILING-C4', '(c4) filed in the trail with its terms', bool(blk) and '(c4)' in blk and '+1.161e-07' in blk and '-8.101e-08' in blk and 'NOT RUN' in blk.upper()),
        ('G-FILING-C2-STANDS', '(c2) priced and not run, measurement open', bool(blk) and '(c2)' in blk and 'measurement stays open' in blk.lower()),
        ('G-N1-SCORED', 'N1 %s' % n1, verdict_line(COMP, '(N1)    the eligible set', n1)),
        ('G-N2-APART', 'N2 two clauses', fold('TWO CLAUSES APART') in F and '(N2)(a)' in COMP and '(N2)(b)' in COMP),
        ('G-N2-SCORED', 'N2 (a) %s (b) %s' % (n2a, n2b), verdict_line(COMP, '(N2)(a) the largest bucket', n2a) and verdict_line(COMP, '(N2)(b) at least one', n2b)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b450 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b450' and SPAN.get('this_act') == 450),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER and REGISTRY untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md') and unchanged(PP, 'REGISTRY.md')
         and 'REGISTRY.md' not in pp_committed),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched; TECHNE tracked tree clean', 0 == len(touched(WINREPO, r'.')) and t_dirty == ''),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b450' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: the trail and the two repaired keystones only', all(f in REPAIRED + ['OPEN_TRAILS.md'] for f in pp_touched + pp_committed)
         and unchanged(PP, 'FINDINGS.md') and unchanged(PP, 'phase2/method/THE_KEYSTONE_CENSUS.md')),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b450' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-13-b450, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
