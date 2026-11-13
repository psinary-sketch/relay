# -*- coding: utf-8 -*-
"""standing/seatfile.py -- THE SEAT'S FILE, (R364)(3)(i) with (3)(xviii), (3)(xix) and amendment row 3 (5) (data/b754_amendments.json).

A file CLAUDE.md at the relay's root, written by this tool and edited by no hand, under 200 lines, tracked; and the same file at the seat's
project settings folder (the folder .claude beside the relay, one level up), the author's word for that one write outside the repositories.
For each kind of the hook's table (tools/standing/hook.py ROWS, :61-:89) the refused form and the form to send in its place; the restatement
rule of (xviii); the step zero after a change of (xix); the paths of the ruling and ferry bank and of the standing clauses. No identifier of
the author and no path under the user's profile is written: the user's settings folder is printed by its name alone.

  python -X utf8 -u tools/standing/seatfile.py places     the places, each by name and size (a file that stands is read and its matter kept)
  python -X utf8 -u tools/standing/seatfile.py write      compose, refuse where a kind of the hook's table has no form, write both places
  python -X utf8 -u tools/standing/seatfile.py arm        the file's kinds against the hook's table; the two copies compared
  python -X utf8 -u tools/standing/seatfile.py control    the controls: every kind present; a planted kind absent, the arm failing;
                                                          a planted difference between the copies, the arm failing
"""
import hashlib
import io
import json
import os
import re
import sys
import tempfile

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
NAME = 'CLAUDE.md'
MAX_LINES = 200
MARK_OPEN = '<!-- seatfile: the lines below are written by tools/standing/seatfile.py; edited by no hand -->'
MARK_CLOSE = '<!-- seatfile: end -->'
if S not in sys.path:
    sys.path.insert(0, S)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def places():
    """(name, path, printable) for each place (R364)(3)(i) names: the relay's root, its project settings folder, the seat's project settings
    folder beside the relay (amendment row 3 (5)), the user's settings folder (printed by name, never by path)."""
    home = os.path.expanduser('~')
    return (('the relay`s root', os.path.join(RELAY, NAME), 'relay/' + NAME),
            ('the relay`s project settings folder', os.path.join(RELAY, '.claude', NAME), 'relay/.claude/' + NAME),
            ('the seat`s project settings folder', os.path.join(os.path.dirname(RELAY), '.claude', NAME), os.path.join(os.path.dirname(RELAY), '.claude', NAME).replace('\\', '/')),
            ('the user`s settings folder', os.path.join(home, '.claude', NAME), 'the user`s settings folder/' + NAME))


TARGETS = (0, 2)   # ### the two places written: the relay's root (tracked) and the seat's project settings folder (row 3 (5))


def stands(path):
    try:
        st = os.stat(path)
        return st.st_size
    except OSError:
        return None


def kept_matter(path):
    """the matter of a file that stands, outside this tool's marks (kept above the tool's block); '' where none stands."""
    if stands(path) is None:
        return ''
    t = io.open(path, encoding='utf-8').read().replace('\r', '')
    if MARK_OPEN in t:
        head = t.split(MARK_OPEN, 1)[0]
        tail = t.split(MARK_CLOSE, 1)[1] if MARK_CLOSE in t else ''
        return (head.rstrip(NL) + (NL + tail.strip(NL) if tail.strip() else '')).strip(NL)
    return t.strip(NL)


