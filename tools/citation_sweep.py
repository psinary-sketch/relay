# -*- coding: utf-8 -*-
"""b175 -- THE CITATION SWEEP's enumerator. RUN, NOT CLAIMED.

### Scans the LIVE documents only. `archive/` and `.git/` are excluded BY NAME and the
### exclusion is printed, because a filter that hides what it does not excuse is worse
### than no filter (banned_terms.py's own law, applied here).

Three classes are enumerated:
  (A) AUTHOR SHORTHANDS  -- initials or surnames possessive, standing where a work-key
      should stand ("CC's X", "Connes's Y").
  (B) NUMBERED RESULTS CITED WITHOUT A WORK -- "Lemma 5.4", "Thm 4.7", "Prop 5.5" with no
      bibliography key on the same line.
  (C) BARE ARXIV/DOI POINTERS -- a key that IS a bibliography key is fine; one that is not
      is reported.

### THE ENUMERATOR DECIDES NOTHING. It locates. Identification and grading are the act's,
### done at content, and the renderer law governs any absence it records.
"""
import io, os, re, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PP = r"D:\MY-DOwnloads\PLACE-papers"
EXCLUDE_DIRS = ('.git', 'archive')

SHORTHAND = re.compile(r"\b(CC|CCM|CM|C\-C)'s\b")
NUMBERED = re.compile(r"\b(Lemma|Lem\.|Theorem|Thm\.?|Proposition|Prop\.?|Corollary|Cor\.?|"
                      r"Remark|Definition|Def\.?)\s*([0-9]+(?:\.[0-9]+)*)\b")
ARXIVKEY = re.compile(r"\b(\d{4}\.\d{4,5}|math/\d{7})\b")
DOIKEY = re.compile(r"\b10\.\d{4,9}/[^\s`)|]+")


def bib_keys(path):
    t = io.open(path, encoding='utf-8').read()
    return set(ARXIVKEY.findall(t)) | set(k.rstrip('.,;`|') for k in DOIKEY.findall(t))


def bib_surnames(path):
    """### The author vocabulary is taken FROM THE CORPUS'S OWN BIBLIOGRAPHY, not from a
    list this tool invents: capitalised surnames appearing in its author fields."""
    t = io.open(path, encoding='utf-8').read()
    names = set(re.findall(r"\b([A-Z][a-z]{3,})(?=[–—,\s]*(?:[A-Z][a-z]{3,}|,|\*|\|))",
                           t))
    drop = {'The', 'This', 'That', 'Title', 'Corpus', 'Enters', 'External', 'Retrieval',
            'Prolate', 'Zeta', 'Spectral', 'Triples', 'Weil', 'Trace', 'Number', 'Theory',
            'Journal', 'None', 'Both', 'Line', 'With', 'Read', 'Held', 'Three', 'What',
            'Wherever', 'Their', 'From', 'Into', 'Only', 'Same', 'Under', 'Where', 'Which'}
    return sorted(n for n in names - drop if len(n) >= 5)


def live_files(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for f in filenames:
            if f.endswith('.md'):
                out.append(os.path.join(dirpath, f))
    return sorted(out)


def main():
    global SURNAMES
    keys = bib_keys(os.path.join(PP, 'BIBLIOGRAPHY.md'))
    SURNAMES = bib_surnames(os.path.join(PP, 'BIBLIOGRAPHY.md'))
    files = live_files(PP)
    print("=" * 92)
    print("THE CITATION SWEEP -- ENUMERATION (citation_sweep.py, b175) -- RUN, NOT CLAIMED")
    print("=" * 92)
    print("  root              : %s" % PP)
    print("  EXCLUDED BY NAME  : %s   ### stated, never silent" % ", ".join(EXCLUDE_DIRS))
    print("  live .md files    : %d" % len(files))
    print("  bibliography keys : %d" % len(keys))
    print("  author vocabulary : %d surnames, taken FROM THE BIBLIOGRAPHY ITSELF" % len(SURNAMES))
    print("     %s" % ", ".join(SURNAMES[:14]) + (" ..." if len(SURNAMES) > 14 else ""))
    print()

    A, B, C = [], [], []
    for f in files:
        rel = os.path.relpath(f, PP).replace('\\', '/')
        for n, line in enumerate(io.open(f, encoding='utf-8'), 1):
            has_key = bool(ARXIVKEY.search(line) or DOIKEY.search(line))
            for m in SHORTHAND.finditer(line):
                A.append((rel, n, m.group(0), line.strip()[:96]))
            ### THE FIRST RUN OF THIS CLASS RETURNED 742 AND WAS OVER-BROAD: it caught the
            ### corpus's OWN theorem numbering ("Theorem 1 (Valence-Fano)"). A numbered
            ### result is only a CITATION when it is attributed OUTSIDE. So the class now
            ### requires an external-attribution cue on the line -- an author shorthand or
            ### a surname drawn from the bibliography's own author vocabulary.
            ### A CHECK'S FIRST RUN IS PART OF ITS CONSTRUCTION (the nursery convention).
            attributed = bool(SHORTHAND.search(line)) or any(s in line for s in SURNAMES)
            for m in NUMBERED.finditer(line):
                if attributed and not has_key:
                    B.append((rel, n, "%s %s" % (m.group(1), m.group(2)), line.strip()[:96]))
            for m in ARXIVKEY.finditer(line):
                if m.group(1) not in keys:
                    C.append((rel, n, m.group(1), line.strip()[:96]))

    for name, rows in (("(A) AUTHOR SHORTHANDS STANDING WHERE A WORK-KEY SHOULD", A),
                       ("(B) NUMBERED RESULTS CITED WITH NO KEY ON THE LINE", B),
                       ("(C) ARXIV POINTERS THAT ARE NOT BIBLIOGRAPHY KEYS", C)):
        print("-" * 92)
        print("%s : %d" % (name, len(rows)))
        print("-" * 92)
        bydoc = {}
        for rel, n, what, txt in rows:
            bydoc.setdefault(rel, []).append((n, what, txt))
        for rel in sorted(bydoc):
            print("  %s  (%d)" % (rel, len(bydoc[rel])))
            for n, what, txt in bydoc[rel]:
                print("     :%-5d %-22s %s" % (n, what, txt))
        print()

    print("=" * 92)
    print("  TOTALS: shorthands %d | numbered-without-key %d | non-key pointers %d"
          % (len(A), len(B), len(C)))
    print("  ### THE ENUMERATOR DECIDES NOTHING. Identification and grading are the act's,")
    print("  ### done at content; and any ABSENCE is established at the source document,")
    print("  ### never at a rendering (the renderer law, b174).")
    print("=" * 92)
    return A, B, C


if __name__ == '__main__':
    main()
