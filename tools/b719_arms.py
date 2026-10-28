"""b719 Component 6 -- (R329)(10): THE CLOSE ARMS' HISTORY b705-b718, THEN THE RETIREMENTS.

  python -X utf8 tools/b719_arms.py history dry|bank     # data/b719_arm_history.txt and .json (bank before any retirement)
  python -X utf8 tools/b719_arms.py retire dry|write     # data/arm_tags.json's RETIRED map, after the history bank is committed

THE HISTORY. For every arm data/arm_tags.json (b718's map) tags CLOSE, and for each act b705-b718 and each reading (pre-push
data/<act>_checks.txt, post-push data/<act>_checks_postpush.txt), the arm's state is read off the bank's own verdict lines: LIVE FAILING
(its list, :13 or so, parsed literally) and the face's declared carried list (:12). Each failure is traced:
  DECLARED   the arm in that reading's declared-as-carried list (the act's face, section (G2));
  NAMED      the arm's name in the act's own record of itself: data/<act>_defects.txt, data/<act>_events.txt, or the next act's
             corrigendum for it, data/<act+1>_corrigendum.txt (each hit with file and line; a name wrapped across lines found by a
             second matcher over the lines joined, both yields printed); the tag CLAIM or CLOSE read off the hit's row where the row has one;
  UNTRACED   neither.
A failure traces to "bookkeeping, own defects or declared failures" ((R329)(10)) when DECLARED, or NAMED with no hit's row tagged CLAIM.
THE GUARDS, kept and named whatever their history: the arms guarding the seal, the root chain, the pushes and the registration order
(the list GUARDS below, each with its class). An arm with no failure in b705-b718 is kept: its clause's "all trace" is not read vacuously
(feedback: a vacuous pass is not evidence). Claim arms are untouched: read only to print the claim figure.
"""
import ast
import io
import json
import os
import re
import sys
import time

D = 'D:/relay'
DATA = os.path.join(D, 'data')
NL = '\n'
ACTS = list(range(705, 719))
TAGS = os.path.join(DATA, 'arm_tags.json')
OUT_TXT = os.path.join(DATA, 'b719_arm_history.txt')
OUT_JSON = os.path.join(DATA, 'b719_arm_history.json')

GUARDS = {
    # ### the seal
    'G-SEALED-AFTER-COMPONENTS': 'seal', 'G-NOTHING-RAN-AHEAD': 'seal', 'G-LOCKGATE-EIGHT': 'seal', 'G-SEAL-VERIFIES': 'seal',
    'G-SEAL-HASHES': 'seal', 'G-ARMS-PRERUN': 'seal', 'G-TRAIL-CARRIES-SEAL': 'seal', 'G-RULE-SCORES-BEFORE-SEAL': 'seal',
    'G-RULE-POSTSEAL-READ': 'seal',
    # ### the root chain
    'G-ACTROOT-BANKED': 'root chain', 'G-ROOT-BANKS-COMMITTED': 'root chain', 'G-ACTROOT-LAST': 'root chain',
    'G-ACTROOT-VERIFY': 'root chain', 'G-TRAIL-CARRIES-ROOT': 'root chain', 'G-ROOTDRY-READY': 'root chain',
    'G-POSTROOT-WRITES-NONE': 'root chain', 'G-GUARD-HELD': 'root chain', 'G-MEMBRANE-WIRED': 'root chain',
    'G-RULE-MIDACT-AFTER-ROOT': 'root chain',
    # ### the pushes
    'G-PUSHOUT-COMMITTED': 'pushes', 'G-PRIOR-CLOSED-PUSHED': 'pushes', 'G-PUSHED-PREDICATE-THREE-CLAUSED': 'pushes',
    'G-LSREMOTE-ONE-PER-REPO': 'pushes', 'G-RULE-REMOTE-REREAD': 'pushes',
    # ### the order of registrations (G-REGISTRATIONS-FIRST is tagged CLAIM and untouched as a claim arm)
    'G-REGISTRATIONS-FIRST': 'registration order',
    # ### THE SEAT'S ADDITION BEYOND (R329)(10)'S FOUR CLASSES, named so, for the author's word at b720: the arms that carry a standing
    # ### safety rule (delete only a verified absolute path, b537; one branch per delete, (R327)(3)(i); the ferry received in full before
    # ### anything runs, the ferry paste rule). Their failures b705-b718 trace to bookkeeping or own defects; they are kept for the rule.
    'G-DELETE-FREE': 'a standing safety rule (deletes), the seat`s addition',
    'G-DELETES-ONE-BRANCH': 'a standing safety rule (deletes), the seat`s addition',
    'G-RECEIPT-IN-FULL': 'a standing safety rule (receipt in full), the seat`s addition',
}


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def lines_of(path):
    if not os.path.exists(path):
        return None
    return io.open(path, encoding='utf-8').read().split(NL)


