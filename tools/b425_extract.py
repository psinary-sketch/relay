# -*- coding: utf-8 -*-
"""b425_extract.py -- THE SURVEY FOR b425, THE SORTIE'S THIRD LEG: THE FALSIFIER READ.
### **THE CORPUS ONLY. NOTHING IS FETCHED BY THIS TOOL: THE SOURCE IS READ AFTER THE LOCK, AS b362 READ ITS OWN.
### EVERY READ ANCHORED IN THE MARKUP-FOLDED TEXT, EVERY MISS COUNTED, EVERY PIN PRINTED.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
OUT = os.path.join(D, 'b425_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]

DOCS = [
    ('FANO', 'phase2/physics/FANO_DERIVATION_OF_LAMBDA.md'),
    ('STORMER', 'phase2/physics/STORMER.md'),
    ('FD', 'phase2/physics-speculative/FORMATION_DISTANCE.md'),
    ('FDDV', 'phase1.5/spectral/FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md'),
    ('REG', 'REGISTRY.md'),
    ('TRAILS', 'OPEN_TRAILS.md'),
]
P = {k: os.path.join(PP, *rel.split('/')) for k, rel in DOCS}


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def git(*args):
    return subprocess.run(['git', '-C', PP] + list(args), capture_output=True, text=True).stdout.strip()


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')).strip()


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def quote(label, key, start, end=None, width=96, cap=600):
    READS[0] += 1
    raw = read(P[key])
    src, s0 = fold(raw), fold(start)
    i = src.find(s0)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-44s ### **MISS** -- anchor absent' % label)
        return ''
    e0 = fold(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    seg = src[i:j + len(e0)] if j > i else src[i:i + cap]
    k = raw.find(start[:40])
    say('  %-44s %s%s' % (label, dict(DOCS)[key], (' line %d' % (raw[:k].count(NL) + 1)) if k >= 0 else ''))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


rule('=')
say('b425_extract.py -- THE SURVEY: THE FALSIFIER READ, THE SORTIE`S THIRD LEG. ### THE CORPUS ONLY.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: b424`S ROW BY ITS MARKER.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m = [int(x.group(1)) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*THE WITNESS ARC AT SITE \(i\)", corr)]
say('  row of b424`s marker : %s' % m)
if m != [273]:
    MISS.append('b424`s row is not 273 by its marker')

rule()
say('### READ 1 -- THE LANE`S DOCUMENTS AND THEIR PINS (PLACE-papers HEAD %s).' % git('rev-parse', '--short', 'HEAD'))
rule()
for k, rel in DOCS:
    say('  %-7s %-62s last commit %s ; blob %s' % (k, rel, git('log', '-1', '--format=%h', '--', rel),
                                                   git('rev-parse', 'HEAD:' + rel)[:12]))

rule()
say('### READ 2 -- THE COMMITMENT ON THE DARK SECTOR`S EQUATION OF STATE, IN EACH DOCUMENT`S OWN WORDS.')
rule()
quote('FANO: the assignment', 'FANO', '4. The equation-of-state assignment sends weight-1 elements', 'to a symmetry-breaking residual.')
quote('FANO: dark energy is one orbit class', 'FANO', 'The dark energy is not a separate substance', '(the Hamming-distance assignment).')
quote('FANO: the residual`s w, its own reach', 'FANO', 'The diagonal residual', 'manifests observationally.')
quote('STORMER: the pending test', 'STORMER', 'DESI 5-year', 'for DE/visible')
quote('FORMATION_DISTANCE: prediction 4', 'FD', '4. **DESI year-3 tests w = −1.**', 'refutes the decomposition.')
quote('the dark-variable document, §IV', 'FDDV', 'The cosmological leg has a near-term', 'would constrain it.')

rule()
say('### READ 3 -- THE REGISTER: EACH DOCUMENT`S ROW.')
rule()
reg = read(P['REG'])
for lab, pat in (('p2-30 FANO', r'(?m)^\| p2-30 \|.*$'), ('p2-10 STORMER', r'(?m)^\| p2-10 \|.*$'),
                 ('p2-d6 FORMATION_DISTANCE', r'(?m)^\| p2-d6 \|.*$'), ('1.5c-14 the dark-variable document', r'(?m)^\| 1\.5c-14 \|.*$'),
                 ('the withdrawal line', r'(?m)^\| `FORMATION_DISTANCE_DARK_VARIABLE_v0_1\.md` \| 1\.5c-14 \|.*$')):
    READS[0] += 1
    hit = re.search(pat, reg)
    if not hit:
        MISS.append('REGISTRY row absent: %s' % lab)
        say('  %-44s ### **MISS**' % lab)
        continue
    say('  %-44s REGISTRY.md line %d' % (lab, reg[:hit.start()].count(NL) + 1))
    for s in wrap(fold(hit.group(0))[:600], 96):
        say('      | %s' % s)

rule()
say('### READ 4 -- THE TRAIL THE CORPUS ALREADY KEEPS ON THIS TEST.')
rule()
quote('OPEN_TRAILS O.8', 'TRAILS', '### O.8 — DESI 5-year analysis prep', 'integrated into Hubble-tension prediction tables.')

rule()
say('### READ 5 -- WHAT RESULT THE CORPUS ALREADY CITES: A SEARCH, EVERY HIT PRINTED.')
rule()
say('  THE SHAPES, FIXED BEFORE THE SEARCH: a named data release, a supernova compilation, or a stated w0/wa figure.')
SHAPES = [('a named release', r'DESI (DR|Y)\d|DESI (year|five)[- ]?\w*'),
          ('a supernova compilation', r'(?i)Pantheon\+?|Union ?3|DES[- ]?SN ?5 ?YR|DESY5'),
          ('a w0 / wa figure', r'(?i)\bw_?0\b[^|]{0,40}\bw_?a\b|\bw_?a\s*[<=>]|w\(z\)|evolving (dark energy|equation)')]
files = git('ls-files', '*.md').split()
say('  files in scope : %d tracked PLACE-papers .md files' % len(files))
for lab, rx in SHAPES:
    hits = []
    for f in files:
        t = read(os.path.join(PP, *f.split('/')))
        for k, ln in enumerate(t.splitlines()):
            if re.search(rx, ln):
                hits.append((f, k + 1, ln.strip()))
    say('  %-28s hits %d' % (lab, len(hits)))
    for f, k, ln in hits[:40]:
        mm = re.search(rx, ln)
        say('      %s:%d  ...%s...' % (f, k, ln[max(0, mm.start() - 60):mm.end() + 80]))
    if len(hits) > 40:
        say('      ... %d further hits not printed' % (len(hits) - 40))

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : %d' % READS[0])
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for x in MISS:
    say('      %s' % x)
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if MISS else 0)
