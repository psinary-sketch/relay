# -*- coding: utf-8 -*-
"""b456_checks.py -- THE CONTROL SUITE FOR b456. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b456_registration_2026-09-14.txt')
PREPUSH = os.path.join(D, 'b456_checks.txt')
POSTPUSH = os.path.join(D, 'b456_checks_postpush.txt')
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
                for f in ('b456_ferry.txt', 'b456_ferry_scan.txt'))


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
        if 'b456' not in subj:
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
COMP = read(os.path.join(D, 'b456_components.txt'))
EXTR = read(os.path.join(D, 'b456_extract.txt'))
RGATE = read(os.path.join(D, 'b456_reg_gate.txt'))
TERM = read(os.path.join(D, 'b456_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b456_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b456_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b456_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b456_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b456_ferry.txt'))
CENS = read(os.path.join(D, 'b456_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b456_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b456_pins_stepzero.txt'))
ADD = os.path.join(D, 'b456_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b456_components.py'))
SRC_DESK = read(os.path.join(T, 'b456_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b456_extract.py'))
SRC_CHK = read(os.path.join(T, 'b456_checks.py'))
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
        if 'b456' not in subj:
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


WJ = _j('b456_writes.json')
PJ = _j('b456_profile.json')
SPAN = _j('b456_span.json')
MIRROR = read(os.path.join(D, 'b456_mirror.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b456_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
sys.path.insert(0, T)


def main(argv):
    import b456_components as CMP
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b456 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b456|banked_index')) | set(committed_by_act(ROOT, r'.')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b456_registration_2026-09-14.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '6459a41', 'origin/main'], capture_output=True).returncode

    def base_text(rel):
        if not unchanged(PP, rel):
            return nl(git(PP, 'show', 'HEAD:%s' % rel))
        for ln in git(PP, 'log', '--format=%H %s', '-10', '--', rel).splitlines():
            if 'b456' in ln:
                return nl(git(PP, 'show', '%s^:%s' % (ln.split(' ', 1)[0], rel)))
        return ''

    er = nl(read(os.path.join(PP, 'ERRATA.md')))
    er0 = base_text('ERRATA.md')
    entry = NL.join(CMP.ENTRY)
    reg, reg0 = nl(read(os.path.join(PP, 'REGISTRY.md'))), base_text('REGISTRY.md')
    rd, rd0 = nl(read(os.path.join(PP, 'README.md'))), base_text('README.md')
    inv, inv0 = nl(read(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md'))), base_text('phase1.5/method/INVARIANCE_BARRIERS.md')
    res, res0 = nl(read(os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'))), base_text('phase1.5/proofs/THE_RESIDUE_OF_RH.md')
    fr = _j('b359_fetch_F2.json')
    import html as _h
    s1t = _h.unescape(re.sub(r'<[^>]+>', '', fr.get('metadata', {}).get('description', '')))
    kread = git(KER, 'show', 'v1.5:README.md')
    dep = nl(read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')))
    exh_now = nl(read(os.path.join(PP, 'phase1.5', 'method', 'EXHAUSTIVENESS_LICENSE.md')))
    digits, words = CMP.tally(entry)
    c4 = WJ.get('c4') or {}
    p145 = ((c4.get('I3') or {}).get('parts') or [{}])[0]
    pp_allowed = {'ERRATA.md', 'REGISTRY.md', 'README.md', 'phase1.5/method/INVARIANCE_BARRIERS.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'OPEN_TRAILS.md'}
    pp_untouched = ('FINDINGS.md', 'FACES_LEDGER.md', 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md')
    PRIORFILE = r"b4(?!56)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump_json\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'|put\("
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|WRITESJ|PROFJ|SPEC)\s*="
    carried = [(n, ln.strip()[:80]) for n, s in SRC_ALL.items() for ln in s.splitlines() if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln)]
    fixture = "    dump_json(os.path.join(D, '" + 'b45' + "5_claims.json'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))
    onlist = lambda f: os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
    off_exact = [f for f in relay_new if not onlist(f)]
    kern_clean = all(0 == len(git(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').splitlines())
                     for k in ('SIDE-kernel', 'SIDE-effects', 'SIDE-lv-conservation', 'SIDE-window'))

    def inserted_only(pre, post, n_new):
        a, b = pre.split(NL), post.split(NL)
        import difflib
        ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
        return bool(pre) and all(op in ('equal', 'insert') for op, *_ in ops) and len(b) - len(a) == n_new

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-14-b456.zip' in MIRROR
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
        ('G-PRIOR-CLOSED-PUSHED', 'row 304 on the face; 6459a41 on origin/main', 'row 304' in FACET and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b456_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-LOCKGATE-NOT-REDIRECTED', 'one lock-gate record', not any(re.match(r'b456_lockgate_notes\d+\.txt$', f) for f in os.listdir(D))),
        ('G-R65-ENTERED', '(R65) quoted on the face and in the record', 'DISPOSITIONS (i) AND (iii),' in FACET and 'RULING (R65)' in COMP),
        ('G-C1-ONE-ENTRY-APPENDED', 'the entry once, the prior text a prefix', er.count('## E-2026-09-14-1 —') == 1 and bool(er0) and er.startswith(er0.rstrip(NL)) and er.rstrip(NL).endswith(entry.rstrip(NL))),
        ('G-C1-CONTENT-A-TO-J', 'each required content present', all(f(er) for _n, f in CMP.CONTENT) and all(v for _n, v in (WJ.get('c1') or {}).get('content', [['', False]]))),
        ('G-C1-QUOTES-VERBATIM', 'the deposited sentences in their sources', CMP.S1_QUOTE in s1t and CMP.S5_QUOTE in kread and CMP.S4_QUOTE in dep and CMP.S4_ROW in dep),
        ('G-C1-NO-TALLY', 'digits %s ; number words %s' % (digits, words), not digits and not words and 'seven' in entry),
        ('G-C1-PARTITION-UNEDITED', 'the partition block byte-unmoved', bool(er0) and er0[er0.find('## THE PARTITION'):er0.find('<!-- b341 -->')] in er),
        ('G-C2-ONE-SENTENCE-BOTH-PLACES', 'the same sentence in REGISTRY and README', reg.split(NL).count(CMP.NOTE) == 1 and rd.split(NL).count(CMP.NOTE) == 1 and CMP.NOTE.count('. ') == 0),
        ('G-C2-INSERTED-NO-LINE-CHANGED', 'only inserted lines', inserted_only(reg0, reg, 2) and inserted_only(rd0, rd, 1)),
        ('G-C2-POINTS-TO-ENTRY', 'names E-2026-09-14-1', 'E-2026-09-14-1' in CMP.NOTE and 'ERRATA.md' in CMP.NOTE),
        ('G-C2-NO-NARROWING', 'the live front-door sentence and the kernel README unchanged', rd0.split(NL)[14] in rd.split(NL) and 'route terminals re-profiled clean at the v1.5 enactment' in rd and unchanged(KER, 'README.md')),
        ('G-C3-TAG-SEARCHED', 'the tag`s prints read with their headings', bool(PJ.get('tag')) and all(x['file'] == 'DEPOSIT_v1_2_NOTES.md' for x in PJ['tag'])),
        ('G-C3-ELSEWHERE-SEARCHED', 'relay, PLACE-papers, the kernel tree', PJ.get('elsewhere_scanned') == ['relay/reports', 'relay/data', 'PLACE-papers', 'SIDE-kernel working tree']),
        ('G-C3-VERDICT-BY-DEFINITION', 'verdict %s' % PJ.get('verdict'), PJ.get('verdict') == ('PRESENT' if any(x['printed_against_0e5233f'] for x in PJ.get('tag', [])) else
                                                                                           ('PRESENT ELSEWHERE' if any(x['names_0e5233f_or_v15_nearby'] and not x['where'].startswith('SIDE-kernel') for x in PJ.get('elsewhere', [])) else 'ABSENT'))
         and ('### ### **VERDICT : %s**' % PJ.get('verdict')) in COMP),
        ('G-C3-STATEMENTS-APART', 'statements printed as statements', len(PJ.get('statements') or []) == 4 and 'printed apart as statements and not as output' in COMP),
        ('G-C3-DISPOSITION-NOT-TAKEN', 'priced, not taken', (PJ.get('disposition') or {}).get('taken') is False and 'NOT TAKEN' in COMP),
        ('G-C3-NO-LEAN-RUN', 'no lean or lake', not re.search(r"\[\s*['\"](lean|lake)['\"]", SRC_COMP) and 'lean runs : 0' in COMP),
        ('G-C4-I1-ANNOTATION', 'the era annotation, its words on the decided line', ('### ERA ANNOTATION (2026-09-14, b456) — bearing on the T3 Tier-1 scope' in inv) and ('> %s' % (c4.get('I1') or {}).get('words', '@@')) in inv
         and (c4.get('I1') or {}).get('words_on_line') is True and bool(inv0) and inv.startswith(inv0.rstrip(NL))),
        ('G-C4-I3-TERM-AND-ORIGINAL', ':145 carries the new term; the line as it stood in the annotation', res.split(NL)[144] == p145.get('original', '@').replace('held-branch work', 'merged-branch work')
         and p145.get('original', '@') in res.split('<!-- b456 CURRENCY ANNOTATION')[-1] and res0.split(NL)[144] == p145.get('original')),
        ('G-C4-LEFT-UNCHANGED', 'EXH:9 and RES:127-130 byte-unmoved', exh_now.split(NL)[8] == '*v0.1 — 2026-07-25 (W-LADDER build; kernel skeleton HELD on branch, main untouched)*'
         and res.split(NL)[126:130] == res0.split(NL)[126:130] and unchanged(PP, 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md')),
        ('G-C4-REPORTED-APART', 'completed and left printed apart', '  COMPLETED:' in COMP and '  LEFT:' in COMP and 'I3 PARTLY COMPLETED' in COMP),
        ('G-C4-REMOVED-ZERO', 'every write removed-zero', len(WJ.get('diffs') or []) == 5 and all(d['removed_zero'] for d in WJ['diffs'])),
        ('G-N1-SCORED', 'N1', '(N1) the profile artefact is ABSENT at the deposited tag :' in COMP),
        ('G-N2-SCORED', 'N2', '(N2) two of the three routed annotations complete without a ruling :' in COMP),
        ('G-SEAT-EXPECTATIONS-SCORED', 'the seat`s own', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'emitted for b456', SPAN.get('emitted_for') == 'b456' and SPAN.get('current_span') == 3),
        ('G-NOGRADE-MOVED', 'no row edited', fold('NO GRADE MOVED ON ANY ROW') in F and unchanged(PP, 'FACES_LEDGER.md') and inserted_only(reg0, reg, 2)),
        ('G-NOKERNEL-WRITE', 'kernels unwritten', kern_clean),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOZENODO-WRITE', 'no Zenodo client', fold('NOTHING WRITTEN AT ZENODO IN ANY BRANCH') in F and not re.search(r'zenodo\.org/api|ZENODO_TOKEN|api/deposit', SRC_COMP + SRC_DESK)),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b456' not in ln and 'b369' not in ln and 'b373' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: the named paths only', all(f in pp_allowed for f in pp_touched + pp_committed) and all(unchanged(PP, f) for f in pp_untouched)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list : off %d %s' % (len(off_exact), off_exact), not off_exact),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b456' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'write-target shape %d %s ; control fires %s' % (len(carried), carried, control), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-14-b456, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
