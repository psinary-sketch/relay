# -*- coding: utf-8 -*-
"""b425_checks.py -- THE GATE SUITE. ### **EVERY ARM DECLARED ON THE FACE IS RUN HERE, AND EVERY ARM RUN
### HERE IS DECLARED ON THE FACE.** ### Reconciled both ways, pre-push and post-push.
### ### Files are compared to their blobs at the pins the act started from (relay a79578e, PLACE-papers 786740b,
### SIDE-global-section 8ef6190), in git's own view; rows are read by marker; the selection is re-derived from the
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
import b425_components as CMP   # noqa: E402
import b425_desk_bank as DB     # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_RELAY, PIN_PP, PIN_SIDE = 'a79578e', '786740b', '8ef6190'
POST = '--post' in sys.argv
OUT = os.path.join(D, 'b425_checks_postpush.txt' if POST else 'b425_checks.txt')
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
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def prefix_ok(rel):
    pin = blob(PP, PIN_PP, rel) or b'x'
    return rb(os.path.join(PP, *rel.split('/'))).startswith(pin.rstrip(b'\n'))


RULE_RE = re.compile('[-=#]{8,}')


def fold(s):
    s = RULE_RE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


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


RAW_TEXTS = ('COMP', 'EXT', 'DESKN', 'LOC', 'LOC1', 'READR', 'LOCK', 'GATE', 'BANK', 'TRAILS', 'B425T', 'CORR', 'FACE',
             'FERRY', 'SCAN', 'SEALV')


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


FACEPATH = os.path.join(D, 'b425_registration_2026-09-11.txt')
FACE = read(FACEPATH)
FERRY = read(os.path.join(D, 'b425_ferry.txt'))
SCAN = read(os.path.join(D, 'b425_ferry_scan.txt'))
CEN = read(os.path.join(D, 'b425_census_stepzero.txt'))
FCEN = read(os.path.join(D, 'b425_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b425_pins_stepzero.txt'))
EXT = read(os.path.join(D, 'b425_extract.txt'))
COMP = read(os.path.join(D, 'b425_components.txt'))
LOC = read(CMP.LOC)
LOC1 = read(os.path.join(D, 'b425_locate_run1.txt'))
LJ = json.loads(read(CMP.LJSON) or '{"results": [], "chosen": [], "sources": []}')
READR = read(CMP.READREC)
RJ = json.loads(read(CMP.RJSON) or '{"sources": [], "fired": []}')
LOCK = read(os.path.join(D, 'b425_lockgate_notes.txt'))
GATE = read(os.path.join(D, 'b425_reg_gate.txt'))
DESKN = read(os.path.join(D, 'b425_desk_notes.txt'))
BANK = read(DB.BANKOUT)
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
TRAILS = read(os.path.join(PP, 'OPEN_TRAILS.md'))
B425T = TRAILS.split('<!-- b425')[-1] if '<!-- b425' in TRAILS else ''
_sv = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACEPATH], capture_output=True,
                     text=True, encoding='utf-8', errors='replace')
SEALV = _sv.stdout or ''

FBANK, FCOMP, FREAD, FFACE, FSEALV = fold(BANK), fold(COMP), fold(READR), fold(FACE), fold(SEALV)
SELFSRC = read(os.path.abspath(__file__))
COMPSRC = read(os.path.join(T, 'b425_components.py'))
EXTSRC = read(os.path.join(T, 'b425_extract.py'))
DESKSRC = read(os.path.join(T, 'b425_desk_bank.py'))
ACT_WORK = pycode_of(COMPSRC + EXTSRC + DESKSRC)
TOOLS_THIS_ACT = [f for f in sorted(os.listdir(T)) if f.startswith('b425_')]
B424MARK = "**THE WITNESS ARC AT SITE (i), THE CLAUSE'S QUANTIFIER: SIXTEEN CANDIDATES READ AT SOURCE, NONE HELD**"
LANE_DOCS = ['phase2/physics/FANO_DERIVATION_OF_LAMBDA.md', 'phase2/physics/STORMER.md',
             'phase2/physics-speculative/FORMATION_DISTANCE.md', 'phase1.5/spectral/FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md',
             'REGISTRY.md']


def rows_of(mark, text):
    return [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mark), text)]


ROW424, ROW425 = rows_of(B424MARK, CORR), rows_of(DB.ROWMARK, CORR)
OLDCORR = (blob(SIDE, PIN_SIDE, 'CORRESPONDENCE.md') or b'').decode('utf-8')


def reselect():
    """### THE RULE RE-RUN ON THE BANKED RESULTS, BY THE COMPONENTS' OWN TESTS."""
    res = LJ['results']
    for r in res:
        t = r['title'] + ' ' + r['abstract']
        if (bool(re.search(CMP.T_A, t)), bool(re.search(CMP.T_B, t)), bool(re.search(CMP.T_C, t))) != (r['a'], r['b'], r['c']):
            return None
    qual = [r for r in res if r['a'] and r['b'] and r['c']]
    dr2 = sorted([r for r in qual if re.search(CMP.DR2, r['title'])], key=lambda r: r['published'], reverse=True)[:1]
    rest = sorted([r for r in qual if r not in dr2], key=lambda r: r['published'], reverse=True)
    return [r['id'] for r in (dr2 + rest)[:CMP.CAP]]


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
        for spec in [dd['claim'], dd['sig'], dd['deciding']] + dd['a'] + ([dd['qualifier']] if dd.get('qualifier') else []):
            if CMP.qtext(CMP.source_text(aid, spec[0]), spec[1], spec[2]) == '### MISS':
                return False
    return set(CMP.DECIDE) == set(LJ['chosen'])


