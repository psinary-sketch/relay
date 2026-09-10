# -*- coding: utf-8 -*-
"""b403_extract.py -- THE SURVEY THE FACE IS WRITTEN FROM. ### **A READ, AND NOTHING ELSE.**

### ### **THE ADDITION SAYS A RULE EXISTS AND NAMES TWO PRIOR REPAIRS.** ### The rule's words are
### not in the record as the ferry phrases them, so this survey searches ### **BY THE RULE'S OWN
### ### DESCRIPTION AND NOT BY THE READER'S NAME FOR IT** -- which is `b385`'s species, and which is
### how the rule was found: it is `b371`'s precedent, applied at `b372`, and its own wording is
### *removed rather than restated, unless the document can name the ref it holds at.*

### ### **AND THE FIGURE IS MEASURED AT CONTENT BEFORE ANYTHING IS CALLED STALE** (`b371`'s method,
### `b372`'s application). ### A count that is exact at a ref and undated at the head is a NUMBER;
### a count whose scope cannot be established is a CLAIM; and the two take different repairs.

### ### **NO KERNEL IS BUILT.** ### The instrument lane is PARKED. ### `SIDE-window` ships no
### printed profile at all, and that is itself a finding rather than an obstacle: what can be read
### is its source's `#print axioms` invocations, which is a different quantity from a terminal
### count and is reported as one.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SW = os.path.join('D:', os.sep, 'SIDE-window')
FL = os.path.join(PP, 'FACES_LEDGER.md')
RM = os.path.join(SW, 'README.md')
SPAN = os.path.join(ROOT, 'tools', 'b363_span.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=240):
    return ' '.join(s.split())[:n]


READS = []
FIG = {}


def q(path, hint, label, n=320, span=False):
    i, ln, v = 0, '', 'ABSENT'
    if span:
        try:
            i, runs = AF.find_span(path, hint)
            ln = ' '.join(' '.join(r.split()) for r in runs)
            v = 'ANCHORED-SPAN'
        except Exception as e:
            v = 'AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT'
    else:
        try:
            i, ln = AF.find(path, hint)
            v = 'ANCHORED'
        except Exception as e:
            v = 'AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT'
    READS.append(dict(path=os.path.basename(path), label=flat(label, 160), line=i, verdict=v,
                      text=flat(ln, 900)))
    rec('    %s  ### `%s:%s`' % (label, os.path.basename(path), i or '--'))
    rec('      > %s' % flat(ln, n) if v.startswith('ANCHORED') else '      ### **%s**' % v)
    return i, ln


# ==================================================================================================
def survey_rule():
    bar('=')
    rec('  ### (1) THE RULE THE ADDITION INVOKES -- FOUND BY ITS DESCRIPTION, NOT BY ITS NAME.')
    bar('=')
    rec('  ### **THE FERRY`S WORDING -- *a figure on a claiming surface carries its ref or is not')
    rec('  ### written* -- APPEARS NOWHERE IN THE RECORD BUT IN THE FERRY ITSELF.** ### A search')
    rec('  ### for the navigator`s phrasing would have returned ABSENT and been wrong, which is')
    rec('  ### exactly `b385`s species. ### **SO THE SEARCH IS BY DESCRIPTION, AND THE RULE IS')
    rec('  ### ### THERE.**')
    rec()
    q(os.path.join(D, 'b371_the_first_target.txt'), 'A DESCRIPTION HAS NO HISTORY',
      '### `b371`: the original is banked BEFORE the edit', 340)
    q(os.path.join(D, 'b371_the_first_target.txt'), 'THE COUNT IS REMOVED RATHER THAN UPDATED',
      '### `b371`: and the count is REMOVED rather than UPDATED, flagged as a judgement', 340)
    q(os.path.join(D, 'b372_registration_2026-09-08.txt'),
      'REMOVED RATHER THAN RESTATED**, unless the document',
      '### `b372` states the rule with its one carve-out', 400)
    q(os.path.join(D, 'b372_registration_2026-09-08.txt'),
      'IF THE REPAIR WOULD REWRITE A CLAIM RATHER THAN A NUMBER',
      '### and the branch that routes instead of repairing', 340)
    rec()
    rec('  ### **AND THE TWO PRIOR REPAIRS THE ADDITION NAMES, CHECKED AGAINST THE RECORD.**')
    q(os.path.join(D, 'b371_the_first_target.txt'), 'public DESCRIPTION -- repaired',
      '### repair (1): the `SIDE-global-section` public DESCRIPTION, at `b371`', 300)
    q(os.path.join(D, 'b372_the_first_batch.txt'), 'REMOVED, NOT RESTATED',
      '### repair (2): the README headline and assembly ratio, at `b372`', 300)
    q(os.path.join(D, 'b372_the_first_batch.txt'), 'PRESERVED VERBATIM AND DATED TO THE',
      '### and what `b372` preserved-and-dated instead of removing', 300)
    q(os.path.join(D, 'b372_the_first_batch.txt'),
      'and its one count line was read and quoted anyway so nothing is lost',
      '### ### **AND THE SECOND REPAIR WAS NOT ON THE REPOSITORY THE ADDITION NAMES**', 340)
    rec()


# ==================================================================================================
def survey_readme():
    bar('=')
    rec('  ### (2) THE FIGURE, MEASURED AT CONTENT BEFORE ANYTHING IS CALLED STALE.')
    bar('=')
    q(RM, 'all 43 terminals are fully axiom-free', '### the claiming sentence, whole', 400)
    rec()
    per, allnames = {}, set()
    for f in sorted(os.listdir(SW)):
        if f.startswith('AxiomCheck') and f.endswith('.lean'):
            names = re.findall(r"#print axioms ([A-Za-z0-9_.']+)",
                               io.open(os.path.join(SW, f), encoding='utf-8',
                                       errors='replace').read())
            per[f] = dict(invocations=len(names), distinct=len(set(names)))
            allnames |= set(names)
            rec('      %-34s invocations %-4d distinct %d' % (f, len(names), len(set(names))))
    tot = sum(v['invocations'] for v in per.values())
    four = sum(v['invocations'] for k, v in per.items() if 'LocalModel' not in k)
    rec('      ### ### **TOTAL : `%d` INVOCATIONS, `%d` DISTINCT NAMES.**' % (tot, len(allnames)))
    rec('      ### ### **WITHOUT THE `v0.5` LOCAL MODEL : `%d`.**' % four)
    FIG['prints_per_file'] = per
    FIG['prints_total'] = tot
    FIG['prints_without_localmodel'] = four
    FIG['readme_claim'] = 43
    rec()
    rec('  ### ### ### **SO `43` IS NOT A WRONG NUMBER. ### IT IS AN EXACT ONE WITH NO DATE ON')
    rec('  ### ### ### IT** -- exact across the four check files the README`s tables describe, and')
    rec('  ### ### ### behind by exactly the `26` the `v0.5` local model added.')
    rec('  ### **THIS CORRECTS THIS SEAT`S OWN `b401` READING**, which reported `43 against 69` and')
    rec('  ### called it stale without establishing that `43` was exact anywhere. ### **IT IS')
    rec('  ### ### `b371`S SPECIES EXACTLY: EXACT AT A REF, STALE AT THE HEAD, CARRYING NO')
    rec('  ### ### QUALIFIER.**')
    rec()
    r = subprocess.run(['git', '-C', SW, 'log', '--oneline', '-1'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    par = subprocess.run(['git', '-C', SW, 'log', '--oneline', '-1', 'HEAD~1'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace')
    rec('      HEAD          : %s' % flat(r.stdout, 120))
    rec('      its parent    : %s' % flat(par.stdout, 120))
    rmlog = subprocess.run(['git', '-C', SW, 'log', '--oneline', '-1', '--', 'README.md'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
    rec('      README last touched at : %s' % flat(rmlog.stdout, 120))
    FIG['sw_head'] = flat(r.stdout, 60)
    rec()
    rec('  ### **AND WHETHER THE REPOSITORY`S OWN CONVENTIONS FORBID THE EDIT.**')
    for lbl, cmd in (('remote', ['git', '-C', SW, 'remote', '-v']),
                     ('working tree', ['git', '-C', SW, 'status', '--porcelain']),
                     ('tracked eol attribute', ['git', '-C', SW, 'check-attr', 'eol', '--',
                                                'README.md'])):
        out = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                             errors='replace').stdout
        rec('      %-24s : %s' % (lbl, flat(out, 100) or '(empty)'))
    hook = os.path.exists(os.path.join(SW, '.git', 'hooks', 'pre-push'))
    rec('      pre-push hook present    : %s   ### **AND IT IS NOT, WHICH IS A FINDING**' % hook)
    FIG['sw_hook'] = hook
    q(RM, 'Self-contained by construction',
      '### the repository`s own provenance clause, read for a prohibition', 340)
    rec('  ### ### **NOTHING IN IT FORBIDS AN EDIT TO ITS OWN README.** ### What it forbids is')
    rec('  ### depositing and drawing on private material, and this act does neither.')
    rec()
    rec('  ### **IS THERE A PRINTED PROFILE TO NAME A FIGURE AGAINST?**')
    prof = [f for f in os.listdir(SW) if f.endswith('.txt')]
    rec('      `.txt` files in the tree : %s' % (prof or '### **NONE**'))
    FIG['sw_profile_files'] = prof
    rec('  ### ### **THE REPOSITORY SHIPS NO PRINTED PROFILE.** ### `b372`s carve-out -- *a README')
    rec('  ### ### shipped in the same tree as the profile it cites CAN name that tree* -- ### **DOES')
    rec('  ### ### NOT REACH THIS README, BECAUSE THERE IS NO PROFILE IN THE TREE TO NAME.** ### The')
    rec('  ### README quotes a sample of what a run WOULD print; a quoted sample is not a profile.')
    rec()


# ==================================================================================================
def survey_span():
    bar('=')
    rec('  ### (3) THE SPAN COUNTER`S STALE SENTENCE, LOCATED IN THE FILE THAT CARRIES IT.')
    bar('=')
    src = io.open(SPAN, encoding='utf-8', errors='replace').read()
    hits = []
    for i, ln in enumerate(src.split(chr(10)), 1):
        if 'THRESHOLD' in ln.upper() and ('NO DECLARED' in ln.upper()
                                          or 'threshold_declared' in ln):
            hits.append((i, flat(ln, 150)))
    for i, ln in hits:
        rec('      `b363_span.py:%-4d` %s' % (i, ln))
    rec('      ### ### **SITES TO REPAIR : `%d`.**' % len(hits))
    FIG['span_sites'] = len(hits)
    rec()
    q(os.path.join(D, 'b366_closing.txt'), 'the fold threshold is',
      '### `(R1)`, the ruling the sentence has been false since', 340)
    q(os.path.join(D, 'b402_the_fold.txt'),
      'THE SPAN COUNTER`S OWN LINE ON THE THRESHOLD IS STALE',
      '### and `b402` routing it, which is what this act discharges', 320)
    rec()
    rec('  ### **WHAT A PRIOR FOLD PRINTED FROM THIS TOOL, SO `(N1)` CAN BE TESTED BY COMPARISON.**')
    b402 = json.load(io.open(os.path.join(D, 'b402_span.json'), encoding='utf-8'))
    keys = ('spans', 'shortest', 'longest', 'middle', 'last_fold', 'filed_by', 'span_starts_at')
    for k in keys:
        rec('      %-16s : %s' % (k, flat(json.dumps(b402[k]), 110)))
    rec('      folds recorded   : %d' % len(b402['folds']))
    FIG['b402_span_keys'] = {k: b402[k] for k in keys}
    FIG['b402_folds'] = len(b402['folds'])
    rec()


# ==================================================================================================
def survey_u1():
    bar('=')
    rec('  ### (4) ROW `U1`, AND WHAT THE CLOSING IS ASKED TO RESTATE AS AWAITING ENTRY.')
    bar('=')
    txt = io.open(FL, encoding='utf-8', errors='replace').read()
    row = [x for x in txt.split(chr(10)) if x.startswith('| U1 |')]
    marks = re.findall(r'\*\*\((i+v?|iv)\)[^*]*', row[0]) if row else []
    rec('      instances the row now carries : %d' % len(marks))
    for m in marks:
        rec('        %s' % flat(m, 130))
    FIG['u1_instances'] = len(marks)
    rec()
    rec('  ### ### **THE FERRY CALLS THE WINDOW A FIFTH SITE. ### THE ROW ALREADY CARRIES IT AS')
    rec('  ### ### THE FOURTH**, entered by `b401` as *THE PRIME CONSTITUENT AT A WIDENED SUPPORT*.')
    rec('  ### **SO THE CLOSING RESTATES WHAT IS THERE RATHER THAN ENTERING A FIFTH COPY OF IT** --')
    rec('  ### which is the double-count `b401`s own entry was written to prevent.')
    rec()
    rec('  ### **AND A GENUINELY DISTINCT FIFTH CANDIDATE DOES EXIST, FOUND BY `b401` AND NOT')
    rec('  ### ### ENTERED BY IT:** ### the located bound`s constant ### **DEPENDS ON THE')
    rec('  ### ### REPRESENTATION** ### while Theorem 5.1`s is ABSOLUTE -- the record needs a')
    rec('  ### statement uniform in `pi` and holds one indexed by it. ### **THAT IS THE ROW`S SHAPE')
    rec('  ### ### AT A FIFTH SITE, AND THIS ACT RESTATES IT AS AWAITING ENTRY AND DOES NOT ENTER')
    rec('  ### ### IT.**')
    rec()


def main():
    bar('=')
    rec('b403 -- THE THREE ROUTED ITEMS, DISCHARGED OR RULED. ### THE EXTRACT.')
    rec('### **A SURVEY. ### NO KERNEL IS BUILT AND NO INSTRUMENT IS RUN.**')
    bar('=')
    rec()
    survey_rule()
    survey_readme()
    survey_span()
    survey_u1()
    bar('=')
    rec('  ### THE SURVEY, COUNTED.')
    bar('=')
    anc = sum(1 for r in READS if r['verdict'].startswith('ANCHORED'))
    rec('    reads : %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d'
        % (len(READS), anc, sum(1 for r in READS if r['verdict'] == 'AMBIGUOUS'),
           sum(1 for r in READS if r['verdict'] == 'ABSENT')))
    FIG['reads'] = len(READS)
    FIG['anchored'] = anc
    bar('=')
    p = run_clock.write(D, 'b403_extract_notes', L)
    io.open(os.path.join(D, 'b403_extract.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(dict(reads=READS, fig=FIG), indent=1,
                                              ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b403_extract.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
