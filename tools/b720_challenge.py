# -*- coding: utf-8 -*-
"""b720_challenge.py -- (R330)(5)(ii), THE CHALLENGE FILE FOR h2_sign_iff_rh at b718's price, form (A) (relay data/b718_challenge_price.txt
(2)(A)): a Lean file carrying the statement alone and its definitions' imports, written on a branch of SIDE-explicit-formula; one runner
dispatch reading that the file elaborates and that the kernel's h2_sign_iff_rh has that statement, read by its run id. No lean or lake
process runs on this host (N1). Main untouched (the commit is made with git's plumbing from main's tree, the working tree and main's ref
unmoved); no tag. Two files are added and nothing else: the challenge module, and a root ChainProbe.lean (imported by no module) that the
workflow's probe step (b706, build-module.yml :101-:115) runs above the target's modules after the build -- the statement check and its
two controls. Carried in shape from tools/b718_pin.py (its free-memory hold, gh calls, artifact read and opening error lines).

  plan              the kernel's main, the branch's absence, the two files' text; writes nothing
  make              the commit on main's tree and the branch BRANCH at it; prints the diff; one ref written, nothing pushed
  dispatch          the one dispatch (refused if one is banked, or if origin's BRANCH is not the local tip); appends its row
  read <id>         the run read by id: status, conclusion, build exit, the opening error lines, the probe's lines; appends its row
  bank              writes data/b720_challenge.txt and data/b720_challenge.json from data/b720_challenge_rows.json
"""
import io
import json
import os
import re
import subprocess
import sys
import time

NL = chr(10)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b718_pin import free_mb, HOLD_MB, hold_or_exit, gh, g, gs, opening_errors   # noqa: E402  (read-only helpers; no route of b718_pin runs)

KERNEL = 'SIDE-explicit-formula'
REPO = 'D:/' + KERNEL
OWNER = 'psinary-sketch'
BRANCH = 'challenge-b720-h2-sign-iff-rh'
MODULE = 'SIDEExplicitFormula.Challenge.H2SignIffRH'
MODPATH = 'SIDEExplicitFormula/Challenge/H2SignIffRH.lean'
TARGET = MODULE + ' SIDEExplicitFormula.Seam'
ROWS = os.path.join(D_, 'b720_challenge_rows.json')
DL = os.path.join(os.environ.get('TEMP', ROOT), 'b720_challenge_artifacts')   # downloaded run artifacts: outside the relay, read as data

CHALLENGE = '''/-
SIDE-explicit-formula -- SIDEExplicitFormula/Challenge/H2SignIffRH.lean
A CHALLENGE FILE (act b720, ruling (R330)(5)(ii); form (A) of relay data/b718_challenge_price.txt): the statement of
`SIDEExplicitFormula.B321.h2_sign_iff_rh` (SIDEExplicitFormula/Seam.lean :101) alone, over the imports of its two definitions --
`SIDEExplicitFormula.B321.h2_sign` (SIDEExplicitFormula/H2Sign.lean :29) and Mathlib's `RiemannHypothesis`
(Mathlib/NumberTheory/LSeries/RiemannZeta.lean :185, at de5ce8a9). Its proof is `sorry`: the file states and proves nothing.
Form (A)'s trust surface is every definition the first import carries (classK, poleTerm, primeSum, archTerm, paperFT, gammaBracket,
weilTest), not the statement alone. An equivalence between open statements; it proves neither.
Imported by no module of the kernel; on a branch of its own; main untouched, no tag.
-/
import SIDEExplicitFormula.H2Sign
import Mathlib.NumberTheory.LSeries.RiemannZeta

theorem h2_sign_iff_rh_challenge : SIDEExplicitFormula.B321.h2_sign ↔ RiemannHypothesis := by
  sorry
'''

