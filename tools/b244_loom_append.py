# -*- coding: utf-8 -*-
"""b244_loom_append.py -- APPEND ONE HUNK TO THE LOOM. ### NOTHING ELSE IS TOUCHED.

### WHY THIS IS A FILE AND NOT A SHELL LINE. ### b158's standing rule: WRITE SCRIPT FILES, NOT
### SHELL STRINGS. ### It has been earned three times -- b178 (a bibliography patch whose
### backticks the shell ate, reporting success), b193 (a correspondence row whose terminals,
### path and axiom list all vanished, reporting success), and ### **THIS ACT, whose first
### attempt at the loom append died on an unmatched quote inside a heredoc.** ### The third
### instance cost nothing because the shell refused; the first two shipped.
###
### ### AND THE LAW THIS FILE EXISTS TO OBEY, b240's MISS 2:
### ### **"A GLOBAL REPLACE ON AN APPEND-ONLY DOCUMENT IS AN EDIT TO THE RECORD WEARING THE
### ### CLOTHES OF A FIX."** ### b240 repaired a banned stem with a whole-file replace and
### ### rewrote SEVEN LINES BELONGING TO EARLIER ACTS, among them a Yang-Mills row whose
### ### subject IS the object whose name contains the stem.
### ### SO THIS TOOL DOES EXACTLY ONE THING: it reads the loom, appends the block, and writes
### ### it back. ### IT NEVER SUBSTITUTES, NEVER REPLACES, AND NEVER TOUCHES A BYTE ABOVE THE
### ### APPEND POINT -- and it PROVES that by comparing the prefix before and after.
"""
import io
import os
import sys

LOOM = r"D:\MY-DOwnloads\PLACE-papers\VERIFICATION_LOOM.md"


def main(block_path):
    if not os.path.exists(block_path):
        print("### REFUSED -- block not found: %s" % block_path)
        return 2
    block = io.open(block_path, encoding="utf-8").read()
    if not block.strip():
        print("### REFUSED -- an empty block is not an entry.")
        return 2
    before = io.open(LOOM, encoding="utf-8").read()
    out = before.rstrip() + "\n" + block
    io.open(LOOM, "w", encoding="utf-8", newline="\n").write(out)

    after = io.open(LOOM, encoding="utf-8").read()
    # ### THE PROOF: every byte of the ORIGINAL, up to its own last non-space character, must
    # ### still be there and unchanged. ### A pure insertion cannot fail this; a replace can.
    prefix_ok = after.startswith(before.rstrip())
    grew = len(after) > len(before)
    print("--- LOOM APPEND (b244) ---")
    print("  loom            : %s" % os.path.basename(LOOM))
    print("  bytes before    : %d" % len(before))
    print("  bytes after     : %d" % len(after))
    print("  block bytes     : %d" % len(block))
    print("  ### PREFIX UNCHANGED (pure insertion) : %s" % ("YES" if prefix_ok else "### NO"))
    print("  ### FILE GREW                          : %s" % ("YES" if grew else "### NO"))
    if not (prefix_ok and grew):
        print("  ### HARD FAILURE -- THIS WAS NOT A PURE APPEND.")
        return 1
    print("  VERDICT         : APPENDED, prefix verified byte-for-byte")
    print("  ### and that means NO EARLIER ACT'S LINE MOVED. It does not mean the block is true.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ""))
