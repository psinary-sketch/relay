# -*- coding: utf-8 -*-
"""b370_lore.py -- COMPONENT 3: THE LORE, WITH ITS MINTS. ### **LOCAL ONLY, NOT PUSHED.**

### ### **THREE MODULES, EACH BESIDE THE ARM SPECIES**, as every module since `b330`.
### ### **AND EACH STATES ITS MECHANIZABLE HALF AND ITS LIMIT APART**, because a rule that does not say
### which half a tool can carry will be trusted for both.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock          # noqa: E402
import gate_needle as GN  # noqa: E402

D = os.path.join(ROOT, 'data')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MODDIR = os.path.join(TC, 'modules', '2026-09')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

M1 = '''# ONE_INCIDENT_IS_NOT_A_PARTITION.md — one incident shows you a class, never its parts

**Minted b370 (2026-09-08), from an incident already in the record.**
**Status: JUDGEMENT RULE. No mechanizable half at all, and this module says so first.**

## The rule

**A single observed failure licenses a CLASS. It does not license a PARTITION of that class.**
When you have met one instance, you know the kind exists. You do not know how many kinds there are,
and the shape you draw around the one you met will be the shape of that one.

## The incident

A ferry drafted a repair as **all-or-nothing**: either the thing was there and could be fixed, or it
was absent and nothing could be done. The act that executed it found the world had a **third** state,
and the draft had no room for it. The correction was a **split** — the class divided into parts the
single incident had not shown, because a single incident cannot show a division.

**The draft was not careless.** It generalised correctly from one case. That is the whole difficulty:
generalising from one case is what one case invites.

## Why there is no mechanizable half

A tool can count the instances a claim rests on. **It cannot tell you whether the class has parts you
have not met**, because the parts you have not met leave no trace to count. Anything that claimed to
would be asserting completeness about a search nobody ran — which is the failure this record calls
`NOT LOCATED` when it is honest and calls a finding when it is not.

## What follows

- **When one incident suggests a shape, write the shape down as a hypothesis with its sample size.**
- **Before acting on it, look for the second case.** If you cannot find one, say the shape rests on one.
- **And when a later act finds a part your shape had no room for, that is the shape being corrected,
  not the earlier act being wrong.** See [[predicate-one-shape]] for the same lesson in a tool.

## The scope of this module

It states a rule and names one incident. **It does not claim any current classification in the record
is under-partitioned**, and it prices no re-partitioning.
'''

M2 = '''# PREDICATE_ONE_SHAPE.md — a predicate that knows one shape finds one shape

**Minted b370 (2026-09-08), from five incidents in nine acts.**
**Status: JUDGEMENT RULE with a NARROW mechanizable half. The halves are listed apart.**

## The rule

**A predicate written against the shape you have seen will report exactly that shape and will report
its absence as absence.** A search for a name preceded by a backtick finds names preceded by
backticks; it does not find the name written as a bare heading, and it reports that name as missing.

## The incidents — five, in one span

- A gate flattener that stripped one marker run and not two.
- A classifier that required a backtick or a slash before an identifier, and so reported a retirement
  ledger as having **no entry at all** for a layer whose entry is headed by that identifier's own name.
- A layer matcher keyed on a layer's **first word**, which put two declarations in the wrong group.
- A count-shape detector that fired on a language version (`Lean 4`) and on a phase number, and — worse
  — reported only its **first** match, so a real count sitting after the noise was invisible.
- An arm that asked for a commit marker in one punctuation form and failed on a comma.

**Five in nine acts is not a run of bad luck. It is the default failure of anyone writing a matcher.**

## The sharp half, and it is the reason this is a judgement rule

**The second incident was caught by RE-DERIVATION, not by any arm.** No gate in the record would have
caught it, and the reason is structural: **the gate would have been written by the same hand, in the
same sitting, with the same predicate.** A guard written from the author's model of the world inherits
that model's holes.

## The mechanizable half — narrow, and stated as narrow

**Mechanizable:** whether a matcher has been exercised against more than one shape. A fixture that
feeds a predicate two spellings of the same thing is a test a tool can demand.

**Not mechanizable:** whether the shapes you thought to test are the shapes that exist. **A predicate
can be widened but never shown complete**, and no amount of fixtures closes that.

## What follows

- **State the shape your predicate assumes, in the predicate's own comment, before you rely on it.**
- **Where a finding is negative — "not present", "no entry", "none found" — re-derive it by a second
  route before banking it.** A negative is exactly where a narrow predicate is invisible.
- **And do not expect the gate to catch this.** It is caught by a second reading, or not at all.
- See [[one-incident-is-not-a-partition]]: both are failures of a shape drawn from what was seen.

## The scope of this module

It states a rule and names five incidents. **It does not claim any current predicate in the record is
narrow**, and it prices no sweep. It also does not claim the five are all of them — which would be the
rule breaking itself.
'''

M3 = '''# DURABILITY_SPLIT.md — a repair to a tracked file travels; a repair to an untracked one does not

**Minted b370 (2026-09-08), from a repair the record made and immediately had to qualify.**
**Status: JUDGEMENT RULE with a REAL mechanizable half. The halves are listed apart.**

## The rule

**A repair to a TRACKED file travels with a clone. A repair to an UNTRACKED one does not.**
Two repairs made in the same act, described in the same sentence, reported as one item discharged, can
have completely different lifetimes — and nothing in the act's own record shows the difference unless
someone writes it down.

## The incident

One act closed two hygiene items together: it added a repository to a **tracked roster**, and it
installed a **pre-push hook** into that repository's `.git/hooks/`. Both were verified; both passed
their arms; both were reported as done.

**`.git/hooks/` is not tracked by git.** The roster mend survives a clone and the hook install does
not. A fresh clone of any repository in this federation starts **with no hook at all** — including the
three that have carried one since it was first installed.

## The sharp half

**The guards that have caught the most are the ones a fresh clone starts without.** The pre-push hook
has refused more bad pushes than any other single check in this record. It is also the check with the
shortest lifetime, and the two facts have never been written on the same page until now.

## The mechanizable half — and this one is real

**Mechanizable:** for any file a guard lives in, whether git tracks it. That is one command per path and
it has no judgement in it. **A tool can produce, for every guard in the record, a DURABLE / NOT DURABLE
column, and it should.**

**Not mechanizable:** whether the record *depends* on a given guard. **No tool can rank guards by how
much they have caught**, because what a guard caught is in the prose of the acts it stopped, not in a
counter. And no tool can decide whether a non-durable guard is worth making durable — that trades
against how it would have to be installed, which is a design question.

## What follows

- **When you report a repair, report its durability beside it.** Two repairs in one sentence are not
  one item.
- **Prefer the tracked fix where both are available**, and where only the untracked one is available,
  say so at the point of the claim rather than in a footnote.
- **A durable fix for an untracked guard exists and is not free:** ship the guard as a tracked file plus
  a bootstrap step that installs it, and make some already-durable check fail when the install is
  missing. **That is a design, not a patch**, and this module prices it as such rather than pretending
  it is a one-line change.

## The scope of this module

It states a rule and names one incident. **It does not claim the record's guards are mostly
non-durable** — nobody has swept for that — and it builds nothing.
'''

MODULES = [('ONE_INCIDENT_IS_NOT_A_PARTITION.md', M1,
            ['licenses a CLASS', 'It does not license a PARTITION',
             'No mechanizable half at all']),  # ### the probe is the module's OWN capitalisation:
            # ### the first version typed it lowercase and the arm demanded a string this act had
            # ### not written -- `b369`'s species, met again inside the act that mints the module
            # ### about predicates that know one shape.
           ('PREDICATE_ONE_SHAPE.md', M2,
            ['caught by RE-DERIVATION, not by any arm',
             'can be widened but never shown complete', 'Mechanizable:']),
           ('DURABILITY_SPLIT.md', M3,
            ['travels with a clone', 'the ones a fresh clone starts without',
             'DURABLE / NOT DURABLE column', 'No tool can rank guards'])]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b370 -- COMPONENT 3: THE LORE. ### **THREE MINTS, LOCAL ONLY.**')
    rec('=' * 100)
    if not os.path.isdir(MODDIR):
        rec('  ### ### **NO MODULE DIRECTORY. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b370_lore_notes', LINES)
        return 2
    sib = sorted(f for f in os.listdir(MODDIR) if f.endswith('.md'))
    rec('')
    rec('  modules already beside them : %d' % len(sib))
    rec('  ### **THE ARM SPECIES ARE THERE : %s**'
        % [f for f in sib if f in ('WRONG_ARM.md', 'DATED_ARM.md', 'DESK_FRESHNESS.md')])
    rec('')
    rec('-' * 100)
    rec('  ### THE MINTS. ### **EACH STATES ITS MECHANIZABLE HALF AND ITS LIMIT APART.**')
    rec('-' * 100)
    written, ok_all = [], True
    for name, text, probes in MODULES:
        p = os.path.join(MODDIR, name)
        existed = os.path.exists(p)
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text)
        back = io.open(p, encoding='utf-8').read()
        nb = GN.norm(back)
        hits = [(pr, GN.norm(pr) in nb) for pr in probes]
        ok = all(v for _pr, v in hits) and back.startswith('# ')
        ok_all = ok_all and ok
        written.append(dict(name=name, bytes=len(back.encode('utf-8')), existed=existed, ok=ok))
        rec('')
        rec('    %-40s %d bytes  (existed before : %s)' % (name, len(back.encode('utf-8')), existed))
        for pr, v in hits:
            rec('        clause present : %-52s %s' % (pr[:52], v))
        rec('        ### **STATES ITS OWN HALVES : %s**' % ok)
    rec('')
    rec('-' * 100)
    rec('  ### THE COMMIT. ### **LOCAL ONLY, AND NOT PUSHED.**')
    rec('-' * 100)
    for name, _t, _p in MODULES:
        subprocess.run(['git', '-C', TC, 'add',
                        ('modules/2026-09/' + name)], capture_output=True, text=True)
    msg = ('Three mints from the b361-b369 fold (b370).' + chr(10) + chr(10)
           + 'ONE_INCIDENT_IS_NOT_A_PARTITION -- a single failure licenses a class, never its'
           + chr(10) + 'parts. No mechanizable half at all, and the module says so first.'
           + chr(10) + chr(10)
           + 'PREDICATE_ONE_SHAPE -- five incidents in nine acts. The sharp one was caught by'
           + chr(10) + 're-derivation and NOT by any arm, because the gate would have been written'
           + chr(10) + 'by the same hand with the same predicate. Mechanizable: whether a matcher'
           + chr(10) + 'was exercised against more than one shape. Not: whether the shapes you'
           + chr(10) + 'thought to test are the shapes that exist.' + chr(10) + chr(10)
           + 'DURABILITY_SPLIT -- a repair to a tracked file travels with a clone; a repair to an'
           + chr(10) + 'untracked one does not. The guards that have caught the most are the ones a'
           + chr(10) + 'fresh clone starts without. Mechanizable: whether a guard is tracked. Not:'
           + chr(10) + 'whether the record depends on it.' + chr(10) + chr(10)
           + 'LOCAL ONLY. NOT PUSHED.' + chr(10))
    subprocess.run(['git', '-C', TC, 'commit', '-q', '-m', msg], capture_output=True, text=True)
    head = subprocess.run(['git', '-C', TC, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    clean = not subprocess.run(['git', '-C', TC, 'status', '--porcelain'],
                               capture_output=True, text=True).stdout.strip()
    ahead = subprocess.run(['git', '-C', TC, 'rev-list', '--count', 'origin/main..HEAD'],
                           capture_output=True, text=True).stdout.strip()
    mods = sorted(f for f in os.listdir(MODDIR) if f.endswith('.md'))
    rec('    local HEAD after the commit : %s ; working tree clean : %s' % (head, clean))
    rec('    ### ### **COMMITS AHEAD OF `origin/main` : %s ### -- NOT PUSHED.**' % (ahead or '?'))
    rec('    ### modules under modules/2026-09 : %d ### -- %s' % (len(mods), mods))
    rec('=' * 100)
    p = run_clock.write(D, 'b370_lore_notes', LINES)
    io.open(os.path.join(D, 'b370_lore.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(minted=len(MODULES), modules=written, all_state_halves=ok_all,
             modules_now=len(mods), module_names=mods,
             techne_head=head, techne_clean=clean, commits_ahead_of_origin=ahead, pushed=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok_all else 1


if __name__ == '__main__':
    sys.exit(main())
