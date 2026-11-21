# -*- coding: utf-8 -*-
"""b765, (R375)(8): THE PLANTED CONTROLS OF THE TWO REPAIRS, ONE A KEY, in the form of tools/b764_repair_controls.py. Each control reads the
fault at the commit before the repair and reads clean at the repair's commit, both printed. Read-only over the relay: each revision's files
are taken by `git show <rev>:<path>` into a scratch folder of the system's temporary directory (removed after), and each revision is probed
in its own interpreter (`python -I`), so no module of one revision is read by the other; the probe calls the revision's functions, writes
nothing, and prints one JSON line. --bank appends the reading to data/b765_repair_controls.txt beneath a head naming the key and both
commits; nothing else is written. The repair's commit must have the commit before it as its first parent, read and printed.

  python -X utf8 -u tools/b765_repair_controls.py <key> <before> <after> [--bank]
"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = '\n'
ACT = 'b765'
BANK = os.path.join(D, 'b765_repair_controls.txt')
PP = 'D:/MY-DOwnloads/PLACE-papers'


def git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True)
    return r.returncode, r.stdout


def snapshot(rev, paths, dest):
    """the files `paths` at `rev` under dest, at their relay paths; [(path, present)]."""
    out = []
    for p in paths:
        rc, b = git('show', '%s:%s' % (rev, p))
        out.append((p, rc == 0))
        if rc == 0:
            q = os.path.join(dest, *p.split('/'))
            os.makedirs(os.path.dirname(q), exist_ok=True)
            with open(q, 'wb') as fh:
                fh.write(b)
    return out


def probe(code, snap, *args):
    r = subprocess.run([sys.executable, '-X', 'utf8', '-I', '-c', code, snap] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    lines = [l for l in r.stdout.split(NL) if l.startswith('{')]
    if r.returncode != 0 or not lines:
        return dict(error='exit %d: %s' % (r.returncode, (r.stderr or r.stdout).strip()[-400:]))
    return json.loads(lines[-1])


# ================================================================================ [K20] THE ROOT'S ANSWER IN THE AUTHOR'S WORDS
K20_PATHS = ('tools/standing/nextact.py',)
K20_PP_REV = '1198a637'   # ### b764's record at PLACE-papers: its entry and its trail as its sealed composition landed them
K20_LINES = (('carried.txt', 'FINDINGS.md', 15921, '**Carried to:**'), ('next.txt', 'FINDINGS.md', 15923, '**Next'),
             ('trail_next.txt', 'OPEN_TRAILS.md', 19131, '**Next'))
# ### the planted answers banks, one a form: (A) a root prompt answered in the author's words between BEGIN and END, the next act named as
# ### "The act after <act>" and nowhere as "<next> is" (b764's form, its RESULT line with the line breaks taken out); (B) an author's word that
# ### names the next act as "the act after <act>" with no "<next> is" and no prompt; (C) a prompt answered by an option, read as before at both.
K20_PLANTS = {
    'b900': ('### b900 -- THE AUTHOR`S ANSWERS, 1 prompt(s) put by the seat in this act (planted)\n\n'
             '### CALL tool-use id planted (planted)\n'
             '### PROMPT 1 (b901): the planted act is sealed. Which is b901?\n'
             '  OPTION 1 [RECOMMENDED]: The planted route (Recommended) :: The act after b900 takes the planted route.\n'
             'RESULT (planted): The user answered: "the planted act is sealed. Which is b901?"="BEGINTHE AUTHOR\'S ANSWER AT THE ROOT OF b900, '
             '2026-11-21: route 2, in my words. The act after b900 reads the planted premises, a reading and no build.(1) THE FIRST STEP, planted.'
             'END". Read the answers carefully.\n'),
    'b910': ('### b910 -- THE AUTHOR`S ANSWERS, 0 prompt(s) put by the seat in this act; and 1 word(s) of the author delivered between BEGIN and '
             'END (planted)\n\n'
             '### THE AUTHOR`S WORD (transcript line 1), BEGIN to END, verbatim:\n'
             'THE AUTHOR\'S WORD ON THE NEXT ACT, 2026-11-21 (planted).\n'
             'The act after b910 computes the planted window and banks it as data.\n'),
    'b920': ('### b920 -- THE AUTHOR`S ANSWERS, 1 prompt(s) put by the seat in this act (planted)\n\n'
             '### PROMPT 1 (b921): Which is b921?\n'
             '  OPTION 1 [RECOMMENDED]: The planted option (Recommended) :: The act after b920 takes the option.\n'
             'RESULT (planted): The user answered: "Which is b921?"="The planted option (Recommended)". Read the answers carefully.\n'),
}
K20_WANT = {'b900': ('the act after b900 reads the planted premises', 'route 2, in my words'),
            'b910': ('the act after b910 computes the planted window',),
            'b920': ('the author chose: the planted option (recommended)',)}
K20_PROBE = r'''
import json, os, sys
snap, inst, relay_data = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import nextact as N
rd = lambda p: open(p, encoding='utf-8').read()
plants = dict((a, N.word(a, inst)) for a in ('b900', 'b910', 'b920'))
w = N.word('b764', relay_data)
want = ('relay data/b764_author_answers.txt :%d, %s' % w) if w else None
car, nxt, trl = (rd(os.path.join(inst, n)).strip('\n') for n in ('carried.txt', 'next.txt', 'trail_next.txt'))
ent = N.entry('b764', car + '\n\n' + nxt, relay_data)
e_car, e_next = ent.split('\n')[0], ent.split('\n')[2]
t_next = N.trail('b764', trl, relay_data)
print(json.dumps(dict(plants=plants, answer=w, carried=bool(want) and want in e_car, next=bool(want) and want in e_next,
                      trail=bool(want) and want in t_next,
                      idem=N.entry('b764', ent, relay_data) == ent and N.trail('b764', t_next, relay_data) == t_next)))
'''


def control_k20(before, after):
    """[K20]: three planted answers banks, one a form ((A) a root prompt answered between BEGIN and END naming "The act after <act>", (B) an
    author's word naming "the act after <act>" with no "<next> is", (C) a prompt answered by an option), each read by word() at each revision;
    and b764's own landed lines (PLACE-papers 1198a637: the entry's Carried to line FINDINGS :15921 and Next line :15923, the trail's Next line
    OPEN_TRAILS :19131, each read by line and sha256, no text printed) read through each revision's entry() and trail() with b764's answers
    bank (data/b764_author_answers.txt, the root's answer at :8). FAULT: (A) or (B) read as no answer, or b764's answer and bank absent from a
    line. CLEAN: (A) and (B) read with their words, (C) as before, b764's answer and bank in each of the three lines, read twice and read once."""
    L, res = [], {}
    inst = tempfile.mkdtemp(prefix='b765k20i_')
    try:
        for a_, text in sorted(K20_PLANTS.items()):
            with open(os.path.join(inst, '%s_author_answers.txt' % a_), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(text)
        shas = []
        for fn, path, ln, opens in K20_LINES:
            r = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (K20_PP_REV, path)], capture_output=True)
            l_ = r.stdout.decode('utf-8').replace('\r', '').split(NL)[ln - 1] if r.returncode == 0 else ''
            shas.append((path, ln, hashlib.sha256(l_.encode('utf-8')).hexdigest()[:16], l_.startswith(opens)))
            with open(os.path.join(inst, fn), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(l_)
        L.append('  THE RECORD INSTANCES (PLACE-papers %s, by line and sha256, no text printed): %s' % (
            K20_PP_REV, '; '.join('%s :%d %s %s' % (p, n, s, 'OPENS AS WANTED' if ok else 'DOES NOT OPEN AS WANTED') for p, n, s, ok in shas)))
        L.append('  THE PLANTED BANKS: (A) b900, a root prompt answered between BEGIN and END, the next act named "The act after b900" ; (B) b910, an '
                 'author`s word naming "The act after b910", no prompt ; (C) b920, a prompt answered by an option')
        for name, rev in (('BEFORE', before), ('AFTER', after)):
            tmp = tempfile.mkdtemp(prefix='b765k20_')
            try:
                got = snapshot(rev, K20_PATHS, tmp)
                j = probe(K20_PROBE, tmp, inst, D)
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b765k20_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
                res[name] = None
                continue
            pl = j['plants']
            hit = dict((a_, bool(pl.get(a_)) and all(x in (pl[a_][1] or '').lower() for x in K20_WANT[a_])) for a_ in K20_WANT)
            clean = hit['b900'] and hit['b910'] and hit['b920'] and bool(j['answer']) and j['carried'] and j['next'] and j['trail'] and j['idem']
            fault = (not pl.get('b900')) or (not pl.get('b910')) or (not j['carried']) or (not j['next']) or (not j['trail'])
            L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
                  '    word() over the plants: (A) b900 %s ; (B) b910 %s ; (C) b920 %s' % tuple(
                      (('line %d, %s' % tuple(pl[a_])) if pl.get(a_) else 'NONE') + (' -- AS WANTED' if hit[a_] else '') for a_ in ('b900', 'b910', 'b920')),
                  '    b764`s answers bank read by word(): %s' % (('line %d, %s' % tuple(j['answer'])) if j['answer'] else 'NONE'),
                  '    b764`s entry`s Carried to line carries the bank and the answer: %s ; its Next line: %s ; the trail`s Next line: %s ; read twice, '
                  'read once: %s' % (j['carried'], j['next'], j['trail'], j['idem']),
                  '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
            res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
    finally:
        if os.path.isabs(inst) and os.path.basename(inst).startswith('b765k20i_'):
            shutil.rmtree(inst, ignore_errors=True)
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and all(ok for _p, _n, _s, ok in shas)


# ================================================================================ [K21] THE ARM G-COEFFS-LAW BEYOND THE FACE
K21_PATHS = ('tools/acts/b765.py', 'tools/standing/act.py')
K21_LOCK = '8d55d1bf'   # ### b764's lock: its worklist and act module as they stood when the arm failed beyond the face
K21_NAMES = ('STANDING_COMMIT', 'CHAIN', 'PASSED_BANK', 'HANDOFF_COMMIT', 'C1_LOCKGATE', 'TIME_ORDER', 'PP_CHAIN', 'C1_RELAY', 'STEPZERO_BANKS',
             'ACT_CURRENT_COMMIT')
K21_CONSTS = r'''
import importlib, json, sys
sys.path.insert(0, 'D:/relay/tools')
name, names = sys.argv[1], sys.argv[2].split(',')
K = importlib.import_module(name)
out, err = {}, {}
for n in names:
    try:
        v = getattr(K, n)
        json.dumps(v)
        out[n] = v
    except Exception as e:
        err[n] = '%s: %s' % (type(e).__name__, str(e)[:120])
print(json.dumps(dict(consts=out, errors=err)))
'''
K21_PROBE = r'''
import json, os, subprocess, sys, types
snap, kjson = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(snap, 'tools', 'standing'))
import act as STANDING_ACT
ROOT, PP = 'D:/relay', 'D:/MY-DOwnloads/PLACE-papers'
k = json.load(open(kjson, encoding='utf-8'))
K = types.SimpleNamespace(**k)
K.CHAIN = tuple(tuple(x) for x in k['CHAIN']); K.PP_CHAIN = tuple(tuple(x) for x in k['PP_CHAIN']); K.TIME_ORDER = tuple(k['TIME_ORDER'])
def gs(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()
def _ct(repo, rev):
    t = gs(repo, 'log', '-1', '--format=%ct', rev) if rev else ''
    return int(t) if t.isdigit() else None
src = open(os.path.join(snap, 'tools', 'acts', 'b765.py'), encoding='utf-8').read().replace('\r', '').split('\n')
i = next(n for n, l in enumerate(src) if l.startswith('def _chain():'))
j = next(n for n in range(i + 1, len(src)) if src[n].startswith(('def ', '#\u27ea')))
ns = dict(K=K, STANDING_ACT=STANDING_ACT, _ct=_ct, ROOT=ROOT)
exec('\n'.join(src[i:j]), ns)
chain = ns['_chain']()
sec = next(n for n, l in enumerate(src) if l.startswith('#\u27eaSECTION checks 33\u27eb'))
ksl = next(src[n] for n in range(sec, len(src)) if src[n].startswith('    ks_ = '))
t = dict([(k_, _ct(ROOT, h_)) for k_, h_ in chain] + [(k_, _ct(PP, h_)) for k_, h_ in K.PP_CHAIN]
         + [('c1', _ct(ROOT, K.C1_RELAY)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)), ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))])
S = dict(r366_chain=chain, t=t)
ks = eval(ksl.split('=', 1)[1].split('#', 1)[0].strip(), dict(S=S, K=K, STANDING_ACT=STANDING_ACT, t_=t))
srt = all(t.get(x) for x in ks) and [t[x] for x in ks] == sorted(t[x] for x in ks)
anc = [(a[0], b[0], subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a[1], b[1]]).returncode == 0) for a, b in zip(chain, chain[1:])]
keys = [x[0] for x in chain]
print(json.dumps(dict(n=len(chain), tail=keys[-4:], ks_tail=list(ks[-4:]), sorted=srt, anc_n=len(anc), anc_false=['%s->%s' % (a, b) for a, b, ok in anc if not ok],
                      lockgate=keys.index('lockgate') if 'lockgate' in keys else None, handoff=keys.index('handoff') if 'handoff' in keys else None,
                      fn=hasattr(STANDING_ACT, 'chain_in_time') and hasattr(STANDING_ACT, 'keys_in_time'))))
'''


def _k21_consts(name, dest):
    """the worklist's constants the arm reads, imported in an interpreter of their own (`python -I`) from the relay's tools/, as JSON at dest."""
    j = probe(K21_CONSTS, name, ','.join(K21_NAMES))
    if 'error' not in j and not j.get('errors'):
        with open(dest, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(j['consts'], fh)
    return j


def _k21_line(j):
    return ('chain keys %d, its last four %s ; the arm`s keys, their last four %s ; their times sorted: %s ; ancestry pairs %d, not ancestors %s ; '
            'the lock gate at %s, the handoff at %s ; act.py`s two functions present: %s' % (
                j['n'], j['tail'], j['ks_tail'], j['sorted'], j['anc_n'], j['anc_false'] or 'none', j['lockgate'], j['handoff'], j['fn']))


def control_k21(before, after):
    """[K21]: the record instance -- b764's worklist at its lock (relay 8d55d1bf, tools/b764_worklist.py, its blob there and at HEAD read by
    sha256), its CHAIN without the lock gate's carry ec439ca3, its HANDOFF_COMMIT 6d4d47f5 set -- read through each revision's composition of
    the arm: the act module's _chain() (tools/acts/b765.py, the function's text taken from the revision and run apart) with the revision's
    tools/standing/act.py, and the arm's key line of checks 33 (its `ks_` line, evaluated apart); each commit's time and each consecutive
    pair's ancestry read from the relay by git. FAULT: the arm's keys out of time order, or a consecutive pair of the chain no ancestor.
    CLEAN: the keys in time order, every pair an ancestor, the lock gate's carry in the chain. And b765's own chain at the repair's
    composition, read from tools/b765_worklist.py where its HANDOFF_COMMIT is set, PENDING where it is not ((R375)(8): the control runs after
    the handoff commit is set), its reading printed and not scored before then."""
    L, res = [], {}
    inst = tempfile.mkdtemp(prefix='b765k21i_')
    try:
        rc, b_lock = git('show', '%s:tools/b764_worklist.py' % K21_LOCK)
        with open(os.path.join(ROOT, 'tools', 'b764_worklist.py'), 'rb') as fh:
            b_head = fh.read().replace(b'\r', b'')
        eq = rc == 0 and hashlib.sha256(b_lock.replace(b'\r', b'')).hexdigest() == hashlib.sha256(b_head).hexdigest()
        kj = os.path.join(inst, 'b764.json')
        c = _k21_consts('b764_worklist', kj)
        L.append('  THE RECORD INSTANCE: b764`s worklist at its lock (relay %s) and in the working tree: %s (sha256 %s) ; its constants read: %s' % (
            K21_LOCK, 'EQUAL' if eq else 'DIFFER', hashlib.sha256(b_head).hexdigest()[:16],
            'ALL %d' % len(K21_NAMES) if ('error' not in c and not c.get('errors')) else (c.get('error') or c.get('errors'))))
        if 'error' not in c and not c.get('errors'):
            cc = c['consts']
            L.append('    CHAIN %d keys, the lock gate`s carry %s in it: %s ; HANDOFF_COMMIT %s ; PASSED_BANK %s' % (
                len(cc['CHAIN']), cc['C1_LOCKGATE'], any(h_[:8] == (cc['C1_LOCKGATE'] or '')[:8] for _k, h_ in cc['CHAIN']), cc['HANDOFF_COMMIT'],
                cc['PASSED_BANK']))
        for name, rev in (('BEFORE', before), ('AFTER', after)):
            tmp = tempfile.mkdtemp(prefix='b765k21_')
            try:
                got = snapshot(rev, K21_PATHS, tmp)
                j = probe(K21_PROBE, tmp, kj) if (eq and os.path.exists(kj)) else dict(error='the record instance not read')
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b765k21_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  %s (%s): THE PROBE FAILED: %s' % (name, rev[:8], j['error']))
                res[name] = None
                continue
            clean = j['sorted'] and not j['anc_false'] and j['lockgate'] is not None and j['fn']
            fault = (not j['sorted']) or bool(j['anc_false'])
            L += ['  %s (relay %s): the files %s' % (name, rev[:8], ', '.join('%s %s' % (p, 'present' if ok else 'ABSENT') for p, ok in got)),
                  '    b764`s chain through this composition: ' + _k21_line(j),
                  '    %s: %s' % (name, 'THE FAULT READ' if fault else ('CLEAN' if clean else 'NEITHER: NOT CLEAN AND NO FAULT READ'))]
            res[name] = 'FAULT' if fault else ('CLEAN' if clean else 'NEITHER')
        kj5 = os.path.join(inst, 'b765.json')
        c5 = _k21_consts('b765_worklist', kj5)
        # ### the handoff is b765's where it descends from the worklist's act_current commit; a value carried from the act before (b764's
        # ### 6d4d47f5, set before b765's base) is not set here (the first run, 11:12:17Z, read the carried value as set: defect (f))
        cs5 = c5.get('consts') or {}
        h5, a5 = cs5.get('HANDOFF_COMMIT'), cs5.get('ACT_CURRENT_COMMIT')
        here = bool(h5) and bool(a5) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a5, h5], capture_output=True).returncode == 0
        if 'error' not in c5 and 'HANDOFF_COMMIT' in cs5 and not here:
            L.append('  b765`S OWN CHAIN (tools/b765_worklist.py, the working tree): PENDING -- HANDOFF_COMMIT not yet set for b765%s; the control runs '
                     'again after it is set ((R375)(8)), this reading not scored%s' % (
                         (' (the worklist carries %s, not a descendant of its act_current commit %s: the act before`s)' % (h5[:8], (a5 or 'NONE')[:8]))
                         if h5 else '',
                         ' (constants not yet readable: %s)' % ', '.join(sorted(c5['errors'])) if c5.get('errors') else ''))
            res['OWN'] = 'PENDING'
        elif 'error' in c5 or c5.get('errors'):
            L.append('  b765`S OWN CHAIN (tools/b765_worklist.py, the working tree): NOT READ: %s' % (c5.get('error') or c5.get('errors')))
            res['OWN'] = 'NOT READ'
        else:
            tmp = tempfile.mkdtemp(prefix='b765k21_')
            try:
                snapshot(after, K21_PATHS, tmp)
                j = probe(K21_PROBE, tmp, kj5)
            finally:
                if os.path.isabs(tmp) and os.path.basename(tmp).startswith('b765k21_'):
                    shutil.rmtree(tmp, ignore_errors=True)
            if 'error' in j:
                L.append('  b765`S OWN CHAIN: THE PROBE FAILED: %s' % j['error'])
                res['OWN'] = None
            else:
                ok5 = j['sorted'] and not j['anc_false'] and j['fn']
                L.append('  b765`S OWN CHAIN (HANDOFF_COMMIT %s) through the repair`s composition (relay %s): %s -- %s' % (
                    c5['consts']['HANDOFF_COMMIT'], after[:8], _k21_line(j), 'CLEAN' if ok5 else 'NOT CLEAN'))
                res['OWN'] = 'CLEAN' if ok5 else 'NOT CLEAN'
    finally:
        if os.path.isabs(inst) and os.path.basename(inst).startswith('b765k21i_'):
            shutil.rmtree(inst, ignore_errors=True)
    return L, res.get('BEFORE') == 'FAULT' and res.get('AFTER') == 'CLEAN' and res.get('OWN') in ('PENDING', 'CLEAN')


