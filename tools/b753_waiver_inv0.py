import io, json
PRIV = ['PLACE-papers', 'TECHNE-Core', 'PLACE-phase1.5', 'PLACE-phase2', 'SIDE-carrier-spec', 'SIDE-spinor-calibration-mathlib', 'SIDE-constants', 'glassbead-game']
for f in ('D:/relay/data/b753_kernels.json', 'D:/relay/data/b753_head_read.json'):
    j = json.load(io.open(f, encoding='utf-8'))
    print(f, type(j).__name__, list(j.keys())[:12] if isinstance(j, dict) else len(j))
    def walk(o, path=''):
        if isinstance(o, dict):
            nm = o.get('name') or o.get('repo')
            if nm in PRIV:
                print('  ', path, {k: (v if not isinstance(v, (str, list, dict)) else ('<str %d>' % len(v) if isinstance(v, str) and len(v) > 60 else v if isinstance(v, str) else '<%s %d>' % (type(v).__name__, len(v)))) for k, v in o.items()})
            for k, v in o.items():
                if k in PRIV:
                    print('  key', path + '/' + k, (list(v.keys()) if isinstance(v, dict) else type(v).__name__))
                walk(v, path + '/' + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, path + '[%d]' % i)
    walk(j)
