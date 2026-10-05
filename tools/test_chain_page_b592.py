# -*- coding: utf-8 -*-
"""test_chain_page_b592.py -- THE TEST OF THE TWO GENERATOR CLAUSES b592 ADDED TO tools/chain_page.py, on the author's answers
before b592's seal (relay data/b592_author_answers.txt, prompts 6 and 7).

### (1)-(3) THE PREMISE CLAUSE: the χ page re-emitted from a v0.16 probe output under the generator as it stood at relay
###   652b58d5 and as it stands -- every DERIVES Correspondence row byte for byte unchanged; the INTERFACES row of
###   epstein_not_h2_sign_cfg printing its premise; no row but an INTERFACES row changed.
### (4)-(8) THE KEYSTONE CLAUSE, on a throwaway git repository built in a temporary directory: a backticked `detector` and a
###   qualified Schema.detector each name the node; the ten English-word sentences (the first use of the word in each of the
###   ten files b592 found) name it under the old rule and not under the new; a list with no plain lower-case name builds the
###   same match under both rules (the ζ list's short names, against PLACE-papers HEAD).
### Usage: python tools/test_chain_page_b592.py [<chi_probe_out.txt>]   (default: b592's χ probe output at relay 12c15c80)
### ### b629, (R239)(3): CASES (1)-(3) RUN NOTHING LIVE. b592's χ list and probe output are read by `git show` at relay 12c15c80
### (their one commit); both generators' every HEAD read is redirected for the run -- relay HEAD to 12c15c80, PLACE-papers HEAD to
### ba5f0ea -- and both run the E0 rule's blob at 12c15c80, the freeze of test_chain_page_b596.py's case (1). The generators' code is
### the subject: the one at 652b58d5 and the one as it stands. tools/chain_page.py is untouched (its `git` and `E0` are swapped here).
"""
import io
import os
import re
import subprocess
import sys
import tempfile
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRE_RELAY = '652b58d5'
RELAY_PIN = '12c15c80'
PRE_PP = 'ba5f0ea'
ENGLISH = [
    'If the brain is a prime detector:',
    'The bimodality is therefore a *determination detector*.',
    '- Independence detector correctly predicted Continuum',
    'The detector predicted independence.',
    'measurement (above) and retained as a **calibrated detector**.',
    'and the repair/detector pair for vacuity that has migrated',
    'the repair/detector pair for vacuity, carried in the edition',
    'It is a detector, not a proof of absence.',
    'the detector\'s 50-digit reach',
    '> **The detector returned 20 for KEYSTONE.',
]


def old_generator():
    src = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/chain_page.py' % PRE_RELAY], capture_output=True).stdout.decode('utf-8')
    m = types.ModuleType('chain_page_before')
    m.__dict__['__file__'] = os.path.join(ROOT, 'tools', 'chain_page.py')
    exec(compile(src, 'chain_page_before', 'exec'), m.__dict__)
    return m


