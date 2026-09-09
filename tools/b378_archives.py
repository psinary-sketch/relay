# -*- coding: utf-8 -*-
"""b378_archives.py -- ADDITION THREE: ### **THE ARCHIVES, CONFIRMED AND NOT REMOVED.**

### For each archive file the project mirror carries, a copy on the canonical drive is confirmed by
### ### **A VERIFIED DIGEST AND BY A TITLE-LINE OR CONTENT MATCH.**
### ### ### **NEVER BY FILENAME.** ### The mirror export is FLAT: its builder derives each archive name
### from the source path -- leaf, or parent-directory plus leaf on collision -- so ### **A NAME IN THE
### ### ARCHIVE NEED NOT BE THE NAME ON DISK**, and the repository strips version suffixes besides.
### **A NAME MATCH IS NOT EVIDENCE OF IDENTITY AND THIS FILE DOES NOT TREAT IT AS ONE.**

### ### **NOTHING IS REMOVED, MOVED OR RENAMED.** ### The removal is the author's and depends on this
### report -- which is exactly why the report must be able to say ### **NOT CONFIRMED** ### and must
### not be tempted to round a near miss up to a match.

### ### **AND THE ORDERED POPULATION IS THE FILES THE MIRROR CARRIES**, which is not every file under
### the archive directories. ### The wider count is printed as ### **CONTEXT, LABELLED AS CONTEXT**,
### and is not presented as the ordered report.
"""
import hashlib
import io
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def title_line(text):
    """### **THE FIRST MARKDOWN HEADING, WHICH IS A CLAIM THE FILE MAKES ABOUT ITSELF.**

    ### It is used ### **BESIDE** ### the digest and never instead of it: a digest proves the bytes
    ### are the same, and a title line proves a human reading both would call them the same document.
    ### **NEITHER ALONE IS THE CONFIRMATION THE ORDER ASKS FOR.**
    """
    for ln in text.split(chr(10))[:60]:
        if ln.startswith('#'):
            return ln.strip()
    for ln in text.split(chr(10))[:60]:
        if ln.strip():
            return ln.strip()[:120]
    return None


def newest_mirror():
    """### **THE MIRROR ARCHIVE, LOCATED BY CONTENT ON DISK AND NOT TYPED.**"""
    cands = []
    for n in os.listdir(DL):
        if n.startswith('mirror-refresh-') and n.endswith('.zip'):
            p = os.path.join(DL, n)
            cands.append((os.path.getmtime(p), p))
    cands.sort()
    return cands[-1][1] if cands else None


