# -*- coding: utf-8 -*-
"""b416_desk_bank.py -- THE DESK, THE REGISTRY ROW, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY
### AND THE BANK.

### ### **THE THREE CARRIERS ARE MEASURED, NOT CHOSEN.** ### `(R32)` says the row names where the
### Reader's content already lives; which documents those are is decided by counting how many
### members of `P` each live document carries, not by this seat's taste.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
REG = os.path.join(PP, 'REGISTRY.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b416 the two stipulations named, the dated instrument repaired, the reader placed -->'
PRIOR = '<!-- b415 the substrate at grade, the four tuples, and the sibling partition screened -->'
BANKOUT = os.path.join(D, 'b416_the_reader_placed.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


FACE = read(os.path.join(D, 'b416_registration_2026-09-11.txt'))
SEALHASH = re.search(r'([0-9a-f]{64})', FACE.split('LOCK')[-1]).group(1)
LG = json.load(io.open(os.path.join(D, 'b416_lockgate.json'), encoding='utf-8'))
GR, GDG = LG['gates_read'], LG['face_subject_gates']
COMP = read(os.path.join(D, 'b416_components.txt'))
PLACE = read(os.path.join(D, 'b416_place.txt'))
FIG = read(os.path.join(D, 'b416_figure.txt'))
EXT = read(os.path.join(D, 'b416_extract.txt'))
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337]


def carriers():
    """### **MEASURED, AND THE MEASUREMENT TIES.** ### Every live document naming at least ten of
    the fifteen and three of the four hard ones is a carrier; the count does NOT discriminate
    between them, so it is reported and a SECOND, STATED rule picks the three."""
    scored = []
    for root, _dirs, files in os.walk(PP):
        if any(x in root for x in ('.git', 'archive', 'outputs', 'heritage', 'internal')):
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            # ### **A LEDGER IS NOT A CARRIER.** ### `OPEN_TRAILS`, `FINDINGS`, `REGISTRY` and
            # ### their siblings name every member of `P` because ACTS WRITE ABOUT THEM there.
            # ### ### **A RECORD OF WORK ON A SET IS NOT A DOCUMENT THAT CARRIES THE SET.**
            if f in ('OPEN_TRAILS.md', 'FINDINGS.md', 'REGISTRY.md', 'VERIFICATION_LOOM.md',
                     'CORRESPONDENCE.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'BIBLIOGRAPHY.md',
                     'MIGRATION.md', 'FACES_LEDGER.md', 'README.md',
                     'EMERGING_RESEARCH_PROGRAMMES.md', 'CASCADE_ANCHORS_CORRECTED.md'):
                continue
            p = os.path.join(root, f)
            src = read(p)
            got = [v for v in P if re.search(r'(?<![0-9./])%d(?![0-9./])' % v, src)]
            big = [v for v in (23, 53, 137, 337) if
                   re.search(r'(?<![0-9./])%d(?![0-9./])' % v, src)]
            if len(got) >= 10 and len(big) >= 3:
                named = len(re.findall(r'[Pp]rime [Cc]ore', src))
                scored.append((len(big), len(got), named,
                               os.path.relpath(p, PP).replace(os.sep, '/')))
    scored.sort(key=lambda r: (-r[0], -r[1], -r[2], r[3]))
    return scored


SCORED = carriers()
# ### **THE FERRY NAMES CONSTANCE. ### THE OTHER TWO ARE PICKED BY A STATED RULE:** ### the
# ### live carriers that name the set AS A SET most often, ties broken alphabetically so the
# ### answer does not depend on the order a directory walk returns.
CONST = 'phase1.5/deep-structure/CONSTANCE.md'
_rest = [r for r in SCORED if r[3] != CONST]
_rest.sort(key=lambda r: (-r[2], r[3]))
TOP3 = [CONST] + [r[3] for r in _rest[:2]]

DESK = [
    ('the four open lists', 'STANDING', 'None fires on this act.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('b321’s face; SIDE-window’s guard; the KINDS write-list shortfall', 'STANDING',
     'ROUTED and still routed.'),
    ('`n1` and `n4`, from owners', 'CLOSE',
     'NAMED. ### `n1` = **independent algebraic channels through which the specification accesses '
     'the substrate**; `n4` = **mechanism classes contributed by the bindings between stages**. '
     'Owner: `phase2/physics/MATTER_AS_ARITHMETIC.md` §I. ### **NEITHER HAS EVER HAD A '
     'DERIVATION ROUTE PRICED.**'),
    ('`(N1)`, the claim that nothing argues `n4`', 'CLOSE',
     '**SPLIT UNDER (R27): MET IN PREMISE, REFUTED IN CONCLUSION.** ### Three documents argue it '
     'and the owner names **Schur’s lemma**. ### The unargued component is `n1` — and it is '
     'unargued because the owner declares it **FREE**.'),
    ('the universality sentence against the declarations', 'CLOSE',
     '**THEY DISAGREE.** ### The owner calls `n2`, `n3`, `n4` universal; the kernel declares '
     '`classB.n2 = 2` and `classD.n2 = 2`. ### **A UNIVERSAL REASON CANNOT DERIVE A COMPONENT IN '
     'A CLASS WHERE THAT COMPONENT HAS ANOTHER VALUE** — which is why b415 found 0 derived '
     'components in B, C and D. ### **THE STIPULATION IS NOT LAZINESS.**'),
    ('deriving `n1` at class A', 'CLOSE',
     'PRICED AT **AT LEAST TWO ACTS, AND THE FIRST IS NOT A BUILD** — the corpus must first say '
     'what an algebraic channel IS and whether the channels of ℤ are in bijection with the '
     'substrate’s generators. ### **THE COMPILED `2` COUNTS PRIMES AND `n1` COUNTS CHANNELS; '
     '(R28) FORBIDS WIRING THEM.** ### And it may be unbuildable: `n1` is the class label.'),
    ('`tools/b371_hookpath.py`', 'CLOSE',
     '**REPAIRED AND RUNNING.** ### Two edits, not one: the retired path, and then the '
     '`SameFileError` the path change exposed — **repointing it revealed a defect it had been '
     'hiding**. ### And running it re-wrote a prior act’s record, which was captured before the '
     'run and restored after: **1 modified, 1 restored, 0 still differing.**'),
    ('`tools/b369_hygiene.py`', 'STANDING',
     'ROUTED. ### It breaks on the same retired path for the same reason and its repair is one '
     'line, **but the ferry orders one tool repaired and the write list names one.** ### An act '
     'that repairs what it was not asked to repair has widened its own order.'),
    ('the `(T1.4)` annotation', 'STANDING',
     'DRAFTED AND NOT APPLIED, with its exact bytes shown — **+4 lines, 0 removed** — and the '
     'sealed file’s sha256 identical before and after. ### **AWAITS THE AUTHOR’S APPROVAL.**'),
    ('the other kernel caveats', 'CLOSE',
     'COUNTED BY DESCRIPTION UNDER A CONTROL THAT HOLDS: **13 across `Core/` in 9 files, 5 of '
     'them in the seal, so 8 elsewhere.** ### **COUNTED, NOT GRADED** — b414 showed one of this '
     'shape can be right on its own evidence and wrong off it.'),
    ('the Prime Core Reader', 'CLOSE',
     'PLACED under `(R32)` at `heritage/PRIME_CORE_READER.md`, Tier N, theory-space. ### **BODY '
     'BYTE-IDENTICAL, 0 BYTES EDITED**, head block prepended with the class line, the scheme line '
     'and the three-clause currency note. ### Registry row **p2-35**.'),
    ('the Reader’s encoding', 'STANDING',
     'ROUTED, NOT REPAIRED. ### **51 em-dashes carry cp1252 re-encoding damage against 25 '
     'written correctly** — the file is half-corrupted. ### `(R32)` says nothing in the body is '
     'edited and **an encoding repair IS an edit to the body.** ### The author may want a '
     'repaired copy; that is a ruling, not a seat decision.'),
    ('the Reader’s arithmetic desert', 'STANDING',
     'ROUTED. ### Its sentence says the jump primes are separated by **arithmetic deserts where '
     'no sum of powers yields a prime**, and between 41 and 137 the lattice carries **six** — 43, '
     '59, 67, 73, 83, 89. ### **AND THE READER’S OWN PREDICTIONS SECTION NAMES TWO OF THEM AS GAP '
     'ELEMENTS**, so it contradicts itself in its own body. ### Reported here; the body stands.'),
    ('the lattice figure', 'CLOSE',
     'DRAWN at `outputs/prime-core-lattice-b416.svg`, 70 cells, four kinds distinguished, 43 shown '
     'on the lattice and outside P with the Reader’s own sentence beside it. ### **A FIGURE '
     'CARRIES NO GRADE** and is cited nowhere as evidence.'),
    ('§9’s certificate; the `I-7` collision; the ten arcs; the deposited title', 'STANDING',
     'ROUTED, unchanged by this act.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING',
     'WHERE THE DEPOSIT LEFT IT. ### The substrate keystone this act`s neighbours read is '
     'h2-INDEPENDENT by its own header, and nothing here touches h2.'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for k in range(0, min(len(why), 1600), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


REGROW = ('| p2-35 | Prime Core: The Unified Reader Edition | `heritage/PRIME_CORE_READER.md` | '
          'v1.0 | ◎ | **TIER N — theory-space cluster** | ~9,900 | **PLACED b416 (2026-09-11) '
          'under author ruling (R32).** January-2026 synthesis of the constants lane; body '
          'byte-identical to the canonical copy at `D:\\MY-DOwnloads\\PRIME_CORE_READER.md`, '
          '**0 bytes edited**, head block prepended with class line, scheme line and a '
          'three-clause currency note. **Cited for orientation, never as certification.** '
          '**Lineage: the lineage stated on the registry row and nowhere else**; the separate '
          'continuation is outside this repo and nothing from it is written here. **Where its '
          'content already lives in the corpus:** the P-ZONE patent provisional 64/065,864 '
          '(filed 2026-05-14), and the CONSTANCE anchors at @C1@ — with @C2@ and @C3@ '
          'carrying the same set. **Currency:** predates the SIDE method and the '
          'forced-versus-permitted screen; its central empirical claim (every tested coefficient '
          'factors into P) is **not re-tested under the screen**; two ratios of its continuation '
          'screened **PERMITTED** at b415. **Known defects, routed and not repaired:** 51 '
          'em-dashes carry cp1252 re-encoding damage; and its arithmetic-desert sentence is false '
          'between 41 and 137, where the lattice carries six sum-of-powers primes. Figure: '
          '`outputs/prime-core-lattice-b416.svg` (illustration only, carries no grade). |')


def do_registry():
    rec('  ### **THE THREE CARRIERS, MEASURED AND NOT CHOSEN.**')
    rec('  ### Test: a LIVE document naming at least ten of the fifteen members of `P`, including')
    rec('  ### at least three of the four hard ones (23, 53, 137, 337). ### Archive, outputs and')
    rec('  ### the heritage layer are excluded.')
    for big, got, named, rel in SCORED[:8]:
        rec('      %-52s %2d of 15, %d of 4 hard, names the set %d time(s)'
            % (rel[:52], got, big, named))
    rec('  ### ### **DOCUMENTS MEETING THE TEST : %d.**' % len(SCORED))
    tied = len([r for r in SCORED if r[0] == 4 and r[1] == 15])
    rec('  ### ### **AND THE MEASUREMENT TIES: %d OF THEM CARRY ALL FIFTEEN AND ALL FOUR HARD '
        'ONES.**' % tied)
    rec('  ### ### **SO THE COUNT CANNOT PICK THREE**, and an ordering taken from it would be a')
    rec('  ### fact about the directory walk. ### The ferry NAMES `CONSTANCE`; the other two are')
    rec('  ### the carriers that name the set ### **AS A SET** ### most often, ties broken')
    rec('  ### alphabetically. ### **THE RULE IS STATED AND THE TIE IS PRINTED.**')
    rec('  ### the three named on the row : %s' % ', '.join(TOP3))
    if len(TOP3) < 3:
        rec('  ### HARD FAILURE -- fewer than three carriers found; refusing to write the row.')
        return 0
    row = REGROW.replace('@C1@', '`%s`' % TOP3[0]).replace('@C2@', '`%s`' % TOP3[1]) \
                .replace('@C3@', '`%s`' % TOP3[2])
    txt = read(REG)
    if '| p2-35 |' in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        return 1
    anchor = [ln for ln in txt.splitlines() if ln.startswith('| p2-34 |')]
    if not anchor:
        rec('  ### HARD FAILURE -- the p2-34 anchor is absent; refusing to write.')
        return 0
    before = len(txt.splitlines())
    new = txt.replace(anchor[-1], anchor[-1] + NL + row, 1)
    write_bytes(REG, new)
    back = read(REG)
    ok = ('| p2-35 |' in back) and (anchor[-1] in back) and \
         len(back.splitlines()) == before + 1
    rec('  registry row written : p2-35   (table grew %d -> %d lines, +1)'
        % (before, len(back.splitlines())))
    rec('  the p2-34 row still present : %s' % (anchor[-1] in back))
    rec('  lines deleted : 0')
    rec('  ### ### **LINEAGE STATED ON THE ROW : %d TIME(S). ### AND NOWHERE ELSE.**'
        % back.count('the lineage stated on the registry row and nowhere else'))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return 1 if ok else 0


def trail_block():
    return [
        '', MARK, '',
        '### b416 — the two stipulations named, the dated instrument repaired, and the Reader '
        'placed — filed 2026-09-11', '',
        '**`n1` and `n4`, from owners.** `n1` counts *the independent algebraic channels through '
        'which the specification accesses the substrate*; `n4` counts *the mechanism classes '
        'contributed by the bindings between stages*. Both are stated in '
        '`phase2/physics/MATTER_AS_ARITHMETIC.md` §I, and the kernel’s own `Core.lean` field '
        'docstring agrees. **Neither has ever had a derivation route priced** — the search found '
        'no sentence in the live tree pricing one.',
        '',
        '**And (N1) splits.** Its premise is met: `n4 = 0` does count something the model asserts '
        'is empty. **Its conclusion is refuted** — three documents argue it, and the owning '
        'document does not merely assert it but **names Schur’s lemma**. `COMPLEX_ANALYSIS` says '
        'all interfaces between mechanism classes are dark for zero locations; '
        '`BSD_VIA_FORMATION_TRANSFER` carries *product formula spectrally inert* into Λ(E,s). '
        '**The component that is really unargued is `n1`** — and it is unargued because the owner '
        'declares it free: *the fourth component `n1` depends on the base algebra*. Asking why '
        '`classA.n1 = 2` is asking why class A is class A.',
        '',
        '**And here is what neither the ferry nor b415 asked, and it undoes the owner’s own '
        'sentence.** The owner says `n2`, `n3` and `n4` are universal across IDS-amenable systems '
        '— `n2 = 3` by Chevalley–Steinberg, `n3 = 2` by bipartite complex analysis, `n4 = 0` by '
        'Schur’s lemma — leaving `n1` free. **The kernel’s own four tuples have TWO components '
        'varying, not one:** `n1` takes 2 and 3, and **`n2` takes 2 and 3 as well**, because '
        '`classB.n2 = 2` and `classD.n2 = 2`. **A universal reason cannot derive a component in a '
        'class where that component has another value.** So the two existing bridges cannot reach '
        'B and D even in principle, and C gets its `n2` and `n3` only by sharing A’s values '
        'rather than by its own argument. **b415 found 0 derived components in B, C and D and '
        'read it as an absence; it is a contradiction.** The stipulation is not laziness — **the '
        'tuples contradict the universality claim that would have derived them.**',
        '',
        '**Deriving `n1` at class A, priced on the bridges’ own pattern.** Both existing bridges '
        'do the same thing: declare a finite type whose elements *are* the things counted, prove '
        'an exhaustiveness theorem over it, take `Fintype.card`. **The hard part is never the '
        'cardinality — it is the exhaustiveness**, and in both cases it came from a named '
        'classical theorem. The analogous supply for `n1` would be a finite type whose elements '
        'are the algebraic channels into ℤ, and a theorem that there are exactly two. **And there '
        'is an obstruction before the Lean begins.** The corpus has a compiled `2` close at hand '
        '— the substrate is *the minimal complete coprime pair* `{2,3}`, with '
        '`FrobeniusCalibration.g_two_three` axiom-free beneath it. **But that 2 counts primes and '
        '`n1` counts channels**, and (R28) says a result applies to an object only if the object '
        'is of the kind the result quantifies over. **The two twos are not known to be the same '
        'two.** Price: **at least two acts, and the first is not a build** — it is a corpus '
        'statement nobody has made. **And it may be unbuildable rather than unbuilt:** a '
        'derivation of the class label would collapse the four classes into one, and the model '
        'needs four. **PRICED; NOT BUILT.**',
        '',
        '**The dated instrument, repaired — and it took two edits, not one.** '
        '`tools/b371_hookpath.py` still named `tools/git-hooks/pre-push`, a path b386 retired when '
        'it single-sourced the guard at `.githooks/`; it raised `FileNotFoundError` on every run. '
        'Repointing it exposed a second consequence of the same move: in relay the source **is** '
        'the destination, and `shutil.copyfile` raises `SameFileError` rather than doing nothing. '
        '**Repointing the path revealed a defect the path had been hiding** — the tool could not '
        'reach that line while it was still looking for a file that did not exist. Both repaired; '
        'it now runs to completion.',
        '',
        '**And a third thing, which is the one worth keeping.** A repaired instrument does what it '
        'was built to do — and this one was built to write its own run records, which live under '
        '**prior acts’ names**. Running it modified one. It was captured before the run and '
        'restored after: **1 modified, 1 restored, 0 still differing**, confirmed against the '
        'working tree. **While the tool was broken it wrote nothing. Repairing it made that '
        'breach possible for the first time**, and the act met it on the first run. A dated tool '
        'is inert; a repaired one is live, and **a live tool’s writes are the repairing act’s '
        'writes.**',
        '',
        '**The search by description found seven static hits in five files and two real breaks.** '
        '`b369_hygiene.py` breaks on the same path; the three `b386` files run, because they name '
        'the retired path **in order to record retiring it**. **A file that names a retired path '
        'to record retiring it is not a dated tool** — the same shape as b410’s '
        '`G-NOBORROWEDBAR`, which fired on the act’s own comment saying the bar had been removed. '
        '`b369_hygiene.py` is **routed, not repaired**: the ferry orders one tool repaired and the '
        'write list names one.',
        '',
        '**The (T1.4) annotation, drafted and not applied.** One additive line after the existing '
        'caveat, striking nothing — **+4 lines, 0 removed** — recording that the condition named '
        'there is too strong and that the separator is a single prime factor. **The proof that it '
        'was not applied is a digest, not a sentence:** `Core/FiniteSideSeal.lean` carries the '
        'same sha256 before and after this act. **A correction that deletes the sentence it '
        'corrects destroys the evidence that the correction was needed.**',
        '',
        '**Thirteen caveats of that shape across `Core/`, in nine files**, five of them in the '
        'seal itself, under a control that found (T1.4) first in the file that owns it. **Counted, '
        'not graded** — b414 showed a caveat of exactly this shape can be exactly right on its own '
        'evidence and wrong off it, and testing thirteen is not this act’s order.',
        '',
        '**(R32) executed: the Reader is placed.** Located **by digest** at '
        '`D:\\MY-DOwnloads\\PRIME_CORE_READER.md`, copied to `heritage/PRIME_CORE_READER.md` as a '
        'Tier N document of the theory-space cluster, **body byte-identical, 0 bytes edited**, '
        'with a head block carrying the class line, the scheme line and the three-clause currency '
        'note (R32) specifies — and not a fourth. Registry row **p2-35**, naming the P-ZONE '
        'provisional 64/065,864 and the CONSTANCE anchors as where its content already lives, '
        'with the lineage the lineage stated on the registry row and nowhere else stated on the '
        'row and nowhere else. **Nothing from the separate continuation is written into any '
        'corpus document, and the continuation is named as outside the repo.**',
        '',
        '**Two defects found in it, both reported here and neither repaired.** First, **the file '
        'is half-corrupted**: 51 em-dashes carry cp1252 re-encoding damage against 25 written '
        'correctly. **An encoding repair is an edit to the body, which (R32) forbids**, so the '
        'damage travels with the copy. Second, **its arithmetic-desert sentence is false.** It '
        'says the jump primes are separated from the consecutive sequence *by arithmetic deserts '
        'where no sum of powers yields a prime*; between 41 and 137 the lattice carries **six** — '
        '43, 59, 67, 73, 83, 89. **And the Reader’s own predictions section names two of them '
        '(43 and 67) as gap elements**, so the document contradicts itself in its own body. **A '
        'Tier N document is placed as it stands**; whether the head note grows a fourth clause is '
        'the author’s ruling and not this seat’s.',
        '',
        '**The lattice drawn, as a figure and not a claim.** '
        '`outputs/prime-core-lattice-b416.svg`: powers of two against powers of three, 70 cells, '
        'every sum marked, the primes among them lit, the fifteen of P distinguished by kind — '
        'generator, consecutive, jump, inclusion — and **43 shown on the lattice and outside P**, '
        'with the Reader’s own sentence beside it and the six-strong count that contradicts it '
        'beneath. **A figure carries no grade.** It is filed as illustration of a Tier N document '
        'and cited nowhere as evidence.',
        '',
        '**And (N5) is refuted by arithmetic.** Forty-three is not the only sum-of-powers prime '
        'below one hundred that P excludes — **there are seven**: 43, 59, 67, 73, 83, 89 and 97. '
        'Each is prime, each is a sum of a power of two and a power of three, and none is in P.',
        '',
        '**What this act did not do.** 0 `.lean` files touched, 0 builds run, 0 terminals added. '
        '0 grades moved. 0 premises discharged. 0 doors restated. 0 routes proposed. 0 kappa '
        'measured. 0 rows of `FACES_LEDGER.md` written. 0 folds run. 0 rules struck or amended — '
        '(R32) is executed, not extended. 0 orientation-layer lines edited. 0 locked faces edited. '
        '**0 bytes of the Reader’s body edited. 0 annotations applied to the sealed file. 0 files '
        'of the separate continuation written or read for adoption. 0 other files under '
        '`outputs/` touched. 0 tools repaired that the write list does not name.** 0 deposit '
        'actions, 0 platform calls. **And h2 where the deposit left it.**',
        '',
    ]


SCOPE = ("### THIS ROW RECORDS TWO COMPONENTS NAMED FROM THEIR OWNER, A CONTRADICTION FOUND "
         "BETWEEN THAT OWNER AND THE KERNEL, A PRICE, AN INSTRUMENT REPAIRED TWICE OVER, AN "
         "ANNOTATION DRAFTED AND WITHHELD, A COUNT OF CAVEATS, A TIER N DOCUMENT PLACED AND A "
         "FIGURE DRAWN. ### IT MOVES NO GRADE, DISCHARGES NO PREMISE, PROVES NOTHING, EDITS NO "
         "BYTE OF THE PLACED BODY AND APPLIES NO ANNOTATION -- AND ITS CENTRAL FINDING IS THAT "
         "THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM")


def corr_rows():
    m = ("**THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM** "
         "(b416, the two stipulations named)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run "
            "as b416 -- @GR@ gates read, @GDG@ checked by digest; the survey left 0 anchor "
            "misses. **A READ ACT IN THE KERNEL: 0 .lean files touched, 0 builds run.** "
            "**COMPONENT 1: n1 COUNTS THE INDEPENDENT ALGEBRAIC CHANNELS THROUGH WHICH THE "
            "SPECIFICATION ACCESSES THE SUBSTRATE; n4 COUNTS THE MECHANISM CLASSES CONTRIBUTED "
            "BY THE BINDINGS BETWEEN STAGES**, both from MATTER_AS_ARITHMETIC section I, and "
            "**NEITHER HAS EVER HAD A DERIVATION ROUTE PRICED**. **(N1) SPLITS UNDER (R27)**: n4 "
            "does count something the model asserts empty, but **THREE DOCUMENTS ARGUE IT AND THE "
            "OWNER NAMES SCHUR'S LEMMA** -- the unargued component is n1, and it is unargued "
            "because the owner declares it FREE. **AND THE OWNER'S UNIVERSALITY SENTENCE AND THE "
            "KERNEL'S DECLARATIONS DISAGREE: the owner calls n2 universal at 3, and classB.n2 = "
            "classD.n2 = 2.** **A UNIVERSAL REASON CANNOT DERIVE A COMPONENT IN A CLASS WHERE "
            "THAT COMPONENT HAS ANOTHER VALUE** -- so b415's 0 derived components in B, C and D "
            "is not an absence but a CONTRADICTION. **COMPONENT 2: DERIVING n1 AT CLASS A PRICES "
            "AT AT LEAST TWO ACTS AND THE FIRST IS NOT A BUILD** -- the compiled 2 counts PRIMES "
            "and n1 counts CHANNELS, and (R28) forbids wiring them; it may be unbuildable, since "
            "a derivation of the class label would collapse the four classes into one. **COMPONENT "
            "3: b371_hookpath.py REPAIRED TWICE OVER** -- the retired path, and then the "
            "SameFileError the path change exposed; **REPOINTING IT REVEALED A DEFECT IT HAD BEEN "
            "HIDING**. Running it modified 1 prior-act record, **CAPTURED BEFORE AND RESTORED "
            "AFTER, 0 STILL DIFFERING** -- **A LIVE TOOL'S WRITES ARE THE REPAIRING ACT'S "
            "WRITES**. 7 static hits in 5 files, **2 REAL BREAKS**; b369_hygiene.py ROUTED. "
            "**COMPONENT 4: THE (T1.4) ANNOTATION DRAFTED AND NOT APPLIED**, +4 lines and 0 "
            "removed, the seal's sha256 identical before and after. **COMPONENT 5: 13 CAVEATS OF "
            "THAT SHAPE ACROSS Core/ IN 9 FILES, 8 OUTSIDE THE SEAL, COUNTED AND NOT GRADED.** "
            "**ADDITION ONE: THE READER PLACED UNDER (R32)** at heritage/PRIME_CORE_READER.md, "
            "Tier N, theory-space, located BY DIGEST, **BODY BYTE-IDENTICAL, 0 BYTES EDITED**, "
            "registry row p2-35. **TWO DEFECTS FOUND AND NEITHER REPAIRED: 51 em-dashes carry "
            "cp1252 damage against 25 clean, and its arithmetic-desert sentence is FALSE** -- the "
            "lattice carries six sum-of-powers primes between 41 and 137, two of which the "
            "Reader's own predictions section names. **ADDITION TWO: THE LATTICE DRAWN**, 70 "
            "cells, four kinds, 43 shown outside P. **A FIGURE CARRIES NO GRADE.** 0 GRADES "
            "MOVED, 0 PREMISES DISCHARGED, 0 BYTES OF THE BODY EDITED, 0 CONTENT LOST")
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AND NONE IS OPENED, ADDED, RENAMED OR "
            "RESTATED. ### THE KERNEL WAS READ AND NOT BUILT. ### THE TERMINALS CITED -- "
            "OstrowskiBridge.formation_n2, CartanBBridge.formation_n_3_eq_two, "
            "FrobeniusCalibration.g_two_three -- ARE CITED AS THEIR OWN MODULES DECLARE THEM, AND "
            "THE ACT REPORTS WHICH COMPONENTS CARRY A BRIDGE AND WHICH DO NOT. ### PRICING A "
            "BRIDGE IS NOT BUILDING ONE")
    prof = ("### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED, NO GRADE MOVED "
            "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
            "CHANNEL OPENED, NO ROUTE PROPOSED, NO ROW OF FACES_LEDGER WRITTEN, NO FOLD RUN, NO "
            "RULE STRUCK OR AMENDED, NO ORIENTATION-LAYER LINE EDITED, NO LOCKED FACE EDITED, NO "
            "PRIOR ACT'S BANK EDITED. ### NO BYTE OF THE PLACED DOCUMENT'S BODY EDITED, NO "
            "ANNOTATION APPLIED TO THE SEALED FILE, NO FILE OF THE SEPARATE CONTINUATION WRITTEN "
            "OR READ FOR ADOPTION, NO OTHER FILE UNDER outputs/ TOUCHED, NO TOOL REPAIRED THAT "
            "THE WRITE LIST DOES NOT NAME. ### THE INSTRUMENT AND INSTRUMENT-AUDIT LANES STAY "
            "PARKED. ### THE CORPUS WRITES ARE ONE PLACED DOCUMENT, ONE REGISTRY ROW, ONE FIGURE, "
            "ONE APPEND-ONLY TRAIL BLOCK AND ONE APPENDED CORRESPONDENCE ROW -- 0 CONTENT LOST")
    grade = ("### AN OWNER'S OWN SENTENCE WAS TESTED AGAINST THE KERNEL'S DECLARATIONS RATHER "
             "THAN QUOTED AND LEFT, AND THE TWO WERE FOUND TO DISAGREE. ### A PREDECESSOR'S "
             "FINDING WAS RE-READ AND ITS KIND CORRECTED: WHAT b415 RECORDED AS AN ABSENCE IS A "
             "CONTRADICTION. ### A PRICE WAS REFUSED A SHORTCUT BECAUSE THE TWO NUMBERS IT WOULD "
             "HAVE JOINED COUNT DIFFERENT KINDS, UNDER (R28). ### AN INSTRUMENT REPAIR REVEALED A "
             "SECOND DEFECT THE FIRST HAD BEEN HIDING, AND A THIRD THAT ONLY A WORKING TOOL COULD "
             "COMMIT. ### A TOOL FOUND BY THE SAME SEARCH WAS ROUTED RATHER THAN REPAIRED, "
             "BECAUSE THE ORDER NAMED ONE. ### AN ANNOTATION WAS DRAFTED AND WITHHELD, WITH A "
             "DIGEST AS THE PROOF INSTEAD OF A SENTENCE. ### A DOCUMENT WAS PLACED WITH ITS "
             "DAMAGE INTACT BECAUSE THE RULING FORBADE EDITING ITS BODY, AND THE DAMAGE WAS "
             "MEASURED RATHER THAN MENTIONED. ### AND A FIGURE WAS DRAWN FROM ARITHMETIC THAT "
             "CONTRADICTS THE SENTENCE PRINTED BESIDE IT, WITH BOTH SHOWN")
    status = ("data/b416_the_reader_placed.txt; data/b416_components.txt; data/b416_extract.txt; "
              "data/b416_place.txt; data/b416_figure.txt; data/b416_lattice.txt; "
              "data/b416_registration_2026-09-11.txt (LOCKED before any write at sha256 %s, "
              "chained on tools/b378_lockgate.py run as b416); tools/b416_extract.py; "
              "tools/b416_regspec.py; tools/b416_reg_gate.py; tools/b416_components.py; "
              "tools/b416_desk_bank.py; tools/b416_checks.py; tools/b371_hookpath.py (REPAIRED); "
              "PLACE-papers heritage/PRIME_CORE_READER.md (PLACED), REGISTRY.md row p2-35, "
              "outputs/prime-core-lattice-b416.svg, OPEN_TRAILS.md; CORRESPONDENCE.md row %%d"
              % SEALHASH[:16])

    def sub(x):
        return x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
    return [(sub(m), sub(stmt), sub(term), sub(prof), sub(grade), SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('what do n1 and n4 count in the formation tuple',
           'why are the formation tuple components stipulated',
           'what would it cost to derive n1',
           'where is the prime core reader placed',
           'is the reader arithmetic desert sentence true',
           'which relay tools point at a retired path')
MUST_NOT_HIT = ('the tuples are derived', 'the annotation was applied',
                'the reader body was edited', 'a grade was moved', 'h2 has moved')
KEY = 'the-reader-placed'


def do_key(rownum):
    statement = (
        "b416 NAMED THE TWO STIPULATIONS, REPAIRED THE DATED INSTRUMENT AND PLACED THE READER. "
        "**n1 COUNTS THE INDEPENDENT ALGEBRAIC CHANNELS THROUGH WHICH THE SPECIFICATION ACCESSES "
        "THE SUBSTRATE; n4 COUNTS THE MECHANISM CLASSES CONTRIBUTED BY THE BINDINGS BETWEEN "
        "STAGES**, both from MATTER_AS_ARITHMETIC section I; **NEITHER HAS EVER HAD A DERIVATION "
        "ROUTE PRICED**. **(N1) SPLITS**: n4 does count something the model asserts empty, but "
        "three documents argue it and **THE OWNER NAMES SCHUR'S LEMMA** -- **THE UNARGUED "
        "COMPONENT IS n1, AND IT IS UNARGUED BECAUSE THE OWNER DECLARES IT FREE**. **AND THE "
        "OWNER'S UNIVERSALITY SENTENCE AND THE KERNEL'S DECLARATIONS DISAGREE**: the owner calls "
        "n2 universal at 3 and the kernel declares classB.n2 = classD.n2 = 2. **A UNIVERSAL "
        "REASON CANNOT DERIVE A COMPONENT IN A CLASS WHERE THAT COMPONENT HAS ANOTHER VALUE**, so "
        "**WHAT b415 RECORDED AS AN ABSENCE IS A CONTRADICTION** -- the stipulation is not "
        "laziness, **THE TUPLES CONTRADICT THE UNIVERSALITY CLAIM THAT WOULD HAVE DERIVED THEM**. "
        "**DERIVING n1 AT CLASS A PRICES AT AT LEAST TWO ACTS AND THE FIRST IS NOT A BUILD**: the "
        "corpus must first say what an algebraic channel IS, because **THE COMPILED 2 COUNTS "
        "PRIMES AND n1 COUNTS CHANNELS** and (R28) forbids wiring them; and it may be unbuildable, "
        "since **A DERIVATION OF THE CLASS LABEL WOULD COLLAPSE THE FOUR CLASSES INTO ONE**. "
        "**b371_hookpath.py WAS REPAIRED TWICE OVER** -- the retired path, then the SameFileError "
        "the path change exposed: **REPOINTING IT REVEALED A DEFECT IT HAD BEEN HIDING**. And "
        "running it modified a prior act's record, captured and restored, **0 STILL DIFFERING** -- "
        "**A LIVE TOOL'S WRITES ARE THE REPAIRING ACT'S WRITES**. The search found 7 static hits "
        "in 5 files and **2 REAL BREAKS**, because **A FILE THAT NAMES A RETIRED PATH IN ORDER TO "
        "RECORD RETIRING IT IS NOT A DATED TOOL**; b369_hygiene.py is ROUTED. **THE (T1.4) "
        "ANNOTATION IS DRAFTED AND NOT APPLIED**, +4 lines and 0 removed, proved by the seal's "
        "sha256 being identical before and after. **13 CAVEATS OF THAT SHAPE ACROSS Core/ IN 9 "
        "FILES, 8 OUTSIDE THE SEAL, COUNTED AND NOT GRADED.** **THE READER IS PLACED UNDER (R32)** "
        "at heritage/PRIME_CORE_READER.md as Tier N of the theory-space cluster, located BY "
        "DIGEST, **BODY BYTE-IDENTICAL AND 0 BYTES EDITED**, registry row p2-35. **TWO DEFECTS "
        "FOUND IN IT AND NEITHER REPAIRED: 51 EM-DASHES CARRY cp1252 DAMAGE AGAINST 25 CLEAN, AND "
        "ITS ARITHMETIC-DESERT SENTENCE IS FALSE** -- six sum-of-powers primes lie between 41 and "
        "137, and **THE READER'S OWN PREDICTIONS SECTION NAMES TWO OF THEM**. **THE LATTICE IS "
        "DRAWN AS A FIGURE AND CARRIES NO GRADE.** And **FORTY-THREE IS NOT THE ONLY ONE P "
        "EXCLUDES BELOW 100: THERE ARE SEVEN** -- 43, 59, 67, 73, 83, 89, 97.")
    grade = (
        "### NO `.lean` FILE TOUCHED, NO BUILD RUN, NO TERMINAL ADDED. ### NO GRADE MOVED "
        "CONFERRED OR MINTED, NO PREMISE DISCHARGED, NO DOOR RESTATED, NO KAPPA MEASURED, NO "
        "ROUTE PROPOSED, NO LEDGER ROW WRITTEN, NO FOLD RUN, NO RULE STRUCK OR AMENDED, NO "
        "ORIENTATION-LAYER LINE EDITED, NO LOCKED FACE OR PRIOR BANK EDITED. ### NO BYTE OF THE "
        "PLACED BODY EDITED, NO ANNOTATION APPLIED TO THE SEALED FILE, NO CONTINUATION FILE "
        "WRITTEN OR ADOPTED, NO TOOL REPAIRED THAT THE WRITE LIST DOES NOT NAME. ### NOTHING "
        "DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### NOTHING WAS PROVED AND NOTHING WAS "
        "COMPILED")
    where = (
        "data/b416_the_reader_placed.txt; data/b416_components.txt; data/b416_extract.txt; "
        "data/b416_place.txt; data/b416_figure.txt; "
        "data/b416_registration_2026-09-11.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b416 -- %d gates read, %d checked by digest); "
        "tools/b416_extract.py; tools/b416_components.py; tools/b416_desk_bank.py; "
        "tools/b416_checks.py; PLACE-papers heritage/PRIME_CORE_READER.md, REGISTRY.md p2-35, "
        "outputs/prime-core-lattice-b416.svg, OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (GR, GDG, rownum))
    act = ("b416 (n1 and n4 named from their owner, the universality sentence found to contradict "
           "the kernel's own tuples, deriving n1 priced, the dated hook instrument repaired twice "
           "over, the (T1.4) annotation drafted and withheld, and the Prime Core Reader placed "
           "under (R32) with its two defects reported and neither repaired)")
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE READER PLACED (b416).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b416 key : %s' % (qq[:58], g2))
    for lbl, cond in (
            ('n1 counts channels', 'INDEPENDENT ALGEBRAIC CHANNELS' in out),
            ('n4 counts mechanism classes', 'MECHANISM CLASSES CONTRIBUTED' in out),
            ('neither priced', 'HAS EVER HAD A DERIVATION ROUTE PRICED' in out),
            ('(N1) splits', '(N1) SPLITS' in out),
            ('Schur named', "OWNER NAMES SCHUR'S LEMMA" in out),
            ('n1 is free', 'OWNER DECLARES IT FREE' in out),
            ('the disagreement', 'DECLARATIONS DISAGREE' in out),
            ('a universal reason cannot', 'UNIVERSAL REASON CANNOT DERIVE' in out),
            ('absence is contradiction', 'RECORDED AS AN ABSENCE IS A CONTRADICTION' in out),
            ('the central finding', 'CONTRADICT THE UNIVERSALITY CLAIM' in out),
            ('the price', 'AT LEAST TWO ACTS AND THE FIRST IS NOT A BUILD' in out),
            ('primes against channels', 'COUNTS PRIMES AND n1 COUNTS CHANNELS' in out),
            ('it may be unbuildable', 'COLLAPSE THE FOUR CLASSES INTO ONE' in out),
            ('repaired twice over', 'REPAIRED TWICE OVER' in out),
            ('the hidden defect', 'REVEALED A DEFECT IT HAD BEEN HIDING' in out),
            ('a live tool writes', "LIVE TOOL'S WRITES ARE THE REPAIRING" in out),
            ('mention is not a break', 'IS NOT A DATED TOOL' in out),
            ('annotation withheld', 'DRAFTED AND NOT APPLIED' in out),
            ('caveats counted', 'COUNTED AND NOT GRADED' in out),
            ('the reader placed', 'PLACED UNDER (R32)' in out),
            ('body untouched', 'BODY BYTE-IDENTICAL AND 0 BYTES EDITED' in out),
            ('the two defects', 'NEITHER REPAIRED' in out),
            ('the desert is false', 'ARITHMETIC-DESERT SENTENCE IS FALSE' in out),
            ('the figure', 'CARRIES NO GRADE' in out),
            ('seven not one', 'THERE ARE SEVEN' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok, regok):
    B = ['=' * 100,
         'b416 -- THE TWO STIPULATIONS NAMED, THE DATED INSTRUMENT REPAIRED, AND THE READER '
         'PLACED.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            B.append(blk)
    B += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, why in DESK:
        B.append('  %-70s %s' % (item[:70], want))
    B += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
          % (Q['items'], Q['closed'], Q['standing']),
          '', '  REGISTRY ROW p2-35 : %s. ### CORRESPONDENCE ROW : %d. ### KEY : %s.'
          % ('WRITTEN' if regok else 'FAIL', rownum, 'PASS' if kok else 'FAIL'),
          '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(B) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(B)))
    return len(B)


def main():
    bar('=')
    rec('b416_desk_bank.py -- THE DESK, THE REGISTRY ROW, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    rec('')
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    rec('')
    bar()
    rec('### THE REGISTRY ROW.')
    bar()
    regok = do_registry()
    rec('')
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2))
    rec('  lines deleted : 0')
    rec('')
    bar()
    rec('### THE CORRESPONDENCE ROW.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    slip = [mm for mm, s2, _t, _p, _g, _sc, _st in ROWS2 if not s2.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS2 if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS2)]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    rec('  prior row 264 still present : %s' % ('| 264 |' in read(TABLE)))
    rec('')
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    rec('')
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok, regok)
    rec('')
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### `.lean` FILES TOUCHED : 0. ### BYTES OF THE '
        'PLACED BODY EDITED : 0. ### ANNOTATIONS APPLIED : 0. ### REGISTRY p2-35 %s. ### CORR ROW '
        '%d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], 'WRITTEN' if regok else 'FAIL', rownum,
           'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b416_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(LINES) + NL)
    return 0 if (kok and regok) else 1


if __name__ == '__main__':
    sys.exit(main())
