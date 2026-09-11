# -*- coding: utf-8 -*-
"""repair_snapshot.py -- A REPAIRED TOOL RUNS FIRST AGAINST A CAPTURED SNAPSHOT. ### (b417, Addition One.)

### ### **THE SPECIES:** ### A BROKEN TOOL IS SAFE BY BEING BROKEN. ### A dormant instrument that dies on a
### retired path writes nothing; repairing it can activate a hazard its breakage was masking. ### `b416`
### repaired `b371_hookpath.py`, and the first run after the repair re-wrote a prior act's record.

### ### **WHAT THIS DOES, IN TWO PHASES, AND THE SECOND ONLY AFTER THE FIRST:**
###   ### **SNAPSHOT** -- the relay tool tree is copied into a scratch sandbox and the tool is run FROM
###     THE SANDBOX, so every write it makes relative to its own root lands in the copy. ### Every file of
###     the sandbox is hashed before and after; ### **AND EVERY LIVE PATH THE TOOL CAN REACH BY AN
###     ABSOLUTE PATH IS CAPTURED TOO** -- relay's `tools/` and `data/` and `.githooks/`, and in each
###     rostered repository its `.githooks/`, its `.git/hooks/`, its refs, its status and its object count.
###     ### A write inside the sandbox is CONTAINED; a write to a live path is ESCAPED, and each escaped
###     file is restored from the bytes captured before the run -- or NAMED, where no bytes can restore it.
###   ### **LIVE** -- the tool runs where it lives, with the same capture, and every change the caller did
###     not PERMIT is restored and counted: ### *modified / restored / still differing*.

### ### **THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:**
### ### (1) ### **IT SEES ONLY WHAT IT WATCHES.** ### A write to a path outside the watch set is invisible to
###     it. ### The watch set is printed with every result.
### ### (2) ### **RELAY'S `data/` IS WATCHED BY SIZE AND MTIME, NOT BY BYTES** -- it holds thousands of
###     records. ### A changed data file is restored from `git HEAD` only if git called it clean before the
###     run; otherwise it is NAMED UNRESTORABLE, never guessed at.
### ### (3) ### **AN OBJECT WRITTEN INTO A REPOSITORY'S STORE IS COUNTED, NOT COLLECTED.** ### Deleting
###     objects is not a restore, it is a second write, and this tool does not make it.
### ### (4) ### **THE SANDBOX DOES NOT STOP A TOOL THAT RUNS ANOTHER TOOL BY AN ABSOLUTE PATH** -- it only
###     makes that escape visible. ### That is the point: the hazard is measured, not prevented.
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def _roster():
    """### THE ROSTER IS READ FROM `b304_hooks.py`, THE ONE PLACE IT IS KEPT -- never retyped here."""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    try:
        import b304_hooks
        return list(b304_hooks.REPOS)
    except Exception:
        return [('relay', ROOT)]


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def files_bytes(d):
    """### EVERY FILE UNDER `d`, BY ITS BYTES. ### For small trees: hook directories and the sandbox."""
    out = {}
    if not os.path.isdir(d):
        return out
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x not in ('.git', '__pycache__')]
        for f in files:
            p = os.path.join(root, f)
            try:
                out[os.path.relpath(p, d)] = open(p, 'rb').read()
            except Exception:
                out[os.path.relpath(p, d)] = None
    return out


def files_stat(d):
    """### EVERY FILE UNDER `d`, BY SIZE AND MTIME. ### For the large trees -- limit (2)."""
    out = {}
    if not os.path.isdir(d):
        return out
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x not in ('.git', '__pycache__')]
        for f in files:
            p = os.path.join(root, f)
            try:
                st = os.stat(p)
                out[os.path.relpath(p, d)] = (st.st_size, st.st_mtime_ns)
            except Exception:
                pass
    return out


def git_state(repo):
    if not os.path.isdir(os.path.join(repo, '.git')):
        return None
    co = dict(ln.split(': ', 1) for ln in _git(repo, 'count-objects', '-v').splitlines() if ': ' in ln)
    return {'head': _git(repo, 'rev-parse', 'HEAD'),
            'branch': _git(repo, 'rev-parse', '--abbrev-ref', 'HEAD'),
            'refs': _git(repo, 'for-each-ref', '--format=%(refname) %(objectname)'),
            'status': _git(repo, 'status', '--porcelain'),
            'loose': int(co.get('count', '0'))}


