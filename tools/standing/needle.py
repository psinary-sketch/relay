# -*- coding: utf-8 -*-
"""standing/needle.py -- v1.38.2, (R374)(5) [K5]: A NEEDLE READ THROUGH ITS READER WHEN IT IS WRITTEN.

b763's defects (l), (n), (o), (p) and (q) (data/b763_defects.txt :56-:111), three of them REPEAT, are one class: a needle, heading or foot
written in one form and graded in another -- a tool's foot as a bare bold line where the act module's last-verdict reader takes only a line
opening "### ### **" (l); the weight arm's needles taken from the corrigendum's body where its reader reads the head line (n); a closing
heading without the "THE " the arm prefixes (o); a face needle in the source's backtick form where the gate reads the trail through conv
(p); a face sentence counting arms where the gate's bar screen reads a multi-arm bar (q). Each was found by the part's probe or the gate's
first run, after the writing. THE CALL, made by the seat at the writing of each needle, heading and foot the suite or the gate reads, takes
the needle and its reader, composes the text as that reader's route composes it, and prints whether the needle stands in it:

  python -X utf8 -u tools/standing/needle.py <act> arm <ARM> <needle> [<needle> ...] [--heavy]
      the act's suite rendered and loaded (tools/standing/fold.py), its sources composed as a part composes them (the part's heavy phases
      only with --heavy), the arm's own predicate run on them (PASS, FAIL or RAISED), and for each needle the texts the arm's code names
      that hold it -- raw, through the landing's conversion (standing.act.conv) and in their last verdict line (the act modules' _vlast)
      -- beside the count of every other composed text holding it; the reader the arm names decides STANDS
  python -X utf8 -u tools/standing/needle.py <act> entry|trail <needle> [...]
      the FINDINGS entry or the trail record composed by the record tool (_finding_text, _trail_text) and converted by conv, as the gate's
      dry-run step reads each needle of the face ((R267)(2), record drycheck); a halt of the composition printed as such
  python -X utf8 -u tools/standing/needle.py <act> foot <bank> <needle> [...]
      the bank's last verdict line as the act modules' last-verdict reader takes it (a line opening "### ### **", the prefix and closing
      "**" cut); a bank with no such line reads an empty foot
  python -X utf8 -u tools/standing/needle.py <act> bar <file>
      the paragraphs of the file through the registration gate's bar-floor screen (tools/registration_gate.py bar_floor_check: a threshold
      without its floor, several arms without the word of their independence), each miss by paragraph and line

Each call appends its reading to data/<act>_needle_calls.txt, one section a call; --dry writes nothing. No text of a composed source is
printed or banked, only the names of the texts and booleans; a needle is banked as written, cut at 160 characters.
"""
import io
import json
import os
import re
import sys
import time
import types

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
NL = '\n'
VPREFIX = '### ### **'
if HERE not in sys.path:
    sys.path.insert(0, HERE)
if T not in sys.path:
    sys.path.insert(1, T)


def conv(t):
    import act as A
    return A.conv(t)


def foot(text):
    """the bank's last verdict line as the act modules' _vlast reads it: the last line opening '### ### **', the prefix and closing '**' cut."""
    ls = [l.rstrip() for l in (text or '').replace('\r', '').split(NL) if l.startswith(VPREFIX)]
    return ls[-1][len(VPREFIX):].rstrip('*') if ls else ''


def foot_read(text, needles):
    f = foot(text)
    return dict(foot_found=bool(f), rows=[(n, n in f) for n in needles])


def conv_read(text, needles):
    """each needle raw in the text and in the text converted as the landing converts it."""
    c = conv(text or '')
    return [(n, n in (text or ''), n in c) for n in needles]


def bar(text):
    """the registration gate's bar-floor screen over the text's paragraphs: (floor misses, arm misses, threshold paragraphs, multi-arm paragraphs)."""
    import registration_gate as G
    return G.bar_floor_check(text)


def _consts(code, g, depth=3, seen=None):
    """the string constants of an arm's code, its nested code objects' and, `depth` calls deep, those of the functions of `g` it names."""
    seen = set() if seen is None else seen
    if id(code) in seen:
        return set()
    seen.add(id(code))
    out = set(c for c in code.co_consts if isinstance(c, str))
    for c in code.co_consts:
        if isinstance(c, types.CodeType):
            out |= _consts(c, g, depth, seen)
    if depth > 0:
        for n in code.co_names:
            f = g.get(n)
            if isinstance(f, types.FunctionType):
                out |= _consts(f.__code__, g, depth - 1, seen)
    return out