PROBE = '''/-
ChainProbe.lean (act b720, ruling (R330)(5)(ii)) -- run by build-module.yml's probe step above the target's modules
(SIDEExplicitFormula.Challenge.H2SignIffRH and SIDEExplicitFormula.Seam). Imported by no module. It reads whether the kernel's
h2_sign_iff_rh has the challenge's statement, by comparing the two declarations' types as expressions, with two controls made the
same way: the statement built by hand from its two constants must compare EQUAL (the construction is sound), and a planted
statement (h2_sign_aim in h2_sign's place) must compare UNEQUAL (the comparison can fail). Then the term check, and the axioms.
-/
open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let some k := env.find? `SIDEExplicitFormula.B321.h2_sign_iff_rh
    | throwError "PROBE ABSENT: SIDEExplicitFormula.B321.h2_sign_iff_rh"
  let some c := env.find? `h2_sign_iff_rh_challenge
    | throwError "PROBE ABSENT: h2_sign_iff_rh_challenge"
  unless env.contains `SIDEExplicitFormula.B321.h2_sign_aim do
    throwError "PROBE ABSENT: SIDEExplicitFormula.B321.h2_sign_aim"
  logInfo m!"PROBE KERNEL TYPE: {k.type}"
  logInfo m!"PROBE CHALLENGE TYPE: {c.type}"
  if k.type == c.type then
    logInfo "PROBE MATCH: the kernel's h2_sign_iff_rh has the challenge's statement (the two types equal as expressions)"
  else
    logInfo "PROBE DIFFER: the kernel's h2_sign_iff_rh does not have the challenge's statement"
  let built := mkApp2 (mkConst ``Iff) (mkConst `SIDEExplicitFormula.B321.h2_sign) (mkConst `RiemannHypothesis)
  if built == k.type then
    logInfo "PROBE CONTROL 1 EQUAL, as wanted: the statement built from its two constants equals the kernel's type"
  else
    logInfo "PROBE CONTROL 1 FAILED: the statement built from its two constants differs from the kernel's type"
  let planted := mkApp2 (mkConst ``Iff) (mkConst `SIDEExplicitFormula.B321.h2_sign_aim) (mkConst `RiemannHypothesis)
  if planted == k.type then
    logInfo "PROBE CONTROL 2 FAILED: the planted statement compared equal"
  else
    logInfo "PROBE CONTROL 2 UNEQUAL, as wanted: the planted statement (h2_sign_aim in h2_sign's place) differs"

theorem b720_probe_term_check : SIDEExplicitFormula.B321.h2_sign ↔ RiemannHypothesis :=
  SIDEExplicitFormula.B321.h2_sign_iff_rh

#print axioms h2_sign_iff_rh_challenge
#print axioms SIDEExplicitFormula.B321.h2_sign_iff_rh
#print axioms b720_probe_term_check
'''

FILES = {MODPATH: CHALLENGE, 'ChainProbe.lean': PROBE}


def rows_load():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def rows_add(row):
    rs = rows_load() + [row]
    t = json.dumps(rs, indent=1, ensure_ascii=False)
    io.open(ROWS + '.tmp', 'w', encoding='utf-8', newline='\n').write(t + NL)
    os.replace(ROWS + '.tmp', ROWS)


def blob(data):
    c, o, e = g(REPO, 'hash-object', '-w', '--stdin', inp=data.encode('utf-8'))
    assert c == 0, e
    return o.strip()


def plan():
    print('### %s main %s ; HEAD %s on %s ; tracked changes %s ; branch %s exists %s' % (
        KERNEL, gs(REPO, 'rev-parse', '--short=8', 'main'), gs(REPO, 'rev-parse', '--short=8', 'HEAD'),
        gs(REPO, 'rev-parse', '--abbrev-ref', 'HEAD'), bool(gs(REPO, 'status', '--porcelain', '--untracked-files=no')),
        BRANCH, bool(gs(REPO, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH))))
    for p in FILES:
        print('### %s at main: %s' % (p, 'PRESENT' if g(REPO, 'cat-file', '-e', 'main:' + p)[0] == 0 else 'absent'))
    print('### target %r ; one dispatch' % TARGET)
    for p, t in FILES.items():
        print('=== %s (%d lines)' % (p, t.count(NL)))
        print(t.rstrip())


