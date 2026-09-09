# -*- coding: utf-8 -*-
"""b378_lockgate.py -- STEP ZERO, AND ### **THE HOLE `b376` NAMED IS CLOSED HERE.**

### `b376` built a lock gate that reads EVERY pre-lock gate and requires each to carry its own pass
### phrase. ### It said, on its own face, what it could not do:
###   ### **IT CANNOT TELL WHETHER THE GATE WAS RUN AGAINST THE RIGHT THING**, and a stale record from
###   an earlier run of the same act would satisfy it.
### `b377` ### **HIT THAT IN PRACTICE** -- a late rewrite of its registration left three gate records
### stale, and only the seat's own discipline caught it.

### ### ### **THIS FILE ADDS THE SECOND HALF: ### EVERY GATE WHOSE SUBJECT IS THE FACE MUST CARRY THE
### ### ### SHA256 OF THE BYTES IT READ, AND THAT DIGEST MUST EQUAL THE FACE ABOUT TO BE LOCKED.**
### A gate with no stamp is ### **REFUSED, NOT WAVED THROUGH** -- an absent claim is not a true one.

### ### **AND IT IS FIXTURED IN BOTH POLARITIES BEFORE IT IS TRUSTED**, on all three failure modes:
### a missing pass phrase, ### **A STALE SUBJECT DIGEST**, and a missing stamp. ### Each must refuse,
### and each must refuse ### **FOR THAT GATE** ### rather than merely refuse.
### ### **IT WRITES NOTHING AND LOCKS NOTHING.** ### It reports; the caller chains on its exit code.
"""
import io
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import gate_hash   # noqa: E402
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **EVERY PRE-LOCK GATE, ITS PASS PHRASE, AND WHETHER ITS SUBJECT IS THE FACE.**
# ### ### **`subject_is_face` IS THE NEW COLUMN AND IT IS THE WHOLE POINT.** ### A gate that reads the
# ### registration must prove WHICH registration; a gate that reads the ferry or the roster must not
# ### be asked to, because the face is not what it read.
GATES = [
    ('the ferry scan (struck clauses and stems)', '%s_ferry_scan.txt',
     '### VERDICT: ### **0 HIT(S) REPORTED.', False),
    ('the handoff census', '%s_census_stepzero.txt', 'TOTAL MISSING : 0', False),
    ('the faces census', '%s_faces_census_stepzero.txt', 'TOTAL MISSING : 0', False),
    ('the pins, by ls-remote through the roster', '%s_pins_stepzero.txt',
     '### REPOS HARD-FAILING : 0', False),
    ('the registration gate, all its own arms', '%s_reg_gate.txt', 'GATE VERDICT : CLEAR', True),
    ('the banned-term scan on the face', '%s_reg_termscan.txt', 'VERDICT          : CLEAN', True),
    ('the clause spec emitted from the face', '%s_regspec_run.txt',
     'ARTIFACT-COUNT PREDICTIONS FOUND : 0', True),
    ('the satisfiability audit', 'audit_%s_reg_satisfiable.txt', 'JOINTLY SATISFIABLE', True),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def read_gates(act, face, directory=D):
    """### **EVERY GATE'S RECORD, ITS PASS PHRASE, AND -- FOR FACE-SUBJECT GATES -- ITS DIGEST.**"""
    out = []
    for label, pat, phrase, subj in GATES:
        p = os.path.join(directory, pat % act)
        row = dict(gate=label, file=os.path.basename(p), phrase=phrase, subject_is_face=subj,
                   present=False, phrase_ok=False, hash_ok=None, recorded=None, actual=None)
        if not os.path.exists(p):
            row['why'] = 'the gate left no run record'
            out.append(row)
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        row['present'] = True
        row['phrase_ok'] = bool(phrase in txt)
        if subj:
            v, recd, actual = gate_hash.matches(p, face)
            row.update(hash_ok=v, recorded=recd, actual=actual)
        why = ''
        if not row['phrase_ok']:
            why = 'the record does not carry the gate`s own pass phrase'
        elif subj and row['hash_ok'] is None:
            why = ('### **THE RECORD CARRIES NO SUBJECT DIGEST** -- an absent claim is not a true one')
        elif subj and row['hash_ok'] is False:
            why = ('### **THE RECORD WAS WRITTEN AGAINST DIFFERENT BYTES** -- recorded `%s`, the face '
                   'is `%s`' % ((recd or '')[:12], (actual or '')[:12]))
        row['why'] = why
        row['passed'] = bool(row['phrase_ok'] and (not subj or row['hash_ok'] is True))
        out.append(row)
    for r in out:
        r.setdefault('passed', False)
    return out


def verdict(gates):
    return all(g['passed'] for g in gates)


def fixture(verbose=True):
    """### **FOUR POLARITIES, NOT TWO.** ### Clean must permit; and each of the three ways a gate can
    ### be wrong must refuse ### **FOR THAT GATE.**"""
    res, log = {}, []
    face_body = 'the face, as locked' + chr(10)
    modes = (('all gates clean', None),
             ('one gate`s phrase missing', ('phrase', 5)),
             ('### **one gate`s subject digest STALE**', ('stale', 4)),
             ('one gate carries no subject digest', ('nostamp', 6)))
    for label, mode in modes:
        tmp = tempfile.mkdtemp(prefix='b378lg_')
        try:
            face = os.path.join(tmp, 'face.txt')
            io.open(face, 'w', encoding='utf-8', newline=chr(10)).write(face_body)
            for i, (_lbl, pat, phrase, subj) in enumerate(GATES):
                p = os.path.join(tmp, pat % 'bFIX')
                body = 'header line' + chr(10)
                body += ('THE PHRASE IS GONE' if (mode and mode[0] == 'phrase' and i == mode[1])
                         else phrase) + chr(10)
                io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
                if subj:
                    if mode and mode[0] == 'nostamp' and i == mode[1]:
                        pass
                    elif mode and mode[0] == 'stale' and i == mode[1]:
                        other = os.path.join(tmp, 'other.txt')
                        io.open(other, 'w', encoding='utf-8',
                                newline=chr(10)).write('OLDER BYTES' + chr(10))
                        gate_hash.stamp(p, other)
                    else:
                        gate_hash.stamp(p, face)
            gs = read_gates('bFIX', face, tmp)
            v = verdict(gs)
            failing = [g['gate'] for g in gs if not g['passed']]
            res[label] = dict(permits=v, failing=failing)
            line = '      %-42s permits : %-5s   failing : %s' % (label[:42], v, failing or 'none')
            log.append(line)
            if verbose:
                rec(line)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    ok = (res['all gates clean']['permits'] is True
          and all(res[k]['permits'] is False and len(res[k]['failing']) == 1
                  for k in res if k != 'all gates clean'))
    return ok, res


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    act = argv[0] if argv else 'b378'
    face = argv[1] if len(argv) > 1 else os.path.join(
        D, '%s_registration_2026-09-08.txt' % act)
    rec('=' * 100)
    rec('b378 -- STEP ZERO: ### **THE LOCK READS EVERY GATE, AND CHECKS WHAT EACH ONE READ.**')
    rec('=' * 100)
    rec('')
    rec('  ### ### **`b376` PROVED EVERY GATE PASSED. ### IT COULD NOT PROVE WHAT ANY OF THEM PASSED')
    rec('  ### ### ON, AND SAID SO ON ITS OWN FACE.** ### `b377` hit that: a late rewrite of its')
    rec('  ### ### registration left three gate records stale and only the seat caught it.')
    rec('  ### ### ### **THIS GATE CLOSES IT: ### A FACE-SUBJECT GATE MUST CARRY THE SHA256 OF THE')
    rec('  ### ### ### BYTES IT READ, AND THAT DIGEST MUST EQUAL THE FACE ABOUT TO BE LOCKED.**')
    rec('')
    rec('  ### the face : %s' % os.path.basename(face))
    if os.path.exists(face):
        rec('  ### its sha256 : %s' % gate_hash.sha_of(face))
    else:
        rec('  ### ### **THE FACE DOES NOT EXIST. ### REFUSING.**')
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE HELPER`S OWN FIXTURES, BEFORE THE GATE USES IT.')
    rec('-' * 100)
    hok, hlog = gate_hash.self_test(False)
    for ln in hlog:
        rec(ln)
    rec('    ### ### **gate_hash SELF-TEST : %s**' % ('HELD' if hok else '### FAILED'))
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE GATE`S FIXTURES -- FOUR POLARITIES, NOT TWO.')
    rec('-' * 100)
    ok, res = fixture(True)
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('CLEAN PERMITS AND EACH FAILURE MODE REFUSES FOR ITS OWN GATE' if ok
           else '### FAILED -- THE GATE IS NOT TRUSTED'))
    rec('    ### **A GATE THAT HAS ONLY EVER SAID YES IS NOT A GATE**, and a gate that refuses for the')
    rec('    ### wrong reason is not one either.')
    if not (ok and hok):
        rec('    ### REFUSING TO REPORT A VERDICT FROM A GATE THAT FAILS ITS OWN FIXTURES.')
        p = run_clock.write(D, '%s_lockgate_notes' % act, LINES)
        io.open(os.path.join(D, '%s_lockgate.json' % act), 'w', encoding='utf-8',
                newline=chr(10)).write(json.dumps(dict(fixture_ok=False, helper_ok=hok,
                                                       fixture=res, permits=False), indent=1))
        return 2

    rec('')
    rec('-' * 100)
    rec('  ### (3) EVERY PRE-LOCK GATE OF `%s`, ITS VERDICT, AND WHAT IT READ.' % act)
    rec('-' * 100)
    gates = read_gates(act, face)
    for g in gates:
        rec('    %-46s %-38s %s'
            % (g['gate'][:46], g['file'][:38], 'PASS' if g['passed'] else '### FAIL ###'))
        rec('        looked for   : %s' % g['phrase'])
        if g['subject_is_face']:
            rec('        subject      : ### **THE FACE** ### -- recorded `%s`'
                % ((g['recorded'] or 'NONE')[:16]))
        else:
            rec('        subject      : not the face; no digest required')
        if not g['passed']:
            rec('        ### ### **%s**' % (g['why'] or 'the phrase is not there'))
    v = verdict(gates)
    nface = sum(1 for g in gates if g['subject_is_face'])
    rec('')
    rec('    ### ### **GATES READ : %d. ### PASSING : %d. ### FACE-SUBJECT GATES CHECKED BY DIGEST : '
        '%d.**' % (len(gates), sum(1 for g in gates if g['passed']), nface))
    rec('    ### ### **VERDICT : %s**' % ('LOCK PERMITTED' if v else '### LOCK REFUSED ###'))
    rec('    ### ### **AND THE LOCK IS CHAINED ON THIS EXIT CODE, NOT ON ANY ONE GATE`S.**')
    rec('=' * 100)
    p = run_clock.write(D, '%s_lockgate_notes' % act, LINES)
    io.open(os.path.join(D, '%s_lockgate.json' % act), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(
                dict(act=act, face=os.path.basename(face), face_sha=gate_hash.sha_of(face),
                     helper_ok=hok, fixture_ok=ok, fixture=res, gates=gates,
                     gates_read=len(gates), gates_passing=sum(1 for g in gates if g['passed']),
                     face_subject_gates=nface, permits=v, run_file=os.path.basename(p),
                     run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if v else 1


if __name__ == '__main__':
    sys.exit(main())
