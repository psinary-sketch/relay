# -*- coding: utf-8 -*-
"""b430_extract.py -- THE SURVEY FOR b430: THE SELF-CONTROL.
### **THE CORPUS AND THIS MACHINE ONLY. ### NOTHING IS FETCHED, NOTHING IS BUILT AND NO KERNEL IS
### COMPILED HERE.** ### Every read anchored in the markup-folded text, every miss counted.
### ### **THE ACT GRADES THE CORPUS'S OWN TERMINAL BY THE PROTOCOL IT USED ON A STRANGER'S**, so
### the survey's job is to put the two claims the terminal will be graded against on disk BEFORE
### the face is typed -- the claim its correspondence row names, and the claim the finite-side
### prose makes -- together with b429's four compared clauses, which are the control.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
SMEAR = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
TABLE = os.path.join(KERN, 'CORRESPONDENCE.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
FIND = os.path.join(PP, 'FINDINGS.md')
RDM = os.path.join(PP, 'README.md')
EXC = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
FERRY = os.path.join(D, 'b430_ferry.txt')
B429G = os.path.join(D, 'b429_the_grade.txt')   # ### **THE BANK THAT CARRIES THE COMPARED
B429C = os.path.join(D, 'b429_closing.txt')     # ### CLAUSES; FIRST WRITING NAMED THE WRONG FILE
# ### and the miss was PRINTED rather than passed -- which is the only reason it was seen.
ROWGEN = os.path.join(ROOT, 'tools', 'rowgen', 'rowgen.py')
OUT = os.path.join(D, 'b430_extract.txt')
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
    """### MARKUP FOLDED BEFORE ANY MATCH -- b427's bar, carried."""
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x201C), '"').replace(chr(0x201D), '"')
                  .replace(chr(0x2014), '--')).strip()


def unbar(s):
    """### b426's WRAP-TRAP CURE: a bank prefixes each wrapped continuation with a bar."""
    return fold(re.sub(NL + r'\s*\|\s?', ' ', s or ''))


def wrap(text, width=98, indent='    '):
    """### WORD BOUNDARIES, never mid-token -- BAR 12."""
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


def qrow(path, marker, maxlen=1400):
    """### A ROW IS READ FROM ITS OWN LINE, BY MARKER -- b428's bar. ### **NEVER BY SEARCHING THE
    ### WHOLE DOCUMENT FOR A PHRASE**, which is how a neighbouring row's words get quoted as this
    ### row's. ### Returns `(line_no, the row's folded text)` or `(None, '')`."""
    txt = read(path)
    for i, ln in enumerate(txt.splitlines(), 1):
        if re.match(r'^\s*\|\s*(\*\*)?' + re.escape(marker) + r'(\*\*)?\s*[|(]', ln):
            return i, unbar(ln)[:maxlen]
    return None, ''


def block(path, needle, before=0, after=0):
    """### A NAMED LINE AND ITS NEIGHBOURS, by a needle checked against the FOLDED text."""
    txt = read(path)
    lines = txt.splitlines()
    n = fold(needle)
    for i, ln in enumerate(lines):
        if n in fold(ln):
            lo, hi = max(0, i - before), min(len(lines), i + after + 1)
            return i + 1, lines[lo:hi]
    return None, []


def defs_in(src, names):
    """### THE DEFINITIONS A STATEMENT RESTS ON, QUOTED FROM THE KERNEL'S OWN SOURCE.
    ### ### **THE UNFOLDING IS THE GRADE'S SUBSTANCE AND IT IS DONE FROM SOURCE, NOT FROM PROSE.**
    ### Searches this file and, where absent, reports the miss rather than guessing a body."""
    out = {}
    for nm in names:
        m = re.search(r'(?m)^\s*(?:@\[[^\]]*\]\s*)?(def|abbrev|theorem|lemma)\s+' +
                      re.escape(nm) + r'\b(.*?)(?=' + NL + r'(?:@\[|def |abbrev |theorem |lemma |'
                      r'end |namespace |/--)|\Z)', src, re.S)
        out[nm] = m.group(0).strip() if m else None
    return out


