# -*- coding: utf-8 -*-
"""b368_index_append.py -- ONE KEY, ONE ROW. ### APPEND ONLY, IDEMPOTENT, READ BACK.

### ### ### **THE ARM THIS FILE EXISTS FOR IS `G-NOTCLOSED`.** ### A reader who asks *what `b368`
### settled* must be handed: ### that the eighteen were ### **RE-DERIVED, NOT CARRIED**; ### that all of
### them are ### **RETIRED** ### and none was ever invented; ### that the retirement ledger ### **NAMES
### ### ONLY HALF OF THEM**; ### that the front document was ### **ANNOTATED, NOT REPAIRED**, and its
### list ### **STILL EXPORTS EIGHTEEN ABSENT NAMES**; ### and that ### **NO `.lean` FILE WAS WRITTEN AND
### ### NO DESK ITEM WAS CLOSED.**
### ### **`the export list is repaired`, `the eighteen are removed`, `a successor is named` AND `the desk
### is confirmed` STAY UNKEYED**, each checked NO KEY before this file was written.
### ### **AND TWO ALIASES ARE DELIBERATELY NOT CLAIMED:** ### `the front document` alone names a file
### rather than a finding, and `retired` alone is the whole record's vocabulary.
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

CORR = io.open(os.path.join(D, 'b368_corr_run.txt'), encoding='utf-8', errors='replace').read()
R1 = re.search(r'row to append : (\d+)', CORR).group(1)
E = json.load(io.open(os.path.join(D, 'b368_reads.json'), encoding='utf-8'))
C = json.load(io.open(os.path.join(D, 'b368_classify.json'), encoding='utf-8'))
R = json.load(io.open(os.path.join(D, 'b368_reconcile.json'), encoding='utf-8'))
K = json.load(io.open(os.path.join(D, 'b368_desk.json'), encoding='utf-8'))
F = json.load(io.open(os.path.join(D, 'b368_filing.json'), encoding='utf-8'))


def s(x):
    return str(x)


KEY_ANCHOR = 'KEYS = {\n'
KEY_NEW = (
    "    'front-document-reconciled': ['the front document reconciled', 'the currency block',\n"
    "                                 'the layer-1 export list', 'the eighteen absent names',\n"
    "                                 'the desk freshness rule'],\n"
)

ROW_ANCHOR = ('INDEX = [\n'
              '    # (key, act, one-line statement, grade as its own act recorded it, location)\n')

ROW_NEW = (
    '    # ### THE FRONT DOCUMENT RECONCILED, APPEND-ONLY (b368).\n'
    '    ("front-document-reconciled", "b368 (a live read, a classification and one appended block; it writes no Lean, runs no build and edits no sentence)",\n'
    '     "THE FRONT DOCUMENT IS RECONCILED BY AN APPENDED CURRENCY BLOCK, AND THE LIST ITSELF IS STILL WRONG. Of the ' + s(C['exported']) + ' names AGENTS.md exports at Layer 1, ' + s(C['n_present']) + ' are declared in this kernel own"\n'
    '     " six .lean files and ' + s(C['n_absent']) + ' are ABSENT, at SIDE-effects ref ' + C['ref'] + ' = ' + C['head'] + ', pinned by ls-remote before the first classification and unmoved since b367. THE EIGHTEEN WERE"\n'
    '     " RE-DERIVED AND NOT CARRIED: b367 constant is held in the classifier as a COMPARISON ONLY and is never an input to the count, and the two independent derivations AGREE. EVERY ABSENT NAME IS"\n'
    '     " RETIRED: RENAMED ' + s(C['renamed_rows']) + ', NEVER EXISTED 0. Each is classified on its own evidence and none from its own sound -- the ledger names the declaration, or its layer entry records the removal, or the"\n'
    '     " repository own history shows the name present in an earlier commit and gone now, and that third kind is why no name is NEVER EXISTED. RENAMED 0 IS A REFUSAL, NOT AN ABSENCE OF LOOKING: a"\n'
    '     " successor was accepted only from a declared mapping, the mapping is deliberately empty, and one resemblance -- a retired name and a live one differing only in case -- was MET AND REFUSED. AND"\n'
    '     " THE NEW FINDING, WHICH NEITHER b157 NOR b367 HAD: THE RETIREMENT LEDGER NAMES ONLY ' + s(C['retired_named_by_ledger']) + ' OF THE ' + s(C['n_absent']) + '. Another ' + s(C['retired_layer_entry']) + ' are covered only by their layer entry, which"\n'
    '     " records that the layer skeletons were retired without listing which, and ' + s(C['retired_history_only']) + ' HAS NO LEDGER ENTRY FOR ITS LAYER AT ALL -- THE LEDGER IS ACCURATE ABOUT WHAT IT SAYS AND INCOMPLETE"\n'
    '     " ABOUT WHAT IT NAMES, and the third group is the sharper half: there the ledger omits a name, here it omits a whole layer. ' + s(E['reads']) + ' reads, ' + s(E['without_anchor']) + ' without an anchor.",\n'
    '     "### THE DOCUMENT IS ANNOTATED, NOT REPAIRED, AND THE HALF-REPAIR IS THE POINT: the Layer-1 list above the block STILL EXPORTS ' + s(R['list_above_still_exports_absent']) + ' ABSENT NAMES and this act did not edit it. A"\n'
    '     " reader who stops at the list is still misled; a reader who reaches the block is not. REPAIRING THE LIST EDITS SENTENCES, AND THAT IS THE AUTHOR DECISION. ### THE BRANCH WAS DECIDED BY THE"\n'
    '     " CLASSIFICATION, NOT CHOSEN: every exported name has a kind and the kinds partition the list, so the price-and-route branch was UNREACHABLE. ### APPEND-ONLY IS MECHANICAL AND WAS READ BEFORE"\n'
    '     " THE PUSH: the file before is a true prefix of the file after (' + s(R['prefix_of_file']) + ') and of its committed blob (' + s(R['prefix_of_blob']) + '). ### THE BLOCK EXPORTS NOTHING -- ' + s(R['export_shaped_lines']) + ' lines in the document own"\n'
    '     " export shape, ' + s(len(R['unstatused'])) + ' absent names outside a status row -- which is a check on the BLOCK, not on the document. ### NO .lean FILE WAS TOUCHED, NO BUILD WAS RUN, NO AXIOM PROFILE WAS COMPUTED"\n'
    '     " AND NO EXISTING SENTENCE WAS EDITED. ### THE RETIREMENTS ARE REPORTED, NOT ENDORSED. ### THE DESK-FRESHNESS RULE IS FILED as a TECHNE module, LOCAL ONLY, with b367 and b157 as incidents, and"\n'
    '     " IT STATES ITS OWN LIMIT: a tool can demand that an item CARRY a file and a date, and no tool can check that the named file still confirms it. ### THE SWEEP PRODUCED MARKS, NOT VERDICTS:"\n'
    '     " ' + s(K['confirmed']) + ' of ' + s(K['items']) + ' CONFIRMED-BY-FILE, ' + s(K['unconfirmed']) + ' UNCONFIRMED, ' + s(K['items_closed']) + ' CLOSED -- and that result is WEAKER THAN IT LOOKS, because a file that mentions an item is not a file that confirms it."\n'
    '     " ### NO HOOK WAS INSTALLED and the absence of a pre-push hook in SIDE-effects is FILED AS A FINDING. ### NO ACT IS RE-VERDICTED: b157 and b367 are RE-MEASURED. ### NO GRADE IS CONFERRED BY A"\n'
    '     " SEAT. ### NOTHING WAS COMPUTED ABOUT THE OBJECT. ### NO COORDINATE IS CLOSED. ### THE PARTITION STAYS UNDECIDED. ### THE CLAUSE HAS NOT MOVED. ### M-2 UNCHANGED",\n'
    '     "data/b368_the_front_document_reconciled.txt; data/' + E['run_file'] + '; data/' + C['run_file'] + '; data/' + R['run_file'] + ';"\n'
    '     " data/' + K['run_file'] + '; data/' + F['run_file'] + ';"\n'
    '     " data/b368_registration_2026-09-08.txt (LOCKED before any write of this act, on the audit own exit code);"\n'
    '     " tools/b368_classify.py (the live ref, the re-derivation and the per-name evidence); tools/b368_reconcile.py (the branch and the append-only arms);"\n'
    '     " tools/b368_desk.py (the rule and the sweep); SIDE-effects at ' + C['ref'] + ' = ' + C['head'] + ', READ and annotated but with no .lean file written;"\n'
    '     " SIDE-effects AGENTS.md (one appended currency block); PLACE-papers OPEN_TRAILS.md (' + F['entry'] + ' marked ' + F['status'] + ', an append-only block; FACES_LEDGER.md NOT written, no row moved);"\n'
    '     " TECHNE-Core ' + K['module'] + ' (local commit ' + K['techne_head'] + ', NOT PUSHED); CORRESPONDENCE.md row ' + R1 + '"),\n'
)

ALIASES = ('the front document reconciled', 'the currency block', 'the layer-1 export list',
           'the eighteen absent names', 'the desk freshness rule')
MUST_NOT_HIT = ('the export list is repaired', 'the eighteen are removed', 'a successor is named',
                'the desk is confirmed')


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(q):
    r = subprocess.run([sys.executable, PATH, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    print('=' * 100)
    print('b368 -- THE INDEX KEY. ### THE FRONT DOCUMENT RECONCILED, APPEND-ONLY.')
    print('=' * 100)
    pre = {}
    for q in MUST_NOT_HIT:
        out, _rc = query(q)
        pre[q] = no_key(out)
        print('    %-40s NO KEY before : %s' % (q, pre[q]))
    have_key = ("'front-document-reconciled'" in txt)
    have_row = ('"front-document-reconciled"' in txt)
    print('  front-document-reconciled key/row already present : %s / %s' % (have_key, have_row))
    written = not (have_key and have_row)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        print('  ### HARD FAILURE -- an anchor is not in the file.')
        return 2
    if written:
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
    out, rc = query('front-document-reconciled')
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    print('  READ BACK : front-document-reconciled returns %d row(s), 1 required  %s'
          % (n, 'PASS' if good else '### FAIL ###'))
    for q in ALIASES:
        o, _rc = query(q)
        g = (not no_key(o)) and 'front-document-reconciled' in o
        ok = ok and g
        print('    %-44s reaches the b368 key : %s  %s' % (q, g, 'PASS' if g else '### FAIL ###'))
    print('  ### ### **G-NOTCLOSED -- THE ARM THIS FILE EXISTS FOR.**')
    a1 = 'RE-DERIVED AND NOT CARRIED' in out
    a2 = 'ANNOTATED, NOT REPAIRED' in out and 'STILL EXPORTS' in out
    a3 = 'NO .lean FILE WAS TOUCHED' in out and 'NO EXISTING SENTENCE WAS EDITED' in out
    a4 = 'INCOMPLETE ABOUT WHAT IT NAMES' in out
    a5 = 'MARKS, NOT VERDICTS' in out and 'WEAKER THAN IT LOOKS' in out
    a6 = 'A REFUSAL, NOT AN ABSENCE OF LOOKING' in out
    ok = ok and a1 and a2 and a3 and a4 and a5 and a6
    print('    the eighteen re-derived and not carried                      : %s' % a1)
    print('    ### annotated not repaired, and the list still exports        : %s' % a2)
    print('    ### no Lean written and no existing sentence edited           : %s' % a3)
    print('    ### the ledger incomplete about what it names                 : %s' % a4)
    print('    ### the sweep marks, and its result weaker than it looks      : %s' % a5)
    print('    ### RENAMED 0 stated as a refusal, not an absence of looking  : %s' % a6)
    post = {}
    for q in MUST_NOT_HIT:
        o, _rc = query(q)
        post[q] = no_key(o)
        g = pre[q] and post[q]
        ok = ok and g
        print('    %-40s NO KEY after  : %s  %s' % (q, post[q], 'PASS' if g else '### FAIL ###'))
    print('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
