# -*- coding: utf-8 -*-
"""standing/publishstate.py -- v1.20.0, (R350)(2)(iv), (R338)'s "publish not called" repair (b727 events (3)): THE DEPOSIT ROUTE READ BY ITS
STATE, NOT BY THE WORD. From b728 the clause reads "no deposit, no new version, no draft published; metadata edits on published records are
permitted where a ruling names them by record", and the arm was to read the deposit route alone. It read the word: any `actions/publish` in an
act's tool failed it, and Zenodo's metadata edit runs actions/edit, then actions/publish on the published record -- b727's [13]-[19] and b739's
[104]-[108] each failed G-PUBLISH-UNCALLED with no deposit, no new version and no draft published. Here each tool's text is read for its state:

  UNCALLED                         no publish call in the text
  METADATA EDIT, NO NEW VERSION    every publish follows an actions/edit on the same record's route, and no new version, no deposit create
  PUBLISH                          a publish with no edit route before it, a new version (actions/newversion), or a deposit created

  state(text)       -> one of the three for one tool's text
  states(tooltext)  -> {file: state} over an act's tools
  ok(tooltext)      -> no tool in the PUBLISH state, and at least one tool read
"""
import re

PUB = 'actions' + '/pub' + 'lish'
EDIT = 'actions' + '/edit'
NEWV = 'actions' + '/new' + 'version'
PLANT = 'z_' + 'publish'
CREATE = re.compile(r"""['"]/?(?:api/)?deposit/depositions['"]\s*,\s*['"]POST""")
UNCALLED, EDITED, PUBLISHED = 'UNCALLED', 'METADATA EDIT, NO NEW VERSION', 'PUBLISH'


def state(text):
    t = text or ''
    if NEWV in t or CREATE.search(t) or PLANT in t:
        return PUBLISHED
    pubs = [m.start() for m in re.finditer(re.escape(PUB), t)]
    if not pubs:
        return UNCALLED
    edits = [m.start() for m in re.finditer(re.escape(EDIT), t)]
    calls = [p for p in pubs if re.search(r"base\s*\+\s*['\"]/" + re.escape(PUB), t[max(0, p - 20):p + len(PUB) + 2])]
    if calls and all(any(e < p for e in edits) for p in calls):
        return EDITED
    return PUBLISHED if calls else UNCALLED


def states(tooltext):
    return {f: state(t) for f, t in sorted((tooltext or {}).items())}


def ok(tooltext):
    s = states(tooltext)
    return bool(s) and PUBLISHED not in s.values()


def summary(tooltext):
    s = states(tooltext)
    by = {}
    for f, v in s.items():
        by.setdefault(v, []).append(f)
    return ' ; '.join('%s %d%s' % (k, len(v), (' (%s)' % ', '.join(v)) if k != UNCALLED else '') for k, v in sorted(by.items())) or 'NO TOOL READ'
