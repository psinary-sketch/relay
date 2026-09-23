# -*- coding: utf-8 -*-
"""b499_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEADING = ('### b499 — the ten metadata edits applied at Zenodo by API and fetched back: '
           'three MATCHES; the guard scans for the token')


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def main():
    R = json.loads(io.open(os.path.join(D, 'b499_results.json'), encoding='utf-8').read())
    SC = json.loads(io.open(os.path.join(D, 'b499_scores.json'), encoding='utf-8').read())
    G = json.loads(io.open(os.path.join(D, 'b499_guard.json'), encoding='utf-8').read())
    c0, c1, c2 = R['c0'], R['c1'], R['c2']['records']
    ents = c1['entities']
    fb = '; '.join('`%s` sha256 `%s…`' % (k, c2[k]['fetchback_sha256'][:16])
                   for k in ('21539068', '21520474', '21539167'))
    body = """
%(heading)s

**(R110) ratified.** The seat may write the title and description of the three `(R109)` records at
Zenodo by the legacy edit / PUT / publish sequence — no new version, no file — the token in the
environment only, every write fetched back anonymously and compared. **The standing line is from
this act on: nothing at Zenodo written by the seat outside (R110).** **(R111) ratified.** Texts [5]
and [6] amended in the v2 file on the record's own statement-reads; the ERRATA entry records both.

**STEP (G) — THE GUARD.** `(R110)` says the pre-push guard scans every commit for the token; **when
the ferry arrived it did not**. The seat asked, and the author chose to have the limb added here,
before any use of the token: limb (v) of `.githooks/pre-push` reads `ZENODO_TOKEN` through `awk`'s
`ENVIRON` and refuses any outgoing commit whose patch or message carries it; with the variable
unset it **warns** and does not refuse. Byte-identical in relay, PLACE-papers, SIDE-global-section
and SIDE-explicit-formula (`%(hook)s…`). Exercised in a scratch clone with a **fake** value: refused
when carried, passed when clean, warned when unset, the value never printed. **The first exercise
was void** — `reset --hard` restored the committed old guard after its first case — and was repaired
and re-run; both banks are kept.

**COMPONENT 0.** The token: length **%(len)d**, sha256 prefix `%(pre)s`; the monograph's deposition
**HTTP %(st)d**.

**COMPONENT 1 — THE PLAN.** Three before-states banked. **Ten of ten targets FOUND ONCE.** The extent
rule sealed on the face — the old span ends at the K-th sentence end, K the sentence ends of the
replacement — cut the right span for each, the heading sentences (`MAIN THEOREM.`, `THE PROOF IN TWO
FORMS.`, `…AS OPEN.`) included. Entity sites in the returned descriptions: %(ents)s. The monograph's
live description is byte-identical to the b359 bank.

**COMPONENT 2 — THE WRITES.** In order `21539068`, `21520474`, `21539167`: edit **201**, PUT **200**
with every other key carried, publish **202**, on all three; **each anonymous fetch-back MATCHED on its
first try, all four limbs of the sealed rule true**, and the raw bytes equal as well. Same DOI, same
version, still the last version, file checksums unchanged. Fetch-backs: %(fb)s.

**COMPONENT 3 — THE RECORD.** ERRATA **`E-2026-09-23-1`** appended through `errata_append.py`,
prior bytes a true prefix, listing the ten edits before and after, the three record URLs, the
fetch-back digests and `(R111)`'s amendments with their authority. Eight notes inserted beside
`REGISTRY.md:77, 82, 94, 98, 414` and `meta/ZENODO_METADATA.md:8, 9, 10`, at the points the face
sealed, each named line verified unchanged first; **no prior line edited or removed**, and the two
table-side notes carry one leading blank line each so the table does not swallow them.

**(N1) %(n1)s** · **(N2) %(n2)s** · **(N3) %(n3)s** — held on its cell, and its "so" is true of
whole sentences only: all seven start phrases are plain ASCII, so a start-phrase match would not
have failed anywhere. The seat's own: **(S1) %(s1)s, (S2) %(s2)s, (S3) %(s3)s** — the platform
stored and served the HTML exactly as sent.

Nothing at Zenodo written by the seat outside (R110); no grade conferred; nothing deposits; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; K1, K2 and K3 not started.
""" % dict(heading=HEADING, hook=G['after'][list(G['after'])[0]][:12], len=c0['length'],
           pre=c0['prefix'], st=c0['status'], ents=ents, fb=fb,
           n1=w(SC['n1']), n2=w(SC['n2']), n3=w(SC['n3']), s1=w(SC['s1']), s2=w(SC['s2']),
           s3=w(SC['s3']))
    tok = os.environ.get('ZENODO_TOKEN') or ''
    if tok and tok in body:
        print('### THE TOKEN IS IN THE RECORD -- REFUSED.')
        return 3
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8', 'replace'):
        print('### ALREADY PRESENT -- REFUSING A SECOND RECORD.')
        return 2
    with open(OT, 'ab') as fh:
        fh.write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl = before.decode('utf-8').replace(chr(13), '').split(NL)
    al = after.decode('utf-8').replace(chr(13), '').split(NL)
    removed = len(bl) - sum(1 for a, b in zip(al, bl) if a == b)
    out = dict(bytes_added=len(after) - len(before), prefix=after.startswith(before),
               lines_removed=removed, headings=after.decode('utf-8').count(HEADING),
               esc=after[len(before):].count(b'\x1b'),
               before_sha=hashlib.sha256(before).hexdigest(), after_sha=hashlib.sha256(after).hexdigest())
    msg = ('OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, %(lines_removed)d lines '
           'removed, %(headings)d heading, %(esc)d ESC bytes' % out)
    print('  ' + msg)
    json.dump(out, io.open(os.path.join(D, 'b499_trail_notes.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    io.open(os.path.join(D, 'b499_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(msg + NL)
    return 0 if (out['prefix'] and removed == 0 and out['headings'] == 1 and out['esc'] == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
