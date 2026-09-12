# -*- coding: utf-8 -*-
"""b432_extract.py -- THE SURVEY FOR b432: THE DISPROOF LANE RESTATED WITH A WORKED CASE.
### **THE CORPUS ONLY. ### NOTHING IS FETCHED, NOTHING IS BUILT, NO LANE IS OPENED BY THIS TOOL.**
### ### **THE LANE WAS NAMED AT b428 WITH NO EXAMPLE OF WHAT A GRADED DISPROOF LOOKS LIKE.** ### The
### sortie has since produced two, and they are of the two different shapes a disproof can take --
### which is why the order asks for the restatement now and not at b428.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
BARRIER = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
RDM = os.path.join(PP, 'README.md')
FERRY = os.path.join(D, 'b432_ferry.txt')
B428 = os.path.join(D, 'b428_components.txt')
OUT = os.path.join(D, 'b432_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    READS[0] += 1
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x201C), '"').replace(chr(0x201D), '"')
                  .replace(chr(0x2014), '--')).strip()


def unbar(s):
    return fold(re.sub(NL + r'\s*\|\s?', ' ', s or ''))


def wrap(text, width=90, indent='        '):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(indent + line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(indent + line)
    return out


def rows_matching(path, pat, cap=6, maxlen=900):
    """### EVERY ROW WHOSE LINE MATCHES, WITH ITS LINE NUMBER. ### **ALL MATCHES, NEVER THE FIRST**
    ### -- b430 learned on `F5` that a marker can name three different rows."""
    out = []
    for i, ln in enumerate(read(path).splitlines(), 1):
        if re.search(pat, ln):
            out.append((i, unbar(ln)[:maxlen]))
        if len(out) >= cap:
            break
    return out


def main(argv):
    rule('=')
    say('b432_extract.py -- THE SURVEY. ### THE DISPROOF LANE\'S VOCABULARY, READ AT CONTENT.')
    rule('=')
    say('  ### NOTHING IS FETCHED. ### NO LANE IS OPENED HERE. ### NO TRIGGER IS TOUCHED.')
    say()

    # ### =========================================================================================
    rule()
    say('  (1) THE LANE AS b428 NAMED IT, QUOTED FROM b428\'S OWN BANK.')
    rule()
    b = read(B428)
    hits = [ln for ln in b.splitlines() if re.search(r'disproof', ln, re.I)]
    say('    lines in b428\'s components naming the lane : %d' % len(hits))
    for ln in hits[:10]:
        for w in wrap(fold(ln), 88, '        '):
            say(w)
    if not hits:
        MISS.append('b428 components carry no line naming the disproof lane')
    say()

    # ### =========================================================================================
    rule()
    say('  (2) THE TWO GRADED TERMINALS THE SORTIE PRODUCED -- THE WORKED CASES.')
    rule()
    say('    ### **THE ORDER SAYS THE RECORD NOW HOLDS TWO: "a terminal graded DERIVES against a')
    say('    ### breakdown statement, and a second graded against the construction that exhibits')
    say('    ### the breakdown." ### THE SURVEY CHECKS THAT AGAINST THE TWO BANKS.**')
    for tag, f, term in (('b429', 'b429_the_grade.txt', 'navier_stokes_breakdown_R3'),
                         ('b431', 'b431_the_grade.json', 'long_prime_gaps')):
        t = read(os.path.join(D, f))
        m = re.search(r'"grade"\s*:\s*"([^"]+)"', t) or re.search(r'GRADE\s*:\s*\*?\*?(\w[\w ]*)', t)
        say('    %s  %-28s grade in its own bank : %s'
            % (tag, term, (m.group(1).strip() if m else '### NOT READ ###')))
        if not m:
            MISS.append('%s: grade not readable from %s' % (tag, f))
    say()
    say('    ### AND THE SHAPE OF EACH CONCLUSION, READ FROM THE STATEMENT AND NOT FROM THE GRADE:')
    ns = read(os.path.join(D, 'b429_the_grade.txt'))
    m = re.search(r'universal negative', ns, re.I)
    say('      b429 / statement C   : %s'
        % ('its own bank calls the conclusion a UNIVERSAL NEGATIVE' if m else '### NOT FOUND ###'))
    lg = read(os.path.join(D, 'b431_components.txt'))
    m2 = re.search(r'∃ c X₀', lg)
    say('      b431 / Theorem 1.1   : %s'
        % ('the statement opens with an EXISTENTIAL -- a construction' if m2
           else '### NOT FOUND ###'))
    say('    ### **SO THE TWO ARE OF TWO SHAPES, AND THOSE ARE THE TWO SHAPES A DISPROOF TAKES.**')
    say()

    # ### =========================================================================================
    rule()
    say('  (3) THE BARRIER KEYSTONE\'S SYMMETRY CLAUSE, AT ITS OWN FILE AND LINE.')
    rule()
    for lbl, pat in (('T1, the functional equation', r'\*\*T1 functional equation\*\*'),
                     ('T6, codimension-2 transversality', r'\*\*T6 codim(ension)?-2 transversality\*\*')):
        for i, r in rows_matching(BARRIER, pat, 4, 700):
            say('    %s' % lbl)
            say('      INVARIANCE_BARRIERS.md:%d' % i)
            for w in wrap(r, 88, '          '):
                say(w)
            say()
    say('    ### **T6 IS THE CLAUSE A DISPROOF OF THE EXHIBITED-ZERO KIND MUST SATISFY**, and it')
    say('    ### is the keystone\'s own statement, not this act\'s gloss: an off-line zero needs')
    say('    ### `Re F = Im F = 0`, two real conditions, so it has CODIMENSION 2.')
    say()

    # ### =========================================================================================
    rule()
    say('  (4) THE NEGATIVE CONTROL, AND WHAT IT WAS RUN ON.')
    rule()
    for i, r in rows_matching(FIND, r'negative control', 6, 700):
        say('    FINDINGS.md:%d' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    say()
    say('    ### AND THE OBJECT IT IS RUN ON, from the barrier keystone\'s own account:')
    for i, r in rows_matching(BARRIER, r'Davenport.{0,3}Heilbronn \(1936\) proved', 2, 600):
        say('      INVARIANCE_BARRIERS.md:%d' % i)
        for w in wrap(r, 88, '          '):
            say(w)
    say()

    # ### =========================================================================================
    rule()
    say('  (5) THE PHASE CONDITION.')
    rule()
    for i, r in rows_matching(FIND, r'phase condition', 4, 700):
        say('    FINDINGS.md:%d' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    for i, r in rows_matching(TRAILS, r'45|phase condition', 4, 600):
        if 'phase' in r.lower() or '45' in r:
            say('    OPEN_TRAILS.md:%d' % i)
            for w in wrap(r, 88, '        '):
                say(w)
    say()

    # ### =========================================================================================
    rule()
    say('  (6) THE CORPUS\'S OWN WORDS FOR THE HYPOTHESIS AND ITS BALANCE.')
    rule()
    for lbl, pat in (('the located clause', r'single located clause'),
                     ('positivity on the zeros', r'positive space on the zeros')):
        for i, r in rows_matching(BARRIER, pat, 2, 700):
            say('    %s -- INVARIANCE_BARRIERS.md:%d' % (lbl, i))
            for w in wrap(r[:600], 88, '        '):
                say(w)
    say()

    rule('=')
    say('  ### READS ATTEMPTED : %d' % READS[0])
    say('  ### MISSES          : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    print(txt)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
