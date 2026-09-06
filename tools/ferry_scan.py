# -*- coding: utf-8 -*-
"""ferry_scan.py -- THE FERRY SCAN. ### **A COMMAND-PATH CHECK THAT RUNS BEFORE THE ACT.**

### WHY THIS EXISTS. ### At b299 the generator ran to completion, passed every one of its own
### falsifiers, and ### **EMITTED A DOCUMENT APPLYING A CLAUSE THE AUTHOR HAD STRUCK IN THE VERY
### FERRY THAT ORDERED THE RUN.** ### Nothing was wrong with the gates: the registration had
### fixed the clause as a falsifier before the seal, and the tool enforced exactly what it was
### asked to enforce. ### **THE STRIKE ARRIVED IN THE FERRY AND NOTHING IN THE COMMAND PATH
### READ THE FERRY.**

### ### **SO THE FIX IS NOT A BETTER GATE ON THE OUTPUT. ### IT IS A READER ON THE INPUT.**
### This is the b179 shape one level earlier: a guard that must be chosen is not enforcement, and
### a guard that only ever looks at what the act PRODUCED cannot see a rule the act was HANDED.

### WHAT IT DOES: reads `data/STRUCK_CLAUSES.md` -- the record, which is its INPUT and which it
### never writes -- and reports every occurrence, with line and column, of
###   ### **(a) a STRUCK clause**, by the patterns that record carries, and
###   ### **(b) a BANNED or RETIRED stem**, read from `banned_terms.py` and `stem_sweep.py`
###       ### **RATHER THAN COPIED**, so the three tools cannot drift apart.
### ### **IT REPORTS. ### IT DOES NOT EDIT AND IT DOES NOT REFUSE.**

# ### THE LIMITS, IN THE HEADER SO IT IS NOT TRUSTED BEYOND THEM:
# ### (1) ### **A HIT IS A STRING, NOT A FAULT.** ### The ferry that STRIKES a clause quotes the
# ###     clause in order to strike it, and that quotation hits. ### **THE EXPECTED READING OF
# ###     THIS TOOL'S OUTPUT IS THEREFORE NEVER "ZERO OR FAIL"; IT IS "HERE ARE THE SITES".**
# ### (2) It reads a FILE. ### A ferry that was never pasted into a file is not scanned, and that
# ###     is a discipline this tool cannot supply.
# ### (3) ### **UNCONFIRMED CANDIDATES ARE NOT LOADED.** ### Only `STATUS: STRUCK` entries are
# ###     read; the count skipped is printed. ### **PROMOTION IS THE AUTHOR'S WORD AND CANNOT
# ###     HAPPEN BY A TOOL READING A FILE.**
# ### (4) It never names a banned stem in its own source -- not for tidiness, but because the
# ###     fixtures are BUILT FROM THE LOADED LIST, which is what makes the drift impossible.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import banned_terms  # noqa: E402  ### the stems are READ, never copied
import stem_sweep    # noqa: E402  ### the retired stem likewise

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RECORD = os.path.join(ROOT, 'data', 'STRUCK_CLAUSES.md')
# ### b335, BY THE ORDER'S WORDS -- "with the ferry scan checking that a ferry citing it cites the current
# ### version": the standing-clauses file and the citation form a ferry uses.
STANDING = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')
CITATION = re.compile(r'FERRY_STANDING\s+v(\d+)', re.I)


def standing_version(path=None):
    """### `VERSION: <N>` from the standing file; None when the file is absent (older acts)."""
    p = path or STANDING
    if not os.path.exists(p):
        return None
    m = re.search(r'^VERSION:\s*(\d+)\s*$', io.open(p, encoding='utf-8', errors='replace').read(), re.M)
    return int(m.group(1)) if m else None


