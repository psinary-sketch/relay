# -*- coding: utf-8 -*-
"""standing/prevdry.py -- v1.24.0, (R354)(2)(i), b743 events (3), (7): THE PRE-LOCK DRY RUNS PREV MODE. Every part's sources() is exercised in
`--prev` mode before the lock, so an act module that reads its own banks by name (b743's :561 `jl('b743_kernel_bases.json')`, rebound to b742's
absent bank; :575 `K.SITTING_PP[0]` on b742's empty tuple) breaks before the lock and not after it. The checks tool is rendered from the act module
(or from a module text given, a blob read at its commit), run with `--prev --part <p>`, and only sources(NEED[p]) is called: main() is never
called and nothing the suite writes is written (b743's read-only simulation, scratch prevsim743.py, promoted). Each part in its own process, in
the foreground, one per call; the result banked as data/<act>_prevdry_<part>.json with the module's blob, so a module edited after its run is
read as not run. The lock gate (standing/prelock.py gate) reads every part of the act banked OK at the module's present blob, or is NOT CLEAR.
Written at b744 by the Write tool.

  python -X utf8 -u tools/standing/prevdry.py run <part>      one part, banked
  python -X utf8 -u tools/standing/prevdry.py print           every part's bank read, nothing written
  exercise(act, part, module_text=None)                      the child's verdict, dict(ok, part, err, line, secs)
  gate(act)                                                  (clear, lines), the lock gate's reading
"""
import hashlib
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
TAIL = "if __name__ == '__main__':\n    sys.exit(main())"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _cur():
    with open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)


def module_blob(act, text=None):
    """the act module's git blob id, of the text given or of tools/acts/<act>.py on disk (LF, as git stores it)."""
    if text is None:
        p = os.path.join(T, 'acts', '%s.py' % act)
        if not os.path.exists(p):
            return None
        text = open(p, 'rb').read().decode('utf-8')
    b = text.replace('\r\n', '\n').encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def child(act, part, module_path=None):
    """in the child process: render the checks tool (from module_path's text where given), bind it with `--prev --part <part>`, call sources()."""
    import traceback
    sys.path.insert(0, S)
    sys.path.insert(1, T)
    os.chdir(RELAY)
    import fold as F
    F.install()
    import act_close as AC
    top = 'b%d' % max(int(n[1:].split('_')[0]) for n in os.listdir(D) if n.startswith('b') and n.endswith('_steps.json') and n[1:].split('_')[0].isdigit())
    if act != top:   # ### a past act replayed (a control): the suite's figures read as that act's, as they read when it was open; printed in the verdict
        f0 = AC.act_figures
        AC.act_figures = lambda dd=None, roots_text=None, act=None, _a=act: f0(dd, roots_text, act or _a)
    if module_path:
        secs, ovs = F._parse(act, open(module_path, encoding='utf-8').read())
        text = F.render(act, 'checks', secs, ovs)
    else:
        text = F.render(act, 'checks')
    if text.count(TAIL) != 1:
        print(json.dumps(dict(ok=False, part=part, err='the rendered checks tool carries its main() call %d times, not once' % text.count(TAIL), line=None)))
        return 1
    text = text.replace(TAIL, 'pass')
    fn = os.path.join(T, '%s_checks.py' % act)
    sys.argv = [fn, '--prev', '--part', part, '--quiet']
    g = {'__name__': '__main__', '__file__': fn, '__builtins__': __builtins__, '__fold__': (act, 'checks')}
    lines = text.split(NL)
    t0 = time.time()
    try:
        try:
            exec(compile(text, fn, 'exec'), g)
        except SystemExit as e:   # ### a refusal at the suite's import is a stop before sources(), read as one
            raise RuntimeError('the suite refused at its import: %s' % str(e)[:250])
        if part not in g['NEED']:
            raise KeyError('the part %r is not one of the suite`s parts %s' % (part, sorted(g['NEED'])))
        got = g['sources'](g['NEED'][part])
        out = dict(ok=True, part=part, err=None, line=None, n=len(got))
    except Exception as e:  # noqa: BLE001
        last = None
        for fr, ln in traceback.walk_tb(sys.exc_info()[2]):
            if fr.f_code.co_filename == fn:
                last = ln
        out = dict(ok=False, part=part, err='%s: %s' % (type(e).__name__, str(e)[:300]), line=last, at=(lines[last - 1].strip()[:300] if last else None))
    out['secs'] = round(time.time() - t0, 1)
    out['replayed_as'] = act if act != top else None
    print('PREVDRY ' + json.dumps(out))
    return 0


