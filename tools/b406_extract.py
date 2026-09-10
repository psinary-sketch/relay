# -*- coding: utf-8 -*-
"""b406_extract.py -- EXTRACT-TO-DISK. ### EVERY READ THIS ACT MAKES, PULLED BY THE ANCHOR TOOL.

### ### (A) The two sites without an existential, from the COMMITTED BLOB of row `U1`.
### ### (B) The record's own name for the other form -- searched BY DESCRIPTION, never by this
###     seat's name for it, and quoted at its source or reported ABSENT.
### ### (C) `(iii)`'s inner existential in the source's own symbols, as `b353` banks them.
### ### (D) The standing laws, for Addition Two's arity audit, each quoted whole.
### ### (E) The finite side's qualifier: the seal's own header, and every LIVE citation of the
###     seal's terminals swept and classified QUALIFIED / UNQUALIFIED.
### ### (F) The navigator's own banked ferries, swept by the same predicate.
###
### ### **THE SUBJECT OF THE SWEEP IS THE SEAL, NOT THE WORDS.** ### The h2 programme's
### ### `TraceSilence` says *trace silence at the finite places* about a DIFFERENT OBJECT in
### ### different repositories. ### **A SWEEP THAT REPAIRS A SENTENCE ABOUT ANOTHER OBJECT BECAUSE
### ### IT USES THE SAME ENGLISH IS NOT A REPAIR, IT IS A NEW DEFECT** -- so the predicate requires
### ### a citation of the seal's own terminals, and the wider yield is PRINTED beside it.
###
### ### **AND EVERY WRITE ENCODES BEFORE IT OPENS** (`b405`'s zero-byte husk).
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
OUT = os.path.join(D, 'b406_extract.txt')
SCRATCH = os.path.join(D, '_b406')
PP = r'D:\MY-DOwnloads\PLACE-papers'
GS = r'D:\SIDE-global-section'

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def write_text(path, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND** -- b405's husk."""
    data = text.encode('utf-8')
    io.open(path, 'wb').write(data)
    return len(data)


def pull(path, hint, label, span=False):
    try:
        if span:
            ln0, run = AF.find_span(path, hint)
            txt = '\n'.join(run)
        else:
            ln0, txt = AF.find(path, hint)
    except AF.AnchorError as e:
        MISS.append(label)
        say('  ### ANCHOR MISS -- %s' % label)
        say('      hint : %r' % hint)
        say('      %s' % str(e).splitlines()[0][:190])
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln0))
    for ln in txt.splitlines():
        say('      | %s' % ln[:600])
    return txt


# ### ==================================================================================================
# ### THE SWEEP'S PREDICATES, WRITTEN ONCE AND PRINTED WITH THEIR YIELDS.
# ### ==================================================================================================
SEAL = re.compile(r'FiniteSideSeal|B329|compact_smear_vanishes|finite_side_silence')
WIDE = re.compile(r'finite[- ]side|finite places|trace silence', re.I)
# ### **THE NARROW CLOSURE VERB SET WAS A PROPERTY OF THE MATCHER, NOT OF THE RECORD.**
# ### Its first version -- compiled / sealed / closed / proved / certified / silent /
# ### established -- returned `0` UNQUALIFIED and would have banked "nothing to repair".
# ### ### **IT MISSED THE CORPUS'S OWN HOUSE FORM FOR THE CLAIM**, which is not a verb at
# ### ### all: *at kernel terminals `B329.*` (24, zero-axiom)*. ### Both yields are printed
# ### and the narrow one is kept only as the thing that was too small.
CLOSE_NARROW = re.compile(r'compiled|sealed|closed|proved|certif|silen|establish', re.I)
CLOSE = re.compile(r'compiled|sealed|closed|proved|certif|silen|establish|kernel terminals?|zero-axiom|carr(?:y|ies|ied) it', re.I)
QUAL = re.compile(r'per[- ]cell|beyond the cells|over no other|and no other|seven[- ]cells?|'
                  r'explicit list|PROVED-AT-CELLS|PROVED-PER-CELL|never averaged|decided over|'
                  r'banked cells|listed cell|at the cells|six cells|at seven|decided list|'
                  r'general and per-cell|the per-cell compact part', re.I)
# ### **INSTRUMENT OUTPUT IS NOT A READER-FACING SENTENCE.** ### A `#print axioms` line naming a
# ### terminal is a MEASUREMENT, not a claim about the finite side, and sweeping it would drown the
# ### real yield in 200 lines of profile. ### The exclusion is PRINTED, with its own count.
PROFILE = re.compile(r"does not depend on any axioms|depends on axioms|"
                     r"^\s*'B329\.|AllPrints|\.olean|compiled object")


