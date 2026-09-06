# -*- coding: utf-8 -*-
"""b342_modules.py -- THE TWO RULES AS TECHNE MODULES, AS THE EXECUTOR'S DRAFT STATES THEM; THE INDEX APPENDED; THE
### UNTOUCHED CHECK; ONE LOCAL COMMIT, NOT PUSHED (registration (C), sealed first).

### ### **WHAT IT WRITES.** ### `modules/2026-09/LIKE_FOR_LIKE.md` and `modules/2026-09/SIGN_RULE.md` in the September
### modules' shape, every quotation a sentence the extract file located; one appended block at the foot of
### `modules/INDEX.md`. ### **WHAT IT CHECKS.** ### Every file under `modules/` hashed before and after; only the two new
### files and the index's suffix may differ. ### **WHAT IT COMMITS.** ### One commit in TECHNE-Core by explicit list;
### the remote read by `ls-remote` before and after and required equal. ### **WHAT IT NEVER DOES.** ### Push.
"""
import hashlib
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules')
INDEX = os.path.join(MOD, 'INDEX.md')
MARK = '<!-- b342 -->'
RUN = os.path.join(D, 'b342_modules_run.txt')
OUT = os.path.join(D, 'b342_modules.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEADER = ('*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b342) \u00b7 **PRIVATE, TECHNE-Core, local-only**. '
          'Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*')

LIKE = '''# The like-for-like rule

%s

---

## WHAT IT DOES

Every quantity an instrument compares carries the name of the function it was computed for, and
the comparator refuses when its two sides name different functions. **A bar sealed against a
banked table names the table's function.** A comparison of a number computed for one test
function against a table made for another is not a comparison, and the tool says so before it
prints a difference.

## WHEN IT APPLIES

Whenever a bar, a route agreement or a diagnosis sets one computed quantity against another —
against a banked table, a second route, a reference value — and the two were computed on test
functions, cells, or conventions that could differ. The name travels with the number from the
line that computed it to the line that compares it.

## WHAT IT REFUSES

- A comparison whose two sides name different functions: the comparator raises, and the fixture
  proves it raises.
- A bar sealed against a banked table without reading the producing tool for the function behind
  the table.
- Reading a table's column of cells as one's own cells because the widths match.

## PROVENANCE

- **Acts:** b333 (2026-09-06): the derivation tool *"did exactly what the seal ordered and printed
  `MISMATCH`"* — the sealed bar had paired the atlas's bump with a table b320 made for
  `autocorrelation(mean_zero_variant(a))`; *"THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED"*; the
  diagnosis was done *"like for like"* in a new tool and *"The like-for-like readings live in a new
  tool and are readings"*; the seat's defect, declared: it *"read b320's table's `a` column as the
  bump's cells without reading b320's tool for the function behind"* it. b334 (2026-09-06): every
  quantity carried as a named pair — *"THE LIKE-FOR-LIKE RULE, ENFORCED BY NAME"* — and the bump's
  negative archimedean term found to be the bump's, the aimed seed's its own, *"which is what the
  like-for-like rule is for."*
- **Tools:** `relay/tools/b334_aimmap.py` (`Q`, `compare` — *"the only comparison in this file; it
  raises when the two sides name different functions"* — and `fixture_like`);
  `relay/tools/b333_diagnose.py`.
- **Family:** READING. Extends `2026-08/HARNESS_LORE.md` rule 19 (scope statements travel with
  results) to the function a number was computed for; the fold's lore (FINDINGS, THE STATED-CLAUSE
  ARC) typed this rule `TOOL` until this module.
''' % HEADER

