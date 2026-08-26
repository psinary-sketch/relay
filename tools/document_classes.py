# -*- coding: utf-8 -*-
"""document_classes.py -- THE DOCUMENT-CLASS CHECK, AGAINST THE STANDING TAXONOMY.

### REWRITTEN 2026-08-26 (b190). ### IT NOW READS THE CORPUS'S OWN AUTHOR-RULED TIERS,
### NOT AN INVENTED SCHEME.

### THE HISTORY, KEPT BECAUSE IT IS THE REASON THIS FILE EXISTS IN THIS FORM.
### b186 built this checker around SYNTHESIS / NOTES / LEDGER -- classes it derived from
### the corpus's BEHAVIOUR without searching for a STANDARD. ### THE STANDARD EXISTED:
### phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md, ### "Standing standard, 2026-07-28
### (Tier E added 2026-08-08, AUTHOR-RULED)".
### ### AND THE INVENTED SCHEME DID NOT MERELY DUPLICATE IT -- ITS "SYNTHESIS" CLASS
### ### SPANNED TIER K AND TIER C AT ONCE, COLLAPSING THE ONE DISTINCTION THE STANDING
### ### TAXONOMY EXISTS TO ENFORCE: "a synthesis being read as a certification."
### ### A STANDARD INVENTED BESIDE A STANDING ONE IS NOT A SECOND STANDARD. IT IS A
### ### CONFLICT.
### b186's scheme is RETIRED (b190), additively -- its class lines stay legible in the
### documents beneath the new ones.

### THE FOUR TIERS, AS THE STANDING TAXONOMY DEFINES THEM (quoted, not paraphrased):
###   K -- keystone-certified; claims backed by a machine-checked kernel terminal at a
###        pin. "may be cited as certification".
###   C -- cluster-synthesis; organizes certified results, asserts relationships NOT
###        individually certified. "cite for orientation ... NEVER as certification".
###   N -- notes / exploratory. "reference-only -- not citable as established".
###   E -- filing-facing; for counsel or a patent examiner. "Tier E cites Tier K;
###        NOTHING CITES TIER E."

### THE LEDGERS ARE **NOT PLACED**, AND THAT IS A RESULT, NOT AN OMISSION (b190).
### A Tier-E placement was ruled and then REFUSED AT CONTENT: Tier E is defined by
### audience; its rule is "nothing cites Tier E" while the ledgers are cited by every
### act; its membership is an author-ruled enumeration the ledgers are not in; and the
### taxonomy exists to prevent "a filing-facing framing being read as the record" --
### which placing the record there would invert.
### ### AND THE STANDING TAXONOMY ALREADY TREATS A LEDGER AS A **VENUE**, NOT A CLASS:
### ### Tier N's admission clause leaves unearned work "loom-resident (ledger lines)".
### Their home is ROUTED to the author; this checker accepts ROUTED as a declared state
### and does NOT invent a tier for them.

# ### THE LIMITS, IN THE HEADER SO THE CHECK IS NOT TRUSTED BEYOND THEM:
# ### (1) ### THE TIER IS DECLARED BY THE DOCUMENT, NOT DERIVED BY THIS TOOL. A document
# ###     declaring TIER K while carrying no terminal is checked against the wrong
# ###     standard and ### NO INSTRUMENT HERE CAN TELL. (b186's M11, unchanged by the
# ###     rewrite -- ### CHANGING WHICH VOCABULARY IS READ DOES NOT MAKE A DECLARATION
# ###     TRUE.)
# ### (2) ### IT DOES NOT ENFORCE THE TIERS' **OBLIGATIONS** -- it does not check that a
# ###     Tier-K document states grade . terminal . pin, nor that a Tier-C document flags
# ###     coordinates. ### IT CHECKS THAT A TIER IS DECLARED, NOT THAT IT IS EARNED.
# ### (3) ### IT CANNOT SEE WHAT THE ROSTER OMITS -- b189's M14. The instrument reads the
# ###     roster; ### AN INCOMPLETE ROSTER YIELDS A CLEAN CHECK OVER THE WRONG SET.

#
# ### AND THE BUILD NOTE, NOW AT ITS **THIRD** INSTANCE: this file's first run died on an
# ### UNCLOSED MODULE DOCSTRING -- as b179's pre-commit hook did, and as b185's
# ### registration gate did. ### THREE TIMES, IN THE SAME SHAPE, IN TWELVE ACTS.
# ### b185's note called it "a habit, not an accident" and that was not enough to stop it.
# ### ALL THREE WERE CAUGHT INSTANTLY BY THE INTERPRETER, SO NONE SHIPPED -- ### AND A
# ### DEFECT CAUGHT BY THE LANGUAGE IS NOT A DEFECT THE OPERATOR HAS LEARNED FROM.
"""

