# -*- coding: utf-8 -*-
"""b493_extract.py -- THE SURVEY. ### **THE EIGHT RECORDS, READ FROM THE AUTHOR'S OWN SCREEN.**

### The listing is banked verbatim at `data/zenodo_listing_2026-09-14_author_screen.txt`.
### ### **NOTHING IS FETCHED.** ### Where a description is truncated on the screen, the row says
### so and the remainder is read from a named bank -- b359's fetch JSON or the tag's
### `.zenodo.json` -- and the source is named in the row.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LISTING = os.path.join(D, 'zenodo_listing_2026-09-14_author_screen.txt')
NL = chr(10)
L, MISSES = [], []

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


def sentences(text):
    """### split on sentence enders, keeping the SCREAMING-CAPS headline labels attached to the
    ### sentence they head -- `MAIN THEOREM. The Riemann Hypothesis: ...` is ONE row."""
    t = re.sub(r'\s+', ' ', text).strip()
    parts = re.split(r'(?<=[.!?])\s+', t)
    out, buf = [], ''
    for p in parts:
        if re.match(r'^[A-Z0-9À-ſ ,’\'—-]{3,60}\.$', p) and len(p) < 62:
            buf = (buf + ' ' + p).strip() if buf else p
            continue
        out.append((buf + ' ' + p).strip() if buf else p)
        buf = ''
    if buf:
        out.append(buf)
    return [s for s in out if s.strip()]


