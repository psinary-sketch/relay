# -*- coding: utf-8 -*-
"""b369_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTAUDITED`.** ### A reader who asks *what `b369`
### settled* must be handed: ### that the list is ### **REPAIRED IN PLACE** ### and the original
### ### **PRESERVED VERBATIM IN THE SAME FILE**; ### that the front document is ### **STILL NOT
### ### CORRECT** ### because its count claim stands untouched; ### that ### **`b368`'s SPLIT WAS WRONG
### ### AND ITS COUNT WAS RIGHT**; ### that the two hygiene items are done and ### **ONLY ONE OF THEM
### ### SURVIVES A CLONE**; ### and that the pass was ### **PRICED AND NOT RUN.**
### ### **`the federation is audited`, `the front document is correct`, `the count claim is repaired`
### AND `b368 is re-verdicted` STAY UNKEYED**, each checked NO KEY before this file was written.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PATH = os.path.join(ROOT, 'tools', 'banked_index.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORR = io.open(os.path.join(D, 'b369_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b369_reads.json'), encoding='utf-8'))
R = json.load(io.open(os.path.join(D, 'b369_repair.json'), encoding='utf-8'))
K = json.load(io.open(os.path.join(D, 'b369_hygiene.json'), encoding='utf-8'))
P = json.load(io.open(os.path.join(D, 'b369_pass.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b369_filing.json'), encoding='utf-8'))
Q = json.load(io.open(os.path.join(D, 'b369_desk.json'), encoding='utf-8'))
CS = next((x['count_shapes'][0] for x in P['rows']
           if x['name'] in P['construction_candidates'] and x['count_shapes']), '?')


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'list-repaired-in-place': ['the list repaired', 'the list repaired in place',\n"
    "                              'the original preserved verbatim', 'the roster mended',\n"
    "                              'the refinement pass priced'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE LIST REPAIRED IN PLACE, THE ROSTER MENDED, THE PASS PRICED (b369).\n'
    '    ("list-repaired-in-place", "b369 (a bounded edit under ruling (R4), two hygiene repairs and a priced pass; it writes no Lean, runs no build and audits nothing)",\n'
    '     "THE LAYER-1 EXPORT LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED VERBATIM IN THE SAME FILE. Ruling (R4): append-only is right for a ledger, where a reader reads the file; it is wrong for"\n'
    '     " a list, where a reader reads the list. ' + s(R['rows_replaced']) + ' export rows were located, quoted verbatim into the currency note, verified byte-for-byte, and ONLY THEN replaced by ' + s(R['rows_written']) + '. The repaired list"\n'
    '     " carries ' + s(len(R['still_absent'])) + ' of the names the classification calls absent, by a CONTENT predicate over the rows themselves. THE EDIT IS BOUNDED AND MEASURED: every byte above the rows is its committed blob own"\n'
    '     " (' + s(R['bar3_above']) + ') and every byte below them up to the appended note is too (' + s(R['bar3_below']) + '), both read BEFORE THE PUSH -- AN EDIT IS NOT AN APPEND. The classification was RE-DERIVED for the third time and"\n'
    '     " AGREES for the third time: of ' + s(R['exported']) + ' names, ' + s(R['n_present']) + ' declared and ' + s(R['n_absent']) + ' absent. AND THE RE-DERIVATION CAUGHT WHAT NOBODY REGISTERED: b368 SHARPER CLAIM IS WRONG. b368 reported one"\n'
    '     " retired name as having NO LEDGER ENTRY FOR ITS LAYER AT ALL; the ledger carries an entry HEADED BY THAT DECLARATION OWN NAME. b368 predicate required a backtick or a slash before a name and the"\n'
    '     " ledger names that one as a bare heading -- A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE. Re-derived from the ledger own entry headings: ' + s(R['n_named']) + ' named outright, ' + s(R['n_by_abbr']) + ' named only by its slash"\n'
    '     " abbreviation (kept apart, because reading an abbreviation as naming its expansions is a judgement not a string match), ' + s(R['n_layer_only']) + ' covered only by a layer entry, and ' + s(R['n_silent']) + ' not covered at all --"\n'
    '     " EVERY RETIRED NAME IS REACHED BY THE LEDGER. THE TWO HYGIENE ITEMS ARE DONE: the exclusion kernel is in the pins roster and carries the pre-push hook, byte-identical to the one tracked source"\n'
    '     " and exercised in BOTH POLARITIES with ' + s(K['repos_failing']) + ' failing. THE REFINEMENT PASS IS PRICED AND NOT RUN: ' + s(P['repos_on_account']) + ' repositories enumerated LIVE, ' + s(P['programme']) + ' of them programme material.",\n'
    '     "### THE FRONT DOCUMENT IS NOT NOW CORRECT: the paragraph above the repaired list still asserts a count of framework consequences and THIS ACT DID NOT TOUCH IT, because the order said the LIST is"\n'
    '     " corrected and a count is not a name -- which is why the trail is UPDATED and NOT CLOSED. ### THE PRESERVATION IS NOT AN APPEND AND THE ACT DOES NOT CLAIM A PREFIX ARM IT CANNOT HAVE. ### NO ACT"\n'
    '     " IS RE-VERDICTED: b368 COUNT stands and is confirmed a third time; its SPLIT is corrected, which is a measurement replaced by a better measurement. ### (R5) HOLDS: no retirement reason is supplied"\n'
    '     " beyond what the kernel own record carries, and where the record is silent the act says the record is silent. ### NO SENTENCE OF b368 BLOCK IS EDITED -- it is NAMED and marked SUPERSEDED, because"\n'
    '     " a ruling that reverses a disposition dates the prose that announced it. ### TWO OWNER INSTRUMENTS WERE EDITED AND BOTH WERE NAMED ON THE REGISTRATION FACE BEFORE THE EDIT. ### THE TWO HYGIENE"\n'
    '     " REPAIRS ARE NOT EQUAL IN DURABILITY: the roster mend is TRACKED and survives a clone, the hook install is NOT, because .git/hooks/ is untracked. ### REPOSITORIES AUDITED ' + s(P['repositories_audited']) + ', SURFACES READ FOR"\n'
    '     " CORRECTNESS ' + s(P['surfaces_read_for_correctness']) + ', REPOSITORIES GRADED ' + s(P['repositories_graded']) + ' -- audit nothing was the cap and it held; a count-SHAPED string is not a claim and an age is not a staleness. ### THE RANKING IS OF"\n'
    '     " EXPOSURE, NOT OF ERROR, AND WHAT IT CANNOT SEE IS REPORTED: SIDE-effects is NOT on it, because its description carries no count shape and the claim lived in its front document -- a criterion is"\n'
    '     " only as wide as the surface it reads. ### THE HINT: (H1) ' + P['h1'].split(' --')[0] + ' -- exactly one description uses the word construction and it carries the shape ' + CS + '; (H2) ' + P['h2'] + ', because deciding it requires"\n'
    '     " reading the profile, which is the audit. ### THE DESK SWEEP PRODUCED MARKS, NOT VERDICTS: ' + s(Q['confirmed']) + ' of ' + s(Q['items']) + ' CONFIRMED-BY-FILE, ' + s(Q['items_closed']) + ' CLOSED, and the same caveat a second time -- a file that"\n'
    '     " mentions an item is not a file that confirms it. A MEASUREMENT WHOSE RESULT AND WHOSE CAVEAT BOTH NEVER MOVE IS A MEASUREMENT NOBODY IS USING. ### NO LEAN FILE WRITTEN, NO BUILD RUN, NO AXIOM"\n'
    '     " PROFILE COMPUTED, NO SUCCESSOR NAMED, NO DESK ITEM CLOSED, NO GRADE CONFERRED. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE"\n'
    '     " CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b369_the_list_repaired.txt; data/' + E['run_file'] + '; data/' + R['run_file'] + '; data/' + K['run_file'] + ';"\n'
    '     " data/' + P['run_file'] + '; data/' + Q['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b369_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b369_repair.py (the located rows, the re-derivation, the ledger split and the three bars); tools/b369_hygiene.py (the roster mend and the hook);"\n'
    '     " tools/b369_pass.py (the live enumeration, the price and the ranking); SIDE-effects at ' + R['ref'] + ' = ' + R['head'] + ', its front document REPAIRED and no .lean file written;"\n'
    '     " PLACE-papers OPEN_TRAILS.md (' + F['entry'] + ' marked ' + F['status'] + ', an append-only block; FACES_LEDGER.md NOT written, no row moved);"\n'
    '     " tools/b303_pins.py and tools/b304_hooks.py (rosters mended); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the list repaired', 'the list repaired in place', 'the original preserved verbatim',
           'the roster mended', 'the refinement pass priced')
MUST_NOT_HIT = ('the federation is audited', 'the front document is correct',
                'the count claim is repaired', 'b368 is re-verdicted')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b369 -- THE INDEX KEY. ### THE LIST REPAIRED IN PLACE.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'list-repaired-in-place'" in txt)
    have_row = ('"list-repaired-in-place"' in txt)
    print('  list-repaired-in-place key/row already present : %s / %s' % (have_key, have_row))
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if not (have_key and have_row):
        new = txt
        if not have_key:
            new = new.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW, 1)
        if not have_row:
            new = new.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
    else:
        print('  ### NOTHING WRITTEN. (idempotent) ### **THE READ-BACK ARMS STILL RUN.**')
    ok = True
    out, rc = query('list-repaired-in-place')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : list-repaired-in-place returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'list-repaired-in-place' in o
        ok = ok and g
        print('    %-44s reaches the b369 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTAUDITED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED VERBATIM' in out
    a2 = 'THE FRONT DOCUMENT IS NOT NOW CORRECT' in out
    a3 = 'AN EDIT IS NOT AN APPEND' in out
    a4 = 'SHAPE FINDS ONE SHAPE' in out and 'SPLIT is corrected' in out
    a5 = 'audit nothing was the cap and it held' in out
    a6 = 'NOT EQUAL IN DURABILITY' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    repaired in place, original preserved verbatim               : %s' % a1)
    print('    ### the front document is NOT now correct                    : %s' % a2)
    print('    ### an edit is not an append                                 : %s' % a3)
    print("    ### b368's split corrected, and why                          : %s" % a4)
    print('    ### audit nothing held                                       : %s' % a5)
    print('    ### the two repairs are not equal in durability              : %s' % a6)
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        g = pre[q] and no_key(o)
        ok = ok and g
        print('    %-40s NO KEY after  : %s  %s' % (q, no_key(o), 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