import io
import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ROSTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mirror_roster.json')

TIER = re.compile(r'DOCUMENT CLASS\s*—\s*THE STANDING TAXONOMY[^\n]*?'
                  r'(?:TIER\s+([KCNE])\b|NOT PLACED\s*—\s*(ROUTED))', re.I)
RETIRED = re.compile(r"b186's SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED", re.I)


def roster():
    return list(json.loads(io.open(ROSTER, encoding='utf-8-sig').read())['files'])


def scan(rel):
    p = os.path.join(REPO, rel)
    if not os.path.exists(p):
        return None
    t = io.open(p, encoding='utf-8', errors='replace').read()
    m = TIER.search(t)
    tier = None
    if m:
        tier = (m.group(1) or m.group(2) or '').upper()
    return {'path': rel.replace('\\', '/'), 'tier': tier, 'retired': bool(RETIRED.search(t))}


def check(rows):
    msg = []
    if not rows:
        # ### THE ZERO CASE. b167's law: a verdict over an empty scope is not a verdict.
        msg.append("### HARD FAILURE -- EMPTY ROSTER. Nothing examined, so nothing verified.")
        msg.append("### An empty set trivially has no undeclared document. THAT IS NOT A PASS.")
        return 2, msg
    und = [r for r in rows if not r['tier']]
    tally = {}
    for r in rows:
        if r['tier']:
            tally[r['tier']] = tally.get(r['tier'], 0) + 1
    msg.append("  documents examined     : %d" % len(rows))
    msg.append("  tiers declared         : %s"
               % ("  ".join("%s=%d" % (k, tally[k]) for k in sorted(tally)) or "none"))
    msg.append("  ### WITHOUT a declared tier: %d" % len(und))
    for r in und[:8]:
        msg.append("      ### UNDECLARED : %s" % r['path'])
    if und:
        msg.append("  ### HARD FAILURE -- documents in the roster declare no tier of the")
        msg.append("  ### STANDING taxonomy. A document with no declared tier is not in the")
        msg.append("  ### restart kit.")
        return 1, msg
    msg.append("  VERDICT : CLEAN")
    msg.append("  ### and that means ONE thing: every roster document declares a tier of")
    msg.append("  ### the corpus's own author-ruled standard, or is ROUTED.")
    msg.append("  ### IT IS NOT A REVIEW OF WHETHER THE DECLARATIONS ARE TRUE, AND IT DOES")
    msg.append("  ### NOT CHECK THE TIERS' OBLIGATIONS.")
    return 0, msg


def main(argv):
    rows = [r for r in (scan(x) for x in roster()) if r]
    if '--check' in argv:
        code, msg = check(rows)
        print("--- DOCUMENT-CLASS CHECK (b186; rewritten to the STANDING taxonomy, b190) ---")
        for l in msg:
            print(l)
        return code
    print("=" * 78)
    print("DOCUMENT CLASSES -- THE ROSTER UNDER THE STANDING TAXONOMY (K/C/N/E)")
    print("=" * 78)
    for r in sorted(rows, key=lambda x: (x['tier'] or 'ZZ', x['path'])):
        print("  %-6s %-58s retired-line=%s"
              % (r['tier'] or '###--', r['path'][:58], 'yes' if r['retired'] else 'no'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
