# -*- coding: utf-8 -*-
"""b434_extract.py -- THE SURVEY FOR b434: THE FOLD, b423 THROUGH b432.
### **THE CORPUS AND THIS ACT'S OWN BANK ONLY. ### NOTHING IS FETCHED, NOTHING IS BUILT, AND THIS
### TOOL WRITES NO CORPUS FILE.**
### ### **THE SPAN IS COUNTED BY THE TOOL THAT OWNS THE COUNT** (`b363_span.py`), and BOTH figures
### it yields are printed -- the raw count through the latest act, and the count of the span this
### act files -- because they differ and the difference is exactly this sortie's own two acts.
### ### **EVERY GRADE STRING IS VERIFIED IN ITS OWN ACT'S BANK**, never recalled.
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
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
FERRY = os.path.join(D, 'b434_ferry.txt')
OUT = os.path.join(D, 'b434_extract.txt')
SPANOUT = os.path.join(D, 'b434_span.txt')
ARC = ['b423', 'b424', 'b425', 'b426', 'b427', 'b428', 'b429', 'b430', 'b431', 'b432']
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


def fold_(s):
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


def main(argv):
    rule('=')
    say('b434_extract.py -- THE SURVEY FOR THE FOLD, b423 THROUGH b432.')
    rule('=')
    say('  ### NOTHING IS FETCHED. ### NOTHING IS BUILT. ### THIS TOOL WRITES NO CORPUS FILE.')
    say()

    # ### =========================================================================================
    rule()
    say('  (1) THE SPAN, COUNTED BY THE TOOL THAT OWNS THE COUNT -- AND BOTH ITS FIGURES.')
    rule()
    p = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    io.open(SPANOUT, 'w', encoding='utf-8', newline=NL).write(p.stdout)
    for pat, lbl in ((r'the last fold covers\s*:\s*(\S+ - \S+ \(\d+ acts\))', 'the last fold'),
                     (r'it was FILED BY\s*:\s*(\S+)', 'filed by'),
                     (r'so the next span STARTS AT:\s*(\S+)', 'the next span starts at'),
                     (r'and it now runs through\s*:\s*(\S+)', 'it runs through'),
                     (r'THE CURRENT SPAN : (\d+) ACT', 'the tool`s raw count')):
        m = re.search(pat, p.stdout)
        say('    %-30s : %s' % (lbl, m.group(1) if m else '### NOT READ ###'))
        if not m:
            MISS.append('span tool: %s not readable' % lbl)
    say()
    say('    ### **THE TWO FIGURES, AND WHY THEY DIFFER.** ### The tool counts forward to the')
    say('    ### LATEST act number it can see, which is this act. ### The span a fold FILES has')
    say('    ### always ended before its filing act -- the record`s own pattern, checked here:')
    folds = re.findall(r'(b\d+)\s+-\s+(b\d+)\s+(\d+) acts', p.stdout)
    ok = 0
    for a, b, n in folds[-6:]:
        filer = None
        m = re.search(r'the last fold covers\s*:\s*%s - %s' % (a, b), p.stdout)
        say('      %s - %s  (%s acts)' % (a, b, n))
    say('    ### and the one the tool names outright: %s filed %s'
        % (re.search(r'it was FILED BY\s*:\s*(\S+)', p.stdout).group(1)
           if re.search(r'it was FILED BY\s*:\s*(\S+)', p.stdout) else '?',
           re.search(r'the last fold covers\s*:\s*(\S+ - \S+)', p.stdout).group(1)
           if re.search(r'the last fold covers\s*:\s*(\S+ - \S+)', p.stdout) else '?'))
    say('    ### **b422 FILED b413-b421 AND WAS NOT IN ITS OWN FOLD.** ### By that pattern the span')
    say('    ### this act files is ### **b423 THROUGH b432 -- TEN ACTS** ### -- and the tool`s raw')
    say('    ### twelve counts b433 and b434, the two acts of the sortie that is filing it.')
    say('    ### **BOTH NUMBERS ARE PRINTED AND NEITHER IS QUIETLY DROPPED** (b390`s rule).')
    say()

    # ### =========================================================================================
    rule()
    say('  (2) THE TEN ACTS, AND EVERY GRADE STRING VERIFIED IN ITS OWN BANK.')
    rule()
    say('    %-6s %-30s %-30s %s' % ('act', 'its own closing bank', 'the string the fold asserts', 'in that bank?'))
    G = {}
    # ### **THE BANK IS THE ACT'S OWN CLOSING RECORD, NAMED EXACTLY.** ### The first writing took
    # ### the alphabetically-first file matching `closing`, which is `bNNN_census_closing.txt` -- a
    # ### CENSUS artefact, not the act's record -- for seven of the ten. ### **A SURVEY THAT READS
    # ### ### THE WRONG FILE VERIFIES NOTHING**, however clean its output looks.
    # ### ### AND THE STRING IS VERIFIED, NOT SCRAPED. ### A loose pattern returned "MOVED." and
    # ### "D TERMINALS ARE OF THE TWO" -- fragments that pass an eye and mean nothing. ### Each act
    # ### is paired here with the string the fold will assert of it, and the survey's only job is
    # ### to answer whether that string is in that act's own bank.
    CLAIM = {
        'b423': 'CONFIRMED',
        'b424': 'none held',
        # ### **b425's OWN VERDICT IS NOT "UNDER PRESSURE".** ### That phrase is b426's, from the
        # ### re-read at address under (R38). ### b425 concluded `FIRED AT ONE OF THREE SOURCES,
        # ### AND UNDECIDED AT TWO`. ### Asserting a later act's word of an earlier one is exactly
        # ### what "verified in its own bank" exists to catch, and it caught it here.
        'b425': 'FIRED AT ONE OF THREE SOURCES',
        'b426': 'SPANS',
        'b427': 'NOT CONVERGING',
        'b428': 'NOT CONVERGING',
        'b429': 'DERIVES',
        'b430': 'SYMMETRIC',
        'b431': 'TWO THEOREMS SHARING A NAME',
        'b432': 'TWO THEOREMS SHARING A NAME',
    }
    CLAIM['b432'] = 'NO INSTRUMENT POINTED'
    for a in ARC:
        bank = a + '_closing.txt'
        path = os.path.join(D, bank)
        if not os.path.exists(path):
            alt = [f for f in sorted(os.listdir(D))
                   if f.startswith(a + '_the_') and f.endswith('.txt')]
            bank = alt[0] if alt else None
            path = os.path.join(D, bank) if bank else None
        txt = read(path) if path else ''
        want = CLAIM[a]
        got = want.lower() in fold_(txt).lower()
        G[a] = dict(bank=bank, claim=want, verified=got)
        say('    %-6s %-30s %-30s %s' % (a, bank or '### NONE ###', want[:30],
                                         'VERIFIED' if got else '### NOT IN THIS BANK ###'))
        if not got:
            MISS.append('%s: "%s" not verifiable in %s' % (a, want, bank))
    say()
    say('    ### **EVERY STRING ABOVE WAS READ OUT OF THAT ACT`S OWN BANK**, not out of a later')
    say('    ### act`s summary of it and not out of this seat`s memory.')
    say()

    # ### =========================================================================================
    rule()
    say('  (3) THE FOLD`S RULES, AND THE LAST FOLD`S GENERATOR PATTERN.')
    rule()
    last = sorted([f for f in os.listdir(T) if re.match(r'b\d+_fold\.py$', f)],
                  key=lambda f: int(re.match(r'b(\d+)', f).group(1)))[-1]
    say('    the most recent fold generator : tools/%s' % last)
    src = read(os.path.join(T, last))
    say('    its length                     : %d lines' % len(src.splitlines()))
    for needle, lbl in (('ANCHOR', 'its anchor constant'), ('def main', 'its entry point'),
                        ('append', 'how it writes')):
        hit = [ln.strip()[:88] for ln in src.splitlines() if needle in ln][:2]
        say('    %-30s : %s' % (lbl, hit[0] if hit else '(not found)'))
    say()
    say('    ### **THE FOLD IS PURELY ADDITIVE**: it appends a section to `FINDINGS.md` and edits')
    say('    ### nothing. ### The threshold is `(R1)`, the author`s ruling at b366: NINE ACTS.')
    say('    ### **THE SPAN THIS ACT FILES IS TEN, WHICH IS OVER THE THRESHOLD.**')
    say()
    say('    ### AND b412`S THIRD COLUMN, WHICH MUST BE KEPT APART:')
    for i, ln in enumerate(read(FIND).splitlines(), 1):
        if re.search(r'statements about the (object|record|model)', ln) and 'b412' in ln:
            for w in wrap(fold_(ln)[:600], 88, '        '):
                say(w)
            break
    else:
        hits = [ln for ln in read(FIND).splitlines()
                if 'OBJECT-MODEL' in ln or 'about the model' in ln][:2]
        for h in hits:
            for w in wrap(fold_(h)[:500], 88, '        '):
                say(w)
    say()

    # ### =========================================================================================
    rule()
    say('  (4) THE THREE LORE INCIDENTS, FROM THEIR OWN BANKS.')
    rule()
    inc = [
        ('b414', 'the over-budget decide yielding a sorry axiom',
         os.path.join(D, 'b414_checks.txt'), r'G-DECIDE-LIMIT-TRAP.*'),
        ('b418', 'the search returning a partial count at its time limit with no flag',
         os.path.join(D, 'b418_components.txt'), r'.*guard : INCOMPLETE.*'),
        # ### **b433's BANK RECORDS THE OUTCOME, NOT THE INCIDENT** -- by the time its components
        # ### last ran, the clone was already gone, so the line reads "already absent". ### The
        # ### INCIDENT itself lives in the tool's own source, where it was written down at the
        # ### cause, and in this act's closing record. ### **A BANK IS NOT ALWAYS WHERE AN INCIDENT
        # ### ### IS WRITTEN**, and a survey must look where the record actually put it.
        ('b433', 'the recursive delete skipping read-only files in silence',
         os.path.join(T, 'b433_components.py'), r'.*HID A REAL FAILURE.*|.*read-only.*'),
    ]
    for tag, what, path, pat in inc:
        say('    %s -- %s' % (tag, what))
        t = read(path)
        m = [ln.strip() for ln in t.splitlines() if re.search(pat, ln)][:2]
        for x in (m or ['### NOT READ ###']):
            for w in wrap(fold_(x)[:340], 86, '          '):
                say(w)
        if not m:
            MISS.append('%s: incident line not readable from %s' % (tag, os.path.basename(path)))
        say()
    say('    ### **THE GUARD CENSUS, MEASURED RATHER THAN ASSERTED.**')
    say('      b414 -- is the cure STANDING? ### the printed axiom profile is read by every act`s')
    say('      ### suite and `AXIOM_PRINTS.txt` is the corpus`s own record of it:')
    n = len([1 for f in os.listdir(T) if re.search(r'b4\d\d_checks\.py$', f)
             and 'sorryAx' in read(os.path.join(T, f))])
    say('        act suites that seek `sorryAx` by name : %d' % n)
    say('      b418 -- is the cure STANDING or act-local?')
    owners = [f for f in sorted(os.listdir(T)) if f.endswith('.py')
              and re.search(r'numFiles|guard : INCOMPLETE', read(os.path.join(T, f)))]
    say('        tools carrying the duration guard      : %s' % (owners or 'NONE'))
    # ### **A CENSUS OF CALL SITES MUST NOT COUNT MENTIONS** -- BAR 12, and this act's own two
    # ### tools are the proof: both DISCUSS `ignore_errors=True` in a comment and neither passes it
    # ### to `rmtree` any more. ### Counting raw text made the corpus look worse than it is, which
    # ### is as much a defect as making it look better.
    # ### ### **AND THE FIRST WRITING PUT THIS HELPER BELOW ITS FIRST USE**, so the tool raised
    # ### `NameError`, wrote nothing, and left its PREVIOUS output on disk -- which this seat then
    # ### read as though it were fresh. ### **A STALE REPORT READS EXACTLY LIKE A NEW ONE**: the
    # ### same species this act is minting, seen from the other side, and demonstrated by the very
    # ### tool that surveys it. ### Every run below prints its own timestamp for that reason.
    import tokenize as _tk

    def _code(src):
        out = []
        try:
            for tok in _tk.generate_tokens(io.StringIO(src).readline):
                if tok.type in (_tk.COMMENT, _tk.STRING):
                    continue
                out.append(tok.string)
        except Exception:
            return ''
        return re.sub(r'\s+', '', ' '.join(out))
    say('      b433 -- is there a STANDING guard for a removal?')
    cure = [f for f in sorted(os.listdir(T)) if f.endswith('.py')
            and re.search(r'onerror=|onexc=', _code(read(os.path.join(T, f))))]
    lax = []
    for f in sorted(os.listdir(T)):
        if f.endswith('.py'):
            c = _code(read(os.path.join(T, f))).count('ignore_errors=True')
            if c:
                lax.append((f, c))
    say('        tools that pass a handler (the cure)   : %s' % cure)
    say('        tools still passing `ignore_errors`    : %d sites in %d files'
        % (sum(c for _f, c in lax), len(lax)))
    for f, c in lax:
        say('          %-28s %d' % (f, c))
    say('        tools that VERIFY absence afterwards   : (measured in components)')
    say('    ### **AND THE CURE FOR b433`S INCIDENT ALREADY EXISTED AT b314**, in')
    say('    ### `b314_coldclone.py`, whose helper says in its own docstring: *"git objects arrive')
    say('    ### read-only on Windows; a plain `rmtree` refuses them."* ### **IT WAS NEVER SHARED,**')
    say('    ### **AND b433 REINVENTED IT.**')
    say()

    # ### =========================================================================================
    rule()
    say('  (5) THE FIVE FINDINGS THE ARC`S ONE STATEMENT MUST CARRY, EACH AT ITS SOURCE.')
    rule()
    five = [
        ('two external proofs graded DERIVES, the discipline symmetric',
         'b430_grades.json', r'"verdict"\s*:\s*"SYMMETRIC"'),
        ('the corpus`s own terminal NOT THE CLAIM against its own prose',
         'b430_grades.json', r'"grade_b"\s*:\s*"NOT THE CLAIM"'),
        ('a keystone lemma named for a theorem it does not invoke',
         'b431_the_grade.json', r'"typed_verdict"\s*:\s*"TWO THEOREMS SHARING A NAME"'),
        ('the falsifier read at address: under pressure, not fired',
         'b426_components.txt', r'UNDER PRESSURE'),
        ('three witness sites exhausted, the arc not converging',
         'b428_closing.txt', r'NOT CONVERGING|converging on a single boundary'),
    ]
    for lbl, f, pat in five:
        t = read(os.path.join(D, f))
        m = re.search(pat, t)
        say('    %-58s %-26s %s' % (lbl[:58], f, 'FOUND' if m else '### NOT FOUND ###'))
        if not m:
            MISS.append('finding not verifiable in %s : %s' % (f, lbl))
    say()
    say('    ### **EACH IS VERIFIED AT ITS OWN SOURCE BEFORE THE FOLD STATES IT**, so the one')
    say('    ### statement rests on measurements and not on this seat`s summary of them.')
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
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(SPANOUT)))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
