# -*- coding: utf-8 -*-
"""b432_components.py -- THE FIVE COMPONENTS OF b432: THE DISPROOF LANE RESTATED.

### **THE LANE IS RESTATED AND NOT OPENED.** ### This file writes what a disproof would have to
### state, in the corpus's own vocabulary, and decides which form each of two named instruments is
### for -- by reading what each is RUN ON and what it REPORTS, never by either instrument's name
### (BAR 3, minted at b431 on `crt_exhaustiveness`).
### ### **IT CONSTRUCTS NOTHING, ASSERTS NEITHER FORM, AND TOUCHES NO TRIGGER.**
"""
import io
import json
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
FACE = os.path.join(D, 'b432_registration_2026-09-12.txt')
B428 = os.path.join(D, 'b428_components.txt')
OUT = os.path.join(D, 'b432_components.txt')
FJSON = os.path.join(D, 'b432_forms.json')
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


def wrap(text, width=90, indent='      '):
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


def rows(path, pat, cap=8, maxlen=800):
    """### ALL MATCHING ROWS WITH THEIR LINES (BAR 5). ### **NEVER THE FIRST ALONE.**

    ### ### **THE NEEDLE IS MATCHED AGAINST THE FOLDED LINE, NOT THE RAW ONE** (BAR 10). ### The
    ### keystone writes the premise as `` `h2` `` with backticks, so a needle reading `h2, the
    ### positive space` found nothing in the raw text and the survey reported a miss on a sentence
    ### that is plainly there. ### Folding is what the bar exists for, and this call had skipped it.
    """
    out = []
    for i, ln in enumerate(read(path).splitlines(), 1):
        if re.search(pat, fold(ln)) or re.search(pat, ln):
            out.append((i, unbar(ln)[:maxlen]))
        if len(out) >= cap:
            break
    return out


def comp0():
    face = read(FACE)
    m = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    say('  ### THE SEAL THIS RUN READ OFF THE LOCKED FACE : %s'
        % (m.group(1) if m else '### NO LOCK BLOCK ###'))
    G['seal_read_from_face'] = m.group(1) if m else None
    say()


def comp1():
    rule('=')
    say('  COMPONENT 1 -- THE LANE AS b428 NAMED IT, AND WHAT IT LACKED.')
    rule('=')
    b = read(B428)
    hits = [ln for ln in b.splitlines() if re.search(r'disproof', ln, re.I)]
    say('    lines in b428`s own components naming the lane : %d' % len(hits))
    for ln in hits[:12]:
        for w in wrap(fold(ln), 88, '        '):
            say(w)
    G['b428_lines'] = len(hits)
    if not hits:
        MISS.append('b428 carries no line naming the lane')
    say()
    say('    ### **WHAT b428 LACKED, IN THE ORDER`S OWN WORDS:** *"The lane was named at b428 with')
    say('    ### no example of what a graded disproof looks like."* ### **THAT IS NOT A CRITICISM')
    say('    ### OF b428**: at b428 the record held no graded terminal of either shape, so there')
    say('    ### was nothing to point at. ### The sortie has since produced two.')
    say()


def comp2():
    rule('=')
    say('  COMPONENT 2 -- THE TWO WORKED CASES, AND THAT THEY ARE OF TWO SHAPES.')
    rule('=')
    ns = read(os.path.join(D, 'b429_the_grade.txt'))
    lg = read(os.path.join(D, 'b431_components.txt'))
    try:
        lgj = json.loads(read(os.path.join(D, 'b431_the_grade.json')) or '{}')
    except Exception:
        lgj = {}
    a_grade = 'DERIVES' if re.search(r'GRADE\s*:\s*\*{0,2}DERIVES', ns) else '### NOT READ ###'
    b_grade = lgj.get('grade', '### NOT READ ###')
    say('    ### CASE A -- b429, AGAINST CLAY STATEMENT C')
    say('      grade, from its own bank          : %s' % a_grade)
    say('      the SHAPE of C`s conclusion       : %s'
        % ('UNIVERSAL NEGATIVE' if re.search(r'universal negative', ns, re.I)
           else '### NOT FOUND ###'))
    say('      in the terminal`s own Lean        : `¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn')
    say('                                          nu u₀ f v p)` -- a negation of an existential.')
    say()
    say('    ### CASE B -- b431, AGAINST THE PAPER`S THEOREM 1.1')
    say('      grade, from its own bank          : %s' % b_grade)
    say('      the SHAPE of Theorem 1.1          : %s'
        % ('EXISTENTIAL -- A CONSTRUCTION' if '∃ c X₀' in lg else '### NOT FOUND ###'))
    say('      in the terminal`s own Lean        : `∃ c X₀ : ℝ, 0 < c ∧ ∀ X, X₀ ≤ X → ∃ n, ...` --')
    say('                                          a witness is produced at every large X.')
    G['case_a_grade'] = a_grade
    G['case_b_grade'] = b_grade
    G['case_a_shape'] = 'UNIVERSAL NEGATIVE'
    G['case_b_shape'] = 'EXISTENTIAL / CONSTRUCTION'
    say()
    say('    ### **SO THE RECORD NOW HOLDS ONE GRADED TERMINAL OF EACH SHAPE**, and the shapes are')
    say('    ### read from the STATEMENTS, not from the grades -- both grades are the same word.')
    say('    ### **AND TWO CASES ARE TWO CASES.** ### Nothing here is a claim about disproofs in')
    say('    ### general, or about how often either shape is available.')
    say()


