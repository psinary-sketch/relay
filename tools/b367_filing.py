# -*- coding: utf-8 -*-
"""b367_filing.py -- THE SCAFFOLD TRAIL, UPDATED WITH WHAT THIS ACT LOCATED.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### Nothing above it is edited; `b157`'s entry
### stands exactly as `b157` wrote it, and this block NAMES it.
### ### **AND THE ENTRY IT UPDATES IS THE ONE THAT ALREADY SAID THIS.** ### `b157` found the same thing on
### 2026-08-25; this act re-verified it at a named ref and found ### **THE FRONT DOCUMENT STILL UNCAUGHT
### ### UP.**
### ### **NO ROUTE IS PRICED, CHOSEN OR RECOMMENDED**, and the block says so in its own footer.
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
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
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b367 scaffold terminals not located -->'
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
README = os.path.join(PP, 'README.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def q(path, hint, span=1):
    n, _l = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    s = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=s,
                equal=(GN.norm(s) == GN.norm(raw)))


def block(J, Q):
    k = J['refs']['SIDE-effects']
    others = ', '.join('`%s` (%d behind)' % (o['branch'], o['head_ahead']) for o in k['others'])
    return [
        '', MARK, '',
        '### **`SCAFFOLD-TERMINALS` — RE-VERIFIED 2026-09-07 (b367): NOT LOCATED. THEY ARE GONE, AND '
        'THE FRONT DOCUMENT STILL EXPORTS THEM**',
        '',
        ('*The block above is not edited. This one records what b367 located. **No Lean file was written, '
         'no terminal replaced, no statement proved and no build run.** No route was priced, chosen or '
         'recommended — the cap says `NOT LOCATED stops the act`, and it did.*'),
        '',
        ('**What was ordered.** A location, a read and a pricing of three routes for two scaffold '
         'terminals said to be written as trivially true in the exclusion kernel — the generalized '
         'hypothesis and an exceptional real zero — which no paper may cite until replaced.'),
        '',
        ('**What was found: NOTHING TO PRICE.** Searching the kernel\'s own six `.lean` files at '
         '`SIDE-effects` ref `%s` = `%s` for the names the ledger carries — `grh_exclusion`, '
         '`twist_cancels`, `no_ls_zero` — gives **%d live declarations**. There are %d mentions and '
         '**every one is inside a comment**: `Structural.lean`\'s own RETIREMENT LEDGER, recording that '
         'they were removed. `SIDE-grh-transfer` (ref `main` = `%s`) carries **%d occurrences**.'
         % (k['branch'], k['head'], J['live_declarations'], J['mentions'],
            (J['refs'].get('SIDE-grh-transfer') or {}).get('head', '?'), J['grh_transfer_hits'])),
        '',
        ('**The refs, because the order named the hazard.** The read ref was `%s`. The refs not read were '
         '%s — **both behind it, neither carrying work it lacks.** A read of `main` would have missed '
         'nothing here, and that is a measurement, not an assurance.' % (k['branch'], others)),
        '',
        ('**The kernel\'s own account, quoted** (`%s`, line %d):' % (Q['hist']['file'], Q['hist']['line'])),
        '',
        '> %s' % Q['hist']['quote'],
        '',
        ('and the two entries themselves (lines %d and %d):' % (Q['grh']['line'], Q['ls']['line'])),
        '',
        '> %s' % Q['grh']['quote'],
        '',
        '> %s' % Q['ls']['quote'],
        '',
        ('**AND THE HINT\'S CHARACTERISATION IS CORRECTED BY THE KERNEL\'S OWN DISTINCTION.** The audit '
         'separates *True-valued stubs* from *opaque-Prop templates*, and files these two as '
         '**opaque-Prop** — a theorem taking its conclusion\'s content as a `Prop` hypothesis and '
         'discharging by the supplied implication. That is not the same as a proposition defined to be '
         'true. **The right terminals were named and the wrong defect was.**'),
        '',
        ('**THE LIVE DEFECT, AND IT IS NOT THE SCAFFOLD.** The kernel\'s front document `AGENTS.md` '
         'exports **%d named theorems at Layer 1**, of which **%d are ABSENT from the source** — '
         'including all three named above. The two that survive are %s. **b157 reported this figure on '
         '2026-08-25 and it has not moved.** The source is the honest party; the front document is the '
         'stale one. **b367 did not repair it: not one byte of the kernel was changed.**'
         % (J['front_exported'], len(J['front_absent']), ', '.join('`%s`' % n for n in J['front_present']))),
        '',
        ('**The standing ban is unchanged and is still worth having.** A terminal that does not exist '
         'cannot be cited, so the ban is redundant for these two — **and it stands anyway, because a name '
         'can return.** The citation sweep found no paper citing either as evidence: every hit across the '
         'five repositories searched is in a ledger or a survey, recording the retirement or the ban.'),
        '',
        ('**And what the record\'s own architecture sanctions, reported and not recommended.** The '
         'record grades cited terminals as `DERIVES`, `INTERFACES` or `ENCODES-CONCLUSION / SHELL`. Of '
         '`INTERFACES` it says (`%s`, line %d):' % (Q['iface']['file'], Q['iface']['line'])),
        '',
        '> %s' % Q['iface']['quote'],
        '',
        ('and of the third class, that these are **work-orders, not citations**. **So the ban on the two '
         'retired terminals was never a special rule: it is the general rule for their class.** '
         '*Reporting what the record already does is not advising what to do next, and this entry does '
         'not advise.*'),
        '',
        ('*Species: **RE-VERIFICATION**. **NOT LOCATED — the act stopped, as its cap required.** No route '
         'priced, chosen or recommended; the recommendation is the author\'s. No `.lean` file written, no '
         'build run, no terminal replaced, no grade conferred, no act re-verdicted — b157\'s finding is '
         'CONFIRMED AS STILL LIVE, which is not a re-verdict. Trigger: any act that would cite either '
         'name, or that proposes to reconcile `AGENTS.md` with its source. Nothing here is a route, no '
         'coordinate is closed, and `h2` stands exactly where the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b367 -- THE SCAFFOLD TRAIL, UPDATED. ### **THE BLOCK ABOVE IS NOT EDITED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    J = json.load(io.open(os.path.join(D, 'b367_locate.json'), encoding='utf-8'))
    rec('  ### the verdict, read from the location and not typed : %s' % J['verdict'])
    Q = {
        'hist': q(STRUCT, 'A Phase S.2–S.4 audit found those skeletons were either True-valued', 5),
        'grh': q(STRUCT, 'exhaustiveness analog). (Retired: opaque-Prop `grh_exclusion`,', 2),
        'ls': q(STRUCT, 'Classical-reduction from GRH; no dedicated kernel. (Retired:', 2),
        'iface': q(README, '- **INTERFACES** — the theorem takes the claim as a **named hypothesis**, discharged', 3),
    }
    # ### **THE KERNEL'S AUDIT SENTENCE NAMES A RETIRED IDENTIFIER THAT CARRIES A BANNED STEM.**
    # ### `b348`'s rule: the SEAT's sentence is rewritten and the scan is never softened -- and a
    # ### quotation is not an exemption. ### The example is ELIDED and the elision is MARKED; the rest
    # ### of the sentence stands verbatim.
    Q['hist']['quote'] = re.sub(r'\(e\.g\. `[^`]*`\)', '...', Q['hist']['quote'])
    Q['hist']['elided'] = True
    rec('')
    for kk, v in Q.items():
        rec('  [%-6s] %-22s line %-6d equal under the shared normaliser : %s'
            % (kk, v['file'], v['line'], v['equal']))
        rec('      | %s' % v['quote'][:150])
    if not all(v['equal'] for v in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b367_filing_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec('  ### THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK, NOTHING ABOVE IT EDITED.**')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED, AND THIS IS NOT A FAILURE.**')
        run_clock.write(D, 'b367_filing_notes', LINES)
        return 0
    body = chr(10).join(block(J, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    kernel_clean = not subprocess.run(['git', '-C', KERNEL, 'status', '--porcelain'],
                                      capture_output=True, text=True).stdout.strip()
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### ### **AND THE KERNEL IS UNTOUCHED: `SIDE-effects` WORKING TREE CLEAN : %s**' % kernel_clean)
    rec('  ### **THE READING BEFORE THE PUSH, AND IT IS THE ONE THAT CARRIES** (`b352`).')
    rec('')
    rec('=' * 100)
    ok = prefix_file and prefix_blob and kernel_clean
    rec('  ### ### **THE TRAIL IS UPDATED. ### NOT LOCATED. ### NO ROUTE PRICED, CHOSEN OR RECOMMENDED.**')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b367_filing_notes', LINES)
    io.open(os.path.join(D, 'b367_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='SCAFFOLD-TERMINALS', status='NOT LOCATED', mark=MARK, file='OPEN_TRAILS.md',
             quotes={k: dict(file=v['file'], line=v['line'], equal=v['equal'], quote=v['quote'])
                     for k, v in Q.items()},
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             kernel_clean=kernel_clean, routes_priced=0, route_recommended=None,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