def exercise(act, part, module_text=None, timeout=590):
    """the part's prev-mode sources() run in a child process; module_text replaces the act module read from disk (a scratch file in the
    system temp, removed after). dict(ok, part, err, line, at, secs, blob)."""
    import tempfile
    mp = None
    if module_text is not None:
        fd, mp = tempfile.mkstemp(suffix='.py', prefix='prevdry_%s_' % act)
        with os.fdopen(fd, 'wb') as f:
            f.write(module_text.encode('utf-8'))
    try:
        r = subprocess.run([sys.executable, '-X', 'utf8', '-u', os.path.abspath(__file__), 'child', act, part] + ([mp] if mp else []),
                           capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout, cwd=RELAY)
        got = [l for l in r.stdout.split(NL) if l.startswith('PREVDRY ')]
        out = json.loads(got[-1][8:]) if got else dict(ok=False, part=part, err='no verdict (exit %d): %s' % (r.returncode, (r.stderr or r.stdout).strip()[-300:]), line=None)
    except subprocess.TimeoutExpired:
        out = dict(ok=False, part=part, err='TIMEOUT after %d s -- THE %d s GUARD HIT: LETTER IT AS A DEFECT WHEN IT HAPPENS ((R358)(3)(x))' % (timeout, timeout), line=None)
    finally:
        if mp:
            os.remove(mp)
    out['blob'] = module_blob(act, module_text)
    return out


def bank_path(act, part):
    return os.path.join(D, '%s_prevdry_%s.json' % (act, part))


def write_bank(act, part, out):
    out = dict(out, act=act, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    s = json.dumps(out, indent=1, ensure_ascii=False) + NL   # ### composed whole before the file opens (b328's zero-byte husk)
    p = bank_path(act, part)
    with open(p + '.tmp', 'wb') as f:
        f.write(s.encode('utf-8'))
    os.replace(p + '.tmp', p)
    return p


def gate(act, parts=None):
    """(clear, lines): every part of the act banked, its sources() OK in prev mode, at the act module's present blob."""
    parts = tuple(parts or _cur().get('parts') or ())
    blob = module_blob(act)
    L = ['  THE PRE-LOCK DRY IN PREV MODE ((R354)(2)(i)): every part`s sources() on the previous act`s banks, the act module at %s' % (blob or 'ABSENT')[:8]]
    bad = []
    for q in parts:
        p = bank_path(act, q)
        if not os.path.exists(p):
            bad.append(q)
            L.append('    %-14s ### NOT RUN (data/%s_prevdry_%s.json absent)' % (q, act, q))
            continue
        with open(p, encoding='utf-8') as f:
            j = json.load(f)
        if not j.get('ok'):
            bad.append(q)
            L.append('    %-14s ### FAILS: %s at the rendered line %s: %s' % (q, j.get('err'), j.get('line'), j.get('at')))
        elif j.get('blob') != blob:
            bad.append(q)
            L.append('    %-14s ### RUN ON ANOTHER MODULE (%s, now %s): run again' % (q, (j.get('blob') or '')[:8], (blob or '')[:8]))
        else:
            L.append('    %-14s SOURCES OK in %s s (%s)' % (q, j.get('secs'), j.get('at')))
    clear = bool(parts) and not bad
    L.append('  ### THE PREV-MODE DRY : %s (parts %d ; not clear %s)' % ('CLEAR' if clear else 'NOT CLEAR', len(parts), bad or 'NONE'))
    return clear, L


def main(argv):
    if argv[:1] == ['child'] and len(argv) >= 3:
        return child(argv[1], argv[2], argv[3] if len(argv) > 3 else None)
    act = _cur()['act']
    if argv[:1] == ['run'] and len(argv) == 2:
        sys.path.insert(0, T)
        import b703_checks as C3
        fm = C3.free_mb()
        print('  free %s MB, the hold 2560 %s' % (fm, 'MET' if isinstance(fm, int) and fm >= 2560 else '### NOT MET'))
        if not isinstance(fm, int) or fm < 2560:
            return 3
        out = exercise(act, argv[1])
        p = write_bank(act, argv[1], out)
        print('  %s %s: %s%s (%s s) -> %s' % (act, argv[1], 'SOURCES OK' if out['ok'] else '### FAILS', '' if out['ok'] else ' %s at line %s: %s' % (out.get('err'), out.get('line'), out.get('at')),
                                              out.get('secs'), os.path.relpath(p, RELAY)))
        return 0 if out['ok'] else 1
    if argv[:1] == ['print']:
        clear, L = gate(act)
        print(NL.join(L))
        return 0 if clear else 1
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