def decided_by_rule():
    for o in RJ['sources']:
        d = o['deciding'].lower()
        want = 'FIRED' if re.search(r'exclud|ruled? out', d) else ('UNDECIDED' if re.search(CMP.T_C, o['deciding']) else 'NOT FIRED')
        if want != o['verdict']:
            return False
    return bool(RJ['sources'])


HOSTS = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join(strings_of(COMPSRC))))
# ### RUN 1 COUNTED THE ATOM NAMESPACE URI AS A HOST REACHED; IT IS AN XML IDENTIFIER THAT NOTHING FETCHES. ### THE HOSTS
# ### REACHED ARE THE ONES `get()` IS CALLED WITH -- the three constants -- and every other URL string must be the
# ### listing's too, the namespace identifier alone excepted BY NAME.
REACHED = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join((CMP.API, CMP.ABS, CMP.PDF))))
NSHOSTS = set(re.findall(r'https?://([A-Za-z0-9.-]+)', ' '.join(CMP.NS.values())))

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
    ('G-LEG2-CLOSED', 'b424 at row 273 by its marker and its closing record tracked',
     ROW424 == [273] and git(ROOT, 'ls-files', 'data/b424_closing.txt') == 'data/b424_closing.txt'),
    ('G-F-COMMITMENT-QUOTED', 'the lane quoted at its pins, every blob matching',
     READR.count('blob matches pin : True') == len(CMP.LANE) and 'blob matches pin : False' not in READR),
    ('G-F-WITHDRAWN-NOT-GOVERNING', 'the withdrawal line quoted and the weaker sentence set aside',
     'WITHDRAWN' in FREAD and 'does not govern' in FREAD),
    ('G-F-SEARCH-PRINTED', 'the three declared queries run and printed, twenty-five results each',
     all(('### %s -- %s' % (t, q)) in LOC for t, q in CMP.QUERIES) and LOC.count('results : 25') == 3
     and all(q in FACE.replace(chr(10) + '### ', ' ') for _t, q in CMP.QUERIES[:2])),
    ('G-F-SELECTION-BY-RULE', 'the chosen three re-derived from the banked results by the rule', reselect() == LJ['chosen']),
    ('G-F-SOURCES-HASHED', 'every source`s bytes hashed and its text on disk', hashed()),
    ('G-F-CAP', 'at most three sources', 0 < len(LJ['chosen']) <= 3 and CMP.CAP == 3),
    ('G-F-SIGNIFICANCE-QUOTED', 'every quotation re-found in its source`s text', quotes_refound()),
    ('G-F-TENSION-THREE-PARTS', 'each source carries parts (a), (b) and (c)',
     all(READR.count(p) == len(RJ['sources']) for p in ('PART (a)', 'PART (b)', 'PART (c)')) and bool(RJ['sources'])),
    ('G-F-DECISION-BY-RULE', 'each verdict is the rule`s on its deciding sentence', decided_by_rule()),
    ('G-F-ROUTED', 'routed, and a FIRED reading names the row as the author`s to move',
     'ROUTED TO THE AUTHOR.' in READR and (not RJ['fired'] or ('REGISTRY.md p2-d6' in READR and 'AUTHOR`S TO MOVE' in READR
                                                                and 'FORMATION_DISTANCE.md line 160' in READR))),
    ('G-F-NOCOMPUTE', 'no fit, sampler or likelihood in the act`s code',
     not re.search(r'numpy|scipy|emcee|curve_fit|minimize|likelihood|chi2', pycode_of(COMPSRC))),
    ('G-L3-APART', '(L3)`s two clauses scored apart', COMP.count('(L3) *') == 2),
    ('G-FOUR-LISTS-OPEN', 'the trail and the bank restate the four lists OPEN with their trigger',
     all(('**LIST %d**' % k) in B425T for k in (1, 2, 3, 4)) and B425T.count('**OPEN.**') == 4
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
     not re.search(r"open\([^)]*b4(0[0-9]|1[0-9]|2[0-4])_[^)]*['\"]w", ACT_WORK)),
    ('G-NOBANKEDFERRY', 'no banked ferry opened for write', not re.search(r"_ferry[^)]*['\"]w", ACT_WORK)),
    ('G-NOLANEEDIT', 'the lane`s documents and REGISTRY.md unchanged since the pin',
     all(unchanged(PP, PIN_PP, r) for r in LANE_DOCS)),
    ('G-NOLEDGERROW', 'FACES_LEDGER.md unchanged since the pin', unchanged(PP, PIN_PP, 'FACES_LEDGER.md')),
    ('G-NOFOLD', 'FINDINGS.md unchanged since the pin and no span record under this act',
     unchanged(PP, PIN_PP, 'FINDINGS.md') and not [f for f in os.listdir(D) if f.startswith('b425_span')]),
    ('G-TRAIL-APPEND-ONLY', 'the pin`s trail is a true prefix and both marks are present',
     prefix_ok('OPEN_TRAILS.md') and '<!-- b425' in TRAILS and '<!-- b424' in TRAILS),
    ('G-CORR-APPEND-ONLY', 'the pin`s table a true prefix; b424 at 273 and this act at 274, by marker',
     CORR.startswith(OLDCORR.rstrip(NL)) and ROW424 == [273] and ROW425 == [274]),
    ('G-WRITELIST-KINDS', 'the face names 5 kinds', 5 == len(re.findall(r'### \*\*KIND \d+\*\*', FACE))),
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
                                          'h2 has moved', 'the lane is refuted'))),
]

declared = set(re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', FACE)) - {'G-NO'}
run = set(n for n, _d, _r in ARMS)
say('=' * 100)
say('b425_checks.py -- THE GATE SUITE.%s' % ('  ### POST-PUSH RUN.' if POST else ''))
say('=' * 100)
say('  hosts named in the component`s strings : %s' % sorted(HOSTS))
say('  hosts reached (the URLs get() is called with) : %s ; the XML namespace identifier, not fetched : %s'
    % (sorted(REACHED), sorted(NSHOSTS)))
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
