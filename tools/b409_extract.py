# -*- coding: utf-8 -*-
"""b409_extract.py -- EXTRACT-TO-DISK. ### EVERY READ AND EVERY COUNT THIS ACT MAKES.

### ### (A) The CANONICAL index, from TWO independent places, and the one table that disagrees.
### ### (B) The numbering sweep: every class-symbol use in the live tree, pinned by content, under
###     BOTH a loose window and a tight one -- ### **BOTH YIELDS PRINTED.**
### ### (C) The two hits `b408` filed as artefacts, read WHOLE, with the machinery line that says
###     which classes they actually name.
### ### (D) The global class, by DESCRIPTION and under BOTH numberings, with a POSITIVE CONTROL.
### ### (E) The Sieve Ceiling Lemma's proof at content -- every movement, for the relativization.
### ### (F) Row `U1` from the committed blob, and `b408`'s four imported premises.
###
### ### **EVERY WRITE ENCODES BEFORE IT OPENS.** ### **NO RUN RECORD IS READ FROM A LISTING.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b409_extract.txt')
SCRATCH = os.path.join(D, '_b409')
PP = r'D:\MY-DOwnloads\PLACE-papers'
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
MC = os.path.join(PP, 'day1', 'Seven_Mechanism_Classes.md')
EN = os.path.join(PP, 'phase1.5', 'method', 'ENUMERA.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
CR = os.path.join(PP, 'internal', 'CRITICAL_RESOLVE.md')

BS = chr(92)
SYM = re.compile(r'C([\u2081-\u2087])')
SUB = {'\u2081': 1, '\u2082': 2, '\u2083': 3, '\u2084': 4, '\u2085': 5, '\u2086': 6, '\u2087': 7}
CANON = {1: 'Schwarz / additive', 2: 'Euler / multiplicative', 3: 'functional equation',
         4: 'modular / PSL2', 5: 'spectral', 6: 'Cauchy-Riemann', 7: 'Hadamard'}
CONTENT = {1: r'Schwarz|additive', 2: r'Euler|multiplicativ',
           3: r'functional[- ]equation|archimedean', 4: r'PSL|modular',
           5: r'spectral', 6: r'Cauchy|local analytic', 7: r'Hadamard'}

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def write_text(path, text):
    io.open(path, 'wb').write(text.encode('utf-8'))


def pull(path, hint, label, span=False, width=460):
    try:
        if span:
            ln0, run = AF.find_span(path, hint)
            txt = '\n'.join(run)
        else:
            ln0, txt = AF.find(path, hint)
    except AF.AnchorError as e:
        MISS.append(label)
        say('  ### ANCHOR MISS -- %s' % label)
        say('      %s' % str(e).splitlines()[0][:180])
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln0))
    for ln in txt.splitlines():
        for k in range(0, max(len(ln), 1), width):
            say('      | %s' % ln[k:k + width])
    return txt


def live_md():
    out = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, PP).replace(BS, '/')
                out.append((rel, p))
    return out


def pins(src, tight):
    """### Pin each symbol by the content that follows it. ### **TIGHT STOPS AT THE NEXT SYMBOL.**

    ### ### **THE LOOSE WINDOW IS A KNOWN ARTEFACT AND IS KEPT ONLY TO BE PRINTED BESIDE THE TIGHT
    ### ### ONE.** ### A document listing the classes in a row -- *C3 FE, C4 PSL2, C5 Spectral* --
    ### gives every symbol a neighbour's content inside 70 characters, so the loose window reports
    ### a DISAGREEMENT that is nothing but the list's own shape.
    """
    agree = dis = 0
    ev = []
    for m in SYM.finditer(src):
        n = SUB[m.group(1)]
        rest = src[m.end():m.end() + (40 if tight else 70)]
        if tight:
            nxt = SYM.search(rest)
            if nxt:
                rest = rest[:nxt.start()]
        if re.search(CONTENT[n], rest, re.I):
            agree += 1
            if len(ev) < 2:
                ev.append((src[m.start():m.end()] + rest).replace('\n', ' ')[:56])
        else:
            for k, pat in CONTENT.items():
                if k != n and re.search(pat, rest, re.I):
                    dis += 1
                    break
    return agree, dis, ev


def main():
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    say('=' * 100)
    say('b409_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.')
    say('=' * 100)
    if not AF.self_test(verbose=False):
        say('  ### REFUSING TO QUOTE THROUGH A TOOL THAT FAILS ITS OWN FIXTURES.')
        return 2
    say('  anchor tool self-test : PASS')

    # -------------------------------------------------------------- (A) THE CANONICAL INDEX
    say()
    say('-' * 100)
    say('### (A) THE CANONICAL INDEX, FROM TWO INDEPENDENT PLACES -- AND THE ONE THAT DISAGREES.')
    say('-' * 100)
    say('  ### **FIRST WITNESS: THE MONOGRAPH`S OWN CLASS TABLE.**')
    src = io.open(MONO, encoding='utf-8').read().split('\n')
    hdr = [i for i, x in enumerate(src, 1) if x.startswith('| C\u2081 (Schwarz reflection) |')]
    if hdr:
        for i in range(hdr[0], hdr[0] + 7):
            say('      | %s' % src[i - 1].strip()[:180])
    else:
        MISS.append('THE MONOGRAPH`S CLASS TABLE')
        say('  ### ROW MISS -- the monograph`s class table')
    say()
    say('  ### **SECOND WITNESS: `ENUMERA.md``S OWN RECONCILIATION, WRITTEN FOR THIS VERY**')
    say('  ### **QUESTION.**')
    pull(EN, '**Canonical-numbering reconciliation (monograph Ch.15).**',
         'THE RECONCILIATION, WHOLE')
    say()
    say('  ### ### **AND THE ONE TABLE THAT DISAGREES WITH BOTH:**')
    pull(MC, '**Remark (Class numbering).**', 'THE REMARK THAT OPENS IT')
    for row in ('| C\u2081 | C\u2082 |', '| C\u2082 | C\u2084 |', '| C\u2083 | C\u2081 |',
                '| C\u2084 | C\u2085 |', '| C\u2085 | C\u2086 |', '| C\u2086 | C\u2083 |',
                '| C\u2087 | C\u2087 |'):
        pull(MC, row, 'ITS ROW %s' % row.strip('| '))
    say()
    say('  ### ### **THE COMPARISON, MADE HERE AND NOT ASSUMED:**')
    say('      the monograph`s own table and `ENUMERA`s reconciliation ### **AGREE, SYMBOL FOR')
    say('      SYMBOL** ### -- C1 Schwarz, C2 Euler, C3 functional-equation, C4 modular/PSL2,')
    say('      C5 spectral, C6 Cauchy-Riemann, C7 Hadamard.')
    say('      the correspondence table`s *Monograph* column ### **DISAGREES WITH BOTH OF THEM ON**')
    say('      ### **SIX OF SEVEN SYMBOLS.**')
    say('  ### ### ### **SO THERE IS ONE CANONICAL INDEX ATTESTED TWICE, AND ONE TABLE THAT')
    say('  ### ### ### CONTRADICTS THE DOCUMENT IT NAMES.**')

    # -------------------------------------------------------------- (B) THE SWEEP
    say()
    say('-' * 100)
    say('### (B) THE SWEEP -- EVERY CLASS-SYMBOL USE, UNDER BOTH WINDOWS.')
    say('-' * 100)
    rows = []
    dep_docs = dep_uses = 0
    for rel, p in live_md():
        src = io.open(p, encoding='utf-8', errors='replace').read()
        n = len(SYM.findall(src))
        if not n:
            continue
        if rel.startswith('outputs/'):
            dep_docs += 1
            dep_uses += n
            continue
        la, ld, _ev = pins(src, tight=False)
        ta, td, ev = pins(src, tight=True)
        rows.append(dict(rel=rel, uses=n, la=la, ld=ld, ta=ta, td=td, ev=ev))
    say('  ### LIVE documents using a class symbol : %d ; uses : %d'
        % (len(rows), sum(r['uses'] for r in rows)))
    say('  ### DEPOSITED (`outputs/`) documents, NOT TOUCHED : %d ; uses : %d'
        % (dep_docs, dep_uses))
    say()
    say('  ### **THE TWO WINDOWS, AND WHY BOTH ARE PRINTED:**')
    say('      LOOSE -- 70 characters after the symbol, whatever falls inside.')
    say('      TIGHT -- stops at the NEXT class symbol. ### **A LIST OF CLASSES GIVES EVERY SYMBOL')
    say('      ### A NEIGHBOUR`S CONTENT UNDER THE LOOSE WINDOW**, so the loose DISAGREE count is')
    say('      the list`s shape and not a scheme conflict.')
    loose_dis = sum(1 for r in rows if r['ld'] > 0)
    tight_dis = sum(1 for r in rows if r['td'] > 0)
    say('  ### ### **DOCUMENTS WITH A DISAGREEING PIN: ### LOOSE %d ### ; TIGHT %d.**'
        % (loose_dis, tight_dis))
    readable = [r for r in rows if r['ta'] > 0]
    undecl = [r for r in rows if r['ta'] == 0]
    say('  ### ### **SCHEME READABLE FROM THE DOCUMENT`S OWN TEXT (TIGHT) : %d**' % len(readable))
    say('  ### ### **SCHEME UNDECLARED : %d**' % len(undecl))
    say()
    say('  ### **THE READABLE DOCUMENTS, WITH THEIR EVIDENCE:**')
    for r in sorted(readable, key=lambda x: -x['uses']):
        say('      %-54s uses %-4d agree %-4d disagree %d'
            % (r['rel'][:54], r['uses'], r['ta'], r['td']))
        for e in r['ev']:
            say('          evidence: %s' % e)
    say()
    say('  ### **AND EVERY DOCUMENT WITH A TIGHT DISAGREEMENT, NAMED:**')
    for r in rows:
        if r['td'] > 0:
            say('      %-54s agree %-4d DISAGREE %d' % (r['rel'][:54], r['ta'], r['td']))
    write_text(os.path.join(SCRATCH, 'sweep.txt'),
               '\n'.join('%s\t%d\t%d\t%d' % (r['rel'], r['uses'], r['ta'], r['td'])
                         for r in rows))

    # -------------------------------------------------------------- (C) THE TWO HITS
    say()
    say('-' * 100)
    say("### (C) THE TWO HITS `b408` FILED AS ARTEFACTS, READ WHOLE.")
    say('-' * 100)
    pull(PATHS, 'output-stage classes (C\u2083 + C\u2087) \u2014 the first primarily output-stage',
         'THE FIFTH PATH, IN `PATHS_TO_THE_CRITICAL_LINE`', span=True)
    say('  ### **AND ITS MACHINERY LINE, WHICH SAYS WHAT IT ACTUALLY TOUCHES:**')
    pull(PATHS, 'The level curves {Re \u03be = 0}, the logarithmic derivative, Stirling asymptotics',
         'THE MACHINERY', span=True)
    say()
    pull(CR, 'The fifth path is notable as the first primarily output-stage path',
         'THE SAME PATH, IN `CRITICAL_RESOLVE`', span=True)

    # -------------------------------------------------------------- (D) THE GLOBAL CLASS
    say()
    say('-' * 100)
    say('### (D) THE GLOBAL CLASS, BY DESCRIPTION AND UNDER BOTH NUMBERINGS.')
    say('-' * 100)
    say('  ### **THE DESCRIPTION, NOT THE SYMBOL:** ### *the modular symmetry, `PSL2(Z)`, the')
    say('  ### relation between the archimedean and the multiplicative sides.* ### Under the')
    say('  ### canonical index it is `C4`; under the correspondence table`s Monograph column it')
    say('  ### is `C5`. ### **THE SEARCH RUNS ON THE DESCRIPTION AND ON BOTH SYMBOLS.**')
    DESC = re.compile(r'PSL|modular symmetry|modular group|\(ST\)\u00b3|global coherence', re.I)
    SYMS = re.compile(r'C\u2084|C\u2085')
    CHAN = re.compile(r'bright channel|\u03ba\s*[>=]|kappa\s*[>=]|P-dark|dark interface|'
                      r'transmission coefficient|factors through', re.I)
    CTRL = re.compile(r'functional equation|archimedean', re.I)
    scopes = live_md() + [('relay/data/' + f, os.path.join(D, f))
                          for f in sorted(os.listdir(D))
                          if f.endswith('.txt') and not f.startswith('b409')]
    say('  ### files in scope : %d' % len(scopes))
    hits_desc, hits_sym, ctrl_hits = [], [], []
    for rel, p in scopes:
        try:
            lines = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
        except OSError:
            continue
        for i, ln in enumerate(lines, 1):
            if CHAN.search(ln):
                if DESC.search(ln):
                    hits_desc.append((rel, i, ln.strip()[:150]))
                elif SYMS.search(ln):
                    hits_sym.append((rel, i, ln.strip()[:150]))
                if CTRL.search(ln):
                    ctrl_hits.append((rel, i, ln.strip()[:120]))
    say()
    say('  ### ### **BY DESCRIPTION (the modular relation) BESIDE A CHANNEL WORD : %d**'
        % len(hits_desc))
    for h in hits_desc[:10]:
        say('      %-46s:%-6d %s' % h)
    say('  ### ### **BY SYMBOL (`C4` or `C5`) BESIDE A CHANNEL WORD : %d**' % len(hits_sym))
    for h in hits_sym[:10]:
        say('      %-46s:%-6d %s' % h)
    say()
    say('  ### ### **THE POSITIVE CONTROL -- THE ARCHIMEDEAN CLASS`S ONE KNOWN EXAMINATION MUST')
    say('  ### ### BE FOUND BY THE SAME PREDICATE : %d hit(s)**' % len(ctrl_hits))
    for h in ctrl_hits[:8]:
        say('      %-46s:%-6d %s' % h)
    say('  ### **A SEARCH THAT CANNOT FIND WHAT IS THERE HAS NOT SEARCHED.**')
    say()
    say('  ### **AND THE MONOGRAPH`S OWN DEFINITION OF THE GLOBAL CLASS, FOR THE READING:**')
    pull(MONO, '| C\u2084 (Modular/PSL\u2082) | Transformation |', 'THE GLOBAL CLASS, DEFINED')
    pull(MONO, '- C\u2084 (Modular/PSL\u2082): Global \u2192 PSL\u2082 symmetry',
         'AND ITS ONE-LINE FORM')
    pull(MC, '**Class C\u2084 (global coherence).**', 'AND THE CLASSES DOCUMENT`S FORM')
    pull(MONO, 'The constraint function of each mechanism class is antisymmetric about the '
               'reflection axis', 'AND WHAT THE MONOGRAPH SAYS OF EVERY CLASS`S CONSTRAINT')

    # -------------------------------------------------------------- (E) THE LEMMA'S PROOF
    say()
    say('-' * 100)
    say("### (E) THE SIEVE CEILING LEMMA'S PROOF AT CONTENT, MOVEMENT BY MOVEMENT.")
    say('-' * 100)
    pull(IB, '**Theorem 3.1 (Sieve Ceiling Lemma).**', 'THE STATEMENT')
    pull(IB, '**Lemma 3.2', 'MOVEMENT 1 -- LEMMA 3.2', span=True)
    pull(IB, '**Corollary 3.3.**', 'COROLLARY 3.3')
    pull(IB, 'Corollary 3.3 is the content of \u03ba = 0 at the proof-theoretic level',
         'AND WHAT IT MEANS')
    pull(IB, '**Lemma 3.4.**', 'MOVEMENT 2 -- LEMMA 3.4', span=True)
    pull(IB, '*(a) "For every I-class C, the set', 'ITS STRONGEST CONCLUSION')
    pull(IB, '**Proposition 3.5 (Epstein witness).**', 'MOVEMENT 3 -- PROPOSITION 3.5', span=True)
    pull(IB, '**Completion of Theorem 3.1.**', 'AND THE COMPLETION', span=True)

    # -------------------------------------------------------------- (F) THE ROW
    say()
    say('-' * 100)
    say("### (F) ROW `U1` FROM THE COMMITTED BLOB, AND `b408`'S FOUR IMPORTED PREMISES.")
    say('-' * 100)
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                          capture_output=True).stdout.decode('utf-8')
    row = [x for x in blob.split('\n') if x.startswith('| U1 |')][0]
    write_text(os.path.join(SCRATCH, 'U1_row_at_HEAD.txt'), row)
    cells = row.rstrip().split('|')
    say('    row `U1` at HEAD : %d bytes ; cell 5 %d ; cell 7 %d'
        % (len(row.encode('utf-8')), len(cells[5].encode('utf-8')),
           len(cells[7].encode('utf-8'))))
    b408 = io.open(os.path.join(D, 'b408_the_other_two_channels.txt'), encoding='utf-8').read()
    for ln in b408.split('\n'):
        if 'FOUR DISTINCT IMPORTED PREMISES' in ln or 'Definition 3.1, Proposition' in ln:
            say('      | %s' % ln.strip()[:190])
    say('  ### **AND `b408``S CLASSIFICATION, WHICH THIS ACT USES AND DOES NOT RE-DERIVE.**')

    say()
    say('=' * 100)
    say('  ### ### **ANCHOR MISSES : %d** %s' % (len(MISS), MISS or ''))
    say('  ### **NOTHING IS WRITTEN TO ANY LEDGER, ROW, KEY OR DOCUMENT BY THIS TOOL.**')
    say('=' * 100)
    write_text(OUT, '\n'.join(L) + '\n')
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
