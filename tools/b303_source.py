# -*- coding: utf-8 -*-
"""b303_source.py -- THE SOURCE READ, ### **MADE REPRODUCIBLE INSTEAD OF NARRATED.**

### WHAT IT IS FOR. ### b302's Component 1 executed a ruling against two clauses the corpus holds
### ### THROUGH A READER ### (b197) rather than through its own extract, and it declared its own
### exposure in its own bank: ### *"IF DEFINITION 3.3.1's LOST CONDITION SHOULD TURN OUT TO ASK FOR
### SOMETHING BEYOND A VECTOR AND A NORM, THIS EXECUTION WOULD NEED REVISITING."*
### ### **THIS TOOL FETCHES NOTHING AND DECIDES NOTHING. ### IT PINS THE ARTEFACT AND CUTS THE
### ### PAGE**, so that the read a human then performs is a read of a NAMED object at a NAMED
### offset, and a later act can cut the same rectangle from the same bytes.

### ### **THE DEFECT IT MEASURES, IN THE ARTEFACT ITSELF:** ### the PDF's OCR text layer drops
### every displayed formula, and Definition 3.3.1's text layer therefore ends mid-sentence. ### The
### tool reports that truncation ### AS A MEASURED PROPERTY OF THE FILE ### rather than as a story
### about it -- and the truncation detector carries both polarities, because a detector that fires
### on every page would make the finding meaningless.

### ### **WHAT IT DOES NOT CLAIM: ### THE IMAGE IS NOT READ BY THIS TOOL.** ### No OCR is run and
### no character is inferred. ### **THE QUOTATION IN THE BANK IS A HUMAN READ OF THE EMITTED PNG**,
### and the tool's entire contribution is that the PNG is identified by hash and reproducible from
### the pinned bytes. ### An instrument that both cut the page and told you what it said would be
### the only witness to its own claim.
"""
import hashlib
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE ARTEFACT, PINNED BY ORIGIN AND BY HASH. ### **THE 6.3 MB PDF IS NOT COMMITTED** -- a
# ### binary of a third party's scan does not belong in this repo -- so the URL AND THE SHA256
# ### TOGETHER are what make the read repeatable.
SOURCE_URL = 'http://www.numdam.org/item/CM_1939__6__1_0.pdf'
SOURCE_CITE = ('von Neumann, "On infinite direct products", '
               'Compositio Mathematica, tome 6 (1939), pp. 1-77')
PAGE_INDEX = 21          # ### 0-based; the article's page 21, which carries DEFINITION 3.3.1
CROP = (0.10, 0.845, 0.95, 0.905)   # ### fractions of (width, height): the definition's two lines


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def truncated_at(text, marker='if and'):
    """### **DOES THIS TEXT END MID-SENTENCE AT `marker`?**

    ### Returns the 0-based line index of a line whose STRIPPED text ENDS with `marker`, or
    ### `None`. ### **THE `endswith` IS THE WHOLE DISCRIMINATION**: a page that merely CONTAINS
    ### the words "if and" is not a page whose text layer stopped there, and conflating the two
    ### would report the defect on pages that do not have it.
    """
    for i, line in enumerate(text.splitlines()):
        if line.strip().endswith(marker):
            return i
    return None


def self_test(verbose=True):
    """### **BOTH POLARITIES, AND THE NEAR-MISS IS THE ONE THAT MATTERS.**"""
    cases = [
        ('fires: a line stopping dead at the marker',
         'DEFINITION 3.3.1. A sequence f, is a C0-sequence, if and\n22\n', 0),
        ('fires: the marker at the end of a later line',
         'first line\nsecond line ending if and\n', 1),
        ('### NEAR-MISS, stays quiet: the marker mid-line, sentence continues',
         'a C0-sequence, if and only if f in H for all alpha\n', None),
        ('### NEAR-MISS, stays quiet: the words present but not terminal',
         'we ask if and when the sum converges here\n', None),
        ('### quiet: a page with no marker at all',
         'LEMMA 3.3.1. Every C0-sequence is a C-sequence, too.\n', None),
        ('### quiet: empty text -- not a silent hit',
         '', None),
    ]
    bad = 0
    if verbose:
        print('  %-58s %-16s %s' % ('truncation fixture', 'got/expected', 'agree'))
    for lbl, text, expect in cases:
        got = truncated_at(text)
        ok = (got == expect)
        bad += 0 if ok else 1
        if verbose:
            print('  %-58s %-16s %s' % (lbl, '%s/%s' % (got, expect),
                                        'YES' if ok else '### NO ###'))
    return bad == 0


