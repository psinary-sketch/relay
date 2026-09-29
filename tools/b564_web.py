# -*- coding: utf-8 -*-
"""b564_web.py -- READING (3) (iii)-(iv): THE PUBLIC SEARCHES FOR PRIOR ART, UNDER (R174)(3). ### READS ONLY.
### `gh` runs GitHub's code and repository searches (the route: `gh`, authenticated here); `ingest <json>` banks the
### seat's web-search results (query, date, URLs, titles) exactly as the search tool returned them. Writes relay
### data/b564_web_*.json and data/b564_web.txt only; deletes nothing; addresses no deposit platform.
"""
import io, json, os, subprocess, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CODE = ["\"Li's criterion\"", '"Li criterion"', '"Keiper"', '"Bombieri-Lagarias"', '"Bombieri Lagarias"', '"liCoeff"',
        '"li_coeff"', '"Li coefficient"', '"Li coefficients"', '"keiper_li"', '"LiCriterion"', '"li_criterion"']
REPO = ["Li's criterion", 'Li criterion Riemann', 'Keiper Li', 'Bombieri Lagarias', 'Li coefficients Riemann hypothesis',
        'Riemann hypothesis Lean', 'Riemann hypothesis formalization', 'Li criterion Lean', 'Li criterion Coq',
        'Li criterion Isabelle']


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def gh(args):
    r = subprocess.run(['gh'] + args, capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        return r.returncode, json.loads(r.stdout or '[]'), r.stderr.strip()[:300]
    except Exception:
        return r.returncode, [], (r.stderr or r.stdout).strip()[:300]


def run_gh():
    out = []
    for q in CODE:
        for lang in ('lean', None):
            a = ['search', 'code', q, '--limit', '100', '--json', 'repository,path,url']
            if lang:
                a += ['--language', lang]
            rc, js, err = gh(a)
            out.append(dict(kind='code', query=q, language=lang or 'ANY', date=now(), rc=rc, count=len(js), err=err,
                            hits=[dict(repo=h['repository']['nameWithOwner'], path=h['path'], url=h['url']) for h in js]))
            print('code %-24s lang %-4s rc %d hits %3d %s' % (q, lang or 'ANY', rc, len(js), err[:80]))
    for q in REPO:
        rc, js, err = gh(['search', 'repos', q, '--limit', '100', '--json', 'fullName,description,url,updatedAt,language'])
        out.append(dict(kind='repos', query=q, date=now(), rc=rc, count=len(js), err=err,
                        hits=[dict(repo=h['fullName'], url=h['url'], language=h.get('language'), updated=h.get('updatedAt'),
                                   description=(h.get('description') or '')[:200]) for h in js]))
        print('repos %-40s rc %d hits %3d %s' % (q, rc, len(js), err[:80]))
    io.open(os.path.join(D, 'b564_web_gh.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1, ensure_ascii=False) + NL)
    print('written: b564_web_gh.json')


def retry():
    """### the code searches the rate limit refused (rc 1, HTTP 403) are run again and replace their entries; the refused
    ### attempt is kept beside each as `refused_first` so the bank shows the retry."""
    p = os.path.join(D, 'b564_web_gh.json')
    out = json.loads(io.open(p, encoding='utf-8').read())
    for s in out:
        if s['kind'] == 'code' and s['rc'] != 0:
            a = ['search', 'code', s['query'], '--limit', '100', '--json', 'repository,path,url']
            if s['language'] != 'ANY':
                a += ['--language', s['language']]
            rc, js, err = gh(a)
            s['refused_first'] = dict(date=s['date'], err=s['err'])
            s.update(date=now(), rc=rc, count=len(js), err=err,
                     hits=[dict(repo=h['repository']['nameWithOwner'], path=h['path'], url=h['url']) for h in js])
            print('retry code %-24s lang %-4s rc %d hits %3d %s' % (s['query'], s['language'], rc, len(js), err[:60]))
    io.open(p, 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1, ensure_ascii=False) + NL)


def ingest(path):
    js = json.loads(io.open(path, encoding='utf-8').read())
    p = os.path.join(D, 'b564_web_search.json')
    old = json.loads(io.open(p, encoding='utf-8').read()) if os.path.exists(p) else []
    old += js
    io.open(p, 'w', encoding='utf-8', newline=NL).write(json.dumps(old, indent=1, ensure_ascii=False) + NL)
    print('banked %d searches (%d in all) into b564_web_search.json' % (len(js), len(old)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'gh':
        run_gh()
    elif a and a[0] == 'retry':
        retry()
    elif a and a[0] == 'ingest':
        ingest(a[1])
    else:
        sys.exit('usage: b564_web.py gh | ingest <json>')