def capture(relay_root, roster):
    """### THE LIVE WATCH SET. ### Printed with every result, per limit (1)."""
    cap = {'relay_tools': files_bytes(os.path.join(relay_root, 'tools')),
           'relay_githooks': files_bytes(os.path.join(relay_root, '.githooks')),
           'relay_data': files_stat(os.path.join(relay_root, 'data')),
           'relay_data_clean': set(),
           'repos': {}}
    st = _git(relay_root, 'status', '--porcelain', '--', 'data')
    dirty = set(ln[3:].strip().strip('"').replace('/', os.sep)[len('data' + os.sep):]
                for ln in st.splitlines() if ln.strip())
    cap['relay_data_clean'] = set(cap['relay_data']) - dirty
    for name, path in roster:
        cap['repos'][name] = {'path': path,
                              'githooks': files_bytes(os.path.join(path, '.githooks')),
                              'githooks_dir': files_bytes(os.path.join(path, '.git', 'hooks')),
                              'git': git_state(path)}
    return cap


def _diff_bytes(a, b):
    mod = sorted(k for k in a if k in b and a[k] != b[k])
    new = sorted(k for k in b if k not in a)
    gone = sorted(k for k in a if k not in b)
    return mod, new, gone


def diff_live(before, after):
    """### RETURN A LIST OF `(where, kind, path)` CHANGES ACROSS THE WHOLE WATCH SET."""
    ch = []
    for key, label in (('relay_tools', 'relay/tools'), ('relay_githooks', 'relay/.githooks')):
        m, n, g = _diff_bytes(before[key], after[key])
        ch += [(label, 'modified', p) for p in m] + [(label, 'created', p) for p in n] + \
              [(label, 'deleted', p) for p in g]
    m, n, g = _diff_bytes(before['relay_data'], after['relay_data'])
    ch += [('relay/data', 'modified', p) for p in m] + [('relay/data', 'created', p) for p in n] + \
          [('relay/data', 'deleted', p) for p in g]
    for name, rb in before['repos'].items():
        ra = after['repos'][name]
        for key, label in (('githooks', '.githooks'), ('githooks_dir', '.git/hooks')):
            m, n, g = _diff_bytes(rb[key], ra[key])
            ch += [('%s/%s' % (name, label), 'modified', p) for p in m] + \
                  [('%s/%s' % (name, label), 'created', p) for p in n] + \
                  [('%s/%s' % (name, label), 'deleted', p) for p in g]
        gb, ga = rb['git'], ra['git']
        if gb and ga:
            for k in ('head', 'branch', 'refs', 'status'):
                if gb[k] != ga[k]:
                    ch.append(('%s/git' % name, 'changed', k))
            if gb['loose'] != ga['loose']:
                ch.append(('%s/git' % name, 'objects', '%+d loose object(s)' % (ga['loose'] - gb['loose'])))
    return ch


def restore(before, changes, relay_root, permit=()):
    """### RESTORE EVERY CHANGED FILE NOT IN `permit`. ### RETURN `(restored, unrestorable, permitted)`."""
    restored, unrest, permitted = [], [], []
    for where, kind, p in changes:
        tag = '%s/%s' % (where, p)
        if any(tag.endswith(x) or p == x for x in permit):
            permitted.append((where, kind, p))
            continue
        if where in ('relay/tools', 'relay/.githooks'):
            base = os.path.join(relay_root, 'tools' if where == 'relay/tools' else '.githooks')
            key = 'relay_tools' if where == 'relay/tools' else 'relay_githooks'
            full = os.path.join(base, p)
            if kind == 'created':
                os.remove(full)
            elif before[key].get(p) is not None:
                open(full, 'wb').write(before[key][p])
            restored.append((where, kind, p))
        elif where == 'relay/data':
            full = os.path.join(relay_root, 'data', p)
            if kind == 'created':
                os.remove(full)
                restored.append((where, kind, p))
            elif p in before['relay_data_clean']:
                blob = subprocess.run(['git', '-C', relay_root, 'show',
                                       'HEAD:data/' + p.replace(os.sep, '/')], capture_output=True)
                if blob.returncode == 0:
                    open(full, 'wb').write(blob.stdout)
                    restored.append((where, kind, p))
                else:
                    unrest.append((where, kind, p))
            else:
                unrest.append((where, kind, p))
        elif where.endswith('/.githooks') or where.endswith('/.git/hooks'):
            name = where.split('/')[0]
            rec = before['repos'][name]
            key = 'githooks' if where.endswith('/.githooks') else 'githooks_dir'
            base = os.path.join(rec['path'], '.githooks' if key == 'githooks' else os.path.join('.git', 'hooks'))
            full = os.path.join(base, p)
            if kind == 'created':
                os.remove(full)
            elif rec[key].get(p) is not None:
                open(full, 'wb').write(rec[key][p])
            restored.append((where, kind, p))
        else:
            # ### git refs, status and objects: counted and named, never rewritten -- limit (3).
            unrest.append((where, kind, p))
    return restored, unrest, permitted