def main():
    rec('=' * 100)
    rec('b378 -- ADDITION THREE: ### **THE ARCHIVES, CONFIRMED AND NOT REMOVED.**')
    rec('=' * 100)
    rec('')
    zp = newest_mirror()
    if not zp:
        rec('  ### ### **NO MIRROR ARCHIVE FOUND ON DISK. ### REFUSING TO REPORT.**')
        run_clock.write(D, 'b378_archives_notes', LINES)
        return 2
    rec('  ### the project mirror : %s' % os.path.basename(zp))
    rec('  ### its own sha256     : %s' % sha(io.open(zp, 'rb').read()))
    roster = json.load(io.open(ROSTER, encoding='utf-8'))['files']
    zf = zipfile.ZipFile(zp)
    names = [n for n in zf.namelist() if not n.endswith('/')]
    rec('  ### entries in the mirror : %d ; roster source paths : %d' % (len(names), len(roster)))
    rec('')

    # ### **THE ORDERED POPULATION: THE ROSTER'S ARCHIVE-DIRECTORY SOURCE PATHS.**
    arch_paths = [p for p in roster
                  if p.replace('\\', '/').split('/')[0].lower() == 'archive']
    rec('-' * 100)
    rec('  ### THE ORDERED POPULATION -- ARCHIVE FILES THE MIRROR CARRIES : ### **%d**'
        % len(arch_paths))
    rec('-' * 100)
    for p in arch_paths:
        rec('    %s' % p.replace('\\', '/'))
    rec('')
    rec('  ### ### **THE MIRROR NAME IS DERIVED FROM THE PATH, SO IT IS NOT THE PATH.** ### Each entry')
    rec('  ### below is matched to a mirror member ### **BY DIGEST**, then confirmed on disk ### **BY')
    rec('  ### ### DIGEST AND BY TITLE LINE** -- never by the name it happens to carry.')
    rec('')

    # ### **EVERY MIRROR MEMBER, BY DIGEST.** ### This is the index the confirmation uses.
    by_digest = {}
    for n in names:
        b = zf.read(n)
        by_digest.setdefault(sha(b), []).append(n)

    rows, confirmed, notconfirmed = [], 0, 0
    rec('-' * 100)
    rec('  ### THE CONFIRMATION, PER FILE.')
    rec('-' * 100)
    for rel in arch_paths:
        relp = rel.replace('\\', os.sep)
        disk = os.path.join(PP, relp)
        row = dict(source_path=rel.replace('\\', '/'), disk_path=None, digest=None,
                   in_mirror_as=None, title_disk=None, title_mirror=None,
                   digest_match=False, title_match=False, verdict=None, missing=[])
        rec('')
        rec('  ### `%s`' % row['source_path'])
        if not os.path.exists(disk):
            row['verdict'] = '### **NOT CONFIRMED**'
            row['missing'].append('no file at that path on the canonical drive')
            rec('    ### ### **NOT CONFIRMED** -- there is no file at that path on `D:`.')
            notconfirmed += 1
            rows.append(row)
            continue
        raw = io.open(disk, 'rb').read()
        dg = sha(raw)
        txt = raw.decode('utf-8', 'replace')
        row.update(disk_path=disk, digest=dg, title_disk=title_line(txt))
        member = by_digest.get(dg)
        if member:
            row['in_mirror_as'] = member[0]
            row['digest_match'] = True
            mtxt = zf.read(member[0]).decode('utf-8', 'replace')
            row['title_mirror'] = title_line(mtxt)
            row['title_match'] = (row['title_mirror'] == row['title_disk']
                                  and row['title_disk'] is not None)
        else:
            row['missing'].append('no mirror member carries this digest')
            # ### **A NEAR MISS IS REPORTED AS A NEAR MISS, NOT ROUNDED UP.**
            same_title = [n for n in names
                          if title_line(zf.read(n).decode('utf-8', 'replace')) == row['title_disk']
                          and row['title_disk']]
            if same_title:
                row['in_mirror_as'] = same_title[0]
                row['title_mirror'] = row['title_disk']
                row['title_match'] = True
                row['missing'].append('a member shares the TITLE LINE but NOT the bytes -- '
                                      'the mirror is older or newer than the disk')
        row['verdict'] = ('### **CONFIRMED PRESENT**'
                          if (row['digest_match'] and row['title_match'])
                          else '### **NOT CONFIRMED**')
        if row['digest_match'] and row['title_match']:
            confirmed += 1
        else:
            notconfirmed += 1
        rec('    on the canonical drive : %s' % disk)
        rec('    sha256                 : %s' % dg)
        rec('    carried in the mirror as : `%s`' % (row['in_mirror_as'] or 'NOT CARRIED'))
        rec('    ### digest match : %-5s   ### title-line match : %-5s'
            % (row['digest_match'], row['title_match']))
        rec('    title on disk   : %s' % (row['title_disk'] or 'NONE')[:96])
        if row['in_mirror_as'] and row['title_mirror'] != row['title_disk']:
            rec('    title in mirror : %s' % (row['title_mirror'] or 'NONE')[:96])
        rec('    ### ### %s' % row['verdict'])
        for m in row['missing']:
            rec('        ### missing : %s' % m)
        # ### **THE FILENAME COMPARISON IS PRINTED SO THE READER CAN SEE IT WAS NOT USED.**
        leaf = os.path.basename(rel.replace('\\', '/'))
        rec('    ### *(filename on disk `%s`; in the mirror `%s`. ### **NOT USED AS EVIDENCE.**)*'
            % (leaf, row['in_mirror_as'] or '-'))
        rows.append(row)

    # ------------------------------------------------------------------------------------ CONTEXT
    rec('')
    rec('-' * 100)
    rec('  ### CONTEXT, LABELLED AS CONTEXT AND NOT PART OF THE ORDERED REPORT.')
    rec('-' * 100)
    allarch = []
    for dp, dn, fn in os.walk(os.path.join(PP, 'archive')):
        for f in fn:
            fp = os.path.join(dp, f)
            allarch.append(os.path.relpath(fp, PP).replace(os.sep, '/'))
    carried = set(p.replace('\\', '/') for p in arch_paths)
    rec('    files under `archive/` on the canonical drive : ### **%d**' % len(allarch))
    rec('    of those, carried by the mirror               : ### **%d**' % len(carried))
    rec('    ### ### **NOT CARRIED BY THE MIRROR : %d**' % (len(allarch) - len(carried)))
    rec('    ### ### ### **THIS IS CONTEXT AND NOT THE ORDERED REPORT.** ### The order asked about')
    rec('    ### ### ### the files the mirror carries. ### **THE OTHER %d ARE NAMED HERE ONLY SO THAT'
        % (len(allarch) - len(carried)))
    rec('    ### ### ### A REMOVAL DECISION IS NOT TAKEN IN IGNORANCE OF THEM**, and this act')
    rec('    ### ### ### ### **DID NOT CONFIRM THEM AND MAKES NO CLAIM ABOUT THEM.**')

    rec('')
    rec('=' * 100)
    rec('  ### ### **CONFIRMED PRESENT : %d ### / ### NOT CONFIRMED : %d ### of %d**'
        % (confirmed, notconfirmed, len(arch_paths)))
    rec('  ### ### **ARCHIVE FILES REMOVED, MOVED OR RENAMED BY THIS ACT : 0.**')
    rec('  ### ### ### **THE REMOVAL IS THE AUTHOR`S AND DEPENDS ON THIS REPORT.** ### A `CONFIRMED')
    rec('  ### ### ### PRESENT` here is a statement about bytes and a title line. ### **IT IS NOT A')
    rec('  ### ### ### RECOMMENDATION ABOUT DISPOSAL**, and it says nothing about whether anything')
    rec('  ### ### ### else in the corpus still cites the file.')
    rec('=' * 100)
    p = run_clock.write(D, 'b378_archives_notes', LINES)
    io.open(os.path.join(D, 'b378_archives.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(mirror=os.path.basename(zp), mirror_entries=len(names),
                        ordered_population=len(arch_paths), rows=rows,
                        confirmed=confirmed, not_confirmed=notconfirmed, removed=0,
                        context_archive_files=len(allarch),
                        context_not_carried=len(allarch) - len(carried),
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
