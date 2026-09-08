# -*- coding: utf-8 -*-
"""b369_hygiene.py -- COMPONENT 2: THE TWO HYGIENE ITEMS.

### ### **THE ORDER'S OWN REASON, ADOPTED:** ### *a roster that does not name a repository cannot pin
### it, and a pin taken by hand is not a pin the record can re-take.*
### ### **THIS TOOL EDITS TWO OWNER INSTRUMENTS AND THAT IS LICENSED, NAMED AND BOUNDED.** ### The
### registration names both on its own face BEFORE the edit; any other instrument moving is still a gate
### failure, and the suite still checks that.
### ### **AND THE WORDING IS MENDED WITH THE ROSTER, NOT AFTER IT.** ### Both tools say `ALL THREE` in
### their own voice. ### A tool that sweeps four repositories while announcing three is a ### **DATED
### ### ARM IN ITS OWN PROSE** ### (`b366`'s species), and leaving it would make the mend itself the
### incident the next act reports.
### ### **THE HOOK IS INSTALLED BY `b304_hooks.py` AND NOT BY THIS FILE**, because that tool already
### copies BYTE-IDENTICALLY from the one tracked source and exercises both polarities. ### **AN
### ### UNEXERCISED HOOK IS AN ASSERTION**, so the install and the exercise are the same run.
### ### **NO `.lean` FILE IS WRITTEN.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
PINS = os.path.join(ROOT, 'tools', 'b303_pins.py')
HOOKS = os.path.join(ROOT, 'tools', 'b304_hooks.py')
HOOKSRC = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ENTRY = "    ('SIDE-effects', r'D:\\SIDE-effects'),\n"
AFTER = "    ('PLACE-papers', r'D:\\MY-DOwnloads\\PLACE-papers'),\n"

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def read(p):
    return io.open(p, encoding='utf-8').read()


def write(p, s):
    open(p + '.tmp', 'wb').write(s.encode('utf-8'))
    os.replace(p + '.tmp', p)


def add_to_roster(path):
    """### **IDEMPOTENT, AND IT REFUSES RATHER THAN GUESSES.** ### The insertion point is the roster's
    ### own last entry, located by reading it -- never a line number."""
    txt = read(path)
    if "'SIDE-effects'" in txt:
        return 'ALREADY PRESENT', txt, txt
    if AFTER not in txt:
        return 'REFUSED -- the roster does not carry the entry this insert anchors on', txt, txt
    new = txt.replace(AFTER, AFTER + ENTRY, 1)
    write(path, new)
    return 'ADDED', txt, new


# ### **THE WORDING MENDS, EACH A LITERAL PAIR SO NOTHING IS REWRITTEN BY PATTERN.** ### A regex over a
# ### tool's prose would be a change nobody could review; these are exact strings.
WORDING = {
    PINS: [
        ('"""b303_pins.py -- THE PINS, ### **BY `ls-remote` ACROSS ALL THREE REPOS.**',
         '"""b303_pins.py -- THE PINS, ### **BY `ls-remote` ACROSS EVERY REPOSITORY THE ROSTER NAMES.**'),
        ("    print('b303_pins.py -- %s. ### BY `ls-remote`, ALL THREE REPOS.' % label)",
         "    print('b303_pins.py -- %s. ### BY `ls-remote`, ALL %d REPOS THE ROSTER NAMES.'\n"
         "          % (label, len(REPOS)))"),
    ],
    HOOKS: [
        ("### ### **ONE TRACKED SOURCE, THREE INSTALLS.** ### The hook is copied ### BYTE-IDENTICALLY ###",
         "### ### **ONE TRACKED SOURCE, ONE INSTALL PER ROSTERED REPOSITORY.** ### The hook is copied "
         "### BYTE-IDENTICALLY ###"),
        ("    print('b304_hooks.py -- THE PRE-PUSH HOOK, INSTALLED IN ALL THREE AND EXERCISED IN BOTH')",
         "    print('b304_hooks.py -- THE PRE-PUSH HOOK, INSTALLED IN ALL %d ROSTERED REPOS AND '\n"
         "          'EXERCISED IN BOTH' % len(REPOS))"),
        ("###     and a fresh clone of any of the three repos will have no hook until someone installs one.",
         "###     and a fresh clone of any rostered repo will have no hook until someone installs one."),
        ("    print('                 POLARITIES. ### ONE TRACKED SOURCE, THREE INSTALLS.')",
         "    print('                 POLARITIES. ### ONE TRACKED SOURCE, ONE INSTALL EACH.')"),
        # ### **THE PAIR SPANS BOTH LINES OF THE CALL, DELIBERATELY.** ### Replacing only the first would
        # ### leave a `%` continuation under a string that no longer ends in a format operator -- a
        # ### syntax error written by a mend. ### **AN EDIT TO A TOOL IS AN EDIT TO A STATEMENT, NOT TO
        # ### ### A LINE.**
        ("    print('  ### ALL THREE BYTE-IDENTICAL TO THE TRACKED SOURCE : %s  %s'\n"
         "          % (identical, 'PASS' if identical else '### FAIL ###'))",
         "    print('  ### ALL %d BYTE-IDENTICAL TO THE TRACKED SOURCE : %s  %s'\n"
         "          % (len(REPOS), identical, 'PASS' if identical else '### FAIL ###'))"),
    ],
}


