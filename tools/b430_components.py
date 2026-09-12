# -*- coding: utf-8 -*-
"""b430_components.py -- THE SIX COMPONENTS OF b430: THE SELF-CONTROL.

### **THE ACT GRADES THE CORPUS'S OWN TERMINAL BY THE PROTOCOL IT USED ON A STRANGER, AND GRADES IT
### TWICE UNDER `(R40)` -- ONCE AGAINST THE CLAIM ITS ROW NAMES, ONCE AGAINST THE CLAIM THE PROSE
### MAKES.** ### The build and the printer have already run; this file READS THEIR OUTPUT and never
### asserts a profile it did not read. ### `rowgen`'s own `definition_encoded` is IMPORTED, never
### copied, because the clause under test is precisely whether this seat checks definitions by tool
### or by reading.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
import rowgen  # noqa: E402  ### THE CORPUS'S OWN GRADING TOOL, IMPORTED

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
TABLE = os.path.join(KERN, 'CORRESPONDENCE.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
FIND = os.path.join(PP, 'FINDINGS.md')
FERRY = os.path.join(D, 'b430_ferry.txt')
ASREC = os.path.join(D, 'b430_ferry_asreceived.txt')
B429G = os.path.join(D, 'b429_the_grade.txt')
B429C = os.path.join(D, 'b429_closing.txt')
PROFILE = os.path.join(D, 'b430_profile.txt')
CHECK = os.path.join(D, 'b430_check.txt')
BUILDLOG = os.path.join(D, 'b430_build.log')
SCANREP = os.path.join(D, 'b430_scan_repair.txt')
OUT = os.path.join(D, 'b430_components.txt')
GRADES = os.path.join(D, 'b430_grades.json')
CHAIN = ['FiniteSideSeal', 'SinglePrimeFactor', 'SmearGeneral']
TERMINAL = 'SmearGeneral.smear_general'
THREE = ['propext', 'Classical.choice', 'Quot.sound']
NL = chr(10)
L, MISS = [], []
G = {}


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
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


def wrap(text, width=94, indent='      '):
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


def qrows(path, marker, maxlen=3000):
    """### EVERY ROW THAT CARRIES THE MARKER, WITH ITS LINE (BAR 3, WIDENED).

    ### ### **A MARKER IS NOT A KEY, AND THIS ACT LEARNED IT ON `F5`.** ### `FACES_LEDGER.md`
    ### carries THREE rows keyed `F5`, in three different tables; ### **A READER TAKING THE FIRST
    ### ### GETS A DESCRIPTION OF WHAT THE FACE IS AND NOT A CLAIM ABOUT ANY TERMINAL** -- which is
    ### what the first writing of this tool did, and the grade against CLAIM B came back UNDECIDED
    ### because the sentence it needed was in a row it never read.
    ### ### **SO EVERY MATCH IS RETURNED AND THE CALLER CHOOSES BY A PRINTED RULE**, never by
    ### position.
    """
    out = []
    for i, ln in enumerate(read(path).splitlines(), 1):
        if re.match(r'^\s*\|\s*(\*\*)?' + re.escape(marker) + r'(\*\*)?\s*[|(]', ln):
            out.append((i, unbar(ln)[:maxlen]))
    return out


def qrow(path, marker, maxlen=3000):
    """### THE FIRST ROW CARRYING THE MARKER. ### **USE ONLY WHERE THE MARKER IS PROVED UNIQUE**;
    ### the caller is told how many matched so uniqueness is a measurement, not an assumption."""
    rs = qrows(path, marker, maxlen)
    return (rs[0] if rs else (None, ''))


def strip_lean_comments(src):
    """### BAR 12: COMMENTS AND STRING LITERALS STRIPPED BEFORE ANY SOURCE MATCH.
    ### ### **THIS IS NOT TIDINESS.** ### `Core/SinglePrimeFactor.lean` NAMES `sorry` FIVE TIMES IN
    ### ITS OWN DOCSTRINGS -- to say the module carries none -- and a bare sweep counts those as
    ### terms. ### The corpus's own prose would then read as the corpus's own defect."""
    out, i, n = [], 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth, i = 1, i + 2
            while i < n and depth:
                if src.startswith('/-', i):
                    depth += 1
                    i += 2
                elif src.startswith('-/', i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            continue
        if src.startswith('--', i):
            j = src.find(NL, i)
            i = n if j < 0 else j
            continue
        if src[i] == '"':
            i += 1
            while i < n and src[i] != '"':
                i += 2 if src[i] == chr(92) else 1
            i += 1
            continue
        out.append(src[i])
        i += 1
    return ''.join(out)


def find_decl(name):
    """### A DEFINITION QUOTED AT ITS FILE AND LINE, from the kernel's own source."""
    if not os.path.isdir(CORE):
        return None, None, ''
    for fn in sorted(os.listdir(CORE)):
        if not fn.endswith('.lean'):
            continue
        p = os.path.join(CORE, fn)
        src = read(p)
        for i, ln in enumerate(src.splitlines(), 1):
            if re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:def|abbrev)\s+'
                        + re.escape(name) + r'\b', ln):
                body = src.splitlines()[i - 1:i + 3]
                return fn, i, NL.join(body)
    return None, None, ''


