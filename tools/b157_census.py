# -*- coding: utf-8 -*-
"""b157 -- THE FEDERATION LIVE CENSUS.

### READ-ONLY. Every figure is read from the repository or from `ls-remote` AT RUN
### TIME. ### NOTHING IS FILLED FROM THE 2026-08-04 SNAPSHOT OR FROM MEMORY: a
### figure that cannot be read is printed as UNREAD, with its reason.
"""
import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = 'D:\\'


def git(repo, *args, timeout=60):
    try:
        r = subprocess.run(['git', '-C', repo] + list(args),
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', timeout=timeout)
        if r.returncode != 0:
            return None, (r.stderr or '').strip().splitlines()[:1]
        return (r.stdout or '').strip(), None
    except subprocess.TimeoutExpired:
        return None, ['TIMEOUT']
    except Exception as e:                                   # noqa: BLE001
        return None, [str(e)[:60]]


def census(name):
    repo = os.path.join(ROOT, name)
    row = {'repo': name}
    row['is_git'] = os.path.isdir(os.path.join(repo, '.git'))
    if not row['is_git']:
        row['note'] = 'NOT A GIT REPOSITORY'
        return row
    row['branch'], _ = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
    row['local'], _ = git(repo, 'rev-parse', 'HEAD')
    row['date'], _ = git(repo, 'log', '-1', '--format=%cI')
    url, _ = git(repo, 'remote', 'get-url', 'origin')
    row['remote_url'] = url
    if url:
        out, err = git(repo, 'ls-remote', 'origin', 'HEAD', timeout=120)
        if out:
            row['remote'] = out.split()[0]
        else:
            row['remote'] = None
            row['remote_err'] = (err or ['no output'])[0][:70]
    else:
        row['remote'] = None
        row['remote_err'] = 'NO ORIGIN CONFIGURED'
    tag, _ = git(repo, 'describe', '--tags', '--abbrev=0')
    row['tag'] = tag
    if tag:
        peeled, _ = git(repo, 'rev-list', '-n', '1', tag)
        row['peeled'] = peeled
    tc = os.path.join(repo, 'lean-toolchain')
    row['toolchain'] = open(tc, encoding='utf-8').read().strip() if os.path.isfile(tc) else None
    dirty, _ = git(repo, 'status', '--porcelain')
    row['dirty'] = (len(dirty.splitlines()) if dirty else 0)
    return row


def main():
    names = sorted(d for d in os.listdir(ROOT)
                   if d.startswith('SIDE-') and os.path.isdir(os.path.join(ROOT, d)))
    print("=" * 118)
    print("b157 -- THE FEDERATION LIVE CENSUS. Every figure read at run time; nothing from the snapshot.")
    print("SIDE-* directories found on %s : %d" % (ROOT, len(names)))
    print("=" * 118)
    rows = [census(n) for n in names]

    print("\n%-34s %-9s %-9s %-9s %-4s %-18s %s"
          % ("repo", "local", "remote", "agree", "drt", "tag (peeled)", "last commit"))
    print("-" * 118)
    for r in rows:
        if not r.get('is_git'):
            print("%-34s %s" % (r['repo'], "### " + r['note']))
            continue
        loc = (r['local'] or '')[:7] or 'UNREAD'
        rem = (r['remote'] or '')[:7] or 'UNREAD'
        if r['remote'] and r['local']:
            agree = 'YES' if r['remote'] == r['local'] else '### NO'
        else:
            agree = '### n/a'
        tag = r['tag'] or '(none)'
        if r.get('peeled'):
            tag = '%s %s' % (tag, r['peeled'][:7])
        print("%-34s %-9s %-9s %-9s %-4s %-18s %s"
              % (r['repo'], loc, rem, agree, r['dirty'], tag[:18], (r['date'] or 'UNREAD')[:10]))

    print("\n" + "=" * 118)
    print("### THE DIVERGENCES, NAMED PER REPO -- never summarized away.")
    print("=" * 118)
    n_ahead = n_norem = n_notag = n_dirty = 0
    for r in rows:
        if not r.get('is_git'):
            continue
        if not r['remote']:
            n_norem += 1
            print("  %-34s ### REMOTE UNREAD: %s" % (r['repo'], r.get('remote_err', '?')))
        elif r['remote'] != r['local']:
            n_ahead += 1
            print("  %-34s ### LOCAL != REMOTE  local %s  remote %s"
                  % (r['repo'], (r['local'] or '')[:12], (r['remote'] or '')[:12]))
        if not r['tag']:
            n_notag += 1
        if r['dirty']:
            n_dirty += 1
            print("  %-34s ### WORKING TREE NOT CLEAN: %d path(s)" % (r['repo'], r['dirty']))
    print("\n  totals: %d repos; %d with local != remote; %d with remote UNREAD; "
          "%d with NO TAG; %d with a dirty tree"
          % (len(rows), n_ahead, n_norem, n_notag, n_dirty))
    print("  ### A COUNT THAT COMES OUT EVEN IS NOT EVIDENCE THE RIGHT THINGS WERE COUNTED.")

    print("\n" + "=" * 118)
    print("### TOOLCHAIN PINS, as read from each repo's lean-toolchain")
    print("=" * 118)
    pins = {}
    for r in rows:
        if not r.get('is_git'):
            continue
        pins.setdefault(r['toolchain'] or '### NO lean-toolchain FILE', []).append(r['repo'])
    for k in sorted(pins, key=lambda s: (-len(pins[s]), s)):
        print("  %-42s %d repo(s)" % (k, len(pins[k])))
        if len(pins[k]) <= 8:
            for n in pins[k]:
                print("      %s" % n)
    return rows


if __name__ == '__main__':
    main()
