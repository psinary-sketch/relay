# -*- coding: utf-8 -*-
"""b457_extract.py -- THE SURVEY'S RECORD OF THE PRE-FACE READS FOR THE PROFILE RUN AT THE TAG, (R68), AND THE SENTENCE GATE.
### ### Addresses, pins and quotations only; nothing is built, run, counted or written here."""
import hashlib
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
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
OUT = os.path.join(D, 'b457_extract.txt')
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def quote_text(txt, name, needle, label, show=140):
    hit = [(i + 1, l.strip()) for i, l in enumerate(txt.replace(chr(13), '').split(chr(10))) if needle in l]
    if not hit:
        MISSES.append((label, name, needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    i, l = hit[0]
    rec('      %s:%d | %s' % (name, i, l[:show]))
    return i


def quote(path, needle, label, show=140):
    try:
        txt = io.open(path, encoding='utf-8-sig', errors='replace').read()
    except Exception:
        txt = ''
    return quote_text(txt, os.path.basename(path), needle, label, show)


def main():
    rec('=' * 100)
    rec('b457 -- THE SURVEY. ### THE PROFILES PRINTED AT THE TAG, AND THE SENTENCE GATE PRICED.')
    rec('=' * 100)
    rec('')
    rec('(P1) THE TAG AND ITS TOOLCHAIN, READ WITHOUT BUILDING.')
    rec('      tag object v1.5 : %s ; peels to : %s ; type : %s' % (git(KER, 'rev-parse', 'v1.5').strip(), git(KER, 'rev-parse', 'v1.5^{commit}').strip(), git(KER, 'cat-file', '-t', 'v1.5').strip()))
    rec('      lean-toolchain at v1.5 : %s ; at HEAD : %s' % (git(KER, 'show', 'v1.5:lean-toolchain').strip(), git(KER, 'show', 'HEAD:lean-toolchain').strip()))
    same = subprocess.run(['git', '-C', KER, 'diff', '--quiet', 'v1.5', 'HEAD', '--', 'lake-manifest.json', 'lakefile.lean', 'lean-toolchain']).returncode == 0
    rec('      lake-manifest.json, lakefile.lean, lean-toolchain identical at v1.5 and HEAD : %s' % same)
    man = json.loads(git(KER, 'show', 'v1.5:lake-manifest.json'))
    for p in man['packages']:
        rv = git(os.path.join(KER, '.lake', 'packages', p['name']), 'rev-parse', 'HEAD').strip()
        dirty = len(git(os.path.join(KER, '.lake', 'packages', p['name']), 'status', '--porcelain', '--untracked-files=no').splitlines())
        rec('      package %-17s manifest %s ; local cache %s ; match %s ; tracked-dirty %d' % (p['name'], p['rev'][:10], rv[:10], rv == p['rev'], dirty))
    w = subprocess.run(['elan', 'which', 'lean'], cwd=KER, capture_output=True, text=True).stdout.strip()
    rec('      elan resolves the tag`s toolchain to : %s ; installed : %s' % (w, os.path.exists(w)))
    rec('')
    rec('(P2) THE ROUTE TERMINALS THE DEPOSIT NAMES, AND THE TAG`S OWN CHECK SCRIPT.')
    fr = json.load(io.open(os.path.join(D, 'b359_fetch_F2.json'), encoding='utf-8'))
    quote_text(fr['metadata']['description'], 'b359_fetch_F2.json:description', 'at the named route theorems (structural_exhaustiveness_proved; SpectralCannonFull.spectral_cannon; ConservationBridge.riemann_hypothesis', 'P2 the record names the route theorems', 60)
    quote_text(fr['metadata']['description'], 'b359_fetch_F2.json:description', 'All route terminals report {propext, Classical.choice, Quot.sound}.', 'P2 the deposited sentence', 60)
    ck = git(KER, 'show', 'v1.5:AxiomCheck_v1_3.lean')
    for n in ('import Bridge.TheBridgeComplete', 'import Bridge.ConservationBridge', 'import Kernel.SpectralCannonFull',
              '#print axioms structural_exhaustiveness_proved', '#print axioms SpectralCannonFull.spectral_cannon', '#print axioms ConservationBridge.riemann_hypothesis'):
        quote_text(ck, 'SIDE-kernel@v1.5:AxiomCheck_v1_3.lean', n, 'P2 script line')
    quote(os.path.join(PP, 'README.md'), 'route terminals re-profiled clean at the v1.5 enactment', 'P2 front door`s sentence', 60)
    quote(os.path.join(PP, 'README.md'), '(R20) note, b456, 2026-09-14:', 'P2 b456`s note line', 60)
    quote(os.path.join(D, 'b456_components.txt'), '### ### **VERDICT : ABSENT**', 'P2 b456 verdict')
    rec('')
    rec('(P3) THE CELLS (R68) NAMES.')
    R = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
    for n in ('| the 𝔽_q anatomy (§6) | same branch |', '| the realization ledger (§6) | same branch |', '| the finite-range inhabitant (§6) | same branch |', '| the eight further rows above | same branch |'):
        quote(R, n, 'P3 RES cell line', 60)
    rec('      "### **HELD-BRANCH**" occurrences in THE_RESIDUE_OF_RH.md : %d' % io.open(R, encoding='utf-8').read().count('### **HELD-BRANCH**'))
    quote(R, '<!-- b456 CURRENCY ANNOTATION, 2026-09-14 -->', 'P3 b456`s currency annotation form')
    rec('')
    rec('(P4) THE DEPOSITED LINE`S SURFACES, FOR THE GATE`S PRICE.')
    for f in fr['files']:
        p = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', f['key'])
        m = 'md5:' + hashlib.md5(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
        rec('      record v1.1.2 file %-30s local copy matches the record`s checksum : %s' % (f['key'], m == f['checksum']))
    rec('      SIDE-kernel tag v1.5 README.md present : %s ; .zenodo.json present : %s' % (bool(git(KER, 'show', 'v1.5:README.md')), bool(git(KER, 'show', 'v1.5:.zenodo.json'))))
    rec('      SIDE-lv-conservation tag v0.10.0 peels to : %s ; README.md present : %s' % (git(LV, 'rev-parse', '--short', 'v0.10.0^{commit}').strip(), bool(git(LV, 'show', 'v0.10.0:README.md'))))
    quote_text(fr['metadata']['description'], 'b359_fetch_F2.json:description', 'SIDE-lv-conservation v0.10.0, DOI 10.5281/zenodo.21539068', 'P4 the paired deposit', 60)
    quote(os.path.join(D, 'b455_components.txt'), '| C2 *"Proved and machine-checked around the argument', 'P4 b455`s graded row, one measured basis', 60)
    quote(os.path.join(D, 'b455_components.txt'), 'yield `exhaust` 20 ; yield the terminal`s name 5 ; items 20', 'P4 b455`s read size', 60)
    rec('')
    rec('(P5) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '457'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|UNPARSED', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 100)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