# ### the form to send in place of each refused form, one per kind of hook.ROWS; a kind of the table with no form here refuses the write
FORMS = {
    'READ': ('a Read with no limit (a short file included), a limit above 200, or a limit with no offset', 'an offset and a limit of at most 200 on every Read'),
    'PIPE': ('a pipe outside quotes in a shell command, `2>&1 |` and a listing included', 'the search tool (Grep, with head_limit), the Read tool, or a scratch script that prints'),
    'REDIR': ('a redirect of any stream outside quotes (`>`, `>>`, `2>/dev/null`, `2>&1`, `*>`)', 'a scratch script that opens and writes its own file; stderr is captured as it is'),
    'ENV': ('a command opening with an assignment (`NAME=value cmd`, `env NAME=`, `$env:NAME =`)', 'none: the environment left as it is, a value passed as an argument'),
    'REMOTE': ('more than one ls-remote in one command', 'one remote read per command; a retry is an event of the act'),
    'SUITE': ('two suite parts, or a part and a combine, in one call', 'one suite part or combine per call, each its own message'),
    'ORDER': ('a branch delete before the citation check has run', 'the citation check first, then each delete by the one-call tool, one per message'),
    'POSTSEAL': ('after the seal, a shell filter or redirect over the entry or the trail', 'the Read tool, with an offset and a limit'),
    'GITWRITE': ('a second git write in one message, any repository, parallel calls included', 'one git write per message: `commit.py <relay|pp> add <paths>` in one message, the commit in the next'),
    'LOCKED': ('a rewrite after the lock of a bank written before it', 'the next act`s bank or the post-seal events bank; the sealed bank stands'),
    'INPLACE': ('an in-place edit by the shell (sed -i, perl -i, Set-Content, Add-Content, Clear-Content)', 'the Edit or Write tool; a rendered file by its render re-run'),
    'SUBJECT': ('a gate, lock or seal commit by the shell, or a subject the tool did not compose', '`commit.py <relay|pp> <gate|lock|seal>`, the subject composed from its bank'),
    'BACKGROUND': ('a suite part or combine sent in the background', 'the foreground with the 600 s limit, each part after its predecessor`s bank'),
    'SED': ('sed in any form, a read included', 'the Read tool, or `tools/standing/peek.py`'),
    'HASHED': ('an Edit or Write of a bank its tool wrote (named in data/<act>_bank_hashes.json)', 'the bank`s own tool run again'),
    'ROWID': ('a PLACE-papers commit adding a ledger row whose ID the file already holds', 'the ID allocated from the file`s maximum over every table of the prefix (tools/standing/rowid.py)'),
    'PLAINGIT': ('a git write by plain git (add, commit, checkout, branch, push, tag)', '`python -X utf8 -u tools/standing/commit.py` with add, restore, delete, branch or the phase and its words'),
    'BYDESIGN': ('an Edit or Write after the lock of a file written after it by design (answers pair, author-words banks, post-lock scans, post-seal events)', 'each by its own tool: `record answers`, tools/standing/append.py, the one-call tool`s scan'),
    'WLIST': ('a Write or Edit of a tracked path outside the (W) list, or with the list absent or stale', '`python -X utf8 -u tools/standing/wlist.py bank <act>` after every amendment row and every change of the worklist`s W_WORDS (the entries a ruling gives in words, each with its clause); write within the list'),
    'COMPOSER': ('a question put to the author that `rootprompt.py put` did not compose and bank', '`python -X utf8 -u tools/standing/rootprompt.py put <act> <json>` first, then the question as banked'),
    'LIMIT': ('a route of tools/standing/limits.py`s table in the foreground with no timeout or one beneath its limit', 'the timeout `tools/standing/limits.py` prints for that route'),
}


def hook_kinds():
    import hook as H
    return list(H.ROWS)


def _clauses():
    """the standing clauses bank of the highest version the relay holds (data/standing_clauses_v<N>.txt)."""
    vs = sorted((int(m.group(1)), f) for f in os.listdir(D) for m in [re.match(r'^standing_clauses_v(\d+)\.txt$', f)] if m)
    return 'data/' + vs[-1][1] if vs else 'data/standing_clauses_v9.txt'


