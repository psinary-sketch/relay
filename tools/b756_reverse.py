# -*- coding: utf-8 -*-
"""tools/b756_reverse.py -- b756 COMPONENT 2, (R366)(4)(ii) AND (iii): THE REVERSE READ OF SIX STATEMENTS, AND WHAT THE TWO TOOLS FIND
BEYOND (3).

Written at b756 by the Write tool and committed before its run ((R366)(4)(ii): "tools/b756_reverse.py, committed before its run, banked as
data/b756_reverse_read.txt"; the ferry's N2: "each tool of (4) commits before it runs and prints its controls before its figures").

THE READ. For each statement of (R366)(4)(ii)'s list, each line that carries it, by path and line, beside the record line it is read
against, over THE SCOPE: the roster's current editions (`tools/standing/roster.py json`, the builder's roster), of which FINDINGS.md and
OPEN_TRAILS.md are the two cuts' ledgers (tools/standing/cuts.py; each hit there marked by where the b756 cut puts its line), and every
file under tools/standing/fold/. PLACE-papers is read in its working tree at HEAD (its status printed), the fold in the relay's.
THE MATCHERS. Each statement has two shapes, printed with their yields (A the tight one, B the widened one); a line is matched alone, or
across a line break with the next (a hard-wrapped template), the hit then named at its first line. A line counts as CARRYING the statement
when shape A hits it, or when shape B alone hits it and the seat's hand-read (HAND, entered after a dry run printed every one) reads it so;
a B-only line the hand-read has not reached prints NOT YET READ and is not counted.
THE LEDGERS' LINES. A hit in a ledger (FINDINGS, REGISTRY, OPEN_TRAILS, SPIRAL_MAP, VERIFICATION_LOOM, ERRATA, INSTRUMENTS, the census,
README, the archive) is printed by path, line and the sha256 of the line, never by its words ([Q]: cited by path, line and digest).
THE CLASSES. A carrying line is ADDRESSED BY (3) (the writes of (R366)(3), the line each cites), REPAIRED BY (1)(ii) (v1.34.7), or BEYOND (3).
THE CONTROLS, printed before the figures: (i) each statement found at every line (R366) cites for it, by either shape, over the files as
read (statement (6) has no line cited in the scope, printed so); (ii) each shape fires on the text of its statement as a constructed line;
(iii) a planted needle in no file reads as no hit over the whole scope.
`beyond` writes data/b756_beyond_three.txt from this bank and the constellation summary (data/b756_constellation_summary.json): what the
two find beyond (3), with its counts, written nowhere else at this act ((R366)(4)(iii)).

  python -X utf8 -u tools/b756_reverse.py dry       the controls and every hit printed, nothing written
  python -X utf8 -u tools/b756_reverse.py run       the same, banked as data/b756_reverse_read.txt and .json
  python -X utf8 -u tools/b756_reverse.py beyond    data/b756_beyond_three.txt and .json
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tools')
D = os.path.join(ROOT, 'data')
FOLD = os.path.join(T, 'standing', 'fold')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
ACT = 'b756'
if T not in sys.path:
    sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'
WSC = 'day1/Which_Structure_Confines_v2_4_0.md'
FAS7 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md'
MONO = 'day1/A_Place_to_Stand.md'
RTPL = 'tools/standing/fold/record.tpl'
I_ = re.I

# ### (R366)(4)(ii)'s list, in its order: the statement, the record line it is read against, the two shapes, the lines (R366) cites for it
STATEMENTS = [
    dict(id='1', what='a zero located in Lean, or none',
         against='zq_offline_zero, SIDE-explicit-formula v0.38, as THE_EPSTEIN_CONTROL_OBJECT §5 cites it ((R366)(3)(iv), (4)(ii))',
         A=r'\bzeros?\b[^.;]{0,60}\blocated\b[^.;]{0,40}\bin\s+Lean\b',
         B=r'\blocated\b.{0,80}\bLean\b|\bLean\b.{0,80}\blocated\b',
         cited=[(FAS7, 45)]),
    dict(id='2', what='the Ramanujan bound at Epstein functions',
         against='relay data/b752_attribution_plan.txt :21 (the record`s mechanism table: the size bound kept, the Euler product dropped)',
         A=r'Ramanujan.{0,200}Epstein|Epstein.{0,200}Ramanujan',
         B=r'\bRamanujan\b',
         cited=[(SIMP, 296), (SIMP, 317), (WSC, 133)]),
    dict(id='3', what='zeros inside the strip credited to Davenport and Heilbronn',
         against='THE_EPSTEIN_CONTROL_OBJECT §5, the paragraph on the classical theorem (their theorem concerns Re s > 1; inside the strip, Voronin`s)',
         A=r'^(?=.*Davenport[-\u2013\u2014 ]+(?:and\s+)?Heilbronn)(?=.*\b(?:strip|off-line|critical|interior)\b)',
         B=r'Davenport.{0,12}Heilbronn',
         cited=[(SIMP, 306), (SIMP, 317)]),
    dict(id='4', what='the primes of valence 7 as \u00b11 mod 24',
         against='ERRATA :841, E-2026-10-04-1 (1 mod 24)',
         A=r'(?:\u00b1|\\pm|\+/-)\s*1\s*(?:\(\s*)?(?:mod|\\pmod|\\bmod)\s*\{?\s*24\b',
         B=r'\bvalence\b.{0,120}\b24\b|\b24\b.{0,120}\bvalence\b',
         cited=[(MONO, 2098)]),
    dict(id='5', what='the events bank for what is found after the seal',
         against='(R366)(1)(ii) (the bank dropped by (R365)(2)(ii) and dropped again; the N4 wording corrected at v1.34.7)',
         A=r'events\s+bank\s+for\s+what\s+is\s+found\s+after\s+the\s+seal',
         B=r'events_postseal|post-?seal\s+events|events\s+bank\s+after\s+the\s+seal',
         cited=[(RTPL, 2533)]),
    dict(id='6', what='the words "verified surround" in a description or front door',
         against='the author`s word of 2026-11-14 that a newcomer cannot check a phrase they cannot parse ((R366)(4)(ii), (6))',
         A=r'verified\s+surround',
         B=r'\bverified\b.{0,40}\bsurround|\bsurround\b.{0,40}\bverified\b',
         cited=[]),
]
# ### the lines the writes of (R366)(3) address (each note cites its line), and the line (1)(ii)'s standing change repaired
ADDRESSED = {(FAS7, 45, '1'): '(3)(iv)', (SIMP, 296, '2'): '(3)(ii)', (SIMP, 317, '2'): '(3)(ii)', (WSC, 133, '2'): '(3)(iii)',
             (SIMP, 306, '3'): '(3)(ii)', (SIMP, 317, '3'): '(3)(ii)', (MONO, 2098, '4'): '(3)(v) [L20]'}
REPAIRED = {(RTPL, 2533, '5'): '(1)(ii), tools/standing/ v1.34.7 (relay dc8319ea)'}
# ### THE SEAT'S HAND-READ of the lines shape B alone hits (path, line, statement): (carries, reading); entered after the dry run
HAND = {}
PLANTED = 'zz-b756-planted-needle-in-no-file'
LEDGER_STEMS = ('FINDINGS', 'REGISTRY', 'OPEN_TRAILS', 'SPIRAL_MAP', 'VERIFICATION_LOOM', 'ERRATA', 'INSTRUMENTS', 'THE_KEYSTONE_CENSUS', 'README')


def is_ledger(path):
    b = os.path.basename(path)
    return path.startswith('archive/') or any(b.startswith(s) for s in LEDGER_STEMS)


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def roster_files():
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'standing', 'roster.py'), 'json'], capture_output=True)
    if r.returncode != 0:
        sys.exit('### roster.py json exit %d' % r.returncode)
    return [p.replace('\\', '/') for p in json.loads(r.stdout.decode('utf-8'))['files']]


def scope():
    """[(label, path for the bank, lines)]: the roster's files at PLACE-papers' working tree, then every file under tools/standing/fold/."""
    out = []
    for p in roster_files():
        fp = os.path.join(PP, *p.split('/'))
        if os.path.isfile(fp):
            out.append(('pp', p, io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    for dp, dn, fn in os.walk(FOLD):
        dn.sort()
        for f in sorted(fn):
            fp = os.path.join(dp, f)
            rel = os.path.relpath(fp, ROOT).replace('\\', '/')
            out.append(('relay', rel, io.open(fp, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)))
    return out


def hits_of(rx, lines):
    """[(line, how)]: the line alone, or the line joined to the next across a break (named at its first line, the next not hit alone)."""
    out = []
    alone = [bool(rx.search(l)) for l in lines]
    for i, l in enumerate(lines):
        if alone[i]:
            out.append((i + 1, 'line'))
        elif i + 1 < len(lines) and not alone[i + 1] and lines[i + 1].strip():
            if rx.search(l.rstrip() + ' ' + lines[i + 1].strip().lstrip('#').strip().strip("'\"")):
                out.append((i + 1, 'wrapped :%d-:%d' % (i + 1, i + 2)))
    return out


def digest(l):
    return hashlib.sha256(l.encode('utf-8')).hexdigest()[:16]


def cut_place():
    """### where the b756 cuts put each line of the two ledgers: a function (path, line, text) -> words, or a refusal's words."""
    try:
        from standing import cuts as CU
        _c, _f, x = CU.build('HEAD', ACT)
    except Exception as e:   # noqa: BLE001 -- the cut's refusal is printed, not raised
        return lambda p, k, t: '', 'THE b756 CUTS NOT READ: %s' % str(e)[:200]

    def where(p, k, t):
        if p == 'FINDINGS.md':
            if k <= x['fend'] or k >= x['fs']:
                return 'in the b756 cut whole'
            return 'in the b756 cut by its heading line' if t.startswith('## ') else 'outside the b756 cut'
        if p == 'OPEN_TRAILS.md':
            s0, s1 = x['st']
            if k < x['ofirst'] or s0 <= k <= s1 or k >= x['t0']:
                return 'in the b756 cut whole'
            return 'in the b756 cut by its heading line' if t.startswith('### ') else 'outside the b756 cut'
        return ''
    return where, 'THE b756 CUTS at PLACE-papers %s: FINDINGS whole :1-:%d and from :%d; OPEN_TRAILS whole :1-:%d, :%d-:%d and from :%d' % (
        x['commit'], x['fend'], x['fs'], x['ofirst'] - 1, x['st'][0], x['st'][1], x['t0'])


