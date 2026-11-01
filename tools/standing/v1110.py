# -*- coding: utf-8 -*-
"""standing/v1110.py -- THE CONTROLS OF v1.11.0 ((R341)(2)(i)-(vii)), in v1100.py's form: each instance replayed through the route as it stood before the repair (read at BASE, the commit
before this version) and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Written at b731 by the Write tool.

  python -X utf8 tools/standing/v1110.py control [face|price|rerun|postlock|arms|word|questions ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v1110.txt with every control run, nothing else.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import act_close as AC          # noqa: E402
import allow as AL              # noqa: E402
import cites as CT              # noqa: E402
import faceform as FF           # noqa: E402
import hook as HK               # noqa: E402
import pricebank as PB          # noqa: E402
import repeat as RP             # noqa: E402

BASE = '64f0d801'               # ### relay's step-zero tip: every route of v1.10.0 as it stood
EF = 'D:/SIDE-explicit-formula'
ZQ_TIP = '5688816e'             # ### zq-b730 at b730's close
B730_LOCK_AT = '2026-11-01T10:46:41Z'
B731_BEGUN_AT = '2026-11-01T13:46:00Z'   # ### a scan printed after this is b731's step zero and not b730's
TRANSCRIPT = os.path.expanduser('~/.claude/projects/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf.jsonl')


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def rd(name):
    with open(os.path.join(D, name), encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r', '')


def base(rel):
    return _git('show', '%s:%s' % (BASE, rel))


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.10.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.11.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case with no failing side: what the repair must leave standing, printed as that and not as a before and after."""
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.11.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def w_section(face):
    return face[face.find('(W) THE WRITE LIST'):face.find('(Z) THE NOTHINGS')]


def control_face():
    L, g, n = ['### (face) THE COMPOSER READS THE CLAUSES INTO (W), (R341)(2)(i); THE INSTANCE, (R340)(6)`S MOVE'], 0, 0
    ruling, face = rd('b730_ferry.txt'), rd('b730_registration_2026-11-01.txt')
    target = 'data/b729_hook_refusals.txt'
    pats = AC.w_patterns(face)
    row = FF.w_row(ruling, w_section(face))
    lines = face.split(NL)
    at = [i for i, l in enumerate(lines) if '(Z) THE NOTHINGS' in l][0]
    after = AC.w_patterns(NL.join(lines[:at] + [row or ''] + lines[at:]))
    n += 1
    g += case(L, 'face', 'b730`s face and (R340)(6): "data/b728_hook_refusals.txt`s two rows read and moved to b729`s bank by one commit"',
              'the (W) list by hand, %d patterns: %s allowed %s, a write of b730 outside its own list; clause_writes at BASE %s' % (len(pats), target, AC.w_allows(target, pats), 'def clause_writes' in base('tools/standing/faceform.py')),
              'the composer`s row: %s ; %s allowed %s' % (row, target, AC.w_allows(target, after)), not AC.w_allows(target, pats), AC.w_allows(target, after))
    own = FF.clause_writes(rd('b731_ferry.txt'))
    n += 1
    g += guard(L, 'face', 'a path only cited is not a write: (R341) cites data/b729_count_price.txt, data/b730_continuation.txt, reads them, and neither is picked; its two plan banks are', ' '.join(own),
               'data/b729_count_price.txt' not in own and 'data/b730_continuation.txt' not in own and 'data/b731_logderiv_plan.txt' in own and 'data/b731_zeros_plan.txt' in own)
    return L, g, n


