# -*- coding: utf-8 -*-
"""standing/deletes.py -- v1.15.0, (R345)(2)(vi), b734 defect (s), G-LISTINGS-BEFORE-CLAUSES: THE DELETE STEP PRINTS THE --merged LISTING AND READS THE NAMES FROM IT BEFORE ANY DELETE, so no sentence
about the listing can be written ahead of it. b734's five deletes ran with no listing and its step-zero bank wrote "each after its --merged listing", false when written.

  python -X utf8 -u tools/standing/deletes.py list <repo> <pattern>
        prints `git branch --merged main --list <pattern>` and appends the listing to data/<act>_merged_listing.txt, its time beside it; the listing's line is the sentence
  python -X utf8 -u tools/standing/deletes.py delete <repo> <branch>
        one branch: refused unless the branch stands in the bank's last listing of that repository; `git branch -d`, one per command;
        v1.18.0, (R348)(2)(iv): refused first unless the act's citation check stands CLEAN

  listing(text) -> [(repo, names)]   allowed(text, repo, branch) -> bool
"""
import json
import os
import re
import subprocess
import sys
import time

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HEAD = re.compile(r'^### LISTING (\S+) (\S+) AT (\S+) :(.*)$', re.M)


def bank():
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f:
        return os.path.join(RELAY, 'data', '%s_merged_listing.txt' % json.load(f)['act'])


def listing(text):
    return [(m.group(1), m.group(4).split()) for m in HEAD.finditer(text or '')]


def allowed(text, repo, branch):
    rows = [n for r, n in listing(text) if r == repo]
    return bool(rows) and branch in rows[-1]


def act():
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)['act']


def citation_clean(relay=RELAY):
    """v1.18.0, (R348)(2)(iv), b737 (d): the delete step after the citation check by the tool -- the act's check banked and CLEAN, the hook's
    own reading (tools/standing/hook.py citation_done), so the order holds where the hook is not installed."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import hook
    return hook.citation_done(relay)


def rd():
    p = bank()
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def main(argv):
    if len(argv) != 3 or argv[0] not in ('list', 'delete'):
        sys.exit(__doc__)
    cmd, repo, arg = argv
    if cmd == 'list':
        out = subprocess.run(['git', '-C', repo, 'branch', '--merged', 'main', '--list', arg], capture_output=True, text=True, encoding='utf-8').stdout
        names = [x.strip(' *+') for x in out.split('\n') if x.strip()]
        row = '### LISTING %s %s AT %s : %s' % (repo, arg, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), ' '.join(names))
        with open(bank(), 'a', encoding='utf-8', newline='\n') as f:
            f.write(row + '\n')
        print(row)
        return 0
    if not citation_clean():
        print('### REFUSED: the act`s citation check has not run CLEAN (data/%s_citation_check.json, its `clean`); nothing deleted ((R348)(2)(iv))' % act())
        return 4
    if not allowed(rd(), repo, arg):
        print('### REFUSED: %s stands in no --merged listing of %s in %s; nothing deleted' % (arg, repo, os.path.basename(bank())))
        return 3
    r = subprocess.run(['git', '-C', repo, 'branch', '-d', arg], capture_output=True, text=True, encoding='utf-8')
    print((r.stdout + r.stderr).strip())
    return r.returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
