# -*- coding: utf-8 -*-
"""b426_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay 7a73635, PLACE-papers 5847a20,
### SIDE-global-section 70fd639), in git's own view; rows are read by marker; the address is re-derived from the
### banked search by the components' own rule, IMPORTED, and every quotation re-found in its source's text.
"""
import ast
import hashlib
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
import b426_components as CMP   # noqa: E402
import b426_desk_bank as DB     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_RELAY, PIN_PP, PIN_SIDE = '7a73635', '5847a20', '70fd639'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b426_checks_postpush.txt' if POST else 'b426_checks.txt')
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
    """### **THE BANKS HARD-WRAP THROUGH A QUOTATION AND PREFIX EACH CONTINUATION WITH `| `.** ### A needle
    ### matched against the raw record therefore never matches -- the wrapping species the record has banked
    ### repeatedly. ### The continuation markers are folded away BEFORE matching, the same way for both sides."""
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


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'LOC', 'LOC1', 'READR', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B426T', 'CORR', 'FACE',
             'FERRY', 'SCAN', 'SEALV', 'WRITES', 'FD', 'REG')


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


FACEPATH = os.path.join(D, 'b426_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b426_ferry.txt'))
SCAN = read(os.path.join(D, 'b426_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b426_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b426_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b426_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b426_extract.txt'))
COMP = read(os.path.join(D, 'b426_components.txt'))
LOC = read(CMP.LOC)
LOC1 = read(os.path.join(D, 'b426_locate_run1.txt'))
LJ = json.loads(read(CMP.LJSON) or '{"results": [], "chosen": [], "sources": []}')
READR = read(CMP.READREC)
RJ = json.loads(read(CMP.RJSON) or '{"address": [], "prior": []}')
WRITES = read(os.path.join(D, 'b426_writes.txt'))
LOCK = read(os.path.join(D, 'b426_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b426_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b426_desk_notes.txt'))
BANK = read(DB.BANKOUT)
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B426T = TRAILS.split('<!-- b426')[-1] if '<!-- b426' in TRAILS else ''
FD = read(CMP.FDPATH)
REG = read(CMP.REGPATH)
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FREAD, FFACE, FSEALV = fold(BANK), fold(COMP), fold(READR), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b426_components.py'))
EXTSRC = read(os.path.join(T, 'b426_extract.py'))
DESKSRC = read(os.path.join(T, 'b426_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b426_')]
B425MARK = ("**THE FALSIFIER READ: THE LANE'S w = −1 AGAINST THREE SUPERNOVA RESULTS -- "
            "FIRED AT 1 BY THE LOCKED RULE, UNDECIDED AT 2**")
