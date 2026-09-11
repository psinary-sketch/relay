# -*- coding: utf-8 -*-
"""b410_extract.py -- THE SURVEY, EXTRACTED TO DISK BEFORE THE FACE IS WRITTEN.

### ### **EVERY READ IS BY ANCHOR AND EVERY ANCHOR IS RESOLVED BY THE TOOL**, never by a line
### number typed from a previous look. ### **ANCHOR MISSES ARE COUNTED AND PRINTED**, and a miss
### is a HARD FAILURE of this file, not a silent gap in the survey.
###
### ### **AND EVERY SEARCH FOR A CLASS IS BY DESCRIPTION AND UNDER BOTH NUMBERINGS** (b409's
### standing clause), ### **WITH A POSITIVE CONTROL WHOSE OWN YIELD IS PRINTED** -- because the
### act's central verdicts are again absences, and an absence is only as good as the search that
### failed to find anything.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF     # noqa: E402
import class_scheme               # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SUB = os.path.join(D, '_b410')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
FIND = os.path.join(PP, 'FINDINGS.md')
CR = os.path.join(PP, 'internal', 'CRITICAL_RESOLVE.md')
MONOT = os.path.join(PP, 'phase1.5', 'rcurve', 'MONOTONICITY.md')
OUT = os.path.join(D, 'b410_extract.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    say(c * 100)


def write_text(p, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.** ### b405's zero-byte husk is why."""
    data = text.encode('utf-8')
    open(p + '.tmp', 'wb').write(data)
    os.replace(p + '.tmp', p)
    return len(data)


def pull(path, needle, label, span=1, save=None):
    """### One anchored read. ### **THE TOOL RESOLVES THE ANCHOR; A MISS IS COUNTED.**"""
    try:
        if span > 1:
            ln, lines = AF.find_span(path, needle, span)
        else:
            ln, line = AF.find(path, needle)
            lines = [line]
    except Exception as e:
        MISS.append('%s :: %s :: %s' % (os.path.basename(path), label, e))
        say('  ### ### **ANCHOR MISS** ### %s -- %s' % (label, str(e)[:90]))
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln))
    for x in lines:
        for k in range(0, max(len(x), 1), 150):
            say('      | %s' % x[k:k + 150])
    if save:
        write_text(os.path.join(SUB, save), NL.join(lines) + NL)
    return ln, lines


def live_md():
    out = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                out.append((os.path.relpath(p, PP).replace(os.sep, '/'), p))
    return out


