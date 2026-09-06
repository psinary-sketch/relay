# -*- coding: utf-8 -*-
"""b344_module.py -- COMPONENT 2's MODULE: THE SEAL CARRIES ITS OWN CLOCK. ### written, indexed, hashed, committed
### locally, NOT PUSHED (registration section (D), sealed first).

### ### Every quotation in the module is a span the extract step located and that lies inside one captured line, so a
### comparison that flattens whitespace finds it whole -- b342's own defect, not repeated. ### Every file under
### `modules/` is hashed before and after; only the new file and the index's appended suffix may differ. ### One commit
### by explicit list; the remote read by `ls-remote` before and after and required equal. ### **IT NEVER PUSHES.**
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
MARK = '<!-- b344 -->'
RUN = os.path.join(D, 'b344_module_run.txt')
OUT = os.path.join(D, 'b344_module.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEADER = ('*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b344) \u00b7 **PRIVATE, TECHNE-Core, local-only**. '
          'Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*')

BODY = '''# The seal carries its own clock

%s

---

## WHAT IT DOES

The block a sealing tool writes carries, beside the hash and the byte count, **the instant the block
was written**, in UTC. Without it the file's own modification time is the only evidence of when the
seal was applied — and any lawful later addition to the file destroys that evidence.

## WHEN IT APPLIES

To any registration, manifest or certificate whose order of writing is itself checked; and in
particular wherever the method licenses a **post-hoc marking appended below the seal**, which
rewrites the file and so moves its modification time.

## WHAT IT REFUSES

- A seal block that records what was sealed but not when.
- An order check that infers the seal's time from the file's modification time, which a lawful
  later append silently changes.
- Claiming more for the clock than it carries: **it is outside the hash**. It records when the seal
  was written by a tool that meant to record it; it is not evidence against a seat that would alter
  it afterwards. A tool whose clock were inside its own hash could not write it at all.

## WHAT IT DOES NOT RECOVER

Nothing sealed before it. The acts already sealed keep exactly the evidence they had, and an order
arm that failed for want of a timestamp stays failed: *"the repair does NOT do: it does not recover
b342's lost timestamp."*

## PROVENANCE

- **Act:** b342 (2026-09-06) bought it, by failing: its order arm was declared a defective bar —
  *"THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING."* — because
  *"A LAWFUL POST-SEAL MARKING"* had rewritten the registration file and the seal block carried no
  time, so one component's position relative to the seal became unrecoverable and the order was left
  *"GATE-ESTABLISHED for this act"* only in the negative. b344 (2026-09-06) repaired the instrument
  and not the past, by the order's words: *"have reg_seal.py record the seal's UTC instant inside
  the seal block"*.
- **Tool:** `relay/tools/reg_seal.py` (`CLOCK`, `stamp`, written into the block by `cmd_seal` and
  `cmd_reseal`; `digest` and `cmd_verify` untouched, so every prior seal verifies unchanged).
- **Fixtures:** every sealed file in the corpus verified before and after the repair with the same
  verdict and none rewritten; a fresh seal carries the clock and verifies; a seal whose clock line is
  altered still verifies — the arm that states the limit rather than hiding it; a seal whose body is
  altered still refuses.
- **Family:** REGISTRATION. Extends `2026-09/REGISTRATION_SEAL_AND_SATISFIABILITY.md` (the seal, the
  joint check, the order, post-hoc marking) with the clock the order check needs, and records that
  the two are in tension: the marking the module licenses is what destroys the evidence the order
  arm used, until the clock exists.
''' % HEADER

INDEX_BLOCK = ['', MARK, '',
               '## The b344 addition',
               '',
               "*Appended 2026-09-06 (research seat, b344): the rule b342 bought by failing — a seal block records when it was written, because a lawful post-hoc marking rewrites the file and moves its modification time. Committed locally, NOT PUSHED. No existing row is edited.*",
               '',
               '| module | family | what it fixes | cross-reference to August |',
               '|:--|:--|:--|:--|',
               '| `2026-09/SEAL_CARRIES_ITS_CLOCK.md` | REGISTRATION | the seal records its own instant; the clock is outside the hash and says so | extends `2026-09/REGISTRATION_SEAL_AND_SATISFIABILITY.md` |',
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
    rec("b344 -- THE MODULE: THE SEAL CARRIES ITS OWN CLOCK. ### written, indexed, hashed, committed locally, NOT PUSHED.")
    rec('=' * 100)
    # ### every quotation must be a span the extract located, whole, after flattening
    import re
    ex = io.open(os.path.join(D, 'b344_extract_notes.txt'), encoding='utf-8').read()

    def flat(s):
        return re.sub(r'\s+', ' ', s.replace('\u2019', "'")).strip()
    exf = flat(ex)
    quotes = re.findall(r'\*"([^"]{12,})"\*', BODY)
    miss = [q for q in quotes if flat(q) not in exf]
    rec('  quotations in the module : %d ; not located by the extract step : %d %s' % (len(quotes), len(miss), miss if miss else ''))
    if miss:
        rec('  ### REFUSED -- a quotation the extract step did not locate. ### Nothing written.')
        return 1
    remote_before = git('ls-remote', 'origin', 'main').split()[0][:7]
    head_before = git('rev-parse', '--short', 'HEAD')
    before = tree()
    idx_before = io.open(INDEX, encoding='utf-8').read()
    rec('  TECHNE-Core HEAD %s ; remote main %s ; %d files under modules/ hashed before' % (head_before, remote_before, len(before)))
    p = os.path.join(MOD, '2026-09', 'SEAL_CARRIES_ITS_CLOCK.md')
    wrote = []
    if os.path.exists(p):
        rec('  %s already present -- not rewritten' % os.path.relpath(p, TC))
    else:
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(BODY)
        wrote.append('modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md')
        rec('  wrote modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md (%d lines)' % len(BODY.splitlines()))
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
    untouched = set(changed) <= {'modules/INDEX.md'} and set(added) <= {'modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md'} and idx_prefix
    rec('  changed among the existing files : %s ; added : %s ; the index a true prefix of its prior self : %s ; UNTOUCHED CHECK : %s'
        % (changed, added, idx_prefix, 'PASS' if untouched else '### FAIL ###'))
    committed = None
    if wrote and untouched:
        subprocess.run(['git', '-C', TC, 'add', '--', 'modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md', 'modules/INDEX.md'], check=True)
        msg = ("modules/2026-09: the seal carries its own clock -- the rule b342 bought by failing, filed as a method module, "
               "the index appended (b344, research seat, NOT PUSHED; the author's ruling of 2026-09-06 on the private clone stands).\n\n"
               "Claude-Session: https://claude.ai/code/session_01ELiKF4s74Yfw58E7zXDx9M\n")
        subprocess.run(['git', '-C', TC, 'commit', '-q', '-F', '-'], input=msg, text=True, encoding='utf-8', check=True)
        committed = git('rev-parse', '--short', 'HEAD')
        rec('  committed %s by explicit list (the module, the index)' % committed)
    else:
        rec('  nothing committed (wrote %s ; untouched %s)' % (wrote, untouched))
        committed = git('log', '-1', '--format=%h', '--', 'modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md') or None
    remote_after = git('ls-remote', 'origin', 'main').split()[0][:7]
    clean = git('status', '--porcelain') == ''
    ahead = git('rev-list', '--count', 'origin/main..HEAD')
    rec('  remote main before %s / after %s : %s ; working tree clean : %s ; commits ahead of origin/main : %s ; NOT PUSHED'
        % (remote_before, remote_after, 'EQUAL' if remote_before == remote_after else '### MOVED ###', clean, ahead))
    ok = untouched and remote_before == remote_after and clean and committed
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    out, k = RUN, 1
    while os.path.exists(out):
        k += 1
        out = RUN.replace('_run.txt', '_run%d.txt' % k)
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(head_before=head_before, committed=committed, head_after=git('rev-parse', '--short', 'HEAD'),
             remote_before=remote_before, remote_after=remote_after, files_before=len(before), changed=changed, added=added,
             index_prefix=idx_prefix, untouched=bool(untouched), clean=clean, ahead=ahead, quotes=len(quotes),
             module_lines=len(BODY.splitlines()), index_lines=len(idx_after.splitlines()), run_file=os.path.basename(out)), indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
