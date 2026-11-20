# -*- coding: utf-8 -*-
"""standing/rootparts.py -- v1.34.0, (R364)(3)(x): THE ROOT ROUTE'S LIMIT.

b753's root route (`fold.py record root`, called 2026-11-12T03:27:05Z) ran past the host's 600 s limit for a foreground call and the host moved it
to the background (its notice 03:37:07Z), where it completed: the first reading of G-ROOT-BANKS-COMMITTED banked at 03:27:33Z
(data/b753_root_banks.json), the compute started at 03:36:52Z (data/b753_act_root.json `at`), 559 s between them that no bank names. The route
now prints the seconds it expects from the previous act's run before it runs, and where they reach four fifths of the host's limit it runs in
parts, each a call of its own in the foreground under the limit, each banking its seconds and what it read, the root computed last from the
parts' bank; the rule against a part in the background binds every part. The root's items, its order rule and its readings are the ones the
route ran whole: the parts take the route apart at its own joints and add no item.

  `record rootpart 1`  the first reading (b698's rootbanks: data/<act>_root_banks.txt, .json), its seconds and verdict banked
  `record rootpart 2`  the second reading (standing.repeat.committed_root's), each named bank's HEAD blob by its sha256, HEAD, the remote main
  `record root`        with both parts banked: the second reading's state confirmed at once (the banks named the same, HEAD the same and the
                       remote main, one status over the named banks clean, each file's sha256 its blob's), then the compute (tools/act_root.py
                       compute --write) and its seconds; with no part banked and the expected seconds under the margin, the route whole as
                       before, its seconds banked; with no part banked and the expected seconds at the margin or unread, a refusal naming
                       the parts' calls
  `record root whole`  the route whole whatever the expectation (the author's word, or a control)

The parts' bank, data/<act>_root_banks_parts.json, is a kind the root excludes (`root_banks.*`), so a part's write never touches a bank the root
names. The next act reads its seconds as its expectation; an act before v1.34.0 is read by the floor its banks give (its first reading's time to
its compute's start), printed as AT LEAST.
"""
import calendar
import hashlib
import json
import os
import subprocess
import sys
import time

NL = '\n'
LIMIT_S = 600       # ### the host's limit for a foreground call: tools/standing/limits.py's row for a record route, 600000 ms
MARGIN = 0.8        # ### the parts where the expected seconds reach four fifths of it
PARTS = '%s_root_banks_parts.json'
GUARD_S = 590       # ### v1.38.4, (R374)(5) [K15]: the suite's guard for a part (tools/standing/fold/checks.tpl's 590 s), read beside the host's limit


def guard_line(key, seconds, prev, D):
    """v1.38.4, (R374)(5) [K15]: a part's seconds read against the 590 s guard and the host's 600 s limit, beside the previous act's same part
    by its parts bank (b762's part 1 587 s and b763's 670.5 s each ran the reading once per record module in the chain, repeat.py's v1.38.4).
    Returns (line, under the guard)."""
    pj = _jl(os.path.join(D, PARTS % prev)) or {}
    ps = ((pj.get('parts') or {}).get(key) or {}).get('seconds')
    under = seconds is not None and seconds < GUARD_S
    return ('  ### PART %s`S SECONDS %.1f AGAINST THE GUARD %d s AND THE HOST`S LIMIT %d s: UNDER THE GUARD %s ; %s`s part %s %s' % (
        key, seconds, GUARD_S, LIMIT_S, under, prev, key, ('%.1f s' % float(ps)) if ps is not None else 'NOT BANKED')), under


def _epoch(iso):
    return calendar.timegm(time.strptime(iso, '%Y-%m-%dT%H:%M:%SZ'))


def _jl(p):
    return json.load(open(p, encoding='utf-8')) if os.path.isfile(p) else None


