# -*- coding: utf-8 -*-
"""test_chain_page_b629.py -- THE TEST OF THE KEYSTONE GUARD b629 EXTENDED IN tools/chain_page.py, on the author's answer after
b629's seal (relay data/b629_author_answers.txt, prompt 3).

### On a throwaway git repository built in a temporary directory, the generator as it stood at relay b76ce426 (before the edit)
### and as it stands:
### (1)-(2) THE NEGATIVE CASE 'NB:': PLACE-papers phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md :453 at f610d1f, a nota
###   bene, names the node NB under the old rule (the control) and not under the new.
### (3)-(4) THE NEGATIVE CASE '(BD)': internal/CONVERGENCE.md :35057 at f610d1f, 'Barrier Discovery (BD)', names BD under the old
###   rule (the control) and not under the new.
### (5)-(6) THE POSITIVE CASE: a backticked `NB` and a qualified NymanBeurling.NB each name the node under the new rule.
### (7) A LIST WITH NO UPPER-CASE SHORT NAME builds the same match under both rules (b628's ζ list, against PLACE-papers HEAD).
### (8) b629's ζ list against PLACE-papers HEAD: neither FOUNDATIONS nor CONVERGENCE is named under the new rule.
### Usage: python tools/test_chain_page_b629.py
"""
import io
import os
import subprocess
import sys
import tempfile
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PRE_RELAY = 'b76ce426'
PIN_PP = 'f610d1f'
FOUND = ('phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 453, 'NB')
CONV = ('internal/CONVERGENCE.md', 35057, 'BD')
FOUNDATIONS_AND_CONVERGENCE = (FOUND[0], CONV[0])


def old_generator():
    src = subprocess.run(['git', '-C', ROOT, 'show', '%s:tools/chain_page.py' % PRE_RELAY], capture_output=True).stdout.decode('utf-8')
    m = types.ModuleType('chain_page_before')
    m.__dict__['__file__'] = os.path.join(ROOT, 'tools', 'chain_page.py')
    exec(compile(src, 'chain_page_before', 'exec'), m.__dict__)
    return m


def pp_line(path, n):
    t = subprocess.run(['git', '-C', C.PP, 'show', '%s:%s' % (PIN_PP, path)], capture_output=True).stdout.decode('utf-8', 'replace')
    return t.split('\n')[n - 1]


def short_names(nodes):
    return [C.short(n.split(' | ')[0].strip()) for n in io.open(os.path.join(ROOT, 'data', nodes), encoding='utf-8')
            if n.strip() and not n.startswith(('#', '@'))]


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-110s %s' % (label, 'PASS' if cond else '### FAIL'))

    old = old_generator()
    found, conv = pp_line(FOUND[0], FOUND[1]), pp_line(CONV[0], CONV[1])
    repo = tempfile.mkdtemp()
    run = lambda *a: subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    run('init', '-q')
    run('config', 'user.email', 'test@local')
    run('config', 'user.name', 'test')
    files = {'neg_nb.md': found + '\n', 'neg_bd.md': conv + '\n',
             'pos_backtick.md': 'The statement `NB` is compiled at v0.24.\n', 'pos_qualified.md': 'Read NymanBeurling.NB at its pin.\n'}
    for f, s in files.items():
        io.open(os.path.join(repo, f), 'w', encoding='utf-8', newline='\n').write(s)
    run('add', '.')
    run('commit', '-q', '-m', 'fixture')
    saved = (C.PP, old.PP)
    C.PP = old.PP = repo
    try:
        new_nb, old_nb = set(C.keystones(['NB'])), set(old.keystones(['NB']))
        new_bd, old_bd = set(C.keystones(['BD'])), set(old.keystones(['BD']))
    finally:
        C.PP, old.PP = saved
    want('(1) the control: FOUNDATIONS :453 at %s (%r...) names NB under the old rule' % (PIN_PP, found[:40]), 'neg_nb.md' in old_nb)
    want('(2) and not under the new', 'neg_nb.md' not in new_nb)
    want('(3) the control: CONVERGENCE :35057 at %s (%r) names BD under the old rule' % (PIN_PP, conv.strip()[:40]), 'neg_bd.md' in old_bd)
    want('(4) and not under the new', 'neg_bd.md' not in new_bd)
    want('(5) a backticked `NB` names the node under the new rule', 'pos_backtick.md' in new_nb)
    want('(6) a qualified NymanBeurling.NB names the node under the new rule', 'pos_qualified.md' in new_nb)
    z8 = short_names('b628_nodes_zeta.txt')
    want('(7) b628`s ζ list has no upper-case short name, and its keystone match is the same under both rules (%d files)' % len(C.keystones(z8)),
         not [s for s in z8 if s.isupper() and s.isalpha()] and C.keystones(z8) == old.keystones(z8))
    z9 = C.keystones(short_names('b629_nodes_zeta.txt'))
    want('(8) b629`s ζ list: neither FOUNDATIONS nor CONVERGENCE named under the new rule (%d files)' % len(z9),
         not set(FOUNDATIONS_AND_CONVERGENCE) & set(z9))
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
