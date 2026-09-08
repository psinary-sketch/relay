### run at (UTC) : 2026-09-08T16:48:28Z   ### NOT COVERED BY ANY HASH; it records when this run file was written.
====================================================================================================
b372 -- COMPONENT 2: THE README, AND THE LABEL THAT DOES NOT FIT IT.
====================================================================================================
  ### mode : WRITE

----------------------------------------------------------------------------------------------------
  ### (1) THE ORDER NAMES ONE OBJECT AND DESCRIBES ANOTHER. ### **BOTH ARE READ.**
----------------------------------------------------------------------------------------------------
    SIDE-effects (the exclusion kernel -- THE LABEL)
        clause 1, a headline figure          : False None
        clause 2, a breakdown summing apart  : False None
        clause 3, ships a profile            : False []
        ### ### **ALL THREE CLAUSES FIT : False**
    SIDE-global-section (the construction kernel)
        clause 1, a headline figure          : True  **212 terminals**
        clause 2, a breakdown summing apart  : True  33 parts summing to 250
        clause 3, ships a profile            : True  ['AXIOM_PRINTS.txt', 'AXIOM_PRINTS_INTERFACES.txt']
        ### ### **ALL THREE CLAUSES FIT : True**

    ### ### **THE DESCRIPTION FITS : ['SIDE-global-section (the construction kernel)']**
    ### ### **AND THE LABEL NAMES THE OTHER ONE.** ### This is `b367`s species -- a hint that
    ### ### names the right terminals and the wrong defect -- and it is REPORTED, not absorbed.
    ### **THE OBJECT IS IDENTIFIED BY THE DESCRIPTION**, because a description is checkable
    ### against a file and a label is not. ### **NOTHING IN THE EXCLUSION KERNEL`S README IS
    ### ### REPAIRED BY THIS ACT.**

----------------------------------------------------------------------------------------------------
  ### (2) THE EXCLUSION KERNEL'S README, READ ANYWAY, SO NOTHING IS LOST IF THE LABEL WAS MEANT.
----------------------------------------------------------------------------------------------------
    its ONE count line, README.md:69
      | 3 theorems, 3 sorrys (each at a marked analytic boundary), 0 axioms.
    ### ### **AND IT SHIPS NO AXIOM PROFILE AT ALL** -- so its count line cannot be checked
    ### ### against a printed profile the way the order`s `PRESENT` test requires.
    ### the exclusion kernel at `b67f29b72512` : tracked files matching AXIOM* : NONE

----------------------------------------------------------------------------------------------------
  ### (3) WHAT EACH FIGURE COUNTS. ### **DETERMINED AT CONTENT, NOT GUESSED.**
----------------------------------------------------------------------------------------------------
    ### the method is `b371`s and is unamended: ### **FIND THE COMMIT THAT INTRODUCED THE
    ### ### FIGURE AND MEASURE THE SAME QUANTITY THERE.**
    the headline figure    `**212 terminals**` ### introduced at : 3fe41b98a3fe
    the assembly ratio     `(250/250)` ### introduced at : 1f423da0a62e
    the module count       `across 50 modules` ### introduced at : 1f423da0a62e

    ### THE SAME QUANTITIES, MEASURED AT EACH REF:
    ref            date         headline  parts     sum       ratio     modules  prints
    3fe41b98a3fe   2026-08-21   **212 terminals** 23        212       (212/212) across 40 modules 212
    1f423da0a62e   2026-08-22   **212 terminals** 33        250       (250/250) across 50 modules 250
    e79e4ca7ff95   2026-09-08   **212 terminals** 33        250       (250/250) across 50 modules 590

    ### the module count against the tree it describes, at each ref:
      3fe41b98a3fe Core `.lean` 55   of which AxiomCheck 15  ### -> 40 not AxiomCheck ; README says across 40 modules
      1f423da0a62e Core `.lean` 65   of which AxiomCheck 15  ### -> 50 not AxiomCheck ; README says across 50 modules
      e79e4ca7ff95 Core `.lean` 110  of which AxiomCheck 16  ### -> 94 not AxiomCheck ; README says across 50 modules

    ### ### **THE FINDING, AND IT IS NOT WHAT THREE DIFFERENT NUMBERS SUGGEST:**
    ### ### **AT `3fe41b98a3fe` (2026-08-21): headline **212 terminals**, breakdown sum 212, ratio (212/212), profile 212.**
    ### ### **AT `1f423da0a62e` (2026-08-22): headline **212 terminals**, breakdown sum 250, ratio (250/250), profile 250.**
    ### ### **AT `e79e4ca7ff95` (2026-09-08): headline **212 terminals**, breakdown sum 250, ratio (250/250), profile 590.**
    ### refs at which the breakdown sum EQUALS the shipped profile : ['3fe41b98a3fe', '1f423da0a62e']

    ### ### ### **SO THE THREE FIGURES DO NOT COUNT THREE DIFFERENT THINGS.** ### They count
    ### ### ### **ONE QUANTITY -- CORE ZERO-AXIOM TERMINALS, ONE PER PRINTED LINE -- READ AT
    ### ### ### THREE DIFFERENT REFS**, and each was exact when it was written.
    ### ### **AND NONE OF THEM NAMES THE REF IT HOLDS AT**, which is the defect.

