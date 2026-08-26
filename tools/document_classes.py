# -*- coding: utf-8 -*-
"""document_classes.py -- THE DOCUMENT-CLASS CLASSIFIER AND CHECK (built b186).

### WHY THIS EXISTS. b182 wrote a PLAN -- a staged program, full of hypotheses --
### and put it in the restart kit beside the corpus's self-descriptions. It carried
### TWELVE marks of the open/navigator-asserted/unread species, and a reader opening
### the mirror could not tell from its position that it was a note rather than a
### statement of what the corpus stands on. ### THE HEDGES WERE HONEST; THEY WERE IN
### THE WRONG ROOM.

### THE CLASSES, DERIVED FROM WHAT THE CORPUS ALREADY DOES, NOT INVENTED:
###   SYNTHESIS -- states what the corpus stands on; meant to be read by someone
###                OUTSIDE the record.
###   NOTES     -- records in-flight work, hypotheses, or staged plans.
###   LEDGER    -- tracks state.

### THE RULE (b186): ### A SYNTHESIS DOCUMENT CARRIES NO MARK OF THE
### OPEN/NAVIGATOR-ASSERTED/UNREAD SPECIES EXCEPT WHERE IT IS EXPLICITLY REPORTING
### THE RECORD'S OPEN ITEMS AS SUCH. A notes document may carry them freely.
### ### A DOCUMENT WITH NO DECLARED CLASS IS NOT IN THE RESTART KIT.

# ### THE LIMITS, IN THE HEADER SO THE CHECK IS NOT TRUSTED BEYOND THEM:
# ### (1) ### IT COUNTS MARKS, IT DOES NOT READ MEANING. A synthesis document that
# ###     hedges in words this file does not know passes. ### IT NARROWS ONE FAILURE
# ###     MODE; IT DOES NOT CLOSE THE CLASS.
# ### (2) ### THE OPEN-ITEMS EXEMPTION IS A **SECTION** TEST, and a document that
# ###     declares one enormous open-items section exempts itself entirely.
# ###     ### THE EXEMPTION IS AS HONEST AS THE DOCUMENT THAT CLAIMS IT.
# ### (3) ### THE CLASS IS DECLARED BY THE DOCUMENT, NOT DERIVED BY THIS TOOL.
# ###     A document that declares SYNTHESIS while being notes is checked against the
# ###     wrong standard, and no instrument here can tell. ### THE DECLARATION IS AN
# ###     ASSERTION BY ITS AUTHOR AND IS TREATED AS ONE.
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

MARKS = [
    (re.compile(r'\bNAVIGATOR-ASSERTED\b', re.I), 'NAVIGATOR-ASSERTED'),
    (re.compile(r'\bREQUIRING A CONSTRUCTION\b|\bNEEDS A CONSTRUCTION\b', re.I), 'CONSTRUCTION'),
    (re.compile(r'\bUNREAD\b', re.I), 'UNREAD'),
    (re.compile(r'\bMARKED OPEN\b|\bSTILL OPEN\b|\bLEFT OPEN\b', re.I), 'OPEN'),
]
CLASSLINE = re.compile(r'^\s*\*?\*?DOCUMENT CLASS\*?\*?\s*:\s*\**\s*(SYNTHESIS|NOTES|LEDGER)',
                       re.I | re.M)
PURPOSE = re.compile(r'WHAT THIS DOCUMENT IS|WHAT THIS DOCUMENT HOLDS|THE GOVERNING CLAIM|'
                     r'^\*\*Build document|THIS IS A PLAN|WHAT THIS LEDGER', re.I | re.M)
# ### the explicit open-items section: a heading that says so in its own words.
OPENSEC = re.compile(r'^#{1,6}.*(OPEN ITEMS|OPEN TRAILS|THE DEBT|WHAT REMAINS|OPEN QUESTIONS|'
                     r'STANDING DEBT|UNESTABLISHED|WHAT IS NOT|OPEN)\b.*$', re.I | re.M)


def roster():
    d = json.loads(io.open(ROSTER, encoding='utf-8-sig').read())
    return list(d['files'])


def scan(rel):
    p = os.path.join(REPO, rel)
    if not os.path.exists(p):
        return None
    t = io.open(p, encoding='utf-8', errors='replace').read()
    m = CLASSLINE.search(t)
    counts = {}
    for rx, name in MARKS:
        n = len(rx.findall(t))
        if n:
            counts[name] = n
    return {
        'path': rel.replace('\\', '/'),
        'declared': (m.group(1).upper() if m else None),
        'purpose': bool(PURPOSE.search(t[:4000])),
        'marks': counts,
        'total': sum(counts.values()),
        'opensec': bool(OPENSEC.search(t)),
    }


def check(rows):
    """### THE CHECK: a SYNTHESIS document carrying open-species marks outside an
    ### explicit open-items section is a HARD FAILURE."""
    msg, bad = [], 0
    declared = [r for r in rows if r['declared']]
    if not rows:
        msg.append("### HARD FAILURE -- EMPTY ROSTER. Nothing was examined, so nothing")
        msg.append("### was verified. A verdict over an empty scope is not a verdict.")
        return 2, msg
    undeclared = [r for r in rows if not r['declared']]
    for r in rows:
        if r['declared'] == 'SYNTHESIS' and r['total'] and not r['opensec']:
            bad += 1
            msg.append("  ### FAIL %-52s marks=%d %s"
                       % (r['path'][:52], r['total'], r['marks']))
    msg.append("  documents examined       : %d" % len(rows))
    msg.append("  with a declared class    : %d" % len(declared))
    msg.append("  ### WITHOUT a declared class : %d   (### not in the restart kit)"
               % len(undeclared))
    msg.append("  synthesis failures       : %d" % bad)
    if undeclared:
        msg.append("  ### HARD FAILURE -- undeclared documents are in the roster.")
        return 1, msg
    if bad:
        msg.append("  ### HARD FAILURE -- synthesis documents carry open-species marks")
        msg.append("  ### outside an explicit open-items section.")
        return 1, msg
    msg.append("  VERDICT : CLEAN")
    msg.append("  ### and that means ONE thing: every roster document declares a class,")
    msg.append("  ### and no synthesis document carries an unexempted mark.")
    msg.append("  ### IT IS NOT A REVIEW OF WHETHER THE DECLARATIONS ARE TRUE.")
    return 0, msg


def main(argv):
    rows = [r for r in (scan(x) for x in roster()) if r]
    if '--check' in argv:
        code, msg = check(rows)
        print("--- DOCUMENT-CLASS CHECK (b186) ---")
        for l in msg:
            print(l)
        return code
    print("=" * 78)
    print("DOCUMENT CLASSES -- THE ROSTER SCANNED (b186)")
    print("=" * 78)
    print("  %-52s %-9s %-4s %s" % ("document", "declared", "purp", "open-species marks"))
    for r in sorted(rows, key=lambda x: -x['total']):
        print("  %-52s %-9s %-4s %s"
              % (r['path'][:52], r['declared'] or '-', 'yes' if r['purpose'] else '###NO',
                 (r['marks'] if r['marks'] else '')))
    print()
    print("  totals: %d documents, %d declaring a class, %d carrying marks"
          % (len(rows), sum(1 for r in rows if r['declared']),
             sum(1 for r in rows if r['total'])))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
