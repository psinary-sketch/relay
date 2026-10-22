b705 -- COMPONENT 1, (R315)(3): THE README FIGURE`S CONTROLS, THE REPAIRED readme() AGAINST THE UNREPAIRED AND ON MUTATED COPIES (2026-10-22T13:03:08Z)

### rows are cases: the copy | the stale lines read | wanted | the arm`s verdict against the reset baseline 0 | wanted. The README is not edited;
### the mutated copies are texts handed to readme(). The repaired readme(): tools/b705_standing_figures.py; the unrepaired: tools/b703_standing_figures.py :163.

  the real README by the repaired readme()                                                         | read  0 | wanted  0 | arm PASS | wanted PASS
  the real README by b703`s unrepaired readme() (b704`s figure beside)                             | read 12 | wanted 12 | arm -    | wanted -
  a mutated copy, the kernel line`s **v0.37** (`38e2734`) set back to **v0.35** (`d4e046a`)        | read  1 | wanted  1 | arm FAIL | wanted FAIL
  a mutated copy with a dated ceiling append naming v0.36 added at its end                         | read  0 | wanted  0 | arm PASS | wanted PASS

### the stale rows of the mutated copy: ['164 SIDE-explicit-formula v0.35']
### the excluded rows of the real README: 14 (a dated ceiling append (the append mark); a deposited version (a Citable deposit sentence); not a currency line (data/b702_readme_currency.txt (A): the kernel, federation and deposit-note lines))

### ### **THE REAL README READS 0 STALE ON THE REPAIRED FIGURE (b704`S 12 ON THE UNREPAIRED) ; THE v0.35 COPY READS 1 AND THE ARM FAILS ; THE APPEND COPY READS 0 ; EVERY CONTROL AS WANTED True.**
