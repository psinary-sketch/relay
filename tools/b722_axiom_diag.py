# -*- coding: utf-8 -*-
"""b722_axiom_diag.py -- (R332)(10): THE AXIOM STEP DIAGNOSED AT FIVE WAVE 1 PINS BY RUN ID. Written whole at b722 by the Write tool.

  diag [dry]   for each of the five runs b721 read (data/b721_rebuild.txt): the run's record, its job, the step "Axioms of the named terminals"
               (its conclusion, its log section by the step's own group line, the opening error lines printed), the workflow file at the
               run's head sha and the step's text there, and the pin's tree (the files the step reads and the modules it imports, looked up
               at the pin, at main and at rebuild-b721); the cause classed by the ruling's four classes, the rule printed before any kernel;
               a repair route priced per kernel on rebuild-b721 (commits, pushes, runs), nothing committed, pushed or dispatched.
               -> data/b722_axiom_diag.txt (.json). Read-only: `gh api` GETs alone, no identifier of the author in any request.
"""
import base64
import io
import json
import os
import re
import subprocess
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b722_coeffs as CO            # noqa: E402  ### the free-memory read under the hold (b722's own, imported)

ACT = 'b722'
OWNER = 'psinary-sketch'
STEP = 'Axioms of the named terminals'
# ### (R332)(10): the five pins and their runs, as the ruling names them; the pins as data/b721_rebuild.txt :14-:47 prints them
RUNS = [('SIDE-kernel', 40706230156, '0e5233f011'), ('SIDE-archimedean', 40706397470, '8019d9dfee'),
        ('SIDE-frobenius', 40713201832, '2efe9f2'), ('SIDE-spinor', 40706542282, 'b235bc6235'), ('SIDE-rcurve', 40706645404, 'd5f33b44ef')]
CLASSES = ['TARGETS ABSENT AT THE PIN', 'BUILD TARGET NOT COVERING THE AXIOM FILE`S IMPORTS', 'STEP NOT THE PIN`S OWN', 'OTHER']
RULE = ('THE RULE, PRINTED BEFORE ANY KERNEL ((R332)(10)): the cause is read from the step`s opening error lines and the files they name. '
        'TARGETS ABSENT AT THE PIN -- the step reads its target list from the checked-out tree (print_targets.txt) and that list is absent at the '
        'pin while the kernel carries it elsewhere (main); BUILD TARGET NOT COVERING THE AXIOM FILE`S IMPORTS -- every module the axiom file '
        'imports is present at the pin and one is not built by the run`s target; STEP NOT THE PIN`S OWN -- the step was written for another '
        'tree than the pin (another kernel`s workflow, or main`s step naming modules or a list the pin never carried); OTHER -- none of these.')