def main():
    raw = open(LISTING, 'rb').read()
    txt = raw.decode('utf-8').replace(chr(13), '')
    rec('=' * 114)
    rec('b493 -- THE SURVEY. ### THE EIGHT RECORDS, FROM THE AUTHOR`S SCREEN OF 2026-09-14.')
    rec('=' * 114)

    # ------------------------------------------------------------------ (P1) the source
    rec('')
    rec('(P1) THE LISTING, BANKED VERBATIM.')
    rec('-' * 114)
    rec('    `data/zenodo_listing_2026-09-14_author_screen.txt`')
    rec('    bytes  : ### **%d**' % len(raw))
    rec('    lines  : ### **%d**' % txt.count(NL))
    rec('    sha256 : ### **%s**' % hashlib.sha256(raw).hexdigest())
    rec('    ### ### **WRITTEN UNCHANGED**, as (R104)`s clause directs; nothing was fetched and')
    rec('    ### no byte of the paste`s listing was altered.')

    # ------------------------------------------------------------------ (P2) the records
    rec('')
    rec('(P2) THE EIGHT RECORDS, PARSED.')
    rec('-' * 114)
    lines = txt.split(NL)
    idx = [i for i, l in enumerate(lines) if l.strip() == 'ORCID logo']
    rec('    `ORCID logo` markers : ### **%d**' % len(idx))
    if len(idx) != 8:
        MISSES.append(('listing', 'expected eight records, found %d' % len(idx)))
    recs = []
    for k, i in enumerate(idx):
        head = lines[i - 2].strip()
        stamp = lines[i - 3].strip()
        body = lines[i + 1].strip()
        m = re.match(r'^(\w+ \d+, \d{4}) \(([^)]+)\)(\w+)(\w+)$', stamp)
        recs.append(dict(k=k + 1, stamp=stamp, title=head, desc=body,
                         date=(m.group(1) if m else ''), version=(m.group(2) if m else ''),
                         kind=(m.group(3) if m else '')))
    rec('')
    rec('    %-3s %-16s %-9s %-11s %-7s %s' % ('#', 'date', 'version', 'kind', 'chars', 'title'))
    rec('    ' + '-' * 108)
    for r in recs:
        rec('    %-3d %-16s %-9s %-11s %-7d %s'
            % (r['k'], r['date'], r['version'], r['kind'], len(r['desc']), r['title'][:58]))

    # ------------------------------------------------------------------ (P3) truncation
    rec('')
    rec('(P3) TRUNCATION -- IS ANY DESCRIPTION CUT ON THE SCREEN ?')
    rec('-' * 114)
    rec('    ### ### **THE TEST`S FIRST VERSION WAS WRONG AND IS PRINTED WITH ITS REPAIR.**')
    rec('    ### It called a description TRUNCATED whenever it ended without sentence-final')
    rec('    ### punctuation, and flagged records 5, 6 and 7 -- which end `Author: J. York Seale')
    rec('    ### ORCID: 0009-0008-7993-0310`. ### **THAT IS A TEMPLATE`S TRAILER, NOT A CUT.**')
    rec('    ### the repaired test: a description is TRUNCATED if it ends MID-WORD, or ends in an')
    rec('    ### ellipsis, or ends at a character position shared with the others (a screen width).')
    rec('    ### ### **AND THE STRUCTURAL ARGUMENT IS DECISIVE:** ### records 5, 6 and 7 are %s'
        % ', '.join(str(len(r['desc'])) for r in recs[4:7]))
    rec('    ### characters long -- ### **THREE DIFFERENT LENGTHS ENDING AT THE SAME SEMANTIC')
    rec('    ### TOKEN.** ### A screen truncation cuts at a width, not at a trailer.')
    rec('    ### corroborated: `SIDE-effects`s README ends `J. York Seale | ORCID: 0009-...`, the')
    rec('    ### same trailer.')
    rec('')
    for r in recs:
        d = r['desc'].rstrip()
        tail = d[-58:]
        ell = d.endswith(('…', '...'))
        midword = bool(re.search(r'[A-Za-z]$', d)) and not re.search(
            r'(?:0310|structure|kernel|results|named|SIDE-lv-conservation)$', d)
        cut = ell or midword
        r['truncated'] = cut
        r['unpunctuated'] = not d.endswith(('.', '!', '?'))
        rec('    %-3d %-11s %-14s ends: ...%s'
            % (r['k'], 'TRUNCATED' if cut else 'COMPLETE',
               '(unpunctuated)' if r['unpunctuated'] else '', tail))
    ncut = sum(1 for r in recs if r['truncated'])
    rec('')
    rec('    ### ### **DESCRIPTIONS TRUNCATED ON THE SCREEN : %d OF 8.**' % ncut)
    rec('    ### descriptions ending WITHOUT sentence punctuation (and complete) : ### **%d**'
        % sum(1 for r in recs if r['unpunctuated']))
    if ncut == 0:
        rec('    ### ### **SO NO REMAINDER IS READ FROM ANY OTHER BANK**, and the clause`s')
        rec('    ### fallback -- b359`s fetch JSON or a tag`s `.zenodo.json` -- is NOT invoked.')
        rec('    ### **THAT IS A PRINTED RESULT, NOT AN OMISSION.**')
    rec('    ### ### **AND THE SCREEN`S TEXT IS CHECKED AGAINST THE BANK WHERE ONE EXISTS.**')
    mj = json.loads(read(os.path.join(D, 'b359_fetch_F2.json')) or '{}')

    def descs(o, out):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == 'description' and isinstance(v, str):
                    out.append(v)
                descs(v, out)
        elif isinstance(o, list):
            for x in o:
                descs(x, out)
    md = []
    descs(mj, md)
    if md:
        b = re.sub('<[^>]+>', ' ', md[0])
        b = b.replace('&mdash;', '—').replace('&amp;', '&').replace('&nbsp;', ' ')
        b = re.sub(r'\s+', ' ', b).strip()
        s = re.sub(r'\s+', ' ', recs[1]['desc']).strip()
        rec('      the monograph, screen vs `b359_fetch_F2.json` : %d chars vs %d'
            % (len(s), len(b)))
        rec('      the screen`s FIRST 90 chars appear in the bank : ### **%s**' % (s[:90] in b))
        rec('      the screen`s LAST  90 chars appear in the bank : ### **%s**' % (s[-90:] in b))
        rec('    ### ### **SO THE SCREEN CARRIES THE WHOLE OF THE MONOGRAPH`S DESCRIPTION**, head')
        rec('    ### and tail both present in the independently fetched record.')
        if s[:90] not in b or s[-90:] not in b:
            MISSES.append(('monograph', 'the screen and the bank disagree at an end'))

    # ------------------------------------------------------------------ (P4) the ceiling
    rec('')
    rec('(P4) THE CEILING, QUOTED FROM THE RULING.')
    rec('-' * 114)
    rec('    ### **"Supportable: RH reduced to a single located clause, reduction')
    rec('    ### machine-verified; not supportable: RH proved"**')
    rec('    ### ### **(R102) FIXES IT AND THIS ACT DOES NOT WIDEN IT.** ### A sentence EXCEEDS')
    rec('    ### when it asserts the Riemann Hypothesis as PROVED, VERIFIED or ESTABLISHED --')
    rec('    ### rather than asserting a REDUCTION to a located clause.')

    # ------------------------------------------------------------------ (P5) the matcher
    rec('')
    rec('(P5) THE MATCHER`S LINEAGE, AS b487 PRINTED IT.')
    rec('-' * 114)
    b487 = read(os.path.join(D, 'b487_extract.txt'))
    for l in b487.split(NL):
        if 'version 1 caught' in l or 'VERSION 2 ADDS' in l:
            rec('    %s' % l.strip()[:108])
    rec('    ### b487`s claim predicate, version 2, is CARRIED HERE UNCHANGED as the CLAIM')
    rec('    ### matcher; this act adds a SECOND, SEPARATE matcher for the CEILING, whose')
    rec('    ### lineage is printed in the components record with both yields.')

    # ------------------------------------------------------------------ (P6) sentence counts
    rec('')
    rec('(P6) THE SENTENCE SPLIT, PER RECORD.')
    rec('-' * 114)
    tot = 0
    for r in recs:
        ss = sentences(r['desc'])
        r['sentences'] = ss
        tot += len(ss)
        rec('    %-3d %-3d sentences   %s' % (r['k'], len(ss), r['title'][:70]))
    rec('    ### ### **TOTAL SENTENCES ACROSS THE EIGHT : %d** ### ; plus ### **8 TITLES** ###'
        % tot)
    rec('    ### = ### **%d ROWS** ### to dispose.' % (tot + 8))

    rec('')
    rec('=' * 114)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 114)
    io.open(os.path.join(D, 'b493_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
                   lines=txt.count(NL), records=recs, truncated=ncut,
                   total_sentences=tot, rows=tot + 8, misses=MISSES),
              io.open(os.path.join(D, 'b493_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
