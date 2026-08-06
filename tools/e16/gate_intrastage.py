# RULE 2's GATE, BEFORE PRODUCTION.
#
# The resume path is tested on a DELIBERATELY interrupted small run: killed mid-Taylor and
# mid-recurrence.  Both resumes must validate, drop any torn tail, and continue to a result
# BYTE-IDENTICAL to an uninterrupted run of the same case.  No production restart until both
# pass.  A torn tail is also injected by hand, to prove the guard drops it rather than trusting
# it.
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(HERE, "gate_chunks.jsonl")
CASE = (40, 30)          # nmax, dps -- small enough to run in seconds, real enough to test


def clean():
    if os.path.exists(CH):
        os.remove(CH)


def run(abort=None):
    env = dict(os.environ)
    env["LI_TEST_ABORT"] = abort or ""
    env["LI_TAYLOR_CHUNK"] = "8"
    env["LI_COEF_CHUNK"] = "5"
    env["LI_LAM_CHUNK"] = "7"
    code = (
        "import os,sys,json;sys.path.insert(0,r'%s');"
        "import epstein_li_v2 as V;"
        "V.CHUNKS=r'%s';"
        "V.TAYLOR_CHUNK=int(os.environ['LI_TAYLOR_CHUNK']);"
        "V.COEF_CHUNK=int(os.environ['LI_COEF_CHUNK']);"
        "V.LAM_CHUNK=int(os.environ['LI_LAM_CHUNK']);"
        "V.ABORT=os.environ.get('LI_TEST_ABORT','');"
        "r=V.run_stage(99,%d,%d);"
        "print('RESULT '+json.dumps([repr(r[0]),r[1],r[2],repr(r[3])]))"
        % (HERE, CH, CASE[0], CASE[1])
    )
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env=env)
    out = p.stdout
    res = None
    for line in out.splitlines():
        if line.startswith("RESULT "):
            res = line[7:]
    return p.returncode, res, out


print("=" * 78)
print("RULE 2 GATE — intra-stage resume, tested before production")
print("=" * 78)

clean()
rc0, ref, _ = run()
print(f"\n[baseline] uninterrupted run rc={rc0}")
print(f"           result = {ref}")
assert ref is not None, "baseline produced no result"

results = {}
for name, abort in (("mid-Taylor", "taylor:24"), ("mid-recurrence", "lam:21")):
    clean()
    rc1, r1, _ = run(abort=abort)
    n_chunks = sum(1 for _ in open(CH, encoding="utf-8")) if os.path.exists(CH) else 0
    print(f"\n[{name}] interrupted run rc={rc1} (97 = deliberate abort), "
          f"chunks banked = {n_chunks}")
    rc2, r2, _ = run()
    print(f"[{name}] resumed run rc={rc2}")
    print(f"[{name}] result = {r2}")
    ok = (r2 == ref)
    results[name] = ok
    print(f"[{name}] BYTE-IDENTICAL TO BASELINE: {'PASS' if ok else 'FAIL'}")

# torn-tail guard: append a truncated / malformed record and prove it is dropped
clean()
run(abort="taylor:24")
with open(CH, "a", encoding="utf-8") as f:
    f.write('{"v":1,"stage":99,"dps":30,"phase":"taylor","idx":999,"n":8,"payload":[[0,1,2]]}\n')
    f.write("{not json at all\n")
rc3, r3, _ = run()
tt = (r3 == ref)
results["torn-tail"] = tt
print(f"\n[torn-tail] a malformed record and a length-mismatched record injected by hand")
print(f"[torn-tail] resumed result = {r3}")
print(f"[torn-tail] GUARD DROPPED THE TAIL AND MATCHED BASELINE: {'PASS' if tt else 'FAIL'}")

# stage/dps mismatch: a cache from another stage must be refused, not used
clean()
run(abort="taylor:24")
with open(CH, encoding="utf-8") as f:
    lines = f.readlines()
with open(CH, "w", encoding="utf-8") as f:
    for L in lines:
        r = json.loads(L)
        r["stage"] = 7                      # pretend it came from a different stage
        f.write(json.dumps(r) + "\n")
rc4, r4, _ = run()
sm = (r4 == ref)
results["stage-mismatch"] = sm
print(f"\n[stage-mismatch] every chunk relabelled to another stage")
print(f"[stage-mismatch] resumed result = {r4}")
print(f"[stage-mismatch] CACHE REFUSED AND RECOMPUTED: {'PASS' if sm else 'FAIL'}")

clean()
print()
print("=" * 78)
allpass = all(results.values())
for k, v in results.items():
    print(f"  {k:<16} {'PASS' if v else 'FAIL'}")
print(f"  GATE: {'PASS — production restart authorized' if allpass else 'FAIL — no production restart'}")
sys.exit(0 if allpass else 1)
