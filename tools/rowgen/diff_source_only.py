"""Run rowgen's diff against precomputed source-only records.

`rowgen.py diff` calls `generate()` itself, which means a lake build per terminal. This driver feeds
it records produced by `gen_source_only.py` instead, so the four build-free checks run now and the
rounded-profile check is explicitly reported as NOT EXERCISED rather than silently passing.
"""
import io, json, os, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rowgen

recs = json.load(io.open(sys.argv[1], encoding="utf-8"))
papers = sys.argv[2:]
total = 0
for p in papers:
    md = io.open(p, encoding="utf-8").read()
    flags = rowgen.diff(recs, md)
    name = os.path.basename(p)
    print("=== %-40s %d flag(s) ===" % (name, len(flags)))
    for f in flags:
        print("   ", f if isinstance(f, str) else " | ".join(str(x) for x in f))
    total += len(flags)
print()
print("TOTAL FLAGS: %d across %d papers" % (total, len(papers)))
print("NOT EXERCISED: the rounded-profile check (records carry no axioms field by construction).")
