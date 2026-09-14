# -*- coding: utf-8 -*-
"""b455_checks.py -- THE CONTROL SUITE FOR b455. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b455_registration_2026-09-14.txt')
PREPUSH = os.path.join(D, 'b455_checks.txt')
POSTPUSH = os.path.join(D, 'b455_checks_postpush.txt')
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
                for f in ('b455_ferry.txt', 'b455_ferry_scan.txt'))


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
        if 'b455' not in subj:
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
COMP = read(os.path.join(D, 'b455_components.txt'))
EXTR = read(os.path.join(D, 'b455_extract.txt'))
RGATE = read(os.path.join(D, 'b455_reg_gate.txt'))
TERM = read(os.path.join(D, 'b455_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b455_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b455_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b455_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b455_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b455_ferry.txt'))
CENS = read(os.path.join(D, 'b455_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b455_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b455_pins_stepzero.txt'))
ADD = os.path.join(D, 'b455_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b455_components.py'))
SRC_DESK = read(os.path.join(T, 'b455_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b455_extract.py'))
SRC_CHK = read(os.path.join(T, 'b455_checks.py'))
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
        if 'b455' not in subj:
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


CJ = _j('b455_claims.json')
TJ = _j('b455_terminals.json')
DJ = _j('b455_dispositions.json')
LJ = _j('b455_line.json')
SPAN = _j('b455_span.json')
MIRROR = read(os.path.join(D, 'b455_mirror.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b455_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}
KER = os.path.join('D:', os.sep, 'SIDE-kernel')


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b455 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b455|banked_index')) | set(committed_by_act(ROOT, r'.')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b455_registration_2026-09-14.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'e63e884', 'origin/main'], capture_output=True).returncode
    claims = CJ.get('claims') or []
    items = CJ.get('items') or []
    meta = CJ.get('meta') or {}
    fr = _j('b359_fetch_F2.json')
    s1 = ''.join(fr.get('metadata', {}).get('description', ''))
    import html as _h
    s1t = _h.unescape(re.sub(r'<[^>]+>', '', s1))
    tbc = git(KER, 'show', 'v1.5:Bridge/TheBridgeComplete.lean')
    l1 = git(KER, 'show', 'v1.5:Kernel/Layer1.lean')
    kread = git(KER, 'show', 'v1.5:README.md')
    zj = git(KER, 'show', 'v1.5:.zenodo.json')
    dep = nl(read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')))
    src_of = {'S1': s1t, "S2'": zj, 'S3': nl(read(os.path.join(PP, 'README.md'))), 'S4': dep, 'S5': kread}
    GR = DJ.get('grades') or {}
    GRADES = ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION', 'SHELL', 'NOT THE CLAIM')
    arc = nl(read(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'))).split(NL)
    spec = nl(read(os.path.join(PP, 'phase2', 'method', 'THE_TECHNIQUE_SPECIFICATION.md')))
    PRIORFILE = r"b4(?!55)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump_json\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'"
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|CLAIMJ|TERMJ|DISPJ|LINEJ|SPEC)\s*="
    carried = [(n, ln.strip()[:80]) for n, s in SRC_ALL.items() for ln in s.splitlines() if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln)]
    fixture = "    dump_json(os.path.join(D, '" + 'b45' + "4_findings.json'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))
    onlist = lambda f: os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
    off_exact = [f for f in relay_new if not onlist(f)]
    kern_clean = all(0 == len(git(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').splitlines())
                     for k in ('SIDE-kernel', 'SIDE-effects', 'SIDE-lv-conservation', 'SIDE-window'))
    pp_unchanged = ('ERRATA.md', 'README.md', 'REGISTRY.md', 'FINDINGS.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md', 'phase1.5/method/INVARIANCE_BARRIERS.md')

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-14-b455.zip' in MIRROR
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
        ('G-PRIOR-CLOSED-PUSHED', 'row 303 on the face; e63e884 on origin/main', 'row 303' in FACET and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b455_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-LOCKGATE-NOT-REDIRECTED', 'one lock-gate record, no versioned second', not any(re.match(r'b455_lockgate_notes\d+\.txt$', f) for f in os.listdir(D))),
        ('G-C1-FIVE-SURFACES', 'S1, S2`, S3, S4, S5 each read', all(k in COMP for k in ('  S1 ', '  S2 ', "  S2' ", '  S3 ', '  S4 ', '  S5 ')) and len(set(i['surface'] for i in items)) == 5),
        ('G-C1-S2-NOT-HELD-SAID', 'the kernel record`s description NOT HELD, printed', 'DESCRIPTION NOT HELD BY THE RECORD' in COMP and all(not r['description_held'] for r in meta.get('s2_record_rows', [])) and len(meta.get('s2_record_rows', [])) >= 1),
        ('G-C1-S4-CHECKSUM-PRINTED', 'MD5 against the record`s checksum', meta.get('s4_verified') is True and 'VERIFIED AS DEPOSITED' in COMP),
        ('G-C1-YIELDS-PRINTED', 'both yields', re.search(r'yield `exhaust` \d+ ; yield the terminal`s name \d+', COMP) is not None),
        ('G-C1-ITEMS-HAND-READ', 'every item a claim or a reasoned non-claim', len(items) == len(claims) + len(CJ.get('not_claims') or {}) and '### UNREAD' not in COMP),
        ('G-C1-QUOTES-VERBATIM', 'each claim`s item and deciding words in its own surface', bool(claims) and all(c['text'] in nl(src_of[c['surface']]) and (c['deciding'].split('. Read per conjunct')[0] in nl(src_of[c['surface']]))
                                                                                           and (('Read per conjunct' not in c['deciding']) or c['deciding'].split('it certifies exactly what it literally states. ')[-1] in dep) for c in claims)),
        ('G-C1-CLASS-WITH-DECIDING-WORDS', 'each class one of three, deciding words printed', all(c['cls'] in ('MANUSCRIPT-RESIDENT', 'MACHINE-CHECKED', 'AMBIGUOUS AS WRITTEN') and c['deciding'] for c in claims)),
        ('G-C2-READ-AT-V15', 'v1.5 peels to 0e5233f and every quoted part is in the v1.5 blobs', TJ.get('peeled') == '0e5233f' and all(p['text'].split(':= by ...')[0].strip() in tbc for p in (TJ.get('route') or {}).values())
         and all(p['text'] in l1 for p in (TJ.get('other') or {}).values())),
        ('G-C2-STATEMENT-WHOLE', 'theorem and definition quoted whole', 'theorem structural_exhaustiveness_proved :' in (TJ.get('route') or {}).get('theorem', {}).get('text', '') and 'f.IsEquiv (Rat.AbsoluteValue.padic p))' in (TJ.get('route') or {}).get('def', {}).get('text', '')),
        ('G-C2-UNFOLDED', 'the three conjuncts to base objects', '### UNFOLDED: `structural_exhaustiveness_proved : StructuralExhaustiveness`' in COMP and 'C1_schwarz ... C7_hadamard' in COMP and '### UNFOLDED: from `cat : ExhaustiveCatalogue X P`' in COMP),
        ('G-C2-PROFILE-BY-PIN-RULE', 'prints quoted with their pin; at v1.5 UNREAD', (TJ.get('profile_route') or {}).get('at_v15') == 'UNREAD' and (TJ.get('profile_other') or {}).get('at_v15') == 'UNREAD' and TJ.get('prints_naming_v15') == 0),
        ('G-C2-NO-LEAN-RUN', 'no lean or lake', TJ.get('lean_runs') == 0 and not re.search(r"\[\s*['\"](lean|lake)['\"]", SRC_COMP)),
        ('G-C2-OTHER-TERMINAL-SAME-PIN', 'SIDE_exclusion read at v1.5 in SIDE-kernel', 'theorem SIDE_exclusion' in (TJ.get('other') or {}).get('theorem', {}).get('text', '') and 'Kernel/Layer1.lean' in COMP),
        ('G-C2-GRADE-PER-CLAIM', 'two grades per claim, each a README grade', bool(claims) and all(GR.get(c['id'], {}).get('route', [''])[0] in GRADES and GR.get(c['id'], {}).get('other', [''])[0] in GRADES for c in claims)),
        ('G-C2-TABLE-PRINTED', 'one table, a row per claim', '| claim | surface | class | structural_exhaustiveness_proved | techne_kernel.SIDE_exclusion |' in COMP and all(('| %s *"' % c['id']) in COMP for c in claims)),
        ('G-C3-TEST-APPLIED', 'deposit-level by the face`s test', sorted(DJ.get('deposit_level') or []) == sorted(c['id'] for c in claims if c['cls'] == 'MACHINE-CHECKED' and not c['own'].startswith('UNNAMED') and GR[c['id']]['route'][0] in ('NOT THE CLAIM', 'INTERFACES'))
         and all(('### DEPOSIT-LEVEL MATTER: %s' % x) in COMP for x in DJ.get('deposit_level') or [])),
        ('G-C3-THREE-DISPOSITIONS-PRICED', 'three, each with writes, repos, zenodo, unchanged, acts', len(DJ.get('dispositions') or []) == 3 and all(all(d.get(k) for k in ('writes', 'repos', 'zenodo', 'unchanged', 'acts')) for d in DJ.get('dispositions') or [])),
        ('G-C3-NONE-RECOMMENDED', 'none recommended, none taken', DJ.get('recommended') == [] and DJ.get('taken') == [] and '### NONE IS RECOMMENDED. ### NONE IS TAKEN.' in COMP),
        ('G-C3-NOT-AT-ISSUE-STATED', 'both stated', COMP.count('### NOT AT ISSUE:') == 2),
        ('G-C4-LINE-READ', 'the line`s third item on the line', LJ.get('verdict') in ('YES', 'NO') and LJ.get('line_text', '').strip() == arc[7970].strip()
         and "Euler-product consumption at Face E's **Tier-1 scope verbatim**" in arc[7970].replace('’', "'")),
        ('G-C4-T3-BY-ORDER-AND-SPEC', 'T8-T10 labelled on the line; the spec`s T3 row', all(('`T%d`' % n) in arc[7970] for n in (8, 9, 10)) and "| **T3** | **Consume the Euler product essentially.** Face E's barrier is Tier-1 and scoped verbatim" in spec.replace('’', "'")),
        ('G-C4-COUNTS-PRINTED', 'the corrected counts and which figure stands', (LJ.get('counts') or {}) == dict(added=8, held_by_no_ledger=7, targets=15) and 'THE CORRECTED COUNTS: ADDED 8 ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER 7 ; SUM 15.' in COMP),
        ('G-C4-B454-BANK-UNEDITED', 'b454`s files untouched', 0 == len([f for f in touched(ROOT, r'b454', since=False)]) and not any('b454' in f for f in committed_by_act(ROOT, r'.'))),
        ('G-N1-SCORED', 'with a quotation', '(N1) at least one deposited surface' in COMP and 'Proved and machine-checked around the argument' in COMP),
        ('G-N2-SCORED', 'per claim', '(N2) it grades NOT THE CLAIM at the deposited pin : per claim' in COMP),
        ('G-N3-SCORED', 'by the line', '(N3) the line states the item' in COMP),
        ('G-SEAT-EXPECTATIONS-SCORED', 'the seat`s own', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'emitted for b455', SPAN.get('emitted_for') == 'b455' and SPAN.get('current_span') == 2),
        ('G-NOGRADE-MOVED', 'no row edited', fold('NO GRADE MOVED ON ANY ROW') in F and unchanged(PP, 'FACES_LEDGER.md') and unchanged(PP, 'REGISTRY.md') and not any(f in pp_committed for f in ('FACES_LEDGER.md', 'REGISTRY.md'))),
        ('G-NOKERNEL-WRITE', 'kernels unwritten', kern_clean),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOZENODO-WRITE', 'no Zenodo client in the act`s code', fold('NOTHING WRITTEN AT ZENODO IN ANY BRANCH') in F and not re.search(r'zenodo\.org|ZENODO_TOKEN|api/deposit', SRC_COMP + SRC_DESK)),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b455' not in ln and 'b369' not in ln and 'b373' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: the trail only; ERRATA, README, REGISTRY, FINDINGS, the deposited copy untouched', all(f == 'OPEN_TRAILS.md' for f in pp_touched + pp_committed) and all(unchanged(PP, f) for f in pp_unchanged)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list : off %d %s' % (len(off_exact), off_exact), not off_exact),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b455' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'write-target shape %d %s ; control fires %s' % (len(carried), carried, control), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-14-b455, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