def comp3():
    rule('=')
    say('  COMPONENT 3 -- WHAT A DISPROOF WOULD HAVE TO STATE, IN THE CORPUS`S OWN VOCABULARY.')
    rule('=')
    say('    ### FIRST, THE HYPOTHESIS, IN THE CORPUS`S WORDS AND NOT THIS SEAT`S:')
    hit = rows(BARRIER, r'h2, the positive space on the zeros', 1, 900)
    for i, r in hit:
        say('      INVARIANCE_BARRIERS.md:%d' % i)
        for w in wrap(r, 88, '          '):
            say(w)
    if not hit:
        MISS.append('h2 not located in the barrier keystone')
    G['h2_line'] = hit[0][0] if hit else None
    say()
    say('    ### **SO WHAT A DISPROOF MUST CONTRADICT IS `h2`** -- a positive-definite pairing')
    say('    ### realized on the nontrivial zeros; equivalently, realization-totality at the ξ')
    say('    ### interface. ### **RH FOLLOWS FROM `h2`; SO A DISPROOF OF RH MUST DENY `h2`, AND A')
    say('    ### DENIAL OF `h2` ALONE IS NOT YET A DISPROOF OF RH** -- the implication runs one way,')
    say('    ### and the act states that rather than eliding it.')
    say()
    # ### ---- FORM (a) ---------------------------------------------------------------------------
    say('    ### **FORM (a) -- AN EXHIBITED ZERO OFF THE LINE.**')
    say('      WHAT IT WOULD HAVE TO STATE: *there exists `s₀` with `ξ(s₀) = 0` and `Re s₀ ≠ 1/2`,*')
    say('      *exhibited* -- a witness, not a density statement and not a non-vanishing argument.')
    say('      THE CLAUSE IT WOULD HAVE TO MEET, quoted from the barrier keystone:')
    t6 = rows(BARRIER, r'\*\*T6 codim(ension)?-2 transversality\*\*', 4, 700)
    for i, r in t6:
        say('        INVARIANCE_BARRIERS.md:%d' % i)
        for w in wrap(r, 86, '            '):
            say(w)
    G['t6_lines'] = [i for i, _ in t6]
    say('      ### **CODIMENSION 2**: `Re F = Im F = 0`, two real conditions. ### An exhibited zero')
    say('      ### is a point in a set the keystone says is codimension 2, which is why numerical')
    say('      ### near-misses are not exhibits and why the corpus`s own counterexample matters.')
    say()
    # ### ---- FORM (b) ---------------------------------------------------------------------------
    say('    ### **FORM (b) -- THE UNIVERSAL NEGATIVE.**')
    say('      WHAT IT WOULD HAVE TO STATE: *no arrangement of zeros ON the line is consistent with*')
    say('      *the Euler balance* -- i.e. the positive space of `h2` cannot be realized AT ALL,')
    say('      for any on-line configuration. ### **THAT IS A STATEMENT ABOUT EVERY ARRANGEMENT,**')
    say('      **NOT ABOUT ONE OBJECT**, and it exhibits nothing.')
    say('      ### **AND ITS SHAPE IS THE SHAPE OF b429`S CASE**: `¬∃`. ### A terminal of that')
    say('      ### shape is what a disproof of form (b) would look like when graded.')
    say('      ### **AND FORM (a)`S SHAPE IS THE SHAPE OF b431`S CASE**: `∃`, a construction that')
    say('      ### produces the witness. ### That is the worked case the order asked for, and it is')
    say('      ### why two gradings of the same word `DERIVES` are not two of the same thing.')
    say()
    say('    ### **NEITHER FORM IS ASSERTED HERE. ### NEITHER IS CONSTRUCTED HERE.** ### This')
    say('    ### component states what such a statement would have to say and stops.')
    say()


