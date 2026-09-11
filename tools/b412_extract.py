# -*- coding: utf-8 -*-
"""b412_extract.py -- THE SURVEY. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **THE SPAN IS READ FROM THE TOOL AND NOT TYPED**, and the tool's number and the fold's
### number are ### **DIFFERENT OBJECTS**: the counter runs through the newest act in the record,
### and ### **THE FOLDING ACT IS NOT IN ITS OWN FOLD.** ### Both are printed.
###
### ### **AND THE ORIENTATION LAYER IS READ AT ITS OWN DATE BEFORE ANYTHING IS WRITTEN INTO IT** --
### how far behind each object is, measured from the newest act each names, not from its build line.
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
SUB = os.path.join(D, '_b412')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
OUT = os.path.join(D, 'b412_extract.txt')
ARCOUT = os.path.join(D, 'b412_arc.txt')
NL = chr(10)
ACT = 412

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


def newest_act(text):
    """### **THE NEWEST ACT A DOCUMENT NAMES, EXCLUDING HITS INSIDE A COMMIT HASH.**

    ### `b515e6b` is a git sha, not an act. ### The first version of this counter read it as one
    ### and reported a document current to an act that has not happened. ### **A MATCHER THAT
    ### ### CANNOT TELL AN ACT FROM A HASH IS MEASURING THE HEXADECIMAL ALPHABET.**
    """
    hits = []
    for m in re.finditer(r'\bb(\d{3})\b', text):
        tail = text[m.end():m.end() + 6]
        if re.match(r'^[0-9a-f]{2,}', tail):
            continue
        hits.append(int(m.group(1)))
    return (max(hits) if hits else None), sorted(set(hits))[-6:]


def main():
    if not os.path.isdir(SUB):
        os.makedirs(SUB)
    say('=' * 100)
    say('b412_extract.py -- THE SURVEY. ### EVERY READ ANCHORED, EVERY MISS COUNTED.')
    say('=' * 100)

    # ---------------------------------------------------------------- (A) THE SPAN
    say()
    bar()
    say('### (A) THE SPAN, READ FROM THE TOOL AND NOT TYPED.')
    bar()
    sp = io.open(os.path.join(D, 'b412_span.txt'), encoding='utf-8').read()
    for ln in sp.split(NL):
        if re.search(r'the last fold covers|it was FILED BY|so the next span|and it now runs|'
                     r'THE CURRENT SPAN', ln):
            say('      %s' % ln.strip())
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', sp)
    tool_n = int(m.group(1)) if m else None
    say('  ### ### **THE TOOL SAYS `%s`. ### THE FOLD`S SPAN IS `%s`.**'
        % (tool_n, (tool_n - 1) if tool_n else '?'))
    say('  ### ### **THE DIFFERENCE IS NOT A DISAGREEMENT.** ### The counter runs through the')
    say('  ### newest act IN THE RECORD, and this act is in the record because its ferry is')
    say('  ### banked. ### **THE FOLDING ACT IS NOT IN ITS OWN FOLD** -- `b402` filed `b385`-`b401`')
    say('  ### and stood outside it, and this act stands outside `b403`-`b411` the same way.')

    # ---------------------------------------------------------------- (B) THE FOLDS
    say()
    bar()
    say('### (B) EVERY FOLD THE RECORD CARRIES, AND ITS OWN ONE-STATEMENT.')
    bar()
    ftxt = io.open(FIND, encoding='utf-8', errors='replace').read()
    lines = ftxt.split(NL)
    heads = [(i + 1, ln) for i, ln in enumerate(lines)
             if re.match(r'^##+ .*(ARC|FOLD)', ln) and 'Addendum' not in ln]
    arcs = []
    for ln, h in heads:
        rng = re.search(r'b(\d{3})\s*[-–]+\s*b?(\d{3})', h)
        # ### the one-statement sits under the section's own `### The arc's one statement`
        stmt, j = None, ln
        while j < len(lines) and not re.match(r'^##[^#]', lines[j]):
            if re.match(r'^###\s+The arc.s one statement', lines[j]):
                k = j + 1
                while k < len(lines) and not lines[k].strip():
                    k += 1
                stmt = lines[k] if k < len(lines) else None
                break
            j += 1
        arcs.append(dict(line=ln, head=h.lstrip('# ').strip(),
                         lo=int(rng.group(1)) if rng else None,
                         hi=int(rng.group(2)) if rng else None, stmt=stmt))
    say('  ### ### **FOLD SECTIONS FOUND : %d.**' % len(arcs))
    for a in arcs:
        say('      line %-5d %-62s span %s-%s  one-statement %s'
            % (a['line'], a['head'][:62], a['lo'], a['hi'],
               'YES' if a['stmt'] else '### NONE ###'))
    write_text(os.path.join(SUB, 'arcs.txt'),
               NL.join('%d\t%s\t%s\t%s' % (a['line'], a['head'], a['lo'], a['hi'])
                       for a in arcs) + NL)

    # ---------------------------------------------------------------- (C) THE DIGEST
    say()
    bar()
    say('### (C) THE DIGEST, READ AT ITS OWN DATE.')
    bar()
    dtxt = io.open(DIGEST, encoding='utf-8', errors='replace').read()
    dlines = len(dtxt.split(NL))
    pull(DIGEST, '# The findings as they stand', 'ITS TITLE')
    pull(DIGEST, '**Built 2026-08-25', 'ITS BUILD LINE', save='digest_build.txt')
    dn, dlast = newest_act(dtxt)
    say('  ### ### **LINES : %d.** ### **NEWEST ACT IT NAMES : `b%s`.** ### Its last few: %s'
        % (dlines, dn, ', '.join('b%d' % x for x in dlast)))
    say('  ### ### ### **SO THE DIGEST IS `%d` ACTS BEHIND** ### (`b%s` -> `b%d`).'
        % (ACT - dn, dn, ACT))
    arcs_after = [a for a in arcs if a['lo'] and a['lo'] > dn]
    say('  ### ### **ARCS FOLDED SINCE THE DIGEST`S NEWEST ACT : %d.**' % len(arcs_after))
    for a in arcs_after:
        say('      b%s-b%s  %s' % (a['lo'], a['hi'], a['head'][:66]))

    # ---------------------------------------------------------------- (D) THE FIVE DOORS
    say()
    bar()
    say('### (D) THE FIVE-DOOR STATE, READ AT ITS OWN DATE.')
    bar()
    ptxt = io.open(PATHS, encoding='utf-8', errors='replace').read()
    pull(PATHS, '**THE FIVE-DOOR STATE — standing orientation object', 'ITS HEAD',
         save='doors_head.txt')
    plines = ptxt.split(NL)
    ph = [i for i, ln in enumerate(plines) if '**THE FIVE-DOOR STATE' in ln]
    rows = []
    if ph:
        for ln in plines[ph[0]:ph[0] + 14]:
            if ln.startswith('| **') or ln.startswith('| Door'):
                rows.append(ln)
    say('  ### ### **DOOR-TABLE ROWS : %d.**' % len([r for r in rows if r.startswith('| **')]))
    for r in rows:
        cells = [c.strip() for c in r.split('|')]
        if len(cells) > 3:
            say('      %-16s %-30s %s' % (cells[1][:16], cells[2][:30], cells[3][:78]))
    write_text(os.path.join(SUB, 'doors.txt'), NL.join(rows) + NL)
    # ### **THE NEWEST ACT THE DOOR BLOCK ITSELF NAMES**, not the whole document.
    blk = NL.join(plines[ph[0]:ph[0] + 14]) if ph else ''
    bn, _ = newest_act(blk)
    pn, plast = newest_act(ptxt)
    say('  ### ### **NEWEST ACT THE DOOR BLOCK NAMES : %s.** ### Newest the whole document names :'
        % ('`b%d`' % bn if bn else '**NONE -- the block names no act at all**'))
    say('  ### `b%s` (its last few: %s).' % (pn, ', '.join('b%d' % x for x in plast)))
    say('  ### ### ### **SO THE FIVE-DOOR STATE IS `%d` ACTS BEHIND** ### on the document`s own'
        % (ACT - pn))
    say('  ### newest act, and the door table itself carries ### **NO ACT NUMBER AT ALL** -- its')
    say('  ### currency is readable only from the kernel pins it cites.')
    say()
    say('  ### **AND THE TWO MOVEMENTS THE FERRY EXPECTS, CHECKED AGAINST THE TABLE AS IT STANDS:**')
    for lbl, pat in (("R4`s finite-set conjunct", r'finite-set conjunct now DERIVES'),
                     ("R5`s compiled boundary marker", r'compiled boundary marker'),
                     ("R5`s `certifiedInput_not_zeroRealizing`",
                      r'certifiedInput_not_zeroRealizing')):
        present = bool(re.search(pat, blk))
        say('      %-42s ALREADY IN THE TABLE : ### **%s**' % (lbl, present))

    # ---------------------------------------------------------------- (E) THE ARC'S OWN BANKS
    say()
    bar()
    say('### (E) THE ARC`S NINE ACTS, EACH READ FROM ITS OWN BANK.')
    bar()
    banks = {}
    for n in range(403, 412):
        cands = [f for f in sorted(os.listdir(D))
                 if f.startswith('b%d_' % n) and f.endswith('.txt')
                 # ### **`_original` AND `_notes` ARE PRESERVED COPIES, NOT BANKS.** ### The
                 # ### first version of this finder took `b403_readme_original.txt` -- a
                 # ### README preserved verbatim by that act -- as `b403`'s bank, because
                 # ### it sorts first. ### **A FINDER THAT TAKES THE ALPHABETICALLY FIRST
                 # ### ### SURVIVOR IS NOT IDENTIFYING ANYTHING.**
                 and not re.search(r'_(checks|census|pins|ferry|reg|lockgate|satisfiable|'
                                   r'desk_notes|extract|components|closing|mirror|audit|'
                                   r'index_query|span|scheme_table|numbering|classification|'
                                   r'original|notes|query|stdout)', f)]
        banks[n] = cands[0] if cands else None
        say('      b%d  %s' % (n, cands[0] if cands else '### NO BANK FOUND ###'))
        if not cands:
            MISS.append('b%d has no locatable bank' % n)
    write_text(os.path.join(SUB, 'banks.txt'),
               NL.join('b%d\t%s' % (k, v) for k, v in banks.items()) + NL)

    # ---------------------------------------------------------------- (F) DID THE ARC MOVE A DOOR?
    say()
    bar()
    say('### (F) DID THE ARC MOVE A DOOR? ### SEARCHED BY DESCRIPTION, WITH A POSITIVE CONTROL.')
    bar()
    say('  ### **THE PREDICATE, FIXED BEFORE THE SEARCH:** ### a sentence in an arc act`s bank')
    say('  ### that states a NEW DEPTH for one of the five registers -- a compiled terminal, a')
    say('  ### certificate, a disproof or a named premise discharged. ### **NOT** ### a sentence')
    say('  ### that merely mentions a register`s name.')
    pats = {
        'names a register R1-R5 at all': r'\bR[1-5]\b',
        'names the goal state or the pentagon': r'goal state|RegisterPentagon|pentagon',
        'claims a door moved': r'door (?:is )?(?:now|moved)|new depth|nearer|closer to the goal',
        'claims a terminal compiled by this arc': r'now (?:DERIVES|compiles)|newly compiled',
    }
    for lbl, pat in pats.items():
        hits = []
        for n, f in banks.items():
            if not f:
                continue
            src = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
            c = len(re.findall(pat, src))
            if c:
                hits.append('b%d(%d)' % (n, c))
        say('      %-42s %s' % (lbl, ', '.join(hits) if hits else '### **0 ACROSS THE SPAN**'))
    say('  ### ### **THE POSITIVE CONTROL -- A WORD THE ARC CERTAINLY USES MUST BE FOUND BY THE')
    say('  ### ### SAME MACHINERY:** ### `h2`.')
    ctl = [n for n, f in banks.items() if f and 'h2' in io.open(
        os.path.join(D, f), encoding='utf-8', errors='replace').read()]
    say('      the control (`h2` in an arc bank) : ### **%d of 9 acts** ### -- ### **%s**'
        % (len(ctl), 'PASSES' if ctl else 'FAILS: THE VERDICT IS WITHHELD'))
    if not ctl:
        MISS.append('the positive control on the door search yielded 0')

    say()
    bar('=')
    say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
    for m2 in MISS:
        say('      %s' % m2)
    bar('=')
    write_text(OUT, NL.join(L) + NL)
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
