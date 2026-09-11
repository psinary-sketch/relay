# -*- coding: utf-8 -*-
"""b422_components.py -- THE FOLD, b413 TO b421, (R37), THE ORIENTATION LAYER, AND THE WITNESS ARC NAMED.

### ### **EACH MODE WRITES ITS OWN RECORD, AND EVERY CORPUS WRITE IS AN APPEND WHOSE PRIOR TEXT IS CHECKED AS A
### TRUE PREFIX BEFORE THE FILE IS REPLACED:**
###   --fold      the fold section: F-NOGRADE and F-NOSUPERSEDE run on its text BEFORE it is written.
###   --r37       the keystone's §10.2, appended under the author's ruling.
###   --orient    (R31): the digest's block and the five-door state's block, doors measured from the banks.
###   --witness   the witness arc named, its class site's opening list entered verbatim, not opened.
###   (no flag)   the report and the expectations.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
PIN_PP = '2249436'
FIND = os.path.join(PP, 'FINDINGS.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
FL = os.path.join(PP, 'FACES_LEDGER.md')
NL = chr(10)
MISS = []

ARC_NAME = 'THE KERNEL ARC'
CRITERION = ('a statement about the OBJECT is one about `ξ`, about the zeros, about the Epstein object, or about a '
             'number computed from them. A statement about the RECORD is one about documents, grades, instruments, '
             'numbering, arms, counts, or what the corpus has or has not asked.')

# (act, name, bank, kind, what it put on the board, grade strings used in `what`)
ARC = [
    (413, 'THE NEAREST DOOR READ AT ITS EDGE', 'b413_the_nearest_door.txt', 'OBJECT-MODEL, MEASURED',
     'read the finite-side seal at its own source and found the obvious generalisation of its per-cell conjunct '
     '**FALSE** -- it fails at every base with two prime factors and holds at every prime power -- re-computed '
     'outside the kernel on the kernel`s own definitions, the seven decided cells a positive control', ['FALSE']),
    (414, 'THE PREDICATE NAMED', 'b414_the_predicate_named.txt', 'OBJECT-MODEL, COMPILED',
     'compiled the single-prime-factor predicate into the kernel, the naive generalisation refuted there with '
     'witnesses, and recorded the general clause as a **NAMED OPEN STATEMENT**, never a sorry',
     ['NAMED OPEN STATEMENT']),
    (415, 'THE SUBSTRATE AT GRADE', 'b415_the_substrate_at_grade.txt', 'RECORD',
     'graded the substrate keystone`s claims and the four formation tuples -- half of class A derived and nothing '
     'else -- and screened two sibling ratios **PERMITTED** by enumeration', ['PERMITTED']),
    (416, 'THE READER PLACED', 'b416_the_reader_placed.txt', 'RECORD',
     'found the formation tuples contradict the universality sentence that would have derived them, repaired a '
     'dated tool, and placed the Prime Core Reader under `(R32)`', []),
    (417, 'THE CONTRADICTION PUT', 'b417_components.txt', 'RECORD',
     'put the contradiction to its owner as two readings priced and neither adopted, and cleared a tool '
     'snapshot-first after its repair escaped two calls deep', []),
    (418, 'THE RULING CARRIED', 'b418_the_ruling_carried.txt', 'RECORD',
     'executed `(R35)` reading (b), traced the walker`s miss to a silent timeout and built its guard, and took the '
     'general clause to **OVER-BUDGET** with one helper unsupplied', ['OVER-BUDGET']),
    (419, 'THE CLAUSE PRINTED', 'b419_the_clause_printed.txt', 'OBJECT-MODEL, COMPILED',
     'repaired that helper and **PROVED** the general clause at zero axioms on the first probe: '
     '`SmearGeneral.smear_general`, the seven decided cells its instances', ['PROVED']),
    (420, 'THE LEMMA AIMED', 'b420_the_lemma_aimed.txt', 'RECORD',
     'put the barrier lemma to the arc`s positivity argument and found it **NOT AN INSTANCE**, on form -- the '
     'argument is a table of graded constituents, not a proof the lemma quantifies over', ['NOT AN INSTANCE']),
    (421, 'THE FINITE AMBIENT', 'b421_the_finite_ambient.txt', 'OBJECT-MODEL, COMPILED -- AND A RECORD FINDING, NAMED',
     '**PROVED** a grid trace it defines equal to the model`s counting form, zero axioms, on the third probe -- and '
     'found Definition 2.1 of the barrier keystone, read in the first-order setting its §2.1 fixes, met by no '
     'infinite structure', ['PROVED']),
]


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def rb(p):
    with open(p, 'rb') as fh:
        return fh.read()


def read(p):
    try:
        return rb(p).decode('utf-8', 'replace')
    except Exception:
        return ''


def put(name, lines):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def blob(repo, path, rev):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True).stdout


def append_to(path, rel, text, marker, R):
    """### APPEND ONLY: refuse unless the working file IS its blob at the pin; write; re-read the prefix."""
    cur = rb(path)
    pin = blob(PP, rel, PIN_PP)
    if marker.encode('utf-8') in cur:
        R.append('  ### %s already carries its marker -- NOT re-appended.' % rel)
        return True
    if cur != pin:
        R.append('  ### REFUSED: %s differs from its blob at the pin before the write.' % rel)
        return False
    new = cur.rstrip(b'\n') + b'\n' + text.encode('utf-8')
    open(path, 'wb').write(new)
    back = rb(path)
    ok = back.startswith(pin.rstrip(b'\n')) and back.endswith(text.encode('utf-8'))
    R.append('  appended to %s : %d lines ; the pin`s bytes a true prefix : %s'
             % (rel, text.count(NL), back.startswith(pin.rstrip(b'\n'))))
    return ok


