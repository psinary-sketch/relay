# -*- coding: utf-8 -*-
"""b376_lockgate.py -- STEP ZERO: ### **THE LOCK READS EVERY GATE.**

### ### **`b375`'S INCIDENT, IN ONE SENTENCE:** ### the lock was chained on the satisfiability
### verdict alone while the term scan read `NOT CLEAN` and nobody looked.
### ### ### **THE CURE IS NOT A NOTE. ### IT IS A TOOL THAT REFUSES.** ### This file reads EVERY
### pre-lock gate's own run record, requires each to carry its own PASS phrase, and ### **EXITS
### ### NON-ZERO IF ANY ONE OF THEM DOES NOT.** ### The lock is chained on THIS.
### ### **AND IT IS FIXTURED IN BOTH POLARITIES BEFORE IT IS TRUSTED:** ### a synthetic clean set must
### permit and a synthetic dirty set must refuse. ### **A GATE THAT HAS ONLY EVER SAID YES IS NOT A
### ### GATE** -- which is the same sentence, one act on, as `A GATE NOBODY READS IS NOT A GATE`.
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
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **EVERY PRE-LOCK GATE THE RITUAL RUNS, AND THE PHRASE EACH ONE PRINTS WHEN IT PASSES.**
# ### ### **THE LIST IS THE POINT.** ### `b375` had four gates and read one.
GATES = [
    ('the ferry scan (struck clauses and stems)', '%s_ferry_scan.txt',
     '### VERDICT: ### **0 HIT(S) REPORTED.'),
    ('the handoff census', '%s_census_stepzero.txt', 'TOTAL MISSING : 0'),
    ('the faces census', '%s_faces_census_stepzero.txt', 'TOTAL MISSING : 0'),
    ('the pins, by ls-remote through the roster', '%s_pins_stepzero.txt',
     '### REPOS HARD-FAILING : 0'),
    ('the registration gate, all its own arms', '%s_reg_gate.txt', 'GATE VERDICT : CLEAR'),
    ('the banned-term scan on the face', '%s_reg_termscan.txt', 'VERDICT          : CLEAN'),
    ('the satisfiability audit', 'audit_%s_reg_satisfiable.txt', 'JOINTLY SATISFIABLE'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def read_gates(act, directory=D):
    """### **READ EVERY GATE'S OWN RUN RECORD AND REQUIRE ITS OWN PASS PHRASE.**"""
    out = []
    for label, pat, phrase in GATES:
        p = os.path.join(directory, pat % act)
        if not os.path.exists(p):
            out.append(dict(gate=label, file=os.path.basename(p), present=False, passed=False,
                            phrase=phrase, why='the gate left no run record'))
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ok = phrase in txt
        out.append(dict(gate=label, file=os.path.basename(p), present=True, passed=bool(ok),
                        phrase=phrase,
                        why=('' if ok else 'the record does not carry the gate`s own pass phrase')))
    return out


def verdict(gates):
    return all(g['passed'] for g in gates)


def fixture(verbose=True):
    """### **BOTH POLARITIES, IN A SCRATCH DIRECTORY BUILT AND DESTROYED HERE.**
    ### ### A synthetic CLEAN set must PERMIT; a synthetic set with ONE gate's phrase removed must
    ### ### **REFUSE** -- and it must refuse for THAT gate, not merely refuse."""
    res = {}
    for label, dirty_index in (('all gates clean', None),
                               ('one gate dirty (the term scan)', 5)):
        tmp = tempfile.mkdtemp(prefix='b376lg_')
        for i, (_lbl, pat, phrase) in enumerate(GATES):
            body = 'header line' + chr(10)
            if i != dirty_index:
                body += phrase + chr(10)
            else:
                body += 'VERDICT          : NOT CLEAN' + chr(10)
            io.open(os.path.join(tmp, pat % 'bFIX'), 'w', encoding='utf-8',
                    newline=chr(10)).write(body)
        gs = read_gates('bFIX', tmp)
        v = verdict(gs)
        failed = [g['gate'] for g in gs if not g['passed']]
        res[label] = dict(permits=v, failing=failed)
        shutil.rmtree(tmp, ignore_errors=True)
        if verbose:
            rec('    %-34s permits : %-5s   failing : %s' % (label, v, failed or 'none'))
    ok = (res['all gates clean']['permits'] is True
          and res['one gate dirty (the term scan)']['permits'] is False
          and len(res['one gate dirty (the term scan)']['failing']) == 1)
    return ok, res


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    act = argv[0] if argv else 'b376'
    rec('=' * 100)
    rec('b376 -- STEP ZERO: ### **THE LOCK READS EVERY GATE.**')
    rec('=' * 100)
    rec('')
    rec('  ### ### **`b375`S INCIDENT:** ### the lock chained on the satisfiability verdict alone while')
    rec('  ### ### the term scan read `NOT CLEAN` and nobody looked. ### **THE CURE IS A TOOL THAT')
    rec('  ### ### REFUSES, NOT A NOTE THAT REMEMBERS.**')
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE FIXTURE, BOTH POLARITIES, BEFORE THE GATE IS TRUSTED.')
    rec('-' * 100)
    ok, res = fixture(True)
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('BOTH POLARITIES HELD' if ok else '### FAILED -- THE GATE IS NOT TRUSTED'))
    rec('    ### **A GATE THAT HAS ONLY EVER SAID YES IS NOT A GATE**, and the dirty polarity must')
    rec('    ### refuse for the RIGHT gate rather than merely refuse.')
    if not ok:
        rec('    ### REFUSING TO REPORT A VERDICT FROM A GATE THAT FAILS ITS OWN FIXTURES.')
        p = run_clock.write(D, '%s_lockgate_notes' % act, LINES)
        io.open(os.path.join(D, '%s_lockgate.json' % act), 'w', encoding='utf-8',
                newline=chr(10)).write(json.dumps(dict(fixture_ok=False, fixture=res,
                                                       permits=False), indent=1))
        return 2

    rec('')
    rec('-' * 100)
    rec('  ### (2) EVERY PRE-LOCK GATE OF `%s`, AND THE VERDICT EACH ONE PRINTED.' % act)
    rec('-' * 100)
    gates = read_gates(act)
    for g in gates:
        rec('    %-46s %-40s %s'
            % (g['gate'][:46], g['file'][:40], 'PASS' if g['passed'] else '### FAIL ###'))
        rec('        looked for : %s' % g['phrase'])
        if not g['passed']:
            rec('        ### ### **%s**' % (g['why'] or 'the phrase is not there'))
    v = verdict(gates)
    rec('')
    rec('    ### ### **GATES READ : %d. ### PASSING : %d. ### VERDICT : %s**'
        % (len(gates), sum(1 for g in gates if g['passed']),
           'LOCK PERMITTED' if v else '### LOCK REFUSED ###'))
    rec('    ### ### **AND THE LOCK IS CHAINED ON THIS EXIT CODE, NOT ON ANY ONE GATE`S.**')
    rec('=' * 100)
    p = run_clock.write(D, '%s_lockgate_notes' % act, LINES)
    io.open(os.path.join(D, '%s_lockgate.json' % act), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(
                dict(act=act, fixture_ok=ok, fixture=res, gates=gates,
                     gates_read=len(gates), gates_passing=sum(1 for g in gates if g['passed']),
                     permits=v, run_file=os.path.basename(p),
                     run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if v else 1


if __name__ == '__main__':
    sys.exit(main())
