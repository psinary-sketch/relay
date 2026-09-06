# -*- coding: utf-8 -*-
"""b337_techne.py -- THE NINE AUGUST TECHNE MODULE FILES COMMITTED TO THE CANONICAL LOCAL CLONE, NOT PUSHED.

### ### **THE RULING, THE AUTHOR'S, RATIFIED BY THE SORTIE PASTE:** *"The nine August TECHNE module files are committed to
### the canonical local clone, not pushed."* ### The clone is `D:\\MY-DOwnloads\\TECHNE-Core`; the nine files are staged BY
### EXPLICIT LIST (never `-A`; `.claude/settings.local.json` stays unstaged); one commit; ### **NO PUSH** -- the remote is
### read by `ls-remote` before and after and must be unchanged; the clone must be exactly two commits ahead of the
### remote afterwards; the second clone `D:\\MY-DOwnloads\\TECHNE_Core` is read and must be untouched. ### Idempotent: if
### the nine files are already tracked, nothing is committed and the state is read back.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TC2 = r'D:\MY-DOwnloads\TECHNE_Core'
NINE = ['BANKED_MEANINGS_ENGINE.md', 'DECISION_CARD_FORMAT.md', 'DISCRIMINATOR_PROTOCOL.md', 'FACE_OFF_PROTOCOL.md', 'HARNESS_LORE.md',
        'IMPORT_LEDGER.md', 'INDEX.md', 'RENDER_AS_E0.md', 'SIGNEDNESS.md']
MSG = ("modules/2026-08: the nine August method modules committed to the canonical local clone, NOT PUSHED "
       "(b337, leg 2 of the sortie; the author's ruling ratified by the sortie paste of 2026-09-06).\n\n"
       "The nine files: " + ', '.join(NINE) + ". Staged by explicit list; the remote read before and after and unchanged; "
       "private until the four provisionals are filed.\n\n"
       "Claude-Session: https://claude.ai/code/session_01ELiKF4s74Yfw58E7zXDx9M\n")
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip(), r.returncode


def main():
    rec('=' * 100)
    rec('b337 -- THE NINE AUGUST TECHNE MODULE FILES, COMMITTED LOCALLY, NOT PUSHED.')
    rec('=' * 100)
    remote_before, _ = git(TC, 'ls-remote', 'origin', 'main')
    head_before, _ = git(TC, 'rev-parse', 'HEAD')
    branch, _ = git(TC, 'rev-parse', '--abbrev-ref', 'HEAD')
    rec('  clone %s on %s at %s ; remote main %s' % (TC, branch, head_before[:7], remote_before.split()[0][:7] if remote_before else 'UNREAD'))
    c2_head, _ = git(TC2, 'rev-parse', 'HEAD')
    c2_status, _ = git(TC2, 'status', '--porcelain')
    rec('  the second clone %s at %s ; status lines %d (read, not touched)' % (TC2, c2_head[:7], len(c2_status.splitlines()) if c2_status else 0))
    tracked, _ = git(TC, 'ls-files', '--', 'modules/2026-08')
    tracked_set = set(x.replace('modules/2026-08/', '') for x in tracked.splitlines())
    present = [n for n in NINE if os.path.exists(os.path.join(TC, 'modules', '2026-08', n))]
    rec('  present on disk %d of %d ; already tracked %d' % (len(present), len(NINE), len(tracked_set & set(NINE))))
    if len(present) != len(NINE):
        rec('  ### REFUSING -- not all nine files are present.')
        rec('=' * 100)
        return 1
    if set(NINE) <= tracked_set:
        rec('  ALREADY COMMITTED -- nothing staged, nothing committed (idempotent).')
        committed = False
    else:
        paths = ['modules/2026-08/' + n for n in NINE]
        _o, rc = git(TC, 'add', '--', *paths)
        staged, _ = git(TC, 'diff', '--cached', '--name-only')
        staged_set = set(staged.splitlines())
        rec('  staged by explicit list : %d paths ; settings.local.json staged : %s' % (len(staged_set), '.claude/settings.local.json' in staged_set))
        if staged_set != set(paths):
            rec('  ### REFUSING -- the staged set is not exactly the nine.')
            git(TC, 'reset', '-q')
            rec('=' * 100)
            return 1
        msgp = os.path.join(D, 'b337_techne_commit_msg.txt')
        open(msgp, 'wb').write(MSG.encode('utf-8'))
        _o, rc = git(TC, 'commit', '-q', '-F', msgp)
        committed = (rc == 0)
        rec('  committed : %s' % committed)
    head_after, _ = git(TC, 'rev-parse', 'HEAD')
    subj, _ = git(TC, 'log', '-1', '--format=%h %s')
    remote_after, _ = git(TC, 'ls-remote', 'origin', 'main')
    remote_sha = remote_after.split()[0] if remote_after else ''
    ahead, _ = git(TC, 'rev-list', '--count', '%s..HEAD' % remote_sha) if remote_sha else ('?', 0)
    tracked2, _ = git(TC, 'ls-files', '--', 'modules/2026-08')
    n_tracked = len([x for x in tracked2.splitlines() if x.replace('modules/2026-08/', '') in NINE])
    unstaged_settings = '.claude/settings.local.json' in (git(TC, 'status', '--porcelain')[0])
    c2_head2, _ = git(TC2, 'rev-parse', 'HEAD')
    rec('  HEAD now %s -- %s' % (head_after[:7], subj[:110]))
    rec('  remote main before %s ; after %s ; UNCHANGED %s ; NOT PUSHED : the clone is %s commits ahead of the remote' % (remote_before.split()[0][:7] if remote_before else '?', remote_sha[:7], remote_before == remote_after, ahead))
    rec('  the nine tracked at HEAD : %d of 9 ; settings.local.json still unstaged : %s ; the second clone unchanged : %s' % (n_tracked, unstaged_settings, c2_head == c2_head2))
    rec('=' * 100)
    ok = (n_tracked == 9 and remote_before == remote_after and str(ahead) == '2' and c2_head == c2_head2)
    return 0 if ok else 1


if __name__ == '__main__':
    code = main()
    wrote = any('committed : True' in x for x in LINES)
    base = 'b337_techne_run' if wrote else 'b337_techne_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
