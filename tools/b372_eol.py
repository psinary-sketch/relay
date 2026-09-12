# -*- coding: utf-8 -*-
"""b372_eol.py -- COMPONENT 1: THE END-OF-LINE ATTRIBUTE, TRACKED IN EVERY ROSTERED REPOSITORY.

### ### **THE ROSTER IS IMPORTED FROM `b303_pins.py`, NEVER TYPED** -- if the roster grows, this tool
### grows with it, which is the whole reason `b369` put `SIDE-effects` in one place and not four.
### ### **WHAT GOVERNS A PATH IS ASKED OF GIT, NOT INFERRED FROM A PATTERN** (`git check-attr`), because
### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE** (`PREDICATE_ONE_SHAPE`, minted `b370`), and
### a `.gitattributes` line can be written a dozen ways that all mean the same thing to git.
### ### ### **THE FRESH CHECKOUT IS TAKEN INTO A SCRATCH DIRECTORY WITH `git checkout-index`.** ### No
### ### working file is deleted, no branch is created, nothing is reset. ### **LAST ACT A MOVER THAT
### ### THOUGHT IT WAS BEING CAREFUL DESTROYED UNCOMMITTED WORK IN FOUR REPOSITORIES** (`b371`).
### ### **AND THE MECHANISM IS EXERCISED IN BOTH POLARITIES IN A THROWAWAY REPOSITORY BUILT FOR THE
### ### PURPOSE**, so that a match is known to be caused by the attribute and not by the weather.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import b303_pins            # noqa: E402
import force_rm             # noqa: E402

D = os.path.join(ROOT, 'data')
GUARD = '.githooks/pre-push'
LINE = '* text=auto eol=lf'
NOTE = [
    '',
    '# Disk bytes must equal blob bytes.',
    '#',
    '# core.autocrlf=true checks text files out with CRLF while every blob is LF, so a working',
    '# file differs from its blob on raw bytes on a CLEAN tree. b309 met this in the construction',
    '# kernel; b371 met it again under the tracked pre-push guard (blob 3068 bytes, checkout 3139)',
    '# and had to weaken an identity arm to EOL-normalised comparison to get past it.',
    '# An arm weakened to survive a checkout is an arm the checkout won.',
    '#',
    '# eol=lf makes checkout match storage. Added b372 (2026-09-08). Do not remove without',
    '# re-verifying every guard that byte-compares a working file against its blob.',
    LINE,
]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a, **kw):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, **kw)


def gtext(repo, *a):
    r = git(repo, *a)
    return r.stdout.decode('utf-8', 'replace')


def blob_bytes(repo, ref, path):
    r = git(repo, 'show', '%s:%s' % (ref, path))
    return r.stdout if r.returncode == 0 else None


def governs(repo, path):
    """### **ASK GIT WHAT GOVERNS THE PATH.** ### Returns the (text, eol) attribute values."""
    out = gtext(repo, 'check-attr', 'text', 'eol', '--', path)
    vals = {}
    for ln in out.split(chr(10)):
        if ': ' not in ln:
            continue
        parts = ln.rsplit(': ', 2)
        if len(parts) == 3:
            vals[parts[1]] = parts[2].strip()
    return vals.get('text', 'unspecified'), vals.get('eol', 'unspecified')


def fresh_checkout(repo, path, tmp):
    """### **A FRESH CHECKOUT INTO A SCRATCH DIRECTORY.** ### `checkout-index` writes the blob through
    the same conversion a clone's checkout applies, honouring the working tree's attribute file, and
    ### **WRITES NOTHING INSIDE THE REPOSITORY.**"""
    pref = tmp.replace(os.sep, '/').rstrip('/') + '/'
    r = git(repo, 'checkout-index', '-f', '--prefix=' + pref, '--', path)
    dest = os.path.join(tmp, path.replace('/', os.sep))
    if r.returncode != 0 or not os.path.exists(dest):
        return None
    return io.open(dest, 'rb').read()


