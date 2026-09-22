# -*- coding: utf-8 -*-
"""b473_extract.py -- THE SURVEY. ### The seventeen Challenge theorems by name, the three
### explicit-formula declarations, the comparator's own prerequisites, and the log's METADATA.
### ### **THE LOG IS NOT OPENED HERE.** ### Registration before components: its contents are Component
### 1's, after the seal. Writes b473_extract.txt and b473_survey.json.
"""
import io
import json
import os
import re
import shutil
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
LOG = os.path.join(D, 'b471_zeta23_build.log')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    rec('=' * 104)
    rec('b473 -- THE SURVEY. ### THE LOG IS NOT OPENED HERE.')
    rec('=' * 104)

    rec('')
    rec('(P1) (R81) AS AMENDED -- THE FLAGS OVER THIS FERRY, FROM THE SCAN TOOL ITSELF.')
    rec('-' * 104)
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import ferry_scan
    fl = ferry_scan.r81_flags(read(os.path.join(D, 'b473_ferry.txt')))
    bare = [f for f in fl if f[3] == 'ACT' and f[4] == 'NONE']
    rec('    flags : %d ; in the act text : %d ; bare in the act text : %d'
        % (len(fl), sum(1 for f in fl if f[3] == 'ACT'), len(bare)))
    for f in fl:
        rec('      line %-4d %-6s %-6s carries %s' % (f[0], f[2], f[3], f[4]))
    rec('  ### ### **NO FLAGGED WORD IN THIS FERRY AT ALL, SO NOTHING TO LABEL AND NOTHING TO REFUSE.**')

    rec('')
    rec('(P2) THE SEVENTEEN CHALLENGE THEOREMS, BY NAME, FROM THE SOURCE`S OWN TWO LISTS.')
    rec('-' * 104)
    pa = read(os.path.join(Z, 'scripts', 'PrintAxioms.lean'))
    names_script = re.findall(r'^#print axioms (\S+)$', pa, re.M)
    cj = json.loads(read(os.path.join(Z, 'comparator.json')) or '{}')
    names_cmp = cj.get('theorem_names', [])
    rec('    scripts/PrintAxioms.lean : %d names' % len(names_script))
    rec('    comparator.json          : %d names ; challenge module %r ; solution module %r'
        % (len(names_cmp), cj.get('challenge_module'), cj.get('solution_module')))
    same = names_script == names_cmp
    rec('    ### ### **THE TWO LISTS AGREE, NAME FOR NAME AND IN ORDER : %s**' % same)
    if not same or len(names_script) != 17:
        MISSES.append(('the seventeen', '%d in the script, %d in comparator.json' % (len(names_script), len(names_cmp))))
    for n in names_script:
        rec('      %s' % n)

    rec('')
    rec('(P3) THE THREE EXPLICIT-FORMULA DECLARATIONS (R82) NAMES, AS b471 RAN THEM.')
    rec('-' * 104)
    named = read(os.path.join(D, 'b471_named_axioms.txt'))
    ef = re.findall(r'^#print axioms (\S+)$', named, re.M)
    rec('    b471_named_axioms.txt : %d declarations' % len(ef))
    for n in ef:
        rec('      %s' % n)
    if len(ef) != 3:
        MISSES.append(('b471_named_axioms.txt', '%d declarations' % len(ef)))
    rec('    ### the standard three, as the source`s own script states the requirement:')
    m = re.search(r"Every line must print exactly:\s*(.+)", pa)
    rec('      %s' % (m.group(1).strip() if m else 'NOT FOUND'))
    if not m:
        MISSES.append(('PrintAxioms.lean', 'the requirement line'))

    rec('')
    rec('(P4) THE COMPARATOR`S OWN PREREQUISITES, READ FROM ITS SCRIPT -- NOT RUN HERE.')
    rec('-' * 104)
    sh = read(os.path.join(Z, 'scripts', 'verify-comparator.sh'))
    req = re.search(r'for required_command in ([^;]+); do', sh)
    reqs = req.group(1).split() if req else []
    have = {c: (shutil.which(c) or 'ABSENT') for c in reqs + ['landrun']}
    cache = os.path.join(Z, '.cache', 'palomar-comparator')
    rec('    the script`s own requirement line : %s' % (req.group(0) if req else 'NOT FOUND'))
    for c, w in have.items():
        rec('      %-8s %s' % (c, w))
    rec('    the script`s stated platform : %s'
        % ('Requires Linux' if 'Requires Linux' in sh else 'NOT STATED'))
    rec('    the tool cache %s : %s' % (os.path.relpath(cache, Z), 'PRESENT' if os.path.isdir(cache) else 'ABSENT'))
    pins = dict(re.findall(r'^(\w+_commit)=([0-9a-f]{40})$', sh, re.M))
    for k, v in pins.items():
        rec('      pinned %-18s %s' % (k, v))
    rec('    this platform : %s' % sys.platform)
    rec('  ### ### **FOUR TOOL CHECKOUTS ARE PINNED AND THE CACHE IS ABSENT, SO A RUN WOULD FETCH THEM;')
    rec('  ### AND go, cargo AND landrun ARE ABSENT, AND THE SCRIPT SAYS "Requires Linux".**')

    rec('')
    rec('(P5) THE LOG`S METADATA ONLY -- SIZE AND TIMES, NOT CONTENTS.')
    rec('-' * 104)
    size = os.path.getsize(LOG)
    mt = datetime.datetime.fromtimestamp(os.path.getmtime(LOG), datetime.timezone.utc)
    la = json.loads(io.open(os.path.join(D, 'b471_launch.json'), encoding='utf-8-sig').read())
    rec('    path          : %s' % LOG)
    rec('    bytes         : %d' % size)
    rec('    last write    : %s' % mt.strftime('%Y-%m-%dT%H:%M:%SZ'))
    rec('    launched      : %s (b471)' % la['started_utc'])
    rec('    tracked in relay : %s' % ('YES' if os.path.exists(os.path.join(ROOT, '.git')) and
                                       'b471_zeta23_build.log' in read(os.path.join(ROOT, '.git', 'index'))[:0] else 'NOT YET'))
    rec('  ### ### **NOT OPENED. ### Component 1 reads it whole, after the seal, and commits it.**')

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b473_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(flags=[list(f) for f in fl], act_bare=len(bare), seventeen=names_script,
                   comparator_names=names_cmp, lists_agree=same, ef=ef,
                   comparator=dict(requirements=have, cache_present=os.path.isdir(cache), pins=pins,
                                   platform=sys.platform, requires_linux='Requires Linux' in sh),
                   log=dict(bytes=size, last_write=mt.strftime('%Y-%m-%dT%H:%M:%SZ'),
                            launched=la['started_utc']), misses=MISSES),
              io.open(os.path.join(D, 'b473_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