def expected(prev, D):
    """(seconds or None, how): the previous act's root route by its banks."""
    j = _jl(os.path.join(D, PARTS % prev))
    if j and j.get('parts'):
        s = sum(float(x.get('seconds') or 0) for x in j['parts'].values())
        return s, 'data/%s : %s' % (PARTS % prev, ' ; '.join('%s %.0f s' % (k, float(v.get('seconds') or 0)) for k, v in sorted(j['parts'].items())))
    rb, ar = _jl(os.path.join(D, '%s_root_banks.json' % prev)), _jl(os.path.join(D, '%s_act_root.json' % prev))
    if rb and ar and rb.get('at') and ar.get('at_epoch'):
        s = float(ar['at_epoch']) - _epoch(rb['at'])
        return s, ('AT LEAST: data/%s_root_banks.json`s time %s (its first reading ended) to data/%s_act_root.json`s compute start %s; the first '
                   'reading`s own seconds and the compute`s not counted' % (prev, rb['at'], prev, ar.get('at')))
    return None, 'NOT READ: data/%s has no parts bank, and no root-banks and act-root pair carrying times' % prev


def decide(seconds, limit=LIMIT_S, margin=MARGIN):
    """'whole' or 'parts': parts where the expected seconds reach the margin of the limit or are unread."""
    return 'parts' if seconds is None or seconds >= margin * limit else 'whole'


def blob_shas(root, rev, banks):
    out = {}
    for b in banks:
        r = subprocess.run(['git', '-C', root, 'show', '%s:%s' % (rev, b)], capture_output=True)
        out[b] = hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else None
    return out


def file_shas(root, banks):
    out = {}
    for b in banks:
        p = os.path.join(root, *b.split('/'))
        out[b] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.isfile(p) else None
    return out


def confirm(part2, banks_now, head_now, remote_now, status_lines, files_now):
    """[the reasons the second reading no longer holds] (empty: it holds): pure over what the final step reads at once."""
    why = []
    if not part2 or not part2.get('ready'):
        why.append('the second reading not banked READY')
        return why
    if sorted(banks_now) != sorted(part2.get('banks') or {}):
        why.append('the banks named now differ from the second reading`s (%d against %d)' % (len(banks_now), len(part2.get('banks') or {})))
    if head_now != part2.get('head'):
        why.append('HEAD %s, the second reading`s %s' % ((head_now or '')[:12], (part2.get('head') or '')[:12]))
    if remote_now != head_now:
        why.append('the remote main %s, not HEAD' % (remote_now or '')[:12])
    if status_lines:
        why.append('the named banks` status not clean: %s' % ', '.join(status_lines[:4]))
    off = [b for b, h in (part2.get('banks') or {}).items() if files_now.get(b) != h]
    if off:
        why.append('%d named bank(s) not their HEAD blob now: %s' % (len(off), ', '.join(off[:4])))
    return why