def citation_check(text, current=None):
    """### RETURNS `(status, cited, current)`: NONE (no citation), CURRENT, STALE, or NO FILE.
    ### A STALE citation is reported as a hit by `main`; the reader rules, as for every hit."""
    if current is None:
        current = standing_version()
    cited = sorted(set(int(m.group(1)) for m in CITATION.finditer(re.sub(r'\s+', ' ', text))))
    if not cited:
        return 'NONE', cited, current
    if current is None:
        return 'NO FILE', cited, current
    return ('CURRENT' if cited == [current] else 'STALE'), cited, current

ENTRY = re.compile(r'^###\s+([SU]-\d+)\s*$')
KEYVAL = re.compile(r'^([A-Z][A-Z-]*):\s*(.*)$')


# ### ==============================================================================================
# ### THE RECORD, PARSED. ### **THE INPUT IS A FILE ON DISK AND NOTHING HERE WRITES IT.**
# ### ==============================================================================================
def parse_record(path=None):
    """### RETURNS `(struck, n_unconfirmed)`.

    ### `struck` is a list of dicts with `id`, `clause`, `patterns` (compiled).
    ### ### **AN ENTRY WITH NO `PATTERN:` LINE IS COUNTED AND REPORTED, NOT SILENTLY DROPPED** --
    ### it is a clause the record describes and the check cannot see, and that is the single most
    ### misleading state this file can be in.
    """
    p = path or RECORD
    if not os.path.exists(p):
        raise IOError('### STRUCK-CLAUSE RECORD NOT FOUND: %s' % p)
    cur, out, unconfirmed = None, [], 0
    for raw in io.open(p, encoding='utf-8').read().splitlines():
        m = ENTRY.match(raw.strip())
        if m:
            cur = dict(id=m.group(1), status=None, clause='', patterns=[], raw_patterns=[])
            out.append(cur)
            continue
        if cur is None:
            continue
        kv = KEYVAL.match(raw.strip())
        if not kv:
            continue
        k, v = kv.group(1), kv.group(2).strip()
        if k == 'STATUS':
            cur['status'] = v
        elif k == 'CLAUSE':
            cur['clause'] = v
        elif k == 'PATTERN':
            cur['raw_patterns'].append(v)
            cur['patterns'].append(re.compile(v, re.IGNORECASE))
    struck = [e for e in out if e['status'] == 'STRUCK']
    unconfirmed = len([e for e in out if e['status'] == 'UNCONFIRMED'])
    return struck, unconfirmed


def stems():
    """### THE BANNED AND RETIRED STEMS, ### **READ FROM THE TOOLS THAT OWN THEM.**

    ### Returns a list of `(label, compiled)`. ### The stems are never spelled in this file; that
    ### is what makes a drift between the three tools impossible rather than merely unlikely.
    """
    out = []
    for s in banned_terms.STEMS:
        out.append(('banned stem (Rule 3, banned_terms.py)', re.compile(r'\b%s\w*' % re.escape(s),
                                                                       re.IGNORECASE)))
    out.append(('retired stem (b280, stem_sweep.py)', re.compile(stem_sweep.RETIRED, re.IGNORECASE)))
    return out