SIGN = '''# The sign rule, with the b328 phase refinement

%s

---

## WHAT IT DOES

A threshold rule is stated together with the sign condition it stands for, and a verdict that a
threshold is passed is printed beside the sign of the term the threshold was derived from. **A
phase past the threshold is not a negative term.** Where a rule was derived at one range of its
variable and applied at another, the term's own sign, not the threshold, is what is read.

## WHEN IT APPLIES

To any rule of the form *the term is negative past this threshold* that is applied outside the
range where it was derived — in particular to phase conditions on oscillatory seeds, whose sign
condition is periodic where the threshold is not.

## WHAT IT REFUSES

- Counting a phase past the threshold as a negative term without the term's sign beside it.
- Restating a threshold rule without its sign condition.
- Editing the rule where it was stated: the block that stated it stands, and the refinement is
  filed as an addendum beside it.

## THE REFINEMENT, CARRIED FROM b328's OWN DERIVATION

For an even seed the quadruple's term is **`S_4 = 4 |G(c)|^2 cos(2 phi)`, NEGATIVE EXACTLY WHEN
`45 deg < |phi| < 135 deg`** (b328, the derivation); *"an even seed needs phase past forty-five; an odd
component needs phase BELOW it; both add"* — the odd component contributes `-4 Re G_o^2`. The rule
as b328 first stated it, *"NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE"*, is the condition at
b328's own phases (every measured phase near ninety degrees) and is unaffected there; the general
condition is the band. b336 filed this as an addendum to b328's block on the faces ledger; this
module carries it as the rule's sign condition.

## PROVENANCE

- **Acts:** b328 (2026-09-05), the derivation of the phase condition with the factor four in front;
  b334 (2026-09-06): *"THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO"* — by
  the sealed rule *"270 of 392 aims are REACHED; with a negative term 170"*, the other hundred at a
  phase near 180 degrees with a positive term; the chart prints *"the quadruple's sign beside the
  threshold verdict"*. b336 (2026-09-06), the addendum to b328's block.
- **Tool:** `relay/tools/b334_aimmap.py` (`chart`, the sign column, which prints the quadruple's
  term's sign beside every threshold verdict); b334's bank states the condition it prints, the
  *"quadruple's term `4 |G|^2 cos 2 phi` is negative only between `45` and `135` degrees"*.
- **Family:** DISCRIMINATOR_PROTOCOL. Extends `2026-08/HARNESS_LORE.md` rule 11 (a falsifier's
  verdict is bounded by its instrument's resolution) with the case of a threshold read for a sign;
  the fold's lore typed this rule `TOOL` until this module.
''' % HEADER

INDEX_BLOCK = ['', MARK, '',
               '## The b342 additions',
               '',
               '*Appended 2026-09-06 (research seat, b342, leg 4 of the sortie b339\u2013b343): the rules the fold of b331\u2013b334 typed `TOOL`, as claim-shaped method modules, with the b328 phase refinement carried into the sign rule. Committed locally, NOT PUSHED. No existing row is edited.*',
               '',
               '| module | family | what it fixes | cross-reference to August |',
               '|:--|:--|:--|:--|',
               '| `2026-09/LIKE_FOR_LIKE.md` | READING | a comparator named with the function it was computed for; a bar names its table\'s function | extends `HARNESS_LORE.md` rule 19 |',
               '| `2026-09/SIGN_RULE.md` | DISCRIMINATOR_PROTOCOL | a threshold rule stated with its sign condition; the 45\u00b0\u2013135\u00b0 band | extends `HARNESS_LORE.md` rule 11 |',
               '']


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def tree():
    out = {}
    for root, _dirs, files in os.walk(MOD):
        for f in files:
            p = os.path.join(root, f)
            out[os.path.relpath(p, TC).replace(chr(92), '/')] = sha(p)
    return out


