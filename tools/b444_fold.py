# -*- coding: utf-8 -*-
"""b444_fold.py -- THE FOLD, b433 THROUGH b443, AND THE ORIENTATION REFRESH. ### **PURELY ADDITIVE.**
### Every string comes from `b444_fold.json`, whose verdicts were verified in their own banks by exact match.
### Each target file is checked as a true prefix of its HEAD blob before and after; a marker already present
### writes nothing."""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
RUN = os.path.join(D, 'b444_fold_run.txt')
MARK_F = '<!-- b444 the fold: b433-b443, the witness and channel arc -->'
MARK_D = '<!-- b444 orientation refresh: the external-grading arc and the witness and channel arc -->'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def blob(rel):
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:%s' % rel], capture_output=True)
    return (r.stdout or b'').decode('utf-8', 'replace')


def append(path, rel, mark, body):
    before = read(path)
    if mark in before:
        rec('  %-40s ALREADY PRESENT -- nothing written' % rel)
        return 'DUPLICATE'
    hb = blob(rel)
    norm = lambda s: s.replace(chr(13) + NL, NL)
    pre_ok = norm(before).startswith(norm(hb).rstrip(NL))
    new = before.rstrip(NL) + NL + NL + NL.join(body) + NL
    open(path + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(path + '.tmp', path)
    after = read(path)
    ok = pre_ok and norm(after).startswith(norm(before).rstrip(NL)) and after.count(mark) == 1
    rec('  %-40s WRITTEN +%d lines ; working was a true prefix of blob %s ; append-only %s ; mark once %s'
        % (rel, len(after.splitlines()) - len(before.splitlines()), pre_ok, ok, after.count(mark) == 1))
    return 'WRITTEN' if ok else 'READ-BACK FAILED'


def main():
    F = json.loads(io.open(os.path.join(D, 'b444_fold.json'), encoding='utf-8').read())
    C2 = json.loads(io.open(os.path.join(D, 'b444_decorrelation.json'), encoding='utf-8').read())
    if F['verified'] != len(F['rows']):
        rec('  ### A VERDICT STRING IS NOT VERIFIED -- NOTHING WRITTEN.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
        return 1
    s = F['span']
    body = [MARK_F, '',
            '## THE WITNESS AND CHANNEL ARC, b433–b443 — THE FOLD', '',
            '**Eleven acts, by the author’s word. The span is counted three ways and all three are printed:** '
            '`b363_span.py` reads **%s** at the filing act, because its heading pattern matches %d of the %d fold '
            'headings and misses b434’s; its own rule — a span starts at the last fold’s filing act plus one — '
            'gives **%s**, b435–b443; and the order’s span is **%s**, b433–b443, because it also holds **b433**, '
            'which lay after the last folded act and before b434 and was in no fold, and **b434**, the previous '
            'fold’s own filing act. b443’s closing called eleven the record’s convention; that was wrong, and is '
            'corrected here with b443’s bank unedited.'
            % (s['tool'], F['headings_matched'], F['headings'], s['rule'], s['order']), '',
            '### The arc in one statement', '',
            F['one'], '',
            F['cited'], '',
            '### The span, act by act, each verdict verified in its own closing bank', '',
            '| act | subject | its verdict, as its bank prints it | column |', '|:--|:--|:--|:--|']
    for r in F['rows']:
        note = (' — *%s*' % r['note']) if r['note'] else ''
        body.append('| **%s** | %s%s | `%s` | %s |' % (r['act'], r['subject'], note,
                                                     r['verdict'].replace('`', "'").replace('|', '/'), r['column']))
    c = F['columns']
    body += ['',
             '### The three columns, kept apart',
             '',
             '**Statements about the object** — the zeros, ξ, the Euler balance: **%d**. **About the model** — the '
             'instrument’s channels, kernels and families: **%d**. **About the record** — its documents, tools and '
             'grades: **%d**. Three acts were borderline and each is named in its row rather than rounded: b436, '
             'b441 and b442.' % (c.get('OBJECT', 0), c.get('MODEL', 0), c.get('RECORD', 0)),
             '',
             '### Filed with this fold, not done by it',
             '',
             F['work_order'],
             '',
             '*Filed by b444 (relay `data/b444_fold.json`, `data/b444_the_fold.txt`). Nothing above this section was '
             'edited; no grade is conferred by a seat; nothing is claimed about `h2`.*']
    st_f = append(FINDINGS, 'FINDINGS.md', MARK_F, body)

    fnd = read(FINDINGS)
    m = re.search(r'## The external-grading arc — b423 through b432, folded at b434.*?### The arc in one statement\s*\n\s*\n(.+?)\n', fnd, re.S)
    prior_one = m.group(1).strip() if m else None
    rec('  the external-grading arc`s one statement located in its fold : %s' % bool(prior_one))
    dbody = [MARK_D, '',
             '**Orientation refresh — filed b444, 2026-09-12 *(additive)*.** Under `(R31)` a fold refreshes this '
             'digest. **b434 folded an arc and did not refresh it**, so two arcs are added here, each with its fold’s '
             'own one statement quoted:', '',
             '- **b423–b432 — THE EXTERNAL-GRADING ARC**, folded at b434. Its one statement, quoted: %s'
             % (prior_one or '*NOT LOCATED in its fold section; nothing is summarised in its place.*'),
             '- **b433–b443 — THE WITNESS AND CHANNEL ARC**, folded at b444. Its one statement, quoted: %s' % F['one'],
             '',
             '**The governing claim at the head of this document is unchanged by either arc.** `h2` stands where the '
             'deposit left it.']
    st_d = append(DIGEST, 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', MARK_D, dbody)
    rec('  ### FINDINGS %s ; DIGEST %s' % (st_f, st_d))
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if st_f in ('WRITTEN', 'DUPLICATE') and st_d in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
