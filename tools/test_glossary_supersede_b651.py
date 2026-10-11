# -*- coding: utf-8 -*-
"""test_glossary_supersede_b651.py -- THE PLANTED TEST OF tools/chain_page.py's marked supersession, under (R261)(3)(a).

###   (1) the shared glossary as it stands reads the same entries through the edited reader as through b638's reader (written here);
###   (2) a planted glossary with no mark: the same;
###   (3) a planted mark `# SUPERSEDES ENTRY 2: beta` drops entry 2 alone, the order of the rest kept;
###   (4) a mark naming entry 2 by another name is refused (ValueError);
###   (5) a mark past the last entry is refused;
###   (6) the three HINGE entries of b644 still print from the shared glossary.
### Temporary files only; nothing in a repository is written. Usage: python tools/test_glossary_supersede_b651.py
"""
import io
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as CP   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def b638_reader(path):
    out = []
    for raw in io.open(path, encoding='utf-8'):
        line = raw.rstrip('\n').rstrip('\r')
        if not line.strip() or line.startswith('#'):
            continue
        out.append(tuple(x.strip() for x in line.split('\t')))
    return out


def planted(lines):
    fd, p = tempfile.mkstemp(suffix='.txt')
    os.close(fd)
    io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    return p


def raises(p):
    try:
        CP.glossary_entries(p)
        return False
    except ValueError:
        return True


BASE = ['# a planted glossary', 'alpha\tthe first\tsrc :1', 'beta\tthe second\tsrc :2', 'gamma\tthe third\tsrc :3']
R = []
shared = os.path.join(ROOT, 'data', 'glossary.txt')
marked = any(l.startswith('# SUPERSEDES ENTRY ') for l in io.open(shared, encoding='utf-8'))
want1 = b638_reader(shared)
if marked:
    want1 = [e for i, e in enumerate(want1, 1) if not any(l.startswith('# SUPERSEDES ENTRY %d: ' % i) for l in io.open(shared, encoding='utf-8'))]
R.append(('(1) the shared glossary through the edited reader: as b638`s reader, less only its marked entries (marks %s)' % marked,
          CP.glossary_entries(shared) == want1))
p2 = planted(BASE)
R.append(('(2) a planted glossary with no mark reads as b638`s reader', CP.glossary_entries(p2) == b638_reader(p2)))
p3 = planted(BASE + ['# SUPERSEDES ENTRY 2: beta'])
R.append(('(3) a mark drops entry 2 alone, the order kept', [e[0] for e in CP.glossary_entries(p3)] == ['alpha', 'gamma']))
R.append(('(4) a mark naming entry 2 by another name is refused', raises(planted(BASE + ['# SUPERSEDES ENTRY 2: gamma']))))
R.append(('(5) a mark past the last entry is refused', raises(planted(BASE + ['# SUPERSEDES ENTRY 9: beta']))))
R.append(('(6) the three HINGE entries still print from the shared glossary', sum(1 for e in CP.glossary_entries(shared) if e[0] == 'HINGE') == 3))
for d, ok in R:
    print('  %-104s %s' % (d, 'PASS' if ok else '### FAIL'))
n = sum(1 for _d, ok in R if ok)
print('### ### **%d of %d cases as wanted -- %s**' % (n, len(R), 'PASS' if n == len(R) else 'FAIL'))
sys.exit(0 if n == len(R) else 1)
