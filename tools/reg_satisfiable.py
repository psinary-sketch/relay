# -*- coding: utf-8 -*-
"""reg_satisfiable.py -- THE REGISTRATION JOINT-SATISFIABILITY CHECK (built b265).

### WHY THIS EXISTS, AND IT IS A DEFECT REPORT BEFORE IT IS A TOOL.
### At b264 the registration's clause (I) declared **"NO SINGLE ALLOCATION ABOVE 256 MB"** and
### its clause (I) ALSO registered a ladder to `x >= 1000` under an `NG = max(400, ceil(8x))`
### law with an `NG` vs `2 NG` convergence test. ### **THOSE TWO CLAUSES CANNOT BOTH BE
### HONOURED**: the rule builder allocates `8 * NG^2` bytes, which passes 256 MB at `NG = 5793`,
### i.e. at the ladder's OWN `x = 500` convergence cell. ### The registration was SEALED in that
### state and the contradiction was discovered only when the run died against it.
### ### **NOTHING IN THE CLOSING SEQUENCE COMPARED A DECLARED CEILING AGAINST THE WORK THE SAME
### ### REGISTRATION ORDERED.** ### b264 filed `W-ORD-GL-PANEL` with the order: *"fix the
### registration template so a declared memory ceiling is checked against the ladder it
### registers, BEFORE the seal."* ### This is that check.

### WHAT IT DOES. It takes a JSON list of CLAUSE PAIRS -- a declared cap and the demand the same
### registration's own parameters imply -- and reports each as SATISFIABLE or CONTRADICTORY, with
### the arithmetic shown. ### **THE DEMANDS ARE SUPPLIED BY THE ACT, NOT INFERRED BY THE TOOL.**
"""

# ### THE LIMIT OF THIS CHECK, STATED IN ITS OWN HEADER BECAUSE A CHECK WHOSE REACH IS NOT
# ### STATED WILL BE TRUSTED BEYOND IT.
# ### ### **IT CANNOT FIND A CLAUSE THE ACT DID NOT THINK TO DECLARE.** It compares the pairs it
# ### is given. A ceiling whose demand the act never computed is invisible to it, exactly as
# ### b264's was invisible to every check b264 owned. ### **IT NARROWS THE CLASS; IT DOES NOT
# ### CLOSE IT.** The act must still enumerate its own ceilings, and THAT enumeration is the
# ### step this tool cannot perform.
import io
import json
import sys


def main(argv):
    if not argv:
        sys.stderr.write("usage: reg_satisfiable.py <spec.json> [--emit <act>]\n")
        return 2
    spec = json.load(io.open(argv[0], encoding='utf-8'))
    rows = spec['clauses']
    out = []

    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("REGISTRATION JOINT-SATISFIABILITY CHECK (reg_satisfiable.py, b265) -- RUN, NOT CLAIMED")
    rec("=" * 100)
    rec("  registration : %s" % spec.get('registration', '(unnamed)'))
    rec("  clauses      : %d" % len(rows))
    rec("")
    rec("  %-34s %-16s %-16s %-6s %s" % ('clause', 'declared cap', 'demand implied', 'units', 'verdict'))
    rec("  " + "-" * 96)
    bad = 0
    for r in rows:
        cap, dem = float(r['cap']), float(r['demand'])
        ok = dem <= cap
        if not ok:
            bad += 1
        rec("  %-34s %-16.6g %-16.6g %-6s %s"
            % (r['clause'][:34], cap, dem, r.get('units', ''),
               'SATISFIABLE' if ok else '### CONTRADICTORY ###'))
        rec("      demand from : %s" % r.get('from', '(not stated)'))
        if not ok:
            rec("      ### **THIS REGISTRATION CANNOT BE HONOURED AS WRITTEN. ### DO NOT SEAL.**")
    rec("")
    if bad:
        rec("  VERDICT          : ### NOT SATISFIABLE -- %d CONTRADICTORY CLAUSE(S). DO NOT SEAL." % bad)
    else:
        rec("  VERDICT          : ### JOINTLY SATISFIABLE -- every declared cap covers the demand")
        rec("  ###                its own registration implies. ### SAFE TO SEAL ON THIS AXIS.")
    rec("  ### REACH: it compares the pairs it is GIVEN. ### A ceiling whose demand the act")
    rec("  ### never computed is invisible to it, exactly as b264's was invisible to b264.")
    rec("  ### **IT NARROWS THE CLASS; IT DOES NOT CLOSE IT.**")

    if '--emit' in argv:
        i = argv.index('--emit')
        act = argv[i + 1] if i + 1 < len(argv) else 'unknown'
        path = r'D:\relay\data\audit_%s_reg_satisfiable.txt' % act
        io.open(path, 'w', encoding='utf-8').write("\n".join(out) + "\n")
        sys.stderr.write("  emitted: %s\n" % path)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
