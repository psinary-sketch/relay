# -*- coding: utf-8 -*-
"""b423_components.py -- THE (R37) QUESTION: b407'S AND b420'S READINGS OF HYPOTHESIS 1, EACH AGAINST §10.2.

### ### **NOBODY IS RE-VERDICTED.** ### Each reading is read as its bank states it, against the ruling's own words, with
### the definition the internal reading would take quoted from the record or its verified source, and scored
### CONFIRMED or MOVED with the deciding sentence quoted.
###   --read      the reading record, data/b423_r37_question.txt.
###   (no flag)   the report and the expectation, its two clauses apart.
"""
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
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
B407 = os.path.join(D, 'b407_the_barriers_own_instance.txt')
C4 = os.path.join(D, 'b420_c4_barrier.txt')
C2 = os.path.join(D, 'b421_c2_specification.txt')
B400 = os.path.join(D, 'b400_components_run2.txt')
QREC = os.path.join(D, 'b423_r37_question.txt')
NL = chr(10)
MISS = []

# ### THE SEARCH FOR A DOCUMENT HOLDING A SPECIFICATION OF THE TEST-FUNCTION STRUCTURE: every paragraph of a tracked
# ### PLACE-papers .md file naming *specification* beside the class, each hit hand-read and dispositioned by file.
HAND = {
    'FINDINGS.md': 'the split notice`s index of archived entry headings -- NOT ONE',
    'OPEN_TRAILS.md': 'b421`s trail on Definition 2.1, stating that none is supplied -- NOT ONE',
    'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md':
        'the two forms named *Weil positivity* and another lane`s pair field -- NOT ONE',
    'day1/A_Place_to_Stand.md': 'the SIDE syllogism: the specification of xi, not of the class -- NOT ONE',
    'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md': 'the SIDE syllogism: the specification of xi, not of the class -- NOT ONE',
    'outputs/DEPOSITED/A_Place_to_Stand.v5.4.EARLIER-DEPOSIT-SNAPSHOT.md':
        'the SIDE syllogism: the specification of xi, not of the class -- NOT ONE',
    'outputs/v54_deposit_line.md': 'the SIDE syllogism: the specification of xi, not of the class -- NOT ONE',
    'phase1.5/method/INVARIANCE_BARRIERS.md': 'the factoring table: *individual-element specification* in Definition 2.5`s sense -- NOT ONE',
}


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def norm(s):
    return re.sub(r'\s+', ' ', s or '').strip()


def unwrapped(text):
    """### A record's quoted blocks carry a `| ` gutter on every wrapped line; strip it, then fold whitespace."""
    return norm(re.sub(r'(?m)^\s*\| ', '', text or ''))


