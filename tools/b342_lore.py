# -*- coding: utf-8 -*-
"""b342_lore.py -- THE FOLD'S LORE RE-TYPED FROM `TOOL` TO `MODULE`, BY AN APPENDED BLOCK ON FINDINGS.md, NOTHING EDITED
### (registration (D), sealed first).

### ### One block under `<!-- b342 lore retyped -->`, an addendum to the fold's lore section (THE STATED-CLAUSE ARC, b331-b334
### -- THE FOLD): the two lore lines named by their opening words, their `TOOL` typing quoted as the fold left it, and the
### module that now carries each. ### The fold's own lines are not touched; the file must be a true prefix of its blob.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
MARK = '<!-- b342 lore retyped -->'
RUN = os.path.join(D, 'b342_lore_run.txt')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINE_LIKE = '- **A comparator is named with the function it was computed for; a bar sealed against a banked table names the table\u2019s function, and a comparison whose two sides name different functions is refused.**'
LINE_SIGN = '- **A threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.**'
HEAD_TOOL = '**Mechanized by a tool** \u2014 a committed tool of this arc enforces the rule; no module carries it yet, and the next extraction\u2019s desk holds it:'


def blob():
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''


def block(J):
    return ['', MARK, '',
            '### Addendum to the lore of THE STATED-CLAUSE ARC \u2014 filed 2026-09-06 (b342, leg 4 of the sortie b339\u2013b343): the rules typed `TOOL`, re-typed `MODULE`',
            '',
            '*The fold\u2019s lines above are not edited; this block names them and the modules that now carry them. The modules are TECHNE-Core method drafts, private, local, committed at `%s` and NOT PUSHED; they state the grade their owning acts carry and confer none.*' % J['committed'],
            '',
            '| the lore line, as the fold typed it | typed then | carried now by |',
            '|:--|:--|:--|',
            '| *\u201cA comparator is named with the function it was computed for; a bar sealed against a banked table names the table\u2019s function, and a comparison whose two sides name different functions is refused.\u201d* | `TOOL` (`tools/b334_aimmap.py`) | `MODULE` \u2014 `modules/2026-09/LIKE_FOR_LIKE.md` |',
            '| *\u201cA threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.\u201d* | `TOOL` (`tools/b334_aimmap.py`) | `MODULE` \u2014 `modules/2026-09/SIGN_RULE.md`, carrying the b328 refinement (`S_4 = 4 \\|G(c)\\|\u00b2 cos 2\u03c6`, negative exactly when 45\u00b0 < \\|\u03c6\\| < 135\u00b0; b336\u2019s addendum) |',
            '',
            '*The tools still enforce the rules; the modules state them. No grade moved. Filed by b342 (relay `data/b342_the_two_rules_as_modules.txt`).*',
            '']


def main():
    L = []

    def rec(s=''):
        L.append(s)
    rec('=' * 100)
    rec("b342 -- THE FOLD'S LORE RE-TYPED, BY AN APPENDED BLOCK ON FINDINGS.md.")
    rec('=' * 100)
    J = json.load(io.open(os.path.join(D, 'b342_modules.json'), encoding='utf-8'))
    txt = io.open(FINDINGS, encoding='utf-8').read()
    hb = blob()
    present = all(x in txt for x in (LINE_LIKE, LINE_SIGN, HEAD_TOOL))
    rec('  the two lore lines and the TOOL heading present in the file : %s' % present)
    if not J.get('committed'):
        rec('  ### the modules were not committed -- nothing written')
        st = 'NOTHING'
    elif MARK in txt:
        rec('  the mark is already present -- DUPLICATE, nothing written')
        st = 'DUPLICATE'
    elif not present:
        rec('  ### a lore line is not in the file -- REFUSED, nothing written')
        st = 'REFUSED'
    else:
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(block(J))
        open(FINDINGS + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(FINDINGS + '.tmp', FINDINGS)
        st = 'WRITTEN'
    after = io.open(FINDINGS, encoding='utf-8').read()
    pw = after.startswith(txt.rstrip(chr(10)))
    pb = after.replace(chr(13) + chr(10), chr(10)).startswith(hb.replace(chr(13) + chr(10), chr(10)).rstrip(chr(10))) if hb else None
    lines_ok = all(after.count(x) == 1 for x in (LINE_LIKE, LINE_SIGN, HEAD_TOOL))
    rec('  status %s ; mark on disk %d time(s) ; append-only against the working file %s ; against the blob %s ; the fold\'s lines once each and untouched %s ; lines %d -> %d'
        % (st, after.count(MARK), pw, pb, lines_ok, len(txt.splitlines()), len(after.splitlines())))
    ok = st in ('WRITTEN', 'DUPLICATE') and pw and (pb is not False) and lines_ok and after.count(MARK) == 1
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    out = RUN if not os.path.exists(RUN) else RUN.replace('_run.txt', '_rerun.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print(chr(10).join(L))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
