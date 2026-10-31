# -*- coding: utf-8 -*-
"""standing/v180.py -- THE CONTROLS OF v1.8.0 ((R338)(2)), in v170.py's form: each instance replayed through the route as it stood before the repair
(read at BASE, the commit before this version) and through the repaired route; AS WANTED where the old route fails the instance and the new passes
it. Written at b728 by the Write tool.

  python -X utf8 tools/standing/v180.py control [vacuous|answers|face|readfirst|closing|remote|closeorder|gitwrite|connectivity|n5|legacy ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v180.txt with every control run, nothing else.
"""
import importlib.util
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
import close as C               # noqa: E402
import faceform as FF           # noqa: E402
import rule_arms as RA          # noqa: E402

BASE = 'a9dd62ce'               # ### relay's step-zero tip: every route of v1.7.0 as it stood
B727_CLOSE = '1bf8a57c'
B727_FACE = 'data/b727_registration_2026-10-31.txt'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf.jsonl'
B727_LO, B727_HI = '2026-10-31T04:20:00Z', '2026-10-31T15:39:00Z'
OLD_WRITE = re.compile(r'\bgit\s+(?:-C\s+\S+\s+)*(?:commit\b|push\b|merge(?![-\w])|rebase\b|reset\b|tag\s+(?!-l\b|--list\b|--points-at\b)\S|'
                       r'branch\s+-[dDmM]\b|branch\s+(?!-)[\w./-]+\s+[0-9a-f]{7,40}\b)|push_gated\.sh')
OLD_PART = re.compile(r'_checks\.py\b[^|;&]*?--part\s+(\S+)')
R727 = dict(act='b727', n=727)
SEVEN = ('4d976ef9', '9f83d1cf', '42f2dd65', 'f08c839f', '6ea30518', 'f224ae19', 'c76b228a')


def _git(*a):
    return subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.7.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.8.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    """a case with no failing side: what the repair must leave standing, printed as that and not as a before and after."""
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.8.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


