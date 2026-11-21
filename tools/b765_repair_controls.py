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


CONTROLS = dict(K20=control_k20)


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
