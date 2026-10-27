# -*- coding: utf-8 -*-
"""standing/classes.py -- THE CLOSE CLASSES GATHERED AT v1.2.0 ((R328)(7) of the derivation act), each class's repair with its control on
the previous act's banks, both instances shown: the RECORD instance (the previous act's banks read the old way, the defect reproduced,
and read the repaired way) and a CONSTRUCTED one (a plant the repaired reading must refuse, or a form it must accept).
  (1) a needle read word for word from the face          tools/standing/needles.py       the test act's event (1)
  (2) a branch pattern read as a pattern                 tools/standing/allow.py         event (2)
  (8) the seconds gather ordered before the seal         tools/standing/close.py         event (8)
  (9) the act's own trail append exempt by its commit    tools/standing/keystone.py      event (9)
  (10) the MANIFEST control read against HEAD            tools/standing/manifest.py      event (10)
The hook's refusal (the test act's fifth uncommitted item) stands as the hook working: no repair, no case.
The acts read are the chain's: the previous act (`prev`, the record) and, for (8)'s accepting instance, the latest chain act whose
gathered seconds bank exists. No act's name, figure or commit stands in the code; each is read from the banks at the call.

  python -X utf8 tools/standing/classes.py            prints; writes nothing
  python -X utf8 tools/standing/classes.py bank       writes data/<act>_classes_controls.txt
  python -X utf8 tools/standing/classes.py repairs    writes data/<act>_tool_repairs.txt: every standing file's diff against HEAD (a new
                                                      file whole), the record of v1.2.0's changes by diff
Each writing route is refused once the act's root is appended to the chain.
"""
import glob
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A          # noqa: E402
import allow as AW       # noqa: E402
import close as C        # noqa: E402
import keystone as KS    # noqa: E402
import manifest as MF    # noqa: E402
import needles as ND     # noqa: E402

NL = '\n'
S = os.path.dirname(os.path.abspath(__file__))
DELETE_ROW = re.compile(r'^\s*#\d+ \| \S+ \| seat \| (?:Bash|PowerShell) \| git -C (\S+) ' + 'branch' + r' -d (\S+)\s*$', re.M)


def deletes_of(act):
    """the act's branch deletes [(repository path, branch)] from its command capture's rows (data/<act>_commands.txt)."""
    return [(r.replace('\\', '/'), b) for r, b in DELETE_ROW.findall(A.rd('%s_commands.txt' % act))]


def face_of(act):
    fs = sorted(glob.glob(os.path.join(A.D, '%s_registration_*.txt' % act)))
    return (fs[-1], A.rd_path(fs[-1])) if fs else (None, '')