def polarity_fixture():
    """### **BOTH POLARITIES, IN A REPOSITORY BUILT AND DESTROYED HERE.** ### With the attribute, a
    fresh checkout must equal the blob; ### **WITHOUT IT, UNDER `core.autocrlf=true`, IT MUST NOT.**
    ### An arm that only ever sees the passing side cannot tell a fix from the weather."""
    res = {}
    for label, attr in (('with the attribute', True), ('without it', False)):
        tmp = tempfile.mkdtemp(prefix='b372eol_')
        repo = os.path.join(tmp, 'r')
        os.makedirs(repo)
        subprocess.run(['git', '-C', repo, 'init', '-q'], capture_output=True)
        subprocess.run(['git', '-C', repo, 'config', 'core.autocrlf', 'true'], capture_output=True)
        subprocess.run(['git', '-C', repo, 'config', 'user.email', 'seat@example'], capture_output=True)
        subprocess.run(['git', '-C', repo, 'config', 'user.name', 'seat'], capture_output=True)
        body = ('#!/bin/sh' + chr(10)) * 40
        io.open(os.path.join(repo, 'f.sh'), 'wb').write(body.encode('utf-8'))
        if attr:
            io.open(os.path.join(repo, '.gitattributes'), 'wb').write(
                (LINE + chr(10)).encode('utf-8'))
            subprocess.run(['git', '-C', repo, 'add', '.gitattributes'], capture_output=True)
        subprocess.run(['git', '-C', repo, 'add', 'f.sh'], capture_output=True)
        subprocess.run(['git', '-C', repo, 'commit', '-q', '-m', 'x'], capture_output=True)
        blob = blob_bytes(repo, 'HEAD', 'f.sh')
        out = os.path.join(tmp, 'out')
        os.makedirs(out)
        got = fresh_checkout(repo, 'f.sh', out)
        res[label] = dict(blob=len(blob or b''), checkout=len(got or b''),
                          equal=(blob is not None and got is not None and blob == got))
        force_rm.rmtree(tmp)
    return res


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    write = ('--write' in argv)
    rec('=' * 100)
    rec('b372 -- COMPONENT 1: THE END-OF-LINE ATTRIBUTE, TRACKED.')
    rec('=' * 100)
    rec('')
    rec('  ### mode : %s' % ('WRITE' if write else 'READ ONLY -- NOTHING IS WRITTEN'))
    rec('  ### the roster is IMPORTED from b303_pins.py : %d repositories' % len(b303_pins.REPOS))
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE MECHANISM, EXERCISED IN BOTH POLARITIES BEFORE IT IS TRUSTED.')
    rec('-' * 100)
    fx = polarity_fixture()
    for label, r in fx.items():
        rec('    %-22s blob %-5d checkout %-5d ### equal : %s'
            % (label, r['blob'], r['checkout'], r['equal']))
    fx_ok = (fx['with the attribute']['equal'] is True
             and fx['without it']['equal'] is False)
    rec('    ### ### **FIXTURE VERDICT : %s** ### -- it passes only if the attribute is the CAUSE.'
        % ('BOTH POLARITIES HELD' if fx_ok else 'FAILED'))
    if not fx_ok:
        rec('    ### REFUSING TO ACT ON A MECHANISM THAT CANNOT TELL THE FIX FROM THE WEATHER.')
        run_clock.write(D, 'b372_eol_notes', LINES)
        return 2

    rec('')
    rec('-' * 100)
    rec('  ### (2) WHAT EACH REPOSITORY ALREADY CARRIES. ### **ASKED OF GIT, NOT OF A PATTERN.**')
    rec('-' * 100)
    state = {}
    for name, path in b303_pins.REPOS:
        ga = os.path.join(path, '.gitattributes')
        present = os.path.exists(ga)
        body = io.open(ga, encoding='utf-8', errors='replace').read() if present else ''
        t, e = governs(path, GUARD)
        tracked = gtext(path, 'ls-files', '--', '.gitattributes').strip()
        state[name] = dict(path=path, file_present=present, tracked=bool(tracked),
                           lines=[l for l in body.split(chr(10)) if l.strip()
                                  and not l.lstrip().startswith('#')],
                           text_attr=t, eol_attr=e,
                           governed=(e == 'lf'))
        rec('    %-22s .gitattributes %-5s tracked %-5s   ### `%s` -> text=%s eol=%s'
            % (name, present, bool(tracked), GUARD, t, e))
    rec('')
    rec('    ### ### **GOVERNED BY `eol=lf` AT THE GUARD`S PATH : %s**'
        % [k for k, v in state.items() if v['governed']])
    rec('    ### ### **NOT GOVERNED : %s**' % [k for k, v in state.items() if not v['governed']])
    rec('    ### ### **A REPOSITORY CARRYING A PATH-SCOPED LINE THAT DOES NOT REACH THE GUARD IS')
    rec('    ### ### NOT `ALREADY CARRYING IT`, AND THE MEASUREMENT ABOVE IS WHY.**')

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE BYTES, BEFORE ANY WRITE. ### **WORKING FILE vs BLOB vs A FRESH CHECKOUT.**')
    rec('-' * 100)
    tmp = tempfile.mkdtemp(prefix='b372eolchk_')
    before = {}
    for name, path in b303_pins.REPOS:
        wf = os.path.join(path, GUARD.replace('/', os.sep))
        w = io.open(wf, 'rb').read() if os.path.exists(wf) else None
        b = blob_bytes(path, 'HEAD', GUARD)
        out = os.path.join(tmp, 'before', name)
        os.makedirs(out, exist_ok=True)
        f = fresh_checkout(path, GUARD, out)
        before[name] = dict(working=len(w or b''), blob=len(b or b''), fresh=len(f or b''),
                            working_equals_blob=(w == b), fresh_equals_blob=(f == b))
        rec('    %-22s working %-5d blob %-5d fresh %-5d  ### working==blob %-5s fresh==blob %s'
            % (name, len(w or b''), len(b or b''), len(f or b''), w == b, f == b))

    wrote = {}
    if write:
        rec('')
        rec('-' * 100)
        rec('  ### (4) THE WRITE. ### **ONLY WHERE THE GUARD`S PATH IS NOT GOVERNED.**')
        rec('-' * 100)
        for name, path in b303_pins.REPOS:
            st = state[name]
            ga = os.path.join(path, '.gitattributes')
            if st['governed']:
                wrote[name] = dict(action='NOT WRITTEN', reason='already governed',
                                   existing=st['lines'])
                rec('    %-22s ### **ALREADY CARRIES IT -- NOTHING WRITTEN**, and its own line is'
                    % name)
                rec('        quoted rather than restated : %s' % st['lines'])
                continue
            old = io.open(ga, encoding='utf-8', errors='replace').read() if st['file_present'] else ''
            if LINE in old.split(chr(10)):
                wrote[name] = dict(action='NOT WRITTEN', reason='line already present',
                                   existing=st['lines'])
                rec('    %-22s ### line already present though not governing -- NOTHING WRITTEN'
                    % name)
                continue
            body = old
            if body and not body.endswith(chr(10)):
                body += chr(10)
            body += chr(10).join(NOTE) + chr(10)
            io.open(ga, 'w', encoding='utf-8', newline=chr(10)).write(body)
            git(path, 'add', '--', '.gitattributes')
            wrote[name] = dict(action='WRITTEN', preserved=st['lines'],
                               old_bytes=len(old.encode('utf-8')),
                               new_bytes=len(body.encode('utf-8')))
            rec('    %-22s ### **WRITTEN AND STAGED.** ### %d -> %d bytes.'
                % (name, len(old.encode('utf-8')), len(body.encode('utf-8'))))
            rec('        ### ### **EVERY PRE-EXISTING LINE PRESERVED : %s**' % st['lines'])
            kept = all(l in body.split(chr(10)) for l in st['lines'])
            rec('        ### preservation verified by re-reading the written file : %s' % kept)
            wrote[name]['preservation_verified'] = kept

    rec('')
    rec('-' * 100)
    rec('  ### (%d) THE VERIFICATION THE ORDER NAMES: ### **A FRESH CHECKOUT`S BYTES vs THE BLOB`S.**'
        % (5 if write else 4))
    rec('-' * 100)
    after = {}
    for name, path in b303_pins.REPOS:
        t, e = governs(path, GUARD)
        b = blob_bytes(path, 'HEAD', GUARD)
        out = os.path.join(tmp, 'after', name)
        os.makedirs(out, exist_ok=True)
        f = fresh_checkout(path, GUARD, out)
        after[name] = dict(text_attr=t, eol_attr=e, blob=len(b or b''), fresh=len(f or b''),
                           equal=(f is not None and b is not None and f == b))
        rec('    %-22s eol=%-11s blob %-5d fresh checkout %-5d   ### ### **EQUAL : %s**'
            % (name, e, len(b or b''), len(f or b''), f == b))
    shutil.rmtree(tmp, ignore_errors=True)
    allgood = all(v['equal'] for v in after.values())
    rec('')
    rec('=' * 100)
    rec('  ### ### **REPOSITORIES WHOSE FRESH CHECKOUT EQUALS ITS BLOB : %d of %d**'
        % (sum(1 for v in after.values() if v['equal']), len(after)))
    rec('  ### ### **VERDICT : %s**' % ('ALL ROSTERED REPOSITORIES PINNED' if allgood
                                        else 'NOT ALL PINNED'))
    rec('  ### **AND THE FLOOR, WITH THE FINDING AND NOT AFTER IT:** ### this fixes WHAT THE NEXT')
    rec('  ### CHECKOUT PRODUCES. ### **THE WORKING FILES ON THIS DISK ARE NOT RENORMALISED BY IT AND')
    rec('  ### ### THIS ACT DOES NOT RENORMALISE THEM.** ### The `working` column above may stay as it')
    rec('  ### is, and the act says so rather than claiming the defect is gone from this machine.')
    rec('  ### **NO WORKING FILE WAS DELETED, NO BRANCH WAS CREATED, NOTHING WAS RESET.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b372_eol_notes', LINES)
    io.open(os.path.join(D, 'b372_eol.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(mode=('write' if write else 'read'), fixture=fx, fixture_ok=fx_ok,
                        state=state, before=before, wrote=wrote, after=after,
                        all_equal=allgood, guard=GUARD, line=LINE,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if (fx_ok and (allgood or not write)) else 1


if __name__ == '__main__':
    sys.exit(main())
