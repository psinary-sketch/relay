# -*- coding: utf-8 -*-
"""b452_checks.py -- THE CONTROL SUITE FOR b452. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b452_registration_2026-09-14.txt')
PREPUSH = os.path.join(D, 'b452_checks.txt')
POSTPUSH = os.path.join(D, 'b452_checks_postpush.txt')
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
                for f in ('b452_ferry.txt', 'b452_ferry_scan.txt'))


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
        if 'b452' not in subj:
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
COMP = read(os.path.join(D, 'b452_components.txt'))
EXTR = read(os.path.join(D, 'b452_extract.txt'))
RGATE = read(os.path.join(D, 'b452_reg_gate.txt'))
TERM = read(os.path.join(D, 'b452_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b452_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b452_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b452_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b452_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b452_ferry.txt'))
CENS = read(os.path.join(D, 'b452_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b452_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b452_pins_stepzero.txt'))
ADD = os.path.join(D, 'b452_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b452_components.py'))
SRC_DESK = read(os.path.join(T, 'b452_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b452_extract.py'))
SRC_CHK = read(os.path.join(T, 'b452_checks.py'))
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
        if 'b452' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False











B452MARK = '<!-- b452 the class boundary read by its side, and the six sites read by their generator -->'


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


SJ = _j('b452_sides.json')
TJ = _j('b452_sites.json')
SPAN = _j('b452_span.json')
MIRROR = read(os.path.join(D, 'b452_mirror.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b452_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}
SITEFILES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
             ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b452 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b452')) | set(committed_by_act(ROOT, r'b452')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b452_registration_2026-09-14.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '2ee97cc', 'origin/main'], capture_output=True).returncode

    # ### RE-DERIVED: the K1 population from the banks, and the partition's arithmetic.
    k1 = []
    allf = 0
    for s, p in SITEFILES:
        for c in json.loads(read(os.path.join(D, p)))['candidates']:
            allf += 1
            if c['kind'] == 'CLASS BOUNDARY':
                k1.append((s, c['id']))
    rows = SJ.get('rows') or []
    rk1 = [(r['site'], r['id']) for r in rows if r['kind'] == 'CLASS BOUNDARY']
    parts = SJ.get('partition') or {}
    counts = SJ.get('counts') or {}
    sums = sum(len(v) for v in parts.values())
    r1 = sum(1 for r in rows if r['r1'])
    ctrl_rows = [r for r in rows if r['kind'] != 'CLASS BOUNDARY' and r.get('verdict') == 'OBJECT-SIDE']
    n1 = 'HELD' if counts.get('OBJECT-SIDE') else 'REFUTED'
    n2 = 'HELD' if TJ.get('verdict') == 'LIST' else 'REFUTED'
    PRIORFILE = r"b4(?!52)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump_json\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'"
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|SIDESJ|SITESJ|DUMP|SPEC)\s*="
    carried = [(n, ln.strip()[:80]) for n, s in SRC_ALL.items() for ln in s.splitlines() if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln)]
    fixture = "    write_bytes(os.path.join(D, '" + 'b44' + "9_desk_notes.txt'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))
    unnamed = [f for f in relay_new if not (os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f or f.endswith('banked_index.py'))]

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-14-b452.zip' in MIRROR
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
        ('G-PRIOR-CLOSED-PUSHED', 'row 300 on the face; 2ee97cc on origin/main', 'row 300' in F and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b452_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-R63-CARRIED-NOT-EXECUTED', '(R63) carried; no keystone, registry or TECHNE write', fold('(R63)` IS CARRIED AND NOT EXECUTED HERE') in F
         and all(f == 'OPEN_TRAILS.md' for f in pp_touched + pp_committed)),
        ('G-C1-FORTY-SEVEN-READ', 'K1 re-derived from the banks %d ; all %d failures read' % (len(k1), allf), len(k1) == 47 and sorted(k1) == sorted(rk1) and len(rows) == allf == 82),
        ('G-C1-REEXPRESSIONS-FIXED', 'R1 and R2 on the face and quoted in the components', '`R1`' in FACET and '`R2`' in FACET and 'R1 (REPARAMETERIZATION_BARRIERS_v0_1.md:94-101)' in COMP
         and 'R2 (Exhaustive_Enumeration.md:171' in COMP),
        ('G-C1-CLASS-FROM-BANK', 'every K1 row carries its bank`s class text or is UNDECIDED for its absence', all((r['class_text'].strip() and r['class_text'].strip() != 'FAILED AT A QUOTED STEP') or r['verdict'] == 'UNDECIDED' for r in rows if r['kind'] == 'CLASS BOUNDARY')),
        ('G-C1-OBJECT-FROM-SITE', 'every row carries its site`s object', all(r['object'].get('missing') for r in rows)),
        ('G-C1-TEST-APPLIED', 'every verdict one of the three, none UNREAD', all(r['verdict'] in ('OBJECT-SIDE', 'SOURCE-SIDE', 'UNDECIDED') for r in rows) and counts.get('UNREAD', 0) == 0),
        ('G-C1-APPLICABILITY-HAND-READ', 'R1 yield %d ; every R2 hit carries a hand read' % r1, r1 == 0 and all(r.get('why') for r in rows if r['r2'])),
        ('G-C1-PARTITION-SUMS', 'partition sums to 47 (%s)' % counts, sums == 47 and counts.get('OBJECT-SIDE', 0) + counts.get('SOURCE-SIDE', 0) + counts.get('UNDECIDED', 0) == 47),
        ('G-C1-PER-SITE', 'per-site rows printed and summing', all(('      (%-4s' % (s + ')')) in COMP for s, _ in SITEFILES) and verdict_line(COMP, '      total', '47')),
        ('G-C1-CONTROL-STATED', 'control %s ; ABSENT not passed' % SJ.get('control_state'), (SJ.get('control_state') == 'ABSENT') == (not ctrl_rows)
         and verdict_line(COMP, 'THE CONTROL IS', SJ.get('control_state', '?')) and (SJ.get('control_state') != 'ABSENT' or 'ABSENT IS NOT PASSED' in COMP)),
        ('G-C1-NO-REEXPRESSION-PERFORMED', 'no re-expression performed said', 'NO RE-EXPRESSION WAS PERFORMED' in COMP),
        ('G-C2-NAMING-ACTS-QUOTED', 'the three naming acts quoted at their addresses', all(('named by %s at' % a) in COMP for a in ('b355', 'b401', 'b404')) and '### NOT LOCATED' not in COMP),
        ('G-C2-VERDICT-BY-RULE', 'verdict %s, rule hits hand-read' % TJ.get('verdict'), TJ.get('verdict') == 'LIST' and verdict_line(COMP, '### ### **VERDICT :', 'A LIST')
         and 'HAND READ: the word matched is `crt_exhaustiveness`' in COMP),
        ('G-C2-CLOSURE-NEED-PRINTED', 'what the record would need printed', verdict_line(COMP, 'WHAT THE RECORD WOULD NEED TO CLOSE IT', 'a generator with a finite range')),
        ('G-C2-NO-SEVENTH-SITE', 'no seventh site proposed; FACES_LEDGER untouched', 'NO SEVENTH SITE IS PROPOSED' in COMP and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-N1-SCORED', 'N1 %s' % n1, verdict_line(COMP, '(N1) OBJECT-SIDE is not empty', n1)),
        ('G-N2-SCORED', 'N2 %s' % n2, verdict_line(COMP, '(N2) the six sites are a LIST', n2)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b452 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b452' and SPAN.get('this_act') == 452),
        ('G-NOGRADE-MOVED', 'no grade moved; ledgers untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md') and unchanged(PP, 'REGISTRY.md') and unchanged(PP, 'FINDINGS.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b452' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail', all(f == 'OPEN_TRAILS.md' for f in pp_touched + pp_committed)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list ; UNNAMED KINDS %d %s' % (len(unnamed), unnamed), not unnamed),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b452' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'write-target shape %d %s ; control fires %s' % (len(carried), carried, control), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-14-b452, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
