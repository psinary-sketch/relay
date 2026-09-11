# -*- coding: utf-8 -*-
"""b422_extract.py -- THE SURVEY FOR b422. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### The fold of b413-b421, (R37) on the keystone, (R31)'s orientation refresh, and the witness arc named.
### **NOTHING IS WRITTEN OUTSIDE THIS ACT'S OWN RECORD.**
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
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
FL = os.path.join(PP, 'FACES_LEDGER.md')
CORR = os.path.join(KERN, 'CORRESPONDENCE.md')
OUT = os.path.join(D, 'b422_extract.txt')
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


def quote(label, path, start, end=None, width=96, cap=900):
    READS[0] += 1
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-44s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = re.sub(r'\s+', ' ', src[i:j + len(end)] if j > i else src[i:i + cap]).strip()
    say('  %-44s %s line %d' % (label, os.path.basename(path), src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


def lines(label, path, pattern, cap=12, width=160):
    READS[0] += 1
    src = read(path).splitlines()
    hits = [(k + 1, x) for k, x in enumerate(src) if re.search(pattern, x)]
    say('  %-44s %s : %d line(s) match%s' % (label, os.path.basename(path), len(hits),
                                           ' ; first %d printed' % cap if len(hits) > cap else ''))
    for k, x in hits[:cap]:
        say('      %5d | %s' % (k, x.strip()[:width]))
    if not hits:
        MISS.append('%s : no line matches %r' % (label, pattern))
    return hits


rule('=')
say('b422_extract.py -- THE SURVEY: THE FOLD, THE RULING, THE ORIENTATION LAYER, AND THE WITNESS ARC.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROW 270 BY ITS MARKER, AND THE SPAN BY THE TOOL (READ MODE, WRITES NOTHING).')
rule()
corr = read(CORR)
m270 = [int(m.group(1)) for m in re.finditer(r"(?m)^\| (\d+) \| \*\*THE GRID TRACE DEFINED HERE EQUALS", corr)]
say('  row of b421`s marker : %s' % m270)
if m270 != [270]:
    MISS.append('b421`s row is not 270 by its marker')
READS[0] += 1
r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'b363_span.py')], capture_output=True, text=True,
                   encoding='utf-8', errors='replace')
for ln in (r.stdout or '').splitlines():
    if re.search(r'the last fold covers|it was FILED BY|so the next span|and it now runs|THE CURRENT SPAN', ln):
        say('      | %s' % ln.strip())
quote('(R1), the threshold', os.path.join(D, 'b366_extract_notes.txt'), '(R1) THE FOLD THRESHOLD is NINE acts.', None, cap=200)
quote('(R31), the orientation layer', os.path.join(D, 'b412_ferry.txt'), 'RULING (R31)', 'is not closed.')
quote('b412: its fold`s span rule', FIND, '**The tool reports 10, counting b403 through b412;', 'the same way.')

rule()
say('### READ 1 -- THE FOLD`S OWN MEASURES, AS THE LAST FOLD WROTE THEM.')
rule()
quote('b412: the OBJECT / RECORD criterion', os.path.join(ROOT, 'tools', 'b412_components.py'), "rec('  ### **THE CRITERION, FIXED ON THE FACE BEFORE THE COUNT:**", "corpus has or has not asked.')")
lines('prior folds: their object counts', FIND, r'Statements about the \*\*object\*\*|statements about the object|STATEMENTS ABOUT THE OBJECT', cap=12, width=200)
lines('fold sections and one-statements', FIND, r'^## .*THE FOLD$|^### The arc’s one statement', cap=30, width=120)
quote('b412: F-NOGRADE and F-NOSUPERSEDE', os.path.join(ROOT, 'tools', 'b412_components.py'), "wrap('### **`F-NOGRADE`** (from `b348`)", 'SUPERSEDED.**')

rule()
say('### READ 2 -- THE SPAN, ACT BY ACT: EACH ACT`S BANK AND ITS GRADE STRINGS.')
rule()
banks = {413: 'b413', 414: 'b414', 415: 'b415', 416: 'b416', 417: 'b417', 418: 'b418_the_ruling_carried.txt',
         419: 'b419_the_clause_printed.txt', 420: 'b420_the_lemma_aimed.txt', 421: 'b421_the_finite_ambient.txt'}
for a in range(413, 422):
    cand = sorted(f for f in os.listdir(D) if f.startswith('b%d_' % a) and f.endswith('.txt')
                  and not re.search(r'census|pins|checks|scan|reg_|regspec|lockgate|extract|ferry|mirror|desk|satisf|registration|closing|components|seal|termscan|span|stderr|build|kernel', f))
    say('  b%d : candidate banks %s' % (a, cand[:6]))
lines('b419`s bank: its grade sentence', os.path.join(D, 'b419_the_clause_printed.txt'), r'(?i)grades? moved', cap=4)
lines('b420`s record: "moved one grade"', os.path.join(D, 'b420_c4_barrier.txt'), r'(?i)moved one grade', cap=4)
quote('row S1`s K3, as the ledger holds it now', FL, 'K3 the finite places’ contribution:', '(b310);')
sub = subprocess.run(['git', '-C', PP, 'log', '-1', '--format=%h %cI %s', '--', 'FACES_LEDGER.md'], capture_output=True, text=True).stdout.strip()
say('  FACES_LEDGER.md last changed by : %s' % sub[:120])

rule()
say('### READ 3 -- (R37): THE KEYSTONE`S SETTING, ITS DEFINITION, AND WHERE AN APPENDED SECTION GOES.')
rule()
quote('the keystone`s logic', IB, 'Throughout, we work in classical first-order logic.', 'in a domain |M|.')
quote('Definition 2.1', IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
ib = read(IB)
say('  keystone lines : %d ; its last heading : %r ; its last html marker : %r'
    % (len(ib.splitlines()), (re.findall(r'(?m)^#{2,3} .*', ib) or ['?'])[-1][:90], (re.findall(r'<!-- .*? -->', ib) or ['?'])[-1][:90]))
quote('b421: the price under Definition 2.1', os.path.join(D, 'b421_c2_specification.txt'), '### ### **PRICE UNDER DEFINITION 2.1, READ AS WRITTEN: NOT SUPPLIABLE.**', 'choosing one is the author`s.')
quote('b421: the Löwenheim-Skolem citation', os.path.join(D, 'b421_c2_specification.txt'), '### ### **THE SEAT`S CITATION, NOT THE RECORD`S', 'contains infinitely many functions.')

rule()
say('### READ 4 -- (R31): THE DIGEST AND THE FIVE-DOOR STATE, AT THEIR OWN DATES.')
rule()
dg = read(DIGEST)
say('  digest lines : %d ; acts named in it, newest : b%s' % (len(dg.splitlines()), max([int(x) for x in re.findall(r'\bb(\d{3})\b', dg)] or [0])))
lines('the digest`s last blocks', DIGEST, r'^#{2,4} |<!-- b4', cap=8, width=150)
pa = read(PATHS)
say('  PATHS lines : %d' % len(pa.splitlines()))
lines('the five-door state: its heading and rows', PATHS, r'I-bis|^\| \*\*R[1-5]|^\| R[1-5]\b', cap=12, width=200)
lines('the five-door state: b412`s block', PATHS, r'b412', cap=4, width=200)

rule()
say('### READ 5 -- THE ADDITION: ROW U1`S WITNESS COLUMN AND ITS CLASS SITE.')
rule()
u1 = next((x for x in read(FL).splitlines() if x.startswith('| U1 ')), '')
w = re.findall(r'WITNESS: *`([A-Z ]+)`', u1)
say('  row U1 WITNESS fields : %d -- %s' % (len(w), w))
say('  every one NONE KNOWN or UNSTATED : %s' % (bool(w) and all(x in ('NONE KNOWN', 'UNSTATED') for x in w)))
quote('site (i), the class site', FL, "### **(i) THE CLAUSE'S QUANTIFIER**, b332:", 'and they are the clause."*')
quote('site (iii), the width', FL, "### **(iii) THE WIDTH COORDINATE'S UNION**, b353:", 'union of all supports.')
quote('the lawful-class bound (b400)', os.path.join(D, 'b400_components_run2.txt'), '### **THEOREM 1 CARRIES A SUPPORT HYPOTHESIS**', 'theta(g)*)."*')
quote('the wide-support window (b400)', os.path.join(D, 'b400_components_run2.txt'), '### ### **AND THE CORRECTION MAKES THE WINDOW BETTER, NOT WORSE:', 'STILL IN FORCE.')

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : %d' % READS[0])
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if MISS else 0)
