# -*- coding: utf-8 -*-
"""b716_keystone.py -- (R326)(5)(iii)-(iv): THE KEYSTONE ITEMS' READINGS AND DIFFS, banked, nothing printed from a file but its bank.

  python -X utf8 tools/b716_keystone.py census     (5)(iv): the 19 names data/b714_pilot.txt (P1) lists with NO PIN STATED, each looked up
                                                   in the census at its edition on PLACE-papers main (phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md,
                                                   read as its blob at main): every census line naming it as a whole word, with the kernels,
                                                   tags and commits on that line; and the census's kernel rows (a kernel with its tag and
                                                   commit) -> data/b716_correspondence_census.txt
  python -X utf8 tools/b716_keystone.py diff       each PLACE-papers file the act edits on main (the (W) list's: Silence :212, ERRATA, the
                                                   day papers' Correspondence rows), its working bytes against its blob at main's HEAD as a
                                                   unified diff -> data/b716_keystone_diffs.txt

Writes only its two banks under relay data/. No git write, no push. The census is read as PLACE-papers' blob at a commit; the relay banks
carry the lines the act cites (the rows' names, kernels and pins), as b714's pilot bank did.
"""
import difflib
import os
import re
import subprocess
import sys
import time

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RELAY, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
NL = '\n'
EDITED = ['day1/Silence_of_Foundations.md', 'ERRATA.md', 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md',
          'day1/Seven_Mechanism_Classes.md', 'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md']
P1_ROW = re.compile(r'^    :(\d+)\s+(\S+)\s+\| NO PIN STATED')
P1_FILE = re.compile(r'^  ### (day1/\S+\.md) -- its Correspondence')
KERNEL = re.compile(r'\bSIDE-[a-z0-9]+(?:-[a-z0-9]+)*\b')
TAG = re.compile(r'(?<![\w.])v\d+(?:\.\d+){1,2}\b')
HEX = re.compile(r'(?<![0-9a-f])[0-9a-f]{7,40}(?![0-9a-f])')


def git(*args):
    r = subprocess.run(['git', '-C', PP] + list(args), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def names_p1():
    """[(file, line, name)] the pilot's NO PIN STATED rows, in its order."""
    out, cur = [], None
    for l in open(os.path.join(D, 'b714_pilot.txt'), encoding='utf-8').read().replace('\r', '').split(NL):
        m = P1_FILE.match(l)
        if m:
            cur = m.group(1)
            continue
        m = P1_ROW.match(l)
        if m and cur:
            out.append((cur, int(m.group(1)), m.group(2)))
    return out


def census_lines(text, name):
    """the census lines naming `name` as a whole word (its last dotted part matched where the name is qualified), each (line, text)."""
    pat = re.compile(r'(?<![\w.])' + re.escape(name) + r'(?![\w])')
    return [(i, l) for i, l in enumerate(text.split(NL), 1) if pat.search(l)]


def census(route_write=True):
    head = git('rev-parse', 'main').strip()
    text = git('show', '%s:%s' % (head, CENSUS)) or ''
    rows = names_p1()
    L = ['b716 -- (R326)(5)(iv): THE 19 NAMES WITH NO PIN, EACH LOOKED UP IN THE CENSUS AT ITS EDITION ON MAIN (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the names: data/b714_pilot.txt (P1), its NO PIN STATED rows ; the census: PLACE-papers %s at main %s (%d lines)' % (CENSUS, head[:8], text.count(NL) + 1),
         '### per name: every census line naming it as a whole word, with the kernels (SIDE-*), tags (vN.N[.N]) and hex runs on that line.',
         '### Written by tools/b716_keystone.py census; the pin each row takes is the seat`s reading of these lines, in data/b716_correspondence_pins.txt.', '']
    found = 0
    for f, ln, name in rows:
        hits = census_lines(text, name)
        found += 1 if hits else 0
        L.append('## %s :%d  %s  -- census lines %d' % (f, ln, name, len(hits)))
        for i, l in hits[:12]:
            L.append('    census :%d  kernels %s ; tags %s ; hex %s' % (i, sorted(set(KERNEL.findall(l))), sorted(set(TAG.findall(l))),
                                                                   sorted(set(HEX.findall(l)))))
            L.append('        %s' % l.strip()[:600])
        if len(hits) > 12:
            L.append('    ... %d more census lines, their numbers: %s' % (len(hits) - 12, [i for i, _l in hits[12:]]))
        L.append('')
    L.append('### ### **NAMES %d ; WITH A CENSUS LINE %d ; WITH NONE %d.**' % (len(rows), found, len(rows) - found))
    p = os.path.join(D, 'b716_correspondence_census.txt')
    if route_write:
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
    print('bank', p)
    print(L[-1])
    return 0


def diff():
    head = git('rev-parse', 'HEAD').strip()
    L = ['b716 -- THE KEYSTONE EDITS ON PLACE-papers MAIN, EACH FILE`S WORKING BYTES AGAINST ITS BLOB AT HEAD %s (%s)' % (
        head[:8], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### --- the file at HEAD, +++ the file as the Edit tool left it ; written by tools/b716_keystone.py diff before the commit.', '']
    n = 0
    for f in EDITED:
        a = (git('show', '%s:%s' % (head, f)) or '').split(NL)
        b = open(os.path.join(PP, *f.split('/')), encoding='utf-8').read().replace('\r', '').split(NL)
        d = list(difflib.unified_diff(a, b, '%s at %s' % (f, head[:8]), '%s edited' % f, lineterm='', n=0))
        if d:
            n += 1
        ws = [(i + 1, repr(x), repr(y)) for i, (x, y) in enumerate(zip(a, b)) if x != y and x.strip() == y.strip()] if len(a) == len(b) else []
        L += ['## %s : %s' % (f, ('%d diff lines' % len(d)) if d else 'UNCHANGED')] + d
        L += ['    WHITESPACE-ONLY CHANGE at :%d : at HEAD %s ; edited %s' % w for w in ws] + ['']
    L.append('### ### **FILES %d ; EDITED %d.**' % (len(EDITED), n))
    p = os.path.join(D, 'b716_keystone_diffs.txt')
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(L) + NL)
    os.replace(p + '.tmp', p)
    print('bank', p)
    print(L[-1])
    return 0


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    sys.exit(census() if r == 'census' else diff() if r == 'diff' else (print(__doc__) or 2))
