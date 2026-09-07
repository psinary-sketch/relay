# -*- coding: utf-8 -*-
"""b360_roster.py -- THE AUTHOR'S RULING, EXECUTED. ### `FACES_LEDGER.md` ADDED TO THE MIRROR ROSTER.

### ### **WHY THIS IS A TOOL AND NOT AN EDIT.** ### The roster's own header says ### *"ORDER IS
### SIGNIFICANT -- the first entry wins the plain slot"*, and `b183`'s history is a row added to a file
### nothing read. ### **A ROW ADDED BY HAND IS A ROW NOBODY READ BACK**, so this file writes the row, reads
### the file back, and checks that ### **EVERY EXISTING ROW IS AT THE INDEX IT WAS AT BEFORE.**
### ### **THE EDIT IS TEXTUAL, NOT A RE-SERIALISATION.** ### Re-emitting the JSON would rewrite every byte
### of a file whose formatting nothing depends on but whose diff everything does. ### The new row is
### inserted before the list's closing bracket and the `lastChanged` field is retyped; ### **NO OTHER BYTE
### ### OF THE FILE CHANGES**, and that is checked by a line-by-line comparison against the blob.
### ### **AND WHAT THE ADDITION DOES AND DOES NOT DO, IN THE RULING'S OWN TERMS:** ### it makes the ledger
### reach the archive ### **FROM THIS REBUILD FORWARD.** ### **IT DOES NOT RETROACTIVELY PLACE IT IN ANY
### ### PRIOR MIRROR, AND PRIOR ARCHIVES ARE NOT REBUILT.** ### A roster row is a carrying decision:
### ### **CARRYING A LEDGER IN AN ARCHIVE SAYS NOTHING ABOUT WHETHER WHAT THE LEDGER SAYS IS TRUE.**
### ### **IDEMPOTENT:** a second run finds the row and writes nothing; the read-back arms still run.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')
PP = r'D:\MY-DOwnloads\PLACE-papers'
ROW = 'FACES_LEDGER.md'
DATE = '2026-09-07'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def blob():
    r = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:tools/mirror_roster.json'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def main():
    rec('=' * 100)
    rec("b360_roster.py -- THE AUTHOR'S RULING, EXECUTED. ### FACES_LEDGER.md ADDED TO THE MIRROR ROSTER.")
    rec('=' * 100)
    before = io.open(ROSTER, encoding='utf-8').read()
    J0 = json.loads(before)
    old = list(J0['files'])
    rec('  roster before : %d source path(s) ; lastChanged %s' % (len(old), J0.get('lastChanged')))
    rec('  ### the source file the ruling names EXISTS in the papers repo : %s'
        % os.path.exists(os.path.join(PP, ROW)))
    if not os.path.exists(os.path.join(PP, ROW)):
        rec('  ### ### **REFUSING -- A ROSTER ROW FOR A FILE THAT IS NOT THERE WOULD BREAK EVERY BUILD.**')
        run_clock.write(D, 'b360_roster_run', LINES)
        return 2
    if ROW in old:
        rec('  ### ### **THE ROW IS ALREADY IN THE ROSTER. ### NOTHING WRITTEN.** (idempotent)')
        written = False
        after = before
    else:
        last = old[-1]
        # ### **THE ANCHOR IS BUILT FROM THE FILE'S OWN ESCAPING, NOT FROM THE PARSED VALUE.** ### The
        # ### roster's paths carry backslashes, which JSON escapes; a tool that anchored on the parsed
        # ### string would look for a line the file does not contain. ### Found by this tool's first run
        # ### REFUSING, which is what the hard failure is for.
        anchor = '    %s\n  ]' % json.dumps(last)
        if anchor not in before:
            rec('  ### ### **HARD FAILURE -- THE LIST\'S CLOSING SHAPE IS NOT WHAT THIS TOOL EXPECTS.**')
            rec('      expected to find : %r' % anchor)
            run_clock.write(D, 'b360_roster_run', LINES)
            return 2
        new = before.replace(anchor, '    %s,\n    %s\n  ]' % (json.dumps(last), json.dumps(ROW)), 1)
        new = new.replace('"lastChanged": "%s"' % J0['lastChanged'], '"lastChanged": "%s"' % DATE, 1)
        open(ROSTER + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(ROSTER + '.tmp', ROSTER)
        after = io.open(ROSTER, encoding='utf-8').read()
        written = True

    J1 = json.loads(after)
    files = list(J1['files'])
    ok_len = len(files) == len(old) + (0 if ROW in old else 1)
    ok_prefix = files[:len(old)] == old if ROW not in old else files == old
    ok_last = files[-1] == ROW
    ok_date = J1.get('lastChanged') == DATE
    rec('')
    rec('  READ BACK, AND THE ARMS:')
    rec('    the file still parses as JSON                         : True')
    rec('    row count %d -> %d, and the addition is exactly one    : %s' % (len(old), len(files), ok_len))
    rec('    ### **EVERY EXISTING ROW IS AT THE INDEX IT WAS AT**  : %s' % ok_prefix)
    rec('    the new row is LAST, so no existing slot changes      : %s' % ok_last)
    rec('    lastChanged brought to this act\'s date                : %s (%s)' % (ok_date, J1.get('lastChanged')))
    # ### ### **THE ARM AGAINST THE BLOB, AND WHY IT IS NOT THE APPEND-ONLY ARM.** ### This edit is NOT a
    # ### pure append: the `lastChanged` value is retyped and the former last row gains a comma. ### A
    # ### greedy in-order line matcher -- the shape the append-only arms use -- stalls at the first changed
    # ### line and reports the whole tail as missing, which is what its first run did here. ### **AN ARM
    # ### ### THAT CANNOT PASS ON A CORRECT EDIT IS NOT A STRICTER ARM; IT IS THE WRONG ARM.**
    # ### So the blob is checked where the meaning is: ### **EVERY ROSTER PATH THE COMMITTED BLOB CARRIES
    # ### IS PRESENT AT THE SAME INDEX**, and the file differs from the blob in AT MOST the three lines the
    # ### edit touches. ### **READ BEFORE THE PUSH**, which is the reading that carries.
    hb = blob()
    kept = None
    ndiff = None
    if hb is not None:
        bfiles = list(json.loads(hb)['files'])
        kept = files[:len(bfiles)] == bfiles
        import difflib
        oldl = hb.replace(chr(13) + chr(10), chr(10)).split(chr(10))
        newl = after.replace(chr(13) + chr(10), chr(10)).split(chr(10))
        ndiff = sum(1 for x in difflib.unified_diff(oldl, newl, n=0)
                    if (x.startswith('+') or x.startswith('-')) and not x.startswith(('+++', '---')))
        # ### **AND THE SEMANTIC ARM, WHICH IS THE ONE THAT MEANS ANYTHING:** ### every OTHER key of the
        # ### roster object is byte-for-byte what the blob carries. ### A textual line count can be right
        # ### for a wrong edit; a key-by-key comparison cannot.
        J0b = json.loads(hb)
        others = sorted(set(J0b) | set(J1) - {'files', 'lastChanged'})
        others = [k for k in others if k not in ('files', 'lastChanged')]
        same_others = all(J0b.get(k) == J1.get(k) for k in others)
        rec('    ### **EVERY ROSTER PATH OF THE COMMITTED BLOB, AT THE SAME INDEX** : %s (blob rows %d)'
            % (kept, len(bfiles)))
        rec('    ### **EVERY OTHER FIELD IDENTICAL TO THE BLOB** : %s (%s)' % (same_others, ', '.join(others)))
        rec('    lines added or removed against the blob : %d (the date, the former last row, the new row: 5)'
            % ndiff)
        kept = kept and same_others
    rec('')
    rec('  ### ### **WHAT THIS DOES: THE LEDGER REACHES THE ARCHIVE FROM THE NEXT REBUILD FORWARD.**')
    rec('  ### ### **WHAT IT DOES NOT DO: IT DOES NOT RETROACTIVELY PLACE IT IN ANY PRIOR MIRROR, AND PRIOR')
    rec('  ### ### ARCHIVES ARE NOT REBUILT.**')
    rec('  ### **AND A ROSTER ROW IS A CARRYING DECISION AND NOTHING ELSE: CARRYING A LEDGER IN AN ARCHIVE')
    rec('  ### SAYS NOTHING ABOUT WHETHER WHAT THE LEDGER SAYS IS TRUE.**')
    ok = ok_len and ok_prefix and ok_last and ok_date and (kept is not False) and (ndiff is None or ndiff <= 5)
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    p = run_clock.write(D, 'b360_roster_run', LINES)
    io.open(os.path.join(D, 'b360_roster.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(row=ROW, before=len(old), after=len(files), written=bool(written), last_is_new=bool(ok_last),
             existing_rows_unmoved=bool(ok_prefix), blob_rows_unmoved=kept, lines_differing_from_blob=ndiff, last_changed=J1.get('lastChanged'),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
