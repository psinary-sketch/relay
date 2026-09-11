# -*- coding: utf-8 -*-
"""b423_extract.py -- THE SURVEY FOR b423, THE SORTIE'S FIRST LEG: THE (R37) QUESTION.
### **EVERY READ ANCHORED, EVERY MISS COUNTED. NOTHING WRITTEN OUTSIDE THIS ACT'S RECORD.**
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
OUT = os.path.join(D, 'b423_extract.txt')
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


rule('=')
say('b423_extract.py -- THE SURVEY: THE (R37) QUESTION, THE SORTIE`S FIRST LEG.')
rule('=')
rule()
say('### READ 0 -- THE ORIENTATION.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m = [int(x.group(1)) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*THE KERNEL ARC FOLDED", corr)]
say('  row of b422`s marker : %s' % m)
if m != [271]:
    MISS.append('b422`s row is not 271 by its marker')

rule()
say('### READ 1 -- THE RULING AND THE DEFINITION IT READS.')
rule()
quote('§10.2: the ruling', IB, '**The ruling, the author’s:**', 'characterized in practice.')
quote('§10.2: what it does not do', IB, '**What the ruling does not do.**', 'not run here.**')
quote('Definition 2.1', IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
quote('Theorem 3.1: its hypothesis on M', IB, '**Theorem 3.1 (Sieve Ceiling Lemma).** *Let M be a determined structure', 'target parameter P.')

rule()
say('### READ 2 -- b407`S READING OF HYPOTHESIS 1 FOR xi, AND WHAT ITS VERDICT RESTS ON.')
rule()
b407 = os.path.join(D, 'b407_the_barriers_own_instance.txt')
quote('b407: the four met, xi determined', b407, '### Four of Theorem 3.1’s five hypotheses are', 'κ(σ, I) = 0."*')
quote('b407: the one that fails', b407, '### ### **THE ONE THAT FAILS IS THE ONE ABOUT `π`.**', 'HAS NOT DISCHARGED.**')

rule()
say('### READ 3 -- b420`S READING OF HYPOTHESIS 1 FOR THE TEST-FUNCTION STRUCTURE, AND ITS VERDICT.')
rule()
c4 = os.path.join(D, 'b420_c4_barrier.txt')
quote('b420: hypothesis 1', c4, '### **FOR THE STRUCTURE WHOSE ELEMENTS ARE THE CLASS`S TEST FUNCTIONS', 'the keystone does not.')
quote('b420: the verdict', c4, '### ### ### **NOT AN INSTANCE -- THE FIFTH HYPOTHESIS FAILS, AND IT FAILS ON FORM.**', 'terminal.')
quote('b420: hypothesis 1 not scored as the verdict', c4, 'Two further readings are printed, not scored as', 'b419`s terminal.')

rule()
say('### READ 4 -- WHAT A SET-THEORETIC DEFINITION OF EACH STRUCTURE WOULD BE BUILT FROM.')
rule()
quote('the monograph`s specification of xi', os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md'),
      'For ξ(s): the specification is θ(τ) = Σ exp(πin²τ)', 'No human choices enter.')
quote('the class, as the source states it (b400)', os.path.join(D, 'b400_components_run2.txt'), '### **PROPOSITION C.1 CARRIES NONE**', 'for all z in F."*')
quote('the local term at a prime (b310, eq. 149)', os.path.join(D, 'b310_the_smear_collapses.txt'), '**`W_p(f) = (log p) SUM_{m>=1}', '(149), Appendix B')
quote('b421: under the monograph`s definition', os.path.join(D, 'b421_c2_specification.txt'), '### ### **PRICE UNDER THE MONOGRAPH`S DEFINITION:', 'NOT WRITTEN.**')

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