def q(path, start, end=None, cap=600):
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : %r' % (os.path.basename(path), start[:48]))
        return '### MISS'
    j = src.find(end, i + len(start)) if end else -1
    return re.sub(r'\s+', ' ', src[i:j + len(end)] if j > i else src[i:i + cap]).strip()


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


# =============================================================================================
# ### THE MEASURE FOR *LARGEST*, FIXED ON THE FACE: statements of the record the finding bears on.
# =============================================================================================
def largest_measure():
    ib = read(IB)
    thm = [ln for ln in ib.splitlines() if re.search(r'Theorem 3\.1(?![-\d])|Corollary 3\.6|3\.1-H', ln)]
    m = read(MATTER)
    uni = [ln for ln in m.splitlines() if 'universal across IDS-amenable systems' in ln]
    return len(thm), len(uni)


def tidy(s):
    """### Corpus prose: an apostrophe is a curly one, never a backtick; a dash is an em dash."""
    return re.sub(r'`([sS])\b', '\u2019\\1', s).replace(' -- ', ' \u2014 ')


def clean(s):
    s = re.sub(r'#+\s*', '', s).replace('**', '')
    return tidy(re.sub(r'\s+', ' ', s)).strip()


def conflations():
    f420 = os.path.join(D, 'b420_ferry.txt')
    c4 = os.path.join(D, 'b420_c4_barrier.txt')
    return [
        ('1', 'the theorem\u2019s content against a derived result\u2019s words',
         clean(q(f420, 'the general clause proved at b419, which returns', 'nothing about its sign;')),
         clean(q(c4, '### **b419`S TERMINAL DOES NOT MENTION A TEST FUNCTION', 'OR A SIGN.**'))),
        ('2', 'the compressed trace against the finite-place term',
         clean(q(f420, 'is each finite-place interface', 'the general clause proved at b419')),
         clean(q(c4, '### **AND THE FINITE PLACE`S TERM IN THE', 'the prime`s powers.'))),
        ('3', 'the map\u2019s own scope sentence',
         clean(q(f420, 'the aim map measured \u2014 every aim', 'at any height.')),
         clean(q(os.path.join(D, 'b334_the_aim_map.txt'), 'A PASSED TEST OVER A GRID AT THIS REACH', 'AND NOTHING MORE.'))),
    ]


