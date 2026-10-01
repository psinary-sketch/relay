# SUITE_README -- how an act's control suite reads the face's write list

Filed at b565 under the author's ruling `(R175)`(5), for b564's defect (h). It describes what the suites already do (the
reader `globs_of`, carried from b558 through `tools/b564_checks.py`) and the one rule b564 added; it binds a face's author,
and the suite that reads the face.

## THE WRITE LIST TAKES GLOBS

- A face's `(W) THE WRITE LIST` section names every KIND of file the act may write, each as a backticked path in a table row.
- The suite reads that section with `globs_of(face)`: every backticked token of path characters, taken by its last path
  component, is a glob (`fnmatch`), and a token whose last component is a bare wildcard is expanded to the files that
  directory holds.
- `*`, `?` and `[...]` are globs in the usual sense. The act's own stem is written `relay/data/bNNN_*`, `relay/tools/bNNN_*`.
- **A `<...>` placeholder in a backticked path is read as `*`** (b564, defect (h): a face wrote `Chi/<name>.lean`, and the
  reader, keeping only tokens of path characters, dropped the row).
- A token with a space, or longer than 120 characters, is not a glob; prose in backticks is ignored.

## WHAT THE READ IS FOR

`G-WRITELIST-KINDS` collects every file the act wrote -- the files of every act commit in the five repositories, and the
working tree's modified files (by file time before the push, by content digest against the pushed tree after it) -- and
fails on any file no glob of the face covers. A face therefore names each kind it writes, and names it in a form the reader
can read: a glob or a placeholder, never a description in words alone.

## THE AS-OF LINES (R179)(3), THREE FORMS (R180)(2)(d)

Filed at b570. A suite re-run after its successor reads each repository at the head its act's as-of line names, from the
act's closing push-out bank (written there by `tools/asof_lines.py` after the closing push) or, for an act closed before
the lines existed, from a companion bank `data/bNNN_asof_<act>.txt`. The reader is `tools/asof.py` (`repo_asof`). The form
list is three:

- `push_gated: as-of <repository> <40-hex sha>` -- the repository's closing head (main equal to its remote main);
- `push_gated: as-of <repository> deleted at close` -- a clone removed by ruling at that close, read as absent;
- `push_gated: as-of <name> present at close` -- a directory that is not a repository, present at that close (b569's
  defect (d), kept by (R180)(2)(d)).

Anything after the head, from `###` on, is a source note and is not read. A name given twice refuses the whole bank.
