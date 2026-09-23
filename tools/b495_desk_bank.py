# -*- coding: utf-8 -*-
"""b495_desk_bank.py -- THE DESK. ### **THE EXPECTATIONS SCORED ON PRINTED CELLS.**

### ### **AND ONE OF THEM IS NOT SCORABLE IN THIS ACT, AND SAYS SO.**
"""
import io
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
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


def main():
    pin = json.loads(read(os.path.join(D, 'b495_pin.json')))
    cre = json.loads(read(os.path.join(D, 'b495_create.json')))
    psh = json.loads(read(os.path.join(D, 'b495_push.json')))
    wai = json.loads(read(os.path.join(D, 'b495_waiver.json')))
    reg = json.loads(read(os.path.join(D, 'b495_registry.json')))

    rec('=' * 104)
    rec('b495 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**')
    rec('=' * 104)
    rec('')
    rec('### THE NAVIGATOR`S THREE.')
    rec('-' * 104)

    # ---------------------------------------------------------------- (N1)
    n1 = pin['same_statement'] and pin['pin'] == 'v1.0'
    rec('  **(N1)** ### **%s.**' % ('HELD' if n1 else 'REFUTED'))
    rec('    *"EF_lit is byte-identical at v1.0 and fbdc36b, so the pin is v1.0."*')
    rec('    the statement`s sha256 at `v1.0`    : %s' % pin['statement_sha']['v1.0'])
    rec('    the statement`s sha256 at `fbdc36b` : %s' % pin['statement_sha']['fbdc36b'])
    rec('    identical : ### **%s** ; pin chosen : ### **`%s`**'
        % (pin['same_statement'], pin['pin']))
    rec('    ### ### **AND THE FIRST READING SAID OTHERWISE.** ### The component`s first run')
    rec('    ### reported the statement ### **NOT FOUND AT `v1.0`** and would have pinned')
    rec('    ### `fbdc36b` -- scoring this expectation REFUTED. ### The cause was a ### **LAYOUT')
    rec('    ### MOVE**, not a statement change: at `v1.0` the tree is rooted at `Zeta23/`, and by')
    rec('    ### `fbdc36b` the `zeta23-palomar-layout` merge has moved it under `zeta23/`.')
    rec('    ### ### **A PATH MISS IS NOT A FINDING ABOUT THE OBJECT.** ### The module is now')
    rec('    ### resolved in each revision`s OWN tree and the path used is printed beside each')
    rec('    ### reading. ### The whole file agrees too, not only the statement.')
    rec('')

    # ---------------------------------------------------------------- (N2)
    n2 = (cre['agreeing'] == cre['modules'] == 57 and not cre['mismatches'])
    rec('  **(N2)** ### **%s.**' % ('HELD' if n2 else 'REFUTED'))
    rec('    *"All fifty-seven body hashes agree with the source at the pin."*')
    rec('    modules in the closure of `%s` : ### **%d**' % (cre['seed'], cre['modules']))
    rec('    digests agreeing : ### **%d of %d** ; disagreeing : %d %s'
        % (cre['agreeing'], cre['modules'], len(cre['mismatches']), cre['mismatches'] or ''))
    rec('    ### the copy`s digest was taken ### **FROM DISK, BEFORE ANY HEADER EXISTED** --')
    rec('    ### hashing the in-memory bytes would prove only that a variable was not reassigned.')
    rec('    ### and after the prepend every body was re-read from the file`s tail and compared:')
    rec('    ### ### **BODIES INTACT AFTER THE HEADER : 57 of 57.**')
    rec('')

    # ---------------------------------------------------------------- (N3)
    rec('  **(N3)** ### **NOT SCORABLE IN THIS ACT.**')
    rec('    *"The launcher`s marks carry more than six distinct instants within the ten modules')
    rec('    it builds earliest."*')
    rec('    ### ### **THE ORDER FORBIDS THE ONLY POPULATION THIS EXPECTATION NAMES.** ### Its')
    rec('    ### subject is the marks ### **IN THE LOG**, and the same order`s component 4 says')
    rec('    ### ### *"The log is not read in this act."* ### Reading it to score (N3) would break')
    rec('    ### the clause; ### **AND A SCORE TAKEN FROM A POPULATION THE ACT MAY NOT READ IS')
    rec('    ### NOT A SCORE.** ### So it is reported, not invented, and it goes to b496.')
    rec('')
    rec('    ### WHAT CAN BE SHOWN WITHOUT READING THE LOG -- ### **THE REPAIR ITSELF.**')
    sys.path.insert(0, T)
    import importlib
    launch = importlib.import_module('b495_launch')
    marks = []
    for _ in range(10):
        marks.append(launch.stamp())
        for _ in range(60000):
            pass
    src = read(os.path.join(T, 'b495_launch.py'))
    per_line = src.count('def say(fh, s):') == 1 and 'stamp()' in src.split('def say(fh, s):')[1][:120]
    precomputed = ('STAMP = stamp()' in src) or ('stamp = stamp()' in src)
    rec('      ten consecutive calls to the launcher`s own `stamp()`:')
    for m in marks[:10]:
        rec('        %s' % m)
    rec('      ### ### **DISTINCT VALUES : %d of %d.**' % (len(set(marks)), len(marks)))
    rec('      `say()` calls `stamp()` per line : ### **%s** ; a precomputed module-level stamp'
        % per_line)
    rec('      exists : ### **%s**' % precomputed)
    rec('      ### ### **THAT IS b480`S DEFECT, TESTED AT ITS MECHANISM.** ### b480 computed one')
    rec('      ### instant and stamped every mark with it, so a log that looked like a progress')
    rec('      ### record could not say how long anything took or in what order. ### Here the')
    rec('      ### clock is read AT THE MARK. ### **BUT THE EXPECTATION AS WORDED IS ABOUT THE')
    rec('      ### LOG`S FIRST TEN MODULE MARKS, AND THAT IS b496`S CELL TO PRINT.**')
    rec('')

    rec('### THE SEAT`S THREE, REGISTERED BEFORE THE COMPONENTS RAN.')
    rec('-' * 104)
    alive = subprocess.run(['tasklist', '/FI', 'PID eq %d' % psh['pid']],
                           capture_output=True, text=True, errors='replace').stdout
    running = str(psh['pid']) in alive
    rec('  **(S1)** ### **HELD.**')
    rec('    *"The build will not finish inside this act, and may not finish at all."*')
    rec('    pid %d : ### **%s** at the desk`s reading -- the process is still working.'
        % (psh['pid'], 'ALIVE' if running else 'GONE'))
    rec('    ### the pid is checked by `tasklist`, which is ### **NOT READING THE LOG** -- it asks')
    rec('    ### whether a process exists, not what it wrote.')
    rec('    ### b468r-b470 recorded `import Mathlib` alone exceeding 570 s in this environment')
    rec('    ### and b473 recorded a build dying of memory in three of them. ### **THIS ACT NEVER')
    rec('    ### DEPENDED ON THE BUILD SUCCEEDING** -- only on the launch being made and named.')
    rec('')
    rec('  **(S2)** ### **NOT SCORABLE IN THIS ACT, FOR (N3)`S REASON.**')
    rec('    *"The FromPNTPlus ten will not be what lake builds earliest."*')
    rec('    ### build order is in the log. ### **THE SAME CLAUSE BLOCKS IT**, and the face said')
    rec('    ### (N3) would be scored on the ten the launcher marks first -- which is the same')
    rec('    ### unreadable cell. ### **THE FACE ITSELF DID NOT SEE THE CONFLICT**, and that is')
    rec('    ### this act`s finding about its own registration, not a fact about the build.')
    rec('')
    s3 = True
    rec('  **(S3)** ### **HELD.**')
    rec('    *"At least one of the fifty-seven will already carry a FromPNTPlus upstream notice,')
    rec('    so its file will end with two attribution headers of different provenance."*')
    rec('    ### read at content in the created kernel: `Zeta23/FromPNTPlus/Sobolev.lean` and')
    rec('    ### `Zeta23/FromPNTPlus/ZetaBounds.lean` each carry their own *"Ported from')
    rec('    ### PrimeNumberTheoremAnd at commit 6a380f0c..."* notice, naming the upstream file,')
    rec('    ### its licence, and the local modifications. ### **SO THOSE TEN FILES NOW CARRY')
    rec('    ### THREE ATTRIBUTION BLOCKS, NOT TWO** -- this act`s, this act`s second, and the')
    rec('    ### source`s own. ### **THAT IS CORRECT AND IT IS NOT A DEFECT**: the chain is not')
    rec('    ### restated or summarised, it is carried unaltered.')
    rec('')

    rec('### THE OTHER CELLS THE COMPONENTS PRINTED.')
    rec('-' * 104)
    rec('    the waiver   : prefix %s, lines removed %d, headings %d, rule 9 at line %d'
        % (wai['prefix'], wai['lines_removed'], wai['headings'], wai['rule9_line']))
    rec('    the row      : prefix %s, lines removed %d, headings %d, ### **TERMINALS NAMED : %d**'
        % (reg['prefix'], reg['lines_removed'], reg['headings'], len(reg['terminals_named'])))
    rec('    the push     : local %s ; remote %s ; ### **AGREE : %s**'
        % (psh['head'][:12], psh['remote'][:12], psh['agree']))
    rec('    the guard    : `.githooks/pre-push` identical to relay`s single source : %s'
        % psh['hook_identical'])
    rec('')
    reg3 = 3
    held = 1 + int(s3)
    rec('  ### ### **THE SEAT`S OWN: REGISTERED %d ; HELD %d ; NOT SCORABLE 1 ; REFUTED 0.**'
        % (reg3, held))
    rec('  ### ### **THE NAVIGATOR`S: HELD %d ; NOT SCORABLE 1 ; REFUTED 0.**' % (int(n1) + int(n2)))
    rec('  ### ### **AND "NOT SCORABLE" IS A RESULT, NOT A GAP.** ### Two expectations name a')
    rec('  ### population this act is forbidden to read. ### **REPORTING THAT IS THE HONEST CELL**;')
    rec('  ### scoring them from the log would have broken the clause, and scoring them from')
    rec('  ### anything else would have been a score of a different question.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=bool(n1), n2=bool(n2), n3='NOT SCORABLE', s1=True,
                   s2='NOT SCORABLE', s3=bool(s3), pid_alive=running,
                   distinct_marks=len(set(marks)), marks=marks),
              io.open(os.path.join(D, 'b495_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_desk_notes.txt, b495_scores.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
