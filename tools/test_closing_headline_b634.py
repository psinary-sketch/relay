# -*- coding: utf-8 -*-
"""test_closing_headline_b634.py -- THE TEST OF THE CLOSING'S HEAD LINE, under (R244)(3).

### The closing tool's `head_line` reads the act's banks; here they are PLANTED in a fresh temporary directory, so no bank of any act
### is read or written. The tool is imported from the path its first argument names (tools/b634_closing.py when none is given).
### (1) the full set: relay and PLACE-papers read back, the suite's post-push count, the root, two prompts, three defects -- the line exact;
### (2) a kernel tag pushed: its repository, tag and commit enter between PLACE-papers and the suite;
### (3) no prompt and no defect: "0 prompts answered; 0 defects";
### (4) one prompt and one defect: the singular;
### (5) the post-push suite bank absent: the suite prints NOT READ and the line is still written.
### Usage: python tools/test_closing_headline_b634.py [closing-tool]
"""
import importlib.util
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RELAY_SHA = 'abcdef0123456789abcdef0123456789abcdef01'
PP_SHA = '1234567fedcba9876543210fedcba9876543210f'
KER_SHA = '89abcde0123456789abcdef0123456789abcdef0'
ROOT_HEX = 'f00dfeed' * 8


def load(path):
    spec = importlib.util.spec_from_file_location('closing_under_test', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def plant(d, act, prompts=2, defects=3, kernel=False, suite=True):
    def w(n, t):
        open(os.path.join(d, n), 'w', encoding='utf-8', newline=NL).write(t)
    w('%s_relay_push_out.txt' % act, 'push_gated: repo D:/relay ; branch push-x\npush_gated: main read back at the remote: %s\n' % RELAY_SHA)
    w('%s_pp_push_out.txt' % act, 'push_gated: main read back at the remote: %s\n' % PP_SHA)
    if kernel:
        w('%s_kernel_push_out.txt' % act, 'push_gated: repo D:/SIDE-planted-kernel ; branch push-x ; tip %s ; checkout before main\n'
                                          'push_gated: main read back at the remote: %s\n'
                                          'push_gated: tag v9.9 made at the read-back %s (0000)\n' % (KER_SHA, KER_SHA, KER_SHA))
    if suite:
        w('%s_checks_postpush.txt' % act, '  ### ### **ARMS RUN : 79. ### LIVE PASSING : 78. ### LIVE FAILING : 1 [x].**\n')
    w('%s_act_root.json' % act, json.dumps(dict(root=ROOT_HEX)))
    w('%s_author_answers.txt' % act, ''.join('### PROMPT %d (x): y\n' % (i + 1) for i in range(prompts)))
    w('%s_defects.json' % act, json.dumps(dict(defects=['(%s) x' % chr(97 + i) for i in range(defects)])))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'tools', 'b634_closing.py')
    C = load(path)
    res = []

    def want(label, cond, got):
        res.append(bool(cond))
        print('  %-90s %s' % (label, 'PASS' if cond else '### FAIL'))
        if not cond:
            print('      got: %s' % got)

    act = 'b999'
    d1 = tempfile.mkdtemp()
    plant(d1, act)
    l1 = C.head_line(d1, act)
    want('(1) the full set: the line exact', l1 == 'b999 closed: relay abcdef01, PLACE-papers 1234567; suite 78 of 79; root f00dfeedf00dfeed…; '
                                                  '2 prompts answered; 3 defects', l1)
    d2 = tempfile.mkdtemp()
    plant(d2, act, kernel=True)
    l2 = C.head_line(d2, act)
    want('(2) a kernel tag pushed: its repository, tag and commit after PLACE-papers', ', SIDE-planted-kernel v9.9 = 89abcde; suite 78 of 79' in l2, l2)
    d3 = tempfile.mkdtemp()
    plant(d3, act, prompts=0, defects=0)
    l3 = C.head_line(d3, act)
    want('(3) no prompt and no defect', l3.endswith('; 0 prompts answered; 0 defects'), l3)
    d4 = tempfile.mkdtemp()
    plant(d4, act, prompts=1, defects=1)
    l4 = C.head_line(d4, act)
    want('(4) one prompt and one defect: the singular', l4.endswith('; 1 prompt answered; 1 defect'), l4)
    d5 = tempfile.mkdtemp()
    plant(d5, act, suite=False)
    l5 = C.head_line(d5, act)
    want('(5) the post-push suite bank absent: NOT READ printed, the line still written', 'suite ### NOT READ;' in l5 and l5.startswith('b999 closed: '), l5)
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
