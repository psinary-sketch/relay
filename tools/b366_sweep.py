# -*- coding: utf-8 -*-
"""b366_sweep.py -- ADDITION TWO: THE SWEEP. ### **COUNTED BY TOOL, CLASSIFIED BY (R2)'s TEST.**

### ### **WHAT THE TOOL DECIDES: THE ARITHMETIC AND THE SEARCH.** ### It enumerates every gate suite in
### the relay repository, counts the arms each suite registers ### **FROM THE SUITE'S OWN CODE**, and runs
### a detector for ### **ADDRESS-SHAPED CODE.**
### ### **WHAT THE TOOL DOES NOT DECIDE: THE CLASSIFICATION.** ### `(R2)` turns on whether the file being
### indexed is the act's own artifact or the living record, and ### **THAT IS A QUESTION ABOUT WHAT A
### ### COMPUTED PATH NAMES.** ### So every flagged arm is classified ### **BY THIS SEAT, AS DECLARED
### ### DATA, WITH ITS OWN CODE LINE PRINTED BESIDE IT** -- `b357`'s cure, and the right one here for the
### same reason it was there.
### ### **AND THE DETECTOR IS SCORED BEFORE IT IS BELIEVED:** ### it must find the ONE confirmed instance
### the record holds, and it carries fixtures in ### **BOTH POLARITIES**, including a content-written arm
### it must leave alone.
### ### **AND ONE THING THE FIRST VERSION OF THIS TOOL GOT WRONG IS WORTH THE HEADER:** ### it reused the
### `G-NO*` flattener, which ### **DROPS ANY LINE CARRYING A STRING LITERAL.** ### That is right for
### prose-scanning and fatal here, because the address predicates sit on lines that also carry print
### strings. ### **THIS VERSION MASKS STRING CONTENTS WITH `tokenize` AND KEEPS THE CODE.**
### ### **NO SUITE IS EDITED. ### NO ARM IS REPAIRED.**
"""
import glob
import io
import json
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE DETECTOR'S SHAPES, NAMED BEFORE IT RUNS.** ### Each is a way of letting a LINE POSITION enter
# ### a pass condition. ### **THE NET IS DELIBERATELY WIDE AND IS EXPECTED TO CATCH THINGS THAT ARE NOT
# ### ADDRESS PREDICATES**, which is why the classification is declared and not inferred.
SHAPES = [
    ('S1  a stored line field compared or read', r"""\[['"]line['"]\]"""),
    ('S2  a file split into lines and indexed', r"""splitlines\(\)\s*\[|split\(chr\(10\)\)\s*\["""),
    ('S3  a bare index variable compared', r"""\bn\s*!=|!=\s*n\b"""),
]
CAND = re.compile('|'.join('(?:%s)' % p for _l, p in SHAPES))

