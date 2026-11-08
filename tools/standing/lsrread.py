# -*- coding: utf-8 -*-
"""standing/lsrread.py -- v1.26.0, (R356)(3)(v), b745 events (8): THE REMOTE READ RETRIED AND THE CACHED PASS.

b745's post-push part standing-a2 made two ls-remote calls on D:/SIDE-simplicity (tools/b616_claims.py remote_refs retried a read with no
refs/heads/, one read of 32.06 s through the run cache), and G-LSREMOTE-ONE-PER-REPO failed on the count; the part was re-run, every remote then
read from the run cache with no call, and the arm passed on nothing (data/b745_lsr_postpush_standing-a2_attempt1.json against
data/b745_lsr_postpush_standing-a2.json). Here each repository of a part is classed from its two records -- the ls-remote calls (KC0.LSR) and
the run cache's log (remotecache.wrap) -- and the part's verdict read from the classes:

  READ     one call, read through the reader
  RETRIED  two calls inside one read through the reader (the cache's log: reads 1): the retry of remote_refs, an EVENT, printed with its two
           timings where remote_refs recorded them (b616_claims.ATTEMPTS), its one total where it did not (b745)
  CACHED   no call, read from the run cache
  OVER     any other count: more than one read of one repository -- the arm's failure

  classify(lsr, times) -> {path: (class, detail)}
  verdict(lsr, times) -> ('PASS' | 'FAIL' | 'CACHED' | 'NONE', [event lines])   CACHED where every repository is CACHED: VACUOUS, counted as no pass;
                                                                        NONE (v1.27.0) over zero repositories: VACUOUS, never FAIL
  ok(lsr, times) -> bool                                                the arm's predicate: True on PASS and on CACHED (not a failure); the
                                                                        suite reads CACHED as VACUOUS and counts it as no pass
"""


def classify(lsr, times):
    lsr, times = dict(lsr or {}), dict(times or {})
    out = {}
    for p in sorted(set(lsr) | set(times)):
        n, t = lsr.get(p, 0), times.get(p) or {}
        if n == 0 and t.get('cached'):
            out[p] = ('CACHED', 'from the run cache at %s' % t.get('at'))
        elif n == 1:
            out[p] = ('READ', '%.2f s' % t.get('secs', 0.0) if t else 'one call')
        elif n == 2 and t.get('reads') == 1 and not t.get('cached'):
            a = t.get('attempts') or []
            out[p] = ('RETRIED', ('the two timings %s' % ' and '.join('%.2f s' % x for x in a)) if len(a) == 2 else
                      ('the two timings not recorded; the read`s total %.2f s' % t.get('secs', 0.0)))
        elif n == 0:
            out[p] = ('READ', 'no call recorded')
        else:
            out[p] = ('OVER', '%d calls' % n)
    return out


def verdict(lsr, times):
    c = classify(lsr, times)
    if not c:
        # ### v1.27.0, (R357)(3)(vi), b746 defect (m): a part that reads no repository is NONE, not FAIL -- nothing was read, nothing failed;
        # ### VACUOUS where an arm reads it, counted as no pass
        return 'NONE', ['NONE: zero repositories read']
    ev = ['RETRIED %s: %s (an event)' % (p, d) for p, (k, d) in sorted(c.items()) if k == 'RETRIED']
    if any(k == 'OVER' for k, _d in c.values()):
        return 'FAIL', ev + ['OVER %s: %s' % (p, d) for p, (k, d) in sorted(c.items()) if k == 'OVER']
    if all(k == 'CACHED' for k, _d in c.values()):
        return 'CACHED', ev + ['CACHED: every one of %d repositories read from the run cache, no ls-remote call -- VACUOUS, NO PASS' % len(c)]
    return 'PASS', ev


def ok(lsr, times):
    return verdict(lsr, times)[0] != 'FAIL'