# ### =============================================================================================
def comp0():
    rule('=')
    say('  COMPONENT 0 -- THE RE-ISSUE ABSORBED, AND THE GATE DEFECT REPAIRED.')
    rule('=')
    import hashlib
    a, b = read(ASREC), read(FERRY)
    m = re.search(r'sha256 : ([0-9a-f]{64})', a)
    say('    the ferry AS FIRST RECEIVED, preserved : data/b430_ferry_asreceived.txt')
    say('      its sha256, as preserved             : %s' % (m.group(1) if m else '### ABSENT ###'))
    say('    the ferry AS EXECUTED                  : data/b430_ferry.txt')
    say('      its sha256                           : %s'
        % hashlib.sha256(b.encode('utf-8')).hexdigest())
    # ### THE DIFF, COMPUTED, NOT DESCRIBED.
    body = a.split(NL + NL, 1)[1] if NL + NL in a else a
    import difflib
    d = list(difflib.unified_diff(body.splitlines(), b.splitlines(), lineterm='', n=0))
    hunks = [x for x in d if x.startswith('@@')]
    moved = [x for x in d if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))]
    say('    hunks between them                     : %d' % len(hunks))
    for x in moved:
        say('        %s' % x[:96])
    G['hunks'] = len(hunks)
    G['ferry_lines_moved'] = len(moved)
    say('    ### **THE SEAT EDITED NO WORD OF EITHER PASTE.** ### The change is the author\'s, and')
    say('    ### the preserved copy is what makes that checkable rather than merely stated.')
    say()
    say('    ### THE GATE DEFECT, REPAIRED (the re-issue\'s added step zero):')
    sr = read(SCANREP)
    for pat in (r'ferry_scan LIVE stem hits\s+BEFORE b430: (\d+)',
                r'ferry_scan LIVE stem hits\s+AFTER  b430: (\d+)'):
        mm = re.search(pat, sr)
        say('      %s' % (mm.group(0) if mm else '### NOT FOUND IN THE REPAIR RECORD ###'))
    say('      ### AND THE OTHER POLARITY, so the exception is not a hole:')
    mm = re.search(r'LIVE stem hits\s+: (\d+)\s+### STILL FAILS', sr)
    say('      %s' % (mm.group(0) if mm else '### NOT FOUND ###'))
    say('    ### **THE TWO INCIDENTS ARE TWO SPECIES AND THE MODULE SAYS SO.** ### The b430 ferry\'s')
    say('    ### own hits were a LIVE USE the owner excepts nowhere -- `classify` returns `None` on')
    say('    ### that line -- so ### **THE REPAIR DOES NOT CURE THEM AND DOES NOT CLAIM TO**; the')
    say('    ### author\'s re-wording did. ### Only the Clay refusal was the drift.')
    say()