def parse_reading(path):
    """(failing list, declared list, the line numbers read) from a suite bank's head, or None if absent."""
    L = lines_of(path)
    if L is None:
        return None
    fail, decl, at = None, None, []
    for i, l in enumerate(L[:40]):
        m = re.search(r'LIVE FAILING : \d+ (\[[^\]]*\])', l)
        if m and fail is None:
            fail, at = ast.literal_eval(m.group(1)), at + [i + 1]
        m = re.search(r'declared on the face as carried \(section \(G2\)\): (\[[^\]]*\])', l)
        if m and decl is None:
            decl, at = ast.literal_eval(m.group(1)), at + [i + 1]
    return dict(fail=fail, decl=decl, at=at)


def joined(L):
    """the lines joined with their leading '#'/space runs stripped, a '-' at a line's end joined without a space; offsets -> line numbers."""
    text, owner = [], []
    for i, l in enumerate(L):
        s = l.lstrip('# ').rstrip()
        sep = '' if (text and text[-1].endswith('-')) else ' '
        piece = (sep if text else '') + s
        text.append(piece)
        owner.extend([i + 1] * len(piece))
    return ''.join(text), owner


def tag_of(L, ln):
    """CLAIM or CLOSE on the hit's row: the hit line and up to four lines after it, the first tag word met; None if the row has none."""
    for l in L[ln - 1:ln + 4]:
        m = re.search(r'\b(CLAIM|CLOSE)\b', l)
        if m:
            return m.group(1)
    return None


def hits_in(rel, arm):
    """(raw hit lines, joined-matcher hit lines, tags) for the arm's name in the bank rel; None if the bank is absent."""
    L = lines_of(os.path.join(D, rel))
    if L is None:
        return None
    pat = re.compile(re.escape(arm) + r'(?![A-Z0-9-])')
    raw = [i + 1 for i, l in enumerate(L) if pat.search(l)]
    jt, owner = joined(L)
    jn = sorted(set(owner[m.start()] for m in pat.finditer(jt)))
    lns = sorted(set(raw) | set(jn))
    return dict(raw=raw, joined=jn, tags={ln: tag_of(L, ln) for ln in lns})


def history():
    tags = json.load(io.open(TAGS, encoding='utf-8'))['tags']
    close = sorted(a for a, t in tags.items() if t == 'CLOSE')
    claim = sorted(a for a, t in tags.items() if t == 'CLAIM')
    readings = {}
    for a in ACTS:
        for kind, suf in (('pre', 'checks'), ('post', 'checks_postpush')):
            readings[(a, kind)] = parse_reading(os.path.join(DATA, 'b%d_%s.txt' % (a, suf)))
    recs = {}
    for a in ACTS:
        recs[a] = ['data/b%d_defects.txt' % a, 'data/b%d_events.txt' % a, 'data/b%d_corrigendum.txt' % (a + 1)]
    rows = {}
    for arm in close:
        fails = []
        for a in ACTS:
            for kind in ('pre', 'post'):
                r = readings[(a, kind)]
                if r is None or r['fail'] is None or arm not in r['fail']:
                    continue
                declared = arm in (r['decl'] or [])
                named = {}
                for rel in recs[a]:
                    h = hits_in(rel, arm)
                    if h and (h['raw'] or h['joined']):
                        named[rel] = h
                claim_named = any(t == 'CLAIM' for h in named.values() for t in h['tags'].values())
                if declared:
                    trace = 'DECLARED'
                elif named and not claim_named:
                    trace = 'NAMED'
                elif named:
                    trace = 'NAMED-CLAIM'
                else:
                    trace = 'UNTRACED'
                fails.append(dict(act='b%d' % a, reading=kind, trace=trace, declared=declared,
                                  named={rel: dict(raw=h['raw'], joined=h['joined'], tags={str(k): v for k, v in h['tags'].items()})
                                         for rel, h in named.items()}))
        guard = GUARDS.get(arm)
        all_traced = bool(fails) and all(f['trace'] in ('DECLARED', 'NAMED') for f in fails)
        if guard:
            verdict = 'KEPT (guards %s)' % guard
        elif not fails:
            verdict = 'KEPT (no failure b705-b718; not read vacuously)'
        elif all_traced:
            verdict = 'RETIRE'
        else:
            verdict = 'KEPT (a failure not traced to bookkeeping, own defects or a declaration)'
        rows[arm] = dict(fails=fails, guard=guard, verdict=verdict)
    return dict(close=close, claim=claim, readings={'b%d %s' % k: v for k, v in readings.items()}, records=recs, rows=rows)