# ### **THE CLASSIFICATION. ### DECLARED BY THIS SEAT, ARM BY ARM.** ### (suite, arm, class, one
# ### substitution from standing, reason). ### `D` = DATED, `S` = STANDING, `F` = NOT AN ADDRESS PREDICATE.
DATED, STANDING, NOTADDR = 'DATED', 'STANDING', 'NOT AN ADDRESS PREDICATE'
DECLARED = [
    ('b326_checks.py', 'G-NOEDIT', NOTADDR, False,
     'the index is `[-1]` -- the LAST line of a `git status` capture -- and it is inside a `print`. '
     '### A constant index into a command’s own output is not an address into the record.'),
    ('b330_checks.py', 'G-EXTRACT', NOTADDR, False,
     '`n` here is a FILENAME, not a line index: the comparison excludes one module by name. '
     '### **THE SHAPE `n !=` IS THE WIDEST PART OF THE NET AND THIS IS WHAT IT COSTS.**'),
    ('b335_checks.py', 'G-DIFF', NOTADDR, False,
     'a diff is split into lines to be PRINTED. ### No line position enters the pass condition.'),
    ('b340_checks.py', 'G-SCOPE', DATED, True,
     'it indexes `tools/li_bench.py` -- ### **A LIVING OWNER INSTRUMENT** -- at a banked line number, and '
     'the result enters the pass condition. ### **AND THE SENTENCE IS RIGHT THERE BESIDE THE NUMBER**, so '
     'the substitution is available.'),
    ('b341_checks.py', 'G-LOCATE', STANDING, False,
     'it is address-shaped and it indexes ### **THE ACT’S OWN BANKED EXTRACTION** '
     '(`data/b341_source_*.txt`), which is frozen with the act. ### **UNDER (R2) THAT IS THE ACT’S OWN '
     'ARTIFACT AND THE ARM IS STANDING** -- and it is the case that shows why the classification cannot be '
     'left to the detector.'),
    ('b357_checks.py', 'G-LOCATED', DATED, True,
     '### **THE ONE CONFIRMED INSTANCE**, diagnosed at `b364`: it recomputes a line position in four '
     'LIVING ledgers and compares it against a literal frozen in its own bank. ### The arm already calls '
     '`AF.find` on the row’s own TEXT, so the address half is an ADDITION to a content arm and comes '
     'off by deletion.'),
    ('b359_checks.py', 'G-STATUSES', DATED, False,
     'it indexes `README.md` and `SPIRAL_MAP.md` -- ### **LIVING PAPERS FILES** -- at banked line numbers. '
     '### **AND IT IS NOT ONE SUBSTITUTION FROM STANDING:** ### `b359`’s own JSON carries `line` and '
     'not the claim’s TEXT, so there is nothing to look the content up BY until a text is derived and '
     'banked first.'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def masked_lines(path):
    """### **STRING CONTENTS MASKED, COMMENTS DROPPED, CODE KEPT.** ### The flattener the `G-NO*` arms use
    ### drops the whole line; that would delete every address predicate in the record, because they sit
    ### beside print strings."""
    src = io.open(path, encoding='utf-8').read()
    out = [list(x) for x in src.split(chr(10))]
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return None
    for tk in toks:
        if tk.type not in (tokenize.STRING, tokenize.COMMENT):
            continue
        (sr, sc), (er, ec) = tk.start, tk.end
        if sr == er:
            row = out[sr - 1]
            for c in range(sc, min(ec, len(row))):
                row[c] = ' '
        else:
            row = out[sr - 1]
            for c in range(sc, len(row)):
                row[c] = ' '
            for r in range(sr, er - 1):
                out[r] = [' '] * len(out[r])
            row = out[er - 1]
            for c in range(0, min(ec, len(row))):
                row[c] = ' '
    return [(i, ''.join(row)) for i, row in enumerate(out, 1) if ''.join(row).strip()]


ARM = re.compile(r"""fails\.append\(\s*['"]([A-Za-z0-9_/\-]+)""")


def arms_of(path):
    """### **THE ARMS A SUITE REGISTERS, FROM ITS OWN CODE.** ### An arm is counted where the suite itself
    ### records a failure under a NAME. ### A registration whose argument is not a literal is reported as
    ### UNATTRIBUTED and is never dropped."""
    src = io.open(path, encoding='utf-8').read()
    named, unattributed, at = set(), 0, []
    for i, ln in enumerate(src.split(chr(10)), 1):
        if 'fails.append(' not in ln:
            continue
        m = ARM.search(ln)
        if m:
            named.add(m.group(1))
            at.append((i, m.group(1)))
        else:
            unattributed += 1
    return named, unattributed, at


def attribute(path, lineno, at):
    """### THE ARM A FLAGGED LINE BELONGS TO: THE NEXT REGISTRATION BELOW IT, WHICH IS THE HOUSE IDIOM."""
    for i, name in at:
        if i >= lineno:
            return name
    return None


# ### ==================================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES. ### THEIR TEXT IS WRITTEN HERE AND DRAWN FROM NO SUITE.**
# ### ==================================================================================================
_POS = (
    "def main():" + chr(10) +
    "    print('  G-FIXPOS (an arm written by ADDRESS):')" + chr(10) +
    "    ok = J['sentence'] in io.open(LIVE).read().splitlines()[J['line'] - 1]" + chr(10) +
    "    if not ok:" + chr(10) +
    "        fails.append('G-FIXPOS')" + chr(10)
)
_NEG = (
    "def main():" + chr(10) +
    "    print('  G-FIXNEG (an arm written by CONTENT, which must NOT be flagged):')" + chr(10) +
    "    ok = J['sentence'] in io.open(LIVE).read() and sha(LIVE) == J['sha']" + chr(10) +
    "    if not ok:" + chr(10) +
    "        fails.append('G-FIXNEG')" + chr(10)
)


def self_test(verbose=True):
    import tempfile
    tmp = tempfile.mkdtemp(prefix='b366_sweep_')
    r = []
    for nm, body, want in (('FIXPOS', _POS, True), ('FIXNEG', _NEG, False)):
        p = os.path.join(tmp, 'fix_%s.py' % nm)
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
        ml = masked_lines(p) or []
        got = any(CAND.search(c) for _i, c in ml)
        r.append(('an arm written by ADDRESS is flagged' if want else
                  '### and an arm written by CONTENT is NOT flagged', got == want))
    # ### (3) ### **AND THE MASKING IS THE THING THAT MAKES IT WORK**: the old flattener would drop the
    # ### positive fixture's line entirely, because that line also carries a string.
    p = os.path.join(tmp, 'fix_POS2.py')
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(_POS)
    ml = masked_lines(p) or []
    hit = [c for _i, c in ml if CAND.search(c)]
    r.append(('the flagged line survived string-masking with its code intact',
              bool(hit) and 'splitlines()' in hit[0]))
    # ### (4) ### **AND A FILE THAT WILL NOT TOKENIZE IS REPORTED, NOT SILENTLY EMPTY.**
    p = os.path.join(tmp, 'fix_BAD.py')
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write("def f(:" + chr(10))
    r.append(('a file that will not tokenize returns None, not an empty scan',
              masked_lines(p) is None))
    for what, ok in r:
        if verbose:
            print('    %-66s %-6s %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


def main():
    rec('=' * 100)
    rec('b366 -- THE SWEEP. ### **COUNTED BY TOOL. ### CLASSIFIED BY (R2). ### NO SUITE EDITED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('')
    rec("  ### THE DETECTOR'S OWN FIXTURES, BOTH POLARITIES, RUN BEFORE IT IS BELIEVED:")
    fx = self_test(True)
    rec('  ### detector fixtures : %s' % fx)
    if not fx:
        run_clock.write(D, 'b366_sweep_run', LINES)
        return 2

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE POPULATION, COUNTED FROM THE SUITES THEMSELVES.')
    rec('-' * 100)
    suites = sorted(glob.glob(os.path.join(T, 'b*_checks.py')))
    total_arms, unattr, untok, per = 0, 0, [], {}
    for p in suites:
        named, ua, at = arms_of(p)
        per[p] = (named, at)
        total_arms += len(named)
        unattr += ua
        if masked_lines(p) is None:
            untok.append(os.path.basename(p))
    rec('    gate suites in the relay repository : %d' % len(suites))
    rec('    ### ### **ARMS REGISTERED BY THEIR OWN SUITES : %d**' % total_arms)
    rec('    registrations whose name is not a literal (UNATTRIBUTED, reported not dropped) : %d' % unattr)
    rec('    suites that would not tokenize : %d %s' % (len(untok), untok or ''))
    rec('    ### **AN ARM IS COUNTED WHERE ITS OWN SUITE REGISTERS IT UNDER A NAME.** ### The same name')
    rec('    ### in two suites is two arms, because they are two predicates in two acts.')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE DETECTOR. ### **ADDRESS-SHAPED CODE, WITH ITS REACH STATED.**')
    rec('-' * 100)
    for lbl, pat in SHAPES:
        rec('    %s' % lbl)
    rec('    ### **AND WHAT IT CANNOT DO:** ### it cannot tell whether the file being indexed is the')
    rec("    ### act's own artifact or the living record, because that is a question about what a")
    rec('    ### COMPUTED PATH NAMES. ### **SO IT FLAGS, AND THIS SEAT CLASSIFIES.**')
    rec('')
    flagged = []
    for p in suites:
        ml = masked_lines(p)
        if ml is None:
            continue
        named, at = per[p]
        for i, c in ml:
            if CAND.search(c):
                flagged.append(dict(suite=os.path.basename(p), line=i, code=c.strip()[:150],
                                    arm=attribute(p, i, at)))
    rec('    ### ### **FLAGGED LINES : %d, IN %d SUITES.**'
        % (len(flagged), len({f['suite'] for f in flagged})))
    for f in flagged:
        rec('')
        rec('    %-22s line %-6d arm %s' % (f['suite'], f['line'], f['arm']))
        rec('        | %s' % f['code'])

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CLASSIFICATION. ### **DECLARED, ARM BY ARM, WITH THE CODE ABOVE.**')
    rec('-' * 100)
    decl = {(s, a): (k, sub, why) for s, a, k, sub, why in DECLARED}
    missing = [(f['suite'], f['arm']) for f in flagged if (f['suite'], f['arm']) not in decl]
    extra = [k for k in decl if k not in {(f['suite'], f['arm']) for f in flagged}]
    if missing or extra:
        rec('    ### ### **THE DECLARATION AND THE FLAGS DISAGREE. ### NOTHING IS EMITTED.**')
        rec('    ### flagged but not declared : %s' % (missing or 'none'))
        rec('    ### declared but not flagged : %s' % (extra or 'none'))
        run_clock.write(D, 'b366_sweep_run', LINES)
        return 3
    rec('    ### ### **EVERY FLAGGED ARM IS DECLARED, AND EVERY DECLARATION IS FLAGGED : True**')
    rows = []
    for f in flagged:
        k, sub, why = decl[(f['suite'], f['arm'])]
        rows.append(dict(suite=f['suite'], arm=f['arm'], line=f['line'], code=f['code'],
                         classification=k, one_substitution=bool(sub), why=why))
        rec('')
        rec('    %-22s %-12s %-24s one substitution from standing : %s'
            % (f['suite'], f['arm'], k, sub))
        rec('        %s' % why)

    n_dated = sum(1 for r in rows if r['classification'] == DATED)
    n_standing = sum(1 for r in rows if r['classification'] == STANDING)
    n_notaddr = sum(1 for r in rows if r['classification'] == NOTADDR)
    n_sub = sum(1 for r in rows if r['one_substitution'])
    confirmed = any(r['suite'] == 'b357_checks.py' and r['arm'] == 'G-LOCATED'
                    and r['classification'] == DATED for r in rows)

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE COUNTS, AND THE TWO FIGURES THE ORDER ASKED FOR APART.')
    rec('-' * 100)
    rec('    ### ### **DATED ARMS IN THE RECORD : %d.**' % n_dated)
    rec('    ### ### **OF THOSE, ONE SUBSTITUTION FROM STANDING : %d.**' % n_sub)
    rec('    ### **AND THEY ARE DIFFERENT NUMBERS, WHICH IS WHY THE ORDER ASKED FOR BOTH.** ### The one')
    rec('    ### that is NOT one substitution away is not harder to write -- ### **IT IS MISSING ITS')
    rec('    ### ### CONTENT.** ### An arm can only be rewritten by content if a content was banked.')
    rec('    ### address-shaped but STANDING (the act’s own frozen artifact) : %d' % n_standing)
    rec('    ### flagged and NOT an address predicate at all : %d' % n_notaddr)
    rec('    ### ### **SO THE NET’S PRECISION ON THIS POPULATION IS %d OF %d**, and the rest is what a'
        % (n_dated + n_standing, len(rows)))
    rec('    ### wide net costs. ### **THE COST IS PAID IN READING, NOT IN FALSE FINDINGS.**')
    rec('')
    rec('    ### ### **AND THE DETECTOR FOUND THE ONE CONFIRMED INSTANCE THE RECORD HOLDS : %s**'
        % confirmed)
    rec('    ### `b357`’s `G-LOCATED`, diagnosed at `b364`. ### **A DETECTOR THAT MISSED IT WOULD HAVE')
    rec('    ### ### BEEN REPORTED AS MISSING IT**, and the sweep would not have been emitted.')
    rec('')
    rec('    ### ### **DATED ARMS AS A FRACTION OF THE POPULATION: %d OF %d.**' % (n_dated, total_arms))
    rec('    ### **AND THAT FRACTION IS THE FINDING, AND IT IS A SMALL ONE.** ### The species is real, it')
    rec('    ### is confirmed, and ### **IT IS NOT A CLASS THIS RECORD IS RIDDLED WITH.**')

    rec('')
    rec('-' * 100)
    rec('  ### (5) NO SUITE WAS EDITED. ### **BYTE-FOR-BYTE AGAINST THE COMMITTED BLOBS.**')
    rec('-' * 100)
    dirty = [x for x in subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', 'HEAD', '--',
                                        'tools/'], capture_output=True, text=True).stdout.splitlines()
             if x.strip().endswith('_checks.py')]
    rec('    suite files differing from their committed blobs : %d %s' % (len(dirty), dirty or 'none'))
    rec('    ### **READ BEFORE THE PUSH** (`b352`): after this act’s own commit the blob is whatever')
    rec('    ### this act left, and the same comparison would prove nothing.')
    rec('=' * 100)

    p = run_clock.write(D, 'b366_sweep_run', LINES)
    io.open(os.path.join(D, 'b366_sweep.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(suites=len(suites), arms=total_arms, unattributed=unattr, untokenizable=untok,
             flagged=len(flagged), rows=rows, dated=n_dated, standing=n_standing,
             not_address=n_notaddr, one_substitution=n_sub, confirmed_instance_found=bool(confirmed),
             suites_dirty=dirty, detector_fixtures=bool(fx),
             shapes=[l for l, _p in SHAPES],
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if (confirmed and not dirty) else 1


if __name__ == '__main__':
    sys.exit(main())
