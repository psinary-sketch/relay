# -*- coding: utf-8 -*-
"""b374_entries.py -- COMPONENT 2: THE GLOSSARY AND THE BIBLIOGRAPHY, ENTRY BY ENTRY.

### ### **FOUR WORDS AND NO FIFTH: `CURRENT` / `RENAMED` / `RETIRED` / `NOT LOCATED`.**
### ### ### **AND `NOT LOCATED` IS NOT `ABSENT`.** ### A bibliography entry points at an EXTERNAL
### work; it was never expected to live in this record. ### **A SWEEP THAT MARKED EVERY EXTERNAL
### ### CITATION `NOT LOCATED` WOULD BE MEASURING ITS OWN SCOPE**, so the external class is separated
### FIRST and the in-record test is stated for what it actually is: ### **IS THE ENTRY STILL CITED
### ### UNDER THAT KEY.**
### ### **THE BIBLIOGRAPHY'S OWN LAWS GOVERN THE READ:** ### nothing is merged, nothing is re-keyed,
### and a `TITLE-UNVERIFIED` entry is carried as that and not resolved by a seat.
### ### **THE GLOSSARY HAS NO FILE OF ITS OWN AND A FROZEN TWIN**, and both facts are reported.
### ### **NO ENTRY IS REWRITTEN.**
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
import anchor_from_file as AF    # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LIVING = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
FROZEN = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
BIB = os.path.join(PP, 'BIBLIOGRAPHY.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RETIRED_WORDS = re.compile(r'\b(retired|withdrawn|struck|superseded|SCOPE-DROPPED|DEFUNCT)\b', re.I)
RENAMED_WORDS = re.compile(r'\b(renamed|now called|formerly|was titled|retitled|git mv)\b', re.I)
EXTERNAL_KEY = re.compile(r'^(\d{4}\.\d{4,5}|math/\d{6,7}|[a-z]+\.\d+|von Neumann)')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def glossary_terms(path):
    """### the appendix's own entry shape: ### `**Term** — definition`."""
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    rows = txt.split(chr(10))
    start = None
    for i, ln in enumerate(rows):
        if re.match(r'^#+\s*Appendix\s+E\s*:\s*Glossary', ln.strip()):
            start = i
            break
    if start is None:
        return [], None, None
    end = len(rows)
    for j in range(start + 1, len(rows)):
        if re.match(r'^#+\s', rows[j]) and 'Glossary' not in rows[j]:
            end = j
            break
    terms = []
    for j in range(start, end):
        m = re.match(r'^\*\*(.+?)\*\*\s*[-—]', rows[j])
        if m:
            terms.append((m.group(1).strip(), j + 1))
    return terms, start + 1, end


def bib_keys(path):
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    keys = []
    # ### ### **THE KEY IS THE FIRST CELL OF ITS ROW, AND A PATH IS NOT A KEY.** ### The first
    # ### version took ANY wholly-backticked cell, and a row whose THIRD cell is
    # ### `phase1.5/method/THE_CORNER_MAP.md` -- the document that cites the work -- came back as a
    # ### bibliography entry nothing cites. ### **A PREDICATE THAT READS THE WRONG COLUMN INVENTS
    # ### ### ENTRIES**, and it invented one before this guard was written.
    for i, ln in enumerate(txt.split(chr(10)), 1):
        if not ln.lstrip().startswith('|'):
            continue
        cells = ln.split('|')
        if len(cells) < 3:
            continue
        m = re.match(r'^\s*#*\s*\**`([^`]+)`\**\s*$', cells[1])
        if not m:
            continue
        k = m.group(1).strip()
        if k.endswith('.md') or k.endswith('.py') or k.endswith('.lean'):
            continue
        if k and k not in [x[0] for x in keys]:
            keys.append((k, i))
    # ### the TITLE-UNVERIFIED run, which is a paragraph of backticked keys and not a table
    for m in re.finditer(r'`(\d{4}\.\d{4,5}|math/\d{6,7})`', txt):
        k = m.group(1)
        if k not in [x[0] for x in keys]:
            keys.append((k, txt[:m.start()].count(chr(10)) + 1))
    return keys


