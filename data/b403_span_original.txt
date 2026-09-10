# -*- coding: utf-8 -*-
"""b363_span.py -- THE FOLD'S OWN THRESHOLD, COUNTED FROM THE RECORD AND NOT TYPED.

### ### **THE ORDER'S WORDS:** ### the next act *"should propose the fold of b360 onward when the span
### reaches the fold's own threshold, counted and not typed."*
### ### **THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD**, and this tool says so rather than
### inventing one. ### What the record has instead is ### **EVERY FOLD IT HAS ACTUALLY RUN**, each with its
### own span printed in its own heading in `FINDINGS.md`. ### So the threshold is read off the folds
### themselves -- their shortest, their longest and their middle -- and the CURRENT span is counted from
### the last fold's own heading forward.
### ### **THIS TOOL DECIDES NOTHING.** ### It prints two numbers so that a later act can compare them
### instead of typing a judgement, and the comparison is that act's to make.

### ### ### **AND AS OF b370 IT WRITES NOTHING EITHER, UNLESS ASKED.**
### ### **THE DEFECT, AND IT WAS THIS FILE'S:** ### the first version wrote a run file and a JSON under
### ### **`b363`'s OWN STEM** ### on every run, whoever ran it. ### `b368` ran it to COUNT and rewrote
### `b363`'s run pointer; `b369` did the same one act later. ### **BOTH REVERTED IT; NEITHER FIXED IT.**
### ### **A TOOL RUN TO READ THAT WRITES IS A TOOL THAT WILL BE READ AGAIN**, and a lesson filed in a
### bank and not built into a tool is a lesson that will be learned again.
### ### **THE CONTRACT NOW:**
###   `python tools/b363_span.py`                -- ### **READS. ### WRITES NOTHING. ### RETURNS 0.**
###   `python tools/b363_span.py --act 370`      -- reads, counting the span through b370.
###   `python tools/b363_span.py --emit b370`    -- ### **WRITES UNDER THE CALLER'S OWN STEM**, never
###                                                 under this file's, and implies `--act 370`.
###   `python tools/b363_span.py --self-test`    -- the fixture, both polarities.
### ### **AND THE ACT NUMBER IS NO LONGER A CONSTANT BAKED INTO THIS FILE.** ### With no `--act` it is
### read from the record: the highest act that has banked a file in `data/`. ### **THE RECORD ANSWERS
### ### THE QUESTION THE CONSTANT USED TO ANSWER.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402

D = os.path.join(ROOT, 'data')
FINDINGS = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'FINDINGS.md')
# ### **NO HARDCODED ACT NUMBER.** ### `b363`'s was 363, and every later caller inherited it silently.
DEFAULT_ACT = None

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def folds():
    """### EVERY FOLD HEADING IN `FINDINGS.md`, WITH THE SPAN IT NAMES IN ITS OWN TITLE."""
    txt = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    out = []
    for m in re.finditer(r'^## (.*?), b(\d+)–b(\d+) — THE FOLD\s*$', txt, re.M):
        lo, hi = int(m.group(2)), int(m.group(3))
        out.append(dict(title=m.group(1), lo=lo, hi=hi, acts=hi - lo + 1))
    return out


def filed_by(hi):
    """### THE ACT THAT FILED THE LAST FOLD, READ FROM ITS OWN `Filed by bNNN` SENTENCE."""
    txt = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    heads = [m.start() for m in re.finditer(r'^## .*— THE FOLD\s*$', txt, re.M)]
    tail = txt[heads[-1]:]
    m = re.search(r'Filed by b(\d+)', tail)
    if not m:
        raise LookupError('the last fold section carries no "Filed by bNNN"')
    return int(m.group(1))


