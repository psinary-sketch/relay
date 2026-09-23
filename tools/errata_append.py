# -*- coding: utf-8 -*-
"""errata_append.py -- THE ERRATA APPENDER. ### Built b487 on ruling (R97).

### ### **WHY THIS EXISTS.** ### b485 appended an entry under the id `E-2026-09-22-1`, which b469
### had already filed. ### **TWO ENTRIES SHARED ONE ID**, and b485's suite had no arm that would
### have looked. ### b486's fold found it; (R97) disposed of it; ### **AND THE GUARD BELONGS IN THE
### APPENDER, NOT IN ONE ACT'S COPY** -- the same lesson `corr_row.py` is still owed.

### ### **WHAT IT DOES.** ### Appends a block to `ERRATA.md` and ### **REFUSES BEFORE IT WRITES IF
### THE ID IS ALREADY IN THE FILE.** ### The refusal is a return code, not an exception, so a caller
### that ignores it still gets a `0`-length write and a printed reason.

### ### **THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:**
### ### (1) ### **IT CHECKS THE ID, NOT THE CONTENT.** ### Two entries with different ids saying the
###     same thing pass. ### **A DUPLICATE ID IS A CLASH; A DUPLICATE CLAIM IS AN ACT'S DUTY.**
### ### (2) ### **IT APPENDS. IT NEVER EDITS.** ### It cannot renumber an existing entry, and (R97)
###     did not ask it to -- a renumber is an APPENDED dated line, which this tool writes like any
###     other block.
### ### (3) ### It preserves the file's BOM and line ending by reading the bytes and re-applying
###     both, and it proves the prior bytes are a TRUE PREFIX of the result.
"""
import io
import os
import re
import sys

NL = chr(10)
ID = re.compile(r'\bE-\d{4}-\d{2}-\d{2}-\d+\b')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def ids_in(text):
    """### every erratum id the file already carries, as a SET."""
    return set(ID.findall(text or ''))


def append(path, new_id, block):
    """### ### **RETURNS `(code, lines)`.** ### `0` on a write, `2` on a refusal.
    ### ### **THE ID IS CHECKED BEFORE ANY BYTE IS WRITTEN.**"""
    out = []
    raw = io.open(path, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    text = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    have = ids_in(text)
    out.append('    file            : %s' % os.path.basename(path))
    out.append('    ids already in it : %d' % len(have))
    out.append('    the id offered  : %s' % new_id)
    if new_id in have:
        out.append('    ### ### **REFUSED -- THAT ID IS ALREADY IN THE FILE. NOTHING WAS WRITTEN.**')
        out.append('    ### A duplicate id is a clash the ledger cannot resolve by reading; the')
        out.append('    ### caller must choose a free id or append under an existing entry.')
        return 2, out
    body = NL.join(block)
    if new_id not in body:
        out.append('    ### ### **REFUSED -- THE BLOCK DOES NOT CARRY THE ID IT CLAIMS.**')
        return 2, out
    add = (eol + eol.join(body.split(NL)) + eol).encode('utf-8')
    io.open(path, 'ab').write(add)
    after = io.open(path, 'rb').read()
    ok = after.startswith(raw) and (after.startswith(b'\xef\xbb\xbf') == bom)
    out.append('    bytes before / appended / after : %d / %d / %d'
               % (len(raw), len(add), len(after)))
    out.append('    PRIOR BYTES A TRUE PREFIX : %s ; BOM preserved : %s'
               % (after.startswith(raw), after.startswith(b'\xef\xbb\xbf') == bom))
    old_lines = text.split(NL)
    new_lines = set(after.decode('utf-8-sig', 'replace').replace(chr(13), '').split(NL))
    missing = [x for x in old_lines if x not in new_lines]
    out.append('    ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    out.append('    ### ### **%s**' % ('WRITTEN.' if ok and not missing else 'WRITE NOT CLEAN.'))
    return (0 if (ok and not missing) else 2), out


def self_test(tmpdir):
    """### ### **BOTH CONTROLS, RUN BEFORE THE TOOL IS TRUSTED.**
    ### ### **POSITIVE CONTROL: A DUPLICATE ID IT MUST REFUSE.**
    ### ### **NEGATIVE CONTROL: A FRESH ID IT MUST ACCEPT.**"""
    lines = []
    p = os.path.join(tmpdir, 'ERRATA_fixture.md')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(
        '# fixture' + NL + NL + '## E-2026-01-01-1 - an entry that already exists' + NL)
    before = io.open(p, 'rb').read()
    code_dup, _ = append(p, 'E-2026-01-01-1',
                         ['## E-2026-01-01-1 - a second entry under the same id'])
    unchanged = io.open(p, 'rb').read() == before
    lines.append('      POSITIVE CONTROL -- a DUPLICATE id : code %d (must be 2) ; '
                 'file unchanged : %s' % (code_dup, unchanged))
    code_new, _ = append(p, 'E-2026-01-01-2', ['## E-2026-01-01-2 - a fresh entry'])
    grew = io.open(p, 'rb').read() != before
    lines.append('      NEGATIVE CONTROL -- a FRESH id     : code %d (must be 0) ; '
                 'file grew : %s' % (code_new, grew))
    ok = (code_dup == 2 and unchanged and code_new == 0 and grew)
    lines.append('      ### ### **BOTH CONTROLS BEHAVE : %s.**' % ok)
    lines.append('      ### ### **AN ARM THAT CANNOT REFUSE IS NOT A GUARD**, so the refusal is')
    lines.append('      ### exercised before the tool is used on the real ledger.')
    try:
        os.remove(p)
    except Exception:
        pass
    return ok, lines


if __name__ == '__main__':
    import tempfile
    d = tempfile.mkdtemp(prefix='errata_')
    good, ls = self_test(d)
    for x in ls:
        print(x)
    sys.exit(0 if good else 2)