def read(write=False):
    t0 = time.time()
    S = scope()
    by = dict((p, ls) for _r, p, ls in S)
    where, cut_line = cut_place()
    pp_head = g(PP, 'rev-parse', '--short=8', 'HEAD')[1].strip()
    pp_status = [l for l in g(PP, 'status', '--porcelain', '--untracked-files=no')[1].split(NL) if l.strip()]
    C = []
    # (i) each statement at every line (R366) cites for it, by either shape
    for st in STATEMENTS:
        ra, rb = re.compile(st['A'], I_), re.compile(st['B'], I_)
        if not st['cited']:
            C.append(('(i) statement (%s)' % st['id'], 'no line of the scope cited by (R366) for this statement: the control NOT AVAILABLE, printed so', None))
        for p, k in st['cited']:
            ls = by.get(p) or []
            got = [h for h in hits_of(ra, ls) + hits_of(rb, ls) if h[0] == k]
            C.append(('(i) statement (%s)' % st['id'], 'found at %s :%d, cited by (R366)' % (p, k), bool(got)))
    # (ii) each shape fires on its statement written as a constructed line
    for st in STATEMENTS:
        line = {'1': 'the control, no zero located in Lean', '2': 'Epstein functions lack the Ramanujan bound',
                '3': 'off-line zeros inside the strip, Davenport-Heilbronn', '4': 'p \u2261 \u00b11 mod 24, valence 7',
                '5': 'the events bank for what is found after the seal present, events_postseal', '6': 'the verified surround'}[st['id']]
        C.append(('(ii) statement (%s)' % st['id'], 'shapes A and B fire on the constructed line "%s"' % line,
                  bool(re.search(st['A'], line, I_)) and bool(re.search(st['B'], line, I_))))
    # (iii) the planted needle over the whole scope
    rp = re.compile(re.escape(PLANTED), I_)
    nplant = sum(len(hits_of(rp, ls)) for _r, _p, ls in S)
    C.append(('(iii) the planted needle', '"%s", in no file, reads no hit over %d files' % (PLANTED, len(S)), nplant == 0))
    L = ['%s -- COMPONENT 2: THE REVERSE READ OF SIX STATEMENTS, (R366)(4)(ii) (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the scope: the roster`s current editions (tools/standing/roster.py json) at PLACE-papers HEAD %s, tracked changes %d; every file under '
         'tools/standing/fold/; %d files in all' % (pp_head, len(pp_status), len(S)),
         '### %s' % cut_line,
         '### a ledger`s line printed by path, line and the sha256 of its text (16 hex), never by its words', '',
         '## THE CONTROLS, BEFORE THE FIGURES']
    for tag, what, ok in C:
        L.append('  %s %s: %s' % ('NOT AVAILABLE' if ok is None else ('AS WANTED' if ok else 'NOT AS WANTED'), tag, what))
    nc = sum(1 for c in C if c[2] is not None)
    nok = sum(1 for c in C if c[2])
    L += ['  ### THE CONTROLS: %d OF %d AS WANTED ; NOT AVAILABLE %d' % (nok, nc, sum(1 for c in C if c[2] is None)), '']
    J = dict(controls=dict(wanted=nc, as_wanted=nok), statements=[])
    tot = dict(carrying=0, addressed=0, repaired=0, beyond=0, b_only_unread=0, b_only_not=0)
    for st in STATEMENTS:
        ra, rb = re.compile(st['A'], I_), re.compile(st['B'], I_)
        rows, ya, yb = [], 0, 0
        for _r, p, ls in S:
            ha = dict(hits_of(ra, ls))
            hb = dict(hits_of(rb, ls))
            ya += len(ha)
            yb += len(hb)
            for k in sorted(set(ha) | set(hb)):
                text = ls[k - 1]
                if k in ha:
                    carries, why = True, 'shape A (%s)' % ha[k]
                else:
                    h = HAND.get((p, k, st['id']))
                    if h is None:
                        carries, why = None, 'shape B alone (%s): NOT YET READ' % hb[k]
                    else:
                        carries, why = h[0], 'shape B alone (%s), hand-read: %s' % (hb[k], h[1])
                cls = ADDRESSED.get((p, k, st['id']))
                cls = ('ADDRESSED BY ' + cls) if cls else (('REPAIRED BY ' + REPAIRED[(p, k, st['id'])]) if (p, k, st['id']) in REPAIRED else 'BEYOND (3)')
                rows.append(dict(path=p, line=k, carries=carries, why=why, cls=cls if carries else '--', where=where(p, k, text),
                                 text=('sha256 %s' % digest(text)) if is_ledger(p) else text.strip()[:240]))
        car = [r for r in rows if r['carries']]
        n_add = sum(1 for r in car if r['cls'].startswith('ADDRESSED'))
        n_rep = sum(1 for r in car if r['cls'].startswith('REPAIRED'))
        n_bey = sum(1 for r in car if r['cls'] == 'BEYOND (3)')
        n_unr = sum(1 for r in rows if r['carries'] is None)
        n_not = sum(1 for r in rows if r['carries'] is False)
        for k_, v_ in (('carrying', len(car)), ('addressed', n_add), ('repaired', n_rep), ('beyond', n_bey), ('b_only_unread', n_unr), ('b_only_not', n_not)):
            tot[k_] += v_
        L += ['## (%s) %s' % (st['id'], st['what'].upper()),
              '### read against: %s' % st['against'],
              '### shape A /%s/ : %d hit(s) ; shape B /%s/ : %d hit(s) ; lines %d ; CARRYING %d (addressed by (3) %d, repaired by (1)(ii) %d, BEYOND (3) %d) ; '
              'B alone, not carrying %d, NOT YET READ %d' % (st['A'], ya, st['B'], yb, len(rows), len(car), n_add, n_rep, n_bey, n_not, n_unr)]
        for r in rows:
            L.append('  %s :%d -- %s -- %s%s -- %s' % (r['path'], r['line'], 'CARRIES' if r['carries'] else ('NOT YET READ' if r['carries'] is None else 'does not carry'),
                                                    r['cls'], (' ; ' + r['where']) if r['where'] else '', r['why']))
            L.append('      %s' % r['text'])
        L.append('')
        J['statements'].append(dict(id=st['id'], what=st['what'], against=st['against'], A=ya, B=yb, carrying=len(car), addressed=n_add,
                                    repaired=n_rep, beyond=n_bey, b_only_not=n_not, b_only_unread=n_unr,
                                    rows=[dict((k, v) for k, v in r.items() if k != 'text') for r in rows]))
    J['totals'] = tot
    J['seconds'] = round(time.time() - t0, 1)
    L.append('### ### **THE REVERSE READ: CONTROLS %d OF %d AS WANTED ; LINES CARRYING THE SIX STATEMENTS %d ; ADDRESSED BY (3) %d ; REPAIRED BY (1)(ii) %d ; '
             'BEYOND (3) %d ; SHAPE B ALONE NOT CARRYING %d, NOT YET READ %d ; %.1f s.**' % (
                 nok, nc, tot['carrying'], tot['addressed'], tot['repaired'], tot['beyond'], tot['b_only_not'], tot['b_only_unread'], J['seconds']))
    if write:
        put('%s_reverse_read.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
        put('%s_reverse_read.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    print(NL.join(L))
    return nok == nc


def put(name, b):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as f:
        f.write(b)
    os.replace(p + '.tmp', p)
    print('  written: data/%s (%d bytes)' % (name, len(b)))


def beyond():
    """### (R366)(4)(iii): what the two find beyond (3), with the two counts the root prompt carries; written nowhere else at this act."""
    rr = json.load(io.open(os.path.join(D, '%s_reverse_read.json' % ACT), encoding='utf-8'))
    cs = json.load(io.open(os.path.join(D, '%s_constellation_summary.json' % ACT), encoding='utf-8'))
    L = ['%s -- (R366)(4)(iii): WHAT THE TWO FIND BEYOND (3), BANKED WITH ITS COUNT AND WRITTEN NOWHERE AT THIS ACT (%s)' % (
        ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### "it goes to the prose pass and the re-cuts, and the root prompt carries the two counts" ((R366)(4)(iii))', '',
         '## THE CONSTELLATION RERUN (relay data/%s_constellation_summary.txt): tables read %d of %d; rows moved or gone by the tool %d %s; '
         'after the seat`s hand-read %d counted, %d not, %d unread. None of them is a line the writes of (3) address.' % (
             ACT, cs['tables'], cs['population'], cs['moved'], cs['kinds'], cs.get('hand_counted', 0), cs.get('hand_not', 0), cs.get('hand_unread', 0)),
         '## THE REVERSE READ (relay data/%s_reverse_read.txt): lines carrying the six statements %d; addressed by (3) %d; repaired by (1)(ii) %d; '
         'BEYOND (3) %d; shape B alone not yet read %d.' % (ACT, rr['totals']['carrying'], rr['totals']['addressed'], rr['totals']['repaired'],
                                                            rr['totals']['beyond'], rr['totals']['b_only_unread']), '']
    for s in rr['statements']:
        bey = [r for r in s['rows'] if r['carries'] and r['cls'] == 'BEYOND (3)']
        L.append('  (%s) %s: %d beyond (3)' % (s['id'], s['what'], len(bey)))
        for r in bey:
            L.append('      %s :%d%s' % (r['path'], r['line'], (' (%s)' % r['where']) if r['where'] else ''))
    n1, n2 = cs.get('hand_counted', cs['moved']), rr['totals']['beyond']
    L += ['', '### ### **THE TWO COUNTS FOR THE ROOT PROMPT: THE CONSTELLATION RERUN %d ROWS MOVED OR GONE (%d BY THE TOOL) ; THE REVERSE READ %d LINES '
              'BEYOND (3).**' % (n1, cs['moved'], n2)]
    put('%s_beyond_three.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    put('%s_beyond_three.json' % ACT, (json.dumps(dict(constellation_counted=n1, constellation_tool=cs['moved'], reverse_beyond=n2), indent=1) + NL).encode('utf-8'))
    print(NL.join(L[-3:]))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'dry':
        sys.exit(0 if read(False) else 1)
    elif cmd == 'run':
        sys.exit(0 if read(True) else 1)
    elif cmd == 'beyond':
        beyond()
    else:
        print('usage: b756_reverse.py dry | run | beyond')
        sys.exit(2)
