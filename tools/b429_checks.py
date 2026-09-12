# -*- coding: utf-8 -*-
"""b429_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Pins are read off this act's own step-zero record; the addresses, the build and the grade are read off
### the components' own JSON, never typed; the foreign source is quoted through the components' own reader.
"""
import ast
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
import b429_components as CMP   # noqa: E402
import b429_desk_bank as DB     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PINS_FILE = os.path.join(D, 'b429_pins_stepzero.txt')


def _pin(name, path):
    t = io.open(PINS_FILE, encoding='utf-8', errors='replace').read() if os.path.exists(PINS_FILE) else ''
    m = re.search(r'--- %s\s+\(%s\)\s+local HEAD\s+: ([0-9a-f]{40})' % (re.escape(name), re.escape(path)), t)
    return m.group(1)[:7] if m else ''


PIN_RELAY = _pin('relay', 'D:\\relay')
PIN_PP = _pin('PLACE-papers', 'D:\\MY-DOwnloads\\PLACE-papers')
PIN_SIDE = _pin('SIDE-global-section', 'D:\\SIDE-global-section')
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b429_checks_postpush.txt' if POST else 'b429_checks.txt')
NL = chr(10)
L = []


def say(s=''):
    L.append(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def blob(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def unchanged(repo, pin, rel):
    return subprocess.run(['git', '-C', repo, 'diff', '--quiet', pin, '--', rel]).returncode == 0


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    return (r.stdout or '').strip()


def prefix_ok(rel):
    pin = blob(PP, PIN_PP, rel) or b'x'
    return rb(os.path.join(PP, *rel.split('/'))).startswith(pin.rstrip(b'\n'))


RULE_RE = re.compile('[-=#]{8,}')


def fold(s):
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def unbar(s):
    """### THE BANKS HARD-WRAP THROUGH A QUOTATION AND PREFIX EACH CONTINUATION WITH `| ` (b426's arm failure)."""
    return fold(re.sub(chr(10) + r'\s*\|\s?', ' ', s or ''))


def pycode_of(src):
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.STRING, tokenize.COMMENT):
                continue
            out.append(tok.string)
    except Exception:
        return 'TOKENIZE-FAILED ' + src
    return ' '.join(out)


def strings_of(src):
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.STRING:
                out.append(tok.string)
    except Exception:
        return [src]
    return out


def verdict_line(text, key):
    for ln in (text or '').splitlines():
        if key in ln:
            return ln
    return ''


def stamp_of(text, key='at (UTC) :'):
    m = re.search(re.escape(key) + r' (\S+)', text or '')
    return m.group(1) if m else ''


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'ADDRT', 'CLAYT', 'BLDT', 'READT', 'GRADET', 'LOCK', 'GATE', 'BANK',
             'TRAILS', 'B429T', 'CORR', 'FACE', 'FERRY', 'SCAN', 'SEALV', 'AXPR')


def _raw_no_arms():
    src = read(os.path.abspath(__file__))
    bad = []
    for node in ast.walk(ast.parse(src)):
        if not (isinstance(node, ast.Assign) and any(getattr(t, 'id', '') == 'ARMS' for t in node.targets)):
            continue
        for el in node.value.elts:
            if not (isinstance(el, ast.Tuple) and len(el.elts) == 3):
                continue
            nm = getattr(el.elts[0], 'value', '')
            if isinstance(nm, str) and nm.startswith('G-NO'):
                names = {n.id for n in ast.walk(el.elts[2]) if isinstance(n, ast.Name)}
                if names & set(RAW_TEXTS):
                    bad.append(nm)
    return bad