def compose(kinds=None):
    """the tool's block: its lines, or SystemExit naming each kind of the table with no form (nothing written)."""
    kinds = list(kinds if kinds is not None else hook_kinds())
    missing = [k for k in kinds if k not in FORMS]
    if missing:
        sys.exit('### THE HOOK`S TABLE HOLDS %d KIND(S) WITH NO FORM IN tools/standing/seatfile.py FORMS: %s -- NOTHING WRITTEN' % (len(missing), ', '.join(missing)))
    L = [MARK_OPEN,
         '# THE SEAT`S FILE',
         '',
         'Read at every start and after every summary. Written by `tools/standing/seatfile.py write` from the hook`s own table',
         '(tools/standing/hook.py ROWS); edited by no hand. The act is the one `data/act_current.json` names.',
         '',
         '## The paths',
         '- the relay: this folder; PLACE-papers and the kernels: at the places the ferry`s PATHS line gives',
         '- the ruling and the ferry: `data/<act>_ferry.txt`; the amendments: `data/<act>_amendments.json`',
         '- the standing clauses: `%s`; the readfirst bank: `data/<act>_readfirst.txt`' % _clauses(),
         '- the act`s banks: `data/<act>_stepzero.txt`, `_events.txt`, `_defects.txt`, `_hook_refusals.txt`, `_steps.json`',
         '- the one-call tool: `tools/standing/commit.py`; the hook: `tools/standing/hook.py`; the (W) list: `data/<act>_wlist.json`',
         '',
         '## The hook`s %d kinds: the refused form, and the form to send in its place' % len(kinds)]
    for k in kinds:
        refused, send = FORMS[k]
        L.append('- %s -- refused: %s. Send: %s.' % (k, refused, send))
    L += ['',
          '## The rules beside the hook',
          '- a commit`s words carry no semicolon; the one-call tool composes `<act> <phase>: <words>`',
          '- one git write per message across every repository; the add in one message, the commit in the next',
          '- a question to the author: through the composer (`rootprompt.py put`), never typed straight',
          '- a long run: the limit `tools/standing/limits.py` prints; no suite part in the background',
          '- the restart flag, the free memory (hold 2,560 MB) and both volumes (floor 5,000 MB) read before each route and commit',
          '- no identifier of the author, and no path under the user`s profile, in anything the act writes',
          '- a passed item`s write beyond the (W) list: `amend.py pass <item> <word_at> <word_cite> <paths> --write` before the write ((R364)(3)(xvi));',
          '  a shared tool committed by any other route: `amend.py shared` read before its commit',
          '',
          '## The restatement ((R364)(3)(xviii))',
          'After a summary of the session or a change of model, and before any write: read whole, from the banks that hold them, the',
          'ruling and the ferry, the author`s words since, and the step-zero, events, defects and refusals banks; then state in ten lines',
          'or fewer where the act stands, the next write and the rules that bind it, and what the act does not do. The chain read`s',
          'boundary rule (`tools/standing/chain.py`) says whether a summary stands.',
          '',
          '## The step zero after a change ((R364)(3)(xix))',
          'After a change of session, of the harness`s version or of a store`s place: each standing instrument that reads the session,',
          'the transcript or the state folder runs its positive control before the act`s opening write (`chain.py control <session>`,',
          '`hold.py control`, `hook.py control`, `harness.py control <session>`); the hook`s state stands in the state folder on the data',
          'volume (`tools/standing/statedir.py`), read by the hook and the one-call tool alike.',
          MARK_CLOSE]
    return L


def body_of(path):
    """the tool's block of a written file, or None."""
    if stands(path) is None:
        return None
    t = io.open(path, encoding='utf-8').read().replace('\r', '')
    if MARK_OPEN not in t or MARK_CLOSE not in t:
        return None
    return MARK_OPEN + t.split(MARK_OPEN, 1)[1].split(MARK_CLOSE, 1)[0] + MARK_CLOSE


def file_kinds(text):
    return [m.group(1) for m in re.finditer(r'(?m)^- ([A-Z]+) -- refused: ', text or '')]


def arm(table=None, paths=None):
    """(ok, lines): the file's kinds against the hook's table, at each written place; the two copies' blocks compared (row 3 (5))."""
    table = list(table if table is not None else hook_kinds())
    paths = list(paths if paths is not None else [places()[i][1] for i in TARGETS])
    L, ok = [], True
    bodies = []
    for p in paths:
        b = body_of(p)
        bodies.append(b)
        if b is None:
            L.append('  %s: NO BLOCK OF THE TOOL -- FAILS' % (os.path.basename(os.path.dirname(p)) + '/' + NAME))
            ok = False
            continue
        fk = file_kinds(b)
        lacking = [k for k in table if k not in fk]
        extra = [k for k in fk if k not in table]
        n = len(b.split(NL))
        good = not lacking and not extra and n <= MAX_LINES
        ok = ok and good
        L.append('  %s: KINDS %d OF THE TABLE`S %d ; LACKING %s ; NOT IN THE TABLE %s ; LINES %d (cap %d) -- %s' % (
            os.path.basename(os.path.dirname(p)) + '/' + NAME, len([k for k in table if k in fk]), len(table), lacking or 'none', extra or 'none', n, MAX_LINES, 'PASSES' if good else 'FAILS'))
    if len(bodies) >= 2:
        same = all(b is not None for b in bodies) and len(set(bodies)) == 1
        ok = ok and same
        L.append('  THE COPIES: %s (sha256 %s)' % ('EQUAL' if same else 'DIFFERENT -- FAILS', ', '.join(hashlib.sha256((b or '').encode('utf-8')).hexdigest()[:12] for b in bodies)))
    return ok, L