def render(H):
    R = []
    R.append('b719 -- (R329)(10): THE CLOSE ARMS` FAILURES b705-b718, EACH TRACED, BEFORE ANY RETIREMENT (%s)' % utc())
    R.append('')
    R.append('### Written by tools/b719_arms.py history (its docstring the method). data/arm_tags.json read as b718 left it: CLOSE %d, CLAIM %d.'
             % (len(H['close']), len(H['claim'])))
    R.append('### The readings, each bank`s verdict lines (failing list and declared list) at the lines printed:')
    for k, v in sorted(H['readings'].items()):
        if v is None:
            R.append('  %s ABSENT' % k)
        else:
            R.append('  %s at :%s ; failing %d ; declared %d' % (k, ', :'.join(str(x) for x in v['at']), len(v['fail'] or []), len(v['decl'] or [])))
    R.append('')
    R.append('## THE CLOSE ARMS, ONE ROW EACH (failures as act/reading:trace; a NAMED trace`s banks with their lines, raw | joined, and tags)')
    for arm in H['close']:
        r = H['rows'][arm]
        R.append('  %-34s %s ; failures %d' % (arm, r['verdict'], len(r['fails'])))
        for f in r['fails']:
            parts = []
            for rel, h in sorted(f['named'].items()):
                parts.append('%s raw %s joined %s tags %s' % (rel.replace('data/', ''), h['raw'][:6], h['joined'][:6],
                                                             sorted(set(t for t in h['tags'].values() if t))))
            R.append('      %s/%s: %s%s' % (f['act'], f['reading'], f['trace'], (' -- ' + ' ; '.join(parts)) if parts else ''))
    v = [H['rows'][a]['verdict'] for a in H['close']]
    ret = [a for a in H['close'] if H['rows'][a]['verdict'] == 'RETIRE']
    guard = [a for a in H['close'] if H['rows'][a]['guard']]
    never = [a for a in H['close'] if H['rows'][a]['verdict'].startswith('KEPT (no failure')]
    untr = [a for a in H['close'] if H['rows'][a]['verdict'].startswith('KEPT (a failure')]
    R.append('')
    R.append('## THE TALLY')
    R.append('  CLOSE arms %d = RETIRE %d + KEPT as guards %d + KEPT never failing %d + KEPT with an untraced or claim-named failure %d'
             % (len(v), len(ret), len(guard), len(never), len(untr)))
    R.append('  RETIRE: %s' % ret)
    R.append('  KEPT AS GUARDS: %s' % ['%s (%s)' % (a, H['rows'][a]['guard']) for a in guard])
    R.append('  KEPT, A FAILURE NOT TRACED: %s' % untr)
    R.append('  GUARDS NAMED BUT NOT IN THE CLOSE MAP: %s' % sorted(g for g in GUARDS if g not in H['close']))
    R.append('')
    R.append('## THE HAND-READ OF THE RESIDUE (the seat, before this bank: every NAMED hit line of the RETIRE rows printed one line each')
    R.append('## by a scratch reader over this tool`s history and read through)')
    R.append('  Each RETIRE arm`s failures are recorded by its act as the close`s own: a face or carried list not bumped (G-NEXT-ACT-NAMED,')
    R.append('  G-STEPZERO-TESTS), an order step not run before the seal (G-ARM-SECONDS-BANKED, G-PARTS-PRERUN), a bank`s phrase or key not')
    R.append('  the arm`s needle (G-PROCS-LISTED, G-REPORT-UNSEALED, G-SCORER-READS-BANKS), a late letter against the trail arms (G-TRAIL-*),')
    R.append('  a sealed predicate miscounting (G-ANSWERS-*, G-RULE-ONE-GIT-WRITE, G-RULE-SUITE-PARTS, G-TABLE-FINAL, G-DEFECTS-LETTERED,')
    R.append('  G-RULE-HEAD-LINE-QUOTED), a (W) row omitted (G-WRITELIST-KINDS), or the face`s declared carry (G-READ-RULE-STANDING,')
    R.append('  G-PRIORBANK-UNCHANGED, G-EDIT-ROUTE). Some hits are a tally line only (THE FAILING TEN and the like); each such failure is')
    R.append('  DECLARED or has a causal row in another of its act`s banks. No RETIRE row`s hit is tagged CLAIM. NAMED is a mention matcher: the hand-read, not')
    R.append('  the matcher, is what reads the cause.')
    R.append('')
    R.append('### ### **CLOSE %d ; RETIRE %d ; KEPT %d (GUARDS %d, NEVER FAILING %d, UNTRACED %d) ; CLAIM ARMS %d UNTOUCHED.**'
             % (len(v), len(ret), len(v) - len(ret), len(guard), len(never), len(untr), len(H['claim'])))
    return R, ret


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else 'history'
    mode = sys.argv[2] if len(sys.argv) > 2 else 'dry'
    if route == 'history':
        H = history()
        R, ret = render(H)
        if mode == 'bank':
            for p, b in ((OUT_TXT, NL.join(R) + NL), (OUT_JSON, json.dumps(dict(H, readings=H['readings'], retire=ret), indent=1, ensure_ascii=False))):
                with open(p + '.tmp', 'wb') as fh:
                    fh.write(b.encode('utf-8'))
                os.replace(p + '.tmp', p)
            print('written data/b719_arm_history.txt (%d lines) and .json' % len(R))
        else:
            print(NL.join(R))
    else:
        sys.exit('### route %r not built yet' % route)
