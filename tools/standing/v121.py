# -*- coding: utf-8 -*-
"""standing/v121.py -- THE THREE REPAIRS OF v1.2.1 ((R331)(2)), EACH WITH ITS CONTROL ON THE PREVIOUS ACT'S BANKS, BOTH INSTANCES SHOWN.

  (i)   title.py landed: G-FINDINGS-ENTRY and G-ENTRY-TITLE-FORM read the title from the author's answers bank when the author rewords it.
        RECORD: the previous act's composition against its landed line, the old reading (the composition alone) and the new.
        CONSTRUCTED: an answers bank with no word (the composition, failing against a reworded line); a word whose old phrase the
        composition does not carry (None).
  (ii)  gitwrite.py reading: one git write per message counts writes only; a git listing is not a write.
        RECORD: the previous act's shell calls (its session window), the old reading by call and the new by write, the messages over one
        each printed with their commands. CONSTRUCTED: a listing alone (0); a listing beside one write (1, passing); two writes in one
        call (2 by write, 1 by call).
  (iii) manifest.py control_at_build: the mirror's MANIFEST control reads each file against the commit the mirror is built at.
        RECORD: the previous act's zip at its build commit, every roster file, and the control its mirror bank printed (against the
        carried reference). CONSTRUCTED: the same zip read at the carried reference as if it were the build (failing, as wanted).
        Its diff printed beside (R328)(7)'s, with the reason the earlier repair did not take.

  python -X utf8 tools/standing/v121.py          prints; writes nothing
  python -X utf8 tools/standing/v121.py bank     writes data/<act>_standing_v121.txt
"""
import io
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A           # noqa: E402
import gitwrite as GW     # noqa: E402
import manifest as MF     # noqa: E402
import title as TI        # noqa: E402

NL = '\n'
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
PP = A.REPOS['pp']
REPAIR_R328 = 'a240e6b6'      # ### b718 C4: tools/standing/ v1.2.0, manifest.py new ((R328)(7))
RECUT = 'a86c9429'            # ### the carried reference b716-b720's mirror banks read


def _pp_line(n):
    t = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8').read().replace('\r', '').split(NL)
    return t[n - 1] if 0 < n <= len(t) else ''


def _window(prev):
    """the previous act's session window: from its ruling's line to the next act's (each read from the transcript's own timestamps)."""
    cur = A.current()
    path = '%s/%s.jsonl' % (PROJ, cur['prev_session'])
    first = last = None
    want_prev, want_cur = 'RULING (%s) BEGIN' % cur['prev_ruling'], 'RULING (%s) BEGIN' % cur['ruling']
    for l in io.open(path, encoding='utf-8', errors='replace'):
        if '"type":"user"' not in l.replace(' ', ''):
            continue
        try:
            j = json.loads(l)
        except ValueError:
            continue
        c = (j.get('message') or {}).get('content')
        txt = c if isinstance(c, str) else ' '.join(x.get('text', '') for x in c or [] if isinstance(x, dict))
        if first is None and want_prev in txt:
            first = j.get('timestamp')
        if first and want_cur in txt:
            last = j.get('timestamp')
            break
    return path, first, last


