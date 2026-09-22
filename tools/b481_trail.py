# -*- coding: utf-8 -*-
"""b481_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**
### The file is opened in BINARY, the prior bytes are held, the new bytes are appended, and the
### read-back proves the prior bytes are a TRUE PREFIX of the result. ### Nothing else is touched.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

W = json.load(io.open(os.path.join(D, 'b481_worklist.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b481_span.json'), encoding='utf-8'))

ENTRY = """
### b481 — the circulation gate, read for what it needs — filed 2026-09-22

**`REGISTRY.md:523` is the only gate in the corpus that binds *reading-out* rather than writing-in**, and this act reads it for what it needs rather than running it. It needs three things, and **the record supplies none of them.** Nothing was fetched, no lane was opened, no site was edited, and both detached runs were left alive with their logs unread — the act reads only files already on disk, as `(R89)` permits.

#### Component 1 — the gate and its trigger

The line is **1,166 characters** and is quoted whole in `data/b481_components.txt`. Its last clause is the trigger:

> **Run when the (c') validation job clears.**

Every live `.md` of the corpus was walked, the archive excluded, for `(c')` in any apostrophe. **Four lines carry it:**

| address | what it is |
|:--|:--|
| `REGISTRY.md:523` | **the gate's own trigger** |
| `phase1.5/method/INSTRUMENTS.md:294` | the **(c′) benchmark**, adopted as a re-platform instrument |
| `phase1.5/method/INSTRUMENTS.md:298` | the benchmark's production-shape clause |
| `phase1.5/method/INSTRUMENTS.md:304` | the benchmark's combined figure, **55.3×** |

**STATE OF THE (c') VALIDATION JOB: ABSENT.** No such job is defined anywhere in the live corpus and no state for one is recorded. The three non-trigger lines are a **benchmark that priced a library swap** — a different object, with nothing to clear and no clearing state. **A near name is not the thing**, and this act does not quietly promote the benchmark into the job the gate waits on.

**What would settle it, named and not supplied:** *(i)* an author's ruling that names the `(c')` validation job, or states that the trigger means the `(c′)` benchmark and that the benchmark has cleared; *(ii)* or an entry at a quotable address — a REGISTRY row, an `OPEN_TRAILS` entry, a relay bank — recording that job's state and the date it took it; *(iii)* or a ruling that strikes the trigger clause, leaving the gate to bind on its own terms. **Until one of those exists the gate's trigger points at nothing the record can read, so the gate neither clears nor fails: it waits on an absent name.**

#### Component 2 — the bar is CAPABILITY, not permission

For record **21432399**, `b395` drafted the historical note and said where it goes in its own words: *"IT IS DRAFTED HERE AND IS WRITTEN NOWHERE. The platform is not called."* Its destination is the Zenodo record itself — which is why no later act could have written it into the corpus. For record **19675356**, the deposited version is *"recorded **NOWHERE IN THE CORPUS**"*, and the smallest recovering read is *"one authenticated fetch of that record's own file manifest, compared against the repository's history. **ONE RECORD, ONE READ, NO CRAWL.**"*

The deciding sentence, quoted:

> **"WHO CAN PERFORM IT: NOT THIS SEAT.** `b389` proved the platform answers on none of six routes from here with a positive control at `200`; this act did not call it at all. **IT IS THE AUTHOR'S READ, OR A SEAT WITH CREDENTIALS AND A LIVE ROUTE."**

**VERDICT: CAPABILITY.** The bank names two missing things and **neither is a permission**: an *authenticated* fetch needs **credentials**, and `b389` measured **six dead routes with a positive control returning 200** to prove the measurement could see a live route if one existed. **A ruling supplies neither.**

And the permission half of the navigator's argument is separately **borne out** — which is precisely why permission is not the bar. `b145` records *"THE DEPOSITED RECORDS (4), all fetched read-only at b144 and unchanged here"*; `b337` records *"PASS (1) the fetch agrees"* with the fetched JSON banked as `b337_record.json`. **The corpus has twice read the platform without writing to it, and nothing forbids a third such read.** What is missing is not a ruling but a route and a credential.

#### Component 3 — the worklist, listed and not run

| site | monograph | SIDE-kernel | SIDE-lv-conservation |
|:--|:--|:--|:--|
| `README.md` | v1.1.2 — **agrees** | v1.5 — **agrees** | v0.10.0 — **agrees** |
| `SPIRAL_MAP.md` | Zenodo v1.1.2 — **agrees** | v1.5 — **agrees** | v0.10.0 — **agrees** |
| `REGISTRY.md` *(authority, Rule 5)* | v1.1.2 | v1.5 | v0.10.0 |
| memory — session | Zenodo v1.1.2 — **agrees** | v1.5 — **agrees** | **NOT STATED** |
| memory — executor | **NOT STATED** | **NOT STATED** | **NOT STATED** |

**DISAGREEMENTS WITH REGISTRY: 0.** **`NOT STATED` is not a disagreement** — a site that says nothing about a field cannot contradict the authority on it — **and it is not a match either.** The gate's own words are *"both memories (session + executor)"*, and one memory that agrees does not satisfy them: **the executor memory the gate names is not locatable at this seat**, the other store on this machine carrying no deposit-state line at all. So the gate's fifth site can be neither reconciled nor declared clean here, and its remaining requirement — *"against a fetch of the live Zenodo records"* — is unmet for Component 2's reason.

**Nothing is corrected by this act and no site is edited. The gate is not run, and nothing circulates.**

#### The expectations, scored

| | the navigator's | verdict |
|:--|:--|:--|
| **(N1)** | the `(c')` job's state is not in the record | **HELD** |
| **(N2)** | the bar is PERMISSION | **REFUTED** — it is CAPABILITY, and a ruling cannot lift it |
| **(N3)** | at least two of the four sites differ from REGISTRY | **REFUTED** — **zero** differ |

*The seat's own, registered before the seal and so refutable:* `(N1)` **HELD**, `(N2)` **REFUTED**, `(N3)` **REFUTED** — all three called at registration and all three borne out by the survey.

#### What this act does not do

**No claim is made about RH in either direction.** No corpus grade moves; row U1 is unedited; no bridge is typed; `h2` stays where the deposit left it; the four lists stay OPEN. Nothing is imported, copied or vendored. **The two detached runs — the `b475` serialized build and the `b477` Gram run — were neither polled nor stopped, and neither log was opened.**

The span by the tool reads **{span}**. The desk stands at **forty**, four minted here: *a gate waits on a job the record does not carry*; *the bar on the deposited records is capability, not permission*; *a drafted note eighty-six acts old is still written nowhere*; *the gate's fifth site is not locatable at this seat*.
"""

ENTRY = ENTRY.replace('{span}', str(SPAN['current_span']))


def main():
    before = io.open(OT, 'rb').read()
    tail = before.decode('utf-8-sig', 'replace')[-2:]
    sep = '' if tail.endswith(NL + NL) else (NL if tail.endswith(NL) else NL + NL)
    add = (sep + ENTRY.strip(NL) + NL).encode('utf-8')
    io.open(OT, 'ab').write(add)
    after = io.open(OT, 'rb').read()

    print('=' * 96)
    print('b481_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b481 ')]
    print('  b481 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b481_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
