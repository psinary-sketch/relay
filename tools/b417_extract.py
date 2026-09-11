# -*- coding: utf-8 -*-
"""b417_extract.py -- THE SURVEY FOR b417. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **THE ACT HAS TWO SUBJECTS THAT SHARE THE SEED `{2, 3}` AND NOTHING ELSE**, and the survey
### keeps them in separate reads so no later record can join them by accident: ### READS 1-5 and 8
### are about the formation tuple's SLOTS; ### READS 9-10 are about the prime core `P`.
### ### **EVERY SEARCH HERE IS BY PYTHON AND NOT BY `rg`**, because `rg` returned no `T1.4` line from
### records this seat knows carry one -- a search tool that is silently blind to part of the tree
### cannot bank an ABSENT.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
FA = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic')
FX = os.path.join('D:', os.sep, 'SIDE-effects')
TECHNE = os.path.join(DL, 'TECHNE-Core')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
CPLX = os.path.join(PP, 'phase2', 'formation', 'COMPLEX_ANALYSIS.md')
BSD = os.path.join(PP, 'phase2', 'empirical', 'BSD_VIA_FORMATION_TRANSFER.md')
READER = os.path.join(PP, 'heritage', 'PRIME_CORE_READER.md')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
HYG = os.path.join(T, 'b369_hygiene.py')
OUT = os.path.join(D, 'b417_extract.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def quote(label, path, start, end=None, width=94, cap=700):
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:46]))
        say('  %-40s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = re.sub(r'\s+', ' ', src[i:j] if j > i else src[i:i + cap]).strip()
    say('  %-40s %s line %d' % (label, os.path.basename(path), src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      %s' % s)
    return seg


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').strip()


LIVE_SKIP = ('.git', 'archive', 'outputs', 'heritage', 'internal')
# ### **A LEDGER IS NOT A CITER.** ### `b416`'s carrier rule, carried: a record of work on a claim
# ### names the claim because ACTS WRITE ABOUT IT there, and that is not a document citing it.
LEDGERS = ('OPEN_TRAILS.md', 'FINDINGS.md', 'REGISTRY.md', 'VERIFICATION_LOOM.md',
           'CORRESPONDENCE.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'BIBLIOGRAPHY.md', 'MIGRATION.md',
           'FACES_LEDGER.md', 'README.md', 'EMERGING_RESEARCH_PROGRAMMES.md',
           'CASCADE_ANCHORS_CORRECTED.md')


def live_docs():
    for root, dirs, files in os.walk(PP):
        rel_root = os.path.relpath(root, PP)
        parts = rel_root.replace(os.sep, '/').split('/')
        if any(p in LIVE_SKIP for p in parts):
            dirs[:] = []
            continue
        for f in files:
            if f.endswith('.md') and f not in LEDGERS:
                p = os.path.join(root, f)
                yield os.path.relpath(p, PP).replace(os.sep, '/'), read(p)


rule('=')
say('b417_extract.py -- THE SURVEY: THE CONTRADICTION, THE SECOND TOOL, THE CAVEATS, AND P.')
rule('=')
say()

# =============================================================================================
rule()
say('### READ 0 -- THE ORIENTATION-LAYER CITATIONS THE FERRY CARRIES, FOUND OR ABSENT.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
rows = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \|', corr)]
# ### **THE CITATION IS FOUND BY ITS CONTENT, AND ITS NUMBER IS READ, NOT ASSUMED.** ### The first
# ### run asked for `| 266 |` by address and banked a miss; the row b416 wrote carries b416's own
# ### marker, and the number it sits at is what the table says.
B416MARK = 'THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM'
mrow = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| \*\*' + re.escape(B416MARK), corr)]
say('  the ferry cites correspondence row     : 266')
say('  the row carrying b416`s marker is      : %s   (last row of the table %s)'
    % (mrow or 'NONE', max(rows) if rows else '-'))
say('  a row numbered 266 exists              : %s' % (266 in rows))
if not mrow:
    MISS.append('the row carrying b416`s marker is absent')
elif mrow[0] != 266:
    say('  ### ### **THE CITATION`S OBJECT IS PRESENT AND ITS NUMBER IS NOT 266.** ### b416`s own')
    say('  ### desk appended row %d; its closing message printed 266, and the ferry carries the' % mrow[0])
    say('  ### closing`s figure. ### **AND THE NEXT ROW THIS ACT APPENDS WILL BE 266**, so a later')
    say('  ### arm asking for `| 266 |` by address would pass on THIS act`s row, not b416`s.')
cl = read(os.path.join(D, 'b416_closing.txt'))
say('  b416`s four-tuple table in its closing : %s'
    % ('| B | **3** | **2** | 2 | 0 |' in cl or 'classB' in cl))
reg = read(os.path.join(PP, 'REGISTRY.md'))
say('  registry row p2-35 present             : %s' % bool(re.search(r'(?m)^\| p2-35 \|', reg)))
if not re.search(r'(?m)^\| p2-35 \|', reg):
    MISS.append('registry row p2-35 is absent')
say()

# =============================================================================================
rule()
say('### READ 1 -- THE SENTENCE AND THE TUPLES, FROM THE DOCUMENT THAT OWNS BOTH.')
rule()
quote('the sentence, in the abstract', MATTER, 'Three of four formation components are universal',
      'Planck 2018 measures')
say()
quote('the sentence, in section I', MATTER, 'Three of four components are universal', '**Theorem (n₂ = 3).**')
quote('its n2 theorem, with its hypothesis', MATTER, '**Theorem (n₂ = 3).**', NL)
quote('its n3 theorem, with its hypothesis', MATTER, '**Theorem (n₃ = 2).**', NL)
quote('its n4 theorem, with its hypothesis', MATTER, '**Theorem (n₄ = 0).**', NL)
say()
quote('the tuples, in the same section', MATTER, '| Class | Substrate | (n₁, n₂, n₃, n₄)',
      'Class A`s tuple' if False else "Class A's tuple is theorem-forced", width=110, cap=900)
say()
mt = read(MATTER)
owner_rows = re.findall(r'(?m)^\| ([ABCD]) — (\w+) \| ([^|]+) \| \((\d), (\d), (\d), (\d)\) \| (\d+) \| ([^|]+) \|', mt)
say('  ### the owner`s table, parsed : %d rows' % len(owner_rows))
for r in owner_rows:
    say('      %s %-14s (%s,%s,%s,%s)  examples: %s' % (r[0], r[1], r[3], r[4], r[5], r[6], r[8].strip()))
if len(owner_rows) != 4:
    MISS.append('the owner`s class table did not parse to four rows')
say()
say('  ### ### **THE OWNER`S OWN DOCUMENT CARRIES BOTH HALVES.** ### The sentence calls `n2`')
say('  ### universal at 3, and the table eleven lines below it gives `B` and `D` the value 2. ### The')
say('  ### abstract does the same inside one paragraph: it states the universality and then lists')
say('  ### `9/32` and `1/4`, which are the values of tuples whose `n2` is 2.')
say()

# =============================================================================================
rule()
say('### READ 2 -- THE KERNEL`S DECLARATIONS AND THE FIGURES ITS OWN HEADER PRINTS.')
rule()
cls = read(os.path.join(FA, 'Classes.lean'))
tup = {m[0]: tuple(int(x) for x in m[1:]) for m in
       re.findall(r'def (class[ABCD]) : FormationTuple := .(\d+), (\d+), (\d+), (\d+).', cls)}
# ### **REPAIRED AFTER ITS FIRST RUN, AND SAID SO:** ### the first pattern stopped at the nested
# ### parenthesis in `(Gauge, SU(N))` and read three header figures, not four -- a defect of this
# ### survey's matcher and not of the header. ### The first run's record is `b417_extract` run 1.
hdr = {m[0]: Fraction(int(m[1]), int(m[2])) for m in
       re.findall(r'Class ([ABCD]) \(.*?\):\s*\(\d, \d, \d, \d\)\s*→ Ω = (\d+)/(\d+)', cls)}
say('  declarations read from Classes.lean : %d ; header Omega figures read : %d' % (len(tup), len(hdr)))
if len(tup) != 4 or len(hdr) != 4:
    MISS.append('the kernel declarations or header figures did not read as four')
core = read(os.path.join(FA, 'Core.lean'))
say('  the formula, from Core.lean : totalCount = n2^(n1+n3) %s ; primitiveCount = n1^n3 %s'
    % ('t.n2 ^ (t.n1 + t.n3)' in core, 't.n1 ^ t.n3' in core))


def omega(t):
    n1, n2, n3, _n4 = t
    return Fraction(n1 ** n3, n2 ** (n1 + n3))


say()
say('  %-7s %-14s %-12s %-12s %-8s' % ('class', 'tuple', 'Omega calc', 'header', 'agree'))
for k in ('A', 'B', 'C', 'D'):
    t = tup.get('class' + k)
    if not t:
        continue
    w = omega(t)
    say('  %-7s %-14s %-12s %-12s %-8s' % (k, str(t), str(w), str(hdr.get(k)), w == hdr.get(k)))
pairs = {k: (tup['class' + k][0] ** tup['class' + k][2],
             tup['class' + k][1] ** (tup['class' + k][0] + tup['class' + k][2]))
         for k in ('A', 'B', 'C', 'D') if 'class' + k in tup}
say('  (primitive, total) pairs as the theorems state them : %s' % pairs)
say('  distinct pairs : %d' % len(set(pairs.values())))
say()
say('  ### **THE ARITHMETIC OF `(N4)`**: `n3` and `n4` are constant across the four tuples and `n1`')
say('  ### takes two values. ### If `n2` were constant too, a pair would be fixed by `n1` alone:')
n1vals = sorted(set(t[0] for t in tup.values()))
say('      values n1 takes : %s ; so with n2 held at any one value, distinct pairs <= %d'
    % (n1vals, len(n1vals)))
say()

# =============================================================================================
rule()
say('### READ 3 -- WHO CITES WHAT: THE SENTENCE, THE TUPLES THAT DISAGREE WITH IT, OR BOTH.')
rule()
say('  ### population : PLACE-papers `.md` outside archive/, outputs/, heritage/, internal/;')
say('  ### the ledgers excluded by `b416`s carrier rule. ### **SEARCHED BY PYTHON, NOT `rg`.**')
SENT = re.compile(r'universal across IDS-amenable|[Tt]hree of (?:the )?four (?:formation )?'
                  r'components (?:are|is) universal|n(?:₂|_2|_\{2\})\s*=\s*3 by Chevalley')
U2 = re.compile(r'every Dedekind zeta function has|universal across (?:all )?(?:Dedekind|completed '
                r'L-functions)|Formation Universality|formation count is universal across Dedekind')
U3 = re.compile(r'formation total is invariant across')
DIS = re.compile(r'\(\s*3\s*,\s*2\s*,\s*2\s*,\s*0\s*\)|\(\s*2\s*,\s*2\s*,\s*2\s*,\s*0\s*\)'
                 r'|\b9\s*/\s*32\b|\\frac\{9\}\{32\}')
ANYT = re.compile(r'\(\s*[23]\s*,\s*[23]\s*,\s*2\s*,\s*0\s*\)')
both, sent_only, tup_only = [], [], []
for rel, src in live_docs():
    s, t = bool(SENT.search(src)), bool(DIS.search(src))
    if s and t:
        both.append(rel)
    elif s:
        sent_only.append(rel)
    elif t:
        tup_only.append(rel)
say('  ### **POSITIVE CONTROL -- the owner must be found carrying BOTH, first.**')
ctl = 'phase2/physics/MATTER_AS_ARITHMETIC.md' in both
say('      MATTER_AS_ARITHMETIC in the BOTH bucket : ### **%s**' % ctl)
if not ctl:
    MISS.append('the citation control failed: the owner is not found carrying both halves')
say()
say('  ### ### **LIVE DOCUMENTS CITING THE SENTENCE AND THE DISAGREEING TUPLES BOTH : %d**' % len(both))
for r in both:
    say('      %s' % r)
say('  ### ### **CITING THE SENTENCE AND NOT THE DISAGREEING TUPLES : %d**' % len(sent_only))
for r in sent_only:
    say('      %s' % r)
say('  ### ### **CITING THE DISAGREEING TUPLES AND NOT THE SENTENCE : %d**' % len(tup_only))
for r in tup_only:
    say('      %s' % r)
say('  ### ### **LIVE DOCUMENTS CITING THE SENTENCE AT ALL : %d**' % (len(both) + len(sent_only)))
say()
say('  ### **A SECOND SHAPE, BEFORE ANY CEILING IS BANKED:** ### any paragraph naming `universal`')
say('  ### together with the second component or its theorem, in any spelling.')
WIDE_U = re.compile(r'universal', re.I)
WIDE_N2 = re.compile(r'n₂|n_2|n_\{2\}|\bn2\b|Chevalley|transformation count|three-level covering', re.I)
wide = []
for rel, src in live_docs():
    for para in re.split(r'\n\s*\n', src):
        if WIDE_U.search(para) and WIDE_N2.search(para):
            wide.append((rel, re.sub(r'\s+', ' ', para).strip()))
wdocs = sorted(set(r for r, _p in wide))
say('      paragraphs : %d ; documents : %d' % (len(wide), len(wdocs)))
for rel in wdocs:
    ps = [p for r, p in wide if r == rel]
    say('      %-58s %d paragraph(s)   first shape finds it : %s'
        % (rel[:58], len(ps), rel in both or rel in sent_only))
    for seg in wrap(ps[0][:300], 88):
        say('          %s' % seg)
say('  ### ### **THE RESIDUE -- found by the second shape and not the first -- IS HAND-READ IN THE')
say('  ### ### COMPONENTS, NOT SCORED HERE.** ### A word match is a mention, not a citation.')
say()

# =============================================================================================
rule()
say('### READ 4 -- THE THREE DOCUMENTS THAT ARGUE `n4`: WHICH UNIVERSALITY EACH ASSERTS, WHICH TUPLE.')
rule()
say('  ### **THREE DIFFERENT CLAIMS CARRY THE WORD `universal` IN THIS CLUSTER, AND `(R28)` KEEPS')
say('  ### ### THEM APART:** ### (U1) the owner`s -- `n2`, `n3`, `n4` universal ACROSS IDS-AMENABLE')
say('  ### SYSTEMS, i.e. across CLASSES; ### (U2) the tuple `(2,3,2,0)` universal ACROSS DEDEKIND ZETA')
say('  ### FUNCTIONS, i.e. inside class A; ### (U3) the formation TOTAL invariant across *the')
say('  ### IDS-amenable cluster*. ### `(N5)` names *the universality sentence*, which is (U1).')
for nm, p in (('MATTER_AS_ARITHMETIC', MATTER), ('COMPLEX_ANALYSIS', CPLX),
              ('BSD_VIA_FORMATION_TRANSFER', BSD)):
    src = read(p)
    tl = sorted(set(re.sub(r'\s+', '', m.group(0)) for m in ANYT.finditer(src)))
    say('  %-28s U1 %-5s U2 %-5s U3 %-5s tuples cited: %s'
        % (nm, bool(SENT.search(src)), bool(U2.search(src)), bool(U3.search(src)),
           ', '.join(tl) or 'NONE'))
say()
quote('COMPLEX_ANALYSIS`s U2, abstract', CPLX, 'This formation is universal:', 'The seven tools')
quote('COMPLEX_ANALYSIS`s U3', CPLX, 'FORMATION_UNIVERSALITY_v3 carries', NL)
quote('BSD`s invariance', BSD, 'but the formation count is invariant', '.')
quote('COMPLEX_ANALYSIS`s own caveat on tuples', CPLX, '> **Note (Gate 1b).**', NL)
say()
say('  ### **AND A SECOND DISAGREEMENT, OF A DIFFERENT KIND, BETWEEN TWO OF THE THREE:** ### the')
say('  ### example SYSTEMS each document places at a tuple.')
cp = read(CPLX)
cx_rows = re.findall(r'(?m)^\| \$\((\d), (\d), (\d), (\d)\)\$ \| (\d+) \| ([^|]+) \| ([^|]+) \|', cp)
cx = {}
for r in cx_rows:
    for ex in r[6].split(','):
        cx[ex.strip()] = '(%s,%s,%s,%s)' % r[:4]
mx = {}
for r in owner_rows:
    for ex in r[8].split(','):
        mx[ex.strip()] = '(%s,%s,%s,%s)' % (r[3], r[4], r[5], r[6])
say('      COMPLEX_ANALYSIS table rows parsed : %d ; systems named : %d' % (len(cx_rows), len(cx)))
KEYS = (('genetic code', 'genetic code'), ('Shannon', 'Shannon'), ('Navier-Stokes', 'Navier-Stokes'),
        ('Yang-Mills', 'Yang-Mills'), ('Dirichlet', 'Dirichlet'))
disagree = []
for lbl, key in KEYS:
    a = [v for k, v in mx.items() if key.lower() in k.lower()]
    b = [v for k, v in cx.items() if key.lower() in k.lower()]
    if a and b:
        same = set(a) == set(b)
        say('      %-16s MATTER %-12s COMPLEX_ANALYSIS %-12s %s'
            % (lbl, ','.join(sorted(set(a))), ','.join(sorted(set(b))),
               'agree' if same else '### **DISAGREE**'))
        if not same:
            disagree.append(lbl)
say('  ### ### **SYSTEMS THE TWO DOCUMENTS PLACE AT DIFFERENT TUPLES : %d** -- %s'
    % (len(disagree), ', '.join(disagree) or 'none'))
say()

# =============================================================================================
rule()
say('### READ 5 -- READING (b)`S WEAKENING: WHAT THE THEOREMS` OWN HYPOTHESES NAME.')
rule()
say('  ### The n2 theorem`s hypothesis names `Connected reductive symmetry groups`. ### Does any')
say('  ### live document say whether the substrates of `B` or `D` carry such a group?')
RED = re.compile(r'reductive', re.I)
BD = re.compile(r'diffeomorphism|σ-algebra|sigma-algebra|Gravitational|Information substrate', re.I)
hits = []
for rel, src in live_docs():
    for para in re.split(r'\n\s*\n', src):
        if RED.search(para) and BD.search(para):
            hits.append((rel, re.sub(r'\s+', ' ', para).strip()[:260]))
say('  paragraphs naming `reductive` together with a B or D substrate : ### **%d**' % len(hits))
for rel, s in hits[:6]:
    say('      %s' % rel)
    for seg in wrap(s, 90):
        say('          %s' % seg)
say()

# =============================================================================================
rule()
say('### READ 6 -- THE SECOND TOOL: WHAT `b369_hygiene.py` NAMES, AND WHAT IT WOULD WRITE.')
rule()
hsrc = read(HYG)
m = re.search(r"HOOKSRC = os\.path\.join\(ROOT, ([^)]*)\)", hsrc)
segs = re.findall(r"'([^']+)'", m.group(1)) if m else []
hp = os.path.join(ROOT, *segs) if segs else ''
say('  HOOKSRC names : %s   exists on disk : %s' % ('/'.join(segs), os.path.exists(hp) if hp else '-'))
say('  the single source b386 left, `.githooks/pre-push`, exists : %s'
    % os.path.exists(os.path.join(ROOT, '.githooks', 'pre-push')))
say('  its `installed` check reads : %s'
    % ('SIDE-effects/.git/hooks/pre-push' if "os.path.join(KERNEL, '.git', 'hooks', 'pre-push')" in hsrc
       else '(not the .git/hooks path)'))
say('  it runs `b304_hooks.py` : %s' % ('subprocess.run([sys.executable, HOOKS]' in hsrc))
say()
say('  ### **ITS WRITE SURFACE, READ FROM ITS SOURCE, BEFORE ANY RUN:**')
say('      run_clock notes under the stem `b369_hygiene_notes` (versioned, never overwritten)')
say('      data/b369_hooks.txt            %s' % ("'b369_hooks.txt'" in hsrc))
say('      data/b369_hygiene.json         %s' % ("'b369_hygiene.json'" in hsrc))
say('      tools/b303_pins.py, tools/b304_hooks.py  (roster and wording mends, idempotent)')
say('      ### and, through `b304_hooks.py`: each rostered repository`s `.githooks/pre-push`, a')
say('      ### `.b304-backup*` beside any hook it replaces, and a THROWAWAY COMMIT on a scratch')
say('      ### branch in every clean repository, deleted after a `--dry-run` push.')
say()
say('  ### **THE BROKEN TOOL, RUN AS IT STANDS, WITH ITS WRITE SURFACE CAPTURED:**')
WATCH = [os.path.join(D, f) for f in ('b369_hooks.txt', 'b369_hygiene.json')] + \
        [os.path.join(T, 'b303_pins.py'), os.path.join(T, 'b304_hooks.py')]
pre = {w: rb(w) for w in WATCH}
pre_notes = sorted(f for f in os.listdir(D) if f.startswith('b369_hygiene_notes'))
r = subprocess.run([sys.executable, HYG], capture_output=True, text=True, encoding='utf-8',
                   errors='replace', timeout=600)
post_notes = sorted(f for f in os.listdir(D) if f.startswith('b369_hygiene_notes'))
changed = [os.path.basename(w) for w in WATCH if rb(w) != pre[w]]
new_notes = [f for f in post_notes if f not in pre_notes]
err = (r.stderr or '').strip().splitlines()
say('      exit code : %d' % r.returncode)
say('      last stderr line : %s' % (err[-1][:110] if err else '(none)'))
say('      ### ### **FILES OF ITS WRITE SURFACE CHANGED BY THE BROKEN RUN : %d ; NEW RUN RECORDS : %d**'
    % (len(changed), len(new_notes)))
for c in changed + new_notes:
    say('          %s' % c)
say('  ### ### **A BROKEN TOOL IS SAFE BY BEING BROKEN** -- measured here, not asserted: it dies')
say('  ### before its first write, on the retired path.')
say()
say('  ### **THE RESIDUE BACKUPS IN `SIDE-effects`, AND WHETHER THEIR BYTES SURVIVE IN ANY OBJECT STORE:**')
gh = os.path.join(FX, '.githooks')
baks = sorted(f for f in os.listdir(gh) if '.b304-backup' in f) if os.path.isdir(gh) else []
say('      backups found : %d' % len(baks))
for f in baks:
    p = os.path.join(gh, f)
    b = rb(p)
    raw = hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
    lf = b.replace(b'\r\n', b'\n')
    nrm = hashlib.sha1(b'blob %d\0' % len(lf) + lf).hexdigest()
    inx = [nm for nm, repo in (('SIDE-effects', FX), ('relay', ROOT))
           if git(repo, 'cat-file', '-e', raw)[0] == 0 or git(repo, 'cat-file', '-e', nrm)[0] == 0]
    tracked = git(FX, 'ls-files', '--error-unmatch', os.path.join('.githooks', f))[0] == 0
    say('      %-28s %5d bytes  sha256 %s  tracked %-5s  blob in : %s'
        % (f, len(b), hashlib.sha256(b).hexdigest()[:16], tracked, ', '.join(inx) or '### NONE'))
say()

# =============================================================================================
rule()
say('### READ 7 -- THE THIRTEEN `Core/` CAVEATS, AND EVERY RECORD THAT NAMES EACH ONE.')
rule()
NOTC = re.compile(r'[^.]{0,300}\b(?:is|are) NOT compiled|[^.]{0,300}\bnot compiled here'
                  r'|[^.]{0,300}\bIS NOT COMPILED', re.I)
caveats = []
for f in sorted(os.listdir(CORE)):
    if f.endswith('.lean'):
        src = read(os.path.join(CORE, f))
        for mm in NOTC.finditer(src):
            caveats.append((f, src[:mm.end()].count(NL) + 1, re.sub(r'\s+', ' ', mm.group(0)).strip()))
say('  ### `b416`s description, re-run unchanged : ### **%d caveats in %d files**'
    % (len(caveats), len(set(c[0] for c in caveats))))
if len(caveats) != 13:
    MISS.append('the caveat description no longer yields thirteen')
# ### **ONE ANCHOR PER CAVEAT, CHOSEN FROM ITS OWN TEXT**, so the five in the seal are told apart.
ANCH = {}
for idx, (f, ln, s) in enumerate(caveats):
    if f != 'FiniteSideSeal.lean':
        ANCH[idx] = f[:-5]
    elif 'exactly when `p` is prime' in s or 'unit of `Z/p^k`' in s:
        ANCH[idx] = '(T1.4)'
    elif 'Tr(theta(t) Pi)' in s:
        ANCH[idx] = 'Tr(theta(t) Pi)'
    elif 'dvd_iff_mod_eq_zero' in s:
        ANCH[idx] = 'dvd_iff_mod_eq_zero'
    elif 'coprimality form' in s:
        # ### WIDENED after run 1 found 0 records under `coprimality form`: the stem, not the phrase.
        ANCH[idx] = 'coprimality'
    elif '`Nat.Coprime` form is not compiled' in s or 'Coprime` form is not compiled' in s:
        ANCH[idx] = 'scaling_shift_inverse'
    else:
        ANCH[idx] = 'FiniteSideSeal'
recs = sorted(f for f in os.listdir(D) if re.match(r'b\d+_.*\.txt$', f)
              and not f.startswith(('b416_', 'b417_')))
RECTXT = {f: read(os.path.join(D, f)) for f in recs}
say('  act records searched (relay data/, b416 and b417 excluded -- they only list) : %d' % len(recs))
say('  ### **POSITIVE CONTROL -- `(T1.4)` must be named by b413 or b414, which tested it.**')
t14 = [f for f, s in RECTXT.items() if '(T1.4)' in s and f.startswith(('b413_', 'b414_'))]
say('      records of b413/b414 naming `(T1.4)` : ### **%d**' % len(t14))
if not t14:
    MISS.append('the caveat-record control failed: no b413/b414 record names (T1.4)')
say()
for idx, (f, ln, s) in enumerate(caveats, start=0):
    a = ANCH[idx]
    who = sorted(set(re.match(r'(b\d+)_', x).group(1) for x, t in RECTXT.items() if a in t),
                 key=lambda x: int(x[1:]))
    say('  [%2d] %-30s line %-4d anchor %-24s acts naming it : %d  %s'
        % (idx + 1, f, ln, repr(a)[:24], len(who), ', '.join(who[:14])))
    for seg in wrap(s[-230:], 90):
        say('         %s' % seg)
say()

# =============================================================================================
rule()
say('### READ 8 -- WHAT EACH READING WOULD MOVE: THE KERNEL`S STATED FIGURES UNDER READING (a).')
rule()


def figs(t):
    n1, n2, n3, _ = t
    tot, prim = n2 ** (n1 + n3), n1 ** n3
    return dict(total=tot, primitive=prim, remainder=tot - prim, wall=n2 ** n1, omega=omega(t))


RA = dict(tup)
RA['classB'] = (tup['classB'][0], 3, tup['classB'][2], tup['classB'][3])
RA['classD'] = (tup['classD'][0], 3, tup['classD'][2], tup['classD'][3])
say('  reading (a) tuples : B %s -> %s ; D %s -> %s'
    % (tup['classB'], RA['classB'], tup['classD'], RA['classD']))
say('  ### reading (a)`s B equals C`s tuple : %s ; its D equals A`s tuple : %s'
    % (RA['classB'] == tup['classC'], RA['classD'] == tup['classA']))
thm = re.findall(r'theorem (class[ABCD])_(total|primitive|remainder|wall) : \w+ class[ABCD] = (\d+)', cls)
say('  kernel theorems stating a figure : %d' % len(thm))
for name, kind, val in thm:
    now = figs(tup[name])[kind]
    ra = figs(RA[name])[kind]
    say('      %s_%-10s states %-5s reading (b) %-5s reading (a) %-5s %s'
        % (name, kind, val, now, ra, 'unmoved' if ra == int(val) else '### **MOVES**'))
dist = re.findall(r'theorem classA_distinct_from_(class[BCD])', cls)
for other in dist:
    pa = (figs(RA['classA'])['primitive'], figs(RA['classA'])['total'])
    po = (figs(RA[other])['primitive'], figs(RA[other])['total'])
    say('      classA_distinct_from_%s : true now ; under reading (a) %s'
        % (other, 'TRUE' if pa != po else '### **FALSE -- THE THEOREM WOULD NOT COMPILE**'))
say()
ob, sd = 0.04930, 0.00066
say('  the owner`s Planck figure : Omega_b = %.5f +- %.5f' % (ob, sd))
for k in ('A', 'B', 'C', 'D'):
    w0, wa = omega(tup['class' + k]), omega(RA['class' + k])
    say('      %s  now %-6s %7.2f sigma    reading (a) %-6s %7.2f sigma   %s'
        % (k, w0, abs(float(w0) - ob) / sd, wa, abs(float(wa) - ob) / sd,
           'unmoved' if w0 == wa else '### **MOVES**'))
say()

# =============================================================================================
rule()
say('### READ 9 -- `P` AGAINST THE CORPUS`S LIVE USE OF IT. ### (A SEPARATE SUBJECT FROM READS 1-8.)')
rule()
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337]
CTX = re.compile(r'[Pp]rime [Cc]ore|PRIME CORE|P-ZONE|𝒫|\\mathcal\{P\}|\bP\s*=\s*\\?\{')


def cited(src):
    got = set()
    for para in re.split(r'\n\s*\n', src):
        if CTX.search(para):
            for v in P:
                if re.search(r'(?<![0-9./])%d(?![0-9./])' % v, para):
                    got.add(v)
    return got


ctlset = cited(read(READER))
say('  ### **POSITIVE CONTROL -- the placed Reader, scored by the same predicate, first.**')
say('      members of P the Reader cites in its own Prime-Core paragraphs : ### **%d of 15**'
    % len(ctlset))
if len(ctlset) != 15:
    MISS.append('the P-use control failed: the Reader does not score 15 of 15')
per = {v: [] for v in P}
docs_any = 0
for rel, src in live_docs():
    g = cited(src)
    if g:
        docs_any += 1
    for v in g:
        per[v].append(rel)
say('  live documents with at least one Prime-Core paragraph citing a member : %d' % docs_any)
for v in P:
    say('      %-4d cited in %2d live document(s)   %s'
        % (v, len(per[v]), ', '.join(per[v][:3]) + (' ...' if len(per[v]) > 3 else '')))
dropped = [v for v in P if not per[v]]
say('  ### ### **MEMBERS STILL CITED : %d. ### MEMBERS DROPPED : %d** %s'
    % (len(P) - len(dropped), len(dropped), dropped or ''))
say()
say('  ### **THE DESERT SENTENCE, SEARCHED EVERYWHERE, CONTROL FIRST:**')
DES = re.compile(r'arithmetic desert|deserts? where no sum|no sum of powers yields', re.I)
say('      found in the placed Reader (control) : ### **%s**' % bool(DES.search(read(READER))))
if not DES.search(read(READER)):
    MISS.append('the desert-sentence control failed')
live_d = [rel for rel, src in live_docs() if DES.search(src)]
all_d = []
for root, dirs, files in os.walk(PP):
    if '.git' in root.split(os.sep):
        continue
    for f in files:
        if f.endswith('.md') and DES.search(read(os.path.join(root, f))):
            all_d.append(os.path.relpath(os.path.join(root, f), PP).replace(os.sep, '/'))
say('      ### ### **LIVE DOCUMENTS ASSERTING IT : %d** %s' % (len(live_d), live_d or ''))
say('      every `.md` in the repository carrying it, ledgers and archive included : %d' % len(all_d))
for a in all_d:
    say('          %s' % a)
say()
CONST = os.path.join(PP, 'phase1.5', 'deep-structure', 'CONSTANCE.md')
say('  ### **THE LIVE CARRIER, READ IN ITS OWN WORDS -- IS IT A QUOTATION OF THE READER OR ITS OWN?**')
quote('CONSTANCE, its own lattice sentence', CONST, 'Beyond 41, the lattice has gaps.', NL)
quote('CONSTANCE, its desert sentence', CONST, 'The structure is not continuous.', NL)
quote('CONSTANCE, its second desert sentence', CONST, 'The gaps between lattice primes', NL)
say('  the Reader`s wording present verbatim in CONSTANCE : %s'
    % ('where no sum of powers yields a prime' in read(CONST)))
csum = {v: [(a, b) for a in range(0, 9) for b in range(0, 6) if 2 ** a + 3 ** b == v]
        for v in (43, 47, 53)}
for v in (43, 47, 53):
    say('      CONSTANCE says no combination of powers yields %d ; 2^a + 3^b = %d at : %s'
        % (v, v, csum[v] or 'none'))
say()

# =============================================================================================
rule()
say('### READ 10 -- THE LATTICE, RECOMPUTED, AND WHAT THE RECORD SAYS ABOUT IT.')
rule()


def isprime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


sums = sorted({2 ** a + 3 ** b for a in range(0, 12) for b in range(0, 8)})
sp = [v for v in sums if isprime(v)]
under100 = [v for v in sp if v < 100 and v not in P]
desert = [v for v in sp if 41 < v < 137]
say('  sum-of-powers primes below 100 outside P : ### **%d** -- %s'
    % (len(under100), ', '.join(map(str, under100))))
say('  sum-of-powers primes strictly between 41 and 137 : ### **%d** -- %s'
    % (len(desert), ', '.join(map(str, desert))))
say()
quote('the Reader`s desert sentence', READER, 'These **jump primes** are separated', NL)
quote('the Reader`s predictions, naming gap elements', READER,
      '- Dark matter particle masses may involve gap elements', NL)
named = [v for v in (23, 43, 47, 67) if v in desert]
say('  gap elements the predictions name that lie in the desert as sums of powers : %s' % named)
say()
say('  ### **WHAT THE RECORD SAYS THE DESERT HOLDS:**')
b416x = read(os.path.join(D, 'b416_extract.txt'))
m9 = re.search(r'BETWEEN 41 AND 137 [^#]*### (\d+)', b416x)
say('      b416`s own extract                    : %s' % (m9.group(1) if m9 else '(anchor miss)'))
for lbl, p in (('b416`s bank', os.path.join(D, 'b416_the_reader_placed.txt')),
               ('registry row p2-35', os.path.join(PP, 'REGISTRY.md')),
               ('b416`s correspondence row', os.path.join(KERN, 'CORRESPONDENCE.md'))):
    src = read(p)
    k = re.search(r'lattice carries (?:\*\*)?(six|seven|nine|\d+)(?:\*\*)? sum-of-powers primes', src)
    say('      %-38s : %s' % (lbl, k.group(1) if k else '(no count stated)'))
say('  ### ### **THE PRIOR RECORD STATES A COUNT ITS OWN EXTRACT DOES NOT.** ### Reported, and not')
say('  ### repaired: a banked record and a registry row are not this act`s to edit.')
say()

# =============================================================================================
rule()
say('### READ 11 -- WHERE THE SPECIES IS FILED, AND THE INCIDENT IT CARRIES.')
rule()
MOD = os.path.join(TECHNE, 'modules', '2026-09')
for f in ('DATED_ARM.md', 'GUARD_WITH_NOTHING_LISTENING.md'):
    say('  %-36s present : %s' % (f, os.path.exists(os.path.join(MOD, f))))
rc, lr = git(TECHNE, 'rev-list', '--left-right', '--count', 'origin/main...HEAD')
say('  TECHNE-Core origin/main...HEAD, left-right (ORIGIN-ONLY FIRST, then LOCAL-ONLY) : %s' % lr)
rc, st = git(TECHNE, 'status', '--porcelain')
say('  TECHNE-Core untracked entries not this act`s : %d' % len([x for x in st.splitlines() if x.startswith('??')]))
b416c = read(os.path.join(D, 'b416_components.txt'))
for lbl, needle in (('the retired path', 'now names ### **`.githooks`**'),
                    ('the SameFileError it hid', 'SameFileError'),
                    ('the prior record rewritten', 'prior-act records the run modified : ### **1**')):
    say('  b416`s incident -- %-28s in its record : %s' % (lbl, needle in b416c or needle in read(
        os.path.join(D, 'b416_the_reader_placed.txt'))))
say()

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : 12')
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')

io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if MISS else 0)
