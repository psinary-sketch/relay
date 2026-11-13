# -*- coding: utf-8 -*-
"""standing/harness.py -- v1.34.0, (R364)(3)(xvii): THE STEP-ZERO PRINT OF THE HARNESS.

Step zero prints the harness: its version with the date of its install, the model as the session's transcript rows give it, the effort level
and the window as the user settings hold them for that model, the update channel and [D1]'s key; a change of any of them within the act is an
event. b753 and b754 printed these by scratch readers (b754's at 15:59:06Z and 15:33:40Z, data/b754_events.txt (1), (2), (7)); the print stands
here, with its record as one json line a bank keeps, and a comparison of a later read with that record. Every path is read at run time from
the home folder; no path is printed and none is written into a string here. Nothing written; no network request.

  python -X utf8 -u tools/standing/harness.py print <session>                   the print and its record line (HARNESS RECORD {...})
  python -X utf8 -u tools/standing/harness.py compare <session> <bank> <line>   the print against the record at <bank> :<line>; a change an EVENT
  python -X utf8 -u tools/standing/harness.py control [<session>]               planted settings and records, and the live read
  figures(settings, model) -> dict    read(session) -> dict    changes(before, after) -> [(figure, before, after)]
"""
import io
import json
import os
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
if S not in sys.path:
    sys.path.insert(0, S)
FIGS = ('version', 'installed', 'model', 'effort', 'window', 'channel', 'd1')
MARK = 'HARNESS RECORD '


def _home(*p):
    return os.path.join(os.path.expanduser('~'), *p)


def figures(settings, model):
    """the settings' figures for `model`: the effort level and the window from its per-model settings, the effort level falling back to the
    top level where the per-model settings carry none (the source named); the update channel; [D1]'s key (env DISABLE_AUTOUPDATER)."""
    ms = ((settings or {}).get('modelSettings') or {}).get(model) or {}
    if 'effortLevel' in ms:
        eff, src = ms.get('effortLevel'), 'per model'
    elif (settings or {}).get('effortLevel') is not None:
        eff, src = settings.get('effortLevel'), 'top level'
    else:
        eff, src = None, 'none'
    return dict(effort=eff, effort_from=src, window=ms.get('autoCompactWindow'), channel=(settings or {}).get('autoUpdatesChannel'),
                d1=((settings or {}).get('env') or {}).get('DISABLE_AUTOUPDATER'))


def last_model(path):
    """the model of the transcript's last assistant row naming one (the harness's synthetic rows skipped)."""
    import chain as CH
    m = None
    for _i, o in CH._rows(path):
        if o and o.get('type') == 'assistant':
            x = (o.get('message') or {}).get('model') or ''
            if x and not x.startswith('<'):
                m = x
    return m


def read(session):
    import chain as CH
    r = subprocess.run('claude --version', capture_output=True, text=True, shell=True)
    ver = ((r.stdout or '') + (r.stderr or '')).strip().split(' ')[0] if r.returncode == 0 else None
    vd = _home('.local', 'share', 'claude', 'versions', ver or '-')
    inst = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(vd))) if ver and os.path.exists(vd) else None
    p = CH.path_of(session)
    model = last_model(p)
    try:
        st = json.load(io.open(_home('.claude', 'settings.json'), encoding='utf-8'))
    except (OSError, ValueError):
        st = {}
    f = figures(st, model)
    return dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), session=session[:8], version=ver, installed=inst, transcript_version=CH._version(p),
                model=model, models=[m for m, _n, _l, _t in CH.models(p)], **f)


def changes(before, after):
    return [(k, before.get(k), after.get(k)) for k in FIGS if before.get(k) != after.get(k)]


