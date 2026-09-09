# -*- coding: utf-8 -*-
"""b377_evidence.py -- COMPONENTS 1, 2 AND 4, PLUS THE AMENDMENT'S SECOND CLAUSE.

### ### **COMPONENT 1 -- THE AUTHOR'S ROLE CLAUSE, BANKED VERBATIM AS EVIDENCE AND NOT AS A RULING.**
### What it bears on is ### **STATED, NOT INFERRED:** ### it speaks to the ROLE axis and not to the
### APPARATUS axis. ### **A CLAUSE THAT BEARS ON ONE AXIS DOES NOT RULE A QUESTION THAT SPANS TWO.**

### ### **COMPONENT 2 -- `b376`'S FIVE OPTIONS, QUOTED WHOLE** ### -- reproduced from `b376`'s bank
### line for line, located by content, ### **SO THE AUTHOR RULES FROM THE TEXT AND NOT FROM A
### ### SUMMARY.** ### One bearing line is added per option: whether the role clause bears on it, and
### how. ### **NO BEARING LINE RECOMMENDS.**

### ### **COMPONENT 4 -- TWO FILINGS, NEITHER OPENED.**
### ### **AND THE AMENDMENT'S SECOND CLAUSE:** ### the banked column-(d) figure is recorded as a
### ### **FLOOR** ### against a wider question this act NAMES and ### **DOES NOT RE-MEASURE.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FERRY = os.path.join(D, 'b377_ferry_2026-09-08.txt')
B376 = os.path.join(D, 'b376_the_two_axis_read.txt')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


# ### **THE FIVE OPTIONS ARE LOCATED BY THEIR OWN OPENING LINE AND COPIED THROUGH TO THE NEXT ONE.**
# ### ### **NO OPTION IS SUMMARISED, TRUNCATED OR PARAPHRASED** -- the order says QUOTED WHOLE.
OPTION_HINTS = [
    ('OPTION 1', '### **OPTION 1 -- ONE CLASS, RULED ON AXIS B ALONE.**'),
    ('OPTION 2', '### **OPTION 2 -- ONE CLASS, RULED ON AXIS A ALONE.**'),
    ('OPTION 3', '### **OPTION 3 -- ONE CLASS, RULED ON BOTH AXES CONJOINED**'),
    ('OPTION 4', '### **OPTION 4 -- TWO MARKS RATHER THAN ONE CLASS**'),
    ('OPTION 5', '### **OPTION 5 -- RULE NOTHING AND RETIRE THE WORD.**'),
]
END_HINT = ('### ### ### **WHAT THE EVIDENCE DOES NOT SUPPORT, SAID SO THAT THE SILENCE IS NOT READ AS')

# ### **THE BEARING LINES. ### EACH SAYS WHETHER AND HOW THE ROLE CLAUSE BEARS -- AND NOTHING ELSE.**
# ### ### **NONE OF THEM RANKS, PREFERS, RECOMMENDS OR CALLS AN OPTION NATURAL, LIKELY OR CLEANEST.**
# ### A bearing line that did any of those would be a ruling wearing a description's clothes, and
# ### `G-NOPREFER` reads this region.
BEARING = {
    'OPTION 1': (
        "### **THE ROLE CLAUSE BEARS AGAINST THIS OPTION'S SUFFICIENCY, AND SAYS SO IN ITS OWN "
        "WORDS.** The clause states what keystones are FOR -- clarifying results, exploring "
        "ramifications and insights, covering pertinent or interesting material. **A DOCUMENT CAN "
        "CARRY A TRAVERSABLE ROW AND DO NONE OF THAT**, and `b376` found 18 documents carrying the "
        "apparatus whose own text says nothing about their role. This option would admit those 18 "
        "and would not ask the clause's question of any of them. **THAT IS A CONSEQUENCE, NOT A "
        "VERDICT.**"),
    'OPTION 2': (
        "### **THE ROLE CLAUSE IS THIS OPTION'S SUBJECT MATTER.** The clause is a statement about "
        "role, and axis A is the role axis; the clause both widens axis A -- *ramifications and "
        "insights*, *any and all pertinent or interesting materials* -- and warns against a reading "
        "narrowed by the current lane. **AND IT SHARPENS THIS OPTION'S KNOWN COST RATHER THAN "
        "SOFTENING IT:** the 340 documents that say nothing about their role are silent about "
        "exactly the property the clause makes central."),
    'OPTION 3': (
        "### **THE ROLE CLAUSE BEARS ON ONE CONJUNCT AND NOT THE OTHER.** This option joins the role "
        "question to the apparatus question with `and`; the clause speaks to the role conjunct only. "
        "**IT NEITHER SUPPORTS NOR OPPOSES THE CONJUNCTION ITSELF**, and the defect Component 1 of "
        "`b376` found in the corpus's own version of this option -- a failing document is not told "
        "which conjunct it failed -- is untouched by the clause."),
    'OPTION 4': (
        "### **THE ROLE CLAUSE IS COMPATIBLE WITH THIS OPTION AND DOES NOT ARGUE FOR IT.** Two marks "
        "would let the clause govern one column outright while the apparatus governs the other, so "
        "the clause could be applied without being weighed against certification. **BUT THE CLAUSE "
        "SAYS NOTHING ABOUT HOW MANY MARKS A DOCUMENT SHOULD CARRY**, and reading support for this "
        "option out of it would be inferring a structural ruling from a statement of purpose."),
    'OPTION 5': (
        "### **THE ROLE CLAUSE BEARS AGAINST THIS OPTION, AND THIS IS THE ONE PLACE THE CLAUSE "
        "POINTS PLAINLY.** Retiring the word would leave the corpus with two marks and no term for "
        "what the clause describes. **THE CLAUSE IS WRITTEN AS THOUGH `KEYSTONE` NAMES SOMETHING "
        "REAL AND WORTH DOING WELL**, which is evidence that the author is using the word as a live "
        "term. **IT IS STILL EVIDENCE AND NOT A RULING**, and the author may retire a word he has "
        "just used."),
}


def span(path, start_hint, end_hint):
    """### **LOCATED BY CONTENT AT BOTH ENDS AND COPIED THROUGH.** ### Never by line number."""
    a, _ = AF.find(path, start_hint)
    b, _ = AF.find(path, end_hint)
    lines = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    return a, b, lines[a - 1:b - 1]