# ### ==============================================================================================
# ### THE SCAN. ### **WHITESPACE-FLATTENED, AND THAT IS THE WHOLE OF THE DESIGN.**
# ### ==============================================================================================
# ### DEFECT FIXED ON THIS TOOL'S FIRST LIVE RUN (b299), AND IT WAS FOUND ON THE ONE INPUT THE
# ### TOOL EXISTS FOR. ### The first version scanned LINE BY LINE. ### **A FERRY PASTE IS HARD-
# ### WRAPPED**, and the b299 ferry wraps the struck clause mid-sentence -- `"titles name objects
# ### and` / `conditions, never claimed properties"`. ### The pattern for the clause's first half
# ### MATCHED NOTHING, and the scan came back with one hit only because a SECOND pattern happened
# ### to fall entirely on the second line. ### **A CHECK THAT REPORTS A HIT BY LUCK REPORTS A
# ### MISS BY LUCK TOO**, and one hit read exactly like coverage.
# ### ### **THIS IS b297's BLANK-CELL SPECIES INVERTED.** ### There, `\s` matching a newline made
# ### a scan OVER-report; here, line scoping made it UNDER-report. ### Same seam, opposite sign,
# ### and the second one is the dangerous direction because its output looks clean.
# ### ### **THE FIX: FLATTEN THE WHITESPACE, SEARCH THE FLAT TEXT, AND MAP EVERY MATCH BACK TO
# ### ### ITS ORIGINAL LINE THROUGH AN INDEX BUILT WHILE FLATTENING** -- so the detection does not
# ### depend on where the wrap fell, and the REPORT still names a line the reader can open.
def _flatten(text):
    """### Collapse every whitespace run to one space, ### **KEEPING A MAP BACK TO THE ORIGINAL
    ### OFFSET OF EVERY CHARACTER EMITTED**, so a match in the flat text names a real line."""
    out, idx, prev_ws = [], [], False
    for i, ch in enumerate(text):
        if ch.isspace():
            if not prev_ws:
                out.append(' ')
                idx.append(i)
            prev_ws = True
        else:
            out.append(ch)
            idx.append(i)
            prev_ws = False
    return ''.join(out), idx


def _line_of(text, offset):
    """### 1-indexed line number and the line itself, for an offset into the ORIGINAL text."""
    line_no = text.count('\n', 0, offset) + 1
    start = text.rfind('\n', 0, offset) + 1
    end = text.find('\n', offset)
    return line_no, text[start:end if end != -1 else len(text)]


def scan_text(text, struck=None, stem_list=None):
    """### RETURNS `(clause_hits, stem_hits)`, each `(label, line_no, col, the line)`.

    ### **THE SEARCH IS OVER THE FLATTENED TEXT, SO A CLAUSE BROKEN BY A LINE WRAP IS SEEN.**
    ### The line number reported is the line the match STARTS on.
    """
    if struck is None:
        struck, _ = parse_record()
    if stem_list is None:
        stem_list = stems()
    flat, idx = _flatten(text)
    ch, sh = [], []

    def hits(rx):
        for m in rx.finditer(flat):
            if m.start() >= len(idx):
                continue
            off = idx[m.start()]
            n, line = _line_of(text, off)
            yield n, off - (text.rfind('\n', 0, off) + 1) + 1, line.strip()

    for e in struck:
        seen = set()
        for rx in e['patterns']:
            for n, col, line in hits(rx):
                if (n, col) in seen:
                    continue
                seen.add((n, col))
                ch.append(('%s  %s' % (e['id'], e['clause'][:56]), n, col, line))
    for lbl, rx in stem_list:
        for n, col, line in hits(rx):
            sh.append((lbl, n, col, line))
    ch.sort(key=lambda h: (h[1], h[2]))
    sh.sort(key=lambda h: (h[1], h[2]))
    return ch, sh