FACEPATH = os.path.join(D, 'b429_registration_2026-09-12.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b429_ferry.txt'))
SCAN = read(os.path.join(D, 'b429_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b429_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b429_faces_census_stepzero.txt'))
PINSREC = read(PINS_FILE)
EXT = read(os.path.join(D, 'b429_extract.txt'))
COMP = read(os.path.join(D, 'b429_components.txt'))
ADDRT = read(CMP.ADDR)
CLAYT = read(CMP.CREC)
BLDT = read(CMP.BREC)
READT = read(CMP.RREC)
GRADET = read(CMP.GREC)
AXPR = read(os.path.join(D, 'b429_axiom_prints.txt'))
AJ = json.loads(read(CMP.AJSON) or '{"addresses": {}, "supplied": 0, "resolved": 0, "unreachable": ["x"], "guessed": 1}')
CJ = json.loads(read(CMP.CJSON) or '{"quoted": []}')
BJ = json.loads(read(CMP.BJSON) or '{"built": null, "profile": {}, "axioms_beyond": {}, "sorryax": {}}')
RJ = json.loads(read(CMP.RJSON) or '{"answers": {}, "mapped": 0, "of": 0}')
GJ = json.loads(read(CMP.GJSON) or '{"grade": null, "clauses": []}')
LOCK = read(os.path.join(D, 'b429_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b429_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b429_desk_notes.txt'))
BANK = read(DB.BANKOUT)
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B429T = TRAILS.split('<!-- b429')[-1] if '<!-- b429' in TRAILS else ''
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FFACE, FSEALV = fold(BANK), fold(COMP), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b429_components.py'))
EXTSRC = read(os.path.join(T, 'b429_extract.py'))
DESKSRC = read(os.path.join(T, 'b429_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b429_')]
B428MARK_RE = r"(?m)^\| (\d+) \| \*\*SITE \(iii\), THE WIDTH COORDINATE'S UNION"
CORPUS_TOUCHED = ['OPEN_TRAILS.md']
CORPUS_UNTOUCHED = ['REGISTRY.md', 'FINDINGS.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md', 'VERIFICATION_LOOM.md',
                    'ERRATA.md', 'README.md', 'phase1.5/method/EXCLUSION_ENGINE.md',
                    'phase2/physics-speculative/FORMATION_DISTANCE.md', 'day1/A_Place_to_Stand.md']
ROW428 = [int(x.group(1)) for x in re.finditer(B428MARK_RE, CORR)]
ROW429 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(DB.ROWMARK), CORR)]
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')
SUPPLIED = (CMP.REPO_URL, CMP.WRITEUP, CMP.CLAY)
BUILT = bool(BJ.get('built'))
HOSTS = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join(strings_of(COMPSRC))))
BUILD_HOSTS = set(BJ.get('hosts', []))
ALLOWED = {'github.com', 'cdn.openai.com', 'claymath.org', 'releases.lean-lang.org', 'raw.githubusercontent.com',
           'lakecache.blob.core.windows.net', 'leanprover-community.github.io', 'objects.githubusercontent.com',
           'codeload.github.com', 'www.apache.org', 'www.claymath.org'}


def addresses_as_given():
    urls = [v.get('url') for v in AJ.get('addresses', {}).values()]
    return sorted(urls) == sorted(SUPPLIED) and AJ.get('supplied') == 3


def pinned():
    a = AJ.get('addresses', {})
    r = a.get('repository', {})
    ok = bool(re.fullmatch(r'[0-9a-f]{40}', r.get('head', '') or ''))
    for k in ('writeup', 'clay'):
        ok = ok and bool(re.fullmatch(r'[0-9a-f]{64}', a.get(k, {}).get('sha256', '') or ''))
    return ok


def stop_rule():
    """### IF ANY ADDRESS IS UNREACHABLE THE GRADE IS WITHHELD; IF NONE IS, THE ACT WAS NOT STOPPED BY IT."""
    un = AJ.get('unreachable', [])
    g = (GJ.get('grade') or '')
    if un:
        return 'NO GRADE' in g
    return 'ADDRESS UNREACHABLE' not in g


def build_or_stop():
    g = (GJ.get('grade') or '')
    if BUILT:
        return 'NO GRADE' not in g and bool(BJ.get('profile'))
    return 'NO GRADE' in g and bool(re.search(r'(?m)^\s*\|', BLDT))


def profile_from_printer():
    if not BUILT:
        return True
    return bool(AXPR) and ('depends on axioms' in AXPR) and bool(BJ.get('profile', {}).get(CMP.TERM_C))


def five_questions():
    return set(RJ.get('answers', {})) == {'Q1', 'Q2', 'Q3', 'Q4', 'Q5'}


def lean_at_line():
    """### EVERY QUOTATION OF COMPONENT 3 CARRIES A FILE AND A LINE RANGE."""
    return len(re.findall(r'(?m)^  .*\.lean lines \d+-\d+$', READT)) >= 8