def control_price():
    L, g, n = ['### (price) THE MEASURED ROW BESIDE THE ESTIMATE, (R341)(2)(ii), %s; THE INSTANCE, b730`S CONTINUATION FIELD' % PB.FORM], 0, 0
    mods = ('Lattice', 'Theta', 'FEPair', 'Continuation')
    each = [len(_git('show', '%s:SIDEExplicitFormula/Schema/ZQ/%s.lean' % (ZQ_TIP, m), repo=EF).split(NL)) - 1 for m in mods]
    runs = [r['run'] for r in json.loads(rd('b730_dispatch_rows.json')) if r.get('kind') == 'dispatch']
    row = PB.measured('continuation', 'the theta route of Schema/ZQ at %s' % ZQ_TIP, sum(each), runs)
    est = dict(field='continuation', est_lines=(1500, 3000), est_disp=(25, 50), source='data/b729_count_price.txt', row=row)
    r = PB.ratio(row, est['est_lines'], est['est_disp'])
    bank = rd('b729_count_price.txt')
    L += ['  the lines by module, read from the tree: %s ; the runs: %s' % (dict(zip(mods, each)), runs)] + PB.rows_text([est])
    n += 1
    g += case(L, 'price', 'the bank beside the build: 1,500-3,000 lines, 25-50 dispatches', 'data/b729_count_price.txt holds the measured 835: %s ; pricebank.py at BASE: %s' % ('835' in bank, bool(base('tools/standing/pricebank.py'))),
              'measured %d lines, %d dispatches, the ratio %.3f-%.3f ; %.3f-%.3f, the figures of (R341)(2)(ii)' % ((row['lines'], row['dispatches']) + r),
              '835' not in bank, row['lines'] == 835 and row['dispatches'] == 6 and ('%.3f %.3f %.2f %.2f' % r) == '0.278 0.557 0.12 0.24')
    try:
        PB.measured('continuation', 'x', 835, [])
        refused = False
    except ValueError:
        refused = True
    n += 1
    g += guard(L, 'price', 'a measured row with no run id is refused', 'refused %s' % refused, refused)
    return L, g, n


def control_rerun():
    L, g, n = ['### (rerun) A STAMPED ROUTE`S RE-RUN TO A SUFFIXED PATH, (R341)(2)(iii); THE INSTANCE, b730`S ROWGEN'], 0, 0
    log = _git('log', '--format=%h', '--', 'data/b730_rowgen_stepzero.txt').split()
    otpl = base('tools/standing/fold/record.tpl')
    ntpl = open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read()
    nm = A.stamped_name(D, 'b730_rowgen_stepzero.txt')
    n += 1
    g += case(L, 'rerun', 'data/b730_rowgen_stepzero.txt, the stamp at 3b661a42, re-run at d533a5c0 (b730 event (5)); the bank`s commits %s' % log, "the route wrote the one name: put_txt('%%s_rowgen_%%s.txt' %% (ACT, stage), L) stands %s, the stamp moved" % ("    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)" in otpl),
              'the route takes stamped_name: %s ; the first bank unedited' % nm, "    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)" in otpl and len(log) >= 2, nm == 'b730_rowgen_stepzero_rerun1.txt' and 'stamped_name(D,' in ntpl)
    have = set(['a.txt', 'a_rerun1.txt'])
    two = A.stamped_name('', 'a.txt', exists=lambda p: p in have)
    fresh = A.stamped_name('', 'b.txt', exists=lambda p: p in have)
    n += 1
    g += guard(L, 'rerun', 'a first run keeps the plain name; a third takes the next suffix', '%s ; %s' % (fresh, two), fresh == 'b.txt' and two == 'a_rerun2.txt')
    return L, g, n


def printed_scans(after, before):
    """the scans b730 printed after its lock, from the session's transcript: (stamp, the bank-form text), no text of it banked here."""
    uses, out = {}, []
    for l in open(TRANSCRIPT, encoding='utf-8', errors='replace'):
        try:
            j = json.loads(l)
        except ValueError:
            continue
        c = (j.get('message') or {}).get('content')
        for b in c if isinstance(c, list) else ():
            if not isinstance(b, dict):
                continue
            if b.get('type') == 'tool_use' and re.search(r'b730_address_scan\.py scan\s*$', str((b.get('input') or {}).get('command'))) and after < j.get('timestamp', '') < before:
                uses[b['id']] = j['timestamp']
            if b.get('type') == 'tool_result' and b.get('tool_use_id') in uses:
                t = b.get('content')
                out.append((uses[b['tool_use_id']], t if isinstance(t, str) else ' '.join(x.get('text', '') for x in t if isinstance(x, dict))))
    return out


def kinds(tpl):
    ln = [l for l in tpl.split(NL) if l.startswith('EXCLUDE_KINDS = ')][0]
    return re.search(r"\+ r'([^']*)'", ln).group(1)