CONTROLS = dict(K20=control_k20, K21=control_k21)


def main(argv):
    if len(argv) < 3 or argv[0] not in CONTROLS:
        sys.exit(__doc__ + '\nkeys: %s' % ', '.join(sorted(CONTROLS)))
    key, before, after = argv[0], argv[1], argv[2]
    rc, b = git('rev-parse', before)
    rc2, a = git('rev-parse', after)
    rc3, p = git('rev-parse', '%s^1' % after)
    if rc or rc2 or rc3:
        sys.exit('### A REVISION DOES NOT RESOLVE -- NOTHING READ')
    b, a, p = b.decode().strip(), a.decode().strip(), p.decode().strip()
    head = ['## [%s] THE PLANTED CONTROL (%s): BEFORE relay %s, THE REPAIR`S COMMIT relay %s, its first parent %s -- %s' % (
        key, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), b[:8], a[:8], p[:8], 'THE COMMIT BEFORE' if p == b else 'NOT THE COMMIT BEFORE')]
    L, ok = CONTROLS[key](b, a)
    ok = ok and p == b
    L = head + L + ['### ### **[%s] THE CONTROL %s: THE FAULT READ BEFORE AND CLEAN AFTER: %s.**' % (key, 'AS WANTED' if ok else 'NOT AS WANTED', ok), '']
    print(NL.join(L))
    if '--bank' in argv:
        prior = io.open(BANK, encoding='utf-8').read() if os.path.exists(BANK) else (
            'b765 -- THE PLANTED CONTROLS OF THE REPAIRS, (R375)(8), one section a key, each appended by tools/b765_repair_controls.py --bank' + NL + NL)
        with open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(prior.rstrip(NL) + NL + NL + NL.join(L))
        os.replace(BANK + '.tmp', BANK)
        print('appended to data/b765_repair_controls.txt')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1:])