def lines():
    cur = A.current()
    act, prev = cur['act'], cur['prev']
    ok_all = []
    L = ['%s -- THE STANDING TOOLSET AT v1.2.1: THE THREE REPAIRS OF %s(2), EACH CONTROLLED ON %s`S BANKS, BOTH INSTANCES SHOWN (%s)' % (
        act, cur['ruling'], prev, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are cases: the repair, the instance (RECORD or CONSTRUCTED), what is read, the figure got, the figure wanted, AS WANTED.',
         '### Written by tools/standing/v121.py.', '']

    def case(rep, kind, what, got, want):
        ok = got == want
        ok_all.append(ok)
        L.append('  (%s) %-11s %s : got %s ; wanted %s ; %s' % (rep, kind, what, got, want, 'AS WANTED' if ok else '### NOT AS WANTED'))

    # ================================================================ (i)
    fj = A.jl('%s_findings.json' % prev)
    ans = A.rd('%s_author_answers.txt' % prev)
    line = _pp_line(fj.get('entry_line') or 0)
    new, notes = TI.landed(fj.get('title'), ans)
    L += ['## (i) THE TITLE THE AUTHOR REWORDED (tools/standing/title.py)',
          '    the composition (relay data/%s_findings.json `title`): %s' % (prev, fj.get('title')),
          '    the landed line (PLACE-papers FINDINGS :%s): %s' % (fj.get('entry_line'), line),
          '    the word`s changes (relay data/%s_author_answers.txt, its verbatim block): %s' % (prev, notes)]
    case('i', 'RECORD', 'the old reading, the composition alone, equal to the landed line', TI.ledger(fj.get('title') or '') == line, False)
    case('i', 'RECORD', 'the new reading, the composition with the word`s change, equal to the landed line', new == line, True)
    case('i', 'CONSTRUCTED', 'an answers bank with no word: the composition, equal to the reworded line', TI.landed(fj.get('title'), '')[0] == line, False)
    planted = ans.replace('"the law REFUTED" reads', '"the law UNREAD" reads')
    case('i', 'CONSTRUCTED', 'a word whose old phrase the composition does not carry: None', TI.landed(fj.get('title'), planted)[0], None)
    L.append('')

    # ================================================================ (ii)
    path, lo, hi = _window(prev)
    calls = GW.calls_of(path, lo or '', hi or '')
    o_ok, o_n, o_over, o_note = GW.old_reading(calls)
    n_ok, n_n, n_over, n_note = GW.reading(calls)
    L += ['## (ii) ONE GIT WRITE PER MESSAGE, COUNTING WRITES (tools/standing/gitwrite.py)',
          '    %s`s window: %s to %s (its ruling`s line to %s`s), shell calls %d' % (prev, lo, hi, cur['ruling'], len(calls)),
          '    the old reading (by call, tools/rule_arms.py :481-:488): %s' % o_note,
          '    the new reading (by write): %s' % n_note]
    over_ids = set(m for m, _t, _n in o_over) | set(m for m, _t, _n in n_over)
    for c in calls:
        if c['mid'] in over_ids:
            L.append('      %s %s : commands %s -> writes %s' % (c['ts'][:19], c['mid'][-8:], GW.commands(c['cmd']), GW.writes(c['cmd'])))
    lst = [c for c in calls if any(GW.is_listing(x) for x in GW.commands(c['cmd']))]
    L.append('    the listings in the window: %d calls, each command a listing counted 0 writes: %s' % (
        len(lst), all(not any(GW.is_listing(w) for w in GW.writes(c['cmd'])) for c in lst)))
    case('ii', 'RECORD', 'the old reading`s messages over one', len(o_over), 2)
    case('ii', 'RECORD', 'the new reading`s messages over one (the call carrying a branch and a push now counted twice)', len(n_over), 3)
    case('ii', 'RECORD', 'the listing `branch --list push-%s-*` of event (12) counted a write' % prev,
         any('--list' in w for c in calls for w in GW.writes(c['cmd'])), False)
    pl = [dict(mid='p1', ts='x', cmd='git -C D:/relay branch --list push-x-*')]
    case('ii', 'CONSTRUCTED', 'a listing alone: messages carrying a write', GW.reading(pl)[1], 0)
    pl2 = [dict(mid='p2', ts='x', cmd='git -C D:/relay branch push-x 1234567; git -C D:/relay branch --list push-x-*')]
    case('ii', 'CONSTRUCTED', 'a listing beside one write: the reading passes', GW.reading(pl2)[0], True)
    pl3 = [dict(mid='p3', ts='x', cmd='git -C D:/relay branch push-x 1234567; bash tools/push_gated.sh /d/relay push-x')]
    case('ii', 'CONSTRUCTED', 'two writes in one call: (new over one, old over one)', (len(GW.reading(pl3)[2]), len(GW.old_reading(pl3)[2])), (1, 0))
    L.append('')

    # ================================================================ (iii)
    mj = A.jl('%s_mirror.json' % prev)
    zp, build = mj.get('zip'), A.gs('pp', 'rev-parse', mj.get('pp_head') or 'HEAD')
    new_c = MF.control_at_build(zp, build)
    stale = MF.control_at_build(zp, RECUT)
    old_rows = mj.get('manifest_control') or []
    L += ['## (iii) THE MIRROR`S MANIFEST CONTROL AT THE BUILD COMMIT (tools/standing/manifest.py control_at_build)',
          '    %s`s zip %s, built at PLACE-papers %s (its mirror bank`s `pp_head`)' % (prev, zp, (build or '')[:8]),
          '    the old control (relay data/%s_mirror.json `manifest_control`, against %s): %s' % (
              prev, RECUT, [(r.get('path'), r.get('lf_equal')) for r in old_rows]),
          '    the new control: rows %d, AS WANTED %d, NOT AS WANTED %s' % (
              len(new_c['rows']), sum(1 for r in new_c['rows'] if r[4] == 'AS WANTED'), [r[0] for r in new_c['rows'] if r[4] == 'NOT AS WANTED'] or 'NONE')]
    case('iii', 'RECORD', 'the old control (the carried reference) as its bank printed it, all equal', all(r.get('lf_equal') for r in old_rows), False)
    case('iii', 'RECORD', 'the new control at the build commit, every roster file', new_c['ok'], True)
    case('iii', 'CONSTRUCTED', 'the same zip read at the carried reference %s as if it were the build' % RECUT, stale['ok'], False)
    L.append('      the stale reading`s rows NOT AS WANTED: %s' % [r[0] for r in stale['rows'] if r[4] == 'NOT AS WANTED'])
    callers = [l for l in (A.gs('relay', 'grep', '-n', '-e', 'MF.control', '--', 'tools') or '').split(NL) if l.strip()]
    L += ['    the callers of MF.control and MF.control_at_build in tools/ now: %s' % (callers or 'NONE'),
          '    THE REASON (R328)(7)`S REPAIR DID NOT TAKE: it added tools/standing/manifest.py (relay %s) and its only caller was the class controls '
          'in tools/standing/classes.py; the record tool`s mbank route, which writes the mirror bank, kept its inline loop against the carried '
          'K.RECUT_MERGE through every carry from b718 to %s. v1.2.1 wires the control into %s`s mbank (control_at_build at PLACE-papers HEAD) '
          'and removes the inline loop.' % (REPAIR_R328, prev, act),
          '', '### (R328)(7)`S REPAIR, relay %s, tools/standing/manifest.py (git show):' % REPAIR_R328]
    L += ['    ' + l for l in (A.gs('relay', 'show', '--format=', REPAIR_R328, '--', 'tools/standing/manifest.py') or '').split(NL)]
    L += ['', '### BESIDE IT, v1.2.1`S REPAIR, tools/standing/manifest.py against the act`s starting relay head %s (git diff):' % cur['pre_relay'][:8]]
    L += ['    ' + l for l in (A.gs('relay', 'diff', cur['pre_relay'], '--', 'tools/standing/manifest.py') or '').split(NL)]
    L += ['', '### AND ITS WIRING, tools/%s_record.py mbank against tools/%s_record.py`s inline loop (the act`s edit since its step-zero carry, git diff):' % (act, prev)]
    base = A.step_commit(act, 'step zero')
    d = A.gs('relay', 'diff', base or 'HEAD', '--', 'tools/%s_record.py' % act) or ''
    L += ['    ' + l for l in d.split(NL)]
    n_ok = sum(ok_all)
    L += ['', '### ### **v1.2.1: CASES %d, AS WANTED %d ; (i) THE TITLE FROM THE ANSWERS BANK ; (ii) WRITES COUNTED, A LISTING 0 ; (iii) THE CONTROL AT THE '
          'BUILD COMMIT, WIRED INTO mbank.**' % (len(ok_all), n_ok)]
    return L, act, all(ok_all)


def main(route):
    L, act, ok = lines()
    if route == 'bank':
        p = os.path.join(A.D, '%s_standing_v121.txt' % act)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    for l in L:
        if not l.startswith('    ') or 'NOT AS WANTED' in l:
            print(l[:300])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