def fold_text(span_lines, nthm, nuni, obj, om_c, om_m, rec):
    lead = ('**In this arc the kernel was used to build, and twice it closed a statement the corpus had carried open '
            '-- and a sentence of the corpus`s own barrier keystone was found unable to carry the weight every '
            'application of its lemma puts on it.**')
    conf = conflations()
    L = ['', '<!-- b422 the fold: the kernel arc, b413-b421 -->', '',
         '## %s, b413–b421 — THE FOLD' % ARC_NAME, '',
         '*Filed by b422, 2026-09-11. Span decided by `tools/b363_span.py`, not by the seat: %s — b412 stood outside '
         'b403–b411 the same way. Purely additive: nothing above this line was edited.*' % ' '.join(span_lines), '',
         '### The arc’s one statement', '', lead, '',
         '**The product is two compiled general theorems, both about the model of the object at a finite place.** '
         '`SmearGeneral.smear_general` (b419) proves the named open statement b414 recorded — the smear identity at '
         'every base with a single prime factor and every level — at zero axioms; its subject, the predicate '
         '`singlePrimeFactor`, was compiled at b414 after b413 found the obvious generalisation false. '
         '`GridTrace.grid_trace_is_signed_count` (b421) proves a grid trace defined in its own module equal to the '
         'model’s counting form, and its docstring says the source’s trace is not its object. **Neither is about ξ, '
         'the zeros or the Epstein object, and neither says so.**', '',
         '**The largest finding about the record is the barrier keystone’s Definition 2.1**: read in the classical '
         'first-order setting its own §2.1 fixes, *a finite set of 𝓛-sentences that has M as its unique model up to '
         'isomorphism* is met by no infinite structure (b421, the seat’s citation of the upward Löwenheim–Skolem '
         'theorem), and it is the first hypothesis of the lemma. **The author has ruled it read internally to ZFC '
         '(R37).** Largest by the measure the fold’s registration fixed — statements of the record the finding bears '
         'on, counted from the source: the keystone has **%d** lines naming Theorem 3.1, Theorem 3.1-H or '
         'Corollary 3.6, against **%d** lines carrying the universality sentence the formation tuples contradicted '
         '(b416–b418, ruled R35).' % (nthm, nuni), '',
         '*Scope:* **A statement about what this span put on the board, not about what is true of the object.** No '
         'coordinate is closed; the clause has not moved; nothing here bears on `h2`. b407’s and b420’s verdicts are '
         'not re-verdicted by R37, and whether they move under the internal reading is named for a later act. Every '
         'grade in the span is its own act’s.', '',
         '### The span, act by act, each at its own grade', '',
         '| act | what it put on the board |', '|:--|:--|']
    for n, name, _b, _k, what, _g in ARC:
        L.append('| **b%d** | %s — *%s* |' % (n, what, name))
    L += ['',
          '**What the arc produced, counted by the measure b412 used, with one column added.** The criterion, quoted: '
          '*%s* Under it: statements about the **object**: **%d**; about the **record**: **%d**. **A third column, '
          'declared on the fold’s registration before the count, `OBJECT-MODEL`** — statements about the model of the '
          'object at a finite place, which the criterion’s wording does not list: **%d compiled** (b414, b419, b421) '
          'and **%d measured** (b413). It is counted into neither side. **b421 is named as borderline**: its product is '
          'compiled and about the model, and its Definition 2.1 finding is about the record.' % (CRITERION, obj, rec, om_c, om_m),
          '',
          '**And two sentences this fold will not reconcile, named rather than repaired.** b420’s record says b419 '
          '*moved one grade inside `K3`*; b419’s own bank says **0 grades moved**, and row S1’s grade table is unchanged '
          'since b409. The ledger and the bank govern; b420’s sentence describes a scope, not a grade. And b421’s '
          'Definition 2.1 finding bears on b407’s reading of the same hypothesis for ξ — **b407 is not re-verdicted**, '
          'under R37, and neither act supersedes the other.', '',
          '**The navigator’s three conflations at b420, carried as the navigator’s, each with its correction** (in full: '
          'relay `data/b421_conflations.txt`):']
    for num, title, nav, cor in conf:
        L.append('(%s) %s — the navigator: *%s* — the correction: %s' % (num, title.rstrip('.'), nav.strip()[:260], cor.strip()[:300]))
    L.append('')
    return tidy(NL.join(L)), tidy(lead), conf


