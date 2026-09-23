# -*- coding: utf-8 -*-
"""b487_extract.py -- THE SURVEY. ### **NOTHING IS FETCHED.** ### The three descriptions are read
### from sources already on disk: the monograph's from the record JSON banked at b359 and read by
### the 2026-09-14 act b455; the kernel's from its tag's `.zenodo.json`; lv's from its README at
### `v0.10.0`, per b462's precedent. ### Each is LABELLED WITH ITS SOURCE.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
NL = chr(10)
L, MISSES = [], []

# ### ### **THE CLAIM PREDICATE, FIXED BEFORE THE SEARCH.** ### A sentence asserts a machine check,
# ### a compiled proof, or a verified claim when it says so in those words about THIS work.
# ### ### **VERSION 1 MISSED THE KERNEL'S MOST IMPORTANT SENTENCE.** ### It caught
# ### `compile`/`verified`/`machine-check` and not ### **`proves`** -- so
# ### *"The kernel proves that no off-line zero exists by exhaustively excluding every mechanism
# ### class"* ### scored as no claim at all, when it is exactly the claim `E-2026-09-14-1`
# ### addresses. ### **THE ORDER ASKS FOR A MACHINE CHECK, A COMPILED PROOF, *OR A VERIFIED
# ### CLAIM*, AND A KERNEL SAYING IT *PROVES* SOMETHING IS THE THIRD.** ### Both versions' yields
# ### are printed below.
CLAIM_V1 = re.compile(r'machine.?(?:check|verif)|compil|verified|zero unproved|proof-check|'
                      r'formally (?:verif|proved)|#print axioms|lake build|sorry-free|no axioms',
                      re.I)
CLAIM = re.compile(r'machine.?(?:check|verif)|compil|verified|zero unproved|proof-check|'
                   r'formally (?:verif|proved)|#print axioms|lake build|sorry-free|no axioms|'
                   r'\b(?:kernel|we|it|this work)\b[^.]{0,40}\bproves\b|'
                   r'\bproves that\b|\bcertified\b',
                   re.I)

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
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '')


def descriptions(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'description' and isinstance(v, str):
                out.append(v)
            descriptions(v, out)
    elif isinstance(obj, list):
        for x in obj:
            descriptions(x, out)


def sentences(text):
    t = re.sub('<[^>]+>', ' ', text)
    t = t.replace('&mdash;', '--').replace('&amp;', '&').replace('&nbsp;', ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]


def main():
    rec('=' * 108)
    rec('b487 -- THE SURVEY. ### THREE DESCRIPTIONS READ FROM DISK. ### **NOTHING IS FETCHED.**')
    rec('=' * 108)

    # ------------------------------------------------------------------ (P1) the (R97) targets
    rec('')
    rec('(P1) THE (R97) TARGETS, AT THEIR ADDRESSES.')
    rec('-' * 108)
    err = read(os.path.join(PP, 'ERRATA.md'))
    lines = err.split(NL)
    hits = [(i + 1, l) for i, l in enumerate(lines) if 'E-2026-09-22-1' in l]
    for i, l in hits:
        rec('    ERRATA.md:%-5d %s' % (i, l.strip()[:130]))
    rec('    ### ### **OCCURRENCES : %d.** ### The FIRST (b469, filed earlier) ### **KEEPS THE ID**;'
        % len(hits))
    rec('    ### the SECOND (b485) becomes ### **E-2026-09-22-2** ### by an appended dated line.')
    if len(hits) != 2:
        MISSES.append(('ERRATA.md', 'expected exactly two occurrences'))
    rec('    ### ### **AND `E-2026-09-22-2` MUST NOT ALREADY EXIST:** occurrences : ### **%d**'
        % err.count('E-2026-09-22-2'))
    if err.count('E-2026-09-22-2'):
        MISSES.append(('ERRATA.md', 'E-2026-09-22-2 already present'))
    rec('    the two pointer targets:')
    ot = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    rec('      `OPEN_TRAILS.md` -- b485`s record, heading present : %s'
        % ('### b485 —' in ot))
    rec('      `data/b485_the_two_records.txt` -- present : %s ; bytes %d'
        % (os.path.exists(os.path.join(D, 'b485_the_two_records.txt')),
           len(read(os.path.join(D, 'b485_the_two_records.txt')))))

    # ------------------------------------------------------------------ (P2) the two errata
    rec('')
    rec('(P2) THE TWO ERRATA, IN THEIR OWN WORDS -- THE ONLY SOURCE A REPLACEMENT MAY DRAW ON.')
    rec('-' * 108)
    errata = {}
    for eid in ('E-2026-09-14-1', 'E-2026-09-22-1'):
        i = next((k for k, l in enumerate(lines) if l.startswith('## ' + eid)), None)
        if i is None:
            MISSES.append(('ERRATA.md', eid))
            continue
        j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith('## ')), len(lines))
        body = NL.join(lines[i:j])
        errata[eid] = dict(line=i + 1, body=body)
        rec('')
        rec('  ### **%s** ### -- `ERRATA.md:%d`' % (eid, i + 1))
        rec('      %s' % lines[i].strip()[:150])
        for l in lines[i + 1:min(i + 14, j)]:
            if l.strip() and not l.startswith('##'):
                rec('        %s' % l.strip()[:145])

    # ------------------------------------------------------------------ (P3) the three descriptions
    rec('')
    rec('(P3) THE THREE DESCRIPTIONS, EACH LABELLED WITH ITS SOURCE.')
    rec('-' * 108)
    srcs = []
    # --- the monograph
    mj = json.loads(read(os.path.join(D, 'b359_fetch_F2.json')) or '{}')
    md = []
    descriptions(mj, md)
    srcs.append(dict(rec_id='21539167', what='the monograph, Zenodo v1.1.2',
                     source='relay `data/b359_fetch_F2.json` -- the record`s own fetched JSON, '
                            'banked at b359 and read by the 2026-09-14 act b455',
                     text=md[0] if md else ''))
    if not md:
        MISSES.append(('b359_fetch_F2.json', 'no description'))
    # --- the kernel
    kz = git(KER, 'show', 'v1.5:.zenodo.json')
    try:
        kd = json.loads(kz).get('description', '')
    except Exception:
        kd = ''
        MISSES.append(('SIDE-kernel v1.5:.zenodo.json', 'unparsable'))
    srcs.append(dict(rec_id='21520474', what='SIDE-kernel v1.5',
                     source='`SIDE-kernel` at tag `v1.5`, file `.zenodo.json`', text=kd))
    # --- lv
    lvr = git(LV, 'show', 'v0.10.0:README.md')
    srcs.append(dict(rec_id='21539068', what='SIDE-lv-conservation v0.10.0',
                     source='`SIDE-lv-conservation` at tag `v0.10.0`, file `README.md` '
                            '(b462`s precedent)', text=lvr))
    if not lvr:
        MISSES.append(('SIDE-lv-conservation v0.10.0:README.md', 'empty'))

    found = []
    for s in srcs:
        rec('')
        rec('  ### RECORD ### **%s** ### -- %s' % (s['rec_id'], s['what']))
        rec('      source : %s' % s['source'])
        ss = sentences(s['text'])
        rec('      sentences : %d' % len(ss))
        claims = [(k + 1, x) for k, x in enumerate(ss) if CLAIM.search(x)]
        v1 = [(k + 1, x) for k, x in enumerate(ss) if CLAIM_V1.search(x)]
        extra = [k for k, _ in claims if k not in [j for j, _ in v1]]
        rec('      ### the matcher`s lineage : version 1 caught %d ; version 2 catches %d'
            % (len(v1), len(claims)))
        if extra:
            rec('      ### ### **VERSION 2 ADDS SENTENCE(S) %s** -- caught by `proves` / `certified`'
                % ', '.join(str(x) for x in extra))
        rec('      ### ### **SENTENCES ASSERTING A MACHINE CHECK, A COMPILED PROOF, OR A VERIFIED')
        rec('      ### CLAIM : %d.**' % len(claims))
        for k, x in claims:
            rec('')
            rec('        ### sentence %d of %d' % (k, len(ss)))
            for chunk in [x[i:i + 130] for i in range(0, len(x), 130)]:
                rec('          %s' % chunk)
            found.append(dict(rec_id=s['rec_id'], what=s['what'], source=s['source'],
                              idx=k, total=len(ss), text=x))
        s['n_sentences'] = len(ss)
        s['n_claims'] = len(claims)

    rec('')
    rec('    ### ### **TOTAL SENTENCES ASSERTING A CHECK, ACROSS THE THREE : %d.**' % len(found))
    for s in srcs:
        rec('      %-10s %-38s %d of %d' % (s['rec_id'], s['what'], s['n_claims'],
                                            s['n_sentences']))

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b487_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(errata_hits=[[i, l[:160]] for i, l in hits],
                   errata={k: dict(line=v['line'], body=v['body'][:4000])
                           for k, v in errata.items()},
                   sources=[{k: (v[:400] if k == 'text' else v) for k, v in s.items()}
                            for s in srcs],
                   claims=found, misses=MISSES),
              io.open(os.path.join(D, 'b487_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