def q(path, start, end=None, cap=600):
    """### ANCHORS ARE FOUND IN THE WHITESPACE-FOLDED SOURCE: banks hard-wrap through anchors (run 1 missed one)."""
    src, s0 = norm(read(path)), norm(start)
    i = src.find(s0)
    if i < 0:
        MISS.append('%s : %r' % (os.path.basename(path), start[:48]))
        return '### MISS'
    e0 = norm(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    return src[i:j + len(e0)] if j > i else src[i:i + cap]


def line_of(path, start):
    src = read(path)
    i = src.find(start)
    return src[:i].count(NL) + 1 if i >= 0 else 0


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


def deciding():
    """### THE DECIDING SENTENCES, EACH (label, source path, the sentence) -- the suite re-finds every one at its source."""
    return [
        ('b407', IB, q(IB, 'the specification is a set-theoretic definition', 'characterized in practice.')),
        ('b407', MONO, q(MONO, 'For ξ(s): the specification is θ(τ) = Σ exp(πin²τ)', 'No human choices enter.')),
        ('b420', IB, q(IB, 'the specification is a set-theoretic definition', 'inside the ambient theory')),
        ('b420', B400, q(B400, 'a finite set disjoint from Z and containing {0,1}', 'for all z in F."*')),
        ('b420', C2, q(C2, 'documents holding the specification : 0', None, cap=len('documents holding the specification : 0'))),
    ]


def search():
    fs = subprocess.run(['git', '-C', PP, 'ls-files', '*.md'], capture_output=True, text=True).stdout.split()
    hits = []
    for f in fs:
        t = read(os.path.join(PP, *f.split('/')))
        for p in re.split(r'\n\s*\n', t):
            if re.search(r'(?i)specification', p) and re.search(r'C_c|C\^\\?infty_c|test[- ]function', p):
                m = re.search(r'(?i).{0,90}specification.{0,90}', p.replace(NL, ' '))
                hits.append((f, m.group(0) if m else ''))
    return len(fs), hits


def run_read():
    R = ['=' * 100, 'b423 -- THE (R37) QUESTION: DO b407`S AND b420`S READINGS OF HYPOTHESIS 1 MOVE?', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append

    def block(label, path, start, end=None):
        s = q(path, start, end)
        say('  %s (%s line %d) :' % (label, os.path.relpath(path, PP if path.startswith(PP) else ROOT).replace(os.sep, '/'),
                                     line_of(path, start)))
        for w in wrap(s, 94):
            say('      | %s' % w)
        return s

    say('-' * 100)
    say('### THE RULING, AND THE DEFINITION IT READS.')
    say('-' * 100)
    ruling = block('§10.2, the ruling', IB, '**The ruling, the author’s:**', 'characterized in practice.')
    block('Definition 2.1', IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
    say('  ### What the internal reading asks of a specification, in the ruling`s own words: *a set-theoretic')
    say('  definition*, with uniqueness *a statement inside the ambient theory*.')

    # ------------------------------------------------------------------------------------------------ b407
    say('')
    say('-' * 100)
    say('### b407 -- HYPOTHESIS 1 FOR xi.')
    say('-' * 100)
    r407 = block('b407`s READING, QUOTED', B407, '### Four of Theorem 3.1’s five hypotheses are', 'κ(σ, I) = 0."*')
    v407 = block('b407`s VERDICT, AND WHAT FAILS', B407, '### ### **THE ONE THAT FAILS IS THE ONE ABOUT `π`.**', 'HAS NOT DISCHARGED.**')
    say('  REST ON : HYPOTHESIS 5 -- the proof`s form (*"a formal first-order proof in ZFC ∪ S"*), not hypothesis 1.')
    spec = block('the definition the internal reading takes, the monograph`s', MONO,
                 'For ξ(s): the specification is θ(τ) = Σ exp(πin²τ)', 'No human choices enter.')
    names_xi = 'the reals and ξ are characterized in practice' in ruling
    ok407 = ('`xi` is determined' in r407) and names_xi and spec != '### MISS'
    say('  the ruling names xi among the objects it characterizes : %s' % names_xi)
    say('  the record holds a set-theoretic definition of xi       : %s' % (spec != '### MISS'))
    say('  ### DECIDING SENTENCE : §10.2 -- *"the specification is a set-theoretic definition and uniqueness is a')
    say('  statement inside the ambient theory, which is how the natural numbers, the reals and ξ are characterized in')
    say('  practice."* ### With the monograph`s definition of xi beside it, the conclusion b407 stated -- `xi` is')
    say('  determined -- stands under the internal reading, and stands on more than before: under the first-order')
    say('  reading b421 found it met by no infinite structure; under the internal reading the ruling names xi itself.')
    say('  ### VERDICT ON b407`S READING : %s' % ('CONFIRMED' if ok407 else 'MOVED'))

    # ------------------------------------------------------------------------------------------------ b420
    say('')
    say('-' * 100)
    say('### b420 -- HYPOTHESIS 1 FOR THE STRUCTURE WHOSE ELEMENTS ARE THE CLASS`S TEST FUNCTIONS.')
    say('-' * 100)
    r420 = block('b420`s READING, QUOTED', C4, '### **FOR THE STRUCTURE WHOSE ELEMENTS ARE THE CLASS`S TEST FUNCTIONS', 'the keystone does not.')
    block('b420`s VERDICT', C4, '### ### ### **NOT AN INSTANCE -- THE FIFTH HYPOTHESIS FAILS, AND IT FAILS ON FORM.**', 'IT FAILS ON FORM.**')
    block('b420`s HYPOTHESIS 1, NOT SCORED AS THE VERDICT', C4, 'Two further readings are printed, not scored as', 'b419`s terminal.')
    say('  REST ON : HYPOTHESIS 5 -- the proof`s form; hypothesis 1 was printed and not scored as the verdict.')
    block('what a specification would have to describe (b421)', C2, 'So the specification must name:', 'row S1 already names.')
    block('the class as the verified source states it (b400)', B400, '### **PROPOSITION C.1 CARRIES NONE**', 'for all z in F."*')
    say('  ### The source`s class is stated with `F` a parameter -- *"a finite set disjoint from Z and containing')
    say('  {0,1}"* -- and the arc fixes `F` by its own vanishing conditions, not the source (b421, quoted above).')
    nfs, hits = search()
    say('')
    say('  ### THE SEARCH, PRINTED: every paragraph of the %d tracked PLACE-papers .md files naming *specification*' % nfs)
    say('  beside `C_c`, `C^infty_c` or *test function*, each hit hand-read and dispositioned by file:')
    unread = []
    for f, ctx in hits:
        disp = HAND.get(f)
        if disp is None:
            unread.append(f)
        say('    %s' % f)
        say('        ... %s ...' % ctx[:180])
        say('        HAND-READ : %s' % (disp or '### UNREAD'))
    holding = 0
    say('  hits : %d ; unread : %d ; ### documents holding a specification of the structure : %d' % (len(hits), len(unread), holding))
    b421zero = 'documents holding the specification : 0' in read(C2)
    say('  b421`s own count, quoted : %s' % ('documents holding the specification : 0' if b421zero else '### MISS'))
    ok420 = ('NOT SUPPLIED BY THE RECORD' in r420) and not unread and holding == 0 and b421zero
    say('  ### DECIDING SENTENCES : §10.2 -- *"the specification is a set-theoretic definition and uniqueness is a')
    say('  statement inside the ambient theory"* -- beside b421`s *"documents holding the specification : 0"*, the')
    say('  search above, and the source`s own *"a finite set disjoint from Z and containing {0,1}"*. ### Under the')
    say('  internal reading the specification b420 found absent is a set-theoretic definition; the source defines')
    say('  its pieces with `F` left free, and no document of the record writes it. ### b420`s conclusion -- NOT')
    say('  SUPPLIED BY THE RECORD -- stands on its own ground, *"no document writes S"*.')
    say('  ### WHAT MOVES IS NOT b420`S READING BUT b421`S EXTRA GROUND: under the first-order reading the')
    say('  specification was NOT SUPPLIABLE, one no writing can do; under the internal reading it is SUPPLIABLE --')
    say('  writable from the source`s definitions with `F` fixed -- and NOT WRITTEN. ### b421 is not re-verdicted.')
    say('  ### VERDICT ON b420`S READING : %s' % ('CONFIRMED' if ok420 else 'MOVED'))

    # ------------------------------------------------------------------------------------------------ (2), (4)
    say('')
    say('-' * 100)
    say('### WHETHER EITHER VERDICT COULD MOVE, AND WHAT THE RULING DOES TO HYPOTHESIS 1.')
    say('-' * 100)
    say('  ### Both verdicts rest on hypothesis 5, the proof`s form -- b407`s *"THE ONE THAT FAILS IS THE ONE ABOUT π"*,')
    say('  b420`s *"THE FIFTH HYPOTHESIS FAILS, AND IT FAILS ON FORM"* -- so no reading of hypothesis 1 could move')
    say('  either verdict, and neither is moved. ### re-verdicts : 0.')
    say('  ### THE SEAT`S READING OF §10.2, ROUTED TO THE AUTHOR AND NOT RULED: read internally, uniqueness of a')
    say('  structure given by an explicit set-theoretic definition is a statement ZFC proves of the object the')
    say('  definition picks out, so hypothesis 1 is met by any structure once its definition is written. ### IF')
    say('  THAT READING STANDS, HYPOTHESIS 1 NO LONGER SEPARATES ONE STRUCTURE FROM ANOTHER, and whether the lemma')
    say('  applies to anything the witness arc meets turns on its other hypotheses -- the fifth above all, the one')
    say('  that failed at both acts on form. ### The keystone is not edited by this act.')
    say('')
    say('  ### FOR THE WITNESS ARC: the lemma has applied to nothing the record has put to it (b407, b420), and')
    say('  under the internal reading it is not hypothesis 1 that stops it.')
    say('')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    io.open(QREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    print(NL.join(R))
    return 0 if not MISS and ok407 and ok420 else 1


def main():
    L = []
    say = L.append
    rec = read(QREC)
    fails = [] if rec else ['the reading record is absent']
    say('=' * 100)
    say('b423_components.py -- THE (R37) QUESTION, THE REPORT.')
    say('=' * 100)
    v = {}
    for who in ('b407', 'b420'):
        ln = next((x for x in rec.splitlines() if ('VERDICT ON %s`S READING :' % who) in x), '')
        v[who] = ln.rsplit(':', 1)[-1].strip() if ln else ''
        say('  %-6s %s' % (who, ln.strip() or '### NO VERDICT LINE'))
        if v[who] not in ('CONFIRMED', 'MOVED'):
            fails.append('%s has no verdict line' % who)
    for (who, path, s) in deciding():
        found = norm(s) in norm(read(path)) and s != '### MISS' and norm(s) in unwrapped(rec)
        say('  deciding sentence for %s at %-28s re-found at its source and in the record : %s'
            % (who, os.path.basename(path), found))
        if not found:
            fails.append('deciding sentence for %s not at %s' % (who, os.path.basename(path)))
    for needle in ('re-verdicts : 0.', 'ROUTED TO THE AUTHOR AND NOT RULED', 'anchor misses : 0'):
        ok = needle in rec
        say('  %-60s %s' % (needle, ok))
        fails += [] if ok else [needle]
    say('')
    say('### THE EXPECTATION, ITS CLAUSES APART (R27):')
    say('  (L1) *b407`s reading CONFIRMED* -- ### **%s** (the reading reads %s).' % ('MET' if v['b407'] == 'CONFIRMED' else 'REFUTED', v['b407']))
    say('  (L1) *b420`s reading CONFIRMED* -- ### **%s** (the reading reads %s; b421`s extra ground, NOT SUPPLIABLE,'
        % ('MET' if v['b420'] == 'CONFIRMED' else 'REFUTED', v['b420']))
    say('       lapses under the internal reading -- the specification is suppliable and not written).')
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b423_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(run_read() if '--read' in sys.argv else main())