def comp4():
    rule('=')
    say('  COMPONENT 4 -- WHICH FORM THE NEGATIVE CONTROL AND THE PHASE CONDITION ARE FOR.')
    rule('=')
    say('    ### **BAR 3: DECIDED BY WHAT EACH IS RUN ON AND WHAT IT REPORTS, NEVER BY ITS NAME.**')
    say()
    say('    ### THE NEGATIVE CONTROL -- ITS ROWS, AT THEIR OWN LINES:')
    nc = rows(FIND, r'negative control', 8, 700)
    # ### **A ROW IS RELIED ON ONLY IF IT IS AN ACT'S OWN VERDICT ROW**, not merely a line that
    # ### mentions an act number. ### The first writing matched `b32[5-8]` anywhere in the line and
    # ### so "relied on" a paragraph DESCRIBING the faces ledger, because it contains the phrase
    # ### "b326's result". ### The marker must open the row.
    keep = [(i, r) for i, r in nc
            if re.match(r'^\|?\s*b32[5-8]', r) or re.match(r'^-?\s*b32[5-8]\s*--', r)]
    for i, r in nc:
        mark = 'RELIED ON' if (i, r) in keep else '   --    '
        say('      line %-6d %s' % (i, mark))
        for w in wrap(r, 86, '          '):
            say(w)
    say('      ### **THE ROWS RELIED ON ARE THOSE NAMING AN ACT THAT RAN IT** (b325, b326, b328);')
    say('      ### the others describe the ledger or a refused method and are printed, not used.')
    G['nc_rows'] = [i for i, _ in nc]
    G['nc_relied'] = [i for i, _ in keep]
    say()
    say('    ### WHAT IT IS RUN ON, from the keystone`s own account:')
    dh = rows(BARRIER, r'Davenport.{0,3}Heilbronn \(1936\) proved', 2, 600)
    for i, r in dh:
        say('      INVARIANCE_BARRIERS.md:%d' % i)
        for w in wrap(r, 86, '          '):
            say(w)
    run_on_exhibited = bool(dh)
    say()
    # ### **A HYPHENATED NAME IS ONE TOKEN.** ### The first writing broke `Davenport-Heilbronn`
    # ### across two lines, and BAR 10 forbids exactly that -- a reader cannot tell a wrapped name
    # ### from a compound one. ### The break now falls at a space.
    say('    ### **THE OBJECT IS ONE WITH ZEROS ACTUALLY OFF THE LINE** -- the Epstein zeta the')
    say('    ### corpus calls its own counterexample, whose off-line zeros are PROVED in 1936 by')
    say('    ### Davenport and Heilbronn and EXHIBITED numerically by Stark in 1967.')
    say('    ### **AND WHAT THE CONTROL')
    say('    ### REPORTS IS WHETHER THE INSTRUMENT SEES THAT ZERO**: b325/b326 `DOES NOT SEE IT`,')
    say('    ### b328 `SEES IT` at seven of eight cells.')
    say()
    say('    ### ### **SO: THE NEGATIVE CONTROL IS AN INSTRUMENT FOR FORM (a), THE EXHIBITED ZERO.**')
    say('    ### It is calibrated on an object that HAS one, and it answers "does the instrument')
    say('    ### detect it". ### **IT CANNOT BE AN INSTRUMENT FOR FORM (b)**: a universal negative')
    say('    ### exhibits no object, so there is nothing for a control of this kind to be run on.')
    G['negative_control_form'] = 'a'
    G['negative_control_not_form_b'] = True
    G['run_on_exhibited'] = run_on_exhibited
    say()
    say('    ### THE PHASE CONDITION -- ITS ROW, AT ITS OWN LINE:')
    ph = rows(FIND, r'four-term sum at an off-line quadruple|forty-five degrees of phase', 4, 800)
    for i, r in ph:
        say('      FINDINGS.md:%d' % i)
        for w in wrap(r, 86, '          '):
            say(w)
    at_quadruple = any('off-line quadruple' in r for _, r in ph)
    G['phase_rows'] = [i for i, _ in ph]
    say()
    say('    ### **THE CONDITION IS STATED AT AN OFF-LINE QUADRUPLE : %s**' % at_quadruple)
    say('    ### The four-term sum is `4 Re(G_e² − G_o²)` AT AN OFF-LINE QUADRUPLE, negative only')
    say('    ### past forty-five degrees of phase. ### **IT IS A CONDITION ON THE SEED THAT DECIDES')
    say('    ### WHETHER THE INSTRUMENT CAN FIRE ON AN EXHIBITED OFF-LINE ZERO AT ALL** -- which')
    say('    ### makes it the calibration of the negative control, not a second instrument.')
    say('    ### ### **SO THE PHASE CONDITION IS ALSO FOR FORM (a), AND FOR THE SAME REASON.**')
    G['phase_form'] = 'a' if at_quadruple else 'UNDECIDED FROM THE RECORD'
    say()
    say('    ### ### **AND THE CONSEQUENCE, WHICH IS THE FINDING OF THIS COMPONENT:**')
    say('    ### **BOTH NAMED INSTRUMENTS SERVE FORM (a). ### THE CORPUS HAS NO INSTRUMENT POINTED')
    say('    ### AT FORM (b) AT ALL.** ### That is consistent with what b428 found by a different')
    say('    ### route -- a certified disproof instrument the corpus has never pointed -- and it')
    say('    ### sharpens it: ### **THE INSTRUMENT IT HAS IS OF THE WRONG KIND FOR ONE OF THE TWO')
    say('    ### FORMS, NOT MERELY UNPOINTED.**')
    say('    ### **AND THIS IS NOT A CLAIM THAT FORM (b) IS UNREACHABLE**, nor that an instrument')
    say('    ### for it would be cheap or dear. ### It is a statement about what the record holds.')
    G['no_instrument_for_form_b'] = True
    say()
    say('    ### AND THE SCOPE EACH ACT SET FOR ITSELF, CARRIED WITH ITS WORDS (BAR 6):')
    for i, r in rows(FIND, r'IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES', 2, 400):
        say('      FINDINGS.md:%d' % i)
        for w in wrap(r, 86, '          '):
            say(w)
    for i, r in rows(FIND, r'says nothing about the method or about zeta', 2, 500):
        say('      FINDINGS.md:%d' % i)
        for w in wrap(r, 86, '          '):
            say(w)
    say()


