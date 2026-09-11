# -*- coding: utf-8 -*-
"""b411_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.

### ### **EVERY READ IS BY ANCHOR AND EVERY ANCHOR IS RESOLVED BY THE TOOL.** ### Misses counted.
###
### ### **AND COMPONENT 3'S SEARCH IS BY DESCRIPTION, WITH A POSITIVE CONTROL WHOSE OWN YIELD IS
### ### PRINTED** -- the act is about to test a claim that something is ABSENT, and `b409` and
### `b410` both found that a search by symbol reaches a different set than a search by description.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SUB = os.path.join(D, '_b411')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
GRADER = os.path.join(PP, 'phase1.5', 'method', 'I7_SURVEYABILITY_GRADER.md')
ENGINE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
FIND = os.path.join(PP, 'FINDINGS.md')
GAUGE = os.path.join(ROOT, 'reports', '2026-08-01-w-half-consult.md')
OUT = os.path.join(D, 'b411_extract.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    say(c * 100)


def write_text(p, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(p + '.tmp', 'wb').write(data)
    os.replace(p + '.tmp', p)
    return len(data)


def pull(path, needle, label, save=None):
    try:
        ln, line = AF.find(path, needle)
    except Exception as e:
        MISS.append('%s :: %s :: %s' % (os.path.basename(path), label, e))
        say('  ### ### **ANCHOR MISS** ### %s -- %s' % (label, str(e)[:90]))
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln))
    for k in range(0, max(len(line), 1), 150):
        say('      | %s' % line[k:k + 150])
    if save:
        write_text(os.path.join(SUB, save), line + NL)
    return ln, line


def live_md():
    out = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                out.append((os.path.relpath(p, PP).replace(os.sep, '/'), p))
    return out


def main():
    if not os.path.isdir(SUB):
        os.makedirs(SUB)
    say('=' * 100)
    say('b411_extract.py -- THE SURVEY. ### EVERY READ ANCHORED, EVERY MISS COUNTED.')
    say('=' * 100)

    # ------------------------------------------------------------- (A) THE JOIN'S TWO SITES
    say()
    bar()
    say('### (A) THE TWO SITES THE JOIN CONNECTS, READ BEFORE EITHER IS TOUCHED.')
    bar()
    pull(IB, '1. The sentences mentioned in', 'SITE 1 -- DEFINITION 2.5, CLAUSE 1',
         save='clause1.txt')
    pull(IB, '**Definition 2.5 (Factoring through an interface).**', 'ITS HEAD, WHERE A NOTE GOES')
    pull(INST, '**The screen, one question, asked of the DEFINITION', 'SITE 2 -- THE SCREEN`S '
         'QUESTION', save='screen.txt')
    pull(INST, '## I-7 — THE PLACEMENT SCREEN', 'ITS HEAD, WHERE A NOTE GOES')
    say('  ### ### **NEITHER DOCUMENT CITES THE OTHER -- RE-MEASURED HERE, NOT CARRIED FROM')
    say('  ### ### `b410`.**')
    ibt = io.open(IB, encoding='utf-8', errors='replace').read()
    it = io.open(INST, encoding='utf-8', errors='replace').read()
    a = len(re.findall(r'I-7|placement screen', ibt, re.I))
    b = len(re.findall('Definition 2[.]5|transmission coefficient|INVARIANCE_BARRIERS', it))
    say('      `INVARIANCE_BARRIERS.md` naming the screen : ### **%d**' % a)
    say('      `INSTRUMENTS.md` naming the keystone`s definition : ### **%d**' % b)

    # ------------------------------------------------------------- (B) THE NUMBERING
    say()
    bar()
    say('### (B) THE INSTRUMENT NUMBERING, ENUMERATED FROM THE REGISTER`S OWN HEADINGS.')
    bar()
    heads = re.findall(r'^#+\s+(I-\d+[a-z]*)\b', it, re.M)
    seen = []
    for h in heads:
        if h not in seen:
            seen.append(h)
    say('  ### headings in `INSTRUMENTS.md` : %s' % ' '.join(seen))
    nums = sorted(set(int(re.match(r'I-(\d+)', h).group(1)) for h in seen))
    say('  ### ### **NUMBERS OCCUPIED : %s**' % ', '.join(str(n) for n in nums))
    gaps = [n for n in range(1, max(nums)) if n not in nums]
    say('  ### ### **GAPS BELOW THE HIGHEST (%d) : ### %s**'
        % (max(nums), gaps if gaps else '**NONE**'))
    say('  ### ### **THE FIRST FREE NUMBER : ### `I-%d`** ### -- ABOVE the highest, because there'
        % (max(nums) + 1))
    say('  ### ### is no gap below it.')
    say()
    say('  ### **AND WHAT IS CITED, ACROSS THE LIVE TREE:**')
    files = [(rel, p) for rel, p in live_md() if not rel.startswith('outputs/')]
    WB = chr(92) + 'b'
    for n in nums:
        pat = WB + 'I-' + str(n) + WB
        docs = [rel for rel, p in files
                if re.search(pat, io.open(p, encoding='utf-8', errors='replace').read())]
        say('      %-6s cited in %2d live document(s)%s'
            % ('I-%d' % n, len(docs), '   ### **THE CONTESTED NUMBER**' if n == 7 else ''))
    pull(GRADER, '# I-7 — the surveyability grader (spec)', 'THE QUEUED DOCUMENT')
    pull(GRADER, 'Joins `INSTRUMENTS.md` as I-7 on the author', 'AND THE WORD IT WAITS ON',
         save='queued.txt')

    # ------------------------------------------------------------- (C) THE GRADING INSTRUMENTS
    say()
    bar()
    say('### (C) WHAT GRADES A CITED CLAIM -- SEARCHED BY DESCRIPTION, NOT BY A GRADE`S NAME.')
    bar()
    say('  ### **THE PREDICATE, FIXED BEFORE THE SEARCH:** ### a live document that states a')
    say('  ### VOCABULARY for how a claim`s backing is graded, and applies it to more than one')
    say('  ### claim. ### **NOT** ### a document that merely uses a grade word in passing.')
    pats = {
        'a three-grade rubric for citations': r'DERIVES\s*/\s*INTERFACES|three[- ]grade rubric'
                                              r'|three grades',
        'an import graded under a bar': r'IMPORT[- ]UNDER[- ]THE[- ]BAR|IMPORT under the bar',
        'a claim stated as a tuple': r'cited claim is a tuple|certificate-type',
        'the two-leg grammar': r'two-leg grammar|two-leg architecture',
        'a salt-check before a citation': r'salt-check',
    }
    for lbl, pat in pats.items():
        docs = sorted(set(rel for rel, p in files
                          if re.search(pat, io.open(p, encoding='utf-8',
                                                    errors='replace').read(), re.I)))
        say('      %-38s %2d document(s)' % (lbl, len(docs)))
        for x in docs[:5]:
            say('          %s' % x)
        if len(docs) > 5:
            say('          ... and %d more' % (len(docs) - 5))
    say('  ### ### **THE POSITIVE CONTROL -- A GRADING VOCABULARY THE RECORD CERTAINLY HAS MUST')
    say('  ### ### BE FOUND BY THE SAME MACHINERY:** ### the axiom-profile grade `Compiled`.')
    ctl = sum(1 for rel, p in files
              if re.search(r'\bCompiled\b', io.open(p, encoding='utf-8',
                                                    errors='replace').read()))
    say('      the control : ### **%d document(s)** ### -- ### **%s**'
        % (ctl, 'PASSES' if ctl > 0 else 'FAILS: THE VERDICT IS WITHHELD'))
    if ctl == 0:
        MISS.append('the positive control on the grading search yielded 0')
    say()
    say('  ### **INSTRUMENT 1 -- THE CLAIM-CERTIFICATE CALCULUS, AND ITS SCOPE.**')
    pull(ENGINE, '**Role.** This record *presents* the **claim-certificate calculus**',
         'ITS CANONICAL HOME', save='calculus.txt')
    pull(ENGINE, 'Every kernel citation in this paper carries one of three grades',
         'AND WHAT IT GRADES -- ### **KERNEL CITATIONS**', save='calculus_scope.txt')
    pull(ENGINE, '**A cited claim is a tuple**', 'THE TUPLE IT USES', save='tuple.txt')
    pull(ENGINE, 'The **salt-check** is a standing gate', 'AND THE GATE IT REQUIRES')
    say()
    say('  ### **INSTRUMENT 2 -- THE E0 GATE`S GRADE TABLE, IN THE LEDGER`S ROW `S1`.**')
    hit = pull(FACES, '| S1 | S1 -- the clause stated', 'ROW S1, THE HEAD OF THE CELL')
    if hit:
        row = hit[1]
        for frag, lbl in (
                ('THE GRADE TABLE, each grade its owner', 'THE GRADE TABLE ANNOUNCED'),
                ('K2 the criterion', 'AND `K2` -- PROPOSITION C.1 ITSELF'),
                ('K8 the quantifiers', 'AND `K8` -- THE HALT'),
                ('THE RANKING, softest first', 'AND THE RANKING')):
            i = row.find(frag)
            if i < 0:
                MISS.append('row S1 :: %s' % lbl)
                say('  ### ### **NOT IN THE ROW** ### %s' % lbl)
            else:
                say('  ### %s' % lbl)
                say('      | %s' % row[i:i + 300])
        write_text(os.path.join(SUB, 'row_s1.txt'), row + NL)
    pull(FIND, '### The E0 gate: every constituent unfolded to its owner',
         'AND THE GATE`S OWN HEADING IN FINDINGS')

    # ------------------------------------------------------------- (D) THE CERTIFICATE
    say()
    bar()
    say('### (D) THE GAUGE VERIFICATION -- SECTION 9`S BRIGHT-HALF CERTIFICATE, LOCATED.')
    bar()
    pull(IB, 'The bright half is certified:', 'WHAT §9 CLAIMS', save='bright_claim.txt')
    pull(IB, '| §9 — the archimedean κ-row and the per-place table |',
         'AND WHERE IT SAYS THE CERTIFICATE LIVES')
    say('  ### ### **AND THE RELAY RECORD ITSELF, FOUND BY DESCRIPTION AND NOT BY A PIN:**')
    pull(GAUGE, '**The gauge theorem, verified numerically', 'THE GAUGE NOTE`S HEAD',
         save='gauge_head.txt')
    pull(GAUGE, '- **(a) the angle-sum over the trivial lattice**', 'ROUTE (a)',
         save='route_a.txt')
    pull(GAUGE, '- **(b) the digamma density**', 'ROUTE (b)', save='route_b.txt')
    pull(GAUGE, 'At T = 50, 100, 150 the two routes agree', 'THE NUMBERS, AND THE GAUGE',
         save='numbers.txt')
    pull(GAUGE, 'The candidate row:', 'AND THE SAME REPORT PROPOSED §9`S ROW, VERBATIM',
         save='candidate.txt')
    pull(GAUGE, '**Boundary sentence, on the face:**', 'AND ITS OWN BOUNDARY SENTENCE')
    say()
    say('  ### **IS THE CERTIFICATE REPRODUCIBLE FROM WHAT IS BANKED? ### MEASURED:**')
    g = io.open(GAUGE, encoding='utf-8', errors='replace').read()
    for lbl, pat in (('both routes given as formulae', r'Im log .|Re .\(.|psi'),
                     ('the test heights named', r'T = 50, 100, 150'),
                     ('the agreement bound printed', r'agree to . 8e.4|8e-4'),
                     ('the asymptotic match printed', r'1e.3'),
                     ('the S(T) values printed', r'S\(T\) . \+?0\.58')):
        ok = bool(re.search(pat, g))
        say('      %-34s %s' % (lbl, '### **YES**' if ok else '### **NO**'))

    say()
    bar('=')
    say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
    for m in MISS:
        say('      %s' % m)
    bar('=')
    write_text(OUT, NL.join(L) + NL)
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
