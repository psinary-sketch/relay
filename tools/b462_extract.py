# -*- coding: utf-8 -*-
"""b462_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE REHEARSED RULES ARE TWO, AND BOTH WILL READ A DOCUMENT IN COMPONENT 1 AND 2:**
###   (1) the SENTENCE SPLITTER -- so a cut at an abbreviation is seen before the count;
###   (2) the PROOF-WORD MATCHER -- so a fire on `unproved` or inside a compound is seen too.
### ### **AND THE POPULATION IS RESOLVED FIRST**, because the order names two surfaces the bank
### may not hold, and a census over a population that is short is a census nobody can read.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
OUT = os.path.join(D, 'b462_extract.txt')
NL = chr(10)
L, MISSES = [], []

PROOF = ('proved', 'proven', 'proof', 'proves', 'machine-checked', 'verified',
         'compiled', 'established', 'establishes')
PW = re.compile(r'(?<![A-Za-z])(' + '|'.join(re.escape(w) for w in PROOF) + r')(?![A-Za-z])', re.I)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def split_sentences(text):
    """### **THE SPLITTER, AND WHAT IT PROTECTS AGAINST, SPELLED OUT BEFORE IT RUNS.**
    ### Markdown is not prose: a table row, a heading and a code fence are not sentences, and a
    ### full stop inside `e.g.`, `cf.`, `Thm.`, `No.`, `vs.`, an initial or a decimal is not an end.
    ### ### **SO: fenced code is dropped, the line kind is kept with the sentence, and the cut is
    ### ### made only at `.`/`!`/`?` followed by space and a capital or a bracket.**"""
    out, infence = [], False
    for i, line in enumerate(text.split(NL), 1):
        s = line.strip()
        if s.startswith('```'):
            infence = not infence
            continue
        if infence or not s:
            continue
        kind = ('table' if s.startswith('|') else
                'heading' if s.startswith('#') else
                'quote' if s.startswith('>') else 'prose')
        # ### protect the abbreviations and the decimals before cutting.
        prot = s
        for ab in ('e.g.', 'i.e.', 'cf.', 'Thm.', 'Prop.', 'Lem.', 'Def.', 'Ch.', 'Sec.', 'No.',
                   'vs.', 'et al.', 'Fig.', 'eq.', 'Eq.', 'approx.', 'resp.', 'viz.'):
            prot = prot.replace(ab, ab.replace('.', '\x00'))
        NUL = chr(0)
        prot = re.sub(r'(\d)\.(\d)', lambda m: m.group(1) + NUL + m.group(2), prot)
        prot = re.sub(r'(\b[A-Z])\.', lambda m: m.group(1) + NUL, prot)
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z(\[`*"\u201c])', prot)
        for p in parts:
            p = p.replace('\x00', '.').strip()
            if p:
                out.append((i, kind, p))
    return out


def items(text):
    return [(ln, kind, s, sorted(set(m.group(1).lower() for m in PW.finditer(s))))
            for ln, kind, s in split_sentences(text) if PW.search(s)]


def main():
    rec('=' * 104)
    rec('b462 -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).')
    rec('=' * 104)
    rec('')

    rec('(P1) THE POPULATION, RESOLVED BEFORE IT IS COUNTED.')
    files = sorted(os.listdir(DEP)) if os.path.isdir(DEP) else []
    rec('      the deposit at outputs/DEPOSITED-v1.1.2/ : %d files' % len(files))
    for f in files:
        rec('        %-34s %7d bytes' % (f, os.path.getsize(os.path.join(DEP, f))))
    rec('      ### **TWO OF THE ELEVEN CARRY NO PROSE:** `PAPER_DEPENDENCIES.svg` is a graphic and')
    rec('      ### `FORMATION_ARCHITECTURE.html` is markup. ### They stay in the population and are')
    rec('      ### counted; whether they yield items is a RESULT, not a reason to drop them.')
    rec('')
    rec('      ### ### **THE TWO KERNEL RECORDS` ZENODO DESCRIPTIONS: NOT BANKED.**')
    banked = []
    for ln in io.open(os.path.join(D, 'zenodo_fetch_2026-08-10.jsonl'), encoding='utf-8'):
        ln = ln.strip()
        if ln.startswith('{') and '"doi"' in ln:
            j = json.loads(ln)
            banked.append((j.get('doi'), j.get('version'), len(j.get('description', '') or '')))
    for doi, v, n in banked:
        if doi in ('10.5281/zenodo.21520474', '10.5281/zenodo.21539068'):
            rec('        %-28s %-8s description chars banked : %d' % (doi, v, n))
    rec('        ### the only banked Zenodo DESCRIPTION in the relay is the MONOGRAPH record`s')
    rec('        ### (b359_fetch_F1/F2.json, %d chars). ### **THE KERNEL RECORDS WERE FETCHED FOR'
        % len(json.load(io.open(os.path.join(D, 'b359_fetch_F1.json'), encoding='utf-8'))
              ['metadata'].get('description', '')))
    rec('        ### METADATA ONLY AND THEIR DESCRIPTIONS WERE NEVER BANKED.**')
    rec('      ### **WHAT STANDS IN THEIR PLACE, AND IT IS b455`S OWN PRECEDENT, LABELLED AS A SUBSTITUTE:**')
    kz = git(os.path.join('D:', os.sep, 'SIDE-kernel'), 'show', 'v1.5:.zenodo.json').stdout
    rec('        SIDE-kernel v1.5 `.zenodo.json` description : %d chars  ### PRESENT'
        % (len(json.loads(kz).get('description', '')) if kz.strip() else 0))
    lz = git(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'show', 'v0.10.0:.zenodo.json')
    rec('        SIDE-lv-conservation v0.10.0 `.zenodo.json`  : ### **ABSENT AT THE TAG** (exit %d)'
        % lz.returncode)
    lr = git(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'show', 'v0.10.0:README.md').stdout
    rec('        SIDE-lv-conservation v0.10.0 `README.md`     : %d chars  ### the only surface it has'
        % len(lr))
    rec('      ### ### **SO THE POPULATION IS ELEVEN FILES PLUS TWO LABELLED SUBSTITUTES, AND NEITHER')
    rec('      ### ### SUBSTITUTE IS CALLED A ZENODO DESCRIPTION ANYWHERE IN THIS ACT.**')
    rec('')

    rec('(R70) REHEARSAL 1 AND 2 -- THE SPLITTER AND THE MATCHER, ON THE MONOGRAPH, FIRST TWENTY ITEMS.')
    mono = os.path.join(DEP, 'A_Place_to_Stand.md')
    it = items(read(mono))
    rec('      A_Place_to_Stand.md : %d sentence-items carrying at least one proof word' % len(it))
    rec('')
    for k, (ln, kind, s, ws) in enumerate(it[:20], 1):
        rec('      %2d) %s:%-5d [%-7s] words=%s' % (k, 'A_Place_to_Stand.md', ln, kind, ','.join(ws)))
        rec('          %s' % s[:190])
    rec('')
    rec('      ### **THE TWO FALSE-FIRE SHAPES THE ORDER NAMES, CHECKED EXPLICITLY:**')
    neg = [(ln, s) for ln, kind, s, ws in it if re.search(r'unprove|disprove|not proved|no proof', s, re.I)]
    rec('      ### items also carrying a NEGATED proof word (`unproved`, `disproved`, `not proved`,')
    rec('      ### `no proof`) : %d   ### **THESE ARE NOT FALSE FIRES** -- the matcher is bounded by' % len(neg))
    rec('      ### `(?<![A-Za-z])`, so `unproved` does NOT match `proved`; they are items whose')
    rec('      ### sentence ALSO denies something, and the census counts sentences, not assertions.')
    for ln, s in neg[:4]:
        rec('          %-5d %s' % (ln, s[:150]))
    frag = [s for ln, kind, s, ws in it if len(s) < 25]
    rec('      ### items shorter than twenty-five characters (a splitter cutting too hard) : %d' % len(frag))
    for s in frag[:5]:
        rec('          %r' % s)
    rec('')

    rec('(P3) b455`S FIGURES, LOCATED IN ITS OWN BANK AND NOT RECALLED.')
    b455 = read(os.path.join(D, 'b455_components.txt'))
    for nd in ('yield `exhaust` 20', 'items 20'):
        h = [(i + 1, l.strip()) for i, l in enumerate(b455.split(NL)) if nd in l]
        if h:
            rec('      b455_components.txt:%d | %s' % (h[0][0], h[0][1][:150]))
    b457 = read(os.path.join(D, 'b457_closing.txt'))
    h = [(i + 1, l.strip()) for i, l in enumerate(b457.split(NL)) if 'S 45 items' in l]
    if h:
        rec('      b457_closing.txt:%d | %s' % (h[0][0], h[0][1][:170]))
    else:
        MISSES.append(('P3 the S=45 figure', 'b457_closing.txt', 'S 45 items'))
        rec('      ### MISS : the S = 45 line')
    h = [(i + 1, l.strip()) for i, l in enumerate(b457.split(NL)) if '494' in l]
    if h:
        rec('      b457_closing.txt:%d | %s' % (h[0][0], h[0][1][:170]))
    rec('      ### **AND THE FIGURES ARE b457`S, NOT b455`S** -- the order attributes S = 45 and 494 to')
    rec('      ### b455; they were measured at ### **b457**, Component 3, over a WIDER population (the')
    rec('      ### record`s files, its description, the kernel README and `.zenodo.json`, and')
    rec('      ### SIDE-lv-conservation`s README). ### **PRINTED, NOT RECONCILED.**')
    rec('')

    rec('(P4) THE KERNEL ROSTER, FOR COMPONENT 2`S RESOLUTION.')
    root = 'D:' + os.sep
    ks = sorted(n for n in os.listdir(root)
                if n.startswith('SIDE-') and os.path.isdir(os.path.join(root, n, '.git')))
    rec('      rostered kernels (D:\\SIDE-* with a .git) : %d' % len(ks))
    rec('      ### resolution reads DECLARED NAMES in `.lean` files. ### **AT A PIN WHERE THE CORPUS')
    rec('      ### NAMES ONE, ELSE AT HEAD, AND THE ACT SAYS WHICH FOR EVERY HIT** -- (R8)`s discipline.')
    rec('')

    rec('(P5) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '462'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|next span STARTS AT|runs through', l):
            rec('      ' + l.strip())
    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(dep_files=files, mono_items=len(it), roster=len(ks),
                   negated=len(neg), fragments=len(frag)),
              io.open(os.path.join(D, 'b462_rehearsal.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
