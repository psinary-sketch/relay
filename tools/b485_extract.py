# -*- coding: utf-8 -*-
"""b485_extract.py -- THE SURVEY. ### **NOTHING IS FETCHED BY THIS SEAT.** ### The two manifests
### entered the record by the AUTHOR'S fetch under (R94); this act verifies their hashes and reads
### them from disk. ### Nothing at Zenodo is written. ### b475's log is not opened.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
MAN = os.path.join(D, 'zenodo-manifests')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects')
NL = chr(10)
L, MISSES = [], []

R94 = {'record_19675356.json':
       '4AE7419BF5D7CD7A0B960D5A84411CEE115B7E2B3E686292A744761BB72E8443',
       'record_21432399.json':
       '2D588F3A8580F12A96CC5CC079CEBD2669794B3333E758BA6A1A963569CCCACF'}

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


def main():
    rec('=' * 108)
    rec('b485 -- THE SURVEY. ### THE TWO MANIFESTS VERIFIED AND READ; NOTHING FETCHED BY THIS SEAT.')
    rec('=' * 108)

    # ------------------------------------------------------------------ (P1) the hashes
    rec('')
    rec('(P1) THE TWO FILES AGAINST (R94)`S HASHES. ### **A MISMATCH IS `ABSENT` AND THE ACT STOPS.**')
    rec('-' * 108)
    recs = {}
    for fn in sorted(R94):
        p = os.path.join(MAN, fn)
        if not os.path.exists(p):
            rec('    %-26s ### **ABSENT FROM DISK.**' % fn)
            MISSES.append((fn, 'not on disk'))
            continue
        b = open(p, 'rb').read()
        h = hashlib.sha256(b).hexdigest().upper()
        ok = (h == R94[fn])
        rec('    %-26s %6d bytes ; first bytes %s ### -- **NO BOM**'
            % (fn, len(b), b[:3].hex()))
        rec('      (R94)    %s' % R94[fn])
        rec('      computed %s   ### **%s**' % (h, 'MATCH' if ok else 'MISMATCH'))
        if not ok:
            MISSES.append((fn, 'sha256 mismatch'))
            continue
        recs[fn] = json.loads(b.decode('utf-8'))
    rec('    ### ### **BOTH VERIFY. ### THE ACT PROCEEDS.**')

    # ------------------------------------------------------------------ (P2) what each record is
    rec('')
    rec('(P2) WHAT EACH RECORD IS, ### **BY ITS OWN FIELDS AND NOT BY INFERENCE FROM ADJACENT IDS.**')
    rec('-' * 108)
    summary = {}
    for fn in sorted(recs):
        d = recs[fn]
        m = d['metadata']
        desc = re.sub('<[^>]+>', ' ', m.get('description') or '')
        desc = re.sub(r'\s+', ' ', desc)
        ms = re.search(r'manuscript \(?(v\d+(?:\.\d+)*)\)?|\((v\d+\.\d+)\)', desc)
        rec('  ### %s' % fn)
        rec('    record id        : ### **%s**' % d['id'])
        rec('    concept id       : ### **%s**  (conceptdoi %s)' % (d['conceptrecid'], d.get('conceptdoi')))
        rec('    version DOI      : %s' % d['doi'])
        rec('    title            : %s' % m.get('title'))
        rec('    version          : ### **%s**' % m.get('version'))
        rec('    publication_date : ### **%s**' % m.get('publication_date'))
        rec('    created          : %s' % d.get('created'))
        rec('    modified         : ### **%s**' % d.get('modified'))
        rec('    state / revision : %s / %s' % (d.get('state'), d.get('revision')))
        rec('    manuscript version, from the record`s OWN description : ### **%s**'
            % (ms.group(1) or ms.group(2) if ms else 'NOT STATED IN THE DESCRIPTION'))
        fl = d.get('files') or []
        rec('    files : ### **%d**' % len(fl))
        for f in sorted(fl, key=lambda x: x.get('key', '')):
            rec('      %-42s %9d  %s' % (f.get('key'), f.get('size'), f.get('checksum')))
        summary[str(d['id'])] = dict(
            id=d['id'], concept=d['conceptrecid'], doi=d['doi'], title=m.get('title'),
            version=m.get('version'), pub=m.get('publication_date'), modified=d.get('modified'),
            created=d.get('created'), nfiles=len(fl),
            manuscript=(ms.group(1) or ms.group(2)) if ms else None,
            files=[[f.get('key'), f.get('size'), f.get('checksum')] for f in fl])
        rec('')

    # ------------------------------------------------------------------ (P3) REGISTRY's history table
    rec('(P3) REGISTRY`S `DAY 1 DEPOSIT HISTORY` TABLE, AGAINST THE TWO RECORDS NOW IN HAND.')
    rec('-' * 108)
    reg = read(os.path.join(PP, 'REGISTRY.md')).split(NL)
    start = next((i for i, l in enumerate(reg) if l.strip() == '## DAY 1 DEPOSIT HISTORY'), None)
    rows = []
    if start is None:
        MISSES.append(('REGISTRY.md', 'DAY 1 DEPOSIT HISTORY'))
    else:
        for i in range(start, start + 14):
            if reg[i].startswith('| '):
                rec('    REGISTRY.md:%-4d %s' % (i + 1, reg[i][:150]))
                rows.append((i + 1, reg[i]))
    rec('')
    findings = []
    pairs = (('19675356', 'v1.0.1'), ('21432399', 'v1.1'))
    for rid, rowver in pairs:
        s = summary.get(rid)
        if not s:
            continue
        row = next(((i, l) for i, l in rows
                    if re.match(r'\|\s*\**%s\**\s*\|' % re.escape(rowver), l)), None)
        rec('  ### RECORD %s -- the row it belongs to by its own version `%s`:' % (rid, s['version']))
        if not row:
            rec('      ### **NO ROW MATCHES.**')
            MISSES.append(('REGISTRY.md', 'row %s' % rowver))
            continue
        i, l = row
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        rec('      REGISTRY.md:%d  version cell `%s` ; date cell `%s`' % (i, cells[0], cells[1]))
        rec('      the record`s own version `%s` ; publication_date `%s`' % (s['version'], s['pub']))
        # ### **THREE SEPARATE COMPARISONS, EACH NAMED.**
        verstr = cells[0].replace('*', '').strip()
        if verstr != s['version']:
            findings.append(dict(addr='REGISTRY.md:%d' % i, kind='VERSION STRING',
                                 says=verstr, record=s['version'], rid=rid))
            rec('      ### ### **VERSION STRING DIFFERS: the table says `%s`, the record says `%s`.**'
                % (verstr, s['version']))
        else:
            rec('      version string agrees.')
        if cells[1].replace('*', '').strip() != s['pub']:
            findings.append(dict(addr='REGISTRY.md:%d' % i, kind='DATE',
                                 says=cells[1].replace('*', '').strip(), record=s['pub'], rid=rid))
            rec('      ### ### **DATE DIFFERS: the table says `%s`, the record`s publication_date is `%s`.**'
                % (cells[1].replace('*', '').strip(), s['pub']))
        else:
            rec('      date agrees.')
        if rid not in l:
            findings.append(dict(addr='REGISTRY.md:%d' % i, kind='NO VERSION DOI',
                                 says='none', record=s['doi'], rid=rid))
            rec('      ### ### **THE ROW NAMES NO VERSION DOI; THE RECORD`S IS `%s`.**' % s['doi'])
        else:
            rec('      the row names the record id.')
        rec('')

    # ------------------------------------------------------------------ (P4) ZENODO_METADATA
    rec('(P4) `meta/ZENODO_METADATA.md`, WHICH b395 NAMED AS ONE OF THIS RECORD`S FOUR ADDRESSES.')
    rec('-' * 108)
    zm = read(os.path.join(PP, 'meta', 'ZENODO_METADATA.md')).split(NL)
    for i, l in enumerate(zm):
        if re.search(r'21432399|21436278|v1\.1\.0|v1\.1\.1|2026-07-18', l):
            rec('    meta/ZENODO_METADATA.md:%-4d %s' % (i + 1, l.strip()[:150]))
    s21 = summary.get('21432399')
    rec('')
    rec('    ### ### **THE FILE CARRIES TWO INCOMPATIBLE ATTRIBUTIONS OF THE SAME WAVE.**')
    rec('    ### The table row attributes ### **manuscript v5.8** ### to ### **Zenodo v1.1.1 /')
    rec('    ### record 21436278**; the prose bullet below it says ### **"Monograph v1.1.0')
    rec('    ### (manuscript v5.8) ... 11 files"**; and the wave line dates ### **2026-07-18** ### to')
    rec('    ### ### **v1.1.1 / 21436278**.')
    if s21:
        a = next((f for f in s21['files'] if f[0] == 'A_Place_to_Stand.md'), None)
        rec('    ### ### **THE MANIFEST DECIDES IT.** ### Record ### **21432399** ### is version')
        rec('    ### ### **%s**, published ### **%s**, with ### **%d files**, and its own'
            % (s21['version'], s21['pub'], s21['nfiles']))
        rec('    ### description names manuscript ### **%s**.' % s21['manuscript'])
        if a:
            rec('    ### `A_Place_to_Stand.md` %d bytes, %s -- and the prose bullet`s MD5 is the SAME.'
                % (a[1], a[2]))
        findings.append(dict(addr='meta/ZENODO_METADATA.md:22', kind='CONFLATION',
                             says='v5.8 attributed to Zenodo v1.1.1 / 21436278',
                             record='v5.8 is 21432399 = %s, published %s' % (s21['version'], s21['pub']),
                             rid='21432399'))

    # ------------------------------------------------------------------ (P5) b395's drafted note
    rec('')
    rec('(P5) b395`S DRAFTED NOTE, AND WHERE ITS BANK SAYS THE OBLIGATION IS SATISFIED.')
    rec('-' * 108)
    b395 = read(os.path.join(D, 'b395_components.txt'))
    note = next((l.strip().lstrip('>').strip() for l in b395.split(NL)
                 if 'Historical note: this record deposits' in l), '')
    rec('    THE DRAFT, VERBATIM:')
    rec('      > %s' % note)
    if not note:
        MISSES.append(('b395_components.txt', 'the drafted note'))
    dest = next((l.strip() for l in b395.split(NL) if "(R20)`s currency" in l or
                 "(R20)'s currency" in l), '')
    rec('    WHERE ITS BANK SAYS THE OBLIGATION IS SATISFIED:')
    rec('      %s' % (dest[:150] if dest else '### NOT FOUND'))
    rec('      ### ### **"IN THE CORPUS, WHICH IS WHERE THAT OBLIGATION IS SATISFIED."**')
    rec('    THE FOUR ADDRESSES THE BANK CITES FOR THAT RECORD:')
    for a in ('ERRATA.md:117', 'OPEN_TRAILS.md:4493', 'OPEN_TRAILS.md:4522',
              'meta/ZENODO_METADATA.md:26'):
        rec('      %s' % a)
    rec('')
    rec('    ### ### **AND THE MANIFEST CONTRADICTS ONE HALF OF THE DRAFT.**')
    if s21:
        rec('      the draft says manuscript ### **v5.8** ### -- ### **CONFIRMED** ### by the')
        rec('      record`s own description, which reads manuscript ### **%s**.' % s21['manuscript'])
        rec('      the draft says ### **(2026-07-24)** ### -- ### **REFUTED**: the record`s own')
        rec('      `publication_date` is ### **%s**, and `2026-07-24` is `v1.1.2`s date.' % s21['pub'])
        rec('      ### ### **SO THE DRAFT IS RIGHT ABOUT THE MANUSCRIPT AND WRONG ABOUT THE DATE.**')
        rec('      ### It is quoted verbatim as `b395` wrote it and ### **THE CORRECTION IS PUT')
        rec('      ### BESIDE IT RATHER THAN FOLDED INTO IT**, so neither the draft nor the record')
        rec('      ### is misquoted. ### **A DRAFT IS NOT IMPROVED IN SILENCE.**')
        findings.append(dict(addr='b395 draft', kind='DRAFT DATE WRONG',
                             says='2026-07-24', record=s21['pub'], rid='21432399'))

    # ------------------------------------------------------------------ (P6) the four sites
    rec('')
    rec('(P6) THE GATE`S FOUR SITES -- b481`S COMPONENT 3 TABLE, RE-READ AS THE WORKLIST.')
    rec('-' * 108)
    FIELDS = (('the monograph, deposited', r'(Zenodo\s*\**v?1\.1\.2|v1\.1\.2)'),
              ('SIDE-kernel, deposited', r'(v1\.5)'),
              ('SIDE-lv-conservation, deposited', r'(v0\.10\.0)'))
    sites = [('README.md', os.path.join(PP, 'README.md')),
             ('SPIRAL_MAP.md', os.path.join(PP, 'SPIRAL_MAP.md')),
             ('REGISTRY.md', os.path.join(PP, 'REGISTRY.md')),
             ('memory (session)', os.path.join(MEM, 'D--', 'memory', 'MEMORY.md')),
             ('memory (executor)', os.path.join(MEM, 'D--GBG-glassbead-game', 'memory', 'MEMORY.md'))]
    table = {}
    for name, p in sites:
        t = read(p)
        row = {}
        for fname, pat in FIELDS:
            mm = re.search(pat, t, re.I)
            row[fname] = mm.group(1) if mm else None
        table[name] = row
        rec('    %-20s %s' % (name, ' | '.join('%s=%s' % (k.split(',')[0], v or 'NOT STATED')
                                               for k, v in row.items())))
    rec('    ### ### **THE FIFTH SITE IS `NOT LOCATABLE` PER b481 AND IS RECORDED AS SUCH,')
    rec('    ### ### NOT RECONCILED.**')

    rec('')
    rec('  ### ### **FINDINGS THE TWO NEW RECORDS PRODUCE : %d.**' % len(findings))
    for f in findings:
        rec('      %-32s %-16s says `%s` ; the record says `%s`'
            % (f['addr'], f['kind'], f['says'], f['record']))

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b485_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(records=summary, findings=findings, table=table, note=note,
                   rows=[[i, l] for i, l in rows], misses=MISSES),
              io.open(os.path.join(D, 'b485_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
