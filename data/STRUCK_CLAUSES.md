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

## UNCONFIRMED CANDIDATES — for the author. **NOT LOADED BY THE CHECK. NONE PROMOTED.**

### **THE STANDARD THESE ARE HELD TO, SAID BEFORE THE LIST.** A candidate here is a clause this
record has **corrected more than once**. It is **not** a proposal to strike it, and **the
executor does not rule on any of them.** Two are seat-corrections and one is the author's; the
difference is marked on each, because a clause the seat keeps correcting in itself is a different
object from a clause the author keeps correcting in the seat.

### U-1
STATUS: UNCONFIRMED
CLAUSE: an act predicts the count of the objects it will build, and declares a miss when the count differs
CORRECTED: twice, both by the seat — b298 registered 10 terminals and built 12, declaring the miss at its own (D1) rather than trimming controls to hit the number; b299's registration then wrote that "A COUNT THE ACT HAS NO REASON TO FIX IN ADVANCE IS A NUMBER INVENTED TO BE PREDICTED" and declined to predict one
NOTE: the two corrections point opposite ways — b298 kept the practice and paid for it, b299 dropped it for one class of count. Neither is a ruling and no act has reconciled them.

### U-2
STATUS: UNCONFIRMED
CLAUSE: a closing sequence reports "HANDOFF current"
CORRECTED: repeatedly, by the seat — `HANDOFF.md`'s head has read b278 since b293, and b298 wrote that the arc's handoff "LIVES IN THE BANKS AND IN FINDINGS.md, AND THIS ACT SAYS SO RATHER THAN LETTING 'CURRENT' DO SILENT WORK"
NOTE: the phrase has been kept and qualified rather than dropped, in every act since. A clause that must be annotated every time it is used is a candidate; it is not thereby struck.

### U-3
STATUS: UNCONFIRMED
CLAUSE: a number an act reports may come from a check the act typed at the shell
CORRECTED: three consecutive acts — b296's tally (an untallied control, a fallback folded into a pass count), b297's blank-cell scan (a newline-spanning match reporting 111 blank cells in a table of 111 rows), b298's float and artifact regexes (one matching the word inside the prose denying it) and its profile BOM
NOTE: **this one is already answered without a strike** — it is filed as the standing work-order `W-ORD-ADHOC-CHECK-FIXTURES` (b298), and b299 is the first act bound by it at a cap of zero. It is listed because it is the record's most repeatedly-corrected clause, and a reader comparing this list against the desk should find it in both.
