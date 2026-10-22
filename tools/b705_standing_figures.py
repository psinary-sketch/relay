# -*- coding: utf-8 -*-
"""b705_standing_figures.py -- THE FOUR STANDING ARMS' FIGURES AT b705, (R315)(3): W-ORD-README-FIGURE-SCOPE taken up at carry time.

### tools/b703_standing_figures.py (sealed at b703) is IMPORTED and unedited: correspondence(), partners() and pins() are its own, re-exported
### here; readme() is REPAIRED here, the old function left in the sealed tool for the diff (relay data/b705_tool_repairs.txt). THE REPAIR, in
### the order's words (PLACE-papers OPEN_TRAILS :15550): the arm reads the README's currency lines, the lines that state current state, as relay
### data/b702_readme_currency.txt registered them, and not every tag; the dated ceiling appends ("Appended under the author's ruling ...") and
### the deposit note's deposited versions (SIDE-lv-conservation v0.10.0, SIDE-kernel v1.5) are records of their date, EXCLUDED BY THEIR TEXT
### and not by line number:
###   (a) a line opening with the append mark `*(Appended under the author's ruling` is a dated ceiling append -- its tags name the tags of its
###       date by design (b704's (n)) -- and no row of it is a currency row;
###   (a') a line that is none of the registered currency lines (the kernel line "**Kernel:**", the federation line "**Federation:**", the
###       deposit note "**Deposit note" -- data/b702_readme_currency.txt (A), by their text) is a dated record, the ceiling rewords of
###       :113-:115 among them, and no row of it is a currency row;
###   (b) a (kernel, tag) pair named in a "Citable deposit" sentence of the README is a deposited version, frozen by REGISTRY's (R20) rule
###       (data/b702_readme_currency.txt :16-:17), and reads EXCLUDED wherever the README names that pair (the kernel line's "beside SIDE-kernel
###       v1.5" among them); the pair is attributed to the nearest kernel named before the tag on the deposit sentence's line.
### Every other row reads as b703's readme() read it: CURRENT where the tag is the kernel's highest at its remote, STALE otherwise. The figure
### is the count of lines holding a STALE row. `readme(remote, text)` takes the README's text for a control on a mutated copy (the README
### itself is not edited by any control). Written by the Write tool at b705; it writes nothing.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b703_standing_figures as SF   # noqa: E402  ### sealed at b703, imported unedited
import b616_claims as KC0            # noqa: E402  ### the one remote read per repository per run

PP, NL = SF.PP, SF.NL
correspondence, partners, pins, highest_local, faces_kernels = SF.correspondence, SF.partners, SF.pins, SF.highest_local, SF.faces_kernels
README_TAG, README_COUNT, _read, _vkey = SF.README_TAG, SF.README_COUNT, SF._read, SF._vkey
APPEND_MARK = "*(Appended under the author's ruling"
# ### the README's current-state lines as data/b702_readme_currency.txt registers them (its (A) rows, by their text): the kernel line (:15, "**Kernel:**"),
# ### the federation line (:18, "**Federation:**") and the deposit note (:164, "**Deposit note"); every other line carrying a tag is a dated record
# ### (the ceiling rewords and appends of :113-:135, the reconciliation note) and no currency row
CURRENCY_MARKS = ('**Kernel:**', '**Federation:**', '**Deposit note')
DEPOSIT_SENTENCE = re.compile(r'Citable deposits?:.*?(?=\. [A-Z*(]|$)')
KERNEL_NAME = re.compile(r'(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)')
TAG_TOKEN = re.compile(r'(?<![\w.])\*{0,2}`?(v\d+(?:\.\d+)+)`?')


def deposited(lines):
    """the (kernel, tag) pairs the README's own "Citable deposit" sentences name, each tag attributed to the nearest kernel named before it on
    the line; a tag with no kernel before it (the monograph's, Zenodo's) is no kernel pair."""
    out = set()
    for l in lines:
        for seg in DEPOSIT_SENTENCE.findall(l):
            start = l.find(seg)
            for m in TAG_TOKEN.finditer(seg):
                pos = start + m.start()
                ks = [(km.start(), km.group(1)) for km in KERNEL_NAME.finditer(l) if km.start() < pos]
                if ks:
                    out.add((ks[-1][1], m.group(1)))
    return out


def readme(remote=None, text=None):
    """the README's currency rows against each kernel's highest tag at its remote; the dated appends and the deposited versions excluded by
    their text; the figure the stale lines among the currency rows."""
    remote = remote or KC0.remote_refs
    rows = []
    t = (text if text is not None else _read(os.path.join(PP, 'README.md'))).split(NL)
    feds = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    dep = deposited(t)
    for n, l in enumerate(t, 1):
        is_append = l.startswith(APPEND_MARK)
        is_currency = l.startswith(CURRENCY_MARKS)
        for m in README_TAG.finditer(l):
            k, v = m.group(1), m.group(2)
            if is_append:
                rows.append(dict(line=n, kernel=k, cited=v, highest=None, state='EXCLUDED', why='a dated ceiling append (the append mark)'))
                continue
            if not is_currency:
                rows.append(dict(line=n, kernel=k, cited=v, highest=None, state='EXCLUDED', why='not a currency line (data/b702_readme_currency.txt (A): the kernel, federation and deposit-note lines)'))
                continue
            if (k, v) in dep:
                rows.append(dict(line=n, kernel=k, cited=v, highest=None, state='EXCLUDED', why='a deposited version (a Citable deposit sentence)'))
                continue
            if not os.path.isdir('D:/' + k):
                rows.append(dict(line=n, kernel=k, cited=v, highest=None, state='UNREAD', why=None))
                continue
            tags = [r[len('refs/tags/'):] for r in remote('D:/' + k) if r.startswith('refs/tags/') and not r.endswith('^{}')]
            hi = max((x for x in tags if _vkey(x)), key=_vkey, default=None)
            rows.append(dict(line=n, kernel=k, cited=v, highest=hi, state='CURRENT' if hi == v else ('STALE' if hi else 'UNREAD'), why=None))
        for m in README_COUNT.finditer(l):
            rows.append(dict(line=n, kernel='(the count)', cited=m.group(1), highest=str(len(feds)),
                             state='CURRENT' if m.group(1) == str(len(feds)) else 'STALE', why=None))
    stale_lines = sorted(set(r['line'] for r in rows if r['state'] == 'STALE'))
    return len(stale_lines), rows


def all_figures(baseline=None, remote=None, readme_text=None):
    c, cr = correspondence()
    r, rr = readme(remote, readme_text)
    p, pr = partners()
    s, sr = pins(baseline)
    return dict(correspondence=dict(figure=c, papers=cr), readme=dict(figure=r, rows=rr), partners=dict(figure=p, rows=pr),
                pins=dict(figure=s, rows=sr['rows'], federation=sr['federation'], faces=sr['faces'], moved=sr['moved']))