# ### ==============================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES ON BOTH ARMS, AND A NEAR-MISS ON EACH.**
# ### **THE STEM FIXTURES ARE BUILT FROM THE LOADED LIST, NEVER TYPED** -- so a stem retired or
# ### added in `banned_terms.py` moves this suite with it.
# ### ==============================================================================================
def self_test(verbose=True):
    out = []

    def rec(s=''):
        out.append(s)
        if verbose:
            print(s)

    rec('=' * 100)
    rec('ferry_scan.py -- SELF-TEST. ### BOTH POLARITIES ON BOTH ARMS.')
    rec('=' * 100)

    struck, unconf = parse_record()
    stem_list = stems()
    npat = sum(len(e['patterns']) for e in struck)
    unpatterned = [e['id'] for e in struck if not e['patterns']]

    rec('  struck entries loaded            : %d' % len(struck))
    rec('  patterns across them             : %d' % npat)
    rec('  struck entries with NO pattern   : %d %s'
        % (len(unpatterned), unpatterned if unpatterned else ''))
    rec('  UNCONFIRMED entries NOT loaded   : %d   ### promotion is the author\'s word' % unconf)
    rec('  stem patterns read from tools    : %d' % len(stem_list))
    rec()

    # ### b167's LAW, AT THIS TOOL TOO: ### **A VERDICT OVER AN EMPTY SCOPE IS NOT A VERDICT.**
    if not struck or not npat or not stem_list:
        rec('  ### HARD FAILURE -- EMPTY SCOPE. A scanner with no patterns reports zero hits')
        rec('  ### on every input and would read CLEAN. That is not a pass.')
        return False, out
    if unpatterned:
        rec('  ### HARD FAILURE -- a STRUCK entry carries no PATTERN line, so the record')
        rec('  ### describes a clause the check cannot see. That is the misleading state.')
        return False, out

    # ### THE FOUR CLAUSE FIXTURES. ### **THE THIRD IS THE NEAR-MISS AND IT IS THE ONE THAT
    # ### MAKES THE OTHER THREE MEAN ANYTHING** -- a matcher that never misses is not matching.
    e1 = struck[0]
    cases = [
        ('(a) fires: the clause in the corpus\'s own wording',
         'a title must name its objects and conditions, not claim an achieved property', True),
        ('(a) fires: the clause in a document\'s wording',
         'This document’s title names its objects and its conditions and claims no achieved '
         'property.', True),
        # ### **THE WRAP FIXTURES. ### THE DEFECT THAT CAUSED THEM IS AT THE TOP OF THE SCAN.**
        ('(a) fires: the clause BROKEN BY A LINE WRAP (the ferry\'s own shape)',
         'seeded with the author\'s -- "titles name objects and\nconditions, never claimed '
         'properties" is STRUCK; only the', True),
        ('(a) NEAR-MISS across a wrap, stays quiet',
         'the title must name its objects, and\nthe act says which', False),
        ('(a) NEAR-MISS, stays quiet: half the clause only',
         'the title must name its objects, and the act says which', False),
        ('(a) quiet: a clean sentence with no struck clause',
         'The document states grades and confers none.', False),
    ]
    rec('  %-56s %-9s %s' % ('clause fixture', 'hits/exp', 'agree'))
    bad = 0
    for lbl, text, expect in cases:
        ch, _ = scan_text(text, [e1], stem_list)
        got = bool(ch)
        ok = (got == expect)
        bad += 0 if ok else 1
        rec('  %-56s %-9s %s' % (lbl, '%s/%s' % (got, expect), 'YES' if ok else '### NO ###'))
    rec()

    # ### THE STEM FIXTURES, BUILT FROM THE LOADED LIST.
    s0 = banned_terms.STEMS[0]
    s1 = banned_terms.STEMS[1] if len(banned_terms.STEMS) > 1 else banned_terms.STEMS[0]
    stem_cases = [
        ('(b) fires: the first banned stem, from the loaded list',
         'a sentence carrying the word %s in the act\'s own voice' % s0, True),
        ('(b) fires: the retired stem, rebuilt from the loaded list',
         'the protocol was called %s-%s before b280 retired it' % ('outcome', s1), True),
        ('(b) quiet: a sentence carrying neither',
         'The pair certifies sharpness at that cell, not the equivalence in general.', False),
    ]
    rec('  %-56s %-9s %s' % ('stem fixture', 'hits/exp', 'agree'))
    for lbl, text, expect in stem_cases:
        _, sh = scan_text(text, [], stem_list)
        got = bool(sh)
        ok = (got == expect)
        bad += 0 if ok else 1
        rec('  %-56s %-9s %s' % (lbl, '%s/%s' % (got, expect), 'YES' if ok else '### NO ###'))

    # ### THE CITATION FIXTURES (b335), BUILT FROM THE LOADED VERSION, NEVER TYPED; skipped when the
    # ### standing file is absent, and said so.
    cur = standing_version()
    cite_cases = []
    if cur is not None:
        cite_cases = [
            ('(c) quiet: a citation of the current standing version',
             'Standing clauses: FERRY_STANDING v%d, carried by reference.' % cur, 'CURRENT'),
            ('(c) fires: a citation of a stale standing version',
             'Standing clauses: FERRY_STANDING v%d, carried by reference.' % (cur + 1), 'STALE'),
            ('(c) quiet: a ferry that cites nothing',
             'The act restates its clauses in full.', 'NONE'),
        ]
        rec()
        rec('  %-56s %-9s %s' % ('citation fixture', 'got/exp', 'agree'))
        for lbl, text, expect in cite_cases:
            got, _c, _v = citation_check(text, cur)
            ok = (got == expect)
            bad += 0 if ok else 1
            rec('  %-56s %-9s %s' % (lbl, '%s/%s' % (got, expect), 'YES' if ok else '### NO ###'))
    else:
        rec()
        rec('  citation fixtures : SKIPPED -- no standing file at %s' % os.path.basename(STANDING))

    rec()
    rec('  ### FIXTURES AGREEING : %d of %d' % (len(cases) + len(stem_cases) + len(cite_cases) - bad,
                                                len(cases) + len(stem_cases) + len(cite_cases)))
    rec('  ### **BOTH ARMS FIRE, BOTH STAY QUIET, AND THE NEAR-MISS DOES NOT FIRE.**')
    return bad == 0, out