def gh(*a):
    p = subprocess.run(['gh', 'api', *a], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def content(repo, path, ref):
    o, rc = gh('repos/%s/%s/contents/%s?ref=%s' % (OWNER, repo, path, ref))
    return base64.b64decode(json.loads(o)['content']).decode('utf-8') if rc == 0 else None


def tree(repo, ref):
    o, rc = gh('repos/%s/%s/git/trees/%s?recursive=1' % (OWNER, repo, ref))
    return set(x['path'] for x in json.loads(o)['tree'] if x['type'] == 'blob') if rc == 0 else set()


def one(repo, rid, pin):
    r = json.loads(gh('repos/%s/%s/actions/runs/%d' % (OWNER, repo, rid))[0])
    job = json.loads(gh('repos/%s/%s/actions/runs/%d/jobs' % (OWNER, repo, rid))[0])['jobs'][0]
    st = [s for s in job['steps'] if s['name'] == STEP][0]
    log = gh('repos/%s/%s/actions/jobs/%d/logs' % (OWNER, repo, job['id']))[0].split(NL)
    i0 = next(i for i, l in enumerate(log) if l[:19] >= st['started_at'][:19] and '##[group]Run' in l)
    j = next((k for k in range(i0 + 1, len(log)) if '##[group]Run' in log[k]), len(log))
    sec = [re.sub(r'\x1b\[[0-9;]*m', '', l[29:]) for l in log[i0:j]]
    end = next(k for k, l in enumerate(sec) if l.startswith('##[endgroup]'))
    errs = [l for l in sec[end + 1:] if l.strip()][:6]
    err_src = 'the step`s log after its script'
    if not errs:                                      # ### a step exiting 0 (`|| true`) leaves its errors in the artifact's out/axioms.txt
        arts = json.loads(gh('repos/%s/%s/actions/runs/%d/artifacts' % (OWNER, repo, rid))[0])['artifacts']
        p = subprocess.run(['gh', 'api', 'repos/%s/%s/actions/artifacts/%d/zip' % (OWNER, repo, arts[0]['id'])], capture_output=True)
        z = zipfile.ZipFile(io.BytesIO(p.stdout))
        ax = z.read('axioms.txt').decode('utf-8', 'replace').split(NL)
        errs = [l for l in ax if 'error' in l][:6]
        err_src = 'the run`s artifact %s, axioms.txt (%d lines; the step exits 0 by `|| true`)' % (arts[0]['name'], len(ax))
    script = [l for l in sec[1:end] if not l.startswith(('shell:', 'env:', '  HOLD_MB', '  TARGET'))]
    target = next((l.split(':', 1)[1].strip() for l in sec[:end] if l.startswith('  TARGET:')), '')
    full = gh('repos/%s/%s/commits/%s' % (OWNER, repo, pin), '--jq', '.sha')[0].strip()
    pt = tree(repo, full)
    ptm, ptb = tree(repo, 'main'), tree(repo, 'rebuild-b721')
    wf_at = content(repo, r['path'], r['head_sha'])
    reads_targets = any('print_targets.txt' in l for l in script)
    imports = [l.split()[1] for l in script if l.startswith('import ')]
    mods = dict((m, m.replace('.', '/') + '.lean') for m in imports)
    out = dict(kernel=repo, run=rid, pin=full[:10], head_sha=r['head_sha'][:10], head_branch=r['head_branch'], event=r['event'],
               path=r['path'], conclusion=r['conclusion'], step_conclusion=st['conclusion'], target=target, errors=errs, errors_from=err_src,
               step_reads_targets=reads_targets, step_imports=len(imports),
               targets_at=dict(pin='print_targets.txt' in pt, main='print_targets.txt' in ptm, rebuild='print_targets.txt' in ptb),
               imports_absent_at_pin=[m for m, f in mods.items() if f not in pt],
               imports_present_at_main=[m for m, f in mods.items() if f in ptm],
               workflow_at_pin=r['path'] in pt, workflow_at_main=r['path'] in ptm, workflow_text_at_head=bool(wf_at))
    names = []
    if reads_targets and 'print_targets.txt' in ptm:
        names = [n.strip() for n in content(repo, 'print_targets.txt', 'main').split(NL) if n.strip()]
        src = dict((f, None) for f in pt if f.endswith('.lean'))
        found = dict((n, False) for n in names)
        for f in sorted(src):
            t = content(repo, f, full) or ''
            for n in names:
                if not found[n] and re.search(r'\b(?:theorem|lemma|def|abbrev|structure|inductive|class|instance)\s+(?:\S+\.)?%s\b' % re.escape(n.split('.')[-1]), t):
                    found[n] = f
        out['main_targets'] = names
        out['main_targets_declared_at_pin'] = dict((n, v or None) for n, v in found.items())
    return out


def classify(x):
    e = ' '.join(x['errors'])
    if x['step_reads_targets'] and "cannot stat 'print_targets.txt'" in e:
        if x['targets_at']['main'] and not x['targets_at']['pin']:
            return CLASSES[0], 'the step`s target list print_targets.txt is read from the pin`s tree, absent at the pin and present at main'
        if not x['targets_at']['main'] and not x['targets_at']['pin']:
            return CLASSES[2], ('the step reads print_targets.txt, which this kernel carries at no ref read (pin, main, rebuild-b721): the '
                                'workflow is another kernel`s (data/b721_rebuild.txt :8, SIDE-explicit-formula`s build-module.yml verbatim)')
    if 'object file' in e and 'does not exist' in e:
        if x['imports_absent_at_pin']:
            return CLASSES[2], ('main`s step imports %d modules, %d absent at the pin (%s), present at main: the step was written for main`s '
                                'tree' % (x['step_imports'], len(x['imports_absent_at_pin']), ', '.join(x['imports_absent_at_pin'])))
        return CLASSES[1], 'every import present at the pin; one not built by the target %s' % x['target']
    return CLASSES[3], 'no class`s predicate met'


def price(x, cls):
    if cls == CLASSES[0]:
        nd = [n for n, v in (x.get('main_targets_declared_at_pin') or {}).items() if not v]
        nn = len(x.get('main_targets') or [])
        return ('one commit on rebuild-b721 adding print_targets.txt (main`s %d names, %s), one push of the branch, one dispatch of main`s '
                'build-module.yml at the ref rebuild-b721 (about 3-4 minutes of runner, as b721`s run); no main or tag touched' % (
                    nn, ('each found declared at the pin by name' if not nd else '%d of them not found declared at the pin by name -- %s -- '
                         'each dropped or kept on the author`s word' % (len(nd), ', '.join(nd)))))
    if cls == CLASSES[2] and x['step_reads_targets']:
        return ('one commit on rebuild-b721 adding print_targets.txt naming SIDEFrobenius`s terminals at the pin (the list is the author`s '
                'word: the kernel never carried one), one push (the branch`s own workflow runs on push, data/b721_rebuild.txt :34-:42); one run')
    if cls == CLASSES[2]:
        return ('the step is main`s workflow`s fixed list: the dispatch reads it from main, so no commit on rebuild-b721 changes it; the route '
                'is the SIDE-frobenius form -- one commit on rebuild-b721 carrying build-module.yml with a push trigger and an axiom step '
                'importing only the pin`s modules (%d of main`s %d imports dropped) and naming terminals declared at the pin, one push, one '
                'run; each line of the changed workflow for the author`s word first' % (len(x['imports_absent_at_pin']), x['step_imports']))
    if cls == CLASSES[1]:
        return 'the run`s target widened to cover the imports: one dispatch with the wider target, no commit'
    return 'NOT PRICED: the cause is not classed'


def diag(*a):
    t0 = time.time()
    L = ['%s -- (R332)(10): THE AXIOM STEP "%s" DIAGNOSED AT FIVE WAVE 1 PINS BY RUN ID (%s)' % (
        ACT, STEP, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### ' + RULE, '### read-only: gh api GETs (the run, its job, its log, the workflow at the run`s head, the trees at the pin, main and '
         'rebuild-b721); nothing committed, pushed or dispatched; no lean process on this host.', '']
    J = []
    for repo, rid, pin in RUNS:
        CO.free_or_exit('the read of %s run %d' % (repo, rid))
        x = one(repo, rid, pin)
        cls, why = classify(x)
        x['class'], x['why'], x['price'] = cls, why, price(x, cls)
        J.append(x)
        L += ['## %s -- run %d (pin %s ; the run`s head %s on %s by %s ; %s) ; run %s, step %s' % (
            repo, rid, x['pin'], x['head_sha'], x['head_branch'], x['event'], x['path'], x['conclusion'], x['step_conclusion']),
              '  THE OPENING ERROR LINES (%s):' % x['errors_from']] +['    | ' + l[:300] for l in x['errors']] + [
              '  print_targets.txt: pin %s, main %s, rebuild-b721 %s ; the step reads it: %s ; imports in the step %d, absent at the pin %d' % (
                  x['targets_at']['pin'], x['targets_at']['main'], x['targets_at']['rebuild'], x['step_reads_targets'], x['step_imports'],
                  len(x['imports_absent_at_pin']))]
        if x.get('main_targets'):
            L.append('  main`s targets declared at the pin (by name): ' + ' ; '.join(
                '%s %s' % (n, ('AT ' + v) if v else 'NOT FOUND') for n, v in x['main_targets_declared_at_pin'].items()))
        L += ['  CLASS: %s -- %s' % (cls, why), '  REPAIR ON rebuild-b721, PRICED: ' + x['price'], '']
    tally = dict((c, sum(1 for x in J if x['class'] == c)) for c in CLASSES)
    L.append('### ### **THE AXIOM STEP AT FIVE PINS: %s ; NOTHING COMMITTED, PUSHED OR DISPATCHED ; %d s.**' % (
        ' ; '.join('%s %d' % kv for kv in tally.items()), int(time.time() - t0)))
    print(NL.join(L))
    if 'dry' in a:
        return
    for name, data in (('%s_axiom_diag.txt' % ACT, NL.join(L) + NL), ('%s_axiom_diag.json' % ACT, json.dumps(J, indent=1, ensure_ascii=False) + NL)):
        p = os.path.join(D, name)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print('written data/%s_axiom_diag.txt, .json' % ACT)


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'diag':
        sys.exit('usage: b722_axiom_diag.py diag [dry]')
    diag(*sys.argv[2:])
