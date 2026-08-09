"""Source-only generate for rowgen — the diff without a build.

WHY THIS EXISTS. `rowgen generate` calls `lake env lean` for every terminal to obtain `#check` and
`#print axioms`. With 90 terminals across 14 kernels, most of which have no `.lake` built, that is
90 subprocess calls at a 600 s timeout — not runnable in a sitting, and the failures would be
indistinguishable from missing terminals.

FOUR OF THE DIFF'S FIVE CHECKS NEED NO BUILD. `doc`, `body1` and `defenc` all come from
`git show <pin>:<file>`, so status-vs-docstring contradictions, definition-encoded-graded-DERIVES,
stale pins and missing terminals are all decidable from source alone. **Only the rounded-profile
check needs the axioms**, and this script leaves that field empty rather than guessing it — an
absent profile is reported as absent, never as clean.

RESOLUTION IS BY PIN, NOT BY WORKING TREE. The sitting-1 defect: an `os.walk` resolver cannot audit
a corpus that cites pins on other branches (it reported three real terminals missing because they
live on `derivative-engine`). Everything here goes through `git show <pin>:<file>`.
"""
import io, json, os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rowgen


def main(cfg_path, out_path):
    cfg = json.load(io.open(cfg_path, encoding="utf-8"))
    records, missing, unpinned = [], [], []
    for t in cfg:
        repo, pin = t["repo"], t.get("pin", "HEAD")
        name, f = t["name"], t.get("file", "")
        src = rowgen.git_show(repo, pin, f) if f else ""
        if not src:
            missing.append((name, repo, pin, f))
            records.append({"name": name, "repo": os.path.basename(repo), "pin": pin,
                            "exists": False, "check": "", "axioms": "", "doc": "",
                            "body1": "", "defenc": False, "defenc_why": "",
                            "source_only": True})
            continue
        doc, body1 = rowgen.extract_doc_body(src, name)
        defenc, why = rowgen.definition_encoded(src, "")
        last = name.split(".")[-1]
        declared = any(
            ln.strip().startswith(k + " " + last) or ln.strip().startswith(k + " " + last + " ")
            for ln in src.splitlines()
            for k in ("theorem", "lemma", "def", "abbrev", "structure", "instance",
                      "noncomputable def")
        )
        if not declared:
            unpinned.append((name, repo, pin, f))
        records.append({"name": name, "repo": os.path.basename(repo), "pin": pin,
                        "exists": declared, "check": "", "axioms": "", "doc": doc,
                        "body1": body1, "defenc": defenc, "defenc_why": why,
                        "source_only": True})
    io.open(out_path, "w", encoding="utf-8").write(json.dumps(records, indent=1))
    print("records written: %d  ->  %s" % (len(records), os.path.basename(out_path)))
    print("  file unreachable at pin : %d" % len(missing))
    print("  declaration not found in that file at that pin : %d" % len(unpinned))
    for n, r, p, f in unpinned[:20]:
        print("     %-46s %s @ %s :: %s" % (n, os.path.basename(r), p, f))
    print()
    print("  NOTE: `axioms` is EMPTY in every record by construction. The rounded-profile check")
    print("  is therefore NOT EXERCISED by this pass and must not be reported as passing.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
