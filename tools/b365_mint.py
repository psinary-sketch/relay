# -*- coding: utf-8 -*-
"""b365_mint.py -- ADDITION TWO: THE MINT AND THE THRESHOLD.

### ### **THE MINT.** ### The wrong-arm species, minted as a ### **JUDGEMENT RULE WITH NO MECHANIZABLE
### HALF**, and the module says so in its own header rather than leaving a reader to expect an arm.
### `b348` minted use-and-mention and `b352` minted the straddling gate, and BOTH had a mechanizable half
### to ship beside the rule. ### **THIS ONE HAS NONE**, and that is the module's content.
### ### **FILED UNDER `modules/2026-09`, COMMITTED LOCALLY, ### NOT PUSHED**, as every module since
### `b330`. ### `TECHNE-Core` is private until the provisionals and this act does not change that.
### ### **THE THRESHOLD.** ### `b363` found no declared fold threshold anywhere in the record. ### This
### act ### **PROPOSES A NUMBER TO THE AUTHOR**, with the observed spans read from `FINDINGS.md`'s own
### headings by `b363_span.py` and not typed, and states that ### **IT IS FIXED BY RULING AND NOT BY THIS
### ### SEAT.**
### ### **EVERY INCIDENT IN THE MODULE IS QUOTED FROM THE BANK OF THE ACT THAT BANKED IT.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODDIR = os.path.join(TC, 'modules', '2026-09')
MODULE = os.path.join(MODDIR, 'WRONG_ARM.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


B360 = d('b360_the_fold.txt')
B362 = d('b362_the_approximation_register.txt')
B363 = d('b363_the_anchored_gate_arms.txt')
B364 = d('b364_the_copy_that_did_not_reproduce.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def quote(path, hint, span=1):
    n, _l = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    q = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=q,
                equal=(GN.norm(q) == GN.norm(raw)))


QUOTES = [
    ('RULE', B360,
     'AN ARM THAT CANNOT PASS ON A CORRECT EDIT IS NOT A STRICTER ARM; IT IS THE WRONG ARM.** ### It was',
     1),
    ('A3', B360, 'FIRST VERSION DEMANDED A COMPONENT ORDER THIS ACT NEVER PROMISED', 1),
    ('A10', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE', 2),
    ('REACH', B363, 'THE WRONG QUESTION**, and this act says that plainly', 1),
    ('B364', B364, 'TWO OF THEM WERE THE WRONG ARM -- IN THE ACT THAT NAMED THE OTHER SPECIES', 1),
]


def module_text(Q, S):
    spans = ', '.join(str(x) for x in S['spans'])
    return '''# WRONG_ARM.md — an arm whose predicate tests something other than its label

**Minted b365 (2026-09-07), from incidents already in the record.**
**Status: JUDGEMENT RULE. NO MECHANIZABLE HALF. The absence of one is the module's content.**

## The rule

**An arm whose predicate tests something other than what its label says is a WRONG ARM. It is not a
stricter arm and it is not a weaker one: it is an arm for a different question, and it will pass or
fail for reasons that have nothing to do with the thing its label names.**

The record's own test for it, banked before the species was named — `%s`, line %d:

> %s

## Why there is no mechanizable half, and why that is the point

The three species this record had already named — needle-wrapping, use-and-mention, and the numbered
repeat — are all failures of **how a sentence is written down**. A needle built from the file cures
every one of them, and b363 built the tool that does it.

**A wrong arm is a failure of which question is asked, and no amount of correctness about bytes
reaches it.** b363 measured this rather than asserting it: over eleven arms in three acts, its helper
would have retired seven, and **the two it could not reach were precisely the two whose predicates
asked the wrong question**. In that act's own words — `%s`, line %d:

> %s

**An arm whose predicate tests something other than its label is invisible to every needle tool by
construction, because the needle checks the SENTENCE and the defect is in the CODE. Its only cure is
a second reader.**

That is why this module ships nothing. `USE_AND_MENTION.md` shipped a judgement rule with a
mechanized companion; `STRADDLING_GATE.md` shipped a rule whose repository half is checked by
`registration_gate.py`. **This one has no companion, and a reader who expects one will trust an arm
that does not exist.**

## The incidents

**`A3` — a component order that was never promised** (`%s`, line %d):

> %s

The arm's label named the act's ritual; its predicate tested the seat's habits. It fired on correct
work and would have fired on any correct work that ordered its components differently.

**`A10` — a true-prefix test on a spliced row** (`%s`, line %d):

> %s

The ledger's writer splices a new row into a table that sits above the cascade section. The arm
tested append-onlyness. **Append-onlyness was never the invariant**, so the arm could not have passed
on a correct write.

**And two more, live, in the act that named the species** (`%s`, line %d):

> %s

`G-PREDICATE` asked a bank for a `print(...)` statement when the bank quotes an arm's label;
`G-UNCHANGED` demanded that a file be byte-identical to its blob *now*, when the claim its own
registration made was that the *diagnosis* had not written it. **Both fired on their own act's correct
work. Neither was caught by a tool: they were caught by being run**, which is not the same thing and
is not as good — **an arm that is wrong AND quiet survives.**

## What follows

- **When you write an arm, state its label as a sentence and then ask whether the predicate decides
  that sentence.** If the predicate would fail on some correct version of the work, it is the wrong
  arm.
- **A failing arm is evidence about the arm, not only about the work.** Before repairing the work,
  read the predicate.
- **Do not soften a needle to make an arm pass** (b348). A wrong arm is not cured by widening it; it
  is cured by replacing the question.
- **And do not expect a tool.** There is none here, and there is unlikely to be one: deciding whether
  a predicate matches a label is reading, and reading is what a second seat is for.

## The scope of this module

It states a rule and names four incidents. **It does not claim the record is free of wrong arms** —
b363's census covered eleven arms in three acts and found two, and b364 found two more in one suite
the next day. **It does not propose an audit**, and it prices none. **And it ships no arm.**

## Appendix — the observed fold spans, for the threshold note filed beside this module

The record has run folds of %s acts (b365, counted by `relay/tools/b363_span.py` from `FINDINGS.md`'s
own headings). **No threshold is declared anywhere in the record.** That is a separate filing and is
the author's to rule.
''' % (
        Q['RULE']['file'], Q['RULE']['line'], Q['RULE']['quote'],
        Q['REACH']['file'], Q['REACH']['line'], Q['REACH']['quote'],
        Q['A3']['file'], Q['A3']['line'], Q['A3']['quote'],
        Q['A10']['file'], Q['A10']['line'], Q['A10']['quote'],
        Q['B364']['file'], Q['B364']['line'], Q['B364']['quote'],
        spans,
    )


def main():
    rec('=' * 100)
    rec('b365 -- ADDITION TWO: THE MINT AND THE THRESHOLD.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE INCIDENTS, QUOTED FROM THE BANKS THAT BANKED THEM.')
    rec('-' * 100)
    Q = {}
    for tag, path, hint, span in QUOTES:
        try:
            Q[tag] = quote(path, hint, span)
        except AF.AnchorError as e:
            rec('  ### ### **NO ANCHOR : %s** -- %s' % (tag, str(e).replace(chr(10), ' | ')[:130]))
            run_clock.write(D, 'b365_mint_notes', LINES)
            return 2
        rec('    [%-5s] %s:%d ### scaffolding removed, equal under the shared normaliser : %s'
            % (tag, Q[tag]['file'], Q[tag]['line'], Q[tag]['equal']))
        rec('        | %s' % Q[tag]['quote'][:160])
    if not all(x['equal'] for x in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b365_mint_notes', LINES)
        return 3

    S = json.load(io.open(d('b363_span.json'), encoding='utf-8'))

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE MODULE. ### **LOCAL-ONLY. ### IT SHIPS NO ARM.**')
    rec('-' * 100)
    if not os.path.isdir(MODDIR):
        rec('  ### ### **NO MODULE DIRECTORY AT %s. ### NOTHING IS WRITTEN.**' % MODDIR)
        run_clock.write(D, 'b365_mint_notes', LINES)
        return 2
    existed = os.path.exists(MODULE)
    body = module_text(Q, S)
    io.open(MODULE, 'w', encoding='utf-8', newline=chr(10)).write(body + chr(10))
    back = io.open(MODULE, encoding='utf-8').read()
    ok_mod = (back.startswith('# WRONG_ARM.md')
              and 'NO MECHANIZABLE HALF' in back
              and 'ITS ONLY CURE IS' in back.upper()
              and 'AND IT SHIPS NO ARM' in back.upper()
              and all(x['quote'][:40] in back for x in Q.values()))
    rec('    written : %s   (existed before : %s)' % (os.path.relpath(MODULE, TC), existed))
    rec('    bytes : %d ; every incident quotation present : %s'
        % (len(back.encode('utf-8')), all(x['quote'][:40] in back for x in Q.values())))
    rec('    ### **THE HEADER SAYS `NO MECHANIZABLE HALF` AND THE MODULE SAYS IT SHIPS NO ARM : %s**'
        % ok_mod)
    modules_now = sorted(f for f in os.listdir(MODDIR) if f.endswith('.md'))
    rec('    ### modules under %s : %d' % (os.path.relpath(MODDIR, TC), len(modules_now)))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE COMMIT. ### **LOCAL ONLY. ### NOT PUSHED, AS EVERY MODULE SINCE b330.**')
    rec('-' * 100)
    subprocess.run(['git', '-C', TC, 'add', os.path.relpath(MODULE, TC).replace(os.sep, '/')],
                   capture_output=True, text=True)
    msg = ('WRONG_ARM.md -- an arm whose predicate tests something other than its label (b365).' + chr(10)
           + chr(10) + 'A JUDGEMENT RULE WITH NO MECHANIZABLE HALF, and the absence of one is the '
           "module's content." + chr(10)
           + 'Four incidents: A3 and A10 from b363 census, and two live ones from b364 own suite.'
           + chr(10) + 'LOCAL ONLY. NOT PUSHED.' + chr(10))
    cm = subprocess.run(['git', '-C', TC, 'commit', '-q', '-m', msg], capture_output=True, text=True)
    head = subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    st = subprocess.run(['git', '-C', TC, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout.strip()
    ahead = subprocess.run(['git', '-C', TC, 'rev-list', '--count', 'origin/main..HEAD'],
                           capture_output=True, text=True).stdout.strip()
    rec('    local HEAD after the commit : %s' % head)
    rec('    working tree clean : %s' % (not st))
    rec('    ### ### **COMMITS AHEAD OF `origin/main` : %s** ### -- and that is the point: TECHNE-Core is'
        % (ahead or '?'))
    rec('    ### private until the provisionals, and this act does not change that.')
    rec('    ### **NOTHING WAS PUSHED BY THIS TOOL. ### IT RUNS NO `git push`.**')

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE THRESHOLD, PROPOSED TO THE AUTHOR. ### **NOT RULED BY THIS SEAT.**')
    rec('-' * 100)
    rec('    ### the observed spans, counted by `tools/b363_span.py` from `FINDINGS.md` own headings:')
    for f in S['folds']:
        rec('        b%-4d - b%-4d  %2d acts   %s' % (f['lo'], f['hi'], f['acts'], f['title'][:56]))
    rec('    ### ### **FOLDS RUN : %d. ### SHORTEST : %d. ### LONGEST : %d. ### MIDDLE : %d.**'
        % (len(S['folds']), S['shortest'], S['longest'], S['middle']))
    proposal = S['middle']
    rec('')
    rec('    ### ### ### **THE NUMBER PROPOSED TO THE AUTHOR: %d ACTS.**' % proposal)
    rec('    ### **AND THE REASON, WHICH IS THE ONLY PART OF THIS THIS SEAT CAN SUPPLY:** ### it is the')
    rec('    ### MIDDLE of the spans the record has actually run, so it is the number that would have')
    rec('    ### changed the fewest past decisions. ### **IT IS NOT DERIVED FROM ANYTHING ABOUT THE WORK**')
    rec('    ### -- not from how much a span contains, not from what a fold costs, not from what a reader')
    rec('    ### can hold. ### **IT IS A DESCRIPTION OF A HABIT, OFFERED AS A NUMBER BECAUSE THE ORDER')
    rec('    ### ### ASKED FOR ONE.**')
    rec('    ### **AND THE SPREAD IS THE ARGUMENT AGAINST TAKING IT TOO SERIOUSLY: %d TO %d.** ### A habit'
        % (S['shortest'], S['longest']))
    rec('    ### that varies by a factor of %.1f is not a rule that was being followed.'
        % (S['longest'] / float(S['shortest'])))
    rec('    ### ### ### **IT IS FIXED BY RULING AND NOT BY THIS SEAT.**')
    rec('    ### ### **AND UNTIL IT IS RULED, `THE FOLD IS DUE` IS A JUDGEMENT AND THE RECORD SAYS SO.**')
    rec('    ### Every act that folded chose to; none was owed. ### An act that writes *the fold is due*')
    rec('    ### before a ruling exists is reporting its own inclination in the grammar of an obligation.')
    rec('=' * 100)

    p = run_clock.write(D, 'b365_mint_notes', LINES)
    io.open(d('b365_mint.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(module=os.path.relpath(MODULE, TC).replace(os.sep, '/'), module_bytes=len(back.encode('utf-8')),
             module_ok=bool(ok_mod), modules_now=len(modules_now), existed_before=existed,
             quotes={k: dict(file=v['file'], line=v['line'], equal=v['equal'], quote=v['quote'])
                     for k, v in Q.items()},
             techne_head=head, techne_clean=(not st), commits_ahead_of_origin=ahead, pushed=False,
             threshold_proposed=proposal, threshold_ruled=False,
             spans=S['spans'], shortest=S['shortest'], longest=S['longest'], middle=S['middle'],
             folds_run=len(S['folds']),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok_mod else 1


if __name__ == '__main__':
    sys.exit(main())