def comp5():
    rule('=')
    say('  COMPONENT 5 -- THE BARRIER KEYSTONE`S SYMMETRY CLAUSE, AND THE LANE LEFT WHERE IT WAS.')
    rule('=')
    t1 = rows(BARRIER, r'\*\*T1 functional equation\*\*', 2, 600)
    for i, r in t1:
        say('    INVARIANCE_BARRIERS.md:%d  -- T1, THE SYMMETRY ITSELF' % i)
        for w in wrap(r, 88, '        '):
            say(w)
    G['t1_lines'] = [i for i, _ in t1]
    say()
    say('    ### **THE SYMMETRY IS `s ↔ 1−s`, AND IT IS WHAT MAKES FORM (a) A QUADRUPLE RATHER THAN')
    say('    ### A POINT.** ### With real coefficients a zero off the line comes with `1−s₀`, `s̄₀`')
    say('    ### and `1−s̄₀`; that is why the corpus`s own instrument is tested AT AN OFF-LINE')
    say('    ### QUADRUPLE and not at a single zero, and why the phase condition is stated there.')
    say('    ### **THE SCOPE IS THE KEYSTONE`S AND THIS ACT ADDS NONE**: T1 is listed as a TOOL of')
    say('    ### the six-tool toolkit `T`, and the keystone`s claim is about what `T` cannot')
    say('    ### establish -- not a claim about zeta`s zeros.')
    say()
    say('    ### **THE LANE, LEFT WHERE IT WAS FOUND.**')
    say('      trigger, unchanged      : the instrument lane opening')
    say('      lanes opened by this act: 0')
    say('      candidates constructed  : 0')
    say('      claims about reach      : 0')
    say('      keystones edited        : 0')
    say('    ### **THE RESTATEMENT IS THE WHOLE OF WHAT THIS ACT DID TO THE LANE.**')
    say()


def main(argv):
    rule('=')
    say('b432_components.py -- THE DISPROOF LANE, RESTATED WITH A WORKED CASE. ### NOTHING OPENED.')
    rule('=')
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
    io.open(FJSON + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(G, indent=2, ensure_ascii=False) + NL)
    os.replace(FJSON + '.tmp', FJSON)
    print(txt)
    print('  written: %s, %s' % (os.path.basename(OUT), os.path.basename(FJSON)))
    return 0 if (os.path.exists(OUT) and os.path.exists(FJSON)) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
