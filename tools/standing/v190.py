# -*- coding: utf-8 -*-
"""standing/v190.py -- THE CONTROLS OF v1.9.0 ((R339)(2)), in v180.py's form: each instance replayed through the route as it stood before the repair (read at BASE, the
commit before this version) and through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Written at b729 by the Write tool.

  python -X utf8 tools/standing/v190.py control [redir|reportdry|required|plants|scanback|n5count|nouns|promptonce ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v190.txt with every control run, nothing else.
"""
import importlib.util
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

BASE = 'b2a7f040'               # ### relay's step-zero tip: every route of v1.8.0 as it stood
B728_CLOSE = '0650a188'


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.8.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.9.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case with no failing side: what the repair must leave standing, printed as that and not as a before and after."""
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.9.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def old_module(rel, name):
    """the module as it stood at BASE, loaded from a scratch file."""
    d = tempfile.mkdtemp(prefix='v190-')
    p = os.path.join(d, name + '.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(_git('show', '%s:%s' % (BASE, rel)))
    sp = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ================================================================================ (redir) (R339)(2)(i)
BANKED = (('b725', 6), ('b727', 1), ('b728', 5), ('b728', 8), ('b728', 9))


def control_redir():
    import hook as H
    old = old_module('tools/standing/hook.py', 'hook_old')
    L = ['### (redir) THE REDIR CLASS -- hook.py judge; the banks hold five REDIR rows, b725 :6, b727 :1, b728 :5, :8, :9, each refused when it ran; `> $null` stands in none of them (a citation MISS, data/b729_stepzero.txt)']
    g = t = 0
    for act, n in BANKED:
        row = [l for l in A.rd('%s_hook_refusals.txt' % act).split(NL) if l.strip()][n - 1]
        shown = json.loads(row.split(' | ')[3].encode('utf-8', 'replace').decode('utf-8')) if row.split(' | ')[3].rstrip().endswith('"') else None
        cmd = shown if shown is not None else row.split(' | ')[3].strip().strip('"').replace('\\n', '\n').replace('\\"', '"')
        v = H.judge('Bash', dict(command=cmd))
        g += int(guard(L, 'redir', 'the banked refusal %s :%d replayed' % (act, n), 'read %s' % (v[0] if v else 'ALLOWED'), bool(v) and v[0] == 'REDIR'))
        t += 1
    for cmd in ("bash -c 'git status > out.txt'", 'sh -c "ls | wc -l"', 'powershell -Command "git log 2>&1"', 'git status; Set-Content -Path a -Value b', 'cmd /c "dir > x.txt"'):
        tool = 'PowerShell' if 'Set-Content' in cmd or 'powershell' in cmd else 'Bash'
        o, n_ = old.judge(tool, dict(command=cmd)), H.judge(tool, dict(command=cmd))
        g += int(case(L, 'redir', 'the form that passed: %s' % cmd, 'read %s' % (o[0] if o else 'ALLOWED'), 'read %s' % (n_[0] if n_ else 'ALLOWED'), o is None, bool(n_) and n_[0] == 'REDIR'))
        t += 1
    for cmd in ('git status > $null', 'python x.py 2>&1'):
        n_ = H.judge('PowerShell', dict(command=cmd))
        g += int(guard(L, 'redir', 'the ruling`s form %s, refused before and after' % cmd, 'read %s' % (n_[0] if n_ else 'ALLOWED'), bool(n_) and n_[0] == 'REDIR'))
        t += 1
    for cmd in ("git -C /d/relay log --oneline -3", "bash -c 'git status'", 'git -C /d/relay commit -m "the Out-File rule, a > b"'):
        g += int(guard(L, 'redir', 'a planted clean command: %s' % cmd, 'read %s' % (H.judge('Bash', dict(command=cmd)) or 'ALLOWED'), H.judge('Bash', dict(command=cmd)) is None))
        t += 1
    return L, g, t


# ================================================================================ (reportdry) (R339)(2)(ii)
def control_reportdry():
    import reportdry as RD
    import act_close as AC
    L = ['### (reportdry) report dry BEFORE THE LOCK -- reportdry.py; reg_gate.tpl; close.py; act_close.py close_steps_printed; instance: b728 event (6), tools/acts/b728.py\'s report section and sk']
    r8 = RD.read('b728')
    cur = A.current().get('act')
    r9 = RD.read(cur)
    g1 = case(L, 'reportdry', 'b728`s section, as sealed', 'no dry before the lock: the crash came at `report bank`, after the root`s prompt', 'the rendered tool read: undefined %s' % r8['undefined'], 'report_dry' not in _git('show', '%s:tools/standing/close.py' % BASE), r8['undefined'] == ['sk'])
    g2 = guard(L, 'reportdry', 'this act`s section', 'undefined %s' % (r9['undefined'] or 'NONE'), not r9['undefined'])
    keys = [s[0] for s in AC.close_steps_printed()]
    g3 = guard(L, 'reportdry', 'the printed order: [5a] after [5] and before [6]', '%s' % keys[:9], keys[keys.index(5) + 1] == '5a' and keys.index('5a') < keys.index(6))
    src = open(os.path.join(S, 'fold', 'reg_gate.tpl'), encoding='utf-8').read()
    g4 = guard(L, 'reportdry', 'the gate reads the dry, the seal refuses without it', 'in reg_gate.tpl %s ; in close.py %s' % ('reportdry' in src, 'STEP [5a]' in open(os.path.join(S, 'close.py'), encoding='utf-8').read()),
               'reportdry' in src and 'STEP [5a]' in open(os.path.join(S, 'close.py'), encoding='utf-8').read())
    return L, int(g1) + int(g2) + int(g3) + int(g4), 4


# ================================================================================ (required) (R339)(2)(iii)
def required_of(act):
    src = open(os.path.join(T, 'acts', '%s.py' % act), encoding='utf-8').read()
    m = re.search(r'(?s)^REQUIRED_BANKS = \((.*?)^#⟪END⟫', src, re.M)
    return re.findall(r"'(data/[^']+)'", m.group(1)) if m else []


def control_required():
    import rootbanks as RB
    L = ['### (required) THE REQUIRED LIST AGAINST WHAT THE ROUTE CAN LIST -- rootbanks.py guard_listable; instance: b728 event (9), data/b726_mechanisms.txt']
    r8, cur = required_of('b728'), A.current().get('act')
    bad = RB.unlistable(r8, 'b728', ('data/b675_corrigenda.txt',))
    g1 = case(L, 'required', 'b728`s list', 'guard read the exclusion alone, %d banks, G-ACTROOT-BANKED failing post-push' % len(r8), 'refused at import, naming %s' % bad,
              'unlistable' not in _git('show', '%s:tools/standing/rootbanks.py' % BASE), bad == ['data/b726_mechanisms.txt'])
    r9 = required_of(cur)
    g2 = guard(L, 'required', 'this act`s list', '%d banks, unlistable %s' % (len(r9), RB.unlistable(r9, cur, ('data/b675_corrigenda.txt',)) or 'NONE'), bool(r9) and not RB.unlistable(r9, cur, ('data/b675_corrigenda.txt',)))
    return L, int(g1) + int(g2), 2


# ================================================================================ (plants) (R339)(2)(iv)
def plants_of(rev=None):
    t = _git('show', '%s:tools/standing/fold/checks.tpl' % rev) if rev else open(os.path.join(S, 'fold', 'checks.tpl'), encoding='utf-8').read()
    a = re.search(r"\('G-SEAL-HASHES'.*?\n\s+lambda S: (put\(.*\))\),\n", t)
    b = re.search(r"\('G-TRAIL-CARRIES-SEAL'.*?\n\s+lambda S: (put\(.*\))\),\n", t)
    return a.group(1).replace('⟪ACT⟫', 'b728'), b.group(1).replace('⟪ACT⟫', 'b728')


class KK:
    pass


def control_plants():
    L = ['### (plants) G-SEAL-HASHES`S PLANT AND G-TRAIL-CARRIES-SEAL`S -- checks.tpl; instance: b728 event (12), each plant replayed over b728`s seal bank and trail line at its close, under b728`s STC.plant_vacuous reading']
    seal = json.loads(_git('show', '%s:data/b728_seal_hashes.json' % B728_CLOSE))
    sealed = sorted(seal['tools'])
    KK.SEALED = tuple(sealed)
    S0 = dict(sealnow=dict(seal['tools']), ot=' '.join('%s agree' % t for t in sealed))

    def put(s, k, v):
        n = dict(s)
        n[k] = v
        return n
    env = dict(put=put, K=KK)
    live1 = lambda s: all(s['sealnow'].get(t) == seal['tools'][t] for t in sealed)   # noqa: E731
    live2 = lambda s: all(('%s agree' % t) in s['ot'] for t in sealed)   # noqa: E731
    o1, o2 = plants_of(BASE)
    n1, n2 = plants_of()
    r = {}
    for name, ex, live in (('o1', o1, live1), ('o2', o2, live2), ('n1', n1, live1), ('n2', n2, live2)):
        m = eval('lambda S: ' + ex, env)(dict(S0))   # noqa: S307
        r[name] = (live(m), m == S0)
    g0 = guard(L, 'plants', 'the arms live on the b728 state', 'seal %s ; trail %s' % (live1(S0), live2(S0)), live1(S0) and live2(S0))
    g1 = case(L, 'plants', 'G-SEAL-HASHES`S POS', 'the plant keyed a tool no list carries: the arm still passes on it, %s (POSITIVE-CONTROL PASSES 1)' % r['o1'][0], 'the plant keyed the list`s first tool: the arm reads %s' % r['n1'][0], r['o1'][0], not r['n1'][0])
    g2 = case(L, 'plants', 'G-TRAIL-CARRIES-SEAL`S POS', 'the plant mutated nothing: %s (VACUOUS 1)' % r['o2'][1], 'the plant mutated the trail: %s, the arm reads %s' % (not r['n2'][1], r['n2'][0]), r['o2'][1], not r['n2'][1] and not r['n2'][0])
    return L, int(g0) + int(g1) + int(g2), 3


# ================================================================================ (scanback) (R339)(2)(v)
def control_scanback():
    L = ['### (scanback) THE SCAN WRITTEN BACK AFTER THE LOCK -- act.py scan_bank_name, scan_append, post_lock_appended; instance: b728`s bank last written at 65a92110, before its lock 689402fe; the suite`s live runs after the lock wrote nothing, so the post-lock run`s own figures stand in no bank and the reproduction carries the closing`s foot in the bank form']
    closing = _git('show', '%s:data/b728_closing.txt' % B728_CLOSE).split(NL)
    row = closing[89]
    m = re.search(r'(PREVIOUS ADDRESS: \d+ ; THE AUTHOR`S NAME: \d+ ; PREVIOUS NAME: \d+ ; PLACES \d+ ; CONTROLS 4 OF 4 AS WANTED ; \d+ s)', row)
    foot = '### ### **%s.**' % m.group(1) if m else ''
    locked = _git('show', '%s:data/b728_address_scan.txt' % B728_CLOSE)
    lf = re.search(r'PLACES (\d+)', locked)
    last = _git('log', '-1', '--format=%h', B728_CLOSE, '--', 'data/b728_address_scan.txt').strip()
    post = _git('ls-tree', B728_CLOSE, 'data/b728_address_scan_postlock.txt').strip()
    bank = A.scan_append('', '2026-10-31T19:00:00Z', foot)
    again = A.scan_append(bank, '2026-10-31T20:00:00Z', foot)
    g1 = case(L, 'scanback', 'b728`s post-lock run', 'the bank`s last commit %s stands before the lock, PLACES %s; a post-lock bank at the close: %s' % (last, lf.group(1) if lf else '?', bool(post)), 'in the bank form at %s: its foot read back %s' % (A.scan_bank_name('b728', True), foot in bank),
              last == '65a92110' and not post, foot in bank and A.scan_bank_name('b728', True) == 'b728_address_scan_postlock.txt')
    g2 = guard(L, 'scanback', 'a second run beneath the first, none rewritten; the name before the lock unchanged; the post-lock bank outside the locked set', '%d runs ; %s ; %s' % (
        again.count('## THE RUN AFTER THE LOCK'), A.scan_bank_name('b728', False), 'data/b728_address_scan_postlock.txt' in A.post_lock_appended('b728')),
        again.startswith(bank) and again.count('## THE RUN AFTER THE LOCK') == 2 and A.scan_bank_name('b728', False) == 'b728_address_scan.txt' and 'data/b728_address_scan_postlock.txt' in A.post_lock_appended('b728'))
    return L, int(g1) + int(g2), 2


# ================================================================================ (n5count) (R339)(2)(vi)
def control_n5count():
    import faceform as FF
    L = ['### (n5count) N5`S COUNT FROM THE (W) LIST -- faceform.py readme_writes; instance: b728`s (14), three README writes where N5 carried the number one']
    face = _git('show', '%s:data/b728_registration_2026-10-31.txt' % B728_CLOSE)
    w = face[face.find('(W) THE WRITE LIST'):face.find('(Z) THE NOTHINGS')]
    r = FF.readme_writes(w)
    g1 = case(L, 'n5count', 'b728`s (W) list', 'N5 said one and the writes were three: a carried number, the word "three writes where N5 says one" printed by hand', FF.n5_count_sentence(w),
              'readme_writes' not in _git('show', '%s:tools/standing/faceform.py' % BASE), r == ['SIDE-archimedean', 'SIDE-rcurve', 'SIDE-spinor'])
    g2 = guard(L, 'n5count', 'a (W) list with no README', FF.n5_count_sentence('tools/x.py ; data/b729_*.txt'), FF.readme_writes('tools/x.py ; data/b729_*.txt') == [])
    return L, int(g1) + int(g2), 2


# ================================================================================ (nouns) (R339)(2)(vii)
ROWS_B728 = (('the entry`s object noun', 'face', r'the C2 (theorem|certificates?) at 18 of 18', 'b728_c2.txt', r'WHAT COMPILED IS THE (CERTIFICATE|THEOREM)'),
             ('the onsets counted', 'ruling', r'the (seven) banked onsets', 'b728_onset_table.txt', r'THE TABLE AT (SIX) ZEROS'))


def control_nouns():
    import nouns as SN
    L = ['### (nouns) COUNTS AND NOUNS FROM THE BANKS -- nouns.py; citation.tpl check; instances: b728`s title "the C2 theorem at 18 of 18 fields" against data/b728_c2.txt, (R338)(3)`s seven against the table`s six']
    texts = dict(face='the C2 theorem at 18 of 18 fields', ruling='the seven banked onsets')

    def rd(n):
        return texts.get(n) if n in texts else _git('show', '%s:data/%s' % (B728_CLOSE, n))
    hl = SN.halts(ROWS_B728, rd)
    g1 = case(L, 'nouns', 'b728`s two typed words through the rows', 'the citation check carried a row by hand for each; the title was typed by the ruling and stood', 'halts %s' % hl,
              'halts' not in _git('show', '%s:tools/standing/fold/citation.tpl' % BASE), [h[1:] for h in hl] == [('theorem', 'certificate'), ('7', '6')])
    texts.update(face='the C2 certificates at 18 of 18 fields', ruling='the six banked onsets')
    ok = SN.halts(ROWS_B728, rd)
    g2 = guard(L, 'nouns', 'the corrected words', 'halts %s' % (ok or 'NONE'), not ok)
    g3 = guard(L, 'nouns', 'the check exits 3 on a halt', 'in citation.tpl: %s' % ('sys.exit(3)' in open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read()), 'sys.exit(3)' in open(os.path.join(S, 'fold', 'citation.tpl'), encoding='utf-8').read())
    return L, int(g1) + int(g2) + int(g3), 3


# ================================================================================ (promptonce) (R339)(2)(viii)
def control_promptonce():
    import allow as AL
    L = ['### (promptonce) THE PROMPT-ONCE CLAUSE -- allow.py calls_read; closing.tpl head_line; instance: b728`s bank, the root`s prompt and two halts, the head line reading 4']
    t = _git('show', '%s:data/b728_author_answers.txt' % B728_CLOSE)
    c = AL.calls_read(t)
    head = _git('show', '%s:data/b728_closing.txt' % B728_CLOSE).split(NL)[0]
    g1 = case(L, 'promptonce', 'b728`s three', 'the head line counted the PROMPT rows, questions: %s' % re.search(r'\d+ prompts answered', head).group(0), 'calls %d ; the root`s 1 ; halts %d' % (c['calls'], c['halts']),
              '4 prompts answered' in head, c == dict(calls=3, root=1, halts=2))
    src = open(os.path.join(S, 'fold', 'closing.tpl'), encoding='utf-8').read()
    g2 = guard(L, 'promptonce', 'the head line reads the calls', 'calls_read in closing.tpl: %s' % ('calls_read' in src), 'calls_read' in src)
    return L, int(g1) + int(g2), 2


CONTROLS = dict(redir=control_redir, reportdry=control_reportdry, required=control_required, plants=control_plants, scanback=control_scanback, n5count=control_n5count,
                nouns=control_nouns, promptonce=control_promptonce)
ORDER = ('redir', 'reportdry', 'required', 'plants', 'scanback', 'n5count', 'nouns', 'promptonce')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.9.0, (R339)(2)(i)-(viii): THE REDIR CLASS, report dry BEFORE THE LOCK, THE REQUIRED LIST, THE TWO PLANTS, THE SCAN AFTER THE LOCK, N5`S COUNT, COUNTS AND NOUNS FROM THE BANKS, THE PROMPT COUNT (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.9.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v190.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v190.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