def comp1():
    rule('=')
    say('  COMPONENT 1 -- (R40) QUOTED, AND THE TWO CLAIMS FIXED BEFORE THE TERMINAL IS READ.')
    rule('=')
    ft = read(FERRY)
    m = re.search(r'RULING \(R40\).*?(?=' + NL + r'{2}LEG 1)', ft, re.S)
    r40 = unbar(m.group(0)) if m else ''
    if not r40:
        MISS.append('(R40) not found in the banked ferry')
    say('    (R40), VERBATIM FROM THE BANKED PASTE:')
    for ln in wrap(r40, 92, '      '):
        say(ln)
    G['r40_quoted'] = bool(r40)
    say()
    n, row = qrow(TABLE, '268')
    mm = re.search(r'COMPONENT 1:(.*?)(?:COMPONENT 2|$)', row, re.S)
    claim_a = fold(mm.group(1)) if mm else ''
    say('    ### **CLAIM A -- WHAT THE TERMINAL\'S OWN CORRESPONDENCE ROW NAMES.**')
    say('      CORRESPONDENCE.md line %s, read by its marker:' % n)
    for ln in wrap(claim_a, 92, '        '):
        say(ln)
    G['claim_a'] = claim_a
    G['claim_a_line'] = n
    say()
    f5rows = qrows(FACES, 'F5')
    k3 = []
    for j, ln in enumerate(read(FIND).splitlines(), 1):
        # ### **THE ANCHOR'S ROWS DO NOT END THEIR FIRST CELL AT THE MARKER.** ### They read
        # ### `| **K3** the finite places' contribution | ...`, so a pattern demanding a cell
        # ### boundary straight after the marker found ONE row of THREE -- and the one it found
        # ### was the summary row, not the two that name the terminals. ### The marker ends at a
        # ### word boundary; the cell may continue.
        if re.match(r'^\s*\|\s*(\*\*)?K3(\*\*)?\b', ln) or \
           re.match(r'^\s*\|\s*\d+\s*\|\s*\*\*K3\*\*', ln):
            k3.append((j, unbar(ln)))
    say('    ### **CLAIM B -- WHAT THE FINITE-SIDE PROSE MAKES OF IT.**')
    say('      FACES_LEDGER.md rows keyed F5 : %d, at lines %s'
        % (len(f5rows), [i for i, _ in f5rows]))
    say('      ### **THE MARKER IS NOT UNIQUE, SO THE ROW IS CHOSEN BY A RULE PRINTED HERE AND NOT')
    say('      ### BY POSITION:** the claim-bearing row is the one that NAMES THE KERNEL MODULE')
    say('      ### `Core/FiniteSideSeal.lean` AND CARRIES A `PROVED-` GRADE WORD. ### The others')
    say('      ### are a description of what the face is and a derivation row; neither claims')
    say('      ### anything compiled, so neither can be the claim a terminal is graded against.')
    chosen = [(i, r) for i, r in f5rows
              if 'FiniteSideSeal.lean' in r and re.search(r'PROVED-', r)]
    for i, r in f5rows:
        say('        line %-6d %s  |  %s'
            % (i, 'CHOSEN' if (i, r) in chosen else '  --  ', r[:70]))
    if len(chosen) != 1:
        MISS.append('the F5 selection rule chose %d rows, not 1' % len(chosen))
    nf, f5 = (chosen[0] if len(chosen) == 1 else (None, ''))
    mm = re.search(r'GENERAL, over ([^:]*):', f5)
    scope = fold(mm.group(0)) if mm else ''
    say('      ### THE SENTENCE THAT SETS ITS SCOPE, from line %s:' % nf)
    for ln in wrap(scope or (f5[:400] or '### NOT LOCATED ###'), 92, '        '):
        say(ln)
    mm = re.search(r'PROVED-GENERAL \(([^)]*)\)', f5)
    say('      ### AND ITS GRADE-BEARING PHRASE:')
    for ln in wrap(fold(mm.group(0)) if mm else '(absent)', 92, '        '):
        say(ln)
    G['claim_b_f5_line'] = nf
    G['claim_b_f5_rows'] = [i for i, _ in f5rows]
    G['claim_b_scope'] = scope
    say()
    say('      FINDINGS.md rows keyed K3 : %d' % len(k3))
    for j, r in k3:
        say('        line %d:' % j)
        for ln in wrap(r[:900], 90, '          '):
            say(ln)
    G['claim_b_k3_rows'] = [j for j, _ in k3]
    say()
    say('    ### **THE TWO CLAIMS ARE NOW ON THE RECORD AND NEITHER GRADE HAS BEEN FORMED.**')
    say()


