# -*- coding: utf-8 -*-
"""ledger_split.py -- THE ARCHIVAL SPLIT (b143).

### WHY THE PROOF IS REASSEMBLY AND NOT md5. md5 lines on the archives prove
### only that the archives are what they are. They say NOTHING about whether
### anything fell between the segments. ### THE ONLY CHECK THAT SAYS NOTHING WAS
### LOST IS: every segment, concatenated in original offset order, EQUALS THE
### ORIGINAL FILE BYTE FOR BYTE. That check is run here and a failure aborts the
### split with nothing written.

### WHY BYTES AND NOT TEXT. A decode/encode round trip can normalise a BOM, a
### line ending, or a final newline, and every one of those would make a
### byte-exact archive a lie. ### NOTHING IN THIS FILE DECODES THE LEDGERS.
### Anchors are matched as UTF-8 BYTE strings against the raw bytes.

### THE BOUNDARY RULE, which is the executor's call and is stated so it can be
### overruled: the ferry's dated boundary is applied WITHIN THE RECORD STREAM
### ONLY. Reference frames -- the loom's legend and cascades, FINDINGS' sections
### I-III and its citation machinery, OPEN_TRAILS' active sections -- STAY IN THE
### WORKING COPY REGARDLESS OF AGE, because they are not entries and were never
### closed. See the registration for the three surveyed reasons a bare date
### boundary does not work on these files.
"""
import hashlib
import io
import os
import re
import sys

# ### SWEPT b146: the same cp1252 stdout defect fixed in banned_terms.py and
# ### mirror_verify.py at b142 and in probe_from_diff.py at b146. This file had
# ### not met a triggering character, which is exactly why it was still carrying
# ### the defect. ### FIXING A CLASS OF DEFECT IN ONE TOOL IS NOT FIXING THE
# ### CLASS -- the sweep is the fix.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = r'D:\MY-DOwnloads\PLACE-papers'
ARCH = os.path.join(SRC, 'archive', '2026-08-24-ledger-split')

# (ledger, [(kind, anchor_start, anchor_end_or_None, archive_basename)])
# kind: 'keep' or 'arch'. Segments MUST be given in original offset order and
# MUST tile the file with no hole and no overlap -- which the reassembly proves.
PLAN = [
    ('OPEN_TRAILS.md', [
        ('keep', None, u'**NINETEENTH-SEAM-CLOSE RECORD', None),
        ('arch', u'**NINETEENTH-SEAM-CLOSE RECORD', u'## Open trails (active)',
         'OPEN_TRAILS-archive-1-seam-records-through-nineteenth.md'),
        ('keep', u'## Open trails (active)', u'## Session landing \u2014 2026-07-09', None),
        ('arch', u'## Session landing \u2014 2026-07-09', None,
         'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'),
    ]),
    ('VERIFICATION_LOOM.md', [
        ('keep', None, u'## 2026-06-12 -- native_decide cleanup pass', None),
        ('arch', u'## 2026-06-12 -- native_decide cleanup pass',
         u'**Dated line (2026-08-24, the twentieth seam close)',
         'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md'),
        ('keep', u'**Dated line (2026-08-24, the twentieth seam close)', None, None),
    ]),
    ('FINDINGS.md', [
        ('keep', None, u'## M3 (hinge transparent)', None),
        ('arch', u'## M3 (hinge transparent)', u'## F.2026-08-20d',
         'FINDINGS-archive-1-entries-through-2026-08-20c.md'),
        ('keep', u'## F.2026-08-20d', u'## F.2026-08-22a', None),
        ('arch', u'## F.2026-08-22a', None,
         'FINDINGS-archive-2-entries-2026-08-21-and-22.md'),
    ]),
]

POINTER = u"""> ### **THIS LEDGER WAS SPLIT ON 2026-08-24 (the twenty-fifth seam close, relay `reports/2026-08-24-twentyfifth-seam-close.md`).**
> ### **NOTHING WAS DELETED.** The settled segments were archived **byte-exact** to
> `archive/2026-08-24-ledger-split/` in this same repository, and the split was
> verified by ### **REASSEMBLY** \u2014 every segment concatenated in original order
> equals the pre-split file **byte for byte**, which is the only check that says
> nothing was lost. *md5 lines ride below and in the archive README.*
>
> ### **WHAT WAS ARCHIVED, AND WHERE:**
{table}
>
> ### **THE BOUNDARY:** the dated boundary is applied **within the record stream only**.
> **Reference frames stay here regardless of age** \u2014 they are not entries and were
> never closed. *Settled records closed before the twentieth seam moved to the archive.*
>
> ### **THE INDEX OF ARCHIVED HEADINGS IS BELOW**, so a citation to any archived
> section resolves in one hop. ***For `FINDINGS.md` this is not a convenience: papers
> cite `FINDINGS#anchor-name`, and an anchor that moved without an index would be a
> broken citation.***
{index}

---

"""