CORPUS_TOUCHED = ['OPEN_TRAILS.md', 'phase2/physics-speculative/FORMATION_DISTANCE.md', 'REGISTRY.md']
CORPUS_UNTOUCHED = ['phase2/physics/FANO_DERIVATION_OF_LAMBDA.md', 'phase2/physics/STORMER.md',
                    'phase1.5/spectral/FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md', 'FACES_LEDGER.md', 'FINDINGS.md',
                    'SPIRAL_MAP.md', 'VERIFICATION_LOOM.md', 'ERRATA.md']


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW425, ROW426 = rows_of(B425MARK, CORR), rows_of(DB.ROWMARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')


def reselect():
    """### THE ADDRESS RULE RE-RUN ON THE BANKED RESULTS, BY THE COMPONENTS' OWN TESTS."""
    res = LJ['results']
    for r in res:
        if (bool(re.search(CMP.T_I, r['title'])), bool(re.search(CMP.T_II, r['title'])),
                bool(re.search(CMP.T_III, r['authors'] + ' ' + r['title'] + ' ' + r['abstract']))) != (r['i'], r['ii'], r['iii']):
            return None
    qual = [r for r in res if r['i'] and r['ii'] and r['iii']]
    named = sorted([r for r in qual if r['constraints']], key=lambda r: r['published'])
    rest = sorted([r for r in qual if not r['constraints']], key=lambda r: r['published'])
    return [r['id'] for r in (named + rest)[:CMP.CAP]]


def hashed():
    for s in LJ['sources']:
        for k in ('abs', 'pdf'):
            x = s.get(k, {})
            if not x.get('sha256') or not os.path.exists(os.path.join(D, x.get('extract', '#'))):
                return False
            f = os.path.join(CMP.SCRATCH, '%s.%s' % (CMP.slug(s['id']), 'html' if k == 'abs' else 'pdf'))
            if os.path.exists(f) and hashlib.sha256(rb(f)).hexdigest() != x['sha256']:
                return False
    return bool(LJ['sources'])


def quotes_refound():
    for aid, dd in CMP.DECIDE.items():
        specs = [dd['claim'], dd['sig']] + dd['a'] + ([dd['excl']] if dd.get('excl') else [])
        for spec in specs:
            if CMP.qtext(CMP.source_text(aid, spec[0]), spec[1], spec[2]) == '### MISS':
                return False
    return set(CMP.DECIDE) == set(LJ['chosen'])


def scored_by_rule():
    """### EVERY VERDICT IS (R38)'S THRESHOLD FUNCTION APPLIED TO THE FIGURE, RE-COMPUTED HERE."""
    for o in RJ.get('address', []):
        if (CMP.verdict_at(o['low'], True), CMP.verdict_at(o['high'], True)) != (o['low_verdict'], o['high_verdict']):
            return False
    for p in RJ.get('prior', []):
        if (CMP.verdict_at(p['low'], False), CMP.verdict_at(p['high'], False)) != (p['low_verdict'], p['high_verdict']):
            return False
    return bool(RJ.get('address')) and bool(RJ.get('prior'))


def weakest_carried():
    lows = [o['low_verdict'] for o in RJ.get('address', [])] + [p['low_verdict'] for p in RJ.get('prior', [])]
    highs = [o['high_verdict'] for o in RJ.get('address', [])] + [p['high_verdict'] for p in RJ.get('prior', [])]
    return (CMP.weakest(lows) == RJ.get('weakest_clause') and CMP.strongest(highs) == RJ.get('any_clause')
            and bool(lows))


def fd_ok():
    """### THE SENTENCE KEPT AND EXACTLY ONE LINE INSERTED, AGAINST THE PIN'S OWN BLOB."""
    old = (blob(PP, PIN_PP, 'phase2/physics-speculative/FORMATION_DISTANCE.md') or b'').decode('utf-8')
    return (FD.count(CMP.FD_LINE160) == 1 and FD.count(CMP.FD_APPEND) == 1
            and FD.replace(NL + CMP.FD_APPEND, '', 1) == old
            and len(FD.split(NL)) == len(old.split(NL)) + 1)


def reg_ok():
    """### THE p2-d6 ROW: THE STATUS CELL GAINS A NOTE AND EVERY OTHER CELL IS BYTE-IDENTICAL TO THE PIN'S."""
    old = (blob(PP, PIN_PP, 'REGISTRY.md') or b'').decode('utf-8')
    a = [ln for ln in old.split(NL) if ln.startswith('| p2-d6 |')]
    b = [ln for ln in REG.split(NL) if ln.startswith('| p2-d6 |')]
    if not (a and b):
        return False, False
    ca = a[0].strip().strip('|').split('|')
    cb = b[0].strip().strip('|').split('|')
    if len(ca) != 8 or len(cb) != 8:
        return False, False
    same = all(ca[k] == cb[k] for k in range(8) if k != 5)
    note = (CMP.NOTEMARK in cb[5]) and cb[5].strip().startswith('READY') and REG.count(CMP.NOTEMARK) == 1
    body_same = old.replace(a[0], b[0], 1) == REG
    return bool(note), bool(same and body_same)


REG_NOTE_OK, REG_CELLS_OK = reg_ok()
HOSTS = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join(strings_of(COMPSRC))))
REACHED = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join((CMP.API, CMP.ABS, CMP.PDF))))
NSHOSTS = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join(CMP.NS.values())))
A0 = (RJ.get('address') or [{}])[0]

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the ferry carries its own paste-end marker', 'paste ends (part 1 of 1)' in FERRY),
    ('G-SCAN-CLEAN', 'the ferry`s scan reports 0 hits', '0 HIT(S) REPORTED' in verdict_line(SCAN, 'VERDICT:')),
    ('G-STEPZERO-CENSUS', 'both step-zero censuses report TOTAL MISSING : 0',
     '0' == (verdict_line(CEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')
     and '0' == (verdict_line(FCEN, 'TOTAL MISSING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-STEPZERO-PINS', 'the pins report REPOS HARD-FAILING : 0',
     '0' == (verdict_line(PINS, 'REPOS HARD-FAILING').rsplit(':', 1)[-1].strip().strip('*# ') or 'x')),
    ('G-SURVEY-NOMISS', 'the survey reports ANCHOR MISSES : 0', 'ANCHOR MISSES : 0' in fold(verdict_line(EXT, 'ANCHOR MISSES'))),
    ('G-REG-LOCKED-FIRST', 'the seal verifies and precedes the first search and the read',
     'SEAL INTACT' in SEALV and bool(stamp_of(LOC1)) and bool(stamp_of(READR))
     and stamp_of(FACE, 'locked at (UTC) :') < min(stamp_of(LOC1), stamp_of(LOC), stamp_of(READR))),
    ('G-LOCKGATE-EIGHT', 'the lock run read 8, passed 8, 4 by digest',
     'GATES READ : 8' in LOCK and 'PASSING : 8' in LOCK and 'CHECKED BY DIGEST : 4' in LOCK and 'LOCK PERMITTED' in LOCK),
    ('G-SEAL-VERIFIES', 'the seal verifies and the registration gate reads CLEAR',
     'SEAL INTACT' in SEALV and 'CLEAR' in verdict_line(GATE, 'GATE VERDICT')
     and 'NOT CLEAR' not in verdict_line(GATE, 'GATE VERDICT')),
    ('G-LEG3-CLOSED', 'b425 at row 274 by its marker and its closing record tracked',
     ROW425 == [274] and git(ROOT, 'ls-files', 'data/b425_closing.txt') == 'data/b425_closing.txt'),
    ('G-R38-QUOTED', '(R38) quoted from the banked ferry, verbatim, in the read',
     CMP.qtext(FERRY, CMP.R38_ANCHOR, CMP.R38_END, cap=600) != '### MISS'
     and CMP.qtext(FERRY, CMP.R38_ANCHOR, CMP.R38_END, cap=600) in unbar(READR)),
    ('G-R39-QUOTED', '(R39) quoted from the banked ferry, verbatim, in the read',
     CMP.qtext(FERRY, CMP.R39_ANCHOR, CMP.R39_END, cap=700) != '### MISS'
     and CMP.qtext(FERRY, CMP.R39_ANCHOR, CMP.R39_END, cap=700) in unbar(READR)),
    ('G-A-SEARCH-PRINTED', 'the three declared queries run and printed, fifty results each',
     all(('### %s -- %s' % (t, q)) in LOC for t, q in CMP.QUERIES)
     and all(q in FACE.replace(NL + '### ', ' ') for _t, q in CMP.QUERIES[:1])
     and len(LJ['results']) > 0),
    ('G-A-ADDRESS-BY-RULE', 'the address re-derived from the banked results by the rule', reselect() == LJ['chosen']),
    ('G-A-COLLAB-AUTHOR', 'the chosen address`s author field names the collaboration',
     bool(LJ['sources']) and all(re.search(CMP.T_III, s.get('authors', '') + ' ' + s.get('title', ''))
                                 for s in LJ['sources'])),
    ('G-A-HASHED', 'the address`s bytes hashed and its text on disk', hashed()),
    ('G-A-CAP', 'at most one address', 0 < len(LJ['chosen']) <= 1 and CMP.CAP == 1),
    ('G-A-QUOTES-REFOUND', 'every quotation re-found in its source`s text', quotes_refound()),
    ('G-A-THREE-PARTS', 'the address carries parts (a), (b) and (c)',
     all(READR.count(p) >= 1 for p in ('PART (a)', 'PART (b)', 'PART (c)')) and bool(RJ.get('address'))),
    ('G-A-EXCLUSION-READ', 'the paper`s own words on exclusion quoted, or their absence reported as absence',
     bool(A0) and (bool(A0.get('exclusion')) or '### **ABSENT**' in READR)),
    ('G-A-RANGE-BOTH-ENDS', 'every stated range read at both ends and each end`s verdict computed by the rule',
     scored_by_rule()),
    ('G-A-BOTH-CLAUSES', 'both clauses of (R38) answered and printed side by side',
     'CLAUSE 1' in READR and 'CLAUSE 2' in READR and RJ.get('any_clause') and RJ.get('weakest_clause')),
    ('G-A-WEAKEST', 'the combined reading carried is the weakest, computed not typed', weakest_carried()),
    ('G-B425-RESTATED', 'b425`s three restated from b425`s own banked record, not re-fetched',
     len(RJ.get('prior', [])) == 3
     and all(p['b425'] in ('UNDECIDED', 'FIRED', 'NOT FIRED') for p in RJ.get('prior', []))
     and not any(('b425_source' in s) for s in strings_of(COMPSRC))),
    ('G-A-NOCOMPUTE', 'no fit, sampler or likelihood in the act`s code',
     not re.search(r'numpy|scipy|emcee|curve_fit|minimize|likelihood|chi2', pycode_of(COMPSRC))),
    ('G-FD-SENTENCE-KEPT', 'line 160 byte-identical and the pin`s text is the new text less one line', fd_ok()),
    ('G-FD-ONE-LINE', 'exactly one line inserted into FORMATION_DISTANCE.md, and it carries (R38)',
     len(FD.split(NL)) == len((blob(PP, PIN_PP, 'phase2/physics-speculative/FORMATION_DISTANCE.md') or b'').decode('utf-8').split(NL)) + 1
     and '(R38)' in CMP.FD_APPEND),
    ('G-REG-P2D6-NOTE', 'the p2-d6 status cell gains the note once and still begins READY', REG_NOTE_OK),
    ('G-REG-CELLS-KEPT', 'every other cell of p2-d6 byte-identical and the rest of the file unchanged', REG_CELLS_OK),
    ('G-PRESERVED-FIRST', 'both preservation records exist and carry a sha256 of what they preserved',
     all(os.path.exists(os.path.join(D, 'b426_preserved_%s.txt' % t))
         and re.search(r'sha256 : [0-9a-f]{64}', read(os.path.join(D, 'b426_preserved_%s.txt' % t)))
         for t in ('fd_line160', 'registry_p2d6'))),
    ('G-L1-APART', '(L1)`s two clauses scored apart', COMP.count('(L1) *') == 2),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B426T for k in (1, 2, 3, 4)) and B426T.count('**OPEN.**') == 4
     and 'Trigger: the ruling on which test governs' in BANK),
    ('G-NOKERNEL', 'no kernel .lean file changed and the profile unchanged',
     not [f for f in git(SIDE, 'diff', '--name-only', PIN_SIDE).split() if f.endswith('.lean')]
     and unchanged(SIDE, PIN_SIDE, 'AXIOM_PRINTS.txt')),
    ('G-NOGRADE', 'no grade string minted', not re.search(r'\b(GRADE (MOVED|CONFERRED|MINTED)|newly graded)\b', FBANK, re.I)),
    ('G-NOPREMISE', 'the bank states 0 premises discharged', '0 premises discharged' in FBANK),
    ('G-NODOOR', 'the bank states 0 doors restated', '0 doors restated' in FBANK),
    ('G-NOROUTE', 'the bank states 0 routes proposed', '0 routes proposed' in FBANK),
    ('G-NOKAPPA', 'no kappa value measured', not re.search(r'kappa\s*=\s*[-0-9]', FBANK, re.I)),
    ('G-NORULE', 'STRUCK_CLAUSES is not written', 'STRUCK_CLAUSES' not in ACT_WORK),
    ('G-NODEPOSIT', 'no Zenodo byte', 'zenodo' not in (ACT_WORK + ' '.join(strings_of(COMPSRC))).lower()),
    ('G-NOPLATFORM', 'the only hosts reached are the arXiv listing`s',
     bool(REACHED) and REACHED <= {'export.arxiv.org', 'arxiv.org'}
     and (HOSTS - NSHOSTS) <= {'export.arxiv.org', 'arxiv.org'} and not re.search(r'import requests', COMPSRC)),
    ('G-NOH2', 'no claim about h2 beyond the standing sentence', FBANK.count('h2') <= 3),
    ('G-NOLOCKEDFACE', 'the seal still verifies', 'SEAL INTACT -- the body is byte-for-byte what was sealed' in FSEALV),
    ('G-NOPRIORBANK', 'no prior act`s bank opened for write',
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-5])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b426_span')]),
    ('G-CORPUS-SCOPE', 'exactly the three declared corpus files differ from the pin',
     sorted(git(PP, 'diff', '--name-only', PIN_PP).split()) == sorted(CORPUS_TOUCHED)
     and all(unchanged(PP, PIN_PP, r) for r in CORPUS_UNTOUCHED)),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b426' in TRAILS and '<!-- b425' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b425 at 274 and this act at 275, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW425 == [274] and ROW426 == [275]),
    ('G-WRITELIST-KINDS', 'the face names 7 kinds', 7 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
    ('G-NOEXTRAKIND', 'exactly six relay act-tool files', 6 == len(TOOLS_THIS_ACT)),
    ('G-NOSTAGE-A', 'no working tool stages by -A', not re.search('add[^' + chr(92) + 'n]{0,24}-A(?![A-Za-z])', ACT_WORK)),
    ('G-NOBORROWEDBAR', 'no `G-NO*` arm reads a raw document text', 0 == len(_raw_no_arms())),
    ('G-ARMS-DECLARED-EQ-RUN', 'declared on the face equals run here, both ways', None),
    ('G-ARMS-OWN-BANK', 'arms run over this act`s own bank', bool(BANK) and len(FBANK) > 2000),
    ('G-ARMS-STRIP-PROSE', 'this suite strips comments and strings by the tokenizer', 'def pycode_of' in SELFSRC),
    ('G-ARMS-FOLD-MARKERS', 'this suite folds markup before matching', 'def fold' in SELFSRC),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'A2: verdict lines read', 'def verdict_line' in SELFSRC),
    ('G-NOWRAP-MIDTOKEN', 'the writers wrap at word boundaries',
     all('def wrap(' in s for s in (COMPSRC, EXTSRC, DESKSRC))
     and 0 == len(re.findall(r'\[k:k ?\+ ?\d+\]', pycode_of(COMPSRC + EXTSRC + DESKSRC)))),
    ('G-MUSTFAIL', 'none of the forbidden lines is in the bank',
     not any(s in FBANK.lower() for s in ('the lock was overridden', 'the lane verdict was changed', 'a grade was moved',
                                          'h2 has moved', 'the lane is refuted', 'the register row was moved'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b426_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
say('  hosts named in the component`s strings : %s' % sorted(HOSTS))
say('  hosts reached (the URLs get() is called with) : %s ; the XML namespace identifier, not fetched : %s'
    % (sorted(REACHED), sorted(NSHOSTS)))
say('  corpus files differing from the pin : %s' % sorted(git(PP, 'diff', '--name-only', PIN_PP).split()))
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
