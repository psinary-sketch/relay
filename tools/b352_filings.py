# -*- coding: utf-8 -*-
"""b352_filings.py -- COMPONENT 3: THE TWO FILINGS.

### ### **FILING ONE** -- the spectral void's width as a work-order note on `OPEN_TRAILS.md`, carrying ### **THE
### MEASURED `10.62` WITH b350 NAMED** and not a round decade. ### Append-only, under its own mark, checked as a
### true prefix of what it was and of its committed blob ### **BEFORE THE PUSH, which is the reading that
### carries** -- after the push the blob IS the file and the check is near-vacuous, which is precisely the rule
### filing two mints.
### ### **FILING TWO** -- the straddling-gate rule, minted as a TECHNE module, ### **LOCAL-ONLY AND NOT PUSHED**,
### as every module since b330. ### Its mechanized half is already appended to `tools/registration_gate.py`; this
### file writes the module and reports the fixtures.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import quote_norm           # noqa: E402
import registration_gate as RG   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b352 void width work-order -->'
MODDIR = os.path.join(TC, 'modules', '2026-09')
MODULE = os.path.join(MODDIR, 'STRADDLING_GATE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def block(P):
    lo, hi = 2.144048e-07, 2.277535e-06
    return [
        '', MARK, '',
        '### **`W-ORD-VOID-WIDTH` — OPENED 2026-09-07 (b352): THE SPECTRAL VOID’S WIDTH, AND WHY NARROWING '
        'IT IS NOT FREE**',
        '',
        ('*A work-order note. **Nothing here is attempted, and no instrument is proposed.** It records a '
         'measured width and one consequence of moving it, so that a later act does not narrow the void '
         'without seeing what the narrowing costs.*'),
        '',
        ('**The width, as b350 measured it and not as a round number.** At every rung of b344’s sealed '
         'ladder, b344 printed the largest eigenvalue dropped and the smallest kept. b350 took the '
         '**intersection across the rungs** and found `(2.144048e-07, 2.277535e-06)` — a factor of '
         '**`10.62`**, with the corpus’s own `tau = 1e-6` inside it, free to fall by `4.66` or rise by '
         '`2.28` with the same eigenvalues kept at every rung and therefore the same rank. **It is `10.62` '
         'and not "a decade", and the distinction is the point of this note:** a round decade invites the '
         'reading that the threshold is comfortably free, and a factor of ten and a half is not comfortable.'),
        '',
        ('**Robust across the quadrature ladder, in the sense b350 established and no stronger.** The '
         'interval is an intersection over every rung b344 ran, so it is the width that survives the whole '
         'ladder rather than the width at any one frame. b319 records that the corpus’s threshold sits '
         '*57 times inside that separation*.'),
        '',
        ('**And the consequence a later act must see before it narrows the void.** The width is a fact about '
         'the **cut** and not about the residual — b350 fixed that sentence in its registration before the '
         'arithmetic, and it holds here. A finer instrument that narrowed the void would shrink the interval '
         'in which the threshold may sit with the rank unchanged; **at the limit, the stable-rank cut becomes '
         'under-determined** — there ceases to be a band of thresholds all giving the same rank, and the rank '
         'the corpus reports becomes a property of the threshold chosen rather than of the operator. **That '
         'is a cost paid in the meaning of every rank the record has banked, not in wall time.**'),
        '',
        ('*Species: **NOTE** (a work-order, not a trail). **NOT ATTEMPTED HERE**, and no act is asked to '
         'attempt it. Trigger: any act proposing a finer quadrature or a narrower stable cut. Nothing here '
         'is a route, no grade moves, and `h2` stands exactly where the deposit left it.*'),
    ]


MODULE_TEXT = '''# STRADDLING_GATE.md — a gate that straddles an event has two readings

**Minted b352 (2026-09-07), from three incidents already in the record.**
**Status: JUDGEMENT RULE with a MECHANIZED HALF. The two halves are listed apart, deliberately.**

## The rule

**A gate arm whose subject changes at an event has two readings — one before the event and one after —
and they are not the same check. The act names the reading it relies on.**

The event in this record is almost always *the push* (or the commit inside it). Before it, the working
tree and the committed blob differ; after it, they are the same object. An arm that compares them is a
real check on one side of that line and very nearly no check at all on the other.

## The three incidents

1. **The mirror, warning about itself.** `tools/mirror_verify.py` carries, in its own header:
   *"A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A CORRECT ONE."* The archive must be
   rebuilt **after** the commit; run before, clause 1 passes on a stale archive and the pass is
   indistinguishable from a correct one. The instrument named this hazard before any act tripped on it.

2. **An arm that cannot pass before the event.** `data/b350_checks_run_prepush.txt`:
   *"the hook and the mirror records are NOT YET WRITTEN (they are written at the push)."* `G-HOOK` and
   `G-MIRROR` necessarily fail pre-push, and b350 banked that failing run rather than hiding it. **The whole
   content of those arms is the after-reading**, and an act that reported only the pre-push run would have
   reported a failure that meant nothing.

3. **An arm that is strong before and near-vacuous after.** The ancestry check — *the working file is a true
   prefix of its committed blob* — is a genuine append-only proof **before** the commit. **After** the commit
   the blob *is* the file, so the check is trivially true and proves nothing about how the file got there.
   b350 and b351 both ran it on both sides; b351's closing said so in the act's own words.

## What follows

- **State the side.** Every arm that reads a repository state declares whether it is the pre-event or the
  post-event reading, or marks itself side-invariant.
- **Bank the pre-event run.** Where an arm's two readings differ, the run that carries is often the one that
  *failed*, and it must survive in the record.
- **A post-event pass is not evidence the pre-event check would have passed.** These are different claims.

## The split: what is mechanized, and what is not

**MECHANIZED** — appended to `tools/registration_gate.py` at b352 as `straddle_check` /
`straddle_self_test`, beside the bar-floor arms and editing nothing:

> a registration that names a gate arm **and** touches a repository state must say whether that arm is read
> **before** or **after** the push, or mark it **SIDE-INVARIANT**.

Six fixtures, both polarities: it fires on an undeclared arm; it is quiet on `AFTER THE PUSH`, on
`pre-push`, and on a deliberate `SIDE-INVARIANT`; and it is quiet both on arms that touch no repository
state and on repository prose that names no arm. Its window is the paragraph, and markers and line breaks
are collapsed before the search — **a lesson from this arm's own fixture, which failed first because the
declaration wrapped across a line and the arm raised a false alarm on text that had declared correctly.**

**NOT MECHANIZED, AND FILED AS JUDGEMENT — NOT LISTED BESIDE THE MECHANIZED HALF:**

> **Which arms straddle cannot be decided by a string.** An arm straddles when its *verdict* would change
> across the event, and no scanner computes that from the arm's text. The mechanized half forces a
> declaration; **it does not and cannot check that the declaration is right.** An act that declares every
> arm `SIDE-INVARIANT` passes the gate and has decided nothing.

## Limits

- It binds registrations written after it. b352 ran it over its own sealed registration as a measurement,
  and re-verdicted nothing.
- It matches text, so an arm phrased in words the pattern does not know is invisible — the false-miss class
  b164 named for the index's keys. **Keys close false hits, not false misses.**
- Related: [BAR_FLOOR_RULE.md](BAR_FLOOR_RULE.md) (a bar carries its object's floor),
  [USE_AND_MENTION.md](USE_AND_MENTION.md) (a scanner over prose cannot tell use from mention).
'''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def main():
    P = json.load(io.open(os.path.join(D, 'b352_fit.json'), encoding='utf-8'))
    rec('=' * 100)
    rec('b352 -- COMPONENT 3: THE TWO FILINGS.')
    rec('=' * 100)

    # ---------------------------------------------------------------- FILING ONE.
    rec('')
    rec("  ### FILING ONE -- THE SPECTRAL VOID'S WIDTH, AS A WORK-ORDER NOTE.")
    txt = io.open(TRAILS, encoding='utf-8').read()
    if MARK in txt:
        st1, det1, wrote = 'DUPLICATE', 'mark already present -- REFUSED, nothing written', []
    else:
        r = git(PP, 'show', 'HEAD:OPEN_TRAILS.md')
        hb = r.stdout if r.returncode == 0 else None
        before = txt
        io.open(TRAILS, 'w', encoding='utf-8', newline=chr(10)).write(
            before.rstrip(chr(10)) + chr(10) + chr(10).join(block(P)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8').read()
        pw = after.startswith(before.rstrip(chr(10)))
        pb = (hb is not None) and norm(after).startswith(norm(hb).rstrip(chr(10)))
        ok = after.count(MARK) == 1 and pw and pb
        st1 = 'WRITTEN' if ok else 'READ-BACK FAILED'
        det1 = 'mark %d time(s); append-only working=%s blob=%s' % (after.count(MARK), pw, pb)
        wrote = ['OPEN_TRAILS.md'] if ok else []
    rec('    OPEN_TRAILS.md : %s -- %s' % (st1, det1))
    rec('    ### ### **THE PREFIX CHECK ABOVE IS THE PRE-PUSH READING, AND IT IS THE ONE THAT CARRIES.**')
    rec('    ### After the push the blob IS the file and the same check proves nothing about how the file')
    rec('    ### got there. ### That is filing two, applied to filing one.')
    tr = io.open(TRAILS, encoding='utf-8', errors='replace').read()
    blk = tr[tr.index(MARK):] if MARK in tr else ''
    v1 = '10.62' in blk
    v2 = 'b350' in blk
    v3 = 'decade' in blk and 'not "a decade"' in blk.replace('\u201c', '"').replace('\u201d', '"')
    v4 = 'under-determined' in blk
    v5 = 'NOT ATTEMPTED HERE' in blk
    rec('    the block carries the measured 10.62 : %s ; names b350 : %s' % (v1, v2))
    rec('    it says the width is NOT a round decade : %s ; the cut goes under-determined : %s' % (v3, v4))
    rec('    and it says NOT ATTEMPTED HERE : %s' % v5)

    # ---------------------------------------------------------------- FILING TWO.
    rec('')
    rec("  ### FILING TWO -- THE STRADDLING-GATE RULE, MINTED. ### LOCAL-ONLY, NOT PUSHED.")
    if not os.path.isdir(MODDIR):
        rec('    ### ### **HARD FAILURE -- the module directory does not exist: %s**' % MODDIR)
        st2 = 'REFUSED'
    elif os.path.exists(MODULE):
        st2 = 'DUPLICATE'
        rec('    %s : already present -- NOTHING WRITTEN.' % os.path.basename(MODULE))
    else:
        io.open(MODULE, 'w', encoding='utf-8', newline=chr(10)).write(MODULE_TEXT)
        st2 = 'WRITTEN'
        rec('    %s : WRITTEN (%d bytes)' % (os.path.basename(MODULE), len(MODULE_TEXT.encode('utf-8'))))
    mod = io.open(MODULE, encoding='utf-8').read() if os.path.exists(MODULE) else ''
    # ### ### **THROUGH THE SHARED NORMALISER, AND THE FIRST RUN OF THIS FILE IS WHY.** ### It asked
    # ### `'true prefix' in mod` and got False, because the module wraps between the two words. ### **AN ARM
    # ### INSIDE THE VERY FILE THAT MINTS THE WRAP-TOLERANT STRADDLE ARM WAS ITSELF WRAP-INTOLERANT**, and
    # ### the sortie built `quote_norm` in its step zero for exactly this. ### The first run is banked.
    rec('    the three incidents each named : %s'
        % all(quote_norm.contains(mod, q)
              for q in ('mirror_verify.py', 'b350_checks_run_prepush.txt', 'true prefix')))
    rec('    the mechanized half named and located : %s'
        % ('registration_gate.py' in mod and 'straddle_check' in mod))
    rec('    the judgement half filed APART from the mechanized one : %s'
        % ('NOT MECHANIZED, AND FILED AS JUDGEMENT' in mod))
    rec('    it says a scanner cannot decide which arms straddle : %s'
        % ('cannot be decided by a string' in mod))

    # ---------------------------------------------------------------- THE ARM ITSELF.
    rec('')
    rec("  ### THE MECHANIZED HALF, RUN. ### **ITS FIXTURES, BOTH POLARITIES:**")
    st_ok = RG.straddle_self_test(True)
    rec('    ### straddle fixtures : %s' % st_ok)
    reg = io.open(os.path.join(D, 'b352_registration_2026-09-07.txt'), encoding='utf-8').read()
    miss, nrepo = RG.straddle_check(reg)
    rec("  ### AND APPLIED TO THIS ACT'S OWN SEALED REGISTRATION, AS A MEASUREMENT:")
    rec('    arm-paragraphs touching a repository state : %d ; undeclared : %d' % (nrepo, len(miss)))
    for st, ln in miss:
        rec('      ### line %d  %s' % (st, ln))
    rec('    ### ### **AND THE REGISTRATION WAS SEALED BEFORE THIS ARM EXISTED**, so this is a test and not')
    rec('    ### ### a self-fulfilment. ### It is reported whichever way it came out.')

    # ---------------------------------------------------------------- THE CENSUS, RE-VERDICTING NOTHING.
    rec('')
    rec('  ### THE ARM OVER EVERY SEALED REGISTRATION IN THE RECORD. ### **A CENSUS. ### NOTHING IS')
    rec('  ### RE-VERDICTED, AND NO ACT IS ASKED TO ANSWER FOR A RULE THAT DID NOT EXIST WHEN IT RAN.**')
    regs = sorted(f for f in os.listdir(D) if f.startswith('b') and '_registration_' in f and f.endswith('.txt'))
    tot_r, tot_m, hits = 0, 0, []
    for f in regs:
        t2 = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
        m2, n2 = RG.straddle_check(t2)
        tot_r += n2
        tot_m += len(m2)
        if m2:
            hits.append((f, len(m2), n2))
    rec('    registrations scanned : %d ; arm-paragraphs touching a repository state : %d ; undeclared : %d'
        % (len(regs), tot_r, tot_m))
    for f, m2, n2 in hits[-12:]:
        rec('      %-46s undeclared %d of %d' % (f, m2, n2))
    rec('    ### ### **THAT IS A COUNT AND NOT A CHARGE.**')

    rec('')
    rec('  ### PLACE-papers files written this run : %d (CAP 1) ; TECHNE files written : %d (CAP 1, NOT PUSHED)'
        % (len(wrote), 1 if st2 == 'WRITTEN' else 0))
    rec('=' * 100)
    p = run_clock.write(D, 'b352_filings_run', LINES)
    io.open(os.path.join(D, 'b352_filings.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(trails=st1, detail=det1, mark=MARK, wrote=wrote, module=st2,
             module_path='modules/2026-09/STRADDLING_GATE.md', straddle_fixtures=bool(st_ok),
             reg_repo_paras=nrepo, reg_undeclared=len(miss),
             census_regs=len(regs), census_paras=tot_r, census_undeclared=tot_m,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if st1 in ('WRITTEN', 'DUPLICATE') and st2 in ('WRITTEN', 'DUPLICATE') and st_ok else 1


if __name__ == '__main__':
    sys.exit(main())
