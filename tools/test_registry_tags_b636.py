# -*- coding: utf-8 -*-
"""test_registry_tags_b636.py -- THE TEST OF tools/b635_record.py's b636 EDIT, under (R246)(2)(iii): the deposit bank's tag matcher
(registry_tags) reads the REGISTRY's tag form alone and nothing in prose, REGISTRY :705's sentence its negative case.

### REGISTRY.md read by git at PLACE-papers 07f4c43 (b635's last head, the bank's own REGISTRY); nothing is written.
###   (1) the negative case: :705's sentence "`ab6f269` prices the `v0.5` matching-certificate target", on its SIDE-window line, gives no
###       (SIDE-window, v0.5) pair, while the same line's tags in the tag form are read (v0.1.0, v0.2.0, v0.3.0, v0.4.0);
###   (2) the REGISTRY at the pin gives exactly the 18 pairs b635's deposit bank resolved at the remote (data/b635_deposit_items.json);
###   (3) the control: b635's matcher (any backticked version on a one-kernel line) gives those 18 and (SIDE-window, v0.5), 19;
###   (4) each tag form, planted on a one-kernel line, is read: `vX` = `sha`; = commit `sha`; = peeled `sha`; tag `vX`; | `vX` |;
###       `vX`, HEAD `sha`; `vX`/`sha`; with emphasis marks around;
###   (5) prose, planted, is not read: at `vX` with; prices the `vX` target; `vX` Lemma A; a version bound to a non-commit word.
### Usage: python tools/test_registry_tags_b636.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b635_record as R   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = chr(10)
PP, PIN = 'D:/MY-DOwnloads/PLACE-papers', '07f4c43'
SENTENCE = '`ab6f269` prices the `v0.5` matching-certificate target'


def old_tags(t):
    """### b635's matcher, as committed at relay be879893 (tools/b635_record.py :553-:564) -- the control."""
    pairs = set()
    for l in t.split(NL):
        ks = set(re.findall(r'\b(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)\b', l))
        tags = set(re.findall(r'`(v\d+(?:\.\d+){1,2})`', l))
        if len(ks) == 1 and tags:
            k = ks.pop()
            for tg in tags:
                pairs.add((k, tg))
    return sorted(pairs)


def main():
    reg = subprocess.run(['git', '-C', PP, 'show', '%s:REGISTRY.md' % PIN], capture_output=True).stdout.decode('utf-8').replace(chr(13), '')
    l705 = reg.split(NL)[704]
    bank = json.load(open(os.path.join(ROOT, 'data', 'b635_deposit_items.json'), encoding='utf-8'))
    good = sorted((x['kernel'], x['tag']) for x in bank['tags'] if x['ok'])
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-110s %s' % (label, 'PASS' if cond else '### FAIL'))

    p705 = R.registry_tags(l705)
    want('(1) :705 carries the sentence (%s) ; its pairs %s' % (SENTENCE in l705, [t for _k, t in p705]),
         SENTENCE in l705 and ('SIDE-window', 'v0.5') not in p705 and sorted(t for _k, t in p705) == ['v0.1.0', 'v0.2.0', 'v0.3.0', 'v0.4.0'])
    new = R.registry_tags(reg)
    want('(2) the REGISTRY at %s: %d pairs ; equal to the bank`s %d resolving pairs: %s' % (PIN, len(new), len(good), new == good),
         len(good) == 18 and new == good)
    old = old_tags(reg)
    want('(3) control, b635`s matcher: %d pairs, the extra %s' % (len(old), sorted(set(old) - set(good))),
         len(old) == 19 and sorted(set(old) - set(good)) == [('SIDE-window', 'v0.5')])
    forms = ['| `SIDE-a` | `v1.0` = `abc1234` |', '`SIDE-a` tag **`v1.0`** = commit `abc1234def`', '`SIDE-a`, tag `v1.0` = peeled `abc1234`',
             '`SIDE-a` at tag `v1.0` (tag object)', '| `SIDE-a` | `v1.0` | HEAD', '`SIDE-a` **`v1.0`, HEAD `abc1234`, branch',
             '`SIDE-a` works at `v1.0`/`abc1234`.', '`SIDE-a` | ### **`v1.0` = `abc1234`** —']
    got4 = [(f, R.registry_tags(f)) for f in forms]
    want('(4) the tag forms read: %d of %d' % (sum(1 for _f, g in got4 if g == [('SIDE-a', 'v1.0')]), len(forms)),
         all(g == [('SIDE-a', 'v1.0')] for _f, g in got4))
    prose = ['`SIDE-a` names terminals at `v1.0` with the ERRATA caveat', '`SIDE-a`: `abc1234` prices the `v1.0` target',
             '`SIDE-a` **`v1.0` Lemma A + the prime', '`SIDE-a` nothing in `v1.0` is a statement', '`SIDE-a` `v1.0` = `main`']
    got5 = [(f, R.registry_tags(f)) for f in prose]
    want('(5) prose read as a tag: %s' % [f for f, g in got5 if g], not any(g for _f, g in got5))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
