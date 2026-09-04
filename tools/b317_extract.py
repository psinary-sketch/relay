# -*- coding: utf-8 -*-
"""b317_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**

### WHY THIS EXISTS. ### The order for this act says it in one line: ### **for each file the act
### needs, extract the needed fragments WITH THEIR LOCATIONS into a notes file, and read only that
### file.** ### A source read by paging whole pages of a typeset PDF into a session is a read
### nobody can re-run; ### **A SOURCE READ THROUGH THIS TOOL IS A FILE ON DISK WITH LINE NUMBERS
### AND PAGE INDICES, AND THE NEXT SEAT RE-RUNS IT.**

### ### **WHAT IT DOES.**
###   ### **(a)** pins the artefact by `sha256` BEFORE a word of it is read, against b304/b305's
###     value, imported from `b305_source.py` ### **RATHER THAN COPIED**;
###   ### **(b)** locates each named fragment by PAGE INDEX and prints a window of the page's own
###     raw text around it -- ### **RAW, NOT NORMALISED**, because the normalisation exists to
###     FIND the fragment and would silently rewrite what is quoted;
###   ### **(c)** slices each named code fragment out of its tool by LINE RANGE.

### ### **THE LIMIT, IN THE HEADER SO IT IS NOT TRUSTED BEYOND IT.** ### This tool LOCATES. ### It
### cannot tell a correct reading from an incorrect one, and a window it prints is a window, not an
### interpretation. ### **AND THE PDF'S TEXT LAYER RENDERS PARENTHESES AS `p`/`q` AND DROPS SOME
### ### SPACING**, so every quotation taken from it is a HUMAN read of a located window and is
### marked as such in the bank.
"""
import io
import os
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b305_source as S5  # noqa: E402  ### the pin and the normaliser are READ, never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(ROOT, 'data', 'b317_extract_notes.txt')

# ### ==============================================================================================
# ### THE SOURCE FRAGMENTS THIS ACT NEEDS. ### **NAMED BEFORE THEY ARE READ.**
# ### Each is `(label, page_index, anchor_normalised, before, after)`.
# ### The anchors are written in the PDF's OWN normalised alphabet -- parentheses as `p`/`q` --
# ### because that is what the text layer contains.
# ### ==============================================================================================
SOURCE_FRAGMENTS = [
    ('(16) THE INNER PRODUCT', 6, 'inL2pRqevasfollows', 40, 300),
    ('(24) THE TRANSFORM', 7, 'itdefinestheunitary', 60, 240),
    ('(53) W_infinity AND (54) THE VANISHING CONDITIONS', 16,
     'weinvestigatethefunctional', 260, 900),
    ('(61) THE SCALING ACTION', 22, 'itsactionisgivenby', 220, 280),
    ('DEFINITION 4.4 / (72) THE SPACE S(a,b)', 24, 'Definition4.4For', 20, 700),
    ('THEOREM 4.7 -- (83) AND (84)', 26, 'Theorem4.7', 120, 900),
    ('(43) THE LOCAL TRACE FORMULA', 12, 'piiiqForf', 60, 420),
]

# ### ==============================================================================================
# ### THE CODE FRAGMENTS. ### `(label, relative path, first line, last line)`, 1-INDEXED INCLUSIVE.
# ### ==============================================================================================
CODE_FRAGMENTS = [
    ('THE ATLAS BUMP -- the corpus\'s integral-one bump, its EMITTING FILE',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 43, 52),
    ('THE ATLAS CHANNELS -- where the corpus\'s archimedean number A is formed',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 55, 82),
    ('THE ATLAS INSTRUMENT CONSTANTS -- committed before any answer',
     os.path.join('tools', 'e16', 'carto_atlas.py'), 24, 25),
    ('THE INSTRUMENT (N1)-(N4) -- the four normalizations, written once',
     os.path.join('tools', 'b316_instrument.py'), 45, 48),
    ('THE INSTRUMENT FRAME -- the truncation, midpoints, and the transform\'s own grid',
     os.path.join('tools', 'b316_instrument.py'), 53, 76),
    ('THE INSTRUMENT SUBSPACE -- the projector S',
     os.path.join('tools', 'b316_instrument.py'), 93, 113),
    ('THE INSTRUMENT SCALING -- eq. (61) as an operator',
     os.path.join('tools', 'b316_instrument.py'), 130, 141),
    ('THE SMEAR TOOL -- b310\'s assembly at a FINITE place, and its stated scope',
     os.path.join('tools', 'b310_smear.py'), 3, 24),
]