def bind(R, ACT, PREV, D, ROOT, put_json, utc):
    """(root, rootpart): the record module's two routes over b698's module R (its routes rebound by the record template)."""
    pp = os.path.join(D, PARTS % ACT)

    def _parts():
        return (_jl(pp) or {}).get('parts') or {}

    def _bank(key, row):
        j = _jl(pp) or dict(act=ACT, limit_s=LIMIT_S, margin=MARGIN, parts={})
        j['parts'][key] = row
        put_json(PARTS % ACT, j)

    def _git(*a):
        return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    def rootpart(*a):
        k = a[0] if a else ''
        if k not in ('1', '2'):
            sys.exit('usage: record rootpart <1|2> -- 1 the first reading, 2 the second; then `record root`')
        t0 = time.time()
        if k == '1':
            first = getattr(R.rootbanks, 'first', None)
            if first is None:
                sys.exit('### THE ROOT ROUTE IN PARTS: R.rootbanks carries no first reading (standing.repeat.committed_root not bound) -- NOTHING RUN')
            ok = bool(first())
            row = dict(at=utc(), seconds=round(time.time() - t0, 1), ok=ok, head=_git('rev-parse', 'HEAD').strip())
            gl, row['under_guard'] = guard_line('1', row['seconds'], PREV, D)   # ### v1.38.4, [K15]
            _bank('1', row)
            print(gl)
            print('### ### **THE ROOT ROUTE, PART 1 OF 2 (the first reading): %s in %.1f s, banked in data/%s.**' % ('READY' if ok else 'NOT READY', row['seconds'], PARTS % ACT))
            return
        if not (_parts().get('1') or {}).get('ok'):
            sys.exit('### THE ROOT ROUTE IN PARTS: PART 1 NOT BANKED READY -- `record rootpart 1` FIRST -- NOTHING RUN')
        banks = R.root_banks()
        s = R.root_banks_state(banks)
        bad = [r['bank'] for r in s['rows'] if not (r['status'] == 'clean' and r['equal'])]
        ready = not bad and bool(s['pushed']) and bool(s['rows'])
        row = dict(at=utc(), seconds=None, ready=ready, head=s['head'], remote=s['remote'], bad=bad, banks=blob_shas(ROOT, s['head'], banks))
        row['seconds'] = round(time.time() - t0, 1)
        gl, row['under_guard'] = guard_line('2', row['seconds'], PREV, D)   # ### v1.38.4, [K15]
        _bank('2', row)
        print(gl)
        print('### ### **THE ROOT ROUTE, PART 2 OF 2 (the second reading): banks %d, not clean or not equal %d, HEAD the remote main %s -- %s in %.1f s, '
              'banked in data/%s.**' % (len(banks), len(bad), s['pushed'], 'READY' if ready else 'NOT READY', row['seconds'], PARTS % ACT))

    def _compute(banks, a):
        r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', ACT] + banks + ([] if 'dry' in a else ['--write']),
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
        if r.returncode:
            sys.exit('### act_root.py exit %d' % r.returncode)

    def root(*a):
        sec, how = expected(PREV, D)
        mode = 'whole' if 'whole' in a else decide(sec)
        P = _parts()
        print('### THE ROOT ROUTE`S EXPECTED SECONDS ((R364)(3)(x)): %s -- %s ; the host`s limit %d s, the margin %.0f s ; %s' % (
            ('%.0f' % sec) if sec is not None else 'UNREAD', how, LIMIT_S, MARGIN * LIMIT_S,
            'THE PARTS BANKED (%s)' % ', '.join(sorted(P)) if P else ('RUN WHOLE' if mode == 'whole' else 'RUN IN PARTS')))
        t0 = time.time()
        if '2' in P or ('1' in P and 'whole' not in a):
            banks = R.root_banks()
            crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
            print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/%s_seal_hashes.json' % ACT in banks, crlf or 'none'))
            if crlf:
                sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
            head = _git('rev-parse', 'HEAD').strip()
            remote = (_git('ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
            st = [l for l in _git('status', '--porcelain', '--', *banks).split(NL) if l.strip()]
            why = confirm(P.get('2'), banks, head, remote, st, file_shas(ROOT, banks))
            if why:
                sys.exit('### THE ROOT ROUTE IN PARTS: THE SECOND READING DOES NOT HOLD AT THE COMPUTE (%s) -- NO ROOT' % ' ; '.join(why))
            print('  the second reading holds at the compute: banks %d, HEAD %s the remote main, status clean, every file its blob' % (len(banks), head[:12]))
            _compute(banks, a)
            if 'dry' not in a:
                r3 = dict(at=utc(), seconds=round(time.time() - t0, 1), head=head)
                gl, r3['under_guard'] = guard_line('3', r3['seconds'], PREV, D)   # ### v1.38.4, [K15]
                _bank('3', r3)
                print(gl)
            return
        if mode == 'parts':
            sys.exit('### THE ROOT ROUTE: THE EXPECTED SECONDS REACH THE MARGIN OR ARE UNREAD -- RUN IN PARTS, EACH A CALL OF ITS OWN IN THE FOREGROUND '
                     'WITH THE LIMIT tools/standing/limits.py PRINTS: `fold.py record rootpart 1`, then `fold.py record rootpart 2`, then `fold.py record '
                     'root` -- NOTHING RUN')
        R.root(*a)
        if 'dry' not in a:
            _bank('whole', dict(at=utc(), seconds=round(time.time() - t0, 1)))

    return root, rootpart