def cited_elsewhere(needle, files, exclude):
    """### **IS IT STILL THERE UNDER THAT NAME?** ### Whole-phrase, outside its own home file."""
    pat = re.compile(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(needle), re.I)
    hits = []
    for rel, txt in files:
        if rel in exclude:
            continue
        for i, ln in enumerate(txt.split(chr(10)), 1):
            if pat.search(ln):
                hits.append((rel, i, ln.strip()[:130]))
                if len(hits) >= 3:
                    return hits
    return hits


def context_verdict(needle, files, exclude):
    """### RETIRED or RENAMED require the record to SAY so, quoted -- never an inference."""
    pat = re.compile(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(needle), re.I)
    for rel, txt in files:
        if rel in exclude:
            continue
        for i, ln in enumerate(txt.split(chr(10)), 1):
            if not pat.search(ln):
                continue
            if RETIRED_WORDS.search(ln):
                return 'RETIRED', (rel, i, ln.strip()[:150])
            if RENAMED_WORDS.search(ln):
                return 'RENAMED', (rel, i, ln.strip()[:150])
    return None, None


def main():
    rec('=' * 100)
    rec('b374 -- COMPONENT 2: THE GLOSSARY AND THE BIBLIOGRAPHY. ### **CLASSIFIED, NOT REWRITTEN.**')
    rec('=' * 100)
    rec('')
    rels = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    files = []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            files.append((rel, io.open(p, encoding='utf-8', errors='replace').read()))
        except OSError:
            continue
    rec('  ### the record searched : %d tracked markdown files' % len(files))
    rec('  ### ### **THE FOUR WORDS, AND NO FIFTH:** ### CURRENT / RENAMED / RETIRED / NOT LOCATED.')
    rec('  ### ### **RETIRED AND RENAMED REQUIRE THE RECORD TO SAY SO, QUOTED.** ### An inference from')
    rec('  ### ### absence is `NOT LOCATED`, which is the weaker word and says so.')

    # ---------------------------------------------------------------- THE GLOSSARY
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE GLOSSARY. ### **IT HAS NO FILE OF ITS OWN AND IT HAS A FROZEN TWIN.**')
    rec('-' * 100)
    n_liv, l_start, l_end = glossary_terms(LIVING)
    n_fro, f_start, f_end = glossary_terms(FROZEN)
    rec('    the living appendix : `day1/A_Place_to_Stand.md` lines %s-%s, %d entries'
        % (l_start, l_end, len(n_liv)))
    rec('    the frozen twin     : `outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md` lines %s-%s, %d entries'
        % (f_start, f_end, len(n_fro)))
    liv_set = set(t for t, _ in n_liv)
    fro_set = set(t for t, _ in n_fro)
    only_liv = sorted(liv_set - fro_set)
    only_fro = sorted(fro_set - liv_set)
    rec('    ### ### **DIVERGENCE BETWEEN THE LIVING AND THE FROZEN: %d only-living, %d only-frozen.**'
        % (len(only_liv), len(only_fro)))
    if only_liv:
        rec('      only in the living document : %s' % only_liv)
    if only_fro:
        rec('      ### **ONLY IN THE DEPOSIT** : %s' % only_fro)
    rec('    ### **THE FROZEN TWIN IS READ AND NOT EDITED.**')
    rec('')
    gl = []
    home = {'day1/A_Place_to_Stand.md', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md'}
    for term, ln in n_liv:
        hits = cited_elsewhere(term, files, home)
        if hits:
            v, ev = 'CURRENT', hits[0]
        else:
            v, ev = context_verdict(term, files, set())
            if v is None:
                v, ev = 'NOT LOCATED', None
        gl.append(dict(term=term, line=ln, verdict=v, evidence=ev))
    tally = {}
    for g in gl:
        tally[g['verdict']] = tally.get(g['verdict'], 0) + 1
    rec('    ### ### **THE GLOSSARY, %d ENTRIES : %s**' % (len(gl), tally))
    for g in gl:
        if g['verdict'] != 'CURRENT':
            rec('      %-44s %-12s %s' % (g['term'][:44], g['verdict'],
                                          (g['evidence'][0] + ':' + str(g['evidence'][1]))
                                          if g['evidence'] else ''))
            if g['evidence']:
                rec('          | %s' % g['evidence'][2])
    rec('    ### **AND THE `CURRENT` ONES ARE NOT LISTED INDIVIDUALLY** -- a term still in use is not a')
    rec('    ### finding, and printing 60 of them would bury the %d that are not.'
        % (len(gl) - tally.get('CURRENT', 0)))

    # ---------------------------------------------------------------- THE BIBLIOGRAPHY
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE BIBLIOGRAPHY. ### **THE EXTERNAL CLASS IS SEPARATED FIRST.**')
    rec('-' * 100)
    keys = bib_keys(BIB)
    rec('    entries parsed from the register : %d' % len(keys))
    ext = [(k, ln) for k, ln in keys if EXTERNAL_KEY.match(k)]
    rec('    ### ### **OF THOSE, POINTING AT AN EXTERNAL WORK : %d**' % len(ext))
    rec('    ### ### **AN EXTERNAL WORK IS NOT EXPECTED TO LIVE IN THIS RECORD AT ALL**, so the')
    rec('    ### ### in-record test is stated for what it is: ### **IS THE ENTRY STILL CITED UNDER THAT')
    rec('    ### ### KEY.** ### That is a fact about the record and is answerable; `does the paper still')
    rec('    ### exist` is not this act`s question and is not asked.')
    rec('')
    bl = []
    bhome = {'BIBLIOGRAPHY.md'}
    for k, ln in keys:
        hits = cited_elsewhere(k, files, bhome)
        if hits:
            v, ev = 'CURRENT', hits[0]
        else:
            v, ev = context_verdict(k, files, bhome)
            if v is None:
                v, ev = 'NOT LOCATED', None
        bl.append(dict(key=k, line=ln, external=bool(EXTERNAL_KEY.match(k)),
                       verdict=v, evidence=ev))
    btally = {}
    for b in bl:
        btally[b['verdict']] = btally.get(b['verdict'], 0) + 1
    rec('    ### ### **THE BIBLIOGRAPHY, %d ENTRIES : %s**' % (len(bl), btally))
    nl = [b for b in bl if b['verdict'] == 'NOT LOCATED']
    rec('    ### **CITED NOWHERE IN THE CORPUS BUT THE REGISTER ITSELF : %d**' % len(nl))
    for b in nl:
        rec('      %-24s line %-6d external : %s' % (b['key'][:24], b['line'], b['external']))
    rec('    ### ### **AND THAT IS A FINDING ABOUT THE REGISTER, NOT ABOUT THE WORK.** ### A reference')
    rec('    ### nothing cites is a reference the corpus carries and does not use.')
    rec('    ### **NO ENTRY WAS MERGED, RE-KEYED, RESOLVED OR REWRITTEN.**')
    rec('    ### **AND NO `TITLE-UNVERIFIED` ENTRY WAS GIVEN A TITLE BY THIS SEAT.**')

    rec('')
    rec('=' * 100)
    rec('  ### ### **NO FIFTH WORD WAS USED. ### NO ENTRY WAS REWRITTEN. ### THE FROZEN TWIN WAS READ')
    rec('  ### ### AND NOT EDITED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b374_entries_notes', LINES)
    io.open(os.path.join(D, 'b374_entries.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(files=len(files),
                        glossary=dict(living_lines=[l_start, l_end], frozen_lines=[f_start, f_end],
                                      entries=len(gl), tally=tally,
                                      only_living=only_liv, only_frozen=only_fro, detail=gl),
                        bibliography=dict(entries=len(bl), external=len(ext), tally=btally,
                                          not_located=len(nl), detail=bl),
                        fifth_words=0, entries_rewritten=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