def main(argv):
    if not argv:
        print('usage: python b303_source.py <path-to-pdf> [out-dir]')
        return 2
    pdf = argv[0]
    outdir = argv[1] if len(argv) > 1 else os.path.dirname(os.path.abspath(pdf))

    print('=' * 100)
    print('b303_source.py -- THE SOURCE READ. ### THE ARTEFACT PINNED, THE PAGE CUT.')
    print('=' * 100)
    ok = self_test()
    print('  truncation-detector self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A READ FROM A DETECTOR THAT FAILS ITS OWN FIXTURES.')
        return 2
    if not os.path.exists(pdf):
        print('  ### HARD FAILURE -- THE ARTEFACT IS NOT AT %s' % pdf)
        return 2
    print()
    print('  citation      : %s' % SOURCE_CITE)
    print('  origin        : %s' % SOURCE_URL)
    print('  local bytes   : %d' % os.path.getsize(pdf))
    print('  sha256        : %s' % sha256_file(pdf))

    from pypdf import PdfReader           # ### imported late so the fixtures run without it
    from PIL import Image

    r = PdfReader(pdf)
    print('  pages in file : %d' % len(r.pages))
    if PAGE_INDEX >= len(r.pages):
        print('  ### HARD FAILURE -- PAGE INDEX %d IS OUT OF RANGE.' % PAGE_INDEX)
        return 2

    page = r.pages[PAGE_INDEX]
    text = page.extract_text() or ''
    cut = truncated_at(text)
    print()
    print('  ### THE PAGE, AT INDEX %d (the article\'s page 21).' % PAGE_INDEX)
    print('  text-layer characters      : %d' % len(text))
    print('  ### TEXT LAYER STOPS DEAD  : %s'
          % ('YES, at line %d' % cut if cut is not None else 'no'))
    if cut is not None:
        lines = text.splitlines()
        print('      the truncated line     : %r' % lines[cut])
        nxt = lines[cut + 1] if cut + 1 < len(lines) else '<end of page>'
        print('      what follows it        : %r' % nxt)
        print('  ### **THE CONDITION IS NOT IN THE TEXT LAYER. ### THAT IS THE CORPUS\'S OLD')
        print('  ### DEFECT, MEASURED IN THE ARTEFACT RATHER THAN RECALLED FROM b197.**')

    # ### THE CONTROL: ### **A NEIGHBOURING PAGE MUST NOT SHOW THE SAME TRUNCATION**, or the
    # ### detector is describing the corpus rather than this page.
    ctl = truncated_at(r.pages[PAGE_INDEX + 1].extract_text() or '')
    print('  CONTROL, the next page     : truncated=%s   %s'
          % (ctl is not None, 'PASS -- the finding is this page\'s' if ctl is None
             else '### the detector fires broadly; treat the finding as weak'))

    imgs = list(page.images)
    print()
    print('  embedded images on the page : %d' % len(imgs))
    if not imgs:
        print('  ### HARD FAILURE -- NO PAGE IMAGE TO CUT. THE READ CANNOT BE MADE.')
        return 2
    img = Image.open(io.BytesIO(imgs[0].data)).convert('L')
    w, h = img.size
    print('  page image                  : %s  %dx%d' % (imgs[0].name, w, h))

    box = (int(w * CROP[0]), int(h * CROP[1]), int(w * CROP[2]), int(h * CROP[3]))
    crop = img.crop(box)
    crop = crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)
    full_path = os.path.join(outdir, 'b303_vN_p21_full.png')
    cut_path = os.path.join(outdir, 'b303_vN_p21_def331.png')
    img.save(full_path)
    crop.save(cut_path)
    print('  crop box (px)               : %s' % (box,))
    print('  full page written           : %s  sha256 %s'
          % (os.path.basename(full_path), sha256_file(full_path)[:32]))
    print('  ### DEFINITION 3.3.1 CUT    : %s  sha256 %s'
          % (os.path.basename(cut_path), sha256_file(cut_path)[:32]))
    print()
    print('  ### **THIS TOOL DID NOT READ THE IMAGE AND RUNS NO OCR.** ### The quotation banked')
    print('  ### by this act is a HUMAN READ of the file named above. ### An instrument that both')
    print('  ### cut the page and reported its words would be the only witness to its own claim.')
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