def lines(rec):
    return ['THE HARNESS ((R364)(3)(xvii)), read %s for session %s:' % (rec['at'], rec['session']),
            '  version %s, installed %s (the transcript`s last row names %s)' % (rec['version'], rec['installed'], rec['transcript_version']),
            '  the model by the transcript`s rows %s (the rows name %s)' % (rec['model'], ', '.join(rec['models']) or 'none'),
            '  for that model: the effort level %s (%s), the window %s' % (rec['effort'], rec['effort_from'], rec['window']),
            '  the update channel %s ; [D1]`s key %r' % (rec['channel'], rec['d1']),
            MARK + json.dumps(dict((k, rec.get(k)) for k in ('at', 'session') + FIGS), ensure_ascii=False)]


def record_at(bank, line):
    with io.open(bank, encoding='utf-8') as f:
        for i, l in enumerate(f, 1):
            if i == int(line):
                k = l.find(MARK)
                return json.loads(l[k + len(MARK):]) if k >= 0 else None
    return None


def control(session=None):
    out, ok = ['### harness.py control ((R364)(3)(xvii))'], []
    st = dict(model='opus', effortLevel=None, autoUpdatesChannel='latest', env=dict(DISABLE_AUTOUPDATER='1'),
              modelSettings={'m-a': dict(effortLevel='xhigh', autoCompactWindow=400000), 'm-b': dict(autoCompactWindow=400000)})
    a, b = figures(st, 'm-a'), figures(st, 'm-b')
    st2 = dict(st, effortLevel='high')
    c = figures(st2, 'm-b')
    ok.append(a['effort'] == 'xhigh' and a['effort_from'] == 'per model' and a['window'] == 400000 and b['effort'] is None and b['effort_from'] == 'none'
              and c['effort'] == 'high' and c['effort_from'] == 'top level' and a['channel'] == 'latest' and a['d1'] == '1')
    out.append('  planted settings: m-a %s/%s/%s ; m-b %s/%s ; m-b under a top-level effort %s/%s -> %s' % (
        a['effort'], a['effort_from'], a['window'], b['effort'], b['effort_from'], c['effort'], c['effort_from'], 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    r0 = dict(version='1', installed='t', model='m-a', effort='xhigh', window=400000, channel='latest', d1='1')
    ch1 = changes(r0, dict(r0, model='m-b'))
    ch0 = changes(r0, dict(r0))
    ok.append(ch1 == [('model', 'm-a', 'm-b')] and ch0 == [])
    out.append('  planted records: a model changed %s ; none changed %s -> %s' % (ch1, ch0, 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    import act as A_
    rec = read(session or A_.current().get('session'))   # ### the session named, else act_current's
    txt = '\n'.join(lines(rec))
    home = os.path.expanduser('~')
    ok.append(bool(rec['version']) and rec['version'] == rec['transcript_version'] and bool(rec['installed']) and bool(rec['model'])
              and home.lower() not in txt.lower() and os.path.basename(home).lower() not in txt.lower())
    out.append('  the live read: version %s, the transcript`s %s, installed %s, model %s ; no path or folder name under the home folder in the '
               'print %s -> %s' % (rec['version'], rec['transcript_version'], rec['installed'], rec['model'],
                                   home.lower() not in txt.lower() and os.path.basename(home).lower() not in txt.lower(), 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    out.append('### harness.py control: %d OF %d AS WANTED' % (sum(ok), len(ok)))
    return out, all(ok)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    a = sys.argv[1:]
    if a[:1] == ['print'] and len(a) == 2:
        print('\n'.join(lines(read(a[1]))))
    elif a[:1] == ['compare'] and len(a) == 4:
        before = record_at(a[2], a[3])
        if before is None:
            sys.exit('### NO RECORD at %s :%s; nothing compared' % (a[2], a[3]))
        rec = read(a[1])
        print('\n'.join(lines(rec)))
        ch = changes(before, rec)
        print('### AGAINST THE RECORD OF %s (%s :%s): %s' % (before.get('at'), a[2], a[3], '; '.join('%s %r -> %r, AN EVENT' % c for c in ch) or 'NO CHANGE'))
    elif a[:1] == ['control'] and len(a) <= 2:
        L, _ok = control(a[1] if len(a) == 2 else None)
        print('\n'.join(L))
    else:
        sys.exit(__doc__)