def make_sandbox(relay_root, with_data=()):
    sb = tempfile.mkdtemp(prefix='repair_snapshot_')
    shutil.copytree(os.path.join(relay_root, 'tools'), os.path.join(sb, 'tools'),
                    ignore=shutil.ignore_patterns('__pycache__'))
    if os.path.isdir(os.path.join(relay_root, '.githooks')):
        shutil.copytree(os.path.join(relay_root, '.githooks'), os.path.join(sb, '.githooks'))
    os.makedirs(os.path.join(sb, 'data'))
    for rel in with_data:
        src = os.path.join(relay_root, rel)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(os.path.join(sb, rel)), exist_ok=True)
            shutil.copy2(src, os.path.join(sb, rel))
    return sb


def run_tool(path, args=(), timeout=900):
    r = subprocess.run([sys.executable, path] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, r.stdout or '', r.stderr or ''


def snapshot(tool_rel, relay_root=ROOT, roster=None, with_data=(), args=()):
    """### PHASE ONE. ### Returns a result dict; writes nothing outside the sandbox that it does not restore."""
    roster = roster if roster is not None else _roster()
    sb = make_sandbox(relay_root, with_data)
    sb_before = files_bytes(sb)
    live_before = capture(relay_root, roster)
    rc, out, err = run_tool(os.path.join(sb, tool_rel), args)
    live_after = capture(relay_root, roster)
    sb_after = files_bytes(sb)
    m, n, g = _diff_bytes(sb_before, sb_after)
    contained = [('sandbox', 'modified', p) for p in m] + [('sandbox', 'created', p) for p in n] + \
                [('sandbox', 'deleted', p) for p in g]
    escaped = diff_live(live_before, live_after)
    restored, unrest, _p = restore(live_before, escaped, relay_root)
    still = diff_live(live_before, capture(relay_root, roster))
    still_files = [c for c in still if c[0] not in [x for x in ('%s/git' % nm for nm, _ in roster)]]
    shutil.rmtree(sb, ignore_errors=True)
    return dict(phase='SNAPSHOT', tool=tool_rel, rc=rc, stdout=out, stderr=err,
                contained=contained, escaped=escaped, restored=restored, named=unrest,
                still_files=still_files, watch=watch_set(relay_root, roster))


def _data_restored_ok(relay_root, p):
    """### **REPAIRED b417, AFTER ITS FIRST LIVE USE.** ### A data file restored from `HEAD` has a NEW
    ### mtime by construction, so a size-and-mtime compare after the restore reports it differing
    ### EVERY TIME. ### b417's live run printed `2` still differing on files whose bytes equalled the
    ### blob. ### The restore is now verified the way it was made: ### **BYTES AGAINST THE BLOB.**"""
    blob = subprocess.run(['git', '-C', relay_root, 'show', 'HEAD:data/' + p.replace(os.sep, '/')],
                          capture_output=True)
    try:
        return blob.returncode == 0 and open(os.path.join(relay_root, 'data', p), 'rb').read() == blob.stdout
    except Exception:
        return False


def live(tool_rel, relay_root=ROOT, roster=None, permit=(), args=()):
    """### PHASE TWO. ### The tool runs where it lives; every change not PERMITTED is restored."""
    roster = roster if roster is not None else _roster()
    before = capture(relay_root, roster)
    rc, out, err = run_tool(os.path.join(relay_root, tool_rel), args)
    changes = diff_live(before, capture(relay_root, roster))
    restored, unrest, permitted = restore(before, changes, relay_root, permit)
    still = diff_live(before, capture(relay_root, roster))
    still_files = [c for c in still if not c[0].endswith('/git')
                   and not any(('%s/%s' % (c[0], c[2])).endswith(x) or c[2] == x for x in permit)
                   and not (c[0] == 'relay/data' and c[1] == 'modified'
                            and ('relay/data', 'modified', c[2]) in restored
                            and _data_restored_ok(relay_root, c[2]))]
    return dict(phase='LIVE', tool=tool_rel, rc=rc, stdout=out, stderr=err, changes=changes,
                restored=restored, named=unrest, permitted=permitted, still_files=still_files,
                watch=watch_set(relay_root, roster))


def watch_set(relay_root, roster):
    w = ['relay/tools (bytes)', 'relay/.githooks (bytes)', 'relay/data (size+mtime)']
    for name, _p in roster:
        w.append('%s: .githooks, .git/hooks (bytes); refs, status, loose objects' % name)
    return w


def report(res):
    """### THE RESULT AS LINES. ### Every list printed in full; nothing summarised away."""
    L = ['### PHASE : %s   ### TOOL : %s   ### EXIT : %d' % (res['phase'], res['tool'], res['rc'])]
    err = [x for x in res['stderr'].splitlines() if x.strip()]
    L.append('  last stderr line : %s' % (err[-1][:110] if err else '(none)'))
    L.append('  watch set : ' + '; '.join(res['watch']))
    if res['phase'] == 'SNAPSHOT':
        L.append('  ### ### **CONTAINED WRITES (inside the sandbox, discarded) : %d**' % len(res['contained']))
        L += ['      %-9s %s' % (k, p) for _w, k, p in res['contained']]
        L.append('  ### ### **ESCAPED WRITES (live paths outside the sandbox) : %d**' % len(res['escaped']))
    else:
        L.append('  ### ### **CHANGES ACROSS THE WATCH SET : %d**' % len(res['changes']))
        L.append('  permitted and left : %d' % len(res['permitted']))
    L += ['      %-26s %-9s %s' % (w, k, p) for w, k, p in (res['escaped'] if res['phase'] == 'SNAPSHOT'
                                                         else res['changes'])]
    L.append('  ### ### **RESTORED FROM CAPTURED BYTES : %d**' % len(res['restored']))
    L.append('  ### ### **NAMED, NOT RESTORABLE BY BYTES : %d**' % len(res['named']))
    L += ['      %-26s %-9s %s' % (w, k, p) for w, k, p in res['named']]
    L.append('  ### ### **FILES STILL DIFFERING AFTER THE RESTORE : %d**' % len(res['still_files']))
    L += ['      %-26s %-9s %s' % (w, k, p) for w, k, p in res['still_files']]
    return L


def self_test(verbose=True):
    """### BOTH POLARITIES, ON TOY TOOLS IN A TOY RELAY. ### **A GUARD THAT HAS ONLY EVER SAID CONTAINED
    ### IS NOT A GUARD.** ### The toy relay is a temp directory; the toy live path is another."""
    ok = True
    toy = tempfile.mkdtemp(prefix='rs_toyrelay_')
    far = tempfile.mkdtemp(prefix='rs_toylive_')
    os.makedirs(os.path.join(toy, 'tools'))
    os.makedirs(os.path.join(toy, 'data'))
    os.makedirs(os.path.join(far, '.githooks'))
    open(os.path.join(far, '.githooks', 'pre-push'), 'wb').write(b'#!/bin/sh\nexit 0\n')
    body_in = ("import os\nR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n"
               "open(os.path.join(R,'data','out.txt'),'w').write('x')\n")
    body_out = ("open(%r,'wb').write(b'CLOBBERED')\n"
                % os.path.join(far, '.githooks', 'pre-push'))
    open(os.path.join(toy, 'tools', 'toy_in.py'), 'w').write(body_in)
    open(os.path.join(toy, 'tools', 'toy_out.py'), 'w').write(body_out)
    roster = [('toylive', far)]
    a = snapshot(os.path.join('tools', 'toy_in.py'), relay_root=toy, roster=roster)
    c1 = (len(a['contained']) == 1 and not a['escaped'])
    b = snapshot(os.path.join('tools', 'toy_out.py'), relay_root=toy, roster=roster)
    c2 = (len(b['escaped']) == 1 and len(b['restored']) == 1 and not b['still_files']
          and open(os.path.join(far, '.githooks', 'pre-push'), 'rb').read() == b'#!/bin/sh\nexit 0\n')
    c = live(os.path.join('tools', 'toy_in.py'), relay_root=toy, roster=roster)
    c3 = (len(c['changes']) == 1 and len(c['restored']) == 1 and not c['still_files']
          and not os.path.exists(os.path.join(toy, 'data', 'out.txt')))
    for lbl, v in (('a tool writing only inside its root is CONTAINED, 0 escaped', c1),
                   ('### a tool writing a live path is ESCAPED and RESTORED, 0 still differing', c2),
                   ('a live run`s unpermitted write is restored, 0 still differing', c3)):
        ok = ok and v
        if verbose:
            print('    %-76s %s' % (lbl, 'PASS' if v else '### FAIL ###'))
    shutil.rmtree(toy, ignore_errors=True)
    shutil.rmtree(far, ignore_errors=True)
    return ok


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        print('repair_snapshot.py -- SELF-TEST, BOTH POLARITIES')
        sys.exit(0 if self_test() else 1)
    print(__doc__)