def latest_banked_act():
    """### THE HIGHEST ACT THAT HAS BANKED A FILE IN `data/`. ### **READ, NOT TYPED.**"""
    hi = 0
    for f in os.listdir(D):
        m = re.match(r'^b(\d{3})_', f)
        if m:
            hi = max(hi, int(m.group(1)))
    return hi


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    emit, act = None, None
    if '--emit' in argv:
        emit = argv[argv.index('--emit') + 1]
        act = int(re.sub(r'\D', '', emit))
    if '--act' in argv:
        act = int(argv[argv.index('--act') + 1])
    if act is None:
        act = latest_banked_act()
    del LINES[:]
    rec('=' * 100)
    rec("b363 -- THE FOLD'S OWN THRESHOLD, COUNTED. ### **NOTHING HERE IS TYPED AND NOTHING IS DECIDED.**")
    rec('=' * 100)
    F = folds()
    if not F:
        rec('  ### ### **NO FOLD HEADING PARSED. ### NOTHING IS REPORTED FROM MEMORY.**')
        return 2
    rec('')
    rec('  ### (1) EVERY FOLD THE RECORD HAS ACTUALLY RUN, WITH ITS OWN SPAN.')
    rec('  ' + '-' * 96)
    for f in F:
        rec('    b%-4d - b%-4d  %2d acts   %s' % (f['lo'], f['hi'], f['acts'], f['title'][:62]))
    spans = sorted(f['acts'] for f in F)
    mid = spans[len(spans) // 2] if len(spans) % 2 else (spans[len(spans) // 2 - 1] + spans[len(spans) // 2]) // 2
    rec('')
    rec('  ### ### **FOLDS RUN : %d. ### SHORTEST : %d ACTS. ### LONGEST : %d ACTS. ### MIDDLE : %d.**'
        % (len(F), spans[0], spans[-1], mid))
    rec('  ### **AND THERE IS NO DECLARED THRESHOLD IN THE RECORD** -- these are the folds that happened,')
    rec('  ### not a rule anyone wrote down. ### **THE RECORD HAS A HABIT AND NOT A LAW**, and this tool')
    rec('  ### prints the habit rather than promoting it.')

    last = F[-1]
    fold_act = filed_by(last['hi'])
    start = fold_act + 1
    current = act - start + 1
    rec('')
    rec('  ### (2) THE CURRENT SPAN, COUNTED FROM THE LAST FOLD FORWARD.')
    rec('  ' + '-' * 96)
    rec('    the last fold covers      : b%d - b%d (%d acts)' % (last['lo'], last['hi'], last['acts']))
    rec('    it was FILED BY           : b%d   ### read from its own section, not typed' % fold_act)
    rec('    so the next span STARTS AT: b%d' % start)
    rec('    and it now runs through   : b%d   ### read from the record, not typed' % act)
    rec('    ### ### **THE CURRENT SPAN : %d ACT(S).**' % current)
    rec('')
    rec('  ### (3) THE COMPARISON, STATED AND NOT RESOLVED.')
    rec('  ' + '-' * 96)
    rec('    ### **%d AGAINST A SHORTEST OF %d AND A MIDDLE OF %d.**' % (current, spans[0], mid))
    reached = current >= spans[0]
    rec('    ### the current span has reached the shortest fold the record has run : %s' % reached)
    rec('    ### ### **AND THAT IS NOT A DECISION.** ### Whether a span is ready to fold is a judgement')
    rec('    ### about what the acts in it say, and no count settles it. ### **THIS TOOL SUPPLIES THE')
    rec('    ### ### NUMBER SO THAT THE NEXT ACT DOES NOT HAVE TO TYPE ONE.**')
    rec('=' * 100)

    # ### ### **THE WRITE HAPPENS ONLY IF A CALLER ASKED FOR IT, AND ONLY UNDER THAT CALLER'S STEM.**
    if not emit:
        print('  ### ### **READ ONLY. ### NOTHING WAS WRITTEN.** ### Pass `--emit bNNN` to bank this run')
        print('  ### under your own act`s stem. ### **NO CALLER WRITES UNDER ANOTHER ACT`S STEM.**')
        return 0
    p = run_clock.write(D, '%s_span_notes' % emit, LINES)
    io.open(os.path.join(D, '%s_span.json' % emit), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(
                dict(folds=F, spans=spans, shortest=spans[0], longest=spans[-1], middle=mid,
                     last_fold=last, filed_by=fold_act, span_starts_at=start, this_act=act,
                     current_span=current, reached_shortest=bool(reached), threshold_declared=False,
                     emitted_for=emit,
                     run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s and %s_span.json' % (os.path.basename(p), emit))
    return 0


def self_test(verbose=True):
    """### THE FIXTURE THE ORDER DEMANDS. ### **BOTH POLARITIES.**

    ### ### **(a) A DEFAULT RUN LEAVES A FOREIGN ACT'S POINTER BYTE-IDENTICAL.** ### The file is hashed,
    ### the tool is run, the hash is compared. ### **NOT A PROMISE IN A DOCSTRING -- A COMPARISON.**
    ### ### **(b) AND `--emit` STILL WRITES**, under the CALLER'S stem and not this file's. ### Without
    ### (b) the arm would pass on a tool that had simply stopped working, which is the failure `b363`
    ### itself named: ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.**"""
    import hashlib
    import tempfile
    foreign = os.path.join(D, 'b363_span.json')
    before = open(foreign, 'rb').read() if os.path.exists(foreign) else None
    h0 = hashlib.sha256(before).hexdigest() if before is not None else None
    main([])
    after = open(foreign, 'rb').read() if os.path.exists(foreign) else None
    h1 = hashlib.sha256(after).hexdigest() if after is not None else None
    a = (h0 == h1)
    stem = 'zz_span_fixture'
    for f in list(os.listdir(D)):
        if f.startswith(stem):
            os.remove(os.path.join(D, f))
    main(['--emit', stem + '370'])
    made = sorted(f for f in os.listdir(D) if f.startswith(stem))
    b = len(made) >= 2
    for f in made:
        os.remove(os.path.join(D, f))
    untouched = open(foreign, 'rb').read() if os.path.exists(foreign) else None
    c = (before == untouched)
    if verbose:
        print('  b363_span self-test:')
        print('    (a) a DEFAULT run leaves the foreign pointer BYTE-IDENTICAL : %s  (%s)'
              % (a, (h0 or 'absent')[:16]))
        print('    (b) an --emit run DOES write, under the CALLER`s stem       : %s  %s' % (b, made))
        print('    (c) and the emit run still left the foreign pointer alone   : %s' % c)
        print('    ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM: (b) IS WHY (a) MEANS SOMETHING.**')
    return bool(a and b and c)


if __name__ == '__main__':
    if '--self-test' in sys.argv[1:]:
        sys.exit(0 if self_test(True) else 1)
    sys.exit(main())
