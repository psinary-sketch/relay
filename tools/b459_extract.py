# -*- coding: utf-8 -*-
"""b459_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE INDEX-SET TEST.
### ### Addresses, offsets and locations only.
### ### **IT DOES NOT EXTRACT ANY SITE'S INDEX AND PLACES NOTHING -- THAT IS COMPONENT 1 AND 2.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b459_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def find(path, needle, label, show=130):
    ls = read(path).split(chr(10))
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def main():
    FL = os.path.join(PP, 'FACES_LEDGER.md')
    FN = os.path.join(PP, 'FINDINGS.md')
    W = os.path.join(T, 'b321_window.py')
    rec('=' * 100)
    rec('b459 -- THE SURVEY. ### THE SIX SITES AGAINST THREE CANDIDATE INDEX SETS.')
    rec('=' * 100)
    rec('')

    rec('(P1) ROW U1 AND ITS SIX SITE MARKERS. ### **LOCATED, NOT READ FOR THEIR INDICES.**')
    ls = read(FL).split(chr(10))
    row = [(i + 1, l) for i, l in enumerate(ls) if l.startswith('| U1 |')]
    if not row:
        MISSES.append(('P1 row U1', 'FACES_LEDGER.md', '| U1 |'))
        rec('      ### MISS : row U1 not found')
        return 2
    n, cell = row[0]
    rec('      FACES_LEDGER.md:%d | row U1, one cell of %d characters' % (n, len(cell)))
    for mark in ('(i) THE CLAUSE', '(ii) THE HEIGHT', '(iii) THE WIDTH', '(iv) THE PRIME',
                 '(v) THE REPRESENTATION', '(vi) THE TYPE-D'):
        j = cell.find(mark)
        if j < 0:
            MISSES.append(('P1 site marker', 'FACES_LEDGER.md', mark))
            rec('      ### MISS : %r' % mark)
        else:
            rec('      site marker %-24s at character offset %5d in the cell' % (mark, j))
    rec('      ### **DECLARED, NOT CONCEALED:** the seat has ALREADY READ THIS CELL IN FULL, in the')
    rec('      ### re-sync turn two turns before this ferry, where a search returned it whole.')
    rec('      ### **SO NO PART OF COMPONENT 1 IS A FIRST READING**, and the expectations are scored')
    rec('      ### knowing it. ### The extraction rule is still fixed on the face before it is applied.')
    rec('')

    rec('(P2) G1 -- THE IDENTITY`S CHANNELS, AT b321`S OWN DEFINITION.')
    find(W, 'def channels(v, w):', 'P2 the generator function')
    find(W, 'the residual the source`s (148) requires to vanish'.replace('`', "'"),
         'P2 the identity in its own words')
    find(W, 'return dict(zero=Z, pole=P, arch=A, prime=PR,', 'P2 the range, as the function returns it')
    rec('')

    rec('(P3) G2 -- THE REGISTER PENTAGON OF SECTION 27.3, AT THE DEPOSIT`S OWN LIST.')
    find(FN, 'These are one premise in five registers', 'P3 the deposit`s list of five')
    find(FN, 'THE REGISTER SENTENCE, UNTOUCHED BY EVERY WORD BELOW', 'P3 the register sentence')
    dep = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
    if os.path.exists(dep):
        find(dep, 'one premise in five registers', 'P3 the deposited copy`s own line')
    else:
        rec('      ### the deposited copy is not at the expected path; the live quotation stands alone')
    rec('')

    rec('(P4) G3 -- THE STATED CLAUSE OF b332, AT ITS FINDINGS ADDRESS.')
    find(FN, '<a id="clause-stated"></a>', 'P4 the stable anchor')
    find(FN, '**(S)** For every `g` in the source', 'P4 the statement itself')
    # ### **THE NEEDLE WAS WRONG, NOT THE RECORD.** ### First form `| **K8** | the quantifiers`
    # ### MISSED: the table writes `| **K8** the quantifiers` with no pipe after the bolded id.
    # ### **BOTH YIELDS PRINTED**, the miss first, as the anchor rule requires.
    rec('      ### needle 1 `| **K8** | the quantifiers` -> MISS (the table carries no pipe after the id)')
    find(FN, '**K8** the quantifiers', 'P4 the constituent that names the quantifiers')
    rec('')

    rec('(P5) THE KINDS, AS THE ROW ITSELF TALLIES THEM.')
    m = re.search(r'THE TALLY, PRINTED SO NO READER HAS TO COUNT: KIND .{0,120}', cell)
    if not m:
        MISSES.append(('P5 the kind tally', 'FACES_LEDGER.md', 'THE TALLY'))
        rec('      ### MISS : the tally sentence')
    else:
        rec('      FACES_LEDGER.md:%d | %s' % (n, m.group(0)))
        rec('      ### **READ OFF IT AND NOTED HERE BECAUSE COMPONENT 3 DEPENDS ON IT:** the row records')
        rec('      ### **ZERO SITES OF KIND `(a)`**. ### The control as the order words it names a site')
        rec('      ### the record does not contain. ### **THE FACE FIXES WHAT HAPPENS THEN, BEFORE IT HAPPENS.**')
    rec('')

    rec('(P6) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '459'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|UNPARSED|next span STARTS AT|runs through', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
