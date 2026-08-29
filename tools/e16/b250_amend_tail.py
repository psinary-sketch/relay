# -*- coding: utf-8 -*-
"""b250 -- AMEND THE 'UNBOUNDED TAIL' SENTENCES WHEREVER THE RECORD CARRIES THEM.

### ### **THE ORIGINALS STAY VISIBLE. ### NOTHING IS DELETED, REWRITTEN OR BACKDATED.**
### b240's append-only-document law; b244's precedent when its own registration held an error.
### Each amendment is APPENDED immediately after the sentence it amends, and each says plainly
### that the original was TRUE WHEN WRITTEN.
###
### ### **AND THE HAZARD THIS TOOL MUST NOT FALL INTO, NAMED BEFORE IT RUNS:** ### the record
### carries the word "unbounded" in a SECOND and UNRELATED sense -- ### **the W-UNION
### `(nonArchimedean, unbounded)` QUADRANT** -- across a dozen reports. ### That is a DIFFERENT
### OBJECT, it is NOT amended by this act, and matching on the bare word would have amended it.
### ### **THIS TOOL MATCHES ON FULL SENTENCES, NOT ON THE WORD.** ### b247's double-name species.
"""
import io

AMEND = (
    u"\n>\n> ### **AMENDED AT b250 (2026-08-29): THE TAIL TERM IS NO LONGER UNBOUNDED.** S4's"
    u" envelope bounds it, and at K1's cut `N = 6` the bound is **`1.158e-14` on ZERO SPECIFIC"
    u" IMPORTS** (`sum_{n>N} t(n) <= (2 - S_N)/(1 - beta_N)`, `beta_N` from the exponential's own"
    u" Taylor series). ### **THE SENTENCE ABOVE STANDS AS WRITTEN AND WAS TRUE WHEN WRITTEN** --"
    u" b242 derived an envelope and refused it, and refusing an unproved envelope was correct."
    u" ### **AND `bar_L`'s AMBER DOES NOT CLEAR: the bar still reports seven computable modes"
    u" against a definition of eleven, which is a bench-precision fact b250 did not remove.**\n"
)

TARGETS = [
    (r"D:\relay\reports\2026-08-28-first-face-off.md",
     u"machine precision**, and its largest term rides an unbounded truncation."),
    (r"D:\relay\reports\2026-08-29-the-serializing-close.md",
     u"rather than inherit a number that looks certified.**"),
    (r"D:\relay\reports\2026-08-29-the-second-face-off.md",
     u"> ### **THE TAIL TERM IS NOT A BOUND.**"),
]


def main():
    for path, anchor in TARGETS:
        txt = io.open(path, encoding="utf-8").read()
        if u"AMENDED AT b250" in txt:
            print("  already amended, untouched : %s" % path)
            continue
        if txt.count(anchor) != 1:
            print("  ### REFUSED (anchor not unique: %d hits) : %s" % (txt.count(anchor), path))
            continue
        # append at the END of the paragraph containing the anchor, so the original reads whole
        i = txt.index(anchor)
        j = txt.find(u"\n\n", i)
        if j < 0:
            print("  ### REFUSED (no paragraph end) : %s" % path)
            continue
        io.open(path, "w", encoding="utf-8").write(txt[:j] + AMEND + txt[j:])
        print("  AMENDED (original intact, %d bytes added) : %s" % (len(AMEND), path))


if __name__ == "__main__":
    main()
