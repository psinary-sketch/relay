# -*- coding: utf-8 -*-
"""b441_extract.py -- THE SURVEY. ### **WRITTEN BEFORE THE FACE.**

### ### **IT READS AND CLASSIFIES; IT MEASURES NOTHING.** ### Every numeric identity, every second
### route and every git-history count belongs to the components, after the lock.
"""
import hashlib
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b441_extract.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
CC = os.path.join(D, 'b328_source_text.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, READS, MISS = [], [0], []
NL = chr(10)


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def wrap(s, n=86):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, clip=700, label=None):
    READS[0] += 1
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('      %s:%d' % (os.path.relpath(path, os.path.dirname(os.path.dirname(path)))
                               .replace(os.sep, '/'), i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip()[:clip], 84):
                    rec('        | %s' % c)
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), (label or needle)[:60]))
    rec('      ### **NOT LOCATED** : %s' % (label or needle)[:60])
    return None


def main():
    rec('=' * 100)
    rec('b441 -- THE IDENTIFICATION FILED, THE OVERSTATEMENT CORRECTED, AND TWO FILINGS. ### SURVEY.')
    rec('=' * 100)

    head(1, 'b440`S THREE NEAR LINES, EACH QUOTED WHOLE AT ITS OWN LINE')
    quote(os.path.join(PP, 'SPIRAL_MAP.md'), 'its `W` is a prime-power COUNTING FUNCTION', clip=900)
    quote(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                       'FINDINGS-archive-1-entries-through-2026-08-20c.md'),
          'NO open term: the odd-sector W_inf mass', after=1, clip=400)
    quote(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                       'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'),
          'the sign reconciliation', clip=520, label='the era-annotation line')

    head(2, 'THE WRITER, AND THE GRADE VOCABULARY IT WRITES IN')
    rec('    ### The corpus calls exactly one module `the writer`, and it writes `FACES_LEDGER.md`:')
    quote(os.path.join(PP, 'FACES_LEDGER.md'), 'Written through the writer', clip=260)
    rec('    ### and the ledger describes itself as the ledger of every equivalence or face:')
    quote(os.path.join(PP, 'FINDINGS.md'), 'is the ledger of every equivalence or face', clip=320)
    rec('    ### and the row the archimedean term was last graded under, by the same writer:')
    quote(T + os.sep + 'b333_filings.py', 'an UPDATE block through the writer', after=2, clip=200)
    src = read(os.path.join(T, 'b327_faces_row.py'))
    rec('    `b327_faces_row.py` public functions : %s'
        % ', '.join(re.findall(r'(?m)^def (\w+)\(', src)))
    led = read(os.path.join(PP, 'FACES_LEDGER.md'))
    fnd = read(os.path.join(PP, 'FINDINGS.md'))
    for g in ('MEASURED', 'MEASURED-ON-FAMILIES', 'MEASURED-AT-COVERED-CELLS', 'DERIVES-ON-IMPORTS',
              'DEFINED-ONLY'):
        rec('      grade %-28s ledger %-4d findings %d'
            % (g, len(re.findall(r'\b%s\b(?!-)' % re.escape(g), led)),
               len(re.findall(r'\b%s\b(?!-)' % re.escape(g), fnd))))
    rec('    ### **FINDINGS.md HAS NO WRITER MODULE:** it is written by appended addenda and folds,')
    rec('    ### generated from an act`s records (`b333_filings.py`, `b402_fold.py`).')

    head(3, 'SITE (ii)`S OWN FAILURE STEPS -- B3 AND B5, AS THE WRITER FILED THEM')
    quote(os.path.join(PP, 'FACES_LEDGER.md'), '| **B3** the density theorems', clip=900)
    quote(os.path.join(PP, 'FACES_LEDGER.md'), '| **B5** the Riemann-von Mangoldt main term', clip=600)
    quote(os.path.join(PP, 'FACES_LEDGER.md'), 'the witness would be **one argument serving every height**',
          clip=300, label='site (ii) cell')

    head(4, 'THE VERIFIED SOURCES -- WHAT THEY SAY ABOUT COUNTING, AND WHAT THEY DO NOT')
    quote(LAG, '(4) The counting function N', after=6, clip=200)
    quote(LAG, 'For the trivial representation', after=1, clip=200)
    quote(LAG, 'The zero-counting estimate in Theorem 2.1(4) implies', after=1, clip=200)
    for nm, p in (('Lagarias', LAG), ('CC', CC)):
        t = read(p)
        rec('      %-9s Riemann-Siegel theta: %d ; `theta(T)`: %d ; Stirling: %d ; `S(T)`: %d'
            % (nm, len(re.findall(r'Riemann.?Siegel', t)), len(re.findall(r'θ\s*\(\s*T', t)),
               len(re.findall(r'Stirling', t)), len(re.findall(r'\bS\s*\(\s*T\s*\)', t))))
    rec('    ### ### **THE COUNT ABOVE CONTRADICTED THIS FILE`S FIRST WRITING**, which printed that the')
    rec('    ### theta function is named in neither verified source. ### CC names it five times:')
    quote(CC, 'The function h`p', after=1, clip=200, label='eq. (153)')
    quote(CC, 'It is the derivative of 2', after=4, clip=200, label='eq. (154)')
    quote(CC, 'its derivative', after=0, clip=200, label='the O(log|s|) growth of theta prime')
    quote(CC, 'the derivative of the Riemann-Siegel angular function', after=0, clip=240,
          label='the transform of W_inf is delta-hat + 2 theta prime')
    rec('    ### ### **AND THE RECORD QUOTED (154) BEFORE THIS ACT** -- b333`s survey, in relay`s banks:')
    quote(os.path.join(D, 'b333_extract_notes.txt'), 'It is the derivative of 2', after=1, clip=240)
    t = read(CC)
    rec('      CC counting-law vocabulary : counting %d ; N(T) %d ; number of zeros %d'
        % (len(re.findall(r'counting', t)), len(re.findall(r'N\s*\(\s*T', t)),
           len(re.findall(r'number of zeros', t))))
    rec('    ### ### **SO THE KERNEL HALF (h+ = 2 theta prime) IS IN A VERIFIED SOURCE AND IN THE RECORD;')
    rec('    ### ### THE COUNTING HALF (theta/pi + 1 = the RvM main term) IS IN NEITHER.** ### b440 searched')
    rec('    ### PLACE-papers `.md` only, and its NOT CARRIED is scoped to that corpus.')

    head(5, 'THE PUSH-SIDE PREDICATE OF EVERY SUITE FROM b430 FORWARD')
    for n in range(430, 441):
        s = read(os.path.join(T, 'b%d_checks.py' % n))
        m = re.search(r'def _pushed\(\):(.*?)\n(?=\S)', s, re.S)
        body = m.group(1) if m else ''
        kind = ("branch -r --contains, SHA sought in names" if "'--contains'" in body else
                'merge-base --is-ancestor' if 'is-ancestor' in body else
                'rev-parse origin/main == HEAD' if "'origin/main'" in body else 'NOT LOCATED')
        rec('      b%d  %-40s pre %-5s post %s'
            % (n, kind, os.path.exists(os.path.join(D, 'b%d_checks.txt' % n)),
               os.path.exists(os.path.join(D, 'b%d_checks_postpush.txt' % n))))
    rec('    ### **READ AT THE WORKING TREE ONLY.** ### Whether b440`s COMMITTED first writing carried a')
    rec('    ### different predicate is a git-history question and belongs to the components.')

    head(6, 'THE GRADES, THE AXIOM SHORTHAND, AND WHERE TECHNE MODULES LIVE')
    quote(os.path.join(PP, 'README.md'), 'A theorem\'s axiom profile says nothing about whether', clip=200)
    quote(os.path.join(PP, 'README.md'), 'Axiom profiles are recorded at the corpus', after=2, clip=200)
    mods = os.path.join(TECHNE, 'modules', '2026-09')
    rec('      TECHNE-Core modules/2026-09 : %d files ; AXIOM_FORM present : %s'
        % (len(os.listdir(mods)) if os.path.isdir(mods) else -1,
           os.path.exists(os.path.join(mods, 'AXIOM_PROFILE_IS_PARTLY_FORM.md'))))

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
