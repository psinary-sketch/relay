# -*- coding: utf-8 -*-
"""b374_figures.py -- COMPONENT 3: THE COUNT-AND-REF SWEEP. ### **THE LIST IS THE PRODUCT.**

### ### **A FIGURE WITHOUT A REF IS A CLAIM ABOUT AN UNNAMED MOMENT** (`b372`'s mint). ### This
### component asks how many of them the roster's descriptive surfaces carry.
### ### **THE WINDOW IS THE SENTENCE AND NOT THE DOCUMENT, AND THAT IS A CHOICE DECLARED AS ONE.** ### A
### document that dates itself once in a header does not thereby date every figure in it --
### ### **A READER LANDING ON A ROW READS THE ROW** -- and the alternative reading is stated so the
### author can disagree with the one taken.
### ### **THE LIST IS NOT RANKED, NOT PRIORITISED AND NOT TURNED INTO A PLAN.**
### ### **NOTHING IS REPAIRED, AND THE FROZEN SURFACES ARE SWEPT AND REPORTED SEPARATELY.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import hedge_audit as HA         # noqa: E402
import b303_pins                 # noqa: E402
import b374_hedge as HG          # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE PREDICATES, DECLARED BEFORE THE SWEEP SO THEY CAN BE DISAGREED WITH.**
# ### A FIGURE: a numeral governing a countable noun. ### The noun list is finite and given, and
# ### ### **A NOUN OFF IT IS INVISIBLE** -- that is the reach, not a defect hidden.
NOUNS = (r'terminals?|theorems?|lemmas?|modules?|files?|rows?|documents?|repositories|repos?|'
         r'kernels?|declarations?|prints?|axioms?|sorr(?:y|ys|ies)|entries|entry|acts?|'
         r'commits?|tags?|places?|zeros?|primes?|cells?|frames?|instances?|components?|'
         r'statements?|claims?|papers?|keystones?|pins?|arms?|bars?|gates?|checks?')
FIGURE = re.compile(r'(?<![A-Za-z0-9.])(\d{1,6})\s+(?:[a-z-]+\s+){0,2}(%s)(?![A-Za-z])' % NOUNS, re.I)
# ### A REF: a commit-like hex, a version tag, a date, or an explicit `at <ref>` form.
REF = re.compile(r'`[0-9a-f]{7,40}`|(?<![A-Za-z0-9])[0-9a-f]{7,40}(?![A-Za-z0-9])|'
                 r'\bv\d+\.\d+(?:\.\d+)?\b|\b20\d\d-\d\d-\d\d\b|\b20\d\d\b|'
                 r'\btag\b|\bHEAD\b|\bat\s+`|\brev\b|\bversion\b', re.I)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def classify(rel):
    if rel.startswith('outputs/DEPOSITED-'):
        return 'DEPOSITED (FROZEN)'
    if rel.startswith('archive/'):
        return 'ARCHIVE (FROZEN)'
    if rel.startswith('outputs/'):
        return 'OUTPUT'
    return None


def main():
    rec('=' * 100)
    rec('b374 -- COMPONENT 3: THE COUNT-AND-REF SWEEP. ### **THE LIST IS THE PRODUCT.**')
    rec('=' * 100)
    rec('')
    rec('  ### **THE PREDICATES, DECLARED:**')
    rec('  ###   FIGURE : a numeral governing a countable noun from a finite given list.')
    rec('  ###     ### **A NOUN OFF THE LIST IS INVISIBLE. ### THAT IS THE REACH, NOT A DEFECT HIDDEN.**')
    rec('  ###   REF    : %s' % REF.pattern[:150])
    rec('  ### ### **THE WINDOW IS THE SENTENCE.** ### A document that dates itself once in a header')
    rec('  ### ### does not thereby date every figure in it. ### **A READER LANDING ON A ROW READS THE')
    rec('  ### ### ROW.** ### The document-wide reading is the alternative and is named so the author')
    rec('  ### can disagree with the one taken.')

    # ---- the keystone / working-note partition, from the census, for (L2)'s second half ----------
    files_pp = [f for f in git(PP, 'ls-files', '*.md').split(chr(10)) if f.strip()]
    names, _a = HG.census_keystones()
    ks = {}
    for nm in names:
        hits = HG.locate(nm, files_pp)
        if len(hits) == 1:
            ks[hits[0]] = 'KEYSTONE'
    dep = set(f for f in files_pp if f.startswith('outputs/DEPOSITED-v1.1.2/'))

    rec('')
    rec('-' * 100)
    rec('  ### THE SWEEP, BY REPOSITORY.')
    rec('-' * 100)
    allrows = []
    totals = {}
    for name, repo in b303_pins.REPOS:
        rels = [f for f in git(repo, 'ls-files', '*.md').split(chr(10)) if f.strip()]
        nfig = nun = 0
        ndocs = 0
        for rel in rels:
            p = os.path.join(repo, rel.replace('/', os.sep))
            try:
                txt = io.open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            ndocs += 1
            for i, ln in enumerate(txt.split(chr(10)), 1):
                for s in HA._sentences(ln):
                    for m in FIGURE.finditer(s):
                        nfig += 1
                        if REF.search(s):
                            continue
                        nun += 1
                        cls = classify(rel) if name == 'PLACE-papers' else None
                        if cls is None and name == 'PLACE-papers':
                            cls = ks.get(rel, 'OTHER')
                        allrows.append(dict(repo=name, file=rel, line=i,
                                            figure=m.group(0).strip(),
                                            cls=(cls or name),
                                            text=s.strip()[:160]))
        totals[name] = dict(docs=ndocs, figures=nfig, undated=nun,
                            pct=(100.0 * nun / nfig if nfig else 0.0))
        rec('    %-22s %4d documents   figures %6d   ### **WITHOUT A REF IN THEIR SENTENCE : %6d'
            % (name, ndocs, nfig, nun))
        rec('    %-22s ### ### (%.0f%%)**' % ('', totals[name]['pct']))

    rec('')
    rec('-' * 100)
    rec('  ### THE PAPERS REPOSITORY, BY CLASS. ### **THE FROZEN SURFACES REPORTED SEPARATELY.**')
    rec('-' * 100)
    bycls = {}
    for r in allrows:
        if r['repo'] != 'PLACE-papers':
            continue
        bycls[r['cls']] = bycls.get(r['cls'], 0) + 1
    for k, v in sorted(bycls.items(), key=lambda x: -x[1]):
        rec('    %-24s %6d undated figures' % (k, v))
    rec('    ### ### **THE FROZEN CLASSES ARE READ, COUNTED, AND NOT REPAIRED IN ANY LEG.**')

    # ---- (L2)'s second half, per thousand sentences ---------------------------------------------
    rec('')
    rec('-' * 100)
    rec("  ### `(L2)`'s SECOND HALF, ON THE SAME FOOTING AS ITS FIRST: PER THOUSAND SENTENCES.")
    rec('-' * 100)
    hedge = json.load(io.open(os.path.join(D, 'b374_hedge.json'), encoding='utf-8'))
    sents = {'KEYSTONE': hedge['totals']['KEYSTONE']['sentences'],
             'DEPOSITED': hedge['totals']['DEPOSITED']['sentences'],
             'WORKING': hedge['totals']['WORKING']['sentences']}
    ks_un = sum(1 for r in allrows if r['cls'] == 'KEYSTONE')
    dep_un = sum(1 for r in allrows if r['cls'] == 'DEPOSITED (FROZEN)')
    oth_un = sum(1 for r in allrows if r['cls'] == 'OTHER')
    rec('  %-24s %10s %12s %14s' % ('population', 'sentences', 'undated', 'undated/k'))
    for lbl, n, s in (('KEYSTONE', ks_un, sents['KEYSTONE']),
                      ('DEPOSITED COMPANION', dep_un, sents['DEPOSITED']),
                      ('WORKING NOTE (OTHER)', oth_un, sents['WORKING'])):
        rec('  %-24s %10d %12d %14.1f' % (lbl, s, n, (1000.0 * n / s if s else 0.0)))
    rec('  ### ### **AND `OTHER` IS NOT EXACTLY THE HEDGE SWEEP`S `WORKING NOTE` POPULATION** -- it is')
    rec('  ### ### every living papers document that is not a keystone -- ### **SO THE RATE IS')
    rec('  ### ### REPORTED WITH THAT CAVEAT AND NOT AS AN EXACT PAIRING.**')

    rec('')
    rec('-' * 100)
    rec('  ### THE LIST. ### **NOT RANKED, NOT PRIORITISED, NOT A PLAN.**')
    rec('-' * 100)
    rec('    ### the first entries of each class, as evidence that the list is a list of real lines:')
    shown = 0
    seen = set()
    for r in allrows:
        if r['cls'] in seen:
            continue
        seen.add(r['cls'])
        rec('')
        rec('    [%s] %s:%d   figure `%s`' % (r['cls'], r['file'], r['line'], r['figure']))
        rec('        | %s' % r['text'])
        shown += 1
    rec('')
    rec('    ### ### **THE FULL LIST IS BANKED AS JSON: %d LINES.** ### It is not printed in full here')
    rec('    ### ### because a list this size in a bank is a wall, and the bank names where it lives.')

    rec('')
    rec('=' * 100)
    rec('  ### ### **TOTAL FIGURES WITHOUT A REF IN THEIR SENTENCE, ACROSS THE ROSTER : %d**'
        % len(allrows))
    rec('  ### **NOTHING WAS REPAIRED. ### NO FIGURE WAS DATED. ### NO LIST WAS RANKED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b374_figures_notes', LINES)
    io.open(os.path.join(D, 'b374_figures.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(totals=totals, by_class=bycls, undated_total=len(allrows),
                        l2=dict(keystone=ks_un, deposited=dep_un, other=oth_un, sentences=sents),
                        figure_pattern=FIGURE.pattern, ref_pattern=REF.pattern,
                        rows=allrows,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s  (%d undated figures banked)' % (os.path.basename(p), len(allrows)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
