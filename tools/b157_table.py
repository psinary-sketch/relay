# -*- coding: utf-8 -*-
"""b157 -- THE ORIENTATION TABLE. Assembled from the live census, the
comment-aware source scan, and REGISTRY's own rows. ### READ-ONLY.

### THE READ-DEPTH COLUMN IS THE HONEST PART. 2005 theorem/lemma declarations
### stand across 43 repositories; a statement-level read-and-grade of all of them
### is not one act's work. This act read a NAMED SUBSET at content and says which,
### so a later act knows exactly what was and was not read.
### AN UNSTATED TRUNCATION WOULD READ AS COVERAGE.
"""
import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.join('D:', os.sep)
REG = r"D:\MY-DOwnloads\PLACE-papers\REGISTRY.md"
BLOCK = re.compile(r'/-.*?-/', re.S)
TOK = re.compile(r'(?<![A-Za-z0-9_])sorry(?![A-Za-z0-9_])')
TH = re.compile(r'(?m)^\s*(theorem|lemma)\s+[A-Za-z_]')

# the repositories read AT CONTENT this act, with the one-line result of the read
DEEP = {
    'SIDE-effects': 'RETIREMENT LEDGER read; 18 of 20 claimed exports ABSENT; 3 open-conjecture sorries',
    'SIDE-bsd-formation-transfer': 'Bool-set-true + decide stubs read at content',
    'SIDE-bsd-multiplicity': 'Bool-set-true + decide stubs read at content',
    'SIDE-global-section': 'AXIOM_PRINTS 281/281 read; zero apparent sorry',
    'SIDE-kernel': 'lakefile targets read; all 32 apparent sorries in unbuilt legacy/',
    'SIDE-substrate-cluster': 'SteaneLabeling terminals read (the repointed citation)',
}


def strip(src):
    src = BLOCK.sub(lambda m: '\n' * m.group(0).count('\n'), src)
    return [l[:l.find('--')] if '--' in l else l for l in src.split('\n')]


def g(repo, *a):
    p = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=120)
    return (p.stdout or '').strip() if p.returncode == 0 else None


def main():
    names = sorted(d for d in os.listdir(ROOT)
                   if d.startswith('SIDE-') and os.path.isdir(os.path.join(ROOT, d, '.git')))
    reg = io.open(REG, encoding='utf-8').read()

    rows = []
    for n in names:
        r = os.path.join(ROOT, n)
        th = so = 0
        for dp, dn, fn in os.walk(r):
            dn[:] = [d for d in dn if d not in ('.git', '.lake', 'build')]
            for f in fn:
                if not f.endswith('.lean'):
                    continue
                s = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
                th += len(TH.findall(s))
                so += sum(1 for l in strip(s) if TOK.search(l))
        tag = g(r, 'describe', '--tags', '--abbrev=0')
        peeled = g(r, 'rev-list', '-n', '1', tag) if tag else None
        head = g(r, 'rev-parse', 'HEAD')
        # REGISTRY mentions, counted on the whole-word repo name
        cites = len(re.findall(re.escape(n) + r'(?![a-z0-9-])', reg))
        rows.append(dict(repo=n, th=th, so=so, tag=tag, peeled=peeled, head=head, cites=cites))

    print("| repo | citable tag (peeled) | HEAD | thm decls | apparent sorry | REGISTRY refs | citation status | read depth, this act |")
    print("|:--|:--|:--|--:|--:|--:|:--|:--|")
    for r in rows:
        tag = ('`%s` = `%s`' % (r['tag'], (r['peeled'] or '')[:7])) if r['tag'] else '### **none**'
        status = ('deposit-grade tag available' if r['tag'] else '### **work-grade HEAD only**')
        if r['cites'] == 0:
            status += ' · ### **cited by no REGISTRY row**'
        depth = DEEP.get(r['repo'])
        depth = ('### **READ AT CONTENT** — ' + depth) if depth else 'enumerated only — **NOT read this act**'
        so = ('### **%d**' % r['so']) if r['so'] else '0'
        print("| `%s` | %s | `%s` | %d | %s | %d | %s | %s |"
              % (r['repo'], tag, (r['head'] or '')[:7], r['th'], so, r['cites'], status, depth))

    tot_t = sum(r['th'] for r in rows)
    tot_s = sum(r['so'] for r in rows)
    deep = sum(1 for r in rows if r['repo'] in DEEP)
    notag = sum(1 for r in rows if not r['tag'])
    nocite = sum(1 for r in rows if r['cites'] == 0)
    print("\n**TOTALS — %d repositories · %d theorem/lemma declarations · %d apparent sorry tokens "
          "outside comments · %d untagged · %d cited by no REGISTRY row.**"
          % (len(rows), tot_t, tot_s, notag, nocite))
    print("### **READ DEPTH: %d of %d repositories were read AT CONTENT this act; the other %d are "
          "ENUMERATED ONLY.** The split is stated because an unstated truncation would read as coverage."
          % (deep, len(rows), len(rows) - deep))


if __name__ == '__main__':
    main()
