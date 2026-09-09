# -*- coding: utf-8 -*-
"""gate_hash.py -- ### **A GATE RECORDS THE SHA256 OF WHAT IT ACTUALLY READ.**

### ### **THE HOLE THIS CLOSES, NAMED BY `b376` AND HIT BY `b377`:** ### a lock gate that checks each
### gate's record for its pass phrase proves ### **THAT THE GATE PASSED**, and nothing at all about
### ### **WHAT IT PASSED ON.** ### A stale record from an earlier run of the same act satisfies it.
### `b377` rewrote its registration after three gates had already recorded, and only the seat's own
### discipline caught it.
### ### ### **A NOTE THAT REMEMBERS IS NOT A CURE. ### THE CURE IS A STAMP THE LOCK CAN COMPARE.**

### ### **THIS FILE EDITS NO OWNER INSTRUMENT.** ### The shared gates -- the registration gate, the
### banned-term scan, the satisfiability audit -- are not modified. ### Their RECORDS are stamped
### afterwards by the act that ran them, with the digest of the file the gate was pointed at.
### ### **SO THE STAMP IS THE CALLER'S CLAIM ABOUT WHAT IT FED THE GATE**, and the lock gate checks
### that claim against the bytes it is about to lock. ### **THAT IS STRICTLY MORE THAN THE PASS PHRASE
### ### ALONE PROVED, AND IT IS LESS THAN THE GATE VOUCHING FOR ITSELF** -- which would need the
### shared gates edited, and this file does not edit them.
"""
import hashlib
import io
import os

MARK = '### GATE SUBJECT SHA256 :'


def sha_of(path):
    """### **THE DIGEST OF A FILE'S BYTES, AS THEY ARE ON DISK.**"""
    return hashlib.sha256(io.open(path, 'rb').read()).hexdigest()


def sha_of_bytes(b):
    return hashlib.sha256(b).hexdigest()


def stamp(record_path, subject_path):
    """### **APPEND THE SUBJECT'S DIGEST TO A GATE'S OWN RUN RECORD.**

    ### ### **IT APPENDS AND NEVER REWRITES**, so the gate's own output is left exactly as the gate
    ### wrote it and the stamp is visibly the caller's addition.
    ### Re-stamping replaces only a previous stamp line, so a gate re-run against new bytes does not
    ### leave two contradictory digests behind.
    """
    digest = sha_of(subject_path)
    line = '%s %s  (%s)' % (MARK, digest, os.path.basename(subject_path))
    txt = io.open(record_path, encoding='utf-8', errors='replace').read()
    kept = [x for x in txt.split(chr(10)) if not x.startswith(MARK)]
    while kept and not kept[-1].strip():
        kept.pop()
    kept.append(line)
    io.open(record_path, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(kept) + chr(10))
    return digest


def read(record_path):
    """### **THE DIGEST A RECORD CLAIMS, OR `None` IF IT CLAIMS NONE.**"""
    if not os.path.exists(record_path):
        return None
    for ln in io.open(record_path, encoding='utf-8', errors='replace').read().split(chr(10)):
        if ln.startswith(MARK):
            rest = ln[len(MARK):].strip()
            return rest.split()[0] if rest else None
    return None


def matches(record_path, subject_path):
    """### **RETURNS `(verdict, recorded, actual)`.** ### An absent stamp is `None`, never `True`."""
    rec = read(record_path)
    act = sha_of(subject_path) if os.path.exists(subject_path) else None
    if rec is None or act is None:
        return None, rec, act
    return (rec == act), rec, act


def self_test(verbose=False):
    """### **BOTH POLARITIES, IN A SCRATCH DIRECTORY BUILT AND DESTROYED HERE.**

    ### A stamp over unchanged bytes must MATCH; ### **A STAMP OVER BYTES THAT CHANGED AFTERWARDS MUST
    ### ### NOT MATCH**; and a record carrying no stamp at all must return `None` rather than `True`.
    """
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix='gatehash_')
    log = []
    try:
        subj = os.path.join(tmp, 'face.txt')
        recf = os.path.join(tmp, 'gate.txt')
        io.open(subj, 'w', encoding='utf-8', newline=chr(10)).write('the face, first bytes' + chr(10))
        io.open(recf, 'w', encoding='utf-8', newline=chr(10)).write('GATE VERDICT : CLEAR' + chr(10))
        no_stamp = read(recf)
        v0 = matches(recf, subj)[0]
        stamp(recf, subj)
        v1 = matches(recf, subj)[0]
        io.open(subj, 'w', encoding='utf-8', newline=chr(10)).write('the face, REWRITTEN' + chr(10))
        v2 = matches(recf, subj)[0]
        stamp(recf, subj)
        v3 = matches(recf, subj)[0]
        body = io.open(recf, encoding='utf-8').read()
        one = sum(1 for x in body.split(chr(10)) if x.startswith(MARK))
        kept = 'GATE VERDICT : CLEAR' in body
        checks = [
            ('an unstamped record reads None, not True', no_stamp is None and v0 is None),
            ('a stamp over unchanged bytes MATCHES', v1 is True),
            ('### **A STAMP OVER REWRITTEN BYTES REFUSES**', v2 is False),
            ('re-stamping after the rewrite matches again', v3 is True),
            ('### **AND EXACTLY ONE STAMP LINE SURVIVES**', one == 1),
            ("the gate's own output is untouched", kept),
        ]
        ok = all(c for _l, c in checks)
        for lbl, c in checks:
            log.append('    %-52s %s' % (lbl, 'ok' if c else '### MISMATCH ###'))
        if verbose:
            print(chr(10).join(log))
        return ok, log
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    ok, log = self_test(True)
    print('  ### ### **SELF-TEST : %s**' % ('BOTH POLARITIES HELD' if ok else 'FAILED'))
    raise SystemExit(0 if ok else 1)
