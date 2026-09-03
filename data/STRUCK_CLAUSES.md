# STRUCK CLAUSES — the record

**Minted 2026-09-02 (b299), on the author's strike of the title law's property half.**

### **WHAT THIS FILE IS.** A record of clauses the author has **STRUCK** — clauses that were
once operative in this record's own voice and are now **not to be applied anywhere**: not in a
title, not in a document, not in a bank, and not in a gate.

### **WHAT IT IS NOT.** It is **not** a list of things that are false, and it is **not** a
correction to any text that already carries a struck clause. The **append-only law** governs: a
struck clause found in a banked act, in a sealed registration, or in a ledger is **FILED with its
file and line, never corrected in place**. Striking a clause changes what the *next* act may
apply; it does not rewrite the acts that applied it.

### **THE SINGLE SOURCE OF TRUTH.** `tools/ferry_scan.py` reads this file. It is the **input**
and nothing overwrites it — the b183 lesson, where a roster that was both an input and an output
silently dropped a row. Nothing in the command path writes here; the author's strike does, and an
act records it.

### **WHY A `PATTERN:` AND NOT THE SENTENCE.** A struck clause does not travel in the wording it
was struck in. The title law was struck as *"titles name objects and conditions, never claimed
properties"* and it lives in the corpus as *"a title must name its objects and conditions, not
claim an achieved property"* and in a document as *"names its objects and its conditions and
claims no achieved property"*. **A record that matched only the striking wording would have found
none of the three sites that mattered.**

### **THE LIMITS, IN THE FILE'S OWN HEAD SO IT IS NOT TRUSTED BEYOND THEM.**
- **(1) IT MATCHES SHAPES, NOT MEANINGS.** A hit is a string, not a fault. **The ferry that
  strikes a clause quotes it in order to strike it, and that quotation hits.** The check reports;
  the reader rules.
- **(2) A CLAUSE WITH NO `PATTERN:` LINE IS INVISIBLE TO THE CHECK** however carefully it is
  written up here. The prose is for the reader; the patterns are the whole of the enforcement.
- **(3) UNCONFIRMED CANDIDATES ARE NOT LOADED.** The scanner reads `STATUS: STRUCK` entries only
  and prints how many `STATUS: UNCONFIRMED` entries it deliberately skipped. **Promotion is the
  author's word and cannot happen by a tool reading a file.**

---

## THE STRUCK LIST — machine-read

Each entry begins `### S-<n>`. Lines beginning with a keyword and a colon are read by the tool;
everything else on the entry is prose for the reader.

### S-1
STATUS: STRUCK
RULED-BY: the author, by paste, the b299 ferry (2026-09-02) — quoted verbatim: "titles name objects and conditions, never claimed properties" is STRUCK; only the numeral half stands (a numeral appears in a title when the numeral is itself the finding)
SOURCE-LAW: F.2026-07-29, the title law, as `FINDINGS.md` line 62 carries it
CLAUSE: a title must name its objects and conditions, not claim an achieved property
SURVIVES: the numeral half — a numeral appears in a title when the numeral is itself the finding (the numeral-title law, `REGISTRY.md` row 1.5c-16)
PATTERN: names?\s+(its\s+|their\s+)?objects?\s+and\s+(its\s+|their\s+)?conditions?
PATTERN: not\s+claim\s+an\s+achieved\s+property
PATTERN: claims?\s+no\s+achieved\s+property
PATTERN: never\s+claimed\s+propert(y|ies)
PATTERN: claim(s|ing)?\s+an\s+achieved\s+property

**The two halves were one sentence and are now not.** The property half is struck; the numeral
half stands on its own footing and has its own site in the record — `REGISTRY.md` calls it *"the
numeral-title law"* at row `1.5c-16`, separately from the composite title law. **So the strike
narrows a law that already had two named halves; it does not invent the split.**

**THE SITES THAT STILL CARRY IT, FILED AND NOT EDITED** (append-only; reconciling them is the
author's, not the executor's):
- `PLACE-papers/FINDINGS.md` line 62 — the ledger entry `F.2026-07-29` itself.
- `PLACE-papers/REGISTRY.md` rows for `p2-16` (two sites) — retitle records quoting the clause as
  their reason.
- `PLACE-papers/FINDINGS.md` line 1224 — the basecamp-shelf finding, quoting the clause.
- `relay/data/b299_registration_2026-09-02.txt` — **this act's own sealed registration**, which
  fixed the clause as a falsifier (`Q-TITLE`) before the author struck it. **The seal is not
  edited. The conflict is declared in the bank, and the document follows the author's ruling over
  the registration's wording.**

---

