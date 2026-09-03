# -*- coding: utf-8 -*-
"""b302_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the `ferry_scan.py`
### design point: a second copy is a second thing to keep in step with ruling (1), and the drift
### would be invisible until the two disagreed on a registration.

### ### **AND THIS ACT'S CAPS ARE NOT ALL ZEROS, WHICH IS THE POINT.** ### b301's shadow check
### found a buildable candidate and b301's own sealed cap of ### ZERO ### `.lean` files forbade
### building it. ### The order for this act says the caps must be written so they do not forbid the
### ordered build. ### **A CEILING IS STILL A CEILING: `CAP 1` MEANS ONE MODULE, AND THE CLOSING
### RE-MEASURES WHAT ACTUALLY LANDED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b302_registration_2026-09-02.txt')
SPEC = os.path.join(ROOT, 'data', 'b302_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` files created", 1, 1, "files",
     "THE ORDERED BUILD: one module, the rational enclosure. ### RE-MEASURED IN THE CLOSING BY"
     " `b302_checks.py`'s G-KERNEL against the kernel repo's working tree."),
    ("`.lean` files modified", 1, 1, "files",
     "`AllPrints.lean` must import the module IN THE SAME COMMIT THAT CREATES IT (b289's scar)."
     " ### RE-MEASURED IN THE CLOSING."),
    ("profile files rewritten", 1, 1, "files",
     "`AXIOM_PRINTS.txt`, regenerated from source rather than copied (b298's D3: a copy is not a"
     " regeneration). ### RE-MEASURED IN THE CLOSING."),
    ("byte-order marks prepended to the profile", 0, 0, "bytes",
     "b298's (D5): a PowerShell redirection prepended a UTF-8 BOM; both of that act's checks agreed"
     " and neither could see it, and the commit's own numstat is what caught it. ### **A CAP THIS"
     " RECORD HAS EARNED.** ### RE-MEASURED IN THE CLOSING BY READING THE FIRST BYTES AS BYTES."),
    ("pre-existing prints altered", 0, 0, "prints",
     "W6: the pre-existing profile must survive BYTE-WISE AS A TRUE PREFIX against `git HEAD`,"
     " never compared line by line. ### RE-MEASURED IN THE CLOSING."),
    ("PLACE-papers files written", 0, 0, "files",
     "THE SCOPE CLAUSE: no papers file is written, so no hook and no mirror. ### RE-MEASURED IN"
     " THE CLOSING BY `b302_checks.py`'s G-NOPAPERS, with the pre-existing untracked row measured"
     " against this registration's own seal time."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / W-ORD-ADHOC-CHECK-FIXTURES (b298). ### RE-MEASURED IN THE CLOSING BY"
     " `b302_checks.py`'s G-TOOLNUM."),
]


def main(argv):
    print('=' * 100)
    print('b302_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2

    text = io.open(REG, encoding='utf-8').read()
    n, hits = CNT.count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))

    clauses = [{"clause": c, "cap": cap, "demand": dem, "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    clauses.append({
        "clause": "artifact counts predicted in this registration",
        "cap": 0, "demand": n, "units": "predictions",
        "from": "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the"
                " counter `b300_regspec.count_predictions`, IMPORTED rather than copied."})

    spec = {"registration":
            "data/b302_registration_2026-09-02.txt -- b302, THE UNIT REQUIREMENT",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)

    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and back['clauses'][-1]['demand'] == n
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CAPS THAT ARE NOT ZERO (the ordered build\'s room) : %s' % ', '.join(nonzero))
    print('  ### **AND THEY ARE STILL CEILINGS. ### THE CLOSING RE-MEASURES WHAT LANDED.**')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
