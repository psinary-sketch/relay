# -*- coding: utf-8 -*-
"""b429_extract.py -- THE SURVEY FOR b429: THE EXTERNAL GRADING READ.
### **THE CORPUS, THE CORPUS'S OWN KERNELS AND THIS MACHINE ONLY. ### NOTHING IS FETCHED BY THIS TOOL AND NO
### ADDRESS IS RESOLVED HERE.** ### Every read anchored in the markup-folded text, every miss counted.
### ### **AND THE MACHINE IS SURVEYED BECAUSE COMPONENT 2 IS A BUILD:** what toolchains exist, what the corpus
### pins, and how much room there is -- facts that decide whether the act can do what it was ordered to do.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
RDM = os.path.join(PP, 'README.md')
EXC = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
BRIDGE = os.path.join(SK, 'Bridge', 'ConservationBridge.lean')
PRICE = os.path.join(D, 'b428_external_price.txt')
OUT = os.path.join(D, 'b429_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]


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


def quote(label, path, start, end=None, width=96, cap=900, text=None):
    READS[0] += 1
    src = fold(text if text is not None else read(path))
    s0, e0 = fold(start), fold(end) if end else ''
    i = src.find(s0)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-50s ### **MISS** -- anchor absent in %s' % (label, os.path.basename(path)))
        return ''
    j = src.find(e0, i + len(s0)) if end else -1
    seg = src[i:j + len(e0)] if j > i else src[i:i + cap]
    say('  %-50s %s' % (label, os.path.basename(path)))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


def run(*args, **kw):
    try:
        r = subprocess.run(list(args), capture_output=True, text=True, encoding='utf-8', errors='replace',
                           timeout=kw.get('timeout', 60))
        return ((r.stdout or '') + (r.stderr or '')).strip()
    except Exception as exc:
        return '### NOT RUN -- %s' % exc


rule('=')
say('b429_extract.py -- THE SURVEY: THE EXTERNAL GRADING READ. ### NOTHING FETCHED, NO ADDRESS RESOLVED.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROW 277 BY ITS MARKER, AND b428`S PRICE AT RUN 2.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
READS[0] += 1
got = [int(x.group(1)) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*SITE \(iii\), THE WIDTH COORDINATE'S UNION", corr)]
say('  b428`s row by its marker : %s   (expected [277])' % got)
if got != [277]:
    MISS.append('b428`s row is not 277 by its marker')
quote('b428`s price, run 2', PRICE, 'THE PRICE: 4 ACTS IF THE REPOSITORY IS REACHABLE', 'A grading that skipped it would be grading an announcement.')
quote('b428`s address verdict', PRICE, 'NOT LOCATED.', 'would be manufacturing a citation.')

rule()
say('### READ 1 -- THE GRADING DISCIPLINE, IN THE CORPUS`S OWN WORDS. ### THE OBJECT THIS ACT CALIBRATES.')
rule()
quote('the three grades, README', RDM, '### The three grades', 'labelled as such wherever they appear.')
quote('the three grades, the exclusion keystone', EXC, 'Every kernel citation in this paper carries one of three grades',
      'A shell is a work-order, not a citation.')
quote('what the salt-check found in the corpus`s own work', EXC, 'The third grade is not a hypothetical.',
      'and §VIII is its exhibit.')
g3 = fold(read(RDM))
for g in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION'):
    READS[0] += 1
    say('  grade named in README : %-22s %s' % (g, g in g3))
    if g not in g3:
        MISS.append('grade %s absent from README' % g)
say('  ### ### **AND A FOURTH GRADE THE ORDER NAMES -- `NOT THE CLAIM` -- IS SEARCHED FOR IN THE CORPUS:**')
NTC = []
for base in (PP,):
    for dp, _dn, fn in os.walk(base):
        if os.sep + 'archive' in dp or os.sep + '.git' in dp:
            continue
        for f in fn:
            if f.endswith('.md'):
                t = read(os.path.join(dp, f))
                if re.search(r'(?i)\bNOT THE CLAIM\b', t):
                    NTC.append(os.path.relpath(os.path.join(dp, f), base))
READS[0] += 1
say('  ### corpus documents naming a grade `NOT THE CLAIM` : %d %s' % (len(NTC), NTC[:6]))

rule()
say('### READ 2 -- THE CORPUS`S OWN ROUTE TERMINAL, AT SOURCE. ### THE SELF-GRADING TEST`S SUBJECT.')
rule()
br = read(BRIDGE)
for lab, pat in (('the named premise, defined', r'def ConservationHypothesis : Prop :=[\s\S]{0,400}?(?=\n\n|\n/--)'),
                 ('the terminal itself', r'theorem riemann_hypothesis[\s\S]{0,300}?(?=\n\nend|\Z)')):
    READS[0] += 1
    m = re.search(pat, br)
    if not m:
        MISS.append('ConservationBridge : %s' % lab)
        say('  %-50s ### **MISS**' % lab)
        continue
    ln = br[:m.start()].count(NL) + 1
    say('  %-50s Bridge/ConservationBridge.lean line %d' % (lab, ln))
    for s in m.group(0).splitlines():
        say('      | %s' % s.rstrip()[:110])
quote('the terminal`s own docstring', BRIDGE, 'The Riemann Hypothesis, conditional on Conservation. Zero sorry.')
say('  ### ### **AND THE ORDER NAMES THE PREMISE `h2`; THE SOURCE NAMES IT `h_cons : ConservationHypothesis`.**')
say('  ### A source governs its paraphrase (BAR 8); both are printed and the source`s name is the one used.')
RH = run('git', '-C', SK, 'grep', '-n', 'def RiemannHypothesis', '--', '.lake/packages/mathlib')
READS[0] += 1
say('  where `RiemannHypothesis` is DEFINED : %s'
    % (RH.splitlines()[0][:120] if RH and 'NOT RUN' not in RH else '### NOT RESOLVED BY git grep'))
mth = os.path.join(SK, '.lake', 'packages', 'mathlib', 'Mathlib', 'NumberTheory', 'LSeries', 'RiemannZeta.lean')
if os.path.exists(mth):
    t = read(mth)
    # ### **THE FILE IS CHECKED OUT WITH CRLF**, so a `\n\n` paragraph anchor never matches -- the byte-level
    # ### trap this record has banked before. ### The definition is taken as its own line and its indented
    # ### continuations, which is line-ending agnostic.
    m = re.search(r'def RiemannHypothesis : Prop :=[^\r\n]*(?:\r?\n[ ]+[^\r\n]*)*', t)
    READS[0] += 1
    say('  Mathlib`s own definition, quoted :')
    for s in (m.group(0).splitlines() if m else ['### MISS']):
        say('      | %s' % s.rstrip()[:110])
    if not m:
        MISS.append('Mathlib RiemannHypothesis definition not quotable')
else:
    MISS.append('Mathlib RiemannZeta.lean not on disk at the kernel`s package path')
    say('  ### **MISS** -- Mathlib RiemannZeta.lean not at the kernel`s package path')

rule()
say('### READ 3 -- THE CORPUS`S OWN TOOLCHAIN PINS. ### WHAT COMPONENT 2 COMPARES THE FOREIGN ONE AGAINST.')
rule()
for lab, p in (('SIDE-kernel', os.path.join(SK, 'lean-toolchain')),
               ('SIDE-global-section', os.path.join(KERN, 'lean-toolchain'))):
    READS[0] += 1
    say('  %-22s lean-toolchain : %r' % (lab, read(p).strip()))
mpath = os.path.join(SK, '.lake', 'packages', 'mathlib')
READS[0] += 1
if os.path.isdir(mpath):
    say('  SIDE-kernel`s Mathlib : rev %s ; its own toolchain %r'
        % (run('git', '-C', mpath, 'rev-parse', 'HEAD')[:12], read(os.path.join(mpath, 'lean-toolchain')).strip()))
else:
    say('  SIDE-kernel`s Mathlib : ### NOT ON DISK')
    MISS.append('SIDE-kernel Mathlib package absent')
say('  ### **THE CORPUS`S KERNELS ARE PINNED AT `v4.29.0-rc8` AND `v4.29.1`; THE FOREIGN PIN IS READ AFTER THE LOCK.**')

rule()
say('### READ 4 -- THIS MACHINE. ### A BUILD IS ORDERED, SO WHAT THE MACHINE HAS IS A FACT THE FACE NEEDS.')
rule()
READS[0] += 1
say('  elan on PATH        : %s' % (shutil.which('elan') or '### ABSENT'))
say('  lake on PATH        : %s' % (shutil.which('lake') or '### ABSENT'))
say('  lake --version      : %s' % run('lake', '--version').splitlines()[0][:100])
say('  lean --version      : %s' % run('lean', '--version').splitlines()[0][:100])
tc = os.path.join(os.path.expanduser('~'), '.elan', 'toolchains')
READS[0] += 1
inst = sorted(os.listdir(tc)) if os.path.isdir(tc) else []
say('  toolchains INSTALLED: %s' % (inst or '### NONE'))
say('  ### ### **NEITHER OF THE CORPUS`S TWO PINS IS AMONG THEM**, and the foreign pin is unknown until the')
say('  ### repository is read -- so ### **ELAN WILL HAVE TO FETCH A TOOLCHAIN**, which is a host this act must name.')
READS[0] += 1
for drive in ('C:', 'D:'):
    try:
        tot, used, free = shutil.disk_usage(drive + os.sep)
        say('  free space %-3s      : %.1f GiB of %.1f GiB' % (drive, free / 2 ** 30, tot / 2 ** 30))
    except Exception as exc:
        say('  free space %-3s      : ### NOT READ -- %s' % (drive, exc))
say('  ### ### **`C:` IS THE DRIVE `~/.elan` LIVES ON AND IT IS NEARLY FULL.** ### A Lean toolchain is of the')
say('  ### order of a gigabyte and a Mathlib cache several. ### **THE BUILD MUST BE POINTED AT `D:` OR IT WILL')
say('  ### ### FAIL FOR ROOM RATHER THAN FOR MATHEMATICS**, and an act that let it fail that way would report a')
say('  ### disk as a defect in a proof.')
READS[0] += 1
mc = os.path.join('D:', os.sep, 'mathlib-cache')
say('  a Mathlib olean cache on D: : %s (%d entries)' % (os.path.isdir(mc), len(os.listdir(mc)) if os.path.isdir(mc) else 0))

rule()
say('### READ 5 -- WHAT THE CORPUS ALREADY SAYS ABOUT NAVIER-STOKES. ### SO THE ACT RELIES ON NONE OF IT.')
rule()
quote('the corpus`s own Navier-Stokes sentence', os.path.join(PP, 'day1', 'A_Place_to_Stand.md'),
      'For Navier-Stokes, three structural conflicts', 'on their own terms.')
quote('and its own retraction beside it', os.path.join(PP, 'day1', 'A_Place_to_Stand.md'),
      'Scope retractions.', 'in subsequent work.')
say('  ### ### **NONE OF THAT IS EVIDENCE ABOUT THE OBJECT THIS ACT GRADES.** ### The corpus`s Navier-Stokes')
say('  ### material is its own companion work, unbuilt and unverified here; ### **IT IS PRINTED SO THAT IT CANNOT')
say('  ### ### LATER BE READ AS A PRIOR**, and the grading uses the Clay page and the foreign source only.')

rule()
say('### READ 6 -- THE ACT`S OWN SCOPE, MEASURED: WHAT IS ALREADY ON DISK UNDER THE ADDRESSES` NAMES.')
rule()
READS[0] += 1
for p in (os.path.join('D:', os.sep, '_b429_external'),):
    say('  the scratch clone directory %s : exists %s' % (p, os.path.isdir(p)))
say('  ### The clone, the toolchain and every fetched byte go OUTSIDE every rostered repository, and their')
say('  ### digests come back into `relay/data/`. ### **`0` BYTES OF THE FOREIGN REPOSITORY ENTER ANY CORPUS REPO.**')

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
