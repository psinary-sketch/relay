# -*- coding: utf-8 -*-
"""b499_record.py -- COMPONENT 3: THE ERRATA ENTRY AND THE NOTES. ### **ON THREE MATCHES ONLY.**

### ### **THE ERRATA ENTRY** goes through `tools/errata_append.py`, IMPORTED and UNEDITED, which
### refuses a duplicate id before it writes. ### ### **THE NOTES** are INSERTED bottom-up at the points
### the face sealed, each named line re-verified byte-unchanged against PLACE-papers `6337cef` first.
### ### **ONE STATED READING:** a line placed directly after a Markdown table row is absorbed into the
### table as a row, so each of the two TABLE-SIDE notes carries ONE leading blank line; the proof
### below counts those blank lines separately and says so.
"""
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import errata_append as EA   # noqa: E402

PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERRATA = os.path.join(PP, 'ERRATA.md')
EID = 'E-2026-09-23-1'
BASE = '6337cef'
NL = chr(10)
L = []
ORDER = ('21539068', '21520474', '21539167')
NAMES = {'21539068': 'SIDE-lv-conservation v0.10.0', '21520474': 'SIDE-kernel v1.5',
         '21539167': 'A Place To Stand (monograph) Zenodo v1.1.2'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    with open(p, 'rb') as fh:
        return fh.read().decode('utf-8')


def dec(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h or ''))).strip()


def git_show(rev, path):
    return subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (rev, path)], capture_output=True,
                          encoding='utf-8', errors='replace').stdout


# ------------------------------------------------------------------------------ the ERRATA block
def errata_block(R, intended):
    c2 = R['c2']['records']
    plan = R['c1']['targets']
    tok = os.environ.get('ZENODO_TOKEN') or ''
    b = []
    b.append('')
    b.append('**`%s` — THE TEN METADATA EDITS AT ZENODO, WRITTEN BY THE SEAT UNDER `(R110)` AND '
             'FETCHED BACK** *(an append; no prior line is edited, the ledger’s own law)*' % EID)
    b.append('')
    b.append('Filed by `b499`, 2026-09-23, on rulings `(R109)`, `(R110)` and `(R111)`. The three '
             'published records below had their **title** and **description** edited through the '
             'legacy deposit API’s edit / PUT / publish sequence — **no new version, no file '
             'touched, no other field changed** — and each was then fetched back **anonymously** and '
             'compared sentence for sentence against the banked replacements: **all three MATCH**. '
             'The input is the author’s `zenodo_edits_2026-09-23_v2.txt`, banked unchanged at '
             '`relay/data/`. The descriptions’ text below is quoted with HTML entities decoded; the '
             'fields’ own bytes are in the banked fetch-backs, whose sha256 are given.')
    b.append('')
    b.append('**The amendments of `(R111)`, with their authority.** Text [5] carries *“five '
             'compiled identifications of σ = 1/2 in five machineries, three of which share one map '
             'under three names”* in place of *“five independent compiled identifications”*, on '
             '`THE_UNCONDITIONAL_SURROUND` §4’s statement-read of 2026-08-09; text [6] states the goal '
             'state’s terminal (`conservation_s_dark`, v1.5) as a stand-in for the clause, in '
             'positive form.')
    b.append('')
    for rid in ORDER:
        c = c2[rid]
        b.append('**Record `%s` — %s** — https://zenodo.org/records/%s — fetch-back sha256 `%s`.'
                 % (rid, NAMES[rid], rid, c['fetchback_sha256']))
        b.append('')
        for p in [x for x in plan if x['record'] == rid]:
            if p['kind'] == 'title':
                b.append('- [%d] **title** — before: *%s* — after, as fetched: *%s*'
                         % (p['n'], p['old'], c['returned_title']))
            else:
                b.append('- [%d] **description sentence** — before: *%s* — after, as fetched: *%s*'
                         % (p['n'], dec(p['old']), dec(html.escape(p['text'], quote=False))))
        b.append('')
    b.append('The seat’s write is bounded by `(R110)`: from this entry on, the standing line reads '
             '*“nothing at Zenodo written by the seat outside (R110)”*. No mathematical claim is '
             'changed by these edits; `h2` stands where the deposit left it.')
    text = NL.join(b)
    if tok and tok in text:
        raise SystemExit('### THE TOKEN IS IN THE BLOCK -- REFUSED.')
    return b


# ------------------------------------------------------------------------------ the notes
def note(rid, where, title):
    return ('*(Note, `b499`, 2026-09-23, beside `%s`, under ruling `(R110)`: Zenodo record `%s` now '
            'carries the corrected title “%s” — written by the seat, fetched back anonymously, MATCH; '
            'see ERRATA `%s`.)*' % (where, rid, title, EID))