def lines():
    cur = A.current()
    act, parts = cur['act'], cur['parts']
    prev = A.prev_of(act)
    pprev = A.prev_of(prev)
    L = ['%s -- THE CLOSE CLASSES OF THE STANDING TOOLSET AT %s, EACH REPAIR WITH ITS CONTROL ON %s`S BANKS, BOTH INSTANCES (%s)' % (
        act, A.rd_path(os.path.join(S, 'VERSION')).strip(), prev, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are cases: the class (its event), the instance (RECORD or CONSTRUCTED), what is read, the figure got, the figure wanted,',
         '### AS WANTED. Written by tools/standing/classes.py; the hook`s refusal stands as the hook working (no case).', '']
    res = []

    def case(k, inst, what, got, want):
        ok = got == want
        res.append(ok)
        L.append('  (%s) %-11s %s' % (k, inst, what))
        L.append('        got %r ; wanted %r -- %s' % (got, want, 'AS WANTED' if ok else '### NOT AS WANTED'))

    # (1) the needle
    fp, face = face_of(prev)
    dj = A.jl('%s_root_banks_dry.json' % prev)
    ready = dj.get('ready')
    old = ('the root route`s dry run READY %s' % ready) in ND.unwrap(face)
    writer_form = 'root route run dry once' in ND.unwrap(face)
    case('1', 'RECORD', '%s`s face (%s): the dry run READY %s ; the arm`s old literal found ; the repaired reader`s needle found ; the face`s '
         'own form ("root route run dry once") found' % (prev, os.path.basename(fp or '-'), ready), (ready, old, ND.carries(face, 'rootdry', ready=ready),
                                                                                                    writer_form), (True, False, False, True))
    built = ND.line('rootdry', ready=True)
    w = built.split(' ')
    wrapped = '### (0) ... ' + ' '.join(w[:3]) + NL + '### ' + ' '.join(w[3:]) + ' its evidence for the seal'   # wrapped at a space, as a bank wraps
    case('1', 'CONSTRUCTED', 'a face written by the table`s line, hard-wrapped through the needle: carried ; its READY True read as READY False: not',
         (ND.carries(wrapped, 'rootdry', ready=True), ND.carries(wrapped, 'rootdry', ready=False)), (True, False))
    # (2) the branch pattern
    ruling = AW.ruling_of(prev)
    dels = deletes_of(prev)
    v110 = AW.deletes_read(dels, ruling, AW.words_of(prev), pattern=AW.BRANCH_V110)
    v120 = AW.deletes_read(dels, ruling, AW.words_of(prev))
    case('2', 'RECORD', '%s`s %d deletes by name (its command capture) against its ruling: outside at v1.1.0 (the star dropped) ; outside at v1.2.0 ; '
         'the kept names' % (prev, len(dels)), (len(v110['outside']), len(v120['outside']), v120['kept']), (len(dels), 0, v110['kept']))
    L.append('        v1.1.0 allowed %s ; v1.2.0 allowed %s' % (v110['allowed'], v120['allowed']))
    other = 'push-%s-closing' % prev   # the previous act's own branch: its ruling names the act before it
    kept = v120['kept'][0] if v120['kept'] else 'port-x'
    pl = AW.deletes_read([('-', other), ('-', kept)], ruling, AW.words_of(prev))
    case('2', 'CONSTRUCTED', 'two deletes the pattern must refuse: %s (an act`s branch the ruling does not name) and %s (kept)' % (other, kept),
         [b for _r, b in pl['outside']], [other, kept])
    # (8) the seconds gather before the seal
    sg = C.seconds_gathered(prev, parts)
    case('8', 'RECORD', '%s`s per-part seconds banks: the gathered bank written before the seal ; parts without a bank' % prev,
         (sg['gathered'], sg['ok'], sg['missing_parts']), (False, False, []))
    gat = next((a for a, _r, _p in reversed(A.chain()) if os.path.isfile(os.path.join(A.D, '%s_arm_seconds.json' % a))), None)
    sg2 = C.seconds_gathered(gat, parts) if gat else dict(ok=None, gathered=None, missing_arms=None)
    case('8', 'RECORD', 'the latest chain act with a gathered bank, %s: gathered, every part`s arms among its rows' % gat,
         (sg2['gathered'], sg2['ok']), (True, True))
    sg3 = C.seconds_gathered(gat, parts + ['a-part-with-no-bank']) if gat else dict(ok=None, missing_parts=None)
    case('8', 'CONSTRUCTED', 'the same bank read with a part the pre-run never banked: refused, the part named', (sg3['ok'], sg3['missing_parts']),
         (False, ['a-part-with-no-bank']))
    # (9) the trail append exempt by its commit
    c5 = [r['commit'] for r in A.steps(prev) if r.get('repo') == 'pp' and r.get('phase') == 'component 5']
    base = c5[-1] if c5 else None
    rec = KS.exempt_of(prev, ('record',))
    head = rec[-1] if rec else None
    files = sorted(p for p in (A.gs('pp', 'diff-tree', '--no-commit-id', '--name-only', '-r', base) or '').split(NL) if p.strip()) if base else []
    k_old = KS.unchanged_since(files, base, head) if base and head else dict(ok=None, rows=[])
    k_new = KS.unchanged_since(files, base, head, exempt=rec) if base and head else dict(ok=None, rows=[])
    ch = lambda r: sorted(f for f, s, _c in r['rows'] if s != 'UNCHANGED')
    case('9', 'RECORD', '%s`s %d files edited at its component-5 commit %s, read to its record`s commit %s: unchanged (the old clause) ; with the '
         'record`s commit exempt ; the files touched after' % (prev, len(files), (base or '-')[:8], (head or '-')[:8]),
         (k_old['ok'], k_new['ok'], ch(k_old)), (False, True, ['OPEN_TRAILS.md']))
    k_pl = KS.unchanged_since(files, base, head, exempt=[base]) if base and head else dict(ok=None)
    case('9', 'CONSTRUCTED', 'the exemption naming a commit that is not the act`s record (the edit commit itself): the trail`s append fails it',
         k_pl['ok'], False)
    # (10) the MANIFEST control against HEAD
    mj = A.jl('%s_mirror_build.json' % prev)
    mz = re.search(r'^built: (.+)$', mj.get('out') or '', re.M)
    zp = mz.group(1).strip() if mz else None
    mtxt = A.rd('%s_mirror.txt' % prev)
    mref = re.search(r'MANIFEST CONTROL, AGAINST ([0-9a-f]{7,40})', mtxt)
    pph = re.search(r'PLACE-papers HEAD AT THE BUILD : ([0-9a-f]{7,40})', mtxt)
    if not (zp and os.path.isfile(zp) and mref and pph):
        case('10', 'RECORD', '%s`s export and its control`s reference' % prev, (zp, bool(mref), bool(pph)), ('PRESENT', True, True))
    else:
        first = [r['commit'] for r in A.steps(prev) if r.get('repo') == 'pp']
        pbase = A.gs('pp', 'rev-parse', first[0] + '^') if first else None
        sil = [p for p in MF.edited(pbase, pph.group(1)) if p.endswith('Silence_of_Foundations.md')]
        old_c = MF.control(zp, pbase, pph.group(1), files=sil, ref=mref.group(1))
        new_c = MF.control(zp, pbase, pph.group(1))
        case('10', 'RECORD', '%s`s export: its carried control (%s against the carried %s) ; the repaired control, every file the act edited '
             '(%s..%s) against the head it was built at' % (prev, sil, mref.group(1)[:8], (pbase or '-')[:8], pph.group(1)[:8]),
             (old_c['ok'], new_c['ok']), (False, True))
        for p, mem, raw_eq, lf_eq, st in new_c['rows']:
            L.append('        %-58s %-18s entries %d ; raw equal %s ; with CR removed %s' % (p, st, len(mem), raw_eq, lf_eq))
        bad = MF.control(zp, pbase, pph.group(1), ref=pbase)
        case('10', 'CONSTRUCTED', 'the same files read against the act`s base (a reference before its edits): NOT AS WANTED', bad['ok'], False)
    L += ['', '### ### **CASES %d ; AS WANTED %d ; NOT AS WANTED %d.**' % (len(res), sum(res), len(res) - sum(res))]
    return L, act, all(res)


def repairs_lines():
    act = A.current()['act']
    L = ['%s -- THE STANDING TOOLSET`S CHANGES AT %s, BY DIFF AGAINST HEAD (%s)' % (act, A.rd_path(os.path.join(S, 'VERSION')).strip(),
                                                                                 time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### every file of tools/standing/: tracked files by `git diff HEAD`, a file not yet tracked whole with each line marked +.', '']
    for f in sorted(os.listdir(S)):
        if not (f.endswith('.py') or f == 'VERSION'):
            continue
        rel = 'tools/standing/' + f
        tracked = A.gs('relay', 'ls-files', rel)
        if tracked:
            d = A.gs('relay', 'diff', 'HEAD', '--', rel) or ''
            if d:
                L += ['### PAIR %s (changed)' % rel] + d.split(NL) + ['']
        else:
            L += ['### PAIR %s (new)' % rel] + ['+' + l for l in A.rd_path(os.path.join(S, f)).split(NL)] + ['']
    return L, act


def write_bank(act, name, L):
    if act in [r[0] for r in A.chain()]:
        print('### %s`s ROOT IS APPENDED TO THE CHAIN -- NOTHING WRITTEN' % act)
        return 4
    p = os.path.join(A.D, name)
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(p + '.tmp', p)
    print('bank', p)
    return 0


def main(route):
    if route == 'repairs':
        L, act = repairs_lines()
        code = write_bank(act, '%s_tool_repairs.txt' % act, L)
        print('### %d lines' % len(L))
        return code
    L, act, ok = lines()
    print(NL.join(L))
    if route == 'bank':
        code = write_bank(act, '%s_classes_controls.txt' % act, L)
        if code:
            return code
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
