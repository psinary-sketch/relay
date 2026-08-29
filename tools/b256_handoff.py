# -*- coding: utf-8 -*-
"""b256_handoff.py -- bring THE HANDOFF current, by DEMOTION and not by rewrite."""
import io
import sys

HANDOFF = r"D:\relay\HANDOFF.md"
PREFIX = u"**Minted 2026-08-23 at the one-sign act (b117); brought current at "
DASH = u"\u2014"
SEP = u" %s " % DASH
NEW_TITLE = u"THE CONTRIBUTION MAP (b256)"
PRIOR_MARK = u"(b255)"

NEW = (
    u"*** ### ### **THE PATENT SESSION'S ENTRY POINT IS ONE DOCUMENT: "
    u"`PLACE-papers/phase1.5/method/CONTRIBUTION_MAP_2026-08.md`.** ### **CLASS LINE: TIER N * "
    u"PRIVATE * PATENT-SESSION INPUT * STATES GRADES, CONFERS NONE.** ### Eighteen rows, each "
    u"carrying the grade its owning act ALREADY holds, its owner, its AIM-if-results-hold, its "
    u"`h2`-dependency, the filing it touches, and its figure candidates. ### **NO GRADE MOVED.** "
    u"### Open items enter OPEN with owners. *** "
    u"### **h2-DEPENDENCY: 13 NO, 5 YES (adjacent). ### EVERY PATENT-FACING ROW IS `NO`** -- and "
    u"that was verified by reading the claim-backing table FIRST: its ten rows are QEC / "
    u"Fano-Steane / Epstein-zero / spinor-leg / cross-exclusion terminals and ### **NOT ONE TOUCHES "
    u"THE RH IDENTITY.** ### **THE FIVE `YES` ROWS ARE MARKED *ADJACENT*: THEY ARE THE ROWS `h2` "
    u"WOULD BEAR ON IF IT MOVED, NOT ROWS THAT ASSUME IT.** ### A blanket sentence would have "
    u"hidden that distinction; a column shows it. *** "
    u"### **THE FOLD-FORWARD LEDGER b234-b255: TWENTY-TWO ACTS, TWENTY-TWO REPORTS, COUNT "
    u"RECONCILED, AND EVERY OBSTACLE *QUOTED* FROM ITS OWNING ACT** -- the fold rules forbid "
    u"paraphrase. ### The arc's own shape, stated: ### **SEVEN ACTS OF READS AND RULINGS "
    u"(b234-b240), THEN FIFTEEN OF BENCH AND DERIVATION (b241-b255), OF WHICH EXACTLY *ONE* "
    u"PRODUCED A THEOREM (b250) AND FOUR PRODUCED HALTS** (b247's clause (i), b250's S3(a), b253's "
    u"R-label, b255's refused reach). *** "
    u"### **THE COUNTS WERE RE-COUNTED FROM THE FILESYSTEM, NOT QUOTED: 44 BUILT** (11+13+7+6+4+3 "
    u"across the six per-filing directories) ### **AND `REVIEW_SET_2026-08` = 31 PRIORITY-A. ### "
    u"BOTH MATCH THE SESSION HEADER EXACTLY.** ### And the number that looks like a divergence and "
    u"is not: a bare `find` returns **82 files / 51 unique basenames**, because the review set and "
    u"the seven top-level files are ### **STAGING COPIES** ### of figures that also live in their "
    u"per-filing directories. ### **44 IS THE BUILT COUNT; 82 IS THE FILE COUNT; SAYING SO IS THE "
    u"WHOLE OF IT.** ### The three walls verified at source in their own batch records; the six "
    u"batch records all present. *** "
    u"### ### **THE ONE ITEM THIS ACT COULD NOT DELIVER, AT FULL PROMINENCE.** ### The ferry "
    u"directs that **SIGNEDNESS (S\u00b7I\u00b7D\u00b7E+S)** be *specified as drafted in the "
    u"conversation layer 2026-08-29 and quoted*. ### **THAT DRAFT IS NOT IN THIS SEAT'S REACH AND "
    u"NOT IN THE CORPUS: a search across `relay/` and ALL of `PLACE-papers/` returns ZERO "
    u"OCCURRENCES of the name.** ### **IT IS RECORDED AS A NAMED SLOT WITH ITS OWNER AND ROUTE AND "
    u"THE QUOTATION MARKED *OWED*. ### IT IS NOT PARAPHRASED AND IT IS NOT INVENTED.** ### The "
    u"likeliest reading is that the draft lives in the ### **AUTHOR'S** ### conversation layer "
    u"rather than this seat's -- in which case ### **THE SWEEP ACT NEEDS IT SUPPLIED, AND THAT IS "
    u"THE REQUEST THE ROW CARRIES FORWARD.** *** "
    u"### **AND A LIVE b148 CONDITION FOUND IN THE SHARED WORKTREE, WHICH IS NOT THIS ACT'S DOING "
    u"BUT IS THIS SEAT'S TO SAY.** ### A gate whose first criterion was wrong exposed it: ### "
    u"**SEVEN PATENT-SEAT FIGURE DIRECTORIES ARE SITTING *UNTRACKED* IN THE SHARED CLONE RIGHT NOW "
    u"-- DATED 2026-08-24, FIVE DAYS BEFORE THIS ACT, HOLDING THE 44 BUILT FIGURES AND THE SIX "
    u"BATCH RECORDS.** ### At b148 this seat ran `git add -A` and swept in EIGHT such files one act "
    u"after the deconfliction was ratified; ### **THE COUNT IS LARGER NOW.** ### This act created "
    u"none of them (verified by mtime) and staged none of them (`place_add.py`, and nowhere else). "
    u"### **REPORTED, NOT RESOLVED -- whether that work should be committed is the patent seat's "
    u"call and the author's, and the one thing this seat owes is to say the condition is present "
    u"rather than let the next `git add -A` discover it.** *** "
    u"### **ANNEX A -- FIGURE CANDIDATES**, every one marked ### **NEW-FILING or CONTINUATION and "
    u"NONE Priority-A**: the sector ladder, quarter-density, the check-harness architecture, the "
    u"surjectivity certificate, the banked-meanings engine, the balance/sawtooth profiles, the "
    u"SIGNEDNESS certificate schematic. ### **ANNEX B -- THE METHODOLOGY-EXTRACTION ANNEX, WHICH IS "
    u"THE SWEEP'S *INPUT* AND NOT THE SWEEP**: the banked-meanings engine, the import ledger, the "
    u"harness lore family, the discriminator protocol, the face-off protocol, the decision-card "
    u"format -- each with owning acts and route (TECHNE-Core, private). *** "
    u"### **J1 IS RECORDED PARKED-BY-AUTHOR (save); J2 IS AN UNPROMOTED CANDIDATE. ### NEITHER IS "
    u"PROMOTED BY APPEARING ON THE MAP.** *** "
    u"### **A CHART-READY CSV OF b255's SIXTEEN-CELL BALANCE PROFILE IS EMBEDDED**, instituting the "
    u"standing practice this paste minted: ### **EVERY PROFILE ACT'S BANK ENDS WITH A CHART-READY "
    u"CSV BLOCK OF ALL COLUMNS.** ### Applied retrospectively to b255; the next profile act "
    u"inherits it without being told again. *** "
    u"Gates ### **12 of 12 CLEAN** (second run; the first failure was a gate criterion, and fixing "
    u"it is what surfaced the b148 condition). ### Term scan CLEAN. ### **THE PLACE-papers HOOK WAS "
    u"EXERCISED AND REPORTED: CLEAN, 0 FOREIGN HITS.** ### **THE MIRROR WAS REBUILT AND VERIFIED "
    u"CLEAN ON ALL THREE CLAUSES** -- 40 files, 40 rows parsed, 0 md5/byte mismatches, declared HEAD "
    u"`2bcdff5` against `ls-remote`, roster and archive agreeing name for name. ### **AND ONE THING "
    u"THE MIRROR DOES *NOT* CARRY, SAID RATHER THAN LEFT: THE MAP IS NOT IN THE ROSTER, BECAUSE IT "
    u"IS TIER N PRIVATE AND THE MIRROR IS THE *REVIEWER* MIRROR. ### WHETHER IT BELONGS THERE IS "
    u"NOT THIS SEAT'S TO SETTLE.** *** "
    u"### **THE FORK AT THIS STOP.** ### **(1) THE PATENT SESSION -- it now reads ONE document, and "
    u"it slots here on your word.** ### **(2) THE METHODOLOGY-EXTRACTION SWEEP (TECHNE-Core), THE "
    u"NEXT RESEARCH ACT -- and it needs the SIGNEDNESS draft supplied.** ### **(3) J1, PARKED "
    u"BEHIND IT.** ### **(4) M-2's finite address and the aggregation; M-3; M-5; `W-ORD-CN-LAW`.** "
    u"*** ### **THE MAP STATES GRADES AND CONFERS NONE. ### M-2, M-3, M-4 AND M-5 STAND OPEN AND "
    u"THIS ACT CLOSED NONE. ### THE THIRTY-SEVENTH SEAM'S DEBT STANDS, UNPAID AND UNTOUCHED. ### "
    u"NOTHING ABOUT h2 BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**"
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
    assert old_title.endswith(PRIOR_MARK), "### prior title is not b255: %r" % old_title
    assert NEW_TITLE not in lead
    demoted = u" *(prior: b255)* %s and at %s%s%s" % (DASH, old_title, SEP, rest)
    new_lead = PREFIX + NEW_TITLE + SEP + NEW + demoted
    assert rest in new_lead and new_lead.endswith(rest)
    for must in (u"STATES GRADES, CONFERS NONE", u"NO GRADE MOVED",
                 u"EVERY PATENT-FACING ROW IS `NO`", u"TWENTY-TWO ACTS",
                 u"44 BUILT", u"QUOTATION MARKED *OWED*",
                 u"IT IS NOT PARAPHRASED AND IT IS NOT INVENTED",
                 u"LIVE b148 CONDITION", u"REPORTED, NOT RESOLVED",
                 u"PARKED-BY-AUTHOR", u"0 FOREIGN HITS",
                 u"CLEAN ON ALL THREE CLAUSES", u"NOTHING DEPOSITS"):
        assert must in new_lead, "### headline assertion missing: %r" % must
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