def relay_blob(rev, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def e0_at(rev):
    m = types.ModuleType('e0_rule_%s' % rev)
    exec(compile(relay_blob(rev, 'tools/e0_rule.py').decode('utf-8'), 'e0_rule@%s' % rev, 'exec'), m.__dict__)
    return m


def frozen_git(gen):
    """### a generator's own `git`, every HEAD read redirected: relay HEAD -> 12c15c80, PLACE-papers HEAD -> ba5f0ea."""
    real = gen.git

    def git(repo, *a):
        a = list(a)
        r = repo.replace(chr(92), '/')
        if a[:1] == ['show'] and len(a) > 1 and a[1].startswith('HEAD:'):
            if r == ROOT.replace(chr(92), '/'):
                a[1] = RELAY_PIN + a[1][4:]
            elif r == gen.PP:
                a[1] = PRE_PP + a[1][4:]
        elif r == gen.PP and a[:1] == ['grep'] and 'HEAD' in a:
            a[a.index('HEAD')] = PRE_PP
        return real(repo, *a)
    return git


def frozen_build(gen, nodes, tmp, probe):
    saved = (gen.git, gen.E0)
    gen.git, gen.E0 = frozen_git(gen), e0_at(RELAY_PIN)
    try:
        return gen.build(nodes, tmp, probe)
    finally:
        gen.git, gen.E0 = saved


def main(argv):
    tmp = tempfile.mkdtemp()
    nodes, probe = os.path.join(tmp, 'b592_nodes_chi.txt'), os.path.join(tmp, 'b592_chi_probe_out.txt')
    io.open(nodes, 'wb').write(relay_blob(RELAY_PIN, 'data/b592_nodes_chi.txt'))
    if argv:
        probe = argv[0]
    else:
        io.open(probe, 'wb').write(relay_blob(RELAY_PIN, 'data/b592_chi_probe_out.txt'))
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-100s %s' % (label, 'PASS' if cond else '### FAIL'))

    old = old_generator()
    rc0, p0, _m0, _l0 = frozen_build(old, nodes, tempfile.mkdtemp(), probe)
    rc1, p1, _m1, _l1 = frozen_build(C, nodes, tempfile.mkdtemp(), probe)
    rows0 = [l for l in (p0 or '').split('\n') if l.startswith('| `SIDEExplicitFormula.')]
    rows1 = [l for l in (p1 or '').split('\n') if l.startswith('| `SIDEExplicitFormula.')]
    want('(1) the χ list re-emitted from the v0.16 probe under both generators: exit 0 both (read %s, %s)' % (rc0, rc1), rc0 == 0 and rc1 == 0)
    der0 = [l for l in rows0 if '| DERIVES |' in l]
    der1 = [l for l in rows1 if '| DERIVES |' in l]
    want('(2) every DERIVES Correspondence row byte for byte unchanged (%d rows)' % len(der1), der0 == der1 and len(der1) > 0)
    ep = '| `SIDEExplicitFormula.Schema.epstein_not_h2_sign_cfg` | SIDE-explicit-formula | INTERFACES | T2-INTERFACES; premises: hP : EpsteinPremises Z rhs |'
    changed = [(a, b) for a, b in zip(rows0, rows1) if a != b]
    want('(3) the INTERFACES row prints its premise, and no row but an INTERFACES row changed',
         ep in rows1 and len(rows0) == len(rows1) and changed and all('| INTERFACES |' in b for a, b in changed))

    repo = tempfile.mkdtemp()
    run = lambda *a: subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    run('init', '-q')
    run('config', 'user.email', 'test@local')
    run('config', 'user.name', 'test')
    files = {'pos_backtick.md': 'The theorem `detector` is compiled at v0.16.\n',
             'pos_qualified.md': 'Read Schema.detector at its pin.\n'}
    for i, s in enumerate(ENGLISH):
        files['neg_%02d.md' % i] = s + '\n'
    for f, s in files.items():
        io.open(os.path.join(repo, f), 'w', encoding='utf-8', newline='\n').write(s)
    run('add', '.')
    run('commit', '-q', '-m', 'fixture')
    saved = (C.PP, old.PP)
    C.PP = old.PP = repo
    try:
        new_hits = set(C.keystones(['detector']))
        old_hits = set(old.keystones(['detector']))
    finally:
        C.PP, old.PP = saved
    neg = set(f for f in files if f.startswith('neg_'))
    want('(4) a backticked `detector` names the node under the new rule', 'pos_backtick.md' in new_hits)
    want('(5) a qualified Schema.detector names the node under the new rule', 'pos_qualified.md' in new_hits)
    want('(6) the ten English-word sentences name it under the old rule (the control: %d of 10)' % len(neg & old_hits), neg <= old_hits and len(neg) == 10)
    want('(7) and none of the ten under the new rule (read %d)' % len(neg & new_hits), not (neg & new_hits))
    zeta = [n.split(' | ')[0].strip() for n in io.open(os.path.join(ROOT, 'data', 'b592_nodes.txt'), encoding='utf-8')
            if n.strip() and not n.startswith(('#', '@'))]
    zs = [C.short(n) for n in zeta if not n.startswith(('RiemannHypothesis', 'riemannZeta'))]
    want('(8) the ζ list has no plain lower-case name, and its keystone match is the same under both rules',
         not [s for s in zs if re.fullmatch(r'[a-z]+', s)] and C.keystones(zs) == old.keystones(zs))
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