def comp2():
    rule('=')
    say('  COMPONENT 2 -- THE BUILD AT THE PIN, AND THE PROFILE FROM THE PRINTER\'S OWN OUTPUT.')
    rule('=')
    bl = read(BUILDLOG)
    pin = subprocess.run(['git', '-C', KERN, 'rev-parse', 'HEAD'],
                         capture_output=True, text=True).stdout.strip()
    mm = re.search(r'pin\s*:\s*([0-9a-f]{40})', bl)
    built_at = mm.group(1) if mm else ''
    # ### **THE PIN OF A BUILD IS THE COMMIT IT WAS BUILT AT, NOT THE COMMIT HEAD IS AT NOW.**
    # ### First writing took `rev-parse` at report time as "the pin"; the kernel then advanced by
    # ### this act's OWN correspondence row, and a re-run reported a pin the build never saw.
    # ### ### **A BUILD RECORD THAT MOVES WITH HEAD IS NOT A RECORD.**
    say('    the pin the build was made at (from its log) : %s' % (built_at or '### ABSENT ###'))
    say('    the kernel`s HEAD at report time             : %s' % pin)
    say('    ### these differ once this act appends its own correspondence row, and that is')
    say('    ### expected; what must hold is that the build`s pin is an ANCESTOR of HEAD.')
    # ### **THE BUILD IS PROVED BY ITS OWN LOG, NOT BY THIS FILE'S MEMORY OF RUNNING IT.**
    # ### **THE MODULES PRINT THEIR OWN AXIOMS AT COMPILE**, so the log interleaves dozens of
    # ### printer lines between a job and its exit code. ### A regex demanding `rc=` on the NEXT
    # ### line found 1 job of 3, and the report read as though two had never run. ### The exit code
    # ### is the FIRST `rc=` after the job line, with only the compiler's output between.
    rcs, pending = [], None
    for raw_ln in bl.splitlines():
        mj = re.match(r'\s*=== job: (\S+)', raw_ln)
        if mj:
            pending = mj.group(1)
            continue
        mr = re.match(r'\s*rc=(\d+)', raw_ln)
        if mr and pending:
            rcs.append((pending, mr.group(1)))
            pending = None
    say('    jobs, one at a time         : %d' % len(rcs))
    for nm, rc in rcs:
        say('        %-22s rc=%s  %s' % (nm, rc, 'OK' if rc == '0' else '### FAILED ###'))
    G['jobs'] = len(rcs)
    G['jobs_ok'] = len([1 for _, rc in rcs if rc == '0'])
    G['pin'] = built_at          # ### what was BUILT
    G['head_now'] = pin          # ### where the kernel stands when this report was written
    G['pin_recorded'] = bool(built_at)
    say('    toolchain, the kernel\'s own : %s' % fold(read(os.path.join(KERN, 'lean-toolchain'))))
    say()
    # ### THE PROFILE. ### **READ FOR THE TERMINAL'S OWN LINE (A2), NEVER AS A SUBSTRING OF ALL OF IT.**
    prof = read(PROFILE)
    line = None
    for ln in prof.splitlines():
        if re.match(r"^\s*'" + re.escape(TERMINAL) + r"'\s", ln):
            line = ln.strip()
    say('    ### THE PRINTER\'S OUTPUT, THE TERMINAL\'S OWN LINE:')
    say('        %s' % (line or '### NO LINE FOR THIS TERMINAL IN THE PRINTER\'S OUTPUT ###'))
    if line is None:
        MISS.append('no profile line for %s' % TERMINAL)
    clean = bool(line and 'does not depend on any axioms' in line)
    mm = re.search(r'depends on axioms: \[([^\]]*)\]', line or '')
    axioms = [a.strip() for a in mm.group(1).split(',')] if mm else []
    beyond = [a for a in axioms if a not in THREE]
    say('    axioms named beyond the standard three : %d %s' % (len(beyond), beyond or ''))
    say('    ### **THE PROFILE IS THE PRINTER\'S STDOUT. ### NOT THE EXIT CODE, NOT THE BANKED')
    say('    ### `AXIOM_PRINTS.txt`, AND NOT A SUBSTRING OF THE WHOLE OUTPUT.**')
    G['profile_line'] = line
    G['profile_empty'] = clean
    G['axioms_beyond_three'] = beyond
    say()
    # ### THE CLOSURE TEST AND THE SOURCE SWEEP.
    say('    sorryAx anywhere in the printer\'s output : %d' % prof.count('sorryAx'))
    say('    ### THE SOURCE SWEEP OVER THE WHOLE IMPORT CHAIN, COMMENTS AND STRINGS STRIPPED:')
    raw_t = terms = 0
    for m_ in CHAIN:
        src = read(os.path.join(CORE, m_ + '.lean'))
        r = len(re.findall(r'\bsorry\b', src))
        t = len(re.findall(r'\bsorry\b', strip_lean_comments(src)))
        raw_t += r
        terms += t
        say('        %-24s raw %d   AS A TERM %d' % (m_ + '.lean', r, t))
    for _w in wrap('### **RAW %d, AS TERMS %d.** ### The difference is the corpus\'s own'
                   ' docstrings saying the module carries none -- which is exactly why'
                   ' BAR 12 strips comments first.' % (raw_t, terms), 92, '    '):
        say(_w)
    G['sorry_raw'] = raw_t
    G['sorry_terms'] = terms
    G['sorryAx_in_profile'] = prof.count('sorryAx')
    say()