----------------------------------------------------------------------------------------------------
  ### (4) THE PROFILE, READ AS A PRINTED RECORD AND COMPARED AGAINST ITS BLOB (`b309`).
----------------------------------------------------------------------------------------------------
    working bytes 42320 ; blob bytes 42320 ; ### EOL-normalised equal : True
    printed lines 590 ; ### lines saying `does not depend on any axioms` : 590 ; distinct names 588
    ### ### **EVERY PRINTED LINE IS ZERO-AXIOM : True**
    ### ### -- so the README`s claim `No terminal failed the bar; none is excluded` is
    ### ### SUPPORTED, and the repair does not touch it.

----------------------------------------------------------------------------------------------------
  ### (5) THE REPAIR. ### **ORIGINAL BANKED VERBATIM; A FIGURE REMOVED, NOT RESTATED.**
----------------------------------------------------------------------------------------------------
    ### THE ORIGINALS, QUOTED BEFORE ANY EDIT:
      README.md:22
      | - **`Core/`** — the vanilla load-bearing layer: **212 terminals** (103 construction-era + 11 purity-and-distance + 7 silence-theorem + 8 Plancherel-shadow + 3 cross-place + 3 pairing + 3 twisted + 3 deficit + 22 character-sum + 3 flatness + 3 silence-only-if + 6 product-minus-sum + 3 metaplectic-root + 2 twisted-root + 3 theta + 5 odd-pairing + 2 product-law + 4 tower-limit + 5 phase-plane + 4 lefschetz + 3 frame-boundary + 3 fourth-visit + 3 theta-continuation + 3 coherence + 4 critical-pass + 6 adelic-plane + 5 radialization + 3 window + 4 rigidity + 3 value + 3 theta-bridge + 3 determination + 4 constructor) across 50 modules plus their AxiomCheck
      README.md:25
      |   assembly, `AXIOM_PRINTS.txt` (250/250). No terminal failed the bar; none is excluded.

    ### THE REPLACEMENTS:
      | - **`Core/`** — the vanilla load-bearing layer: **as many zero-axiom terminals as `AXIOM_PRINTS.txt` in this tree carries**, one per printed line. The figure is not written out here: a figure written out goes stale the moment the layer grows, and this one did. The layer census that follows is held at `1f423da` (2026-08-22) and is not re-derived here — (103 construction-era + 11 purity-and-distance + 7 silence-theorem + 8 Plancherel-shadow + 3 cross-place + 3 pairing + 3 twisted + 3 deficit + 22 character-sum + 3 flatness + 3 silence-only-if + 6 product-minus-sum + 3 metaplectic-root + 2 twisted-root + 3 theta + 5 odd-pairing + 2 product-law + 4 tower-limit + 5 phase-plane + 4 lefschetz + 3 frame-boundary + 3 fourth-visit + 3 theta-continuation + 3 coherence + 4 critical-pass + 6 adelic-plane + 5 radialization + 3 window + 4 rigidity + 3 value + 3 theta-bridge + 3 determination + 4 constructor) across 50 modules plus their AxiomCheck
      |   assembly, `AXIOM_PRINTS.txt` in this tree. No terminal failed the bar; none is excluded.

    ### **WHAT WAS REMOVED AND WHAT WAS KEPT, ITEM BY ITEM:**
      -- the headline figure `**212 terminals**` : ### **REMOVED**, and not restated with the current one,
         because a new number re-arms the same trap (`b371`s rule, unamended).
      -- the assembly ratio `(250/250)` : ### **REMOVED**; the file it points at is named instead.
      -- the layer census and the module count : ### **PRESERVED VERBATIM AND DATED TO THE
         ### REF THEY HOLD AT**, which is what the order permits in place of removal.
      -- ### **NO CLAIM IS REWRITTEN.** ### `No terminal failed the bar; none is excluded`
         stands, and section (4) above is its evidence.
    ### ### **AND ONE THING IS ROUTED RATHER THAN REPAIRED:** ### re-deriving the census at
    ### ### HEAD is a per-layer recount of the tree, ### **A CLAIM AND NOT A NUMBER**, and
    ### ### the order says route it. ### It is routed.

    ### ### **WRITTEN.** ### 3802 -> 4095 bytes.
    ### the removed figures still present after the edit : [] ### -- must be []
    ### the census and module count preserved verbatim  : True
    ### the line count is unchanged                     : True

====================================================================================================
  ### **NO BUILD WAS RUN. ### NO `.lean` FILE WAS TOUCHED. ### THE PROFILE WAS READ.**
  ### **NOTHING IN THE EXCLUSION KERNEL WAS WRITTEN.**
====================================================================================================