def _names(code, g, depth=3):
    import toset as TS
    return TS.code_names(code, g, depth)


def _texts(v, path, out, depth=0):
    """every text of a composed source, (path, text): strings, and bytes read as UTF-8; dicts, lists and tuples walked four deep."""
    if isinstance(v, str):
        out.append((path, v))
    elif isinstance(v, (bytes, bytearray)):
        out.append((path, bytes(v).decode('utf-8', 'replace')))
    elif depth < 4 and isinstance(v, dict):
        for k, x in v.items():
            _texts(x, '%s[%r]' % (path, k), out, depth + 1)
    elif depth < 4 and isinstance(v, (list, tuple)):
        for i, x in enumerate(v):
            _texts(x, '%s[%d]' % (path, i), out, depth + 1)
    return out


def _load(act, tool):
    import fold as F
    argv0 = sys.argv
    sys.argv = [os.path.join(T, '%s_%s.py' % (act, tool))]
    try:
        F.install()
        return F.load(act, tool, name='%s_%s_needle' % (act, tool))
    finally:
        sys.argv = argv0


def arm_read(act, arm, needles, heavy=False):
    """the arm's reading of each needle on the sources its part composes: a dict of the arm's verdict and the rows."""
    t0 = time.time()
    M = _load(act, 'checks')
    a = next((x for x in M.ARMS if x[0] == arm), None)
    if a is None:
        return dict(error='### NO ARM %s IN %s`S RUN LIST (%d arms)' % (arm, act, len(M.ARMS)))
    part = M._part_of(arm)
    need = tuple(M.NEED.get(part, ())) if heavy else ()
    S = M.sources(need)
    try:
        S['pushed'] = bool(M.is_pushed())
    except Exception:
        S['pushed'] = False
    try:
        verdict = 'PASS' if bool(a[2](S)) else 'FAIL'
    except Exception as e:
        verdict = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    g = M.__dict__
    names = _names(a[2].__code__, g)
    own = sorted(k for k in _consts(a[2].__code__, g) if k in S)
    readers = [r for r in ('conv', '_vlast') if r in names]
    texts = []
    for k in S:
        if k in ('REC', 'ER'):
            continue
        _texts(S[k], k, texts)
    rows = []
    for n in needles:
        raw_own = sorted(set(p.split('[')[0] for p, t in texts if p.split('[')[0] in own and n in t))
        conv_own = sorted(set(p.split('[')[0] for p, t in texts if p.split('[')[0] in own and n in conv(t)))
        foot_own = sorted(set(p.split('[')[0] for p, t in texts if p.split('[')[0] in own and n in foot(t)))
        other = len(set(p for p, t in texts if p.split('[')[0] not in own and n in t))
        stands = bool(foot_own) if '_vlast' in readers else bool(conv_own) if 'conv' in readers else bool(raw_own)
        rows.append(dict(needle=n, raw=raw_own, conv=conv_own, foot=foot_own, other=other, stands=stands))
    return dict(arm=arm, part=part, heavy=list(need), verdict=verdict, own=own, readers=readers, rows=rows, secs=round(time.time() - t0, 1))


def record_read(act, which, needles):
    t0 = time.time()
    M = _load(act, 'record')
    try:
        if which == 'entry':
            head, text = M._finding_text()
        else:
            head, text = M.TRAIL_HEAD(), M._trail_text()
    except SystemExit as e:
        return dict(error='### THE %s`S COMPOSITION HALTED: %s' % (which.upper(), str(e)[:300]))
    return dict(which=which, rows=[dict(needle=n, raw=r, conv=c, stands=c) for n, r, c in conv_read(text, needles)], secs=round(time.time() - t0, 1))


def _cut(n):
    return n if len(n) <= 160 else n[:157] + '...'


