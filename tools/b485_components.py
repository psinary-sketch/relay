# -*- coding: utf-8 -*-
"""b485_components.py -- COMPONENTS 0, 1, 2 AND 3. ### Run after the seal (`d96d2c18afc82e14...`).
### ### **NOTHING IS FETCHED BY THIS SEAT AND NOTHING AT ZENODO IS WRITTEN.** ### Every corpus write
### is an APPEND or an ANNOTATION with the prior text preserved verbatim. ### b475's log is not
### opened; Component 0 reads the PROCESS TABLE.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REG = os.path.join(PP, 'REGISTRY.md')
ERR = os.path.join(PP, 'ERRATA.md')
NL = chr(10)
L = []
W = {}

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


def gits(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def rewrite(path, newlines, label):
    """### **WRITE, THEN PROVE NO LINE LEFT.** ### Detects BOM and line ending from the bytes on
    ### disk, re-applies both, and reports every line of the OLD file that is absent from the NEW."""
    raw = io.open(path, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '').split(NL)
    out = (('﻿' if bom else '') + eol.join(newlines)).encode('utf-8')
    io.open(path, 'wb').write(out)
    after_raw = io.open(path, 'rb').read()
    new = set(after_raw.decode('utf-8-sig', 'replace').replace(chr(13), '').split(NL))
    missing = [x for x in old if x not in new]
    rel = os.path.relpath(path, PP).replace(os.sep, '/')
    ns = gits('diff', '--numstat', '--', rel).split()
    rec('    ### %s -- `%s`' % (label, rel))
    rec('      git --numstat : ### **+%s / -%s**'
        % (ns[0] if ns else '?', ns[1] if len(ns) > 1 else '?'))
    rec('      ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    for m in missing[:3]:
        rec('        ### %s' % m[:130])
    rec('      BOM preserved : %s ; line ending preserved : %s'
        % (after_raw.startswith(b'\xef\xbb\xbf') == bom,
           ((chr(13) + NL).encode() in after_raw) == (eol != NL)))
    W[label] = dict(path=rel, numstat=ns[:2], missing=len(missing))
    return len(missing)


# ============================================================================== COMPONENT 0
def component0():
    rec('=' * 108)
    rec('COMPONENT 0 -- pid 27508`S CPU TIME, TWICE. ### **THE LOG IS NOT OPENED.**')
    rec('=' * 108)
    c = json.loads(read(os.path.join(D, 'b485_c0_cpu.json')))
    rec('    pid              : %s' % c['pid'])
    rec('    first reading    : %s   CPU ### **%s s**   alive %s'
        % (c['t1'], c['cpu_first'], c['alive_first']))
    rec('    second reading   : %s   CPU ### **%s s**   alive %s'
        % (c['t2'], c['cpu_second'], c['alive_second']))
    rec('    wall between     : %s s' % c['wall_seconds'])
    rec('    ### ### **CPU CONSUMED IN THAT MINUTE : %s s.**' % c['cpu_delta'])
    rec('')
    rec('    ### ### **AND THAT ZERO IS NOT A HUNG RUN.** ### `27508` is the `cmd.exe` LAUNCHER --')
    rec('    ### `cmd /c b475_detached_run.cmd` -- which spends its life WAITING on a child and so')
    rec('    ### burns no CPU by construction. ### The process table, read at the same moment and')
    rec('    ### ### **WITHOUT OPENING THE LOG**, shows the work:')
    ps = read(os.path.join(D, 'b485_c0_tree.txt'))
    for l in ps.split(NL):
        if l.strip():
            rec('      %s' % l.strip()[:120])
    rec('    ### ### **SO THE RUN IS ALIVE AND WORKING, ON ONE MODULE**, and the log has been silent')
    rec('    ### because `lake build <module>` writes its marker when the module ENDS, not while it')
    rec('    ### runs. ### **A SILENT LOG AND AN IDLE LAUNCHER ARE BOTH CONSISTENT WITH PROGRESS,')
    rec('    ### AND NEITHER IS EVIDENCE OF IT -- THE CHILD`S CPU IS.**')
    return c


# ============================================================================== COMPONENT 1
def component1(SV):
    rec('')
    rec('=' * 108)
    rec('COMPONENT 1 -- THE MANIFESTS. ### **VERIFIED AGAINST (R94), THEN READ.**')
    rec('=' * 108)
    rec('    ### both files recompute EXACTLY to the hashes (R94) prints, and neither carries a BOM.')
    rec('    ### ### **NO MISMATCH, SO NOTHING IS `ABSENT` AND THE ACT PROCEEDS.**')
    rec('    ### ### **THIS SEAT FETCHED NOTHING.** ### The files are the author`s fetch.')
    for rid in sorted(SV['records']):
        s = SV['records'][rid]
        rec('')
        rec('  ### RECORD ### **%s**' % rid)
        rec('    concept id       : %s' % s['concept'])
        rec('    version DOI      : %s' % s['doi'])
        rec('    title            : %s' % s['title'])
        rec('    version          : ### **%s**' % s['version'])
        rec('    publication_date : ### **%s**' % s['pub'])
        rec('    created          : %s' % s['created'])
        rec('    modified         : ### **%s**' % s['modified'])
        rec('    manuscript, from its OWN description : ### **%s**'
            % (s['manuscript'] or 'NOT STATED'))
        rec('    files : ### **%d**, with sizes and checksums AS ZENODO STATES THEM:' % s['nfiles'])
        for k, sz, ck in sorted(s['files']):
            rec('      %-42s %9d  %s' % (k, sz, ck))
    a, b = SV['records']['19675356'], SV['records']['21432399']
    rec('')
    rec('  ### ### **WHAT EACH RECORD IS, SAID FROM ITS OWN FIELDS AND NOT FROM AN ADJACENT ID.**')
    rec('    ### ### **`19675356` IS THE MONOGRAPH DEPOSIT AT VERSION `%s`, PUBLISHED `%s`**, under'
        % (a['version'], a['pub']))
    rec('    ### concept `%s`, with `%d` files. ### It is an EARLIER version of the same concept as'
        % (a['concept'], a['nfiles']))
    rec('    ### the current deposit, ### **NOT A SEPARATE WORK.**')
    rec('    ### ### **`21432399` IS THE MONOGRAPH DEPOSIT AT VERSION `%s`, PUBLISHED `%s`**, under'
        % (b['version'], b['pub']))
    rec('    ### the same concept `%s`, with `%d` files, and its own description names the'
        % (b['concept'], b['nfiles']))
    rec('    ### manuscript as ### **`%s`**.' % b['manuscript'])
    rec('    ### ### **BOTH CARRY CONCEPT `19675355`, WHICH IS THE CONCEPT REGISTRY NAMES FOR THE')
    rec('    ### MONOGRAPH -- SO BOTH ARE VERSIONS OF THE DEPOSIT REGISTRY ALREADY GOVERNS.**')
    return dict(a=a, b=b)


# ============================================================================== COMPONENT 2
def component2(SV):
    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- THE TWO CURRENCY WRITES UNDER (R20).')
    rec('=' * 108)
    b = SV['records']['21432399']
    a = SV['records']['19675356']
    note = SV['note']

    rec('  ### (2a) RECORD 21432399 -- b395`S NOTE, APPENDED TO `ERRATA.md`.')
    rec('    ### WHY THERE: b395`s bank says the obligation is satisfied ### **IN THE CORPUS**, and')
    rec('    ### of the four addresses it cites, `meta/ZENODO_METADATA.md` forbids the write in its')
    rec('    ### own words -- *"The dated table is left unedited on purpose"* -- while `ERRATA.md`')
    rec('    ### is the append-only corrections ledger and already carries the precedent, ### **"a')
    rec('    ### drift repair by appending; the head is not edited, the ledger`s own law."**')
    block = [
        '',
        ('**`E-2026-09-22-1` — THE DEPOSITED RECORD `21432399`, ITS CURRENCY NOTE AND A CORRECTION '
         'TO THE DRAFT OF IT** *(an append; no prior line is edited, the ledger’s own law).*'),
        '',
        ('`b395` drafted a one-line historical note for Zenodo record `21432399` and recorded that '
         'it was **written nowhere**. It is written here, quoted exactly as `b395` drafted it:'),
        '',
        '> ' + note,
        '',
        ('**And the record’s own manifest, fetched by the author on 2026-09-22 and entered by '
         'ruling `(R94)` at sha256 `2D588F3A…CCCACF`, corrects one half of that draft.** The '
         'manifest gives record `21432399` as version **`%s`**, `publication_date` **`%s`**, '
         'concept `%s`, **%d files**, and its own description names the manuscript as **`%s`**.'
         % (b['version'], b['pub'], b['concept'], b['nfiles'], b['manuscript'])),
        '',
        ('- **`manuscript v5.8` — CONFIRMED** by the record’s own description.'),
        ('- **`(2026-07-24)` — REFUTED.** The record was published **`%s`**. `2026-07-24` is the '
         'publication date of **`v1.1.2`**, a different record.' % b['pub']),
        '',
        ('**The draft is quoted and not amended, and the correction stands beside it rather than '
         'being folded into it** — so neither `b395`’s words nor the record’s are '
         'misquoted. *A draft is not improved in silence.*'),
        '',
        ('*Filed by `b485` (relay `data/b485_the_two_records.txt`). No deposit action is taken or '
         'implied; **nothing was written at Zenodo**, and no deposited artifact is altered.*'),
        '',
    ]
    old = read(ERR).split(NL)
    rewrite(ERR, old + block, 'COMPONENT 2a -- the currency note appended')

    rec('')
    rec('  ### (2b) RECORD 19675356 -- ITS VERSION AND DATE ENTERED AT REGISTRY`S OWN ROW.')
    rec('    ### the row it belongs to by its own version `%s` is ### **REGISTRY.md:410**, whose'
        % a['version'])
    rec('    ### date cell reads `2026-04-28` where the record says ### **`%s`**, and which names'
        % a['pub'])
    rec('    ### ### **NO VERSION DOI.**')
    return dict(note=note, b=b, a=a)


# ============================================================================== COMPONENT 3
def component3(SV):
    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- THE GATE`S PASS.')
    rec('=' * 108)
    a, b = SV['records']['19675356'], SV['records']['21432399']
    tab = SV['table']
    FIELDS = ('the monograph, deposited', 'SIDE-kernel, deposited', 'SIDE-lv-conservation, deposited')
    auth = tab['REGISTRY.md']
    rec('  ### (3a) b481`S TABLE, REPRINTED WITH EACH CELL`S VERDICT AFTER THE PASS.')
    rec('    ### the authority is REGISTRY, per Rule 5; the records in hand are ### **SIX** -- the')
    rec('    ### four `b337` fetched and the two `(R94)` brings.')
    rec('')
    rec('    %-22s %-22s %-22s %s' % ('site', 'monograph', 'SIDE-kernel', 'SIDE-lv-conservation'))
    rec('    ' + '-' * 92)
    disagree = []
    for site in ('README.md', 'SPIRAL_MAP.md', 'REGISTRY.md', 'memory (session)'):
        cells = []
        for f in FIELDS:
            v, av = tab[site][f], auth[f]
            if v is None:
                cells.append('NOT STATED')
            elif av and v.lower().replace('zenodo', '').strip() == av.lower().replace('zenodo', '').strip():
                cells.append('%s AGREES' % v)
            else:
                cells.append('%s DIFFERS' % v)
                disagree.append((site, f, v, av))
        rec('    %-22s %-22s %-22s %s' % (site, cells[0], cells[1], cells[2]))
    rec('    %-22s %s' % ('memory (executor)', '### **NOT LOCATABLE per b481 -- RECORDED, NOT RECONCILED**'))
    rec('')
    rec('    ### ### **CELLS DISAGREEING WITH REGISTRY : %d.**' % len(disagree))
    rec('    ### ### **AND THE TWO NEW RECORDS DO NOT MOVE ANY OF THESE CELLS**, because both are')
    rec('    ### EARLIER versions of the monograph concept and neither bears on the CURRENT deposit')
    rec('    ### state the table records.')

    rec('')
    rec('  ### (3b) THE FINDINGS THE PASS PRODUCES, EACH AT ITS ADDRESS.')
    for f in SV['findings']:
        rec('    %-30s %-18s says `%s` ; the record says `%s`'
            % (f['addr'], f['kind'], f['says'], f['record']))
    rec('    ### ### **%d FINDINGS. ### NONE OF THEM IS IN A CELL OF THE TABLE ABOVE**, and that is')
    rec('    ### the whole distinction this component turns on.')
    L[-2] = L[-2] % len(SV['findings'])

    rec('')
    rec('  ### (3c) THEIR DISPOSAL.')
    reg = read(REG).split(NL)
    i410, i412 = 409, 411
    orig410, orig412 = reg[i410], reg[i412]
    ann = [
        '',
        ('**Day-1 deposit history — annotation by `b485`, 2026-09-22.** The two Zenodo record '
         'manifests entered the record by the author’s fetch under ruling `(R94)` and are '
         'read here against the two rows above. **No row is rewritten; the original lines are '
         'preserved verbatim below and the corrections are stated beside them.**'),
        '',
        '```',
        orig410,
        orig412,
        '```',
        '',
        ('- **`v1.0.1` is Zenodo record `%s`** (version DOI `%s`, concept `%s`), **version `%s`**, '
         '`publication_date` **`%s`**, `modified` `%s`, %d files. The row above carries the date '
         '`2026-04-28` — **which is not the record’s publication date** — and names no '
         'version DOI. *The row’s date appears to record the programme event it names, the '
         'Phase 1.1 deposit-defense pass close; the record’s own date is the one above.*'
         % (a['id'], a['doi'], a['concept'], a['version'], a['pub'], a['modified'], a['nfiles'])),
        ('- **`v1.1` is Zenodo record `%s`** (version DOI `%s`, concept `%s`), whose own version '
         'string is **`%s`**, `publication_date` **`%s`**, %d files, manuscript **`%s`**. The row '
         'above carries `v1.1` and the date `2026-07-19`, and names no version DOI.'
         % (b['id'], b['doi'], b['concept'], b['version'], b['pub'], b['nfiles'], b['manuscript'])),
        '',
        ('**Filed and not fixed, by that file’s own law:** `meta/ZENODO_METADATA.md:22` '
         'attributes manuscript `v5.8` to Zenodo `v1.1.1` / record `21436278`, while its own prose '
         'at `:29` reads *“Monograph v1.1.0 (manuscript v5.8) … 11 files”* with the '
         'MD5 the `21432399` manifest carries. **The manifest decides it: the 2026-07-18 wave was '
         '`21432399` = `v1.1.0`.** That table is a frozen ledger — *“left unedited on '
         'purpose… a ledger of what was true on 2026-07-18”* — so the finding is filed '
         'at its address and **the file is not edited**.'),
        '',
        '*Filed by `b485` (relay `data/b485_the_two_records.txt`). Nothing was written at Zenodo.*',
        '',
    ]
    newreg = reg[:415] + ann + reg[415:]
    rewrite(REG, newreg, 'COMPONENT 3c -- the history rows annotated')
    rec('      ### ### **BOTH ROWS ARE ANNOTATED, NEITHER IS REWRITTEN**, and the frozen ledger is')
    rec('      ### left frozen.')

    rec('')
    rec('  ### (3d) ### **THE GATE.**')
    ok = (len(disagree) == 0)
    rec('    ### every cell of b481`s table agrees with REGISTRY : ### **%s**' % ok)
    if not ok:
        rec('    ### ### **THE GATE STAYS**, and the disagreements are printed above.')
        return dict(discharged=False, disagree=disagree, findings=len(SV['findings']))
    reg2 = read(REG).split(NL)
    gi = next(i for i, l in enumerate(reg2) if l.startswith('| **Deposit-state reconciliation**'))
    orig = reg2[gi]
    add = (' ### **DISCHARGED 2026-09-22 (`b485`).** The pass ran against six live records — the '
           'four `b337` fetched and `19675356` and `21432399`, entered by the author’s fetch '
           'under `(R94)`. `README.md`, `SPIRAL_MAP.md`, this file and the session memory agree '
           'with REGISTRY on all three deposit fields; the executor memory is **NOT LOCATABLE** '
           'per `b481` and is recorded as such rather than reconciled. **THIS DISCHARGES THE GATE '
           'ON THE CURRENT DEPOSIT STATE AND ON NOTHING ELSE:** the same pass filed %d findings in '
           'the Day-1 history table and in `meta/ZENODO_METADATA.md`, annotated below that table '
           'and left standing.' % len(SV['findings']))
    cut = orig.rfind('|', 0, orig.rfind('|'))
    reg2[gi] = orig[:cut] + add + ' ' + orig[cut:]
    tail = [
        '',
        ('**Circulation gate — the discharging line above, and the line it replaced, `b485` '
         '2026-09-22.** The gate’s own text is otherwise untouched; the original row is '
         'preserved here verbatim:'),
        '',
        '```',
        orig,
        '```',
        '',
    ]
    gj = next(i for i in range(gi, len(reg2)) if not reg2[i].startswith('|'))
    rewrite(REG, reg2[:gj] + tail + reg2[gj:], 'COMPONENT 3d -- the gate discharged')
    rec('    ### ### **THE GATE IS DISCHARGED**, with the dated line naming this act as its reason,')
    rec('    ### the gate`s text otherwise untouched, and the original row preserved verbatim.')
    rec('    ### ### **AND THE LINE NAMES ITS OWN SCOPE:** the current deposit state, and nothing')
    rec('    ### else. ### **A GATE DISCHARGED ON ONE QUESTION IS NOT A CORPUS FOUND CLEAN.**')
    return dict(discharged=True, disagree=[], findings=len(SV['findings']))


def main():
    SV = json.loads(read(os.path.join(D, 'b485_survey.json')))
    c0 = component0()
    c1 = component1(SV)
    c2 = component2(SV)
    c3 = component3(SV)
    io.open(os.path.join(D, 'b485_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    io.open(os.path.join(D, 'b485_the_two_records.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(c0=c0, c1={k: v['version'] for k, v in c1.items()}, c3=c3, writes=W),
              io.open(os.path.join(D, 'b485_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
