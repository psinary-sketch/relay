# -*- coding: utf-8 -*-
"""b364_diagnose.py -- THE DIAGNOSIS. ### **DIAGNOSE, DO NOT REPAIR-TO-PASS.**

### ### **THE ORDER'S OWN PHRASE IS A BAR, NOT A PREFERENCE:** ### an arm made to pass by editing the
### thing it reads has not been diagnosed, it has been silenced. ### **SO THIS TOOL WRITES NOTHING BUT ITS
### OWN RUN FILE AND ITS OWN JSON**, and proves that mechanically: every file it reads is compared
### byte-for-byte against its committed blob BEFORE and AFTER the diagnosis.
### ### **THE THREE FINDINGS ARE KEPT APART**, because the whole of this act is the difference between
### them: ### (i) what the arm CHECKS, quoted from its own suite; ### (ii) what it found in the COPY;
### ### (iii) what it finds in the BANKED SUITE AT ITS OWN LOCATION, run there, UNEDITED.
### ### **AND THE BRANCH IS DECIDED BY (iii) AND NOT BY (ii).** ### The copy has already failed; that is
### the datum, not the question.
"""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(T, n)


SUITE_REL = 'tools/b357_checks.py'
SUITE = t('b357_checks.py')
B357 = d('b357_what_the_ledgers_say.txt')
CEN363 = d('b363_census_run3.txt')

# ### **EVERY FILE THE DIAGNOSIS READS THAT IT MUST NOT WRITE.** ### Compared against its blob, both ends.
UNTOUCHABLE = ['tools/b357_checks.py', 'tools/banked_index.py',
               'data/b357_what_the_ledgers_say.txt', 'data/b357_read.json',
               'data/b357_read_run2.txt', 'data/b363_census_run3.txt']

# ### (label, hint) -- THE PREDICATE, QUOTED FROM ITS OWN SUITE. ### **BAR 1.**
PREDICATE = [
    ('the label the arm prints for itself',
     'G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW)'),
    ('the ledgers it reads', "LEGDERS_PLACEHOLDER"),
    ('what it does with each classified row', "n, line = AF.find(path, r['text'][:110])"),
    ('what it calls a hard failure', "print('    ### FAIL (NO ANCHOR NOW)"),
    ('what it allows -- a MOVED line -- and on what condition',
     "ok_dec = ('%d' % was) in bank and ('%d' % now) in bank and 'STRADDLE THIS ACT' in bf"),
]
PREDICATE[1] = ('the ledgers it reads', "LEDGERS = {'FINDINGS.md': FINDINGS,")

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def sha(path):
    return hashlib.sha256(io.open(path, 'rb').read()).hexdigest()


def blob_sha(rel):
    r = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD:' + rel], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    r2 = subprocess.run(['git', '-C', ROOT, 'cat-file', 'blob', r.stdout.strip()], capture_output=True)
    return hashlib.sha256(r2.stdout).hexdigest() if r2.returncode == 0 else None


def worktree_sha(rel):
    """### THE WORKING FILE'S BYTES, NORMALISED FOR LINE ENDINGS ONLY -- ### `core.autocrlf` makes a
    ### checked-out file CRLF while its blob stays LF (`b309`), so a raw comparison fails on a clean tree
    ### and would report an edit that never happened."""
    b = io.open(os.path.join(ROOT, rel.replace('/', os.sep)), 'rb').read()
    return hashlib.sha256(b.replace(b'\r\n', b'\n')).hexdigest()


def unchanged():
    out = []
    for rel in UNTOUCHABLE:
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        out.append(dict(path=rel, exists=os.path.exists(p),
                        worktree=worktree_sha(rel) if os.path.exists(p) else None,
                        blob=blob_sha(rel)))
    return out


def section(text, start_needle, stop_prefix='  G-'):
    """### THE ARM'S OWN BLOCK OF A RUN, LIFTED WHOLE AND NOT SUMMARISED."""
    lines = text.split(chr(10))
    keep, on = [], False
    for ln in lines:
        if not on and start_needle in ln:
            on = True
            keep.append(ln)
            continue
        if on:
            if ln.startswith(stop_prefix) and start_needle not in ln:
                break
            keep.append(ln)
    return chr(10).join(keep).rstrip()


def run_suite_at_home():
    """### (iii) ### **THE BANKED SUITE, RUN WHERE IT LIVES, UNEDITED.** ### `BAR 2`: a suite run somewhere
    ### else is the copy again, and the copy is the thing being diagnosed."""
    r = subprocess.run([sys.executable, SUITE], cwd=ROOT, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=1800)
    return (r.stdout or '') + (r.stderr or ''), r.returncode


