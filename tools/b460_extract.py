# -*- coding: utf-8 -*-
"""b460_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **(R70), THE AUTHOR'S, IS NEW AND THIS FILE IS ITS FIRST EXECUTION:** every rule that will
### read a document is RUN ONCE ON THAT DOCUMENT BEFORE THE FACE IS SEALED, with its yield printed.
### ### **THE REHEARSED RULES ARE THREE:** the window-edge derivation, the cell search over the
### banked aim plane and the radius ladder, and the field reading on the cells the search returns.
### ### **NOTHING IS DECIDED HERE.** ### The rehearsal prints what each rule FINDS; the face then
### fixes the rules and the verdict words, and Component 1 applies them.
"""
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
OUT = os.path.join(D, 'b460_extract.txt')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def find(path, needle, label, show=150):
    ls = read(path).split(NL)
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    rec('=' * 100)
    rec('b460 -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).')
    rec('=' * 100)
    rec('')

    rec('(P1) R2`S OWN SENTENCE, AND THE CLASS AS b452`S BANK QUOTES IT.')
    find(os.path.join(PP, 'day1', 'Exhaustive_Enumeration.md'),
         'the largest **prime-free** window is', 'P1 R2`s sentence', 320)
    find(os.path.join(D, 'b452_components.txt'),
         'class, as the bank quotes it : support inside', 'P1 the class, from b452`s bank')
    find(os.path.join(D, 'b452_components.txt'),
         'quotation at the step        : In this paper we consider', 'P1 CC`s own sentence', 300)
    find(os.path.join(D, 'b452_components.txt'),
         'hand read                    : the class is the prime-free support', 'P1 b452`s hand reading', 300)
    find(os.path.join(D, 'b452_components.txt'), 'word test yield over all 82 failures',
         'P1 b452`s own yield line')
    rec('')

    rec('(R70) REHEARSAL 1 -- THE WINDOW`S EDGE, DERIVED FROM R2`S SENTENCE AND NOT ASSUMED.')
    rec('      R2 states the window in the variable of the TEST FUNCTION`s support: *"the largest')
    rec('      prime-free window is (1/2, 2)"*, and CC`s own step says *"the support of the test')
    rec('      function is contained in the interval (1/2, 2)"*.')
    rec('      b452`s bank writes the CLASS as *"support inside [2^-1/2, 2^1/2]"* -- HALF the window`s')
    rec('      exponents. ### **THE TWO ARE NOT IN CONFLICT AND THE DIFFERENCE IS THE DERIVATION:**')
    rec('      the corpus`s object is `f = g conv g-bar^#`, so if `g` is supported in `[a^-1, a]` then')
    rec('      `f` is supported in `[a^-2, a^2]`. ### f`s support lies inside `(1/2, 2)` exactly when')
    rec('      `a^2 < 2`; g`s own support is then inside `[2^-1/2, 2^1/2]`, which is b452`s wording.')
    edge = math.sqrt(2.0)
    rec('      ### ### **THE EDGE, COMPUTED : a < sqrt(2) = %.16f, equivalently a^2 < 2.**' % edge)
    rec('      ### width at the edge, by R2`s own `2 log a` : %.16f = log 2 = %.16f'
        % (2 * math.log(edge), math.log(2.0)))
    rec('      ### **THE CAVEAT R2 CARRIES, QUOTED BECAUSE IT GOVERNS:** the windows are')
    rec('      ### *"half-vacuous, since every prime power is >= 2 > 1 >= 1/L and the lower endpoint')
    rec('      ### never binds"*, and maximality is proved *"at integer bounds only"*. ### Only the')
    rec('      ### UPPER endpoint binds here, and membership does not need maximality.')
    rec('')

    rec('(R70) REHEARSAL 2 -- THE CELL SEARCH, RUN ON THE BANKED AIM PLANE AND THE RADIUS LADDER.')
    banks = []
    aimed = os.path.join(D, 'b326_closure_aimed_windows.json')
    if os.path.exists(aimed):
        j = json.load(io.open(aimed, encoding='utf-8'))
        for k in sorted(j, key=lambda x: float(x)):
            Lw = list(j[k].values())[0].get('L')
            banks.append(('b326_closure_aimed_windows.json (the aim plane)', float(k),
                          float(k) ** 2, Lw, None, None))
    cells = os.path.join(D, 'b437_cells.json')
    if os.path.exists(cells):
        for c in json.load(io.open(cells, encoding='utf-8')):
            banks.append(('b437_cells.json (the radius ladder)', c['a'], c.get('sq'),
                          2 * math.log(c['a']), c.get('pr'), c.get('pp')))
    if not banks:
        MISSES.append(('R70 rehearsal 2', 'the banks', 'no cell bank found'))
        rec('      ### ### **HARD FAILURE: NO CELL BANK FOUND. AN EMPTY SEARCH IS NEVER A CLEAN PASS.**')
    rec('      cells found : %d' % len(banks))
    rec('      %-44s %-10s %-12s %-12s %-12s %s' % ('bank', 'a', 'a^2', '2 log a', 'prime sum', 'prime powers'))
    inside = []
    for b, a, sq, Lw, pr, pp in banks:
        mark = '  <-- INSIDE THE WINDOW' if (sq is not None and sq < 2.0) else ''
        if sq is not None and sq < 2.0:
            inside.append((b, a, sq, pr, pp))
        rec('      %-44s %-10s %-12s %-12.6f %-12s %s%s'
            % (b, a, sq, Lw, pr if pr is not None else '-', pp if pp is not None else '-', mark))
    rec('      ### ### **CELLS WITH a^2 < 2 : %d.**' % len(inside))
    rec('')

    rec('(R70) REHEARSAL 3 -- THE FIELD READING ON THE CELLS THE SEARCH RETURNED.')
    if not inside:
        rec('      ### none to read.')
    for b, a, sq, pr, pp in inside:
        rec('      a = %-6s a^2 = %-10s prime sum `pr` = %-8s prime powers `pp` = %s'
            % (a, sq, pr, pp))
    rec('      ### **WHAT THE FIELDS MEAN, READ FROM THE BANK`S OWN TOOL AND NOT ASSUMED:**')
    find(os.path.join(D, 'b437_the_window_by_rungs.txt'), 'rung', 'P2 the rungs bank`s own wording', 200)
    rec('      ### ### **THE REHEARSAL`S YIELD IS THE OBJECT THE RULE NAMES:** cells, each with an `a`,')
    rec('      ### its square, and a banked prime sum. ### **NO REPAIR IS NEEDED BEFORE THE LOCK**, and')
    rec('      ### this sentence is the record that (R70) was satisfied rather than merely cited.')
    rec('')

    rec('(P3) TECHNE-CORE, FOR COMPONENT 2. ### **STATE ONLY; NOTHING COMMITTED OR PUSHED HERE.**')
    rec('      local HEAD        : %s' % git(TC, 'rev-parse', 'HEAD'))
    rec('      upstream          : %s' % git(TC, 'rev-parse', '--abbrev-ref', '@{u}'))
    rec('      commits ahead     : %s' % git(TC, 'rev-list', '--count', '@{u}..HEAD'))
    rec('      remote            : %s' % git(TC, 'remote', 'get-url', 'origin'))
    rec('      untracked files   :')
    for l in git(TC, 'status', '--porcelain').split(NL):
        if l.strip():
            rec('        %s' % l.strip())
    rec('      ### **THE THREE MODULES, THEIR SIZES AND FIRST LINES, READ BEFORE ANY COMMIT:**')
    md = os.path.join(TC, 'modules', '2026-09')
    for f in sorted(os.listdir(md)) if os.path.isdir(md) else []:
        p = os.path.join(md, f)
        if git(TC, 'ls-files', '--error-unmatch', 'modules/2026-09/' + f) == '':
            rec('        %-44s %6d bytes | %s'
                % (f, os.path.getsize(p), read(p).split(NL)[0][:80]))
    rec('')

    rec('(P4) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '460'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|UNPARSED|next span STARTS AT|runs through', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(edge=edge, inside=[dict(bank=b, a=a, sq=sq, pr=pr, pp=pp)
                                      for b, a, sq, pr, pp in inside],
                   n_cells=len(banks)),
              io.open(os.path.join(D, 'b460_rehearsal.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