# ### ==============================================================================================
# ### THE DECOMPOSITION. ### **THIS IS THE DEFECT THAT COST FOUR FRAGMENTS ON THE FIRST RUN, AND
# ### ### THE CORPUS ALREADY OWNED THE FIX.**
# ### The typesetter emits `De<fi>nition` with ONE character, `U+FB01`, and ### **`str.isalnum()` IS
# ### ### TRUE OF IT**, so it survived this tool's strip untouched: the normalised page read
# ### `De<fi>nition44` and the ASCII anchor `Definition44` could never match it. ### **A LIGATURE
# ### ### MISS LOOKS EXACTLY LIKE AN ABSENT FRAGMENT AND IS NOT ONE.**
# ### ### **AND `b305_source.flatten` HAD ALREADY SOLVED THIS, WITH `NFKD`, AND SAYS SO IN ITS OWN
# ### ### DOCSTRING.** ### This tool needs an index MAP that `flatten` does not return, so a second
# ### implementation was necessary -- ### **BUT IT SHOULD HAVE CARRIED b305's NORMALISATION AND IT
# ### ### DID NOT.** ### It now uses the same `NFKD` step, so there is ONE convention and not two.
# ### The window is still cut from the RAW page, so a quotation keeps the glyph the source set.
# ### ==============================================================================================


def normalise_with_map(raw):
    """### RETURNS `(norm, idx)` where `norm[i]` came from `raw[idx[i]]`.

    ### ### **THE MAP IS THE WHOLE POINT.** ### The anchor is matched in the normalised string and
    ### the window is cut from the RAW one, so the quotation carries the source's own characters.
    ### ### **A LIGATURE EXPANDS TO TWO NORMALISED CHARACTERS THAT SHARE ONE RAW INDEX**, which is
    ### why `idx` is built by appending rather than by enumeration.
    """
    keep, idx = [], []
    for i, ch in enumerate(raw):
        for c in unicodedata.normalize('NFKD', ch):
            if c.isalnum():
                keep.append(c)
                idx.append(i)
    return ''.join(keep), idx


def fold_anchor(anchor):
    """### THE ANCHOR THROUGH THE SAME DECOMPOSITION, so an anchor may be written in plain ASCII.

    ### **THE SAME `NFKD` STEP `b305_source.flatten` TAKES**, so the two tools agree on what a
    ### character is."""
    return ''.join(c for ch in anchor for c in unicodedata.normalize('NFKD', ch) if c.isalnum())


def window(raw, anchor, before, after):
    """### THE RAW WINDOW AROUND `anchor`. ### RETURNS `(text, char_offset)` or `(None, -1)`."""
    norm, idx = normalise_with_map(raw)
    a = fold_anchor(anchor)
    at = norm.find(a)
    if at < 0:
        return None, -1
    lo = max(0, idx[at] - int(before))
    hi = min(len(raw), idx[min(at + len(a) - 1, len(idx) - 1)] + int(after))
    return raw[lo:hi], idx[at]


