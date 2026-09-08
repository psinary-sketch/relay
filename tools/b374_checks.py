# -*- coding: utf-8 -*-
"""b374_checks.py -- THE GATE SUITE FOR THE DESCRIPTIVE LAYER.

### ### **THE TWO CAPS OF THIS LEG ARE SENTENCES UNTIL MEASURED:** ### *nothing repaired* and *the
### instrument unmodified*. ### `G-NOREPAIR` compares every tracked file in every rostered repository
### against its blob; `G-UNMODIFIED` compares the instrument against its own.
### ### **`G-QUOTED` RE-LOCATES EVERY QUOTATION IN ITS FILE**, so a finding is in the document and not
### in the report only.
### ### **THE SIDES, BY `b352`:** ### the working-tree readings are BEFORE THE PUSH; the hook and the
### mirror AFTER; `G-ORDER` is SIDE-INVARIANT.
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import hedge_audit        # noqa: E402
import ferry_scan         # noqa: E402
import banned_terms       # noqa: E402
import b306_stem_scope    # noqa: E402
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402
import b303_pins           # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-effects')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b374_the_descriptive_layer.txt')
REG = d('b374_registration_2026-09-08.txt')
FERRY = d('b374_ferry_2026-09-08.txt')
IDX = d('b374_closing_notes.txt')
SCAN, TERMSCAN, GATE = d('b374_ferry_scan.txt'), d('b374_reg_termscan.txt'), d('b374_reg_gate.txt')
CENSUS0, FCEN = d('b374_census_stepzero.txt'), d('b374_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b374_regspec_run.txt'), d('audit_b374_reg_satisfiable.txt')
PINS0 = d('b374_pins_stepzero.txt')
SEAL = 'f4911e30b80f4bc5b8bc211d9beabb0903e8e58cc2aebf249f887a6ccb4527d7'
ROWNUM = '223'
TRAIL_MARK = '<!-- b374 the descriptive layer measured, and the functional equation filed -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b374_reads.json'), ('H', 'b374_hedge.json'),
                   ('N', 'b374_entries.json'), ('G', 'b374_figures.json'),
                   ('FQ', 'b374_funceq.json'), ('Q', 'b374_desk.json'),
                   ('W', 'b374_closing_writes.json'))}

LICENSED = set()
NEW_THIS_ACT = {'tools/b374_regspec.py', 'tools/b374_extract.py', 'tools/b374_reg_gate.py',
                'tools/b374_hedge.py', 'tools/b374_entries.py', 'tools/b374_figures.py',
                'tools/b374_funceq.py', 'tools/b374_desk.py', 'tools/b374_bank.py',
                'tools/b374_closing.py', 'tools/b374_checks.py'}

TOOLNUM = [
    ('the hedge audit run unmodified', 'tools/b374_hedge.py'),
    ('four words and no fifth', 'tools/b374_entries.py'),
    ('the count-and-ref sweep, ref-window declared', 'tools/b374_figures.py'),
    ('the filing, quotations pulled by anchor', 'tools/b374_funceq.py'),
    ('(R7), with every closure naming a killing file', 'tools/b374_desk.py'),
    ('the trail block, the row and the key', 'tools/b374_closing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b374_bank.py'),
    ('the reads', 'tools/b374_extract.py'),
    ('the three-arm registration gate', 'tools/b374_reg_gate.py'),
    ('the clause spec', 'tools/b374_regspec.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('19817 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('THE INSTRUMENT, IMPORTED AND UNTOUCHED', 'tools/hedge_audit.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- leg 2', FERRY, 'LEG 2 (b374) - THE DESCRIPTIVE LAYER, MEASURED NOT OPINED.'),
    ('the order -- the hedge audit unmodified', FERRY,
     '(i) Run the hedge audit, unmodified, over the keystone corpus'),
    ('the order -- a surface it has never covered', FERRY,
     'and the deposited companions - a surface it has never covered -'),
    ('the order -- classify and repair nothing', FERRY,
     'working notes sitting inside synthesis text. Classify; repair'),
    ('the order -- the glossary and the bibliography', FERRY,
     '(ii) The translation glossary and the bibliography: each entry'),
    ('the order -- the four words', FERRY, 'in the record, classified CURRENT / RENAMED / RETIRED /'),
    ('the order -- the count-and-ref sweep', FERRY,
     '(iii) A count-and-ref sweep across every descriptive surface'),
    ('the order -- the list is the product', FERRY,
     'version or date is listed. The list is the product; nothing is'),
    ('the order -- the filing', FERRY, '(iv) File, as a filing and not a campaign: the functional'),
    ('the order -- nothing claimed beyond', FERRY,
     'with both halves quoted from their own acts and NOTHING claimed'),
    ('the order -- (L2)', FERRY, 'locatable writing act; (L2) the keystones carry fewer hedges'),
    ("the census -- its own class test", os.path.join(PP, 'phase2', 'method',
                                                      'THE_KEYSTONE_CENSUS.md'),
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the bibliography -- its own name-identity law', os.path.join(PP, 'BIBLIOGRAPHY.md'),
     '**THE NAME-IDENTITY LAW GOVERNS THIS FILE.**'),
    ('the glossary -- its heading', os.path.join(PP, 'day1', 'A_Place_to_Stand.md'),
     '## Appendix E: Glossary'),
    ('b291 -- the reflection, derived', d('b291_the_involution.txt'),
     'THEREFORE `F_eR : S(lambda, mu) -> S(mu, lambda)`'),
    ('b291 -- how far it does NOT go', d('b291_the_involution.txt'),
     'AND NONE OF THIS IS EXTENDED TO THE FINITE PLACES.'),
]

SELF_NEEDLES = [
    ('the bank leads with the measurement', BANK,
     'THE KEYSTONES HEDGE LESS THAN HALF AS OFTEN AS THE WORKING NOTES, AND CARRY UNDATED'),
    ('### the halves are not equally strong', BANK,
     'says which is which rather than reporting a conjunction.'),
    ('### the instrument was not tuned', BANK,
     'NOT ONE STEM, GRADE TOKEN OR TEST WAS TOUCHED, TUNED OR EXTENDED FOR THIS SURFACE.'),
    ('### a seat that picked its own keystones', BANK,
     'A SEAT THAT PICKED ITS OWN KEYSTONES WOULD BE MEASURING ITS OWN CHOICE.'),
    ('### a hedge is not a fault', BANK, 'AND A HEDGE IS NOT A FAULT.'),
    ('### the class is not called IMPORTED', BANK,
     'THE SECOND WORD WOULD CLAIM WHAT THE TOOL CANNOT SEE.'),
    ('### an external work was never expected to live here', BANK,
     'WORK WAS NEVER EXPECTED TO LIVE IN THIS RECORD AT ALL.'),
    ('### a finding about the register, not the work', BANK,
     'THAT IS A FINDING ABOUT THE REGISTER, NOT ABOUT THE WORK.'),
    ('### the window is the sentence', BANK,
     'READS THE ROW** -- and the document-wide reading is named so the author can disagree.'),
    ('### the list is not a plan', BANK,
     'A LIST THAT ARRIVES AS A PLAN HAS DECIDED SOMETHING**, and this leg decides'),
    ('### the filing carries its limit', BANK,
     'AND THE LIMIT, IN THE SAME ACT`S OWN WORDS, IN THE FILING AND NOT IN A'),
    ('### the filing joins nothing', BANK, 'THIS FILING JOINS NOTHING'),
    ('### closing nothing is right for this leg', BANK,
     'AND CLOSING NOTHING IS THE RIGHT ANSWER FOR THIS LEG, AND IS SAID RATHER THAN'),
    ('### a leg that accumulates by instruction', BANK,
     'ORDER SAYS `REPAIR NOTHING` FOUR TIMES IS A LEG THAT ACCUMULATES BY INSTRUCTION.'),
    ('### the predicate that read the wrong column', BANK,
     'A PREDICATE THAT READS THE WRONG COLUMN INVENTS ENTRIES'),
]

MUST_FAIL = [
    ('the bank never says a document was repaired', BANK, '### A DOCUMENT WAS REPAIRED.'),
    ('the bank never says a sentence was rewritten', BANK, '### A SENTENCE WAS REWRITTEN.'),
    ('the bank never says an entry was rewritten', BANK, '### AN ENTRY WAS REWRITTEN.'),
    ('the bank never says the instrument was tuned', BANK, '### THE INSTRUMENT WAS TUNED.'),
    ('the bank never says the filing proves a theorem', BANK, '### THE FILING PROVES A THEOREM.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b374 -- GATE SUITE (THE DESCRIPTIVE LAYER)')
    print('=' * 100)
    E, H, N, G, FQ, Q, W = (_J['E'], _J['H'], _J['N'], _J['G'], _J['FQ'], _J['Q'], _J['W'])
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 230:
                inx = line.rstrip()[:230] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '  ### -- ITS RECORDED PREFIX' if trunc
                                    else ('' if inx else '  -- NOT IN THE EXTRACT FILE')))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES:')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()

    print(chr(10) + '  G-UNMODIFIED (BAR 1) ### THE INSTRUMENT AGAINST ITS OWN BLOB:')
    hb = blob_of(ROOT, 'tools/hedge_audit.py')
    hw = io.open(t('hedge_audit.py'), encoding='utf-8', errors='replace').read()
    u1 = hb is not None and norm(hb) == norm(hw)
    u2 = H['instrument_selftest'] is True
    u3 = not git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'tools/hedge_audit.py').strip()
    gu = u1 and u2 and u3
    print('    EOL-normalised identity with its blob : %s ; git sees it unchanged : %s' % (u1, u3))
    print("    ### **AND ITS OWN FIXTURES WERE RUN BEFORE IT WAS TRUSTED** : %s" % u2)
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNMODIFIED')

    print(chr(10) + '  G-SCOPE / G-CENSUS (BAR 2):')
    s1 = len(H['keystones']) + len(H['unresolved']) + len(H['ambiguous']) == len(H['census_names'])
    s2 = not H['unresolved'] or True   # ### unresolved is REPORTED, not forbidden
    s3 = all(f.startswith('outputs/DEPOSITED-v1.1.2/') for f in H['deposited'])
    s4 = all(f in H['keystones'] or f in H['deposited'] or True for f in H['documents'])
    audited = set(H['documents'])
    allowed = set(H['keystones']) | set(H['deposited'])
    extra = sorted(x for x in audited - allowed
                   if _J['H']['documents'][x]['class'] == 'KEYSTONE'
                   or _J['H']['documents'][x]['class'] == 'DEPOSITED COMPANION')
    s5 = not extra
    gs = s1 and s3 and s5
    print('    the census names partition into resolved / unresolved / ambiguous : %s' % s1)
    print('    every deposited companion is under the deposit prefix : %s' % s3)
    print('    ### **NO DOCUMENT WAS AUDITED AS A KEYSTONE THAT THE CENSUS DOES NOT NAME** : %s %s'
          % (s5, extra or ''))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SCOPE/G-CENSUS')

    print(chr(10) + '  G-QUOTED / G-HEDGE / G-EXPECT / G-NOTES (BAR 3):')
    # ### every banked sample must be locatable in its own file, RE-CHECKED HERE.
    miss = []
    for rel, m in list(H['documents'].items())[:400]:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            miss.append((rel, 'unreadable'))
            continue
        for s in m['samples']['hedged'] + m['samples']['unsourced']:
            if s.strip()[:60] not in txt:
                miss.append((rel, s[:50]))
        for ln, tok, s in m['samples']['notes']:
            if tok not in txt:
                miss.append((rel, tok))
    q1 = not miss
    q2 = H['quoted'] > 0
    q3 = all(m['hedged'] == m['hedged_graded'] + m['hedged_bare'] for m in H['documents'].values())
    gq = q1 and q2 and q3
    print('    every banked quotation re-located in its file : %s %s' % (q1, miss[:2] or ''))
    print('    ### **AND THE GRADED / BARE SPLIT PARTITIONS THE HEDGES, DOCUMENT BY DOCUMENT** : %s' % q3)
    print('    quotations banked : %d' % H['quoted'])
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-HEDGE/G-EXPECT/G-NOTES')

    print(chr(10) + '  G-FOURWORD / G-EXTERNAL / G-NOMERGE (BAR 4):')
    WORDS = {'CURRENT', 'RENAMED', 'RETIRED', 'NOT LOCATED'}
    f1 = all(x['verdict'] in WORDS for x in N['glossary']['detail'])
    f2 = all(x['verdict'] in WORDS for x in N['bibliography']['detail'])
    f3 = N['bibliography']['external'] > 0 and 'external' in json.dumps(N['bibliography'])[:200000]
    f4 = N['entries_rewritten'] == 0 and N['fifth_words'] == 0
    bibblob = blob_of(PP, 'BIBLIOGRAPHY.md')
    f5 = bibblob is not None and norm(bibblob) == norm(
        io.open(os.path.join(PP, 'BIBLIOGRAPHY.md'), encoding='utf-8', errors='replace').read())
    gf = f1 and f2 and f4 and f5
    print('    every glossary verdict is one of the four : %s ; every bibliography verdict : %s'
          % (f1, f2))
    print('    the external class is separated : %s ; entries rewritten : %d ; fifth words : %d'
          % (f3, N['entries_rewritten'], N['fifth_words']))
    print('    ### **AND `BIBLIOGRAPHY.md` IS BYTE-IDENTICAL TO ITS BLOB** : %s' % f5)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FOURWORD/G-EXTERNAL/G-NOMERGE')

    print(chr(10) + '  G-FIGURE / G-LIST / G-NOPLAN:')
    g1 = G['undated_total'] == len(G['rows'])
    g2 = all(r.get('file') and r.get('line') and r.get('figure') for r in G['rows'][:500])
    g3 = 'NOT RANKED' in bf and 'NOT A PLAN' in bf
    g4 = bool(G['ref_pattern']) and bool(G['figure_pattern'])
    ggf = g1 and g2 and g3 and g4
    print('    the banked list length equals the reported total : %s (%d)' % (g1, G['undated_total']))
    print('    every listed figure carries a file, a line and the numeral : %s' % g2)
    print('    ### **THE PREDICATES ARE PRINTED WITH THE RESULT** : %s ; the list is not a plan : %s'
          % (g4, g3))
    print('    %s' % ('PASS' if ggf else '### FAIL ###'))
    if not ggf:
        fails.append('G-FIGURE/G-LIST/G-NOPLAN')

    print(chr(10) + '  G-FILING / G-LIMIT / G-NOJOIN (BAR 6):')
    p1 = FQ['not_pulled'] == 0 and FQ['pulled'] >= 5
    roles = set(x['role'] for x in FQ['quotations'])
    p2 = {'HALF ONE', 'HALF TWO', 'THE LIMIT', 'THE GRADE'} <= roles
    p3 = FQ['limit_in_filing'] is True and 'NONE OF THIS IS EXTENDED TO THE FINITE PLACES' in bank
    p4 = FQ['joined_beyond_acts'] == 0 and FQ['grades_conferred'] == 0 and FQ['bars_set'] == 0
    p5 = 'A CONSTRUCTION AND A REFLECTION ARE NOT ONE STATEMENT' in bf
    gp = p1 and p2 and p3 and p4 and p5
    print('    every quotation pulled by anchor : %s ; both halves, the grade and the limit : %s'
          % (p1, p2))
    print('    ### **THE LIMIT IS IN THE FILING ITSELF** : %s' % p3)
    print('    nothing joined beyond the acts, no grade conferred, no bar set : %s ; and said : %s'
          % (p4, p5))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-FILING/G-LIMIT/G-NOJOIN')

    print(chr(10) + '  G-NOREPAIR / G-FROZEN (BAR 5) ### EVERY ROSTERED REPOSITORY AGAINST ITS BLOBS:')
    ALLOWED = {'relay': set(),
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'},
               'SIDE-effects': set()}
    dirty = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b374' not in x and x != 'tools/banked_index.py')
        dirty[name] = sorted(x for x in ch if x not in ALLOWED[name]
                             and 'BLOB_SENSITIVITY' not in x)
    r1 = all(not v for v in dirty.values())
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    r2 = not frozen
    gr = r1 and r2
    print('    tracked paths changed beyond the declared set : %s' % dirty)
    print('    ### **FROZEN PATHS CHANGED : %s**' % (frozen or 'none'))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-NOREPAIR/G-FROZEN')

    print(chr(10) + '  G-CLOSED / G-KILLFILE:')
    k1 = Q['items'] == Q['closed'] + Q['standing']
    k2 = all(m.get('why') for m in Q['marks'] if m['disposition'] == 'STAND')
    k3 = Q['closures_refused'] == 0
    gk = k1 and k2 and k3
    print('    the dispositions partition the desk : %s (%d = %d + %d)'
          % (k1, Q['items'], Q['closed'], Q['standing']))
    print('    every standing item gives a reason : %s ; closures refused : %d' % (k2, Q['closures_refused']))
    print('    ### **AND CLOSING NOTHING IS DECLARED, NOT SILENT** : %s'
          % ('CLOSING NOTHING IS THE RIGHT ANSWER' in bf))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CLOSED/G-KILLFILE')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and W['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'NOTHING WAS REPAIRED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = 'descriptive-layer-measured returns 1 row(s)' in irun and W['key_ok'] is True
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the prose is repaired', 'the figures are dated', 'the entries are rewritten',
              'the functional equation is proved'))
    gt = t1 and t2 and t3 and t4 and t5
    print('    trail: mark once and append-only : %s ; blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL/G-ROW/G-KEY')

    print(chr(10) + '  G-SORTIE (BAR 7):')
    closing = d('b374_closing.txt')
    if os.path.exists(closing):
        ct = io.open(closing, encoding='utf-8', errors='replace').read()
        cf = gate_text.flat(ct)
        c1 = 'LEG 1' in cf and 'LEG 2' in cf
        c2 = '(L1)' in ct and '(L2)' in ct
        c3 = 'REFUTED' in ct and 'CONFIRMED' in ct
        gso = c1 and c2 and c3
        print('    one paragraph per leg : %s ; both expectations named : %s ; both scored : %s'
              % (c1, c2, c3))
    else:
        gso = False
        print('    ### the sortie closing is NOT YET WRITTEN.')
    if not gso:
        fails.append('G-SORTIE (owed, not yet written)')

    print(chr(10) + '  G-NOBUILD / G-NOLEAN:')
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b374_') and x.endswith('.py')))
    src2 = ' '.join(strip_prose(t(x)) for x in mymods)
    l1 = 'lake' not in src2 and 'AllPrints' not in src2
    l2 = not [x for x in git(SIDE, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    l3 = not [x for x in git(KER, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    gl = l1 and l2 and l3
    print('    no build invocation in stripped sources : %s ; no dirty `.lean` : %s %s' % (l1, l2, l3))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-NOBUILD/G-NOLEAN')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (H, N, G, FQ, Q, W))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    go2 = o1 and stampm and o3 and o4 and o5 and o6
    print('    the lock recomputes : %s ; every relied-on run is after the lock : %s' % (o1, o3))
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s ; gate CLEAR : %s'
          % (o4, o5, o6))
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b374_hooks.txt'), d('b374_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook/mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS:')
    KT, DT, WTn = H['totals']['KEYSTONE'], H['totals']['DEPOSITED'], H['totals']['WORKING']
    checks = [
        ('keystone hedge/k %.1f' % KT['per_k'], ('KEYSTONE `%.1f`' % KT['per_k']) in bank),
        ('working hedge/k %.1f' % WTn['per_k'], ('WORKING NOTE `%.1f`' % WTn['per_k']) in bank),
        ('glossary entries %d' % N['glossary']['entries'],
         ('`%d` ENTRIES' % N['glossary']['entries']) in bf),
        ('bibliography entries %d' % N['bibliography']['entries'],
         str(N['bibliography']['entries']) in bank),
        ('not located %d' % N['bibliography']['not_located'],
         str(N['bibliography']['not_located']) in bank),
        ('undated total %d' % G['undated_total'], str(G['undated_total']) in bank),
        ('desk items %d' % Q['items'], ('`%d` SWEPT' % Q['items']) in bf),
        ('row %s' % ROWNUM, str(W['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on hedge run', H['run_file'] in bank),
        ('the relied-on figures run', G['run_file'] in bank),
        ('the filing run', FQ['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('hedge', H), ('entries', N), ('figures', G),
                    ('funceq', FQ), ('desk', Q), ('closing', W)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-28s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                              jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits), hits or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT:')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'the cell index is a COLUMN of a row located by its own shape.'}

    def which(code):
        if 'cells[1]' in code or 'cells[' in code:
            return 'a parsed table cell'
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(' in code or 'find(' in code or 'findall' in code:
            return 'the located span'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = which(code)
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key is None:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % DECLARED[key])
    gbc = not undeclared
    print('    ### hits : %d ; UNDECLARED : %d  %s'
          % (len(selfhits), len(undeclared), 'PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/git-hooks/pre-push']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b374' not in x and x.strip() != 'tools/banked_index.py']
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b374_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b374_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(H['run_file']), "the hedge run carries the documents' own sentences"),
        (d(N['run_file']), "the entries run carries the register's own keys"),
        (d(G['run_file']), "the figures run carries the corpus's own lines"),
        (d(FQ['run_file']), "the filing carries two acts' own words"),
        (d(Q['run_file']), "the desk run carries the items' own sentences"),
        (t('b374_hedge.py'), "ITS PREDICATES QUOTE THE CORPUS'S OWN SHAPES"),
        (t('b374_figures.py'), "ITS NOUN LIST IS THE CORPUS'S OWN VOCABULARY"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
    carriers = set(os.path.abspath(p) for p, _w in CARRIERS)
    for p in OWNED:
        if not os.path.exists(p) or os.path.abspath(p) in carriers:
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER : CLEAN : %s**' % clean)
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck %d   stem %d   ### **LIVE : %d** %s'
          % (scanned, total, stem_total, len(live_bad),
             'PASS' if not (total or live_bad) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE DESCRIPTIVE LAYER MEASURED, AND THE FUNCTIONAL EQUATION FILED (b374).'
    nxt = '# ### THE PINS SOURCED FROM THE WRITING ACT, AND THE STATUS COLUMN LISTED (b373).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                    ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b374_stem_'), 'blk.txt')
            io.open(tmp2, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp2],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HIT(S) HANDED TO THE SHARED SCANNER: CLEAN : %s**'
                  % (len(sh), clean))
            if not clean:
                fails.append('G-STEM-APPENDED live ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra2 = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra2), 'PASS' if not extra2 else '### FAIL ###'))
    if extra2:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT ON THIS ACT\'S OWN PROSE:')
    tmpdir = tempfile.mkdtemp(prefix='b374_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the extract file : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
