# -*- coding: utf-8 -*-
"""b382_account.py -- COMPONENTS 1-4. ### **THE ACCOUNT, THE CONCLUSION, THE CAUTION, THE OPEN ITEMS.**

### ### **EVERY CLAIM THE ACCOUNT MAKES ABOUT A PRIOR ACT IS CARRIED BY A LINE FROM THAT ACT'S OWN
### ### BANK**, quoted verbatim with its file and its line number, and ### **RE-READ OUT OF THAT FILE
### ### BEFORE THE ACCOUNT IS WRITTEN.** ### A quotation that does not re-read is a ### **HARD
### ### FAILURE** ### here, not a footnote -- the locked face's BAR 2.
### ### **THE CONNECTIVE PROSE IS THIS SEAT'S. ### THE FIGURES ARE NOT.**

### ### **AND THE LOAD-BEARING COUNT IS RE-MEASURED RATHER THAN CARRIED.** ### The second half of the
### conclusion -- that role is stated by too few documents to be recoverable from their prose --
### rests on a count, so ### **THE COUNT IS TAKEN AGAIN HERE UNDER ALL THREE READINGS THE SEQUENCE
### ### PRODUCED** ### and the conclusion is required to survive the most generous of them.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def quote(built, label, width=96):
    """### **PULL A READ BY ITS LABEL AND RE-READ IT OUT OF ITS OWN FILE AT ITS OWN LINE.**"""
    hit = [b for b in built if b['label'] == label]
    assert len(hit) == 1, 'label %r matched %d reads' % (label, len(hit))
    b = hit[0]
    src = os.path.join(D, b['file'])
    if not os.path.exists(src):
        return b, False, None
    ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
    ok = (b['line'] - 1 < len(ls)) and ls[b['line'] - 1].rstrip(chr(13)) == b['text']
    return b, ok, (ls[b['line'] - 1] if b['line'] - 1 < len(ls) else None)