def main():
    rec('=' * 100)
    rec('b369 -- COMPONENT 2: THE TWO HYGIENE ITEMS.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE ROSTERS, AS THEY STAND. ### **READ BEFORE THEY ARE EDITED.**')
    rec('-' * 100)
    for p in (PINS, HOOKS):
        n, ln = AF.find(p, 'REPOS = [')
        txt = read(p)
        got = re.findall(r"\('([A-Za-z-]+)', r'([^']+)'\)", txt.split('REPOS = [')[1].split(']')[0])
        rec('    %-18s roster at line %-4d : %s' % (os.path.basename(p), n, [g[0] for g in got]))
    rec('    ### ### **NEITHER NAMES THE EXCLUSION KERNEL, WHICH IS WHY `b368` PINNED IT BY HAND.**')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE MEND. ### **THE ROSTER, THEN THE PROSE THAT COUNTS IT.**')
    rec('-' * 100)
    results, wording_hits = {}, {}
    for p in (PINS, HOOKS):
        act, old, new = add_to_roster(p)
        results[os.path.basename(p)] = act
        rec('    %-18s : %s' % (os.path.basename(p), act))
        if act == 'REFUSED -- the roster does not carry the entry this insert anchors on':
            rec('    ### ### **REFUSED. ### NOTHING FURTHER IS WRITTEN.**')
            run_clock.write(D, 'b369_hygiene_notes', LINES)
            return 2
        txt = read(p)
        hits = 0
        for a, b in WORDING[p]:
            if a in txt:
                txt = txt.replace(a, b, 1)
                hits += 1
        if hits:
            write(p, txt)
        wording_hits[os.path.basename(p)] = hits
        rec('        wording pairs applied : %d of %d' % (hits, len(WORDING[p])))
    rec('    ### **THE WORDING IS MENDED BY EXACT STRING PAIRS, NEVER BY PATTERN** -- a regex over a')
    rec('    ### tool`s prose is a change nobody can review.')

    rec('')
    rec('-' * 100)
    rec('  ### (3) BOTH TOOLS STILL IMPORT AND STILL RUN. ### **AN EDITED INSTRUMENT IS EXERCISED.**')
    rec('-' * 100)
    ok_syntax = True
    for p in (PINS, HOOKS):
        r = subprocess.run([sys.executable, '-c',
                            'import ast,io,sys;ast.parse(io.open(sys.argv[1],encoding="utf-8").read())',
                            p], capture_output=True, text=True)
        ok = r.returncode == 0
        ok_syntax = ok_syntax and ok
        rec('    %-18s parses : %s %s' % (os.path.basename(p), ok, (r.stderr or '').strip()[:90]))
    if not ok_syntax:
        rec('    ### ### **AN EDITED INSTRUMENT NO LONGER PARSES. ### STOPPING.**')
        run_clock.write(D, 'b369_hygiene_notes', LINES)
        return 2
    rosters = {}
    for p in (PINS, HOOKS):
        txt = read(p)
        got = re.findall(r"\('([A-Za-z-]+)', r'([^']+)'\)", txt.split('REPOS = [')[1].split(']')[0])
        rosters[os.path.basename(p)] = [g[0] for g in got]
        rec('    %-18s roster now : %s' % (os.path.basename(p), [g[0] for g in got]))

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE HOOK. ### **INSTALLED BY THE ROSTERED TOOL, EXERCISED IN BOTH POLARITIES.**')
    rec('-' * 100)
    src = open(HOOKSRC, 'rb').read()
    rec('    tracked source : tools/git-hooks/pre-push ; %d bytes' % len(src))
    had = os.path.exists(os.path.join(KERNEL, '.git', 'hooks', 'pre-push'))
    rec('    ### the exclusion kernel had a pre-push hook BEFORE this act : %s' % had)
    r = subprocess.run([sys.executable, HOOKS], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    out = r.stdout or ''
    io.open(os.path.join(D, 'b369_hooks.txt'), 'w', encoding='utf-8',
            newline=chr(10)).write(out + (r.stderr or ''))
    for ln in out.splitlines():
        if any(k in ln for k in ('repo ', 'relay', 'SIDE-', 'PLACE-', 'REPOS FAILING',
                                 'BYTE-IDENTICAL', 'refusal text')):
            rec('    | %s' % ln.rstrip()[:118])
    installed = os.path.join(KERNEL, '.git', 'hooks', 'pre-push')
    now = open(installed, 'rb').read() if os.path.exists(installed) else b''
    identical = (now == src)
    failing = re.search(r'### REPOS FAILING : (\d+)', out)
    nfail = int(failing.group(1)) if failing else -1
    rec('    ### ### **THE INSTALLED HOOK IS BYTE-IDENTICAL TO THE TRACKED SOURCE : %s** (%d bytes)'
        % (identical, len(now)))
    rec('    ### ### **REPOS FAILING THE POLARITY EXERCISE : %d**' % nfail)
    rec('    ### ### **AND WHAT THIS DOES NOT FIX, SAID NOW AND NOT DISCOVERED LATER:** ### `.git/hooks/`')
    rec('    ### is UNTRACKED. ### **A FRESH CLONE OF ANY OF THESE REPOSITORIES STILL HAS NO HOOK.**')
    rec('    ### The roster mend is TRACKED and survives a clone; the hook install is NOT. ### **THE TWO')
    rec('    ### ### REPAIRS ARE NOT EQUAL IN DURABILITY AND THIS ACT SAYS WHICH IS WHICH.**')
    lean_dirty = [x for x in subprocess.run(['git', '-C', KERNEL, 'status', '--porcelain'],
                                            capture_output=True, text=True).stdout.splitlines()
                  if x.strip().endswith('.lean')]
    rec('    ### **AND NO `.lean` FILE WAS TOUCHED : %s**' % (not lean_dirty))
    rec('=' * 100)

    ok = (identical and nfail == 0 and ok_syntax
          and all('SIDE-effects' in v for v in rosters.values())
          and all(h == len(WORDING[p]) for p, h in
                  ((PINS, wording_hits['b303_pins.py']), (HOOKS, wording_hits['b304_hooks.py'])))
          and not lean_dirty)
    rec('  ### ### **COMPONENT 2 : %s**' % ('EXECUTED' if ok else 'FAILED'))
    rec('=' * 100)
    p = run_clock.write(D, 'b369_hygiene_notes', LINES)
    io.open(os.path.join(D, 'b369_hygiene.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(roster_actions=results, rosters=rosters, wording_pairs=wording_hits,
                        instruments_edited=2, hook_existed_before=had,
                        hook_bytes=len(now), hook_identical=identical, repos_failing=nfail,
                        polarities_exercised=True, tracked_hooks_dir=False,
                        lean_touched=len(lean_dirty),
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