def old_module(rel, name):
    """the module as it stood at BASE, loaded from a scratch file."""
    d = tempfile.mkdtemp(prefix='v180-')
    p = os.path.join(d, name + '.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(_git('show', '%s:%s' % (BASE, rel)))
    sp = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def b727_calls():
    import gitwrite as GW
    return GW.calls_of(SESSION, B727_LO, B727_HI)


# ================================================================================ (vacuous) (R338)(2)(ii)
def control_vacuous():
    L = ['### (vacuous) THE VACUOUS CLASS -- close.py plant_vacuous, neg_shown; checks.tpl\'s arm loop; instance: b727 event (1), G-RUNNER-GATE at relay 56249341']
    state = dict(rebuild_rows=[], other=1)
    planted = dict(state, rebuild_rows=[dict(r, free_mb=100) for r in state['rebuild_rows']])   # ### the carried plant, checks.tpl :1692
    posv = all(int(r.get('free_mb') or 0) >= 2560 for r in planted['rebuild_rows'])            # ### gate_ok's reading of the rows
    oldc = old_module('tools/standing/close.py', 'close_v170')
    e_old = dict(live=True, neg=True, pos=True, pos_raised=None, shown_failing=False)
    bank = dict(mode='prerun', exercise={'G-RUNNER-GATE': e_old})
    o = oldc.neg_shown([('G-RUNNER-GATE', 'p')], {'p': bank}, [])
    vac = C.plant_vacuous(state, planted, posv)
    e_new = dict(e_old, pos=posv and not vac, vacuous=vac)
    n = C.neg_shown([('G-RUNNER-GATE', 'p')], {'p': dict(mode='prerun', exercise={'G-RUNNER-GATE': e_new})}, [])
    g1 = case(L, 'vacuous', 'b727`s state: rebuild_rows empty, the plant over no rows', 'the mutated copy read PASS, the seal refused: %s' % (o.bad,),
              'the row reads VACUOUS %s ; shown %s ; bad %s ; vacuous %s' % (vac, n.shown, n.bad, n.vacuous), bool(o.bad) and posv, vac and not n.bad and not n.shown and n.vacuous == ['G-RUNNER-GATE'])
    real = dict(state, other=2)
    g2 = guard(L, 'vacuous', 'a plant that changed a key and still passed', 'plant_vacuous %s: stays a defect, the class does not excuse it' % C.plant_vacuous(state, real, True), not C.plant_vacuous(state, real, True))
    row = '  G-RUNNER-GATE                                  PASS  PASS  VAC   0.001    VACUOUS: THE PLANT MUTATED NOTHING'
    g3 = case(L, 'vacuous', 'the part`s row and the combine`s reader', 'ARM_ROW reads the VAC row: %s' % bool(oldc.ARM_ROW.search(row)), 'ARM_ROW reads it %s ; vacuous_of %s' % (bool(C.ARM_ROW.search(row)), C.vacuous_of([('p', None, row)])),
              not oldc.ARM_ROW.search(row), C.vacuous_of([('p', None, row)]) == ['G-RUNNER-GATE'])
    calls = b727_calls()
    old_n = sum(1 for c in calls if OLD_PART.search(c['cmd']))
    pc = [c for c in calls if RA.SUITE_PART.search(c['cmd'])]
    mine = [c for c in pc if '--mid' not in c['cmd'] and '--prev' not in c['cmd']]
    r0 = RA.reading('G-RULE-SUITE-PART-CALLS', dict(R727, calls=mine[-7:]))
    plant = mine[-7:] + [dict(mid='planted', ts='x', cmd=mine[-1]['cmd'] + ' && ' + mine[-1]['cmd'])]
    r1 = RA.reading('G-RULE-SUITE-PART-CALLS', dict(R727, calls=plant))
    parts = [OLD_NAME(c['cmd']) for c in mine[-7:]]
    L.append('  the calls` source: data/b727_commands.txt stops at the lock (05:23:39Z) and carries one part call, the probe at #168; b727`s post-push seven stand in the session`s transcript and are read there')
    g4 = case(L, 'vacuous', 'b727`s seven post-push part calls: %s' % parts, 'SUITE_PART reads %d of the %d part calls of the fold`s route: the arm`s VACUOUS' % (old_n, len(pc)),
              'read %d, failing %d ; a planted eighth, two parts in one call: %s, failing %d' % (r0[1], r0[2], 'PASS' if r1[0] else 'REFUSED', r1[2]), old_n == 0, r0[0] and r0[1] == 7 and not r1[0])
    return L, int(g1) + int(g2) + int(g3) + int(g4), 4


def OLD_NAME(cmd):
    m = RA.SUITE_PART.search(cmd)
    return m.group(1) if m else None


# ================================================================================ (answers) (R338)(2)(iii)
def control_answers():
    import v170
    L, g, n = v170.control_answers()
    return L + ['  v1.7.0 carried this repair at b727 (relay data/b727_standing_v170.txt); replayed here unedited, the (W) naming the pair on b728`s face'], g, n


# ================================================================================ (face) (R338)(2)(iv)(a)
def control_face():
    L = ['### (face) THE FIELD OF PRE-FACE COMMITS -- faceform.py; checks.tpl nothing_ahead_ok; instance: b727 event (4), seven PLACE-papers commits']
    face = _git('show', '%s:%s' % (B727_CLOSE, B727_FACE))
    undeclared = [h for h in SEVEN if h[:7] in face]
    field = face + NL + FF.PRE_FACE_TITLE + ' ' + ' '.join(SEVEN) + NL
    g1 = case(L, 'face', 'b727`s seven through the face as it stood and through the field', '%d of 7 on the face: the arm read them as ran ahead' % len(undeclared),
              '%d of 7 declared by the field' % sum(FF.declared(h, field) for h in SEVEN), not undeclared, all(FF.declared(h, field) for h in SEVEN))
    g2 = case(L, 'face', 'a planted eighth', 'the arm`s reading of a hash anywhere on the face: no field to read', 'deadbee declared %s: ran ahead' % FF.declared('deadbeefcafe', field),
              FF.pre_face_field(face) is None, not FF.declared('deadbeefcafe', field))
    prose = field.replace('### (1)', 'a hash in the later prose abcdef1' + NL + '### (1)', 1) + 'abcdef2' + NL
    g3 = case(L, 'face', 'a hash in the face`s prose beyond the section, the field standing', 'read declared: %s' % ('abcdef2' in prose), 'read declared: %s' % FF.declared('abcdef2aa', prose),
              'abcdef2' in prose, not FF.declared('abcdef2aa', prose))
    return L, int(g1) + int(g2) + int(g3), 3


# ================================================================================ (readfirst) (R338)(2)(iv)(b)
def control_readfirst():
    import readfirst as RF
    L = ['### (readfirst) THE BANK WRITTEN BY THE TOOL -- readfirst.py compose, regenerate; instance: data/b727_readfirst.txt (event (5))']
    t = _git('show', '%s:data/b727_readfirst.txt' % B727_CLOSE)
    new = RF.regenerate(t)
    g1 = case(L, 'readfirst', 'b727`s bank regenerated', 'the title %r in the hand bank: %s' % (RF.OWN_TITLE, RF.OWN_TITLE in t), 'in the regenerated bank: %s, ferry title %s' % (RF.OWN_TITLE in new, RF.FERRY_TITLE in new),
              RF.OWN_TITLE not in t, RF.OWN_TITLE in new and RF.FERRY_TITLE in new)
    ours = open(os.path.join(D, 'b728_readfirst.txt'), encoding='utf-8').read()
    g2 = guard(L, 'readfirst', 'this act`s bank, by the tool', 'both titles present: %s' % (RF.OWN_TITLE in ours and RF.FERRY_TITLE in ours), RF.OWN_TITLE in ours and RF.FERRY_TITLE in ours)
    return L, int(g1) + int(g2), 2


# ================================================================================ (closing) (R338)(2)(iv)(c)
def control_closing():
    L = ['### (closing) THE CLOSING COMPOSED FROM THE FACE`S CLAUSE -- faceform.py outbound_clause; checks.tpl closing_sentence_ok; instance: tools/acts/b727.py at %s (event (6))' % B727_CLOSE]
    src = _git('show', '%s:tools/acts/b727.py' % B727_CLOSE)
    ph = 'plain requests to github.com'
    new = FF.outbound_clause('six anonymous reads')
    g1 = case(L, 'closing', 'the phrase b727 dropped', 'in b727`s closing section: %s' % (ph in src), 'on regeneration from the clause: %s' % (ph in new), ph not in src, ph in new)
    return L, int(g1), 1


# ================================================================================ (remote) (R338)(2)(iv)(d)
def control_remote():
    import hook as H
    L = ['### (remote) ONE REMOTE READ PER COMMAND -- hook.py judge; instance: b727 event (7), the chained diagnostic of 05:5xZ']
    Hold = old_module('tools/standing/hook.py', 'hook_v170')
    ch = [c for c in b727_calls() if c['cmd'].count('ls-remote') > 1]
    shell = 'Bash'
    o = [Hold.judge(shell, dict(command=c['cmd'])) for c in ch]
    n = [H.judge(shell, dict(command=c['cmd'])) for c in ch]
    L.append('  the chained call(s) of b727: %d, the first %s, %d reads' % (len(ch), ch[0]['ts'] if ch else '-', ch[0]['cmd'].count('ls-remote') if ch else 0))
    g1 = case(L, 'remote', 'b727`s chained diagnostic replayed', 'the hook read %s' % o, 'the hook read %s' % [x[0] if x else None for x in n], bool(ch) and all(x is None or x[0] != 'REMOTE' for x in o), bool(ch) and all(x and x[0] in ('REMOTE', 'PIPE', 'REDIR') for x in n) and any(x and x[0] == 'REMOTE' for x in n))
    one = H.judge('Bash', dict(command='git -C /d/relay ls-remote origin'))
    quoted = H.judge('Bash', dict(command='git -C /d/relay commit -m "two ls-remote ls-remote words"'))
    g2 = guard(L, 'remote', 'one read alone, and the words in a quoted message', 'one read %s ; quoted %s' % (one, quoted), one is None and quoted is None)
    return L, int(g1) + int(g2), 2


# ================================================================================ (closeorder) (R338)(2)(iv)(e)
def control_closeorder():
    import act_close as AC
    L = ['### (closeorder) close.py dry AFTER THE COMBINE -- act_close.py close_steps_printed; close.py seal_write; instance: b727 event (2)']
    oldp = _git('show', '%s:tools/act_close.py' % BASE)
    steps = AC.close_steps_printed()
    src = open(os.path.join(S, 'close.py'), encoding='utf-8').read()
    keys = [s[0] for s in steps]
    g1 = case(L, 'closeorder', 'the printed order', 'a step [7a] in tools/act_close.py: %s' % ('7a' in oldp), 'printed after [7]: %s ; the row`s numbers unmoved: %s' % (keys[keys.index(7) + 1] == '7a', [k for k in keys if not isinstance(k, str)] == list(range(1, 26))),
              '7a' not in oldp, keys[keys.index(7) + 1] == '7a' and [k for k in keys if not isinstance(k, str)] == list(range(1, 26)))
    g2 = case(L, 'closeorder', 'the seal without the dry', 'b727`s seal found its own refusal: no read of the bank', 'seal_write refuses where data/<act>_close_dry.txt is absent: %s' % ('STEP [7a]' in src), 'close_dry' not in _git('show', '%s:tools/standing/close.py' % BASE), 'STEP [7a]' in src)
    return L, int(g1) + int(g2), 2


# ================================================================================ (gitwrite) (R338)(2)(v)
def control_gitwrite():
    import gitwrite as GW
    L = ['### (gitwrite) G-RULE-ONE-GIT-WRITE -- rule_arms.py GIT_WRITE and the arm; the trace data/b728_gitwrite_trace.txt, run before the repair; instance: b727`s two adds, 11:33:49Z']
    calls = b727_calls()
    ch = [c for c in calls if re.search(r'git\s+add\b.*&&\s*git\s+add\b', c['cmd'])]
    oldn = sum(1 for c in ch if OLD_WRITE.search(RA.QUOTED.sub('""', c['cmd'])))
    new = RA.reading('G-RULE-ONE-GIT-WRITE', dict(R727, calls=ch))
    g1 = case(L, 'gitwrite', 'the arm over b727`s chained call', 'the old expression matches %d of %d: the pass read 39, none flagged' % (oldn, len(ch)), 'reads %s, messages over %d: %s' % ('PASS' if new[0] else 'FAILS, AS IT SHOULD', new[2], new[3]),
              oldn == 0, bool(ch) and not new[0])
    br = 'git -C /d/relay branch push-b728-x main'
    g2 = case(L, 'gitwrite', 'the push branch', 'the old expression reads it a write: %s' % bool(OLD_WRITE.search(br)), 'the new: %s ; a listing `git branch` still no write: %s' % (bool(GW.writes(br)), not GW.writes('git branch --list')),
              not OLD_WRITE.search(br), bool(GW.writes(br)) and not GW.writes('git branch --list'))
    whole = RA.reading('G-RULE-ONE-GIT-WRITE', dict(R727, calls=calls))
    L += ['  b727`s whole session through the repaired arm: %s, messages %d, over %d: %s' % ('PASS' if whole[0] else 'FAIL', whole[1], whole[2], whole[3]),
          '  THE PASS OF b727 AND BEFORE STANDS MARKED WEAK; from this version the arm has fired on the two adds']
    return L, int(g1) + int(g2), 2


# ================================================================================ (connectivity) (R338)(2)(vi)
def control_connectivity():
    import act_root as AR
    L = ['### (connectivity) THE CONNECTIVITY READING -- act_root.py verify; instance: b727 events (9)-(10), every remote read empty, the chain read DISAGREE']
    acts = ('b727',)
    empty = lambda p: {}   # noqa: E731
    o = AR._verify(empty, None, acts)
    n = AR.verify(empty, None, acts)
    g1 = case(L, 'connectivity', 'every remote empty, twice', 'the rows read %s' % [v for _a, v, _w in o], 'the rows read %s, no DISAGREE' % [v for _a, v, _w in n],
              any(v == 'DISAGREE' for _a, v, _w in o), not any(v == 'DISAGREE' for _a, v, _w in n))

    class Flip(dict):
        """the fixture's cache: verify's clear before its re-run is the moment the fixture's remote comes back, so the whole first run reads empty."""
        back = False

        def clear(self):
            Flip.back = True

    sys.modules['v180_fake'] = type(sys)('v180_fake')
    sys.modules['v180_fake']._REMOTE = Flip()

    def flaky(p):
        return AR.ls_remote(p) if Flip.back else {}
    flaky.__module__ = 'v180_fake'
    AR._REMOTE.clear()
    t = AR.verify(flaky, None, acts)
    g2 = case(L, 'connectivity', 'empty once, read on the re-run (the instance b727 met)', 'read DISAGREE at the first run, as above', 'the rows read %s after one re-run' % [v for _a, v, _w in t],
              any(v == 'DISAGREE' for _a, v, _w in o), all(v == 'AGREE' for _a, v, _w in t))
    return L, int(g1) + int(g2), 2


# ================================================================================ (n5) (R338)(2)(vii)
def control_n5():
    L = ['### (n5) THE N5 CLAUSE AND THE REPORT`S WORD -- faceform.py n5_kernel_clause; report.tpl scores; instances: b727 (g), the author`s ruling (5)']
    agents = [('SIDE-cosmo', '[20] and [22]')]
    g1 = case(L, 'n5', 'SIDE-cosmo`s AGENTS.md, 4e9387ba and 5ad736fe', 'N5`s words named README.md alone: AGENTS.md beyond them', '%s ; allowed %s ; on another kernel %s' % (
        FF.n5_kernel_clause(agents), FF.kernel_file_allowed('SIDE-cosmo', 'AGENTS.md', agents), FF.kernel_file_allowed('SIDE-spinor', 'AGENTS.md', agents)),
        not FF.kernel_file_allowed('SIDE-cosmo', 'AGENTS.md'), FF.kernel_file_allowed('SIDE-cosmo', 'AGENTS.md', agents) and not FF.kernel_file_allowed('SIDE-spinor', 'AGENTS.md', agents))
    old = _git('show', '%s:tools/standing/fold/report.tpl' % BASE)
    new = open(os.path.join(S, 'fold', 'report.tpl'), encoding='utf-8').read()
    g2 = case(L, 'n5', 'the report`s word for a refuted score', "REFUTED='BROKEN' at v1.7.0: %s" % ("REFUTED='BROKEN'" in old), "REFUTED='REFUTED': %s" % ("REFUTED='REFUTED'" in new), "REFUTED='BROKEN'" in old, "REFUTED='REFUTED'" in new and "'BROKEN'" not in new)
    return L, int(g1) + int(g2), 2


# ================================================================================ (legacy) (R338)(2)(ix)
def control_legacy():
    L = ['### (legacy) THE LEGACY COPY -- the ruling reads "as (R335)(2)(iii) ordered and b725 did not land": THE STATE READ, A CITATION MISS. v1.5.0 landed the copy at relay 7be1601c']
    before = '7be1601c^'
    src = _git('show', 'HEAD:tools/b644_record.py').split(NL)
    cp = open(os.path.join(S, 'routes', 'b644_record.py'), encoding='utf-8').read().split(NL)
    hdr = len(cp) - len(src)
    dif = [i + 1 for i in range(len(src)) if src[i] != cp[i + hdr]]
    import legacy as LG
    prior = _git('show', '%s:tools/standing/legacy.py' % before)
    g1 = case(L, 'legacy', 'the copy against its source, beneath its %d-line header' % hdr, 'no copy before 7be1601c: %s ; legacy.py named b644_record: %s' % (
        _git('ls-tree', before, 'tools/standing/routes/b644_record.py') == '', "'b644_record'" in prior),
        'lines differing %s ; legacy.py names it %s' % (dif, 'b644_record' in LG.NAMES), _git('ls-tree', before, 'tools/standing/routes/b644_record.py') == '' and "'b644_record'" in prior,
        dif == [1088] and 'b644_record' not in LG.NAMES)
    L.append('  THE EXCEPTION FILE: %d names remain, so "emptied if nothing else remains" reads NOT EMPTIED; the flatten of those names was not ordered and is not run (priced at data/b725_standing_v150.txt)' % len(LG.NAMES))
    return L, int(g1), 1


CONTROLS = dict(vacuous=control_vacuous, answers=control_answers, face=control_face, readfirst=control_readfirst, closing=control_closing, remote=control_remote,
                closeorder=control_closeorder, gitwrite=control_gitwrite, connectivity=control_connectivity, n5=control_n5, legacy=control_legacy)
ORDER = ('vacuous', 'answers', 'face', 'readfirst', 'closing', 'remote', 'closeorder', 'gitwrite', 'connectivity', 'n5', 'legacy')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.8.0, (R338)(2)(ii)-(ix): THE VACUOUS CLASS, THE ANSWERS PAIR, THE SITTING`S FOUR AND closeorder, ONE GIT WRITE, THE CONNECTIVITY READING, N5 AND THE REPORT`S WORD, THE LEGACY COPY (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '', '### the instances read at their commits; each case through both routes; the route before the repair read at relay %s' % BASE, '']
    tg = tn = 0
    for k in names:
        try:
            L, g, n = CONTROLS[k]()
        except Exception as e:  # noqa: BLE001
            L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + n
    out.append('### ### **v1.8.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v180.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v180.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