def cmd_places():
    for name, path, shown in places():
        n = stands(path)
        print('  %s: %s -- %s' % (name, shown, 'ABSENT' if n is None else 'STANDS, %d bytes%s' % (n, '' if body_of(path) else ', NOT THE TOOL`S: its matter kept above the block')))


def cmd_write():
    cmd_places()
    block = compose()
    for i in TARGETS:
        name, path, shown = places()[i]
        keep = kept_matter(path)
        text = ((keep + NL + NL) if keep else '') + NL.join(block) + NL
        if len(text.split(NL)) - 1 > MAX_LINES:
            sys.exit('### %s: %d LINES OVER THE CAP %d -- NOTHING WRITTEN' % (shown, len(text.split(NL)) - 1, MAX_LINES))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + '.seatfile.tmp'
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write(text)
        os.replace(tmp, path)
        print('  written %s: %d lines, %d bytes, sha256 %s%s' % (shown, len(text.split(NL)) - 1, len(text.encode('utf-8')),
                                                                hashlib.sha256(text.encode('utf-8')).hexdigest()[:16], ', the matter that stood kept above' if keep else ''))
    ok, L = arm()
    print(NL.join(L))
    print('  THE ARM: %s' % ('PASSES' if ok else 'FAILS'))


def control():
    """(ok, lines): (1) every kind of the table in the file at both places; (2) a planted kind added to the table and absent from the file,
    the arm failing; (3) a planted difference between the copies (a scratch copy, one character changed), the arm failing."""
    import shutil
    out, good, n = [], 0, 0
    tab = hook_kinds()
    ok1, L1 = arm()
    n += 1
    good += ok1
    out += ['  (1) every kind of the table (%d) in the file at both places, the copies equal: %s' % (len(tab), 'AS WANTED' if ok1 else 'NOT AS WANTED')] + ['    ' + l for l in L1]
    ok2, L2 = arm(table=tab + ['PLANTEDKIND'])
    n += 1
    good += (not ok2)
    out += ['  (2) a planted kind PLANTEDKIND in the table, absent from the file: the arm %s -- %s' % ('FAILS' if not ok2 else 'PASSES', 'AS WANTED' if not ok2 else 'NOT AS WANTED')] + ['    ' + l for l in L2]
    d = tempfile.mkdtemp(prefix='seatfile_ctl_')
    try:
        a, b = os.path.join(d, 'a', NAME), os.path.join(d, 'b', NAME)
        for src, dst in ((places()[TARGETS[0]][1], a), (places()[TARGETS[1]][1], b)):
            os.makedirs(os.path.dirname(dst))
            shutil.copyfile(src, dst)
        t = io.open(b, encoding='utf-8').read()
        io.open(b, 'w', encoding='utf-8', newline='\n').write(t.replace('Send: ', 'Send:  ', 1))
        ok3, L3 = arm(paths=[a, b])
    finally:
        shutil.rmtree(d, ignore_errors=True)
    n += 1
    good += (not ok3)
    out += ['  (3) a planted difference between the copies (one space added in a scratch copy): the arm %s -- %s' % ('FAILS' if not ok3 else 'PASSES', 'AS WANTED' if not ok3 else 'NOT AS WANTED')] + ['    ' + l for l in L3]
    out.append('  ### THE SEAT`S FILE: CONTROLS %d OF %d AS WANTED' % (good, n))
    return good == n, out


def main(argv):
    if not argv or argv[0] not in ('places', 'write', 'arm', 'control'):
        sys.exit(__doc__)
    if argv[0] == 'places':
        cmd_places()
    elif argv[0] == 'write':
        cmd_write()
    elif argv[0] == 'arm':
        ok, L = arm()
        print(NL.join(L))
        print('  THE ARM: %s' % ('PASSES' if ok else 'FAILS'))
    else:
        ok, L = control()
        print(NL.join(L))


if __name__ == '__main__':
    main(sys.argv[1:])
