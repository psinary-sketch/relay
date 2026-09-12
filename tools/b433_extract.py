# -*- coding: utf-8 -*-
"""b433_extract.py -- THE SURVEY FOR b433: THE FIVE RULINGS EXECUTED.
### **THE CORPUS ONLY. ### NOTHING IS FETCHED, NOTHING IS BUILT, AND THIS TOOL WRITES NO CORPUS
### FILE.** ### Its job is to put every blob this act will repair on disk BEFORE the face is typed,
### together with ### **EACH DOCUMENT'S OWN PRECEDENT FOR ANNOTATION**, so that no repair invents a
### form the document does not already use (`(R4)`: preserve by quotation, repair by edit).
"""
import hashlib
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
RDM = os.path.join(PP, 'README.md')
EXC = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
CONSP = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
FIND = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
BARRIER = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
CLONE = os.path.join('D:', os.sep, '_b431_external')
FERRY = os.path.join(D, 'b433_ferry.txt')
OUT = os.path.join(D, 'b433_extract.txt')
BLOBS = os.path.join(D, 'b433_preact_blobs.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]
PRE = {}


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


def blob(path):
    """### **THE PRE-ACT BLOB, BY DIGEST AND BY BYTES.** ### Every repair is measured against this
    ### and not against a memory of it; the byte delta in the closing is `after - before`."""
    b = open(path, 'rb').read() if os.path.exists(path) else b''
    h = hashlib.sha256(b).hexdigest()
    PRE[os.path.relpath(path, PP) if path.startswith(PP) else path] = (len(b), h)
    return len(b), h


def rows(path, pat, cap=8, maxlen=900):
    """### ALL MATCHING LINES, FOLDED BEFORE MATCHING (b432's bar)."""
    out = []
    for i, ln in enumerate(read(path).splitlines(), 1):
        if re.search(pat, fold(ln)) or re.search(pat, ln):
            out.append((i, fold(ln)[:maxlen]))
        if len(out) >= cap:
            break
    return out


def main(argv):
    rule('=')
    say('b433_extract.py -- THE SURVEY. ### EVERY BLOB THIS ACT WILL REPAIR, AND EACH DOCUMENT\'S')
    say('### OWN PRECEDENT FOR ANNOTATION.')
    rule('=')
    say('  ### NOTHING IS FETCHED. ### NOTHING IS BUILT. ### THIS TOOL WRITES NO CORPUS FILE.')
    say()

    # ### =========================================================================================
    rule()
    say('  (1) THE PRE-ACT BLOBS, BY BYTES AND DIGEST.')
    rule()
    for p in (RDM, EXC, CONSP, FIND, FACES, TRAILS, BARRIER):
        n, h = blob(p)
        say('    %-52s %9d bytes  %s' % (os.path.relpath(p, PP), n, h[:16]))
    say('    ### **EVERY REPAIR IS MEASURED AGAINST THESE.** ### The closing prints `after - before`')
    say('    ### for each, and a NEGATIVE delta anywhere would mean something was removed.')
    say()

    # ### =========================================================================================
    rule()
    say('  (2) (R41) -- THE TWO GRADE-VOCABULARY DOCUMENTS, AT THEIR OWN HEADINGS.')
    rule()
    for lbl, p, pat in (('README.md', RDM, r'^### The three grades\s*$'),
                        ('EXCLUSION_ENGINE.md', EXC, r'^## 0\. Reading this paper: the three grades')):
        txt = read(p)
        ln = next((i for i, x in enumerate(txt.splitlines(), 1) if re.match(pat, x)), None)
        say('    %-24s heading at line %s' % (lbl, ln))
        if ln is None:
            MISS.append('%s: grade heading not located' % lbl)
            continue
        body = txt.splitlines()[ln - 1:ln + 14]
        for x in body:
            say('        %s' % x.rstrip()[:96])
        say()
    say('    ### **BOTH SAY "THREE" IN A HEADING AND LIST THREE BULLETS.** ### (R41) makes it four,')
    say('    ### ADDITIVELY: the heading gains its correction, the three bullets are UNTOUCHED, and')
    say('    ### a fourth bullet is added with the two incidents that produced it.')
    say()
    say('    ### THE TWO INCIDENTS (R41) REQUIRES CITED, FROM THEIR OWN BANKS:')
    for tag, f, needle in (('b429', 'b429_the_grade.txt', r'four grades, including'),
                           ('b430', 'b430_grades.json', r'"grade_b"\s*:\s*"NOT THE CLAIM"')):
        t = read(os.path.join(D, f))
        m = re.search(needle, t)
        say('      %s  %-28s : %s' % (tag, f, 'FOUND' if m else '### NOT FOUND ###'))
        if not m:
            MISS.append('%s incident not readable from %s' % (tag, f))
    say()

    # ### =========================================================================================
    rule()
    say('  (3) (R42) -- THE CONSPIRACY KEYSTONE: THE PROSE CLAIM, AND ITS OWN ANNOTATION FORM.')
    rule()
    for i, r in rows(CONSP, r'beyond what the Chinese Remainder Theorem explains', 2, 900):
        say('    THE PROSE CLAIM -- line %d:' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    for i, r in rows(CONSP, r'CRT exhaustiveness via periodic lift', 3, 400):
        say('    THE LEMMA AS THE PROSE NAMES IT -- line %d:' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    say()
    say('    ### **THE DOCUMENT\'S OWN ANNOTATION FORM, QUOTED SO THIS ACT INVENTS NOTHING:**')
    for i, r in rows(CONSP, r'annotation added .*existing text PRESERVED', 2, 400):
        say('      line %d:' % i)
        for w in wrap(r, 88, '          '):
            say(w)
    say('    ### **SO THE FORM IS: AN ANNOTATION BLOCK THAT DECLARES THE EXISTING TEXT PRESERVED**')
    say('    ### **AND SAYS WHAT IT ADDS.** ### (R42) says the name STAYS and the prose NARROWS, so')
    say('    ### the narrowing is written as this document already writes one.')
    say()
    say('    ### AND THE MEASURED FACT THE ANNOTATION WILL STATE, from b431\'s bank:')
    b431 = read(os.path.join(D, 'b431_components.txt'))
    for needle in (r'moduli := \{[^}]*\} -- A SINGLETON', r'no Chinese remainder',
                   r'the periodic lift'):
        m = re.search(needle, b431)
        say('      %-40s : %s' % (needle[:40], 'FOUND in b431_components.txt' if m else '### NO ###'))
    say()

    # ### =========================================================================================
    rule()
    say('  (4) (R43) -- K3 IN THE CLAUSE ANCHOR AND F5 IN THE FACES LEDGER.')
    rule()
    k3 = [(i, r) for i, r in rows(FIND, r'^\|\s*(\*\*)?K3', 8, 900)]
    k3 += [(i, r) for i, r in rows(FIND, r'^\|\s*\d+\s*\|\s*\*\*K3\*\*', 4, 900)]
    for i, r in k3:
        say('    FINDINGS.md:%d' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    say()
    f5 = rows(FACES, r'^\|\s*(\*\*)?F5', 6, 1400)
    for i, r in f5:
        say('    FACES_LEDGER.md:%d  %s' % (i, '<-- THE CLAIM-BEARING ROW (b430\'s printed rule)'
                                           if 'FiniteSideSeal.lean' in r else ''))
        for w in wrap(r[:1000], 88, '        '):
            say(w)
    say()
    say('    ### **AND THE READING THIS ACT TAKES OF (R43), STATED BEFORE IT ACTS.** ### The ruling')
    say('    ### says "narrowed ... originals preserved ... K3\'s nine named objects KEPT ... and')
    say('    ### MARKED as not carried by the terminal" -- ### **WHICH IS ADDITIVE BY ITS OWN**')
    say('    ### **WORDS.** ### That matters, because `F5`\'s clause *GENERAL, over every base')
    say('    ### p >= 2* is TRUE of the terminals `F5` lists -- `valuation_exists` and the rest of')
    say('    ### the scaling part -- and `smear_general` is in NEITHER of its lists, being a later')
    say('    ### terminal (b419). ### **REWRITING THAT CLAUSE TO "SINGLE-PRIME-FACTOR" WOULD MAKE**')
    say('    ### **THE ROW FALSE ABOUT ITS OWN LISTED TERMINALS.** ### So the narrowing is written')
    say('    ### as a marking beside the original, which is what the ruling asks for.')
    say()

    # ### =========================================================================================
    rule()
    say('  (5) THE DISPROOF LANE\'S TRAIL ENTRY, AND THE SYMMETRY CLAUSE TO QUOTE BESIDE IT.')
    rule()
    t = read(TRAILS)
    mk = '<!-- b432 the disproof lane restated with a worked case -->'
    say('    b432\'s trail marker present : %s' % (mk in t))
    if mk not in t:
        MISS.append('b432 trail marker absent')
    say('    the entry ends at the file\'s end : %s' % t.rstrip().endswith('left it.**'))
    for i, r in rows(BARRIER, r'\*\*T1 functional equation\*\*', 2, 600):
        say('    THE SYMMETRY CLAUSE -- INVARIANCE_BARRIERS.md:%d' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    say()
    say('    ### **THE SENTENCE THE ORDER REQUIRES** -- that the instruments are not symmetric')
    say('    ### though the theory is -- rests on b432\'s own finding, which is in its bank:')
    b432 = read(os.path.join(D, 'b432_components.txt'))
    m = re.search(r'THE CORPUS HAS NO INSTRUMENT POINTED', b432)
    say('      b432_components.txt carries the form-(b) finding : %s' % bool(m))
    if not m:
        MISS.append('b432 form-(b) finding not readable')
    say()

    # ### =========================================================================================
    rule()
    say('  (6) (R45) -- THE EXTERNAL CLONE, AS IT STANDS NOW.')
    rule()
    exists = os.path.isdir(CLONE)
    say('    D:/_b431_external present : %s' % exists)
    if exists:
        # ### **THE FIRST WRITING WALKED THE WHOLE CLONE AND DID NOT RETURN.** ### A Mathlib
        # ### checkout is hundreds of thousands of files across `.lake` and `.git`, and a survey
        # ### step that cannot finish is not a survey step. ### **THE SIZE IS A NICETY AND NOTHING
        # ### IN THIS ACT RESTS ON IT**; what the act needs is PRESENCE before and ABSENCE after.
        say('    top-level entries        : %s' % sorted(os.listdir(CLONE))[:8])
        say('    ### size NOT measured here -- see the note in this tool; the removal reports the')
        say('    ### space freed, measured once, by the platform`s own tool.')
    say('    ### **WHAT STANDS IN ITS PLACE, ALL BANKED AT RELAY AND ALL COMMITTED:**')
    for f in ('b431_paper_pin.txt', 'b431_stepzero_lsremote.txt', 'b431_build.log',
              'b431_profile.txt', 'b431_the_grade.json'):
        p = os.path.join(D, f)
        say('      %-32s %s' % (f, 'PRESENT, %d bytes' % os.path.getsize(p)
                                if os.path.exists(p) else '### ABSENT ###'))
        if not os.path.exists(p):
            MISS.append('the record substitute is missing: %s' % f)
    tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch',
                              'data/b431_build.log', 'data/b431_profile.txt',
                              'data/b431_paper_pin.txt'],
                             capture_output=True, text=True)
    say('      all three tracked in git  : %s' % (tracked.returncode == 0))
    say('    ### **THE CLONE IS REMOVED ONLY AFTER THIS LINE READS TRUE**, because a removal whose')
    say('    ### substitutes are not committed is a deletion, not a substitution.')
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
    bl = ['b433 -- THE PRE-ACT BLOBS. ### EVERY REPAIR IS MEASURED AGAINST THESE.', '']
    for k in sorted(PRE):
        bl.append('%-56s %9d  %s' % (k, PRE[k][0], PRE[k][1]))
    io.open(BLOBS + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(bl) + NL)
    os.replace(BLOBS + '.tmp', BLOBS)
    print(txt)
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(BLOBS)))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
