# -*- coding: utf-8 -*-
"""b373_checks.py -- THE GATE SUITE FOR THE PINS AND THE STATUS COLUMN.

### ### **`G-NOHEAD` AND `G-SOURCED` RE-DERIVE THE PIN EVIDENCE RATHER THAN TRUSTING THE TOOL'S JSON**:
### every pin the act located is re-read out of the banked file it claims to come from.
### ### **`G-FROZEN` AND `G-NOREGRADE` COMPARE THE PAPERS REPOSITORY AGAINST ITS BLOBS**, because the
### two caps of this act -- no frozen surface edited, no grade moved -- are sentences until measured.
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

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-effects')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b373_the_pins_and_the_status_column.txt')
REG = d('b373_registration_2026-09-08.txt')
FERRY = d('b373_ferry_2026-09-08.txt')
CORR, IDX = d('b373_corr_run.txt'), d('b373_index_run.txt')
SCAN, TERMSCAN, GATE = d('b373_ferry_scan.txt'), d('b373_reg_termscan.txt'), d('b373_reg_gate.txt')
CENSUS0, FCEN = d('b373_census_stepzero.txt'), d('b373_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b373_regspec_run.txt'), d('audit_b373_reg_satisfiable.txt')
PINS0 = d('b373_pins_stepzero.txt')
SEAL = '710dcc0688509502e4ef3464c34e2e95b9a51da6eedf7fad48411a738699d66a'
ROWNUM = '222'
TRAIL_MARK = '<!-- b373 the pins sourced from the writing act, and the status column listed -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b373_reads.json'), ('P', 'b373_pins.json'),
                   ('S', 'b373_status.json'), ('Q', 'b373_desk.json'),
                   ('F', 'b373_filing.json'))}

LICENSED = {'tools/b304_hooks.py'}
NEW_THIS_ACT = {'tools/b373_regspec.py', 'tools/b373_extract.py', 'tools/b373_reg_gate.py',
                'tools/b373_pins.py', 'tools/b373_status.py', 'tools/b373_desk.py',
                'tools/b373_filing.py', 'tools/b373_bank.py', 'tools/b373_correspondence.py',
                'tools/b373_index_append.py', 'tools/b373_checks.py'}

TOOLNUM = [
    ('the sourcing chain, and every link failure named', 'tools/b373_pins.py'),
    ('the grade sweep and its three-way split', 'tools/b373_status.py'),
    ('(R7), with every closure naming a killing file', 'tools/b373_desk.py'),
    ('the closures and the routing filed', 'tools/b373_filing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b373_bank.py'),
    ('the reads', 'tools/b373_extract.py'),
    ('the three-arm registration gate', 'tools/b373_reg_gate.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 222', 'tools/b373_correspondence.py'),
    ('the key', 'tools/b373_index_append.py'),
    ('the clause spec', 'tools/b373_regspec.py'),
    ('20255 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('the one licensed instrument, corrected', 'tools/b304_hooks.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
    ('the pinless set this act walked', 'tools/b371_inventory.py'),
    ("b372's per-declaration verdicts", 'tools/b372_batch.py'),
    ("b369's absent list", 'tools/b369_repair.py'),
]

OWNER_NEEDLES = [
    ('the order -- the sortie', FERRY,
     'CONCURRENCY: SOLO (research seat). SORTIE: two legs in order,'),
    ('the order -- (R9)', FERRY, 'strikeable: A CITING ROW NAMES A PIN. b372'),
    ('the order -- the sourcing rule', FERRY,
     'therefore ADDED to citing rows, and sourced ONLY from the act'),
    ('the order -- never from the current head', FERRY,
     'current head, which would date the claim to today rather than'),
    ('the order -- the unknown-ref mark', FERRY,
     'is marked CITES-AT-AN-UNKNOWN-REF and left, which is honest and'),
    ('the order -- priced first', FERRY, 'is not a pin. Priced first; if the price does not fit one act,'),
    ('the order -- leg 1', FERRY, 'LEG 1 (b373) - THE PINS AND THE STATUS COLUMN. The executor'),
    ('the order -- the count reported plainly', FERRY,
     'and the count of rows whose act could not be located reported'),
    ('the order -- a claim about what is verified', FERRY,
     'is a claim about what is verified, not a stale number - each'),
    ('the order -- the hooks tool', FERRY,
     'moved by the seat. Also: the hooks tool carries a sentence that'),
    ('the order -- leg 2, named and not opened here', FERRY,
     'LEG 2 (b374) - THE DESCRIPTIVE LAYER, MEASURED NOT OPINED.'),
    ("the order -- the navigator's expectations", FERRY,
     'the next ferry as DRAFT - NAVIGATOR EDITS. The navigator'),
    ("b372's finding, which (R9) rests on", d('b372_the_first_batch.txt'),
     'AND ONE COMPARISON INSIDE THIS ACT IS THE WHOLE ARGUMENT FOR'),
    ('a banked pins record, the shape the ref is read from', d('b329_pins_stepzero.txt'),
     '    local HEAD   : 50200cc7c84512e092bdb9139f3cbfe3a045ed45'),
]

SELF_NEEDLES = [
    ('the bank says it wrote no pin', BANK,
     'WAS EXECUTED AS FAR AS ITS OWN SOURCING RULE ALLOWS, AND IT WROTE NO PIN.'),
    ('### the papers are older than the instruments', BANK,
     'THE PAPERS ARE OLDER THAN THE INSTRUMENTS. ### THAT IS THE FINDING.'),
    ('### a good rule reaching back', BANK,
     'RECORD THAT DID NOT YET KEEP THE EVIDENCE THE RULE REQUIRES.'),
    ('### the scope was fixed before the read', BANK,
     'registration`s face before any read, not a discovery made when the edit got difficult.'),
    ('### the defect is bounded', BANK,
     'found ### **NO INSTANCE OUTSIDE THAT SET**, which bounds the problem rather than widening it.'),
    ('### no grade moved', BANK, 'NO GRADE WAS MOVED BY THIS SEAT.**'),
    ('### the two failure kinds are not the same problem', BANK,
     'PROBLEM.** ### Collapsing them into one number would have hidden the only thing this'),
    ('### the bar tests the value, the ruling forbids the source', BANK,
     'BAR TESTS THE VALUE; THE RULING FORBIDS THE SOURCE; A KERNEL THAT HAS NOT MOVED MAKES THE'),
    ('### the caveat kept, not deleted', BANK,
     'A CORRECTION THAT DELETES THE CAVEAT IS A WORSE'),
    ('### an item that changes meaning while keeping its name', BANK,
     'NEVER CLOSES ANYTHING.**'),
    ('### appending is not editing', BANK,
     'AND THIS ACT APPENDED TO A LEDGER IT REFUSED TO EDIT.'),
    ('### (L1) refuted', BANK, 'act.* ### REFUTED, BY A PRINTED CLASSIFICATION.**'),
    ('### the seat predicted the wrong wall', BANK,
     'THIS SEAT PREDICTED THE ROSTER WOULD BE THE WALL AND THE COMMIT SUBJECTS WERE.'),
    ('### the species this act committed in its own tool', BANK,
     'INSTRUMENT.**'),
    ('### the scope of a search is a predicate', BANK,
     'MET AGAIN -- THE SCOPE OF A SEARCH IS A PREDICATE.'),
]

MUST_FAIL = [
    ('the bank never says a pin was taken from the head', BANK, '### A PIN WAS TAKEN FROM THE HEAD.'),
    ('the bank never says a grade was moved', BANK, '### A GRADE WAS MOVED.'),
    ('the bank never says a deposited file was edited', BANK, '### A DEPOSITED FILE WAS EDITED.'),
    ('the bank never says an archive was edited', BANK, '### AN ARCHIVE WAS EDITED.'),
    ('the bank never says a row was checked at its new pin', BANK,
     '### A ROW WAS CHECKED AT ITS NEW PIN.'),
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
    print('b373 -- GATE SUITE (THE PINS AND THE STATUS COLUMN)')
    print('=' * 100)
    E, P, S, Q, F = (_J['E'], _J['P'], _J['S'], _J['Q'], _J['F'])
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
    DET = P['detail']
    PINNABLE = [x for x in DET if x['status'] == 'PINNABLE']

    print(chr(10) + '  G-CHAIN / G-SOURCED (BAR 1) ### THE PIN EVIDENCE RE-DERIVED HERE:')
    bad = []
    for x in PINNABLE:
        src = d(x['pin_from'])
        if not os.path.exists(src):
            bad.append((x['file'], 'the banked file it names does not exist'))
            continue
        txt = io.open(src, encoding='utf-8', errors='replace').read()
        if x['pin'][:7] not in txt:
            bad.append((x['file'], 'the pin is not in the banked file it names'))
    c1 = not bad
    c2 = all(x.get('act') for x in PINNABLE)
    c3 = all(x['anchor'] == 'BY CONTENT' for x in DET if 'anchor' in x)
    c4 = P['pinnable'] + P['unknown'] == P['rows']
    gc = c1 and c2 and c3 and c4
    print('    every pin re-read out of the banked file it claims : %s %s' % (c1, bad or ''))
    print('    every pinnable row names the act it came from : %s' % c2)
    print('    ### **EVERY ROW RE-ANCHORED BY CONTENT, NEVER BY LINE NUMBER** : %s' % c3)
    print('    the classification partitions the set : %s (%d + %d = %d)'
          % (c4, P['pinnable'], P['unknown'], P['rows']))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CHAIN/G-SOURCED')

    print(chr(10) + '  G-NOHEAD (BAR 2) ### THE PROHIBITION, MEASURED:')
    written = [x for x in DET if x.get('write') == 'WRITTEN']
    heads = set(P['heads'].values())
    n1 = P['written'] == 0 and not written
    n2 = not [x for x in written if x['pin'] in heads]
    src = strip_prose(t('b373_pins.py'))
    n3 = 'rev-parse' in src
    gn = n1 and n2
    print('    pins written : %d ### -- and none may equal a head' % P['written'])
    print('    ### **PINS THIS ACT LOCATED THAT EQUAL A CURRENT HEAD : %d**' % P['equals_a_head'])
    print('    ### ### **NONE OF THEM WAS WRITTEN** : %s' % n2)
    print('    ### the tool reads heads only to refuse them (it does resolve refs) : %s' % n3)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOHEAD')

    print(chr(10) + '  G-UNKNOWN (BAR 5) ### EVERY UNPINNED ROW HAS A STATED REASON:')
    unk = [x for x in DET if x['status'] == 'CITES-AT-AN-UNKNOWN-REF']
    u1 = all(x.get('reason') for x in unk)
    named = {"INTRODUCING COMMIT NOT LOCATED", "WRITING ACT NOT NAMED",
             "NO PINS RECORD AND NO REF IN THE ACT'S BANK", "KERNEL NOT ON THAT ACT'S ROSTER",
             "ROW NAMES NO PLACEABLE KERNEL", "ROW NOT RE-ANCHORABLE BY CONTENT",
             "THE ACT'S BANK NAMES MORE THAN ONE REF FOR THAT KERNEL"}
    u2 = set(x['reason'] for x in unk) <= named
    u3 = len(unk) == P['unknown']
    gu = u1 and u2 and u3
    print('    every unpinned row has a reason : %s ; all reasons are declared ones : %s' % (u1, u2))
    print('    reasons seen : %s' % sorted(set(x['reason'] for x in unk)))
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNKNOWN')

    print(chr(10) + '  G-SCOPE / G-FROZEN (BAR 4) ### THE FROZEN SURFACES, COMPARED TO THEIR BLOBS:')
    changed = sorted(x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
                     if x.strip())
    frozen_touched = [x for x in changed
                      if x.startswith('outputs/DEPOSITED-') or x.startswith('archive/')
                      or os.path.basename(x) in ('FINDINGS.md', 'ERRATA.md', 'FACES_LEDGER.md')]
    f1 = not frozen_touched
    f2 = changed in ([], ['OPEN_TRAILS.md'])
    f3 = all(x['excluded'] for x in PINNABLE)
    f4 = 'ROUTED, NOT DECIDED' in bf or 'routed, not decided' in bank.lower()
    gf = f1 and f2 and f3 and f4
    print('    tracked papers files changed : %s' % changed)
    print('    ### **FROZEN OR LEDGER PATHS AMONG THEM : %s**' % (frozen_touched or 'none'))
    print('    every pinnable row was on an excluded surface : %s ; the exclusion is routed : %s'
          % (f3, f4))
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-SCOPE/G-FROZEN')

    print(chr(10) + '  G-STATUS / G-NOREGRADE / G-CARRIER / G-ROUTED (BAR 6):')
    s1 = S['grades_moved'] == 0
    # ### **NO GRADE TOKEN ANYWHERE DIFFERS FROM ITS BLOB** -- measured, not asserted.
    s2 = True
    for h in S['detail']:
        blob = blob_of(PP, h['file'])
        if blob is None:
            s2 = False
            break
        lines = norm(blob).split(chr(10))
        if h['line'] - 1 >= len(lines) or lines[h['line'] - 1].strip() != h['text']:
            s2 = False
            break
    s3 = all(h['file'] for h in S['detail'])
    s4 = S['hits'] == S['defect'] + S['corrected'] + S['live_graded']
    s5 = 'THREE CHOICES' in bf.upper()
    gs = s1 and s2 and s3 and s4 and s5
    print('    grades moved : %d ; every swept row is byte-identical to its blob : %s' % (0, s2))
    print('    every hit names its carrier : %s ; the three-way split partitions the hits : %s (%d = %d + %d + %d)'
          % (s3, s4, S['hits'], S['defect'], S['corrected'], S['live_graded']))
    print('    ### **THE CONSEQUENCE IS ROUTED WITH ITS CHOICES NAMED** : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-STATUS/G-NOREGRADE/G-CARRIER/G-ROUTED')

    print(chr(10) + '  G-INSTRUMENT / G-CAVEAT (BAR 7):')
    # ### ### **THIS ARM READS WHAT THE TOOL PRINTS, NOT WHAT ITS SOURCE CONTAINS.** ### The first
    # ### version grepped the source for the false sentence and FAILED -- because the correction's own
    # ### comment ### **QUOTES THE FALSE SENTENCE TO SAY IT WAS FALSE.** ### That is `b348`'s
    # ### use-and-mention species, committed by an arm written to catch a stale sentence. ### The
    # ### tool's own run record is the right surface: ### **A SENTENCE NOBODY PRINTS IS NOT A SENTENCE
    # ### ### THE RECORD CARRIES.**
    hkrun = d('b373_hooks.txt')
    hk = io.open(hkrun, encoding='utf-8', errors='replace').read() if os.path.exists(hkrun) else ''
    i1 = bool(hk) and 'No `.gitattributes` pins it' not in hk
    i2 = 'NOW PINS `eol=lf` IN EVERY ROSTERED REPOSITORY' in hk
    i3 = 'THIS ARM STILL WOULD NOT' in hk and 'EOL-normalised' in hk
    i4 = 'NOT WHAT IS ON A DISK TODAY' in hk
    touched = [p for p in ('tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
                           'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
                           'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
                           'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
                           'tools/b363_span.py', 'tools/git-hooks/pre-push',
                           'tools/b371_inventory.py', 'tools/b372_batch.py')
               if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    i5 = set(touched) <= LICENSED
    gi = i1 and i2 and i3 and i4 and i5
    print('    the false sentence is gone : %s ; the true one is there : %s' % (i1, i2))
    print('    ### **AND THE CAVEAT SURVIVES** : %s / %s' % (i3, i4))
    print('    owner instruments modified : %s ; all licensed : %s' % (touched or 'none', i5))
    print('    %s' % ('PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-INSTRUMENT/G-CAVEAT')

    print(chr(10) + '  G-NOCHECK / G-NOBUILD / G-NOLEAN:')
    src2 = ' '.join(strip_prose(t(x)) for x in ('b373_pins.py', 'b373_status.py'))
    k1 = 'lake' not in src2 and 'AllPrints' not in src2
    k2 = 'ls-tree' not in src2 and 'show' not in src2.replace('git show HEAD', '')
    k3 = not [x for x in git(SIDE, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    k4 = not [x for x in git(KER, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    k5 = not [x for x in git(SK, 'status', '--porcelain').split(chr(10)) if x.strip()]
    gk = k1 and k3 and k4 and k5
    print('    no build invocation in stripped sources : %s' % k1)
    print('    ### **NO `.lean` FILE IS DIRTY IN ANY KERNEL** : %s %s ### ; SIDE-kernel untouched : %s'
          % (k3, k4, k5))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-NOCHECK/G-NOBUILD/G-NOLEAN')

    print(chr(10) + '  G-CLOSED / G-KILLFILE:')
    q1 = Q['items'] == Q['closed'] + Q['standing']
    q2 = all(m.get('killing_file') and m.get('exists') and m.get('carries')
             for m in Q['marks'] if m['disposition'] == 'CLOSE')
    badq = []
    for m in Q['marks']:
        if m['disposition'] != 'CLOSE':
            continue
        p = d(m['killing_file'])
        if not os.path.exists(p) or GN.norm(m['sentence']) not in GN.norm(
                io.open(p, encoding='utf-8', errors='replace').read()):
            badq.append(m['killing_file'])
    q3 = not badq
    q4 = all(m.get('why') for m in Q['marks'] if m['disposition'] == 'STAND')
    gq = q1 and q2 and q3 and q4
    print('    the dispositions partition the desk : %s (%d = %d + %d)'
          % (q1, Q['items'], Q['closed'], Q['standing']))
    print('    ### **EVERY KILLING FILE RE-READ HERE** : %s %s' % (q3, badq or ''))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-CLOSED/G-KILLFILE')

    print(chr(10) + '  G-TRAIL ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['appended_only'] and F['committed_prefix_intact'] and F['prior_present']
    t4 = 'None' not in trails.split(TRAIL_MARK)[-1]
    gt = t1 and t2 and t3 and t4
    print('    the mark appears once : %s ; blob is a true prefix : %s ; append-only : %s' % (t1, t2, t3))
    print('    ### **NO UNFILLED PLACEHOLDER IN THE APPENDED BLOCK** : %s' % t4)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rws) == 1 and 'A RULE CAN OUTRUN THE RECORD' in rws[0]
            and 'NO PIN WAS WRITTEN' in rws[0] and 'NO GRADE WAS MOVED' in rws[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rws) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW')

    print(chr(10) + '  G-KEY / G-NOTCHECKED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : rule-outruns-record returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the pins are added', 'the grades are corrected', 'the rows are checked',
               'the archive is updated'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = ('IT WROTE NO PIN' in idx and 'NO GRADE WAS MOVED BY THIS SEAT' in idx)
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; four overreadings NO KEY after : %s ; run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY SAYS NO PIN WAS WRITTEN AND NO GRADE MOVED** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTCHECKED')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (P, S, Q, F))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    go2 = o1 and stampm and o3 and o4 and o5 and o6
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s ; gate CLEAR : %s'
          % (o4, o5, o6))
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b373_hooks_after.txt'), d('b373_mirror.txt')
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
    checks = [
        ('rows walked %d' % P['rows'], ('`%d` rows' % P['rows']) in bank),
        ('located act %d' % P['located_act'],
         ('`%d` of `%d` rows have a locatable writing act' % (P['located_act'], P['rows'])) in bank),
        ('not located %d' % P['act_not_located'], ('`%d` DO NOT' % P['act_not_located']) in bf),
        ('pinnable %d' % P['pinnable'], ('`%d` ROWS WERE PINNABLE' % P['pinnable']) in bf),
        ('pins written 0', 'NO PIN WAS WRITTEN TO ANY ROW' in bf),
        ('equals a head %d' % P['equals_a_head'], str(P['equals_a_head']) in bank),
        ('status defect %d' % S['defect'], ('`%d` ROWS IN' % S['defect']) in bf),
        ('status corrected %d' % S['corrected'], str(S['corrected']) in bank),
        ('rows scanned %d' % S['rows_scanned'], str(S['rows_scanned']) in bank),
        ('desk items %d' % Q['items'], ('`%d` SWEPT' % Q['items']) in bf),
        ('closed %d' % Q['closed'], ('`%d` CLOSED' % Q['closed']) in bf),
        ('row %s' % ROWNUM, re.search(r'row to append : (\d+)',
                                      io.open(CORR, encoding='utf-8').read()).group(1) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on pins run', P['run_file'] in bank),
        ('the relied-on status run', S['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('pins', P), ('status', S), ('desk', Q), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-28s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                              jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b373_') and x.endswith('.py')))
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
    DECLARED = {
        'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
        'the located span': 'the span is located by content and only then indexed.',
        'the oldest commit': 'it takes `[-1]` of a HISTORY LIST -- the oldest commit, which is what '
                             '`introduced it` means; not an address in a document.',
    }

    def which(code):
        if 'commits[-1]' in code or 'wide[-1]' in code:
            return 'the oldest commit'
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
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b373' not in x and x.strip() != 'tools/banked_index.py'
              and x.strip() not in LICENSED]
    ppstat = [x for x in git(PP, 'status', '--porcelain').split(chr(10))
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() not in ('OPEN_TRAILS.md',)]
    gse = [x for x in git(SIDE, 'status', '--porcelain').split(chr(10))
           if x.strip() and x[3:].strip() not in ('CORRESPONDENCE.md',)]
    kse = [x for x in git(KER, 'status', '--porcelain').split(chr(10))
           if x.strip() and 'b304-backup' not in x]
    gne = (not others and not ppbad and not gse and not kse and k5)
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    papers paths beyond the trail : %s' % (ppbad or 'none'))
    print('    construction-kernel paths beyond the row : %s' % (gse or 'none'))
    print('    exclusion-kernel paths : %s ### ; SIDE-kernel untouched : %s' % (kse or 'none', k5))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b373_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b373_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the record's own documents"),
        (d(P['run_file']), "the pins run carries the rows' own text and the banks' own refs"),
        (d(S['run_file']), "the status run carries the rows' own text"),
        (d(Q['run_file']), "the desk run carries the items' own sentences"),
        (d(F['run_file']), 'the filing carries the closures and the routing'),
        (t('b373_status.py'), "ITS CLASSIFIED SET IS THE KERNEL'S OWN RETIRED NAMES"),
        (t('b373_pins.py'), "ITS KERNEL NAMES ARE DISCOVERED FROM THE DISK"),
        (d('b373_hooks.txt'), "the exerciser's own log"),
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

    marker = '# ### THE PINS SOURCED FROM THE WRITING ACT, AND THE STATUS COLUMN LISTED (b373).'
    nxt = '# ### THE EOL PIN, THE README FIGURES, THE FIRST BATCH OF ROW CHECKS (b372).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b373_stem_'), 'blk.txt')
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
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
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

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b373_hedge_')
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