def plan_notes(titles):
    """### ### **THE SEALED POINTS.** ### (file, named line, insert-after line, prefix, blank-first, record)"""
    return [
        ('REGISTRY.md', 77, 77, '', False, '21539167'),
        ('REGISTRY.md', 82, 89, '', True, '21539167'),
        ('REGISTRY.md', 94, 94, '  ', False, '21520474'),
        ('REGISTRY.md', 98, 98, '  ', False, '21539068'),
        ('REGISTRY.md', 414, 414, '', True, '21539167'),
        ('meta/ZENODO_METADATA.md', 8, 11, '> ', False, '21520474'),
        ('meta/ZENODO_METADATA.md', 9, 11, '> ', False, '21539167'),
        ('meta/ZENODO_METADATA.md', 10, 11, '> ', False, '21539068'),
    ]


def main():
    R = json.loads(read(os.path.join(D, 'b499_results.json')))
    intended = json.loads(read(os.path.join(D, 'b499_intended.json')))
    rec('=' * 104)
    rec('COMPONENT 3 -- THE RECORD. ### **ON THREE MATCHES ONLY.**')
    rec('=' * 104)
    if (R.get('c2') or {}).get('matches') != 3:
        rec('    ### ### **NOT THREE MATCHES -- COMPONENT 3 WRITES NOTHING.**')
        return 2
    titles = {rid: R['c2']['records'][rid]['returned_title'] for rid in ORDER}

    # -------------------------------------------------- the named lines, re-verified FIRST
    pts = plan_notes(titles)
    files = sorted(set(p[0] for p in pts))
    cur = {f: read(os.path.join(PP, f)).split(NL) for f in files}
    base = {f: git_show(BASE, f).split(NL) for f in files}
    rec('')
    rec('### (a) THE NAMED LINES, AGAINST PLACE-papers `%s`.' % BASE)
    rec('-' * 104)
    unchanged = True
    for f, named, after, pre, blank, rid in pts:
        same = cur[f][named - 1] == base[f][named - 1]
        same_after = cur[f][after - 1] == base[f][after - 1]
        unchanged = unchanged and same and same_after
        rec('    %-26s :%-4d unchanged %s ; insert after :%-4d (unchanged %s) ; record %s'
            % (f, named, same, after, same_after, rid))
    if not unchanged:
        rec('    ### ### **A NAMED LINE HAS MOVED -- STOP. NOTHING IS WRITTEN.**')
        return 2

    # -------------------------------------------------- the ERRATA entry
    rec('')
    rec('### (b) THE ERRATA ENTRY, THROUGH `errata_append.py` (IMPORTED, UNEDITED).')
    rec('-' * 104)
    block = errata_block(R, intended)
    code, lines = EA.append(ERRATA, EID, block)
    for l in lines:
        rec(l)
    if code != 0:
        rec('    ### ### **THE APPENDER REFUSED -- STOP. NO NOTE IS WRITTEN.**')
        return 2

    # -------------------------------------------------- the notes, bottom-up per file
    rec('')
    rec('### (c) THE NOTES, INSERTED BOTTOM-UP.')
    rec('-' * 104)
    proof = {}
    for f in files:
        path = os.path.join(PP, f)
        raw = open(path, 'rb').read()
        crlf = b'\r\n' in raw
        old = raw.decode('utf-8').replace(chr(13), '').split(NL)
        new = list(old)
        mine = [p for p in pts if p[0] == f]
        # ### same insert point, several notes (ZENODO_METADATA): keep their named-line order.
        groups = {}
        for p in mine:
            groups.setdefault(p[2], []).append(p)
        added_notes = added_blank = 0
        for after in sorted(groups, reverse=True):
            ins = []
            for _, named, _, pre, blank, rid in sorted(groups[after], key=lambda p: p[1]):
                if blank:
                    ins.append('')
                    added_blank += 1
                ins.append(pre + note(rid, '%s:%d' % (f, named), titles[rid]))
                added_notes += 1
            new[after:after] = ins
        out = NL.join(new)
        if crlf:
            out = out.replace(NL, chr(13) + NL)
        with open(path, 'wb') as fh:
            fh.write(out.encode('utf-8'))
        # ### THE PROOF: every prior line present in order; the added lines exactly the notes
        # ### and the blank lines the table-side notes carry.
        it = iter(new)
        kept = all(any(o == n for n in it) for o in old)
        extra = len(new) - len(old)
        proof[f] = dict(kept=kept, lines_before=len(old), lines_after=len(new),
                        added=extra, notes=added_notes, blanks=added_blank,
                        exact=(extra == added_notes + added_blank),
                        sha_before=hashlib.sha256(raw).hexdigest(),
                        sha_after=hashlib.sha256(open(path, 'rb').read()).hexdigest())
        rec('    %-26s lines %d -> %d ; notes %d + leading blanks %d = %d added ; every prior line '
            'kept in order %s' % (f, len(old), len(new), added_notes, added_blank, extra, kept))
    ok = all(v['kept'] and v['exact'] for v in proof.values())
    rec('    ### ### **%s**' % ('NOTES WRITTEN; NO PRIOR LINE EDITED OR REMOVED.' if ok else 'PROOF FAILED.'))
    rec('=' * 104)
    R['c3'] = dict(errata_id=EID, errata_code=code, notes=proof, named_unchanged=unchanged, ok=ok)
    io.open(os.path.join(D, 'b499_results.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(R, indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b499_components_c3.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    print('  written: b499_components_c3.txt')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