def render(mode, res, args):
    L = []
    if 'error' in res:
        return [res['error']], False
    if mode == 'arm':
        L += ['  the arm %s, part %s, heavy phases composed %s ; ON THE COMPOSED SOURCES: %s (%.1f s)' % (
                  res['arm'], res['part'], res['heavy'] or 'NONE', res['verdict'], res['secs']),
              '  the texts its code names %s ; the readers it names %s' % (res['own'] or 'NONE', res['readers'] or 'raw')]
        for r in res['rows']:
            L.append('  NEEDLE %r: raw in %s ; through conv in %s ; in the last verdict line of %s ; other composed texts holding it %d -- %s' % (
                _cut(r['needle']), r['raw'] or 'NONE', r['conv'] or 'NONE', r['foot'] or 'NONE', r['other'], 'STANDS' if r['stands'] else 'DOES NOT STAND'))
        ok = all(r['stands'] for r in res['rows']) and res['verdict'] == 'PASS'
        L.append('### ### **NEEDLES %d ; STANDING IN THE TEXT THE ARM READS %d ; THE ARM ON THE COMPOSED SOURCES %s.**' % (
            len(res['rows']), sum(1 for r in res['rows'] if r['stands']), res['verdict']))
        return L, ok
    if mode in ('entry', 'trail'):
        for r in res['rows']:
            L.append('  NEEDLE %r: raw %s ; through conv %s -- %s' % (_cut(r['needle']), r['raw'], r['conv'], 'STANDS' if r['stands'] else 'DOES NOT STAND'))
        ok = all(r['stands'] for r in res['rows'])
        L.append('### ### **THE %s AS COMPOSED AND CONVERTED: NEEDLES %d ; STANDING %d (%.1f s).**' % (
            mode.upper(), len(res['rows']), sum(1 for r in res['rows'] if r['stands']), res['secs']))
        return L, ok
    if mode == 'foot':
        L.append('  the bank %s: a verdict line opening "### ### **" %s' % (args[0], 'FOUND' if res['foot_found'] else 'ABSENT -- THE FOOT READS EMPTY'))
        for n, s in res['rows']:
            L.append('  NEEDLE %r in the foot: %s' % (_cut(n), 'STANDS' if s else 'DOES NOT STAND'))
        ok = res['foot_found'] and all(s for _n, s in res['rows'])
        L.append('### ### **THE FOOT AS THE LAST-VERDICT READER TAKES IT: NEEDLES %d ; STANDING %d.**' % (len(res['rows']), sum(1 for _n, s in res['rows'] if s)))
        return L, ok
    if mode == 'bar':
        fm, am, nt, nm = res['check']
        L.append('  %s: threshold paragraphs %d ; multi-arm paragraphs %d ; floor misses %s ; arm misses %s' % (
            args[0], nt, nm, [x[0] if isinstance(x, (list, tuple)) else x for x in fm] or 'NONE', [x[0] if isinstance(x, (list, tuple)) else x for x in am] or 'NONE'))
        ok = not fm and not am
        L.append('### ### **THE BAR-FLOOR SCREEN: FLOOR MISSES %d ; ARM MISSES %d.**' % (len(fm), len(am)))
        return L, ok
    return ['### NO MODE %s' % mode], False


def main(argv):
    dry = '--dry' in argv
    heavy = '--heavy' in argv
    argv = [a for a in argv if a not in ('--dry', '--heavy')]
    if len(argv) < 3 or not re.match(r'^b\d{3}$', argv[0]) or argv[1] not in ('arm', 'entry', 'trail', 'foot', 'bar'):
        sys.exit(__doc__)
    act, mode, rest = argv[0], argv[1], argv[2:]
    if mode == 'arm':
        if len(rest) < 2:
            sys.exit(__doc__)
        res, args = arm_read(act, rest[0], rest[1:], heavy), rest
    elif mode in ('entry', 'trail'):
        res, args = record_read(act, mode, rest), rest
    elif mode == 'foot':
        p = os.path.join(D, os.path.basename(rest[0]))
        if not os.path.isfile(p) or len(rest) < 2:
            sys.exit('### THE BANK %s RESOLVES TO NO FILE, OR NO NEEDLE GIVEN -- NOTHING READ' % rest[0])
        res, args = foot_read(io.open(p, encoding='utf-8').read(), rest[1:]), ['data/' + os.path.basename(p)] + rest[1:]
    else:
        p = rest[0]
        if not os.path.isfile(p):
            sys.exit('### THE FILE %s RESOLVES TO NO FILE -- NOTHING READ' % p)
        res, args = dict(check=bar(io.open(p, encoding='utf-8').read())), [os.path.basename(p)]
    L, ok = render(mode, res, args)
    head = '## %s THE NEEDLE CALL (v1.38.2, (R374)(5) [K5]): %s %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), mode,
                                                                       rest[0] if mode in ('arm', 'foot') else '(%d needle(s))' % len(rest) if mode != 'bar' else args[0])
    print(NL.join([head] + L))
    if not dry:
        bank = os.path.join(D, '%s_needle_calls.txt' % act)
        prior = io.open(bank, encoding='utf-8').read() if os.path.exists(bank) else (
            '%s -- THE NEEDLE CALLS, (R374)(5) [K5]: each appended by tools/standing/needle.py, one section a call' % act + NL)
        with open(bank + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join([head] + L) + NL)
        os.replace(bank + '.tmp', bank)
        print('appended to data/%s_needle_calls.txt' % act)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
