# -*- coding: utf-8 -*-
"""b498_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def word(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def main():
    R = json.loads(read(os.path.join(D, 'b498_results.json')))
    c1, c2, c3 = R.get('c1') or {}, R.get('c2') or {}, R.get('c3') or {}

    rec('=' * 104)
    rec('b498 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**')
    rec('=' * 104)
    rec('')
    rec('### THE NAVIGATOR`S THREE.')
    rec('-' * 104)

    f = c2.get('fetched')
    n1 = None if f is None else (f > 4000)
    rec('  **(N1)** ### **%s.**' % word(n1))
    rec('    *"the cache fetches more than 4,000 files"*')
    rec('    ### ### **FILES FETCHED : %s** ; from the tool`s line : %s'
        % (f if f is not None else 'NOT FOUND', c2.get('fetched_line')))
    rec('    `lake exe cache get` exit %s, wall %.1f s' % (c2.get('cache_exit'), c2.get('cache_wall') or 0))
    rec('    ### ### **AND THE FACE SAID WHAT THIS COUNT IS:** ### a count of what was MISSING from a')
    rec('    ### cache directory that already held 121141 files before the act began, ### **NOT A')
    rec('    ### COUNT OF WHAT THE BUILD NEEDS.**')
    rec('')

    if c2.get('closure_run'):
        b = c2.get('built_mathlib')
        n2 = b < 40
        rec('  **(N2)** ### **%s.**' % word(n2))
        rec('    *"after the cache, fewer than 40 Mathlib modules compile"*')
        rec('    ### ### **LINES READING `Built Mathlib.` : %d** ; replayed %d ; closure exit %d ; wall %.1f s'
            % (b, c2.get('replayed_mathlib'), c2.get('closure_exit'), c2.get('closure_wall')))
        rec('    over ### **%d** external `Mathlib.*` roots of the vendored library, computed from its'
            % len(c2.get('closure_roots') or []))
        rec('    import lines. ### **REPLAYED IS NOT COMPILED**, and only `Built` is counted.')
    else:
        n2 = None
        rec('  **(N2)** ### **NOT SCORABLE.**')
        rec('    *"after the cache, fewer than 40 Mathlib modules compile"*')
        rec('    ### the cache was unavailable, so (R109)(2)`s fallback ran and no closure build ran in')
        rec('    ### the foreground; the count the expectation names was never produced here.')
    rec('')

    n3 = c3.get('new_group')
    rec('  **(N3)** ### **%s.**' % word(n3))
    rec('    *"the launcher`s creation flags include a new process group"*')
    rec('    ### ### **FLAGS : 0x%08X = %s**' % (c3.get('flags') or 0, ' | '.join(c3.get('flag_names') or [])))
    rec('    ### ### **AND THE CELL SAYS LESS THAN IT SEEMS TO.** ### b495`s launcher ALSO carried')
    rec('    ### `CREATE_NEW_PROCESS_GROUP` (Component 1 (a): %s) and its build was killed anyway.' % c1.get('new_group'))
    rec('    ### ### **A NEW PROCESS GROUP WAS NOT WHAT b495 LACKED.** ### What differs is the console:')
    rec('    ### DETACHED_PROCESS then (%s), CREATE_NEW_CONSOLE now (%s).' % (c1.get('detached'), c3.get('new_console')))
    rec('')

    rec('### THE SEAT`S THREE.')
    rec('-' * 104)
    s1 = bool(c1.get('new_group') and c1.get('detached') and not c1.get('new_console')
              and c1.get('sender') == 'NOT ESTABLISHED')
    rec('  **(S1)** ### **%s.**' % word(s1))
    rec('    *"Component 1 will print that b495`s build shared neither the seat`s process group nor its')
    rec('    console, and will name no event of the seat`s shell that could deliver the signal."*')
    rec('    own group %s ; no console (DETACHED_PROCESS) %s ; sender : %s'
        % (c1.get('new_group'), c1.get('detached'), c1.get('sender')))
    rec('    ### ### **CHEAP, AND THE FACE SAID SO**: drawn from a declared peek at b495`s launch code.')
    rec('    ### And the component found what the peek did not ask about: ### **THE FIRST KILL FOLLOWS')
    rec('    ### THE END OF THE SEAT`S b495 TURN BY %.3f s.** ### That is a coincidence in time and the'
        % (c1.get('kill_after_turn_end_s') or 0))
    rec('    ### record gives it no mechanism; it is banked, not explained.')
    rec('')
    s2 = (c2.get('cache_exit') == 0) if 'cache_exit' in c2 else None
    rec('  **(S2)** ### **%s.**' % word(s2))
    rec('    *"`lake exe cache get` exits 0 at the pinned Mathlib commit"* -- exit %s' % c2.get('cache_exit'))
    rec('')
    s3 = (c2.get('kernel_status') == '') if 'kernel_status' in c2 else None
    rec('  **(S3)** ### **%s.**' % word(s3))
    rec('    *"Component 2 leaves the kernel`s tracked tree unchanged"* -- `git status --porcelain` : %r'
        % c2.get('kernel_status'))
    rec('')
    nav = [n1, n2, n3]
    seat = [s1, s2, s3]
    rec('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
        % (nav.count(True), nav.count(False), nav.count(None)))
    rec('### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE %d.**'
        % (seat.count(True), seat.count(False), seat.count(None)))
    rec('=' * 104)
    io.open(os.path.join(D, 'b498_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3,
                   nav_held=nav.count(True), seat_held=seat.count(True)),
              io.open(os.path.join(D, 'b498_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print('  written: b498_desk_notes.txt, b498_scores.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
