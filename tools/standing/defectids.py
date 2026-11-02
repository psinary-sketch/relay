# -*- coding: utf-8 -*-
"""standing/defectids.py -- v1.14.0, (R344)(2)(ix), b733 event (9): A DEFECT'S COMMIT IDS READ FROM THE LOG. b733's defect (q) listed seven commits by hand and named relay 3471c14b where the seventh of the arm's messages
was the kernel's 834f6ac: the count was right and one id wrong. Here the ids are read: a message over the one-write row is traced through the subject its `git commit -m` carries to the commit that subject names in the repositories' logs.

  subject_of(cmd)           the -m text of a commit command, or None
  commits_over(calls, log)  [(ts, short id, repo)] for the messages over the row; log(subject, cmd) -> [(short id, repo)]
Pure in its arguments; nothing written.
"""
import re

import gitwrite as GW

MSG = re.compile(r'git\s+(?:-C\s+\S+\s+)*commit\b[^"\']*-m\s+("(?:[^"\\]|\\.)*"|\'[^\']*\')')


def subject_of(cmd):
    m = MSG.search(cmd or '')
    return m.group(1)[1:-1].replace('\\"', '"') if m else None


def commits_over(calls, log):
    _ok, _n, over, _note = GW.reading(calls)
    out = []
    for mid, ts, _k in over:
        for c in calls:
            s = subject_of(c['cmd']) if c['mid'] == mid else None
            if s:
                out += [(ts, i, r) for i, r in log(s, c['cmd'])] or [(ts, None, s[:50])]
    return out
