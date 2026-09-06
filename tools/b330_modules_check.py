# -*- coding: utf-8 -*-
"""b330_modules_check.py -- THE SEPTEMBER MODULES, MEASURED: SHAPE, PROVENANCE, NO RESEARCH CONTENT.

### ### **`G-NORESEARCH`** ### -- every module and the top-level index swept for the programme's object
### vocabulary; one hit is one failure. ### The list is stated here, in the tool, and a control string
### carrying one term must be reported as a hit.
### ### **`G-SHAPE`** ### -- the four sections in order (WHAT IT DOES; WHEN IT APPLIES; WHAT IT REFUSES;
### PROVENANCE) and the August header's standing sentence on every file.
### ### **`G-PROVENANCE`** ### -- every `relay/tools/<file>` path named in a provenance line exists on disk;
### every act id named exists as a relay data file; every quoted fragment (italic, in double quotes) is a
### substring of a line in the extract file.
### ### **`G-INDEX`** ### -- every module in the top-level index with exactly one family; each new family
### named once in the families paragraph.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TC = r'D:\MY-DOwnloads\TECHNE-Core'
SEP = os.path.join(TC, 'modules', '2026-09')
INDEX = os.path.join(TC, 'modules', 'INDEX.md')
EXTRACT = os.path.join(ROOT, 'data', 'b330_extract_notes.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### the programme's object vocabulary -- a method statement needs none of it
RESEARCH = ['zeta', 'Zeta', 'Riemann', 'Epstein', 'Sonin', 'Weil', 'Connes', 'Consani', 'Lagarias', 'h2', 'M-2',
            'archimedean', 'Archimedean', 'adele', 'adelic', 'p-adic', 'eigenvalue', 'eigenfunction', 'Hilbert',
            'cyclotomic', 'Haar', 'Fourier', 'Mellin', 'prime', 'Prime', 'ξ', 'xi(', 'Li coefficient', 'explicit formula',
            'Ostrowski', 'formation', 'Formation', 'spectral', 'Spectral', 'hypothesis', 'Hypothesis', 'Sfrak', 'S-bar']
HEADER = 'a module states the grade its owning act carries and confers none'
SECTIONS = ['## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE']
FAMILIES_OLD = ['HARNESS_LORE', 'DISCRIMINATOR_PROTOCOL', 'IMPORT_LEDGER']
FAMILIES_NEW = ['VACUITY', 'REGISTRATION', 'READING', 'CERTIFICATION', 'NEGATIVE_CONTROL']


def research_hits(text):
    return [(w, m.start()) for w in RESEARCH for m in re.finditer(re.escape(w), text)]


def shape_ok(text):
    pos = [text.find(s) for s in SECTIONS]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and HEADER in text and text.count(HEADER) == 1


def provenance(text):
    tools = re.findall(r'`relay/tools/([A-Za-z0-9_\-\.\*]+)`', text)
    data = re.findall(r'`relay/data/([A-Za-z0-9_\-\.]+)`', text)
    acts = sorted(set(re.findall(r'\bb(\d{3})\b', text)))
    quotes = re.findall(r'\*"([^"]+)"\*', text)
    return tools, data, acts, quotes


def check_provenance(text, extract):
    tools, data, acts, quotes = provenance(text)
    bad_tools = [t for t in tools if not glob.glob(os.path.join(ROOT, 'tools', t))]
    bad_data = [d for d in data if not os.path.exists(os.path.join(ROOT, 'data', d))]
    bad_acts = [a for a in acts if not glob.glob(os.path.join(ROOT, 'data', 'b%s_*' % a))]
    # ### a quotation wraps lines inside a module; both sides are compared with whitespace collapsed
    ex = re.sub(r'\s+', ' ', extract)
    bad_quotes = [q for q in quotes if re.sub(r'\s+', ' ', q) not in ex]
    return bad_tools, bad_data, bad_acts, bad_quotes, len(tools), len(acts), len(quotes)


def fixtures():
    fires = bool(research_hits('the method computes a zeta value'))
    quiet = not research_hits('the method computes a value at a named input')
    shape_fires = not shape_ok('# x\n## WHAT IT DOES\n## WHAT IT REFUSES\n## WHEN IT APPLIES\n## PROVENANCE\n' + HEADER)
    return fires, quiet, shape_fires


def main():
    fails = []
    print('=' * 100)
    print('b330 -- THE SEPTEMBER MODULES, MEASURED.')
    print('=' * 100)
    f1, f2, f3 = fixtures()
    print('  fixtures: research sweep fires %s / quiet %s ; shape check fires on wrong order %s' % (f1, f2, f3))
    if not (f1 and f2 and f3):
        return 2
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    files = sorted(glob.glob(os.path.join(SEP, '*.md')))
    print('  modules on disk : %d' % len(files))
    idx = io.open(INDEX, encoding='utf-8', errors='replace').read()
    print('\n  %-44s %-6s %-6s %-6s %s' % ('module', 'shape', 'resrch', 'prov', 'tools/acts/quotes'))
    for p in files:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        name = os.path.basename(p)
        sh = shape_ok(txt)
        rh = research_hits(txt)
        bt, bd, ba, bq, nt, na, nq = check_provenance(txt, extract)
        pv = not (bt or bd or ba or bq)
        in_idx = ('`2026-09/%s`' % name) in idx
        fams = re.findall(r'\*\*Family:\*\*\s+([A-Z_]+)', txt)
        ok = sh and not rh and pv and in_idx and len(fams) == 1
        print('  %-44s %-6s %-6s %-6s %d/%d/%d  index %s family %s  %s' % (name[:44], sh, len(rh), pv, nt, na, nq, in_idx, fams, 'PASS' if ok else '### FAIL ###'))
        for w, i in rh[:5]:
            print('      research term %r at %d : %s' % (w, i, txt[max(0, i - 40):i + 40].replace('\n', ' ')))
        for lbl, lst in (('tool missing', bt), ('data missing', bd), ('act missing', ba), ('quote not in extract', bq)):
            for x in lst[:5]:
                print('      %s : %s' % (lbl, x[:100]))
        if not ok:
            fails.append(name)
    rh = research_hits(idx)
    print('\n  INDEX research terms : %d ; every new family named once in the families paragraph : %s' % (len(rh), all(idx.count('**`%s`**' % f) == 1 for f in FAMILIES_NEW)))
    for w, i in rh[:5]:
        print('      research term %r : %s' % (w, idx[max(0, i - 40):i + 40].replace('\n', ' ')))
    rows = re.findall(r'^\| `2026-09/([A-Z_]+\.md)` \| ([A-Z_]+) \|', idx, re.M)
    names = sorted(os.path.basename(p) for p in files)
    rows_ok = sorted(n for n, _f in rows) == names and all(f in FAMILIES_OLD + FAMILIES_NEW for _n, f in rows)
    print('  index rows %d == modules %d, every family known : %s' % (len(rows), len(names), rows_ok))
    aug_link = '`2026-08/INDEX.md` (untouched' in idx
    print('  the August index linked untouched : %s' % aug_link)
    if rh or not rows_ok or not aug_link or not all(idx.count('**`%s`**' % f) == 1 for f in FAMILIES_NEW):
        fails.append('INDEX')
    print('\n  ### MODULES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