def main(argv):
    rule('=')
    say('b430_extract.py -- THE SURVEY FOR b430: THE SELF-CONTROL.')
    rule('=')
    say('  ### NOTHING IS FETCHED. ### NO KERNEL IS BUILT HERE. ### NO GRADE IS CONFERRED HERE.')
    say('  ### This file exists so that every claim the act grades against is ON DISK BEFORE the')
    say('  ### registration face is typed, which is the only order in which a face can be honest.')
    say()

    # ### =========================================================================================
    # ### (1) THE RULING, QUOTED FROM THE BANKED FERRY AND NOT FROM MEMORY.
    # ### =========================================================================================
    rule()
    say('  (1) RULING (R40), QUOTED FROM THE BANKED FERRY.')
    rule()
    ft = read(FERRY)
    m = re.search(r'RULING \(R40\).*?(?=' + NL + r'{2}LEG 1)', ft, re.S)
    r40 = unbar(m.group(0)) if m else ''
    if not r40:
        MISS.append('(R40) not found in the banked ferry')
    for ln in wrap(r40):
        say(ln)
    say()
    say('      ### THE FOURTH GRADE THE RULING NAMES : NOT THE CLAIM')
    say('      ### ITS SCOPE, IN THE RULING\'S OWN WORDS : "for a terminal that states strictly')
    say('      ### less than the claim named".')
    say()

    # ### =========================================================================================
    # ### (2) THE CORPUS'S GRADE VOCABULARY, MEASURED RATHER THAN RECALLED.
    # ### =========================================================================================
    rule()
    say('  (2) THE GRADE VOCABULARY, MEASURED IN THE CORPUS\'S OWN DOCUMENTS.')
    rule()
    for lbl, p, needle in (('README.md', RDM, 'DERIVES'),
                           ('EXCLUSION_ENGINE.md', EXC, 'DERIVES')):
        n, ls = block(p, needle, 0, 3)
        say('    %-22s : %s' % (lbl, ('line %d' % n) if n else '### NOT FOUND ###'))
        for ln in ls[:4]:
            for w in wrap(fold(ln), 92, '        '):
                say(w)
    say()
    # ### **THE FOURTH GRADE IS COUNTED, NOT ASSERTED ABSENT** -- b429 measured 0 and this act
    # ### re-measures, because an absence asserted from a prior act is a memory, not a reading.
    corpus_docs = ['README.md', 'FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md',
                   'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'ERRATA.md']
    hits = []
    for f in corpus_docs:
        t = fold(read(os.path.join(PP, f)))
        if re.search(r'NOT THE CLAIM', t, re.I):
            hits.append(f)
    say('    documents naming NOT THE CLAIM as a grade : %d %s' % (len(hits), hits if hits else ''))
    say('    ### **THE FOURTH GRADE IS THE FERRY\'S, NOT THE CORPUS\'S**, and (R40) is what seats')
    say('    ### it. ### This count is re-measured here and not carried from b429.')
    say()

    # ### =========================================================================================
    # ### (3) THE FIRST CLAIM: WHAT THE TERMINAL'S OWN CORRESPONDENCE ROW NAMES.
    # ### =========================================================================================
    rule()
    say('  (3) CLAIM A -- THE CLAIM THE TERMINAL\'S CORRESPONDENCE ROW NAMES (row 268, b419).')
    rule()
    n268, row268 = qrow(TABLE, '268', 2000)
    say('    CORRESPONDENCE.md line : %s' % (n268 if n268 else '### NOT FOUND ###'))
    m = re.search(r'COMPONENT 1:(.*?)(?:COMPONENT 2|$)', row268, re.S)
    claim_a = fold(m.group(1)) if m else ''
    say('    ### THE ROW\'S COMPONENT-1 SENTENCE, WHICH IS WHERE THE ROW NAMES ITS CLAIM:')
    for ln in wrap(claim_a, 92, '        '):
        say(ln)
    say('    ### THE TERMINALS THE ROW NAMES:')
    m = re.search(r'\|\s*(SmearGeneral[^|]*)\|', row268)
    for ln in wrap(fold(m.group(1)) if m else '### NOT FOUND ###', 92, '        '):
        say(ln)
    say()

    # ### =========================================================================================
    # ### (4) THE SECOND CLAIM: WHAT THE FINITE-SIDE PROSE SAYS.
    # ### =========================================================================================
    rule()
    say('  (4) CLAIM B -- THE FINITE-SIDE PROSE: THE FACES LEDGER\'S F5 ROW AND THE ANCHOR\'S K3.')
    rule()
    nf5, f5 = qrow(FACES, 'F5', 2600)
    say('    FACES_LEDGER.md F5 at line : %s' % (nf5 if nf5 else '### NOT FOUND ###'))
    for ln in wrap(f5, 92, '        '):
        say(ln)
    say()
    for i, mk in enumerate(('K3',)):
        txt = read(FIND)
        rows = [(j, unbar(ln)) for j, ln in enumerate(txt.splitlines(), 1)
                if re.match(r'^\s*\|\s*(\*\*)?' + mk + r'(\*\*)?\s*[|(]', ln)
                or re.match(r'^\s*\|\s*\d+\s*\|\s*\*\*' + mk + r'\*\*', ln)]
        say('    FINDINGS.md rows keyed %s : %d' % (mk, len(rows)))
        for j, r in rows:
            say('      line %d:' % j)
            for ln in wrap(r[:1200], 90, '          '):
                say(ln)
    say()

    # ### =========================================================================================
    # ### (5) THE TERMINAL ITSELF, AND THE DEFINITIONS ITS STATEMENT RESTS ON.
    # ### =========================================================================================
    rule()
    say('  (5) THE TERMINAL, AND THE BASE OBJECTS ITS STATEMENT UNFOLDS TO.')
    rule()
    src = read(SMEAR)
    say('    Core/SmearGeneral.lean : %d bytes, %d lines'
        % (len(src.encode('utf-8')), len(src.splitlines())))
    n, ls = block(SMEAR, 'theorem smear_general', 0, 2)
    say('    the statement, at line %s:' % n)
    for ln in ls[:3]:
        say('        %s' % ln.rstrip()[:96])
    say()
    # ### THE DEFINITIONS ARE HUNTED ACROSS THE KERNEL, NOT ASSUMED LOCAL.
    want = ['ballQ', 'sumAN', 'sumAQ', 'singlePrimeFactor', 'gridN']
    found, where = {}, {}
    core = os.path.join(KERN, 'Core')
    files = [os.path.join(core, f) for f in sorted(os.listdir(core))] if os.path.isdir(core) else []
    for f in files:
        if not f.endswith('.lean'):
            continue
        s = read(f)
        for nm, body in defs_in(s, [w for w in want if w not in found]).items():
            if body:
                found[nm] = body
                where[nm] = os.path.basename(f)
    for nm in want:
        say('    %-20s : %s' % (nm, where.get(nm, '### NOT LOCATED IN Core/ ###')))
        if nm in found:
            for ln in found[nm].splitlines()[:6]:
                say('        %s' % ln.rstrip()[:96])
    if [w for w in want if w not in found]:
        MISS.append('definitions not located: %s' % ', '.join(w for w in want if w not in found))
    say()

    # ### =========================================================================================
    # ### (6) THE PROTOCOL b429 USED, SO THIS ACT CAN BE HELD TO IT RATHER THAN TO A PARAPHRASE.
    # ### =========================================================================================
    rule()
    say('  (6) b429\'S PROTOCOL AND ITS FOUR COMPARED CLAUSES -- THE CONTROL, QUOTED.')
    rule()
    g = read(B429G)
    c = read(B429C)
    # ### **THE BANK HARD-WRAPS THESE CLAUSES**, so a single-line needle returns the first line of
    # ### each and loses the rest. ### First writing did exactly that and the quotes read as
    # ### sentences that stop mid-clause. ### The block runs to the NEXT label or marked line.
    def clauses(txt, label):
        out = []
        for m_ in re.finditer(r'(?m)^\s*' + label + r'\s*:\s*(.*(?:' + NL +
                              r'(?!\s*(?:TO THE STRANGER|TO ITSELF)\s*:)(?!\s*###).*)*)', txt):
            out.append(fold(m_.group(1)))
        return out
    both = g + NL + c
    pairs = clauses(both, 'TO THE STRANGER')
    selfs = clauses(both, 'TO ITSELF')
    say('    b429 bank TO THE STRANGER lines : %d' % len(pairs))
    say('    b429 bank TO ITSELF        lines : %d' % len(selfs))
    for i, (a, b) in enumerate(zip(pairs, selfs), 1):
        say('      clause %d' % i)
        for ln in wrap('TO THE STRANGER : ' + fold(a), 88, '          '):
            say(ln)
        for ln in wrap('TO ITSELF       : ' + fold(b), 88, '          '):
            say(ln)
    if len(pairs) < 4:
        MISS.append('fewer than four compared clauses recovered from b429\'s bank')
    say()

    # ### =========================================================================================
    # ### (7) THE MECHANICAL DEFINITION CHECK THE FERRY NAMES, LOCATED AND NOT RUN.
    # ### =========================================================================================
    rule()
    say('  (7) rowgen\'s defenc -- THE TOOL THE FERRY NAMES, LOCATED HERE AND RUN IN COMPONENTS.')
    rule()
    rg = read(ROWGEN)
    say('    tools/rowgen/rowgen.py : %s' % ('PRESENT, %d lines' % len(rg.splitlines())
                                             if rg else '### ABSENT ###'))
    n, ls = block(ROWGEN, 'def definition_encoded', 0, 12)
    say('    definition_encoded at line %s:' % n)
    for ln in ls:
        say('        %s' % ln.rstrip()[:96])
    say()

    # ### =========================================================================================
    # ### (8) THE MACHINE, BECAUSE THE ACT MUST BUILD FROM THE PIN.
    # ### =========================================================================================
    rule()
    say('  (8) THE KERNEL AT ITS PIN, AND THE BUILD ROUTE THIS CORPUS USES.')
    rule()
    try:
        head = subprocess.run(['git', '-C', KERN, 'rev-parse', 'HEAD'], capture_output=True,
                              text=True).stdout.strip()
        dirty = subprocess.run(['git', '-C', KERN, 'status', '--porcelain'], capture_output=True,
                               text=True).stdout.strip()
    except Exception as exc:
        head, dirty = '### %s' % exc, ''
    say('    SIDE-global-section HEAD  : %s' % head)
    say('    working tree              : %s' % ('CLEAN' if not dirty else
                                                '%d modified path(s)' % len(dirty.splitlines())))
    ap = os.path.join(KERN, 'AXIOM_PRINTS.txt')
    apt = read(ap)
    say('    AXIOM_PRINTS.txt          : %s'
        % ('%d lines' % len(apt.splitlines()) if apt else '### ABSENT ###'))
    hits = [ln for ln in apt.splitlines() if 'smear_general' in ln]
    say('    lines naming smear_general: %d' % len(hits))
    for ln in hits[:4]:
        say('        %s' % ln.strip()[:96])
    say('    lakefile present          : %s'
        % os.path.exists(os.path.join(KERN, 'lakefile.lean')))
    say('    ### **NO lakefile: THE ROUTE IS `LEAN_PATH=build lean`, AND AXIOM_PRINTS IS THE')
    say('    ### STDOUT OF `lean AllPrints`.** ### Read here; the build is the components\' work.')
    say()

    # ### =========================================================================================
    rule('=')
    say('  ### READS ATTEMPTED : %d' % READS[0])
    say('  ### MISSES          : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.** ### A survey that silently supplies what it')
    say('  ### could not read is the one state from which a face cannot be honest.')
    rule('=')

    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    print(txt)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
