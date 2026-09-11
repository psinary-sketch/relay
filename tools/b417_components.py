# -*- coding: utf-8 -*-
"""b417_components.py -- THE FIVE COMPONENTS AND THE TWO ADDITIONS.

### ### **THE WRITES HAPPEN BEHIND THEIR OWN FLAGS, IN THE ORDER THE FACE FIXES:** ### `--snapshot`
### runs the repaired tool against a captured snapshot, and ### **`--live` REFUSES UNTIL A SNAPSHOT
### ### RECORD EXISTS**; `--sweep` applies the backup rule at (E); `--place` adds `(R33)`'s clause to
### the Reader's head; `--reads` prints every candidate line the hand-reads turn on. ### Folded here
### rather than written as new act-tools because the locked write list names ### **SIX** ### relay
### tools, and a file of a KIND the write list does not name is a breach.

### ### **THE TWO SUBJECTS ARE KEPT APART IN THIS FILE AS IN THE ACT:** ### the slots (Components
### 1, 2 and 4, and Addition Two) and the fifteen (Component 5 and `(R33)`) are reported in
### separate sections and no line of this record joins them.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import repair_snapshot as RS   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
FX = os.path.join('D:', os.sep, 'SIDE-effects')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
FA = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic')
READER = os.path.join(PP, 'heritage', 'PRIME_CORE_READER.md')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
TOOL = os.path.join('tools', 'b369_hygiene.py')
NL = chr(10)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def read(p):
    return rb(p).decode('utf-8', 'replace')


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


def put(name, lines):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').strip()


# =============================================================================================
# ### COMPONENT 3, PHASE ONE. ### **THE HARNESS'S OWN FIXTURES FIRST; A FAILED FIXTURE REFUSES.**
# =============================================================================================
def run_snapshot():
    R = ['=' * 100, 'b417 COMPONENT 3, PHASE ONE -- THE REPAIRED TOOL AGAINST A CAPTURED SNAPSHOT.',
         '=' * 100, '  run at (UTC) : %s' % utc()]
    ok = RS.self_test(verbose=False)
    R.append('  ### the harness`s fixtures, both polarities, before it is trusted : %s'
             % ('PASS' if ok else '### FAIL'))
    if not ok:
        R.append('  ### ### **REFUSED -- A HARNESS THAT FAILS ITS OWN FIXTURES MEASURES NOTHING.**')
        put('b417_snapshot.txt', R)
        return 2
    res = RS.snapshot(TOOL)
    R += RS.report(res)
    R.append('')
    R.append('  ### **WHAT THE TOOL ITSELF SAID, FROM ITS OWN VERDICT LINES (A2):**')
    for ln in res['stdout'].splitlines():
        if any(k in ln for k in ('COMPONENT 2 :', 'REPOS FAILING', 'BYTE-IDENTICAL TO THE TRACKED',
                                 'wording pairs applied', ': ALREADY PRESENT', 'SKIPPED')):
            R.append('      | %s' % ln.rstrip()[:118])
    R.append('  FileNotFoundError in the snapshot run : %s' % ('FileNotFoundError' in res['stderr']))
    R.append('=' * 100)
    put('b417_snapshot.txt', R)
    json.dump({k: v for k, v in res.items() if k not in ('stdout', 'stderr')},
              io.open(os.path.join(D, 'b417_snapshot.json'), 'w', encoding='utf-8'), indent=1)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### COMPONENT 3, PHASE TWO. ### **REFUSES WITHOUT A SNAPSHOT RECORD ON DISK.**
# =============================================================================================
def run_live():
    snap = read(os.path.join(D, 'b417_snapshot.txt'))
    R = ['=' * 100, 'b417 COMPONENT 3, PHASE TWO -- THE REPAIRED TOOL, LIVE, ITS WRITES CAPTURED.',
         '=' * 100, '  run at (UTC) : %s' % utc()]
    if '### PHASE : SNAPSHOT' not in snap:
        R.append('  ### ### **REFUSED -- NO SNAPSHOT RECORD. THE LIVE RUN DOES NOT COME FIRST.**')
        put('b417_live.txt', R)
        print(NL.join(R))
        return 2
    R.append('  the snapshot record precedes this run : True (%s)'
             % (re.search(r'run at \(UTC\) : (\S+)', snap).group(1)))
    res = RS.live(TOOL)
    R += RS.report(res)
    R.append('')
    R.append('  ### **WHAT THE TOOL ITSELF SAID, FROM ITS OWN VERDICT LINES (A2):**')
    for ln in res['stdout'].splitlines():
        if any(k in ln for k in ('COMPONENT 2 :', 'REPOS FAILING', 'BYTE-IDENTICAL TO THE TRACKED',
                                 'wording pairs applied', ': ALREADY PRESENT', 'SKIPPED')):
            R.append('      | %s' % ln.rstrip()[:118])
    R.append('  FileNotFoundError in the live run : %s' % ('FileNotFoundError' in res['stderr']))
    R.append('=' * 100)
    put('b417_live.txt', R)
    json.dump({k: v for k, v in res.items() if k not in ('stdout', 'stderr')},
              io.open(os.path.join(D, 'b417_live.json'), 'w', encoding='utf-8'), indent=1)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### THE BACKUP RULE AT (E). ### **SWEPT ONLY IF EVERY BACKUP'S BYTES ARE IN AN OBJECT STORE.**
# =============================================================================================
def blob_ids(b):
    lf = b.replace(b'\r\n', b'\n')
    return (hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest(),
            hashlib.sha1(b'blob %d\0' % len(lf) + lf).hexdigest())


def run_sweep():
    gh = os.path.join(FX, '.githooks')
    baks = sorted(f for f in os.listdir(gh) if '.b304-backup' in f)
    R = ['=' * 100, 'b417 COMPONENT 3 -- THE RESIDUE BACKUPS IN SIDE-effects, BY THE RULE AT (E).',
         '=' * 100, '  run at (UTC) : %s' % utc(), '  backups found : %d' % len(baks)]
    present = {}
    for f in baks:
        b = rb(os.path.join(gh, f))
        ids = blob_ids(b)
        where = [nm for nm, repo in (('SIDE-effects', FX), ('relay', ROOT))
                 if any(git(repo, 'cat-file', '-e', i)[0] == 0 for i in ids)]
        tracked = git(FX, 'ls-files', '--error-unmatch', '.githooks/' + f)[0] == 0
        present[f] = bool(where) and not tracked
        R.append('      %-26s %5d bytes  sha256 %s  blob %s  in : %s  tracked : %s'
                 % (f, len(b), hashlib.sha256(b).hexdigest()[:16], ids[1][:12],
                    ', '.join(where) or '### NONE', tracked))
    rule_ok = bool(baks) and all(present.values())
    R.append('  ### ### **EVERY BACKUP`S BYTES PRESENT IN AN OBJECT STORE, AND NONE TRACKED : %s**' % rule_ok)
    swept = []
    if rule_ok:
        for f in baks:
            os.remove(os.path.join(gh, f))
            swept.append(f)
        R.append('  ### ### **SWEPT : %d** -- %s' % (len(swept), ', '.join(swept)))
        R.append('  still present after the sweep : %d' % len([f for f in swept if os.path.exists(os.path.join(gh, f))]))
        R.append('  ### content lost : 0 -- every byte swept is a blob in a repository`s store, shown above.')
    else:
        R.append('  ### ### **NAMED AND LEFT.** ### The rule does not permit the sweep.')
    st = git(FX, 'status', '--porcelain')[1]
    R.append('  SIDE-effects status after : %s' % (st.replace(NL, ' ; ') or 'clean'))
    R.append('=' * 100)
    put('b417_sweep.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### (R33). ### **ONE CLAUSE ADDED BELOW THE THREE; THE THREE AND THE BODY UNTOUCHED.**
# =============================================================================================
ANCHOR = '>    not a refutation.**\n'
CLAUSE = ('>\n'
          '> **AND A FOURTH, per (R33), added b417 (2026-09-11).**\n'
          '> 4. **Its arithmetic-desert sentence is false.** It says the jump primes are separated\n'
          '>    from the consecutive sequence *"by arithmetic deserts where no sum of powers yields a\n'
          '>    prime"*; sums `2^a + 3^b` that are prime lie inside that stretch — among them the\n'
          '>    seven below one hundred that `P` excludes: 43, 59, 67, 73, 83, 89 and 97. **The\n'
          '>    Reader\'s own predictions section names two of them**, 43 and 67, as gap elements:\n'
          '>    *"Dark matter particle masses may involve gap elements (23, 43, 47, 67, ...)"*.\n')


def run_place():
    R = ['=' * 100, 'b417 (R33) -- THE READER`S HEAD NOTE GROWS A FOURTH CLAUSE.', '=' * 100,
         '  run at (UTC) : %s' % utc()]
    pb, cb = rb(READER), rb(CANON)
    hl = pb.find(b'# PRIME CORE')
    head, body = pb[:hl].decode('utf-8'), pb[hl:]
    R.append('  body identical to the canonical copy BEFORE : %s' % (body == cb))
    if ANCHOR not in head or head.count(ANCHOR) != 1:
        R.append('  ### ### **REFUSED -- the anchor is not in the head exactly once.**')
        put('b417_place.txt', R)
        return 2
    if '**AND A FOURTH, per (R33)' in head:
        R.append('  ### the clause is already present -- nothing written.')
        put('b417_place.txt', R)
        return 0
    new_head = head.replace(ANCHOR, ANCHOR + CLAUSE, 1)
    out = new_head.encode('utf-8') + body
    open(READER + '.tmp', 'wb').write(out)
    os.replace(READER + '.tmp', READER)
    pa = rb(READER)
    hl2 = pa.find(b'# PRIME CORE')
    body2, head2 = pa[hl2:], pa[:hl2].decode('utf-8')
    R.append('  head bytes %d -> %d ; body bytes %d -> %d' % (len(head.encode()), len(head2.encode()),
                                                           len(body), len(body2)))
    R.append('  body sha256 after : %s' % hashlib.sha256(body2).hexdigest())
    R.append('  canonical sha256  : %s' % hashlib.sha256(cb).hexdigest())
    R.append('  ### ### **BODY BYTE-IDENTICAL TO THE CANONICAL COPY AFTER THE WRITE : %s**' % (body2 == cb))
    R.append('  ### ### **BYTES OF THE BODY EDITED : %d**' % (0 if body2 == cb else -1))
    prior = [head[head.find('> 1.'):head.find('> 2.')], head[head.find('> 2.'):head.find('> 3.')],
             head[head.find('> 3.'):head.find(ANCHOR) + len(ANCHOR)]]
    R.append('  b416`s three clauses present byte-for-byte after : %s' % all(p in head2 for p in prior))
    R.append('  the old head is the new head with exactly the clause removed : %s'
             % (head2.replace(CLAUSE, '', 1) == head))
    R.append('  clauses numbered in the head now : %d' % len(re.findall(r'(?m)^> \d\.', head2)))
    seven = [43, 59, 67, 73, 83, 89, 97]
    R.append('  the seven named in the clause : %s' % all(str(v) in CLAUSE for v in seven))
    R.append('  primes beyond the seven named in the clause (113, 131) : %s'
             % any(x in CLAUSE for x in ('113', '131')))
    R.append('  the predictions section cited, naming 43 and 67 : %s'
             % ('predictions section' in CLAUSE and '43 and 67' in CLAUSE))
    R.append('')
    R.append('  ### THE CLAUSE, EXACTLY AS WRITTEN:')
    R += ['      |%s' % ln for ln in CLAUSE.rstrip(NL).split(NL)]
    R.append('=' * 100)
    put('b417_place.txt', R)
    print(NL.join(R))
    return 0 if body2 == cb else 1


# =============================================================================================
# ### THE READS THE HAND-READS TURN ON. ### Every candidate line printed; nothing is marked here.
# =============================================================================================
def run_reads():
    ext = read(os.path.join(D, 'b417_extract.txt'))
    R = ['=' * 100, 'b417 -- THE CANDIDATE LINES, PRINTED BEFORE ANY MARK IS SET.', '=' * 100]
    R.append('### (i) COMPONENT 4 -- FOR EACH CAVEAT, THE ACTS NAMING IT AFTER ITS WRITER, AND THEIR LINES.')
    recs = sorted(f for f in os.listdir(D) if re.match(r'b\d+_.*\.txt$', f)
                  and not f.startswith(('b416_', 'b417_')))
    for m in re.finditer(r"\[\s*(\d+)\] (\S+)\s+line (\d+)\s+anchor '([^']*)'?\s+acts naming it : (\d+)  ?(.*)", ext):
        idx, f, ln, anc, n, acts = m.groups()
        acts = [a.strip() for a in acts.split(',') if a.strip()]
        R.append('')
        R.append('  [%s] %s line %s   anchor %r   acts %s' % (idx, f, ln, anc, acts))
        if not acts:
            R.append('      (no act record names it)')
            continue
        writer = acts[0]
        R.append('      writer (earliest act naming it) : %s' % writer)
        for a in acts[1:]:
            for rf in recs:
                if not rf.startswith(a + '_'):
                    continue
                src = read(os.path.join(D, rf))
                hits = [x.strip() for x in src.splitlines() if anc in x]
                for h in hits[:3]:
                    R.append('      %-6s %-40s %s' % (a, rf[:40], h[:150]))
    R.append('')
    R.append('### (ii) COMPONENT 1 -- THE SECOND SHAPE`S RESIDUE, EVERY PARAGRAPH IN FULL.')
    WU = re.compile(r'universal', re.I)
    WN = re.compile(r'n₂|n_2|n_\{2\}|\bn2\b|Chevalley|transformation count|three-level covering', re.I)
    for rel in ('phase1.5/structural/AT_REST.md', 'phase2/formation/CAPACITY.md',
                'phase2/formation/UNIVERSALITY.md',
                'clusters/IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19.md',
                'meta/W1_REVIEW_DIGEST.md', 'phase2/physics/YANG_MILLS_MONOGRAPH.md',
                'phase2/quantum/ARITHMETIC_ORIGIN_QECC.md'):
        src = read(os.path.join(PP, rel.replace('/', os.sep)))
        paras = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', src)
                 if WU.search(p) and WN.search(p)]
        R.append('')
        R.append('  %s -- %d paragraph(s)' % (rel, len(paras)))
        for p in paras:
            # ### **REPAIRED AFTER RUN 1**: the first version sliced at fixed widths and broke words
            # ### mid-token, against the face's BAR 11; run 1 is kept as `b417_reads_run1.txt`.
            for seg in wrap(p[:900], 110):
                R.append('      %s' % seg)
            R.append('      ----')
    R.append('=' * 100)
    put('b417_reads.txt', R)
    print(NL.join(R))
    return 0


# =============================================================================================
# ### THE HAND-READS, SET AFTER `b417_reads.txt` WAS PRINTED, EACH WITH THE WORDS IT TURNS ON.
# =============================================================================================
# ### COMPONENT 1 -- THE SECOND SHAPE'S RESIDUE, SCORED BY THE (U1) RULE AT THE FACE'S (C).
CITERS = [
    ('phase2/physics/MATTER_AS_ARITHMETIC.md', 'U1',
     'the owner: *Three of four formation components are universal across IDS-amenable systems*'),
    ('phase1.5/structural/AT_REST.md', 'U1',
     '*We proved three of four components universal*; and *n2 = 3 universally. For any IDS-amenable '
     'system WITH CONNECTED REDUCTIVE SYMMETRY GROUP G* -- the hypothesis written inline'),
    ('phase2/formation/UNIVERSALITY.md', 'U2',
     '*No component depends on K* -- constant across number fields, inside class A; and it gives '
     'n2 = 3 *by Ostrowski*, not by Chevalley-Steinberg'),
    ('clusters/IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19.md', 'U3',
     '*the formation total is universal ... for every Dedekind zeta function*'),
    ('phase2/quantum/ARITHMETIC_ORIGIN_QECC.md', 'U2',
     'the tuple (2, 3, 2, 0) for xi, cited to FORMATION_UNIVERSALITY_v3'),
    ('phase2/formation/CAPACITY.md', 'MENTION',
     '*the system`s universal property* -- a property P of one system, not a component claim'),
    ('meta/W1_REVIEW_DIGEST.md', 'MENTION', 'a review table; the words meet by accident'),
    ('phase2/physics/YANG_MILLS_MONOGRAPH.md', 'MENTION',
     'its own stage table (3, 3, 2, 0) and *universal interfaces are spectrally inert* -- the n4 '
     'theorem`s phrase, not a claim that any component is constant across classes'),
]
# ### COMPONENT 4 -- THE PREDICATE AT THE FACE'S (F), APPLIED TO EACH CANDIDATE LINE PRINTED.
MARKS = [
    (1, 'UNTESTED', 'SCOPE DISCLAIMER', 'named only by its writer b298'),
    (2, 'TESTED', 'CONDITION (primality)', 'b414 compiled composite_bases_keep_the_identity and '
     'those_bases_are_composite: the identity decided at 4, 8, 9 -- inputs outside the primes'),
    (3, 'UNTESTED', 'CONDITION (the trace identified with a signed count)', 'b308, b310, b311, b329, '
     'b413 quote or APPLY it; b311`s run carries no line checking it against an independent trace'),
    (4, 'UNTESTED', 'LIBRARY LEMMA (general; carries propext)', 'named only by its writer b329'),
    (5, 'UNTESTED', 'LIBRARY FORM (coprimality of a unit)', 'the widened anchor`s earliest hit b10 is '
     'an unrelated act; b331`s lines DESCRIBE the seal`s witnessed-equation form, not a test'),
    (6, 'UNTESTED', 'LIBRARY FORM (proved with its witness for every p)', 'named only by its writer b329'),
    (7, 'UNTESTED', 'CITED CONTRAST (one field, h = 3)', 'b226 and b227 re-measure axioms, nothing more'),
    (8, 'UNTESTED', 'SCOPE DISCLAIMER', 'named only by its writer b304'),
    (9, 'UNTESTED', 'SCOPE DISCLAIMER', 'named only by its writer b302'),
    (10, 'UNTESTED', 'READING (the bank`s, at the listed cells)', 'b329 quotes the cell list only'),
    (11, 'UNTESTED', 'CONDITION (restates T1.4; evidence 4 .. 49)', 'b415 names the module it built'),
    (12, 'UNTESTED', 'DERIVATION (b310`s, at the listed cells)', 'b329 quotes fragments only'),
    (13, 'UNTESTED', 'SCOPE DISCLAIMER', 'named only by its writer b303'),
]

L = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def omega(t):
    return Fraction(t[0] ** t[2], t[1] ** (t[0] + t[2]))


def main():
    ext = read(os.path.join(D, 'b417_extract.txt'))
    snap = read(os.path.join(D, 'b417_snapshot.txt'))
    live = read(os.path.join(D, 'b417_live.txt'))
    sweep = read(os.path.join(D, 'b417_sweep.txt'))
    place = read(os.path.join(D, 'b417_place.txt'))
    fails = []
    for nm, txt in (('extract', ext), ('snapshot', snap), ('live', live), ('sweep', sweep),
                    ('place', place)):
        if not txt:
            fails.append('record absent: %s' % nm)
    cls = read(os.path.join(FA, 'Classes.lean'))
    tup = {m[0]: tuple(int(x) for x in m[1:]) for m in
           re.findall(r'def (class[ABCD]) : FormationTuple := .(\d+), (\d+), (\d+), (\d+).', cls)}
    RA = dict(tup)
    RA['classB'] = (tup['classB'][0], 3, tup['classB'][2], 0)
    RA['classD'] = (tup['classD'][0], 3, tup['classD'][2], 0)

    rule('=')
    say('b417_components.py -- THE CONTRADICTION PUT TO ITS OWNER, AND THE SECOND TOOL CLEARED.')
    rule('=')
    say()
    rule('#')
    say('### PART ONE -- THE SLOTS. ### Components 1, 2 and 4, (R34) and Addition Two.')
    rule('#')
    say()
    rule()
    say('### COMPONENT 1 -- THE DEFECT REPORT, SIDE BY SIDE, FOR THE AUTHOR TO RULE ON.')
    rule()
    say('  %-12s %-52s %s' % ('HALF', 'WHAT IT SAYS, IN ITS OWN WORDS', 'WHERE'))
    say('  %-12s %-52s %s' % ('SENTENCE', 'Three of four formation components are universal', 'MATTER_AS_ARITHMETIC'))
    say('  %-12s %-52s %s' % ('', 'across IDS-amenable systems: n2 = 3 by Chevalley-', 'line 14 (abstract)'))
    say('  %-12s %-52s %s' % ('', 'Steinberg, n3 = 2 by bipartite complex analysis,', 'and line 27 (section I)'))
    say('  %-12s %-52s %s' % ('', 'n4 = 0 by Schur`s lemma.', ''))
    say('  %-12s %-52s %s' % ('TUPLES', 'classB := (3, 2, 2, 0) ; classD := (2, 2, 2, 0)', 'Classes.lean, and'))
    say('  %-12s %-52s %s' % ('', 'n2 = 2 in both, against the sentence`s universal 3', 'MATTER lines 40, 42'))
    say()
    say('  ### ### **THE OWNER`S DOCUMENT CARRIES BOTH HALVES**, eleven lines apart in section I and')
    say('  ### inside one paragraph in the abstract, which states the universality and then lists 9/32')
    say('  ### and 1/4 -- the ratios of tuples whose second component is 2.')
    say()
    say('  ### **WHAT EACH CHANGE WOULD COST, FROM THE ARITHMETIC BELOW AND THE COUNTS ABOVE:**')
    say('    ### to change THE SENTENCE (reading b): its two occurrences in MATTER, and the two AT_REST')
    say('    ### paragraphs that restate it. ### **0 kernel figures move. 0 ratios move.**')
    say('    ### to change THE TUPLES (reading a): two declarations in Classes.lean, five figure theorems,')
    say('    ### one distinctness theorem that becomes false, two rows of the owner`s ratio table, the')
    say('    ### abstract`s 9/32 and 1/4 and its sigma range, and the five live documents that cite the')
    say('    ### disagreeing tuples.')
    say()
    say('  ### **WHO CITES THE SENTENCE -- TWO SHAPES, THE RESIDUE HAND-READ BY THE (U1) RULE:**')
    m1 = re.search(r'LIVE DOCUMENTS CITING THE SENTENCE AT ALL : (\d+)', ext)
    m2 = re.search(r'paragraphs : (\d+) ; documents : (\d+)', ext)
    say('      first shape (the sentence`s own words) : %s document(s)' % (m1.group(1) if m1 else '?'))
    say('      second shape (universal + the second component) : %s paragraph(s) in %s document(s)'
        % ((m2.group(1), m2.group(2)) if m2 else ('?', '?')))
    for rel, kind, why in CITERS:
        say('      %-8s %s' % (kind, rel))
        say('               %s' % why)
    u1 = [r for r, k, _w in CITERS if k == 'U1']
    say('  ### ### **LIVE DOCUMENTS CITING THE SENTENCE (U1) : %d** -- %s' % (len(u1), ', '.join(u1)))
    tonly = re.findall(r'(?m)^      (phase[\w./-]+\.md)$', ext.split('CITING THE DISAGREEING TUPLES AND NOT')[1]
                       .split('LIVE DOCUMENTS CITING THE SENTENCE AT ALL')[0]) if 'CITING THE DISAGREEING' in ext else []
    say('  ### ### **LIVE DOCUMENTS CITING THE DISAGREEING TUPLES AND NOT THE SENTENCE : %d**' % len(tonly))
    for r in tonly:
        say('      %s' % r)
    say('  ### ### **SO THE DOWNSTREAM CITES THE TUPLES MORE THAN THE SENTENCE** -- counted, not ruled on.')
    say('  ### **UNDER (R34) THIS SEAT DOES NOT SAY WHICH HALF IS WRONG. THE AUTHOR RULES.**')
    say()
    rule()
    say('### COMPONENT 2 -- THE RATIO AT THE FOUR TUPLES, AGAINST THE KERNEL`S OWN HEADER.')
    rule()
    i, j = ext.find('  class   tuple'), ext.find('  distinct pairs')
    for ln in ext[i:j].splitlines():
        say('  %s' % ln.rstrip())
    say()
    for k in ('B', 'D'):
        t = tup['class' + k]
        alt = (t[0], 3, t[2], 0)
        say('  class %s : n2 = 2 gives %s ; n2 = 3 gives %s ; ### **%s**'
            % (k, omega(t), omega(alt), 'LOAD-BEARING' if omega(t) != omega(alt) else 'incidental'))
    say('  ### ### **`n2 = 2` IS LOAD-BEARING FOR BOTH B AND D**: change it and each ratio moves.')
    say()
    rule()
    say('### (R34) -- WHAT EACH RESOLUTION WOULD MOVE, FROM ARITHMETIC.')
    rule()
    i, j = ext.find('  reading (a) tuples'), ext.find('### READ 9 --')
    for ln in ext[i:j].splitlines():
        if ln.strip() and not ln.startswith('---'):
            say('  %s' % ln.rstrip())
    say()
    say('  ### **AND IN THE OWNER`S OWN DOCUMENT:** the abstract`s *9/32 (Gravitational)* and *1/4')
    say('  ### (Information)* and its range *excluding the others by 18.6 sigma to 351 sigma*; the section II')
    say('  ### ratio table`s rows B and D. ### Under reading (a) all of them move; D lands on 4/81 at 0.13')
    say('  ### sigma, so *selecting the Arithmetic class* no longer selects one class. ### Under reading (b)')
    say('  ### ### **NO FIGURE MOVES ANYWHERE** -- only the sentence`s scope changes.')
    wa = omega(RA['classA'])
    say('  ### ### **CLASS A`S VALUE : %s UNDER READING (a), %s UNDER READING (b). ### UNMOVED UNDER BOTH.**'
        % (wa, omega(tup['classA'])))
    say()
    rule()
    say('### ADDITION TWO -- THE TWO READINGS PRICED, FOR THE RULING. ### NEITHER ADOPTED.')
    rule()
    say('  ### **READING (a) -- THE SENTENCE IS RIGHT.**')
    say('      B %s -> %s ; D %s -> %s' % (tup['classB'], RA['classB'], tup['classD'], RA['classD']))
    say('      ratio pairs : B (9, 32) -> (9, 243) ; D (4, 16) -> (4, 81)')
    ndist = len(set(RA.values()))
    say('      distinct tuples among the four named classes : 4 -> ### **%d**' % ndist)
    say('      ### ### **B BECOMES C AND D BECOMES A.** ### The ferry`s parenthetical said *two named')
    say('      classes become one*; ### **THE ARITHMETIC SAYS TWO COLLISIONS: FOUR NAMED CLASSES BECOME')
    say('      ### TWO DISTINCT TUPLES.** ### Both are printed; the arithmetic`s is the count.')
    say('      ### **WHAT THE CORPUS LOSES:** Gravitational and Information as distinct predictions; the')
    say('      ### Planck discrimination`s exclusion of D (D would sit on A at 0.13 sigma); the kernel`s')
    say('      ### classA_distinct_from_classD, which would be false and could not compile.')
    say()
    say('  ### **READING (b) -- THE TUPLES ARE RIGHT AND THE SENTENCE OVER-CLAIMS.**')
    say('      ### What *universal* would have to be weakened to, from the theorems` own hypothesis lines:')
    say('      *Connected reductive symmetry groups admit exactly three-level covering towers* -- MATTER`s')
    say('      n2 theorem; ### and AT_REST already writes the weakened form: *For any IDS-amenable system')
    say('      with connected reductive symmetry group G*. ### **SO THE WEAKENING IS: n2 = 3 FOR SYSTEMS')
    say('      ### WHOSE SYMMETRY GROUP IS CONNECTED REDUCTIVE, NOT ACROSS IDS-AMENABLE SYSTEMS.**')
    rs = re.search(r'B or D substrate : ### \*\*(\d+)\*\*', ext)
    say('      live paragraphs saying whether B`s or D`s substrate carries such a group : %s'
        % (rs.group(1) if rs else '?'))
    say('      ### ### **THE CORPUS DOES NOT SAY**, so reading (b) leaves B and D`s n2 = 2 stipulated.')
    say('      ### **WHICH n4 DOCUMENTS ALSO ASSERT THE UNIVERSALITY (U1):**')
    i, j = ext.find('  MATTER_AS_ARITHMETIC         U1'), ext.find('  COMPLEX_ANALYSIS`s U2')
    for ln in ext[i:j].splitlines():
        if ln.strip():
            say('    %s' % ln.rstrip())
    say('      ### only MATTER asserts (U1); COMPLEX_ANALYSIS asserts (U2) and (U3); BSD asserts none.')
    say('  ### ### **NEITHER READING IS ADOPTED. THE AUTHOR RULES.**')
    say()
    say('  ### **AND A SECOND DISAGREEMENT, OF ANOTHER KIND, REPORTED BESIDE IT AND NOT FOLDED IN:**')
    say('  ### COMPLEX_ANALYSIS and MATTER place the genetic code, Shannon`s system and Navier-Stokes at')
    say('  ### different tuples. ### ROUTED.')
    say()
    rule()
    say('### COMPONENT 4 -- THE Core/ CAVEATS, EACH MARKED UNDER THE PREDICATE AT THE FACE`S (F).')
    rule()
    cav = re.findall(r"\[\s*(\d+)\] (\S+)\s+line (\d+)", ext)
    say('  %-4s %-32s %-9s %-44s %s' % ('#', 'FILE, LINE', 'MARK', 'KIND', 'THE READ IT TURNS ON'))
    for (n, mark, kind, why) in MARKS:
        f, ln = next(((c[1], c[2]) for c in cav if int(c[0]) == n), ('?', '?'))
        say('  [%2d] %-32s %-9s %-44s' % (n, '%s:%s' % (f, ln), mark, kind[:44]))
        say('        %s' % why)
    nt = len([m for m in MARKS if m[1] == 'TESTED'])
    cond = [m for m in MARKS if m[2].startswith(('CONDITION', 'CITED', 'READING', 'DERIVATION'))]
    say('  ### ### **TESTED : %d. ### UNTESTED : %d.**' % (nt, len(MARKS) - nt))
    say('  ### ### **AND THE KIND BESIDE THE MARK, SO THE BINARY HIDES NOTHING:** %d of the caveats state a'
        % len(cond))
    say('  ### condition over a bounded evidence set; the rest are scope disclaimers or library forms with')
    say('  ### nothing to leave. ### **Of those that state one, %d has been tested outside its evidence.**'
        % len([m for m in cond if m[1] == 'TESTED']))
    say('  ### COUNTED AND MARKED, NOT GRADED.')
    say()
    rule()
    say('### THE EXPECTATIONS ABOUT THE SLOTS, EACH OVER ITS NAMED POPULATION (R26), PREMISE AND')
    say('### CONCLUSION APART (R27).')
    rule()
    say('**(N1)** over the live population of READ 3, by the (U1) rule')
    say('      *the universality sentence is the wrong half* -- ### **NOT SCORED BY THIS SEAT, UNDER (R34).')
    say('      ### IT IS THE AUTHOR`S.**')
    say('      *at least four live documents cite it* -- ### **REFUTED: %d** (%s).' % (len(u1), ', '.join(u1)))
    say('**(N2)** over classes B and D -- ### **MET: LOAD-BEARING FOR BOTH.**')
    say('**(N3)** over the caveats of READ 7, by the predicate at (F)')
    say('      *at most three have been tested outside their own evidence* -- ### **MET: %d.** ### And the' % nt)
    say('      premise is nearly vacuous: most of the population states no bounded condition to leave.')
    say('**(N4)** over the header`s pairs and READ 2`s arithmetic')
    say('      PREMISE -- *four distinct pairs only exist if the second component varies* -- ### **MET**: with n2')
    say('      held constant, n1 takes two values and n3, n4 none, so at most two pairs; the header prints four.')
    say('      CONCLUSION -- *so the header supports reading (b)* -- ### **NOT A SECOND WITNESS.** The header is')
    say('      computed from the same declarations: it is the tuples stated twice. It is consistent with (b)')
    say('      and inconsistent with (a) because it IS one half of the contradiction, and it cannot decide')
    say('      between the halves. ### **MET IN PREMISE / NOT MET IN CONCLUSION, UNDER (R27).**')
    say('**(N5)** over the documents arguing n4 named in READ 4, scored over (U1)')
    say('      *at least one asserts the sentence and cites no tuple* -- ### **REFUTED.** The only n4 document')
    say('      asserting (U1) is MATTER, and it cites all four tuples; the other two assert no (U1) at all.')
    say()

    rule('#')
    say('### PART TWO -- THE TOOLS. ### Component 3 and Addition One.')
    rule('#')
    say()
    for nm, txt in (('THE SNAPSHOT', snap), ('THE LIVE RUN', live), ('THE BACKUPS', sweep)):
        say('### %s' % nm)
        for ln in txt.splitlines():
            if ln.strip() and not ln.startswith('='):
                say('  %s' % ln.rstrip()[:118])
        say()
    # ### THE LIVE RECORD'S *STILL DIFFERING* FIGURE, RE-MEASURED THE WAY THE RESTORE WAS MADE.
    byteok = []
    for f in ('b369_hooks.txt', 'b369_hygiene.json'):
        blob = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/' + f], capture_output=True).stdout
        byteok.append(rb(os.path.join(D, f)) == blob)
    ms = re.search(r'FILES STILL DIFFERING AFTER THE RESTORE : (\d+)', live)
    say('### ### **THE LIVE RECORD SAYS %s STILL DIFFERING. ### BYTES AGAINST THE BLOB SAY %d.**'
        % (ms.group(1) if ms else '?', len([b for b in byteok if not b])))
    say('### The harness compared a restored data file by size and mtime, and a restore changes the mtime,')
    say('### so it reported every restored data file differing. ### **THE DEFECTIVE PREDICATE IS NAMED')
    say('### ### AND THE HARNESS REPAIRED** to compare bytes against the blob; the live record is kept as run.')
    say('### ### **A NEW INSTRUMENT IS A REPAIRED TOOL TOO** -- its masked defect surfaced on its first live use.')
    say()
    say('### THE REPAIRED TOOL`S OWN VERDICT, REPORTED AND NOT EDITED: ### **COMPONENT 2 : FAILED**, on')
    say('### predicates its own history dated -- its wording pairs were applied at b369 (0 of 2, 0 of 5 now),')
    say('### and its `installed` check reads SIDE-effects/.git/hooks/pre-push, a path no guard runs from')
    say('### since `core.hooksPath` names `.githooks`. ### Its printed label *tracked source : tools/git-hooks*')
    say('### is dated prose, named and not repaired: it stops nothing from running.')
    say()

    rule('#')
    say('### PART THREE -- THE FIFTEEN. ### Component 5 and (R33). A SEPARATE SUBJECT FROM PART ONE.')
    rule('#')
    say()
    i, j = ext.find('### READ 9 --'), ext.find('### READ 10 --')
    for ln in ext[i:j].splitlines():
        if ln.strip() and not ln.startswith('---') and not ln.startswith('###  READ'):
            say('  %s' % ln.rstrip()[:118])
    say()
    say('  ### ### **THE LIVE CARRIER ASSERTS THE DESERT IN ITS OWN WORDS, NOT THE READER`S** -- and its')
    say('  ### own sentence is sharper and false at one point: *No combination of powers yields 43, 47, or')
    say('  ### 53 directly*, where 43 = 2^4 + 3^3. ### ROUTED, NOT REPAIRED.')
    say()
    i, j = ext.find('### READ 10 --'), ext.find('### READ 11 --')
    for ln in ext[i:j].splitlines():
        if ln.strip() and not ln.startswith('---'):
            say('  %s' % ln.rstrip()[:118])
    say()
    say('### (R33) EXECUTED')
    for ln in place.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  %s' % ln.rstrip())
    say('  ### ### **THE STRETCH ALSO CARRIES 113 AND 131. ### THEY ARE IN THIS RECORD AND NOT IN THE')
    say('  ### ### CLAUSE**, which names the seven the ruling names and does not claim they are all.')
    say()
    rule()
    say('### THE COMPONENTS` OWN TALLY.')
    rule()
    say('  ### ### **RECORD FAILURES : %d**' % len(fails))
    for f in fails:
        say('      %s' % f)
    rule('=')
    io.open(os.path.join(D, 'b417_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    for flag, fn in (('--snapshot', run_snapshot), ('--live', run_live), ('--sweep', run_sweep),
                     ('--place', run_place), ('--reads', run_reads)):
        if flag in sys.argv:
            sys.exit(fn())
    sys.exit(main())
