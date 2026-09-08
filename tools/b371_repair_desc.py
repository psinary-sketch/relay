# -*- coding: utf-8 -*-
"""b371_repair_desc.py -- COMPONENT 1's REPAIR. ### **THE STALE BRANCH, EXECUTED.**

### ### **THE ORDER'S OWN CLAUSE: `if stale, repair the description`.** ### The verdict is read from the
### settler's JSON and is never re-decided here; if the verdict is not `STALE` this tool writes nothing.
### ### **THE ORIGINAL IS PRESERVED BEFORE THE EDIT** -- `(R4)`'s discipline, applied to a surface that
### has no file to preserve it in: the old text is banked in this act's own record, verbatim, because
### ### **A DESCRIPTION HAS NO HISTORY AND NOTHING ELSE WILL REMEMBER IT.**
### ### ### **AND THE REPAIR IS CHOSEN TO NOT GO STALE AGAIN.** ### Replacing one number with another
### buys one act's correctness and re-arms the same trap. ### The count is removed and the ARTIFACT that
### carries it is named, so the description states a property the repository asserts everywhere else and
### points at the file that holds the number.
### ### **THAT IS A JUDGEMENT AND IT IS THIS SEAT'S, SO IT IS FLAGGED AS ONE** -- the author may prefer a
### dated number, and the alternative wording is banked beside the one written.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OWNER, REPO = 'psinary-sketch', 'SIDE-global-section'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NEW = ("The global section: the construction era's verified Lean material — every Core terminal prints "
       "\"does not depend on any axioms\"; the count and the full profile live in AXIOM_PRINTS.txt, not "
       "in this description. Mathlib interfaces declared; correspondence spine. RH reduced to a single "
       "located clause, reduction machine-verified — never wider.")

ALTERNATIVE = ("The global section: the construction era's verified Lean material — Core: 590 zero-axiom "
               "prints at 2026-09-08 (114 at tag v0.1.0); Mathlib interfaces declared; correspondence "
               "spine. RH reduced to a single located clause, reduction machine-verified — never wider.")

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=90)
    return r.returncode, (r.stdout or ''), (r.stderr or '')


def main():
    rec('=' * 100)
    rec("b371 -- COMPONENT 1's REPAIR. ### **THE STALE BRANCH.**")
    rec('=' * 100)
    S = json.load(io.open(os.path.join(D, 'b371_settle.json'), encoding='utf-8'))
    rec('')
    rec('  ### the verdict, read from the settler and never re-decided here : %s' % S['verdict'])
    if S['verdict'] != 'STALE':
        rec('  ### ### **NOT THE STALE BRANCH. ### NOTHING IS WRITTEN, AND THE WORDING IS ROUTED.**')
        run_clock.write(D, 'b371_repair_desc_notes', LINES)
        return 0

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE ORIGINAL, PRESERVED BEFORE THE EDIT.')
    rec('-' * 100)
    rc, out, err = gh('repo', 'view', '%s/%s' % (OWNER, REPO), '--json', 'description')
    if rc != 0:
        rec('  ### ### **COULD NOT RE-READ THE DESCRIPTION. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b371_repair_desc_notes', LINES)
        return 2
    before = json.loads(out)['description'] or ''
    rec('    | %s' % before)
    rec('    bytes : %d' % len(before))
    same = (before == S['description_before'])
    rec('    ### ### **AND IT IS BYTE-IDENTICAL TO WHAT THE SETTLER READ : %s.**' % same)
    rec('    ### **IF IT HAD MOVED BETWEEN THE SETTLING AND THE REPAIR, THE VERDICT WOULD BE ABOUT A')
    rec('    ### ### TEXT THAT NO LONGER EXISTS**, and this arm is why the act would know.')
    already = (before == NEW)
    if already:
        rec('    ### ### **THE ACCOUNT ALREADY CARRIES THE REPLACEMENT.** ### This tool is idempotent:')
        rec('    ### it re-verifies its arms and edits nothing. ### **A RE-RUN IS NOT A SECOND REPAIR.**')
    elif not same:
        rec('    ### ### **IT MOVED, AND NOT TO THIS ACT`S TEXT. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b371_repair_desc_notes', LINES)
        return 3
    rec('    ### ### **A DESCRIPTION HAS NO HISTORY. ### THIS RECORD IS THE ONLY PLACE THE OLD TEXT')
    rec('    ### ### WILL SURVIVE**, so it is banked verbatim above and in this act`s bank.')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE REPLACEMENT, AND WHY IT IS SHAPED THIS WAY.')
    rec('-' * 100)
    rec('    | %s' % NEW)
    rec('    bytes : %d' % len(NEW))
    rec('    ### ### **THE COUNT IS REMOVED RATHER THAN UPDATED.** ### Replacing `%s` with `%s` would be'
        % (S['figure'], S['prints_at_head']))
    rec('    ### correct today and stale on the next commit that adds a terminal -- ### **AND THE')
    rec('    ### ### REPOSITORY IS `%s` COMMITS PAST THE LAST TIME SOMEBODY UPDATED IT.**'
        % S['head_ahead_of_tag'])
    rec('    ### **WHAT REPLACES IT IS A PROPERTY, NOT A COUNT:** ### the repository`s own `README` and')
    rec('    ### its profile both assert that EVERY terminal prints zero axioms, and the profile shows')
    rec('    ### `%d` of `%d` lines saying exactly that with `%d` otherwise.'
        % (S['prints_at_head'], S['prints_at_head_all'], S['prints_at_head_all'] - S['prints_at_head']))
    rec('    ### ### ### **AND THIS IS A JUDGEMENT BY THIS SEAT, FLAGGED AS ONE.** ### The order said')
    rec('    ### REPAIR and did not say how. ### **THE AUTHOR MAY PREFER A DATED NUMBER**, and that')
    rec('    ### wording is banked here so the choice is one edit away:')
    rec('    ###     | %s' % ALTERNATIVE)

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE EDIT, AND THE READ-BACK.')
    rec('-' * 100)
    rc, out, err = (0, '', '') if already else gh('repo', 'edit', '%s/%s' % (OWNER, REPO),
                                                  '--description', NEW)
    if already:
        rec('    ### **NO EDIT ISSUED -- THE ACCOUNT ALREADY CARRIES IT.**')
    if rc != 0:
        rec('  ### ### **THE EDIT FAILED : %s. ### THE DESCRIPTION IS UNCHANGED.**' % err.strip()[:120])
        run_clock.write(D, 'b371_repair_desc_notes', LINES)
        return 2
    rc2, out2, _e = gh('repo', 'view', '%s/%s' % (OWNER, REPO), '--json', 'description')
    after = json.loads(out2)['description'] or '' if rc2 == 0 else ''
    rec('    read back from the account:')
    rec('    | %s' % after)
    ok_set = (after == NEW)
    ok_gone = ('114' not in after)
    ok_artifact = ('AXIOM_PRINTS.txt' in after)
    ok_register = ('never wider' in after)
    rec('    ### ### **THE ACCOUNT NOW CARRIES THE REPLACEMENT, BYTE-FOR-BYTE : %s**' % ok_set)
    rec('    ### ### **THE STALE FIGURE IS GONE : %s** ; the artifact is named : %s' % (ok_gone,
                                                                                        ok_artifact))
    # ### **THE PLACEHOLDER-SPLIT SPECIES, A FIFTH TIME** (`b365`, `b368`, `b369`, `b370`, here): the
    # ### format string ended one line and its argument was attached to the NEXT call, so the first line
    # ### printed a literal `%s` and the value never reached the record. ### **CAUGHT BY READING THE
    # ### ### ACT'S OWN OUTPUT, WHICH IS THE ONLY THING THAT EVER CATCHES IT.**
    rec('    ### ### **AND THE REGISTER SENTENCE SURVIVED THE EDIT : %s** -- ### the one clause in that'
        % ok_register)
    rec('    ### description this seat must not touch, and the arm that proves it did not.')
    rec('')
    rec('    ### ### **AND THE DURABILITY IS STATED WITH THE REPAIR, NOT AFTER IT** (`DURABILITY_SPLIT`):')
    rec('    ### a description is ### **ACCOUNT METADATA, NOT A TRACKED FILE.** ### This correction')
    rec('    ### survives a clone and survives nothing else, ### **AND THERE IS NO TRACKED ARTIFACT THAT')
    rec('    ### ### WOULD FAIL IF IT DRIFTED AGAIN.** ### The repair is real and its guard is absent.')
    rec('=' * 100)
    ok = ok_set and ok_gone and ok_artifact and ok_register
    rec('  ### ### **COMPONENT 1 REPAIR : %s**' % ('DONE' if ok else 'FAILED'))
    rec('=' * 100)
    p = run_clock.write(D, 'b371_repair_desc_notes', LINES)
    io.open(os.path.join(D, 'b371_repair_desc.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(verdict=S['verdict'], before=before, after=after, written=NEW,
                        alternative_banked=ALTERNATIVE, unchanged_since_settling=same,
                        set_byte_for_byte=ok_set, stale_figure_gone=ok_gone,
                        artifact_named=ok_artifact, register_sentence_survived=ok_register,
                        tracked=False, guarded_by_any_tracked_artifact=False,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
