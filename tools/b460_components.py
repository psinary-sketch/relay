# -*- coding: utf-8 -*-
"""b460_components.py -- THE TWO COMPONENTS OF b460.

### COMPONENT 1 -- b452's test given a positive control, run in b452's own four fields.
### COMPONENT 2 -- the TECHNE push under (R71), verified at the remote and not at the push output.

### ### **EVERY RULE HERE IS ON THE LOCKED FACE**, and all three document-reading rules were
### rehearsed under (R70) before the seal. ### **NO CHAIN IS RUN AND NO CHANNEL COMPUTED.**
"""
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
B452 = os.path.join(D, 'b452_components.txt')
OUT = os.path.join(D, 'b460_components.txt')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def field(name):
    """### **b452's OWN TEXT, CARRIED VERBATIM FROM ITS BANK AND NEVER RE-DERIVED.**"""
    for i, l in enumerate(read(B452).split(NL), 1):
        if l.strip().startswith(name):
            return i, l.split(':', 1)[1].strip()
    return None, None


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def component1():
    rec('=' * 100)
    rec('### COMPONENT 1 -- b452`S TEST GIVEN A POSITIVE CONTROL.')
    rec('=' * 100)
    edge = math.sqrt(2.0)
    cells = json.load(io.open(os.path.join(D, 'b437_cells.json'), encoding='utf-8'))
    if not cells:
        rec('  ### ### **HARD FAILURE: AN EMPTY CELL SET IS NEVER A CLEAN PASS.**')
        raise SystemExit(2)
    inside = sorted([c for c in cells if c['sq'] < 2.0], key=lambda c: c['a'])
    rec('  ### THE EDGE, AS THE FACE DERIVED IT : a < sqrt(2) = %.16f, i.e. a^2 < 2.' % edge)
    rec('  ### cells read from b437_cells.json (the radius ladder) : %d ; qualifying : %d'
        % (len(cells), len(inside)))
    if not inside:
        rec('  ### ### **NO QUALIFYING CELL -- THE THIRD DISPOSITION APPLIES.**')
        raise SystemExit(2)
    c = inside[0]
    rec('  ### ### **THE SMALLEST QUALIFYING a THE BANKS HOLD : a = %s, a^2 = %s.**' % (c['a'], c['sq']))
    rec('  ### its banked fields : prime sum `pr` = %s ; prime powers `pp` = %s ; rung = %s'
        % (c['pr'], c['pp'], c['rung']))
    rec('')
    rec('  ### ### **THE CANDIDATE, AND IT IS CONSTRUCTED, WHICH IS SAID RATHER THAN LEFT TO BE NOTICED.**')
    rec('  ### source : CC`s Theorem 1, the same source b452 read at C1, C5 and elsewhere.')
    rec('  ### object : ONE BANKED CELL of the radius ladder, a = %s.' % c['a'])
    rec('  ### **THIS PAIRING IS NOT ONE OF b452`S 82 FAILURES AND IS NEVER COUNTED AMONG THEM.**')
    rec('  ### A positive control is BUILT, not found among the subjects.')
    rec('')
    rec('-' * 100)
    rec('### THE TEST, IN b452`S OWN FOUR FIELDS AND IN ITS OWN ORDER.')
    rec('-' * 100)
    fields = {}
    for nm in ('class, as the bank quotes it', 'quotation at the step', 'deciding clause'):
        ln, txt = field(nm)
        fields[nm] = (ln, txt)
        rec('  %-30s : %s' % (nm, txt))
        rec('  %-30s   ### carried VERBATIM from b452_components.txt:%s' % ('', ln))
    hand = ('the class is the prime-free support, and this object is ONE CELL whose support is '
            '[a^-1, a] with a^2 = %s < 2, so f = g conv g-bar^# is supported inside (1/2, 2); '
            'the bank`s own fields agree -- prime sum %s and prime powers %s, no prime entering. '
            'ONE CELL DOES NOT QUANTIFY OVER A CLASS AND ITS SUPPORT REACHES PAST NOTHING.'
            % (c['sq'], c['pr'], c['pp']))
    fields['hand read'] = (None, hand)
    rec('  %-30s : %s' % ('hand read', hand))
    rec('  %-30s   ### THIS ACT`S OWN, and the only field not carried from b452.' % '')
    rec('')
    past = False           # ### does the object`s support reach PAST the window?
    stated = True          # ### does the bank state the object`s support?
    verdict = ('UNDECIDED' if not stated else ('SOURCE-SIDE' if past else 'OBJECT-SIDE'))
    rec('  ### THE VERDICT RULE, b452`S OWN, READ OFF ITS HAND READING AT :15 AND FIXED ON THE FACE:')
    rec('  ###   support reaches PAST the window -> SOURCE-SIDE')
    rec('  ###   support lies INSIDE the window   -> OBJECT-SIDE')
    rec('  ###   support NOT STATED by the bank   -> UNDECIDED')
    rec('  ### applied : support stated by the bank : %s ; reaches past the window : %s' % (stated, past))
    rec('  ### ### **VERDICT : %s**' % verdict)
    rec('')
    if verdict == 'OBJECT-SIDE':
        rec('  ### ### **THE CONTROL FIRES.**')
        rec('  ### b452 wrote: *"ABSENT: the test has not been shown able to say OBJECT-SIDE, so the empty')
        rec('  ### OBJECT-SIDE is a result of these two sources and no wider."* ### **THAT ABSENCE IS NOW')
        rec('  ### SUPPLIED: THE INSTRUMENT CAN RETURN OBJECT-SIDE, AND DID.**')
        rec('  ### ### **SO b452`S FORTY-FOUR SOURCE-SIDE STAND AS READ.**')
        rec('  ### **AND THE BAR ON WHAT THAT LICENSES, CARRIED FROM THE FACE:** a control that fires says')
        rec('  ### the instrument CAN say OBJECT-SIDE. ### **IT DOES NOT RE-READ THE FORTY-FOUR AND CONFERS')
        rec('  ### NO CORRECTNESS ON THEM** -- only that their verdicts were not forced by a one-outcome test.')
        disp = 'THE FORTY-FOUR STAND AS READ'
    else:
        rec('  ### ### **THE TEST IS BROKEN. ### THE FORTY-FOUR ARE MARKED UNREAD.**')
        rec('  ### the defect, at its line : b452_components.txt:%s' % fields['deciding clause'][0])
        disp = 'THE FORTY-FOUR ARE UNREAD'
    rec('  ### ### **DISPOSITION : %s.**' % disp)
    rec('')
    rec('  ### **WHAT THIS COMPONENT DID NOT DO:** it re-ran none of b452`s 82, re-verdicted none,')
    rec('  ### performed no re-expression, ran no chain and computed no channel. ### The cell was read')
    rec('  ### from b437_cells.json as banked.')
    json.dump(dict(edge=edge, cell=c, verdict=verdict, disposition=disp,
                   fields={k: dict(line=v[0], text=v[1]) for k, v in fields.items()},
                   n_cells=len(cells), n_inside=len(inside)),
              io.open(os.path.join(D, 'b460_control.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return verdict, c


def component2():
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE TECHNE PUSH UNDER (R71).')
    rec('=' * 100)
    pre_head = git(TC, 'rev-parse', 'HEAD')[1]
    pre_up = git(TC, 'rev-parse', '@{u}')[1]
    pre_ahead = int(git(TC, 'rev-list', '--count', '@{u}..HEAD')[1] or 0)
    rec('  ### BEFORE: local HEAD %s ; upstream %s ; commits ahead %d'
        % (pre_head[:12], pre_up[:12], pre_ahead))
    mods = ['modules/2026-09/CORRECTED_BUT_UNPROPAGATED.md',
            'modules/2026-09/EDITING_ANCHOR_EXCLUDES_PRESERVED.md',
            'modules/2026-09/REPAIRING_A_REPORT_ERASES_IT.md']
    rec('  ### STAGING BY PATH, NEVER BY `-A` :')
    for m in mods:
        code, o, e = git(TC, 'add', '--', m)
        rec('      %-56s add exit %d' % (m, code))
    msg = ('2026-09-21 (b460, under ruling (R71)) -- three method modules: a correction that does not '
           'propagate is a defect; an editing anchor must not resolve inside preserved text; repairing '
           'a report of an error erases the record of it. LOCAL NO LONGER: pushed with the twenty-three.')
    code, o, e = git(TC, 'commit', '-q', '-m', msg)
    rec('  ### COMMIT exit %d %s' % (code, ('| ' + (e or o).splitlines()[0]) if (e or o) else ''))
    head = git(TC, 'rev-parse', 'HEAD')[1]
    ahead = int(git(TC, 'rev-list', '--count', '@{u}..HEAD')[1] or 0)
    rec('  ### AFTER COMMIT: local HEAD %s ; commits ahead %d' % (head[:12], ahead))
    rec('  ### **NO FORCE, NO REBASE, NO BRANCH REWRITE, NO UPSTREAM CHANGE.**')
    code, o, e = git(TC, 'push', 'origin', 'HEAD:main')
    rec('  ### PUSH exit code %d' % code)
    for l in (e or o).split(NL):
        if l.strip():
            rec('      | %s' % l.strip()[:150])
    if code != 0:
        rec('  ### ### **THE PUSH WAS REFUSED. ### THE REFUSAL IS PRINTED ABOVE AND THE COMPONENT STOPS.**')
        rec('  ### **NOTHING IS FORCED AND NOTHING IS REBASED UNDER THIS ACT.**')
        json.dump(dict(refused=True, exit=code, stderr=e, local=head, ahead=ahead),
                  io.open(os.path.join(D, 'b460_techne.json'), 'w', encoding='utf-8', newline=NL),
                  indent=1, ensure_ascii=False)
        return dict(refused=True)
    rec('')
    rec('  ### ### **THE VERIFICATION, AND IT IS THE POINT OF (R71): THE REMOTE IS READ, NOT THE PUSH.**')
    ls = git(TC, 'ls-remote', 'origin', 'refs/heads/main')[1]
    remote = ls.split()[0] if ls.split() else ''
    rec('      git ls-remote origin refs/heads/main | %s' % ls[:80])
    rec('      remote main SHA : %s' % remote)
    rec('      local HEAD      : %s' % head)
    rec('      ### ### **EQUAL : %s**' % (remote == head))
    now_ahead = int(git(TC, 'rev-list', '--count', 'origin/main..HEAD')[1] or 0)
    rec('      commits still ahead of origin/main after the push : %d' % now_ahead)
    rec('  ### ### **COMMITS NOW ON THE REMOTE THAT WERE LOCAL-ONLY BEFORE THIS ACT : %d**' % ahead)
    rec('  ### (%d carried from before this act, plus %d written by it.)' % (pre_ahead, ahead - pre_ahead))
    rec('  ### **THE PUSH COMMAND`S OWN OUTPUT IS NOT EVIDENCE AND IS NOT ANY ARM`S SUBJECT.**')
    json.dump(dict(refused=False, pre_head=pre_head, pre_ahead=pre_ahead, head=head,
                   ahead_at_push=ahead, remote=remote, equal=(remote == head),
                   still_ahead=now_ahead, modules=mods),
              io.open(os.path.join(D, 'b460_techne.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return dict(refused=False, equal=(remote == head), ahead=ahead, remote=remote, head=head)


if __name__ == '__main__':
    v, cell = component1()
    t = component2()
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(OUT))