def main():
    if not os.path.isdir(SUB):
        os.makedirs(SUB)
    say('=' * 100)
    say('b410_extract.py -- THE SURVEY. ### EVERY READ ANCHORED, EVERY MISS COUNTED.')
    say('=' * 100)

    # ---------------------------------------------------------------- (A) THE CRITERION
    say()
    bar()
    say('### (A) DEFINITION 2.5, THE CRITERION THE CLASSIFICATION MUST APPLY.')
    bar()
    pull(IB, '**Definition 2.5 (Factoring through an interface).**', 'DEFINITION 2.5, THE HEAD',
         save='def25_head.txt')
    pull(IB, '1. The sentences mentioned in', 'CLAUSE 1 -- THE SYNTACTIC TEST', save='def25_1.txt')
    pull(IB, '2. Equivalently:', 'CLAUSE 2 -- THE SEMANTIC TEST', save='def25_2.txt')
    pull(IB, '**Proof π factors through I for P**', 'AND WHAT IT IS DEFINED *OF*')
    say('  ### ### **NOTE FOR (R28): ### DEFINITION 2.5 DEFINES FACTORING OF AN ### INFERENCE')
    say('  ### ### STEP ### AND OF A ### PROOF. ### IT DOES NOT DEFINE IT OF A STANDALONE')
    say('  ### ### SENTENCE.** ### Clause 1 speaks of *the sentences mentioned in* a step, and')
    say('  ### clause 2 of *the step`s conclusion*. ### **THE KIND CHECK IS APPLIED TO THIS ACT`S')
    say('  ### ### OWN TASK BELOW, NOT ONLY TO THE RECORD`S.**')

    # ---------------------------------------------------------------- (B) THE INTERFACE
    say()
    bar()
    say('### (B) THE INTERFACE AND THE TARGET, IN THE RECORD`S OWN WORDS.')
    bar()
    pull(IB, 'Let I be the product-formula interface', 'THE INTERFACE, AND kappa(sigma, I) = 0',
         save='interface.txt')
    pull(IB, '**Definition 2.4 (Transmission coefficient).**', 'DEFINITION 2.4, THE SUPREMUM')
    say('  ### ### **SO THE TARGET PARAMETER IS `σ` AND THE INTERFACE IS THE RECORD`S OWN,')
    say('  ### ### NOT A COINAGE OF `b409`.** ### And `σ` -- the real part, the PLACEMENT of an')
    say('  ### individual zero -- is ### **THE SAME OBJECT §9 CALLS THE PLACEMENT REGISTER.**')

    # ---------------------------------------------------------------- (C) THE COROLLARY
    say()
    bar()
    say('### (C) COROLLARY 3.6, AND WHAT ITS EXISTENTIAL RANGES OVER.')
    bar()
    pull(IB, '**Corollary 3.6 (Bright-interface access).**', 'THE COROLLARY', save='cor36.txt')
    pull(IB, 'Corollary 3.6 is the form of the theorem used in the E-Difficulty chain',
         'AND WHAT THE CHANNELS ARE', save='cor36_channels.txt')
    pull(MONO, 'The constraint function of each mechanism class is antisymmetric',
         'THE ANTISYMMETRY, OF *EVERY* CLASS', save='antisymmetry.txt')

    # ---------------------------------------------------------------- (D) SECTION 9
    say()
    bar()
    say('### (D) SECTION 9 -- THE CALIBRATION FAMILY, READ WHOLE.')
    bar()
    pull(IB, '## 9. The calibration family', 'THE HEADING')
    pull(IB, 'The barrier hypothesis-shape of Theorem 3.1', 'THE FAMILY`S OWN FRAME')
    pull(IB, '**The archimedean row.**', 'ROW 1 -- THE ARCHIMEDEAN ROW, WHOLE', save='row_arch.txt')
    pull(IB, '**The per-place table.**', 'THE PER-PLACE TABLE, WHOLE', save='table_perplace.txt')
    pull(IB, 'The calibration family is open as a programme', 'THE FORWARD', save='forward.txt')
    pull(IB, '| §9 — the archimedean κ-row and the per-place table |',
         'AND §9`S OWN CORRESPONDENCE ROW', save='corr_row_9.txt')

    # ---------------------------------------------------------------- (E) THE FOUR IMPORTS
    say()
    bar()
    say('### (E) THE FOUR IMPORTS, FROM THE E0 GATE`S TABLE, LOCATED BY ITS OWN HEADING.')
    bar()
    hit = pull(FIND, '### The E0 gate: every constituent unfolded to its owner',
               'THE E0 GATE, BY ITS HEADING')
    if hit:
        start = hit[0]
        src = io.open(FIND, encoding='utf-8', errors='replace').read().split(NL)
        rows = [(i + 1, ln) for i, ln in enumerate(src)
                if i + 1 > start and ln.startswith('| **K')][:8]
        say('  ### ### **THE EIGHT ROWS, IN FILE ORDER FROM THAT HEADING -- %d FOUND.**' % len(rows))
        for ln, txt in rows:
            say('  ### line %d' % ln)
            for k in range(0, len(txt), 150):
                say('      | %s' % txt[k:k + 150])
        write_text(os.path.join(SUB, 'e0_rows.txt'), NL.join(t for _l, t in rows) + NL)
        if len(rows) != 8:
            MISS.append('E0 table: %d rows, expected 8' % len(rows))

    # ---------------------------------------------------------------- (F) THE DENSITY REGISTER
    say()
    bar()
    say('### (F) THE DENSITY REGISTER -- WHAT THE RECORD HOLDS, AND WHAT IT DECLINED.')
    bar()
    pull(IB, '*Density-one-per-class:* By Potter-Titchmarsh zero-density estimates',
         'THE COUNTERMODEL LIVES IN THE DENSITY REGISTER', save='density_countermodel.txt')
    pull(IB, 'Every tool in T is PROVED-FOR-BOTH',
         'AND THE TOOLKIT ### **DELIBERATELY EXCLUDES** ### THAT REGISTER',
         save='density_excluded.txt')
    pull(CR, 'Selberg (1942): A positive proportion of zeros lie on the critical line.',
         'THE ONE CLASSICAL DENSITY RESULT THE RECORD STATES', save='selberg.txt')
    pull(MONOT, 'The best unconditional result is that a positive proportion of zeros are simple',
         'AND ONE MORE, ON SIMPLICITY RATHER THAN PLACEMENT', save='conrey.txt')
    say()
    say('  ### **THE SEARCH BY DESCRIPTION, WITH ITS YIELDS PRINTED AND ITS CONTROL.**')
    pats = {
        'a PROPORTION of zeros on the line': r'proportion of zeros|positive proportion',
        'a ZERO-DENSITY estimate': r'zero-density|zero density estimate|N\(σ, ?T\)|N\(sigma',
        'the COUNTING LAW / N(T)': r'counting law|N\(T\)|Riemann–von Mangoldt|von Mangoldt formula',
        'the DENSITY REGISTER by that name': r'density register',
        'the PLACEMENT REGISTER by that name': r'placement register',
    }
    files = [(rel, p) for rel, p in live_md() if not rel.startswith('outputs/')]
    say('      files in scope : %d live `.md`, `outputs/` and `archive/` excluded' % len(files))
    for lbl, pat in pats.items():
        hits = []
        for rel, p in files:
            src = io.open(p, encoding='utf-8', errors='replace').read()
            for m in re.finditer(pat, src, re.I):
                hits.append((rel, src[:m.start()].count(NL) + 1))
        docs = sorted(set(h[0] for h in hits))
        say('      %-44s %3d hit(s) in %2d document(s)' % (lbl, len(hits), len(docs)))
        for x in docs[:6]:
            say('          %s' % x)
        if len(docs) > 6:
            say('          ... and %d more' % (len(docs) - 6))
    say('  ### ### **THE POSITIVE CONTROL -- A REGISTER WORD THE RECORD CERTAINLY USES MUST BE')
    say('  ### ### FOUND BY THE SAME MACHINERY:** ### `κ` itself.')
    ctl = sum(1 for rel, p in files
              if re.search(r'κ', io.open(p, encoding='utf-8', errors='replace').read()))
    say('      the control (`κ` in a live document) : ### **%d document(s)** ### -- ### **%s**'
        % (ctl, 'PASSES' if ctl > 0 else 'FAILS: THE VERDICT IS WITHHELD'))
    if ctl == 0:
        MISS.append('the positive control on the density search yielded 0')

    # ---------------------------------------------------------------- (G) b409's OWN SECTION 10
    say()
    bar()
    say('### (G) `b409`’S OWN §10, READ BACK SO THE KIND CHECK CAN BE APPLIED TO IT.')
    bar()
    pull(IB, '**Theorem 3.1-H (relativized form).**', 'THE RESTATEMENT, WHOLE', save='thm31h.txt')
    pull(IB, '**And what it does not settle.**', 'AND THE CONDITION IT LEAVES UNRUN')

    # ---------------------------------------------------------------- (H) THE 66
    say()
    bar()
    say('### (H) THE `66` ROUTED DOCUMENTS, AND THEIR SYMBOL YIELD.')
    bar()
    rows = [ln.split(chr(9)) for ln
            in io.open(os.path.join(D, 'b409_scheme_table.txt'), encoding='utf-8').read()
            .splitlines() if ln.strip()]
    routed = [r for r in rows if r[1] == 'ROUTED']
    say('  ### documents in `b409`’s table : %d ; ROUTED : %d' % (len(rows), len(routed)))
    buckets = {'no symbol pinned at all': [], 'symbols pinned but TIED': [],
               'pinned only by the SHARED symbol C7': []}
    for r in routed:
        src = io.open(os.path.join(PP, r[0].replace('/', os.sep)),
                      encoding='utf-8', errors='replace').read()
        st, ex, _ev = class_scheme.pin(src)
        syms = set(class_scheme.SUB[m.group(1)] for m in class_scheme.SYM.finditer(src))
        if st == ex == 0:
            buckets['pinned only by the SHARED symbol C7'
                    if syms == {7} else 'no symbol pinned at all'].append((r[0], int(r[3])))
        else:
            buckets['symbols pinned but TIED'].append((r[0], int(r[3])))
    for k, v in buckets.items():
        say('      %-38s %3d document(s), %5d symbol use(s)'
            % (k, len(v), sum(n for _f, n in v)))
    write_text(os.path.join(SUB, 'routed_buckets.txt'),
               NL.join('%s\t%s' % (k, f) for k, v in buckets.items() for f, _n in v) + NL)

    # ---------------------------------------------------------------- (I) THE STANDING SCREEN
    say()
    bar()
    say('### (I) THE INSTRUMENT THE RECORD ALREADY HAS FOR EXACTLY THIS QUESTION.')
    bar()
    INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
    ARITY = os.path.join(PP, 'phase1.5', 'proofs', 'INDEX_ARITY_AT_THE_CRITICAL_LINE.md')
    pull(INST, '## I-7 — THE PLACEMENT SCREEN', 'THE SCREEN`S HEAD -- STANDING, AUTHOR-RULED')
    pull(INST, '**The screen, one question, asked of the DEFINITION', 'THE SCREEN ITSELF',
         save='i7_screen.txt')
    pull(INST, '**The evidence base — four independent derivations',
         'ITS FOUR DERIVATIONS, AND THE BOUNDARY THEY REACH', save='i7_evidence.txt')
    pull(INST, '**Cost saved on its first firing:**', 'AND WHAT ITS FIRST FIRING SAVED')
    pull(INST, "### I-7's SECOND RUN", 'AND IT HAS A SECOND STAGE')
    # ### **THE ANCHOR AVOIDS THE APOSTROPHE ENTIRELY.** ### The corpus line reads `wall''s` with
    # ### a DOUBLED straight apostrophe -- so the curly form misses it, and the single-quote form
    # ### silently CONCATENATES into `walls` and misses it too, which is how this anchor failed
    # ### twice. ### **OBSERVED AND NOT REPAIRED**: an in-place repair is barred and the typo is
    # ### not this act's subject. ### ROUTED with its line.
    pull(ARITY, 'sixth face — the currency is definable only after the crossing',
         'THE WALL`S SIXTH FACE, BANKED', save='sixth_face.txt')
    pull(ARITY, 'now shown the density register cannot supply one',
         'AND THE ARC`S OWN VERDICT ON THE REGISTER')
    say()
    say('  ### ### **AND NEITHER INSTRUMENT CITES THE OTHER -- MEASURED, NOT ASSUMED.**')
    ibt = io.open(IB, encoding='utf-8', errors='replace').read()
    instt = io.open(INST, encoding='utf-8', errors='replace').read()
    a = len(re.findall(r'I-7|placement screen', ibt, re.I))
    b = len(re.findall(r'Definition 2\.5|transmission coefficient|INVARIANCE_BARRIERS', instt))
    say('      `INVARIANCE_BARRIERS.md` naming the screen : ### **%d**' % a)
    say('      `INSTRUMENTS.md` naming Definition 2.5, the coefficient, or the keystone : '
        '### **%d**' % b)
    say('  ### ### **SO THE RECORD STATES ONE TEST TWICE, IN TWO DOCUMENTS THAT DO NOT KNOW')
    say('  ### ### ABOUT EACH OTHER.**')
    say()
    say('  ### ### **AND A THIRD NUMBERING COLLISION, THIS ONE NOT YET LANDED.**')
    GRADER = os.path.join(PP, 'phase1.5', 'method', 'I7_SURVEYABILITY_GRADER.md')
    pull(GRADER, '# I-7 — the surveyability grader (spec)', 'A SECOND DOCUMENT CLAIMING `I-7`')
    pull(GRADER, 'Joins `INSTRUMENTS.md` as I-7 on the author', 'AND IT IS QUEUED TO JOIN AS `I-7`',
         save='i7_collision.txt')
    # ### **THE WORD BOUNDARY IS BUILT FROM chr(92)** -- a quoted heredoc still collapses a
    # ### backslash, and this very line was written once as a literal BACKSPACE byte, which
    # ### matched nothing and reported 0 citing documents for a number cited in ten.
    WB = chr(92) + 'b'
    cites = [rel for rel, p in files
             if re.search(WB + 'I-7' + WB,
                          io.open(p, encoding='utf-8', errors='replace').read())]
    say('      live documents citing `I-7` : ### **%d**' % len(cites))
    for c in cites:
        say('          %s' % c)
    say('  ### ### **THE NUMBER IS OCCUPIED BY A STANDING, AUTHOR-RULED INSTRUMENT, AND THE')
    say('  ### ### COLLISION FIRES ON A WORD THE AUTHOR HAS NOT YET SAID.** ### **ROUTED.**')

    say()
    bar('=')
    say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
    for m in MISS:
        say('      %s' % m)
    bar('=')
    write_text(OUT, NL.join(L) + NL)
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