def control_postlock():
    L, g, n = ['### (postlock) THE POST-LOCK SCAN`S BANK OUT OF THE LOCK`S HASH, (R341)(2)(iv); THE INSTANCE, b730`S PRINTED SCANS'], 0, 0
    rows = printed_scans(B730_LOCK_AT.replace('Z', '.000Z'), B731_BEGUN_AT.replace('Z', '.000Z'))
    text = ''
    for at, t in rows:
        text = A.scan_append(text, at, t)
    name = A.scan_bank_name('b730', True)
    ok = [t for _, t in rows if 'NO NEW OCCURRENCE' in t]
    head = len(re.findall(r'(?m)^## THE RUN AFTER THE LOCK, ', text))
    oldk, newk = kinds(base('tools/standing/fold/record.tpl')), kinds(open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read())
    rx = lambda k: re.compile(r'^b730_(%s)(\.|$)' % k)   # noqa: E731
    n += 1
    g += case(L, 'postlock', 'b730`s scans after its lock %s, printed and in no bank: %d read from the session`s transcript, %d carrying the scan`s head, first %s last %s (bounded at b731`s start %s; the texts entered in the bank form in memory and not banked here, the count being what the control needs)' % (B730_LOCK_AT, len(rows), len(ok), rows[0][0] if rows else None, rows[-1][0] if rows else None, B731_BEGUN_AT),
              'the root`s exclusion takes %s: %s, so a written bank sits in the root and a hashed name after the lock' % (name, bool(rx(oldk).match(name))),
              'entered into the form, %d runs of %d under their heads, %d characters; the exclusion takes it: %s ; the lock`s excluded list names it: %s' % (head, len(rows), len(text), bool(rx(newk).match(name)), 'data/' + name in A.post_lock_appended('b730')),
              not rx(oldk).match(name), len(rows) >= 1 and head == len(rows) and rx(newk).match(name) and 'data/' + name in A.post_lock_appended('b730'))
    keep = 'b730_address_scan.txt'
    n += 1
    g += guard(L, 'postlock', 'the pre-lock scan bank stays in the lock and the root', '%s taken by the exclusion: %s' % (keep, bool(rx(newk).match(keep))), not rx(newk).match(keep))
    return L, g, n


