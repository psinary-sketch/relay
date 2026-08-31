# -*- coding: utf-8 -*-
"""b269_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE M-2 STATEMENT (b269)"
PRIOR_MARK = u"(b268)"

NEW = (
    u"*** ### ### **M-2 IS NOT STATED. ### VERDICT: (HALT-WITH-DOSSIER), AND THE DOSSIER IS ON "
    u"THE AUTHOR'S DESK.** ### `RULE M2-ORDER: A1 then A2`; A1 closed at b268, and A2 does not "
    u"close. ### **M-2 REMAINS ### SPECIFIED-NOT-STATED ### . ### NOTHING WAS CONSTRUCTED.** *** "
    u"### ### **R1 -- TRANSPORT. ### THE ANSWER IS ASYMMETRIC, AND THAT ASYMMETRY IS THIS ACT'S "
    u"ONE ADDITION TO THE RECORD.** ### In the direction `S-bar` side -> `V_inv` ### A MAP EXISTS "
    u"AND IT IS THE CORPUS'S OWN ### : b10 states ### **\u201cS_quot = orthoprojection onto "
    u"V_inv\u201d** ### , and writes the quantity as an AMBIENT trace, ### **\u201cT_quot(k) = "
    u"|Tr(U^k S_quot)|\u201d**. ### ### **SO A MAP IS NOT MISSING THERE. ### WHAT IS BLOCKED IS "
    u"NOT THE MAP BUT THE STRUCTURE IT WOULD HAVE TO CARRY** -- b10: *the Fourier half does not "
    u"descend* -- and b227: *on V_inv the transform does not descend, so E_1 does not exist "
    u"there*. ### ### **\u201cBLOCKED\u201d DOES NOT MEAN \u201cNO MAP\u201d; IT MEANS THE MAP "
    u"EXISTS AND LOSES THE SECTOR THAT DEFINES THE UNIT. ### THE RECORD HAS BEEN CARRYING BOTH "
    u"SENSES AS ONE, AND THEY ARE NOW SEPARATED.** *** "
    u"### **IN THE OTHER DIRECTION (`V_inv` -> `S-bar`/`E_1`) THE ANSWER IS (ABSENT) -- AND IT IS "
    u"### b228's ### , NOT THIS ACT'S GREP.** ### b228's READ 1 asked exactly this and answered "
    u"at content: ### **\u201cABSENT. Searched at content \u2026 THE ONLY SENTENCES CONNECTING "
    u"V_inv AND Son ARE b10's OWN \u2026 NO OWNER STATES AN ACTION. b10 STATES THE OBSTRUCTION "
    u"AND CALLS IT INFORMATIVE.\u201d** ### b237 says the same of the same thing. ### This act "
    u"corroborates at a stated scope -- 1282 files, needles drawn from the OBJECTS not from the "
    u"sentence naming the absence -- and says plainly that ### **A GREP OVER ONE DIRECTORY IS NOT "
    u"A PROOF OF CORPUS-WIDE ABSENCE.** ### And one near-miss is recorded: b230's *\u201c(3) THE "
    u"SPACE FACE -- (ABSENT)\u201d* is an absence in the ### ENGINE STATEMENT ### , not of the "
    u"transport, and would have been easy to over-read as a second owner-stated absence. *** "
    u"### ### **R2 -- RE-DERIVATION ON `S-bar_v`. ### HALT, AND THE MISSING CHOICE IS NAMED: ### "
    u"act 9's QUANTITY IS A FIXED-ORBIT COUNT, DEFINED RELATIVE TO `x ~ px`, AND THAT RELATION IS "
    u"PART OF `V_inv`'s DEFINITION. ### `S-bar_v` CARRIES NO SUCH RELATION IN THE RECORD.** ### To "
    u"re-derive the count there one must first PUT an orbit structure on `S-bar_v` -- ### **A "
    u"CHOICE, NOT IN THE RECORD, AND CHOOSING IT IS A RULING AND NOT A CALCULATION.** ### R2 "
    u"halts and offers no substitute (b250's standard). *** "
    u"### ### **R3 -- THE STATE ROUTE. ### REFUTED, AND DERIVED RATHER THAN ARGUED. ### THIS IS "
    u"THE ONE ROUTE THE ACT CLOSES.** ### The operators the corpus states on `S-bar_v` are `Pi` "
    u"and `M`, and b227 records the state on them is ### **1** ### because `u` lies in `E_1`. "
    u"### But `Theta_q`'s terms at `k <= n-1` are `p^{-k/2}(p^n - p^k)/(p^n - 1)`, ### **STRICTLY "
    u"BETWEEN 0 AND 1 AND VARYING WITH `k`.** ### ### **A CONSTANT 1 DOES NOT REDUCE TO A FAMILY "
    u"OF VALUES STRICTLY BELOW 1. ### (SPEC-2) FAILS FOR EVERY OPERATOR THE CORPUS STATES ON "
    u"`S-bar_v`.** *** "
    u"### **THE DOSSIER: FOUR CANDIDATES, UNRANKED AND UNADOPTED.** ### **C1 THE AMBIENT "
    u"PAIRING** -- wants a RULING; lowest cost; ### **RISK: b227 refused numbers of exactly this "
    u"shape as the double-name species, and the ruling would have to say why this one is not "
    u"that.** ### **C2 EXTEND THE PROJECTION TO AN ACTION** -- wants a RESULT (what `S_quot` does "
    u"to `E_1`); medium; ### **b268's A1 does not transfer without it.** ### **C3 PUT AN ORBIT "
    u"STRUCTURE ON `S-bar_v`** -- wants BOTH; highest; ### **the only candidate that would give a "
    u"number defined AT `k = n`, which is what (SPEC-1) needs -- and b267's TEST 1 means it would "
    u"be a DIFFERENT OBJECT, not a re-indexing.** ### **C4 CHANGE THE UNIT** -- wants a RULING; "
    u"### **re-opens A1 and discards a result just paid.** ### ### **THEY DIFFER IN KIND, NOT "
    u"ONLY IN COST: WHETHER THE CAMPAIGN SPENDS A RULING OR A RESULT NEXT IS THE DECISION, AND "
    u"THIS SEAT DOES NOT RULE IT.** *** "
    u"### **NOTHING WAS CONSTRUCTED, AND THE TEMPTATION WAS NAMED BEFORE IT COULD BE TAKEN:** the "
    u"registration fixed at (B) that the arithmetically available ambient pairing "
    u"`<U^k S_quot u_v, u_v>` would be a ### DOSSIER CANDIDATE AND NOT A RESULT ### , and ### **NO "
    u"NUMBER WAS COMPUTED FOR IT.** ### b227's own refusal is the precedent. *** "
    u"### **NO SHADOW WAS BUILT, AND THE FERRY'S CLAUSE WAS CONDITIONAL.** ### The condition "
    u"fails: both spaces are defined through a Fourier transform on `Z/N`, and the mismatch IS "
    u"that transform's non-descent. ### **A TOY MODEL WOULD HAVE COMPILED CLEANLY AND SETTLED "
    u"NOTHING, IN A FILE WHOSE HEADER NAMED THE REAL SPACES -- THE DOUBLE-NAME SPECIES IN LEAN.** "
    u"### **0 `.lean` FILES MOVED, CHECKED NOT ASSUMED.** *** "
    u"### **b267 NOW CARRIES TWO ADDENDA, BOTH LEAVING IT BYTE-IDENTICAL:** the author's "
    u"`RULE M2-ORDER` (filed with b268), and ### **TEST 2's (PARTIAL) NOTED AS SUPPLIED BY b268** "
    u"(filed here). ### **NEITHER IS AN EDIT AND NEITHER IS AN ERRATUM -- b267 WAS RIGHT WHEN IT "
    u"WROTE (PARTIAL), AND HAS BEEN SUPERSEDED BY WORK RATHER THAN CORRECTED.** *** "
    u"### **AND A DEFECT WORTH THE RECORD: F-QUOTE FIRED ON A NEEDLE THIS SEAT HAS NOW MIS-TYPED "
    u"TWICE** -- `THEY EXCLUDE` where b263's bank says ### **`THESE EXCLUDE`** ### , and "
    u"### **b263's OWN GATE FILE CARRIES A COMMENT RECORDING THAT EXACT SLIP.** ### Caught before "
    u"the bank. ### Gates 10/10, 11 check bodies tokenized with 0 offending (b268's fix, "
    u"standing); term scan CLEAN; seal `7a914743` INTACT at the close. *** "
    u"### ### **WHAT THE AUTHOR'S RULING WOULD UNLOCK: ### C1 OR C4 WOULD LET THE CAMPAIGN "
    u"PROCEED IMMEDIATELY ON A RULING ALONE; C2 WOULD PUT A NARROW RESULT IN FRONT OF IT; C3 "
    u"WOULD OPEN NEW MATHEMATICS AND IS THE ONLY ONE THAT REACHES (SPEC-1)'s `k = n`. ### UNTIL "
    u"ONE IS RULED, M-2 HAS THREE NAMED DEMANDS AND NO ROUTE.** *** "
    u"### **M-2 IS OWED. ### ITEM 1 OF THE SEAM'S DEBT IS STILL NOT PAID -- b267 LOCATED, b268 "
    u"PAID A PREREQUISITE, b269 RESOLVED THE OBSTRUCTION AND CLOSED ONE ROUTE, AND NONE OF THAT "
    u"IS M-2. ### NO PRIOR ACT RE-VERDICTED. ### NO OWNER INSTRUMENT OR OWNING BANK EDITED. ### "
    u"b259's BANK REMAINS UNTRACKED AS b259 RULED. ### NOTHING ABOUT h2 BEYOND THE REGISTER "
    u"SENTENCE EXACT. ### NOTHING DEPOSITS. LOCKS LAST.**"
)


def main():
    src = io.open(HANDOFF, encoding='utf-8').read()
    lines = src.split(u"\n")
    lead = lines[2]
    assert lead.startswith(PREFIX)
    tail = lead[len(PREFIX):]
    cut = tail.find(SEP)
    assert cut > 0
    old_title, rest = tail[:cut], tail[cut + len(SEP):]
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b268: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b268)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"M-2 IS NOT STATED",
                 u"HALT-WITH-DOSSIER",
                 u"S_quot = orthoprojection onto",
                 u"IT MEANS THE MAP EXISTS AND LOSES THE SECTOR",
                 u"NO OWNER STATES AN ACTION",
                 u"CHOOSING IT IS A RULING AND NOT A CALCULATION",
                 u"(SPEC-2) FAILS FOR EVERY OPERATOR",
                 u"THEY DIFFER IN KIND",
                 u"NO NUMBER WAS COMPUTED FOR IT",
                 u"0 `.lean` FILES MOVED, CHECKED NOT ASSUMED",
                 u"NEITHER IS AN EDIT AND NEITHER IS AN ERRATUM",
                 u"MIS-TYPED TWICE",
                 u"WHAT THE AUTHOR'S RULING WOULD UNLOCK",
                 u"M-2 IS OWED",
                 u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
    for kept in (u"b226's OWED STEP IS ### PAID ###",
                 u"THE AGGREGATION'S TERM IS LOCATED",
                 u"THE J-ARC IS IN THE FINDINGS DOCUMENT WHOLE",
                 u"M-2's ADDRESS IS DERIVED",
                 u"STATES GRADES, CONFERS NONE"):
        assert kept in new_lead, "### prior headline lost in demotion: %r" % kept
    lines[2] = new_lead
    out = u"\n".join(lines)
    assert out.split(u"\n")[:2] == src.split(u"\n")[:2]
    assert out.split(u"\n")[3:] == src.split(u"\n")[3:]
    io.open(HANDOFF, 'w', encoding='utf-8', newline='\n').write(out)
    back = io.open(HANDOFF, encoding='utf-8').read().split(u"\n")[2]
    ok = (back == new_lead)
    sys.stdout.write("  prior title : %s\n" % old_title.encode('ascii', 'replace').decode())
    sys.stdout.write("  new title   : %s\n" % NEW_TITLE)
    sys.stdout.write("  lead length : %d -> %d\n" % (len(lead), len(new_lead)))
    sys.stdout.write("  prior kept  : %s\n" % ("YES" if rest in back else "NO"))
    sys.stdout.write("  read-back   : %s\n" % ("YES" if ok else "NO"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