def main():
    BR = J('b377_branch')
    AX = J('b376_axes')
    TS = J('b376_tests')
    IN375 = J('b375_integration')
    CL375 = J('b375_clusters')
    PR376 = J('b376_prior')

    rec('=' * 100)
    rec('b377 -- COMPONENTS 1, 2 AND 4. ### **THE EVIDENCE, ASSEMBLED AND NOT RULED FROM.**')
    rec('=' * 100)

    # ------------------------------------------------------------------------------- COMPONENT 1
    rec('')
    rec('-' * 100)
    rec("  ### COMPONENT 1 -- THE AUTHOR`S ROLE CLAUSE, BANKED VERBATIM.")
    rec('-' * 100)
    clause = []
    for hint in ('evidence and not as a ruling: "Keystones are for clarifying',
                 'results and as well as for exploring ramifications and',
                 'insights"; and "the keystones should cover any and all',
                 'pertinent or interesting materials, not just having tunnel',
                 'vision in explanatory clarity just because we have been',
                 'relentlessly focused on a particular problem at a particular',
                 'research phase." Author\'s own words, 2026-09-08, ratified by'):
        n, line = AF.find(FERRY, hint)
        clause.append(dict(line=n, text=line.rstrip(chr(10))))
        rec('    `b377_ferry_2026-09-08.txt` line %-3d | %s' % (n, line.strip()))
    rec('')
    rec('    ### ### **THE CLAUSE, READ AS ONE SENTENCE PAIR:**')
    rec('    ###   `Keystones are for clarifying results and as well as for exploring ramifications')
    rec('    ###   and insights`')
    rec('    ###   `the keystones should cover any and all pertinent or interesting materials, not')
    rec('    ###   just having tunnel vision in explanatory clarity just because we have been')
    rec('    ###   relentlessly focused on a particular problem at a particular research phase`')
    rec('')
    rec('    ### **WHAT IT BEARS ON, STATED AND NOT INFERRED:**')
    rec('    ### ### **IT SPEAKS TO THE ROLE AXIS.** ### Every content word in it is about what a')
    rec('    ### keystone is FOR -- clarifying, exploring, covering. ### **NOT ONE WORD OF IT IS ABOUT')
    rec('    ### ### WHETHER A DOCUMENT CARRIES A CORRESPONDENCE TABLE**, which is the apparatus axis.')
    rec('    ### ### **AND IT WIDENS THE ROLE AXIS RATHER THAN NARROWING IT.** ### `b375`s rubric said')
    rec('    ### keystones `synthesize a cluster against other available content`; ### this clause adds')
    rec('    ### ### **RAMIFICATIONS AND INSIGHTS** ### and ### **ANY AND ALL PERTINENT OR INTERESTING')
    rec('    ### ### MATERIALS**, and warns in as many words against ### **TUNNEL VISION IN EXPLANATORY')
    rec('    ### ### CLARITY** ### driven by the current lane.')
    rec('    ### ### ### **A CLAUSE THAT BEARS ON ONE AXIS DOES NOT RULE A QUESTION THAT SPANS TWO**,')
    rec('    ### ### ### and this act does not rule from it.')
    rec('    ### **AND ITS SHARPEST CONSEQUENCE IS A MEASUREMENT THAT ALREADY EXISTS:** ### `b376`')
    rec('    ### found ### **%d DOCUMENTS CARRYING A TRAVERSABLE ROW WHOSE OWN TEXT SAYS NOTHING ABOUT'
        % (AX['quadrants'].get('A-B+', 0) + AX['quadrants'].get('A?B+', 0)))
    rec('    ### ### THEIR ROLE**, and ### **%d OF %d THAT DO NOT SAY WHAT THEY ARE AT ALL.** ### The'
        % (AX['axis_a_tally'].get('A?', 0), len(AX['scored'])))
    rec('    ### clause is a statement about precisely the property that population is silent on.')

    # ------------------------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 -- THE FIVE OPTIONS, QUOTED WHOLE FROM `b376`S BANK.')
    rec('-' * 100)
    rec('  ### ### **REPRODUCED LINE FOR LINE SO THE AUTHOR RULES FROM THE TEXT AND NOT FROM A')
    rec('  ### ### SUMMARY.** ### Each is followed by ONE bearing line, and ### **NO BEARING LINE')
    rec('  ### ### RECOMMENDS, RANKS OR PREFERS.**')
    options = []
    for i, (name, hint) in enumerate(OPTION_HINTS):
        nxt = OPTION_HINTS[i + 1][1] if i + 1 < len(OPTION_HINTS) else END_HINT
        a, b, body = span(B376, hint, nxt)
        body = [x for x in body if x.strip()]
        rec('')
        rec('  ' + '=' * 96)
        rec('  ### **%s** ### -- quoted whole from `b376_the_two_axis_read.txt` lines %d-%d'
            % (name, a, b - 1))
        rec('  ' + '=' * 96)
        for x in body:
            rec('  ' + x)
        rec('')
        rec('  ### **DOES THE ROLE CLAUSE BEAR ON IT, AND HOW:**')
        for seg in _wrap(BEARING[name], 92):
            rec('  ### ' + seg)
        options.append(dict(name=name, start=a, end=b - 1, lines=len(body),
                            text=chr(10).join(body), bearing=BEARING[name]))
    rec('')
    rec('  ### ### **FIVE OPTIONS REPRODUCED WHOLE; FIVE BEARING LINES; ### NONE RECOMMENDED, NONE')
    rec('  ### ### RANKED, AND THE ORDER ABOVE IS `b376`S PRINTING ORDER AND NOT AN ORDER OF MERIT.**')
    rec('  ### ### ### **AND THE RULING REMAINS THE AUTHOR`S.**')

    # ------------------------------------------------------------------------------- COMPONENT 4
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 4, FILING (i) -- THE CENSUS`S DEFINITION-VERSUS-OPERATION DRIFT.')
    rec('-' * 100)
    rec('  ### **FILED AGAINST `phase2/method/THE_KEYSTONE_CENSUS.md`. ### QUOTED, NOT REPAIRED** --')
    rec('  ### repairing it belongs to the ruling, because a census repaired under a definition the')
    rec('  ### author has not chosen would be a fourth authority rather than an orientation.')
    rec('')
    rec('    ### **WHAT IT STATES**, line %d, verbatim:' % PR376['stated']['KEYSTONE']['line'])
    rec('      | %s' % PR376['stated']['KEYSTONE']['text'])
    rec('    ### **WHAT IT SAYS IT APPLIES**, line %d, verbatim:' % PR376['operationalised_line'])
    rec('      | %s' % PR376['operationalised_text'])
    rec('')
    rec('    ### **THE DRIFT, IN FOUR PARTS:**')
    rec('    ###   (1) clause `(i)` is applied through a ### **TYPOGRAPHIC PROXY** ### -- an `Abstract`')
    rec('    ###       heading or an ORCID block -- and not as the judgement it states.')
    rec('    ###   (2) clause `(ii)` is narrowed from ### **A TABLE NAMING TERMINALS** ### to')
    rec('    ###       ### **A HEADING CARRYING THE WORD.**')
    rec('    ###   (3) clause `(iii)` -- the only clause that looks OUTSIDE the document -- is')
    rec('    ###       ### **NOT OPERATIONALISED AT ALL.**')
    rec('    ###   (4) a ### **`6 KB` SIZE FLOOR THE DEFINITION NEVER MENTIONS** ### is applied.')
    rec('    ### **AND THREE DIFFERENT NUMBERS COME OUT OF ONE DOCUMENT:** ### its own detector')
    rec('    ### returned ### **20**; the document publishes ### **%d** ### after removing four by a'
        % len(PR376['census_named']))
    rec('    ### rule from its own SUPPORT row that is on no operational clause; and re-applied at the')
    rec('    ### head by `b376`, its own operation returns ### **%d**.' % len(PR376['operation_returns']))
    rec('    ### ### **THE DOCUMENT IS HONEST ABOUT THE HAND CORRECTION AND RECORDS IT IN ITS OWN')
    rec('    ### ### TEXT.** ### The honesty is on the record; ### **THE DRIFT STILL GOVERNS EVERY')
    rec('    ### ### NUMBER THE CENSUS PRINTED**, and every later act that cited one.')
    rec('    ### ### ### **FILED. ### NOT OPENED. ### NOT REPAIRED. ### AND THE CENSUS`S OWN')
    rec('    ### ### ### DECLARED CLASS IS NOT DISPUTED OR MOVED BY THIS FILING.**')

    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 4, FILING (ii) -- THE CLUSTERS WITH REGISTRY ROWS AND NO KEYSTONE.')
    rec('-' * 100)
    nokey = CL375['subject_clusters_without_keystone']
    rec('  ### **THE FACT, AS `b375` LEFT IT:** ### ### **%d SUBJECT CLUSTERS HAVE REGISTRY ROWS AND'
        % len(nokey))
    rec('  ### ### NO KEYSTONE** -- %s.' % ', '.join('`%s`' % x for x in nokey))
    rec('  ### **RESTATED BESIDE THE ROLE CLAUSE, WHICH IS WHAT MAKES IT A WORK-ORDER AND NOT A')
    rec('  ### ### CURIOSITY:** ### the clause says keystones should cover ### **ANY AND ALL PERTINENT')
    rec('  ### ### OR INTERESTING MATERIALS** ### and warns against ### **TUNNEL VISION IN EXPLANATORY')
    rec('  ### ### CLARITY** ### driven by ### **A PARTICULAR PROBLEM AT A PARTICULAR RESEARCH PHASE.**')
    rec('  ### ### ### **A SUBJECT CLUSTER WITH DOCUMENTS AND NO KEYSTONE IS THAT WARNING, MEASURED.**')
    rec('  ### ### **AND MOST OF THIS WORK SITS OUTSIDE THE CURRENT LANE**, which is why it has not')
    rec('  ### been done and is exactly why the clause names the risk.')
    rec('')
    rec('  ### **THE PRICE, AS FAR AS THE RECORD SUPPORTS ONE, AND NO FURTHER:**')
    rec('  ###   the record supports a price for ### **ONE** ### unit of this work and not for the')
    rec('  ###   whole: ### **a keystone is one document with a correspondence table**, and this act')
    rec('  ###   measured what appending a pinned table to an EXISTING document costs.')
    rec('  ###   ### **IT DOES NOT SUPPORT A PRICE FOR WRITING A KEYSTONE THAT DOES NOT EXIST YET**,')
    rec('  ###   because no act in this record has written one, and ### **A PRICE FROM NO')
    rec('  ###   ### MEASUREMENT IS AN ESTIMATE WEARING A MEASUREMENT`S CLOTHES.**')
    rec('  ###   ### **WHAT THE RECORD DOES BOUND:** ### the %d clusters are named; each has registry'
        % len(nokey))
    rec('  ###   rows; and `b375` listed the documents in each. ### **SO THE INPUT IS ENUMERATED AND')
    rec('  ###   ### THE OUTPUT IS NOT.**')
    rec('  ### ### ### **FILED AS A WORK-ORDER. ### NOT OPENED. ### NO CLUSTER IS ASSIGNED A KEYSTONE')
    rec('  ### ### ### AND NO DOCUMENT IS PROMOTED BY THIS FILING.**')

    # ------------------------------------------------------ THE AMENDMENT'S SECOND CLAUSE: THE FLOOR
    rec('')
    rec('-' * 100)
    rec("  ### THE AMENDMENT`S SECOND CLAUSE -- THE BANKED FIGURE IS A FLOOR.")
    rec('-' * 100)
    dn, dk = IN375['d_nonempty'], IN375['keystones']
    rec('  ### **THE BANKED FIGURE:** ### `b375` column (d) -- what bears on a keystone and is not in')
    rec('  ### it -- is non-empty for ### **%d of %d**.' % (dn, dk))
    rec('  ### **HOW IT WAS TAKEN:** ### against the ### **FINDINGS LAYER ALONE**, which is weighted')
    rec('  ### toward the current lane.')
    rec('  ### ### ### **SO IT IS RECORDED HERE AS A FLOOR AND NOT AS AN ANSWER.**')
    rec('  ### **THE WIDER QUESTION, NAMED AS THE ONE THE RECONCILIATION MUST ASK:** ### what bears on')
    rec('  ### a keystone`s ### **SUBJECT** ### anywhere in the corpus -- other clusters, other')
    rec('  ### kernels, the emerging-programmes ledger, the faces ledger -- and not merely what the')
    rec('  ### findings layer happens to have recorded about it.')
    rec('  ### ### **AND THIS ACT DOES NOT RE-MEASURE IT.** ### The amendment says so in as many words,')
    rec('  ### and ### **A FLOOR RE-MEASURED BADLY WOULD REPLACE A HONEST BOUND WITH A WRONG ONE.**')
    rec('  ### ### ### **WHY THE WIDER FIGURE CAN ONLY BE LARGER:** ### the findings layer is one')
    rec('  ### ### ### source among several, so every source added can only add material that bears.')
    rec('  ### ### ### **`%d of %d` IS THEREFORE A LOWER BOUND ON THE WIDER QUESTION, AND THAT IS THE'
        % (dn, dk))
    rec('  ### ### ### ONLY CLAIM THIS ACT MAKES ABOUT IT.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b377_evidence_notes', LINES)
    io.open(os.path.join(D, 'b377_evidence.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(role_clause=clause, options=options,
                        filing_census=dict(stated_line=PR376['stated']['KEYSTONE']['line'],
                                           operationalised_line=PR376['operationalised_line'],
                                           detector=20, published=len(PR376['census_named']),
                                           reapplied=len(PR376['operation_returns']),
                                           repaired=False, opened=False),
                        filing_clusters=dict(clusters=nokey, count=len(nokey),
                                             priced_unit='one existing document, pinned table appended',
                                             priced_whole=False, opened=False),
                        floor=dict(banked=dn, of=dk, layer='findings layer alone',
                                   remeasured=False,
                                   wider_question='what bears on a keystone subject anywhere in the '
                                                  'corpus, including other clusters, other kernels, '
                                                  'the emerging-programmes ledger and the faces '
                                                  'ledger'),
                        branch_arm1=BR['arm1'], branch_arm2=BR['arm2'],
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


def _wrap(s, n):
    out, cur = [], ''
    for w in s.split():
        if len(cur) + len(w) + 1 > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out


if __name__ == '__main__':
    sys.exit(main())
