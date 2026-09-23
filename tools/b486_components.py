# -*- coding: utf-8 -*-
"""b486_components.py -- THE FOLD'S COMPONENTS. ### Run after the seal (`8c701ea1aea0ec7b...`).
### ### **A FOLD DECIDES NOTHING NEW.** ### Every verdict is quoted from the act that reached it.
"""
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


# ### ### **ONE LINE PER ACT, QUOTED FROM ITS OWN CLOSING BANK'S HEADLINE.** ### The fold adds
# ### nothing; where a phrase is compressed to fit, the act's own bank is the authority.
HEAD = {
    'b475': 'THE AXIOM RUN, DETACHED AND SERIALIZED UNDER (R80) -- launched, closed RUNNING',
    'b478': 'THE SITES SET AGAINST THE CONSTITUENTS, BY THEIR OWN WORDS',
    'b476': 'THE COMPRESSION EXPERIMENT REGISTERED, NOTHING COMPUTED',
    'b480': 'THE b475 LOG READ AS A SNAPSHOT, AND WHAT A SNAPSHOT CAN DECIDE',
    'b477': 'THE GRAM RUN, DETACHED, UNDER b476 AS AMENDED BY (R87)',
    'b481': 'THE CIRCULATION GATE, READ FOR WHAT IT NEEDS',
    'b483': 'THE b477 LOG READ TO ITS END, AND THE SIX SCORED',
    'b484': 'THE CURRENCY REPAIR, THE QUADRATURE WORK-ORDER, AND THE SUPPORT-EDGE TEST',
    'b485': 'THE TWO RECORDS READ, AND THE CIRCULATION GATE`S PASS RUN',
    'b482': 'THE XiPrime TOPIC READ AGAINST THE CORPUS STATEMENTS',
    'b479': 'THE SEVEN CLASSES AGAINST THE FORM, A READ (re-issued under (R96))',
}
CARRY = {
    'b475': 'the run started and the act closed RUNNING; no verdict of its own.',
    'b478': 'six sites against eight E0 constituents; TWO sites bear on nothing the table grades '
            'and THREE constituents no site touches.',
    'b476': 'registered with a diagonal control; two of the order`s own premises corrected.',
    'b480': '169 of 188 modules, every EXIT 0, no memory line; (N1) HELD; (R82) NOT YET DECIDABLE.',
    'b477': 'launched detached; the act closed RUNNING with pid and log named.',
    'b481': "the (c') validation job ABSENT; the bar CAPABILITY; ZERO of four sites disagree.",
    'b483': 'RUN COMPLETE at 2337 s; (F1) FIRES, (F2) THRESHOLD-DEPENDENT, (F3) NOT MET, '
            '(N1) REFUTED, (N2) HELD-or-REFUTED by threshold, (N3) REFUTED.',
    'b484': '(R92) executed, +14/-1 with ZERO lines absent; 7 acts cite trunc_bound and ONE '
            'predicates it; verdict SEPARATE OBJECTS.',
    'b485': 'both manifests verified; 19675356 = v1.0.1, 21432399 = v1.1.0; the gate DISCHARGED '
            'on the current deposit state with SEVEN findings filed.',
    'b482': '24 cells: SAME OBJECT 0, TOUCHES 10, APART 14; and the b479 halt proved.',
    'b479': 'TOUCHES C2 and C7; APART C1, C3, C4, C5, C6; (N1) HELD IN PART, (N2) HELD, (N3) HELD.',
}
# ### ### **THE SIX CLAUSES, EACH WITH THE ACT IT IS CITED FROM.**
DIGEST = [
    ('the six sites reduce to conditions on the test function, on the data of the representation, '
     'and on the instrument`s truncation, with (i) and (ii) the same object as K8',
     'b478', False),
    ('the class boundary at `a = sqrt 2`, reached by two routes', 'b110', True),
    ('zeta23`s explicit formula contains b321`s identity, and the grade is DERIVES, CONDITIONAL on '
     'a profile that has not run', 'b468r, b470, b480', False),
    ('the compression register RAN and takes NO GRADE; its blocker is measured as the places-side '
     'quadrature bound, filed as `W-ORD-QUADRATURE-BOUND`', 'b483, b484', False),
    ('the circulation gate is DISCHARGED on the current deposit state, with the authority`s own '
     'five findings standing', 'b485', False),
    ('the eight unanchored sentences, under `E-2026-09-22-1`', 'b469 (from b464)', True),
]


