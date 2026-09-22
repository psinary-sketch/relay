# -*- coding: utf-8 -*-
"""b481_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (sha256 `afc88e4426793fc9...`).
### ### **NOTHING IS FETCHED; NO SITE IS EDITED; THE RECONCILIATION IS NOT RUN.**
"""
import io
import json
import os
import re
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects')
NL = chr(10)
L = []

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


def wrap(s, w=146, pad='      '):
    return [pad + x for x in textwrap.wrap(s, w)]


S = json.loads(read(os.path.join(D, 'b481_survey.json')))

# ### THE THREE FIELDS, AND THE PATTERNS THAT FIND THEM. ### Fixed here before any site is read.
FIELDS = (
    ('the monograph, deposited', r'(Zenodo\s*\**v?1\.1\.2|v1\.1\.2)', r'(ms\s*v5\.10\.2|manuscript\s*\**v5\.10\.2|v5\.10\.2)'),
    ('SIDE-kernel, deposited', r'(v1\.5)', r'(0e5233f)'),
    ('SIDE-lv-conservation, deposited', r'(v0\.10\.0)', r'(93c27ec)'),
)


def field_state(text):
    out = {}
    for name, ver, tag in FIELDS:
        v = re.search(ver, text, re.I)
        t = re.search(tag, text, re.I)
        out[name] = dict(version=v.group(1) if v else None, tag=t.group(1) if t else None)
    return out