def self_test():
    """### **FIXTURES. ### THE FINDER MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok = []
    raw = 'alpha ppq beta\ngamma delta'
    # ### (i) it finds an anchor that is there, ACROSS the whitespace the text layer inserts.
    t, off = window(raw, 'betagamma', 0, 0)
    ok.append(t is not None and off == 10)
    # ### (ii) ### **AND IT DOES NOT FIND ONE THAT IS ABSENT** -- an arm that always finds is
    # ### not a finder.
    t2, off2 = window(raw, 'epsilonzeta', 0, 0)
    ok.append(t2 is None and off2 == -1)
    # ### (iii) the window is cut from the RAW string, so it carries the newline the normaliser
    # ### threw away.
    t3, _ = window(raw, 'beta', 0, 12)
    ok.append(t3 is not None and '\n' in t3)
    # ### (iv) the map is honest: the reported offset indexes the raw string at the anchor.
    ok.append(raw[off:off + 4] == 'beta')
    # ### (v) an empty anchor is not a match everywhere by accident -- it is a match at 0, and
    # ### the caller never passes one; the fixture records the behaviour rather than hiding it.
    t5, off5 = window(raw, '', 0, 3)
    ok.append(off5 == 0)
    # ### (vi) ### **THE LIGATURE ARM.** ### An ASCII anchor finds a ligatured page ...
    lig = 'Deﬁnition 4.4 For'
    t6, off6 = window(lig, 'Definition4.4For', 0, 0)
    ok.append(t6 is not None and off6 == 0)
    # ### (vii) ### **AND THE FOLD DOES NOT MAKE THE FINDER FIND ANYTHING** -- the same page
    # ### still refuses an anchor that is not on it.
    t7, off7 = window(lig, 'Definition4.5For', 0, 0)
    ok.append(t7 is None and off7 == -1)
    # ### (viii) the raw window still carries the LIGATURE, not the expansion -- the fold is for
    # ### finding only, and a quotation that silently de-ligatured the source would be a rewrite.
    t8, _ = window(lig, 'Definition4.4', 0, 20)
    ok.append(t8 is not None and 'ﬁ' in t8)
    return all(ok), ok


def main(argv):
    good, arms = self_test()
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b317_extract.py -- THE EXTRACT STEP. ### **NOTHING RAW IS PAGED INTO THE ACT.**')
    rec('=' * 100)
    rec('  finder self-test : %s  %s' % (arms, 'PASS' if good else 'FAIL'))
    if not good:
        rec('  ### HARD FAILURE -- THE FINDER DOES NOT PASS ITS OWN FIXTURES. ### NOTHING READ.')
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 1

    if not argv:
        rec('  usage: python b317_extract.py <path-to-cc-pdf>')
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 2
    pdf = argv[0]

    # ### ------------------------------------------------------------------ THE PIN, BEFORE A READ
    rec('')
    rec('-' * 100)
    rec('### THE PIN. ### **BEFORE A WORD OF THE ARTEFACT IS READ.**')
    rec('-' * 100)
    if not os.path.exists(pdf):
        rec('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 3
    got = S5.sha256_file(pdf)
    rec('  artefact  : %s' % os.path.basename(pdf))
    rec('  cite      : %s' % S5.SOURCE_CITE)
    rec('  url       : %s' % S5.SOURCE_URL)
    rec('  bytes     : %d' % os.path.getsize(pdf))
    rec('  sha256    : %s' % got)
    rec('  ### MATCHES THE VALUE b304 PINNED AND b305 RE-COMPUTED : %s  %s'
        % (got == S5.EXPECT_SHA, 'YES' if got == S5.EXPECT_SHA else '### NO -- HARD FAILURE'))
    if got != S5.EXPECT_SHA:
        io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
        return 4

    from pypdf import PdfReader
    r = PdfReader(pdf)
    rec('  pages     : %d' % len(r.pages))

    # ### ------------------------------------------------------------------ THE SOURCE FRAGMENTS
    rec('')
    rec('-' * 100)
    rec('### THE SOURCE FRAGMENTS, LOCATED BY PAGE INDEX.')
    rec('### **THE TEXT LAYER RENDERS PARENTHESES AS `p`/`q` AND BREAKS WORDS ACROSS LINES.**')
    rec('### ### **EVERY WINDOW BELOW IS RAW. ### THE READING OF IT IS THE AUTHOR\'S, NOT THIS')
    rec('### ### TOOL\'S, AND THE BANK MARKS IT SO.**')
    rec('-' * 100)
    missing = 0
    for label, pg, anchor, before, after in SOURCE_FRAGMENTS:
        raw = r.pages[pg].extract_text() or ''
        text, off = window(raw, anchor, before, after)
        rec('')
        rec('### ==== %s' % label)
        rec('###      page index %d (printed page %d) | anchor %r | char offset %s'
            % (pg, pg + 1, anchor, off if off >= 0 else 'NOT FOUND'))
        if text is None:
            rec('### ### **NOT FOUND ON THAT PAGE.** ### The fragment the act names is not where')
            rec('### ### the act says it is, and that is a HARD failure for this fragment.')
            missing += 1
            continue
        for ln in text.splitlines():
            rec('    | %s' % ln)
    rec('')
    rec('### SOURCE FRAGMENTS NOT FOUND : %d' % missing)

    # ### ------------------------------------------------------------------ THE CODE FRAGMENTS
    rec('')
    rec('-' * 100)
    rec('### THE CODE FRAGMENTS, BY FILE AND LINE RANGE. ### **1-INDEXED, INCLUSIVE.**')
    rec('-' * 100)
    cmissing = 0
    for label, rel, lo, hi in CODE_FRAGMENTS:
        path = os.path.join(ROOT, rel)
        rec('')
        rec('### ==== %s' % label)
        rec('###      %s : lines %d-%d' % (rel.replace(os.sep, '/'), lo, hi))
        if not os.path.exists(path):
            rec('### ### **FILE NOT FOUND.**')
            cmissing += 1
            continue
        src = io.open(path, encoding='utf-8').read().splitlines()
        for i in range(lo - 1, min(hi, len(src))):
            rec('  %5d | %s' % (i + 1, src[i]))
    rec('')
    rec('### CODE FRAGMENTS NOT FOUND : %d' % cmissing)
    rec('')
    rec('=' * 100)

    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('b317_extract: wrote %s  (%d bytes, %d lines)'
          % (os.path.basename(NOTES), os.path.getsize(NOTES), len(lines)))
    print('  source fragments missing : %d' % missing)
    print('  code fragments missing   : %d' % cmissing)
    return 0 if (missing == 0 and cmissing == 0) else 5


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