def control_arms():
    L, g, n = ['### (arms) THE SEAT`S THREE, (R341)(2)(v): G-RULE-SUITE-PART-CALLS, G-SEALED-AFTER-COMPONENTS, G-BRANCHES-BANKED, EACH REFUSED AT THE SEAT`S HAND, EACH WITH ITS EVENT`S CONTROL. A READ OF b730`S CALLS CANNOT BE REPAIRED: THE CURE IS THE REFUSAL NEXT TIME'], 0, 0
    d = tempfile.mkdtemp(prefix='v1110-')
    os.makedirs(os.path.join(d, 'data'))
    with open(os.path.join(d, 'data', 'act_current.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(act='b730', next='b731'), f)
    oldt = base('tools/standing/hook.py')
    chained = 'python -X utf8 -u tools/standing/fold.py checks --combine b730_arms_prerun.txt && python -X utf8 -u tools/standing/fold.py checks --prev --part standing-a'
    r = HK.judge('Bash', {'command': chained}, d)
    n += 1
    g += case(L, 'arms', 'b730 event (1), 11:10:34Z, G-RULE-SUITE-PART-CALLS: `%s`' % chained, "the hook carried no such kind: 'SUITE' in the hook %s, the call ran" % ("'SUITE'" in oldt), 'refused %s' % (r,), "'SUITE'" not in oldt, bool(r) and r[0] == 'SUITE')
    alone = HK.judge('Bash', {'command': 'python -X utf8 -u tools/standing/fold.py checks --prev --part standing-a'}, d)
    n += 1
    g += guard(L, 'arms', 'one part alone runs', 'judged %s' % (alone,), alone is None)
    rows = (json.loads(rd('b730_steps.json')).get('rows') or [])
    before = [x for x in rows if x['commit'][:8] < 'zzzzzzzz' and x['at'] < '2026-11-01T11:34:38Z']
    try:
        RP.one_lock(before, 'lock')
        said = None
    except SystemExit as e:
        said = str(e)
    tplo = base('tools/standing/fold/record.tpl')
    n += 1
    g += case(L, 'arms', 'b730 event (2), 11:34:38Z, G-SEALED-AFTER-COMPONENTS: a835a8cd named `lock` with 0d3c026f standing: rows of phase lock in b730`s steps %d' % sum(1 for x in rows if x.get('phase') == 'lock'), 'the step recorder at BASE checks a lock row: %s, the row written' % ('one_lock' in tplo), 'refused: %s' % said, 'one_lock' not in tplo, bool(said) and 'seal' in said)
    n += 1
    g += guard(L, 'arms', 'the first lock row and a `seal` row after it pass', '%s ; %s' % (len(RP.one_lock([], 'lock')), len(RP.one_lock(before, 'seal'))), RP.one_lock(before, 'seal') == before)
    c = json.loads(rd('b730_citation_check.json'))
    delete = 'git -C /d/relay branch -d push-b729-closing'
    r0 = HK.judge('Bash', {'command': delete}, d)
    with open(os.path.join(d, 'data', 'b730_citation_check.json'), 'w', encoding='utf-8') as f:
        f.write('{}')
    r1 = HK.judge('Bash', {'command': delete}, d)
    n += 1
    g += case(L, 'arms', 'b730 event (8), G-BRANCHES-BANKED: the first delete 08:39:51Z, the citation check`s first_at %s' % c.get('first_at'), "the hook carried no such kind: 'ORDER' in the hook %s, the delete ran" % ("'ORDER'" in oldt), 'before the check: refused %s' % (r0,), "'ORDER'" not in oldt, bool(r0) and r0[0] == 'ORDER')
    n += 1
    g += guard(L, 'arms', 'after the check the delete runs', 'judged %s' % (r1,), r1 is None)
    return L, g, n


def control_word():
    L, g, n = ['### (word) THE CITATION CHECK OVER THE AUTHOR`S WORD, (R341)(2)(vi); THE INSTANCE, b730`S ROOT WORD, VACUOUS'], 0, 0
    word = rd('b730_author_answers.txt').split(NL)[12]
    ck = rd('b730_answer_check.txt')
    rows = CT.word_rows(word, act='b730')
    for r in rows:
        L.append('    %-11s %-22s %s' % (r[0], r[1], 'FOUND' if r[2] else 'NOT FOUND'))
    tpl = open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()
    n += 1
    g += case(L, 'word', 'data/b730_author_answers.txt :13, %d characters' % len(word), 'the check read paths, ledger lines and commits alone: "%s"' % next((l.strip()[:120] for l in ck.split(NL) if re.search(r'(?i)cites?\b', l)), None), 'word_rows yields %d rows, %d found, %d not, the route reading it: %s' % (len(rows), sum(1 for r in rows if r[2]), sum(1 for r in rows if not r[2]), 'word_rows(best)' in tpl),
              'VACUOUS' in ck or ' 0 ' in ck, len(rows) >= 1 and 'word_rows(best)' in tpl)
    fake = CT.word_rows('(R999)(7) and I-999 and 987654 dispatches', act='b730')
    n += 1
    g += guard(L, 'word', 'a cite of nothing reads NOT FOUND, three rows', ' ; '.join('%s %s' % (r[1], r[2]) for r in fake), len(fake) == 3 and not any(r[2] for r in fake))
    return L, g, n


def control_questions():
    L, g, n = ['### (questions) THE HEAD LINE`S COUNT, (R341)(2)(vii); THE INSTANCE, b730`S ONE CALL OF TWO QUESTIONS'], 0, 0
    a = rd('b730_author_answers.txt')
    r = AL.calls_read(a)
    head = rd('b730_closing.txt').split(NL)[0]
    tpl = open(os.path.join(S, 'fold', 'closing.tpl'), encoding='utf-8').read()
    n += 1
    g += case(L, 'questions', 'b730`s head line: "%s"' % head[head.find('1 prompt'):][:17], 'the route printed calls: %d' % r['calls'], 'the route prints questions: %d' % r['questions'], '1 prompt' in head and r['calls'] == 1, r['questions'] == 2 and "['questions']" in tpl)
    return L, g, n


CONTROLS = dict(face=control_face, price=control_price, rerun=control_rerun, postlock=control_postlock, arms=control_arms, word=control_word, questions=control_questions)
ORDER = ('face', 'price', 'rerun', 'postlock', 'arms', 'word', 'questions')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.11.0, (R341)(2)(i)-(vii): THE COMPOSER AND (W), THE MEASURED ROW, A STAMPED RE-RUN, THE POST-LOCK SCAN, THE SEAT`S THREE ARMS, THE AUTHOR`S WORD, THE QUESTIONS COUNT (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.11.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v1110.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v1110.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