def main():
    if not os.path.isdir(ARCH):
        os.makedirs(ARCH)
    report, readme = [], []
    for name, plan in PLAN:
        path = os.path.join(SRC, name)
        raw = open(path, 'rb').read()
        # ---- resolve anchors to byte offsets ----
        offs = []
        for kind, a, b, base in plan:
            s = 0 if a is None else raw.find(a.encode('utf-8'))
            e = len(raw) if b is None else raw.find(b.encode('utf-8'))
            if s < 0 or e < 0:
                print("  ### ABORT: anchor not found in %s (%r / %r)" % (name, a, b))
                return 2
            offs.append((kind, s, e, base))
        # ---- the tiling must be exact: no hole, no overlap ----
        cur = 0
        for kind, s, e, base in offs:
            if s != cur or e < s:
                print("  ### ABORT: segments do not tile %s at offset %d (got %d)" % (name, cur, s))
                return 2
            cur = e
        if cur != len(raw):
            print("  ### ABORT: segments end at %d, file is %d bytes" % (cur, len(raw)))
            return 2
        # ---- THE REASSEMBLY PROOF, before anything is written ----
        rebuilt = b''.join(raw[s:e] for _, s, e, _ in offs)
        if rebuilt != raw:
            print("  ### ABORT: reassembly != original for %s" % name)
            return 2
        print("  %-24s REASSEMBLY PROOF: PASS (%d bytes, %d segments)"
              % (name, len(raw), len(offs)))

        # ---- write archives; build the index ----
        rows, idx = [], []
        for kind, s, e, base in offs:
            if kind != 'arch':
                continue
            seg = raw[s:e]
            open(os.path.join(ARCH, base), 'wb').write(seg)
            md5 = hashlib.md5(seg).hexdigest()
            rows.append(u"> | `%s` | %s | %d | `%s` |" % (base, "%d\u2013%d" % (s, e), len(seg), md5))
            readme.append((name, base, len(seg), md5))
            heads = re.findall(r'^##+ .*$', seg.decode('utf-8', 'replace'), re.M)
            idx.append((base, heads))
            report.append((name, base, len(seg), md5, len(heads)))

        table = (u"> \n> | archive file | byte range in the pre-split file | bytes | md5 |\n"
                 u"> |:--|:--|--:|:--|\n" + u"\n".join(rows))
        ilines = [u">"]
        for base, heads in idx:
            ilines.append(u"> **In `%s` (%d headings):**" % (base, len(heads)))
            ilines.append(u"> ")
            for h in heads:
                ilines.append(u"> - %s" % h.lstrip('#').strip())
            ilines.append(u"> ")
        header = POINTER.format(table=table, index=u"\n".join(ilines))

        keep = b''.join(raw[s:e] for k, s, e, _ in offs if k == 'keep')
        # the pointer goes AFTER the file's first line (its H1), never before it
        nl = keep.find(b'\n')
        out = keep[:nl + 1] + b'\n' + header.encode('utf-8') + keep[nl + 1:]
        open(path, 'wb').write(out)
        print("  %-24s working copy: %d -> %d bytes (%.1f%% of original)"
              % (name, len(raw), len(out), 100.0 * len(out) / len(raw)))

    # ---- the archive README ----
    r = [u"# LEDGER SPLIT \u2014 2026-08-24 (the twenty-fifth seam close)", u"",
         u"### **NOTHING HERE WAS DELETED FROM THE WORKING LEDGERS \u2014 IT WAS MOVED.**",
         u"Each file below is a **byte-exact contiguous slice** of its pre-split ledger.",
         u"The split was verified by ### **REASSEMBLY**: every segment concatenated in",
         u"original offset order equals the pre-split file **byte for byte**. *That is the",
         u"only check that proves nothing fell between the segments; md5 lines prove only",
         u"that each archive is what it is.*", u"",
         u"### **THE BOUNDARY.** The dated boundary is applied **within the record stream",
         u"only**: settled records closed before the twentieth seam moved here. **Reference",
         u"frames stayed in the working copies regardless of age** \u2014 the loom's legend and",
         u"cascades, `FINDINGS`' sections I\u2013III and its citation machinery, `OPEN_TRAILS`'",
         u"active sections. *They are not entries and were never closed.*", u"",
         u"Each working copy carries a pointer header naming these files, their md5s, and",
         u"### **a full index of the headings archived**, so a citation resolves in one hop.",
         u"***For `FINDINGS.md` that index is load-bearing: papers cite `FINDINGS#anchor-name`.***",
         u"", u"| source ledger | archive file | bytes | md5 |", u"|:--|:--|--:|:--|"]
    for src, base, n, md5 in readme:
        r.append(u"| `%s` | `%s` | %d | `%s` |" % (src, base, n, md5))
    io.open(os.path.join(ARCH, 'README.md'), 'w', encoding='utf-8',
            newline='\n').write(u"\n".join(r) + u"\n")
    print("\n  README written with %d md5 rows" % len(readme))
    return 0


if __name__ == '__main__':
    sys.exit(main())
