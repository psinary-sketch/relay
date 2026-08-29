# -*- coding: utf-8 -*-
"""b256 -- FILE THE INDEX KEY. ### APPEND ONLY.
### `contribution-map` was queried BEFORE any step and returned NO KEY.
"""
import io

PATH = r"D:\relay\tools\banked_index.py"

KEY_ANCHOR = ("    'limit-profile': ['the limit profile', 'the cutoff ladder', "
              "'the balance along a^2',\n"
              "                      'the junction sawtooth', 'the staircase sawtooth', "
              "'sixteen cells'],\n")
KEY_NEW = (
    "    'contribution-map': ['the contribution map', 'the whole position at grade',\n"
    "                         'the patent session input', 'the fold-forward ledger',\n"
    "                         'h2-dependency column', 'the figure candidates'],\n"
)

ROW_ANCHOR = ("     'data/b255_limit_profile.txt; data/b255_run.txt; data/b255_pricing.txt; '\n"
              "     'data/b255_meanings.txt; reports/2026-08-29-the-limit-profile.md'),\n")
ROW_NEW = (
    "    ('contribution-map', 'b256 (reads + one document at support-voice)',\n"
    "     'the whole research position stated at grade in ONE document, placed at '\n"
    "     'PLACE-papers/phase1.5/method/CONTRIBUTION_MAP_2026-08.md. ### CLASS LINE: TIER N * '\n"
    "     'PRIVATE * PATENT-SESSION INPUT * **STATES GRADES, CONFERS NONE**. ### 18 rows, each '\n"
    "     'carrying grade-today + owner + AIM + h2-dependency + filing touched + figure '\n"
    "     'candidates; plus the fold-forward ledger b234-b255 with **every obstacle QUOTED from '\n"
    "     'its owning act** (22 acts, 22 reports, count reconciled); plus two annexes',\n"
    "     '### **NO GRADE MOVED.** ### h2-dependency: 13 NO, 5 YES (adjacent), and **EVERY '\n"
    "     'PATENT-FACING ROW IS NO** -- verified by reading the claim-backing table FIRST (its ten '\n"
    "     'rows are QEC / Fano-Steane / Epstein / spinor / cross-exclusion terminals, none '\n"
    "     'touching the RH identity). ### **THE YES ROWS ARE MARKED *ADJACENT*: they are the rows '\n"
    "     'h2 would BEAR ON if it moved, not rows that assume it -- a blanket sentence would have '\n"
    "     'hidden that and a column shows it.** ### Counts RE-COUNTED from the filesystem: **44 '\n"
    "     'built** (11+13+7+6+4+3) and **REVIEW_SET_2026-08 = 31**, both matching the session '\n"
    "     'header exactly; the bare find count of 82 files / 51 unique basenames is reconciled as '\n"
    "     'STAGING COPIES, not a divergence. ### **AND THE ONE ITEM THE ACT COULD NOT DELIVER, AT '\n"
    "     'FULL PROMINENCE: SIGNEDNESS (S.I.D.E+S) WAS TO BE *QUOTED* AND IS NOT IN THIS SEAT '\n"
    "     'REACH OR IN THE CORPUS -- zero occurrences across relay/ and all of PLACE-papers/. ### '\n"
    "     'RECORDED AS A NAMED SLOT WITH OWNER AND ROUTE, QUOTATION MARKED OWED, NOT PARAPHRASED '\n"
    "     'AND NOT INVENTED.** ### J1 recorded PARKED-BY-AUTHOR (save); J2 UNPROMOTED CANDIDATE; '\n"
    "     'no annex-A candidate marked Priority-A. ### **AND A LIVE b148 CONDITION FOUND AND '\n"
    "     'REPORTED: SEVEN PATENT-SEAT FIGURE DIRECTORIES SIT UNTRACKED IN THE SHARED WORKTREE, '\n"
    "     'DATED 2026-08-24, HOLDING THE 44 FIGURES AND THE SIX BATCH RECORDS** -- not this act '\n"
    "     'doing (verified by mtime), not staged by it (place_add.py used), and reported rather '\n"
    "     'than resolved. ### Hook exercised: CLEAN, 0 foreign hits. ### Mirror rebuilt and '\n"
    "     'verified CLEAN on all three clauses (40 files, HEAD 2bcdff5 vs ls-remote). ### '\n"
    "     '**STANDING PRACTICE INSTITUTED: every profile act bank ends with a chart-ready CSV '\n"
    "     'block of all columns** -- applied retrospectively to b255',\n"
    "     'PLACE-papers/phase1.5/method/CONTRIBUTION_MAP_2026-08.md; '\n"
    "     'data/b256_contribution_map.txt; data/b256_b255_profile.csv; '\n"
    "     'reports/2026-08-29-the-contribution-map.md'),\n"
)


def main():
    txt = io.open(PATH, encoding="utf-8").read()
    if "'contribution-map'" in txt:
        print("  ### already filed, untouched.")
        return
    for name, anchor in (("KEYS", KEY_ANCHOR), ("ROWS", ROW_ANCHOR)):
        if txt.count(anchor) != 1:
            print("  ### REFUSED: %s anchor hit %d times." % (name, txt.count(anchor)))
            return
    txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + KEY_NEW)
    txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + ROW_NEW)
    io.open(PATH, "w", encoding="utf-8").write(txt)
    print("  FILED: contribution-map.")


if __name__ == "__main__":
    main()