### U-1
STATUS: STRUCK
RULED-BY: the author, by paste, the b300 ferry (2026-09-02) — quoted verbatim: "U-1 CONFIRMED STRUCK — a registration does not predict counts of artifacts; it registers expected outcomes and mechanisms, and a predicted count creates pressure to hit it"
SOURCE-LAW: none — this was a practice, not a filed law. It became a candidate at b299 by having been corrected twice, and the author ruled on the candidate.
CLAUSE: an act predicts the count of the objects it will build, and declares a miss when the count differs
SURVIVES: the registration's duty to state expected OUTCOMES and MECHANISMS, which is what it was ever for. **Reporting what an act DID produce, in its closing, is untouched by this strike.**
PATTERN: (?:registers?|predicts?|will\s+build|will\s+produce|will\s+write|expects?\s+to\s+build)\s+(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+(?:gates?|tools?|needles?|fixtures?|terminals?|artifacts?|documents?|modules?|banks?|components?|checks?)
PATTERN: (?:predicted|registered|expected|projected)\s+(?:\w+[\s\-]+){0,3}counts?\b[^0-9A-Za-z]{0,12}(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)
PATTERN: declar\w+\s+(?:a|the)\s+miss\b

**THE REASON THE AUTHOR GAVE, AND IT IS THE WHOLE OF THE STRIKE:** *"a predicted count creates
pressure to hit it."* The record's own evidence is that the pressure is real and that paying it
honestly is not a defence — b298 registered a count, built a different one, and declared the miss
at its own (D1) rather than trimming controls to reach the number. **THAT ACT DID THE RIGHT THING
WITH A CLAUSE THAT SHOULD NOT HAVE BEEN THERE.**

**THE TWO CORRECTIONS POINTED OPPOSITE WAYS AND THE AUTHOR RESOLVED THEM, WHICH IS WHY THIS IS A
RULING AND NOT A SEAT DECISION.** b298 kept the practice and paid for it; b299's registration
wrote that *"A COUNT THE ACT HAS NO REASON TO FIX IN ADVANCE IS A NUMBER INVENTED TO BE
PREDICTED"* and declined to predict one. No act had reconciled them.

**THE SITE, FOUND BY THE CHECK AND NOT ASSERTED BY THE ENTRY — AND THE SECOND PATTERN EXISTS
BECAUSE THE FIRST ONE MISSED IT.** The first pattern written here matched the numeral BEFORE the
noun (*"registers ten terminals"*). **`b298`'s REGISTRATION WRITES IT THE OTHER WAY ROUND —
`"PREDICTED TERMINAL COUNT: ### 10."` — AND THE SCAN CAME BACK WITH ZERO HITS ACROSS THE WHOLE
CORPUS, WHICH READ EXACTLY LIKE A CLAUSE NOBODY HAD EVER APPLIED.** That is the under-report
direction `ferry_scan.py`'s own header names as the dangerous one, met on this record's second
entry. The second pattern was added and `data/b298_registration_2026-09-02.txt` now returns its
site. **FILED AND NOT EDITED** (append-only); striking a clause changes what the *next* act may
apply.

### U-2
STATUS: STRUCK
RULED-BY: the author, by paste, the b300 ferry (2026-09-02) — quoted verbatim: "U-2 CONFIRMED STRUCK — the phrase asserting a ledger is current may be used only when a check has counted what is missing; otherwise the act states what it wrote and what it did not check"
SOURCE-LAW: none — a closing-sequence habit, corrected repeatedly by the seat before the author ruled.
CLAUSE: a closing sequence asserts that a ledger is current
SURVIVES: **the same phrase after a check that has COUNTED WHAT IS MISSING.** The strike is conditional in the author's own words and the condition is a real check, not a reading.
PATTERN: HANDOFF\s+(?:IS\s+)?CURRENT
PATTERN: (?:FINDINGS|REGISTRY|OPEN_TRAILS|VERIFICATION_LOOM|the\s+ledgers?)\s*(?:\.md)?\s+(?:IS|ARE)\s+CURRENT

**WHAT REPLACES IT, IN THE AUTHOR'S OWN WORDS:** *"the act states what it wrote and what it did
not check."* Two lists, not one adjective.

**THE HABIT THE STRIKE ENDS.** The phrase had been kept and qualified in every act since b293 —
`HANDOFF.md`'s head has read b278 that whole time, and b298 wrote that the arc's handoff *"LIVES
IN THE BANKS AND IN FINDINGS.md, AND THIS ACT SAYS SO RATHER THAN LETTING 'CURRENT' DO SILENT
WORK"*. **A CLAUSE THAT MUST BE ANNOTATED EVERY TIME IT IS USED WAS A CANDIDATE AT b299; IT IS
STRUCK AT b300.**

**THE SITES THAT STILL CARRY IT ARE FILED AND NOT EDITED**: `b285`, `b286`, `b287`, `b291` and
`b292` each close with it, and `HANDOFF.md`'s own head. Reconciling them is the author's.

---

## UNCONFIRMED CANDIDATES — for the author. **NOT LOADED BY THE CHECK. NONE PROMOTED.**

### **THE STANDARD THESE ARE HELD TO, SAID BEFORE THE LIST.** A candidate here is a clause this
record has **corrected more than once**. It is **not** a proposal to strike it, and **the
executor does not rule on any of them.**

### **THE LIST IS EMPTY AT b300, AND AN EMPTY LIST IS REPORTED RATHER THAN THE HEADING DROPPED**
— b167's law in this file's own terms: a section that quietly disappears reads like a section that
was never there. The three candidates b299 filed have all been ruled on:

- **U-1 and U-2 — STRUCK**, by the author at b300, and they are now entries in the struck list
  above with patterns. They are **not duplicated here**.
- **U-3 — NOT A STRUCK CLAUSE.** The author's ruling, quoted verbatim: *"U-3 is NOT a struck
  clause; it stands as its existing work-order and is not duplicated."* That work-order is
  `W-ORD-ADHOC-CHECK-FIXTURES` (b298), b299 was the first act bound by it at a cap of zero, and
  **b300 IS THE SECOND.** It was listed at b299 because it is the record's most repeatedly
  corrected clause; **THE RULING IS THAT BEING REPEATEDLY CORRECTED IS NOT BY ITSELF GROUNDS FOR A
  STRIKE WHEN AN ANSWER IS ALREADY FILED SOMEWHERE ELSE.** Removed from this list per the ruling,
  and recorded here so its removal is not a silent drop.