def git(*args):
    return subprocess.run(['git', '-C', TC] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def main():
    L = []

    def rec(s=''):
        L.append(s)
        print(s, flush=True)
    rec('=' * 100)
    rec('b342 -- THE TWO RULES AS TECHNE MODULES. ### written, indexed by an appended block, hashed before and after, committed locally, NOT PUSHED.')
    rec('=' * 100)
    remote_before = git('ls-remote', 'origin', 'main').split()[0][:7] if git('ls-remote', 'origin', 'main') else '?'
    head_before = git('rev-parse', '--short', 'HEAD')
    before = tree()
    idx_before = io.open(INDEX, encoding='utf-8').read()
    rec('  TECHNE-Core HEAD %s ; remote main %s ; %d files under modules/ hashed before' % (head_before, remote_before, len(before)))
    like_p = os.path.join(MOD, '2026-09', 'LIKE_FOR_LIKE.md')
    sign_p = os.path.join(MOD, '2026-09', 'SIGN_RULE.md')
    wrote = []
    # ### `--correct` REWRITES THIS ACT'S OWN TWO MODULES FROM THE CONSTANTS ABOVE, AND NOTHING ELSE. ### It exists because
    # ### b342's gate suite found three quotations in them that were not their emitters' text: two transcriptions (a
    # ### capital dropped; a span carrying a source escape) and one the extract step had not located. ### The files it may
    # ### rewrite are the two this act created; every pre-existing file stays under the untouched check, which still runs.
    correct = '--correct' in sys.argv
    for p, body in ((like_p, LIKE), (sign_p, SIGN)):
        if os.path.exists(p) and correct and io.open(p, encoding='utf-8').read() != body:
            io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
            wrote.append(os.path.relpath(p, TC).replace(chr(92), '/'))
            rec('  ### CORRECTED %s (the quotations b342\'s gate suite found were not their emitters\' text)' % os.path.relpath(p, TC))
        elif os.path.exists(p):
            rec('  %s already present -- not rewritten' % os.path.relpath(p, TC))
        else:
            io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
            wrote.append(os.path.relpath(p, TC).replace(chr(92), '/'))
            rec('  wrote %s (%d lines)' % (os.path.relpath(p, TC), len(body.splitlines())))
    if MARK in idx_before:
        rec('  the index already carries %s -- not appended' % MARK)
    else:
        new = idx_before.rstrip(chr(10)) + chr(10) + chr(10).join(INDEX_BLOCK)
        io.open(INDEX, 'w', encoding='utf-8', newline=chr(10)).write(new)
        wrote.append('modules/INDEX.md')
        rec('  appended the index block (%d -> %d lines)' % (len(idx_before.splitlines()), len(new.splitlines())))
    after = tree()
    idx_after = io.open(INDEX, encoding='utf-8').read()
    changed = sorted(k for k in before if before[k] != after.get(k))
    added = sorted(k for k in after if k not in before)
    idx_prefix = idx_after.startswith(idx_before.rstrip(chr(10)))
    OURS = {'modules/2026-09/LIKE_FOR_LIKE.md', 'modules/2026-09/SIGN_RULE.md'}
    # ### a correction of THIS ACT'S OWN two modules is not an edit of an existing file: the pre-act tree is the tree at
    # ### `head_before`, and neither module is in it. ### Every other file must still be byte-identical.
    pre_act = set(git('ls-tree', '-r', '--name-only', '4c0a6af').split())
    untouched = set(changed) <= ({'modules/INDEX.md'} | (OURS - pre_act)) and set(added) <= OURS and idx_prefix
    rec('  changed among the existing files : %s ; added : %s ; the index a true prefix of its prior self : %s ; UNTOUCHED CHECK : %s' % (changed, added, idx_prefix, 'PASS' if untouched else '### FAIL ###'))
    # ### the commit, by explicit list, NOT PUSHED
    st = git('status', '--porcelain')
    committed = None
    if wrote and untouched:
        subprocess.run(['git', '-C', TC, 'add', '--'] + ['modules/2026-09/LIKE_FOR_LIKE.md', 'modules/2026-09/SIGN_RULE.md', 'modules/INDEX.md'], check=True)
        msg = ('modules/2026-09: the two rules as modules -- LIKE_FOR_LIKE.md and SIGN_RULE.md (the b328 phase refinement carried into the sign rule), '
               'the index appended (b342, leg 4 of the sortie b339-b343, research seat, NOT PUSHED; the author\'s ruling of 2026-09-06 on the private clone stands).\n\n'
               'Claude-Session: https://claude.ai/code/session_01ELiKF4s74Yfw58E7zXDx9M\n')
        subprocess.run(['git', '-C', TC, 'commit', '-q', '-F', '-'], input=msg, text=True, encoding='utf-8', check=True)
        committed = git('rev-parse', '--short', 'HEAD')
        rec('  committed %s by explicit list (the like-for-like module, the sign-rule module, the index)' % committed)
    else:
        rec('  nothing committed (wrote %s ; untouched %s)' % (wrote, untouched))
    remote_after = git('ls-remote', 'origin', 'main').split()[0][:7] if git('ls-remote', 'origin', 'main') else '?'
    clean = git('status', '--porcelain') == ''
    ahead = git('rev-list', '--count', 'origin/main..HEAD') if git('rev-parse', '--verify', '-q', 'origin/main') else '?'
    rec('  remote main before %s / after %s : %s ; working tree clean : %s ; commits ahead of origin/main : %s ; NOT PUSHED' % (remote_before, remote_after, 'EQUAL' if remote_before == remote_after else '### MOVED ###', clean, ahead))
    ok = untouched and remote_before == remote_after and clean
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    out, k = RUN, 1
    while os.path.exists(out):
        k += 1
        out = RUN.replace('_run.txt', '_run%d.txt' % k)
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    if not wrote:
        # ### a re-run that wrote nothing reconstructs the record from git rather than overwriting the writing run's record
        # ### (the second run of this tool overwrote it with a no-op result; the third run repaired that here).
        c = git('log', '-1', '--format=%h', '--', 'modules/2026-09/LIKE_FOR_LIKE.md')
        parent = git('rev-parse', '--short', c + '^') if c else None
        names = git('show', '--name-status', '--format=', c).splitlines() if c else []
        committed, head_before = c or None, parent
        changed = sorted(ln.split()[-1] for ln in names if ln.startswith('M'))
        added = sorted(ln.split()[-1] for ln in names if ln.startswith('A'))
        before = {kk: v for kk, v in after.items() if kk not in added}
        wrote = added + changed
        rec('  (record reconstructed from git: commit %s on %s ; added %s ; changed %s)' % (committed, head_before, added, changed))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(head_before=head_before, committed=committed, head_after=git('rev-parse', '--short', 'HEAD'), remote_before=remote_before, remote_after=remote_after,
                                                                              files_before=len(before), changed=changed, added=added, index_prefix=idx_prefix, untouched=bool(untouched), clean=clean, ahead=ahead,
                                                                              sha_like=sha(like_p), sha_sign=sha(sign_p), sha_index=sha(INDEX), index_lines=len(idx_after.splitlines()), wrote=wrote, run_file=os.path.basename(out)), indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