def make():
    if gs(REPO, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + BRANCH):
        sys.exit('## branch %s exists; nothing written' % BRANCH)
    for p in FILES:
        if g(REPO, 'cat-file', '-e', 'main:' + p)[0] == 0:
            sys.exit('## %s is present at main; nothing written' % p)
    c, idx, e = g(REPO, 'ls-tree', '-r', '--full-tree', 'main')
    assert c == 0, e
    rows = [l for l in idx.split(NL) if l.strip()]
    for p, t in FILES.items():
        rows.append('100644 blob %s\t%s' % (blob(t), p))
    # mktree takes one level; build the nested tree through a temporary index instead, the working tree and main untouched
    env = dict(os.environ, GIT_INDEX_FILE=os.path.join(os.environ.get('TEMP', ROOT), 'b720_challenge.index'))
    if os.path.exists(env['GIT_INDEX_FILE']):
        os.remove(env['GIT_INDEX_FILE'])
    r = subprocess.run(['git', '-C', REPO, 'update-index', '--index-info'], input=(NL.join(
        '%s %s %s\t%s' % tuple(l.split('\t')[0].split() + [l.split('\t', 1)[1]]) for l in rows) + NL).encode('utf-8'), capture_output=True, env=env)
    assert r.returncode == 0, r.stderr
    r = subprocess.run(['git', '-C', REPO, 'write-tree'], capture_output=True, env=env)
    assert r.returncode == 0, r.stderr
    tree = r.stdout.decode().strip()
    os.remove(env['GIT_INDEX_FILE'])
    msg = ('b720 under (R330)(5)(ii): the challenge file for h2_sign_iff_rh, form (A) of relay data/b718_challenge_price.txt -- '
           '%s, the statement alone over its definitions\' imports, proof sorry; ChainProbe.lean at the root (imported by no module), '
           'the statement check and its two controls for build-module.yml\'s probe step; nothing else changed; main untouched, no tag' % MODPATH)
    c, cm, e = g(REPO, 'commit-tree', tree, '-p', 'main', '-m', msg)
    assert c == 0, e
    cm = cm.strip()
    c, _o, e = g(REPO, 'branch', BRANCH, cm)
    assert c == 0, e
    print('## %s at %s (parent main %s)' % (BRANCH, cm[:10], gs(REPO, 'rev-parse', '--short=8', 'main')))
    print(g(REPO, 'diff', '--stat', 'main', cm)[1].rstrip())
    print('## main unmoved: %s ; working tree tracked changes: %s' % (gs(REPO, 'rev-parse', '--short=8', 'main'),
                                                                    bool(gs(REPO, 'status', '--porcelain', '--untracked-files=no'))))