def run_copy():
    """### (ii) ### **THE COPY, REMADE EXACTLY AS `b363` MADE IT**, run, and DELETED IN A `finally`."""
    dst = t('b364_copy_b357_checks.py')
    shutil.copy2(SUITE, dst)
    try:
        r = subprocess.run([sys.executable, dst], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=1800)
        return (r.stdout or '') + (r.stderr or ''), r.returncode
    finally:
        if os.path.exists(dst):
            os.remove(dst)


def failing(text):
    m = re.findall(r'GATES FAILING : (\d+)(.*)', text)
    if not m:
        return None, ''
    return int(m[-1][0]), m[-1][1].strip()


def main():
    rec('=' * 100)
    rec('b364 -- THE DIAGNOSIS. ### **DIAGNOSE, DO NOT REPAIR-TO-PASS.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('  ### the needle helper fixtures, run before it is trusted : %s' % GN.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (0) THE UNCHANGED BAR, READ BEFORE THE DIAGNOSIS. ### **BEFORE THE PUSH.**')
    rec('-' * 100)
    before = unchanged()
    for u in before:
        same = (u['worktree'] == u['blob'])
        rec('    %-40s worktree==blob : %-5s  %s' % (u['path'], same, (u['blob'] or 'NO BLOB')[:16]))
    b_ok = all(u['worktree'] == u['blob'] for u in before)
    rec('    ### ### **EVERY FILE THE DIAGNOSIS READS IS BYTE-IDENTICAL TO ITS COMMITTED BLOB : %s**' % b_ok)

    rec('')
    rec('-' * 100)
    rec('  ### (i) WHAT THE ARM CHECKED. ### **QUOTED FROM ITS OWN SUITE, NEVER PARAPHRASED.**')
    rec('-' * 100)
    pred, pbad = [], 0
    for lbl, hint in PREDICATE:
        try:
            n, line = AF.find(SUITE, hint)
        except AF.AnchorError as e:
            pbad += 1
            rec('    ### ### **NO ANCHOR : %s** -- %s' % (lbl, str(e).replace(chr(10), ' | ')[:120]))
            continue
        pred.append(dict(label=lbl, line=n, text=line.rstrip()))
        rec('')
        rec('    %s   ### %s:%d' % (lbl, os.path.basename(SUITE), n))
        rec('      | %s' % line.rstrip()[:180])
    rec('')
    rec('    ### ### **SO THE ARM CERTIFIES TWO THINGS AND NOT ONE:**')
    rec('    ###   ### **(a) EVERY ROW `b357` CLASSIFIED IS STILL FINDABLE AT ITS OWN LEDGER, NOW** -- by')
    rec('    ###     the anchor tool, on the row text, at one of FOUR ledgers: `FINDINGS.md`,')
    rec('    ###     `FACES_LEDGER.md`, `CORRESPONDENCE.md` and `tools/banked_index.py`.')
    rec('    ###   ### **(b) AND ANY ROW WHOSE LINE NUMBER HAS MOVED SINCE THE READING IS DECLARED IN')
    rec("    ###     ### `b357`'s OWN BANK, WITH BOTH NUMBERS**, and the bank carries the phrase")
    rec('    ###     `STRADDLE THIS ACT`.')
    rec('    ### ### **AND (b) IS THE HALF THAT CANNOT SURVIVE TIME.** ### It compares a number computed')
    rec('    ### NOW against a fixed string in a bank that was written ONCE and is append-only. ### **AN')
    rec('    ### ### ARM WHOSE PASS CONDITION IS A LITERAL IN A FROZEN FILE IS DATED BY CONSTRUCTION.**')

    rec('')
    rec('-' * 100)
    rec('  ### (ii) WHAT IT FOUND IN THE COPY.')
    rec('-' * 100)
    cen = io.open(CEN363, encoding='utf-8', errors='replace').read()
    row = [ln for ln in cen.split(chr(10)) if ln.strip().startswith('b357  banked GATES FAILING')]
    for ln in row:
        rec('    ### b363, banked : %s' % ln.strip())
    ctext, crc = run_copy()
    cn, cnames = failing(ctext)
    rec('    ### this act re-made the copy, ran it, and DELETED it in a `finally`.')
    rec('    ### the copy reports GATES FAILING : %s %s   (exit %s)' % (cn, cnames, crc))
    csec = section(ctext, 'G-LOCATED (')
    for ln in csec.split(chr(10)):
        rec('      | %s' % ln[:170])

    rec('')
    rec('-' * 100)
    rec('  ### (iii) WHAT IT FINDS IN THE BANKED SUITE AT ITS OWN LOCATION. ### **RUN THERE, UNEDITED.**')
    rec('-' * 100)
    htext, hrc = run_suite_at_home()
    hn, hnames = failing(htext)
    rec('    ### `%s` run from `%s`' % (SUITE_REL, ROOT))
    rec('    ### ### **GATES FAILING : %s %s**   (exit %s)' % (hn, hnames, hrc))
    hsec = section(htext, 'G-LOCATED (')
    for ln in hsec.split(chr(10)):
        rec('      | %s' % ln[:170])

    rec('')
    rec('-' * 100)
    rec('  ### (0) THE UNCHANGED BAR, READ AGAIN AFTER THE DIAGNOSIS.')
    rec('-' * 100)
    after = unchanged()
    a_ok = all(u['worktree'] == u['blob'] for u in after)
    same_pair = all(x['worktree'] == y['worktree'] for x, y in zip(before, after))
    rec('    ### every file still byte-identical to its blob : %s ; unchanged across the run : %s'
        % (a_ok, same_pair))
    leftovers = [f for f in os.listdir(T) if f.startswith('b364_copy_')]
    rec('    ### ### **NO COPY SURVIVED THE RUN** (tools/b364_copy_*) : %s %s'
        % (not leftovers, leftovers or ''))

    rec('')
    rec('-' * 100)
    rec('  ### (iv) THE BRANCH, DECIDED BY (iii) AND NOT BY (ii).')
    rec('-' * 100)
    home_passes = (hn == 0)
    copy_fails = (cn is not None and cn > 0)
    home_locates = ('G-LOCATED' not in (hnames or ''))
    if hn is None:
        branch = 'UNDECIDED'
        why = 'the banked suite produced no verdict line at its own location'
    elif home_passes:
        branch = 'ENVIRONMENTAL'
        why = 'the banked suite still passes where it lives'
    elif not home_locates:
        branch = 'REAL'
        why = 'G-LOCATED fails at the banked suite own location too'
    else:
        branch = 'UNDECIDED'
        why = 'the banked suite fails at its own location but not on G-LOCATED'
    rec('    the copy fails            : %s (%s %s)' % (copy_fails, cn, cnames))
    rec('    the banked suite at home  : GATES FAILING %s %s' % (hn, hnames))
    rec('    ### ### **BRANCH : %s** ### -- %s' % (branch, why))
    rec('    ### **AND THE OTHER TWO BRANCHES ARE SHOWN UNREACHABLE, NOT LEFT UNCLAIMED** (b350):')
    for b in ('ENVIRONMENTAL', 'REAL', 'UNDECIDED'):
        if b == branch:
            continue
        if b == 'ENVIRONMENTAL':
            rec('    ###   (ENVIRONMENTAL) -- UNREACHABLE: it requires the banked suite to PASS at its own')
            rec('    ###     location, and it reports GATES FAILING %s.' % hn)
        elif b == 'REAL':
            rec('    ###   (REAL) -- UNREACHABLE: it requires G-LOCATED to fail at the banked suite own')
            rec('    ###     location, and there it reports %s.' % (hnames or 'nothing failing'))
        else:
            rec('    ###   (UNDECIDED) -- UNREACHABLE: no step resisted. ### The suite ran to a verdict at')
            rec('    ###     its own location and the verdict line was read off its own output.')
    rec('')
    rec('    ### ### **AND WHAT IS NOT DONE, IN EITHER DIRECTION: NOTHING IS REPAIRED, NOTHING IS EDITED,')
    rec('    ### ### AND NO VERDICT IS MOVED BY THIS SEAT.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b364_diagnose_run', LINES)
    io.open(d('b364_diagnose.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(suite=SUITE_REL, predicate=pred, predicate_missing=pbad,
             copy_failing=cn, copy_names=cnames, copy_rc=crc,
             home_failing=hn, home_names=hnames, home_rc=hrc,
             copy_section=csec, home_section=hsec,
             branch=branch, why=why,
             unchanged_before=before, unchanged_after=after,
             unchanged_ok=bool(b_ok and a_ok and same_pair), copies_left=leftovers,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if (b_ok and a_ok and same_pair and not leftovers and not pbad and not pbad) else 1


if __name__ == '__main__':
    sys.exit(main())