def grade_one_of_four():
    g = (GJ.get('grade') or '')
    return g.startswith(('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION', 'NOT THE CLAIM', 'NO GRADE'))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0 and the three pins parse',
     '0' == (verdict_line(PINSREC, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and all(len(p) == 7 for p in (PIN_RELAY, PIN_PP, PIN_SIDE))),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes every component record',
     'SEAL INTACT' in SEALV and all(bool(stamp_of(x)) for x in (ADDRT, CLAYT, BLDT, READT, GRADET))
     and stamp_of(FACE, 'locked at (UTC) :') < min(stamp_of(x) for x in (ADDRT, CLAYT, BLDT, READT, GRADET))),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the seal verifies and the registration gate reads CLEAR',
     'SEAL INTACT' in SEALV and 'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-PRIOR-CLOSED', 'b428 at row 277 by its marker and its closing record tracked',
     ROW428 == [277] and git(ROOT, 'ls-files', 'data/b428_closing.txt') == 'data/b428_closing.txt'),
    # ---- READING (1), THE ADDRESSES
    ('G-ADDR-AS-GIVEN', 'exactly the three addresses the author supplied were resolved', addresses_as_given()),
    ('G-ADDR-NOTHING-GUESSED', 'no address was guessed and none substituted',
     AJ.get('guessed') == 0 and AJ.get('substituted') == 0),
    ('G-ADDR-PINNED', 'the repository by a 40-hex SHA, each document by a 64-hex sha256', pinned()),
    ('G-ADDR-UNREACHABLE-PRINTED', 'an unreachable address carries the response the host gave',
     all(v.get('status') == 'RESOLVED' or bool(v.get('response')) for v in AJ.get('addresses', {}).values())),
    ('G-STOP-RULE-HONOURED', 'reading (7)`s stop rule was applied as written', stop_rule()),
    # ---- COMPONENT 1
    ('G-CLAY-VERBATIM', 'statement C is quoted verbatim from the page', 'STATEMENT C, VERBATIM' in CLAYT
     and 'Breakdown of Navier' in CLAYT),
    ('G-CLAY-CONDITIONS-FOUR', 'conditions (4), (5), (6) and (7) are each quoted',
     len([q for q in CJ.get('quoted', []) if q.startswith(('(4)', '(5)', '(6)', '(7)'))]) == 4),
    ('G-CLAY-NOT-PARAPHRASE', 'the errata are read on the page and their reach is stated',
     'THE ERRATA' in CLAYT and 'WHERE THEY APPLY' in CLAYT),
    # ---- COMPONENT 2
    ('G-REPO-PINNED', 'the clone`s HEAD equals the SHA `ls-remote` returned',
     bool(BJ.get('head')) and BJ.get('head') == BJ.get('remote_head')),
    ('G-TERMINAL-FROM-README', 'where the terminal was located from is stated, README or manifest',
     BJ.get('readme_names_terminal') is False and 'formalization.yaml' in BLDT),
    ('G-TOOLCHAIN-REPORTED', 'the foreign toolchain and Mathlib are reported against the corpus`s',
     bool(BJ.get('foreign_toolchain')) and bool(BJ.get('corpus_pins')) and BJ.get('newer') is not None),
    ('G-BUILD-OR-STOP', 'it built and was graded, or it did not and no grade was conferred', build_or_stop()),
    ('G-PROFILE-FROM-PRINTER', 'the axiom profile comes from `#print axioms`, not an exit code', profile_from_printer()),
    ('G-AXIOMS-BEYOND-THREE-NAMED', 'every axiom outside the standard three is named',
     (not BUILT) or isinstance(BJ.get('axioms_beyond', {}).get(CMP.TERM_C), list)),
    ('G-SORRY-SWEPT', 'a source-level `sorry` sweep ran and its result is printed',
     isinstance(BJ.get('sorry_lines'), int) and 'sorry` SWEEP' in BLDT),
    # ---- COMPONENT 3
    ('G-UNFOLD-FIVE-QUESTIONS', 'all five questions are answered', five_questions()),
    ('G-LEAN-QUOTED-AT-LINE', 'every clause is quoted from the Lean source at its file and line', lean_at_line()),
    ('G-UNIQUENESS-ROUTED', 'the uniqueness question is answered by one of the four readings',
     bool(RJ.get('answers', {}).get('Q5'))),
    # ---- COMPONENT 4
    ('G-GRADE-ONE-OF-FOUR', 'the grade is one of the four, or a stated withholding', grade_one_of_four()),
    ('G-FOURTH-GRADE-MEASURED', 'the corpus`s own vocabulary was measured, not assumed',
     'NOT THE CLAIM' in GRADET and 'the corpus names a grade' in GRADET),
    ('G-SELFGRADE-RUN', 'the corpus`s own route terminal is graded under the same reading',
     bool(GJ.get('corpus_grade')) and 'riemann_hypothesis' in GRADET),
    # ### **RUN 1 COUNTED PROSE.** ### `TO ITSELF` also occurs in narrative sentences ("the corpus applied it to
    # ### itself harshly"), so a bare count made 4 labels look like 6. ### The arm counts the LABEL -- a line whose
    # ### stripped form begins with it -- and not the words wherever they fall.
    ('G-SELFGRADE-BOTH-WAYS', 'every compared clause is labelled to the stranger and to itself',
     len(re.findall(r'(?m)^\s*TO THE STRANGER\s*:', GRADET)) == len(re.findall(r'(?m)^\s*TO ITSELF\s*:', GRADET))
     and len(re.findall(r'(?m)^\s*TO ITSELF\s*:', GRADET)) >= 4),
    ('G-CANNOT-TELL-ALLOWED', 'the act says CANNOT TELL where it cannot tell',
     GJ.get('cannot_tell') is True and 'CANNOT TELL' in GRADET),
    ('G-SOURCE-OVER-PARAPHRASE', 'the order`s `h2` is corrected to the source`s `h_cons`',
     'h_cons' in GRADET and 'a source governs its paraphrase' in fold(GRADET)),
    # ---- THE EXPECTATIONS
    ('G-N1-APART', '(N1)`s two clauses scored apart', COMP.count('(N1) *') == 2),
    ('G-N2-SCORED', '(N2) scored once', COMP.count('(N2) *') == 1),
    ('G-N3-SCORED', '(N3) scored once', COMP.count('(N3) *') == 1),
    # ---- THE ENVIRONMENT AND THE SCOPE
    ('G-HOSTS-NAMED', 'every host the act`s code names is one reading (6) permits', HOSTS <= ALLOWED),
    ('G-HOSTS-BYTES-PRINTED', 'the hosts the build reached are read off the build`s own logs',
     isinstance(BJ.get('hosts'), list) and BUILD_HOSTS <= ALLOWED),
    ('G-CLONE-OUTSIDE', 'the clone is outside every rostered repository',
     CMP.REPO.replace(chr(92), '/').startswith('D:/_b429_external')
     and not os.path.isdir(os.path.join(ROOT, 'repo'))),
    ('G-NOCORPUSKERNEL', 'no corpus kernel .lean file changed and the profile unchanged',
     not [f for f in git(SIDE, 'diff', '--name-only', PIN_SIDE).split() if f.endswith('.lean')]
     and unchanged(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt')),
    # ### **RUN 1 READ THE TOOL'S OWN REPORT TEXT.** ### `lake build` occurs in a `say(...)` literal that PRINTS
    # ### the foreign build's exit code, so the arm fired on the act's own prose about itself -- the exact species
    # ### `BAR 12` names. ### It now reads the STRIPPED CODE: the act never runs a subprocess inside a corpus
    # ### kernel, and the corpus kernel's own build outputs are unchanged.
    ('G-NOCORPUSBUILD', 'no corpus kernel was built',
     not re.search(r'cwd\s*=\s*(SK|KERN)', pycode_of(COMPSRC + EXTSRC + DESKSRC))
     and unchanged(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt')),
    # ### **RUN 1 MATCHED A GIT SHA.** ### `b429` is a substring of the commit `...4b4296e5cc...` that
    # ### `REGISTRY.md` has carried for months, so a bare substring made an untouched file look like a citation.
    # ### ### **AN ACT TOKEN IS A WORD, NOT A SUBSTRING** (`A2`'s species in a new dress). ### The arm now
    # ### requires a word boundary, and it checks in git's own view that this act changed none of these files.
    ('G-CITED-NOWHERE', 'the grading is cited in no corpus document',
     0 == len([1 for f in ('FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md')
               if re.search(r'b429', read(os.path.join(PP, f)))])
     and all(unchanged(PP, PIN_PP, f) for f in ('FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md'))),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B429T for k in (1, 2, 3, 4)) and B429T.count('**OPEN.**') == 4
     and 'Trigger: the ruling on which test governs' in BANK),
    ('G-ARC-CHECKPOINTED', 'the witness arc is restated checkpointed after site (iii)',
     'checkpointed after site (iii)' in fold(BANK).lower() or 'CHECKPOINTED after site (iii)' in BANK),
    # ---- THE STANDING NEGATIVES
    ('G-NOGRADE-MOVED', 'no grade of the corpus`s own was moved or minted',
     not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in (ACT_WORK + ' '.join(strings_of(COMPSRC))).lower()),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 6),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-8])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b429_span')]),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-NOLANEEDIT', 'the lane documents, the keystones and REGISTRY.md unchanged',
     all(unchanged(PP, PIN_PP, r) for r in ('REGISTRY.md', 'phase2/physics-speculative/FORMATION_DISTANCE.md',
                                            'phase1.5/method/EXCLUSION_ENGINE.md', 'README.md'))),
    ('G-CORPUS-SCOPE', 'exactly the one declared corpus file differs from the pin',
     sorted(git(PP, 'diff', '--name-only', PIN_PP).split()) == sorted(CORPUS_TOUCHED)
     and all(unchanged(PP, PIN_PP, r) for r in CORPUS_UNTOUCHED)),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b429' in TRAILS and '<!-- b428' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b428 at 277 and this act at 278, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW428 == [277] and ROW429 == [278]),
    ('G-WRITELIST-KINDS', 'the face names 6 kinds', 6 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'exactly six relay act-tool files', 6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool stages by -A', not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', ACT_WORK)),
    ('G-NOBORROWEDBAR', 'no `G-NO*` arm reads a raw document text', 0 == len(_raw_no_arms())),
    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms run over this act`s own bank', bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments and strings by the tokenizer', 'def pycode_of' in SELFSRC),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup and quotation bars before matching',
     'def fold' in SELFSRC and 'def unbar' in SELFSRC),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdict lines read', 'def verdict_line' in SELFSRC),
    ('G-NOWRAP-MIDTOKEN', 'the writers wrap at word boundaries',
     all('def wrap(' in s for s in (COMPSRC, EXTSRC, DESKSRC))
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', pycode_of(COMPSRC + EXTSRC + DESKSRC)))),
    ('G-MUSTFAIL', 'none of the forbidden lines is in the bank',
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'a grade was moved', 'h2 has moved',
                                          'the proof is correct', 'the proof is wrong', 'a lane was opened'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b429_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
say('  pins read off this act`s own step-zero record : relay %s ; PLACE-papers %s ; SIDE-global-section %s'
    % (PIN_RELAY, PIN_PP, PIN_SIDE))
say('  hosts named in the component`s strings : %s' % sorted(HOSTS))
say('  hosts the build reached, off its own logs : %s' % sorted(BUILD_HOSTS))
say('  corpus files differing from the pin : %s' % sorted(git(PP, 'diff', '--name-only', PIN_PP).split()))
say('  BUILT : %s ; GRADE : %s' % (BUILT, GJ.get('grade')))
passing = failing = 0
for name, desc, res in ARMS:
    if res is None:
        res = (declared == run)
    ok = bool(res)
    passing += 1 if ok else 0
    failing += 0 if ok else 1
    say('  %-42s %-56s %s' % (name, desc[:56], 'PASS' if ok else '### **FAIL**'))
say('-' * 100)
say('  declared on the face : %d' % len(declared))
say('  run here             : %d' % len(run))
say('  declared but not run : %s' % (sorted(declared - run) or 'none'))
say('  run but not declared : %s' % (sorted(run - declared) or 'none'))
say('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**' % (len(ARMS), passing, failing))
say('=' * 100)
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if failing else 0)
