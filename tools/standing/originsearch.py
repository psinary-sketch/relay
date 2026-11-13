# -*- coding: utf-8 -*-
"""standing/originsearch.py -- THE ORIGIN SEARCH ((R364)(5)[Q], passed whole at b754 on the author's word, relay
data/b754_author_answers.txt :95, 2026-11-13T21:57:50Z): does a line's words, or its figures and formulas, already stand in a
revision's tree. Built from the scripts of b753's waiver: tools/b753_waiver_inv6.py (the words arm, five-word shingles) and
tools/b753_waiver_inv8.py (the figure and formula arm as widened after its control failed on a formula with a comma inside its
left side). Written at b754 by the Write tool; no identifier of the author is read into any string here.

ITS REACH. It finds a run of words as written: five consecutive words, case and punctuation ignored, a line of four words or fewer
read whole. It finds a figure or a formula as written: a dotted number, a decimal, a fraction or a percentage, and a run of
mathematical tokens. IT DOES NOT FIND A PARAPHRASE (the same words in another order, or other words for the same matter), AND IT DOES
NOT FIND A FORMULA IN ANOTHER NOTATION (x^2 for x squared written with a superscript, a renamed variable). A row reading NOT FOUND
says that no run of five of its words and none of its figures stands as written in the tree read; it does not say the matter is new.

THE TREE. One pass over the text blobs of <rev> (default the relay's origin/main, the remote main as last fetched), each distinct
blob read once by `git cat-file --batch`, a blob carrying a NUL in its first 8000 bytes set apart as binary; with --path, the blobs
whose path matches that glob alone (fnmatch, case kept). Nothing is written; the hits are printed by path and line, and a query by its digest and length, never
its words, so that a protected line sought is not printed by its search.

  python -X utf8 -u tools/standing/originsearch.py control                 the controls, printed; nothing written
  python -X utf8 -u tools/standing/originsearch.py search <file> [--rev R] [--path P]
                                                                           each line of <file> sought; printed
"""
import collections
import fnmatch
import hashlib
import io
import os
import re
import subprocess
import sys
import time

S = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(os.path.dirname(S))
NL = '\n'
K = 5
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


# ---------------------------------------------------------------- the words arm (b753's inv6)
def toks(s):
    return re.findall(r'[^\W_]+', s.replace('[...]', ' ').lower())


def shingles(s):
    t = toks(s)
    if len(t) < K:
        return [' '.join(t)] if len(t) >= 3 else []
    return [' '.join(t[i:i + K]) for i in range(len(t) - K + 1)]


def line_shingles(t):
    ss = [' '.join(t[i:i + K]) for i in range(max(1, len(t) - K + 1))]
    if len(t) < K + 3:
        ss += [' '.join(t[i:i + 3]) for i in range(len(t) - 2)] + [' '.join(t[i:i + 4]) for i in range(len(t) - 3)]
    return set(ss)


# ---------------------------------------------------------------- the figure and formula arm (b753's inv8, widened)
NUM = re.compile(r'(?<![\w.:/-])(?:\d+(?:\.\d+)+|\d+/\d+|\d+(?:\.\d+)?\s?%)(?![0-9A-Za-z_/-])')
DATE = re.compile(r'\d{4}-\d{2}-\d{2}|\bv\d+(?:\.\d+)+\S*|\b10\.\d{4,}/\S+|\S+\.(?:md|py|json|txt|lean|tpl)\b|\S*[/\\]\S*[/\\]\S*')
OPS = set('|^/·×±≥≤≈∏∑√∈=<>+−∀∃→↔⊂∩∪∘⊗')
REL_ = '=≈≥≤∈'
PRE = re.compile(r'[0-9|^·×±≥≤≈∏∑√∈=−Ͱ-Ͽ⁰-₟℀-⅏∀-⋿²³¹]')


def _mathy(t):
    for c in t:
        if (c.isdigit() or c in OPS or c in '()_' or 'Ͱ' <= c <= 'Ͽ' or '⁰' <= c <= '₟' or '℀' <= c <= '⅏'
                or '∀' <= c <= '⋿' or c in '²³¹'):
            return True
    return False


def _clean(x):
    return x.strip('.,;:"\'“”’`*=≈')


def _ok(x):
    nop = sum(1 for c in x if c in OPS)
    return len(x) >= 5 and (nop >= 2 or (nop >= 1 and any(c.isdigit() or c > 'ͯ' for c in x)))


