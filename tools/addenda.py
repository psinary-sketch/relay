# -*- coding: utf-8 -*-
"""addenda.py -- THE POST-SEAL ADDENDUM FORMS OF (R177)(3), SHARED BY EVERY SUITE THAT READS THEM (b567).

### ### (g) THE WRITE-LIST ADDENDUM. A sealed face is never edited. A file an act wrote that its (W) list omitted is carried by
### a line, in a bank written after the seal, of the one form
###     WRITE-LIST ADDENDUM: <path>, carried by (Rn)(k)
### accepted ONLY when the cited ruling clause -- read from the act's own banked paste, between `RULING (Rn) BEGIN` and
### `RULING (Rn) END` -- names the file or its class. "Names" is read on the clause's own words: the path's basename, or its
### stem (the basename less its extension), appears there as a whole word, case folded; `licence` and `license` are one class.
### A line of any other shape, a clause that cannot be found, or a clause that does not name the file, is REFUSED and printed.
"""
import re

NL = '\n'
ADD_RE = re.compile(r'^WRITE-LIST ADDENDUM: (\S+), carried by \((R\d+)\)\((\d+)\)\s*$')
CLASSES = ({'licence', 'license'},)


def ruling_text(paste, rn):
    """### the ruling's own text, BEGIN to END; '' when the paste does not carry it."""
    m = re.search(r'^RULING \(' + rn + r'\) BEGIN\s*$(.*?)^RULING \(' + rn + r'\) END\s*$', paste, re.S | re.M)
    return m.group(1) if m else ''


def clause(paste, rn, k):
    """### clause (k) of ruling (Rn): from the line opening `(k) ` to the next line opening `(k+1) ` or the ruling's end."""
    body = ruling_text(paste, rn)
    m = re.search(r'^\(' + str(k) + r'\) (.*?)(?=^\(' + str(int(k) + 1) + r'\) |\Z)', body, re.S | re.M)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def _words(text):
    return set(w.lower() for w in re.findall(r"[A-Za-z0-9_.-]+", text)) | set(w.lower() for w in re.findall(r'[A-Za-z0-9_]+', text))


def names(clause_text, path):
    """### True, with the word found, when the clause names the file or its class; (False, '') otherwise."""
    base = path.replace('\\', '/').split('/')[-1]
    stem = base.rsplit('.', 1)[0] if '.' in base[1:] else base
    words = _words(clause_text)
    for cand in (base.lower(), stem.lower()):
        if cand and cand in words:
            return True, cand
        for cl in CLASSES:
            if cand in cl and words & cl:
                return True, sorted(words & cl)[0]
    return False, ''


def writelist_addenda(text, paste_of):
    """### every line of an addendum bank, read: a list of dicts (line, path, base, rn, k, clause, accepted, why).
    ### `paste_of(rn)` returns the banked paste carrying ruling (Rn), or ''."""
    out = []
    for line in text.split(NL):
        if not line.startswith('WRITE-LIST ADDENDUM'):
            continue
        m = ADD_RE.match(line)
        if not m:
            out.append(dict(line=line, path=None, base=None, rn=None, k=None, clause='', accepted=False, why='LINE NOT OF THE FORM'))
            continue
        path, rn, k = m.groups()
        c = clause(paste_of(rn) or '', rn, k)
        ok, word = names(c, path) if c else (False, '')
        out.append(dict(line=line, path=path, base=path.replace('\\', '/').split('/')[-1], rn=rn, k=int(k), clause=c,
                        accepted=ok, why=('CLAUSE NAMES IT: "%s"' % word) if ok else ('CLAUSE NOT FOUND' if not c else 'CLAUSE DOES NOT NAME IT')))
    return out


def accepted_bases(text, paste_of):
    """### the basenames the accepted addenda carry."""
    return set(a['base'] for a in writelist_addenda(text, paste_of) if a['accepted'])

def paste_reader(data_dir):
    """### `paste_of(rn)` over a relay data directory: the banked paste (`bNNN_ferry.txt`) whose text carries `RULING (Rn) BEGIN`."""
    import glob
    import io
    import os

    def paste_of(rn):
        for p in sorted(glob.glob(os.path.join(data_dir, 'b*_ferry.txt'))):
            t = io.open(p, encoding='utf-8', errors='replace').read().replace('\r\n', NL)
            if ('RULING (%s) BEGIN' % rn) in t:
                return t
        return ''
    return paste_of