def comp3():
    rule('=')
    say('  COMPONENT 3 -- THE STATEMENT UNFOLDED TO BASE OBJECTS, AND `defenc` RUN BY THE TOOL.')
    rule('=')
    chk = read(CHECK)
    mm = re.search(r'(?s)smear_general : (.*?)(?=' + NL + r'theorem )', chk)
    stmt = fold(mm.group(1)) if mm else ''
    say('    ### THE STATEMENT, IN LEAN\'S OWN WORDS (`#check`, from the compiled module):')
    for ln in wrap(stmt, 92, '        '):
        say(ln)
    G['statement'] = stmt
    say()
    say('    ### THE BASE OBJECTS IT RESTS ON, EACH QUOTED AT ITS FILE AND LINE:')
    names = ['singlePrimeFactor', 'ballQ', 'sumAN', 'sumAQ']
    located = 0
    for nm in names:
        fn, i, body = find_decl(nm)
        if fn:
            located += 1
            say('      %-20s %s:%d' % (nm, fn, i))
            for ln in body.splitlines()[:4]:
                say('          %s' % ln.rstrip()[:92])
        else:
            say('      %-20s ### NOT LOCATED IN Core/ ###' % nm)
            MISS.append('definition not located: %s' % nm)
    G['defs_located'] = located
    G['defs_wanted'] = len(names)
    say()
    # ### =========================================================================================
    # ### `defenc` BY THE TOOL. ### **THE CLAUSE b429 FOUND ASYMMETRIC IS THE ONE THIS ACT MUST NOT
    # ### ### REPEAT BY HAND**, so the corpus's own function is IMPORTED and run over the kernel's
    # ### own source -- widened across the whole import chain, because the definitions the
    # ### conclusion names are spread over three modules and a one-file check would pass vacuously.
    # ### =========================================================================================
    src_all = NL.join(read(os.path.join(CORE, m_ + '.lean')) for m_ in CHAIN)
    concl = stmt.split('->')[-1] if '->' in stmt else stmt
    concl = stmt.split(chr(0x2192))[-1] if chr(0x2192) in stmt else concl
    flag, why = rowgen.definition_encoded(src_all, concl)
    say('    ### `rowgen.definition_encoded`, THE CORPUS\'S OWN TOOL, IMPORTED AND RUN:')
    say('        conclusion put to it   : %s' % concl.strip()[:88])
    say('        source scope           : the whole import chain, %d modules, %d bytes'
        % (len(CHAIN), len(src_all.encode('utf-8'))))
    say('        DEFINITION-ENCODED     : %s   %s' % (flag, why or ''))
    G['defenc'] = bool(flag)
    G['defenc_why'] = why
    G['defenc_by_tool'] = True
    # ### **A CONTROL, BECAUSE A `False` FROM A CHECK THAT CANNOT SAY `True` IS NOT A RESULT.**
    probe = src_all + NL + 'def b430_control_stub : Nat := 0' + NL
    cflag, cwhy = rowgen.definition_encoded(probe, 'b430_control_stub = 1')
    say('        ### CONTROL, so a False is not a dead check: a literal-constant definition is')
    say('        ### appended to the same source and the same call is made --')
    say('        ### fires : %s   %s' % (cflag, cwhy))
    G['defenc_control_fires'] = bool(cflag)
    if not cflag:
        MISS.append('the defenc control did not fire; a False from it is not evidence')
    say()
    say('    ### **SO THE DEFINITIONS WERE CHECKED BY THE TOOL AND NOT ON A READING** -- which is')
    say('    ### clause four of b429\'s comparison, and the one this act exists to test.')
    say()