def figs(s):
    s0 = DATE.sub(' ', s.replace('[...]', ' '))
    out = set()
    for m in NUM.finditer(s0):
        out.add('N ' + re.sub(r'\s', '', m.group(0)))
    s1 = re.sub(r'[*`\\$]+', '', s0)
    run = []

    def flush():
        if run:
            x = _clean(''.join(run))
            if _ok(x):
                out.add('X ' + x)
            for side in re.split('[%s]' % REL_, x):
                side = _clean(side)
                if side != x and _ok(side) and len(side) >= 6:
                    out.add('X ' + side)
        del run[:]
    for t in s1.split():
        if _mathy(t) or (run and len(t) <= 2 and run[-1][-1:] in OPS):
            run.append(t)
            if t[-1:] in '.;"”' or (t[-1:] == ',' and not run[0].count('(') > ''.join(run).count(')')):
                flush()
        else:
            flush()
    flush()
    return out


# ---------------------------------------------------------------- one pass over the tree
def search(texts, repo=RELAY, rev='origin/main', path=None):
    """[dict(digest, chars, nsh, cov, best, bestcov, figs, fhit)] for each text, and the pass's own counts."""
    want_sh, want_fg = collections.defaultdict(list), collections.defaultdict(list)
    Q = []
    for k, t in enumerate(texts):
        sh, fg = set(shingles(t)), figs(t)
        Q.append((sh, fg))
        for s in sh:
            want_sh[s].append(k)
        for f in fg:
            want_fg[f].append(k)
    t0 = time.time()
    seen = {}
    for l in git(repo, 'ls-tree', '-r', rev).split(NL):
        if l:
            meta, p = l.split('\t', 1)
            parts = meta.split()
            p = p.strip('"')
            if len(parts) == 3 and parts[1] == 'blob' and (path is None or fnmatch.fnmatchcase(p, path)):
                seen.setdefault(parts[2], p)
    proc = subprocess.Popen(['git', '-C', repo, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sh_line = collections.defaultdict(collections.Counter)
    sh_any = collections.defaultdict(set)
    fg_hit = collections.defaultdict(dict)
    WS = set(want_sh)
    read = binary = cut = 0
    nbytes = 0
    for sha, p in sorted(seen.items()):
        proc.stdin.write((sha + NL).encode())
        proc.stdin.flush()
        head = proc.stdout.readline().split()
        data = proc.stdout.read(int(head[2]))
        proc.stdout.read(1)
        if b'\0' in data[:8000]:
            binary += 1
            continue
        read += 1
        nbytes += len(data)
        for n, l in enumerate(data.decode('utf-8', 'replace').split(NL), 1):
            if len(l) < 4:
                continue
            if len(l) > 200000:
                l = l[:200000]
                cut += 1
            t = toks(l)
            if len(t) >= 3 and WS:
                for s in line_shingles(t) & WS:
                    for k in want_sh[s]:
                        sh_line[k][(p, n)] += 1
                        sh_any[k].add(s)
            if want_fg and PRE.search(l):
                for f in figs(l):
                    if f in want_fg:
                        for k in want_fg[f]:
                            fg_hit[k].setdefault(f, (p, n))
    proc.stdin.close()
    proc.wait()
    out = []
    for k, t in enumerate(texts):
        sh, fg = Q[k]
        best = sh_line[k].most_common(1)
        out.append(dict(digest=digest(t), chars=len(t), nsh=len(sh), cov=(len(sh_any[k]) / len(sh)) if sh else None,
                        best=best[0][0] if best else None, bestcov=(best[0][1] / len(sh)) if (best and sh) else 0.0,
                        figs=sorted(fg), fhit=dict(fg_hit[k])))
    stats = dict(rev=rev, path=path or '(the whole tree)', blobs=len(seen), read=read, binary=binary, cut=cut, bytes=nbytes,
                 secs=round(time.time() - t0, 1))
    return out, stats


def verdict(r):
    if r['nsh'] and r['bestcov'] >= 1.0:
        w = 'WORDS AS WRITTEN at %s :%d' % r['best']
    elif r['cov']:
        w = 'WORDS IN PART: %.0f%% of %d runs anywhere, %.0f%% in one line (%s :%d)' % (100 * r['cov'], r['nsh'], 100 * r['bestcov'], r['best'][0], r['best'][1])
    elif r['nsh']:
        w = 'WORDS NOT FOUND (%d runs)' % r['nsh']
    else:
        w = 'NO RUN OF WORDS TO SEEK'
    f = ' ; FIGURES %d, FOUND %d%s' % (len(r['figs']), len(r['fhit']), (': ' + ', '.join('%s :%d' % v for v in sorted(set(r['fhit'].values()))[:3])) if r['fhit'] else '')
    return w + f


def stats_line(st):
    return ('the tree: %s at %s, %d blob(s), %d text read, %d binary set apart, %d line(s) cut at 200000 characters, %d bytes, %.1f s'
            % (st['path'], st['rev'], st['blobs'], st['read'], st['binary'], st['cut'], st['bytes'], st['secs']))


# ---------------------------------------------------------------- the controls
CONTROL_PATH = 'data/b753_*'
KNOWN = ('data/b753_closing.txt', 1)      # ### a line the remote main carries (b753's closing head, pushed at 34332a00)
FIGSRC = 'data/b753_dayend.txt'          # ### a pushed bank whose lines carry decimal figures


def _planted_words(seed, words):
    """the words with a token made from the seed's digest after every second word, so that no run of five stands anywhere."""
    h = hashlib.sha256(seed.encode('utf-8')).hexdigest()
    out = []
    for i, w in enumerate(words):
        out.append(w)
        if i % 2 == 1:
            out.append('q' + h[(i * 3) % 50:(i * 3) % 50 + 9])
    return ' '.join(out)


def control(repo=RELAY, rev='origin/main'):
    """(ok, lines): the three controls of (R364)(5)[Q] and the reach's own, in one pass over CONTROL_PATH at rev."""
    L = ['### THE ORIGIN SEARCH`S CONTROLS (tools/standing/originsearch.py), over %s at %s (%s)' % (CONTROL_PATH, rev, git(repo, 'rev-parse', '--short=8', rev).strip())]
    known = git(repo, 'show', '%s:%s' % (rev, KNOWN[0])).replace('\r', '').split(NL)
    kline = known[KNOWN[1] - 1] if len(known) >= KNOWN[1] else ''
    fl = git(repo, 'show', '%s:%s' % (rev, FIGSRC)).replace('\r', '').split(NL)
    fig, fln = None, None
    for n, l in enumerate(fl, 1):
        m = re.search(r'(?<![\w.:/-])\d+\.\d+(?![0-9A-Za-z_/-])', DATE.sub(' ', l))
        if m:
            fig, fln = m.group(0), n
            break
    stamp = time.strftime('%Y%m%dT%H%M%S', time.gmtime())
    planted = _planted_words('planted ' + stamp, 'this planted line of the control carries words that no blob of the tree holds as written'.split())
    planted_fig = _planted_words('figure ' + stamp, 'a sentence of other words carrying the figure'.split()) + ' ' + (fig or '') + ' ' + \
        _planted_words('figure tail ' + stamp, 'and nothing else of its line'.split())
    para = ' '.join(reversed(toks(kline)))
    texts = [kline, planted, planted_fig, para]
    R, st = search(texts, repo, rev, CONTROL_PATH)
    L.append('  ' + stats_line(st))
    C = []

    def case(name, ok, r):
        C.append(bool(ok))
        L.append('  (%d) %-74s %s ; query %s, %d characters ; %s' % (len(C), name[:74], 'AS WANTED' if ok else 'NOT AS WANTED', r['digest'], r['chars'], verdict(r)))
    k = R[0]
    case('a line known at the remote main found (%s :%d)' % KNOWN, bool(kline) and k['bestcov'] >= 1.0 and k['best'] is not None, k)
    case('a planted line not found, words nor figures', R[1]['nsh'] > 0 and not R[1]['cov'] and not R[1]['fhit'], R[1])
    f = R[2]
    case('a figure found under other words (%s, from %s :%s)' % (fig, FIGSRC, fln), fig is not None and ('N ' + fig) in f['fhit'] and not f['cov'], f)
    case('THE REACH: the known line`s words in reversed order (a paraphrase) not found as written', R[3]['nsh'] > 0 and R[3]['bestcov'] < 0.5, R[3])
    ok = sum(C) == len(C)
    L.append('### ORIGIN SEARCH CONTROLS %d OF %d %s' % (sum(C), len(C), 'AS WANTED' if ok else 'NOT AS WANTED'))
    return ok, L


def main(argv):
    if argv[:1] == ['control']:
        ok, L = control()
        print(NL.join(L))
        sys.exit(0 if ok else 1)
    if argv[:1] == ['search'] and len(argv) >= 2:
        rev = argv[argv.index('--rev') + 1] if '--rev' in argv else 'origin/main'
        path = argv[argv.index('--path') + 1] if '--path' in argv else None
        texts = [l for l in io.open(argv[1], encoding='utf-8').read().replace('\r', '').split(NL) if l.strip()]
        R, st = search(texts, RELAY, rev, path)
        print('### THE ORIGIN SEARCH: %d line(s) of the file sought ; %s' % (len(texts), stats_line(st)))
        for i, r in enumerate(R, 1):
            print('  :%d query %s, %d characters ; %s' % (i, r['digest'], r['chars'], verdict(r)))
        return
    sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