def sweep(paths, label, subject, own_prefix=None):
    rows = []
    excluded = 0
    for rel, p in paths:
        try:
            src = io.open(p, encoding='utf-8', errors='replace').read().split('\n')
        except OSError:
            continue
        for i, ln in enumerate(src, 1):
            if not (subject.search(ln) and CLOSE.search(ln)):
                continue
            if PROFILE.search(ln):
                excluded += 1
                continue
            near = ' '.join(src[max(0, i - 4):i + 4])
            rows.append(dict(file=rel, line=i, qual=bool(QUAL.search(near)),
                             qual_same=bool(QUAL.search(ln)), text=ln.strip()))
    say('  ### %s' % label)
    say('      lines matching subject AND a closure verb : %d' % (len(rows) + excluded))
    say('      excluded as INSTRUMENT OUTPUT (a profile line is a measurement, not a claim) : %d'
        % excluded)
    say('      reader-facing candidates : %d ; QUALIFIED within reach : %d ; UNQUALIFIED : %d'
        % (len(rows), sum(1 for r in rows if r['qual']), sum(1 for r in rows if not r['qual'])))
    for r in rows:
        say('      %-10s %-46s:%-6d %s'
            % ('QUALIFIED' if r['qual'] else '### UNQUAL', r['file'], r['line'],
               r['text'][:110]))
    return rows


def live_md():
    out = []
    bs = chr(92)
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive', 'outputs')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                out.append((os.path.relpath(p, PP).replace(bs, '/'), p))
    return out