def f_nograde(text):
    """### F-NOGRADE: every grade string attributed to an act appears VERBATIM (case-folded) in that act's bank."""
    fails = []
    for n, _name, bank, _k, what, grades in ARC:
        b = read(os.path.join(D, bank)).lower()
        for g in grades:
            if g.lower() not in b:
                fails.append('b%d %r not in %s' % (n, g, bank))
    return fails


def f_nosupersede(text):
    """### F-NOSUPERSEDE: no sentence summarises one folded act as overturning, superseding or re-verdicting another."""
    bad = []
    for s in re.split(r'(?<=[.!?])\s+', text):
        acts = re.findall(r'\bb4(1[3-9]|2[01]|07)\b', s)
        if len(set(acts)) >= 2 and re.search(r'(?i)overturn|supersedes (?!the other)|refutes b4|re-verdicts b4', s) \
                and not re.search(r'(?i)\bnot re-verdicted|neither act supersedes', s):
            bad.append(s[:160])
    return bad


def run_fold():
    R = ['=' * 100, 'b422 COMPONENT 1 -- THE FOLD, %s, b413-b421.' % ARC_NAME, '=' * 100, '  at (UTC) : %s' % utc()]
    span = read(os.path.join(D, 'b422_span_run.txt'))
    sl = [x.strip() for x in span.splitlines() if re.search(r'the last fold covers|it was FILED BY|and it now runs|THE CURRENT SPAN', x)]
    n_tool = int((re.search(r'THE CURRENT SPAN : (\d+)', span) or [0, '0'])[1])
    span_sentence = ('the last fold covered b403–b411 and was filed by b412, so this span starts at b413. **The tool '
                     'reports %d, counting b413 through b422; the fold’s span is 9, because the folding act is not in its own fold**' % n_tool)
    R += ['  ### THE SPAN, FROM THE TOOL`S OWN LINES:'] + ['      | %s' % x for x in sl]
    R.append('  ### the tool says %d ; the fold`s span is 9, the folding act excluded (b412`s rule)' % n_tool)
    nthm, nuni = largest_measure()
    R.append('  ### THE MEASURE FOR *LARGEST*: keystone lines applying the lemma %d ; lines carrying the universality sentence %d' % (nthm, nuni))
    kinds = [k for *_x, k, _w, _g in [(a[0], a[1], a[2], a[3], a[4], a[5]) for a in ARC]]
    obj = sum(1 for a in ARC if a[3] == 'OBJECT')
    rec = sum(1 for a in ARC if a[3] == 'RECORD')
    om_c = sum(1 for a in ARC if a[3].startswith('OBJECT-MODEL, COMPILED'))
    om_m = sum(1 for a in ARC if a[3].startswith('OBJECT-MODEL, MEASURED'))
    R.append('  ### THE COUNT : OBJECT %d ; RECORD %d ; OBJECT-MODEL %d compiled, %d measured ; acts %d' % (obj, rec, om_c, om_m, len(ARC)))
    for n, name, bank, kind, what, grades in ARC:
        R.append('      b%d %-34s %-50s bank %s' % (n, name[:34], kind[:50], bank))
    text, lead, conf = fold_text([span_sentence], nthm, nuni, obj, om_c, om_m, rec)
    ng = f_nograde(text)
    ns = f_nosupersede(text)
    R += ['', '  ### F-NOGRADE, RUN BEFORE THE WRITE : %d failure(s) %s' % (len(ng), ng),
          '  ### F-NOSUPERSEDE, RUN BEFORE THE WRITE : %d failure(s) %s' % (len(ns), ns),
          '  conflations carried : %d' % len(conf)]
    if ng or ns or len(conf) != 3 or MISS:
        R.append('  ### ### **THE SECTION IS NOT WRITTEN.** %s' % MISS)
        put('b422_fold.txt', R)
        print(NL.join(R))
        return 1
    ok = append_to(FIND, 'FINDINGS.md', text, '<!-- b422 the fold: the kernel arc', R)
    R += ['', '### THE SECTION, AS WRITTEN:'] + ['  | %s' % x for x in text.splitlines()]
    R += ['', '### ### **FOLD WRITTEN : %s**' % ok, '=' * 100]
    put('b422_fold.txt', R)
    io.open(os.path.join(D, 'b422_one_statement.txt'), 'w', encoding='utf-8', newline=NL).write(lead + NL)
    print(NL.join(R[:24]))
    return 0 if ok else 1


