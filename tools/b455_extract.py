# -*- coding: utf-8 -*-
"""b455_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE DEPOSIT'S EXHAUSTIVENESS CLAIM.
### ### Addresses and quotations only; no claim is classified, no terminal graded, no line decided here."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
OUT = os.path.join(D, 'b455_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def quote_text(txt, name, needle, label, show=160):
    ls = txt.splitlines()
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, name, needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (name, i, l[:show]))
    return i


def quote(path, needle, label, show=160):
    try:
        txt = io.open(path, encoding='utf-8-sig', errors='replace').read()
    except Exception:
        txt = ''
    return quote_text(txt, os.path.basename(path), needle, label, show)


def main():
    rec('=' * 100)
    rec('b455 -- THE SURVEY. ### THE DEPOSIT`S EXHAUSTIVENESS CLAIM READ AGAINST ITS OWN ROUTE TERMINAL.')
    rec('=' * 100)
    rec('')
    rec('(P1) WHAT b454 BANKED.')
    ej = json.load(io.open(os.path.join(D, 'b454_enumera.json'), encoding='utf-8'))
    rec('      b454 second figure : %s %s:%s -> %s' % (ej['second']['name'], ej['second']['path'], ej['second']['line'], ej['second']['grade']))
    rec('      b454 nearest by rule : %s' % ['%s %s:%d -> %s' % (h['kernel'], h['path'], h['line'], h['graded']['grade']) for h in ej['nearest']])
    fj = json.load(io.open(os.path.join(D, 'b454_findings.json'), encoding='utf-8'))
    rec('      b454 counts : %s ; defect : %s:%d' % (fj['counts'], fj['defect']['ledger'].split('/')[-1], fj['defect']['line']))
    rec('')
    rec('(P2) THE DEPOSITED PIN.')
    rec('      SIDE-kernel tag v1.5 peels to : %s ; HEAD : %s' % (git(KER, 'rev-parse', '--short', 'v1.5^{commit}').strip(), git(KER, 'rev-parse', '--short', 'HEAD').strip()))
    for f in ('Bridge/TheBridgeComplete.lean', 'Kernel/Layer1.lean'):
        same = subprocess.run(['git', '-C', KER, 'diff', '--quiet', 'v1.5', 'HEAD', '--', f]).returncode == 0
        rec('      %s identical at v1.5 and HEAD : %s' % (f, same))
    rec('      Kernel/Layer1.lean identical at v1.2 and v1.5 : %s' % (subprocess.run(['git', '-C', KER, 'diff', '--quiet', 'v1.2', 'v1.5', '--', 'Kernel/Layer1.lean']).returncode == 0))
    quote(os.path.join(PP, 'REGISTRY.md'), '| ### **`SIDE-kernel`** | ### **`v1.5` = `0e5233f`** — the deposited wave; concept DOI `10.5281/zenodo.19674312`, version DOI `10.5281/zenodo.21520474`', 'P2 REGISTRY pin row', 120)
    rec('')
    rec('(P3) THE ZENODO DESCRIPTIONS AS THE RECORD HOLDS THEM.')
    fr = json.load(io.open(os.path.join(D, 'b359_fetch_F2.json'), encoding='utf-8'))
    rec('      b359_fetch_F2.json : doi %s ; version %s ; title %r ; description %d chars ; banked by relay commit %s'
        % (fr['doi'], fr['metadata']['version'], fr['metadata']['title'], len(fr['metadata']['description']), git(ROOT, 'log', '--format=%h %ad', '-1', '--', 'data/b359_fetch_F2.json').strip()))
    quote_text(fr['metadata']['description'], 'b359_fetch_F2.json:description', 'Proved and machine-checked around the argument: the exhaustiveness of the seven-class catalogue over the places of', 'P3 monograph record paragraph', 120)
    zl = io.open(os.path.join(D, 'zenodo_fetch_2026-08-10.jsonl'), encoding='utf-8').read().splitlines()
    for i, l in enumerate(zl):
        try:
            j = json.loads(l)
        except Exception:
            continue
        if j.get('doi') == '10.5281/zenodo.21520474':
            rec('      zenodo_fetch_2026-08-10.jsonl:%d : doi %s version %s ; keys %s ; description held : %s' % (i + 1, j['doi'], j.get('version'), sorted(j.keys()), 'description' in json.dumps(j)))
    zj = git(KER, 'show', 'v1.5:.zenodo.json')
    quote_text(zj, 'SIDE-kernel@v1.5:.zenodo.json', 'The kernel proves that no off-line zero exists by exhaustively excluding every mechanism class derivable from the specification.', 'P3 kernel .zenodo.json at the tag', 120)
    rec('')
    rec('(P4) THE FRONT DOOR, THE CONCORDANCE, THE KERNEL README AT THE TAG.')
    quote(os.path.join(PP, 'README.md'), '**Kernel:** [SIDE-kernel](https://github.com/psinary-sketch/SIDE-kernel) — cited by named terminal, not by count.', 'P4 PLACE-papers README kernel line', 100)
    DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
    quote(DEP, '## 25.8 Kernel Concordance', 'P4 deposited §25.8')
    quote(DEP, '| Route 1 — structural exhaustiveness, unconditional in Lean | `structural_exhaustiveness_proved` |', 'P4 §25.8 Route 1 row')
    quote(DEP, '**On Route 1.** `structural_exhaustiveness_proved` is the conjunction', 'P4 §25.8 On Route 1', 100)
    quote(DEP, '# Chapter 26: What Compiles and What Doesn', 'P4 §25.8 ends')
    quote(DEP, '**v5.10.2, 2026-07-24**', 'P4 deposited copy version line')
    fnames = [f.get('key') for f in fr.get('files', [])]
    rec('      the v1.1.2 record`s files : %s' % fnames)
    kr = git(KER, 'show', 'v1.5:README.md')
    quote_text(kr, 'SIDE-kernel@v1.5:README.md', '- `structural_exhaustiveness_proved` in `Bridge/TheBridgeComplete.lean` — the seven mechanism classes are exhaustive', 'P4 kernel README at tag', 120)
    rec('')
    rec('(P5) THE PRINTED PROFILES, BY PIN.')
    quote_text(git(KER, 'show', 'v1.5:DEPOSIT_v1_2_NOTES.md'), 'SIDE-kernel@v1.5:DEPOSIT_v1_2_NOTES.md', "'structural_exhaustiveness_proved' depends on axioms: [propext, Classical.choice, Quot.sound]", 'P5 route 1 printed (v1.2 notes)')
    quote_text(git(KER, 'show', 'v1.5:DEPOSIT_v1_2_NOTES.md'), 'SIDE-kernel@v1.5:DEPOSIT_v1_2_NOTES.md', '## ', 'P5 notes first heading', 100)
    quote(os.path.join(ROOT, 'reports', '2026-07-11-keystone-review-2.md'), 'techne_kernel.SIDE_exclusion                                     does not depend on any axioms', 'P5 SIDE_exclusion printed')
    quote(os.path.join(ROOT, 'reports', '2026-07-11-keystone-review-2.md'), 'Kernels: SIDE-kernel `ce5d7bd` (v1.2 = `b1407b2`)', 'P5 that print`s pin', 100)
    rec('')
    rec('(P6) THE GRADES AND THE DISPOSITION FORMS THE RECORD KNOWS.')
    quote(os.path.join(PP, 'README.md'), '### The four grades', 'P6 grades')
    quote(os.path.join(PP, 'ERRATA.md'), '## THE PARTITION — filed 2026-09-06 (b337, leg 2 of the sortie)', 'P6 ERRATA partition')
    quote(os.path.join(PP, 'ERRATA.md'), '## E-2026-07-12-1 — "zero custom axioms" does not hold, as deposited, of Route 1 and the formation certificates', 'P6 ERRATA deposit-facing entry form')
    quote(os.path.join(PP, 'ERRATA.md'), '## E-2026-08-24-2 — The deposited record TITLES carry a grammar the corpus', 'P6 ERRATA routed platform-metadata entry')
    quote(os.path.join(PP, 'REGISTRY.md'), '> ### **THE CURRENCY OBLIGATION.** *Every deposited record **either** sits at a version a citable claim uses, **or** carries a note saying it is historical.', 'P6 (R20) currency obligation', 100)
    rec('')
    rec('(P7) THE ARCHIVE LINE b454 PRINTED, AND THE SPECIFICATION IT SUMMARISES.')
    quote(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'), '**`T1`–`T10` assembled**, each cited / compiled / measured-at-bank', 'P7 the line')
    quote(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'), '### **`THE_TECHNIQUE_SPECIFICATION` `v0.1`** (2026-08-11;', 'P7 the line`s heading')
    quote(os.path.join(PP, 'phase2', 'method', 'THE_TECHNIQUE_SPECIFICATION.md'), '| **T3** | **Consume the Euler product essentially.**', 'P7 the spec`s T3 row', 120)
    quote(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md'), 'Face E / keyhole (i)+(iv) as used by the `S`-table; the `T3` Tier-1 scope', 'P7 the census finding')
    rec('')
    rec('(P8) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '455'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'STARTS AT|runs through|THE CURRENT SPAN|UNPARSED|NOTHING WAS WRITTEN', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