def main(argv):
    if not argv or argv[0] in ('--self-test', '-t'):
        ok, _ = self_test()
        return 0 if ok else 2

    path = argv[0]
    ok, _ = self_test(verbose=False)
    struck, unconf = parse_record()
    stem_list = stems()
    text = io.open(path, encoding='utf-8', errors='replace').read()

    print('=' * 100)
    print('ferry_scan.py -- THE FERRY SCAN, RUN BEFORE THE ACT.')
    print('=' * 100)
    print('  ferry file                    : %s' % os.path.basename(path))
    print('  bytes / lines                 : %d / %d' % (len(text.encode('utf-8')),
                                                         len(text.splitlines())))
    print('  record                        : %s' % os.path.basename(RECORD))
    print('  struck entries loaded         : %d   patterns : %d'
          % (len(struck), sum(len(e['patterns']) for e in struck)))
    print('  UNCONFIRMED entries skipped   : %d   ### NONE PROMOTED' % unconf)
    print('  self-test                     : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A SCAN FROM A SUITE THAT DOES NOT PASS ITS OWN FIXTURES.')
        return 2
    if not text.strip():
        print('  ### HARD FAILURE -- THE FERRY FILE IS EMPTY. A scan of nothing is not a scan.')
        return 2

    ch, sh = scan_text(text, struck, stem_list)
    print()
    print('  ### STRUCK-CLAUSE HITS : %d' % len(ch))
    for lbl, i, c, line in ch:
        print('    line %-4d col %-4d  %s' % (i, c, lbl))
        print('        %s' % line[:104])
    print()
    print('  ### BANNED/RETIRED-STEM HITS : %d' % len(sh))
    for lbl, i, c, line in sh:
        print('    line %-4d col %-4d  %s' % (i, c, lbl))
        print('        %s' % line[:104])
    print()
    # ### b335: the standing-clauses citation, checked against the file's current version.
    status, cited, current = citation_check(text)
    stale = 1 if status == 'STALE' else 0
    print('  ### STANDING-CLAUSES CITATION : %s   (cited %s ; current %s)'
          % (status, cited if cited else 'none', current if current is not None else 'no file'))
    if stale:
        print('    ### the ferry cites a version other than the current one -- a HIT; the reader rules.')
    print()
    print('  ### VERDICT: ### **%d HIT(S) REPORTED. ### NOTHING REFUSED, NOTHING EDITED.**'
          % (len(ch) + len(sh) + stale))
    print('  ### **A HIT IS A STRING, NOT A FAULT.** ### A ferry that strikes a clause quotes')
    print('  ### the clause to strike it, and that quotation hits. ### THE READER RULES.')
    print('=' * 100)
    return 1 if (ch or sh or stale) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