def main():
    SV = json.loads(read(os.path.join(D, 'b486_survey.json')))
    span = json.loads(read(os.path.join(D, 'b486_span.json')) or '{}')

    rec('=' * 108)
    rec('COMPONENT 1 -- THE SPAN, ACT BY ACT, IN FILING ORDER.')
    rec('=' * 108)
    rec('    ### the trail`s own filing order after the b474 fold. ### **ELEVEN ACTS.**')
    rec('    ### ### **BOTH SPAN READINGS, PER (R96):** by FILING ### **%d** ### ; the tool, by'
        % SV['count'])
    rec('    ### NUMBER order, reads ### **%s** ### -- and ### **THE TOOL IS NOT EDITED.**'
        % span.get('current_span', '?'))
    rec('')
    for i, a in enumerate(SV['filed'], 1):
        rec('  ### **%2d. %s** -- %s' % (i, a, HEAD.get(a, '')))
        rec('        %s' % CARRY.get(a, ''))
        v = next((x for x in SV['acts'] if x['act'] == a), None)
        if v and v['verdicts']:
            rec('        scored, from its own bank : %s' % ' ; '.join(v['verdicts'])[:120])
        elif v:
            rec('        scored, from its own bank : ### **NONE REGISTERED**')
    rec('')
    rec('    ### ### **A FOLD DECIDES NOTHING NEW.** ### Every line above is quoted from the act`s')
    rec('    ### own closing bank; ### **NO VERDICT IS RE-SCORED AND NONE IS INVENTED.**')

    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- THE (R31) DIGEST BLOCK. ### ONE DATED BLOCK, 2026-09-22.')
    rec('=' * 108)
    rec('')
    rec('  ### ### **THE CLAUSE`S COORDINATES, AS THE RECORD HOLDS THEM AT b485.**')
    rec('  ### Each line names the act it is cited from. ### **NOTHING HERE THAT A CITED ACT DOES')
    rec('  ### NOT SAY**, checked needle by needle over every banked file before the block was')
    rec('  ### written.')
    rec('')
    for k, (text, cite, pre) in enumerate(DIGEST, 1):
        mark = ' ### **[CITED FROM OUTSIDE THE SPAN]**' if pre else ''
        rec('    ### **(%d)** %s' % (k, text))
        rec('          --- cited from ### **%s**%s' % (cite, mark))
        rec('')
    rec('  ### ### **TWO OF THE SIX REST ONLY ON ACTS OLDER THAN THIS SPAN** -- clause (2) at b110')
    rec('  ### and clause (6) at b469, whose own source is `b464_the_eight_and_the_parameters.txt`.')
    rec('  ### **A FOLD`S DIGEST MAY CITE AN ACT OLDER THAN ITS SPAN, AND THIS ONE SAYS WHICH.**')
    rec('')
    rec('  ### ### **AND THE CHECK`S OWN LIMITS ARE PRINTED.** ### Five needles discriminate --')
    rec('  ### `K8` (21 acts), `sqrt 2` (61), `W-ORD-QUADRATURE-BOUND` (4), `E-2026-09-22-1` (5),')
    rec('  ### `unanchored` (3). ### Five are permissive -- `sites`, `conditional`, `no grade`,')
    rec('  ### `DISCHARGED`, `five` -- matching ### **85 TO 264 ACTS EACH.**')
    rec('  ### ### **A FILTER THAT KEEPS MOST OF THE CORPUS PROVES NOTHING**, so the block rests on')
    rec('  ### the discriminating needles and both yields are on the record.')

    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- THE TWO LEDGER TABLES.')
    rec('=' * 108)
    rec('')
    rec('  ### ### **THE NAVIGATOR`S -- RULINGS RATIFIED IN THE SPAN`S OWN BANKED FERRIES : %d.**'
        % len(SV['rulings']))
    rec('    %-7s %-9s %s' % ('ruling', 'banked at', 'what it rules'))
    rec('    ' + '-' * 96)
    SHORT = {
        'R84': 'the h2 lane is open as active research',
        'R85': 'a face names each tool`s write pattern, not each file',
        'R86': 'the numerical instrument lane opens at b476`s price',
        'R87': 'the b476 registration is amended in ORIENTATION: signature on -G',
        'R89': 'the standing order is amended: a disk-reading act may open',
        'R90': 'the circulation gate`s trigger is STRUCK and replaced',
        'R91': 'a face`s (W) block may carry its act`s own STEM glob',
        'R92': 'the one live currency claim b481 found is repaired as CURRENCY',
        'R93': "(R92)`s addressee is b484, not b479 or b482",
        'R94': 'the two manifests enter the record by the AUTHOR`S fetch',
        'R95': 'a metadata edit on Zenodo is not a re-issue under (R66)',
        'R96': 'b479 is re-issued under its own number; the fold counts BY FILING',
    }
    for r, a, _ in SV['rulings']:
        rec('    %-7s %-9s %s' % (r, a, SHORT.get(r, '(see the banked ferry)')))
    rec('    %-7s %-9s %s' % ('R88', 'b477', 'b477 STANDS; the flagged word is [procedural] by '
                              'ruling'))
    rec('    ### ### **(R88) IS NAMED SEPARATELY BECAUSE IT IS NOT IN A FERRY FILE** -- it was')
    rec('    ### banked as `b477_r88_standing_order.txt`, and a count over ferries alone would have')
    rec('    ### dropped it silently. ### **THIRTEEN RULINGS IN THE SPAN, NOT TWELVE.**')
    rec('')
    rec('  ### ### **THE SEAT`S -- ACTS WHOSE OWN CLOSING RECORDS A DEFECT OF THEIR OWN : %d.**'
        % len(SV['seat']))
    rec('    %-7s %s' % ('act', 'what its closing records'))
    rec('    ' + '-' * 96)
    SEATSHORT = {
        'b480': 'a batch FOR block stamps ONE instant on every module line -- the durations of '
                'b475`s run are unrecoverable from its log',
        'b481': 'two files the sealed face`s (W) block did not cover; the arm was NOT weakened',
        'b483': "(N2)`s predicate read backwards; and two word anchors eaten as backspace bytes, "
                'leaving an arm unable to fire',
        'b484': 'the census found ITSELF -- a quotation matches the rule that condemns what it '
                'quotes',
        'b485': 'an index-query gate fired on an arm`s NAME, then on the explanation; the desk '
                'tool wrote its row then crashed; an arm fired on the word "deposit"',
        'b482': '`G-NO-LEAN-RUN` read live git inside its predicate, so it could not fail',
        'b479': 'a `def` and a `theorem` do not mean the same by `:=`; and step zero`s pins '
                'failed once on the weather, both runs banked',
    }
    for a, _ in SV['seat']:
        rec('    %-7s %s' % (a, SEATSHORT.get(a, '')))
    rec('')
    rec('    ### ### **AND ONE ENTRY THAT IS NOT A DEFECT OF ANY ACT:** ### the ### **b479 CLOSING')
    rec('    ### REACHED THE NAVIGATOR TRUNCATED.** ### That is a DELIVERY failure between the seat')
    rec('    ### and the reader, not a fault in the act: ### **ITS BANK IS WHOLE ON DISK** at')
    rec('    ### `data/b479_closing.txt`, and its trail record is whole in `OPEN_TRAILS.md`.')
    rec('    ### **A MESSAGE THAT DID NOT ARRIVE IS NOT A RECORD THAT WAS NOT MADE**, and the')
    rec('    ### distinction is worth a row of its own.')
    rec('')
    rec('  ### ### **AND ONE FINDING THIS FOLD MAKES ABOUT AN ACT IT FOLDS.** ### `ERRATA.md`')
    rec('    ### carries ### **`E-2026-09-22-1` TWICE**: filed at ### **b469** ### under (R77), and')
    rec('    ### appended again at ### **b485** ### by this seat. ### **b485 MINTED AN ID THE LEDGER')
    rec('    ### ALREADY HELD, AND ITS SUITE HAD NO ARM THAT WOULD HAVE LOOKED.**')
    rec('    ### ### **THE FOLD REPORTS IT AND DOES NOT RENUMBER IT** -- ERRATA is append-only and')
    rec('    ### its ids are cited elsewhere, so a renumber is a ruling`s business. ### ROUTED.')

    io.open(os.path.join(D, 'b486_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    io.open(os.path.join(D, 'b486_the_fold.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(span=SV['count'], tool=span.get('current_span'),
                   digest=[[d[0][:80], d[1], d[2]] for d in DIGEST],
                   rulings=len(SV['rulings']) + 1, seat=len(SV['seat'])),
              io.open(os.path.join(D, 'b486_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