def main():
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    say('=' * 100)
    say('b406_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.')
    say('=' * 100)
    ok = AF.self_test(verbose=False)
    say('  anchor tool self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        return 2

    # ---------------------------------------------------------------- (A) THE TWO SITES
    say()
    say('-' * 100)
    say('### (A) THE TWO SITES WITHOUT AN EXISTENTIAL, FROM THE COMMITTED BLOB.')
    say('-' * 100)
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FACES_LEDGER.md'],
                          capture_output=True).stdout.decode('utf-8')
    row = [l for l in blob.split('\n') if l.startswith('| U1 |')]
    assert len(row) == 1
    cells = row[0].rstrip().split('|')
    write_text(os.path.join(SCRATCH, 'U1_row_at_HEAD.txt'), row[0])
    say('    row U1 at HEAD : %d bytes, %d pipe-pieces'
        % (len(row[0].encode('utf-8')), len(cells)))
    c5 = cells[5]
    for tag, name in (('**(i) ', '(i) THE CLAUSE\u2019S QUANTIFIER'),
                      ('**(iv) ', '(iv) THE PRIME CONSTITUENT AT A WIDENED SUPPORT')):
        at = c5.find(tag)
        end = min([x for x in (c5.find('### **(', at + 4), len(c5)) if x > 0])
        seg = c5[at:end]
        say('  ### %s   [cell 5 offset %d, %d bytes]' % (name, at, len(seg.encode('utf-8'))))
        for k in range(0, min(len(seg), 2400), 150):
            say('      | %s' % seg[k:k + 150])
    say()
    say('  ### AND THE b405 CELLS THOSE TWO NOW CARRY:')
    for tag in ('**`(i)` \u2014 KIND', '**`(iv)` \u2014 KIND'):
        at = c5.find(tag)
        seg = c5[at:at + 620] if at >= 0 else '### NOT FOUND'
        for k in range(0, len(seg), 150):
            say('      | %s' % seg[k:k + 150])
        say('      ---')

    # ---------------------------------------------------------------- (B) THE NAME
    say()
    say('-' * 100)
    say("### (B) THE RECORD'S OWN NAME FOR THE OTHER FORM -- SEARCHED BY DESCRIPTION.")
    say('-' * 100)
    say('  ### **THE SEARCH IS BY THE FORM\u2019S DESCRIPTION, NOT BY THIS SEAT\u2019S NAME FOR IT**')
    say('  ### (`search-by-the-rules-own-words`): *what is called the barrier between statements')
    say('  ### holding at each instance and one statement holding across them, and what is called')
    say('  ### the thing that closes it.*')
    ib = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
    dk = os.path.join(PP, 'phase1.5', 'method', 'THE_DIFFICULTY_KINDS.md')
    say()
    pull(ib, 'Theorem 3.1 (Sieve Ceiling Lemma)', 'THE BARRIER, NAMED AND STATED', span=True)
    pull(ib, 'can establish "P holds for x in a density-one subset of each I-class,"',
         'ITS OWN STATEMENT OF WHAT SURVIVES THE BARRIER')
    say()
    pull(ib, 'Corollary 3.6 (Bright-interface access)', 'THE REPAIR, NAMED', span=True)
    pull(ib, 'any proof of universality must contain at least one inference step',
         "AND THE RECORD'S NAME FOR IT, IN ITS OWN WORDS")
    say()
    pull(ib, 'the fraction of P-dependent information that crosses',
         'THE MECHANISM: THE TRANSMISSION COEFFICIENT')
    say()
    pull(dk, 'classifies *why* finite certificates don', 'THE CLASSIFICATION OF THE GAP ITSELF')
    pull(dk, 'TWO escape-kinds suffice', 'ITS TWO KINDS, AND THE VERDICT ON THEM')

    # ---------------------------------------------------------------- (C) (iii)'s EXISTENTIAL
    say()
    say('-' * 100)
    say("### (C) `(iii)`'S INNER EXISTENTIAL, IN THE SOURCE'S OWN SYMBOLS.")
    say('-' * 100)
    b353 = os.path.join(D, 'b353_the_missing_statement.txt')
    pull(b353, 'There exists g in Cc^infty(R)', 'BOAS-KAC, AS b353 QUOTES IT', span=True)
    pull(b353, 'RH <=> sum_v W_v(g * gbar', 'THE CRITERION THE WIDTH SERVES', span=True)
    pull(b353, 'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS',
         'AND THE GAP IT LEAVES', span=True)

    # ---------------------------------------------------------------- (D) THE LAWS
    say()
    say('-' * 100)
    say('### (D) THE STANDING LAWS, EACH QUOTED WHOLE, FOR THE ARITY AUDIT.')
    say('-' * 100)
    trails = os.path.join(PP, 'OPEN_TRAILS.md')
    faces = os.path.join(PP, 'FACES_LEDGER.md')
    pull(faces, 'THE DEPOSIT\u2019S REFUSAL GOVERNS THIS LEDGER',
         "THE DEPOSIT'S \u00a727.3 REFUSAL, AS THE LEDGER'S OWN HEAD CARRIES IT")
    say()
    pull(trails, 'RATIFIED BY THE FERRY AND RECORDED HERE', '(R14), WHOLE')
    say()
    pull(trails, 'THE DEPOSIT RULE, WRITTEN, WITH A CURRENCY OBLIGATION', '(R20), WHOLE')
    say()
    pull(os.path.join(D, 'b366_ferry_2026-09-07.txt'), 'THE FOLD THRESHOLD is NINE acts',
         '(R1), WHOLE', span=True)

    # ---------------------------------------------------------------- (E) THE QUALIFIER SWEEP
    say()
    say('-' * 100)
    say("### (E) THE FINITE SIDE'S QUALIFIER: THE SEAL'S OWN HEADER, THEN EVERY LIVE CITATION.")
    say('-' * 100)
    seal = os.path.join(GS, 'Core', 'FiniteSideSeal.lean')
    pull(seal, 'THE GENERAL AND THE PER-CELL ARE STATED HERE SEPARATELY',
         "THE SEAL'S OWN HEADER QUALIFIER", span=True)
    pull(seal, 'PER CELL (decided by finite evaluation over the explicit list',
         'AND THE HEADER LINE THAT SCOPES THE COMPACT PART', span=True)
    pull(seal, 'WHY COMPONENT 3 IS PER CELL AND NOT GENERAL',
         'AND WHY, IN THE SEAL\u2019S OWN WORDS')
    say()
    rows = sweep(live_md(), 'THE SWEEP, SCOPED TO CITATIONS OF THE SEAL\u2019S OWN TERMINALS',
                 SEAL)
    say()
    say('  ### **AND THE WIDER SHAPE, THROWN OUT WITH ITS YIELD PRINTED** ### (`a-filter-that-')
    say('  ### keeps-nine-tenths`): the same sweep on the WORDS *finite side / finite places /')
    say('  ### trace silence*, which reaches a DIFFERENT OBJECT -- the h2 programme\u2019s')
    say('  ### `TraceSilence`, `general_p_no_fixed_cell` and `Grading.*`, in other repositories.')
    wide = sweep(live_md(), 'THE WIDE SWEEP, PRINTED AND NOT ACTED ON', WIDE)
    say('  ### ### **THE WIDE SWEEP IS NOT HAND-READ HERE AND NOTHING IN IT IS REPAIRED.** ### A')
    say('  ### sentence about another object is not an unqualified sentence about this one.')

    # ---------------------------------------------------------------- (F) THE FERRIES
    say()
    say('-' * 100)
    say("### (F) THE NAVIGATOR'S OWN BANKED FERRIES, SWEPT BY THE SAME PREDICATE.")
    say('-' * 100)
    fer = [(f, os.path.join(D, f)) for f in sorted(os.listdir(D))
           if 'ferry' in f and f.endswith('.txt') and not f.endswith('_scan.txt')
           and not f.startswith('b406')]
    frows = sweep(fer, 'THE FERRIES', re.compile(r'finite side|finite-side|B329|FiniteSideSeal',
                                                 re.I))
    say('  ### ### **A FERRY IS THE NAVIGATOR\u2019S OWN WORDS AND A PRIOR ACT\u2019S BANK.** ###')
    say('  ### It is DECLARED here and ### **NOT REPAIRED**: this seat does not edit the')
    say('  ### navigator\u2019s text, and a banked ferry is not a living record.')

    say()
    say('=' * 100)
    say('  ### ### **ANCHOR MISSES : %d** %s' % (len(MISS), MISS or ''))
    say('  ### **NOTHING IS WRITTEN TO ANY LEDGER, BANK, ROW OR KEY BY THIS TOOL.**')
    say('=' * 100)
    write_text(OUT, '\n'.join(L) + '\n')
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