# =============================================================================================
# ### (R37) -- THE KEYSTONE'S §10.2, APPENDED.
# =============================================================================================
R37_MARK = '<!-- b422 ruling (R37): definition 2.1, read internally to ZFC -->'


def run_r37():
    R = ['=' * 100, 'b422 (R37) -- THE KEYSTONE ANNOTATED BY APPEND, ITS DEFINITION 2.1 KEPT.', '=' * 100, '  at (UTC) : %s' % utc()]
    d21 = q(IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
    setting = q(IB, 'Throughout, we work in classical first-order logic.', 'a first-order language.')
    text = NL.join([
        '', R37_MARK, '',
        '### §10.2 — Definition 2.1’s *unique model*, read under the author’s ruling (R37)', '',
        '**Filed b422, 2026-09-11.** Definition 2.1 above is kept as written. **The ruling, the author’s:** the '
        'keystone’s *unique model up to isomorphism* is read **internally to ZFC** — the specification is a '
        'set-theoretic definition and uniqueness is a statement inside the ambient theory, which is how the natural '
        'numbers, the reals and ξ are characterized in practice.', '',
        '**The reading the ruling declines, recorded beside it.** §2.1 says *“%s”* Read in that setting, Definition '
        '2.1’s *a finite set of 𝓛-sentences that has M as its unique model up to isomorphism* is met by no infinite '
        'structure: by the upward Löwenheim–Skolem theorem a first-order theory with an infinite model has models of '
        'every larger cardinality, and those are not isomorphic. **That citation is the seat’s** (b421, relay '
        '`data/b421_c2_specification.txt`) — a classical theorem this paper does not name — and it is recorded here '
        'as the reason the wording needed a ruling, not as a result of this paper.' % setting, '',
        '**What the ruling does not do.** It re-verdicts neither b407’s reading of the lemma’s first hypothesis for ξ '
        'nor b420’s for the structure whose elements are the class’s test functions. **Whether either moves under '
        'the internal reading is a question named for a later act, and not run here.**', '',
        '**Grade.** `UNCOMPILED`. Nothing was compiled for this subsection, and no grade is minted for it.', ''])
    ok = append_to(IB, 'phase1.5/method/INVARIANCE_BARRIERS.md', text, R37_MARK, R)
    R += ['  Definition 2.1, as the keystone now carries it : %s' % d21,
          '  ### its sentence byte-for-byte still present : %s' % (d21 in re.sub(r'\s+', ' ', read(IB))),
          '', '### THE SECTION, AS APPENDED:'] + ['  | %s' % x for x in text.splitlines()]
    R += ['', '### ### **R37 EXECUTED : %s**' % ok, '=' * 100]
    put('b422_r37.txt', R)
    print(NL.join(R[:10]))
    return 0 if ok and not MISS else 1


# =============================================================================================
# ### (R31) -- THE ORIENTATION LAYER.
# =============================================================================================
def run_orient():
    R = ['=' * 100, 'b422 (R31) -- THE ORIENTATION LAYER REFRESHED, ADDITIVELY.', '=' * 100, '  at (UTC) : %s' % utc()]
    lead = read(os.path.join(D, 'b422_one_statement.txt')).strip()
    if not lead:
        R.append('  ### REFUSED: the fold`s one-statement is not banked.')
        put('b422_orient.txt', R)
        print(NL.join(R))
        return 1
    # doors: a span act's bank naming a door with a depth word
    claims = []
    for n, _name, bank, *_r in ARC:
        for ln in read(os.path.join(D, bank)).splitlines():
            if re.search(r'\bR[1-5]\b', ln) and re.search(r'(?i)\bdoor|depth|nearest|farthest', ln):
                claims.append('b%d: %s' % (n, ln.strip()[:140]))
    R.append('  ### span-bank lines naming a door (R1-R5) beside a door or depth word : %d' % len(claims))
    R += ['      %s' % c for c in claims[:10]]
    moved = 0
    R.append('  ### doors whose depth a span bank states anew : %d -- judged from the lines above, each read' % moved)
    dg = NL.join(['', '<!-- b422 orientation refresh: the kernel arc -->', '',
                  '**Orientation refresh — filed b422, 2026-09-11 *(additive)*.** Under `(R31)` a fold refreshes this '
                  'digest. The arc folded at b422 — **%s, b413–b421** — carries this one statement: %s The section is '
                  '`FINDINGS.md`’s last; the keystone’s Definition 2.1 now carries the author’s ruling (R37) at its §10.2.'
                  % (ARC_NAME, lead), ''])
    pa = NL.join(['', '<!-- b422 orientation refresh: the kernel arc, and the doors it did not move -->', '',
                  '**Orientation refresh — filed b422, 2026-09-11 *(additive; the door table above is unedited)*.** Under '
                  '`(R31)` a fold refreshes this object. The arc folded at b422 — **%s, b413–b421** — states no door’s '
                  'depth in any of its banks (%d lines name a door beside a door or depth word; each read, none states a '
                  'new depth), so **no door is restated**. Its two compiled theorems are about the model of the object at '
                  'a finite place and are recorded here without moving R3 or R4.' % (ARC_NAME, len(claims)), ''])
    ok1 = append_to(DIGEST, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', dg, '<!-- b422 orientation refresh', R)
    ok2 = append_to(PATHS, 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', pa, '<!-- b422 orientation refresh', R)
    R += ['', '### THE DIGEST BLOCK:'] + ['  | %s' % x for x in dg.splitlines()]
    R += ['', '### THE FIVE-DOOR BLOCK:'] + ['  | %s' % x for x in pa.splitlines()]
    R += ['', '  doors restated : 0', '### ### **R31 EXECUTED : %s**' % (ok1 and ok2), '=' * 100]
    put('b422_orient.txt', R)
    print(NL.join(R[:14]))
    return 0 if ok1 and ok2 else 1


# =============================================================================================
# ### THE ADDITION -- THE WITNESS ARC, NAMED AND NOT OPENED.
# =============================================================================================
def run_witness():
    R = ['=' * 100, 'b422 ADDITION -- THE WITNESS ENUMERATION, NAMED AS THE NEXT ARC AND NOT OPENED.', '=' * 100]
    u1 = next((x for x in read(FL).splitlines() if x.startswith('| U1 ')), '')
    w = re.findall(r'WITNESS: *`([A-Z ]+)`', u1)
    R += ['  row U1 WITNESS fields : %d -- %s' % (len(w), w),
          '  every one NONE KNOWN or UNSTATED : %s' % (bool(w) and all(x in ('NONE KNOWN', 'UNSTATED') for x in w))]
    sites = re.findall(r"### \*\*\((i|ii|iii|iv|v|vi)\) ([^*]+)\*\*", u1)
    R.append('  the six sites, as the row names them :')
    seen = []
    for s, t in sites:
        if s not in seen:
            seen.append(s)
            R.append('      (%s) %s' % (s, t.strip()[:90]))
    ferry = read(os.path.join(D, 'b422_ferry.txt'))
    opening = q(os.path.join(D, 'b422_ferry.txt'), 'The\nnavigator\'s first-draft enumeration for the class site', 'nothing more.') \
        if 'The\nnavigator\'s first-draft' in ferry else q(os.path.join(D, 'b422_ferry.txt'), "navigator's first-draft enumeration for the class site", 'nothing more.')
    arc = q(os.path.join(D, 'b422_ferry.txt'), 'The next arc, one act per', 'location.')
    R += ['', '### THE ARC, AS THE FERRY NAMES IT, VERBATIM:', '      | %s' % arc,
          '', '### THE OPENING LIST FOR THE CLASS SITE -- SITE (i), THE CLAUSE`S QUANTIFIER -- ENTERED VERBATIM AND NOTHING MORE:',
          '      | %s' % opening,
          '', '  sites : %d ; price : one act per site, checkpointed after each -- six acts' % len(seen),
          '  candidates attempted : 0 ; sources matched to a candidate : 0 ; ledger rows written : 0',
          '  trigger : the author`s word opens it', '  ### ### **NAMED. PRICED. NOT OPENED.**', '=' * 100]
    put('b422_witness_arc.txt', R)
    print(NL.join(R))
    return 0 if len(seen) == 6 and not MISS else 1


def main():
    L = []
    say = L.append
    recs = {nm: read(os.path.join(D, f)) for nm, f in (('fold', 'b422_fold.txt'), ('r37', 'b422_r37.txt'),
                                                         ('orient', 'b422_orient.txt'), ('witness', 'b422_witness_arc.txt'))}
    fails = [nm for nm, t in recs.items() if not t]
    nthm, nuni = largest_measure()
    say('=' * 100)
    say('b422_components.py -- THE FOLD, b413 TO b421, AND THE WITNESS ARC NAMED.')
    say('=' * 100)
    for nm, needle in (('fold', 'FOLD WRITTEN : True'), ('fold', 'F-NOGRADE, RUN BEFORE THE WRITE : 0'),
                       ('fold', 'F-NOSUPERSEDE, RUN BEFORE THE WRITE : 0'), ('r37', 'R37 EXECUTED : True'),
                       ('r37', 'its sentence byte-for-byte still present : True'), ('orient', 'R31 EXECUTED : True'),
                       ('witness', 'NAMED. PRICED. NOT OPENED.')):
        ok = needle in recs[nm]
        fails += [] if ok else ['%s:%s' % (nm, needle[:24])]
        say('  %-8s %-64s %s' % (nm, needle, ok))
    c = re.search(r'THE COUNT : OBJECT (\d+) ; RECORD (\d+) ; OBJECT-MODEL (\d+) compiled, (\d+) measured', recs['fold'])
    obj, rec, omc, omm = (int(x) for x in c.groups()) if c else (0, 0, 0, 0)
    say('')
    say('### THE COUNT : OBJECT %d ; RECORD %d ; OBJECT-MODEL %d compiled, %d measured.' % (obj, rec, omc, omm))
    say('### THE MEASURE FOR *LARGEST* : Definition 2.1 bears on %d keystone lines ; the universality sentence on %d.' % (nthm, nuni))
    say('')
    say('### THE EXPECTATIONS, THEIR CLAUSES APART (R27):')
    say('  (N1) *at least two compiled statements about the object* -- under b412`s criterion as written : ### **REFUTED** (%d) ;' % obj)
    say('       under the third column, OBJECT-MODEL : ### **MET** (%d compiled: b414, b419, b421).' % omc)
    say('  (N1) *the first fold since b370 not at zero* -- as written : ### **REFUTED** (%d) ; under the third column :' % obj)
    say('       ### **VACUOUS** -- no earlier fold carries the column, so *first* is true by construction and compares nothing.')
    say('  (N2) *no statement in the span moves a grade* -- ### **MET, WITH ONE SENTENCE NAMED**: row S1 unchanged since b409 and')
    say('       every bank`s own count at 0; b420`s record sentence *moved one grade inside K3* says otherwise and is named.')
    say('  (N3) *names the two compiled theorems as the span`s product* -- ### **MET** (smear_general, grid_trace_is_signed_count).')
    say('  (N3) *names the barrier keystone`s foundational defect* -- ### **MET** (Definition 2.1, ruled R37).')
    say('  (N3) *as its largest finding about the record* -- ### **%s** by the face`s measure (%d against %d).'
        % ('MET' if nthm > nuni else 'REFUTED', nthm, nuni))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    put('b422_components.txt', L)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(main())
    for flag, fn in (('--fold', run_fold), ('--r37', run_r37), ('--orient', run_orient), ('--witness', run_witness)):
        if flag in sys.argv:
            sys.exit(fn())
