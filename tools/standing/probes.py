# -*- coding: utf-8 -*-
"""standing/probes.py -- v1.14.0, (R344)(2)(i), the class at its third act (b729, b731's form, b733): THE SUITE'S PROBES WRITE TO PROBE PATHS, AND THE LOCK REFUSES OVER A TRACKED PROBE OUTPUT.

b733's gate commit tracked seventeen of the suite's banks before the lock; the pre-push suite wrote those names, and N4's reader counted them as edited after the lock (b733 event (11)). b729's trap and
b731's act-suffixed exercise name each moved one name. Here the rule is one list: before the lock a suite part writes data/<act>_probe_<part>.txt (the `mid` banks beside it), never a name the pre-push suite
writes; the lock gate refuses while any path the pre-push suite writes is tracked, printing the paths; and N4's reader leaves a probe path out by rule, a probe being no bank of the close.

  outputs(act, names)    the names among `names` the pre-push suite writes
  is_probe(act, name)    a bank of the probes' own, outside the lock's hash set and N4's read
  auto(act, directory)   a plain suite part runs as a probe: no lock gate has permitted the lock
  refusal(act, names)    (refused, lines): the lock gate's reading of a tracked list
Pure in its arguments but auto, which reads the gate's record; nothing written.
"""
import json
import os
import re

PARTS = ('standing-a', 'standing-c', 'standing-b1', 'standing-b2a', 'standing-b2b', 'standing-b3', 'act')
BASE = '%s_probe.txt'


def _alt():
    return '|'.join(re.escape(p) for p in PARTS)


def outputs(act, names):
    """the tracked names the pre-push suite writes: the combined bank and exercise, each part's bank, exercise and ls-remote bank, the chain halves' checks. Post-push, pre-run and mid names are none of them."""
    pat = re.compile(r'^data/%s_(?:checks\.txt|exercise\.json|(?:checks_(?:%s)\.txt)|(?:exercise_(?:%s)\.json)|(?:lsr_(?:%s)\.json)|chain_half_[a-z0-9]+_checks\.json)$' % (act, _alt(), _alt(), _alt()))
    return sorted(n for n in names if pat.match(n))


def is_probe(act, name):
    n = name.split('/')[-1]
    return bool(re.match(r'^%s_(?:probe_(?:%s)\.(?:txt|json)|mid_exercise_(?:%s)\.json|chain_half_[a-z0-9]+_probe\.json)$' % (act, _alt(), _alt()), n))


def auto(act, directory):
    """a suite part with no mode named, before the lock gate has permitted the lock, is a probe."""
    p = os.path.join(directory, '%s_lockgate.json' % act)
    try:
        with open(p, encoding='utf-8') as f:
            return not json.load(f).get('permits')
    except (OSError, ValueError):
        return True


def refusal(act, names):
    """(R344) (N4): no tracked path is a probe output at the lock: the names the suite writes, and the probe paths themselves, which stay untracked; the pre-lock comparison's bank carries what they read."""
    bad = sorted(set(outputs(act, names)) | set(n for n in names if is_probe(act, n)))
    return bool(bad), ['    ### ### **%d TRACKED PATH(S) ARE PROBE OUTPUTS -- THE LOCK WOULD COUNT THE SUITE`S OWN RUN AS AN EDIT:**' % len(bad)] + ['        %s' % n for n in bad] if bad \
        else ['    ### no tracked path is a probe output (%d tracked paths read)' % len(names)]
