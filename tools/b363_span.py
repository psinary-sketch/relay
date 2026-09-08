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
THIS_ACT = 363

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


def main():
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
    current = THIS_ACT - start + 1
    rec('')
    rec('  ### (2) THE CURRENT SPAN, COUNTED FROM THE LAST FOLD FORWARD.')
    rec('  ' + '-' * 96)
    rec('    the last fold covers      : b%d - b%d (%d acts)' % (last['lo'], last['hi'], last['acts']))
    rec('    it was FILED BY           : b%d   ### read from its own section, not typed' % fold_act)
    rec('    so the next span STARTS AT: b%d' % start)
    rec('    and it now runs through   : b%d (this act)' % THIS_ACT)
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
    p = run_clock.write(D, 'b363_span_notes', LINES)
    io.open(os.path.join(D, 'b363_span.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(folds=F, spans=spans, shortest=spans[0], longest=spans[-1], middle=mid,
             last_fold=last, filed_by=fold_act, span_starts_at=start, this_act=THIS_ACT,
             current_span=current, reached_shortest=bool(reached), threshold_declared=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
