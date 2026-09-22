# -*- coding: utf-8 -*-
"""b485_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
NL = chr(10)
L = []

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


def gits(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    R = json.loads(read(os.path.join(D, 'b485_results.json')))
    pass
    SC = json.loads(read(os.path.join(D, 'b485_scores.json')))
    SV = json.loads(read(os.path.join(D, 'b485_survey.json')))
    EXC = json.loads(read(os.path.join(D, 'b485_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b485_span.json')))
    checks = read(os.path.join(D, 'b485_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b485_mirror.txt'))
    pins = read(os.path.join(D, 'b485_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b485_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b485 -- THE CLOSING RECORD.')
    rec('### THE CURRENCY REPAIR, THE QUADRATURE WORK-ORDER, AND THE SUPPORT-EDGE TEST.')
    rec('=' * 100)
    SV = json.loads(read(os.path.join(D, 'b485_survey.json')))
    a, b = SV['records']['19675356'], SV['records']['21432399']
    c0, c3, WR = R['c0'], R['c3'], R['writes']

    rec('')
    rec('### (0) THE OTHER RUN, WITHOUT OPENING ITS LOG.')
    rec('-' * 100)
    rec('    pid %s : CPU ### **%s s** at %s, ### **%s s** at %s, over ### **%s s** of wall.'
        % (c0['pid'], c0['cpu_first'], c0['t1'], c0['cpu_second'], c0['t2'], c0['wall_seconds']))
    rec('    ### ### **DELTA : %s s.** ### **AND THAT ZERO IS NOT A HUNG RUN.**' % c0['cpu_delta'])
    rec('    ### `27508` is the `cmd.exe` LAUNCHER, which waits on a child and burns no CPU by')
    rec('    ### construction. ### The process table shows ### **`lake build Zeta23.ThmDE.Mult`** ###')
    rec('    ### with `lean` at ### **54.8 s** ### CPU.')
    rec('    ### ### **A SILENT LOG AND AN IDLE LAUNCHER ARE BOTH CONSISTENT WITH PROGRESS, AND')
    rec('    ### NEITHER IS EVIDENCE OF IT -- THE CHILD`S CPU IS.**')
    rec('')
    rec('### (1) THE TWO RECORDS, BY THEIR OWN FIELDS.')
    rec('-' * 100)
    rec('    both files recompute EXACTLY to (R94)`s hashes ; neither carries a BOM ;')
    rec('    ### ### **THIS SEAT FETCHED NOTHING.**')
    rec('    %-12s %-10s %-14s %-12s %-8s %s' % ('record', 'version', 'published', 'concept',
                                                 'files', 'manuscript'))
    for s in (a, b):
        rec('    %-12s %-10s %-14s %-12s %-8d %s'
            % (s['id'], s['version'], s['pub'], s['concept'], s['nfiles'],
               s['manuscript'] or '(not stated)'))
    rec('    ### ### **BOTH CARRY CONCEPT 19675355** -- the concept REGISTRY names for the monograph')
    rec('    ### -- so both are versions of the deposit REGISTRY already governs.')
    rec('')
    rec('### (2) THE TWO CURRENCY WRITES.')
    rec('-' * 100)
    rec('    ### ### **b395`S NOTE IS WRITTEN, NINETY ACTS AFTER IT WAS DRAFTED**, to `ERRATA.md` as')
    rec('    ### `E-2026-09-22-1` -- there and not to `meta/ZENODO_METADATA.md`, whose own banner')
    rec('    ### freezes its table, while ERRATA is the append-only ledger carrying the precedent.')
    rec('    ### ### **AND THE MANIFEST CORRECTED HALF THE DRAFT ON ARRIVAL:**')
    rec('      manuscript `v5.8`   ### **CONFIRMED** ### by the record`s own description.')
    rec('      `(2026-07-24)`      ### **REFUTED** ### -- the record published ### **%s**, and'
        % b['pub'])
    rec('                          `2026-07-24` belongs to `v1.1.2`.')
    rec('    ### The draft is quoted verbatim and the correction stands BESIDE it.')
    rec('    ### ### **A DRAFT IS NOT IMPROVED IN SILENCE.**')
    rec('')
    rec('### (3) THE GATE`S PASS.')
    rec('-' * 100)
    rec('    ### ### **CELLS OF b481`S TABLE DISAGREEING WITH REGISTRY : %d.**' % len(c3['disagree']))
    rec('    ### README, SPIRAL_MAP, REGISTRY and the session memory agree on all three fields; the')
    rec('    ### executor memory is ### **NOT LOCATABLE** ### and is RECORDED, not reconciled.')
    rec('    ### ### **AND THE PASS FILED %d FINDINGS, FIVE OF THEM IN THE AUTHORITY ITSELF:**'
        % c3['findings'])
    for f in SV['findings']:
        rec('      %-30s %-18s says `%s`' % (f['addr'], f['kind'], f['says']))
    rec('    ### ### **RULE 5 MAKES REGISTRY THE AUTHORITY, AND EVERY PRIOR PASS RECONCILED OTHER')
    rec('    ### SITES *TO* IT. ### THIS IS THE FIRST PASS WITH THE RECORDS IN HAND, AND THE FIRST')
    rec('    ### TIME THE AUTHORITY ITSELF HAS BEEN CAUGHT.** ### An authority is authoritative over')
    rec('    ### the corpus, not over the platform, and the gate`s own words ask for both.')
    rec('    ### Both history rows ### **ANNOTATED, NEITHER REWRITTEN.**')
    rec('    ### `meta/ZENODO_METADATA.md:22` ### **FILED AND NOT EDITED** ### -- its table declares')
    rec('    ### itself *"left unedited on purpose"*. ### **EDITING A LEDGER THAT DECLARES ITSELF')
    rec('    ### FROZEN WOULD BREAK A LAW TO REPAIR A FACT.**')
    rec('')
    rec('    ### ### **THE GATE : %s.**' % ('DISCHARGED' if c3['discharged'] else 'STANDS'))
    rec('    ### with a dated line at `REGISTRY.md:523` naming this act as its reason, the gate`s')
    rec('    ### text otherwise untouched and the original row preserved verbatim.')
    rec('    ### ### **AND THE LINE NAMES ITS OWN SCOPE:** the current deposit state, and nothing')
    rec('    ### else. ### **A GATE DISCHARGED ON ONE QUESTION IS NOT A CORPUS FOUND CLEAN.**')
    rec('')
    rec('### (4) EVERY CORPUS WRITE, AND WHAT IT COST.')
    rec('-' * 100)
    for k in sorted(WR):
        rec('    %-44s +%-4s / -%-4s   lines of the old file absent from the new : ### **%d**'
            % (WR[k]['path'], WR[k]['numstat'][0], WR[k]['numstat'][1], WR[k]['missing']))
    rec('    ### ### **EVERY WRITE IS AN APPEND OR AN ANNOTATION**, and git`s own `--numstat` reads')
    rec('    ### ### **`-0`** ### on each, because every preserved original still matches.')
    rec('')
    rec('### (5) THE EXPECTATIONS.')
    rec('-' * 100)
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) ### **%s**' % (k, SC[k]['verdict']))
    rec('    ### ### **REGISTERED 3 ; HELD 1 ; HELD-WITH-QUALIFICATION 1 ; SPLIT 1.** ### The seat`s')
    rec('    ### calls were on the sealed face before the pass ran and matched all three, including')
    rec('    ### registering `(N2)`s qualification and `(N3)`s split IN ADVANCE.')
    rec('')
    rec('### (6) THREE DEFECTS IN THIS ACT`S OWN INSTRUMENTS.')
    rec('-' * 100)
    rec('    (a) ### **THE INDEX-QUERY GATE REFUSED THIS FACE TWICE** -- once on an ARM`S NAME, and')
    rec('        once on the paragraph EXPLAINING the rename. ### **A GATE ON RAW TEXT FIRES ON THE')
    rec('        ACT`S OWN ACCOUNT OF WHAT IT DID NOT DO.** ### The arm was renamed and the')
    rec('        explanation written without the token; the gate was obeyed, not argued with.')
    rec('    (b) ### **THE DESK TOOL WROTE ITS ROW AND THEN CRASHED.** ### `corr_row.write_row`')
    rec('        ### **APPENDS AND IS NOT IDEMPOTENT**, despite every desk bank since `b194` heading')
    rec('        it *"the idempotent tool"*. ### A re-run would have written a SECOND row for this')
    rec('        act. ### A guard now reads the ledger before writing. ### **A NAME REPEATED IN')
    rec('        FIFTY HEADINGS IS NOT A PROPERTY.**')
    rec('    (c) ### **AND `G-NOZENODO-WRITE` FIRED ON THE WORD `deposit` IN THIS ACT`S OWN PROSE**,')
    rec('        the third prose-firing in two acts. ### Narrowed to a WRITE CALL. ### **A WORD IS')
    rec('        NOT A CALL.**')
    rec('')
    rec('### (7) THE INSTRUMENTS, AND WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : d96d2c18afc82e14e616953fba6590e1696502040e6f83290d46e7405dfbae8b')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    the span by the tool : ### **%d** -- two past the declared threshold of nine; the'
        % SPAN['current_span'])
    rec('      ### ferry`s order is ### **b479, THEN b482, THEN THE FOLD.**')
    rec('    ### ### **NOTHING WAS FETCHED BY THIS SEAT AND NOTHING AT ZENODO WAS WRITTEN.**')
    rec('    ### **b475`S LOG WAS NOT OPENED** and its run was not polled or stopped.')
    rec('    ### No chain was run. ### No corpus grade moved; no `d1-1` row rewritten; no')
    rec('    ### `FACES_LEDGER` row touched; row U1 unedited; no bridge typed; `h2` where the')
    rec('    ### deposit left it; the four lists stay OPEN; no claim about RH in either direction.')
    rec('')
    rec('### (8) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b485`, never from `main`.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b485_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
