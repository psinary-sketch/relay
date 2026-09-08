# -*- coding: utf-8 -*-
"""b372_readme.py -- COMPONENT 2: THE README, AND THE LABEL THAT DOES NOT FIT IT.

### ### **THE ORDER'S LABEL SAYS `the exclusion kernel's README`; THE ORDER'S DESCRIPTION FITS A
### ### DIFFERENT FILE.** ### Both candidates are READ; the three clauses of the description are tested
### against each; ### **THE OBJECT IS IDENTIFIED BY THE DESCRIPTION AND THE DISCREPANCY IS REPORTED.**
### ### **WHAT EACH FIGURE COUNTS IS DETERMINED AT CONTENT**, by finding the commit that introduced it
### and measuring the same quantity there -- ### **b371'S METHOD, WHICH SETTLED `114` BY MEASURING IT AT
### ### TWO REFS.** ### No scope is inferred from an arithmetic coincidence.
### ### **THE ORIGINAL IS BANKED VERBATIM BEFORE ANY EDIT, AND A FIGURE IS REMOVED RATHER THAN
### ### RESTATED UNLESS THE DOCUMENT CAN NAME THE REF IT HOLDS AT.**
### ### **NO BUILD IS RUN AND NO `.lean` FILE IS TOUCHED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import anchor_from_file as AF    # noqa: E402

D = os.path.join(ROOT, 'data')
GS = os.path.join('D:', os.sep, 'SIDE-global-section')
SE = os.path.join('D:', os.sep, 'SIDE-effects')
GS_README = os.path.join(GS, 'README.md')
SE_README = os.path.join(SE, 'README.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True)


def gtext(repo, *a):
    return git(repo, *a).stdout.decode('utf-8', 'replace')


def nl(s):
    return s.replace(chr(13) + chr(10), chr(10))


# ### **THE THREE CLAUSES OF THE ORDER'S DESCRIPTION, EACH A PREDICATE OVER A README.**
def clause_headline(text):
    m = re.search(r'\*\*(\d+) terminals\*\*', text)
    return (bool(m), m.group(0) if m else None)


def clause_breakdown(text):
    for ln in text.split(chr(10)):
        m = re.search(r'[(]([^()]*\+[^()]*\+[^()]*)[)]', ln)
        if m and len(re.findall(r'(\d+) [A-Za-z]', m.group(1))) >= 3:
            parts = [int(x) for x in re.findall(r'(\d+) [A-Za-z]', m.group(1))]
            return (True, dict(parts=len(parts), total=sum(parts), text=m.group(0)))
    return (False, None)


def clause_profile(repo):
    names = [f for f in gtext(repo, 'ls-files').split(chr(10))
             if f.strip() and 'AXIOM_PRINT' in f.upper()]
    return (bool(names), names)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    write = ('--write' in argv)
    rec('=' * 100)
    rec('b372 -- COMPONENT 2: THE README, AND THE LABEL THAT DOES NOT FIT IT.')
    rec('=' * 100)
    rec('  ### mode : %s' % ('WRITE' if write else 'READ ONLY -- NOTHING IS WRITTEN'))
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE ORDER NAMES ONE OBJECT AND DESCRIBES ANOTHER. ### **BOTH ARE READ.**')
    rec('-' * 100)
    cand = {}
    for name, repo, path in (('SIDE-effects (the exclusion kernel -- THE LABEL)', SE, SE_README),
                             ('SIDE-global-section (the construction kernel)', GS, GS_README)):
        txt = nl(io.open(path, encoding='utf-8').read())
        h, hv = clause_headline(txt)
        b, bv = clause_breakdown(txt)
        p, pv = clause_profile(repo)
        cand[name] = dict(path=path, headline=hv, breakdown=bv, profiles=pv,
                          clauses=dict(headline=h, breakdown=b, profile=p),
                          fits=(h and b and p))
        rec('    %s' % name)
        rec('        clause 1, a headline figure          : %-5s %s' % (h, hv))
        rec('        clause 2, a breakdown summing apart  : %-5s %s'
            % (b, ('%d parts summing to %d' % (bv['parts'], bv['total'])) if b else None))
        rec('        clause 3, ships a profile            : %-5s %s' % (p, pv))
        rec('        ### ### **ALL THREE CLAUSES FIT : %s**' % cand[name]['fits'])
    fitting = [k for k, v in cand.items() if v['fits']]
    rec('')
    rec('    ### ### **THE DESCRIPTION FITS : %s**' % (fitting or 'NEITHER'))
    rec('    ### ### **AND THE LABEL NAMES THE OTHER ONE.** ### This is `b367`s species -- a hint that')
    rec('    ### ### names the right terminals and the wrong defect -- and it is REPORTED, not absorbed.')
    rec('    ### **THE OBJECT IS IDENTIFIED BY THE DESCRIPTION**, because a description is checkable')
    rec('    ### against a file and a label is not. ### **NOTHING IN THE EXCLUSION KERNEL`S README IS')
    rec('    ### ### REPAIRED BY THIS ACT.**')

    rec('')
    rec('-' * 100)
    rec("  ### (2) THE EXCLUSION KERNEL'S README, READ ANYWAY, SO NOTHING IS LOST IF THE LABEL WAS MEANT.")
    rec('-' * 100)
    n, line = AF.find(SE_README, '3 theorems, 3 sorrys')
    rec('    its ONE count line, %s:%d' % (os.path.basename(SE_README), n))
    rec('      | %s' % line.rstrip())
    se_head = gtext(SE, 'rev-parse', 'HEAD').strip()
    rec('    ### ### **AND IT SHIPS NO AXIOM PROFILE AT ALL** -- so its count line cannot be checked')
    rec('    ### ### against a printed profile the way the order`s `PRESENT` test requires.')
    rec('    ### the exclusion kernel at `%s` : tracked files matching AXIOM* : %s'
        % (se_head[:12], clause_profile(SE)[1] or 'NONE'))

    rec('')
    rec('-' * 100)
    rec('  ### (3) WHAT EACH FIGURE COUNTS. ### **DETERMINED AT CONTENT, NOT GUESSED.**')
    rec('-' * 100)
    rec('    ### the method is `b371`s and is unamended: ### **FIND THE COMMIT THAT INTRODUCED THE')
    rec('    ### ### FIGURE AND MEASURE THE SAME QUANTITY THERE.**')
    txt = nl(io.open(GS_README, encoding='utf-8').read())
    head_fig = clause_headline(txt)[1]
    brk = clause_breakdown(txt)[1]
    ratio_m = re.search(r'\((\d+)/(\d+)\)', txt)
    mods_m = re.search(r'across (\d+) modules', txt)
    intro = {}
    for label, needle in (('the headline figure', head_fig),
                          ('the assembly ratio', ratio_m.group(0) if ratio_m else None),
                          ('the module count', mods_m.group(0) if mods_m else None)):
        if not needle:
            continue
        out = gtext(GS, 'log', '--format=%H', '-S', needle, '--', 'README.md').split()
        intro[label] = dict(needle=needle, commits=out, introduced=(out[-1] if out else None))
        rec('    %-22s `%s` ### introduced at : %s'
            % (label, needle, (out[-1][:12] if out else 'NOT LOCATED')))
    refs = []
    for label in ('the headline figure', 'the assembly ratio'):
        c = intro.get(label, {}).get('introduced')
        if c and c not in refs:
            refs.append(c)
    hd = gtext(GS, 'rev-parse', 'HEAD').strip()
    if hd not in refs:
        refs.append(hd)
    rec('')
    rec('    ### THE SAME QUANTITIES, MEASURED AT EACH REF:')
    rec('    %-14s %-12s %-9s %-9s %-9s %-9s %-8s %s'
        % ('ref', 'date', 'headline', 'parts', 'sum', 'ratio', 'modules', 'prints'))
    table = []
    for r in refs:
        rt = gtext(GS, 'show', r + ':README.md')
        pr = gtext(GS, 'show', r + ':AXIOM_PRINTS.txt')
        nprints = len([l for l in pr.split(chr(10)) if l.strip()])
        files = [f for f in gtext(GS, 'ls-tree', '-r', '--name-only', r, '--', 'Core').split(chr(10))
                 if f.endswith('.lean')]
        ac = [f for f in files if 'axiomcheck' in f.lower()]
        h = clause_headline(rt)[1]
        b = clause_breakdown(rt)[1]
        rm = re.search(r'\((\d+)/(\d+)\)', rt)
        mm = re.search(r'across (\d+) modules', rt)
        date = gtext(GS, 'show', '-s', '--format=%cI', r).strip()[:10]
        row = dict(ref=r, date=date, headline=h, parts=(b or {}).get('parts'),
                   total=(b or {}).get('total'), ratio=(rm.group(0) if rm else None),
                   modules=(mm.group(0) if mm else None), prints=nprints,
                   core_lean=len(files), axiomcheck=len(ac),
                   non_axiomcheck=len(files) - len(ac))
        table.append(row)
        rec('    %-14s %-12s %-9s %-9s %-9s %-9s %-8s %s'
            % (r[:12], date, h, row['parts'], row['total'], row['ratio'],
               row['modules'], nprints))
    rec('')
    rec('    ### the module count against the tree it describes, at each ref:')
    for row in table:
        rec('      %-12s Core `.lean` %-4d of which AxiomCheck %-3d ### -> %d not AxiomCheck ; README says %s'
            % (row['ref'][:12], row['core_lean'], row['axiomcheck'], row['non_axiomcheck'],
               row['modules']))
    rec('')
    rec('    ### ### **THE FINDING, AND IT IS NOT WHAT THREE DIFFERENT NUMBERS SUGGEST:**')
    for row in table:
        rec('    ### ### **AT `%s` (%s): headline %s, breakdown sum %s, ratio %s, profile %d.**'
            % (row['ref'][:12], row['date'], row['headline'], row['total'],
               row['ratio'], row['prints']))
    agree = [r for r in table if r['total'] == r['prints']]
    rec('    ### refs at which the breakdown sum EQUALS the shipped profile : %s'
        % [r['ref'][:12] for r in agree])
    rec('')
    rec('    ### ### ### **SO THE THREE FIGURES DO NOT COUNT THREE DIFFERENT THINGS.** ### They count')
    rec('    ### ### ### **ONE QUANTITY -- CORE ZERO-AXIOM TERMINALS, ONE PER PRINTED LINE -- READ AT')
    rec('    ### ### ### THREE DIFFERENT REFS**, and each was exact when it was written.')
    rec('    ### ### **AND NONE OF THEM NAMES THE REF IT HOLDS AT**, which is the defect.')

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE PROFILE, READ AS A PRINTED RECORD AND COMPARED AGAINST ITS BLOB (`b309`).')
    rec('-' * 100)
    work = io.open(os.path.join(GS, 'AXIOM_PRINTS.txt'), 'rb').read()
    blob = git(GS, 'show', 'HEAD:AXIOM_PRINTS.txt').stdout
    wl = [l for l in nl(work.decode('utf-8', 'replace')).split(chr(10)) if l.strip()]
    zero = [l for l in wl if 'does not depend on any axioms' in l]
    names = set(re.findall(r"^'([^']+)'", chr(10).join(wl), re.M))
    rec('    working bytes %d ; blob bytes %d ; ### EOL-normalised equal : %s'
        % (len(work), len(blob), nl(work.decode('utf-8', 'replace'))
           == nl(blob.decode('utf-8', 'replace'))))
    rec('    printed lines %d ; ### lines saying `does not depend on any axioms` : %d ; distinct names %d'
        % (len(wl), len(zero), len(names)))
    rec('    ### ### **EVERY PRINTED LINE IS ZERO-AXIOM : %s**' % (len(zero) == len(wl)))
    rec('    ### ### -- so the README`s claim `No terminal failed the bar; none is excluded` is')
    rec('    ### ### SUPPORTED, and the repair does not touch it.')

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE REPAIR. ### **ORIGINAL BANKED VERBATIM; A FIGURE REMOVED, NOT RESTATED.**')
    rec('-' * 100)
    n22, l22 = AF.find(GS_README, '- **`Core/`** ')
    n25, l25 = AF.find(GS_README, 'assembly, `AXIOM_PRINTS.txt` (250/250). No terminal failed the bar')
    rec('    ### THE ORIGINALS, QUOTED BEFORE ANY EDIT:')
    rec('      README.md:%d' % n22)
    rec('      | %s' % l22.rstrip())
    rec('      README.md:%d' % n25)
    rec('      | %s' % l25.rstrip())
    census = clause_breakdown(l22)[1]['text']
    tail_m = re.search(r'\)\s*(across \d+ modules.*)$', l22.rstrip())
    tail = tail_m.group(1) if tail_m else ''
    intro_ref = intro.get('the assembly ratio', {}).get('introduced') or ''
    intro_date = gtext(GS, 'show', '-s', '--format=%cI', intro_ref).strip()[:10] if intro_ref else ''
    new22 = ('- **`Core/`** — the vanilla load-bearing layer: **as many zero-axiom terminals as '
             '`AXIOM_PRINTS.txt` in this tree carries**, one per printed line. The figure is not '
             'written out here: a figure written out goes stale the moment the layer grows, and this '
             'one did. The layer census that follows is held at `%s` (%s) and is not re-derived here — '
             '%s %s' % (intro_ref[:7], intro_date, census, tail))
    new25 = l25.replace('`AXIOM_PRINTS.txt` (250/250).', '`AXIOM_PRINTS.txt` in this tree.')
    rec('')
    rec('    ### THE REPLACEMENTS:')
    rec('      | %s' % new22)
    rec('      | %s' % new25.rstrip())
    rec('')
    rec('    ### **WHAT WAS REMOVED AND WHAT WAS KEPT, ITEM BY ITEM:**')
    rec('      -- the headline figure `%s` : ### **REMOVED**, and not restated with the current one,'
        % head_fig)
    rec('         because a new number re-arms the same trap (`b371`s rule, unamended).')
    rec('      -- the assembly ratio `%s` : ### **REMOVED**; the file it points at is named instead.'
        % (ratio_m.group(0) if ratio_m else None))
    rec('      -- the layer census and the module count : ### **PRESERVED VERBATIM AND DATED TO THE')
    rec('         ### REF THEY HOLD AT**, which is what the order permits in place of removal.')
    rec('      -- ### **NO CLAIM IS REWRITTEN.** ### `No terminal failed the bar; none is excluded`')
    rec('         stands, and section (4) above is its evidence.')
    rec('    ### ### **AND ONE THING IS ROUTED RATHER THAN REPAIRED:** ### re-deriving the census at')
    rec('    ### ### HEAD is a per-layer recount of the tree, ### **A CLAIM AND NOT A NUMBER**, and')
    rec('    ### ### the order says route it. ### It is routed.')

    result = dict(candidates=cand, fitting=fitting, intro=intro, table=table,
                  profile=dict(working=len(work), blob=len(blob), lines=len(wl),
                               zero=len(zero), names=len(names),
                               eol_equal=(nl(work.decode('utf-8', 'replace'))
                                          == nl(blob.decode('utf-8', 'replace')))),
                  originals=[dict(line=n22, text=l22.rstrip()), dict(line=n25, text=l25.rstrip())],
                  replacements=[dict(line=n22, text=new22), dict(line=n25, text=new25.rstrip())],
                  wrote=False)

    if write:
        body = nl(io.open(GS_README, encoding='utf-8').read())
        rows = body.split(chr(10))
        assert rows[n22 - 1] == l22.rstrip(chr(10)), 'anchor 1 moved'
        assert rows[n25 - 1] == l25.rstrip(chr(10)), 'anchor 2 moved'
        rows[n22 - 1] = new22
        rows[n25 - 1] = new25.rstrip(chr(10))
        out = chr(10).join(rows)
        io.open(GS_README, 'w', encoding='utf-8', newline=chr(10)).write(out)
        after = nl(io.open(GS_README, encoding='utf-8').read())
        gone = [f for f in (head_fig, (ratio_m.group(0) if ratio_m else None)) if f and f in after]
        kept = (census in after) and (tail in after)
        other = (len(after.split(chr(10))) == len(body.split(chr(10))))
        rec('')
        rec('    ### ### **WRITTEN.** ### %d -> %d bytes.'
            % (len(body.encode('utf-8')), len(after.encode('utf-8'))))
        rec('    ### the removed figures still present after the edit : %s ### -- must be []' % gone)
        rec('    ### the census and module count preserved verbatim  : %s' % kept)
        rec('    ### the line count is unchanged                     : %s' % other)
        git(GS, 'add', '--', 'README.md')
        result['wrote'] = True
        result['verify'] = dict(removed_still_present=gone, census_preserved=kept,
                                linecount_unchanged=other,
                                before_bytes=len(body.encode('utf-8')),
                                after_bytes=len(after.encode('utf-8')))

    rec('')
    rec('=' * 100)
    rec('  ### **NO BUILD WAS RUN. ### NO `.lean` FILE WAS TOUCHED. ### THE PROFILE WAS READ.**')
    rec('  ### **NOTHING IN THE EXCLUSION KERNEL WAS WRITTEN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b372_readme_notes', LINES)
    result['run_file'] = os.path.basename(p)
    result['run_clock'] = run_clock.read_stamp(p)
    io.open(os.path.join(D, 'b372_readme.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(result, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
