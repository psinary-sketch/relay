# -*- coding: utf-8 -*-
"""b426_extract.py -- THE SURVEY FOR b426, THE SORTIE'S FIRST LEG: THE FALSIFIER RE-READ BY ADDRESS.
### **THE CORPUS ONLY. NOTHING IS FETCHED BY THIS TOOL: THE ADDRESS IS LOCATED AFTER THE LOCK, AS b425 LOCATED ITS
### OWN SOURCES. EVERY READ ANCHORED IN THE MARKUP-FOLDED TEXT, EVERY MISS COUNTED, EVERY PIN PRINTED.**
"""
import io
import json
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
OUT = os.path.join(D, 'b426_extract.txt')
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

B424MARK = "**THE WITNESS ARC AT SITE (i), THE CLAUSE'S QUANTIFIER: SIXTEEN CANDIDATES READ AT SOURCE, NONE HELD**"
B425MARK = ("**THE FALSIFIER READ: THE LANE'S w = −±AGAINST THREE SUPERNOVA RESULTS**")  # placeholder, re-set below
B425MARK = ("**THE FALSIFIER READ: THE LANE'S w = −1 AGAINST THREE SUPERNOVA RESULTS -- "
            "FIRED AT 1 BY THE LOCKED RULE, UNDECIDED AT 2**")


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
    return subprocess.run(['git', '-C', PP] + list(args), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


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
say('b426_extract.py -- THE SURVEY: THE FALSIFIER RE-READ BY ADDRESS, THE SORTIE`S FIRST LEG. ### THE CORPUS ONLY.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROWS 273 AND 274 BY THEIR MARKERS.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
for lab, mk, want in (('b424`s row', B424MARK, 273), ('b425`s row', B425MARK, 274)):
    READS[0] += 1
    got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), corr)]
    say('  %-16s by its marker : %s   (expected [%d])' % (lab, got, want))
    if got != [want]:
        MISS.append('%s is not %d by its marker' % (lab, want))

rule()
say('### READ 1 -- THE LANE`S DOCUMENTS AND THEIR PINS (PLACE-papers HEAD %s).' % git('rev-parse', '--short', 'HEAD'))
rule()
for k, rel in DOCS:
    say('  %-7s %-62s last commit %s ; blob %s' % (k, rel, git('log', '-1', '--format=%h', '--', rel),
                                                   git('rev-parse', 'HEAD:' + rel)[:12]))

rule()
say('### READ 2 -- THE SENTENCE (R38) APPENDS TO: FORMATION_DISTANCE.md LINE 160, AND ITS NEIGHBOURS.')
rule()
fd = read(P['FD'])
fdlines = fd.splitlines()
for n in (158, 159, 160, 161, 162):
    READS[0] += 1
    if 1 <= n <= len(fdlines):
        say('  line %-4d | %s' % (n, fdlines[n - 1][:180]))
    else:
        MISS.append('FORMATION_DISTANCE.md has no line %d' % n)
        say('  line %-4d ### **MISS** -- the file has %d lines' % (n, len(fdlines)))
quote('FORMATION_DISTANCE: the condition', 'FD', '4. **DESI year-3 tests w = −1.**', 'refutes the decomposition.')

rule()
say('### READ 3 -- THE LANE`S COMMITMENT, IN EACH DOCUMENT`S OWN WORDS (CARRIED FROM b425, RE-READ HERE).')
rule()
quote('FANO: the assignment', 'FANO', '4. The equation-of-state assignment sends weight-1 elements', 'to a symmetry-breaking residual.')
quote('FANO: the residual`s w, its own reach', 'FANO', 'The diagonal residual', 'manifests observationally.')
quote('STORMER: the pending test', 'STORMER', 'DESI 5-year', 'for DE/visible')

rule()
say('### READ 4 -- THE REGISTER ROW (R39) NOTES: p2-d6, VERBATIM, AND ITS COLUMN COUNT.')
rule()
reg = read(P['REG'])
for lab, pat in (('p2-d6 FORMATION_DISTANCE', r'(?m)^\| p2-d6 \|.*$'),
                 ('the row above it', r'(?m)^\| p2-d5 \|.*$'),
                 ('the withdrawal line', r'(?m)^\| `FORMATION_DISTANCE_DARK_VARIABLE_v0_1\.md` \| 1\.5c-14 \|.*$')):
    READS[0] += 1
    hit = re.search(pat, reg)
    if not hit:
        MISS.append('REGISTRY row absent: %s' % lab)
        say('  %-44s ### **MISS**' % lab)
        continue
    say('  %-44s REGISTRY.md line %d ; cells %d' % (lab, reg[:hit.start()].count(NL) + 1,
                                                    len(hit.group(0).strip().strip('|').split('|'))))
    say('      | %s' % hit.group(0))

rule()
say('### READ 5 -- b425`S THREE SOURCES, THEIR VERDICTS AND THEIR STATED FIGURES, FROM b425`S OWN BANKED RECORD.')
rule()
try:
    RJ = json.loads(read(os.path.join(D, 'b425_the_read.json')))
except Exception as exc:
    RJ = dict(sources=[], fired=[])
    MISS.append('b425_the_read.json : %s' % exc)
for s in RJ.get('sources', []):
    READS[0] += 1
    say('  %-12s %-10s %s' % (s['id'], s['verdict'], s['title'][:74]))
    for w in wrap('deciding sentence, as b425 banked it: ' + s['deciding'][:400], 94):
        say('      | %s' % w)
say('  b425`s FIRED list : %s' % RJ.get('fired', []))
if len(RJ.get('sources', [])) != 3:
    MISS.append('b425 banked %d sources, not 3' % len(RJ.get('sources', [])))

rule()
say('### READ 6 -- THE TRAIL THE CORPUS ALREADY KEEPS ON THIS TEST.')
rule()
quote('OPEN_TRAILS O.8', 'TRAILS', '### O.8 — DESI 5-year analysis prep', 'integrated into Hubble-tension prediction tables.')

rule()
say('### READ 7 -- DOES THE CORPUS ALREADY CARRY AN ADDRESS FOR THE COLLABORATION`S OWN PAPER? A SEARCH, EVERY HIT PRINTED.')
rule()
say('  THE SHAPES, FIXED BEFORE THE SEARCH: an arXiv identifier; a DOI; a named second data release.')
SHAPES = [('an arXiv identifier', r'(?i)arxiv[:\s]*\d{4}\.\d{4,5}|\b\d{4}\.\d{5}\b'),
          ('a DOI', r'(?i)doi[:\s/]*10\.\d{4,9}/'),
          ('a named second data release', r'(?i)DESI.{0,40}(DR2|Data Release 2)|DESI DR2')]
files = git('ls-files', '*.md').split()
say('  files in scope : %d tracked PLACE-papers .md files' % len(files))
CORPUS = {f: read(os.path.join(PP, *f.split('/'))) for f in files}
for lab, rx in SHAPES:
    READS[0] += 1
    hits = []
    for f, t in CORPUS.items():
        for k, ln in enumerate(t.splitlines()):
            if re.search(rx, ln):
                hits.append((f, k + 1, ln.strip()))
    say('  %-32s hits %d' % (lab, len(hits)))
    for f, k, ln in hits[:25]:
        mm = re.search(rx, ln)
        say('      %s:%d  ...%s...' % (f, k, ln[max(0, mm.start() - 50):mm.end() + 60]))
    if len(hits) > 25:
        say('      ... %d further hits not printed' % (len(hits) - 25))

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
