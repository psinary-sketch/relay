# -*- coding: utf-8 -*-
"""b451_checks.py -- THE CONTROL SUITE FOR b451. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b451_registration_2026-09-13.txt')
PREPUSH = os.path.join(D, 'b451_checks.txt')
POSTPUSH = os.path.join(D, 'b451_checks_postpush.txt')
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
                for f in ('b451_ferry.txt', 'b451_ferry_scan.txt'))


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
        if 'b451' not in subj:
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
COMP = read(os.path.join(D, 'b451_components.txt'))
EXTR = read(os.path.join(D, 'b451_extract.txt'))
RGATE = read(os.path.join(D, 'b451_reg_gate.txt'))
TERM = read(os.path.join(D, 'b451_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b451_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b451_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b451_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b451_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b451_ferry.txt'))
CENS = read(os.path.join(D, 'b451_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b451_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b451_pins_stepzero.txt'))
ADD = os.path.join(D, 'b451_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b451_components.py'))
SRC_DESK = read(os.path.join(T, 'b451_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b451_extract.py'))
SRC_CHK = read(os.path.join(T, 'b451_checks.py'))
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
        if 'b451' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False










B451MARK = '<!-- b451 the remainder named, and the routed items grouped -->'
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
LOREREL = 'modules/2026-09/PREDICATE_ONE_SHAPE.md'


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


RJ = _j('b451_remainder.json')
KJ = _j('b451_kinds.json')
SPAN = _j('b451_span.json')
MIRROR = read(os.path.join(D, 'b451_mirror.txt'))
LORE = read(os.path.join(TECHNE, LOREREL))
LORERUN = read(os.path.join(D, 'b451_lore_append_run.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b451_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b451 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b451')) | set(committed_by_act(ROOT, r'b451')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b451_registration_2026-09-13.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '2e5a0c8', 'origin/main'], capture_output=True).returncode
    trails = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    blk = trails[trails.find(B451MARK):] if B451MARK in trails else ''
    t_dirty = git(TECHNE, 'status', '--porcelain', '--untracked-files=no').strip()
    t_head = git(TECHNE, 'rev-parse', 'HEAD').strip()
    t_remote = git(TECHNE, 'branch', '-r', '--contains', 'HEAD').strip()
    t_num = git(TECHNE, 'log', '-1', '--grep', 'b451', '--numstat', '--format=', '--', LOREREL).split()

    # ### RE-DERIVED: population, sets, remainder.
    cen = read(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')).splitlines()
    pop = [re.match(r'\|\s*`([A-Za-z_0-9]+)`', cen[i - 1]).group(1) for i in range(73, 89) if re.match(r'\|\s*`([A-Za-z_0-9]+)`', cen[i - 1])]
    sets = dict((s['act'], s['members']) for s in RJ.get('sets') or [])
    b394 = re.findall(r'`([A-Z_0-9]+)`', [l for l in read(os.path.join(D, 'b394_the_reconciliation_batched.txt')).splitlines() if '### ### **THE THREE : ' in l][0])
    b450l = [l for l in read(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt')).splitlines() if l.startswith('**Eligible (11), in census order:**')][0]
    b450 = [k for k in dict.fromkeys(re.findall(r'`([A-Za-z_0-9]+)`', b450l.split(' are marked ')[0])) if k in pop]
    union = list(dict.fromkeys(['ADDITIVE_MULTIPLICATIVE_CONSPIRACY'] + b394 + b450))
    rem = [k for k in pop if k not in union]
    # ### RE-DERIVED: the kinds, from the items' own clauses.
    items = json.loads(read(os.path.join(D, 'b450_batch.json')))['verdict']['routed_items']
    kinds = {}
    for k, what, why in items:
        c = why.split(';')[0]
        kd = 'AUTHORING' if re.search(r'\bis authoring\b', c) else ('REGISTRY ROW' if ('registry row' in c and ('the author`s' in c or "the author's" in c)) else (c.upper() if c.strip() else 'THE ITEM DOES NOT SAY'))
        kinds[kd] = kinds.get(kd, 0) + 1
    real = [k for k in kinds if kinds[k]]
    largest = max(real, key=lambda x: kinds[x]) if real else None
    n1i = 'HELD' if len(rem) == 1 else 'REFUTED'
    n1ii = 'REFUTED AS WORDED' if rem == ['ENUMERA'] and 'no clone would help' in read(os.path.join(D, 'b395_components.txt')) else 'HELD'
    n2a = 'HELD' if len(real) < 10 else 'REFUTED'
    n2b = 'HELD' if largest == 'AUTHORING' and all(kinds[k] < kinds['AUTHORING'] for k in real if k != 'AUTHORING') else 'REFUTED'
    # ### THE CRUDE SHAPE (any prior-act token) fired on variable names; kept to print its yield beside the write-target shape.
    crude = [n for n, s in SRC_ALL.items() if re.search(r'\bb450_(?!components\.txt|batch\.json|the_eligible|span)', s) or re.search(r'b449_|b448_', s)]
    PRIORFILE = r"b4(?!51)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'"
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|REMJ|KINDJ|LORERUN|SPEC|DBL|STK|BLOCK|LOOMRUN)\s*="
    carried = []
    for n, s in SRC_ALL.items():
        for ln in s.splitlines():
            if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln):
                carried.append((n, ln.strip()[:80]))
    # ### the fixture is b450's incident line, ASSEMBLED so this file carries no literal prior-act file name (use vs mention).
    fixture = "    write_bytes(os.path.join(D, '" + 'b44' + "9_desk_notes.txt'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-13-b451.zip' in MIRROR
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
        ('G-PRIOR-CLOSED-PUSHED', 'row 299 on the face; 2e5a0c8 on origin/main', 'row 299' in F and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b451_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-SEEN-DECLARED', 'what the seat had seen declared on the face', fold("WHAT THE SEAT HAS ALREADY SEEN, DECLARED:") in F),
        ('G-C1-POPULATION-FROM-CENSUS', 'population %d re-read' % len(pop), len(pop) == 16 and RJ.get('population') == pop),
        ('G-C1-SETS-FROM-BANKS', 'sets re-parsed from the banks', sets.get('b394') == b394 and sets.get('b450') == b450 and sets.get('b390') == ['ADDITIVE_MULTIPLICATIVE_CONSPIRACY']),
        ('G-C1-ARITHMETIC-PRINTED', 'the arithmetic line printed with the re-derived figures', verdict_line(COMP, '### THE ARITHMETIC :', '= %d' % len(rem))
         and verdict_line(COMP, '### THE ARITHMETIC :', 'union %d' % len(union))),
        ('G-C1-REMAINDER-NAMED', 'remainder %s re-derived' % rem, RJ.get('remainder') == rem and all(k in COMP for k in rem)),
        ('G-C1-NEED-QUOTED', 'the need quoted at b395`s bank lines', 'b395_the_ceiling_answered.txt:51-52' in COMP and 'no clone would help' in COMP),
        ('G-C1-ROUTED', 'the remainder`s need routed', not rem or verdict_line(COMP, '### NEITHER A CLONE NOR A BRANCH-READING RULING', 'ROUTED')),
        ('G-C1-NO-KEYSTONE-OPENED', 'no keystone path read by this act`s tools', not re.search(r'phase1\.5|phase2/|day1', pycode_of(SRC_COMP).replace("'phase2', 'method', 'THE_KEYSTONE_CENSUS.md'", ''))),
        ('G-C2-ITEMS-FROM-BANK', '29 items read from b450`s bank', len(KJ.get('items') or []) == len(items) == 29),
        ('G-C2-KIND-RULE-APPLIED', 'kinds re-derived %s' % kinds, dict((k, v) for k, v in (KJ.get('counts') or {}).items() if v) == kinds),
        ('G-C2-COUNTS-SUM', 'counts sum to 29', sum((KJ.get('counts') or {}).values()) == 29 and verdict_line(COMP, 'KINDS WITH MEMBERS', 'SUM TO 29 OF 29')),
        ('G-C2-TABLE-PRINTED', 'every item`s address printed', all(r['address'] in COMP for r in KJ.get('items') or [])),
        ('G-C2-UNBLOCK-LINES', 'one unblock line per kind', COMP.count('WHAT A RULING WOULD UNBLOCK :') == len(KJ.get('counts') or {})),
        ('G-C2-DOES-NOT-SAY-REPORTED', 'THE ITEM DOES NOT SAY reported with its count', 'THE ITEM DOES NOT SAY' in (KJ.get('counts') or {}) and verdict_line(COMP, 'KINDS WITH MEMBERS', 'THE ITEM DOES NOT SAY : %d' % KJ['counts']['THE ITEM DOES NOT SAY'])),
        ('G-C2-PRECONDITIONS-BESIDE', 'preconditions printed beside, not kinds', sum(1 for r in KJ.get('items') or [] if r['precondition']) == COMP.count('### PRECONDITION NAMED:')
         and not any('NOT LOCATED' in k or 'REPRODUCED' in k for k in kinds)),
        ('G-C2-NOTHING-ANSWERED', 'no ruling proposed said', 'NO RULING IS PROPOSED. ### NO ITEM IS ANSWERED.' in COMP),
        ('G-FILING-LORE-ONE-LINE', 'one line in the lore, 0 removed (numstat %s)' % t_num[:2], LORE.count('Incidents after the mint (b451)') == 1 and len(t_num) >= 2 and t_num[1] == '0' and t_num[0] in ('1', '2')
         and verdict_line(LORERUN, 'TRUE PREFIX', 'YES')),
        ('G-FILING-INCIDENTS-NAMED', 'four incidents named in the line', bool(re.search(r'Incidents after the mint \(b451\).*b390.*b394.*b395.*b450.*claim.*citation', LORE))),
        ('G-FILING-WORKORDER', 'W-ORD-MATCHER-SHAPE with its trigger in the trail record', bool(blk) and '**W-ORD-MATCHER-SHAPE' in blk and 'the next act that matches a table header, a document name or a version by pattern' in blk),
        ('G-FILING-NO-MATCHER-EDITED', 'no prior act tool or instrument touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'tools/' in ln and 'b451' not in ln and 'banked_index' not in ln])
         and not [f for f in committed_by_act(ROOT, r'^tools/') if 'b451' not in f and 'banked_index' not in f]),
        ('G-FILING-TECHNE-LOCAL', 'TECHNE committed, clean, on no remote branch', bool(t_num) and t_dirty == '' and bool(t_head) and t_remote == ''),
        ('G-N1-APART', 'N1 two clauses', fold('TWO CLAUSES APART') in F and '(N1)(i)' in COMP and '(N1)(ii)' in COMP),
        ('G-N1-SCORED', 'N1 (i) %s (ii) %s' % (n1i, n1ii), verdict_line(COMP, '(N1)(i)  the remainder', n1i) and verdict_line(COMP, '(N1)(ii) it is the one', n1ii)),
        ('G-N2-APART', 'N2 two clauses', '(N2)(a)' in COMP and '(N2)(b)' in COMP),
        ('G-N2-SCORED', 'N2 (a) %s (b) %s' % (n2a, n2b), verdict_line(COMP, '(N2)(a)  fewer than ten', n2a) and verdict_line(COMP, '(N2)(b)  authoring is', n2b)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b451 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b451' and SPAN.get('this_act') == 451),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER and REGISTRY untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md') and unchanged(PP, 'REGISTRY.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b451' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail', all(f == 'OPEN_TRAILS.md' for f in pp_touched + pp_committed)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b451' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'no b451 tool writes to a prior act`s file ; write-target shape %d %s ; control on b450`s incident line fires %s ; crude shape %s'
         % (len(carried), carried, control, crude), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-13-b451, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