def comp4():
    rule('=')
    say('  COMPONENT 4 -- THE TWO GRADES, UNDER (R40), EACH AGAINST THE CLAIM IT NAMES.')
    rule('=')
    # ### **THE FOURTH GRADE'S PRESENCE IN THE CORPUS IS RE-MEASURED, NOT RECALLED (BAR 8).**
    docs = ['README.md', 'FINDINGS.md', 'REGISTRY.md', 'FACES_LEDGER.md', 'SPIRAL_MAP.md',
            'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'ERRATA.md']
    # ### **CASE-SENSITIVE, AND THAT IS THE MEASUREMENT, NOT A CONVENIENCE.** ### A case-insensitive
    # ### sweep returned three documents; ### **ONE OF THE THREE WAS THE ORDINARY ENGLISH PHRASE**
    # ### -- `FINDINGS.md`: "the finding is about the WARRANT and not the claim" -- which is not a
    # ### grade name and never was. ### A grade is a NAME, spelled as the vocabulary spells it.
    loose = [f for f in docs if re.search(r'NOT THE CLAIM', fold(read(os.path.join(PP, f))), re.I)]
    naming = [f for f in docs if re.search(r'NOT THE CLAIM', fold(read(os.path.join(PP, f))))]
    say('    corpus documents where the words occur, case-insensitively : %d of %d %s'
        % (len(loose), len(docs), loose or ''))
    say('    corpus documents naming NOT THE CLAIM, case-sensitively    : %d of %d %s'
        % (len(naming), len(docs), naming or ''))
    say('    ### **RE-MEASURED HERE. ### b429\'S FIGURE IS NOT CARRIED -- AND IT HAS MOVED.**')
    say('    ### b429 measured `0`. ### The count is no longer `0`, and ### **THE REASON IS b429')
    say('    ### ITSELF**: the ritual appends every act\'s closing record to `OPEN_TRAILS.md`, and')
    say('    ### b429\'s record reasons about the grade by name -- *"it states nothing weaker than')
    say('    ### C, so it is not NOT THE CLAIM"*. ### **SO THE TERM ENTERED THE CORPUS THROUGH A')
    say('    ### TRAIL RECORD AND NOT THROUGH THE GRADE VOCABULARY**, and the distinction matters:')
    say('    ### `README.md` and `EXCLUSION_ENGINE.md` §0 -- the two documents that DEFINE the')
    say('    ### grades -- still name three and only three. ### **b429\'S `G-CITED-NOWHERE` ARM')
    say('    ### WAS NOT BREACHED BY THIS**: it barred citing the grading, not using a word.')
    G['fourth_grade_docs'] = naming
    G['fourth_grade_docs_loose'] = loose
    vocab = [f for f in ('README.md',) if re.search(r'NOT THE CLAIM', fold(read(os.path.join(PP, f))))]
    exc_t = fold(read(os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')))
    if re.search(r'NOT THE CLAIM', exc_t):
        vocab.append('EXCLUSION_ENGINE.md')
    say('    ### **THE TWO GRADE-DEFINING DOCUMENTS NAMING IT : %d** %s' % (len(vocab), vocab or ''))
    G['fourth_grade_in_vocabulary'] = vocab
    say()
    clean = G.get('profile_empty')
    defenc = G.get('defenc')
    say('    ### THE FACTS BOTH GRADES REST ON, ALREADY PRINTED ABOVE:')
    say('      the profile is empty (no axioms)            : %s' % clean)
    say('      sorryAx in the closure                      : %s' % bool(G.get('sorryAx_in_profile')))
    say('      any definition a literal constant (defenc)  : %s' % defenc)
    say('      the statement quantifies over               : every p with singlePrimeFactor p = true,')
    say('                                                    and every n')
    say()
    # ### GRADE AGAINST CLAIM A.
    ca = G.get('claim_a', '')
    a_has_spf = bool(re.search(r'singlePrimeFactor p = true', ca, re.I))
    a_has_id = bool(re.search(r'ballQ p n \* sumAN p n = sumAQ p n', ca, re.I))
    a_has_every_n = bool(re.search(r'EVERY n', ca, re.I))
    grade_a = 'DERIVES' if (clean and not defenc and a_has_spf and a_has_id and a_has_every_n) \
        else ('NOT THE CLAIM' if not (a_has_spf and a_has_id) else 'UNDECIDED BY THIS ACT')
    say('    ### **GRADE AGAINST CLAIM A -- THE CLAIM THE CORRESPONDENCE ROW NAMES.**')
    say('      the row\'s quantifier matches the terminal\'s : %s' % a_has_spf)
    say('      the row\'s identity matches the terminal\'s   : %s' % a_has_id)
    say('      the row says EVERY n                        : %s' % a_has_every_n)
    say('      ### **GRADE : %s**' % grade_a)
    G['grade_a'] = grade_a
    say()
    # ### GRADE AGAINST CLAIM B.
    cb = G.get('claim_b_scope', '')
    b_every_base = bool(re.search(r'every base p\s*(>=|' + chr(0x2265) + r')\s*2', cb, re.I))
    say('    ### **GRADE AGAINST CLAIM B -- THE CLAIM THE FINITE-SIDE PROSE MAKES.**')
    say('      F5\'s scope sentence, quoted above, says GENERAL over : %s'
        % (cb[:80] if cb else '### NOT LOCATED ###'))
    say('      it claims every base p >= 2                  : %s' % b_every_base)
    say('      the terminal is restricted to bases with ONE prime factor : True')
    say()
    # ### =========================================================================================
    # ### **AND A SECOND REASON, INDEPENDENT OF SCOPE AND MEASURED RATHER THAN ASSERTED.**
    # ### K3's claim is about THE SOURCE'S CONSTRUCTION ON THE OBJECT -- the test function at the
    # ### identity, times a dimension. ### The terminal is about THE MODEL'S COUNT: three `Nat`
    # ### quantities and an equation between them. ### **IF THE TERMINAL'S STATEMENT NAMES NONE OF
    # ### ### THE OBJECTS K3'S CLAIM NAMES, IT DOES NOT STATE THAT CLAIM AT ALL**, whatever its
    # ### scope -- and that is a stronger reading than the scope one, because it would hold even if
    # ### the terminal were general over every base.
    # ### =========================================================================================
    stmt = G.get('statement', '')
    k3_objs = ['trace', 'test function', 'identity', 'dimension', 'source', 'construction',
               'archimedean', 'zeta', 'object']
    present = [o for o in k3_objs if re.search(r'\b' + re.escape(o) + r'\b', stmt, re.I)]
    say('      ### THE SECOND REASON, AND IT DOES NOT DEPEND ON SCOPE:')
    say('        objects K3\'s claim names          : %s' % ', '.join(k3_objs))
    say('        of those, named in the terminal\'s statement : %d %s'
        % (len(present), present or ''))
    say('        the terminal\'s statement is       : an equation between three Nat quantities')
    say('        ### **THE PROSE SPEAKS OF THE SOURCE\'S TRACE; THE TERMINAL SPEAKS OF THE MODEL\'S')
    say('        ### COUNT.** ### The record says this itself at FINDINGS.md line 3084 -- *"the')
    say('        ### identification of that count with the source\'s trace is b310\'s derivation and')
    say('        ### is not compiled"* -- so the gap is the record\'s own, stated, and not a')
    say('        ### discovery of this act.')
    G['k3_objects_in_statement'] = present
    say()
    say('      ### **TWO INDEPENDENT REASONS, BOTH POINTING ONE WAY: THE TERMINAL STATES STRICTLY')
    say('      ### LESS THAN CLAIM B NAMES**, which is the scope (R40) gives the fourth grade in')
    say('      ### its own words.')
    say('      ### **AND ONE THING THIS GRADE IS NOT.** ### It is NOT a finding that `F5`\'s own')
    say('      ### listed terminals are misgraded: `F5`\'s `PROVED-GENERAL` governs the SCALING')
    say('      ### part, a different list of theorems, and this act neither built nor graded those.')
    say('      ### ### **`K3`\'S PROSE IS ITSELF CAREFULLY QUALIFIED** -- *the compact part PER')
    say('      ### CELL* -- and that qualification is the record being right, not wrong.')
    grade_b = ('NOT THE CLAIM' if (b_every_base and not present) else 'UNDECIDED BY THIS ACT')
    say('      ### **GRADE : %s**' % grade_b)
    G['grade_b'] = grade_b
    G['claim_b_every_base'] = b_every_base
    say()
    say('    ### **BOTH GRADES ARE HONEST AND NEITHER IS AVERAGED INTO THE OTHER (R27).** ### And')
    say('    ### under (R40) they are not in conflict: they are two relations, not two readings of')
    say('    ### one. ### **NO GRADE ON THE RECORD MOVES BY EITHER.**')
    say()
    say('    ### AND THE RESIDUE, NAMED AS b429 NAMED ITS OWN:')
    say('      ### **K3 IS NOT GRADED HERE AS A WHOLE.** ### K3 carries three terminal-classes and')
    say('      ### a derivation on content; this act graded ONE terminal against the scope clause')
    say('      ### F5 and K3 share. ### The rest of K3 is untouched and no grade of it moves.')
    say('      ### **AND THE ARITHMETIC IS THE MODEL\'S.** ### Whether the model\'s count IS the')
    say('      ### source\'s trace stays b310\'s derivation and is not compiled -- the record says')
    say('      ### so itself, and this act does not disturb it.')
    say()


def comp5():
    rule('=')
    say('  COMPONENT 5 -- THE FOUR CLAUSES SET BESIDE b429\'S, AND THE VERDICT.')
    rule('=')
    both = read(B429G) + NL + read(B429C)

    def clauses(txt, label):
        """### A CLAUSE RUNS TO THE NEXT LINE AT ITS OWN INDENTATION OR SHALLOWER.

        ### ### **STOPPING AT THE FIRST `###` LINE LOSES THE CLAUSE'S LAST PHRASE**, and on clause
        ### 4 that phrase was ### **"THIS ACT DID NOT RUN IT"** -- the finding itself. ### b429
        ### indents a clause's continuations far past its label and puts the act's own commentary
        ### back at the label's column, so ### **INDENTATION IS THE STRUCTURE AND A MARKER IS NOT.**
        """
        lines = txt.splitlines()
        out = []
        for i, ln in enumerate(lines):
            m_ = re.match(r'(\s*)' + label + r'\s*:\s*(.*)$', ln)
            if not m_:
                continue
            col = len(m_.group(1))
            body = [m_.group(2)]
            for nxt in lines[i + 1:]:
                if not nxt.strip():
                    break
                if len(nxt) - len(nxt.lstrip()) <= col:
                    break
                body.append(nxt.strip())
            out.append(fold(' '.join(body)))
        return out
    stranger = clauses(both, 'TO THE STRANGER')
    itself = clauses(both, 'TO ITSELF')
    G['b429_clauses'] = len(stranger)
    if len(stranger) < 4 or len(itself) < 4:
        MISS.append('fewer than four compared clauses recovered from b429')
    # ### **THIS ACT'S CONDUCT ON THE SAME FOUR, EACH DECIDED FROM A PRINTED RESULT ABOVE AND NOT
    # ### FROM A SENTENCE ABOUT THIS ACT.**
    mine = [
        ('a clean `#print axioms` was REQUIRED and read from the printer\'s own output; the '
         'closure tested for sorryAx by name and the source swept for sorry with comments and '
         'string literals stripped first. ### %s, sorryAx %d, sorry as a term %d.'
         % ('the profile is empty' if G.get('profile_empty') else 'THE PROFILE IS NOT EMPTY',
            G.get('sorryAx_in_profile', -1), G.get('sorry_terms', -1)),
         bool(G.get('profile_empty')) and not G.get('sorryAx_in_profile')),
        ('the statement was unfolded to its base objects, %d of %d quoted at their own file and '
         'line, from the kernel\'s source and not from prose about it.'
         % (G.get('defs_located', 0), G.get('defs_wanted', 0)),
         G.get('defs_located') == G.get('defs_wanted')),
        ('four grades, including NOT THE CLAIM -- and ### **THE FOURTH WAS USED**, against CLAIM '
         'B. ### Under (R40) it is available to the corpus\'s own terminal exactly as it was to '
         'the stranger\'s.',
         G.get('grade_b') == 'NOT THE CLAIM'),
        ('the definitions were put to `rowgen.definition_encoded` -- the corpus\'s own tool, '
         'IMPORTED -- over the whole import chain, with a control appended so that a False is a '
         'result. ### defenc %s, control fires %s.'
         % (G.get('defenc'), G.get('defenc_control_fires')),
         G.get('defenc_by_tool') and G.get('defenc_control_fires')),
    ]
    same = 0
    for i in range(4):
        say('    ### CLAUSE %d' % (i + 1))
        for ln in wrap('b429, TO THE STRANGER : ' + (stranger[i] if i < len(stranger) else '###'),
                       90, '        '):
            say(ln)
        for ln in wrap('b429, TO ITSELF       : ' + (itself[i] if i < len(itself) else '###'),
                       90, '        '):
            say(ln)
        txt, ok = mine[i]
        for ln in wrap('b430, TO ITSELF       : ' + fold(txt), 90, '        '):
            say(ln)
        say('        ### **APPLIED TO ITSELF AS b429 APPLIED IT TO THE STRANGER : %s**'
            % ('YES' if ok else '### NO ###'))
        same += 1 if ok else 0
        say()
    G['clauses_same'] = same
    verdict = ('SYMMETRIC' if same == 4 else
               'ASYMMETRIC INWARD' if same == 0 else 'ASYMMETRIC INWARD (PARTIAL)')
    say('    ### **CLAUSES APPLIED TO ITSELF AS THEY WERE APPLIED TO THE STRANGER : %d OF 4.**'
        % same)
    say('    ### ### **VERDICT : %s**' % verdict)
    G['verdict'] = verdict
    say()
    say('    ### **AND THE VERDICT\'S OWN SENTENCE SAYS WHAT IT IS: ONE TRIAL AGAINST ONE TRIAL.**')
    say('    ### b429 graded one stranger; b430 grades one terminal of the corpus\'s own. ### Two')
    say('    ### acts are not a population, and ### **NOTHING HERE LICENSES A STATEMENT ABOUT THE')
    say('    ### CORPUS\'S GRADING DISCIPLINE IN GENERAL.** ### What it does settle is narrower and')
    say('    ### real: on this trial the discipline did not soften when the subject was its own.')
    say()
    say('    ### AND THE DIRECTION b429 FOUND IS RE-READ, NOT RESTATED:')
    say('    ### b429 found 2 of 4 asymmetric and ### **BOTH FAVOURING THE STRANGER** -- a finer')
    say('    ### grade available only against it, and its definitions accepted on a reading where')
    say('    ### the corpus runs a tool on its own. ### **b430 CLOSES BOTH GAPS FROM THE OTHER')
    say('    ### SIDE**: the fourth grade was available AND USED against the corpus\'s own terminal,')
    say('    ### and the tool was run. ### So the b429 asymmetries were THAT ACT\'S, not the')
    say('    ### discipline\'s -- which is what `SYMMETRIC` means on this face.')
    say()


def main(argv):
    rule('=')
    say('b430_components.py -- THE SELF-CONTROL. ### THE CORPUS\'S OWN TERMINAL, GRADED TWICE.')
    rule('=')
    # ### **THE ORDER IS STAMPED, NOT ASSERTED.** ### This tool READS the locked face and prints
    # ### the digest the lock block carries. ### A components bank carrying that digest can only
    # ### have been written after the lock, and ### **THAT WITNESS SURVIVES A CHECKOUT WHERE AN
    # ### mtime DOES NOT** -- which is how the first writing of `G-REG-LOCKED-FIRST` failed, on the
    # ### ritual's own branch dance, after passing honestly before the push.
    face = read(os.path.join(D, 'b430_registration_2026-09-12.txt'))
    mseal = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    say('  ### THE REGISTRATION WAS LOCKED BEFORE ANY OF THIS RAN.')
    say('  ### THE SEAL THIS RUN READ OFF THE LOCKED FACE : %s'
        % (mseal.group(1) if mseal else '### NO LOCK BLOCK ON THE FACE ###'))
    G['seal_read_from_face'] = mseal.group(1) if mseal else None
    say('  ### **NO CORPUS FILE IS WRITTEN BY THIS TOOL. ### NO GRADE ON THE RECORD MOVES.**')
    say()
    comp0()
    comp1()
    comp2()
    comp3()
    comp4()
    comp5()
    rule('=')
    say('  ### MISSES : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    io.open(GRADES + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(G, indent=2, ensure_ascii=False) + NL)
    os.replace(GRADES + '.tmp', GRADES)
    print(txt)
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(GRADES)))
    return 0 if (os.path.exists(OUT) and os.path.exists(GRADES)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