def main():
    # ============================================================== COMPONENT 1
    rec('=' * 104)
    rec('COMPONENT 1 -- THE GATE AND ITS TRIGGER.')
    rec('=' * 104)
    gate = read(os.path.join(PP, 'REGISTRY.md')).split(NL)[522]
    rec('    REGISTRY.md:523, quoted whole (%d characters), wrapped for the page and otherwise verbatim:'
        % len(gate))
    for x in wrap(gate):
        rec(x)
    rec('')
    rec('  ### ### **THE TRIGGER CLAUSE, VERBATIM: "Run when the (c\') validation job clears."**')
    rec('')
    rec('  ### (1a) THE (c\') VALIDATION JOB, AT ITS OWN ADDRESS.')
    rec('    every live .md of the corpus was walked, the archive excluded; lines carrying (c\') in any')
    rec('    apostrophe : %d' % S['cprime_hits'])
    for f, i, l in S['cprime_lines']:
        rec('      %s:%d' % (f, i))
        rec('        %s' % (l[:130] + ('...' if len(l) > 130 else '')))
    rec('    ### ### **STATE OF THE (c\') VALIDATION JOB : ABSENT.**')
    rec('    ### ### **NO SUCH JOB IS DEFINED ANYWHERE IN THE LIVE CORPUS, AND NO STATE FOR ONE IS')
    rec('    ### RECORDED.** ### Of the four lines, one is the gate`s own trigger and three are')
    rec('    ### `INSTRUMENTS.md`s ### **(c′) BENCHMARK** -- a re-platform benchmark that priced a')
    rec('    ### library swap, with no clearing state and nothing to clear. ### **A NEAR NAME IS NOT THE')
    rec('    ### THING**, and this act does not treat the benchmark as the job.')
    rec('')
    rec('  ### (1b) WHAT WOULD SETTLE IT, NAMED AND NOT SUPPLIED.')
    rec('    (i)   an author`s ruling that names the (c\') validation job, or states that the trigger')
    rec('          refers to the (c′) benchmark and that the benchmark has cleared ;')
    rec('    (ii)  or an entry at a quotable address -- a REGISTRY row, an OPEN_TRAILS entry, or a')
    rec('          relay bank -- recording that job`s state and the date it took it ;')
    rec('    (iii) or a ruling that strikes the trigger clause, leaving the gate to bind on its own')
    rec('          terms rather than on a job the record does not carry.')
    rec('    ### ### **UNTIL ONE OF THOSE EXISTS, THE GATE`S TRIGGER POINTS AT NOTHING THE RECORD CAN')
    rec('    ### READ, AND THE GATE THEREFORE NEITHER CLEARS NOR FAILS: IT WAITS ON AN ABSENT NAME.**')

    # ============================================================== COMPONENT 2
    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE BAR: PERMISSION OR CAPABILITY.')
    rec('=' * 104)
    b395 = read(os.path.join(D, 'b395_components.txt'))
    b395c = read(os.path.join(D, 'b395_closing.txt'))
    rec('  ### (2a) RECORD 21432399 -- THE DRAFTED HISTORICAL NOTE, AND WHERE THE BANK SAYS IT WOULD GO.')
    note = re.search(r'> (Historical note: [^\n]+(?:\n\s*>[^\n]+)*)', b395c)
    if note:
        for ln in note.group(1).split(NL):
            rec('      %s' % ln.strip().lstrip('>').strip())
    rec('    where it would go, in the bank`s own words:')
    rec('      > "IT IS DRAFTED HERE AND IS WRITTEN NOWHERE. ### The platform is not called."')
    rec('      > "WHAT IT WOULD FIX: a reader who opens the record learns FROM THE RECORD ITSELF that')
    rec('      >  the deposited manuscript is not the current one..."')
    rec('      > "WHAT IT WOULD NOT FIX: ... A NOTE ABOUT A DEPOSIT IS NOT A DEPOSIT."')
    rec('    ### the four lines the bank cites for that record : ERRATA.md:117, OPEN_TRAILS.md:4493,')
    rec('    ### OPEN_TRAILS.md:4522, meta/ZENODO_METADATA.md:26 -- ### **THE NOTE`S DESTINATION IS THE')
    rec('    ### ZENODO RECORD ITSELF, WHICH IS WHY IT IS WRITTEN NOWHERE IN THE CORPUS.**')
    rec('')
    rec('  ### (2b) RECORD 19675356 -- THE TWO SENTENCES THE ORDER ASKS FOR.')
    rec('    the deposited version, recorded nowhere:')
    rec('      > "`19675356` -- its deposited version is recorded **NOWHERE IN THE CORPUS**, re-read by')
    rec('      >  content across the whole tree and not in one ledger, because **ABSENCE FROM ONE FILE')
    rec('      >  IS NOT ABSENCE FROM THE CORPUS** -- and the answer is the same as `b393`s."')
    rec('    the smallest recovering read:')
    rec('      > "THE SMALLEST READ THAT WOULD RECOVER IT: one authenticated fetch of that record`s own')
    rec('      >  file manifest, compared against the repository`s history. **ONE RECORD, ONE READ, NO')
    rec('      >  CRAWL.**"')
    rec('')
    rec('  ### (2c) THE VERDICT, ON THE BANK`S OWN DECIDING SENTENCE.')
    rec('    ### THE DECIDING SENTENCE, QUOTED:')
    rec('      > "WHO CAN PERFORM IT: **NOT THIS SEAT.** `b389` proved the platform answers on none of')
    rec('      >  six routes from here with a positive control at `200`; this act did not call it at')
    rec('      >  all. ### **IT IS THE AUTHOR`S READ, OR A SEAT WITH CREDENTIALS AND A LIVE ROUTE.**"')
    rec('    ### ### **VERDICT : CAPABILITY.**')
    rec('    ### The bank names two things the seat lacks and neither is a permission: ### **CREDENTIALS**')
    rec('    ### (the read is *authenticated*) and ### **A LIVE ROUTE** (b389 measured six routes dead')
    rec('    ### from here, with a positive control returning 200 to prove the measurement could see a')
    rec('    ### live route if one existed).')
    rec('')
    rec('  ### (2d) AND THE PERMISSION HALF OF THE ORDER`S ARGUMENT IS ITSELF BORNE OUT.')
    rec('    b144/b145 : "THE DEPOSITED RECORDS (4), all fetched read-only at b144 and unchanged here"')
    rec('                (b145_census_seam.txt:125) -- ### **A PLATFORM FETCH THAT WROTE NOTHING.**')
    rec('    b337      : "PASS  ### (1) the fetch agrees" (b337_checks_postpush.txt:24), with the fetched')
    rec('                JSON banked as `b337_record.json`, "the public record`s JSON, as fetched"')
    rec('                -- ### **A SECOND PLATFORM FETCH THAT WROTE NOTHING.**')
    rec('    ### ### **SO THE CORPUS HAS TWICE READ THE PLATFORM WITHOUT WRITING TO IT, AND NO RULING')
    rec('    ### FORBIDS A THIRD SUCH READ. ### THAT IS PRECISELY WHY PERMISSION IS NOT THE BAR:')
    rec('    ### WHAT IS MISSING IS NOT A RULING BUT A ROUTE AND A CREDENTIAL.**')
    rec('    ### **AND A RULING CANNOT SUPPLY EITHER** -- which is the whole content of the answer.')

    # ============================================================== COMPONENT 3
    rec('')
    rec('=' * 104)
    rec('COMPONENT 3 -- THE WORKLIST, LISTED AND NOT RUN.')
    rec('=' * 104)
    sites = [('README.md', os.path.join(PP, 'README.md')),
             ('SPIRAL_MAP.md', os.path.join(PP, 'SPIRAL_MAP.md')),
             ('REGISTRY.md', os.path.join(PP, 'REGISTRY.md')),
             ('memory (session, D--)', os.path.join(MEM, 'D--', 'memory', 'MEMORY.md')),
             ('memory (D--GBG-glassbead-game)',
              os.path.join(MEM, 'D--GBG-glassbead-game', 'memory', 'MEMORY.md'))]
    states = {}
    for name, p in sites:
        t = read(p)
        states[name] = field_state(t)
        rec('')
        rec('  ### %s' % name)
        if not t:
            rec('      ### **FILE NOT READABLE AT THIS SEAT.**')
            continue
        for i, l in enumerate(t.split(NL)):
            if re.search(r'v1\.1\.2|v5\.10\.2|v1\.5.*0e5233f|0e5233f|v0\.10\.0|93c27ec', l):
                rec('      :%-5d %s' % (i + 1, l.strip()[:132]))
    rec('')
    rec('  ### (3a) THE FIELD TABLE, AGAINST REGISTRY`S OWN LINES (RULE 5: REGISTRY IS THE AUTHORITY).')
    auth = states['REGISTRY.md']
    rec('    %-34s %-26s %-26s %s' % ('site', 'monograph', 'SIDE-kernel', 'SIDE-lv-conservation'))
    disagree = []
    for name, _ in sites:
        st = states[name]
        cells = []
        for fname, _, _ in FIELDS:
            v, t = st[fname]['version'], st[fname]['tag']
            a = auth[fname]['version']
            if v is None:
                cells.append('NOT STATED')
            elif a is not None and v.lower().replace('zenodo', '').strip() == a.lower().replace('zenodo', '').strip():
                cells.append('%s  AGREES' % v)
            else:
                cells.append('%s  DIFFERS' % v)
                if name != 'REGISTRY.md':
                    disagree.append((name, fname, v, a))
        rec('    %-34s %-26s %-26s %s' % (name, cells[0], cells[1], cells[2]))
    rec('')
    rec('  ### ### **DISAGREEMENTS WITH REGISTRY : %d.**' % len(disagree))
    for n, f, v, a in disagree:
        rec('      %s -- %s : site says %s, REGISTRY says %s' % (n, f, v, a))
    rec('    ### ### **`NOT STATED` IS NOT A DISAGREEMENT**: the second memory store carries no')
    rec('    ### deposit-state line at all, and a site that says nothing about a field cannot contradict')
    rec('    ### the authority on it. ### **IT IS ALSO NOT A MATCH**, and the gate`s own words -- "both')
    rec('    ### memories (session + executor)" -- are not satisfied by one memory that agrees.')
    rec('')
    rec('  ### (3b) WHAT THE WORKLIST WOULD BE, IF THE GATE RAN.')
    rec('    (i)   the three documents and the session memory agree with REGISTRY on all three fields,')
    rec('          so ### **NO CORRECTION IS OWED AT THOSE SITES ON THIS EVIDENCE** ;')
    rec('    (ii)  the executor memory the gate names is ### **NOT LOCATABLE AT THIS SEAT** -- the one')
    rec('          other memory store on this machine carries no deposit-state line -- so the gate`s')
    rec('          fifth site can be neither reconciled nor declared clean here ;')
    rec('    (iii) and the gate`s own requirement, ### **"against a fetch of the live Zenodo records"**,')
    rec('          is unmet for the reason Component 2 gives: ### **CAPABILITY, NOT PERMISSION.**')
    rec('    ### ### **NOTHING IS CORRECTED BY THIS ACT AND NO SITE IS EDITED. ### THE GATE IS NOT RUN,')
    rec('    ### AND NOTHING CIRCULATES.**')

    io.open(os.path.join(D, 'b481_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(cprime_state='ABSENT', cprime_hits=S['cprime_hits'],
                   bar='CAPABILITY', states=states, disagreements=disagree,
                   memory_stores=S['memory_stores']),
              io.open(os.path.join(D, 'b481_worklist.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