def dispatch():
    if [r for r in rows_load() if r.get('kind') == 'dispatch']:
        sys.exit('one dispatch is banked; the ruling allows one; nothing dispatched')
    sha = gs(REPO, 'rev-parse', 'refs/heads/' + BRANCH)
    c, o, e = g(REPO, 'ls-remote', 'origin', 'refs/heads/' + BRANCH)
    if not o.startswith(sha):
        sys.exit('## origin %s is %r, not the local %s; nothing dispatched' % (BRANCH, o.strip()[:12], sha[:12]))
    fm = hold_or_exit('the dispatch of the challenge')
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print('### free memory %d MB (hold %d) ; dispatching %s at main, ref %s, target %s' % (fm, HOLD_MB, KERNEL, sha[:12], TARGET))
    c, o, e = gh('workflow', 'run', 'build-module.yml', '-R', '%s/%s' % (OWNER, KERNEL), '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + TARGET)
    print('   gh workflow run: exit %d %s %s' % (c, o.strip(), e.strip()))
    if c != 0:
        sys.exit('dispatch refused; no row')
    rid = None
    for _i in range(12):
        time.sleep(5)
        c, o, e = gh('run', 'list', '-R', '%s/%s' % (OWNER, KERNEL), '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '-L', '5',
                     '--json', 'databaseId,createdAt,status')
        new = [r for r in json.loads(o or '[]') if r['createdAt'] >= t0]
        if new:
            rid = new[-1]['databaseId']
            break
    print('   run id %s (created at or after %s)' % (rid, t0))
    rows_add({'kind': 'dispatch', 'kernel': KERNEL, 'sha': sha, 'target': TARGET, 'at': t0, 'run': rid, 'free_mb': free_mb()})


def read(rid):
    fm = hold_or_exit('the read of run %s' % rid)
    print('### free memory %d MB (hold %d) ; reading %s run %s' % (fm, HOLD_MB, KERNEL, rid))
    R = '%s/%s' % (OWNER, KERNEL)
    c, o, e = gh('run', 'view', str(rid), '-R', R, '--json', 'status,conclusion,createdAt,updatedAt,headSha,event,url,jobs')
    v = json.loads(o) if c == 0 else {}
    print('   status %s conclusion %s ; %s -> %s ; event %s' % (v.get('status'), v.get('conclusion'), v.get('createdAt'), v.get('updatedAt'), v.get('event')))
    if v.get('status') != 'completed':
        print('   not completed; no row')
        return
    row = {'kind': 'read', 'kernel': KERNEL, 'run': rid, 'free_mb': fm, 'status': v.get('status'), 'conclusion': v.get('conclusion'),
           'created': v.get('createdAt'), 'updated': v.get('updatedAt'),
           'steps': [(s.get('name'), s.get('conclusion')) for j in v.get('jobs', []) for s in j.get('steps', [])]}
    d = os.path.join(DL, '%s_%s' % (KERNEL, rid))
    if not os.path.isdir(d):
        os.makedirs(d)
        c, o, e = gh('run', 'download', str(rid), '-R', R, '-D', d)
        print('   artifact download: exit %d %s' % (c, e.strip()[:200]))
    f = {}
    for root, _ds, fs in os.walk(d):
        for n in fs:
            f[n] = os.path.join(root, n)

    def txt(n):
        return io.open(f[n], encoding='utf-8', errors='replace').read() if n in f else None
    ref, ex, log, mem, ax = txt('ref.txt'), txt('build_exit.txt'), txt('build.log') or '', txt('mem.log') or '', txt('axioms.txt') or ''
    probe, plog = txt('chainprobe.txt') or '', txt('chainprobe_log.txt') or ''
    low = re.findall(r'^LOW (\S+)', mem, re.M)
    stops = re.findall(r'^STOP .*$', mem, re.M)
    errs = opening_errors(log)
    plines = [l for l in probe.replace('\r', '').split(NL) if l.strip()]
    pk = [l for l in plines if 'PROBE ' in l or 'axioms' in l or 'error' in l.lower() or 'sorryAx' in l or 'propext' in l]
    chal_warn = [l for l in log.replace('\r', '').split(NL) if 'H2SignIffRH' in l]
    row.update({'ref': (ref or '').split(), 'build_exit': (ex or '').strip(), 'mem_low_mb': low[-1] if low else None, 'stops': stops,
                'error_lines': errs, 'log_lines': log.count(NL), 'sorry_warnings': len(re.findall(r'declaration uses .sorry.', log)),
                'challenge_log_lines': chal_warn[:12], 'probe_log': plog.strip(), 'probe_lines': pk[:60]})
    built = row['build_exit'] == '0' and not stops and not errs
    match = any('PROBE MATCH' in l for l in plines)
    c1 = any('PROBE CONTROL 1 EQUAL' in l for l in plines)
    c2 = any('PROBE CONTROL 2 UNEQUAL' in l for l in plines)
    perr = [l for l in plines if re.search(r'(^|\s)error(:|\b)', l)]
    row.update({'elaborates': built, 'match': match, 'control1': c1, 'control2': c2, 'probe_errors': perr[:12]})
    if built and match and c1 and c2 and not perr:
        verdict = 'ELABORATES; THE KERNEL\'S STATEMENT MATCHES'
    elif built and not plines:
        verdict = 'ELABORATES; THE PROBE PRINTED NOTHING (the statement check NOT READ)'
    elif built:
        verdict = 'ELABORATES; THE STATEMENT CHECK NOT AS WANTED (match %s, control 1 %s, control 2 %s, probe errors %d)' % (match, c1, c2, len(perr))
    else:
        verdict = 'DOES NOT ELABORATE (HELD)' if row['build_exit'] not in ('', None) else 'NO EXIT READ'
    row['verdict'] = verdict
    print('   ref %s ; build exit %r ; memory low %s MB ; stops %d ; log lines %d ; sorry warnings %d' % (
        row['ref'], row['build_exit'], row['mem_low_mb'], len(stops), row['log_lines'], row['sorry_warnings']))
    for l in errs:
        print('     | ' + l[:220])
    print('   the challenge module in the log:')
    for l in chal_warn[:12]:
        print('     | ' + l[:220])
    print('   probe: %s' % row['probe_log'][:200])
    for l in pk[:60]:
        print('     > ' + l[:300])
    print('   ELABORATES %s ; MATCH %s ; CONTROL 1 %s ; CONTROL 2 %s ; probe errors %d ; VERDICT %s' % (built, match, c1, c2, len(perr), verdict))
    rows_add(row)


def bank():
    rs = rows_load()
    disp = [r for r in rs if r['kind'] == 'dispatch']
    reads = [r for r in rs if r['kind'] == 'read']
    out = ['b720 -- (R330)(5)(ii): THE CHALLENGE FILE FOR h2_sign_iff_rh, FORM (A), ON A BRANCH OF %s, ONE DISPATCH READ BY ITS RUN ID (%s)' % (
        KERNEL, time.strftime('%Y-%m-%d', time.gmtime())), '',
        '### Written by tools/b720_challenge.py bank from data/b720_challenge_rows.json (the rows its dispatch and read routes appended). The',
        '### branch %s carries two files on main\'s tree, made by git plumbing: %s and the root ChainProbe.lean' % (BRANCH, MODPATH),
        '### (imported by no module), run by build-module.yml\'s probe step. Main untouched, no tag; no lean or lake process on this host.', '',
        '## THE CHALLENGE FILE, AS COMMITTED', ''] + ['    ' + l for l in CHALLENGE.rstrip().split(NL)] + ['',
        '## THE PROBE, AS COMMITTED', ''] + ['    ' + l for l in PROBE.rstrip().split(NL)] + ['',
        'DISPATCHES %d (one allowed) ; READ %d' % (len(disp), len(reads)), '']
    for d in disp:
        out.append('  DISPATCH run %s at %s, ref %s, target %r, host free %d MB' % (d['run'], d['at'], d['sha'][:10], d['target'], d['free_mb']))
    for r in reads:
        out.append('  READ run %s: %s %s ; %s -> %s ; build exit %s ; memory low %s MB ; stops %d ; sorry warnings %d ; host free %d MB at the read' % (
            r['run'], r['status'], r['conclusion'], r['created'], r['updated'], r['build_exit'], r['mem_low_mb'], len(r['stops']),
            r['sorry_warnings'], r['free_mb']))
        for l in r['error_lines']:
            out.append('      | ' + l[:220])
        out.append('  the challenge module in the build log:')
        for l in r['challenge_log_lines']:
            out.append('      | ' + l[:220])
        out.append('  the probe: %s' % r['probe_log'][:200])
        for l in r['probe_lines']:
            out.append('      > ' + l[:300])
        out.append('  ELABORATES %s ; MATCH %s ; CONTROL 1 (built statement equal) %s ; CONTROL 2 (planted statement unequal) %s ; probe errors %d' % (
            r['elaborates'], r['match'], r['control1'], r['control2'], len(r['probe_errors'])))
        out.append('  VERDICT: %s' % r['verdict'])
    out += ['', 'SCOPE: an equivalence between open statements; the challenge proves neither (its proof is sorry), and the kernel\'s theorem is',
            'read for its statement only. Form (A)\'s trust surface is every definition SIDEExplicitFormula.H2Sign carries, not the statement alone.']
    t = NL.join(out) + NL
    j = json.dumps({'branch': BRANCH, 'module': MODULE, 'target': TARGET, 'dispatch': disp, 'read': reads}, indent=1, ensure_ascii=False) + NL
    io.open(os.path.join(D_, 'b720_challenge.txt'), 'w', encoding='utf-8', newline='\n').write(t)
    io.open(os.path.join(D_, 'b720_challenge.json'), 'w', encoding='utf-8', newline='\n').write(j)
    print(t)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['plan']:
        plan()
    elif a == ['make']:
        make()
    elif a == ['dispatch']:
        dispatch()
    elif len(a) == 2 and a[0] == 'read':
        read(a[1])
    elif a == ['bank']:
        bank()
    else:
        sys.exit(__doc__)