def main():
    E = J('b382_reads')
    built = E['built']
    RS80, C81, EX81, VD81 = J('b380_rescore'), J('b381_control'), J('b381_exemplars'), J('b381_verdict')
    P75 = J('b375_population')
    CL375 = J('b375_clusters')
    reread_failures = []

    def say(label, note=None):
        b, ok, live = quote(built, label)
        if not ok:
            reread_failures.append((label, b['file'], b['line']))
        rec('###   `%s` line %d %s' % (b['file'], b['line'], '' if ok else '### ### **DID NOT RE-READ**'))
        rec('###   | %s' % b['text'].strip())
        if note:
            rec('###   %s' % note)
        rec('')

    rec('=' * 100)
    rec('b382 -- COMPONENTS 1-4. ### THE ACCOUNT, THE CONCLUSION, THE CAUTION, THE OPEN ITEMS.')
    rec('=' * 100)

    # =========================================================== COMPONENT 1 -- THE ACCOUNT
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE SEQUENCE`S OWN ACCOUNT. ### **QUOTED, NOT SUMMARISED.**')
    rec('-' * 100)
    rec('### Seven acts. ### **WHAT EACH ASKED, WHAT IT FOUND, AND WHAT IT LEFT** -- and every claim')
    rec('### about a prior act carried by a line from that act`s own bank, re-read before it was')
    rec('### written here.')
    rec('')

    rec('### ### **`b375` -- THE KEYSTONE CENSUS.**')
    rec('### ### **ASKED:** ### what the corpus means by `keystone`, and how many documents are one.')
    rec('### ### **FOUND:** ### three definitions, and the same instrument answering differently')
    rec('### depending which it runs on.')
    say('b375 -- the same instrument on two definitions gives opposite answers')
    say('b375 -- the instrument did not change, the definition did')
    rec('### ### **LEFT:** ### six subject clusters with documents and no keystone, ### **FILED AND')
    rec('### ### NOT OPENED** ### -- `%d` in the banked count, unchanged since.'
        % len(CL375['subject_clusters_without_keystone']))
    say('b375 -- six clusters have documents and no keystone')

    rec('### ### **`b376` -- THE TWO-AXIS READ.**')
    rec('### ### **ASKED:** ### whether the three tests measure one thing or two -- a document`s ROLE')
    rec('### (does it synthesise against other content?) and its APPARATUS (can a stranger traverse')
    rec('### its correspondence table?).')
    rec('### ### **FOUND:** ### ### **ALL THREE TESTS CROSS THE QUADRANTS.** ### None equals either')
    rec('### axis, and they disagree because each asks two questions at once.')
    say('b376 -- every one of the three tests crosses the quadrants')
    rec('### ### **AND THE CORPUS`S OWN CENSUS DRIFTS BETWEEN WHAT IT STATES AND WHAT IT DOES:** ###')
    rec('### it states three clauses, operationalises two of them through proxies, drops the third')
    rec('### entirely, and adds a size floor its definition never mentions.')
    say('b376 -- the census drops clause (iii) and adds a size floor')
    rec('### ### **LEFT:** ### the role column, and the figure the whole sequence turns on.')
    say('b376 -- 340 of 349 documents')

    rec('### ### **`b377` -- THE UNBLOCKED OBLIGATION.**')
    rec('### ### **ASKED:** ### whether the documents the apparatus axis marked deficient really lack')
    rec('### what the taxonomy requires.')
    rec('### ### **FOUND:** ### they mostly do not. ### The missing element was not the terminal.')
    say('b377 -- the pin was the missing element, not the terminal')
    rec('### ### **LEFT:** ### the reconciliation figure, ### **AS A FLOOR AND NOT AN ANSWER**, with')
    rec('### the wider question named and deliberately not re-measured.')
    say('b377 -- the banked figure is a floor and not an answer')

    rec('### ### **`b378` -- THE REFS WIDENED.**')
    rec('### ### **ASKED:** ### whether the identifiers no kernel declares are really absent.')
    rec('### ### **FOUND:** ### a count taken at one ref is not a count -- and the sweep that found')
    rec('### them had been ### **SILENTLY DEAD**, every invocation dying on a rejected pattern while')
    rec('### the caller read the fatal exit as `no matches`.')
    say('b378 -- an upper bound taken at one ref is not a count')
    say('b378 -- b377`s number was never wrong')
    rec('### ### **LEFT:** ### the standing clause this act still runs under -- ### **AN ABSENCE')
    rec('### ### NEEDS A PROVED SEARCH, AND AN ERROR EXIT IS NOT AN ANSWER.**')
    rec('')

    rec('### ### **`b379` -- THE APPARATUS AXIS RE-SCORED.**')
    rec('### ### **ASKED:** ### whether the apparatus column was undercounting.')
    rec('### ### **FOUND:** ### it was, and correcting it changed nothing that mattered.')
    say('b379 -- correcting the suspect column moved nothing where the ruling needs movement')
    say('b379 -- the correction leaves the role column exactly where it was')
    rec('### ### **LEFT:** ### the observation the next two acts were built on -- ### **FOUR')
    rec('### ### WIDENINGS OF THE APPARATUS COLUMN, AND NOT ONE MOVEMENT OF THE ROLE COLUMN.**')
    rec('')

    rec('### ### **`b380` -- THE ROLE AXIS, SCORED STRUCTURALLY.** ### **THE FIRST STRUCTURAL')
    rec('### ### FEATURE: REACH.**')
    rec('### ### **ASKED:** ### whether role can be read from what a document DRAWS ON rather than')
    rec('### from what it says.')
    rec('### ### **FOUND:** ### the column moved for the first time -- and the predicate failed its')
    rec('### own control on exactly the distinction the rubric is about.')
    say('b380 -- the role column moved and the predicate failed its own control')
    say('b380 -- agreement over all nine that declare anything')
    say('b380 -- the A- column is measuring narrow reach')
    rec('### ### **AND THE PREMISE WAS MEASURED, NOT ASSUMED**, which is why the rest of the sequence')
    rec('### means anything.')
    say('b380 -- the premise survives its own widening')

    rec('### ### **`b381` -- THE CONTROL REBUILT, AND CO-LOCATION TESTED.** ### **THE SECOND')
    rec('### ### STRUCTURAL FEATURE: CO-LOCATION.**')
    rec('### ### **ASKED:** ### whether a control that can fail in both directions would separate')
    rec('### under a feature that reads WHERE the sources sit rather than how far they reach.')
    rec('### ### **FOUND:** ### `b380`s control could not have taught its predicate anything --')
    say('b381 -- a control that cannot fail on one side is one defect')
    rec('### -- so it was rebuilt from the record`s own purpose statements, and the new feature')
    rec('### failed on the rebuilt one.')
    say('b381 -- heads stating a gathering purpose')
    say('b381 -- the balance of the rebuilt control')
    say('b381 -- the control was rebuilt so it could fail and the feature failed')
    say('b381 -- the two sets overlap completely')
    say('b381 -- the branch, not adopted, the corpus not scored')
    rec('### ### **LEFT:** ### the fact this act is sent to conclude from.')
    say('b381 -- two independent structural features now fail the same distinction')

    # ============================================ THE LOAD-BEARING COUNT, RE-MEASURED
    rec('-' * 100)
    rec('### THE STANDING COUNT, RE-MEASURED UNDER ALL THREE READINGS THE SEQUENCE PRODUCED.')
    rec('-' * 100)
    rec('### ### **THIS IS THE FIGURE THE SECOND HALF OF THE CONCLUSION RESTS ON**, so it is taken')
    rec('### again here rather than carried.')
    pop = RS80['population']
    strict = RS80['statement_tally'].get('A?', 0)
    broad = RS80['statement_broad_tally'].get('A?', 0)
    scanned81, wide81 = EX81['scanned'], EX81['wide_hits']
    rec('###   %-58s %-14s %s' % ('READING', 'STATES A ROLE', 'SAYS NOTHING'))
    rec('###   %-58s %-14s %s'
        % ('b376 strict -- one sentence carrying both halves', '%d of %d' % (pop - strict, pop),
           '%d (%.1f%%)' % (strict, 100.0 * strict / pop)))
    rec('###   %-58s %-14s %s'
        % ('b376 broad -- any self-description a reader would accept',
           '%d of %d' % (pop - broad, pop), '%d (%.1f%%)' % (broad, 100.0 * broad / pop)))
    rec('###   %-58s %-14s %s'
        % ('b381 -- a head stating a GATHERING purpose', '%d of %d' % (wide81, scanned81),
           '%d (%.1f%%)' % (scanned81 - wide81, 100.0 * (scanned81 - wide81) / scanned81)))
    rec('### ### **THE THREE DISAGREE, AND THE MOST GENEROUS OF THEM IS `b381`S: `%d` OF `%d`.**'
        % (wide81, scanned81))
    rec('### ### **AND EVEN THE MOST GENEROUS READING FINDS ROLE STATED BY A MINORITY**, and finds')
    rec('### it stated ### **ALMOST ENTIRELY ON ONE SIDE:** ### `%d` heads state a gathering purpose'
        % wide81)
    rec('### and ### **`%d` DOCUMENTS DECLARE SYNTHESIS IN THEIR CLASS LINE.** ### The side the'
        % C81['synthesis_n'])
    rec('### rubric turns on is the side the corpus is nearly silent about.')
    generous_minority = wide81 < scanned81 / 2.0
    rec('### ### ### **THE CONCLUSION SURVIVES THE MOST GENEROUS READING : %s.**' % generous_minority)
    rec('')

    # ======================================================= COMPONENT 2 -- THE CONCLUSION
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE CONCLUSION THE EVIDENCE SUPPORTS. ### **ABOUT METHOD, NOT A CLASS.**')
    rec('-' * 100)
    rec('### ### ### **ROLE IS NOT RECOVERABLE FROM A DOCUMENT`S STRUCTURE, AND IT IS STATED BY TOO')
    rec('### ### ### FEW DOCUMENTS TO BE RECOVERABLE FROM THEIR PROSE. ### SO A CLASS RULING, WHATEVER')
    rec('### ### ### IT RULES, MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION.**')
    rec('')
    rec('### ### **THE FIRST HALF IS EVIDENCED BY TWO FEATURES THAT FAILED ON A CONTROL BUILT TO')
    rec('### ### FAIL.** ### `b380`s reach called both documents that declare gathering synthesisers;')
    rec('### `b381`s co-location put `%d` of `%d` synthesis exemplars below its own bar while `%d` of'
        % (C81['synthesis_n'] - C81['synthesis_cplus'], C81['synthesis_n'], C81['gathering_cplus']))
    rec('### `%d` gathering exemplars cleared it, with the lowest synthesis ratio at `%.3f` against a'
        % (C81['gathering_n'], C81['lowest_synthesis_ratio']))
    rec('### highest gathering ratio of `%.3f`. ### **THE SETS OVERLAP COMPLETELY.**'
        % C81['highest_gathering_ratio'])
    rec('### ### **THE SECOND HALF IS EVIDENCED BY THE COUNT ABOVE**, re-measured under three')
    rec('### readings and surviving the most generous.')
    rec('')
    rec('### ### ### **AND THE LIMIT IS STATED WITH THE CONCLUSION AND NOT BELOW IT: TWO FAILED')
    rec('### ### ### FEATURES ARE EVIDENCE AND NOT PROOF.** ### A third feature might separate the')
    rec('### control. ### The order did not build one, and it recorded why: ### **IT WOULD NEED A')
    rec('### ### SENTENCE UNDERSTOOD RATHER THAN A STRUCTURE MEASURED, WHICH IS A READER AND NOT A')
    rec('### ### PREDICATE.** ### That is the author`s judgement, recorded as the author`s, and')
    rec('### ### **NOT A MEASUREMENT THIS SEAT MADE.**')
    rec('### ### **THIS IS WHAT THE EVIDENCE SUPPORTS, WHICH IS THE ORDER`S OWN WORD -- NOT WHAT IT')
    rec('### ### PROVES.**')
    rec('')
    rec('### ### **WHAT A DECLARATION RULE WOULD OBLIGE, PRICED FROM THE RECORD`S OWN FIGURES.**')
    rec('### ### ### **NOTHING BELOW IS ORDERED, RECOMMENDED OR RANKED. ### A PRICE IS NOT A')
    rec('### ### ### PROPOSAL.**')
    declared = P75['declared'] if isinstance(P75['declared'], int) else len(P75['declared'])
    notdecl = P75['not_declared'] if isinstance(P75['not_declared'], int) else len(P75['not_declared'])
    rec('###   ### **(i) A RULE STATING WHAT A DECLARATION MUST SAY.** ### One document, written')
    rec('###     once, by the author. ### The rubric already supplies the two halves and `b375`')
    rec('###     found the corpus carries ### **THREE DEFINITIONS OF `KEYSTONE`**, so the rule`s')
    rec('###     first job is to say which one a declaration is declaring against.')
    rec('###     ### **PRICE: ONE DOCUMENT. ### AND IT IS THE PIECE NOTHING ELSE CAN PROCEED')
    rec('###     ### WITHOUT.**')
    rec('###   ### **(ii) A CLASS LINE IN EVERY DOCUMENT THAT LACKS ONE.**')
    rec('###     ### `b375` measured the corpus`s class-line coverage: ### **`%d` DECLARE A CLASS'
        % declared)
    rec('###     ### LINE AND `%d` DO NOT**, out of `%d`.' % (notdecl, declared + notdecl))
    rec('###     ### **PRICE: `%d` DOCUMENTS TO EDIT**, each a one-line append.' % notdecl)
    rec('###     ### And what the line COSTS is not typing: ### **`%d` OF THE `%d` SAY NOTHING'
        % (strict, pop))
    rec('###     ### ABOUT THEIR OWN ROLE** ### under the strict reading, so for most documents')
    rec('###     the line ### **CANNOT BE WRITTEN FROM THE DOCUMENT`S OWN TEXT AND IS A JUDGEMENT')
    rec('###     ### -- THE AUTHOR`S.**')
    rec('###     ### ### **AND HOW MANY OF THE `%d` ARE ALSO AMONG THE `%d` IS NOT IN THE RECORD.**'
        % (notdecl, strict))
    rec('###     ### The class-line census banked counts and not lists, so the overlap is')
    rec('###     ### **NAMED UNCOUNTED RATHER THAN ESTIMATED** -- the same discipline the phase')
    rec('###     plan gets below. ### **TWO FIGURES OVER TWO POPULATIONS ARE NOT A SUBSET.**')
    rec('###   ### **(iii) A PHASED APPLICATION.**')
    rec('###     ### The record partitions the corpus by subject cluster and by layer, and `b375`')
    rec('###     found ### **`%d` CLUSTERS WITH NO KEYSTONE AT ALL**, which is where a phase boundary'
        % len(CL375['subject_clusters_without_keystone']))
    rec('###     would naturally fall.')
    rec('###     ### ### **PRICE: UNPRICED, AND NAMED UNPRICED RATHER THAN ESTIMATED.** ### The')
    rec('###     record counts documents and clusters; ### **IT DOES NOT COUNT REVIEWER EFFORT OR')
    rec('###     ### ELAPSED TIME**, and a phase plan is priced in those. ### `(E2)` MET.')
    rec('')

    # ========================================================= COMPONENT 3 -- THE CAUTION
    rec('-' * 100)
    rec('### COMPONENT 3 -- THE EXEMPLAR CAUTION, CARRIED FORWARD.')
    rec('-' * 100)
    rec('### ### **THE GATHERING EXEMPLAR SET WAS PRODUCED BY A MATCHER REPAIRED TWICE AFTER ITS')
    rec('### ### OUTPUT WAS SEEN**, and `b381` printed all three counts rather than the last one:')
    rec('###   `v1` ### **`%d`** ### of `%d` heads ### / ### `v2` ### **`%d`** ### / ### `v3` ###'
        % (EX81['loose_hits'], EX81['scanned'], EX81['loose2_hits']))
    rec('###   ### **`%d`** -- and the third is the set.' % EX81['wide_hits'])
    say('b381 -- the matcher was repaired twice after its output was seen')
    say('b381 -- the part a reader should be most sceptical of')
    rec('### ### ### **SO IF THAT SET IS EVER REUSED IT IS RE-DERIVED AND NOT INHERITED.** ### The')
    rec('### repairs each trace to text written before the run, but that is exactly the claim a')
    rec('### reader cannot check from the set alone.')
    rec('### ### **AND NOTHING CURRENTLY RESTS ON IT -- CHECKED AGAINST THE RECORD RATHER THAN')
    rec('### ### REPEATED FROM IT:** ### `b381`s banked control records `corpus_scored = %s` and its'
        % C81['corpus_scored'])
    rec('### verdict records `prior_scores_overwritten = %d`, so ### **THE BRANCH DID NOT ADOPT AND'
        % VD81['prior_scores_overwritten'])
    rec('### ### NO COLUMN, TABLE OR CLASS DEPENDS ON THE SET.**')
    nothing_rests = (C81['corpus_scored'] is False and VD81['prior_scores_overwritten'] == 0
                     and C81['adopted'] is False)
    rec('### ### ### **NOTHING RESTS ON IT : %s**, measured.' % nothing_rests)
    rec('')

    # ====================================================== COMPONENT 4 -- THE OPEN ITEMS
    rec('-' * 100)
    rec('### COMPONENT 4 -- THE OPEN ITEMS, RESTATED FOR THE RULING.')
    rec('-' * 100)
    LISTS = [
        ('LIST 1', 'the rows that cite at a ref nobody can name',
         'b378 widened the refs and b379 gave the categories a vocabulary; nothing has closed it'),
        ('LIST 2', 'the rows grading a declaration the record has classified absent',
         'b373 listed them with their carriers and ROUTED them; no grade has moved'),
        ('LIST 3', 'the undated figures across the roster',
         'b374 listed every figure stated without a ref; none has been dated'),
        ('LIST 4', 'the bibliography entries nothing cites',
         'b374 found entries the register carries that appear nowhere else; none rewritten'),
    ]
    rec('### ### **THE FOUR LISTS, BY NAME AND `OPEN`:**')
    for tag, name, why in LISTS:
        rec('###   ### **%s -- %s. ### OPEN.**' % (tag, name))
        rec('###     %s.' % why)
    rec('')
    rec('### ### **THE DOWNLOAD-LAYER BOOK`S REGISTRY DRIFT -- OPEN, AND THE AUTHOR`S.** ### `(R14)`')
    rec('### settled that the class ruling reaches the book and the mirroring ruling does not, and')
    rec('### ### **THE RULING`S OWN WORDS LEAVE THE DRIFT OPEN AND THE AUTHOR`S.** ### The registry')
    rec('### carries it at one version and class, later documents at two others; ### **THE REGISTRY')
    rec('### ### IS NOT EDITED AND THE BOOK IS NOT OPENED.**')
    rec('')
    rec('### ### **THE SIX SUBJECT CLUSTERS WITH REGISTRY ROWS AND NO KEYSTONE -- FILED, NOT')
    rec('### ### OPENED.** ### `%d` clusters, unchanged since `b375` banked them, and `b375`s own'
        % len(CL375['subject_clusters_without_keystone']))
    rec('### words stand: ### **A CLUSTER MAY SIMPLY NOT BE READY FOR ONE**, and whether that is a')
    rec('### defect or a state is a ruling.')
    rec('')
    rec('### ### **THE RECONCILIATION FIGURE -- A FLOOR AGAINST THE WIDER QUESTION.** ### `b377`s')
    rec('### amendment fixed it as a floor and forbade re-measuring it; ### **NO LATER ORDER HAS')
    rec('### ### LIFTED THAT AND THIS ACT DOES NOT RE-MEASURE IT.**')
    say('b377 -- the banked figure is a floor and not an answer')
    rec('### ### ### **NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF.**')
    rec('')

    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s'
        % (len(reread_failures), reread_failures or ''))
    rec('### ### **NO CLASS IS RULED. ### NO DECLARATION IS MOVED. ### NO DECLARATION RULE IS')
    rec('### ### ORDERED. ### NO LIST IS CLOSED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b382_account_notes', LINES)
    out = dict(acts_covered=7, quotations=len([b for b in built if b['tag'] in ('SEQ', 'CAUTION')]),
               reread_failures=reread_failures, reread_ok=(not reread_failures),
               population=pop, strict_silent=strict, broad_silent=broad,
               b381_scanned=scanned81, b381_wide=wide81,
               generous_minority=generous_minority,
               declared_class_line=declared, not_declared_class_line=notdecl,
               clusters_without_keystone=len(CL375['subject_clusters_without_keystone']),
               nothing_rests_on_the_set=nothing_rests,
               lists_open=len(LISTS), open_items=4,
               class_ruled=False, declaration_rule_ordered=False,
               phased_application_priced=False,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b382_account.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 1 if reread_failures else 0


if __name__ == '__main__':
    sys.exit(main())
